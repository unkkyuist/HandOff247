---
generator: HandOff247
id: "file:handoff247/model.py"
type: File
source: "handoff247/model.py"
---

# `handoff247/model.py`

> Dataclasses: FileInfo, Symbol, Fact, Edge, Project. A Fact is one observation with a file and line; everything in the pack traces back to one.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 91
- **Source:** [handoff247/model.py](../../../../handoff247/model.py)

**Notes from the previous owner**

> Dataclasses: FileInfo, Symbol, Fact, Edge, Project. A Fact is one observation with a file and line; everything in the pack traces back to one.

**defines** →

- `Edge` · [handoff247/model.py:65](../../../../handoff247/model.py#L65)
- `Fact` · [handoff247/model.py:25](../../../../handoff247/model.py#L25)
- `FileInfo` · [handoff247/model.py:38](../../../../handoff247/model.py#L38)
- `Project` · [handoff247/model.py:75](../../../../handoff247/model.py#L75)
- `Symbol` · [handoff247/model.py:14](../../../../handoff247/model.py#L14)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/analyzers/__init__.py:4](../../../../handoff247/analyzers/__init__.py#L4)
- [`handoff247/analyzers/csharp.py`](handoff247__analyzers__csharp.py.md) · [handoff247/analyzers/csharp.py:8](../../../../handoff247/analyzers/csharp.py#L8)
- [`handoff247/analyzers/docs.py`](handoff247__analyzers__docs.py.md) · [handoff247/analyzers/docs.py:9](../../../../handoff247/analyzers/docs.py#L9)
- [`handoff247/analyzers/python.py`](handoff247__analyzers__python.py.md) · [handoff247/analyzers/python.py:10](../../../../handoff247/analyzers/python.py#L10)
- [`handoff247/analyzers/shell.py`](handoff247__analyzers__shell.py.md) · [handoff247/analyzers/shell.py:7](../../../../handoff247/analyzers/shell.py#L7)
- [`handoff247/analyzers/web.py`](handoff247__analyzers__web.py.md) · [handoff247/analyzers/web.py:7](../../../../handoff247/analyzers/web.py#L7)
- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:11](../../../../handoff247/build.py#L11)
- [`handoff247/connect.py`](handoff247__connect.py.md) · [handoff247/connect.py:11](../../../../handoff247/connect.py#L11)
- [`handoff247/inventory.py`](handoff247__inventory.py.md) · [handoff247/inventory.py:14](../../../../handoff247/inventory.py#L14)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/leaving.py:16](../../../../handoff247/leaving.py#L16)
- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/mermaid.py:12](../../../../handoff247/mermaid.py#L12)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/notes.py:17](../../../../handoff247/notes.py#L17)
- [`handoff247/ontology.py`](handoff247__ontology.py.md) · [handoff247/ontology.py:12](../../../../handoff247/ontology.py#L12)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/pipeline.py:9](../../../../handoff247/pipeline.py#L9)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_md.py:11](../../../../handoff247/render_md.py#L11)
- [`handoff247/summarize.py`](handoff247__summarize.py.md) · [handoff247/summarize.py:28](../../../../handoff247/summarize.py#L28)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [handoff247/translate.py:15](../../../../handoff247/translate.py#L15)

## Comment in the file

Data model shared by every analyzer and renderer. *(module docstring)*

## Defined here

- `Symbol` — class, [line 14](../../../../handoff247/model.py#L14)
- `Fact` — class, [line 25](../../../../handoff247/model.py#L25) — One observation.
- `FileInfo` — class, [line 38](../../../../handoff247/model.py#L38)
- `FileInfo.to_json` — method, [line 57](../../../../handoff247/model.py#L57)
- `Edge` — class, [line 65](../../../../handoff247/model.py#L65)
- `Project` — class, [line 75](../../../../handoff247/model.py#L75)
- `Project.file` — method, [line 84](../../../../handoff247/model.py#L84)
- `Project.facts_of` — method, [line 90](../../../../handoff247/model.py#L90)
