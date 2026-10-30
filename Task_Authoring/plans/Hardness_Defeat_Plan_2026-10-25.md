# Hardness defeat plan: the additions that make the next tasks beat Opus 5.5

**Date:** 2026-10-25
**Status:** Proposal, reviewed 2026-10-25. Useful items moved to their owner documents; not an authority.
**Scope:** the Phase 0–1 tool session, the Opus 5.5 calibration battery, task 1's design, and the decision gates between them.
**Evidence labels:** [O] observed · [D] derived · [I] inference.

## 0. Relationship to the existing plans

- `Implementation_Session_Prompt_Fixes.md` remains the execution prompt for P0/P1. This file adds what that prompt must include to serve the actual goal, and what must happen outside it.
- `V3_Opus55_Difficulty_Plan.md` remains the design doctrine. This file turns its §3, §5, §6 and §7 into gates, tests and task-1 rules.
- `Fold_Hardening_Into_Scenario_And_Injection.md` owns the skill-architecture change (hardening folded into scenario/injection, the geometry and budget tool specs, the removal checklist). This file assumes that change and does not re-specify it; where both touch the hardness budget, the §5 gate here is the acceptance test for the §5 budget there.
- `Learnings_And_Improvements_2026-10-25.md` and `Rev14_Precheck_Findings.md` are the evidence base.
- No task is in flight; Season Pass is skipped. Nothing here reopens the Season Pass files or `task_inputs/`.
- Every new test plants the failure it guards against, and every acceptance test must fail on the pre-fix code and pass after it.

## 1. Why the current fixes plan is not enough

### 1.1 The evidence in one table

| Fact | Value | Source |
|---|---|---|
| Revision-14 grades of record | pre 90.2, r1 92.2, r2 76.1, r3 about 91.8, r6 99.6 % | `support/backtests/season_pass/rev14/README.md` **[O]** |
| Runs with a fallback | 4 of 5 rev14 runs; 8 of 12 platform runs across revisions 13–14 | `Rev14_Precheck_Findings.md` §5, §9 **[O]** |
| Only pure Opus 4.8 run | r3, about 91.8 %; losses were the native Sheet and two membership slips, not the designed mechanisms | `Rev14_Precheck_Findings.md` §9 **[O]** |
| Pre-check designed landings | **0 of 4**. M1, M3 and M4 leaked; M2 was applied correctly to its six members and failed one control (SP-110) | `Rev14_Precheck_Findings.md` §1, §3 **[O]** |
| `/hardness` on that pre-check | 3, NON-FAIL, PROCEED. It does not predict the six-run baseline | `Rev14_Precheck_Findings.md` §8.6 **[O]** |
| The control error's cost | 9.8 points, weight 25: S04, S05, S07, S08, S40 | `Rev14_Precheck_Findings.md` §2 **[O]** |
| Grader error | frozen proxy 70.2 % vs corrected 90.2 %; one run moved 20 points | `Rev14_Precheck_Findings.md` §4 **[O]** |
| Forecast error | pre-registered E[average] 72 % vs about 90 % observed; A17 expected 2–7 landings, observed 1, 1, 0 | `Learnings…` §2 B1, §3; `Rev14_Precheck_Findings.md` §7 **[O]** |
| Forecast interval coverage | 4 of 11 landing counts inside the prior's 90 % intervals; observed 92.1 % inside the band in 2 of 24 scenario-views | `Implementation_Phase0_1_Final_Report.md` **[O]** |
| Slips-only floor | 95.1 %; the pre-check scored 90.2 % only because of the control error the model lacks | `Rev14_Precheck_Findings.md` §7 **[O]** |
| Partial baseline mean | 89.3 %, population SD 0.098 over three runs | `Rev14_Precheck_Findings.md` §9 **[D]** |
| Hard arithmetic | with three runs at 89.3 %, the other three must average below 50.7 % for a six-run average below 70 % | `Rev14_Precheck_Findings.md` §9 **[D]** |
| V3 caps and targets | Easy < 90 / target ≤ 82; Medium < 85 / target ≤ 77; Hard < 70 / target ≤ 62 | `V3_Opus55_Difficulty_Plan.md` §3 **[O]** |

### 1.2 The four implications

1. **The valid 4.8 baseline is about 92 %, not 90 %.** The only pure run scored 91.8 % with no designed mechanism landing. Opus 5.5 is unlikely to be worse. The next task starts at the top of the range, not the bottom. **[O]/[I]**
2. **The fallback supplied the variance.** It hit 4 of 5 rev14 runs; every traced failure was its decision. V3 invalidates those runs. Remove the fallback and the task returns to the slips-only floor. **[O]**
3. **The forecast over-credits landings.** Theory-based p̂ said 72 %; the runs said 90 %. H2 fixes one prior's counting, not the general over-credit. Without measurement on 5.5, the design gate is arithmetic on the wrong rates. **[O]/[D]**
4. **The gap is not a tweak.** The valid task needs 22–30 points more loss for Hard and 7–15 for Medium. A better grader cannot create those points; only a mechanism that lands on the target model can. **[D]**

