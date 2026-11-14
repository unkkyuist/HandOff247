---
generator: HandOff247
id: "file:handoff247/handlers.py"
type: File
source: "handoff247/handlers.py"
---

# `handoff247/handlers.py`

> What a route does. `PyIndex` follows a Python handler through `ast` into the project functions it calls (four levels deep) and records every effect with its file, line, call chain (`via`), the handler line that led ther…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 710
- **Source:** [handoff247/handlers.py](../../../../handoff247/handlers.py)

**Notes from the previous owner**

> What a route does. `PyIndex` follows a Python handler through `ast` into the project functions it calls (four levels deep) and records every effect with its file, line, call chain (`via`), the handler line that led there (`root`) and the `if` tests it sits inside (`when`). `parse_sql` reads tables and literal column values out of SQL strings; a value passed as a parameter counts only when the parameter list holds a literal. Two data flows are traced through variables instead of matched by name: an uploaded file object to the call that stores it, and the stored name into the SQL parameter. `access_other` reads role checks written directly on an Express route or above an ASP.NET action; handlers in those languages are not followed. A sentence that starts with `Select` is not SQL: both keywords must be present in the same letter case.

**defines** →

- `PyIndex` · [handoff247/handlers.py:258](../../../../handoff247/handlers.py#L258)

**imports** →

- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/handlers.py:25](../../../../handoff247/handlers.py#L25)

**refers to** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/handlers.py:316](../../../../handoff247/handlers.py#L316)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/journeys.py`](handoff247__journeys.py.md) · [handoff247/journeys.py:25](../../../../handoff247/journeys.py#L25)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:852](../../../../tests/test_handoff.py#L852)

## Comment in the file

What a route does, read from its handler. *(module docstring)*

## Defined here

- `parse_sql` — function, [line 83](../../../../handoff247/handlers.py#L83) — Tables a statement reads or writes, and the column values it sets or filters on.
- `PyIndex` — class, [line 258](../../../../handoff247/handlers.py#L258) — Functions, imports and module-level settings of every Python file of the project.
- `PyIndex.module_file` — method, [line 309](../../../../handoff247/handlers.py#L309)
- `PyIndex.resolve_call` — method, [line 336](../../../../handoff247/handlers.py#L336) — (file, function name) when the call certainly targets a function of this project.
- `PyIndex.resolve_const` — method, [line 350](../../../../handoff247/handlers.py#L350) — (file, NAME) of a module-level variable that an expression names.
- `PyIndex.handler` — method, [line 364](../../../../handoff247/handlers.py#L364)
- `PyIndex.access` — method, [line 377](../../../../handoff247/handlers.py#L377) — Who may call a route, as far as its decorators say.
- `PyIndex.effects` — method, [line 410](../../../../handoff247/handlers.py#L410)
- `access_other` — function, [line 679](../../../../handoff247/handlers.py#L679) — Role checks written directly on a route in JavaScript/TypeScript or C#.
