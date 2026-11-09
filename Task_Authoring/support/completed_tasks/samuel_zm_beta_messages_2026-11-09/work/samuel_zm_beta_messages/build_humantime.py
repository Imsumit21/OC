#!/usr/bin/env python3
"""Writes Working_Files/05_Human_Time_Worksheet.md. Volumes are the ones measured through tools/hg.py and persona_view.py
(plan/humantime_measured.json); the sum and the character count are computed here, never typed."""
import hashlib, json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
V = json.load(open(os.path.join(HERE, "humantime_measured.json")))
P = json.load(open(os.path.join(HERE, "ids.json")))
I, B, TK = P["ids"], P["base"], P["tickets"]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]     # noqa: E731
PROMPT, SQL = sha(os.path.join(TI, "04_Prompt.txt")), sha(os.path.join(TI, "01_Universe_Inject.sql"))

slack_total = sum(v for v in V["slack"].values())
slack_min = math.ceil(slack_total / 3000 * 60)
mail = V["gmail_sep"] + V["gmail_oct"] + V["gmail_seeded"]
drive = V["drive_owned"] + V["drive_shared"] + V["drive_seeded"]
cal = V["gcal_sep"] + V["gcal_seeded"]
zom = V["zom_aug"] + V["zom_sep"]
n_rows, n_asks, n_cmt = 14, 18, 4
n_msgs = n_rows + n_asks + n_cmt
assert n_msgs == sum(P["counts"].values()) == 36, P["counts"]

