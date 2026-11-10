"""Command line: build a pack, create/extend the notes file, check documentation coverage."""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

from . import __version__, leaving, translate, workspace
from .build import write_pack
from .notes import DEFAULT_NAME, load, skeleton, update
from .pipeline import analyze_project


def _common(p: argparse.ArgumentParser) -> None:
    p.add_argument("project", nargs="?", default=".", help="project folder to analyze (default: current folder)")
    p.add_argument("--name", help="project name shown in the pack (default: folder name)")
    p.add_argument("--notes", help=f"notes file (default: <project>/{DEFAULT_NAME})")
    p.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                   help="skip matching paths (repeatable; also read from <project>/.handoffignore)")


def _notes_path(args) -> Path:
    return Path(args.notes) if args.notes else Path(args.project) / DEFAULT_NAME


COMMANDS = ("go", "build", "notes", "check")


def _print_readiness(rows: list[dict]) -> None:
    ok, total = leaving.score(rows)
    print(f"handover checklist: {ok} of {total} ready")
    for r in rows:
        mark = {"ok": "[x]", "todo": "[ ]", "na": "[-]"}[r["state"]]
        print(f"  {mark} {r['label']}" + (f" ({r['detail']})" if r["detail"] and r["state"] != "ok" else ""))


def _go(args) -> int:
    """One step for a person about to leave: notes file, pack, and what is still open."""
    root = Path(args.project)
    if not root.is_dir():
        print(f"error: {root} is not a folder", file=sys.stderr)
        return 2
    date = args.date or datetime.date.today().isoformat()
    ws_out = Path(args.out) if args.out else root / "handoff"
    as_workspace = args.workspace or (not args.single and workspace.is_workspace(root, ws_out))
    if as_workspace:
        data = workspace.build_workspace(root, ws_out, date, args.exclude)
        if not data["projects"] and not data["failed"]:
            print(f"error: no project found under {root} (use --single to treat the folder itself as one)", file=sys.stderr)
            return 2
        warn = [(x["name"], workspace.attention(x)) for x in data["projects"]]
        warn = [(n, a) for n, a in warn if a]
        print(f"\nHandOff247 {__version__}: {len(data['projects'])} project(s) documented"
              + (f", {len(data['failed'])} failed" if data["failed"] else "")
              + (f", {len(data['unrecognised'])} folder(s) not recognised as projects" if data["unrecognised"] else ""))
        if warn:
            print("before the computer goes away:")
            for n, a in warn:
                print(f"  {n}: " + "; ".join(a))
        index = ws_out / "index.html"
        print(f"open {index}")
        print(f"notes to fill: each project's {DEFAULT_NAME}, or {ws_out / 'notes'} for projects that had none; then run this again")
    else:
        project = analyze_project(root, None, args.exclude)
        notes_path = root / DEFAULT_NAME
        added, rows, existing = update(notes_path, project)
        out = Path(args.out) if args.out else root / "docs" / "handoff"
        notes = load(notes_path)
        info = write_pack(project, out, notes, "auto", "", date, DEFAULT_NAME)
        print(f"HandOff247 {__version__}: {info['files']} files, {len(info['diagrams'])} diagrams "
              f"({', '.join(info['diagrams']) or 'none'}), 6 pages")
        print(f"ontology: {info['entities']} things, {info['relations']} relations (ontology.json, Graph tab); "
              f"wiki: {info['wiki_pages']} pages (wiki/, llms.txt)")
        print(f"notes: {notes_path} ({'created' if not existing else f'{added} heading(s) added'})")
        _print_readiness(info["readiness"])
        todo_topics = [k for k, _ in skeleton(project) if k.startswith(("Project", "Topic: ")) and not notes.get(k)]
        if todo_topics:
            print(f"next: answer these in {notes_path.name}, then run this again:")
            for k in todo_topics:
                print(f"  ## {k}")
        if info["untranslated"]:
            print(f"  ## Translations ({info['untranslated']} text(s) need an English version)")
        index = out / "index.html"
        print(f"open {index}")
    if args.open:
        import webbrowser
        webbrowser.open(index.resolve().as_uri())
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (OSError, ValueError):
            pass
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] not in COMMANDS and not argv[0].startswith("-"):
        argv.insert(0, "go")                        # handoff247 <folder> is the one-step form
    ap = argparse.ArgumentParser(prog="handoff247", description="Turn a project folder into a handoff pack: "
                                 "diagrams, structure, comments, how the tools connect, and a handover checklist. "
                                 "`handoff247 <folder>` does everything in one step.")
    ap.add_argument("--version", action="version", version=f"HandOff247 {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)
    go = sub.add_parser("go", help="one step: create or extend the notes file, build the pack, list what is left; "
                        "a folder of projects gets one pack per project plus an index")
    go.add_argument("project", nargs="?", default=".", help="a project folder, or a folder that holds projects")
    go.add_argument("-o", "--out", help="output folder (default: <project>/docs/handoff, or <folder>/handoff for several projects)")
    go.add_argument("--single", action="store_true", help="treat the folder as one project")
    go.add_argument("--workspace", action="store_true", help="treat the folder as a set of projects")
    go.add_argument("--date", help="date printed in the pack (default: today)")
    go.add_argument("--exclude", action="append", default=[], metavar="GLOB", help="skip matching paths (repeatable)")
    go.add_argument("--open", action="store_true", help="open the result in the browser")
    b = sub.add_parser("build", help="analyze the project and write the handoff pack")
    _common(b)
    b.add_argument("-o", "--out", help="output folder (default: ./handoff/<name>)")
    b.add_argument("--links", choices=["auto", "relative", "url", "plain"], default="auto",
                   help="how file:line references link to source (auto: relative inside the project, GitHub blob URL otherwise)")
    b.add_argument("--link-base", default="", help="URL prefix for source links, e.g. https://github.com/me/repo/blob/main/")
    b.add_argument("--date", help="date printed in the pack (default: today); pin it in CI for stable diffs")
    n = sub.add_parser("notes", help="create the notes file or add headings for new files/modes/folders")
    _common(n)
    c = sub.add_parser("check", help="report what is still undocumented; non-zero exit below --min")
    _common(c)
    c.add_argument("--min", type=float, default=0.0, help="minimum share (0-100) of files with notes")
    args = ap.parse_args(argv)
    if args.cmd == "go":
        return _go(args)

    root = Path(args.project)
    if not root.is_dir():
        print(f"error: {root} is not a folder", file=sys.stderr)
        return 2
    project = analyze_project(root, args.name, args.exclude)
    notes_path = _notes_path(args)

    if args.cmd == "build":
        out = Path(args.out) if args.out else Path.cwd() / "handoff" / project.name
        notes = load(notes_path)
        label = notes_path.name if notes_path.parent.resolve() == root.resolve() else notes_path.as_posix()
        info = write_pack(project, out, notes, args.links, args.link_base, args.date, label)
        L = project.links
        print(f"HandOff247 {__version__}: {info['files']} files, {info['edges']} links, "
              f"{len({m['name'] for m in L['modes']})} modes, {sum(len(t['ops']) for t in L['tables'])} operations, "
              f"{len(L['routes'])} routes, {len(L['mcp_tools'])} MCP tools")
        print(f"diagrams: {', '.join(info['diagrams']) or 'none'} · source links: {info['links']}")
        print(f"ontology: {info['entities']} things, {info['relations']} relations · wiki: {info['wiki_pages']} pages")
        if info["applied"] or info["untranslated"] or info["unused"]:
            print(f"translations: {info['applied']} used, {info['untranslated']} text(s) still in another language"
                  + (f", {info['unused']} row(s) no longer match the code" if info["unused"] else ""))
        print(f"wrote {out}{'' if notes_path.exists() else f'  (no notes file yet: run handoff247 notes {args.project})'}")
        return 0
    if args.cmd == "notes":
        added, rows, existing = update(notes_path, project)
        print(f"{notes_path}: {added} heading(s) added, {existing} already there. Existing text was not changed.")
        if rows:
            print(f"{rows} comment(s) or heading(s) in another language listed under ## Translations; fill the English column.")
        stale = load(notes_path).stale(project)
        if stale:
            print("headings for items that no longer exist (kept, review by hand):")
            for s in stale:
                print(f"  ## {s}")
        return 0
    # check
    notes = load(notes_path)
    items = skeleton(project)
    file_items = [k for k, _ in items if k.startswith("File: ")]
    filled = [k for k in file_items if notes.get(k)]
    share = 100.0 * len(filled) / len(file_items) if file_items else 100.0
    print(f"notes: {notes_path} ({'found' if notes_path.exists() else 'missing'})")
    print(f"files with notes: {len(filled)}/{len(file_items)} ({share:.0f}%)")
    for key in ("Project",):
        print(f"{key}: {'ok' if notes.get(key) else 'TODO'}")
    topics = [k for k, _ in items if k.startswith("Topic: ")]
    for k in topics:
        print(f"{k}: {'ok' if notes.get(k) else 'TODO'}")
    foreign = translate.texts(project)
    if foreign:
        have = {translate.norm(o) for o in notes.translations()}
        print(f"translations: {sum(x in have for x in foreign)}/{len(foreign)} texts in another language have an English version")
    from .render_md import Pages, Linker
    pages = Pages(project, {}, notes, Linker("plain"), notes_path.name, "")
    gaps = pages.undocumented()
    project.links.setdefault("untranslated", [x for x in foreign if x not in {translate.norm(o) for o in notes.translations()}])
    _print_readiness(pages.ready())
    if gaps:
        print("most important undocumented files:")
        for g in gaps[:15]:
            print(f"  {g}")
    stale = notes.stale(project)
    if stale:
        print("stale headings:")
        for s in stale:
            print(f"  ## {s}")
    return 1 if share < args.min else 0
