---
generator: HandOff247
id: "project:PlayBookOS"
type: Project
---

# PlayBookOS

**What the previous owner says it is**

> PlayBook OS is a shared ledger for projects, references and AI work. The web UI, the JSON CLI and MCP (stdio and HTTP) all go through the same operations and the same SQLite records (README.en.md).
> It is a trusted-owner workspace service: there are no per-user roles or tenant isolation (README.en.md, "Verification and scope").

- **Repository:** https://github.com/unkkyuist/PlayBookOS at commit `7153e47`
- **Human-readable pack:** [README](../README.md), [handover checklist](../HANDOVER.md), [how to run it](../RUNNING.md), [connections](../CONNECTIONS.md), [code map](../CODEMAP.md)
- **What only the previous owner knew:** [notes](notes.md)

## What was found

| Class | Count | Where |
|---|---|---|
| Areas | 6 | [index](index.md), under Areas |
| Files | 96 | [index](index.md), under Files |
| Types | 34 | on the page of the file that defines it |
| Run modes | 6 | [index](index.md), under Run modes |
| Dispatch tables | 1 | [operations.md](operations.md) |
| Operations | 65 | [index](index.md), under Operations |
| HTTP routes | 6 | [routes.md](routes.md) |
| MCP tools | 46 | [index](index.md), under MCP tools |
| Environment variables | 8 | [environment.md](environment.md) |
| Ports | 5 | [ports.md](ports.md) |
| Packages | 3 | [packages.md](packages.md) |
| External hosts | 8 | [hosts.md](hosts.md) |
| Command-line tools | 3 | [commands.md](commands.md) |
| People | 1 | [people.md](people.md) |

## How it starts

- run mode [`agent`](modes/agent.md) — background service
- run mode [`cli`](modes/cli.md) — One operation per process: `PlayBook.dll cli <operation> <json | @file | ->`. Errors go to stderr as JSON with exit code 1.
- run mode [`mcp`](modes/mcp.md) — MCP over stdio
- run mode [`serve`](modes/serve.md) — What people normally run: web UI, `/api/{operation}`, HTTP MCP at `/mcp`, and the local AI worker.
- run mode [`server`](modes/server.md) — Central multi-PC server. Needs its own `PLAYBOOK_HOME` and an account created with `cli server.setup` first.
- run mode [`worker`](modes/worker.md)
- launch script [`START_PLAYBOOK.cmd`](files/START_PLAYBOOK.cmd.md)
- launch script [`playbook-harness.ps1`](files/playbook-harness.ps1.md)
- launch script [`playbook.ps1`](files/playbook.ps1.md)
- launch script [`playbook.sh`](files/playbook.sh.md)
- launch script [`Start-PlayBook-Desktop.ps1`](files/Start-PlayBook-Desktop.ps1.md)
- launch script [`portable/INSTALL_PLAYBOOK.cmd`](files/portable__INSTALL_PLAYBOOK.cmd.md)
- launch script [`portable/START_PLAYBOOK.cmd`](files/portable__START_PLAYBOOK.cmd.md)
- launch script [`portable/Install-PlayBook.ps1`](files/portable__Install-PlayBook.ps1.md)
- launch script [`portable/Start-PlayBook.ps1`](files/portable__Start-PlayBook.ps1.md)

## Relations

**contains** →

- [`Properties`](areas/Properties.md)
- [`docs`](areas/docs.md)
- [`examples`](areas/examples.md)
- [`portable`](areas/portable.md)
- [`scripts`](areas/scripts.md)
- [`wwwroot`](areas/wwwroot.md)
- [`.gitattributes`](files/gitattributes.md)
- [`.gitignore`](files/gitignore.md)
- [`AGENTS.md`](files/AGENTS.md.md)
- [`Access.cs`](files/Access.cs.md)
- [`AgentWorker.cs`](files/AgentWorker.cs.md)
- [`Connection.cs`](files/Connection.cs.md)
- [`Desktop.cs`](files/Desktop.cs.md)
- [`Domain.cs`](files/Domain.cs.md)
- [`Folders.cs`](files/Folders.cs.md)
- [`Harnesses.cs`](files/Harnesses.cs.md)
- [`Library.cs`](files/Library.cs.md)
- [`McpTools.cs`](files/McpTools.cs.md)
- [`Ontology.cs`](files/Ontology.cs.md)
- [`Operations.cs`](files/Operations.cs.md)
- [`Orchestration.cs`](files/Orchestration.cs.md)
- [`PlayBook.csproj`](files/PlayBook.csproj.md)
- [`Program.cs`](files/Program.cs.md)
- [`ProjectScanner.cs`](files/ProjectScanner.cs.md)
- [`Providers.cs`](files/Providers.cs.md)
- [`README.en.md`](files/README.en.md.md)
- [`README.md`](files/README.md.md)
- [`START_GRAPHIFY.cmd`](files/START_GRAPHIFY.cmd.md)
- [`START_PLAYBOOK.cmd`](files/START_PLAYBOOK.cmd.md)
- [`Start-PlayBook-Desktop.ps1`](files/Start-PlayBook-Desktop.ps1.md)
- [`Store.cs`](files/Store.cs.md)
- [`ToolRunner.cs`](files/ToolRunner.cs.md)
- [`Workspace.cs`](files/Workspace.cs.md)
- [`appsettings.Development.json`](files/appsettings.Development.json.md)
- [`appsettings.json`](files/appsettings.json.md)
- [`graphify.ps1`](files/graphify.ps1.md)
- [`packages.lock.json`](files/packages.lock.json.md)
- [`playbook-harness.ps1`](files/playbook-harness.ps1.md)
- [`playbook.ps1`](files/playbook.ps1.md)
- [`playbook.sh`](files/playbook.sh.md)

**has commits by** ←

- [R B](people.md)
