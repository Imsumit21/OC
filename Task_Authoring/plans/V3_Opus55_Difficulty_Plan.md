# Making Opus 5.5 fail validly under V3: what we lack, and the plan

Written 2026-10-25, after the Season Pass task was skipped and the Phase 0–1 implementation audit finished. For every
contributor building V3 tasks.

Evidence labels: **[O]** observed (measured or read), **[D]** derived, **[I]** inference or estimate.

Sources:
- `references/Docs/11_V3_Changes.md`: the V3 rules;
- `references/Hardness_Mastery.md` §0, §9 and §11: the measured mechanism library;
- `plans/Rev13_Results.md` and
  `support/backtests/season_pass/rev14/working_files/rev14_platform_runs/Rev14_Precheck_Findings.md`
  (Season Pass revisions 13–14);
- `support/audit/phase0_1/AUDIT_REPORT.md`: the tools audit;
- `plans/Fold_Hardening_Into_Scenario_And_Injection.md`: the tool plan this builds on.

## 0. In brief
**Diagnosis.**
- **Difficulty that a frontier agent defeats.** We build difficulty as "things the agent won't find or won't apply",
  then incorporate them, for fairness, so explicitly that the agent runs them as a checklist.
- **What Season Pass showed.** Opus 4.8 read every pointed record, applied every stated rule, followed every pointer and
  resisted every decoy and claim. The designed mechanisms landed only where the Opus 5 fallback took over. Pure Opus 4.8
  runs scored about 90–100 %.
- **What's missing.** Measurement on the target model before building, a fair source of difficulty, variance
  engineering, trustworthy grading, and run-validity control. **[O]**

**Opportunity.** V3 caps depend on the mode: Easy below 90 % (about 30 % of tasks), Medium below 85 % (about 65 %),
Hard below 70 % (about 5 %). Most tasks need 10–15 points of loss, not the 30 Season Pass needed. **[O]**

**Plan.**
1. **Calibrate first.** One shared Opus 5.5 probe battery measures the strongest mechanism families on this universe
   and harness, before anyone builds a full task. Meanwhile, the first task calibrates itself through early harness
   runs.
2. **Design to the mode's loss budget.** Use measured landing rates × weight, three or more independent mechanisms on
   separate outputs, and difficulty that lives in judgment and synthesis, not in hiding.
3. **Build the minimum, measure early, and stop by rule.** At most two pre-checks per scenario, then switch scenario.
4. **Fix the tools.** Clear the audit blockers, harden the grader, and keep one shared ledger, so every contributor's
   runs improve everyone's priors.

## 1. What Season Pass taught us
| Revision | Model | Corrected average | What landed | What failed |
|---|---|---|---|---|
| 10 (platform baseline) | Opus 4.8 | 84.69 % raw (V2 matrix) | the issue remap in one run (0 of 8 briefs carried the rule) | remap, row association |
| 13 | Opus 4.8 | 92.1 % proxy, SD 0.068, 1 of 6 full passes | 3 rules, once each; two in fallback runs | slips, about 1 wrong row in 128 per run |
| 14 | Opus 4.8 (fallback to Opus 5 in 4 of 5 runs) | about 90 % over 4 baseline runs (92.2, 76.1, 91.8, 99.6); pre-check 90.2 % | M1 and M2 only through Opus 5 decisions; M3 and M4 never | Opus 5 briefs and Opus 5 classification |

All of this is **[O]**.
1. **Retrieval is complete on the main path.**
   - Every revision-13 run read all of these: validation comments (330–338 of 338), PR comments (302), reviews (265),
     timelines (944), PRs (128), and every source the hub names.
   - Revision 14 read 344 of 352 Linear comments.
   - The "half the runs never look" levers didn't exist on this task.
2. **Explicit rules leak.** Seven rule families leaked in every revision-13 run. Rules written into a hub-named
   document became worker checklists.
3. **Pointers are followed.** A plain-words pointer in the tracker description sent Opus 4.8 to the comments within 26
   events.
4. **Lists the agent compiles itself come out exact,** including value notes and process findings.
5. **Claims and decoys lose to the records:** T39 export 0 of 7, the revision-10 decoys 0 of 6, the confident claim 0
   of 5.
