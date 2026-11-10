---
generator: HandOff247
id: "op:library.register"
type: Operation
source: "Operations.cs"
---

# `library.register`

> handled by `Library.Register`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Library.Register`
- **Expression in the table:** `await library.Register(args.Text("projectId"), args.Text("path"), args.Text("actor"), args.Text("license"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L75)

**is handled by** →

- [`Library.cs`](../files/Library.cs.md) (Library.Register) · [Operations.cs:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L75)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L75)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:101](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L101)
- [`scripts/real-provider-smoke.py`](../files/scripts__real-provider-smoke.py.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:28](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L28)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L64)

**is invoked by** ←

- [`share_reference`](../tools/share_reference.md) · [McpTools.cs:101](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L101)
