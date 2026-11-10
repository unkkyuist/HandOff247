---
generator: HandOff247
id: "op:tool.status"
type: Operation
source: "Operations.cs"
---

# `tool.status`

> handled by `ToolRunner.Status`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `ToolRunner.Status`
- **Expression in the table:** `await tools.Status(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L94)

**is handled by** →

- [`ToolRunner.cs`](../files/ToolRunner.cs.md) (ToolRunner.Status) · [Operations.cs:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L94)

**is documented in** ←

- [`README.md`](../files/README.md.md) (cli tool.status) · [README.md:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L67)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L94)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L52)
- [`portable/oz/install.py`](../files/portable__oz__install.py.md) (playbook()) · [portable/oz/install.py:296](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L296)
- [`portable/oz/oz_graphify_mcp.py`](../files/portable__oz__oz_graphify_mcp.py.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L76)
- [`scripts/graphify-playbook.py`](../files/scripts__graphify-playbook.py.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:383](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L383)
- [`scripts/oz-package-smoke.py`](../files/scripts__oz-package-smoke.py.md) (playbook()) · [scripts/oz-package-smoke.py:185](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L185)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:162](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L162)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)

**is invoked by** ←

- [`tool_status`](../tools/tool_status.md) · [McpTools.cs:52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L52)
