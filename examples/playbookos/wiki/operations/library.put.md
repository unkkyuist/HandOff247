---
generator: HandOff247
id: "op:library.put"
type: Operation
source: "Operations.cs"
---

# `library.put`

> handled by `Library.Put`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Library.Put`
- **Expression in the table:** `library.Put(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L76)

**is handled by** →

- [`Library.cs`](../files/Library.cs.md) (Library.Put) · [Operations.cs:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L76)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L76)

**is called from** ←

- [`Library.cs`](../files/Library.cs.md) (Request()) · [Library.cs:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L19)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:129](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L129) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
