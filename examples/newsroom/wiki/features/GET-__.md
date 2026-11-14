---
generator: HandOff247
id: "route:GET /"
type: Route
source: "app.py"
---

# `GET /`

> handler `home`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)

**shows** →

- [`templates/home.html`](../screens/templates__home.html.md) · [app.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L20)

**reads** →

- [`articles`](../data/articles.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)

**lists only** →

- [`articles.status = 'published'`](../states.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)

**is started from** ←

- [`Front page`](../terms.md) (GET) · [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12)

**is reached by redirect from** ←

- [`GET,POST /login`](GET-POST-__login.md) (request.method == 'POST') · [app.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L49)

**receives from** ←

- [`POST /review/<int:article_id>/publish`](POST-__review__-int-article_id-__publish.md) (articles.status = 'published') · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) · *inferred: one statement sets this value and the other filters on it; that the same rows are meant was not verified*

**Called:** "Front page"  
**User types:** [`anyone`](../users/anyone.md)

## Started from

- link "Front page" on [`templates/base.html`](../screens/templates__base.html.md) ([templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12)) — seen by [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)

## Shows

- [`templates/home.html`](../screens/templates__home.html.md) "Latest articles" — seen by [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. author, editor, anyone: link "Front page" on templates/base.html — [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12)
2. GET / runs `home` — [app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)
3. shows templates/home.html — [app.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L20)
4. reads articles; only rows with status = 'published' — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*

## Hand-overs

*Inferred:* derived from a column value that one statement sets and another tests.

- ← [`editor`](../users/editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](POST-__review__-int-article_id-__publish.md)), because `articles.status = 'published'` — set at [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*, read at [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*

## Code

- handler `home` — [app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)
- `published_articles` — [db.py:64](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L64) — shared with 1 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)

## Data and assets

- table [`articles`](../data/articles.md): reads, only rows with `status = 'published'` — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*
- [`upload:cover`](../assets/upload-cover.md) (uploaded): shows it
- [`generated:published.csv`](../assets/generated-published.csv.md) (generated): shows it
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.published_articles → query → connect`)*
- the query only returns rows with articles.status = 'published' — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*

## Not verified by the analysis

- no access check was found on the route; a check made in middleware or a base class would not be seen
- hand-overs are derived from a shared column value, not traced row by row

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
