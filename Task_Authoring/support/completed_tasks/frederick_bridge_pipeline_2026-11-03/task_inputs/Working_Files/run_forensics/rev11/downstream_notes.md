# Rev11 notes for Oracle Events, rubric and the next platform runs

Rev11 is bound to the task SQL stored in this folder (`01_Universe_Inject.sql`). The prompt `b5ea6f0ff28c` is unchanged since rev7. The truth changes for Paul Heydon only (solver/truth.json, copied here). Everything else in `run_forensics/rev10/downstream_notes.md`, `rev9/downstream_notes.md` and `rev8/platform/downstream_notes.md` still applies unless it mentions Paul or the old counts.

## Why rev11 exists (rev10 baseline)
- Rev10 passed /injection and /prompt, and /hardness gave NON-FAIL 3 (PROCEED).
- The six baseline runs averaged 133 counted calls (lowest 114) with 0 full passes. But runs 1, 3, 5 and 6 failed exactly the same values: SciPlay plus both build-access cells. One failure signature covered 4 of 6 failing runs, over the 50% limit, and the score spread was about 0.04, under the 0.1 floor. See `run_forensics/rev10/baseline/baseline_review.md`.
- Cause: build access was missed 7 of 7 times and SciPlay 5 of 7, while Paul's rev10 trap was caught 7 of 7. Traps nearly every run misses, or nearly every run catches, make every run fail the same way.

## What changed
- **Paul backs out (DONE1, truth change).** His rev10 "Done, signed it" reply is gone. On Sep 30 at 7:55am PT he writes Leonard only that he has to back out. At 10:05am PT Leonard replies under his own Sep 19 #executives angel post (C07C2866011/1759251900.863415): "Paul's out, he wrote me this morning that he can't put money in this year after all". Under the send-list doc that is a pass with no call, so Paul is off the send list: no row, no checklist item, no follow-up card.
- **T-Accelerate's correction moves into Karthic's own thread (DONE2, truth unchanged).** Karthic reports at 10:20Z that the Android link doesn't work. At 1:05pm PT Arthur answers in the same thread (Frederick cc'd) that the Play tester list the investor accounts are on was never attached to the internal test track, so nobody on it has the Android build yet; iOS is all set. Arthur's #zombie-match3d reply now covers the 3 Dentsu folks only. Dentsu and T-Accelerate both stay "iOS only".

## Truth (rev11)
- 25 on the send list: New investor 1 (Anton Bernstein, $25,000); In talks 7 (GFR Fund, Andreessen Horowitz, NCsoft, Homa, Brightwater Games Fund, Dentsu Ventures iOS only, T-Accelerate iOS only); Awaiting reply 14; Keep warm 3 (LVP, Hiro Capital, SciPlay).
- Off the list: Paul Heydon (backed out), Play Ventures, March Gaming Fund / 1AM, Grishin Robotics, Lakestar Ventures, [PERSON_NAME_5402], and everyone not contacted since Sep 3.
- Trello: 4 checklists with 25 items; 18 "F/up with" cards (no card for NCsoft, Dentsu Ventures or Makers Fund); one comment on the Anel card (NCsoft).
- Reply counts: New investor 0 firms, 1 angel; In talks 7 firms, 0 angels; Awaiting reply 14 firms, 0 angels; Keep warm 3 firms, 0 angels.

## Rubric guidance (the pattern and spread gates depend on it)
Two failing runs count as different patterns only if they differ on 2 or more rubric rows (Evals scoring.json, Agent Failure Rate). So grade each deciding fact on its own rows, the way a reviewer would check it anyway. Don't add rows only to split patterns, and don't re-weight rows to hit a number.
1. Weight 5 on the deciding values, one row each:
   - SciPlay in Keep warm;
   - Paul Heydon not on the send list;
   - Dentsu Ventures build access "iOS only";
   - T-Accelerate build access "iOS only";
   - Anton Bernstein New investor at $25,000.
