---
generator: HandOff247
id: "op:git"
type: Operation
source: "Operations.cs"
---

# `git`

> handled by `Workspace.Git`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.Git`
- **Expression in the table:** `await workspace.Git(args.Text("projectId"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L81)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.Git) · [Operations.cs:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L81)

**is documented in** ←

- [`README.md`](../files/README.md.md) (cli git) · [README.md:65](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L65)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L81)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L38)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L63)

**is invoked by** ←

- [`git`](../tools/git.md) · [McpTools.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L38)
