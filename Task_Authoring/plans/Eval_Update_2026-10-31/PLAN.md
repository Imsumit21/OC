# Eval bundle update (2026-10-31): replace `Evals/` + `claude/`, align `Task_Authoring/`

Source of the new bundle: `Eval-new/` (user-supplied). Analysis reports in this folder:
`A_stage_docs_changes.md` (A-01…A-34), `B_references_rules_changes.md` (B-01…B-25),
`C_tools_changes_and_TA_impact.md` (C-01…C-24, breakage table, seam design),
`D_authoring_dependency_inventory.md` (routing map, every Task_Authoring dependency).
Change IDs below refer to those reports.

## 0. Status

| Step | State | Evidence |
|---|---|---|
| Backup of old `Evals/` + `claude/` | not kept (user decision) | the previous bundle remains only in git history |
| Replace `Evals/` and `claude/` with `Eval-new/` | done | `rsync --delete`, `task_inputs/` and `.cache/` excluded; `diff -rq` = identical; `Evals/task_inputs` byte-identical |
| New Evals unit suite in place | done | `Ran 799 tests … OK (skipped=5)` |
| Task_Authoring alignment | done | §7 (outcome, evidence, follow-ups) |
| Universe data installed (`Universe_Normal/`, `Universe_SynthCut/`) | done | `verify_universe_data.py --sha256`: ALL OK, 13/13 services per universe (§8) |
| Per-universe KBs built, `bound`, deterministic | done | rebuilds identical across Python hash seeds; both real tasks `bound` (§8) |
| Contributor handoff docs | done | root `README.md`, `Guide/00_Start_Here.md`, GEN_EXECUTION § 0a |

## 1. What changed (one screen)

1. **Two universes, chosen by task date, no default** (A-01, A-02, B-01, C-01). Feb 14, 2026 → `normal`
   (`Universe_Normal/Normal_HarmonyGames_*`, hg4-2026-08-31 v37, clock 2026-02-14 00:00 UTC, shutdown
   rules apply). Oct 1, 2025 → `synthcut` (`Universe_SynthCut/SynthCut_HarmonyGames_*`, hg4-synth-sep30cut
   v16, clock 2025-10-01 00:00 PT = 07:00 UTC; no shutdown; Victor Barnes departed Apr 2025; nothing after
   2025-09-30 23:59:59 PT, six storylines absent: Combo Fighter, Zombie Match Lite, Telegram Domino
   Delights port, UI sprite optimization sprint, Mattel Barbie idle life sim pitch, web distribution
   partnership). Per-universe references moved to `Evals/references/universes/<key>/`.
2. **Dates** (A-04, B-13): persona text in Pacific time; "today" is the universe date (Sat Feb 14, 2026 /
   Wed Oct 1, 2025); date rows accept the PT or UTC day when they differ (`pt_or_utc_date`).
3. **Injection** (A-05…A-11, B-04…B-07, B-19, C-24): event timestamps ≤ clock (only plan fields later);
   grader-facing text and padding comments FAIL; new mandatory static linter `hg_injection_lint.py`;
   Drive files must be readable; one account per person; `id_contracts.json`; generated FTS columns
   untouched; Linear text dates `YYYY-MM-DDTHH:MM:SSZ` / `YYYY-MM-DD`; `state_history_json` NOT NULL;
   Gmail/Slack attachments return no content.
4. **Prompt** (A-12…A-15, A-24, A-26, A-27, B-14…B-16, B-24): staged typos, trap hints/riddles, hidden
   destinations the persona knows, audit-form wording and if-chains each FAIL Contrived; clean writing is
   fine; premise checks per universe; voice judged against role only; `BOTH_FAIR_FIGURE` narrow UGT PASS.
5. **Oracle Events** (A-19, A-23, B-17, B-18): `expected_values` ledger — every value on an `Expected:`
   line quoted from a cited record (call site, not declaration); absence claims need a scoped check;
   two-way rubric↔OE cross-check.
