# 09 — Rubric Coverage Plan & Rubric Check (Playbook) — HarmonyGames · Spec V2

> Command: `/create-rubric-plan` (prep) · `/create-rubric-plan check` (check) · Writes: `task_inputs/09_Rubric_Coverage_Plan.md` / `task_inputs/Working_Files/09_Rubric_Check.md` · Paired eval: `/rubric` · Read first: `setup/GEN_EXECUTION.md`

## Purpose

Rubric criteria are human-written in Spec V2: prefill is off and the Criteria Builder
opens empty. The last audit's top defects were incorrect (22%), non-atomic (22%) and
missing coverage (21%), then unauthorized (6%) and overly specific (5%). Rubrics failed
correct answers (44%) more often than they passed wrong ones (29%)
(`Task_Authoring/references/Docs/07_Rubric_Writing.md` §10).

The plan targets those defects. It lists everything that must be graded, the final
state that proves it, the values a self-contained criterion must name, the category
decision and the weight band. It never contains the criterion. `check` mode lints the
human's builder export against the plan and the twelve-point checklist.

## The authorship boundary

- Criteria are human-only (GEN_EXECUTION §2; `07_Rubric_Writing.md` §1: "The eval sandbox may be used to query the universe, never to draft criteria").
- The plan describes what must be verified, not how to word it. It contains no criterion sentence ("Agent sends…", "Agent's record states…"), no draft rows, no example criteria for this task, no justification or evidence text, and no suggested titles. Rows are noun phrases plus values ("owner notification — recipient = F4").
- `check` is report-only: quote, rule, defect, plan row. It never proposes replacement wording, never rewrites, splits, merges or reweights, never fixes typos.
- If asked to write, draft, rewrite or polish criteria (or OEs), decline per GEN_EXECUTION §2 and offer prep or check mode.

## Inputs / Output

Prep inputs (`task_inputs/` = `Task_Authoring/task_inputs/`):
- `04_Prompt.txt` — human; required.
- `08_Oracle_Events.md` — human; **required, stop if missing** (the plan uses it as the path reference). `/rubric` itself does not require an `/oe` PASS (it treats a supplied OE as a comparison reference); if `/oe` has not passed, proceed only when `08_OE_Check.md` shows no BLOCKING finding, and mark the plan PROVISIONAL.
- `08_Evidence_Ledger.md` — required (values, write capability, traps, open risks); if missing, run `/create-oe-ledger` first.
- `00_Assigments.md` (persona, tier), `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md`, `05_Human_Time_Worksheet.md` if present (set-size sanity).
- `01_Scenario_Design.md` (§10 grading devices: cohort multisets, aggregate invariants, spot-check groups) and `01_Hardness_Manifest.json` (chains → `ends_in`, traps → requirement, authorities → `governs`) if present — they say which requirement each independent difficulty lands on.
- Universe: `Task_Authoring/tools/hg.py search` to re-verify values (`get` takes a service-relative `--file`, e.g. `--file contacts.json`). Tools: `Evals/references/tools/catalog.json`.
- Rules: `Evals/3_Rubrics_Eval.md` local-override table (`hg-strict-overrides-v1` — stricter than the Docs and applied by `/rubric`), `07_Rubric_Writing.md`, `06_Oracle_Events.md` §8, `09_Long_Horizon_Task.md` §9, `10_Common_Errors_and_PreQC.md` §8, `11_QC_Companion.md` §1–2, `12_Example_Task.md` §5, `04_Persona_ACL_Policy.md` §5 and §9, QC Spec `Task_Authoring/references/Docs/QC_Spec_V2.csv` (Rubrics dimensions).

Check inputs: the above, plus `09_Rubric_Coverage_Plan.md` (required — run prep first)
and `09_Rubrics.json`, the builder JSON export (required — stop if missing).

Output: `task_inputs/09_Rubric_Coverage_Plan.md` (prep) or `task_inputs/Working_Files/09_Rubric_Check.md`
(check). `09_Rubrics.json` is never touched.

## Hard gates

