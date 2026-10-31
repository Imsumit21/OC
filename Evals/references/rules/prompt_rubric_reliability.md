# Prompt and rubric evidence reliability

The shared `task-quality-v1` package retains `prompt-rubric-reliability-v1` source
safeguards and release binding. Its prompt policy is `prompt-source-checks-v2`:
format-2 premise records also bind the mandatory Unique Ground Truth comparison.
Existing QC scores, severities, weights, atomicity exceptions and sampling policy
remain authoritative. OE policy remains `oracle-events-v2`; its scoring contract
is separate in [oracle_events.md](oracle_events.md). Rubric evaluation still
preserves supplied criteria and only suggests repairs.

## Use the installed release

Resolve helpers from the installed skill's package, not from an older copied
`Task_Examples/.../Evals` directory. Keep task inputs separate from policy copies.
Run `python3 Evals/tools/hg_eval_release.py snapshot prompt` (or `rubric`). This
verifies the complete installed manifest and returns the `eval_release` object
for the internal record. A missing, changed or partial package must be restored
before issuing a scored audit; it is not a task-quality failure.

Every scored prompt/rubric report includes `Eval version` and `Eval release
SHA-256`, matching its bound record. These identify the exact package, not just
a directory name or the word v10. The writer checks them. Older reports remain
readable but cannot be reissued as current without a new evidence review.

For a batch, use `hg_eval_release.py summarize rubric <report-path> ...` or the
prompt equivalent. It separates current bound records, historical/unbound
records and invalid bindings. Do not merge those groups into a current-version
pass rate. An audit pass rate is not evaluator precision: precision requires
independently established labels and a confusion matrix. This inventory does
not revalidate source evidence or certify historical findings.

## Primary evidence and search scope

`07_Dynamic_Context.md`, difficulty notes, run summaries, audit reports and model
outputs are authoring/review metadata. They can help locate sources but cannot
prove a workplace fact or its absence. The helper also recognizes registered
input roles, including renamed uploads; `source_role: AUTHORING_METADATA`,
AUDIT_REPORT or MODEL_OUTPUT identifies non-primary derived material. Keep
original provenance on extracted sources. A valid hash does not establish truth.

Verify the claimed entity, property, time window, source attribution, filters,
units and correction scope. Read source versions and applicable static SQL
before deciding that a premise or criterion is wrong. A real task-specific
injection is part of the proposed world; authoring commentary is not.

For factual claims, non-primary evidence becomes UNRESOLVED **before** computing
a match or contradiction. It cannot establish either PASS or Incorrect. Do not
copy a reference answer into the rubric to resolve disagreements; inspect the
underlying records. Correct alternative wording must remain accepted unless the
prompt/source explicitly requires a particular literal or classification.

### Absence and exclusivity

Empty JSON search results prove only the stated JSON scope. Inspect relevant
attachment contents, repository exports and tag/ref inventories, table comments
and applicable SQL overlays. A stripped checkout's empty `git tag -l` is not
proof that the exported repository has no tags. A failed regex/command is not an
empty successful search. Use `rg -F` for literal discovery and retain exit/errors.

Each absence/exclusivity inference needs `evidence_check` on its fact claim:

- `method: ABSENCE`, `scope`, `reason`, `errors` (an explicit array).
- `surfaces`: one entry for each of JSON, ATTACHMENTS, REPOSITORY_FILES,
  REPOSITORY_REFS, TABLE_METADATA and INJECTION. Each has `kind`, `status`
  (COMPLETE/INCOMPLETE/NOT_APPLICABLE), `source_ids`, and a concrete `reason`.
  Inspect only relevant surfaces; justify NOT_APPLICABLE. COMPLETE needs exact
  evidence anchors or saved search receipts. Document original source hashes
  and extraction/selection when using derived text or inventories.
- `positive_control: {source_id, quote}` identifies a known-present record
  in the applicable search scope, demonstrating that the lookup worked.

Errors, incomplete relevant surfaces and JSON-only receipts mislabeled as
attachment/repository coverage leave the fact unresolved. Zero count results
also require this evidence. One positive counterexample can refute an absence
without exhaustively searching the universe. For direct positive evidence or
a phrase that is not an absence inference, use `method: DIRECT`, `reason`,
`source_id` and `positive_evidence` (an exact source quote). The helper checks
record consistency; relevant-scope selection remains a semantic judgment.

## Prompt premise record

