---
generator: HandOff247
id: "route:GET /review/<int:article_id>"
type: Route
source: "app.py"
---

# `GET /review/<int:article_id>`

> handler `review_detail`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)

**is open to** →

- [`editor`](../users/editor.md) (@require_role('editor')) · [app.py:94](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L94)

**shows** →

- [`templates/review_detail.html`](../screens/templates__review_detail.html.md) · [app.py:96](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L96)

**redirects to** →

- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`articles`](../data/articles.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)

**is reached by redirect from** ←

- [`POST /review/<int:article_id>/publish`](POST-__review__-int-article_id-__publish.md) (COVER_REQUIRED == '1' and (not row['cover'])) · [app.py:108](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L108)

**Called:** review_detail  
**User types:** [`editor`](../users/editor.md)

## Started from

- link whose text is set at run time on [`templates/review.html`](../screens/templates__review.html.md) ([templates/review.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L7)) — seen by [`editor`](../users/editor.md)

## Shows

- [`templates/review_detail.html`](../screens/templates__review_detail.html.md) — seen by [`editor`](../users/editor.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. editor: link whose text is set at run time on templates/review.html — [templates/review.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L7)
2. the route lets through role editor (@require_role('editor')) — [app.py:94](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L94)
3. GET /review/<int:article_id> runs `review_detail` — [app.py:95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)
4. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
5. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
6. shows templates/review_detail.html — [app.py:96](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L96)
7. reads articles — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*

## Branches

| If | Then | Where |
|---|---|---|
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Code

- handler `review_detail` — [app.py:95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)
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
