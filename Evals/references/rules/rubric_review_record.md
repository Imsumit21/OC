# Historical rubric creation record (retired)

This is archival schema documentation for pre-evaluation-only records. Do not
follow its creation/publication procedure. Current `/rubric` uses only
[review_scoring.md](review_scoring.md) and [rubric_checks.md](rubric_checks.md).
The former writer routes are disabled; this document has no operational authority.
Its per-row `valid_case` and whole-set `final_reply` test now live in the
format-5 scoring record (`rubric_checks.md`, with the `do_nothing_case`).

Read this in CREATE mode after staging a proposal. This replaces duplicate prose
ledgers with one machine-checkable record; it does not add rubric fields or alter
the final JSON/download path. Keep explanations concise but concrete. Do not fill
reasons with PASS labels, repeat the title as evidence, or invent test outcomes.

The Agent performs the semantic review. The helper checks record completeness,
cross-references, exact source quotations, recorded results and binding to the exact draft. It cannot prove
that a quoted source is true, a requirement list is exhaustive or a declared test
result is correct. A populated record is not a substitute for doing the review.

## Save and publish

1. Save `rubric-draft` and read its receipt.
2. Write a review record in the format below. Read the saved proposal's five fields
   for each row. Test concrete candidate answers against the actual predicates.
3. Save it with `python3 Evals/tools/hg_write_output.py rubric-review --source "<record.json>"`.
   It is saved at `Evals/task_inputs/reports/drafts/rubric_review_record.json`.
4. Use the returned `review_record_sha256` as `Review record SHA-256` in the report.
   Summarize findings in `3_rubric.md` and link the record rather than copying all
   ledgers into prose. A ready CREATE report must match this record's hash.
5. Publish through `rubric-json` only after all checks clear. A record with issues
   can be saved for diagnosis, but cannot authorize publication. If intake or
   source gaps prevent a complete record, save an unready report; do not invent
   rows, evidence or a record hash. Each new draft archives the previous record.

Changing a saved record archives its prior record, ready report and final prefill.
The updated record needs a new matching review. Identical re-saves are harmless.
AUDIT mode remains report-only and does not need this publication record. Apply the same authority, alternative and overlap review in the audit findings. Both modes require the separate computed scoring record for a scored report; see [review_scoring.md](review_scoring.md).

## JSON contract

Top-level keys:

| Field | Contents |
|---|---|
| `format_version` | Integer `4` for `rubric-revision-v10` (publication-record shape is retained; scoring records are format 4 with mandatory checks and executable factual evidence in both modes); stale records cannot authorize new publication |
| `review_policy`, `review_iteration`, `reviewed_json_sha256`, `review_context_sha256` | Exact values from the latest draft receipt |
| `requirements` | Complete authorized requirement ledger described below |
| `rows` | Exactly one record per proposal row, numbered from 1, including the assertion inventory below |
| `set_checks` | The nine named checks below, each with `status` and `reason` |
| `set_tests` | Whole-answer tests described below |

Each requirement has:

```json
{
  "id": "Q1",
  "authority": "Exact prompt/incorporation chain and quoted instruction",
  "authority_chain": ["P1"],
  "accepted_result": "Expected value or objective semantic rule and valid alternatives",
  "output": "Required artifact/audience, property, condition and time",
  "source_evidence": "Source path, record/pointer and observed value; persona visibility",
  "outcomes": [
    {
      "id": "Q1-O1",
      "entity": "The specific ticket, metric, destination or permitted set",
      "property": "The single required reported fact, final state or other result",
      "output": "Required artifact/audience and applicable condition/time",
      "accepted_result": "Expected value or objective semantic rule with valid alternatives"
    }
  ],
  "rows": [1],
  "coverage_mode": "direct",
  "coverage_reason": "How the mapped predicates cover this authorized outcome"
}
```

`rows` must reference current criteria. Reverse mapping in each criterion must
agree. Do not drop an uncovered requirement to make the ledger validate: repair
the proposal, or keep the report unready. Unrequested handbook rules and invented
recap duties must not enter this ledger as requirements.

