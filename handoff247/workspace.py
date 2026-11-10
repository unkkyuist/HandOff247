"""A folder that holds several projects: one pack per project plus an index of all of them.

The index answers the questions of a person about to leave: which projects exist, which of
them live only on this computer, what is still uncommitted or unpushed, how far each handover
is, and which projects point into each other's folders.
"""
from __future__ import annotations

import html
import json
import os
import re
from collections import Counter
from pathlib import Path

from . import __version__, leaving
from . import summarize as model_summaries
from .build import write_pack
from .inventory import ALWAYS_SKIP_DIRS, CODE_LANGS, SCRIPT_LANGS, classify, excluded, read_ignore
from .mermaid import Flow
from .notes import DEFAULT_NAME, load, skeleton, update
from .pipeline import analyze_project
from .render_html import MARKED, MERMAID, PURIFY, TEMPLATE
from .render_md import LANG_NAMES, cell, table

MANIFESTS = {"package.json", "pyproject.toml", "setup.py", "requirements.txt", "cargo.toml", "go.mod", "pom.xml",
             "build.gradle", "build.gradle.kts", "makefile", "cmakelists.txt", "project.godot", "dockerfile",
             "composer.json", "gemfile", "deno.json", "wrangler.toml"}
MANIFEST_EXT = (".sln", ".csproj", ".fsproj", ".vbproj", ".xcodeproj", ".uproject")
REL_REF = re.compile(rf"(?<![\w.])((?:\.\.{leaving.SEP})+{leaving.SEG}(?:{leaving.SEP}{leaving.SEG})*)")


def project_reason(d: Path) -> str:
    """Why a folder counts as a project ('' when it does not)."""
    if (d / ".git").exists():
        return "git"
    code = False
    try:
        with os.scandir(d) as entries:
            for entry in entries:
                if not entry.is_file():
                    continue
                low = entry.name.lower()
                if low in MANIFESTS or low.endswith(MANIFEST_EXT):
                    return "manifest"
                if classify(entry.name)[0] in CODE_LANGS | SCRIPT_LANGS:
                    code = True
    except OSError:
        return ""
    return "code" if code else ""


def _children(d: Path, out: Path) -> list[Path]:
    kids = []
    try:
        for c in sorted(d.iterdir(), key=lambda p: p.name.lower()):
            if not c.is_dir() or c.is_symlink() or c.name.startswith(".") or c.name.lower() in ALWAYS_SKIP_DIRS:
                continue
            if c.resolve() == out.resolve() or (c / "workspace.json").is_file() or (c / "handoff.json").is_file():
                continue
            kids.append(c)
    except OSError:
        pass
    return kids


def find_projects(root: Path, out: Path, patterns: list[str] | None = None) -> tuple[list[Path], list[str]]:
    """Projects one or two levels below ``root`` and the folders where none was recognised."""
    projects, loose = [], []
    for child in _children(root, out):
        if patterns and excluded(child.name + "/", patterns):
            continue
        if project_reason(child):
            projects.append(child)
            continue
        inner = [g for g in _children(child, out) if project_reason(g)
                 and not (patterns and excluded(f"{child.name}/{g.name}/", patterns))]
        if inner:
            projects += inner
        else:
            loose.append(child.name)
    return projects, loose


def is_workspace(root: Path, out: Path) -> bool:
    """True when ``root`` holds projects rather than being one: it has no manifest of its own
    or at least two sub-folders that are their own Git repositories."""
    projects, _ = find_projects(root, out)
    own_repos = [p for p in projects if (p / ".git").exists()]
    if len(own_repos) >= 2:
        return True
    return not project_reason(root) and any(project_reason(p) in ("git", "manifest") for p in projects)


