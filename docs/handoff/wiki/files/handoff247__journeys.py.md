---
generator: HandOff247
id: "file:handoff247/journeys.py"
type: File
source: "handoff247/journeys.py"
---

# `handoff247/journeys.py`

> Joins screens.py and handlers.py into `project.links["journeys"]`: user types, screens, terms, features (one per route), data tables with states, assets, hand-overs, shared functions and gaps. `match_path` fits a path w…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 671
- **Source:** [handoff247/journeys.py](../../../../handoff247/journeys.py)

**Notes from the previous owner**

> Joins screens.py and handlers.py into `project.links["journeys"]`: user types, screens, terms, features (one per route), data tables with states, assets, hand-overs, shared functions and gaps. `match_path` fits a path written in a template to a route; a hole in the path only fits a route parameter, never a fixed word. A hand-over is one feature setting a column value that another feature's query filters on; it is always marked inferred. Everything that could not be connected goes to `gaps` instead of being guessed. The user types are those of the analysed application and must never be used to hide part of the pack from its reader.

**defines** →

- [`handoff247/journeys.py:139`](../operations.md) · [handoff247/journeys.py:139](../../../../handoff247/journeys.py#L139)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/journeys.py:24](../../../../handoff247/journeys.py#L24)
- [`handoff247/handlers.py`](handoff247__handlers.py.md) · [handoff247/journeys.py:25](../../../../handoff247/journeys.py#L25)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/journeys.py:26](../../../../handoff247/journeys.py#L26)
- [`handoff247/screens.py`](handoff247__screens.py.md) · [handoff247/journeys.py:24](../../../../handoff247/journeys.py#L24)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/explore.py`](handoff247__explore.py.md) · [handoff247/explore.py:19](../../../../handoff247/explore.py#L19)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/pipeline.py:6](../../../../handoff247/pipeline.py#L6)
- [`handoff247/render_users.py`](handoff247__render_users.py.md) · [handoff247/render_users.py:12](../../../../handoff247/render_users.py#L12)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:871](../../../../tests/test_handoff.py#L871)

## Comment in the file

The application as its users meet it. *(module docstring)*

## Defined here

- `match_path` — function, [line 49](../../../../handoff247/journeys.py#L49) — Features whose route template fits a path written in a template or script.
- `build` — function, [line 93](../../../../handoff247/journeys.py#L93)
- `attach` — function, [line 662](../../../../handoff247/journeys.py#L662)
- `empty` — function, [line 669](../../../../handoff247/journeys.py#L669)
