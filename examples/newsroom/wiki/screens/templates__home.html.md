---
generator: HandOff247
id: "screen:templates/home.html"
type: Screen
source: "templates/home.html"
---

# `templates/home.html`

> Latest articles

- **Class:** Screen — A template or page a user sees.
- **Kind:** page
- **Source:** [templates/home.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L1)

**is built on** →

- [`templates/base.html`](templates__base.html.md) (extends) · [templates/home.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L1)

**shows** →

- [`generated:published.csv`](../assets/generated-published.csv.md) (link "Download the list") · [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13)
- [`static/logo.svg`](../assets/static__logo.svg.md) (through the layout templates/base.html) · [templates/base.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L10)
- [`static/paper.png`](../assets/static__paper.png.md) (through the layout templates/base.html) · [static/site.css:2](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/static/site.css#L2)
- [`upload:cover`](../assets/upload-cover.md) (<img>) · [templates/home.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L8)

**is defined in** ←

- [`templates/home.html`](../files/templates__home.html.md) · [templates/home.html:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L1)

**is seen by** ←

- [`anyone`](../users/anyone.md) (GET /) · [app.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L20)

**is shown by** ←

- [`GET /`](../features/GET-__.md) · [app.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L20)

**Seen by:** [`anyone`](../users/anyone.md)  
**Kind:** page

Shown by [`GET /`](../features/GET-__.md).

Built on the layout [`templates/base.html`](templates__base.html.md); its menu and other terms appear here too.

## Words on this screen

| Text | Kind | Where | Shown when | Leads to | Field in the code |
|---|---|---|---|---|---|
| "Latest articles" | heading | [templates/home.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L4) |  |  |  |
| *(text set at run time)* | link | [templates/home.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L10) |  | [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) |  |
| "Download the list" | link | [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13) |  | [`GET /published.csv`](../features/GET-__published.csv.md) |  |
| "Newsroom" | title | [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) *(layout)* |  |  |  |
| "Front page" | link | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) |  |
| "My desk" | link | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) |  |
| "Review queue" / "검토 대기열" | link | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)*<br>text from [locales/en.json:3](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/locales/en.json#L3) (`nav.review`) | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) |  |
| "Sign in" | link | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) |  |

## Assets shown

- [`upload:cover`](../assets/upload-cover.md)
- [`generated:published.csv`](../assets/generated-published.csv.md)
