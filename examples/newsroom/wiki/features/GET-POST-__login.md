---
generator: HandOff247
id: "route:GET,POST /login"
type: Route
source: "app.py"
---

# `GET,POST /login`

> handler `login`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)

**shows** →

- [`templates/login.html`](../screens/templates__login.html.md) · [app.py:50](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L50)

**redirects to** →

- [`GET /`](GET-__.md) (request.method == 'POST') · [app.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L49)

**reads** →

- [`users`](../data/users.md) (db.find_user) · [db.py:30](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L30)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)

**is started from** ←

- [`Sign in`](../terms.md) (GET) · [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20)
- [`Work e-mail`](../terms.md) (POST) · [templates/login.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L6)
- [`Continue`](../terms.md) (POST) · [templates/login.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L8)

**is reached by redirect from** ←

- [`GET /desk`](GET-__desk.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`GET /preview/<int:article_id>`](GET-__preview__-int-article_id.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`GET /review`](GET-__review.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`GET /review/<int:article_id>`](GET-__review__-int-article_id.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`GET,POST /desk/new`](GET-POST-__desk__new.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`POST /desk/<int:article_id>/submit`](POST-__desk__-int-article_id-__submit.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`POST /review/<int:article_id>/publish`](POST-__review__-int-article_id-__publish.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)
- [`POST /review/<int:article_id>/return`](POST-__review__-int-article_id-__return.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**Called:** "Continue" / "Sign in"  
**User types:** [`anyone`](../users/anyone.md)

## Started from

- link "Sign in" on [`templates/base.html`](../screens/templates__base.html.md) ([templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20)), shown when `not user` — seen by [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)
- button "Continue" on [`templates/login.html`](../screens/templates__login.html.md) ([templates/login.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L8)) — seen by [`anyone`](../users/anyone.md)

## Shows

- [`templates/login.html`](../screens/templates__login.html.md) "Sign in" — seen by [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. author, editor, anyone: link "Sign in" on templates/base.html, shown when `not user` — [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20)
2. anyone: button "Continue" on templates/login.html — [templates/login.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L8)
3. GET,POST /login runs `login` — [app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)
4. *when* `request.method == 'POST'`: reads users — [db.py:30](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L30) *(through `db.find_user`)*
5. *when* `request.method == 'POST'`: reads the form field `email` — [app.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L44)
6. *when* `request.method == 'POST'` and `user is None`: shows the message "Unknown e-mail address" — [app.py:46](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L46)
7. *when* `request.method == 'POST'` and `user is None`: redirects to GET,POST /login — [app.py:47](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L47)
8. *when* `request.method == 'POST'`: redirects to GET / — [app.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L49)
9. shows templates/login.html — [app.py:50](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L50)

## Branches

| If | Then | Where |
|---|---|---|
| `request.method == 'POST'` | redirects to `home` | [app.py:43](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L43) |
| `user is None` | shows the message "Unknown e-mail address"; redirects to `login` | [app.py:45](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L45) |

## Code

- handler `login` — [app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)
- `find_user` — [db.py:29](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L29)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:30](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L30) *(through `db.find_user`)*
- [`static/logo.svg`](../assets/static__logo.svg.md) (static): shows it
- [`static/paper.png`](../assets/static__paper.png.md) (static): shows it

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.find_user → query → connect`)*
- condition `request.method == 'POST'` → redirects to `home` — [app.py:43](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L43)
- condition `user is None` → shows the message "Unknown e-mail address"; redirects to `login` — [app.py:45](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L45)
- the control is only shown when `not user` — [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20)

## Not verified by the analysis

- no access check was found on the route; a check made in middleware or a base class would not be seen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
