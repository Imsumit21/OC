# 01a Hardening Report — jl-zm-difficulty-baseline · round 1

## 1 Mode, inputs and run validity

**MODE B (pre-check).** There is one unhinted Opus 5.5 run and no baseline yet, so this report gives provisional verdicts, a predicted `/hardness` band and a projected average. It has no gate statistics.

Inputs read:
- 00_Assigments.md
- 01_Universe_Inject.sql (before: a58a5d1e61b3; after: 10c1ee9238d4)
- 01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json
- 04_Prompt.txt (22f26066688c, unchanged)
- 03_Error_Async_Config.txt (Friction: none)
- 06_PreCheck_Trajectory/trajectory.json (a copy of task_inputs/Run1_trajectory.json, sha256 ecfae005…, 2,174 events)
- the platform report /home/sumit/Downloads/6adfee3ef9092601a61245bb_1a_hardness.md (FAIL 2, Easy, gate HOLD INSUFFICIENT_DIFFICULTY)

Inputs missing: 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md and 12_Difficulty_Stats.txt (no baseline yet). There are no reference files.

**Run validity (B0)** for run-1:
- **Model:** the main agent and all 11 subagents ran on claude-opus-5-5 (741 tool calls, all claude-opus-5-5).
- **Hints:** none. The run starts cold: profile (event 2), Leonard search (event 4), the DM (event 6), then the card search (event 13).
- **Source match:** the run saw the SQL a58a5d1e61b3 overlay. Its results contain the rule-5 "Copy its Live tab as it stands" text (event 13) and the comment "written out (ATK on its own" (event 16).
- **Completeness:** the run completed with a final reply (event 2171). The second init (event 907) is the same session after background agents, not a new run.
- **Horizon:** 741 calls, 619 of them `linear_list_comments` (415 in subagents). That is far above the author's ≥ 120-call target.

## 2 Gate status, projection and mechanism weight share

There is no baseline, so there are no gate numbers. The projection below uses the weight plan in §11, which is facts and weights only and is to be confirmed at `/create-rubric-writing`.

| Block | Rows · weight | Depends on |
|---|---|---|
| status per kept ticket | 29 × 1 = 29 | — |
| other non-lever rows | 51: replaced-by 3; ZOM-199/254 comments 6; folder 3; Robert, Leonard and Arthur shares 9; two tabs 3; rules tab 5 × 3 = 15; DM place 3; Editor only / Not shipped / Replaced counts 9 | — |
| L1 (thread reply) | 40: 6 exclusions × 3 = 18; total and Live counts 2 × 5 = 10; 12 keys in the reply × 1 = 12 | Leonard's thread reply |
| L2 (checklist) | 39: 12 comments × 3 = 36; Brian as editor 3 | the card's checklist |
| Total | 159 | mechanism weight share 79 / 159 = **50%** |

Projected average = (80 + 40·p1 + 39·p2) / 159, less about 2 points of natural slips. p1 is the rate of opening the thread reply and p2 the rate of opening the checklist.

| p1 / p2 | Projected average | Basis |
|---|---|---|
| 0.30 / 0.45 | ≈ 67% | Hardness_Mastery A14: 67/124 Slack-using runs made zero thread-reply calls. Run-1 made none (it printed ts/user/text only, event 10). The checklist shows only as `badges.checkItems: 2` in the search result (event 13) |
| 0.40 / 0.40 | ≈ 68% | middle case |
| 0.50 / 0.50 | ≈ 73% | upper case, still under 75% |

Other projected gates:
- **SD:** the run outcomes are about 98% (both levers found), about 73–74% (one found) and about 50% (neither), so the SD is ≈ 0.15–0.20.
- **pass@1:** only runs that open both carriers pass (p1·p2 ≈ 0.14–0.25).
- **Failure patterns:** the patterns differ by carrier, so there are ≥ 2 and none is above 50%.

**Clean average:** no CONFOUNDED criterion exists yet (there is no rubric).

## 3 Predicted /hardness band

**Run-1 on the new universe.** The facts from run-1's write payloads are:
- it made no thread-reply call and no checklist call;
- its register (event 2150) has 35 rows, including ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262 and ZOM-275;
- it wrote 2 comments (events 2165, 2167);
- it shared with Brian as commenter (event 2163);
- its DM reply (event 2169) gives counts only.

