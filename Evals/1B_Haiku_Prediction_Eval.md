# Haiku-to-Opus prediction eval

Be a **ruthlessly thorough, evidence-based grader** of Haiku-to-Opus predictions.
Challenge the evidence for transfer under this branch and the
[Ruthless grading standard](WORKFLOW.md#ruthless-grading-standard); a Haiku miss
alone does not establish Opus difficulty.

Assessment version: `model-aware-v3`. Mode: `HAIKU_TO_OPUS`.

Load this eval only when `/hardness` selects an unhinted Haiku trajectory.
For Opus use [1A_Hardness_Eval.md](1A_Hardness_Eval.md) instead; neither path
requires reading the other eval. The actual input model remains Haiku.

## Purpose and scope

Answer: **Does this Haiku run, interpreted against the actual task, provide
credible evidence that Opus would also struggle?** Record Haiku correctness
first, then evaluate transfer. A severe Haiku failure does not automatically
mean a hard Opus task. The prediction is qualitative and uncertain: never
invent an Opus pass-rate percentage, probability, rubric weight or score loss.
The later average weighted pass-rate target below 75% remains an empirical QC
check; clearing this screen neither measures nor guarantees it.

The author supplies the run before review. No Opus backfill, OE, rubric,
verifier, paired runs or calibration batch is required. Missing Opus alone does
not block this prediction. The old pattern/calibration documents remain historical
and are not active scoring dependencies or transfer rates. HOLD never prevents
obtaining a run for review. Other stages and baseline QC keep their own rules.

## 1. Load and save inputs

Follow [INPUTS.md](INPUTS.md) before source checks: list saved inputs with
`python3 Evals/tools/hg_store_input.py list`, save new submissions under their
own keys, and read relevant saved contents. Omitted inputs remain saved.

- Exact task prompt, supplied or saved under `prompt`.
- One selected unhinted Haiku trajectory run JSON. Save with
  `hg_store_input.py save haiku --source "<run.json>"` under
  `Evals/task_inputs/haiku/trajectory.json`; preserve the original bytes/model.
- Optional injection SQL, or an explicit saved no-injection choice. Read SQL
  as a static overlay; it does not prove application in this run. Never execute it.
- Prompt reference files, if any: inspect relevant content/visuals, matching
  the run's versions and availability. Requested outputs are not input files.

Reuse saved assignment/persona and settings for requirements, access and provenance.
If injection intake is unresolved, ask with other missing inputs: **Injection
SQL (optional): does this task use any? If yes, paste or attach it; if not, say
no injection.** Save an explicit no-injection answer with `hg_store_input.py
no-injection`. Save partial inputs and wait for unresolved intake. Bare `/hardness`
collects inputs in chat; it needs no task folder and creates no report during intake.

Use INPUTS.md's selection rules: explicit user selection wins; otherwise Opus
is preferred and Haiku is the fallback. Confirm actual model, unhinted status
and task/source match from the evidence; filenames and storage keys are not proof.
Resolve damaged/unmapped preferred inputs or conflicting labels instead of silently
skipping or relabeling them. Record why Haiku was selected, model/version, run ID,
settings, unhinted status and input hashes. Legitimate source rules are not hints.

Only explicit task-folder mode needs structural preflight:

```bash
python3 Evals/tools/hg_preflight.py "<task>" --stage hardness --trajectory "<run.json>" --format json
```

It checks structure, not model identity or success. The evaluator never launches
models, replays commands/tool calls, executes SQL or uses live workplace connectors.

## 2. Establish requirements and observed Haiku outcomes

Read [EXECUTION.md](EXECUTION.md), [ENVIRONMENT.md](ENVIRONMENT.md),
[UNIVERSE_MAP.md](UNIVERSE_MAP.md), and this eval in full. Use
`python3 Evals/tools/hg_reference.py guide hardness` for shared WORKFLOW/scoring
sections, without duplicate reads. Follow [SEARCH.md](SEARCH.md) for targeted local
checks. Apply persona/ACL, tool capability and task requirement authority contracts.
Local evaluator access does not prove Agent access or output-generation capability.

Build the complete diagnostic requirement map from the exact prompt and incorporated
instructions under `prompt-incorporation-v1`. Exclude unmentioned handbook/policy
obligations and their apparent failures from Haiku-to-Opus prediction evidence.
Reassess old requirement maps before reuse. Include valid alternatives,
required decisions/deliverables and final-response obligations. Include correct
work; do not tailor requirements to misses or later grading artifacts. This is
not a Oracle Events or weighted rubric. Cite source paths, IDs/JSON pointers and
trajectory locations, checking actual run/source versions. Current base files
do not prove what an older run saw; reuse facts only with matching dependencies.

Compare material tool results, final response and available outputs. Runner
success labels and completion claims do not prove success. Exact write payloads
plus successful tool results can establish an output without a redundant copy.
Record expected versus observed, impact and MET / MINOR_GAP / MATERIAL_FAIL /
UNASSESSED for each requirement. Group shared causes; repeated mistakes across
artifacts do not create independent failures. Keep delivery obligations visible.

Record genuine retrieval, rule-following, calculation, reasoning and execution
errors, but do not turn their severity directly into Opus difficulty. Exclude
missing capabilities, inaccessible sources, invalid requirements and external
interruptions from model-hardness evidence. A reasonable alternative under
ambiguity is not a proven error. Preserve independent mistakes when other scope
is unassessed. A complete run omitting required work can demonstrate failure;
a truncated export cannot prove the missing continuation never happened.
Ask only to resolve material evidence gaps, not for redundant proof.

## 3. Screen each material failure

Establish all four checks before crediting a judgment failure:

1. **Valid and consequential requirement.** Identify the prompt or authorized
   source requirement, a normal discovery path, Agent access, expected behavior
   and its effect on a required decision or delivery. Exclude unavailable tools,
   inaccessible data, invalid requirements and other task/environment defects.
2. **Observed failure at the relevant step.** Cite what Haiku saw, what it did
   and what went wrong. Separate sources seen from discoverable sources it
   never opened. A judgment it never reached is a candidate, not an observed
   judgment failure. Group repeated consequences of one mistake as one cause.
3. **Reason to expect Opus difficulty.** Explain the evidence/decision mechanism
   and what could persist beyond Haiku. Candidate mechanisms include reconciling
   later corrections, using facts that eliminate a plausible alternative,
   retaining decisive evidence in synthesis, and resolving identity or exclusion
   boundaries. A pattern name or source count is not evidence of transfer.
4. **Transfer check.** Identify the decisive step that would remain after
   ordinary complete retrieval and careful reading, and classify it below.
   For cohort sweeps, use Section 4 instead of assuming the sweep is already done.

| Transfer class | Meaning | Can support predicted difficulty? |
|---|---|---|
| `CAPABILITY_FLOOR` | The decisive miss is an unissued search, unopened pointer/file, unread returned record, ignored explicit rule, isolated arithmetic/copy error, refusal or routine skipped write. | No, by itself. It is still a real Haiku failure. |
| `JUDGMENT_AMBIGUITY` | A supported inference, identity/scope boundary, evidence reconciliation or synthesis decision remains after retrieval; Haiku actually failed at that step. | Yes, when all four checks and the task-level assessment hold. |
| `SCALE_COMPLETENESS` | Exact classification/aggregation across a source-defined cohort requires per-record evidence and sustained consistency that a bulk view cannot supply. | Only when all conditions in Section 4 hold. |
| `UNDETERMINED` | Available evidence cannot establish what failed or whether the mechanism transfers. | No; determine whether this gap prevents the task-level score. |

`JUDGMENT_AMBIGUITY` does not authorize grading a truly underdetermined task.
The expected outcome must be supportable, allowing valid alternatives. A
contradiction with no defensible resolution is a task defect. Do not manufacture
ambiguity, rename a missed search as synthesis, or treat every later correction
as difficult when a source explicitly states which rule supersedes which.
Conversely, an easy repair after the evaluator supplies the decisive inference
does not prove that finding the inference was easy.

If the run fails upstream and never attempts the judgment, record the unobserved
candidate without crediting it. Its existence alone cannot establish 3–5.
Do not downgrade an actual Opus failure using this counterfactual; this section
is exclusively a check on predictions from Haiku.

## 4. Cohort-sweep exception

Complete retrieval cannot be assumed away when acquiring and classifying the
cohort is itself the task. Before calling an early Haiku bailout weak evidence,
check all four conditions against the prompt/authorized sources and the
**task Agent's tool surface**, not the evaluator's archive access:

1. Required record-level evidence spans a source-defined cohort whose necessary
   work fits the [Long or Super Long Horizon guidance](references/rules/long_horizon.md).
   Use the applicable tier under `horizon-tiers-v1`; the 500-call starting point
   belongs to Super Long Horizon, not Long Horizon. Establish the scope and
   feasible retrieval path; a large row or call count alone is insufficient.
2. No available bulk/list operation supplies every predicate-read field for
   every relevant record. Account for actual pagination, child objects and
   filters. A thread reply count is not its content, and an archive that mixes
   parents with replies is not proof channel history returns both. Check
   realistic cheaper tool paths; evaluator-local search is not an Agent tool.
3. Required exact totals or classifications are derived from each record's
   evidence, so a missed/misread record changes an acceptance-bearing answer.
4. Per-record application is more than a lookup: it requires multiple evidence
   surfaces, matching with substantive exclusions, or interacting rules.

Record each condition's evidence. If a condition is disproven, the exception
does not apply. If a material condition is unknown, do not substitute volume
or label the task easy; resolve it or use insufficient evidence.

When all four hold, a `SCALE_COMPLETENESS` prediction may qualify even if Haiku
abandoned the sweep before deriving the totals. Record `basis: task_structure`
and distinguish the observed bailout from the predicted Opus challenge. This
is the specific structural exception to the observed-judgment requirement;
it is not permission for generic design-only promotion. No paired Opus runs
are required. Explain why sustained exactness threatens the required result,
the feasible tool path, and what evidence could weaken the prediction.

If the supplied Haiku run actually performed the sweep and made relevant
classification/aggregation errors, record `basis: observed_sweep` with citations.
One predicate across one cohort is one cause, however many cells it affects.
Neither basis establishes that Opus has failed; both remain predictions.

## 5. Judge the task as a whole

Record `decision_rule_source`: `enumerated_single_source`, `distributed`, or
`unstated_inference`. A single source enumerating all rules over a bounded
cohort generally supplies weak transfer evidence. Cap such a screen at 2
unless an independently qualifying judgment or cohort-sweep chain establishes
the specific difficulty. Distributed sources and unstated inference never
raise a score by themselves. A stated predicate is not a shortcut for acquiring
all the per-record evidence it needs; apply Section 4 before this cap.

Include correct work and valid alternatives. Count independent root causes,
how much core work the qualifying signals affect, and whether one local
correction would resolve nearly everything. Exclude capability-floor failures
from the prediction rationale even when they dominate the factual Haiku ledger.

| Score / verdict | Opus prediction |
|---|---|
| 1 / FAIL | Adequate task/run coverage shows straightforward core work with no qualifying difficulty signal. |
| 2 / FAIL | Investigation is needed, but supported signals are weak/too narrow; includes adequately reviewed runs with only capability-floor failures. Haiku may still have failed badly. |
| 3 / NON-FAIL | A qualifying judgment or cohort-sweep chain supports consequential predicted Opus difficulty over meaningful core work, with bounded correction and substantial usable work expected to remain. |
| 4 / NON-FAIL | Qualifying signals support broad correction: independent judgment causes or a verified cohort sweep whose derived answers are central, while substantial usable work can remain. |
| 5 / PASS | Qualifying signals strongly support failure of the central decision/delivery or much of the core task. A cohort qualifies only if it threatens that central result, beyond incidental totals. Repeated copies of one narrow mistake or skipped writes alone cannot justify 5. |

Explain why the selected band and its neighbor differ. These are ordinal
screening judgments, not a translated Haiku grade or a calibrated forecast.
Scores 3–5 clear the gate **on prediction**; 1–2 HOLD for insufficient predicted
difficulty. None is a guarantee about a later Opus run.

Low scores require adequate evidence too. If Haiku stopped before engaging
the task's substance, do not infer ease from its failure list. Check the
cohort exception; otherwise leave the score unassigned if no defensible
prediction can be made. A missing source/version, unresolved transfer mechanism
or unknown tool view may require unscored NON-FAIL / PARTIAL or BLOCKED / HOLD.
State the gap and smallest fix. Missing Opus alone and the inherent uncertainty
of prediction are scope limits, not missing mandatory evidence.

## 6. Report the prediction and its limits

Save at **`Evals/task_inputs/reports/1a_hardness.md`**, the same `/hardness`
report path used by Opus; 1B is a conditional branch, not a seventh stage.

```bash
python3 Evals/tools/hg_write_output.py hardness --source "<completed-report.md>"
```

Use exactly one rendered verdict block. Retain model-aware-v3 and all standard
report fields. Scores 1–2 map to Too easy/Easy and HOLD; 3–4 to Hard and PROCEED;
5 to Really hard and PROCEED. Numeric scores require COMPLETE review coverage.
Insufficient evidence uses provisional NON-FAIL, omit Score, Difficulty: unassigned,
PARTIAL/BLOCKED and HOLD. An unresolved model is Unconfirmed / UNCONFIRMED,
unscored only; it cannot establish a Haiku prediction.

Include:

- The actual Haiku model/version, run and input provenance; never relabel it.
- The factual Haiku requirement/outcome ledger, including correct work.
- A transfer ledger for credited and rejected candidates: `chain_id`, expected
  versus observed, requirement/source/trajectory citations, source exposure,
  discovery path, impact, root cause, `transfer_class`, `transfer_rationale`,
  `qualifies`. Include the four sweep conditions and basis when applicable.
- The task-level prediction: rule-source shape, independent qualifying causes,
  core scope affected, contrary evidence, band rationale and uncertainty.

The verdict block uses `Assessed model: Haiku`, `Assessment mode: HAIKU_TO_OPUS`,
and a nonempty `Prediction basis` that identifies the deciding chains or gap.
Scores 3–5 use `PREDICTED_OPUS_DIFFICULTY`; scores 1–2 use
`INSUFFICIENT_DIFFICULTY`; unscored uses `INSUFFICIENT_EVIDENCE`.
Always disclose: **Qualitative Opus prediction from one Haiku run; Opus performance
was not observed.** COMPLETE means this prediction review is complete, not that
Opus validated it. Preserve history when a later matching Opus run replaces it.

Example structure for a supported prediction; replace the illustrative basis
with the actual reviewed evidence:

```markdown
### FINAL VERDICT: NON-FAIL
Assessment version: model-aware-v3
Assessed model: Haiku
Assessment mode: HAIKU_TO_OPUS
Score: 3
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: PREDICTED_OPUS_DIFFICULTY
Prediction basis: C1 passes all four transfer checks; the identity inference affects a required reuse decision.
Evaluator model: [model name (model ID), effort running this review]
Next action: Proceed on this prediction; assess a matching Opus run directly when supplied.
Evidence limits: Qualitative Opus prediction from one Haiku run; Opus performance was not observed.
```

### Boundary examples

- Haiku ignores a clearly stated cutoff, skips a named document and omits a
  requested write. These can invalidate its result, but alone establish no
  Opus-relevant signal. With adequate coverage and no sweep exception, use 2,
  not a direct-Haiku severity score of 5.
- Haiku retrieves the relevant evidence, then makes an unsupported identity
  inference that changes an important reuse decision. A supported, nontrivial
  inference can qualify; assess its task-level impact before choosing 3–5.
- Haiku writes two rows of a large required register. Do not infer either
  easy or hard from two rows: verify the four tool-visible sweep conditions.
  If they all hold, a structural prediction can qualify with explicit limits.
  If the evidence is materially unknown, leave the score unassigned.
- A later matching Opus run ignores that same cutoff and invalidates the
  central deliverable. The direct Opus review may score 5 even though the
  earlier Haiku prediction was 2. Observation replaces prediction.


For low predicted difficulty, explain the weak transfer signal without claiming
Haiku succeeded; suggest task-relevant revisions if needed. For insufficient
evidence, identify the smallest gap while retaining proven errors. Do not edit
task inputs or runs, manufacture trajectories, or tune later rubrics around misses.
Preserve historical reports. A later matching Opus run becomes preferred and is
reviewed directly, replacing this prediction without inheriting its score.
Older matching Haiku runs can be reassessed here; old scores are not automatically
current. A rules-only change can reuse a run; task/source changes need a matching run.
