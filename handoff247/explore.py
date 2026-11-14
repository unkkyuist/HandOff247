"""Questions a successor asks, answered from the model in ``journeys.py``.

Five ways in, all over the same data, so the answers always agree with the pages:

    users() / user_flow()   start from a user type      -> screens -> features -> code
    find()                  start from words on screen, or from what a user reported
    asset()                 start from an asset or data -> where it comes from, where it shows
    impact()                start from code             -> features, screens and user types
    feature()               everything about one feature in one place

Every answer keeps the file and line behind each statement and ends with what the analysis
could not verify. Static analysis shows what the code does under which condition; it never
says which condition applied to a particular user at a particular moment.
"""
from __future__ import annotations

import re

from .journeys import ANYONE, SIGNED_IN, empty

CAVEAT = ("This is what the code does and under which conditions, read without running it. It does not tell which "
          "condition applied to this user: check the live data, settings and logs at the points listed under `check`.")
STOP = {"the", "a", "an", "is", "are", "was", "be", "to", "of", "in", "on", "it", "my", "me", "i", "we", "you", "and",
        "or", "but", "not", "no", "can", "cannot", "cant", "t", "s", "do", "does", "did", "that", "this", "there",
        "with", "for", "at", "by", "from", "have", "has", "when", "what", "where", "why", "how", "please", "so"}
WORD = re.compile(r"[^\W_]+", re.UNICODE)
METHOD_TEST = re.compile(r"(not \()?[\w.]*method\s*==\s*['\"](\w+)['\"]")


def applies(effect: dict, method: str) -> bool:
    """False when an effect sits under ``if request.method == …`` for another HTTP method than
    the one a control uses: a link (GET) to a page does not run what its form (POST) runs."""
    if not method:
        return True
    for w in effect.get("when", []):
        m = METHOD_TEST.search(w)
        if m:
            same = m.group(2).upper() == method.upper()
            if (same and m.group(1)) or (not same and not m.group(1)):
                return False
    return True


def tokens(text: str) -> list[str]:
    out = []
    for w in WORD.findall(text.lower()):
        if w not in STOP and (len(w) > 1 or not w.isascii()) and w not in out:
            out.append(w)
    return out


def _score(query: list[str], phrase: str, text: str) -> float:
    """How well some text on a screen fits the words of a question. Whole-word hits count
    fully; a hit inside a longer word counts when the script has no spaces (e.g. Korean)."""
    if not text:
        return 0.0
    low = text.lower()
    words = set(WORD.findall(low))
    score = 0.0
    for q in query:
        if q in words:
            score += 1.0
        elif len(q) >= 3 and any(w.startswith(q) or q.startswith(w) and len(w) >= 4 for w in words):
            score += 0.6
        elif not q.isascii() and (q in low or any(len(w) >= 2 and w in q for w in words)):
            score += 0.8                                # a word with a particle attached still names the term
    if score and len(low) >= 3 and low in phrase:
        score += 1.0 + 0.2 * len(words)                 # the exact term appears in the question
    return score


