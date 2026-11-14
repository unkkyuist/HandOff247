---
generator: HandOff247
---

# Screen terms

Words a user reads: a link, button, field label, heading, or a message the code shows.

32 found. [Back to the index](index.md)

| Text | Kind | Where | Shown when | Leads to |
|---|---|---|---|---|
| `Add a cover image before publishing` | message | [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) [app.py:107](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L107) |  |  |
| `Continue` | button | [`templates/login.html`](screens/templates__login.html.md) [templates/login.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L8) |  | [`GET,POST /login`](features/GET-POST-__login.md) |
| `Cover image` | field | [`templates/edit.html`](screens/templates__edit.html.md) [templates/edit.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L10) |  | [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) |
| `Download the list` | link | [`templates/home.html`](screens/templates__home.html.md) [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13) |  | [`GET /published.csv`](features/GET-__published.csv.md) |
| `Draft saved` | message | [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) [app.py:68](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L68) |  |  |
| `Editor's note` | column | [`templates/desk.html`](screens/templates__desk.html.md) [templates/desk.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L7) |  |  |
| `Front page` | link | [`templates/base.html`](screens/templates__base.html.md) [templates/base.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L12) |  | [`GET /`](features/GET-__.md) |
| `Headline` | column | [`templates/desk.html`](screens/templates__desk.html.md) [templates/desk.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L7) |  |  |
| `Headline` | field | [`templates/edit.html`](screens/templates__edit.html.md) [templates/edit.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L6) |  | [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) |
| `Latest articles` | heading | [`templates/home.html`](screens/templates__home.html.md) [templates/home.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L4) |  |  |
| `My desk` | link | [`templates/base.html`](screens/templates__base.html.md) [templates/base.html:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L14) | `user and user.role == 'author'` | [`GET /desk`](features/GET-__desk.md) |
| `My desk` | heading | [`templates/desk.html`](screens/templates__desk.html.md) [templates/desk.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L4) |  |  |
| `New article` | link | [`templates/desk.html`](screens/templates__desk.html.md) [templates/desk.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L5) |  | [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) |
| `New article` | heading | [`templates/edit.html`](screens/templates__edit.html.md) [templates/edit.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L4) |  |  |
| `Newsroom` | title | [`templates/base.html`](screens/templates__base.html.md) [templates/base.html:5](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L5) |  |  |
| `Only a draft can be sent for review` | message | [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) [app.py:78](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L78) |  |  |
| `Only an article in review can be published` | message | [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) [app.py:104](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L104) |  |  |
| `Open the preview` | link | [`templates/review_detail.html`](screens/templates__review_detail.html.md) [templates/review_detail.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L8) |  | [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) |
| `Publish` / `게시` | button | [`templates/review_detail.html`](screens/templates__review_detail.html.md) [templates/review_detail.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L10) |  | [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) |
| `Reason for the author` | field | [`templates/review_detail.html`](screens/templates__review_detail.html.md) [templates/review_detail.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L13) |  | [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) |
| `Review queue` / `검토 대기열` | link | [`templates/base.html`](screens/templates__base.html.md) [templates/base.html:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L17) | `user and user.role == 'editor'` | [`GET /review`](features/GET-__review.md) |
| `Review queue` / `검토 대기열` | heading | [`templates/review.html`](screens/templates__review.html.md) [templates/review.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review.html#L4) |  |  |
| `Save draft` | button | [`templates/edit.html`](screens/templates__edit.html.md) [templates/edit.html:12](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L12) |  | [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) |
| `Send back` | button | [`templates/review_detail.html`](screens/templates__review_detail.html.md) [templates/review_detail.html:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L15) |  | [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) |
| `Send for review` | button | [`templates/desk.html`](screens/templates__desk.html.md) [templates/desk.html:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L16) | `a.status == 'draft'` | [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) |
| `Sent to the editors` | message | [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) [app.py:81](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L81) |  |  |
| `Sign in` | link | [`templates/base.html`](screens/templates__base.html.md) [templates/base.html:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/base.html#L20) | `not user` | [`GET,POST /login`](features/GET-POST-__login.md) |
| `Sign in` | heading | [`templates/login.html`](screens/templates__login.html.md) [templates/login.html:4](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L4) |  |  |
| `State` | column | [`templates/desk.html`](screens/templates__desk.html.md) [templates/desk.html:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/desk.html#L7) |  |  |
| `Text` | field | [`templates/edit.html`](screens/templates__edit.html.md) [templates/edit.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L8) |  | [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) |
| `Unknown e-mail address` | message | [`GET,POST /login`](features/GET-POST-__login.md) [app.py:46](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L46) |  |  |
| `Work e-mail` | field | [`templates/login.html`](screens/templates__login.html.md) [templates/login.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/login.html#L6) |  | [`GET,POST /login`](features/GET-POST-__login.md) |
