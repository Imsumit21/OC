# Long and Super Long Horizon evaluation rules

Read when the assignment is Long Horizon or Super Long Horizon, involves sustained work over a large source-defined cohort, or uses the large audit-table exception. The numbered Evals and shared environment/input contracts govern. Examples below are static explanations, not required external artifacts, current task evidence, or additional user inputs. Tool and access claims require the bundled catalog and available run evidence, if a check requires observed behavior.

### How 116 Records Are Graded Without 116 Rubrics

The source guide describes a 116-row register graded with 79 criteria; the examples below are sufficient to explain the rule without that task file. It reaches complete coverage through five devices rather than row-by-row expansion:

- **Exact cohort multisets.** "The Agent records the Combo-Fighters PR-number multiset as every integer from 1 through 37 exactly once" rejects missing, duplicate, and extra keys in one independently verifiable claim.
- **Whole-cohort verification.** The OE/source audit verifies every first SHA; that verification is not a single scored criterion claiming all 116 independently variable SHA values are atomic. Use grounded one-record spot checks for rubric coverage of repetitive cells under the exception.
- **Aggregate invariants.** Each of the five provenance flags gets an exact row count — 30, 105, 78, 21, and 22. Matching counts alone cannot prove every row correct because misclassifications can cancel out; combine them with cohort controls and grounded spot checks.
- **Atomic spot checks.** One row is pinned by name: dominoes PR #79 must read exactly `MULTI_COMMIT_WITHOUT_APPROVAL`. There is no required number of these.
- **Exclusions.** Leonard limited totals to per-repository and combined, so two criteria confirm the memo carries no state-level or contributor-level breakdown.

Every non-repetitive requirement — tab name, cutoff, memo links, source anchors, handoff facts — still gets its own direct rubric. The exception compresses repetition, not coverage.

### Explicit Spot-Check Rule for Large Redundant Audits

For rubric evaluation, apply [rubric-sampling-v1](rubric_sampling.md): cover
core/distinct requirements directly and sample only repetitive items of comparable
importance. Record scope, ordinary/edge selection and limits. This is artifact
sampling; every supplied rubric criterion still receives a full review. There
is no automatic row-count trigger or criterion cap, and a normal-horizon label
does not exclude an otherwise eligible repetitive artifact.

Do **not** create one rubric for every repeated row, record, or field. For
example, a 166-PR audit does not need 166 rubrics for each audited field.
Instead, combine:

- an exact cohort or artifact-row-total criterion;
- exact reconciliation controls such as key multisets
  and aggregate invariants; and
- source-grounded atomic spot checks for selected PRs.

There is **no required minimum number of spot checks**, either overall or per
group/component. Choose enough grounded checks to make the task objectively
reviewable without recreating the full audit as hundreds of rubrics. The
Oracle Events and intended execution must still cover the complete cohort, and every
non-repetitive requirement still needs direct rubric coverage.

Do not replace this policy with an “at least N records are correct” rubric.
`At least N` usually packs independent pass/fail items into one threshold and
is non-atomic. Large-audit sampling applies only to repetitive cohort cells.
The separate coherent_record exception in `coherent_record.md` allows tightly
coupled attributes of one record; it does not authorize sampling or grouping
separate records/actions. Ordinary tasks
follow `Evals/3_Rubrics_Eval.md` Split Completely: independent facts in one
Slack/email/ticket still need separate criteria, and the same fact on two
prompt-specified artifacts still needs two criteria. Do not import this
paragraph into a normal-horizon task as a license to AND every close-out fact
into one mega-row.

## What Qualifies as Long-Horizon

