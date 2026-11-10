---
generator: HandOff247
id: "project:HandOff247"
type: Project
---

# HandOff247

**What the previous owner says it is**

> HandOff247 reads a project folder and writes a handoff pack for the next person: diagrams, structure, extracted comments and a map of how the tools connect. It is static analysis only (it never imports or runs the target's code) and it is standard-library Python, so `python -m handoff247` works on any machine with Python 3.10+.
> Status: v0.4.0. `python -m handoff247 <folder>` does everything in one step (notes file, pack, handover checklist), and a folder that holds several projects gets one pack per project plus an index. Since v0.4.0 every pack also holds the ontology (`ontology.json`), a graph of it in the viewer, and a wiki for AI assistants (`wiki/`, `llms.txt`). The first real target was PlayBookOS (see examples/playbookos). C#, Python, JavaScript/TypeScript, PowerShell, shell and batch have analyzers; other languages are inventoried but not parsed. Output is English; a project's own comments and headings in another language get English versions from the notes file's `## Translations` table.

- **Repository:** https://github.com/unkkyuist/HandOff247 at commit `5be3bdf`
- **Human-readable pack:** [README](../README.md), [handover checklist](../HANDOVER.md), [how to run it](../RUNNING.md), [connections](../CONNECTIONS.md), [code map](../CODEMAP.md)
- **What only the previous owner knew:** [notes](notes.md)

## What was found

| Class | Count | Where |
|---|---|---|
| Areas | 3 | [index](index.md), under Areas |
| Files | 34 | [index](index.md), under Files |
| Types | 16 | on the page of the file that defines it |
| Sub-commands | 4 | [subcommands.md](subcommands.md) |
| Dispatch tables | 2 | [operations.md](operations.md) |
| Operations | 20 | [index](index.md), under Operations |
| Ports | 1 | [ports.md](ports.md) |
| External hosts | 4 | [hosts.md](hosts.md) |
| Command-line tools | 2 | [commands.md](commands.md) |
| People | 1 | [people.md](people.md) |

## Relations

**contains** →

- [`.github`](areas/github.md)
- [`handoff247`](areas/handoff247.md)
- [`tests`](areas/tests.md)
- [`.gitignore`](files/gitignore.md)
- [`.handoffignore`](files/handoffignore.md)
- [`HANDOFF.notes.md`](files/HANDOFF.notes.md.md)
- [`LICENSE`](files/LICENSE.md)
- [`README.md`](files/README.md.md)
- [`action.yml`](files/action.yml.md)
- [`pyproject.toml`](files/pyproject.toml.md)

**has commits by** ←

- [R B](people.md)
