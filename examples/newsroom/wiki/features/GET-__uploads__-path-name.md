---
generator: HandOff247
id: "route:GET /uploads/<path:name>"
type: Route
source: "app.py"
---

# `GET /uploads/<path:name>`

> handler `uploaded`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)

**delivers** →

- [`upload:cover`](../assets/upload-cover.md) (serves any file of the folder) · [app.py:33](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L33)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)

**Called:** uploaded  
**User types:** [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. GET /uploads/<path:name> runs `uploaded` — [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)
2. sends a file from send_from_directory(storage.UPLOAD_DIR, name) — [app.py:33](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L33)

## Code

- handler `uploaded` — [app.py:32](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L32)

## Data and assets

- [`upload:cover`](../assets/upload-cover.md) (uploaded): served

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_UPLOADS` (variable `UPLOAD_DIR`) — [app.py:33](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L33)

## Not verified by the analysis

- no access check was found on the route; a check made in middleware or a base class would not be seen
- no link, button or script call that starts this feature was found on a screen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
