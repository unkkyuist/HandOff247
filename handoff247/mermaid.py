"""Mermaid flowchart builders. Every diagram is derived from Project.links / Project.edges;
nothing is drawn that is not backed by an observed fact."""
from __future__ import annotations

import posixpath
import re
from collections import Counter, defaultdict
from contextlib import contextmanager

from .connect import area_of
from .labels import t
from .model import Project

CLASSDEFS = [
    "classDef entry fill:#fde68a,stroke:#b45309,color:#1f2937",
    "classDef launcher fill:#e0e7ff,stroke:#4338ca,color:#1f2937",
    "classDef mode fill:#dcfce7,stroke:#15803d,color:#1f2937",
    "classDef iface fill:#cffafe,stroke:#0e7490,color:#1f2937",
    "classDef table fill:#fce7f3,stroke:#be185d,color:#1f2937",
    "classDef hub fill:#f3f4f6,stroke:#6b7280,color:#1f2937,stroke-dasharray:4 3",
    "classDef data fill:#fef3c7,stroke:#92400e,color:#1f2937",
    "classDef ext fill:#ffffff,stroke:#9ca3af,color:#374151,stroke-dasharray:2 2",
    "classDef test fill:#ede9fe,stroke:#6d28d9,color:#1f2937",
    "classDef file fill:#ffffff,stroke:#64748b,color:#1f2937",
]


def esc(text: str) -> str:
    text = str(text).replace('"', "#quot;").replace("<", "#lt;").replace(">", "#gt;")
    text = text.replace("*", "#42;").replace("_", "#95;").replace("`", "#96;")   # no accidental markdown
    return text.replace("|", "#124;").replace("\n", "<br/>")


class Flow:
    SHAPES = {"rect": ('["', '"]'), "round": ('("', '")'), "stadium": ('(["', '"])'), "sub": ('[["', '"]]'),
              "hex": ('{{"', '"}}'), "para": ('[/"', '"/]'), "db": ('[("', '")]'), "circle": ('(("', '"))'),
              "flag": ('>"', '"]')}

    def __init__(self, direction: str = "LR"):
        self.lines = [f"flowchart {direction}"]
        self.ids: dict[str, str] = {}
        self.files: dict[str, str] = {}      # node id -> project file (for the HTML viewer)
        self.indent = "  "
        self.edges_seen: set[tuple] = set()
        self.n = 0

    def node(self, key: str, label: str, shape: str = "rect", cls: str = "", file: str = "") -> str:
        if key in self.ids:
            return self.ids[key]
        self.n += 1
        nid = f"n{self.n}"
        self.ids[key] = nid
        a, b = self.SHAPES[shape]
        self.lines.append(f"{self.indent}{nid}{a}{esc(label)}{b}" + (f":::{cls}" if cls else ""))
        if file:
            self.files[nid] = file
        return nid

    def edge(self, a: str, b: str, label: str = "", style: str = "-->") -> None:
        if not a or not b or a == b or (a, b, label) in self.edges_seen:
            return
        self.edges_seen.add((a, b, label))
        lab = f'|"{esc(label)}"|' if label else ""
        self.lines.append(f"{self.indent}{a} {style}{lab} {b}")

    @contextmanager
    def group(self, key: str, title: str):
        self.n += 1
        self.lines.append(f'{self.indent}subgraph g{self.n}["{esc(title)}"]')
        old = self.indent
        self.indent += "  "
        yield
        self.indent = old
        self.lines.append(f"{self.indent}end")

    def render(self) -> str:
        return "\n".join(self.lines + ["  " + c for c in CLASSDEFS]) + "\n"


def short(path: str) -> str:
    return path.rsplit("/", 1)[-1]


def display(path: str, project: Project) -> str:
    """File name, or the full path when another file has the same name."""
    base = short(path)
    same = sum(1 for f in project.files if short(f.path) == base)
    return path if same > 1 else base


def holes(text: str) -> str:
    """Interpolation holes such as {DateTime.UtcNow:yyyyMMdd} shown as *."""
    return re.sub(r"\{[^{}]*\}", "*", text)


def _label_ops(keys: list[str], limit: int = 4) -> str:
    keys = sorted(set(keys))
    if len(keys) <= limit:
        return ", ".join(keys)
    prefixes = Counter(k.split(".")[0] + (".*" if "." in k else "") for k in keys)
    top = [p for p, _ in prefixes.most_common(3)]
    return ", ".join(top) + (" …" if len(prefixes) > 3 else "") + f" ({len(keys)})"


