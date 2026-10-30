# Season Pass — revision 14 (last iteration)

You are taking the HarmonyGames task "Season Pass engineering transfer" to revision 14:
- persona: Oliver Brooks, Senior Game Engineer;
- freeze: 2026-02-14T00:00:00Z.

This is the last iteration. If revision 14 does not make Opus 4.8 fail validly on the platform, the task is dropped.
Spend the effort on the mechanisms that make runs fail, not on polish.

## 0. Goal and acceptance
The platform runs this task on Opus 4.8. I haven't confirmed whether it grades with the V2 or the V3 Hard gates, so
design for both at once:

| Gate | Requirement | Design target |
|---|---|---|
| Six-run average (corrected) | < 70 % (V3 Hard); V2 needs < 75 % | ≤ 62 % |
| Full passes | ≤ 3 of 6 (V2); V3 needs < 5 | ≤ 1 |
| Per-run SD | 0.10–0.30 | about 0.15 |
| Failure patterns | ≥ 2, largest ≤ 50 % of failing runs | ≥ 3 |
| All-fail rows | none predicted (local tolerance 0; `/rubric` fails two or more) | every slot passable, and P(fails in all 6 runs) ≤ 0.25 |
| `/hardness` on the pre-check | score ≥ 3: a consequential failure, meaning something wrong, missing or misdirected | ≥ 2 mechanisms land in one run |

Validity is not negotiable:
- every graded requirement is incorporated;
- every fair reading is accepted;
- no new coherence defect is introduced;
- `/injection` and `/prompt` pass;
- Oliver can reach every load-bearing record.

## 1. Local certification mode
`00_Assigments.md` is a V3 assignment (Hard, Opus 5.5), but the platform runs this task on Opus 4.8.
- **Model checks are N/A.** These checks can never pass on Opus 4.8 runs. Report each as "N/A: V2 task on Opus 4.8",
  keep its literal output, and never relabel it PASS:
  - `v3.precheck_model`: the hardening gate runs it only when `06_PreCheck_Trajectory/trajectory.json` exists, and
    release always runs it;
  - `baseline_models` in the V3 difficulty view. The `difficulty` stage only requires the calculator lines pasted
    verbatim, so it can still PASS;
  - at release, also `release.precheck_trajectory` (it needs `trajectory.json`) and `release.difficulty` (it needs no
    blocking gate, and `baseline_models` always blocks). `release.difficulty` is N/A only while `baseline_models` is
    its sole blocking gate.

  So local release is "not certified: V2 task on Opus 4.8". Every other release check must PASS.
- **Pre-check file name.** I save the pre-check as `06_PreCheck_Trajectory/trajectory-run-1.json`, so the hardening
  gate can still be re-run after the pre-check. Don't rename or copy it to `trajectory.json`.
- **Difficulty.** Build two matrices from the same verifier results:
  - `Working_Files/12_difficulty_input.json`: the V3 matrix, built with `--task-dir`. The `difficulty` stage re-runs
    it.
  - `Working_Files/hardening_rev14/12_difficulty_input.v2.json`: the V2 matrix, built with `tools/difficulty_stats.py
    --build --legacy-v2 --task-type "Long Horizon" …` and computed with `--legacy-v2`.

  Report both verdicts. Until I confirm which one the platform applies, a FAIL on any numerical difficulty gate
  (errored runs, pass@1, average, SD, failure patterns, horizon) under either view is a design failure. The N/A
  provenance checks above don't count.
  `--legacy-v2` refuses a V3 matrix, so keep the two files separate.
- **Don't work around it.** Don't edit `00_Assigments.md` or `00_Task_Context.json`. Certify every stage whose checks
  don't depend on run provenance.

## 2. Rules
- **Workspace.** The root is `/Users/sumitkumar/Source/Outlier/OC`. Read `Task_Authoring/setup/GEN_EXECUTION.md` first;
  it binds. In short:
  - write only inside `Task_Authoring/`;
  - `Evals/`, `claude/` and `HarmonyGames_*` are read-only, and you never run git inside them;
  - never execute SQL;
  - never fabricate or estimate platform outputs.
- **Task folder.** `Task_Authoring/task_inputs/`. `Working_Files` is a symlink to
  `Task_Authoring/task_inputs/Audit-Report/Working_Files`.
