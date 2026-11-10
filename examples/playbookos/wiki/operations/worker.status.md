---
generator: HandOff247
id: "op:worker.status"
type: Operation
source: "Operations.cs"
---

# `worker.status`

> handled by `AgentWorker.Status`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `AgentWorker.Status`
- **Expression in the table:** `Worker?.Status() ?? new { workerEnabled = connection.Settings.WorkerEnabled, note = "Start serve on this device to run the worker." }`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:65](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L65)

**is handled by** →

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (AgentWorker.Status) · [Operations.cs:65](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L65)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:65](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L65)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L86) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