| Requirement | Result on the hardened universe | Evidence |
|---|---|---|
| R1 membership (29) | MATERIAL_FAIL: 6 extra rows | run-1 · event 2150 |
| R6 reply counts and keys | MATERIAL_FAIL: 35/22 and no keys | run-1 · event 2169 |
| R7 ticket comments (14) | MATERIAL_FAIL: 2 of 14 | run-1 · event 2165, event 2167 |
| R8 shares | MINOR_GAP: Brian commenter, not editor | run-1 · event 2163 |
| R2–R5, R9 | MET | run-1 · event 2150, event 2152, event 2154 |

Predicted band: **4** for a run like run-1. There are two independent root causes (the unopened thread reply and the unopened checklist), and each needs correction across the result: the rows and counts for one, 12 writes for the other. It is not 5, because the core register, folder, rules tab and statuses are correct and usable. It is not 3, because there are two consequential failures, not one bounded one.

A run that opens one carrier lands at **3**. A run that opens both lands at 1–2.

## 4 Designed-difficulty register (verdicts)

Counts are LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED, out of 1 completed run.

| Node | Mechanism / records | Verdict | Counts | Evidence (rollout · step) |
|---|---|---|---|---|
| T1 attack-power amendment | card comment 68dbfa4362a051efb5e0ae45 | LEAKED | 0·0·1·0·0 | run-1 · event 16 read the comment; event 70 regex includes "attack power" |
| T2 window up to Aug 31 | rule 1; ZOM-517 out | LEAKED | 0·0·1·0·0 | run-1 · event 70 filters createdAt ≤ 2025-08-31 |
| T3 ZOM-271 "ATK POWER" | card comment "written out" | LEAKED | 0·0·1·0·0 | run-1 · event 70 whole-word regex; ZOM-271 absent at event 2150 |
| T4 duplicates | ZOM-203, ZOM-276 Duplicate | LEAKED | 0·0·1·0·0 | run-1 · event 2150 omits both |
| T5 ZOM-45 / ZOM-277 scope alias | notes cmt_bed381141007e04f1aac, cmt_b0aa45d307c981ce4487 | LEAKED | 0·0·1·0·0 | run-1 · event 2150: ZOM-45 Live, ZOM-277 Editor only |
| T6 deck ">= 90" | Blake's reply in the thread | LEAKED | 0·0·1·0·0 | run-1 · event 23 gmail_get_thread; event 2152 "> 90" |
| T7 Brian's recap | C090N54TG79/1759185077.402611 | BYPASSED | 0·0·0·1·0 | run-1 never read #zombie-design (no slack channel or search call after event 6) |
| T8 ZOM-282 → #401 → sheet | note, PR comment, sheet | LEAKED | 0·0·1·0·0 | run-1 · event 48 sheet read; event 2152 enrage per monster, hp 0 |
| T9 Next pass tab | sheet tab | LEAKED | 0·0·1·0·0 | run-1 · event 48 read all tabs; event 2152 uses Live |
| T10 ZOM-42 full spec | ZOM-42 description | LEAKED | 0·0·1·0·0 | run-1 · event 359 get_issue ZOM-42; event 2152 both demotion rules |
| T11 deck +25% HP | deck vs sheet | LEAKED | 0·0·1·0·0 | run-1 · event 41 deck; event 48 sheet; event 2152 no HP |
| T12 Domino Delights card | 683dbef4e319167a802bd888 | LEAKED | 0·0·1·0·0 | run-1 · event 13 search returned both cards; it used card 80 |
| T13 invite as share list | evt_91674a9c23d012a9ac34da | LEAKED | 0·0·1·0·0 | run-1 · event 20 attendees; events 2157–2163 shares |
| T14 comment set / no new tickets | rule 6 | LEAKED | 0·0·1·0·0 | run-1 · event 2165, event 2167 only |
| T15 shared PRs #243/#265 | notes + PR files | LEAKED | 0·0·1·0·0 | run-1 · event 2105–2128 PR files; event 2150 ZOM-173/312 Editor only |
| T16 Vincent's channel request | C090N54TG79/1759248760.118527 | BYPASSED | 0·0·0·1·0 | run-1 never read #zombie-design; reply in the DM at event 2169 |
| T17 Domino Delights sheet | f_34f0950581934de1278969 | BYPASSED | 0·0·0·1·0 | run-1 · event 31/32 searches "difficulty"/"enrage" never surfaced it |
| T18 untagged Blake tickets | no "tiers:" | LEAKED | 0·0·1·0·0 | run-1 · event 105 subagent filter on "tiers:"; event 2150 excludes them |
| T19 old iOS build | C08R27X0EAH/1758081917.318539 | BYPASSED | 0·0·0·1·0 | run-1 never read #zombie-bugs; mail at event 23 |
| T20 lives tickets | ZOM-305 tagged, ZOM-352 not | LEAKED | 0·0·1·0·0 | run-1 · event 2150: ZOM-305 in, ZOM-352 out |
| T21 #401 as a replacement | rule 4 record-based | LEAKED | 0·0·1·0·0 | run-1 · event 2150 ZOM-282 Live; event 2167 |
| T22 (new) Leonard's thread reply | D05HB64NMQU/1759262838.442871 | NOT-REACHED (new) | 0·0·0·0·1 | absent from run-1's universe; run-1 · event 10 shows the habit that misses it |
| T23 (new) card checklist | 68dc033bf7d24e86b8a9cc67 | NOT-REACHED (new) | 0·0·0·0·1 | absent from run-1's universe; run-1 · event 13/16 shows the card read path that misses it |

