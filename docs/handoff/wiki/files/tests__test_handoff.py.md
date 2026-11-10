---
generator: HandOff247
id: "file:tests/test_handoff.py"
type: File
source: "tests/test_handoff.py"
---

# `tests/test_handoff.py`

> Runs the full pipeline on a copy of the fixture outside Git, so both file-listing paths are covered.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 447
- **Source:** [tests/test_handoff.py](../../../../tests/test_handoff.py)

**Notes from the previous owner**

> Runs the full pipeline on a copy of the fixture outside Git, so both file-listing paths are covered.

**defines** →

- `AnalysisTests` · [tests/test_handoff.py:49](../../../../tests/test_handoff.py#L49)
- `LexerTests` · [tests/test_handoff.py:31](../../../../tests/test_handoff.py#L31)
- `PackTests` · [tests/test_handoff.py:142](../../../../tests/test_handoff.py#L142)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [tests/test_handoff.py:15](../../../../tests/test_handoff.py#L15)
- [`handoff247/build.py`](handoff247__build.py.md) · [tests/test_handoff.py:16](../../../../tests/test_handoff.py#L16)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [tests/test_handoff.py:17](../../../../tests/test_handoff.py#L17)
- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [tests/test_handoff.py:18](../../../../tests/test_handoff.py#L18)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [tests/test_handoff.py:19](../../../../tests/test_handoff.py#L19)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [tests/test_handoff.py:438](../../../../tests/test_handoff.py#L438)

**refers to** →

- [`HANDOFF.notes.md`](HANDOFF.notes.md.md) · [tests/test_handoff.py:153](../../../../tests/test_handoff.py#L153)
- [`README.md`](README.md.md) · [tests/test_handoff.py:139](../../../../tests/test_handoff.py#L139)
- [`pyproject.toml`](pyproject.toml.md) · [tests/test_handoff.py:272](../../../../tests/test_handoff.py#L272)

**mentions** →

- [`api.partner-billing.com`](../hosts.md) · [tests/test_handoff.py:269](../../../../tests/test_handoff.py#L269)
- [`5050`](../ports.md) (address literal) · [tests/test_handoff.py:111](../../../../tests/test_handoff.py#L111)

**starts** →

- [`git`](../commands.md) · [tests/test_handoff.py:290](../../../../tests/test_handoff.py#L290)

**is part of** ←

- [`tests`](../areas/tests.md)

## Comment in the file

End-to-end and unit tests. *(module docstring)*

## Defined here

- `copy_fixture` — function, [line 24](../../../../tests/test_handoff.py#L24) — Copy outside any Git work tree so the plain directory walk is exercised too.
- `LexerTests` — class, [line 31](../../../../tests/test_handoff.py#L31)
- `LexerTests.test_csharp_strings_and_comments_are_blanked` — method, [line 32](../../../../tests/test_handoff.py#L32)
- `LexerTests.test_js_regex_and_template` — method, [line 42](../../../../tests/test_handoff.py#L42)
- `AnalysisTests` — class, [line 49](../../../../tests/test_handoff.py#L49)
- `AnalysisTests.setUpClass` — method, [line 51](../../../../tests/test_handoff.py#L51)
- `AnalysisTests.tearDownClass` — method, [line 58](../../../../tests/test_handoff.py#L58)
- `AnalysisTests.test_modes` — method, [line 61](../../../../tests/test_handoff.py#L61)
- `AnalysisTests.test_dispatch_table_and_handlers` — method, [line 69](../../../../tests/test_handoff.py#L69)
- `AnalysisTests.test_routes_forward_to_table` — method, [line 78](../../../../tests/test_handoff.py#L78)
- `AnalysisTests.test_mcp_tools` — method, [line 83](../../../../tests/test_handoff.py#L83)
- `AnalysisTests.test_callers_and_channels` — method, [line 92](../../../../tests/test_handoff.py#L92)
- `AnalysisTests.test_launch_chain` — method, [line 105](../../../../tests/test_handoff.py#L105)
- `AnalysisTests.test_environment_and_ports` — method, [line 113](../../../../tests/test_handoff.py#L113)
- `AnalysisTests.test_code_edges` — method, [line 121](../../../../tests/test_handoff.py#L121)
- `AnalysisTests.test_comments_extracted` — method, [line 128](../../../../tests/test_handoff.py#L128)
- `AnalysisTests.test_cli_usage_in_docs` — method, [line 136](../../../../tests/test_handoff.py#L136)
- `PackTests` — class, [line 142](../../../../tests/test_handoff.py#L142)
- `PackTests.setUp` — method, [line 143](../../../../tests/test_handoff.py#L143)
- `PackTests.tearDown` — method, [line 147](../../../../tests/test_handoff.py#L147)
- `PackTests.test_build_notes_check_cycle` — method, [line 150](../../../../tests/test_handoff.py#L150)
- `PackTests.test_handoffignore` — method, [line 194](../../../../tests/test_handoff.py#L194)
- `PackTests.test_python_dispatch_needs_callables` — method, [line 202](../../../../tests/test_handoff.py#L202)
- `PackTests.test_notes_parse_is_lossless_for_existing_text` — method, [line 215](../../../../tests/test_handoff.py#L215)
- `PackTests.test_translations_cycle` — method, [line 220](../../../../tests/test_handoff.py#L220)
- `PackTests.test_handover_findings` — method, [line 274](../../../../tests/test_handoff.py#L274)
- `PackTests.test_git_state_and_files_only_on_this_computer` — method, [line 294](../../../../tests/test_handoff.py#L294)
- `PackTests.test_go_one_project` — method, [line 323](../../../../tests/test_handoff.py#L323)
- `PackTests.test_ontology_graph_and_wiki` — method, [line 348](../../../../tests/test_handoff.py#L348)
- `PackTests.test_go_folder_of_projects` — method, [line 403](../../../../tests/test_handoff.py#L403)
- `PackTests.test_foreign_detection` — method, [line 437](../../../../tests/test_handoff.py#L437)
