---
generator: HandOff247
id: "file:portable/Start-PlayBook.ps1"
type: File
source: "portable/Start-PlayBook.ps1"
---

# `portable/Start-PlayBook.ps1`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Creates the data folder, finds an existing PlayBook server for that data location or starts one on an available localhost port from 7331 to 7360, and waits for its health check. It prints the server URL and opens it in a browser unless `-NoBrowser` is set.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** PowerShell
- **Kind of file:** script
- **Lines:** 40
- **Source:** [portable/Start-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [portable/Start-PlayBook.ps1:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1#L6)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [portable/Start-PlayBook.ps1:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1#L25)
- [`PLAYBOOK_PORT`](../environment.md) · [portable/Start-PlayBook.ps1:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1#L25)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [portable/Start-PlayBook.ps1:27](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1#L27)
- [`PLAYBOOK_PORT`](../environment.md) · [portable/Start-PlayBook.ps1:27](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1#L27)

**is part of** ←

- [`portable`](../areas/portable.md)

**is run by** ←

- [`portable/Install-PlayBook.ps1`](portable__Install-PlayBook.ps1.md) · [portable/Install-PlayBook.ps1:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L81)
- [`portable/START_PLAYBOOK.cmd`](portable__START_PLAYBOOK.cmd.md) · [portable/START_PLAYBOOK.cmd:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/START_PLAYBOOK.cmd#L2)

**is referred to by** ←

- [`portable/Install-PlayBook.ps1`](portable__Install-PlayBook.ps1.md) · [portable/Install-PlayBook.ps1:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L81)
- [`portable/START_PLAYBOOK.cmd`](portable__START_PLAYBOOK.cmd.md) · [portable/START_PLAYBOOK.cmd:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/START_PLAYBOOK.cmd#L2)
- [`scripts/check-package.py`](scripts__check-package.py.md) · [scripts/check-package.py:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L60)
