---
generator: HandOff247
id: "file:handoff247/analyzers/python.py"
type: File
source: "handoff247/analyzers/python.py"
---

# `handoff247/analyzers/python.py`

> Uses `ast`, never imports the file. Finds argparse sub-commands, subprocess launches (rendered with `{variable}` placeholders), env reads/writes, dict/if-chain/match dispatch tables, Flask/FastAPI routes and MCP tool de…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 281
- **Source:** [handoff247/analyzers/python.py](../../../../handoff247/analyzers/python.py)

**Notes from the previous owner**

> Uses `ast`, never imports the file. Finds argparse sub-commands, subprocess launches (rendered with `{variable}` placeholders), env reads/writes, dict/if-chain/match dispatch tables, Flask/FastAPI routes and MCP tool decorators.

**imports** →

- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [handoff247/analyzers/python.py:9](../../../../handoff247/analyzers/python.py#L9)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/analyzers/python.py:10](../../../../handoff247/analyzers/python.py#L10)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)

**handles** ←

- [`python`](../operations/python.md) (python.analyze) · [handoff247/analyzers/__init__.py:9](../../../../handoff247/analyzers/__init__.py#L9)

## Comment in the file

Python analyzer built on the standard ``ast`` module (no code is executed). *(module docstring)*

## Defined here

- `analyze` — function, [line 69](../../../../handoff247/analyzers/python.py#L69)