Prompt quality already requires tight-identifier, state and relationship checks.
Record those checks before saving a scored report or any numerically scored UGT
dimension, even in an otherwise unscored report. Do not grade requested new
outputs or explicit hypotheses as false assertions of existing facts.

Run `hg_prompt_checks.py start` to obtain binding fields, then save the completed
internal JSON with `hg_write_output.py prompt-checks`. Its fields are:

- Binding fields from start: `format_version: 2`, `eval_release`,
  `reviewed_prompt_sha256`, `review_context_sha256`. Format-1 records are historical;
  a current report needs a new review under `prompt-source-checks-v2`.
- `sources`: existing exact-path/hash/quote/visibility/access anchors. See
  [source fields](rubric_checks.md#sources-and-instruction-coverage); authority
  chains start at the actual saved prompt, and incorporated instructions record
  `incorporated_by` and `incorporation_reason`.
- `inventory_complete`, `inventory_reason`, `other_checks_complete`.
- `clauses`: partition the entire prompt using exact `start`, `end`, `quote`,
  `role` (REQUEST/PREMISE/HYPOTHESIS/CONTEXT), `premise_ids` and `reason`.
  Requests can contain assumed existing entities and link to their checks.
- `premises`: unique `id`, exact prompt `quote` and `start`, `kind`
  (EXISTENCE/STATE/RELATIONSHIP), `reason`, and `fact_review` using the rubric
  factual-check schema, with conditional absence evidence above. The prompt
  itself cannot prove its own premise. Every premise needs source checks;
  quoted numeric facts use executable comparisons or remain unresolved.
- `unique_ground_truth`: the dimension-specific comparison below. It is required
  in every format-2 record; an incomplete review uses the explicit no-score form.
- `other_failures`: supported failures from other existing Eval 1 dimensions,
  each with `dimension`, `reason`, `source_ids`; empty when none. Truthfulness
  findings belong in premise checks and UGT findings in `unique_ground_truth`,
  never in this list. Complete all original phase tables.
- `verdict`, `verdict_score`, `execution_status`, `verdict_reason`: retain
  existing prompt bands. Confirmed contradictions/other supported failures
  require FAIL. Missing evidence alone cannot produce FAIL. An incomplete
  review remains PARTIAL/BLOCKED, with no numeric NON-FAIL score.

The report includes `Reviewed prompt SHA-256`, `Review context SHA-256` and
`Prompt record SHA-256`, plus the release fields. Save through the existing
`prompt` writer. Unscored intake/evidence-blocked reports with no definitive UGT
verdict or numeric UGT score can still be saved without inventing a completed record. An aggregate
unscored or FAIL verdict does not bypass binding for a scored UGT dimension.
The internal record is an evidence ledger, not a rewritten prompt, second
reviewer or additional contributor input.

## Unique Ground Truth comparison

Apply Eval 1 §2.1 before **every scored UGT verdict**, including PASS within an
overall FAIL. Test the strongest plausible alternative and account for every
explicit option; eliminating one option does not resolve the remaining choice.
Apply its five checks to each material difference: newer source, authority,
source identity, scope and same material result. A later applicable update for
the same issue and scope can resolve an earlier statement without explicitly
announcing replacement. Respect cutoff dates and prompt-specified source priority;
retain unaffected requirements when an update changes only part of the task.
Compare concrete decisions, writes, destinations and contents. One coherent
procedure, a leading reading, the same destination, or resolving only one part
of the task is insufficient for PASS. Cite the resolving evidence in each
comparison's existing `reason`, `evidence` and `challenge` fields.
Two supported readings with an unresolved material difference in one required
outcome establish FAIL without completing every other task deliverable.

In a complete `unique_ground_truth` object:

- `complete: true`, `verdict: PASS` with `score: 5`, or `verdict: FAIL` with
  `score: 1` or `2`; `reason` and `evidence_limits: []`. UGT has no scored NON-FAIL
  band. A UGT FAIL requires aggregate FAIL with a score no higher than its own.
- `alternative_search_complete: true`, `alternative_selection_reason`, and
  at least two `readings`. The first reading leads; each has a unique `id`,
  `interpretation`, `support` and `material_result` with nonempty `decision`,
  `writes`, `destinations`, `contents`. Describe no-write outcomes explicitly.
- Each `support` or `evidence` array contains `{source_id, quote}`. Quotes must be
  exact substrings of verified source passages; sources must be visible and
  primary. Prompt text is instructional authority, not proof of its own factual
  premises. Metadata, reports, later rubrics/OE and model answers cannot resolve
  the prompt's outcomes.
- `comparisons` contains one entry per alternative, with `alternative_id`,
  `resolution`, `reason`, `evidence` and `field_comparison`. Each of the four
  material fields has `relation: SAME` or `DIFFERENT` and a concrete `reason`.
  `SAME_MATERIAL_RESULT` requires all four SAME; equivalent meaning need not use
  identical strings. `UNRESOLVED_MATERIAL_DIFFERENCE` requires at least one
  DIFFERENT and makes UGT FAIL. PASS cannot retain this resolution.
- `EXCLUDED` and `AUTHORIZED_VARIATION` additionally require an `authority_chain`
  from the actual prompt to the resolver, whose final source is quoted in the
  comparison evidence. `AUTHORIZED_VARIATION` also needs `authority_kind`
  (`EXPLICIT_DELEGATION` or `OBJECTIVE_ACCEPTANCE_BOUNDARY`), `acceptance_boundary`
  and `acceptance_checks` explaining how both leading and alternate reading IDs
  satisfy that boundary. Merely listing options is not delegation.
- `BOTH_FAIR_FIGURE` (Eval 1 §2.1 local override, 2026-10-17) is the only PASS
  for a fork no source settles. It needs decision, writes and destinations
  `SAME` and stated word for word the same in both readings, contents
  `DIFFERENT`, no `authority_chain`, `delegation_basis: NOT_CLAIMED`, and a
  `figure` object: `kind` (AMOUNT, COUNT, RATE or DATE); `label` (one fork per
  label); `values`, exactly two, leading reading first, each `{reading_id, value,
  evidence, derivation}`, where `evidence` quotes a visible primary record other
  than the prompt, `derivation` is required when no quote contains the value,
  and each reading's `contents` contains its value; `checks` with
  `newer_source`, `authority`, `source_identity`, `scope` and
  `same_material_result`, each `{settles: false, reason}` (`settles: true`
  rejects the label); and `asks_completed` and `next_step_unchanged` reasons.
  The rendered section prints `Rubric must accept: X or Y`, and
  `hg_prompt_checks.py` returns the pairs as `both_fair_figures`.
- `option_inventory` has `complete: true`, `reason`, `evidence` citing the actual
  prompt, and `options`. Every explicit option has `id`, `option`, `source_id`,
  exact `quote`, `reading_ids`, `disposition` (RETAINED/EXCLUDED) and `reason`.
  Map even excluded options to tested readings. EXCLUDED must agree with each
  linked comparison. If no explicit list exists, use `options: []` and explain
  that conclusion with prompt evidence.
- `challenge_review` identifies `strongest_alternative_id`,
  `strongest_alternative_reason` and `evidence`. Each comparison also has
  `challenge` with `resolution_relevance`, `evidence`, `delegation_reason` and
  `delegation_basis` (`EXPLICIT_AUTHORITY` for AUTHORIZED_VARIATION;
  `NOT_CLAIMED` otherwise). Explain why the alternative is not a strawman, why
  each cited passage resolves this actual difference, and why any delegated
  choice is authorized rather than inferred from an option list.

This complete example shows the `unique_ground_truth` field for the synthetic
prompt **“Post the approved total, 10, to #finance.”** Source `P` is the verified,
visible anchor for that whole prompt in the enclosing record's `sources`.
Its two messages express the same required result:

```json
{
  "complete": true,
  "verdict": "PASS",
  "score": 5,
  "reason": "The amount and destination are fixed; wording changes preserve the required result.",
  "evidence_limits": [],
  "alternative_search_complete": true,
  "alternative_selection_reason": "The prompt fixes the amount and destination; the remaining plausible variation is the message wording.",
  "readings": [
    {
      "id": "A", "interpretation": "Post a short total message.",
      "support": [{"source_id": "P", "quote": "Post the approved total, 10, to #finance."}],
      "material_result": {"decision": "Report approved total 10", "writes": "Create a Slack message", "destinations": "#finance", "contents": "Total: 10"}
    },
    {
      "id": "B", "interpretation": "Label the total as approved in the message.",
      "support": [{"source_id": "P", "quote": "Post the approved total, 10, to #finance."}],
      "material_result": {"decision": "Report approved total 10", "writes": "Create a Slack message", "destinations": "#finance", "contents": "Approved total: 10"}
    }
  ],
  "comparisons": [{
    "alternative_id": "B", "resolution": "SAME_MATERIAL_RESULT",
    "reason": "Both messages communicate the required approved total to the required channel.",
    "evidence": [{"source_id": "P", "quote": "Post the approved total, 10, to #finance."}],
    "field_comparison": {
      "decision": {"relation": "SAME", "reason": "Both report approved total 10."},
      "writes": {"relation": "SAME", "reason": "Both create one Slack message."},
      "destinations": {"relation": "SAME", "reason": "Both target #finance."},
      "contents": {"relation": "SAME", "reason": "Both convey total 10; the prompt prescribes no literal message wording."}
    },
    "challenge": {
      "resolution_relevance": "The cited prompt fixes the value and channel while leaving message wording open.",
      "evidence": [{"source_id": "P", "quote": "Post the approved total, 10, to #finance."}],
      "delegation_basis": "NOT_CLAIMED", "delegation_reason": "No materially different final call is accepted."
    }
  }],
  "option_inventory": {
    "complete": true, "reason": "The full prompt contains no candidate option list.",
    "evidence": [{"source_id": "P", "quote": "Post the approved total, 10, to #finance."}],
    "options": []
  },
  "challenge_review": {
    "strongest_alternative_id": "B",
    "strongest_alternative_reason": "The specified value and destination exclude different totals or channels; the wording variation preserves both.",
    "evidence": [{"source_id": "P", "quote": "Post the approved total, 10, to #finance."}]
  }
}
```

For genuinely missing evidence, use this minimal partial object in the same
format-2 record. `UNVERIFIED` is an internal no-score state, not a fourth overall
verdict or a scored UGT band. Optional unfinished comparison fields are not
certified or rendered:

```json
{
  "complete": false,
  "verdict": "UNVERIFIED",
  "score": null,
  "reason": "The required decision source has not been read.",
  "evidence_limits": ["Read the prompt-incorporated approval record to determine which final call is authorized."]
}
```

The overall report follows the existing provisional rules: PARTIAL/BLOCKED and
no numeric NON-FAIL score when no failure is demonstrated; an independently
proven failure remains FAIL. Missing evidence alone never proves ambiguity.

Save and render from the installed package:

```sh
python3 Evals/tools/hg_prompt_checks.py start
python3 Evals/tools/hg_write_output.py prompt-checks --source <completed-record.json>
python3 Evals/tools/hg_prompt_checks.py render-ugt
python3 Evals/tools/hg_write_output.py prompt --source <completed-report.md>
```

`render-ugt` validates the saved
`Evals/task_inputs/reports/drafts/prompt_check_record.json` and prints its required
Markdown section to stdout. To validate and render another record, use
`python3 Evals/tools/hg_prompt_checks.py render-ugt <record-path>`. Include the
generated section verbatim exactly once, visibly outside code fences/comments.
Any separately written UGT verdict or score, including the scoring-table row,
must agree with the record. Retain the existing report binding hashes.

The gate checks source binding, comparison completeness and declared consistency.
It does **not** establish semantic truth: choosing the strongest alternative,
judging a citation's relevance and deciding whether a choice is authorized remain
the evaluator's substantive work. A receipt cannot replace that challenge.

## Rubric acceptance and calibration

Continue the existing prompt-to-outcome mapping, omission/wrong-result tests,
whole-rubric valid-alternative tests and row-level fact review. Include the
current `eval_release` in the score record. For explicit numerical acceptance
bands use `kind: RANGE`, an exact quote such as `6,100–6,200` or
`approximately 6,140 (band 6,100–6,200)`, and the existing source-bound calculation.
The helper compares the unrounded source value with the closed interval. It
does not invent a tolerance for bare "approximately" or round an outside value
into the band. Source-unit checks still apply. Unsupported forms stay unresolved.

Before flagging bundling, apply the evidenced QC exceptions. Before flagging
missing coverage, apply `rubric-sampling-v1`: directly cover core/distinct
outcomes and use justified sampling for comparable repetition. A valid boundary
comparison or a permitted record grouping is not a bundle merely because it has
several words or numbers. Never demand one criterion per cell as a blanket fix.

Calibrate against paired faulty/valid cases: wrong and correct value ranges;
invented and authorized recipients; restrictive and valid alternative wording;
independent-action bundles and permitted grouping; missing core outcomes and
eligible unsampled repetitive cells. Establish labels from sources and QC
exceptions, not from the prior audit verdict or whether a run passed.
