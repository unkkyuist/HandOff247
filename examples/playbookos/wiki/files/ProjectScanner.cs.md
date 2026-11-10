---
generator: HandOff247
id: "file:ProjectScanner.cs"
type: File
source: "ProjectScanner.cs"
---

# `ProjectScanner.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> ProjectScanner recursively scans a selected folder, skips configured directory names and links, and records candidate folders with project markers, file names, instruction files, and any existing registration. Import validates selected candidates against the saved scan, preserves existing registrations, and creates project records for new selections.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 84
- **Source:** [ProjectScanner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs)

**defines** →

- `ProjectCandidate` · [ProjectScanner.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L7)
- `ProjectScan` · [ProjectScanner.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L8)
- `ProjectScanner` · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry) · [ProjectScanner.cs:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L3)

**takes as a dependency** →

- [`Connection.cs`](Connection.cs.md) (Connection) · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)
- [`Store.cs`](Store.cs.md) (Store) · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [ProjectScanner.cs:14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L14)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (ProjectScanner) · [AgentWorker.cs:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L94)
- [`Operations.cs`](Operations.cs.md) (ProjectScanner) · [Operations.cs:21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L21)

**handles** ←

- [`scan`](../operations/scan.md) (ProjectScanner.Scan) · [Operations.cs:55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L55)
- [`scan.import`](../operations/scan.import.md) (ProjectScanner.Import) · [Operations.cs:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L56)

## Defined here

- `ProjectCandidate` — record, [line 7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L7)
- `ProjectScan` — record, [line 8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L8)
- `ProjectScanner` — class, [line 10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)
- `ProjectScanner.Scan` — method, [line 16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L16)
- `ProjectScanner.Import` — method, [line 54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L54)
- `ProjectScanner.CheckLinks` — method, [line 79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L79)
