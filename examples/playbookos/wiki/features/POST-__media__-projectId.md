---
generator: HandOff247
id: "route:POST /media/{projectId}"
type: Route
source: "Program.cs"
---

# `POST /media/{projectId}`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

**is defined in** ←

- [`Program.cs`](../files/Program.cs.md) · [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

**is exposed by** ←

- [`serve`](../modes/serve.md) · [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)
- [`server`](../modes/server.md) · [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

**is started from** ←

- [`wwwroot/index.html`](../screens/wwwroot__index.html.md) (script call) · [wwwroot/media.js:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L84)

**Called:** POST /media/{projectId}  
**User types:** [`anyone`](../users/anyone.md)

## Started from

- script call on [`wwwroot/index.html`](../screens/wwwroot__index.html.md) ([wwwroot/media.js:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L84)) — seen by [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. anyone: script call on wwwroot/index.html — [wwwroot/media.js:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L84)
2. POST /media/{projectId} runs `its handler` — [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

## Code

- handler `` — [Program.cs:104](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L104)

## Not verified by the analysis

- the handler was not analysed (only Python handlers are followed), so what it reads and writes is unknown
- no access check was found on the route; a check made in middleware or a base class would not be seen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
