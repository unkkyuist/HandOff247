---
generator: HandOff247
id: "file:AgentWorker.cs"
type: File
source: "AgentWorker.cs"
---

# `AgentWorker.cs`

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 196
- **Source:** [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs)

**defines** →

- `AgentWorker` · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry) · [AgentWorker.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L4)
- [`ProjectScanner.cs`](ProjectScanner.cs.md) (ProjectScanner) · [AgentWorker.cs:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L94)
- [`ToolRunner.cs`](ToolRunner.cs.md) (RunState) · [AgentWorker.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L72)

**takes as a dependency** →

- [`Connection.cs`](Connection.cs.md) (Connection) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Operations.cs`](Operations.cs.md) (Operations) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Providers.cs`](Providers.cs.md) (Providers) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Store.cs`](Store.cs.md) (Store) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [AgentWorker.cs:186](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L186)

**calls** →

- [`agent.register`](../operations/agent.register.md) (Execute(), in-process) · [AgentWorker.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L41)
- [`library.list`](../operations/library.list.md) (Execute(), in-process) · [AgentWorker.cs:101](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L101)
- [`run.claim`](../operations/run.claim.md) (Execute(), in-process) · [AgentWorker.cs:47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L47)
- [`run.complete`](../operations/run.complete.md) (Execute(), in-process) · [AgentWorker.cs:177](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L177)
- [`run.heartbeat`](../operations/run.heartbeat.md) (Execute(), in-process) · [AgentWorker.cs:155](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L155)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Operations.cs`](Operations.cs.md) (AgentWorker) · [Operations.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L6)
- [`Program.cs`](Program.cs.md) (AgentWorker) · [Program.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L44)

**handles** ←

- [`worker.configure`](../operations/worker.configure.md) (AgentWorker.Configure) · [Operations.cs:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L66)
- [`worker.status`](../operations/worker.status.md) (AgentWorker.Status) · [Operations.cs:65](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L65)

## Defined here

- `AgentWorker` — class, [line 8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- `AgentWorker.Status` — method, [line 12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L12)
- `AgentWorker.Configure` — method, [line 13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L13)
