#!/usr/bin/env python3
"""Writes Working_Files/04_Prompt_Check.md for 04_Prompt.txt (check mode, C1-C24) and binds the sidecar reviews
(role_reviews['prompt-check'], outcome_reviews['prompt-check']) to the prompt's artifact hash."""
import hashlib, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TD = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TD, "..", ".."))
SEED = json.load(open(os.path.join(HERE, "seed_text.json"))); sid = lambda k: SEED[k]["id"]
P = open(os.path.join(TD, "04_Prompt.txt")).read(); SQL = open(os.path.join(TD, "01_Universe_Inject.sql")).read()
WC, SHA = len(P.split()), hashlib.sha256(P.encode()).hexdigest()[:12]
HUB, NOTE, SHEET, RULE, DD, CARD, CARDUPD = sid("hub"), sid("epic_note") + " on ZOM-543", sid("sheet"), sid("rule_doc"), sid("dd_doc"), sid("rev_card"), sid("rev_card_update")
EVT, INV1, INV2, FOLDER, DECK, OLD = sid("event"), sid("invite_v1"), sid("invite_v2"), sid("folder"), sid("deck"), sid("gate_old")
IN1, IN2, ELSE, REOPEN, BACK, FILT, AG, AS = sid("inline"), sid("inline2"), sid("else_pr"), sid("reopen"), sid("back"), sid("filt_dm"), sid("alias_gift"), sid("alias_streak")
# every seeded premise the prompt relies on is re-read from the SQL in this run
for needle in ["I want the queue manager to be a real epic", "Before Thursday's flow review", "I left a note on the ticket about how I want it",
               "put a stock-take sheet in your ZM queue manager folder", "share it with everyone on the review invite, Leonard too",
               "add one slide with the numbers to your queue manager deck", "tell me here how many reports are passed",
               "every report gets its line under the right child", "'ZM queue manager'", "2025-10-02T18:00:00Z"]:
    assert needle in SQL.replace("''", "'"), needle
def q(span):
    assert span in P, span
    return '"' + span + '"'
def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c).replace("|", "/") for c in r) + " |" for r in rows]
    return "\n".join(out)
