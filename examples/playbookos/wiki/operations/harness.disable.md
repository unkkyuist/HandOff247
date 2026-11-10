---
generator: HandOff247
id: "op:harness.disable"
type: Operation
source: "Operations.cs"
---

# `harness.disable`

> handled by `Harnesses.Disable`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Harnesses.Disable`
- **Expression in the table:** `harnesses.Disable(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L42)

**is handled by** →

- [`Harnesses.cs`](../files/Harnesses.cs.md) (Harnesses.Disable) · [Operations.cs:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L42)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L42)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L93)
- [`wwwroot/harness.js`](../files/wwwroot__harness.js.md) (api(), over HTTP) · [wwwroot/harness.js:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L44) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`disable_harness`](../tools/disable_harness.md) · [McpTools.cs:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L93)
