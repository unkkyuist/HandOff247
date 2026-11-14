---
generator: HandOff247
id: "area:tests"
type: Area
---

# `tests`

> `test_handoff.py` plus two fixtures. `fixtures/newsroom` is a small Flask application with three user types (author, editor, anyone) used by `UserContextTests`: one user type's action, the code, the data and upload it c…

- **Class:** Area — A top-level folder of the project.
- **Files:** 1

**Notes from the previous owner**

> `test_handoff.py` plus two fixtures. `fixtures/newsroom` is a small Flask application with three user types (author, editor, anyone) used by `UserContextTests`: one user type's action, the code, the data and upload it changes, the next user type's follow-up and the public page are asserted end to end, and the lines the analysis points at are checked in the fixture's files. `fixtures/mini`, a small fake app (C# + JS + Python + PowerShell + batch) wired the same way as PlayBookOS: three modes, one dispatch switch, HTTP route, MCP tools, launch scripts. Every connection type the tool claims to detect has an assertion here.

**contains** →

- [`tests/test_handoff.py`](../files/tests__test_handoff.py.md)

**is part of** ←

- [HandOff247](../overview.md)
