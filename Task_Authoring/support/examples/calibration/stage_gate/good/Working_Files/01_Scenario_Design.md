# Scenario Design — stage-gate-fixture · design only · contains no prompt, OE or criterion text

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Persona | Arthur Blake · `arthur_blake` · arthur.blake@harmonygames.co (Co-founder & CTO, Executive) |
| Competency / skill | Engineering Ops / Analysis and Synthesis (stacked: Actions) |
| Horizon | Long Horizon → extreme profile |

Persona census (`python3 Task_Authoring/tools/persona_view.py reach arthur_blake --no-correspondents --top 3`):

```
REACH  Arthur Blake <arthur.blake@harmonygames.co>  Co-founder & CTO / Executive
clock 2026-02-14

SLACK  user=EMPLOYEE_0025_SLACK_ID  visible channels=216 {'mpim': 72, 'private': 76, 'public': 36, 'im': 32}  messages=372611  public-not-member (UNVERIFIED)=34
  persona posts=38591 last post=2026-02-12  last activity in visible channels=2026-02-13
  C05433XK267    builds                                 public  mem=31  msgs=41107  2023-04-20..2026-02-12
  C04UTBZL6AX    founders                               private mem=7   msgs=40552  2023-03-20..2025-10-06
  C07C2866011    executives                             private mem=9   msgs=28266  2024-07-11..2026-02-13

GMAIL  mailbox=arthur.blake@harmonygames.co threads=4721 messages=6876 range=2023-03-23..2026-02-13
```

Horizon note: Long Horizon assignment, so the extreme profile applies (GEN_EXECUTION §3a).

## 1 Storyline

Known-defects schedule for the IP sale (Feb 12–13 2026), placed against universe_kb timeline spine events of Feb 2026.

