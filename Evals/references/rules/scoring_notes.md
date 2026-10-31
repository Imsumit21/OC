# Scoring interpretation

`Evals/references/rules/scoring.json` supplies scored dimensions, selectable
error labels and numerical thresholds. Rubric uses six numeric Sub-Dimensions,
separate repair gates and six named review checks under rubric-revision-v10
(QC category severity, authored denominator, executable factual checks and input
binding; see `qc_rubric_v10.md` and `review_scoring.md`). Oracle Events use `oracle-events-v2` with separate completeness/accuracy scores.
Other stage definitions and the rubric percentage thresholds are preserved. The Injection entry is an unscored static-check reference under
`injection-static-v2`; its former difficulty/style/discovery gates are removed.
Authority, input, catalog, date and schema notes are adapted to this bundle. Source hashes and
adaptations are recorded in `manifest.json`.

## Authority and stage scope

Use the supplied task prompt and authorized sources under `WORKFLOW.md`'s
**Task requirement authority** contract (`prompt-incorporation-v1`): only the
prompt and instructions it clearly incorporates establish grading requirements.
Unmentioned handbooks, onboarding documents and policies cannot add obligations,
even when official or injected. Cite the incorporating prompt passage for each
source-derived instruction and recheck older requirement maps before reuse.
Use the local archive and supported evidence for
facts, capabilities and visibility. Apply `Evals/ENVIRONMENT.md` and
`Evals/WORKFLOW.md` for setup, read-only scope, inputs, evidence and outputs.
The numbered Evals supply current stage procedures and explicit policy overrides.
Apply the JSON's scored dimensions where no explicit stage override applies.
Optional historical examples never establish new requirements or live facts.

`service-availability-v1` in ENVIRONMENT.md applies to every stage: Snowflake
and Confluence are confirmed live, and their reads are unscoped per `acl.md`
(QC Rating Form V12). Concrete task-specific restrictions and materially
unresolved access conflicts still follow the normal evidence rules.

The original QC form and the stricter authoring gates are distinct. A form
dimension without a NON-FAIL option does not acquire one merely because the
report vocabulary supports NON-FAIL. Preserve exact selectable error labels
when reporting a form dimension. The stage's final verdict follows its own
existing aggregation rule and `Evals/WORKFLOW.md`'s report contract.

Examples of existing overrides: prompt date alignment may fail for a material
scenario contradiction before runs, and the prompt's naturalness and originality
gates apply as defined in Eval 1. Rubric exclusion coverage must remain
affirmative under Eval 3. Optional injection SQL and absent reviewer evidence
must be handled under the shared contracts.

## Stage ownership and repeated checks

Use `WORKFLOW.md`'s **Stage ownership and evidence reuse** contract. `/prompt`
checks request/design/feasibility before later artifacts exist; it does not load
Oracle Events, rubrics or agent runs. Its necessary-work thresholds are design
requirements, not observed Too easy/Easy/Hard/Really hard judgments. Those belong
to `/hardness`; per-criterion rubric weights and baseline metrics remain distinct.

Hardness uses `model-aware-v3`. Route by the actual selected run: Opus reads
`Evals/1A_Hardness_Eval.md` for observed assessment; Haiku reads
`Evals/1B_Haiku_Prediction_Eval.md` for Opus prediction. Load only the matching
eval and use its bands, not the JSON's trajectory QC metrics. Prefer Opus,
accept Haiku without backfill, and require no later authoring artifacts.

Both branches use FAIL 1–2 / HOLD, NON-FAIL 3–4 or PASS 5 / PROCEED. Numeric scores
require COMPLETE evidence for the relevant check; material gaps use unscored
provisional NON-FAIL / PARTIAL or BLOCKED / HOLD, retaining proven errors.
Task/environment defects do not establish hardness. HOLD never prevents obtaining
a needed run, and one run cannot establish average pass rate or repeatability.
Later matching Opus runs are assessed afresh without inheriting predictions.
Other stages retain their own rules; older scores are not automatically current.

A matching static injection review can supply its already-verified checks.
OE evaluation validates the supplied critical path against the task and universe; rubric validates
the actual criteria against those outcomes and facts. Reuse source-backed facts
only when dependencies and scope match; inspect new/changed claims directly.
Each stage still issues its own
verdict and records its own complete coverage.

## Grading rigor

Every eval follows `ruthless-grading-v1` in WORKFLOW's **Ruthless grading standard**:
actively challenge acceptance and score rationales, substantiate findings and
complete all applicable checks. Strictness changes review rigor, not stage
scope, input requirements, scoring thresholds or verdict meanings. Preserve valid
alternatives, distinguish missing evidence from demonstrated defects, and keep
task/environment limitations separate from Agent failures. Use eligible evidence
reuse and targeted checks; no extra runs or failure-rate targets are introduced.

## Evidence and time

The fixed current date and time is the task date's clock: `2026-02-14 00:00 UTC` for Feb 14 tasks, `2025-10-01 00:00 PT` (`2025-10-01 07:00 UTC`) for Oct 1 tasks. Base and injected records may predate January 1, 2026; there is no
global earliest allowed date. Use ENVIRONMENT.md's chronology and timestamp
rules, together with the task's actual date scope. Future events may be described
as future, not already completed; new outputs requested by the task need not
exist yet.

