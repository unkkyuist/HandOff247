---
generator: HandOff247
id: "op:library.resolve"
type: Operation
source: "Operations.cs"
---

# `library.resolve`

> handled by `Library.Resolve`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Library.Resolve`
- **Expression in the table:** `await library.Resolve(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L78)

**is handled by** →

- [`Library.cs`](../files/Library.cs.md) (Library.Resolve) · [Operations.cs:78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L78)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L78)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L99)

**is invoked by** ←

- [`reference_asset`](../tools/reference_asset.md) · [McpTools.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L99)
