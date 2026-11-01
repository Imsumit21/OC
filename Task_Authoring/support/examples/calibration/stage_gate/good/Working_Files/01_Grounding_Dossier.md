# Grounding Dossier — stage-gate-fixture · contains no prompt, OE or criterion text

## 1.A Structural

| Table | Columns (NOT NULL) | Base sample ids | Timestamp format |
|---|---|---|---|
| slack.slack_messages | id, ts, channel_id, type, text, created_at | C0ADGSZKR3R/1770937460.360699 | ISO-Z, ts 6 decimals |

## 1.B Entity table

| Entity | Canonical | Services (cited) | Verdict |
|---|---|---|---|
| Arthur Blake | arthur.blake@harmonygames.co | Slack EMPLOYEE_0025_SLACK_ID in C0ADGSZKR3R | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | Slack D04UGG61DUM/1770751702.596069 | AGREE |

## 1.C Voice and realism

Seeded speakers, each checked in activity.json; lengths and hours from conventions.json (slack length_chars_by_channel_type, private channel median band).

| Speaker | Evidence |
|---|---|
| Arthur Blake (arthur.blake@harmonygames.co) | activity.json status_at_clock active_feb_2026; last Slack post 2026-02-12; seeded post at 23:46Z inside his conventions.json per_person_hours_and_style window |

## 1.D Keyword / findability

| Term | Hits / pointer |
|---|---|
| "defect list" | NEW TERM — introduced in C0ADGSZKR3R/1770940000.000100, reached via the #winddown hub |
| "loading screen" | 207 visible hits; decisive D04UGG61DUM/1770751702.596069 |

## 1.E Persona reach

| Record | Class | Visibility path |
|---|---|---|
| C0ADGSZKR3R/1770940000.000100 | seeded, Slack private | Arthur in members of #winddown |
| D04UGG61DUM/1770751702.596069 | base, Slack IM | Arthur is a party |
| arthur.blake@harmonygames.co/1856689465050769375 | base, Gmail | own mailbox |
| evt_e02ad4661e15802e6a6e84 | base, GCal | own calendar |

```
CHECK-SQL as arthur_blake <arthur.blake@harmonygames.co>
[YES LB] L2 slack.slack_messages insert b759cfabc37fef15d3b8d50fb4aeb564, C0ADGSZKR3R/1770940000.000100 - persona EMPLOYEE_0025_SLACK_ID is in members of private winddown
[YES LB] base slack D04UGG61DUM/1770751702.596069 - base record: message inherits channel: persona EMPLOYEE_0025_SLACK_ID is in members of im D04UGG61DUM
[YES LB] base gmail arthur.blake@harmonygames.co/1856689465050769375 - base record: thread is in the persona's own mailbox arthur.blake@harmonygames.co
[YES LB] base gcal evt_e02ad4661e15802e6a6e84 - base record: event is on the persona's own calendar arthur.blake@harmonygames.co

summary: {'YES': 1}  unscoped rows (always visible): 0
  slack.slack_messages: {'YES': 1}
verdict: PASS (0 load-bearing rows not visible)
```

## 1.F Collision checks

Minted id b759cfabc37fef15d3b8d50fb4aeb564 (C0ADGSZKR3R, ts 1770940000.000100): hg.py search lookup slack, scan_complete true, 0 hits.

## 2 Record ledger

| # | Service | Table | Id | Manifest element | Carrier | Reach | Role |
|---|---|---|---|---|---|---|---|
| 1 | slack | slack_messages | C0ADGSZKR3R/1770940000.000100 | A1 / T1 | ● | member | first link |

## 3 Findability and discovery-order proofs

| Record | Likely query | Term present | Chain position |
|---|---|---|---|
| C0ADGSZKR3R/1770940000.000100 | "defect" in #winddown | NEW TERM, newest message after 1770937460.360699 | first link |

## 4 Self-validation

| QC category | Tool-enforced | Manual evidence |
|---|---|---|
| Temporal Field | sql_lint clean | text date "tomorrow" = 2026-02-13, before the clock (C0ADGSZKR3R/1770940000.000100) |

## 4a Integrations and companions

| Seeded service | Integration | Companion seeded | Reason |
|---|---|---|---|
| slack | INT-22 | none | Slack e-mail notifications are not sent for this private-channel post type (integrations.json base rate) |

## 5 Touched-data census and coherence hazards

Census from coherence_hazards.json: every record a correct run opens was matched against the hazard index.

| Record | Category | Hazard id | Disposition |
|---|---|---|---|
| GameOfDominoes#1583 | temporal | T01 | avoid |
| match3d#522 | semantic | S01 | avoid |
| C080X4GTZ0E/1741568716.506519 | referential | R01 | avoid |
| C0ADGSZKR3R/1770940000.000100 | quantitative | Q01 | fold into design |
| ENG-2417 | state lifecycle | L01 | avoid |
| C05433XK267 | identifier format | I01 | avoid |

