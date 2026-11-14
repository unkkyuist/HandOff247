"""The application as its users meet it.

``screens.py`` says what is on each screen and ``handlers.py`` what each route does. This
module joins the two into one model, stored in ``project.links["journeys"]``:

    user types   who the code distinguishes (role checks on routes and in templates)
    screens      templates and pages, the routes that show them, the layout they extend
    terms        the words on a screen and the feature each of them leads to
    features     one per route: who may use it, what it reads, writes, stores and shows
    data         tables, and the column values ("states") that features set or filter on
    assets       static files, uploads, generated files and external storage, in context
    handoffs     where one feature sets a state that another feature's query filters on
    functions    project code that features call (modelled once, referenced by many)
    gaps         what the analysis could not connect, stated instead of guessed

The user types are those of the analysed application. They never limit what the reader of
the handoff pack may see: every flow links to the flows of the other user types.
"""
from __future__ import annotations

import posixpath
import re

from . import screens as scr
from .handlers import PyIndex, access_other, parse_sql
from .model import Project

ANYONE = "anyone"
SIGNED_IN = "signed-in user"
MEDIA_EXT = scr.ASSET_EXT
MAX_GAPS = 60


# ---------------------------------------------------------------------------- route matching

def _route_segments(tpl: str) -> list[tuple[str, str]]:
    """Each segment of a route template as (kind, text): lit, one (one segment), rest (the remainder)."""
    out = []
    for seg in tpl.strip("/").split("/"):
        if re.fullmatch(r"<path:[^>]+>|\{\*[^}]*\}|\{[^}]*:path\}|\*\*?|\{\*\*[^}]*\}", seg):
            out.append(("rest", seg))
        elif re.fullmatch(r"<[^>]+>|\{[^}]*\}|:[A-Za-z_]\w*|\[[^\]]+\]", seg):
            out.append(("one", seg))
        else:
            out.append(("lit", seg))
    return out


def match_path(path: str, method: str, features: list[dict]) -> list[str]:
    """Features whose route template fits a path written in a template or script. A hole in
    the path (``*``) only fits a parameter of the route, never a fixed word of another route."""
    path = path.split("?", 1)[0].split("#", 1)[0]
    if re.match(r"https?://", path):
        path = "/" + path.split("/", 3)[3] if path.count("/") >= 3 else "/"
    if not path.startswith("/"):
        return []
    prefix_only = path.endswith("/") and len(path) > 1
    segs = path.strip("/").split("/")
    hits = []
    for f in features:
        if not f["path"].startswith("/"):
            continue
        verbs = [v.strip().upper() for v in f["verb"].split(",")]
        if method and "ANY" not in verbs and method.upper() not in verbs:
            continue
        rs = _route_segments(f["path"])
        ok, score = True, 0
        for i, (kind, text) in enumerate(rs):
            if kind == "rest":
                ok = i < len(segs) or prefix_only
                break
            if i >= len(segs):
                ok = prefix_only and kind == "one" and i == len(segs)      # '/api/' + name  ->  /api/{name}
                break
            if kind == "one":
                continue
            if "*" in segs[i] or segs[i] != text:
                ok = False
                break
            score += 1
        else:
            ok = len(segs) == len(rs)
        if ok:
            hits.append((score, f["id"]))
    if not hits:
        return []
    best = max(s for s, _ in hits)
    return [fid for s, fid in hits if s == best]


# ---------------------------------------------------------------------------- build

