---
generator: HandOff247
id: "op:connection.disconnect"
type: Operation
source: "Operations.cs"
---

# `connection.disconnect`

> handled by `Connection.Disconnect`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Connection.Disconnect`
- **Expression in the table:** `await connection.Disconnect()`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L59)

**is handled by** →

- [`Connection.cs`](../files/Connection.cs.md) (Connection.Disconnect) · [Operations.cs:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L59)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L59)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L85) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
