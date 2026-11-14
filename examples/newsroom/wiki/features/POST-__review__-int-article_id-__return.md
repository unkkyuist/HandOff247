---
generator: HandOff247
id: "route:POST /review/<int:article_id>/return"
type: Route
source: "app.py"
---

# `POST /review/<int:article_id>/return`

> handler `send_back`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116)

**is open to** →

- [`editor`](../users/editor.md) (@require_role('editor')) · [app.py:115](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L115)

**redirects to** →

- [`GET /review`](GET-__review.md) · [app.py:118](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L118)
- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**writes** →

- [`articles`](../data/articles.md) (db.return_to_author) · [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61)

**sets** →

- [`articles.status = 'draft'`](../states.md) (db.return_to_author) · [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116)

**is started from** ←

- [`Reason for the author`](../terms.md) (POST) · [templates/review_detail.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L13)
- [`Send back`](../terms.md) (POST) · [templates/review_detail.html:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L15)

**Called:** "Send back"  
**User types:** [`editor`](../users/editor.md)

## Started from

- button "Send back" on [`templates/review_detail.html`](../screens/templates__review_detail.html.md) ([templates/review_detail.html:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L15)) — seen by [`editor`](../users/editor.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. editor: button "Send back" on templates/review_detail.html — [templates/review_detail.html:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L15)
2. the route lets through role editor (@require_role('editor')) — [app.py:115](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L115)
3. POST /review/<int:article_id>/return runs `send_back` — [app.py:116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116)
4. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
5. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
6. updates articles; sets status = 'draft' — [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61) *(through `db.return_to_author`)*
7. reads the form field `reason` — [app.py:117](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L117)
8. redirects to GET /review — [app.py:118](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L118)

## Branches

| If | Then | Where |
|---|---|---|
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Hand-overs

*Inferred:* derived from a column value that one statement sets and another tests.

- → [`author`](../users/author.md): [`templates/desk.html`](../screens/templates__desk.html.md), because `articles.status = 'draft'`; controls "Send for review" — set at [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61) *(through `db.return_to_author`)*, tested at [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)
- → [`author`](../users/author.md): [`POST /desk/<int:article_id>/submit`](POST-__desk__-int-article_id-__submit.md), because `articles.status = 'draft'`; then shows the message "Only a draft can be sent for review"; redirects to `desk` — set at [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61) *(through `db.return_to_author`)*, tested at [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77)

## Code

- handler `send_back` — [app.py:116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `return_to_author` — [db.py:60](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L60)
- `execute` — [db.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L19) — shared with 3 other feature(s)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): writes, sets `status = 'draft'` — [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61) *(through `db.return_to_author`)*

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.return_to_author → execute → connect`)*
- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*

## Not verified by the analysis

- hand-overs are derived from a shared column value, not traced row by row

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
