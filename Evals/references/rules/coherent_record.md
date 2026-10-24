# Coherent record and consistency contract (rubric-revision-v10)

Adopted from the 2026-09-22 consistency trial candidate. These are narrow,
explicit boundaries; they do not lower evidentiary standards or expand the
large-audit exception.

## A1. One coherent record

A criterion may grade tightly coupled attributes of one selected source record.
In particular, the first merged PR's identifier and that PR's own merge date may
be paired. The date still has to belong to the selected PR. Selection of the
first PR must itself be verified against the complete relevant candidate set.
Another PR sharing the date does not make a wrong identifier correct.

For this exception, both a correctly paired criterion and correctly split
criteria are acceptable. Do not demand splitting or merging solely because you
prefer the other representation. A partial-success example can show that the
fields can be misstated independently; it does not cancel this explicit exception.

The exception is not permission to bundle unrelated claims from a large search
response, multiple tickets' states or separate write actions. It does not import
unrequested details. It applies to one actual record, one coherent requested
finding and one required output. A comparison or causal finding may continue to
use its necessary operands/premises under existing rules.

For the validator (`Evals/tools/hg_coherent_record.py`), supported record kinds are `pull_request` (number,
merged_at) and `relocation` (person, company, city). Other proposed coherent record
kinds need explicit semantic review; do not mislabel them to pass the helper.
The `coherent_record` exception carries `record_kind`, `source_id`, `entity` and
`fields`. Each required field assertion carries the same source_id and entity,
its actual field name as property and the same outcome ID for the record result.
The linked source must select one visible JSON record with an exact pointer;
fields must exist in that record. The helper cannot establish semantic relevance
or selection correctness by field presence alone; those reviews remain required.

## C1. Coverage decisions precede critique

Record coverage by requirement and required column before judging a rubric.
Ordinary direct coverage stays direct. Existing qualified large redundant audits
may use exact cohort/reconciliation controls plus grounded atomic spot checks.
Their eligibility and limitations must be explicit; size or horizon label alone
does not establish eligibility. Required distinct actions and non-repetitive
outcomes are never waived by this exception.

Do not demand a per-cell quota from a rubric that demonstrably satisfies the
existing exception. A single sampled Completed-ticket cell without the required
controls does not establish complete column coverage. Omitting the whole requested
column or a required delivery is a gap. Preserve exhaustive source verification
of the OE's required cohort. Sampling cannot prove every individual cell right.

Reuse the coverage decision only when relevant sources, requirements and policy
match. Reversal requires new evidence, a policy change or a demonstrated earlier
error. Do not force expansion just because a new reviewer starts another run.

## F1. Numerical corrections must be reproducible

For counts, record the complete matching IDs, repository/entity scope, filters,
time boundary and timezone, deduplication rule, source fingerprint and computation.
Recompute from that membership. A prose assertion, changed filter, incomplete
search or failed lookup cannot override a verified count from the same scope.

When counts disagree, explain the exact membership difference. Mark a missing
or conflicting verification unresolved until reconciled. Unresolved evidence is
not itself proof that the author's count is wrong. When complete evidence proves
the saved answer wrong, report the factual defect; do not preserve it for stability.
Use relevant source attachments before absence-based conclusions.

## T1. Direction of authority

Prompt and clearly incorporated instructions establish task obligations. Source
records establish facts. Eval policy establishes rubric structure. An OE's
sentence saying two fields are "graded together" cannot decide rubric atomicity.
Rubric structure changes do not require rewriting the OE. OE facts and
alternatives still require source verification and cannot excuse bad criteria.

## R1. Stable revisions, with correction permitted

Record stable finding IDs, rule IDs, evidence and dependency fingerprints. Reuse
unaffected verified facts, not previous PASS headings. Reversing earlier advice
requires a concrete new source, rule change or demonstrated earlier mistake and
a counterexample. A prior reviewer is not an authority that can suppress a real
new defect. Recheck changed items plus affected coverage, duplicate, acceptance
and weight relationships; a cosmetic rubric edit does not reopen unrelated facts.

## S1. Historical run-score binding (outside rubric review)

This paragraph applies only to other stages that already consume run scores.
The rubric stage does not read or request verifier, all-failing or batch inputs.
Pairing and splitting can change partial credit even when both structures are
valid. Bind verifier scores, all-fail labels and pass rates to the exact rubric.
Recompute after acceptance or weight changes. Do not compare scores from
different rubrics as evidence of improvement. Follow the existing weight policy;
do not invent a new normalization rule to make different rubrics look equivalent.

## Trial QC content exceptions

The v10 trial also recognizes same_tool_output and shared_email_content as
described in qc_rubric_v10.md. Their source/field/content assertions are checked
by hg_coherent_record.py. They do not permit independent send actions to merge,
and do not make an arbitrary database export one observed tool output.
