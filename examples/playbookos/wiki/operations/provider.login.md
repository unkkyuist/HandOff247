---
generator: HandOff247
id: "op:provider.login"
type: Operation
source: "Operations.cs"
---

# `provider.login`

> handled by `Providers.Login`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Providers.Login`
- **Expression in the table:** `await providers.Login(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L63)

**is handled by** →

- [`Providers.cs`](../files/Providers.cs.md) (Providers.Login) · [Operations.cs:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L63)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L63)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L92) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
