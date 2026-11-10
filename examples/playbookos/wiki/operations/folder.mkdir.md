---
generator: HandOff247
id: "op:folder.mkdir"
type: Operation
source: "Operations.cs"
---

# `folder.mkdir`

> handled by `Folders.Create`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Folders.Create`
- **Expression in the table:** `folders.Create(args.Text("projectId"), args.Text("path"), args.Text("actor"), args.Text("reason"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L89)

**is handled by** →

- [`Folders.cs`](../files/Folders.cs.md) (Folders.Create) · [Operations.cs:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L89)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L89)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L66)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:26](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L26)
- [`wwwroot/folders.js`](../files/wwwroot__folders.js.md) (api(), over HTTP) · [wwwroot/folders.js:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js#L74) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`create_folder`](../tools/create_folder.md) · [McpTools.cs:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L66)
