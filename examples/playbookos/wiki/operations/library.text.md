---
generator: HandOff247
id: "op:library.text"
type: Operation
source: "Operations.cs"
---

# `library.text`

> handled by `Library.Text`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Library.Text`
- **Expression in the table:** `await library.Text(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L79)

**is handled by** →

- [`Library.cs`](../files/Library.cs.md) (Library.Text) · [Operations.cs:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L79)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L79)

**is called from** ←

- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:138](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L138) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
