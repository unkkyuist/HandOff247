---
generator: HandOff247
id: "route:POST /auth/login"
type: Route
source: "Program.cs"
---

# `POST /auth/login`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)

**is defined in** ←

- [`Program.cs`](../files/Program.cs.md) · [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)

**is exposed by** ←

- [`serve`](../modes/serve.md) · [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)
- [`server`](../modes/server.md) · [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)

**is started from** ←

- [`wwwroot/index.html`](../screens/wwwroot__index.html.md) (script call) · [wwwroot/workspace-ui.js:148](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L148)

**Called:** POST /auth/login  
**User types:** [`anyone`](../users/anyone.md)

## Started from

- script call on [`wwwroot/index.html`](../screens/wwwroot__index.html.md) ([wwwroot/workspace-ui.js:148](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L148)) — seen by [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. anyone: script call on wwwroot/index.html — [wwwroot/workspace-ui.js:148](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L148)
2. POST /auth/login runs `its handler` — [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)

## Code

- handler `` — [Program.cs:99](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L99)

## Not verified by the analysis

- the handler was not analysed (only Python handlers are followed), so what it reads and writes is unknown
- no access check was found on the route; a check made in middleware or a base class would not be seen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
