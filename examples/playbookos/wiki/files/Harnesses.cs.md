---
generator: HandOff247
id: "file:Harnesses.cs"
type: File
source: "Harnesses.cs"
---

# `Harnesses.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Stores project harness proposals, trial snapshots, comparisons, and reviewed adoption or disablement in the project store. It enqueues paired read-only trial runs, checks revisions and evidence before adoption, and records reviewed lessons as research entries.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 181
- **Source:** [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs)

**defines** →

- `Harnesses` · [Harnesses.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry, WriteEntry) · [Harnesses.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L4)
- [`Orchestration.cs`](Orchestration.cs.md) (Orchestration) · [Harnesses.cs:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L111)

**takes as a dependency** →

- [`Store.cs`](Store.cs.md) (Store) · [Harnesses.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [Harnesses.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10)

**reads** →

- [`PLAYBOOK_RUN_ID`](../environment.md) · [Harnesses.cs:170](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L170)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Operations.cs`](Operations.cs.md) (Harnesses) · [Operations.cs:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L25)
- [`Orchestration.cs`](Orchestration.cs.md) (Harnesses) · [Orchestration.cs:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L76)
- [`Store.cs`](Store.cs.md) (Harnesses) · [Store.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L80)

**handles** ←

- [`harness.adopt`](../operations/harness.adopt.md) (Harnesses.Adopt) · [Operations.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L41)
- [`harness.compare`](../operations/harness.compare.md) (Harnesses.Compare) · [Operations.cs:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L40)
- [`harness.disable`](../operations/harness.disable.md) (Harnesses.Disable) · [Operations.cs:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L42)
- [`harness.probe`](../operations/harness.probe.md) (Harnesses.Probe) · [Operations.cs:39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L39)
- [`harness.propose`](../operations/harness.propose.md) (Harnesses.Propose) · [Operations.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L38)
- [`harness.state`](../operations/harness.state.md) (Harnesses.State) · [Operations.cs:37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L37)

## Defined here

- `Harnesses` — class, [line 10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10) — A bounded, native adaptation of Harness²'s propose/probe/compose/reflection loop.
- `Harnesses.Active` — method, [line 30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L30)
- `Harnesses.Snapshot` — method, [line 38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L38)
- `Harnesses.Validate` — method, [line 43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L43)
- `Harnesses.State` — method, [line 60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L60)
- `Harnesses.Propose` — method, [line 69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L69)
- `Harnesses.Probe` — method, [line 87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L87)
- `Harnesses.Compare` — method, [line 129](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L129)
- `Harnesses.Adopt` — method, [line 137](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L137)
- `Harnesses.Disable` — method, [line 174](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L174)
