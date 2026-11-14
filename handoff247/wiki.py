"""The LLM wiki: the ontology written out as small, interlinked Markdown pages that an AI
assistant (or a person) can read one at a time.

Layout, all inside the pack:

    llms.txt            entry point in the llms.txt convention
    llms-full.txt       every wiki page in one file, for pasting into a context window
    wiki/index.md       catalog of every page with a one-line summary
    wiki/AGENTS.md      how to read the wiki and where new knowledge has to be written
    wiki/overview.md    the project; wiki/notes.md what the previous owner wrote
    wiki/files/…        one page per file      wiki/areas/…       one per top-level folder
    wiki/modes/…        one per run mode       wiki/operations/…  one per operation
    wiki/tools/…        one per MCP tool       wiki/*.md          one list page per small class
    wiki/users/…        one per user type      wiki/features/…    one per route, the whole feature in one place
    wiki/screens/…      one per screen         wiki/assets/…, wiki/data/…  one per asset and data table

The pages are generated: they are rewritten on every run. What a person or an assistant
learns goes into the notes file, and the next run carries it into the pages.
"""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
from collections import defaultdict

from . import __version__
from .labels import t
from .notes import TOPICS
from . import render_users
from .explore import Explorer
from .render_md import LANG_NAMES, Linker

MARK = "generator: HandOff247"
OWN_PAGE = {"Area": "areas", "File": "files", "Mode": "modes", "Operation": "operations", "McpTool": "tools",
            "UserType": "users", "Route": "features", "Screen": "screens", "Asset": "assets", "Data": "data"}
LIST_PAGE = {"Table": "operations.md", "Subcommand": "subcommands.md", "EnvVar": "environment.md",
             "Port": "ports.md", "Package": "packages.md", "Host": "hosts.md", "Command": "commands.md", "Person": "people.md",
             "Term": "terms.md", "State": "states.md", "Function": "functions.md"}
NOTE_KEY = {"File": "File: ", "Area": "Area: ", "Mode": "Mode: ", "Operation": "Op: ", "UserType": "User: "}
ATTR_LABELS = {"language": "Language", "category": "Kind of file", "lines": "Lines", "not_parsed": "Not parsed",
               "files": "Files", "default": "Default mode", "transports": "Transports", "reads_stdin": "Reads standard input",
               "handler": "Handler", "expression": "Expression in the table", "routes": "Reachable through",
               "method": "Method", "name_from": "Name comes from", "development_only": "Development only",
               "kind": "Kind", "default_value": "Default value", "shown_when": "Shown when", "field": "Field in the code",
               "other_languages": "In other languages", "seen_by": "Seen by", "not_verified": "Not verified"}
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}
MAX_LIST = 60


def _slug(name: str, used: set[str]) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", name.replace("/", "__")).strip("-.") or "x"
    if len(s) > 100:
        s = s[:90] + "-" + hashlib.sha1(name.encode("utf-8")).hexdigest()[:8]
    if s.split(".")[0].lower() in RESERVED:
        s = "_" + s
    base, i = s, 2
    while s.lower() in used:
        s, i = f"{base}-{i}", i + 1
    used.add(s.lower())
    return s


def assign_pages(onto: dict) -> None:
    """Give every entity the pack-relative path of the wiki page that describes it."""
    used: dict[str, set[str]] = defaultdict(set)
    by_id = {e["id"]: e for e in onto["entities"]}
    for e in onto["entities"]:
        cls = e["type"]
        if cls == "Project":
            e["page"] = "wiki/overview.md"
        elif cls in OWN_PAGE:
            e["page"] = f"wiki/{OWN_PAGE[cls]}/{_slug(e['name'], used[cls])}.md"
        elif cls in LIST_PAGE:
            e["page"] = "wiki/" + LIST_PAGE[cls]
    for e in onto["entities"]:
        if e["type"] == "Type":
            owner = by_id.get("file:" + e.get("file", ""))
            e["page"] = owner["page"] if owner else "wiki/index.md"


def _code(name: str) -> str:
    return "`" + str(name).replace("`", "'") + "`"


def _value(v) -> str:
    if v is True:
        return "yes"
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return str(v)


