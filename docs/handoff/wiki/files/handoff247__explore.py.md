---
generator: HandOff247
id: "file:handoff247/explore.py"
type: File
source: "handoff247/explore.py"
---

# `handoff247/explore.py`

> `Explorer` answers a successor's questions from the journeys model: `users`/`user_flow` (from a user type), `find` (from words on a screen or a user's request), `asset` (from an asset or table), `impact` (from code), `f…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 718
- **Source:** [handoff247/explore.py](../../../../handoff247/explore.py)

**Notes from the previous owner**

> `Explorer` answers a successor's questions from the journeys model: `users`/`user_flow` (from a user type), `find` (from words on a screen or a user's request), `asset` (from an asset or table), `impact` (from code), `feature` (everything about one feature) and `overview` (the whole project). The pages, the MCP tools and `handoff247 trace` all call it, so they cannot disagree. `applies` keeps a GET link from being credited with what the POST branch of the same handler does. Every answer carries `not_verified` and the reminder that a condition in the code is not a diagnosis of a live problem.

**defines** →

- `Explorer` · [handoff247/explore.py:72](../../../../handoff247/explore.py#L72)

**imports** →

- [`handoff247/journeys.py`](handoff247__journeys.py.md) · [handoff247/explore.py:19](../../../../handoff247/explore.py#L19)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/explore.py:605](../../../../handoff247/explore.py#L605)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:113](../../../../handoff247/cli.py#L113)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:28](../../../../handoff247/mcp.py#L28)
- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/mermaid.py:472](../../../../handoff247/mermaid.py#L472)
- [`handoff247/ontology.py`](handoff247__ontology.py.md) · [handoff247/ontology.py:156](../../../../handoff247/ontology.py#L156)
- [`handoff247/render_users.py`](handoff247__render_users.py.md) · [handoff247/render_users.py:11](../../../../handoff247/render_users.py#L11)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/wiki.py:32](../../../../handoff247/wiki.py#L32)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:556](../../../../tests/test_handoff.py#L556)

## Comment in the file

Questions a successor asks, answered from the model in ``journeys.py``. *(module docstring)*

## Defined here

- `applies` — function, [line 30](../../../../handoff247/explore.py#L30) — False when an effect sits under ``if request.method == …`` for another HTTP method than the one a control uses: a link (GET) to a page does not run what its form (POST) runs.
- `tokens` — function, [line 44](../../../../handoff247/explore.py#L44)
- `Explorer` — class, [line 72](../../../../handoff247/explore.py#L72)
- `Explorer.who` — method, [line 88](../../../../handoff247/explore.py#L88)
- `Explorer.who_sees` — method, [line 92](../../../../handoff247/explore.py#L92)
- `Explorer.screen_terms` — method, [line 106](../../../../handoff247/explore.py#L106) — Terms of a screen, then those of the layouts it extends and the partials it includes.
- `Explorer.triggers` — method, [line 121](../../../../handoff247/explore.py#L121) — Where on which screen a user starts this feature.
- `Explorer.label` — method, [line 136](../../../../handoff247/explore.py#L136) — A feature named the way a user would: by the control that starts it or the page it shows.
- `Explorer.handoffs_from` — method, [line 146](../../../../handoff247/explore.py#L146) — Who picks the work up after this feature.
- `Explorer.handoffs_to` — method, [line 181](../../../../handoff247/explore.py#L181)
- `Explorer.users` — method, [line 193](../../../../handoff247/explore.py#L193)
- `Explorer.user_flow` — method, [line 206](../../../../handoff247/explore.py#L206)
- `Explorer.feature` — method, [line 253](../../../../handoff247/explore.py#L253)
- `Explorer.find` — method, [line 379](../../../../handoff247/explore.py#L379)
- `Explorer.asset` — method, [line 467](../../../../handoff247/explore.py#L467)
- `Explorer.impact` — method, [line 507](../../../../handoff247/explore.py#L507)
- `Explorer.overview` — method, [line 602](../../../../handoff247/explore.py#L602)
- `format_find` — function, [line 661](../../../../handoff247/explore.py#L661)
- `format_feature` — function, [line 688](../../../../handoff247/explore.py#L688)
