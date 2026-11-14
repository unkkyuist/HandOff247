"""The project as an ontology: typed entities and typed relations between them.

It is a second view of what the analyzers and ``connect.link`` already found, nothing new is
detected here. Every relation keeps the file and line it was observed at, and a relation that
rests on an inference says so. ``ontology.json`` is this structure; the graph tab of the
viewer and the wiki are drawn from it, so all three always agree.
"""
from __future__ import annotations

from . import __version__
from .connect import area_of
from .model import Project

TYPE_KINDS = {"class", "record", "record struct", "record class", "struct", "interface", "enum"}

# (id, label, plural, colour group, shape, description). Groups share a colour in the graph;
# the shape tells the classes of one group apart.
CLASSES = [
    ("Project", "Project", "Project", "structure", "diamond", "The thing being handed over."),
    ("Area", "Area", "Areas", "structure", "square", "A top-level folder of the project."),
    ("File", "File", "Files", "file", "circle", "A file of the project (images and other assets are left out)."),
    ("Type", "Type", "Types", "type", "circle", "A class, record, struct, interface or enum defined in a file."),
    ("Mode", "Run mode", "Run modes", "run", "diamond", "A way to start the program, picked by its first argument."),
    ("Subcommand", "Sub-command", "Sub-commands", "run", "square", "A sub-command of a command-line parser."),
    ("Table", "Dispatch table", "Dispatch tables", "operation", "square",
     "A switch or mapping that turns an operation name into the code that handles it."),
    ("Operation", "Operation", "Operations", "operation", "circle", "One named operation of a dispatch table."),
    ("Route", "HTTP route", "HTTP routes", "interface", "triangle", "An HTTP endpoint the program serves."),
    ("McpTool", "MCP tool", "MCP tools", "interface", "diamond", "A tool the program offers to AI clients over MCP."),
    ("EnvVar", "Environment variable", "Environment variables", "config", "circle",
     "An environment variable the code reads or sets (operating-system variables are left out)."),
    ("Port", "Port", "Ports", "config", "square", "A network port number found in an address or a port setting."),
    ("Package", "Package", "Packages", "outside", "circle", "A third-party package the project declares or imports."),
    ("Host", "External host", "External hosts", "outside", "triangle", "A host name found in a URL."),
    ("Command", "Command-line tool", "Command-line tools", "outside", "square",
     "A well-known program the project's scripts start; it has to be installed."),
    ("Person", "Person", "People", "outside", "diamond", "An author in the Git history."),
    # the application as its users meet it (journeys.py)
    ("UserType", "User type", "User types", "structure", "triangle",
     "A kind of user the analysed application tells apart, found from role checks. Not an access level of this pack."),
    ("Screen", "Screen", "Screens", "interface", "square", "A template or page a user sees."),
    ("Term", "Screen term", "Screen terms", "interface", "circle",
     "Words a user reads: a link, button, field label, heading, or a message the code shows."),
    ("Function", "Function", "Functions", "type", "square",
     "Project code that a feature runs. Modelled once, however many features use it."),
    ("Data", "Data table", "Data tables", "file", "square", "A table named in an SQL statement."),
    ("State", "State", "States", "file", "diamond",
     "A column value that statements set or filter on, such as status = 'published'."),
    ("Asset", "Asset", "Assets", "file", "triangle",
     "A file users see or provide: shipped with the project, uploaded, generated, or kept in external storage."),
]

