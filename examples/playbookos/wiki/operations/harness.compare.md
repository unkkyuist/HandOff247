---
generator: HandOff247
id: "op:harness.compare"
type: Operation
source: "Operations.cs"
---

# `harness.compare`

> handled by `Harnesses.Compare`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Harnesses.Compare`
- **Expression in the table:** `harnesses.Compare(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L40)

**is handled by** →

- [`Harnesses.cs`](../files/Harnesses.cs.md) (Harnesses.Compare) · [Operations.cs:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L40)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L40)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L89)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L80)
- [`wwwroot/harness.js`](../files/wwwroot__harness.js.md) (api(), over HTTP) · [wwwroot/harness.js:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L60) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`compare_harness`](../tools/compare_harness.md) · [McpTools.cs:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L89)
