# Fix session 2026-10-25: running log

Task: `plans/Implementation_Session_Prompt_Fixes.md` (P0, the move, P1). Labels: [O] observed, [D] derived, [I] inference.
Season Pass backtests are development fixtures, not validation.

## Conventions
- Logs, evidence and fingerprints: this folder (`support/fix_session_2026-10-25/`).
- Scratch root for every self-test temp folder and sandbox: `support/scratch/` (tempfile.mkdtemp(dir=...), unique per
  run, removed afterwards). Never the system temp folder.
- Fingerprint exclusions (never walked): `support/archive/` (read-only records, 5.7 GB), `support/scratch/` (scratch
  root), `support/fix_session_2026-10-25/` (this log folder). `task_inputs/` is included, so a write there would show;
  a parallel session (task 1 design) may write there, and its changes are reported, never treated as mine.
- Tool: `scripts/fingerprint.py OUT.tsv [--only REL ...]`, `--diff A B [--only ...]`.

## Log
- 16:38:45 IST: baseline fingerprint `logs/fp_00_baseline.tsv`, 19,816 entries [O].
- Frozen copies verified before use: rev13 `shasum -a 256 -c SHA256SUMS` 243/243 OK; rev14 254/254 OK [O].
- `apply_pending.py` check-only: "ready: 21 staged file(s) to copy, 10 tool(s) to move into tools/", exit 0 [O].
- Gate-policy hash of live `tools/*.py`: 17 files, `4459b8bdd4de` [O].

### B1 (apply_pending.py, staged in pending_edits/)
- Rewritten: backup to `.rollback/<ts>/` (verified), fsync'd journal before/after every step, tools copied (deleted from
  pending_tools only after every copy), `--resume`, `--rollback [TS] [--force]` (removes new targets, created folders,
  generated files; restores pending_tools), `--check` reports ready / already applied / partially applied.
- MANIFEST: `"generated": ["references/mechanism_priors.json"]`.
- `--self-test`: 17 cases on scratch bundles under support/scratch/, real SIGKILLs at 5 apply points then --resume, at
  4 points then --rollback, mid-rollback kill, completed apply + generated file rolled back with policy hash restored,
  --force, already-applied with/without journal. PASS [O].
- `scripts/rehearse_move.py` (real MANIFEST on a scratch copy): kill at step 19 -> resume -> write-priors -> rollback;
  16 originals sha = base, 5 new files + mechanism_priors.json removed, 10 pending tools restored, policy
  5920233735ca -> 4459b8bdd4de. PASS [O] (`logs/b1_rehearsal_1.txt`). To be re-run on the final staged set.

### H3
- New pending tool `selftest_sandbox.py` (scratch root `support/scratch/`, `scratch_tmp()`, Sandbox: copies + linked
  read-only folders, sandbox-only local_search patch, path probe before each command, `find -newer` after).
- Staged stage_gate: SELFTEST_TMP = scratch root, mkdtemp per run, removed in finally; self-test reruns itself in a
  sandbox. Staged hardness_gate: same. Ledger/forecast self-tests: temp ledgers in scratch. All 8 other pending tools:
  scratch_tmp(). check_staged_stage_gate.py now runs the staged layout in a sandbox (`--suite` = every move self-test).
- MANIFEST after: `selftest_sandbox.py --suite move`, `write-priors` (L10 clean-up dropped: P2).
- Evidence [O]: staged suite (`logs/h3_suite_staged_1.txt`) 13/14 ok, hardness_gate failed on the symlink root check
  (an error, not a leak) -> local_search sandbox patch -> `hardness_gate --self-test` ok in the staged sandbox;
  shared fingerprint (support/local_search + support/hardness_ledger, 18,067 paths) 0 differences each time;
  planted rebuild (`logs/h3_planted_rebuild.txt`): persona_view, base_check and hg.py rebuilt inside the sandbox,
  find -newer 0, shared fingerprint 0 differences.
### B2
- trajectory_ledger: `revision_content` (keyed rows: INSERT ids / Slack channel-ts, UPDATE where), `binding()` with
  BOUND (basis discriminating content | sole revision) / AMBIGUOUS / INSUFFICIENT / UNBOUND and evidence counts,
  `binding_ok()` (the one owner of "certifies a revision"), `stored_revisions()`, `check_sole_revision()`,
  `--sole-revision REASON` (refused while another revision is stored, or without --task-dir).
- node_verdicts: `evaluate_runs()` always binds on evidence; a run that is not BOUND is recorded and never evaluated
  (no first-SQL fallback); proposals carry each run's own revision + sql_sha256; `--sole-revision`; compare reports an
  unevaluated reference run as a difference.
