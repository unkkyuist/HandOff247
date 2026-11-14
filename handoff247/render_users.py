"""Markdown for the user-context view: USERS.md and the wiki pages of user types, features,
screens, assets and data tables.

All of it is written from ``explore.Explorer``, the same object the MCP server and the
command line use, so a page, a tool answer and a diagram never disagree. Each statement
carries the file and line it was read from; what rests on an inference is marked
*inferred*, and every section ends with what was not verified.
"""
from __future__ import annotations

from .explore import CAVEAT, Explorer, applies
from .journeys import ANYONE, SIGNED_IN
from .labels import t

MAX_ROWS = 80


def cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def table(headers: list[str], rows: list[list]) -> list[str]:
    if not rows:
        return []
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows[:MAX_ROWS]]
    if len(rows) > MAX_ROWS:
        out.append(f"\n… and {len(rows) - MAX_ROWS} more rows; all of them are in `handoff.json` under `links.journeys`.")
    return out + [""]


def code(text) -> str:
    return "`" + str(text).replace("`", "'") + "`"


def user_label(name: str) -> str:
    return {ANYONE: "anyone (no role check found)", SIGNED_IN: "any signed-in user"}.get(name, name)


class Ctx:
    """Where a page lives: how to link a source line and how to link another page from here."""

    def __init__(self, ex: Explorer, link, href, pages: dict[str, str]):
        self.ex, self.L, self.href, self.pages = ex, link, href, pages

    def ent(self, eid: str, text: str) -> str:
        page = self.pages.get(eid)
        return f"[{text}]({self.href(page)})" if page else text

    def feat(self, fid: str) -> str:
        return self.ent("route:" + fid, code(fid))

    def screen(self, sid: str) -> str:
        return self.ent("screen:" + sid, code(sid))

    def user(self, name: str) -> str:
        return self.ent("user:" + name, code(name))

    def users(self, names: list[str]) -> str:
        return ", ".join(self.user(n) for n in names)

    def asset(self, aid: str) -> str:
        return self.ent("asset:" + aid, code(aid))

    def data(self, name: str) -> str:
        return self.ent("data:" + name, code(name))

    def at(self, x: dict) -> str:
        return self.L(x["file"], x.get("line", 0)) + (f" *(through {code(x['via'])})*" if x.get("via") else "")


def short(ex: Explorer, sid: str) -> str:
    """File name of a screen, or its whole path when another screen has the same name."""
    base = sid.rsplit("/", 1)[-1]
    return sid if sum(1 for s in ex.screens if s.rsplit("/", 1)[-1] == base) > 1 else base


def does(ex: Explorer, fid: str, method: str = "") -> str:
    """One line on what a feature changes, for a table cell. ``method`` narrows it to what a
    control with that HTTP method starts."""
    f = dict(ex.features[fid])
    for key in ("sql", "files", "external", "renders"):
        f[key] = [x for x in f[key] if applies(x, method)]
    bits = []
    for q in f["sql"]:
        for s in q["sets"]:
            bits.append(f"sets {code(s['table'] + '.' + s['column'] + ' = ' + repr(s['value']))}")
        for tb in q["writes"]:
            if not any(s["table"] == tb for s in q["sets"]):
                bits.append(f"{q['verb'].lower()}s {code(tb)}")
    for x in f["files"]:
        if x["op"] != "serve":
            bits.append({"store": "stores the uploaded file", "write": "writes a file", "delete": "deletes a file"}[x["op"]])
    for x in f["external"]:
        bits.append(x["what"])
    if not bits:
        for q in f["sql"]:
            for s in q["filters"]:
                bits.append(f"lists rows with {code(s['column'] + ' = ' + repr(s['value']))}")
        shown = [r["screen"] for r in f["renders"] if r.get("screen")]
        if shown:
            bits.append("shows " + ", ".join(code(short(ex, s)) for s in dict.fromkeys(shown)))
        elif any(x["op"] == "serve" for x in f["files"]):
            bits.append("sends a file")
    if not f["analysed"]:
        bits.append("*handler not analysed*")
    return "; ".join(dict.fromkeys(bits))