Build `outcomes` before drafting. IDs are unique across the record. Each inherits
its requirement's authority and source evidence; use separate requirements when
those differ. Each outcome needs coverage, and each row's `atomicity.outcome_ids`
must agree with its requirement links. Review the inventory against the actual
titles and instructions: an identifier named "all ticket statuses" cannot hide
independently requested results. Merge duplicate descriptions of one obligation.
Ordinary ticket/property outcomes and distinct required outputs stay separate.
Qualifiers, operands and premises of one finding do not create extra outcomes.

For a qualifying large audit, `coverage_mode: "sampled"` additionally requires:

```json
{
  "sampling": {
    "eligibility": "Why the task qualifies under long_horizon.md, beyond its label",
    "controls": [1],
    "spot_checks": [2],
    "limitations": "Which unsampled errors can escape; why this permitted compression is adequate"
  }
}
```

Both lists must reference rows mapped to that requirement. Use actual overall
cohort/reconciliation controls, not merely populated cells. Do not claim that
sampling detects every wrong cell. No fixed number of spot checks is imposed.
Distinct non-repetitive deliverables still require direct coverage.
For sampled coverage, inventory the cohort/reconciliation outcomes and selected
atomic spot checks, not every repetitive cell. The requirement retains the full
cohort scope and limits. Sampling never licenses an all-cells-correct mega-row.

Each criterion record has:

```json
{
  "row": 1,
  "requirement_ids": ["Q1"],
  "predicate": "The exact acceptance boundary of this saved title",
  "output": "The required artifact/audience, property, condition and time",
  "source_evidence": "Exact supporting path/record/value, or eligible reused evidence",
  "valid_case": {
    "example": "Concrete correct answer, including a valid alternative where one exists",
    "result": "ACCEPT",
    "reason": "Why the actual criterion accepts it without extra obligations"
  },
  "near_miss": {
    "example": "Concrete plausible wrong answer to this criterion's own requirement",
    "result": "REJECT",
    "reason": "The actual predicate that rejects this wrong result"
  },
  "atomicity": {
    "status": "PASS",
    "reason": "One required result, or the specifically justified atomic exception",
    "outcome_ids": ["Q1-O1"],
    "independence_test": {
      "classification": "ONE_RESULT",
      "example": "Concrete attempted partial-success answer; for a single measurement, 214 MB versus 214.0 MB expresses the same result",
      "satisfied_outcome_ids": [],
      "failed_outcome_ids": [],
      "reason": "Why the apparent parts cannot be independently satisfied authorized outcomes"
    },
    "exception": null,
    "split_plan": []
  },
  "restriction_review": {
    "reason": "Requested result only; no additional method, format, date, owner or surface restriction",
    "restrictions": []
  },
  "supporting_fields": {
    "status": "PASS",
    "reason": "Title read alone, compared with justification/evidence; supporting fields neither add nor widen acceptance conditions"
  }
}
```

## Factual inventory (required for each row)

Add `fact_review` to every row using the exact schema and source-selection rules
in `rubric_factual_checks.md`. Reuse those claim IDs and evidence anchors in the
scoring ledger; both paths execute the same comparisons. The abbreviated row
above still needs this factual inventory and the assertion inventory below before
it is complete. An empty fact list is appropriate only when the title has no
acceptance-bearing factual claims; explain why. Recorded completeness cannot
waive missing digit-bearing claims or an unresolved source.

## Assertion inventory (required in format 4)

Each row additionally has `assertion_inventory`. Build it from the actual saved
criterion before accepting its outcome decomposition. It has Boolean `complete`,
a concrete `reason`, and a nonempty `assertions` array. Inspect all three text
fields; category/weight are covered by their existing checks. Do not mechanically
split words, repeat an entire sentence as an opaque assertion, or hide several
business entities under a collective label.

```json
{
  "assertion_inventory": {
    "complete": true,
    "reason": "One implementation-status result; no extra requirements in supporting fields",
    "assertions": [
      {
        "id": "A1",
        "field": "title",
        "quote": "identifies begin_level as already implemented",
        "role": "REQUIRED_RESULT",
        "outcome_id": "Q1-O1",
        "kind": "ENTITY_PROPERTY",
        "entities": ["begin_level"],
        "property": "reported implementation status",
        "reason": "The task requires this event's implementation status"
      }
    ]
  }
}
```

