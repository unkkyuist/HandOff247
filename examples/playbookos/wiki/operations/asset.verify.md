---
generator: HandOff247
id: "op:asset.verify"
type: Operation
source: "Operations.cs"
---

# `asset.verify`

> handled by `Workspace.VerifyAsset`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.VerifyAsset`
- **Expression in the table:** `await workspace.VerifyAsset(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L82)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.VerifyAsset) · [Operations.cs:82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L82)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L82)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L40)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L80)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L77)

**is invoked by** ←

- [`verify_asset`](../tools/verify_asset.md) · [McpTools.cs:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L40)
