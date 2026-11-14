---
generator: HandOff247
id: "asset:generated:published.csv"
type: Asset
source: "storage.py"
---

# `generated:published.csv`

> generated; appears on 1 screen(s)

- **Class:** Asset — A file users see or provide: shipped with the project, uploaded, generated, or kept in external storage.
- **Kind:** generated
- **Seen by:** anyone
- **Source:** [storage.py:23](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L23)

**appears on** ←

- [`templates/home.html`](../screens/templates__home.html.md) (link "Download the list") · [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13)

**is provided by** ←

- [`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md) (writes it) · [storage.py:23](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L23)

**is delivered by** ←

- [`GET /published.csv`](../features/GET-__published.csv.md) · [app.py:38](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L38)

## Where it comes from and where it shows

**Kind:** generated

**Written by**

- [`editor`](../users/editor.md): "Publish" ([`POST /review/<int:article_id>/publish`](../features/POST-__review__-int-article_id-__publish.md)) — [storage.py:23](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L23) *(through `storage.write_published_list`)* — `os.path.join(EXPORT_DIR, 'published.csv')`, folder from setting `NEWSROOM_EXPORTS`

**Delivered by**

- [`anyone`](../users/anyone.md): "Download the list" ([`GET /published.csv`](../features/GET-__published.csv.md)) — [app.py:38](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L38)

**Appears on**

- [`templates/home.html`](../screens/templates__home.html.md) — seen by [`anyone`](../users/anyone.md)

**Referenced at**

- [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13) — link "Download the list"

**If it is replaced or deleted**

1 screen(s) show it, seen by [`anyone`](../users/anyone.md). These are the places the analysis found; a path built at run time is not seen.
