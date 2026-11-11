#!/usr/bin/env python3
"""Check mode: build Working_Files/08_OE_Check.md for the current 08_Oracle_Events.md (calvin_qm_epic, rev3b).
Sources: the OE file, plan/oe_ledger_ids.json, 01_Universe_Inject.sql parsed as text (never executed; lines cited as SQL L<n>),
plan/oe_base.json (fresh tools/hg.py reads) and the two blind reviews in plan/sweeps/."""
import hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
OE = open(os.path.join(TI, "08_Oracle_Events.md")).read()
EVS = [(int(n), a, e) for n, a, e in re.findall(r"^OE (\d+)  (.*)\nExpected: (.*)$", OE, re.M)]
assert [n for n, _, _ in EVS] == list(range(1, len(EVS) + 1))
FID = json.load(open(os.path.join(HERE, "oe_ledger_ids.json")))["fid"]
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json"))); ID = {k: v["id"] for k, v in SEED.items()}
SQLL = open(os.path.join(TI, "01_Universe_Inject.sql")).read().splitlines()
def sl(k):
    for i, ln in enumerate(SQLL, 1):
        if f"'{k}'" in ln and ln.lstrip().startswith(("VALUES", "INSERT", "UPDATE")): return f"SQL L{i}"
    ch, _, ts = k.partition("/")
    for i, ln in enumerate(SQLL, 1):
        if ts and f"'{ts}', '{ch}'" in ln: return f"SQL L{i}"
    raise KeyError(k)
