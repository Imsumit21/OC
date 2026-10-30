# Learnings and improvements after Season Pass (2026-10-25)

This reconciles everything learned from Season Pass revisions 10–14, the Phase 0–1 tools audit and the revision-14
analysis. It records your decisions and lists the improvements: the ones made in this session (documents) and the ones
for the code session.

Evidence labels: **[O]** observed, **[D]** derived, **[I]** inference.

Sources:
- `support/audit/phase0_1/AUDIT_REPORT.md`
- `support/backtests/season_pass/rev14/working_files/rev14_platform_runs/Rev14_Precheck_Findings.md`. The full Season
  Pass task folder is archived at `support/archive/task_inputs_season_pass_2026-10-25/` (see its `../README.md`), and
  `task_inputs/` is a fresh V3 template for task 1.
- `plans/Rev13_Results.md`
- `plans/V3_Opus55_Difficulty_Plan.md`
- `references/Hardness_Mastery.md` §12

## 1. Your decisions
1. **The audit's open items: all five recommendations accepted.**
   - **Deviation 3:** `surface.coverage` becomes a real, tested check.
   - **Deviation 5:** rule-placement liveness flags apply to A15 nodes only.
   - **Deviation 6:** `surface.valid` blocks on structure only; geometry is advisory.
   - **Criterion 9a:** recorded as not met in 2 of 12 scenarios per view. The next pre-registration names its headline
     scenario in advance.
   - **`--max-k`:** the default stays 8; anything above needs an explicit, disclosed override, otherwise UNSUPPORTED.
2. **Calibration battery:** yes, alongside task 1 (§5).
3. **Who does what:** documents here (§4.1, done); code in a fresh session
   (`plans/Implementation_Session_Prompt_Fixes.md`), then a quick re-audit.
4. **Shared ledger:** explained in §6. The code session builds the merge procedure either way; pooling waits for your
   yes.
5. **Hard stays Hard.** An assigned Hard task is never downgraded or skipped. If single traps land too rarely on Opus
   5.5, the scenario and the injection escalate until Hard is reachable:
   - several independent cohorts with exact derived values;
   - dependency chains;
   - more delegation;
   - dependent writes across services.

   **Why it can work [D]:** an exact total over N members at per-member error rate e fails with probability
   1 − (1 − e)^N when member errors are independent: about a third to two-thirds of runs at N = 40–60 and e = 1–2 %.
   Shared causes (one rule, source or format behind many members) give less, opposing count errors can cancel, and a
   sampled member fails at only about e, so only aggregate rows compound. Three independent 20 % risks in a chain
   compound to about 49 %. Library evidence (model unstated): the A2 PR residue register, 133 PRs, averaged 70.2 %,
   with 0/6 runs right on its two derived totals (`references/Hardness_Mastery.md` §0, A2). It is not the revision-14
   frozen proxy, which also read 70.2 %. Season Pass had essentially one cohort, so scale cost at most one 8–10-point
   cascade per run.

   Every escalation stays V3-fair:
   - findable and incorporated;
   - at most 5 samples per group, plus a volume row and direct exception rows;
   - no impossible row. A predicted all-fail is a value the persona can't reach, on one of the four Evals bases, and
     blocks at any count (`playbooks/09_Rubric_Writing.md` gate 11). A row that fails all six runs is legal when
     VALID, with a step-14 justification; two invalid all-fails fail QC (`playbooks/11_AllFail_Analysis.md`);
   - runs that still finish; an errored run counts against validity, not toward difficulty.

   Intermediate failure rates are needed for the spread gate (population SD of the six runs, 0.10–0.30) and the
   failure-pattern gate, not for the all-fail rule. Each escalation is measured in the early runs. F1 and M6 move to
   P1, so the forecast can model this loss.

## 2. Reconciled learnings
**A. Opus on this universe.** These are Opus 4.8 observations. On Opus 5.5 each one is an assumption until §5 measures
it.

