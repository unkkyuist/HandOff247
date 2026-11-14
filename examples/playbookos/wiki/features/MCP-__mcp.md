---
generator: HandOff247
id: "route:MCP /mcp"
type: Route
source: "Program.cs"
---

# `MCP /mcp`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)

**is defined in** ←

- [`Program.cs`](../files/Program.cs.md) · [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)

**is exposed by** ←

- [`serve`](../modes/serve.md) · [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)
- [`server`](../modes/server.md) · [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)

**Called:** MCP /mcp  
**User types:** [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. MCP /mcp runs `its handler` — [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)

## Code

- handler `` — [Program.cs:109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L109)

## Not verified by the analysis

- the handler was not analysed (only Python handlers are followed), so what it reads and writes is unknown
- no access check was found on the route; a check made in middleware or a base class would not be seen
- no link, button or script call that starts this feature was found on a screen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
