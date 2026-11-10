---
generator: HandOff247
id: "op:connection.status"
type: Operation
source: "Operations.cs"
---

# `connection.status`

> handled by `Connection.Status`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Connection.Status`
- **Expression in the table:** `connection.Status()`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L57)

**is handled by** →

- [`Connection.cs`](../files/Connection.cs.md) (Connection.Status) · [Operations.cs:57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L57)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L57)

**is called from** ←

- [`scripts/check-package.py`](../files/scripts__check-package.py.md) (cli(), by starting a process) · [scripts/check-package.py:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L43)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:48](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L48) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
