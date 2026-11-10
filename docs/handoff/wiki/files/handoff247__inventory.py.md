---
generator: HandOff247
id: "file:handoff247/inventory.py"
type: File
source: "handoff247/inventory.py"
---

# `handoff247/inventory.py`

> Lists files with `git ls-files` (so .gitignore applies), falls back to a directory walk, applies `.handoffignore` and skips folders that contain an earlier pack.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 254
- **Source:** [handoff247/inventory.py](../../../../handoff247/inventory.py)

**Notes from the previous owner**

> Lists files with `git ls-files` (so .gitignore applies), falls back to a directory walk, applies `.handoffignore` and skips folders that contain an earlier pack.

**imports** →

- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/inventory.py:14](../../../../handoff247/inventory.py#L14)

**starts** →

- [`git`](../commands.md) · [handoff247/inventory.py:95](../../../../handoff247/inventory.py#L95)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/leaving.py:15](../../../../handoff247/leaving.py#L15)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/pipeline.py:8](../../../../handoff247/pipeline.py#L8)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:19](../../../../handoff247/workspace.py#L19)

## Comment in the file

Find the project's files and classify them. *(module docstring)*

## Defined here

- `read_ignore` — function, [line 60](../../../../handoff247/inventory.py#L60) — fnmatch patterns from <project>/.handoffignore plus --exclude options.
- `excluded` — function, [line 72](../../../../handoff247/inventory.py#L72)
- `list_files` — function, [line 83](../../../../handoff247/inventory.py#L83)
- `classify` — function, [line 187](../../../../handoff247/inventory.py#L187)
- `load` — function, [line 223](../../../../handoff247/inventory.py#L223)
