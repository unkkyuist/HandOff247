---
generator: HandOff247
id: "op:canon.approve"
type: Operation
source: "Operations.cs"
---

# `canon.approve`

> handled by `Store.Approve`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Store.Approve`
- **Expression in the table:** `store.Approve(args.Text("id"), args["expectedRevision"]?.GetValue<int>() ?? -1, args.Text("actor"), args.Text("reason"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L53)

**is handled by** →

- [`Store.cs`](../files/Store.cs.md) (Store.Approve) · [Operations.cs:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L53)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L53)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:36](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L36)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L64)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L85)

**is invoked by** ←

- [`approve_canon`](../tools/approve_canon.md) · [McpTools.cs:36](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L36)
