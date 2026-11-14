---
generator: HandOff247
id: "mode:server"
type: Mode
source: "Program.cs"
---

# `server`

> Central multi-PC server. Needs its own `PLAYBOOK_HOME` and an account created with `cli server.setup` first.

- **Class:** Run mode — A way to start the program, picked by its first argument.
- **Transports:** MCP over HTTP, HTTP server, background service
- **Source:** [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)

**Notes from the previous owner**

> Central multi-PC server. Needs its own `PLAYBOOK_HOME` and an account created with `cli server.setup` first.

**uses** →

- [`Access`](../files/Access.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`AgentWorker`](../files/AgentWorker.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`Connection`](../files/Connection.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`DomainError`](../files/Domain.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`Json`](../files/Domain.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`Library`](../files/Library.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`McpTools`](../files/McpTools.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`Operations`](../files/Operations.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`Store`](../files/Store.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
- [`Workspace`](../files/Workspace.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)

**serves** →

- [`Operations.Execute`](../operations.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)

**exposes** →

- [`GET /health`](../features/GET-__health.md) · [Program.cs:108](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L108)
- [`GET /session`](../features/GET-__session.md) · [Program.cs:98](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L98)
- [`MCP /mcp`](../features/MCP-__mcp.md) · [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)
- [`POST /api/{operation}`](../features/POST-__api__-operation.md) · [Program.cs:100](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L100)
- [`POST /auth/login`](../features/POST-__auth__login.md) · [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)
- [`POST /media/{projectId}`](../features/POST-__media__-projectId.md) · [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

**is defined in** ←

- [`Program.cs`](../files/Program.cs.md) · [Program.cs:15](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L15)
