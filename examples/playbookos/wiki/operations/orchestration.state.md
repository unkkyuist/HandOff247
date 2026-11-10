---
generator: HandOff247
id: "op:orchestration.state"
type: Operation
source: "Operations.cs"
---

# `orchestration.state`

> handled by `Orchestration.State`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Orchestration.State`
- **Expression in the table:** `orchestration.State(Optional("projectId"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L68)

**is handled by** →

- [`Orchestration.cs`](../files/Orchestration.cs.md) (Orchestration.State) · [Operations.cs:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L68)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L68)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L79)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:149](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L149)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L97) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`orchestration_state`](../tools/orchestration_state.md) · [McpTools.cs:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L79)