## 2. Hardness rules

These are the design rules the next task must satisfy. Each is testable; each has a named failure mode from Season Pass.

| # | Rule | Why it adds hardness | Test |
|---|---|---|---|
| H1 | **Difficulty after complete retrieval, not in finding.** Assume Opus 5.5 opens every record a reasonable worker would. | Rev14 read 344 of 352 Linear comments, 281 of 281 reviews, and the current Confluence page. Finding is not a lever. | The mechanism's deciding record is returned by the natural call; a run that reads it still fails on judgment. |
| H2 | **Incorporate by role, not by location.** Name the governing thing in ordinary words; let the records lead; never enumerate every source in a hub. | A7: the same families landed on V7-T1 and SB-T2 where the rule was named but its location was not; they leaked on Season Pass where the hub named every source. | The prompt/records name what governs; no hub lists every authority; the deciding record is reachable by a normal multi-hop path. |
| H3 | **Judgment, not stated rules.** Use A1+A14, A4, A9, A12, A19, A20 and A15. Do not make an explicit per-record rule the engine. | Rev13's 4 pure runs landed one explicit rule on one key; rev14's pre-check landed 0 of 4. Opus 4.8 executes stated rules at about 99 % field accuracy. | The mechanism survives complete retrieval; the loss is in the conclusion, not in a missed rule. |
| H4 | **3+ independent mechanisms on separate outputs; Hard 4–5.** No single hidden control gating most rows. | One hidden control makes runs bimodal (SB-T2: 2, 4, 3, 2, 54, 2 of 54), failing the pattern and SD gates. | The portfolio table has one row per mechanism, a distinct output, and no shared gate over 50 % of weight. |
| H5 | **Make the deliverable carry the load.** Ask for many per-item facts across services. | Synthesis is where the fallback lost items in rev14 (A20); it is a real 5.5 risk and a fair ask. | 40+ items, 6+ facts per item, per-item grading, a volume row. |
| H6 | **Collect slips, never manufacture them.** Exact derived totals over a real cohort; per-record outputs that cannot cancel; never grade one fact in 3+ rows. | A2: one class error cascades through totals; 2–5 points on a large cohort. Multi-membership slips cost r3 two keys. | Aggregate slots recomputed from the cohort; no fact appears in 3+ slots. |
| H7 | **Control errors are a measured channel.** A rule with a control set outside its scope; the agent must apply it only to the right members. | Rev14's SP-110 control error cost 9.8 points and was a judgment error, not a trick. The forecast currently lacks this channel. | The control set is explicit; a failure flips the totals; the forecast credits it. |
| H8 | **Multi-membership at scale is a slip floor, not the engine.** | r3 lost two keys on "count a component under every condition it fails"; A6 calls slips a 2–5 point floor. | The rule applies to a large cohort; the loss is visible in exact totals, not a single row. |
| H9 | **Tool-surface realism only.** Use a surface blind spot only if measured on the real tool surface; never use forced errors or async waits as difficulty. | A3 is 44.1 % author-reported; forced errors are excluded by V3 and produce CONFOUNDED runs. | The natural bulk call misses the evidence; the right call returns it; the path is verified on the actual export. |
| H10 | **Variance engineering.** Target per-run SD 0.10–0.30, at least 2 failure patterns, largest ≤ 50 %, fewer than 5 full passes. | V3 fails a flat task even at a low average. The rev14 valid run was a single 91.8 % point; the SD came from the fallback. | The forecast reports SD and pattern distribution; a synthetic six-run matrix passes the gates at the cap boundary. |
| H11 | **No fallback reliance.** A fallback run is invalid for V3; every mechanism must land in 5.5's own decisions. | Rev14's only losses came from the fallback. Counting them is the exact false-go the V1 fix exists to prevent. | Every landing has a deciding event and a 5.5 model label; the brief writer is 5.5. |
| H12 | **No rubric or verifier tuning.** Fix unfair rows first, then make the universe harder. | The easiest false defeat is a stricter rubric; the rev14 r3 case shows a 5-point swing from decoder rules alone. | Rubric hash frozen before the pre-check; any change has a fairness disposition and a full re-grade. |

## 3. The improvement plan

Priorities: **P0** before task 1's design; **P1** before task 1's first run; **P2** after the first baseline (unless pulled forward). "Hardness value" is **Direct** (changes the difficulty), **Enabling** (makes the signal trustworthy), **Protective** (prevents a false verdict), or **Ops** (keeps the toolchain stable).

