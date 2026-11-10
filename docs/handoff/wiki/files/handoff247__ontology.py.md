---
generator: HandOff247
id: "file:handoff247/ontology.py"
type: File
source: "handoff247/ontology.py"
---

# `handoff247/ontology.py`

> Turns `project.links` and `project.edges` into typed entities and relations. It detects nothing itself; add a new kind of fact in an analyzer or in `connect.py` first, then map it here. `CLASSES` and `RELATIONS` are the…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 278
- **Source:** [handoff247/ontology.py](../../../../handoff247/ontology.py)

**Notes from the previous owner**

> Turns `project.links` and `project.edges` into typed entities and relations. It detects nothing itself; add a new kind of fact in an analyzer or in `connect.py` first, then map it here. `CLASSES` and `RELATIONS` are the schema: a class has a colour group and a shape (the graph has eight colours, so classes share one and differ by shape), a relation has a label for each direction. `_Builder.rel` drops a relation whose ends are not both entities, which is why assets and system environment variables never appear.

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/ontology.py:10](../../../../handoff247/ontology.py#L10)
- [`handoff247/connect.py`](handoff247__connect.py.md) · [handoff247/ontology.py:11](../../../../handoff247/ontology.py#L11)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/ontology.py:12](../../../../handoff247/ontology.py#L12)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/ontology.py:128](../../../../handoff247/ontology.py#L128)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:9](../../../../handoff247/build.py#L9)

## Comment in the file

The project as an ontology: typed entities and typed relations between them. *(module docstring)*

## Defined here

- `first_line` — function, [line 70](../../../../handoff247/ontology.py#L70)
- `_Builder.ent` — method, [line 84](../../../../handoff247/ontology.py#L84)
- `_Builder.rel` — method, [line 100](../../../../handoff247/ontology.py#L100)
- `build` — function, [line 119](../../../../handoff247/ontology.py#L119)