6. **What did cost points:**
   - slips at scale, where one class error cascaded to about 8–10 points through the aggregates;
   - tool-surface friction: the native-Sheet substitution in 5 of 12 runs;
   - in revision 14's four fallback runs, every traced failure was decided by the Opus 5 fallback;
   - one rule slip in the only pure Opus 4.8 revision-14 run: "count under every condition" on two keys.
7. **The forecast was miscalibrated.** Pre-registered E[average] was 72 %; observed was about 90 %. "At least one
   landing" was predicted at 0.72 and didn't happen.
8. **The proxy grader was wrong.**
   - Eight decoder defects on real revision-14 outputs. One defect was introduced in the corrected copy and fixed
     during the analysis.
   - The defects moved one run by 20 points.
   - The pending `surface_grader.py` carries the first four.
9. **Run validity broke.** A "bio" safety false positive switched the main agent to another model in 8 of 12 platform
   runs. On V3, every pre-check and baseline run must be Opus 5.5, so such a run is invalid.

## 2. What we lack, and where it gets fixed
| Lack | Consequence | Fix |
|---|---|---|
| Target-model measurement before building | 14 revisions designed from theory; findings arrived only after platform runs | §6 probe battery; §7 step 3 early runs |
| Fair difficulty that survives complete retrieval | Mechanisms leak once incorporated | §4 principles, §5 portfolio |
| Variance engineering | One population with cascading aggregates gives correlated, low-SD outcomes | §3 budget, §7 step 2 |
| Grading fidelity | Steering difficulty with a broken thermometer | §8 T4 |
| Run-validity control | Fallbacks contaminate runs | §7 step 0 theme screen; §8 T8 |
| Mode awareness | Designing every task like Hard | §3 |
| Shared priors and kill rules | Every contributor rediscovers the same leaks; revisions never stop | §9; §7 step 5 |
| Tools ready to move | Audit: READY AFTER FIXES (B1, B2, H3) | §8 T1–T3 |

## 3. The V3 target as a design budget
| Mode | Share | Cap (strict) | Minimum average loss | Design target E[average] | Typical portfolio |
|---|---|---|---|---|---|
| Easy | ~30 % | < 90 % | > 10 points | ≤ 82 % | 2–3 independent mechanisms; about 30 % of weight at risk |
| Medium | ~65 % | < 85 % | > 15 points | ≤ 77 % | 3 mechanisms; about 40 % of weight at risk |
| Hard | ~5 % | < 70 % | > 30 points | ≤ 62 % | 4–5 mechanisms; 55–70 % of weight at risk |

**Other gates:**
- Opus 5.5 for the pre-check and all six runs;
- fewer than 5 full passes;
- at least 2 failure patterns, the largest at most 50 %;
- errored runs unchanged from V2;
- the local per-run SD band of 0.10–0.30;
- horizon: Long-Horizon (85 % of tasks) needs at least 100 calls, Normal at least 50;
- the human-time tier;
- the assigned universe date: October 1, 2025 for 75 % of tasks.

**Arithmetic.** Use these to set the portfolio. **[D]**
- **Expected loss** ≈ Σ (mechanism weight × landing rate), plus slips (about 2–5 points on a large cohort).
- **At-risk weight.** With weight W at risk, failing at a weighted mean rate p̄, and the rest passing at r (about 0.95
  with slips), E[average] = r(1 − W) + (1 − p̄)W. Hard's 62 % target needs W ≥ 73 % at p̄ = 0.5 (76 % at r = 1), or
  about 55 % at p̄ = 0.65. Two-thirds of the weight at p̄ = 0.5 gives 66.7 % (65.0 % at r = 95 %), which clears the
  cap but misses the target by 4.7 points with a perfect remainder, or 3.0 with a 95 % remainder. The table's
  "typical" column assumes p̄ of about 0.5–0.65.
- **Margin.** The design target sits about 8 points under the cap, roughly two standard errors of a six-run mean at
  SD 0.10.
- **Spread.** k independent mechanisms of weight w, landing at rate p, give a per-run SD of about w·√(k·p(1−p)).
  - Medium, 3 × 13 % at p 0.5: SD ≈ 0.11, inside the band.
  - Easy tasks need wider weights or more variance to reach SD 0.10.
  - The gate reads the population SD of the six runs. Under an IID normal approximation σ = 0.10 lands in band about
    30 % of the time, so an interior σ ≈ 0.15–0.20 is a model-motivated candidate; it is not a validated requirement,
    and σ alone does not determine the six-run SD (mixtures and correlated channels defeat it). Read the forecast's
    P(SD in band) computed on the actual rubric rows, with covariance. Near-certain rows add loss but no spread.
    Equal independent channels at p̄ = 0.5 illustrate the arithmetic (W_v ≈ 0.32√k); never transfer a channel count.