### 3.1 Track A — make the signal trustworthy

This is the existing P0/P1 work plus the integration tests the current prompt lacks. It is necessary; it is not sufficient.

| ID | Pri | Change | Hardness value | Acceptance |
|---|---|---|---|---|
| A1 | P0 | **B1**: backups, journal, `--resume`, `--rollback`, already-applied detection, copy tools instead of move. | Enabling | Kill mid-apply, resume, roll back, already-applied; real subprocess kill via a fault-injection hook. |
| A2 | P0 | **B2**: evidence-based binding, explicit INSUFFICIENT, no unchecked SINGLE, per-run revision and `sql_sha256`. | Enabling | A rev13 run vs rev14 SQL gives INSUFFICIENT/UNBOUND, never BOUND; a two-revision batch is labelled per run; the gate rejects unchecked SINGLE. |
| A3 | P0 | **H3**: temp-folder self-tests; sandbox `persona_view` and `hg.py`; replace the move's shared-cache follow-ups. | Ops | Fingerprint of `support/local_search/` and `support/hardness_ledger/` unchanged by every self-test. |
| A4 | P0 | **D3, D5, D6, MK**: real `surface.coverage`; A15-only rule-placement flags; structure-only `surface.valid`; max-k default 8 with a disclosed override. | Protective | Bad/good coverage cases; rev10 liveness precision; structural vs geometry defects; max-k self-test. |
| A5 | P1 | **G1**: eight decoder defects, rev14 surface format, UNGRADED-not-false, 12-run format fixtures. | Enabling | Rev13 exact; rev14 **exact failed-slot sets**, not aggregate percentages. |
| A6 | P1 | **V1**: any non-5.5 message invalidates for V3; attribute the failure to the deciding model; per-run provenance table. | Enabling | Rev14 pre/r1/r2/r6 flagged, r3 clean; a non-5.5 subagent fixture; a fallback-event-removed fixture with 5.5 calls still flagged. |
| A7 | P1 | **H1 + CONTROL**: unreproduced cohort errors are `mechanism?` pending review; add **CONTROL** as a verdict distinct from LANDED; compare landed-key sets. | Enabling | The rev14 pre-check outputs **0 designed landings**, M2 a control error; SP-091 vs SP-079 adjudicated with record pointers. |
| A8 | P1 | **H2**: one trial per (task, revision, run, family); `n_raw`/`n_eff`; profile-matched priors; record ids. | Enabling | A17 prior recomputed with a golden value and its records; a mismatched profile is flagged, not silently used. |
| A9 | P1 | **M2, M5, M7**: geometry U is UNVERIFIED with a written disposition when not composable; determinism across processes; planted defects for the uncovered families. | Enabling | Planted non-composable solver; different `PYTHONHASHSEED` gives identical truth; each audit M7 gap has a case. |
| A10 | **P1 new** | **End-to-end difficulty fixture.** One command: rev14 pre-check and r3 through `trajectory_ledger` → `node_verdicts` → `surface_grader` → `hardness_ledger` → `hardness_forecast`; assert pre invalid, 0 designed landings, r3 ~91.8 with S01/S47/S49/S52/S54, two membership slips. | Enabling | The only test that fails if the chain silently reports "M2 LANDED, 90.2 %, go". |
| A11 | **P1 new** | **Forecast provenance and staleness.** Bind each forecast to the ledger prefix, portfolio, surface, priors version and tool hashes; reject stale inputs. | Enabling | A forecast produced before H2/F1 is rejected after the tool changes; a forecast for another surface is rejected. |
| A12 | **P1 new** | **Grader-disagreement queue.** Any disagreement between `surface_grader`, `node_verdicts`, `/hardness` and the verifier gets a written disposition and a record pointer. | Enabling | The 70.2 vs 90.2 class of disagreement is visible, not silently resolved. |
| A13 | **P1 new** | **No-rubric-tuning guard.** Freeze the rubric hash before the pre-check; any change needs a fairness disposition and a full re-grade. | Protective | A hash change between pre-check and baseline blocks the difficulty verdict. |
| A14 | **P1 new** | **Pre-register the headline scenario and max-k.** Record the 9a scenario and any `--allow-max-k` disclosure before the first run. | Protective | The next pre-registration names both; a post-hoc scenario choice is rejected. |
| A15 | **P1 new** | **Red-green tests + final fingerprint.** Each new test fails on the pre-fix code and passes after; full `tools/` fingerprint after P1, not only after the move. | Ops | Pasted fail-before/pass-after output; fingerprint after P1. |
| A16 | **P1 new** | **G1 timebox and split.** G1a: rev13 exact + rev14 slot sets. G1b: format fixtures + 5.5 dry run. | Ops | Task 1 can start on G1a with manual slot reads; G1b does not block S5f. |
| A17 | **P1 new** | **Doc-delta check + rollback drill.** Grep for S0/S4/S5a/S5f/MODE B/gate 5 after the merge; apply/kill/resume/rollback on a bundle copy. | Ops | The 2026-10-25 edits are present; the gate-policy hash returns to its original value after rollback. |
| A18 | **P1 new** | **Readiness table + "tools ready ≠ task hard."** A short table for S0–S5a, S5f, pre-check, baseline: ready/blocked and the dependency. | Protective | The report cannot claim frontier defeat from a tool-only pass. |

