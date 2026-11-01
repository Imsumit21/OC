# 01a — Hardening (Playbook) — HarmonyGames · Spec V2

> Command: `/create-hardening` · Writes: `task_inputs/Working_Files/01a_Hardening_Report.md` + `Working_Files/run_forensics/<revision>/` (ledgers, node verdicts) + ledger records in `support/hardness_ledger/ledger.jsonl` · Tools: `tools/trajectory_ledger.py`, `tools/node_verdicts.py`, `tools/surface_grader.py`, `tools/hardness_ledger.py`, `tools/hardness_forecast.py` · Consumed by: `/create-scenario --revise` (S0r), which decides; `/create-injection` makes every universe change · Gate: **`tools/stage_gate.py hardening` (blocking)** · Read first: `setup/GEN_EXECUTION.md`, then `playbooks/01_Universe_Injection.md`, `plans/Fold_Hardening_Into_Scenario_And_Injection.md` §2, §7.7, §7.9

## Purpose

This step uses trajectory evidence to show whether the designed difficulty landed, and proposes how the universe can carry more genuine difficulty. It writes one report.
- **MODE A, design (no runs).** Moved: its steps now live in `/create-scenario` (S1 coupling seams, S5a mechanism portfolio, S5b liveness, S6b gradable surface) and `/create-injection` (S4b solver, S5b mutation, S5b′ geometry, S5c liveness, S5e forecast). For a legacy task that has none of those artifacts, the MODE A section below maps each part to the step that now does it; this skill writes no MODE A report.
- **MODE B, forensics (runs exist).** This skill stays the single owner of run forensics (plan decision 3). Read every tool call, with the shared tools doing the mechanical part, and give each designed difficulty a verdict with citations. Explain every point Opus scored and propose what to purge and where each fix goes. `/create-scenario --revise` (S0r) consumes the result and decides (plan §2, B5–B6): it dispositions the verdicts and routes each fix — universe changes to S5a onward and then `/create-injection`, prompt-side defects reported with proposed wording.
- **MODE B (pre-check intake).** One trajectory of your independent harness (`06_PreCheck_Trajectory/trajectory.json`): validity, node verdicts, deliverable diff, ledger, posterior forecast and a go / no-go call before the six-run baseline is spent (§7.9 below).

This step measures and proposes; it changes no other stage's artifact. Universe changes are decided in `/create-scenario --revise` and made by `/create-injection` as the next revision (it *is* the revision, plan §2). Prompt, OE and rubric edits belong to their own stages; report their defects with evidence and route them there. Model drafting remains allowed by the explicit repository exception (GEN_EXECUTION §2).

## Inputs / Output

First run `python3 Task_Authoring/tools/task_context.py --task-dir <task_dir> --write --require-source`
and read `Working_Files/00_Task_Context.json` (GEN_EXECUTION § 0). Use all eight
assignment fields, the assigned freeze and the context's registered universe/KB source.
The assigned universe date selects the universe (GEN_EXECUTION § 0a): Feb 14,
2026 → normal, Oct 1, 2025 → synth-cut. Read only that universe, apply its state
rules and clock, and stop if the date is missing — there is no default. Check
each relied-on fact at the assigned freeze; shared KB summaries are leads, not a
separate dataset gate.
V3 changed-topic rules take
precedence over the older V2 reference documents in `references/Docs/`; local authorship and hardness-profile
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
| No run artifacts | none here: MODE A moved to `/create-scenario` and `/create-injection` (the MODE A section maps each part to its step) |
| `06_PreCheck_Trajectory/` only | MODE B (pre-check): one trajectory, provisional verdicts, a predicted `/hardness` band (B3c), no gate statistics; the pre-check intake below |
| A Haiku run only | MODE B (pre-check, prediction): apply the `Evals/1B_Haiku_Prediction_Eval.md` transfer checks to every failure (B3c); a Haiku miss is never hardness evidence on its own |
| `07_Baseline_Trajectories/` + `10` + `12` | MODE B (baseline) |