def _apps(project: Project) -> list[dict]:
    """Runnable programs: build targets paired with their entry file, plus stand-alone entry files with modes."""
    L = project.links
    apps = []
    entry_files = {e["file"] for e in L["entries"]}
    for bt in L["build_targets"]:
        d = posixpath.dirname(bt["file"])
        entry = next((e for e in L["entries"] if posixpath.dirname(e["file"]) == d and e["file"].endswith(".cs")), None)
        apps.append({"key": bt["file"], "label": f'{bt["assembly"]} ({short(bt["file"])})', "file": bt["file"],
                     "entry": entry["file"] if entry else ""})
    covered = {a["entry"] for a in apps}
    for m in L["modes"]:
        if m["file"] not in covered:
            apps.append({"key": m["file"], "label": short(m["file"]), "file": m["file"], "entry": m["file"]})
            covered.add(m["file"])
    return apps


def system_map(project: Project) -> Flow | None:
    """Launchers → program → modes → interfaces → dispatch table, with the clients that call in."""
    L = project.links
    apps = _apps(project)
    if not apps and not L["tables"] and not L["routes"]:
        return None
    fl = Flow("LR")
    runs = [e for e in project.edges if e.kind == "runs"]
    app_keys = {a["key"] for a in apps}
    files = {f.path: f for f in project.files}
    # launchers that start an app directly or through other launchers (no tests)
    launchers = set(L.get("launchers", {}))
    if len(launchers) > 3:
        # the full chain is on the startup diagram; here one node keeps the overview readable
        names = list(L["launchers"])
        label = t("launchers") + f" ×{len(launchers)}\n" + ", ".join(display(p, project) for p in names[:3]) + " …"
        lid = fl.node("launchers", label, "rect", "launcher", names[0])
        for a in apps:
            if any(e.src in launchers and e.dst == a["key"] for e in runs):
                fl.edge(lid, fl.node(a["key"], a["label"], "sub", "entry", a["file"]), t("runs"))
    elif launchers:
        with fl.group("launch", t("launchers")):
            for p in sorted(launchers):
                fl.node(p, display(p, project), "rect", "launcher", p)
        for e in runs:
            if e.src in launchers and (e.dst in launchers or e.dst in app_keys):
                label = e.label if e.label and e.label != "build output" else ""
                if e.dst in app_keys:
                    fl.node(e.dst, next(a["label"] for a in apps if a["key"] == e.dst), "sub", "entry", e.dst)
                fl.edge(fl.ids[e.src], fl.ids[e.dst], label)
    mode_ids = {}
    for a in apps:
        aid = fl.node(a["key"], a["label"], "sub", "entry", a["file"])
        modes = [m for m in L["modes"] if m["file"] == a["entry"]]
        if modes:
            with fl.group("modes" + a["key"], t("modes_of", file=short(a["entry"]))):
                for m in modes:
                    label = m["name"] + (f' ({t("default")})' if m["default"] else "")
                    mid = fl.node("mode:" + m["file"] + ":" + m["name"], label, "stadium", "mode", m["file"])
                    mode_ids[m["name"]] = mid
            for m in modes:
                fl.edge(aid, mode_ids[m["name"]])
    # interfaces
    route_groups = defaultdict(list)
    for r in L["routes"]:
        for mname in r["modes"] or [""]:
            route_groups[mname].append(r)
    table_ids = {}
    for tb in L["tables"]:
        table_ids[tb["id"]] = fl.node("table:" + tb["id"], f'{tb["id"]} · {len(tb["ops"])} {t("ops")}', "hex", "table", tb["file"])
    http_id = None
    if L["routes"]:
        http_routes = [r for r in L["routes"] if r["verb"] != "MCP"]
        if http_routes:
            http_id = fl.node("http", t("http_routes", n=len(http_routes)), "para", "iface", http_routes[0]["file"])
        mcp_http = [r for r in L["routes"] if r["verb"] == "MCP"]
        for r in L["routes"]:
            for mname in r["modes"]:
                if mname in mode_ids:
                    if r["verb"] == "MCP":
                        fl.edge(mode_ids[mname], fl.node("mcp-http", f'MCP HTTP {r["path"]}', "para", "iface", r["file"]))
                    elif http_id:
                        fl.edge(mode_ids[mname], http_id)
        for r in L["routes"]:
            if r["forwards_to"] and r["forwards_to"] in table_ids and http_id:
                fl.edge(http_id, table_ids[r["forwards_to"]], f'{r["verb"]} {r["path"]}')
    tools = L["mcp_tools"]
    tool_id = None
    if tools:
        tool_files = sorted({x["file"] for x in tools})
        tool_id = fl.node("mcp-tools", t("mcp_tools_n", n=len(tools), files=", ".join(short(p) for p in tool_files)), "sub", "iface", tool_files[0])
        for tb in L["tables"]:
            if any(x["table"] == tb["id"] for x in tools):
                fl.edge(tool_id, table_ids[tb["id"]], t("calls"))
        if "mcp-http" in fl.ids:
            fl.edge(fl.ids["mcp-http"], tool_id)
    for m in L["modes"]:
        mid = mode_ids.get(m["name"])
        if not mid:
            continue
        for tid in m["tables"]:
            if tid in table_ids and not m["routes"]:
                fl.edge(mid, table_ids[tid], t("direct"))
        if "MCP over stdio" in m["transports"] and tool_id:
            fl.edge(mid, tool_id, "stdio")
        if m["name"] not in ("serve", "server") and not m["tables"] and not m["routes"] and "MCP over stdio" not in m["transports"]:
            for u in m["uses"][:3]:
                p = project.links["types"].get(u, [""])[0]
                if p:
                    fl.edge(mid, fl.node(p, f"{u} ({short(p)})", "rect", "file", p))
    # clients
    clients = defaultdict(lambda: {"files": set(), "keys": set(), "inferred": False})
    for c in L["consumers"]:
        f = files.get(c["file"])
        if not f:
            continue
        ch = c.get("channel", "")
        if c["file"] in {x["file"] for x in tools}:
            continue
        area = area_of(c["file"])
        key = (area if area != "(root)" else short(c["file"]), ch, c.get("route", "") or c.get("mode", ""))
        clients[key]["files"].add(c["file"])
        clients[key]["keys"].update(c["keys"])
        clients[key]["inferred"] |= bool(c.get("inferred"))
    for cl in L["mcp_clients"]:
        cid = fl.node("mcpc:" + cl["file"], f'{t("mcp_client")}: {short(cl["file"])}', "rect", "ext", cl["file"])
        if cl["mode"] in mode_ids:
            fl.edge(cid, mode_ids[cl["mode"]], cl["mode"])
    if clients:
        with fl.group("clients", t("callers")):
            for (area, ch, via), info in sorted(clients.items(), key=lambda kv: -len(kv[1]["keys"])):
                n = len(info["files"])
                label = f'{area} · {n} {t("files")}' if n > 1 else sorted(info["files"])[0]
                cls = "test" if all(files[p].category == "test" for p in info["files"]) else "file"
                fl.node(f"client:{area}:{ch}:{via}", label, "rect", cls, sorted(info["files"])[0])
        for (area, ch, via), info in clients.items():
            cid = fl.ids[f"client:{area}:{ch}:{via}"]
            style = "-.->" if info["inferred"] or not ch else "-->"
            ops = f'{len(info["keys"])} {t("ops")}'
            if ch == "http" and http_id:
                fl.edge(cid, http_id, ops, style)
            elif ch == "process" and via in mode_ids:
                fl.edge(cid, mode_ids[via], f"{via} · {ops}", style)
            else:
                for tid in table_ids.values():
                    fl.edge(cid, tid, ops + (f" · {ch}" if ch else ""), style)
                    break
    # handlers
    if L["tables"]:
        with fl.group("handlers", t("handlers")):
            for tb in L["tables"]:
                per = defaultdict(list)
                for op in tb["ops"]:
                    if op["handler_file"]:
                        per[op["handler_file"]].append(op["key"])
                for p, keys in sorted(per.items(), key=lambda kv: -len(kv[1])):
                    if p == tb["file"]:
                        continue
                    fl.node(p, short(p), "rect", "file", p)
        for tb in L["tables"]:
            per = defaultdict(list)
            for op in tb["ops"]:
                if op["handler_file"] and op["handler_file"] != tb["file"]:
                    per[op["handler_file"]].append(op["key"])
            for p, keys in per.items():
                fl.edge(table_ids[tb["id"]], fl.ids[p], _label_ops(keys, 3))
    # data stores
    for rp in L["runtime_paths"]:
        for part in rp["parts"]:
            if re.search(r"\.(db|sqlite3?|mdb)$", part, re.I):
                did = fl.node("data:" + holes(part), holes(part), "db", "data")
                if rp["file"] in fl.ids:
                    fl.edge(fl.ids[rp["file"]], did)
                else:
                    fl.edge(fl.node(rp["file"], short(rp["file"]), "rect", "file", rp["file"]), did)
    for s in L["static"]:
        if http_id:
            web = fl.node("static:" + s["dir"], t("static_files", dir=s["dir"]), "rect", "iface")
            fl.edge(http_id, web, t("serves"), "-.->")
    return fl


