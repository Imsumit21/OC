# Executable rubric factual checks

Use this contract in AUDIT. `hg_rubric_facts.py` validates the
`fact_review` on each row of the scoring record's checks ledger.
The supplied rubric JSON stays unchanged. A number asserted in a criterion
is the expected value; a separate reviewer-entered expected value or PASS cannot
override its executable comparison.

Apply [prompt/rubric evidence reliability](prompt_rubric_reliability.md) before
accepting source evidence. Metadata cannot establish a match or mismatch. Add
conditional `evidence_check` to absence/exclusivity claims; incomplete search
coverage stays unresolved. Explicit closed acceptance intervals use `kind: RANGE`
with their exact title quote and the existing source-bound `calculation`; compare
the unrounded source result with the bounds rather than either endpoint alone.

## Review the claim and select its actual source

Inventory acceptance-bearing numbers, dates, source/entity names, classifications,
negative facts and other factual conditions. A source hash proves which bytes
were read, not that the source, grain, period or metric answers the claim.
For every selection, explain why it belongs to the named entity, property,
period, cohort and source. Verify source attribution as well as value: two tables
agreeing numerically does not make their names interchangeable.

`source_ids` refer to the evidence ledger's verified anchors. Each executable
anchor must quote its entire selected JSON value or text excerpt. Narrow the
anchor with its JSON pointer or line range instead of quoting one convenient
number from a larger record. Calculation/selection pointers are relative to
that selected value, not the original file. An empty pointer selects the entire
anchor. Sources must have current hashes and established persona visibility.

Aggregates need the complete relevant candidate set. Record table/repository,
record grain, filters, period/timezone, included record IDs and deduplication
rule in the source/check evidence. Use the native source selection where possible.
A derived source extract additionally needs its original source hash, reproducible
selection/projection and membership evidence; independently establish that the
extract is complete. An extract's hash alone does not prove its derivation.
Never select only the matching answer to hide conflicting records.

For an absence claim, inspect applicable attachment bytes as well as JSON text,
complete pagination/coverage and a known-present control. Empty results alone
are not proof of absence. An unavailable source or incomplete selection remains
UNRESOLVED. Do not invent a contradiction or waive the claim to complete review.

## Row schema

Every row includes:

```json
{
  "fact_review": {
    "complete": true,
    "reason": "All acceptance-bearing facts inventoried and selected sources checked",
    "claims": [
      {
        "id": "F1",
        "quote": "214 MB",
        "kind": "NUMBER",
        "source_ids": ["S1"],
        "reason": "S1 selects the required build's size_mb; the stated unit is MB",
        "calculation": {
          "op": "direct",
          "operands": [{"source_id": "S1", "pointer": ""}]
        }
      }
    ]
  }
}
```

Here S1 is an evidence anchor selecting the actual numeric value `214` and
quoting `214` in full. `214 MB` is an exact substring of the criterion title.
Each claim needs a unique `id`, exact `quote`, `kind`, unique `source_ids` and
specific `reason`. If a quote occurs more than once, include its zero-based
`start` character offset. Quotes cannot come from a rewritten title.

Allowed kinds:

- `NUMBER`: one numeric literal or supported English cardinal, with an optional
  currency/unit and `calculation`. English cardinals include zero through
  nineteen, tens, hundred/thousand/million and supported compounds/hyphens.
  For example, a title quote of `fourteen` computes an expected 14 and must fail
  a matching-source count of 15.
  Supported operations are `direct`, `count`, `distinct_count`, `sum`, `min`,
  `max`, `difference` and `ratio`. The last two take two operands; others take one.
- `DATE`: an unambiguous ISO date or timezone-qualified instant, with
  `selection: {source_id, pointer}`. `comparison` defaults to `exact`; use
  `utc_date` only when the authorized requirement is a UTC calendar date.
- `LITERAL`: an exact source string, with `selection: {source_id, pointer}`.
  This supports immutable names and IDs, not free-form response wording that may
  legitimately vary. A numeric JSON scalar cannot be coerced to a literal string.
- `SEMANTIC`: a source-backed judgment with `status` VERIFIED, CONTRADICTED or
  UNRESOLVED. Quote and explain the actual predicate and source evidence. This is
  a recorded judgment, not executable proof; it cannot satisfy numeric coverage.
- `UNRESOLVED`: the exact claim whose evidence/computation cannot be established,
  with a reason. It may have no source IDs when none is available. It creates no
  automatic QC defect but keeps the review incomplete.
