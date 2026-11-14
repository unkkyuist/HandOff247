---
generator: HandOff247
id: "route:GET /review"
type: Route
source: "app.py"
---

# `GET /review`

> handler `review_queue`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)

**is open to** →

- [`editor`](../users/editor.md) (@require_role('editor')) · [app.py:88](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L88)

**shows** →

- [`templates/review.html`](../screens/templates__review.html.md) · [app.py:90](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L90)

**redirects to** →

- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`articles`](../data/articles.md) (db.waiting_for_review) · [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53)
- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**lists only** →

- [`articles.status = 'in_review'`](../states.md) (db.waiting_for_review) · [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)

**is started from** ←

- [`Review queue`](../terms.md) (GET) · [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17)

**is reached by redirect from** ←

- [`POST /review/<int:article_id>/publish`](POST-__review__-int-article_id-__publish.md) · [app.py:111](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L111)
- [`POST /review/<int:article_id>/return`](POST-__review__-int-article_id-__return.md) · [app.py:118](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L118)

**receives from** ←

- [`POST /desk/<int:article_id>/submit`](POST-__desk__-int-article_id-__submit.md) (articles.status = 'in_review') · [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) · *inferred: one statement sets this value and the other filters on it; that the same rows are meant was not verified*

**Called:** "Review queue"  
**User types:** [`editor`](../users/editor.md)

## Started from

- link "Review queue" on [`templates/base.html`](../screens/templates__base.html.md) ([templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17)), shown when `user and user.role == 'editor'` — seen by [`editor`](../users/editor.md)

## Shows

- [`templates/review.html`](../screens/templates__review.html.md) "Review queue" — seen by [`editor`](../users/editor.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. editor: link "Review queue" on templates/base.html, shown when `user and user.role == 'editor'` — [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17)
2. the route lets through role editor (@require_role('editor')) — [app.py:88](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L88)
3. GET /review runs `review_queue` — [app.py:89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)
4. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
5. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
6. shows templates/review.html — [app.py:90](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L90)
7. reads articles; only rows with status = 'in_review' — [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*

## Branches

| If | Then | Where |
|---|---|---|
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Hand-overs

*Inferred:* derived from a column value that one statement sets and another tests.

- ← [`author`](../users/author.md): "Send for review" ([`POST /desk/<int:article_id>/submit`](POST-__desk__-int-article_id-__submit.md)), because `articles.status = 'in_review'` — set at [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*, read at [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*

## Code

- handler `review_queue` — [app.py:89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `waiting_for_review` — [db.py:52](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L52)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): reads, only rows with `status = 'in_review'` — [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*
- the control is only shown when `user and user.role == 'editor'` — [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17)
- the query only returns rows with articles.status = 'in_review' — [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*

## Not verified by the analysis

- hand-overs are derived from a shared column value, not traced row by row

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
