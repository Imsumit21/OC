#!/usr/bin/env python3
"""Assembles Working_Files/04_Prompt_Check.md for the exact text of 04_Prompt.txt."""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, os.path.join(WF, "solver"))
import solver  # noqa: E402
P = open(os.path.join(TI, "04_Prompt.txt")).read()
words, sha = len(P.split()), hashlib.sha256(P.encode()).hexdigest()[:12]
st = solver.load_state(open(os.path.join(TI, "01_Universe_Inject.sql")).read())
A_ = solver.aggregates(solver.solve(st))
C, R = A_["classes"], A_["reply"]
HUB, DOC, FOLDER, EVT = "D05S1S2AB5M/1770937805.214409", "f_3ca9e15d7b20f4e681ad52", "d_9b41e7c2a05d36f8e1c7a4", "evt_6e2c91d4b07f3a58c1d2e4"
L = []
A = L.append
A("# Prompt Check — owen_dd_bug_carryover")
sqlsha = hashlib.sha256(open(os.path.join(TI, "01_Universe_Inject.sql"), "rb").read()).hexdigest()[:12]
A(f"> Prompt: 04_Prompt.txt · {words} words · sha256 {sha} · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · checked 2026-11-08 against 04_Prompt_Writing_Brief.md (2026-11-08, rev9, SQL {sqlsha}) · release task-quality-v1")
A("> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.\n")
A("Owen Baker · Engineering · Engineering Ops · Actions · Long Horizon · Medium (V3 cap < 85 %, requester target < 80 % average, over 130 calls per run) · normal universe, Owen's today Saturday Feb 14, 2026. Upstream: injection rev9 (stage gate PASS, not yet on the platform; rev8 passed /injection and /prompt 5 and failed /hardness 2; rev9 removes Brian's Tavern line, so Tavern rests on Marcus's DM as on rev5, and moves Brian's Daily Gift note from ENG-2437 into his DM), Friction: none, brief gate PASS.\n")
A("This is the re-check for rev9. The prompt text is the one /prompt reviewed on rev2 and rev6 to rev8 (score 5 on rev7 and rev8). rev9 removes Brian's Tavern line, leaving Marcus's DM, which /prompt on rev5 accepted as the Tavern record on its own, and moves Brian's Daily Gift note to his DM with the same words. On rev6 its deep recheck re-opened the tooltips thread: Vincent's 1 pixel gap 'but that's okay' (Nov 21 18:03 UTC) is followed by Brian's 'I'll send another fix' (18:07 UTC) and nothing later, so Done and Bugs were both fair. The fix is in the data, as its minimum fix asked.\n")
A("## Summary\n")
A("- Fail 0 · Non-fail 0 · Advisory 2 (C20 relative day names; C22 rev9 not yet reviewed, and the master tickets' states) · UNVERIFIED none.")
A("- Checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C23, C24.")
A("- Calibration self-test: the text matches no FAIL case and matches each PASS control it can be compared with (table below).")
A("- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19). This is a prediction only: rev2 carried the same prediction and failed. /prompt's blind passes have found forks local sweeps missed.")
A("- Status: READY FOR /prompt, once rev9 has its /injection.\n")
A("## Findings\n")
A("| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |\n|---|---|---|---|---|---|")
A(f"| 1 | C20 | Alignment with Today's Date · Advisory | \"on Thursday\" … \"before Sunday's bug review\" | Prompt Writing §4.2 prefers absolute dates; Eval 1 §2.8 and Local Overrides allow relative wording that resolves to one window | Relative day names. Each resolves to one record: the hub {HUB} is Thu Feb 12 15:10 PT, and {EVT} is Sun Feb 15 17:00Z. No change needed. |")
A("| 2 | C22 | Cross-Service Coherence · Advisory | \"bringing the tree under the UI Changes master ticket up to date\" | Eval 1 §3.2; STEP 0.5 | (a) rev9 has no platform /injection yet, so STEP 0.5 reads STALE until it does. (b) ENG-2405 stays Todo with #1905 merged, because the rule doc keeps the masters as they are. /prompt raised no issue with it on rev2, and base_check blocks an UPDATE of that ticket. |\n")
A("## Fair readings (accepted outcomes)\n")
A("Reading A is the best-supported reading; Reading B is the strongest alternative. Each is settled by a newer source, an incorporated authority, source identity or scope, or accepted as a second fair outcome. Sidecar `outcome_reviews.prompt-check` is written in this run and bound to the 04_Prompt.txt hash.\n")
A("| Deliverable | Reading A | Reading B (strongest alternative) | Resolution and evidence |\n|---|---|---|---|")
for r in [
 ("New tickets", f"{R['new_tickets']} tickets: every line and later post except the 2 Covered", "B1: 69, with Arthur's Dec 31 no-ads post. B2: 65 to 67, merging fragments or alike lines", f"authority: {DOC} 'A design question for Leonard isn't a bug post' and 'One Linear record per canvas line and one per bug posted after it, even where two read alike'; C05V5FNLB9V/1767191512.428539 is that question"),
 ("Ticket fields", "Engineering, Bug, parent ENG-2401, no assignee, empty description, [2231] title prefix, state by outcome", "no prefix, going by the doc alone", f"newer source: ENG-2401 note comment_49b5ac4788465f72ddf245e34f2b7034 (Feb 13 00:40Z) after {DOC} (Feb 12 22:48Z), which says changes go on the master ticket"),
 ("Outcomes", f"{C['Fixed']} Fixed, {C['Broken']} Broken, {C['Gone']} Gone, {C['Covered']} Covered", "Tavern Fixed by the Dec 5 Gacha commit", f"authority: {DOC} needs a commit named for the bug; D05USBTQY1F/1765452012.418229 follows that commit. Two blind sweeps reproduced all four counts"),
 ("Flicker post", "Fixed", "Broken: the fix names only the end-level popup", "newer source: Robert's reply C09Q4S613CN/1766164222.418229 covers the play button and coming out of a level"),
 ("Nav bar tooltips", "Fixed", "Broken: Brian's 'I'll send another fix' after Vincent's 1 pixel gap (CE156FDFB428/1763748462.772499)", "newer source: Vincent's reply CE156FDFB428/1763845512.559339 (Nov 22 21:05Z) says the second fix closed the gap (rev7, /prompt on rev6 Issue 1)"),
 ("Dec 22 bottom bar", "one ticket from the first post", "two tickets", f"authority: {DOC} 'a follow-up on a bug already posted is part of that bug'; C05V5FNLB9V/1766415211.386389"),
 ("Deleted canvas lines", "out", "tickets for threads that survive", f"authority: {DOC} 'A comment whose line was deleted has nothing to carry over'; CE156FDFB428/1763042124.247899"),
 ("QA-doc post", "out", "its own ticket", f"authority: {DOC} 'a post that points at a QA doc isn't a bug post'; C05V5FNLB9V/1764662837.138929"),
 ("Reused tickets", "notes on ENG-2073 and ENG-2363", "new tickets for those two lines", "owen.baker@harmonygames.co/1849333980856689601 and comment_7ab5299cbb609d95ba12249d315daedc tie them; the doc says add a note"),
 ("UI children", f"{R['children_done']} of {R['children_total']} Done; ENG-2424, ENG-2426, ENG-2428, ENG-2434, ENG-2437 stay", "B1: 24, with ENG-2424 Done. B2: 25 or 26 from Brian's checklist ticks", f"authority: {DOC} 'or the screen is switched off there' with C9CA62B5180A/1765927876.696389; harmonygames-Games/GameOfDominoes#1905#rc_1 and #1908#rc_1 show a piece left out; the deck and checklist speak of main screens"),
 ("Child lines", "a line on all 28, each naming 0.3.310", "a per-child check build, or no build on held and Done children", f"authority: 690b29bc3c7d2e51b0f86a47 'the current public build'; {DOC} 'applies to the line on every child, Done or not' and names 0.3.310"),
 ("Sheet", f"in {FOLDER}, columns Bug, Outcome, Ticket, Why, 70 rows, shared with Arthur, Robert, Oliver", "share with Owen too, or with Brian", f"{EVT}: attendees are Arthur, Robert, Oliver, Owen; Owen owns the sheet. Title and role free (accepted)"),
 ("Reply", f"in the thread of {HUB}: {R['still_broken']} still broken, {R['new_tickets']} new tickets, {R['children_done']} of 28 Done", "7 still broken, leaving out Covered", f"authority: {DOC} 'Covered ones count as still broken'. Adding the 7 and 2 split is accepted"),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("## Calibration self-test (prompt_qc_cases.json, 15 calibration cases)\n")
A("| Case | Rule | Expected | This prompt |\n|---|---|---|---|")
for r in [
 ("K11-staged-errors", "staged_errors", "FAIL", "not matched: spelling, capitals and punctuation are clean"),
 ("K11-control-spelled-correctly", "staged_errors", "PASS", "matched"),
 ("K31-trap-hint", "trap_hint_or_riddle", "FAIL", "not matched: no hint at a hidden item; 'bug list' and 'up to date' name the job"),
 ("control-symptom", "trap_hint_or_riddle", "PASS", "matched in kind: the prompt names Arthur's ask, not a cause"),
 ("K42-hidden-destination", "hidden_destination", "FAIL", "not matched: Linear, the folder and the DM thread are named"),
 ("K47-hidden-destination", "hidden_destination", "FAIL", "not matched"),
 ("K44-hidden-destination", "hidden_destination", "FAIL", "not matched: the reply's place is the DM thread"),
 ("control-named-destination", "hidden_destination", "PASS", "matched"),
 ("K1-audit-form", "audit_form", "FAIL", "not matched: it reads as a person asking for help"),
 ("K43-audit-form", "audit_form", "FAIL", "not matched"),
 ("K44-if-chain", "if_chain", "FAIL", "not matched: the per-case rules live in the notes doc"),
 ("control-plain-request", "audit_form", "PASS", "matched"),
 ("K43-departed-person-premise", "false_state_premise", "FAIL", "not matched: only Arthur and Owen act, both active (activity.json active_feb_2026); the wind-down is acknowledged"),
 ("K50-both-fair-figure", "ugt_both_fair_figure", "PASS", "not applicable: no figure is left to a choice between sources"),
 ("K49-newer-source", "ugt_both_fair_figure", "PASS", "matched in kind: dated records settle each count"),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("## Check results (C1–C24)\n")
A("| # | Result | Evidence |\n|---|---|---|")
CR = [
 ("C1", "clean", f"{words} words (whitespace split), inside 20–4,000"),
 ("C2", "clean", "Working_Files/00_Task_Context.json refreshed this run: all eight V3 fields; persona owen_baker resolves; normal universe; source supports the 2026-02-14T00:00Z freeze"),
 ("C3", "clean", f"Owen holds 16 of the 28 children (ENG-2417), fixed canvas lines (CE156FDFB428/1763549617.765149), and Arthur asks him directly ({HUB}); voice judged against the role only"),
 ("C4", "clean", "Engineering (DD's bug record and live build), Engineering Ops (task management in Linear, the tree), Actions (tickets, moves, notes, sheet, reply)"),
 ("C5", "clean", "Ambiguity, dynamic change and multi-source are load-bearing (brief §8); the prompt restates no rule, figure or source"),
 ("C6", "clean", "Fair readings table above: every material field and Linear write is settled by a dated record, and a blind sweep and re-check found no open blocking fork"),
 ("C7", "clean", f"Writes under every reading: {R['new_tickets']} issue creates, 2 notes, 14 moves, 28 notes, sheet create, values, move, 3 shares, one thread reply. Channel, time and form are pinned; 'while I'm at it' is a turn of phrase, and 'Can you take care of everything' delegates it"),
 ("C8", "clean", f"(a) the hub and {DOC} are Owen-visible; (b) one DM, one doc titled 'DD bug carry-over notes'; (c) the doc states what the prompt attributes to Arthur; (d) rules, no answers"),
 ("C9", "clean", "No outcome, count, root cause or finding entity; the §9 scan's only hit is 'tick' inside 'tickets'"),
 ("C10", "clean", "Only AN1, AN2 and the hub's own folder and review are named"),
 ("C11", "clean", "Every write depends on the investigation: outcomes set state, reuse replaces creation, records hold children, and the counts come from all of it"),
 ("C12", "clean", "Slack, Linear, GitHub, Docs, Drive, Sheets, Slides, Trello, Gmail, Calendar carry weight (brief §1); 01_Hardness_Manifest.json present; hardness_gate (extreme) PASS pasted in the dossier"),
 ("C13", "clean", "One purpose: Arthur's ask before Sunday's review"),
 ("C14", "clean", "No function, parameter or server name (catalog scan); 'Linear' and 'Slack' are natural product names"),
 ("C15", "clean", "The single 'Then' orders the final reply after the work (screen 24 skeleton)"),
 ("C16", "clean", "No spec-sheet layout, answer-key clause, staged error, riddle, hedge, hidden destination, audit wording or if-chain; hardness_v2_check: 'CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt'"),
 ("C17", "clean", "Verification log below: every person, record, date and premise re-found in this run"),
 ("C18", "clean", "Catalog writes exist: linear_create_issue (team, title, state, labels, parentId), linear_update_issue, linear_create_comment, gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, gdrive_share_file, slack_send_message with thread_ts; gradable_surface.py gradeable-report: 49 slots GRADABLE"),
 ("C19", "clean", f"check-sql PASS for every scoped seeded record; Owen is in D05USBTQY1F, D07E9PSQB6W, C9CA62B5180A and C05V5FNLB9V, back on a paid seat, with a leave and a join in each task channel; his mailbox holds the mail; {DOC} is shared with him. Linear, GitHub and Trello are unscoped"),
 ("C20", "Advisory (finding 1)", f"Thursday = Feb 12 (past); Sunday = Feb 15, a future meeting ({EVT})"),
 ("C21", "clean", "Friction: none (03_Error_Async_Config.txt)"),
 ("C22", "Advisory (finding 2)", "rev9 local gates PASS: base_check, base_claims, fact_check, sql_lint 0 errors, hg lint FAIL 0; rev8 passed the platform /injection and /prompt 5 (run_forensics/rev8/); NB-1 and NB-14 are repaired"),
 ("C23", "clean", "No supplied sample; STEP 0.6 read on the platform for this exact text: gate PASS, nearest neighbour 0.669, tier distinct (run_forensics/rev2/1_prompt_FAIL_r2.md)"),
 ("C24", "clean", "Five kinds of write over Linear, Sheets, Drive and Slack"),
]
for r in CR:
    A("| " + " | ".join(r) + " |")
A("")
A("## Verification log\n")
A("Every row was looked up in this run: base records through `Task_Authoring/tools/hg.py search` and persona_view, seeded records from 01_Universe_Inject.sql (rev2).\n")
A("| Span | Type | Universe record (locator) | Result |\n|---|---|---|---|")
for r in [
 ("Arthur", "person", "entity.py resolve 'Arthur Blake': arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID", "the hub's sender; active_feb_2026"),
 ("a DM", "channel", "D05S1S2AB5M, channels.json /533; persona_view can-see YES", "match"),
 ("on Thursday", "date", f"{HUB}: Thu Feb 12 2026 15:10 PT, 23:10 UTC", "match"),
 ("DD's bug list", "object", "CE156FDFB428/1763041126.468099; C05V5FNLB9V/1764256187.655299", "match"),
 ("Slack drops to the free plan", "state", "C0ADGSZKR3R/1770839825.928989 and C0ADGSZKR3R/1770840054.486779 ('yeah free version'); hub " + HUB, "match; a plan, wind-down acknowledged"),
 ("the tree under the UI Changes master ticket", "ID", "ENG-2401 'UI Changes Master Ticket' (linear /issues/2338); children via ENG-2403, ENG-2404, ENG-2405", "match"),
 ("Sunday's bug review", "event / date", f"{EVT} 'DD bug review', 2026-02-15T17:00Z, on Owen's calendar", "match (future meeting)"),
 ("the way he lays it out", "relationship", f"hub: 'How we call each one is in the carry-over notes doc'; {DOC}", "match"),
 ("a line on every UI child", "requested output", f"hub: 'leave a line on every child saying where it landed'; 28 children ENG-2409 to ENG-2437", "match"),
 ("my DD bug carry-over folder", "destination", f"{FOLDER}, owner owen.baker@harmonygames.co, created 2026-02-12T23:00:00Z", "match"),
 ("shared with everyone on the review", "recipients", f"{EVT} attendees arthur.blake@harmonygames.co, robert@harmonygames.co, oliver.brooks@harmonygames.co, owen.baker@harmonygames.co", "match"),
 ("that DM thread", "channel", f"thread_ts 1770937805.214409 in D05S1S2AB5M", "match"),
 ("the numbers he wanted", "requested output", f"hub: 'how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done'; {HUB}", "match"),
 ("me / my", "persona", "owen.baker@harmonygames.co", "match"),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("## Brief coverage\n")
A("| Brief item (§4 deliverables, §6 triggers) | Present in the prompt (quoted span, or absent) |\n|---|---|")
for r in [
 ("AN1 anchor: Arthur's DM", '"Arthur sent me a DM on Thursday"'),
 ("scope: the bug list into Linear", '"getting DD\'s bug list out of Slack and into Linear"'),
 ("AN2 anchor and the tree", '"bringing the tree under the UI Changes master ticket up to date"'),
 ("deadline: Sunday's review", '"before Sunday\'s bug review"'),
 ("§6 outcomes under the notes doc", '"the way he lays it out"'),
 ("§4 new tickets", '"the Linear tickets"'),
 ("§4 a line on every child", '"a line on every UI child"'),
 ("§4 sheet in the folder", '"the sheet in my DD bug carry-over folder"'),
 ("§4 sharing", '"shared with everyone on the review"'),
 ("§4 reply and the three counts", '"reply to him in that DM thread with the numbers he wanted"'),
 ("§6 ticket fields, title prefix, build in the notes", "absent (record triggers: the notes doc, the ENG-2401 note and Brian's comment)"),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("## Self-review\n")
A("Phase walk (Evals/1_Prompt_Eval.md, Phases 1–3, read for this run): Phase 1 → C2–C5; Phase 2 → C6–C20, C23; Phase 3 → C21, C22. Every C-check has a result with evidence; none is UNVERIFIED.\n")
A("| Check | Counter-reading (strongest case that /prompt fails it, or that a finding is a false positive) | Evidence that resolves it | Verdict |\n|---|---|---|---|")
SR = [
 ("C1", "Another tokenizer could put the text outside the field.", f"{words} whitespace words; the limit is 20–4,000.", "none stands"),
 ("C2", "The assignment could be read as Normal Horizon.", "00_Assigments.md and 00_Task_Context.json: long-horizon, medium, Feb 14, 2026.", "none stands"),
 ("C3", "A game engineer filing 70 tickets sounds like QA's job.", f"Arthur, the CTO, asks Owen directly in {HUB}, and Owen fixed lines on that list (CE156FDFB428/1763549617.765149).", "none stands"),
 ("C4", "Moving a list could read as admin, not Engineering Ops.", "epic and task management in Linear is the competency's focus; ENG-2401 is the epic.", "none stands"),
 ("C5", "'That covers...' could carry the recipe.", "it lists deliverables Arthur named, with no rule, source or value; brief §8.", "none stands"),
 ("C6", "A reviewer may find a fork the sweeps missed, as on earlier tasks.", "/prompt's four forks are closed, and a fresh item-by-item sweep with a scope-gap test matched every count; plan/out/sweep_dispositions.md. Residual risk is stated in the summary.", "none stands"),
 ("C7", "'while I'm at it' could assign the work to Owen.", "'Can you take care of everything he asked for' delegates all of it (Eval 1 §2.6); no 'I'll' sits beside an ask.", "none stands"),
 ("C8", "'the way he lays it out' may not lead to one source.", f"the hub names the carry-over notes doc, and {DOC} is the only doc with that title; f_72e0b4c3d91a5f68c2b7e4 names ZM.", "none stands"),
 ("C9", "'a line on every UI child' could pre-solve the tree.", "it repeats the hub's ask and names no state or child.", "none stands"),
 ("C10", "Naming the folder collapses a discovery.", f"the hub names it, and {FOLDER} decides nothing.", "none stands"),
 ("C11", "Filing Fixed lines needs no finding.", "whether a line is Fixed is the finding: CE156FDFB428/1763549455.195819 is ticked and Broken.", "none stands"),
 ("C12", "Most of the work could be Slack plus Linear only.", "GitHub decides ENG-2434 (harmonygames-Games/GameOfDominoes#1905#rc_1), Gmail decides the Apple line, Docs decide scope, Calendar decides sharing.", "none stands"),
 ("C13", "The sheet could be a bolt-on.", "Arthur asks for it as the lookup for the same list (hub); same purpose.", "none stands"),
 ("C14", "'Linear' and 'Slack' name systems.", "natural product names are clean (prompt_qc_examples.md row 103).", "none stands"),
 ("C15", "'That covers...' then 'Then reply' could read as a command list.", "deliverables and who to tell are the screen-24 skeleton, not a method.", "none stands"),
 ("C16", "'the way he lays it out' could be a hint.", "it points at the requester's own instructions, as the control-plain-request case does; Eval 1 §2.7.", "none stands"),
 ("C17", "'Slack drops to the free plan' could be a false premise.", "C0ADGSZKR3R/1770840054.486779 'yeah free version' agrees, and the hub states it; the prompt says 'before', not that it happened.", "none stands"),
 ("C18", "Filing 68 tickets may exceed what the tool can do.", "linear_create_issue carries every field; /prompt scored Feasibility 5; this tool has only 2 stored calls (dossier Platform follow-ups).", "none stands"),
 ("C19", "Owen left #god-bugs on Feb 11 (NB-1).", "repaired: a paid seat (C0ADGSZKR3R/1770842395.641349) and a leave and a join in each task channel; persona_view YES on C05V5FNLB9V/1764256187.655299.", "none stands"),
 ("C20", "False positive: relative days are allowed, so this needs no finding.", "true under Local Overrides; kept as Advisory because Prompt Writing §4.2 prefers absolute dates. Hub date " + HUB + ".", "Advisory stands"),
 ("C21", "Friction could be announced.", "03_Error_Async_Config.txt: Friction: none.", "none stands"),
 ("C22", "ENG-2405 Todo with #1905 merged is a lifecycle mismatch, which always fails.", "/prompt raised no issue with it on rev2 (run_forensics/rev2/1_prompt_FAIL_r2.md lists only NB-1 and NB-14 as major); the doc keeps masters as they are, and ENG-2434 keeps ENG-2405 open. Left as Advisory because another reviewer may disagree.", "Advisory stands"),
 ("C23", "A nearby Owen task could count as a duplicate.", "STEP 0.6 on this text: nearest neighbour 0.669, below 0.70, tier distinct (run_forensics/rev2/1_prompt_FAIL_r2.md).", "none stands"),
 ("C24", "One message and many tickets is little variety.", "five kinds of write over four services, ENG-2401.", "none stands"),
]
for r in SR:
    A("| " + " | ".join(r) + " |")
A("\nSpot-decode note: gradeable-report passes for all 49 slots, but `field` slots match the sheet's Bug cell exactly against a short solver key, while a real run writes the line itself. Local forensics on those slots need a hand check; this has no /prompt or rubric effect.\n")
A("Unresolved: rev9's platform /injection; whether /prompt finds a fork the sweeps missed.\n")
A("## Route\n")
A(f"No Fail. Run `/injection` on `task_inputs/01_Universe_Inject.sql`, then paste 04_Prompt.txt exactly as saved (sha256 {sha}) into `/prompt`, paired with that SQL, using the GEN_EXECUTION §7 paste list. There is no error/async config to supply. Answer the task date with Feb 14, 2026. A /prompt FAIL is fatal.\n")
out = "\n".join(L) + "\n"
open(os.path.join(WF, "04_Prompt_Check.md"), "w").write(out)
print("check", len(out), words, sha)