def slug(rel: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", rel.replace("/", "-")).strip("-") or "project"


def _norm(p: str) -> str:
    return os.path.normcase(os.path.normpath(p))


def cross_refs(project, root: Path, others: dict[str, str]) -> list[dict]:
    """Paths in this project's files that point into another project's folder.
    ``others`` maps a normalised absolute folder to the project name."""
    own = _norm(project.root)
    roots = sorted(others, key=len, reverse=True)

    def target(abs_path: str) -> str:
        n = _norm(abs_path)
        if n == own or n.startswith(own + os.sep):
            return ""
        for r in roots:
            if n == r or n.startswith(r + os.sep):
                return others[r]
        return ""
    found: dict[str, dict] = {}

    def add(name: str, file: str, line: int) -> None:
        e = found.setdefault(name, {"to": name, "count": 0, "where": []})
        e["count"] += 1
        if len(e["where"]) < 3 and not any(w["file"] == file for w in e["where"]):
            e["where"].append({"file": file, "line": line})
    for mp in project.links["leaving"]["machine_paths"]:
        if re.match(r"[A-Za-z]:", mp["path"]):
            name = target(mp["path"].replace("/", os.sep).replace("\\", os.sep))
            if name:
                for w in mp["where"]:
                    add(name, w["file"], w["line"])
    for f in project.files:
        if not f.text or f.skipped or ".." not in f.text or "vendored" in f.tags:
            continue
        base = Path(project.root, f.path).parent
        for ln, line in enumerate(f.text.split("\n"), 1):
            if ".." not in line or len(line) > 2000:
                continue
            for m in REL_REF.finditer(line):
                rel = re.sub(r"\\+", "/", m.group(1))
                name = target(os.path.join(base, *rel.split("/")))
                if name:
                    add(name, f.path, ln)
    return sorted(found.values(), key=lambda e: (-e["count"], e["to"]))


def _describe(project, notes) -> str:
    text = notes.get("Project")
    if not text:
        readme = next((f for f in project.files if f.path.lower() in leaving.README_NAMES), None)
        text = readme.summary if readme else ""
    first = next((l.strip() for l in text.split("\n") if l.strip()), "")
    return first if len(first) <= 200 else first[:197] + "…"


def _git_cell(g: dict) -> str:
    if not g["repo"]:
        return "not in Git"
    bits = []
    if not g["remotes"]:
        bits.append("no remote")
    n = sum(u["commits"] for u in g["unpushed"])
    if n:
        bits.append(f"{n} unpushed")
    if g["uncommitted"]:
        bits.append(f"{g['uncommitted']} uncommitted")
    if g["stashes"]:
        bits.append(f"{g['stashes']} stash")
    return ", ".join(bits) or "clean, pushed"


def attention(s: dict) -> list[str]:
    """What must not be lost when the computer goes away, most serious first."""
    g, out = s["git"], []
    if not g["repo"]:
        out.append("is not in Git: the only copy is this folder")
    elif not g["remotes"]:
        out.append("has no Git remote: the history exists only on this computer")
    else:
        n = sum(u["commits"] for u in g["unpushed"])
        if n:
            out.append(f"has {n} commit(s) that are on no remote")
        if g["stashes"]:
            out.append(f"has {g['stashes']} stash(es)")
    if g["repo"] and g["uncommitted"]:
        out.append(f"has {g['uncommitted']} uncommitted change(s)")
    if s["local_key"]:
        out.append(f"has {s['local_key']} ignored settings or data file(s) that are not in the repository")
    if s["secrets"]:
        out.append(f"has {s['secrets']} line(s) that look like a key or token")
    return out


def summarize(project, notes, info: dict, rel: str, folder: str, refs: list[dict]) -> dict:
    lv = project.links["leaving"]
    langs = Counter()
    for f in project.files:
        if f.lang in LANG_NAMES and f.category in ("code", "script", "web", "test"):
            langs[f.lang] += f.lines
    file_items = [k for k, _ in skeleton(project) if k.startswith("File: ")]
    ok, total = leaving.score(info["readiness"])
    lo = lv["local_only"] or []
    return {"name": rel, "pack": folder, "description": _describe(project, notes),
            "languages": [LANG_NAMES[k] for k, _ in langs.most_common(4)],
            "files": len(project.files), "lines": sum(f.lines for f in project.files),
            "git": lv["git"], "last_commit": lv["git"].get("last_commit", ""),
            "ready": ok, "checks": total, "open_checks": [r["label"] for r in info["readiness"] if r["state"] == "todo"],
            "notes_files": sum(1 for k in file_items if notes.get(k)), "files_to_note": len(file_items),
            "local_key": sum(1 for x in lo if x["kind"] in ("settings or secrets", "data")),
            "secrets": len(lv["secrets"]), "todos": len(lv["todos"]), "refs": refs}


def diagram(summaries: list[dict]) -> Flow | None:
    linked = {s["name"] for s in summaries if s["refs"]} | {r["to"] for s in summaries for r in s["refs"]}
    if not linked:
        return None
    fl = Flow("LR")
    ids = {}
    for s in summaries:
        if s["name"] in linked:
            label = s["name"] + ("\n" + ", ".join(s["languages"][:3]) if s["languages"] else "")
            ids[s["name"]] = fl.node(s["name"], label, "round", "entry" if attention(s) else "file")
    for s in summaries:
        for r in s["refs"]:
            fl.edge(ids[s["name"]], ids.get(r["to"], ""), f"{r['count']} path(s)")
    return fl


def index_md(title: str, summaries: list[dict], failed: list[dict], loose: list[str], date: str, page: str) -> str:
    s = [f"# Handoff: {title}", "",
         f"<sub>Generated by HandOff247 {__version__} on {date}: {len(summaries)} project(s). Re-run `handoff247 go` to refresh.</sub>", ""]
    ok = sum(x["ready"] for x in summaries)
    total = sum(x["checks"] for x in summaries)
    s.append(f"> One pack per project. Open a project's name for its diagrams, structure, handover checklist, "
             f"a graph of everything found and a wiki for AI assistants (`llms.txt` here lists them all). "
             f"Across all projects **{ok} of {total}** handover checks are ready.\n")
    warn = [(x, attention(x)) for x in summaries]
    warn = [(x, a) for x, a in warn if a]
    s.append("## Before the computer goes away\n")
    if warn:
        s.append("These would be lost or left unfinished. The detail is on each project's Handover page.\n")
        for x, a in warn:
            s.append(f"- **[{x['name']}]({x['pack']}/{'index.html#HANDOVER.md' if page == 'index.html' else 'HANDOVER.md'})** " + "; ".join(a))
        s.append("")
    else:
        s.append("Every project is in Git, pushed, and has no ignored settings or data files.\n")
    s.append("## Projects\n")
    rows = []
    for x in summaries:
        notes = f"{x['notes_files']}/{x['files_to_note']}" if x["files_to_note"] else "–"
        rows.append([f"[{x['name']}]({x['pack']}/{page})", x["description"], ", ".join(x["languages"]),
                     f"{x['files']} / {x['lines']:,}", x["last_commit"], _git_cell(x["git"]), f"{x['ready']}/{x['checks']}", notes])
    s.append(table(["Project", "What it is", "Languages", "Files / lines", "Last commit", "Git", "Ready", "Files with notes"], rows))
    fl = diagram(summaries)
    if fl:
        s.append("\n## How the projects point at each other\n")
        s.append("An arrow means files of one project contain a path into another project's folder. Projects without such paths are not drawn.\n")
        s.append(f"```mermaid\n{fl.render()}```\n")
        rows = []
        for x in summaries:
            for r in x["refs"]:
                rows.append([x["name"], r["to"], r["count"], ", ".join(f"`{w['file']}:{w['line']}`" for w in r["where"])])
        s.append(table(["From", "To", "Paths", "Where"], rows))
    if failed:
        s.append("\n## Could not be analysed\n")
        s += [f"- `{cell(x['name'])}` — {cell(x['error'])}" for x in failed]
        s.append("")
    if loose:
        s.append("\n## Folders where no project was recognised\n")
        s.append("No Git repository, manifest or code file at the top level or one level down. Check them by hand.\n")
        s.append(", ".join(f"`{x}`" for x in loose) + "\n")
    return "\n".join(s) + "\n"


INDEX_SCRIPT = r"""
const SRC = JSON.parse(document.getElementById('data').textContent).md;
const page = document.getElementById('page');
const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
if (window.marked && window.DOMPurify) page.innerHTML = DOMPurify.sanitize(marked.parse(SRC, {gfm: true}));
else page.innerHTML = '<pre>' + esc(SRC) + '</pre>';
(async () => {
  if (!window.mermaid) return;
  mermaid.initialize({startOnLoad: false, securityLevel: 'strict', theme: 'default', flowchart: {htmlLabels: true, useMaxWidth: false}});
  let n = 0;
  for (const code of page.querySelectorAll('pre > code.language-mermaid')) {
    const box = document.createElement('div'); box.className = 'diagram';
    try { box.innerHTML = (await mermaid.render('ws' + (++n), code.textContent)).svg; code.parentElement.replaceWith(box); } catch (e) {}
  }
})();
"""


def index_html(title: str, md: str, date: str) -> str:
    style = re.search(r"<style>.*?</style>", TEMPLATE, re.S).group(0)
    payload = json.dumps({"md": md}, ensure_ascii=False).replace("</", "<\\/")
    name = html.escape(f"Handoff · {title}")
    return ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"<meta name=\"generator\" content=\"HandOff247 {__version__}\">\n<title>{name}</title>\n{style}\n</head>\n<body>\n"
            f"<header><div><h1>{name}</h1><div class=\"meta\">HandOff247 {__version__} · {date}</div></div></header>\n"
            "<main><article id=\"page\"></article></main>\n"
            f"<script id=\"data\" type=\"application/json\">{payload}</script>\n"
            f"<script src=\"{MARKED}\"></script>\n<script src=\"{PURIFY}\"></script>\n<script src=\"{MERMAID}\"></script>\n"
            f"<script>{INDEX_SCRIPT}</script>\n</body>\n</html>\n")


