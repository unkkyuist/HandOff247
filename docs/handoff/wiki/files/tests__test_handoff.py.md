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
- **Lines:** 1061
- **Source:** [tests/test_handoff.py](../../../../tests/test_handoff.py)

**Notes from the previous owner**

> Runs the full pipeline on a copy of the fixture outside Git, so both file-listing paths are covered.
>
> <!-- added by HandOff247 for new items -->

**defines** →

- `AnalysisTests` · [tests/test_handoff.py:49](../../../../tests/test_handoff.py#L49)
- `LexerTests` · [tests/test_handoff.py:31](../../../../tests/test_handoff.py#L31)
- `PackTests` · [tests/test_handoff.py:142](../../../../tests/test_handoff.py#L142)
- `UserContextTests` · [tests/test_handoff.py:548](../../../../tests/test_handoff.py#L548)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [tests/test_handoff.py:15](../../../../tests/test_handoff.py#L15)
- [`handoff247/build.py`](handoff247__build.py.md) · [tests/test_handoff.py:16](../../../../tests/test_handoff.py#L16)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [tests/test_handoff.py:17](../../../../tests/test_handoff.py#L17)
- [`handoff247/explore.py`](handoff247__explore.py.md) · [tests/test_handoff.py:556](../../../../tests/test_handoff.py#L556)
- [`handoff247/handlers.py`](handoff247__handlers.py.md) · [tests/test_handoff.py:852](../../../../tests/test_handoff.py#L852)
- [`handoff247/journeys.py`](handoff247__journeys.py.md) · [tests/test_handoff.py:871](../../../../tests/test_handoff.py#L871)
- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [tests/test_handoff.py:18](../../../../tests/test_handoff.py#L18)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [tests/test_handoff.py:19](../../../../tests/test_handoff.py#L19)
- [`handoff247/screens.py`](handoff247__screens.py.md) · [tests/test_handoff.py:872](../../../../tests/test_handoff.py#L872)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [tests/test_handoff.py:533](../../../../tests/test_handoff.py#L533)

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
- `PackTests.test_model_summaries` — method, [line 403](../../../../tests/test_handoff.py#L403)
- `PackTests.test_mcp_server` — method, [line 455](../../../../tests/test_handoff.py#L455)
- `PackTests.test_go_folder_of_projects` — method, [line 498](../../../../tests/test_handoff.py#L498)
- `PackTests.test_foreign_detection` — method, [line 532](../../../../tests/test_handoff.py#L532)
- `source_line` — function, [line 544](../../../../tests/test_handoff.py#L544)
- `UserContextTests` — class, [line 548](../../../../tests/test_handoff.py#L548) — The application from its users' side, on a synthetic app with three user types: an author writes and uploads, an editor reviews and publishes, anyone reads the result.
- `UserContextTests.setUpClass` — method, [line 555](../../../../tests/test_handoff.py#L555)
- `UserContextTests.tearDownClass` — method, [line 565](../../../../tests/test_handoff.py#L565)
- `UserContextTests.line` — method, [line 568](../../../../tests/test_handoff.py#L568)
- `UserContextTests.test_user_types_come_from_role_checks` — method, [line 572](../../../../tests/test_handoff.py#L572)
- `UserContextTests.test_each_user_type_has_its_own_flow` — method, [line 583](../../../../tests/test_handoff.py#L583)
- `UserContextTests.test_flows_link_across_user_types` — method, [line 600](../../../../tests/test_handoff.py#L600)
- `UserContextTests.test_whole_chain_from_one_user_to_the_public_page` — method, [line 617](../../../../tests/test_handoff.py#L617) — author's action -> code -> data -> editor's follow-up -> what a reader sees.
- `UserContextTests.test_screen_term_to_implementation` — method, [line 648](../../../../tests/test_handoff.py#L648)
- `UserContextTests.test_terms_from_locale_files_in_every_language` — method, [line 661](../../../../tests/test_handoff.py#L661)
- `UserContextTests.test_same_words_in_two_places_are_told_apart` — method, [line 670](../../../../tests/test_handoff.py#L670)
- `UserContextTests.test_request_gives_points_to_check_not_a_diagnosis` — method, [line 681](../../../../tests/test_handoff.py#L681)
- `UserContextTests.test_shared_code_and_screens_are_modelled_once` — method, [line 701](../../../../tests/test_handoff.py#L701)
- `UserContextTests.test_uploaded_asset_from_form_to_public_page` — method, [line 722](../../../../tests/test_handoff.py#L722)
- `UserContextTests.test_generated_static_and_unreferenced_assets` — method, [line 743](../../../../tests/test_handoff.py#L743)
- `UserContextTests.test_data_states_carry_the_work_between_user_types` — method, [line 762](../../../../tests/test_handoff.py#L762)
- `UserContextTests.test_code_change_to_user_experience` — method, [line 774](../../../../tests/test_handoff.py#L774)
- `UserContextTests.test_every_connection_has_evidence_or_is_marked` — method, [line 796](../../../../tests/test_handoff.py#L796)
- `UserContextTests.test_unmatched_and_unanalysed_parts_are_reported` — method, [line 828](../../../../tests/test_handoff.py#L828)
- `UserContextTests.test_sql_reading` — method, [line 851](../../../../tests/test_handoff.py#L851)
- `UserContextTests.test_role_conditions_and_route_matching` — method, [line 869](../../../../tests/test_handoff.py#L869)
- `UserContextTests.test_decorators_read_as_access_checks` — method, [line 895](../../../../tests/test_handoff.py#L895)
- `UserContextTests.test_pages_without_routes_and_their_scripts` — method, [line 911](../../../../tests/test_handoff.py#L911) — A single-page app: no route renders the page, its script calls the API.
- `UserContextTests.test_pack_pages_graph_and_wiki` — method, [line 926](../../../../tests/test_handoff.py#L926)
- `UserContextTests.test_trace_command` — method, [line 987](../../../../tests/test_handoff.py#L987)
- `UserContextTests.test_mcp_server_gives_an_agent_the_whole_project` — method, [line 1004](../../../../tests/test_handoff.py#L1004)
