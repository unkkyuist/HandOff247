---
generator: HandOff247
id: "route:POST /review/<int:article_id>/publish"
type: Route
source: "app.py"
---

# `POST /review/<int:article_id>/publish`

> handler `publish`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101)

**is open to** →

- [`editor`](../users/editor.md) (@require_role('editor')) · [app.py:100](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L100)

**redirects to** →

- [`GET /review`](GET-__review.md) · [app.py:111](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L111)
- [`GET /review/<int:article_id>`](GET-__review__-int-article_id.md) (COVER_REQUIRED == '1' and (not row['cover'])) · [app.py:108](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L108)
- [`GET,POST /login`](GET-POST-__login.md) (user is None) · [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21)

**reads** →

- [`articles`](../data/articles.md) (db.get_article) · [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35)
- [`users`](../data/users.md) (require_role → current_user → db.get_user) · [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25)

**writes** →

- [`articles`](../data/articles.md) (db.publish_article) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)

**sets** →

- [`articles.status = 'published'`](../states.md) (db.publish_article) · [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57)

**lists only** →

- [`articles.status = 'published'`](../states.md) (db.published_articles) · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65)

**hands over to** →

- [`GET /`](GET-__.md) (articles.status = 'published') · [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) · *inferred: one statement sets this value and the other filters on it; that the same rows are meant was not verified*

**provides** →

- [`generated:published.csv`](../assets/generated-published.csv.md) (writes it) · [storage.py:23](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L23)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101)

**is started from** ←

- [`Publish`](../terms.md) (POST) · [templates/review_detail.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L10)

**tests** ←

- [`articles.status = 'in_review'`](../states.md) (row['status'] != 'in_review') · [app.py:103](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L103) · *inferred: the condition names the same column and value; not traced to the same rows*

**Called:** "Publish"  
**User types:** [`editor`](../users/editor.md)

## Started from

- button "Publish" on [`templates/review_detail.html`](../screens/templates__review_detail.html.md) ([templates/review_detail.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L10)) — seen by [`editor`](../users/editor.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. editor: button "Publish" on templates/review_detail.html — [templates/review_detail.html:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/review_detail.html#L10)
2. the route lets through role editor (@require_role('editor')) — [app.py:100](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L100)
3. POST /review/<int:article_id>/publish runs `publish` — [app.py:101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101)
4. *when* `user_id`: reads users — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
5. *when* `user is None`: redirects to GET,POST /login — [auth.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L21) *(through `require_role`)*
6. reads articles — [db.py:35](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L35) *(through `db.get_article`)*
7. *when* `row['status'] != 'in_review'`: shows the message "Only an article in review can be published" — [app.py:104](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L104)
8. *when* `row['status'] != 'in_review'`: redirects to GET /review — [app.py:105](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L105)
9. *when* `COVER_REQUIRED == '1' and (not row['cover'])`: shows the message "Add a cover image before publishing" — [app.py:107](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L107)
10. *when* `COVER_REQUIRED == '1' and (not row['cover'])`: redirects to GET /review/<int:article_id> — [app.py:108](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L108)
11. updates articles; sets status = 'published' — [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*
12. writes the file os.path.join(EXPORT_DIR, 'published.csv') — [storage.py:23](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L23) *(through `storage.write_published_list`)*
13. reads articles; only rows with status = 'published' — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*
14. redirects to GET /review — [app.py:111](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L111)

## Branches

| If | Then | Where |
|---|---|---|
| `row['status'] != 'in_review'` | shows the message "Only an article in review can be published"; redirects to `review_queue` | [app.py:103](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L103) |
| `COVER_REQUIRED == '1' and (not row['cover'])` | shows the message "Add a cover image before publishing"; redirects to `review_detail` | [app.py:106](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L106) |
| `user is None` | redirects to `login` | [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)* |
| `user['role'] not in roles` | stops with abort(403) | [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)* |

## Hand-overs

*Inferred:* derived from a column value that one statement sets and another tests.

- → [`anyone`](../users/anyone.md): [`GET /`](GET-__.md) ([`templates/home.html`](../screens/templates__home.html.md)), because `articles.status = 'published'` — set at [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*, tested at [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*
- → [`anyone`](../users/anyone.md): [`GET /articles/<int:article_id>`](GET-__articles__-int-article_id.md), because `articles.status = 'published'`; then stops with abort(404) — set at [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*, tested at [app.py:26](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L26)

## Code

- handler `publish` — [app.py:101](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L101)
- `require_role` — [auth.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L14) — shared with 7 other feature(s)
- `current_user` — [auth.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L9) — shared with 7 other feature(s)
- `get_user` — [db.py:24](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L24) — shared with 7 other feature(s)
- `query` — [db.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L14) — shared with 10 other feature(s)
- `connect` — [db.py:8](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L8) — shared with 10 other feature(s)
- `get_article` — [db.py:34](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L34) — shared with 4 other feature(s)
- `publish_article` — [db.py:56](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L56)
- `execute` — [db.py:19](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L19) — shared with 3 other feature(s)
- `write_published_list` — [storage.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L21)
- `published_articles` — [db.py:64](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L64) — shared with 1 other feature(s)

## Data and assets

- table [`users`](../data/users.md): reads — [db.py:25](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L25) *(through `require_role → current_user → db.get_user`)*
- table [`articles`](../data/articles.md): reads, writes, sets `status = 'published'`, only rows with `status = 'published'` — [db.py:57](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L57) *(through `db.publish_article`)*
- [`generated:published.csv`](../assets/generated-published.csv.md) (generated): written

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_DB` (variable `DB_PATH`) — [db.py:9](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L9) *(through `db.publish_article → execute → connect`)*
- setting `NEWSROOM_EXPORTS` (variable `EXPORT_DIR`) — [storage.py:23](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L23) *(through `storage.write_published_list`)*
- setting `NEWSROOM_COVER_REQUIRED` (variable `COVER_REQUIRED`) — [app.py:106](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L106)
- condition `row['status'] != 'in_review'` → shows the message "Only an article in review can be published"; redirects to `review_queue` — [app.py:103](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L103)
- condition `COVER_REQUIRED == '1' and (not row['cover'])` → shows the message "Add a cover image before publishing"; redirects to `review_detail` — [app.py:106](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L106)
- condition `user is None` → redirects to `login` — [auth.py:20](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L20) *(through `require_role`)*
- condition `user['role'] not in roles` → stops with abort(403) — [auth.py:22](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/auth.py#L22) *(through `require_role`)*
- the query only returns rows with articles.status = 'published' — [db.py:65](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/db.py#L65) *(through `db.published_articles`)*

## Not verified by the analysis

- hand-overs are derived from a shared column value, not traced row by row

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
