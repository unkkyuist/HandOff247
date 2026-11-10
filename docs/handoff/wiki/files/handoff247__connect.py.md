---
generator: HandOff247
id: "file:handoff247/connect.py"
type: File
source: "handoff247/connect.py"
---

# `handoff247/connect.py`

> Turns per-file facts into edges and connection maps. The key idea: string keys of a dispatch table (`"list"`, `"ontology.search"`) are followed to every caller (`api('list')`, `cli('list')`, `Call("list")`, `cli list` i…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 677
- **Source:** [handoff247/connect.py](../../../../handoff247/connect.py)

**Notes from the previous owner**

> Turns per-file facts into edges and connection maps. The key idea: string keys of a dispatch table (`"list"`, `"ontology.search"`) are followed to every caller (`api('list')`, `cli('list')`, `Call("list")`, `cli list` in docs), and each caller's wrapper function is inspected to tell HTTP, CLI process or in-process apart. A caller group only counts when it uses two or more keys or a dotted key, so ordinary strings like "git" are not mistaken for operations.

**defines** →

- `FileIndex` · [handoff247/connect.py:37](../../../../handoff247/connect.py#L37)

**imports** →

- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/connect.py:11](../../../../handoff247/connect.py#L11)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/mermaid.py:10](../../../../handoff247/mermaid.py#L10)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/notes.py:15](../../../../handoff247/notes.py#L15)
- [`handoff247/ontology.py`](handoff247__ontology.py.md) · [handoff247/ontology.py:11](../../../../handoff247/ontology.py#L11)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/pipeline.py:7](../../../../handoff247/pipeline.py#L7)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_md.py:8](../../../../handoff247/render_md.py#L8)

## Comment in the file

Cross-file linking: turns per-file facts into edges and the connection maps (entry modes, dispatch tables and who calls each operation, routes, MCP tools, launch chain, environment variables, ports). *(module docstring)*

## Defined here

- `area_of` — function, [line 33](../../../../handoff247/connect.py#L33)
- `FileIndex` — class, [line 37](../../../../handoff247/connect.py#L37)
- `FileIndex.resolve` — method, [line 46](../../../../handoff247/connect.py#L46)
- `FileIndex.build_output` — method, [line 86](../../../../handoff247/connect.py#L86)
- `link` — function, [line 94](../../../../handoff247/connect.py#L94)
