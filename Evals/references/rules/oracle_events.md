# Oracle Event evidence and scores

Authority: user-supplied Oracle Events/MVP Path requirements and QC components
15 (OE Completeness) and 16 (OE Accuracy), adopted 2026-09-25. Policy
`oracle-events-v2` supersedes golden scoring for the active stage. The old golden
engine and reports are retained only for historical compatibility.

| Dimension | Category | Score |
|---|---|---|
| Completeness | Full critical path: discovery, dependencies, required writes | 5 |
| Completeness | Non-Fail - Non-action or final-response event | 3 |
| Completeness | Fail - Incomplete Oracle Events (critical step missing) | 2 |
| Accuracy | All existing steps accurate when followed literally | 5 |
| Accuracy | Non-Fail - Minor OE Inaccuracies | 3 |
| Accuracy | Fail - Inaccurate Oracle Events | 2 |

The FAIL bands follow the Oracle Events guideline §10, which grades an incomplete
or an inaccurate solution path as Fail. The NON-FAIL 3 band is a local decision
(2026-09-26): §9 of that guideline says `/oe` issues no NON-FAIL at all, while
§10 grades a minor inaccuracy Non-fail and a non-action or final-response event
Moderate. This package resolves that contradiction by keeping one NON-FAIL 3
band for exactly those cases. Missing steps affect
completeness; wrong existing steps affect accuracy; a submission can have both.
The overall score is the minimum of the two components: PASS 5, NON-FAIL 3,
FAIL 2. A proven failure stays FAIL even while other checks are unresolved.
Without a proven failure, unresolved required evidence gives NON-FAIL / PARTIAL
and null scores; intake problems use BLOCKED. Preserve confirmed findings.

Use [QC review examples](oracle_events_qc_examples.md) for concrete mistakes and
valid counterexamples before completing the existing step/coverage checks.

## Internal review record

This JSON is written by the evaluator, never requested as a user input and never
used as a required OE authoring schema. `hg_oe_review.py start` returns the exact
binding fields for the current saved OEs, prompt/context and installed release.
For a binary original upload, retain `source:oe`, inspect it and save its verified
text extraction under `oe` with the source mapping. Both versions remain in the
context fingerprint; a newer canonical text input takes precedence.
The current record is format 2 (`oracle-events-v2`). Copy its binding fields, then add:

- `inventory_complete` (boolean) and `inventory_reason`: whether the reviewer
  derived and examined the full critical path from prompt/source authority.
- `sources`: exact evidence anchors with `id`, `path`, `sha256`, `quote`,
  `visibility` (`VISIBLE`, `INACCESSIBLE`, `UNRESOLVED`) and `access` rationale.
  Optional `pointer` or inclusive `line_start`/`line_end` limits the quote.
  Prompt-incorporated sources use `incorporated_by` and `incorporation_reason`.
  Cite primary source records and tool contracts, not the OE or prior verdict.
- `segments`: partition the complete OE text, including notes, into exact
  Python character offsets `start`/`end` (exclusive), `quote`, `reason`, `role`
  (`STEP`, `CONTEXT`, `RESPONSE_DESCRIPTION`, `NON_ACTION`) and `step_ids`. A step
  segment names the step(s) reviewed below. Context is metadata, not a way to skip
  an asserted instruction. A final-response description or a non-action statement
  ("the agent does not give up") caps completeness at NON-FAIL 3.
- `steps`: unique `id`, `checks` and `rubric_verification`. `checks` has exactly
  `action`, `information`, `tool_service`, `parameters`, `expected_data`,
  `dependencies`. Each has `result`, `reason`, and source IDs for factual checks.
  Results: `VERIFIED`, `MINOR`, `INACCURATE`, `MISSING`, `UNRESOLVED`,
  `NOT_APPLICABLE`. NOT_APPLICABLE needs a reason and is allowed only for tool,
  parameters or dependencies (e.g. first discovery or internal calculation).
  MISSING describes absent material step detail, not uncollected review evidence.
  If absence is the basis, include the scope-bound `evidence_check` under
  [prompt_rubric_reliability.md](prompt_rubric_reliability.md). Record exact
  calculations, operands, cohort, units and observed values in the reason/source
  anchors for derived expected data. Approximate prose is not a numeric tolerance.
