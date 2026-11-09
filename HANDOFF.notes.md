# HandOff247 notes · HandOff247

<!--
HandOff247 notes. Write in plain sentences under each heading; the text is shown next to that item in the handoff pack.
Lines that still start with TODO count as undocumented. Keep the headings exactly as they are (they are matched by name).
Never paste passwords or tokens here — say where they are kept instead.
-->

## Project
HandOff247 reads a project folder and writes a handoff pack for the next person: diagrams, structure, extracted comments and a map of how the tools connect. It is static analysis only (it never imports or runs the target's code) and it is standard-library Python, so `python -m handoff247` works on any machine with Python 3.10+.
Status: v0.2.0. The first real target was PlayBookOS (see examples/playbookos). C#, Python, JavaScript/TypeScript, PowerShell, shell and batch have analyzers; other languages are inventoried but not parsed. Output is English; a project's own comments and headings in another language get English versions from the notes file's `## Translations` table.

## Topic: Successor checklist
1. Run the tests: `python -m unittest discover -s tests`.
2. Regenerate the examples after any analyzer change: `python -m handoff247 build <PlayBookOS checkout> --name PlayBookOS -o examples/playbookos --notes examples/playbookos.notes.md --date <date>`. If an analyzer change surfaces new Korean comments or headings, `check --notes examples/playbookos.notes.md` reports them; add their rows to the Translations table there. Read the diff of the generated pages: a change there is a change in what successors will be told.
3. Regenerate this pack: `python -m handoff247 build . -o docs/handoff --date <date>`.
4. Open `index.html` of a pack in a browser and check that every diagram renders (Mermaid errors show as red text in the page).

## Topic: Known issues and risks
- The rule that matters most: a wrong statement is worse than a missing one. When a pattern is ambiguous the analyzers leave it out; inferences (for example a wrapper passed in as a parameter) are labelled and drawn dashed. Keep it that way.
- Analysis is regex/lexer based for everything except Python (which uses `ast`). Code built from runtime strings, reflection or dependency-injection containers is not followed.
- MCP tool names from the C# SDK are derived from method names (snake_case, `Async` removed) and marked with * in the pack.
- Mermaid labels must go through `mermaid.esc`; `*`, `_` and backticks are escaped because Mermaid otherwise formats them as Markdown.

## Topic: Credentials and accounts
None. The tool needs no keys. The GitHub Action only uses the workflow's own checkout.

## Area: .github
CI: unit tests on Linux and Windows (Python 3.10 and 3.12), a self-documentation run, and a run of the composite action against the test fixture.

## Area: handoff247
The package. Data flows inventory → analyzers → connect → (mermaid, render_md, render_html) → build. pipeline.py wires the first three; cli.py and build.py the rest.

## Area: tests
`test_handoff.py` plus `fixtures/mini`, a small fake app (C# + JS + Python + PowerShell + batch) wired the same way as PlayBookOS: three modes, one dispatch switch, HTTP route, MCP tools, launch scripts. Every connection type the tool claims to detect has an assertion here.

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
Writes the pack: five Markdown pages, `diagrams/*.mmd`, `handoff.json` (its first key `"generator": "HandOff247"` is how later runs recognise and skip an old pack) and `index.html`.

## File: handoff247/cli.py
Three commands: `build`, `notes`, `check`. `check --min N` exits 1 when fewer than N% of files have notes, which is how CI can enforce documentation.

## File: handoff247/connect.py
Turns per-file facts into edges and connection maps. The key idea: string keys of a dispatch table (`"list"`, `"ontology.search"`) are followed to every caller (`api('list')`, `cli('list')`, `Call("list")`, `cli list` in docs), and each caller's wrapper function is inspected to tell HTTP, CLI process or in-process apart. A caller group only counts when it uses two or more keys or a dotted key, so ordinary strings like "git" are not mistaken for operations.

## File: handoff247/labels.py
Every generated heading and label, in one table, so pages and diagrams use the same words. Extracted comments and notes never pass through it.

## File: handoff247/inventory.py
Lists files with `git ls-files` (so .gitignore applies), falls back to a directory walk, applies `.handoffignore` and skips folders that contain an earlier pack.

## File: handoff247/lexer.py
Produces two views of C-like source with identical offsets: strings+comments blanked (for identifiers) and comments blanked (for literal patterns). Handles C# verbatim, interpolated and raw strings and JS template and regex literals. If a regex in an analyzer misbehaves, check the lexer view first.

## File: handoff247/mermaid.py
Builds the five diagrams. `system` collapses launch scripts into one node when there are more than three; `code` hides incoming arrows of shared foundations (hubs) so the rest stays readable.

## File: handoff247/model.py
Dataclasses: FileInfo, Symbol, Fact, Edge, Project. A Fact is one observation with a file and line; everything in the pack traces back to one.

## File: handoff247/notes.py
Parses and extends the notes file. `update` only appends missing headings and missing Translations rows; it never rewrites existing text. Stale headings (for deleted files) are reported, not removed.

## File: handoff247/pipeline.py
analyze_project(): inventory, per-file analysis, linking.

## File: handoff247/render_html.py
The single-file viewer. It embeds the Markdown pages and loads marked, DOMPurify and Mermaid from jsDelivr at pinned versions. Diagram nodes are matched back to files through the `flowchart-nN-` element ids, so clicking a node opens that file's card.

## File: handoff247/render_md.py
The five Markdown pages. `Linker` decides how file:line references are linked: relative when the pack is inside the project, GitHub blob URLs at the exact commit when it is outside, plain text otherwise.

## File: handoff247/translate.py
Finds extracted prose with letters outside the Latin script (summaries, doc comments, Markdown headings, MCP tool descriptions, sub-command help, commit subjects) and swaps in the English from the notes' Translations table. Matching is exact apart from spacing, so a comment that changed later shows its original again instead of a stale translation. Identifiers such as file names are never touched.

## File: tests/test_handoff.py
Runs the full pipeline on a copy of the fixture outside Git, so both file-listing paths are covered.
