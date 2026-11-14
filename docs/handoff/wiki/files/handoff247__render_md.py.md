---
generator: HandOff247
id: "file:handoff247/render_md.py"
type: File
source: "handoff247/render_md.py"
---

# `handoff247/render_md.py`

> The Markdown pages except USERS.md (render_users.py writes that one); `handover()` puts each of the leaver's answers next to what `leaving.py` found. `Linker` decides how file:line references are linked: relative when t…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 663
- **Source:** [handoff247/render_md.py](../../../../handoff247/render_md.py)

**Notes from the previous owner**

> The Markdown pages except USERS.md (render_users.py writes that one); `handover()` puts each of the leaver's answers next to what `leaving.py` found. `Linker` decides how file:line references are linked: relative when the pack is inside the project, GitHub blob URLs at the exact commit when it is outside, plain text otherwise.

**defines** →

- `Linker` · [handoff247/render_md.py:19](../../../../handoff247/render_md.py#L19)
- `Pages` · [handoff247/render_md.py:67](../../../../handoff247/render_md.py#L67)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/render_md.py:7](../../../../handoff247/render_md.py#L7)
- [`handoff247/connect.py`](handoff247__connect.py.md) · [handoff247/render_md.py:8](../../../../handoff247/render_md.py#L8)
- [`handoff247/labels.py`](handoff247__labels.py.md) · [handoff247/render_md.py:9](../../../../handoff247/render_md.py#L9)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/render_md.py:7](../../../../handoff247/render_md.py#L7)
- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/render_md.py:10](../../../../handoff247/render_md.py#L10)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/render_md.py:11](../../../../handoff247/render_md.py#L11)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/render_md.py:12](../../../../handoff247/render_md.py#L12)
- [`handoff247/render_users.py`](handoff247__render_users.py.md) · [handoff247/render_md.py:249](../../../../handoff247/render_md.py#L249)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/render_md.py:111](../../../../handoff247/render_md.py#L111)

**mentions** →

- [`github.com`](../hosts.md) · [handoff247/render_md.py:647](../../../../handoff247/render_md.py#L647)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:14](../../../../handoff247/build.py#L14)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:262](../../../../handoff247/cli.py#L262)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:302](../../../../handoff247/mcp.py#L302)
- [`handoff247/render_users.py`](handoff247__render_users.py.md) · [handoff247/render_users.py:384](../../../../handoff247/render_users.py#L384)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/wiki.py:33](../../../../handoff247/wiki.py#L33)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:24](../../../../handoff247/workspace.py#L24)

## Comment in the file

Markdown pages of the handoff pack. *(module docstring)*

## Defined here

- `Linker` — class, [line 19](../../../../handoff247/render_md.py#L19) — Turns file:line into a link.
- `cell` — function, [line 35](../../../../handoff247/render_md.py#L35)
- `table` — function, [line 39](../../../../handoff247/render_md.py#L39)
- `mermaid_block` — function, [line 48](../../../../handoff247/render_md.py#L48)
- `note_block` — function, [line 54](../../../../handoff247/render_md.py#L54)
- `more` — function, [line 61](../../../../handoff247/render_md.py#L61)
- `Pages` — class, [line 67](../../../../handoff247/render_md.py#L67)
- `Pages.header` — method, [line 83](../../../../handoff247/render_md.py#L83)
- `Pages.L` — method, [line 97](../../../../handoff247/render_md.py#L97)
- `Pages.importance` — method, [line 100](../../../../handoff247/render_md.py#L100) — Files a successor should open first, with the reason (all derived from facts).
- `Pages.undocumented` — method, [line 143](../../../../handoff247/render_md.py#L143)
- `Pages.readme` — method, [line 154](../../../../handoff247/render_md.py#L154)
- `Pages.users` — method, [line 248](../../../../handoff247/render_md.py#L248)
- `Pages.ready` — method, [line 253](../../../../handoff247/render_md.py#L253)
- `Pages.where` — method, [line 258](../../../../handoff247/render_md.py#L258)
- `Pages.topic` — method, [line 261](../../../../handoff247/render_md.py#L261)
- `Pages.handover` — method, [line 265](../../../../handoff247/render_md.py#L265)
- `Pages.running` — method, [line 393](../../../../handoff247/render_md.py#L393)
- `Pages.connections` — method, [line 469](../../../../handoff247/render_md.py#L469)
- `Pages.codemap` — method, [line 531](../../../../handoff247/render_md.py#L531)
- `Pages.file_cards` — method, [line 566](../../../../handoff247/render_md.py#L566)
- `make_linker` — function, [line 635](../../../../handoff247/render_md.py#L635)
