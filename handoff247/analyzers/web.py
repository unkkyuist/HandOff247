"""JavaScript/TypeScript, HTML and CSS analyzers."""
from __future__ import annotations

import re

from ..lexer import clean_comment, first_sentence, lex, line_at, match_brace
from ..model import Fact, FileInfo, Symbol

IMPORT_RES = [
    re.compile(r"\bimport\s+(?:type\s+)?(?:[\w*{}\s,$]+?\s+from\s+)?['\"]([^'\"\n]+)['\"]"),
    re.compile(r"\bexport\s+[\w*{}\s,$]*?\s+from\s+['\"]([^'\"\n]+)['\"]"),
    re.compile(r"\bimport\(\s*['\"]([^'\"\n]+)['\"]\s*\)"),
    re.compile(r"\brequire\(\s*['\"]([^'\"\n]+)['\"]\s*\)"),
]
FUNC_RES = [
    (re.compile(r"(?m)^[ \t]*export\s+(?:default\s+)?(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)\s*\("), "export"),
    (re.compile(r"(?m)^[ \t]*export\s+(?:default\s+)?class\s+([A-Za-z_$][\w$]*)"), "class"),
    (re.compile(r"(?m)^[ \t]*export\s+(?:const|let|var)\s+([A-Za-z_$][\w$]*)"), "export"),
    (re.compile(r"(?m)^(?:async\s+)?function\s*\*?\s*([A-Za-z_$][\w$]*)\s*\("), "function"),
    (re.compile(r"(?m)^class\s+([A-Za-z_$][\w$]*)"), "class"),
    (re.compile(r"(?m)^(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s*)?(?:\([^()\n]*\)|[A-Za-z_$][\w$]*)\s*=>"), "function"),
]
CALL_RE = re.compile(r"(?<![\w$.])([A-Za-z_$][\w$]*)\s*\(\s*['\"]([A-Za-z][\w.:/-]{0,79})['\"]")
FETCH_RE = re.compile(r"\b(fetch|axios\.(?:get|post|put|delete|patch)|\$\.(?:get|post|ajax))\(\s*(['\"`])([^'\"`\n]*)")
ROUTE_RE = re.compile(r"\b(app|router|server|api|fastify)\.(get|post|put|delete|patch|all)\(\s*['\"`](/[^'\"`\n]*)")
MCP_RE = re.compile(r"\.(?:tool|registerTool)\(\s*['\"]([\w.-]+)['\"](?:\s*,\s*['\"]((?:[^'\"\\]|\\.)*)['\"])?")
ENV_RES = [re.compile(r"\bprocess\.env\.([A-Z_][A-Z0-9_]*)"), re.compile(r"\bprocess\.env\[\s*['\"](\w+)['\"]\s*\]"),
           re.compile(r"\bimport\.meta\.env\.([A-Z_][A-Z0-9_]*)")]
LAUNCH_RE = re.compile(r"\b(?:spawn|exec|execFile|fork|execSync|spawnSync|execFileSync)\(\s*['\"`]([^'\"`\n]+)")


def _doc_before(comments, line: int) -> str:
    for c in comments:
        if c.end_line == line - 1:
            return first_sentence(clean_comment(c.text))
    return ""


