---
generator: HandOff247
id: "file:portable/Install-PlayBook.ps1"
type: File
source: "portable/Install-PlayBook.ps1"
---

# `portable/Install-PlayBook.ps1`

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** PowerShell
- **Kind of file:** script
- **Lines:** 81
- **Source:** [portable/Install-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [portable/Install-PlayBook.ps1:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L59)
- [`portable/Start-PlayBook.ps1`](portable__Start-PlayBook.ps1.md) · [portable/Install-PlayBook.ps1:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L81)

**refers to** →

- [`portable/Start-PlayBook.ps1`](portable__Start-PlayBook.ps1.md) · [portable/Install-PlayBook.ps1:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L81)

**calls** →

- [`connection.configure`](../operations/connection.configure.md) (cli connection.configure, by starting a process) · [portable/Install-PlayBook.ps1:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L67)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [portable/Install-PlayBook.ps1:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L60)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [portable/Install-PlayBook.ps1:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L62)

**is part of** ←

- [`portable`](../areas/portable.md)

**is run by** ←

- [`portable/INSTALL_PLAYBOOK.cmd`](portable__INSTALL_PLAYBOOK.cmd.md) · [portable/INSTALL_PLAYBOOK.cmd:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/INSTALL_PLAYBOOK.cmd#L2)

**is referred to by** ←

- [`portable/INSTALL_PLAYBOOK.cmd`](portable__INSTALL_PLAYBOOK.cmd.md) · [portable/INSTALL_PLAYBOOK.cmd:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/INSTALL_PLAYBOOK.cmd#L2)
- [`scripts/check-package.py`](scripts__check-package.py.md) · [scripts/check-package.py:31](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L31)
