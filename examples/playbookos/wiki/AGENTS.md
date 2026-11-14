---
generator: HandOff247
---

# How to use this wiki

This wiki describes **PlayBookOS** for an AI assistant that has to answer questions about the project or change it. HandOff247 generated it by static analysis; it did not run the code and no language model wrote these pages.

## Reading

1. Start at [index.md](index.md). Open [overview.md](overview.md), then only the pages the question needs.
2. Each page is one thing. `Relations` lists what it points to (→) and what points to it (←); follow those links.
3. A `file:line` next to a statement is where it was observed. Open that source before you change code.
4. *inferred* marks a conclusion, not an observation. Check it in the source before relying on it.
   Text labelled *written by a language model* (and *(model)* in lists) was not checked by a person either.
5. Something that is not in the wiki was not found. That does not mean it does not exist: code built from runtime strings, reflection or dependency-injection containers is not followed. Say that you do not know.
6. [notes.md](notes.md) is the only human-written page. "Not answered" there is a question for a person.

## Helping someone who uses the application

The user types in this wiki (`users/`) are the kinds of user the analysed application tells apart. They are not access levels of the wiki: read every flow you need, whoever it belongs to. Five ways in:

- **From a user type:** `users/<name>.md` lists the screens, what each control does and who picks the work up next.
- **From words on a screen:** [terms.md](terms.md) has every link, button, field label, heading and message, with the feature it leads to. The word a user says and the name in the code often differ; the page gives both.
- **From an asset or a table:** `assets/` and `data/` say who provides it, what stores it and where it shows.
- **From code:** a file page lists the features that run it under *runs for*; a feature page lists its code.
- **From a request:** find the feature through the words, then read its page in `features/`: started from, what the code does, branches, hand-overs, what to check, not verified.

Two rules when you answer. The same word can be on several screens: name the screen and the user type, and if two candidates fit, show both instead of picking one. And a condition in the code is not a diagnosis: "the article is only listed when status is in_review" is what the code does, not proof of why this user's article is missing. Say what to check (*What to check* on the feature page) unless you have the live data or a log.

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
| User type | A kind of user the analysed application tells apart, found from role checks. Not an access level of this pack. |
| Screen | A template or page a user sees. |
| Screen term | Words a user reads: a link, button, field label, heading, or a message the code shows. |
| Function | Project code that a feature runs. Modelled once, however many features use it. |
| Data table | A table named in an SQL statement. |
| State | A column value that statements set or filter on, such as status = 'published'. |
| Asset | A file users see or provide: shipped with the project, uploaded, generated, or kept in external storage. |

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
| is open to | may use | Role check on the route, or none found (anyone). |
| sees | is seen by | A route this user type may use shows the screen. |
| shows | is shown by | The route renders the screen. |
| is built on | is part of | The template extends or includes the other one. |
| displays | is displayed on | The words are on the screen, or the route shows the message. |
| leads to | is started from | The link, button or form of the term targets the route; a script of the screen calls it. |
| redirects to | is reached by redirect from | The handler redirects to the other route. |
| runs | runs for | The handler calls the function, directly or through other functions. |
| reads | is read by | An SQL statement of the feature reads the table. |
| writes | is written by | An SQL statement of the feature inserts, updates or deletes rows. |
| has the state | is a state of | A literal column value found in a statement. |
| sets | is set by | A statement of the feature sets the column to this value. |
| lists only | is the filter of | A statement of the feature filters on this value. |
| is tested by | tests | A template condition or a handler branch names the same column and value. |
| hands over to | receives from | One feature sets a state that the other filters on. |
| shows | appears on | The screen references the file. |
| provides | is provided by | The feature receives the upload or writes the generated file. |
| delivers | is delivered by | The route sends the file to the browser. |
| has its name kept in | keeps the name of | The stored file name is written to a column of the table. |
| takes its text from | words | The text of the term comes from a locale file. |

## Writing

Do not edit these pages: the next run overwrites them. Knowledge that should last goes into `examples/playbookos.notes.md`, under the heading of the thing it is about:

- `## Project` — what the project is and its status
- `## Topic: <name>` — the handover questions listed in [notes.md](notes.md)
- `## Area: <folder>`, `## File: <path>`, `## Mode: <name>`, `## Op: <operation>` — one thing each
- `## User: <user type>` — who these users are in real life and what they usually ask for

Write plain sentences, say only what you verified in the source, and never paste a password or token; say where it is kept. Then run `python -m handoff247 <project folder>` again: the note appears on the matching wiki page, in the handoff pages and in the viewer.

## Files

- `../llms.txt` — short entry point; `../llms-full.txt` — every page of this wiki in one file
- `../ontology.json` — entities (`id`, `type`, `name`, `summary`, `page`) and relations (`s`, `p`, `o`, `file`, `line`)
- `../index.html` — viewer with a graph of the same ontology

## Working through MCP

`python -m handoff247 mcp` is an MCP server over the same data: a briefing of the whole project, the flows of each user type, a search from a user's own words, one feature in full, assets, the effect of a code change, entities, source lines, what is still undocumented, and notes written under the right heading (marked as written by an agent). It is the supported way for an assistant to add to this wiki.
