---
generator: HandOff247
id: "route:GET,POST /desk/new"
type: Route
source: "app.py"
---

# `GET,POST /desk/new`

> handler `new_article`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)

**is open to** →

- [`author`](../users/author.md) (@require_role('author')) · [app.py:62](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L62)

**shows** →

- [`templates/edit.html`](../screens/templates__edit.html.md) · [app.py:70](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L70)

**redirects to** →

- [`GET /desk`](GET-__desk.md) (request.method == 'POST') · [app.py:69](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L69)
- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**writes** →

- [`articles`](../data/articles.md) (db.create_article) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)

**sets** →

- [`articles.status = 'draft'`](../states.md) (db.create_article) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)

**provides** →

- [`upload:cover`](../assets/upload-cover.md) (receives it) · [app.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L65)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)

**is started from** ←

- [`New article`](../terms.md) (GET) · [templates/desk.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L5)
- [`Cover image`](../terms.md) (POST) · [templates/edit.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L10)
- [`Save draft`](../terms.md) (POST) · [templates/edit.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L12)
- [`Headline`](../terms.md) (POST) · [templates/edit.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L6)
- [`Text`](../terms.md) (POST) · [templates/edit.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L8)

**Called:** "New article" / "Save draft"  
**User types:** [`author`](../users/author.md)

## Started from

- link "New article" on [`templates/desk.html`](../screens/templates__desk.html.md) ([templates/desk.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L5)) — seen by [`author`](../users/author.md)
- button "Save draft" on [`templates/edit.html`](../screens/templates__edit.html.md) ([templates/edit.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L12)) — seen by [`author`](../users/author.md)

## Shows

- [`templates/edit.html`](../screens/templates__edit.html.md) "New article" — seen by [`author`](../users/author.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. author: link "New article" on templates/desk.html — [templates/desk.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L5)
2. author: button "Save draft" on templates/edit.html — [templates/edit.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L12)
3. the route lets through role author (@require_role('author')) — [app.py:62](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L62)
4. GET,POST /desk/new runs `new_article` — [app.py:63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)
5. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
6. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
7. *when* `request.method == 'POST'`: reads the uploaded file `cover` — [app.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L65)
8. *when* `request.method == 'POST'` and `cover`: stores the uploaded file `cover` os.path.join(UPLOAD_DIR, name) — [storage.py:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L17) *(through `storage.save_upload`)*
9. *when* `request.method == 'POST'`: inserts articles; sets status = 'draft'; keeps the stored file name of `cover` in column cover — [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)*
10. *when* `request.method == 'POST'`: reads the form field `title` — [app.py:67](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L67)
11. *when* `request.method == 'POST'`: reads the form field `body` — [app.py:67](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L67)
12. *when* `request.method == 'POST'`: shows the message "Draft saved" — [app.py:68](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L68)
13. *when* `request.method == 'POST'`: redirects to GET /desk — [app.py:69](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L69)
14. shows templates/edit.html — [app.py:70](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L70)

## Branches

| If | Then | Where |
|---|---|---|
| `request.method == 'POST'` | shows the message "Draft saved" | [app.py:64](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L64) |
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Hand-overs

*Inferred:* derived from a column value that one statement sets and another tests.

- → [`author`](../users/author.md): [`templates/desk.html`](../screens/templates__desk.html.md), because `articles.status = 'draft'`; controls "Send for review" — set at [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)*, tested at [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)
- → [`author`](../users/author.md): [`POST /desk/<int:article_id>/submit`](POST-__desk__-int-article_id-__submit.md), because `articles.status = 'draft'`; then shows the message "Only a draft can be sent for review"; redirects to `desk` — set at [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)*, tested at [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77)

## Code

- handler `new_article` — [app.py:63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `create_article` — [db.py:43](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L43)
- `execute` — [db.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L19) — shared with 3 other feature(s)
- `save_upload` — [storage.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L14)
- `safe_name` — [storage.py:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L10)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): writes, sets `status = 'draft'` — [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)*
- [`upload:cover`](../assets/upload-cover.md) (uploaded): registered, stored
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.create_article → execute → connect`)*
- setting `NEWSROOM_UPLOADS` (variable `UPLOAD_DIR`) — [storage.py:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L17) *(through `storage.save_upload`)*
- condition `request.method == 'POST'` → shows the message "Draft saved" — [app.py:64](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L64)
- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*

## Not verified by the analysis

- hand-overs are derived from a shared column value, not traced row by row

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