## 6 Intended disagreements

| Claim met first | Overturned by | Why realistic |
|---|---|---|
| hub count in C0ADGSZKR3R/1770940000.000100 | ENG-2280 children | a dated human estimate superseded by the tracker |

## 7 Constraints for the prompt brief

- Never name C0ADGSZKR3R or ENG-2280; the deadline is 2026-02-16 (evt_e02ad4661e15802e6a6e84 follow-up).

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | the known-defects list; the open defect list | C0ADGSZKR3R/1770940000.000100 |

## 8 Facts for the human

| Locator | Base / seeded | Fact | Reach | Role |
|---|---|---|---|---|
| C0ADGSZKR3R/1770940000.000100 | seeded | Arthur, 2026-02-12 23:46Z, defect list announced | member | claim met first |
| D04UGG61DUM/1770751702.596069 | base | Leonard, 2026-02-10, 0.3.309 stuck at 8% | IM party | evidence |
| arthur.blake@harmonygames.co/1856689465050769375 | base | 9-message thread, last 2026-02-11T04:28:45Z | own mailbox | authority |

## 8a Fact sheet (`facts` in 01_Hardness_Manifest.json)

| Key | Value | Kind | Must appear in |
|---|---|---|---|
| defect list | open | status | C0ADGSZKR3R/1770940000.000100 |

```
FACT CHECK: PASS — 1 text-bearing rows, 1 declared facts, 0 declared superseded records
Errors: none
```

## 9 Platform follow-ups

- None for ○ carriers: the only seeded row is a Slack message (● carrier, C0ADGSZKR3R).

## 10 Self-review

Tool outputs, verbatim:

```
schemas touched (1): slack
rows by schema: {'slack': 1}  total rows: 1  ops: {'insert': 1}
errors: 0  warnings: 0
```

```
BASE CHECK (/injection A + C, static): PASS  — 1 inserts, 0 updates
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
```

```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```

```
HARDNESS GATE (extreme): PASS
  [ok] fixture: thin manifest, not re-run under --rerun lint
```

Walked /injection Check A, Check B and Check C in order against the SQL; touched-data census in section 5.

| Category | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| Temporal | PASS | "tomorrow" resolves after the clock | 2026-02-13 is before 2026-02-14 (C0ADGSZKR3R/1770940000.000100) | none |
| Semantic / category | PASS | #winddown purpose does not fit a defect list | channel purpose covers the wind-down hand-off (C0ADGSZKR3R) | none |
| Cross-service referential | PASS | the IM report is a different build | D04UGG61DUM/1770751702.596069 names 0.3.309 | none |
| Quantitative | PASS | the hub count matches no source | ENG-2280 children re-read via hg.py | none |
| State / lifecycle | PASS | a sibling ticket also shows the designed defect | L01 hazard ids (ENG-2417) are outside the cohort | none |
| Identifier / format | PASS | the seeded id deviates from the sha scheme | b759cfabc37fef15d3b8d50fb4aeb564 = sha256 of channel and ts | none |
| Other | PASS | the disagreement reads as two silent fields | dated human claim vs tracker (ENG-2280) | none |
| Designed disagreement | PASS | the hub count is an unintended inconsistency | it is Arthur's dated estimate, overturned by ENG-2280 | none |

Unresolved: none.

```
STAGE GATE injection: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 01_Universe_Inject.sql#07dc66233f21 · 01_Hardness_Manifest.json#478336148743 · 01_Grounding_Dossier.md#e60eccb5cb64 · blocking 0 · warnings 0 · checks 28
[PASS] structure.outputs: 3 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#7c50cac596b6, 01_Hardness_Manifest.draft.json#2eea4cffbb5d)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 2/2 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 4/4 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 1/1 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 3/3 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 0, rows 1
[SKIP] tool.base_check_rerun: base_check pasted PASS; re-run skipped (--rerun lint)
[SKIP] tool.hardness_gate_rerun: hardness_gate (SQL) pasted PASS; re-run skipped (--rerun lint)
[PASS] structure.design_delta: final manifest keeps all 2 draft ids
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 4 scoped load-bearing ids YES for arthur_blake
[PASS] structure.facts_declared: manifest declares 1 load-bearing fact(s) in `facts`
[SKIP] tool.fact_check_rerun: fact_check --no-leak pasted PASS; re-run skipped (--rerun lint)
[PASS] kb.coherence_hazards: coherence audit cites 6 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 1 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (1 INT ids, services ['slack'])
[PASS] boundary.prompt_phrases+criterion+oe: human-only boundary clean in 01_Grounding_Dossier.md (prompt_phrases, criterion, oe)
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 8 evidenced counter-readings (of 8 found; need ≥ 8) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```






