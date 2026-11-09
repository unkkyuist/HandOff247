"""Markdown pages of the handoff pack. GitHub renders the ```mermaid blocks natively."""
from __future__ import annotations

import posixpath
from collections import Counter, defaultdict

from . import __version__
from .connect import area_of
from .i18n import T
from .mermaid import Flow, short
from .model import Project
from .notes import CHECKLIST_NAMES, RISK_NAMES, SECRET_NAMES, Notes

LANG_NAMES = {"csharp": "C#", "python": "Python", "javascript": "JavaScript", "typescript": "TypeScript",
              "powershell": "PowerShell", "shell": "Shell", "batch": "Batch", "markdown": "Markdown",
              "html": "HTML", "css": "CSS", "json": "JSON", "toml": "TOML", "yaml": "YAML", "msbuild": "MSBuild"}


class Linker:
    """Turns file:line into a link. Modes: relative (pack inside the project), url (e.g. GitHub blob), plain."""

    def __init__(self, mode: str, base: str = "", rel_prefix: str = ""):
        self.mode, self.base, self.rel_prefix = mode, base.rstrip("/") + "/" if base else "", rel_prefix

    def __call__(self, path: str, line: int = 0, text: str | None = None) -> str:
        label = text if text is not None else (f"{path}:{line}" if line else path)
        label = label.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
        if self.mode == "plain" or not path:
            return f"`{label}`" if text is None else label
        anchor = f"#L{line}" if line else ""
        target = (self.base if self.mode == "url" else self.rel_prefix) + path.replace(" ", "%20") + anchor
        return f"[{label}]({target})"


def cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def table(headers: list[str], rows: list[list]) -> str:
    if not rows:
        return ""
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(cell(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def mermaid_block(fl: Flow | None, name: str, t) -> str:
    if fl is None:
        return ""
    return f"```mermaid\n{fl.render()}```\n\n<sub>{t('diagram_source', file=f'diagrams/{name}.mmd')}</sub>\n"


def note_block(text: str, t) -> str:
    if not text:
        return ""
    quoted = "\n".join("> " + l if l.strip() else ">" for l in text.split("\n"))
    return f"> **{t('notes')}**\n>\n{quoted}\n"


def more(items: list[str], limit: int, t) -> str:
    if len(items) <= limit:
        return ", ".join(items)
    return ", ".join(items[:limit]) + " " + t("more", n=len(items) - limit)


class Pages:
    def __init__(self, project: Project, diagrams: dict[str, Flow], notes: Notes, lang: str, link: Linker,
                 notes_label: str, date: str):
        self.p, self.d, self.n, self.lang, self.link = project, diagrams, notes, lang, link
        self.t = T(lang)
        self.notes_label = notes_label
        self.date = date
        self.files = {f.path: f for f in project.files}
        self.out_edges = defaultdict(list)
        self.in_edges = defaultdict(list)
        for e in project.edges:
            self.out_edges[e.src].append(e)
            self.in_edges[e.dst].append(e)

    # ------------------------------------------------------------ helpers
    def header(self, title_key: str, **kw) -> str:
        t = self.t
        g = self.p.git
        source = self.p.name
        if g.get("remote") and g.get("head"):
            source = f"{g['remote'].removesuffix('.git')}@{g['head']}"
        elif g.get("head"):
            source = f"{self.p.name}@{g['head']}"
        lines = [f"# {t(title_key, **kw)}", "",
                 f"<sub>{t('generated', version=__version__, source=source, date=self.date)}</sub>", ""]
        if title_key != "title_readme":
            lines += [f"[{t('back')}](README.md)", ""]
        return "\n".join(lines) + "\n"

    def L(self, path: str, line: int = 0, text: str | None = None) -> str:
        return self.link(path, line, text)

    def importance(self) -> list[tuple[str, str]]:
        """Files a successor should open first, with the reason (all derived from facts)."""
        L = self.p.links
        out: list[tuple[str, str]] = []
        seen = set()

        def add(p: str, why: str):
            if p and p in self.files and p not in seen:
                seen.add(p)
                out.append((p, why))
        ko = self.lang == "ko"
        for f in self.p.files:
            if f.path.lower() in ("readme.md", "readme.en.md", "readme.txt", "readme"):
                add(f.path, "what the project says about itself" if not ko else "프로젝트 소개 문서")
                break
        for m in L["modes"]:
            add(m["file"], "entry point; picks the run mode" if self.lang != "ko" else "진입점, 실행 모드를 고름")
        for e in L["entries"]:
            if e["file"].endswith(".cs"):
                add(e["file"], "entry point" if self.lang != "ko" else "진입점")
        for tb in L["tables"]:
            add(tb["file"], (f"dispatch table: {len(tb['ops'])} operations" if self.lang != "ko"
                             else f"분기표: operation {len(tb['ops'])}개"))
        for p in list(L.get("launchers", {}))[:2]:
            add(p, "how people start it" if not ko else "사람이 실행하는 스크립트")
        for h in L["hubs"]:
            add(h["file"], (f"shared foundation used by {h['used_by']} files" if self.lang != "ko"
                            else f"{h['used_by']}개 파일이 쓰는 공통 기반"))
        handlers = Counter()
        for tb in L["tables"]:
            for op in tb["ops"]:
                if op["handler_file"]:
                    handlers[op["handler_file"]] += 1
        tools = sorted({x["file"] for x in L["mcp_tools"]})
        for p in tools:
            add(p, "MCP tool definitions" if self.lang != "ko" else "MCP 도구 정의")
        for p, n in handlers.most_common(5):
            add(p, f"handles {n} operations" if self.lang != "ko" else f"operation {n}개 처리")
        for e in self.p.edges:
            if e.kind == "runs" and self.files.get(e.src) and self.files[e.src].category == "script":
                add(e.src, "launch script" if self.lang != "ko" else "실행 스크립트")
        for f in self.p.files:
            if f.path.lower() in ("agents.md", "claude.md", "contributing.md", "readme.en.md", "readme.ko.md"):
                add(f.path, "project document" if self.lang != "ko" else "프로젝트 문서")
        return out

    def undocumented(self) -> list[str]:
        out = []
        for p, why in self.importance():
            f = self.files[p]
            if f.category == "docs":
                continue
            if not self.n.get(f"File: {p}"):
                out.append(p)
        return out

    # ------------------------------------------------------------ README
    def readme(self) -> str:
        t, L, p = self.t, self.p.links, self.p
        s = [self.header("title_readme", name=p.name)]
        s.append(f"> {t('legend', notes=f'`{self.notes_label}`')}\n")
        # at a glance
        code_files = [f for f in p.files if f.category != "asset"]
        metrics = [(t("metric_files"), len(p.files)), (t("metric_lines"), f"{sum(f.lines for f in p.files):,}"),
                   (t("metric_langs"), len({f.lang for f in code_files if f.lang in LANG_NAMES and f.category in ('code', 'script', 'web', 'test')})),
                   (t("metric_modes"), len({m["name"] for m in L["modes"]})),
                   (t("metric_ops"), sum(len(tb["ops"]) for tb in L["tables"])),
                   (t("metric_routes"), len(L["routes"])), (t("metric_tools"), len(L["mcp_tools"])),
                   (t("metric_env"), len([k for k, v in L["env"].items() if not v["system"]]))]
        metrics = [m for m in metrics if str(m[1]) not in ("0",)]
        s.append(f"## {t('at_a_glance')}\n")
        s.append(table([m[0] for m in metrics], [[m[1] for m in metrics]]))
        langs = Counter()
        lines = Counter()
        for f in p.files:
            if f.lang in LANG_NAMES and f.category in ("code", "script", "web", "test"):
                langs[f.lang] += 1
                lines[f.lang] += f.lines
        if langs:
            s.append(" · ".join(f"{LANG_NAMES[k]} {v} ({lines[k]:,} {t('lines')})" for k, v in langs.most_common()) + "\n")
        # what it is
        s.append(f"\n## {t('what_it_is')}\n")
        proj_note = self.n.get("Project")
        if proj_note:
            s.append(note_block(proj_note, t))
        else:
            s.append(f"*{t('todo_project')}*\n")
        readme = next((f for f in p.files if f.path.lower() in ("readme.md", "readme.en.md", "readme.txt", "readme")), None)
        if readme and readme.summary:
            s.append(f"\n{t('from_readme', file=self.L(readme.path))}: *{readme.summary}*\n")
        # system map
        if "system" in self.d:
            s.append(f"\n## {t('system_map')}\n\n{t('system_map_hint')}\n\n" + mermaid_block(self.d["system"], "system", t))
        elif "areas" in self.d:
            s.append(f"\n## {t('areas_map')}\n\n" + mermaid_block(self.d["areas"], "areas", t))
        s.append(f"\n## {t('pages')}\n")
        s.append(f"- [RUNNING.md](RUNNING.md) — {t('page_running')}")
        s.append(f"- [CONNECTIONS.md](CONNECTIONS.md) — {t('page_connections')}")
        s.append(f"- [CODEMAP.md](CODEMAP.md) — {t('page_codemap')}")
        s.append(f"- [FILES.md](FILES.md) — {t('page_files')}")
        s.append(f"- [index.html](index.html) — {t('page_viewer')}\n")
        # reading order
        order = self.importance()
        if order:
            s.append(f"## {t('reading_order')}\n")
            for i, (path, why) in enumerate(order[:12], 1):
                f = self.files[path]
                summ = f" — {f.summary}" if f.summary and f.category != "docs" else ""
                s.append(f"{i}. {self.L(path)} — **{why}**{summ}")
            s.append("")
        # notes topics
        for names, key, todo in ((CHECKLIST_NAMES, "topic_checklist", "todo_checklist"),
                                 (RISK_NAMES, "topic_risks", "todo_risks"),
                                 (SECRET_NAMES, "topic_secrets", "todo_secrets")):
            s.append(f"## {t(key)}\n")
            v = self.n.topic(names)
            s.append(note_block(v, t) if v else f"*{t(todo)}*\n")
        gaps = self.undocumented()
        if gaps:
            s.append(f"## {t('gaps')}\n\n{t('gaps_hint', notes=f'`{self.notes_label}`')}\n")
            for g in gaps[:20]:
                s.append(f"- {self.L(g)}")
            if len(gaps) > 20:
                s.append(f"- {t('more', n=len(gaps) - 20)}")
            s.append("")
        g = p.git
        if g.get("commits"):
            s.append(f"## {t('recent_commits')}\n")
            for c in g["commits"]:
                s.append(f"- `{c['sha']}` {c['date']} — {c['subject']}")
            if g.get("uncommitted"):
                s.append(f"\n{t('uncommitted', n=g['uncommitted'])}")
            s.append("")
        return "\n".join(s) + "\n"

    # ------------------------------------------------------------ RUNNING
    def running(self) -> str:
        t, L = self.t, self.p.links
        s = [self.header("title_running")]
        if "startup" in self.d:
            s.append(f"## {t('startup_chain')}\n\n{t('startup_hint')}\n\n" + mermaid_block(self.d["startup"], "startup", t))
        if L["modes"]:
            by_file = defaultdict(list)
            for m in L["modes"]:
                by_file[m["file"]].append(m)
            for path, modes in by_file.items():
                s.append(f"\n## {t('modes')}\n\n{t('modes_hint', file=self.L(path), var=modes[0].get('var', 'args'))}\n")
                rows = []
                for m in modes:
                    exposes = list(m["transports"])
                    if m["routes"]:
                        exposes.append(f'{len(m["routes"])} HTTP routes' if self.lang != "ko" else f'HTTP 라우트 {len(m["routes"])}개')
                    exposes += [f"→ {x}" for x in m["tables"]]
                    note = self.n.get(f"Mode: {m['name']}")
                    rows.append([f"`{m['name']}`" + (f" ({t('default')})" if m["default"] else ""),
                                 self.L(path, m["start"], f"{short(path)}:{m['start']}–{m['end']}"),
                                 more(m["uses"], 6, t), ", ".join(exposes), note])
                s.append(table([t("mode"), t("where"), t("uses"), t("exposes"), t("notes")], rows))
        launches = [l for l in L["launches"] if self.files.get(l["file"]) and self.files[l["file"]].category in ("script", "config") and not l["ci"]]
        if launches:
            s.append(f"\n## {t('launch_scripts')}\n")
            rows = []
            for l in launches:
                rows.append([self.L(l["file"], l["line"]), f"`{l['text'][:140]}`",
                             ", ".join(self.L(x) for x in l["targets"]) + (f" → `{l['arg']}`" if l["arg"] else "")])
            s.append(table([t("where"), t("command"), t("runs")], rows))
        if L["env"]:
            s.append(f"\n## {t('env_vars')}\n\n{t('env_hint')}\n")
            rows = []
            for name, use in sorted(L["env"].items(), key=lambda kv: (kv[1]["system"], kv[0])):
                reads = [self.L(r["file"], r["line"]) + (f" (`{r['default']}`)" if r["default"] else "") for r in use["reads"]]
                writes = [self.L(w["file"], w["line"]) + (f" = `{w['value']}`" if w.get("value") else "") for w in use["writes"]]
                rows.append([f"`{name}`" + (f" ({t('system_var')})" if use["system"] else ""), more(reads, 4, t), more(writes, 4, t)])
            s.append(table([t("name"), t("read_by"), t("set_by")], rows))
        if L["ports"]:
            s.append(f"\n## {t('ports')}\n")
            s.append(table([t("port"), t("where"), t("source")],
                           [[f"`{x['port']}`", self.L(x["file"], x["line"]), x["source"]] for x in L["ports"]]))
        if L["runtime_paths"]:
            s.append(f"\n## {t('runtime_paths')}\n\n{t('runtime_paths_hint')}\n")
            seen = {}
            for rp in L["runtime_paths"]:
                key = " / ".join(rp["parts"])
                seen.setdefault(key, []).append(self.L(rp["file"], rp["line"]))
            rows = [[f"`{k}`", more(v, 3, t)] for k, v in sorted(seen.items())]
            s.append(table([t("path"), t("where")], rows[:80]))
        if L["build_targets"]:
            s.append(f"\n## {t('build')}\n")
            s.append(table([t("file"), "Assembly", "SDK", "Framework", t("version")],
                           [[self.L(b["file"]), b["assembly"], b["sdk"], b["framework"], b["version"]] for b in L["build_targets"]]))
        if L["packages"]:
            s.append(f"\n## {t('packages')}\n")
            rows = []
            for pk in sorted(L["packages"], key=lambda x: (x["ecosystem"], x["name"].lower())):
                where = self.L(pk["file"], pk["line"]) if pk["line"] else more([self.L(u) for u in pk.get("used_in", [])], 3, t)
                rows.append([f"`{pk['name']}`", pk.get("version", ""), pk["ecosystem"], where])
            s.append(table([t("package"), t("version"), t("kind"), t("declared_in")], rows))
        tests = [f for f in self.p.files if f.category == "test"]
        if tests:
            s.append(f"\n## {t('tests')}\n")
            rows = []
            for f in tests:
                modes = sorted({l["mode"] for l in L["launches"] if l["file"] == f.path and l["mode"]})
                rows.append([self.L(f.path), f.summary or "", ", ".join(f"`{m}`" for m in modes)])
            s.append(table([t("file"), t("summary"), t("in_modes")], rows))
        if L["subcommands"]:
            s.append(f"\n## {t('subcommands')}\n")
            s.append(table([t("file"), t("command"), t("description")],
                           [[self.L(c["file"], c["line"]), f"`{c['name']}`", c["help"]] for c in L["subcommands"]]))
        return "\n".join(s) + "\n"

    # ------------------------------------------------------------ CONNECTIONS
    def connections(self) -> str:
        t, L = self.t, self.p.links
        s = [self.header("title_connections")]
        if "operations" in self.d:
            s.append(f"## {t('interface_map')}\n\n{t('interface_hint')}\n\n" + mermaid_block(self.d["operations"], "operations", t))
        if L["routes"]:
            s.append(f"\n## {t('routes')}\n")
            s.append(table([t("verb"), t("path"), t("where"), t("forwards_to"), t("in_modes")],
                           [[r["verb"], f"`{r['path']}`", self.L(r["file"], r["line"]), r["forwards_to"],
                             ", ".join(r["modes"])] for r in L["routes"]]))
        if L["mcp_tools"]:
            s.append(f"\n## {t('mcp_tools')}\n\n{t('mcp_tools_hint')}\n")
            rows = []
            for x in L["mcp_tools"]:
                star = "*" if "snake_case" in x["name_source"] else ""
                desc = x["description"]
                desc = desc if len(desc) < 160 else desc[:157] + "…"
                rows.append([f"`{x['name']}`{star}", f"`{x['op']}`" if x["op"] else "",
                             self.L(x["file"], x["line"], f"{x['method'] or x['name']}"), desc])
            s.append(table([t("tool"), t("operation"), t("where"), t("description")], rows))
        if L["mcp_clients"]:
            s.append(f"\n## {t('mcp_clients')}\n")
            s.append(table([t("file"), "server", t("command"), t("mode"), t("runs")],
                           [[self.L(c["file"], c["line"]), c["server"], f"`{c['command']} {' '.join(c['args'])}`".strip(),
                             c["mode"], self.L(c["target"]) if c["target"] else c["url"]] for c in L["mcp_clients"]]))
        for tb in L["tables"]:
            s.append(f"\n## {t('dispatch_tables')}: `{tb['id']}`\n")
            s.append(t("dispatch_hint", table=tb["id"], file=self.L(tb["file"], tb["line"]), selector=tb["selector"]) + "\n")
            rows = []
            for op in tb["ops"]:
                handler = ""
                if op["handler_type"] and op["handler_method"]:
                    label = f"{op['handler_type']}.{op['handler_method']}"
                    handler = self.L(op["handler_file"], 0, label) if op["handler_file"] else f"`{label}`"
                elif op["expr"]:
                    handler = f"`{op['expr'][:60]}`"
                users = sorted({u["file"] for u in op["used_by"]})
                docs = sorted({d["file"] for d in op["documented_in"]})
                note = self.n.get(f"Op: {op['key']}")
                rows.append([self.L(tb["file"], op["line"], op["key"]), handler,
                             more([self.L(u) for u in users], 3, t), ", ".join(f"`{m}`" for m in op["mcp_tools"]),
                             more([self.L(d) for d in docs], 2, t), note])
            s.append(table([t("operation"), t("handler"), t("called_by"), "MCP", t("documented_in"), t("notes")], rows))
        if L["consumers"]:
            s.append(f"\n## {t('callers_table')}\n")
            names = {"http": t("channel_http"), "process": t("channel_process"), "in-process": t("channel_inproc")}
            rows = []
            for c in L["consumers"]:
                ch = names.get(c.get("channel", ""), t("channel_unknown"))
                via = c.get("route") or (f"`{c['mode']}` mode" if c.get("mode") else c.get("detail", ""))
                if c.get("inferred"):
                    ch += f" ({t('inferred')})"
                wrapper = c.get("wrapper", "")
                wl = self.L(wrapper.rsplit(":", 1)[0], int(wrapper.rsplit(":", 1)[1]), f"{c['func']}()") if wrapper else f"`{c['func']}()`"
                rows.append([self.L(c["file"], c["first_line"], c["file"]), wl, ch, via, len(c["keys"])])
            s.append(table([t("file"), t("wrapper"), t("channel"), t("forwards_to"), t("count")], rows))
            inferred = [c for c in L["consumers"] if c.get("inferred")]
            if inferred:
                s.append("\n" + "\n".join(f"- {t('inferred')}: {self.L(c['file'])} — {c['inferred']}" for c in inferred[:12]) + "\n")
        return "\n".join(s) + "\n"

    # ------------------------------------------------------------ CODEMAP
    def codemap(self) -> str:
        t, L = self.t, self.p.links
        s = [self.header("title_codemap")]
        if "code" in self.d:
            s.append(f"## {t('code_map')}\n\n{t('code_map_hint')}\n\n" + mermaid_block(self.d["code"], "code", t))
        if "areas" in self.d:
            s.append(f"\n## {t('areas_map')}\n\n" + mermaid_block(self.d["areas"], "areas", t))
        if L["hubs"]:
            s.append(f"\n## {t('hubs')}\n")
            for h in L["hubs"]:
                f = self.files[h["file"]]
                s.append(f"- {self.L(h['file'])} — {t('used_by_n', n=h['used_by'])}" + (f" — {f.summary}" if f.summary else ""))
            s.append("")
        s.append(f"\n## {t('components')}\n")
        kinds = {"uses", "injects", "imports", "extends", "loads", "runs", "dispatches", "calls-op"}
        by_area = defaultdict(list)
        for f in self.p.files:
            if f.category in ("code", "script", "web", "test"):
                by_area[area_of(f.path)].append(f)
        for area in sorted(by_area):
            note = self.n.get(f"Area: {area}")
            s.append(f"### {area}\n")
            if note:
                s.append(note_block(note, t))
            rows = []
            for f in by_area[area]:
                outs = sorted({short(e.dst) for e in self.out_edges[f.path] if e.kind in kinds})
                ins = sorted({short(e.src) for e in self.in_edges[f.path] if e.kind in kinds})
                summary = self.n.get(f"File: {f.path}") or f.summary
                rows.append([self.L(f.path, 0, short(f.path) if area != "(root)" else f.path), f"{f.lines}",
                             summary[:180], more(outs, 6, t), more(ins, 6, t)])
            s.append(table([t("file"), t("lines"), t("summary"), t("depends_on"), t("used_by")], rows))
        return "\n".join(s) + "\n"

    # ------------------------------------------------------------ FILES
    def file_cards(self) -> str:
        t, L = self.t, self.p.links
        s = [self.header("title_files")]
        iface = defaultdict(list)
        for m in L["modes"]:
            iface[m["file"]].append(f"mode `{m['name']}` (L{m['start']}–{m['end']})")
        for r in L["routes"]:
            iface[r["file"]].append(f"route `{r['verb']} {r['path']}` (L{r['line']})")
        for x in L["mcp_tools"]:
            iface[x["file"]].append(f"MCP `{x['name']}`")
        for tb in L["tables"]:
            iface[tb["file"]].append(f"dispatch `{tb['id']}` ({len(tb['ops'])} ops, L{tb['line']})")
        by_area = defaultdict(list)
        for f in self.p.files:
            if f.category != "asset":
                by_area[area_of(f.path)].append(f)
        toc = " · ".join(f"[{a}](#{a.strip('()').lower().replace(' ', '-').replace('.', '')})" for a in sorted(by_area))
        s.append(toc + "\n")
        for area in sorted(by_area):
            s.append(f"\n## {area}\n")
            for f in by_area[area]:
                s.append(f"### {f.path}\n")
                tags = [x for x in f.tags if not x.startswith("ns:")]
                meta = f"`{LANG_NAMES.get(f.lang, f.lang)}` · {f.lines} {t('lines')} · {f.category}"
                if tags:
                    meta += " · " + ", ".join(tags)
                ns = next((x[3:] for x in f.tags if x.startswith("ns:")), "")
                if ns:
                    meta += f" · namespace `{ns}`"
                s.append(meta + " · " + self.L(f.path, 0, "source") + "\n")
                if f.skipped:
                    s.append(f"*{t('skipped', reason=f.skipped)}*\n")
                note = self.n.get(f"File: {f.path}")
                if note:
                    s.append(note_block(note, t))
                if f.summary:
                    s.append(f"> {f.summary}  \n> <sub>{t('comment_from', src=f.summary_source)}</sub>\n")
                syms = [x for x in f.symbols if x.public and x.kind not in ("h3",)]
                if syms:
                    s.append(f"**{t('symbols')}**\n")
                    for x in syms[:16]:
                        parent = f"{x.parent}." if x.parent and x.kind == "method" else ""
                        doc = f" — {x.doc}" if x.doc else ""
                        s.append(f"- {self.L(f.path, x.line, f'{parent}{x.name}')} · {x.kind}{doc}")
                    if len(syms) > 16:
                        s.append(f"- {t('more', n=len(syms) - 16)}")
                    s.append("")
                if iface[f.path]:
                    s.append(f"**{t('interfaces')}:** " + more(iface[f.path], 8, t) + "\n")
                outs = defaultdict(set)
                for e in self.out_edges[f.path]:
                    outs[e.kind].add(e.dst)
                ins = defaultdict(set)
                for e in self.in_edges[f.path]:
                    ins[e.kind].add(e.src)
                if outs:
                    s.append(f"**{t('links_out')}:** " + "; ".join(
                        f"{k} → " + more([self.L(x, 0, short(x)) for x in sorted(v)], 6, t) for k, v in sorted(outs.items())) + "\n")
                if ins:
                    s.append(f"**{t('links_in')}:** " + "; ".join(
                        f"{k} ← " + more([self.L(x, 0, short(x)) for x in sorted(v)], 6, t) for k, v in sorted(ins.items())) + "\n")
        return "\n".join(s) + "\n"


def make_linker(mode: str, project: Project, out_dir, link_base: str) -> Linker:
    from pathlib import Path
    if mode == "plain":
        return Linker("plain")
    if link_base:
        return Linker("url", link_base)
    root = Path(project.root).resolve()
    out = Path(out_dir).resolve()
    try:
        rel = out.relative_to(root)
        prefix = "/".join([".."] * len(rel.parts)) + "/"
        return Linker("relative", rel_prefix=prefix)
    except ValueError:
        pass
    g = project.git
    remote = g.get("remote", "")
    if mode in ("auto", "url") and remote.startswith("https://github.com/") and g.get("head"):
        sub = (g.get("subdir") or "").strip("/")
        return Linker("url", f"{remote.removesuffix('.git')}/blob/{g.get('head_full') or g['head']}/" + (sub + "/" if sub else ""))
    return Linker("plain")