- **Preserve history.**
  - Before you first overwrite any file in `task_inputs/`, copy it into `Working_Files/hardening_rev14/before/`.
  - Start with:
    - `01_Universe_Inject.sql` and `Working_Files/01_Universe_Inject.comment-free.sql`;
    - both manifests, the dossier, `01_Scenario_Design.md` and `01a_Hardening_Report.md`;
    - `04_Prompt.txt`, `00_V3_Authoring_Evidence.json`, `04_Prompt_Writing_Brief.md` and `04_Prompt_Check.md`.
  - Copy the 05/08/09/10/11/12 files the same way before replacing them.
  - `Working_Files/hardening_rev14/` doesn't exist yet. Create it, and put every revision-14 script and output there.
- **Frozen revision 13.** `Task_Authoring/support/backtests/season_pass/rev13/` is read-only; read its `README.md`
  first. It holds the revision-13 SQL, runs and reference outputs, and copies of `hardening_rev11–13/`.
- **Historical scripts write fixed live paths.** Never run any script in place under the `Working_Files/` root,
  `hardening_rev11/`, `hardening_rev12/`, `hardening_rev13/` or `injection_fix_20261024/`:
  - `hardening_rev12/build.py` and `hardening_rebuild.py` overwrite the live SQL and manifest;
  - `report.py` and `hardening_report.py` overwrite the dossier and `01a_Hardening_Report.md`;
  - `coverage.py` and `verify.py` overwrite their own outputs, computed from whatever SQL is live.

  Never import `hardening_intake.py`: it writes into `hardening_rev11/` on import. Import only `oracle.py`,
  `hardening_analysis.py` and `precheck_probe.py` as libraries. To reuse anything else, copy it into
  `hardening_rev14/` and adapt the copy.
- **Don't modify:**
  - `hardening_rev11/`, `hardening_rev12/`, `hardening_rev13/` and `injection_fix_20261024/`;
  - the root `Working_Files/*.py` scripts;
  - `rev13_platform_runs/` and `Plateform_reports/`;
  - `task_inputs/06_*` and `07_*`, where I place runs;
  - `Task_Authoring/support/backtests/`;
  - existing files in `Task_Authoring/support/analysis/` (you may add new files there).
- **Parallel session.** Another session is building new tools in `Task_Authoring/support/pending_tools/`, staged edits
  in `support/pending_edits/` and fixtures in `support/fixtures/`. Ignore those folders. Don't edit any file in `tools/`:
  the gate certificates hash every `tools/*.py`. Helper caches under `support/local_search/` are shared: don't delete,
  rebuild or refresh them, and don't run `setup/local_search.py`.
- **Keep fixed:** the persona, the assignment, the freeze, the prompt's goal and the deliverables.
  - Keep `04_Prompt.txt` byte-identical (sha256 `4f530d031be23b81defc5a44162e679861ed3be7fc9783a74963650f6ea05d55`).
    It reads: "can you finish Arthur's Season Pass handoff for me, the Zombie Match 3D engineering transfer? follow
    the handoff instructions and get the complete register, review slide and tracking issue done. send Arthur the
    register and reply on the handoff thread once it's sent."
  - If a mechanism truly needs prompt support, stop and ask me, with exact wording.
- **Ask me before:**
  - changing the prompt;
  - deleting a record or rewriting what an existing record means;
  - any decision these instructions don't settle.
- **Evidence labels.** Use **[O]** observed, **[D]** derived and **[I]** inference in reports.

## 3. Read first
1. `Task_Authoring/plans/Rev13_Results.md`: revision 13, measured.
2. `Task_Authoring/task_inputs/Plateform_reports/`:
   - `6ad576cdef355e00e72cd8b2_1a_hardness.md`: `/hardness` on the revision-13 pre-check, score 2. Its §7 gives two
     revision ideas; M3 below uses both.
   - `Latest_injection-report.md` and `Latest-prompt-report.md`: both passed revision 13. Read their advisories.
   - Skim every earlier injection and prompt report for finding classes. None may come back.