Each assertion has a unique row-local `id`, `field` (title/justification/evidence),
an exact nonempty `quote` from that field, `role`, and concrete `reason`. A short
entity/property phrase is fine if the explanation states the actual assertion;
do not use a generic quote such as "The Agent". Overlapping excerpts are allowed
when a shared predicate applies to several named entities.

- **REQUIRED_RESULT:** needs `outcome_id`, `kind`, nonempty unique `entities`, and
  `property`. Its authority comes from the linked requirement. It must be stated
  in the title; finding it only in a supporting field exposes a hidden condition.
  Record each independent required result separately even when an old outcome
  map combines them. More than one required assertion in one criterion blocks
  publication, including when all point to the same outcome ID. Repair the
  inventory/outcome map and existing independence witness/split plan together.
- **QUALIFIER:** needs `outcome_id` and a reason why it defines that one result,
  e.g. a measurement's date, market or unit. Do not relabel a separately required
  status, deadline, owner, stall or data-quality finding as a qualifier.
- **SUPPORTING_EVIDENCE:** needs `outcome_id` and `omission_test` with `example`,
  actual `result` (ACCEPT/REJECT/UNRESOLVED) and `reason`. Give a correct completion
  that omits the source narrative. It must still pass; otherwise that detail is
  acting as another acceptance condition. Supporting fields may locate records
  and explain verification, but cannot silently require the agent to report them.
- **UNREQUESTED_REQUIREMENT:** `outcome_id: null`, with `repair` describing removal
  of the unsupported acceptance condition. Do not create a rubric row for an
  unrequested detail. It may remain as ungraded source evidence where useful.
- **UNRESOLVED:** `outcome_id: null`, with `repair` explaining the needed authority
  or decomposition check. This remains unready; do not guess a role to publish.

Required-result kinds:

| Kind | Meaning |
|---|---|
| ENTITY_PROPERTY | One actual entity's status/value/property. Multiple listed entities require separate criteria, even with an identical value. |
| RELATIONSHIP | One required comparison, discrepancy or causal conclusion. Add `conclusion` stating that single finding; explain why operands are not separate required outputs. It is not an escape hatch for discrepancy plus stall or implementation plus separately required data quality. |
| IDENTITY_SET | Literal identifier membership only. Requires `property: "membership"` and the existing identity_only_set exception. "These events are implemented" and "these systems are approved for removal" assign a property to every member and are not identity-only membership. |
| AGGREGATE | One aggregate/invariant; requires aggregate_invariant or an eligible large_audit exception. It cannot secretly grade every member's result. |
| DESTINATION | One destination identity; requires destination_identity. |
| ATOMIC_CELL | One naturally indivisible requested cell; requires atomic_cell. |

Exactly one required assertion may clear a row, except the documented
coherent_record field group; its binding must agree with the row's
existing outcome links. Qualifiers and supporting evidence do not add required
outcomes. Their classification still needs semantic review. The helper verifies
quotes, counts, declared roles, entity cardinality and mappings. It cannot infer
omitted assertions or prove a RELATIONSHIP/QUALIFIER label is truthful. Complete
real partial-success and omission tests instead of treating a populated record
as proof. AUDIT uses the same semantic rules and reports exact split/removal
findings; the publication record remains required for CREATE.

Record **actual judged behavior**, not the hoped-for result. Case `result` can be
ACCEPT, REJECT or UNRESOLVED. A valid case rejected or near miss accepted blocks
publication. Check `status` can be PASS, ISSUE or UNRESOLVED; only PASS clears.
For atomicity, `classification` is ONE_RESULT, INDEPENDENT_RESULTS or UNRESOLVED.
Use an example about the current title, not the illustrative measurement above.
ONE_RESULT must link exactly one semantic outcome; the helper checks the count,
but the reviewer must check whether the inventory itself conceals a bundle.
INDEPENDENT_RESULTS needs nonempty, disjoint satisfied/failed ID lists covering
all linked outcomes and a `split_plan` containing one singleton ID array for
each. For example, with O1 = report ENG-2410 Done and O2 = report ENG-2414 Done:
"ENG-2410 Done; ENG-2414 In Progress" satisfies O1 and fails O2; the split plan
is `[["O1"], ["O2"]]`. Record ISSUE. Even a contradictory PASS cannot publish.
UNRESOLVED remains unready. Use an empty split plan for ONE_RESULT/UNRESOLVED;
their satisfied/failed arrays may be empty when no partial-success witness exists.

