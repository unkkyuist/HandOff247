---
generator: HandOff247
id: "data:users"
type: Data
source: "schema.sql"
---

# `users`

> id, email, role

- **Class:** Data table — A table named in an SQL statement.
- **Source:** [schema.sql:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/schema.sql#L1)

**is defined in** ←

- [`schema.sql`](../files/schema.sql.md) · [schema.sql:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/schema.sql#L1)

**is read by** ←

- [`GET /desk`](../features/GET-__desk.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET /review`](../features/GET-__review.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET,POST /login`](../features/GET-POST-__login.md) (db.find_user) · [db.py:30](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L30)
- [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

## Who reads and writes it

Defined at [schema.sql:1](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/schema.sql#L1).

Columns: `id`, `email`, `role`.

**Read by**

- [`anyone`](../users/anyone.md): "Continue" / "Sign in" ([`GET,POST /login`](../features/GET-POST-__login.md)) — [db.py:30](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L30) *(through `db.find_user`)*
- [`author`](../users/author.md): "My desk" ([`GET /desk`](../features/GET-__desk.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`author`](../users/author.md): "New article" / "Save draft" ([`GET,POST /desk/new`](../features/GET-POST-__desk__new.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`author`](../users/author.md): "Send for review" ([`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`editor`](../users/editor.md): "Review queue" ([`GET /review`](../features/GET-__review.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`editor`](../users/editor.md): review_detail ([`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`editor`](../users/editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`editor`](../users/editor.md): "Send back" ([`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- [`author`](../users/author.md), [`editor`](../users/editor.md): "Open the preview" ([`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md)) — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*

**Not verified**

- access through an ORM or SQL built at run time is not seen