- **Full passes.** P(a run passes everything) ≈ Π(1 − p) × P(no slip). Two mechanisms at 0.5 already make five full
  passes negligible.

## 4. Design principles for Opus 5.5
1. **Put the difficulty in reasoning and synthesis, not in finding.** V3: "Keep the real difficulty in the work and the
   universe." Assume Opus 5.5 opens every record a reasonable worker would. **[O]/[I]**
2. **Incorporate by role, not by location.**
   - The prompt and the records name what governs ("the refund policy", "the vendor's latest reply"), reachable through
     ordinary multi-hop paths, which V3 allows.
   - Never enumerate rules in a hub document; never write answer-key clauses or trap hints (V3 §8).
3. **Every mechanism must survive complete retrieval.** The failure has to come from a judgment the agent makes:
   deferring to a confident summary, stopping at the apparent conclusion, choosing the plausible authority, dropping an
   eliminating fact in the write-up, not computing a comparison the request implies, losing a detail in synthesis.
4. **Use independent mechanisms on separate outputs.**
   - One hidden control gating most rows makes runs bimodal (SB-T2: 2, 4, 3, 2, 54, 2 of 54), which fails the pattern
     and SD gates.
   - Use 3 or more independent ones; Hard tasks need 4 or more.
5. **Collect slips naturally, never through duplication.**
   - Exact derived values over a real cohort, and per-record outputs that can't cancel, catch slips.
   - Never grade one fact in three or more rows (V3).
6. **Make the deliverable carry the load.** Ask for outputs that must hold many specific per-item facts, such as values,
   dates, owners and outcomes, gathered across many records. Synthesis is where the Opus 5 fallback lost items in
   revision 14 (A20).
7. **Use a realistic tool surface.** Choose evidence the obvious bulk call doesn't return: thread replies, later pages,
   attachments. Measure this on the real tool surface, never assume it (A3, A14).
8. **Protect run validity.** No bio-adjacent themes (zombies, infection, outbreaks, contamination). Check every
   pre-check for fallback events. **[I]** The trigger is suspected, not proven, but the cost of a contaminated V3 run
   is a re-run.

## 5. Mechanism portfolio
Every measured number below is Opus 4.8, except A1, whose model label is uncertain (audit L5). Nothing is calibrated on
Opus 5.5 yet; §6 measures it.

**Tier A: build on these, once calibrated**

| Mechanism | V3-fair form | Graded on | Evidence |
|---|---|---|---|
| A1 + A14: a confident early summary, with the thread continuing past it | A colleague's confident status message early in a thread the work leads to; later replies in the same thread overturn a decisive fact; nothing hints | the overturned facts in the deliverable | pass@1 0/6, best 18/31 |
| A4: a chain of eliminating facts | 4–6 facts across hops, each ruling out the obvious alternative; the request asks for the conclusion in ordinary words | the conclusion, and each eliminated alternative as its own fact | averages 47 % and 52 % |
| A9: response pairing | Every item in scope has a later reply from the other party; some reverse the answer | per-item outcomes (at most 5 samples) plus an exact count | 4/5 missed the reversing reply |
| A12: the authority where its owner keeps it, a plausible older version where people look first | The prompt names the policy by its everyday name; the current version is in its natural home (a Trello card or handbook), an older one in Confluence or Slack; dates and ownership decide | outputs the policy governs | SB-T2 0.21 (5/6 latched on the decoy); SB-T3 0.40 |
| A3: tool-surface blind spot | The obvious bulk read doesn't carry the evidence; the right call does | items whose evidence lives only there | 44.1 % (author-reported) |
| A19: a derived comparison the request implies | "How does this compare with last quarter / the plan?" | the derived numbers | retrieved 5/6, never computed 6/6 |
| A20: synthesis load | The deliverable must carry many per-item facts that subagents gathered | samples plus a volume row | 6/6 and 4/6; revision 14 (Opus 5) dropped items in 2 of 5 runs |
| A15: a house rule against the natural reading, applied per record | The rule lives in the team document the work needs, written as normal prose, not in a hub checklist | per-record outcomes | V7-T1 4–5/6; Season Pass, hub-enumerated: 0/7 |

