"""The human half of a handoff: a Markdown notes file with one heading per item.

Headings are matched by name: ``## Project``, ``## Topic: …``, ``## Mode: serve``,
``## Area: scripts``, ``## File: path/to/file.cs``, ``## Op: list``. Updating the skeleton
only appends missing headings; existing text is never rewritten or removed.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .connect import area_of
from .i18n import STRINGS, T
from .model import Project

DEFAULT_NAME = "HANDOFF.notes.md"
HEADING = re.compile(r"^##\s+(.+?)\s*$")
CHECKLIST_NAMES = set(STRINGS["topic_checklist"])
RISK_NAMES = set(STRINGS["topic_risks"])
SECRET_NAMES = set(STRINGS["topic_secrets"])


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

    def stale(self, project: Project) -> list[str]:
        paths = {f.path for f in project.files}
        areas = {area_of(f.path) for f in project.files}
        modes = {m["name"] for m in project.links.get("modes", [])}
        ops = {o["key"] for t in project.links.get("tables", []) for o in t["ops"]}
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


def skeleton(project: Project, lang: str, max_files: int = 400) -> list[tuple[str, str]]:
    t = T(lang)
    items = [("Project", t("todo_project")),
             (f"Topic: {t('topic_checklist')}", t("todo_checklist")),
             (f"Topic: {t('topic_risks')}", t("todo_risks")),
             (f"Topic: {t('topic_secrets')}", t("todo_secrets"))]
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
    return items


def render_new(project: Project, lang: str) -> str:
    t = T(lang)
    lines = [f"# HandOff247 notes · {project.name}", "", "<!--", t("notes_preamble"), "-->", ""]
    for key, body in skeleton(project, lang):
        lines += [f"## {key}", body, ""]
    return "\n".join(lines)


def update(path: Path, project: Project, lang: str) -> tuple[int, int]:
    """Create the notes file or append headings that are missing. Returns (added, existing)."""
    if not path.exists():
        path.write_text(render_new(project, lang), encoding="utf-8")
        return len(skeleton(project, lang)), 0
    text = path.read_text(encoding="utf-8-sig")
    notes = parse(text, path)
    missing = [(k, b) for k, b in skeleton(project, lang) if k not in notes.body]
    if missing:
        add = ["", f"<!-- added by HandOff247 for new items -->"]
        for key, body in missing:
            add += [f"## {key}", body, ""]
        sep = "" if text.endswith("\n") else "\n"
        path.write_text(text + sep + "\n".join(add), encoding="utf-8")
    return len(missing), len(notes.order)