def then(c: Ctx, fid: str, method: str = "") -> str:
    out = []
    for h in c.ex.handoffs_from(fid, method):
        target = c.feat(h["to_feature"]) if h.get("to_feature") else ", ".join(c.screen(s) for s in h["to_screens"])
        if h.get("to_feature") and h["to_screens"]:
            target = ", ".join(c.screen(s) for s in h["to_screens"])
        out.append(f"→ {c.users(h['to_user_types'])}: {target} ({code(h['because'])}, *inferred*)")
    return "<br>".join(out)


# ---------------------------------------------------------------------------- sections

def user_section(c: Ctx, name: str, heading: str = "###") -> list[str]:
    ex = c.ex
    flow = ex.user_flow(name)
    s: list[str] = []
    if flow["note"]:
        s += [f"> **{t('notes')}**", ">", *["> " + l if l.strip() else ">" for l in flow["note"].split("\n")], ""]
    if flow["kind"] == "anyone":
        s += ["No role check was found on the routes below. A check made in middleware, a base class or the web server "
              "would not be seen.", ""]
    elif flow["told_by"]:
        s += ["The code tells this user type apart at " + ", ".join(c.L(e["file"], e["line"]) for e in flow["told_by"][:6])
              + (f" and {len(flow['told_by']) - 6} more places" if len(flow["told_by"]) > 6 else "") + ".", ""]
    for sc in flow["screens"]:
        title = f' "{sc["title"]}"' if sc["title"] else ""
        head = f"{heading}# Screen{title} — {c.screen(sc['screen'])}"
        s += [head, ""]
        facts = []
        if sc["opened_by"]:
            facts.append("opened by " + ", ".join(f"{c.feat(fid)} ({c.L(ex.features[fid]['file'], ex.features[fid]['line'])})"
                                                    for fid in sc["opened_by"]))
        else:
            facts.append("no route was found that opens it for this user type")
        if sc["layout"]:
            facts.append("built on " + ", ".join(c.screen(x) for x in sc["layout"]))
        if sc["also_seen_by"]:
            facts.append("also seen by " + c.users(sc["also_seen_by"]))
        s += ["; ".join(facts) + ".", ""]
        rows = []
        for it in sc["can_do_here"]:
            label = f'"{it["on_screen"]}"' if it["on_screen"] else "*(text set at run time)*"
            where = c.L(it["file"], it["line"]) + (" *(layout)*" if it.get("from_layout") else "")
            shown = " and ".join(code(x) for x in it["shown_when"])
            leads = "<br>".join(f"{c.feat(i['feature'])} → {c.L(i['file'], i['line'], i['handler'] or 'handler')}"
                                for i in it.get("implemented_in", []))
            if it.get("not_verified"):
                leads = f"*not verified: {it['not_verified']}*"
            elif it.get("external"):
                leads = f"another site: {code(it['external'])}"
            elif not leads:
                leads = "*not determined from the page; a script may handle it*"
            if it.get("needs_other_user_type"):
                leads += f"<br>*needs {', '.join(it['needs_other_user_type'])}*"
            what = "<br>".join(does(ex, fid, it["method"]) for fid in it["leads_to"])
            nxt = "<br>".join(x for x in (then(c, fid, it["method"]) for fid in it["leads_to"]) if x)
            rows.append([f"{label} ({it['kind']})", where, shown, leads, what, nxt])
        s += table(["On the screen", "Where", "Shown when", "Leads to", "What the code does", "Then"], rows)
        if sc["fields"]:
            s += ["Fields: " + "; ".join(f'"{f["label"]}"' + (f" → {code(f['field'])}" if f["field"] else "") for f in sc["fields"]) + ".", ""]
        if sc["assets"]:
            s += ["Shows: " + ", ".join(c.asset(a) for a in sc["assets"]) + ".", ""]
    if flow["features_without_a_screen_of_their_own"]:
        s += ["Actions that show no page of their own:", ""]
        for x in flow["features_without_a_screen_of_their_own"]:
            f = ex.features[x["feature"]]
            s.append(f"- {c.feat(x['feature'])} — {x['called']} — {c.L(f['file'], f['line'])}" + (f" — {does(ex, x['feature'])}" if does(ex, x["feature"]) else ""))
        s.append("")
    if flow["receives_from_others"]:
        s += ["Receives from other user types (*inferred*):", ""]
        for h in flow["receives_from_others"]:
            s.append(f"- from {c.users(h['from_user_types'])}: {h['what']} ({c.feat(h['from_feature'])}), because {code(h['because'])} "
                     f"— set at {c.at(h['set_at'])}, read at {c.at(h['read_at'])}")
        s.append("")
    if not flow["screens"] and not flow["features_without_a_screen_of_their_own"]:
        s += ["Nothing this user type can open was found.", ""]
    return s


