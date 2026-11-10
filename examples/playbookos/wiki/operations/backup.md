---
generator: HandOff247
id: "op:backup"
type: Operation
source: "Operations.cs"
---

# `backup`

> handled by `Store.Backup`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Store.Backup`
- **Expression in the table:** `new { path = store.Backup() }`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L87)

**is handled by** →

- [`Store.cs`](../files/Store.cs.md) (Store.Backup) · [Operations.cs:87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L87)

**is documented in** ←

- [`README.md`](../files/README.md.md) (cli backup) · [README.md:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L70)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L87)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L62)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L83)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L88)

**is invoked by** ←

- [`backup`](../tools/backup.md) · [McpTools.cs:62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L62)
