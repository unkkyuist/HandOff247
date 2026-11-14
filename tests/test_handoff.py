"""End-to-end and unit tests. Run: python -m unittest discover -s tests"""
from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from handoff247 import notes as notes_mod  # noqa: E402
from handoff247.build import write_pack  # noqa: E402
from handoff247.cli import main  # noqa: E402
from handoff247.lexer import lex  # noqa: E402
from handoff247.pipeline import analyze_project  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "mini"


def copy_fixture(tmp: Path) -> Path:
    """Copy outside any Git work tree so the plain directory walk is exercised too."""
    dst = tmp / "mini"
    shutil.copytree(FIXTURE, dst)
    return dst


class LexerTests(unittest.TestCase):
    def test_csharp_strings_and_comments_are_blanked(self):
        src = 'var a = @"C:\\x ""q"""; // "list" => no\nvar b = $"{x} {(y ? "a" : "b")}"; var c = """ "raw" """;\nreal();'
        lx = lex(src, "csharp")
        self.assertNotIn("list", lx.code)
        self.assertNotIn("raw", lx.code)
        self.assertIn("real()", lx.code)
        self.assertEqual(len(lx.code), len(src))
        self.assertEqual(lx.code.count("\n"), src.count("\n"))
        self.assertIn('C:\\x ""q""', [s for s, _, _ in lx.strings])

    def test_js_regex_and_template(self):
        src = "const r = /a'b\"c/g; const t = `x ${f('y')} z`; call('k');"
        lx = lex(src, "javascript")
        self.assertIn("call(", lx.code)
        self.assertIn("k", [s for s, _, _ in lx.strings])


class AnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        cls.root = copy_fixture(cls.tmp)
        cls.p = analyze_project(cls.root, "Mini")
        cls.L = cls.p.links

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_modes(self):
        modes = {m["name"]: m for m in self.L["modes"]}
        self.assertEqual(set(modes), {"cli", "mcp", "serve", "server"})
        self.assertTrue(modes["serve"]["default"])
        self.assertIn("Operations.Execute", modes["cli"]["tables"])
        self.assertIn("MCP over stdio", modes["mcp"]["transports"])
        self.assertIn("McpTools", modes["mcp"]["uses"])

    def test_dispatch_table_and_handlers(self):
        (table,) = self.L["tables"]
        ops = {o["key"]: o for o in table["ops"]}
        self.assertEqual(set(ops), {"list", "get", "notes.add", "notes.count", "notes.size", "info"})
        self.assertEqual((ops["list"]["handler_type"], ops["list"]["handler_file"]), ("Store", "Store.cs"))
        self.assertEqual((ops["notes.add"]["handler_type"], ops["notes.add"]["handler_file"]), ("Notes", "Notes.cs"))
        self.assertEqual(ops["notes.size"]["handler_method"], "Count")
        self.assertEqual(ops["info"]["handler_file"], "")      # inline expression, not guessed

    def test_routes_forward_to_table(self):
        routes = {(r["verb"], r["path"]): r for r in self.L["routes"]}
        self.assertEqual(routes[("POST", "/api/{operation}")]["forwards_to"], "Operations.Execute")
        self.assertEqual(set(routes[("GET", "/health")]["modes"]), {"serve", "server"})

    def test_mcp_tools(self):
        tools = {t["name"]: t for t in self.L["mcp_tools"]}
        self.assertEqual(set(tools), {"list", "add_note", "record_get"})
        self.assertEqual(tools["add_note"]["op"], "notes.add")
        self.assertEqual(tools["record_get"]["name_source"], "attribute")
        self.assertEqual(tools["list"]["description"], "List records. Returns [{id}] items.")
        self.assertEqual(self.L["mcp_clients"][0]["mode"], "mcp")
        self.assertEqual(self.L["mcp_clients"][0]["target"], "Mini.csproj")

    def test_callers_and_channels(self):
        by = {(c["file"], c["func"]): c for c in self.L["consumers"]}
        app = by[("wwwroot/app.js", "api")]
        self.assertEqual((app["channel"], app["route"]), ("http", "POST /api/{operation}"))
        self.assertNotIn("inferred", app)
        panel = by[("wwwroot/panel.js", "api")]
        self.assertEqual(panel["channel"], "http")
        self.assertIn("inferred", panel)                       # parameter, so only an inference
        smoke = by[("scripts/smoke.py", "cli")]
        self.assertEqual((smoke["channel"], smoke["mode"]), ("process", "cli"))
        self.assertEqual(by[("McpTools.cs", "Call")]["channel"], "in-process")
        self.assertNotIn("fake", {k for c in self.L["consumers"] for k in c["keys"]})

    def test_launch_chain(self):
        runs = {(e.src, e.dst, e.label) for e in self.p.edges if e.kind == "runs"}
        self.assertIn(("START.cmd", "run.ps1", "serve"), runs)
        self.assertIn("run.ps1", {s for s, d, _ in runs if d == "Mini.csproj"})
        self.assertEqual(list(self.L["launchers"])[0], "START.cmd")
        urls = [u for l in self.L["launches"] for u in l["urls"]]
        self.assertIn("http://127.0.0.1:5050/", urls)

    def test_environment_and_ports(self):
        env = self.L["env"]
        self.assertTrue(env["APP_HOME"]["reads"] and env["APP_HOME"]["writes"])
        self.assertNotIn("errorlevel", {k.lower() for k in env})
        self.assertIn(5050, {p["port"] for p in self.L["ports"]})
        parts = {p for rp in self.L["runtime_paths"] for p in rp["parts"]}
        self.assertTrue({"mini.db", "store.db"} <= parts)

    def test_code_edges(self):
        kinds = {(e.src, e.dst, e.kind) for e in self.p.edges}
        self.assertIn(("Operations.cs", "Store.cs", "injects"), kinds)
        self.assertIn(("wwwroot/app.js", "wwwroot/panel.js", "imports"), kinds)
        self.assertIn(("wwwroot/index.html", "wwwroot/app.js", "loads"), kinds)
        self.assertIn(("README.md", "scripts/smoke.py", "documents"), kinds)

    def test_comments_extracted(self):
        f = self.p.file("Operations.cs")
        cls = next(s for s in f.symbols if s.name == "Operations" and s.kind == "class")
        self.assertEqual(cls.doc, "Single entry point for every operation the app supports.")
        self.assertEqual(self.p.file("Notes.cs").summary, "")      # comment is not at the top of the file
        self.assertTrue(self.p.file("run.ps1").summary.startswith("Starts the Mini app"))
        self.assertEqual(self.p.file("scripts/smoke.py").summary, "Smoke test: drives the CLI mode against a temporary home.")

    def test_cli_usage_in_docs(self):
        (table,) = self.L["tables"]
        ops = {o["key"]: o for o in table["ops"]}
        self.assertIn("README.md", {d["file"] for d in ops["notes.add"]["documented_in"]})


class PackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.root = copy_fixture(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_build_notes_check_cycle(self):
        out = self.root / "docs" / "handoff"
        self.assertEqual(main(["notes", str(self.root)]), 0)
        notes_file = self.root / "HANDOFF.notes.md"
        text = notes_file.read_text(encoding="utf-8")
        self.assertIn("## File: Program.cs", text)
        self.assertIn("## Mode: cli", text)
        self.assertNotIn("## Translations", text)                  # the fixture is all English
        # a person fills two items
        text = text.replace("## Project\nTODO: What does this project do, who uses it, and what state is it in right now?",
                            "## Project\nRecords for the front desk. Owner: ops team.")
        text = text.replace("## File: Program.cs\nTODO: Role of this file; anything surprising about it.",
                            "## File: Program.cs\nPick the mode here; serve is what people use.")
        notes_file.write_text(text, encoding="utf-8")
        # re-running notes keeps the person's text
        (self.root / "Extra.cs").write_text("namespace Mini; public class Extra {}", encoding="utf-8")
        self.assertEqual(main(["notes", str(self.root)]), 0)
        text2 = notes_file.read_text(encoding="utf-8")
        self.assertIn("Records for the front desk. Owner: ops team.", text2)
        self.assertIn("## File: Extra.cs", text2)
        self.assertEqual(text2.count("## File: Program.cs"), 1)

        self.assertEqual(main(["build", str(self.root), "-o", str(out), "--date", "2026-01-01"]), 0)
        for name in ("README.md", "RUNNING.md", "CONNECTIONS.md", "CODEMAP.md", "FILES.md", "index.html",
                     "handoff.json", "diagrams/system.mmd", "diagrams/operations.mmd", "diagrams/startup.mmd"):
            self.assertTrue((out / name).is_file(), name)
        readme = (out / "README.md").read_text(encoding="utf-8")
        self.assertIn("Records for the front desk", readme)
        self.assertIn("](../../Program.cs)", readme)                 # relative links inside the project
        files_md = (out / "FILES.md").read_text(encoding="utf-8")
        self.assertIn("Pick the mode here; serve is what people use.", files_md)
        data = json.loads((out / "handoff.json").read_text(encoding="utf-8"))
        self.assertEqual(data["generator"], "HandOff247")
        self.assertNotIn(str(self.tmp), (out / "handoff.json").read_text(encoding="utf-8"))
        html = (out / "index.html").read_text(encoding="utf-8")
        self.assertIn('"README.md"', html)
        self.assertNotIn("__DATA__", html)
        # second build must not analyze its own previous output
        p2 = analyze_project(self.root)
        self.assertFalse(any(f.path.startswith("docs/handoff/") for f in p2.files))
        # check: 1 of N files documented -> below a 50% bar
        self.assertEqual(main(["check", str(self.root), "--min", "50"]), 1)
        self.assertEqual(main(["check", str(self.root)]), 0)

    def test_handoffignore(self):
        (self.root / ".handoffignore").write_text("scripts/\n*.css\n", encoding="utf-8")
        p = analyze_project(self.root)
        paths = {f.path for f in p.files}
        self.assertNotIn("scripts/smoke.py", paths)
        self.assertNotIn("wwwroot/style.css", paths)
        self.assertIn("wwwroot/app.js", paths)

    def test_python_dispatch_needs_callables(self):
        (self.root / "tool.py").write_text(
            "import handlers\n"
            "def a(): pass\n"
            "def b(): pass\n"
            "TABLE = {'alpha': a, 'beta': b, 'gamma': handlers.gamma}\n"
            "def record(fc, line, table):\n"
            "    return {'file': fc.file, 'line': line, 'table': table}\n", encoding="utf-8")
        p = analyze_project(self.root)
        tables = [t for t in p.links["tables"] if t["file"] == "tool.py"]
        self.assertEqual(len(tables), 1)
        self.assertEqual({o["key"] for o in tables[0]["ops"]}, {"alpha", "beta", "gamma"})

    def test_notes_parse_is_lossless_for_existing_text(self):
        n = notes_mod.parse("# t\n\n## Project\nline 1\n\nline 2\n## File: a.py\nTODO: x\n")
        self.assertEqual(n.get("Project"), "line 1\n\nline 2")
        self.assertEqual(n.get("File: a.py"), "")

    def test_translations_cycle(self):
        # source text written in Korean: a leading comment, a doc comment and a Markdown heading
        (self.root / "Ledger.cs").write_text(
            "// 기록을 저장하는 원장.\nnamespace Mini;\n/// <summary>모든 변경을 검증한다.</summary>\n"
            "public class Ledger {}\n", encoding="utf-8")
        (self.root / "GUIDE.md").write_text("# 사용 안내\n\nHow to use it.\n\n## 설치 | 설정\n", encoding="utf-8")
        self.assertEqual(main(["notes", str(self.root)]), 0)
        notes_file = self.root / "HANDOFF.notes.md"
        text = notes_file.read_text(encoding="utf-8")
        self.assertIn("## Translations", text)
        self.assertIn("| 기록을 저장하는 원장. | TODO |", text)
        self.assertIn("| 설치 \\| 설정 | TODO |", text)              # a pipe in the original is escaped
        self.assertNotIn("| Records", text)                         # English text is never listed
        text = (text.replace("| 기록을 저장하는 원장. | TODO |", "| 기록을 저장하는 원장. | The ledger that stores records. |")
                    .replace("| 사용 안내 | TODO |", "| 사용 안내 | User guide |")
                    .replace("| 설치 \\| 설정 | TODO |", "| 설치 \\| 설정 | Install \\| configure |"))
        notes_file.write_text(text, encoding="utf-8")
        # a new Korean comment appears: only its row is added, filled rows stay as written
        (self.root / "Audit.cs").write_text("// 감사 기록.\nnamespace Mini; public class Audit {}\n", encoding="utf-8")
        self.assertEqual(main(["notes", str(self.root)]), 0)
        text2 = notes_file.read_text(encoding="utf-8")
        self.assertIn("| 감사 기록. | TODO |", text2)
        self.assertIn("| 기록을 저장하는 원장. | The ledger that stores records. |", text2)
        self.assertEqual(text2.count("## Translations"), 1)

        out = self.tmp / "pack"
        self.assertEqual(main(["build", str(self.root), "-o", str(out), "--date", "2026-01-01"]), 0)
        files_md = (out / "FILES.md").read_text(encoding="utf-8")
        self.assertIn("> The ledger that stores records.", files_md)
        self.assertIn("translated", files_md)
        self.assertIn("User guide", files_md)
        self.assertIn("Install \\| configure", files_md)             # escaped inside the link label
        self.assertNotIn("기록을 저장하는 원장", files_md)
        self.assertIn("모든 변경을 검증한다", files_md)               # not translated yet, so shown as written
        readme = (out / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Still in another language", readme)
        data = json.loads((out / "handoff.json").read_text(encoding="utf-8"))
        ledger = next(f for f in data["files"] if f["path"] == "Ledger.cs")
        self.assertEqual(ledger["translated"], [{"where": "summary", "original": "기록을 저장하는 원장."}])
        self.assertEqual(set(data["links"]["untranslated"]), {"모든 변경을 검증한다.", "감사 기록."})
        self.assertNotIn("Translations", data["notes"])

    # ---------------------------------------------------------------- handover findings
    def _leaver_script(self):
        self.personal = "C:" + "\\Users\\alice\\exports"           # split so this test file holds no such path itself
        (self.root / "sync.ps1").write_text(
            "# Copy the export to the share.\n"
            "# TODO: stop hard-coding the share name\n"
            f'$target = "{self.personal}"\n'
            "Invoke-WebRequest https://api.partner-billing.com/v2/upload -Headers @{ a = $env:BILLING_API_TOKEN }\n"
            f'$k = "{"AKIA" + "ABCDEFGHIJKLMNOP"}"\n'
            '$fixture = "sk-TEST_ONLY_PRIVATE_PROMPT_7fa299fd"\n', encoding="utf-8")
        (self.root / "pyproject.toml").write_text('[project]\nname = "mini"\nrequires-python = ">=3.11"\n', encoding="utf-8")

    def test_handover_findings(self):
        self._leaver_script()
        lv = analyze_project(self.root).links["leaving"]
        self.assertIn({"file": "sync.ps1", "line": 2, "tag": "TODO", "text": "stop hard-coding the share name"}, lv["todos"])
        personal = [x for x in lv["machine_paths"] if x["user"]]
        self.assertEqual([x["path"] for x in personal], [self.personal])
        self.assertIn("api.partner-billing.com", [h["host"] for h in lv["hosts"] if h["code"]])
        self.assertEqual([(s["file"], s["line"], s["kind"]) for s in lv["secrets"]], [("sync.ps1", 5, "AWS access key id")])
        self.assertIn("BILLING_API_TOKEN", lv["secret_env"])
        self.assertIn(("Python", ">=3.11"), [(x["tool"], x["version"]) for x in lv["prerequisites"]])
        self.assertEqual(lv["git"], {"repo": False})
        self.assertIsNone(lv["local_only"])
        self.assertEqual(lv["has"]["readme"], "README.md")

    def _git(self, cwd, *args):
        import subprocess
        subprocess.run(["git", "-C", str(cwd), "-c", "user.name=T", "-c", "user.email=t@example.com",
                        "-c", "commit.gpgsign=false", *args], check=True, capture_output=True)

    @unittest.skipUnless(shutil.which("git"), "git is not installed")
    def test_git_state_and_files_only_on_this_computer(self):
        (self.root / ".gitignore").write_text(".env\n*.db\nbin/\n", encoding="utf-8")
        self._git(self.root, "init", "-q")
        self._git(self.root, "add", "-A")
        self._git(self.root, "commit", "-q", "-m", "first")
        (self.root / ".env").write_text("X=1\n", encoding="utf-8")
        (self.root / "records.db").write_text("x", encoding="utf-8")
        (self.root / "bin").mkdir()
        (self.root / "bin" / "Mini.dll").write_text("x", encoding="utf-8")
        (self.root / "new.py").write_text("print(1)\n", encoding="utf-8")
        p = analyze_project(self.root)
        lv = p.links["leaving"]
        g = lv["git"]
        self.assertTrue(g["repo"])
        self.assertEqual((g["remotes"], g["uncommitted"], g["unpushed"], g["commits"]), ([], 1, [], 1))
        self.assertEqual(g["authors"][0]["name"], "T")
        self.assertEqual(lv["local_only"], [{"path": ".env", "kind": "settings or secrets"},
                                            {"path": "records.db", "kind": "data"}])      # bin/ is build output
        self.assertNotIn(".env", {f.path for f in p.files})
        out = self.tmp / "pack"
        self.assertEqual(main(["build", str(self.root), "-o", str(out), "--date", "2026-01-01"]), 0)
        page = (out / "HANDOVER.md").read_text(encoding="utf-8")
        self.assertIn("**No remote is configured.**", page)
        self.assertIn("| `.env` | settings or secrets |", page)
        self.assertNotIn("X=1", page)
        rows = {r["key"]: r["state"] for r in json.loads((out / "handoff.json").read_text(encoding="utf-8"))["links"]["readiness"]}
        self.assertEqual((rows["git"], rows["committed"], rows["local"], rows["readme"]), ("todo", "todo", "todo", "ok"))
        self.assertNotIn("pushed", rows)                             # no remote, so there is nothing to compare with

    def test_go_one_project(self):
        self._leaver_script()
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)       # no command = go
        out = self.root / "docs" / "handoff"
        for name in ("README.md", "HANDOVER.md", "index.html", "handoff.json", "diagrams/system.mmd"):
            self.assertTrue((out / name).is_file(), name)
        notes_text = (self.root / "HANDOFF.notes.md").read_text(encoding="utf-8")
        self.assertIn("## Topic: Open work and next steps", notes_text)
        self.assertIn("## Topic: People and contacts", notes_text)
        page = (out / "HANDOVER.md").read_text(encoding="utf-8")
        self.assertIn("## Ready to hand over?", page)
        self.assertIn(f"`{self.personal}`", page)
        self.assertIn("**personal**", page)
        self.assertNotIn("AKIA", page)                               # location and kind only, never the value
        self.assertIn("Handover status:", (out / "README.md").read_text(encoding="utf-8"))
        self.assertIn("'HANDOVER.md', 'Handover'", (out / "index.html").read_text(encoding="utf-8"))
        # answering a question moves the count
        before = notes_mod.load(self.root / "HANDOFF.notes.md")
        self.assertEqual(before.get("Topic: People and contacts"), "")
        (self.root / "HANDOFF.notes.md").write_text(notes_text.replace(
            "## Topic: People and contacts\nTODO", "## Topic: People and contacts\nFront desk lead owns it.\nTODO"), encoding="utf-8")
        self.assertEqual(main(["go", str(self.root), "--date", "2026-01-01"]), 0)
        self.assertIn("Front desk lead owns it.", (out / "HANDOVER.md").read_text(encoding="utf-8"))
        self.assertIn("1/8 answered", (out / "HANDOVER.md").read_text(encoding="utf-8"))

    def test_ontology_graph_and_wiki(self):
        self._leaver_script()
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        out = self.root / "docs" / "handoff"
        onto = json.loads((out / "ontology.json").read_text(encoding="utf-8"))
        ents = {e["id"]: e for e in onto["entities"]}
        rels = {(r["s"], r["p"], r["o"]): r for r in onto["relations"]}
        self.assertEqual(ents["op:list"]["type"], "Operation")
        self.assertIn(("op:list", "handledBy", "file:Store.cs"), rels)
        self.assertIn(("table:Operations.Execute", "hasOperation", "op:notes.add"), rels)
        self.assertTrue(any(p == "calls" and o == "op:list" for _, p, o in rels))
        self.assertTrue(any(p == "invokes" and ents[s]["type"] == "McpTool" for s, p, _ in rels))
        self.assertIn(("mode:cli", "serves", "table:Operations.Execute"), rels)
        self.assertEqual(ents["env:BILLING_API_TOKEN"]["type"], "EnvVar")
        self.assertIn("host:api.partner-billing.com", ents)
        classes = {c["id"] for c in onto["schema"]["classes"]}
        known = {r["id"] for r in onto["schema"]["relations"]}
        for (s, p, o), r in rels.items():                            # nothing dangling, everything observed somewhere
            self.assertIn(s, ents)
            self.assertIn(o, ents)
            self.assertIn(p, known)
            if p not in ("contains", "authored"):
                self.assertTrue(r.get("file"), (s, p, o))
        link = re.compile(r"\]\(([^)\s]+)\)")
        for e in ents.values():
            self.assertIn(e["type"], classes)
            self.assertTrue((out / e["page"]).is_file(), e["id"])
        pages = list((out / "wiki").rglob("*.md"))
        self.assertGreater(len(pages), 20)
        for page in pages + [out / "llms.txt"]:                      # every link of the wiki leads somewhere
            for href in link.findall(page.read_text(encoding="utf-8")):
                if href.startswith(("http:", "https:", "#")):
                    continue
                target = (page.parent / href.split("#")[0].replace("%20", " ")).resolve()
                self.assertTrue(target.exists(), f"{page.name}: {href}")
        full = (out / "llms-full.txt").read_text(encoding="utf-8")
        self.assertIn("<!-- page: wiki/files/Store.cs.md -->", full)
        self.assertNotIn("AKIA", full)
        self.assertNotIn("AKIA", (out / "ontology.json").read_text(encoding="utf-8"))
        viewer = (out / "index.html").read_text(encoding="utf-8")
        self.assertIn("'@graph'", viewer)
        self.assertIn('"wiki/index.md"', viewer)
        # a note written by a person reaches the wiki; stale generated pages go, hand-made pages stay
        notes_file = self.root / "HANDOFF.notes.md"
        notes_file.write_text(notes_file.read_text(encoding="utf-8").replace(
            "## File: Store.cs\nTODO", "## File: Store.cs\nKeeps every record in memory; nothing is saved."), encoding="utf-8")
        stale = out / "wiki" / "files" / "Gone.cs.md"
        stale.write_text("---\ngenerator: HandOff247\n---\n\n# `Gone.cs`\n", encoding="utf-8")
        mine = out / "wiki" / "my-own-page.md"
        mine.write_text("# Written by hand\n", encoding="utf-8")
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        self.assertIn("Keeps every record in memory", (out / "wiki" / "files" / "Store.cs.md").read_text(encoding="utf-8"))
        self.assertFalse(stale.exists())
        self.assertTrue(mine.exists())

    def test_model_summaries(self):
        from handoff247 import summarize
        self._leaver_script()
        notes_file = self.root / "HANDOFF.notes.md"
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        notes_file.write_text(re.sub(r"## File: Store\.cs\nTODO[^\n]*", "## File: Store.cs\nWritten by the owner.",
                                     notes_file.read_text(encoding="utf-8")), encoding="utf-8")
        project = analyze_project(self.root)
        notes = notes_mod.load(notes_file)
        prompts = []

        def fake(prompt):
            prompts.append(prompt)
            ids = re.findall(r"^### id: (\S+)\npath: (\S+)", prompt, re.M)
            items = [{"id": i, "summary": f"Model text for {p}."} for i, p in ids]
            items.append({"id": "nope", "summary": "an id that was never asked for"})
            return json.dumps({"items": items})
        fake.engine = "fake"
        cache = summarize.cache_path(notes_file)
        self.assertEqual(cache.name, "HANDOFF.summaries.json")
        st = summarize.run(project, notes, cache, call=fake, log=lambda m: None, date="2026-01-01")
        self.assertGreater(st["written"], 3)
        self.assertEqual(st["failed"], 0)
        sent = "\n".join(prompts)
        self.assertNotIn("path: Store.cs", sent)                     # the owner's note wins: not asked
        self.assertIn("path: sync.ps1", sent)
        self.assertNotIn("AKIA", sent)                               # key-shaped lines never leave the computer
        self.assertIn("[removed]", sent)
        data = json.loads(cache.read_text(encoding="utf-8"))["files"]
        self.assertNotIn("nope", json.dumps(data))
        self.assertEqual(data["sync.ps1"]["summary"], "Model text for sync.ps1.")
        # a second run asks for nothing; the pack shows the text with its label and the checklist does not count it
        self.assertEqual(summarize.run(project, notes, cache, call=fake, log=lambda m: None)["asked"], 0)
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        out = self.root / "docs" / "handoff"
        page = (out / "wiki" / "files" / "sync.ps1.md").read_text(encoding="utf-8")
        self.assertIn("Written by a language model (fake, 2026-01-01); not checked by a person", page)
        self.assertIn("Model text for sync.ps1.", page)
        index = (out / "wiki" / "index.md").read_text(encoding="utf-8")
        self.assertIn("*(model)* Model text for McpTools.cs.", index)     # a file with no comment and no note
        self.assertIn("— Copy the export to the share.", index)          # the file's own comment comes first
        self.assertNotIn("Model text for Store.cs", (out / "llms-full.txt").read_text(encoding="utf-8"))
        onto = json.loads((out / "ontology.json").read_text(encoding="utf-8"))
        ent = next(e for e in onto["entities"] if e["id"] == "file:McpTools.cs")
        self.assertEqual(ent["model_summary"]["engine"], "fake")
        self.assertNotIn("summary", ent)                              # model text is never the plain summary
        self.assertNotIn("HANDOFF.summaries.json", {f["path"] for f in json.loads((out / "handoff.json").read_text(encoding="utf-8"))["files"]})
        # a changed file loses its summary until the next --summarize run
        (self.root / "sync.ps1").write_text("# changed\n", encoding="utf-8")
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        self.assertNotIn("Model text for sync.ps1", (out / "wiki" / "files" / "sync.ps1.md").read_text(encoding="utf-8"))

    def test_mcp_server(self):
        import subprocess
        msgs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                                                                "clientInfo": {"name": "test", "version": "0"}}},
                {"jsonrpc": "2.0", "method": "notifications/initialized"},
                {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}]
        calls = [("handoff_todo", {"limit": 5}),
                 ("handoff_entity", {"id": "op:list"}),
                 ("handoff_search", {"query": "store", "type": "File"}),
                 ("handoff_source", {"path": "Store.cs", "start": 1, "end": 3}),
                 ("handoff_source", {"path": "../outside.txt"}),
                 ("handoff_write_note", {"heading": "File: Store.cs", "text": "Keeps the records; see Store.cs:4."}),
                 ("handoff_write_note", {"heading": "File: Store.cs", "text": "second try"}),
                 ("handoff_write_note", {"heading": "File: Nope.cs", "text": "x"}),
                 ("handoff_write_note", {"heading": "Topic: Credentials and accounts", "text": "key AKIA" + "ABCDEFGHIJKLMNOP"}),
                 ("handoff_build", {})]
        msgs += [{"jsonrpc": "2.0", "id": 10 + i, "method": "tools/call", "params": {"name": n, "arguments": a}}
                 for i, (n, a) in enumerate(calls)]
        r = subprocess.run([sys.executable, "-m", "handoff247", "mcp", str(self.root)], cwd=ROOT, capture_output=True,
                           input="\n".join(json.dumps(m) for m in msgs) + "\n", text=True, encoding="utf-8", timeout=120)
        replies = {m["id"]: m for m in map(json.loads, r.stdout.splitlines())}   # stdout carries only JSON-RPC
        self.assertEqual(len(replies), 2 + len(calls))
        self.assertEqual(replies[1]["result"]["serverInfo"]["name"], "handoff247")
        self.assertEqual(len(replies[2]["result"]["tools"]), 13)
        res = {n: replies[10 + i]["result"] for i, (n, _) in enumerate(calls) if n not in ("handoff_source", "handoff_write_note")}
        text = lambda i: replies[10 + i]["result"]["content"][0]["text"]        # noqa: E731
        err = lambda i: replies[10 + i]["result"]["isError"]                     # noqa: E731
        self.assertIn('"heading": "Project"', text(0))
        self.assertIn('"id": "file:Store.cs"', text(1))
        self.assertIn("Store.cs", text(2))
        self.assertIn("    1  namespace Mini;", text(3))
        self.assertTrue(err(4))                                                  # only files of the project
        self.assertFalse(err(5))
        self.assertTrue(err(6))                                                  # never over existing text
        self.assertTrue(err(7))                                                  # only known headings
        self.assertTrue(err(8))                                                  # never a secret
        self.assertFalse(res["handoff_build"]["isError"])
        self.assertIn("handover checklist", text(9))
        notes = (self.root / "HANDOFF.notes.md").read_text(encoding="utf-8")
        self.assertIn("Keeps the records; see Store.cs:4.\n\n_Written by an AI agent through the HandOff247 MCP server", notes)
        self.assertNotIn("AKIA", notes)
        self.assertIn("Keeps the records", (self.root / "docs" / "handoff" / "wiki" / "files" / "Store.cs.md").read_text(encoding="utf-8"))

    def test_go_folder_of_projects(self):
        ws = self.tmp / "ws"
        (ws / "Tools").mkdir(parents=True)
        (ws / "Pictures").mkdir()
        (ws / "Pictures" / "a.txt").write_text("x", encoding="utf-8")
        shutil.move(str(self.root), str(ws / "Mini"))
        (ws / "Tools" / "requirements.txt").write_text("requests\n", encoding="utf-8")
        (ws / "Tools" / "export.ps1").write_text("# Export through Mini.\n& ..\\Mini\\run.ps1 cli list\n", encoding="utf-8")
        self.assertEqual(main([str(ws), "--date", "2026-01-01"]), 0)
        out = ws / "handoff"
        for name in ("README.md", "index.html", "workspace.json", "workspace.mmd", "Mini/HANDOVER.md", "Tools/index.html",
                     "notes/Mini.notes.md", "notes/Tools.notes.md"):
            self.assertTrue((out / name).is_file(), name)
        self.assertFalse((ws / "Mini" / "HANDOFF.notes.md").exists())            # projects are left untouched
        data = json.loads((out / "workspace.json").read_text(encoding="utf-8"))
        by_name = {p["name"]: p for p in data["projects"]}
        self.assertEqual(set(by_name), {"Mini", "Tools"})
        self.assertEqual(data["unrecognised"], ["Pictures"])
        self.assertEqual([(r["to"], r["where"]) for r in by_name["Tools"]["refs"]],
                         [("Mini", [{"file": "export.ps1", "line": 2}])])
        self.assertEqual(by_name["Mini"]["refs"], [])
        index = (out / "README.md").read_text(encoding="utf-8")
        self.assertIn("**[Mini](Mini/HANDOVER.md)** is not in Git", index)
        self.assertIn("| Tools | Mini | 1 |", index)
        self.assertIn("](../../Mini/Program.cs", (out / "Mini" / "README.md").read_text(encoding="utf-8"))
        # a second run reads the notes it created and does not analyze its own output
        notes_file = out / "notes" / "Tools.notes.md"
        notes_file.write_text(notes_file.read_text(encoding="utf-8").replace(
            "## Project\nTODO", "## Project\nExports for the finance team.\nTODO"), encoding="utf-8")
        self.assertEqual(main([str(ws), "--date", "2026-01-01"]), 0)
        data = json.loads((out / "workspace.json").read_text(encoding="utf-8"))
        self.assertEqual({p["name"]: p["description"] for p in data["projects"]}["Tools"], "Exports for the finance team.")
        self.assertEqual(len(data["projects"]), 2)

    def test_foreign_detection(self):
        from handoff247.translate import foreign
        self.assertTrue(foreign("기록을 저장한다"))
        self.assertTrue(foreign("ログを書く"))
        self.assertTrue(foreign("Журнал"))
        self.assertFalse(foreign("Café façade, Straße — naïve"))
        self.assertFalse(foreign("PlayBook.dll cli list"))


