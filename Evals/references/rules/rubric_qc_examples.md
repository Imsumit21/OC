# Rubric review examples from QC

`prompt-rubric-qc-examples-v1` supplements the existing requirement ledger,
per-row checks and whole-set challenges. It changes no QC thresholds, severity
definitions, denominator, atomicity exceptions, sampling policy or weights.
`/rubric` remains evaluation-only: preserve supplied criteria and report findings.

The [rubric case file](rubric_qc_cases.json) preserves 88 exported flags on 63
cards / 61 tasks, including 18 rubric FAIL flags, with full prompts, criteria,
supporting fields and exact QC explanations. Its provenance is the user-supplied
QC audit HTML/CSV for project `69a74e16c6538223558b70f6`, cross-checked locally.
Neither the original universes nor historical verdicts were independently
re-audited. Read selected relevant cases, not the entire corpus routinely.
Do not use these examples or auditor assertions as current task facts.

## Challenge coverage at the required destination

Start from prompt-authorized requirements, including incorporated instructions.
For each core requirement or distinct action, identify the entity, property,
required output/audience, success state and substantive content. Apply the
existing sampling policy to comparable repetition. Then construct an omission
or wrong-result witness and check whether the whole supplied rubric accepts it.
Record the evidence in the existing checks ledger; no new input is required.

| Pattern | Historical lead | Review challenge |
|---|---|---|
| Required write absent | …9cb37 checks loan-note properties; …abc43 omits required invoice comments. | Could the Agent report the right facts without making the required record change? Check the actual predicate: “adds a note containing X” already enforces creation and does not need a redundant creation row. |
| Content graded only elsewhere | …5296f C8 grades board write-back while its justification grades correctness only in Diane's order; …3551f checks vault metadata while all content criteria target email. | Could the required board or stored memo be wrong/empty while the email is correct and every criterion passes? Correctness at one destination does not automatically establish correctness at another required destination. Use permitted shared-content grouping where it truly verifies both; do not duplicate the same obligation. |
| Substance replaced by formatting | …2ec99 checks organization by client/vendor without the required exposure; …beaed uses “close checklist status”; …2ec79 uses “correct figure.” | Identify the accepted substance or objective rule from allowed judge-visible context. Could a well-formatted but substantively wrong answer pass? A title need not repeat a value already unambiguously supplied by permitted prompt/sibling context. Private evidence and justification cannot supply missing acceptance conditions. |
| Scope and exceptions missing | …9cb35 grades only problematic loans despite an all-active-loans ask; …965fb9 accepts either of two qualifying obligations. | Derive the requested population before filtering. Protect core/distinct outcomes and consequential exceptions. Apply valid cohort controls and ordinary/edge samples to comparable repetitive items; do not demand one criterion per cell or per routine finding. |
| Delivery or end state weakened | …52977 permits a draft as notification; …2ec9e permits a note instead of a required status correction; …965fb6 grades a notice draft's existence without its cause/term end. | Does the predicate prove the authorized completion state and material content? Drafting can satisfy a draft request; it does not deliver a send request. A note is valid only if it satisfies the requested record state. Tool limitations do not silently weaken the prompt. |
| Unauthorized Agent duties | …10aed C14–18 turn “I'll post … and send Harry …” into Agent sends; …1fbba grades a different cost metric. | Trace each action, recipient, metric and exclusive format to prompt authority. OEs, business examples and CB justifications cannot add obligations. Preserve user-owned actions and valid create/update or delivery alternatives. |

## Challenge each predicate and the full set

- **Atomicity with the existing exceptions.** …3d7b8e combines a CRM risk note
  and calendar call; …2ec9b groups three independent ticket updates. Test partial
  success before flagging a bundle. A send with the content that defines it,
  one coherent record, a supported comparison or permitted shared email content
  is not automatically non-atomic. Do not transplant old recommendations to
  split every fact or write from its content.
- **Category follows the graded requirement.** …ae902 grades searching and
  comparing; …4f0d8's historical auditor calls several findings Process. Inspect
  what is actually graded: a reported finding or observable output property is
  Outcome even if retrieval was needed. A retrieval method is Process only
  when the task requires it and no Outcome can verify that requirement. Zero
  Process criteria can be correct. Do not import historical Process quotas.
- **Exact subject and framing.** Historical cases often use “The Agent's email
  …”, which can be agent-centric but nonstandard. Apply current phrasing rules
  to the exact title, distinguishing those from an artifact-only subject such
  as “The write-up …”. Use affirmative framing even when the prompt explicitly
  requires a prohibition (`hg-strict-overrides-v1`); a negative fact descriptor
  is not a prohibited action.
- **Entity, financial direction and lifecycle.** …09270 allegedly treats a
  vendor payable as tenant debt; …965fae mistakes a designed missing CRM deal
  for a tracking defect; …10afe names an approver as blocker after approval.
  Verify actual relationships, source scope, correction history, units and
  current versus proposed state. Presence of a person's name in a bill does
  not make that person the debtor. OEs are leads, not factual authority.
- **Whole-set contradictions and scope.** …1fbbd includes different creator
  identities, lead counts and renewal amounts. Compare the same entity,
  period, condition and output before declaring a contradiction. A historical
  quoted price and its corrected current price can coexist; a valid answer
  must not be forced to assert incompatible current values. Recompute numeric
  acceptance checks from primary sources; do not copy the old verdict/count.
- **Valid alternatives and near misses.** Test both a valid nonliteral solution
  and a plausible wrong one. Reject ungrounded exact titles, top-level-only
  posts, arbitrary new-record demands or exclusive recipient lists. Conversely,
  an “or” is too permissive if it allows omission of an independently required
  outcome. Identify the exact lost requirement and apply the current category.
- **Overlaps and weight.** Repeated facts are not independent successes merely
  because they appear in multiple rows. Separately required communications or
  substantive outputs still need coverage. Apply the existing shared-content,
  overlap counting, sampling and complexity-based weight rules; do not add
  grading volume or weight for incidental formatting.

## Historical labels are not current policy

The export contains inconsistent severity descriptions, scores and category
labels. Row 89 even lists five issues plus two more but calls the total six.
Recalculate from the current criterion set under
[qc_rubric_v10.md](qc_rubric_v10.md); keep the authored-row denominator and
highest-severity-once accounting. A low percentage does not change a Major
defect into a Minor defect. Do not use raw mention counts as missing-outcome
counts or double-count one obligation described several ways.

Row 14's old feedback explicitly predates spot-check guidance; current
[rubric_sampling.md](rubric_sampling.md) controls. Claims supported only by OEs
need prompt authority and primary facts. Missing written reasons remain
unexplained. Historical All-Failing flags are retained for provenance only:
this evaluator does not consume verifier results or revive those dimensions.

The helpers enforce record consistency, known source boundaries, explicit fact
comparisons and score calculation. They do not infer every obligation, choose
authoritative sources or automatically determine semantic coverage/atomicity.
Complete those reviews with concrete witnesses. The historical cases are review
examples, not independently established pass/fail regression labels.