- Gate `revise.revision_binding` via `tl.binding_ok` (SINGLE / evidence-free BOUND / INSUFFICIENT need `historical`);
  hardness_forecast compare `every_run_bound` via `tl.binding_ok`.
- Fixtures: 7 BOUND bindings in staged cases.json now carry basis + evidence; +4 bad cases (SINGLE, BOUND without
  evidence, INSUFFICIENT not historical, sole revision without reason); +1 control (INSUFFICIENT marked historical).
- Docs (staged): 01_Universe_Injection S5e store `run_forensics/<rev>/01_Universe_Inject.sql`, Output list, S5f early
  runs in `run_forensics/<rev>/early/` + every stored revision; 01a MODE B + pre-check commands pass every stored
  revision, INSUFFICIENT stops the intake; 01_Scenario_Design S0r + gate 13; Guide §14.7 `$SQLS`; create-difficulty,
  create-injection, create-hardening SKILL; GEN_EXECUTION slot map + §6b revise row; stage_gate docstring.
- Evidence [O]: `logs/b2_acceptance.txt`: 7 rev13 runs vs [rev14] INSUFFICIENT; vs [rev14, rev13] INSUFFICIENT (subset
  case); 5 rev14 runs vs [rev14, rev13] BOUND rev14 on 111-112 needles; rev13 runs vs [rev13..rev10] BOUND rev13 on
  `f_ddbcc47ba64c9c00764727`. Criterion-5 re-run (`logs/b2/c05_rerun.txt`): all BOUND rev13, 0 differences from
  attribution.json, 70 proposals identical to the audit's except binding detail, each `rev13`/`fdfc7988`. CLI
  (`logs/b2/b2_cli.txt`): INSUFFICIENT exit 1; NOT EVALUATED exit 1; --sole-revision refused (rev13 stored) exit 2;
  allowed when only rev14 is stored, BOUND. Staged gate self-test 105 cases ok.

### D6 (decision: the V3 rubric rules block; geometry = difficulty figures, report-only)
- gradable_surface: FAMILY_BASIS (structure, weights, duplicates, sampling, exceptions, mechanisms), a `basis` on every
  finding; docstring; self-test 16 distinct planted checks covering all 6 families (+6 structure sub-checks that had
  none), meta-assert every family planted, 0 % mechanism share still PASS.
- Gate `surface.valid`: failing families printed with their basis; PASS detail states geometry report-only.
  Self-test case field `expect_detail`; +6 gate cases (slot_ids, duplicates.fact, sampling.limit, sampling.volume,
  exceptions.singled_out_by, mechanisms.known) + `expect_detail` on the weights case; +1 control (no mechanism: PASS).

### D3 (surface.coverage)
- Gate `surface.coverage` in rubric-writing (§G) and rubric-check ("Coverage — gradable surface"): covering row id or
  a reasoned disposition per slot; missing / neither / bare label / gap / stale slot block. Planted first: the good
  fixture without §G failed both rubric stages [O].
- Staged good fixture copies (2 new edited targets, MANIFEST base sha recorded): 09_Rubric_Writing_Plan.md (§G, §E
  line; own digest 1685f5279950 -> 42231d21cd87), 09_Rubric_Check.md (table; own digest 6c86c1af6201 -> c3be20bddac9).
  Informational digest mentions in 11_AF_Justification.md:29 and 13_Release_Gate.txt:22-23 left as they were (pasted
  gate lines: excluded from digests and never re-verified).
- +6 bad cases; staged self-test 118 cases ok [O].

### D5
- trap_liveness: rule placement only on A15 nodes (portfolio or trap mechanism id); otherwise SKIP with the reason
  per node and in the scope line (legacy manifest / no A15 in the portfolio / not an A15 node).
- Rev10 re-run (`logs/d5/`): before 14/17 flagged, FALSE 8/8, precision 0.571; after 13/17, FALSE 7/8 (T12 missed),
  precision 0.538 (base rate 0.471); rule placement SKIP 17/17 [O]. Criterion 8 (>= 6/8) still met.

### MK
- difficulty_mutation.resolve_max_k (one owner): default 8; above only with --allow-max-k N (same N), disclosed on
  stderr and as `max_k_override` in the JSON; otherwise UNSUPPORTED exit 2. Wired into difficulty_mutation,
  hardness_forecast (forecast, exhaustive) and preflight_report. Planted CLI refusals in each self-test [O].
- Note: the rev13 replay's recorded `--max-k 12` now needs `--allow-max-k 12` to re-run.