def startup(project: Project) -> Flow | None:
    """Every observed 'X starts Y' link: launch scripts, build outputs, MCP client configs, CI."""
    runs = [e for e in project.edges if e.kind == "runs"]
    L = project.links
    files = {f.path: f for f in project.files}
    if not runs and not L["launches"]:
        return None
    fl = Flow("LR")
    apps = {a["key"]: a for a in _apps(project)}
    nodes = set()
    for e in runs:
        if files.get(e.src) and files[e.src].category == "test":
            continue
        nodes.update([e.src, e.dst])
    tests_running = sorted({e.src for e in runs if files.get(e.src) and files[e.src].category == "test"})
    if not nodes and not tests_running:
        return None

    def nid(p: str) -> str:
        f = files.get(p)
        if p in apps:
            return fl.node(p, apps[p]["label"], "sub", "entry", p)
        if any(c["file"] == p for c in L["mcp_clients"]):
            return fl.node(p, f'{t("mcp_client")}: {short(p)}', "rect", "ext", p)
        cls = "launcher" if f and f.category == "script" else ("test" if f and f.category == "test" else "file")
        return fl.node(p, p if "/" in p and len(p) < 40 else short(p), "rect", cls, p)
    for e in runs:
        if e.src in nodes:
            label = "" if e.label == "build output" else e.label
            fl.edge(nid(e.src), nid(e.dst), label)
    for a in apps.values():
        if a["key"] in fl.ids and a["entry"]:
            modes = [m for m in L["modes"] if m["file"] == a["entry"]]
            for m in modes:
                fl.edge(fl.ids[a["key"]], fl.node("mode:" + m["name"], m["name"] + (f' ({t("default")})' if m["default"] else ""),
                                                  "stadium", "mode", m["file"]))
    for l in L["launches"]:
        if l["file"] in fl.ids:
            for u in l["urls"]:
                fl.edge(fl.ids[l["file"]], fl.node("url:" + u, u, "flag", "ext"), t("opens"), "-.->")
    if tests_running:
        label = t("tests_n", n=len(tests_running))
        tid = fl.node("tests", label, "rect", "test", tests_running[0])
        for a in apps:
            if a in fl.ids:
                modes = Counter(l["mode"] for l in L["launches"] if l["file"] in tests_running and l["mode"])
                fl.edge(tid, fl.ids[a], ", ".join(m for m, _ in modes.most_common(4)) or t("runs"), "-.->")
    return fl


