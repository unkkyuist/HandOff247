---
generator: HandOff247
id: "op:tool.logs"
type: Operation
source: "Operations.cs"
---

# `tool.logs`

> handled by `ToolRunner.Logs`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `ToolRunner.Logs`
- **Expression in the table:** `tools.Logs(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L97)

**is handled by** →

- [`ToolRunner.cs`](../files/ToolRunner.cs.md) (ToolRunner.Logs) · [Operations.cs:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L97)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L97)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L58)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:164](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L164)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)

**is invoked by** ←

- [`tool_logs`](../tools/tool_logs.md) · [McpTools.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L58)