# (id, label, label read from the other end, description)
RELATIONS = [
    ("contains", "contains", "is part of", "Project → area → file."),
    ("defines", "defines", "is defined in", "The file holds the definition."),
    ("imports", "imports", "is imported by", "Import or include statement."),
    ("uses", "uses", "is used by", "The code names a type defined in the other file; a run mode uses a type."),
    ("injects", "takes as a dependency", "is a dependency of", "Constructor parameter of that type."),
    ("extends", "extends", "is extended by", "Base class or implemented interface."),
    ("loads", "loads", "is loaded by", "A page loads a script or stylesheet."),
    ("runs", "runs", "is run by", "A script or configuration starts the other file."),
    ("refers", "refers to", "is referred to by", "A string in the file is the other file's path."),
    ("references", "references", "is referenced by", "Project reference in a build file."),
    ("documents", "documents", "is documented in", "A document links to the file or shows the operation in an example."),
    ("serves", "serves", "is served by", "A run mode passes requests to the dispatch table."),
    ("exposes", "exposes", "is exposed by", "A run mode registers the HTTP route."),
    ("hasOperation", "has operation", "is an operation of", "Key of the dispatch table."),
    ("handledBy", "is handled by", "handles", "The file that holds the handler the table calls."),
    ("calls", "calls", "is called from", "The file asks for the operation by name (over HTTP, a process or in-process)."),
    ("invokes", "invokes", "is invoked by", "An MCP tool runs the operation."),
    ("forwardsTo", "forwards to", "receives from", "An HTTP route hands the request to the dispatch table."),
    ("reads", "reads", "is read by", "The file reads the environment variable."),
    ("sets", "sets", "is set by", "The file sets the environment variable."),
    ("mentions", "mentions", "is mentioned in", "The host or port appears in the file."),
    ("dependsOn", "depends on", "is a dependency of", "The file declares or imports the package."),
    ("starts", "starts", "is started by", "The file starts the command-line tool."),
    ("authored", "has commits in", "has commits by", "Author in the Git history of the project."),
    # the application as its users meet it; a route is a feature
    ("openTo", "is open to", "may use", "Role check on the route, or none found (anyone)."),
    ("sees", "sees", "is seen by", "A route this user type may use shows the screen."),
    ("shows", "shows", "is shown by", "The route renders the screen."),
    ("builtOn", "is built on", "is part of", "The template extends or includes the other one."),
    ("displays", "displays", "is displayed on", "The words are on the screen, or the route shows the message."),
    ("leadsTo", "leads to", "is started from", "The link, button or form of the term targets the route; a script of the screen calls it."),
    ("redirectsTo", "redirects to", "is reached by redirect from", "The handler redirects to the other route."),
    ("runsCode", "runs", "runs for", "The handler calls the function, directly or through other functions."),
    ("readsData", "reads", "is read by", "An SQL statement of the feature reads the table."),
    ("writesData", "writes", "is written by", "An SQL statement of the feature inserts, updates or deletes rows."),
    ("hasState", "has the state", "is a state of", "A literal column value found in a statement."),
    ("setsState", "sets", "is set by", "A statement of the feature sets the column to this value."),
    ("listsState", "lists only", "is the filter of", "A statement of the feature filters on this value."),
    ("testedBy", "is tested by", "tests", "A template condition or a handler branch names the same column and value."),
    ("handsOverTo", "hands over to", "receives from", "One feature sets a state that the other filters on."),
    ("showsAsset", "shows", "appears on", "The screen references the file."),
    ("provides", "provides", "is provided by", "The feature receives the upload or writes the generated file."),
    ("delivers", "delivers", "is delivered by", "The route sends the file to the browser."),
    ("keptIn", "has its name kept in", "keeps the name of", "The stored file name is written to a column of the table."),
    ("wordedIn", "takes its text from", "words", "The text of the term comes from a locale file."),
]
SKIP_EDGES = {"calls-op", "dispatches"}        # the same facts are told through operations


def first_line(text: str, limit: int = 220) -> str:
    for line in (text or "").split("\n"):
        s = line.strip().lstrip("-*#> ").strip()
        if s:
            return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"
    return ""


