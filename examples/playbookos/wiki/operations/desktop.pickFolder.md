---
generator: HandOff247
id: "op:desktop.pickFolder"
type: Operation
source: "Operations.cs"
---

# `desktop.pickFolder`

> handled by `Desktop.PickFolder`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Desktop.PickFolder`
- **Expression in the table:** `await Desktop.PickFolder(args.Text("root"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L80)

**is handled by** →

- [`Desktop.cs`](../files/Desktop.cs.md) (Desktop.PickFolder) · [Operations.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L80)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L80)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L71) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