- `rubric_verification` within each step: `category` (`OUTCOME`, `PROCESS`,
  `NONE`) and `reason`. PROCESS also needs `why_no_outcome`. This is an advisory
  mapping to verification evidence, not a mandate for one rubric per OE or a
  third scored OE dimension. Apply Eval 3 before requiring any Process criterion.
- `coverage`: unique `id`, `requirement`, `authority_chain`, `step_ids`, `result`
  (`COVERED`, `MISSING`, `UNRESOLVED`) and `reason`. Each chain begins at the exact
  prompt. Include discovery and dependencies needed to satisfy its asks, plus
  every required write/action. Empty step IDs are appropriate for missing steps.
  A missing required action must appear here even if no OE mentions it.
- `format_review`: `checked` (must be `true`), `reason`, and `findings` (empty
  list when the shape is clean). Each finding has `defect` (`NO_DETAILS_OR_EXPECTED`,
  `ARROW_CHAIN`, `MULTIPLE_ACTIONS`, `JSON`, `NO_NUMBER_OR_SERVICE`), `step_ids`,
  an exact `quote` from the OE text and a `reason`. Any finding caps Accuracy at
  NON-FAIL 3; it never FAILs and never replaces a content result. Tool names, IDs
  and query-style wording are not format defects.

The validator computes scores; a self-written PASS field cannot override its
findings. It verifies exact hashes and source quotations, not arbitrary semantic
classification. Registered OE/golden/rubric files and authoring/model metadata
cannot establish factual matches or contradictions. They leave checks unresolved.

Save with `hg_write_output.py oe-review --source <record.json>`. Then save the
matching report with `hg_write_output.py oe --source <report.md>`. Both operations
recheck sources and bindings. New records archive the prior record/report under
`reports/drafts/oe_history/`; supplied OEs are never altered.

## Execution model (`path_review`)

Required reviewer metadata, not a user input or required OE format. Do not ask
an author to rewrite prose OEs as API calls. The model must represent the actual
supplied steps faithfully, including defects. A missing reviewer mapping is an
incomplete review; it is not an authored OE omission.

- `complete` (boolean), `reason`, and `nodes`: map every supplied step. A node
  has a unique simple `id`, `step_ids`, exact `oe_quote`, `mapping_reason`,
  `mode` (TOOL or REASONING), `depends_on` (node IDs), `parameters` (object),
  and `outputs` (object). Multiple nodes may implement one supplied step.
- TOOL nodes name `tool`, `service`, and `parameter_style`: DESCRIPTIVE for
  prose/material inputs, LITERAL for an actual JSON call payload. LITERAL also
  includes the exact `payload_quote` from the OE; parameters must equal it.
  Required missing arguments in a literal call are inaccuracies. Unlisted
  scaffolding in prose is not automatically an omission; assess materiality in
  the six step checks. A REASONING node explains the calculation/decision and
  its evidence; it does not invent an executable tool.
- Tool/service membership and primitive/union parameter types come from the
  bundled catalogs. An unknown tool stays unresolved pending a supported alias
  or current schema. A source-selected `runtime_schema` may give `source_id`
  and `pointer` (relative to that anchor) for an actual schema object with
  `name`, `service`, and `parameters` using the catalog format. Merely supplying
  an unavailable schema cannot bypass service checks. Record its provenance.
- Preserve literal wrong names. For a harmless descriptive parameter-name
  imprecision only, `parameter_aliases` can map a supplied name to an object
  with `canonical`, exact `oe_quote`, `source_ids`, and `reason` proving an
  unambiguous mapping without a changed outcome. This records Minor; it is
  not a silent repair of a broken literal payload. Tool aliases likewise need
  source-supported mapping reasons; record any imprecision in the step checks.
- Parameters may contain `{"$ref":"NODE.output"}` anywhere, including lists.
  References add dependencies. `input_bindings` can also relate a hardcoded
  downstream value to its upstream source: `from_node`, `output`,
  `parameter_pointer` (JSON pointer into the parameters), and `reason`.
  Use bindings for repeated IDs, recipients, filters, dates and values; compare
  derived values after a documented reasoning node, not as if unchanged.