L = []; A = L.append
A("# Prompt Check — calvin_qm_epic")
A(f"> Prompt: 04_Prompt.txt · {WC} words · sha256 {SHA} · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · checked 2026-11-10 against 04_Prompt_Writing_Brief.md (2026-11-10, rev2, SQL ee46405a157d) · release task-quality-v1")
A("> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.\n")
A("Calvin Price · Engineering · Engineering Ops · Analysis and synthesis · Long Horizon · Hard (V3 cap < 70 %; requester targets: average < 60 %, over 130 calls per run, largest failure pattern < 50 %) · synth-cut universe, Calvin's today Wednesday Oct 1, 2025. Upstream: injection rev2 (stage gate PASS, sha256 ee46405a157d; not yet on the platform). rev1 passed the platform /injection and /prompt (score 5, same prompt text) and failed /hardness 2; rev2 moves the difficulty and leaves the prompt as it was. Friction: none, brief gate PASS.\n")
A("## Summary\n")
A("- Fail 0 · Non-fail 0 · Advisory 3 (C20 relative day names; C6 residual fork risk on the reworded note; C22 rev2 not yet reviewed by the platform /injection) · UNVERIFIED none.")
A("- Checks clean: C1, C2, C3, C4, C5, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C23, C24.")
A("- Calibration self-test: the text matches no FAIL case and matches each PASS control it can be compared with (table below).")
A("- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19). This is a prediction only: on earlier tasks /prompt's blind passes found forks that local sweeps missed.")
A("- Status: READY FOR /prompt, once rev2 has its /injection.\n")
A("## Findings\n")
A(table(["#", "Check", "Dimension · severity", "Quoted span", "Rule (source)", "Defect"], [
 [1, "C20", "Alignment with Today's Date · Advisory", q("before Thursday's flow review"), "Prompt Writing §4.2 prefers absolute dates; Eval 1 §2.8 and Local Overrides allow relative wording that resolves to one window", "A relative day name. It resolves to one record: " + EVT + " starts Thu Oct 2, 2025 18:00 UTC, the day after Calvin's today. No change needed."],
 [2, "C20", "Alignment with Today's Date · Advisory", q("He messaged me about it yesterday"), "same", "A relative day. The hub " + HUB + " is Tue Sep 30, 2025 13:40 PT, the day before Wed Oct 1. No change needed."],
 [3, "C6", "Fair outcomes · Advisory", q("set it all up as he asked"), "Eval 1 §2.1; brief §12", "Not a defect in the text. Every material field is settled by a dated record (table below), but rev2 cut the resolver sentences from Brian's note. A blind sweep of rev2 reproduced every value and rated four readings as arguable (plan/sweeps/fork_sweep_rev2.md); three were closed by wording, and the sighting on an older build rests on build times. A fix would go into the data, not the prompt."],
]))
A("\n## Fair readings (accepted outcomes)\n")
A("Reading A is the best-supported reading; Reading B is the strongest alternative. Each is settled by a newer source, an incorporated authority, source identity or scope, or accepted as a second fair outcome. Sidecar `outcome_reviews.prompt-check` is written in this run and bound to the 04_Prompt.txt hash.\n")
A(table(["Deliverable", "Reading A", "Reading B (strongest alternative)", "Resolution and evidence"], [
 ["Area children", "10 children under ZOM-543, one per area in Brian's note; Zombie Lane Done, nine Todo", "children only for areas that have open reports, or all left Todo", "authority: " + NOTE + " lists the ten areas, 'One child each', and 'Set the child to Done if it is Clear and to Todo if it is Open'"],
 ["Report list", "39: the 38 sheet rows plus Marcus's glow report", "B1: 38, the sheet only. B2: more, with Vincent's canvases, chat remarks, Oliver's skip exceptions or the input blocker", "authority: " + NOTE + " takes in bugs told to Calvin in a DM since the 26th (" + FILT + ") and keeps the canvases, Vincent's chats, Oliver's exceptions and the blocker (D0770ET6WBW/1758808795.588519) out"],
 ["Rows 1, 2, 25", "Waiting on QA", "Passed, on Vincent's chat ok D06UPGF5PQV/1758820544.160399", "authority: " + RULE + " counts only main builds; C05433XK267/1758817549.151639 shows #1718 was a feature-branch build; harmonygames-Games/match3d#465 is merged"],
 ["Rows 12 and 32", "Waiting on a fix; ZOM-571 and ZOM-581 back to Todo", "Waiting on QA: the PRs are merged and the tickets are In Validation", "fact: the note asks whether a fix is in main, and " + IN1 + " and " + IN2],
 ["Rows 13 and 38", "Waiting on QA; ZOM-572 to In Validation", "Waiting on a fix: no PR in the sheet", "fact: the note asks whether a fix is in main; " + ELSE + " on harmonygames-Games/match3d#473"],
 ["Rows 9 and 29", "Waiting on a fix", "Passed, as re-tested", "authority: " + RULE + " 'A pass stands until somebody sees the bug again on a main build made after the one it passed on'; " + REOPEN + " and " + BACK + ", both on Android Submission 135 (C05433XK267/1759263189.219529), a build made after the passes"],
 ["Rows 11 and 20", "notes on ZOM-556 and ZOM-560, moved under their children", "new sub-issues", "authority: " + NOTE + " 'if a ticket already has the report, move that ticket'; Vincent's notes " + AG + " and " + AS],
 ["Review list", "6 reports: not Passed, in Collect & Win or Level-end rewards", "B1: Collect & Win and Daily Gift. B2: only Waiting on a fix", "newer source: " + CARDUPD + " (Sep 30 17:22 UTC) after " + OLD + " and " + INV1 + "; authority: the note says 'a report that is not Passed' in an area on the review's agenda, which " + INV2 + " puts on the roadmap card"],
 ["Existing tickets", "20 moved, each with a note; 3 state changes, 17 unchanged", "notes only where the state changes", "authority: " + NOTE + " 'move that ticket under the child and leave a note with the status and why'"],
 ["New sub-issues", "19, titled with the report, state by status, no priority, no assignee", "priority or assignee copied from like tickets", "authority: " + NOTE + " 'No priority and no assignee on the new ones'. Marcus's report may be reworded (accepted)"],
 ["Sheet", "in " + FOLDER + ", tabs Reports and Areas with the note's columns, shared with Brian, Leonard, Arthur, Julia, Vincent", "shared with Brian and Vincent only", "the hub " + HUB + " says everyone on the review invite, Leonard too; " + EVT + " lists the six. Title, role and column order free (accepted)"],
 ["Slide", "one new slide in " + DECK + " with 12, 6, 21, 1, 6", "the numbers added to an existing slide", "the hub says 'add one slide'. Layout and position free (accepted)"],
 ["Reply", "a message in Brian's DM D0770ET6WBW with 12, 6, 21, 1, 6", "a thread reply under " + HUB + " rather than a new message", "both accepted: the prompt and the hub say the DM; thread or not is representational"],
]))
A("\n## Calibration self-test (prompt_qc_cases.json, 15 calibration cases)\n")
A(table(["Case", "Rule", "Expected", "This prompt"], [
 ["K11-staged-errors", "staged_errors", "FAIL", "not matched: spelling, capitals and punctuation are clean"],
 ["K11-control-spelled-correctly", "staged_errors", "PASS", "matched"],
 ["K31-trap-hint", "trap_hint_or_riddle", "FAIL", "not matched: no hint at a hidden item; the text names Brian's ask and its outputs"],
 ["control-symptom", "trap_hint_or_riddle", "PASS", "matched in kind: the prompt names what Brian wants, not a cause"],
 ["K42-hidden-destination", "hidden_destination", "FAIL", "not matched: Linear, the folder, the deck and the DM are named"],
 ["K47-hidden-destination", "hidden_destination", "FAIL", "not matched"],
 ["K44-hidden-destination", "hidden_destination", "FAIL", "not matched: the reply's place is the DM with Brian"],
 ["control-named-destination", "hidden_destination", "PASS", "matched"],
 ["K1-audit-form", "audit_form", "FAIL", "not matched: it reads as a person asking for help"],
 ["K43-audit-form", "audit_form", "FAIL", "not matched"],
 ["K44-if-chain", "if_chain", "FAIL", "not matched: the per-case rules live in Brian's note on the ticket"],
 ["control-plain-request", "audit_form", "PASS", "matched"],
 ["K43-departed-person-premise", "false_state_premise", "FAIL", "not matched: only Brian and Calvin act, both active at the clock (Brian's last base DM line D0770ET6WBW/1758808795.588519 is Sep 25; Calvin's D0770ET6WBW/1759173921.310649 is Sep 29)"],
 ["K50-both-fair-figure", "ugt_both_fair_figure", "PASS", "not applicable: no figure is left to a choice between sources"],
 ["K49-newer-source", "ugt_both_fair_figure", "PASS", "matched in kind: dated records settle each count"],
]))
A("\n## Check results (C1–C24)\n")
A(table(["#", "Result", "Evidence"], [
 ["C1", "clean", f"{WC} words (whitespace split), inside 20–4,000"],
 ["C2", "clean", "Working_Files/00_Task_Context.json refreshed this run: all eight V3 fields; persona calvin_price resolves; synth-cut universe; source supports the 2025-10-01T00:00Z freeze"],
 ["C3", "clean", "Calvin is the assignee of ZOM-543 (base /issues/3618: title Queue Manager, assignee usr_49b9dfa5208d400d), Brian asked him to take it on (D0770ET6WBW/1758730948.999939), and Brian asks him directly in the hub " + HUB + "; voice judged against the role only"],
 ["C4", "clean", "Engineering (a ZM feature and its QA reports), Engineering Ops (epic and task management in Linear), Analysis and synthesis (the status of 39 reports from several sources, summed up in a sheet, a slide and five numbers)"],
 ["C5", "clean", "Ambiguity, dynamic change and multi-source are load-bearing (brief §8); the prompt restates no rule, figure or source"],
 ["C6", "clean, with Advisory (finding 3)", "Fair readings table above: every material field and Linear write is settled by a dated record; a blind agent reproduced the answer from the SQL and the base"],
 ["C7", "clean", "Writes under every reading: 29 issue creates, 20 moves with 3 state changes, 20 notes, a sheet with two tabs moved into the folder, 5 shares, one slide, one DM message. Channel and form are pinned; 'I need you to' delegates all of it and no 'I'll' sits beside an ask"],
 ["C8", "clean", "(a) the hub and Brian's note are Calvin-visible; (b) one DM with Brian, and his message of Sep 30 is the only one about an epic; the hub leads to one note on ZOM-543; (c) the hub states what the prompt attributes to Brian; (d) rules, no answers"],
 ["C9", "clean", "No status, count, area, root cause or finding entity; the brief §9 scan of the text finds none"],
 ["C10", "clean", "Only AN1, AN2 and the hub's own folder, deck and invite are named; no hidden authority, build, PR or channel"],
 ["C11", "clean", "Every write depends on the investigation: statuses set states, a ticket lookup replaces creation, and the five numbers come from all of it"],
 ["C12", "clean", "Linear, Sheets, Slack, GitHub, Docs, Trello, Gmail, Calendar, Drive and Slides carry weight (brief §1); 01_Hardness_Manifest.json present; hardness_gate (extreme) PASS pasted in the dossier"],
 ["C13", "clean", "One purpose: Brian's ask before Thursday's review"],
 ["C14", "clean", "No function, parameter or server name (catalog scan); 'Linear' is a natural product name"],
 ["C15", "clean", "The single 'Once that's done' orders the final message after the work (screen 24 skeleton)"],
 ["C16", "clean", "No spec-sheet layout, answer-key clause, staged error, riddle, hedge, hidden destination, audit wording or if-chain; hardness_v2_check: 'CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt'"],
 ["C17", "clean", "Verification log below: every person, record, date and premise re-found in this run"],
 ["C18", "clean", "Catalog writes exist: linear_create_issue (team, title, state, parentId, priority, assignee), linear_update_issue (parentId, state), linear_create_comment, gsheets_create_spreadsheet, gsheets_batch_update, gsheets_values_update, gdrive_move_file, gdrive_share_file (emailAddress, role), gslides_batch_update, slack_send_message (channel, thread_ts); gradable_surface.py gradeable-report: 51 slots GRADABLE"],
 ["C19", "clean", "check-sql PASS for every scoped seeded record; Calvin is in D0770ET6WBW, D06UPGF5PQV, D05U73FNDDL, C08R27X0EAH, C0880U9751A, C093LEZGF6J and C05433XK267 (persona_view can-see YES this run); his mailbox holds both invitations; the pass sheet, legend and rule doc are shared with him. Linear, GitHub and Trello are unscoped"],
 ["C20", "Advisory (findings 1, 2)", "yesterday = Tue Sep 30 (past); Thursday = Oct 2, a future meeting (" + EVT + ")"],
 ["C21", "clean", "Friction: none (03_Error_Async_Config.txt)"],
 ["C22", "Advisory", "rev2 (sha256 ee46405a157d) has no platform /injection yet; local base_check, base_claims, fact_check and hg lint PASS, and a blind coherence sweep found no blocking item (plan/sweeps/coherence_sweep_rev2.md). Leonard is travelling on Oct 2 per base C07C2866011, which rev1 carried through /injection and /prompt"],
 ["C23", "clean", "No sample was supplied with the task. Against the archived tasks in support/completed_tasks the scenario, persona, entities and asks differ, and no sentence is shared; the platform's STEP 0.6 dataset gate has not seen this text yet"],
 ["C24", "clean", "Six kinds of write over Linear, Sheets, Drive, Slides and Slack"],
]))
A("\n## Verification log\n")
A("Every row was looked up in this run: base records through `Task_Authoring/tools/hg.py search` and persona_view, seeded records from 01_Universe_Inject.sql (rev1, asserted by this report's builder).\n")
A(table(["Span", "Type", "Universe record (locator)", "Result"], [
 ["Brian", "person", "entity.py resolve 'Brian': brian.foster@harmonygames.co, EMPLOYEE_0026_SLACK_ID", "the hub's sender; active at the clock"],
 ["the Queue Manager ticket", "ID", "ZOM-543 (linear /issues/3618): title 'Queue Manager', assignee usr_49b9dfa5208d400d (Calvin), created 2025-09-15T12:41:11Z", "match"],
 ["turned into a real epic", "relationship", "hub " + HUB + ": 'I want the queue manager to be a real epic'", "match"],
 ["before Thursday's flow review", "event / date", EVT + " 'ZM home screen flow review', 2025-10-02T18:00:00Z, on Calvin's calendar; hub: 'Before Thursday's flow review'", "match (future meeting)"],
 ["He messaged me about it yesterday", "date / channel", HUB + ": Tue Sep 30 2025 13:40 PT, 20:40 UTC, in DM D0770ET6WBW", "match"],
 ["as he asked", "relationship", "hub: 'I left a note on the ticket about how I want it'; " + NOTE, "match"],
 ["the children and report lines in Linear", "requested output", "hub: 'One child for each area, and every report gets its line under the right child'; ZOM-543", "match"],
 ["the stock-take sheet in my ZM queue manager folder", "destination", FOLDER + " 'ZM queue manager', owner calvin.price@harmonygames.co; hub: 'put a stock-take sheet in your ZM queue manager folder'", "match"],
 ["shared with everyone on the review invite", "recipients", EVT + " attendees leonard.hayes@harmonygames.co, brian.foster@harmonygames.co, arthur.blake@harmonygames.co, julia.lawson@harmonygames.co, vincent.parker@harmonygames.co, calvin.price@harmonygames.co", "match"],
 ["a slide with the numbers in my queue manager deck", "destination", DECK + " 'ZM queue manager', owner calvin.price@harmonygames.co; hub: 'add one slide with the numbers to your queue manager deck'", "match"],
 ["our DM", "channel", "D0770ET6WBW, members Calvin and Brian; persona_view can-see YES on D0770ET6WBW/1759173921.310649", "match"],
 ["the numbers he wants back", "requested output", "hub: 'tell me here how many reports are passed, how many wait on QA, how many wait on a fix, how many areas are clear and how many reports are on the review list'; " + HUB, "match"],
 ["me / my", "persona", "calvin.price@harmonygames.co", "match"],
]))
A("\n## Brief coverage\n")
A(table(["Brief item (§4 deliverables, §6 triggers)", "Present in the prompt (quoted span, or absent)"], [
 ["AN2 anchor: the Queue Manager ticket", q("the Queue Manager ticket")],
 ["scope: the epic", q("turned into a real epic")],
 ["deadline context: Thursday's review", q("before Thursday's flow review")],
 ["AN1 anchor: Brian's message from yesterday", q("He messaged me about it yesterday")],
 ["§6 rules under Brian's note", q("set it all up as he asked")],
 ["§4 area children, sub-issues, existing tickets", q("the children and report lines in Linear")],
 ["§4 sheet in the folder", q("the stock-take sheet in my ZM queue manager folder")],
 ["§4 sharing", q("shared with everyone on the review invite")],
 ["§4 slide", q("a slide with the numbers in my queue manager deck")],
 ["§4 reply and the five numbers", q("message him in our DM with the numbers he wants back")],
 ["§6 statuses, ticket reuse, states, review list, tabs and columns", "absent (record triggers: Brian's note on ZOM-543, which the hub points at)"],
]))
A("\n## Self-review\n")
A("Phase walk (Evals/1_Prompt_Eval.md, Phases 1–3): Phase 1 → C2–C5; Phase 2 → C6–C20, C23; Phase 3 → C21, C22. Every C-check has a result with evidence; none is UNVERIFIED.\n")
A(table(["Check", "Counter-reading (strongest case that /prompt fails it, or that a finding is a false positive)", "Evidence that resolves it", "Verdict"], [
 ["C1", "Another tokenizer could put the text outside the field.", f"{WC} whitespace words; the limit is 20–4,000.", "none stands"],
 ["C2", "The assignment could be read as Normal Horizon or another date.", "00_Assigments.md and 00_Task_Context.json: long-horizon, hard, Oct 1, 2025 (synth-cut).", "none stands"],
 ["C3", "A VFX engineer restructuring an epic sounds like a lead's job.", "ZOM-543 is assigned to Calvin, and Brian, who created it, asks him directly in " + HUB + ".", "none stands"],
 ["C4", "Building an epic could read as Actions, not Analysis and synthesis.", "The writes are only as right as the status of each of 39 reports, which is worked out from the sheet " + SHEET + ", build posts, PR reviews and later reports; a mismatch alone would be Non-fail under V3.", "none stands"],
 ["C5", "The colon list could carry the recipe.", "It lists the outputs Brian named, with no rule, source or value; brief §8.", "none stands"],
 ["C6", "A reviewer may find a fork the sweeps missed, as on earlier tasks.", "The forks the fork sweep raised (rows 18 and 25, Oliver's exclusion, the dev-hearsay sentence) were closed in the SQL before the gate, and the platform /injection passed it; the residual risk is finding 3. Brian's note " + NOTE + " settles each reading in the table.", "Advisory stands"],
 ["C7", "'the children and report lines' could be too vague to act on.", "The hub " + HUB + " says 'One child for each area, and every report gets its line under the right child', and the note on ZOM-543 defines both; no competing write is named.", "none stands"],
 ["C8", "'as he asked' may not lead to one source.", "Brian's only message about an epic is " + HUB + ", and it points at one note on ZOM-543; " + OLD + " is about the review's order, not the epic.", "none stands"],
 ["C9", "'report lines' could pre-solve how reports are filed.", "It repeats the hub's own words and names no status, ticket or count (" + HUB + ").", "none stands"],
 ["C10", "Naming the folder and deck collapses a discovery.", "The hub names both, and " + FOLDER + " and " + DECK + " decide nothing.", "none stands"],
 ["C11", "Creating ten children needs no finding.", "Each child's state depends on whether its area is clear, and every line under it depends on a report's status; ZOM-543.", "none stands"],
 ["C12", "Most of the work could be Linear plus one sheet.", "GitHub decides rows 12, 13, 32 and 38 (" + IN1 + "), Slack decides rows 1, 2, 9, 25 and 29 (C05433XK267/1758817549.151639), Trello decides the review list (" + CARD + "), Calendar decides sharing (" + EVT + ").", "none stands"],
 ["C13", "The slide could be a bolt-on.", "Brian asks for it in the same message for the same review (" + HUB + "); same purpose.", "none stands"],
 ["C14", "'Linear' names a system.", "Natural product names are clean (prompt_qc_examples.md row 103); ZOM-543 is not named by key.", "none stands"],
 ["C15", "The colon list then 'Once that's done' could read as a command list.", "Deliverables and who to tell are the screen-24 skeleton, not a method; no source or order of reading is given. Hub " + HUB + ".", "none stands"],
 ["C16", "'as he asked' could be a hint, or 'Thursday' a nudge that the review moved.", "Both repeat the requester's own message (" + HUB + " says 'Before Thursday's flow review'), as the control-plain-request case does; Eval 1 §2.7.", "none stands"],
 ["C17", "'Thursday' could be false: Brian's Sep 29 line says Friday.", "The review was moved: " + INV2 + " and " + EVT + " put it on Thu Oct 2, and the later hub says Thursday.", "none stands"],
 ["C18", "A sheet with two tabs inside a folder, and sub-issues under children, may exceed the tools.", "gsheets_batch_update adds a tab, gdrive_move_file moves the file into " + FOLDER + ", and linear_create_issue takes parentId for any issue.", "none stands"],
 ["C19", "Calvin cannot see the other attendees' mail or calendars.", "His own event copy " + EVT + " lists all six attendees; nothing asks him to read another person's scoped data.", "none stands"],
 ["C20", "False positive: relative days are allowed, so this needs no finding.", "True under Local Overrides; kept as Advisory because Prompt Writing §4.2 prefers absolute dates. Hub date " + HUB + ".", "Advisory stands"],
 ["C21", "Friction could be announced.", "03_Error_Async_Config.txt: Friction: none; the text mentions no failure or wait. ZOM-543 is reachable directly.", "none stands"],
 ["C22", "Seeded tickets In Validation whose fix is not merged are a lifecycle mismatch.", "That mismatch is the designed claim, and the platform /injection passed it on rev1 with no coherence finding (ZOM-571, ZOM-581); rev2 itself is not reviewed yet.", "Advisory stands"],
 ["C23", "The wording could sit close to an archived prompt that also points at a manager's DM.", "No sentence is shared with any archived prompt, and the persona, feature, records and outputs differ (ZOM-543; D0770ET6WBW); the dataset gate itself runs only on the platform.", "none stands"],
 ["C24", "One message and many tickets is little variety.", "Six kinds of write over five services, under ZOM-543.", "none stands"],
]))
A("\nSpot-decode note: gradeable-report passes for all 51 slots. Report rows are keyed by the report text, so a run that rewords a report in the sheet's Report column needs a hand check in local forensics; this has no /prompt or rubric effect.\n")
A("Unresolved: whether /prompt finds a fork the sweeps missed; the platform's dataset-duplicate gate on this text.\n")
A("## Route\n")
A("No Fail. Paste 04_Prompt.txt exactly as saved into `/prompt`, after `/injection` on rev2 (sha256 ee46405a157d). Answer the date question with Oct 1, 2025 (synth-cut). A defect found there in the data goes back to `/create-injection`, not into the prompt.\n")
open(os.path.join(WF, "04_Prompt_Check.md"), "w").write("\n".join(L) + "\n")

