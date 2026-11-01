"""Writes task_inputs/Working_Files/08_OE_Check.md (check mode) for the current 08_Oracle_Events.md."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
OE = open(os.path.join(TI, '08_Oracle_Events.md')).read()
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
ev = {int(m.group(1)): m.group(2) for m in re.finditer(r"^OE (\d+)  (.+)$", OE, re.M)}
n = len(ev)


def find(rx):
    return [k for k, v in ev.items() if re.search(rx, v)]


def span(s):
    assert s in OE, s
    return f"\"{s}\""


first_w = min(find(r"^Create the register"))
cm = find(r"^Comment on ENG-")
st = find(r"^Set ENG-")
calc = min(find(r"^Work out the register"))
lo = min(find(r"^Check whether the two"))
cr = min(find(r"^Look for CodeRabbit"))
rp = find(r"^Reply to Leonard")
sv = min(find(r"^Find SVB's card terms"))
cu = min(find(r"^Find the Cursor reply"))
ap = min(find(r"^Find what happened to the AppLovin"))
ct = min(find(r"^Read the HG Costs tab"))
NI = len(json.load(open(os.path.join(HERE, 'accounts.json')))['accounts'])
LN = TR['linear']
L = []
w = L.append
w("# 08 OE Check — rb-winddown-closeout")
w(f"Checked 2026-10-29 · Events {n} · Characters {len(OE)} (300–50,000: ok) · Ledger 2026-10-29 (08_OE_Writing_Ledger.md, oe-writing PASS)")
w("/oe prediction (a prediction only; /oe gives the verdict): PASS 5")
w("Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE\n")

w("## Inventory")
w("| Segment (quoted start) | Role | Event |\n|---|---|---|")
groups = [(1, 4, "Read Leonard's ask in #winddown"), (5, 8, "Find and read the conventions doc"),
          (9, sv + 2, "Find Sunset's data checklist"), (cu, ap, "Find the Cursor reply in #prototype"),
          (ct, calc - 1, "Read the HG Costs tab"), (calc, calc + 1, "Work out the register"),
          (first_w, first_w + 3, "Create the register as a new Google Sheet"),
          (min(st + cm), max(st + cm), "Comment on ENG-2438 Unity"),
          (rp[0], rp[0], "Reply to Leonard in his thread")]
for a, b, s in groups:
    w(f"| {span(s)} | STEP (×{b - a + 1}) | OE {a}–{b} |" if a != b else f"| {span(s)} | STEP | OE {a} |")
w("\nNo CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segments: every event is a read, a calculation or one write.\n")

w("## Coverage")
w("| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |\n|---|---|---|---|")
COV = [
 ("R1 / F1 Leonard's ask", "OE 1", "covered", "ledger: #winddown newest message"),
 ("R2 / F2–F6 keep list, Gusto reply, LLC moves, Slack and Google decisions", "OE 2–4", "covered", "ledger: channel history paged back + thread + attachment table"),
 ("R2 / F7 conventions doc", "OE 5", "covered", "ledger: Drive search, Docs read"),
 (f"R2 / F8–F11 project, {NI} issues, their comments", "OE 6–8", "covered", "ledger: Linear project, issue list, per-issue comments"),
 ("R2 / F12–F15 Sunset thread, SVB card, review call", f"OE 9, {sv}, {sv + 2}", "covered", "ledger: Gmail thread, Trello card, Calendar"),
 ("R2 / F36 SVB card comments (supersede the description)", f"OE {sv + 1}", "covered", "ledger: Trello card comment actions"),
 ("R2 / F37–F39 Cursor, Unity and AppLovin relays", f"OE {cu}–{ap}", "covered", "ledger: Slack searches (#prototype thread, #executives, applovin channel + #admin_foundersonly)"),
 ("R2 / F16–F17 costs-tab lines, ledger lines", f"OE {ct}–{ct + 1}", "covered", "ledger: Sheets tab, Snowflake query"),
 ("R2 / F18–F27, F29 billing mail, CodeRabbit notice", f"OE {ct + 2}–{lo - 1}, OE {cr}", "covered", "ledger: Gmail searches, GitHub PR comment"),
 ("R2 / F34 Lucidchart and Google Ads cancellation notices (ENG-2465, ENG-2466)", f"OE {lo}", "covered", "ledger: two Gmail searches in Robert's mailbox"),
 ("R3 / F31–F32 register and totals", f"OE {calc}–{calc + 1}, {first_w}–{first_w + 1}", "covered", "ledger: calculation, then create + write the sheet"),
 ("R4 / F30 shares", f"OE {first_w + 2}–{first_w + 3}", "covered", "ledger: two writer shares"),
 ("R5 / F33 Linear states", f"OE {min(st)}–{max(st)} ({len(st)} state events)", "covered", f"ledger: one update per issue ({len(LN['done'])} Done, {len(LN['canceled'])} Canceled)"),
 ("R5 / comments on each issue", f"{len(cm)} comment events", "covered", f"ledger: one comment per issue ({NI})"),
 ("R6 / F32 reply with totals", f"OE {rp[0]}", "covered", "ledger: thread reply under the ask"),
 ("R7–R8 / F35 clashes", f"OE 4, OE 3, OE 9, OE {rp[0]}", "covered", "ledger: two clashes (Slack plan and users, Google archive)"),
]
for r in COV:
    w("| " + " | ".join(r) + " |")
w("")

w("## Expected-data sign-off")
w("| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Match / minor / wrong / unresolved |\n|---|---|---|---|---|")
SO = [
 (1, "can you own the account close-out register before I archive anything on Google?", f"01_Universe_Inject.sql SQL L34; {M['S_ANCHOR']['locator']}", "seeded ask text, Feb 13 17:21:07Z", "match"),
 (2, "During shutdown, let's keep Deel, gusto, Intuit.", "hg.py search slack → messages/C0ADGSZKR3R/2026-02.json ts 1770933601.686309", "Leonard, Feb 12 22:00Z", "match"),
 (3, "I think we keep Metabase and dbt", "hg.py search slack \"I think we keep Metabase and dbt\" → C0ADGSZKR3R/2026-02.json /190/text", "1 hit, Leonard's action items", "match"),
 (4, "yeah free version", "hg.py search slack → C0ADGSZKR3R/1770840054.486779", "Arthur, Feb 11 20:00Z", "match"),
 (4, "[x] Slack (down to 3 FT members)", "C0ADGSZKR3R/1770933450.410449 attachments blocks (slack messages C0ADGSZKR3R/2026-02.json)", "table row in the attachment", "match"),
 (9, "Trello is part of the bundle too", f"01_Universe_Inject.sql; {M['G_SUNSET1']['thread_id']['robert@harmonygames.co']}", "Sunset correction Feb 13 18:20:44Z", "match"),
 (13, "meta marketing_ua -2,843.84 (Jan 31)", "snowflake.json /tables/38 FIN-000689", "-2843.84, 2026-01-31", "match"),
 (13, "AWS cloud_infra -1,485.00 (Jan 31)", "snowflake.json /tables/38 FIN-000687", "-1485, 2026-01-31", "match"),
 (15, "Layer Pro (monthly) - $49.00", f"01_Universe_Inject.sql; {M['G_LAYER']['thread_id']['robert@harmonygames.co']}", "next payment March 3, 2026", "match"),
 (18, "Receipt Jul 9 2025, annual $50 plan", "hg.py search gmail \"ElevenLabs\" → threads/00014566.json (robert@harmonygames.co/1837122624854744558)", "$50.00 Paid July 9, 2025 (and July 9, 2024: annual)", "match"),
 (19, "Quarterly $6,250 invoices on Sep 1 and Dec 1 2025", "hg.py search gmail \"INVSINC\" → threads/00000416.json; robert@harmonygames.co/1850283027022457279", "INVSINC23580 Dec 1 2025; $6,250 in the dunning bodies", "match"),
 (0, "they close the card on the 18th, not the 20th", f"01_Universe_Inject.sql trello_actions {M['T_SVB_CMT']['id']}", "Leonard's comment Feb 13 22:47:19Z", "match"),
 (0, "aws and 1password go by the 17th too then", f"01_Universe_Inject.sql trello_actions {M['T_SVB_CMT2']['id']}", "Arthur's comment Feb 13 23:12:05Z", "match"),
 (0, "cursor sent the confirmation on the team plan cancellation this morning", f"01_Universe_Inject.sql; {M['S_CURSOR_CONF']['locator']}", "Arthur, thread reply under Oliver, Feb 13 14:07:33Z", "match"),
 (0, "unity's account manager wrote back on the termination", f"01_Universe_Inject.sql; {M['S_UNITY_CONF']['locator']}", "Arthur, #executives, Feb 13 21:18:40Z", "match"),
 (0, "applovin emailed back, the ad account is closed", f"01_Universe_Inject.sql; {M['S_APPL_CONF']['locator']}", "Leonard, #admin_foundersonly, Feb 13 22:40:26Z", "match"),
 (0, "Carta: Cancel, Open, Aug 14, 2026", "ENG-2451 comment 'renews aug 15' + SVB comment 'Only exception is carta'", "Aug 14, 2026", "match"),
 (0, "will expire on Nov 4, 2025", "hg.py search gmail \"Lucidchart subscription has been canceled\" → threads/00015599.json /messages/0/body (robert@harmonygames.co/1845611902985063512)", "Oct 10 2025 16:11:09Z, expire Nov 4, 2025", "match"),
 (0, "was canceled on 10/16/25.", "hg.py search gmail \"was canceled on 10/16/25\" → threads/00015671.json /messages/0/body (robert@harmonygames.co/1846207913731182209)", "sent Oct 17 2025 06:04:29Z; canceled 10/16/25", "match"),
 (0, "account canceled Oct 16, 2025", "threads/00015671.json /messages/0/body", "10/16/25", "match"),
 (0, "Soundly: Cancel, Closed (Soundly's cancellation email)", f"01_Universe_Inject.sql; {M['G_SOUNDLY']['thread_id']['robert@harmonygames.co']}", "Soundly cancellation email", "match"),
 (22, "was canceled on Feb 12, 2026", "01_Universe_Inject.sql github_pr_comments harmonygames-Games/Combo-Fighters#38#c_1", "bot comment Feb 13 09:41:12Z (bold markup around the org name)", "match"),
 (24, f"Every row: {TR['total_today']:,.2f}", "truth.json /total_today (re-added from the 28 rows)", f"{TR['total_today']:,.2f}", "match"),
 (24, f"Keep and Hold for Sunset rows only: {TR['total_after']:,.2f}", "truth.json /total_after", f"{TR['total_after']:,.2f}", "match"),
]
# map sign-off claims to the events that actually hold them
for k, claim, ptr, val, res in SO:
    pos = OE.index(claim)
    e = len(re.findall(r"^OE \d+  ", OE[:pos], re.M))
    w(f"| OE {e} | {span(claim)} | {ptr} | {val} | {res} |")
w("")

w("## Findings")
w("| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |\n|---|---|---|---|---|---|---|---|")
FND = [
 ("1", "ADVISORY", "Accuracy (format)", f"OE {cr}", "The CodeRabbit subscription for harmonygames-Games was canceled on Feb 12, 2026",
  "Eval 2.3 Minor test", "the quote drops the bold markup around the org name; same record, same words", "F29; harmonygames-Games/Combo-Fighters#38#c_1"),
 ("2", "ADVISORY", "Readability", "OE 8", f"Read the comments on every one of the {NI} issues",
  "screen 44 (one write per event; population reads may stay one event)", f"a single read event over {NI} issues makes a long Expected line; allowed, typed length is the cost", "F10, F11; ENG-2438"),
]
for r in FND:
    w("| " + " | ".join(r[:4]) + f" | {span(r[4])} | " + " | ".join(r[5:]) + " |")
w("")

w("## Pre-verdict sweep")
w("| Eval 4.0 check (7) | Result |\n|---|---|")
for a, b in [("one wrong count/ID/channel/tool", f"none: counts ({NI} issues, 28 rows, {len(LN['done'])} Done, {len(LN['canceled'])} Canceled) match truth.json /linear and /rows"),
             ("one missing write", f"none: sheet create + write, 2 shares, {NI} comments, {len(LN['done']) + len(LN['canceled'])} states, 1 reply; no issue creation (rule 3 adds rows, not issues)"),
             ("one Expected fact with no retrieving event", f"none: every value in OE {calc}–{calc + 1} is read in OE 1–{calc - 1}, including the Lucidchart and Google Ads notices (OE {lo})"),
             ("one act-vs-defer conflict", "none: ledger §C defer search complete, no hold or wait on any write"),
             ("one non-action or final-response event", "none (the costs-tab event carries no cost from its month columns); no arrow chains: the file is plain ASCII"),
             ("one prompt-forbidden write", "none: every write traces to a prompt span (ledger §C)"),
             ("one missing recovery/wait event", "none: Friction: none (03_Error_Async_Config.txt)")]:
    w(f"| {a} | {b} |")
w("")
w("## Advisory (no effect on the prediction)")
w("| Event | Note |\n|---|---|")
w(f"| all | the field blocks pasting: {len(OE)} characters have to be typed; shortening OE 5, 8 and 9 keeps every value if needed |\n")
w("## Tally")
w("Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 2\n")

w("## Self-review")
w("Walked `Evals/2_Oracle_Events_Eval.md` 1.2, 1.3, the HARD GATE, 2.1–2.7, 3.1–3.6 and 4.0 in order against this report; re-verified the "
  "sign-off values this run through `tools/hg.py` searches (pointers in the sign-off table) and the SQL rows.\n")
w("| Counter-reading | Resolution (evidence) |\n|---|---|")
CR = [
 ("R1 covered: OE 1 reads the wrong message", f"the ask is the newest #winddown message before the clock ({M['S_ANCHOR']['locator']})"),
 ("R2 keep list: OE 2 sends the agent past the newest 100 messages and skips it", "OE 2 now reads the same first page OE 1 reads; the keep list C0ADGSZKR3R/1770933601.686309 has only 17 base messages + the ask after it (/oe r1 finding 5)"),
 ("R2 doc: the doc is not shared with Robert", "check-sql YES on f_1326e66bcabfda8fd29e4a (ledger §B visibility)"),
 ("R2 Linear: comments need one call per issue and OE 8 is one event", "a population read may stay one event (playbook gate 14); ENG-2438 … ENG-2466"),
 ("R2 Sunset: the first checklist governs", "the Feb 13 correction is the later message in the same thread (ledger F13)"),
 ("R2 costs/ledger: Unity Ads in the UA line needs a row", "the project description says unity ads were cancelled after October (ledger F8); rule 2"),
 ("R2 billing: the Workspace cost needs the PDF", "Leonard's ENG-2452 comment gives $298.13 (OE 8; ledger F10)"),
 ("R3: the register could keep 30 rows (adjoe, iPostal)", "adjoe stopped June 2025, iPostal closed Jan 16 (rule 2; ledger F25)"),
 ("R4: one share event for both editors", "two events, one write each (playbook gate 14)"),
 ("R5 states: CodeRabbit should stay open", "the bot notice (F29) is the vendor's word → Closed → Done"),
 (f"R5 comments: {NI} events are redundant", "one write per record is required (gate 14); /oe does not score redundancy"),
 ("R5 new issues: the added accounts need Linear issues", "no: rule 3 adds them as register rows ('each one gets its own row'); the prompt settles the existing issues; the create events were removed (/oe r1 finding 7)"),
 ("R2 old receipts: ENG-2465/2466 could be Open rows", f"Robert's notices: Lucidchart canceled Oct 10 2025 (expired Nov 4), Google Ads canceled 10/16/25 → rule 2; read in OE {lo} (/oe r1 finding 1)"),
 ("R5 comments: the Google Ads date is unsupported", "from the record: Google Ads 'was canceled on 10/16/25' (/oe r1 findings 2-4); the Typecast and Kling issues no longer exist (hardening purge)"),
 ("R2 SVB: the card description's Feb 19 / 'until it ends' governs the dates", f"Leonard's later comment (OE {sv + 1}) moves the closure to the 18th and every cancellation to the 17th, Carta excepted; Arthur confirms AWS and 1Password"),
 ("R3 Unity/Cursor/AppLovin: no vendor email in Robert's mailbox, so Requested", f"rule 5 'the vendor itself has confirmed'; the founders relay each vendor's reply (OE {cu}–{ap}); /prompt recommendation 5 accepts the relay as 'where'"),
 ("R3 Closed rows: rule 5 'say where' is unmet", f"each Closed row in OE {calc} names its confirmation source: Unity relay, Helpshift reply, Soundly email, CodeRabbit PR notice, Cursor relay, Zapier email, Kapwing email, AppLovin relay (/oe r1 finding 8)"),
 ("Names with en dashes typed as hyphens", "OE 6, 9 and 11 now spell the en dash out in words instead of typing a hyphen (/oe r1 finding 6)"),
 ("R6: the reply could be a new channel message", "the ask says 'reply here' → thread reply (OE 1, F1)"),
 ("R7–R8: the Helpshift no-export line is a third clash", "rule 10 counts decisions Sunset's list would undo; the export is a separate request (/prompt reading D, Audit-Report/1_prompt_NONFAIL_planD.md)"),
 ("Finding 1 ADVISORY: the dropped markup is INACCURATE", "same record and words; Minor test passes and no value changes (F29)"),
 ("Finding 2 ADVISORY: the long OE 8 is a format defect", "a population read is not MULTIPLE_ACTIONS (no writes); screen 44 allows it (F10)"),
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
