---
generator: HandOff247
id: "op:run.enqueue"
type: Operation
source: "Operations.cs"
---

# `run.enqueue`

> handled by `Orchestration.Enqueue`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Orchestration.Enqueue`
- **Expression in the table:** `orchestration.Enqueue(ParentRun(args))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L69)

**is handled by** →

- [`Orchestration.cs`](../files/Orchestration.cs.md) (Orchestration.Enqueue) · [Operations.cs:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L69)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L69)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L81)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:205](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L205)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:142](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L142)
- [`scripts/real-provider-smoke.py`](../files/scripts__real-provider-smoke.py.md) (cli(), by starting a process) · [scripts/real-provider-smoke.py:29](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L29)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:106](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L106) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`enqueue_run`](../tools/enqueue_run.md) · [McpTools.cs:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L81)