NEWSROOM = ROOT / "tests" / "fixtures" / "newsroom"


def source_line(root: Path, file: str, line: int) -> str:
    return (root / file).read_text(encoding="utf-8").split("\n")[line - 1]


class UserContextTests(unittest.TestCase):
    """The application from its users' side, on a synthetic app with three user types:
    an author writes and uploads, an editor reviews and publishes, anyone reads the result.
    Nothing below is read from a hand-written expectation file: every assertion is about what
    the analysis found in the fixture's code, and the lines it points at are checked in the files."""

    @classmethod
    def setUpClass(cls):
        from handoff247.explore import Explorer
        cls.tmp = Path(tempfile.mkdtemp())
        cls.root = cls.tmp / "newsroom"
        shutil.copytree(NEWSROOM, cls.root)
        cls.p = analyze_project(cls.root, "Newsroom")
        cls.j = cls.p.links["journeys"]
        cls.ex = Explorer(cls.p)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def line(self, where: dict) -> str:
        return source_line(self.root, where["file"], where["line"])

    # ---- a user type decides which flow is found
    def test_user_types_come_from_role_checks(self):
        users = {u["name"]: u for u in self.j["user_types"]}
        self.assertEqual(set(users), {"author", "editor", "anyone"})
        for ev in users["editor"]["evidence"]:
            self.assertIn("editor", self.line(ev))                   # each place really names the role
        self.assertEqual(users["anyone"]["kind"], "anyone")
        self.assertIn("templates/desk.html", users["author"]["screens"])
        self.assertNotIn("templates/review.html", users["author"]["screens"])
        self.assertIn("templates/review.html", users["editor"]["screens"])
        self.assertIn("templates/home.html", users["anyone"]["screens"])

    def test_each_user_type_has_its_own_flow(self):
        author = self.ex.user_flow("author")
        editor = self.ex.user_flow("editor")
        on = lambda flow: {i["on_screen"] for s in flow["screens"] for i in s["can_do_here"]}   # noqa: E731
        self.assertIn("Send for review", on(author))
        self.assertIn("My desk", on(author))                         # menu entry shown to authors only
        self.assertNotIn("Review queue", on(author))
        self.assertIn("Review queue", on(editor))
        self.assertIn("Publish", on(editor))
        self.assertNotIn("Send for review", on(editor))
        desk = next(s for s in author["screens"] if s["screen"] == "templates/desk.html")
        send = next(i for i in desk["can_do_here"] if i["on_screen"] == "Send for review")
        self.assertEqual(send["shown_when"], ["a.status == 'draft'"])
        self.assertEqual(send["leads_to"], ["POST /desk/<int:article_id>/submit"])
        self.assertEqual(desk["layout"], ["templates/base.html"])

    # ---- nothing is closed: one user type's flow leads into the next
    def test_flows_link_across_user_types(self):
        author = self.ex.user_flow("author")
        desk = next(s for s in author["screens"] if s["screen"] == "templates/desk.html")
        send = next(i for i in desk["can_do_here"] if i["on_screen"] == "Send for review")
        then = [(t["user_types"], t["screens"], t["feature"]) for t in send["then"]]
        self.assertIn((["editor"], ["templates/review.html"], "GET /review"), then)       # the queue lists it
        self.assertIn((["editor"], [], "POST /review/<int:article_id>/publish"), then)    # and publishing tests the same value
        self.assertTrue(all(t["inferred"] for t in send["then"]))
        self.assertEqual(set(author["other_user_types"]), {"editor", "anyone"})
        queue = self.ex.feature("GET /review")
        self.assertEqual([(h["from_user_types"], h["from_feature"]) for h in queue["receives_from"]],
                         [(["author"], "POST /desk/<int:article_id>/submit")])
        back = self.ex.feature("POST /review/<int:article_id>/return")   # the editor's action returns work to the author
        self.assertTrue(any(h["to_user_types"] == ["author"] and "templates/desk.html" in h["to_screens"] for h in back["hands_over_to"]))
        shared = self.ex.who_sees("templates/article.html")              # one template, three kinds of viewer
        self.assertEqual(set(shared), {"author", "editor", "anyone"})

    def test_whole_chain_from_one_user_to_the_public_page(self):
        """author's action -> code -> data -> editor's follow-up -> what a reader sees."""
        term = next(t for t in self.j["terms"] if t["text"] == "Send for review")
        self.assertEqual(self.ex.who_sees(term["screen"]), ["author"])
        (submit,) = term["leads_to"]
        feat = self.ex.features[submit]
        self.assertEqual((feat["file"], self.line(feat).strip()), ("app.py", "def submit(article_id):"))
        (stmt,) = [q for q in feat["sql"] if q["sets"]]
        self.assertEqual(stmt["sets"], [{"table": "articles", "column": "status", "value": "in_review"}])
        self.assertIn("UPDATE articles SET status = 'in_review'", self.line(stmt))
        self.assertEqual(stmt["via"], "db.send_for_review")
        (hand,) = [h for h in self.j["handoffs"] if h["from"] == submit]
        self.assertEqual((hand["to"], self.ex.who(hand["to"])), ("GET /review", ["editor"]))
        self.assertIn("WHERE status = 'in_review'", self.line(hand["read_at"]))
        self.assertTrue(hand["inferred"])
        queue = self.ex.features[hand["to"]]
        self.assertEqual([r["screen"] for r in queue["renders"]], ["templates/review.html"])
        row = next(t for t in self.j["terms"] if t["screen"] == "templates/review.html" and t["kind"] == "link")
        self.assertEqual(row["leads_to"], ["GET /review/<int:article_id>"])
        detail = self.ex.features[row["leads_to"][0]]["renders"][0]["screen"]
        publish_term = next(t for t in self.j["terms"] if t["screen"] == detail and t["text"] == "Publish")
        (publish,) = publish_term["leads_to"]
        self.assertEqual(self.ex.who(publish), ["editor"])
        sets = [s for q in self.ex.features[publish]["sql"] for s in q["sets"]]
        self.assertEqual(sets, [{"table": "articles", "column": "status", "value": "published"}])   # the value was a parameter
        public = [h["to"] for h in self.j["handoffs"] if h["from"] == publish]
        self.assertEqual(public, ["GET /"])
        self.assertEqual(self.ex.who("GET /"), ["anyone"])
        self.assertEqual([r["screen"] for r in self.ex.features["GET /"]["renders"]], ["templates/home.html"])

    # ---- from the words on a screen to the code
    def test_screen_term_to_implementation(self):
        hit = self.ex.find("Headline")
        new = next(c for c in hit["candidates"] if c["feature"] == "GET,POST /desk/new")
        field = next(m for m in new["matched"] if m.get("field_in_code"))
        self.assertEqual((field["on_screen"], field["field_in_code"]), ("Headline", "title"))     # the label is not the identifier
        term = next(t for t in self.j["terms"] if t["text"] == "Headline" and t["kind"] == "field")
        self.assertIn('request.form["title"]', self.line(term["read_at"][0]))
        cover = next(t for t in self.j["terms"] if t["text"] == "Cover image")
        self.assertIn('request.files.get("cover")', self.line(cover["read_at"][0]))
        publish = self.ex.find("Publish")["candidates"][0]
        self.assertEqual(publish["implemented_in"], "app.py:101 publish")
        self.assertEqual(source_line(self.root, "app.py", 101).strip(), "def publish(article_id):")

    def test_terms_from_locale_files_in_every_language(self):
        term = next(t for t in self.j["terms"] if t["text"] == "Review queue" and t["kind"] == "link")
        self.assertEqual(term["i18n"]["key"], "nav.review")
        self.assertIn("Review queue", self.line(term["i18n"]))
        self.assertEqual([o["text"] for o in term["other_texts"]], ["검토 대기열"])
        korean = self.ex.find("검토 대기열에 글이 안 보여요", "editor")           # the user's own words, particle attached
        self.assertEqual(korean["candidates"][0]["feature"], "GET /review")
        self.assertTrue(korean["candidates"][0]["for_this_user_type"])

    def test_same_words_in_two_places_are_told_apart(self):
        hit = self.ex.find("Headline")
        feats = {c["feature"] for c in hit["candidates"]}
        self.assertEqual(feats, {"GET,POST /desk/new", "GET /desk"})    # a field label and a table column
        hit = self.ex.find("review")
        self.assertGreater(len(hit["candidates"]), 2)
        self.assertTrue(all(c["implemented_in"] for c in hit["candidates"]))
        other = self.ex.find("Publish", "author")
        self.assertFalse(other["candidates"][0]["for_this_user_type"])  # found and shown, marked as another user type's
        self.assertIn("not_found", self.ex.find("zzzz qqqq"))

    def test_request_gives_points_to_check_not_a_diagnosis(self):
        hit = self.ex.find("I sent it for review but the editor cannot find it", "author")
        self.assertEqual(hit["candidates"][0]["feature"], "POST /desk/<int:article_id>/submit")
        self.assertIn("does not tell which condition applied", hit["how_to_read"])
        card = self.ex.feature("POST /review/<int:article_id>/publish")
        checks = " | ".join(c["what"] for c in card["check"])
        self.assertIn("setting `NEWSROOM_COVER_REQUIRED`", checks)
        self.assertIn("condition `row['status'] != 'in_review'`", checks)
        branch = next(b for b in card["branches"] if "COVER_REQUIRED" in b["when"])
        self.assertIn('shows the message "Add a cover image before publishing"', branch["then"])
        self.assertIn("COVER_REQUIRED", self.line(branch))
        steps = card["normal_flow"]
        gated = next(s for s in steps if "Add a cover image" in s["step"])
        self.assertTrue(gated["when"])                                  # a conditional step is never told as unconditional
        update = next(s for s in steps if "sets status = 'published'" in s["step"])
        self.assertNotIn("when", update)
        self.assertEqual(update["via"], "db.publish_article")
        self.assertTrue(card["not_verified"])

    # ---- shared code and shared assets exist once
    def test_shared_code_and_screens_are_modelled_once(self):
        ids = [f["id"] for f in self.j["functions"]]
        self.assertEqual(len(ids), len(set(ids)))
        get_article = next(f for f in self.j["functions"] if f["id"] == "db.py:get_article")
        self.assertGreaterEqual(len(get_article["features"]), 4)
        self.assertEqual(len([s for s in self.j["screens"] if s["id"] == "templates/base.html"]), 1)
        base = self.ex.screens["templates/base.html"]
        self.assertEqual(len(base["extended_by"]), 7)
        self.assertEqual(len([t for t in self.j["terms"] if t["text"] == "Front page"]), 1)   # the menu entry is not copied per screen
        article = self.ex.screens["templates/article.html"]
        self.assertEqual(set(article["routes"]), {"GET /articles/<int:article_id>", "GET /preview/<int:article_id>"})
        from handoff247 import notes as n, ontology
        onto = ontology.build(self.p, n.Notes())
        names = [e["id"] for e in onto["entities"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(names.count("func:db.py:get_article"), 1)
        self.assertEqual(names.count("asset:static/logo.svg"), 1)
        runs = [r for r in onto["relations"] if r["p"] == "runsCode" and r["o"] == "func:db.py:get_article"]
        self.assertGreaterEqual(len(runs), 4)                           # many features, one function entity

    # ---- an asset from where it is made to where it shows
    def test_uploaded_asset_from_form_to_public_page(self):
        (a,) = self.ex.asset("cover")["assets"]
        self.assertEqual(a["kind"], "uploaded")
        self.assertEqual([p["text"] for p in a["comes_from"]["picked_with"]], ["Cover image"])
        self.assertEqual([(r["feature"], r["user_types"]) for r in a["comes_from"]["registered_by"]],
                         [("GET,POST /desk/new", ["author"])])
        (stored,) = a["stored_or_transformed_by"]
        self.assertEqual(stored["via"], "storage.save_upload")
        self.assertIn("file.save(", self.line(stored))
        self.assertNotIn("inferred", stored)                           # traced through the variables, not guessed
        self.assertEqual(stored["dir_env"], "NEWSROOM_UPLOADS")
        self.assertEqual([(c["table"], c["column"]) for c in a["linked_data"]], [("articles", "cover")])
        self.assertIn("INSERT INTO articles", self.line(a["linked_data"][0]))
        self.assertEqual([r["feature"] for r in a["delivered_by"]], ["GET /uploads/<path:name>"])
        shown = {x["screen"]: set(x["seen_by"]) for x in a["appears_on"]}
        self.assertEqual(set(shown), {"templates/home.html", "templates/article.html", "templates/review_detail.html"})
        self.assertEqual(shown["templates/review_detail.html"], {"editor"})
        self.assertEqual(set(a["if_replaced_or_deleted"]["user_types"]), {"author", "editor", "anyone"})
        for use in a["used_in"]:
            self.assertIn("url_for('uploaded'", self.line(use))

    def test_generated_static_and_unreferenced_assets(self):
        (gen,) = self.ex.asset("published.csv")["assets"]
        self.assertEqual(gen["kind"], "generated")
        self.assertEqual([(r["feature"], r["user_types"]) for r in gen["comes_from"]["written_by"]],
                         [("POST /review/<int:article_id>/publish", ["editor"])])
        self.assertIn('open(os.path.join(EXPORT_DIR, "published.csv"), "w"', self.line(gen["comes_from"]["written_by"][0]))
        self.assertEqual([r["feature"] for r in gen["delivered_by"]], ["GET /published.csv"])
        self.assertEqual([(x["screen"], x["seen_by"]) for x in gen["appears_on"]], [("templates/home.html", ["anyone"])])
        (logo,) = self.ex.asset("static/logo.svg")["assets"]
        self.assertEqual(logo["kind"], "static")
        self.assertEqual(len(logo["appears_on"]), 8)                    # the layout and the seven screens built on it
        self.assertTrue(any(x["through_layout"] == "templates/base.html" for x in logo["appears_on"]))
        (paper,) = self.ex.asset("paper.png")["assets"]                 # referenced from the stylesheet the layout loads
        self.assertEqual(paper["used_in"][0]["file"], "static/site.css")
        self.assertIn("templates/home.html", {x["screen"] for x in paper["appears_on"]})
        (old,) = self.ex.asset("old-banner.png")["assets"]
        self.assertEqual(old["appears_on"], [])
        self.assertTrue(any("no reference was found" in x for x in old["not_verified"]))   # unknown, not "unused"

    def test_data_states_carry_the_work_between_user_types(self):
        (d,) = self.ex.asset("articles")["data"]
        self.assertEqual(d["defined"], [{"file": "schema.sql", "line": 7}])
        states = {s["value"]: s for s in d["states"]}
        self.assertEqual(set(states), {"status = 'draft'", "status = 'in_review'", "status = 'published'"})
        self.assertEqual([r["user_types"] for r in states["status = 'in_review'"]["set_by"]], [["author"]])
        self.assertEqual([r["user_types"] for r in states["status = 'in_review'"]["filtered_on_by"]], [["editor"]])
        tested = states["status = 'draft'"]["tested_in"]
        self.assertTrue(any(x["where"] == "template" and x["text"] == "Send for review" for x in tested))
        self.assertTrue(any(x["where"] == "handler" and x["feature"] == "POST /desk/<int:article_id>/submit" for x in tested))

    # ---- from code to the people it reaches
    def test_code_change_to_user_experience(self):
        up = self.ex.impact("storage.py", symbol="save_upload")
        self.assertEqual([f["feature"] for f in up["features"]], ["GET,POST /desk/new"])
        self.assertEqual(up["user_types_affected"], ["author"])
        self.assertIn("templates/edit.html", {s["screen"] for s in up["screens"]})
        stmt = self.ex.impact("db.py", line=49)                         # the UPDATE that sends an article to review
        (feat,) = stmt["features"]
        self.assertEqual(feat["feature"], "POST /desk/<int:article_id>/submit")
        self.assertEqual(feat["then_affects"][0]["user_types"], ["editor"])
        self.assertEqual(set(stmt["user_types_affected"]), {"author", "editor"})
        shared = self.ex.impact("db.py", symbol="get_article")
        self.assertEqual(set(shared["user_types_affected"]), {"author", "editor", "anyone"})
        layout = self.ex.impact("templates/base.html")
        self.assertEqual(len(layout["screens"]), 8)
        self.assertEqual(set(layout["user_types_affected"]), {"author", "editor", "anyone"})
        words = self.ex.impact("locales/en.json")
        self.assertIn("templates/review.html", {s["screen"] for s in words["screens"]})
        css = self.ex.impact("static/site.css")
        self.assertIn("templates/home.html", {s["screen"] for s in css["screens"]})
        self.assertTrue(up["not_verified"])

    # ---- every connection has evidence or says it is not verified
    def test_every_connection_has_evidence_or_is_marked(self):
        files = {f.path for f in self.p.files}

        def check(where: dict, label: str) -> None:
            self.assertIn(where["file"], files, label)
            self.assertGreater(where["line"], 0, label)
        for t in self.j["terms"]:
            check(t, t["text"])
            if t["kind"] in ("link", "button") and t["screen"]:
                self.assertTrue(t["leads_to"] or t.get("unmatched") or t.get("external") or t.get("asset_file"), t["text"])
        for f in self.j["features"]:
            check(f, f["id"])
            for key in ("renders", "redirects", "fields", "sql", "files", "settings", "branches", "messages", "calls"):
                for x in f[key]:
                    check(x, f"{f['id']} {key}")
            if f["roles"]:
                self.assertTrue(f["access_evidence"], f["id"])
        for h in self.j["handoffs"]:
            check(h["set_at"], "handoff")
            check(h["read_at"], "handoff")
            self.assertTrue(h["inferred"])
        for a in self.j["assets"]:
            self.assertTrue(a["used_in"] or a["registered_by"] or a["written_by"] or a["unknown"], a["id"])
        for fid in self.ex.features:
            card = self.ex.feature(fid)
            for step in card["normal_flow"]:
                check(step, fid)
            self.assertIn("how_to_read", card)
        open_route = self.ex.feature("GET /uploads/<path:name>")
        self.assertTrue(any("no access check was found" in x for x in open_route["not_verified"]))
        self.assertEqual(self.j["gaps"], [])                             # nothing in this fixture had to be left open

    def test_unmatched_and_unanalysed_parts_are_reported(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            shutil.copytree(NEWSROOM, tmp / "n")
            page = tmp / "n" / "templates" / "home.html"
            marker = "<h1>Latest articles</h1>"
            extra = '<a href="/archive">Archive</a>\n<a href="{{ url_for(\'home\') }}">{{ t(\'nav.missing\') }}</a>'
            page.write_text(page.read_text(encoding="utf-8").replace(marker, marker + "\n" + extra), encoding="utf-8")
            (tmp / "n" / "server.js").write_text(
                "const app = require('express')();\napp.post('/api/notes', requireRole('admin'), (req, res) => res.json({}));\n",
                encoding="utf-8")
            j = analyze_project(tmp / "n", "N").links["journeys"]
            gaps = " | ".join(g["what"] for g in j["gaps"])
            self.assertIn("'Archive' points to '/archive'; no route was found for it", gaps)
            self.assertIn("translation key 'nav.missing' was not found", gaps)
            self.assertIn("POST /api/notes: the handler was not analysed", gaps)
            js = next(f for f in j["features"] if f["id"] == "POST /api/notes")
            self.assertEqual((js["roles"], js["analysed"]), (["admin"], False))   # the role on the route is read, the body is not
            self.assertIn("admin", {u["name"] for u in j["user_types"]})
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    # ---- small parts
    def test_sql_reading(self):
        from handoff247.handlers import parse_sql
        q = parse_sql("UPDATE articles SET status = ?, note = 'x' WHERE id = ? AND kind = 'news'", [("lit", "published"), None])
        self.assertEqual(q["writes"], ["articles"])
        self.assertEqual({(s["column"], s["value"]) for s in q["sets"]}, {("status", "published"), ("note", "x")})
        self.assertEqual([(s["column"], s["value"]) for s in q["filters"]], [("kind", "news")])
        q = parse_sql("SELECT a.id FROM articles a JOIN users u ON u.id = a.author_id WHERE a.status IN ('draft', 'in_review') AND u.role != 'admin'")
        self.assertEqual(q["reads"], ["articles", "users"])
        self.assertEqual({(s["table"], s["value"]) for s in q["filters"]}, {("articles", "draft"), ("articles", "in_review")})
        q = parse_sql("SELECT id FROM a, b WHERE status = 'x'")          # which table the column belongs to is not known
        self.assertEqual(q["filters"], [])
        self.assertIsNone(parse_sql("select the best option"))
        self.assertIsNone(parse_sql("Select a file from the list"))      # a sentence, not a statement
        self.assertEqual(parse_sql("select * from notes where kind = 'memo'")["reads"], ["notes"])
        q = parse_sql("INSERT INTO t (a, b) VALUES (?, 'new')", [("name", "stored")])
        self.assertEqual(q["param_columns"], [{"table": "t", "column": "a", "variable": "stored"}])
        self.assertEqual(q["sets"], [{"table": "t", "column": "b", "value": "new"}])

    def test_role_conditions_and_route_matching(self):
        from handoff247.handlers import access_other
        from handoff247.journeys import match_path
        from handoff247.screens import roles_in
        self.assertEqual(roles_in("user and user.role == 'editor'"), ["editor"])
        self.assertEqual(roles_in("current_user.role in ('editor', 'admin')"), ["editor", "admin"])
        self.assertEqual(roles_in("user.role != 'editor'"), [])          # says who is not, not who is
        self.assertEqual(roles_in("not (user.role == 'editor')"), [])
        self.assertEqual(roles_in("not user.is_admin"), [])
        self.assertEqual(roles_in("user.is_admin"), ["admin"])
        self.assertEqual(roles_in("a.status == 'draft'"), [])
        feats = [{"id": "GET /review/<int:id>", "verb": "GET", "path": "/review/<int:id>"},
                 {"id": "GET /review/export", "verb": "GET", "path": "/review/export"},
                 {"id": "POST /api/{op}", "verb": "POST", "path": "/api/{op}"},
                 {"id": "GET /files/<path:name>", "verb": "GET", "path": "/files/<path:name>"}]
        self.assertEqual(match_path("/review/*", "GET", feats), ["GET /review/<int:id>"])     # a hole is not a fixed word
        self.assertEqual(match_path("/review/export", "GET", feats), ["GET /review/export"])
        self.assertEqual(match_path("/api/", "", feats), ["POST /api/{op}"])
        self.assertEqual(match_path("/api/list", "GET", feats), [])                          # wrong method
        self.assertEqual(match_path("/files/a/b.png", "GET", feats), ["GET /files/<path:name>"])
        cs = ['[Authorize(Roles = "Admin, Editor")]', '[HttpPost("publish")]', "public IActionResult Publish() {"]
        self.assertEqual(access_other(cs, "csharp", "C.cs", 2)["roles"], ["Admin", "Editor"])
        self.assertTrue(access_other(["[Authorize]", '[HttpGet("x")]'], "csharp", "C.cs", 2)["signed_in"])
        js = ["router.get('/admin', requireAuth, (req, res) => res.render('admin'));"]
        self.assertTrue(access_other(js, "javascript", "s.js", 1)["signed_in"])

    def test_decorators_read_as_access_checks(self):
        import ast
        from handoff247.handlers import PyIndex
        src = ("@app.route('/a')\n@admin_required\ndef a(): pass\n"
               "@app.route('/b')\n@ajax_only\ndef b(): pass\n"
               "@app.route('/c')\n@login_required\ndef c(): pass\n"
               "@app.route('/d')\n@permission_required('articles.publish')\ndef d(): pass\n"
               "@app.route('/e')\n@roles_accepted('editor', 'chief')\ndef e(): pass\n")
        nodes = {n.name: n for n in ast.parse(src).body}
        acc = lambda name: PyIndex.access(None, "x.py", nodes[name])            # noqa: E731
        self.assertEqual(acc("a")["roles"], ["admin"])
        self.assertEqual((acc("b")["roles"], [d["text"] for d in acc("b")["unread"]]), ([], ["@ajax_only"]))   # not a user type
        self.assertTrue(acc("c")["signed_in"])
        self.assertEqual((acc("d")["roles"], acc("d")["permissions"]), ([], ["articles.publish"]))
        self.assertEqual(acc("e")["roles"], ["editor", "chief"])

    def test_pages_without_routes_and_their_scripts(self):
        """A single-page app: no route renders the page, its script calls the API."""
        tmp = Path(tempfile.mkdtemp())
        try:
            j = analyze_project(copy_fixture(tmp), "Mini").links["journeys"]
            (page,) = j["screens"]
            self.assertEqual(page["kind"], "page without a known route")
            self.assertEqual([(c["feature"], c["file"]) for c in page["calls"]], [("POST /api/{operation}", "wwwroot/app.js")])
            (anyone,) = j["user_types"]
            self.assertEqual((anyone["name"], anyone["screens"]), ("anyone", ["wwwroot/index.html"]))
            self.assertTrue(any("handler was not analysed" in g["what"] for g in j["gaps"]))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    # ---- the pack, the viewer, the command line and the MCP server tell the same story
    def test_pack_pages_graph_and_wiki(self):
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        out = self.root / "docs" / "handoff"
        users = (out / "USERS.md").read_text(encoding="utf-8")
        for heading in ("## User types", "### `author`", "### `editor`", "### `anyone`", "## Hand-overs between features",
                        "## Words on the screens", "## Assets in context", "## Shared code", "## Not verified by the analysis"):
            self.assertIn(heading, users)
        self.assertIn("not access levels of this pack", users)
        self.assertIn('"Send for review" (button)', users)
        self.assertIn('"Review queue" / "검토 대기열"', users)
        self.assertTrue((out / "diagrams" / "users.mmd").is_file())
        self.assertIn("[USERS.md](USERS.md)", (out / "README.md").read_text(encoding="utf-8"))
        onto = json.loads((out / "ontology.json").read_text(encoding="utf-8"))
        ents = {e["id"]: e for e in onto["entities"]}
        rels = {(r["s"], r["p"], r["o"]): r for r in onto["relations"]}
        self.assertEqual(ents["user:editor"]["type"], "UserType")
        self.assertIn(("user:editor", "sees", "screen:templates/review.html"), rels)
        self.assertIn(("route:GET /review", "openTo", "user:editor"), rels)
        hand = rels[("route:POST /desk/<int:article_id>/submit", "handsOverTo", "route:GET /review")]
        self.assertTrue(hand["inferred"])
        self.assertIn(("asset:upload:cover", "keptIn", "data:articles"), rels)
        self.assertIn(("screen:templates/home.html", "showsAsset", "asset:upload:cover"), rels)
        known = {r["id"] for r in onto["schema"]["relations"]}
        for (s, p, o), r in rels.items():
            self.assertIn(s, ents)
            self.assertIn(o, ents)
            self.assertIn(p, known)
            if p not in ("contains", "authored"):
                self.assertTrue(r.get("file"), (s, p, o))
        link = re.compile(r"\]\(([^)\s]+)\)")
        pages = list((out / "wiki").rglob("*.md")) + [out / "USERS.md", out / "llms.txt"]
        for e in ents.values():
            self.assertTrue((out / e["page"]).is_file(), e["id"])
        for page in pages:                                               # every link leads somewhere
            for href in link.findall(page.read_text(encoding="utf-8")):
                if href.startswith(("http:", "https:", "#")):
                    continue
                target = (page.parent / href.split("#")[0].replace("%20", " ")).resolve()
                self.assertTrue(target.exists(), f"{page.name}: {href}")
        editor = (out / "wiki" / "users" / "editor.md").read_text(encoding="utf-8")
        self.assertIn("## Other user types", editor)
        self.assertIn("](author.md)", editor)                            # one user type's page leads to the others
        feature = (out / ents["route:POST /review/<int:article_id>/publish"]["page"]).read_text(encoding="utf-8")
        for heading in ("## Started from", "## What the code does", "## Branches", "## Hand-overs", "## Code",
                        "## Data and assets", "## What to check", "## Not verified by the analysis"):
            self.assertIn(heading, feature)
        self.assertIn("`Cover image`", (out / "wiki" / "terms.md").read_text(encoding="utf-8"))
        viewer = (out / "index.html").read_text(encoding="utf-8")
        self.assertIn("'USERS.md', 'Users'", viewer)
        self.assertIn("Bring forward", viewer)
        self.assertIn('"users": ["author", "editor", "anyone"]', viewer)
        notes_text = (self.root / "HANDOFF.notes.md").read_text(encoding="utf-8")
        self.assertIn("## User: author", notes_text)
        self.assertNotIn("## User: anyone", notes_text)
        # what the owner writes about a user type reaches that user type's pages
        (self.root / "HANDOFF.notes.md").write_text(notes_text.replace(
            "## User: author\nTODO", "## User: author\nAbout thirty reporters.\nTODO"), encoding="utf-8")
        self.assertEqual(main([str(self.root), "--date", "2026-01-01"]), 0)
        self.assertIn("About thirty reporters.", (out / "wiki" / "users" / "author.md").read_text(encoding="utf-8"))
        self.assertIn("About thirty reporters.", (out / "USERS.md").read_text(encoding="utf-8"))

    def test_trace_command(self):
        import contextlib
        import io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.assertEqual(main(["trace", str(self.root), "review", "queue", "--user", "editor"]), 0)
            self.assertEqual(main(["trace", str(self.root), "--feature", "publish"]), 0)
            self.assertEqual(main(["trace", str(self.root), "--impact", "db.py:49", "--json"]), 0)
            self.assertEqual(main(["trace", str(self.root), "--asset", "cover"]), 0)
            self.assertEqual(main(["trace", str(self.root), "--user", "author"]), 0)
            self.assertEqual(main(["trace", str(self.root)]), 0)
        text = buf.getvalue()
        self.assertIn('1. "Review queue"  ->  GET /review', text)
        self.assertIn("hands over to (inferred):", text)
        self.assertIn('"feature": "POST /desk/<int:article_id>/submit"', text)
        self.assertEqual(main(["trace", str(self.root), "--feature", "no-such-feature"]), 2)

    def test_mcp_server_gives_an_agent_the_whole_project(self):
        import subprocess
        msgs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                                                                "clientInfo": {"name": "test", "version": "0"}}},
                {"jsonrpc": "2.0", "method": "notifications/initialized"},
                {"jsonrpc": "2.0", "id": 2, "method": "resources/list"},
                {"jsonrpc": "2.0", "id": 3, "method": "resources/read", "params": {"uri": "handoff://page/USERS.md"}}]
        calls = [("handoff_overview", {}),
                 ("handoff_users", {}),
                 ("handoff_users", {"user": "editor"}),
                 ("handoff_request", {"text": "검토 대기열에 안 보여요", "user": "editor"}),
                 ("handoff_feature", {"id": "POST /desk/<int:article_id>/submit"}),
                 ("handoff_asset", {"name": "cover"}),
                 ("handoff_impact", {"path": "storage.py", "symbol": "save_upload"}),
                 ("handoff_page", {}),
                 ("handoff_page", {"name": "wiki/users/author.md"}),
                 ("handoff_entity", {"id": "user:editor"}),
                 ("handoff_search", {"query": "cover", "type": "Asset"}),
                 ("handoff_write_note", {"heading": "User: editor", "text": "Two people at the news desk."}),
                 ("handoff_feature", {"id": "nothing like this"}),
                 ("handoff_users", {"user": "nobody"})]
        msgs += [{"jsonrpc": "2.0", "id": 10 + i, "method": "tools/call", "params": {"name": n, "arguments": a}}
                 for i, (n, a) in enumerate(calls)]
        r = subprocess.run([sys.executable, "-m", "handoff247", "mcp", str(self.root)], cwd=ROOT, capture_output=True,
                           input="\n".join(json.dumps(m) for m in msgs) + "\n", text=True, encoding="utf-8", timeout=180)
        replies = {m["id"]: m for m in map(json.loads, r.stdout.splitlines())}
        self.assertEqual(len(replies), 3 + len(calls), r.stderr[-2000:])
        self.assertIn("handoff_overview", replies[1]["result"]["instructions"])
        self.assertIn("not access levels", replies[1]["result"]["instructions"])
        uris = {x["uri"] for x in replies[2]["result"]["resources"]}
        self.assertIn("handoff://page/USERS.md", uris)
        self.assertIn("## Flows by user type", replies[3]["result"]["contents"][0]["text"])
        text = lambda i: replies[10 + i]["result"]["content"][0]["text"]        # noqa: E731
        err = lambda i: replies[10 + i]["result"]["isError"]                     # noqa: E731
        overview = json.loads(text(0))
        self.assertEqual([u["user_type"] for u in overview["who_uses_it"]], ["author", "editor", "anyone"])
        self.assertIn("NEWSROOM_COVER_REQUIRED", overview["settings"])
        self.assertIn("handoff_request", json.dumps(overview["where_to_go_next"]))
        self.assertEqual(len(json.loads(text(1))["user_types"]), 3)
        self.assertEqual(json.loads(text(2))["user_type"], "editor")
        self.assertEqual(json.loads(text(3))["candidates"][0]["feature"], "GET /review")
        card = json.loads(text(4))
        self.assertEqual(card["hands_over_to"][0]["to_user_types"], ["editor"])
        self.assertTrue(card["check"])
        self.assertEqual(json.loads(text(5))["assets"][0]["linked_data"][0]["column"], "cover")
        self.assertEqual(json.loads(text(6))["user_types_affected"], ["author"])
        self.assertIn("USERS.md", json.loads(text(7))["pages"])
        self.assertIn("## What this user type sees and does", text(8))
        self.assertIn('"note_heading": "User: editor"', text(9))
        self.assertIn("asset:upload:cover", text(10))
        self.assertFalse(err(11))
        self.assertTrue(err(12))
        self.assertTrue(err(13))
        self.assertIn("Two people at the news desk.", (self.root / "HANDOFF.notes.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