class Explorer:
    def __init__(self, project, notes=None):
        self.p = project
        self.notes = notes
        self.j = project.links.get("journeys") or empty()
        j = self.j
        self.features = {f["id"]: f for f in j["features"]}
        self.screens = {s["id"]: s for s in j["screens"]}
        self.terms = {t["id"]: t for t in j["terms"]}
        self.users_by_name = {u["name"]: u for u in j["user_types"]}
        self.assets = {a["id"]: a for a in j["assets"]}
        self.data = {d["id"]: d for d in j["data"]}
        self.functions = {f["id"]: f for f in j["functions"]}
        self.chains = j.get("chains", {})

    # ------------------------------------------------------------ small helpers
    def who(self, fid: str) -> list[str]:
        f = self.features[fid]
        return list(f["roles"]) or [SIGNED_IN if f["signed_in"] or f["permissions"] else ANYONE]

    def who_sees(self, sid: str) -> list[str]:
        s = self.screens[sid]
        out = list(s["roles"])
        if s["signed_in"]:
            out.append(SIGNED_IN)
        if s["open"] or s["kind"] == "page without a known route":
            out.append(ANYONE)
        if not out:                                     # a layout or partial: whoever sees the screens built on it
            for child in s["extended_by"] + s["included_by"]:
                for u in self.who_sees(child):
                    if u not in out:
                        out.append(u)
        return out

    def screen_terms(self, sid: str, own_only: bool = False) -> list[dict]:
        """Terms of a screen, then those of the layouts it extends and the partials it includes."""
        out = []
        for i, part in enumerate(self.chains.get(sid, [sid])):
            if own_only and i:
                break
            members = [part] + [inc["screen"] for inc in self.screens[part]["includes"]]
            for m in members:
                for tid in self.screens[m]["terms"]:
                    t = dict(self.terms[tid])
                    if m != sid:
                        t["from_layout"] = m
                    out.append(t)
        return out

    def triggers(self, fid: str) -> list[dict]:
        """Where on which screen a user starts this feature."""
        out = []
        for t in self.j["terms"]:
            if fid in t["leads_to"] and t["kind"] in ("link", "button"):
                out.append({"screen": t["screen"], "term": t["text"], "kind": t["kind"],
                            "file": t["file"], "line": t["line"], "shown_when": t["conditions"],
                            "seen_by": t["roles"] or self.who_sees(t["screen"]), "method": t["method"]})
        for s in self.j["screens"]:
            for c in s["calls"]:
                if c["feature"] == fid:
                    out.append({"screen": s["id"], "term": "", "kind": "script call", "file": c["file"], "line": c["line"],
                                "shown_when": [], "seen_by": self.who_sees(s["id"]), "method": ""})
        return out

    def label(self, fid: str) -> str:
        """A feature named the way a user would: by the control that starts it or the page it shows."""
        f = self.features[fid]
        tr = [t for t in self.triggers(fid) if t["term"] and t["kind"] != "script call"]
        named = sorted({t["term"] for t in tr})
        if named:
            return " / ".join(f'"{n}"' for n in named[:3])
        titles = [self.screens[r["screen"]]["title"] for r in f["renders"] if r.get("screen") and self.screens[r["screen"]]["title"]]
        return f'page "{titles[0]}"' if titles else (f["handler"] or f["id"])

    def handoffs_from(self, fid: str, method: str = "") -> list[dict]:
        """Who picks the work up after this feature. ``method`` narrows it to what one control starts."""
        out = []
        live = {(s["table"], s["column"], s["value"]) for q in self.features[fid]["sql"] if applies(q, method) for s in q["sets"]}
        for h in self.j["handoffs"]:
            if h["from"] == fid and tuple(h["state"]) in live:
                to = self.features[h["to"]]
                out.append({"to_feature": h["to"], "to_user_types": self.who(h["to"]),
                            "to_screens": [r["screen"] for r in to["renders"] if r.get("screen")],
                            "because": f"{h['state'][0]}.{h['state'][1]} = '{h['state'][2]}'",
                            "set_at": h["set_at"], "read_at": h["read_at"], "inferred": h["inferred"]})
        f = self.features[fid]
        for q in f["sql"]:                              # the value is tested in a template or a branch elsewhere
            if not applies(q, method):
                continue
            for s in q["sets"]:
                st = self._state(s["table"], s["column"], s["value"])
                for t in (st or {}).get("tested_in", []):
                    target = t.get("feature") or ""
                    if target == fid:
                        continue
                    row = {"because": f"{s['table']}.{s['column']} = '{s['value']}'", "tested": t["condition"],
                           "set_at": {"file": q["file"], "line": q["line"], "via": q["via"]},
                           "read_at": {"file": t["file"], "line": t["line"], "via": ""},
                           "inferred": "the condition names the same column and value; that it reads the same rows was not traced"}
                    if t["where"] == "template":
                        row.update({"to_feature": "", "to_screens": [t["screen"]], "to_user_types": self.who_sees(t["screen"]),
                                    "controls": t["text"]})
                    else:
                        row.update({"to_feature": target, "to_screens": [], "to_user_types": self.who(target),
                                    "outcome": t.get("outcome", "")})
                    if not any(o.get("read_at") == row["read_at"] for o in out):
                        out.append(row)
        return out

    def handoffs_to(self, fid: str) -> list[dict]:
        return [{"from_feature": h["from"], "from_user_types": self.who(h["from"]), "what": self.label(h["from"]),
                 "because": f"{h['state'][0]}.{h['state'][1]} = '{h['state'][2]}'", "set_at": h["set_at"], "read_at": h["read_at"],
                 "inferred": h["inferred"]} for h in self.j["handoffs"] if h["to"] == fid]

    def _state(self, table: str, column: str, value: str) -> dict | None:
        for st in self.data.get(table, {}).get("states", []):
            if st["column"] == column and st["value"] == value:
                return st
        return None

    # ------------------------------------------------------------ A. from a user type
    def users(self) -> dict:
        rows = []
        for u in self.j["user_types"]:
            rows.append({"user_type": u["name"], "kind": u["kind"],
                         "told_by": u["evidence"][:4] if u["kind"] != "anyone" else "no role check was found on these routes",
                         "screens": [{"screen": s, "title": self.screens[s]["title"]} for s in u["screens"]],
                         "can_do": [{"feature": fid, "called": self.label(fid)} for fid in u["features"]],
                         "note": self.notes.get(f"User: {u['name']}") if self.notes else ""})
        return {"user_types": rows, "screens_total": len(self.j["screens"]), "features_total": len(self.j["features"]),
                "reminder": "These are the user types of the analysed application, not access levels of this tool: "
                            "every flow of every user type is open to you.",
                "not_verified": self._gaps(8)}

    def user_flow(self, name: str) -> dict:
        u = self.users_by_name.get(name) or next((x for x in self.j["user_types"] if x["name"].lower() == name.lower()), None)
        if not u:
            raise KeyError(f"no user type {name!r}; known: {', '.join(self.users_by_name) or 'none found'}")
        screens = []
        for sid in u["screens"]:
            s = self.screens[sid]
            items = []
            for t in self.screen_terms(sid):
                if t["kind"] not in ("link", "button"):
                    continue
                if t["roles"] and u["kind"] == "role" and u["name"] not in t["roles"]:
                    continue                            # shown to another user type only
                row = {"on_screen": t["text"], "kind": t["kind"], "file": t["file"], "line": t["line"],
                       "shown_when": t["conditions"], "leads_to": t["leads_to"], "method": t["method"]}
                if t.get("from_layout"):
                    row["from_layout"] = t["from_layout"]
                if t.get("unmatched"):
                    row["not_verified"] = f"points to {t['unmatched']!r}; no route was found"
                if t.get("external"):
                    row["external"] = t["external"]
                for fid in t["leads_to"]:
                    f = self.features[fid]
                    if u["name"] not in self.who(fid) and ANYONE not in self.who(fid):
                        row.setdefault("needs_other_user_type", self.who(fid))
                    hand = self.handoffs_from(fid, t["method"])
                    if hand:
                        row.setdefault("then", []).extend(
                            {"user_types": h["to_user_types"], "screens": h["to_screens"], "feature": h["to_feature"],
                             "because": h["because"], "inferred": True} for h in hand)
                    row.setdefault("implemented_in", []).append({"feature": fid, "file": f["file"], "line": f["line"],
                                                                 "handler": f["handler"]})
                items.append(row)
            screens.append({"screen": sid, "title": s["title"], "opened_by": [r for r in s["routes"] if u["name"] in self.who(r)],
                            "also_seen_by": [x for x in self.who_sees(sid) if x != u["name"]],
                            "layout": self.chains.get(sid, [sid])[1:], "can_do_here": items,
                            "fields": [{"label": t["text"], "field": t.get("field", ""), "line": t["line"]}
                                       for t in self.screen_terms(sid, own_only=True) if t["kind"] == "field"],
                            "assets": s["assets"]})
        other = [fid for fid in u["features"] if not any(fid in s["opened_by"] for s in screens)]
        return {"user_type": u["name"], "kind": u["kind"], "told_by": u["evidence"], "screens": screens,
                "features_without_a_screen_of_their_own": [{"feature": fid, "called": self.label(fid)} for fid in other],
                "receives_from_others": [h for fid in u["features"] for h in self.handoffs_to(fid) if u["name"] not in h["from_user_types"]],
                "other_user_types": [x["name"] for x in self.j["user_types"] if x["name"] != u["name"]],
                "note": self.notes.get(f"User: {u['name']}") if self.notes else "", "how_to_read": CAVEAT}

    # ------------------------------------------------------------ one feature, everything in one place
    def feature(self, fid: str) -> dict:
        f = self.features.get(fid) or next((x for x in self.j["features"] if x["id"].lower() == fid.lower()
                                            or x["handler"] == fid or x["path"] == fid), None)
        if not f:
            close = [x["id"] for x in self.j["features"] if fid.lower() in x["id"].lower()][:8]
            raise KeyError(f"no feature {fid!r}" + (f"; did you mean {', '.join(close)}?" if close else ""))
        fid = f["id"]
        steps = []
        for t in self.triggers(fid):
            cond = f", shown when `{'` and `'.join(t['shown_when'])}`" if t["shown_when"] else ""
            what = f'{t["kind"]} "{t["term"]}"' if t["term"] else (t["kind"] if t["kind"] == "script call" else f'{t["kind"]} whose text is set at run time')
            steps.append({"seq": -3, "step": f"{', '.join(t['seen_by'])}: {what} on {t['screen']}{cond}", "file": t["file"], "line": t["line"]})
        if f["roles"] or f["signed_in"] or f["permissions"]:
            need = ("role " + " or ".join(f["roles"])) if f["roles"] else ("permission " + ", ".join(f["permissions"]) if f["permissions"] else "a signed-in user")
            for ev in f["access_evidence"][:2]:
                steps.append({"seq": -2, "step": f"the route lets through {need} ({ev['text']})", "file": ev["file"], "line": ev["line"]})
        steps.append({"seq": -1, "step": f"{f['id']} runs `{f['handler'] or 'its handler'}`", "file": f["file"], "line": f["line"]})
        if f["analysed"]:
            for x in f["fields"]:
                kind = {"file": "the uploaded file", "form": "the form field", "query": "the query parameter", "json": "the JSON field"}[x["source"]]
                steps.append({**_at(x), "step": f"reads {kind} `{x['name']}`"})
            for q in f["sql"]:
                bits = []
                if q["writes"]:
                    bits.append(f"{q['verb'].lower()}s {', '.join(q['writes'])}")
                if q["reads"]:
                    bits.append(f"reads {', '.join(q['reads'])}")
                for s in q["sets"]:
                    bits.append(f"sets {s['column']} = '{s['value']}'")
                for s in q["filters"]:
                    bits.append(f"only rows with {s['column']} = '{s['value']}'")
                for pc in q["param_columns"]:
                    if pc.get("upload"):
                        bits.append(f"keeps the stored file name of `{pc['upload']}` in column {pc['column']}")
                steps.append({**_at(q), "step": "; ".join(bits) or q["text"], "sql": q["text"]})
            for x in f["files"]:
                verb = {"store": "stores the uploaded file" + (f" `{x['upload']}`" if x.get("upload") else ""), "write": "writes the file",
                        "serve": "sends a file from", "delete": "deletes"}[x["op"]]
                steps.append({**_at(x), "step": f"{verb} {x['expr']}"})
            for x in f["external"]:
                steps.append({**_at(x), "step": f"{x['what']}: {x['text']}"})
            for x in f["background"]:
                steps.append({**_at(x), "step": f"starts background work: {x['text']}"})
            for x in f["messages"]:
                steps.append({**_at(x), "step": f'shows the message "{x["text"]}"'})
            for x in f["redirects"]:
                steps.append({**_at(x), "step": "redirects to " + (", ".join(x.get("to") or []) or x.get("endpoint") or x.get("path", ""))})
            for x in f["renders"]:
                steps.append({**_at(x), "step": f"shows {x.get('screen') or x['template']}"})
        steps.sort(key=lambda s: s.get("seq", 0))
        for s in steps:
            s.pop("seq", None)
        data = []
        for q in f["sql"]:
            for tb in q["reads"] + q["writes"]:
                row = next((d for d in data if d["table"] == tb), None)
                if row is None:
                    row = {"table": tb, "reads": [], "writes": [], "sets": [], "filters_on": [],
                           "defined": self.data.get(tb, {}).get("defined", [])}
                    data.append(row)
                at = {"file": q["file"], "line": q["line"], "via": q["via"]}
                if tb in q["reads"]:
                    row["reads"].append(at)
                if tb in q["writes"]:
                    row["writes"].append(at)
                row["sets"] += [f"{s['column']} = '{s['value']}'" for s in q["sets"] if s["table"] == tb]
                row["filters_on"] += [f"{s['column']} = '{s['value']}'" for s in q["filters"] if s["table"] == tb]
        assets = []
        for a in self.j["assets"]:
            roles = [k for k in ("registered_by", "stored_by", "written_by", "served_by", "deleted_by") if any(r["feature"] == fid for r in a[k])]
            shown = [sid for sid in a["screens"] if any(r.get("screen") == sid for r in f["renders"])]
            if roles or shown:
                assets.append({"asset": a["id"], "kind": a["kind"], "this_feature": [r.replace("_by", "") for r in roles]
                               + (["shows it"] if shown else [])})
        check = []
        for x in f["settings"]:
            check.append({"what": f"setting `{x['name']}`" + (f" (variable `{x['variable']}`)" if x.get("variable") else ""),
                          "file": x["file"], "line": x["line"], "via": x["via"]})
        for b in f["branches"]:
            check.append({"what": f"condition `{b['test']}`" + (f" → {b['outcome']}" if b["outcome"] else ""),
                          "file": b["file"], "line": b["line"], "via": b["via"]})
        for t in self.triggers(fid):
            for c in t["shown_when"]:
                check.append({"what": f"the control is only shown when `{c}`", "file": t["file"], "line": t["line"], "via": ""})
        for q in f["sql"]:
            for s in q["filters"]:
                check.append({"what": f"the query only returns rows with {s['table']}.{s['column']} = '{s['value']}'",
                              "file": q["file"], "line": q["line"], "via": q["via"]})
        for x in f["external"] + f["background"]:
            check.append({"what": f"depends on {x.get('what', 'background work')}: {x['text']}", "file": x["file"], "line": x["line"], "via": x["via"]})
        unverified = []
        if not f["analysed"]:
            unverified.append("the handler was not analysed (only Python handlers are followed), so what it reads and writes is unknown")
        if not f["roles"] and not f["signed_in"] and not f["permissions"]:
            unverified.append("no access check was found on the route; a check made in middleware or a base class would not be seen")
        for d in f["unread_decorators"]:
            unverified.append(f"{d['text']} also wraps the handler and was not read as an access check ({d['file']}:{d['line']})")
        for d in f["dynamic"]:
            unverified.append(f"{d['what']}: {d['text']} ({d['file']}:{d['line']})")
        if not self.triggers(fid):
            unverified.append("no link, button or script call that starts this feature was found on a screen")
        if f["analysed"] and not f["sql"] and not f["files"] and not f["renders"]:
            unverified.append("no SQL statement, file operation or template was found in the handler; "
                              "an ORM or another data layer is not followed")
        if any(h.get("inferred") for h in self.handoffs_from(fid) + self.handoffs_to(fid)):
            unverified.append("hand-overs are derived from a shared column value, not traced row by row")
        code = [{"what": f"handler `{f['handler']}`", "file": f["file"], "line": f["line"]}]
        seen = set()
        for c in f["calls"]:
            key = f"{c['def_file']}:{c['func']}"
            if key in seen:
                continue
            seen.add(key)
            code.append({"what": f"`{c['func']}`", "file": c["def_file"], "line": c["def_line"], "called_at": f"{c['file']}:{c['line']}",
                         "shared_with": len(self.functions[key]["features"]) - 1})
        return {"feature": fid, "called": self.label(fid), "user_types": self.who(fid),
                "access": {"roles": f["roles"], "permissions": f["permissions"], "signed_in": f["signed_in"], "evidence": f["access_evidence"]},
                "started_from": self.triggers(fid),
                "shows": [{"screen": r["screen"], "title": self.screens[r["screen"]]["title"], "also_seen_by": self.who_sees(r["screen"])}
                          for r in f["renders"] if r.get("screen")],
                "normal_flow": steps,
                "branches": [{"when": b["test"], "then": b["outcome"], "file": b["file"], "line": b["line"], "via": b["via"]} for b in f["branches"]],
                "hands_over_to": self.handoffs_from(fid), "receives_from": self.handoffs_to(fid),
                "code": code, "data": data, "assets": assets, "check": check, "not_verified": unverified, "how_to_read": CAVEAT}

    # ------------------------------------------------------------ B and E. from words
    def find(self, text: str, user: str = "", limit: int = 8) -> dict:
        query = tokens(text)
        phrase = " ".join(text.lower().split())
        cand: dict[str, dict] = {}

        def hit(fid: str, score: float, what: dict) -> None:
            c = cand.setdefault(fid, {"feature": fid, "score": 0.0, "matched": []})
            c["score"] += score
            if what not in c["matched"]:
                c["matched"].append(what)

        loose = {"screens": [], "terms": []}
        for t in self.j["terms"]:
            texts = [t["text"]] + [o["text"] for o in t.get("other_texts", [])]
            score = max(_score(query, phrase, x) for x in texts)
            if not score:
                continue
            what = {"on_screen": t["text"], "kind": t["kind"], "file": t["file"], "line": t["line"]}
            if t.get("other_texts"):
                what["also_shown_as"] = [o["text"] for o in t["other_texts"]]
            if t["conditions"]:
                what["shown_when"] = t["conditions"]
            if t.get("field"):
                what["field_in_code"] = t["field"]
            targets = list(t["leads_to"]) or ([t["feature"]] if t.get("feature") else [])
            if not targets and t["screen"]:
                targets = self.screens[t["screen"]]["routes"]
                score *= 0.7                            # a heading names the page, not an action
            if not targets:
                loose["terms"].append({**what, "screen": t["screen"], "note": "on a layout or a page no route was found for"})
            for fid in targets:
                hit(fid, score, what)
        for f in self.j["features"]:
            s = _score(query, phrase, " ".join(re.split(r"[^\w]+", f["path"]) + re.split(r"_", f["handler"])))
            if s:
                hit(f["id"], s * 0.5, {"route": f["id"], "handler": f["handler"], "file": f["file"], "line": f["line"]})
        for s in self.j["screens"]:
            sc = _score(query, phrase, s["title"])
            if sc:
                for fid in s["routes"]:
                    hit(fid, sc * 0.5, {"screen_title": s["title"], "screen": s["id"]})
                if not s["routes"]:
                    loose["screens"].append({"screen": s["id"], "title": s["title"], "kind": s["kind"]})
        assets = [{"asset": a["id"], "kind": a["kind"]} for a in self.j["assets"]
                  if _score(query, phrase, re.sub(r"[`/._:-]+", " ", a["name"]))]
        data = []
        for d in self.j["data"]:
            if _score(query, phrase, d["id"]):
                data.append({"table": d["id"]})
            for st in d["states"]:
                if _score(query, phrase, st["value"].replace("_", " ")):
                    data.append({"state": f"{d['id']}.{st['column']} = '{st['value']}'"})
        wanted = user.lower()
        out = []
        for c in cand.values():
            f = self.features[c["feature"]]
            who = self.who(c["feature"])
            sees = sorted({u for t in self.triggers(c["feature"]) for u in t["seen_by"]})
            row = {"feature": c["feature"], "called": self.label(c["feature"]), "score": round(c["score"], 2), "matched": c["matched"][:6],
                   "user_types": who, "started_from": sorted({t["screen"] for t in self.triggers(c["feature"])}),
                   "shows": [r["screen"] for r in f["renders"] if r.get("screen")],
                   "implemented_in": f"{f['file']}:{f['line']} {f['handler']}".strip(),
                   "hands_over_to": [{"user_types": h["to_user_types"], "to": h["to_screens"] or [h["to_feature"]],
                                      "because": h["because"]} for h in self.handoffs_from(c["feature"])][:4]}
            if wanted:
                names = [w.lower() for w in who + sees]
                row["for_this_user_type"] = wanted in names or ANYONE in names
            out.append(row)
        # the requester's own features come forward, but a clearly better match elsewhere still leads
        out.sort(key=lambda r: (-r["score"] * (1.3 if r.get("for_this_user_type") else 1.0), r["feature"]))
        if len(out) > 1 and out[0]["score"] > 0 and len({r["called"] for r in out[:limit]}) < len(out[:limit]):
            for r in out[:limit]:                       # same words in several places: say what tells them apart
                r["tell_apart"] = f"{', '.join(r['user_types'])}; from {', '.join(r['started_from']) or 'no screen found'}; {r['implemented_in']}"
        result = {"query": text, "words_used": query, "candidates": out[:limit], "more_candidates": max(0, len(out) - limit),
                  "also_matched": {k: v for k, v in (("assets", assets), ("data", data), ("screens_without_route", loose["screens"]),
                                                      ("terms_without_feature", loose["terms"][:6])) if v},
                  "next": "open a candidate with the feature id to see its flow, branches, hand-overs and what to check",
                  "how_to_read": CAVEAT}
        if wanted and wanted not in {u.lower() for u in self.users_by_name}:
            result["note"] = f"user type {user!r} is not one the code distinguishes; known: {', '.join(self.users_by_name) or 'none found'}"
        if not out:
            result["not_found"] = ("no term, screen or route matched these words. The words on screen may come from data or from "
                                   "a script; try the exact label, or start from the user type.")
        elif out[0]["score"] < 1.0:
            result["weak_match"] = "only partial word matches; treat the candidates as places to look, not as the answer"
        return result

    # ------------------------------------------------------------ C. from an asset or data
    def asset(self, name: str) -> dict:
        low = name.lower().strip("`'\" ")
        hits = [a for a in self.j["assets"] if low in (a["id"].lower(), a["name"].lower(), a.get("field", "").lower(),
                                                       a["id"].rsplit("/", 1)[-1].lower(), a["id"].split(":", 1)[-1].lower())]
        hits = hits or [a for a in self.j["assets"] if low and low in a["id"].lower()]
        tables = [d for d in self.j["data"] if low == d["id"].lower() or low.startswith(d["id"].lower() + ".")]
        if not hits and not tables:
            raise KeyError(f"no asset or data named {name!r}; assets: {', '.join(list(self.assets)[:20]) or 'none found'}; "
                           f"data: {', '.join(self.data) or 'none found'}")
        out = {"assets": [], "data": [], "how_to_read": CAVEAT}
        for a in hits[:6]:
            def rows(key: str) -> list[dict]:
                return [{**r, "user_types": self.who(r["feature"]), "called": self.label(r["feature"])} for r in a[key]]
            affected = sorted({u for sid in a["screens"] for u in self.who_sees(sid)})
            item = {"asset": a["id"], "kind": a["kind"], "name": a["name"],
                    "comes_from": {"picked_with": a.get("picked_with", []), "registered_by": rows("registered_by"),
                                   "written_by": rows("written_by")},
                    "stored_or_transformed_by": rows("stored_by"), "linked_data": a["columns"],
                    "delivered_by": rows("served_by"), "deleted_by": rows("deleted_by"),
                    "appears_on": [{"screen": sid, "seen_by": self.who_sees(sid),
                                    "through_layout": next((t["layout"] for t in a.get("through_layout", []) if t["screen"] == sid), "")}
                                   for sid in a["screens"]],
                    "used_in": a["used_in"],
                    "if_replaced_or_deleted": {"screens": a["screens"], "user_types": affected,
                                               "note": "these are the places the analysis found; a path built at run time is not seen"},
                    "not_verified": a["unknown"] + [r["inferred"] for r in a["stored_by"] if r.get("inferred")]}
            if a.get("file"):
                item["file"] = a["file"]
            out["assets"].append(item)
        for d in tables:
            def rows2(items: list[dict]) -> list[dict]:
                return [{**r, "user_types": self.who(r["feature"]), "called": self.label(r["feature"])} for r in items]
            out["data"].append({"table": d["id"], "defined": d["defined"], "columns": d["columns"],
                                "written_by": rows2(d["writers"]), "read_by": rows2(d["readers"]),
                                "states": [{"value": f"{st['column']} = '{st['value']}'", "set_by": rows2(st["set_by"]),
                                            "filtered_on_by": rows2(st["read_by"]), "tested_in": st["tested_in"]} for st in d["states"]],
                                "not_verified": ["access through an ORM or SQL built at run time is not seen"]})
        return out

    # ------------------------------------------------------------ D. from code
    def impact(self, path: str, line: int = 0, symbol: str = "") -> dict:
        path = re.sub(r"^(?:\./)+", "", path.replace("\\", "/"))
        f = self.p.file(path)
        if not f:
            raise KeyError(f"{path!r} is not a file of this project")
        direct: dict[str, list[str]] = {}

        def add(fid: str, why: str) -> None:
            direct.setdefault(fid, [])
            if why not in direct[fid]:
                direct[fid].append(why)

        screens: dict[str, str] = {}
        notes = []
        if path in self.screens:
            todo, seen = [path], set()
            while todo:
                sid = todo.pop()
                if sid in seen:
                    continue
                seen.add(sid)
                screens[sid] = "this template" if sid == path else f"built on {path}"
                for fid in self.screens[sid]["routes"]:
                    add(fid, f"renders {sid}")
                todo += self.screens[sid]["extended_by"] + self.screens[sid]["included_by"]
            if line:
                near = [t for t in self.j["terms"] if t["file"] == path and abs(t["line"] - line) <= 2]
                for t in near:
                    for fid in t["leads_to"]:
                        add(fid, f'started by "{t["text"]}" at line {t["line"]}')
        elif path in self.assets:
            for sid in self.assets[path]["screens"]:
                screens[sid] = "shows this file"
        else:
            for a in self.j["assets"]:
                for u in a["used_in"]:
                    if u["file"] == path and (not line or abs(u["line"] - line) <= 2):
                        for sid in a["screens"]:
                            screens.setdefault(sid, f"shows {a['id']}, which this file refers to")
            for s in self.j["screens"]:
                for c in s["calls"]:
                    if c["file"] == path and (not line or abs(c["line"] - line) <= 3):
                        screens.setdefault(s["id"], "loads this script")
                        add(c["feature"], f"called from this script at line {c['line']}")
            for t in self.j["terms"]:
                if t.get("i18n", {}).get("file") == path and (not line or t["i18n"]["line"] == line):
                    screens.setdefault(t["screen"], f'text of "{t["text"]}" comes from this file')
                    for fid in t["leads_to"]:
                        add(fid, f'its control "{t["text"]}" is worded in this file')
            for feat in self.j["features"]:
                if feat["file"] == path and (not line or feat["line"] - 3 <= line <= feat.get("end_line", feat["line"])) \
                        and (not symbol or feat["handler"] == symbol):
                    add(feat["id"], "its handler is here")
                for c in feat["calls"]:
                    if c["def_file"] != path:
                        continue
                    if symbol and c["func"] != symbol:
                        continue
                    if line and not (c["def_line"] <= line <= c["end_line"]):
                        continue
                    add(feat["id"], f"calls `{c['func']}`" + (f" through {c['via']}" if c["via"] else ""))
                for key in ("sql", "files", "settings", "branches"):
                    for x in feat[key]:
                        if x["file"] == path and line and x["line"] == line:
                            add(feat["id"], f"runs line {line}" + (f" through {x['via']}" if x["via"] else ""))
            if f.lang == "python" and not direct and not screens:
                notes.append("no route reaches this code through calls the analysis could follow; "
                             "callers that go through a class instance, a registry or a string are not seen")
        rows = []
        users: list[str] = []
        for fid, why in direct.items():
            feat = self.features[fid]
            trig = self.triggers(fid)
            shown = [r["screen"] for r in feat["renders"] if r.get("screen")]
            for sid in shown + [t["screen"] for t in trig]:
                screens.setdefault(sid, f"through {fid}")
            down = [{"user_types": h["to_user_types"], "screens": h["to_screens"], "feature": h["to_feature"], "because": h["because"]}
                    for h in self.handoffs_from(fid)]
            rows.append({"feature": fid, "called": self.label(fid), "why": why, "user_types": self.who(fid),
                         "started_from": [{"screen": t["screen"], "term": t["term"], "line": t["line"]} for t in trig],
                         "shows": shown, "then_affects": down})
            for u in self.who(fid) + [x for d in down for x in d["user_types"]]:
                if u not in users:
                    users.append(u)
        for sid in screens:
            for u in self.who_sees(sid):
                if u not in users:
                    users.append(u)
        return {"file": path, **({"line": line} if line else {}), **({"symbol": symbol} if symbol else {}),
                "features": rows, "screens": [{"screen": sid, "why": why, "seen_by": self.who_sees(sid)} for sid, why in screens.items()],
                "user_types_affected": users,
                "not_verified": notes + ["only calls that name a project function directly are followed; dynamic dispatch is not",
                                         "this lists who can be affected, not whether a given change breaks them"]}

    # ------------------------------------------------------------ the whole project in one answer
    def overview(self, onto: dict | None = None) -> dict:
        L = self.p.links
        note = (self.notes.get("Project") if self.notes else "") or ""
        readme = next((f for f in self.p.files if f.path.lower() in ("readme.md", "readme.en.md", "readme.txt", "readme")), None)
        langs: dict[str, int] = {}
        for f in self.p.files:
            if f.category in ("code", "script", "web", "test"):
                langs[f.lang] = langs.get(f.lang, 0) + 1
        topics = {}
        if self.notes:
            for key in self.notes.order:
                if key.startswith("Topic: ") and self.notes.get(key):
                    topics[key[7:]] = self.notes.get(key)
        out = {
            "project": self.p.name,
            "what_it_is": {"from_the_previous_owner": note, "from_the_readme": readme.summary if readme else ""},
            "size": {"files": len(self.p.files), "languages": dict(sorted(langs.items(), key=lambda kv: -kv[1]))},
            "how_it_starts": {"run_modes": [{"name": m["name"], "file": m["file"], "line": m["line"], "default": bool(m.get("default"))}
                                            for m in L.get("modes", [])],
                              "launch_scripts": list(L.get("launchers", {}))[:8],
                              "entry_points": [{"file": e["file"], "line": e["line"]} for e in L.get("entries", [])][:8]},
            "interfaces": {"http_routes": len(L.get("routes", [])), "mcp_tools": [t["name"] for t in L.get("mcp_tools", [])][:40],
                           "operations": sum(len(tb["ops"]) for tb in L.get("tables", []))},
            "settings": sorted(k for k, v in L.get("env", {}).items() if not v.get("system"))[:40],
            "who_uses_it": [{"user_type": u["name"], "screens": len(u["screens"]), "features": len(u["features"])} for u in self.j["user_types"]],
            "screens": len(self.j["screens"]), "data": [d["id"] for d in self.j["data"]],
            "assets": {k: sum(1 for a in self.j["assets"] if a["kind"] == k) for k in ("uploaded", "generated", "external", "static")},
            "notes_from_the_previous_owner": topics,
            "open_questions": [k for k in ("Project",) if self.notes is not None and not self.notes.get(k)],
            "where_to_go_next": {
                "a user asked for help": "handoff_request with their words (and their user type if you know it)",
                "what a kind of user sees and does": "handoff_users, then handoff_users with user",
                "one feature end to end": "handoff_feature",
                "an image, upload, generated file or table": "handoff_asset",
                "what a code change touches": "handoff_impact",
                "anything else by name": "handoff_search, handoff_entity, handoff_source, handoff_page",
            },
            "not_verified": self._gaps(10),
            "how_to_read": "Everything except the previous owner's notes was read from the files without running them. "
                           "What is not listed was not found, which does not mean it does not exist.",
        }
        if onto:
            out["found"] = onto.get("counts", {})
        return out

    def _gaps(self, limit: int) -> list[str]:
        out = [g["what"] + (f" ({g['file']}:{g['line']})" if g["file"] else "") for g in self.j["gaps"][:limit]]
        if len(self.j["gaps"]) > limit:
            out.append(f"… and {len(self.j['gaps']) - limit} more, listed in USERS.md")
        return out


