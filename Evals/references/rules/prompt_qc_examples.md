# Prompt review examples from QC

`prompt-rubric-qc-examples-v1` supplements the existing prompt phases and premise
record. It adds no scoring dimension or automatic failure rule. Use the checks
below during the applicable existing phases; record concrete evidence and impact
there instead of producing another checklist or report.

The [prompt case file](prompt_qc_cases.json) contains 29 exported flags on 25
cards / 24 tasks, including 10 prompt FAIL flags. It preserves full prompts and
exact explanations from the user-supplied QC audit HTML/CSV for project
`69a74e16c6538223558b70f6`. The exports were cross-checked locally; the database
and historical universes were not independently audited. Reported categories
are not established ground-truth labels. Some disagree with exported scores.
Two FAILs have no explanation: …9cb3d (Multiple Valid Answers, CSV row 93) and
…965faf (Feasibility, row 98). Do not invent a diagnosis for either.

The same file also carries `calibration_cases`: 15 cases (9 FAIL, 6 PASS) from
9 tasks in Kelvin's 50-task review, for the rules agreed on 2026-10-17. Each task
case binds its exact prompt by `prompt_sha256`; each control is a short text that
must raise no flag. See [Calibration from the 50-task review](#calibration-from-the-50-task-review-2026-10-17).

Read relevant cases only when useful. The prompt case file intentionally omits
rubrics, OEs and run results. Do not load those later artifacts to interpret or
grade the current prompt. Historical feedback is a source lead, never evidence
that a present-day entity, constraint, capability or obligation exists.

## Challenge material ambiguity

For a suspected ambiguity, write two reasonable readings, the resulting
actions/deliverables and the material difference. Test both against the exact
prompt and its authorized source context. If the context resolves the choice,
or the user validly delegates it, do not manufacture an ambiguity failure.
Use the existing Unique Ground Truth and Action Decision Ambiguity rules.

| Pattern | Historical lead | Check and valid control |
|---|---|---|
| Selection changes recipients or work | …54441 asks for agents who “mattered most”; different volume/revenue/referral interpretations select different people. | Establish a supported selection rule, tie handling or explicit discretion when it affects outreach or other material outcomes. Multiple defensible analytical recommendations can be valid. Do not invent an arbitrary top-three requirement. |
| Destination ambiguity | …09270 says “put something on the board”; feedback names Airtable Property Operations and Linear Property Ops. | Resolve the intended record/system through the prompt and source context. If different supported readings change required writes, show that consequence. A natural business name is sufficient when unambiguous; literal tool names are not required. |
| Approval and action ownership | …52957 says “stage for approval” then update tracking; …10aed says “I'll post … and send Harry …”. | Identify who acts and when. Distinguish staging from approval, informing from waiting for permission, and internal edits from external sends. The user's promised action is not an Agent obligation. Do not infer an approval gate merely from “once I know” when the surrounding request resolves it. |
| Identity and joins | …9cb35 allegedly maps the same loan IDs to different borrowers across records. | Verify entity identity across sources and the authoritative reconciliation. A last name or hardcoded ID need not appear in the prompt if discovery resolves the person. A null creator field does not prove someone else created the object. |
| Conflicting financial interpretations | …965fa0 has two $8,400 records with duplicate-versus-separate interpretations. | Inspect source type, payer/payee, identity, status, period and corrections. Agreement among copies is not independent corroboration. A task asking the Agent to identify an unresolved conflict can still be solvable; it need not force an unsupported total. |
| Scheduling and coverage | …3d7b8e lacks a promised call time; …52966 leaves unclear whether cover applies to a showing or an owner call. | Check the actual commitment, availability, timezone, deadline and covered event. Multiple feasible slots are not inherently a failure when scheduling is delegated. A missing exact timestamp alone is insufficient. |

## Verify premises and feasibility separately

- **Existing fact versus hypothesis.** …2ec9b allegedly invents a prior email
  and reopen order. Verify the asserted event with the existing premise ledger
  and scoped absence checks. “I think this is resolved; check it” permits a
  correction; a requested new record need not already exist. A failed lookup or
  missing reviewer access is not proof of a nonexistent source.
- **Operational effect, not just a tool name.** Verify that the available path
  can complete each required action for this persona, including target entity,
  data fields and numeric observability. A draft-only operation does not send
  an email. An authorized delivery alternative may solve the task; an unknown
  capability remains unresolved. The unexplained historical feasibility flag
  cannot establish any particular tool limitation.
- **Background imprecision versus material error.** …10af3's “went back and
  forth” and …10aea's incidental names illustrate narrative claims whose impact
  must be assessed separately from required writes. Apply the current factual
  bands, not a blanket FAIL for every inaccurate background phrase.
- **Role fit versus hard access.** …10ad5 concerns bookkeeper/HR work;
  …abc43 concerns contributor/manager coordination. Check actual assignment and
  persona evidence. A better-fitting colleague does not itself prove the
  assigned persona cannot act. Separate realism, business-function fit and
  confirmed access blockers under their current dimensions.

## Calibration from the 50-task review (2026-10-17)

These are judgment calls with no word list and no count. Use the cases to
calibrate, then judge the actual wording under the Eval 1 phase named.

| Rule (Eval 1) | Fails | Passes |
|---|---|---|
| Staged errors (§1.2, Typing override) | #11: "breakdiwn", "wirk", "calndars", "telll", 11 misspellings in about 120 words | The same #11 prompt spelled correctly |
| Trap hint or riddle (§2.7, Riddles override) | #31: "the thing that actually bites us is not on anybody's list" | "CPI jumped last week and I don't know which test did it" |
| Hidden destination (§1.5 Ambiguity, §2.7) | #42 "wherever that's actually been asked for"; #47 "the same place the rest of these wind down calls have been going"; #44 "answer him there too" | "post the summary in #winddown" |
| Audit form or if-chain (§2.7) | #1 and #43 "…complete the … handoff it requires"; #44 "If he asked me somewhere else, not the rules or his posts about them, …" | "Arthur wants the merge-review stuff sorted before the next push, can you check what's still open and close it out?" |
| Shutdown or departed-person premise (§2.3) | #43: Victor, who left in April 2025, holds a "current" control | None given |
| Both-fair figure (§2.1, UGT override) | The BOTH_FAIR_FIGURE label on #49: $8.5K (2026-01-22) vs $8K (2026-01-23) is settled by the newer source as today, and a file-now versus defer fork is never a figure | #50: 32.8% or 28.5%, recorded as BOTH_FAIR_FIGURE; the rubric must accept either |

## Avoid importing old policy

Historical judgments are not new rules. For example, row 103 flags product
names; apply the current tool-mention rule to the actual wording instead of
banning every business-system name. Rows 104–115 illustrate disputed channel,
timing and workflow assumptions: use the current material-divergence exceptions,
not the historical label. A business-function description's “typical actions”
does not mandate every listed write unless the prompt incorporates that duty.

The source helper checks declared evidence bindings and recorded comparisons.
It does not discover every implied premise, establish complete search scope or
decide whether two readings materially differ. These examples guide that review;
they are not independently replayed historical tests.
