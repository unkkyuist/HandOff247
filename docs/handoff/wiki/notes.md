---
generator: HandOff247
---

# Notes from the previous owner

Written by a person in `HANDOFF.notes.md`; nothing on this page was derived from code. A question without an answer is a real gap: ask, do not guess.

## What the project is

HandOff247 reads a project folder and writes a handoff pack for the next person: diagrams, structure, extracted comments and a map of how the tools connect. It is static analysis only (it never imports or runs the target's code) and it is standard-library Python, so `python -m handoff247` works on any machine with Python 3.10+.
Status: v0.4.0. `python -m handoff247 <folder>` does everything in one step (notes file, pack, handover checklist), and a folder that holds several projects gets one pack per project plus an index. Since v0.4.0 every pack also holds the ontology (`ontology.json`), a graph of it in the viewer, and a wiki for AI assistants (`wiki/`, `llms.txt`). The first real target was PlayBookOS (see examples/playbookos). C#, Python, JavaScript/TypeScript, PowerShell, shell and batch have analyzers; other languages are inventoried but not parsed. Output is English; a project's own comments and headings in another language get English versions from the notes file's `## Translations` table.

## Successor checklist

1. Run the tests: `python -m unittest discover -s tests`.
2. Regenerate the examples after any analyzer change: `python -m handoff247 build <PlayBookOS checkout> --name PlayBookOS -o examples/playbookos --notes examples/playbookos.notes.md --date <date>`. If an analyzer change surfaces new Korean comments or headings, `check --notes examples/playbookos.notes.md` reports them; add their rows to the Translations table there. Read the diff of the generated pages: a change there is a change in what successors will be told.
3. Regenerate this pack after committing and pushing, so its Handover page does not report your own work as uncommitted: `python -m handoff247 . --date <date>`.
4. Open `index.html` of a pack in a browser and check that every diagram renders (Mermaid errors show as red text in the page).

## Known issues and risks

- The rule that matters most: a wrong statement is worse than a missing one. When a pattern is ambiguous the analyzers leave it out; inferences (for example a wrapper passed in as a parameter) are labelled and drawn dashed. Keep it that way.
- Analysis is regex/lexer based for everything except Python (which uses `ast`). Code built from runtime strings, reflection or dependency-injection containers is not followed.
- MCP tool names from the C# SDK are derived from method names (snake_case, `Async` removed) and marked with * in the pack.
- Mermaid labels must go through `mermaid.esc`; `*`, `_` and backticks are escaped because Mermaid otherwise formats them as Markdown.

## Credentials and accounts

None. The tool needs no keys. The GitHub Action only uses the workflow's own checkout.

## Open work and next steps

- A folder of projects has a graph and a wiki per project but no single graph across projects; `workspace.py` only writes an `llms.txt` that links them.
- The wiki is generated without a language model. If prose written by a model is wanted, the place for it is the notes file (see `wiki/AGENTS.md` in any pack), not the generator.
- Go, Rust, Java and other languages are only inventoried. An analyzer for one of them is the natural next piece: copy the shape of `analyzers/python.py` and add an assertion per fact to the tests.
- The workspace index has no example in `examples/`; it is covered by `test_go_folder_of_projects` only.

## Deploy and release

There is no server and no package upload. A release is a push to `main` on GitHub; people run it from a clone or use the repository as a GitHub Action (`uses: unkkyuist/HandOff247@main`), so `main` is what users get. Bump the version in `handoff247/__init__.py` and `pyproject.toml` together. To roll back, revert the commit.

## Routine operations

Nothing runs on a schedule. CI runs on every push and pull request. The viewer loads marked, DOMPurify and Mermaid from jsDelivr at pinned versions (`render_html.py`); check now and then that those versions still load.

## Data and backups

The tool stores nothing. Its only state is the Git repository. Generated packs can always be rebuilt; a project's `HANDOFF.notes.md` cannot, so it belongs in that project's repository.

## People and contacts

Owner: the GitHub account `unkkyuist` (issues on the repository). There are no other maintainers and no known outside users yet.