### 3.2 Track B — add real hardness

These are the items that change the score. The current prompt has none of them.

| ID | Pri | Change | Hardness value | Acceptance |
|---|---|---|---|---|
| B1 | **P0 for the goal** | **Opus 5.5 calibration battery.** 8 probes, one Tier-A mechanism each (A1+A14, A4, A9, A12, A3, A19, A20, A15); 3 runs each = 24 runs; 50–100 calls; 3–6 graded facts; seed ≤ 60 rows. | **Direct.** Replaces theory p̂ with measured 5.5 landing rates; the single highest-value item. | Catalog: per mechanism k/3, model, harness, source; approved at 2/3, weak at 1/3, leaks at 0/3. Forecasts credit only approved/weak. |
| B2 | **P0 for the goal** | **Task 1 candidate portfolio.** 5–6 mechanisms, 3–4 independent, 1–2 spares; at least one each of A1+A14, A4/A9, A20 and a control-error mechanism; plus A2 exact totals. | **Direct.** The engine; without it the task stays at the slips floor. | A portfolio table with weights, priors, expected loss, independence, outputs; a forecast at E ≤ cap−8, P ≥ 0.5, SD ≥ 0.10, < 5 full passes. |
| B3 | P0 | **Profile-matched priors.** Add `evidence_profile` to the portfolio rule: explicit-per-record, cohort-boundary, summary-override, synthesis. Match the library family's profile; a mismatch is flat or `TRANSFERRED · MISMATCHED`. | **Direct.** Fixes the A17 mismatch that over-credited landings. | A17 recomputed; a mismatched profile is flagged; the prior prints its records and `n_eff`. |
| B4 | P0 | **Control-error mechanism.** A rule with a control set outside its scope; measure it; add the SP-110 class to the ledger; pull the control channel from F1 into P1. | **Direct.** Rev14's only measured loss channel: 9.8 points, a judgment error. | The SP-110 fixture is CONTROL, not LANDED; a synthetic design where the control is the only failure; the forecast credits it. |
| B5 | P0 | **Synthesis-load mechanism (A20).** 40+ per-item facts across services; a volume row; per-item grading. | **Direct.** The fallback dropped items in rev14; 5.5 can too. | The deliverable carries 6+ facts per item; dropped items are visible; the forecast credits synthesis loss. |
| B6 | P0 | **Variance plan.** 3+ independent mechanisms on separate outputs; weights 1/3/5; simulate the six-run gates before building; target SD 0.10–0.30 and ≥ 2 failure patterns, largest ≤ 50 %. | **Direct.** V3 fails a flat task; the rev14 valid run was one 91.8 % point. | The forecast's SD and pattern distribution; a synthetic six-run matrix at the cap boundary passes. |
| B7 | P1 | **S5f early runs.** 2 valid Opus 5.5 harness runs before `/injection`; 1–2 cycles; keep/replace; CONTROL verdict; no fallback. | **Direct.** The only pre-injection measurement on the target model. | 2 valid runs; ≥ 2 mechanisms land in 5.5's own decisions; no fallback; a written keep/replace decision. |
| B8 | P1 | **Go/kill rule.** Corrected proxy ≤ cap−5; ≥ 2 mechanisms in 5.5's own decisions; no fallback; `/hardness` ≥ 3; at most two pre-checks per scenario. | **Direct.** The rev14 pre-check would fail it (0 designed landings). | A table of the four conditions per pre-check; a no-go if any fails; a second pre-check only after one universe-side fix. |
| B9 | P1 | **Harness parity.** Run the platform pre-check and the harness on the same task; if they differ by > 10 points or land different mechanisms, harness results gate nothing. | **Protective.** Prevents optimizing on an unrepresentative harness. | A parity table; a written decision on which results gate. |
| B10 | P2 | **Ledger seed and merge.** Seed rev14 with fallback landings labelled `claude-opus-5`; seed the probes; no pooling across models; a merge procedure. | **Enabling.** The priors are the design's input. | Priors print per model with record ids; a merge of two ledgers is idempotent. |

