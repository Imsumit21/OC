#!/usr/bin/env python3
"""Write review_notes.json for build_check.py: the sweep, advisories, counter-readings and the reviewers' outcome."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(HERE, 'events.json')))
L = E['label']
def o(k): return f"OE {L[k]}"
N = json.load(open(os.path.join(HERE, 'review_log.json')))
notes = {
 'prediction': 'PASS 5', 'completeness': 5, 'accuracy': 5,
 'findings': [],
 'base_ptr': {'music': 'hg.py get slack messages/C06DJBJL798/2025-08.json /22 and /33', 'icon': 'hg.py get slack messages/C08R8CHB0QL/2025-09.json /121; SQL L27',
              'users': 'hg.py get linear data.json /users/33, /users/18, /users/9, /users/28, /teams/0', 'who': 'hg.py get slack users.json /3'},
 'sweep': [
  ['1 One wrong count, ID, channel or tool', f"PASS: 62, 58, 56, 48, 42, 36, 30, 18, 14, 12, 11, 10, 6, 5, 4, 3, 2 recomputed by oe_gen/model.py and by the blind reviewer; ids from the SQL rows"],
  ['2 One required write missing', f"PASS: doc {o('w_doc')}, tracker {o('w_sheet')} and {o('w_rows')}, 12 shares, 58 comments, 48 assignments, 2 tickets, reply {o('w_reply')}"],
  ['3 One fact in expected data with no retrieving step', 'PASS: every Expected fact comes from its own read or an earlier event'],
  ['4 One act-vs-defer conflict', 'PASS: research/defer_absence.md finds no hold on any of the six write families (ledger section C)'],
  ['5 One non-action or final-response event', 'PASS: none in 161 events'],
  ['6 One prompt-forbidden write', 'PASS: the prompt forbids none; the Skip tickets get a comment and no assignee, the exported sets no ticket'],
  ['7 One missing recovery/wait event for an injected error', 'PASS: Friction: none (03_Error_Async_Config.txt)'],
 ],
 'advisory': [
  [f"{o('reply')}, {o('note')}, {o('leave')}, {o('packs')}", 'No baseline run read these records, so their search routes rest on the tool contract (state_full.json) and the seeded text, not on a run. The contract says Slack search is keyword AND and trello_search free words match comment text.'],
  ['Comment and assignment events', 'Each is one write on one ticket by rule, so the set runs to 161 events; the rubric review will cite these labels.'],
 ],
 'self_review': "Re-read as the eval: walked Evals/2_Oracle_Events_Eval.md 1.2 (inventory), 1.3 (five fields per STEP), the HARD GATE (no non-action or final-response event), 2.1 to 2.7 (service, tool, parameters, expected data, visibility, authority, act-vs-defer, format), 3.1 to 3.6 (completeness) and 4.0 (the sweep above) in order. Re-verified: every quoted span re-read from its record in this run by oe_gen/build_events.py (SQL parsed again, base through hg.py get), every call, date and maker recomputed by oe_gen/model.py and asserted equal to solver/truth.json, and every scoped id re-proved by the oe-writing gate through persona_view.",
 'independent': N['independent'],
 'counter': [
  ['R1', f"Counter-reading: COVERED, best case missing: the anchor could be another Leonard post; {o('ask')} pins the Sep 30 post that tags Claire, C06DJBJL798/1759269913.882683 (SQL L19)"],
  ['R2', f"Counter-reading: COVERED, best case missing: the review could be a different meeting; {o('review')} pins evt_d947bf7cd910549b674b1f, whose description names the plan and tracker"],
  ['R3', f"Counter-reading: COVERED, best case missing: an incorporated source could be unread; {o('ask')} lists five sources and {o('readme')}, {o('calendar')}, {o('deck')}, {o('changes')} and {o('leave')} read each (F1)"],
  ['R4', f"Counter-reading: COVERED, best case missing: the population could be narrowed to the sheet; {o('library')} adds ART-826 and ART-831 and {o('archive')} removes four (SQL L196)"],
  ['R5', f"Counter-reading: COVERED, best case missing: one date could cover all ads; {o('d_due')} splits 30 and 18 on C0880U9751A/1759275738.984915"],
  ['R6', f"Counter-reading: COVERED, best case missing: creating a doc is not the plan; {o('w_doc')} states the contents brief 4b requires (04_Prompt_Writing_Brief.md)"],
  ['R7', f"Counter-reading: COVERED, best case missing: the tracker could stop at the sheet's rows; {o('w_rows')} states 62 rows with ART-826 and ART-831 (solver/truth.json)"],
  ['R8', f"Counter-reading: COVERED, best case missing: one share could be offered for both files; each of the 12 events shares one file with one person from evt_d947bf7cd910549b674b1f"],
  ['R9', f"Counter-reading: COVERED, best case missing: Skip tickets could be left out; the comment events run over all 58 tickets, Skip with no date (ART-806 and nine more)"],
  ['R10', f"Counter-reading: COVERED, best case missing: an assignee could be the wrong Marcus; {o('users')} names marcus.bennett@harmonygames.co and sets marcus.lee@harmonygames.co apart (usr_b501f018a4c5319f)"],
  ['R11', f"Counter-reading: COVERED, best case missing: the exported sets could need tickets; {o('export')} quotes C08R8CHB0QL/1759247246.453725"],
  ['R12', f"Counter-reading: COVERED, best case missing: a link could be absent because the doc create returns no URL; {o('w_reply')} takes it from the share result (research/baseline_tool_shapes.md)"],
 ],
}
json.dump(notes, open(os.path.join(HERE, 'review_notes.json'), 'w'), indent=1)
print('notes written')