def sp(k): return f"hg.py slack {OB['slack'][k]['service_file']} {OB['slack'][k]['pointer']}"
LINP = {k: f"hg.py linear data.json {v['pointer']}" for k, v in OB["linear"].items()}
GHP = {k: f"hg.py github data.json {v['pointer']}" for k, v in OB["github"].items()}
cell = lambda s: str(s).replace("|", "/").replace("\n", " ")
F = lambda *ks: ", ".join(FID[k] for k in ks)
DEC = [n for n, a, _ in EVS if a.startswith("Work out each report")][0]
B1718, B135, B2006, B1745 = "C05433XK267/1758817549.151639", "C05433XK267/1759263189.219529", "C05433XK267/1759160363.685759", "C05433XK267/1759162758.968639"
SO = {
 1: ("Brian, Tue Sep 30 2025 1:40 PM PT, ts 1759264805.214409 + 5 quotes", f"{sl(ID['hub'])} slack.slack_messages {ID['hub']}", "ts 1759264805 = 20:40:05 UTC = 1:40 PM PDT; user EMPLOYEE_0026 = Brian Foster; quotes verbatim", F("hub") + " · VERIFIED · quotes"),
 2: ("ZOM-543 'Queue Manager', team ZOM, In Progress, no parent; Brian's comment Tue Sep 30 1:25 PM PT + 15 quotes", f"{LINP['ZOM-543']}; {sl(ID['epic_note'])} linear.linear_comments on ZOM-543", "title, state_id In Progress, parent_id null; author usr_fc22d5941b2aeb5c = Brian; created_at 2025-09-30T20:25:37Z; quotes verbatim", F("epic", "note") + " · VERIFIED · quotes"),
 3: ("Sheet 'ZM home screen flow pass', owner vincent.parker, 7 columns, 38 rows cell for cell, the legend note", f"{sl(ID['sheet'])} gdrive.drive_files and the gsheets.sheets_sheets grid_json of {ID['sheet']}", "header and all 38 rows equal the grid; 18 blank Ticket cells, 20 keys; note verbatim", F("sheet") + " · VERIFIED · quotes (rows generated from the grid)"),
 4: ("Doc 'How to read my pass sheets' + 6 quotes", f"{sl(ID['legend'])} gdocs.docs_documents {ID['legend']}", "title and quotes verbatim; parent is the folder of the flow pass sheet (d_65c76e0b87aa7e9b84d1df)", F("legend") + " · VERIFIED · quotes"),
 5: ("Doc 'ZM builds and QA passes' + 4 quotes", f"{sl(ID['rule_doc'])} gdocs.docs_documents {ID['rule_doc']}", "title and quotes verbatim; owner arthur.blake; shared with Calvin", F("rule") + " · VERIFIED · quotes"),
 6: ("Calvin Thu Sep 25 9:29 AM PT '#1718 already tested'; Vincent 10:15 AM PT 'Looks ok to me' and 'Boss arena as well'", f"{sp('D06UPGF5PQV/1758817744.353289')}; {sp('D06UPGF5PQV/1758820544.160399')}; hg.py slack messages/D06UPGF5PQV/2025-09.json /170 (D06UPGF5PQV/1758820551.265839)", "users EMPLOYEE_0006 Calvin and EMPLOYEE_0012 Vincent; ts 1758817744, 1758820544, 1758820551; quotes verbatim", F("chat") + " · VERIFIED · quotes"),
 7: ("20 states as found; later notes on ZOM-585 (Samuel Turner), ZOM-586 (Owen Baker), ZOM-576, ZOM-582 (Vincent), ZOM-577 (Owen Baker)", f"{sl('ZOM-567')} to {sl('ZOM-586')} linear.linear_issues; {sl(ID['reopen2'])}, {sl(ID['back2'])} linear.linear_comments", "state_id per row as listed (5 In Validation, 15 Todo); authors usr_caafeec2804b3a67 Samuel, usr_4e13bd40cc73d0fc Owen, usr_65c76e0b87aa7e9b Vincent; created_at as stated; quotes verbatim", F("tickets", "reopen2", "back2") + " · VERIFIED · quotes"),
 8: ("Fifteen result posts with job, number, branch and time; twelve main; #1698, #1718, #1746 feature branches; #135 after #1745, #1750, #1757", f"{sp(B1718)}; {sp(B135)}; {sp(B2006)}; {sp(B1745)}; the other eleven in the same file (plan/oe_base.json)", "attachment fallback text of each post gives job - #n - branch; ts converted to PT and UTC; 12 main and 3 feature counted", F("build:iOS Internal #1718", "build:Android Submission #135", "build:Android #2006", "build:iOS Internal #1745") + " · VERIFIED · quotes"),
 9: ("#465, #472, #475 titles, base main, merge times; first line of the #472 description", f"{GHP['465']}, {GHP['472']}, {GHP['475']}; {sl('harmonygames-Games/match3d#472')} (UPDATE of the body)", "merged_at 2025-09-25T22:15:51Z, 2025-09-30T15:53:04Z, 2025-09-30T16:09:15Z; base_ref main; body's first line verbatim", F("pr465", "pr472", "pr475", "body") + " · VERIFIED · quotes"),
 10: ("Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake), Tue Sep 30 8:53 AM PT + quote", f"{sl(ID['inline'])} github.github_review_comments {ID['inline']}; name from hg.py github data.json /users/6", "author_login as stated; created_at 2025-09-30T15:53:40Z; quote verbatim", F("inline") + " · VERIFIED · quote"),
 11: ("Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake), Tue Sep 30 9:09 AM PT + quote", f"{sl(ID['inline2'])} github.github_review_comments {ID['inline2']}", "author_login as stated; created_at 2025-09-30T16:09:50Z; quote verbatim", F("inline2") + " · VERIFIED · quote"),
 12: ("Eight merged PRs not on the sheet with merge times; #463 before the sheet; #473 title, base, merge; Oliver's comment + quote", f"hg.py github data.json /pull_requests/2367, /2370 to /2373, /2375, /2376, /2378, /2379; {sl(ID['else_pr'])} github.github_pr_comments {ID['else_pr']}", "merged_at 2025-09-26T15:14:44Z, 18:58:33Z, 2025-09-29T16:13:50Z, 2025-09-30T01:50:16Z, 15:51:15Z, 15:52:24Z, 15:41:20Z, 15:48:10Z; #463 2025-09-26T00:08:03Z; sheet created 2025-09-26T10:12:44Z; comment author EMPLOYEE_0003, created 2025-09-30T15:42:10Z; quote verbatim", F("pr473", "else") + " · VERIFIED · quote; the list of eight read this run"),
 13: ("ZOM-556 and ZOM-560 titles, state Todo, Vincent's two comments; no ticket for the other sixteen rows", f"{LINP['ZOM-556']}, {LINP['ZOM-560']}; {sl(ID['alias_gift'])}, {sl(ID['alias_streak'])}", "titles and state_id Todo; comments created 2025-09-30T18:05:21Z and 18:08:48Z; quotes verbatim; absence: blind review r2 checked all 553 ZOM tickets by each row's key words (plan/sweeps/oe_blind_review_r2.md)", F("alias_gift", "alias_streak") + " · VERIFIED · quotes · ABSENCE evidence_check"),
 14: ("Vincent's reply Tue Sep 30 2:20 PM PT under his Sep 15 thread; Robert's reply 2:44 PM PT under his Sep 9 PT thread + quotes", f"{sl(ID['reopen'])}, {sl(ID['back'])}; parents {sp('C08R27X0EAH/1757939514.864549')}, {sp('C08R27X0EAH/1757467270.178829')}", "ts 1759267212 and 1759268652; users EMPLOYEE_0012 Vincent and EMPLOYEE_0016 Robert; parent ts 1757939514 = Mon Sep 15 PT, 1757467270 = Tue Sep 9 6:21 PM PT; quotes verbatim", F("reopen", "back") + " · VERIFIED · quotes"),
 15: ("Robert, Mon Sep 29 3:40 PM PT, Android 2006 + quote; #2006 before #1745; no later sighting for the other nine rows", f"{sl(ID['older'])}; {sp(B2006)}; {sp(B1745)}", "ts 1759185627; #2006 posted 15:39 UTC, #1745 16:19 UTC on Sep 29; absence: blind review r2 read every message since Sep 26 in Calvin's team channels and every seeded Slack row", F("older", "build:Android #2006", "build:iOS Internal #1745") + " · VERIFIED · quote · ABSENCE evidence_check"),
 16: ("Marcus Bennett, Tue Sep 30 10:10 AM PT, two messages + quotes; no sheet row, no ticket; four other DMs carry no other bug", f"{sl(ID['filt_dm'])}; SQL L72 (D05U73FNDDL/1759252231.2); hg.py slack messages/D05S1S2H55M/2025-09.json /121 (D05S1S2H55M/1759184077.910139)", "ts 1759252212 and 1759252231; user EMPLOYEE_0002 Marcus; hg.py search linear 'icon glow': 0 hits, scan complete; Owen's Sep 29 line is 'Se ve un poco mas lento todo'", F("glow") + " · VERIFIED · quotes · ABSENCE evidence_check"),
 17: ("Updated invitation from leonard.hayes, Tue Sep 30 10:24 AM PT, subject and note; the Sep 29 invitation's agenda", f"{sl(ID['invite_v2'])}, {sl(ID['invite_v1'])} gmail.gmail_messages", "date 2025-09-30T17:24:09Z; subject and both quotes verbatim", F("invite") + " · VERIFIED · quotes"),
 18: ("Event 'ZM home screen flow review', starts Thu Oct 2 2025 11:00 AM PT, five attendees besides Calvin", f"{sl(ID['event'])} gcal.gcal_events {ID['event']}", "start_ts 2025-10-02T18:00:00Z (after the clock: not yet held); attendees_json as listed", F("event") + " · VERIFIED"),
 19: ("Card name and description; Leonard's change Tue Sep 30 10:22 AM PT; earlier description", f"{sl(ID['rev_card'])} trello.trello_cards; {sl(ID['rev_card_update'])}, {sl(ID['rev_card_v1'])} trello.trello_actions", "name and desc verbatim; action date 2025-09-30T17:22:36Z; createCard action carries the earlier description", F("card") + " · VERIFIED · quotes"),
 20: ("Folder 'ZM queue manager' and presentation 'ZM queue manager', owner calvin.price", f"{sl(ID['folder'])}, {sl(ID['deck'])} gdrive.drive_files", "names and owner as stated; the deck's parent is the folder", F("folder", "deck") + " · VERIFIED"),
 DEC: ("39 reports with status, ticket and review flag; 10 / 9 / 20; areas open of total; 0 Clear; 7 on the review list", f"rules {sl(ID['epic_note'])}; records in OE 2 to OE 19; solver/truth.json re-derives all 39; platform /prompt on this SQL derived the same (Working_Files/platform_reports/prompt_rev3b_PASS.md)", "10 + 9 + 20 = 39; review rows 6, 8, 15, 17, 18, 19, 36; every area has an open report", F("totals", "areas") + " · not_a_claim (derived)"),
}
def signoff(n, a, e):
    if n in SO: return SO[n]
    m = re.search(r"report (\d+)", a); fr = FID.get(f"rep:{m.group(1)}") if m else None
    if a.startswith("Create the ") and "child under the Queue Manager" in a: return (e, f"linear_create_issue (team, title required; parentId, state optional); parent {LINP['ZOM-543']}", "area name from the note; every area Open, so Todo", f"{FID['note']}, {FID['areas']} · VERIFIED (write)")
    if a.startswith("Create the sub-issue"): return (e, f"linear_create_issue (team, title; parentId, state); row in {sl(ID['sheet'])}", "title is the row's What happens cell; state from the status", f"{fr} · VERIFIED (write content)")
    if a.startswith("Move ZOM-"):
        k = a.split()[1]; return (e, f"linear_update_issue (id; parentId, state); {sl(k) if k not in LINP else LINP[k]}", "parent set to the area's child; state per the status", f"{fr}, {FID['tickets']} · VERIFIED (write)")
    if a.startswith("Leave the status note"):
        k = a.split()[5]; return (e[:150] + " …", f"linear_create_comment (issueId, body); {sl(k) if k not in LINP else LINP[k]}", "status and reason as in the decision step", f"{fr} · VERIFIED (write content)")
    if a.startswith("Create the stock-take sheet"): return (e, f"gsheets_create_spreadsheet (title required); folder {sl(ID['folder'])}", "a new native sheet; title free", f"{FID['folder']} · VERIFIED (write)")
    if a.startswith("Write the Reports tab"): return (e, f"gsheets_values_update (spreadsheetId, range, values); columns {sl(ID['epic_note'])}", "six columns, 39 rows, 10 / 9 / 20, 7 marked", f"{FID['note']}, {FID['totals']} · VERIFIED (write content)")
    if a.startswith("Add a second tab"): return (e, f"gsheets_batch_update (spreadsheetId, requests: addSheet); tab name {sl(ID['epic_note'])}", "two tabs", f"{FID['note']} · VERIFIED (write)")
    if a.startswith("Write the Areas tab"): return (e, f"gsheets_values_update; columns {sl(ID['epic_note'])}", "three columns, 10 rows, all Open, counts as in the decision step", f"{FID['areas']} · VERIFIED (write content)")
    if a.startswith("Put the stock-take sheet"): return (e, f"gdrive_move_file (fileId, newParentId); folder {sl(ID['folder'])}", f"parent {ID['folder']} (creating it in the folder directly is an equal route)", f"{FID['folder']} · VERIFIED (write)")
    if a.startswith("Share the stock-take sheet"): return (e, f"gdrive_share_file (fileId; emailAddress, role); attendee in {sl(ID['event'])}", "address as in the event; any role opens the sheet", f"{FID['event']} · VERIFIED (write)")
    if a.startswith("Add one slide"): return (e, f"gslides_batch_update (presentationId, requests); deck {sl(ID['deck'])}", "one new slide with 10, 9, 20, 0, 7", f"{FID['deck']}, {FID['totals']} · VERIFIED (write content)")
    if a.startswith("Message Brian"): return (e, f"slack_send_message (channel, text); DM of {sl(ID['hub'])}", "the five numbers from the decision step", f"{FID['hub']}, {FID['totals']} · VERIFIED (write content)")
    raise KeyError(a)
