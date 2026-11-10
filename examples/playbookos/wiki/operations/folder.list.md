---
generator: HandOff247
id: "op:folder.list"
type: Operation
source: "Operations.cs"
---

# `folder.list`

> handled by `Folders.List`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Folders.List`
- **Expression in the table:** `folders.List(args.Text("projectId"), args.Text("path"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L88)

**is handled by** →

- [`Folders.cs`](../files/Folders.cs.md) (Folders.List) · [Operations.cs:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L88)

**is documented in** ←

- [`docs/CLAUDE-AND-FOLDERS.md`](../files/docs__CLAUDE-AND-FOLDERS.md.md) (cli folder.list) · [docs/CLAUDE-AND-FOLDERS.md:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L42)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L88)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L64)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L74)
- [`wwwroot/folders.js`](../files/wwwroot__folders.js.md) (api(), over HTTP) · [wwwroot/folders.js:26](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js#L26) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`list_folder`](../tools/list_folder.md) · [McpTools.cs:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L64)