**Tier B: supporting**
- **A2: exact derived totals over a large cohort.** Collects slips: in revision 13 the HOLD total failed in 4 of 6 runs,
  and the READY total and the review group in 3 of 6, on 128 records.
- **A17: a cohort boundary no keyword marks.** 3/6.
- **A16: a conflict the request asks to be flagged.** 5/6 on V7-T1. Phrase it as an ordinary ask, never an answer-key
  clause.
- **A21: per-surface format rules in an incorporated source.**

**Don't build on these** (`Hardness_Mastery.md` §9; Season Pass):
- rules enumerated in a hub-named document;
- decoys and authorities every run reaches;
- claims contradicted by records the agent reads per item;
- explicit pointers to the deciding record;
- forced errors and async waits;
- ACL-only difficulty;
- RETIRED drafts;
- unincorporated rules;
- repeated framings ("Actually…", "go by the doc", "don't trust the summary", shutdown backdrops);
- stricter or duplicated rubric rows.

**Archetypes where several Tier-A mechanisms arise naturally.** Match one to the role and vary across the batch.
- **Vendor or partner dispute reconciliation:** A9, A4, A19 and A20.
- **Incident or launch retrospective from long threads:** A1 + A14, A4 and A3.
- **A policy-governed release or refund decision over a cohort:** A12, A15 and A2.
- **Budget or KPI variance review:** A19, A17 and A20.
- **Partner or contractor onboarding audit:** A20, A9 and A21.

## 6. Calibration first: the Opus 5.5 probe battery
**Why.** Every landing rate we hold is Opus 4.8. One week of shared measurement replaces months of per-task guessing.

**What a probe is.**
- **Coverage.** 8 probes, one Tier-A mechanism each: A1 + A14, A4, A9, A12, A3, A19, A20 and A15.
- **Shape.** A small realistic request (Normal tier, 50–100 calls) on the October 2025 universe, with 3–6 graded facts.
- **Build.** A seed of at most about 60 rows, a solver, and grading by the hardened `surface_grader`.
- **Runs.** 3 Opus 5.5 runs each in the independent harness, configured like the platform: Claude Code version, effort
  and subagent policy. That is 24 runs.

**What it measures:**
- per-mechanism landing (k of 3), with its model context;
- fallback events by theme;
- call counts;
- subagent fan-out and brief content;
- synthesis loss.

**What it produces.**
- **Priors.** Beta records in the ledger (`claude-opus-5-5`, the harness, `source: probe`).
- **A catalog.** *Approved* at 2 or more of 3, *weak* at 1 of 3, *leaks* at 0 of 3.

  Forecasts credit only approved and weak mechanisms.

**Harness parity.** Run the first real task's pre-check on both the platform and the harness. If they differ by more
than 10 points, or land different mechanisms, harness results gate nothing until the parity issue is fixed (tool plan
§15.6).

**Cost.** **[I]** About 2–3 authoring days on a shared template, and 1 day of parallel runs.

**Fast path for task 1.** It shouldn't wait for the battery:
- design with 5–6 candidate mechanisms, one or two of them spares;
- run 2 Opus 5.5 harness trajectories on the first full build before `/injection`;
- keep what lands and drop what leaks.

## 7. Workflow for every new task
0. **Intake.**
   - Read the assignment: mode, which sets the budget (§3); universe date; role plausibility; horizon tier.
   - Screen the theme for safety false positives.
   - From the next task, V3 local certification runs as designed: model-provenance checks apply and are never N/A.
1. **Scenario.**
   - Pick an archetype (§5) where at least three Tier-A mechanisms come from the role's real work.
   - Check every fact in Universe Explorer.
   - Vary framings across the batch.
2. **Portfolio and geometry.**
   - Use at least 3 independent mechanisms on separate outputs; Hard needs at least 4.
   - Weight by kind of work: 1, 3 or 5.
   - **Forecast.** Use Opus 5.5 priors. Until the battery reports, use Opus 4.8 priors transferred at quarter weight and
     discounted by half.
   - Require E[average] ≤ cap − 8 and P(all gates) ≥ 0.5, or redesign before any SQL.
   - This uses the forecast only to reject, and only on the loss channels it models. The forecast is advisory until
     calibrated (tool plan §10 Phase 2), and its known error on trap landings is optimistic (revision 14: 72 % forecast,
     about 90 % observed). A design that misses even this forecast is redesigned, not built.
   - Loss from scale, dependency chains and delegation counts once the forecast models it (F1, now P1). Until then it is
     measured in the early runs (step 3), and a design that meets the forecast still has to land its mechanisms there.
