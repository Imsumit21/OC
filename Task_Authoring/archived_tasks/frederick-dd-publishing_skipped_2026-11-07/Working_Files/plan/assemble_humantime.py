#!/usr/bin/env python3
"""Assemble Working_Files/05_Human_Time_Worksheet.md (first pass) from plan/humantime_volumes.json, the manifest and truth. Facts and arithmetic only."""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(TI, "..", "tools")); sys.path.insert(0, os.path.join(WF, "solver"))
import brief_facts as BF  # noqa: E402
import solver as SV  # noqa: E402
B, I, BASE, SL, MSG, TH = BF.B, BF.I, BF.BASE, BF.SL, BF.MSG, BF.TH
term = B.term
V = json.load(open(os.path.join(HERE, "humantime_volumes.json")))
TR = json.load(open(os.path.join(WF, "solver", "truth.json"))); TOT = SV.aggregates(TR)["totals"]
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SHA = hashlib.sha256(PROMPT.encode()).hexdigest()[:12]
sd = V["seeded"]
thr = V["gmail_threads_window"] + sd["threads_fred"]
sl = {k: sum(V[k].values()) for k in ("executives", "bridge-pitch", "analytics", "dm_leonard")}
msgs = sum(sl.values()) + sd["slack"]
tri = round(thr / 450 * 60); skim = round(msgs / 3000 * 60)
R = [
 ("Read Leonard's email and what it points to: the ground rules doc, the DD publishing card, the August sync position, the May one-pager", "read", f"5 records ({I['hub_thread']}, {I['rule_doc']}, {I['dd_card']}, {BASE['sync_doc']}, {I['onepager_deck']})", "anchor 'read one decisive thread' ≈ 20 min for the rule doc; 5–10 min each for the rest", 45),
 ("Triage Frederick's inbox for publishers that came to us (scope starts Apr 1, 2025)", "read", f"{thr:,} threads started Apr 1 – Sep 30, 2025 PT in {'frederick.stone@harmonygames.co'} ({V['gmail_threads_window']:,} base + {sd['threads_fred']} seeded)", "≈ 450 items/h (triage by sender and subject)", tri),
 ("Skim the channels Frederick is in, for any publisher that reached one of the four, however it came", "read", f"{msgs:,} messages Apr–Sep 2025: #executives C07C2866011 {sl['executives']:,}, #bridge-pitch C096HFA5Z8W {sl['bridge-pitch']:,}, #analytics C069FF9Q57S {sl['analytics']:,}, DM D05S58U4SAK {sl['dm_leonard']:,}, seeded {sd['slack']}", "≈ 3,000 messages/h (skim anchor)", skim),
 ("Per publisher: read its thread and its terms, then set its status", "read", f"{TOT['publishers']} publishers; 24 outreach sheet rows, 8 term sheets, 22 seeded threads, 2 base threads, 2 offers off the sheet", "10 min each (low end of the 8–15 min anchor for one record across 2–3 surfaces)", 260),
 ("Check each person who gave terms or said no against Contacts", "read", "16 lookups in 172 contacts (170 base + 2 seeded)", "1 min each (one name lookup)", 16),
 ("Read the BD Follow Up list and match its cards to publishers", "read", "7 cards on list 670015c2ecd45b634d5eec81 (4 base + 3 seeded)", "1 min each", 7),
 ("Add up DD's revenue for Jul, Aug and Sep from the warehouse table", "read", "184 rows in ANALYTICS.MONETIZATION.REVENUE_DAILY (92 days × 2 platforms)", "15 s per row, below the 2 h day-level anchor because it's one table and one column", 46),
 ("Compute each Live offer's gross, share, 12-month value, payment dates and Q4 cash", "read", f"{sum(1 for v in TR.values() if v['Status'] == 'Live')} Live offers", "6 min each (five small sums and a date count)", 42),
 (f"T1 the $10K looks banked (Marek's mail, card comment) until Arthur's reply under the banker post ({SL['arthur_cash']})", "dead end", "1 mail, 1 comment, 1 thread reply", "anchor 'read one decisive thread past its apparent conclusion'", 20),
 (f"T2 Tallwater's $60,000 until the note past the agenda on {I['pb_event']}", "dead end", "1 term sheet, 1 event", "15 min", 15),
 (f"T3 Moonrail looks Live until Robert's Kestrel post ({SL['kestrel_post']}) is joined through the signature and Contacts", "dead end", "1 post, 1 signature, 1 contact", "15 min (alias join)", 15),
 (f"T4 Copperleaf's offer, off the sheet, in a reply under an unrelated post ({SL['copperleaf_relay']})", "dead end", "1 thread of 9 replies", "10 min", 10),
 (f"T5 Redwood's offer behind Arthur's #analytics pointer, on ENG-2362 ({I['eng2362_comment']})", "dead end", "1 post, 1 ticket, 1 comment", "15 min", 15),
 (f"T6 Northglow looks like the best deal until its all-platform grant meets the August position ({BASE['rights_post']})", "dead end", "1 term sheet, 1 post, 1 doc", "15 min", 15),
 (f"T7 Sunfold's 50,000 installs until the comment on the card named for Lena ({I['sunfold_comment']})", "dead end", "1 term sheet, 1 card, 1 comment", "15 min (card named for a person)", 15),
 (f"T8 no note looks owed until Leonard's line under the Matthew post ({SL['standing_line']}) is matched to the sheet's What we sent column", "dead end", "1 thread reply, 24 sheet rows, 1 deck", "15 min", 15),
 (f"T9 signing looks like Oct 31 until the ESG thread ({I['esg_thread']}) moves it to Nov 14", "dead end", "2 mails", "10 min", 10),
 ("T10 two publishers already have cards, named for people", "dead end", f"2 cards ({I['oakline_card']}, {I['sunfold_card']})", "5 min", 5),
 (f"T11 Summit's auto-reply reads as an answer ({TH['Summit Mobile']})", "dead end", "1 message", "5 min", 5),
 (f"T12 Frederick's Sep 4 Rayking message reads as sent until its Drafts label and his DM ({SL['rayking_dm']})", "dead end", "1 thread, 1 DM", "10 min", 10),
 (f"T13 the paid-traffic numbers ({BASE['board_followup']}) tempt instead of the organic figure", "dead end", "1 mail", "5 min", 5),
 (f"T14 Pinegrove's grant is mobile only but takes the code ({term('Pinegrove Games')})", "dead end", "1 term sheet", "10 min", 10),
 ("T15 Homa and NCsoft look like publishers in talks", "dead end", f"2 posts ({BASE['homa_codev']}, {BASE['ncsoft_question']})", "5 min each", 10),
 (f"T16 Tilting Point's form looks like an approach ({BASE['tilting_ack']})", "dead end", "1 mail", "5 min", 5),
 (f"T17 Apple Arcade reads as a dominoes lead ({BASE['apple_arcade']})", "dead end", "1 post", "5 min", 5),
 (f"T18 the Publishing Partners doc reads as the population ({BASE['partners_doc']})", "dead end", "1 doc", "10 min (compare it with the sheet)", 10),
 (f"T19 the Biz Dev Notes list reads as the population ({BASE['bizdev_doc']})", "dead end", "1 doc", "5 min", 5),
 (f"T20 the Sep 24 lead reads as a publisher to add ({BASE['lead']})", "dead end", "1 DM line", "5 min", 5),
 (f"T21 the co-dev doc reads as rules for an offer ({I['codev_doc']})", "dead end", "1 doc", "5 min", 5),
 ("Redo the numbers and the ranking after late corrections", "re-read", "4 reruns (Tallwater, Sunfold, Oakline, the first pick)", "5 min each", 20),
 (f"Create the model sheet in the DD publishing folder and enter one row per publisher, plus the Summary tab", "write", f"1 sheet, {TOT['publishers']} rows × 6 columns, 3 summary lines", "5 min setup + 3 min per row + 5 min summary", 88),
 ("Checklists and items on the DD publishing card", "write", f"{TOT['checklists']} checklists, {TOT['checklist_items']} items", "2 min per checklist, 1 min per item", 38),
 ("New follow-up cards on BD Follow Up", "write", f"{TOT['cards_new']} cards", "2 min each (a name only, no tailoring)", 30),
 ("Status comments on the two existing cards", "write", f"{TOT['card_comments']} comments", "2 min each", 4),
 ("Contacts for people who gave terms or said no", "write", f"{TOT['contacts_added']} contacts", "2 min each (name, email, company)", 28),
 ("Reminders on Frederick's calendar, one per Live offer", "write", f"{TOT['reminders']} events", "2 min each (title and date only)", 14),
 ("One-line nudges left as Gmail drafts", "write", f"{TOT['nudges']} drafts", "4 min each (one line, below the tailored-write anchor)", 28),
 ("Organic-figure notes left as Gmail drafts", "write", f"{TOT['organic_notes']} drafts", "7 min each (tailored-write anchor 5–10 min)", 21),
 ("Reply to Leonard with the first pick, its value, its Q4 cash and what's banked", "write", "1 reply", "10 min", 10),
]
total = sum(r[4] for r in R)
assert total % 15 == 0, total
H = total / 60
traps = {t["id"] for t in MAN["traps"]}
assert traps <= {r[0].split()[0] for r in R if r[1] == "dead end"}, traps - {r[0].split()[0] for r in R}
g = lambda k: sum(r[4] for r in R if r[1] == k)
L = []; A = L.append
A("# Human Time Worksheet — frederick_dd_publishing")
A("")
A("Pass: first (re-measured for rev2)        Tier: Long-Horizon")
A("Universe: synth-cut · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
A(f"Hours: {H:g}")
A("")
A("Basis:")
A(f"- The work 04_Prompt.txt asks for (sha256 {SHA}): model what each publisher would bring in for DD, going by Leonard's email; the model in the DD publishing folder; the board work on the DD publishing card; a reply to Leonard.")
A("- Leonard's email adds Contacts; the ground rules doc adds reminders and, through its last line, the organic-figure notes; the card adds checklists, follow-up cards and nudges.")
A("- The work is done by hand in Frederick's own accounts: no search, scripts or AI.")
A("- The person doesn't start out knowing the 26 publishers or where each correction sits; finding them is the inbox and Slack sweep below.")
A("")
A("| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |")
A("|---|---|---|---|---|")
for r in R:
    A("| " + " | ".join(str(x) for x in r) + " |")
A(f"| Total | | | | {total} = {H:g} h |")
A("")
A(f"Tier check: in band (Long-Horizon ≈ 12–24 h; {H:g} h). No trigger.")
A(f"- Re-measured in this run: inbox {thr:,} threads, Slack {msgs:,} messages, 184 revenue rows, 26 publishers, 86 write objects.")
A("- The planned call budget is 203 (01_Hardness_Manifest.json call_budget). Hand-time is driven by the sweeps and 26 manual reads, which an agent batches with search.")
A("")
A("Baseline count basis (post-baseline only): n/a (first pass)")
A("")
C = [
 f"Rules: Leonard's email, ground rules doc, card, sync, one-pager (5 records) 45 min",
 f"Inbox triage: {thr:,} threads Apr–Sep at 450/h {tri} min",
 f"Slack skim: {msgs:,} messages at 3,000/h {skim} min",
 f"26 publishers: thread + terms + status, 10 min each 260 min",
 f"Contacts checks 16 min; board list 7 min; revenue 184 rows 46 min; 7 offers computed 42 min",
 f"21 traps (returned wire, Tallwater call, Kestrel, Copperleaf, Redwood, rights, Sunfold comment, organic note, signing date, decoys) {g('dead end')} min; redo numbers {g('re-read')} min",
 "Model sheet 26 rows 88 min; 6 checklists + 26 items 38 min; 15 cards + 2 comments 34 min",
 "14 contacts 28 min; 7 reminders 14 min; 7 nudges 28 min; 3 notes 21 min; reply 10 min",
 f"Total {total:,} min = {H:g} h",
]
A("Condensed breakdown (one line per sub-task, facts only; the human types the reasoning in their own words):")
for c in C:
    A(f"- {c}")
A("")
n = len("\n".join(C))
A(f"Condensed breakdown length: {n} characters (field accepts 50–2,000)")
A("")
A("Sources measured:")
A("- hg.py search files gmail 'threads/frederick@harmonygames.co_' (4,656 files; dates decoded from thread ids, 1,779 started Apr 1 – Sep 30 PT).")
A("- hg.py search search slack '.' --file messages/C07C2866011/2025-09.json --key ts, repeated for each month Apr–Sep 2025 and for C096HFA5Z8W, C069FF9Q57S and D05S58U4SAK (plan/measure_volumes.py, plan/humantime_volumes.json).")
A("- hg.py search search snowflake domino_delights --pointer /tables/12/rows, then hg.py search get for the row dates (184 rows, 2025-07-01 to 2025-09-30).")
A("- hg.py records contacts (170 base contacts, plan/id_checks_sql.out.json); hg.py search get trello /lists/25 (BD Follow Up).")
A(f"- 01_Universe_Inject.sql rows (rev2): {sd['threads_fred']} Frederick threads, {sd['messages_fred']} messages, {sd['docs']} docs, {sd['slack']} Slack messages, {sd['contacts']} contacts. solver/truth.json for the write counts.")
A("")
A("## Self-review")
A("")
A("Checked in order against 10_Long Horizon Guidelines - V2.md §5 and §10, the Pre-QC 'Difficulty and submission' list and the Screen 25 field rules (0.25 step, 50–2,000 characters, pasting and copying blocked).")
A("")
A("| Area | Counter-reading | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
S = [
 ("Inflated", f"{H:g} h is near the top of the band, and 10 min per publisher plus separate dead-end lines could double-count reads", f"The dead-end lines cost only the extra misleading record and the join (T1–T21, 01_Hardness_Manifest.json traps). The publisher rate is the low end of the 8–15 min anchor; the sweeps use the anchor rates ({tri} and {skim} min). Every line has a measured volume", "holds"),
 ("Solution-path estimate", "It could be written as if the person already knew the publishers and where each correction sits", f"The inbox triage ({thr:,} threads) and Slack skim ({msgs:,} messages) come first. All 21 manifest traps have a dead-end line, checked by an assert in plan/assemble_humantime.py, including {SL['arthur_cash']}, {I['pb_event']} and ENG-2362", "holds"),
 ("Evaluator-wide volume", "Search is evaluator-wide, so the counts could include other people's mail or channels", "Gmail is counted only in the frederick@harmonygames.co_ thread files; Slack covers only four containers Frederick is in (persona_view can-see in brief §5a, check-sql); Contacts, Trello and Snowflake are unscoped", "holds"),
 ("Tier mismatch", "The task could be thin, or over the 24 h ceiling", f"{H:g} h is inside 12–24 h. The minutes were summed from the rates; one line, the board list, uses a 1-min-per-card rate that also puts the sum on the 0.25 step. The planned budget is 203 calls (01_Hardness_Manifest.json call_budget; volumes in plan/humantime_volumes.json, Slack C07C2866011)", "holds"),
 ("Linter reading", "The linter sees only the prompt, the hours, the reasoning and the SQL. An 81-word prompt could make 22 h look 3× too high", f"The reasoning names what the SQL shows: 26 publishers, 8 term sheets, the sweep sizes and 86 writes. 01_Universe_Inject.sql carries 144 inserts across 10 schemas; hand-time rests on those reads and writes, not the prompt's length (for example {term('Tallwater Games')}, {I['dd_card']})", "holds"),
]
for r in S:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: none. Refresh after 08_Oracle_Events.md and after the baseline.")
A("")
open(os.path.join(WF, "05_Human_Time_Worksheet.md"), "w").write("\n".join(L) + "\n")
print("hours", H, "total", total, "read", g("read"), "dead end", g("dead end"), "re-read", g("re-read"), "write", g("write"), "chars", n)