def _at(x: dict) -> dict:
    return {"seq": x.get("seq", 0), "file": x["file"], "line": x["line"], **({"via": x["via"]} if x.get("via") else {}),
            **({"when": x["when"]} if x.get("when") else {})}


# ---------------------------------------------------------------------------- plain text for the command line

def format_find(result: dict) -> str:
    s = [f"request: {result['query']}", f"words used: {', '.join(result['words_used']) or '(none)'}", ""]
    if result.get("note"):
        s += [result["note"], ""]
    if result.get("not_found"):
        s += [result["not_found"], ""]
    if result.get("weak_match"):
        s += [result["weak_match"], ""]
    for i, c in enumerate(result["candidates"], 1):
        mark = "" if c.get("for_this_user_type", True) else "  [other user type]"
        s.append(f"{i}. {c['called']}  ->  {c['feature']}{mark}")
        s.append(f"   who: {', '.join(c['user_types'])} · code: {c['implemented_in']}")
        if c["started_from"]:
            s.append(f"   started from: {', '.join(c['started_from'])}")
        for m in c["matched"][:3]:
            if "on_screen" in m:
                cond = f" (shown when {' and '.join(m['shown_when'])})" if m.get("shown_when") else ""
                s.append(f"   matched {m['kind']} \"{m['on_screen']}\" at {m['file']}:{m['line']}{cond}")
        for h in c["hands_over_to"]:
            s.append(f"   then: {', '.join(h['user_types'])} at {', '.join(h['to'])}, because {h['because']} (inferred)")
        s.append("")
    for k, v in result["also_matched"].items():
        s.append(f"also matched {k.replace('_', ' ')}: " + "; ".join(str(next(iter(x.values()))) for x in v[:8]))
    s += ["", result["how_to_read"]]
    return "\n".join(s)


