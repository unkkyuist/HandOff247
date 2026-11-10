---
generator: HandOff247
id: "file:handoff247/wiki.py"
type: File
source: "handoff247/wiki.py"
---

# `handoff247/wiki.py`

> Writes the ontology as Markdown pages plus `llms.txt` and `llms-full.txt`. `assign_pages` decides which page describes an entity (own page for files, areas, modes, operations and MCP tools; a list page for the small cla…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 391
- **Source:** [handoff247/wiki.py](../../../../handoff247/wiki.py)

**Notes from the previous owner**

> Writes the ontology as Markdown pages plus `llms.txt` and `llms-full.txt`. `assign_pages` decides which page describes an entity (own page for files, areas, modes, operations and MCP tools; a list page for the small classes; a type lives on its file's page). File names are slugs with `/` as `__`; Windows reserved names get a `_` prefix. The pages are regenerated on every run, so durable knowledge belongs in the notes file; `agents()` is the page that tells an assistant so.

**defines** →

- `Wiki` · [handoff247/wiki.py:88](../../../../handoff247/wiki.py#L88)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/wiki.py:26](../../../../handoff247/wiki.py#L26)
- [`handoff247/labels.py`](handoff247__labels.py.md) · [handoff247/wiki.py:27](../../../../handoff247/wiki.py#L27)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/wiki.py:28](../../../../handoff247/wiki.py#L28)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/wiki.py:29](../../../../handoff247/wiki.py#L29)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/wiki.py:225](../../../../handoff247/wiki.py#L225)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)

## Comment in the file

The LLM wiki: the ontology written out as small, interlinked Markdown pages that an AI assistant (or a person) can read one at a time. *(module docstring)*

## Defined here

- `assign_pages` — function, [line 58](../../../../handoff247/wiki.py#L58) — Give every entity the pack-relative path of the wiki page that describes it.
- `Wiki` — class, [line 88](../../../../handoff247/wiki.py#L88)
- `Wiki.href` — method, [line 106](../../../../handoff247/wiki.py#L106)
- `Wiki.ref` — method, [line 109](../../../../handoff247/wiki.py#L109)
- `Wiki.src` — method, [line 116](../../../../handoff247/wiki.py#L116)
- `Wiki.front` — method, [line 119](../../../../handoff247/wiki.py#L119)
- `Wiki.note` — method, [line 128](../../../../handoff247/wiki.py#L128)
- `Wiki.relations` — method, [line 134](../../../../handoff247/wiki.py#L134)
- `Wiki.body` — method, [line 158](../../../../handoff247/wiki.py#L158) — Summary, attributes, the owner's note and the relations of one entity.
- `Wiki.entity_page` — method, [line 182](../../../../handoff247/wiki.py#L182)
- `Wiki.list_page` — method, [line 202](../../../../handoff247/wiki.py#L202)
- `Wiki.overview` — method, [line 212](../../../../handoff247/wiki.py#L212)
- `Wiki.notes_page` — method, [line 250](../../../../handoff247/wiki.py#L250)
- `Wiki.index` — method, [line 259](../../../../handoff247/wiki.py#L259)
- `Wiki.line_summary` — method, [line 303](../../../../handoff247/wiki.py#L303)
- `Wiki.agents` — method, [line 312](../../../../handoff247/wiki.py#L312)
- `Wiki.llms_txt` — method, [line 348](../../../../handoff247/wiki.py#L348)
- `Wiki.render` — method, [line 373](../../../../handoff247/wiki.py#L373) — Pack-relative path → text for every wiki file, llms.txt and llms-full.txt included.
