---
generator: HandOff247
id: "route:POST /desk/<int:article_id>/submit"
type: Route
source: "app.py"
---

# `POST /desk/<int:article_id>/submit`

> handler `submit`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75)

**is open to** →

- [`author`](../users/author.md) (@require_role('author')) · [app.py:74](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L74)

**redirects to** →

- [`GET /desk`](GET-__desk.md) · [app.py:82](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L82)
- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`articles`](../data/articles.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**writes** →

- [`articles`](../data/articles.md) (db.send_for_review) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)

**sets** →

- [`articles.status = 'in_review'`](../states.md) (db.send_for_review) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)

**hands over to** →

- [`GET /review`](GET-__review.md) (articles.status = 'in_review') · [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) · *inferred: one statement sets this value and the other filters on it; that the same rows are meant was not verified*

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75)

**is started from** ←

- [`Send for review`](../terms.md) (POST) · [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)

**tests** ←

- [`articles.status = 'draft'`](../states.md) (row['status'] != 'draft') · [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77) · *inferred: the condition names the same column and value; not traced to the same rows*

**Called:** "Send for review"  
**User types:** [`author`](../users/author.md)

## Started from

- button "Send for review" on [`templates/desk.html`](../screens/templates__desk.html.md) ([templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)), shown when `a.status == 'draft'` — seen by [`author`](../users/author.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. author: button "Send for review" on templates/desk.html, shown when `a.status == 'draft'` — [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)
2. the route lets through role author (@require_role('author')) — [app.py:74](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L74)
3. POST /desk/<int:article_id>/submit runs `submit` — [app.py:75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75)
4. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
5. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
6. reads articles — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
7. *when* `row['status'] != 'draft'`: shows the message "Only a draft can be sent for review" — [app.py:78](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L78)
8. *when* `row['status'] != 'draft'`: redirects to GET /desk — [app.py:79](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L79)
9. updates articles; sets status = 'in_review' — [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*
10. shows the message "Sent to the editors" — [app.py:81](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L81)
11. redirects to GET /desk — [app.py:82](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L82)

## Branches

| If | Then | Where |
|---|---|---|
| `row['status'] != 'draft'` | shows the message "Only a draft can be sent for review"; redirects to `desk` | [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77) |
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Hand-overs

*Inferred:* derived from a column value that one statement sets and another tests.

- → [`editor`](../users/editor.md): [`GET /review`](GET-__review.md) ([`templates/review.html`](../screens/templates__review.html.md)), because `articles.status = 'in_review'` — set at [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*, tested at [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*
- → [`editor`](../users/editor.md): [`POST /review/<int:article_id>/publish`](POST-__review__-int-article_id-__publish.md), because `articles.status = 'in_review'`; then shows the message "Only an article in review can be published"; redirects to `review_queue` — set at [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*, tested at [app.py:103](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L103)

## Code

- handler `submit` — [app.py:75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `get_article` — [db.py:34](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L34) — shared with 4 other feature(s)
- `send_for_review` — [db.py:48](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L48)
- `execute` — [db.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L19) — shared with 3 other feature(s)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): reads, writes, sets `status = 'in_review'` — [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.send_for_review → execute → connect`)*
- condition `row['status'] != 'draft'` → shows the message "Only a draft can be sent for review"; redirects to `desk` — [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77)
- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*
- the control is only shown when `a.status == 'draft'` — [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)

## Not verified by the analysis

- hand-overs are derived from a shared column value, not traced row by row

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