**Why these are the right levers.** The V3 plan's Tier A list is the only measured set that survives complete retrieval; the rev14 evidence says the old explicit-rule engines do not land on the target model. B1 measures the Tier A list on 5.5; B2 designs with the survivors; B4 and B5 add the two loss channels rev14 actually measured or exposed; B6 makes the outcome vary across runs instead of collapsing to one point. B3 and B8 stop the forecast and the go rule from over-crediting the old rates.

### 3.3 Track C — governance and decision gates

| ID | Pri | Change | Hardness value | Acceptance |
|---|---|---|---|---|
| C1 | P0 | **Design-budget gate or `budget_exception`.** Block a scenario that misses E ≤ cap−8 / P ≥ 0.5, or record the reason, requester and date. | **Protective.** Rev14's preregistration knew it missed the target and proceeded; the next task can repeat. | The rev14 design fails the gate; a synthetic design passes; an exception is visible in the report. |
| C2 | P0 | **Pre-registration.** Forecast, headline 9a scenario, max-k disclosure, rubric hash, portfolio and surface hashes, frozen before the first run. | **Protective.** Prevents post-hoc scenario or rubric choices. | A pre-registration file with hashes and the four gate predictions. |
| C3 | P0 | **No rubric or verifier tuning.** Freeze the rubric and verifier hashes; fix unfair rows first; re-grade all runs after any change. | **Protective.** The easiest false defeat is a stricter rubric. | A hash change between pre-check and baseline blocks the verdict. |
| C4 | P1 | **Kill/continue ledger.** Every pre-check's four conditions recorded; the second pre-check's decision automatic; a scenario switch after the second miss. | **Direct.** Prevents 14 revisions on one theory. | A table per scenario: pre-check 1, fix, pre-check 2, switch. |
| C5 | P1 | **Run-validity early stop.** After the pre-check and after baseline run 1: model, fallback event, brief writers, valid/invalid; stop before runs 2–6 if invalid. | **Direct.** Saves five runs and prevents contaminated priors. | A one-page validity table; a stop decision. |
| C6 | P1 | **"Tools ready ≠ task hard" statement and readiness table.** | **Protective.** The report cannot imply frontier defeat from a tool-only pass. | The table names each stage and its dependency. |

### 3.4 Track D — operations and handoff

| ID | Pri | Change | Hardness value | Acceptance |
|---|---|---|---|---|
| D1 | P0 | **Stage P1 before the move.** One move for P0+P1; final fingerprint after P1; sandbox suite from `tools/`. | Ops | The move log covers the final toolchain, not an intermediate one. |
| D2 | P1 | **Doc-delta check.** Grep for S0/S4/S5a/S5f/MODE B/gate 5 after the merge. | Ops | The 2026-10-25 edits are present. |
| D3 | P1 | **Rollback drill on a bundle copy.** Apply, kill, resume, roll back; compare the gate-policy hash. | Ops | The hash returns to `4459b8bdd4de` after rollback. |
| D4 | P1 | **G1 timebox and split.** G1a before task 1's S5f; G1b after. | Ops | Task 1 is not blocked on the full format suite. |
| D5 | P2 | **Known false-positive list for `trap_liveness`.** 14/17 flags, precision 0.571; use as a ranking, not a gate. | Ops | The next task's dispositions are not spent on false alarms. |
| D6 | P1 | **Task 1 readiness table.** S0–S5a, S5f, pre-check, baseline: ready/blocked and the dependency. | Ops | The next session starts on a true premise. |

## 4. Task 1 design template

This is a template, not a fixed task. It shows the shape that can reach the Hard budget without relying on the fallback.

### 4.1 Archetype and candidate mechanisms

Pick one archetype where at least three Tier-A mechanisms arise from the role's real work:

- **Vendor or partner dispute reconciliation:** A9, A4, A19, A20.
- **Incident or launch retrospective from long threads:** A1+A14, A4, A3.
- **Policy-governed release or refund decision over a cohort:** A12, A15, A2.
- **Budget or KPI variance review:** A19, A17, A20.
- **Partner or contractor onboarding audit:** A20, A9, A21.

