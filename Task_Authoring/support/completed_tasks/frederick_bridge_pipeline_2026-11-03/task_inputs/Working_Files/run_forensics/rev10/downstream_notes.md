# Rev10 notes for Oracle Events, rubric and the next platform runs

Rev10 is bound to the new task SQL (see `01_Universe_Inject.sql` in this folder). The prompt `b5ea6f0ff28c` is unchanged since rev7, and the truth is unchanged too: solver/truth.json, sha256 f3dd0b9de6e2d3f8. Everything in `run_forensics/rev9/downstream_notes.md` (Trello truth, rubric guidance) and `run_forensics/rev8/platform/downstream_notes.md` (sheet and reply) still applies.

## Why rev10 exists (rev9 /hardness)
- /injection and /prompt passed on rev9 (a34c7de38601). The Opus pre-check made 135 tool calls, so the Trello writes fixed the horizon.
- /hardness scored 1 (Too easy, FAIL). That single run found every trap:
  - it read the #executives thread with SciPlay's pass;
  - a Slack search for "tester" returned Arthur's root post directly;
  - Leonard's "still sitting with you" nudge showed Paul's gap in plain view.
- The rev8 pre-check, on the same traps, missed two of them and scored 4. The pre-check is one run, so the result depends on whether that run happens to catch every trap. Rev10 makes a perfect run much less likely.

## What changed (truth unchanged)
- **DONE2 (build access):** Arthur's correction (C0880U9751A/1759274400.518306) and Leonard's answer are now replies in the thread under Leonard's base Sep 29 post "I just released 0.3.49 on IOS" (C0880U9751A/1759182908.627389).
  - The new text names Karthic, the 3 Dentsu folks, the Play console group, the internal track and "the Linear log".
  - It no longer says tester, TestFlight or ZOM-567.
  - Dentsu and T-Accelerate stay "iOS only".
- **DONE1 (Paul):** Paul's reply in the nudge thread, Sep 30 8:40am PT: "Done, signed it last night".
  - No DocuSign Completed notice for Paul exists.
  - Leonard's #executives note says only a Completed notice counts, and "them telling us they're in doesn't count".
  - Paul stays In talks at $50,000. He gets an In talks checklist item and a follow-up card.

## Rev10 platform results (Nov 2, 2026)
- /injection PASS / COMPLETE on c999829d668e (lint 0 FAIL, 0 CHECK). /prompt PASS (dataset similarity 0.762). Reports: `platform/`.
- /hardness: **NON-FAIL, score 3, PROCEED (OBSERVED_OPUS_FAILURE)**. Run `precheck/trajectory.json`, sha 8c579cc2.
  - 144 tool calls: 130 in the main thread and 14 in two subagents. 127 are MCP calls (114 main, 13 sub), with 0 errors. The horizon holds.
  - **Missed (MATERIAL_FAIL R7):** Dentsu and T-Accelerate written as "iOS and Android" from ZOM-567. The run never opened Arthur's thread reply, and never searched Slack for Dentsu, Karthic or android. Both of its subagents died ("Autocompact is thrashing"); the reviewer still counts the miss as the model's.
  - **Caught:** Paul (In talks, "no DocuSign Completed notice yet"), SciPlay (#executives thread), Anton $25K, the a16z speedrun, Hiro/Edith, the off-list firms, the NCsoft comment, both BOOKED skips, the counts 0/1, 7/1, 14/0, 3/0.
  - The run repeated the wrong build access in the reply to Leonard and in its final response.
- Reviewer's suggestions: a weight-5 rubric row and an OE step on the two build-access cells (T-Accelerate iOS only, Dentsu iOS only, from Arthur's Sep 30 #zombie-match3d thread reply over ZOM-567); keep the routine Trello writes at low weight.

## Rubric guidance (adds to rev9's)
1. Put weight 5 on the deciding values, per the hardness reviewer:
   - SciPlay's group (Keep warm);
   - the two "iOS only" cells (Dentsu Ventures, T-Accelerate);
   - Paul Heydon's group (In talks, $50,000);
   - Anton's amount ($25,000).
2. Keep the routine Trello writes (checklist items, ordinary follow-up cards) on light weights. Grade the follow-up set as one criterion, as rev9's notes say.
3. A run that makes Paul a New investor also gets the reply counts wrong: New investor 0 firms / 2 angels and In talks 7 / 0, instead of 0 / 1 and 7 / 1. It also puts Paul on the New investor checklist and gives him no follow-up card. Grade the group on its own row and the counts on another; don't grade every downstream effect separately.
4. Expected failure patterns, in addition to rev9's:
   - DONE1: Paul as New investor (from his "signed it" reply).
   - DONE2: Dentsu and/or T-Accelerate as "iOS and Android" (from ZOM-567).