Emergent, not designed: the starting-tier window "first 10 levels" vs the code's 10 games (run-1 · event 2152) was a MINOR_GAP in the platform report. It stays off the rubric (the prompt review and injection advisories).

## 5 Per-rollout ledger (run-1)

| Step | Tool | Input (query / IDs) | What came back | Agent's decision | Requirement |
|---|---|---|---|---|---|
| event 6–10 | slack_read_channel + Bash print | DM D05HB64NMQU | 83 KB of history; the printout kept ts/time/user/text only | read the ask; no thread call | R1, R6 |
| event 13 | trello_search | "difficulty baseline" | card 80 (desc + badges) and the DD card | used card 80 | R1–R9 |
| event 16 | trello_get_comments | card 80 | the attack-power comment | applied it | R1 |
| event 18–23 | gmail search + get_thread | "store builds" | both messages | > 90; editor/debug stripped | R2, R4 |
| event 20 | gcal_search_events | "tuning" | invite, 5 attendees | share list | R8 |
| event 39–48 | gdocs, gslides, gdrive, gsheets | agenda, deck, folder, sheet tabs | rules, layout, enrage | two tabs; Live values | R4, R9 |
| event 56–70 | linear_list_issues ×3 + Bash | ZOM, 500 issues | titles/states | title-word cohort (31 + 4 tagged) | R1 |
| event 105–1224 | 11 subagents, 415 linear_list_comments | candidate batches | only "tiers:" / "replac" / "supersede" matches reported | tagged tickets, ZOM-282's replacing note | R1, R3 |
| event 344 | subagent "Ticket shipping research" | member list + mail rules | statuses | Live / Editor only / Not shipped | R2 |
| event 359–607 | get_issue ZOM-42/303/293/199; code reads | TierManager, WinRateRule, GameLoader | rules in code | rules tab | R4 |
| event 2033–2128 | get_issue ×30; PR files #243/#244/#265/#271 | member descriptions; PR file tables | statuses confirmed | — | R2 |
| event 2146–2169 | writes | sheet, tabs, move, 4 shares, 2 comments, DM | — | — | R1–R9 |

Where it stopped: it never called `slack_read_thread` or `slack_conversations_replies`, `trello_get_card`, `trello_get_checklist` or `trello_get_card_actions`, `github_get_pull_request_comments` or reviews, or any Slack channel other than the DM.

## 6 Friction, tool-defect and horizon checks

- **Friction:** none is configured (03_Error_Async_Config.txt). There are no async or forced errors.
- **Unconfigured tool defects:** event 6 returned 83 KB, saved to a file. The agent read it with python (event 10), so it is not a defect. No errored calls changed an outcome.
- **Horizon:** 741 calls (619 comment reads). After hardening the budget is 161 unconditional calls (01_Hardness_Manifest.json), which is above the ≥ 120 author target.

