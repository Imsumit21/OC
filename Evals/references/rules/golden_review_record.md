# Historical golden audit evidence record

This schema is retained for historical reports/helper compatibility only. The
active solution-path stage is `/oe` under [oracle_events.md](oracle_events.md).
Do not apply these legacy binary scores or final-answer rules to OEs.

`/golden` audits the supplied answer. These helpers record and check the audit;
they never generate or rewrite an answer. Use this contract after intake. It
replaces duplicated prose ledgers, not source verification or human judgment.

## Workflow

1. Save supplied inputs using INPUTS.md, then read the exact prompt, golden,
   assignment, applicable references and optional SQL decision. Resolve intended
   outcomes from their authority and source facts before accepting the golden's
   assertions. Read the whole golden, including tables and alternative notes.
2. Run `python3 Evals/tools/hg_golden_review.py start`. It snapshots the current
   input/rule context and hashes the saved golden without changing it. If using
   an explicit saved `golden`/`source:golden` mapping, use `--answer "<saved path>"`.
   Its receipt supplies the five binding fields below.
3. Complete the structured record below. For every required outcome, establish
   the expected answer, compare its actual resolution, verify evidence, and test
   a valid answer and a plausible wrong answer. Never remove an uncovered
   requirement to make the record pass. Inspect all advertised alternatives and
   all factual supporting claims; include them in the claim ledger.
4. Save it using `python3 Evals/tools/hg_write_output.py golden-review --source "<record.json>"`.
   The fixed path is `Evals/task_inputs/reports/drafts/golden_review_record.json`.
5. Summarize findings in the report and include `Review record SHA-256` from that
   save's receipt. Save the report with `hg_write_output.py golden`. PASS requires
   a current, complete record with all checks cleared. FAIL/NON-FAIL reports can
   be saved before a complete record exists; omit unavailable hashes rather than
   fabricating them. Do all remaining useful verification even after finding a defect.

Starting another review archives the old context, record and report under
`reports/drafts/golden_history/`. Editing a saved record archives its prior record
and report; the revised report needs the new hash. Source/input/rule changes
invalidate approval. Report path remains `Evals/task_inputs/reports/2_golden.md`.

The separate, pre-existing explicit authoring mode may review its already written
`reports/drafts/08_Golden_Answer.md` with `start --draft`. This reads that file; it
does not create one, promote it to the canonical input or enable authoring on
ordinary `/golden` invocations. Reports label this mode DRAFT rather than AUDIT.

## Record format

Top level: integer `format_version: 3` (`golden-audit-v4`; format 2 records cannot authorize a new PASS); the exact `review_policy`, `review_mode`,
`review_iteration`, `reviewed_golden_sha256`, `review_context_sha256` from the
start receipt; arrays `sources`, `claims`, `requirements`, `repairs`; and objects `checks`, `chronology`, `alternative_review`.

Each source records:

```json
{
  "id": "S1",
  "path": "Workspace-relative source file or an explicit absolute path",
  "sha256": "SHA-256 of the exact source file",
  "location": "Record ID / JSON pointer / page or line",
  "observed": "Observed values and interpretation",
  "quote": "Exact source excerpt",
  "visibility": "VISIBLE",
  "access": "Why this source is observable to the assigned persona; limits if any"
}
```

The helper rechecks unique source files by hash and verifies each exact quote. For JSON, add `pointer` to select the actual record using an RFC 6901 pointer; the quote must occur inside that record, not elsewhere in the export. Prefer relative paths within
the bundle; absolute paths support isolated review workspaces. Reuse source IDs
across claims instead of duplicating reads. SQL is evidence of the proposed
overlay, not proof of runtime execution. A source excerpt saved separately must
retain its original path/record provenance in `location`/`observed`; extraction
must not silently filter contradictory records. A generated summary alone is
not primary evidence. Describe inaccessible evidence in the relevant unresolved
finding rather than inventing a source file/hash.

Each claim records:

```json
{
  "id": "C1",
  "statement": "Exact factual claim, derivation, requirement or advertised alternative",
  "golden_location": "Passage/table row or attached deliverable location",
  "golden_quote": "Exact passage in the saved golden being evaluated",
  "source_ids": ["S1"],
  "supporting_source_ids": ["S1"],
  "result": "VERIFIED",
  "reason": "Comparison with the actual source; calculation or contradiction where relevant"
}
```