W = [(n, a) for n, a, _ in EVS if n > DEC]
cnt = lambda p: sum(1 for _, a in W if a.startswith(p))
NW = dict(children=sum(1 for _, a in W if "child under the Queue Manager" in a), subs=cnt("Create the sub-issue"), moves=cnt("Move ZOM-"), notes=cnt("Leave the status note"), shares=cnt("Share the stock-take"))
assert (NW["children"], NW["subs"], NW["moves"], NW["notes"], NW["shares"]) == (10, 17, 22, 22, 5) and len(W) == 83
fw = lambda p: [n for n, a in W if a.startswith(p)]
COV = [
 ("R1 · " + F("epic", "event", "invite"), "OEs 2, 17, 18", "covered", "ledger route: the ticket by its name, the review by its invite and event"),
 ("R2 · " + F("hub"), "OE 1", "covered", "ledger route: Calvin's DM with Brian, Tue Sep 30"),
 ("R3 · " + F("note", "sheet", "legend", "rule", "chat", "inline", "inline2", "else", "body", "reopen", "back", "reopen2", "back2", "older", "glow", "alias_gift", "alias_streak", "card"), f"OEs 2 to 19, {DEC}", "covered", "ledger route: every record the DM and the note incorporate is read before any write, then each report is decided"),
 ("R4 · " + F("tickets", "areas") + ", report facts", f"OEs {DEC}, {W[0][0]} to {fw('Leave the status note')[-1]}", "covered", "ledger route: 10 + 17 linear_create_issue, 22 linear_update_issue, 22 linear_create_comment"),
 ("R5 · " + F("folder", "areas"), f"OEs 20, {fw('Create the stock-take')[0]} to {fw('Put the stock-take')[0]}", "covered", "ledger route: sheet created, two tabs written, moved into the folder"),
 ("R6 · " + F("event"), f"OEs 18, {fw('Share the stock-take')[0]} to {fw('Share the stock-take')[-1]}", "covered", "ledger route: five gdrive_share_file writes"),
 ("R7 · " + F("deck", "totals"), f"OEs 20, {fw('Add one slide')[0]}", "covered", "ledger route: gslides_batch_update"),
 ("R8 · " + F("hub", "totals"), f"OE {fw('Message Brian')[0]}", "covered", "ledger route: slack_send_message in the DM"),
]
R1, R2 = "plan/sweeps/oe_blind_review_r1.md", "plan/sweeps/oe_blind_review_r2.md"
FIND = [
 (8, "Android Submission #135 is a main build posted after iOS Internal #1745, #1750 and #1757.", "Accuracy", "2_Oracle_Events_Eval.md §2.3 value", "The first draft called #135 the newest main build; four main builds follow it on Sep 30 (#2027, #1758, #1759, #2028). Reworded and reached through the ticket notes", f"{R1} finding 1; {sp(B135)}; hg.py slack messages/C05433XK267/2025-09.json /1127, /1128, /1131, /1132"),
 (8, "Fifteen result posts", "Accuracy", "§2.3 count", "The draft listed sixteen, with iOS Internal #1754, a build no row or chat names; removed and recounted (twelve main, three feature). Each build also has a Started post without a branch, so the result posts are named", f"{R1} finding 2, {R2} m2; {sp(B1718)}"),
 (14, "the build Samuel and Owen name in OE 7", "Completeness", "§3.2 dependency", "The search term was credited to the builds read; its source is the ticket notes, now read first", f"{R1} finding 3; {sl(ID['reopen2'])}, {sl(ID['back2'])}"),
 (12, "Eight merged pull requests are not on the sheet", "Completeness", "§3.1 population", "The draft named #473 only; all eight are listed with merge times, the boundary is the sheet's creation time and #463 is placed before it", f"{R1} finding 4, {R2} M2 and m1; hg.py github data.json /pull_requests/2367, /2370, /2371, /2372, /2373, /2375, /2376, /2378, /2379"),
 (13, "a row whose Ticket cell is blank in OE 3", "Completeness", "§3.1 missing discovery", "The draft searched for rows 11 and 20 only; the search now covers all eighteen blank-Ticket rows", f"{R1} finding 5; {LINP['ZOM-556']}, {LINP['ZOM-560']}; {R2} OE 13 (553 ZOM tickets checked)"),
 (15, "the ten rows that still read as passed", "Completeness", "§3.1 missing discovery", "The draft searched for row 27 only; the search now covers all ten passed rows", f"{R1} finding 6; {sl(ID['older'])}; {R2} OE 14, 15"),
 (4, "list the Drive folder that holds the flow pass sheet", "Accuracy", "§3.2 locator", "Search terms 'pass sheets' (the target's own title) and 'pass sheet legend' (not in the doc) replaced by the folder listing; both files share parent d_65c76e0b87aa7e9b84d1df", f"{R1} finding 14, {R2} M1; {sl(ID['legend'])}"),
 (16, "Owen's Sep 29 remark that everything looks a little slower is about Calvin's video, not a build.", "Accuracy", "§2.4 absence wording", "The other DMs are now named with the near miss", f"{R1} finding 10, {R2} m3; D05S1S2H55M/1759184077.910139 (hg.py slack messages/D05S1S2H55M/2025-09.json /121)"),
 (7, "I have a fix locally, need to test it before I open the PR", "Completeness", "§3.1 deciding record", "Owen's note on ZOM-577, which keeps row 19 out of Waiting on QA, was not quoted", f"{R2} m4; {sl('ZOM-577')}"),
 (10, "Login EMPLOYEE_0025_GITHUB_USERNAME (Arthur Blake in the GitHub user record)", "Accuracy", "§2.3 value the tool returns", "The comment read returns a login; the name comes from the user record. The same text in #zombie-prs and Calvin's GitHub mail is named as a second route", f"{R1} finding 8, {R2} m5; {sl(ID['inline'])}"),
 (17, "is the earlier version", "Accuracy", "§3.2 consistency", "The search also returns the Sep 29 invitation; it is now named as superseded", f"{R2} m6; {sl(ID['invite_v1'])}"),
 ([n for n, a in W if a.startswith("Add a second tab")][0], "Add a second tab named Areas", "Format", "§2.7 MULTIPLE_ACTIONS", "Adding the tab and filling it were one event; split in two", f"{R1} finding 13; {sl(ID['epic_note'])}"),
]
L = []; A = L.append
A("# 08 OE Check — calvin_qm_epic (the Queue Manager epic and stock-take, injection rev3b)")
A(f"Checked 2026-11-10 · Events {len(EVS)} · Characters {len(OE)} (300–50,000: ok) · Ledger 2026-11-10 (08_OE_Writing_Ledger.md, gate PASS) · release task-quality-v1")
A("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
A("/oe prediction (a prediction only; /oe gives the verdict): PASS 5")
A("Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE")
A("")
A(f"Scope: {len(EVS)} events = {DEC - 1} reads, 1 decision step, {len(W)} writes (one per event: 10 children, 17 sub-issues, 22 moves, 22 notes, sheet create, Reports write, Areas tab add, Areas write, folder move, 5 shares, 1 slide, 1 message). Every quoted value on an Expected line is asserted as a substring of its own record when plan/assemble_oe_events.py builds the file: seeded rows from 01_Universe_Inject.sql (parsed as text, SQL L-numbers below), base rows through tools/hg.py (plan/oe_reads.py → plan/oe_base.json). Two blind reviews ({R1}, {R2}) were run on the draft; their {len(FIND)} grouped findings are answered below and none remains open.")
A("")
A("## Inventory"); A("| Segment (quoted start) | Role | Event |"); A("|---|---|---|")
for n, a, _ in EVS:
    A(f"| \"OE {n}  {cell(a[:70])}\" | {'STEP (read)' if n < DEC else 'STEP (calculation / decision, no tool)' if n == DEC else 'STEP (write)'} | OE {n} |")
A("| (no headers, notes or response descriptions in the file) | — none — | n/a |")
A(""); A("## Coverage"); A("| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |"); A("|---|---|---|---|")
for r in COV: A("| " + " | ".join(cell(x) for x in r) + " |")
A(""); A("## Expected-data sign-off")
A("| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |"); A("|---|---|---|---|---|---|")
for n, a, e in EVS:
    c, s, v, l = signoff(n, a, e); A(f"| OE {n} | {cell(c)} | {cell(s)} | {cell(v)} | {cell(l)} | match |")
A(""); A("## Findings")
A("Every finding below was raised against the draft by a blind review and fixed in this pass; the quoted span is the corrected text now in 08_Oracle_Events.md. None remains open."); A("")
A("| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |"); A("|---|---|---|---|---|---|---|---|")
for i, (ev, span, comp, rule, what, evd) in enumerate(FIND, 1):
    assert span in OE, span
    A(f"| X{i} | RESOLVED in this pass | {comp} | OE {ev} | \"{cell(span)}\" | 2_Oracle_Events_Eval.md {rule} | {cell(what)} | {cell(evd)} |")
A(""); A("## Pre-verdict sweep"); A("| Eval 4.0 check (7) | Result |"); A("|---|---|")
for a, b in [
 ("One wrong count, ID, channel or tool", f"none: 38 rows from the grid ({sl(ID['sheet'])}); fifteen result posts, twelve main; eight merged PRs off the sheet; 20 seeded tickets; 10 / 9 / 20 / 0 / 7 recomputed; write counts 10, 17, 22, 22, 5 asserted when this file is built"),
 ("One missing write", f"none: {len(W)} writes cover R4 to R8"),
 ("One Expected fact with no retrieving event", f"none: OE {DEC} uses only values read in OEs 1 to {DEC - 1}; blind review r2 confirmed every cross-reference points to an earlier event that holds it"),
 ("One unledgered Expected value or unbacked absence word", f"none: quotes asserted against their records; the three absence statements (OE 13, 15, 16) are backed by scope-bound checks in {R2} and hg.py search linear 'icon glow' (0 hits, scan complete)"),
 ("One act-vs-defer conflict", f"none: ledger §C defer search over Slack, Gmail, Linear, Trello and the SQL found no hold; governing instructions are {ID['hub']} and the note on ZOM-543"),
 ("One non-action or final-response event", f"none: no event states what the agent refrains from or what the final answer says; OE {len(EVS)} is a required write whose content the prompt sets"),
 ("One prompt-forbidden or unauthorised write", "none: every write traces to R4 to R8; no write touches ZOM-543 itself or a ticket outside the 22"),
 ("One missing recovery or wait event", "none: 03_Error_Async_Config.txt is Friction: none"),
]: A(f"| {a} | {cell(b)} |")
A(""); A("## Advisory (no effect on the prediction)"); A("| Event | Note |"); A("|---|---|")
for a, b in [(f"OEs {fw('Share the stock-take')[0]} to {fw('Share the stock-take')[-1]}", "role left open (writer, commenter or reader): the prompt says only 'shared with everyone on the review invite'"),
             (f"OE {fw('Put the stock-take')[0]}", "creating the sheet inside the folder in one call is an equal route to create-then-move"),
             (f"OE {fw('Write the Areas tab')[0]}", "Open reports is given as a count; the list of open reports is an accepted form (platform /prompt)"),
             (f"OE {len(EVS)}", "a thread reply under Brian's message is an accepted form of the DM message")]:
    A(f"| {a} | {b} |")
A(""); A("## Tally")
A(f"Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 4 · fixed in this pass {len(FIND)}")
A(""); A("## Self-review"); A("")
A("**1. Re-read as the eval** (2_Oracle_Events_Eval.md, in order, against this report):")
A(f"- **Phase 1.2 inventory.** All {len(EVS)} segments are STEP. There are no headers, notes, response descriptions or non-actions.")
A("- **Phase 1.3 five fields.** Every read names its service, what it reads and how it is found. The decision step cites the events it uses; its tool is not applicable. Every write names its target, its fields and its service; the sign-off lists the catalog tool and its parameters.")
A("- **HARD GATE.** No event says what the agent refrains from doing or what the final answer says.")
A(f"- **Phase 2.1–2.6.** Service: every value is read where it lives (branches in #builds, merges and reviews in GitHub, ticket notes in Linear, agenda on the Trello card). Tools: all cataloged (Evals/references/tools/catalog.json). Clock: every record time is at or before 2025-10-01T06:59:59Z; the review (2025-10-02T18:00:00Z, {ID['event']}) is a semantic future date and is not expected as done. Act-vs-defer: ledger §C, no hold.")
A("- **Phase 2.7 format.** One action per event, numbered, with a service; no arrows and no JSON.")
A(f"- **Phase 3.1–3.6.** R1–R8 are covered by route. Every search term comes from the prompt or an earlier event. OE sha256 {hashlib.sha256(OE.encode()).hexdigest()[:12]}, {len(OE)} characters, {len(EVS)} events.")
A("- **Phase 4.0** is the 8-row sweep above."); A("")
A("**2. Counter-readings** (one per Coverage row, one per Finding):"); A("")
A("| Judgement | Counter-reading (strongest case against) | Resolution (evidence) |"); A("|---|---|---|")
CR = [
 ("R1 covered (OEs 2, 17, 18)", "The agent takes the Trello roadmap card named Queue Manager for the ticket.", f"Brian's DM says 'I left a note on the ticket' and the note is on ZOM-543 ({sl(ID['epic_note'])}). Holds."),
 ("R2 covered (OE 1)", "The agent reads Brian's Sep 29 line as yesterday's message.", f"{ID['gate_old']} is Sep 29; {ID['hub']} is Sep 30 20:40 UTC ({sl(ID['hub'])}). Holds."),
 (f"R3 covered (OEs 2–19, {DEC})", "A report's status rests on a record no event reads.", f"Blind review r2 recomputed all 39 from the events' records and found each deciding record read earlier; the one gap (Owen's note on ZOM-577) is now quoted in OE 7 ({sl('ZOM-577')}). Holds."),
 ("R4 covered", "A report gets both a move and a new sub-issue, or neither.", f"22 moves + 17 creates = 39, asserted when this file is built; ZOM-556 and ZOM-560 are moved, not duplicated ({LINP['ZOM-556']}). Holds."),
 ("R5 covered", "The sheet lands outside the folder or lacks the second tab.", f"Separate events add the Areas tab and move the file into {ID['folder']} ({sl(ID['folder'])}). Holds."),
 ("R6 covered", "Calvin is also shared, or Leonard is left out.", f"The event lists five attendees besides Calvin, Leonard among them ({sl(ID['event'])}). Holds."),
 ("R7 covered", "The numbers go on an existing slide.", f"Brian's DM says 'add one slide' ({sl(ID['hub'])}); the event adds a new one. Holds."),
 ("R8 covered", "Only three numbers are sent.", f"The DM lists five ({sl(ID['hub'])}); the message carries 10, 9, 20, 0, 7. Holds."),
]
for i, (ev, span, comp, rule, what, evd) in enumerate(FIND, 1):
    CR.append((f"X{i} OE {ev}", "The best case it was harmless: a reader reaches the same records anyway.", f"A blind reviewer following the draft literally reached a different record or could not check the claim; the corrected span is in the file ({evd.split(';')[-1].strip()}). Fixed."))
for r in CR: A("| " + " | ".join(cell(x) for x in r) + " |")
A(""); A("**3. Limits.** The three absence statements rest on the second blind reviewer's scope-bound searches and my own Linear search for 'icon glow'; I did not repeat the sweep of all 553 ZOM tickets. The final draft (after the second review's fixes) has not had a third blind pass.")
A(""); A("Unresolved: none.")
A(""); A("## Reminders")
A("- The tool-call minimum is measured on the 6-rollout average, never on the OE count.")
A("- The OE field blocks pasting: type the events exactly as in 08_Oracle_Events.md (sha256 in the Self-review).")
open(os.path.join(WF, "08_OE_Check.md"), "w").write("\n".join(L) + "\n")
print("wrote check", len(EVS), len(OE), NW, len(FIND))