If an artifact a part needs is missing, name it and skip that part.

Output: `task_inputs/Working_Files/01a_Hardening_Report.md`, the forensics under `Working_Files/run_forensics/<revision>/` and the dispositioned ledger records. A universe-side fix is not made here: `/create-scenario --revise` (S0r) decides it, and `/create-injection` implements it as the next revision with an updated dossier and Facts for the human (plan §2, B5–B6 and gate 7).

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
7. **Every SQL change re-passes 01** — and is made there: `/create-injection` is the revision (plan §2), so all `01_Universe_Injection.md` gates, `tools/sql_lint.py`, `tools/hardness_gate.py`, the preflight and `/injection` run on it. This report lists every fact a proposed fix would change, so the human can re-check their prompt, Oracle Events and criteria.
8. **Count only genuine failures, the way `/hardness` does** (`Evals/1A_Hardness_Eval.md` §2–§3). A failure is hardness evidence only if all four hold. Otherwise it is CONFOUNDED; it is reported as a defect and routed, never counted as a landed difficulty.
   - The requirement is incorporated (`prompt-incorporation-v1`): the prompt names the source, or a named source delegates to it.
   - The evidence was reachable for the persona and returned by the tool the agent used or by an ordinary alternative call.
   - Every fair reading/outcome is accepted by the rubric; no fair alternative is counted as a failure.
   - The verifier judged it correctly against the trajectory.

   For Opus, a missed discoverable source is a genuine retrieval failure. For Haiku it is `CAPABILITY_FLOOR` (1B §3).
9. **Two numbers, never one.** `/hardness` describes one Opus 5.5 run; the final gate measures corrected six-rollout rubric results against the assigned mode's cap. Report both and never infer one from the other. A Haiku run is historical diagnostic material only, never the V3 pre-check/baseline substitute.

## Procedure (checklist)

### MODE A — design (no runs): moved to `/create-scenario` and `/create-injection`

The design steps now run where the design is made (plan §2). For a legacy task without those artifacts, run them there:

| Part | New owner | Made mechanical by |
|---|---|---|
| A1 Register the design | `/create-scenario` S5 (traps, chains) + S5a `mechanism_portfolio` | `hardness_gate.py` field checks |
| A2 Coupling seams | `/create-scenario` S1 | — |
| A3 Ranked grounded candidates (the candidate table moved too) | `/create-scenario` S5a | ledger priors per candidate (`hardness_ledger.py priors`) |
| A4 Depth over breadth | `/create-scenario` S5a | advisory forecast ranking |
| A5 Adversarial lazy solver | `/create-injection` S5b | information-ablation mutants (`difficulty_mutation.py`) |
| A5b(1) Incorporated | `/create-scenario` S4 | `hardness_gate` incorporation checks |
| A5b(2) Survives complete retrieval | declared in S5a; diagnosed in `/create-injection` S5d | optional blind probe (advisory) |
| A5b(3) Tool-surface proof | `/create-injection` S5c | `trap_liveness.py` flags + recorded platform calls |
| A5b(4) Graded weight | `/create-scenario` S6b + `/create-injection` S5b′ | `01_Gradable_Surface.json`, geometry U / L_max, forecast |
| A6 Implement | `/create-injection` S1–S5 | existing gates |

### MODE B — forensics

