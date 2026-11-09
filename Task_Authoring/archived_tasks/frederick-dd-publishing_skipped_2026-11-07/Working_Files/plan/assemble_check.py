#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Check.md (check mode) for the exact text of 04_Prompt.txt."""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(TI, "..", "tools"))
import brief_facts as BF  # noqa: E402
B, I, BASE, SL, MSG, TH = BF.B, BF.I, BF.BASE, BF.SL, BF.MSG, BF.TH
term = B.term
P = open(os.path.join(TI, "04_Prompt.txt")).read()
WC, SHA = len(P.split()), hashlib.sha256(P.encode()).hexdigest()[:12]
FRED, LEO = "frederick.stone@harmonygames.co", "leonard.hayes@harmonygames.co"
HUB = MSG["hub"]
def q(s):
    assert s in P, s
    return f'"{s}"'
L = []; A = L.append
A("# Prompt Check — frederick_dd_publishing")
A(f"> Prompt: 04_Prompt.txt · {WC} words · sha256 {SHA} · checked 2026-11-07 against 04_Prompt_Writing_Brief.md (2026-11-07, rev2 refresh) · release task-quality-v1")
A("> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.")
A("")
A("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
A("")
A("Inputs: 00_Assigments.md, Working_Files/00_Task_Context.json (context ec895c36b5f1), 01_Universe_Inject.sql rev2 (rev1 e6aa859bea5f passed /injection and failed /prompt on one fork, attempt 6aed99b31c89eba1436ef322; rev2 not yet reviewed), 01_Grounding_Dossier.md, 03_Error_Async_Config.txt (Friction: none), 04_Prompt_Writing_Brief.md. No 02_Reference_Files_Manifest.md: the task has no reference files.")
A("")
A("## Summary")
A("")
A("- Fail 0 · Non-fail 1 (C7, two Minor open non-action details) · Advisory 4 (C23 settled, C6 later-stage, C18, C22) · UNVERIFIED 0 hard gates")
A("- Checks clean: C1, C2, C3, C4, C5, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C19, C20, C21, C24")
A("- Predicted /prompt band: NON-FAIL by the local formula (one Non-fail at C7). Both C7 items are non-action details under Eval 1 §2.6 (the same writes under every reading), so the §2.6 PASS band may still apply.")
A("- Status: READY FOR /prompt")
A("")
A("## Findings")
A("")
A("| # | Check | Dimension | Severity | Quoted span | Rule (source) | Defect |")
A("|---|---|---|---|---|---|---|")
F = [
 ("C7", "Clarity", "Non-fail (Minor)", q("going by his email for what he wants and how he wants it done"), "Playbook C7: an open time or form listed as representational in §4b is Minor; Eval 1 §2.6 NON-FAIL band", f"The reminders' time of day is open (brief §4b D7; {I['rule_doc']} gives the date only). Every reading makes the same seven events on the same dates."),
 ("C7", "Clarity", "Non-fail (Minor)", q("going by his email for what he wants and how he wants it done"), "Playbook C7 (form of a write to the same recipient); Eval 1 §2.6", f"A draft reply on the publisher's thread and a new draft to the same person are both fair (brief §4b D4, D5; neither {I['dd_card']} nor {I['standing_line']} says which). Same recipient and content."),
 ("C23", "Originality", "Advisory", q("Leonard's email from yesterday asks me to model what each publisher would bring in for DD before we all sit down on Monday."), "Eval 1 §2.9 (no samples supplied with this task); platform STEP 0.6 dataset duplicate", "Settled for this text on rev1: STEP 0.6 PASS, distinct, nearest 0.599. The prompt doesn't change in rev2, so it stands unless the library changes."),
 ("C6", "Fair outcomes (later stage)", "Advisory", "—", "tools/surface_grader.py spot-decode, plan/spot_decode.py (this run)", "A realistic correct run decodes 64 of 72 slots. All eight misses are local grader limits, not task defects: it ignores the sheet tab, so a Summary write overlays the Publishers rows (7 slots; 71 of 72 when Summary is written first), and K_home needs a share call no record asks for (72 of 72 with one). Separately, the surface's reply selector is the placeholder hub-message, so a real message id misses K_reply and P_sheet, P_checklists, P_cards, P_drafts. B_PA's regex accepts any 'banked' text, and K_r_banked misses wording like 'haven't banked anything'. Route: read these slots by hand at /create-hardening, and write the rubric on the real values."),
 ("C18", "Feasibility (later stage)", "Advisory", q("the board work he mentions is on the DD publishing card"), "Brief §12; catalog trello_create_card, trello_create_checklist, trello_create_check_item", f"The writes are in the catalog, but card and checklist writes on the UA/BD board and the full read of the {I['pb_event']} description are unproven until the Opus pre-check."),
 ("C22", "Cross-Service Coherence", "Advisory", "—", "Eval 1 §3.2; run_forensics/rev1/platform_injection_review.md advisories 2 and 4", f"Rev2 needs a fresh /injection review; rev1 passed. Its realism advisory stands: outside-owned term sheets sit in {I['dd_folder']}; /prompt scored Cross-Service Coherence 5 with that advisory unscored, and each sheet is shared with Frederick (dossier 1.E)."),
]
for i, f in enumerate(F, 1):
    A(f"| {i} | " + " | ".join(f) + " |")
A("")
A("## Fair readings")
A("")
A("| Deliverable | Reading A (best supported) | Reading B (strongest alternative) | Resolution and evidence |")
A("|---|---|---|---|")
R = [
 ("D1 model", f"A native sheet named DD publishing model in {I['dd_folder']}, tabs Publishers and Summary", "A Doc, or a sheet elsewhere", f"Settled by source identity: {HUB} 'Put the model in your DD publishing folder, laid out the way the doc says'; {I['rule_doc']} 'Layout'"),
 ("D1 population", "The 26 publishers in brief §4b", "The sheet's 24 only, or 25 without Kitebridge", f"Settled: {I['rule_doc']} 'however it reached us' brings in {SL['copperleaf_relay']} and ENG-2362 comment {I['eng2362_comment']}; {HUB} 'never made it onto your sheet' keeps Kitebridge"),
 ("D1 values", "Latest terms, including the two calls", "Term-sheet numbers, because Live says 'in writing'", f"Settled: {I['rule_doc']} 'wherever they are, calls included'; {I['pb_event']}, {I['sunfold_comment']}"),
 ("D1 Oakline Q4", "$30,000", "$20,000 if the resend isn't counted", f"Settled: {SL['arthur_cash']} 'so it'll land in October'; {I['rule_doc']} counts what lands in Q4"),
 ("D2 checklists", "One per status, on the card", "One checklist with statuses as items", f"Settled: {I['dd_card']} 'One checklist per status on this card, one item per publisher'"),
 ("D3 cards", "15 new cards and 2 comments", "17 new cards", f"Settled: {I['dd_card']} 'If they already have a card here, leave a comment'; {I['oakline_card']}, {I['sunfold_card']}"),
 ("D4 nudges", "Seven unsent Gmail drafts", "Sent mail, or text on the cards", f"Settled: {I['dd_card']} 'in your Gmail drafts so it's ready to send'. Thread form both fair, reported under C7"),
 ("D5 notes", "Three unsent drafts to Paola, Diego and Sofia", "None, reading the doc as a limit on content (the rev1 /prompt fork); five with Orchard Lane and Summit; four with Moonrail", f"Settled: {I['rule_doc']} 'still aren't done, so do those as part of this too'; {I['standing_line']} 'still has an offer in with us', 'before we go any further', 'left in your Gmail drafts'; {SL['kestrel_post']}"),
 ("D6 contacts", "14, company in the job", "16, or every publisher", f"Settled: {HUB} 'given us terms or told us no', 'Skip anyone who's already there'; {I['anika_contact']}, {I['lena_contact']}"),
 ("D7 reminders", "Seven events, one per Live offer", "Three events, one per date", f"Settled: {I['rule_doc']} 'One for each Live offer'"),
 ("D8 reply", "A reply on Leonard's email: Copperleaf Games, $67,200, $32,000, $0", "A Q4 total across offers", f"Settled: the prompt 'reply to Leonard on his email'; {HUB} 'which offer goes first, what it brings in over 12 months, what it brings in during Q4'. Reply and reply-all reach only Leonard (To Frederick only)"),
 ("Who acts", "The agent does every write for Frederick", "Frederick writes some himself", "Settled: no 'I'll' statement in the prompt; 'Can you take the whole thing on for me'"),
]
for r in R:
    A("| " + " | ".join(r) + " |")
A("")
A("No reported figure stays unsettled (no BOTH_FAIR_FIGURE).")
A("")
A("## Verification log")
A("")
A("| Span | Type | Universe record (locator) | Result |")
A("|---|---|---|---|")
V = [
 ('"Leonard"', "person", f"roster leonard_hayes, {LEO} (Evals/references/persona/roster.json)", "match; active at the clock (activity.json)"),
 ('"Leonard\'s email from yesterday"', "event / date", f"{HUB}, sent 2025-09-30T23:10:00Z = Tue Sep 30, 4:10 PM PT, To Frederick only", f"match: yesterday for Wed Oct 1. His other Sep 30 PT mails are the ESG reply {MSG['esg_leo']} (9:10 AM PT) and base 'Fwd: Speedrun feedback' {FRED}/1844748127814183717 (8:21 PM PT, hg.py); only the hub asks for this, so the prompt's content picks one"),
 ('"model what each publisher would bring in"', "narrative", f"{HUB}: 'knowing what each publisher would actually bring in. Can you build the model for that?'", "match"),
 ('"DD"', "entity", f"Domino Delights; {HUB}, {BASE['rights_post']} (hg.py)", "match; the founders' own short form"),
 ('"before we all sit down on Monday"', "date / event", f"{HUB}: 'On Monday Oct 6 I want the four of us to sit down'; {I['monday_event']}, 2025-10-06T17:00:00Z", "match: the next Monday after Wed Oct 1; a future event, not described as done"),
 ('"my DD publishing folder"', "doc / state", f"{I['dd_folder']} 'DD publishing', owner {FRED}, parent d_175c0d7bc72ed244b944cb (Frederick's root; hg.py), created 2025-09-24T19:00:00Z", "match; check-sql YES"),
 ('"The model"', "doc", f"{I['rule_doc']} 'A Google Sheet called DD publishing model'", "match (new output, not a premise)"),
 ('"the board work he mentions"', "narrative", f"{HUB}: 'Do what's on the DD publishing card on the UA/BD board too.'", "match"),
 ('"the DD publishing card"', "entity", f"{I['dd_card']} on board {B.UABD_BOARD} (trello /boards/3 'UA/BD'; list /lists/25 'BD Follow Up'; hg.py)", "match; unscoped; Frederick is a member"),
 ('"reply to Leonard on his email"', "narrative", f"{HUB}: 'reply here with which offer goes first'", "match"),
 ('"what he asked for"', "narrative", f"the same hub {HUB}", "match"),
 ("persona reach of every anchor", "ACL", f"persona_view check-sql frederick_stone 01_Universe_Inject.sql --load-bearing plan/load_bearing.txt: {HUB}, {I['rule_doc']}, {I['dd_folder']} (this run)", "verdict: PASS (0 load-bearing rows not visible)"),
]
for r in V:
    A("| " + " | ".join(r) + " |")
A("")
A("## Brief coverage")
A("")
A("| Brief item | Present in the prompt |")
A("|---|---|")
C = [
 ("A1 Leonard's email from yesterday (§6)", q("Leonard's email from yesterday")),
 ("A2 the DD publishing card (§6)", q("the DD publishing card")),
 ("A3 my DD publishing folder (§6)", q("my DD publishing folder")),
 ("D1 model sheet", q("The model goes in my DD publishing folder")),
 ("D2 checklists, D3 follow-ups", q("the board work he mentions is on the DD publishing card")),
 ("D4 nudges", f"absent by design: incorporated through the card ({q('the DD publishing card')})"),
 ("D5 organic notes", f"absent by design: incorporated through Leonard's email and the rule doc ({q('going by his email for what he wants and how he wants it done')})"),
 ("D6 contacts", f"absent by design: incorporated through Leonard's email ({q('going by his email for what he wants')})"),
 ("D7 reminders", f"absent by design: incorporated through the rule doc ({q('how he wants it done')})"),
 ("D8 reply to Leonard (R13)", q("reply to Leonard on his email with what he asked for")),
 ("R1–R8 rules", f"absent by design (§9: the rules stay in the records); incorporated by {q('how he wants it done')}"),
 ("§9 must-not-appear", "none present: no publisher, status, count, date, amount, id, tool name or rule text (programmatic token check in this run); hardness_v2_check RULE_IN_PROMPT CLEAN"),
 ("§11 word count 20–4,000", f"{WC} words"),
]
for r in C:
    A("| " + " | ".join(r) + " |")
A("")
A("## Calibration self-test (Evals/references/rules/prompt_qc_cases.json)")
A("")
A("| Case | Rule | Matched? | Why |")
A("|---|---|---|---|")
K = [
 ("K11-staged-errors", "staged_errors", "not matched", "clean spelling and punctuation, no emoji"),
 ("K11-control-spelled-correctly", "control", "matched (PASS pattern)", "ordinary correctly spelled request"),
 ("K31-trap-hint", "trap_hint_or_riddle", "not matched", "no line points at a hidden problem"),
 ("control-symptom", "control", "matched (PASS pattern)", "states the job, not the cause"),
 ("K42-hidden-destination", "hidden_destination", "not matched", "every destination is named: my DD publishing folder, the DD publishing card, his email"),
 ("K47-hidden-destination", "hidden_destination", "not matched", "the reply target is named ('on his email')"),
 ("K44-hidden-destination", "hidden_destination", "not matched", "no 'answer him there too'"),
 ("control-named-destination", "control", "matched (PASS pattern)", "destinations are named"),
 ("K1-audit-form", "audit_form", "not matched", "no 'reconcile, classify, complete the record' catalogue"),
 ("K43-audit-form", "audit_form", "not matched", "same"),
 ("K44-if-chain", "if_chain", "not matched", "no if / but-not / then-also chain"),
 ("control-plain-request", "control", "matched (PASS pattern)", "'going by his email' mirrors a plain hand-off"),
 ("K43-departed-person-premise", "false_state_premise", "not matched", "Leonard is active at the clock; nothing after 2025-09-30 23:59:59 PT is described as done"),
 ("K50-both-fair-figure", "ugt_both_fair_figure", "not matched", "no figure in the prompt, none unsettled"),
 ("K49-newer-source", "ugt_both_fair_figure", "not matched", "no 'go with the most recent' line"),
]
for r in K:
    A("| " + " | ".join(r) + " |")
A("")
A("## Self-review")
A("")
A(f"Re-read as Evals/1_Prompt_Eval.md Phases 1–3 against 04_Prompt.txt (sha256 {SHA} before and after this run). Values were re-read in this run from 01_Universe_Inject.sql and through tools/hg.py: the hub, Leonard's other Sep 30 mail, the folder, the card, the board and list, the roster. Every quoted span was verified programmatically.")
A("")
A("| Check | Counter-reading (strongest case it fails, or that a finding is a false positive) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
S = [
 ("C1", "The field could reject a very short prompt", f"{WC} words, inside 20–4,000 (wc -w on 04_Prompt.txt)", "clean"),
 ("C2", "The assignment could be incomplete or the source unsupported", "00_Task_Context.json: all eight fields, universe synthcut, freeze 2025-10-01T00:00:00Z, KB bound, context ec895c36b5f1", "clean"),
 ("C3", "A co-founder building a finance model could read as an analyst's job (role implausible)", f"Taxonomy screen 9 lists Co-founder for Finance; he ran the talks ({BASE['appodeal_thread']}, {BASE['tranche']}), and Leonard asks him by name ({HUB})", "clean"),
 ("C4", "Finance could expect budget or cap-table work, not offer comparison", "Screen 9 focus includes forecast, outputs Models and spreadsheets; screen 10's 'compute, model, reconcile'; brief §1", "clean"),
 ("C5", "The prompt could carry the recipe", f"No rule text appears (RULE_IN_PROMPT CLEAN); Ambiguity, Dynamic change and Multi-source live in the records (brief §8: {SL['arthur_cash']}, {I['pb_event']}, {I['sunfold_comment']})", "clean"),
 ("C6", "Reading B of any deliverable may be fair but rejected", "Fair readings above settle each with a record; the thread form is accepted both ways; the local grader's limits are a later-stage Advisory, not a rejected reading", "clean; Advisory kept"),
 ("C7", "The two Minor findings could be false positives, because neither changes a write", "Eval 1 §2.6 scores only write-action divergence as Fail; the playbook still reports representational open fields as Minor (brief §4b D4, D5, D7)", "Non-fail (Minor), kept"),
 ("C8", "'his email' may not be unique, may not state what's attributed to it, or may leave an ask unowed (the rev1 /prompt fork)", f"Content identifies it among his Sep 30 mails (Verification log); {HUB} names the doc and card and states the asks; {I['rule_doc']} gives rules, no answers, and now says the notes are owed; every record is shared with Frederick (check-sql)", "clean"),
 ("C9", "'what each publisher would bring in' could presuppose a finding", f"It names the job in Leonard's own words ({HUB}); no publisher, count or conclusion appears", "clean"),
 ("C10", "Naming the folder and the card could collapse discovery", f"They're §6 anchors; the corrections ({SL['arthur_cash']}, {I['pb_event']}, ENG-2362) stay unnamed. The folder holds stale sheets by design", "clean"),
 ("C11", "The writes could be fixed in advance", "Every write depends on a publisher's status or terms (brief §3): rows, checklists, cards, drafts, contacts, reminders and the reply all change with the findings", "clean"),
 ("C12", "A second service could carry no weight", "10 services plus Snowflake carry weight (brief §1; dossier hardness_gate extreme PASS, tier certified by the gate below)", "clean"),
 ("C13", "The card sentence could be a bolt-on", f"Card work follows from the model's statuses and serves the same Monday decision ({I['dd_card']}, {HUB}); deleting it removes R9's trigger word only, since the hub also carries it", "clean (stacking)"),
 ("C14", "'email', 'folder', 'board' or 'card' could count as tool mentions", "Natural product nouns are clean (prompt_qc_examples.md row 103); no catalog name of 298 in the text (Evals/references/tools/catalog.json)", "clean"),
 ("C15", "'When it's all in, reply…' could be a sequenced command list", "It's the order of deliverables and who to tell (screen 24 skeleton), not an ordered list of sources", "clean"),
 ("C16", "'how he wants it done' could read as a hint at hidden rules", f"It points at Leonard's stated instructions, not a trap ({HUB}); 'control-plain-request' in prompt_qc_cases.json has the same form", "clean"),
 ("C17", "'yesterday', 'Monday' or 'my folder' could be a loose slip", f"Hub 4:10 PM PT Sep 30; Oct 6 is a Monday ({I['monday_event']}); folder owner {FRED} ({I['dd_folder']})", "clean"),
 ("C18", "A write could be impossible, or a send could only be a draft", "gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file, trello_create_checklist, trello_create_check_item, trello_create_card, trello_add_comment, gmail_create_draft, gmail_reply_to_message, contacts_add_new_contact and gcal_create_event are all in catalog.json; the drafts are asked for as drafts", "clean; Advisory for the pre-check"),
 ("C19", "A deciding record could sit in another person's mailbox or a private channel", "check-sql verdict PASS in this run; brief §5a; Linear, Trello, Contacts and Snowflake are unscoped (Evals/references/persona/acl.md)", "clean"),
 ("C20", "'Monday' or 'yesterday' could contradict the clock", "Today is Wed Oct 1; Monday resolves to Oct 6, a future event; yesterday is Sep 30 PT, and the hub is 23:10Z the same day, so no PT/UTC split", "clean"),
 ("C21", "Friction could be announced or remove the only route", "03_Error_Async_Config.txt: Friction: none; the prompt mentions no error or wait", "clean"),
 ("C22", "/prompt's deep re-check could score a base contradiction", "/prompt scored Cross-Service Coherence 5 on rev1; rev2 changes one doc line and moves one sheet cell (run_forensics/rev1/platform_prompt_review.md); the coherence sweep's blocker and fixes are in (plan/sweep/coherence_sweep.md)", "Advisory kept"),
 ("C23", "STEP 0.6 could find a publisher-model task at 0.80 or more", "/prompt scored this exact text distinct on rev1: nearest neighbour 0.599 of 470 tasks, below the 0.70 cutoff (run_forensics/rev1/platform_prompt_review.md)", "Advisory kept"),
 ("C24", "The task could be 'investigate and post one message'", "Eight deliverable kinds across Sheets, Gmail, Trello, Contacts and Calendar (brief §4)", "clean"),
]
for r in S:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: the UA/BD writes and calendar description route await the pre-check; the local surface limits in Finding 4 stay routed to /create-hardening and the rubric stage. No UNVERIFIED hard gate.")
A("")
A("## Route")
A("")
A("No Fail. Paste the rev2 SQL into /injection, then 04_Prompt.txt exactly as saved into /prompt, then run /hardness. Answer the task date with Oct 1, 2025 (synth-cut).")
A("")
out = os.path.join(WF, "04_Prompt_Check.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, len(L), "lines", WC, SHA)