| # | Learning | Evidence | Changes |
|---|---|---|---|
| A1 | It reads every record a reasonable worker would, once the work points there | attention maps 7/7; 344/352 comments in revision 14 **[O]** | difficulty can't come from finding |
| A2 | It runs stated rules as checklists, and its own subagent briefs keep them | 7 rule families leaked 7/7 in revision 13; Opus 4.8 briefs kept the dismissal exception in revision 14 **[O]** | no hub-enumerated rules |
| A3 | It follows plain-words pointers | the ZOM-801 comments were listed 26 events after the description **[O]** | no pointer to the deciding record |
| A4 | Lists it compiles itself, with explicit membership, come out exact | value notes and process findings in pure runs **[O]** | not a lever |
| A5 | Per-item records beat confident claims and decoys | 0/5 claims, 0/7 and 0/6 decoys **[O]** | A1 needs the thread-continuation form |
| A6 | It still slips at scale and on the tool surface | about 1 wrong row in 128 per run; 2 multi-membership slips in run 3; native Sheet in 5/12 runs **[O]** | on one cohort, slips are a 2–5 point floor; several independent cohorts with exact derived values make scale an engine (§1 item 5) |
| A7 | Incorporation style, not the mechanism family, decided transfer | the same families landed on V7-T1 and SB-T2 (rule named, location not) and leaked on Season Pass (hub named every source) **[I]** | playbook S4 caution |

**B. Our design method.**
- **B1. Measure late, revise long.** Fourteen revisions on theory. The pre-registered E[average] was 72 % against about
  90 % observed. **[O]**
- **B2. One design posture for every mode.** Season Pass was Hard, a band only about 5 % of tasks get; most tasks need
  10–15 points of loss. **[O]**
- **B3. Correlated outcomes.** One population with cascading aggregates gives low SD. Use three or more independent
  mechanisms on separate outputs. **[O]/[D]**
- **B4. Run validity has to be designed in** (theme screen, §D). **[I]**

**C. Grading.**
- **C1. The proxy broke on real outputs.** Eight decoder defects (§4.2 G1), one of them introduced and fixed during the
  analysis, made the frozen proxy read 70.2 % for a pre-check whose corrected grade is 90.2 %. The pending
  `surface_grader.py` carries at least four of them and can't read the revision-14 surface format (audit §8). **[O]**
- **C2. Reviewer narratives can name the wrong root cause.** `/hardness` credited the Opus 4.8 briefs (events 445 and
  463), but the briefs that covered SP-110 (events 5017 and 6049) were the fallback's and dropped the exception. Read the
  payloads and the brief authors yourself. **[O]**
- **C3. `/rubric` precedent.** The same fact in two prompt-specified deliverables is not a duplicate, and rows that only
  share a root cause are not an overlap group (`02_Rubric.md` L63, L168). **[O]**

**D. Run validity.**
- **D1. The fallback.** A `model_refusal_fallback` (category bio) hit 8 of 12 platform runs. Afterwards the fallback
  model rewrote briefs or took over classification. Every traced failure in the four revision-14 fallback runs was its
  decision; the one pure Opus 4.8 run (r3) lost about 8 points to its own slips. Under V3 a fallback run is invalid.
  **[O]**
- **D2. Harness instability.** "Autocompact is thrashing" subagent stubs (45, 29 and 59 in three revision-14 runs) and
  auto-compactions. **[O]**

**E. The tools (audit).**
- **Real.** Outputs are computed from SQL and trajectories; planted changes moved only their own rows; `trajectory_ledger`
  matched revision 14 on every shared number. **[O]**
- **Ready after fixes:** B1, B2, H3, H1, H2, M1–M7, L1–L10. **[O]**

**F. Forecast and priors.**
- **F1. Priors.** They came from mismatched families, with within-run trials pooled (H2). The replay put only 4 of 11
  landing counts inside the 90 % intervals. **[O]**
