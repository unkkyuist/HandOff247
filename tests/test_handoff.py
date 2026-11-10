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


if __name__ == "__main__":
    unittest.main()
