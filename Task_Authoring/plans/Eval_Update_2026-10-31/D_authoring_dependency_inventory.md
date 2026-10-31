# D — Task_Authoring dependency inventory on the eval bundle

Scope: `Task_Authoring/skills/*/SKILL.md`, `Task_Authoring/playbooks/*.md`, `Task_Authoring/setup/*`, `Task_Authoring/Guide/*.md`, `Task_Authoring/README.md`, `Task_Authoring/references/*.md|*.json`, `references/Docs/*.md` (rule-overlap only), `references/Tasks_Template/**`, `tools/*.py`, `tests/*.py`, and the root file `learnings`.
Evidence is from the CURRENT bundle (`Evals/` + `claude/`) compared against `Eval-new/Evals/` (`ENVIRONMENT.md`, `INPUTS.md`, `UNIVERSE_MAP.md`, `tools/hg_universe.py`, `tools/hg_injection_lint.py`, `references/universes/**`, `3_Rubrics_Eval.md`). `HarmonyGames_*` data folders, `Task_Authoring/support/**`, `Task_Authoring/task_inputs*/` and `archived_tasks/` were not read.

## Summary (biggest risks under the new bundle)

- **One registry selects the wrong universe for every task.** `universe_sources.json` maps both dates to the single old manifest (`Evals/references/universe_manifest.json`, clock `2026-02-14 00:00`), so `--require-source` validates a Feb-2026 source for an Oct-1 task. The new bundle has two manifests under `references/universes/{normal,synthcut}/` and no default. (§2)
- **The Oct 1 freeze is wrong by seven hours.** `v3_policy.json`, `GEN_EXECUTION`, `task_context.py` and all fixtures use `2025-10-01T00:00:00Z`; the new synthcut clock is `2025-10-01 07:00 UTC` (PT midnight). Every "Pacific plus UTC" acceptance and every post-clock check inherits the error. (§3)
- **The "same data for both dates" premise is asserted in ~30 files** (all 11 skills, 11 playbooks, GEN_EXECUTION, Guide, README, Manual_Commands, 5 references). It is now false for six whole storylines and the shutdown, so it cannot be patched in one place. (§2)
- **No shutdown or departed-person rule exists anywhere in Task_Authoring.** The Feb-11-2026 announcement, the Feb-11 termination letters and the backdated terminations exist only as recalled *atlas* facts, not as rules; Oct-1 tasks must not apply them and Feb-14 tasks must. (§3)
- **The scenario/knowledge products are Feb-14 artifacts.** `universe_kb` (`_meta.clock = 2026-02-14T00:00:00Z`), `Scenario_Atlas`, `Persona_Briefs`, `Universe_Brief`, `Ask_Carriers` and `Hardness_Mastery` all carry Combo Fighter, Zombie Match Lite, the Telegram DD port, the UI-sprite sprint, the Mattel Barbie pitch and the web-distribution partnership as live material. (§8, §3)
- **Five tools hard-code the Feb 14 clock as a module default** (`sql_lint.py:42`, `base_check.py:92`, `persona_view.py:111`, inherited by `fact_check.py:65`, `entity.py`), and `runtime_context.py:98` hard-codes the string `"2026-02-14"`. (§3)
- **The old folder layout is assumed in code**: `HarmonyGames_*` roots in `base_check`, `persona_view`, `entity`, `shortcut_probe`; `Evals/tools/hg_search.py` and `Evals/references/universe_manifest.json` literals in `setup/local_search.py`; `Evals/references/persona/roster.json` in `task_context.py`/`persona_view.py`. (§2)
- **No task-date input channel.** `00_Assigments.md` carries a platform `Universe Date` display string only; there is no `universe` saved input, no `hg_store_input.py` call, and the loader maps the date through a hard-coded freeze table. (§7)
- **Eval-rule versions have already drifted.** `playbooks/09:212` rates `overly_broad` Moderate; the current `hg-strict-overrides-v1` made it Major on 2026-10-17, and the QC quality bands changed with `rubric-flow-v2` (2026-10-09). (§4)
- **Local linters duplicate the eval and can disagree**: `sql_lint.py` (144-table `universe_schema_live.json`, own clock) vs new `hg_injection_lint.py` (58-table `references/schema/injection.json`, `id_contracts.json`, clock from `hg_universe`); `base_check.py` re-implements `/injection` Checks A and C. (§6)
- **The new input/preflight helpers are deliberately excluded** (`setup/local_search.py:34` skips `hg_store_input.py`, `hg_write_output.py`, `hg_preflight.py`), and nothing calls `hg_universe.py`. (§5)
- **`learnings:80` already records this exact failure**: "The platform report used a synth-cut source and a different clock interpretation from the local shared-universe authoring context."

Counts: §1 11 skills × 6 columns (all 11 mapped); §2 39 rows / 30 files; §3 48 rows; §4 36 rows; §5 11 rows; §6 12 rows; §7 9 rows; §8 8 rows.

## 1. Routing map

Every `SKILL.md` opens with "Read `<bundle>/setup/GEN_EXECUTION.md` first, then follow the playbook … in full" and ends with "Self-review (GEN_EXECUTION §6a)" plus `stage_gate.py` (GEN_EXECUTION §6b). So **all 11 skills depend on GEN_EXECUTION §0, §1, §6a, §6b**; the column below lists only the additional section a skill names. "Templates" = `references/Tasks_Template/**` plus the in-playbook output template.