def operations(project: Project) -> Flow | None:
    """Per dispatch table: who calls which group of operations, and which component handles them."""
    L = project.links
    if not L["tables"]:
        return None
    fl = Flow("LR")
    files = {f.path: f for f in project.files}
    for tb in L["tables"]:
        tid = fl.node("table:" + tb["id"], tb["id"] + "\n" + f'{tb["file"]}:{tb["line"]}', "hex", "table", tb["file"])
        callers = defaultdict(set)
        for op in tb["ops"]:
            for u in op["used_by"]:
                callers[u["file"]].add(op["key"])
            for name in op["mcp_tools"]:
                callers["@mcp"].add(op["key"])
        with fl.group("callers" + tb["id"], t("callers")):
            for p, keys in sorted(callers.items(), key=lambda kv: (-len(kv[1]), kv[0])):
                if p == "@mcp":
                    fl.node("mcp", t("mcp_tools_short", n=sum(len(o["mcp_tools"]) for o in tb["ops"])), "sub", "iface",
                            L["mcp_tools"][0]["file"] if L["mcp_tools"] else "")
                else:
                    f = files.get(p)
                    fl.node(p, p, "rect", "test" if f and f.category == "test" else "file", p)
        consumer_info = {(c["file"]): c for c in L["consumers"]}
        for p, keys in callers.items():
            src = fl.ids["mcp" if p == "@mcp" else p]
            c = consumer_info.get(p, {})
            ch = c.get("route") or (f'{c.get("mode")}' if c.get("channel") == "process" and c.get("mode") else c.get("channel", ""))
            label = _label_ops(list(keys), 2) + (f" · {ch}" if ch else "")
            fl.edge(src, tid, label, "-.->" if c.get("inferred") else "-->")
        per = defaultdict(list)
        for op in tb["ops"]:
            key = op["handler_file"] or ("inline" if not op["handler_type"] else op["handler_type"])
            per[key].append(op["key"])
        with fl.group("handlers" + tb["id"], t("handlers")):
            for key in sorted(per):
                if key == "inline":
                    fl.node("inline" + tb["id"], t("inline"), "round", "hub")
                elif key in files:
                    fl.node(key, short(key), "rect", "file", key)
                else:
                    fl.node("type:" + key, key, "rect", "ext")
        for key, keys in per.items():
            dst = fl.ids["inline" + tb["id"]] if key == "inline" else fl.ids.get(key) or fl.ids.get("type:" + key)
            fl.edge(tid, dst, _label_ops(keys, 3))
    return fl


