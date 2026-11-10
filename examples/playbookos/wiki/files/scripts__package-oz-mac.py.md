---
generator: HandOff247
id: "file:scripts/package-oz-mac.py"
type: File
source: "scripts/package-oz-mac.py"
---

# `scripts/package-oz-mac.py`

> Build offline Mac handoff ZIPs from explicit native runtime directories.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Stages Mac handoff packages for Apple Silicon and Intel by copying published app files, Python dependencies, Graphify assets, setup scripts, and notices into a staging directory. It checks the bundled Python archive checksum, screens staged files for private data and machine paths, writes a manifest, and creates ZIP archives (plus an Intel TAR.XZ archive).

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 197
- **Source:** [scripts/package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

**refers to** →

- [`portable/oz/install.py`](portable__oz__install.py.md) · [scripts/package-oz-mac.py:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L97)
- [`portable/oz/oz_graphify_mcp.py`](portable__oz__oz_graphify_mcp.py.md) · [scripts/package-oz-mac.py:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L93)
- [`portable/oz/oz_mcp_proxy.py`](portable__oz__oz_mcp_proxy.py.md) · [scripts/package-oz-mac.py:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L94)
- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [scripts/package-oz-mac.py:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L95)
- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [scripts/package-oz-mac.py:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L91)
- [`scripts/graphify/index.html`](scripts__graphify__index.html.md) · [scripts/package-oz-mac.py:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L92)

**mentions** →

- [`github.com`](../hosts.md) · [scripts/package-oz-mac.py:115](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L115)

**is part of** ←

- [`scripts`](../areas/scripts.md)

## Defined here

- `sha` — function, [line 21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L21)
- `command` — function, [line 25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L25)
- `stage` — function, [line 68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L68)
- `archive` — function, [line 155](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L155)
