# 09 — Rubric Coverage Plan & Rubric Check (Playbook) — HarmonyGames · Spec V2

> Command: `/create-rubric-plan` (prep) · `/create-rubric-plan check` (check) · Writes: `task_inputs/09_Rubric_Coverage_Plan.md` / `task_inputs/Working_Files/09_Rubric_Check.md` · Paired eval: `/rubric` · Read first: `setup/GEN_EXECUTION.md`

## Purpose

Rubric criteria are human-written in Spec V2: prefill is off and the Criteria Builder
opens empty. The last audit's top defects were incorrect (22%), non-atomic (22%) and
missing coverage (21%), then unauthorized (6%) and overly specific (5%). Rubrics failed
correct answers (44%) more often than they passed wrong ones (29%)
(`Task_Authoring/references/Docs/8_Rubric Writing - V2.md` §10).

The plan targets those defects. It lists everything that must be graded, the final
state that proves it, the values a self-contained criterion must name, the category
decision and the weight band. It never contains the criterion. `check` mode lints the
human's builder export against the plan, the twelve-point checklist and every
`/rubric` check, with `/rubric`'s severities.

## The authorship boundary

- Criteria are human-only (GEN_EXECUTION §2; `8_Rubric Writing - V2.md` §1: "The eval sandbox may be used to query the universe, never to draft criteria").
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
- Rules: `Evals/3_Rubrics_Eval.md` in full (Phases 1–5 and the `hg-strict-overrides-v1` table — stricter than the Docs and applied by `/rubric`); `Evals/references/rules/qc_rubric_v10.md`, `coherent_record.md`, `rubric_sampling.md`, `rubric_factual_checks.md`; `rubric_qc_examples.md` and `rubric_qc_cases.json` (historical calibration, not policy); Docs in `references/Docs/`: `8_Rubric Writing - V2.md`, `7_Oracle Events V2.md` §8, `10_Long Horizon Guidelines - V2.md` §9, `9_Common Errors & Pre-QC - V2.md` §8, `4_Persona ACL Policy - V2.md` §5 and §9, `QC_Spec_Doc_Latest.csv` (Rubrics rows); `references/Taxonomy_V2_Step_Map.md` step 51 (builder: minimum 5 criteria); `Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` (the ML-selected example task).
- **Where sources disagree the strictest governs (GEN_EXECUTION §3), and these Docs statements are superseded:** Rubric Writing §3/§12 and Common Errors §8.2 "Process > 50% fails" (removed in QC Spec V2 and the Evals override — only zero Outcome fails); Rubric Writing §4/§12 and QC Spec V2 "negative allowed when the prompt prohibits" (Evals: prohibition-only always fails); Rubric Writing §5 axis-count weights (work-kind weights apply); ACL Policy §9 "restriction never shown = Moderate" (Evals `unauthorized` = Major); QC "self-containment may use the prompt and sibling criteria" (Evals: title-only).

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
6. **Atomic, no duplicates.** One verifiable claim per row. Split independently variable contents of one artifact; never pair a factual claim with a formatting claim. Keep together only what `coherent_record.md` allows: coupled attributes of one record, components of one evidenced tool output, the same content of one message sent to several people, a send with the content that defines it, the qualifiers and operands of one metric or comparison. Each fact is graded once, where it matters most.
7. **Four prohibitions** (`8_Rubric Writing - V2.md` §6). No unstated expectations. No single conclusion on ambiguous evidence unless a careful human reading reaches the same answer. Grade how a distractor is handled, not its disclosure. No hard-coded titles or phrasings the prompt did not specify. Under the Evals overrides, a **prohibition-only or absence-only** acceptance always fails Negative Criteria — record each exclusion as a preserved state or scope boundary on its own row.
8. **Weight by the kind of work** (QC Spec V2 "Criteria Weights", applied by the Evals override): 1 = direct lookup or literal check from one source; 3 = interpretation, calculation, comparison or limited reconciliation; 5 = multi-source reconciliation, deeper reasoning, cross-modal evidence or tracing. Record the kind and its reason per row. Only 1/3/5. Essential-and-easy is still 1.
9. **Passable.** Every write row cites a feasible ledger write. No row depends on evidence outside the persona's view, requires describing a restriction the agent only saw as "not found", expects a successful retry on a rate-1.0 tool, or grades recovery as a non-action.
10. **One destination.** If two valid routes end in different final states, stop: that is a Unique Ground Truth defect in the prompt (`8_Rubric Writing - V2.md` §9; `references/Docs/QC_Spec_Doc_Latest.csv`), not a rubric problem. Where routes differ but the destination is the same, mark the row "phrase broadly"; never enumerate branches.
11. **Evals overrides** (`Evals/3_Rubrics_Eval.md`). Self-containment is **title-only** — the values a row lists must all be nameable in the title; the prompt, sibling titles, justification and evidence supply none. No ranking word (`primary`, `main`, `chief`, `principal`, `leading`, `mainly`, `largely`, `generally`, `overall`) that admits what it outranks — record the exclusion as a value. Multi-recipient content is planned per recipient unless one message to everyone is the graded artifact. Rows that would all fail on one agent error because each embeds the same acceptance condition form one cascading-overlap group — note each group (a write row and its own content row never form one). **Predicted all-fail:** mark any row whose values the persona cannot reach, on one of the four Evals bases — `target_data_absent`, `required_tool_absent`, `filter_impossible`, `entity_unreachable`; two or more fail the rubric before any run. Over-specific acceptance is a separate risk (it fails correct runs and becomes an invalid all-fail after the verifier): note it in A2, not as predicted all-fail.
12. **Failure diversity.** Map each independent chain, hidden authority and trap requirement from the manifest to the row(s) it decides. No single discovery may decide more than half of the total weight; independent chains land on different rows, so failing runs differ on ≥ 2 rubric results (the failure-pattern gate).

## Procedure — prep mode (checklist)

- [ ] Read GEN_EXECUTION, this playbook, `8_Rubric Writing - V2.md` and `7_Oracle Events V2.md` §8. Load inputs; stop per gate 1.
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
- [ ] Fill the summary (section E), run the Self-review (prep), self-scan for criterion text (gate 2), write the plan.

## Plan template

Write exactly these headings and columns.

```text
# 09 Rubric Coverage Plan — <task id>
Generated <date> · Clock 2026-02-14T00:00:00Z · Persona <name> <email> · Tier <…> · Human time <h> · OE status: /oe PASS <date> | PROVISIONAL

## A · Coverage matrix
| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs; exact / tolerance) |

## A2 · Grading risks and weight
| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |

## B · OE trace
| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |

## C · Process candidates — three-condition test
| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |

## D · Spot-check groups
| G | Item set (F-IDs, total N) | Sampled items (≤ 5) and why hard/edge | Volume row | Core requirement? (must be no) |

## E · Summary
Rows N · Outcome N · Process candidates N — ≥ 1 Outcome ☐ (no Process ratio: QC Spec V2 and the Evals override fail only zero Outcome) · builder minimum 5 ☐ · one volume row per spot-check group ☐ · predicted all-fail rows ≤ 1 ☐
Failure diversity: largest single-discovery share of weight N% (≤ 50% ☐) · chains landing on distinct rows ☐
Bands: 5 ×N · 3 ×N · 1 ×N
Set size: N rows for <h> h (reference: 31 criteria for a ~10-hour task; ~60 signals duplicate grading, ~12 missing coverage)
Coverage: requirements N/N · OEs N/N · writes N/N · told facts N/N · friction N/N
Four prohibitions: ☐ unstated expectations ☐ conclusions on ambiguous evidence ☐ grading the distractor ☐ hard-coded titles/phrasings
Blocking: <UGT defects · infeasible writes · unverified visibility>
```

## Procedure — check mode (checklist)

Walk the checks in `/rubric`'s order (`Evals/3_Rubrics_Eval.md` Phases 1–5). For every row
record: requirement → title predicate → valid alternative → plausible near miss → finding.

- [ ] **Intake (schema gate).** Load `09_Rubrics.json` and the plan; stop if either is missing. Edit neither. If the JSON does not parse (a hand copy often double-escapes or leaves inner quotes unescaped), report the line and column, readiness FAIL-RISK (schema), and stop — the human re-exports from the builder; never repair the file. Record the key map (criterion/title, weight, category, justification, evidence). Every row needs all five non-blank; category `Outcome` or `Process` (letter case is cosmetic — note it); weight an integer 1, 3 or 5. A blank field or invalid value fails the schema gate.
- [ ] Number criteria C1…Cn in file order. The denominator is the authored count; fewer than 5 breaks the builder minimum (taxonomy step 51).
- [ ] **Coverage (hard gate; Eval 1.4, 3.1).** Build the requirement list from the prompt and what it clearly incorporates, then check it against the plan (an unmentioned handbook adds nothing). A requirement is covered only when a title predicate rejects **both** its omission and a plausible wrong result on the **correct artifact**; topic similarity, a heading mention or a justification is not coverage. Check in particular: every write the prompt assigns to the Agent has a result row and its prompt-set content (a content row that requires the write covers both); every fact or verdict the user asked to be told has a final-response row (rows on a post or record do not cover the reply, and vice versa); a determination ask has a row on the verdict itself; both halves of a compound ask; a required exclusion or decoy has a row rejecting the all-inclusive answer; a draft does not satisfy a send, nor a note a requested status change. Each missing outcome is one `missing_coverage` entry (numerator only). A write row for an action the prompt leaves to the user ("I'll post it") is `unauthorized`. An OE result the prompt never asked for is an OE defect, not a gap.
- [ ] **Per-row lint.** Assign each finding its `/rubric` type (severity table below):
  - *Self-containment, title-only (2.1).* Hide everything but the title: every acceptance-bearing ID, value, status, destination, recipient and finding must be there. Flag "that message", "the designated channel", "the right person", "the correct figure", catch-alls that extend a named set of entities, values or routes ("or another account", "relevant vendors", "via email, Slack or similar") — and a catch-all route that admits a wrong completion (a draft for a send) is also `overly_broad`. "(or similar)" / "or equivalent" qualifying a meaning the title states in full ("confirms the lease is closed (or similar)") is a paraphrase allowance (2.10), not a defect. A title that names the topic but not the finding ("mentions the billing status for X") does not name its answer. A supporting field that **widens** acceptance → `not_self_contained`; one that **narrows** it → `overly_specific` if it changes grading, else `harmless_specificity`.
  - *Atomicity (2.2) — decompose every row.* Two or more claims that can pass or fail separately → `non_atomic`, including `at least N`, `any one of`, `X and Y` over independently required items, a filtered list ("A, B and C are done"), and a verdict bundled with its grounding. Apply the exceptions **first** (`coherent_record.md`): attributes of one record (a PR and its own merge date), components of one evidenced tool output, the same content of **one** message sent to several people, a send plus the content that defines it, qualifiers and operands of one metric or comparison, premises of one causal finding. Content "delivered to both X and Y" when separate sends are accepted is `non_atomic` (and a cascade group if repeated). A disjunctive title is `non_atomic` when both branches are required, `overly_broad` when the "or" admits a wrong alternative. An "or" over a complete closed set of valid alternatives (two accepted channels, two accepted spellings) is valid flexibility, not a defect.
  - *Correctness and verifiability (2.3–2.4; `rubric_factual_checks.md`).* Re-read every literal through `hg.py` and the injection SQL (know which layer each value belongs to). `incorrect`: contradicts the records, the SQL or the clock; a literal found nowhere; an impossible derivation or imported qualifier; persona-scope error ("my projects" given an entity total); role overreach; a mandated write that an accessible human decision defers. `unobservable`: the value is not reachable at the required precision through cataloged tools, or only another persona can see the evidence, or passing depends on hidden tool returns. A count needs the complete candidate set; an absence claim needs a positive control. Unverifiable without SQL or source → UNRESOLVED, never a guessed defect.
  - *Objectivity and ranking (2.5).* `enough`, `professional`, `thorough`, `appropriate`, `comprehensive`, `sufficient`, `reasonable`, `adequate`, `properly`, `correctly`, `accurately` in place of a concrete target → the row does not name its answer (`not_self_contained`). Ranking words (list in gate 11) → `not_self_contained` (Major) when only a supporting field states the exclusion, else `overly_broad`.
  - *Specificity (2.7; anti-rationalization).* A valid prompt-authorized alternative the row rejects → `overly_specific`: channel or method lock-in where the prompt said "notify/reach out", content chained to a locked channel, a structured value the catalog does not require, a hard-coded title, heading or phrasing, a forced single conclusion on ambiguous evidence. Never excuse it as "the likely route". **Overly-broad test on every row in isolation:** a plausible wrong answer passes → `overly_broad`; never argue a sibling row catches it; very unlikely wrong paths are not flagged.
  - *Vague exemplar (2.7A).* `such as`, `e.g.`, `for example` in **any** field → `vague_exemplar` once per row (inside a verified immutable name: UNRESOLVED).
  - *What not to grade (2.8).* Unstated expectation or graded distractor → `unauthorized`; same fact graded again elsewhere → `duplicate`.
  - *Agent-centric and negative (2.9).* Subject an artifact or model ("The response states…", "The write-up…") or a catalog tool identifier in the **title** → `non_agent_centric` (Major) and the Agent-Centric dimension fails. "The Agent's report states…" and bare "Reports…" are valid nonstandard forms: dimension NON-FAIL, no tally issue. A tool name only in justification/evidence is a note (Docs say "anywhere"; `/rubric` permits it to locate evidence). Lexical pre-scan of every title: `does not`, `do not`, `must not`, `makes no`, `has no`, `no`, `not`, `never`, `without`, `avoid`, `refrain`, `fail to`. Prohibition-only or absence-only acceptance fails Negative Criteria even when the prompt prohibits the action; a positive second clause does not cure it; a reported negative fact ("reports that PR #438 had no review") is affirmative. The exclusion still needs its own row.
  - *Category (2.6, 3.2).* A write or observable result labeled Process, or a Process row a stricter Outcome could capture → `category`. Record which of the three conditions each Process row fails.
  - *Clock (2.11)* 2026-02-14T00:00Z: nothing on or after it has happened. *Weight (2.12):* expected weight by work kind (1/3/5) for the atomic result, against the plan band; record one-level vs two-level misses. A bundled row needs splitting, not a higher weight.
- [ ] **Set-level (3.3–3.7).** Duplicates: wholly redundant row → `duplicate` per row; overlapping rows and cascading-failure rows → one `OVERLAP_GROUP` per shared condition, counted once after removing members already Major, no intersecting groups. A cascade group needs one embedded acceptance condition (the same recipient pair, the same wrong premise) — rows that merely share a likely root cause (one miscalculated value that each prompt-required deliverable must carry), or that fail only because their own artifact was never created, are not a group. Not duplicates: a write row and its content row; the same fact in two prompt-specified deliverables (a document **and** the reply, when the prompt asks for both); an aggregate control and its spot checks. Spot checks (`rubric_sampling.md`): repetitive items of equal importance only; > 5 samples in a group → one overlap group; no volume row for a sampled output → `missing_coverage`; a sampled core requirement → `missing_coverage` for the unsampled part; a weak sample choice is a note. Contradictions: rows (and each row's three fields) must be jointly satisfiable; a proven contradiction fails that repair gate — record the source-wrong row as `incorrect`. Mutation test: a complete valid solution (including correct delivery plus a concise reply) must pass every row; change one value, recipient, status or output at a time and name the row that rejects it — an unrejected change is a coverage or broadness finding.
- [ ] **Predicted all-fail (5.1).** From defects already recorded, list rows that would fail every run on a basis of `target_data_absent`, `required_tool_absent`, `filter_impossible` or `entity_unreachable` (includes a successful retry on a rate-1.0 tool and evidence outside the persona's view). Two or more → FAIL.
- [ ] **Tally and dimensions.** Count each row once at its highest severity; overlap groups once; missing outcomes in the numerator only. Apply the dimension table; give the threshold margin when the set is small (with 11 rows one Major is 9.1%).
- [ ] Run the Self-review (check), then write the report. No replacement wording anywhere.

Severity — the `/rubric` issue types (`3_Rubrics_Eval.md` taxonomy + `hg-strict-overrides-v1`; `qc_rubric_v10.md`). `/rubric` decides; this is a prediction.

| `/rubric` type | Severity | Covers |
|---|---|---|
| `missing_coverage` | Major, one per missing outcome, numerator only | Uncovered authorized requirement or wrong artifact; missing volume row for a sampled output; sampled core requirement |
| `not_self_contained` | Major | Title alone does not name the answer; catch-all; vague reference; subjective word in place of a target; supporting field widens acceptance; ranking word whose exclusion sits only in a supporting field |
| `non_atomic` | Major | Independent results outside the documented exceptions; `at least N` / any-one; disjunction of required items; multi-recipient content when sends are graded separately |
| `incorrect` | Major | Contradicts records / SQL / clock; fabricated literal; impossible derivation; persona scope; role overreach; deferred mandated write; source-wrong side of a contradiction |
| `unauthorized` | Major | Unstated expectation; user-owned action; graded distractor; unmentioned handbook rule; requires describing a restriction only seen as "not found" (ACL Policy §9 says Moderate — strictest governs) |
| `unobservable` | Major | Precision or evidence the persona's tools cannot reach; hidden tool returns |
| `non_agent_centric` | Major + Agent-Centric FAIL | Artifact/model subject or tool name in the title |
| `overly_specific` | Major | Rejects a valid prompt-authorized answer (lock-ins, hard-coded title/phrasing, forced conclusion, narrowing supporting field) |
| `overly_broad` | Moderate | A plausible wrong answer passes; ranking word otherwise; "or" admitting a wrong branch |
| `duplicate` | Moderate | Wholly redundant row (per row); overlap / cascading-failure / > 5-sample group (once per group) |
| `category` | Moderate | Write or observable result labeled Process; Process row an Outcome could capture |
| `vague_exemplar` | Moderate | `such as` / `e.g.` / `for example` in any field, once per row |
| `harmless_specificity` | Minor | Wording preference that rejects no valid answer |
| — (not tallied) | dimension or note | Prohibition-only title (Negative FAIL); nonstandard Agent form (Agent-Centric NON-FAIL); missing Process for a real ordering dependency (Process NON-FAIL); typo the judge still reads correctly; tool name only in a supporting field |

| Dimension (QC Spec V2 + Evals) | FAIL (1–2) | NON-FAIL (3–4) | PASS (5) |
|---|---|---|---|
| Overall Rubric Quality | Major > 10%, or Major+Moderate > 15%, or all > 20% of authored rows | Within all three but any Major/Moderate, or Minor ≥ 5% | No Major/Moderate, Minor < 5% |
| Criteria Weights | ≥ 15% off by two levels or ≥ 30% off by one | Any smaller disagreement | All match |
| Category Balance | Zero Outcome rows (no Process ratio) | — | ≥ 1 Outcome |
| Process Rubrics | 2+ invalid Process rows | Exactly 1 invalid, or a missing Process for a genuine sequential/causal dependency | Any Process rows valid |
| Agent-Centric Phrasing | 1+ artifact/model subject or tool name in a title | Valid possessive or bare action form | Standard Agent + action |
| Negative Criteria | 1+ prohibition-only / absence-only title, even with prompt authority | — | All affirmative |
| Predicted all-fail gate | 2+ rows on the four bases | (1 row: report) | 0 |
| Repair gates (no score) | Schema, self-containment, accuracy, atomicity, coverage, duplicates, weights, contradiction — a failure is reported; its tally issue carries the score | | |

Readiness: **FAIL-RISK** if any dimension or the schema gate fails · **NON-FAIL-RISK** if any is NON-FAIL or a required fact is UNRESOLVED · **CLEAN** if all PASS. The lowest dimension controls `/rubric`'s verdict.

## Self-review (GEN_EXECUTION §6a — this stage)

Run before saving either output; record it under **Self-review** in that output. It may quote and judge criteria; it never proposes wording.

Prep mode:
1. **Re-read as `/rubric`.** Walk `3_Rubrics_Eval.md` 1.4 and 3.1 against the plan: every prompt requirement, write, told fact, verdict, exclusion and friction has a row on the correct artifact.
2. **Counter-readings per row.** (a) Could a valid answer fail a criterion that names exactly these values — another channel, route, format, rounding, or a second reasonable conclusion? Resolve with evidence: mark "phrase broadly", add a tolerance, or record the ambiguity risk. (b) Could a wrong answer pass — the all-inclusive answer, the runner-up, the decoy, the stale value? Resolve by listing the excluding value or a separate exclusion row.
3. **Re-verify every value** the plan lists through `tools/hg.py` (and the SQL for injected values): record the command and pointer. A ledger value is a lead, not evidence.
4. **Predicted all-fail re-check.** For each row: the persona can reach the value through a cataloged tool at the stated precision, the write exists in the catalog, no rate-1.0 retry, no evidence outside the persona's view. Count rows on the four bases (≤ 1).
5. **No criterion text.** Scan every cell: nothing begins with "Agent", "The Agent" or "Agent's"; no agent-subject sentence; no quoted candidate title; no "should say". Rows stay noun phrases plus values.

Check mode:
1. **Re-read as `/rubric`** in phase order; apply the pre-verdict sweep (5.0): one missing requirement, one phrasing mismatch with the prompt, one non-atomic row, one category mislabel, one over-specific or hard-coded title, one duplicate or cascade group, one vague exemplar, one prohibition-only title.
2. **Counter-reading per finding** (false positive?): a documented atomicity exception, a descriptive negation, a valid possessive, permitted sampling, an immutable source name, a value the title does name. **Counter-reading per cleared row** (false negative?): try a valid alternative and a plausible near miss against the title alone. Resolve each with a rule § or record pointer.
3. **Re-verify** through `hg.py` every value a finding or a clearance depends on.
4. **Recount** predicted all-fail from recorded defects only, then the tally from the findings table (highest severity once, overlap groups once after removing Major members, missing outcomes in the numerator only).
5. **Boundary.** The report contains quotes, rules, defects and plan rows only — no "rewrite as", no alternative title, no split or merge proposal.

Record: `| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |`

## Check report template

```text
# 09 Rubric Check — <task id>
Checked <date> · Criteria N (builder minimum 5: ok / short) · Plan <date>
JSON field map: criterion=`<key>` · weight=`<key>` · category=`<key>` · justification=`<key>` · evidence=`<key>` · schema gate: pass / fail (<defect>)
Readiness for /rubric: FAIL-RISK (<dimensions>) | NON-FAIL-RISK | CLEAN — a prediction only; /rubric gives the verdict

## Coverage
| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |
Unauthorized criteria: <C-n list>

## Findings
| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |

## Overlap groups · Spot-check groups · Predicted all-fail
| Group / row | Members / basis | Shared condition / reason |

## Dimensions
| Dimension | Count / % | Threshold | Status |
(Overall Rubric Quality · Criteria Weights · Category Balance · Process Rubrics · Agent-Centric Phrasing · Negative Criteria · Predicted all-fail · schema and other repair gates) · threshold margin

## Self-review
| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |

## Reminders
- An all-Outcome set is normal; Process is not added to look thorough.
- The human fixes criteria in the builder, re-exports, re-runs check, then runs /rubric.
```

## Deliver

Prep: report the path, row counts, Process-candidate results, and blocking items (UGT
defects, infeasible writes, unverified visibility). Next: the human writes every
criterion in the builder in their own words from the plan, exports the JSON to
`task_inputs/09_Rubrics.json`, then runs `/create-rubric-plan check`.

Check: report the path, readiness, the dimension table, the tallies and the self-review. Next: the human
fixes and re-runs check; then `/rubric` with the criteria JSON, the exact prompt,
assignment + persona, the SQL or "no injection", and reference files (the OEs may be
supplied as a comparison reference). PASS or a scored NON-FAIL proceeds; NON-FAIL with
PARTIAL/BLOCKED does not clear the gate. After the verifier runs: `/create-allfail`.