- **F2. Missing loss channels.** The forecast had none for synthesis loss, control over-application or tool-surface
  substitution. Its slips-only floor of 95.1 % sits above the observed 90 %. **[D]**

## 3. Where sources disagreed, and the resolution
| Topic | Says | Says | Resolution |
|---|---|---|---|
| SP-110 root cause | `/hardness`: the orchestrator passed the rule correctly; a worker misread it | revision-14 session and my trace: the briefs covering SP-110 were Opus 5's and dropped the exception | Briefs 5017 and 6049 (Opus 5) lack the clause; 463 and 632 (Opus 4.8) have it. It was a fallback-brief failure: valid for the platform (OPUS_OBSERVED), not Opus 4.8 evidence |
| Pre-check score | frozen proxy 70.2 % | corrected copy 90.2 %; `/hardness` reading | 90.2 %, confirmed against the payloads |
| Run-3 score | driver 86.7 % | manual reading, about 91.8 % | about 91.8 %: S43, S44 and S69–S71 are grader artifacts |
| Revision-13 run-4 landed keys | `node_verdicts`: includes SP-091 | ledger seed: SP-079 instead | Neither is established (audit H1). Adjudicate both in the code session |
| The A17 prior | Beta(14, 6), expecting 2–7 landings in 7 runs | observed 1, 1 and 0 | mismatched families (H2): count one trial per (task, revision, run, family) and record the family choice |
| Criterion 9a | shard reading passes | all scenarios: fails 2 of 12 | decided: not met in 2 of 12 |
| Who made the revision-14 errors | findings §9: every traced failure was the fallback's, none Opus 4.8's | the same section's r3, added later: a native Sheet and two group-membership slips, all Opus 4.8's | Every traced failure in the four fallback runs was the fallback's; r3's about 8 points were Opus 4.8's own. The frozen findings line predates r3 |
| The library's only Opus 5.5 record | `Hardness_Mastery.md` §0, A1: "Opus 5.5 pass@1 0/6" | audit L5: its source doesn't establish the model | Treat it as model-unknown; there is no Opus 5.5 evidence yet |
| Revision binding | implementation: BOUND | audit: SINGLE is vacuous | audit B2: bind on evidence, with an explicit INSUFFICIENT outcome |
| What "predicted all-fail" means | this session, 2026-10-25: a row expected to fail every run, so Hard needs intermediate rates (also sent to the defeat-plan reviewer) | `playbooks/09_Rubric_Writing.md` gate 11: a value the persona can't reach, on four Evals bases; `playbooks/11_AllFail_Analysis.md`: an observed all-fail is legal when VALID | The playbooks. Intermediate rates come from the SD and pattern gates. Corrected in §1 item 5 and the V3 plan §11 |
| The graded shape for Hard | defeat-plan reviewer: 8–10 rows at p ≈ 0.5 is the only band | review: the SD bound depends on W, the 1/3/5 weights and shared causes (at W = 0.76, equal independent rows keep σ ≥ 0.10 up to 14 rows); the pattern gate is no upper bound; an all-fail is justification work | No fixed row count. S5a states the constraints, and the forecast evaluates the weighted portfolio |

## 4. Improvements
### 4.1 Done in this session (documents)
- **`references/Hardness_Mastery.md`:**
  - a new §12 with the Season Pass evidence and lessons;
  - an Oct-25 update under §0's recipe;
  - the Season Pass leaks added to §9.
- **Staged playbooks, guide and plans.** These are in `support/pending_edits/`, and the move applies them. The live
  originals are unchanged, so the move's base hashes still match.

