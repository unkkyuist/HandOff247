---
generator: HandOff247
id: "file:portable/oz/oz_mcp_proxy.py"
type: File
source: "portable/oz/oz_mcp_proxy.py"
---

# `portable/oz/oz_mcp_proxy.py`

> Transparent stdio MCP proxy.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Runs a child MCP server and forwards messages between it and standard input/output. It records allowlisted request and response metadata in the local audit journal, without recording protocol bodies.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 141
- **Source:** [portable/oz/oz_mcp_proxy.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py)

**imports** →

- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [portable/oz/oz_mcp_proxy.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py#L12)

**is part of** ←

- [`portable`](../areas/portable.md)

**is referred to by** ←

- [`portable/oz/install.py`](portable__oz__install.py.md) · [portable/oz/install.py:188](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L188)
- [`scripts/oz-logging-smoke.py`](scripts__oz-logging-smoke.py.md) · [scripts/oz-logging-smoke.py:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L58)
- [`scripts/oz-package-smoke.py`](scripts__oz-package-smoke.py.md) · [scripts/oz-package-smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L64)
- [`scripts/package-oz-mac.py`](scripts__package-oz-mac.py.md) · [scripts/package-oz-mac.py:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L94)

## Defined here

- `run` — function, [line 17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py#L17)
