"""What a route does, read from its handler.

For Python the handler is followed through ``ast`` into the project functions it calls
(a few levels deep), and every effect keeps the file and line it was seen at plus the call
chain that led there: the role check on the route, form fields and uploaded files it reads,
SQL statements (tables, and the literal column values they set or filter on), files it
stores, writes, serves or deletes, settings it depends on, messages it shows, branches,
redirects and the template it renders. Nothing is executed.

Two small data flows are traced through variables, because name matching alone would be a
guess: an uploaded file object from ``request.files`` to the call that stores it, and the
stored name from there into the SQL parameter (so the column that holds the file name is
known, not assumed).

For other languages only what sits directly on the route is read (role middleware on an
Express route, ``[Authorize]`` above an ASP.NET action). Their handlers are reported as not
analysed.
"""
from __future__ import annotations

import ast
import posixpath
import re

from .model import Project

ROUTE_DECOS = {"route", "get", "post", "put", "delete", "patch", "websocket"}
ROLE_WORD = re.compile(r"role|group|admin|staff|member|user_?type|allowed|restrict|access", re.I)
PERMISSION_WORD = re.compile(r"perm|scope|\bcan\b|capabilit|privilege", re.I)
SIGNED_IN = re.compile(r"^(?:login|auth|authentication|jwt|token|user|session|fresh_login|fresh_jwt)_?(?:required|only|needed)$"
                       r"|^(?:requires?_?(?:auth|login)|authenticated|is_authenticated|ensure_logged_in|logged_in)$", re.I)
ROLE_FROM_NAME = re.compile(r"^(?:require[sd]?_)?([a-z]+?)_(?:required|only)$", re.I)
# `@admin_required` names a role; `@ajax_only` or `@https_required` do not. Only names from this list are
# read as a role, because a wrong user type is worse than a missing one.
ROLE_NAMES = {"admin", "administrator", "staff", "superuser", "moderator", "editor", "manager", "owner", "member",
              "teacher", "student", "operator", "reviewer", "author", "seller", "buyer", "customer", "vendor",
              "employee", "supervisor", "publisher", "contributor", "maintainer", "auditor"}
QUIET_DECOS = {"wraps", "staticmethod", "classmethod", "property", "cache", "cached", "lru_cache", "csrf_exempt",
               "contextmanager", "overload", "abstractmethod", "override"}
RENDER_FUNCS = {"render_template", "render", "TemplateResponse", "render_to_response", "render_to_string", "template"}
TEMPLATE_NAME = re.compile(r"\.(html?|jinja2?|j2|njk|twig|hbs|txt|xml)$", re.I)
REQUEST_SOURCES = {"form": "form", "files": "file", "args": "query", "values": "form", "json": "json",
                   "POST": "form", "GET": "query", "FILES": "file", "data": "form", "query_params": "query"}
STORAGE_METHODS = {"upload_file", "upload_fileobj", "put_object", "download_file", "download_fileobj", "get_object",
                   "generate_presigned_url", "upload_blob", "download_blob", "upload_from_file", "upload_from_filename",
                   "upload_from_string", "download_to_filename", "delete_object", "delete_blob"}
MAIL_METHODS = {"sendmail", "send_message", "send_mail", "send_email"}
BACKGROUND_METHODS = {"delay", "apply_async", "enqueue", "enqueue_call", "add_task", "send_task", "create_task"}
HTTP_ROOTS = ("requests.", "httpx.", "urllib.request.", "aiohttp.")

SQL_START = re.compile(r"^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE|WITH)\b", re.I)
SQL_KEYWORDS = {"where", "join", "on", "order", "group", "limit", "left", "right", "inner", "outer", "cross", "full",
                "having", "union", "set", "values", "as", "using", "natural", "returning", "offset", "for"}
STATE_VALUE = re.compile(r"[\w .:/-]{1,40}$")


# ---------------------------------------------------------------------------- SQL

def _split_top(text: str) -> list[str]:
    parts, depth, cur, quote = [], 0, [], ""
    for ch in text:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = ""
            continue
        if ch in "'\"":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
            continue
        cur.append(ch)
    if "".join(cur).strip():
        parts.append("".join(cur).strip())
    return parts


