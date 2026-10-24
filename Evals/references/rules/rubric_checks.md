# Evidence-linked rubric checks (rubric-revision-v10)

Every scored AUDIT needs the `checks` object below inside its format-4 scoring
record. Reuse the source, assertion and judgment ledgers; do not run another
reviewer or invent a second task answer. Preserve the supplied rubric unchanged.

The helper checks exact titles, source bytes, instruction coverage, executable
factual comparisons, concrete test declarations and consistency with issues/scores. It does not infer all
English-language requirements, execute the hypothetical answers or prove a
source interpretation. Missing evidence stays unresolved. Never fill these
fields with generic PASS judgments to get a receipt.

## Sources and instruction coverage

`checks.sources` uses the existing EvidenceReader anchors: `id`, `path`,
`sha256`, `quote`, `visibility` (VISIBLE/INACCESSIBLE/UNRESOLVED), and `access`.
Optional exact JSON `pointer` or inclusive `line_start`/`line_end` selects a
record/excerpt. Incorporated instructions additionally record `incorporated_by`
and `incorporation_reason`. Requirement authority starts at the actual saved
prompt. Research facts support an answer; they do not create extra obligations.

`checks.instruction_reviews` accounts for the entire saved prompt and every
incorporated instruction excerpt used as authority. Each entry has `source_id`
and `clauses`. Quote the entire selected instruction text in its source anchor.
Each clause has:

- `start`, `end`: zero-based Python character offsets, end exclusive. Ordered
  clauses partition the quoted text exactly, including whitespace, without gaps.
- `quote`: exactly that substring.
- `role`: REQUIREMENT, CONTEXT or UNRESOLVED.
- `outcome_ids`: unique IDs below; nonempty for REQUIREMENT, empty for CONTEXT.
- `reason`: why this text creates these outcomes or is context only.

Split a clause containing independently required deliverables before mapping.
An explicit request for commercial exposure cannot be called context or an
optional depth preference. A polite preamble is not a new outcome. Do not copy
every reference-answer detail into the outcome list. For incorporated excerpts,
verify that the selected text includes all applicable instructions, not only the
convenient sentence. The helper checks the selected text, not omitted semantics.

## Outcome tests

`checks.requirements` contains one object per independently requested outcome:

- `id`, `entity`, `property`, `output`, `accepted_result`, `reason`.
- `authority_chain`: exact source IDs starting at the saved prompt.
- `criticality`: critical/non_critical. An omission or wrong answer that passes
  despite violating an explicit required deliverable is **critical**. Optional
  embellishments are excluded from this ledger, not turned into coverage defects.
- `rows`: unique one-based criterion numbers that purport to cover the outcome;
  empty when absent.
- `coverage`: SUBSTANTIVE, MENTION_ONLY, MISSING or UNRESOLVED.
- `omission_test` and `wrong_result_test`: each has `example`, `result`
  (ACCEPT/REJECT/UNRESOLVED), `reason`, and `caught_by`. Judge the changed answer
  against the **whole rubric**, preserving all other task requirements.

For a REJECT test, `caught_by` is a nonempty array of `{ "row": 7,
"quote": "exact acceptance-bearing phrase in that row's title" }`. Other
results have `caught_by: []`. A justification, source pointer, a requirement to
mention a heading, or the word "addresses" cannot substitute for a substantive
predicate. Explain what wrong/omitted content the quoted predicate actually rejects.

Both tests must REJECT for SUBSTANTIVE coverage. An ACCEPT test means MISSING
or MENTION_ONLY, and requires a matching critical `missing_coverage` issue with
`rows: []` and `outcome_id`. A failed expected value within an existing row may
instead need an `incorrect` issue; still test the requested outcome across the
whole set. Do not count the same omission under multiple IDs or duplicate
entity/property/output identities. An unknown result means UNRESOLVED, never
invented FAIL or full coverage.

