---
generator: HandOff247
id: "screen:templates/base.html"
type: Screen
source: "templates/base.html"
---

# `templates/base.html`

> Newsroom

- **Class:** Screen — A template or page a user sees.
- **Kind:** layout
- **Source:** [templates/base.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (<img>) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (url() in a stylesheet) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)

**is defined in** ←

- [`templates/base.html`](../files/templates__base.html.md) · [templates/base.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L1)

**is part of** ←

- [`templates/article.html`](templates__article.html.md) (extends) · [templates/article.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L1)
- [`templates/desk.html`](templates__desk.html.md) (extends) · [templates/desk.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L1)
- [`templates/edit.html`](templates__edit.html.md) (extends) · [templates/edit.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L1)
- [`templates/home.html`](templates__home.html.md) (extends) · [templates/home.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L1)
- [`templates/login.html`](templates__login.html.md) (extends) · [templates/login.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L1)
- [`templates/review.html`](templates__review.html.md) (extends) · [templates/review.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L1)
- [`templates/review_detail.html`](templates__review_detail.html.md) (extends) · [templates/review_detail.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L1)

**Seen by:** [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)  
**Kind:** layout

Part of: [`templates/article.html`](templates__article.html.md), [`templates/desk.html`](templates__desk.html.md), [`templates/edit.html`](templates__edit.html.md), [`templates/home.html`](templates__home.html.md), [`templates/login.html`](templates__login.html.md), [`templates/review.html`](templates__review.html.md), [`templates/review_detail.html`](templates__review_detail.html.md).

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17)<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |

## Assets shown

- [`static/logo.svg`](../assets/static__logo.svg.md)
- [`static/paper.png`](../assets/static__paper.png.md)
