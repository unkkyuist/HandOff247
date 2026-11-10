---
generator: HandOff247
id: "file:scripts/graphify-playbook.py"
type: File
source: "scripts/graphify-playbook.py"
---

# `scripts/graphify-playbook.py`

> Local Graphify companion using PlayBook's existing tool and ontology APIs.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 398
- **Source:** [scripts/graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/graphify-playbook.py:27](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L27)

**refers to** →

- [`examples/mcp.json`](examples__mcp.json.md) · [scripts/graphify-playbook.py:207](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L207)
- [`portable/oz/oz_support.py`](portable__oz__oz_support.py.md) · [scripts/graphify-playbook.py:32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L32)
- [`scripts/graphify/index.html`](scripts__graphify__index.html.md) · [scripts/graphify-playbook.py:296](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L296)

**calls** →

- [`context`](../operations/context.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:182](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L182)
- [`get`](../operations/get.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L79)
- [`list`](../operations/list.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:255](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L255)
- [`ontology.connect`](../operations/ontology.connect.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:235](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L235)
- [`ontology.connections`](../operations/ontology.connections.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:232](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L232)
- [`ontology.sync`](../operations/ontology.sync.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:237](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L237)
- [`tool.start`](../operations/tool.start.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:386](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L386)
- [`tool.status`](../operations/tool.status.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:383](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L383)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [scripts/graphify-playbook.py:23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L23)

**mentions** →

- [`unpkg.com`](../hosts.md) · [scripts/graphify-playbook.py:203](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L203)
- [`7331`](../ports.md) (address literal) · [scripts/graphify-playbook.py:297](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L297)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is run by** ←

- [`graphify.ps1`](graphify.ps1.md) · [graphify.ps1:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L5)

**is referred to by** ←

- [`graphify.ps1`](graphify.ps1.md) · [graphify.ps1:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L5)
- [`portable/oz/install.py`](portable__oz__install.py.md) · [portable/oz/install.py:189](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L189)
- [`portable/oz/oz_graphify_mcp.py`](portable__oz__oz_graphify_mcp.py.md) · [portable/oz/oz_graphify_mcp.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L16)
- [`scripts/graphify-smoke.py`](scripts__graphify-smoke.py.md) · [scripts/graphify-smoke.py:82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L82)
- [`scripts/oz-package-smoke.py`](scripts__oz-package-smoke.py.md) · [scripts/oz-package-smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L64)
- [`scripts/package-oz-mac.py`](scripts__package-oz-mac.py.md) · [scripts/package-oz-mac.py:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L91)

## Defined here

- `audit_event` — function, [line 40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L40)
- `read_json` — function, [line 45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L45)
- `write_json` — function, [line 49](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L49)
- `playbook` — function, [line 62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L62)
- `project_dir` — function, [line 71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L71)
- `project` — function, [line 77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L77)
- `local_path` — function, [line 85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L85)
- `project_lock` — function, [line 95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L95)
- `make_feed` — function, [line 115](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L115) — Bounded overview; the complete graph stays available to Graphify queries.
- `analyze` — function, [line 173](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L173)
- `current` — function, [line 221](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L221)
- `sync` — function, [line 228](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L228)
- `query` — function, [line 243](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L243)
- `projects` — function, [line 253](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L253)
- `serve` — function, [line 268](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L268)
- `main` — function, [line 355](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L355)
