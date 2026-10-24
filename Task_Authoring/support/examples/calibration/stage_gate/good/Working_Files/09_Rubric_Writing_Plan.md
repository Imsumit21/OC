# 09 Rubric Writing Plan — stage-gate-fixture
Generated 2026-10-04 · Clock 2026-02-14T00:00:00Z · Persona Arthur Blake arthur.blake@harmonygames.co · Tier Long-Horizon · Human time 10.50 h · OE status: /oe PASS 2026-10-04

Canonical outcome: brief §4b (one acceptance class per deliverable); rows grade material fields only.

## A · Coverage matrix

| P | Source (prompt span · OE n) | What must be verified | Final state that proves it | Category | Values the criterion must name |
|---|---|---|---|---|---|
| P1 | "put the schedule in my drive folder for the sale" · OE 3 | schedule file in the sale folder | file in folder | Outcome | F3 (exact) `d_cc3e90160f490686039986` |
| P2 | "some of the stuff people said was fixed probably isnt" · OE 2 | loading-screen defect listed open | schedule row | Outcome | F2 (exact) `0.3.309` |
| P3 | "tell him in winddown once its there" | hand-off post | message | Outcome | F1 (exact) `winddown` |
| P4 | "go through whats actually still open on domino delights" | Canceled tickets outside the open set | schedule rows | Outcome | F5 (exact) `ENG-2280` |
| P5 | "go through whats actually still open on domino delights" | open-defect total | schedule total | Outcome | F5 (exact) |

## A2 · Grading risks and weight

| P | Title specified? | Distractor? | Ambiguous evidence? | Kind of work + reason | Band | Decided by | Spot-check group | Duplicate risk (per deliverable) | Predicted all-fail basis |
|---|---|---|---|---|---|---|---|---|---|
| P1 | no | no | no | interpretation: "my drive folder" resolves to the root | 3 | A1 | — | none | none |
| P2 | no | T1 → handling | no | multi-source: hub vs IM report | 5 | T1 | — | none | none |
| P3 | no | no | no | lookup: one channel | 1 | A1 | — | none | none |
| P4 | no | no | no | interpretation: state filter | 3 | C1 | — | none | none |
| P5 | no | no | no | multi-source: tracker count vs hub estimate | 5 | C1 | — | schedule only (the reply carries no count) | none |

## B · OE trace

| OE | Kind | Proved by row(s) | Own row? |
|---|---|---|---|
| OE 1 | discovery | P2 | no: result carried by P2 |
| OE 2 | discovery | P2 | no |
| OE 3 | write | P1 | yes |

## C · Process candidates — three-condition test

No Process candidates: every requirement has an Outcome row (P1–P5).

## D · Spot-check groups

No repetitive item groups in this fixture (P1–P5 are single items; P4/P5 grade the open set as one aggregate).

## E · Summary

Rows 5 · Outcome 5 · Process candidates 0 — ≥ 1 Outcome ☑ · builder minimum 5 ☑ · predicted all-fail rows 0 ☑
Failure diversity: largest unit of discovery C1 / ENG-2280 at 47% of 17 (≤ 50% ☑) · chains landing on distinct rows ☑
Bands: 5 ×2 · 3 ×2 · 1 ×1

Visibility proof (persona_view, pasted verbatim):

```
arthur_blake slack D04UGG61DUM/1770751702.596069: YES
arthur_blake gdrive d_cc3e90160f490686039986: YES
[YES LB] L2 slack.slack_messages insert b759cfabc37fef15d3b8d50fb4aeb564, C0ADGSZKR3R/1770940000.000100 - persona EMPLOYEE_0025_SLACK_ID is in members of private winddown
```

## F · Shortcut probe

```
SHORTCUT PROBE as arthur_blake <arthur.blake@harmonygames.co> · values 09_Rubric_Writing_Plan.md (4 values, 0 populations, sha a7959b8c90f6) · k 3 · services all · sql 01_Universe_Inject.sql
SKIPPED value:"48" (shorter than 3 characters)
verdict: CLEAR (0 shortcut records)
```

Dispositions: none needed (verdict CLEAR). The skipped value `48` is a two-character count; P5 grades it exactly.

## Self-review

| Row | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| P1 | PASS | another folder fits "my drive folder" | owner of d_cc3e90160f490686039986 is the persona (F3) | none |
| P2 | PASS | a valid answer lists the defect as fixed | D04UGG61DUM/1770751702.596069 is dated after the claimed fix (F2) | none |
| P3 | PASS | a DM to Leonard is also valid | prompt names winddown (F1, C0ADGSZKR3R) | none |
| P4 | PASS | Canceled tickets count as open | Linear state set re-read via hg.py (ENG-2280, F5) | none |
| P5 | PASS | the hub estimate is the expected total | tracker children re-read via hg.py (ENG-2280, F5) | none |

Predicted all-fail re-check: every value reachable (can-see YES above); 0 rows on the four bases. Every value re-verified through hg.py. No criterion text: scan over every cell, zero hits.

Unresolved: none.

```
STAGE GATE rubric-writing: PASS — Task_Authoring/support/local_search/cache/stage_gate_selftest/gen · 09_Rubric_Writing_Plan.md#1685f5279950 · blocking 0 · warnings 0 · checks 26
[PASS] structure.outputs: 1 output(s) present: 09_Rubric_Writing_Plan.md
[PASS] structure.inputs: 3 input(s) present: 04_Prompt.txt, 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#8626697ef090)
[PASS] chain.oe-check: upstream 'oe-check' PASS pasted and current (08_OE_Check.md#5aff27342bc4, 08_Oracle_Events.md#6d482956142b)
[PASS] structure.sections: 7 required sections present and non-empty (09_Rubric_Writing_Plan.md)
[PASS] structure.placeholders: no placeholders in 09_Rubric_Writing_Plan.md
[PASS] structure.oe_status: OE status line present
[PASS] evidence.prompt_spans: 5 quoted span(s) verified as exact substrings of 04_Prompt.txt
[PASS] evidence.values_fids: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.fids_in_ledger: 4 F-ids resolve to ledger rows
[PASS] structure.bands: 5 A2 rows for 5 A rows; 0 band(s) not 1/3/5
[PASS] structure.summary_rows: summary Rows 5 vs 5 matrix rows
[PASS] tool.visibility_proof: 3 pasted can-see lines match the re-run; every required id has a YES line
[PASS] reach.plan_fids: 3 scoped id(s) behind 4 cited F-ids YES for arthur_blake
[PASS] validity.predicted_allfail: 0 predicted all-fail rows (tolerance 0)
[PASS] diversity.authority_share: largest unit of discovery authority C1 decides 47% of 17 weight (≤ 50%; transitive over Depends-on, 7 units)
[PASS] structure.exact_set_rows: every spot-check population names its exact-set Outcome row (or no population is sampled)
[PASS] tool.shortcut_probe: shortcut_probe pasted (4 values, 0 populations, k 3, verdict CLEAR); 0 reported item(s), all dispositioned
[SKIP] tool.shortcut_probe_rerun: shortcut_probe re-run skipped (--rerun lint)
[PASS] boundary.criterion+replacement+prompt_phrases: human-only boundary clean in 09_Rubric_Writing_Plan.md (criterion, replacement, prompt_phrases)
[PASS] boundary.agent_cells: no cell begins with 'Agent'
[PASS] review.counter_readings: 5 evidenced counter-readings (of 5 found; need ≥ 5) in 09_Rubric_Writing_Plan.md
[PASS] review.coverage: self-review addresses all 3 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```