Results: VERIFIED, INCORRECT, UNRESOLVED. VERIFIED and INCORRECT require evidence.
UNRESOLVED may have no source IDs and must identify the precise missing evidence.
An incidental claim can be separate from an outcome requirement; do not invent
a required output merely to link it. An INCORRECT claim still prevents PASS. Every INCORRECT claim, FAIL requirement,
FAIL check, FAIL chronology comparison and FAIL alternative branch also carries
`defect_class` (`wrong_value`, `added_restriction`, `missing_outcome`,
`loose_acceptance`, `contradiction`, `infeasible_path`, `upstream_artifact`) and
`repair_owner` (`contributor`, `platform`, `prompt`); the receipt tallies them.

Each authorized requirement records:

```json
{
  "id": "Q1",
  "authority": "Prompt passage and incorporated instruction chain",
  "authority_chain": ["P1"],
  "scope": "Entity/property, cohort, condition/time and required audience/output",
  "expected_result": "Source-derived value/decision/action or objective accepted branch",
  "golden_resolution": "Where and how the supplied golden resolves it, or explicitly MISSING",
  "source_ids": ["S1"],
  "claim_ids": ["C1"],
  "result": "PASS",
  "reason": "Actual comparison, practical defect or precise evidence gap",
  "verification": {
    "kind": "direct",
    "complete": true,
    "details": "What was checked; NEW or eligible REUSED with matching dependencies"
  },
  "valid_case": {
    "example": "Concrete task-valid solution or legitimate alternative",
    "result": "ACCEPT",
    "reason": "Why the whole golden permits it without invented restrictions"
  },
  "wrong_case": {
    "example": "Plausible wrong value, decision, scope, recipient or omitted action",
    "result": "REJECT",
    "reason": "The actual golden passage that rejects this case"
  }
}
```

Requirement results: PASS, FAIL, UNRESOLVED. PASS needs supporting verified
claims, source evidence and completed verification. A missing outcome may have
no corresponding claims: mark FAIL/MISSING and cite the authorized requirement.
Missing *reviewer* evidence stays UNRESOLVED; do not label it a missing answer.
Case results are ACCEPT, REJECT or UNRESOLVED and describe actual judged behavior,
not desired labels. A rejected valid case or accepted wrong case prevents PASS.

`verification.kind` is direct, calculation, absence, cohort or decision. Choose
the decisive verification type and include other relevant details in the text:

- **Calculation:** show source operands, units, formula, precision, time and result.
- **Absence:** record queried corpus/version, filters, pagination/completion and
  candidate exclusions. “No result yet” or a pending async job cannot establish
  “no matching open issue.” Finish available checks; `complete: false` blocks PASS.
- **Cohort:** verify the complete required member set, exclusions and aggregates.
  Golden review does not use the rubric's sampling exception.
- **Decision:** verify the applicable rule and each necessary premise. A status
  alone is not evidence of affectedness or a fulfilled conditional rule.
- **Direct:** exact values, destinations or other directly observable outcomes.

For absence and cohort claims, include source entries that bind the complete
queried corpus (or its authoritative version manifest), not just a few matching
excerpts. A changed corpus can add a candidate even when old excerpts are unchanged.

Test meaningful wrong content, not just complete omission. Test the precise
scope and required output: correct artifact delivery does not imply a second
obligation to repeat every fact in the final reply. Preserve source-supported
uncertainty and legitimate open-ended alternatives. Do not apply rubric
atomicity or isolated-title checks to the golden's prose.

`checks` contains exactly six keys: `completeness`, `accuracy`, `authority`,
`valid_solutions`, `wrong_solutions`, `consistency_feasibility`. Each has `result`
(PASS/FAIL/UNRESOLVED) and a concrete `reason`. Explain vacuous PASS where a check
has no applicable route/action; a justified N/A in the report is recorded as
PASS with that explanation. Do not invent requirements to exercise it.

**Ledger completeness.** The helper extracts every currency amount, percentage,
ISO date, ticket id (`ENG-2438`) and PR number (`#540`) from the saved golden.
Each must occur in some claim's `golden_quote` or `statement`; otherwise the
receipt lists it under `unledgered_values` as an open item and PASS is withheld.

**Intake receipt.** `start` records `golden_length`, `golden_answer_length` (the
`## golden_answer` section body when the export is composite), `integrity_override`
(the `--accept-ending` reason, or null) and `prompt_overlap` (distinctive tokens
and entities of the prompt and dynamic context that recur in the answer, with
examples). It refuses to bind a golden whose answer body is exactly 5,000 or 50,000
characters (the platform caps before and after 2026-09-22) or ends mid-sentence without an override; those are BLOCKED platform
findings, not audit findings.

