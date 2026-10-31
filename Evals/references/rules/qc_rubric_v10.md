# Rubric v10 contract

QC authority is the current centralized spec's visible Audit Workflow change log and current rubric
appendix, except where `hg-strict-overrides-v1` below overrides it. Preserve
prompt-incorporation-v1, persona visibility, live services, attachment
inspection, historical injection dates and source-version discipline.

## Local strict overrides (`hg-strict-overrides-v1`, 2026-09-26)

These repository decisions supersede the workbook cells cited in the anchor
table below:

- Overly Specific that rejects a valid prompt-authorized answer is Major.
  A wording preference that rejects no valid answer is `harmless_specificity`
  (Minor).
- Overly Broad is Major (2026-10-17), the same level as Overly Specific. Never
  repair an overly broad row with a count, format or phrasing; name the value.
- Rows that would all fail on one Agent error because each embeds the same
  acceptance condition form one Moderate overlap group.
- Prohibition-only or absence-only acceptance syntax fails Negative Criteria even
  with explicit prompt authority, and so does any row an Agent passes by doing
  nothing, however it is worded ("leaves X as found", "keeps X off Y").
- A row whose title subject is not The Agent, or that names a tool, is a Major
  `non_agent_centric` tally issue (the spec's 09/27 Appendix lists it as Minor),
  in addition to failing Agent-Centric Phrasing.
- Self-containment is title-only; the prompt and sibling titles cannot supply
  acceptance values.
- Two or more rows predicted to fail every run make the rubric FAIL.
- Category Balance fails only with zero Outcome rows; the Process ratio rules
  are removed (2026-09-26 update).
- Spot checks follow Rubric Writing §8: at most five samples per group, one
  output-volume criterion per sampled output, never a sampled core requirement.

## Inputs and review direction

Use the actual prompt, assignment, supplied rubric, OE as a checked reference
path, applicable static injection and source/reference evidence. This stage
does not consume verifier results, all-failing justifications or run metrics.
Requirements come from prompt/incorporated instructions, not an OE
inventing its own authority. A copied citation does not establish a true claim.
When the task has OEs, map every row to the OE steps that reach it and record
each OE conflict with both quotes (Eval 3 §3.1, `oe_cross_check`); the OE eval
itself stays blind to the rubric.

Build the requirement ledger from these sources, enumerate the acceptance
conditions, and test legitimate alternative answers against the entire rubric.
Apply `rubric_factual_checks.md` in both modes. Execute the supported number,
date and literal comparisons from exact source selections; retain the filter,
grain, included records and arithmetic. Semantic claims require source-backed
judgments and whole-rubric alternative tests. A number can be correct but assigned to the wrong source.
For absence claims, check the relevant records and attachment bytes with positive
controls; incomplete coverage is unresolved. No model output or old audit heading
replaces this work.

## Agent subjects and vague examples

Standard titles use The Agent + action + context. Artifact/model subjects are
failing even with positive verbs. Recognized Agent possessives and bare action
forms are nonstandard and fail Agent-Centric Phrasing (1–2, 2026-10-05); they add
no tally issue.
Unfamiliar syntax cannot be relabeled IMPLICIT_ACTION. It needs an actual supported
Agent subject or must remain unresolved. Literal tool names are prohibited.

Actual vague exemplar phrases in acceptance requirements are Moderate. Record
uses of such as, e.g., and for example; they cannot disappear from the tally.
The appendix both prohibits these phrases (C9) and requires exact source strings
(C8). Local override (common errors checklist, 2026-10-04): C9 wins, so a phrase
inside a validated immutable source name is still one Moderate `vague_exemplar`
for that row. The repair is wording that identifies the record without the
phrase. Descriptive negatives remain affirmative. Every
prohibition-only acceptance rule fails Negative Criteria, even when the prompt
explicitly forbids the action; rewrite it as a condition on a write the Agent must
make (an exact count or scope), or a requirement inside a required artifact. Never
a standalone row an Agent passes by doing nothing.

## QC atomicity and self-containment

Apply allowed exceptions before declaring a split necessary. Preserve PR plus
its own merge date, tightly coupled record attributes, components within one
evidenced tool output, and shared content of the same email sent to several people.
The actual sends remain separate actions. Same-file or same-export claims are not
proof of a shared tool output. Generic source containers cannot hide multiple
independently required actions or arbitrary results.

`same_tool_output` needs a visible selected source marked as the actual tool
output, an output ID and its fields; its required assertions must be content from
that same source. `shared_email_content` needs a common content predicate,
recipients and a visible supporting source. Assertions classify CONTENT versus
ACTION; this label remains a semantic judgment, not something the helper proves.
Use source-confirmed exceptions, never labels alone. Unknown provenance remains unresolved. Table sampling remains totals/controls plus atomic spot checks
where appropriate, with no universal minimum spot-check count. Apply
[rubric-sampling-v1](rubric_sampling.md): direct coverage for core/distinct
requirements, justified ordinary/edge samples for repetitive items of comparable
importance, and full review of every supplied criterion. Sampling changes no
severity category, percentage threshold or 1/3/5 complexity-based weight rule.

Self-containment is title-only. The title must state every acceptance-bearing
ID, value, status, destination, recipient and finding. The original prompt,
sibling titles, external universe facts, private justifications and hidden
evidence cannot define acceptance.

## Severity and score

- Major: Incorrect, unauthorized obligations, non-atomic, not self-contained,
  unobservable acceptance, Overly Specific that rejects a valid answer, and each
  missing explicit Outcome.
- Major (local override 2026-10-17): Overly Broad. Exclude implausible invalid
  paths from Overly Broad under the workbook's explicit broadness exception.
- Moderate: duplicate/overlap (including cascading-failure groups), wrong
  category, vague exemplars.
- Minor: harmless specificity that rejects no valid answer. A wording typo the
  judge would still read correctly is non-failing (QC Appendix B12) and is not tallied.

Use the most specific applicable category. The Overly Specific discriminator is
whether a valid prompt-authorized alternative exists that the row would fail.
Count each affected authored row once at its highest severity. Distinct missing
outcomes enter the numerator only.
For `duplicate`, record `duplicate_kind`:

- `COMPLETELY_REDUNDANT`: count each wholly redundant authored row once at
  Moderate, except where that row already counts at higher severity.
- `OVERLAP_GROUP`: give a stable `group_id`, at least two `rows`, and evidence of
  the shared predicate. The canonical group contributes one Moderate issue,
  not one per member. Remove members already counted at higher severity; if no
  members remain, the group contributes zero. Do not repeat the same group or
  use intersecting group memberships: merge them into one canonical group and
  explain the actual overlap. A row cannot count twice across other issues and
  an overlap group. Record the full member list even when deduplication removes
  members from the tally.

This follows the specific appendix C6 numerator rule with the authored-row
denominator unchanged. Distinct output surfaces or an aggregate versus its
atomic spot checks are not automatically redundant. A demonstrated non-atomic
row remains Major even if duplicate controls cover every component; those
controls do not waive atomicity.

Overall Quality follows the rubric-flow-v2 bands in the Eval 3 Local Overrides
(2026-10-09): any Major or Moderate fails; Minor on 5-10% of rows is NON-FAIL 3;
Minor on more than 10% fails; no Major or Moderate and Minor under 5% is PASS.
There is no absolute three-row failure rule. `/rubric` never publishes criteria.

Criteria Weights is separate. Each row records expected_weight, work_kind,
source_ids and reason. The helper maps direct lookup/literal verification to 1;
interpretation/calculation/comparison/limited reconciliation to 3; multi-source
reconciliation/deep reasoning/cross-modal/tracing to 5. Review the work of the
agent, not business importance, grader effort or a sibling criterion's work.
Weights are NON-FAIL 4 only when 10% or fewer rows are one level off and none
are two levels off (Eval 3 Local Overrides); otherwise FAIL. All correct is 5. Classification still needs
evidence; arithmetic is deterministic.

## Evaluation result

Score six static dimensions: overall_quality, criteria_weights, category_balance,
process, agent_centric and negative. The lowest score controls the QC verdict.
The `predicted_all_fail` record is required; two or more predicted rows cap the
score at 2 and make the verdict FAIL.
Static review gates are repair checks, not extra numeric dimensions. A QC PASS
with an outstanding defect, failed gate, weight disagreement or unresolved check
has repair_free false. The evaluation reports suggested fixes and preserves its
input. It never generates, revises or publishes criteria; no OE PASS is required.

Do not claim that passing helper tests proves semantic accuracy. Release testing
must distinguish mechanical checks, source-grounded case reviews, and independent
fresh model reviews. Replaying a deterministic calculation is not a new LLM review.

## QC source anchors and interpretation boundaries

Source: `[External] MCP Advanced Commercial _ original_conference _
6a5595596cf3031de47f0ea2 - QC Centralized Spec Doc.xlsx`, SHA-256
`3e52358d3c98fac68330721fa6e6c4fd5f99df1a15e2d44e859bf8b970be32ad`.
Use the visible Audit Workflow and current Appendix - Criteria Error & Wei;
obsolete hidden sheets do not override these cells.

| Rule | Source anchor | Applied interpretation |
|---|---|---|
| Weight meanings and failure thresholds | Audit Workflow C10; Appendix C18:C20 | Difficulty 1/3/5; >=15% two-level or >=30% one-level disagreement |
| Source of factual truth; severity changes | Audit Workflow C17 | Universe facts establish truth. Overridden locally: Overly Specific that rejects a valid answer is Major; Overly Broad is Major |
| Atomicity exceptions | Appendix C4; Audit Workflow C17 | Same actual output and shared email content may group; separate sends do not |
| Context for self-containment | Appendix C3 | Overridden locally: title-only; the prompt and sibling criteria cannot supply acceptance values |
| Large tables and quantifiers | Audit Workflow C14; Appendix C2/C4 | Totals plus spot checks permitted, no minimum; exceptions apply before splitting |
| Overlap numerator | Appendix C6 | “count multiple overlapping criteria as one Moderate issue”; locally includes cascading-failure groups |
| Vague phrases | Audit Workflow C14; Appendix C9 | Actual exemplar use Moderate; no documented literal-name exception |
| Exact source strings | Appendix C8 | Exact immutable strings are permitted. Overridden locally: an exemplar phrase inside one still counts as Moderate `vague_exemplar` |

The overlap rule is a specific numerator exception, not permission to change the
denominator or count a member twice. Other stage
clock, horizon, OE and run-scoring rules are outside this rubric-only update.
