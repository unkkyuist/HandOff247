---
generator: HandOff247
id: "op:export"
type: Operation
source: "Operations.cs"
---

# `export`

> handled by `Workspace.Export`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.Export`
- **Expression in the table:** `workspace.Export(args.Text("projectId"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L86)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.Export) · [Operations.cs:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L86)

**is documented in** ←

- [`README.md`](../files/README.md.md) (cli export) · [README.md:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L69)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L86)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:48](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L48)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L81)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L63)

**is invoked by** ←

- [`export`](../tools/export.md) · [McpTools.cs:48](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L48)