6. **Rubric** (A-16…A-22, A-25, A-32, A-33, B-09…B-13, C-12…C-16, C-22): `overly_broad` Moderate→**Major**;
   do-nothing test (no "leaves X open" rows); format-5 record (`valid_case`, `do_nothing_case`,
   `final_reply_test`, `reachability`, `oe_cross_check`); format locks over-specific; LITERAL binding of
   keys/IDs/anonymized tokens; narrow NON-FAIL bands restored; rubric lint gains 4 families.
7. **Release/report** (A-28, A-31, B-25, C-09…C-11): release `task-quality-v1`; every verdict block
   carries a `Clock:` line; old records/ledgers are not reusable.

## 2. Decisions

**D1 — Universe source on the authoring side.** The assignment's `universe_date_key` (user-pasted platform
field in `00_Assigments.md`) selects the universe: `2026-02-14` → `normal`, `2025-10-01` → `synthcut`.
Missing or unrecognised → stop and ask (no default). The key→date/folder/clock/label/shutdown table is
read from `Evals/tools/hg_universe.py` (`UNIVERSES`), never duplicated; a test pins the registry to it.
Rationale: the date is an explicit user input, not an inference; one source of truth.

**D2 — Seam into the copied eval helpers.** Every copied helper now resolves the universe through
`hg_universe.selected(ROOT)`, whose `INDEX` literal points at the eval bundle's
`Evals/task_inputs/inputs.json` (C §4). Fix: `local_search.patched()` rewrites that single `INDEX` anchor
to a Task_Authoring-owned index under the active context (`<LOCAL>/universe/inputs.json`), and `build()`
writes that index + `02_Universe_Date.txt` in the exact `hg_store_input` format from
`TASK_AUTHORING_UNIVERSE` (and deletes it when unset). Upstream `selected()` validation (state, SHA-256,
parse) is reused unchanged. Every patch anchor is **required**: if an expected literal is absent, `build()`
exits non-zero (closes the silent-failure class that killed `TASK_AUTHORING_UNIVERSE_MANIFEST`). The dead
manifest override is removed. A guard rejects any remaining `Evals/task_inputs` literal in the modules
`hg.py` can execute. Never fall back to the eval bundle's saved inputs.

**D3 — The Oct 1 clock conflict.** `references/Docs/11_V3_Changes.md` §3: "Both freeze times are at
00:00 UTC" (Oct 1 = Tue Sep 30 5 PM PT). New bundle: synth-cut clock 2025-10-01 00:00 PT = 07:00 UTC.
GEN_EXECUTION's standing rule is "apply the stricter rule where sources differ", so:
- `freeze_utc` stays the V3 value (2025-10-01T00:00:00Z / 2026-02-14T00:00:00Z) and is the **seed bound**:
  no seeded event timestamp after it; nothing after it treated as completed. This satisfies both sources.
- `universe.clock_utc` (eval clock, 07:00Z for synth-cut) is recorded beside it and used for the eval's
  `Clock:` line and for reading the base data's coverage.
- The persona's "today" is the universe date (Wed Oct 1, 2025 / Sat Feb 14, 2026) — both sources and
  `learnings` §20 agree.
- Base records in the 7-hour window (00:00Z–07:00Z Oct 1) exist in the synth-cut data but are after the
  V3 freeze: do not rely on them as completed facts.
Flagged for the user in the final report; changing it later is a one-line policy edit + tests.

**D4 — Data folders.** Source paths come only from the selected universe manifest
(`Evals/references/universes/<key>/universe_manifest.json`). The new data folders are absent locally, so
`--require-source` must fail loudly (`SOURCE BLOCKED … Universe_Normal/… missing`). No silent fallback to
the old root `HarmonyGames_*` folders in V3 mode (legacy V2 self-tests may keep their fixtures).

**D5 — Universe KB.** `references/universe_kb/` was built from the old Feb data. Until a per-universe build
exists (`universe_kb/by_universe/<key>/`, needs the new data), the existing KB is served as a
**reference-only view** for both universes (existing `_reference_view` mechanism: verify every fact against
records; facts after the seed bound dropped), never as authoritative. A KB whose `source_fingerprint`
matches the selected universe is served normally. Remove the hard-coded `"2026-02-14"` exemption.

