---
generator: HandOff247
id: "op:folder.recover"
type: Operation
source: "Operations.cs"
---

# `folder.recover`

> handled by `Folders.Recover`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Folders.Recover`
- **Expression in the table:** `folders.Recover(args.Text("planId"), args["confirmed"]?.GetValue<bool>() ?? false)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L92)

**is handled by** →

- [`Folders.cs`](../files/Folders.cs.md) (Folders.Recover) · [Operations.cs:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L92)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L92)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L72)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L68)

**is invoked by** ←

- [`recover_folder_move`](../tools/recover_folder_move.md) · [McpTools.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L72)