Unverified evidence is not a demonstrated defect. Preserve a proven FAIL during
a partial review, but do not certify unsupported gates or turn a missing
reviewer connection into a task FAIL. Required unresolved evidence without a
proven failure uses NON-FAIL with PARTIAL/BLOCKED and no numeric score under
`Evals/WORKFLOW.md`; provisional NON-FAIL does not clear gates. For hardness, model failure is not
an artifact-quality FAIL: all numeric bands require COMPLETE review coverage
for the band; retain independent errors during an unscored partial assessment.
Apply that rule to required checks within the selected stage's scope. For
`/injection`, lack of live evidence or verified schema definitions is an
outside-scope compatibility limit, not a PENDING gate. A static PASS can include
those limits. Schema rules are in `Evals/references/schema/README.md`.

## Complexity thresholds

- Tool-call requirements live only in Trajectory - Task Type & Horizon
  (2026-09-26 update): count from a 100%-scoring baseline rollout when one
  exists, otherwise the average of the six baseline rollouts. Normal Horizon is
  50–100 calls; Long Horizon is 100–500+.
- The former prompt gate (more than 15 necessary calls) and the trajectory
  average-≥15 floor are removed. `/prompt` checks cross-service friction,
  investigation feeding meaningful writes and a load-bearing complexity
  dimension, without estimating a call count.

Do not request runs to score prompt design.
Retries against inaccessible records, unnecessary repeated calls and persona
configuration are not necessary Agent work. Batch-size and model checks use
the actual assignment and supplied run evidence; do not fabricate runs to fit
an example count or launch new runs from an eval.

## OE and rubric rules

Eval 2 uses `oracle-events-v2`: complete critical path plus accurate tools,
parameters and expected data. See `oracle_events.md`. Following the Oracle Events
guideline, a missing critical step or a wrong existing step FAILs (2); minor,
non-action and final-response defects are NON-FAIL 3; a clean set is PASS 5.
The overall result is the minimum of both components. Without a proven failure,
missing review evidence remains unscored NON-FAIL / PARTIAL or BLOCKED. Review
OEs as steps, not as a final answer. A full reference path is not mandatory for
every valid solution. `/oe` preserves supplied OEs and writes an evidence-bound
review; no Oracle Events, rubric or model run is required.

Eval 3 derives complete rubric coverage from verified requirements and uses
exactly `title`, `category`, `weight`, `justification`, `evidence`, with weights
1, 3 or 5 and categories Outcome/Process.


Eval 3 uses `rubric-revision-v10`. Its six review checks (Atomicity,
Overly Specified, Self-Contained, Process Supervision, Duplicates, Contradictory)
organize evidence; its six scored dimensions are Overall Quality, Criteria Weights,
Category Balance, Process, Agent-Centric and Negative. No verifier, all-failing or
batch-result input or score belongs to this stage.

Use `qc_rubric_v10.md` as the rubric policy contract, `review_scoring.md` for the
score record, and `rubric_factual_checks.md` for source selection and executable
comparisons in AUDIT. Category Balance fails only with zero Outcome rows (no Process ratio cap);
keep the existing Process eligibility rules. Affirmative artifact-subject wording still fails
Agent-Centric; descriptive negative facts remain affirmative. Under
`hg-strict-overrides-v1`, prohibition-only acceptance fails Negative Criteria
even with explicit prompt authority.

Evaluation preserves the input and reports scores plus suggested fixes. Bind the
review to the exact supplied rubric, source dependencies and current policy.
A computed factual mismatch cannot be cleared by a reviewer PASS label.
Semantic source relevance, coverage and legitimate alternative checks still need
evidence. AUDIT preserves supplied inputs and reports actual QC findings.

Self-containment is title-only under `hg-strict-overrides-v1`: prompt and
sibling-criterion context cannot supply acceptance values. Justification/evidence
cannot silently impose or widen acceptance conditions. A bounded search miss does
not prove absence; read relevant attachment bytes and retain unresolved coverage.
Contradictions require incompatible conditions in the same scope, date and branch.

Overall Quality has no non-fail band (2026-10-05): any Major, any Moderate, or
Minor on 5% or more of the rows fails; no Major/Moderate and Minor <5% is PASS.
No absolute row count or failed repair gate overrides these QC fractions. Severity follows
`hg-strict-overrides-v1`: Overly Specific that rejects a valid answer is Major,
Overly Broad is Major (2026-10-17), harmless specificity is Minor, and rows that all fail
on one Agent error form one Moderate overlap group. Separately, two or more
predicted all-fail rows make the rubric FAIL. Count each authored
row once at its highest severity, distinct missing outcomes in the numerator
only, and each canonical overlap group once according to `qc_rubric_v10.md`.
Criteria Weights is separate and uses the current 1/3/5 difficulty definitions;
it fails on any one- or two-level disagreement.

A below-threshold defect remains a suggested repair. The score and repairs are
reported separately. The large-audit exception permits totals/controls plus
atomic spot checks with no universal minimum; it does not make the full source
cohort optional or waive distinct requested actions.
