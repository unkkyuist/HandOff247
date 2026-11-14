---
generator: HandOff247
id: "route:GET /desk"
type: Route
source: "app.py"
---

# `GET /desk`

> handler `desk`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)

**is open to** →

- [`author`](../users/author.md) (@require_role('author')) · [app.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L56)

**shows** →

- [`templates/desk.html`](../screens/templates__desk.html.md) · [app.py:58](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L58)

**redirects to** →

- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`articles`](../data/articles.md) (db.articles_of) · [db.py:40](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L40)
- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)

**is started from** ←

- [`My desk`](../terms.md) (GET) · [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14)

**is reached by redirect from** ←

- [`GET,POST /desk/new`](GET-POST-__desk__new.md) (request.method == 'POST') · [app.py:69](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L69)
- [`POST /desk/<int:article_id>/submit`](POST-__desk__-int-article_id-__submit.md) · [app.py:82](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L82)

**Called:** "My desk"  
**User types:** [`author`](../users/author.md)

## Started from

- link "My desk" on [`templates/base.html`](../screens/templates__base.html.md) ([templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14)), shown when `user and user.role == 'author'` — seen by [`author`](../users/author.md)

## Shows

- [`templates/desk.html`](../screens/templates__desk.html.md) "My desk" — seen by [`author`](../users/author.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. author: link "My desk" on templates/base.html, shown when `user and user.role == 'author'` — [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14)
2. the route lets through role author (@require_role('author')) — [app.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L56)
3. GET /desk runs `desk` — [app.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)
4. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
5. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
6. shows templates/desk.html — [app.py:58](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L58)
7. reads articles — [db.py:40](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L40) *(through `db.articles_of`)*

## Branches

| If | Then | Where |
|---|---|---|
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Code

- handler `desk` — [app.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `articles_of` — [db.py:39](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L39)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): reads — [db.py:40](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L40) *(through `db.articles_of`)*
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*
- the control is only shown when `user and user.role == 'author'` — [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14)

## Not verified by the analysis

- nothing specific to this feature

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