- [ ] **Run the shared tools first** (they do the mechanical part; the model reviews and dispositions):
      `python3 Task_Authoring/tools/trajectory_ledger.py --task-dir Task_Authoring/task_inputs --sql <rev>=Task_Authoring/task_inputs/01_Universe_Inject.sql --sql <older rev>=Task_Authoring/task_inputs/Working_Files/run_forensics/<older rev>/01_Universe_Inject.sql … --out-dir Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>`
      (B0–B2: validity, provenance per phase and per brief, revision binding by content, decoded writes, briefs, counted
      calls through `difficulty_stats.count_tool_calls`), then
      `python3 Task_Authoring/tools/node_verdicts.py --task-dir Task_Authoring/task_inputs --sql <rev>=… --sql <older rev>=… … --ledger-out Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>/proposals.jsonl --out Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>/node_verdicts.json`
      (B3 proposals, each run graded with the solver of the revision it is bound to). Event numbers are 0-based indexes
      into the export array.
      **Pass every stored revision**, one `--sql` per `Working_Files/run_forensics/*/01_Universe_Inject.sql`
      (`/create-injection` stores each one). A run binds only on content no other stored revision holds: one SQL alone
      gives INSUFFICIENT. For the task's first revision use `--sole-revision "<why this is the only revision>"`
      instead; the tools refuse it while another revision is stored, and it still needs the run to show that SQL's
      content. A run that is not BOUND (INSUFFICIENT, AMBIGUOUS, UNBOUND) is listed and never evaluated: mark it
      `historical` in the revision intake, or bind it.
- [ ] **B0 Run validity and provenance**, per trajectory, before any verdict. `trajectory_ledger.py` reports each item
      below; confirm it, and add what the tool cannot see.
  - **Model and route.** Record the main-agent model and every subagent model. Subagents on another model, such as a Haiku or Sonnet sweep, make a mixed run. Record it and do not credit its failures to Opus without saying so.
  - **Report provenance.** Keep each quoted eval report's `Clock:` line and cite the universe manifest at `Evals/references/universes/<key>/universe_manifest.json`, never the retired root manifest (A-28).
  - **Hint status and source match.** The export carries no user prompt, so match on the content the run touched.
  - **Re-applied injection.** Check that the injected records actually appear in the results.
  - **Completeness.** Look for context compaction, truncation and result events after the final answer, such as background agents still reporting. Calls whose results never reached the deliverable are excluded from the horizon count.
  - **File mapping.** Map each file to its verifier `Run #N` by content, never by file order. Missing or duplicate rollout files are a delivery defect: name them.
  - **Scope of the call.** A truncated export cannot prove an omission (1A §3). A complete export that ends without a required write can.
- [ ] **B1 Per-rollout tool-call ledger.** `trajectory_ledger.py` writes it per run (`calls.jsonl`, `writes.json`,
      `briefs.json`). You review every call in `node_verdicts.json`'s `review_queue`: every call that touches a node's
      deciding records, briefs or writes, plus every call the tool cannot classify. List the calls you did not review, and
      state each verdict's coverage. Read the **write payloads** too: comment bodies, message text, document edits and email bodies. Check every designed per-record flag or report against them. Narration and the final response are not the deliverable (calibration: two mechanisms that failed 5/6 were visible only in comment bodies, Hardness_Mastery §11, V7-T1):

| Step | Tool | Input (query / IDs) | What came back (designed node · decoy · claim met first · nothing) | Agent's decision | Rubric(s) affected (from `10`) |
|---|---|---|---|---|---|

  Mark where it searched, what it skipped, where it stopped, where it relied on chat instead of the source, where it committed to a framing, and which calls were blocked or repeated.
- [ ] **B2 Friction and horizon checks.**
  - *Async:* for each configured `*_submit_*` function, check whether submit → check → get appears in each rollout. If the agent bypassed the slow path, name the route it used; the wait contributed nothing.
  - *Forced errors:* confirm the configured tool actually failed in the trajectory. If the agent never called it, the injection did nothing and any recovery criterion is ungradeable. Report it. A configured error that every run routed around added calls and no difficulty (Hardness_Mastery §11: persistent errors on three tools, 10–24 failed calls per run, no failure caused).
  - *Unconfigured tool defects:* list every error or wrong result that the configuration does not explain, such as an ID collision on a write endpoint or a search that misses a record the index holds. Say whether each changed an outcome. One that changed an outcome makes the affected node CONFOUNDED-tool.
  - *Horizon:* use the count basis from gate 6 and exclude blocked or repeated calls. If the count is under the tier, name the missing necessary work: a source that matters, not a deliverable.
