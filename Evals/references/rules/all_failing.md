# All-failing rubric diagnosis

Use only when actual run/verifier evidence is supplied. All-failing status is not a pre-run input requirement for rubric creation. The stage input contracts in `Evals/WORKFLOW.md` govern. Examples here explain diagnosis, not current universe facts.

## What “all-failing” means

An all-failing (AF) rubric failed **every completed run**. Exclude errored or
empty runs. If four of six runs completed, a rubric is AF only when it failed
all four. A rubric that passed at least one completed run is not AF.

Zero task-level passes can be a valid difficulty result. It does not make every
AF rubric valid. Each AF rubric still needs the platform's required 1–2 line
justification confirming that the repeated failure is a genuine Agent failure,
not a false negative caused by the criterion, judge, data, or environment.

Use current verified task/source facts under `Evals/WORKFLOW.md`'s evidence-reuse
contract where eligible. Still inspect the actual criterion, judged evidence
and run-state provenance for the suspected failure. Reuse never proves a model
miss or judge error merely because an earlier artifact passed.

## Diagnose before justifying

For output-related criteria, first apply `Evals/WORKFLOW.md`'s **Output capability
and failure attribution** contract. A confirmed missing creation/export/delivery
capability makes the criterion defective, not the Agent. Uncertain support is
unresolved. Preserve raw scores and assess independent model mistakes normally.

For each AF rubric:

1. Compare the criterion and its supporting fields with the prompt and authorized
   instructions under `Evals/WORKFLOW.md`'s **Task requirement authority** contract
   (`prompt-incorporation-v1`). Cite the incorporating prompt passage and verify
   applicability, Agent access and current version. An unmentioned handbook/policy
   rule makes the criterion invalid, not the Agent wrong. Recheck older maps before reuse.
2. Verify every expected fact in the live task state and base/injected ground
   truth.
3. Verify feasibility and observable precision against every relevant
   `Evals/references/tools/catalog.json` catalog, the assigned persona's applicable read scope,
   and the actual trajectory results.
4. Read each completed trajectory rather than relying on the verifier summary.
5. Classify the pattern:
   - **Legitimate Agent failure:** the criterion is valid and the completed runs
     genuinely missed it.
   - **Rubric invalid:** the criterion is ungrounded, beyond scope,
     non-atomic, over-specific, negatively phrased, or otherwise broken.
   - **Judge error:** the trajectory satisfies a valid criterion but the judge
     missed the evidence.
   - **Environment/tool-observability failure:** the required valid operation
     or precision systematically cannot be reached. This is an invalid AF, not
     model difficulty, and should be escalated.

For Gmail, Slack, GCal, and Drive-family (GDrive/GDocs/GSheets/GSlides) reads,
inspect supplied failure evidence and authorized read results for the exact
assigned roster persona; do not replay trajectory writes or launch new runs.
A record found only through Explorer, local export, or
another persona does not establish Runner reachability. Required scoped-service
evidence inaccessible to the assigned persona makes the task/rubric invalid
unless the authorized outcome is an affirmative denial finding plus reporting,
escalation, or an authorized alternative. Use the existing ACL matrix for
explicitly unscoped services and `service-availability-v1` in
`Evals/ENVIRONMENT.md` for Snowflake and Confluence. Both are live; their older
ACL omission alone is neither evidence of an impossible criterion nor a review
blocker. Concrete task-specific denial evidence still matters. Writes are
outside ACL scope.

The number of failures is only a prioritization signal. Repetition never proves
that the Agent is wrong.

## Outcome rubric checks

Outcome rubrics are the default. When one fails every run, check:

- **Grounding:** every ID, name, status, amount, date, count, destination, and
  expected conclusion exists and is tool-observable.
- **Prompt scope:** the criterion grades an authorized requirement, not an
  incidental OE-answer or universe fact.
- **Atomicity:** one criterion checks one independently pass/fail condition.
- **Destination:** grade the artifact or action the prompt requested.
- **Precision:** use exact values for IDs, dates, counts, and discrete structured
  fields. Use “approximately” only for genuinely calculated or rounded values.
- **Generated wording:** allow equivalent free text with an objective rule or
  “(or similar)” where appropriate; do not loosen exact source values.
- **Affirmative, Agent-centric phrasing:** state what the Agent accomplishes,
  classifies, preserves, or leaves unchanged. Do not define success only as
  inactivity.
- **Scoped verifier evidence:** the verifier can grade from the trajectory,
  final response, visible write arguments, or evidence visible to that same
  persona, not hidden cross-persona state.


### Affirmative exclusion example

Invalid prohibition-only criterion:

> The Agent does not mark the release approved.

Affirmative criterion:

> The Agent leaves the release-approval state unchanged.

Exclusions still require coverage; express the accepted scope or preserved
state positively. A negative factual finding remains valid when reported as an
affirmative behavior: “The Agent reports that human approval remains
unconfirmed.”

The same rule applies to ACL outcomes. “The Agent does not access another
mailbox” is prohibition-only and invalid. A task intentionally testing access
denial should grade the Agent's affirmative report, escalation, or authorized
alternative while preserving the factual denial.

## Process rubric checks

Process rubrics are optional and rare. Apply the current three-condition test to
every Process criterion. It is valid only when all three are true:

1. **Required by every valid solution path**, or phrased broadly enough to
   accept all valid paths.
2. **A stricter Outcome cannot capture the requirement.**
3. **It describes a behavioral verification property, not an execution trace.**

If any condition fails, delete the Process rubric, relabel a write action as an
Outcome, or tighten the relevant Outcome. Never make an invalid Process rubric
“flexible” by listing alternative tools, query strings, or call sequences.

Automatic `set_acting_user` application is environment configuration. It is
never a Process criterion, Agent action, or complexity/call-count
item.

Only identify a **missing** Process rubric when the prompt or a validly
incorporated source creates a sequential or causal dependency that Outcomes
cannot verify. A genuinely missing dependency check is Non-Fail under current
QC; do not invent Process coverage when no dependency exists.

### Invalid Process example: Outcome can prove it

Process criterion:

> The Agent checks the ENG-2230 record directly before posting the Season Pass
> update.

If the prompt only asks for a status update, an Outcome can require the exact
grounded result—ENG-2230, “Season Pass Vfx Animations Implementation,” is Done.
The Process criterion unnecessarily fixes a path and adds no distinct signal.
Delete it and tighten the update's Outcome content criterion.

### Valid Process example: required ordering

Suppose the prompt explicitly requires the Agent to brief the team in
`#season-pass` before changing ENG-2230. Separate Outcomes can prove that both
actions happened, but neither can prove their order. This affirmative
behavioral criterion may be valid:

> The Agent posts the ENG-2230 briefing in `#season-pass` before updating
> ENG-2230.

It still must be grounded, required by every valid path, self-contained, and
verified against the trajectory.

## Writing the AF justification

A useful 1–2 line justification states:

- what exact requirement the completed runs missed; and
- why the criterion remains grounded, achievable, in scope, atomic,
  affirmative, and fair to every valid path.

Do not justify an AF rubric by saying only that “all runs failed.” If the
investigation reveals a rubric, judge, or environment defect, record that defect instead of defending the criterion.
