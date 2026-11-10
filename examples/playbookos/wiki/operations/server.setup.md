---
generator: HandOff247
id: "op:server.setup"
type: Operation
source: "Operations.cs"
---

# `server.setup`

> handled by `Access.Setup`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Access.Setup`
- **Expression in the table:** `access.Setup(args.Text("user"), args.Text("password"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L61)

**is handled by** →

- [`Access.cs`](../files/Access.cs.md) (Access.Setup) · [Operations.cs:61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L61)

**is documented in** ←

- [`docs/PORTABLE-AND-AGENTS.md`](../files/docs__PORTABLE-AND-AGENTS.md.md) (cli server.setup) · [docs/PORTABLE-AND-AGENTS.md:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L42)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L61)
