---
generator: HandOff247
id: "file:app.py"
type: File
source: "app.py"
---

# `app.py`

> Newsroom: authors write articles, editors review and publish them, readers see the result.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 130
- **Source:** [app.py](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py)

**defines** →

- [`GET /`](../features/GET-__.md) · [app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)
- [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) · [app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)
- [`GET /desk`](../features/GET-__desk.md) · [app.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)
- [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) · [app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)
- [`GET /published.csv`](../features/GET-__published.csv.md) · [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)
- [`GET /review`](../features/GET-__review.md) · [app.py:89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)
- [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) · [app.py:95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)
- [`GET /uploads/<path:name>`](../features/GET-__uploads__-path-name.md) · [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)
- [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) · [app.py:63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)
- [`GET,POST /login`](../features/GET-POST-__login.md) · [app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)
- [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) · [app.py:75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75)
- [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) · [app.py:101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101)
- [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) · [app.py:116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116)

**imports** →

- [`auth.py`](auth.py.md) · [app.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L8)
- [`db.py`](db.py.md) · [app.py:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L6)
- [`storage.py`](storage.py.md) · [app.py:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L7)

**refers to** →

- [`templates/article.html`](templates__article.html.md) · [app.py:28](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L28)
- [`templates/desk.html`](templates__desk.html.md) · [app.py:58](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L58)
- [`templates/edit.html`](templates__edit.html.md) · [app.py:70](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L70)
- [`templates/home.html`](templates__home.html.md) · [app.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L20)
- [`templates/login.html`](templates__login.html.md) · [app.py:50](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L50)
- [`templates/review.html`](templates__review.html.md) · [app.py:90](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L90)
- [`templates/review_detail.html`](templates__review_detail.html.md) · [app.py:96](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L96)

**reads** →

- [`NEWSROOM_COVER_REQUIRED`](../environment.md) · [app.py:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L12)
- [`NEWSROOM_PORT`](../environment.md) · [app.py:130](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L130)
- [`NEWSROOM_SECRET`](../environment.md) · [app.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L11)

**mentions** →

- [`5080`](../ports.md) (NEWSROOM_PORT default) · [app.py:130](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L130)

**depends on** →

- [`flask`](../packages.md) (imported) · [app.py](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py)

**is part of** ←

- [Newsroom](../overview.md)

## Defined here

- `home` — function, [line 18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) — Front page: the published articles.
- `article` — function, [line 24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)
- `uploaded` — function, [line 32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)
- `published_list` — function, [line 37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)
- `login` — function, [line 42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)
- `desk` — function, [line 57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)
- `new_article` — function, [line 63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)
- `submit` — function, [line 75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75)
- `review_queue` — function, [line 89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)
- `review_detail` — function, [line 95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)
- `publish` — function, [line 101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101)
- `send_back` — function, [line 116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116)
- `preview` — function, [line 125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)
