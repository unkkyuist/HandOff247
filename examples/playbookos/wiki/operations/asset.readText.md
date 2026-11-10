---
generator: HandOff247
id: "op:asset.readText"
type: Operation
source: "Operations.cs"
---

# `asset.readText`

> handled by `Workspace.ReadText`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.ReadText`
- **Expression in the table:** `workspace.ReadText(args.Text("projectId"), args.Text("path"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L84)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.ReadText) · [Operations.cs:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L84)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L84)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L44)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:73](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L73)
- [`wwwroot/media.js`](../files/wwwroot__media.js.md) (api(), over HTTP) · [wwwroot/media.js:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L68) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`read_project_text`](../tools/read_project_text.md) · [McpTools.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L44)