def code_map(project: Project, max_area_nodes: int = 25) -> Flow | None:
    """File-level dependency map grouped by folder. Shared foundations (hubs) are drawn once
    without their incoming edges so the rest stays readable."""
    kinds = {"injects": 3, "extends": 3, "imports": 2, "uses": 1, "loads": 2}
    edges = [e for e in project.edges if e.kind in kinds]
    if not edges:
        return None
    files = {f.path: f for f in project.files}
    hubs = {h["file"]: h["used_by"] for h in project.links["hubs"]}
    involved = set()
    for e in edges:
        involved.update([e.src, e.dst])
    involved |= {e["file"] for e in project.links["entries"] if e["file"] in files and files[e["file"]].category == "code"}
    areas = defaultdict(list)
    for p in sorted(involved):
        f = files.get(p)
        if not f:
            continue
        a = area_of(p)
        if a == "(root)":
            a = f"(root) · {f.lang}"
        areas[a].append(p)
    collapsed = {a for a, ps in areas.items() if len(ps) > max_area_nodes}
    fl = Flow("LR")
    node_of = {}
    for a in sorted(areas):
        ps = areas[a]
        if a in collapsed:
            nid = fl.node("area:" + a, f'{a}/ · {len(ps)} {t("files")}', "rect", "hub")
            for p in ps:
                node_of[p] = nid
            continue
        with fl.group("area:" + a, a):
            for p in ps:
                f = files[p]
                syms = [s.name for s in f.symbols if s.kind in ("class", "record", "interface", "struct", "enum")]
                label = short(p)
                if f.lang == "csharp" and syms and syms[0] != short(p).rsplit(".", 1)[0]:
                    label += "\n" + syms[0]
                if p in hubs:
                    label += "\n(" + t("used_by_n", n=hubs[p]) + ")"
                cls = "hub" if p in hubs else ("entry" if "entry" in f.tags else ("test" if f.category == "test" else "file"))
                node_of[p] = fl.node(p, label, "rect", cls, p)
    best = {}
    for e in edges:
        if e.dst in hubs:
            continue
        a, b = node_of.get(e.src), node_of.get(e.dst)
        if not a or not b or a == b:
            continue
        k = (a, b)
        if k not in best or kinds[e.kind] > kinds[best[k].kind]:
            best[k] = e
    drawn = sorted(best.items(), key=lambda kv: -kinds[kv[1].kind])
    if len(drawn) > 160:
        drawn = [d for d in drawn if kinds[d[1].kind] >= 2][:160]
    for (a, b), e in drawn:
        style = "==>" if e.kind in ("injects", "extends") else ("-.->" if e.kind == "loads" else "-->")
        fl.edge(a, b, "", style)
    return fl


def areas_map(project: Project) -> Flow:
    """Folder-level overview with file counts and aggregated links between folders."""
    fl = Flow("LR")
    counts = defaultdict(Counter)
    for f in project.files:
        counts[area_of(f.path)][f.category] += 1
    for a in sorted(counts):
        c = counts[a]
        total = sum(c.values())
        detail = ", ".join(f"{k} {v}" for k, v in c.most_common(3))
        fl.node("area:" + a, f"{a} · {total}" + "\n" + detail, "rect", "file")
    agg = defaultdict(Counter)
    for e in project.edges:
        if e.kind in ("documents", "refers"):
            continue
        a, b = area_of(e.src), area_of(e.dst)
        if a != b:
            agg[(a, b)][e.kind] += 1
    for (a, b), c in sorted(agg.items()):
        label = ", ".join(f"{k} {v}" for k, v in c.most_common(2))
        fl.edge(fl.ids["area:" + a], fl.ids["area:" + b], label)
    return fl


def all_diagrams(project: Project) -> dict[str, Flow]:
    out = {}
    for name, fn in (("system", system_map), ("startup", startup), ("operations", operations),
                     ("code", code_map), ("areas", areas_map)):
        fl = fn(project)
        if fl is not None and len(fl.lines) > 1:
            out[name] = fl
    return out
