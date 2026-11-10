---
generator: HandOff247
id: "op:library.download"
type: Operation
source: "Operations.cs"
---

# `library.download`

> handled by `Library.Download`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Library.Download`
- **Expression in the table:** `library.Download(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L77)

**is handled by** →

- [`Library.cs`](../files/Library.cs.md) (Library.Download) · [Operations.cs:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L77)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L77)

**is called from** ←

- [`Library.cs`](../files/Library.cs.md) (Request()) · [Library.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L83)