- Hub in #winddown: seeded Arthur message C0ADGSZKR3R/1770940000.000100 announces the defect list.
- Leonard's loading-screen report D04UGG61DUM/1770751702.596069 (0.3.309 stuck at 8%).
- Cohort from cohorts.json LIN-OPEN-ENG (open ENG tickets), parent ENG-2280.
- Wind-down call evt_e02ad4661e15802e6a6e84 on Arthur's calendar.
- Lookalike-document trap from trap_catalog D01 and ticket-series trap N01 (ENG-1458 vs GameOfDominoes#1458).

## 1a Coherence audit

Checked against coherence_hazards.json (universe_kb), scope = every record a correct run opens.

| Record | QC category | Fields | Evidence pointer | Hazard id | Disposition |
|---|---|---|---|---|---|
| Timeline review events on GameOfDominoes#1583 | temporal | created_at | GameOfDominoes#1583#ev_2 | T01 | avoid: no review event is graded |
| match3d PRs citing ENG keys | semantic | title | match3d#522 | S01 | avoid: ZOM-616 graded by Linear only |
| Slack keys absent from Linear | cross-service referential | text | C080X4GTZ0E/1741568716.506519 | R01 | avoid: channel not in scope |
| Thread reply_count drift | quantitative | reply_count | C0ADGSZKR3R/1770940000.000100 | Q01 | fold into design: seeded hub has no replies |
| Issue in state PR with merged PR | state/lifecycle | state | ENG-2417 | L01 | avoid: not a defect, outside the cohort |
| Raw-shaped Slack records | identifier/format | id | C05433XK267 | I01 | avoid: #builds not opened |

Sibling-defect sweep: no other open ENG ticket in the cohort carries a merged fix PR (search over ENG-2280 children, pointer linear/issues.json /issues/12).

## 1b Active speakers

| Person | Email | status_at_clock (activity.json) | Seeding role |
|---|---|---|---|
| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | hub author |
| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | base report only |
| Vincent Parker | vincent.parker@harmonygames.co | quiet_since_2025-12 | never given a 2026 voice |

## 1c Identity traps

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
```

| Correct entity | Lookalike | Locator |
|---|---|---|
| Marcus Bennett | Marcus Lee, Marcus mailbox | marcus.bennett@harmonygames.co vs marcus@harmonygames.co |

## 2 Cohort spine

- Rule: open ENG defects (state Bugs or Regression), cohort LIN-OPEN-ENG, parent ENG-2280.
- Surfaces: Linear comments per issue (ENG-2280), PR conversation via GameOfDominoes#1583.
- Shortcut audit: list call returns state only; comments need one read per issue (ENG-2073).

## 3 Hidden authorities

| Authority | Home | Decoy | Governs | Findability proof |
|---|---|---|---|---|
| Cohort rule | Gmail arthur.blake@harmonygames.co/1856689465050769375 | Confluence page_company_home | cohort membership | search "Sunset" returns the thread |
| Tier rule | Trello card 640643a3fd8f3ca308d93195 | Slack C0ADGSZKR3R/1770940000.000100 | tiers | search "tiers" returns the card |

## 4 Delegation lattice

| Fragment | Service | Container | Delegated by record |
|---|---|---|---|
| K1 cohort scope | gmail | arthur.blake@harmonygames.co/1856689465050769375 | C0ADGSZKR3R/1770940000.000100 |
| K2 destination folder | gdrive | d_cc3e90160f490686039986 | C0ADGSZKR3R/1770940000.000100 |

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
| A1 | the known-defects list | C0ADGSZKR3R/1770940000.000100 |

## 5 Chains and trap register

| Trap | Family | Records | Requirement | Resolver |
|---|---|---|---|---|
| T1 | superseding count | C0ADGSZKR3R/1770940000.000100 | totals | ENG-2280 |
| T2 | lookalike document (trap_catalog D01) | d_cc3e90160f490686039986 | destination | owner field |

## 6 Failure-diversity plan

Chain 1 (stale count, ENG-2280) and chain 2 (lookalike folder, d_cc3e90160f490686039986) land on different requirements.

## 7 Deliverables and dependent writes

One schedule in d_cc3e90160f490686039986 and one Slack post in C0ADGSZKR3R, both fed by the cohort.

## 8 Service role map

Slack carries the hub (C0ADGSZKR3R); Linear the cohort (ENG-2280); GitHub the fix evidence (GameOfDominoes#1583).

## 9 Call budget

Fixture only: 3 services, budget not exercised (the real gate checks it with hardness_gate.py).

## 10 QC rails

### Two-reading table

| Decision point | Best reading | Strongest alternative | Resolved by |
|---|---|---|---|
| D1 destination | d_cc3e90160f490686039986 | C0ADGSZKR3R channel post only | authority in arthur.blake@harmonygames.co/1856689465050769375 |

### Reach table (load-bearing records)

| Record | Service | Visibility path |
|---|---|---|
| D04UGG61DUM/1770751702.596069 | slack | persona in the IM |
| arthur.blake@harmonygames.co/1856689465050769375 | gmail | own mailbox |
| evt_e02ad4661e15802e6a6e84 | gcal | own calendar |
| d_63fffeb4fab5233ed5bb73 | gdrive | DENIAL-INTENDED: Leonard's private root is the designed denial (probe, not load-bearing); alternate_evidence_ids: D04UGG61DUM/1770751702.596069 |

## 11 Record plan for /create-injection

| Service | Record | Carrier | Id scheme |
|---|---|---|---|
| slack | hub message C0ADGSZKR3R/1770940000.000100 | ● | sha256 of channel and ts |

### Integrations and companions

| Seeded service | Integration (integrations.json) | Companion | Decision |
|---|---|---|---|
| slack | INT-22 | Slack e-mail notification | none seeded: base rate low for private channels |
| linear | INT-03 | linear[bot] PR comment | none: no PR is seeded |
| github | INT-01 | #engineering-bots mirror C050WGU41HR | none: no PR comment is seeded |

## 12 Self-test results

Lazy-solver pass: the stale count in C0ADGSZKR3R/1770940000.000100 is the only first hit; it is overturned by ENG-2280.

### Self-review

```
HARDNESS GATE (extreme (design)): PASS
  [ok] fixture: thin manifest, not re-run under --rerun lint
```

| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| Temporal | PASS | a prose date contradicts a field | dates re-read: C0ADGSZKR3R/1770940000.000100 is 2026-02-12, before the clock | none |
| Semantic / category | PASS | a title misdescribes its content | S01 kept out of scope (match3d#522 not opened) | none |
| Cross-service referential | PASS | a cited ticket does not exist | ENG-2280 re-read via hg.py | none |
| Quantitative | PASS | the stale count matches no source | count re-derived from ENG-2280 children | none |
| State / lifecycle | PASS | a sibling ticket shares the designed defect | sibling sweep found none (L01 ids ENG-2417 out of cohort) | none |
| Identifier / format | PASS | a seeded id breaks the base scheme | sha256 id b759cfabc37fef15d3b8d50fb4aeb564 follows Ask_Carriers.md | none |
| Other | PASS | the designed disagreement reads as two silent fields | it is a dated human claim in C0ADGSZKR3R/1770940000.000100 | none |
| Decision point D1 | PASS | the channel post alone could be the deliverable | authority arthur.blake@harmonygames.co/1856689465050769375 pins the folder | none |

Unresolved: none.

```
STAGE GATE scenario: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 01_Scenario_Design.md#7c50cac596b6 · 01_Hardness_Manifest.draft.json#2eea4cffbb5d · blocking 0 · warnings 0 · checks 27
[PASS] structure.outputs: 2 output(s) present: 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json
[PASS] structure.inputs: 1 input(s) present: 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md)
[PASS] structure.sections: 19 required sections present and non-empty (01_Scenario_Design.md)
[PASS] structure.placeholders: no placeholders in 01_Scenario_Design.md
[PASS] evidence.storyline: 5/5 items carry a source pointer (min 80%)
[PASS] evidence.coherence_audit: 6/6 items carry a source pointer (min 100%)
[PASS] evidence.hidden_authorities: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.delegation: 3/3 items carry a source pointer (min 90%)
[PASS] evidence.trap_register: 2/2 items carry a source pointer (min 90%)
[PASS] evidence.record_plan: 4/4 items carry a source pointer (min 80%)
[PASS] evidence.active_speakers: 3/3 items carry a source pointer (min 100%)
[SKIP] tool.hardness_gate_design_rerun: hardness_gate --design pasted PASS; re-run skipped (--rerun lint)
[PASS] tool.persona_reach: persona_view reach pasted for arthur.blake@harmonygames.co and matches the re-run (216 channels)
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] kb.coherence_hazards: coherence audit cites 6 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 3 speaker rows carry their activity.json status_at_clock
[PASS] kb.integrations: companions listed per integrations.json (3 INT ids, services ['github', 'linear', 'slack'])
[PASS] kb.storyline: timeline cited; cohorts ['LIN-OPEN-ENG']; trap_catalog ['D01', 'N01']
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] tool.redteam_dual: dual red team present (01b_Redteam_Review.md + .second.md)
[PASS] reach.scenario: 3 scoped load-bearing ids YES for arthur_blake; 1 denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids
[PASS] boundary.prompt_phrases+criterion+oe: human-only boundary clean in 01_Scenario_Design.md (prompt_phrases, criterion, oe)
[PASS] review.counter_readings: 8 evidenced counter-readings (of 8 found; need ≥ 8) in 01_Scenario_Design.md
[PASS] review.coverage: self-review addresses all 8 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```








## 13 Red team (dual)

| Finding | Source | Disposition |
|---|---|---|
| Slides count shortcut | 01b_Redteam_Review.md | fixed: Linear is the authority (ENG-2280) |
| D01 defeated by owner sort | 01b_Redteam_Review.second.md | rebutted: owner differs on d_cc3e90160f490686039986 |
