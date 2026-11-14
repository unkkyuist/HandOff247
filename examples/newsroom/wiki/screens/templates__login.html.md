---
generator: HandOff247
id: "screen:templates/login.html"
type: Screen
source: "templates/login.html"
---

# `templates/login.html`

> Sign in

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/login.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/login.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)

**is defined in** ←

- [`templates/login.html`](../files/templates__login.html.md) · [templates/login.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L1)

**is seen by** ←

- [`anyone`](../users/anyone.md) (GET,POST /login) · [app.py:50](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L50)

**is shown by** ←

- [`GET,POST /login`](../features/GET-POST-__login.md) · [app.py:50](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L50)

**Seen by:** [`anyone`](../users/anyone.md)  
**Kind:** page

Shown by [`GET,POST /login`](../features/GET-POST-__login.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "Sign in" | heading | [templates/login.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L4) |  |  |  |
| "Work e-mail" | field | [templates/login.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L6) |  | [`GET,POST /login`](../features/GET-POST-__login.md) | `email` read at [app.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L44) |
| "Continue" | button | [templates/login.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L8) |  | [`GET,POST /login`](../features/GET-POST-__login.md) |  |
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |
