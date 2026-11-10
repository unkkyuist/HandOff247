---
generator: HandOff247
id: "file:Orchestration.cs"
type: File
source: "Orchestration.cs"
---

# `Orchestration.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Stores worker registrations and AI runs in the revisioned Store, queues work with project, permission, dependency, and delegation checks, and provides state, claim, heartbeat, and cancellation operations. Claiming work checks worker availability and run constraints, then supplies project context, dependency outputs, and ontology references; the excerpt ends partway through heartbeat handling.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 196
- **Source:** [Orchestration.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs)

**defines** →

- `Orchestration` · [Orchestration.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry) · [Orchestration.cs:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L3)
- [`Harnesses.cs`](Harnesses.cs.md) (Harnesses) · [Orchestration.cs:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L76)
- [`Ontology.cs`](Ontology.cs.md) (Ontology) · [Orchestration.cs:137](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L137)

**takes as a dependency** →

- [`Store.cs`](Store.cs.md) (Store) · [Orchestration.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [Orchestration.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Harnesses.cs`](Harnesses.cs.md) (Orchestration) · [Harnesses.cs:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L111)
- [`Operations.cs`](Operations.cs.md) (Orchestration) · [Operations.cs:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L22)

**handles** ←

- [`agent.register`](../operations/agent.register.md) (Orchestration.Register) · [Operations.cs:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L67)
- [`orchestration.state`](../operations/orchestration.state.md) (Orchestration.State) · [Operations.cs:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L68)
- [`run.cancel`](../operations/run.cancel.md) (Orchestration.Cancel) · [Operations.cs:73](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L73)
- [`run.claim`](../operations/run.claim.md) (Orchestration.Claim) · [Operations.cs:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L70)
- [`run.complete`](../operations/run.complete.md) (Orchestration.Heartbeat) · [Operations.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L72)
- [`run.enqueue`](../operations/run.enqueue.md) (Orchestration.Enqueue) · [Operations.cs:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L69)
- [`run.heartbeat`](../operations/run.heartbeat.md) (Orchestration.Heartbeat) · [Operations.cs:71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L71)

## Defined here

- `Orchestration` — class, [line 8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8) — Queue, leases and results live in the same revisioned, audited ledger as projects.
- `Orchestration.Register` — method, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L22)
- `Orchestration.Enqueue` — method, [line 37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L37)
- `Orchestration.Enqueue` — method, [line 42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L42)
- `Orchestration.State` — method, [line 103](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L103)
- `Orchestration.Claim` — method, [line 110](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L110)
- `Orchestration.Heartbeat` — method, [line 152](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L152)
- `Orchestration.Cancel` — method, [line 187](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L187)
