---
generator: HandOff247
id: "user:editor"
type: UserType
source: "app.py"
---

# `editor`

> The news desk. They mostly ask about articles that will not publish and about cover images that do not show.

- **Class:** User type — A kind of user the analysed application tells apart, found from role checks. Not an access level of this pack.
- **Kind:** role
- **Source:** [app.py:88](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L88)

**Notes from the previous owner**

> The news desk. They mostly ask about articles that will not publish and about cover images that do not show.

## What this user type sees and does

> **Notes**
>
> The news desk. They mostly ask about articles that will not publish and about cover images that do not show.

The code tells this user type apart at [app.py:88](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L88), [app.py:94](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L94), [app.py:100](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L100), [app.py:115](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L115), [app.py:124](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L124), [templates/base.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L16).

### Screen "Review queue" — [`templates/review.html`](../screens/templates__review.html.md)

opened by [`GET /review`](../features/GET-__review.md) ([app.py:89](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89)); built on [`templates/base.html`](../screens/templates__base.html.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| *(text set at run time)* (link) | [templates/review.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L7) |  | [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) → [review_detail](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95) | shows `review_detail.html` |  |
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "Review queue" (link) | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)* | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) → [review_queue](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89) | lists rows with `status = 'in_review'`; shows `review.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

### Screen — [`templates/review_detail.html`](../screens/templates__review_detail.html.md)

opened by [`GET /review/<int:article_id>`](../features/GET-__review__-int-article_id.md) ([app.py:95](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L95)); built on [`templates/base.html`](../screens/templates__base.html.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "Open the preview" (link) | [templates/review_detail.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L8) |  | [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) → [preview](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125) | shows `article.html` |  |
| "Publish" (button) | [templates/review_detail.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L10) |  | [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) → [publish](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101) | sets `articles.status = 'published'`; writes a file | → [`anyone`](anyone.md): [`templates/home.html`](../screens/templates__home.html.md) (`articles.status = 'published'`, *inferred*)<br>→ [`anyone`](anyone.md): [`GET /articles/<int:article_id>`](../features/GET-__articles__-int-article_id.md) (`articles.status = 'published'`, *inferred*) |
| "Send back" (button) | [templates/review_detail.html:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L15) |  | [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) → [send_back](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116) | sets `articles.status = 'draft'` | → [`author`](author.md): [`templates/desk.html`](../screens/templates__desk.html.md) (`articles.status = 'draft'`, *inferred*)<br>→ [`author`](author.md): [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) (`articles.status = 'draft'`, *inferred*) |
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "Review queue" (link) | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)* | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) → [review_queue](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89) | lists rows with `status = 'in_review'`; shows `review.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Fields: "Reason for the author" → `reason`.

Shows: [`upload:cover`](../assets/upload-cover.md).

### Screen — [`templates/article.html`](../screens/templates__article.html.md)

opened by [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) ([app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)); built on [`templates/base.html`](../screens/templates__base.html.md); also seen by [`author`](author.md), [`anyone`](anyone.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "Review queue" (link) | [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) *(layout)* | `user and user.role == 'editor'` | [`GET /review`](../features/GET-__review.md) → [review_queue](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L89) | lists rows with `status = 'in_review'`; shows `review.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Shows: [`upload:cover`](../assets/upload-cover.md).

Actions that show no page of their own:

- [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) — "Publish" — [app.py:101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101) — sets `articles.status = 'published'`; writes a file
- [`POST /review/<int:article_id>/return`](../features/POST-__review__-int-article_id-__return.md) — "Send back" — [app.py:116](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L116) — sets `articles.status = 'draft'`

Receives from other user types (*inferred*):

- from [`author`](author.md): "Send for review" ([`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md)), because `articles.status = 'in_review'` — set at [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49) *(through `db.send_for_review`)*, read at [db.py:53](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L53) *(through `db.waiting_for_review`)*

## Other user types

Nothing here is hidden from you; follow a hand-over or open another user type: [`author`](author.md), [`anyone`](anyone.md).
