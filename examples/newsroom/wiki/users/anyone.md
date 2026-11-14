---
generator: HandOff247
id: "user:anyone"
type: UserType
---

# `anyone`

> no role check was found on the routes it uses

- **Class:** User type — A kind of user the analysed application tells apart, found from role checks. Not an access level of this pack.
- **Kind:** anyone

## What this user type sees and does

No role check was found on the routes below. A check made in middleware, a base class or the web server would not be seen.

### Screen "Latest articles" — [`templates/home.html`](../screens/templates__home.html.md)

opened by [`GET /`](../features/GET-__.md) ([app.py:18](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18)); built on [`templates/base.html`](../screens/templates__base.html.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| *(text set at run time)* (link) | [templates/home.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L10) |  | [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) → [article](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24) | shows `article.html` |  |
| "Download the list" (link) | [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13) |  | [`GET /published.csv`](../features/GET-__published.csv.md) → [published_list](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37) | sends a file |  |
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "My desk" (link) | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) → [desk](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)<br>*needs author* | shows `desk.html` |  |
| "Review queue" (link) | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)* | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) → [review_queue](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)<br>*needs editor* | lists rows with `status = 'in_review'`; shows `review.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Shows: [`upload:cover`](../assets/upload-cover.md), [`generated:published.csv`](../assets/generated-published.csv.md).

### Screen — [`templates/article.html`](../screens/templates__article.html.md)

opened by [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) ([app.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L24)); built on [`templates/base.html`](../screens/templates__base.html.md); also seen by [`author`](author.md), [`editor`](editor.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "My desk" (link) | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) → [desk](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)<br>*needs author* | shows `desk.html` |  |
| "Review queue" (link) | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)* | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) → [review_queue](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)<br>*needs editor* | lists rows with `status = 'in_review'`; shows `review.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Shows: [`upload:cover`](../assets/upload-cover.md).

### Screen "Sign in" — [`templates/login.html`](../screens/templates__login.html.md)

opened by [`GET,POST /login`](../features/GET-POST-__login.md) ([app.py:42](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42)); built on [`templates/base.html`](../screens/templates__base.html.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "Continue" (button) | [templates/login.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L8) |  | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "My desk" (link) | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) → [desk](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)<br>*needs author* | shows `desk.html` |  |
| "Review queue" (link) | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)* | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) → [review_queue](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)<br>*needs editor* | lists rows with `status = 'in_review'`; shows `review.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Fields: "Work e-mail" → `email`.

Actions that show no page of their own:

- [`GET /uploads/<path:name>`](../features/GET-__uploads__-path-name.md) — uploaded — [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32) — sends a file
- [`GET /published.csv`](../features/GET-__published.csv.md) — "Download the list" — [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37) — sends a file

Receives from other user types (*inferred*):

- from [`editor`](editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md)), because `articles.status = 'published'` — set at [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*, read at [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*

## Other user types

Nothing here is hidden from you; follow a hand-over or open another user type: [`author`](author.md), [`editor`](editor.md).