| File | What changed |
|---|---|
| `playbooks/01_Scenario_Design.md` | S0: the loss budget from the mode, and the theme screen. S4: delegate by role, not by location. S5a: the Season Pass leaks rejected, and the portfolio sized to the budget, with prior sources |
| `playbooks/01_Universe_Injection.md` | new S5f: 1–2 early Opus 5.5 harness runs before `/injection`, keep or replace mechanisms, at most two cycles |
| `playbooks/01a_Hardening.md` | V3 run validity (a fallback run is invalid; attribute failures to the deciding model); confirm every failed slot against the payload, UNGRADED never false; the V3 go rule and the two-pre-check stop rule |
| `playbooks/09_Rubric_Writing.md` | gate 5: accept unambiguous identifier prefixes of 7 or more characters |
| `Guide/How_To_Author_A_Task.md` | "Rules that cost the most cycles": the Season Pass lessons |
| `plans/V3_Opus55_Difficulty_Plan.md` | the decisions recorded |
| `plans/Fold_Hardening_Into_Scenario_And_Injection.md` | change log, revision 5 |

### 4.2 For the code session
Priority: **P0** before the move, **P1** before task 1's platform pre-check, **P2** soon after.

**Status, 2026-10-25 17:50:** P0 done and verified by the code session (evidence in `support/fix_session_2026-10-25/`);
the move is next. Rows and clauses marked "2026-10-25 review" come from the review of the defeat plan.

