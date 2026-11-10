---
generator: HandOff247
id: "file:handoff247/mermaid.py"
type: File
source: "handoff247/mermaid.py"
---

# `handoff247/mermaid.py`

> Builds the five diagrams. `system` collapses launch scripts into one node when there are more than three; `code` hides incoming arrows of shared foundations (hubs) so the rest stays readable.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 476
- **Source:** [handoff247/mermaid.py](../../../../handoff247/mermaid.py)

**Notes from the previous owner**

> Builds the five diagrams. `system` collapses launch scripts into one node when there are more than three; `code` hides incoming arrows of shared foundations (hubs) so the rest stays readable.

**defines** →

- `Flow` · [handoff247/mermaid.py:34](../../../../handoff247/mermaid.py#L34)

**imports** →

- [`handoff247/connect.py`](handoff247__connect.py.md) · [handoff247/mermaid.py:10](../../../../handoff247/mermaid.py#L10)
- [`handoff247/labels.py`](handoff247__labels.py.md) · [handoff247/mermaid.py:11](../../../../handoff247/mermaid.py#L11)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/mermaid.py:12](../../../../handoff247/mermaid.py#L12)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:10](../../../../handoff247/build.py#L10)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_md.py:10](../../../../handoff247/render_md.py#L10)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:20](../../../../handoff247/workspace.py#L20)

## Comment in the file

Mermaid flowchart builders. *(module docstring)*

## Defined here

- `esc` — function, [line 28](../../../../handoff247/mermaid.py#L28)
- `Flow` — class, [line 34](../../../../handoff247/mermaid.py#L34)
- `Flow.node` — method, [line 47](../../../../handoff247/mermaid.py#L47)
- `Flow.edge` — method, [line 59](../../../../handoff247/mermaid.py#L59)
- `Flow.group` — method, [line 67](../../../../handoff247/mermaid.py#L67)
- `Flow.render` — method, [line 76](../../../../handoff247/mermaid.py#L76)
- `short` — function, [line 80](../../../../handoff247/mermaid.py#L80)
- `display` — function, [line 84](../../../../handoff247/mermaid.py#L84) — File name, or the full path when another file has the same name.
- `holes` — function, [line 91](../../../../handoff247/mermaid.py#L91) — Interpolation holes such as {DateTime.UtcNow:yyyyMMdd} shown as *.
- `system_map` — function, [line 123](../../../../handoff247/mermaid.py#L123) — Launchers → program → modes → interfaces → dispatch table, with the clients that call in.
- `startup` — function, [line 285](../../../../handoff247/mermaid.py#L285) — Every observed 'X starts Y' link: launch scripts, build outputs, MCP client configs, CI.
- `operations` — function, [line 335](../../../../handoff247/mermaid.py#L335) — Per dispatch table: who calls which group of operations, and which component handles them.
- `code_map` — function, [line 383](../../../../handoff247/mermaid.py#L383) — File-level dependency map grouped by folder.
- `areas_map` — function, [line 445](../../../../handoff247/mermaid.py#L445) — Folder-level overview with file counts and aggregated links between folders.
- `all_diagrams` — function, [line 469](../../../../handoff247/mermaid.py#L469)
