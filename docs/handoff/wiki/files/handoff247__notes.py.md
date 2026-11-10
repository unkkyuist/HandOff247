---
generator: HandOff247
id: "file:handoff247/notes.py"
type: File
source: "handoff247/notes.py"
---

# `handoff247/notes.py`

> Parses and extends the notes file. `update` only appends missing headings and missing Translations rows; it never rewrites existing text. Stale headings (for deleted files) are reported, not removed.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 201
- **Source:** [handoff247/notes.py](../../../../handoff247/notes.py)

**Notes from the previous owner**

> Parses and extends the notes file. `update` only appends missing headings and missing Translations rows; it never rewrites existing text. Stale headings (for deleted files) are reported, not removed.

**defines** →

- `Notes` · [handoff247/notes.py:34](../../../../handoff247/notes.py#L34)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/notes.py:14](../../../../handoff247/notes.py#L14)
- [`handoff247/connect.py`](handoff247__connect.py.md) · [handoff247/notes.py:15](../../../../handoff247/notes.py#L15)
- [`handoff247/labels.py`](handoff247__labels.py.md) · [handoff247/notes.py:16](../../../../handoff247/notes.py#L16)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/notes.py:17](../../../../handoff247/notes.py#L17)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [handoff247/notes.py:14](../../../../handoff247/notes.py#L14)

**refers to** →

- [`HANDOFF.notes.md`](HANDOFF.notes.md.md) · [handoff247/notes.py:19](../../../../handoff247/notes.py#L19)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:12](../../../../handoff247/build.py#L12)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:11](../../../../handoff247/cli.py#L11)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:23](../../../../handoff247/mcp.py#L23)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_md.py:12](../../../../handoff247/render_md.py#L12)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/wiki.py:28](../../../../handoff247/wiki.py#L28)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:21](../../../../handoff247/workspace.py#L21)

## Comment in the file

The human half of a handoff: a Markdown notes file with one heading per item. *(module docstring)*

## Defined here

- `Notes` — class, [line 34](../../../../handoff247/notes.py#L34)
- `Notes.get` — method, [line 40](../../../../handoff247/notes.py#L40) — Filled text for a heading, or '' when missing / still TODO.
- `Notes.topic` — method, [line 45](../../../../handoff247/notes.py#L45)
- `Notes.translation_rows` — method, [line 52](../../../../handoff247/notes.py#L52) — Every (original, english) row of the Translations table, TODO rows included.
- `Notes.translations` — method, [line 65](../../../../handoff247/notes.py#L65) — Original → English for the rows that have been filled in.
- `Notes.stale` — method, [line 69](../../../../handoff247/notes.py#L69)
- `is_filled` — function, [line 83](../../../../handoff247/notes.py#L83)
- `parse` — function, [line 92](../../../../handoff247/notes.py#L92)
- `load` — function, [line 117](../../../../handoff247/notes.py#L117)
- `translation_skeleton` — function, [line 127](../../../../handoff247/notes.py#L127)
- `skeleton` — function, [line 134](../../../../handoff247/notes.py#L134)
- `render_new` — function, [line 156](../../../../handoff247/notes.py#L156)
- `update` — function, [line 181](../../../../handoff247/notes.py#L181) — Create the notes file or append headings (and translation rows) that are missing.
