---
generator: HandOff247
id: "file:handoff247/render_users.py"
type: File
source: "handoff247/render_users.py"
---

# `handoff247/render_users.py`

> Markdown for USERS.md and for the wiki pages of user types, features, screens, assets and data tables. `Ctx` holds how to link a source line and another page from where the text will live, so the same section renders in…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 469
- **Source:** [handoff247/render_users.py](../../../../handoff247/render_users.py)

**Notes from the previous owner**

> Markdown for USERS.md and for the wiki pages of user types, features, screens, assets and data tables. `Ctx` holds how to link a source line and another page from where the text will live, so the same section renders in the pack root and two folders down in the wiki.

**defines** →

- `Ctx` · [handoff247/render_users.py:40](../../../../handoff247/render_users.py#L40)

**imports** →

- [`handoff247/explore.py`](handoff247__explore.py.md) · [handoff247/render_users.py:11](../../../../handoff247/render_users.py#L11)
- [`handoff247/journeys.py`](handoff247__journeys.py.md) · [handoff247/render_users.py:12](../../../../handoff247/render_users.py#L12)
- [`handoff247/labels.py`](handoff247__labels.py.md) · [handoff247/render_users.py:13](../../../../handoff247/render_users.py#L13)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_users.py:384](../../../../handoff247/render_users.py#L384)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_md.py:249](../../../../handoff247/render_md.py#L249)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/wiki.py:31](../../../../handoff247/wiki.py#L31)

## Comment in the file

Markdown for the user-context view: USERS.md and the wiki pages of user types, features, screens, assets and data tables. *(module docstring)*

## Defined here

- `cell` — function, [line 18](../../../../handoff247/render_users.py#L18)
- `table` — function, [line 22](../../../../handoff247/render_users.py#L22)
- `code` — function, [line 32](../../../../handoff247/render_users.py#L32)
- `user_label` — function, [line 36](../../../../handoff247/render_users.py#L36)
- `Ctx` — class, [line 40](../../../../handoff247/render_users.py#L40) — Where a page lives: how to link a source line and how to link another page from here.
- `Ctx.ent` — method, [line 46](../../../../handoff247/render_users.py#L46)
- `Ctx.feat` — method, [line 50](../../../../handoff247/render_users.py#L50)
- `Ctx.screen` — method, [line 53](../../../../handoff247/render_users.py#L53)
- `Ctx.user` — method, [line 56](../../../../handoff247/render_users.py#L56)
- `Ctx.users` — method, [line 59](../../../../handoff247/render_users.py#L59)
- `Ctx.asset` — method, [line 62](../../../../handoff247/render_users.py#L62)
- `Ctx.data` — method, [line 65](../../../../handoff247/render_users.py#L65)
- `Ctx.at` — method, [line 68](../../../../handoff247/render_users.py#L68)
- `short` — function, [line 72](../../../../handoff247/render_users.py#L72) — File name of a screen, or its whole path when another screen has the same name.
- `does` — function, [line 78](../../../../handoff247/render_users.py#L78) — One line on what a feature changes, for a table cell.
- `then` — function, [line 110](../../../../handoff247/render_users.py#L110)
- `user_section` — function, [line 122](../../../../handoff247/render_users.py#L122)
- `feature_card` — function, [line 189](../../../../handoff247/render_users.py#L189)
- `screen_section` — function, [line 248](../../../../handoff247/render_users.py#L248)
- `asset_section` — function, [line 285](../../../../handoff247/render_users.py#L285)
- `data_section` — function, [line 332](../../../../handoff247/render_users.py#L332)
- `users_page` — function, [line 367](../../../../handoff247/render_users.py#L367)
