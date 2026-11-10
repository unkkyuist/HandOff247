---
generator: HandOff247
id: "op:provider.status"
type: Operation
source: "Operations.cs"
---

# `provider.status`

> handled by `Providers.All`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Providers.All`
- **Expression in the table:** `await providers.All()`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L62)

**is handled by** →

- [`Providers.cs`](../files/Providers.cs.md) (Providers.All) · [Operations.cs:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L62)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L62)

**is called from** ←

- [`scripts/real-provider-smoke.py`](../files/scripts__real-provider-smoke.py.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L25)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L90) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
