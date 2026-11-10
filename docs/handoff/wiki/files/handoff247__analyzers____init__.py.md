---
generator: HandOff247
id: "file:handoff247/analyzers/__init__.py"
type: File
source: "handoff247/analyzers/__init__.py"
---

# `handoff247/analyzers/__init__.py`

> Maps a file's language to its analyzer. An exception inside one analyzer marks only that file as "not parsed"; it never stops the run.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 37
- **Source:** [handoff247/analyzers/__init__.py](../../../../handoff247/analyzers/__init__.py)

**Notes from the previous owner**

> Maps a file's language to its analyzer. An exception inside one analyzer marks only that file as "not parsed"; it never stops the run.

**defines** →

- [`handoff247/analyzers/__init__.py:7`](../operations.md) · [handoff247/analyzers/__init__.py:7](../../../../handoff247/analyzers/__init__.py#L7)

**imports** →

- [`handoff247/analyzers/csharp.py`](handoff247__analyzers__csharp.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)
- [`handoff247/analyzers/docs.py`](handoff247__analyzers__docs.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)
- [`handoff247/analyzers/python.py`](handoff247__analyzers__python.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)
- [`handoff247/analyzers/shell.py`](handoff247__analyzers__shell.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)
- [`handoff247/analyzers/web.py`](handoff247__analyzers__web.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/analyzers/__init__.py:4](../../../../handoff247/analyzers/__init__.py#L4)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/pipeline.py:6](../../../../handoff247/pipeline.py#L6)

## Comment in the file

Per-language analyzers. *(module docstring)*

## Defined here

- `analyze` — function, [line 28](../../../../handoff247/analyzers/__init__.py#L28)
