---
generator: HandOff247
id: "file:handoff247/pipeline.py"
type: File
source: "handoff247/pipeline.py"
---

# `handoff247/pipeline.py`

> analyze_project(): inventory, per-file analysis, linking.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 21
- **Source:** [handoff247/pipeline.py](../../../../handoff247/pipeline.py)

**Notes from the previous owner**

> analyze_project(): inventory, per-file analysis, linking.

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/pipeline.py:6](../../../../handoff247/pipeline.py#L6)
- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/pipeline.py:6](../../../../handoff247/pipeline.py#L6)
- [`handoff247/connect.py`](handoff247__connect.py.md) · [handoff247/pipeline.py:7](../../../../handoff247/pipeline.py#L7)
- [`handoff247/inventory.py`](handoff247__inventory.py.md) · [handoff247/pipeline.py:8](../../../../handoff247/pipeline.py#L8)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/pipeline.py:6](../../../../handoff247/pipeline.py#L6)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/pipeline.py:9](../../../../handoff247/pipeline.py#L9)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:12](../../../../handoff247/cli.py#L12)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:21](../../../../handoff247/workspace.py#L21)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:19](../../../../tests/test_handoff.py#L19)

## Comment in the file

Scan → analyze each file → link files together. *(module docstring)*

## Defined here

- `analyze_project` — function, [line 12](../../../../handoff247/pipeline.py#L12)