- [ ] **B3 Give each designed difficulty a verdict**, citing rollout and step. `node_verdicts.py` proposes one per node ×
      run (was the deciding record in a result the responsible agent saw; did the briefs for the affected records carry
      the rule, in their text or in a file the worker read; does the written value match the solver for that run's
      revision) and classifies every register difference once (mechanism · `mechanism?` · slip · representation ·
      cascade). `mechanism?` is an error inside a rule's cohort that no ablation reproduces; it is pending your review.
      It never assigns CONFOUNDED; it flags candidates. You disposition every proposal, then append the dispositioned
      records: `python3 Task_Authoring/tools/hardness_ledger.py append <dispositioned.jsonl>`. Each record keeps model,
      harness and source; a correction supersedes, never overwrites. A verdict with `mechanism?` errors is refused
      until `features.disposed_by` records their disposition. Control and channel records never enter the priors:

| Verdict | Meaning |
|---|---|
| LANDED | Caused a genuine failure (gate 8) or real struggle in the rollouts that reached it |
| CONFOUNDED | Failed, but the cause fails gate 8. Name the sub-class: **tool** (the call did not return the data, an endpoint errored, a result spilled), **fairness** (unincorporated rule, fair alternative incorrectly rejected, open-ended ask graded on one item, unreachable record), **verifier** (judge contradicts the trajectory) or **run** (B0 defect). Route it as a defect |
| LEAKED | Rollouts passed it anyway. State why |
| BYPASSED | Rollouts reached the end state without traversing it, so it was off the true path |
| NOT-REACHED | The run stopped or failed upstream before the node; it is a candidate, not evidence |
| FALSE | Added calls but no coupling: independent, redundant or trivially satisfied |

Give counts per node: runs LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED, out of the completed rollouts. A cascade from one root cause, such as a missed rule repeated in a state, a comment and a summary, is one LANDED cause, not several (1A §3).

- [ ] **B3b Read the score shape** (from `12_Difficulty_Stats.txt`) with the shape → cause → fix table, which moved to
      `playbooks/12_Difficulty.md` (merged into its table; `/create-difficulty` owns the routing).

- [ ] **B3c Predict the `/hardness` band** (pre-check; on the baseline, for the run closest to the median). Use 1A's own procedure, not the rubric:
  - Build a requirement map from the prompt and incorporated sources. Give each requirement MET, MINOR_GAP, MATERIAL_FAIL or UNASSESSED with a step citation.
  - Group failures by root cause. Drop CONFOUNDED failures.
  - Assign the band from 1A §5 and give a one-line reason it is not the neighbouring band.
    - **1–2, HOLD:** core correct, or minor defects only.
    - **3:** one consequential failure with a bounded correction.
    - **4:** material failures needing correction across the result.
    - **5:** the central result or delivery is defeated.
  - For a Haiku run, classify each failure as `CAPABILITY_FLOOR`, `JUDGMENT_AMBIGUITY`, `SCALE_COMPLETENESS` (all four 1B §4 conditions, measured on the tool surface) or `UNDETERMINED`. Only `JUDGMENT_AMBIGUITY` and `SCALE_COMPLETENESS` can carry the prediction. A run that stopped before the governing source gives no score (`INSUFFICIENT_EVIDENCE`). Apply the `enumerated_single_source` cap of 2 unless a qualifying chain exists.
- [ ] **B3d Baseline projection and clean average** (baseline only). Before a rubric or verifier exists,
      `python3 Task_Authoring/tools/surface_grader.py --task-dir Task_Authoring/task_inputs` grades the runs on the
      gradable surface and runs the four gates through `difficulty_stats.compute()` (a design check, labelled as such;
      the rubric and verifier remain the grading of record). After them, `difficulty_stats.py`'s corrected view is the
      number of record.
  - **Clean average.** Recompute the average with every CONFOUNDED criterion removed or corrected, beside the platform numbers from `12`. Never replace them. A pass that holds only on the raw numbers is a defect to route, not hardness.
  - **Mechanism weight share.** Report the share of weight whose result depends on a LANDED node. Compare actual corrected results with the assigned mode cap; the historical ~30% mechanism-share heuristic is not an empirical gate.
  - **Concentration risk.** If one node drives most failures, flag it (B3b bimodal and uniform rows).
