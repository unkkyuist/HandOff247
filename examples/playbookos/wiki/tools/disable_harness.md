---
generator: HandOff247
id: "tool:disable_harness"
type: McpTool
source: "McpTools.cs"
---

# `disable_harness`

> Explicit user action: disable the adopted project harness using its current revision and confirmed=true. Already queued runs retain their exact snapshots; new runs receive no harness.

- **Class:** MCP tool — A tool the program offers to AI clients over MCP.
- **Method:** `McpTools.DisableHarness`
- **Name comes from:** method name (SDK snake_case)
- **Source:** [McpTools.cs:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L93)

**invokes** →

- [`harness.disable`](../operations/harness.disable.md) · [McpTools.cs:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L93)

**is defined in** ←

- [`McpTools.cs`](../files/McpTools.cs.md) · [McpTools.cs:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L93)
