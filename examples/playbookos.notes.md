# HandOff247 notes · PlayBookOS

<!--
Example notes for the PlayBookOS demo pack. They were written while building HandOff247 and only
restate what PlayBookOS's own README.en.md and AGENTS.md (commit 7153e47) say, so the demo shows
how notes appear next to the generated facts. In a real handoff the outgoing owner writes these.
-->

## Project
PlayBook OS is a shared ledger for projects, references and AI work. The web UI, the JSON CLI and MCP (stdio and HTTP) all go through the same operations and the same SQLite records (README.en.md).
It is a trusted-owner workspace service: there are no per-user roles or tenant isolation (README.en.md, "Verification and scope").

## Topic: Successor checklist
1. Install the .NET 10 SDK, run `dotnet build -c Release`, then `dotnet bin/Release/net10.0/PlayBook.dll serve` and open http://127.0.0.1:7331.
2. Point every client (GUI, CLI, MCP) at the same `PLAYBOOK_HOME`, or they will each see a different database.
3. After any business-logic change run `python scripts/smoke.py` (plus folders/ontology/central smokes before a release).
4. Track work for this project in PlayBook itself under project ID `playbook` (AGENTS.md).

## Topic: Known issues and risks
- Every write must send `expectedRevision`; on conflict reread and merge instead of retrying blindly (README.en.md).
- macOS runtime is unverified; cross-publishing does not count as evidence (AGENTS.md).
- Real Claude model execution was not verified in v0.2.0; see docs/RELEASE-0.2.0.md.

## Topic: Credentials and accounts
The HTTP/MCP key lives in `PLAYBOOK_HOME/api-key` (created on first `serve`). Never commit `data/`, tool credentials, logs or API keys (AGENTS.md).

## Mode: serve
What people normally run: web UI, `/api/{operation}`, HTTP MCP at `/mcp`, and the local AI worker.

## Mode: server
Central multi-PC server. Needs its own `PLAYBOOK_HOME` and an account created with `cli server.setup` first.

## Mode: cli
One operation per process: `PlayBook.dll cli <operation> <json | @file | ->`. Errors go to stderr as JSON with exit code 1.

## File: Operations.cs
The single place new features plug into. AGENTS.md: use this shared Operations service for CLI/GUI/MCP features and do not add a second data authority.

## File: Store.cs
All record changes must pass validation here and write an audit event in the same transaction (AGENTS.md).
