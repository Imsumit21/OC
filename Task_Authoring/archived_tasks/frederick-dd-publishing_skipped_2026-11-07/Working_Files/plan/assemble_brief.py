#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md (prep) from the rev1 SQL, ids, truth.json, the persona-view searches, the entity
output and the blind sweeps. Design facts only: requirements and record locators, never the prompt text itself."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools")); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(WF, "solver"))
import brief_facts as BF  # noqa: E402
import solver as SV  # noqa: E402
B, IDS, I, BASE, SL, MSG, TH = BF.B, BF.IDS, BF.I, BF.BASE, BF.SL, BF.MSG, BF.TH
term = B.term
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
AGG = SV.aggregates(TRUTH); TOT = AGG["totals"]
SRCH = {r["fid"]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json")))}
M = {m["key"]: m for m in B.M}
FRED, LEO = "frederick.stone@harmonygames.co", "leonard.hayes@harmonygames.co"
HUB = MSG["hub"]
L = []; A = L.append
def rd(n): return open(os.path.join(HERE, n)).read().rstrip()
live = sorted((v for v in TRUTH.values() if v["Status"] == "Live"), key=lambda v: -v["12-month value"])
def names(g): return ", ".join(AGG["groups"].get(g, []))
def addr(m): return f"{m['person'][0].lower()}@{m['dom']}" if m.get("person") else f"partnerships@{m['dom']}"
n_no = [k for k, v in TRUTH.items() if v["Status"] == "No reply"]

A("# Prompt Brief — frederick_dd_publishing · prep")
A("> Built 2026-11-06 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (rev2; rev1 passed /injection and failed /prompt on one fork), 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json, 03_Error_Async_Config.txt and three blind passes (plan/sweep/) · Persona view verified: all · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.")
A("")
A("## 1 · Assignment fit")
A("")
A("| Axis | Assigned value | What it requires here (cited) |")
A("|---|---|---|")
A(f"| Business function | Executive | Maps to `task_categories.md` 'Founders / Exec / Strategy' (strategic decisions, priorities and executive coordination): the founders choose which publisher, if any, gets Domino Delights (hub {HUB}; Leonard's Aug 25 post {BASE['rights_post']}) |")
A(f"| Persona | Frederick Stone, {FRED}, Co-founder (roster frederick_stone; department Executive) | Voice: a co-founder handing his assistant a job Leonard gave him; plain, brief. Remit: he ran the Appodeal talks ({BASE['appodeal_thread']}), was handed the Rayking mail ({BASE['rayking_thread']}) and opened publisher outreach on Sep 24 ({BASE['tranche']}). Reads: his mailbox, calendar and Drive shares; #executives C07C2866011, #bridge-pitch C096HFA5Z8W, #analytics C069FF9Q57S, DM D05S58U4SAK |")
A(f"| Competency | Finance | Taxonomy screen 9: 'Budget, forecast, cap table, fundraising'; outputs 'Models, spreadsheets, decks'. Here: a forecast model of publisher offers for a founders' decision, in a Google Sheet (rule doc {I['rule_doc']} 'Layout') |")
A(f"| Task skill | Analysis and synthesis (stacked: Retrieval, Actions) | Screen 10 'Combine information from multiple sources and compute, model, reconcile, or diagnose to reach findings': reconcile each publisher's latest terms across term sheets, a calendar note, a card comment and Slack, then compute value and Q4 cash ({I['rule_doc']}) |")
A(f"| Task type | long-horizon (Long Horizon → extreme profile; requester-confirmed volume and cohort exceptions in the manifest) | 10 services carry weight: Gmail (24 publisher threads, ESG thread), Drive and Docs (8 term sheets, rule doc), Sheets (outreach, model), Slides (one-pager), Slack (4 containers), Trello (UA/BD board), Calendar (3 calls), Linear (ENG-2362), Contacts, plus Snowflake ({'ANALYTICS.MONETIZATION.REVENUE_DAILY'}). hardness_gate PASS in the dossier. 26 publishers, 86 write objects |")
A("")
A("## 2 · Situation")
A("")
A("| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |")
A("|---|---|---|---|")
A(f"| The founders meet on Monday Oct 6 to decide on Domino Delights publishing; Leonard has asked Frederick for a model of what each publisher would bring in, with follow-up on the board and in Contacts | Frederick (To, INBOX) | hub {HUB}; event {I['monday_event']}; card {I['dd_card']} | Leonard's mailbox copies; P&L workbooks (not needed, dossier 'Known data issues') |")
A("")
A("## 3 · Investigation → action")
A("")
A("Questions the run must resolve (answers only in §5 and the records, never in the prompt):")
for i, (q, r) in enumerate([
 ("Who is in: the outreach sheet plus any publisher that came to one of the four founders about DD since Apr 1, 2025, however it reached them, less passed-along names and co-dev, engine or investment talks", I["rule_doc"]),
 ("Each publisher's status, first that fits, from its thread, its terms and anything said about it elsewhere", I["rule_doc"]),
 ("The latest terms for each offer, wherever they are", I["rule_doc"]),
 ("Whether an offer's terms take something the founders keep", BASE["rights_post"]),
 ("Each Live offer's 12-month value and Q4 cash, given the signing date", MSG["esg_note"]),
 ("What publisher money is actually in the SVB account", I["rule_doc"]),
 ("The game's keep value from the named warehouse table", I["rule_doc"]),
 ("Which offer goes first", I["rule_doc"]),
 ("Who is already in Contacts, who has a card already, and what was each publisher sent", I["outreach_sheet"]),
 ("Which notes Leonard asked for on what goes out to publishers, and who gets one", I["rule_doc"]),
], 1):
    A(f"{i}. {q} ({r}).")
A("")
A("Writes those answers feed (each depends on a publisher's status or terms):")
for w in [f"the model sheet in {I['dd_folder']}", f"checklists and items on {I['dd_card']}", f"follow-up cards on list {B.BD_LIST}, and comments on {I['oakline_card']} and {I['sunfold_card']}", "Gmail drafts: nudges and notes", "Contacts entries", "calendar reminders", f"one reply on the hub thread {I['hub_thread']}"]:
    A(f"- {w};")
A("")
A("## 4 · Pinned final state (UGT anchor)")
A("")
A("| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |")
A("|---|---|---|---|---|---|")
A(f"| D1 model sheet | a native Google Sheet called DD publishing model; tab Publishers with Publisher, Status, Advance, Monthly installs, 12-month value, Q4 cash, one row per publisher ({TOT['publishers']}), figures only on Live rows; tab Summary with Keep value, First pick, Banked so far | folder {I['dd_folder']} (A3) | — | gsheets_create_spreadsheet, gsheets_values_update, gdrive_move_file | {I['rule_doc']} 'Layout' |")
A(f"| D2 checklists | one checklist per status ({TOT['checklists']}), one item per publisher ({TOT['checklist_items']}) | card {I['dd_card']} (A2) | — | trello_create_checklist, trello_create_check_item | {I['dd_card']} desc |")
A(f"| D3 follow-ups | a card named F/up with plus the publisher's name for each Live, Waiting on us and No reply publisher without one ({TOT['cards_new']}); a comment with the status on an existing card ({TOT['card_comments']}: {I['oakline_card']}, {I['sunfold_card']}) | list {B.BD_LIST} on board {B.UABD_BOARD} | — | trello_create_card, trello_add_comment | {I['dd_card']} desc |")
A(f"| D4 nudges | a one-line draft to each No reply publisher ({TOT['nudges']}), not sent | Frederick's Gmail drafts ({FRED}) | {', '.join(addr(M[k]) for k in n_no)} | gmail_create_draft | {I['dd_card']} desc |")
A(f"| D5 organic notes | a short draft with the organic figure, $0.50 D30 ARPI, to each publisher that got the May one-pager and still has an offer in ({TOT['organic_notes']}), not sent | Frederick's Gmail drafts ({FRED}) | {', '.join(addr(M[k]) for k in AGG['groups']['organic_note'])} | gmail_create_draft | {I['standing_line']} |")
A(f"| D6 contacts | a contact for everyone at a publisher who gave terms or said no, with the company in the job title, skipping anyone already there ({TOT['contacts_added']}) | Contacts (skip {I['anika_contact']}, {I['lena_contact']}) | — | contacts_add_new_contact | {HUB} |")
A(f"| D7 reminders | one event per Live offer on its response date, named for the publisher ({TOT['reminders']}) | Frederick's calendar ({FRED}) | — | gcal_create_event | {I['rule_doc']} 'Reminders' |")
A(f"| D8 reply | which offer goes first, its 12-month value, its Q4 cash, publisher money banked so far | reply on the hub thread {I['hub_thread']} | {LEO} | gmail_reply_to_message | {HUB} |")
A("")
A("Alternatives a careful run could defend, and how each is settled:")
for a in [
 f"D1 destination: created in the folder or created elsewhere and moved there; both end in {I['dd_folder']}.",
 f"D1 rows: the 26 keys; Homa, NCsoft, Tilting Point, Tamatem and the Sep 24 lead stay out ({I['rule_doc']}, {HUB}).",
 f"D1 Advance for Oakline: the total, $30,000 ({term('Oakline Games')}; the rule doc says 'the total advance').",
 f"D1 Q4 cash for Oakline: $30,000, the resent $10,000 and the $20,000 on Dec 14 ({I['arthur_cash']}: it'll land in October).",
 f"D3 card names: the publisher's name after 'F/up with' (the card's wording, {I['dd_card']}); existing cards named for people keep their names and get a comment.",
 f"D4 Summit: to partnerships@summitmobile.io, the address Frederick wrote to, not the noreply@ sender ({TH['Summit Mobile']}).",
 f"D4, D5 thread: a draft reply on the publisher's thread or a new draft to the same person are both the draft asked for; neither {I['dd_card']} nor {I['standing_line']} says which.",
 f"D5 Moonrail: no note, its offer is off ({SL['kestrel_post']}); Oakline, Sunfold, Copperleaf and Redwood: no note, they didn't get the one-pager ({I['outreach_sheet']}).",
 f"D6 job field: the company must be in it; any role words are representational ({HUB}). Copperleaf's and Redwood's people come from {SL['copperleaf_relay']} and {I['eng2362_comment']}.",
 f"D7 time of day, duration and all-day form are representational; the date and one event per offer are not ({I['rule_doc']}).",
 f"D8 reply or reply-all on {I['hub_thread']}: both reach Leonard; extra lines are allowed. The Q4 figure is the first pick's, never a total across offers ('what it brings in during Q4', {HUB}).",
 f"Who sends: every write is the agent's on Frederick's behalf; drafts stay drafts ({SL['standing_line']}, {I['dd_card']}).",
]:
    A(f"- {a}")
A("")
A("### 4b · Canonical outcome (all fair outcomes)")
A("")
A("| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by | Allowed equivalence class | Material / representational |")
A("|---|---|---|---|---|---|")
A(f"| D1 | Name and home | a native Sheet named DD publishing model whose final parent is {I['dd_folder']} | — | created there or moved there | material |")
A(f"| D1 | Tabs | Publishers and Summary, with the columns in {I['rule_doc']} | — | case | material |")
A(f"| D1 | Rows | {', '.join(TRUTH[k]['Publisher'] for k in TRUTH if TRUTH[k]['Status'])} ({I['rule_doc']}, {I['outreach_sheet']}) | — | record spelling or an obvious short form | material |")
SRC = {k: (term(k) if k in B.TERM_DOCS else SL["copperleaf_relay"] if k.startswith("Copper") else "ENG-2362") for k in TRUTH}
for v in live:
    A(f"| D1 | {v['Publisher']} | Live; Advance {v['Advance']:,}; Monthly installs {v['Monthly installs']:,}; 12-month value {v['12-month value']:,}; Q4 cash {v['Q4 cash']:,} (solver/truth.json; {SRC[v['Publisher']]}) | — | currency symbols, commas | material |")
for s in ("Withdrawn", "Out on rights", "Passed", "Waiting on us", "No reply"):
    A(f"| D1 | {s} | {', '.join(k for k, v in TRUTH.items() if v['Status'] == s)}; figures blank ({I['rule_doc']}) | — | a dash or blank in figure cells | material |")
A(f"| D1 | Summary | Keep value 12,723.96; First pick Copperleaf Games; Banked so far 0 ({I['rule_doc']}, {SL['arthur_cash']}) | — | keep value to the dollar ($12,724); 'none' or 'nothing' for banked | material |")
A(f"| D2 | Checklists | Live, Withdrawn, Out on rights, Passed, Waiting on us, No reply on {I['dd_card']}, each holding the publishers of that status | — | item wording carrying the publisher's name | material |")
A(f"| D3 | New cards | F/up with: {names('card_new')}, on list {B.BD_LIST} | — | short forms of the publisher's name | material |")
A(f"| D3 | Comments | Live on {I['oakline_card']} and {I['sunfold_card']} | — | extra words beside the status | material |")
A(f"| D4 | Nudges | {', '.join(n_no)}: one each, unsent ({I['dd_card']}) | 'Leave a one-line nudge' ({I['dd_card']}) | wording is the run's; new draft or draft reply | wording representational |")
A(f"| D5 | Notes | {names('organic_note')}: one each, unsent, carrying $0.50 D30 ARPI ({I['standing_line']}) | 'one short note each' ({I['standing_line']}) | wording is the run's; new draft or draft reply | figure material, wording representational |")
A(f"| D6 | Contacts | {names('contact_add')}: person, address, company in job ({HUB}) | — | role words | material |")
A(f"| D7 | Reminders | " + "; ".join(f"{v['Publisher']} {v['Respond by']}" for v in live) + f" on {FRED}'s calendar | — | time of day, all-day form | date material |")
A(f"| D8 | Reply | Copperleaf Games; $67,200; $32,000; $0 banked, on {I['hub_thread']} | — | reply or reply-all; 'nothing banked yet'; added explanation | material |")
A("")
A("## 5 · Discovery map")
A("")
A("Root causes and corrections appear only here and are never in the prompt.")
A("")
A("| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |")
A("|---|---|---|---|---|---|---|")
NAMED = {"F1": "Yes (A1, the job's source)", "F4": "Yes (A2, on the hub)", "F5": "Yes (A3, the destination)"}
for f in BF.F:
    fid, label, value, loc, met, risk = f[:6]
    A(f"| {fid} {label} | {value} | {loc} | YES | {met} | {risk} | {NAMED.get(fid, 'No')} |")
A("")
A("## 5a · Search-as-persona proof")
A("")
A("`persona_view.py search` reads the base only; seeded hits are counted from the SQL rows Frederick can see (the same rows check-sql proves visible). One row per §5 fact.")
A("")
A("| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |")
A("|---|---|---|---|---|---|---|")
for f in BF.F:
    r = SRCH[f[0]]
    A(f"| {f[0]} {f[1]} | {r['service']} | \"{r['query']}\" | base {r['base']}; seeded {r['seeded']} | {r['hidden']} | {r['first']} | {r['found']} |")
A("")
A("Search outputs, verbatim:")
A("")
A("```")
A(rd("brief_searches.txt"))
A("```")
A("")
A("Search-behaviour risks (design notes only, never in the prompt): runs latch onto the outreach sheet as the population; they stop at Marek's 'sent' mail; they rarely open replies under old roots; they read the first lines of a calendar description; they treat cards named for people as unrelated; Snowflake isn't advertised, but the rule doc names the table.")
A("")
A("## 6 · Triggers, incorporation and implicit requirements")
A("")
A("| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |")
A("|---|---|---|---|---|")
R = [
 ("R1 population", I["rule_doc"], "deliverable (the model)", f"{HUB} → {I['rule_doc']} · YES · one doc · states who counts, not who they are", "yes"),
 ("R2 status", I["rule_doc"], "deliverable", f"{I['rule_doc']} · YES · one doc · states the order, not the answers", "yes"),
 ("R3 latest terms", I["rule_doc"], "deliverable", f"{I['rule_doc']} 'latest terms' · YES · one sentence · no values", "yes"),
 ("R4 12-month value", I["rule_doc"], "deliverable", f"{I['rule_doc']} · YES · a formula, no results", "yes"),
 ("R5 Q4 cash and banked", I["rule_doc"], "deliverable", f"{I['rule_doc']} and {HUB} · YES · a definition, no results", "yes"),
 ("R6 rights", BASE["rights_post"], "constraint, via the doc", f"{I['rule_doc']} → {BASE['rights_post']}, {BASE['sync_doc']} · YES · 'the August sync' · a position, not a verdict", "yes"),
 ("R7 first pick", I["rule_doc"], "deliverable", f"{I['rule_doc']} · YES · a definition", "yes"),
 ("R8 keep value", I["rule_doc"], "deliverable", f"{I['rule_doc']} · YES · names the table, gives no number", "yes"),
 ("R9 board writes", I["dd_card"], "deliverable (the card)", f"{HUB} → {I['dd_card']} · YES · one card · instructions", "yes"),
 ("R10 contacts", HUB, "deliverable, via the hub", f"{HUB} · YES · one sentence · no names", "yes"),
 ("R11 reminders", I["rule_doc"], "deliverable, via the doc", f"{I['rule_doc']} · YES · no dates", "yes"),
 ("R12 organic notes", I["standing_line"], "deliverable, via the doc's last line", f"{I['rule_doc']} (says the notes are owed) → {I['standing_line']} · YES · one reply · an instruction, no recipient list", "yes"),
 ("R13 reply", HUB, "deliverable and recipient", f"{HUB} · YES · lists the asks, gives no values", "yes"),
]
for r in R:
    A("| " + " | ".join(r) + " |")
A("")
A("| Anchor | May be named |")
A("|---|---|")
A("| A1 | Leonard's email from yesterday; Leonard's email yesterday; his email |")
A("| A2 | the DD publishing card |")
A("| A3 | my DD publishing folder; the DD publishing folder |")
A("")
A("## 7 · Dates and constraints")
A("")
A("| Item | Absolute date or value | Source | Past fact or deadline |")
A("|---|---|---|---|")
for r in [
 ("Today", "Wed Oct 1, 2025 (Pacific)", f"00_Task_Context.json universe.persona_today; the day after {HUB}", "clock"),
 ("Leonard's email ('yesterday')", "Tue Sep 30, 2025 4:10 PM PT = 2025-09-30T23:10:00Z", HUB, "past fact"),
 ("Founders' meeting", "Mon Oct 6, 2025 10:00 AM PT = 2025-10-06T17:00:00Z", I["monday_event"], "deadline (plan field)"),
 ("Scope start", "Apr 1, 2025", I["rule_doc"], "past fact"),
 ("Signing, as first assumed", "Oct 31, 2025", I["rule_doc"], "superseded"),
 ("Signing", "Nov 14, 2025", MSG["esg_note"], "deadline"),
 ("Q4 window", "Oct 1 to Dec 31, 2025", I["rule_doc"], "deadline"),
 ("Net 30 / 45 / 60 from Nov 14", "Dec 14, 2025 / Dec 29, 2025 / Jan 13, 2026", I["rule_doc"], "computed"),
 ("Response dates", "Oct 17 (Tallwater, Copperleaf), Oct 24 (Oakline, Harbor Lane), Oct 31 (Sunfold, Wavecrest, Redwood)", f"{term('Tallwater Games')}, {SL['copperleaf_relay']}", "deadlines"),
 ("Keep-value months", "Jul, Aug, Sep 2025", "snowflake.wh_analytics__monetization__revenue_daily", "past fact"),
 ("Oakline's wire", "sent Sep 29, 2025; returned; resent the week of Oct 6", f"{MSG['Oakline Games:2']}, {SL['arthur_cash']}", "past fact"),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("## 8 · Difficulty levers")
A("")
A("| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |")
A("|---|---|---|---|---|")
A(f"| Ambiguity | yes | yes | where each offer and correction lives; the prompt names the job and the known destinations only (A1, A2, A3) | vague about where answers live, never about what's asked |")
A(f"| Dynamic change | yes | yes | term sheets, Marek's 'sent' and the rule doc's Oct 31 are met first (T1, T2, T7, T9) | the prompt names neither the summary nor the correction |")
A("| Multi-source | yes | yes | 10 services plus Snowflake | no source named as an exact artifact beyond the anchors |")
A("| Async | no | — | — | no wait configured (03_Error_Async_Config.txt: Friction: none) |")
A("| Error recovery | no | — | — | no forced error |")
A("| Access control | no | — | — | every deciding record is Frederick-visible (§5a) |")
A("")
A("## 9 · Must not appear in the prompt")
A("")
A("- Tool and server names (`Evals/references/tools/catalog.json`): gmail_search_messages, gmail_get_thread, gmail_reply_to_message, gmail_create_draft, gdrive_search, gdrive_move_file, gdocs_get_document, gsheets_create_spreadsheet, gsheets_values_update, gslides_get_presentation, slack_read_thread, trello_create_card, trello_add_comment, trello_create_checklist, trello_create_check_item, contacts_add_new_contact, contacts_search_contacts, gcal_create_event, snowflake_execute_query, and any MCP server name.")
A("- Ids and opaque names: any f_/d_/evt_ id, thread or message id, Slack channel id or ts, ENG-2362, card or list ids, PERSON_ tokens, the warehouse table name.")
A("- Root causes and findings (from §5): the returned wire, the Tallwater note, the Sunfold comment, Kestrel, the rights position, Copperleaf, Redwood, the Nov 14 date, the organic figure and Leonard's standing line.")
A("- The rules themselves: status order, who's in, the value formula, the Q4 definition, reminders, layout.")
A("- Any publisher name, status, amount, date or count (26 publishers, 7 Live, 15 cards, 14 contacts, 10 drafts, 7 reminders).")
A("- Wording close to a fundraising hand-off, investor list or bridge round (dataset-duplicate risk).")
A("- Markdown, numbered steps, per-deliverable content lists or format rules (they belong in the records).")
A("")
A("## 10 · Entity traps")
A("")
A("```")
A(rd("entity_brief.txt"))
A("```")
A("")
A("| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |")
A("|---|---|---|---|")
for r in [
 ("Leonard Hayes", "file alias leonard@", "one person", LEO),
 ("Arthur Blake", "file alias blake@", "one person", "arthur.blake@harmonygames.co"),
 ("Robert", "no surname in any service", "one person", "robert@harmonygames.co"),
 ("Frederick Stone", "GitHub display name 'Ryan' (S04); file alias frederick@", "GitHub not used", FRED),
 ("UA/BD board", "the other boards, each with its own lists", "the card's board", f"{B.UABD_BOARD} (list {B.BD_LIST})"),
 ("the ground rules doc", "the co-dev doc", "scope: DD publishing vs co-dev", f"{I['rule_doc']} vs {I['codev_doc']}"),
 ("Moonrail Studios", "Kestrel Group (its parent)", "one offer, one row", f"{TH['Moonrail Studios']}, {I['anika_contact']}"),
 ("Sunfold Mobile", "the card 'F/up with Lena'", "one publisher, named for its contact", f"{term('Sunfold Mobile')}, {I['sunfold_card']}"),
 ("Oakline Games", "the card 'F/up with Marek'", "one publisher, named for its contact", f"{term('Oakline Games')}, {I['oakline_card']}"),
 ("Summit Mobile", "its noreply@ sender", "the partnerships@ address is the contact", TH["Summit Mobile"]),
]:
    A("| " + " | ".join(r) + " |")
A("")
A("## 11 · Pre-submit checklist")
A("")
for box in [
 "Persona voice: an ordinary request from Frederick to his assistant; clean spelling; no spec-sheet layout",
 "Names Leonard's email from yesterday (A1) as the source of the job, not its rules",
 "Names my DD publishing folder (A3) for the model and asks for the reply to Leonard on his email (R13)",
 "No publisher name, status, count, date, amount, rule, id or tool name (§9)",
 "No hint, riddle, hedge, if-chain or audit-form wording; no fundraising or investor framing",
 "Every deliverable in §4 is reachable from the prompt or Leonard's email",
 "hardness_v2_check RULE_IN_PROMPT clean; word count 20–4,000",
]:
    A(f"- [ ] {box}")
A("")
A("## 12 · Blockers and routed defects")
A("")
A("- No blocker. Blind sweeps ran before this stage; every fork and coherence finding they raised was settled in records (dossier 'Blind sweeps'; plan/sweep/).")
A(f"- Rev1 passed /injection and failed /prompt on one fork (`run_forensics/rev1/platform_prompt_review.md`): whether the organic-figure notes were part of this job. Rev2 settles it in the rule doc's last line ({I['rule_doc']}), so /injection, /prompt and /hardness must run again.")
A(f"- For the pre-check to prove: the calendar description route on {I['pb_event']}, and card and checklist writes on the UA/BD board.")
A("- Unverified: none load-bearing.")
A("")
A("## 13 · Self-review")
A("")
A("Re-read as Eval 1 Phases 1–3 against this brief (brief mode). Load-bearing values were re-read from the rev1 SQL or through `tools/hg.py` in this run (§5a outputs, dossier check-sql). Three blind passes matched the solver on every value; the last found 0 forks.")
A("")
A("| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
 ("Fair readings", "Oakline's Q4 cash could be $20,000, because a resend is only a promise", f"{I['arthur_cash']}: 'so it'll land in October'; the rule doc counts money that lands Oct 1 to Dec 31", "settled in a record"),
 ("Fair readings", "phone changes aren't 'in writing', so Tallwater and Sunfold keep their term-sheet terms, which flips the pick to Sunfold", f"'in writing' tests Live; {I['rule_doc']} says 'Use the latest terms we have from them, wherever they are, calls included'", "settled in a record"),
 ("Fair readings", "the Sep 24 lead could be a sheet publisher such as Kitebridge", f"{HUB}: 'never made it onto your sheet'", "settled in a record"),
 ("Clarity", "reminders could be one per date; notes could live in a Doc", f"{I['rule_doc']}: 'One for each Live offer'; {I['standing_line']}: 'left in your Gmail drafts'", "settled in a record"),
 ("Clarity", "'reply here' could read as a new mail or a send of the drafts", f"{HUB} says reply here; {I['dd_card']} and {I['standing_line']} keep the drafts unsent", "settled in a record"),
 ("Incorporation", "the organic note is graded, but no prompt word asks for it, and a line saying it 'still applies' could be a limit on content (rev1 /prompt fork)", f"{I['rule_doc']}'s last line now says the notes aren't done and to do them as part of this; the hub points at that doc; {I['standing_line']} states who and what", "incorporated"),
 ("Incorporation", "the hub could be read as handing over an answer", f"{HUB}, {I['rule_doc']} and {I['dd_card']} state rules and asks, no publisher or value", "instructions, not answers"),
 ("Truthfulness", "a prompt premise like 'Leonard emailed yesterday' could be off", f"{HUB} is Tue Sep 30 23:10Z = 4:10 PM PT, the day before Wed Oct 1 (§7)", "holds"),
 ("Feasibility / ACL", "a deciding record could sit outside Frederick's view", "check-sql PASS (dossier 1.E); §5a finds every fact as frederick_stone; Linear, Trello, Contacts and Snowflake are unscoped", "holds"),
 ("Feasibility / ACL", "a sheet with two tabs, drafts and checklists may not be writable", "catalog has gsheets_create_spreadsheet, gsheets_values_update, gmail_create_draft, trello_create_checklist and trello_create_check_item; the UA/BD board write is for the pre-check to prove", "holds; pre-check"),
 ("Contrived register", "naming the folder and the card could read as a spec sheet or a hint", "both are destinations the persona knows from his own folder and Leonard's mail; no rule, publisher or trap is named", "ordinary request"),
]
for c in CR:
    A("| " + " | ".join(c) + " |")
A("")
A("Unresolved: thread form of the drafts and the reminders' time of day stay open by design (accepted both ways in §4b). No independent red team ran (REDTEAM_* unset).")
A("")
out = os.path.join(WF, "04_Prompt_Writing_Brief.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, len(L), "lines")