3. **Minimum build and early runs.**
   - Seed the mechanism records and their context.
   - Run 1–2 Opus 5.5 harness trajectories and analyze them with the post-move tools.
   - Keep channels that fail in Opus 5.5's own decisions (designed mechanisms or declared complexity channels); replace
     leaks. At most two cycles.
4. **Full build.** Injection with every gate (solver, preflight, dispositions), then `/injection` and `/prompt`.
5. **Pre-check (platform, Opus 5.5) and `/hardness`.**
   - **Before the pre-check:** the prompt review's ground-truth forks are settled, and the surface↔grader dry-run
     (`surface.gradeable`) reports no ungradable slot. A pre-check graded on an ambiguous prompt or an undecodable
     surface is not evidence about difficulty.
   - **Go** only if all four hold:
     - `/hardness` is 3 or more;
     - the corrected proxy is at most cap − 5;
     - at least 2 independent pre-registered loss channels failed in Opus 5.5's own decisions: designed mechanisms
       that landed, or declared complexity channels (scale, chain, delegation) that failed. Control errors and
       unattributed slips count for neither;
     - the run is valid: every message from Opus 5.5.
   - **Otherwise** make one universe-side fix and run a second pre-check.
   - **Kill rule:** if the second pre-check also misses, switch scenario. Never more than two pre-checks per scenario.
6. **Baseline.**
   - Six Opus 5.5 runs, with the OEs and rubric written in parallel.
   - Run the V3 fairness pass on every low-pass row before judging difficulty. The course found about 70 % of low-pass
     rows were fair misses and about 24 % author faults.
   - Then the verifier, corrections, difficulty and release. If the corrected average is at or above the cap, make the
     universe harder, never the rubric stricter.
7. **After the task.** Record the intake and baseline in the shared ledger, update the catalog, and hold a 15-minute
   retro.

## 8. Tool work, in order
| # | Work | Accept when |
|---|---|---|
| T1 | Audit blockers. B1: the move gets backups, a journal, resume, rollback and "already applied". B2: evidence-based binding with an explicit INSUFFICIENT outcome, and each run's own revision label. H3: self-tests in temp folders, with cache writers sandboxed | the audit's smallest fixes are in, each with a planted-failure test |
| T2 | Decisions (§12): deviations 3, 5 and 6; 9a; max-k | recorded in the tool plan's change log |
| T3 | The move (P1 is met: Season Pass is skipped) | check-only says "ready", the move runs in a maintenance window, fingerprints are taken before and after, and every self-test passes in a sandbox |
| T4 | Grader hardening. The eight decoder defects: first-mention headings; sections ended by intros or table headers; JSON-escaped text; last-update-only; bullet key lists; group detection on intro prose; tool aliases (`slack_conversations_add_message`); SHA-prefix length. Add a format-fixture suite from all 12 Season Pass runs; unparseable content returns UNGRADED, never false | revision 13 reproduces exactly; revision-14 grades match the manual readings (90.2 / 92.2 / 76.1 / about 91.8 / 99.6 %) |
| T5 | Audit H1/H2. An unreproduced error inside a cohort is "mechanism?", not the rule; one trial per (task, revision, run, family) | the audit's planted cases pass |
| T6 | Forecast channels: synthesis loss, control over-application, tool-surface substitution, and base slips scaled to population size. A fallback is a validity flag, never a lever | the Season Pass revision-14 posterior replay brackets the observed about 90 % |
| T7 | Ledger. Seed Season Pass revision 14, with landings decided by the fallback labelled `claude-opus-5`, and then the probe battery. Write a merge procedure for contributors' ledgers | priors print per model with their record ids |
| T8 | Intake. Any non-Opus-5.5 message flags the run as invalid for V3 and recommends a re-run | planted fallback fixtures are caught |
| T9 | Optional. An LLM-judge cross-check of text rows (`PROBE_*` environment), reconciled with the deterministic grader | the two agree on the Season Pass fixtures, or every disagreement is explained |