## 7 Verifier sanity

Not applicable: there is no verifier or rubric yet (`10` is absent).

## 8 Why Opus passed

| Point scored | Mechanism | Class |
|---|---|---|
| Membership, 35 exact | every membership rule sat in the card desc and comment (read at event 13/16) and in notes found by keyword subagents (event 105) | universe leak: the rules sat where Opus reads first |
| All statuses | the notes state the status plainly; the mail lists what is stripped (event 23) | genuine capability plus over-findable notes |
| > 90, enrage, demotion | the thread is opened with get_thread (event 23); the sheet tabs are read in full (event 48); ZOM-42 in full (event 359) | genuine capability |
| Shares, comments, DM | rule 7 + invite (event 20); rule 6 is closed (event 2165/2167) | genuine capability |
| BYPASSED Slack decoys | the run never opened #zombie-design / #zombie-bugs, so Brian's recap and Vincent's request were never met | universe leak: the decoys were off the true path |

## 9 Purge list

- **T7, T16, T19 (Slack decoys):** BYPASSED in run-1. They are kept for realism and coherence: they are base-consistent and cost nothing. They are no longer counted as difficulty, and no weight is planned on them.
- **T17 Domino Delights sheet:** BYPASSED; kept as is.
- **The timing lever proposed by the platform report:** rejected. No member's PR merged after the Sep 26 cut or closed unmerged (match3d PRs #243–#319 all merged 2025-06-25..07-19, github data.json), so seeding one would be a false code claim.

## 10 Candidates and selection (rebuild)

| # | Anchor storyline (cited) | Coupling | Discovery-order proof | Gradable fact | Selected |
|---|---|---|---|---|---|
| 1 | Leonard follows up under his own ask (D05HB64NMQU/1759261706.530914 → reply D05HB64NMQU/1759262838.442871, 2025-09-30T20:07:18Z) | drops 6 rows (ZOM-30, 49, 50, 161, 262, 275) → totals 29 / 16 Live → the reply needs 12 keys | the parent shows reply_count 1; run-1 · event 10 printed text only | 29 rows; 29 / 16 / 9 / 3 / 1; keys 202, 280, 293 + 9 Editor only | yes (A14) |
| 2 | Leonard's "Before Monday" checklist on card 80 (68dc033bf7d24e86b8a9cc67, addChecklistToCard 2025-09-30T16:20:11Z) | rule 6 change → 12 more comments; rule 7 change → Brian edits | the search result shows only badges.checkItems 2 (run-1 · event 13); the items need trello_get_checklist / get_card | 14 comments; Brian writer | yes (A3) |
| 3 | timing: a Done member whose PR merged after the cut | — | — | — | rejected: no such record (§9) |
| 4 | an owner column (Linear assignee) per row | 29 cells | — | — | rejected: 5 members carry a redacted assignee (EMPLOYEE_0032_EMAIL) |
| 5 | Blake's PR comment carrying a status | — | — | — | rejected: any status claim on a PR is a code claim git history can contradict |

