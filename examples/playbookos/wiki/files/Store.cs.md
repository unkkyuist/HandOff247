---
generator: HandOff247
id: "file:Store.cs"
type: File
source: "Store.cs"
---

# `Store.cs`

> All record changes must pass validation here and write an audit event in the same transaction (AGENTS.md).

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 183
- **Source:** [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs)

**Notes from the previous owner**

> All record changes must pass validation here and write an audit event in the same transaction (AGENTS.md).

**defines** →

- `Store` · [Store.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L6)

**uses** →

- [`Connection.cs`](Connection.cs.md) (Connection) · [Store.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L9)
- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry, WriteEntry, Change) · [Store.cs:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L2)
- [`Harnesses.cs`](Harnesses.cs.md) (Harnesses) · [Store.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L80)
- [`Ontology.cs`](Ontology.cs.md) (Ontology) · [Store.cs:118](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L118)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Program.cs`](Program.cs.md) (Store) · [Program.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L7)

**is a dependency of** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (Store) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Folders.cs`](Folders.cs.md) (Store) · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)
- [`Harnesses.cs`](Harnesses.cs.md) (Store) · [Harnesses.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10)
- [`Library.cs`](Library.cs.md) (Store) · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)
- [`Ontology.cs`](Ontology.cs.md) (Store) · [Ontology.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L11)
- [`Operations.cs`](Operations.cs.md) (Store) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`Orchestration.cs`](Orchestration.cs.md) (Store) · [Orchestration.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8)
- [`ProjectScanner.cs`](ProjectScanner.cs.md) (Store) · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)
- [`Providers.cs`](Providers.cs.md) (Store) · [Providers.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L11)
- [`ToolRunner.cs`](ToolRunner.cs.md) (Store) · [ToolRunner.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L11)
- [`Workspace.cs`](Workspace.cs.md) (Store) · [Workspace.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L8)

**handles** ←

- [`backup`](../operations/backup.md) (Store.Backup) · [Operations.cs:87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L87)
- [`canon.approve`](../operations/canon.approve.md) (Store.Approve) · [Operations.cs:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L53)
- [`events`](../operations/events.md) (Store.Events) · [Operations.cs:52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L52)
- [`get`](../operations/get.md) (Store.Get) · [Operations.cs:35](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L35)
- [`list`](../operations/list.md) (Store.List) · [Operations.cs:34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L34)
- [`save`](../operations/save.md) (Store.Save) · [Operations.cs:36](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L36)

## Defined here

- `Store` — class, [line 6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L6)
- `Store.Open` — method, [line 32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L32)
- `Store.List` — method, [line 40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L40)
- `Store.Get` — method, [line 56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L56)
- `Store.Get` — method, [line 62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L62)
- `Store.Save` — method, [line 68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L68)
- `Store.Save` — method, [line 74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L74)
- `Store.Approve` — method, [line 141](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L141)
- `Store.Events` — method, [line 167](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L167)
- `Store.Backup` — method, [line 176](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L176)
