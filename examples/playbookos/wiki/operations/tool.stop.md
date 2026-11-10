---
generator: HandOff247
id: "op:tool.stop"
type: Operation
source: "Operations.cs"
---

# `tool.stop`

> handled by `ToolRunner.Stop`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `ToolRunner.Stop`
- **Expression in the table:** `tools.Stop(args.Text("id"), args.Text("actor"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:96](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L96)

**is handled by** →

- [`ToolRunner.cs`](../files/ToolRunner.cs.md) (ToolRunner.Stop) · [Operations.cs:96](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L96)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:96](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L96)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L56)
- [`portable/oz/install.py`](../files/portable__oz__install.py.md) (playbook()) · [portable/oz/install.py:209](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L209)
- [`scripts/oz-package-smoke.py`](../files/scripts__oz-package-smoke.py.md) (playbook()) · [scripts/oz-package-smoke.py:186](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L186)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:166](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L166)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)

**is invoked by** ←

- [`stop_tool`](../tools/stop_tool.md) · [McpTools.cs:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L56)