def feature_card(c: Ctx, fid: str) -> list[str]:
    ex = c.ex
    card = ex.feature(fid)
    s = [f"**Called:** {card['called']}  ", f"**User types:** {c.users(card['user_types'])}", ""]
    if card["started_from"]:
        s += ["## Started from", ""]
        for x in card["started_from"]:
            what = f'{x["kind"]} "{x["term"]}"' if x["term"] else (x["kind"] if x["kind"] == "script call" else f"{x['kind']} whose text is set at run time")
            cond = f", shown when {' and '.join(code(w) for w in x['shown_when'])}" if x["shown_when"] else ""
            s.append(f"- {what} on {c.screen(x['screen'])} ({c.L(x['file'], x['line'])}){cond} — seen by {c.users(x['seen_by'])}")
        s.append("")
    if card["shows"]:
        s += ["## Shows", ""] + [f"- {c.screen(x['screen'])}" + (f' "{x["title"]}"' if x["title"] else "") +
                                 f" — seen by {c.users(x['also_seen_by'])}" for x in card["shows"]] + [""]
    s += ["## What the code does", "", "In the order of the handler. A step that starts with *when* only runs under that condition.", ""]
    for i, st in enumerate(card["normal_flow"], 1):
        when = f"*when* {' and '.join(code(w) for w in st['when'])}: " if st.get("when") else ""
        via = f" *(through {code(st['via'])})*" if st.get("via") else ""
        s.append(f"{i}. {when}{st['step']} — {c.L(st['file'], st['line'])}{via}")
    s.append("")
    if card["branches"]:
        s += ["## Branches", ""]
        s += table(["If", "Then", "Where"], [[code(b["when"]), b["then"] or "*(continues)*", c.at(b)] for b in card["branches"]])
    if card["hands_over_to"] or card["receives_from"]:
        s += ["## Hand-overs", "", "*Inferred:* derived from a column value that one statement sets and another tests.", ""]
        for h in card["hands_over_to"]:
            target = c.feat(h["to_feature"]) if h.get("to_feature") else ", ".join(c.screen(x) for x in h["to_screens"])
            extra = f"; controls \"{h['controls']}\"" if h.get("controls") else (f"; then {h['outcome']}" if h.get("outcome") else "")
            s.append(f"- → {c.users(h['to_user_types'])}: {target}"
                     + (f" ({', '.join(c.screen(x) for x in h['to_screens'])})" if h.get("to_feature") and h["to_screens"] else "")
                     + f", because {code(h['because'])}{extra} — set at {c.at(h['set_at'])}, tested at {c.at(h['read_at'])}")
        for h in card["receives_from"]:
            s.append(f"- ← {c.users(h['from_user_types'])}: {h['what']} ({c.feat(h['from_feature'])}), because {code(h['because'])} "
                     f"— set at {c.at(h['set_at'])}, read at {c.at(h['read_at'])}")
        s.append("")
    s += ["## Code", ""]
    for x in card["code"]:
        shared = f" — shared with {x['shared_with']} other feature(s)" if x.get("shared_with") else ""
        s.append(f"- {x['what']} — {c.L(x['file'], x['line'])}{shared}")
    s.append("")
    if card["data"] or card["assets"]:
        s += ["## Data and assets", ""]
        for d in card["data"]:
            bits = (["reads"] if d["reads"] else []) + (["writes"] if d["writes"] else []) + \
                [f"sets {code(x)}" for x in dict.fromkeys(d["sets"])] + [f"only rows with {code(x)}" for x in dict.fromkeys(d["filters_on"])]
            at = (d["writes"] or d["reads"])[0]
            s.append(f"- table {c.data(d['table'])}: {', '.join(bits)} — {c.at(at)}")
        for a in card["assets"]:
            s.append(f"- {c.asset(a['asset'])} ({a['kind']}): {', '.join(a['this_feature'])}")
        s.append("")
    if card["check"]:
        s += ["## What to check", "", "Settings, states and outside dependencies this feature depends on.", ""]
        s += [f"- {x['what']} — {c.at(x)}" for x in card["check"]] + [""]
    s += ["## Not verified by the analysis", ""]
    s += [f"- {x}" for x in card["not_verified"]] or ["- nothing specific to this feature"]
    s += ["", f"*{CAVEAT}*", ""]
    return s


