---
generator: HandOff247
id: "file:Program.cs"
type: File
source: "Program.cs"
---

# `Program.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Initializes PlayBook services and selects worker, CLI, MCP, agent, local web server, or shared server behavior from the command-line mode. In server modes it configures the HTTP endpoints, access checks, API operation dispatch, media preview, health response, and MCP transport.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 111
- **Source:** [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

**defines** →

- [`agent`](../modes/agent.md) · [Program.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L41)
- [`cli`](../modes/cli.md) · [Program.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L20)
- [`mcp`](../modes/mcp.md) · [Program.cs:33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L33)
- [`serve`](../modes/serve.md) · [Program.cs:49](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L49)
- [`server`](../modes/server.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`worker`](../modes/worker.md) · [Program.cs:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L19)
- [`GET /health`](../routes.md) · [Program.cs:108](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L108)
- [`GET /session`](../routes.md) · [Program.cs:98](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L98)
- [`MCP /mcp`](../routes.md) · [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)
- [`POST /api/{operation}`](../routes.md) · [Program.cs:100](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L100)
- [`POST /auth/login`](../routes.md) · [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)
- [`POST /media/{projectId}`](../routes.md) · [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

**uses** →

- [`Access.cs`](Access.cs.md) (Access) · [Program.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L12)
- [`AgentWorker.cs`](AgentWorker.cs.md) (AgentWorker) · [Program.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L44)
- [`Connection.cs`](Connection.cs.md) (Connection) · [Program.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L11)
- [`Domain.cs`](Domain.cs.md) (Json, DomainError) · [Program.cs:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L2)
- [`Library.cs`](Library.cs.md) (Library) · [Program.cs:105](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L105)
- [`McpTools.cs`](McpTools.cs.md) (McpTools) · [Program.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L38)
- [`Operations.cs`](Operations.cs.md) (Operations) · [Program.cs:14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L14)
- [`Providers.cs`](Providers.cs.md) (Providers) · [Program.cs:13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L13)
- [`Store.cs`](Store.cs.md) (Store) · [Program.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L7)
- [`ToolRunner.cs`](ToolRunner.cs.md) (ToolRunner) · [Program.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L9)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [Program.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L8)

**refers to** →

- [`docs/PORTABLE-AND-AGENTS.md`](docs__PORTABLE-AND-AGENTS.md.md) · [Program.cs:50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L50)

**reads** →

- [`PLAYBOOK_BIND`](../environment.md) · [Program.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L58)
- [`PLAYBOOK_HOME`](../environment.md) · [Program.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L6)
- [`PLAYBOOK_PORT`](../environment.md) · [Program.cs:57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L57)
- [`PLAYBOOK_PUBLIC_URL`](../environment.md) · [Program.cs:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L74)

**mentions** →

- [`7331`](../ports.md) (PLAYBOOK_PORT default) · [Program.cs:57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L57)

**is part of** ←

- [PlayBookOS](../overview.md)
