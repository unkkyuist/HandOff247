"""Python analyzer built on the standard ``ast`` module (no code is executed)."""
from __future__ import annotations

import ast
import io
import re
import tokenize

from ..lexer import first_sentence
from ..model import Fact, FileInfo, Symbol

SUBPROCESS_FUNCS = {"run", "Popen", "call", "check_call", "check_output", "system", "execv", "execvp",
                    "spawnv", "startfile", "create_subprocess_exec", "create_subprocess_shell"}
ROUTE_DECOS = {"route", "get", "post", "put", "delete", "patch", "websocket"}


def _name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Call):
        return _name(node.func)
    return ""


def _dotted(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _dotted(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    return ""


def _lit(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _render_cmd(node: ast.AST) -> str:
    """Readable rendering of a subprocess argument (literals kept, variables shown as {name})."""
    if isinstance(node, (ast.List, ast.Tuple)):
        parts = []
        for el in node.elts:
            if isinstance(el, ast.Starred):
                parts.append("{*" + (_dotted(el.value) or "…") + "}")
            elif _lit(el) is not None:
                parts.append(_lit(el))
            elif isinstance(el, ast.Call) and _name(el.func) == "str" and el.args:
                parts.append("{" + (_dotted(el.args[0]) or "…") + "}")
            else:
                parts.append("{" + (_dotted(el) or "…") + "}")
        return " ".join(parts)
    if _lit(node) is not None:
        return _lit(node)
    if isinstance(node, ast.JoinedStr):
        out = ""
        for v in node.values:
            if isinstance(v, ast.Constant):
                out += str(v.value)
            else:
                out += "{" + (_dotted(getattr(v, "value", v)) or "…") + "}"
        return out
    return "{" + (_dotted(node) or "…") + "}"


def analyze(f: FileInfo, facts: list[Fact]) -> None:
    try:
        tree = ast.parse(f.text, filename=f.path)
    except (SyntaxError, ValueError) as e:
        f.skipped = f"python syntax error line {getattr(e, 'lineno', '?')}"
        return
    doc = ast.get_docstring(tree)
    if doc:
        f.summary, f.summary_source = first_sentence(" ".join(doc.split()), 300), "module docstring"
    else:
        head = []
        try:
            for tok in tokenize.generate_tokens(io.StringIO(f.text).readline):
                if tok.type == tokenize.COMMENT:
                    text = tok.string.lstrip("#").strip()
                    if text and not text.startswith("!") and "coding" not in text[:20]:
                        head.append(text)
                elif tok.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.ENCODING):
                    break
        except (tokenize.TokenError, IndentationError, SyntaxError):
            pass
        if head:
            f.summary, f.summary_source = first_sentence(" ".join(head), 300), "file comment"

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            kind = "class" if isinstance(node, ast.ClassDef) else "function"
            d = ast.get_docstring(node) or ""
            f.symbols.append(Symbol(node.name, kind, node.lineno, first_sentence(" ".join(d.split())),
                                    public=not node.name.startswith("_"), end_line=getattr(node, "end_lineno", node.lineno)))
            if isinstance(node, ast.ClassDef):
                for sub in node.body:
                    if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)) and not sub.name.startswith("_"):
                        sd = ast.get_docstring(sub) or ""
                        f.symbols.append(Symbol(sub.name, "method", sub.lineno, first_sentence(" ".join(sd.split())),
                                                parent=node.name, end_line=getattr(sub, "end_lineno", sub.lineno)))

    func_spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_spans.append((node.name, node.lineno, getattr(node, "end_lineno", node.lineno)))
    if func_spans:
        facts.append(Fact("func_spans", f.path, 1, {"spans": func_spans}))

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                f.imports.append((a.name, node.lineno))
        elif isinstance(node, ast.ImportFrom):
            mod = "." * node.level + (node.module or "")
            f.imports.append((mod, node.lineno))
            if node.level and not node.module:
                for a in node.names:
                    f.imports.append(("." * node.level + a.name, node.lineno))
        elif isinstance(node, ast.If):
            t = node.test
            if (isinstance(t, ast.Compare) and isinstance(t.left, ast.Name) and t.left.id == "__name__"
                    and t.comparators and _lit(t.comparators[0]) == "__main__"):
                facts.append(Fact("entry", f.path, node.lineno, {"style": "__main__ guard"}))
                if "entry" not in f.tags:
                    f.tags.append("entry")
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            f.strings.append((node.value, node.lineno))

    from_subprocess = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module in ("subprocess", "os", "asyncio"):
            from_subprocess.update(a.asname or a.name for a in node.names)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for deco in node.decorator_list:
                dname = _name(deco)
                target = deco.func if isinstance(deco, ast.Call) else deco
                owner = _dotted(target.value) if isinstance(target, ast.Attribute) else ""
                if dname in ROUTE_DECOS and isinstance(deco, ast.Call) and deco.args and _lit(deco.args[0]) is not None:
                    verb = dname.upper() if dname != "route" else "ANY"
                    for kw in deco.keywords:
                        if kw.arg == "methods" and isinstance(kw.value, (ast.List, ast.Tuple)):
                            verb = ",".join(_lit(e) or "?" for e in kw.value.elts)
                    facts.append(Fact("route", f.path, node.lineno, {"verb": verb, "path": _lit(deco.args[0]),
                                                                    "handler": node.name, "calls": []}))
                if dname == "tool" and owner:
                    name = node.name
                    if isinstance(deco, ast.Call):
                        for kw in deco.keywords:
                            if kw.arg == "name" and _lit(kw.value):
                                name = _lit(kw.value)
                    facts.append(Fact("mcp_tool", f.path, node.lineno, {
                        "name": name, "name_source": "decorator", "method": node.name, "cls": "",
                        "description": " ".join((ast.get_docstring(node) or "").split()), "literals": [],
                        "params": [a.arg for a in node.args.args]}))
        if not isinstance(node, ast.Call):
            continue
        fname = _name(node.func)
        dotted = _dotted(node.func)
        if node.args and _lit(node.args[0]) is not None and re.fullmatch(r"[A-Za-z][\w.:/-]{0,79}", _lit(node.args[0])):
            facts.append(Fact("call", f.path, node.lineno, {"func": fname, "value": _lit(node.args[0])}))
        if fname in SUBPROCESS_FUNCS and (dotted.startswith(("subprocess.", "os.", "asyncio.")) or dotted in from_subprocess):
            if node.args:
                cmd = _render_cmd(node.args[0])
                env_keys = []
                for kw in node.keywords:
                    if kw.arg == "env" and isinstance(kw.value, ast.Call) and _name(kw.value.func) == "dict":
                        env_keys = [k.arg for k in kw.value.keywords if k.arg]
                facts.append(Fact("launch", f.path, node.lineno, {"cmd": cmd.split(" ", 1)[0], "text": cmd[:220]}))
                for k in env_keys:
                    facts.append(Fact("env_write", f.path, node.lineno, {"name": k}))
        if dotted in ("os.environ.get", "os.getenv", "environ.get", "os.environ.setdefault") and node.args and _lit(node.args[0]):
            default = _lit(node.args[1]) if len(node.args) > 1 else ""
            facts.append(Fact("env_read", f.path, node.lineno, {"name": _lit(node.args[0]), "default": default or ""}))
        if fname == "add_parser" and node.args and _lit(node.args[0]):
            help_text = next((_lit(k.value) for k in node.keywords if k.arg == "help" and _lit(k.value)), "")
            facts.append(Fact("subcommand", f.path, node.lineno, {"name": _lit(node.args[0]), "help": help_text or ""}))
        if fname == "add_argument" and node.args and _lit(node.args[0]):
            help_text = next((_lit(k.value) for k in node.keywords if k.arg == "help" and _lit(k.value)), "")
            facts.append(Fact("cli_option", f.path, node.lineno, {"name": _lit(node.args[0]), "help": help_text or ""}))
        if fname == "Tool" and any(k.arg == "name" for k in node.keywords):
            nm = next((_lit(k.value) for k in node.keywords if k.arg == "name"), None)
            if nm:
                desc = next((_lit(k.value) for k in node.keywords if k.arg == "description" and _lit(k.value)), "")
                facts.append(Fact("mcp_tool", f.path, node.lineno, {"name": nm, "name_source": "Tool(name=…)",
                                                                   "method": "", "cls": "", "description": desc or "",
                                                                   "literals": [], "params": []}))
        if fname in ("join",) and dotted.endswith("path.join") or (fname == "Path" and node.args):
            parts = [_lit(a) for a in node.args if _lit(a)]
            if parts:
                facts.append(Fact("path_literal", f.path, node.lineno, {"parts": parts}))
        if fname in ("urlopen", "Request", "get", "post", "put", "delete") and node.args:
            url = _render_cmd(node.args[0])
            if url.startswith(("http://", "https://", "{")) and ("/" in url):
                if fname in ("urlopen", "Request") or dotted.startswith(("requests.", "httpx.", "session.")):
                    facts.append(Fact("http_call", f.path, node.lineno, {"path": url, "func": fname}))

    # names that certainly refer to callables: functions defined here, imported modules/names
    defined = {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    imported_mods = set()
    imported_names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            imported_mods.update((a.asname or a.name).split(".")[0] for a in n.names)
        elif isinstance(n, ast.ImportFrom):
            imported_names.update(a.asname or a.name for a in n.names)

    def callable_ref(v: ast.AST) -> bool:
        if isinstance(v, ast.Lambda):
            return True
        if isinstance(v, ast.Name):
            return v.id in defined or v.id in imported_names
        if isinstance(v, ast.Attribute) and isinstance(v.value, ast.Name):
            base = v.value.id
            return base in imported_mods or base in imported_names or (base in ("self", "cls") and v.attr in defined)
        return False

    for node in ast.walk(tree):
        # os.environ["X"] reads and writes
        if isinstance(node, ast.Subscript) and _dotted(node.value) in ("os.environ", "environ"):
            key = _lit(node.slice)
            if key:
                kind = "env_write" if isinstance(node.ctx, ast.Store) else "env_read"
                facts.append(Fact(kind, f.path, node.lineno, {"name": key, "default": ""}))
        # if op == "a" / elif op == "b" chains and match statements as dispatch tables
        if isinstance(node, ast.Dict):
            keys = [_lit(k) for k in node.keys if k is not None]
            vals = node.values
            if len(keys) >= 3 and all(keys) and all(callable_ref(v) for v in vals):
                table = f"{f.path}:{node.lineno}"
                facts.append(Fact("dispatch_table", f.path, node.lineno, {"table": table, "cls": "", "method": "",
                                                                         "selector": "dict", "count": len(keys)}))
                for k, v in zip(keys, vals):
                    facts.append(Fact("dispatch", f.path, getattr(v, "lineno", node.lineno), {
                        "table": table, "key": k, "handler_type": "", "handler_method": _dotted(v) if not isinstance(v, ast.Lambda) else "lambda",
                        "expr": _dotted(v) or "lambda"}))
        if isinstance(node, ast.Match) and isinstance(node.subject, ast.Name):
            keys = []
            for case in node.cases:
                pat = case.pattern
                if isinstance(pat, ast.MatchValue) and _lit(pat.value):
                    keys.append((_lit(pat.value), case.pattern.lineno))
            if len(keys) >= 3:
                table = f"{f.path}:{node.lineno}"
                facts.append(Fact("dispatch_table", f.path, node.lineno, {"table": table, "cls": "", "method": "",
                                                                         "selector": node.subject.id, "count": len(keys)}))
                for k, ln in keys:
                    facts.append(Fact("dispatch", f.path, ln, {"table": table, "key": k, "handler_type": "",
                                                               "handler_method": "", "expr": ""}))
    # if/elif chains comparing one variable to string literals
    in_chain: set[int] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.If) or id(node) in in_chain:
            continue
        chain = []
        cur = node
        var = None
        while isinstance(cur, ast.If):
            t = cur.test
            if (isinstance(t, ast.Compare) and isinstance(t.left, ast.Name) and len(t.ops) == 1
                    and isinstance(t.ops[0], ast.Eq) and _lit(t.comparators[0]) is not None):
                if var is None:
                    var = t.left.id
                if t.left.id != var:
                    break
                in_chain.add(id(cur))
                chain.append((_lit(t.comparators[0]), cur.lineno))
            else:
                break
            cur = cur.orelse[0] if len(cur.orelse) == 1 and isinstance(cur.orelse[0], ast.If) else None
        if len(chain) >= 3 and var and var != "__name__":
            table = f"{f.path}:{node.lineno}"
            facts.append(Fact("dispatch_table", f.path, node.lineno, {"table": table, "cls": "", "method": "",
                                                                     "selector": var, "count": len(chain)}))
            for k, ln in chain:
                facts.append(Fact("dispatch", f.path, ln, {"table": table, "key": k, "handler_type": "",
                                                           "handler_method": "", "expr": ""}))
