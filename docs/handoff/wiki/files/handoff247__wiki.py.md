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
- **Lines:** 456
- **Source:** [handoff247/wiki.py](../../../../handoff247/wiki.py)

**Notes from the previous owner**

> Writes the ontology as Markdown pages plus `llms.txt` and `llms-full.txt`. `assign_pages` decides which page describes an entity (own page for files, areas, modes, operations and MCP tools; a list page for the small classes; a type lives on its file's page). File names are slugs with `/` as `__`; Windows reserved names get a `_` prefix. The pages are regenerated on every run, so durable knowledge belongs in the notes file; `agents()` is the page that tells an assistant so.

**defines** →

- `Wiki` · [handoff247/wiki.py:95](../../../../handoff247/wiki.py#L95)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/wiki.py:28](../../../../handoff247/wiki.py#L28)
- [`handoff247/explore.py`](handoff247__explore.py.md) · [handoff247/wiki.py:32](../../../../handoff247/wiki.py#L32)
- [`handoff247/labels.py`](handoff247__labels.py.md) · [handoff247/wiki.py:29](../../../../handoff247/wiki.py#L29)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/wiki.py:30](../../../../handoff247/wiki.py#L30)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/wiki.py:33](../../../../handoff247/wiki.py#L33)
- [`handoff247/render_users.py`](handoff247__render_users.py.md) · [handoff247/wiki.py:31](../../../../handoff247/wiki.py#L31)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/wiki.py:266](../../../../handoff247/wiki.py#L266)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)

## Comment in the file

The LLM wiki: the ontology written out as small, interlinked Markdown pages that an AI assistant (or a person) can read one at a time. *(module docstring)*

## Defined here

- `assign_pages` — function, [line 65](../../../../handoff247/wiki.py#L65) — Give every entity the pack-relative path of the wiki page that describes it.
- `Wiki` — class, [line 95](../../../../handoff247/wiki.py#L95)
- `Wiki.ctx` — method, [line 114](../../../../handoff247/wiki.py#L114) — The user-context sections, with links that work from ``page``.
- `Wiki.href` — method, [line 120](../../../../handoff247/wiki.py#L120)
- `Wiki.ref` — method, [line 123](../../../../handoff247/wiki.py#L123)
- `Wiki.src` — method, [line 130](../../../../handoff247/wiki.py#L130)
- `Wiki.front` — method, [line 133](../../../../handoff247/wiki.py#L133)
- `Wiki.note` — method, [line 142](../../../../handoff247/wiki.py#L142)
- `Wiki.relations` — method, [line 148](../../../../handoff247/wiki.py#L148)
- `Wiki.body` — method, [line 172](../../../../handoff247/wiki.py#L172) — Summary, attributes, the owner's note and the relations of one entity.
- `Wiki.entity_page` — method, [line 196](../../../../handoff247/wiki.py#L196)
- `Wiki.list_page` — method, [line 232](../../../../handoff247/wiki.py#L232)
- `Wiki.overview` — method, [line 253](../../../../handoff247/wiki.py#L253)
- `Wiki.notes_page` — method, [line 291](../../../../handoff247/wiki.py#L291)
- `Wiki.index` — method, [line 300](../../../../handoff247/wiki.py#L300)
- `Wiki.line_summary` — method, [line 350](../../../../handoff247/wiki.py#L350)
- `Wiki.agents` — method, [line 359](../../../../handoff247/wiki.py#L359)
- `Wiki.llms_txt` — method, [line 412](../../../../handoff247/wiki.py#L412)
- `Wiki.render` — method, [line 438](../../../../handoff247/wiki.py#L438) — Pack-relative path → text for every wiki file, llms.txt and llms-full.txt included.