class Wiki:
    def __init__(self, project, onto: dict, notes, linker: Linker, notes_label: str, date: str):
        self.p, self.o, self.n, self.date, self.notes_label = project, onto, notes, date, notes_label
        self.ents = {e["id"]: e for e in onto["entities"]}
        self.classes = {c["id"]: c for c in onto["schema"]["classes"]}
        self.rels = {r["id"]: r for r in onto["schema"]["relations"]}
        self.out, self.inn = defaultdict(list), defaultdict(list)
        for r in onto["relations"]:
            self.out[r["s"]].append(r)
            self.inn[r["o"]].append(r)
        self.by_class = defaultdict(list)
        for e in onto["entities"]:
            self.by_class[e["type"]].append(e)
        self.files = {f.path: f for f in project.files}
        self.linkers = {d: Linker(linker.mode, linker.base, "../" * d + linker.rel_prefix) for d in (1, 2)}
        self.project = self.by_class["Project"][0]
        self.ex = Explorer(project, notes)
        self.pages = {e["id"]: e["page"] for e in onto["entities"] if e.get("page")}

    def ctx(self, page: str) -> render_users.Ctx:
        """The user-context sections, with links that work from ``page``."""
        return render_users.Ctx(self.ex, lambda file, line=0, text=None: self.src(page, file, line, text),
                                lambda target: self.href(page, target), {k: v for k, v in self.pages.items() if v != page})

    # ------------------------------------------------------------ helpers
    def href(self, page: str, target: str) -> str:
        return posixpath.relpath(target, posixpath.dirname(page)).replace(" ", "%20")

    def ref(self, page: str, eid: str) -> str:
        e = self.ents[eid]
        name = e["name"] if e["type"] in ("Project", "Person") else _code(e["name"])
        if e.get("page") in (None, page):
            return name
        return f"[{name}]({self.href(page, e['page'])})"

    def src(self, page: str, file: str, line: int = 0, text: str | None = None) -> str:
        return self.linkers[page.count("/")](file, line, text)

    def front(self, title: str, e: dict | None = None) -> list[str]:
        s = ["---", MARK]
        if e:
            s += [f"id: {json.dumps(e['id'], ensure_ascii=False)}", f"type: {e['type']}"]
            if e.get("file"):
                s.append(f"source: {json.dumps(e['file'], ensure_ascii=False)}")
        s += ["---", "", f"# {title}", ""]
        return s

    def note(self, e: dict) -> str:
        if e["type"] == "Project":
            return self.n.get("Project")
        key = NOTE_KEY.get(e["type"])
        return self.n.get(key + e["name"]) if key else ""

    def relations(self, page: str, eid: str, skip: tuple[str, ...] = ()) -> list[str]:
        s = []
        for arrow, rows, end, word in (("→", self.out[eid], "o", "label"), ("←", self.inn[eid], "s", "inverse")):
            grouped = defaultdict(list)
            for r in rows:
                if r["p"] not in skip:
                    grouped[r["p"]].append(r)
            for p in [x["id"] for x in self.o["schema"]["relations"] if x["id"] in grouped]:
                items = grouped[p]
                s.append(f"**{self.rels[p][word]}** {arrow}\n")
                for r in items[:MAX_LIST]:
                    bits = [self.ref(page, r[end])]
                    if r.get("label"):
                        bits.append(f"({r['label']})")
                    if r.get("file"):
                        bits.append("· " + self.src(page, r["file"], r.get("line", 0)))
                    if r.get("inferred"):
                        bits.append(f"· *inferred: {r['inferred']}*")
                    s.append("- " + " ".join(bits))
                if len(items) > MAX_LIST:
                    s.append(f"- … and {len(items) - MAX_LIST} more (all of them are in `ontology.json`)")
                s.append("")
        return s

    def body(self, page: str, e: dict, skip: tuple[str, ...] = ()) -> list[str]:
        """Summary, attributes, the owner's note and the relations of one entity."""
        s = []
        if e.get("summary"):
            s += [f"> {e['summary']}", ""]
        ms = e.get("model_summary")
        if ms:
            s += [f"**{t('model_written', engine=ms.get('engine', ''), date=ms.get('date', ''))}.** "
                  "Check it against the source before relying on it.", "", f"> {ms['summary']}", ""]
        facts =[f"- **Class:** {self.classes[e['type']]['label']} — {self.classes[e['type']]['description']}"]
        for k, v in e.get("attrs", {}).items():
            if k == "language":
                v = LANG_NAMES.get(v, v)
            facts.append(f"- **{ATTR_LABELS.get(k, k)}:** {_code(v) if k in ('handler', 'expression', 'method') else _value(v)}")
        if e.get("file"):
            facts.append(f"- **Source:** {self.src(page, e['file'], e.get('line', 0))}")
        s += facts + [""]
        note = self.note(e)
        if note and e["type"] != "Project":
            s += ["**Notes from the previous owner**", "", *["> " + l if l.strip() else ">" for l in note.split("\n")], ""]
        s += self.relations(page, e["id"], skip)
        return s

    # ------------------------------------------------------------ pages
    def entity_page(self, e: dict) -> str:
        page = e["page"]
        s = self.front(_code(e["name"]), e)
        own = {"UserType": ("sees", "openTo"), "Route": ("displays", "runsCode"), "Screen": ("displays",)}.get(e["type"], ())
        s += self.body(page, e, own)                # what the section below tells is not listed twice
        key = e["id"].split(":", 1)[1]
        if e["type"] == "UserType" and key in self.ex.users_by_name:
            s += ["## What this user type sees and does", ""] + render_users.user_section(self.ctx(page), key, "##")
            others = [u for u in self.ex.users_by_name if u != key]
            if others:
                s += ["## Other user types", "", "Nothing here is hidden from you; follow a hand-over or open another user type: "
                      + ", ".join(self.ref(page, "user:" + u) for u in others) + ".", ""]
        elif e["type"] == "Route" and key in self.ex.features:
            s += render_users.feature_card(self.ctx(page), key)
        elif e["type"] == "Screen" and key in self.ex.screens:
            s += render_users.screen_section(self.ctx(page), key)
        elif e["type"] == "Asset" and key in self.ex.assets:
            s += ["## Where it comes from and where it shows", ""] + render_users.asset_section(self.ctx(page), key)
        elif e["type"] == "Data" and key in self.ex.data:
            s += ["## Who reads and writes it", ""] + render_users.data_section(self.ctx(page), key)
        if e["type"] == "File":
            f = self.files.get(e["name"])
            if f and f.summary and f.summary != e.get("summary"):
                s += ["## Comment in the file", "", f"{f.summary}" + (f" *({f.summary_source})*" if f.summary_source else ""), ""]
            syms = [x for x in (f.symbols if f else []) if x.public]
            if syms:
                s += ["## Defined here", ""]
                for x in syms[:120]:
                    name = (x.parent + "." if x.parent and x.kind == "method" else "") + x.name
                    s.append(f"- {_code(name)} — {x.kind}, {self.src(page, f.path, x.line, f'line {x.line}')}"
                             + (f" — {x.doc}" if x.doc else ""))
                if len(syms) > 120:
                    s.append(f"- … and {len(syms) - 120} more")
                s.append("")
        return "\n".join(s).rstrip("\n") + "\n"

    def list_page(self, cls: str) -> str:
        c = self.classes[cls]
        page = "wiki/" + LIST_PAGE[cls]
        s = self.front(c["plural"])
        s += [c["description"], "", f"{len(self.by_class[cls])} found. [Back to the index](index.md)", ""]
        if cls == "Term":                           # hundreds of short entries read better as one table
            s += ["| Text | Kind | Where | Shown when | Leads to |", "|---|---|---|---|---|"]
            for e in sorted(self.by_class[cls], key=lambda e: (e["name"].lower(), e["id"])):
                attrs = e.get("attrs", {})
                text = _code(e["name"]) + "".join(" / " + _code(o) for o in attrs.get("other_languages", []))
                leads = ", ".join(self.ref(page, r["o"]) for r in self.out[e["id"]] if r["p"] == "leadsTo")
                where = " ".join(self.ref(page, r["s"]) for r in self.inn[e["id"]] if r["p"] == "displays")
                row = [text, attrs.get("kind", ""), f"{where} {self.src(page, e.get('file', ''), e.get('line', 0))}".strip(),
                       _code(attrs["shown_when"]) if attrs.get("shown_when") else "", leads]
                s.append("| " + " | ".join(str(x).replace("|", "\\|") for x in row) + " |")
            return "\n".join(s).rstrip("\n") + "\n"
        for e in self.by_class[cls]:
            s += [f"## {_code(e['name'])}", ""]
            s += self.body(page, e)
        return "\n".join(s).rstrip("\n") + "\n"

    def overview(self) -> str:
        e, page = self.project, "wiki/overview.md"
        s = self.front(e["name"], e)
        note = self.n.get("Project")
        if note:
            s += ["**What the previous owner says it is**", "", *["> " + l if l.strip() else ">" for l in note.split("\n")], ""]
        elif e.get("summary"):
            s += [f"> {e['summary']} *(from the README)*", ""]
        else:
            s += ["*Nobody has written what this project is yet.*", ""]
        g = self.p.git
        if g.get("remote"):
            s.append(f"- **Repository:** {g['remote'].removesuffix('.git')}" + (f" at commit `{g['head']}`" if g.get("head") else ""))
        s += ["- **Human-readable pack:** [README](../README.md), [handover checklist](../HANDOVER.md), "
              "[how to run it](../RUNNING.md), [connections](../CONNECTIONS.md), [code map](../CODEMAP.md)",
              "- **What only the previous owner knew:** [notes](notes.md)", ""]
        s += ["## What was found", "", "| Class | Count | Where |", "|---|---|---|"]
        for c in self.o["schema"]["classes"]:
            n = self.o["counts"].get(c["id"], 0)
            if not n or c["id"] == "Project":
                continue
            where = f"[{LIST_PAGE[c['id']]}]({LIST_PAGE[c['id']]})" if c["id"] in LIST_PAGE else \
                ("on the page of the file that defines it" if c["id"] == "Type" else f"[index](index.md), under {c['plural']}")
            s.append(f"| {c['plural']} | {n} | {where} |")
        s.append("")
        modes = self.by_class["Mode"]
        launchers = list(self.p.links.get("launchers", {}))
        if modes or launchers:
            s += ["## How it starts", ""]
            for m in modes:
                s.append(f"- run mode {self.ref(page, m['id'])}" + (f" — {m['summary']}" if m.get("summary") else ""))
            for path in launchers[:12]:
                if "file:" + path in self.ents:
                    s.append(f"- launch script {self.ref(page, 'file:' + path)}")
            s.append("")
        s += ["## Relations", ""] + self.relations(page, e["id"])
        return "\n".join(s).rstrip("\n") + "\n"

    def notes_page(self) -> str:
        s = self.front("Notes from the previous owner")
        s += [f"Written by a person in `{self.notes_label}`; nothing on this page was derived from code. "
              "A question without an answer is a real gap: ask, do not guess.", ""]
        s += ["## What the project is", "", self.n.get("Project") or "*Not answered.*", ""]
        for key, _ in TOPICS:
            s += [f"## {t(key)}", "", self.n.get(f"Topic: {t(key)}") or "*Not answered.*", ""]
        return "\n".join(s).rstrip("\n") + "\n"

    def index(self) -> str:
        page = "wiki/index.md"
        s = self.front(f"Wiki: {self.p.name}")
        s += [f"<sub>Generated by HandOff247 {__version__} on {self.date}. Rewritten on every run; see [AGENTS.md](AGENTS.md).</sub>", "",
              f"{len(self.o['entities'])} things and {len(self.o['relations'])} relations between them, one small page each. "
              "Read the page you need and follow its links; do not load everything.", "",
              "## Start here", "",
              f"- [Overview](overview.md) — {self.project.get('summary') or 'the project and what was found in it'}",
              "- [Notes from the previous owner](notes.md) — what could not be read from the code",
              "- [Who uses it](../USERS.md) — user types, their screens, hand-overs, the words on the screens, assets",
              "- [AGENTS.md](AGENTS.md) — how to read this wiki and where to write what you learn",
              "- [ontology.json](../ontology.json) — the same content as data", ""]

        def catalog(cls: str, title: str | None = None) -> None:
            items = self.by_class[cls]
            if not items:
                return
            s.extend([f"## {title or self.classes[cls]['plural']} ({len(items)})", ""])
            for e in items:
                s.append(f"- {self.ref(page, e['id'])}" + self.line_summary(e))
            s.append("")
        catalog("UserType")
        catalog("Route", "Features")
        catalog("Screen")
        catalog("Asset")
        catalog("Data")
        catalog("Area")
        catalog("Mode")
        catalog("McpTool")
        catalog("Operation")
        lists = [c for c in LIST_PAGE if self.by_class[c]]
        if lists:
            s += ["## Lists", ""]
            for c in lists:
                s.append(f"- [{self.classes[c]['plural']}]({LIST_PAGE[c]}) — {len(self.by_class[c])}")
            s.append("")
        files = self.by_class["File"]
        if files:
            s += [f"## Files ({len(files)})", ""]
            last = None
            for e in sorted(files, key=lambda e: ("/" in e["name"], e["name"].split("/", 1)[0].lower(), e["name"].lower())):
                area = e["name"].split("/", 1)[0] if "/" in e["name"] else "(top level)"
                if area != last:
                    s += ["", f"### {area}", ""]
                    last = area
                s.append(f"- {self.ref(page, e['id'])}" + self.line_summary(e))
            s.append("")
        return "\n".join(s).rstrip("\n") + "\n"

    @staticmethod
    def line_summary(e: dict) -> str:
        if e.get("summary"):
            return f" — {e['summary']}"
        ms = e.get("model_summary")
        if ms:
            text = ms["summary"] if len(ms["summary"]) <= 220 else ms["summary"][:219].rstrip() + "…"
            return f" — *(model)* {text}"
        return ""

    def agents(self) -> str:
        s = self.front("How to use this wiki")
        s += [f"This wiki describes **{self.p.name}** for an AI assistant that has to answer questions about the project or "
              "change it. HandOff247 generated it by static analysis; it did not run the code and no language model wrote these pages.", "",
              "## Reading", "",
              "1. Start at [index.md](index.md). Open [overview.md](overview.md), then only the pages the question needs.",
              "2. Each page is one thing. `Relations` lists what it points to (→) and what points to it (←); follow those links.",
              "3. A `file:line` next to a statement is where it was observed. Open that source before you change code.",
              "4. *inferred* marks a conclusion, not an observation. Check it in the source before relying on it.",
              "   Text labelled *written by a language model* (and *(model)* in lists) was not checked by a person either.",
              "5. Something that is not in the wiki was not found. That does not mean it does not exist: code built from "
              "runtime strings, reflection or dependency-injection containers is not followed. Say that you do not know.",
              "6. [notes.md](notes.md) is the only human-written page. \"Not answered\" there is a question for a person.", "",
              "## Helping someone who uses the application", "",
              "The user types in this wiki (`users/`) are the kinds of user the analysed application tells apart. They are "
              "not access levels of the wiki: read every flow you need, whoever it belongs to. Five ways in:", "",
              "- **From a user type:** `users/<name>.md` lists the screens, what each control does and who picks the work up next.",
              "- **From words on a screen:** [terms.md](terms.md) has every link, button, field label, heading and message, "
              "with the feature it leads to. The word a user says and the name in the code often differ; the page gives both.",
              "- **From an asset or a table:** `assets/` and `data/` say who provides it, what stores it and where it shows.",
              "- **From code:** a file page lists the features that run it under *runs for*; a feature page lists its code.",
              "- **From a request:** find the feature through the words, then read its page in `features/`: started from, "
              "what the code does, branches, hand-overs, what to check, not verified.", "",
              "Two rules when you answer. The same word can be on several screens: name the screen and the user type, and "
              "if two candidates fit, show both instead of picking one. And a condition in the code is not a diagnosis: "
              "\"the article is only listed when status is in_review\" is what the code does, not proof of why this "
              "user's article is missing. Say what to check (*What to check* on the feature page) unless you have the "
              "live data or a log.", "",
              "## Classes", "", "| Class | Meaning |", "|---|---|"]
        s += [f"| {c['label']} | {c['description']} |" for c in self.o["schema"]["classes"]]
        s += ["", "## Relations", "", "| Relation | Read backwards | Meaning |", "|---|---|---|"]
        s += [f"| {r['label']} | {r['inverse']} | {r['description']} |" for r in self.o["schema"]["relations"]]
        s += ["", "## Writing", "",
              "Do not edit these pages: the next run overwrites them. Knowledge that should last goes into "
              f"`{self.notes_label}`, under the heading of the thing it is about:", "",
              "- `## Project` — what the project is and its status",
              "- `## Topic: <name>` — the handover questions listed in [notes.md](notes.md)",
              "- `## Area: <folder>`, `## File: <path>`, `## Mode: <name>`, `## Op: <operation>` — one thing each",
              "- `## User: <user type>` — who these users are in real life and what they usually ask for", "",
              "Write plain sentences, say only what you verified in the source, and never paste a password or token; "
              "say where it is kept. Then run `python -m handoff247 <project folder>` again: the note appears on the "
              "matching wiki page, in the handoff pages and in the viewer.", "",
              "## Files", "",
              "- `../llms.txt` — short entry point; `../llms-full.txt` — every page of this wiki in one file",
              "- `../ontology.json` — entities (`id`, `type`, `name`, `summary`, `page`) and relations (`s`, `p`, `o`, `file`, `line`)",
              "- `../index.html` — viewer with a graph of the same ontology", "",
              "## Working through MCP", "",
              "`python -m handoff247 mcp` is an MCP server over the same data: a briefing of the whole project, the flows "
              "of each user type, a search from a user's own words, one feature in full, assets, the effect of a code "
              "change, entities, source lines, what is still undocumented, and notes written under the right heading "
              "(marked as written by an agent). It is the supported way for an assistant to add to this wiki.", ""]
        return "\n".join(s).rstrip("\n") + "\n"

    def llms_txt(self) -> str:
        e = self.project
        s = [f"# {self.p.name}", ""]
        if e.get("summary"):
            s += [f"> {e['summary']}", ""]
        s += [f"Handoff pack generated by HandOff247 {__version__} on {self.date} by static analysis. "
              f"{len(self.o['entities'])} entities and {len(self.o['relations'])} relations; every relation has the file and line it was observed at.", "",
              "## Start here", "",
              "- [Overview](wiki/overview.md): what the project is, what was found, how it starts",
              "- [Wiki index](wiki/index.md): one line per page",
              "- [How to use the wiki](wiki/AGENTS.md): reading rules, classes, relations, where to write new knowledge",
              "- [Notes from the previous owner](wiki/notes.md): what could not be read from the code", "",
              "## Handoff pages", "",
              "- [Handover checklist](HANDOVER.md): unfinished work, what exists only on one computer, accounts, tools to install",
              "- [Who uses it](USERS.md): user types, their screens, what each control does, hand-overs, words on the screens, assets",
              "- [Running](RUNNING.md): how to start, run modes, environment variables, ports",
              "- [Connections](CONNECTIONS.md): which tool calls which, and over what",
              "- [Code map](CODEMAP.md): folders, shared foundations, dependencies", "",
              "## Data", "",
              "- [ontology.json](ontology.json): entities and relations",
              "- [handoff.json](handoff.json): everything the analysis found", "",
              "## Optional", "",
              "- [llms-full.txt](llms-full.txt): all wiki pages in one file",
              "- [File cards](FILES.md): one long page with every file", ""]
        return "\n".join(s)

    def render(self) -> dict[str, str]:
        """Pack-relative path → text for every wiki file, llms.txt and llms-full.txt included."""
        pages = {"wiki/index.md": self.index(), "wiki/AGENTS.md": self.agents(), "wiki/overview.md": self.overview(),
                 "wiki/notes.md": self.notes_page()}
        for cls in LIST_PAGE:
            if self.by_class[cls]:
                pages["wiki/" + LIST_PAGE[cls]] = self.list_page(cls)
        for cls in OWN_PAGE:
            for e in self.by_class[cls]:
                pages[e["page"]] = self.entity_page(e)
        full = [f"# {self.p.name}: the whole wiki in one file", "",
                f"Generated by HandOff247 {__version__} on {self.date}. Each section below is one page of `wiki/`.", ""]
        for path, text in pages.items():
            body = text.split("\n---\n", 1)[1] if text.startswith("---\n") else text
            full += [f"<!-- page: {path} -->", "", body.strip("\n"), "", "----", ""]
        out = dict(pages)
        out["llms.txt"] = self.llms_txt()
        out["llms-full.txt"] = "\n".join(full)
        return out
