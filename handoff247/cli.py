"""Command line: build a pack, create/extend the notes file, check documentation coverage."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__, translate
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


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (OSError, ValueError):
            pass
    ap = argparse.ArgumentParser(prog="handoff247", description="Turn a project folder into a handoff pack: "
                                 "diagrams, structure, comments and how the tools connect.")
    ap.add_argument("--version", action="version", version=f"HandOff247 {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)
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
