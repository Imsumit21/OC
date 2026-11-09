#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Check.md and its V3 evidence. Values come from the prompt file, the SQL and plan/ids.json."""
import hashlib, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SQLT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
SQL_SHA = hashlib.sha256(SQLT.encode()).hexdigest()[:12]
P = json.load(open(os.path.join(HERE, "ids.json")))
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
I, B, TK = P["ids"], P["base"], P["tickets"]
HUB, RULE, CARD, FOLDER, SHEET = I["hub"], I["rule_doc"], B["pn_card"], B["folder"], B["pn_sheet"]
G = json.load(open(os.path.join(HERE, "golden", "grade.json")))["runs"]
words, sha = len(PROMPT.split()), hashlib.sha256(PROMPT.encode()).hexdigest()[:12]
hub_text = [x["row"]["text"] for x in parse_sql(SQLT) if x["op"] == "insert" and x["table"] == "slack.slack_messages" and x["row"]["channel_id"] == "D06L58XCVKK"][0]
for ph in ("more money behind beta", "one straight answer on what we actually say to players", "one-page note", "our push notifications card", "Email each person who asked for something, apart from me", "how many Go, Hold and Drop", "your Drive folder"):
    assert ph in hub_text, ph
assert "so open one when you make the call" in SQLT
env = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputsK"}
brief_hash = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputsK/Working_Files/04_Prompt_Writing_Brief.md"], cwd=WS, capture_output=True, text=True, env=env).stdout.strip().split()[-1]
L = []
A = L.append
A("# Prompt Check — samuel_zm_beta_messages")
A(f"> Prompt: 04_Prompt.txt · {words} words · sha256 {sha} · checked 2026-11-05 against 04_Prompt_Writing_Brief.md (2026-11-05, #{brief_hash}) · release task-quality-v1")
A("> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no hints/riddles and every fair outcome.")
A("")
A("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
A("")
A(f"Inputs: 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Universe_Inject.sql rev6 ({SQL_SHA}; local injection gate PASS; the platform `/injection` PASS and `/prompt` NON-FAIL 3 are on rev5, run_forensics/rev5/), 01_Grounding_Dossier.md, 03_Error_Async_Config.txt (Friction: none), 04_Prompt_Writing_Brief.md. No reference files.")
A("")
A("Changes since the last check, prompt and Leonard's DM untouched: rev6 takes the `/hardness` FAIL 2 on rev5 and `/prompt` Coherence 3. Plague Race now reads like every other pass and Vincent's reply is reworded. Vincent's channel post takes his pass off Lives recharged. Leonard's calendar note replaces his Sep 29 line. The Hold rule moved from a card comment to the card's description. Two more comment asks sit outside the parent. One Trello action renames the list to BETA: Oct 10, which settles SC-13. The Rewarded ad ready ask is removed, because the warehouse can answer its live-today test (plan/sweep_fork_rev6.md F1). Truth moves to Go 2, Hold 28, Drop 6 over 36 messages.")
A("")
A("## Summary")
A("")
A("- Fail 0 · Non-fail 0 · Advisory 4 open + 3 resolved (rev4, rev5, rev6) · UNVERIFIED 1 (C22, not a hard gate)")
A("- Checks clean: C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C23, C24")
A("- Predicted /prompt band: PASS by the local formula, on condition that `/injection` passes on rev6. The same formula predicted PASS on rev4 and `/prompt` failed it, so read this as a lint result, not a forecast.")
A("- Status: READY FOR /prompt, after `/injection` on rev6")
A("")
A("## Findings")
A("")
A("| # | Check | Dimension | Severity | Quoted span | Rule (source) | Defect |")
A("|---|---|---|---|---|---|---|")
F = [
 ("C22", "Cross-Service Coherence", "UNVERIFIED", "—", "Playbook C22: reuse a matching /injection PASS", f"No /injection PASS matches rev6 ({SQL_SHA}). The last one is on rev5 (c40a78a9db79, run_forensics/rev5/injection_report_PASS.md)."),
 ("C22", "Cross-Service Coherence", "Advisory (resolved in rev6)", "—", "run_forensics/rev5/prompt_report_NONFAIL_3.md, Issue 1", f"SC-13: the BETA list was named BETA: Oct 10 while its history said BETA: Sep 30. {I['beta_rename']} records the rename. Coherence scored 3 on it."),
 ("C22", "Cross-Service Coherence", "Advisory (resolved in rev5)", "—", "Eval 1 §3.2; run_forensics/rev4/prompt_report_FAIL.md", f"Snowflake PUSH_NOTIFICATION_STATS shows Firebase rows for Zombie Match against 'All our PNs are local' ({B['all_local']}). The rev4 check rated this Advisory and that was too low: the note asked who hears from us, so the table was a competing answer and `/prompt` scored Coherence and Unique Ground Truth 2. Rev5 removes the question. The table stays in the base, but no deliverable asks anything it can answer, and rule test 2 decides the five server rows whether or not a server send exists."),
 ("C13", "Coherence", "Advisory", "\"He also wants things done on the tickets and some emails sent, so do those too.\"", "common_errors 6.6 against scoring.json Coherence", "Sentences 3 to 5 restate parts of Leonard's DM, so a literal reader could delete them. They are not unrelated asks, which is what scoring.json fails, and they name destinations and scope. Kept."),
 ("C16", "Contrived", "Advisory", "—", "Prompt Writing §4.1; GEN_EXECUTION §2", "The text is model-drafted under the local exception. An independent read found 0 of 5 AI-text flags, but the platform's detector still screens it. Retyping it in the human's own words before submission would remove the risk."),
 ("C4", "Competency", "Advisory", "\"what we actually say to players\"", "Eval 1 §1.5; taxonomy screen 7", "The work fits demand, retention and communications, and the outputs are a spreadsheet, a memo and emails. Most tool writes are still on Linear, so a reviewer could call the fit defensible rather than clear. Under V3 a mismatch alone is at most Non-fail."),
 ("C6", "Unique Ground Truth (later stage)", "Advisory", "—", "tools/surface_grader.py spot-decode (this run)", "D1 stays strict: register_parent also wants a share call nothing asks for (weight 1). X1c, X6c and X8c are local proxies by count of state moves, so the rubric must name DES-320, DES-318 and DES-319."),
 ("C7", "Clarity", "Advisory (resolved in rev4)", "\"You don't need to run anything by me first.\"", "Eval 1 §2.6 write-action gate; plan/prompt_read_independent.md F1", f"The rule doc said a changed line needs a string ticket without saying who files it, and this sentence waives any check-in, so runs could split on a write. Rev4 adds 'so open one when you make the call' to {RULE}. The prompt did not change."),
]
for n, r in enumerate(F, 1):
    A(f"| {n} | " + " | ".join(r) + " |")
A("")
A("## Fair readings")
A("")
A("| Deliverable | Reading A (best supported) | Reading B (strongest alternative) | Resolution and evidence |")
A("|---|---|---|---|")
for r in [
 ("W1 plan", "One native sheet, seven columns, 36 rows, in my Drive folder", "A tab on the PN sheet or a Doc", f"Settled by source identity: {HUB} 'Put it in one sheet in your Drive folder'; {SHEET} is read-only for Samuel"),
 ("W1 population", "14 PNs Beta rows plus 22 asks", "Sheet rows and the parent's children only (32)", f"Settled: {HUB} 'every ask ... filed on a ticket or a card'; asks {I['boss_ask']}, {I['gift_ask']}, {I['team_ask']} and {I['inf_ask']}"),
 ("W1 Go set", "Lapsed 1 day, Lapsed 7 days", "Fewer (partial reach, moved phone date, passes on an older iOS build) or more (Lives recharged, Plague Race, Weekly Leaderboard reset)", f"Settled in records: {RULE} test 4; {I['qa_thread']}; {I['lives_pull']} takes one pass off and says the lapsed ones still come through; {I['qa_reply']}; {I['arthur_inline']}"),
 ("W1 Lapsed 7 days headline", f"{P['new_line']}", f"{P['slack_line']}, Leonard's Sep 29 reply", f"Settled: {RULE} 'the latest line I've called'; {I['copy_check']} is dated later, by Leonard, and says it replaces the art thread line"),
 ("W1 Daily gift about to reset", "Hold on its own row", "Same as Daily chest ready, or Drop while the bug is open", f"Settled: {I['gift_ask']} says the streak is live and it is separate from Calvin's chest ping"),
 ("W2 note", "Per-platform baseline, the lapsed reminders the client schedules by day, the four built Holds with why, in my Drive folder", "Pooled D1 and D7, a total count of messages, or server campaigns from the warehouse", f"Settled by {HUB}: 'iOS and Android separately', 'the client schedules', 'the client already schedules'; {RULE} test 3 uses the same words; no total is graded"),
 ("W3, W4 tickets", "A comment on every message ticket; Hold to Backlog unassigned; Drop to Canceled; Go unchanged", "Hold to Todo; Done tickets left alone", f"Settled: {RULE} defers to the roadmap; {I['freeze_comment']}; only Go tickets stay as they are"),
 ("W5 new tickets", "Four for the asks with no ticket, one string ticket under DES-314", "No string ticket, or a second ticket for Win & Collect", f"Settled: {RULE} 'so open one when you make the call'; {HUB} 'under whatever name'; page_liveops_calendar maps the names"),
 ("W7 emails", "One email to each of eight askers", "Leonard too, or one group mail", f"Settled: {HUB} 'Email each person who asked for something, apart from me'"),
 ("W8 counts", "Go 2, Hold 28, Drop 6 in the DM", "A channel post or the sheet only", f"Settled: the prompt 'in that same DM' and {HUB} 'tell me here'"),
 ("Who acts", "The agent does every write for Samuel", "Samuel sends the emails, or the agent stages them", "Settled: no 'I'll' statement; 'I need you to do all of it for me'; 'You don't need to run anything by me first' (plan/prompt_read_independent.md section 2)")]:
    A("| " + " | ".join(r) + " |")
A("")
A("No reported figure stays unsettled (no BOTH_FAIR_FIGURE).")
A("")
A("## Verification log")
A("")
A("| Span | Type | Universe record (locator) | Result |")
A("|---|---|---|---|")
for r in [
 ("\"Leonard\"", "person", "leonard.hayes@harmonygames.co, roster leonard_hayes; hub sender EMPLOYEE_0038_SLACK_ID", "match; active at the clock (dossier 1.C activity.json)"),
 ("\"more money behind beta\"", "state", f"{HUB} 'we're about to put more money behind beta'", "match, verbatim; paid traffic was already running in base, so 'more' holds"),
 ("\"one straight answer on what we actually say to players\"", "state", HUB, "match, verbatim"),
 ("\"His DM to me from yesterday\"", "event", f"{HUB}, ts 1759264851, Tue Sep 30, 2025 1:40 PM PT; base files for D06L58XCVKK end at messages/D06L58XCVKK/2025-07.json", "match; today is Wed Oct 1; it is the only message in that DM after July"),
 ("\"the Zombie Match PN sheet\"", "doc", f"{SHEET} 'Push Notifications Zombie Match'; hg.py search gsheets; persona_view can-see YES; twin f_351b98dfb06f61fb8357d0 is Domino", "match; 'Zombie Match' keeps it unique"),
 ("\"The new sheet\"", "doc", f"{HUB} 'Put it in one sheet in your Drive folder'", "a requested new output"),
 ("\"the one-page note\"", "doc", f"{HUB} 'a one-page note for the team'", "a requested new output"),
 ("\"my Drive folder\"", "doc", f"{FOLDER}, Samuel's only owned folder (hg.py search gdrive); persona_view can-see YES", "match"),
 ("\"the checklist\"", "doc", f"{HUB} 'Every Go goes on a checklist'; no checklist on {CARD}", "a requested new output"),
 ("\"our push notifications card\"", "doc", f"{CARD} '[Feature] Push Notifications - Samuel + Leonard', reopened by {IDS['card_reopen']}", "match; 'our' holds, the card names Samuel and Leonard"),
 ("\"the tickets\"", "state", f"{I['parent']} and its children; {HUB}", "match"),
 ("\"some emails\"", "state", f"{HUB} 'Email each person who asked for something, apart from me'", "match"),
 ("\"the counts\"", "figure", f"{HUB} 'tell me here how many Go, Hold and Drop'", "match; no number in the prompt"),
 ("\"that same DM\"", "channel", f"D06L58XCVKK, {HUB}", "match")]:
    A("| " + " | ".join(r) + " |")
A("")
A("## Brief coverage")
A("")
A("| Brief item | Present in the prompt |")
A("|---|---|")
for a, b in [
 ("A1 Leonard's DM from yesterday (§6)", "\"His DM to me from yesterday\""), ("A2 the Zombie Match PN sheet (§6)", "\"the Zombie Match PN sheet\""), ("A3 my Drive folder (§6)", "\"my Drive folder\""),
 ("W1 plan sheet (§4)", "\"The new sheet\""), ("W2 team note (§4)", "\"the one-page note\""), ("W3, W4, W5 ticket work (§4)", "\"things done on the tickets\""),
 ("W6 checklist (§4)", "\"the checklist goes on our push notifications card\""), ("W7 emails (§4)", "\"some emails sent\""), ("W8 counts (§4)", "\"tell him the counts in that same DM\""),
 ("R1 to R9 through the hub (§6)", "\"has the whole job in it\""), ("Act without staging (§4 decision risks)", "\"You don't need to run anything by me first.\"")]:
    A(f"| {a} | {b} |")
A("")
A("## Calibration self-test (Evals/references/rules/prompt_qc_cases.json)")
A("")
A("| Case | Rule | Matched? | Why |")
A("|---|---|---|---|")
for r in [
 ("K11-staged-errors", "staged_errors", "not matched", "clean spelling and punctuation, no emoji"), ("K11-control-spelled-correctly", "staged_errors", "matched (PASS pattern)", "an ordinary correctly spelled request"),
 ("K31-trap-hint", "trap_hint_or_riddle", "not matched", "no line points at a hidden problem; Leonard's distrust of the sheet is not in the prompt"), ("control-symptom", "trap_hint_or_riddle", "matched (PASS pattern)", "states the job, not the cause"),
 ("K42-hidden-destination", "hidden_destination", "not matched", "the folder, the card and the DM are named"), ("K47-hidden-destination", "hidden_destination", "not matched", "no 'same place as the rest' wording"),
 ("K44-hidden-destination", "hidden_destination", "not matched", "'that same DM' has a clear antecedent"), ("control-named-destination", "hidden_destination", "matched (PASS pattern)", "destinations are named"),
 ("K1-audit-form", "audit_form", "not matched", "no reconcile or complete-the-artifact catalogue"), ("K43-audit-form", "audit_form", "not matched", "same"),
 ("K44-if-chain", "if_chain", "not matched", "the prompt has no if, unless or but"), ("control-plain-request", "audit_form", "matched (PASS pattern)", "'do all of it for me' reads like 'can you check what's still open and close it out'"),
 ("K43-departed-person-premise", "false_state_premise", "not matched", "Leonard is active; no Victor; nothing after 2025-09-30 23:59:59 PT is described as done"), ("K50-both-fair-figure", "ugt_both_fair_figure", "not matched", "no reported figure"), ("K49-newer-source", "ugt_both_fair_figure", "not matched", "no figure")]:
    A("| " + " | ".join(r) + " |")
A("")
A("## Spot decode")
A("")
A(f"Synthetic runs through the real tool shapes (`plan/golden/make_runs.py`), graded by `tools/surface_grader.py`, coverage 100%. They are not platform evidence. A correct run scores {G['golden']['score']:.4f}, losing only D1; a natural-reading run scores {G['natural']['score']:.4f}. `SURFACE.GRADEABLE PASS`, 47 slots. Before the repair a correct run scored 0.69.")
A("")
A("## Self-review")
A("")
A(f"Re-read as Evals/1_Prompt_Eval.md Phases 1 to 3 against 04_Prompt.txt (sha256 {sha} before and after this run). Every value was re-read in this run from rev6 or through `tools/hg.py` and `tools/persona_view.py`. A fresh agent that saw the prompt, the hub and the rule doc but not the brief read it independently (`plan/prompt_read_independent.md`): 0 of 5 AI-text flags, 9 of 9 attributions supported, one write-action fork. That agent read the universe with read-only grep rather than `tools/hg.py`, because the brief given to it did not repeat that rule; nothing was written and no finding here rests on its base reads alone.")
A("")
A("| Check | Counter-reading (strongest case it fails, or that a finding is a false positive) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
C = [
 ("C1", "the field could reject a short prompt", f"{words} words, inside 20 to 4,000 (04_Prompt.txt)", "clean"),
 ("C2", "the assignment could be incomplete", "00_Task_Context.json: all eight fields, universe synthcut, freeze 2025-10-01T00:00:00Z", "clean"),
 ("C3", "a designer deciding message go or hold could be a producer's job", f"{B["pns_sent"]} Leonard sent him the sheet; {CARD} names Samuel; he authored {B['pr248']}", "clean"),
 ("C4", "the work could read as a release sign-off, which is Engineering Ops", f"taxonomy screen 7 lists demand and retention, communications and a Designer; {HUB} frames it on what players hear; finding 5 keeps the risk visible", "clean, Advisory kept"),
 ("C5", "the prompt could carry the recipe", f"no rule, column or test appears (hardness_v2_check RULE_IN_PROMPT CLEAN); brief §8 lists Ambiguity, Dynamic change and Multi-source, e.g. {I['arthur_inline']}", "clean"),
 ("C6", "a second fair outcome could be rejected", "brief §4b and four blind sweeps (plan/sweep_fork.md, plan/sweep_fork_rev2.md, plan/sweep_fork_rev5.md, plan/sweep_fork_rev6.md); forks that moved a call were settled in records, and the note forks /prompt found on rev4 were removed from the hub", "clean"),
 ("C7", "runs could split on a write", f"plan/prompt_read_independent.md F1, fixed by rev4 in {RULE}; act, send and scope are pinned by the prompt", "clean after rev4"),
 ("C8", "the prompt could point at a record that isn't unique or hands over the answer", f"{HUB} is readable, the only such DM, and gives instructions; {RULE} states rules, not calls", "clean"),
 ("C9", "'what we actually say' could imply the sheet is wrong", f"it is Leonard's own goal ({HUB}); no finding, cause or count appears", "clean"),
 ("C10", "naming the card could collapse discovery", f"{CARD} is a destination the hub names, not a hidden authority; brief F39 marks it Yes", "clean"),
 ("C11", "the writes might not need the findings", "every write takes a call from the rule's tests (brief §3)", "clean"),
 ("C12", "one service could do it", "Linear, Sheets, Trello, GitHub, Slack, Gmail and Snowflake all decide facts (brief §8)", "clean"),
 ("C13", "sentences 3 to 5 can be deleted", "scoring.json fails unrelated asks; these serve one job; plan/prompt_read_independent.md F2", "clean, Advisory kept"),
 ("C14", "'Drive', 'DM' and 'tickets' could count as tool mentions", "natural product names are clean (prompt_qc_examples.md row 103); no catalog name matches (Evals/references/tools/catalog.json)", "clean"),
 ("C15", "'When it's all finished' sequences steps", "one closing report, the screen 24 skeleton; no source order is scripted", "clean"),
 ("C16", "the text could read as LLM-polished", "plan/prompt_read_independent.md section 1: 0 of 5 flags; sentence lengths 21, 31, 21, 16, 12, 9; finding 4 keeps the detector risk visible", "clean, Advisory kept"),
 ("C17", "a premise could be false", "every span is in the verification log; 'more money' follows rev2's hub wording against base paid traffic", "clean"),
 ("C18", "a write could be impossible", "gsheets_create_spreadsheet, gdocs_create_document, linear_create_comment, linear_update_issue, linear_create_issue, trello_create_checklist, gmail_send_message and slack_send_message are in catalog.json; Samuel's DES membership is seeded", "clean"),
 ("C19", "a required read could be outside Samuel's view", "dossier check-sql PASS; persona_view can-see YES for the base records; #executives is not needed (C07C2866011)", "clean"),
 ("C20", "'yesterday' could cross a day in UTC", f"{HUB} is Sep 30 in both Pacific and UTC", "clean"),
 ("C21", "friction could be announced", "03_Error_Async_Config.txt: Friction: none", "clean"),
 ("C22", "rev6 has no matching /injection PASS", f"local stage gate PASS on {SQL_SHA}; the platform /injection PASS on rev5 does not cover the new rows; needs /injection on rev6", "UNVERIFIED"),
 ("C23", "the prompt could duplicate a library task", "no samples supplied; word overlap with six completed tasks at most 0.27; platform STEP 0.6 can't be measured here (memory prompt-dataset-duplicate-gate)", "clean, unmeasured at STEP 0.6"),
 ("C24", "it could be one Slack post", "eight kinds of write across Sheets, Docs, Linear, Trello, Gmail and Slack (brief §4)", "clean"),
]
for r in C:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: C22 needs `/injection` on rev6. NotificationManager.cs is a blob `tools/hg.py` can't read, but the rev5 pre-check read it at opus · event 165, which confirms the schedule the note states: day 1 and days 7, 14, 21 and 28. STEP 0.6 similarity can't be measured locally. 27 client-code claims stay unverified without repo blobs (plan/inj_review_C2.md).")
A("")
A("## Route")
A("")
A(f"- No Fail: run `/injection` on rev6 (SQL {SQL_SHA}), then paste 04_Prompt.txt exactly as saved ({words} words, sha256 {sha}) into `/prompt` with that SQL, answering the task date with \"Oct 1, 2025 (synth-cut)\".")
A("- Later stages: `/create-rubric-writing` must name DES-320, DES-318, DES-319 and DES-315 where the local surface uses a count; `/create-humantime` comes after `/prompt`. Oracle Events and rubric text say the five server rows fail test 2 and never say no server push exists; the rubric grades the two lapsed messages without penalising a mention of the leaderboard batch, and does not grade the string ticket's state or assignee (plan/sweep_fork_rev5.md F2 to F4).")
A("")
open(os.path.join(WF, "04_Prompt_Check.md"), "w").write("\n".join(L) + "\n")
ah = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputsK/04_Prompt.txt"], cwd=WS, capture_output=True, text=True, env=env).stdout.strip().split()[-1]
path = os.path.join(WF, "00_V3_Authoring_Evidence.json")
ev = json.load(open(path))
pw = ev["outcome_reviews"]["prompt-writing"]
ev["role_reviews"]["prompt-check"] = {"artifact": "04_Prompt.txt", "artifact_hash": ah, "reviewer": "Claude (Opus 5.5), prompt-check self-review plus an independent fresh-agent read of voice, clarity and role (plan/prompt_read_independent.md); no independent human reviewer",
    "persona_role": "Game Designer",
    "rationale": f"Samuel Turner, Game Designer, asks his assistant to carry out Leonard's DM on what the game says to players. He owns this work: Leonard sent him the sheet, the roadmap card names him, and he authored the client change. The independent read found nothing out of role.",
    "source_ids": [HUB, B["pns_sent"], CARD, B["pr248"], FOLDER]}
ev["outcome_reviews"]["prompt-check"] = {"artifact": "04_Prompt.txt", "artifact_hash": ah, "reviewer": pw["reviewer"] + "; plus the independent read of the prompt (plan/prompt_read_independent.md)",
    "rationale": "Every deliverable the prompt names has one fair outcome or a closed set, settled by a prompt sentence or a persona-visible record. The one write-action fork the independent read found was fixed in the rule doc in rev4, and the note forks /prompt found on rev4 were removed from the hub in rev5. Rev6 moves corrections and adds two asks without touching the hub.",
    "accepted_outcomes": pw["accepted_outcomes"], "alternatives_considered": pw["alternatives_considered"]}
json.dump(ev, open(path, "w"), indent=1, ensure_ascii=False)
print("check", words, sha, "evidence", ah)
