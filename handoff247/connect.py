"""Cross-file linking: turns per-file facts into edges and the connection maps
(entry modes, dispatch tables and who calls each operation, routes, MCP tools,
launch chain, environment variables, ports)."""
from __future__ import annotations

import posixpath
import re
import sys
from collections import Counter, defaultdict

from .model import Edge, Fact, FileInfo, Project

PATH_TOKEN = re.compile(r"[A-Za-z0-9_.~%$:{}()\\/@+-]*[A-Za-z0-9_-]\.[A-Za-z0-9]{1,10}(?![\w])")
PORT_LITERAL = re.compile(r"\b(?:localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\]|\*|\+):(\d{2,5})\b")
STDLIB = set(getattr(sys, "stdlib_module_names", ())) | {"__future__"}
# calls that take a string key but are lookups/formatting, never "run operation X"
ACCESSORS = {"get", "group", "start", "end", "span", "pop", "setdefault", "getattr", "hasattr", "setattr",
             "Text", "GetValue", "GetProperty", "GetString", "getItem", "setItem", "getAttribute", "setAttribute",
             "querySelector", "querySelectorAll", "getElementById", "closest", "t", "T", "_", "gettext", "translate",
             "format", "split", "replace", "startswith", "endswith", "StartsWith", "EndsWith", "find", "index",
             "count", "join", "append", "add", "remove", "has", "contains", "Contains", "ContainsKey",
             "TryGetValue", "Add", "Remove", "includes", "push", "Equals", "equals", "print", "log", "warn",
             "error", "info", "debug", "WriteLine", "Write", "assert", "assertEqual", "assertIn", "check",
             "Header", "header", "cookie", "param", "query", "on", "off", "emit", "addEventListener", "env",
             "getenv", "dataset", "matches", "test", "match", "search", "fullmatch", "compile", "sub", "findall"}
BATCH_DYNAMIC = {"errorlevel", "cd", "date", "time", "random", "cmdextversion", "cmdcmdline", "highestnumanodenumber"}
SYSTEM_ENV = {"PATH", "HOME", "USERPROFILE", "USERNAME", "USER", "LOCALAPPDATA", "APPDATA", "PROGRAMFILES",
              "PROGRAMFILES(X86)", "PROGRAMDATA", "TEMP", "TMP", "TMPDIR", "SYSTEMROOT", "WINDIR", "COMSPEC",
              "PATHEXT", "SHELL", "LANG", "PWD", "OS", "COMPUTERNAME", "HOSTNAME", "XDG_CONFIG_HOME",
              "XDG_DATA_HOME", "XDG_CACHE_HOME", "PSMODULEPATH", "PROCESSOR_ARCHITECTURE"}


