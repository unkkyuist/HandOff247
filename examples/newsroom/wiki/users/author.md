---
generator: HandOff247
id: "user:author"
type: UserType
source: "app.py"
---

# `author`

> Reporters. They mostly ask why an article they sent is not on the front page yet: it is waiting in the editors' queue, or an editor sent it back with a note.

- **Class:** User type — A kind of user the analysed application tells apart, found from role checks. Not an access level of this pack.
- **Kind:** role
- **Source:** [app.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L56)

**Notes from the previous owner**

> Reporters. They mostly ask why an article they sent is not on the front page yet: it is waiting in the editors' queue, or an editor sent it back with a note.

## What this user type sees and does

> **Notes**
>
> Reporters. They mostly ask why an article they sent is not on the front page yet: it is waiting in the editors' queue, or an editor sent it back with a note.

The code tells this user type apart at [app.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L56), [app.py:62](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L62), [app.py:74](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L74), [app.py:124](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L124), [templates/base.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L13).

### Screen "My desk" — [`templates/desk.html`](../screens/templates__desk.html.md)

opened by [`GET /desk`](../features/GET-__desk.md) ([app.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57)); built on [`templates/base.html`](../screens/templates__base.html.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "New article" (link) | [templates/desk.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L5) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) → [new_article](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63) | shows `edit.html` |  |
| *(text set at run time)* (link) | [templates/desk.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L10) |  | [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) → [preview](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125) | shows `article.html` |  |
| "Send for review" (button) | [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16) | `a.status == 'draft'` | [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) → [submit](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75) | sets `articles.status = 'in_review'` | → [`editor`](editor.md): [`templates/review.html`](../screens/templates__review.html.md) (`articles.status = 'in_review'`, *inferred*)<br>→ [`editor`](editor.md): [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) (`articles.status = 'in_review'`, *inferred*) |
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "My desk" (link) | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) → [desk](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57) | shows `desk.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

### Screen "New article" — [`templates/edit.html`](../screens/templates__edit.html.md)

opened by [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) ([app.py:63](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63)); built on [`templates/base.html`](../screens/templates__base.html.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "Save draft" (button) | [templates/edit.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L12) |  | [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) → [new_article](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L63) | sets `articles.status = 'draft'`; stores the uploaded file | → `author`: [`templates/desk.html`](../screens/templates__desk.html.md) (`articles.status = 'draft'`, *inferred*)<br>→ `author`: [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) (`articles.status = 'draft'`, *inferred*) |
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "My desk" (link) | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) → [desk](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57) | shows `desk.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Fields: "Headline" → `title`; "Text" → `body`; "Cover image" → `cover`.

### Screen — [`templates/article.html`](../screens/templates__article.html.md)

opened by [`GET /preview/<int:article_id>`](../features/GET-__preview__-int-article_id.md) ([app.py:125](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L125)); built on [`templates/base.html`](../screens/templates__base.html.md); also seen by [`editor`](editor.md), [`anyone`](anyone.md).

| On the screen | Where | Shown when | Leads to | What the code does | Then |
|---|---|---|---|---|---|
| "Front page" (link) | [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) *(layout)* |  | [`GET /`](../features/GET-__.md) → [home](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L18) | lists rows with `status = 'published'`; shows `home.html` |  |
| "My desk" (link) | [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) *(layout)* | `user and user.role == 'author'` | [`GET /desk`](../features/GET-__desk.md) → [desk](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L57) | shows `desk.html` |  |
| "Sign in" (link) | [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) *(layout)* | `not user` | [`GET,POST /login`](../features/GET-POST-__login.md) → [login](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L42) | shows `login.html` |  |

Shows: [`upload:cover`](../assets/upload-cover.md).

Actions that show no page of their own:

- [`POST /desk/<int:article_id>/submit`](../features/POST-__desk__-int-article_id-__submit.md) — "Send for review" — [app.py:75](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L75) — sets `articles.status = 'in_review'`

## Other user types

Nothing here is hidden from you; follow a hand-over or open another user type: [`editor`](editor.md), [`anyone`](anyone.md).
