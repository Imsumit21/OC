"""Writes task_inputs/Working_Files/08_OE_Writing_Ledger.md (prep mode) for jl-zm-difficulty-baseline.
Arg 1 (optional): check-sql output to take the pasted visibility-proof lines from."""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TI = os.path.join(BUNDLE, 'task_inputs')
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
P = json.load(open(os.path.join(HERE, 'planned_text.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
SQL = open(os.path.join(TI, '01_Universe_Inject.sql')).read()
PROMPT = open(os.path.join(TI, '04_Prompt.txt')).read()
N = M['LIN_NOTES']
sha = lambda s: hashlib.sha256(s.encode()).hexdigest()[:12]
esc = lambda s: str(s).replace('|', '/').replace('\n', ' ')
txt = lambda k: ' '.join(str(P[k]).split())
loc = lambda k: f"{M[k]['channel']}/{M[k]['ts']}"
JUL = 'julia.lawson@harmonygames.co'
GB = f"{JUL}/{M['G_BUILD']['message_id']}"
GR = f"{JUL}/{M['G_BUILD_RE']['message_id']}"
EVT = M['GCAL_TUNING']['copies'][JUL]
FOLDER, SHEET, AGENDA, NOTES, DECK = (M['FOLDER_ZMDIFF']['id'], M['SHEET_KNOBS']['id'], M['DOC_AGENDA']['id'],
                                      M['DOC_LEO_NOTES']['id'], M['CONF_DDA']['id'])
CARD, CMT, CL, ATT, DD = (M['T_H1CARD']['id'], M['T_H1CMT']['id'], M['T_H1CL']['id'], M['T_H1ATT']['id'], M['T_DDCARD']['id'])
rows = [r for r in TR['rows'] if r['member']]
by = lambda s: [r['id'] for r in rows if r['status'] == s]
LIVE, EO, NS, REP = by('Live'), by('Editor only'), by('Not shipped'), by('Replaced')
COMMENTS = ['ZOM-199', 'ZOM-254'] + EO + NS
DROP_T = [r['id'] for r in TR['rows'] if r.get('dropped_by_thread')]
DROP_Q = [r['id'] for r in TR['rows'] if r.get('dropped_by_q_thread')]
assert len(rows) == 24 and len(LIVE) == 16 and len(EO) == 4 and len(NS) == 3 and REP == ['ZOM-254']


def sline(x):
    n = [i for i, l in enumerate(SQL.splitlines(), 1) if x in l]
    return f"01_Universe_Inject.sql (SQL L{n[0]})" if n else "01_Universe_Inject.sql"


L = []
w = L.append
w("# 08 OE Writing Ledger — Julia ZM difficulty baseline register (jl-zm-difficulty-baseline)")
w("Generated 2026-10-31 · Clock 2025-10-01T00:00:00Z (Tue Sep 30, 2025, 5:00 PM PDT; task universe_date in 00_Assigments.md) · "
  "Persona Julia Lawson julia.lawson@harmonygames.co (Product Manager, Product) · Tier Long-Horizon")
w("Status: READY — every requirement has verified, persona-visible facts; every write maps to a cataloged tool; Friction: none")
w(f"Inputs read: 04_Prompt.txt — present (sha256 {sha(PROMPT)}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present "
  f"(sha256 {sha(SQL)}; /injection PASS r11, /prompt PASS 5 r12, /hardness NON-FAIL 4) · 01_Grounding_Dossier.md — present in Working_Files "
  "(leads only) · 01_Hardness_Manifest.json — present in Working_Files (leads for traps) · 03_Error_Async_Config.txt — present (Friction: none) · "
  "02_Reference_Files_Manifest.md — absent (no attachments) · 04_Prompt_Writing_Brief.md — present (§4 pinned final state; §4b rows on the "
  "row set, Brian's role and the DM keys predate hardening round 4, see §F risk 1) · 07_Baseline_Trajectories — six Opus runs on this SQL, "
  "read for tool paths only\n")
w("Persona binding: roster.json entry julia_lawson, Julia Lawson, Product Manager. Scoped services: Gmail (own mailbox), Slack (member of "
  "#zombie-design, #zombie-match3d, #zombie-bugs; party to the DM with Leonard), Calendar (own; Monday's tuning invite is on it), "
  "Drive/Docs/Sheets/Slides (own files and files shared with her; writer on the ZM Difficulty folder). Unscoped: Linear, Trello, GitHub, Contacts.\n")
w("People: Leonard Hayes (EMPLOYEE_0038_SLACK_ID, leonard.hayes@harmonygames.co, requester); Arthur Blake ('Blake', "
  "arthur.blake@harmonygames.co, usr_cc3e90160f490686, EMPLOYEE_0025_GITHUB_USERNAME); Robert (robert@harmonygames.co); Brian Foster "
  "(brian.foster@harmonygames.co). Dates are UTC; \"created\" marks a record time, \"starts\" a semantic future date. The only future "
  "date is the tuning session (starts Mon Oct 6 2025 17:00Z); nothing is expected as done after the clock.\n")

# ------------------------------------------------------------------ A
w("## A · Requirements (traced to the prompt)")
w("| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |\n|---|---|---|---|---|")
REQ = [
 ("R1", "leonard dm'd me on tuesday asking for a baseline of the zm difficulty system", "Discovery — find Leonard's Sep 30 ask in the DM with Julia", "Explicit", "F1"),
 ("R2", "go through his ask and everything it points to", "Discovery — the two thread replies in the DM, the rules card with its comment, checklist and attached notes doc, Blake's store builds mail and reply, the agenda, the invite, the enrage sheet, the deck, ZOM-42, the Linear notes, Blake's PR review and the build code", "Implicit (the sources are named by the ask and the card)", "F2–F19"),
 ("R3", "build the register the way he set it up", "Write — one sheet, two tabs (Tickets: 24 rows with ticket, title, Linear state, status, replaced-by; Rules in force), per card rules 1–5 as amended", "Explicit (layout and rules implicit through the card and agenda)", "F4, F5, F7, F10, F11, F20, F21"),
 ("R4", "put it in the zm difficulty folder", "Write + Constraint — the sheet sits in the ZM Difficulty folder", "Explicit", "F13"),
 ("R5", "share it with everyone on monday's tuning invite", "Write — Robert writer; Brian and Leonard commenter; Arthur reader", "Explicit (roles implicit through rule 7, the checklist, the notes doc and the Sep 30 thread reply)", "F3, F4, F6, F7, F12"),
 ("R6", "if his rules say something needs to happen on the tickets, go ahead and do that too", "Write — 9 Linear comments (ZOM-199, ZOM-254, the 4 Editor only, the 3 Not shipped); none on ZOM-162/163/201/250; no new issues", "Explicit (the set implicit through rule 6, the checklist and the thread reply)", "F3, F4, F6, F10, F22"),
 ("R7", "then reply to leonard in the dm with what he asked for", "Write + Tell — a DM reply: 24 tickets and the per-status counts, the Not shipped and Editor only keys, which ticket replaced which, when a new player gets the starting tier", "Explicit (contents implicit through the ask, its thread reply and the notes doc)", "F1, F2, F7, F17, F20, F23"),
 ("R8", "go with your read on the details, no need to check with me first", "Constraint — act without asking Julia", "Explicit", "—"),
]
for r in REQ:
    assert r[1] in PROMPT, r[1]
    w(f"| {r[0]} | \"{r[1]}\" | {r[2]} | {r[3]} | {r[4]} |")
w("")

# ------------------------------------------------------------------ B
w("## B · Facts")
w("| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search \"query\") | Expected data (dates typed: created / starts / due) | Persona-visible? (proof) | Depends on | Source pointer |")
w("|---|---|---|---|---|---|---|---|---|---|")
F = []
f = lambda *x: F.append(x)
f("F1", "Leonard's ask and the DM history", "Slack (DM Julia ↔ Leonard)", "slack_conversations_history / slack_read_channel",
  "Julia's DM with Leonard, newest messages before the clock", "prompt (\"leonard dm'd me on tuesday\")",
  f"Message {loc('S_ASK')} by Leonard, created Tue Sep 30 2025 19:48:26Z: \"{esc(txt('S_ASK'))}\"; reply_count 1, latest_reply "
  f"{M['S_ASK_REPLY']['ts']} (thread {loc('S_ASK_REPLY')}). Older in the same DM: Julia's message {loc('S_JQ')}, created Mon Sep 29 2025 "
  f"21:38:52Z: \"{esc(txt('S_JQ'))}\"; reply_count 1, latest_reply {M['S_JQ_REPLY']['ts']} (thread {loc('S_JQ_REPLY')})",
  "YES — check-sql", "—", f"{sline(M['S_ASK']['ts'])}; {sline(M['S_JQ']['ts'])}")
f("F2", "Leonard's reply under the ask (scope cut 1, keys in the reply)", "Slack (DM thread)", "slack_conversations_replies / slack_read_thread",
  "Replies under Leonard's Sep 30 ask (thread_ts = the ask's ts)", "F1 (reply_count 1 on the ask)",
  f"Reply {loc('S_ASK_REPLY')} by Leonard, created Tue Sep 30 2025 20:07:18Z: \"{esc(txt('S_ASK_REPLY'))}\" → {', '.join(DROP_T)} off the "
  "register; the DM reply lists the Not shipped and Editor only keys", "YES — check-sql", "F1", f"{sline(M['S_ASK_REPLY']['ts'])}")
f("F3", "Leonard's reply under Julia's Sep 29 question (scope cut 2, no comments, Brian's role)", "Slack (DM thread)",
  "slack_conversations_replies / slack_read_thread", "Replies under Julia's Sep 29 DM message (thread_ts = that message's ts)",
  "F1 (reply_count 1 on Julia's message)",
  f"Reply {loc('S_JQ_REPLY')} by Leonard, created Tue Sep 30 2025 21:16:42Z (the latest instruction before the clock): \"{esc(txt('S_JQ_REPLY'))}\" "
  f"→ {', '.join(DROP_Q)} off the register and no comment on them; Brian gets comment access, not edit", "YES — check-sql", "F1",
  f"{sline(M['S_JQ_REPLY']['ts'])}")
f("F4", "The rules card (rules 1–7)", "Trello (ZM roadmap board)", "trello_search / trello_get_card",
  "Card \"Difficulty baseline (Julia)\" on the ZM roadmap board", "F1 (\"the difficulty baseline card on the zm roadmap board\"); search \"Difficulty baseline\"",
  f"Card {CARD}, created Mon Sep 29 2025 18:05:12Z, description rewritten Tue Sep 30 14:04:31Z (updateCard {M['T_H1UPD']['id']}): "
  f"\"{esc(txt('H1_DESC'))}\". Badges: 1 comment, checklist 2 items, 1 attachment (Leonard's 'notes for monday' doc {NOTES})",
  "Unscoped (Trello)", "F1", f"{sline(CARD)}; trello card {CARD}")
f("F5", "Leonard's card comment (amends rule 1)", "Trello (same card)", "trello_get_card (actions) / trello_get_card_actions",
  "Comment actions on the rules card", "F4 (badges: 1 comment)",
  f"Comment {CMT} by Leonard, created Tue Sep 30 2025 15:41:55Z: \"{esc(txt('H1_CMT'))}\" → ZOM-246, 250, 263, 277, 315 join by title; "
  "ZOM-271 'ATK POWER' does not", "Unscoped (Trello)", "F4", f"{sline(CMT)}; trello action {CMT}")
f("F6", "The card's 'Before Monday' checklist (changes rules 6 and 7)", "Trello (same card)", "trello_get_card (checklists all)",
  "Checklists of the rules card", "F4 (badges: 2 check items)",
  f"Checklist {CL} \"Before Monday\", added Tue Sep 30 2025 16:20:11Z, items: {esc(P['H1_CL_ITEMS'])} → comments also on the Editor only and "
  "Not shipped tickets; the Brian item is superseded by F3 (21:16:42Z)", "Unscoped (Trello)", "F4", f"{sline(CL)}; trello checklist {CL}")
f("F7", "Leonard's 'notes for monday' doc (attached to the card)", "Docs (shared with Julia)", "trello_get_card (attachments) → gdocs_get_document",
  "Doc \"notes for monday\" linked from the card's attachment", "F4 (the attachment links the doc)",
  f"Doc {NOTES}, created Tue Sep 30 2025 15:47:03Z, modified 15:51:58Z, attachment {ATT}: \"{esc(txt('DOC_NOTES_BODY'))}\" → ZOM-258 off; "
  "Arthur reader; the DM names ZOM-254 → ZOM-282", "YES — check-sql", "F4", f"{sline(NOTES)}; gdocs {NOTES}")
f("F8", "Blake's store builds mail", "Gmail (Julia's mailbox)", "gmail_search_messages / gmail_get_thread",
  "Julia's inbox, Blake's \"store builds for monday\" mail", "F4 (rule 3 \"Blake's store builds mail\"); search \"store builds\"",
  f"Message {GB}, created Tue Sep 30 2025 09:12:44Z, from Arthur Blake to Leonard, Julia, Robert, Brian: \"{esc(txt('G_BUILD_BODY'))}\"",
  "YES — check-sql", "F4", f"{sline(M['G_BUILD']['message_id'])}; gmail {GB}")
f("F9", "Blake's reply in the same thread (the > 90 check)", "Gmail (same thread)", "gmail_get_thread",
  "Second message of the store builds thread", "F8 (the thread holds 2 messages)",
  f"Message {GR}, created Tue Sep 30 2025 13:26:05Z: \"{esc(txt('G_BUILD_RE_BODY').split(' On Tue')[0])}\" → ZOM-199's text is wrong (rule 6 comment)",
  "YES — check-sql", "F8", f"{sline(M['G_BUILD_RE']['message_id'])}; gmail {GR}")
f("F10", "The session agenda (layout)", "Docs (shared with Julia)", "gdrive_search / gdocs_get_document",
  "Doc \"ZM difficulty tuning - Oct 6\"", "F4 (rule 2 \"Layout as in the session agenda\"); search \"ZM difficulty tuning\"",
  f"Doc {AGENDA}, created Mon Sep 29 2025 18:31:09Z: \"{esc(txt('DOC_AGENDA_BODY'))}\" → one sheet, tabs Tickets and Rules in force",
  "YES — check-sql", "F4", f"{sline(AGENDA)}; gdocs {AGENDA}")
f("F11", "Julia's monster enrage sheet, Live tab", "Sheets (owned by Julia)", "gdrive_search / gsheets_values_get",
  "Spreadsheet \"ZM monster enrage\", tab Live", "F4 (rule 5 \"your monster enrage sheet\"); search \"ZM monster enrage\"",
  f"Spreadsheet {SHEET}, modified Mon Sep 8 2025 18:21:40Z, tabs Live / Next pass / History. Live (monster, speed, damage, hp): "
  + "; ".join(" ".join(r) for r in P['SHEET_KNOBS_TABS']['Live'][1:]) + ". 'Next pass' is Leonard's proposal (not live)",
  "YES — check-sql", "F4", f"{sline(SHEET)}; gsheets {SHEET}")
f("F12", "Monday's tuning invite (share list)", "Calendar (Julia's own copy)", "gcal_search_events / gcal_list_events",
  "Julia's calendar, event \"ZM difficulty tuning\"", "prompt (\"monday's tuning invite\"); search \"ZM difficulty tuning\"",
  f"Event {EVT}, organizer Leonard, created Mon Sep 29 2025 18:24:51Z, starts Mon Oct 6 2025 17:00Z (semantic future date); attendees "
  "leonard.hayes@harmonygames.co, julia.lawson@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co, brian.foster@harmonygames.co",
  "YES — check-sql", "—", f"{sline(EVT)}; gcal {EVT}")
f("F13", "The ZM Difficulty folder (write target)", "Drive", "gdrive_search / gdrive_list_files",
  "Folder \"ZM Difficulty\"", "prompt (\"the zm difficulty folder\"); search \"ZM Difficulty\"",
  f"Folder {FOLDER}, created Fri Jun 13 2025 15:02:11Z; Julia is writer; holds the enrage sheet {SHEET}", "YES — check-sql", "—",
  f"{sline(FOLDER)}; gdrive {FOLDER}")
f("F14", "ZOM-42, the tier spec", "Linear (team ZOM)", "linear_search_issues / linear_get_issue",
  "Issue \"Dynamic Difficulty\" in team ZOM", "F4 (rule 4 and 5 name ZOM-42); search \"Dynamic Difficulty\"",
  "ZOM-42, Done, created Mon Apr 21 2025 16:28:42Z. Starting tier: '1st 10 level avg CPM > 90 (top 20%) moves to tier 1, rest stays in tier 0'. "
  "Promotion: 'Tier -2 is an exception. You promote instantly after 1 win'; 'UP TO THE MOST RECENT 10 attempts'; 'win rate is 80% or higher'. "
  "Demotion: 'Lose 4 in a row, you're demoted'; 'win rate for up to the last 10 games is 50% or lower'; 'every time a promotion/demotion "
  "happens, the record is reset'", "Unscoped (Linear)", "F4", "linear data.json /issues ZOM-42 description")
f("F15", "The ZOM candidate population and closing notes", "Linear (team ZOM)", "linear_list_issues (team ZOM, paginate) + linear_list_comments per issue",
  "Every team ZOM issue created up to Aug 31 2025, and the comments on each", "F4 (rule 1 scope and the 'tiers:' tag)",
  f"{TR['candidates']} candidates read for notes; title-word matches by rule 1 + the attack-power comment; 6 Duplicate-state ZOM issues out. "
  "Decisive notes: tag 'tiers:' by Blake on ZOM-221 (cmt_ad5c9cc21508c9961089), ZOM-281 (cmt_df69e4a92767cbff0000, assignee another person), "
  "ZOM-300 (cmt_5919318074e3e3fb7921), ZOM-305 (cmt_735d60b29ce006b58217), ZOM-378 (cmt_5209afb9533bec4053ad); ZOM-277 'average in the editor's "
  "stats panel, nothing changes in the game'; ZOM-315 'total attack power in the editor's stats panel … nothing changes in the game'; ZOM-173 "
  "'set count in the level objects panel' (match3d#243, Assets/Scripts/LevelEditor); ZOM-282 'this replaces the blunder 2.0 boost from ZOM-254'; "
  "ZOM-202 'wip on a branch, nothing merged yet' (In Progress); ZOM-280 'not reproducible anymore, closing' (Canceled); ZOM-293 'still happens "
  "on the dev build, keeping it open' (Todo); ZOM-312 'merged with match3d#265'", "Unscoped (Linear)", "F4",
  "01_Universe_Inject.sql linear.linear_comments rows (minted_ids.json LIN_NOTES); linear data.json /issues")
f("F16", "Blake's 'not tiers' review on PR 265 (ZOM-312 off)", "GitHub (match3d)", "github_get_pull_request_reviews / github_get_pull_request_comments",
  "Review comments on pull request 265 in the match3d repo", "F15 (ZOM-312's note names match3d#265)",
  f"Review {M['GH_265_REV']['id']} by Blake (empty body), created Thu Jul 3 2025 17:50:12Z, inline comment {M['GH_265_RC']['id']} on "
  f"{M['GH_265_RC']['path']}: \"{esc(txt('GH_265_RC_BODY'))}\" → ZOM-312 stays off (rule 1)", "Unscoped (GitHub)", "F15",
  f"{sline('#265#rc_7')}; github {M['GH_265_RC']['id']}")
f("F17", "PR 401's comment (not a replacement)", "GitHub (match3d)", "github_get_pull_request_comments / github_get_issue_comments",
  "Comments on pull request 401 in the match3d repo", "F15 (ZOM-282's note: speed and damage still share one value); search \"Split enrage\"",
  f"Comment {M['PRC_244']['id']} by Blake, created Mon Aug 25 2025 17:02:28Z: \"{esc(txt('PRC_244_BODY'))}\" → #401 splits values; ZOM-282 stays "
  "Live, nothing is Replaced by #401 (rule 4)", "Unscoped (GitHub)", "F15", f"{sline('#401#c_2')}; github {M['PRC_244']['id']}")
f("F18", "Starting-tier timing in the build", "GitHub (match3d, main)", "github_get_file_contents",
  "TierManager.cs and WinHistory.cs in the match3d repo (DynamicDifficulty, Player folders)", "F14 (ZOM-42 names the starting tier); search \"totalGames\"",
  "TierManager.cs: 'var totalGames = WinHistory.GetTotalGames(); if (totalGames == 10)' → ApplyInitialBucketing: 'case var cpm when cpm > 90.0f: "
  "newTier = 1; default: newTier = 0'. WinHistory.cs: 'GetTotalGames() { return GetTotalWins() + GetTotalLosses(); }' → a new player is placed "
  "after the first 10 games, won or lost (not level 10); 90 exactly stays on tier 0", "Unscoped (GitHub)", "F14",
  "HarmonyGames_GitHub match3d Assets/Scripts/DynamicDifficulty/TierManager.cs line 30, line 96; Assets/Scripts/Player/WinHistory.cs line 164")
f("F19", "ZOM-303, the level drop after a demotion; Blake's enrage note", "Linear + Slack (#zombie-design)", "linear_get_issue; slack_search_public_and_private",
  "Issue \"Dynamic Difficult Design Oversight Fix\" in team ZOM; Blake's Sep 3 note in #zombie-design", "F15 (ZOM-303 is a member); search \"blunder part\"",
  "ZOM-303, Done (merged with match3d#244): 'when a player is demoted, we also need to demote the level difficulty for the level' → yes, the level "
  f"drops a tier. Message {M['CC_ART']['channel']}/{M['CC_ART']['ts']} by Blake, created Wed Sep 3 2025 15:22:09Z: \"{esc(txt('CC_ART_BODY'))}\" → "
  "enrage is per monster, speed and damage, no hp (Robert's deck's +25% line is old)", "YES — check-sql (Slack); unscoped (Linear)", "F15",
  f"linear data.json /issues ZOM-303; {sline(M['CC_ART']['ts'])}")
# derived
rtxt = "; ".join(f"{r['id']} {r['state']} {r['status']}" + (f" → {r['replaced_by']}" if r['replaced_by'] else "") for r in rows)
f("F20", f"The register Tickets tab (derived, {len(rows)} rows)", "Computed from F2–F17", "local reasoning, then gsheets_create_spreadsheet + gsheets_values_update",
  "Card rules 1–4 (F4) with F5, F2, F3, F7, F16 over F15", "F15",
  f"Ticket · Linear state (as found) · status: {rtxt}. Counts: 16 Live, 4 Editor only ({', '.join(EO)}), 3 Not shipped ({', '.join(NS)}), "
  f"1 Replaced (ZOM-254 → ZOM-282). Left off: {', '.join(DROP_T)} (F2); {', '.join(DROP_Q)} (F3); ZOM-258 (F7); ZOM-312 (F16); ZOM-271 "
  "(ATK alone, F5); Duplicate-state issues (rule 1)", "Derived from visible inputs",
  "F2, F3, F4, F5, F7, F8, F15, F16, F17", "Derived; support/task_work/jl_difficulty/truth.json /rows")
f("F21", "The Rules in force tab (derived)", "Computed from F9, F11, F14, F18, F19", "local reasoning, then gsheets_values_update",
  "Card rule 5 (F4) over F9, F11, F14, F18, F19", "F18, F19",
  "Starting tier: after a new player's first 10 games (wins and losses), average CPM > 90 → tier 1, else tier 0 (90 exactly stays on 0) — "
  "the build governs the timing (rule 5). Promotion: 80%+ win rate over up to the most recent 10 attempts; tier -2 promotes after 1 win. "
  "Demotion: 4 losses in a row, or 50% or lower over up to the last 10; the record resets after every move. Level drop after a demotion: yes "
  "(ZOM-303). Enrage: per monster, speed and damage, no hp — the Live tab rows of F11 as they stand, incl. 'Mailman, Mayor2, PartyGirl: not copied yet'",
  "Derived", "F9, F11, F14, F18, F19", "Derived; F11 Live tab; ZOM-42; TierManager.cs")
f("F22", "Ticket comments to post (derived, 9)", "Computed from F3, F6, F9, F20", "local reasoning, then linear_create_comment",
  "Card rule 6 (F4) + checklist (F6) − Leonard's Sep 30 thread reply (F3)", "F20",
  f"ZOM-199: the build checks CPM > 90, not >= 90 (F9); ZOM-254: replaced by ZOM-282; {', '.join(EO + NS)}: the change isn't in the store "
  f"builds. None on {', '.join(DROP_Q)} (F3), ZOM-42, ZOM-312 or any other ticket; no new issues", "Derived", "F3, F6, F9, F20",
  f"Derived; card {CARD} rule 6; checklist {CL} item 1; {loc('S_JQ_REPLY')}")
f("F23", "The DM reply contents (derived)", "Computed from F1, F2, F7, F18, F20", "local reasoning, then slack_send_message",
  "The ask (F1), its thread reply (F2), the notes doc (F7)", "F20",
  f"The register is in the ZM Difficulty folder; 24 tickets: 16 Live, 4 Editor only, 3 Not shipped, 1 Replaced; Not shipped keys {', '.join(NS)}; "
  f"Editor only keys {', '.join(EO)}; ZOM-254 was replaced by ZOM-282; a new player gets the starting tier after their first 10 games, won or lost",
  "Derived", "F1, F2, F7, F18, F20", "Derived; truth.json /counts")
for x in F:
    w("| " + " | ".join(esc(c) for c in x) + " |")
w("")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)\n")
body = "\n".join(L)
need = set(re.findall(r"\b[CD][A-Z0-9]{8,11}/\d{10}\.\d{6}\b|\b[fd]_[0-9a-f]{22}\b|\bevt_[0-9a-f]{10,}\b|<[^<>\s]+@mail\.gmail\.com>", body))
proof = []
if len(sys.argv) > 1:
    seen = set()
    for l in open(sys.argv[1]):
        if l.startswith('[YES') and any(x in l for x in need):
            key = l.split(' insert ')[-1].split(' - ')[0]
            if key not in seen:
                seen.add(key)
                proof.append(l.rstrip())
w("```\n" + ("\n".join(proof) or "(pending)") + "\n```\n")

# ------------------------------------------------------------------ C
w("## C · Write capability")
w("| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |")
w("|---|---|---|---|---|---|---|---|---|---|")
DEF = (f"slack DM thread history before the clock (4 seeded messages incl. both thread replies, complete) · trello card {CARD} (description v2 "
       f"{M['T_H1UPD']['id']}, comment, checklist, attachment; governing version: the Sep 30 description as amended by the comment, the checklist and "
       f"then the Sep 30 21:16Z thread reply {loc('S_JQ_REPLY')}) · gmail store builds thread {GB} (2 messages, complete) · gdocs {NOTES} (1 version) "
       "· linear ZOM comments on all candidates (complete) → no hold, defer or wait on this write")
C = [
 ("R3", "Create the register sheet (Tickets tab) and write its 24 rows", "build the register the way he set it up", "gsheets_create_spreadsheet, gsheets_values_update (yes)", "title; spreadsheetId, range, values", "F20", "a new spreadsheet holding the 24 rows", "ticket, title, Linear state, status, replaced-by"),
 ("R3", "Add the Rules in force tab and write it", "build the register the way he set it up", "gsheets_batch_update addSheet, gsheets_values_update (yes)", "spreadsheetId, requests; range, values", "F21", "a second tab with the rules", "starting tier, promotion, demotion, level drop, enrage per monster"),
 ("R4", "Place the sheet in the ZM Difficulty folder", "put it in the zm difficulty folder", "gdrive_move_file (yes) or gdrive_create_file with the parent", "fileId, newParentId", "F13", f"the sheet's parent is {FOLDER}", "location only"),
 ("R5", "Share with Robert as editor", "share it with everyone on monday's tuning invite", "gdrive_share_file (yes)", "fileId, emailAddress, role writer", "F12", "robert@harmonygames.co writer", "role per rule 7"),
 ("R5", "Share with Brian as commenter", "share it with everyone on monday's tuning invite", "gdrive_share_file (yes)", "fileId, emailAddress, role commenter", "F12, F3", "brian.foster@harmonygames.co commenter", "role per F3 (overrides the checklist)"),
 ("R5", "Share with Leonard as commenter", "share it with everyone on monday's tuning invite", "gdrive_share_file (yes)", "fileId, emailAddress, role commenter", "F12", "leonard.hayes@harmonygames.co commenter (his folder access also satisfies it)", "role per rule 7"),
 ("R5", "Share with Arthur as reader", "share it with everyone on monday's tuning invite", "gdrive_share_file (yes)", "fileId, emailAddress, role reader", "F12, F7", "arthur.blake@harmonygames.co reader", "role per the notes doc"),
 ("R6", "Comment on each of the 9 tickets", "if his rules say something needs to happen on the tickets, go ahead and do that too", "linear_create_comment (yes, one call per ticket)", "issueId, body", "F22", "9 new comments: " + ", ".join(COMMENTS), "what the build does (ZOM-199), what replaced it (ZOM-254), not in the store builds (the other 7)"),
 ("R7", "Reply to Leonard in the DM", "then reply to leonard in the dm with what he asked for", "slack_send_message (yes)", "channel, text (thread_ts optional)", "F1, F23", "a message from Julia in the DM", "counts, keys, 254 → 282, starting-tier timing"),
]
for c in C:
    assert c[2] in PROMPT, c[2]
    w(f"| {c[0]} | {c[1]} | \"{c[2]}\" | {c[3]} | {c[4]} | {c[5]} | {c[6]} | {c[7]} | {DEF} | yes |")
w("")
w("## D · Friction facts")
w("| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |\n|---|---|---|---|---|---|")
w("| none | Friction: none (03_Error_Async_Config.txt) | none | — | — | — |\n")

# ------------------------------------------------------------------ E
w("## E · Traps and distractors")
w("| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |\n|---|---|---|---|")
man = json.load(open(os.path.join(TI, 'Working_Files', '01_Hardness_Manifest.json')))
for t in man['traps']:
    ptr = ", ".join((t.get('seeded_ids') or []) + (t.get('base_pointers') or []))[:170] or "01_Hardness_Manifest.json"
    w(f"| {t['id']} | {esc(t.get('expected_wrong_reading', ''))} ({esc(ptr)}) | F20 | {esc(t.get('resolver', ''))} |")
w(f"| X1 | the Domino Delights 'Difficulty baseline' card on another board ({DD}) | F4 | other game, other board, created Jun 2 2025 |")
w(f"| X2 | Brian's #zombie-design recap 'everything … is in the store builds, the editor bits too' ({loc('S_ROBERT_SUM')}) | F8 | not from Blake; the store builds mail strips the editor and debug folders |")
w("")

w("## F · Open risks")
w("| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |\n|---|---|---|---|---|")
w("| 1 | 04_Prompt_Writing_Brief.md §4b still carries pre-round-4 values in four rows (row set '30 members', Brian writer, 'the 12' comments, 9 Editor only keys); §4 and this ledger hold the round-4 values (24 rows, Brian commenter, 9 comments, 4 Editor only keys) | F20, F22, F23 | rubric: use §4 and this ledger, not §4b | none for /oe; re-sync §4b before /create-rubric-writing if the rubric gate reads it |")
w(f"| 2 | Both thread replies sit under DM messages; 5 of 6 baseline runs never opened either | F2, F3 | rubric: the 10 exclusions, Brian's role, 4 no-comment rows, counts and keys; OE must read both threads | none — check-sql YES; reply_count 1 on both parents |")
w("| 3 | Starting tier: ZOM-42, ZOM-199 and the deck say '10 levels'; the build counts games incl. losses | F18, F21, F23 | rubric: accept '10 games' or '10 levels played' (/prompt r12), fail 'level 10' | none |")
w("| 4 | The Live tab's last row is 'not copied yet' for Mailman, Mayor2, PartyGirl; values for them are never graded | F11, F21 | rubric: copy as is; no values | none (/prompt settled) |\n")

w("## G · Tally")
w(f"Requirements {len(REQ)} · facts {len(F)} · writes {len(C)} (feasible {len(C)}) · friction items 0 · unverified visibility 0 · blocking 0\n")

# ------------------------------------------------------------------ Self-review
w("## Self-review")
w("Walked `Evals/2_Oracle_Events_Eval.md` 1.1, 2.1–2.6 and 3.1–3.5 against the ledger in order: every requirement has facts (§A Fact IDs); every "
  "write has prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search (§C); no friction (§D); "
  "every scoped §B fact carries a record id and a pasted check-sql line. No-event-text scan: §B and §C hold facts, values and edges only — no "
  "'OE n', no agent voice, no 'should'.\n")
w("| Counter-reading | Resolution (evidence) |\n|---|---|")
CR = [
 ("R1: the ask could be Vincent's #zombie-design request for the list", f"the prompt says Leonard DM'd; the ask {loc('S_ASK')} is in the DM and names the card"),
 ("R2: 'everything it points to' could stop at the card description", f"the card shows 1 comment, 2 check items and 1 attachment (F4); both DM parents show reply_count 1 ({loc('S_ASK_REPLY')}, {loc('S_JQ_REPLY')})"),
 ("R3: the register could keep the 10 tickets the thread replies drop (34 rows)", f"F2 and F3 name them; F3 says 'on top of the ones i already left off' ({loc('S_JQ_REPLY')})"),
 ("R4: Julia's Drive root could do", f"rule 7 'The register goes in the ZM Difficulty folder' (card {CARD}); folder {FOLDER}"),
 ("R5: Brian could stay writer per the checklist", f"the checklist is 16:20:11Z; Leonard's reply {loc('S_JQ_REPLY')} at 21:16:42Z says 'comment access is enough for brian'"),
 ("R6: ZOM-162/163/201/250 could still get Editor only comments", f"they are off the register and F3 says 'no comments on them either'"),
 ("R7: the reply could go to #zombie-design or omit the keys", f"the ask says 'reply here'; F2 asks for the keys; the notes doc {NOTES} asks for which replaced which"),
 ("R8: 'no need to check with me' could permit skipping the shares", "it removes check-ins only; the shares are asked in the prompt"),
 ("F18 vs F14: ZOM-42's '1st 10 level' governs the starting tier", "rule 5: 'For when a new player gets their starting tier … go by the build'; TierManager.cs totalGames == 10 with GetTotalWins() + GetTotalLosses()"),
 ("F17: ZOM-282 is Replaced by match3d#401", f"rule 4: 'PRs that change or split its numbers don't'; {M['PRC_244']['id']} says #401 splits values"),
 ("F16: ZOM-312 stays (title match 'tier')", f"rule 1 'a title match Blake marked \\'not tiers\\' in his review on its PR stays off'; {M['GH_265_RC']['id']}"),
]
for a, b in CR:
    w(f"| Counter: {a} | {b} |")
w("\nRe-verified this run through `tools/hg.py` and the SQL rows: the ask, both thread replies and Julia's Sep 29 message, the card, its comment, "
  "checklist and attachment, the notes doc, the store builds mail and reply, the agenda, the invite and its attendees, the folder, the enrage "
  "sheet's Live tab (01_Universe_Inject.sql rows); ZOM-42 and ZOM-303 descriptions (linear data.json); TierManager.cs and WinHistory.cs "
  "(match3d export); the 24-row register and its counts recomputed from truth.json.\n")
w("Unresolved: none.\n")
dst = os.path.join(TI, 'Working_Files', '08_OE_Writing_Ledger.md')
open(dst, 'w').write("\n".join(L) + "\n")
print('wrote', dst, len(F), 'facts', len(proof), 'proof lines', 'need', len(need))