### P0 verification
- Direct self-tests of the 11 pending tools + apply_pending: all ok; shared fingerprint 0 differences
  (`logs/p0_direct_selftests.txt`) [O].
- Rehearsal on the final staged set (`logs/b1_rehearsal_2_final.txt`): 18 edited, 5 new, 11 tools; predicted
  post-move policy `0fb8083a2463` (28 files) = observed after resume; rollback back to `4459b8bdd4de` [O].
- Real check-only: "ready: 23 staged file(s) to copy, 11 tool(s) to copy into tools/" [O].
- Falsification (`scripts/falsify_p0.py`, `logs/p0_falsification.txt`): 13 fixes undone one at a time in a staged
  sandbox copy (B1 x3, B2 x3, H3 x2, D3, D5, D6 x2, MK): each one's self-test FAILS; the 8 unmodified controls PASS [O].
- Staged suite 17:33-17:37 (`logs/p0_suite_staged.txt`): all 14 move self-tests ok in the post-move layout
  (stage_gate 118 cases, hardness_gate, 11 tools, difficulty_stats, selftest_sandbox); 13 write paths asserted inside
  the sandbox before every command; find -newer on the linked folders empty after every command; shared fingerprint
  0 differences over 18,067 paths [O].
- Bundle fingerprint `logs/fp_01_p0_done.tsv` vs baseline: 33 differences (`logs/fp_diff_00_01_p0.txt`):
  29 mine (16 CHANGED + 2 ADDED in support/pending_edits/, 10 CHANGED + 1 ADDED in support/pending_tools/);
  4 NOT mine, changed 16:57-17:18 by the user or the parallel session: references/Hardness_Mastery.md,
  plans/V3_Opus55_Difficulty_Plan.md, plans/Learnings_And_Improvements_2026-10-25.md,
  plans/Hardness_Defeat_Plan_2026-10-25.md. task_inputs/: no difference.

## The move (maintenance window confirmed by the user; authoring + reviewer sessions paused)
- Attribution (user): the 4 files of 16:57-17:18 are the authoring session's (Learnings, V3 plan, Hardness_Mastery)
  and the reviewer's (Hardness_Defeat_Plan status line); 17:46-17:52 more authoring edits (Learnings, V3 plan, staged
  01_Scenario_Design S5a, 01_Universe_Injection S5f, 01a MODE B step 6).
- 18:00:34 baseline `logs/fp_10_premove.tsv` (19,819 entries); vs fp_01: 5 differences, exactly those edits [O].
- Check-only: "ready: 23 staged file(s) to copy, 11 tool(s) to copy into tools/" [O]. Predicted policy 0fb8083a2463.
- 18:01:00 `--apply`: "applied (20261025T123100Z_ao36cyhg): 23 staged file(s) and 11 tool(s) in place, each sha256
  verified" (`logs/mv_apply.txt`); LIVE policy `0fb8083a2463` (28 files) = rehearsal [O]. Check after: "already applied".
- After #1 `tools/selftest_sandbox.py --suite move` 18:01-18:03 (`logs/mv_suite_live.txt`): 14/14 ok from tools/
  (live layout); paths inside; linked folders unchanged; shared fingerprint 0 differences [O].
- After #2 `write-priors` -> references/mechanism_priors.json (claude-opus-4-8, 19 families). Pre-H2 A17:
  Beta(15, 17), mean 0.469, n_eff 30, 14 records (`logs/h2_A17_before.txt`, copy `logs/mechanism_priors.pre_H2.json`).
- 18:03:54 `logs/fp_11_postmove.tsv`; diff vs premove (`logs/fp_diff_10_11_move.txt`): 77 = 18 CHANGED targets +
  5 ADDED fixtures + 11 ADDED tools + 11 REMOVED pending tools + mechanism_priors.json + 31 .rollback files; nothing
  else [O]. `.rollback/20261025T123100Z_ao36cyhg/` kept until the re-audit.

## P1 (after the move: edits go into the live files; playbooks by targeted replacement only)
### V1 (one owner of model labels: difficulty_stats)
- difficulty_stats: `model_id` (strips only a bracketed suffix), `classify_model` (expected / other / synthetic /
  unknown, exact comparison), `is_opus_55`, `check_models`, `message_models`, `model_provenance` (mixed_model and
  v3_valid separate; off-model labels with source, count, events, fallback event before them); `model_gate` through
  `check_models` (UNKNOWN never valid). trajectory_ledger `provenance(..., expected_model)` adds `model_check` and
  `v3_valid` from the owner; `deciders()`; `expected_model_for(task_dir)` (context baseline_model, else the V3 policy
  model); `--expected-model`; V3-invalid and synthetic flags; `trajectory_models` from the loaded events (equal to
  the file read on 6 real runs [O]). stage_gate's release check and surface_grader's view choice use `check_models`.
