---
generator: HandOff247
id: "file:handoff247/translate.py"
type: File
source: "handoff247/translate.py"
---

# `handoff247/translate.py`

> Finds extracted prose with letters outside the Latin script (summaries, doc comments, Markdown headings, MCP tool descriptions, sub-command help, commit subjects) and swaps in the English from the notes' Translations ta…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 93
- **Source:** [handoff247/translate.py](../../../../handoff247/translate.py)

**Notes from the previous owner**

> Finds extracted prose with letters outside the Latin script (summaries, doc comments, Markdown headings, MCP tool descriptions, sub-command help, commit subjects) and swaps in the English from the notes' Translations table. Matching is exact apart from spacing, so a comment that changed later shows its original again instead of a stale translation. Identifiers such as file names are never touched.

**imports** →

- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/translate.py:15](../../../../handoff247/translate.py#L15)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/notes.py:14](../../../../handoff247/notes.py#L14)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:533](../../../../tests/test_handoff.py#L533)

## Comment in the file

English for project text that was written in another language. *(module docstring)*

## Defined here

- `norm` — function, [line 20](../../../../handoff247/translate.py#L20)
- `foreign` — function, [line 24](../../../../handoff247/translate.py#L24) — True when the text has letters outside the Latin script (Hangul, kana, CJK, Cyrillic, Greek, …).
- `texts` — function, [line 64](../../../../handoff247/translate.py#L64) — Extracted text in another language, normalised, in first-seen order.
- `apply` — function, [line 74](../../../../handoff247/translate.py#L74) — Replace text that has an English version.