- Outputs use named declarations. SOURCE has `source_id`, `pointer` relative
  to that source anchor, and optionally `expected` plus exact `expected_quote`
  from the OE. The source anchor must quote its entire selected value; the
  helper compares values and types. GENERATED has a primitive `type`,
  `source_ids` establishing creation/derivation capability, and `reason`.
  It is a future symbolic result, not a fabricated existing identifier.
  UNRESOLVED has a reason. Missing/unresolved producers never justify cascaded
  wrong-ID or type findings. Cycles in the faithfully mapped supplied path are
  inaccuracies; absent reviewer nodes are unresolved mapping gaps.
- `feasibility` has exactly `data_access`, `tool_capability`, `preconditions`,
  `completion`. Each has `result`, `reason` and supporting `source_ids` for
  settled findings. Results: SUPPORTED, BLOCKED, UNRESOLVED, INCOMPLETE.
  INCOMPLETE requires an authored omission already recorded in coverage or
  step checks. BLOCKED requires an `evidence_check` using DIRECT contradiction
  or the complete ABSENCE contract. Cite readable ACL/policy evidence when
  proving access denial. A tool catalog alone cannot prove data or access.
- `runtime`: `status` (NOT_NEEDED, UNAVAILABLE, OBSERVED) and `reason`.
  NOT_NEEDED means static evidence suffices. UNAVAILABLE means a necessary
  runtime uncertainty remains, not merely that no connection exists. OBSERVED
  adds `effect: READ_ONLY`, `receipt_source_id`, optional `receipt_pointer`,
  and nonempty `bound_source_ids`. The selected JSON receipt must itself
  contain `effect: READ_ONLY`, `task_fingerprints` from
  `hg_oe_path.task_fingerprints(context(root)['manifest'])`, and
  `source_fingerprints` mapping each bound source path to its SHA-256. The
  receipt cannot bind itself. Save authentic observations with provenance;
  never invent successful runtime evidence. Stale observations are unresolved.
- `upstream_blockers` defaults to `[]`. Each confirmed item names a
  `requirement_id`, `feasibility_field` pointing to a supported BLOCKED check,
  `reason`, `source_ids`, `all_authorized_routes_ruled_out: true`, and
  `alternatives_reason`. Explain why the obstacle applies to the task, not
  just this OE's chosen route. Do not claim exhaustive alternative-route proof
  from a boolean; evidence relevance and that explanation require review.

The validator checks mechanical consistency and evidence bindings; it does not
execute tools or establish arbitrary semantic truth. See the source-grounded
Michelle delivery regression fixture in `tools/tests/fixtures/oe_delivery_397a.json`.
That example covers delivery only, not a submitted OE or the full task solution.

Diagnostics are computed from the existing QC findings and evidence:
SUPPORTED requires no omissions, inaccurate steps or unresolved checks;
BROKEN means a confirmed inaccurate step; otherwise unresolved evidence takes
UNRESOLVED, and confirmed omissions take INCOMPLETE. A broken path can also have
unresolved checks, which remain listed. Minor imprecision can retain a supported
path when it cannot change the outcome. Task solvability is SUPPORTED_BY_OE only
for a supported path, otherwise NOT_ESTABLISHED, unless a separately supported
UPSTREAM_BLOCKER warrants Prompt follow-up REQUIRED. No prompt files are changed.

Historical format-1 reports remain readable but cannot be republished as current
format-2 reviews. Current scored/bound reports require the path model and matching
diagnostics. Intake-only unscored reports do not need a fabricated path model.

## Report verdict block

Use exact computed values; hashes below are placeholders for real receipts.

```text
### FINAL VERDICT: PASS
Score: 5
Execution status: COMPLETE
Completeness score: 5
Accuracy score: 5
Path feasibility: SUPPORTED
Task solvability: SUPPORTED_BY_OE
Prompt follow-up: NONE
Review policy: oracle-events-v2
Reviewed OE SHA-256: <hash>
Review context SHA-256: <hash>
OE record SHA-256: <hash>
Eval version: <installed release version>
Eval release SHA-256: <hash>
Evaluator model: Opus 5.5 (claude-opus-5-5), xhigh effort
Next action: Review complete
Evidence limits: Static universe/tool evidence; no live writes executed
```

For a missing or wrong step use FAIL and score 2; for minor, non-action or
final-response defects use NON-FAIL and score 3; report the actual 2/3/5
component scores. Unresolved reviews without a proven failure omit all three
score lines. A blocked intake report
can omit binding fields if no valid artifact could be bound; identify the gap.
Old golden reports remain readable under `golden`, never interpreted as OEs.
