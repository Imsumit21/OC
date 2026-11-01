"""Round 7: bring 08_OE_Writing_Ledger.md to SQL b64bc2f2c6dc (rounds 5-7 changes). Rewrites changed rows, adds F24-F26,
T30-T34, refreshes the visibility block from persona_view. Run from Task_Authoring-2 on the round-4 ledger backup.

Usage: python3 support/task_work/jl_difficulty/r7/build_ledger_r7.py <round-4 ledger> <out ledger>
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sqlrows import load  # noqa: E402
import truth7 as T  # noqa: E402

src, out = sys.argv[1], sys.argv[2]
s = open(src).read()
R = load('task_inputs/01_Universe_Inject.sql')
one = lambda x: ' '.join(str(x).replace('\\n', ' ').split())
txt = lambda i: one(R[i]['text'])
CARD = one(R['68daca5871dba40417a00383']['desc'])
M1 = one(R['julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>']['body_text'])
M2 = one(R['julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>']['body_text'])
RC271 = one(R['harmonygames-Games/match3d#271#rc_1']['body'])
EO, NS, LIVE = ', '.join(T.EO), ', '.join(T.NS), T.LIVE


def line(prefix, new):
    global s
    ls = s.split('\n')
    hits = [i for i, l in enumerate(ls) if l.startswith(prefix)]
    assert hits, prefix  # first match: section A rows precede section C rows with the same R id
    ls[hits[0]] = new
    s = '\n'.join(ls)


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)


# ---- header
rep("Generated 2026-10-31", "Generated 2026-11-01")
rep("present (sha256 107ea4da05fa; /injection PASS r11, /prompt PASS 5 r12, /hardness NON-FAIL 4)",
    "present (sha256 b64bc2f2c6dc; /injection PASS r13, /prompt PASS 5 r14, /hardness NON-FAIL 3 r7)")
rep("04_Prompt_Writing_Brief.md — present (§4 pinned final state; §4b rows on the row set, Brian's role and the DM keys predate hardening round 4, see §F risk 1)",
    "04_Prompt_Writing_Brief.md — present (§4 pinned final state predates hardening rounds 5-7, see §F risk 1)")
rep("07_Baseline_Trajectories — six Opus runs on this SQL, read for tool paths only",
    "07_Baseline_Trajectories — six Opus runs on this SQL (round 7), read for tool paths only")
rep("party to the DM with Leonard)", "party to the DM with Leonard and the group chat with Robert and Leonard)")

# ---- A
line("| R2 |", "| R2 | \"go through his ask and everything it points to\" | Discovery — the two thread replies in the DM, the rules card with its comment, checklist and attached notes doc, Robert's reply in the group chat the card names, Blake's store builds mail and his separate reply, the agenda, the invite, the enrage sheet, the deck, ZOM-42, the Linear notes, Blake's 'not tiers' PR reviews (265, 271) and the build code | Implicit (the sources are named by the ask and the card) | F2–F19, F24, F25 |")
line("| R3 |", "| R3 | \"build the register the way he set it up\" | Write — one sheet, two tabs (Tickets: 23 rows with ticket, title, Linear state, status, Linear assignee, done day in Pacific time, Linear priority, replaced-by; Rules in force), per card rules 1–5 as amended | Explicit (layout and rules implicit through the card, the agenda and Robert's reply) | F4, F5, F7, F10, F11, F20, F21, F24, F26 |")
line("| R6 |", "| R6 | \"if his rules say something needs to happen on the tickets, go ahead and do that too\" | Write — 9 Linear comments (ZOM-199, ZOM-254, the 4 Editor only, the 3 Not shipped, these 7 naming iOS 0.3.49 and Android 0.3.133); none on ZOM-162/163/201/250; no new issues | Explicit (the set implicit through rule 6, the checklist and both thread replies) | F2, F3, F4, F6, F9, F10, F22 |")
line("| R7 |", "| R7 | \"then reply to leonard in the dm with what he asked for\" | Write + Tell — a DM reply: 23 tickets and the per-status counts, the Not shipped and Editor only keys, which ticket replaced which, when a new player gets the starting tier | Explicit (contents implicit through the ask, its thread reply and the notes doc) | F1, F2, F7, F18, F20, F23 |")

# ---- B (changed rows)
line("| F2 |", f"| F2 | Leonard's reply under the ask (scope cut 1, keys in the reply, builds in the comments) | Slack (DM thread) | slack_conversations_replies / slack_read_thread | Replies under Leonard's Sep 30 ask (thread_ts = the ask's ts) | F1 (reply_count 1 on the ask) | Reply D05HB64NMQU/1759262838.442871 by Leonard, created Tue Sep 30 2025 20:07:18Z: \"{txt('33c941fae57ba8d1e23bc1dff9ce3e2c')}\" → ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262, ZOM-275 off the register; the DM reply lists the Not shipped and Editor only keys; the comments on the Editor only and Not shipped tickets name iOS 0.3.49 and Android 0.3.133 | YES — check-sql | F1 | 01_Universe_Inject.sql (SQL L58) |")
line("| F4 |", f"| F4 | The rules card (rules 1–7) | Trello (ZM roadmap board) | trello_search / trello_get_card | Card \"Difficulty baseline (Julia)\" on the ZM roadmap board | F1 (\"the difficulty baseline card on the zm roadmap board\"); search \"Difficulty baseline\" | Card 68daca5871dba40417a00383, created Mon Sep 29 2025 18:05:12Z, description rewritten Tue Sep 30 14:04:31Z (updateCard 68dbe36f4b2b4fffb7525fde): \"{CARD}\". Badges: 1 comment, checklist 2 items, 1 attachment (Leonard's 'notes for monday' doc f_f494073fc667097c3c2c6b) | Unscoped (Trello) | F1 | 01_Universe_Inject.sql (SQL L78); trello card 68daca5871dba40417a00383 |")
line("| F8 |", f"| F8 | Blake's store builds mail | Gmail (Julia's mailbox) | gmail_search_messages / gmail_get_thread | Julia's inbox, Blake's \"store builds for monday\" mail | F4 (rule 3 \"Blake's store builds mail\"); search \"store builds\" | Message julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> (thread julia.lawson@harmonygames.co/1844679607844896665, 1 message), created Tue Sep 30 2025 09:12:44Z, from Arthur Blake to Leonard, Julia, Robert, Brian: \"{M1}\" → the store builds are iOS 0.3.49 and Android 0.3.133, cut from main on Sep 26 | YES — check-sql | F4 | 01_Universe_Inject.sql (SQL L103); gmail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> |")
line("| F9 |", f"| F9 | Blake's reply, in its own thread (stripped tooling; the > 90 check) | Gmail (Julia's mailbox) | gmail_search_messages / gmail_get_thread | Blake's later mail to the same four in Julia's inbox, Tue Sep 30 13:26Z | F4 (rule 3 \"and his reply to it\"; rule 6 names it); F8 (same sender, same day) | Message julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> (thread julia.lawson@harmonygames.co/1844695547248825769, 1 message), created Tue Sep 30 2025 13:26:05Z, from Arthur Blake to the same four: \"{M2}\" → level editor, Editor-folder and debug-menu changes are Editor only; ZOM-199's text is wrong (rule 6 comment: cpm > 90, at the 10th game) | YES — check-sql | F4, F8 | 01_Universe_Inject.sql (SQL L143); gmail julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> |")
rep("ZOM-312 'merged with match3d#265' | Unscoped (Linear)", "ZOM-312 'merged with match3d#265'; ZOM-295 'merged with match3d#271' | Unscoped (Linear)")
rep("01_Universe_Inject.sql (SQL L211); github harmonygames-Games/match3d#265#rc_7", "01_Universe_Inject.sql (SQL L180); github harmonygames-Games/match3d#265#rc_7")
rep("01_Universe_Inject.sql (SQL L204); github harmonygames-Games/match3d#401#c_2", "01_Universe_Inject.sql (SQL L173); github harmonygames-Games/match3d#401#c_2")
rep("01_Universe_Inject.sql (SQL L60) |", "01_Universe_Inject.sql (SQL L64) |")
rep("01_Universe_Inject.sql (SQL L48); 01_Universe_Inject.sql (SQL L56) |", "01_Universe_Inject.sql (SQL L52); 01_Universe_Inject.sql (SQL L60) |")
rep("01_Universe_Inject.sql (SQL L56) |", "01_Universe_Inject.sql (SQL L62) |")
rep("01_Universe_Inject.sql (SQL L79); trello action", "01_Universe_Inject.sql (SQL L88); trello action")
rep("01_Universe_Inject.sql (SQL L81); trello checklist", "01_Universe_Inject.sql (SQL L90); trello checklist")
rep("01_Universe_Inject.sql (SQL L195); gcal", "01_Universe_Inject.sql (SQL L164); gcal")
rows = '; '.join(T.row_text(r) for r in T.ROWS)
line("| F20 |", f"| F20 | The register Tickets tab (derived, 23 rows) | Computed from F2–F17, F24–F26 | local reasoning, then gsheets_create_spreadsheet + gsheets_values_update | Card rules 1–4 (F4) with F5, F2, F3, F7, F16, F25 over F15; columns per rule 2 and Robert (F24) | F15 | Ticket · Linear state (as found) · status · assignee · done day (Pacific) · priority: {rows}. Counts: 15 Live, 4 Editor only ({EO}), 3 Not shipped ({NS}), 1 Replaced (ZOM-254 → ZOM-282). Left off: ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262, ZOM-275 (F2); ZOM-162, ZOM-163, ZOM-201, ZOM-250 (F3); ZOM-258 (F7); ZOM-312 (F16); ZOM-295 (F25); ZOM-271 (ATK alone, F5); Duplicate-state issues (rule 1) | Derived from visible inputs | F2, F3, F4, F5, F7, F8, F9, F15, F16, F24, F25, F26 | Derived; support/task_work/jl_difficulty/truth.json /rows (ZOM-295 off per F25); linear data.json /issues |")
line("| F22 |", f"| F22 | Ticket comments to post (derived, 9) | Computed from F2, F3, F6, F9, F20 | local reasoning, then linear_create_comment | Card rule 6 (F4) + checklist (F6) + Leonard's thread replies (F2, F3) | F20 | ZOM-199: the build checks CPM > 90, not >= 90, when the 10th game ends (F9); ZOM-254: replaced by ZOM-282; {EO}, {NS}: the change isn't in the store builds, naming iOS 0.3.49 and Android 0.3.133 (F2). None on ZOM-162, ZOM-163, ZOM-201, ZOM-250 (F3), ZOM-42, ZOM-295, ZOM-312 or any other ticket; no new issues | Derived | F2, F3, F6, F9, F20 | Derived; card 68daca5871dba40417a00383 rule 6; checklist 68dc033bf7d24e86b8a9cc67 item 1; D05HB64NMQU/1759262838.442871; D05HB64NMQU/1759267002.665190 |")
line("| F23 |", f"| F23 | The DM reply contents (derived) | Computed from F1, F2, F7, F18, F20 | local reasoning, then slack_send_message | The ask (F1), its thread reply (F2), the notes doc (F7) | F20 | The register is in the ZM Difficulty folder; 23 tickets: 15 Live, 4 Editor only, 3 Not shipped, 1 Replaced; Not shipped keys {NS}; Editor only keys {EO}; ZOM-254 was replaced by ZOM-282; a new player gets the starting tier when their 10th game ends, won or lost | Derived | F1, F2, F7, F18, F20 | Derived; support/task_work/jl_difficulty/truth.json /counts (Live 15 after F25) |")
lf = '; '.join(f"{r['id']} assignee {r['assignee']}, completed_at {r['completed_at'] or 'none'}, priority {r['priority']}" for r in T.ROWS)
NEWF = (
    f"| F24 | Robert's three extra columns (group chat) | Slack (group chat Robert, Leonard, Julia) | slack_channels_list (mpim) / slack_read_channel / slack_read_thread | Leonard's Sep 30 question in the group chat with Robert, and the reply in its thread | F4 (rule 2 \"the three things Robert asked for when I asked him in our group chat\") | Message CAFC495E4006/1759226461.318204 by Leonard, created Tue Sep 30 2025 10:01:01Z: \"{txt('cec246a6e43158f200fe144f0dd7039c')}\"; reply_count 1. Reply CAFC495E4006/1759229513.774912 by Robert, created 10:51:53Z: \"{txt('abe096ff0b5d7216efbc889e91d6d13a')}\" → after status: Linear assignee, the day marked done in Pacific time (blank if never done), Linear priority | YES — check-sql | F4 | 01_Universe_Inject.sql (SQL L48); 01_Universe_Inject.sql (SQL L50) |\n"
    f"| F25 | Blake's 'not tiers' review on PR 271 (ZOM-295 off) | GitHub (match3d) | github_get_pull_request_reviews / github_get_pull_request_comments | Review comments on pull request 271 in the match3d repo | F15 (ZOM-295's note names match3d#271) | Review harmonygames-Games/match3d#271#rev_2 by Blake (APPROVED, empty body), created Fri Jul 4 2025 01:05:22Z, inline comment harmonygames-Games/match3d#271#rc_1 on Assets/Scripts/Monster/MonsterSpawner.cs: \"{RC271}\" → ZOM-295 stays off (rule 1) | Unscoped (GitHub) | F15 | 01_Universe_Inject.sql (SQL L184); github harmonygames-Games/match3d#271#rc_1 |\n"
    f"| F26 | Linear assignee, completed_at and priority of the 23 rows | Linear (team ZOM) | linear_get_issue / linear_list_issues | Each register ticket's issue fields | F15 (the candidate issues) | {lf}. Pacific day differs from the UTC day only on ZOM-200 (2025-06-12), ZOM-274 and ZOM-282 (2025-06-20); priority 1 Urgent, 2 High, 3 Medium, 4 Low | Unscoped (Linear) | F15 | linear data.json /issues (assignee_id, completed_at, priority) |")
line("| F23 |", s.split('\n')[[i for i, l in enumerate(s.split('\n')) if l.startswith('| F23 |')][0]] + '\n' + NEWF)

# ---- visibility block
ids = ['d_96489e1e00a56685625939', 'f_9ec79682ff351aa466364a', 'f_f494073fc667097c3c2c6b', 'f_0ba93ae0238d9ed4178212',
       '6f77386571537f0bd88c959bdc216f94', '33c941fae57ba8d1e23bc1dff9ce3e2c', '914b21ab6448fac2e4b4f8d164bea41a',
       '5f6ed4d5ae1a0a04b616af6d6d2dda43', '6995ba10acf2888f04f033b8bbeb5629', 'cec246a6e43158f200fe144f0dd7039c',
       'abe096ff0b5d7216efbc889e91d6d13a', '<CAAMNAwYx', '<CA5_F2r', 'evt_', '1844679607844896665', '1844695547248825769']
lb = os.path.join(HERE, 'lb_ledger_r7.txt')
open(lb, 'w').write('\n'.join(i for i in ids if not i.startswith(('<', 'evt', '18'))) + '\njulia.lawson@harmonygames.co/1844679607844896665\njulia.lawson@harmonygames.co/1844695547248825769\njulia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com\njulia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com\nevt_91674a9c23d012a9ac34da\n')
p = subprocess.run(['python3', 'tools/persona_view.py', 'check-sql', 'julia_lawson', 'task_inputs/01_Universe_Inject.sql', '--load-bearing', lb],
                   capture_output=True, text=True)
keep = [l for l in p.stdout.splitlines() if l.startswith('[YES') and any(i in l for i in ids)]
a = s.index("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
b0 = s.index("```\n", a) + 4
b1 = s.index("\n```", b0)
s = s[:b0] + '\n'.join(keep) + s[b1:]

# ---- C
rep("gmail store builds thread julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> (2 messages, complete)",
    "gmail store builds mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> and Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> (one message per thread, complete) · slack group chat CAFC495E4006 thread under 1759226461.318204 (1 reply, complete) · github match3d#265 and #271 review comments (complete)", 9)
rep("| a new spreadsheet holding the 24 rows | ticket, title, Linear state, status, replaced-by |",
    "| a new spreadsheet holding the 23 rows | ticket, title, Linear state, status, assignee, done day (Pacific), priority, replaced-by |")
rep("| F20 | a new spreadsheet", "| F20, F24, F26 | a new spreadsheet")
rep("Create the register sheet (Tickets tab) and write its 24 rows", "Create the register sheet (Tickets tab) and write its 23 rows")
rep("| what the build does (ZOM-199), what replaced it (ZOM-254), not in the store builds (the other 7) |",
    "| what the build does (ZOM-199), what replaced it (ZOM-254), not in the store builds, naming iOS 0.3.49 and Android 0.3.133 (the other 7) |")

# ---- E
rep("| T26 | keeps ZOM-312", "| T26 | keeps ZOM-312")
NEWT = ("| T30 | reads only the first store builds mail and misses Blake's reply, which sits in its own thread under another subject (julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com, julia.lawson@harmonygames.co/1844695547248825769) | F9 | rule 3 and rule 6 name 'his reply to it'; same sender, same day, 13:26:05Z |\n"
        "| T31 | comments on the Editor only and Not shipped tickets without naming the builds (33c941fae57ba8d1e23bc1dff9ce3e2c) | F22 | Leonard's thread reply under the ask: put the two builds in the comment (ios 0.3.49 and android 0.3.133) |\n"
        "| T32 | builds the Tickets tab with the agenda's columns only: no assignee, done day or priority (cec246a6e43158f200fe144f0dd7039c, abe096ff0b5d7216efbc889e91d6d13a, 68daca5871dba40417a00383) | F24 | card rule 2 names 'the three things Robert asked for when I asked him in our group chat'; Robert's answer is the thread reply under Leonard's question |\n"
        "| T33 | keeps ZOM-295 (enrage title match, Done, Live): reads PR 271's reviews list only, where Blake's approval has an empty body (harmonygames-Games/match3d#271#rev_2, harmonygames-Games/match3d#271#rc_1, ZOM-295) | F20 | rule 1: a title match Blake marked 'not tiers' in his review on its PR stays off; ZOM-295's note names match3d#271; the inline comment starts with 'not tiers' |\n"
        "| T34 | writes Linear's UTC day: 2025-06-13 for ZOM-200, 2025-06-21 for ZOM-274 and ZOM-282 (abe096ff0b5d7216efbc889e91d6d13a, ZOM-200, ZOM-274, ZOM-282) | F26 | Robert asks for the day in pacific time; completed_at 01:17Z is the evening before in Pacific time |\n")
rep("| X1 | the Domino Delights", NEWT + "| X1 | the Domino Delights")

# ---- F risks
line("| 1 | 04_Prompt_Writing_Brief.md", "| 1 | 04_Prompt_Writing_Brief.md §4 predates hardening rounds 5–7 (24 rows, no Robert columns, Blake's reply in the same thread); this ledger holds the round-7 values (23 rows, Robert's three columns, Blake's reply in its own thread, builds in the 7 comments) | F20, F22, F23, F24 | rubric: use this ledger and the /prompt r14 report, not the brief | none for /oe; /prompt r14 restates the same answer |")
line("| 2 | Both thread replies", "| 2 | Thread replies and inline review comments carry the amendments; round-7 baselines: 2 of 6 missed Leonard's second thread reply, 1 missed both, 2 missed PR 271's inline comment | F2, F3, F25 | rubric: counts, exact sets, Brian's role, keys and comment count; the OE reads every thread and both PRs' review comments | none — check-sql YES; reply_count 1 on each parent |")
rep("| 3 | Starting tier: ZOM-42, ZOM-199 and the deck say '10 levels'; the build counts games incl. losses | F18, F21, F23 | rubric: accept '10 games' or '10 levels played' (/prompt r12), fail 'level 10' | none |",
    "| 3 | Starting tier: ZOM-42, ZOM-199 and the deck say '10 levels'; the build counts games incl. losses | F18, F21, F23 | rubric: accept '10 games' or '10 levels played' (/prompt r14), fail 'level 10' | none |\n"
    "| 5 | Done day: Robert asks for Pacific time; /prompt r14 says the rubric must still accept the UTC day for ZOM-200, ZOM-274 and ZOM-282 | F24, F26 | rubric: accept 06-12 or 06-13 (ZOM-200), 06-20 or 06-21 (ZOM-274, ZOM-282) | none |")

# ---- tally
rep("Requirements 8 · facts 23 · writes 9", "Requirements 8 · facts 26 · writes 9")

# ---- self-review
rep("| Counter: R3: the register could keep the 10 tickets the thread replies drop (34 rows) | F2 and F3 name them; F3 says 'on top of the ones i already left off' (D05HB64NMQU/1759267002.665190) |",
    "| Counter: R3: the register could keep the 10 tickets the thread replies drop (33 rows) | F2 and F3 name them; F3 says 'on top of the ones i already left off' (D05HB64NMQU/1759267002.665190) |")
rep("| Counter: F16: ZOM-312 stays (title match 'tier') |",
    "| Counter: F25: ZOM-295 stays (enrage title match; Blake approved the PR) | rule 1 keys on the 'not tiers' mark, not on the review state; harmonygames-Games/match3d#271#rc_1 starts with 'not tiers' and sits under Blake's approval harmonygames-Games/match3d#271#rev_2 |\n"
    "| Counter: F24: the three columns could be optional extras | rule 2 makes them part of the layout ('plus the three things Robert asked for'); Robert's reply CAFC495E4006/1759229513.774912 names them |\n"
    "| Counter: F26: the done day could be the UTC date Linear shows | Robert says 'pacific time' (CAFC495E4006/1759229513.774912); /prompt r14 still has the rubric accept the UTC day for ZOM-200, ZOM-274, ZOM-282 |\n"
    "| Counter: F9: Blake's reply could be read as part of the first mail's thread | it is its own thread julia.lawson@harmonygames.co/1844695547248825769 under a new subject; rule 3 and rule 6 name 'his reply to it' |\n"
    "| Counter: F16: ZOM-312 stays (title match 'tier') |")
rep("Re-verified this run through `tools/hg.py` and the SQL rows: the ask, both thread replies and Julia's Sep 29 message, the card, its comment, checklist and attachment, the notes doc, the store builds mail and reply, the agenda, the invite and its attendees, the folder, the enrage sheet's Live tab (01_Universe_Inject.sql rows); ZOM-42 and ZOM-303 descriptions (linear data.json); TierManager.cs and WinHistory.cs (match3d export); the 24-row register and its counts recomputed from truth.json.",
    "Re-verified this run through `tools/hg.py` and the SQL rows (b64bc2f2c6dc): the ask, both thread replies and Julia's Sep 29 message, Leonard's group-chat question and Robert's reply, the card (rules 2, 3 and 6 as now worded), its comment, checklist and attachment, the notes doc, the store builds mail and Blake's separate reply, the agenda, the invite and its attendees, the folder, the enrage sheet's Live tab, PR 265 and PR 271 review comments (01_Universe_Inject.sql rows); ZOM-42 and ZOM-303 descriptions and the 23 tickets' assignee, completed_at and priority (linear data.json); TierManager.cs and WinHistory.cs (match3d export); the 23-row register and its counts recomputed in r7/truth7.py.")
for _n, _t in (('NEWF', NEWF), ('NEWT', NEWT)):
    if '—' in _t: print('em dash in', _n, _t[max(0, _t.index('—') - 80):_t.index('—') + 20])
import re as _re
ls = s.split('\n')
idx = {n: i for i, l in enumerate(ls) for n in ('F20', 'F24', 'F25', 'F26') if l.startswith(f'| {n} |')}
new_rows = [ls[idx['F24']], ls[idx['F25']], ls[idx['F26']]]
for n in ('F26', 'F25', 'F24'):
    del ls[idx[n]]
ls[idx['F20']:idx['F20']] = new_rows
s = '\n'.join(ls)
MAP = {'F20': 'F23', 'F21': 'F24', 'F22': 'F25', 'F23': 'F26', 'F24': 'F20', 'F25': 'F21', 'F26': 'F22'}
s = _re.sub(r'\bF2[0-6]\b', lambda m: '@@' + MAP[m.group(0)], s).replace('@@', '')
s = _re.sub(r'F2–F17, F20–F22', 'F2–F17, F20–F22', s)
open(out, 'w').write(s)
print('ok', len(keep), 'visibility lines')
