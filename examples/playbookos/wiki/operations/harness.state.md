---
generator: HandOff247
id: "op:harness.state"
type: Operation
source: "Operations.cs"
---

# `harness.state`

> handled by `Harnesses.State`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Harnesses.State`
- **Expression in the table:** `harnesses.State(args.Text("projectId"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L37)

**is handled by** →

- [`Harnesses.cs`](../files/Harnesses.cs.md) (Harnesses.State) · [Operations.cs:37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L37)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L37)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L83)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L88)
- [`wwwroot/harness.js`](../files/wwwroot__harness.js.md) (api(), over HTTP) · [wwwroot/harness.js:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L42) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`harness_state`](../tools/harness_state.md) · [McpTools.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L83)
