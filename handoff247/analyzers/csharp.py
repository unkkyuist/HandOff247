"""C# analyzer: types, members, constructor dependencies, entry modes, switch dispatch tables,
ASP.NET minimal-API routes, MCP server tools, environment variables and process launches."""
from __future__ import annotations

import re

from ..lexer import Lexed, clean_comment, first_sentence, lex, line_at, match_brace
from ..model import Fact, FileInfo, Symbol

TYPE_RE = re.compile(
    r"(?<![\w.])(?P<mods>(?:(?:public|internal|private|protected|static|sealed|abstract|partial|readonly|file|unsafe|new|ref)\s+)*)"
    r"(?P<kind>record\s+struct|record\s+class|record|class|struct|interface|enum)\s+(?P<name>[A-Za-z_]\w*)")
METHOD_RE = re.compile(
    r"(?m)^[ \t]*(?:\[[^\]\n]*\][ \t]*)*"
    r"(?P<mods>(?:(?:public|internal|protected|private|static|async|override|virtual|sealed|abstract|extern|unsafe|new|partial|readonly)\s+)*)"
    r"(?P<ret>(?:[\w.]+(?:<[^<>()\n]*(?:<[^<>()\n]*>[^<>()\n]*)*>)?(?:\[\])*\??|\([^()\n]*\)\??)\s+)"
    r"(?P<name>[A-Za-z_]\w*)\s*(?:<[^<>()\n]*>)?\s*\(")
CTOR_RE = re.compile(r"(?m)^[ \t]*(?P<mods>(?:(?:public|internal|protected|private|static)\s+)+)(?P<name>[A-Z_]\w*)\s*\(")
NOT_RETURN = {"return", "await", "throw", "new", "else", "case", "yield", "var", "using", "if", "for",
              "foreach", "while", "switch", "catch", "lock", "when", "is", "as", "in", "out", "ref",
              "goto", "default", "typeof", "nameof", "sizeof", "do", "try", "finally", "checked", "unchecked",
              "fixed", "where", "select", "from", "orderby", "let", "group", "into", "join", "on", "equals", "by"}
NOT_NAME = {"if", "for", "foreach", "while", "switch", "catch", "using", "lock", "return", "nameof",
            "typeof", "sizeof", "default", "when", "new", "fixed", "checked", "unchecked", "not", "or",
            "and", "is", "await", "throw", "case", "in"}

ENV_READ_RE = re.compile(r'GetEnvironmentVariable\(\s*"(\w+)"\s*\)(?:\s*\?\?\s*"([^"\n]*)")?')
ENV_WRITE_RE = re.compile(r'SetEnvironmentVariable\(\s*"(\w+)"|Environment(?:Variables)?\[\s*"(\w+)"\s*\]\s*=(?!=)')
LAUNCH_RE = re.compile(r'Process\.Start\(\s*"([^"\n]+)"|new\s+ProcessStartInfo\s*\(\s*"([^"\n]+)"|FileName\s*=\s*"([^"\n]+)"')
ROUTE_RE = re.compile(r'\.(Map(?:Get|Post|Put|Delete|Patch|Methods|Fallback|Mcp|Hub<\w+>)?)\s*\(\s*"([^"\n]*)"')
ATTR_ROUTE_RE = re.compile(r'\[\s*(Http(?:Get|Post|Put|Delete|Patch)|Route)\s*(?:\(\s*"([^"\n]*)")?')
CALL_RE = re.compile(r'\b([A-Za-z_]\w*)\s*\(\s*"([A-Za-z][\w.:/-]{0,79})"')
MODE_EQ_RE = re.compile(r'\b([a-z_]\w*)\s*==\s*"([\w.-]+)"')
MODE_IS_RE = re.compile(r'\b([a-z_]\w*)\s+is\s+(?:not\s+)?\(?\s*("[\w.-]+"(?:\s+or\s+"[\w.-]+")*)')
MODE_DEFAULT_RE = re.compile(r'\b(?:var|string\??)\s+([a-z_]\w*)\s*=\s*args\b[^;\n]*?\?\?\s*"([\w.-]+)"')
ARM_RE = re.compile(r'(?m)^[ \t]*((?:"[^"\n]+"\s*(?:or\s+)?)+)\s*=>')
CASE_RE = re.compile(r'\bcase\s+"([^"\n]+)"\s*:')
HANDLER_RE = re.compile(r'\b([A-Za-z_]\w*)\??\.([A-Z]\w*)\s*\(')
LOCAL_CALL_RE = re.compile(r'(?<![\w.])([A-Z]\w*)\s*\(')
SIMPLE_TYPE = re.compile(r"[A-Za-z_]\w*")


