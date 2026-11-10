---
generator: HandOff247
id: "file:portable/oz/install.py"
type: File
source: "portable/oz/install.py"
---

# `portable/oz/install.py`

> Oz's offline Mac installer and launch/repair/diagnostic actions.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 445
- **Source:** [portable/oz/install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py)

**refers to** →

- [`portable/oz/oz_graphify_mcp.py`](portable__oz__oz_graphify_mcp.py.md) · [portable/oz/install.py:188](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L188)
- [`portable/oz/oz_mcp_proxy.py`](portable__oz__oz_mcp_proxy.py.md) · [portable/oz/install.py:188](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L188)
- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [portable/oz/install.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L25)
- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [portable/oz/install.py:189](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L189)
- [`scripts/graphify/index.html`](scripts__graphify__index.html.md) · [portable/oz/install.py:189](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L189)

**calls** →

- [`connection.configure`](../operations/connection.configure.md) (playbook()) · [portable/oz/install.py:146](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L146)
- [`info`](../operations/info.md) (playbook()) · [portable/oz/install.py:145](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L145)
- [`list`](../operations/list.md) (playbook()) · [portable/oz/install.py:162](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L162)
- [`save`](../operations/save.md) (playbook()) · [portable/oz/install.py:164](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L164)
- [`tool.start`](../operations/tool.start.md) (playbook()) · [portable/oz/install.py:302](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L302)
- [`tool.status`](../operations/tool.status.md) (playbook()) · [portable/oz/install.py:296](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L296)
- [`tool.stop`](../operations/tool.stop.md) (playbook()) · [portable/oz/install.py:209](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L209)

**reads** →

- [`CLAUDE_CONFIG_DIR`](../environment.md) · [portable/oz/install.py:387](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L387)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [portable/oz/install.py:103](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L103)

**depends on** →

- [`mcp`](../packages.md) (imported) · [portable/oz/install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py)

**is part of** ←

- [`portable`](../areas/portable.md)

**is referred to by** ←

- [`scripts/oz-logging-smoke.py`](scripts__oz-logging-smoke.py.md) · [scripts/oz-logging-smoke.py:33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L33)
- [`scripts/oz-package-smoke.py`](scripts__oz-package-smoke.py.md) · [scripts/oz-package-smoke.py:132](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L132)
- [`scripts/package-oz-mac.py`](scripts__package-oz-mac.py.md) · [scripts/package-oz-mac.py:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L97)

## Defined here

- `read` — function, [line 30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L30)
- `write` — function, [line 34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L34)
- `digest` — function, [line 48](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L48)
- `verify` — function, [line 52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L52)
- `extract_runtime` — function, [line 63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L63)
- `merge_claude` — function, [line 78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L78)
- `load_bridge` — function, [line 102](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L102)
- `choose_port` — function, [line 110](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L110)
- `configure` — function, [line 132](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L132)
- `mcp_definitions` — function, [line 169](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L169)
- `upgrade_logging` — function, [line 179](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L179) — One bounded 0.1.0 -> 0.1.1 script-only update; never replace the ledger/runtimes.
- `install` — function, [line 247](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L247)
- `start` — function, [line 292](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L292)
- `check_mcp` — function, [line 318](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L318)
- `diagnose` — function, [line 342](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L342)
- `main` — function, [line 366](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L366)