- [ ] **B3e Verifier sanity.** For every all-fail criterion, every run whose score collapses (≥ 25 points below the median) and every criterion that fails a run with the required write present, open the judge text and the trajectory side by side.
  - Classify each as genuine, verifier error (the judge concedes the fact and still fails it) or rubric defect (unauthorized, over-specific, unincorporated).
  - Feed rubric defects to `/create-allfail` and `/create-rubric-writing check`, with proposed wording where it helps.
- [ ] **B3f New-release FAIL classes to attribute** (`Evals/3_Rubrics_Eval.md`, `1_Prompt_Eval.md`):
  - `overly_broad` is Major: one broad row that a plausible wrong answer can pass fails the rubric outright (B-09).
  - A row an idle agent passes (no writes, no answer) is a Negative Criteria FAIL; test every row's `do_nothing_case` (B-11).
  - Prompt Contrived: staged typos, trap hints/riddles, a destination the persona knows hidden, audit-form wording, if-chains (B-14).
  - False premise by universe: a departed person acting, business as usual after the Feb 11 shutdown on Feb 14, post-cut objects on Oct 1 (A-26, B-16).
  - Evidence only on Trash, in an attachment or in an unlinked record is `unobservable` (Major) (A-20).
  - An OE edit makes the rubric review stale, and `prompt-ugt-v1` records, rubric format-4 records and rubric ledger format 1 are not reusable: expect a FULL re-review (A-19, C-13, C-11, C-22).
- [ ] **B4 Explain why Opus passed.** For each passed criterion or scored point in `10`, name the mechanism and classify it:
  - *Genuine capability.* Out-design it with a deeper node, never by obstructing it.
  - *Universe leak.* The answer was over-findable; the decoy was obviously wrong or never returned by the real query; the correction was met before the claim; the deciding fact was reachable from chat; the ACL did not bind; or the node was off the path.
  - *Prompt leak.* See B6.
- [ ] **B5 Propose the purge** (S0r decides, plan §2). List every BYPASSED and FALSE node, and every LEAKED node that cannot be repaired into real coupling, as purge or rebuild, each with its evidence. A leaner, deeper design beats a wide, shallow one.
- [ ] **B6 Propose the routing** (S0r decides).
  - *Universe-fixable:* name the node to rebuild and the facts it would change; `/create-scenario --revise` takes it from S5a onward (`design_delta`), and `/create-injection` implements it as the next revision, then `/injection`.
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

### MODE B (pre-check) — intake of your independent-harness trajectory (plan §7.9)

Advisory and UNCALIBRATED, pre-registered. **Trigger:** `06_PreCheck_Trajectory/trajectory.json` appears for the
current revision, after scenario → injection → prompt. It decides whether to spend the six-run baseline. Write
everything under `Working_Files/run_forensics/<rev>/` and summarise it in report section 1. `<rev>` is the current
revision's label; `<harness>` is `NAME@VERSION`; `<model>` is the run's model label.

