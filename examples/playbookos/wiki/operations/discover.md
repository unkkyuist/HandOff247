---
generator: HandOff247
id: "op:discover"
type: Operation
source: "Operations.cs"
---

# `discover`

> handled by `Workspace.Discover`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.Discover`
- **Expression in the table:** `workspace.Discover(args.Text("root"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L54)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.Discover) · [Operations.cs:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L54)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L54)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L60)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L86)

**is invoked by** ←

- [`discover`](../tools/discover.md) · [McpTools.cs:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L60)
