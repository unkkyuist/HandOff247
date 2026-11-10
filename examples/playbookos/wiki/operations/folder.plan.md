---
generator: HandOff247
id: "op:folder.plan"
type: Operation
source: "Operations.cs"
---

# `folder.plan`

> handled by `Folders.Plan`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Folders.Plan`
- **Expression in the table:** `folders.Plan(args.Text("projectId"), args.Text("source"), args.Text("destination"), args.Text("actor"), args.Text("reason"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L90)

**is handled by** →

- [`Folders.cs`](../files/Folders.cs.md) (Folders.Plan) · [Operations.cs:90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L90)

**is documented in** ←

- [`docs/CLAUDE-AND-FOLDERS.md`](../files/docs__CLAUDE-AND-FOLDERS.md.md) (cli folder.plan) · [docs/CLAUDE-AND-FOLDERS.md:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L43)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L90)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L68)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L25)
- [`wwwroot/folders.js`](../files/wwwroot__folders.js.md) (api(), over HTTP) · [wwwroot/folders.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js#L88) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`plan_folder_move`](../tools/plan_folder_move.md) · [McpTools.cs:68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L68)
