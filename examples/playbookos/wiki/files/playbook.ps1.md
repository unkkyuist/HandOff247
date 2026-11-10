---
generator: HandOff247
id: "file:playbook.ps1"
type: File
source: "playbook.ps1"
---

# `playbook.ps1`

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** PowerShell
- **Kind of file:** script
- **Lines:** 10
- **Source:** [playbook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [playbook.ps1:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1#L4)

**refers to** →

- [`PlayBook.csproj`](PlayBook.csproj.md) · [playbook.ps1:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1#L6)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [playbook.ps1:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1#L3)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [playbook.ps1:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1#L3)

**starts** →

- [`dotnet`](../commands.md) · [playbook.ps1:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1#L10)

**is part of** ←

- [PlayBookOS](../overview.md)

**is run by** ←

- [`START_PLAYBOOK.cmd`](START_PLAYBOOK.cmd.md) (serve) · [START_PLAYBOOK.cmd:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_PLAYBOOK.cmd#L3)

**is referred to by** ←

- [`START_PLAYBOOK.cmd`](START_PLAYBOOK.cmd.md) · [START_PLAYBOOK.cmd:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_PLAYBOOK.cmd#L3)
- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