class _Builder:
    def __init__(self) -> None:
        self.entities: dict[str, dict] = {}
        self.relations: dict[tuple[str, str, str], dict] = {}
        self.extra: list[str] = []

    def ent(self, eid: str, cls: str, name: str, summary: str = "", file: str = "", line: int = 0, **attrs) -> str:
        e = self.entities.get(eid)
        if e is None:
            e = {"id": eid, "type": cls, "name": name}
            self.entities[eid] = e
        if summary and not e.get("summary"):
            e["summary"] = summary
        if file and not e.get("file"):
            e["file"] = file
            if line:
                e["line"] = line
        for k, v in attrs.items():
            if v not in ("", None, [], False):
                e.setdefault("attrs", {}).setdefault(k, v)
        return eid

    def rel(self, s: str, p: str, o: str, file: str = "", line: int = 0, label: str = "", inferred: str = "") -> None:
        if s == o or s not in self.entities or o not in self.entities:
            return
        r = self.relations.get((s, p, o))
        if r:
            r["count"] = r.get("count", 1) + 1
            return
        r = {"s": s, "p": p, "o": o}
        if file:
            r["file"] = file
            if line:
                r["line"] = line
        if label:
            r["label"] = label
        if inferred:
            r["inferred"] = inferred
        self.relations[(s, p, o)] = r


