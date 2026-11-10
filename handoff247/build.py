"""Write the handoff pack to disk."""
from __future__ import annotations

import datetime
import json
from dataclasses import asdict
from pathlib import Path

from . import __version__, ontology, translate, wiki
from .mermaid import all_diagrams
from .model import Project
from .notes import TRANSLATIONS, Notes
from .render_html import render as render_html
from .render_md import Pages, make_linker

PAGE_FILES = ("README.md", "HANDOVER.md", "RUNNING.md", "CONNECTIONS.md", "CODEMAP.md", "FILES.md")


def to_json(project: Project, notes: Notes, date: str) -> dict:
    git = {k: v for k, v in project.git.items()}
    return {
        "generator": "HandOff247",
        "version": __version__,
        "generated": date,
        "project": {"name": project.name, "git": git},
        "notes": {k: notes.body[k] for k in notes.order if k != TRANSLATIONS and notes.get(k)},
        "files": [f.to_json() for f in project.files],
        "edges": [asdict(e) for e in project.edges],
        "links": project.links,
    }


def write_pack(project: Project, out_dir: Path, notes: Notes, links: str = "auto", link_base: str = "",
               date: str | None = None, notes_label: str = "HANDOFF.notes.md") -> dict:
    """Render every page. Text with an English version in the notes' Translations table is
    replaced in ``project`` first, so all pages, diagrams and the viewer show the same words."""
    date = date or datetime.date.today().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)
    tr = translate.apply(project, notes.translations())
    diagrams = all_diagrams(project)
    linker = make_linker(links, project, out_dir, link_base)
    pages = Pages(project, diagrams, notes, linker, notes_label, date)
    project.links["readiness"] = pages.ready()
    content = {"README.md": pages.readme(), "HANDOVER.md": pages.handover(), "RUNNING.md": pages.running(),
               "CONNECTIONS.md": pages.connections(), "CODEMAP.md": pages.codemap(), "FILES.md": pages.file_cards()}
    for name, text in content.items():
        (out_dir / name).write_text(text, encoding="utf-8", newline="\n")
    ddir = out_dir / "diagrams"
    ddir.mkdir(exist_ok=True)
    for old in ddir.glob("*.mmd"):
        if old.stem not in diagrams:
            old.unlink()
    for name, fl in diagrams.items():
        (ddir / f"{name}.mmd").write_text(fl.render(), encoding="utf-8", newline="\n")
    data = to_json(project, notes, date)
    (out_dir / "handoff.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    onto = ontology.build(project, notes)
    wiki.assign_pages(onto)
    (out_dir / "ontology.json").write_text(json.dumps({**onto, "generated": date}, ensure_ascii=False, indent=1),
                                           encoding="utf-8", newline="\n")
    wiki_pages = wiki.Wiki(project, onto, notes, linker, notes_label, date).render()
    write_wiki(out_dir, wiki_pages)
    embedded = {**content, **{k: v for k, v in wiki_pages.items() if k.startswith("wiki/")}}
    (out_dir / "index.html").write_text(render_html(project, embedded, diagrams, notes, date, linker, onto),
                                        encoding="utf-8", newline="\n")
    return {"out": str(out_dir), "pages": list(content), "diagrams": list(diagrams), "files": len(project.files),
            "edges": len(project.edges), "links": linker.mode, "readiness": project.links["readiness"],
            "gaps": pages.undocumented(), "entities": len(onto["entities"]), "relations": len(onto["relations"]),
            "wiki_pages": sum(1 for k in wiki_pages if k.startswith("wiki/")), **tr}


def write_wiki(out_dir: Path, pages: dict[str, str]) -> None:
    """Write the wiki and remove pages of an earlier run that no longer exist. Only files that
    carry the generator mark are removed, so a page a person added by hand stays."""
    wanted = set()
    for rel, text in pages.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        wanted.add(path.resolve())
    root = out_dir / "wiki"
    for old in root.rglob("*.md"):
        if old.resolve() in wanted:
            continue
        try:
            with old.open(encoding="utf-8", errors="replace") as fh:
                head = fh.read(200)
        except OSError:
            continue
        if head.startswith("---\n" + wiki.MARK):
            old.unlink()
