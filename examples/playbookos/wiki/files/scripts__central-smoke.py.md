---
generator: HandOff247
id: "file:scripts/central-smoke.py"
type: File
source: "scripts/central-smoke.py"
---

# `scripts/central-smoke.py`

> Isolated recursive scanning, authentication, queue/lease and two real device-client processes.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 184
- **Source:** [scripts/central-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/central-smoke.py:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L20)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [scripts/central-smoke.py:49](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L49)
- [`scripts/fixtures/provider.py`](scripts__fixtures__provider.py.md) · [scripts/central-smoke.py:112](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L112)

**reads** →

- [`PLAYBOOK_TEST_DLL`](../environment.md) · [scripts/central-smoke.py:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L20)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [scripts/central-smoke.py:30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L30)
- [`PLAYBOOK_PORT`](../environment.md) · [scripts/central-smoke.py:117](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L117)

**starts** →

- [`dotnet`](../commands.md) · [scripts/central-smoke.py:30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L30)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

## Defined here

- `check` — function, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L22)
- `port` — function, [line 26](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L26)
- `call` — function, [line 29](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L29)
- `request` — function, [line 35](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L35)