3. The snapshot's `reference/attention_map.json` and `reference/attribution.json`.
4. `Task_Authoring/plans/Fold_Hardening_Into_Scenario_And_Injection.md` §6, §14.3 and §15.5.
5. `Task_Authoring/references/Hardness_Mastery.md` §0, §2.6, §3, §4, §6, §7, §8, §9 and §11.
6. Playbooks and references:
   - playbooks `01_Scenario_Design.md`, `01_Universe_Injection.md`, `01a_Hardening.md`, `04_Prompt_Writing.md`,
     `05_Human_Time_Estimate.md`, `08_Oracle_Event_Writing.md`, `09_Rubric_Writing.md`, `11_AllFail_Analysis.md` and
     `12_Difficulty.md`;
   - `references/Hardness_Manifest_Spec.md`;
   - `references/Ask_Carriers.md` §5–§7.
7. Revision machinery to reuse, not re-derive:
   - `Working_Files/hardening_rev12/`: `oracle.py` (import it), plus `build.py`, `coverage.py`, `verify.py`,
     `report.py` and `revision.json` (copy, never run in place);
   - `hardening_rev13/changes.json` and `injection_fix_20261024/patch.py`;
   - `Task_Authoring/support/analysis/season_pass_runs.py` with `rev13_slots.json`, which reproduces every number in
     `Rev13_Results.md`.

## 4. What revision 13 established
Re-verify anything you rely on.
- **Rules leak.** **[O]**
  - Opus 4.8 running uninterrupted (pre-check, runs 1, 2 and 6) had 0, 1, 0 and 3 wrong register rows out of 128.
  - Leaked in every run: issue remap, own-package receipts, receipt journal, fixture binding (combined and split),
    review lane, dismissal timing, ZOM-801 key lists.
  - Landed once each:
    - the aborted- and diagnostic-run rule (run-4, through fallback-written briefs);
    - billing-label history (run-3, a mixed-model run);
    - the acceptance epoch (run-6, one key, with the rule in its brief).
  - Decoys and stale summaries misled no run: the T39 export (0 of 7), and revision 10's wrong-game sheet, other-game
    mail, old deck and merged-conclusion traps (0 of 6).
- **The big miss was a fallback.** The largest miss (run-4, 10 keys) came after a `model_refusal_fallback` (category
  bio) made Opus 5 the main agent, and its briefs dropped a rule. Fallbacks hit 4 of 7 runs and can't be controlled;
  never design for them. **[O]**
- **Reading is near-deterministic.** **[O]**
  - Every run read:
    - 330–338 of the 338 validation-issue comments;
    - all 302 PR comments, 265 reviews, 944 timeline events and 128 PRs;
    - every source the hub names, including the hub thread reply;
    - the whole Gmail protocol thread;
    - the ZOM-801 description (`linear_get_issue`, first between events 71 and 1298).
  - No run listed ZOM-801's comments or opened Confluence version history.
  - PR inline review comments, commits and branches were essentially never read. The tool catalog has no PR
    review-comment reader, so never use them.
  - Linear issue descriptions were read for only 1–5 of 133 issues per run.
  - So nothing here is found in only half the runs. Variance has to come from judgment.
- **Scores.** Proxy grades: average 92.1 %, SD 0.068, 1 of 6 full passes, 5 patterns.
  - Run-1 lost 8.4 points to one class slip (SP-043), through cascades into class totals, groups and key lists.
  - **[O]/[D]**
- **CSV.** 3 of 7 runs delivered a native Sheet instead of the CSV after the base64 upload failed. It's natural and
  worth keeping, but it is one weight-1 row, and `/hardness` called it a local deviation, not a consequential failure.
  **[O]**
- **ZOM-801.** **[O]**
  - Its description reads: "Tracking the engineering transfer packet. When delivered, append the register link, class
    totals and blocker counts by failed condition to this issue's description; move this issue to In Validation. Keep
    validation issues unchanged."
  - Arthur's comment on it (`cmt_c0696e5f7676681c910c`, 2026-02-13T20:20Z) asks for the HOLD keys under each group.
  - Confluence v4 repeats that rule, which is why every run passed it without reading the comment. Keep the Confluence
    rule.

## 5. Design strategy (binding)
1. **Keep what exists.** Keep every existing rule, trap and record: they are fair background and the classification
   core. Don't add more rules about record conditions like those of revisions 11–13; they leak. The one exception is
   M2(b), with a conservative p̂.