- Planted: `difficulty_stats._self_test_models()` (the old prefix rule rejected `claude-opus-5-5[1m]`; synthetic
  alone is no model; an unrecognised label is UNKNOWN; a subagent off-model message flags the run; audit L4 with no
  fallback event); trajectory_ledger self-test asserts the owner's check on its 4.8 + 5 fixture.
- Behaviour change: `Opus 5.5` and `claude-opus-5-5-20261001` are no longer Opus 5.5 (`test_difficulty_v3.py`
  updated; 9/9 in the sandbox [O]).
- Acceptance `scripts/v1_acceptance.py` PASS (`logs/v1_acceptance.txt`) [O]: default expected model claude-opus-5-5
  -> all five rev14 runs v3_valid False; expected claude-opus-4-8 -> pre/r1/r2/r6 mixed, r3 unmixed and the only
  VALID one; model gate FAIL; L4 (rev13 pre-check without its fallback event 5855) still mixed/INVALID; a synthetic
  Opus 5.5 run v3_valid True, unmixed. Live 01a MODE B step 1: V1 bullets added (targeted).

### G1 (surface_grader hardening)
- surface_grader: the eight defects fixed as patchable module functions (`_section_start`, `_section_body`,
  `_strings`, `tracker_final_state`, `tracker_preserved`, `_row_keys`, `_range_only`, `TOOL_ALIASES`,
  `_entry_match`); `register_parent`, `tracker_entry`; unreadable register (decode error) and tracker (patch with no
  text) -> UNGRADED (None); gates: average / full passes by bounds, SD / patterns by enumerating up to 2^12
  completions, else INCOMPLETE; UNGRADED cells listed; `decided_by` per failed slot; docstring updated.
  gradable_surface: rev14 format converted on load (`from_revision14`, Season Pass deliverables), selectors
  `tracker_entry` / `register_parent`, `slot_keys` for tracker selectors. trajectory_ledger `table()` keeps an
  undecodable CSV as a candidate with rows None.
- rev13 c10 reproduction: 0 differences with `--truth` and with `--solver` (`logs/g1/rev13_c10*.txt`); V3 92.1 %,
  SD 0.068 [O].
- rev14 (`logs/g1/rev14_grades.txt`): pre 90.2 % {S04 S05 S07 S08 S40}; r1 92.2 % {S43 S46 S47 S52}; r2 76.1 %
  {S04 S05 S07 S08 S38-S46}; r3 91.8 % {S01 S47 S49 S52 S54} with S43/S44 and S69-S71 passing; r6 99.6 % {S01}:
  exactly the grades of record [O]. V3 gates refused (4 baseline slots, V3 needs 6), as designed.
- Format suite `support/fixtures/surface_formats/` (new; builder `build_fixtures.py`, README, MANIFEST): minimal
  write payloads of all 12 runs (1.2 MB), built only after the full runs matched the grades of record and each
  fixture graded like its full run; `--check` rebuilds byte-identical [O]. selftest_sandbox COPY now includes it.
- Planted (`surface_grader.PLANTED_G1`, run by the self-test): 8 defect cases, unreadable register, unreadable
  tracker, UNGRADED gates (0.4/0.6 bounds: average PASS, SD INCOMPLETE over 64 completions), the 12-run format suite.
  Falsification `scripts/falsify_g1.py` PASS (`logs/g1/falsify_g1.txt`) [O]: control passes; each of 11 undone
  fixes fails its own case; the real-run fixtures also catch defects 1, 2, 3, 4, 5, 7, 8 (e.g. 7 -> r3 S69-S71,
  8 -> r3 S43/S44). Defect 6 flips no real slot: undone, r3's review group reads (0, 2) instead of (27, 27), but r3
  fails S49/S54 either way (truth 28) [O]; the planted case is its guard.
- Frozen copies: SHA256SUMS verified before and after each use; `find -newer` marker empty [O].

### H1 (node_verdicts) + contract and ledger support
- oracle_kit: optional `RULES[r].controls` + `over_application`, `CHANNELS {kind, degrade, members, ...}`; owners
  `controls_of`, `channels_of`; blocking `contract.controls` (live operators). Planted: ghost member, dead
  over-application, unknown channel kind, dead channel degrade each FAIL [O].