| Candidate | V3-fair form | Graded on | Why it can land on 5.5 |
|---|---|---|---|
| A1+A14 | A colleague's confident early status; later replies in the same thread overturn a decisive fact; nothing hints. | The overturned facts in the deliverable. | Retrieval is complete; the failure is deferring to the early summary. 0/6 pass@1 on 4.8. |
| A4 | 4–6 eliminating facts across hops; the request asks for the conclusion in ordinary words. | The conclusion and each eliminated alternative. | Lists the agent compiles are exact; the judgment is the conclusion. 47–52 % on 4.8. |
| A9 | Every item has a later reply from the other party; some reverse the answer. | Per-item outcomes (≤ 5 samples) plus an exact count. | 4/5 missed the reversing reply on 4.8. |
| A12 | The prompt names the policy by its everyday name; the current version is in its natural home; an older one where people look first. | Outputs the policy governs. | 5/6 latched on the decoy in SB-T2. |
| A19 | "How does this compare with last quarter / the plan?" | The derived numbers. | Retrieved 5/6, computed 0/6. |
| A20 | The deliverable must carry many per-item facts that subagents gathered. | Samples plus a volume row. | 6/6 and 4/6; rev14 dropped items. |
| A15 | A house rule against the natural reading, applied per record, in the team document the work needs. | Per-record outcomes. | 4–5/6 on V7-T1; 0/7 when hub-enumerated. |
| Control | A rule with a control set outside its scope; the agent must apply it only to the right members. | The totals and the exact count. | Rev14 SP-110 cost 9.8 points. |
| A2 | Exact derived totals over a real cohort. | Aggregate slots recomputed from the cohort. | One class error cascades to 8–10 points. |

### 4.2 Weights and budget

- Weight by kind of work: lookup 1; interpretation, calculation, comparison, limited reconciliation 3; multi-source reconciliation, deeper reasoning, cross-modal, tracing 5.
- Target **40–55 % of weight at risk** for Medium; **55–70 %** for Hard.
- Hard: at least 4 independent mechanisms; Medium: at least 3; Easy: 2–3.
- The portfolio's expected loss is `Σ weight × landing rate`, plus the slip floor. It must reach `cap − 8` on the measured 5.5 priors, not the transferred 4.8 rates.
- If the forecast cannot reach the budget, redesign before SQL. Do not override without a written `budget_exception`.

### 4.3 Independence and variance

- Separate outputs: register, memo, slide, message, thread reply, ticket update.
- No single hidden control over more than 50 % of weight.
- At least two failure patterns, the largest at most 50 %.
- Target per-run SD 0.10–0.30. At 3 mechanisms × 13 % weight × p 0.5, SD ≈ 0.11; at 4 × 13 % × 0.5, SD ≈ 0.13. If the measured p is lower, add weight or mechanisms, not rubric rows.
- Use the forecast's SD and pattern distribution, not just its mean.

### 4.4 What to measure in S5f

- 2 valid Opus 5.5 harness runs, configured like the platform: Claude Code version, effort, subagent policy.
- Per run: model, fallback event, brief writers, call count, mechanism landings, CONTROL verdicts, synthesis loss, tool-surface substitutions.
- Keep mechanisms that land in 5.5's own decisions; replace leaks; at most two cycles; then change the scenario.
- A run with a fallback is invalid; do not count its landings.

## 5. Decision gates

| Gate | When | Pass condition | If fail |
|---|---|---|---|
| **0 Tools** | after P0/P1 | Every P0/P1 acceptance test passes; the end-to-end rev14 fixture passes; the final fingerprint is recorded. | Fix; do not start task 1. |
| **1 Calibration** | before task 1's S5a | At least 3 Tier-A mechanisms approved at 2/3 on Opus 5.5, **or** a signed risk acceptance that the design uses theory priors. | Run the battery; or design Medium/Easy. |
| **2 Design budget** | before SQL | E ≤ cap−8; P(all gates) ≥ 0.5; ≥ 3 independent mechanisms (Hard 4+); SD ≥ 0.10; < 5 full passes on the forecast. | Redesign; never build. |
| **3 S5f** | after the minimum build | ≥ 2 mechanisms land in valid 5.5 runs; no fallback; the keep/replace decision is written. | Replace mechanisms; max 2 cycles; switch scenario. |
| **4 Pre-check** | platform | Corrected proxy ≤ cap−5; ≥ 2 mechanisms in 5.5's own decisions; no fallback; `/hardness` ≥ 3. | One universe-side fix; second pre-check; then switch scenario. |
| **5 Baseline** | six runs | Six valid 5.5 runs; V3 average, SD, patterns and full-pass gates. | Harden the universe, never the rubric. |

**The `/hardness` caveat.** `/hardness` 3 is necessary, not sufficient. Rev14's pre-check scored 3 with zero designed landings. The go decision is the corrected proxy plus the mechanism count plus the provenance, not the reviewer's band.

## 6. Acceptance tests