2. **Add 4 independent mechanisms.** Use 5 if the forecast needs it, and never fewer than 3. Each mechanism:
   - survives complete retrieval: the agent will open every main-path record, so the failure must come from judgment
     or from not following an explicit pointer, never from not finding;
   - has a material consequence when it lands: a wrong class (with its cascade), a missing required list or decision,
     or a misdirected delivery. A missing note alone is not material;
   - has its own root cause and its evidence in different records from the others, so an agent that defeats three can
     still fail the fourth. Use only mechanism ids that `tools/hardness_gate.py` accepts (A1–A21, 2.6.1–2.6.14);
   - decides several distinct gradable facts in the deliverables;
   - has a predicted per-run landing rate p̂, with its evidence basis.
3. **Change classes.** Prefer at least two class-changing mechanisms; at least one is required. One class change
   cascades into totals, groups and key lists (about 8 points), which moves the average and the spread far more than a
   list row.
4. **Geometry.**
   - Mechanism-dependent weight, cascades included, is at least 50 % of the planned rubric weight.
   - Each mechanism carries 12–25 %; always-pass weight is at most 35 %.
   - Use honest p̂ from evidence: a weak mechanism gets a low p̂, and the forecast decides whether the set is enough.
     Keep every p̂ ≤ 0.79. Nothing may be predicted to land in every run (all-fail rows) or never to land.
5. **Fairness rails, for every mechanism:**
   - **Incorporation.** It is incorporated through explicit delegating words in a record the agent reads; quote them
     verbatim in the manifest.
   - **One reading.** There is one governing reading, and every fair alternative is accepted. Define scope by artifact,
     time and supersession: which artifact, which dates, and what withdraws or supersedes it.
   - **Reachability.** Its evidence is reachable for Oliver through ordinary catalog calls; prove it with
     `persona_view`.
   - **No cues, no answer key.** No self-advertising cues. Records may carry attributed, defeasible claims (M4 depends
     on them), but never the answer key.
   - **No hidden copy.** The only copy is never hidden behind the ACL.
   - **No surprise asks.** It never grades an instruction the agent had no reason to look for.

## 6. Mechanism menu
Ground every mechanism in real Season Pass records, and pick 4. The ranking reflects evidence on this task and model.

**M3 — An explicit pointer into ZOM-801's comments, carrying the owner's final calls (A13/A14). Strongest.**
- **Evidence.**
  - No run listed ZOM-801's comments, while every run read the description.
  - `/hardness` §7 proposes both a material ask that lives only in those comments and a dated delivery change.
  - A14 base rates (`Hardness_Mastery.md` §0): 67 of 124 Slack-using runs never opened a thread reply, and pagination
    was followed 18 % of the time.
- **Sketch.**
  - A minimal, documented addition to the ZOM-801 description says in plain words that Arthur's final calls for this
    update are in the comments below.
  - A new, dated comment from Arthur there carries material changes, such as:
    - calls on named components that change their classes;
    - a delivery change the prompt leaves open, for example the folder the register goes in or an extra recipient;
    - a layout ask.
- **Authority for class changes.** Handoff Instructions v2 fixes the source of every register input, so a comment
  alone can't change a class.
  - The same added sentence must also scope the comments' authority. For example: "Arthur's final calls on individual
    components are in the comments below; for the components they name, they take precedence over the register
    instructions."
  - I pre-approve that one scoped amendment. Arthur created ZOM-801. Record its exact wording in the manifest and
    dossier.
  - Prefer calls toward HOLD; they agree with doc v2's "Missing input is HOLD, never an inferred pass".
  - If you can't make the class changes decidable this way, restrict M3 to delivery and list asks, and take the
    required class change from M2(b) or M4.
- **Graded.**
  - the named components' classes, as direct rows, with their cascades;
  - the delivery fact;
  - at most 5 spot checks for any layout ask.
- **Guards.**
  - **Placement.** The hub names ZOM-801, and its description is the only allowed place for the pointer. Never name
    the comments in the hub, its replies or any other hub-named document: those were read in 7 of 7 runs, and the
    pointer would leak.
  - **Prompt.** Never contradict the prompt. It fixes "send Arthur the register" and "reply on the handoff thread".
  - **Decidability.** Class changes must be decidable under the existing rules plus the scoped amendment above; never
    an unexplained override.
  - **Rate.** Never carry revision 13's 0 of 7 over as M3's rate: it was measured without a pointer. Keep p̂ ≤ 0.79,
    or its rows become all-fail. Linear comments render (a verified ● carrier).
  - **Key-list rule.** Never move it out of Confluence.

