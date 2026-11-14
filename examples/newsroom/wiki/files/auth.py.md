---
generator: HandOff247
id: "file:auth.py"
type: File
source: "auth.py"
---

# `auth.py`

> Who is signed in, and the role check used by the routes.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 26
- **Source:** [auth.py](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py)

**defines** →

- [`current_user`](../functions.md) · [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9)
- [`require_role`](../functions.md) · [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14)

**imports** →

- [`db.py`](db.py.md) · [auth.py:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L6)

**depends on** →

- [`flask`](../packages.md) (imported) · [auth.py](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py)

**is part of** ←

- [Newsroom](../overview.md)

**is imported by** ←

- [`app.py`](app.py.md) · [app.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L8)

## Defined here

- `current_user` — function, [line 9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9)
- `require_role` — function, [line 14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — Let the request through only when the signed-in user has one of the roles.