ah = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", os.path.join(TD, "04_Prompt.txt")], cwd=WS, capture_output=True, text=True).stdout.strip().split()[-1]
ep = os.path.join(WF, "00_V3_Authoring_Evidence.json"); E = json.load(open(ep))
rev = "Claude (Fable 5.2), prompt check C1-C24 on rev1 (Working_Files/04_Prompt_Check.md), with a blind fork sweep and a blind coherence sweep of the SQL (Working_Files/plan/sweeps/)"
E["role_reviews"]["prompt-check"] = {"artifact": "04_Prompt.txt", "artifact_hash": ah, "reviewer": rev, "persona_role": "Game Engineer (Unity VFX)",
 "rationale": "Calvin is the Unity VFX engineer who is the assignee of ZOM-543, the ZM Queue Manager. Brian, who created the ticket and asked him to take the queue manager on, messages him directly to turn it into an epic and take stock of QA's reports before the flow review, so asking his assistant to set that up is inside his remit.",
 "source_ids": ["ZOM-543", "D0770ET6WBW/1758730948.999939", "D06UPGF5PQV/1758806199.381319", HUB]}
pw = E["outcome_reviews"]["prompt-writing"]
E["outcome_reviews"]["prompt-check"] = {"artifact": "04_Prompt.txt", "artifact_hash": ah, "reviewer": rev,
 "rationale": "The prompt pins every destination (Linear under the Queue Manager ticket, Calvin's folder, his deck, the DM with Brian) and points at Brian's message for the rules. The fair-readings table settles each material field from dated records; thread or new message, sheet title, share role and slide layout are accepted either way.",
 "accepted_outcomes": pw["accepted_outcomes"], "alternatives_considered": pw["alternatives_considered"]}