| Test | Fixture | Assertion |
|---|---|---|
| T1 End-to-end | rev14 pre-check and r3 | Pre invalid; 0 designed landings; r3 ~91.8 with S01/S47/S49/S52/S54; two membership slips. |
| T2 CONTROL | rev14 pre-check | M2 is a control error, not LANDED; the go rule counts only LANDED. |
| T3 G1 exact slots | rev14 pre, r1, r2, r3, r6 | Exact failed-slot sets: pre S04/S05/S07/S08/S40; r1 S43/S46/S47/S52; r2 S04/S05/S07/S08/S38–S46; r3 S01/S47/S49/S52/S54; r6 S01. |
| T4 G1 r3 artifacts | rev14 r3 | 8-character SHA prefixes (S43/S44) and `slack_conversations_add_message` (S69–S71) pass; 86.7 → ~91.8. |
| T5 Budget gate | rev14 preregistration + synthetic | Rev14 design fails (E 72 % vs ≤ 62 %, P 0.297 vs ≥ 0.6); a synthetic design passes. |
| T6 Calibration | probe records | A 5.5 probe record is used; a 4.8 record needs a transfer; a missing model/harness/source is rejected. |
| T7 Variance | synthetic six-run matrix | At the cap boundary, the gates pass/fail on average, SD, patterns and full passes exactly. |
| T8 Run validity | fallback, pure, non-5.5 subagent | Fallback invalid; pure valid; non-5.5 subagent invalid. |
| T9 No rubric tuning | rubric hash | A hash change between pre-check and baseline blocks the verdict. |
| T10 B1 recovery | subprocess kill | Kill, resume; kill, roll back; already-applied; the gate-policy hash returns. |
| T11 B2 binding | rev13 vs rev14 SQL; two revisions | INSUFFICIENT/UNBOUND, never BOUND; per-run labels; gate rejects SINGLE. |
| T12 H2 A17 | ledger | Golden A17 value and records; `n_raw`/`n_eff`; mismatched profile flagged. |
| T13 M2 geometry | non-composable solver | UNVERIFIED plus a written disposition, not BLOCK; a missing disposition fails. |
| T14 M5 determinism | two `PYTHONHASHSEED` processes | Identical truth; a base-record value is checked through `hg.py records`. |
| T15 M7 defects | audit gaps | Each uncovered family has a planted case. |
| T16 Doc delta | staged docs | S0/S4/S5a/S5f/MODE B/gate 5 present after the merge. |
| T17 Final fingerprint | `tools/` after P1 | The fingerprint is recorded and matches the sandbox suite. |

## 7. Sequencing and effort

| Phase | Work | Effort | Exit |
|---|---|---|---|
| 0 | P0: B1, B2, H3, D3, D5, D6, MK | 1 session | Check-only ready; B1 recovery tests pass. |
| 1 | P1: G1, V1, H1, H2, M2, M5, M7 + A10–A18 | 1 session | End-to-end fixture; exact slot sets; final fingerprint. |
| 1.5 | Calibration battery: 8 probes × 3 Opus 5.5 runs | 1–1.5 days | Catalog v1: approved/weak/leaks. |
| 2 | Task 1: S0–S5a; portfolio; S5f | 2–3 days | Budget gate; 2 valid 5.5 runs; keep/replace. |
| 3 | Pre-check and baseline | Platform time | Gate 4 and Gate 5. |
| 4 | P2: F1, M6, L, M3, J, Lx | After task 1 | Forecast brackets the observed average. |

**The sequence change.** The current prompt does P0 → move → P1 and stops. This plan stages P0 and P1 together, moves once, then runs the battery before task 1's S5a. That ordering is deliberate: task 1's early runs wait for G1/V1 anyway, so the early move buys nothing, and a Hard portfolio sized before the battery repeats the rev14 theory-based design.

## 8. Risks and mitigations

| Risk | Trigger | Mitigation |
|---|---|---|
| Opus 5.5 defeats Tier A too | ≤ 1 mechanism approved in the battery | Lean on breadth (several independent cohorts), target Medium/Easy, and tell the project Hard may be infeasible on this universe. |
| Fallback contaminates runs | Any `model_refusal_fallback` | Theme screen; early stop after the pre-check or run 1; re-run only with a valid theme. |
| Grader bias | Aggregate score moves without slot changes | Exact slot sets; UNGRADED policy; disagreement queue; no rubric tuning. |
| Forecast over-credits | E[average] much lower than observed | Battery; profile-matched priors; F1 channels; treat the forecast as advisory until calibrated. |
| Harness parity | Platform vs harness differ > 10 points | Harness results gate nothing until parity is fixed. |
| Overfitting to Season Pass | Reused patterns or numbers | New archetype, new cohort, new outputs; the originality check in S1. |
| Governance override | A known-miss design proceeds | `budget_exception`; the four-condition gate; the kill/continue ledger. |
| G1 slips | P1 takes longer than P0 | G1a/G1b split; manual slot reads for the first 5.5 run. |
| Toolchain drift | P1 edits after the move | Stage P1; one move; final fingerprint. |

## 9. What not to do

