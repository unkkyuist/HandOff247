---
generator: HandOff247
id: "route:GET /published.csv"
type: Route
source: "app.py"
---

# `GET /published.csv`

> handler `published_list`

- **Class:** HTTP route — An HTTP endpoint the program serves.
- **Source:** [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)

**is open to** →

- [`anyone`](../users/anyone.md) (no role check found) · [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)

**delivers** →

- [`generated:published.csv`](../assets/generated-published.csv.md) · [app.py:38](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L38)

**is defined in** ←

- [`app.py`](../files/app.py.md) · [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)

**is started from** ←

- [`Download the list`](../terms.md) (GET) · [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13)

**Called:** "Download the list"  
**User types:** [`anyone`](../users/anyone.md)

## Started from

- link "Download the list" on [`templates/home.html`](../screens/templates__home.html.md) ([templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13)) — seen by [`anyone`](../users/anyone.md)

## What the code does

In the order of the handler. A step that starts with *when* only runs under that condition.

1. anyone: link "Download the list" on templates/home.html — [templates/home.html:13](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/templates/home.html#L13)
2. GET /published.csv runs `published_list` — [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)
3. sends a file from send_from_directory(storage.EXPORT_DIR, 'published.csv') — [app.py:38](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L38)

## Code

- handler `published_list` — [app.py:37](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L37)

## Data and assets

- [`generated:published.csv`](../assets/generated-published.csv.md) (generated): served

## What to check

Settings, states and outside dependencies this feature depends on.

- setting `NEWSROOM_EXPORTS` (variable `EXPORT_DIR`) — [app.py:38](https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/app.py#L38)

## Not verified by the analysis

- no access check was found on the route; a check made in middleware or a base class would not be seen

*This is what the code does and under which conditions, read without running it. It does not tell which condition applied to this user: check the live data, settings and logs at the points listed under `check`.*