def format_feature(card: dict) -> str:
    s = [f"{card['feature']}  ({card['called']})", f"user types: {', '.join(card['user_types'])}", "", "normal flow:"]
    for st in card["normal_flow"]:
        via = f" [through {st['via']}]" if st.get("via") else ""
        when = f"when {' and '.join(st['when'])}: " if st.get("when") else ""
        s.append(f"  - {when}{st['step']}  ({st['file']}:{st['line']}){via}")
    if card["branches"]:
        s += ["", "branches:"]
        s += [f"  - if {b['when']}" + (f": {b['then']}" if b["then"] else "") + f"  ({b['file']}:{b['line']})" for b in card["branches"]]
    if card["hands_over_to"]:
        s += ["", "hands over to (inferred):"]
        for h in card["hands_over_to"]:
            target = h.get("to_feature") or ", ".join(h["to_screens"])
            s.append(f"  - {', '.join(h['to_user_types'])}: {target}, because {h['because']}")
    if card["receives_from"]:
        s += ["", "receives from (inferred):"]
        s += [f"  - {', '.join(h['from_user_types'])}: {h['what']} ({h['from_feature']}), because {h['because']}" for h in card["receives_from"]]
    if card["data"] or card["assets"]:
        s += ["", "data and assets:"]
        for d in card["data"]:
            bits = [x for x in ("reads" if d["reads"] else "", "writes" if d["writes"] else "") if x] + d["sets"] + [f"only {x}" for x in d["filters_on"]]
            s.append(f"  - table {d['table']}: {', '.join(dict.fromkeys(bits))}")
        s += [f"  - {a['asset']} ({a['kind']}): {', '.join(a['this_feature'])}" for a in card["assets"]]
    if card["check"]:
        s += ["", "check:"]
        s += [f"  - {c['what']}  ({c['file']}:{c['line']})" for c in card["check"]]
    if card["not_verified"]:
        s += ["", "not verified by the analysis:"]
        s += [f"  - {x}" for x in card["not_verified"]]
    s += ["", card["how_to_read"]]
    return "\n".join(s)
