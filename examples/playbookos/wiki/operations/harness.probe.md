---
generator: HandOff247
id: "op:harness.probe"
type: Operation
source: "Operations.cs"
---

# `harness.probe`

> handled by `Harnesses.Probe`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Harnesses.Probe`
- **Expression in the table:** `harnesses.Probe(ParentRun(args))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L39)

**is handled by** →

- [`Harnesses.cs`](../files/Harnesses.cs.md) (Harnesses.Probe) · [Operations.cs:39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L39)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L39)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L87)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:210](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L210)
- [`wwwroot/harness.js`](../files/wwwroot__harness.js.md) (api(), over HTTP) · [wwwroot/harness.js:55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L55) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`probe_harness`](../tools/probe_harness.md) · [McpTools.cs:87](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L87)
