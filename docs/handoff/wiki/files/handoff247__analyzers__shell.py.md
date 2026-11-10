---
generator: HandOff247
id: "file:handoff247/analyzers/shell.py"
type: File
source: "handoff247/analyzers/shell.py"
---

# `handoff247/analyzers/shell.py`

> PowerShell, POSIX shell and batch: leading comment / .SYNOPSIS as summary, `$env:` / `export` / `set` variables, and command lines that launch something (dotnet, python, powershell -File, `&` call operator, start URL).

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 178
- **Source:** [handoff247/analyzers/shell.py](../../../../handoff247/analyzers/shell.py)

**Notes from the previous owner**

> PowerShell, POSIX shell and batch: leading comment / .SYNOPSIS as summary, `$env:` / `export` / `set` variables, and command lines that launch something (dotnet, python, powershell -File, `&` call operator, start URL).

**imports** →

- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [handoff247/analyzers/shell.py:6](../../../../handoff247/analyzers/shell.py#L6)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/analyzers/shell.py:7](../../../../handoff247/analyzers/shell.py#L7)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)

**handles** ←

- [`batch`](../operations/batch.md) (shell.analyze_batch) · [handoff247/analyzers/__init__.py:16](../../../../handoff247/analyzers/__init__.py#L16)
- [`powershell`](../operations/powershell.md) (shell.analyze_powershell) · [handoff247/analyzers/__init__.py:14](../../../../handoff247/analyzers/__init__.py#L14)
- [`shell`](../operations/shell.md) (shell.analyze_shell) · [handoff247/analyzers/__init__.py:15](../../../../handoff247/analyzers/__init__.py#L15)

## Comment in the file

PowerShell, POSIX shell and Windows batch analyzers (line based, no execution). *(module docstring)*

## Defined here

- `analyze_powershell` — function, [line 52](../../../../handoff247/analyzers/shell.py#L52)
- `analyze_shell` — function, [line 124](../../../../handoff247/analyzers/shell.py#L124)
- `analyze_batch` — function, [line 151](../../../../handoff247/analyzers/shell.py#L151)
