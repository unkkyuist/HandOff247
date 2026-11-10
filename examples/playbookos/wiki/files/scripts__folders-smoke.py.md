---
generator: HandOff247
id: "file:scripts/folders-smoke.py"
type: File
source: "scripts/folders-smoke.py"
---

# `scripts/folders-smoke.py`

> Real, isolated filesystem + SQLite tests for folder organization.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Creates isolated filesystem and SQLite scenarios to exercise folder creation, move previews and application, reference updates, and recovery. It checks rejection of unsafe or stale operations and writes the check results to `artifacts/folders-smoke.json`.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 83
- **Source:** [scripts/folders-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/folders-smoke.py:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L9)

**calls** →

- [`events`](../operations/events.md) (call(), by starting a process) · [scripts/folders-smoke.py:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L42)
- [`folder.apply`](../operations/folder.apply.md) (call(), by starting a process) · [scripts/folders-smoke.py:36](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L36)
- [`folder.list`](../operations/folder.list.md) (call(), by starting a process) · [scripts/folders-smoke.py:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L74)
- [`folder.mkdir`](../operations/folder.mkdir.md) (call(), by starting a process) · [scripts/folders-smoke.py:26](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L26)
- [`folder.plan`](../operations/folder.plan.md) (call(), by starting a process) · [scripts/folders-smoke.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L25)
- [`folder.recover`](../operations/folder.recover.md) (call(), by starting a process) · [scripts/folders-smoke.py:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L68)
- [`get`](../operations/get.md) (call(), by starting a process) · [scripts/folders-smoke.py:39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L39)
- [`list`](../operations/list.md) (call(), by starting a process) · [scripts/folders-smoke.py:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L40)
- [`save`](../operations/save.md) (call(), by starting a process) · [scripts/folders-smoke.py:23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L23)

**reads** →

- [`PLAYBOOK_TEST_DLL`](../environment.md) · [scripts/folders-smoke.py:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L9)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

## Defined here

- `check` — function, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L11)
