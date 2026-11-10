---
generator: HandOff247
id: "op:worker.configure"
type: Operation
source: "Operations.cs"
---

# `worker.configure`

> handled by `AgentWorker.Configure`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `AgentWorker.Configure`
- **Expression in the table:** `Worker is not null ? await Worker.Configure(args["enabled"]?.GetValue<bool>() ?? false, args["concurrency"]?.GetValue<int>() ?? 1) : throw new DomainError("Conf`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L66)

**is handled by** →

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (AgentWorker.Configure) · [Operations.cs:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L66)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L66)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L88) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