| Skill | Playbooks | References | Tools | Templates | GEN_EXECUTION sections |
|---|---|---|---|---|---|
| create-scenario | `01_Scenario_Design.md` (S0r–S9, §template) | `Hardness_Mastery.md`, `Scenario_Atlas.md`, `Ask_Carriers.md`, `Universe_Brief.md`, `Persona_Briefs.md`, `Hardness_Manifest_Spec.md`, `universe_kb/{timeline,cohorts,trap_catalog,coherence_hazards,activity,integrations,conventions}` | `task_context.py`, `hardness_gate.py --design`, `gradable_surface.py validate`, `redteam_review.py --dual`, `persona_view.py reach`, `entity.py collisions/resolve`, `hardness_ledger.py priors`, `trap_liveness.py --design`, `hardness_forecast.py forecast --design`, `stage_gate.py scenario` | `Tasks_Template/00_Assigments.md`; `01_Scenario_Design.md` template | **§3a** (named in SKILL), §6a, §6b |
| create-injection | `01_Universe_Injection.md` (S1–S7) | `universe_schema_live.json`, `Ask_Carriers.md`, `Native_Artifact_Anatomy.md`, `universe_kb/integrations.json`, `Hardness_Manifest_Spec.md`, `setup/extract_schema.sql` | `sql_lint.py`, `base_check.py`, `fact_check.py --no-leak`, `persona_view.py check-sql`, `hardness_gate.py`, `oracle_kit.py check/truth`, `difficulty_mutation.py mutate/geometry`, `trap_liveness.py`, `hardness_forecast.py`, `preflight_report.py`, `stage_gate.py injection` | `Tasks_Template/01_Universe_Inject.sql`, `Working_Files/01_Grounding_Dossier` headings | §6a, §6b |
| create-hardening | `01a_Hardening.md` (MODE A/B) | `Hardness_Mastery.md` (unverified section), `Evals/1A_Hardness_Eval.md`, `Evals/1B_Haiku_Prediction_Eval.md` | `trajectory_ledger.py`, `node_verdicts.py`, `surface_grader.py`, `hardness_ledger.py`, `hardness_forecast.py`, `stage_gate.py hardening` | `Tasks_Template/06_PreCheck_Trajectory/`, `07_Baseline_Trajectories/`, `10_Baseline_Verifier_Results.md` | §2 (authorship), §6a, §6b |
| create-error-async | `03_Error_Async_Config.md` | `Evals/references/tools/catalog.json`, `Evals/1_Prompt_Eval.md` §1.5/§2.2, `Evals/2_Oracle_Events_Eval.md` §3.5, `Evals/references/rules/long_horizon.md`, `Evals/WORKFLOW.md` | `hg.py search`, `stage_gate.py error-async` | `Tasks_Template/03_Error_Async_Config.txt` | §6a, §6b |
| create-reference-files | `02_Reference_Files.md` | `Native_Artifact_Anatomy.md` (§M + source service), `Evals/WORKFLOW.md` (`prompt-incorporation-v1`), `Evals/1_Prompt_Eval.md` | `hg.py search`, `stage_gate.py reference-files` | `Tasks_Template/02_Reference_Files/README.md` (deleted on write) | §6a, §6b |
| create-prompt-writing | `04_Prompt_Writing.md` (brief + C1–C24 check) | `Evals/references/persona/roster.json`, `acl.md`, `Evals/references/tools/catalog.json`, `Evals/references/rules/task_categories.md`, `1_Prompt_Eval.md`, `scoring.json`, `prompt_qc_examples.md`/`prompt_qc_cases.json`, `Docs/{6_Prompt Writing,9_Common Errors,10_Long Horizon,4_Persona ACL} - V2.md`, `QC_Spec_Doc_Latest.csv`, `Taxonomy_V2_Step_Map.md`, `universe_kb/trap_catalog.json` | `persona_view.py search/can-see`, `entity.py collisions/resolve`, `gradable_surface.py gradeable-report`, `hg.py search`, `stage_gate.py prompt-writing/prompt-check` | `Tasks_Template/04_Prompt.txt`; `04_Prompt_Writing_Brief.md` §1–§13 | §2, §6a, §6b |
| create-humantime | `05_Human_Time_Estimate.md` | `Tasks_Template/05_Human_Time.md`, `Evals/references/Docs` (no QC row — playbook states it) | `hg.py search`, `stage_gate.py humantime` | `Tasks_Template/05_Human_Time.md`, `Working_Files/05_Human_Time_Worksheet.md` | §6a, §6b |
| create-oe-writing | `08_Oracle_Event_Writing.md` | `roster.json`, `acl.md`, `catalog.json`, `Evals/references/schema/snowflake.json`, `Evals/2_Oracle_Events_Eval.md`, `Evals/references/rules/oracle_events.md` + `oracle_events_qc_examples.md`/`.json`, `Docs/{7_Oracle Events,9_Common Errors} - V2.md`, `QC_Spec_Doc_Latest.csv` | `persona_view.py can-see/check-sql`, `hg.py search`, `stage_gate.py oe-writing/oe-check` | `Tasks_Template/08_Oracle_Events.md`, `Working_Files/08_OE_Writing_Ledger.md` §A–§F | §2, §6a, §6b |
| create-rubric-writing | `09_Rubric_Writing.md` (prep/check, gate 1–17, §templates) | `Evals/3_Rubrics_Eval.md`, `qc_rubric_v10.md`, `coherent_record.md`, `rubric_sampling.md`, `rubric_factual_checks.md`, `rubric_qc_examples.md`/`.json`, `Docs/{8_Rubric Writing,7_Oracle Events,10_Long Horizon,9_Common Errors,4_Persona ACL} - V2.md`, `QC_Spec_Doc_Latest.csv`, `Taxonomy_V2_Step_Map.md`, `Hardness_Manifest_Spec.md` | `shortcut_probe.py`, `persona_view.py can-see`, `hg.py`, `stage_gate.py rubric-writing/rubric-check` | `Tasks_Template/09_Rubrics.json`; `09_Rubric_Writing_Plan.md` §A–§G | §2, §6a, §6b |
| create-allfail | `11_AllFail_Analysis.md` | `Evals/references/rules/all_failing.md`, `coherent_record.md`, `scoring.json`, `Docs/8_Rubric Writing - V2.md` §11, `Evals/WORKFLOW.md` (`prompt-incorporation-v1`) | `difficulty_stats.py --build`, `hg.py search`, `stage_gate.py allfail` | `Tasks_Template/11_AF_Justification.md` | §6a, §6b |
| create-difficulty | `12_Difficulty.md` | `QC_Spec_Doc_Latest.csv`, `scoring.json`, `long_horizon.md`, `docs/…` (unverified) | `difficulty_stats.py --build`, `trajectory_ledger.py --sql`, `hardness_forecast.py score`, `stage_gate.py difficulty` (+ `release`) | `Tasks_Template/10_Baseline_Verifier_Results.md`; `Working_Files/12_Difficulty_Stats.txt` | §6a, §6b |

Edit-ownership consequence: a change to `GEN_EXECUTION §0/§3` touches all 11 skills; a change to the clock touches all 11 playbooks' "Inputs / Output" paragraph; a universe change touches `references/*` and `universe_kb`, which every design/injection/prompt/rubric stage reads.

## 2. Single-universe / old-layout assumptions