def screen_section(c: Ctx, sid: str) -> list[str]:
    ex = c.ex
    sc = ex.screens[sid]
    s = [f"**Seen by:** {c.users(ex.who_sees(sid)) or 'not determined'}  ", f"**Kind:** {sc['kind']}", ""]
    if sc["routes"]:
        s += ["Shown by " + ", ".join(c.feat(fid) for fid in sc["routes"]) + ".", ""]
    if sc["extends"]:
        s += [f"Built on the layout {c.screen(sc['extends'])}; its menu and other terms appear here too.", ""]
    if sc["extended_by"] or sc["included_by"]:
        s += ["Part of: " + ", ".join(c.screen(x) for x in sc["extended_by"] + sc["included_by"]) + ".", ""]
    rows = []
    for tm in ex.screen_terms(sid):
        text = f'"{tm["text"]}"' if tm["text"] else "*(text set at run time)*"
        if tm.get("other_texts"):
            text += " / " + " / ".join(f'"{o["text"]}"' for o in tm["other_texts"])
        origin = c.L(tm["file"], tm["line"]) + (" *(layout)*" if tm.get("from_layout") else "")
        if tm.get("i18n"):
            origin += f"<br>text from {c.L(tm['i18n']['file'], tm['i18n']['line'])} ({code(tm['i18n']['key'])})"
        leads = ", ".join(c.feat(fid) for fid in tm["leads_to"])
        if tm.get("unmatched"):
            leads = f"*no route found for {code(tm['unmatched'])}*"
        elif tm.get("external"):
            leads = f"another site: {code(tm['external'])}"
        field = ""
        if tm.get("field"):
            field = code(tm["field"]) + "".join(f" read at {c.L(r['file'], r['line'])}" for r in tm.get("read_at", [])[:2])
        rows.append([text, tm["kind"], origin, " and ".join(code(x) for x in tm["conditions"]), leads, field])
    s += ["## Words on this screen", ""] + (table(["Text", "Kind", "Where", "Shown when", "Leads to", "Field in the code"], rows)
                                              or ["None found.", ""])
    if sc["calls"]:
        s += ["## Calls made by its scripts", ""]
        s += [f"- {c.feat(x['feature'])} from {c.L(x['file'], x['line'])}" for x in sc["calls"][:60]] + [""]
    if sc["assets"]:
        s += ["## Assets shown", ""] + [f"- {c.asset(a)}" for a in sc["assets"]] + [""]
    return s


