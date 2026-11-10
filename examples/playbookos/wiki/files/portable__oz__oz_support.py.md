---
generator: HandOff247
id: "file:portable/oz/oz_support.py"
type: File
source: "portable/oz/oz_support.py"
---

# `portable/oz/oz_support.py`

> Bounded, content-free local audit journal and opt-in troubleshooting exports.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Writes a bounded local audit journal containing filtered event metadata and provides a status summary of recent errors and unanswered requests. On request, it creates a local ZIP support bundle with filtered audit records and a checksum file.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 201
- **Source:** [portable/oz/oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py)

**is part of** ←

- [`portable`](../areas/portable.md)

**is imported by** ←

- [`portable/oz/oz_graphify_mcp.py`](portable__oz__oz_graphify_mcp.py.md) · [portable/oz/oz_graphify_mcp.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L12)
- [`portable/oz/oz_mcp_proxy.py`](portable__oz__oz_mcp_proxy.py.md) · [portable/oz/oz_mcp_proxy.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py#L12)

**is referred to by** ←

- [`portable/oz/install.py`](portable__oz__install.py.md) · [portable/oz/install.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L25)
- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [scripts/graphify-playbook.py:32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L32)
- [`scripts/oz-logging-smoke.py`](scripts__oz-logging-smoke.py.md) · [scripts/oz-logging-smoke.py:32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L32)
- [`scripts/oz-package-smoke.py`](scripts__oz-package-smoke.py.md) · [scripts/oz-package-smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L64)
- [`scripts/package-oz-mac.py`](scripts__package-oz-mac.py.md) · [scripts/package-oz-mac.py:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L95)

## Defined here

- `ref` — function, [line 28](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L28) — Correlate IDs without recording paths, names, prompts or user supplied RPC IDs.
- `category` — function, [line 33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L33)
- `clean` — function, [line 52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L52) — Allowlist fields and values again on export; never trust text in local log files.
- `locked` — function, [line 77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L77)
- `emit` — function, [line 111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L111)
- `snapshot` — function, [line 135](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L135)
- `summarize` — function, [line 153](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L153)
- `status` — function, [line 168](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L168)
- `create_bundle` — function, [line 172](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L172)
