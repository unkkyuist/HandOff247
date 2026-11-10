---
generator: HandOff247
---

# Notes from the previous owner

Written by a person in `examples/playbookos.notes.md`; nothing on this page was derived from code. A question without an answer is a real gap: ask, do not guess.

## What the project is

PlayBook OS is a shared ledger for projects, references and AI work. The web UI, the JSON CLI and MCP (stdio and HTTP) all go through the same operations and the same SQLite records (README.en.md).
It is a trusted-owner workspace service: there are no per-user roles or tenant isolation (README.en.md, "Verification and scope").

## Successor checklist

1. Install the .NET 10 SDK, run `dotnet build -c Release`, then `dotnet bin/Release/net10.0/PlayBook.dll serve` and open http://127.0.0.1:7331.
2. Point every client (GUI, CLI, MCP) at the same `PLAYBOOK_HOME`, or they will each see a different database.
3. After any business-logic change run `python scripts/smoke.py` (plus folders/ontology/central smokes before a release).
4. Track work for this project in PlayBook itself under project ID `playbook` (AGENTS.md).

## Known issues and risks

- Every write must send `expectedRevision`; on conflict reread and merge instead of retrying blindly (README.en.md).
- macOS runtime is unverified; cross-publishing does not count as evidence (AGENTS.md).
- Real Claude model execution was not verified in v0.2.0; see docs/RELEASE-0.2.0.md.

## Credentials and accounts

The HTTP/MCP key lives in `PLAYBOOK_HOME/api-key` (created on first `serve`). Never commit `data/`, tool credentials, logs or API keys (AGENTS.md).

<!-- The next five questions can only be answered by the person leaving, so the demo leaves them open:
     the pack shows them as "to do" on its Handover page. -->

## Open work and next steps

*Not answered.*

## Deploy and release

*Not answered.*

## Routine operations

*Not answered.*

## Data and backups

*Not answered.*

## People and contacts

*Not answered.*