- [ ] **1. Validity** (`trajectory_ledger.py`): harness identity and model labels, subagents included (from the init
      event; a `model_refusal_fallback` that hands the main agent to another model is a mixed run); completeness (a
      final result event, no compaction gap, no background events after the result); **revision binding by content**
      (the current revision's seeded ids and values appear in the results); prompt match by content (exports may omit the
      user prompt).
      `python3 -B Task_Authoring/tools/trajectory_ledger.py --task-dir Task_Authoring/task_inputs --run precheck=Task_Authoring/task_inputs/06_PreCheck_Trajectory/trajectory.json --surface Task_Authoring/task_inputs/Working_Files/01_Gradable_Surface.json --sql <rev>=Task_Authoring/task_inputs/01_Universe_Inject.sql --sql <older rev>=Task_Authoring/task_inputs/Working_Files/run_forensics/<older rev>/01_Universe_Inject.sql … --prompt Task_Authoring/task_inputs/04_Prompt.txt --source independent-harness --harness <harness> --out-dir Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>`
      (one `--sql` per stored revision; the task's first revision: `--sole-revision "<reason>"` instead, refused while
      another revision is stored).
      Anything but BOUND on evidence (INSUFFICIENT, AMBIGUOUS, UNBOUND), or an errored run, stops the intake: the run is
      not evidence for this revision.
      **V3 run validity.** Every message must come from Opus 5.5. Any other model, for example after a
      `model_refusal_fallback`, makes the run invalid for V3: report it and re-run it.
      - `trajectory_ledger` reads the model of every message through one owner (`difficulty_stats.model_provenance`,
        also behind the six-run model gate). It compares labels exactly after stripping a bracketed suffix:
        `claude-opus-5-5[1m]` is Opus 5.5; `claude-opus-5` is not.
      - `<synthetic>` is a harness message: it is counted, never checked. An unrecognised label is UNKNOWN, never
        valid.
      - It reports `mixed_model` (two or more models) and `v3_valid` apart. An off-model message with no fallback
        event before it still flags the run, and each one is listed with its source (main thread or subagent).
      - When diagnosing such a run, attribute each failure to the model that decided it: the writer of the brief, and
        the thread that wrote the row.
      - In Season Pass revision 14, every traced failure in the four fallback runs was the fallback model's
        (`Hardness_Mastery.md` §12).
- [ ] **2. Node verdicts** against **this revision's** solver, with the per-rule brief-transmission check over the
      subagent inputs:
      `python3 -B Task_Authoring/tools/node_verdicts.py --task-dir Task_Authoring/task_inputs --run precheck=Task_Authoring/task_inputs/06_PreCheck_Trajectory/trajectory.json --sql <rev>=Task_Authoring/task_inputs/01_Universe_Inject.sql --sql <older rev>=… … --source independent-harness --task <task> --ledger-out Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>/precheck.proposals.jsonl --out Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>/precheck.node_verdicts.json`
      (the same `--sql` set, or `--sole-revision`, as step 1).
      Review the queued calls (B1) and disposition each proposal (B3); CONFOUNDED is yours to assign.
- [ ] **3. Deliverable comparison**: decode the write payloads (CSV, Sheets, comments, slides, mail) and diff them field
      by field against `truth.json`:
      `python3 -B Task_Authoring/tools/surface_grader.py --task-dir Task_Authoring/task_inputs --run precheck=Task_Authoring/task_inputs/06_PreCheck_Trajectory/trajectory.json --out Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>/precheck.surface_grades.json`
      (a pre-check is graded but never enters the six-run gates; UNGRADED slots are listed with the coverage).
      **Confirm every failed slot against the write payload before it counts.** On Season Pass revision 14, the proxy's
      decoder defects failed slots the run had met, and moved one run by 20 points. They included:
      - headings taken from intro prose;
      - sections ended by a table header;
      - JSON-escaped text;
      - only the last update read;
      - bullet key lists;
      - tool aliases;
      - SHA-prefix length.

      A slot the decoder can't read is UNGRADED, never failed.
- [ ] **4. Ledger**: append the dispositioned verdicts with `source: independent-harness`, the harness id and the model
      label: `python3 -B Task_Authoring/tools/hardness_ledger.py append <dispositioned precheck records.jsonl>`.
- [ ] **5. Posterior forecast**: the priors now include this run's dispositioned verdicts (the revision has no platform
      runs yet, so the §11 rule that a revision's priors never use its own platform runs holds); forecast the six-run
      gates and pre-register the result before anything else changes:
      `python3 -B Task_Authoring/tools/hardness_forecast.py forecast --task-dir Task_Authoring/task_inputs --model <model> --task <task> --preregister --harness <harness> --out Task_Authoring/task_inputs/Working_Files/run_forensics/<rev>/precheck.posterior_forecast.json`
      Another model's evidence enters only through a transfer record (printed TRANSFERRED · UNCALIBRATED). Declared
      channels need ledger records of their family or a disclosed `--channel-rate`. Pass this run's `briefs.json`
      (`--briefs`, from the `trajectory_ledger` output) so the batches scenario uses the run's real brief batches.
