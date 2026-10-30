# Red-team review 2 — independent methodology and fairness review

Reviewer: methodologist-gpt agent (GPT-6.1 Sol, independent read-only session). Artifacts reviewed: `01_Scenario_Design.md`, `01_Hardness_Manifest.draft.json`, `01_Gradable_Surface.json`. Mode: methodology, sampling validity, difficulty arithmetic and fairness. The external review proxy was not configured in this session; this is the second recorded fallback review. See the design's section 13.

## Findings and dispositions

**M1 — MAJOR — the surface bypassed V3 sampling with core labels.** The earlier surface graded twelve statuses, eight decisions, six owners and six feature names, mostly as `core`, which evades the five-samples-per-group rule. Disposition: fixed. The surface now has seven sampled groups, each with at most five samples and a volume row: status 5, decision 4, qualifier 2, owner 5, feature 5, evidence 5, evidence_date 5. The validator passes with 45 slots and weight 91.

**M2 — MAJOR — the summary delivery slot named the wrong channel and did not bind the thread.** Disposition: fixed. The delivery selector is `slack_thread` with the A1 timestamp `1759248600.000100`; the channel is the leadership mpim `C1CB3D58E38B`, which is not archived and has Julia as a member.

**M3 — MAJOR — M8's fix was cosmetic and several mechanism attributions were wrong.** Exact claim keys do not prove workbook reuse; M5 does not change C07; M1/M6 do not change C13's status. Disposition: fixed. M8 is removed from the portfolio and is a rubric delivery row. M5 is removed from C07. C13 is graded as a decision (`QUALIFY`) rather than a status, with M4/M6. M6 is on the C06 conflict and the C13 decision only.

**M4 — MAJOR — authority independence was overstated.** H1 originally stated that internal tooling is out of scope, so H3 was not needed for C11. Disposition: fixed. H1 governs liveness only; H3 governs player-facing scope. The failure-diversity plan now states the clusters: C1/C5 share the Season Pass finding, C2/C3 share the Hero Offers finding, and C4 is independent, so there are three independent discovery clusters, not five.

**M5 — MAJOR — the zero-enablement predicate was still not exhaustive.** The earlier "otherwise LIVE" could admit full enablement without a production surface. Disposition: fixed. The predicate is now: scope, positive subset, 100% plus production surface, otherwise not live. The C10 boundary is explicit: the enabled 48-hour rotation at a 10% cohort is TESTING.

**M6 — MAJOR — the launch-date truth was contradictory and the slot graded status, not date.** The GDD says US 11 April and worldwide 6 May; the readiness document says 23 April. Disposition: fixed. H3 fixes the GDD dates as the external values; the readiness 23 April is a reported conflict; S10 grades the C13 decision (`QUALIFY`) with M4/M6, not the status.

**M7 — MAJOR — the 71-call floor was not an honest necessary-call floor.** Disposition: fixed. The budget is 67 calls; non-spine is 42; Slack is 8/42 (19.0%); the per-record sum is 25 (11 Linear × 2.0 + 2 GitHub × 1.5). The GitHub surface is now only the two contested PR threads, so it is not corroboration padding. The design acknowledges the one Gmail re-read and the write read-backs as clause-check and delivery verification, not difficulty.

**M8 — MODERATE — M1's provenance was overstated.** The ledger record `hev_0e23d0e0b6b029a5` carries an uncertain model-provenance flag and n_eff about 0.86; 0.65 is a weak posterior mean, not a measured six-run mean. Disposition: fixed. The design now discloses both. The forecast remains UNCALIBRATED and is not presented as validation.

**M9 — MODERATE — revisions had not propagated.** Several stale references remained: Win Streak, 1,180/20, the wrong channel, the stale hash and the 76-call pasted block. Disposition: fixed in the current tree. The design, manifest and surface were re-read after the repairs; the role-review hash and the pasted gate block are refreshed in the final run. The level manifest is 4,755 active and 245 planned, matching `page_domino_gdd`.

## Residuals carried to injection

| Residual | Severity | Mitigation |
|---|---|---|
| M-R1 text selectors do not bind the Confluence page or the Linear parent | moderate | the rubric and OE name `page_q4_product_claims` and `ENG-2371`; the register and thread slots are bound |
| M-R2 the forecast is a declared-rule model with six Beta(1,1) priors | moderate | disclosed as UNCALIBRATED; the empirical baseline decides the mode |
| M-R3 both fallback reviewers are GPT-family | low | recorded in section 13 with the proxy reason; no silent skip |

## Difficulty arithmetic check

The reviewer reproduced the 45-slot/91-weight intermediate state (mechanism 61, 67%) and the 0.538 / 0.544 / 0.574 forecast. After the review the author consolidated the five duplicate volume rows into one and added three properly sampled register groups (claim, scope, action) to replace the relabelled padding; the final surface is 55 slots, weight 101, mechanism 61 (60.4%), and the final forecast (hev_8203a6ce967f5047) is 0.584 / 0.589 / 0.617 (independent / source / correlated, P(all gates) 0.309–0.406). The at-risk weight remains enough to fail a run that misses the authorities and the per-record facts; the 62% target sits inside the correlated interval and the independent scenario is 3.6 points under it. The forecast is advisory, not a calibration.

## Verdict

NON-FAIL for the scenario stage's methodology after the repairs, with the residuals carried to `/create-injection` and the rubric. The sampling, predicate, authority separation, budget and prior disclosure now meet the design contract; the remaining risks are grading-surface binding, not universe fairness.