| file:line | snippet | why it breaks |
|---|---|---|
| `references/universe_sources.json:7,14` | `"manifest": "Evals/references/universe_manifest.json"` (both dates) | Old single manifest; new bundle has `references/universes/{normal,synthcut}/universe_manifest.json` per date. |
| `references/universe_sources.json:3` | "both V3 dates use the same supplied universe data" | The premise the new bundle replaces: two universes, and Oct 1 lacks six storylines. |
| `references/universe_sources.json:6,13` | `"mode": "shared-universe"` | Mode exists only to model "one export, two freezes"; the new bundle selects a universe, it does not reinterpret one. |
| `references/universe_sources.json:8-9` | `"kb_path": "Task_Authoring/references/universe_kb"`, `"kb_output_path": …/by_date/2025-10-01` | One KB for both dates; the `by_date/2025-10-01` directory **does not exist** (Feb KB only). |
| `setup/GEN_EXECUTION.md:47` | "Both assigned freeze dates use the same local universe data." | Setup instruction for every command; false. |
| `setup/GEN_EXECUTION.md:69-73` | "maps both assigned dates to the same local universe manifest … No separate October export or date-specific KB build/review is required." | Explicit instruction **not** to use a second universe. |
| `setup/GEN_EXECUTION.md:240-243` | "The shared universe is split across the folders in the validated context's `source.manifest` (the read-only Evals manifest for both assigned dates)." | Location authority points at the old `Evals/references/universe_manifest.json`. |
| `setup/GEN_EXECUTION.md:87-88` | "`HarmonyGames_GitHub/`, `HarmonyGames_Gmail/` and `HarmonyGames_Other_Services/` are read-only" | Root folder names; new roots are `Universe_Normal/Normal_HarmonyGames_*`, `Universe_SynthCut/SynthCut_HarmonyGames_*`. |
| `setup/GEN_EXECUTION.md:268-271` | `Evals/references/tools/catalog.json` (298 tools) · `Evals/references/persona/roster.json` (17) · `Evals/references/schema/injection.json` | Shared-reference locations survive, but all three are universe-independent only by assumption; the 58-table snapshot is described as advisory. |
| `setup/GEN_EXECUTION.md:297` | "Each slot maps to an Evals input key (`Evals/INPUTS.md`, last column)" | New `INPUTS.md` adds a `universe` key/key set that has no `Task_Authoring` slot. |
| `Guide/How_To_Author_A_Task.md:220-221` | "Both freeze dates use the same local data; a February archive label is provenance, not an October-task blocker." | Explicitly tells the author to ignore the February source for an October task. |
| `Guide/How_To_Author_A_Task.md:234` | "No separate October dataset or KB review is needed." | Contradicts per-universe references. |
| `Guide/Manual_Commands.md:34-35` | "Both dates use the same local universe data." | Copy-paste command text handed to the user. |
| `README.md:84-86` | "`references/universe_sources.json` maps both freeze dates to the same local universe data and shared KB." | Install-time instruction. |
| `README.md:127` | "Both freeze dates use the same data" | Tool-table description of `task_context.py`. |
| `references/Hardness_Mastery.md:8-9` | "Both freeze dates use the same local data; no separate October export or KB build is required." | Read before every design. |
| `references/Universe_Brief.md:3-8` | "both freeze dates use the same local universe data … No separate October dataset/KB build is required." | Orientation doc for every scenario. |
| `references/Persona_Briefs.md:3-6` | "both freeze dates use the same local universe data … No separate October dataset or KB review is needed." | Persona reach/voice source. |
| `references/Scenario_Atlas.md:3-6` | "both freeze dates use the same local universe data … no separate October dataset/KB gate." | Storyline source; the six missing storylines are inside it. |
| `references/Hardness_Manifest_Spec.md:7-8` | "Both dates use the same local export" | Manifest contract read by every gate. |
| `playbooks/01_Scenario_Design.md:34-35` | "Both freeze dates use the same local universe data … shared KB summaries are leads, not a separate dataset gate." | Stage-1 input rule. |
| `playbooks/01_Universe_Injection.md:39-40,76` | "Both freeze dates use the same local universe data." (twice) | Stage-2 input rule and hard gate 4. |
| `playbooks/02_Reference_Files.md:36-37,61` | "Both freeze dates use the same local universe data." / "Both dates use the same local data." | Reference-file grounding. |
| `playbooks/03_Error_Async_Config.md:43-44` | same sentence | Friction config. |
| `playbooks/04_Prompt_Writing.md:47-48` | same sentence | Prompt brief/check. |
| `playbooks/05_Human_Time_Estimate.md:28-29` | same sentence | Human time. |
| `playbooks/08_Oracle_Event_Writing.md:38-39` | same sentence | OE ledger. |
| `playbooks/09_Rubric_Writing.md:36-37,161` | same sentence + "Both freeze dates use that same local data." | Rubric plan and check. |
| `playbooks/11_AllFail_Analysis.md:24-25` | same sentence | All-fail. |
| `playbooks/01a_Hardening.md:19-20` | same sentence | Hardening. |
| `skills/*/SKILL.md` (all 11; e.g. `create-scenario:23-24`, `create-rubric-writing:28`) | "Both dates use the same local data; validate relied-on record dates and earlier state before grounding." | Repeated in every command's Inputs block. |
| `setup/local_search.py:62-64` | `src_dir = WORKSPACE / "Evals" / "tools"` … "keep Task_Authoring/ beside Evals/" | Hard-coded old bundle path and sibling-folder assumption; new bundle is `Eval-new/Evals/`. |
| `setup/local_search.py:45-49` | patches literal `Evals/references/universe_manifest.json` via `TASK_AUTHORING_UNIVERSE_MANIFEST` | Patches the old single-manifest path only; per-universe manifests still work through the env var but the trigger string may vanish. |
| `tools/task_context.py:26` | `ROSTER_PATH = WORKSPACE / "Evals" / "references" / "persona" / "roster.json"` | Old bundle location; no fallback to `Eval-new/`. |
| `tools/task_context.py:168-175` | `manifest.get("evaluation_clock")` then `if mode == "shared-universe" and clock < freeze: raise` | Assumes one manifest clock; with the synthcut manifest this comparison no longer expresses "same source". |
| `tools/task_context.py:180-182` | "Non-GitHub/Gmail services must share one Services_Data parent" | Layout rule built for `HarmonyGames_Other_Services/Services_Data`; new per-universe trees satisfy it but the error text/assumption is stale. |
| `tools/base_check.py:88-90` | `OTHER = WS / "HarmonyGames_Other_Services" / "Services_Data"` (and GitHub/Gmail) | Old roots; overridden at runtime by `runtime_context`, but the defaults and self-tests stay on the old layout. |
| `tools/persona_view.py:103-107` | same three roots + `ROSTER_V1 = WS / "Evals" / "references" / "persona" / "roster.json"` | Old roots and old roster path. |
| `tools/shortcut_probe.py:241` | `for root in sorted(WS.glob("HarmonyGames_*"))` | Globs the old root folders; finds nothing under `Universe_*`. |
| `tools/selftest_sandbox.py:62` | `LINKED = ("Evals", "HarmonyGames_GitHub", "HarmonyGames_Gmail", "HarmonyGames_Other_Services")` | Self-test sandbox links the old four folders. |
| `tools/test_task_context.py:193-199` | reads `Evals/tools/{hg_search,hg_records,hg_reference,hg_compact_index}.py` | Test asserts the old helper set/location. |
| `references/Ask_Carriers.md:11,17-18,23` | "the folder that holds `Evals/`, `claude/`, `Task_Authoring/` and the three `HarmonyGames_*` folders"; `Evals/references/{source_layout.json, universe_manifest.json}`; `Evals/references/search_indexes/snowflake-snowflake.json` | Old layout in the carrier authority used by design and injection. |
| `tools/runtime_context.py:89-109` | `shared-universe` branch; `# preserve the established February view exactly`; `if not clock and universe_date_key == "2026-02-14"` | Runtime explicitly models "one KB, earlier freeze" instead of "one universe per date". |
| `tools/v3_artifact_checks.py:207,354` | requires `temporal_evidence` for `shared-universe`; branches on `mode == "shared-universe"` | Evidence checks keyed to the retired mode. |
| `learnings:80` | "The platform report used a synth-cut source and a different clock interpretation from the local shared-universe authoring context." | The failure this inventory is about, already observed on 30/31 Oct 2026. |

