---
generator: HandOff247
id: "op:library.list"
type: Operation
source: "Operations.cs"
---

# `library.list`

> handled by `Library.List`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Library.List`
- **Expression in the table:** `library.List()`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L74)

**is handled by** →

- [`Library.cs`](../files/Library.cs.md) (Library.List) · [Operations.cs:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L74)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L74)

**is called from** ←

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (Execute(), in-process) · [AgentWorker.cs:101](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L101)
- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L97)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:133](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L133) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`shared_assets`](../tools/shared_assets.md) · [McpTools.cs:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L97)
