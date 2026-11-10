---
generator: HandOff247
id: "file:Operations.cs"
type: File
source: "Operations.cs"
---

# `Operations.cs`

> The single place new features plug into. AGENTS.md: use this shared Operations service for CLI/GUI/MCP features and do not add a second data authority.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 113
- **Source:** [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs)

**Notes from the previous owner**

> The single place new features plug into. AGENTS.md: use this shared Operations service for CLI/GUI/MCP features and do not add a second data authority.

**defines** →

- [`Operations.Execute`](../operations.md) · [Operations.cs:33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L33)
- `Operations` · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)

**uses** →

- [`AgentWorker.cs`](AgentWorker.cs.md) (AgentWorker) · [Operations.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L6)
- [`Desktop.cs`](Desktop.cs.md) (Desktop) · [Operations.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L80)
- [`Domain.cs`](Domain.cs.md) (Json, DomainError, WriteEntry) · [Operations.cs:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L1)
- [`Folders.cs`](Folders.cs.md) (Folders) · [Operations.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L20)
- [`Harnesses.cs`](Harnesses.cs.md) (Harnesses) · [Operations.cs:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L25)
- [`Library.cs`](Library.cs.md) (Library) · [Operations.cs:23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L23)
- [`Ontology.cs`](Ontology.cs.md) (Ontology) · [Operations.cs:24](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L24)
- [`Orchestration.cs`](Orchestration.cs.md) (Orchestration) · [Operations.cs:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L22)
- [`ProjectScanner.cs`](ProjectScanner.cs.md) (ProjectScanner) · [Operations.cs:21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L21)

**takes as a dependency** →

- [`Access.cs`](Access.cs.md) (Access) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`Connection.cs`](Connection.cs.md) (Connection) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`Providers.cs`](Providers.cs.md) (Providers) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`Store.cs`](Store.cs.md) (Store) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`ToolRunner.cs`](ToolRunner.cs.md) (ToolRunner) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)

**refers to** →

- [`docs/API.md`](docs__API.md.md) · [Operations.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L99)

**reads** →

- [`PLAYBOOK_RUN_ID`](../environment.md) · [Operations.cs:13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L13)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Program.cs`](Program.cs.md) (Operations) · [Program.cs:14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L14)

**is a dependency of** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (Operations) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`McpTools.cs`](McpTools.cs.md) (Operations) · [McpTools.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L6)

**handles** ←

- [`connection.configure`](../operations/connection.configure.md) (Operations.Configure) · [Operations.cs:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L60)

## Defined here

- `Operations` — class, [line 4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- `Operations.LocalOperation` — method, [line 8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L8)
- `Operations.Execute` — method, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L11)