- [ ] **6. Decision** (advisory until calibrated). Spend the six-run baseline only if both hold: at least one
      consequential, fair failure exists (the `/hardness`-style test, B3c), and the posterior P(all gates pass) clears
      the provisional threshold (plan §5 starting candidates: P(all gates) ≥ 0.8 and E[average] ≤ cap − 0.05; not
      blocking until §10 Phase 2 calibrates them). Otherwise go to `/create-scenario --revise`.
      For the platform pre-check, add the V3 plan's go rule (`plans/V3_Opus55_Difficulty_Plan.md` §7 step 5). Go only if
      all four hold:
      - `/hardness` is 3 or more;
      - the corrected proxy is at most cap − 5;
      - at least 2 independent pre-registered loss channels failed in Opus 5.5's own decisions: designed mechanisms
        that LANDED, or declared complexity channels (scale, chain, delegation) that failed. Control errors and
        unattributed slips count for neither;
      - the run is valid.

      `node_verdicts` reports this tally per run (`go_rule`): the landed mechanisms and failed channels whose deciding
      models are all the expected model, merged when they share a landed key or a source. It lists apart what it didn't
      count: other models' decisions, control over-applications, slips and `mechanism?` errors pending review.

      **Stop rule:** at most two platform pre-checks per scenario. After two misses, change the scenario.
- [ ] **7. Hardness v2 diagnosis** (`Hardness_Mastery.md` §13.4; Opus 5.5). Run
      `python3 -B Task_Authoring/tools/hardness_v2_check.py --task-dir Task_Authoring/task_inputs` on the revision the run
      is bound to and quote its table in section 8. For every trap the run settled, state which kind of v2 failure it
      was, from the call ledger: the correction came back in the same call or container as the original
      (`same_container`), in an anchor's thread or file (`first_read`), or in the record that delegates to the original
      (`on_delegation_path`); a bulk call carried the answer; a decoy was never on the path; volume was brute-forced.
      Then list the heavy rows (weight 5) that passed: those are the parts Opus finds easy, and the proposed rebuilds
      (section 10) must not add more of them. Propose only v2 moves: move a correction out of the obvious place, add a
      done source with a missing piece (A24) or a completion note elsewhere (A25), move one or two in-scope items
      outside the obvious filter, or put the deciding fact behind an alias a contact or history record resolves. Never
      propose more rows, items, steps or volume, and never spell a rule out in the prompt (one v2 task went from
      failing to 100 %).

**What one run can and cannot show.** The screen is asymmetric. It can reject a design strongly: if success needs k
mechanisms each landing with p ≥ 0.7, a run in which all k leak has likelihood ≤ 0.3ᵏ (2.7 % for k = 3). It cannot
confirm one: a run with landings is consistent with a wide range of p, and the six-run gates (SD band, ≥ 2 patterns,
< 5 full passes) need run-to-run variation one run cannot show.

**Harness fidelity.** An independent harness can differ from the platform tool surface (search ranking, result
spills, list endpoints). Record the harness; track per-mechanism agreement between harness and platform verdicts over
time; until it is measured, weigh discovery-type verdicts (A12, A13, A14, A18) below judgment-type verdicts (A1, A15,
A16 after retrieval).

### Report skeleton (`01a_Hardening_Report.md`)

1. Mode, inputs read, inputs missing, run validity (B0). Write `MODE A` or `MODE B` here first; the gate takes the first mention as the mode (MODE B: every register row cites a rollout and a step, e.g. `run-3 · event 212`). MODE B (pre-check): the intake's six results — binding verdict, mixed-model flags, proposals and their dispositions with review coverage, the deliverable diff, the ledger record ids, the pre-registered posterior forecast id with its P(all gates) range (UNCALIBRATED), and the go / no-go call.
2. Gate status, copied from `12`, beside the clean average and mechanism weight share (B3d) (MODE B baseline only).
3. Predicted `/hardness` band with its requirement map and neighbour reasoning (B3c).
4. Designed-difficulty register with verdicts and per-node counts (LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED).
5. Per-rollout ledgers.
6. Friction, tool-defect and horizon checks.
7. Verifier sanity findings (B3e).
8. Why Opus passed (with the `hardness_v2_check` table and, per settled trap, its v2 failure kind; heavy rows that passed).
9. Purge list (proposed; S0r decides).
10. Proposed rebuilds (candidates for `/create-scenario --revise` S5a), each a Hardness v2 move (§13.4), never added volume.
11. Routing (proposed; S0r decides): universe changes proposed (the facts they would change) · prompt-side defects (with proposed wording) · routed OE and rubric observations.
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
5. **Re-run the mechanical checks.** Recompute the clean average with `tools/difficulty_stats.py` on the corrected matrix, and re-run `trajectory_ledger.py` / `node_verdicts.py` if any input they read changed. (SQL changes, and their `sql_lint` / `hardness_gate` runs, belong to `/create-injection`.)
6. **Record** each verdict, its counter-reading and its resolution, and anything left unresolved, named (gate minimum: one evidenced counter-reading per LANDED or LEAKED verdict in the register, plus the band). Never soften a CONFOUNDED finding to keep a mechanism looking landed. Never quote replacement wording for the prompt, Oracle Events or criteria.

## Self-check (QC Spec V2 dimensions this step owns)

- **Trajectory — Agent Failure Rate, Average Weighted Rubric Pass Rate, Failure Signature Concentration, Task Type & Horizon, Error Rate** (the Trajectory rows of `references/Docs/QC_Spec_Doc_Latest.csv`, which GEN_EXECUTION calls `QC_Spec_Doc_Latest.csv`): this step explains a Fail and routes the fix. It never recomputes these differently from `12`. The clean average (B3d) is reported beside them, never instead of them.
  - Horizon counts exclude calls that never reached the deliverable, such as background subagents reporting after the final answer (B0).
  - An errored run is one without a completed export. A compacted or mixed-model run is complete but flagged.
- **Universe — Feasibility and Cross-service Coherence:** owned by `/create-injection`, where every SQL change re-passes the `01_Universe_Injection.md` S5 table; this step only proposes.
- **Prompt — Pre-solved, Explicit Tool Mention, Contrived, Unique Ground Truth:** reported only, never fixed here.

## Deliver

Run `python3 Task_Authoring/tools/stage_gate.py hardening Task_Authoring/task_inputs --paste`; handoff is blocked until it prints `STAGE GATE hardening: PASS`, and `--paste` writes that output into the Self-review of `01a_Hardening_Report.md` (the next stage's gate refuses an upstream artifact without a current PASS block). The gate also re-runs the injection checks on the current revision (`revision.injection`), so this stage cannot pass while `stage_gate.py injection` fails.

Report:
- the report path and the mode that ran
- the predicted `/hardness` band, and on the baseline the raw and clean averages
- verdict counts (landed / confounded / leaked) and the top leak mechanisms
- the proposed purge and routing
- the proposed universe changes, with the facts they would change
- the prompt-side defects, with proposed wording
- MODE B (pre-check): the go / no-go call with the pre-registered posterior forecast id (UNCALIBRATED)

Next:
- Universe-side: `/create-scenario --revise` (S0r) dispositions the verdicts and decides the purge and routing; `/create-injection` implements the change as the next revision, then `/injection`. The user re-applies the SQL before the next run.
- Pre-check intake: go → the six-run baseline; no-go → `/create-scenario --revise`.
- If there are prompt defects: revise the prompt (Claude, Codex or the human), then run `/prompt`.
- Then the human repeats the pre-check or baseline as the flow requires.
