---
generator: HandOff247
id: "op:harness.adopt"
type: Operation
source: "Operations.cs"
---

# `harness.adopt`

> handled by `Harnesses.Adopt`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Harnesses.Adopt`
- **Expression in the table:** `harnesses.Adopt(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L41)

**is handled by** →

- [`Harnesses.cs`](../files/Harnesses.cs.md) (Harnesses.Adopt) · [Operations.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L41)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L41)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L91)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L69)
- [`wwwroot/harness.js`](../files/wwwroot__harness.js.md) (api(), over HTTP) · [wwwroot/harness.js:66](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L66) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`adopt_harness`](../tools/adopt_harness.md) · [McpTools.cs:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L91)
