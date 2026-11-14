# HandOff247 notes · HandOff247

<!--
HandOff247 notes. Write in plain sentences under each heading; the text is shown next to that item in the handoff pack.
Lines that still start with TODO count as undocumented. Keep the headings exactly as they are (they are matched by name).
Never paste passwords or tokens here — say where they are kept instead.
-->

## Project
HandOff247 reads a project folder and writes a handoff pack for the next person: diagrams, structure, extracted comments and a map of how the tools connect. It is static analysis only (it never imports or runs the target's code) and it is standard-library Python, so `python -m handoff247` works on any machine with Python 3.10+.
Status: v0.6.0. `python -m handoff247 <folder>` does everything in one step (notes file, pack, handover checklist), and a folder that holds several projects gets one pack per project plus an index. Since v0.4.0 every pack also holds the ontology (`ontology.json`), a graph of it in the viewer, and a wiki for AI assistants (`wiki/`, `llms.txt`). v0.6.0 adds the user-context view: who uses the analysed application (user types found from role checks), what each of them sees and can do, how work passes from one user type to the next, the words on the screens, and assets in context (USERS.md, the Users tab, `handoff247 trace`, seven more MCP tools; see `examples/newsroom`). v0.5.0 added optional file summaries written through the signed-in Codex CLI (`--summarize`) and an MCP server (`handoff247 mcp`) through which an AI agent reads the project and writes notes. The first real target was PlayBookOS (see examples/playbookos). C#, Python, JavaScript/TypeScript, PowerShell, shell and batch have analyzers; other languages are inventoried but not parsed. Output is English; a project's own comments and headings in another language get English versions from the notes file's `## Translations` table.

## Topic: Successor checklist
1. Run the tests: `python -m unittest discover -s tests`.
2. Regenerate the examples after any analyzer change (`examples/newsroom` too: `python -m handoff247 build tests/fixtures/newsroom --name Newsroom -o examples/newsroom --notes examples/newsroom.notes.md --date <date> --link-base https://github.com/unkkyuist/HandOff247/blob/main/tests/fixtures/newsroom/`): `python -m handoff247 build <PlayBookOS checkout> --name PlayBookOS -o examples/playbookos --notes examples/playbookos.notes.md --date <date>`. If an analyzer change surfaces new Korean comments or headings, `check --notes examples/playbookos.notes.md` reports them; add their rows to the Translations table there. Read the diff of the generated pages: a change there is a change in what successors will be told.
3. Regenerate this pack after committing and pushing, so its Handover page does not report your own work as uncommitted: `python -m handoff247 . --date <date>`.
4. Open `index.html` of a pack in a browser and check that every diagram renders (Mermaid errors show as red text in the page).

## Topic: Known issues and risks
- The rule that matters most: a wrong statement is worse than a missing one. When a pattern is ambiguous the analyzers leave it out; inferences (for example a wrapper passed in as a parameter) are labelled and drawn dashed. Keep it that way.
- Analysis is regex/lexer based for everything except Python (which uses `ast`). Code built from runtime strings, reflection or dependency-injection containers is not followed.
- MCP tool names from the C# SDK are derived from method names (snake_case, `Async` removed) and marked with * in the pack.
- Mermaid labels must go through `mermaid.esc`; `*`, `_` and backticks are escaped because Mermaid otherwise formats them as Markdown.

## Topic: Credentials and accounts
None. The tool needs no keys. The GitHub Action only uses the workflow's own checkout.

## Topic: Open work and next steps
- A folder of projects has a graph and a wiki per project but no single graph across projects; `workspace.py` only writes an `llms.txt` that links them.
- Codex is the only engine for `--summarize` (`summarize.codex_call`). Another signed-in CLI (Claude Code's `claude -p`, for example) would be a second function with the same signature: prompt in, JSON text out.
- The MCP server is tested by driving it over stdio (`test_mcp_server`) and was tried once by hand with Codex. It speaks protocol versions up to 2025-11-25 and offers tools only, no resources or prompts.
- The user-context view follows Python handlers only (Flask-style routes, SQL written as strings). An ORM, Django URL patterns, and handlers in JavaScript or C# are not followed; their routes are listed with what sits on the route itself and reported under "Not verified". Controls of a single-page app that a script wires up are listed without a target. The next analyzers to write are an Express handler reader and an ORM model reader, each with an assertion per fact in `UserContextTests`.
- Go, Rust, Java and other languages are only inventoried. An analyzer for one of them is the natural next piece: copy the shape of `analyzers/python.py` and add an assertion per fact to the tests.
- The workspace index has no example in `examples/`; it is covered by `test_go_folder_of_projects` only.

## Topic: Deploy and release
There is no server and no package upload. A release is a push to `main` on GitHub; people run it from a clone or use the repository as a GitHub Action (`uses: unkkyuist/HandOff247@main`), so `main` is what users get. Bump the version in `handoff247/__init__.py` and `pyproject.toml` together. To roll back, revert the commit.

## Topic: Routine operations
Nothing runs on a schedule. CI runs on every push and pull request. The viewer loads marked, DOMPurify and Mermaid from jsDelivr at pinned versions (`render_html.py`); check now and then that those versions still load.

## Topic: Data and backups
The tool stores nothing. Its only state is the Git repository. Generated packs can always be rebuilt; a project's `HANDOFF.notes.md` cannot, so it belongs in that project's repository.

## Topic: People and contacts
Owner: the GitHub account `unkkyuist` (issues on the repository). There are no other maintainers and no known outside users yet.

## Area: .github
CI: unit tests on Linux and Windows (Python 3.10 and 3.12), a self-documentation run, and a run of the composite action against the test fixture.

## Area: handoff247
The package. Data flows inventory → analyzers → connect → (mermaid, render_md, render_html) → build. pipeline.py wires the first three; cli.py and build.py the rest.

## Area: tests
`test_handoff.py` plus two fixtures. `fixtures/newsroom` is a small Flask application with three user types (author, editor, anyone) used by `UserContextTests`: one user type's action, the code, the data and upload it changes, the next user type's follow-up and the public page are asserted end to end, and the lines the analysis points at are checked in the fixture's files. `fixtures/mini`, a small fake app (C# + JS + Python + PowerShell + batch) wired the same way as PlayBookOS: three modes, one dispatch switch, HTTP route, MCP tools, launch scripts. Every connection type the tool claims to detect has an assertion here.

## File: handoff247/__init__.py
Holds `__version__`; the version is printed in every generated page.

## File: handoff247/__main__.py
Lets `python -m handoff247` run the CLI.

## File: handoff247/analyzers/__init__.py
Maps a file's language to its analyzer. An exception inside one analyzer marks only that file as "not parsed"; it never stops the run.

## File: handoff247/analyzers/csharp.py
The richest analyzer: types and primary-constructor dependencies, entry modes (`if (mode == "x")` in the entry file), `switch` dispatch tables with handler resolution, minimal-API routes, `[McpServerTool]` methods, environment variables and `Path.Combine` literals.

## File: handoff247/analyzers/docs.py
Markdown (summary, headings, relative links, code blocks for `<mode> <op>` usage), plus config formats: .csproj, package.json, pyproject, requirements, MCP client configs (`mcpServers` / `[mcp_servers]`), Dockerfile, GitHub workflows.

## File: handoff247/analyzers/python.py
Uses `ast`, never imports the file. Finds argparse sub-commands, subprocess launches (rendered with `{variable}` placeholders), env reads/writes, dict/if-chain/match dispatch tables, Flask/FastAPI routes and MCP tool decorators.

## File: handoff247/analyzers/shell.py
PowerShell, POSIX shell and batch: leading comment / .SYNOPSIS as summary, `$env:` / `export` / `set` variables, and command lines that launch something (dotnet, python, powershell -File, `&` call operator, start URL).

## File: handoff247/analyzers/web.py
JavaScript/TypeScript (imports, exported functions with spans, `fetch` calls, Express routes, MCP registrations, `case` tables), HTML (`<script src>`, `<link>`, inline scripts) and CSS imports.

## File: handoff247/build.py
Writes the pack: seven Markdown pages, `diagrams/*.mmd`, `handoff.json` (its first key `"generator": "HandOff247"` is how later runs recognise and skip an old pack), `ontology.json`, the wiki and `index.html`. `write_wiki` deletes wiki pages of an earlier run that no longer exist, but only files that start with the generator mark, so a page someone added by hand stays.

## File: handoff247/ontology.py
Turns `project.links` and `project.edges` into typed entities and relations. It detects nothing itself; add a new kind of fact in an analyzer or in `connect.py` first, then map it here. `CLASSES` and `RELATIONS` are the schema: a class has a colour group and a shape (the graph has eight colours, so classes share one and differ by shape), a relation has a label for each direction. `_Builder.rel` drops a relation whose ends are not both entities, which is why assets and system environment variables never appear.

## File: handoff247/wiki.py
Writes the ontology as Markdown pages plus `llms.txt` and `llms-full.txt`. `assign_pages` decides which page describes an entity (own page for files, areas, modes, operations and MCP tools; a list page for the small classes; a type lives on its file's page). File names are slugs with `/` as `__`; Windows reserved names get a `_` prefix. The pages are regenerated on every run, so durable knowledge belongs in the notes file; `agents()` is the page that tells an assistant so.

## File: handoff247/cli.py
Six commands: `go`, `build`, `notes`, `check`, `mcp`, `trace`. `trace` answers a question from the user's side (a request in words, a user type, a feature, an asset, a code file) without writing a pack. A first argument that is not a command is taken as a folder for `go`. `go` decides between one project and a folder of projects (`workspace.is_workspace`), then does notes + build + report. `check --min N` exits 1 when fewer than N% of files have notes, which is how CI can enforce documentation.

## File: handoff247/leaving.py
The handover findings: Git state (uncommitted, commits on no remote, stashes, authors), files Git ignores that are present, absolute paths, hosts in URLs, TODO comments, key and token patterns, declared tool versions, and the readiness rows. Two rules to keep: a secret hit records file, line and kind but never the value, and anything that cannot be known is left out (no history figures for shallow clones, no "pushed" row without a remote). `JUNK_DIRS` decides which ignored folders are build output; add to it when a pack lists noise.

## File: handoff247/summarize.py
The optional `--summarize` step. It shells out to `codex exec` (read-only sandbox, empty temporary folder, `--ephemeral`, an output schema) with batches of files and their analysis facts, and keeps the answers in `<notes>.summaries.json` keyed by path with a content hash. Rules to keep: a file with a note is never sent; key-like lines are replaced with `[removed]` before sending (`redact`); answers for ids that were not asked for are dropped; a summary whose file hash no longer matches is ignored. `prepare()` is what the CLI and the workspace call before writing a pack.

## File: handoff247/mcp.py
The MCP server (`handoff247 mcp`): newline-delimited JSON-RPC on stdin/stdout, with `sys.stdout` pointed at stderr so stray prints cannot corrupt the protocol. Thirteen tools; only `handoff_write_note` and `handoff_build` write. `handoff_overview` is the briefing an agent starts with; `handoff_users`, `handoff_request`, `handoff_feature`, `handoff_asset` and `handoff_impact` are thin wrappers over `explore.Explorer`; `handoff_page` renders any page of the pack in memory, and the same pages are offered as MCP resources when the server was started with a project folder. `handoff_write_note` accepts only skeleton headings (plus `Op:` for real operations), never overwrites filled text without `replace`, rejects key-like text and appends the agent mark. The analysed project is cached per folder and dropped after every write.

## File: handoff247/workspace.py
The folder-of-projects mode: finds projects one or two levels down, builds a pack for each, and writes the index (README.md, index.html, workspace.json, workspace.mmd). It does not write into the projects: notes for a project without its own notes file go to `<out>/notes/`. One failing project is listed as failed and the rest continue. Cross-project arrows come only from paths that resolve into another project's folder.

## File: handoff247/connect.py
Turns per-file facts into edges and connection maps. The key idea: string keys of a dispatch table (`"list"`, `"ontology.search"`) are followed to every caller (`api('list')`, `cli('list')`, `Call("list")`, `cli list` in docs), and each caller's wrapper function is inspected to tell HTTP, CLI process or in-process apart. A caller group only counts when it uses two or more keys or a dotted key, so ordinary strings like "git" are not mistaken for operations.

## File: handoff247/labels.py
Every generated heading and label, in one table, so pages and diagrams use the same words. Extracted comments and notes never pass through it.

## File: handoff247/inventory.py
Lists files with `git ls-files` (so .gitignore applies), falls back to a directory walk, applies `.handoffignore` and skips folders that contain an earlier pack.

## File: handoff247/lexer.py
Produces two views of C-like source with identical offsets: strings+comments blanked (for identifiers) and comments blanked (for literal patterns). Handles C# verbatim, interpolated and raw strings and JS template and regex literals. If a regex in an analyzer misbehaves, check the lexer view first.

## File: handoff247/mermaid.py
Builds the six diagrams. `users_map` groups screens by who sees them and joins them through the states and files that pass work on. `system` collapses launch scripts into one node when there are more than three; `code` hides incoming arrows of shared foundations (hubs) so the rest stays readable.

## File: handoff247/model.py
Dataclasses: FileInfo, Symbol, Fact, Edge, Project. A Fact is one observation with a file and line; everything in the pack traces back to one.

## File: handoff247/notes.py
Parses and extends the notes file. `update` only appends missing headings and missing Translations rows; it never rewrites existing text. Stale headings (for deleted files) are reported, not removed.

## File: handoff247/pipeline.py
analyze_project(): inventory, per-file analysis, linking.

## File: handoff247/render_html.py
The single-file viewer. It embeds the Markdown pages and loads marked, DOMPurify and Mermaid from jsDelivr at pinned versions. Diagram nodes are matched back to files through the `flowchart-nN-` element ids, so clicking a node opens that file's card. The Graph tab is hand-written canvas code with no library: a force layout with a fixed seed (the same picture every run), hit testing, and names drawn most-connected first without overlap. The eight colours are the `--g1`…`--g8` variables; do not add a ninth, give a new class a shape inside an existing group. Wiki pages are embedded too, and `resolveHref` turns their page-relative links into pack-relative ones.

## File: handoff247/render_md.py
The Markdown pages except USERS.md (render_users.py writes that one); `handover()` puts each of the leaver's answers next to what `leaving.py` found. `Linker` decides how file:line references are linked: relative when the pack is inside the project, GitHub blob URLs at the exact commit when it is outside, plain text otherwise.

## File: handoff247/translate.py
Finds extracted prose with letters outside the Latin script (summaries, doc comments, Markdown headings, MCP tool descriptions, sub-command help, commit subjects) and swaps in the English from the notes' Translations table. Matching is exact apart from spacing, so a comment that changed later shows its original again instead of a stale translation. Identifiers such as file names are never touched.

## File: tests/test_handoff.py
Runs the full pipeline on a copy of the fixture outside Git, so both file-listing paths are covered.

<!-- added by HandOff247 for new items -->
## File: handoff247/explore.py
`Explorer` answers a successor's questions from the journeys model: `users`/`user_flow` (from a user type), `find` (from words on a screen or a user's request), `asset` (from an asset or table), `impact` (from code), `feature` (everything about one feature) and `overview` (the whole project). The pages, the MCP tools and `handoff247 trace` all call it, so they cannot disagree. `applies` keeps a GET link from being credited with what the POST branch of the same handler does. Every answer carries `not_verified` and the reminder that a condition in the code is not a diagnosis of a live problem.

## File: handoff247/handlers.py
What a route does. `PyIndex` follows a Python handler through `ast` into the project functions it calls (four levels deep) and records every effect with its file, line, call chain (`via`), the handler line that led there (`root`) and the `if` tests it sits inside (`when`). `parse_sql` reads tables and literal column values out of SQL strings; a value passed as a parameter counts only when the parameter list holds a literal. Two data flows are traced through variables instead of matched by name: an uploaded file object to the call that stores it, and the stored name into the SQL parameter. `access_other` reads role checks written directly on an Express route or above an ASP.NET action; handlers in those languages are not followed. A sentence that starts with `Select` is not SQL: both keywords must be present in the same letter case.

## File: handoff247/journeys.py
Joins screens.py and handlers.py into `project.links["journeys"]`: user types, screens, terms, features (one per route), data tables with states, assets, hand-overs, shared functions and gaps. `match_path` fits a path written in a template to a route; a hole in the path only fits a route parameter, never a fixed word. A hand-over is one feature setting a column value that another feature's query filters on; it is always marked inferred. Everything that could not be connected goes to `gaps` instead of being guessed. The user types are those of the analysed application and must never be used to hide part of the pack from its reader.

## File: handoff247/render_users.py
Markdown for USERS.md and for the wiki pages of user types, features, screens, assets and data tables. `Ctx` holds how to link a source line and another page from where the text will live, so the same section renders in the pack root and two folders down in the wiki.

## File: handoff247/screens.py
Reads templates and HTML pages as text: the visible terms (links, buttons, field labels, headings), the link target or form each belongs to, the `{% if %}` conditions around it, the layout it extends, and the files it references. `Locales` resolves translation keys through JSON locale files and keeps the text of every language, so a term is found by the word a user reads. `roles_in` only reports a role for a positive test (`==`, `in`, `has_role`); a negated test names a role without saying who passes, so it yields nothing. Jinja, Django, Twig, Nunjucks and Handlebars conditions are read; EJS, ERB and Razor are not.
