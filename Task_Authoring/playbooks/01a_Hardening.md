# 01a — Hardening (Playbook) — HarmonyGames · Spec V2

> Command: `/create-hardening` · Writes: `task_inputs/Working_Files/01a_Hardening_Report.md` (+ hardened `task_inputs/01_Universe_Inject.sql` and `01_Grounding_Dossier.md`) · Paired eval: `/injection` after any SQL change · Gate: **`tools/stage_gate.py hardening` (blocking)** · Read first: `setup/GEN_EXECUTION.md`, then `playbooks/01_Universe_Injection.md`

## Purpose

This step makes the universe carry more genuine difficulty and uses trajectory evidence to show whether the designed difficulty landed. It has two modes and writes one report.
- **MODE A, design (no runs).** Generate grounded scenario candidates, select them for depth, update `01_Scenario_Design.md` + `01_Hardness_Manifest.json`, and harden `01_Universe_Inject.sql` against the `01_Universe_Injection.md` gates.
- **MODE B, forensics (runs exist).** Read every tool call and give each designed difficulty a verdict with citations. Explain every point Opus scored and purge false difficulty. Route each fix either to the universe, where it is fixed here, or to the prompt, where it is reported with proposed wording.

This step changes the universe only. Prompt, OE and rubric edits belong to their own stages; report their defects with evidence and route them there. Model drafting remains allowed by the explicit repository exception (GEN_EXECUTION §2).

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze and the context's registered universe/KB source.
Both freeze dates use the same local universe data. Check each relied-on fact at
the assigned freeze; shared KB summaries are leads, not a separate dataset gate.
V3 changed-topic rules take
precedence over older Evals/V2 references; local authorship and hardness-profile
exceptions remain as recorded in GEN_EXECUTION § 2 and § 3a.

All modes read:
- `00_Assigments.md`, `01_Universe_Inject.sql` and `01_Grounding_Dossier.md`.
- `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md` and any prior `01a_Hardening_Report.md`, if present.
- The universe, through `Task_Authoring/tools/hg.py search`.

