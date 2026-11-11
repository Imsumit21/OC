# Lessons from completed tasks for the S2 rev6 to rev7 decision

Written 2026-11-08. Read-only review of platform reports, READMEs, learnings, the hardness guides, the measured habits file and memory notes. I did not read the task_inputsS2 trajectory or its rev6 /hardness report. What rev6 did is taken from the caller's summary.

## How to read this

Tags: **[E]** = stated in a cited file or computed from one. **[I]** = my inference from that evidence. A single pre-check run is one observation, not a rate (V2:13).

Path aliases. CT = `Task_Authoring/support/completed_tasks`. ER = that task's `eval_reports/`.

| Alias | Path |
|---|---|
| LLC | CT/robert_llc_takeover_2026-11-06 |
| WD | CT/robert_winddown_closeout_2026-10-30 |
| Q4 | CT/frederick_q4_commitments_2026-11-05 |
| VN | CT/vincent_zm3d_release_gate_2026-11-06 (report prefix `6ae9909f7b5249d3148f3707_` dropped) |
| BR | CT/frederick_bridge_pipeline_2026-11-03 |
| JL | CT/julia_zm_difficulty_baseline_2026-11-01 |
| DG | CT/douglas_beta_server_signoff_2026-10-28 (report prefix `6ad90ea979eb9e5d89f8879f_` dropped) |
| CL | CT/claire_zm3d_halloween_art_plan_2026-11-07 |
| CS | CT/frederick_card_spend_q3_6ad83eebbd6456fd065bbd20 |
| HO | CT/frederick_account_handover_2026-10-26 |
| JC | CT/julia_zm3d_beta_calendar_2026-11-07 |
| V2 | Task_Authoring/references/Docs/13_Hardness_v2_Opus55.md |
| HM | Task_Authoring/references/Hardness_Mastery.md |
| FPG | Task_Authoring/Audit_2026-11-08_Hardness_Guide/Failure_Pattern_Guide_From_Screenshots.md |
| CF | Task_Authoring/Audit_2026-11-08_Hardness_Guide/Combined_Findings.md |
| A06 | Task_Authoring/Audit_2026-11-06_Pipeline_Iterations |
| SC4 | Task_Authoring/task_inputsS2/Working_Files/plan/research/sc4_habits.md |
| LRN | root `learnings` |
| MEM:x | `~/.claude/projects/-Users-sumit-Source-OC/memory/x.md` |
| KDI | Task_Authoring/references/known_data_issues/normal.md |

Row pass rates and weight shares marked "recomputed" are mine, from each task's `task_inputs/Working_Files/12_difficulty_input.json` (LLC from `task_inputs/10_Baseline_Verifier_Results.md` plus `09_Rubrics.json`, which reproduces LLC README:40-41 exactly). Script and output: `/private/tmp/claude-501/-Users-sumit-Source-OC/bdfc97aa-4237-48cb-813b-efb76f52ae54/scratchpad/rows.py` and `rows.out`.

## Five findings that matter most

1. **[E] Every move from band 1-2 to 3 or more came with a deciding fact moved off the run's swept path. In LLC, Q4, CL, VN and JL the prompt was byte-identical across that move (BR's first move also changed the job).** Adding rules or volume never moved a band (section 1).
2. **[E] A band says little about the average.** LLC band 5 gave 83.6%, WD band 3 gave 85.7%, Q4 band 4 gave 71.0%, DG band 4 gave 56.3% (section 1 end).
3. **[E] Seen means used.** In 16 traced traps, 35 of 35 runs that had the record's text passed the trap. Misses were retrieval misses (SC4:180). Judgment traps almost never cost points (JL README:25).
4. **[E] Hiding too well gives a low average and a flat SD.** Q4 and CL show it (section 4). Spread needs heavy traps caught by a third to two thirds of runs (FPG:70).
5. **[E] Most /prompt failures after hardening came from the new or moved records themselves:** a new fork, or a claim the base contradicts (section 3).

## 1. What moved /hardness

"Universe" = SQL only. Band is the platform score.