- node_verdicts: `mechanism?` for unreproduced in-cohort errors (pending review, never a landing); class-field
  attribution for rules that decide the class; `decider()` via `tl.deciders`; control trials (OVER-APPLIED / HELD,
  beside the rule's verdict); channel reports (FAILED / HELD); go-rule tally (expected model's own decisions, shared
  key or source merged, controls / slips / pending excluded); SURFACE-ONLY for rules that decide no register column
  (never proposed); `compare_attribution` compares landed-key sets with the reference and `--seed-ledger` records;
  proposals carry verdict, control and channel records; `--expected-model`. Self-test planted cases incl. "over-
  applies -> control record, no landing" and "both -> both".
- hardness_ledger: kinds `control` / `channel` (outside the priors); a verdict with `features.pending_review` is
  refused until `disposed_by`.
- Falsification `scripts/falsify_h1.py` PASS (`logs/h1/falsify_h1.txt`): control passes; 9 undone fixes each fail
  their self-test; shared fingerprint 0 differences [O].
- rev13 c05 (`logs/h1/c05_h1.txt`, exit 1 by design): 0 item differences; landed-key differences: run-4 validation
  tool = reference-implied = 8 keys {003 019 035 051 067 083 099 115}, SP-039/091 pending; run-3 snapshot_labels
  LEAKED with SP-091/106/112 pending (pre-H1 both LANDED, `logs/h1/c05_pre_h1.txt`). Shared fingerprint 0 [O].
- Adjudication [O] (rev13 SQL parsed as data; run-3 trajectory):
  - run-4 SP-039 / SP-091: wrote 2 = the early "device validation"; the eligible 17:54 replay says 0 (truth); the
    designed natural reading gives 3 (SP-039) / 0 (SP-091). An over-exclusion, not the mechanism: slips.
  - run-4 SP-079: receipt slip; its class HOLD is a cascade that happens to match the validation ablation.
  - run-3 SP-091/106/112: every timeline call returned labeled + unlabeled (Feb 12 ~12:30Z, before the snapshot);
    the first extraction kept both; a later single-key re-extraction (briefs by claude-opus-5 after the fallback at
    987: "Extract SP-091" / "SP-106" / "SP-112") dropped the unlabel and decided the register. Transcription slips.
  - Seeds to correct (P2 L row; ledger not edited): `hev_b639bb440e0cc1c4` (run-4 validation: 10 keys -> the 8
    above; SP-039, SP-079 out) and `hev_0aea2ae9c00e83c2` (run-3 snapshot_labels LANDED -> LEAKED, 3 slips).

### E2E (support/fixtures/season_pass_rev14/: solver.py wrapper, e2e_rev14.py)
- Wrapper over the frozen rev14 oracle (imported under -B): 12 rules (8 rev12 + M1-M4 with T40-T47 / C12-C15
  nodes and families A16/A15/A14/A1), per-key disables spliced, M2 controls SP-110/119/123 with
  `over:process_findings`, M4 agreeing controls SP-009/019 (no operator). Truth = the oracle's [O].
- `python3 -B Task_Authoring/support/fixtures/season_pass_rev14/e2e_rev14.py`: E2E PASS 13/13
  (`logs/e2e/e2e_run3_postH2.txt`, 19:05-19:08) [O]: every run BOUND rev14; pre v3-invalid + mixed; pre 0 landings,
  go rule 0; SP-110 M2 OVER-APPLIED decided by the brief at 6049 (claude-opus-5; briefs 632/1835/5017/6049); the
  failed-slot sets of record; r3 S43/S44/S69-S71 pass; 25 control records move no prior; only r2's pending reviews
  (SP-101) refused; r3's verdicts move exactly its 6 families; the forecast runs; frozen copies unchanged; shared
  fingerprint 0. Run 1 failed on the forecast (value_notes inert); run 2's prior check was vacuous (parsed the
  wrong JSON level) - both fixed before run 3.
- Also seen: r2 M2 LANDED SP-108/SP-114 (class attribution); r1 fixture_binding SP-016.

### H2 (priors)
- One trial per (task, revision, run, family); Kish design effect per task, rho 0.5 (assumption, `--rho`); n_eff
  per task in priors / mechanism_priors.json. The design effect counts a task's trials, not its weighted trials
  (corrected ~20:00: with weighted trials, six correlated library runs at weight 0.5 were worth 1.0 trial at rho 1
  instead of 0.5). Self-test planted: three rules in one run = one trial; rho 0 / 0.5 / 1; the weighted-trials
  design effect fails (falsify_h1). hardness_forecast, hardness_gate, stage_gate self-tests ok [O].