## 3. Hard-coded dates, clock, shutdown, departed personas, post-cut storylines

| file:line | hard-codes | why it breaks |
|---|---|---|
| `tools/sql_lint.py:42` | `CLOCK = dt.datetime(2026, 2, 14, tzinfo=dt.timezone.utc)` | Module default; overridden from context, but the fallback (and every `--legacy-v2`/self-test path) is Feb 14. |
| `tools/sql_lint.py:525,537` | `return when > CLOCK if … else when >= CLOCK` / error text with `CLOCK.isoformat()` | Boundary semantics are defined against whichever clock is loaded — for synthcut the correct clock is `07:00Z`, not `00:00Z`. |
| `tools/base_check.py:92` | `CLOCK = dt.datetime(2026, 2, 14, …)` | Same; also used for the ±60-day voice window. |
| `tools/base_check.py:1415` | `lo, hi = t - 60d, min(t + 60d, CLOCK)` | Voice-realism window anchored on the clock. |
| `tools/persona_view.py:111` | `CLOCK = dt.datetime(2026, 2, 14, …)` | Reach/recency math, `:207`, `:675`, `:718-719`. |
| `tools/fact_check.py:65` | `from base_check import (CLOCK, …)` | Inherits the Feb default; `:294` uses `CLOCK.year` to complete a bare date. |
| `tools/entity.py:254,392` | `if d and d <= pv.CLOCK` / `"clock": pv.CLOCK.isoformat()` | Entity activity and `entities.json` metadata clock. |
| `references/v3_policy.json:5-8` | `"2025-10-01": "2025-10-01T00:00:00Z"`, `"2026-02-14": "2026-02-14T00:00:00Z"` | Wrong Oct clock (new: `2025-10-01 07:00 UTC`); also the sole freeze source for `task_context`. |
| `tools/task_context.py:60-61` (via GEN_EXECUTION) / `:221-223` | freeze = `policy["freeze_dates"][date]` | Two hard-coded values; the Oct one is 7 h early. |
| `setup/GEN_EXECUTION.md:60-61` | "The canonical freeze is the assigned date at 00:00 UTC, either `2025-10-01T00:00:00Z` or `2026-02-14T00:00:00Z`." | The rule that produces the 7-hour error. |
| `setup/GEN_EXECUTION.md:157` | table row: "**2025-10-01T00:00:00Z** or **2026-02-14T00:00:00Z**" | Numbers of record. |
| `setup/GEN_EXECUTION.md:57-58` | "a February archive label does not make an October assignment unsupported" | Treats the Feb source as usable for October. |
| `Guide/How_To_Author_A_Task.md:223-224` | "the assigned 00:00 UTC freeze. A displayed `07:00` is retained as input text, not silently interpreted as a new freeze." | Directly contradicts the new synthcut clock (07:00 **is** the freeze). |
| `tools/runtime_context.py:98` | `if not clock and context["universe_date_key"] == "2026-02-14": return data` | Hard-coded date string in the KB provenance path. |
| `tools/task_context.py:130-142` | `_date_key` "The time is preserved, not converted. V3 defines the two assignment dates." | The displayed time is preserved in text only; the freeze ignores it. |
| `tools/task_context.py:250-262` | `date_acceptance` returns `pacific`/`utc` and "display": `pacific + " PT"` | For an Oct 1 07:00Z instant this prints `2025-09-30 PT`, i.e. the wrong persona "today". |
| `tools/test_task_context.py:54-55` | `assertEqual(ctx["universe_date_raw"], "October 1, 2025 07:00")` / `freeze_utc == "2025-10-01T00:00:00Z"` | Locks the 7-hour error into the test suite for the exact platform display value. |
| `tools/test_task_context.py:185` | `date_acceptance("2025-10-01T00:00:00Z")["pacific"] == "2025-09-30"` | Encodes the off-by-one-day Pacific behaviour. |
| `tools/test_task_context.py:106-108` | October context gets `data_clock 2026-02-14T00:00:00Z` | Test asserts one Feb clock serving an Oct task. |
| `tests/test_v3_stage_gate.py:60` | `mode="shared-universe", data_clock="2026-02-14T00:00:00Z"` | Fixture for the shared mode. |
| `references/Tasks_Template/00_Assigments.md:78-79` | "October 1, 2025 → `2025-10-01T00:00:00Z`; February 14, 2026 → `2026-02-14T00:00:00Z`" | Every task starts from this template. |
| `references/Scenario_Atlas.md:417` | "Orderly wind-down, Feb 9–13 2026" | Shutdown storyline presented as a live option; invalid for Oct 1. |
| `references/Scenario_Atlas.md:449-488` | shutdown decided Feb 9; contracts terminated; Feb 11 letters; Sherwood/Sunset; `evt_…` wind-down calls | Shutdown mechanics; none may appear in an Oct-1 task. |
| `references/Scenario_Atlas.md:531-546` | "Frederick Stone received an 'involuntary termination' notice effective Oct 24 … The remaining contractors were terminated by letter on Feb 11 2026." | Termination/backdating material. |
| `references/Scenario_Atlas.md:506,515` | "except Frederick, who was terminated Oct 24" / '"Shut down" vs still working' | Persona status and shutdown framing. |
| `references/Scenario_Atlas.md:565-570` | Calvin Price termination, Frederick's role, "Date typo … effective January 31, 2025" | Departure/backdating traps. |
| `references/Ask_Carriers.md:104` | "The clock is 2026-02-14T00:00:00Z, a Saturday. The last weekday is 2026-02-13." | Hard-coded clock and activity census; no Oct variant. |
| `references/Ask_Carriers.md:982` | "All timestamps must be before 2026-02-14T00:00:00Z." | SQL skeleton instruction. |
| `references/Native_Artifact_Anatomy.md:92` | "keep every date before 2026-02-14" | Naming guidance for reference files. |
| `references/Taxonomy_V2_Step_Map.md:122,124,511,651` | "The universe is frozen at **February 14, 2026, 12:00 AM**" | Three separate restatements of the single clock. |
| `references/Persona_Briefs.md:8` | "Fixed clock **2026-02-14T00:00:00Z** (Saturday)." | Persona orientation. |
| `references/Persona_Briefs.md:5` | "later departures, pivots or wind-down facts cannot be October knowledge" | Knows the hazard but supplies no rule. |
| `setup/GEN_EXECUTION.md:178` | "**17 usable**: the roster in `Evals/references/persona/roster.json`. `thomas` and `tim_steudler` …" | Persona set assumed identical across universes. |
| `references/Scenario_Atlas.md:14` | "Only the 17 personas in `Evals/references/persona/roster.json` pass `/prompt`." | Same. |
| `references/Persona_Briefs.md:73` | "### Victor Barnes — Game Engineer … `victor_barnes`" | Present-tense persona; on Oct 1 he is the one departed person (Apr 2025). |
| `references/Ask_Carriers.md:135,639` | `usr_Victor Barnes`, token `EMPLOYEE_0030` / `user_EMPLOYEE_0030` | Identity tokens used in examples. |
| `references/Scenario_Atlas.md:535` | "End months 2025-10-31 for Felix, Victor Barnes, Josh Dempsey …" | Departure facts stated as rosters, not as rules. |
| `references/universe_kb/timeline.md:26` | "2025-04-15 \| people \| Victor Barnes goes quiet (last authored activity 2025-04-15 via slack)" | The only departed person at Oct 1; encoded as a timeline beat, not a rule. |
| `playbooks/01_Universe_Injection.md:306` | "a `$0` roster + headcount line to 2026-02-13 (payee counts unchanged)" | A Feb-2026-specific "still on unpaid" convention that cannot exist on Oct 1. |
| `playbooks/01_Universe_Injection.md:142` | "boards went quiet in Nov 2025 — 2026 activity stands out" | Feb-2026-relative Trap rationale. |
| `references/Persona_Briefs.md:34` | "Mattel 'Dream Life Glow' pitch · Combo Fighter live experiment · Telegram DD port · Helpshift wind-down" | Three post-cut storylines in one line. |
| `references/Persona_Briefs.md:40,46,58` | Combo Fighter backend; Combo Fighter design; Combo Fighter UX | Post-cut (Nov 2025–Feb 2026). |
| `references/Persona_Briefs.md:62,64-65` | Mattel pitch deck + Q&A prep; Zombie Match Lite scoping | Post-cut. |
| `references/Persona_Briefs.md:98-100` | "Zombie Match Lite branch work" / "Zombie Match Lite (stalled)" | Post-cut. |
| `references/Persona_Briefs.md:135,179,195` | Tim Steudler as Mattel licensing contact; "Person 5536 \| BD / Partnerships (web distribution)"; "Mattel Game Studios (Barbie pitch)" | Post-cut partners. |
| `references/Scenario_Atlas.md:61,65,68` | Quest lifecycle through "Zombie Lite"; difficulty work through Oct 2025; "Reserve A \| Combo Fighter monetisation readiness … Nov 2025 – Feb 2026" | Post-cut storyline entries in the ranked Atlas. |
| `references/Scenario_Atlas.md:163-225,246-257,313,338,347-352` | Zombie Match 3D/Lite, season pass, leaderboards, rebuild PRs | Some pre-cut, but the Atlas presents them as Feb-current. |
| `references/Scenario_Atlas.md:386-393` | "A. Combo Fighter monetisation readiness" with Nov-2025 kickoff, Dec–Feb Meta spend, 90 revenue rows | Entirely post-cut. |
| `references/Scenario_Atlas.md:423,442,445` | "Rank 7, Mattel Barbie 'Dream Life Glow'"; "Publisher / web distribution canvass"; row 7 Mattel | Two post-cut storylines. |
| `references/Scenario_Atlas.md:453,515` | "Shutdown was decided Feb 9 after Combo Fighter's data came in"; "Combo Fighter PRs were still merged after the shutdown announcement" | Shutdown + Combo Fighter coupled. |
| `references/Scenario_Atlas.md:581-587` | "Combo Fighter ran Meta campaigns from Dec 2025 to Feb 2026" | Post-cut UA storyline. |
| `references/Scenario_Atlas.md:761-786` | "## 7. Mattel Barbie 'Dream Life Glow' (Aug–Dec 2025)" | Post-cut pitch (won't exist on Oct 1). |
| `references/Universe_Brief.md:17-21` | "$3M Series Seed … Zombie Match 3D … Combo Fighter (fighting-meets-match-3)" | Narrative treats post-cut titles as core. |
| `references/Universe_Brief.md:100` | "Elliot Mercer termination and backfill" | Personnel fact needing per-universe status. |
| `learnings:186` | "The freeze 2026-02-14T00:00Z is Friday 4:00 pm Pacific … the platform reads the universe date as the persona's today (Saturday)" | The persona-"today" rule that must be re-derived per universe. |

## 4. Cited eval rule IDs / versions / thresholds / paraphrased rules

| file:line | cites | snippet |
|---|---|---|
| `setup/GEN_EXECUTION.md:166` | `hg-strict-overrides-v1` | "**Harness tolerance for predicted all-fail rows is 0** (stricter than `/rubric`)" |
| `setup/GEN_EXECUTION.md:159` | `horizon-tiers-v1` | "Normal **50–100** tool calls · Long **100–500+**" |
| `setup/GEN_EXECUTION.md:163-164` | `Evals scoring.json` | "> 0.3 suggests ambiguous rubrics, < 0.1 a deterministic task" |
| `setup/GEN_EXECUTION.md:170` | QC Spec V2 | "> 10% major, > 15% moderate-or-worse, or > 20% minor-or-worse issues = Fail" |
| `setup/GEN_EXECUTION.md:285` | `service-availability-v1` | "Confluence and Snowflake are confirmed live (`Evals/ENVIRONMENT.md`, `service-availability-v1`)" |
| `setup/GEN_EXECUTION.md:408-411` | Paired eval file names + `all_failing.md`, `scoring.json` | "Open the paired Eval file (`Evals/0_Injection_Quality_Eval.md`, …)" |
| `setup/GEN_EXECUTION.md:414` | `*_qc_cases.json` / `*_qc_examples.md` | "a reviewer case in … that looks similar" |
| `setup/GEN_EXECUTION.md:234` | `Evals/references/rules/long_horizon.md` | "the Evals anti-inflation check" |
| `skills/create-rubric-writing/SKILL.md:3` | `hg-strict-overrides-v1`, "QC Spec V2 dimension thresholds" | "using /rubric's issue types, severities (hg-strict-overrides-v1)" |
| `playbooks/09_Rubric_Writing.md:50` | `3_Rubrics_Eval.md`, `hg-strict-overrides-v1`, `qc_rubric_v10.md`, `coherent_record.md`, `rubric_sampling.md`, `rubric_factual_checks.md` | "the `hg-strict-overrides-v1` table — stricter than the Docs and applied by `/rubric`" |
| `playbooks/09_Rubric_Writing.md:67,71,200,235-236` | `hg-strict-overrides-v1` | "Under the Evals overrides, a **prohibition-only or absence-only** acceptance always fails" |
| `playbooks/09_Rubric_Writing.md:212` | `/rubric` severity taxonomy | "`overly_broad` \| Moderate \| A plausible wrong answer passes" — **now Major** (`3_Rubrics_Eval.md:38`, 2026-10-17) |
| `playbooks/09_Rubric_Writing.md:219-227` | "Dimension (QC Spec V2 + Evals)" bands | "Major > 10%, or Major+Moderate > 15% … = FAIL" — superseded by `rubric-flow-v2` non-fail bands |
| `playbooks/09_Rubric_Writing.md:15,50,75,200` | `qc_rubric_v10.md` | "controls do not waive atomicity (`qc_rubric_v10.md`)" |
| `playbooks/04_Prompt_Writing.md:201,207,216` | `prompt-incorporation-v1`, Eval 1 §s | "| C8 | Incorporation (`prompt-incorporation-v1`) …" |
| `playbooks/04_Prompt_Writing.md:31,61,67` | QC Spec V2 CSV, `scoring.json`, `task_categories.md` | "the Prompt rows of the QC Spec V2 CSV" |
| `playbooks/04_Prompt_Writing.md:252-256` | `1_Prompt_Eval.md` Phases 1–3, `prompt_qc_cases.json` | "Walk `Evals/1_Prompt_Eval.md` Phases 1–3 in order" |
| `playbooks/08_Oracle_Event_Writing.md:56` | `2_Oracle_Events_Eval.md`, `oracle_events.md`, `oracle_events_qc_*` | "historical labels, V12 era: every flag scored Non-Fail 3" |
| `playbooks/08_Oracle_Event_Writing.md:74` | `service-availability-v1`, `Evals/ENVIRONMENT.md` | "Confluence and Snowflake confirmed live" |
| `playbooks/01a_Hardening.md:43,69,304` | `1B_Haiku_Prediction_Eval.md`, `1A_Hardness_Eval.md` | "apply the `Evals/1B_Haiku_Prediction_Eval.md` transfer checks" |
| `playbooks/11_AllFail_Analysis.md:3,10,98,101,157` | `all_failing.md`, `coherent_record.md` | "the four classes of `all_failing.md`, plus unresolved" |
| `playbooks/11_AllFail_Analysis.md:78` | `prompt-incorporation-v1`, `Evals/WORKFLOW.md` | "incorporates (`prompt-incorporation-v1`, `Evals/WORKFLOW.md`)" |
| `playbooks/12_Difficulty.md:70,76-77,147` | `scoring.json`, `long_horizon.md`, QC Spec CSV | "`scoring.json`: 'score only valid rubrics'" |
| `playbooks/03_Error_Async_Config.md:18-20,83` | `1_Prompt_Eval.md` §1.5, `long_horizon.md`, `scoring.json`, `Evals/WORKFLOW.md` | "the complexity hard gate counts only Ambiguity, Dynamic Change and Multi-Source" |
| `playbooks/02_Reference_Files.md:60,93` | `prompt-incorporation-v1`, `Evals/WORKFLOW.md` | "A rule or instruction inside a file becomes a requirement only if …" |
| `playbooks/01_Scenario_Design.md:122,151,162-164,462-463` | `task_categories.md`, `hardness_calibration.md`, `1_Prompt_Eval.md` §2.1/§2.2/§3.2, `0_Injection_Quality_Eval.md` Check C | "Do not reuse the ML-selected example … the calibration tasks" |
| `playbooks/01_Universe_Injection.md:277,311,318-321` | `0_Injection_Quality_Eval.md` Checks A–C, `injection-static-v2`, QC Spec V2 | "Walk `Evals/0_Injection_Quality_Eval.md` Checks A–C in order" |
| `references/Ask_Carriers.md:118,164` | `Evals/references/persona/acl.md` (2026-09-27, "citing QC Rating Form V12"), `service-availability-v1` | "[V] `Evals/references/persona/acl.md` (2026-09-27, citing QC Rating Form V12)" |
| `references/Hardness_Mastery.md:21-22,398,512,661,665` | rules dir files, `prompt-incorporation-v1`, `service-availability-v1`, `scoring.json`, "Evals rubric overrides" | "`prompt-incorporation-v1` (Evals/WORKFLOW.md)" |
| `references/Universe_Brief.md:55-56` | `service-availability-v1`, `Evals/ENVIRONMENT.md` | "confirmed live and unscoped" |
| `tools/difficulty_stats.py:13-35,462-464,955-989` | "QC Spec V2 and Evals `references/rules/scoring.json`"; legacy `<75%` gate | "Avg weighted pass: < 75% gate (Evals scoring.json; QC Spec V2 alone allows < 90%)" |
| `tools/gradable_surface.py:34,130` | QC Spec V2 weights | "weight by kind of work, 1/3/5 … (09_Rubric_Writing gate 8)" |
| `tools/stage_gate.py:1568` | `qc_rubric_v10` | "controls do not waive atomicity (qc_rubric_v10)" |
| `tools/hg.py:44` | `Evals/references/rules/scoring.json` | `"legacy_reference": "Evals/references/rules/scoring.json; superseded topics do not override V3"` |
| `references/Taxonomy_V2_Step_Map.md:78` | `scoring.json` (<75%, SD 0.1–0.3) | "design to the strictest" |
| `references/Persona_Briefs.md:8` + `references/Docs/4_Persona ACL Policy - V2.md` | ACL policy version V2 | Persona read rules; new bundle keeps V12 form + `service-availability-v1` |
| `learnings:216` | `base-data-v1` (Eval 1 Phase 3.2) | "injection SQL can't edit Confluence (Eval 1 Phase 3.2, base-data-v1)" |

Overlap with `references/Docs/*.md`: `11_V3_Changes.md` (cited as authority at `GEN_EXECUTION:23-25`, `README:8`, `v3_policy.json:4`) and `12_V3_Quiz_Answers.md` (not cited anywhere in scope) restate the same V3 rules the Eval bundle now versions separately; `11_V3_Changes.md:176,287` discuss shutdown framing and the "shutdown backdrop" prompt count, which now splits by universe. `QC_Spec_Doc_Latest.csv` (@ `04:31`, `09:50`, `08:55`) is the docs-side copy of the QC bands that `3_Rubrics_Eval.md` overrides.

## 5. Evals helper / review-skill invocations

| file:line | command | args |
|---|---|---|
| `tools/hg.py:30-31` | `hg.py` → `hg_search.py`, `hg_records.py`, `hg_reference.py`, `hg_context.py` | dispatch table; patched copies only |
| `setup/GEN_EXECUTION.md:250-260` | `hg.py search` | `inventory`, `files <svc>`, `search <svc> "<q>" [--file F --pointer P --limit N]`, `get <svc> --file`, `get-many --request`, `search-many --request`, `lookup <svc> --ids-file F --file GLOB`, `records --request`, `reference routes <svc>` |
| `setup/GEN_EXECUTION.md:244-247` | forbidden | "Running `Evals/tools/hg_*.py` directly writes into `Evals/` and breaks § 1" |
| `setup/local_search.py:34` | excluded helpers | `SKIP = {"hg_store_input.py", "hg_write_output.py", "hg_preflight.py"}` |
| `setup/GEN_EXECUTION.md:12-13,106-109` | `/injection`, `/prompt`, `/hardness`, `/oe`, `/rubric` | "remain user-run Portal steps"; "the eval commands are not run from this bundle" |
| `setup/GEN_EXECUTION.md:530-536` | supply lists per review | `/injection` SQL only; `/prompt` prompt + 8 fields + SQL + config + files; `/hardness` + trajectory JSON; `/oe` + OEs; `/rubric` + rubric JSON |
| `skills/*/SKILL.md` Deliver sections | `/prompt`, `/injection`, `/oe`, `/rubric`, `/hardness` | e.g. `create-prompt-writing:41` "then `/injection` + `/prompt` as a pair"; `create-rubric-writing:41` "then `/rubric`"; `create-oe-writing:39` "then `/oe`" |
| `playbooks/01_Universe_Injection.md:227` | `tools/judgment_probe.py` | "when it exists" — no such file in `tools/` |
| `tools/test_task_context.py:193-199` | reads `Evals/tools/*.py` | `hg_search`, `hg_records`, `hg_reference`, `hg_compact_index` |
| `tools/hg.py:44` | `hg.py context <stage>` | prints context + `v3_policy.json` + "legacy_reference" |
| (absent) | `hg_universe.py`, `hg_injection_lint.py`, `hg_injection_gate.py`, `hg_preflight.py`, `hg_prompt_ugt.py`, `hg_oe_review.py`, `hg_rubric_*.py` | no caller anywhere in `Task_Authoring/` |

## 6. Locally duplicated eval logic

| local construct | duplicates | divergence risk |
|---|---|---|
| `tools/sql_lint.py` (647 lines) | new `Evals/tools/hg_injection_lint.py` (checks: `future_date`, `id_contract`, `drive_unreadable`, `duplicate_account`, `actor_name`, `unknown_actor`, `grader_language`, `padding_comment`, `generated_column`, `text_time_format`, `missing_required`) | Different schema of record: `references/universe_schema_live.json` (144 tables, export 2026-10-04) vs `Evals/references/schema/injection.json` (58 tables) + `id_contracts.json`; different clock source (module `CLOCK` vs `hg_universe.clock`); different ID-contract coverage. |
| `tools/base_check.py` | `/injection` Checks A + C (`base_check.py:2-6` "mirrors `/injection` Checks A and C") | New bundle's static checks live in `hg_injection_lint.py` + `hg_injection_gate.py` (which gates a *saved* injection reviewed by `/injection`); local tool re-derives the rules from the base. |
| `tools/hardness_gate.py` | runs `sql_lint` + `base_check` and re-checks the manifest against SQL | Inherits both divergences above; adds its own thresholds (`GEN_EXECUTION §3a`), which are local policy, not Evals. |
| `tools/fact_check.py` | fact/leak discipline inside the SQL | Uses `base_check.CLOCK` and roster names; no Evals counterpart. |
| `tools/persona_view.py` | `Evals/references/persona/acl.md` (`persona_view.py:22` "authority: Evals/references/persona/acl.md") | Re-implements ACL; `ROSTER_V1` path and Feb `CLOCK`; new bundle keeps `acl.md` but the roster/date are per-universe. |
| `tools/difficulty_stats.py` | QC Spec V2 + `scoring.json` gates | Carries **legacy** `<75%` and SD gates beside V3 caps (`:13-35,462-464`), so a run can be judged against a superseded threshold. |
| `tools/stage_gate.py` (3,231 lines) | `/injection`, `/prompt`, `/oe`, `/rubric`, PD/QC rules | Re-states rule text (e.g. `:1568` `qc_rubric_v10` atomicity); drift is silent because the gate is local and blocking. |
| `tools/difficulty_mutation.py`, `gradable_surface.py`, `oracle_kit.py`, `trap_liveness.py`, `hardness_forecast.py`, `preflight_report.py`, `node_verdicts.py`, `surface_grader.py`, `trajectory_ledger.py` | model-owned local machinery (no Evals counterpart) | They encode `GEN_EXECUTION §3a` targets and the V3 caps; a change to the eval's numbers requires editing all of them. |
| `playbooks/04_Prompt_Writing.md` C1–C24 table | `Evals/1_Prompt_Eval.md` | 24 checks with §-citations (`§2.1`–`§3.2`); the new file's section numbering has shifted (e.g. `1.2 Naturalness` now at 2_Prompt `:406`), so the citations drift even where the rule is unchanged. |
| `playbooks/09_Rubric_Writing.md` severity + dimension tables | `3_Rubrics_Eval.md` + `hg-strict-overrides-v1` + `qc_rubric_v10` | Already stale: `overly_broad` Moderate→Major; quality bands replaced by `rubric-flow-v2`; negative-criteria wording extended to "any row an agent passes by doing nothing". |
| `playbooks/08_Oracle_Event_Writing.md` | `2_Oracle_Events_Eval.md` + `oracle_events.md` | Local severity labels must track the new `/oe` phases. |
| `references/universe_kb/_build/*` | rebuilds KB from the selected manifest | `common.py:40-41` hard-codes `Evals/references/search_indexes/snowflake-snowflake.json` and `HarmonyGames_Other_Services/metadata`; `OUT` may be `kb_output_path` (missing `by_date/2025-10-01`). |

## 7. Assignment inputs (00_Assigments.md template)

`references/Tasks_Template/00_Assigments.md` is copied into `task_inputs/` (`README.md:69`) and is the only assignment intake.

| element | template lines | notes |
|---|---|---|
| Platform block (user-supplied) | `:10-32` | Seven emoji groups / eight fields. `📅 Universe Date` at `:30-31`: "[Universe date exactly as displayed, including its time]". **This is the only date field that exists.** |
| Eight assigned fields | `:43-53` | `business_function`, `persona_name`, `persona_role`, `competency`, `task_skill`, `task_type`, `difficulty_mode`, `universe_date` (plus `horizon` mirror). |
| Derived mirror | `:54-58` | `universe_date_key: [2025-10-01 \| 2026-02-14]`, `freeze_utc`, `persona_key`, `email`, `department`. `task_context.py:95-101` reads `freeze_utc`/`universe_date_key` as metadata and `:234-236` rejects a value that disagrees with `v3_policy.json` — so supplying the correct `2025-10-01T07:00:00Z` would raise `"Stale assignment mirror freeze_utc"`. |
| Freeze mapping | `:78-80` | Hard-coded `0:00 UTC` mapping for both dates. |
| "Both dates one universe" | `:81-84` | "Both V3 dates use the supplied shared universe." |
| Difficulty / horizon / runs | `:85-96` | Caps, 50/100 calls, Opus 5.5, 5-of-6. |
| Non-required metadata | `:67-70` | Task ID, attempt, version, env, snapshot, specializations, category — intentionally not inputs. |

**Is there a date/universe field?** A date is present (`universe_date`, `universe_date_key`, `freeze_utc`), but it is the platform's displayed text plus a hard-coded table: there is **no universe selector, no `universe` saved input, no default, and no `hg_store_input.py` call**. The new bundle's required intake (`Eval-new/Evals/INPUTS.md:14-37`: ask "Oct 1, 2025 (synth-cut) or Feb 14, 2026 (normal)?", save with `hg_store_input.py universe <answer>`, never infer from prompt/SQL/data/task ID, no fallback to Feb 14) has no counterpart here.

## 8. Data products built from the old universe

| product | built from | evidence |
|---|---|---|
| `references/universe_sources.json` | one manifest for both dates; `verification_basis` quotes a user statement | `:3,6-7,10,13-14,17` |
| `references/universe_kb/*` (activity, coherence_hazards, cohorts, conventions, entities, integrations, timeline, trap_catalog) | `Evals/references/universe_manifest.json` (hg4-2026-08-31, `evaluation_clock 2026-02-14 00:00`) + the three root `HarmonyGames_*` folders; rebuild entry `_build/run_all.py` | `_meta.clock = 2026-02-14T00:00:00Z` in `activity.json`, `coherence_hazards.json`, `timeline.json`, `trap_catalog.json`; `entities.json` `2026-02-14T00:00:00+00:00`; `timeline.md:1` "clock 2026-02-14"; `_build/common.py:20-25,40-41` |
| `references/universe_kb/by_date/2025-10-01` | declared output for the Oct date (`universe_sources.json:9`) | **does not exist**; only the Feb build is present |
| `references/universe_schema_live.json` | platform DB export 2026-10-04 via `setup/extract_schema.sql` (144 tables) | `GEN_EXECUTION.md:271`; `sql_lint.py:20-22,45-47`; `README.md:133,183` |
| `references/persona_roster_v2.json` | Taxonomy 19; 17 copied from `Evals/references/persona/roster.json` on 2026-10-03, plus `thomas` and `tim_steudler` from `contacts.json` | `:2-4` ("thomas and tim_steudler are not yet in the Evals roster") |
| `references/v3_policy.json` | `Docs/11_V3_Changes.md`; freeze table, caps, model, timezone | `:3-13`; Oct freeze 00:00Z (wrong) |
| `references/mechanism_priors.json` | `support/hardness_ledger/ledger.jsonl` (sha256 bound); model `claude-opus-4-8`; UNCALIBRATED | `:2-12` |
| `references/{Scenario_Atlas,Persona_Briefs,Universe_Brief,Ask_Carriers,Hardness_Mastery,Native_Artifact_Anatomy}.md` | Feb-2026 exports; re-verified 2026-10-03/04; Confluence/Snowflake "being regenerated" | `Scenario_Atlas.md:10`; `Ask_Carriers.md:3,13-23`; `Hardness_Mastery.md:14`; `Persona_Briefs.md:12`; `Native_Artifact_Anatomy.md:4` |

**Consequence:** every one of these must either be rebuilt per universe (normal from `hg4-2026-08-31` v37; synthcut from `hg4-synth-sep30cut` v16, per `Eval-new/Evals/UNIVERSE_MAP.md` and `hg_universe.py:19-31`) or be split into a `normal/` and `synthcut/` variant. The Feb product cannot be "filtered" to Oct 1: the six missing storylines, the Feb-11 shutdown, the Feb-11 terminations and the "17 usable personas" assumption differ in kind, not only in date.
