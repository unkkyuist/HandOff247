---
generator: HandOff247
id: "file:Providers.cs"
type: File
source: "Providers.cs"
---

# `Providers.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Providers locates the Codex or Claude CLI, checks installation and login status, and can open a login process on Windows. It also builds MCP configuration and provider-specific process arguments for running a PlayBook job.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 124
- **Source:** [Providers.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs)

**defines** →

- `ProviderCommand` · [Providers.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L8)
- `ProviderStatus` · [Providers.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L9)
- `Providers` · [Providers.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L11)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry) · [Providers.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L4)

**takes as a dependency** →

- [`Store.cs`](Store.cs.md) (Store) · [Providers.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L11)

**refers to** →

- [`examples/mcp.json`](examples__mcp.json.md) · [Providers.cs:113](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L113)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [Providers.cs:120](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L120)
- [`PLAYBOOK_RUN_ID`](../environment.md) · [Providers.cs:121](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L121)

**starts** →

- [`powershell`](../commands.md) · [Providers.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L80)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Program.cs`](Program.cs.md) (Providers) · [Program.cs:13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L13)

**is a dependency of** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (Providers) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Operations.cs`](Operations.cs.md) (Providers) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)

**handles** ←

- [`provider.login`](../operations/provider.login.md) (Providers.Login) · [Operations.cs:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L63)
- [`provider.mcp`](../operations/provider.mcp.md) (Providers.McpConfig) · [Operations.cs:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L64)
- [`provider.status`](../operations/provider.status.md) (Providers.All) · [Operations.cs:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L62)

## Defined here

- `ProviderCommand` — record, [line 8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L8)
- `ProviderStatus` — record, [line 9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L9)
- `Providers` — class, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L11)
- `Providers.Self` — method, [line 13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L13)
- `Providers.Find` — method, [line 19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L19)
- `Providers.StartInfo` — method, [line 39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L39)
- `Providers.Status` — method, [line 57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L57)
- `Providers.All` — method, [line 71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L71)
- `Providers.Login` — method, [line 72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L72)
- `Providers.McpConfig` — method, [line 84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L84)
- `Providers.Run` — method, [line 90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L90)