**Lazy solver.** One DM read, the card search, its comments, the thread, the sheet and the invite give the register at 35 rows with 2 comments and Brian as commenter. That fails L1 (6 rows, the counts and the keys) and L2 (12 comments, Brian's role).

**A5b check (each node).**
- **Incorporated:** L1 is part of Leonard's ask, which the prompt names ("go through his ask"). L2 is on the card the ask names, and each item says "rule 6 change" / "rule 7 change".
- **Survives complete retrieval:** opening the reply or checklist still needs the rows dropped, the counts recomputed, and 12 comments written.
- **Tool-surface proof:** `slack_read_thread` on D05HB64NMQU/1759261706.530914 and `trello_get_checklist` on 68dc033bf7d24e86b8a9cc67 (both cataloged) return the text.
- **Graded weight:** 50% in the §2 plan.

## 11 Routing

**Universe changes made** (`01_Universe_Inject.sql` a58a5d1e61b3 → 10c1ee9238d4; 158 → 163 INSERTs, 1 UPDATE unchanged):

| Statement(s) | Change |
|---|---|
| slack_messages (S_ASK) | reply_count 1, reply_users_count 1, latest_reply 1759262838.442871 |
| slack_messages (new) | 33c941fae57ba8d1e23bc1dff9ce3e2c: Leonard's reply in the ask's thread (2025-09-30T20:07:18Z), dropping ZOM-30, 49, 50, 161, 262, 275 and asking for the Not shipped and Editor only keys |
| trello_checklists, trello_check_items ×2, trello_actions addChecklistToCard (new) | checklist "Before Monday" 68dc033bf7d24e86b8a9cc67 with "rule 6 change: the Editor only and Not shipped tickets get a comment too…" and "rule 7 change: Brian gets edit as well…"; action 68dc033b328def4251f2a731 at 2025-09-30T16:20:11Z |
| trello_cards (card 80) | dateLastActivity 2025-09-30T16:20:11Z; badges.checkItems 2 |

Checks after the change:
- sql_lint: 0 errors, 19 warnings
- base_check: PASS
- fact_check: PASS
- check-sql: PASS (the thread reply is visible to Julia: DM member)
- hardness_gate (long): PASS
- stage_gate scenario and injection: PASS

**Facts that changed**, for the human, OEs and rubric:
- **Register:** 29 rows. Out: ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262, ZOM-275.
- **Counts:** 29 tickets — 16 Live, 9 Editor only, 3 Not shipped, 1 Replaced (ZOM-254 → ZOM-282).
- **DM reply:** the counts plus the keys. Not shipped: ZOM-202, ZOM-280, ZOM-293. Editor only: ZOM-162, ZOM-163, ZOM-173, ZOM-200, ZOM-201, ZOM-250, ZOM-277, ZOM-312, ZOM-315.
- **Linear comments, 14:** ZOM-199 (> 90), ZOM-254 (replaced by ZOM-282), and one on each of the 9 Editor only and 3 Not shipped tickets saying the change isn't in the store builds.
- **Shares:** Robert and Brian writer; Leonard and Arthur commenter.
- Unchanged: the folder, the two tabs and the rules tab.

**Prompt-side defects:** none. The prompt (22f26066688c) already says "go through his ask and everything it points to", "if his rules say something needs to happen on the tickets, go ahead and do that too" and "reply to leonard in the dm with what he asked for". It stays unchanged.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | — | — | run-1 · event 6–23 read the ask, card and thread the prompt points to |

**Routed observations for `/create-oe-writing` and `/create-rubric-writing`** (facts and weights only, no wording):
- **Weight plan:** keep the §2 plan. Per-ticket status rows at 1. One row per excluded ticket at 3. Total and Live counts at 5. One row per reply key at 1. One row per required comment (14) at 3. One row per share role at 3. Mechanism share ≈ 50%.
- **Keep off:** the "first 10 levels vs games" window, enrage damage stacking, the win-history direction, and values for Mailman, Mayor2 and PartyGirl.

## 12 Self-review

Walked `Evals/1A_Hardness_Eval.md` §3–§5 against this report. There are no LANDED verdicts in run-1. Each LEAKED verdict is counter-read below to check whether the trap was live.

| Verdict | Counter-reading | Resolution (evidence) |
|---|---|---|
| T1 LEAKED | the comment was never in the run's path | live: run-1 · event 16 returned it and event 70 used it |
| T2 LEAKED | the window had no edge case to fail | live: ZOM-517 (created 2025-09-03) exists; event 70 applied ≤ Aug 31 |
| T3 LEAKED | ZOM-271 never surfaced | live: event 70 listed near misses including ZOM-271 |
| T4 LEAKED | duplicates were obvious | live but easy: Linear state Duplicate for ZOM-203 and ZOM-276 is in the list result (run-1 · event 56) |
| T5 LEAKED | the notes handed over the answer | yes, the note is explicit (cmt_b0aa45d307c981ce4487 "nothing changes in the game itself"); this is why L1/L2 were added |
| T6 LEAKED | the thread was not opened | false: event 23 get_thread returned both messages |
| T8 LEAKED | the sheet answered without the chain | yes: event 48 read the Live tab directly; the chain added no difficulty |
| T9 LEAKED | the Next pass tab was not read | false: event 48 requested all three tabs |
| T10 LEAKED | the description was truncated | false: event 359 get_issue returned the full spec |
| T11 LEAKED | the deck was not read | false: event 41 |
| T12 LEAKED | the decoy was not returned | false: event 13 returned both cards (verified: the search result contains 683dbef4e319167a802bd888) |
| T13 LEAKED | the invite was not read | false: event 20 |
| T14 LEAKED | the rule left nothing to get wrong | rule 6 is closed (card 68daca5871dba40417a00383); run-1 · event 2165 / 2167 wrote exactly two, on ZOM-199 and ZOM-254 |
| T15 LEAKED | the notes settled it before the PRs | yes: the notes split the shared PRs; event 2105–2128 only confirmed |
| T18 LEAKED | the subagent filter was given the tag | yes, from rule 1 (event 105 prompt); the tag is a fair, findable rule |
| T20 LEAKED | the lives tickets were not compared | event 2150: ZOM-305 in, ZOM-352 out, as designed |
| T21 LEAKED | rule 4 hands over the answer | rule 4 is record-based by design (prompt round 2); event 2167 |
| T7 / T16 / T19 BYPASSED | the Slack decoys were never live, so they are FALSE, not BYPASSED | they were live (C090N54TG79/1759185077.402611, C090N54TG79/1759248760.118527, C08R27X0EAH/1758081917.318539 exist and are visible to Julia) but off run-1's path (no channel read after event 6); kept for realism, no weight planned (§9) |
| T22 new lever | the thread reply is too easy to see, since the parent shows reply_count | run-1 · event 10 printed only ts/time/user/text from the 83 KB DM dump; Hardness_Mastery A14 (67/124 runs never open replies); estimate p1 0.3–0.5, stated as unresolved |
| T23 new lever | the checklist shows in the search result, so every run opens it | run-1 · event 13 result shows only badges.checkItems and idChecklists (68dc033bf7d24e86b8a9cc67 after hardening); the items need trello_get_checklist; estimate p2 0.4–0.5, stated as unresolved |
| Band 4 (prediction) | argue band 3: only L1 or only L2 would bind | for a run like run-1 (neither carrier opened, events 6–16) both bind, giving two independent root causes; a one-carrier run is 3, as §3 says |
| Band 4 vs 5 | the central result is defeated | no: the register, statuses, folder, rules tab and core shares are correct (event 2150–2163) |

Re-verified through `tools/hg.py` sources and the SQL this run:
- the thread reply row and the parent's reply_count (01_Universe_Inject.sql S_ASK / 33c941fae57ba8d1e23bc1dff9ce3e2c);
- the checklist rows and action (68dc033bf7d24e86b8a9cc67, 68dc033b328def4251f2a731);
- the match3d PR merge dates for #243–#319 (github data.json);
- the 6 dropped tickets' titles (linear data.json);
- the assignees (5 × EMPLOYEE_0032_EMAIL).

Unresolved:
- p1 and p2 are estimates from one run and Hardness_Mastery A14, not measured. The projected average depends on them (§2). The weight plan must be honoured at the rubric stage, or the average rises.

```
STAGE GATE hardening: PASS — Task_Authoring-2/task_inputs · 01a_Hardening_Report.md#56cc0cdf7daa · 01_Universe_Inject.sql#10c1ee9238d4 · 01_Hardness_Manifest.json#774707c53352 · blocking 0 · warnings 0 · checks 14
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#10c1ee9238d4, 01_Hardness_Manifest.json#774707c53352, 01_Grounding_Dossier.md#9a331dcaae22)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 23/23 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 21 evidenced counter-readings (of 22 found; need ≥ 20) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 Next steps

1. Paste the hardened `01_Universe_Inject.sql` (sha256 10c1ee9238d4) into `/injection`.
2. Run `/prompt` with the unchanged `04_Prompt.txt` (the final state changed, so `/prompt` re-checks it).
3. Get a fresh unhinted Opus run, then `/hardness`.
4. Then `/create-oe-writing` and `/create-rubric-writing`, using the §11 facts and weight plan.
