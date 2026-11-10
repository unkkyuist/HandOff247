---
generator: HandOff247
id: "op:asset.files"
type: Operation
source: "Operations.cs"
---

# `asset.files`

> handled by `Folders.Files`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Folders.Files`
- **Expression in the table:** `folders.Files(args.Text("projectId"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L83)

**is handled by** →

- [`Folders.cs`](../files/Folders.cs.md) (Folders.Files) · [Operations.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L83)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L83)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L42)
- [`wwwroot/assets.js`](../files/wwwroot__assets.js.md) (api(), over HTTP) · [wwwroot/assets.js:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L22) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`project_files`](../tools/project_files.md) · [McpTools.cs:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L42)