def build_workspace(root: Path, out: Path, date: str, excludes: list[str] | None = None, log=print,
                    summaries_for=None) -> dict:
    root, out = root.resolve(), out.resolve()
    patterns = read_ignore(root, excludes)
    dirs, loose = find_projects(root, out, patterns)
    names = {d: d.relative_to(root).as_posix() for d in dirs}
    others = {_norm(str(d)): names[d] for d in dirs}
    out.mkdir(parents=True, exist_ok=True)
    summaries, failed = [], []
    for i, d in enumerate(dirs, 1):
        rel = names[d]
        folder = slug(rel)
        try:
            project = analyze_project(d, rel, excludes)
            own = d / DEFAULT_NAME
            notes_path = own if own.is_file() else out / "notes" / f"{folder}.notes.md"
            notes_path.parent.mkdir(parents=True, exist_ok=True)
            update(notes_path, project)
            notes = load(notes_path)
            label = DEFAULT_NAME if notes_path == own else f"../notes/{notes_path.name}"
            # model summaries stay in the handoff folder: the projects themselves are not written to
            model_summaries.prepare(project, notes, out / "notes" / f"{folder}.summaries.json", summaries_for,
                              log=lambda m: log(f"  {rel}: {m}"))
            info = write_pack(project, out / folder, notes, "local", "", date, label)
            summaries.append(summarize(project, notes, info, rel, folder, cross_refs(project, root, others)))
            x = summaries[-1]
            log(f"[{i}/{len(dirs)}] {rel}: {x['files']} files, ready {x['ready']}/{x['checks']}, Git: {_git_cell(x['git'])}")
        except Exception as e:                      # one broken project must not stop the others
            failed.append({"name": rel, "error": f"{e.__class__.__name__}: {e}"[:200]})
            log(f"[{i}/{len(dirs)}] {rel}: failed ({e.__class__.__name__}: {e})")
    title = root.name or str(root)
    fl = diagram(summaries)
    if fl:
        (out / "workspace.mmd").write_text(fl.render(), encoding="utf-8", newline="\n")
    (out / "README.md").write_text(index_md(title, summaries, failed, loose, date, "README.md"), encoding="utf-8", newline="\n")
    (out / "index.html").write_text(index_html(title, index_md(title, summaries, failed, loose, date, "index.html"), date),
                                    encoding="utf-8", newline="\n")
    llms = [f"# {title}", "", f"> {len(summaries)} project(s) in one folder, each with its own handoff pack, wiki and ontology. "
            f"Generated by HandOff247 {__version__} on {date}.", "", "## Projects", ""]
    llms += [f"- [{x['name']}]({x['pack']}/llms.txt): {x['description'] or 'no description yet'}" for x in summaries]
    llms += ["", "## Index", "", "- [README.md](README.md): what would be lost, all projects, how they point at each other", ""]
    (out / "llms.txt").write_text("\n".join(llms), encoding="utf-8", newline="\n")
    data = {"generator": "HandOff247", "kind": "workspace", "version": __version__, "generated": date,
            "projects": summaries, "failed": failed, "unrecognised": loose}
    (out / "workspace.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    return data
