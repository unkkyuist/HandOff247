---
generator: HandOff247
id: "file:handoff247/build.py"
type: File
source: "handoff247/build.py"
---

# `handoff247/build.py`

> Writes the pack: six Markdown pages, `diagrams/*.mmd`, `handoff.json` (its first key `"generator": "HandOff247"` is how later runs recognise and skip an old pack), `ontology.json`, the wiki and `index.html`. `write_wiki…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 91
- **Source:** [handoff247/build.py](../../../../handoff247/build.py)

**Notes from the previous owner**

> Writes the pack: six Markdown pages, `diagrams/*.mmd`, `handoff.json` (its first key `"generator": "HandOff247"` is how later runs recognise and skip an old pack), `ontology.json`, the wiki and `index.html`. `write_wiki` deletes wiki pages of an earlier run that no longer exist, but only files that start with the generator mark, so a page someone added by hand stays.

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)
- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/build.py:10](../../../../handoff247/build.py#L10)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/build.py:11](../../../../handoff247/build.py#L11)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/build.py:12](../../../../handoff247/build.py#L12)
- [`handoff247/ontology.py`](handoff247__ontology.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)
- [`handoff247/render_html.py`](handoff247__render_html.py.md) · [handoff247/build.py:13](../../../../handoff247/build.py#L13)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/build.py:14](../../../../handoff247/build.py#L14)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)

**refers to** →

- [`HANDOFF.notes.md`](HANDOFF.notes.md.md) · [handoff247/build.py:34](../../../../handoff247/build.py#L34)
- [`README.md`](README.md.md) · [handoff247/build.py:16](../../../../handoff247/build.py#L16)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:10](../../../../handoff247/cli.py#L10)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:18](../../../../handoff247/workspace.py#L18)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:16](../../../../tests/test_handoff.py#L16)

## Comment in the file

Write the handoff pack to disk. *(module docstring)*

## Defined here

- `to_json` — function, [line 19](../../../../handoff247/build.py#L19)
- `write_pack` — function, [line 33](../../../../handoff247/build.py#L33) — Render every page.
- `write_wiki` — function, [line 72](../../../../handoff247/build.py#L72) — Write the wiki and remove pages of an earlier run that no longer exist.
