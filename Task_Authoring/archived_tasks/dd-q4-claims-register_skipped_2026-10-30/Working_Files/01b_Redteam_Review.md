# Red-team review 1 — adversarial falsification of `dd-q4-claims-register`

Reviewer: redteam agent (GPT-6.1 Sol, independent read-only session). Artifacts reviewed: `01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json`, `01_Gradable_Surface.json`. Mode: adversarial; each finding tries to construct a concrete failing case. The external review proxy was not configured in this session, so this file is the first recorded fallback review; see the design's section 13.

## Findings and dispositions

**R1 — BLOCKER — C11 treated Game of Dominoes as another title.** `page_domino_gdd` states that "Game of Dominoes / GoD" is Domino Delights' internal codename. The original C11 ("Win Streak is live") therefore could not be out of scope on a title boundary. Disposition: fixed. C11 is now "the live-ops event engine is live", an internal-tooling claim, and H3 governs player-facing scope. No GoD or Win Streak reference remains in the design or manifest.

**R2 — BLOCKER — the H1 predicate sent zero enablement to TESTING.** "Enabled for less than 100%" is true at zero, so a disabled Season Pass classified as TESTING before reaching NOT_LIVE. Disposition: fixed. The predicate is now ordered and exhaustive: scope first, then a positive subset, then 100% enablement plus a production surface, then otherwise NOT_LIVE.

**R3 — MAJOR — the correction reply stated the classification.** The original K2 said "C06 never went live and C07 is not being built", which hands two answers to a run that opens the thread. Disposition: fixed. K2 now states two raw facts: the production flag is still default-off, and Collectibles has no build slot this quarter. The classification still has to be derived from H1.

**R4 — BLOCKER — T6's Trello card was newer than its correction.** The first eight hex digits of the original id decoded to 2025-09-29, after the September correction. Disposition: fixed. New ids encode their declared activity dates: `68d672304f5e6d7a8b9c0d11` and `68d6735c4f5e6d7a8b9c0d12` (2025-09-26), and `680222a04f5e6d7a8b9c0d13` (2025-04-18). The version order is Apr 18 then Sep 26.

**R5 — MAJOR — M4 and M8 had no graded consequence.** No slot named the wording rule or the reuse rule. Disposition: fixed for M4 (C10 and C09 qualifier slots, plus M4 on the three count decisions); M8 was removed from the portfolio because the surface cannot bind a workbook id, and the reuse requirement is now a rubric delivery row keyed to `f_6b2c3d4e5f60718293a4b5` (residual R1 below).

**R6 — MAJOR — correct content in a new workbook or the Old register could pass.** The decoder reconstructs grids from writes and does not bind the spreadsheet or tab. Disposition: partially fixed. The Old register path writes only nine keys, so the volume check fails. The new-workbook path passes the volume check; the reuse requirement is a delivery row in the rubric, not a surface selector. Recorded as residual.

**R7 — MAJOR — text slots accepted wrong assertions and unrelated destinations.** "LIVE 9" matched "NOT_LIVE 9"; the page and ticket text were not bound to the required object. Disposition: partially fixed. The summary patterns are now `LIVE: 9 claims` and `QUALIFY: 5 claims`; the delivery slot uses `slack_thread` on the claims thread. The page/ticket slots remain text-only; the rubric must grade the page id and the ticket parent. Recorded as residual.

**R8 — MAJOR — a permitted update of the existing ticket could not satisfy the ticket slot.** The decoder reads issue creation only. Disposition: fixed. D4 now requires a new issue under `ENG-2371`, not an update of the parent.

**R9 — MAJOR — the 76-call floor charged avoidable work.** Disposition: fixed. The budget is 67 unconditional calls: 22 Linear (11 issues plus comments), 3 GitHub (the two contested PR threads), and no repeated discovery read. The one Gmail re-read is the clause check; the write read-backs verify delivery.

**R10 — MAJOR — the event-feature count used the wrong unit.** C01–C05 name six event features across five claims. Disposition: fixed. T7 and the design both say six event features across five claims.

**R11 — MAJOR — the Season Pass readiness text was overstated.** The readiness document is a scoped out-of-moves instruction, not proof the pass never shipped. Disposition: fixed. The decisive record is the seeded 2025-09-28 production-config comment plus the empty warehouse; the readiness instruction is corroboration.

## Residuals carried to injection

| Residual | Severity | Mitigation |
|---|---|---|
| R1 workbook identity | moderate | the rubric delivery row names `f_6b2c3d4e5f60718293a4b5` and the Register tab; the prompt pins "the tab we already use" |
| R2 text destination | moderate | the page id (`page_q4_product_claims`) and the ticket parent (`ENG-2371`) are in the OE; the rubric grades them |
| R3 independent-review model | low | both fallback reviewers are GPT-family; the design records the fallback and the reason, and the external proxy is unavailable in this session |

## Verdict

After the fixes, the adversarial case no longer breaks the core classification: the three authorities are separate, the correction reply is factual, the date and count traps are grounded, and the budget is inside the Normal floor. The remaining residuals are grading-surface limitations, not universe or fairness defects. Verdict: NON-FAIL for the scenario stage, conditional on the residuals being carried into the rubric and OE.
