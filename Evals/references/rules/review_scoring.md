# Rubric v10 scoring record

This release uses rubric-revision-v10. Read qc_rubric_v10.md for
QC classifications, source standards and allowed exceptions. This stage consumes
no verifier, all-failing or batch-result inputs. No such score or placeholder is
required.

## Required fields

- format_version: 5 (2026-10-17: per-row `valid_case` and `do_nothing_case`,
  `final_reply_test`, source `reachability` and `oe_cross_check`).
- review_mode: AUDIT. CREATE records are rejected by the current writer.
- eval_release: the current `hg_eval_release.py snapshot rubric` object. Report
  its Eval version and Eval release SHA-256; historical versions remain separate.
- rubric_path: the exact saved supplied rubric input, never an unregistered draft.
- reviewed_json_sha256 and review_context_sha256: actual current fingerprints.
- checks: all exact-title, source, prompt-clause, coverage and assertion checks
  from rubric_checks.md, including each row's fact_review under
  rubric_factual_checks.md, valid_case and do_nothing_case, and the
  final_reply_test. A valid object is not proof of semantic truth.
- coverage: required_outcomes, covered_outcomes, and unresolved_outcomes when
  applicable. Missing explicit outcomes are distinct set-level findings.
  For eligible sampling these count the actual control/sample/protected outcome
  ledger, not every repeated artifact cell; use rubric_sampling.md's conditional
  group evidence. The QC denominator remains the authored criterion count.
- issues: type, affected rows, impact, provenance, reason and a concrete witness
  or omission test. Inherited issues need the copied source passage. Use the
  most specific QC category. Weight disagreements are not Overall Quality issues.
- weight_reviews: exactly one per authored row, with row, expected_weight,
  work_kind, source_ids and reason. Work kinds and their 1/3/5 mapping are in
  hg_rubric_qc.py. For unresolved classification use expected_weight null and
  work_kind UNRESOLVED. Every source ID must resolve in the verified checks ledger.
- hard_gates: schema, self_containment, accuracy_acceptance, atomicity, coverage,
  duplicates, weights and contradiction. Each needs result PASS/FAIL/UNRESOLVED
  and a supported reason. These track repairs; they do not change QC thresholds.
- hard_gate_score: null. No extra numeric score is invented from a repair gate.
- dimensions: overall_quality, criteria_weights, category_balance, process,
  agent_centric and negative. Each needs score 1–5 and reason. The helper validates
  derived score bands; semantic Process judgments still need actual evidence.
- unresolved: remaining checks, empty only when the review is complete.
- predicted_all_fail: array of `{row, basis, reason}` for rows predicted to fail
  every run because of a defect already recorded in `issues`; empty when none.
  Basis is one of target_data_absent, required_tool_absent, filter_impossible or
  entity_unreachable. Two or more entries make the verdict FAIL with a score of
  at most 2. This is a pre-run prediction, not verifier all-failing input.
- oe_cross_check (Eval 3 §3.1): `oe_present` (true exactly when an OE input is
  saved). With OEs: `steps` (the saved OE's step labels), one `rows` entry per
  authored row with `oe_step_ids` and `reason` (an empty list is `oe_unmapped`
  and needs `unmapped: {resolution: ROW_DEFECT | OE_GAP | UNRESOLVED, reason}`),
  and `conflicts` (each `{step, row, oe_quote, row_quote, resolution: FIX_ROW |
  FIX_OE | UNRESOLVED, source_ids, reason}`). The writer checks the step labels
  and OE quotes against the saved OE, the row quote against the title, and the
  source IDs against the checks ledger. ROW_DEFECT and FIX_ROW need the row's
  issue; OE_GAP and FIX_OE are reported as `oe_send_back` (an OE defect, not a
  rubric score change); UNRESOLVED keeps the review PARTIAL.

Record one Major per distinct missing explicit Outcome, using rows: [],
outcome_id and criticality. Count it in the numerator only, not as a new authored
row. Count each existing row once at its highest severity. A duplicate issue
needs duplicate_kind COMPLETELY_REDUNDANT or OVERLAP_GROUP. The latter has a
stable group_id and at least two member rows; it contributes one Moderate
numerator after higher-severity deduplication, zero if no members remain. Group
memberships must be canonical and disjoint; no row is counted twice. See
qc_rubric_v10.md for the authoritative overlap rule and evidence requirements.

## Scoring and suggested repairs

Overall Quality follows the rubric-flow-v2 bands in the Eval 3 Local Overrides
(2026-10-09): any Major or Moderate fails; Minor on 5-10% of rows is NON-FAIL 3;
Minor on more than 10% fails; no Major/Moderate and Minor <5% is PASS.
No three-row absolute rule or acceptance-changing gate overrides the QC score.

Weights are NON-FAIL 4 only when 10% or fewer rows are one level off and none
are two levels off (Eval 3 Local Overrides); otherwise FAIL. All equal is PASS. The
reviewer must substantiate work_kind; arithmetic alone cannot establish it.

Artifact/model subjects or literal MCP tool names fail Agent-Centric and are a
Major `non_agent_centric` tally issue on each such row. Nonstandard Agent
forms (possessives such as "The Agent's report states…", bare actions) also
fail Agent-Centric (1–2) and add no tally issue. Under `hg-strict-overrides-v1`, any
negatively framed graded action fails Negative Criteria, even with prompt
authority; descriptive negative facts remain affirmative. A row an Agent passes
by doing nothing (`do_nothing_case` ACCEPT) is a prohibition in disguise.

Severity follows `hg-strict-overrides-v1`: overly_specific is Major,
overly_broad is Major (2026-10-17) and harmless_specificity is Minor. Rows that
would all fail on one Agent error because each embeds the same condition are one
OVERLAP_GROUP.

Save rubric-score through hg_write_output.py. Its receipt reports the QC verdict,
score, authored denominator, exact fractions, weight disagreement rows, repairs,
gate_tier and repair_free. A below-threshold defect remains a suggested repair,
without overriding the QC score. Copy the computed results and input/context
hashes into the report. No OE PASS, creation record, prefill readiness or
publication is part of this evaluation-only workflow.

Incomplete evidence is PARTIAL without an invented score unless an independently
established failing dimension already fixes FAIL. Fix the underlying missing
proof; filling PASS fields is not a substitute for reviewing source records.

Executable factual results cannot be replaced by a declared PASS. Reconcile each
mismatch with a source-backed issue and its failed repair gate; record required
unresolved claims without a manufactured QC count. Exact source names that collide
with the exemplar phrase rule remain unresolved under qc_rubric_v10.md.