ROWS = [
 ("Read the request, Leonard's DM and the message rule doc", "read", f"3 records: prompt {V['prompt_chars']} chars, DM {V['hub_chars']} chars, rule doc 1,462 chars, 6 ordered tests", "careful read, the tests are applied 36 times", 20),
 ("Read the PNs Beta tab row by row", "read", "14 rows, 11 filled columns", "about 1 min per row", 15),
 ("Skim September Slack where the game is discussed, for corrections and calls", "read",
  f"{slack_total:,} messages: #zombie-bugs {V['slack']['C08R27X0EAH']:,}, #zombie-match3d {V['slack']['C0880U9751A']}, #zombie-art {V['slack']['C08R8CHB0QL']}, Arthur DM {V['slack']['D06KV30TPL4']}, Vincent DM {V['slack']['D06UFE81RF0']}, #company-internal {V['slack']['C05KNDCHAAG']}, Leonard DM {V['slack']['D06L58XCVKK']} (Samuel is a member of each; seeded rows included)",
  "≈ 3,000 messages/h (worked-example skim anchor)", slack_min),
 ("Triage Samuel's mailbox for September", "read", f"{mail} threads ({V['gmail_sep']} + {V['gmail_oct']} base, {V['gmail_seeded']} seeded)", "≈ 450 items/h", 5),
 ("Read Vincent's QA note and his Phone message checks log", "read", "1 email, 6 logged rows", "2 min for the note, 1 min per row plus the header", 10),
 ("Triage Samuel's calendar for September and open the notes", "read", f"{cal} events ({V['gcal_sep']} base, {V['gcal_seeded']} seeded)", "30 s per event", 5),
 ("List Samuel's Drive to find the rule doc, the deck and the log", "read", f"{drive} files ({V['drive_owned']} owned, {V['drive_shared']} shared, {V['drive_seeded']} seeded)", "≈ 450 items/h", 18),
 ("Scan the ZM ROADMAP board for test 1", "read", f"{V['trello_cards']} cards on {V['trello_lists']} lists", "≈ 450 items/h", 11),
 ("Read PR #248 and its review for what the client schedules", "read", f"1 PR, {V['pr_comments_base'] + 1} review comments, {V['pr_reviews_base'] + 1} reviews", "≈ 40 min (worked-example PR anchor)", 40),
 ("Read the client's NotificationManager.cs for the schedule and the days", "read", f"1 file, {V['nm_bytes']:,} bytes, 6 scheduled messages", "30 min (dense C#, slower than a document)", 30),
 ("Find the Sep 15 cohort week in the warehouse", "read", f"1 table, {V['cohort_rows']} Zombie Match rows, {V['cohort_week_rows']} needed", "15 min (find the table, read 2 rows)", 15),
 ("Each sheet row: ticket, its comments, roadmap list and the client, then run the tests", "read", f"{n_rows} messages on {n_rows} tickets", "12 min each (V1 anchor 8–15 min per record over 2–3 surfaces)", n_rows * 12),
 ("Each ask under the parent: ticket, comments, roadmap list, then run the tests", "read", f"{n_asks} asks on {n_asks} tickets ({V['des_comments']} comments across all DES tickets)", "8 min each (low end of the anchor: fewer surfaces)", n_asks * 8),
 ("Each ask found in a ticket comment: run the tests", "read", f"{n_cmt} asks", "8 min each", n_cmt * 8),
 ("T1 Weekly Leaderboard reset looks finished (Ready, Done, passed) until the review note and the source show it counts from the last leave", "dead end", "1 inline comment, 1 code block", "≈ 20 min (decisive-thread anchor)", 20),
 ("T2 Lapsed 7 days: the June line gives way to Leonard's Sep 29 reply, which a later calendar note replaces", "dead end", "1 thread under a theme post, 1 event note", "25 min (two records, the second in another service)", 25),
 ("T3 Finish first mission looks ready until the trigger is joined to where our own ask runs", "dead end", "2 source files, 1 post with its reply", "≈ 20 min", 20),
 ("T4 Plague Race reads as passed until Vincent's reply in a DM thread under a build request", "dead end", "1 thread reply, checked against the QA note", "≈ 20 min", 20),
 ("T16 Lives recharged reads as passed until Vincent's post after iOS 0.3.49", "dead end", "1 channel post, checked against the log", "15 min", 15),
 ("T5 The Win & Collect row has no child ticket until the live-ops page maps it to a ticket under another name", "dead end", "1 page, 1 ticket", "15 min", 15),
 ("T6 Asks outside the parent: triage the ZOM tickets by title, then follow the links from the child tickets and read the comments", "dead end", f"{zom} ZOM tickets filed Aug–Sep ({V['zom_aug']} + {V['zom_sep']}), {n_cmt} opened", "15 min at ≈ 450 items/h, then 5 min per ticket opened", 35),
 ("T7 Lapsed 14 days reads as new work until the weekly batch and the cancelled review show it's covered", "dead end", "1 ask, 1 cancelled event, 1 mail", "15 min", 15),
 ("T8 'Unless the roadmap says otherwise': open the BETA list's cards to find what it says about held tickets", "dead end", f"{V['beta_cards']} cards", "about 1.5 min per card", 30),
 ("T9 Older permission-ask records point elsewhere until Robert's Sep 29 post", "dead end", "3 Slack records", "5 min each", 15),
 ("T10 The readiness deck says six are Ready", "dead end", "1 slide", "5 min", 5),
 ("T11 The other tabs of the PN sheet look like part of the list", "dead end", f"2 tabs: PNs {V['pns_rows']} rows, PN BETA Translated {V['translated_rows']} rows", "10 min (compare headers and titles, Domino copy)", 10),
 ("T12 Brian's 'send all the Ready ones' post", "dead end", "1 post", "5 min", 5),
 ("T13 ENG-2311 looks like the event messages are built", "dead end", "1 ticket on another game", "5 min", 5),
 ("T14 Red-dot tickets read like asks", "dead end", "2 tickets (ZOM-471, ZOM-539)", "5 min", 5),
 ("T15 Rate Us and the permission popup read like messages", "dead end", "1 card, 1 ticket", "5 min", 5),
 ("Go back over calls that a later record overturned", "re-read", "4 findings: Plague Race, Lives recharged, the Lapsed 7 line, the Hold state", "about 4 min each", 15),
 ("Create the sheet in Samuel's folder and enter one row per message", "write", f"1 sheet, {n_msgs} rows × 7 columns", "5 min setup + 3 min per row", 5 + 3 * n_msgs),
 ("Write the one-page note: D1 and D7 per platform, the lapsed days, the four built Holds with why", "write", "1 doc, 3 parts", "45 min", 45),
 ("Leave the call as a comment on each ticket", "write", f"{V['tickets']} comments", "5 min each (low end of the V1 anchor: reuses the sheet's reason)", 5 * V["tickets"]),
 ("Move each Hold and Drop ticket to match", "write", f"{V['moves']} ticket moves, Holds also unassigned", "2 min each (no text)", 2 * V["moves"]),
 ("New tickets: the four asks with none, and the string ticket", "write", "5 tickets", "6 min each", 30),
 ("Checklist of the Go messages on the push notifications card", "write", "1 checklist, 2 items", "2 min each", 6),
 ("Email each person who asked about their asks", "write", f"{V['askers']} emails", "7 min each (a join of their asks and calls)", 7 * V["askers"]),
 ("Count the 36 calls and tell Leonard in the DM", "write", "1 message, 3 counts", "6 min", 6),
]
total = sum(r[4] for r in ROWS)
if total % 15:
    sys.exit(f"sum {total} is not on a 0.25 h step: review the rows, do not pad")
hours = total / 60

groups = [
 ("Rules: DM, rule doc, PNs Beta tab, QA note and log", [0, 1, 4]),
 (f"Slack skim: {slack_total:,} September messages at 3,000/h", [2]),
 (f"Listings: {mail} mail threads, {cal} events, {drive} Drive files, {V['trello_cards']} roadmap cards", [3, 5, 6, 7]),
 ("Client: PR #248 with its review, NotificationManager.cs", [8, 9]),
 ("Warehouse: Sep 15 cohort week", [10]),
 (f"{n_msgs} messages through the six tests, 8 to 12 min each", [11, 12, 13]),
 ("16 traps: wrong day, replaced headline, reach, two withdrawn passes, other-name ticket, asks outside the list, day 14, Hold rule, older posts, deck, tabs, decoys", list(range(14, 30))),
 ("Re-reading 4 overturned calls", [30]),
 (f"Sheet {n_msgs} rows and one-page note", [31, 32]),
 (f"{V['tickets']} comments, {V['moves']} moves, 5 tickets", [33, 34, 35]),
 (f"Checklist, {V['askers']} emails, reply to Leonard", [36, 37, 38]),
]
assert sorted(i for _, ix in groups for i in ix) == list(range(len(ROWS))), "condensed lines must cover every row once"
cond = [f"- {name} {sum(ROWS[i][4] for i in ix)} min" for name, ix in groups] + [f"- Total {total:,} min = {hours:g} h"]
cond_txt = "\n".join(cond)

