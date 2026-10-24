# Opus hardness eval

Be a **ruthlessly thorough, evidence-based grader** of observed Opus task
difficulty. Challenge every claimed consequential failure and hardness score
under the [Ruthless grading standard](WORKFLOW.md#ruthless-grading-standard);
exclude task/environment defects and preserve this branch's scoring rules.

Assessment version: `model-aware-v3`.

**Model route:** use this eval for an Opus trajectory. If the selected run is
Haiku, use [1B_Haiku_Prediction_Eval.md](1B_Haiku_Prediction_Eval.md) instead.
Identify the actual run model before reading the rest; Opus reviews do not load 1B.

## Purpose and scope

Answer: **How much did this unhinted Opus run actually fail the valid task?**
Higher hardness scores mean worse supported Opus performance, not better Agent
performance. This is an observed-run assessment, not a prediction. One run cannot
establish an average weighted pass rate below 75%, pass@1 or repeatability.

The author supplies the run before review. Supported scores 3–5 clear this gate
for dependent authoring; 1–2 or insufficient evidence HOLD accepted-task
progression. HOLD never prevents obtaining a run needed for review. Other
stages and baseline QC keep their own rules; standalone reviews remain possible
under WORKFLOW.md. The evaluator never launches models, replays tools, executes
SQL or uses live workplace connectors.

## 1. Load and save inputs

Follow [INPUTS.md](INPUTS.md): run `python3 Evals/tools/hg_store_input.py list`,
save newly supplied inputs, then read relevant saved contents. New submissions
replace their own key; unmentioned inputs remain saved. Bare `/hardness` asks
for missing inputs in chat without requiring a task folder or fabricating a report.

- Exact prompt, supplied or saved under `prompt`.
- One selected unhinted Opus run JSON. Save under `opus` with
  `hg_store_input.py save opus --source "<run.json>"`; keep the original bytes at
  `Evals/task_inputs/opus/trajectory.json`.
- Optional injection SQL, or an explicit saved no-injection choice. SQL is a
  proposed overlay, not proof it was applied in the run. Never execute it.
- Reference files used by the prompt, if any. Inspect relevant document/slide
  content and visuals, matching their version and availability in the run.
  Requested outputs are not incoming reference files.

If the saved injection decision is unresolved, ask with other missing inputs:
**Injection SQL (optional): does this task use any? If yes, paste or attach it;
if not, say no injection.** Save an explicit answer with
`hg_store_input.py no-injection`. Save partial inputs, then wait for unresolved
intake before source-dependent review. No OE, rubric, verifier, calibration
batch or second run is required. Reuse assignment/persona/settings for material
requirement, access and provenance checks; ask only about relevant ambiguities.

Follow INPUTS.md's selection rules: an explicit user selection wins; otherwise
prefer matching unhinted Opus. Confirm the actual model from the export, task/source
match and hint status; filenames and input keys are not model identity. Resolve
conflicting labels without rewriting the export. Unknown models, hinted runs
and unresolved source matches cannot establish an unhinted Opus score. Do not
infer hint use merely because task sources contain legitimate rules.

Only explicit task-folder mode uses the structural preflight:

```bash
python3 Evals/tools/hg_preflight.py "<task>" --stage hardness --trajectory "<run.json>" --format json
```

It checks structure, not model identity or success. Honor saved input integrity;
never silently skip a damaged preferred run. Record actual model/version, run ID,
available settings, unhinted status and input hashes. Preserve original provenance.

## 2. Establish requirements and evidence

Read [EXECUTION.md](EXECUTION.md), [ENVIRONMENT.md](ENVIRONMENT.md),
[UNIVERSE_MAP.md](UNIVERSE_MAP.md), and this Eval in full. Use
`python3 Evals/tools/hg_reference.py guide hardness` for the applicable shared
WORKFLOW sections and scoring groups; do not load those sections twice.

Build a concise requirement map from the exact prompt and incorporated instructions
under WORKFLOW.md's **Task requirement authority** contract (`prompt-incorporation-v1`).
Exclude unmentioned handbook/policy obligations and any misses caused only by them
from difficulty evidence. Reassess old requirement maps before reuse. Include valid alternatives, core decisions,
required deliverables and final-response obligations. Include what the run got
right; do not construct the map around its misses or later grading criteria.
This map is a diagnostic checklist, not a Oracle Events or weighted rubric.

Use the three local base folders and [SEARCH.md](SEARCH.md) for targeted source
checks. Reuse supported facts only when input/source versions, rules and coverage
match. Cite source paths plus record IDs or JSON pointers and trajectory locations.
Match the run's source version: refreshed current files do not prove what an
older run saw. Never assume that supplied SQL was deployed. Do not execute it.

Read the current persona roster/ACL and tool catalog under ENVIRONMENT.md.
Evaluator-local access does not prove Agent access. A catalog entry describes
capability, not proof that an operation succeeded in this run. Apply WORKFLOW.md's
**Output capability and failure attribution** contract before attributing missing
or wrong-format outputs to the model.

## 3. Review the observed run

Inspect the material tool calls/results, final response and available outputs.
A runner's `success` label or the Agent's claim of completion does not prove task
success. An exact write payload plus a successful tool result can establish a
written result; do not demand a second artifact copy when that evidence suffices.

For each requirement record expected behavior, observed behavior, citations,
impact and one outcome:

| Outcome | Meaning |
|---|---|
| `MET` | Correct supported result or confirmed required action. |
| `MINOR_GAP` | Local defect that leaves the core result usable. |
| `MATERIAL_FAIL` | Wrong, unsupported or omitted required result/action that materially changes correctness, scope, usefulness or delivery. |
| `UNASSESSED` | Missing evidence or unresolved requirement prevents judgment. |

Retrieval misses, ignored explicit rules, incorrect calculations, bad synthesis,
wrong destinations and omitted execution can all be genuine model failures.
Judge their actual consequences. A simple repair after the fact does not erase
a consequential error. Stated rules, one-source tasks, bounded cohorts and
routine writes have no special score cap. Call count, source
count, cohort size and complicated design alone do not establish an observed failure.

Group shared root causes. One wrong conclusion repeated in three artifacts is
one causal failure with three affected outputs. Record delivery obligations
separately where appropriate, without multiplying failure counts to inflate
severity. Conversely, missing a required write can invalidate the task when
that delivery is its central purpose; execution failures are not excluded.

Keep authored/task defects and external interruptions separate. Missing tools,
inaccessible required data, contradictory requirements, platform outages or
missing runtime capability do not demonstrate model hardness. A reasonable
answer to an ambiguous request is not a proven model error. An Agent's own wrong
arguments, neglected discoverable source or premature declaration of completion
can count when the task and available capabilities are established.

**Incomplete task execution is not the same as incomplete evidence.** A complete
export showing the Agent finish without required actions can support MATERIAL_FAIL.
A truncated export ending before any final result cannot by itself prove those
actions were never completed. Likewise, a source the run never opened is a
retrieval failure when its discoverability, accessibility and required facts are
established; it is not automatically UNASSESSED.

## 4. Decide whether the evidence supports a score

Score when the selected unhinted Opus run, task requirements and material results
are established well enough to justify a band. Execution status describes the
**review**, not whether the Agent completed the task. A fully reviewed failed run can
have review status COMPLETE.

Insufficient evidence means a material uncertainty prevents a defensible band:
for example, a missing original prompt, a truncated export, an uninspectable
claimed output with no adequate write evidence, unresolved model/hint status,
or a source-version/access conflict that changes the expected answer.
It does not mean that a task is easy, that the assessed model succeeded, or that every tool
call or output needs redundant proof. Resolve only gaps relevant to the decision.

Retain independently demonstrated errors even when other scope is unassessed.
Do not assume unknown outcomes were met or failed, and do not convert a missing
tool into hardness evidence. If a material confound prevents assessment, use
provisional NON-FAIL, no numeric score, PARTIAL or BLOCKED, and HOLD. Explain
the exact gap and what would resolve it. A provisional NON-FAIL does not clear
the gate. Do not fill that evidence gap with a made-up score or percentage.

## 5. Assign observed hardness

Apply these bands to the supported task-level result, including correct work,
material failures, root causes and required delivery. The numbers are ordinal
hardness labels, not a rubric grade or error-count formula.

| Difficulty | Score | Verdict | Observed result |
|---|---:|---|---|
| Too easy | 1 | FAIL | The assessed model meets the core requirements with no meaningful defect. |
| Easy | 2 | FAIL | Only minor defects remain; the core result is correct and usable. |
| Hard | 3 | NON-FAIL | A consequential failure needs a bounded correction; substantial core work remains correct and usable. |
| Hard | 4 | NON-FAIL | Material failures require substantial correction across the result, while substantial correct work remains usable. |
| Really hard | 5 | PASS | Genuine model failures invalidate the central result/delivery or defeat much of the core task. |

Distinguish 3 from 4 by the extent of needed correction and remaining usability,
not a mandatory number of independent causes. A single root cause may invalidate
the central result and justify 5. Several cosmetic errors do not become a material
failure through counting alone. Explain why the chosen band fits and why the
neighboring band does not. Labels describe this run, not universal task ease.

For Opus, do not use transfer classes, a hypothetical stronger reader, source-shape
caps, paired-run calibration or design-only advancement. Scores 3–5 require
actual material Opus failure. A retrieval or execution error cannot be discounted
merely because a stronger or more careful run might avoid it.

## 6. Report and next action

Save the report at **`Evals/task_inputs/reports/1a_hardness.md`** through:

```bash
python3 Evals/tools/hg_write_output.py hardness --source "<completed-report.md>"
```

Use exactly one rendered verdict block. Example of a supported result:

```markdown
### FINAL VERDICT: NON-FAIL
Assessment version: model-aware-v3
Assessed model: Opus
Assessment mode: OPUS_OBSERVED
Score: 4
Execution status: COMPLETE
Difficulty: Hard
Gate decision: PROCEED
Gate reason: OBSERVED_OPUS_FAILURE
Evaluator model: [model name (model ID), effort running this review]
Next action: Proceed with dependent authoring; retain the observed failure evidence.
Evidence limits: One run only; no average-score or repeatability claim.
```

| Result | Execution status | Gate | Gate reason |
|---|---|---|---|
| FAIL, score 1–2 | COMPLETE | HOLD | `INSUFFICIENT_DIFFICULTY` |
| NON-FAIL, score 3–4; PASS, score 5 | COMPLETE | PROCEED | `OBSERVED_OPUS_FAILURE` |
| Provisional NON-FAIL, omit Score, Difficulty: unassigned | PARTIAL or BLOCKED | HOLD | `INSUFFICIENT_EVIDENCE` |

Use `Assessed model: Opus` and `Assessment mode: OPUS_OBSERVED`. If model
identity cannot be resolved, use Unconfirmed / UNCONFIRMED only in an unscored
report. The writer validates field consistency; the evaluator verifies the evidence.

For 1–2, explain the lack of consequential observed failure and suggest natural
task-relevant revisions if needed. Changed tasks need a matching run; HOLD never
forbids obtaining it. For 3–5, clear only this gate. For insufficient evidence,
identify the smallest missing evidence or setup fix while retaining proven errors.

Also include input/source/model provenance, the requirement map with expected
versus observed outcomes and citations, grouped failures and independent causes,
correct work and usability, task/environment defects, unassessed scope, and the
score rationale or exact reason no score is supported. Reference
`references/universe_manifest.json` for source provenance.

Do not edit the task or raw export during review. Preserve earlier reports as
history. A current matching Opus review replaces an earlier prediction at the
same fixed report path without inheriting its score. Reuse source facts only
when dependencies match. New reports use model-aware-v3; a rules-only update
can reassess an existing matching run without requiring a new export.
