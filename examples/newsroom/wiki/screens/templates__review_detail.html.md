---
generator: HandOff247
id: "screen:templates/review_detail.html"
type: Screen
source: "templates/review_detail.html"
---

# `templates/review_detail.html`

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/review_detail.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/review_detail.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)
- [`upload:cover`](../assets/upload-cover.md) (<img>) · [templates/review_detail.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L6)

**is defined in** ←

- [`templates/review_detail.html`](../files/templates__review_detail.html.md) · [templates/review_detail.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L1)

**is seen by** ←

- [`editor`](../users/editor.md) (GET /review/<int:article_id>) · [app.py:96](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L96)

**is shown by** ←

- [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) · [app.py:96](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L96)

**Seen by:** [`editor`](../users/editor.md)  
**Kind:** page

Shown by [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "Open the preview" | link | [templates/review_detail.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L8) |  | [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) |  |
| "Publish" / "게시" | button | [templates/review_detail.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L10)<br>text from [locales/en.json:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L6) (`review.publish`) |  | [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) |  |
| "Reason for the author" | field | [templates/review_detail.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L13) |  | [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) | `reason` read at [app.py:117](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L117) |
| "Send back" | button | [templates/review_detail.html:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L15) |  | [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) |  |
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |

## Assets shown

- [`upload:cover`](../assets/upload-cover.md)
