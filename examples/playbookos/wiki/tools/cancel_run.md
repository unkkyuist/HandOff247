---
generator: HandOff247
id: "tool:cancel_run"
type: McpTool
source: "McpTools.cs"
---

# `cancel_run`

> Cancel a queued/running run using its current revision. Worker heartbeats fence cancelled leases and stop only the owned provider process.

- **Class:** MCP tool — A tool the program offers to AI clients over MCP.
- **Method:** `McpTools.CancelRun`
- **Name comes from:** method name (SDK snake_case)
- **Source:** [McpTools.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L95)

**invokes** →

- [`run.cancel`](../operations/run.cancel.md) · [McpTools.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L95)

**is defined in** ←

- [`McpTools.cs`](../files/McpTools.cs.md) · [McpTools.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L95)