def _decl_doc(text_lines: list[str], comments_by_end: dict, line: int) -> str:
    parts: list[str] = []
    k = line - 1
    while k >= 1:
        stripped = text_lines[k - 1].strip() if k - 1 < len(text_lines) else ""
        if k in comments_by_end:
            c = comments_by_end[k]
            parts.append(c.text)
            k = c.line - 1
            continue
        if stripped.startswith("["):
            k -= 1
            continue
        break
    if not parts:
        return ""
    return first_sentence(clean_comment("\n".join(reversed(parts))))


def _body_end(code: str, open_paren: int) -> int:
    """Given the index of a member's '(' return the index where its body ends."""
    close = match_brace(code, open_paren, "(", ")")
    j = close + 1
    n = len(code)
    while j < n and code[j] in " \t\n":
        j += 1
    # skip constraints / base calls such as ": base(x)" or "where T : class"
    stop = j
    while stop < n and code[stop] not in "{;=" and stop - j < 400:
        stop += 1
    if stop < n and code[stop] == "{":
        return match_brace(code, stop)
    if stop + 1 < n and code[stop] == "=" and code[stop + 1] == ">":
        depth = 0
        for k in range(stop, n):
            ch = code[k]
            if ch in "({[":
                depth += 1
            elif ch in ")}]":
                depth -= 1
            elif ch == ";" and depth <= 0:
                return k
        return n - 1
    return stop


def _params(text: str) -> list[tuple[str, str]]:
    """Split a parameter list into (type, name) pairs."""
    out = []
    depth = 0
    cur = ""
    for ch in text:
        if ch in "<([{":
            depth += 1
        elif ch in ">)]}":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    pairs = []
    for p in out:
        p = p.split("=", 1)[0].strip()
        p = re.sub(r"\[[^\]]*\]", "", p).strip()
        p = re.sub(r"^(this|params|ref|out|in|scoped)\s+", "", p)
        bits = p.rsplit(None, 1)
        if len(bits) == 2:
            pairs.append((bits[0].strip(), bits[1].strip()))
    return pairs