## 9. Team protocol
- **One shared ledger and mechanism catalog,** with one owner. Every contributor appends intake records after each
  pre-check and baseline. Records are content-addressed and merge idempotently; pooling CB data is a policy decision.
- **Pre-register every task's forecast** before its first run, and score it after the baseline. Calibration improves for
  everyone.
- **A 30-minute design review before any SQL.** It covers:
  - the mode budget;
  - the portfolio with its priors;
  - the fairness of each incorporation path;
  - the theme screen;
  - the archetype and framing variety across the batch.
- **Rubric discipline.** Never tune rubrics to runs: fix unfair rows first, then make the universe harder.
- **A fallback log.** Every run's model provenance; themes that trigger fallbacks are avoided.

## 10. The next ten working days
All estimates are **[I]**.

| Days | Track 1: tools | Track 2: calibration | Track 3: task 1 |
|---|---|---|---|
| 1–2 | T1–T3, then T4 | author the 8 probes | intake, scenario, portfolio (transferred priors) |
| 3–4 | T4–T5 | 24 Opus 5.5 probe runs; T7 priors | minimum build; 2 early harness runs; prune |
| 5–6 | T6, T8 | catalog v1 | full build, `/injection` and `/prompt`, pre-check, `/hardness`, harness-parity check |
| 7–9 | T9 (optional) | refresh priors from task 1 | baseline, OEs and rubric, fairness pass, verifier, difficulty, release |
| 10 | retro | catalog v2 | ledger update, plan revision |

## 11. Risks and open questions
- **Opus 5.5 may defeat Tier A too.** If the battery approves at most one lever, Hard is still built: an assigned mode
  is never downgraded or skipped (your decision, 2026-10-25). Escalate the scenario and the injection instead:
  - several independent cohorts of 40 or more members with exact derived values. An exact total over N members at
    per-member error e fails with probability 1 − (1 − e)^N when member errors are independent: about a third to
    two-thirds of runs at N = 40–60 and e = 1–2 %. Shared causes give less, and sampled members fail at about e;
  - dependency chains, where a graded fact needs several upstream judgments (three 20 % risks compound to about 49 %);
  - delegation load and dependent writes across services, with synthesis graded through samples and volume rows.

  Every escalation stays V3-fair (findable, incorporated, no impossible row: a predicted all-fail on the four Evals
  bases blocks at any count) and is measured in the early runs. A row that fails all six runs is legal when VALID,
  with a step-14 justification; spread comes from the SD and pattern gates. A run that errors out counts against
  validity, not toward difficulty.
- **Harness parity is unmeasured.** Until the parity check, harness results are advisory.
- **Fallback on Opus 5.5 is unknown.** A fallback run is invalid for V3; plan for re-runs.
- **Easy tasks and the SD band.** Their small budgets make SD ≥ 0.10 harder to reach; check the forecast's SD, not just
  its mean.
- **A1's evidence is weak.** Its "Opus 5.5" figure has an uncertain model label.
- **Cost.** About 30 extra Opus 5.5 runs in the first week; you have said cost is not the constraint.

## 12. Decisions for you
**Decided 2026-10-25** (`plans/Learnings_And_Improvements_2026-10-25.md` §1):
- **Item 1:** the battery runs alongside task 1.
- **Item 2:** all five accepted as recommended.
- **Item 3:** after the code session's P0 fixes, in a maintenance window.
- **Items 4–5:** open. The merge procedure is built either way, and nothing is pooled until you say yes.
- **Hard stays Hard** (added the same day): never downgraded or skipped. If traps land too rarely, escalate the
  scenario and the injection (§11).

My recommendation came first in each.
1. **The probe battery.** Approve it, run in parallel with task 1. The alternative is calibrating only inside tasks.
2. **The audit decisions:**
   - **Deviation 3:** implement `surface.coverage` as a real, tested check (audit M1).
   - **Deviation 5:** restrict rule-placement flags to A15 nodes, as the plan says.
   - **Deviation 6:** keep `surface.valid` blocking for structure only, with geometry advisory.
   - **Criterion 9a:** record it as not met in 2 of 12 scenarios, and name the headline scenario in advance next time.
   - **max-k:** keep the default of 8, with an explicit, disclosed override.
3. **Move timing.** Right after T1, in a window when no other session runs gates.
4. **Ledger pooling** across contributors: yes, per model, with source tags.
5. **An owner** for the shared ledger and catalog.
