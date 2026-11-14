---
generator: HandOff247
id: "data:articles"
type: Data
source: "schema.sql"
---

# `articles`

> id, author_id, title, body, cover, status, review_note, published_at

- **Class:** Data table — A table named in an SQL statement.
- **Source:** [schema.sql:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/schema.sql#L7)

**has the state** →

- [`articles.status = 'draft'`](../states.md) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)
- [`articles.status = 'in_review'`](../states.md) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)
- [`articles.status = 'published'`](../states.md) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)

**is defined in** ←

- [`schema.sql`](../files/schema.sql.md) · [schema.sql:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/schema.sql#L7)

**is read by** ←

- [`GET /`](../features/GET-__.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)
- [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`GET /desk`](../features/GET-__desk.md) (db.articles_of) · [db.py:40](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L40)
- [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`GET /review`](../features/GET-__review.md) (db.waiting_for_review) · [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53)
- [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)

**is written by** ←

- [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) (db.create_article) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)
- [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) (db.send_for_review) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)
- [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) (db.publish_article) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)
- [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) (db.return_to_author) · [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61)

**keeps the name of** ←

- [`upload:cover`](../assets/upload-cover.md) (column cover) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)

## Who reads and writes it

Defined at [schema.sql:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/schema.sql#L7).

Columns: `id`, `author_id`, `title`, `body`, `cover`, `status`, `review_note`, `published_at`.

**Written by**

- [`author`](../users/author.md): "New article" / "Save draft" ([`GET,POST /desk/new`](../features/GET-POST-__desk__new.md)) — [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)*
- [`author`](../users/author.md): "Send for review" ([`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md)) — [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*
- [`editor`](../users/editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md)) — [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*
- [`editor`](../users/editor.md): "Send back" ([`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md)) — [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61) *(through `db.return_to_author`)*

**Read by**

- [`anyone`](../users/anyone.md): "Front page" ([`GET /`](../features/GET-__.md)) — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*
- [`anyone`](../users/anyone.md): article ([`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md)) — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
- [`author`](../users/author.md): "My desk" ([`GET /desk`](../features/GET-__desk.md)) — [db.py:40](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L40) *(through `db.articles_of`)*
- [`author`](../users/author.md): "Send for review" ([`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md)) — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
- [`editor`](../users/editor.md): "Review queue" ([`GET /review`](../features/GET-__review.md)) — [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*
- [`editor`](../users/editor.md): review_detail ([`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md)) — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
- [`editor`](../users/editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md)) — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
- [`editor`](../users/editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md)) — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*
- [`author`](../users/author.md), [`editor`](../users/editor.md): "Open the preview" ([`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md)) — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*

**States**

A value that one feature sets and another filters on is where work passes from one user type to the next.

| Value | Set by | Listed by (query filter) | Tested in a condition (same column and value, not traced) |
|---|---|---|---|
| `status = 'published'` | [`editor`](../users/editor.md): "Publish" — [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)* | [`anyone`](../users/anyone.md): "Front page" — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*<br>[`editor`](../users/editor.md): "Publish" — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)* | `row is None or row['status'] != 'published'` — [app.py:26](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L26) |
| `status = 'draft'` | [`author`](../users/author.md): "New article" / "Save draft" — [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)*<br>[`editor`](../users/editor.md): "Send back" — [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61) *(through `db.return_to_author`)* |  | `a.status == 'draft'` — [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16)<br>`row['status'] != 'draft'` — [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77) |
| `status = 'in_review'` | [`author`](../users/author.md): "Send for review" — [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)* | [`editor`](../users/editor.md): "Review queue" — [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)* | `row['status'] != 'in_review'` — [app.py:103](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L103) |

**Not verified**

- access through an ORM or SQL built at run time is not seen
