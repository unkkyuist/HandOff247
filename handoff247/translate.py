"""English for project text that was written in another language.

HandOff247 quotes a project's comments and headings exactly as written. When they are in
another language, a person (or an assistant) writes the English under ``## Translations`` in
the notes file, one table row per original. The pack then shows the English, marks it as
translated and keeps the original in handoff.json. An original only matches when it is the
same text (spacing aside), so a comment that changed later falls back to the original instead
of showing a translation of something the code no longer says.
"""
from __future__ import annotations

import unicodedata
from typing import Any, Iterator

from .model import FileInfo, Project

HEADING_KINDS = ("h1", "h2", "h3")


def norm(text: str) -> str:
    return " ".join(text.split())


def foreign(text: str) -> bool:
    """True when the text has letters outside the Latin script (Hangul, kana, CJK, Cyrillic, Greek, …).
    Accented Latin letters such as é or ß do not count."""
    for ch in text:
        if ch.isalpha() and not ch.isascii() and "LATIN" not in unicodedata.name(ch, ""):
            return True
    return False


def _fields(project: Project) -> Iterator[tuple[FileInfo | None, str, Any, str]]:
    """Every piece of extracted prose the pack shows: (file, where, object, attribute or key).
    Identifiers (file names, symbol names in code) are never included: they must stay exact."""
    files = {f.path: f for f in project.files}
    for f in project.files:
        yield f, "summary", f, "summary"
        for s in f.symbols:
            if not s.public:
                continue
            if s.kind in HEADING_KINDS:
                yield f, f"heading L{s.line}", s, "name"
            yield f, f"doc comment L{s.line}", s, "doc"
    for x in project.links.get("mcp_tools", []):
        yield files.get(x["file"]), f"MCP tool {x['name']}", x, "description"
    for c in project.links.get("subcommands", []):
        yield files.get(c["file"]), f"sub-command {c['name']}", c, "help"
    for c in project.git.get("commits", []):
        yield None, f"commit {c['sha']}", c, "subject"


def _get(obj: Any, attr: str) -> str:
    return (obj.get(attr) if isinstance(obj, dict) else getattr(obj, attr, "")) or ""


def _set(obj: Any, attr: str, value: str) -> None:
    if isinstance(obj, dict):
        obj[attr] = value
    else:
        setattr(obj, attr, value)


def texts(project: Project) -> list[str]:
    """Extracted text in another language, normalised, in first-seen order."""
    seen: dict[str, None] = {}
    for _, _, obj, attr in _fields(project):
        v = _get(obj, attr)
        if v and foreign(v):
            seen.setdefault(norm(v), None)
    return list(seen)


def apply(project: Project, table: dict[str, str]) -> dict[str, Any]:
    """Replace text that has an English version. Changes the project in place and records what
    was replaced in ``project.links['translations']`` and on each file (``FileInfo.translated``)."""
    table = {norm(k): v.strip() for k, v in table.items() if k.strip() and v.strip()}
    uses: dict[str, int] = {}
    for f, where, obj, attr in _fields(project):
        v = _get(obj, attr)
        key = norm(v)
        if not v or key not in table:
            continue
        _set(obj, attr, table[key])
        uses[key] = uses.get(key, 0) + 1
        if f is not None:
            f.translated.append({"where": where, "original": v})
            if obj is f and attr == "summary":
                f.summary_source = f"{f.summary_source}, translated" if f.summary_source else "translated"
    rows = [{"original": k, "english": table[k], "uses": n} for k, n in uses.items()]
    project.links["translations"] = rows
    project.links["untranslated"] = texts(project)
    return {"applied": len(rows), "unused": len(table) - len(rows), "untranslated": len(project.links["untranslated"])}
