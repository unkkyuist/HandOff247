---
generator: HandOff247
id: "op:connection.connect"
type: Operation
source: "Operations.cs"
---

# `connection.connect`

> handled by `Connection.Connect`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Connection.Connect`
- **Expression in the table:** `await connection.Connect(args.Text("url"), args.Text("user"), args.Text("password"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L58)

**is handled by** →

- [`Connection.cs`](../files/Connection.cs.md) (Connection.Connect) · [Operations.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L58)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L58)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L84) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
