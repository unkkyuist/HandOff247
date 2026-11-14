---
generator: HandOff247
id: "route:GET /articles/<int:article_id>"
type: Route
source: "app.py"
---

# `GET /articles/<int:article_id>`

> handler `article`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)

**shows** →

- [`templates/article.html`](../screens/templates__article.html.md) · [app.py:28](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L28)

**reads** →

- [`articles`](../data/articles.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)

**tests** ←

- [`articles.status = 'published'`](../states.md) (row is None or row['status'] != 'published') · [app.py:26](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L26) · *inferred: the condition names the same column and value; not traced to the same rows*

**Called:** article  
**User types:** [`anyone`](../users/anyone.md)

## Started from

- link whose text is set at run time on [`templates/home.html`](../screens/templates__home.html.md) ([templates/home.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L10)) — seen by [`anyone`](../users/anyone.md)

## Shows

- [`templates/article.html`](../screens/templates__article.html.md) — seen by [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. anyone: link whose text is set at run time on templates/home.html — [templates/home.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L10)
2. GET /articles/<int:article_id> runs `article` — [app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)
3. reads articles — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
4. shows templates/article.html — [app.py:28](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L28)

## Branches

| If | Then | Where |
|---|---|---|
| `row is None or row['status'] != 'published'` | stops with abort(404) | [app.py:26](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L26) |

## Code

- handler `article` — [app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)
- `get_article` — [db.py:34](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L34) — shared with 4 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)

## Data and assets

- table [`articles`](../data/articles.md): reads — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
- [`upload:cover`](../assets/upload-cover.md) (uploaded): shows it
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.get_article → query → connect`)*
- condition `row is None or row['status'] != 'published'` → stops with abort(404) — [app.py:26](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L26)

## Not verified by the analysis

- no access check was found on the route; a check made in middleware or a base class would not be seen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