**D6 — Linters.** `create-injection` runs both: local `sql_lint.py` (+`base_check.py`) and the eval's
`hg_injection_lint.py` through `hg.py lint` (patched copy, task SQL, task universe). `sql_lint` must not
accept what the eval FAILs on the overlapping rules (Linear text-date format, generated columns).
`hg.py rubric-lint` exposes the eval's `hg_rubric_lint.py` for rubric drafts.

**D7 — Authority clause.** GEN_EXECUTION's authority paragraph changes from "local Evals are read-only
reference implementations whose older clock … overrides do not override V3" to: the Evals bundle
(`task-quality-v1`, `dual-universe-v1`) is what QC review runs; authoring must pass it; where it and V3
differ, apply the stricter (D3 is the known case).

**D8 — Stage-gate compatibility.** `stage_gate.py` parses playbook-defined artifacts. Content edits may add
fields/columns only where the gate tolerates them; any template change must keep
`Task_Authoring/tests/test_v3_stage_gate.py` and the stage-gate self-tests passing.

## 2b. Architecture review (oracle-gpt, GPT-6.1 Sol, 2026-10-31) — accepted changes

Verdict on the first draft: FAIL with changes; all accepted below. These supersede §2 where they differ.

- **D2+** Keep the guarded upstream copy (not a shim). `build()` recomputes LOCAL/TOOLS/cache paths on every
  call (no mutated globals); a universe index is published only inside a context dir (requires
  `TASK_AUTHORING_CONTEXT_HASH`; `TASK_AUTHORING_UNIVERSE` without a hash is an error; the default dir never
  holds one). Paths in the index are workspace-relative (`Task_Authoring/...`). Publication is atomic
  (temp + `os.replace`) and skips identical bytes. Required anchors also cover `hg_injection_lint.SAVED_SQL`
  and `hg_rubric_lint`'s default-input branch. The `Evals/task_inputs` guard is AST-based over code string
  constants (docstrings excluded) in the transitive import closure of every `hg.py` subcommand.
- **D3+** `freeze_utc` stays the V3 seed bound (writes and completed facts). New **data horizon** =
  `universe.clock_utc` (07:00Z on synth-cut): records up to it exist and the agent sees them, so a record in
  the 00:00Z–07:00Z window can supersede a "current/latest" answer. Authoring rule: if a window record
  touches an entity the answer depends on, avoid that dependency. Tools get `CLOCK` (seed bound) and
  `DATA_CLOCK` (data horizon); each `CLOCK` use is audited (writes → `CLOCK`, what-exists/visibility →
  `DATA_CLOCK`). The `Clock:` line is emitted exactly as `hg_universe.report_line(key)`.