Coverage counts must equal the ledger. Include `unresolved_outcomes` in the
top-level `coverage` only when nonzero. An independently established failing QC
dimension remains FAIL while other checks are incomplete; unresolved evidence alone produces unscored provisional
NON-FAIL/PARTIAL and cannot establish a complete PASS.

For eligible repetitive contents, apply [rubric-sampling-v1](rubric_sampling.md).
Record the source-defined cohort/column controls and actual atomic samples as
separate outcomes, plus direct coverage of core/distinct outcomes. When relying
on sampling, add `coverage_basis: SPOT_CHECK`, the group binding and eligibility
to each sampled outcome and complete `checks.sampling_groups`. Describe eligible
unsampled cells in the group's scope, rather than manufacturing one missing
outcome per cell. Controls/samples still need the normal mutation tests. Do not
call an ungraded requested column optional. Direct-only reviews need no new fields.

## Row checks

`checks.rows` contains exactly one object per actual criterion, with `row` and
`title` equal to the saved criterion number and exact title. Exported annotation
fields are read from the original array; do not score a rewritten substitute.
Each row also contains:

1. `wording`: `{ "subject": "AGENT_ACTION", "reason": "..." }`. Subjects are
   AGENT_ACTION, AGENT_POSSESSIVE, IMPLICIT_ACTION, NON_AGENT or UNRESOLVED.
   **"The write-up explicitly addresses…" and "The reply states…" are NON_AGENT
   and fail Agent-Centric Phrasing even though the verbs are affirmative.**
   "The Agent's reply states…" and a bare "Reports…" are nonstandard Agent forms
   (no tally issue): NON-FAIL 3 on Agent-Centric Phrasing when they are 10% or
   fewer of the rows, FAIL (1–2) when more. "Agent reports…"
   and "The Agent reports…" are both standard (QC spec: "Agent" + action +
   necessary context); never flag or recommend changing one to the other.
   Exact catalog tool identifiers fail; service names such as Gmail do not.
   The helper rejects classifications that contradict recognizable title syntax.
   Unfamiliar syntax cannot be relabeled IMPLICIT_ACTION. For unfamiliar syntax classified as Agent-centric, include `actor_quote`
   naming the actual Agent subject in the saved title; otherwise use UNRESOLVED.
2. `negative`: `classification` (AFFIRMATIVE, DESCRIPTIVE_NEGATION, PROHIBITION
   or UNRESOLVED) and `reason`. Under `hg-strict-overrides-v1` every PROHIBITION
   makes Negative Criteria score 1–2, even when the prompt explicitly forbids the
   action; `explicit_prompt_prohibition` and an authority quote may be recorded
   for the repair note but do not change the result. "The Agent reports that
   PR #438 had no human-submitted review" is descriptive and affirmative. "The
   Agent does not treat X as proof" grades a prohibition. A positive second clause
   does not erase the first clause's negative acceptance rule.
3. `atomicity`: record `outcome_ids`, `exception` and `independence_test`. The test has `classification` (ONE_RESULT,
   INDEPENDENT_RESULTS or UNRESOLVED), `example`, `reason`,
   `satisfied_outcome_ids` and `failed_outcome_ids`. A concrete partial-success
   example cannot be cleared by relabelling the test ONE_RESULT. Every declared
   independent bundle outside the documented QC exceptions needs a `non_atomic`
   Major issue and a failed atomicity repair gate.
4. `assertion_inventory`: the existing format-4 inventory: `complete`, `reason`,
   and `assertions` with exact field quotes, roles, entities/properties and outcome
   links. Each assertion includes `id`, `field` (title/justification/evidence),
   `quote`, `role`, `outcome_id` and `reason`. Roles: REQUIRED_RESULT, QUALIFIER,
   SUPPORTING_EVIDENCE, UNREQUESTED_REQUIREMENT or UNRESOLVED. Required results
   additionally include `kind` (ENTITY_PROPERTY/RELATIONSHIP/IDENTITY_SET/AGGREGATE/
   DESTINATION/ATOMIC_CELL), `entities` and `property`; RELATIONSHIP includes a
   `conclusion`. Supporting evidence needs an `omission_test` with example,
   ACCEPT/REJECT/UNRESOLVED result and reason. Unsupported/unresolved assertions
   have no outcome ID and describe a suggested `repair`. Multiple REQUIRED_RESULT assertions
   cannot hide under one outcome ID. Preserve validated coherent_record,
   same_tool_output, shared_email_content, identity-only, qualifier and source-only
   cases according to their actual evidence and documented scope.
