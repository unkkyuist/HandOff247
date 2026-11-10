---
generator: HandOff247
id: "file:scripts/real-provider-smoke.py"
type: File
source: "scripts/real-provider-smoke.py"
---

# `scripts/real-provider-smoke.py`

> Explicit, small read-only smoke against installed, already signed-in Codex and Claude.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Runs a read-only smoke workflow using already signed-in Codex and Claude CLIs against a temporary project, separate data directory, and local server. It checks provider execution, shared-reference access, and handoff between runs, then writes a results report; Claude access may be reported as blocked when the organization disables subscription access.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 82
- **Source:** [scripts/real-provider-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/real-provider-smoke.py:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L15)

**refers to** →

- [`README.md`](README.md.md) · [scripts/real-provider-smoke.py:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L19)

**calls** →

- [`library.register`](../operations/library.register.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:28](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L28)
- [`provider.status`](../operations/provider.status.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L25)
- [`run.enqueue`](../operations/run.enqueue.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:29](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L29)
- [`save`](../operations/save.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:27](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L27)

**reads** →

- [`PLAYBOOK_TEST_DLL`](../environment.md) · [scripts/real-provider-smoke.py:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L15)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

## Defined here

- `cli` — function, [line 21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L21)
- `request` — function, [line 35](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L35)
