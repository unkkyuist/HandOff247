---
generator: HandOff247
id: "op:harness.propose"
type: Operation
source: "Operations.cs"
---

# `harness.propose`

> handled by `Harnesses.Propose`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Harnesses.Propose`
- **Expression in the table:** `harnesses.Propose(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L38)

**is handled by** →

- [`Harnesses.cs`](../files/Harnesses.cs.md) (Harnesses.Propose) · [Operations.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L38)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:38](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L38)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L85)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:208](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L208)
- [`wwwroot/harness.js`](../files/wwwroot__harness.js.md) (api(), over HTTP) · [wwwroot/harness.js:50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L50) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`propose_harness`](../tools/propose_harness.md) · [McpTools.cs:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L85)
