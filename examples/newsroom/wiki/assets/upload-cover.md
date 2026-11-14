---
generator: HandOff247
id: "asset:upload:cover"
type: Asset
source: "app.py"
---

# `upload:cover`

> uploaded; appears on 3 screen(s)

- **Class:** Asset — A file users see or provide: shipped with the project, uploaded, generated, or kept in external storage.
- **Kind:** uploaded
- **Seen by:** anyone, author, editor
- **Source:** [app.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L65)

**has its name kept in** →

- [`articles`](../data/articles.md) (column cover) · [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44)

**appears on** ←

- [`templates/article.html`](../screens/templates__article.html.md) (<img>) · [templates/article.html:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L9)
- [`templates/home.html`](../screens/templates__home.html.md) (<img>) · [templates/home.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L8)
- [`templates/review_detail.html`](../screens/templates__review_detail.html.md) (<img>) · [templates/review_detail.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L6)

**is provided by** ←

- [`GET,POST /desk/new`](../features/GET-POST-__desk__new.md) (receives it) · [app.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L65)

**is delivered by** ←

- [`GET /uploads/<path:name>`](../features/GET-__uploads__-path-name.md) (serves any file of the folder) · [app.py:33](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L33)

## Where it comes from and where it shows

**Kind:** uploaded

**Picked on the screen with**

- "Cover image" — [templates/edit.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/edit.html#L10)

**Registered or changed by**

- [`author`](../users/author.md): "New article" / "Save draft" ([`GET,POST /desk/new`](../features/GET-POST-__desk__new.md)) — [app.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L65)

**Stored by**

- [`author`](../users/author.md): "New article" / "Save draft" ([`GET,POST /desk/new`](../features/GET-POST-__desk__new.md)) — [storage.py:17](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L17) *(through `storage.save_upload`)* — `os.path.join(UPLOAD_DIR, name)`, folder from setting `NEWSROOM_UPLOADS`

**Linked data**

- the stored name is kept in [`articles`](../data/articles.md).`cover` — [db.py:44](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L44) *(through `db.create_article`)* *(traced through the variables)*

**Delivered by**

- [`anyone`](../users/anyone.md): uploaded ([`GET /uploads/<path:name>`](../features/GET-__uploads__-path-name.md)) — [app.py:33](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L33) — serves any file of that folder

**Appears on**

- [`templates/article.html`](../screens/templates__article.html.md) — seen by [`author`](../users/author.md), [`editor`](../users/editor.md), [`anyone`](../users/anyone.md)
- [`templates/home.html`](../screens/templates__home.html.md) — seen by [`anyone`](../users/anyone.md)
- [`templates/review_detail.html`](../screens/templates__review_detail.html.md) — seen by [`editor`](../users/editor.md)

**Referenced at**

- [templates/article.html:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/article.html#L9) — <img>, shown when `article.cover`
- [templates/home.html:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L8) — <img>, shown when `a.cover`
- [templates/review_detail.html:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L6) — <img>, shown when `article.cover`

**If it is replaced or deleted**

3 screen(s) show it, seen by [`anyone`](../users/anyone.md), [`author`](../users/author.md), [`editor`](../users/editor.md). These are the places the analysis found; a path built at run time is not seen.
