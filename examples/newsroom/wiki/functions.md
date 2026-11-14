---
generator: HandOff247
---

# Functions

Project code that a feature runs. Modelled once, however many features use it.

18 found. [Back to the index](index.md)

## `articles_of`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:39](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L39)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:39](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L39)

**runs for** ←

- [`GET /desk`](features/GET-__desk.md) · [app.py:58](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L58)

## `connect`

> run by 11 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8)

**runs for** ←

- [`GET /`](features/GET-__.md) (db.published_articles → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET /articles/<int:article_id>`](features/GET-__articles__-int-article_id.md) (db.get_article → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET /desk`](features/GET-__desk.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET /review`](features/GET-__review.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET /review/<int:article_id>`](features/GET-__review__-int-article_id.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`GET,POST /login`](features/GET-POST-__login.md) (db.find_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) (require_role → current_user → db.get_user → query) · [db.py:15](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L15)

## `create_article`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:43](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L43)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:43](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L43)

**runs for** ←

- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) · [app.py:67](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L67)

## `current_user`

> run by 8 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9)

**is defined in** ←

- [`auth.py`](files/auth.py.md) · [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9)

**runs for** ←

- [`GET /desk`](features/GET-__desk.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`GET /review`](features/GET-__review.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`GET /review/<int:article_id>`](features/GET-__review__-int-article_id.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) (require_role) · [auth.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L19)

## `execute`

> run by 4 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L19)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L19)

**runs for** ←

- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (db.create_article) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (db.send_for_review) · [db.py:49](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L49)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (db.publish_article) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) (db.return_to_author) · [db.py:61](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L61)

## `find_user`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:29](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L29)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:29](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L29)

**runs for** ←

- [`GET,POST /login`](features/GET-POST-__login.md) · [app.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L44)

## `get_article`

> run by 5 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:34](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L34)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:34](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L34)

**runs for** ←

- [`GET /articles/<int:article_id>`](features/GET-__articles__-int-article_id.md) · [app.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L25)
- [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) · [app.py:126](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L126)
- [`GET /review/<int:article_id>`](features/GET-__review__-int-article_id.md) · [app.py:96](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L96)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) · [app.py:76](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L76)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) · [app.py:102](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L102)

## `get_user`

> run by 8 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24)

**runs for** ←

- [`GET /desk`](features/GET-__desk.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`GET /review`](features/GET-__review.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`GET /review/<int:article_id>`](features/GET-__review__-int-article_id.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) (require_role → current_user) · [auth.py:11](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L11)

## `publish_article`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L56)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L56)

**runs for** ←

- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) · [app.py:109](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L109)

## `published_articles`

> run by 2 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:64](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L64)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:64](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L64)

**runs for** ←

- [`GET /`](features/GET-__.md) · [app.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L20)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) · [app.py:110](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L110)

## `query`

> run by 11 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14)

**runs for** ←

- [`GET /`](features/GET-__.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)
- [`GET /articles/<int:article_id>`](features/GET-__articles__-int-article_id.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`GET /desk`](features/GET-__desk.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET /review`](features/GET-__review.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET /review/<int:article_id>`](features/GET-__review__-int-article_id.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`GET,POST /login`](features/GET-POST-__login.md) (db.find_user) · [db.py:30](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L30)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

## `require_role`

> run by 8 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14)

**is defined in** ←

- [`auth.py`](files/auth.py.md) · [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14)

**runs for** ←

- [`GET /desk`](features/GET-__desk.md) · [app.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L56)
- [`GET /preview/<int:article_id>`](features/GET-__preview__-int-article_id.md) · [app.py:124](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L124)
- [`GET /review`](features/GET-__review.md) · [app.py:88](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L88)
- [`GET /review/<int:article_id>`](features/GET-__review__-int-article_id.md) · [app.py:94](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L94)
- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) · [app.py:62](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L62)
- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) · [app.py:74](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L74)
- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) · [app.py:100](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L100)
- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) · [app.py:115](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L115)

## `return_to_author`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:60](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L60)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:60](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L60)

**runs for** ←

- [`POST /review/<int:article_id>/return`](features/POST-__review__-int-article_id-__return.md) · [app.py:117](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L117)

## `safe_name`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [storage.py:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L10)

**is defined in** ←

- [`storage.py`](files/storage.py.md) · [storage.py:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L10)

**runs for** ←

- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) (storage.save_upload) · [storage.py:16](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L16)

## `save_upload`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [storage.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L14)

**is defined in** ←

- [`storage.py`](files/storage.py.md) · [storage.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L14)

**runs for** ←

- [`GET,POST /desk/new`](features/GET-POST-__desk__new.md) · [app.py:66](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L66)

## `send_for_review`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:48](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L48)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:48](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L48)

**runs for** ←

- [`POST /desk/<int:article_id>/submit`](features/POST-__desk__-int-article_id-__submit.md) · [app.py:80](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L80)

## `waiting_for_review`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [db.py:52](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L52)

**is defined in** ←

- [`db.py`](files/db.py.md) · [db.py:52](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L52)

**runs for** ←

- [`GET /review`](features/GET-__review.md) · [app.py:90](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L90)

## `write_published_list`

> run by 1 feature(s)

- **Class:** Function — Project code that a feature runs. Modelled once, however many features use it.
- **Source:** [storage.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L21)

**is defined in** ←

- [`storage.py`](files/storage.py.md) · [storage.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L21)

**runs for** ←

- [`POST /review/<int:article_id>/publish`](features/POST-__review__-int-article_id-__publish.md) · [app.py:110](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L110)
