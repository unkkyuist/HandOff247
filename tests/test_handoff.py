"""End-to-end and unit tests. Run: python -m unittest discover -s tests"""
from __future__ import annotations

import json
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
        self.assertEqual(main(["notes", str(self.root), "--lang", "ko"]), 0)
        notes_file = self.root / "HANDOFF.notes.md"
        text = notes_file.read_text(encoding="utf-8")
        self.assertIn("## File: Program.cs", text)
        self.assertIn("## Mode: cli", text)
        # a person fills two items
        text = text.replace("## Project\nTODO: 이 프로젝트가 하는 일, 쓰는 사람, 지금 상태를 적어 주세요.",
                            "## Project\nRecords for the front desk. Owner: ops team.")
        text = text.replace("## File: Program.cs\nTODO: 이 파일의 역할, 알아둘 점.",
                            "## File: Program.cs\nPick the mode here; serve is what people use.")
        notes_file.write_text(text, encoding="utf-8")
        # re-running notes keeps the person's text
        (self.root / "Extra.cs").write_text("namespace Mini; public class Extra {}", encoding="utf-8")
        self.assertEqual(main(["notes", str(self.root), "--lang", "ko"]), 0)
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


if __name__ == "__main__":
    unittest.main()