`exception` is null or an object with `kind` and a specific `reason`. Allowed
kinds: `destination_identity`, `identity_only_set`, `aggregate_invariant`,
`atomic_cell`, `large_audit`, `coherent_record`. Explain eligibility and the independence test;
never invent a "same_status", "one_partition" or generic "same_source" exception.
For coherent_record, record kind, source ID, entity and field names explicitly;
see `coherent_record.md`. One batch response containing many records is not one record.
An exception cannot override independently required outcomes. A large-audit
exception row must belong to the mapped sampled controls/spot checks; each
control/spot check still grades one result. Keep causal premises and comparison
operands with their single finding, normally with `exception: null`.

An exact identity-only list may be one outcome. A list pairing separate members
with statuses or amounts is multiple outcomes. The helper does not infer these
semantics from English text or prove that reviewer-supplied examples are truthful.

`set_checks` must contain exactly these keys, each with `status` and a substantive
`reason`: `atomicity`, `overly_specified`, `self_contained`, `process_supervision`,
`duplicates`, `contradictory`, `coverage`, `accuracy_authority`, `weights`.
Use PASS with an explanation for a vacuously satisfied check (e.g. no Process);
do not invent Process rows. These are checks, not new numerical dimensions.

`set_tests` contains:

- `valid_completion`: `example`, `result`, `reason`. A complete task-valid solution
  must be accepted by the entire set, including supporting fields.
- `final_reply`: the same fields plus `authority`. Test correct artifact delivery
  with a concise completion reply when no detailed recap is requested. If the
  prompt requires reply content, include that content and quote its authority.
  For answer-only tasks, test the requested answer. Never impose “done is always
  enough” or “every artifact fact must also appear in chat.”
- `mutations`: at least one wrong-result test for each requirement, with
  `requirement_id`, `example`, `result`, `reason`, `caught_by` (current row numbers).
  Start from the valid completion, change only that required value/status/scope,
  omit that delivery, or change its audience. Identify which actual predicate
  rejects it. A rejected mutation needs a nonempty catching-row list mapped to
  its requirement. An accepted/unresolved mutation uses `caught_by: []` and blocks
  publication. With permitted sampling, test an error the claimed controls own
  and explicitly disclose unsampled blind spots in `sampling.limitations`.

Content tests must use meaningful wrong content, not only an entirely absent
artifact. Example: change a required 6.99 metric to 0.00 while preserving the
sheet structure and all other required outputs. If no predicate catches it,
record the coverage gap and revise; do not change the expected answer.

## Regression examples for evaluator maintenance

`Evals/tools/tests/fixtures/rubric_semantic_cases.json` contains isolated semantic
cases. `rubric_regression_cases.json` adds complete-set and acceptance-boundary
cases from the freeze review. Use their stated scope: do not flag missing coverage
in excerpts. During maintenance, save actual judgments before comparing against
the separate expected file with `hg_check_rubric_cases.py`. The comparator checks
agreement only; it does not run a model or independently judge the cases.
`rubric_atomicity_cases.json` and its separate `rubric_atomicity_expectations.json`
add partition, same-status, multi-repository, report/update and valid combined
controls for v5. Pass the latter with `--expected` when comparing those cases.
Do not load the entire fixture corpus on every task. Keep regression results
separate from the task's CREATE evidence; passing fixtures never certifies a task.

## Authority, alternatives and overlap (retained in format 4)

Add `sources`, `alternative_review` and `overlap_review` at the top level.
Each source has `id`, `path`, `sha256`, an **exact** `quote`, `visibility`
(VISIBLE/INACCESSIBLE/UNRESOLVED), and `access` explaining the assigned persona's
access. Use an RFC 6901 `pointer` for JSON so the quote must occur in that record,
not an unrelated record elsewhere in the file. Plain-text anchors should retain
record/line provenance. The helper checks bytes and quote presence, not whether
an excerpt is exhaustive, accurately extracted, authorized or logically supports
an assertion. Use original text or a provenance-preserving extraction; a generated
summary is not primary evidence. Reuse source IDs rather than repeating reads.