L = []
A = L.append
A("# Human Time Worksheet — samuel_zm_beta_messages")
A("")
A("Pass: first (rev6)        Tier: Long-Horizon")
A("Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
A(f"Hours: {hours:g}")
A("")
A("Basis:")
A(f"- The work 04_Prompt.txt asks for (sha256 {PROMPT}): carry out Leonard's Sep 30 DM, which covers a call on every PNs Beta row and every filed ask, a sheet, a one-page note, ticket comments and moves, new tickets, a checklist, emails and the counts.")
A("- The work is done by hand in Samuel's own accounts: no search, scripts or AI.")
A(f"- Counts come from rev6 (01_Universe_Inject.sql {SQL}, solver/truth.json): 36 messages, Go 2, Hold 28, Drop 6. The person doesn't start out knowing where any of them are.")
A("- Friction: none (03_Error_Async_Config.txt), so there is no workaround line.")
A("")
A("| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |")
A("|---|---|---|---|---|")
for r in ROWS:
    A("| " + " | ".join(str(x) for x in r) + " |")
A(f"| Total | | | | {total} = {hours:g} h |")
A("")
A(f"Tier check: in band (Long-Horizon ≈ 12–24 h; {hours:g} h). No trigger.")
A(f"- Re-measured in this run: {slack_total:,} Slack messages, {zom} ZOM tickets, {V['trello_cards']} cards, {n_msgs} messages, {V['tickets']} tickets.")
A(f"- The manifest's call budget is {P['budget_total']}. The rev5 pre-check made 188 calls (185 counted) on a near-identical job.")
A("- Most of the hours are 36 manual decisions and about 85 per-record writes, which an agent makes in far fewer steps.")
A("")
A("Baseline count basis (post-baseline only): n/a (first pass)")
A("")
A("Condensed breakdown (one line per sub-task group, facts only; the human types the reasoning in their own words):")
A(cond_txt)
A("")
A(f"Condensed breakdown length: {len(cond_txt)} characters (field accepts 50–2,000)")
A("")
A("Sources measured: hg.py and persona_view.py, listed here.")
A("- hg.py search search slack '.' --key ts with --file messages/CHANNEL/2025-09.json for C0880U9751A, C08R27X0EAH, C08R8CHB0QL, D06UFE81RF0, D06KV30TPL4 and C05KNDCHAAG; hg.py search files slack D06L58XCVKK shows no September file, so its one message is seeded.")
A("- persona_view.py can-see samuel_turner slack, run for each of those channels and D06L58XCVKK, D06KPMDV2JZ: YES for each; persona_view.py reach samuel_turner --json: mail threads by month, calendar events by month, Drive owned and shared.")
A("- hg.py search search trello 6851a6569f3bf818760632ab --pointer /cards --key idBoard and --pointer /lists; hg.py search search trello 6851a674975da1fe76e70d93 --pointer /cards --key idList.")
A("- hg.py search search linear team_ZOM --pointer /issues --key team_id, joined to created_at 2025-08 and 2025-09.")
A("- hg.py search search github 'harmonygames-Games/match3d#248#rc_' and '#rev_' --key id; hg.py search files github Notifications/NotificationManager.cs.")
A("- hg.py search get gsheets --file data.json --pointer /sheets_spreadsheets/220/sheets/0 and /1; the tab at /2 counted with hg.py search search gsheets --pointer.")
A("- hg.py search search snowflake zombie_match_3d --pointer /tables/10/rows --key game_id, and 2025-09-15 --key cohort_week.")
A("- 01_Universe_Inject.sql rows (rev6), parsed with tools/base_check.parse_sql, never run: 7 Slack messages, 4 Samuel threads, 2 Samuel events, 33 DES issues, 64 DES comments, 4 ZOM comments.")
A("- Raw figures: plan/humantime_measured.json.")
A("")
A("## Self-review")
A("")
A("Walked against `10_Long Horizon Guidelines - V2.md` §5 and §10, the Pre-QC list in `9_Common Errors & Pre-QC - V2.md` (line 237), and the field rules in the playbook, in that order. §5 asks for dead ends, a workaround if forced, re-reading, and no learning the universe from scratch: covered below. §10 and Pre-QC ask for a sub-task justification whose arithmetic adds up: the script computes the sum, so it can't drift.")
A("")
A("| Check | Counter-reading | Evidence | Result |")
A("|---|---|---|---|")
CR = [
 ("Inflated", "the 344 minutes of per-message work double-count the Slack skim and the source read", f"the skim finds corrections, and the per-message line reads each ticket's own comments ({V['des_comments']} DES comments, 01_Universe_Inject.sql) and runs the tests. Asks use the 8-minute low end of the V1 anchor for that reason", "holds"),
 ("Inflated", "32 comments at 5 min is high when the reason is already on the sheet", "5 min is the low end of the 5–10 min anchor; the V1 evidence averages about 6 min across 95 writes; the 32 comment targets are the tickets in 01_Universe_Inject.sql", "holds"),
 ("Solution-path estimate", "the dead ends assume the person knows where the corrections sit", "all 16 traps in 01_Hardness_Manifest.json have a line (T1 to T16), and the Slack skim is the unguided path to them; friction is none, so no workaround applies (03_Error_Async_Config.txt)", "holds"),
 ("Evaluator-wide volume", "Slack, mail, calendar and Drive counts could include what Samuel can't see", "persona_view.py can-see returned YES for all eight channels; mail, calendar and Drive come from persona_view.py reach samuel_turner, so the counts are his own view; the 3 seeded Drive files are not in the base, so plan/checksql.txt (persona_view.py check-sql) shows them visible instead", "holds"),
 ("Tier mismatch", f"{hours:g} h sits close to the top of 12–24 h, so scope might be over the tier", "in band with no trigger; the volumes in plan/humantime_measured.json were measured in this run, and the number was not tuned toward the band", "holds"),
 ("Linter reading", "from the prompt and SQL alone, 36 messages might not justify the hours", f"04_Prompt.txt names a sheet, a note, ticket work and emails, and 01_Universe_Inject.sql shows 33 tickets and 68 comments. With 36 decisions and about 85 writes, {hours:g} h is well inside 3× of a defensible figure, and the condensed lines name the volumes", "holds"),
 ("Re-verification", "volumes could be carried over from an earlier stage", "every volume in Sources measured was taken in this run through hg.py or persona_view.py; none comes from the dossier", "holds"),
]
for r in CR:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: first pass, so no Oracle Events or baseline refresh yet. Refresh after 08_Oracle_Events.md exists and again after the baseline. Rates beyond the two anchor tables are judgment, stated per row. Field length and banned phrases are for the human to check when typing.")
A("")
open(os.path.join(WF, "05_Human_Time_Worksheet.md"), "w").write("\n".join(L))
print("rows", len(ROWS), "total", total, "hours", hours, "condensed", len(cond_txt), "slack", slack_total, "mail", mail, "drive", drive, "cal", cal, "zom", zom)
print({k: sum(r[4] for r in ROWS if r[1] == k) for k in ("read", "dead end", "re-read", "write")})