**M1 — Report a disagreement (A16).**
- **Evidence.** On V7-T1, 5 of 6 Opus 4.8 runs resolved a source conflict silently when asked to report it
  (`Hardness_Mastery.md` §11). Reporting is a secondary obligation, not a classification rule.
- **Sketch.**
  - For about 6–8 components, a dated note by a real colleague, active at the freeze, sits on a record the agent reads
    (a validation-issue comment or a PR conversation comment). It states a value for a register field, and the
    governing record disagrees.
  - The existing rules already decide the class.
  - An incorporated instruction says to keep the record's value and to list each such component, with both values,
    under its own heading in the ZOM-801 update. It could be a new Confluence version or a doc v2 amendment.
  - The list must have a stated purpose in the records, so a missing list is material.
- **Graded.** At most 5 spot checks of listed components, plus one volume row with the exact count. The population is
  emergent, so it is sampled. Weights follow the kind of work.
- **Guards.**
  - A disagreement means an explicit value for the same field of the same component and artifact, dated before the
    snapshot, and not withdrawn later.
  - Include near-miss controls (notes that agree, notes about another package) so precision matters.

**M2 — Process findings on approved work (A15, with A6).**
- **Evidence.**
  - For: on V7-T1, 5 of 6 runs missed "CHANGES_REQUESTED then APPROVED counts as a process finding".
  - Against: on this task, the resolved-history rules leaked. Review dismissal timing leaked in every run, and
    billing-label history landed only once, in a mixed-model run.
- **Variants.**
  - (a) A required "process findings" list in the ZOM-801 update, with a stated purpose. This is a secondary
    obligation, as on V7-T1.
  - (b) Class-changing: such a component is WATCH, not READY. Use p̂ ≤ 0.5 for (b) unless you have better evidence.
- **Graded.** At most 5 spot checks plus a volume row. For (b), the cascade into the READY and WATCH totals.
- **Guards.**
  - The oracle computes the full set, including components that already qualify from base or earlier seeds.
  - A CHANGES_REQUESTED on a different artifact, or one that was dismissed, doesn't count, and the rule says so.

**M4 — A confident claim met first, overturned by the records (A1). Weak here.**
- **Evidence.** In the ML-selected example, pass@1 was 0 of 6: Opus "found the data, computed it correctly, and then
  deferred to the most confident-sounding summary" (`Hardness_Mastery.md` §0). The model label of those runs is
  uncertain. On this task, every stale-summary and decoy trap failed, so use a conservative p̂.
- **Sketch.**
  - Early in the hub thread or channel, a senior colleague who is not the handoff owner states confidently that a few
    named components are fixed, cleared or shipped.
  - At the snapshot, the records contradict this for some of those components and agree for others.
- **Graded.** Only the true class of each named component (direct rows, because the message singles them out), with
  its cascades. Never grade whether the run disclosed that the claim was wrong.
- **Guards.**
  - The governing snapshot rule decides, not seniority.
  - It is a claim, not an instruction, and it doesn't come from Arthur.
  - The agreeing controls keep it decidable.

**M5 — A cohort boundary no keyword marks (A17).**
- NF2: 3 of 6. The population was right in 7 of 7 runs, and a boundary change cascades widely.
- It needs a complete cohort amendment: the membership rule in both directions, incorporated, with proof.
- Use it only if the others can't reach the geometry.

