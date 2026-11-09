#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md from truth.json, the SQL ids, the manifest and the saved searches.
Facts, requirements and locators only: no prompt text. Re-run after any SQL or truth change, then the stage gate."""
import collections, json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
P = json.load(open(os.path.join(HERE, "ids.json")))
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
TRUTH = TRUTH.get("rows", TRUTH)
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
EXTRA = json.load(open(os.path.join(HERE, "brief_extra.json"))) if os.path.exists(os.path.join(HERE, "brief_extra.json")) else {}
I, BASE, T, Q, TK, M = P["ids"], P["base"], P["times"], P["quotes"], P["tickets"], P["members"]
SL = IDS["slack_mid"]
SAM = "samuel.turner@harmonygames.co"
QA = IDS["qa_msg"]
PARENT = P["parent"]
HUB, RULE, DECK, SHEET = I["hub"], I["rule_doc"], I["deck"], BASE["pn_sheet"]
LIVE = BASE["liveops_page"]
PN_CARD, TECH = BASE["pn_card"], BASE["tech_card"]
FOLDER = BASE["folder"]
DM = HUB.split("/")[0]
SQL_SHA = __import__("hashlib").sha256(open(os.path.join(TI, "01_Universe_Inject.sql"), "rb").read()).hexdigest()[:12]
rows = {k: v for k, v in TRUTH.items() if v.get("Call")}
by = collections.defaultdict(list)
for k, v in rows.items():
    by[v["Call"]].append(k)
for v in by.values():
    v.sort()
go, hold, drop = by["Go"], by["Hold"], by["Drop"]
off = [k for k, v in TRUTH.items() if not v.get("Call")]
tick = lambda ks: ", ".join(sorted((TK[k] for k in ks if k in TK), key=lambda s: int(s.split("-")[1])))   # noqa: E731
miss = collections.defaultdict(list)
for k in hold:
    miss[rows[k]["What's missing"]].append(k)
askers = collections.defaultdict(list)
for m in M:
    if m["asker"] != "leonard" and not m["source"].startswith("PNs Beta"):
        askers[m["asker"]].append(m)
askers["calvin.price"] += [m for m in M if m["key"] == "Win & Collect start"]      # his ticket predates the parent, and it is his ask
EMAIL = {"brian.foster": "brian.foster@harmonygames.co", "calvin.price": "calvin.price@harmonygames.co", "julia.lawson": "julia.lawson@harmonygames.co",
         "martin.walsh": "martin.walsh@harmonygames.co", "oliver.brooks": "oliver.brooks@harmonygames.co", "owen.baker": "owen.baker@harmonygames.co",
         "robert": "robert@harmonygames.co"}
L = []
A = L.append


def rd(p):
    return open(os.path.join(HERE, p)).read().rstrip()


def fence(t):
    L.extend(["```", t, "```"])


A("# Prompt Brief — samuel_zm_beta_messages · prep")
A(f"> Built 2026-11-05 from 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (sha256 {SQL_SHA}, rev5), 01_Scenario_Design.md, 01_Hardness_Manifest.json, 03_Error_Async_Config.txt (Friction: none). No reference files. Persona view verified: all")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.")
A(f"> **Clock:** 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Samuel's today is Wed Oct 1, 2025. The latest seeded event is Leonard's DM {HUB} ({T['hub']}, Tue Sep 30, 1:40 PM PT). Seed bound 2025-10-01T00:00:00Z.")
A("")
# ---------------------------------------------------------------- 1
A("## 1 · Assignment fit")
A("")
A("Raw assignment: Business Function Design · Persona Samuel Turner, Role: Game Designer · Competency Marketing and GTM · Task Skill Retrieval · Task Type long-horizon · Difficulty Mode medium · Universe Date Oct 1, 2025.")
A("")
A("| Axis | Assigned value | What it requires here (cited) |")
A("|---|---|---|")
A("| Business function | Design → Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay and design requirements) | a designer's call on what the game says to players, by the rule Leonard wrote; the requirement decisions are the plan's Call and Audience columns |")
A(f"| Persona / role | Samuel Turner, {SAM}, Game Designer (roster `samuel_turner`) | Voice: an ordinary colleague request, clean spelling. Remit: Leonard sent him the sheet ({BASE['pns_sent']}), the roadmap card reads '[Feature] Push Notifications - Samuel + Leonard' ({PN_CARD}), he authored {BASE['pr248']}. Read scope: DMs with Leonard, Vincent, Robert, Arthur; #zombie-match3d C0880U9751A, #zombie-bugs C08R27X0EAH, #zombie-art C08R8CHB0QL, #company-internal C05KNDCHAAG; not #executives C07C2866011 |")
A(f"| Competency | Marketing and GTM (taxonomy screen 7: demand and retention, GTM, communications; outputs: memos, spreadsheets, emails) | the job is what players hear and when, to protect D1 and D7 before more money goes behind beta ({HUB}): a retention communications plan plus a team note with the warehouse baseline; a Designer is a listed typical persona. Open risk: most writes are on Linear |")
A(f"| Task skill | Retrieval (find and return specific information across connectors, extracting structured values) | each message's facts come from the sheet, its ticket and comments, the roadmap lists, PR #248 and Slack, assembled into the plan; stacked: Analysis and Synthesis (the rule's ordered tests), Actions (ticket comments and moves, checklist, emails) |")
A(f"| Task type / tier | long-horizon → Long Horizon 100–500+; requester bar: over 130 counted calls per run, corrected average under 80% | 12 services carry weight; volumes: {len(TK)} message tickets each read and written, 35 plan rows, 7 emails; manifest call budget {P['budget_total']} (01_Hardness_Manifest.json), `HARDNESS GATE (extreme): PASS` in the dossier |")
A("| Difficulty mode / date | medium (cap 85%); Oct 1, 2025 | nothing on or after Wed Oct 1 00:00 PT may be described as done |")
A("")
# ---------------------------------------------------------------- 2
A("## 2 · Situation")
A("")
A("| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |")
A("|---|---|---|---|")
A(f"| Leonard wants one straight answer on what the game actually says to players before more money goes behind beta, and doesn't trust the sheet's six Ready | Samuel, in his DM with Leonard | {HUB} | — |")
A(f"| The sheet's two status columns are from June and disagree on four of 14 rows | Samuel, on the PN sheet | {SHEET} (tab PNs Beta, last changed 2025-06-23T07:02:43Z) | — |")
A(f"| Tickets for the messages sit under one parent, six Done and the rest In Review, and people have added asks | Samuel, in Linear | {PARENT} | — |")
A(f"| A readiness deck and a channel post both repeat the six | Samuel | {DECK}, {I['brian_opinion']} | — |")
A("| The iOS prompt debate of Sep 23 | not Samuel | #executives C07C2866011/1758659424.324079 | Samuel is not a member; his visible records are C08R27X0EAH/1758265279.763959 and the Sep 29 post with its reply |")
A("")
A("No cause belongs in the situation. Why the obvious reading is wrong is discovery-only (§5, never in the prompt).")
A("")
# ---------------------------------------------------------------- 3
A("## 3 · Investigation → action")
A("")
A("Questions to resolve (no answers here):")
for i, q in enumerate(["What is on the list: every sheet row and every ask for a new phone message filed on a ticket or card, and what stays off?",
                       "For each message, which of the rule's ordered tests does it pass, and where does it stop?",
                       "What does the client actually schedule, and on which days?",
                       "What counts as reaching a player and as Vincent having seen it?",
                       "What is the latest line for each message that goes, and does the client ship it?",
                       "Who is each message for?", "Which ask already has a ticket under another name, and which has none?",
                       "What happens to a ticket after its call, and has that rule changed?",
                       "What were D1 and D7 for the Sep 15 cohort week on each platform, which lapsed reminders does the client schedule by day, and what is in the client but still on Hold?"], 1):
    A(f"{i}. {q}")
A("")
A("Writes they feed: W1 plan sheet (1–7) → W2 team note (3, 4, 9) → W3 ticket comments (2, 7) → W4 ticket moves (2, 8) → W5 new tickets (5, 7) → W6 checklist (2) → W7 emails to askers (1, 2) → W8 counts to Leonard (W1). No write is a bolt-on: Leonard's DM asks for each.")
A("")
# ---------------------------------------------------------------- 4
A("## 4 · Pinned final state (UGT anchor)")
A("")
A("| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |")
A("|---|---|---|---|---|---|")
A(f"| W1 plan sheet | one row per message, 35 rows; columns Message, Ticket, Call, What's missing, Audience, Final headline, String change; Go 3, Hold 25, Drop 7 | Samuel's Drive folder {FOLDER} | — | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file if needed | {HUB}, {RULE}, {SHEET} |")
A(f"| W2 team note | one page: D1 and D7 for the Sep 15 cohort week, iOS and Android separately; the lapsed reminders the client schedules by day; anything the client already schedules that's still a Hold and why | next to the plan in {FOLDER} | the team | gdocs_create_document | {HUB}, wh_USER_COHORT_RETENTION, {BASE['pr248']} |")
A(f"| W3 ticket comments | the call as a comment on each of the {len(TK)} message tickets, Go ones included | {TK['Win & Collect start']}, DES-315 to DES-{P['last_ticket']} | — | linear_create_comment | {HUB}, {RULE} |")
A(f"| W4 ticket moves | Drop to Canceled ({len(drop)}); Hold to Backlog, unassigned ({len([k for k in hold if k in TK])} with tickets); Go stay as they are ({len(go)}) | the same tickets | — | linear_update_issue | {RULE}, {I['freeze_comment']} |")
A(f"| W5 new tickets | one for each of the two asks with no ticket; one string ticket for the changed line, under {PARENT} | Linear team_DES | — | linear_create_issue | {HUB}, {RULE}, {I['boss_ask']}, {I['gift_ask']}, {I['corr_reply']} |")
A(f"| W6 checklist | a checklist with the {len(go)} Go messages | the push notifications card {PN_CARD} | Vincent ticks it | trello_create_checklist, trello_create_check_item | {HUB} |")
A(f"| W7 emails | one email per person who asked, saying what happened to their asks | mail | {', '.join(EMAIL[k] for k in sorted(EMAIL))} | gmail_send_message | {HUB} |")
A(f"| W8 counts | how many Go, Hold and Drop | Leonard's DM {DM} | leonard.hayes@harmonygames.co | slack_send_message or slack_conversations_add_message | {HUB} |")
A("")
A("| Decision-ambiguity risk | Alternative a careful run could take | What pins it |")
A("|---|---|---|")
for a, b, c in [
    ("which tab", "PNs or PN BETA Translated as well", f"the DM names the PNs Beta tab ({HUB}); the others hold Domino copy ({SHEET})"),
    ("which sheet", "Push Notifications Domino Adventure, which also has a PNs Beta tab", "the DM's sheet is the Zombie Match one with six Ready; f_351b98dfb06f61fb8357d0 has no Ready column"),
    ("what counts as an ask", "Slack asks too, or red dots and in-game popups", f"the DM says filed on a ticket or a card; the rule doc defines a message as what reaches a closed phone ({RULE})"),
    ("a second ticket for Win & Collect", "file a new one because no child of the parent has that name", f"the DM's 'under whatever name'; {LIVE} maps the names; {TK['Win & Collect start']} carries it"),
    ("Done tickets on Hold rows", "leave them Done", f"the rule doc says Hold tickets move ({RULE}); only Go tickets stay as they are"),
    ("Hold state", "Todo, as the rule doc's last sentence says", f"the doc's 'unless the roadmap says otherwise' and Leonard's later comment {I['freeze_comment']}"),
    ("base tickets holding the asks", "move ZOM-542 or ZOM-556, or leave the call there", f"they are not message tickets; the new tickets take the call (DM: 'Anything with no ticket gets one')"),
    ("who gets email", "Leonard too, or one group mail", f"the DM says 'Email each person who asked for something, apart from me' ({HUB}); he hears on Slack"),
    ("the note's scope", "every message still in the client, a total count, or the warehouse's server campaigns", f"the DM asks for the lapsed reminders the client schedules by day and the Holds already in the client ({HUB}); no total is graded, and nothing in the note reads the push stats table"),
    ("where counts go", "a channel, or the sheet only", f"'tell me here' in {HUB}")]:
    A(f"| {a} | {b} | {c} |")
A("")
A("### 4b · Canonical outcome (all fair outcomes)")
A("")
A("| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by | Allowed equivalence class | Material / representational |")
A("|---|---|---|---|---|---|")
B4 = [
    ("W1", "location", f"final parent {FOLDER}", "—", "created there or moved there", "material"),
    ("W1", "name", f"a name about beta messages (no name set in {HUB})", "—", "any name carrying beta, message, PN or player", "representational"),
    ("W1", "header", f"Message · Ticket · Call · What's missing · Audience · Final headline · String change ({HUB})", "—", "same seven names, same order", "material"),
    ("W1", "membership", f"exactly these {len(rows)} ({HUB}): " + "; ".join(sorted(rows)), "—", "record spelling or obvious short forms; a row may use the sheet's or the ticket's name", "material"),
    ("W1", "excluded", "; ".join(sorted(off)) + f" ({RULE}: a message reaches a closed phone; {HUB}: the PNs Beta tab)", "—", "absent", "material"),
    ("W1", "Call = Go", "; ".join(go) + f" (rule: {RULE})", "—", f"Go ({HUB})", "material"),
    ("W1", "Call = Drop", "; ".join(drop) + f" (rule: {RULE})", "—", "Drop", "material"),
    ("W1", "Call = Hold", "the other 25: " + "; ".join(hold) + f" (rule: {RULE})", "—", "Hold", "material"),
    ("W1", "What's missing, not scheduled", "; ".join(miss["not scheduled in the client"]) + f" (Arthur's notes on the tickets; {BASE['pr248']})", "—", "any wording saying the client doesn't schedule it, or test 3", "material"),
    ("W1", "What's missing, server", "; ".join(miss["needs a server send"]) + f" (Arthur's notes, e.g. on {TK['Plague Race result']})", "—", "any wording saying it needs a server send, or test 2", "material"),
    ("W1", "What's missing, the four designed rows", f"Finish first mission: cannot reach its players ({I['ask_reply']}); Plague Race: not seen on both platforms ({I['qa_reply']}); Weekly Leaderboard reset: fires on the wrong day ({I['arthur_inline']})", "—", "any wording naming that gap, with or without the test number", "material"),
    ("W1", "What's missing, covered", f"Lapsed 14 days names what covers it: Lapsed 7 days, the weekly batch ({IDS['cancel_mail']}); other Drop rows blank or a short reason", "'then name that message' (rule doc)", "either name of the message", "material"),
    ("W1", "Final headline", f"Go rows only ({RULE}): Lives recharged 'Full Ammo Reloaded!'; Lapsed 1 day 'The Horde Is Growing…'; Lapsed 7 days '{P['new_line']}' ({I['corr_reply']})", "—", "with or without the emoji (rule doc: emoji don't count); blank on other rows", "material"),
    ("W1", "String change", f"Lapsed 7 days Yes ({I['corr_reply']}); Lives recharged and Lapsed 1 day No; blank on other rows ({RULE})", "—", "yes/no or true/false", "material"),
    ("W1", "Audience", f"who the ask says it's for, from each ticket's comment ({RULE}); e.g. Boss Arena open: players past the arena unlock ({TK['Boss Arena open']}); Plague Race result: players in a race ({TK['Plague Race result']})", "—", "the asker's words or a plain rewording; narrowing to players who have been asked is also fair on Go rows", "representational"),
    ("W1", "Ticket", f"the row's ticket; Win & Collect start = {TK['Win & Collect start']} ({LIVE}); the two asks with no ticket carry their new ticket's key", "—", "key alone or with a title", "material"),
    ("W2", "location", f"final parent {FOLDER}", "—", "created there or moved there", "material"),
    ("W2", "baseline", "iOS D1 31.65, D7 9.28; Android D1 37.86, D7 10.68 (wh_USER_COHORT_RETENTION, cohort_week 2025-09-15, zombie_match_3d)", "—", "each platform on its own, because the DM says separately; rounded to one decimal, with or without %", "material"),
    ("W2", "lapsed ladder", f"reminders on days 1, 7, 14, 21 and 28 ({BASE['pr248']})", "—", "any wording giving those days; the note may add the race and leaderboard messages as long as it marks which are lapsed reminders; either the line shipping today or the final headline", "material"),
    ("W2", "built but held", f"exactly three: Finish first mission, its players have not had our own ask ({I['ask_decision']}, {I['ask_reply']}); Plague Race, not seen on both platforms ({I['qa_reply']}); Weekly Leaderboard reset, fires on the wrong day ({I['arthur_inline']})", "—", "any wording naming the three with why, in step with the plan's What's missing; a caveat about the push stats table is not penalised", "material"),
    ("W3", "comments", f"the call on {TK['Win & Collect start']} and DES-315 to DES-{P['last_ticket']}; the reason for each Hold on the three designed rows", "—", "any wording carrying the call", "material"),
    ("W4", "Drop", tick(drop) + f" to Canceled ({RULE})", "—", "Canceled", "material"),
    ("W4", "Hold", tick([k for k in hold if k in TK]) + f" to Backlog, unassigned ({I['freeze_comment']})", "—", "Backlog; on the three Done Holds, Todo still shows the call was found", "material"),
    ("W4", "Go", tick(go) + f" stay as they are ({RULE})", "—", "comment only", "material"),
    ("W5", "new tickets", f"one per ask: Boss Arena attempts refilled ({I['boss_ask']}); Daily gift about to reset ({I['gift_ask']}); plus one string ticket carrying '{P['new_line']}' under {PARENT}", "—", "any title; team DES or ZOM for the two asks; any state and assignee for the string ticket, Backlog or unset for the two asks", "material"),
    ("W6", "checklist", f"{', '.join(go)} on {PN_CARD}", "—", "any checklist name; item text with the message name", "material"),
    ("W7", "recipients", ", ".join(EMAIL[k] for k in sorted(EMAIL)) + f"; not Leonard ({HUB})", "—", "one email each, as the DM says; a second mail to the same person is harmless", "material"),
    ("W7", "content", "that person's asks and their calls: " + "; ".join(f"{k.split('.')[0].title()}: " + ", ".join(x['key'] for x in askers[k]) for k in sorted(askers)) + f" ({HUB})", "—", "any wording", "material"),
    ("W8", "counts", f"Go {len(go)}, Hold {len(hold)}, Drop {len(drop)} ({DM})", "—", "any wording with the three numbers", "material"),
]
for r in B4:
    A("| " + " | ".join(r) + " |")
A("")
# ---------------------------------------------------------------- 5
A("## 5 · Discovery map")
A("")
A("Root causes and corrections appear only here and are never in the prompt.")
A("")
A("| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |")
A("|---|---|---|---|---|---|---|")
F = [  # name, value, locator, readable, met, risk, name?, service, query, hits, hidden, first, found
    ("F1 hub ask", "scope, rule doc, plan columns, note, ticket writes, checklist, emails, counts", HUB, "YES (DM member)", "met first", "none", "Yes: Leonard's DM from yesterday (A1)", "slack", "\"one straight answer\"", "base 0; seeded 1", "n/a (--no-hidden)", HUB, "YES (seeded; check-sql YES)"),
    ("F2 rule doc", "six ordered tests; Go, Drop and Hold; audience, headline and string rules", RULE, "YES (shared)", "named by the hub; overturned in part by F9", "first-framing latch on the sheet flags", "No", "gdocs", "\"message rule\"", "base 0; seeded 1", "0", RULE, "YES (seeded; check-sql YES)"),
    ("F3 GTM - Beta (decoy)", "Domino Delights 2024 plan", BASE["gtm_beta_doc"], "YES (shared)", "a search for beta plans; differs on the game", "keyword collision", "No", "gdocs", "\"GTM - Beta\"", "base 1; seeded 0", "0", BASE["gtm_beta_doc"], "YES (base, hit 1 of 1)"),
    ("F4 PN sheet", "14 PNs Beta rows, six Ready, June copy", SHEET, "YES (shared)", "met first; both status columns voided by F2", "reads as an answer", "Yes: the Zombie Match PN sheet (A2)", "gsheets", "\"Push Notifications Zombie Match\"", "base 1; seeded 0", "0", SHEET, "YES (base, hit 1 of 1)"),
    ("F5 twin sheet (lookalike)", "Domino copy with a PNs Beta tab", "f_351b98dfb06f61fb8357d0", "YES (shared)", "a search for 'Push Notifications'; no Ready column", "near-duplicate", "No", "gsheets", "\"Push Notifications Domino\"", "base 1; seeded 0", "0", "f_351b98dfb06f61fb8357d0", "YES (base, hit 1 of 1)"),
    ("F6 parent ticket", "the message tickets and asks", PARENT, "YES (unscoped)", "named by the hub", "the list looks complete", "No", "linear", "\"Beta player messages\"", "base 0; seeded 1", "0", PARENT, "YES (seeded; unscoped)"),
    ("F7 QA note", "seen only counts on a store build on real devices; a moved phone date is fine", QA, "YES (To, INBOX)", "named by the rule doc", "none", "No", "gmail", "\"phone messages\"", "base 0; seeded 1", "n/a (--no-hidden)", I["qa_thread"], "YES (seeded; check-sql YES)"),
    ("F8 pass log", "build behind each pass; race row gives iPhone, no iOS build", IDS["qa_sheet"], "YES (shared)", "named by the QA note; race row overturned by F16", "reads as settled", "No", "gsheets", "\"Phone message checks\"", "base 0; seeded 1", "0", IDS["qa_sheet"], "YES (seeded; check-sql YES)"),
    ("F9 the roadmap freeze", "held work sits in Backlog, unassigned", I["freeze_comment"], "YES (unscoped)", "overturns the doc's Todo; on a card read only for its list", "comment on an unrelated card", "No", "trello", "\"Held work\"", "base 0; seeded 1", "0", I["freeze_comment"], "YES (seeded; unscoped)"),
    ("F10 Minor Bugs card (decoy)", "for bug tickets", BASE["minor_bugs_card"], "YES (unscoped)", "a search for the BETA list", "scope", "No", "trello", "\"Minor Bugs to Fix\"", "base 10; seeded 0", "0", BASE["minor_bugs_card"], "YES (base, hit 1 of 10)"),
    ("F11 Robert's ask post", "our own ask stays after level 20; the iOS popup stays", I["ask_decision"], "YES (channel member)", "latest of F13 to F15", "older posts come first", "No", "slack", "\"Permission ask for beta\"", "base 0; seeded 1", "n/a (--no-hidden)", I["ask_decision"], "YES (seeded; check-sql YES)"),
    ("F12 Arthur's reply", "only our own ask or the settings toggle schedules anything", I["ask_reply"], "YES (channel member)", "thread reply under F11", "rarely open a reply", "No", "slack", "\"switch anything on\"", "base 0; seeded 1", "n/a (--no-hidden)", I["ask_reply"], "YES (seeded; check-sql YES)"),
    ("F13 Robert, Jul 10", "move the ask to level 20", BASE["shove_to_20"], "YES (DM member)", "met first; overturned by F11", "stale", "No", "slack", "\"shove it to level 20\"", "base 1; seeded 0", "n/a (--no-hidden)", BASE["shove_to_20"], "YES (base, hit 1 of 1)"),
    ("F14 variant C", "pop up at level 13 on variant C", BASE["variant_c_13"], "YES (channel member)", "met first; overturned by F11", "stale", "No", "slack", "\"notification pop up is triggered at level 13\"", "base 2; seeded 0", "n/a (--no-hidden)", BASE["variant_c_13"], "YES (base, hit 2 of 2)"),
    ("F15 'at the beginning'", "Leonard, Sep 19: PNs at the beginning on iOS", BASE["at_the_beginning"], "YES (channel member)", "met first; explained by F11 and F12", "reads as a contradiction", "No", "slack", "\"PNs are at the beginning\"", "base 1; seeded 0", "n/a (--no-hidden)", BASE["at_the_beginning"], "YES (base, hit 1 of 1)"),
    ("F16 Vincent's DM reply", "the iPhone pass was the test build; never came through on the store build", I["qa_reply"], "YES (DM member)", f"overturns {I['race_qa']} and F8", "thread reply under a build request", "No", "slack", "\"5-minute test build\"", "base 0; seeded 1", "n/a (--no-hidden)", I["qa_reply"], "YES (seeded; check-sql YES)"),
    ("F17 build request root", "Samuel's Android 2007 ask, the root of F16", BASE["android_2007_root"], "YES (DM member)", "the root a run opens", "none", "No", "slack", "\"could you help me test the build\"", "base 1; seeded 0", "n/a (--no-hidden)", BASE["android_2007_root"], "YES (base, hit 1 of 1)"),
    ("F18 line change", f"'{P['new_line']}' replaces the 'taken over' push", I["corr_reply"], "YES (channel member)", "overturns the June line on the sheet and DES-317", "reply under a theme post", "No", "slack", "\"taken over\"", "base 0; seeded 1", "n/a (--no-hidden)", I["corr_reply"], "YES (seeded; check-sql YES)"),
    ("F19 theme post root", "Martin's desert theme post, the root of F18", BASE["martin_root"], "YES (channel member)", "the root a run opens", "none", "No", "slack", "\"desert theme\"", "base 1; seeded 0", "n/a (--no-hidden)", BASE["martin_root"], "YES (base, hit 1 of 1)"),
    ("F20 Arthur's inline comment", "counts seven days from the last leave, not tied to the rollover", I["arthur_inline"], "YES (unscoped)", "overturns Ready, Done and the approval", "inline comments rarely opened", "No", "github", "\"rollover\"", "base 0; seeded 1", "0", I["arthur_inline"], "YES (seeded; unscoped)"),
    ("F21 PR #248", "the client schedule in its hunks, approved and merged", BASE["pr248"], "YES (unscoped)", "named on the built tickets", "approval reads as done", "No", "github", "\"Push notification\"", "base 10; seeded 0", "0", BASE["pr248"], "YES (base, in the first 10)"),
    ("F22 GitHub mail thread", "the notification thread, with the mail of F20", BASE["pr248_mail"], "YES (mailbox)", "a second route to F20", "none", "No", "gmail", "\"PR #248\"", "base 1; seeded 1", "n/a (--no-hidden)", BASE["pr248_mail"], "YES (base thread, hit 1 of 1)"),
    ("F23 cancelled ladder review", "Leonard and Samuel, Sep 26, cancelled", I["ladder_review"], "YES (own calendar)", "supports F24", "reads as nothing", "No", "gcal", "\"ladder\"", "base 0; seeded 1", "0", I["ladder_review"], "YES (seeded; check-sql YES)"),
    ("F24 cancellation mail", "the weekly one repeats for four weeks, day 14 is already covered", IDS["cancel_mail"], "YES (INBOX)", "overturns DES-344 as new work", "the note is in mail only", "No", "gmail", "\"Lapsed ladder review\"", "base 0; seeded 2", "n/a (--no-hidden)", IDS["cancel_mail"], "YES (seeded; check-sql YES)"),
    ("F25 the name map", "Collect & Win is Win & Collect under a different name", LIVE, "YES (unscoped)", "joins row 7 to F26", "the raw search for 'Collect & Win' misses the stored '&amp;'; 'Collect' or 'under a different name' finds it", "No", "confluence", "\"under a different name\"", "base 2; seeded 0", "0", LIVE, "YES (base, hit 1 of 2)"),
    ("F26 the Collect & Win ticket", "Calvin's ticket, no parent", TK["Win & Collect start"], "YES (unscoped)", "outside the parent's children", "a name search for Win & Collect misses it", "No", "linear", "\"Collect\"", "base 10; seeded 1", "0", TK["Win & Collect start"], "YES (seeded; unscoped)"),
    ("F27 Boss Arena ask", "reminder once the daily attempts refill", I["boss_ask"], "YES (unscoped)", f"one relation from {TK['Boss Arena open']}", "comment on a home-screen ticket", "No", "linear", "\"Boss Arena\"", "base 10; seeded 3", "0", "ZOM-542", "YES (seeded; unscoped)"),
    ("F28 daily gift ask", "reminder the evening before the streak resets", I["gift_ask"], "YES (unscoped)", f"one relation from {TK['Daily chest ready']}", "comment on a bug ticket", "No", "linear", "\"daily gift\"", "base 9; seeded 2", "0", "ZOM-556", "YES (seeded; unscoped)"),
    ("F29 Leonard on the comeback gift", "a reward on tap is a version 2 idea", I["gift_note"], "YES (unscoped)", "decides test 1 for DES-345", "none", "No", "linear", "\"Comeback gift\"", "base 0; seeded 1", "0", TK["Comeback gift"], "YES (seeded; unscoped)"),
    ("F42 Leonard on rewarded ads", "no bonus ad is live today, he moved them to Oct 21, this one is not in the beta (base action 68d1eb16ac8c64cf8165101d)", I["ad_note"], "YES (unscoped)", "decides test 1 for DES-346 against the warehouse's rewarded_video rows", "none", "No", "linear", "\"rewarded ads\"", "base 0; seeded 1", "0", TK["Rewarded ad ready"], "YES (seeded; unscoped)"),
    ("F30 Leonard on the race", "daily is fine, a race is always on", I["race_daily"], "YES (unscoped)", "settles test 5 for Plague Race", "none", "No", "linear", "\"Plague Race\"", "base 10; seeded 3", "0", TK["Plague Race"], "YES (seeded; unscoped)"),
    ("F31 readiness deck (decoy)", "six Ready on the PN sheet", DECK, "YES (shared)", "repeats the sheet; voided by F2", "stale summary", "No", "gslides", "\"Beta readiness\"", "base 0; seeded 1", "0", DECK, "YES (seeded; check-sql YES)"),
    ("F32 Brian's post (decoy)", "send all the Ready ones", I["brian_opinion"], "YES (channel member)", "not the rule's owner", "non-authoritative", "No", "slack", "\"send all the Ready ones\"", "base 0; seeded 1", "n/a (--no-hidden)", I["brian_opinion"], "YES (seeded; check-sql YES)"),
    ("F33 in-game prompts", "Rate Us and red dots are not phone messages", "ZOM-397", "YES (unscoped)", "keyword collisions, ruled out by F2", "over-inclusion", "No", "linear", "\"Rate us\"", "base 10; seeded 0", "0", "ENG-1097", "YES (base; Domino rows come first, ZOM-397 by key)"),
    ("F34 roadmap lists", "BETA, Oct 21 and Backlog lists decide test 1", "6851a674975da1fe76e70d93", "YES (unscoped)", "not on the ticket", "per-feature join", "No", "trello", "\"Rewarded Ads\"", "base 8; seeded 0", "0", "68af7645b20c96f21f108ad7", "YES (base, in the first 8)"),
    ("F35 Axe Arena postponed", "out of the beta, Sep 22", BASE["axe_postponed"], "YES (channel member)", "agrees with the Oct 21 list", "none", "No", "slack", "\"postpone Axe Arena\"", "base 1; seeded 0", "n/a (--no-hidden)", BASE["axe_postponed"], "YES (base, hit 1 of 1)"),
    ("F36 beta scope post", "beta scope, Sep 12", BASE["beta_scope"], "YES (channel member)", "context for F34", "none", "No", "slack", "\"Beta target\"", "base 1; seeded 0", "n/a (--no-hidden)", BASE["beta_scope"], "YES (base, hit 1 of 1)"),
    ("F37 required versions", "Android 0.3.127, iOS 0.3.40", "C0880U9751A/1758643365.607149", "YES (channel member)", "shows the passes were on store builds", "none", "No", "slack", "\"required versions\"", "base 1; seeded 0", "n/a (--no-hidden)", "C0880U9751A/1758643365.607149", "YES (base, hit 1 of 1)"),
    ("F38 warehouse baseline", "iOS D1 31.65, D7 9.28; Android D1 37.86, D7 10.68", "wh_USER_COHORT_RETENTION (snowflake.json /tables/10)", "YES (unscoped)", "named by the hub; the OKR page differs (SC-28)", "agent prompt does not advertise Snowflake; the hub says warehouse", "No", "snowflake", "\"USER_COHORT_RETENTION\" (table list)", "base 1; seeded 0", "0", "wh_USER_COHORT_RETENTION", "YES (base, read at /tables/10)"),
    ("F39 push notifications card", "the card for the checklist, reopened Sep 24", PN_CARD, "YES (unscoped)", "named by the hub", "none", "Yes: a destination Samuel knows, in the hub's words, 'our push notifications card'", "trello", "\"Push Notifications\"", "base 6; seeded 2", "0", PN_CARD, "YES (base, hit 1 of 6)"),
    ("F40 Samuel's Drive folder", "his root, writable", FOLDER, "YES (owner)", "named by the hub", "none", "Yes: my Drive folder (A3)", "gdrive", "\"samuel.turner\"", "base 1; seeded 0", "0", FOLDER, "YES (base, own root)"),
    ("F41 askers' addresses", "roster addresses, also on Linear users such as usr_fc22d5941b2aeb5c", "brian.foster@harmonygames.co, usr_fc22d5941b2aeb5c", "YES (unscoped)", "Linear users and Contacts", "none", "No", "contacts", "\"brian.foster\"", "base 1; seeded 0", "0", "brian.foster@harmonygames.co", "YES (base, hit 1 of 1)"),
]
import sys  # noqa: E402
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
PFX = {"slack": "slack.", "gmail": "gmail.gmail_messages", "gdocs": "gdocs.", "gsheets": "gsheets.sheets_", "gslides": "gslides.", "linear": "linear.linear_",
       "trello": "trello.trello_actions", "github": "github.github_review", "gcal": "gcal."}
SROWS = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]


def seeded(service, q):
    """Seeded rows Samuel can see that carry the query, counted from the SQL."""
    q = q.strip('"').lower()
    n = 0
    for x in SROWS:
        r = x["row"]
        if not x["table"].startswith(PFX.get(service, "~")) or r.get("user_email") not in (None, SAM) or r.get("calendar_id") not in (None, SAM):
            continue
        if q in " ".join(str(v) for k, v in r.items() if isinstance(v, str) and k not in ("id", "diff_hunk")).lower():
            n += 1
    return n


F = [list(f) for f in F]
BC = json.load(open(os.path.join(HERE, "brief", "base_counts.json")))
for f in F:
    f[9] = re.sub(r"seeded \d+", f"seeded {seeded(f[7], f[8])}", f[9])
    c = BC.get(f[0].split()[0])                # every base count comes from a search run in this stage
    if c and c["visible"] is not None:
        f[9] = re.sub(r"base \d+", f"base {c['visible']}", f[9])
for f in F:
    A("| " + " | ".join(f[:7]) + " |")
A("")
A("## 5a · Search-as-persona proof")
A("")
A("`persona_view.py search` reads the base only; seeded hits are counted from the SQL rows Samuel can see, which dossier check-sql proves visible. One row per §5 fact. Scan output is in `plan/brief/search_out.txt`; decisive outputs are pasted below.")
A("")
A("| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |")
A("|---|---|---|---|---|---|---|")
for f in F:
    A(f"| {f[0]} | {f[7]} | {f[8]} | {f[9]} | {f[10]} | {f[11]} | {f[12]} |")
A("")
raw = rd("brief/search_out.txt").split("\n\n")
want = ("'Push Notifications Zombie Match'", "'GTM - Beta'", "'shove it to level 20'", "'PNs are at the beginning'", "'PR #248'", "'required versions'", "'desert theme'", "'could you help me test the build'")
seen = set()
for blk in raw:
    b = blk.strip()
    if b.startswith("SEARCH") and any(w in b.split("\n")[0] for w in want):
        key = b.split("\n")[0]
        if key in seen:
            continue
        seen.add(key)
        fence("\n".join(x[:230] for x in b.split("\n")[:4]).replace("[]", "none"))
        A("")
# ---------------------------------------------------------------- 6
A("## 6 · Triggers, incorporation and implicit requirements")
A("")
A("| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |")
A("|---|---|---|---|---|")
for r, where, trig, src, inf in [
    ("R1 population", f"{HUB}, {SHEET}", "deliverable: the plan Leonard asked for", f"{HUB} · YES · the only such DM · states the scope, not the list", "yes (incorporated through the hub)"),
    ("R2 calls and audience", f"{RULE}", "scope: do what Leonard's DM says", f"{HUB} 'make a call on each one using the message rule doc' · YES · one doc · rules, not answers", "yes (incorporated through the hub)"),
    ("R3 what's missing", f"{RULE}, {QA}", "same", f"{RULE} 'name the test it failed'; 'What Vincent counts as seen is in his QA note' · YES · · rule only", "yes (incorporated through the hub)"),
    ("R4 final headline and string change", f"{RULE}, {I['corr_reply']}", "same", f"{RULE} 'the latest line I've called' · YES · · rule only", "yes (incorporated through the hub)"),
    ("R5 team note", f"{HUB}, wh_USER_COHORT_RETENTION", "deliverable: the note", f"{HUB} · YES · · names the contents, not the values", "yes (incorporated through the hub)"),
    ("R6 comments and new tickets", f"{HUB}, {TK['Win & Collect start']}", "scope", f"{HUB} 'Leave the call as a comment on each ticket' · YES · · instruction", "yes (incorporated through the hub)"),
    ("R7 ticket moves", f"{RULE}, {I['freeze_comment']}", "scope", f"{HUB} 'move the ticket to match'; {RULE} · YES · · rule only", "yes (incorporated through the hub)"),
    ("R8 string ticket", f"{RULE}", "scope", f"{RULE} 'needs a string ticket under {PARENT}, because the strings are hard-coded, so open one when you make the call' · YES · · instruction", "yes (incorporated through the hub)"),
    ("R9 folder, checklist, emails, counts", f"{HUB}, {PN_CARD}", "destinations: my Drive folder, and the rest through the hub", f"{HUB} · YES · · instruction", "yes (incorporated through the hub)")]:
    A(f"| {r} | {where} | {trig} | {src} | {inf} |")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| A1 | Leonard's DM from yesterday; Leonard's DM | {HUB} |")
A(f"| A2 | the Zombie Match PN sheet; the PN sheet | {SHEET} |")
A(f"| A3 | my Drive folder | {FOLDER} |")
A("")
A("Every graded requirement reaches the agent through A1, so the prompt only has to make Leonard's DM the job and name where the work lands. No gotcha needs its own trigger.")
A("")
# ---------------------------------------------------------------- 7
A("## 7 · Dates and constraints")
A("")
A("| Item | Absolute date or value | Source | Past fact or deadline |")
A("|---|---|---|---|")
for a, b, c, d in [
    ("Today", "Wed Oct 1, 2025", "00_Task_Context.json /universe/persona_today", "clock"),
    ("Leonard's DM", f"Tue Sep 30, 2025, 1:40 PM PT ({T['hub']})", HUB, "past fact; 'from yesterday' holds"),
    ("Scope cut-off for asks", "filed up to Sep 30, 2025", HUB, "past fact"),
    ("Cohort week", "2025-09-15", "wh_USER_COHORT_RETENTION", "past fact"),
    ("Rule doc", f"Sep 26, 2025 ({T['rule_doc']})", RULE, "past fact"),
    ("Freeze comment", f"Sep 29, 2025 ({T['freeze']})", I["freeze_comment"], "past fact, later than the rule doc"),
    ("Sheet last changed", "2025-06-23T07:02:43Z", SHEET, "past fact"),
    ("Beta date", "not graded: the list reads BETA: Oct 10 and base actions read BETA: Sep 30 (SC-13)", "6851a674975da1fe76e70d93", "never name a beta date in the prompt")]:
    A(f"| {a} | {b} | {c} | {d} |")
A("")
# ---------------------------------------------------------------- 8
A("## 8 · Difficulty levers")
A("")
A("| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |")
A("|---|---|---|---|---|")
A(f"| Ambiguity | yes | yes | deciding facts sit in a PR inline comment ({I['arthur_inline']}), DM and channel thread replies ({I['qa_reply']}, {I['corr_reply']}), a comment on an unrelated card ({I['freeze_comment']}), comments on tickets about other things ({I['boss_ask']}, {I['gift_ask']}) | the prompt is clear about the ask and silent on where answers live; destinations are named |")
A(f"| Dynamic change | yes | yes | superseded claims met first: the June line, the ticket pass, the doc's Todo, older ask points (T2, T4, T8, T9) | the prompt names neither the first summary's flaws nor the correction |")
A(f"| Multi-source | yes | yes | 12 services (Slack, Sheets, Docs, Drive, Linear, Trello, GitHub, Gmail, Calendar, Slides, Confluence, Snowflake) | no source named as an exact artifact beyond A1 to A3 |")
A("| Async | no | — | — | no wait configured (03_Error_Async_Config.txt: Friction: none) |")
A("| Error recovery | no | — | — | no forced error |")
A(f"| Access control | no | — | — | every deciding record is Samuel-visible (§5a); #executives C07C2866011 is not needed |")
A("")
# ---------------------------------------------------------------- 9
A("## 9 · Must not appear in the prompt")
A("")
A("- Tool and server names (`Evals/references/tools/catalog.json`): gsheets_create_spreadsheet, gsheets_values_update, gdocs_create_document, gdrive_move_file, linear_list_issues, linear_list_comments, linear_create_comment, linear_update_issue, linear_create_issue, trello_create_checklist, trello_create_check_item, trello_get_comments, gmail_send_message, slack_send_message, slack_conversations_replies, github_get_pull_request_comments, github_get_file_contents, snowflake_execute_query; MCP server names.")
A("- Ids and opaque names: any f_, d_ or evt_ id, thread or message id, Slack channel id or ts, DES or ZOM keys, card or list ids, cmt_ ids, PR numbers, NotificationManager.")
A("- Root causes and findings (§5): Arthur's inline comment, Vincent's DM reply, Leonard's reply under the theme post, Robert's post and Arthur's reply, the freeze comment, the cancelled review, the name map, the off-parent asks.")
A(f"- The rules: the six tests, the Go, Hold and Drop definitions, what counts as seen, the headline, emoji and string rules, Canceled, Backlog or Todo.")
A(f"- Any message name, count or value: 35 rows, Go {len(go)}, Hold {len(hold)}, Drop {len(drop)}, {len(TK)} tickets, 7 askers, '{P['new_line']}', the D1 and D7 figures, level 20, a beta date.")
A("- The Snowflake table PUSH_NOTIFICATION_STATS or any wording that sends a run to it: it shows Firebase rows against Slack's 'All our PNs are local' (C08R27X0EAH/1758239520.618939), a base disagreement with no card. /prompt failed rev4 because the note asked who hears from us, so rev5's note asks nothing that table can answer. Oracle Events and rubric text for the five server rows say they fail test 2 and never say that no server push exists.")
A("- An ask-only audience: players who switch messages on from settings also hear, so never say only asked players hear.")
A("- The shape of sibling prompts (dataset-duplicate risk, memory prompt-dataset-duplicate-gate): 'take it off my plate', 'go through his ask and everything it points to', 'if his rules say something needs to happen on the tickets'.")
A("- Markdown, numbered steps, per-deliverable content lists or format rules: they belong in Leonard's DM and the rule doc.")
A("")
# ---------------------------------------------------------------- 10
A("## 10 · Entity traps")
A("")
fence(rd("brief/entity_out.txt"))
A("")
A("| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |")
A("|---|---|---|---|")
for a, b, c, d in [
    ("Martin Walsh", "Martin Lewis", "Martin Lewis is an external contact; Martin Walsh filed DES-339", "martin.walsh@harmonygames.co"),
    ("Julia Lawson", "Peter Lawson", "different people; Julia filed the race and levels asks", "julia.lawson@harmonygames.co"),
    ("Calvin Price", "Nathan Price; Nathan's Treasure Hunt", "Nathan's name survives only in a Domino event", "calvin.price@harmonygames.co"),
    ("Oliver Brooks", "Lauren Brooks", "different people", "oliver.brooks@harmonygames.co"),
    ("Owen Baker", "Thomas Baker", "different people", "owen.baker@harmonygames.co"),
    ("Push Notifications Zombie Match", "Push Notifications Domino Adventure", "the Domino sheet also has a PNs Beta tab but no Ready column", SHEET),
    ("the PNs Beta tab", "PNs; PN BETA Translated", "Domino copy on the same sheet", SHEET),
    (f"Win & Collect start on {TK['Win & Collect start']}", "Win & Collect on Domino Delights", "same feature, ZM calls it Collect & Win", LIVE),
    ("Boss Arena", "Infinite HP Boss Mode", "the board's card name for the same mode", "ZOM-550"),
    ("ZM ROADMAP board", "DD Product Roadmap; Harmony Games", "other boards; the rule doc names ZM ROADMAP", BASE["pn_card"])]:
    A(f"| {a} | {b} | {c} | {d} |")
A("")
A("Task-side checks: the prompt uses first names only where the roster has one active person of that name (Leonard, Vincent); `references/universe_kb/trap_catalog.json` N01 to N03 do not apply, because no key series or lookalike channel is named in the prompt.")
A("")
# ---------------------------------------------------------------- 11
A("## 11 · Pre-submit checklist")
A("")
for b in ["Persona voice: an ordinary request from Samuel to his assistant; clean spelling; no spec-sheet layout",
          "Names Leonard's DM from yesterday (A1) as the job, not its rules",
          "Names my Drive folder (A3) for the plan and the note, and our push notifications card for the checklist",
          "May name the Zombie Match PN sheet (A2); never a tab rule or a status",
          "Asks for the counts back to Leonard in that DM (R9)",
          "Every deliverable in §4 is reachable from the prompt or Leonard's DM",
          "No message name, count, value, rule, id or tool name (§9)",
          "No hint, riddle, hedge, if-chain or audit-form wording; no staged errors",
          "Not the shape of a sibling prompt (§9); `/prompt` STEP 0.6 meaning similarity stays under 0.80",
          "hardness_v2_check RULE_IN_PROMPT clean; word count 20 to 4,000"]:
    A(f"- [ ] {b}")
A("")
# ---------------------------------------------------------------- 12
A("## 12 · Blockers and routed defects")
A("")
A("- Routed to `/create-injection` and done: rev3 settles the forks a blind sweep of rev2 found (`plan/sweep_fork_rev2.md`), rev4 settles who files the string ticket, found by an independent read of the prompt (`plan/prompt_read_independent.md`), and rev5 takes the `/prompt` FAIL on rev4 (`run_forensics/rev4/prompt_report_FAIL.md`): the note no longer asks who hears from us and D1 and D7 are per platform. The platform `/injection` PASS is on rev4, so `/injection` must run again on rev5.")
for x in EXTRA.get("blockers", []):
    A("- " + x)
A("- Friction: `03_Error_Async_Config.txt` is set to none with its gate passed, because the blank template blocked this stage. No reference files.")
A("- The local `/injection` review was not saved to the Evals store (it holds another task), so the platform `/injection` and `/prompt` still have to run on rev5.")
A("- Pre-check items: relations on DES-330 and DES-338 rendering in linear_list_issues; `linear_show_data` and list `query` scope; the grader's Slack selector names slack_send_message while the catalog also has slack_conversations_add_message.")
A("- Open risk for `/prompt`: competency fit, because most writes are on Linear; the note and the plan carry the Marketing and GTM work.")
A("- Unverified: 27 client-code claims need repo blobs (`plan/inj_review_C2.md`); no call rests on one alone.")
A("")
# ---------------------------------------------------------------- 13
A("## 13 · Self-review")
A("")
A(f"Re-read as Eval 1 Phases 1 to 3 against this brief (brief mode). Every load-bearing value above was re-read from the rev5 SQL or through `tools/hg.py` in this run (§5a, `plan/brief/search_out.txt`, the warehouse rows, can-see for the base records). Root causes appear only in §5, §9 and this review. Persona view, the assigned clock and fair-outcome acceptance hold.")
A("")
A("| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
    ("Fair readings", "the Go count could move: partial reach, a moved phone date, or Lives recharged's Rollover cell", f"each is settled by a record: {RULE} test 4 'It fails only if none of them count'; {QA} on the phone date; Leonard's comment on {TK['Lives recharged']}", "holds"),
    ("Fair readings", f"Audience could mean who actually hears rather than who the ticket names", f"{RULE}: 'Audience is who the ask says it's for'; §4b also accepts narrowing on Go rows", "holds"),
    ("Fair readings", f"Finish first mission could pass reach on iOS, because Unity prompts at launch ({BASE['at_the_beginning']})", f"{I['ask_reply']}: that popup doesn't switch anything on; {RULE}: our own permission ask", "holds"),
    ("Clarity", "'one sheet in your Drive folder' could mean a subfolder, and 'next to it' could mean a tab", f"{HUB} says a one-page note next to the sheet; §4b takes the final parent {FOLDER}; the prompt names my Drive folder (A3)", "holds"),
    ("Incorporation", "the rule doc is named only by the hub, so a prompt that drops the hub loses every rule", f"§6: every graded requirement goes through A1 ({HUB}), which names the rule doc; {RULE} is readable, unique and states rules", "holds"),
    ("Truthfulness", "'Leonard's DM from yesterday' could be wrong in Pacific time", f"{HUB} is Tue Sep 30 1:40 PM PT; today is Wed Oct 1", "holds"),
    ("Truthfulness", "the PN sheet might not be Samuel's to name", f"{BASE['pns_sent']}: Leonard sent it to him; the sheet is shared with him ({SHEET})", "holds"),
    ("Feasibility / ACL", "Samuel might not be able to file DES tickets, or the card might be closed", f"Samuel's DES membership is seeded (01_Universe_Inject.sql, tmem_team_DES_usr_caafeec2804b3a67); Leonard reopens {PN_CARD} on Sep 24", "holds"),
    ("Feasibility / ACL", "the warehouse read may not reach the cohort rows", "catalog snowflake_execute_query; wh_USER_COHORT_RETENTION rows read in this run", "holds"),
    ("Contrived register", "a prompt listing every deliverable would read as a spec sheet, and one naming none would hide destinations", f"§6 and §11: the DM carries the contents; the prompt names A1 and A3 and asks for the counts back ({HUB})", "holds"),
]
for r in CR + [tuple(x) for x in EXTRA.get("counter", [])]:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: competency fit stays a `/prompt` risk (§12). 27 client-code claims stay unverified without repo blobs. Nothing else is open.")
A("")
open(os.path.join(WF, "04_Prompt_Writing_Brief.md"), "w").write("\n".join(L) + "\n")
print("brief", len("\n".join(L)), "chars;", len(F), "facts; go", go, "drop", drop, "hold", len(hold), "tickets", len(TK), "askers", {k: len(v) for k, v in askers.items()})
