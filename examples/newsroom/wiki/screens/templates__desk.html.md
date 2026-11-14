---
generator: HandOff247
id: "screen:templates/desk.html"
type: Screen
source: "templates/desk.html"
---

# `templates/desk.html`

> My desk

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/desk.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/desk.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L1)

**shows** →

- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)

**is defined in** ←

- [`templates/desk.html`](../files/templates__desk.html.md) · [templates/desk.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L1)

**is seen by** ←

- [`author`](../users/author.md) (GET /desk) · [app.py:58](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L58)

**is shown by** ←

- [`GET /desk`](../features/GET-__desk.md) · [app.py:58](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L58)

**tests** ←

- [`articles.status = 'draft'`](../states.md) (a.status == 'draft') · [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16) · *inferred: the condition names the same column and value; not traced to the same rows*

**Seen by:** [`author`](../users/author.md)  
**Kind:** page

Shown by [`GET /desk`](../features/GET-__desk.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "My desk" | heading | [templates/desk.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L4) |  |  |  |
| "New article" | link | [templates/desk.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L5) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) |  |
| "Headline" | column | [templates/desk.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L7) |  |  |  |
| "State" | column | [templates/desk.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L7) |  |  |  |
| "Editor's note" | column | [templates/desk.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L7) |  |  |  |
| *(text set at run time)* | link | [templates/desk.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L10) |  | [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) |  |
| "Send for review" | button | [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16) | `a.status == 'draft'` | [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) |  |
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |
