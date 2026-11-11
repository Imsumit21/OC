#!/usr/bin/env python3
"""Adds outcome_reviews['prompt-writing'] to 00_V3_Authoring_Evidence.json, bound to the current brief."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
ah = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", os.path.join(WF, "04_Prompt_Writing_Brief.md")], cwd=WS, capture_output=True, text=True).stdout.strip().split()[-1]
p = os.path.join(WF, "00_V3_Authoring_Evidence.json"); E = json.load(open(p))
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json"))); E["context_hash"] = ctx["context_hash"]
E.setdefault("outcome_reviews", {})["prompt-writing"] = {
 "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": ah,
 "reviewer": "Claude (Fable 5.2), with the platform /injection PASS on rev1, a blind item-by-item fork sweep and a blind coherence sweep of the SQL (Working_Files/plan/sweeps/fork_sweep_inj.md, coherence_sweep_inj.md)",
 "rationale": "Brief §4b fixes every material field from dated records: Brian's note comment_faaa792418a942cd40be046d8d217a7d on ZOM-543, Arthur's rule doc f_6d0326fa006b136f1bbf82, the pass sheet f_cb40955893624e1acb8500 and its legend, the two review comments, Oliver's PR comment, Vincent's and Robert's later reports, Marcus's DM, Vincent's two ticket notes and Leonard's changed card. A blind agent given only the SQL and the base reproduced 12 Passed, 6 Waiting on QA, 21 Waiting on a fix, 1 clear area, 6 on the review list, the two reused tickets, the three state changes and the share list; the forks it raised were fixed in the SQL before the gate.",
 "accepted_outcomes": [
  "10 area children under ZOM-543, team ZOM, no assignee, Zombie Lane Done and the other nine Todo; the title is the area name, with or without a prefix",
  "19 new sub-issues, each under its area's child, titled with the report (Marcus's report may be reworded), state Done, In Validation or Todo by status, no priority, no assignee",
  "20 existing tickets (ZOM-567 to ZOM-584, ZOM-556, ZOM-560) moved under their area's child, each with a note giving the status and why in any wording; ZOM-571 and ZOM-581 to Todo, ZOM-572 to In Validation, the other 17 unchanged",
  "a stock-take sheet in d_36cdb0374c4aad3b8bf741 with tab Reports (Report, Area, Status, Ticket, Review list, Why; 39 rows) and tab Areas (Area, Status, Open reports; 10 rows), any title, any column order, shared with Brian, Leonard, Arthur, Julia and Vincent at any role",
  "one new slide in f_637e63ae6c1b4a7eb016aa giving 12 passed, 6 waiting on QA, 21 waiting on a fix, 1 area clear, 6 on the review list, any layout",
  "a message in Brian's DM D0770ET6WBW, as a thread reply to the ask or a new message, giving the same five numbers"
 ],
 "alternatives_considered": [
  "rows 1, 2 and 25 Passed on Vincent's chat ok: rejected, #1718 is a feature-branch build (C05433XK267/1758817549.151639) and Arthur's rule counts only main builds",
  "row 12 and row 32 Waiting on QA because #472 and #475 are merged: rejected by Arthur's review comments harmonygames-Games/match3d#472#rc_1 and #475#rc_1",
  "rows 13 and 38 Waiting on a fix for lack of a PR in the sheet: rejected by Oliver's comment harmonygames-Games/match3d#473#c_2 and the note's sentence on a dev's own merged PR",
  "row 9 Passed: rejected by Vincent's later reply C08R27X0EAH/1759267212.418339 on Android Submission 135",
  "row 29 Passed: rejected by Robert's later post C0880U9751A/1759268652.552719; the note says somebody, not only QA",
  "Daily Gift on the review list: rejected, Leonard's card was changed on Sep 30 (68dc11dceb76ad640995fd98) after Brian's line and the first invitation",
  "only Waiting on a fix on the review list: rejected by the note's 'a report that is not Passed'",
  "Marcus's glow line left out: rejected by the note's sentence on bugs told to Calvin in a DM since the 26th",
  "new sub-issues for the day counter and freezer rows: rejected by Vincent's notes on ZOM-556 and ZOM-560",
  "Vincent's canvases, his chat remarks, Oliver's skip exceptions and the input blocker as reports: rejected by the note's scope paragraph",
  "sharing with Brian and Vincent only: rejected by the hub's 'everyone on the review invite, Leonard too' and the event's attendee list",
  "leaving ZOM-571, ZOM-572 and ZOM-581 in their found state: rejected by the note's 'If its state does not match the status'"
 ]}
json.dump(E, open(p, "w"), indent=1); print("outcome review written, artifact hash", ah)
