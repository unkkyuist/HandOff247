---
generator: HandOff247
id: "route:GET /preview/<int:article_id>"
type: Route
source: "app.py"
---

# `GET /preview/<int:article_id>`

> handler `preview`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)

**is open to** →

- [`author`](../users/author.md) (@require_role('author', 'editor')) · [app.py:124](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L124)
- [`editor`](../users/editor.md) (@require_role('author', 'editor')) · [app.py:124](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L124)

**shows** →

- [`templates/article.html`](../screens/templates__article.html.md) · [app.py:126](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L126)

**redirects to** →

- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`articles`](../data/articles.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)

**is started from** ←

- [`Open the preview`](../terms.md) (GET) · [templates/review_detail.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L8)

**Called:** "Open the preview"  
**User types:** [`author`](../users/author.md), [`editor`](../users/editor.md)

## Started from

- link whose text is set at run time on [`templates/desk.html`](../screens/templates__desk.html.md) ([templates/desk.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L10)) — seen by [`author`](../users/author.md)
- link "Open the preview" on [`templates/review_detail.html`](../screens/templates__review_detail.html.md) ([templates/review_detail.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L8)) — seen by [`editor`](../users/editor.md)

## Shows

- [`templates/article.html`](../screens/templates__article.html.md) — seen by [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. author: link whose text is set at run time on templates/desk.html — [templates/desk.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L10)
2. editor: link "Open the preview" on templates/review_detail.html — [templates/review_detail.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L8)
3. the route lets through role author or editor (@require_role('author', 'editor')) — [app.py:124](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L124)
4. GET /preview/<int:article_id> runs `preview` — [app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)
5. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
6. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
7. shows templates/article.html — [app.py:126](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L126)
8. reads articles — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*

## Branches

| If | Then | Where |
|---|---|---|
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Code

- handler `preview` — [app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `get_article` — [db.py:34](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L34) — shared with 4 other feature(s)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): reads — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
- [`upload:cover`](../assets/upload-cover.md) (uploaded): shows it
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*

## Not verified by the analysis

- nothing specific to this feature

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
