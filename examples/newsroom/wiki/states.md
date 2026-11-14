---
generator: HandOff247
---

# States

A column value that statements set or filter on, such as status = 'published'.

3 found. [Back to the index](index.md)

## `articles.status = 'draft'`

> set by 2, listed by 0 feature(s)

- **Class:** State — A column value that statements set or filter on, such as status = 'published'.
- **Source:** [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)

**is tested by** →

- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (row['status'] != 'draft') · [app.py:77](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L77) · *inferred: the condition names the same column and value; not traced to the same rows*
- [`templates/desk.html`](screens/templates__desk.html.md) (a.status == 'draft') · [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16) · *inferred: the condition names the same column and value; not traced to the same rows*

**is a state of** ←

- [`articles`](data/articles.md) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)

**is set by** ←

- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (db.create_article) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) (db.return_to_author) · [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61)

## `articles.status = 'in_review'`

> set by 1, listed by 1 feature(s)

- **Class:** State — A column value that statements set or filter on, such as status = 'published'.
- **Source:** [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)

**is tested by** →

- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (row['status'] != 'in_review') · [app.py:103](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L103) · *inferred: the condition names the same column and value; not traced to the same rows*

**is a state of** ←

- [`articles`](data/articles.md) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)

**is set by** ←

- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (db.send_for_review) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)

**is the filter of** ←

- [`GET /review`](features/GET-__review.md) (db.waiting_for_review) · [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53)

## `articles.status = 'published'`

> set by 1, listed by 2 feature(s)

- **Class:** State — A column value that statements set or filter on, such as status = 'published'.
- **Source:** [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)

**is tested by** →

- [`GET /articles/<int:article_id>`](features/GET-__articles__-int-article_id.md) (row is None or row['status'] != 'published') · [app.py:26](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L26) · *inferred: the condition names the same column and value; not traced to the same rows*

**is a state of** ←

- [`articles`](data/articles.md) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)

**is set by** ←

- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (db.publish_article) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)

**is the filter of** ←

- [`GET /`](features/GET-__.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)