MODE B also reads the following files. They are read-only: never edited, never estimated, never fabricated.
- `04_Prompt.txt`.
- `06_PreCheck_Trajectory/` (one Opus 5.5 run plus the human's difficulty answer).
- `07_Baseline_Trajectories/` (six rollouts).
- `10_Baseline_Verifier_Results.md` and `12_Difficulty_Stats.txt`.
- `08_Oracle_Events.md`, `09_Rubrics.json` and `11_AF_Justification.md`, if present.

Choose the mode from what exists:

| Present | Mode |
|---|---|
| No run artifacts | MODE A |
| `06_PreCheck_Trajectory/` only | MODE B (pre-check): one trajectory, provisional verdicts, a predicted `/hardness` band (B3c), no gate statistics |
| A Haiku run only | MODE B (pre-check, prediction): apply the `Evals/1B_Haiku_Prediction_Eval.md` transfer checks to every failure (B3c); a Haiku miss is never hardness evidence on its own |
| `07_Baseline_Trajectories/` + `10` + `12` | MODE B (baseline) |

If an artifact a part needs is missing, name it and skip that part.

Output: `task_inputs/Working_Files/01a_Hardening_Report.md`. When the routing decision is universe-side, also write the hardened SQL and the updated dossier, including Facts for the human.

## Hard gates

1. **Prompt-side defects.** Report a prompt-side defect as quoted span · rule (doc §) · defect · evidence, and propose revised wording where it helps. Route OE and criterion issues to `/create-oe-writing check`, `/create-rubric-writing check` or `/create-allfail`.
2. **Evidence only.** Every verdict cites a rollout and a step. A trajectory you have not read is marked "not read", never inferred. Counts and scores come from `10` and `12`, never from estimates.
3. **Full read.** Read every tool call in every available trajectory, input and output, before writing any verdict.
4. **Do not tune to the baseline.** Never delete, soften or re-weight criteria to move the numbers. Never make a change that only blocks the exact query one rollout typed. Fix the mechanism that let the shortcut work.
5. **No false difficulty.** None of these count as hardening, and each is rejected:
   - hiding the only copy of the evidence behind the ACL
   - making the ask artificially vague or using a hidden cause as a prompt hint/riddle
   - adding a requirement the prompt gives no reason to look for
   - treating another fair outcome as wrong instead of accepting it
   - padding or extra deliverables
6. **Numbers of record** (GEN_EXECUTION §3):
   - Five or more fully passing rollouts out of six fails; retain the unchanged SD 0.1–0.3 check.
   - Corrected average strictly below the assigned cap: Easy 90%, Medium 85%, Hard 70%; equality fails. Correct unfair rows and re-grade before this comparison.
   - ≥ 2 distinct failure patterns. Two rollouts share a pattern unless they differ on ≥ 2 rubric results, and the largest pattern is ≤ 50% of failing rollouts.
   - Errored runs ≤ 2 of 6.
   - Tier is measured on the golden run if one exists, otherwise on the six-rollout average.
7. **Every SQL change re-passes 01.** That means all `01_Universe_Injection.md` gates, `tools/sql_lint.py`, `tools/hardness_gate.py` against the updated manifest, and `/injection`. Update the dossier and its Facts for the human. The report lists every fact that changed so the human can re-check their prompt, Oracle Events and criteria.
8. **Count only genuine failures, the way `/hardness` does** (`Evals/1A_Hardness_Eval.md` §2–§3). A failure is hardness evidence only if all four hold. Otherwise it is CONFOUNDED; it is reported as a defect and routed, never counted as a landed difficulty.
   - The requirement is incorporated (`prompt-incorporation-v1`): the prompt names the source, or a named source delegates to it.
   - The evidence was reachable for the persona and returned by the tool the agent used or by an ordinary alternative call.
   - Every fair reading/outcome is accepted by the rubric; no fair alternative is counted as a failure.
   - The verifier judged it correctly against the trajectory.

   For Opus, a missed discoverable source is a genuine retrieval failure. For Haiku it is `CAPABILITY_FLOOR` (1B §3).
9. **Two numbers, never one.** `/hardness` describes one Opus 5.5 run; the final gate measures corrected six-rollout rubric results against the assigned mode's cap. Report both and never infer one from the other. A Haiku run is historical diagnostic material only, never the V3 pre-check/baseline substitute.

## Procedure (checklist)

### MODE A — design (no runs)

- [ ] **A1 Register the design.** From the dossier, list each designed difficulty: node · mechanism · records · expected wrong reading · overturning evidence · discovery-order proof.
- [ ] **A2 Explore** for coupling seams the design under-uses. Use the `01_Scenario_Design.md` roles, sized to the task, and read inside records, not just metadata.
- [ ] **A3 Generate a ranked set of grounded candidates.** Scale the count to the tier; about 10–15 is plenty. Each candidate is cited to real records:

| # | Anchor storyline (cited) | Coupling (finding → what it changes next) | Characteristic | Discovery-order proof | Reach | Findability term | Gradable fact (a fact, not criterion text) | Services carrying weight | Walk Δ vs tier | Risks |
|---|---|---|---|---|---|---|---|---|---|---|

- [ ] **A4 Select depth over breadth.**
  - Prefer: a wrong reading at one node that corrupts the next; one authoritative-but-wrong claim met before the evidence that overturns it (`Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` (the ML-selected example task)); reading past an apparent conclusion; a deciding fact held only in a structured system; day-level data that must be aggregated.
  - Reject, with a reason: independent lookups, bolt-on writes, unreachable or unfindable evidence, an unfairly rejected alternative outcome, an unauthorized requirement, or a walk pushed outside the tier.
- [ ] **A5 Run the adversarial lazy solver** on the selection. It uses the fewest calls, takes first hits and stops at the first conclusion. Every point it still scores is a leak; fix it before writing SQL.
- [ ] **A5b Design for `/hardness` 4–5 for the right reasons.** For each selected node, write one line covering four checks. A node that fails any of them is redesigned, not shipped:
  - **Incorporated.** Show the chain from a named anchor to the rule. A rule only in an unnamed handbook or policy does not count, and its misses are excluded from hardness evidence (V1 recert task, Hardness_Mastery §11).
  - **Survives complete retrieval.** Name the step that is still hard after every source is opened: a scope or alias call, a house rule against the natural reading, a reported conflict, a finding on a record whose state is already correct, or a per-record derivation. A node that is hard only because nobody searches is a call multiplier, not the engine (§0).
  - **Tool-surface proof.** The decisive record is returned by the natural call. Record the call, or the `hg.py` pointer it maps to. A node that lands only because a search tool misses, a result spills or an endpoint errors is CONFOUNDED by design.
  - **Graded weight.** Preserve the local design target: mechanism-dependent criteria carry ≥30% of planned weight across ≥3 independent causes. Report the share; empirical success is still measured against the assigned mode cap after fair regrading.
- [ ] **A6 Implement** through `01_Universe_Injection.md` S1–S5: dossier blocks, findability and discovery-order proofs, SQL, and the self-validation table.

### MODE B — forensics

- [ ] **B0 Run validity and provenance**, per trajectory, before any verdict.
  - **Model and route.** Record the main-agent model and every subagent model. Subagents on another model, such as a Haiku or Sonnet sweep, make a mixed run. Record it and do not credit its failures to Opus without saying so.
  - **Hint status and source match.** The export carries no user prompt, so match on the content the run touched.
  - **Re-applied injection.** Check that the injected records actually appear in the results.
  - **Completeness.** Look for context compaction, truncation and result events after the final answer, such as background agents still reporting. Calls whose results never reached the deliverable are excluded from the horizon count.
  - **File mapping.** Map each file to its verifier `Run #N` by content, never by file order. Missing or duplicate rollout files are a delivery defect: name them.
  - **Scope of the call.** A truncated export cannot prove an omission (1A §3). A complete export that ends without a required write can.
- [ ] **B1 Per-rollout tool-call ledger.** Build one for each available trajectory. Read the **write payloads** too: comment bodies, message text, document edits and email bodies. Check every designed per-record flag or report against them. Narration and the final response are not the deliverable (calibration: two mechanisms that failed 5/6 were visible only in comment bodies, Hardness_Mastery §11, V7-T1):

| Step | Tool | Input (query / IDs) | What came back (designed node · decoy · claim met first · nothing) | Agent's decision | Rubric(s) affected (from `10`) |
|---|---|---|---|---|---|

  Mark where it searched, what it skipped, where it stopped, where it relied on chat instead of the source, where it committed to a framing, and which calls were blocked or repeated.
- [ ] **B2 Friction and horizon checks.**
  - *Async:* for each configured `*_submit_*` function, check whether submit → check → get appears in each rollout. If the agent bypassed the slow path, name the route it used; the wait contributed nothing.
  - *Forced errors:* confirm the configured tool actually failed in the trajectory. If the agent never called it, the injection did nothing and any recovery criterion is ungradeable. Report it. A configured error that every run routed around added calls and no difficulty (Hardness_Mastery §11: persistent errors on three tools, 10–24 failed calls per run, no failure caused).
  - *Unconfigured tool defects:* list every error or wrong result that the configuration does not explain, such as an ID collision on a write endpoint or a search that misses a record the index holds. Say whether each changed an outcome. One that changed an outcome makes the affected node CONFOUNDED-tool.
  - *Horizon:* use the count basis from gate 6 and exclude blocked or repeated calls. If the count is under the tier, name the missing necessary work: a source that matters, not a deliverable.
- [ ] **B3 Give each designed difficulty a verdict**, citing rollout and step:

| Verdict | Meaning |
|---|---|
| LANDED | Caused a genuine failure (gate 8) or real struggle in the rollouts that reached it |
| CONFOUNDED | Failed, but the cause fails gate 8. Name the sub-class: **tool** (the call did not return the data, an endpoint errored, a result spilled), **fairness** (unincorporated rule, fair alternative incorrectly rejected, open-ended ask graded on one item, unreachable record), **verifier** (judge contradicts the trajectory) or **run** (B0 defect). Route it as a defect |
| LEAKED | Rollouts passed it anyway. State why |
| BYPASSED | Rollouts reached the end state without traversing it, so it was off the true path |
| NOT-REACHED | The run stopped or failed upstream before the node; it is a candidate, not evidence |
| FALSE | Added calls but no coupling: independent, redundant or trivially satisfied |

Give counts per node: runs LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED, out of the completed rollouts. A cascade from one root cause, such as a missed rule repeated in a state, a comment and a summary, is one LANDED cause, not several (1A §3).

- [ ] **B3b Read the score shape** (from `12_Difficulty_Stats.txt`), using the forensics evidence in `references/Hardness_Mastery.md` §0:

| Shape | Usual cause | Fix (universe side) |
|---|---|---|
| Bimodal (some runs near 0, some near 100) | one discovery gates most requirements — usually a single hidden authority (A12) | split governance across 2–4 independent authorities in different rarely-searched services |
| Uniform success (corrected avg ≥ assigned cap) | rules stated in the place Opus reads first; mechanical cohort; no rarely-opened evidence | move rules to hidden authorities with decoys; add A13/A14/A15/A17 chains; never just add volume |
| Uniform failure, low spread (SD < 0.1) | one choke point everyone misses the same way | make chains partially solvable; give each chain a different root cause |
| Short runs (< 100 calls) on a cohort task | no cohort mandate reached the agent, or a bulk shortcut exists | make the cohort rule an incorporated requirement; remove the shortcut (`Ask_Carriers.md` §3) |
| Many calls, high score | volume without judgment (the 0.984 / 816-call case) | add per-record house rules, boundary records, derived figures |
| Latching early (narration "I have enough") | decoy is the first plausible source | keep — this is the lever; ensure the real authority is findable by its name |
| Raw average low, clean average (B3d) high | all-fail rows from unincorporated rules, unauthorized criteria or verifier errors | not hardness — route the defects; rebuild the difficulty on incorporated mechanisms (Hardness_Mastery §11, recert task: 48.7% raw, ≈ 80% clean) |
| Material failures in most runs, corrected average ≥ assigned cap | mechanism-dependent weight is too small (≈ 26% in Hardness_Mastery §11, NF2) | add independent chains whose facts the deliverable must carry; never re-weight to hit the gate |

- [ ] **B3c Predict the `/hardness` band** (pre-check; on the baseline, for the run closest to the median). Use 1A's own procedure, not the rubric:
  - Build a requirement map from the prompt and incorporated sources. Give each requirement MET, MINOR_GAP, MATERIAL_FAIL or UNASSESSED with a step citation.
  - Group failures by root cause. Drop CONFOUNDED failures.
  - Assign the band from 1A §5 and give a one-line reason it is not the neighbouring band.
    - **1–2, HOLD:** core correct, or minor defects only.
    - **3:** one consequential failure with a bounded correction.
    - **4:** material failures needing correction across the result.
    - **5:** the central result or delivery is defeated.
  - For a Haiku run, classify each failure as `CAPABILITY_FLOOR`, `JUDGMENT_AMBIGUITY`, `SCALE_COMPLETENESS` (all four 1B §4 conditions, measured on the tool surface) or `UNDETERMINED`. Only `JUDGMENT_AMBIGUITY` and `SCALE_COMPLETENESS` can carry the prediction. A run that stopped before the governing source gives no score (`INSUFFICIENT_EVIDENCE`). Apply the `enumerated_single_source` cap of 2 unless a qualifying chain exists.
- [ ] **B3d Baseline projection and clean average** (baseline only).
  - **Clean average.** Recompute the average with every CONFOUNDED criterion removed or corrected, beside the platform numbers from `12`. Never replace them. A pass that holds only on the raw numbers is a defect to route, not hardness.
  - **Mechanism weight share.** Report the share of weight whose result depends on a LANDED node. Compare actual corrected results with the assigned mode cap; the historical ~30% mechanism-share heuristic is not an empirical gate.
  - **Concentration risk.** If one node drives most failures, flag it (B3b bimodal and uniform rows).
- [ ] **B3e Verifier sanity.** For every all-fail criterion, every run whose score collapses (≥ 25 points below the median) and every criterion that fails a run with the required write present, open the judge text and the trajectory side by side.
  - Classify each as genuine, verifier error (the judge concedes the fact and still fails it) or rubric defect (unauthorized, over-specific, unincorporated).
  - Feed rubric defects to `/create-allfail` and `/create-rubric-writing check`, with proposed wording where it helps.
- [ ] **B4 Explain why Opus passed.** For each passed criterion or scored point in `10`, name the mechanism and classify it:
  - *Genuine capability.* Out-design it with a deeper node, never by obstructing it.
  - *Universe leak.* The answer was over-findable; the decoy was obviously wrong or never returned by the real query; the correction was met before the claim; the deciding fact was reachable from chat; the ACL did not bind; or the node was off the path.
  - *Prompt leak.* See B6.
- [ ] **B5 Purge false difficulty.** Remove or rebuild every BYPASSED and FALSE node, and every LEAKED node that cannot be repaired into real coupling. Record each one with its evidence. A leaner, deeper design beats a wide, shallow one.
- [ ] **B6 Route each fix.**
  - *Universe-fixable:* regenerate the node through A3–A6 and harden the SQL and dossier here (or hand this report to `/create-injection`, which reads it as a hardening request), then re-run `/injection`.
  - *Prompt-side defect:* report it with proposed wording; the prompt is revised (Claude, Codex or the human) and `/prompt` re-run. If both kinds apply, land the universe change first so the prompt is checked against the final universe. Report each defect in this table; there is no fix column:

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|

  Typical prompt-side defects:
  - It names the channel, doc or ticket, so discovery collapses to a fetch and the async search never fires (`6_Prompt Writing Guidelines - V2.md` §06).
  - It states the root cause or the conclusion: Pre-solved (`05` §03).
  - It announces an injected failure or wait, or names a tool, server or parameter (`05` §4.2).
  - It includes an internal ID a real person would not know (`4_Persona ACL Policy - V2.md` §9).
  - It gives no reason to look for a seeded requirement, which makes the criterion unauthorized (`05` §03).
  - Two readings lead to different writes: decision ambiguity (`05` §07).

### Report skeleton (`01a_Hardening_Report.md`)

1. Mode, inputs read, inputs missing, run validity (B0). Write `MODE A` or `MODE B` here first; the gate takes the first mention as the mode (MODE B: every register row cites a rollout and a step, e.g. `run-3 · event 212`).
2. Gate status, copied from `12`, beside the clean average and mechanism weight share (B3d) (MODE B baseline only).
3. Predicted `/hardness` band with its requirement map and neighbour reasoning (B3c).
4. Designed-difficulty register with verdicts and per-node counts (LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED).
5. Per-rollout ledgers.
6. Friction, tool-defect and horizon checks.
7. Verifier sanity findings (B3e).
8. Why Opus passed.
9. Purge list.
10. Candidates and selection (MODE A, or rebuilds in MODE B).
11. Routing: universe changes made (statements and facts changed) · prompt-side defects (with proposed wording) · routed OE and rubric observations.
12. Self-review (below).
13. Next steps.

## Self-review (GEN_EXECUTION §6a, stage-specific)

Run this after the report is drafted and record it as the report's Self-review section. Paired eval: `Evals/1A_Hardness_Eval.md` (or 1B for a Haiku run). Walk §3–§5 in order against the report, not from memory.

1. **Counter-read every LANDED verdict.** Write the strongest argument that the run failed for a reason outside the design, and resolve it with a pointer:
   - **Tool.** Did the call the agent made return the decisive record? Open the raw result in the trajectory, then confirm the record exists through `tools/hg.py`. If the record exists but the call did not return it, ask whether an ordinary alternative call would have.
   - **Fairness.** Does each rule trace to the prompt and reachable source? Accept all fair alternatives; if a miss only reflects a rejected fair reading, mark it CONFOUNDED, fix the row and re-grade before attributing difficulty.
   - **Verifier.** Does the judge's own text concede the fact?
   - **Run.** Is it a mixed-model run, compacted, or missing its run-1 file?

   A verdict whose counter-reading cannot be resolved with evidence becomes CONFOUNDED.
2. **Counter-read every LEAKED verdict.** Write the best argument that the trap was never live. Resolve each with the trajectory step:
   - Did the natural query return the decoy?
   - Was the claim met before the correction?
   - Was the rule stated verbatim where the agent reads first (§9: verbatim supersession)?
   - Did a bulk call carry the answer?

   A trap that was never live is FALSE, not LEAKED, and goes to the purge list.
3. **Counter-read the band.** Argue for the neighbouring band from the same requirement map. Check that no CONFOUNDED failure is still counted, and that no cascade is counted as several causes. Check, by grepping the write payloads, that a designed flag was not missed.
4. **Re-verify facts, not notes.** Re-read through `tools/hg.py` every record that decides a LANDED, LEAKED or CONFOUNDED verdict. A value carried over from the dossier, Oracle Events or golden answer is a lead, not evidence. Example from calibration: a "title-only" PR whose merge commit names the ticket.
5. **Re-run the mechanical checks** after any SQL change (`sql_lint`, `hardness_gate`). Recompute the clean average with `tools/difficulty_stats.py` on the corrected matrix.
6. **Record** each verdict, its counter-reading and its resolution, and anything left unresolved, named (gate minimum: one evidenced counter-reading per LANDED or LEAKED verdict in the register, plus the band). Never soften a CONFOUNDED finding to keep a mechanism looking landed. Never quote replacement wording for the prompt, Oracle Events or criteria.

## Self-check (QC Spec V2 dimensions this step owns)

- **Trajectory — Agent Failure Rate, Average Weighted Rubric Pass Rate, Failure Signature Concentration, Task Type & Horizon, Error Rate** (the Trajectory rows of `references/Docs/QC_Spec_Doc_Latest.csv`, which GEN_EXECUTION calls `QC_Spec_Doc_Latest.csv`): this step explains a Fail and routes the fix. It never recomputes these differently from `12`. The clean average (B3d) is reported beside them, never instead of them.
  - Horizon counts exclude calls that never reached the deliverable, such as background subagents reporting after the final answer (B0).
  - An errored run is one without a completed export. A compacted or mixed-model run is complete but flagged.
- **Universe — Feasibility and Cross-service Coherence:** every SQL change re-passes the `01_Universe_Injection.md` S5 table.
- **Prompt — Pre-solved, Explicit Tool Mention, Contrived, Unique Ground Truth:** reported only, never fixed here.

## Deliver

Run `python3 Task_Authoring/tools/stage_gate.py hardening Task_Authoring/task_inputs --paste`; handoff is blocked until it prints `STAGE GATE hardening: PASS`, and `--paste` writes that output into the Self-review of `01a_Hardening_Report.md` (the next stage's gate refuses an upstream artifact without a current PASS block). If the SQL changed, re-run `stage_gate.py injection` too: its pasted digests go stale and every downstream gate blocks until it passes again.

Report:
- the report path and the mode that ran
- the predicted `/hardness` band, and on the baseline the raw and clean averages
- verdict counts (landed / confounded / leaked) and the top leak mechanisms
- the routing decision
- any SQL changes, with the facts that changed
- the prompt-side defects, with proposed wording

Next:
- If the SQL changed: re-run `sql_lint.py` and `hardness_gate.py`, then paste it into `/injection`. The user re-applies it before the next run.
- If there are prompt defects: revise the prompt (Claude, Codex or the human), then run `/prompt`.
- Then the human repeats the pre-check or baseline as the flow requires.
