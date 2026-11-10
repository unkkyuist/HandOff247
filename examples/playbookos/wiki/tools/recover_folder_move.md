---
generator: HandOff247
id: "tool:recover_folder_move"
type: McpTool
source: "McpTools.cs"
---

# `recover_folder_move`

> Recover an interrupted folder operation from its journal. Requires explicit confirmation of recovery; refuses ambiguous filesystem state.

- **Class:** MCP tool — A tool the program offers to AI clients over MCP.
- **Method:** `McpTools.RecoverFolderMove`
- **Name comes from:** method name (SDK snake_case)
- **Source:** [McpTools.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L72)

**invokes** →

- [`folder.recover`](../operations/folder.recover.md) · [McpTools.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L72)

**is defined in** ←

- [`McpTools.cs`](../files/McpTools.cs.md) · [McpTools.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L72)
