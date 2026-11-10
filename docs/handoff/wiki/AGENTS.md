---
generator: HandOff247
---

# How to use this wiki

This wiki describes **HandOff247** for an AI assistant that has to answer questions about the project or change it. HandOff247 generated it by static analysis; it did not run the code and no language model wrote these pages.

## Reading

1. Start at [index.md](index.md). Open [overview.md](overview.md), then only the pages the question needs.
2. Each page is one thing. `Relations` lists what it points to (→) and what points to it (←); follow those links.
3. A `file:line` next to a statement is where it was observed. Open that source before you change code.
4. *inferred* marks a conclusion, not an observation. Check it in the source before relying on it.
   Text labelled *written by a language model* (and *(model)* in lists) was not checked by a person either.
5. Something that is not in the wiki was not found. That does not mean it does not exist: code built from runtime strings, reflection or dependency-injection containers is not followed. Say that you do not know.
6. [notes.md](notes.md) is the only human-written page. "Not answered" there is a question for a person.

## Classes

| Class | Meaning |
|---|---|
| Project | The thing being handed over. |
| Area | A top-level folder of the project. |
| File | A file of the project (images and other assets are left out). |
| Type | A class, record, struct, interface or enum defined in a file. |
| Run mode | A way to start the program, picked by its first argument. |
| Sub-command | A sub-command of a command-line parser. |
| Dispatch table | A switch or mapping that turns an operation name into the code that handles it. |
| Operation | One named operation of a dispatch table. |
| HTTP route | An HTTP endpoint the program serves. |
| MCP tool | A tool the program offers to AI clients over MCP. |
| Environment variable | An environment variable the code reads or sets (operating-system variables are left out). |
| Port | A network port number found in an address or a port setting. |
| Package | A third-party package the project declares or imports. |
| External host | A host name found in a URL. |
| Command-line tool | A well-known program the project's scripts start; it has to be installed. |
| Person | An author in the Git history. |

## Relations

| Relation | Read backwards | Meaning |
|---|---|---|
| contains | is part of | Project → area → file. |
| defines | is defined in | The file holds the definition. |
| imports | is imported by | Import or include statement. |
| uses | is used by | The code names a type defined in the other file; a run mode uses a type. |
| takes as a dependency | is a dependency of | Constructor parameter of that type. |
| extends | is extended by | Base class or implemented interface. |
| loads | is loaded by | A page loads a script or stylesheet. |
| runs | is run by | A script or configuration starts the other file. |
| refers to | is referred to by | A string in the file is the other file's path. |
| references | is referenced by | Project reference in a build file. |
| documents | is documented in | A document links to the file or shows the operation in an example. |
| serves | is served by | A run mode passes requests to the dispatch table. |
| exposes | is exposed by | A run mode registers the HTTP route. |
| has operation | is an operation of | Key of the dispatch table. |
| is handled by | handles | The file that holds the handler the table calls. |
| calls | is called from | The file asks for the operation by name (over HTTP, a process or in-process). |
| invokes | is invoked by | An MCP tool runs the operation. |
| forwards to | receives from | An HTTP route hands the request to the dispatch table. |
| reads | is read by | The file reads the environment variable. |
| sets | is set by | The file sets the environment variable. |
| mentions | is mentioned in | The host or port appears in the file. |
| depends on | is a dependency of | The file declares or imports the package. |
| starts | is started by | The file starts the command-line tool. |
| has commits in | has commits by | Author in the Git history of the project. |

## Writing

Do not edit these pages: the next run overwrites them. Knowledge that should last goes into `HANDOFF.notes.md`, under the heading of the thing it is about:

- `## Project` — what the project is and its status
- `## Topic: <name>` — the handover questions listed in [notes.md](notes.md)
- `## Area: <folder>`, `## File: <path>`, `## Mode: <name>`, `## Op: <operation>` — one thing each

Write plain sentences, say only what you verified in the source, and never paste a password or token; say where it is kept. Then run `python -m handoff247 <project folder>` again: the note appears on the matching wiki page, in the handoff pages and in the viewer.

## Files

- `../llms.txt` — short entry point; `../llms-full.txt` — every page of this wiki in one file
- `../ontology.json` — entities (`id`, `type`, `name`, `summary`, `page`) and relations (`s`, `p`, `o`, `file`, `line`)
- `../index.html` — viewer with a graph of the same ontology

## Working through MCP

`python -m handoff247 mcp` is an MCP server over the same data: search and read entities, read source lines, list what is still undocumented, and write notes under the right heading (marked as written by an agent). It is the supported way for an assistant to add to this wiki.
