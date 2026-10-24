# Prompt Brief — stage-gate-fixture · prep only · contains no prompt text
> Built 2026-10-04 from 00, 01_Grounding_Dossier.md, 01_Universe_Inject.sql · Persona view verified: all
> Write 04_Prompt.txt yourself, from scratch, without an LLM (Spec V2).

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Persona | Arthur Blake, arthur.blake@harmonygames.co | CTO; member of C0ADGSZKR3R |
| Competency | Engineering Ops | defect inventory from ENG-2280 |

## 2 · Situation

| Symptom | Seen by | Where it shows | Records the persona cannot see |
|---|---|---|---|
| defect count in the hub disagrees with the tracker | persona | C0ADGSZKR3R/1770940000.000100 | none |

## 3 · Investigation → action

Questions: which ENG defects are still open (ENG-2280 children); which claimed fixes lack a merged PR (GameOfDominoes#1583). Writes: schedule file, channel post.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipient | Catalog write | Fed by |
|---|---|---|---|---|---|
| defect schedule | open defects with fix evidence | d_cc3e90160f490686039986 | leonard.hayes@harmonygames.co | gdrive create | ENG-2280 |
| hand-off note | location of the schedule | C0ADGSZKR3R | leonard.hayes@harmonygames.co | slack post | d_cc3e90160f490686039986 |

### 4b · Canonical outcome (one acceptance class)

| Deliverable | Field | Fixed value (pinned) | Delegated by (prompt span) | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| defect schedule | destination | d_cc3e90160f490686039986 | — | that folder only | material |
| defect schedule | open-defect set | ENG-2280 children not Canceled or Done | — | exact key set | material |
| defect schedule | file title and format | — | "put the schedule in my drive folder" names no title (d_cc3e90160f490686039986) | any title, Doc or Sheet | representational |
| hand-off note | channel and recipient | C0ADGSZKR3R · leonard.hayes@harmonygames.co | — | that channel only | material |

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 hub count | stale estimate | C0ADGSZKR3R/1770940000.000100 | YES | met first; overturned by ENG-2280 | latching | No |
| F2 loading-screen report | 0.3.309 stuck at 8% | D04UGG61DUM/1770751702.596069 | YES | evidence | buried in IM | No |

## 5a · Search-as-persona proof

| Fact | Service | Natural query | Visible hits | Hidden by ACL | First visible hit | Found? |
|---|---|---|---|---|---|---|
| F1 hub count | slack | "defect list" | 1 | 0 | C0ADGSZKR3R/1770940000.000100 | YES |
| F2 loading-screen report | slack | "0.3.309" | 1 | 0 | D04UGG61DUM/1770751702.596069 | YES |

```
SEARCH slack '0.3.309' as arthur_blake  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "D04UGG61DUM/1770751702.596069", "channel": "D04UGG61DUM", "kind": "im", "date": "2026-02-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I updated DD from app store to 0.3.309 and got stuck at the loading screen at 8%"}
note: --no-hidden: containers outside the persona's view were not scanned
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category | Incorporating source | Inferable |
|---|---|---|---|---|
| open-defect scope | arthur.blake@harmonygames.co/1856689465050769375 | scope | thread in own mailbox, unique, instructions only | gotcha: needs a scope trigger |

## 7 · Dates and constraints

| Item | Absolute date | Source | Past fact or deadline |
|---|---|---|---|
| data-room deadline | 2026-02-16 | evt_e02ad4661e15802e6a6e84 | deadline |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Dynamic change | yes | yes | C0ADGSZKR3R/1770940000.000100 vs ENG-2280 | neither record named |

## 9 · Must not appear in the prompt

- Ids: C0ADGSZKR3R, ENG-2280, d_cc3e90160f490686039986 (dossier §7).
- Tool names: slack_send_message, gdrive_create_file (catalog.json).

## 10 · Entity traps

```
ENTITY email:oscar.bennett@harmonygames.co  name=Oscar Bennett  kind=person  emails=['oscar.bennett@harmonygames.co']
```

| Correct entity | Lookalike | How they differ | Locator |
|---|---|---|---|
| Leonard Hayes | none in scope | single Leonard | leonard.hayes@harmonygames.co |
| ENG-1458 | GameOfDominoes#1458 | ticket vs PR number (trap_catalog N02) | ENG-1458 |

## 11 · Pre-submit checklist

- [ ] Prompt names the problem, not the method (Prompt Writing §08).
- [ ] No id from §9.

## 12 · Blockers and routed defects

None routed; every fact verified this run (persona_view, hg.py).

## 13 · Self-review

| Area | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| UGT | PASS | the channel post alone could be the deliverable | authority in arthur.blake@harmonygames.co/1856689465050769375 pins the folder | none |
| Clarity | PASS | the hand-off channel is left open | C0ADGSZKR3R is the only shared channel with Leonard (§4) | none |
| Incorporation | PASS | the scope rule is unreachable | own mailbox thread arthur.blake@harmonygames.co/1856689465050769375, can-see YES | none |
| Truthfulness | PASS | 0.3.309 is the wrong build | D04UGG61DUM/1770751702.596069 states 0.3.309 | none |
| Feasibility / ACL | PASS | the folder is not writable | owner is the persona (d_cc3e90160f490686039986) | none |
| Contrived register | PASS | the brief implies a format list | §4 holds requirements only (§2.7) | none |

No-transcribable-sentence pass: run over every line and cell; zero hits (stage_gate boundary scan).

Unresolved: none.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 04_Prompt_Writing_Brief.md#b2e5ff44a81f · blocking 0 · warnings 0 · checks 23
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt, 02_Reference_Files_Manifest.md, 01a_Hardening_Report.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#07dc66233f21, 01_Hardness_Manifest.json#478336148743, 01_Grounding_Dossier.md#bb1aa413b80d)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#c507ded42175)
[PASS] chain.reference-files: upstream 'reference-files' PASS pasted and current (02_Reference_Files_Manifest.md#e9b203ccc16e)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 1/1 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 6/6 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 2/2 items carry a source pointer (min 100%)
[PASS] evidence.dates: 1/1 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 2/2 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 2 facts proven findable by persona_view search as arthur_blake
[PASS] reach.brief: 2 scoped load-bearing ids YES for arthur_blake
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.canonical_outcome: canonical outcome table: 4 field(s), each fixed or delegated
[PASS] boundary.transcribable+prompt_phrases+criterion+oe: human-only boundary clean in 04_Prompt_Writing_Brief.md (transcribable, prompt_phrases, criterion, oe)
[PASS] boundary.anchor_naming: 0 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 7 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```