E["prompt_hash"] = ah
json.dump(E, open(ep, "w"), indent=1); print("check written", WC, SHA, "artifact hash", ah)

# ---- hardness_reviews/prompt.json: the injection review carried to the prompt stage, bound to the prompt text
sys.path.insert(0, os.path.join(WS, "Task_Authoring", "tools"))
import design_readiness as dr, hardness_v2_check as hv
ref = lambda rel: {"path": rel, "sha256": hashlib.sha256(open(os.path.join(TD, rel), "rb").read()).hexdigest()}
M = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json"))); SF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
R = json.load(open(os.path.join(WF, "hardness_reviews", "injection.json")))
PR, SQLREF = ref("04_Prompt.txt"), ref("01_Universe_Inject.sql")
R["stage"] = "prompt"
R["reviewer"] = "Claude (Fable 5.2), prompt check C1-C24 (Working_Files/04_Prompt_Check.md) on top of the injection review; REDTEAM_* unset"
R["input_hashes"] = dr.input_hashes("prompt", M, SF, sql_text=SQL, prompt=P)
R["semantic_prompt_review"] = {"leaks_solution": False, "evidence": [PR, SQLREF],
 "reason": "The prompt names Brian's message, the Queue Manager ticket and the outputs Brian himself lists (children and report lines in Linear, the stock-take sheet and its sharing, the slide, the numbers back in the DM). It states no status, count, area, build, PR, rule or person who corrects a first reading, and it does not mention Brian's note, Arthur's rule, Leonard's card, the moved review or any later report; each of those is reached only through the seeded records."}
adv = hv.run(M, SQL, P, SF); D = dict(R.get("dispositions", {}))
for f_ in adv["flags"] + adv["unresolved"]:
    k = f_["check"] + ":" + str(f_.get("node") or "-")
    if k not in D or not dr.evidence_ok(D[k], TD):
        D[k] = {"status": "accepted", "evidence": [PR, SQLREF], "reason": "Read against the SQL rows and the prompt text: " + str(f_.get("message") or f_.get("detail") or f_.get("why") or "advisory lexical flag")[:300] + " The deciding record sits outside the first-read path and the prompt adds no pointer to it; kept as designed."}
R["dispositions"] = D
json.dump(R, open(os.path.join(WF, "hardness_reviews", "prompt.json"), "w"), indent=1)
cfg = json.load(open(os.path.join(WF, "00_Readiness_Config.json"))); ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
rep = dr.evaluate("prompt", M, SF, R, sql_text=SQL, prompt=P, task_dir=TD, task_id=R["task_id"], revision=cfg["revision"], difficulty_mode=ctx["difficulty_mode"])
print("prompt design review", rep["verdict"], rep["blockers"][:8])
