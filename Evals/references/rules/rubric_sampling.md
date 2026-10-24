# Rubric sampling (rubric-sampling-v1)

This policy governs coverage of repetitive artifact contents. `/rubric` still
evaluates **every supplied criterion**, including its title, evidence, weights
and atomicity. It suggests repairs; it never rewrites the rubric or emits a prefill.

## Select coverage by what matters

- Cover core requirements and distinct requested outcomes directly. Preserve
  substantive conclusions, important exceptions, requested actions, destinations
  and independently required deliverables. A sample of routine rows cannot stand
  in for these requirements.
- Sampling is appropriate for repetitive items of comparable importance, such
  as routine cells in a large spreadsheet. Establish the complete source-defined
  scope and requested properties, then use exact cohort/reconciliation controls
  and grounded atomic spot checks. Do not require a criterion for every cell.
- Include ordinary representative cases and meaningful hard/edge cases. Choose
  across relevant subgroups; selecting only the first or easiest rows needs more
  than convenience as justification. If an exception is itself a core/distinct
  outcome, cover it directly. Explain when no relevant edges exist within the
  eligible group or when they are protected by direct criteria elsewhere.
- Avoid grading the same obligation twice just because it appears in two places.
  Distinct prompt-required deliverables or independent actions can still require
  separate checks. A cohort control and a sample value test different predicates;
  overlap must be demonstrated, not inferred from shared records or values.
- Keep the existing **1/3/5 complexity-based weight rules**. Do not overweight
  minor formatting or details. Importance determines which requirements need
  direct coverage; it does not replace QC's weight calculation.

Rubric Writing §8 limits (hg-strict-overrides-v1): keep **five or fewer samples
per group** (rows beyond five in one group form one Moderate OVERLAP_GROUP), and
add **one criterion checking the volume of the output** (its exact count or
total; without it the cohort control is a Major missing outcome). Never
spot-check a core requirement. Otherwise there is no automatic row-count
threshold or requirement to shrink an otherwise valid exhaustive rubric. A normal-horizon
task can have eligible repetitive contents; its horizon label alone neither
permits nor prohibits sampling. An efficient-looking rubric is not evidence of
complete coverage. Never replace many checks with one “at least N items correct”
mega-criterion. Preserve the separate QC atomicity exceptions.

The intended artifact still covers the full requested scope. Sampling does not
prove every unsampled cell correct. Reviewers record that limit instead of
inventing an independent missing-criterion issue for each eligible unsampled
cell. An ungraded core requirement, distinct requested property/column, meaningful
exception, or independent action still receives the normal coverage review.

## Conditional evidence ledger

Use this only when the **supplied rubric's coverage actually relies on sampling**.
A suggestion to reduce an exhaustive rubric belongs in the report, not in a
fictional replacement coverage ledger. Ordinary direct reviews need no new fields.

Keep each actual control, spot check and protected direct outcome as its own
`checks.requirements` entry with the existing omission/wrong-result tests. For
eligible unsampled repetitive cells, describe the full family in a sampling group;
do not enumerate each cell as a separate missing outcome. Map the prompt's family
requirement to the actual controls, samples and protected outcomes. Do not label
that request optional or map one generic “all rows correct” ID to many criteria.

For each spot-check outcome add:

```json
{
  "coverage_basis": "SPOT_CHECK",
  "sampling_group": "routine-arrivals",
  "sampling_eligible": true
}
```

`sampling_eligible: true` means this is a representative member of a repetitive,
comparably important family, not a core/distinct outcome. Establish that judgment
from the prompt and sources. Other outcomes default to `coverage_basis: DIRECT`.
All listed outcomes still need their normal tests; sampling cannot excuse a
missing or incorrect selected check.

`checks.sampling_groups` is an optional array (empty for direct-only reviews).
Each group contains:

- `id`, `scope`, `property`, `output`, `source_ids`: identify the full family,
  requested property, artifact and verified source anchors. A source must define
  the complete scope, not just the selected examples. Each group covers one
  repeated property on one output; controls may be shared across groups.
- `eligibility`: ELIGIBLE or UNRESOLVED. `repetition_reason` and
  `comparable_importance_reason` substantiate the choice from prompt/source facts.
- `control_outcome_ids`: nonempty IDs of direct cohort/reconciliation checks.
  State the scope and predicate precisely; totals alone can hide cancelling errors.
- `protected_outcome_ids` and `protected_review_reason`: identify applicable
  core/distinct outcomes protected by direct checks, or explain an empty list.
  Do not omit a missing core outcome from the requirement ledger to clear sampling.
- `samples`: objects with `outcome_id`, `case_kind` (ORDINARY/EDGE), and `reason`.
  Include an ordinary representative. All IDs refer to actual spot-check outcomes
  on this same property/output, each with its own row mapping.
- `selection_reason`: why these cases represent relevant subgroups and risks.
  Neither random selection nor first-row selection alone establishes that.
- `edge_cases_complete`, `edge_review_reason`, `edge_cases`: explicitly inspect
  meaningful edge cases. Each edge object has `id`, `description`, `outcome_ids`
  and `reason`; its IDs must reference edge samples or protected direct outcomes.
  An empty inventory needs a reason. An incomplete inventory stays unresolved.
- `limitations`: what the controls and samples cannot establish about unsampled
  cells. Do not claim exhaustive value verification.

The helper checks exact source anchors through the existing evidence reader,
known IDs, group/output/property bindings, ordinary/edge representation and the
separation between direct and sampled outcomes. It cannot prove that an author
classified importance correctly or found every edge case. Unsupported judgments
remain unresolved; do not fill in generic reasons to force a PASS.

Missing or contradictory reviewer metadata is a record-validation error, **not
a new QC failure category**. Actual missing core outcomes, duplicate grading,
non-atomic rows and wrong weights retain their existing categories and thresholds.
The denominator is always the number of authored criteria, even when recommending
a smaller rubric. No verifier input or second reviewer is required.