| Task (mode, competency) | Before | What changed | After | File pointers |
|---|---|---|---|---|
| **LLC** (Easy, Finance) | Platform SQL rev 6: band 2. One cause (Apple App Review email listed, never opened), about 96% right, and the miss changed wording only | Universe only; prompt same sha (README:25). Proposed RB1-RB5. SQL diff rev3 to rev4 confirms: CF stacks $62 taken off the ENG-2445 comment (now a stale $95) and put in Arthur's "jenkins" email; layer.ai art note taken off ENG-2454 and put in Leonard's #prototype thread reply; project text reworded so ENG-2462 flips Done vs Todo | Platform rev 9: **band 5**, 157 calls. VO $3,000 missed (central total wrong by 87%) plus ENG-2462 now a status miss | ER/1a_hardness_FAIL_r1.md:37,52,71,73,79-81; `task_inputs/Working_Files/01a_Hardening_Report.md` s10 (lines 200-236); `run_forensics/rev3` vs `rev4` SQL; ER/1a_hardness_PASS_r2.md:35,39,76 |
| **Q4** (Easy, Corp Ops) | Rev 5: band 2. Only Nintendo missed, 95% right. Traps "all linked from Leonard's email or in obvious places" | Universe only. M1-M4: correction text de-named (contact and offer, no company name); answer moved to a thread under an unrelated root; one note de-named and calendar carrier removed; Hootline moved before the listing window | Rev 8: **band 4**, 5 independent causes, about 17% failed, 231 calls | ER/1a_hardness_FAIL_r1.md:85,125-133; `Working_Files/01a_Hardening_Report.md`:143-146; ER/1a_hardness_NONFAIL_r2.md:10,72-87,91,155 |
| **VN** (Easy, Eng Ops) | Rev 11: band 1, no miss. "Most deciding records sit where a thorough agent already looks"; each re-check on its own ticket; How-we-gate spelled every value | Universe only, no prompt change. R1 missing piece put in an inline PR review; R3a Brian's Sep 29 DM naming two tickets; R3b ZOM-293 symptom only in the reporter's July comment | Rev 18: **band 4**, 3 causes, about 14% failed, 122 calls | ER/1a_hardness.md:109-117,127; `Working_Files/01a_Hardening_Report.md`:177-240; ER/1a_hardness-4.md:62-83,158 |
| **CL** (Medium) | Rev 2: band 2, 58 of 58 ad calls right, six rules LEAKED | Universe only (prompt byte-identical). Six carriers moved off the swept path: a thread reply, a leave post, a mail, a Trello comment on another card | Rev 3: **band 4**, 8 causes, about 38% failed | ER/1a_hardness_FAIL_r1.md:10,19; `Working_Files/01a_Hardening_Report.md`:137-160; ER/1a_hardness_NONFAIL_r2.md:10,19,85,91 |
| **DG** (Medium) | Rev 7: band 3, one cause (Arthur's mail never fetched) | Later additions spread over a mail reply, a DM thread and a Confluence comment (records named in the report; the exact edit list is not in the report) | Rev 10: **band 4**, three independent retrieval misses | ER/1a_hardness.md:122; ER/1a_hardness (1).md:59-72,106 |
| **BR** (Medium) | Rev 9: band 1. "One read hands Opus the whole rulebook" (Oct 14 template); corrections in channels the run paged | Rev 14: the prompt also changed (sha differs; the job became the Q4 send list, README:31). Rules split; SciPlay pass moved to an #executives thread reply; Arthur's correction moved to #zombie-match3d, overriding ZOM-567 | **Rev 14 band 4** | ER/1a_hardness_FAIL_r1.md:118-136; `Working_Files/01a_Hardening_Report.md` s4 and s8; ER/1a_hardness_NONFAIL_r2.md s4 |
| BR, next | Rev 14 band 4 | Rev 17: about 50 routine Trello writes added; Arthur's post was top-level and used the words "tester" and "testflight" | **Rev 17 band 1.** Same traps, all found | ER/1a_hardness_FAIL_r3.md:105,111 |
| BR, next | Rev 17 band 1 | Rev 20: correction became a thread reply without the keywords. Rev 23 and rev 26: placement tuned | **Bands 3, 3, 3.** One trap per run, a different trap by run | ER/1a_hardness_NONFAIL_r4.md:132; ER/1a_hardness_NONFAIL_r6.md:145 |
| **JL** (Medium) | Rev 14, 17, 22: bands 2, 2, 2 at 741, 222 and 836 calls | Added checklist, DM layers and rule wording, all readable. Reviewer: difficulty must come "from facts the Agent has to establish rather than read" | Unmoved | ER/1a_hardness_FAIL_r3.md s8; A06/02_Completed_Tasks_Evidence.md:30 |
| JL, next | Band 2 | Prompt unchanged. Rev 25 added a notes doc and a PR review; rev 42 moved Blake's reply into its own thread. Runs solved those new layers and missed older DM thread replies, because their own parser dropped `reply_count` | Bands 3, 4, 3, 3 (rev 25, 42, 45, 48). Still one choke point | ER/1a_hardness_NONFAIL_r4.md s4-5; ER/1a_hardness_NONFAIL_r5.md s4-5,7; JL README:27 |

Tasks where it did not move or was not re-run:

- **WD (Easy):** one round, band 3 on rev 13. Causes: unpaged #winddown history and a GitHub bot notice no run looked at (ER/1a_hardness.md:62-73,105).
- **CS (Medium, Finance):** band 3, no round history (README:8).
- **HO:** no reports stored.
- **JC:** never reached /hardness (README:7).
- Other tasks that came back too easy: robert-vendor-schedule rev 6 (LRN:253,270-274), dd-2024 rev 1 (LRN:459,464-477) and dd-2025 rev 6 (LRN:582-591).

**[E] What failed, repeatedly.** Rules on the delegation path (BR r1:118-126; LLC r1:79). A correction in the same container or returned by a bulk call (LRN:270-274, 466-470). A correction that reuses the words the pointer sends the run to search (BR r3:111). Extra readable rule layers (JL r3 s8). Routine writes (BR r3:105).

**Band vs baseline.** [E]

| Task | Final band | Baseline avg | SD |
|---|---|---|---|
| LLC | 5 | 83.6 | .103 |
| Q4 | 4 | 71.0 | .016 |
| VN | 4 | 78.3 | .049 |
| DG | 4 | 56.3 | .117 |
| CL | 4 | 60.6 (local proxy only) | .025 (proxy) |
| WD | 3 | 85.7 | .034 |
| BR | 3 | 77.7 | .106 |
| JL | 3 | 83.8 | .099 |

Sources: each README. [I] A band tells you the run failed materially. It does not predict average or spread, and the rubric's final granularity moves both (LLC README:79).

## 2. Which trap types have cost Opus 5.5 points

The nine-trap order in V2:22-79 comes from 46 outside tasks that scored under 75%. The table below is our own archive. The order is my inference from rows lost and catch rates. Catch rates are from SC4:154-178 or recomputed.

| Rank | Trap type | Finance (LLC, CS) | Easy, not Finance (WD, Q4, VN) | Medium (BR, DG, JL, CL) |
|---|---|---|---|---|
| 1 | Off-path correction or hidden input that changes a total or a decision (V2 traps 2, 8) | LLC VO $3,000 1/6, 14 rows fail together (README:78). layer.ai 1/6. CS Webflow, Murf 0/6; WeWork 1/6; Sensor Tower thread reply 4/6; CF stacks $62 5/6 | VN Brian's DM 1/6 on ZOM-458/473/535; WD Unity note 1/6 | BR rev 12 over 13 runs: SciPlay 6, Paul 6, build access 9, Anton 11 (`run_forensics/rev12/baseline2/baseline_review.md`:31). CL Oct 10 reply 0/7 (README:51) |
| 2 | "Done" source with a missing piece elsewhere (V2 trap 1) | LLC ENG-2462 3/6 | VN ZOM-562 1/6, ZOM-293 0/6 (symptom only in a comment) | DG: three tickets 0/6, three 2/6, one 4/6; 17 all-fail rows and 26.4% of weight at 0/6 |
| 3 | Completion or answer recorded elsewhere (V2 trap 9) | CS SavvyCal, Buttondown disputes 1/6; Edgegap 5/6 | Q4 Lanternfly, Spotlight, Balancy 0/6; WD CodeRabbit 0/6, Cursor 4/6 | CS is in the Finance column; no Medium case beyond it |
| 4 | In-scope item outside the obvious filter (V2 trap 7) | LLC VO issue 1/6 ("exactly one new issue") | Q4 Nintendo 0/6; Hootline 5/6 | JL scope count 1/6. BR Homa and Brightwater 6/6 (no cost: one calendar listing returned them) |
| 5 | Rule requiring a date or follow-through write (V2 traps 3, 4) | LLC ENG-2462 By date 2/6 | WD "nothing is due" rows 2/6 to 4/6 | JL Pacific-time conversion 0/6 (README:26) |
| 6 | Alias alone (V2 trap 6) | No opaque-payee case exists; "mostly G" (SC4:197) | Q4 "night pager" right in the pre-check. Wen and Maren were aliases plus an off-path thread, 0/6 | BR Hiro resolved through contacts, LEAKED once the template named the lookup (BR 01a s4). HO partner rows 3/6 |

**[E] Finance and reconciliation only.**
- A total was reconciled against a second source only when told to: 12 of 12 asked, 0 of 18 unasked (SC4:102).
- Rule-led anomalies were caught 6 of 6. Self-noticed ones were found by 2 to 3 of 6 and reported, not chased (SC4:118).
- Near-duplicate payments and currency parsing have no measured rate (SC4:117,199).
- The average lost on a Finance total is cascade weight: LLC's VO took the total, all shares, the sheet row, the issue and the reply (ER/1a_hardness_PASS_r2.md:43,50).

**[E] What reliably did not cost points, even when it looked hard.**
- Judgment and status calls once the record is read: "never landed across 28+ runs" (JL README:25; SC4:180). The one exception was WD's clash wording, 3/6 (SC4:166).
- Long lists and bulk writes: LLC 36 of 37 issue calls right (ER/1a_hardness_PASS_r2.md:72); 44 of 45 and every total in WD (WD ER/1a_hardness.md:77); BR rev 17's 50 writes; the 44-file Drive task (V2:85).
- Clean arithmetic: every total adds up when inputs are right (V2:86; WD 1a:51).
- A rule stated in a doc the hub names: CS adjustments tabs 6/6 (SC4:172); LLC DD test 5/6.
- A same-channel or same-thread correction (V2:17; LRN:466-470).
- Stacked traps on one fact (HM:883-884, pass rates 0.68, 0.63, 0.77: stacking made rows easier).
- Decoys on a path the run never takes (LRN:483).
- More services or rows (V2:90).

**[E] Measured habits to place traps against (SC4).**
- 0 of 339 searches carried an amount (SC4:43,219). 0 of 24 runs used a page token (SC4:37).
- Founder channels were never opened by read or thread (SC4:74).
- Channel reads never reach further back than the task's own window: 4 days on Robert tasks (SC4:69).
- Undated searches are payee or firm names (SC4:81). Thread replies are invisible to `read_channel` (SC4:85).
- Habits that split runs near 50%: a date sweep of the mailbox (6 of 12 Robert runs), reading the clock-week DM, a date-bounded generic Slack word, `read_thread` from a pointer (SC4:45,182).
- Places that gave 0 to 1 of 6: a surface no hub names, mail with no name in the run's list, a reply off the swept channels (SC4:183).

**[I] SC4's estimates need discounting.** Its channel estimates (mean miss 0.59, SC4:201) are mostly guesses. The caller's report of a band 1 rev6 run is one observation against them.

## 3. Keeping a "correction elsewhere" fair

### What the passing cases had [E]

| Condition | Evidence |
|---|---|
| Same item, same owner or person, later than the original, before the clock | V2:36; BR r4 s4: "Both records are Arthur's. The correction is later, names the same people and the same platform, and explicitly says the Linear log is wrong"; LLC r2:20 (dated before the Slack cut) |
| It is a fact that answers an existing ask, not a new rule | LLC r2:25 ("facts that answer existing asks... They add no new obligation"); Q4 r2:33 ("Facts, not obligations") |
| An incorporated rule makes the record part of the job | LLC r1:23 and r2:25 chain; Q4 r2 s5: guardrails rule 1 "makes these records part of the job, not trivia" |
| A record outside the owner settles a claimed-done gap | LLC ER/1_prompt_FAIL_r1.md:328: Blake's "done" vs Apple's rejection, fork REJECTED because "A different record settles the gap". Owner's own claim alone is a fail basis (JC ER/1_prompt_FAIL_r3.md:400 SCOPE_GAP; MEM:closed-rule-and-census-for-open-sets line 19) |
| Persona can read it; author belongs to the channel | LLC r2:27; MEM:same-bytes-prompt-verdict-flip line 12; KDI NB-1 |
| Each new record is named per item, and the /prompt basis says RECORD | CL ER/1_prompt_PASS_r3.md:115; LLC ER/1_prompt_PASS_r3.md:232 (later email over earlier comment) |
| A pointer exists from where the run already is, if the carrier is a comment | VN ER/1a_hardness-4.md F1, "same as Brian found"; ER/1_prompt-1.md:106; MEM:task-authoring-tool-quirks ("a deciding comment on either needs a seeded pointer") |

Worked examples that passed both /injection and /prompt on the same SQL:
- LLC rev4: $62 in the Jenkins mail, VO in a #prototype thread reply, layer.ai in a thread reply, Apple rejection in Robert's inbox (README:24,30; ER/1_prompt_PASS_r3.md:232,241).
- CL rev3: six single-item carriers (ER/1_prompt_PASS_r3.md:115).
- BR rev12: Paul in a DM, SciPlay in a thread reply, Arthur's post (ER/1_prompt_PASS_r6.md:143; final PASS r10).
- VN rev18: Brian's DMs, vendor mail, an inline PR comment (ER/1_prompt-4.md:135,580).

**Evidence limit.** Q4's de-named carriers have no stored /prompt or /injection pass. The only stored /prompt report is on rev 5 (ER/1_prompt_PASS_r1.md:19), and rev 8 changed the carriers (README:11; ER/1a_hardness_NONFAIL_r2.md:10). Treat the de-named pattern as unproven for /prompt. /hardness r2 s5 did test it and held it fair.

**Thread reply under an unrelated parent is mixed.** It passed in BR (rev 11 note in `rev11/baseline/baseline_review.md`: "reply under the unrelated a16z post") and CL. MEM:coherence-presweep-before-prompt-review line 21 lists it as a flagged pattern. [I] Prefer a parent on a related topic.

### What failed review, including fixes that broke /prompt [E]

| Task, round | What happened | Dimension |
|---|---|---|
| LLC r1 | Hidden cost outside the tracker had no record saying whether it gets an issue. Fixed in the universe by adding "or pay for" to the project description (rev2 to rev3 diff, SQL line 113) | UGT 2, Clarity 2 (`1_prompt_FAIL_r1.md`:94,299-301) |
| JL r11 | Hardening carrier "leave the level editor tickets off too (162, 163, 201, 250)" did not say the list was complete | UGT 2, Clarity 2 (`1_prompt_FAIL_r11.md`:209,889) |
| JL r7 | "go by the build" in rule 5 opened a fork against the deck | UGT 2 (`1_prompt_FAIL_r7.md`:127,667) |
| JL r9 | Injected PR comment later than the PR's `updated_at` | Coherence 3 (`1_prompt_NONFAIL_r9.md`:823) |
| VN, six FAIL rounds before rev 18 | Each round a new defect: ZOM-564 checked on one build; two rules fit one ticket; undefined status value; injected comment contradicted the backend start script (SC-45); a doc called an old build current; a Done bug still failing | UGT 2 or Coherence 2 (`1_prompt.md`:116; `(1).md`:102; `(2).md`:104; `-1.md`:414; `-2.md`:417; `-3.md`:139) |
| CL r1 | "new store art" 2 or 4 tickets; lifecycle fields disagreed with comments | UGT, Clarity, Coherence 2 (`1_prompt_FAIL_r1.md`:103,445) |
| BR r1, r2 | Nine forks; then one firm's status with no outreach record | UGT 2 (`1_prompt_FAIL_r1.md`:115; `_r2.md`:135) |
| WD (3) | Figure existed only in an unreadable PDF | Feasibility, UGT, Coherence 2 (`(3).md`:590) |
| WD (1), (6) | Snowflake ledger and base P&L disagree on a graded value | Coherence 2 (`(1).md`:419; `(6).md`:563,567) |
| S2 rev4 | Lauren Brooks bucket; Combo Fighter revenue on NB-26 | UGT 2, Clarity 1, Coherence 1 (`plateform_reports/..._1_prompt.md`:98,352,366) |
| JC | Open set "what still has to land": about 90 candidates | UGT 2 (LRN:709-713) |
| dd-2024 | Seeded notes contradicted base git | Coherence 2 (LRN:534-547) |
| Same bytes | Identical SQL and prompt passed, then failed on a fork already present | UGT 2 (MEM:same-bytes-prompt-verdict-flip) |

**[E] Finance-specific coherence rules.**
- Census every vendor across all mailboxes and Slack before seeding a lifecycle or payment fact (LRN:116-121). Take payment status from receipts, never a cost sheet (LRN:125-126).
- A repeated global fact becomes hundreds of findings (LRN:130).
- Never on an injected Confluence page, never only in an attachment (LRN:216; HM:885-886).
- No activity on a closed record (LRN:552).

**[E] Known-issue cards that bear on rev7.**
- NB-12: do not grade a vendor named only by a token; use a record that spells it out (KDI:68).
- NB-6: no Slack after Feb 13 10:03 UTC.
- NB-1: no post by someone in a channel they left after Feb 11 20:40 UTC.
- NB-4: February payment status.
- NB-26: Combo Fighter sales.

## 4. Score spread and failure patterns

**How the gate counts [E].** A pattern is the exact failed-criterion set. Two runs differ only at 2 or more rows, with transitive merging (FPG:13-16,33-36; CF:17-19). Exactly 50% passes (CF:19,43).

**Baseline shape, recomputed** (share of rubric weight by rows passed out of 6):

| Task (mode) | Avg | SD | Patterns, largest | Full | 6/6 | 0/6 | 1-2 | 3-4 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| HO (Medium) | 80.8 | .161 | 4, 40% | 1 | 50.4 | 0 | 4.2 | **31.9** | 13.4 |
| DG (Medium) | 56.3 | .117 | 4, 33% | 0 | 44.6 | 26.4 | **21.7** | 7.3 | 0 |
| BR (Medium) | 77.7 | .106 | 4, 40% | 1 | 61.3 | 0 | 8.9 | **29.8** | 0 |
| LLC (Easy) | 83.6 | .103 | 3, 40% | 1 | 64.9 | 0 | 14.3 | 3.4 | 17.4 |
| JL (Medium) | 83.8 | .099 | 4, 40% | 1 | 66.5 | 0 | 11.6 | 11.6 | 10.4 |
| CS (Medium, Finance) | 78.3 | .054 | 4, 50% | 0 | 65.0 | 8.2 | 12.8 | 3.3 | 10.7 |
| VN (Easy) | 78.3 | .049 | 4, 50% | 0 | 68.7 | 4.8 | 17.6 | 4.4 | 4.4 |
| WD (Easy) | 85.7 | .034 | 6, 17% | 0 | 77.4 | 4.6 | 7.2 | 10.8 | 0 |
| Q4 (Easy) | 71.0 | .016 | 4, 50% | 0 | 61.1 | 23.7 | 4.3 | 4.0 | 6.9 |

**What the data shows [E].**
- LLC and BR each cleared .1 with one 100% run, and neither clears it without that run (SC4:266). DG cleared it with no full pass, through heavy clusters at 0/6 and 2/6.
- Weight at 0/6 adds nothing to spread: Q4 has 23.7% at 0/6 and SD .016 (README:55). All-fail rows cancel out of symmetric differences (CF:27).
- Spread comes from heavy traps at mid rates that move the score by 10 points or more when missed (DG, BR, HO). "Corrections nobody finds add no spread" (CL README:51).
- Only mid-findability traps separated runs: CL Sep 29 mail 5 of 7, Robert's rejection 2 of 7 (CL README:51). VN and LLC say the same (VN README:36; LLC README:78).
- Per-target rows dilute. LLC went 73 to 130 rows and proxy about 76 to 83.6 (README:79; different proxies, A06/07:22). BR's added rows took projected SD .131 to .106 (README:28). SD falls as always-passed weight grows: BR reached .1 near weight 129 (`rev12/baseline2/baseline_review.md`, Robustness). Builder weights alone flipped .106 to .098 (LRN:684).
- Identical SQL gives different pattern outcomes: BR rev12 batch 1 failed patterns at 80%, batch 2 passed at 40% (`rev12/downstream_notes.md`:70; baseline2:32, "Batch-to-batch variance is large").
- Author estimates err both ways. BR rev11 guessed Paul caught 45-60% and build 55-70%; both were 7 of 7 (`rev11/baseline/baseline_review.md`). VN guessed miss 0.5-0.55; actual 0.83 to 1.0 (`01a_Hardening_Report.md`:241; recomputed).

**How to get runs to differ on 2 or more rubric results [E].**
1. Three independent traps, four safer, each with its own dated decider (FPG:82-84). "Two traps settled by the same message are one trap."
2. Grade each trap on two atomic rows that can pass or fail separately: decision plus reason, one rule on two records, one rule on two figures, value plus destination (FPG:90-101). The same number in the sheet and the reply is not a second row (FPG:101).
3. Do not let the total and share rows carry all differentiation. In LLC, four traps converged on the same total/share/reply rows and differed only on item rows; a single ENG-2462 row would have merged four failing runs (1a_hardness_PASS_r2.md:67,84; `rev4/baseline/BASELINE_DECODE.md`:48).
4. One early miss must not block later traps (FPG:103-109). LLC's VO was 14 rows from one miss (README:78).
5. Independence of route, not only of record. SC4:284 warns that two habits (founder-channel reach, mail sweep) drive most S2 channels, so seven channels are fewer independent patterns.

**[I] For a reconciliation page.** Put the traps on separate game or payee rows that each move at least one per-game figure and its own payee row. A trap that moves only the grand total will merge with the others. V2:73 asks for the corrected input and the final figure on separate rows. Note the bridge-run risk: CF:85 shows two rows apart can still merge through a third run.

## 5. Common hardening moves that backfire

| Move | Evidence [E] |
|---|---|
| Padding, more steps, more payees | BR rev 17 band 1 after 50 routine writes (r3:105). JL 741/222/836 calls, band 2 (A06/02:30). V2:90, V2:135. Padding is contrived (Evals/1_Prompt_Eval.md:955) and a failing error (LRN:554). Per-record writes that a rule needs are the honest horizon source (BR README:29; SC4:20) |
| Deleting a rule or conclusion without a settling record | LLC r1:79: "Don't just delete them: a rule nothing in the data settles becomes a fork". Vaguer asks: 18 of 31 QMS reviews failed UGT (HM:693-694) |
| Removing incorporation | Graded rules in a handbook the prompt never names: 9 all-fail rows, all invalid (HM:700-701). prompt-incorporation-v1 excludes unincorporated rules (Evals/1_Prompt_Eval.md:443-449). VN README:28 shows the rubric and scope follow the incorporation chain. Local reviewers without it asked for rows the platform rejected |
| Closing forks by adding sentences | Each clarifying sentence settles cells a run would explore; forecast then about 76% (LRN:733). Patched text starts to look planted (LRN:737). Five edits in JC made new forks (LRN:727) |
| Staged typos | Fail Contrived (Evals/1_Prompt_Eval.md:102,438,1494; LRN:58) |
| Hidden destination | Fails Contrived alone (Evals/1_Prompt_Eval.md:1005,1496; LRN:54) |
| Rules in the prompt | One task went from failing to 100% (V2:135). Deliverable-spec prompts fail (LRN:55-56) |
| If-chain | Fails Contrived alone; "A per-case rule belongs in a seeded record" (Evals/1_Prompt_Eval.md:1032-1050) |
| Trap hint or riddle | Fails Contrived (Evals/1_Prompt_Eval.md:1007-1012) |
| Hiding everything | Q4, CL: 0/6 records, SD .016 and .025. FPG:86: buried deciders are "likely to be judged a Unique Ground Truth failure" |
| Raising a weight or splitting rows after the run | FPG:121-123; CF:75,78. Local policy: weight follows the work |
| Alias through a token | NB-12. The alias must be a spelled-out record in contacts or history (V2:61,99) |

**Local gates vs platform [E].**

| Area | Local | Platform |
|---|---|---|
| v2 self-checks | `hardness_v2_check` all CLEAN on BR rev5, then band 1 (BR 01a s8). Advisory, lexical on prompt leak (HM:911; CF:69) | Reads the run |
| Trap floors | At least 12 traps, 7 families (`playbooks/01_Scenario_Design.md`:305) | No such count: "1-2 load-bearing" (HM:880-883). Floors never showed difficulty (CF:77) |
| `diversity.authority_share` | Fails when one doc governs most rows | No effect on the platform (WD README:24; DG README:24; VN README:33). LLC cleared it with honest origins (README:89) |
| UGT rules | `ugt-fork-v1` and `base-data-v1` not in the local bundle (LRN:718) | Applied. Local PASS does not predict it (LRN:111,209,717) |
| Local gates passing | Structure, hashes, citations (LRN:71,374-382) | Semantic forks and base contradictions |
| Base claims | `base_check` can fail what /prompt passed (LRN:632-637) | Check `git log` before trusting a gate |
| Proxy grader | `surface_grader` 26.1% on a run that met every slot (BR 01a s1); 43.1% (LLC BASELINE_DECODE:10) | Hand decode write payloads |
| Forecast | Advisory; solver view cannot fail write-content slots (MEM:task-authoring-tool-quirks) | Only runs count |
| Narrow-miss rule | Not in local `Evals/1A_Hardness_Eval.md` (no occurrence of "narrow"; band table at 165-182) | Applied: one cause under Easy's 10% loss scores 2 (LLC r1:52,71) |
| Rubric | Older release, no `scope_tail` or `bundled_writes` (VN README:27; CL README:39) | Failed files local passed 5 |
| Stability | Local P2 stricter on Coherence (MEM:same-bytes-prompt-verdict-flip) | A /prompt PASS does not hold on re-run (same note) |

## 6. Checklist for rev6 to rev7

**Must do**

1. Keep `04_Prompt.txt` byte-identical and do all edits in SQL; then re-send /injection and /prompt as a pair, a fresh Opus run and /hardness. [E: LLC README:25, Q4 01a:171, LRN:576]
2. Before cutting any Linear conclusion or doc exception, write a row for it: fork, the dated record that now settles it, its author, its service, the route from an incorporated hub. No record, no cut. [E: LLC r1:79]
3. Name 3 to 4 independent traps, each with its own decider and each changing a status or number. Each should carry 10% or more of the weighted core, or expect two to land per run, because of the narrow-miss rule. [E: FPG:82-84; LLC r1:52,71]
4. Aim catch rates at a third to two thirds. Put carriers on routes that split runs: mailbox inside the last 4 to 9 days before the clock, a reply reachable by `read_thread` from a pointer, a date-bounded generic Slack word. [E: FPG:70; SC4:182]
5. Make each correction fair: same item and owner, later, before the clock, states the figure and names what it replaces, in a place Robert can read. Where a claim is "done", let a non-owner or counterparty settle it. [E: section 3]
6. Grade each trap on two atomic rows on separate payees or figures, weight 5 by kind of work, with per-game rows carrying differences. Plan at final per-target granularity. [E: FPG:90-101; LLC README:79]
7. Census each touched payee across all mailboxes, Slack and the warehouse, and check NB-1, NB-4, NB-6, NB-12 and NB-26. [E: LRN:116-121; KDI]

**Must not do**

8. No new payees, issues, steps, rows or routine writes. [E: V2:135; BR r3:105]
9. No rules, hints or if-chains in the prompt; no hidden destination; no staged errors. [E: section 5]
10. No correction in the same issue, thread, doc or bulk call as the original, and none using the words the pointer sends runs to search. [E: LRN:270-274; BR r3:111]
11. Do not hide everything. Avoid founder channels, unnamed surfaces, thread replies many months back and full de-naming as the default; those give 0/6. Keep at most one such wall, checked for fairness. [E: Q4 README:55; CL README:51; SC4:183]
12. No open-set rule, no clause that feeds no truth value, no token-only alias, no comment on a closed record, no fact only in an attachment or injected Confluence page. [E: LRN:552,711; MEM:closed-rule-and-census-for-open-sets; NB-12; HM:885]

**Test before spending a run**

13. Replay the run's habits on the draft SQL: run SC4 Appendix query shapes per carrier; confirm which search words hit it, and that no bulk call returns it. Treat every estimate as a guess; BR's and VN's were wrong in opposite directions. [E: SC4; BR rev11 review]
14. Score policies on the real surface: a full-retrieval solver must score 100%, each single miss must cost a stated amount, and SD must be recomputed at final rows. Run `hardness_v2_check` and resolve flags, but do not treat CLEAN as evidence. [E: LRN:411-419; BR 01a s8]
15. Cold reviewers before review: fork sweep over every payee and bucket, coherence claim audit of every new record, delta review of each new sentence, and one reviewer acting as an Opus run. Do not resume a reviewer to confirm its own list. After two pre-checks falsify a mechanism, change the mechanism. [E: MEM:closed-rule-and-census-for-open-sets; MEM:coherence-presweep-before-prompt-review line 39; A06/02:70]

## Conflicts and limits

- FPG:79 lists a correction later in the thread as a splitter; V2:17 and BR say same-thread is caught. CF:82 resolves this for V2 placement. On S2's Linear notes, follow V2.
- V2:126 says "raise the weight". Local policy and CF:75 say change the work instead. V2 Part 6 and CF:78 also differ on guard rows.
- The SD rule uses population SD. BR and JL sit at the edge, where sample and unweighted SD read the other way (BR `12_Difficulty_Stats.txt`; JL `12_Difficulty_Stats.txt`).
- VN's rev-18 report calls ZOM-562 the "same miss as the previous run" (1a_hardness-4.md F2), but the rev-11 report marks that trap right (1a_hardness.md:47,84). One report is wrong, so I did not use that sentence.
- LLC and the other READMEs record final local-weight scores. LLC has no `12_Difficulty_Stats.txt` (README:44), so its pattern count above is my recompute.
- Nothing here has been tested on S2 rev7. The section 2 order and every [I] line are judgment.
