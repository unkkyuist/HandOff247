---
generator: HandOff247
id: "file:scripts/oz-logging-smoke.py"
type: File
source: "scripts/oz-logging-smoke.py"
---

# `scripts/oz-logging-smoke.py`

> Real-process failure/privacy/concurrency tests for Oz's content-free audit boundary.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> This script exercises Oz logging and support-bundle behavior using temporary configurations, fixture processes, and concurrent writers. Its checks cover content-free audit events, error and crash handling, log rotation, bundle contents and checksums, and installer diagnostics; it writes a JSON report with the check results.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 139
- **Source:** [scripts/oz-logging-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py)

**refers to** →

- [`portable/oz/install.py`](portable__oz__install.py.md) · [scripts/oz-logging-smoke.py:33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L33)
- [`portable/oz/oz_mcp_proxy.py`](portable__oz__oz_mcp_proxy.py.md) · [scripts/oz-logging-smoke.py:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L58)
- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [scripts/oz-logging-smoke.py:32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L32)

**is part of** ←

- [`scripts`](../areas/scripts.md)

## Defined here

- `check` — function, [line 19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L19)
- `load` — function, [line 25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L25)
