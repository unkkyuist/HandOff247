---
generator: HandOff247
id: "op:provider.mcp"
type: Operation
source: "Operations.cs"
---

# `provider.mcp`

> handled by `Providers.McpConfig`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Providers.McpConfig`
- **Expression in the table:** `providers.McpConfig()`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L64)

**is handled by** →

- [`Providers.cs`](../files/Providers.cs.md) (Providers.McpConfig) · [Operations.cs:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L64)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L64)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L88) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
