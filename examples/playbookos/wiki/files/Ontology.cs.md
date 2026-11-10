---
generator: HandOff247
id: "file:Ontology.cs"
type: File
source: "Ontology.cs"
---

# `Ontology.cs`

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 505
- **Source:** [Ontology.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs)

**defines** →

- `Ontology` · [Ontology.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L11)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, WriteEntry) · [Ontology.cs:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L5)

**takes as a dependency** →

- [`Domain.cs`](Domain.cs.md) (Entry) · [Ontology.cs:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L17)
- [`Store.cs`](Store.cs.md) (Store) · [Ontology.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L11)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Operations.cs`](Operations.cs.md) (Ontology) · [Operations.cs:24](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L24)
- [`Orchestration.cs`](Orchestration.cs.md) (Ontology) · [Orchestration.cs:137](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L137)
- [`Store.cs`](Store.cs.md) (Ontology) · [Store.cs:118](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L118)
- [`Workspace.cs`](Workspace.cs.md) (Ontology) · [Workspace.cs:156](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L156)

**handles** ←

- [`ontology.connect`](../operations/ontology.connect.md) (Ontology.Connect) · [Operations.cs:48](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L48)
- [`ontology.connections`](../operations/ontology.connections.md) (Ontology.Connections) · [Operations.cs:47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L47)
- [`ontology.ingest`](../operations/ontology.ingest.md) (Ontology.Ingest) · [Operations.cs:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L43)
- [`ontology.rebuild`](../operations/ontology.rebuild.md) (Ontology.Rebuild) · [Operations.cs:50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L50)
- [`ontology.reference`](../operations/ontology.reference.md) (Ontology.Reference) · [Operations.cs:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L45)
- [`ontology.search`](../operations/ontology.search.md) (Ontology.Search) · [Operations.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L44)
- [`ontology.sync`](../operations/ontology.sync.md) (Ontology.Sync) · [Operations.cs:49](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L49)
- [`ontology.usage`](../operations/ontology.usage.md) (Ontology.Usage) · [Operations.cs:46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L46)

## Defined here

- `Ontology` — class, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L11) — Ontology is a projection and a source ledger inside Store, never a second database.
- `Ontology.Validate` — method, [line 56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L56)
- `Ontology.CompactEntry` — method, [line 134](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L134)
- `Ontology.CompactReference` — method, [line 171](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L171) — Prompt references are excerpts.
- `Ontology.ProjectRecord` — method, [line 221](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L221)
- `Ontology.Ingest` — method, [line 317](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L317)
- `Ontology.Search` — method, [line 361](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L361)
- `Ontology.Reference` — method, [line 369](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L369)
- `Ontology.Usage` — method, [line 390](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L390)
- `Ontology.Connections` — method, [line 426](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L426)
- `Ontology.Connect` — method, [line 432](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L432)
- `Ontology.Sync` — method, [line 444](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L444)
- `Ontology.Rebuild` — method, [line 492](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L492)