def parse_sql(sql: str, params: list | None = None) -> dict | None:
    """Tables a statement reads or writes, and the column values it sets or filters on.

    Only values that are written in the statement, or passed as a literal in the parameter
    list at the matching placeholder, are reported. ``params`` holds one entry per
    placeholder: ``("lit", value)``, ``("name", variable)`` or ``None``.
    """
    s = " ".join(sql.split())
    m = SQL_START.match(s)
    if not m:
        return None
    verb = m.group(1).upper().split()[0]
    # a sentence such as "Select a file from the list" is not a statement: the second keyword has
    # to be there, in the same letter case, and lower-case SQL has to look like SQL
    partner = {"SELECT": "FROM", "WITH": "SELECT", "INSERT": "INTO", "UPDATE": "SET", "DELETE": "FROM", "CREATE": "TABLE"}[verb]
    pm = re.search(r"\b" + partner + r"\b", s, re.I)
    if not pm or pm.group(0).isupper() != m.group(1).isupper() or not (m.group(1).isupper() or m.group(1).islower()):
        return None
    if m.group(1).islower() and not re.search(r"[*=?(;]", s):
        return None
    counter = iter(range(10_000))
    s = re.sub(r"\?|%s", lambda _: f"?{next(counter)}", s)
    out = {"verb": verb, "reads": [], "writes": [], "sets": [], "filters": [], "param_columns": [], "creates": [],
           "text": " ".join(sql.split())[:200]}
    params = params or []

    def value_of(token: str):
        token = token.strip()
        q = re.fullmatch(r"'([^']*)'", token)
        if q:
            return ("lit", q.group(1))
        p = re.fullmatch(r"\?(\d+)", token)
        if p and int(p.group(1)) < len(params):
            return params[int(p.group(1))]
        return None

    def note(kind: str, table: str, column: str, token: str) -> None:
        v = value_of(token)
        if not v or not table:
            return
        if v[0] == "lit" and STATE_VALUE.match(v[1]):
            out[kind].append({"table": table, "column": column, "value": v[1]})
        elif v[0] == "name" and kind == "sets":
            out["param_columns"].append({"table": table, "column": column, "variable": v[1]})

    aliases: dict[str, str] = {}

    def where(text: str, tables: list[str]) -> None:
        def table_of(col: str) -> tuple[str, str]:
            if "." in col:
                q, c = col.split(".", 1)
                return aliases.get(q, q if q in tables else ""), c
            return (tables[0] if len(tables) == 1 else ""), col
        for cm in re.finditer(r"([A-Za-z_]\w*(?:\.\w+)?)\s*(?<![!<>])=\s*('[^']*'|\?\d+)", text):
            t, c = table_of(cm.group(1))
            note("filters", t, c, cm.group(2))
        for cm in re.finditer(r"([A-Za-z_]\w*(?:\.\w+)?)\s+IN\s*\(([^)]*)\)", text, re.I):
            if re.search(r"\bNOT\s*$", text[:cm.start()], re.I):
                continue
            t, c = table_of(cm.group(1))
            for tok in _split_top(cm.group(2)):
                note("filters", t, c, tok)

    if verb == "CREATE":
        cm = re.match(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[\"`\[]?(\w+)[\"`\]]?\s*\((.*)\)", s, re.I)
        if cm:
            cols = []
            for seg in _split_top(cm.group(2)):
                word = seg.split(" ", 1)[0].strip("\"`[]")
                if word and word.upper() not in ("PRIMARY", "FOREIGN", "UNIQUE", "CHECK", "CONSTRAINT", "KEY", "INDEX"):
                    cols.append(word)
            out["creates"].append({"table": cm.group(1), "columns": cols})
        return out
    if verb == "INSERT":
        cm = re.match(r"INSERT\s+(?:OR\s+\w+\s+)?INTO\s+[\"`\[]?(\w+)[\"`\]]?\s*(?:\(([^)]*)\))?\s*(?:VALUES\s*\((.*)\))?", s, re.I)
        if cm:
            table = cm.group(1)
            out["writes"].append(table)
            if cm.group(2) and cm.group(3):
                body = cm.group(3)
                depth, end = 0, len(body)
                for i, ch in enumerate(body):               # stop at the bracket that closes VALUES (
                    if ch == "(":
                        depth += 1
                    elif ch == ")":
                        if depth == 0:
                            end = i
                            break
                        depth -= 1
                cols, vals = [c.strip(" \"`[]") for c in cm.group(2).split(",")], _split_top(body[:end])
                if len(cols) == len(vals):
                    for c, v in zip(cols, vals):
                        note("sets", table, c, v)
        return out
    if verb == "UPDATE":
        cm = re.match(r"UPDATE\s+(?:OR\s+\w+\s+)?[\"`\[]?(\w+)[\"`\]]?\s+SET\s+(.*?)(?:\s+WHERE\s+(.*))?$", s, re.I)
        if cm:
            table = cm.group(1)
            out["writes"].append(table)
            for seg in _split_top(cm.group(2)):
                am = re.match(r"[\"`\[]?(\w+)[\"`\]]?\s*=\s*(.+)$", seg)
                if am:
                    note("sets", table, am.group(1), am.group(2))
            if cm.group(3):
                where(cm.group(3), [table])
        return out
    if verb == "DELETE":
        cm = re.match(r"DELETE\s+FROM\s+[\"`\[]?(\w+)[\"`\]]?(?:\s+WHERE\s+(.*))?", s, re.I)
        if cm:
            out["writes"].append(cm.group(1))
            if cm.group(2):
                where(cm.group(2), [cm.group(1)])
        return out
    tables = []
    stop = r"(?=\b(?:WHERE|GROUP|ORDER|LIMIT|JOIN|LEFT|RIGHT|INNER|OUTER|CROSS|FULL|NATURAL|UNION|HAVING|ON)\b|\)|$)"
    items = [x for fm in re.finditer(r"\bFROM\s+(.+?)" + stop, s, re.I) for x in fm.group(1).split(",")]
    items += [jm.group(1) for jm in re.finditer(r"\bJOIN\s+(.+?)" + stop, s, re.I)]
    for item in items:                                  # "articles", "articles a", "articles AS a"
        tm = re.fullmatch(r"\s*[\"`\[]?(\w+)[\"`\]]?(?:\s+(?:AS\s+)?(\w+))?\s*", item, re.I)
        if not tm or tm.group(1).lower() in SQL_KEYWORDS:
            continue
        if tm.group(1) not in tables:
            tables.append(tm.group(1))
        if tm.group(2) and tm.group(2).lower() not in SQL_KEYWORDS:
            aliases[tm.group(2)] = tm.group(1)
    out["reads"] = tables
    wm = re.search(r"\bWHERE\b(.*)$", s, re.I)
    if wm and tables:
        where(wm.group(1), tables)
    return out


# ---------------------------------------------------------------------------- Python

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
    if isinstance(node, ast.Call):
        return _dotted(node.func)
    return ""


def _lit(node: ast.AST | None) -> str | None:
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None


def _src(node: ast.AST, limit: int = 160) -> str:
    try:
        text = " ".join(ast.unparse(node).split())
    except Exception:                                   # unparse cannot fail on parsed code, but never break a run
        return ""
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _strings(node: ast.AST) -> list[str]:
    out = []
    for el in (node.elts if isinstance(node, (ast.List, ast.Tuple, ast.Set)) else [node]):
        if _lit(el) is not None:
            out.append(_lit(el))
    return out


class PyIndex:
    """Functions, imports and module-level settings of every Python file of the project."""

    def __init__(self, project: Project):
        self.paths = {f.path for f in project.files}
        self.trees: dict[str, ast.Module] = {}
        self.funcs: dict[str, dict[str, ast.AST]] = {}
        self.imports: dict[str, dict[str, tuple]] = {}
        self.consts: dict[str, dict[str, dict]] = {}
        for f in project.files:
            if f.lang != "python" or not f.text or f.skipped:
                continue
            try:
                self.trees[f.path] = ast.parse(f.text)
            except (SyntaxError, ValueError):
                continue
        for path, tree in self.trees.items():
            funcs: dict[str, ast.AST] = {}
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    funcs[node.name] = node
                elif isinstance(node, ast.ClassDef):
                    for sub in node.body:
                        if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            funcs[f"{node.name}.{sub.name}"] = sub
            self.funcs[path] = funcs
        for path, tree in self.trees.items():
            imp: dict[str, tuple] = {}
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for a in node.names:
                        target = self.module_file(a.name, path, 0)
                        if target:
                            imp[(a.asname or a.name).split(".")[0] if not a.asname else a.asname] = ("module", target)
                elif isinstance(node, ast.ImportFrom):
                    base = self.module_file(node.module or "", path, node.level) if (node.module or node.level) else ""
                    for a in node.names:
                        alias = a.asname or a.name
                        sub = self.module_file(((node.module + ".") if node.module else "") + a.name, path, node.level)
                        if sub:
                            imp[alias] = ("module", sub)
                        elif base:
                            imp[alias] = ("name", base, a.name)
            self.imports[path] = imp
            consts: dict[str, dict] = {}
            for node in tree.body:
                if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                    env = self._env_in(node.value)
                    consts[node.targets[0].id] = {"line": node.lineno, "env": env, "expr": _src(node.value, 80)}
            self.consts[path] = consts

    def module_file(self, module: str, importer: str, level: int) -> str:
        rel = module.replace(".", "/")
        here = posixpath.dirname(importer)
        for _ in range(max(0, level - 1)):
            here = posixpath.dirname(here)
        bases = [here] if level else [here, ""]
        for base in bases:
            for cand in (posixpath.join(base, rel + ".py") if rel else "", posixpath.join(base, rel, "__init__.py")):
                cand = posixpath.normpath(cand) if cand else ""
                if cand and cand in self.paths:
                    return cand
        if rel and not level:
            hits = [p for p in self.paths if p.endswith("/" + rel + ".py")]
            if len(hits) == 1:
                return hits[0]
        return ""

    @staticmethod
    def _env_in(node: ast.AST) -> str:
        for n in ast.walk(node):
            if isinstance(n, ast.Call) and _dotted(n.func) in ("os.environ.get", "os.getenv", "environ.get") and n.args:
                if _lit(n.args[0]):
                    return _lit(n.args[0])
            if isinstance(n, ast.Subscript) and _dotted(n.value) in ("os.environ", "environ") and _lit(n.slice):
                return _lit(n.slice)
        return ""

    def resolve_call(self, file: str, func: ast.AST) -> tuple[str, str] | None:
        """(file, function name) when the call certainly targets a function of this project."""
        if isinstance(func, ast.Name):
            if func.id in self.funcs.get(file, {}):
                return file, func.id
            imp = self.imports.get(file, {}).get(func.id)
            if imp and imp[0] == "name" and imp[2] in self.funcs.get(imp[1], {}):
                return imp[1], imp[2]
        elif isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            imp = self.imports.get(file, {}).get(func.value.id)
            if imp and imp[0] == "module" and func.attr in self.funcs.get(imp[1], {}):
                return imp[1], func.attr
        return None

    def resolve_const(self, file: str, node: ast.AST) -> tuple[str, str] | None:
        """(file, NAME) of a module-level variable that an expression names."""
        if isinstance(node, ast.Name) and node.id in self.consts.get(file, {}):
            return file, node.id
        if isinstance(node, ast.Name):
            imp = self.imports.get(file, {}).get(node.id)
            if imp and imp[0] == "name" and imp[2] in self.consts.get(imp[1], {}):
                return imp[1], imp[2]
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            imp = self.imports.get(file, {}).get(node.value.id)
            if imp and imp[0] == "module" and node.attr in self.consts.get(imp[1], {}):
                return imp[1], node.attr
        return None

    def handler(self, file: str, name: str, line: int) -> ast.AST | None:
        tree = self.trees.get(file)
        if tree is None:
            return None
        best = None
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
                if node.lineno == line:
                    return node
                best = best or node
        return best

    # ------------------------------------------------------------ access
    def access(self, file: str, node: ast.AST) -> dict:
        """Who may call a route, as far as its decorators say."""
        out = {"roles": [], "permissions": [], "signed_in": False, "evidence": [], "unread": []}
        for deco in getattr(node, "decorator_list", []):
            name = _name(deco)
            if name in ROUTE_DECOS and isinstance(deco, ast.Call) and deco.args and _lit(deco.args[0]) is not None:
                continue
            text = "@" + _src(deco, 120)
            lits: list[str] = []
            if isinstance(deco, ast.Call):
                for a in deco.args:
                    lits += _strings(a)
                for kw in deco.keywords:
                    if kw.arg and re.search(r"role|group|perm|scope|allow", kw.arg, re.I):
                        lits += _strings(kw.value)
            ev = {"file": file, "line": deco.lineno, "text": text}
            if lits and PERMISSION_WORD.search(name) and not re.search(r"role|group", name, re.I):
                out["permissions"] += [x for x in lits if x not in out["permissions"]]
                out["evidence"].append(ev)
            elif lits and ROLE_WORD.search(name):
                out["roles"] += [x for x in lits if x not in out["roles"]]
                out["evidence"].append(ev)
            elif SIGNED_IN.match(name):
                out["signed_in"] = True
                out["evidence"].append(ev)
            elif not lits and (m := ROLE_FROM_NAME.match(name)) and m.group(1).lower() in ROLE_NAMES:
                out["roles"].append(m.group(1).lower())
                out["evidence"].append({**ev, "from_name": True})
            elif name not in QUIET_DECOS:
                out["unread"].append(ev)
        return out

    # ------------------------------------------------------------ effects
    def effects(self, file: str, node: ast.AST, max_depth: int = 4) -> list[dict]:
        out: list[dict] = []
        self._visited: set = set()                  # a helper reached twice with the same inputs is read once
        self._walk(file, node, "", {}, {}, set(), 0, max_depth, out, None, [])
        return out

    @staticmethod
    def _conditions(node: ast.AST) -> dict[int, list[str]]:
        """For every node of a function: the tests of the ``if`` statements it sits inside."""
        found: dict[int, list[str]] = {}

        def visit(n: ast.AST, conds: list[str]) -> None:
            for child in ast.iter_child_nodes(n):
                c = conds
                if isinstance(n, (ast.If, ast.IfExp)) and child is not n.test:
                    body = n.body if isinstance(n.body, list) else [n.body]
                    test = _src(n.test, 120)
                    c = conds + [test if any(child is b for b in body) else f"not ({test})"]
                found[id(child)] = c
                visit(child, c)
        visit(node, [])
        return found

    def _walk(self, file: str, node: ast.AST, via: str, files_in: dict, names_in: dict, seen: set, depth: int,
              max_depth: int, out: list[dict], root: int | None, when_in: list[str]) -> None:
        """``files_in``: variable -> upload field whose file object it holds.
        ``names_in``: variable -> upload field whose stored name it holds.
        ``root``: line in the route handler that led here; ``when_in``: conditions on that path."""
        files, names = dict(files_in), dict(names_in)
        conds = self._conditions(node)

        def add(kind: str, at: ast.AST, **data) -> None:
            line = getattr(at, "lineno", 0)
            when = when_in + conds.get(id(at), [])
            out.append({"kind": kind, "file": file, "line": line, "via": via, "root": root if root is not None else line,
                        "when": when, **data})

        def field_access(n: ast.AST) -> tuple[str, str] | None:
            """request.form["x"], request.files.get("x") … -> (source, field)."""
            if isinstance(n, ast.Subscript):
                base, key = _dotted(n.value), _lit(n.slice)
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in ("get", "getlist") and n.args:
                base, key = _dotted(n.func.value), _lit(n.args[0])
            else:
                return None
            if key is None or "." not in base:
                return None
            owner, attr = base.rsplit(".", 1)
            if owner.split(".")[-1] not in ("request", "req") or attr not in REQUEST_SOURCES:
                return None
            return REQUEST_SOURCES[attr], key

        def upload_in(expr: ast.AST) -> str:
            for n in ast.walk(expr):
                fa = field_access(n)
                if fa and fa[0] == "file":
                    return fa[1]
                if isinstance(n, ast.Name) and n.id in files:
                    return files[n.id]
            return ""

        def dir_of(expr: ast.AST) -> dict:
            """The module-level folder variable and literal file name an expression is built from."""
            info = {"expr": _src(expr, 100)}
            for n in ast.walk(expr):
                c = self.resolve_const(file, n)
                if c and "dir" not in info:
                    info["dir"] = f"{c[0]}:{c[1]}"
                    info["dir_name"] = c[1]
                    env = self.consts[c[0]][c[1]].get("env")
                    if env:
                        info["dir_env"] = env
                if _lit(n) and re.search(r"\.\w{2,5}$", _lit(n)) and "name" not in info:
                    info["name"] = _lit(n)
            return info

        # variables that hold an uploaded file, or the name it was stored under (assignments first)
        body_nodes = list(ast.walk(node))
        for n in body_nodes:
            if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
                up = upload_in(n.value)
                if not up:
                    continue
                stores = any(isinstance(c, ast.Call) and (self.resolve_call(file, c.func) or
                             (isinstance(c.func, ast.Attribute) and c.func.attr == "save")) for c in ast.walk(n.value))
                (names if stores else files)[n.targets[0].id] = up

        handled_sql: set[int] = set()
        for n in body_nodes:
            if isinstance(n, ast.If) and n is not node:
                outcome = []
                for st in n.body[:4]:
                    call = st.value if isinstance(st, (ast.Expr, ast.Return)) and isinstance(getattr(st, "value", None), ast.Call) else None
                    if call is not None:
                        cn = _name(call.func)
                        if cn == "flash" and call.args and _lit(call.args[0]):
                            outcome.append(f'shows the message "{_lit(call.args[0])}"')
                        elif cn == "abort" and call.args:
                            outcome.append(f"stops with {_src(call, 60)}")
                        elif cn == "redirect":
                            outcome.append("redirects" + self._redirect_text(call))
                        elif cn in RENDER_FUNCS:
                            tpl = next((_lit(a) for a in call.args if _lit(a)), "")
                            outcome.append(f"shows {tpl}" if tpl else "renders a page")
                    elif isinstance(st, ast.Raise):
                        outcome.append("raises " + (_src(st.exc, 60) if st.exc else "again"))
                    elif isinstance(st, ast.Return) and st.value is None:
                        outcome.append("returns early")
                add("branch", n, test=_src(n.test), outcome="; ".join(outcome), has_else=bool(n.orelse))
            elif isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                c = self.resolve_const(file, n)
                if c and self.consts[c[0]][c[1]].get("env"):
                    add("setting", n, name=self.consts[c[0]][c[1]]["env"], variable=c[1], defined_file=c[0],
                        defined_line=self.consts[c[0]][c[1]]["line"])
            elif isinstance(n, ast.Attribute) and isinstance(n.ctx, ast.Load):
                c = self.resolve_const(file, n)
                if c and self.consts[c[0]][c[1]].get("env"):
                    add("setting", n, name=self.consts[c[0]][c[1]]["env"], variable=c[1], defined_file=c[0],
                        defined_line=self.consts[c[0]][c[1]]["line"])
                elif isinstance(n.value, ast.Name) and n.value.id == "settings" and n.attr.isupper():
                    add("setting", n, name=n.attr, variable="settings." + n.attr)
            elif isinstance(n, ast.JoinedStr):
                head = "".join(v.value for v in n.values if isinstance(v, ast.Constant) and isinstance(v.value, str))
                if SQL_START.match(head):
                    add("sql_dynamic", n, text=_src(n, 120))
            elif isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in handled_sql and SQL_START.match(n.value):
                parsed = parse_sql(n.value)
                if parsed:
                    add("sql", n, **parsed)
            fa = field_access(n)
            if fa:
                add("field", n, source=fa[0], name=fa[1])
            if isinstance(n, ast.Subscript) and _lit(n.slice):
                base = _dotted(n.value)
                if base in ("os.environ", "environ"):
                    add("setting", n, name=_lit(n.slice), variable="")
                elif base.endswith(".config") or base == "config":
                    add("setting", n, name=_lit(n.slice), variable=base)
            if not isinstance(n, ast.Call):
                continue
            fname, dotted = _name(n.func), _dotted(n.func)
            first = n.args[0] if n.args else None
            if first is not None and _lit(first) is not None and SQL_START.match(_lit(first)):
                params = []
                if len(n.args) > 1 and isinstance(n.args[1], (ast.Tuple, ast.List)):
                    for el in n.args[1].elts:
                        if _lit(el) is not None:
                            params.append(("lit", _lit(el)))
                        elif isinstance(el, ast.Name):
                            params.append(("name", el.id))
                        else:
                            params.append(None)
                parsed = parse_sql(_lit(first), params)
                handled_sql.add(id(first))
                if parsed:
                    for pc in parsed["param_columns"]:
                        if pc["variable"] in names:
                            pc["upload"] = names[pc["variable"]]
                    add("sql", n, **parsed)
            if dotted in ("os.environ.get", "os.getenv", "environ.get") and first is not None and _lit(first):
                add("setting", n, name=_lit(first), variable="")
            elif isinstance(n.func, ast.Attribute) and n.func.attr == "get" and _dotted(n.func.value).endswith("config") \
                    and first is not None and _lit(first):
                add("setting", n, name=_lit(first), variable=_dotted(n.func.value))
            if fname in RENDER_FUNCS:
                tpl = next((_lit(a) for a in n.args if _lit(a) and TEMPLATE_NAME.search(_lit(a))), None)
                if tpl:
                    add("render", n, template=tpl)
                elif fname == "render_template":
                    add("render_dynamic", n, text=_src(n, 100))
            elif fname == "redirect":
                target = self._redirect_target(n)
                if target:
                    add("redirect", n, **target)
            elif fname == "flash" and first is not None and _lit(first):
                add("message", n, text=_lit(first), how="flash")
            elif fname == "abort":
                msg = next((_lit(a) for a in n.args[1:] if _lit(a)), None) or \
                    next((_lit(k.value) for k in n.keywords if k.arg in ("description", "message", "detail") and _lit(k.value)), None)
                if msg:
                    add("message", n, text=msg, how=f"abort({_src(first, 10) if first is not None else ''})")
            elif fname == "HTTPException":
                msg = next((_lit(k.value) for k in n.keywords if k.arg == "detail" and _lit(k.value)), None)
                if msg:
                    add("message", n, text=msg, how="HTTPException")
            if isinstance(n.func, ast.Attribute) and n.func.attr == "save" and n.args:
                up = upload_in(n.func.value)
                add("file", n, op="store", upload=up, **dir_of(n.args[0]))
            elif fname == "open" and n.args:
                mode = _lit(n.args[1]) if len(n.args) > 1 else next((_lit(k.value) for k in n.keywords if k.arg == "mode"), None)
                if mode and any(ch in mode for ch in "wax"):
                    add("file", n, op="write", upload="", **dir_of(n.args[0]))
            elif fname in ("write_text", "write_bytes") and isinstance(n.func, ast.Attribute):
                add("file", n, op="write", upload="", **dir_of(n.func.value))
            elif fname in ("send_from_directory", "send_file", "FileResponse", "sendfile") and n.args:
                info = dir_of(ast.Tuple(elts=list(n.args[:2]), ctx=ast.Load()))
                info["expr"] = _src(n, 100)
                add("file", n, op="serve", upload="", **info)
            elif dotted in ("os.remove", "os.unlink", "shutil.rmtree") and n.args:
                add("file", n, op="delete", upload="", **dir_of(n.args[0]))
            elif fname == "unlink" and isinstance(n.func, ast.Attribute):
                add("file", n, op="delete", upload="", **dir_of(n.func.value))
            if dotted.startswith(HTTP_ROOTS) or fname == "urlopen":
                add("external", n, what="HTTP request", text=_src(n, 100))
            elif fname in STORAGE_METHODS:
                add("external", n, what="external storage", text=_src(n, 100))
            elif fname in MAIL_METHODS or dotted.startswith("smtplib."):
                add("external", n, what="e-mail", text=_src(n, 100))
            elif fname in BACKGROUND_METHODS and isinstance(n.func, ast.Attribute):
                add("background", n, text=_src(n, 100))
            elif fname == "Thread" and any(k.arg == "target" for k in n.keywords):
                add("background", n, text=_src(n, 100))
            target = self.resolve_call(file, n.func)
            if target and target != (file, getattr(node, "name", "")):
                tfile, tname = target
                callee = self.funcs[tfile][tname]
                label = (via + " → " if via else "") + (dotted or tname)
                add("call", n, func=tname, def_file=tfile, def_line=callee.lineno, end_line=getattr(callee, "end_lineno", callee.lineno),
                    label=dotted or tname)
                if depth < max_depth and target not in seen:
                    params = [a.arg for a in callee.args.args]
                    if params and params[0] in ("self", "cls"):
                        params = params[1:]
                    sub_files, sub_names = {}, {}
                    for i, a in enumerate(n.args):
                        if i < len(params) and isinstance(a, ast.Name):
                            if a.id in files:
                                sub_files[params[i]] = files[a.id]
                            if a.id in names:
                                sub_names[params[i]] = names[a.id]
                        elif i < len(params) and upload_in(a):
                            sub_files[params[i]] = upload_in(a)
                    for kw in n.keywords:
                        if kw.arg and isinstance(kw.value, ast.Name):
                            if kw.value.id in files:
                                sub_files[kw.arg] = files[kw.value.id]
                            if kw.value.id in names:
                                sub_names[kw.arg] = names[kw.value.id]
                    key = (target, tuple(sorted(sub_files.items())), tuple(sorted(sub_names.items())))
                    if key in self._visited:
                        continue
                    self._visited.add(key)
                    self._walk(tfile, callee, label, sub_files, sub_names, seen | {target}, depth + 1, max_depth, out,
                               root if root is not None else n.lineno, when_in + conds.get(id(n), []))

    @staticmethod
    def _redirect_target(call: ast.Call) -> dict | None:
        for n in ast.walk(call):
            if isinstance(n, ast.Call) and _name(n.func) in ("url_for", "reverse") and n.args and _lit(n.args[0]):
                return {"endpoint": _lit(n.args[0]).rsplit(".", 1)[-1]}
        if call.args and _lit(call.args[0]) and _lit(call.args[0]).startswith("/"):
            return {"path": _lit(call.args[0])}
        return None

    def _redirect_text(self, call: ast.Call) -> str:
        t = self._redirect_target(call)
        if not t:
            return ""
        return f" to `{t['endpoint']}`" if "endpoint" in t else f" to {t['path']}"


# ---------------------------------------------------------------------------- other languages

JS_ROLE = re.compile(r"\b(\w*(?:role|authori[sz]e|permit|allow|restrict)\w*)\(\s*\[?\s*((?:['\"][^'\"]+['\"]\s*,?\s*)+)\]?\s*\)", re.I)
JS_SIGNED_IN = re.compile(r"\b(requireAuth|isAuthenticated|ensureLoggedIn|ensureAuthenticated|requireLogin|verifyToken|authenticate\w*)\b")
CS_AUTHORIZE = re.compile(r"\[\s*Authorize\s*(?:\((.*?)\))?\s*\]")
CS_ROLES = re.compile(r"Roles\s*=\s*\"([^\"]+)\"")


def access_other(text_lines: list[str], lang: str, file: str, line: int) -> dict:
    """Role checks written directly on a route in JavaScript/TypeScript or C#."""
    out = {"roles": [], "permissions": [], "signed_in": False, "evidence": [], "unread": []}
    if not (0 < line <= len(text_lines)):
        return out
    if lang in ("javascript", "typescript"):
        stmt = text_lines[line - 1]
        head = stmt.split("=>", 1)[0].split("function", 1)[0]
        for m in JS_ROLE.finditer(head):
            out["roles"] += [r for r in re.findall(r"['\"]([^'\"]+)['\"]", m.group(2)) if r not in out["roles"]]
            out["evidence"].append({"file": file, "line": line, "text": m.group(0)})
        m = JS_SIGNED_IN.search(head)
        if m and not out["roles"]:
            out["signed_in"] = True
            out["evidence"].append({"file": file, "line": line, "text": m.group(0)})
    elif lang == "csharp":
        i = line - 2
        same = text_lines[line - 1]
        if ".RequireAuthorization(" in same:
            out["signed_in"] = True
            out["evidence"].append({"file": file, "line": line, "text": ".RequireAuthorization(…)"})
        while i >= 0 and text_lines[i].strip().startswith("["):
            m = CS_AUTHORIZE.search(text_lines[i])
            if m:
                roles = CS_ROLES.search(m.group(1) or "")
                if roles:
                    out["roles"] += [r.strip() for r in roles.group(1).split(",") if r.strip() and r.strip() not in out["roles"]]
                else:
                    out["signed_in"] = True
                out["evidence"].append({"file": file, "line": i + 1, "text": text_lines[i].strip()[:120]})
            i -= 1
    return out