5. `supporting_fields`: `status` (PASS/ISSUE/UNRESOLVED) and `reason`. Check that
   the exact title agrees with its justification and evidence about value,
   condition, destination, surface, timing and ownership. ISSUE also needs a
   concrete `witness` and a recorded `incorrect`, `unauthorized` or
   `not_self_contained` issue. Supporting text cannot repair the title silently.

6. `fact_review`: the complete claim inventory and executable comparisons in
   `rubric_factual_checks.md`. Every supplied row has this field.
   Exact source selections support NUMBER/DATE/LITERAL comparisons; SEMANTIC
   judgments remain evidence-backed judgments. Required unresolved facts keep the review incomplete. A stated PASS cannot override a computed mismatch.

If other criteria already grade every component of a non-atomic row, record those
controls as duplicate-coverage evidence; they do not waive its Major atomicity
defect. Existing `precision_controls` may identify `{assertion_id, row, quote,
reason}` for each REQUIRED_RESULT assertion, but are not a severity override.
The same row cannot be its own catching control. Use the highest severity once
per authored row and the canonical overlap-group rule in `qc_rubric_v10.md`.

## Non-overridable results

- Recognized NON_AGENT/MCP wording requires Agent-Centric FAIL (1–2).
- A supported prohibition without explicit instruction requires Negative FAIL.
- Recorded independent results outside a documented QC exception require an
  atomicity issue and failed repair gate.
- Computed factual mismatches cannot be cleared by declared semantic PASS labels.
  Required unresolved facts keep the review incomplete without manufacturing QC failure.
- Accepted omissions/wrong substantive outcomes require missing-coverage issues;
  full-coverage counts or "depth weakness" cannot override the tests.
- A sampling declaration needs verified source scope, eligibility rationale,
  direct controls, ordinary/edge selection and protected core/distinct outcomes.
  Sampling never exempts supplied criterion rows from review.
- Missing/stale source anchors, wrong titles, unmatched IDs and contradictory
  records must be corrected before saving a scored report. Actual unresolved
  evidence is recorded as unresolved rather than filled in to satisfy a schema.

For factual claims such as "currently relevant", verify the source version,
scope, chronology and task meaning. Age alone does not prove irrelevance, and
run pass rates do not prove truth. Search attachment bytes when absence evidence
depends on them. These factual judgments still require the reviewer's evidence.

Scoring uses **authored criterion count only** as the denominator, highest
severity once per real criterion and distinct missing outcomes once in the
numerator. Missing outcomes do not inflate the denominator. Keep separate
Agent-Centric/Negative scores out of Overall Quality unless another independently
supported rubric-quality issue applies to the same criterion.

## V10 QC extensions

The score record additionally requires per-row weight_reviews with evidence IDs.
Use qc_rubric_v10.md for work-kind classification and exact disagreement thresholds.
Actual vague exemplar use in title requirements must have a recorded Moderate
issue. A verified immutable LITERAL name containing a matched phrase remains
unresolved under the C8/C9 policy conflict; quotes alone are not an exemption.
Apply verified same_tool_output/shared_email_content atomicity exceptions before
splitting; their source evidence is checked along with coherent_record.
Self-containment is title-only: prompt and sibling criterion context cannot
supply acceptance values. The record also needs `predicted_all_fail` (see
review_scoring.md). Publication readiness is separate from QC score. No verifier
inputs are used.
