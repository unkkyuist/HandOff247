---
generator: HandOff247
id: "file:scripts/oz-package-smoke.py"
type: File
source: "scripts/oz-package-smoke.py"
---

# `scripts/oz-package-smoke.py`

> Audit real Mac payloads and exercise their installer/MCP logic on Windows.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 243
- **Source:** [scripts/oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/oz-package-smoke.py:143](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L143)

**refers to** →

- [`portable/oz/install.py`](portable__oz__install.py.md) · [scripts/oz-package-smoke.py:132](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L132)
- [`portable/oz/oz_graphify_mcp.py`](portable__oz__oz_graphify_mcp.py.md) · [scripts/oz-package-smoke.py:225](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L225)
- [`portable/oz/oz_mcp_proxy.py`](portable__oz__oz_mcp_proxy.py.md) · [scripts/oz-package-smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L64)
- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [scripts/oz-package-smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L64)
- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [scripts/oz-package-smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L64)

**calls** →

- [`get`](../operations/get.md) (playbook()) · [scripts/oz-package-smoke.py:205](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L205)
- [`tool.status`](../operations/tool.status.md) (playbook()) · [scripts/oz-package-smoke.py:185](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L185)
- [`tool.stop`](../operations/tool.stop.md) (playbook()) · [scripts/oz-package-smoke.py:186](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L186)

**depends on** →

- [`mcp`](../packages.md) (imported) · [scripts/oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py)

**is part of** ←

- [`scripts`](../areas/scripts.md)

## Defined here

- `check` — function, [line 21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L21)
- `import_file` — function, [line 27](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L27)
- `arches` — function, [line 34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L34)
- `check_installed_mcp` — function, [line 68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L68)