def asset_section(c: Ctx, aid: str) -> list[str]:
    info = c.ex.asset(aid)["assets"]
    a = next((x for x in info if x["asset"] == aid), None)
    if not a:
        return []
    s = [f"**Kind:** {a['kind']}", ""]

    def rows(title: str, items: list[dict], extra=lambda r: "") -> None:
        if items:
            s.extend([f"**{title}**", ""])
            s.extend(f"- {c.users(r['user_types'])}: {r['called']} ({c.feat(r['feature'])}) — {c.at(r)}{extra(r)}"
                     + (f" — *inferred: {r['inferred']}*" if r.get("inferred") else "") for r in items)
            s.append("")
    if a["comes_from"]["picked_with"]:
        s += ["**Picked on the screen with**", ""]
        s += [f'- "{p["text"]}" — {c.L(p["file"], p["line"])}' for p in a["comes_from"]["picked_with"]] + [""]
    rows("Registered or changed by", a["comes_from"]["registered_by"])
    rows("Written by", a["comes_from"]["written_by"], lambda r: f" — {code(r['expr'])}" + (f", folder from setting {code(r['dir_env'])}" if r.get("dir_env") else ""))
    rows("Stored by", a["stored_or_transformed_by"], lambda r: f" — {code(r['expr'])}" + (f", folder from setting {code(r['dir_env'])}" if r.get("dir_env") else ""))
    if a["linked_data"]:
        s += ["**Linked data**", ""]
        s += [f"- the stored name is kept in {c.data(x['table'])}.{code(x['column'])} — {c.at(x)} *(traced through the variables)*"
              for x in a["linked_data"]] + [""]
    rows("Delivered by", a["delivered_by"], lambda r: "" if r.get("exact_file") else " — serves any file of that folder")
    rows("Deleted by", a["deleted_by"])
    if a["appears_on"]:
        s += ["**Appears on**", ""]
        for x in a["appears_on"]:
            s.append(f"- {c.screen(x['screen'])} — seen by {c.users(x['seen_by'])}"
                     + (f" *(through the layout {code(x['through_layout'])})*" if x["through_layout"] else ""))
        s.append("")
    if a["used_in"]:
        s += ["**Referenced at**", ""]
        s += [f"- {c.L(u['file'], u['line'])} — {u['how']}" + (f", shown when {' and '.join(code(w) for w in u['conditions'])}" if u.get("conditions") else "")
              for u in a["used_in"][:40]] + [""]
    imp = a["if_replaced_or_deleted"]
    s += ["**If it is replaced or deleted**", ""]
    if imp["screens"]:
        s.append(f"{len(imp['screens'])} screen(s) show it, seen by {c.users(imp['user_types'])}. {imp['note'].capitalize()}.")
    else:
        s.append("No screen was found that shows it. That is not proof that nothing uses it.")
    s.append("")
    if a["not_verified"]:
        s += ["**Not verified**", ""] + [f"- {x}" for x in a["not_verified"]] + [""]
    return s


def data_section(c: Ctx, name: str) -> list[str]:
    info = c.ex.asset(name)["data"]
    d = next((x for x in info if x["table"] == name), None)
    if not d:
        return []
    s = []
    if d["defined"]:
        s += ["Defined at " + ", ".join(c.L(x["file"], x["line"]) for x in d["defined"]) + ".", ""]
    if d["columns"]:
        s += ["Columns: " + ", ".join(code(x) for x in d["columns"]) + ".", ""]
    for title, key in (("Written by", "written_by"), ("Read by", "read_by")):
        if d[key]:
            s += [f"**{title}**", ""]
            seen = set()
            for r in d[key]:
                if (r["feature"], r["file"], r["line"]) in seen:
                    continue
                seen.add((r["feature"], r["file"], r["line"]))
                s.append(f"- {c.users(r['user_types'])}: {r['called']} ({c.feat(r['feature'])}) — {c.at(r)}")
            s.append("")
    if d["states"]:
        s += ["**States**", "", "A value that one feature sets and another filters on is where work passes from one user type to the next.", ""]
        rows = []
        for st in d["states"]:
            sets = "<br>".join(f"{c.users(r['user_types'])}: {r['called']} — {c.at(r)}" for r in st["set_by"])
            reads = "<br>".join(f"{c.users(r['user_types'])}: {r['called']} — {c.at(r)}" for r in st["filtered_on_by"])
            tests = "<br>".join(f"{code(x['condition'])} — {c.L(x['file'], x['line'])}" for x in st["tested_in"][:6])
            rows.append([code(st["value"]), sets, reads, tests])
        s += table(["Value", "Set by", "Listed by (query filter)", "Tested in a condition (same column and value, not traced)"], rows)
    s += ["**Not verified**", ""] + [f"- {x}" for x in d["not_verified"]] + [""]
    return s


