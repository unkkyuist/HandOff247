---
generator: HandOff247
id: "file:handoff247/screens.py"
type: File
source: "handoff247/screens.py"
---

# `handoff247/screens.py`

> Reads templates and HTML pages as text: the visible terms (links, buttons, field labels, headings), the link target or form each belongs to, the `{% if %}` conditions around it, the layout it extends, and the files it r…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 439
- **Source:** [handoff247/screens.py](../../../../handoff247/screens.py)

**Notes from the previous owner**

> Reads templates and HTML pages as text: the visible terms (links, buttons, field labels, headings), the link target or form each belongs to, the `{% if %}` conditions around it, the layout it extends, and the files it references. `Locales` resolves translation keys through JSON locale files and keeps the text of every language, so a term is found by the word a user reads. `roles_in` only reports a role for a positive test (`==`, `in`, `has_role`); a negated test names a role without saying who passes, so it yields nothing. Jinja, Django, Twig, Nunjucks and Handlebars conditions are read; EJS, ERB and Razor are not.

**defines** →

- `Locales` · [handoff247/screens.py:87](../../../../handoff247/screens.py#L87)

**imports** →

- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/screens.py:19](../../../../handoff247/screens.py#L19)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/journeys.py`](handoff247__journeys.py.md) · [handoff247/journeys.py:24](../../../../handoff247/journeys.py#L24)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:872](../../../../tests/test_handoff.py#L872)

## Comment in the file

What a person sees: screens (templates and HTML pages) and the words on them. *(module docstring)*

## Defined here

- `is_template` — function, [line 55](../../../../handoff247/screens.py#L55)
- `roles_in` — function, [line 59](../../../../handoff247/screens.py#L59) — Role names a template condition tests for with ==, ``in`` or a has-role call.
- `Locales` — class, [line 87](../../../../handoff247/screens.py#L87) — Translation resources: flat ``key -> text`` per language, with the line of each key.
- `Locales.lookup` — method, [line 129](../../../../handoff247/screens.py#L129) — English text first; the same key in other languages is kept as alternatives, so a term can be found by the word a user of another language reads.
- `classify_url` — function, [line 152](../../../../handoff247/screens.py#L152) — What a link, form action or src points at, as far as the text says.
- `parse_template` — function, [line 193](../../../../handoff247/screens.py#L193)
- `css_refs` — function, [line 414](../../../../handoff247/screens.py#L414) — url(…) references of a stylesheet, with their lines.
- `resolve_template` — function, [line 424](../../../../handoff247/screens.py#L424) — The project file a template name such as ``admin/list.html`` refers to: next to the file that names it, or the one file whose path ends with the name.