def build(project: Project) -> dict:
    files = {f.path: f for f in project.files}
    paths = set(files)
    locales = scr.Locales(project.files)
    py = PyIndex(project)
    gaps: list[dict] = []

    def gap(what: str, file: str = "", line: int = 0) -> None:
        if len(gaps) < MAX_GAPS:
            gaps.append({"what": what, "file": file, "line": line})

    # ------------------------------------------------------------ features (one per route)
    features: dict[str, dict] = {}
    by_endpoint: dict[str, list[str]] = {}
    for r in project.links.get("routes", []):
        fid = f"{r['verb']} {r['path']}"
        if fid in features:
            continue
        feat = {"id": fid, "verb": r["verb"], "path": r["path"], "file": r["file"], "line": r["line"],
                "handler": r.get("handler", ""), "roles": [], "permissions": [], "signed_in": False, "access_evidence": [],
                "unread_decorators": [], "analysed": False, "renders": [], "redirects": [], "fields": [], "sql": [],
                "files": [], "settings": [], "external": [], "background": [], "branches": [], "messages": [], "calls": [],
                "dynamic": []}
        f = files.get(r["file"])
        node = py.handler(r["file"], feat["handler"], r["line"]) if f and f.lang == "python" and feat["handler"] else None
        if node is not None:
            feat["analysed"] = True
            feat["end_line"] = getattr(node, "end_lineno", r["line"])
            acc = py.access(r["file"], node)
            effects = py.effects(r["file"], node)
        else:
            acc = access_other(f.text.split("\n"), f.lang, r["file"], r["line"]) if f and f.text else \
                {"roles": [], "permissions": [], "signed_in": False, "evidence": [], "unread": []}
            effects = []
        feat["roles"], feat["permissions"], feat["signed_in"] = acc["roles"], acc["permissions"], acc["signed_in"]
        feat["access_evidence"], feat["unread_decorators"] = acc["evidence"], acc["unread"]
        seen = set()
        for seq, e in enumerate(effects):
            key = (e["kind"], e["file"], e["line"], e.get("name", ""), e.get("text", ""), e.get("test", ""), e.get("func", ""))
            if key in seen:
                continue
            seen.add(key)
            where = {"file": e["file"], "line": e["line"], "via": e["via"], "seq": e["root"] * 10000 + seq}
            if e["when"]:
                where["when"] = e["when"]
            k = e["kind"]
            if k == "render":
                feat["renders"].append({**where, "template": e["template"]})
            elif k == "render_dynamic":
                feat["dynamic"].append({**where, "what": "template name is not a literal", "text": e["text"]})
            elif k == "redirect":
                feat["redirects"].append({**where, **{x: e[x] for x in ("endpoint", "path") if x in e}})
            elif k == "field":
                feat["fields"].append({**where, "source": e["source"], "name": e["name"]})
            elif k == "sql":
                feat["sql"].append({**where, **{x: e[x] for x in ("verb", "reads", "writes", "sets", "filters", "param_columns",
                                                                    "creates", "text")}})
            elif k == "sql_dynamic":
                feat["dynamic"].append({**where, "what": "SQL built at run time", "text": e["text"]})
            elif k == "file":
                feat["files"].append({**where, **{x: e[x] for x in ("op", "upload", "expr", "dir", "dir_name", "dir_env", "name")
                                                  if x in e}})
            elif k == "setting":
                item = {**where, **{x: e[x] for x in ("name", "variable", "defined_file", "defined_line") if e.get(x)}}
                if not any(s["name"] == item["name"] and s["file"] == item["file"] for s in feat["settings"]):
                    feat["settings"].append(item)
            elif k == "external":
                feat["external"].append({**where, "what": e["what"], "text": e["text"]})
            elif k == "background":
                feat["background"].append({**where, "text": e["text"]})
            elif k == "branch":
                feat["branches"].append({**where, "test": e["test"], "outcome": e["outcome"]})
            elif k == "message":
                feat["messages"].append({**where, "text": e["text"], "how": e["how"]})
            elif k == "call":
                feat["calls"].append({**where, "func": e["func"], "label": e["label"], "def_file": e["def_file"],
                                      "def_line": e["def_line"], "end_line": e["end_line"]})
        features[fid] = feat
        if feat["handler"]:
            by_endpoint.setdefault(feat["handler"], []).append(fid)
    feature_list = list(features.values())
    for feat in feature_list:
        for d in feat["dynamic"]:
            gap(f"{feat['id']}: {d['what']} ({d['text']})", d["file"], d["line"])
        for d in feat["unread_decorators"]:
            gap(f"{feat['id']} is also wrapped by {d['text']}, which was not read as an access check", d["file"], d["line"])
        if not feat["analysed"]:
            gap(f"{feat['id']}: the handler was not analysed (only Python handlers are followed)", feat["file"], feat["line"])
        for rd in feat["redirects"]:
            rd["to"] = by_endpoint.get(rd["endpoint"], []) if "endpoint" in rd else match_path(rd["path"], "GET", feature_list)

    # ------------------------------------------------------------ screens
    parsed = {f.path: scr.parse_template(f, locales) for f in project.files if scr.is_template(f)}
    tpaths = set(parsed)
    screens: dict[str, dict] = {}
    for path, t in parsed.items():
        ext = scr.resolve_template(t["extends"], path, tpaths) if t["extends"] else ""
        if t["extends"] and not ext:
            gap(f"{path} extends {t['extends']!r}, which was not found among the templates", path, 1)
        screens[path] = {"id": path, "file": path, "title": t["title"], "extends": ext, "includes": [], "extended_by": [],
                         "included_by": [], "routes": [], "roles": [], "open": False, "signed_in": False, "terms": [],
                         "assets": [], "calls": [], "kind": "page"}
        for inc in t["includes"]:
            target = scr.resolve_template(inc["name"], path, tpaths)
            if target:
                screens[path]["includes"].append({"screen": target, "line": inc["line"]})
    for s in screens.values():
        if s["extends"]:
            screens[s["extends"]]["extended_by"].append(s["id"])
        for inc in s["includes"]:
            screens[inc["screen"]]["included_by"].append(s["id"])
    for feat in feature_list:
        for rn in feat["renders"]:
            target = scr.resolve_template(rn["template"], rn["file"], tpaths)
            rn["screen"] = target
            if target:
                if feat["id"] not in screens[target]["routes"]:
                    screens[target]["routes"].append(feat["id"])
            else:
                gap(f"{feat['id']} renders {rn['template']!r}, which was not found among the templates", rn["file"], rn["line"])
    for s in screens.values():
        if not s["routes"]:
            if s["extended_by"]:
                s["kind"] = "layout"
            elif s["included_by"]:
                s["kind"] = "partial"
            else:
                s["kind"] = "page without a known route"
        for fid in s["routes"]:
            feat = features[fid]
            for role in feat["roles"]:
                if role not in s["roles"]:
                    s["roles"].append(role)
            if not feat["roles"]:
                if feat["signed_in"] or feat["permissions"]:
                    s["signed_in"] = True
                else:
                    s["open"] = True

    def chain(screen_id: str) -> list[str]:
        """The screen and every layout it extends, nearest first."""
        out, cur = [], screen_id
        while cur and cur not in out:
            out.append(cur)
            cur = screens[cur]["extends"]
        return out

    # scripts a page loads, and the HTTP calls those scripts make
    def resolve_file(raw: str, from_file: str) -> str:
        raw = scr.HOLE.sub("", raw).split("?", 1)[0].split("#", 1)[0]
        if not raw or re.match(r"(?:https?:)?//", raw):
            return ""
        here = posixpath.dirname(from_file)
        rel = raw.lstrip("/")
        for cand in (posixpath.normpath(posixpath.join(here, raw)) if not raw.startswith("/") else "", rel):
            if cand and cand in paths:
                return cand
        hits = [p for p in paths if p.endswith("/" + rel)]
        return hits[0] if len(hits) == 1 else ""

    def resolve_static(name: str, from_file: str) -> str:
        name = name.lstrip("/")
        hits = [p for p in paths if p == "static/" + name or p.endswith("/static/" + name)]
        if len(hits) == 1:
            return hits[0]
        return resolve_file(name, from_file) if not hits else ""

    def url_file(url: dict, from_file: str) -> str:
        if url["kind"] == "static":
            return resolve_static(url.get("file", ""), from_file) if url.get("file") else ""
        if url["kind"] == "path":
            return resolve_file(url["path"], from_file)
        return ""

    def url_features(url: dict, method: str) -> list[str]:
        if url["kind"] == "endpoint":
            fids = by_endpoint.get(url["endpoint"], [])
            ok = [fid for fid in fids if not method or method in features[fid]["verb"].split(",") or features[fid]["verb"] == "ANY"]
            return ok or fids
        if url["kind"] == "path":
            return match_path(url["path"], method, feature_list)
        return []

    http_calls: dict[str, list] = {}
    for fc in project.facts:
        if fc.kind == "http_call":
            http_calls.setdefault(fc.file, []).append(fc)
    script_edges: dict[str, list[str]] = {}
    for e in project.edges:
        if e.kind in ("loads", "imports") and files.get(e.dst) and files[e.dst].lang in ("javascript", "typescript"):
            script_edges.setdefault(e.src, []).append(e.dst)
    for sid, s in screens.items():
        reach, todo = [sid], [sid]
        for ref in parsed[sid]["refs"]:
            if ref["tag"] == "script":
                target = url_file(ref["url"], sid)
                if target and target not in reach:
                    reach.append(target)
                    todo.append(target)
        while todo:
            cur = todo.pop()
            for nxt in script_edges.get(cur, []):
                if nxt not in reach:
                    reach.append(nxt)
                    todo.append(nxt)
        for src in reach:
            for fc in http_calls.get(src, []):
                raw = scr.HOLE.sub("*", fc.data["path"])
                for fid in match_path(raw, "", feature_list):
                    if not any(c["feature"] == fid and c["file"] == fc.file and c["line"] == fc.line for c in s["calls"]):
                        s["calls"].append({"feature": fid, "file": fc.file, "line": fc.line, "func": fc.data.get("func", "")})

    # ------------------------------------------------------------ terms
    terms: list[dict] = []
    for sid, t in parsed.items():
        own_routes = screens[sid]["routes"]
        for n, raw in enumerate(t["terms"]):
            term = {"id": f"{sid}:{raw['line']}:{n}", "text": raw["text"], "kind": raw["kind"], "screen": sid, "file": sid,
                    "line": raw["line"], "conditions": list(raw["conditions"]), "condition_lines": raw.get("condition_lines", []),
                    "roles": [], "leads_to": [], "method": ""}
            for c in raw["conditions"]:
                for role in scr.roles_in(c):
                    if role not in term["roles"]:
                        term["roles"].append(role)
            if raw.get("i18n"):
                i = raw["i18n"]
                term["i18n"] = {k: i[k] for k in ("key", "lang", "file", "line")}
                term["other_texts"] = [{"lang": o["lang"], "text": o["text"], "file": o["file"], "line": o["line"]} for o in i["other"]]
            if raw.get("unresolved_key"):
                term["unresolved_key"] = True
                gap(f"translation key {raw['text']!r} was not found in a locale file", sid, raw["line"])
            for k in ("field", "field_type", "dynamic", "partly_dynamic", "placeholder"):
                if raw.get(k):
                    term[k] = raw[k]
            url, method, form = raw.get("url"), raw.get("method") or "GET", None
            if "form" in raw:
                form = t["forms"][raw["form"]]
                url, method = form["action"], form["method"]
                term["form_line"] = form["line"]
                if form["conditions"]:
                    for c in form["conditions"]:
                        if c not in term["conditions"]:
                            term["conditions"].append(c)
            if url is not None and raw["kind"] in ("link", "button", "field"):
                term["method"] = method
                if url["kind"] in ("endpoint", "path"):
                    term["leads_to"] = url_features(url, method)
                    if not term["leads_to"] and not url_file(url, sid):
                        term["unmatched"] = url["raw"]
                        if raw["kind"] != "field":
                            gap(f"{raw['text'] or 'a link'!r} points to {url['raw']!r}; no route was found for it", sid, raw["line"])
                elif url["kind"] == "external":
                    term["external"] = url["host"]
                elif url["kind"] == "none" and form is not None and not form["action_raw"]:
                    # HTML: a form without an action posts back to the URL of the page it is on
                    back = [fid for fid in own_routes if method in features[fid]["verb"].split(",") or features[fid]["verb"] == "ANY"]
                    if len(back) == 1:
                        term["leads_to"], term["posts_back"] = back, True
                target = url_file(url, sid)
                if target and files[target].category == "asset":
                    term["asset_file"] = target
            if term["text"] or term.get("dynamic"):
                terms.append(term)
                screens[sid]["terms"].append(term["id"])
    for feat in feature_list:                               # messages the code shows are words the user reads too
        for n, msg in enumerate(feat["messages"]):
            terms.append({"id": f"{msg['file']}:{msg['line']}:m{n}", "text": msg["text"], "kind": "message", "screen": "",
                          "file": msg["file"], "line": msg["line"], "conditions": [], "roles": [], "leads_to": [],
                          "method": "", "feature": feat["id"], "how": msg["how"]})
    for term in terms:                                      # a field label is implemented where the handler reads the field
        if term["kind"] == "field" and term.get("field"):
            for fid in term["leads_to"]:
                hit = next((fl for fl in features[fid]["fields"] if fl["name"] == term["field"]), None)
                if hit:
                    term.setdefault("read_at", []).append({"feature": fid, "file": hit["file"], "line": hit["line"],
                                                           "source": hit["source"]})

    # ------------------------------------------------------------ user types
    user_types: dict[str, dict] = {}

    def user(name: str, kind: str, file: str, line: int, text: str) -> None:
        u = user_types.setdefault(name, {"id": name, "name": name, "kind": kind, "evidence": [], "features": [], "screens": []})
        if len(u["evidence"]) < 12 and not any(e["file"] == file and e["line"] == line for e in u["evidence"]):
            u["evidence"].append({"file": file, "line": line, "text": text})

    for feat in feature_list:
        for role in feat["roles"]:
            for ev in feat["access_evidence"] or [{"file": feat["file"], "line": feat["line"], "text": ""}]:
                user(role, "role", ev["file"], ev["line"], ev["text"])
        for br in feat["branches"]:
            for role in scr.roles_in(br["test"]):
                user(role, "role", br["file"], br["line"], "if " + br["test"])
                br.setdefault("roles", []).append(role)
    for term in terms:
        for role in term["roles"]:
            i = next((n for n, c in enumerate(term["conditions"]) if role in scr.roles_in(c)), 0)
            at = term["condition_lines"][i] if i < len(term.get("condition_lines", [])) else term["line"]
            user(role, "role", term["file"], at, "{% if " + term["conditions"][i] + " %}")
    any_open = [f for f in feature_list if not f["roles"] and not f["signed_in"] and not f["permissions"]]
    any_signed = [f for f in feature_list if not f["roles"] and (f["signed_in"] or f["permissions"])]
    if any_signed:
        ev = any_signed[0]["access_evidence"][0] if any_signed[0]["access_evidence"] else {"file": any_signed[0]["file"], "line": any_signed[0]["line"], "text": ""}
        user(SIGNED_IN, "signed-in", ev["file"], ev["line"], ev["text"])
    if any_open and (user_types or screens):
        user_types[ANYONE] = {"id": ANYONE, "name": ANYONE, "kind": "anyone", "evidence": [], "features": [], "screens": []}
    for feat in feature_list:
        owners = feat["roles"] or ([SIGNED_IN] if feat["signed_in"] or feat["permissions"] else [ANYONE])
        for o in owners:
            if o in user_types:
                user_types[o]["features"].append(feat["id"])
                for rn in feat["renders"]:
                    if rn.get("screen") and rn["screen"] not in user_types[o]["screens"]:
                        user_types[o]["screens"].append(rn["screen"])
    for sid, s in screens.items():                          # pages no route renders (single-page apps, static sites)
        if s["kind"] == "page without a known route" and (s["terms"] or s["calls"]):
            user_types.setdefault(ANYONE, {"id": ANYONE, "name": ANYONE, "kind": "anyone", "evidence": [], "features": [], "screens": []})
            user_types[ANYONE]["screens"].append(sid)

    # ------------------------------------------------------------ data and states
    data: dict[str, dict] = {}

    def table(name: str) -> dict:
        return data.setdefault(name, {"id": name, "defined": [], "columns": [], "readers": [], "writers": [], "states": []})

    def state(tb: str, column: str, value: str) -> dict:
        t = table(tb)
        for st in t["states"]:
            if st["column"] == column and st["value"] == value:
                return st
        st = {"table": tb, "column": column, "value": value, "set_by": [], "read_by": [], "tested_in": []}
        t["states"].append(st)
        return st

    def once(rows: list[dict], row: dict) -> None:
        if not any(r["feature"] == row["feature"] and r["file"] == row["file"] and r["line"] == row["line"] for r in rows):
            rows.append(row)

    for f in project.files:
        if f.path.lower().endswith(".sql") and f.text:
            offset = 0
            for stmt in f.text.split(";"):
                line = f.text.count("\n", 0, offset + len(stmt) - len(stmt.lstrip())) + 1
                offset += len(stmt) + 1
                p = parse_sql(stmt)
                for c in (p or {}).get("creates", []):
                    t = table(c["table"])
                    t["defined"].append({"file": f.path, "line": line})
                    t["columns"] = t["columns"] or c["columns"]
    for feat in feature_list:
        for q in feat["sql"]:
            where = {"feature": feat["id"], "file": q["file"], "line": q["line"], "via": q["via"]}
            for c in q["creates"]:
                t = table(c["table"])
                t["defined"].append({"file": q["file"], "line": q["line"]})
                t["columns"] = t["columns"] or c["columns"]
            for tb in q["reads"]:
                once(table(tb)["readers"], where)
            for tb in q["writes"]:
                once(table(tb)["writers"], {**where, "verb": q["verb"]})
            for s in q["sets"]:
                once(state(s["table"], s["column"], s["value"])["set_by"], where)
            for s in q["filters"]:
                once(state(s["table"], s["column"], s["value"])["read_by"], where)

    handoffs: list[dict] = []
    for t in data.values():
        for st in t["states"]:
            for a in st["set_by"]:
                for b in st["read_by"]:
                    if a["feature"] == b["feature"]:
                        continue
                    if any(h["from"] == a["feature"] and h["to"] == b["feature"] and h["state"] == [st["table"], st["column"], st["value"]]
                           for h in handoffs):
                        continue
                    handoffs.append({"from": a["feature"], "to": b["feature"], "state": [st["table"], st["column"], st["value"]],
                                     "set_at": {k: a[k] for k in ("file", "line", "via")},
                                     "read_at": {k: b[k] for k in ("file", "line", "via")}, "kind": "query",
                                     "inferred": "one statement sets this value and the other filters on it; "
                                                 "that the same rows are meant was not verified"})
    # a value that is set by one feature and tested in a template condition or a handler branch elsewhere
    for t in data.values():
        for st in t["states"]:
            # status == 'x', row["status"] != 'x', status in ('a', 'x')
            needle = re.compile(r"\b" + re.escape(st["column"]) + r"\b['\"\])]*\s*(?:[=!]==?|(?:not\s+)?in\b)\s*[\[(]?[^)\]]*?['\"]"
                                + re.escape(st["value"]) + r"['\"]")
            tested = []
            for term in terms:
                for c in term["conditions"]:
                    if needle.search(c):
                        tested.append({"where": "template", "screen": term["screen"], "term": term["id"], "text": term["text"],
                                       "condition": c, "file": term["file"], "line": term["line"]})
            for feat in feature_list:
                for br in feat["branches"]:
                    if needle.search(br["test"]):
                        tested.append({"where": "handler", "feature": feat["id"], "condition": br["test"], "outcome": br["outcome"],
                                       "file": br["file"], "line": br["line"]})
            st["tested_in"] = tested

    # ------------------------------------------------------------ shared code
    functions: dict[str, dict] = {}
    for feat in feature_list:
        for c in feat["calls"]:
            fn = functions.setdefault(f"{c['def_file']}:{c['func']}", {"id": f"{c['def_file']}:{c['func']}", "name": c["func"],
                                                                      "file": c["def_file"], "line": c["def_line"],
                                                                      "end_line": c["end_line"], "features": []})
            if feat["id"] not in fn["features"]:
                fn["features"].append(feat["id"])

    # ------------------------------------------------------------ assets
    assets: dict[str, dict] = {}

    def asset(aid: str, kind: str, name: str, **extra) -> dict:
        a = assets.setdefault(aid, {"id": aid, "kind": kind, "name": name, "used_in": [], "screens": [], "registered_by": [],
                                    "stored_by": [], "written_by": [], "served_by": [], "deleted_by": [], "columns": [],
                                    "unknown": []})
        a.update({k: v for k, v in extra.items() if v})
        return a

    def use(a: dict, file: str, line: int, how: str, screen: str = "", conditions: list | None = None) -> None:
        if not any(u["file"] == file and u["line"] == line for u in a["used_in"]):
            a["used_in"].append({"file": file, "line": line, "how": how, **({"conditions": conditions} if conditions else {})})
        if screen and screen not in a["screens"]:
            a["screens"].append(screen)
            if a["id"] not in screens[screen]["assets"]:
                screens[screen]["assets"].append(a["id"])

    for f in project.files:                                 # files that ship with the project
        if f.lang == "binary" and f.path.lower().endswith(MEDIA_EXT) and "vendored" not in f.tags:
            asset(f.path, "static", f.path, file=f.path)
    css_users: dict[str, list[tuple[str, int]]] = {}        # stylesheet -> screens that load it
    for sid, t in parsed.items():
        for ref in t["refs"]:
            target = url_file(ref["url"], sid)
            if target and target in assets:
                use(assets[target], sid, ref["line"], f"<{ref['tag']}>", sid, ref["conditions"])
            elif target and files[target].lang == "css":
                css_users.setdefault(target, []).append((sid, ref["line"]))
    for term in terms:
        if term["screen"] and term.get("asset_file") in assets:
            use(assets[term["asset_file"]], term["screen"], term["line"], f"link \"{term['text']}\"", term["screen"], term["conditions"])
    for f in project.files:
        if f.lang == "css" and f.text:
            for ref in scr.css_refs(f):
                target = resolve_file(ref["raw"], f.path)
                if target in assets:
                    use(assets[target], f.path, ref["line"], "url() in a stylesheet")
                    for sid, _ in css_users.get(f.path, []):
                        use(assets[target], f.path, ref["line"], "url() in a stylesheet", sid)
    for e in project.edges:                                 # a string in code that is the file's path
        if e.kind == "refers" and e.dst in assets and not any(u["file"] == e.src for u in assets[e.dst]["used_in"]):
            use(assets[e.dst], e.src, e.line, "path written in the file")

    def serving(dir_id: str, name: str = "") -> list[dict]:
        out = []
        for feat in feature_list:
            for fl in feat["files"]:
                if fl["op"] == "serve" and dir_id and fl.get("dir") == dir_id and (not fl.get("name") or not name or fl["name"] == name):
                    out.append({"feature": feat["id"], "file": fl["file"], "line": fl["line"], "via": fl["via"],
                                "exact_file": bool(fl.get("name"))})
        return out

    # every place where a template points at a route, computed once
    pointers: list[tuple[set, dict]] = []
    for sid, t in parsed.items():
        for ref in t["refs"]:
            targets = set(url_features(ref["url"], "GET"))
            if targets:
                pointers.append((targets, {"screen": sid, "file": sid, "line": ref["line"], "how": f"<{ref['tag']}>",
                                           "conditions": ref["conditions"]}))
    for term in terms:
        if term["screen"] and term["kind"] == "link" and term["leads_to"]:
            pointers.append((set(term["leads_to"]), {"screen": term["screen"], "file": term["screen"], "line": term["line"],
                                                     "how": f"link \"{term['text']}\"", "conditions": term["conditions"]}))

    def shown(fids: list[str]) -> list[dict]:
        """Where a template points at the routes that deliver a file."""
        want = set(fids)
        return [where for targets, where in pointers if targets & want] if want else []

    for feat in feature_list:
        uploads = [fl for fl in feat["fields"] if fl["source"] == "file"]
        stores = [fl for fl in feat["files"] if fl["op"] == "store"]
        for up in uploads:
            exact = [s for s in stores if s.get("upload") == up["name"]]
            guess = stores if not exact and len(uploads) == 1 and len(stores) == 1 else []
            dir_id = next((s.get("dir", "") for s in exact + guess), "")
            a = asset(f"upload:{up['name']}", "uploaded", f"uploaded file `{up['name']}`", field=up["name"])
            a["registered_by"].append({"feature": feat["id"], "file": up["file"], "line": up["line"], "via": up["via"]})
            for s in exact + guess:
                row = {"feature": feat["id"], "file": s["file"], "line": s["line"], "via": s["via"], "expr": s["expr"]}
                for k in ("dir", "dir_name", "dir_env"):
                    if s.get(k):
                        row[k] = s[k]
                if s in guess:
                    row["inferred"] = "the handler reads one uploaded file and stores one file; that they are the same was not traced"
                a["stored_by"].append(row)
            if not exact and not guess:
                a["unknown"].append("where the uploaded file is stored was not found")
            for q in feat["sql"]:
                for pc in q["param_columns"]:
                    if pc.get("upload") == up["name"]:
                        a["columns"].append({"table": pc["table"], "column": pc["column"], "feature": feat["id"], "file": q["file"],
                                             "line": q["line"], "via": q["via"]})
            if not a["columns"]:
                a["unknown"].append("which data column keeps the stored name was not traced")
            for sv in serving(dir_id):
                if not any(x["feature"] == sv["feature"] for x in a["served_by"]):
                    a["served_by"].append(sv)
        for fl in feat["files"]:
            if fl["op"] == "write":
                name = fl.get("name") or fl["expr"]
                a = asset(f"generated:{name}", "generated", f"generated file `{name}`")
                a["written_by"].append({"feature": feat["id"], "file": fl["file"], "line": fl["line"], "via": fl["via"], "expr": fl["expr"],
                                        **({"dir_name": fl["dir_name"]} if fl.get("dir_name") else {}),
                                        **({"dir_env": fl["dir_env"]} if fl.get("dir_env") else {})})
                for sv in serving(fl.get("dir", ""), fl.get("name", "")):
                    if not any(x["feature"] == sv["feature"] for x in a["served_by"]):
                        a["served_by"].append(sv)
            elif fl["op"] == "delete":
                for a in assets.values():
                    if any(s.get("dir") and s.get("dir") == fl.get("dir") for s in a["stored_by"]):
                        a["deleted_by"].append({"feature": feat["id"], "file": fl["file"], "line": fl["line"], "via": fl["via"]})
        for ex in feat["external"]:
            if ex["what"] == "external storage":
                a = asset(f"external:{ex['file']}:{ex['line']}", "external", f"external storage call at {ex['file']}:{ex['line']}",
                          text=ex["text"])
                a["registered_by"].append({"feature": feat["id"], "file": ex["file"], "line": ex["line"], "via": ex["via"]})
                a["unknown"].append("what happens to the object in the external store cannot be read from this code")
    for a in assets.values():
        if a["kind"] in ("uploaded", "generated"):
            for sh in shown([s["feature"] for s in a["served_by"]]):
                use(a, sh["file"], sh["line"], sh["how"], sh["screen"], sh["conditions"])
            if a["kind"] == "uploaded":                     # the form control the user picks the file with
                for term in terms:
                    if term["kind"] == "field" and term.get("field") == a.get("field") and \
                            set(term["leads_to"]) & {r["feature"] for r in a["registered_by"]}:
                        a.setdefault("picked_with", []).append({"term": term["id"], "text": term["text"], "file": term["file"],
                                                                "line": term["line"]})
            if not a["served_by"]:
                a["unknown"].append("no route was found that delivers it")
        elif a["kind"] == "static" and not a["used_in"]:
            a["unknown"].append("no reference was found; a path built at run time would not be seen")
    for a in assets.values():                               # screens that show it through a layout they extend
        for sid in list(a["screens"]):
            todo = list(screens[sid]["extended_by"]) + list(screens[sid]["included_by"])
            while todo:
                child = todo.pop()
                if child not in a["screens"]:
                    a["screens"].append(child)
                    a.setdefault("through_layout", []).append({"screen": child, "layout": sid})
                    todo += screens[child]["extended_by"] + screens[child]["included_by"]

    for s in screens.values():
        if s["kind"] == "page without a known route" and (s["terms"] or s["calls"]) and not s["id"].lower().endswith((".html", ".htm")):
            gap(f"no route was found that renders {s['id']}", s["id"], 1)
    return {
        "user_types": sorted(user_types.values(), key=lambda u: ({"role": 0, "signed-in": 1, "anyone": 2}[u["kind"]], u["name"])),
        "screens": sorted(screens.values(), key=lambda s: s["id"]),
        "terms": terms,
        "features": feature_list,
        "data": sorted(data.values(), key=lambda t: t["id"]),
        "assets": sorted(assets.values(), key=lambda a: ({"uploaded": 0, "generated": 1, "external": 2, "static": 3}[a["kind"]], a["id"])),
        "handoffs": handoffs,
        "functions": sorted(functions.values(), key=lambda f: f["id"]),
        "gaps": gaps,
        "chains": {sid: chain(sid) for sid in screens},
    }


def attach(project: Project) -> None:
    try:
        project.links["journeys"] = build(project)
    except RecursionError:
        project.links["journeys"] = empty("the analysis ran too deep")


def empty(reason: str = "") -> dict:
    return {"user_types": [], "screens": [], "terms": [], "features": [], "data": [], "assets": [], "handoffs": [],
            "functions": [], "gaps": [{"what": reason, "file": "", "line": 0}] if reason else [], "chains": {}}