- Do not claim frontier defeat from a 90 % task.
- Do not rely on a fallback-driven failure; V3 invalidates it.
- Do not tune the rubric or the verifier to manufacture a defeat.
- Do not enumerate rules in a hub-named document.
- Do not put a plain-words pointer to the deciding record in a record every run reads.
- Do not use a claim contradicted by per-item records the agent reads anyway.
- Do not use decoys or authorities every run reaches.
- Do not make an explicit per-record rule the main engine.
- Do not use forced errors or async waits as difficulty.
- Do not grade one fact in 3 or more rows.
- Do not use one hidden control for most of the weight.
- Do not pool models in the priors.
- Do not use a forecast without provenance.
- Do not skip the battery and call the result calibrated.

## 10. Deliverables

1. **Updated `Implementation_Session_Prompt_Fixes.md`** with Appendix A below.
2. **New tests and fixtures** for T1–T17, including the end-to-end rev14 fixture.
3. **A calibration battery prompt** (separate session): 8 probes, 24 runs, catalog v1.
4. **Task 1 design brief** with the portfolio, weights, priors and forecast.
5. **The readiness table** and the final fingerprint.
6. **The report**, with the per-row evidence, the deviations, the open issues, and a "what this does not prove" section.

## 11. Decisions for you

1. **Calibration timing.** Run the battery before task 1's S5a (recommended), or proceed on theory priors with a signed risk acceptance.
2. **Task 1 mode.** Hard (needs the battery; 5 % of tasks), or Medium/Easy (can start sooner; the same tools and the same gates).
3. **P1 staging.** Stage P1 with P0 and move once (recommended), or move after P0 and edit live.
4. **Budget gate.** Blocking, or a written `budget_exception` with the reason and the requester.
5. **Ledger pooling.** Per model, with source tags and one owner; still open from `Learnings…` §6.

## Appendix A — copy-paste additions to `Implementation_Session_Prompt_Fixes.md`

Add these to the existing prompt. They do not replace its P0/P1 rows.

### A. Scope and sequencing

- Stage P0 **and** P1 in `support/pending_edits/` and `support/pending_tools/`; move once; take the final fingerprint after P1.
- Add the end-to-end rev14 fixture (T1) to P1's acceptance.
- Add the calibration gate: no Hard design before the Opus 5.5 battery, unless a written risk acceptance is recorded.
- Add the design-budget gate: E ≤ cap−8, P ≥ 0.5, ≥ 3 independent mechanisms (Hard 4+), SD ≥ 0.10, < 5 full passes.

### B. Per-row additions

- **B1:** add a real subprocess kill/resume/rollback test via a fault-injection hook; test the three check states.
- **B2:** test the gate rejects unchecked SINGLE; test a two-revision batch labels each proposal; test INSUFFICIENT and UNBOUND separately.
- **G1:** assert the exact failed-slot sets for pre/r1/r2/r3/r6, not aggregate percentages; assert the r3 8-character prefixes and the Slack alias.
- **V1:** add a per-run provenance table (model, fallback event, brief writers, deciding event, valid/invalid); add a non-5.5 subagent fixture and a fallback-event-removed fixture with 5.5 calls.
- **H1:** add **CONTROL** as a verdict; test the rev14 pre-check outputs 0 designed landings and M2 is a control error; compare landed-key sets.
- **H2:** add `evidence_profile`; mismatched profile = flat or `TRANSFERRED · MISMATCHED`; print `n_raw`/`n_eff`; golden A17 value.
- **M2:** require a written disposition when U is UNVERIFIED; a missing disposition fails.
- **M5:** run two subprocesses with different `PYTHONHASHSEED`; check a base-record value through `hg.py records`.
- **M7:** add a case for each audit gap.
- **MK:** record the `--allow-max-k` disclosure in the output JSON and the pre-registration.

### C. New report sections

- **Hardness value:** for each row, say whether it is Direct, Enabling, Protective or Ops, and why.
- **What this does not prove:** the toolchain is ready; the next task's difficulty is unproven until the battery and S5f.
- **Readiness table:** S0–S5a, S5f, pre-check, baseline: ready/blocked and the dependency.
- **Residual risks:** the top five, with the trigger and the owner.

### D. New tests

- **T1 End-to-end rev14:** pre invalid, 0 designed landings, r3 ~91.8, exact slots, two membership slips.
- **T2 CONTROL:** SP-110 is CONTROL, not LANDED.
- **T3–T4 G1 exact slots and r3 artifacts.**
- **T5 Budget:** rev14 design fails; synthetic passes.
- **T6 Calibration:** 5.5 probe record; 4.8 needs transfer.
- **T7 Variance:** synthetic six-run matrix at the cap boundary.
- **T8 Run validity:** fallback invalid; pure valid; non-5.5 subagent invalid.
- **T9 No rubric tuning:** hash change blocks.
- **T10–T17:** B1 recovery, B2 binding, H2 A17, M2 geometry, M5 determinism, M7 defects, doc delta, final fingerprint.

### E. The one-sentence addition to the goal

> This session makes the measurement trustworthy.
