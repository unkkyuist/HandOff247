---
generator: HandOff247
id: "file:scripts/check-package.py"
type: File
source: "scripts/check-package.py"
---

# `scripts/check-package.py`

> Install the Windows package into an isolated folder and exercise its own launcher.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Installs the Windows release package into a temporary folder and exercises its CLI, installer, launcher, and stop script. It checks package hashes, upgrade preservation, health and GUI responses, and records the results in `artifacts/package-check.json`.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 77
- **Source:** [scripts/check-package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/check-package.py:37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L37)

**refers to** →

- [`portable/Install-PlayBook.ps1`](portable__Install-PlayBook.ps1.md) · [scripts/check-package.py:31](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L31)
- [`portable/Start-PlayBook.ps1`](portable__Start-PlayBook.ps1.md) · [scripts/check-package.py:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L60)
- [`portable/Stop-PlayBook.ps1`](portable__Stop-PlayBook.ps1.md) · [scripts/check-package.py:73](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L73)

**calls** →

- [`connection.status`](../operations/connection.status.md) (cli(), by starting a process) · [scripts/check-package.py:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L43)
- [`get`](../operations/get.md) (cli(), by starting a process) · [scripts/check-package.py:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L59)
- [`info`](../operations/info.md) (cli(), by starting a process) · [scripts/check-package.py:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L42)
- [`scan`](../operations/scan.md) (cli(), by starting a process) · [scripts/check-package.py:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L44)
- [`scan.import`](../operations/scan.import.md) (cli(), by starting a process) · [scripts/check-package.py:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L45)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

## Defined here

- `check` — function, [line 14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L14)
- `powershell` — function, [line 18](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L18)
