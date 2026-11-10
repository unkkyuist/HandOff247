---
generator: HandOff247
id: "op:events"
type: Operation
source: "Operations.cs"
---

# `events`

> handled by `Store.Events`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Store.Events`
- **Expression in the table:** `store.Events(args["after"]?.GetValue<long>() ?? 0, Optional("projectId"), args["latest"]?.GetValue<bool>() ?? false)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L52)

**is handled by** →

- [`Store.cs`](../files/Store.cs.md) (Store.Events) · [Operations.cs:52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L52)

**is documented in** ←

- [`README.md`](../files/README.md.md) (cli events) · [README.md:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L64)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:52](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L52)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L34)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L42)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:209](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L209)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:270](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L270)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L59)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L64)

**is invoked by** ←

- [`changes`](../tools/changes.md) · [McpTools.cs:34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L34)
