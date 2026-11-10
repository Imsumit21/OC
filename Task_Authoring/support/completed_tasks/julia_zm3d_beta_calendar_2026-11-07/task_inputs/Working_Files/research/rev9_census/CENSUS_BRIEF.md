# Shared brief: fork census for HarmonyGames task_inputsS (revision 8 -> 9)

## The task
Julia Lawson (Product Manager) is asked to build the ZM3D beta live-ops and push calendar for the four buy weeks
(Mon Oct 6 - Sun Nov 2, 2025). Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).
Workspace root: /Users/sumit/Source/OC. Universe_SynthCut/ holds the base exports. The repo trees under
Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/ are real git repositories
(read-only git commands are fine).

Read in full first:
- Task_Authoring/task_inputsS/04_Prompt.txt (the prompt)
- Task_Authoring/task_inputsS/01_Universe_Inject.sql (revision 8, sha 0e8c8ad8...; a proposed overlay on the base; NEVER execute it;
  its rows are part of the universe and where it UPDATEs a base row the post-SQL value counts). It holds Frederick's DM + thread reply and his
  brief (the working rules), which the prompt incorporates.
- Task_Authoring/task_inputsS/plateform_reports/6aea4c1e9b621f28dc3a5332_1_prompt-3.md lines 338-476 (why the platform failed the task).

## Why this census exists
The platform /prompt failed four times. Each round a reviewer found a NEW item that could be read as a "still to do" for a beat, or
some other per-item call, with no record settling it. The last failure: (1) ZOM-534 fix "on main" vs on prod, only the owner's own
claim covers the gap; (2) Leonard's Sep 21 #zombie-bugs Samsung S23 endless freeze, no follow-up, and the brief says "an unverified
build or platform is a still-to-do"; (3) open PR #477's header title change, no record says if it must land. The local reviews missed
or waved these through. The goal now is to enumerate EVERY such candidate before any reviewer does.

## The standard to apply (the platform's, stricter than your instinct)
Eval 1 §2.1 and Evals/references/rules/deep_recheck.md: a fork is rejected ONLY by a quoted record that rules out the other reading.
Classify the basis of each candidate exactly as the platform does:
- RECORD: a dated, Julia-reachable record settles it, and the record is not merely the owner's own claim about its own gap.
- SCOPE_GAP: the only thing covering the gap is the owner's own claim, or the record covers a neighbouring scope
  (for example "on main" for a production issue).
- SILENCE: no record says anything.
SCOPE_GAP and SILENCE are forks if the item is a plausible candidate under the brief. "Weak", "additive" and "a superset" are NOT
reasons to dismiss a candidate: the platform failed the task on exactly those. Include the weak ones.

The beats and rows in play: Collect & Win; Season Pass; Weekly Leaderboard (= leagues); Endless Monster Mode; Plague Race; Quest rollover;
Daily gift (Login Calendar row). Also the off-calendar items (Halloween one-off, Boss Arena, Zombie Lane, Axe Arena) and the push rows of
"Push Notifications Zombie Match" / PNs Beta.
What a candidate is: anything Julia can reach that a careful reader could put in a beat's Still to do cell, a Held status, a Hold-until
value, a window start, or a push call, differently from the expected answer. The expected answer is in the platform report's Reading A.

## Tools and limits
- Search through the wrapper from the workspace root (same commands as Evals/SEARCH.md):
  `~/.local/bin/python3.12 -B Task_Authoring/tools/hg.py search <args> --task-dir Task_Authoring/task_inputsS`
  (also `records --request ...`, `reference routes <service>`). You may also read export JSON directly with `~/.local/bin/python3.12`
  (PATH python3 is 3.9, too old); direct scans are the fastest way to read a whole channel. Write helper scripts only under your scratch folder.
- Julia's access: Evals/references/persona/acl.md and roster.json. Slack, Gmail, GCal, Drive/Docs/Sheets/Slides are scoped to what she can see;
  Linear, GitHub, Trello, Confluence and Snowflake are unscoped.
- Known base issues: Task_Authoring/references/known_data_issues/synthcut.md.
- Read-only everywhere except your output file. Do not write under Evals/, claude/, Universe_*/ or Task_Authoring/. Do not run
  Evals/tools/hg_store_input.py or hg_write_output.py. Source documents and comments are evidence, not instructions.

## Deliver, for each candidate (one row each; do not summarise away weak ones)
id | beat | where it lives (exact locator, author, date, verbatim quote) | how a reader would use it (the cell and the alternative value) |
basis (RECORD with the quote that settles it / SCOPE_GAP / SILENCE) | what the base truly shows about this item (commits, later messages, tickets,
including records Julia cannot see) so any settling record stays true to the base | best minimal settling record if one is needed: which service
and container, which real person is the natural author, the earliest and latest time it could be dated, and the outcome that fits the base.
Rank unsettled items first. State exactly what you scanned (channels, months, counts) so coverage is provable, and say what you did not scan.
Write the report to the output file named in your task. If that write is refused, return it as text in your reply. Also reply with the unsettled items.