def analyze(f: FileInfo, facts: list[Fact]) -> None:
    lx: Lexed = lex(f.text, "csharp")
    f.code, f.code_str = lx.code, lx.code_str
    f.strings = [(v, ln) for v, ln, _ in lx.strings]
    code, cs, nl = lx.code, lx.code_str, lx.newlines
    lines = f.text.split("\n")
    comments_by_end = {}
    for c in lx.comments:
        comments_by_end[c.end_line] = c

    # file summary: comments before the first line of code
    first_code_line = None
    for idx, ln in enumerate(code.split("\n"), 1):
        if ln.strip():
            first_code_line = idx
            break
    head = [c.text for c in lx.comments if first_code_line is None or c.end_line < first_code_line]
    if head:
        f.summary = first_sentence(clean_comment("\n".join(head)), 300)
        f.summary_source = "file comment"

    ns = re.search(r"\bnamespace\s+([\w.]+)", code)
    namespace = ns.group(1) if ns else ""

    # ---- types
    types = []   # (name, kind, start_off, body_start, body_end, symbol)
    for m in TYPE_RE.finditer(code):
        name, kind = m.group("name"), re.sub(r"\s+", " ", m.group("kind"))
        line = line_at(nl, m.start("kind"))
        j = m.end()
        n = len(code)
        while j < n and code[j] in " \t\n":
            j += 1
        if j < n and code[j] == "<":
            j = match_brace(code, j, "<", ">") + 1
            while j < n and code[j] in " \t\n":
                j += 1
        ctor_params = []
        if j < n and code[j] == "(":
            close = match_brace(code, j, "(", ")")
            ctor_params = _params(f.text[j + 1:close])
            j = close + 1
        bases = ""
        k = j
        while k < n and code[k] not in "{;":
            k += 1
        between = code[j:k]
        if ":" in between:
            bases = between.split(":", 1)[1].split("where")[0].strip()
        body_start, body_end = k, k
        if k < n and code[k] == "{":
            body_end = match_brace(code, k)
        sym = Symbol(name=name, kind=kind, line=line, doc=_decl_doc(lines, comments_by_end, line),
                     public=bool(re.search(r"\b(public|internal)\b", m.group("mods"))) or not m.group("mods").strip(),
                     end_line=line_at(nl, body_end))
        f.symbols.append(sym)
        types.append((name, kind, m.start(), body_start, body_end, sym))
        dep_types = []
        for typ, pname in ctor_params:
            dep_types.append({"type": typ, "name": pname, "tokens": SIMPLE_TYPE.findall(typ)})
        if dep_types:
            facts.append(Fact("ctor_dep", f.path, line, {"cls": name, "params": dep_types, "primary": True}))
        if bases:
            facts.append(Fact("bases", f.path, line, {"cls": name, "bases": SIMPLE_TYPE.findall(bases)}))

    def enclosing_type(offset: int):
        best = None
        for t in types:
            if t[3] <= offset <= t[4] and (best is None or t[3] >= best[3]):
                best = t
        return best

    # ---- methods
    methods = []   # (name, parent, start_off, end_off, symbol)
    for m in METHOD_RE.finditer(code):
        ret = m.group("ret").strip()
        name = m.group("name")
        if ret.split("<")[0] in NOT_RETURN or name in NOT_NAME or ret in ("class", "struct", "record", "interface", "enum", "namespace"):
            continue
        paren = m.end() - 1
        end = _body_end(code, paren)
        t = enclosing_type(m.start())
        parent = t[0] if t else ""
        mods = m.group("mods")
        line = line_at(nl, m.start("name"))
        public = bool(re.search(r"\b(public|internal)\b", mods)) or (t is not None and t[1] == "interface")
        sym = Symbol(name=name, kind="method", line=line, doc=_decl_doc(lines, comments_by_end, line),
                     parent=parent, public=public, end_line=line_at(nl, end))
        methods.append((name, parent, m.start(), end, sym))
    for m in CTOR_RE.finditer(code):
        t = enclosing_type(m.start())
        if not t or m.group("name") != t[0]:
            continue
        paren = m.end() - 1
        close = match_brace(code, paren, "(", ")")
        params = _params(f.text[paren + 1:close])
        line = line_at(nl, m.start("name"))
        end = _body_end(code, paren)
        sym = Symbol(name=t[0], kind="constructor", line=line, parent=t[0],
                     public="public" in m.group("mods") or "internal" in m.group("mods"), end_line=line_at(nl, end))
        methods.append((t[0], t[0], m.start(), end, sym))
        if params:
            facts.append(Fact("ctor_dep", f.path, line, {"cls": t[0], "params": [
                {"type": a, "name": b, "tokens": SIMPLE_TYPE.findall(a)} for a, b in params], "primary": False}))
    methods.sort(key=lambda x: x[2])
    seen = set()
    for name, parent, start, end, sym in methods:
        key = (name, parent, sym.line)
        if key in seen:
            continue
        seen.add(key)
        f.symbols.append(sym)

    def enclosing_method(offset: int):
        best = None
        for mm in methods:
            if mm[2] <= offset <= mm[3] and (best is None or mm[2] >= best[2]):
                best = mm
        return best

    # ---- entry point
    has_main = re.search(r"\bstatic\s+(?:async\s+)?(?:void|int|Task(?:<int>)?)\s+Main\s*\(", code)
    outside = code
    for t in types:
        if t[4] > t[3]:
            outside = outside[:t[3]] + " " * (t[4] - t[3] + 1) + outside[t[4] + 1:]
    outside_lines = [l for l in outside.split("\n") if l.strip() and not re.match(r"\s*(using|namespace)\b", l)
                     and not re.match(r"\s*\[assembly:", l)]
    top_level = not has_main and len(outside_lines) >= 3 and re.search(r"\bargs\b|\bawait\b|\.Run\(|\.Build\(\)", outside)
    if has_main:
        facts.append(Fact("entry", f.path, line_at(nl, has_main.start()), {"style": "Main method"}))
    elif top_level:
        first = next((i for i, l in enumerate(outside.split("\n"), 1) if l.strip() and not re.match(r"\s*using\b", l)), 1)
        facts.append(Fact("entry", f.path, first, {"style": "top-level statements"}))
        f.tags.append("entry")
    if has_main:
        f.tags.append("entry")

    # ---- runtime modes (only in entry files)
    if "entry" in f.tags:
        literals: dict[str, dict[str, int]] = {}
        for m in MODE_EQ_RE.finditer(cs):
            literals.setdefault(m.group(1), {}).setdefault(m.group(2), line_at(nl, m.start()))
        for m in MODE_IS_RE.finditer(cs):
            for lit in re.findall(r'"([\w.-]+)"', m.group(2)):
                literals.setdefault(m.group(1), {}).setdefault(lit, line_at(nl, m.start()))
        defaults = {}
        for m in MODE_DEFAULT_RE.finditer(cs):
            defaults[m.group(1)] = (m.group(2), line_at(nl, m.start()))
            literals.setdefault(m.group(1), {}).setdefault(m.group(2), line_at(nl, m.start()))
        for var, lits in literals.items():
            compared = [l for l in lits if l != defaults.get(var, ("",))[0]]
            if len(compared) < 2 or len(lits) < 3:
                continue
            blocks = {}
            for m in re.finditer(r'\bif\s*\(\s*' + re.escape(var) + r'\s*==\s*"([\w.-]+)"\s*\)', cs):
                j = m.end()
                while j < len(code) and code[j] in " \t\n":
                    j += 1
                if j < len(code) and code[j] == "{":
                    end = match_brace(code, j)
                else:
                    end = code.find(";", j)
                blocks.setdefault(m.group(1), (line_at(nl, m.start()), line_at(nl, end)))
            last_block_end = max([b[1] for b in blocks.values()] or [0])
            total = len(lines)
            for lit, ln in sorted(lits.items(), key=lambda kv: kv[1]):
                if lit in blocks:
                    start, end = blocks[lit]
                    body = "block"
                else:
                    start, end = last_block_end + 1, total
                    body = "main body"
                facts.append(Fact("mode", f.path, ln, {"var": var, "name": lit, "start": start, "end": end,
                                                      "body": body, "default": defaults.get(var, ("",))[0] == lit}))

    # ---- switch dispatch tables
    for m in re.finditer(r"\bswitch\b", code):
        j = m.end()
        n = len(code)
        selector = ""
        before = code[max(0, m.start() - 80):m.start()].rstrip()
        sm = re.search(r"([A-Za-z_][\w.]*)\s*$", before)
        while j < n and code[j] in " \t\n":
            j += 1
        if j < n and code[j] == "(":
            close = match_brace(code, j, "(", ")")
            selector = f.text[j + 1:close].strip()
            j = close + 1
            while j < n and code[j] in " \t\n":
                j += 1
        elif sm:
            selector = sm.group(1)
        if j >= n or code[j] != "{":
            continue
        end = match_brace(code, j)
        body = cs[j:end]
        arms = []
        for am in ARM_RE.finditer(body):
            keys = re.findall(r'"([^"\n]+)"', am.group(1))
            arm_start = j + am.end()
            line_end = cs.find("\n", arm_start)
            expr = cs[arm_start: line_end if line_end > 0 else end].strip().rstrip(",").strip()
            arms.append((keys, line_at(nl, j + am.start()), expr))
        for cm in CASE_RE.finditer(body):
            arm_start = j + cm.end()
            nxt = re.search(r"\bcase\b|\bdefault\b|\bbreak\b|\breturn\b", cs[arm_start:end])
            expr = cs[arm_start: arm_start + (nxt.end() + 120 if nxt and nxt.group(0) == "return" else (nxt.start() if nxt else 200))]
            expr = " ".join(expr.split())[:200]
            arms.append(([cm.group(1)], line_at(nl, j + cm.start()), expr))
        n_keys = sum(len(a[0]) for a in arms)
        if n_keys < 3:
            continue
        meth = enclosing_method(m.start())
        t = enclosing_type(m.start())
        cls = t[0] if t else ""
        mname = meth[0] if meth else ""
        table = f"{cls}.{mname}" if cls and mname else (cls or mname or f.path)
        # receiver -> type resolution inside this file
        receivers: dict[str, str] = {}
        for fct in facts:
            if fct.kind == "ctor_dep" and fct.file == f.path and fct.data["cls"] == cls:
                for p in fct.data["params"]:
                    if p["tokens"]:
                        receivers[p["name"]] = p["tokens"][0]
        scope = code[meth[2]:meth[3]] if meth else code
        for lm in re.finditer(r"\bvar\s+(\w+)\s*=\s*new\s+([A-Za-z_]\w*)\s*\(", scope):
            receivers[lm.group(1)] = lm.group(2)
        for pm in re.finditer(r"\b([A-Z]\w*)\??\s+([A-Z]\w*)\s*\{\s*get", code[t[3]:t[4]] if t else code):
            receivers[pm.group(2)] = pm.group(1)
        facts.append(Fact("dispatch_table", f.path, line_at(nl, m.start()), {
            "table": table, "cls": cls, "method": mname, "selector": selector, "count": n_keys}))
        for keys, line, expr in arms:
            hm = HANDLER_RE.search(expr)
            htype, hmeth = "", ""
            if hm:
                recv, hmeth = hm.group(1), hm.group(2)
                htype = receivers.get(recv, recv if recv[:1].isupper() else "")
            else:
                lm = LOCAL_CALL_RE.search(expr)
                if lm and not expr.lstrip().startswith("new"):
                    htype, hmeth = cls, lm.group(1)
            for key in keys:
                facts.append(Fact("dispatch", f.path, line, {"table": table, "key": key, "handler_type": htype,
                                                             "handler_method": hmeth, "expr": expr[:160]}))

    # ---- literal-argument calls (resolved against dispatch keys later)
    for m in CALL_RE.finditer(cs):
        name = m.group(1)
        if name in NOT_NAME:
            continue
        facts.append(Fact("call", f.path, line_at(nl, m.start()), {"func": name, "value": m.group(2)}))

    # ---- MCP tools
    if re.search(r"\[\s*McpServerToolType\b", cs):
        f.tags.append("mcp-tool-type")
    for m in re.finditer(r"\[\s*McpServerTool\b(?!Type)", code):
        close = match_brace(code, m.start(), "[", "]")
        attr = cs[m.start():close + 1]
        name_m = re.search(r'\bName\s*=\s*"([^"]+)"', attr)
        desc_m = re.search(r'Description\(\s*"((?:[^"\\]|\\.)*)"', attr)
        after = [mm for mm in methods if mm[2] > m.start()]
        if not after:
            continue
        meth = after[0]
        if not desc_m:
            between = cs[close:meth[2]]
            desc_m = re.search(r'Description\(\s*"((?:[^"\\]|\\.)*)"', between)
        desc = desc_m.group(1).replace('\\"', '"') if desc_m else ""
        method_name = meth[0]
        base = method_name[:-5] if method_name.endswith("Async") and len(method_name) > 5 else method_name
        tool = name_m.group(1) if name_m else re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", base).lower()
        literals = [v for v, ln, off in lx.strings if meth[2] <= off <= meth[3]]
        sig_open = code.find("(", meth[2])
        params = [b for a, b in _params(f.text[sig_open + 1:match_brace(code, sig_open, "(", ")")])] if sig_open > 0 else []
        meth[4].doc = meth[4].doc or first_sentence(desc)
        facts.append(Fact("mcp_tool", f.path, meth[4].line, {
            "name": tool, "name_source": "attribute" if name_m else "method name (SDK snake_case)",
            "method": method_name, "cls": meth[1], "description": desc, "literals": literals, "params": params}))

    # ---- HTTP routes
    for m in ROUTE_RE.finditer(cs):
        kind = m.group(1)
        verb = {"MapGet": "GET", "MapPost": "POST", "MapPut": "PUT", "MapDelete": "DELETE", "MapPatch": "PATCH",
                "MapMcp": "MCP", "Map": "ANY", "MapMethods": "ANY", "MapFallback": "ANY"}.get(kind, "HUB" if kind.startswith("MapHub") else "ANY")
        paren = code.find("(", m.start())
        close = match_brace(code, paren, "(", ")")
        span = cs[paren:close]
        calls = [{"recv": c.group(1), "method": c.group(2)} for c in HANDLER_RE.finditer(span)]
        facts.append(Fact("route", f.path, line_at(nl, m.start()), {"verb": verb, "path": m.group(2) or "/",
                                                                   "calls": calls, "end": line_at(nl, close)}))
    for m in ATTR_ROUTE_RE.finditer(cs):
        verb = m.group(1).replace("Http", "").upper() if m.group(1) != "Route" else "ROUTE"
        facts.append(Fact("route", f.path, line_at(nl, m.start()), {"verb": verb, "path": m.group(2) or "", "calls": []}))
    if re.search(r"\.UseStaticFiles\s*\(", code):
        roots = [v for v, ln in f.strings if v in ("wwwroot", "public", "static")]
        facts.append(Fact("static_files", f.path, line_at(nl, re.search(r"\.UseStaticFiles", code).start()),
                          {"dir": roots[0] if roots else "wwwroot"}))
    for m in re.finditer(r"\bapp\.Use\s*\(", code):
        facts.append(Fact("middleware", f.path, line_at(nl, m.start()), {}))
    for m in re.finditer(r'UseUrls\(\s*\$?"([^"\n]+)"', cs):
        facts.append(Fact("listen", f.path, line_at(nl, m.start()), {"value": m.group(1)}))

    # ---- environment, launches, path literals
    for m in ENV_READ_RE.finditer(cs):
        facts.append(Fact("env_read", f.path, line_at(nl, m.start()), {"name": m.group(1), "default": m.group(2) or ""}))
    for m in ENV_WRITE_RE.finditer(cs):
        facts.append(Fact("env_write", f.path, line_at(nl, m.start()), {"name": m.group(1) or m.group(2)}))
    for m in LAUNCH_RE.finditer(cs):
        cmd = next(g for g in m.groups() if g)
        facts.append(Fact("launch", f.path, line_at(nl, m.start()), {"cmd": cmd, "text": cmd}))
    for m in re.finditer(r"\bPath\.(?:Combine|Join)\s*\(", code):
        paren = m.end() - 1
        close = match_brace(code, paren, "(", ")")
        parts = [v for v, ln, off in lx.strings if paren <= off <= close]
        if parts:
            facts.append(Fact("path_literal", f.path, line_at(nl, m.start()), {"parts": parts}))
    if namespace:
        f.tags.append("ns:" + namespace)
