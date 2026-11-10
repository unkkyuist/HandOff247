---
generator: HandOff247
id: "file:playbook.sh"
type: File
source: "playbook.sh"
---

# `playbook.sh`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> This shell wrapper sets the default PlayBook data directory, builds the Release DLL if it is missing, and executes it with the supplied arguments from the project directory.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Shell
- **Kind of file:** script
- **Lines:** 9
- **Source:** [playbook.sh](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [playbook.sh:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh#L9)

**refers to** →

- [`PlayBook.csproj`](PlayBook.csproj.md) · [playbook.sh:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh#L7)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [playbook.sh:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh#L4)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [playbook.sh:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh#L4)

**is part of** ←

- [PlayBookOS](../overview.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