Apply [WORKFLOW's horizon tiers](../../WORKFLOW.md#required-prompt-assignment):
**Normal Horizon: 50–100 tool calls; Long Horizon: 100–500+** (2026-09-26 update;
Super-Long-Horizon is paused). Counts are measured at Trajectory - Task Type &
Horizon, not at `/prompt`. `/prompt` assesses the design; it does not require a
completed trajectory or estimate a call count. Keep estimated necessary work separate
from observed run length.

For either tier, the work should arise from necessary, dependent retrievals,
reconciliations, or writes. Common patterns include:

- Auditing every member of a large, source-defined cohort.
- Checking several distinct evidence surfaces for every record.
- Reconciling records across services when no authoritative bulk view contains the answer.
- Producing a large register whose totals and classifications depend on record-level evidence.
- Completing a broad closeout or handoff where omissions would make the deliverable unreliable.

The assigned horizon selects the applicable scale target; call volume alone
does not establish task quality or difficulty. Do not apply Super Long Horizon's
500-call starting point to Long Horizon. Repeatedly opening the same record,
splitting one useful query into many smaller queries, or adding arbitrary
checkpoints solely to increase the count is artificial inflation.

ACL-denied reads, repeated retries against inaccessible records, and automatic
`set_acting_user` environment configuration do not count toward the threshold.
The high call count must come from reachable, necessary Agent work.

### Practical Design Pattern: Record × Evidence-Surface Matrix

The most reliable way to design legitimate long-horizon work is to identify a large, source-defined cohort and require several distinct, necessary evidence surfaces to be checked for every cohort member:

`number of records × separate evidence surfaces per record = core record-level calls`

For example, 116 pull requests requiring five individually exposed GitHub evidence checks produce 580 core calls. This illustrates **Super Long Horizon**, not a minimum for Long Horizon. The governing constraint is that a cohort listing or summary cannot substitute for record-level verification when it does not contain the requested evidence.

The same pattern can apply to incident closeouts, vendor wind-downs, access handoffs, release audits, customer escalations, or contract reconciliations. In each case, every surface must be separately exposed by the available tools and must materially affect the requested deliverable. If one bulk call contains the complete evidence, require the bulk call instead.

> **DO NOT COPY THESE EXAMPLES EXACTLY. Do not reuse their wording, numbers, cohorts, evidence-surface combinations, or deliverable structure. They are reference patterns only. Every task must be original and grounded in its assigned environment.**

## Keep the Prompt Natural

Long-horizon tasks fail quality checks when the prompt reads like a spec sheet. The agent should receive a realistic work request; detailed operating rules, field definitions, checkpoint mechanics, and classification vocabulary may live in environment sources the prompt clearly incorporates.

**Unnatural prompts** over-specify:

- Exact channel names, file paths, and internal artifact titles.
- Column-by-column spreadsheet schemas.
- Process choreography (“save 20 rows at a time,” “six checkpoint slots,” “re-open each range before the next block”).
- Full policy text that employees would already have recorded elsewhere.
- Verification scripts embedded in the user message.

**Natural prompts** state:

- The business situation and urgency.
- What outcome is needed and by when.
- Which source anchors to follow (“the wind-down decision,” “the task list on my Drive”).
- The deliverables in plain language (spreadsheet + memo).
- Enough constraints to grade the result, without walking the agent through every step.

The natural version should still produce the same long-horizon work. The complexity comes from the data and the deliverable, not from the prompt acting as an operations manual.


### Generalizing the Pattern

The same compression applies to any long-horizon scenario. Once the conventions live in the environment, a prompt can shrink to something like:

> Can you prep the handoff spreadsheet John asked for? Follow Jane's recommendations from the meeting notes, include a blurb I can send via Slack, and drop a summary `.md` file when you're done.

That still requires hundreds of tool calls, because the agent must find John's request, read Jane's recommendations, discover the vocabulary and deliverable shape from those sources, and then execute the full cohort audit. The call count comes from investigation and record-level work, not from repeating instructions in the prompt.

## Environment Injection

**Most of the detail in an unnatural long-horizon prompt should live in the environment, not in the user message.**

“Injection” means adding a small amount of **synthetic task context** to that task’s **unique environment**. It does **not** mean prompt injection or adversarial instruction hijacking.

### Why Inject Instead of Over-Specifying the Prompt?

Long prompts become unnatural when they contain every policy, flag definition, column schema, and process constraint. In a real company, those details already exist somewhere:

- A Slack thread where the team agreed on preservation flags.
- Meeting notes with Jane’s register recommendations.
- A Drive checklist or policy doc for wind-down closeouts.
- A Linear comment or GDoc defining evidence standards.

Put them in a source the prompt clearly directs the agent to follow. Under
`Evals/WORKFLOW.md`'s `prompt-incorporation-v1` contract, a short delegation can
incorporate detailed instructions without restating them. Merely placing a rule
in an injected handbook, policy or related record does not make it gradeable.
Finding facts during research does not automatically incorporate source instructions.

### What to Inject vs What to Keep in the Prompt

| Belongs in the environment | Can stay in the prompt |
|----------------------------|------------------------|
| Flag definitions and approval rules | Business situation and deadline |
| Column schemas and naming conventions | Repositories or cohort scope |
| “Follow Jane’s recommendations” source content | Deliverable types (spreadsheet, memo) |
| Prior requests (“John asked for this last night”) | High-level evidence areas to preserve |
| Team conventions (`NONE FOUND`, completion rules) | Source anchors in plain language |
| Register formatting standards | Request to verify row count at handoff |

**Example:** Instead of pasting this into the prompt:

> Use these preservation-gap flags so the roll-up stays consistent: NO_SUBMITTED_REVIEW, NO_INLINE_REVIEW_DISCUSSION, NO_GENERAL_CONVERSATION, NO_REVIEW_REQUEST_EVENT, and MULTI_COMMIT_WITHOUT_APPROVAL. Use NONE when no flag applies. Apply MULTI_COMMIT_WITHOUT_APPROVAL when a pull request has more than one commit and no submitted review anywhere in its record has state APPROVED; later commits do not cancel that approval. Treat the flags as record gaps, not judgments about the code or people involved.

**Inject** a realistic Slack exchange—for example, Arthur or Jane posting the team’s standard flag list and rules in `#engineering-bots` or a wind-down thread. The prompt then says:

> Use our standard flags for record gaps—check the thread where we defined them.

The agent must read Slack to learn the vocabulary. That adds tool calls **and** keeps the prompt natural.

### Injection Rules

- **Task-isolated:** Each task has its own environment copy. Synthetic additions affect only that task, not other contributors’ universes or the shared base export.
- **Small and plausible:** Keep synthetic records realistic and proportionate as authoring guidance. Eval 0 checks static data integrity; this guidance does not add a style or size gate to `/injection`.
- **Discoverable, not prescriptive:** Seed policies, requests, and constraints—not the final register contents or pre-computed totals.
- **Cross-service consistent:** If Slack references `Task List.xlsx` or a specific PR, that record must exist (or be intentionally seeded) in Drive/GitHub.
- **Persona-reachable:** Required Gmail, Slack, GCal, or Drive-family (GDrive/GDocs/GSheets/GSlides) records must
  be visible to the exact assigned persona unless the intended outcome is an
  affirmative denial finding plus reporting, escalation, or an authorized
  alternative. Universe Explorer author god-mode and local exports prove global
  existence only.
- **Documented in ground truth:** Record every injected row in
  `01_Universe_Inject.sql` and the recorded source provenance. Include injected facts in
  the Oracle Events and rubrics only when they are needed for the authorized
  solution path or acceptance criteria.
- **No adversarial hidden instructions:** Injection supports realistic work discovery; it must not trick the model.

A compliant injection for this example is small — one private channel, one thread, fourteen messages, each recorded as an individual row in the task's own `01_Universe_Inject.sql` and the recorded source provenance. Nothing in that injection contains a register row, a flag total, or a cohort size; it seeds only the rules the agent must discover.

### Synthetic Data Is Acceptable

Injected Slack messages, meeting notes, or checklist rows are synthetic additions to a task-specific environment. That is expected and allowed in small amounts. Reviewers grade against ground truth derived from the full environment (real + injected), not against whether every byte predated the task.


## Guidance for Reviewers

Review the business logic before counting calls.

### Confirm the Task Is Legitimately Long-Horizon

- Is the assigned tier Long Horizon or Super Long Horizon, and is its own scale target being used? Fewer than 500 calls is not itself a defect for Long Horizon.
- Is the request realistic for the persona and company situation?
- Does the prompt sound natural, or does it read like a spec sheet / command list?
- Are detailed rules in environment sources the prompt clearly directs the agent to follow?
- Does the environment contain the referenced source trail?
- Is there one coherent outcome?
- Does each repeated lookup contribute necessary evidence?
- Is every required scoped read reachable to the assigned persona, or is the
  designed outcome an affirmative denial plus reporting, escalation, or an
  authorized alternative?
- Is the task difficult because of real scale or reconciliation rather than arbitrary process constraints?
- Could a bulk call validly replace hundreds of record-level calls? If so, require the efficient route.
- Conversely, does a bulk listing omit the evidence the prompt actually asks to preserve? If so, record-level calls are justified.

### Confirm the Ground Truth Is Complete

- Derive cohort sizes from authoritative records.
- Account for pagination and cutoff dates.
- Verify empty surfaces as carefully as populated ones.
- Check exact flag or classification totals.
- Confirm synthetic environment additions are internally consistent.
- Make the Oracle Events sufficient to prove solvability without forcing one invalidly narrow execution trace.

### Review Outcomes First

Follow the normal rubric guidelines:

- Use Outcome criteria for required artifact creation or updates, required content, and facts the user asked to receive directly.
- Use only Outcome and Process as category names in rubrics, reports and coverage maps; do not introduce numbered subtypes.
- Add Process rubrics only when a necessary behavior cannot be verified by a stricter outcome.
- Do not write a rubric for every expected tool call.
- Do not reward a model merely for producing a high call count.

For a large register, assess completeness through source-defined keys, exact totals, required columns, classification rules, and verified artifact contents. The deliverable—not the length of the trajectory—is the primary result. See [How 116 Records Are Graded Without 116 Rubrics](#how-116-records-are-graded-without-116-rubrics) for what that looks like in practice.

For repetitive row-level checks, use the
[explicit spot-check rule](#explicit-spot-check-rule-for-large-redundant-audits):
exact cohort/row controls plus selected grounded spot checks, with no mandatory
minimum count. Do not create one rubric per record-field cell.