2. Reply counts: one row per group (New investor, In talks, Awaiting reply, Keep warm), weight 3 each. A SciPlay miss fails In talks and Keep warm; a Paul miss fails In talks.
3. Checklists: one row per group's item set (weight 3); the follow-up card set as one row (weight 3); the NCsoft comment as one row.
4. Keep routine delivery rows light (weight 1): sheet name and folder, reply on Leonard's thread, not sending to the whole list.
5. Fair variations to accept: card titles with the firm or the contact's name; the reply's recipients (reply or reply-all); "iOS only" written as TestFlight only.
6. Expected failure patterns (rev11):
   - DONE1: Paul In talks at $50,000 (adds his row, an In talks item and a card; In talks count 7 / 1);
   - DONE2: Dentsu and/or T-Accelerate "iOS and Android" (from ZOM-567);
   - CORR: SciPlay In talks (as rev8-rev10);
   - INPUT: Anton at $40,000;
   - natural: Treo VC left out (its Sep 3 outreach not opened).

## Estimates (UNCALIBRATED; six-run simulation from the 15 rev8-rev10 runs)
- P(perfect pre-check run) about 3-7%: /hardness should again see a consequential miss.
- Baseline: P(no pattern over 50% of failing runs) about 0.92-0.95; P(spread 0.1-0.3) about 0.80; P(average under 80%) about 0.97-0.99; P(all baseline gates) about 0.74-0.77.

## Rev11 platform results (Nov 3, 2026)
- /injection PASS / COMPLETE on 75b6cb2ac453 (lint 0 FAIL, 0 CHECK, 0 INFO). /prompt PASS, score 5 (dataset similarity 0.762). Reports: `platform/` (copies in `Platform_Report/` as injection_report11, prompt_report9, hardness_report5).
- /hardness: **NON-FAIL, score 3, PROCEED (OBSERVED_OPUS_FAILURE)**. Run `precheck/trajectory.json`, sha 9edcc952.
  - 216 tool calls: 166 in the main thread and 50 in five subagents (all five died with "Autocompact is thrashing"; the main thread redid their reads). 182 are MCP calls. 57 writes, 0 errors.
  - **Missed (MATERIAL_FAIL R5):** SciPlay filed In talks. The run read #executives at the top level but never opened the a16z thread that holds Robert's reply, and never searched Slack for SciPlay. Effects: SciPlay's row, an In talks item instead of Keep warm, a spurious "F/up with SciPlay" card (19 cards), reply counts In talks 8/0 and Keep warm 2/0.
  - **Caught:** Paul off the list (it opened the angel-update thread right after its "SAFE" search), both build-access cells iOS only (from Karthic's and Arthur's emails over ZOM-567), Anton $25K, the a16z speedrun, Hiro/Edith, the off-list firms, the NCsoft comment, the Dentsu and Makers skips.
- Reviewer's suggestions: a weight-5 rubric row and an OE step on SciPlay = Keep warm (Robert's Sep 30 #executives thread reply); separate rows for build access and for Paul off the list; reply counts 0/1, 7/0, 14/0, 3/0.

### What the pre-check does and doesn't predict for the baseline
- The pre-check ran with a different Slack tool set (`slack_conversations_search_messages`): its search results show `reply_count`, `latest_reply` and `latest_reply_time` on a parent post. That made the angel post's Sep 30 reply plain to see.
- All seven rev10 runs (pre-check and six baselines) used `slack_search_public_and_private`. Its results show no reply count, only `thread_ts` equal to `ts` on a parent. Every one of those seven runs had the angel post in a search result ("SAFE", "docusign", "angel" or "Paul"), but only 4 of 7 opened any thread at all.
- The T-Accelerate thread was read in full (get_thread) by 5 of 7 rev10 runs; one more read only the base message by id.
- So the baseline catch rates stay near the design estimates: SciPlay about 0.25-0.33 (2 of 8 so far), build access about 0.55-0.7, Paul about 0.45-0.6 with the baseline tool set.

### Updated estimates (UNCALIBRATED; same six-run simulation, scratchpad sim6.py)
| SciPlay catch | Build catch | Paul catch | Patterns OK | SD 0.1-0.3 | Avg < 80% | All gates |
|---|---|---|---|---|---|---|
| 0.25-0.33 | 0.55 | 0.45-0.6 | 0.92-0.94 | 0.80-0.83 | 0.96-0.99 | 0.73-0.77 |
| 0.25-0.33 | 0.7 | 0.45-0.6 | 0.87-0.91 | 0.78-0.82 | 0.94-0.99 | 0.67-0.72 |
| 0.25-0.33 | 0.55-0.7 | 0.8 | 0.75-0.85 | 0.75-0.79 | 0.84-0.95 | 0.53-0.62 |
- The last row is the risk case: if the baseline tool set ever shows reply counts, Paul gets caught most of the time, SciPlay becomes the only common miss, and the runs start to fail the same way again.
