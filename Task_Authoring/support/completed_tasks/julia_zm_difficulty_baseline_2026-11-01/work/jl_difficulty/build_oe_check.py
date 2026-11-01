"""Writes task_inputs/Working_Files/08_OE_Check.md (check mode) for the current 08_Oracle_Events.md."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
OE = open(os.path.join(TI, '08_Oracle_Events.md')).read()
SQL = open(os.path.join(TI, '01_Universe_Inject.sql')).read()
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
ev = {int(m.group(1)): m.group(2) for m in re.finditer(r"^OE (\d+)  (.+)$", OE, re.M)}
n = len(ev)
JUL = 'julia.lawson@harmonygames.co'
GB, GR = f"{JUL}/{M['G_BUILD']['message_id']}", f"{JUL}/{M['G_BUILD_RE']['message_id']}"
loc = lambda k: f"{M[k]['channel']}/{M[k]['ts']}"


def find(rx):
    return [k for k, v in ev.items() if re.search(rx, v)]


def span(s):
    assert s in OE, s
    return f"\"{s}\""


def sline(x):
    k = [i for i, l in enumerate(SQL.splitlines(), 1) if x in l]
    return f"01_Universe_Inject.sql SQL L{k[0]}" if k else "01_Universe_Inject.sql"


calc = min(find(r"^Work out the register"))
cm = find(r"^Comment on ZOM-")
sh = find(r"^Share the register")
rp = min(find(r"^Reply to Leonard"))
cr8 = min(find(r"^Create the register"))
L = []
w = L.append
w("# 08 OE Check — jl-zm-difficulty-baseline")
w(f"Checked 2026-10-31 · Events {n} · Characters {len(OE)} (300–50,000: ok) · Ledger 2026-10-31 (08_OE_Writing_Ledger.md, oe-writing PASS)")
w("/oe prediction (a prediction only; /oe gives the verdict): PASS 5")
w("Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE\n")

w("## Inventory")
w("| Segment (quoted start) | Role | Event |\n|---|---|---|")
for a, b, s in [(1, 3, "Read Julia's DM with Leonard"), (4, 7, "Find the rules card the ask names"),
                (8, 13, "Read Blake's store builds mail"), (14, 21, "Read ZOM-42, the tier spec"),
                (calc, calc, "Work out the register from rules 1–4"), (cr8, min(sh) - 1, "Create the register spreadsheet"),
                (min(sh), max(sh), "Share the register with Robert"), (min(cm), max(cm), "Comment on ZOM-199"),
                (rp, rp, "Reply to Leonard in the DM")]:
    w(f"| {span(s)} | STEP (×{b - a + 1}) | OE {a}–{b} |" if a != b else f"| {span(s)} | STEP | OE {a} |")
w("\nNo CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segments: every event is a read, one calculation or one write.\n")

w("## Coverage")
w("| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |\n|---|---|---|---|")
COV = [
 ("R1 / F1 Leonard's ask and the DM history", "OE 1", "covered", "ledger: DM history"),
 ("R2 / F2 reply under the ask", "OE 2", "covered", "ledger: thread replies of the ask"),
 ("R2 / F3 reply under Julia's Sep 29 question", "OE 3", "covered", "ledger: thread replies of Julia's message"),
 ("R2 / F4–F7 card, comment, checklist, notes doc", "OE 4–7", "covered", "ledger: Trello card, actions, checklists, attachment → Docs"),
 ("R2 / F8–F9 store builds mail and reply", "OE 8", "covered", "ledger: one Gmail thread read"),
 ("R2 / F10–F13 agenda, invite, folder, enrage sheet", "OE 9–12", "covered", "ledger: Docs, Calendar, Drive, Sheets"),
 ("R2 / deck and Blake's enrage note (rule 5 sources)", "OE 13, 16", "covered", "ledger F19: Slides, Slack search"),
 ("R2 / F14 ZOM-42; F18 build code", "OE 14–15", "covered", "ledger: Linear issue, GitHub file contents"),
 ("R2 / F15 population and notes", "OE 17–18", "covered", "ledger: list team ZOM issues to the end, comments per issue"),
 ("R2 / F16–F17 the four title-match PRs' reviews (243, 244, 265, 271), PR 401 comment; F19 ZOM-303", "OE 19–21", "covered", "ledger: GitHub reviews/comments on every title-match PR, Linear issue"),
 ("R3 / F20–F21 register and rules tab", f"OE {calc}, {cr8}–{cr8 + 3}", "covered", "ledger: calculation, create, write rows, add tab, write rules"),
 ("R4 / F13 folder", f"OE {cr8 + 4}", "covered", "ledger: move into the folder (creating it there is another valid route)"),
 ("R5 / F12 shares", f"OE {min(sh)}–{max(sh)}", "covered", "ledger: 4 shares, one per event"),
 ("R6 / F22 ticket comments", f"OE {min(cm)}–{max(cm)} ({len(cm)} events)", "covered", "ledger: one comment per ticket"),
 ("R7 / F23 DM reply", f"OE {rp}", "covered", "ledger: DM message (thread or top level)"),
 ("R8 act without asking", "all writes", "covered", "constraint: no event asks Julia"),
]
for r in COV:
    w("| " + " | ".join(r) + " |")
w("")

w("## Expected-data sign-off")
w("| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Match / minor / wrong / unresolved |\n|---|---|---|---|---|")
SO = [
 ("tell me when a new player gets their starting tier", f"{sline(M['S_ASK']['ts'])}; {loc('S_ASK')}", "seeded ask, Sep 30 19:48:26Z", "match"),
 ("forgot one thing: leave the analytics and tutorial tickets off the list", f"{sline(M['S_ASK_REPLY']['ts'])}; {loc('S_ASK_REPLY')}", "reply Sep 30 20:07:18Z", "match"),
 ("take 162, 163, 201 and 250 off the list too", f"{sline(M['S_JQ_REPLY']['ts'])}; {loc('S_JQ_REPLY')}", "reply Sep 30 21:16:42Z", "match"),
 ("The card shows 1 comment, a checklist with 2 items and 1 attachment", f"{sline('68daca5871dba40417a00383')} badges_json", "comments 1, checkItems 2, attachments 1", "match"),
 ("ATK on its own doesn't", f"{sline(M['T_H1CMT']['id'])}; trello {M['T_H1CMT']['id']}", "comment Sep 30 15:41:55Z", "match"),
 ("rule 7 change: Brian gets edit as well", f"{sline(M['T_H1CL']['id'])}; trello {M['T_H1CL']['id']}", "checklist Sep 30 16:20:11Z", "match"),
 ("leave ZOM-258 off the list", f"{sline(M['DOC_LEO_NOTES']['id'])}; {M['DOC_LEO_NOTES']['id']}", "doc owner Leonard, Julia reader", "match"),
 ("Arthur Blake to Leonard, Julia, Robert and Brian", f"{sline(M['G_BUILD']['message_id'])}; {GB}", "to Julia, Leonard, Robert, Brian", "match"),
 ("the starting tier check in the build is cpm > 90, not >= 90", f"{sline(M['G_BUILD_RE']['message_id'])}; {GR}", "Sep 30 13:26:05Z", "match"),
 ("One sheet with two tabs, Tickets and Rules in force", f"{sline(M['DOC_AGENDA']['id'])}; {M['DOC_AGENDA']['id']}", "agenda body", "match"),
 ("brian.foster@harmonygames.co. So the shares go to", f"{sline(M['GCAL_TUNING']['copies'][JUL])}; {M['GCAL_TUNING']['copies'][JUL]}", "5 attendees incl. Julia", "match"),
 ("Folder \"ZM Difficulty\", created Jun 13 2025; Julia can write to it", f"{sline(M['FOLDER_ZMDIFF']['id'])}; {M['FOLDER_ZMDIFF']['id']}", "permissions julia writer", "match"),
 ("Mailman, Mayor2, PartyGirl (incl. PartyGirl 50HP): speed not copied yet", f"{sline(M['SHEET_KNOBS']['id'])}; {M['SHEET_KNOBS']['id']}#0", "Live tab last row", "match"),
 ("90 or more starts you on tier 1", f"{sline(M['CONF_DDA']['id'])}; {M['CONF_DDA']['id']}", "deck slide text", "match"),
 ("enrage adds speed and damage only", f"{sline(M['CC_ART']['ts'])}; {loc('CC_ART')}", "Blake Sep 3 15:22:09Z", "match"),
 ("We promote if if win rate is 80% or higher", "hg.py get linear --file data.json /issues ZOM-42 description", "verbatim incl. the doubled 'if'", "match"),
 ("if (totalGames == 10)", "HarmonyGames_GitHub match3d Assets/Scripts/DynamicDifficulty/TierManager.cs line 31", "line 31", "match"),
 ("return GetTotalWins() + GetTotalLosses();", "match3d Assets/Scripts/Player/WinHistory.cs line 166", "line 166", "match"),
 ("ZOM-203 and ZOM-276 also match but are Duplicates", "hg.py get linear --file data.json /issues ZOM-203, ZOM-276 state Duplicate", "Duplicate", "match"),
 ("31 title matches that are not in the Duplicate state", "linear data.json /issues: 33 ZOM title matches up to Aug 31 minus 2 Duplicates", "31", "match"),
 ("tiers: closing. checked on the dev build", f"{sline('cmt_df69e4a92767cbff0000')}; cmt_df69e4a92767cbff0000", "Blake on ZOM-281, Jun 27", "match"),
 ("no other comment on a ZOM issue starts with", "hg.py search linear \"tiers:\" over linear data.json /comments → 0 base hits; seeded only the 5", "5", "match"),
 ("not tiers: this is level settings tooling for the designers", f"{sline('#265#rc_7')}; harmonygames-Games/match3d#265#rc_7", "inline comment, empty-body review #265#rev_8", "match"),
 ("PR 243 has no reviews, and PRs 244 and 271 have only the automated review bot's reviews", "github data.json /reviews for match3d PRs 243, 244, 271 (bot PERSON_6026_GITHUB_USERNAME, 'Actionable comments posted')", "243: none; 244: 2 bot; 271: 1 bot", "match"),
 ("Only four title matches have a PR in the match3d repo", "github data.json /pull_requests: titles and bodies naming the 31 title matches → match3d#243, #244, #265, #271 only", "4 PRs", "match"),
 ("because the build (OE 15) sets the tier when the player's 10th game ends", "TierManager.cs line 31 (read in OE 15, before OE 16)", "totalGames == 10", "match"),
 ("they shared one since ZOM-282", f"{sline('#401#c_2')}; harmonygames-Games/match3d#401#c_2", "Aug 25 17:02:28Z", "match"),
 ("we also need to demote the level difficulty for the level", "hg.py get linear --file data.json /issues ZOM-303 description", "substring of the Solution line", "match"),
 ("Counts: 16 Live, 4 Editor only (ZOM-173, ZOM-200, ZOM-277, ZOM-315), 3 Not shipped (ZOM-202, ZOM-280, ZOM-293)", "support/task_work/jl_difficulty/truth.json /counts", "16/4/3/1", "match"),
]
for claim, ptr, val, res in SO:
    pos = OE.index(claim)
    e = len(re.findall(r"^OE \d+  ", OE[:pos], re.M))
    w(f"| OE {e} | {span(claim)} | {ptr} | {val} | {res} |")
w("")

w("## Findings")
w("| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |\n|---|---|---|---|---|---|---|---|")
FND = [
 ("1", "ADVISORY", "Readability", "OE 18", "Read the comments on every ZOM issue created up to Aug 31",
  "screen 44 (population reads may stay one event)", "one read over ~498 issues makes a long event; allowed", "F15; cmt_df69e4a92767cbff0000"),
 ("2", "ADVISORY", "Route", f"OE {cr8 + 4}", "Move the spreadsheet into the ZM Difficulty folder",
  "Eval 3.1 (any valid route)", "a run that creates the file inside the folder needs no move; both reach the same end state", "F13; d_96489e1e00a56685625939"),
]
for r in FND:
    w("| " + " | ".join(r[:4]) + f" | {span(r[4])} | " + " | ".join(r[5:]) + " |")
w("")

w("## Pre-verdict sweep")
w("| Eval 4.0 check (7) | Result |\n|---|---|")
for a, b in [("one wrong count/ID/channel/tool", "none: 31 title matches, 24 rows, 16/4/3/1, 5 attendees, 9 comments re-read (sign-off)"),
             ("one missing write", f"none: create, rows, tab, rules, move, {len(sh)} shares, {len(cm)} comments, 1 DM reply"),
             ("one Expected fact with no retrieving event", f"none: every value in OE {calc} and the writes is read in OE 1–{calc - 1}; the Brian recap trap was removed from OE 8 because no event reads it"),
             ("one act-vs-defer conflict", "none: ledger §C defer search complete"),
             ("one non-action or final-response event", f"none: OE {calc} is a calculation with stated results"),
             ("one prompt-forbidden write", "none: no comment on ZOM-162/163/201/250, no new issues, Brian not writer"),
             ("one missing recovery/wait event", "none: Friction: none (03_Error_Async_Config.txt)")]:
    w(f"| {a} | {b} |")
w("")
w("## Advisory (no effect on the prediction)")
w("| Event | Note |\n|---|---|")
w(f"| all | the field blocks pasting: {len(OE)} characters to type; long quotes (OE 4, 8, 18) can be trimmed to the decisive sentences if needed |\n")
w("## Tally")
w("Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 2\n")

w("## Self-review")
w("Walked `Evals/2_Oracle_Events_Eval.md` 1.2, 1.3, the HARD GATE, 2.1–2.7, 3.1–3.6 and 4.0 in order against this report; re-verified the "
  "sign-off values this run through `tools/hg.py` reads, the match3d export and the SQL rows. Fixed after /oe r1 (NON-FAIL 3, Accuracy 3; 6adfee3ef9092601a61245bb_2_oe.md): finding 1 OE 13 → the deck now follows the code read as OE 16 and cites OE 8 (> 90), OE 15 (10th game) and OE 13 (blunder line) for each stale value; finding 2 OE 19 → checks all four title-match PRs (243, 244, 265, 271), only 265 has a not-tiers review; OE 22 gives a reason per non-Live row (/oe readability advice). Sweep: every other (OE n) citation re-checked and points to an earlier event that holds the value. Earlier fixes in the events: OE 1 'a few "
  "messages back' → 'the message just before it' (the DM has no other September messages); OE 18's closing-note summary narrowed to the title "
  "matches; OE 8's Brian-recap trap removed (no event retrieved it).\n")
w("| Counter-reading | Resolution (evidence) |\n|---|---|")
CR = [
 ("R1 covered: OE 1 could read the wrong DM message", f"the ask is the newest message before the clock in the DM ({loc('S_ASK')})"),
 ("R2 F2: the reply might not be reachable", "reply_count 1 on the ask; check-sql YES (ledger §B)"),
 ("R2 F3: Julia's Sep 29 thread could be ignored as her own", f"its reply is Leonard's ({loc('S_JQ_REPLY')}), the latest instruction"),
 ("R2 F4–F7: the DD card could be the one meant", "the ask says 'on the zm roadmap board'; the DD card is on another board (683dbef4e319167a802bd888)"),
 ("R2 F8: the mail's first message alone suffices", f"the > 90 fact is only in the reply ({GR})"),
 ("R2 F10–F13: the invite could need Robert only", "rule 7 'everyone on the tuning session invite'; 5 attendees (evt_91674a9c23d012a9ac34da)"),
 ("R2 deck: OE 13 is redundant", "rule 5 names the deck; its stale values are traps the later events overturn; /oe does not score redundancy"),
 ("R2 F14/F18: ZOM-42's '10 level' governs the timing", "rule 5 'go by the build' for the starting tier; TierManager.cs line 31"),
 ("R2 F15: the population could be title matches only", "rule 1 adds 'tiers:' notes on any ticket; ZOM-281 has no title word (cmt_df69e4a92767cbff0000)"),
 ("R2 F16–F17: #401 replaces ZOM-282", "rule 4 'PRs that change or split its numbers don't' (harmonygames-Games/match3d#401#c_2)"),
 ("R3 F20: 28 rows (no Sep 29 thread)", f"OE 3 drops four more ({loc('S_JQ_REPLY')})"),
 ("R4 F13: the move is missing for a create-in-folder run", "Eval 3.1 credits any valid route (Finding 2)"),
 ("R5 F12: Brian writer per the checklist", "Leonard's 21:16Z reply takes it back; OE 6 and OE 3 say so"),
 ("R6 F22: comments on the four dropped tickets", "'no comments on them either' (OE 3)"),
 ("R7 F23: keys should include the dropped Editor only tickets", "they are off the list; the reply lists the register's keys"),
 ("R8: OE should confirm with Julia", "the prompt says 'no need to check with me first'"),
 ("/oe r1 finding 1: OE 16 (deck) still cites a later event", "the deck moved after the code read; it cites OE 8, OE 13, OE 14, OE 15, all earlier (f_048bf5e69f8e7f1a659a5c)"),
 ("/oe r1 finding 2: another title match could have a PR with a not-tiers review", "only 4 PRs name a title-match key (match3d#243, #244, #265, #271); only harmonygames-Games/match3d#265#rc_7 says not tiers"),
 ("OE 22 reasons could add an unretrieved fact", "each reason cites OE 8 or OE 18 (cmt_bb9c4deb176b2c894ca6 ZOM-173, cmt_b0aa45d307c981ce4487 ZOM-277)"),
 ("Finding 1 ADVISORY could be MULTIPLE_ACTIONS", "a population read is not two writes (screen 44); F15, cmt_df69e4a92767cbff0000"),
 ("Finding 2 ADVISORY could be INACCURATE (wrong tool)", "gdrive_move_file exists in the catalog with fileId and newParentId; F13, d_96489e1e00a56685625939"),
]
for a, b in CR:
    w(f"| Counter: {a} | {b} |")
w("\nUnresolved: none.\n")
w("## Reminders")
w("- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.")
w("- Type the events exactly as saved in 08_Oracle_Events.md, then run /oe.\n")
dst = os.path.join(TI, 'Working_Files', '08_OE_Check.md')
open(dst, 'w').write("\n".join(L) + "\n")
print('wrote', dst, n, len(OE))
