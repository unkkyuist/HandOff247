---
generator: HandOff247
id: "file:ToolRunner.cs"
type: File
source: "ToolRunner.cs"
---

# `ToolRunner.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> ToolRunner reads local tool definitions, reports process and HTTP status, and starts or stops tool processes it owns. It records run state and audit entries, and exposes recent log output for each registered tool.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 132
- **Source:** [ToolRunner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs)

**defines** →

- `RunState` · [ToolRunner.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L9)
- `ToolDefinition` · [ToolRunner.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L6)
- `ToolRunner` · [ToolRunner.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L11)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError) · [ToolRunner.cs:14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L14)

**takes as a dependency** →

- [`Store.cs`](Store.cs.md) (Store) · [ToolRunner.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L11)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (RunState) · [AgentWorker.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L72)
- [`Program.cs`](Program.cs.md) (ToolRunner) · [Program.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L9)

**is a dependency of** ←

- [`Folders.cs`](Folders.cs.md) (ToolRunner) · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)
- [`Operations.cs`](Operations.cs.md) (ToolRunner) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)

**handles** ←

- [`tool.logs`](../operations/tool.logs.md) (ToolRunner.Logs) · [Operations.cs:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L97)
- [`tool.start`](../operations/tool.start.md) (ToolRunner.Start) · [Operations.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L95)
- [`tool.status`](../operations/tool.status.md) (ToolRunner.Status) · [Operations.cs:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L94)
- [`tool.stop`](../operations/tool.stop.md) (ToolRunner.Stop) · [Operations.cs:96](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L96)
- [`tools`](../operations/tools.md) (ToolRunner.Definitions) · [Operations.cs:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L93)

## Defined here

- `ToolDefinition` — record, [line 6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L6)
- `RunState` — record, [line 9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L9)
- `ToolRunner` — class, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L11)
- `ToolRunner.Definitions` — method, [line 13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L13)
- `ToolRunner.RunsList` — method, [line 18](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L18)
- `ToolRunner.Status` — method, [line 25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L25)
- `ToolRunner.Start` — method, [line 43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L43)
- `ToolRunner.Stop` — method, [line 85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L85)
- `ToolRunner.Logs` — method, [line 102](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L102)
- `ToolRunner.Worker` — method, [line 111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L111)