def _journeys(b: _Builder, project: Project, notes, fid) -> None:
    """User types, screens, terms, data, states, assets and shared functions, with the
    relations between them and to the routes and files that already exist."""
    from .explore import Explorer
    ex = Explorer(project, notes)
    j = ex.j
    if not j["user_types"] and not j["screens"]:
        return

    def rid(feature: str) -> str:
        return "route:" + feature

    def state_id(table: str, column: str, value: str) -> str:
        return f"state:{table}.{column}={value}"

    for u in j["user_types"]:
        told = "no role check was found on the routes it uses" if u["kind"] == "anyone" else \
            (f"told apart in {len(u['evidence'])} place(s)" if u["evidence"] else "")
        ev = u["evidence"][0] if u["evidence"] else {}
        b.ent("user:" + u["name"], "UserType", u["name"], first_line(notes.get(f"User: {u['name']}")) or told,
              ev.get("file", ""), ev.get("line", 0), kind=u["kind"])
    for s in j["screens"]:
        b.ent("screen:" + s["id"], "Screen", s["id"], s["title"], s["file"], 1, kind=s["kind"])
        b.rel(fid(s["file"]), "defines", "screen:" + s["id"], s["file"], 1)
    for s in j["screens"]:
        if s["extends"]:
            b.rel("screen:" + s["id"], "builtOn", "screen:" + s["extends"], s["file"], 1, "extends")
        for inc in s["includes"]:
            b.rel("screen:" + s["id"], "builtOn", "screen:" + inc["screen"], s["file"], inc["line"], "includes")
        for c in s["calls"]:
            b.rel("screen:" + s["id"], "leadsTo", rid(c["feature"]), c["file"], c["line"], "script call")
    for f in j["features"]:
        for owner in ex.who(f["id"]):
            ev = f["access_evidence"][0] if f["access_evidence"] else {"file": f["file"], "line": f["line"], "text": ""}
            b.rel(rid(f["id"]), "openTo", "user:" + owner, ev["file"], ev["line"], ev.get("text", "") or "no role check found")
        for rn in f["renders"]:
            if rn.get("screen"):
                b.rel(rid(f["id"]), "shows", "screen:" + rn["screen"], rn["file"], rn["line"])
                for owner in ex.who(f["id"]):
                    b.rel("user:" + owner, "sees", "screen:" + rn["screen"], rn["file"], rn["line"], f["id"])
        for rd in f["redirects"]:
            for target in rd.get("to", []):
                b.rel(rid(f["id"]), "redirectsTo", rid(target), rd["file"], rd["line"], " and ".join(rd.get("when", [])))
    for u in j["user_types"]:                               # pages no route renders
        for sid in u["screens"]:
            b.rel("user:" + u["name"], "sees", "screen:" + sid, sid, 1, "no route found; served as a file")
    for fn in j["functions"]:
        b.ent("func:" + fn["id"], "Function", fn["name"], f"run by {len(fn['features'])} feature(s)", fn["file"], fn["line"])
        b.rel(fid(fn["file"]), "defines", "func:" + fn["id"], fn["file"], fn["line"])
    for f in j["features"]:
        for c in f["calls"]:
            b.rel(rid(f["id"]), "runsCode", f"func:{c['def_file']}:{c['func']}", c["file"], c["line"], c["via"])
    for t in j["terms"]:
        if not t["text"]:
            continue
        tid = "term:" + t["id"]
        summary = t["kind"] + (f" on {t['screen']}" if t["screen"] else f", shown by {t.get('feature', '')}")
        b.ent(tid, "Term", t["text"], summary, t["file"], t["line"], kind=t["kind"],
              shown_when=" and ".join(t["conditions"]), field=t.get("field", ""),
              other_languages=[o["text"] for o in t.get("other_texts", [])])
        if t["screen"]:
            b.rel("screen:" + t["screen"], "displays", tid, t["file"], t["line"])
        elif t.get("feature"):
            b.rel(rid(t["feature"]), "displays", tid, t["file"], t["line"], t.get("how", ""))
        for target in t["leads_to"]:
            b.rel(tid, "leadsTo", rid(target), t["file"], t["line"], t["method"])
        if t.get("i18n"):
            b.rel(tid, "wordedIn", fid(t["i18n"]["file"]), t["i18n"]["file"], t["i18n"]["line"], t["i18n"]["key"])
    for d in j["data"]:
        where = d["defined"][0] if d["defined"] else {}
        b.ent("data:" + d["id"], "Data", d["id"], ", ".join(d["columns"][:12]), where.get("file", ""), where.get("line", 0))
        if where:
            b.rel(fid(where["file"]), "defines", "data:" + d["id"], where["file"], where["line"])
        for r in d["readers"]:
            b.rel(rid(r["feature"]), "readsData", "data:" + d["id"], r["file"], r["line"], r["via"])
        for r in d["writers"]:
            b.rel(rid(r["feature"]), "writesData", "data:" + d["id"], r["file"], r["line"], r["via"])
        for st in d["states"]:
            first = (st["set_by"] or st["read_by"])[0]
            sid = b.ent(state_id(d["id"], st["column"], st["value"]), "State", f"{d['id']}.{st['column']} = '{st['value']}'",
                        f"set by {len(st['set_by'])}, listed by {len(st['read_by'])} feature(s)", first["file"], first["line"])
            b.rel("data:" + d["id"], "hasState", sid, first["file"], first["line"])
            for r in st["set_by"]:
                b.rel(rid(r["feature"]), "setsState", sid, r["file"], r["line"], r["via"])
            for r in st["read_by"]:
                b.rel(rid(r["feature"]), "listsState", sid, r["file"], r["line"], r["via"])
            for x in st["tested_in"]:
                target = "screen:" + x["screen"] if x["where"] == "template" else rid(x["feature"])
                b.rel(sid, "testedBy", target, x["file"], x["line"], x["condition"],
                      "the condition names the same column and value; not traced to the same rows")
    for h in j["handoffs"]:
        b.rel(rid(h["from"]), "handsOverTo", rid(h["to"]), h["read_at"]["file"], h["read_at"]["line"],
              f"{h['state'][0]}.{h['state'][1]} = '{h['state'][2]}'", h["inferred"])
    for a in j["assets"]:
        first = next((x for key in ("registered_by", "written_by", "used_in") for x in a[key]), {})
        gone = sorted({u for sid in a["screens"] for u in ex.who_sees(sid)})
        b.ent("asset:" + a["id"], "Asset", a["id"], a["kind"] + (f"; appears on {len(a['screens'])} screen(s)" if a["screens"]
                                                                  else "; no use found"),
              a.get("file", "") or first.get("file", ""), first.get("line", 0) if not a.get("file") else 0,
              kind=a["kind"], seen_by=gone, not_verified=a["unknown"])
        for sid in a["screens"]:
            use = next((u for u in a["used_in"] if u["file"] == sid), None) or (a["used_in"][0] if a["used_in"] else None)
            if use:
                through = next((x["layout"] for x in a.get("through_layout", []) if x["screen"] == sid), "")
                b.rel("screen:" + sid, "showsAsset", "asset:" + a["id"], use["file"], use["line"],
                      f"through the layout {through}" if through else use["how"])
        for key in ("registered_by", "written_by", "stored_by"):
            for r in a[key]:
                b.rel(rid(r["feature"]), "provides", "asset:" + a["id"], r["file"], r["line"],
                      {"registered_by": "receives it", "written_by": "writes it", "stored_by": "stores it"}[key],
                      r.get("inferred", ""))
        for r in a["served_by"]:
            b.rel(rid(r["feature"]), "delivers", "asset:" + a["id"], r["file"], r["line"],
                  "" if r.get("exact_file") else "serves any file of the folder")
        for col in a["columns"]:
            b.rel("asset:" + a["id"], "keptIn", "data:" + col["table"], col["file"], col["line"], f"column {col['column']}")


