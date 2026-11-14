---
generator: HandOff247
id: "screen:templates/article.html"
type: Screen
source: "templates/article.html"
---

# `templates/article.html`

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/article.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/article.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)
- [`upload:cover`](../assets/upload-cover.md) (<img>) · [templates/article.html:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L9)

**is defined in** ←

- [`templates/article.html`](../files/templates__article.html.md) · [templates/article.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L1)

**is seen by** ←

- [`anyone`](../users/anyone.md) (GET /articles/<int:article_id>) · [app.py:28](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L28)
- [`author`](../users/author.md) (GET /preview/<int:article_id>) · [app.py:126](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L126)
- [`editor`](../users/editor.md) (GET /preview/<int:article_id>) · [app.py:126](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L126)

**is shown by** ←

- [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) · [app.py:28](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L28)
- [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) · [app.py:126](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L126)

**Seen by:** [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)  
**Kind:** page

Shown by [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md), [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |

## Assets shown

- [`upload:cover`](../assets/upload-cover.md)
