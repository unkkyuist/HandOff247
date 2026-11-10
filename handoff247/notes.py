"""The human half of a handoff: a Markdown notes file with one heading per item.

Headings are matched by name: ``## Project``, ``## Topic: …``, ``## Mode: serve``,
``## Area: scripts``, ``## File: path/to/file.cs``, ``## Op: list``, plus ``## Translations``
(a two-column table, original → English). Updating the skeleton only appends missing
headings and missing table rows; existing text is never rewritten or removed.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from . import translate
from .connect import area_of
from .labels import t
from .model import Project

DEFAULT_NAME = "HANDOFF.notes.md"
TRANSLATIONS = "Translations"
HEADING = re.compile(r"^##\s+(.+?)\s*$")
CELL_SPLIT = re.compile(r"(?<!\\)\|")
SEPARATOR = re.compile(r":?-{2,}:?")
CHECKLIST_NAMES = {t("topic_checklist")}
RISK_NAMES = {t("topic_risks")}
SECRET_NAMES = {t("topic_secrets")}
# (label key, TODO prompt key): the questions only the person leaving can answer
TOPICS = [("topic_checklist", "todo_checklist"), ("topic_risks", "todo_risks"), ("topic_secrets", "todo_secrets"),
          ("topic_open", "todo_open"), ("topic_deploy", "todo_deploy"), ("topic_routine", "todo_routine"),
          ("topic_data", "todo_data"), ("topic_people", "todo_people")]


@dataclass
class Notes:
    path: Path | None = None
    preamble: str = ""
    order: list[str] = field(default_factory=list)
    body: dict[str, str] = field(default_factory=dict)

    def get(self, key: str) -> str:
        """Filled text for a heading, or '' when missing / still TODO."""
        text = self.body.get(key, "")
        return text.strip() if is_filled(text) else ""

    def topic(self, names: set[str]) -> str:
        for n in names:
            v = self.get(f"Topic: {n}")
            if v:
                return v
        return ""

    def translation_rows(self) -> list[tuple[str, str]]:
        """Every (original, english) row of the Translations table, TODO rows included."""
        rows = []
        for line in self.body.get(TRANSLATIONS, "").split("\n"):
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip().replace("\\|", "|") for c in CELL_SPLIT.split(s[1:-1] if s.endswith("|") else s[1:])]
            if len(cells) != 2 or SEPARATOR.fullmatch(cells[0]) or (cells[0], cells[1]) == ("Original", "English"):
                continue
            rows.append((cells[0], cells[1]))
        return rows

    def translations(self) -> dict[str, str]:
        """Original → English for the rows that have been filled in."""
        return {o: e for o, e in self.translation_rows() if o and e and not e.upper().startswith("TODO")}

    def stale(self, project: Project) -> list[str]:
        paths = {f.path for f in project.files}
        areas = {area_of(f.path) for f in project.files}
        modes = {m["name"] for m in project.links.get("modes", [])}
        ops = {o["key"] for tb in project.links.get("tables", []) for o in tb["ops"]}
        out = []
        for k in self.order:
            kind, _, name = k.partition(": ")
            if (kind == "File" and name not in paths) or (kind == "Area" and name not in areas) or \
               (kind == "Mode" and name not in modes) or (kind == "Op" and name not in ops):
                out.append(k)
        return out


def is_filled(text: str) -> bool:
    cleaned = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for line in cleaned.split("\n"):
        s = line.strip()
        if s and not s.upper().startswith("TODO"):
            return True
    return False


def parse(text: str, path: Path | None = None) -> Notes:
    notes = Notes(path=path)
    current = None
    buf: list[str] = []
    pre: list[str] = []
    for line in text.replace("\r\n", "\n").split("\n"):
        m = HEADING.match(line)
        if m:
            if current is not None:
                notes.body[current] = "\n".join(buf).strip("\n")
            current = m.group(1).strip()
            if current not in notes.body:
                notes.order.append(current)
            buf = []
            continue
        if current is None:
            pre.append(line)
        else:
            buf.append(line)
    if current is not None:
        notes.body[current] = "\n".join(buf).strip("\n")
    notes.preamble = "\n".join(pre).strip("\n")
    return notes


def load(path: Path | None) -> Notes:
    if path and path.is_file():
        return parse(path.read_text(encoding="utf-8-sig"), path)
    return Notes(path=path)


def _row(original: str) -> str:
    return "| " + original.replace("|", "\\|") + " | TODO |"


def translation_skeleton(project: Project) -> str:
    rows = [_row(x) for x in translate.texts(project)]
    if not rows:
        return ""
    return "\n".join([f"<!-- {t('translations_hint')} -->", "| Original | English |", "|---|---|", *rows])


def skeleton(project: Project, max_files: int = 400) -> list[tuple[str, str]]:
    items = [("Project", t("todo_project"))] + [(f"Topic: {t(k)}", t(todo)) for k, todo in TOPICS]
    seen = set()
    for m in project.links.get("modes", []):
        if m["name"] not in seen:
            seen.add(m["name"])
            items.append((f"Mode: {m['name']}", t("todo_mode")))
    for a in sorted({area_of(f.path) for f in project.files} - {"(root)"}):
        items.append((f"Area: {a}", t("todo_area")))
    n = 0
    for f in project.files:
        if f.category in ("code", "script", "test", "web") and "vendored" not in f.tags and not f.skipped:
            items.append((f"File: {f.path}", t("todo_file")))
            n += 1
            if n >= max_files:
                break
    tr = translation_skeleton(project)
    if tr:
        items.append((TRANSLATIONS, tr))
    return items


def render_new(project: Project) -> str:
    lines = [f"# HandOff247 notes · {project.name}", "", "<!--", t("notes_preamble"), "-->", ""]
    for key, body in skeleton(project):
        lines += [f"## {key}", body, ""]
    return "\n".join(lines)


def _add_translation_rows(text: str, notes: Notes, project: Project) -> tuple[str, int]:
    """Insert rows for new foreign text after the last row of an existing Translations table."""
    have = {translate.norm(o) for o, _ in notes.translation_rows()}
    new = [x for x in translate.texts(project) if x not in have]
    if not new:
        return text, 0
    lines = text.split("\n")
    start = next(i for i, l in enumerate(lines) if (m := HEADING.match(l)) and m.group(1).strip() == TRANSLATIONS)
    end = next((i for i in range(start + 1, len(lines)) if HEADING.match(lines[i])), len(lines))
    rows = [i for i in range(start + 1, end) if lines[i].strip().startswith("|")]
    if rows:
        at, insert = rows[-1] + 1, [_row(x) for x in new]
    else:
        at = start + 1
        insert = ["| Original | English |", "|---|---|", *[_row(x) for x in new]]
    return "\n".join(lines[:at] + insert + lines[at:]), len(new)


def update(path: Path, project: Project) -> tuple[int, int, int]:
    """Create the notes file or append headings (and translation rows) that are missing.
    Returns (headings added, translation rows added, headings already there)."""
    if not path.exists():
        path.write_text(render_new(project), encoding="utf-8")
        return len(skeleton(project)), len(translate.texts(project)), 0
    text = path.read_text(encoding="utf-8-sig")
    notes = parse(text, path)
    added = 0
    if TRANSLATIONS in notes.body:
        text, added = _add_translation_rows(text, notes, project)
    missing = [(k, b) for k, b in skeleton(project) if k not in notes.body]
    if missing:
        add = ["", "<!-- added by HandOff247 for new items -->"]
        for key, body in missing:
            add += [f"## {key}", body, ""]
        sep = "" if text.endswith("\n") else "\n"
        text = text + sep + "\n".join(add)
    if added or missing:
        path.write_text(text, encoding="utf-8")
    return len(missing), added, len(notes.order)
