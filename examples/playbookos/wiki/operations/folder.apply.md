---
generator: HandOff247
id: "op:folder.apply"
type: Operation
source: "Operations.cs"
---

# `folder.apply`

> handled by `Folders.Apply`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Folders.Apply`
- **Expression in the table:** `folders.Apply(args.Text("planId"), args["confirmed"]?.GetValue<bool>() ?? false)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L91)

**is handled by** →

- [`Folders.cs`](../files/Folders.cs.md) (Folders.Apply) · [Operations.cs:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L91)

**is documented in** ←

- [`docs/CLAUDE-AND-FOLDERS.md`](../files/docs__CLAUDE-AND-FOLDERS.md.md) (cli folder.apply) · [docs/CLAUDE-AND-FOLDERS.md:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L45)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L91)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L70)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:36](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L36)
- [`wwwroot/folders.js`](../files/wwwroot__folders.js.md) (api(), over HTTP) · [wwwroot/folders.js:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js#L91) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`apply_folder_move`](../tools/apply_folder_move.md) · [McpTools.cs:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L70)