- A17 (claude-opus-4-8): before Beta(15, 17), mean 0.469, n_eff 30, 14 records [O] -> after Beta(2.57, 2.85), mean
  0.47, n_eff 3.42 from 40 trials (library:FE-6a7e 0.97 = 30 trials / deff 15.5; library:NF2 0.86 = 6 / 3.5;
  season_pass 1.6 = 4 / 2.5) [O] (`logs/h2_A17_final.txt`). Criterion-2 view (--exclude-task season_pass): before
  Beta(14, 6) [D, recorded] -> Beta(2.17, 1.65), mean 0.57, n_eff 1.82 [O]. `references/mechanism_priors.json`
  regenerated (`logs/h2_write_priors_final.txt`). The 19:0x figures (Beta(3.59, 3.39)) used weighted trials:
  superseded.
- prior_family + prior_family_reason per portfolio rule: hardness_gate check (2 planted defects), forecast
  `family_of`, Manifest Spec row, live 01_Scenario_Design S5a bullet (targeted).

### F1 + M6 (forecast channels, batches)
- difficulty_mutation Engine: channel degrades and over-application operators are elements (geometry U counts them),
  never whole mechanisms. Planted: a scale-driven toy passes U (2/3) only with CHANNELS declared, BLOCKs (0/1)
  without [O].
- hardness_forecast: channel specs (members the degrade moves; latent member / batch / run; slots-only channels);
  rates from ledger channel / control records (per-task design effect), else disclosed `--channel-rate`, else
  UNPARAMETERIZED (not simulated); e drawn per baseline (1 - E[(1-e)^N] beside the plug-in); members re-solved via
  Engine.rows; per-channel expected loss alone; per-slot P(fail) / P(fails all six) (workload, never a block); run-score
  band; E_patterns; extent `batches` (M6, b = 1 - (1-theta)^(1/B), briefs from `--briefs`); `--mechanism-rate`
  (CONDITIONAL). Self-test planted [O]: 40 members at e = 0.02 -> 0.558 independent (exact 0.554), 0.023 linked;
  integrated 0.494 < plug-in 0.554 for Beta(2, 98); a cancelling count passes while both members fail; shared cause
  0.88 vs 1.34 patterns; three-step chain through a non-key-local solver 0.497 (exact 0.496); rates from records; an
  unrecorded channel UNPARAMETERIZED; M6 keeps the landing rate. oracle_kit: slots-only channels, `latent`;
  node_verdicts: slots-only channels judged on the surface, UNOBSERVED when the degrade moves no register column,
  channel records carry counts.
- rev14 wrapper channels: scale:groups (slip:groups moves 67 components with groups), tool_surface:register (S01).
- Replay `scripts/f1_acceptance.py` (`logs/f1/f1_replay_variants.txt`, exit 1 by its pre-set B criterion) [O]:
  observed baseline average 0.899, r3 0.918.
  - A out of sample (ledger priors, 9 mechanisms): E[avg] 0.67-0.86; average bracketed 1/15 views, r3 5/15.
  - B slips-only + channels: E[avg] 0.957 (0.928-0.984); average 0/15 (r2's real landings are excluded by
    construction), r3 15/15.
  - C evidence-weighted (0.10 / 0.15 / 0.08) + channels: E[avg] 0.919 (0.873-0.963); average 7/15 (every whole /
    batches view + correlated shard:32), r3 15/15. M1 is tracker-only and not modeled (its slots are NOT_SOLVER),
    so C's averages are if anything high [I]. Reported as PARTIAL.

### M2 (geometry U on a non-composable solver)
- difficulty_mutation: U UNVERIFIED (bound_verdict kept) + `geometry_dispositions` (geometry.U: accepted-unverified
  / redesign / solver-gap + reason); `geometry --dispositions`; exit 1 only on BLOCK or a missing disposition.
  preflight_report and stage_gate accept UNVERIFIED only with the disposition. Self-test: the LINKED toy ->
  UNVERIFIED, disposition required, a bad disposition refused [O]; stage_gate cases (both ways).

### M5 (oracle_kit)
- `contract.deterministic` also compares fresh processes with PYTHONHASHSEED 1 and 2 (SQL on stdin). Optional
  `base_route(record_id)`: base-record golden values read through `tools/hg.py records` (request in a scratch
  folder): absent or wrong -> FAIL. Self-test (auto-sandboxed; a direct call outside a sandbox is refused): set-order
  solver passes in one process, FAILs across processes; team_ZOM ("Zombie Match 3D") found PASS, wrong value FAIL,
  absent record FAIL [O].