- `NOT_A_CLAIM`: a numeric token that asserts no fact, with a reason. Use it for
  a figure the criterion is *assessing* rather than stating (the "3" in a rejected
  "Day 3 token bump"), the row's own acceptance quantifier (the "one" in "at least
  one finding"), a version or build string, or a number inside a proper name. It
  must cite no source, since declaring a token non-factual and then offering
  evidence for it is contradictory. It satisfies token coverage and does **not**
  keep the review incomplete. Do not reach for it to avoid a hard check: if the
  title is asserting the figure, it is a NUMBER, and if you simply could not bind
  it, it is UNRESOLVED.

The helper requires executable NUMBER/DATE/LITERAL coverage or an explicit
UNRESOLVED or NOT_A_CLAIM claim for every complete numeric literal, supported English cardinal or digit-bearing
title token. A complete ISO date needs one DATE/LITERAL/UNRESOLVED/NOT_A_CLAIM claim; separate
fragments cannot substitute. A proper name such as One may instead use a verified
exact LITERAL source claim. Unsupported quantity phrases stay unresolved. The
helper does not discover all English-language facts: ordinals, prose date
interpretations, implied time comparisons and classifications still require
explicit source-backed review. Never label a
numeric claim SEMANTIC to bypass its executable comparison. Unsupported numeric
representations or calculations remain unresolved until their comparison is
supported. Preserve the submitted title and describe the evidence limit.

## Computation details

An aggregate operand selects an array and may contain:

```json
{
  "source_id": "S2",
  "pointer": "/records",
  "filters": [{"pointer": "/game_id", "equals": "combo_fighter"}],
  "field": "/spend_usd"
}
```

Filters are exact scalar equality tests applied to each record. `field` projects
an array property for sum/min/max/distinct_count; count counts selected records
and does not accept field projection. Source IDs must exactly match the operands.
Complex joins, unsupported filters or other calculations require a verified
source extract or an unresolved check; there is no arbitrary code-expression
field. Selection, membership and grain still need semantic source review.

Empty count/distinct_count/sum requires `allow_empty: true` plus a concrete
`empty_reason`; min/max over an empty selection remain undefined. This technical
option does not prove that the search was complete or absence is true.

Values compare exactly after the declared supported transformation. Numerically
equivalent `214` and `214.0` compare equal. Optional `conversion: {from, to, source_unit: {source_id, pointer}}`
uses only the helper's built-in compatible unit conversions. The mandatory
source_unit selection must execute to the exact source unit named by from, and
its source ID belongs in the claim's source_ids. Verify the original unit from
the actual source; a manually declared unit is insufficient. Arbitrary scale factors are not allowed. Optional
`rounding: {places, mode}` uses HALF_UP, HALF_EVEN or DOWN, with places equal to
the title's displayed precision. Establish the task's rounding convention;
rounding cannot conceal a substantive mismatch. No free tolerance or manually
entered expected result is accepted.

## Factual judgments beyond calculations

For currentness, root cause, status and classification, inspect all applicable
source versions, branches and decision rules. An old timestamp alone does not
make a record irrelevant. A merged approved PR can contradict a never-started
classification even if a ticket status is stale. Define precedence when source
classes overlap; an OE cannot invent it as task authority.

Test each supported alternative against the entire rubric, including totals and
umbrella checks. A row that accepts an alternative is not sufficient if a total
or another row rejects that same valid answer. Link required outcomes to their
actual predicates and test omissions and plausible wrong answers. Preserve
source-supported narrow grouping and sampling exceptions.

## Results and readiness

The helper returns computed comparisons, mismatches and unresolved claims. A
computed mismatch must be reconciled with the actual source and recorded as the
applicable defect; a PASS declaration cannot clear it. Fix a bad source selection
using evidence, not by choosing another source solely to match the title.
A source-backed factual contradiction is Incorrect (Major). Other semantic
findings use the most specific applicable QC category.

Missing proof, ambiguous dates, unsupported transformations and the literal-name
exemplar conflict in `qc_rubric_v10.md` remain unresolved without an invented
failure count. Record mismatches and open defects under QC scoring; required
unresolved facts keep the review incomplete and stale bindings require rechecking. Source-backed semantic judgments are still the reviewing agent's work;
passing this finite helper does not prove arbitrary semantic correctness.