| # | Pri | Work | Accept when |
|---|---|---|---|
| B1 | P0 | `apply_pending.py`: back up every live target to `.rollback/<timestamp>/`; a durable journal written before each step; copy the tools rather than move them; `--resume` and `--rollback` (which also removes new targets); `--check` recognises "already applied" | planted failure tests: kill mid-apply, then resume; kill, then roll back; already-applied detection |
| B2 | P0 | Binding on evidence in `node_verdicts` and `trajectory_ledger`, with an explicit INSUFFICIENT outcome; no unchecked SINGLE in the gate; each run's own revision and `sql_sha256` on its proposals; no fallback to the first SQL | a revision-13 run against revision-14 SQL gives INSUFFICIENT or UNBOUND, never BOUND; a planted mislabel test |
| H3 | P0 | Self-tests use `tempfile` folders (`stage_gate`'s `SELFTEST_TMP`, a temp ledger); cache writers (`persona_view`, `hg.py`) sandboxed; the move's follow-up commands replaced with the temp-folder checker and a sandboxed `hardness_gate` | the fingerprint of `support/local_search/` and `support/hardness_ledger/` is unchanged by every self-test |
| D3 | P0 | Gate 17, `surface.coverage`: when a surface exists, require a §G line or a covering row per slot, plus one planted defect (audit M1) | the bad case fails, the good one passes |
| D5 | P0 | Rule-placement liveness flags on A15 nodes only | the revision-10 liveness re-run reports the new precision |
| D6 | P0 | `surface.valid` blocks only on structure (schema, selectors, weights); geometry advisory | planted structural and geometry defects behave as specified |
| MK | P0 | `--max-k` default 8; above 8 needs `--allow-max-k N` and prints a disclosure; otherwise UNSUPPORTED | self-test |
| MV | P0 | **The move**, in a maintenance window: check-only says "ready", fingerprints are taken before and after, the sandboxed self-tests pass, and `mechanism_priors.json` is generated | the gate-policy hash changes as expected, and every self-test passes from `tools/` |
| G1 | P1 | `surface_grader` hardening. The eight decoder defects: (1) the heading is the first mention instead of a heading-like line; (2) sections end at intro prose or table headers; (3) `text` selectors search JSON-escaped strings; (4) only the last tracker update is read for state or preservation; (5) a bullet holding a key list counts only its first key; (6) group detection matches intro prose ("Evidence review … (SP-001..SP-128)"); (7) tool aliases (`slack_conversations_add_message` as a thread reply); (8) SHA-prefix length in entry regexes (accept unambiguous prefixes of 7 or more). Also read the revision-14 surface format and its selectors (`register_parent`, `tracker_entry`); make unreadable content UNGRADED, never false: the average and full-pass verdicts by bounds (UNGRADED counted as pass and as fail), SD and patterns by enumerating the completions, otherwise INCOMPLETE; add a format-fixture suite from all 12 Season Pass runs | revision 13 reproduces exactly; the revision-14 failed-slot sets match the grades of record exactly (`support/backtests/season_pass/rev14/README.md`), with the scores they imply (pre 90.2, r1 92.2, r2 76.1, r6 99.6 %; r3 whatever its slots give, about 91.8 %) |
| V1 | P1 | Intake provenance, with one owner of model labels shared by `trajectory_ledger` and `difficulty_stats`' model gate: strip only bracketed suffixes and compare exactly; `<synthetic>` stays out of the model check but counts under completeness; an unknown label gives UNKNOWN. `mixed_model` and `v3_valid` are separate outcomes (2026-10-25 review). Failures are attributed to the deciding model (brief writer, writing thread) | default expected model: all five revision-14 runs v3-invalid; `--expected-model claude-opus-4-8`: pre, r1, r2 and r6 mixed, r3 unmixed; a synthetic Opus 5.5 run with `[1m]` and `<synthetic>` labels is v3-valid; an off-model subagent and a removed fallback event still flag |
| H1 | P1 | An unreproduced error inside a cohort is "mechanism?" pending review; `compare_attribution` compares landed-key sets; adjudicate SP-091 against SP-079. **Control records** (2026-10-25 review): when the solver declares a rule's control members and an over-application degrade, an error on a control member whose written value matches the degrade is a control trial (OVER-APPLIED, else HELD), with its deciding event and model, beside the rule's verdict on its scope (a rule can land and over-apply in the same run). Control trials never count as landings for the go rule or the mechanism priors; they are F1's control-channel evidence | audit planted cases; a planted run that over-applies a rule to a control member gives a control record and no landing; one that does both gives both |
| E2E | P1 (2026-10-25 review) | One command runs the five revision-14 runs through `trajectory_ledger` → `node_verdicts` → `surface_grader` → a temp `hardness_ledger` → `hardness_forecast`, inside the sandbox | the exact failed-slot sets of record; r3's S43/S44 (8-character SHA prefixes) and S69–S71 (`slack_conversations_add_message`) pass; the pre-check is v3-invalid and mixed, with 0 designed landings, and SP-110 is a control record for M2 from an Opus 5 brief (declared in a fixture wrapper if the frozen solver can't express it; never edit the snapshot) |
| H2 | P1 | Priors: one trial per (task, revision, run, family); within-task replicates get an effective sample size; the library family recorded per portfolio rule | the A17 prior recomputed and printed with its records |
| M2 | P1 | Geometry U when the solver isn't composable: UNVERIFIED plus a written disposition, not BLOCK | self-test |
| M5 | P1 | `oracle_kit` determinism across processes (different `PYTHONHASHSEED`); golden values through `hg.py records` | self-test |
| M7 | P1 | Planted defects for the uncovered check families (audit M7) | checker cases |
| F1 | **P1** (from P2, 2026-10-25, §1 item 5) | Forecast channels for complexity: scale slips (a per-member error rate per model); dependency chains (a slot fails when an upstream fact it depends on fails); delegation (M6); synthesis loss (A20), control over-application (H1's control records), tool-surface substitution; base slips scaled to population size. **Dependence** (2026-10-25 review): sampled member errors are re-solved through the solver, never applied by formula, so a sampled member fails at about e, aggregates compound, and opposing count errors can cancel; shared causes are latents from the solver's rule→member, batch and run structure, plus independent per-member slips; rates are integrated over their uncertainty (1 − E[(1 − e)^N], not the plug-in). Each channel reported apart from mechanism landings, with its parameters, their ledger records and UNCALIBRATED, and each slot's P(fail) and P(fails all six runs), the latter as all-fail justification workload, never a block; a parameter without a record needs an explicit, disclosed override. `node_verdicts` reports each declared channel per run (failed or held, deciding event and model) for the go rule. Geometry U counts complexity channels the solver declares as degrades. A fallback is a validity flag, never a lever | the revision-14 replay brackets the observed about 90 % and r3's about 91.8 %; planted surfaces at the same marginal e = 0.02 over 40 members: independent ≈ 0.554, fully linked 0.02; a count slot with one false inclusion and one false exclusion passes while the affected sample slots fail; a cause shared across slots gives fewer failure patterns in the simulated gates; a three-step chain compounds as 1 − Π(1 − q); a planted scale-driven design passes geometry U only through its declared degrades |
| M6 | **P1** (from P2, with F1) | Shard scenarios: per-batch misses within a run, with batch sizes from the `trajectory_ledger` briefs | self-test |
| WT | P1 (2026-10-25) | Write boundary: `tests/test_v3_stage_gate.py` and `difficulty_stats`' self-test put their temp folders under the scratch root, even outside the sandbox | the shared-cache fingerprint is unchanged by both; neither is run before the fix |
| L | P2 | Ledger: seed Season Pass revision 14 (5 runs; fallback decisions labelled `claude-opus-5`); a merge procedure for contributors' ledgers (§6) | priors print per model, with record ids; a merge of two ledgers is idempotent |
| RB | P2, before task 1's step 15 (2026-10-25 review) | Difficulty provenance: `12_difficulty_input.json` records the hashes of `09_Rubrics.json`, `10_Baseline_Verifier_Results.md` and the trajectories it was built from, and `stage_gate.py difficulty` checks them; every rubric change after the rubric check (step 12c) carries a fairness disposition and a regrade receipt for all six runs | a matrix built from an older rubric or verifier export is refused; a change without a receipt blocks |
| M3 | P2 | `trap_liveness`: rank nodes, with per-feature precision on the backtest, instead of flagging | revision-10 report |
| J | P2, optional | An LLM-judge cross-check of text rows (`PROBE_*` environment), reconciled with the deterministic grader | agreement on the Season Pass fixtures, or every disagreement explained |
| Lx | P2 | Audit L1–L10, wherever cheap | listed in the report |
| SG | **P1** (2026-10-26) | `surface.gradeable`: a dry-run that decodes a synthetic fixture for every slot through the grader's real decoder and fails any slot it cannot read. Planted cases per selector class (text-only group source; one-table decode; keys-exact against the whole truth; `tracker_state` on a Trello id; `slack_thread` on a channel id) | task 1's surface has 0 ungradable slots; every slot is either graded on the pre-check proxy or listed UNGRADED with a reason |

### 4.3 For task 1's build (owner: the scenario/injection session)
Priority: **before any pre-check**. Neither item is about difficulty.

| # | Pri | Work | Accept when |
|---|---|---|---|
| GT | P0 | **Prompt ground truth.** Settle the six forks the platform prompt review lists: cut-level resubmissions (EN 2/4, FR 2); TR/PL wave-2 scope via the English fallback; FR r1/r3 overlays; register scope; register row grain (per asset vs per storefront and slot); ES held-out tickets. Each changes register rows, tickets, the Storefronts table and the posted counts. Settle each with one prompt sentence or one persona-visible record the agent can find — never an answer-key sentence | a re-run of the prompt review reports Unique Ground Truth PASS, and each fork has one fair outcome the rubric can grade |
| SF | P0 | **Surface↔grader conformance.** `truth_fields.groups` is `"reason"`, so the 9 `group_count` and 2 `group_key` slots read the wrong truth side (47 of 148 weight); `register_keys_exact` compares 60 register keys against the whole truth file; `tracker_state` reads a Linear state for a Trello card id; `slack_thread` tests a channel id. Re-point every slot to a deliverable and selector class the grader can read: group memberships in the truth's row groups, counts derived from the register/pack tables, Trello card fields for the brief card, a channel-post check for the art-channel post, keys-exact against the register deliverable | 0 ungradable slots; the pre-check proxy grades every slot or names it UNGRADED; the rubric is written only after GT passes |

## 5. The calibration battery (alongside task 1)
**What it measures.** Opus 5.5 catch rates for eight trap families: A1 + A14, A4, A9, A12, A3, A19, A20 and A15. The
V3-fair form of each is in `plans/V3_Opus55_Difficulty_Plan.md` §5.

**What a probe is:**
- one small, realistic request (Normal tier, 50–100 calls) on the October 2025 universe;
- 3–6 graded facts;
- a seed of at most about 60 rows;
- a solver.

**Runs.** 3 Opus 5.5 runs per probe in the independent harness, configured like the platform. That is 24 runs.

**Scale probe** (added 2026-10-25, §1 item 5). One larger probe measures Opus 5.5's per-member error rate and how it
compounds: a delegated cohort of 40 or more members, with exact derived totals. It is the first Opus 5.5 evidence for
F1's scale parameter, and it is load-bearing: its rate sets N for every scale row, and a scale row's failure rate can
be tuned through N, which a trap family's can't. Record member-level errors with their shared causes (rule, source,
format, batch), so F1 can separate shared from independent errors.

**Grading.** The hardened `surface_grader` (G1), or a per-probe checker until G1 lands.

**Records.** `claude-opus-5-5` · `NAME@VERSION` · `source: probe`.

**Catalog** (revised 2026-10-25). Three runs are weak evidence: 2 of 3 has a 95 % interval of 21–94 %. A family is
*promising* at 2 or more of 3, *weak* at 1 of 3, and *leaks* at 0 of 3; never "approved". For each family a task relies
on, prefer a second probe design over more runs of one: at ρ = 0.5, three runs of one probe count as 1.5. Add a control
probe (a rule with out-of-scope members) before a task relies on control errors.

**Exit.** Stated for the portfolio, not per probe. The battery is done when its posteriors, with the scale probe's
per-member rate, let a fair task-1 portfolio meet the design gate (E[average] ≤ cap − 8 and P(all gates) ≥ 0.5) with at
least one spare channel. The forecast draws each rate once per simulated six-run baseline, so P(all gates) already
carries the uncertainty; no family has to land in every run. Otherwise escalate with complexity (§1 item 5) or re-probe.

**Dependencies and owner.** It needs B2, V1 and G1 (or per-probe checkers). A probe-authoring session builds it once the
code session lands P0 and P1; I'll write its prompt then.

**Harness parity.** Run task 1's platform pre-check through your harness too. If they differ by more than 10 points, or
land different mechanisms, harness results gate nothing until that is fixed.

## 6. The shared ledger, simply
- **What it is.** The ledger is our notebook of results: "in run X of task Y, on model Z, this kind of trap caught the
  agent", or "didn't". The forecast reads it to predict how hard a new design will be.
- **What "shared" means.** Every contributor's pre-checks and baselines go into one notebook, not one each. With ten
  contributors, we learn Opus 5.5's real catch rates about ten times faster, and nobody repeats a trap someone else has
  already seen fail.
- **"Kept separate per model".** Opus 4.8 results never count as Opus 5.5 results.
- **"Tagged by source".** Each line says where it came from (platform run, harness run, probe), so we can filter.
- **The risk.** One person's mislabelled result can skew everyone's forecast. Three things limit it: the tool rejects
  conflicting duplicates, the source tags, and one owner who merges contributions.
- **What you decide:** yes or no, and who owns the master copy. Until then, the code session builds the merge procedure
  and nothing is pooled.

## 7. Order from here
1. **The code session** (`plans/Implementation_Session_Prompt_Fixes.md`): P0, then the move, then P1.
2. **A quick re-audit** of P0/P1 and the move. I write its prompt after the session reports.
3. **In parallel:** the probe-authoring session (prompt after P1), and task 1 through S0–S5a. Task 1's early runs
   (injection S5f) wait for B2, V1 and G1.