- selftest_sandbox: COPY + the rev13 fixture's 00_Assigments.md; TASK_CONTEXT_PATCH lets the sandbox's
  task_context accept the linked universe sources (two read checks only; KB paths stay the sandbox's).

### M7 (stage_gate planted cases) + WARN-expectation case type
- Runner: `expect_warn` (WARN here, PASS on the good stage or a named `baseline`), `expect_pass` controls. Cases:
  structure.fresh surface input, raised self-review minimum (need >= 33), empty mutation.dispositions,
  geometry.margin WARN, liveness.dispositions WARN, forecast.preregistered control + WARN, geometry UNVERIFIED
  without / with disposition. stage_gate self-test: 127 cases ok (100 FAIL, 5 WARN / control) [O].

### WT
- tests/test_v3_stage_gate.py and difficulty_stats' self-test use `selftest_sandbox.scratch_tmp` (support/scratch/).
  First runs after the fix, outside the sandbox: 28 tests OK, self-test ok; shared fingerprint 0 differences; nothing
  outside scratch/logs newer than the marker; scratch empty afterwards [O].

### Incident (shared cache)
- 19:4x: `scripts/falsify_h1.py` called `oracle_kit._self_test()` in-process outside a sandbox; its new M5 golden
  check ran `tools/hg.py records` against the shared cache: 4 ADDED + 1 CHANGED under
  `support/local_search/contexts/dfabbff8a8c2c8eeb574/cache/{records,compact}/` (`logs/fp_*_final_falsify.tsv`) [O].
  Valid cache entries for the team_ZOM lookups; left in place (not deleted). Fixed: oracle_kit's `_self_test` refuses
  to run outside a sandbox; falsify_h1 re-runs itself in one (re-run: 0 differences) [O].

### After the move suite (19:46-20:15): fixes found while finishing P1
- node_verdicts: a control trial is OVER-APPLIED, and a channel member FAILED, only when the row reproduces the
  operator's own change (the fields it changes; the class only when it changes nothing else). Before, a class that
  matched as the cascade of another error counted. The go rule no longer lists as slips the errors a failed channel
  member or an over-applied control explains. Channel reports and records carry `family`. Planted: K-02's cascade
  class is no channel failure; K-04's cascade class is HELD with its error [O].
- hardness_forecast: channel rates pooled across tasks by family, like the mechanism priors (channel records: the
  channel's family, default its kind; control trials: the rule's family); before, they matched the channel id, so no
  other task's record could feed a new task. Planted: another task's scale records feed both scale channels, its
  chain record feeds none [O]. oracle_kit CHANNELS doc: `family`.
- trajectory_ledger `table_spec_from_surface` reads through `gradable_surface.load`. Before, a revision-14 surface
  gave no key pattern, so every brief had keys [] (r3: 37 briefs, 0 with keys): the replay's `batches` extent
  silently equalled `whole`, and E2E run 5 forecast with 0 brief batches [O]. Planted [O].
- difficulty_mutation `shards_for` refuses briefs that name no solver key (silent empty batches before). Planted [O].
- e2e_rev14: the forecast runs independent x {whole, batches} with r3's briefs. A new check: the channels take
  their rates from the temp ledger's records (scale:groups stays UNPARAMETERIZED: invisible in the register), with
  brief batches > 0.
- falsify_h1: 6 module controls + 16 undone fixes (adds the slip filter, channel / control own-change, H2 weighted
  trials, F1 channel-id rates, raw surface read, silent empty batches).
- Playbooks (targeted): 01_Universe_Injection S4b (declare controls, channels, base routes; contract.controls) and
  S5e (channel rates or a disclosed --channel-rate; per-slot P(fail) / P(fails all six) are workload); 01a B3
  (`mechanism?`, disposed_by, control / channel records outside the priors) and step 5 (channel rates, --briefs).
  The 01a wording "every traced failure in the four fallback runs" is intact (grep count 1) [O].
- The session dropped at ~20:15 before the final round started (no file, process or sandbox left; shared cache 0
  differences since 20:13; frozen copies verify) [O]. Re-run from 20:2x.

- Resolved by WT (above): `tests/test_v3_stage_gate.py` temp folders in support/local_search/cache, and
  difficulty_stats' self-test temp folder outside a sandbox.

## P1 round 2: independent verification and its fixes (20:5x ->)
- `verify` round 1 (openai/gpt-6.1-sol#max, no fallbacks except methodology's anthropic timeout) FAILED all six
  bundles that ran: code_g1, code_h1, code_misc, redteam_grading, redteam_attribution, methodology. The verdicts and
  their findings are stored under `logs/verify/round1/` (the methodology one was not written by the tool; recorded
  from the output in `round1/methodology.md`). `code_f1` was rejected by a provider auth error and never judged.
- Three `explore` subagents audited every finding against the code and measured its blast radius on the 12 real runs
  (consolidated in `logs/verify/design_round2_amendments.md`): 24 confirmed, 1 partial, 0 refuted; three verifier
  claims corrected (the `gradable:false` framing, a naive SHA fix flipping 7 real cells, and the class-cascade "fix"
  resurrecting SP-039). Every planned fix is output-neutral on the 12 runs except where the design says it moves.
- Design `logs/verify/design_round2.md` + `design_round2_amendments.md`: shared interfaces and disjoint ownership for
  three implementation subagents (grader; attribution+priors; forecast+oracle+labels).
- `methodologist` design review: FAIL, with corrections now applied - Q1 observation collapse (T = max counted runs,
  L = max landed, lower bound with the upper bound reported; refuse differing counts.runs), Q2 rate units must match
  the simulator's draws (member / batch / run per (revision, run); this found a real units defect), Q3 replay labels
  and caveats 6-10, Q4 exact conditional batch sampler, J1 H1-9 as a stated convention with a known false negative,
  J2 extra metamorphic G1 cases, J3 claims wording.
- Implementation is running on disjoint files; build keeps the E2E driver, the falsification scripts, integration
  and the full eval run. The E2E now asserts the exact accepted/rejected proposal ids and each channel's Beta against
  its exact eligible record set.

## Round-2 implementation (23:35 ->)
- All three implementation subagents hit their step limits before finishing; build completed their disjoint files.
  The tree is integrated; no subagent edits are outstanding.
- H2 correction from the methodologist's re-review: T = max(landed + not_landed) (not counts.runs), so A7 is
  unchanged at Beta(1.4524, 2.2381); A15 lower Beta(2.1429, 3.1714) mean 0.4032 and upper Beta(2.7143, 2.6)
  mean 0.5108; A17 Beta(2.5705, 2.8544). `references/mechanism_priors.json` regenerated
  (sha256 3b2ecb6f610e59b1d99b3dcc8f5cb14f233e7a97311d59df918692fe8fa12aaa; was 39f25c04...).
  Priors at rho 0/0.5/1 are in the final report; A17 mean 0.625 (rho 0) -> 0.474 (rho 0.5) -> 0.47 (rho 1).
- Q2 rate units implemented in `hardness_forecast.channel_rate`: member/batch/run per (revision, run), member->run
  conversion, a batch/member mix refused; control/channel records must be OVER-APPLIED/HELD or FAILED/HELD.
- M6 sampler replaced by an exact zero-truncated Binomial(B, b) draw (inverse CDF) and a uniform choice of that many
  batches; planted test at B=34, theta 0.3 and 0.005, 4000 draws (E[K] and marginals within 3+ SE).
- M5 golden: every routed id is read even when some evidence ids are in the SQL index; an absent routed record, a
  non-zero hg.py exit or an incomplete scan FAILs the block. V1: explicit ""/null model labels are UNKNOWN, and
  model_id/classify_model no longer strip whitespace.
- G1-1..G1-11 implemented; `surface_grader` now has 19 planted cases (including the round-1 counterexamples:
  replay replacement, register replacement/identity, delivery binding, entry tail, exact issue, range endpoint
  member, declared-ungradable gates). `falsify_g1.py` PASS: 19/19 cases and 12/12 fixtures under the control; every
  undo is caught; only "entry tail" also flips rev14 r3 S43/S44 (the old whole-line entry match), noted.
- H1-1..H1-9 implemented; `node_verdicts`/`hardness_ledger` planted cases for supersession+revision seeds, key-event
  deciders, unknown decisions, observation collapse/confounded run/differing runs/rho, unobserved controls, slots-only
  provenance, held provenance, control-explained channels, conditional class attribution (known false negative:
  the verifier's class+count case is a cascade by convention). `falsify_h1.py` PASS with 26 undos.
- E2E run 1: 13/14; the only failure was my own strengthened append assertion (pending proposals are rejected
  before an id is assigned, so the printed id is "?"). The assertion now checks the rejection count and reason.
  E2E run 2 is in `logs/e2e/e2e_round2b.log`.
- Open: F1 round-2 replay (seeds 7-9) running in `logs/f1/f1_replay_round2.log`; the 9 reclassified tracker lines
  still need blind labels from a reviewer; `build_fixtures.py` refuses a full run with an UNGRADED slot, so the
  12-run fixture suite cannot exercise the unreadable paths (planted self-test cases are the guard).