**`artifact_match` (required object).** `{ "result": "MATCH" | "MISMATCH",
"reason": "what the prompt asks for and what the answer resolves" }`. Use the
receipt's `prompt_overlap` as evidence, not as the decision. MISMATCH forces
`verdict: NON-FAIL`, `execution_status: BLOCKED`, records `upstream_artifact` /
`platform` in the tallies, and makes PASS impossible; optional `defect_class`
and `repair_owner` may override those defaults with a reason.

## Limits

The helper verifies record completeness, references, declared results and source
versions. It cannot infer every real requirement from natural language, prove
source interpretation, or detect a falsely declared test result. These are
evaluator responsibilities. `review_open_items` are unresolved/failed checks,
not a new score or defect-count formula. No publication loop, numeric scoring
change, rubric input, routine model run or write to task services is added.

## Exact text, access, chronology and corrections (format 2)

`golden_quote` must appear in the saved answer at the receipt's hash. For a JSON
answer use `golden_pointer` to select the decoded field. A missing required answer
belongs in the requirement ledger as MISSING, not an invented claim quotation.
Every VERIFIED claim needs nonempty `supporting_source_ids`, a subset of its
`source_ids`, all with `visibility: VISIBLE`. Sources considered and rejected can
remain in `source_ids`; never present inaccessible evidence as solver support.
Visibility is VISIBLE/INACCESSIBLE/UNRESOLVED and needs concrete persona/ACL
reasoning in `access`. Raw-export access is not assigned-persona access. Do not
quote an accessible $6,250 notice as support for a separate private $8,250 total.
Exact-quote validation does not itself prove logical implication or access.

Every requirement has `authority_chain`, a list of source IDs beginning with the
actual saved prompt. Each later instruction source needs `incorporated_by` (the
preceding ID) and `incorporation_reason`. Preserve prompt-incorporation-v1. Do not
promote the golden, an official handbook or injected policy into independent
instruction authority. Research facts and authorized business conditions remain
evidence of the requested answer.

`chronology` contains `complete` (Boolean), `reason`, and `comparisons` (an array).
Each comparison has `source_ids`, `claim_ids`, `result` (PASS/FAIL/UNRESOLVED) and
`reason`. Cover conflicting revisions and claimed supersession: effective scope,
dates, accessible latest evidence, and why each old value is retained or replaced.
A newer source supersedes only what it actually changes. Record an empty array
with a reason when no comparison applies. Complete all required calculation,
absence and cohort checks in the existing requirement verification fields;
record operands, units, formula, result and the full required member set. Do not
accept a correct total as proof every constituent or source claim is correct.

`alternative_review` contains Boolean `complete`, `reason` and `branches`.
Each branch has `golden_quote` (optional `golden_pointer`), `authority_chain`,
`example`, `result` (PASS/FAIL/UNRESOLVED) and `reason`. Compare advertised branches
to the main answer and to prompt/source authority. If the main example uses new
cards but alternatives permit editing existing ones, the main answer must not
claim that new cards are mandatory. An example layout is not automatically a
restriction; examine actual modal wording and explicitly accepted variation.
Explain an empty branch list after reading the entire answer and alternative
notes. Both incomplete inventories prevent PASS.

`repairs` is an array, empty for a first audit with no claimed fixes. If claiming
an earlier defect was fixed, each entry needs `old_quote`, `golden_quote` (the
replacement actually saved), `claim_ids` and `reason`. The replacement must exist
in the current reviewed file, and affected claims must verify. The old wording
may appear only in a clearly distinguished historical context, not as the still
operative answer. Do not trust a prior PASS report's statement that it edited the
answer. AUDIT still proposes corrections without editing the user's answer;
if a proposed correction is not saved, keep the defect open instead of adding a
successful repair. Rehash/restart after an authorized revision.

The helper derives verdict/status from the recorded checks: proven defects stay
FAIL; only unresolved evidence gives provisional NON-FAIL; all clear gives PASS
(5). A report bound to a record must agree with that record. This enforces internal
consistency, not the truth or completeness of reviewer judgments. Existing v1/v2
reports remain readable but cannot authorize a new PASS.

For plain text or SQL containing multiple records, add inclusive one-based
`line_start` and `line_end` to constrain the quote to the cited record/statement.
The helper checks the full source hash plus the selected lines. Do not combine
line bounds with a JSON pointer. Retain enough surrounding context to evaluate
contradictions; an exact excerpt is not evidence that omitted context is irrelevant.
