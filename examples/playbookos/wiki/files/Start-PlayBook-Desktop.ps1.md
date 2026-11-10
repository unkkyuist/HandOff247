---
generator: HandOff247
id: "file:Start-PlayBook-Desktop.ps1"
type: File
source: "Start-PlayBook-Desktop.ps1"
---

# `Start-PlayBook-Desktop.ps1`

> For the desktop shortcut: starts the server if it is not running, then opens the UI.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> The PowerShell script starts the PlayBook server on port 7331, building the Release executable when it is missing. It checks that an existing server uses the same data folder, waits for startup, and optionally opens the local page in a browser.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** PowerShell
- **Kind of file:** script
- **Lines:** 34
- **Source:** [Start-PlayBook-Desktop.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [Start-PlayBook-Desktop.ps1:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1#L6)

**refers to** →

- [`PlayBook.csproj`](PlayBook.csproj.md) · [Start-PlayBook-Desktop.ps1:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1#L11)

**reads** →

- [`PLAYBOOK_HOME`](../environment.md) · [Start-PlayBook-Desktop.ps1:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1#L19)
- [`PLAYBOOK_PORT`](../environment.md) · [Start-PlayBook-Desktop.ps1:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1#L19)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [Start-PlayBook-Desktop.ps1:21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1#L21)
- [`PLAYBOOK_PORT`](../environment.md) · [Start-PlayBook-Desktop.ps1:21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1#L21)

**is part of** ←

- [PlayBookOS](../overview.md)
