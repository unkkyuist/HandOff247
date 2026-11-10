---
generator: HandOff247
id: "file:Folders.cs"
type: File
source: "Folders.cs"
---

# `Folders.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Provides project-scoped file listing and folder operations, including folder creation and planning moves between project-relative paths. The shown code filters protected directories and links, checks path boundaries and registered references, fingerprints move sources, and prepares record updates for a planned move.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 259
- **Source:** [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs)

**defines** →

- `FolderPlan` · [Folders.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L7)
- `Folders` · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)
- `ProjectFileEntry` · [Folders.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L9)
- `in` · [Folders.cs:167](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L167)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError) · [Folders.cs:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L3)

**takes as a dependency** →

- [`Domain.cs`](Domain.cs.md) (WriteEntry) · [Folders.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L8)
- [`Store.cs`](Store.cs.md) (Store) · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)
- [`ToolRunner.cs`](ToolRunner.cs.md) (ToolRunner) · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Operations.cs`](Operations.cs.md) (Folders) · [Operations.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L20)

**handles** ←

- [`asset.files`](../operations/asset.files.md) (Folders.Files) · [Operations.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L83)
- [`folder.apply`](../operations/folder.apply.md) (Folders.Apply) · [Operations.cs:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L91)
- [`folder.list`](../operations/folder.list.md) (Folders.List) · [Operations.cs:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L88)
- [`folder.mkdir`](../operations/folder.mkdir.md) (Folders.Create) · [Operations.cs:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L89)
- [`folder.plan`](../operations/folder.plan.md) (Folders.Plan) · [Operations.cs:90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L90)
- [`folder.recover`](../operations/folder.recover.md) (Folders.Recover) · [Operations.cs:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L92)

## Defined here

- `FolderPlan` — record, [line 7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L7)
- `ProjectFileEntry` — record, [line 9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L9)
- `Folders` — class, [line 12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12) — Project-internal file operations.
- `in` — record, [line 167](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L167)
- `Folders.List` — method, [line 68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L68)
- `Folders.Files` — method, [line 80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L80)
- `Folders.Create` — method, [line 120](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L120)
- `Folders.Plan` — method, [line 198](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L198)
- `Folders.Apply` — method, [line 210](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L210)
- `Folders.Recover` — method, [line 238](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L238)