# ---------------------------------------------------------------------------- USERS.md

def users_page(pg, pages: dict[str, str]) -> str:
    ex = Explorer(pg.p, pg.n)
    j = ex.j
    c = Ctx(ex, pg.L, lambda target: target, pages)
    s = [pg.header("title_users"), f"> {t('users_legend')}", ""]
    if not j["user_types"] and not j["screens"]:
        s += [t("users_none"), ""]
        return "\n".join(s) + "\n"
    s += [f"## {t('users_types')}", "", t("users_types_hint"), ""]
    rows = []
    for u in j["user_types"]:
        told = "no role check found on these routes" if u["kind"] == "anyone" else \
            ", ".join(pg.L(e["file"], e["line"]) for e in u["evidence"][:3]) + (" …" if len(u["evidence"]) > 3 else "")
        rows.append([c.user(u["name"]), user_label(u["name"]) if u["kind"] != "role" else "role", told,
                     ", ".join(code(short(ex, x)) for x in u["screens"]) or "–", len(u["features"])])
    s += table(["User type", "Kind", "Told apart at", "Screens", "Features"], rows)
    if "users" in pg.d:
        from .render_md import mermaid_block
        s += [t("users_diagram_hint"), "", mermaid_block(pg.d["users"], "users", t)]
    s += [f"## {t('users_flows')}", "", t("users_flows_hint"), ""]
    for u in j["user_types"]:
        s += [f"### {code(u['name'])}" + ("" if u["kind"] == "role" else f" — {user_label(u['name'])}"), ""]
        s += user_section(c, u["name"], "###")
    if j["handoffs"]:
        s += [f"## {t('users_handoffs')}", "", t("users_handoffs_hint"), ""]
        rows = []
        for h in j["handoffs"]:
            to = ex.features[h["to"]]
            shown = ", ".join(c.screen(r["screen"]) for r in to["renders"] if r.get("screen"))
            rows.append([c.users(ex.who(h["from"])), f"{ex.label(h['from'])}<br>{c.feat(h['from'])}",
                         code(f"{h['state'][0]}.{h['state'][1]} = '{h['state'][2]}'"), c.users(ex.who(h["to"])),
                         f"{shown or ex.label(h['to'])}<br>{c.feat(h['to'])}", f"set {c.at(h['set_at'])}<br>read {c.at(h['read_at'])}"])
        s += table(["From", "Action", "State", "To", "Where it shows up", "Evidence"], rows)
    feats = [f for f in j["features"]]
    if feats:
        s += [f"## {t('users_features')}", "", t("users_features_hint"), ""]
        rows = []
        for f in feats:
            trig = sorted({short(ex, x["screen"]) for x in ex.triggers(f["id"])})
            rows.append([c.feat(f["id"]), ex.label(f["id"]), c.users(ex.who(f["id"])), ", ".join(code(x) for x in trig),
                         pg.L(f["file"], f["line"], f["handler"] or None), does(ex, f["id"])])
        s += table(["Feature", "Called", "User types", "Started from", "Handler", "What it does"], rows)
    words = [x for x in j["terms"] if x["text"]]
    if words:
        s += [f"## {t('users_terms')}", "", t("users_terms_hint"), ""]
        rows = []
        for tm in sorted(words, key=lambda x: (x["text"].lower(), x["file"], x["line"])):
            text = f'"{tm["text"]}"' + "".join(f' / "{o["text"]}"' for o in tm.get("other_texts", []))
            seen = tm["roles"] or (ex.who_sees(tm["screen"]) if tm["screen"] else ex.who(tm["feature"]))
            leads = ", ".join(c.feat(fid) for fid in tm["leads_to"]) or (c.feat(tm["feature"]) if tm.get("feature") else "")
            impl = ""
            targets = tm["leads_to"] or ([tm["feature"]] if tm.get("feature") else [])
            if tm.get("read_at"):
                impl = f"{code(tm['field'])} read at " + ", ".join(pg.L(r["file"], r["line"]) for r in tm["read_at"][:2])
            elif targets:
                f = ex.features[targets[0]]
                impl = pg.L(f["file"], f["line"], f["handler"] or None)
            where = pg.L(tm["file"], tm["line"])
            if tm.get("i18n"):
                where += f"<br>text: {pg.L(tm['i18n']['file'], tm['i18n']['line'])}"
            rows.append([text, tm["kind"], where, c.users(seen), " and ".join(code(x) for x in tm["conditions"]), leads, impl])
        s += table(["Text on the screen", "Kind", "Where", "Seen by", "Shown when", "Leads to", "Implemented at"], rows)
    if j["data"]:
        s += [f"## {t('users_data')}", ""]
        for d in j["data"]:
            s += [f"### {c.data(d['id'])}", ""] + data_section(c, d["id"])
    if j["assets"]:
        s += [f"## {t('users_assets')}", "", t("users_assets_hint"), ""]
        rows = []
        for a in j["assets"]:
            info = ex.asset(a["id"])["assets"][0]
            come = info["comes_from"]["registered_by"] + info["comes_from"]["written_by"]
            who = "<br>".join(f"{c.users(r['user_types'])}: {r['called']} — {c.at(r)}" for r in come) or \
                ("ships with the project" if a["kind"] == "static" else "")
            store = "<br>".join(f"{code(r['expr'])} — {c.at(r)}" for r in info["stored_or_transformed_by"] + info["comes_from"]["written_by"])
            link = "<br>".join(f"{c.data(x['table'])}.{code(x['column'])} — {c.at(x)}" for x in info["linked_data"])
            shows = "<br>".join(f"{c.screen(x['screen'])} ({', '.join(x['seen_by'])})" for x in info["appears_on"][:6])
            if len(info["appears_on"]) > 6:
                shows += f"<br>… and {len(info['appears_on']) - 6} more"
            gone = ", ".join(info["if_replaced_or_deleted"]["user_types"]) or "*no use found*"
            rows.append([c.asset(a["id"]), a["kind"], who, store, link, shows, gone, "; ".join(info["not_verified"])])
        s += table(["Asset", "Kind", "Registered or changed by", "Stored or written by", "Linked data", "Appears on (seen by)",
                    "Replacing or deleting it affects", "Not verified"], rows)
    shared = [f for f in j["functions"] if len(f["features"]) > 1]
    if shared:
        s += [f"## {t('users_shared')}", "", t("users_shared_hint"), ""]
        rows = []
        for fn in sorted(shared, key=lambda f: -len(f["features"])):
            users = sorted({u for fid in fn["features"] for u in ex.who(fid)})
            rows.append([code(fn["name"]), pg.L(fn["file"], fn["line"]), len(fn["features"]), c.users(users)])
        s += table(["Function", "Defined at", "Features that run it", "User types reached"], rows)
    layouts = [x for x in j["screens"] if x["extended_by"] or x["included_by"]]
    if layouts:
        s += ["Shared screens (layouts and partials): " + "; ".join(
            f"{c.screen(x['id'])} is part of {len(x['extended_by']) + len(x['included_by'])} screen(s)" for x in layouts) + ".", ""]
    s += [f"## {t('users_gaps')}", "", t("users_gaps_hint"), ""]
    for g in j["gaps"]:
        s.append(f"- {g['what']}" + (f" — {pg.L(g['file'], g['line'])}" if g["file"] else ""))
    if not j["gaps"]:
        s.append("- No specific gap was recorded for this project. The general limits still apply: only Python handlers are "
                 "followed, an ORM is not read, and code that builds names at run time is not seen.")
    s += ["", f"*{CAVEAT}*", ""]
    return "\n".join(s) + "\n"
