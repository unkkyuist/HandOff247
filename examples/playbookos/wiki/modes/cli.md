---
generator: HandOff247
id: "mode:cli"
type: Mode
source: "Program.cs"
---

# `cli`

> One operation per process: `PlayBook.dll cli <operation> <json | @file | ->`. Errors go to stderr as JSON with exit code 1.

- **Class:** Run mode — A way to start the program, picked by its first argument.
- **Reads standard input:** yes
- **Source:** [Program.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L20)

**Notes from the previous owner**

> One operation per process: `PlayBook.dll cli <operation> <json | @file | ->`. Errors go to stderr as JSON with exit code 1.

**uses** →

- [`Json`](../files/Domain.cs.md) · [Program.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L20)
- [`Operations`](../files/Operations.cs.md) · [Program.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L20)

**serves** →

- [`Operations.Execute`](../operations.md) · [Program.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L20)

**is defined in** ←

- [`Program.cs`](../files/Program.cs.md) · [Program.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L20)