1. **Human artifacts first.** No prompt or no OEs, no plan.
2. **No criterion text** (boundary above). Self-scan before saving: no cell beginning "Agent", no agent-subject sentence, no quoted candidate wording.
3. **Prompt-traced.** Every row quotes a prompt span. An OE result the prompt never asked for is not a row (unstated expectation). A discovery OE maps to the row whose final state proves it.
4. **Outcome first.** Every write OE → a result row, plus one content row per requirement the prompt sets for it. Every fact the user asked to be told → a final-response row. Process only as a candidate, for ordering (rarely source verification) that no Outcome can prove, with the three-condition test recorded per condition. When in doubt, Outcome.
5. **Self-contained values.** Each row lists the exact values its criterion must name (emails, IDs, amounts, dates, counts, the specific finding) with ledger F-IDs, re-verified now. Exact for IDs, dates, counts and addresses; tolerance only for calculated or rounded figures. Clock 2026-02-14T00:00:00Z.
6. **Atomic, no duplicates.** One verifiable claim per row. Split independently variable contents of one artifact; never pair a factual claim with a formatting claim. Each fact is graded once, where it matters most.
7. **Four prohibitions** (`07_Rubric_Writing.md` §6). No unstated expectations. No single conclusion on ambiguous evidence unless a careful human reading reaches the same answer. Grade how a distractor is handled, not its disclosure. No hard-coded titles or phrasings the prompt did not specify. Under the Evals overrides, a **prohibition-only or absence-only** acceptance always fails Negative Criteria — record each exclusion as a preserved state or scope boundary on its own row.
8. **Weight by the kind of work** (QC Spec V2 "Criteria Weights", applied by the Evals override): 1 = direct lookup or literal check from one source; 3 = interpretation, calculation, comparison or limited reconciliation; 5 = multi-source reconciliation, deeper reasoning, cross-modal evidence or tracing. Record the kind and its reason per row. Only 1/3/5. Essential-and-easy is still 1.
9. **Passable.** Every write row cites a feasible ledger write. No row depends on evidence outside the persona's view, requires describing a restriction the agent only saw as "not found", expects a successful retry on a rate-1.0 tool, or grades recovery as a non-action.
10. **One destination.** If two valid routes end in different final states, stop: that is a Unique Ground Truth defect in the prompt (`07_Rubric_Writing.md` §9; `11_QC_Companion.md` §1), not a rubric problem. Where routes differ but the destination is the same, mark the row "phrase broadly"; never enumerate branches.
11. **Evals overrides** (`Evals/3_Rubrics_Eval.md`). Self-containment is **title-only** — the values a row lists must all be nameable in the title. No ranking word (`primary`, `main`, `chief`, `principal`) that admits what it outranks. Multi-recipient content is planned per recipient unless one message to everyone is the graded artifact. Rows that would all fail on one agent error form one cascading-overlap group — note each group. **Predicted all-fail:** mark any row a careful correct run could still fail (unreachable, unpassable, over-specific); two or more fail the rubric before any run.
12. **Failure diversity.** Map each independent chain, hidden authority and trap requirement from the manifest to the row(s) it decides. No single discovery may decide more than half of the total weight; independent chains land on different rows, so failing runs differ on ≥ 2 rubric results (the failure-pattern gate).

