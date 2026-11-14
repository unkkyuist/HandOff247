# HandOff247 notes · newsroom

<!--
HandOff247 notes. Write in plain sentences under each heading; the text is shown next to that item in the handoff pack.
Lines that still start with TODO count as undocumented. Keep the headings exactly as they are (they are matched by name).
Never paste passwords or tokens here — say where they are kept instead.
-->

## Project
A small publishing application that exists only as a test fixture for HandOff247 (`tests/fixtures/newsroom`). Authors write articles and upload a cover image, editors review and publish them, and readers see the published articles on the front page. It is not deployed anywhere; the notes below are example text.

## Topic: Successor checklist
TODO: First things a successor must do (accounts, machines, deploy steps, scheduled jobs).

## Topic: Known issues and risks
Publishing refuses an article without a cover image while `NEWSROOM_COVER_REQUIRED` is `1` (the default). Editors usually report this as "the Publish button does nothing"; the message is shown on the review page.

## Topic: Credentials and accounts
TODO: Where credentials and keys are kept (location only, never the values).

## Topic: Open work and next steps
TODO: What is half done, what was promised to someone, and what you would do next.

## Topic: Deploy and release
TODO: How a change reaches users: where it runs, who can deploy, the exact steps, how to roll back.

## Topic: Routine operations
TODO: What has to be done by hand and how often (daily, monthly, renewals), what to watch, what to do when it breaks.

## Topic: Data and backups
TODO: Where the data lives, what is backed up and how to restore it, what cannot be recreated.

## Topic: People and contacts
TODO: Who uses it, who to ask about what, vendors and other teams (names and how to reach them).

## User: author
Reporters. They mostly ask why an article they sent is not on the front page yet: it is waiting in the editors' queue, or an editor sent it back with a note.

## User: editor
The news desk. They mostly ask about articles that will not publish and about cover images that do not show.

## Area: locales
TODO: What lives in this folder and why.

## Area: static
TODO: What lives in this folder and why.

## Area: templates
TODO: What lives in this folder and why.

## File: app.py
TODO: Role of this file; anything surprising about it.

## File: auth.py
TODO: Role of this file; anything surprising about it.

## File: db.py
TODO: Role of this file; anything surprising about it.

## File: static/site.css
TODO: Role of this file; anything surprising about it.

## File: storage.py
TODO: Role of this file; anything surprising about it.

## File: templates/article.html
TODO: Role of this file; anything surprising about it.

## File: templates/base.html
TODO: Role of this file; anything surprising about it.

## File: templates/desk.html
TODO: Role of this file; anything surprising about it.

## File: templates/edit.html
TODO: Role of this file; anything surprising about it.

## File: templates/home.html
TODO: Role of this file; anything surprising about it.

## File: templates/login.html
TODO: Role of this file; anything surprising about it.

## File: templates/review.html
TODO: Role of this file; anything surprising about it.

## File: templates/review_detail.html
TODO: Role of this file; anything surprising about it.