def build(project: Project, notes) -> dict:
    L = project.links
    lv = L.get("leaving", {})
    b = _Builder()
    known = {r[0] for r in RELATIONS}

    def fid(path: str) -> str:
        return "file:" + path

    readme = next((f for f in project.files if f.path.lower() in ("readme.md", "readme.en.md", "readme.txt", "readme")), None)
    pid = b.ent("project:" + project.name, "Project", project.name,
                first_line(notes.get("Project")) or (readme.summary if readme else ""))

    # ---------------------------------------------------------------- structure
    files = [f for f in project.files if f.category != "asset"]
    per_area: dict[str, int] = {}
    for f in files:
        per_area[area_of(f.path)] = per_area.get(area_of(f.path), 0) + 1
    for area in sorted(a for a in per_area if a != "(root)"):
        b.ent("area:" + area, "Area", area, first_line(notes.get(f"Area: {area}")), files=per_area[area])
        b.rel(pid, "contains", "area:" + area)
    model_text = L.get("model_summaries", {})
    for f in files:
        note = notes.get(f"File: {f.path}")
        b.ent(fid(f.path), "File", f.path, first_line(note) or first_line(f.summary), f.path,
              language=f.lang, category=f.category, lines=f.lines, not_parsed=f.skipped)
        m = model_text.get(f.path)
        if m and not note:                            # a person's note always wins
            b.entities[fid(f.path)]["model_summary"] = {k: m[k] for k in ("summary", "engine", "model", "date") if m.get(k)}
        area = area_of(f.path)
        b.rel(pid if area == "(root)" else "area:" + area, "contains", fid(f.path))
    for f in files:
        for s in f.symbols:
            if s.kind in TYPE_KINDS and s.public:
                tid = f"type:{s.name}" if f.lang == "csharp" else f"type:{f.path}#{s.name}"
                b.ent(tid, "Type", s.name, first_line(s.doc), f.path, s.line, kind=s.kind)
                b.rel(fid(f.path), "defines", tid, f.path, s.line)
    for e in project.edges:
        if e.kind in SKIP_EDGES or e.kind.startswith("mode:"):
            continue
        if e.kind not in known:
            known.add(e.kind)
            b.extra.append(e.kind)
        b.rel(fid(e.src), e.kind, fid(e.dst), e.src, e.line, e.label)

    # ---------------------------------------------------------------- how it runs
    for m in L.get("modes", []):
        mid = b.ent("mode:" + m["name"], "Mode", m["name"],
                    first_line(notes.get(f"Mode: {m['name']}")) or ", ".join(m.get("transports", [])), m["file"], m["line"],
                    default=m.get("default"), transports=m.get("transports"), reads_stdin=m.get("reads_stdin"))
        b.rel(fid(m["file"]), "defines", mid, m["file"], m["line"])
    for sc in L.get("subcommands", []):
        if sc.get("name"):
            sid = b.ent("subcmd:" + str(sc["name"]), "Subcommand", str(sc["name"]), first_line(sc.get("help", "")),
                        sc["file"], sc["line"])
            b.rel(fid(sc["file"]), "defines", sid, sc["file"], sc["line"])

    # ---------------------------------------------------------------- operations
    key_count: dict[str, int] = {}
    for tb in L.get("tables", []):
        for op in tb["ops"]:
            key_count[op["key"]] = key_count.get(op["key"], 0) + 1

    def op_id(table: str, key: str) -> str:
        return f"op:{key}" if key_count.get(key, 0) <= 1 else f"op:{table}:{key}"

    inferred_by = {(c["file"], f"{c['func']}()"): c["inferred"] for c in L.get("consumers", []) if c.get("inferred")}
    for tb in L.get("tables", []):
        tid = b.ent("table:" + tb["id"], "Table", tb["id"], f"{len(tb['ops'])} operation(s), picked by `{tb['selector']}`"
                    if tb.get("selector") else f"{len(tb['ops'])} operation(s)", tb["file"], tb["line"])
        b.rel(fid(tb["file"]), "defines", tid, tb["file"], tb["line"])
        for op in tb["ops"]:
            handler = ".".join(x for x in (op["handler_type"], op["handler_method"]) if x)
            oid = b.ent(op_id(tb["id"], op["key"]), "Operation", op["key"],
                        first_line(notes.get(f"Op: {op['key']}")) or (f"handled by `{handler}`" if handler else ""),
                        tb["file"], op["line"], handler=handler, expression=op.get("expr", "")[:200],
                        routes=op.get("routes"))
            b.rel(tid, "hasOperation", oid, tb["file"], op["line"])
            if op["handler_file"]:
                b.rel(oid, "handledBy", fid(op["handler_file"]), tb["file"], op["line"], handler)
            for u in op["used_by"]:
                how = {"http": "over HTTP", "process": "by starting a process", "in-process": "in-process"}.get(u.get("channel", ""), "")
                b.rel(fid(u["file"]), "calls", oid, u["file"], u["line"], ", ".join(x for x in (u.get("via", ""), how) if x),
                      inferred_by.get((u["file"], u.get("via", "")), ""))
            for u in op["documented_in"]:
                b.rel(fid(u["file"]), "documents", oid, u["file"], u["line"], u.get("via", ""))
    for m in L.get("modes", []):
        for t in m.get("tables", []):
            b.rel("mode:" + m["name"], "serves", "table:" + t, m["file"], m["line"])
        for u in m.get("uses", []):
            b.rel("mode:" + m["name"], "uses", "type:" + u, m["file"], m["line"])

    # ---------------------------------------------------------------- interfaces
    for r in L.get("routes", []):
        name = f"{r['verb']} {r['path']}"
        rid = b.ent("route:" + name, "Route", name, f"handler `{r['handler']}`" if r.get("handler") else "", r["file"], r["line"])
        b.rel(fid(r["file"]), "defines", rid, r["file"], r["line"])
        if r.get("forwards_to"):
            b.rel(rid, "forwardsTo", "table:" + r["forwards_to"], r["file"], r["line"])
        for mode in r.get("modes", []):
            b.rel("mode:" + mode, "exposes", rid, r["file"], r["line"])
    for tool in L.get("mcp_tools", []):
        tid = b.ent("tool:" + tool["name"], "McpTool", tool["name"], first_line(tool.get("description", "")),
                    tool["file"], tool["line"], method=".".join(x for x in (tool.get("cls", ""), tool.get("method", "")) if x),
                    name_from=tool.get("name_source", "") if "snake_case" in tool.get("name_source", "") else "")
        b.rel(fid(tool["file"]), "defines", tid, tool["file"], tool["line"])
        if tool.get("op"):
            b.rel(tid, "invokes", op_id(tool["table"], tool["op"]), tool["file"], tool["line"])

    # ---------------------------------------------------------------- configuration
    secret_names = set(lv.get("secret_env", []))
    for name, use in L.get("env", {}).items():
        if use.get("system"):
            continue
        default = next((r["default"] for r in use["reads"] if r.get("default")), "")
        eid = b.ent("env:" + name, "EnvVar", name, "the name suggests a secret; the value is not in the pack"
                    if name in secret_names else "", default_value="" if name in secret_names else default)
        for r in use["reads"]:
            b.rel(fid(r["file"]), "reads", eid, r["file"], r["line"])
        for w in use["writes"]:
            b.rel(fid(w["file"]), "sets", eid, w["file"], w["line"])
    for p in L.get("ports", []):
        eid = b.ent(f"port:{p['port']}", "Port", str(p["port"]), p.get("source", ""))
        b.rel(fid(p["file"]), "mentions", eid, p["file"], p["line"], p.get("source", ""))

    # ---------------------------------------------------------------- the outside
    for pk in L.get("packages", []):
        if not pk.get("name"):
            continue
        declared = pk.get("ecosystem") != "import"
        eid = b.ent("pkg:" + str(pk["name"]).lower(), "Package", str(pk["name"]),
                    " ".join(x for x in (pk.get("ecosystem", ""), pk.get("version", "")) if x) if declared else "",
                    development_only=pk.get("dev"))
        if declared:
            b.rel(fid(pk["file"]), "dependsOn", eid, pk["file"], pk.get("line", 0), "declared")
        for user in pk.get("used_in", []):
            b.rel(fid(user), "dependsOn", eid, user, 0, "imported")
    for h in lv.get("hosts", []):
        eid = b.ent("host:" + h["host"], "Host", h["host"], f"in {h['count']} URL(s)")
        for w in h["code"] + h["docs"]:
            b.rel(fid(w["file"]), "mentions", eid, w["file"], w["line"])
    for c in lv.get("commands", []):
        eid = b.ent("cmd:" + c["command"], "Command", c["command"], f"started in {c['count']} place(s)")
        for w in c["where"]:
            b.rel(fid(w["file"]), "starts", eid, w["file"], w["line"])
    for a in lv.get("git", {}).get("authors", []):
        eid = b.ent("person:" + a["name"], "Person", a["name"], f"{a['commits']} commit(s), {a['first']} to {a['last']}")
        b.rel(eid, "authored", pid)

    _journeys(b, project, notes, fid)

    order = {c[0]: i for i, c in enumerate(CLASSES)}
    entities = sorted(b.entities.values(), key=lambda e: (order[e["type"]], e["name"].lower(), e["id"]))
    counts: dict[str, int] = {}
    for e in entities:
        counts[e["type"]] = counts.get(e["type"], 0) + 1
    relations = [{"id": r[0], "label": r[1], "inverse": r[2], "description": r[3]} for r in RELATIONS]
    relations += [{"id": k, "label": k, "inverse": f"{k} (from)", "description": ""} for k in b.extra]
    return {
        "generator": "HandOff247", "kind": "ontology", "version": __version__, "project": project.name,
        "schema": {"classes": [{"id": c[0], "label": c[1], "plural": c[2], "group": c[3], "shape": c[4], "description": c[5]}
                               for c in CLASSES],
                   "relations": relations},
        "counts": counts,
        "entities": entities,
        "relations": sorted(b.relations.values(), key=lambda r: (r["s"], r["p"], r["o"])),
    }
