---
generator: HandOff247
id: "screen:templates/edit.html"
type: Screen
source: "templates/edit.html"
---

# `templates/edit.html`

> New article

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/edit.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/edit.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)

**is defined in** ←

- [`templates/edit.html`](../files/templates__edit.html.md) · [templates/edit.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L1)

**is seen by** ←

- [`author`](../users/author.md) (GET,POST /desk/new) · [app.py:70](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L70)

**is shown by** ←

- [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) · [app.py:70](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L70)

**Seen by:** [`author`](../users/author.md)  
**Kind:** page

Shown by [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "New article" | heading | [templates/edit.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L4) |  |  |  |
| "Headline" | field | [templates/edit.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L6) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) | `title` read at [app.py:67](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L67) |
| "Text" | field | [templates/edit.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L8) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) | `body` read at [app.py:67](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L67) |
| "Cover image" | field | [templates/edit.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L10) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) | `cover` read at [app.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L65) |
| "Save draft" | button | [templates/edit.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L12) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) |  |
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |
