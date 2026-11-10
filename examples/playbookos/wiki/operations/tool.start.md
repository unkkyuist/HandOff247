---
generator: HandOff247
id: "op:tool.start"
type: Operation
source: "Operations.cs"
---

# `tool.start`

> handled by `ToolRunner.Start`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `ToolRunner.Start`
- **Expression in the table:** `await tools.Start(args.Text("id"), args.Text("actor"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L95)

**is handled by** →

- [`ToolRunner.cs`](../files/ToolRunner.cs.md) (ToolRunner.Start) · [Operations.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L95)

**is documented in** ←

- [`README.md`](../files/README.md.md) (cli tool.start) · [README.md:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L68)
- [`docs/GRAPHIFY.md`](../files/docs__GRAPHIFY.md.md) (cli tool.start) · [docs/GRAPHIFY.md:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L99)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L95)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L54)
- [`portable/oz/install.py`](../files/portable__oz__install.py.md) (playbook()) · [portable/oz/install.py:302](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L302)
- [`portable/oz/oz_graphify_mcp.py`](../files/portable__oz__oz_graphify_mcp.py.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L78)
- [`scripts/graphify-playbook.py`](../files/scripts__graphify-playbook.py.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:386](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L386)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:160](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L160)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)

**is invoked by** ←

- [`start_tool`](../tools/start_tool.md) · [McpTools.cs:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L54)
