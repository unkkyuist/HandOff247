---
generator: HandOff247
id: "file:handoff247/render_md.py"
type: File
source: "handoff247/render_md.py"
---

# `handoff247/render_md.py`

> The six Markdown pages; `handover()` puts each of the leaver's answers next to what `leaving.py` found. `Linker` decides how file:line references are linked: relative when the pack is inside the project, GitHub blob URL…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 654
- **Source:** [handoff247/render_md.py](../../../../handoff247/render_md.py)

**Notes from the previous owner**

> The six Markdown pages; `handover()` puts each of the leaver's answers next to what `leaving.py` found. `Linker` decides how file:line references are linked: relative when the pack is inside the project, GitHub blob URLs at the exact commit when it is outside, plain text otherwise.

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

**refers to** →

- [`README.md`](README.md.md) · [handoff247/render_md.py:110](../../../../handoff247/render_md.py#L110)

**mentions** →

- [`github.com`](../hosts.md) · [handoff247/render_md.py:638](../../../../handoff247/render_md.py#L638)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:14](../../../../handoff247/build.py#L14)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:205](../../../../handoff247/cli.py#L205)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:131](../../../../handoff247/mcp.py#L131)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/wiki.py:29](../../../../handoff247/wiki.py#L29)
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
- `Pages.header` — method, [line 82](../../../../handoff247/render_md.py#L82)
- `Pages.L` — method, [line 96](../../../../handoff247/render_md.py#L96)
- `Pages.importance` — method, [line 99](../../../../handoff247/render_md.py#L99) — Files a successor should open first, with the reason (all derived from facts).
- `Pages.undocumented` — method, [line 142](../../../../handoff247/render_md.py#L142)
- `Pages.readme` — method, [line 153](../../../../handoff247/render_md.py#L153)
- `Pages.ready` — method, [line 244](../../../../handoff247/render_md.py#L244)
- `Pages.where` — method, [line 249](../../../../handoff247/render_md.py#L249)
- `Pages.topic` — method, [line 252](../../../../handoff247/render_md.py#L252)
- `Pages.handover` — method, [line 256](../../../../handoff247/render_md.py#L256)
- `Pages.running` — method, [line 384](../../../../handoff247/render_md.py#L384)
- `Pages.connections` — method, [line 460](../../../../handoff247/render_md.py#L460)
- `Pages.codemap` — method, [line 522](../../../../handoff247/render_md.py#L522)
- `Pages.file_cards` — method, [line 557](../../../../handoff247/render_md.py#L557)
- `make_linker` — function, [line 626](../../../../handoff247/render_md.py#L626)