- **D4+** Readiness at every base-read boundary: when the source is not ready, `_apply` points the data
  globals at a sentinel path (never the old/default roots, never the previous task's roots); root defaults
  only under explicit legacy execution; `ensure_active(require_source=True)` re-checks readiness even when
  the context hash is unchanged. Source validation checks manifest identity (`universe` field, folder =
  `hg_universe.base_folder`) and takes the clock from `hg_universe.UNIVERSES` (manifest `evaluation_clock`
  is human-readable text — never `fromisoformat` it).
- **D5+** Synth-cut gets **no** legacy KB until rebuilt (`kb_status: "unavailable"`, `kb_path: null`, which
  clears any previous binding): `_reference_view` leaves cohorts, traps (e.g. Combo Fighter), hazards and
  integrations intact, and gates/base checks use KB membership mechanically. Normal's old KB is
  `"reference-only"` advisory orientation, never validation authority. `"bound"` requires matching
  `_meta.universe`, `_meta.clock`, `_meta.source_fingerprint` and `_meta.build == "per-universe-v1"`.
- **D6+** `hg_injection_lint` exits 0 even with FAIL flags: consumers parse `counts.FAIL` and the flags.
  The injection stage gate runs `hg.py lint` (with base data) and blocks on any FAIL or any undispositioned
  CHECK. `sql_lint`'s seed-bound check covers at least the upstream `EVENT_FIELDS` (pinned by a test).
- **D7+** Authority: Evals owns the selected universe, its state and the evaluation clock; V3 additionally
  limits seeded/completed facts. "Stricter wins" applies only to comparable constraints.
- **D8+** `tools/stage_gate.py` joins the work (lint consumption, KB-status handling), as do the KB build
  scripts (`_build/assemble_hazards_traps.py`, `assemble_integrations_conventions.py`, `assemble_timeline.py`,
  `run_all.py`, `common.py`): normal-only hard-coded facts are emitted only for `normal`; every output is
  stamped with universe/clock/fingerprint/build provenance.
- Interface edits: `universe.source` → `universe.build_label`; `source.kb_status` ∈
  `bound | reference-only | unavailable` with nullable `kb_path`; `source.kb_output_path` per universe;
  `hg.py universe`, `rubric-lint` and `lint --no-base` run without installed exports.

## 3. Interfaces (fixed before work starts; amended by §2b)

Context (`Working_Files/00_Task_Context.json`, produced by `task_context.load_context`):
- unchanged: `universe_date_key`, `freeze_utc` (V3 seed bound), `source.paths`, `source.manifest`,
  `source.kb_path`, `context_hash`.
- `source.mode`: `"universe"` replaces `"shared-universe"` (`"snapshot"` kept); `source.universe`: key.
- new top-level `universe`: `{key, date, label, folder, prefix, clock_utc, clock_text, clock_line,
  shutdown_rules_apply, persona_today, persona_today_weekday, source}` (values from `hg_universe`).
- new `source.kb_status`: `"bound"` (KB fingerprint = selected universe) or `"reference-only"`.

Environment set by `runtime_context.activate`: `TASK_AUTHORING_TASK_DIR`, `TASK_AUTHORING_CONTEXT_HASH`
(existing), `TASK_AUTHORING_UNIVERSE=<normal|synthcut>` (new). `TASK_AUTHORING_UNIVERSE_MANIFEST` removed.

Commands (`Task_Authoring/tools/hg.py`):
- `hg.py universe [show|list]` — the active task's universe (patched `hg_universe.py`).
- `hg.py lint [--sql PATH] [--checks a,b] [--no-base] [--summary]` — eval `hg_injection_lint.py`;
  `--sql` defaults to `<task_dir>/01_Universe_Inject.sql`; `--no-base` works without universe data.
- `hg.py rubric-lint <rubric.json>` — eval `hg_rubric_lint.py`.
- `search | records | reference | context` unchanged, now universe-aware.

Canonical sentence for every skill's Inputs block and playbook Inputs paragraph (replaces "Both
(freeze) dates use the same local (universe) data"):
> The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14, 2026 → normal, Oct 1,
> 2025 → synth-cut. Read only that universe, apply its state rules and clock, and stop if the date is
> missing — there is no default.

## 4. Work packages (disjoint file ownership)

| WP | Owner | Files (only these) |
|---|---|---|
| T1 seam | general | `tools/task_context.py`, `tools/runtime_context.py`, `setup/local_search.py`, `tools/hg.py`, `references/universe_sources.json`, `tools/test_task_context.py`, new `tools/test_universe_seam.py` |
| T2 consumers | general | `tools/v3_artifact_checks.py`, `tools/entity.py`, `tools/hardness_forecast.py`, `tools/difficulty_mutation.py`, `tools/sql_lint.py`, `tools/shortcut_probe.py`, `tools/selftest_sandbox.py`, `references/universe_kb/_build/common.py`, `references/universe_kb/_build/test_v3_build_context.py`, `tests/test_v3_stage_gate.py` |
| C1 design side | general | playbooks `01_Scenario_Design`, `01_Universe_Injection`, `01a_Hardening`, `02_Reference_Files`, `03_Error_Async_Config`; skills `create-scenario`, `create-injection`, `create-hardening`, `create-reference-files`, `create-error-async` |
| C2 prompt/OE | general | playbooks `04_Prompt_Writing`, `05_Human_Time_Estimate`, `08_Oracle_Event_Writing`; skills `create-prompt-writing`, `create-humantime`, `create-oe-writing` |
| C3 rubric side | general | playbooks `09_Rubric_Writing`, `11_AllFail_Analysis`, `12_Difficulty`; skills `create-rubric-writing`, `create-allfail`, `create-difficulty` |
| C4a contract | general | `setup/GEN_EXECUTION.md`, `Guide/*.md`, `README.md` (Task_Authoring), `references/Tasks_Template/00_Assigments.md`, `references/Taxonomy_V2_Step_Map.md` |
| C4b references | general | `references/{Universe_Brief,Persona_Briefs,Scenario_Atlas,Ask_Carriers,Hardness_Mastery,Hardness_Manifest_Spec,Native_Artifact_Anatomy}.md` |
| Integration | build | full test runs, consistency greps, smoke runs, verification gates |

Per-stage content checklists (C1–C4) are in each agent brief and map 1:1 to the A/B/C IDs in §1.

## 5. Acceptance

- Evals suite: 799 tests OK. Task_Authoring suites (5 existing files, 81 tests at baseline) pass, plus the
  new seam tests (no fallback to `Evals/task_inputs`; required anchors; registry pinned to
  `hg_universe.UNIVERSES`; synth-cut/normal selection; `hg.py lint --no-base` flags a post-clock timestamp,
  an FTS column write and a `+00:00` Linear date).
- Smoke: `hg.py universe` prints `normal` for `task_inputs/` and `synthcut` for `task_inputs2/`;
  `task_context.py --require-source` prints `SOURCE BLOCKED … Universe_*` (data absent) — never a silent
  read of the old root folders.
- Greps return nothing outside history/legacy fixtures: "same local (universe) data", `shared-universe`
  in V3 paths, `Evals/references/universe_manifest.json`, `Evals/references/{search,id}_indexes`,
  `overly_broad` = Moderate, "preserved state … on its own row", "Leave in small typos".
- Gates: `verify` code + redteam + methodology on the final tree (eval path changed).

## 6. User-only follow-ups (cannot be done here)

1. ~~Install the new universe data~~ — done 2026-10-31 (§8).
2. ~~Rebuild the per-universe KB~~ — done; both `bound` (§8).
3. In-progress tasks: `task_inputs2/` (Oct 1) was authored on the old shared Feb data — re-validate it on
   synth-cut (post-cut storylines, Victor, shutdown premises, 7-hour window). `task_inputs/` (Feb 14) must
   be re-checked against v37 and the new rubric/OE/prompt rules.
4. Review side: `/injection`, `/prompt`, … now ask the task date first; answer with the assignment date.
   `Evals/task_inputs/` holds an Oct 1 task without a saved `universe` input.
5. Optional: delete `Eval-new/` after review (identical copy now lives in `Evals/` + `claude/`).
6. Upstream bundle note (not edited — vendor files): `Evals/references/persona/manifest.json` still pins the
   old `acl.md` SHA-256 (`19f0609…`); `prompt_rubric_release.json` pins the new one (`e9bca2b…`), and all 94
   release pins verify.

## 7. Outcome (2026-10-31)

**Content.** All 11 `skills/create-*/SKILL.md`, all 11 playbooks, `setup/GEN_EXECUTION.md` (new § 0a, authority
clause per D7+), `Guide/*`, `README.md`, `Tasks_Template/00_Assigments.md`, `Taxonomy_V2_Step_Map.md` and seven
reference docs follow `task-quality-v1` + `dual-universe-v1` (universe-first, seed bound vs data horizon, PT
dating, injection Checks A–C + eval lint, prompt Contrived classes, OE `expected_values` ledger, rubric
do-nothing/format-5/Overly Broad Major/new bands, Clock lines). Normal-only material in the reference docs is
tagged `[normal-only]`, not deleted.

**Tooling.** `task_context.py` (universe from the assignment date via `Evals/tools/hg_universe.py`, registry v2,
manifest identity, KB status), `runtime_context.py` (`CLOCK`/`DATA_CLOCK`, sentinel roots, readiness on every
path, per-file KB provenance, legacy refusal on V3 tasks), `local_search.py` (per-context index, required
anchors, blanket `Evals/task_inputs` redirect, context re-validation before publishing), `hg.py`
(`universe`, `lint`, `rubric-lint`; refuses eval-input paths), `stage_gate.py` (eval lint consumed per flag,
KB-status handling, record-only locators, Clock labels), `sql_lint.py` (upstream event fields, exact Linear
text dates, generated flags, ms/RFC-2822 times), `base_check.py`/`persona_view.py`/`fact_check.py`/`entity.py`/
`shortcut_probe.py`/`v3_artifact_checks.py`/`selftest_sandbox.py`, KB build scripts (per-universe output and
provenance stamping). Note: `tools/base_check.py` carried uncommitted user edits before this work; they are
preserved and its diff contains both.

**Evidence (final tree).** Evals suite 799 OK; Task_Authoring 121 tests OK (baseline 81): `test_v3_stage_gate`
41, `test_skill_registration` 13, `test_difficulty_v3` 13, `test_task_context` 27, `test_universe_seam` 14,
`test_v3_build_context` 13. All 20 tool self-tests ok; 3 live sub-checks print an explicit SKIP until the
universe data is installed. Smoke: `hg.py universe` → `normal` (task_inputs) / `synthcut` (task_inputs2);
`--require-source` → `SOURCE BLOCKED … Install Universe_*`; `hg.py lint --no-base` on a planted SQL → FAIL
flags `future_date`, `generated_column`, `missing_required`, `text_time_format`; no copied helper references
`Evals/task_inputs`; `Evals/` byte-identical to `Eval-new/` after every run.

**Independent review trail.** Architecture: oracle-gpt FAIL → §2b adopted. Code review (reviewer, GPT-6.1):
FAIL, 3 high + 4 medium → fixed with regressions. Red team (GPT-6.1): FAIL, C1–C5 broken → fixed with
regressions. Re-review and `verify` gates: see the final report.

**Rollback.** No backup of the old bundle is kept (user decision); git history still holds it
(`git checkout -- Evals claude` would restore it). Task_Authoring changes are ordinary uncommitted edits
(keep the user's pre-existing `base_check.py` edits in mind).

## 8. Data install, KB rebuild and evidence round (2026-10-31 → 2026-11-01)

**Data.** The user installed both universes; the Finder-split Normal GitHub export (`… 2`, `… 3`) was merged
(0 conflicts) and the three Normal bases moved into `Universe_Normal/`. `tools/verify_universe_data.py` (new,
read-only) checks every service folder against its `source_manifest.json` (presence, sizes, SHA-256 with
`--sha256`, regular files only, Unicode spellings never merged) and each source manifest against the Evals
routing manifest's pins (file count, bytes, archive SHA-256 and entry): ALL OK for 13/13 services in both
universes, with full hashing.

**Fixes.** Legacy V2 self-tests read the Feb 14 data from `Universe_Normal/` once the old root folders are
gone (`task_context.v2_export_root`); data drift in the persona facts (Marcus Bennett now has the mailbox
`marcus.bennett@…` in both universes; trap P02/P03 text) corrected in `Ask_Carriers.md`, the self-tests and the
KB generator; KB determinism: `_build/pass_other.py` iterated sets of email strings (order and the three ids
kept followed the per-process hash seed), now sorted; the assignment parser no longer lets a label with a
deleted value capture the next heading; `--help` exits 0 for `hg.py` and `base_check.py`; tests no longer depend
on the live task folder or scratch files. The synth-cut KB no longer carries Feb 14 evidence: hand-written
(`Scenario_Atlas`) rows are emitted there only when every id they cite resolves in the synth-cut exports, and
storyline beats that the data's own metadata flags with an editorial note are left out (both listed in `_meta`).
The source fingerprint and the KB stamp are machine-independent (workspace-relative manifest path, no context
hash, no absolute paths), so the committed KBs stay `bound` on a clone with the same data.

**Evidence.**
- Determinism: 68 files (both KBs and the `kb_cache` intermediates) byte-identical across Python hash seeds
  101/202 and 303/404, and 72 after the leakage fix (505/606 vs 707/808). After the stamp change the final
  build equals the previous one in all 28 KB files across seeds 707/808 vs 909/1010, the only difference being
  the removed `_meta.context_hash` (Python 3.15.0, macOS 25.6; `entity.py --task-dir <t> build`, then
  `_build/run_all.py --task-dir <t>`). Both real tasks resolve `kb_status: bound` (normal fingerprint
  `56f200f90f8a`, synth-cut `35ef23cdb4f6`); the KB files contain no machine paths.
- Access audit (a `sys.addaudithook` hook in every Python process of the run): both KB builds, 18 read-side
  commands per universe on scratch tasks, and the isolation probes made 0 writes to `Evals/`, `claude/`,
  `Eval-new/`, `Universe_*`, task folders or the legacy KB root; opened 0 files under `Evals/task_inputs`; touched
  0 files of the other universe or its KB; each build wrote only its own `by_universe/<key>/` (23 files).
- Isolation: one interpreter switching normal → synth-cut → normal re-binds roots, caches, clocks and KB (the
  in-memory KB cache is emptied on each switch); two tasks with the same assignment share a cache folder but
  not seeded rows (a row whose channel exists only in task A's SQL is unresolved in task B); a forged saved
  context (a normal context saved in a synth-cut task) is ignored.
- Clock: a synth-cut cited record or completed fact between 00:00Z and 07:00Z is rejected (offset spellings
  too), at or before 00:00Z accepted; a seeded row in that window passes the eval lint but fails the gate's
  `sql_lint` re-run (regression tests in `tests/test_v3_stage_gate.py`).
- Leakage (synth-cut KB against the normal KB as control): the six post-cut storylines and the shutdown
  premises occur 0 times (e.g. Combo Fighter 0 vs 249, Telegram 0 vs 17, Mattel 0 vs 20, `2026-02-11` 0 vs 103);
  the only 2026 dates left are one scheduled board meeting that exists in the synth-cut calendar. The audit
  found Feb 14 evidence reaching synth-cut through hand-written hazard/trap rows and four flagged beats; after
  the fix, hazards S05–S07, Q06–Q08, L14 and traps D08, C04, X03 are not emitted on synth-cut, the four beats are
  excluded, and the 15 leaked ids/strings occur 0 times in the synth-cut KB (all still present in the normal
  one). The audit is lexical plus id resolution, not a semantic review of every entry.
- Tests: Evals 799 OK; Task_Authoring 149 OK (`test_v3_stage_gate` 45, `test_skill_registration` 13,
  `test_difficulty_v3` 13, `test_task_context` 29, `test_universe_seam` 33, `test_v3_build_context` 16); all
  tool self-tests ok, sandboxed.

**Vendor note (not edited).** `Evals/tools/tests/test_hg_compact_index.py`
`PortableTests.test_source_change_during_import` patches `content_sha256` with a function that rewrites every
file it hashes (`needle` → `change`); the helper signature hashes the real `Evals/tools` helpers, so running the
vendor suite truncates and rewrites them in place. The bytes stay identical only because those files contain
no `needle`. Report upstream; run the vendor suite only on a tree you can restore.

**Open items for the user.** (1) The saved `Working_Files/00_Task_Context.json` in `task_inputs/` predates the
KB rebuild (`kb_status: reference-only`); tools recompute the context on every run, but refresh the record with
`task_context.py --write` when convenient. (2) The per-universe KBs are committed. New
`support/local_search/contexts/` folders are now ignored, but the ~1,660 context files committed earlier stay
tracked until someone untracks them (`git rm -r --cached Task_Authoring/support/local_search/contexts`), a
separate decision. (3) `Eval-new/` (the supplied bundle) is removed once this work is committed; git history
is the record of both bundles.
