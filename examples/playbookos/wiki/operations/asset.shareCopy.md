---
generator: HandOff247
id: "op:asset.shareCopy"
type: Operation
source: "Operations.cs"
---

# `asset.shareCopy`

> handled by `Workspace.ShareAsset`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.ShareAsset`
- **Expression in the table:** `workspace.ShareAsset(args.Text("projectId"), args.Text("path"), args.Text("actor"), args.Text("reason"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L85)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.ShareAsset) · [Operations.cs:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L85)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L85)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L46)

**is invoked by** ←

- [`share_project_asset`](../tools/share_project_asset.md) · [McpTools.cs:46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L46)