def area_of(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else "(root)"


class FileIndex:
    def __init__(self, files: list[FileInfo]):
        self.paths = {f.path for f in files}
        self.lower = {f.path.lower(): f.path for f in files}
        self.by_base = defaultdict(list)
        for f in files:
            self.by_base[f.path.rsplit("/", 1)[-1].lower()].append(f.path)
        self.assemblies = {}

    def resolve(self, token: str, from_file: str) -> str | None:
        token = token.strip().strip("'\"`").replace("\\", "/")
        token = token.split("?", 1)[0].split("#", 1)[0]
        relative = token.startswith(("./", "../"))
        # %~dp0x.ps1, $PSScriptRoot/x, ${root}/x, {ROOT}/x  ->  x
        token = re.sub(r"%~[a-z]*\d|%[A-Za-z_]\w*%|\$\{?[A-Za-z_]\w*\}?|\{[^}]*\}|\$\([^)]*\)", "/", token)
        segs = [s for s in token.split("/") if s]
        # drop leading segments that are variables, drive letters or dots
        while segs and (re.search(r"[$%{}~()]|^[A-Za-z]:$", segs[0]) or segs[0] in (".", "..")):
            segs = segs[1:]
        if not segs:
            return None
        here = posixpath.dirname(from_file)
        if relative:
            cand = posixpath.normpath(posixpath.join(here, token))
            if cand in self.paths:
                return cand
        for k in range(len(segs)):
            suffix = "/".join(segs[k:])
            if k == len(segs) - 1:
                # bare file name: same folder, project root, or unique in project
                for cand in (posixpath.join(here, suffix) if here else suffix, suffix):
                    if cand in self.paths:
                        return cand
                    if cand.lower() in self.lower:
                        return self.lower[cand.lower()]
                hits = self.by_base.get(suffix.lower(), [])
                if len(hits) == 1 and len(suffix) >= 6:
                    return hits[0]
                return None
            for cand in (posixpath.join(here, suffix) if here else suffix, suffix):
                if cand in self.paths:
                    return cand
                if cand.lower() in self.lower:
                    return self.lower[cand.lower()]
            ends = [p for p in self.paths if p.lower().endswith("/" + suffix.lower())]
            if len(ends) == 1:
                return ends[0]
        return None

    def build_output(self, token: str) -> str | None:
        base = token.replace("\\", "/").rstrip("'\"` ").rsplit("/", 1)[-1].lower()
        m = re.match(r"(.+)\.(dll|exe)$", base)
        if m and m.group(1) in self.assemblies:
            return self.assemblies[m.group(1)]
        return None


def link(project: Project) -> None:
    files = {f.path: f for f in project.files}
    facts = project.facts
    idx = FileIndex(project.files)
    for fc in facts:
        if fc.kind == "build_target":
            idx.assemblies[fc.data["assembly"].lower()] = fc.file
    edges: dict[tuple[str, str, str], Edge] = {}

    def add_edge(src: str, dst: str, kind: str, line: int, label: str = "") -> None:
        if src == dst or not src or not dst:
            return
        key = (src, dst, kind)
        e = edges.get(key)
        if e:
            e.count += 1
            if label and label not in e.label.split(", "):
                e.label = (e.label + ", " + label).strip(", ")
        else:
            edges[key] = Edge(src, dst, kind, line, 1, label)

    # ---------------------------------------------------------------- C# types
    types: dict[str, list[str]] = defaultdict(list)
    type_kind: dict[str, str] = {}
    for f in project.files:
        if f.lang == "csharp":
            for s in f.symbols:
                if s.kind in ("class", "record", "record struct", "record class", "struct", "interface", "enum"):
                    if f.path not in types[s.name]:
                        types[s.name].append(f.path)
                    type_kind[s.name] = s.kind
    ctor_tokens = defaultdict(set)
    for fc in facts:
        if fc.kind == "ctor_dep":
            for p in fc.data["params"]:
                ctor_tokens[fc.file].update(p["tokens"])
    base_tokens = defaultdict(set)
    for fc in facts:
        if fc.kind == "bases":
            base_tokens[fc.file].update(fc.data["bases"])
    for f in project.files:
        if f.lang != "csharp" or not f.code:
            continue
        own = {s.name for s in f.symbols if s.kind not in ("method", "constructor")}
        counts = Counter(re.findall(r"\b[A-Z_][A-Za-z0-9_]*\b", f.code))
        first_line = {}
        for name in counts:
            if name in types and name not in own:
                m = re.search(r"\b" + re.escape(name) + r"\b", f.code)
                first_line[name] = f.code.count("\n", 0, m.start()) + 1 if m else 0
        for name, line in first_line.items():
            kind = "injects" if name in ctor_tokens[f.path] else ("extends" if name in base_tokens[f.path] else "uses")
            for dst in types[name]:
                add_edge(f.path, dst, kind, line, name)

    # ---------------------------------------------------------------- imports
    py_files = [f.path for f in project.files if f.lang == "python"]
    py_mods = {}
    for p in py_files:
        mod = p[:-3].replace("/", ".")
        if mod.endswith(".__init__"):
            mod = mod[: -len(".__init__")]
        py_mods[mod] = p
    external = defaultdict(set)
    for f in project.files:
        if not f.imports:
            continue
        for target, line in f.imports:
            dst = None
            if f.lang == "python":
                dst = _resolve_py(target, f.path, py_mods)
                if not dst and not target.startswith("."):
                    top = target.split(".")[0]
                    if top and top not in STDLIB:
                        external[top].add(f.path)
                if dst:
                    add_edge(f.path, dst, "imports", line)
                continue
            if f.lang in ("javascript", "typescript", "html", "css"):
                dst = _resolve_web(target, f.path, idx, project)
                if dst:
                    add_edge(f.path, dst, "loads" if f.lang == "html" else "imports", line)
                elif not target.startswith((".", "/", "http:", "https:", "data:")) and f.lang in ("javascript", "typescript"):
                    pkg = "/".join(target.split("/")[:2]) if target.startswith("@") else target.split("/")[0]
                    if not pkg.startswith("node:"):
                        external[pkg].add(f.path)
                continue
            if f.lang == "markdown":
                dst = idx.resolve(target, f.path) if not target.endswith("/") else None
                if dst:
                    add_edge(f.path, dst, "documents", line)
                continue
            if f.lang == "msbuild":
                dst = idx.resolve(target, f.path)
                if dst:
                    add_edge(f.path, dst, "references", line)
                continue
            if f.lang == "json":
                dst = idx.resolve(target, f.path)
                if dst:
                    add_edge(f.path, dst, "refers", line)

    # ---------------------------------------------------------------- entry modes
    entries = [fc for fc in facts if fc.kind == "entry"]
    modes = [fc for fc in facts if fc.kind == "mode"]
    tables_by_id: dict[str, dict] = {}
    for fc in facts:
        if fc.kind == "dispatch_table":
            tables_by_id[fc.data["table"]] = {"id": fc.data["table"], "file": fc.file, "line": fc.line,
                                              "cls": fc.data["cls"], "method": fc.data["method"],
                                              "selector": fc.data["selector"], "ops": {}}
    for fc in facts:
        if fc.kind == "dispatch" and fc.data["table"] in tables_by_id:
            t = tables_by_id[fc.data["table"]]
            htype = fc.data["handler_type"]
            hfile = types.get(htype, [""])[0] if htype else ""
            hm = fc.data["handler_method"]
            if not hfile and "." in hm:
                # python: {"x": module.func} -> the imported module's file
                base = hm.split(".")[0]
                for e in list(edges.values()):
                    if e.src == fc.file and e.kind == "imports" and posixpath.splitext(posixpath.basename(e.dst))[0] == base:
                        hfile = e.dst
                        break
            if fc.data["key"] not in t["ops"]:
                t["ops"][fc.data["key"]] = {"key": fc.data["key"], "line": fc.line, "handler_type": htype,
                                            "handler_method": fc.data["handler_method"], "handler_file": hfile,
                                            "expr": fc.data["expr"], "used_by": [], "documented_in": [], "mcp_tools": [],
                                            "routes": []}
                if hfile:
                    add_edge(t["file"], hfile, "dispatches", fc.line, fc.data["key"].split(".")[0])
    key_tables: dict[str, list[str]] = defaultdict(list)
    for tid, t in tables_by_id.items():
        for k in t["ops"]:
            key_tables[k].append(tid)
    table_methods = {t["method"] for t in tables_by_id.values() if t["method"]}

    def code_range(path: str, start: int, end: int) -> str:
        f = files.get(path)
        if not f or not f.code:
            return ""
        return "\n".join(f.code.split("\n")[start - 1:end])

    def text_range(path: str, start: int, end: int) -> str:
        f = files.get(path)
        if not f:
            return ""
        src = f.code_str or f.text
        return "\n".join(src.split("\n")[start - 1:end])

    mode_info = []
    var_types: dict[str, dict[str, str]] = {}
    for m in modes:
        if m.file not in var_types:
            src = files[m.file].code or ""
            var_types[m.file] = {vm.group(1): vm.group(2) for vm in
                                 re.finditer(r"\bvar\s+(\w+)\s*=\s*new\s+([A-Z_]\w*)\s*\(", src) if vm.group(2) in types}
        block = code_range(m.file, m.data["start"], m.data["end"])
        block_str = text_range(m.file, m.data["start"], m.data["end"])
        used_set = {n for n in re.findall(r"\b[A-Z_]\w*\b", block) if n in types}
        vt = var_types[m.file]
        used_set |= {vt[v] for v in re.findall(r"\b([a-z_]\w*)\s*\.", block) if v in vt}
        used = sorted(used_set)
        tables = []
        for tid, t in tables_by_id.items():
            if t["method"] and re.search(r"\.\s*" + re.escape(t["method"]) + r"\s*\(", block):
                tables.append(tid)
        transports = []
        if "WithStdioServerTransport" in block:
            transports.append("MCP over stdio")
        if "WithHttpTransport" in block:
            transports.append("MCP over HTTP")
        if re.search(r"\bWebApplication\b|\.UseUrls\(|\.MapGet\(|\.MapPost\(", block):
            transports.append("HTTP server")
        if re.search(r"IHostedService|AddHostedService|BackgroundService", block):
            transports.append("background service")
        mcp_types = [u for u in used if any("mcp-tool-type" in files[p].tags for p in types[u])]
        info = {"name": m.data["name"], "var": m.data["var"], "file": m.file, "line": m.line, "start": m.data["start"],
                "end": m.data["end"], "body": m.data["body"], "default": m.data["default"], "uses": used,
                "tables": tables, "transports": transports, "mcp_types": mcp_types, "routes": [],
                "reads_stdin": "Console.In" in block or "ReadToEnd" in block_str, "op_carrying": bool(tables)}
        mode_info.append(info)
        for u in used:
            for p in types[u]:
                add_edge(m.file, p, "mode:" + m.data["name"], m.line, m.data["name"])
    mode_info.sort(key=lambda mi: (mi["file"], mi["start"], not mi["default"], mi["line"]))
    op_modes = [mi["name"] for mi in mode_info if mi["op_carrying"]]
    mode_names = {mi["name"] for mi in mode_info}

    # ---------------------------------------------------------------- routes
    routes = []
    for fc in facts:
        if fc.kind != "route":
            continue
        r = {"verb": fc.data["verb"], "path": fc.data["path"], "file": fc.file, "line": fc.line,
             "forwards_to": "", "modes": [], "handler": fc.data.get("handler", "")}
        f = files[fc.file]
        receivers = {mm.group(1): mm.group(2) for mm in re.finditer(r"\bvar\s+(\w+)\s*=\s*new\s+(\w+)\s*\(", f.code or "")}
        for c in fc.data.get("calls", []):
            for tid, t in tables_by_id.items():
                if c["method"] == t["method"] and (receivers.get(c["recv"]) == t["cls"] or c["recv"].lower() == t["cls"].lower()):
                    r["forwards_to"] = tid
        for mi in mode_info:
            if mi["file"] == fc.file and mi["start"] <= fc.line <= mi["end"]:
                r["modes"].append(mi["name"])
                mi["routes"].append(f'{r["verb"]} {r["path"]}')
        routes.append(r)
    static = [fc for fc in facts if fc.kind == "static_files"]

    # ---------------------------------------------------------------- MCP tools
    mcp_tools = []
    for fc in facts:
        if fc.kind != "mcp_tool":
            continue
        op, table = "", ""
        for lit in fc.data["literals"]:
            if lit in key_tables:
                op, table = lit, key_tables[lit][0]
                break
        tool = {"name": fc.data["name"], "name_source": fc.data["name_source"], "file": fc.file, "line": fc.line,
                "method": fc.data["method"], "cls": fc.data["cls"], "description": fc.data["description"],
                "op": op, "table": table, "params": fc.data.get("params", [])}
        mcp_tools.append(tool)
        if op:
            tables_by_id[table]["ops"][op]["mcp_tools"].append(tool["name"])

    # ---------------------------------------------------------------- consumers of operation keys
    spans = defaultdict(dict)       # file -> name -> (start, end)
    for f in project.files:
        for s in f.symbols:
            if s.kind in ("method", "function", "export", "constructor") and s.end_line:
                spans[f.path].setdefault(s.name, (s.line, s.end_line))
    for fc in facts:
        if fc.kind == "func_spans":
            for name, a, b in fc.data["spans"]:
                spans[fc.file].setdefault(name, (a, b))
    http_by_file = defaultdict(list)
    for fc in facts:
        if fc.kind == "http_call":
            http_by_file[fc.file].append(fc)
    launch_by_file = defaultdict(list)
    for fc in facts:
        if fc.kind == "launch":
            launch_by_file[fc.file].append(fc)

    def channel_of(path: str, func: str, seen: set | None = None) -> dict:
        seen = seen if seen is not None else set()
        if (path, func) in seen:
            return {}
        seen.add((path, func))
        if func in table_methods:
            t = next(t for t in tables_by_id.values() if t["method"] == func)
            return {"channel": "in-process", "detail": f'{t["cls"]}.{t["method"]}'}
        span = spans.get(path, {}).get(func)
        if span:
            a, b = span
            for h in http_by_file[path]:
                if a <= h.line <= b:
                    route = _match_route(h.data["path"], routes)
                    return {"channel": "http", "detail": h.data["path"], "route": route, "wrapper": f"{path}:{a}"}
            for l in launch_by_file[path]:
                if a <= l.line <= b:
                    toks = re.findall(r"[\w.-]+", l.data["text"])
                    mode = next((t for t in toks if t in mode_names), "")
                    return {"channel": "process", "detail": l.data["text"], "mode": mode, "wrapper": f"{path}:{a}"}
            body = text_range(path, a, b)
            for tid, t in tables_by_id.items():
                if t["method"] and re.search(r"\.\s*" + re.escape(t["method"]) + r"\s*\(", body):
                    return {"channel": "in-process", "detail": f'{t["cls"]}.{t["method"]}', "wrapper": f"{path}:{a}"}
            # a wrapper that calls another local wrapper (cli() -> command() -> subprocess.run)
            for inner in dict.fromkeys(re.findall(r"(?<![\w.])([A-Za-z_]\w*)\s*\(", body)):
                if inner != func and inner in spans.get(path, {}):
                    got = channel_of(path, inner, seen)
                    if got.get("channel"):
                        got["wrapper"] = f"{path}:{a}"
                        return got
            return {"channel": "", "wrapper": f"{path}:{a}"}
        for e in list(edges.values()):
            if e.src == path and e.kind == "imports":
                got = channel_of(e.dst, func, seen)
                if got:
                    got["via_import"] = e.dst
                    return got
        # not defined here: a file that imports this one defines a function of the same name
        # (typically passed in as a parameter). Reported as an inference, never as fact.
        f = files.get(path)
        if f and f.code and re.search(r"\(\s*[^()]*\b" + re.escape(func) + r"\b[^()]*\)\s*(?:=>|\{)", f.code):
            for e in list(edges.values()):
                if e.dst == path and e.kind == "imports" and func in spans.get(e.src, {}):
                    got = channel_of(e.src, func, seen)
                    if got.get("channel"):
                        got["inferred"] = f"{func} is a parameter here; same-name function in {e.src}, which imports this file"
                        return got
        return {}

    groups = defaultdict(list)
    for fc in facts:
        if fc.kind == "call" and fc.data["value"] in key_tables and fc.data["func"] not in ACCESSORS:
            groups[(fc.file, fc.data["func"])].append(fc)
    consumers = []
    for (path, func), calls in sorted(groups.items()):
        keys = {c.data["value"] for c in calls}
        f = files[path]
        if func in table_methods and any(t["file"] == path and t["method"] == func for t in tables_by_id.values()):
            continue
        strong = len(keys) >= 2 or any("." in k for k in keys) or func in table_methods
        if not strong:
            continue
        ch = channel_of(path, func)
        consumer = {"file": path, "func": func, "keys": sorted(keys), "calls": len(calls),
                    "first_line": min(c.line for c in calls), **ch}
        consumers.append(consumer)
        for c in calls:
            for tid in key_tables[c.data["value"]]:
                op = tables_by_id[tid]["ops"][c.data["value"]]
                op["used_by"].append({"file": path, "line": c.line, "via": f"{func}()", "channel": ch.get("channel", "")})
                add_edge(path, tables_by_id[tid]["file"], "calls-op", c.line, ch.get("channel", "") or f"{func}()")

    # CLI usages "<mode> <op>" in scripts and documentation code blocks
    cli_usage = []
    if op_modes and key_tables:
        rx = re.compile(r"(?<![\w-])(" + "|".join(map(re.escape, op_modes)) + r")\s+['\"]?([A-Za-z][\w.-]*)")
        for fc in facts:
            if fc.kind == "doc_code":
                for ln, text in fc.data["lines"]:
                    for m in rx.finditer(text):
                        if m.group(2) in key_tables:
                            cli_usage.append({"file": fc.file, "line": ln, "mode": m.group(1), "op": m.group(2), "doc": True})
        for f in project.files:
            if f.category in ("script", "test") and f.lang in ("powershell", "shell", "batch") and f.text:
                for ln, text in enumerate(f.text.split("\n"), 1):
                    for m in rx.finditer(text):
                        if m.group(2) in key_tables:
                            cli_usage.append({"file": f.path, "line": ln, "mode": m.group(1), "op": m.group(2), "doc": False})
        for u in cli_usage:
            for tid in key_tables[u["op"]]:
                op = tables_by_id[tid]["ops"][u["op"]]
                target = op["documented_in"] if u["doc"] else op["used_by"]
                entry = {"file": u["file"], "line": u["line"], "via": f'{u["mode"]} {u["op"]}', "channel": "process"}
                if entry not in target:
                    target.append(entry)

    for tid, t in tables_by_id.items():
        for r in routes:
            if r["forwards_to"] == tid:
                for op in t["ops"].values():
                    op["routes"].append(f'{r["verb"]} {r["path"]}')

    # ---------------------------------------------------------------- launches and file references
    launch_chain = []
    for fc in facts:
        if fc.kind != "launch":
            continue
        targets = []
        text = fc.data["text"]
        for tok in PATH_TOKEN.findall(text):
            dst = idx.resolve(tok, fc.file) or idx.build_output(tok)
            if dst and dst != fc.file and dst not in targets:
                targets.append(dst)
        arg = ""
        for dst in targets:
            base = dst.rsplit("/", 1)[-1]
            mm = re.search(re.escape(base) + r"[\"']?\s+([A-Za-z][\w.-]*)", text, re.I)
            if mm:
                arg = mm.group(1)
        toks = re.findall(r"(?<![\w{-])[A-Za-z][\w.-]*", text)
        mode = next((t for t in toks if t in mode_names), "")
        urls = re.findall(r"https?://[^\s\"'`]+", text)
        launch_chain.append({"file": fc.file, "line": fc.line, "cmd": fc.data["cmd"], "text": text,
                             "targets": targets, "arg": arg, "mode": mode, "urls": urls, "ci": fc.data.get("ci", False),
                             "script": fc.data.get("script", "")})
        for dst in targets:
            add_edge(fc.file, dst, "runs", fc.line, arg or mode)
    # string literals that name another project file or a build output
    launching_files = {fc.file for fc in facts if fc.kind == "launch"}
    for f in project.files:
        if f.category not in ("code", "script", "test", "web") or not f.strings:
            continue
        for value, line in f.strings:
            if len(value) > 300 or "\n" in value:
                continue
            for tok in PATH_TOKEN.findall(value):
                dst = idx.resolve(tok, f.path)
                if dst and dst != f.path:
                    add_edge(f.path, dst, "refers", line)
                out = idx.build_output(tok)
                if out and out != f.path:
                    add_edge(f.path, out, "runs" if f.path in launching_files else "refers", line, "build output")

    # MCP client configurations (how outside AI tools start this project)
    mcp_clients = []
    for fc in facts:
        if fc.kind != "mcp_client":
            continue
        target, mode = "", ""
        for a in [fc.data["command"], *fc.data["args"]]:
            target = target or idx.build_output(a) or idx.resolve(a, fc.file) or ""
            if a in mode_names:
                mode = a
        mcp_clients.append({**fc.data, "file": fc.file, "line": fc.line, "target": target, "mode": mode})
        if target:
            add_edge(fc.file, target, "runs", fc.line, mode or "mcp")

    # ---------------------------------------------------------------- environment & ports
    env = defaultdict(lambda: {"reads": [], "writes": [], "system": False})
    for fc in facts:
        if fc.kind in ("env_read", "env_write") and fc.data["name"].lower() in BATCH_DYNAMIC:
            continue
        if fc.kind == "env_read":
            env[fc.data["name"]]["reads"].append({"file": fc.file, "line": fc.line, "default": fc.data.get("default", "")})
        elif fc.kind == "env_write":
            env[fc.data["name"]]["writes"].append({"file": fc.file, "line": fc.line, "value": fc.data.get("value", "")})
    for name, uses in env.items():
        uses["system"] = name.upper() in SYSTEM_ENV
    ports = []
    seen_ports = set()

    def add_port(value: str, path: str, line: int, source: str) -> None:
        if not value.isdigit() or not (10 <= int(value) <= 65535):
            return
        if (value, path) in seen_ports:
            return
        seen_ports.add((value, path))
        ports.append({"port": int(value), "file": path, "line": line, "source": source})
    for name, uses in env.items():
        if "PORT" in name.upper():
            for r in uses["reads"]:
                add_port(r["default"], r["file"], r["line"], f"{name} default")
            for w in uses["writes"]:
                add_port(w["value"], w["file"], w["line"], f"{name} set")
    for fc in facts:
        if fc.kind == "listen":
            for p in re.findall(r":(\d{2,5})", fc.data["value"]) or re.findall(r"^(\d{2,5})$", fc.data["value"]):
                add_port(p, fc.file, fc.line, "listen address")
    for f in project.files:
        if f.category == "docs":
            continue
        for value, line in f.strings:
            for p in PORT_LITERAL.findall(value):
                add_port(p, f.path, line, "address literal")
    ports.sort(key=lambda p: (p["port"], p["file"]))

    runtime_paths = []
    for fc in facts:
        if fc.kind == "path_literal":
            parts = [p for p in fc.data["parts"] if p and len(p) < 120 and not re.fullmatch(r"\.\w{1,6}", p)]
            if parts:
                runtime_paths.append({"file": fc.file, "line": fc.line, "parts": parts})

    packages = [{"file": fc.file, "line": fc.line, **fc.data} for fc in facts if fc.kind == "package"]
    for name, users in sorted(external.items()):
        packages.append({"file": sorted(users)[0], "line": 0, "name": name, "version": "", "ecosystem":
                         "import", "dev": False, "used_in": sorted(users)})

    # ---------------------------------------------------------------- hubs (shared foundations)
    code_kinds = {"uses", "injects", "imports", "extends"}
    indeg = defaultdict(set)
    for e in edges.values():
        if e.kind in code_kinds:
            indeg[e.dst].add(e.src)
    # a hub is used by at least half of the files (min 4) of its own language that use anything
    users_by_lang = defaultdict(set)
    for e in edges.values():
        if e.kind in code_kinds and e.src in files:
            users_by_lang[files[e.src].lang].add(e.src)
    hubs = []
    for p, srcs in indeg.items():
        lang = files[p].lang if p in files else ""
        if len(srcs) >= max(4, int(len(users_by_lang[lang]) * 0.5) + 1):
            hubs.append(p)
    hubs.sort(key=lambda p: -len(indeg[p]))

    # launch scripts/configs that reach a build target through other launch scripts
    targets = {fc.file for fc in facts if fc.kind == "build_target"} | {m["file"] for m in mode_info}
    reverse = defaultdict(list)
    for e in edges.values():
        if e.kind == "runs":
            reverse[e.dst].append(e.src)
    app_launchers: dict[str, int] = {}
    frontier = [(t, 0) for t in targets]
    while frontier:
        node, depth = frontier.pop()
        for src in reverse.get(node, []):
            f = files.get(src)
            if f and f.category in ("script", "config") and src not in app_launchers \
                    and not any(fc.kind == "mcp_client" and fc.file == src for fc in facts):
                app_launchers[src] = depth + 1
                frontier.append((src, depth + 1))

    project.edges = sorted(edges.values(), key=lambda e: (e.src, e.kind, e.dst))
    tables = []
    for t in tables_by_id.values():
        t = dict(t)
        t["ops"] = sorted(t["ops"].values(), key=lambda o: o["line"])
        tables.append(t)
    project.links = {
        "types": {k: v for k, v in sorted(types.items())},
        "entries": [{"file": e.file, "line": e.line, **e.data} for e in entries],
        "modes": mode_info,
        "tables": tables,
        "routes": routes,
        "static": [{"file": s.file, "line": s.line, **s.data} for s in static],
        "mcp_tools": mcp_tools,
        "mcp_clients": mcp_clients,
        "consumers": consumers,
        "cli_usage": cli_usage,
        "launches": launch_chain,
        "env": {k: env[k] for k in sorted(env)},
        "ports": ports,
        "runtime_paths": runtime_paths,
        "packages": packages,
        "hubs": [{"file": h, "used_by": len(indeg[h])} for h in hubs],
        "build_targets": [{"file": fc.file, **fc.data} for fc in facts if fc.kind == "build_target"],
        "subcommands": [{"file": fc.file, "line": fc.line, **fc.data} for fc in facts if fc.kind == "subcommand"],
        "script_params": [{"file": fc.file, "line": fc.line, **fc.data} for fc in facts if fc.kind == "script_params"],
        # launcher -> steps to the program (1 = starts it directly)
        "launchers": dict(sorted(app_launchers.items(), key=lambda kv: (kv[0].count("/"), -kv[1], kv[0].lower()))),
    }


def _match_route(path: str, routes: list[dict]) -> str:
    """Match a client-side path or path prefix to a server route template."""
    path = path.split("?", 1)[0]
    if path.startswith(("http://", "https://")):
        path = "/" + path.split("/", 3)[3] if path.count("/") >= 3 else "/"
    best = ""
    for r in routes:
        tpl = r["path"]
        if not tpl.startswith("/"):
            continue
        prefix = tpl.split("{", 1)[0]
        rx = "^" + re.sub(r"\\\{[^}]*\\\}", r"[^/]+", re.escape(tpl)) + "$"
        if re.match(rx, path) or (prefix != tpl and path == prefix) or (prefix != tpl and path.startswith(prefix) and path.endswith("/")):
            cand = f'{r["verb"]} {tpl}'
            if len(tpl) > len(best.split(" ", 1)[-1]):
                best = cand
    return best


def _resolve_py(target: str, importer: str, mods: dict[str, str]) -> str | None:
    here = posixpath.dirname(importer)
    if target.startswith("."):
        level = len(target) - len(target.lstrip("."))
        base = here
        for _ in range(level - 1):
            base = posixpath.dirname(base)
        rest = target.lstrip(".")
        mod = (base.replace("/", ".") + ("." + rest if rest else "")).strip(".")
        return mods.get(mod)
    if here:
        local = (here.replace("/", ".") + "." + target)
        if local in mods:
            return mods[local]
    if target in mods:
        return mods[target]
    parts = target.split(".")
    while len(parts) > 1:
        parts = parts[:-1]
        cand = ".".join(parts)
        if here and here.replace("/", ".") + "." + cand in mods:
            return mods[here.replace("/", ".") + "." + cand]
        if cand in mods and target.startswith(cand + "."):
            return mods[cand]
    return None


def _resolve_web(target: str, importer: str, idx: FileIndex, project: Project) -> str | None:
    if target.startswith(("http:", "https:", "data:", "//")):
        return None
    clean = target.split("?", 1)[0].split("#", 1)[0]
    if clean.startswith("/"):
        roots = [s.data.get("dir", "") for s in project.facts if s.kind == "static_files"]
        roots += [posixpath.dirname(importer)] if importer.endswith((".html", ".htm")) else []
        for root in roots + [""]:
            cand = posixpath.normpath(posixpath.join(root, clean.lstrip("/"))) if root else clean.lstrip("/")
            if cand in idx.paths:
                return cand
        return None
    here = posixpath.dirname(importer)
    cand = posixpath.normpath(posixpath.join(here, clean))
    for c in (cand, cand + ".js", cand + ".ts", cand + ".mjs", cand + "/index.js", cand + "/index.ts"):
        if c in idx.paths:
            return c
    return None
