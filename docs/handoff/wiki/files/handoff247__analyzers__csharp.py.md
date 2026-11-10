---
generator: HandOff247
id: "file:handoff247/analyzers/csharp.py"
type: File
source: "handoff247/analyzers/csharp.py"
---

# `handoff247/analyzers/csharp.py`

> The richest analyzer: types and primary-constructor dependencies, entry modes (`if (mode == "x")` in the entry file), `switch` dispatch tables with handler resolution, minimal-API routes, `[McpServerTool]` methods, envi…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 435
- **Source:** [handoff247/analyzers/csharp.py](../../../../handoff247/analyzers/csharp.py)

**Notes from the previous owner**

> The richest analyzer: types and primary-constructor dependencies, entry modes (`if (mode == "x")` in the entry file), `switch` dispatch tables with handler resolution, minimal-API routes, `[McpServerTool]` methods, environment variables and `Path.Combine` literals.

**imports** →

- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [handoff247/analyzers/csharp.py:7](../../../../handoff247/analyzers/csharp.py#L7)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/analyzers/csharp.py:8](../../../../handoff247/analyzers/csharp.py#L8)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)

**handles** ←

- [`csharp`](../operations/csharp.md) (csharp.analyze) · [handoff247/analyzers/__init__.py:8](../../../../handoff247/analyzers/__init__.py#L8)

## Comment in the file

C# analyzer: types, members, constructor dependencies, entry modes, switch dispatch tables, ASP.NET minimal-API routes, MCP server tools, environment variables and process launches. *(module docstring)*

## Defined here

- `analyze` — function, [line 117](../../../../handoff247/analyzers/csharp.py#L117)