def analyze_js_text(f: FileInfo, text: str, facts: list[Fact], lang: str, line_offset: int = 0) -> None:
    lx = lex(text, lang)
    code, cs, nl = lx.code, lx.code_str, lx.newlines

    def ln(off: int) -> int:
        return line_at(nl, off) + line_offset

    if not line_offset:
        f.code, f.code_str = code, cs
        first_code = next((i for i, l in enumerate(code.split("\n"), 1) if l.strip()), None)
        head = [c.text for c in lx.comments if first_code is None or c.end_line < first_code]
        if head and not f.summary:
            f.summary, f.summary_source = first_sentence(clean_comment("\n".join(head)), 300), "file comment"
    f.strings.extend((v, line_at(nl, off) + line_offset) for v, _, off in lx.strings)
    for rx in IMPORT_RES:
        for m in rx.finditer(cs):
            f.imports.append((m.group(1), ln(m.start())))
    spans = []
    seen = set()
    for rx, kind in FUNC_RES:
        for m in rx.finditer(code):
            name = m.group(1)
            line = ln(m.start(1))
            if (name, line) in seen:
                continue
            seen.add((name, line))
            start = m.end()
            if code[m.end() - 1] == "(":
                start = match_brace(code, m.end() - 1, "(", ")") + 1   # skip defaults like args = {}
            brace = code.find("{", start)
            end_line = line
            if brace >= 0 and (kind in ("export", "function", "class")) and (brace - start < 400):
                end_line = line_at(nl, match_brace(code, brace)) + line_offset
            f.symbols.append(Symbol(name, kind, line, _doc_before(lx.comments, line - line_offset),
                                    public=kind in ("export", "class") or True, end_line=end_line))
            spans.append((name, line, end_line))
    if spans:
        facts.append(Fact("func_spans", f.path, 1, {"spans": spans}))
    for m in CALL_RE.finditer(cs):
        if m.group(1) in ("require", "import", "fetch", "if", "while", "for", "switch", "catch"):
            continue
        facts.append(Fact("call", f.path, ln(m.start()), {"func": m.group(1), "value": m.group(2)}))
    for m in FETCH_RE.finditer(cs):
        facts.append(Fact("http_call", f.path, ln(m.start()), {"path": m.group(3), "func": m.group(1)}))
    for m in ROUTE_RE.finditer(cs):
        facts.append(Fact("route", f.path, ln(m.start()), {"verb": m.group(2).upper(), "path": m.group(3), "calls": []}))
    for m in MCP_RE.finditer(cs):
        facts.append(Fact("mcp_tool", f.path, ln(m.start()), {"name": m.group(1), "name_source": "registration",
                                                              "method": "", "cls": "", "description": m.group(2) or "",
                                                              "literals": [], "params": []}))
    for rx in ENV_RES:
        for m in rx.finditer(cs):
            facts.append(Fact("env_read", f.path, ln(m.start()), {"name": m.group(1), "default": ""}))
    for m in LAUNCH_RE.finditer(cs):
        facts.append(Fact("launch", f.path, ln(m.start()), {"cmd": m.group(1).split()[0], "text": m.group(1)[:220]}))
    # switch/case dispatch tables
    for m in re.finditer(r"\bswitch\s*\(", code):
        paren = m.end() - 1
        close = match_brace(code, paren, "(", ")")
        brace = code.find("{", close)
        if brace < 0:
            continue
        end = match_brace(code, brace)
        cases = [(cm.group(1), ln(brace + cm.start())) for cm in re.finditer(r"\bcase\s+['\"]([^'\"\n]+)['\"]\s*:", cs[brace:end])]
        if len(cases) >= 3:
            table = f"{f.path}:{ln(m.start())}"
            facts.append(Fact("dispatch_table", f.path, ln(m.start()), {"table": table, "cls": "", "method": "",
                                                                       "selector": text[paren + 1:close].strip()[:40],
                                                                       "count": len(cases)}))
            for key, line in cases:
                facts.append(Fact("dispatch", f.path, line, {"table": table, "key": key, "handler_type": "",
                                                             "handler_method": "", "expr": ""}))


def analyze_js(f: FileInfo, facts: list[Fact]) -> None:
    analyze_js_text(f, f.text, facts, "typescript" if f.lang == "typescript" else "javascript")


def analyze_html(f: FileInfo, facts: list[Fact]) -> None:
    text = f.text
    title = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
    if title and title.group(1).strip():
        f.summary, f.summary_source = " ".join(title.group(1).split())[:200], "<title>"
    for m in re.finditer(r"<script\b[^>]*\bsrc\s*=\s*['\"]([^'\"]+)['\"]", text, re.I):
        f.imports.append((m.group(1), text.count("\n", 0, m.start()) + 1))
    for m in re.finditer(r"<link\b[^>]*\bhref\s*=\s*['\"]([^'\"]+)['\"]", text, re.I):
        f.imports.append((m.group(1), text.count("\n", 0, m.start()) + 1))
    for m in re.finditer(r"<script\b(?![^>]*\bsrc\s*=)[^>]*>(.*?)</script>", text, re.S | re.I):
        body = m.group(1)
        if body.strip():
            offset = text.count("\n", 0, m.start(1))
            analyze_js_text(f, body, facts, "javascript", line_offset=offset)


def analyze_css(f: FileInfo, facts: list[Fact]) -> None:
    lx = lex(f.text, "css")
    if lx.comments and lx.comments[0].line <= 2:
        f.summary, f.summary_source = first_sentence(clean_comment(lx.comments[0].text), 200), "file comment"
    for m in re.finditer(r"@import\s+(?:url\()?['\"]?([^'\")\s;]+)", lx.code_str):
        f.imports.append((m.group(1), line_at(lx.newlines, m.start())))
