---
generator: HandOff247
id: "file:portable/oz/oz_graphify_mcp.py"
type: File
source: "portable/oz/oz_graphify_mcp.py"
---

# `portable/oz/oz_graphify_mcp.py`

> Project-aware Graphify MCP.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Implements an MCP server with tools to list and register local projects, analyze and search their code graphs, sync a code overview, and record user-confirmed workflows. It calls the PlayBook bridge for project and workflow records and exposes local support status and bundle creation tools.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 149
- **Source:** [portable/oz/oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py)

**imports** →

- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [portable/oz/oz_graphify_mcp.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L12)

**refers to** →

- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [portable/oz/oz_graphify_mcp.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L16)

**calls** →

- [`list`](../operations/list.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L63)
- [`save`](../operations/save.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L70)
- [`tool.start`](../operations/tool.start.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L78)
- [`tool.status`](../operations/tool.status.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L76)

**depends on** →

- [`mcp`](../packages.md) (imported) · [portable/oz/oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py)

**is part of** ←

- [`portable`](../areas/portable.md)

**is referred to by** ←

- [`portable/oz/install.py`](portable__oz__install.py.md) · [portable/oz/install.py:188](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L188)
- [`scripts/oz-package-smoke.py`](scripts__oz-package-smoke.py.md) · [scripts/oz-package-smoke.py:225](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L225)
- [`scripts/package-oz-mac.py`](scripts__package-oz-mac.py.md) · [scripts/package-oz-mac.py:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L93)

## Defined here

- `schema` — function, [line 39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L39)
- `register_project` — function, [line 57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L57)
- `ensure_companion` — function, [line 75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L75)
- `call` — function, [line 90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L90)
- `list_tools` — function, [line 130](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L130)
- `call_tool` — function, [line 134](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L134)
- `main` — function, [line 142](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L142)
