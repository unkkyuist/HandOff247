---
generator: HandOff247
id: "op:scan"
type: Operation
source: "Operations.cs"
---

# `scan`

> handled by `ProjectScanner.Scan`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `ProjectScanner.Scan`
- **Expression in the table:** `scanner.Scan(args.Text("root"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L55)

**is handled by** →

- [`ProjectScanner.cs`](../files/ProjectScanner.cs.md) (ProjectScanner.Scan) · [Operations.cs:55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L55)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L55)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L75)
- [`scripts/check-package.py`](../files/scripts__check-package.py.md) (cli(), by starting a process) · [scripts/check-package.py:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L44)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L72) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`scan_projects`](../tools/scan_projects.md) · [McpTools.cs:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L75)
