---
generator: HandOff247
id: "file:storage.py"
type: File
source: "storage.py"
---

# `storage.py`

> Files on disk: cover images that authors upload and the list that publishing writes.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 27
- **Source:** [storage.py](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py)

**defines** →

- [`safe_name`](../functions.md) · [storage.py:10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L10)
- [`save_upload`](../functions.md) · [storage.py:14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L14)
- [`write_published_list`](../functions.md) · [storage.py:21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L21)

**reads** →

- [`NEWSROOM_EXPORTS`](../environment.md) · [storage.py:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L7)
- [`NEWSROOM_UPLOADS`](../environment.md) · [storage.py:6](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L6)

**is part of** ←

- [Newsroom](../overview.md)

**is imported by** ←

- [`app.py`](app.py.md) · [app.py:7](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L7)

## Defined here

- `safe_name` — function, [line 10](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L10)
- `save_upload` — function, [line 14](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L14) — Store an uploaded file and return the name it was stored under.
- `write_published_list` — function, [line 21](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/storage.py#L21) — Rewrite the CSV of published articles that readers can download.
