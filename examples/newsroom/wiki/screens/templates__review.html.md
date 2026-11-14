---
generator: HandOff247
id: "screen:templates/review.html"
type: Screen
source: "templates/review.html"
---

# `templates/review.html`

> Review queue

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/review.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/review.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)

**is defined in** ←

- [`templates/review.html`](../files/templates__review.html.md) · [templates/review.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L1)

**is seen by** ←

- [`editor`](../users/editor.md) (GET /review) · [app.py:90](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L90)

**is shown by** ←

- [`GET /review`](../features/GET-__review.md) · [app.py:90](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L90)

**Seen by:** [`editor`](../users/editor.md)  
**Kind:** page

Shown by [`GET /review`](../features/GET-__review.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "Review queue" / "검토 대기열" | heading | [templates/review.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L4)<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) |  |  |  |
| *(text set at run time)* | link | [templates/review.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L7) |  | [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) |  |
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |
