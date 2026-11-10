---
generator: HandOff247
id: "file:graphify.ps1"
type: File
source: "graphify.ps1"
---

# `graphify.ps1`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> The PowerShell wrapper sets a default PlayBook data directory and UTF-8 Python output, then passes its arguments to scripts/graphify-playbook.py and returns that process's exit code.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** PowerShell
- **Kind of file:** script
- **Lines:** 6
- **Source:** [graphify.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1)

**runs** →

- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [graphify.ps1:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L5)

**refers to** →

- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [graphify.ps1:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L5)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [graphify.ps1:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L3)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [graphify.ps1:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L3)
- [`PYTHONIOENCODING`](../environment.md) · [graphify.ps1:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L4)

**starts** →

- [`python`](../commands.md) · [graphify.ps1:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1#L5)

**is part of** ←

- [PlayBookOS](../overview.md)

**is run by** ←

- [`START_GRAPHIFY.cmd`](START_GRAPHIFY.cmd.md) (start) · [START_GRAPHIFY.cmd:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_GRAPHIFY.cmd#L3)

**is referred to by** ←

- [`START_GRAPHIFY.cmd`](START_GRAPHIFY.cmd.md) · [START_GRAPHIFY.cmd:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_GRAPHIFY.cmd#L3)
