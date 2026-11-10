---
generator: HandOff247
id: "op:scan.import"
type: Operation
source: "Operations.cs"
---

# `scan.import`

> handled by `ProjectScanner.Import`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `ProjectScanner.Import`
- **Expression in the table:** `scanner.Import(args.Text("scanId"), args["paths"]?.AsArray().Select(n => n!.GetValue<string>()).ToArray() ?? [], args.Text("actor"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L56)

**is handled by** →

- [`ProjectScanner.cs`](../files/ProjectScanner.cs.md) (ProjectScanner.Import) · [Operations.cs:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L56)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L56)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L77)
- [`scripts/check-package.py`](../files/scripts__check-package.py.md) (cli(), by starting a process) · [scripts/check-package.py:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L45)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L54) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`import_scanned_projects`](../tools/import_scanned_projects.md) · [McpTools.cs:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L77)
