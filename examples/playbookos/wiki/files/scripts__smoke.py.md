---
generator: HandOff247
id: "file:scripts/smoke.py"
type: File
source: "scripts/smoke.py"
---

# `scripts/smoke.py`

> End-to-end tests against a fresh SQLite database, real CLI, HTTP and MCP transports.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 173
- **Source:** [scripts/smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/smoke.py:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L19)

**calls** →

- [`asset.verify`](../operations/asset.verify.md) (cli(), by starting a process) · [scripts/smoke.py:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L80)
- [`backup`](../operations/backup.md) (cli(), by starting a process) · [scripts/smoke.py:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L83)
- [`canon.approve`](../operations/canon.approve.md) (cli(), by starting a process) · [scripts/smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L64)
- [`context`](../operations/context.md) (cli(), by starting a process) · [scripts/smoke.py:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L75)
- [`events`](../operations/events.md) (cli(), by starting a process) · [scripts/smoke.py:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L59)
- [`export`](../operations/export.md) (cli(), by starting a process) · [scripts/smoke.py:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L81)
- [`get`](../operations/get.md) (cli(), by starting a process) · [scripts/smoke.py:49](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L49)
- [`save`](../operations/save.md) (cli(), by starting a process) · [scripts/smoke.py:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L45)
- [`tool.logs`](../operations/tool.logs.md) (cli(), by starting a process) · [scripts/smoke.py:164](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L164)
- [`tool.start`](../operations/tool.start.md) (cli(), by starting a process) · [scripts/smoke.py:160](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L160)
- [`tool.status`](../operations/tool.status.md) (cli(), by starting a process) · [scripts/smoke.py:162](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L162)
- [`tool.stop`](../operations/tool.stop.md) (cli(), by starting a process) · [scripts/smoke.py:166](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L166)

**reads** →

- [`PLAYBOOK_TEST_DLL`](../environment.md) · [scripts/smoke.py:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L19)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

## Defined here

- `check` — function, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L22)
- `port` — function, [line 28](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L28)