## Procedure — prep mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook, `07_Rubric_Writing.md` and `06_Oracle_Events.md` §8. Load inputs; stop per gate 1.
- [ ] Step 1 — Outcomes. Walk the OEs in order. Write event → result row (target, recipient, location) + one content row per prompt-set requirement. Discovery event → the content or final-response row that carries its result (section B); no separate row unless the prompt asks for that result itself. Each Tell requirement in the ledger → final-response row.
- [ ] Cross-check with the ledger: every requirement R has a row; every OE appears in section B.
- [ ] Step 2 — gaps. List requirements no Outcome row can verify: ordering stated or implied by the prompt (A before B, one step gating another); rarely, source verification where the right answer also sits in a shallow source and no Outcome can be made specific enough.
- [ ] Step 3 — three-condition test per candidate: (1) required by every valid path, or phrasable broadly enough; (2) no stricter Outcome can capture it; (3) a behavioural property, not an execution trace. Record each condition with its reason. Any fail → name the Outcome row to tighten and the value that tightens it.
- [ ] Fill values from the ledger and re-verify each in the universe.
- [ ] Per row mark: title/phrasing specified by the prompt (quote it, or "no — must not hard-code"); distractor present (ledger T-ID → grade handling); ambiguous evidence (ledger risk # → no single conclusion); kind of work with a reason; weight band; the chain / authority / trap that decides it; predicted all-fail risk.
- [ ] Failure-diversity check (gate 12): weight decided by each discovery; flag any discovery above 50%.
- [ ] Spot-check: for repetitive items of equal importance, choose ≤ 5 hard or edge items per group (say why each) plus one volume row with the expected count. Never spot-check a core requirement; never one row per line of a long output.
- [ ] Duplicate risk: for each value appearing in more than one deliverable, name the one row that grades it.
- [ ] Friction: recovery appears as an Outcome on what the alternative source yielded; no row names the failing tool.
- [ ] Fill the summary (section E), self-scan for criterion text (gate 2), write the plan.

## Plan template

Write exactly these headings and columns.

```text
# 09 Rubric Coverage Plan — <task id>
Generated <date> · Clock 2026-02-14T00:00:00Z · Persona <name> <email> · Tier <…> · Human time <h> · OE status: /oe PASS <date> | PROVISIONAL

## A · Coverage matrix
| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs; exact / tolerance) |

## A2 · Grading risks and weight
| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk / overlap group | Predicted all-fail risk |

## B · OE trace
| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |

## C · Process candidates — three-condition test
| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |

## D · Spot-check groups
| G | Item set (F-IDs, total N) | Sampled items (≤ 5) and why hard/edge | Volume row | Core requirement? (must be no) |

## E · Summary
Rows N · Outcome N · Process candidates N — ≥ 1 Outcome ☐ (no Process ratio under the Evals override; QC Spec V2 still fails > 50% Process) · builder minimum 5 ☐ · one volume row per spot-check group ☐ · predicted all-fail rows ≤ 1 ☐
Failure diversity: largest single-discovery share of weight N% (≤ 50% ☐) · chains landing on distinct rows ☐
Bands: 5 ×N · 3 ×N · 1 ×N
Set size: N rows for <h> h (reference: 31 criteria for a ~10-hour task; ~60 signals duplicate grading, ~12 missing coverage)
Coverage: requirements N/N · OEs N/N · writes N/N · told facts N/N · friction N/N
Four prohibitions: ☐ unstated expectations ☐ conclusions on ambiguous evidence ☐ grading the distractor ☐ hard-coded titles/phrasings
Blocking: <UGT defects · infeasible writes · unverified visibility>
```

## Procedure — check mode (checklist)

- [ ] Load `09_Rubrics.json` and the plan; stop if either is missing. Edit neither.
- [ ] Inspect the JSON before linting: top-level shape and the keys each criterion carries. Record which key holds the criterion text, weight, category, justification and evidence. Do not assume a schema; a field absent or empty on a criterion is a finding (the builder needs all three: criterion, justification, evidence).
- [ ] Number criteria C1…Cn in file order. The denominator is the authored count; fewer than 5 breaks the builder minimum.
- [ ] Coverage: map every criterion to plan rows. A plan row with no criterion is a coverage gap (one numerator entry each; never added to the denominator). A criterion with no plan row and no prompt trace is unauthorized.
- [ ] Lint each criterion against the twelve-point checklist (`07_Rubric_Writing.md` §12) and the plan:
  - duplicate of another criterion (same fact) · non-atomic (independently variable claims, or fact + format) · not self-contained (does not name the answer, or leans on justification/evidence for a value)
  - passive or artifact subject (not agent-centric) · off-pattern but still an agent action (note only) · any catalog tool name in any field
  - prohibition-only or absence-only acceptance (always a Negative Criteria failure under the Evals override, even when the prompt prohibits the action) — "does not", "must not", "never", "no", "without", "fails to", "avoids" are leads, not proof; a descriptive negative fact inside an affirmative criterion is fine
  - title-only self-containment: a value supplied only by justification/evidence or a sibling title · a ranking word (`primary`, `main`, `chief`, `principal`) admitting what it outranks · content bundled across recipients whose deliveries are graded separately · rows forming a cascading-overlap group
  - predicted all-fail: a row a careful correct run would still fail (count them; two or more fail the rubric)
  - disjunctive (enumerates routes for the judge to pick) · hard-coded title or phrasing the prompt did not specify · grades the distractor · hard-codes a conclusion the plan marks ambiguous
  - value contradicts the ledger or the clock · requires describing a restriction the agent only saw as "not found" · unpassable (no catalog write, retry on a rate-1.0 tool, evidence outside the persona's view)
  - weight not 1/3/5, or off the plan band (record one level vs two levels)
  - Process: which of the three conditions each fails; missing Process where section C holds a valid candidate and the prompt has a sequential or causal dependency (non-fail)
- [ ] Assign severity once per criterion, at its highest level. Tally against the thresholds; evaluate the stand-alone dimensions separately.
- [ ] Write the report. No replacement wording anywhere.

Severity — mapped to the Evals overrides (`hg-strict-overrides-v1`); `/rubric` decides.

| Defect | Severity |
|---|---|
| Duplicate grading | Moderate (`07_Rubric_Writing.md` §7) |
| Cascading-overlap group (rows all failing on one agent error) | Moderate, once per group |
| Requires describing a restriction never shown | Moderate — unauthorized (`04_Persona_ACL_Policy.md` §9) |
| Overly specific — rejects a valid prompt-authorized answer | Major (wording preference rejecting nothing: Minor) |
| Overly broad | Moderate |
| Not agent-centric (subject is not the Agent, or names a tool) | Major, plus the Agent-Centric dimension fails |
| Non-atomic multi-recipient content where deliveries are graded separately | Major |
| Ranking word admitting what it outranks | Major if only a supporting field states the exclusion, else Moderate |
| Incorrect, unauthorized, non-atomic, not self-contained, disjunctive, hard-coded conclusion or title, graded distractor, unpassable — when it would fail a correct answer or pass a wrong one | Major |
| The same defects with a precision-only effect | Moderate |
| Harmless wording or specificity | Minor |
| Coverage gap | Major if the uncovered row is a core requirement, else Moderate |

| QC Spec V2 dimension | Fails when |
|---|---|
| Overall Rubric Quality | > 10% major, > 15% moderate-or-worse, or > 20% minor-or-worse |
| Criteria Weights | ≥ 15% off by two levels (1 vs 5) or ≥ 30% off by one level; any value other than 1/3/5 |
| Category Balance / Process | Zero Outcome (Evals); QC Spec V2 also fails Process > 50%; 2+ Process failing the three-condition test |
| Agent-Centric Phrasing | 1+ criterion passive or naming a tool |
| Negative Criteria | 1+ prohibition-only or absence-only criterion (Evals: even with an explicit prompt prohibition) |
| Predicted all-fail | 2+ rows predicted to fail every run (Evals) |
| Spot checks | > 5 samples in a group, or a group with no volume row (Evals) |

## Check report template

```text
# 09 Rubric Check — <task id>
Checked <date> · Criteria N (builder minimum 5: ok / short) · Plan <date>
JSON field map: criterion=`<key>` · weight=`<key>` · category=`<key>` · justification=`<key>` · evidence=`<key>`
Readiness for /rubric: FAIL-RISK (<dimensions>) | NON-FAIL-RISK | CLEAN — a prediction only; /rubric gives the verdict

## Coverage
| Plan row | Criteria | Covered / gap |
Unauthorized criteria: <C-n list>

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | Severity |

## Dimensions
| Dimension | Count / % | Threshold | Status |
(Overall Rubric Quality · Criteria Weights · Category Balance · Process Criteria · Agent-Centric Phrasing · Negative Criteria · three fields present)

## Reminders
- An all-Outcome set is normal; Process is not added to look thorough.
- The human fixes criteria in the builder, re-exports, re-runs check, then runs /rubric.
```

## Deliver

Prep: report the path, row counts, Process-candidate results, and blocking items (UGT
defects, infeasible writes, unverified visibility). Next: the human writes every
criterion in the builder in their own words from the plan, exports the JSON to
`task_inputs/09_Rubrics.json`, then runs `/create-rubric-plan check`.

Check: report the path, readiness, the dimension table and the tallies. Next: the human
fixes and re-runs check; then `/rubric` with the criteria JSON, the exact prompt,
assignment + persona, the SQL or "no injection", and reference files (the OEs may be
supplied as a comparison reference). PASS or a scored NON-FAIL proceeds; NON-FAIL with
PARTIAL/BLOCKED does not clear the gate. After the verifier runs: `/create-allfail`.