**Rejected for this task, from measurement:**
- more rules about record conditions stated where the agent reads (except M2(b));
- decoys, stale summaries and bulk exports;
- forced errors and async waits;
- PR inline review comments, which have no catalog tool;
- a dated delivery change anywhere the agent reads in full (allowed only behind M3's pointer);
- anything relying on the fallback.

## 7. Prove the design before writing SQL (blocking)
1. **Oracle.**
   - Copy `hardening_rev12/oracle.py` to `hardening_rev14/oracle.py`. It imports `hardening_analysis` from
     `Working_Files/`, which stays where it is.
   - Add the new rules, each behind a disable flag, plus a per-key disable for partial misses.
   - Keep the signature `solve(sql, new=True, disable=())`. It must also accept the eight existing flags: validation,
     receipt, review, journal, fixture_binding, acceptance, epoch_binding, history.
   - It must also return what the new mechanisms decide beyond the register (lists, delivery targets).
   - Revision 14's truth comes only from this oracle. With every new flag disabled, it must reproduce
     `hardening_rev12/truth.after.json` on the frozen revision-13 SQL
     (`support/backtests/season_pass/rev13/sql/01_Universe_Inject.sql`).
2. **Gradable surface.** Write `Working_Files/01_Gradable_Surface.json`.
   - Use the format of `support/analysis/rev13_slots.json`: `{"slots": [{id, weight, selector, title}]}`. Add
     mechanism ids (or "core"), requirement and incorporating quote per slot.
   - Follow V3 rules:
     - one fact per row, and no fact in three or more rows;
     - at most 5 spot checks per sampled population, plus a volume row;
     - direct rows only for members a record singles out;
     - at least one Outcome row;
     - every prompt requirement covered;
     - weights 1/3/5 by kind of work.
   - This is the rubric's blueprint: the rubric written later must implement it exactly. Selectors are proxies; where a
     selector and the rubric criterion differ, the criterion is authoritative. List the known gaps.
   - **One analysis entry point.** Use `support/analysis/season_pass_runs.py`.
     - If you need a selector it lacks, copy it to `support/analysis/season_pass_runs_rev14.py` and extend the copy.
     - The copy must still reproduce revision 13: per run 99.6, 91.6, 99.6, 91.6, 79.7, 100.0 and 89.9 %; average
       92.1 %; SD 0.068.
     - From then on, use only the copy. Name the entry point in the pre-registration.

     The revision-13 reproduction (`-B` keeps bytecode out of the frozen folder):
     ```
     S=Task_Authoring/support/backtests/season_pass/rev13; R=$S/runs/07_Baseline_Trajectories
     python3 -I -B Task_Authoring/support/analysis/<entry point> --sql $S/sql/01_Universe_Inject.sql \
       --oracle-dir $S/working_files/hardening_rev12 --slots Task_Authoring/support/analysis/rev13_slots.json \
       --run pre=$S/runs/06_PreCheck_Trajectory/trajectory-run-1.json --run r1=$R/trajectory-run-1.json \
       --run r2=$R/trajectory-run-2.json --run r3=$R/trajectory-run-3.json --run r4=$R/trajectory-run-4.json \
       --run r5=$R/trajectory-run-5.json --run r6=$R/trajectory-run-6.json \
       --out Task_Authoring/support/analysis/rev13_check.rev14.json
     ```
3. **Forecast.**
   - **Probe (optional, before any SQL).** Run it if `PROBE_BASE_URL`, `PROBE_API_KEY` and `PROBE_MODEL` are set; never
     print them.
     - It is a blind, targeted Opus 4.8 probe of M3's pointer and M1's instruction.
     - Show the real revised records in a realistic tool-result context, with n ≥ 20, and record whether the model
       lists ZOM-801's comments (or reports the disagreements).
     - It is diagnostic and UNCALIBRATED. An isolated probe may inflate attention; treat its rate as an assumption,
       not a validated bound.
     - If the model follows M3's pointer in ≥ 90 % of samples, use p̂ ≤ 0.3 for M3.
   - **Model, per run:**
     - each mechanism m misses as a whole with probability p̂_m;
     - otherwise each of its keys misses independently with probability q_m. State q_m and its basis; use 0 for
       mechanisms that land or not as a whole, such as M3;
     - base slips: N ~ Poisson(1) wrong register rows per run on random components, each changing the class with
       probability 0.5 (rev-13 pure runs: 1.0 wrong rows and 0.5 class changes per run), cascades included.
   - **Two dependence scenarios:**
     - independent;
     - correlated: a latent Gaussian correlation of 0.3 between mechanism misses (a Gaussian copula), with the same
       marginals. Report the binary correlations it achieves; a binary 0.3 is impossible for some pairs of rates.
   - **Exact flips.** For every combination of whole-mechanism misses, and for partial misses, take the failed slot set
     from the oracle. A slot fails once, however many causes hit it. Use exact combinations, because interactions are
     non-monotone.
   - **Aggregates first.** Aggregate rows (class totals, group counts, key lists) may fail whenever anything that
     touches them lands, base slips included. Recompute them from the combined oracle result for each combination, and
     never model them as an unconditional OR: balanced changes can leave a total right.
     - In revision 13, the HOLD total failed in 4 of 6 runs, and the READY total and the review group's count and size
       in 3 of 6 each.
     - Check their all-fail probability before anything else. If one exceeds the ceiling:
       - route mechanisms into different aggregates;
       - or use offsetting moves: changes in both directions that leave a total unchanged.
     - Never drop a required aggregate row.
   - **Simulation.** At least 5,000 six-run baselines per scenario, through `tools/difficulty_stats.compute()` under
     both V2 and V3 Hard.
   - **Report, at p̂ and at 0.8 × p̂, for both scenarios:**
     - E[average], with its 10–90 % band;
     - P(each gate) and P(all four gates);
     - U, the largest achievable loss;
     - every slot's P(fails in all 6 runs);
     - the break-even multiplier k: scale every p̂ and q by k (capped at 1) and report the smallest k at which
       E[average] ≤ 70 %, or "none", noting any non-monotonicity.
   - **Labels.** Every forecast number is conditional on the assumed p̂. Label them CONDITIONAL · UNCALIBRATED.
   - **Proceed only if** all four hold:
     - at p̂: E[average] ≤ 62 % in both scenarios, and P(all four gates under both specs) ≥ 0.6 independent and ≥ 0.4
       correlated;
     - at 0.8 × p̂: E[average] < 70 % in both scenarios;
     - at p̂: every slot's all-fail probability is ≤ 0.25;
     - every slot passes the structural all-fail check: its data exists, a catalog tool returns it to Oliver, and its
       requirement is incorporated.
   - **Otherwise change the design:** add weight on mechanisms, add a mechanism, or use a class-changing variant.
     Never shrink weights to pass, because weights follow the kind of work.
   - If two redesigns still miss the targets, stop and report the best design with its numbers; I'll decide.
4. **Pre-registration.** Before handoff, write `Task_Authoring/plans/Rev14_Preregistration.md`.
   - It records the frozen hashes of the SQL, the comment-free SQL, the prompt, the manifest, the surface, the oracle,
     the forecast output and the analysis entry point.
   - It also records each mechanism's p̂, q and basis, the forecast's assumptions, and the predicted gate outcome.
   - Never edit it afterwards.

## 8. Implement
The playbooks are binding, and every gate must PASS, except the N/A checks in §1.
1. **Re-certify the scenario stage** on the current assignment.
   - `stage_gate.py scenario` currently blocks on four items:
     - the design and draft manifest are older than `00_Assigments.md`;
     - the pasted `hardness_gate --design` PASS no longer re-runs;
     - the draft manifest lacks `assignment_context`;
     - `00_V3_Authoring_Evidence.json` doesn't match the context (`role_reviews.scenario` with `context_hash`).
   - Add a revision-14 section to `01_Scenario_Design.md` (mechanisms, a summary of the gradable surface, the forecast)
     and update the draft manifest.
   - `hardness_gate --design` must PASS, then `stage_gate.py scenario --paste`.
   - Red team: run `redteam_review --dual` if `REDTEAM_*` is set. Otherwise write
     `RED TEAM UNAVAILABLE: error: REDTEAM_* not set` in the design; the gate needs the colon and an error, HTTP or
     budget reason. The existing `01b_Redteam_Review*.md` files predate revision 13, so don't count them as a review.
2. **Build the SQL** with a declarative `hardening_rev14/build.py`.
   - It reads only `hardening_rev14/before/01_Universe_Inject.sql`, so re-running it gives identical bytes.
   - Add records rather than rewriting them. Edits to existing records, such as M3's pointer, stay minimal and
     documented.
   - Keep every companion field: thread counters, `updated_at`, Linear stamps, Trello badges and board activity,
     Confluence versions, and mirrors per `integrations.json`.
   - Collision-check every id.
   - Use literal values, with `E''` escaping wherever text has line breaks.
   - Seeded speakers must be active at the freeze. No timestamp after the freeze, except future events.
   - No words that announce a mechanism. Keep new text free of bio-adjacent words, a cheap precaution given the
     fallbacks.
3. **Re-run the checks and paste their outputs:**
   - `sql_lint`, `base_check`;
   - `fact_check --no-leak`, with every new fact declared;
   - `persona_view check-sql` for every load-bearing record;
   - `hardness_gate`.

   Regenerate `Working_Files/01_Universe_Inject.comment-free.sql` with only the intake-marker line removed, and record
   both sha256 values.
4. **Verify (`hardening_rev14/verify.py`).**
   - For each mechanism, removing its deciding records changes only its dependency closure.
   - Components that no mechanism touches keep their revision-13 truth.
   - Run the lazy-solver and literal-value sweeps for each mechanism.
5. **Write the dossier, manifest and report.**
   - Dossier: Facts for the human, constraints for the prompt brief, intended disagreements.
   - Final manifest: `design_delta`, mechanism ids, traps, facts.
   - `01a_Hardening_Report.md`: MODE B on the revision-13 runs, citing run and event from the probe outputs and
     `attribution.json`, with the rebuild section describing revision 14.
   - `stage_gate.py injection --paste` and `stage_gate.py hardening --paste` must PASS.
6. **Prompt chain.** Keep `04_Prompt.txt`. Refresh `04_Prompt_Writing_Brief.md` and `04_Prompt_Check.md` against the
   new universe, so `prompt-writing` and `prompt-check` PASS. If the check finds a prompt-side defect, stop and ask.
7. **Self-review** per GEN_EXECUTION §6a, with counter-readings (fairness, tool, verifier, run) for every mechanism.

## 9. Handoff, then stop
Report:
- the comment-free SQL path and its sha256, for `/injection`;
- what `/prompt` needs;
- a one-page summary covering, for each mechanism, its records, incorporation quote, graded facts and p̂ with its
  basis, plus the geometry, the forecast table and what the pre-check should show;
- every gate output;
- open risks.

Then wait. I run `/injection` and `/prompt`, re-inject, and run one Opus 4.8 pre-check. I'll put the trajectory in
`06_PreCheck_Trajectory/trajectory-run-1.json` and the `/hardness` report in `Plateform_reports/`. If a review fails,
fix the cited defect at its source and re-run the affected gates.

## 10. Pre-check analysis (when I give you the run)
1. Run the entry point on it from the workspace root (`Working_Files` here means `Task_Authoring/task_inputs/Working_Files`),
   with `--run pre=Task_Authoring/task_inputs/06_PreCheck_Trajectory/trajectory-run-1.json` and:
   - `--sql Task_Authoring/task_inputs/01_Universe_Inject.sql`;
   - `--oracle-dir Working_Files/hardening_rev14`;
   - `--slots Working_Files/01_Gradable_Surface.json`;
   - `--attribute` with your new flags plus validation, receipt, review, journal, fixture_binding, acceptance,
     epoch_binding and history;
   - `--out Working_Files/hardening_rev14/precheck_analysis.json`.
2. Check provenance: fallback events, and which model wrote each brief.
3. For each mechanism, give a verdict: LANDED, LEAKED or NOT-REACHED, with event citations. Counter-read each landing
   for fairness, tool and run validity.
4. Decide. Recommend the baseline if `/hardness` is 3 or more and at least two mechanisms landed genuinely. Otherwise
   report why each one leaked and the smallest universe-side fix, and change nothing without my OK.

## 11. Baseline and the rest of the chain
1. **Six runs.** When I give you six runs, run the same analysis on all of them:
   - proxy gates under V2 and V3 Hard;
   - mechanism landing per run;
   - mixed-model runs flagged.

   Score `Rev14_Preregistration.md`.
2. **OEs and rubric.** Write the OEs and the rubric per their playbooks (oe-writing → oe-check, rubric-writing →
   rubric-check, gates PASS). Implement `01_Gradable_Surface.json` exactly. Write every mechanism row so the verifier
   can check it from the output alone. Then stop: I run `/oe`, `/rubric` and the verifier.
3. **Verifier results.** When I give you `10_Baseline_Verifier_Results.md`:
   - check each judgment against the run and the rubric, and record fair corrections with their evidence in
     `11_AF_Justification.md`;
   - run the allfail stage: every row that fails in all six runs needs a validity justification or a fix;
   - compute corrected difficulty per §1;
   - refresh human time (`humantime`) if the task changed;
   - run the release gate. Every check except the N/A checks in §1 must PASS.
4. **Never tune the surface to the runs.** Only documented fairness or correctness repairs are allowed, re-graded.

## 12. Report format
- Every file created or changed.
- Every gate output, verbatim.
- The forecast table.
- Decisions, and why.
- Anything unresolved, named.