Each requirement's `authority_chain` lists source IDs, starting with an exact
passage in the actual saved prompt. Later instructions need `incorporated_by`
(the previous source ID) and `incorporation_reason`. Verify the prompt genuinely
incorporates those instructions. Official status, injection, a golden assertion,
or permission to research facts is not incorporation. A prompt asking to fix
records does not choose new cards over in-place edits. A prompt asking for clear
status does not prescribe exactly two headings.

For **every row**, inventory restrictive clauses across title, justification
and evidence in `restriction_review.restrictions`. Each item has `field`
(title/justification/evidence), exact `quote`, `status` (AUTHORIZED/UNSUPPORTED/
UNRESOLVED), and `reason`. AUTHORIZED needs `authority_chain`; other statuses
need a concrete `counterexample` (or the candidate whose validity is unresolved).
An empty array requires an explanation confirming the whole row was checked.
Format, order, method, owner, date, destination, permitted branches and final-reply
requirements all count. A supported restriction requires actual authority;
copying the golden's preferred route is insufficient. Failed/unresolved entries
prevent publication even if the row or set otherwise says PASS.

`alternative_review` has `complete` (Boolean), `source_ids`, `reason`, and
`branches`. Inspect the **whole** main golden and alternative notes plus prompt
flexibility. Explain an empty inventory; do not omit alternatives to pass.
For each advertised or source-permitted branch, record:

```json
{
  "id": "A1",
  "source_id": "G1",
  "quote": "Exact passage describing the alternative",
  "validity": "SUPPORTED",
  "authority_chain": ["P1"],
  "example": "Concrete complete valid solution using this alternative",
  "tested_rows": [1, 2],
  "rejecting_rows": [],
  "result": "ACCEPT",
  "reason": "Compare this solution to every actual predicate, including supporting fields"
}
```

`tested_rows` must include every current row exactly once; `rejecting_rows`
identifies actual failures. Test equivalent outputs against the full set, not
just one convenient criterion. `validity` is SUPPORTED/UNSUPPORTED/UNRESOLVED:
a golden's unsupported alternative is a golden defect, not a reason to relax a
correct rubric. Explain unsupported branches; supported branches need authority.
A supported branch rejected or unresolved by the set blocks publication.

`overlap_review` has Boolean `complete` and a concrete `reason`. Compare all rows
by entity/property/output/condition/time. Use consistent outcome IDs for the
same obligation. The helper flags reused outcome IDs and identical declared
entity/property/output units. Reviewers must also catch paraphrased overlap and
umbrella rows that repeat narrower checks. Correlated model behavior alone proves
nothing, but rows that would all fail on one Agent error because each embeds the
same acceptance condition form one OVERLAP_GROUP under `hg-strict-overrides-v1`.
A separately requested document and final reply are distinct outputs;
counting both is allowed. Valid aggregate controls measure a distinct aggregate
outcome; they must not regrade every child result. All independent result bundles
still follow the atomicity rules above. Older format 2/v5 and format 3/v6 records cannot authorize a
new publication.

For plain text or SQL containing multiple records, add inclusive one-based
`line_start` and `line_end` to constrain the quote to the cited record/statement.
The helper checks the full source hash plus the selected lines. Do not combine
line bounds with a JSON pointer. Retain enough surrounding context to evaluate
contradictions; an exact excerpt is not evidence that omitted context is irrelevant.

For calibration maintenance, `rubric_assertion_cases.json` includes the user's five analytics
event examples plus corrected and valid single-result controls. Each case states
its limited task requirement so an unrequested date is not confused with a
necessary date qualifier. These are semantic calibration cases and validator
fixtures, not verified source records from a live task or model-accuracy results.
Do not load the full test corpus during ordinary task intake.

Both CREATE and AUDIT require `rubric_checks.md` and the executable factual
contract in `rubric_factual_checks.md`. Reuse exact sources, atomicity tests and
assertion inventories; do not substitute a publication record for the scoring
record. Non-Agent wording, computed factual mismatches and unresolved facts block
publication even if a review declares PASS. Use `qc_rubric_v10.md` for overlap
group counting and documented atomicity exceptions.
