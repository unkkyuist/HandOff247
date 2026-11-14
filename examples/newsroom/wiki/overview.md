---
generator: HandOff247
id: "project:Newsroom"
type: Project
---

# Newsroom

**What the previous owner says it is**

> A small publishing application that exists only as a test fixture for HandOff247 (`tests/fixtures/newsroom`). Authors write articles and upload a cover image, editors review and publish them, and readers see the published articles on the front page. It is not deployed anywhere; the notes below are example text.

- **Repository:** https://github.com/unkkyuist/HandOff247 at commit `3cdb94f`
- **Human-readable pack:** [README](../README.md), [handover checklist](../HANDOVER.md), [how to run it](../RUNNING.md), [connections](../CONNECTIONS.md), [code map](../CODEMAP.md)
- **What only the previous owner knew:** [notes](notes.md)

## What was found

| Class | Count | Where |
|---|---|---|
| Areas | 3 | [index](index.md), under Areas |
| Files | 18 | [index](index.md), under Files |
| HTTP routes | 13 | [index](index.md), under HTTP routes |
| Environment variables | 6 | [environment.md](environment.md) |
| Ports | 1 | [ports.md](ports.md) |
| Packages | 1 | [packages.md](packages.md) |
| User types | 3 | [index](index.md), under User types |
| Screens | 8 | [index](index.md), under Screens |
| Screen terms | 32 | [terms.md](terms.md) |
| Functions | 18 | [functions.md](functions.md) |
| Data tables | 2 | [index](index.md), under Data tables |
| States | 3 | [states.md](states.md) |
| Assets | 5 | [index](index.md), under Assets |

## Relations

**contains** →

- [`locales`](areas/locales.md)
- [`static`](areas/static.md)
- [`templates`](areas/templates.md)
- [`README.md`](files/README.md.md)
- [`app.py`](files/app.py.md)
- [`auth.py`](files/auth.py.md)
- [`db.py`](files/db.py.md)
- [`requirements.txt`](files/requirements.txt.md)
- [`schema.sql`](files/schema.sql.md)
- [`storage.py`](files/storage.py.md)
