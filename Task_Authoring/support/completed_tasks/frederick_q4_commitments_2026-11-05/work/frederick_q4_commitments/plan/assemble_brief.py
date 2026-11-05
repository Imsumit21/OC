#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md (prep) from the rev4 SQL, the ids, truth.json, the persona-view
searches (plan/brief_searches.json/.txt), the entity output (plan/entity_brief.txt) and the blind fork sweeps.
Design facts only: the brief carries requirements and record locators, never the prompt text itself."""
import collections
import contextlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B  # noqa: E402

IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
SRCH = {r["fid"]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json")))}
I, BASE, SL = B.IDS, B.BASE, IDS["slack_mid"]
FRED = "frederick.stone@harmonygames.co"
M = {m["key"]: m for m in B.M}
HUB_MSG = IDS["msg"]["hub"]
TODO_LIST = "640643a3fd8f3ca308d93195"
BOARD = "640643a3fd8f3ca308d9318e"
ESG_INTAKE = "9b0185e445572aeee9f27d35"


def rd(name):
    return open(os.path.join(HERE, name)).read().rstrip()


def dname(d):
    if not d:
        return "blank"
    import datetime as dt
    x = dt.date.fromisoformat(d)
    return f"{x.isoformat()} ({x.strftime('%a %b')} {x.day}, {x.year})"


L = []
A = L.append
by_class = collections.defaultdict(list)
for k, v in TRUTH.items():
    if v.get("Decision"):
        by_class[v["Decision"]].append(k)
groups = collections.defaultdict(list)
for k, v in TRUTH.items():
    for g in v.get("groups") or []:
        groups[g].append(k)
IN = [k for k, v in TRUTH.items() if v.get("Decision")]
OUT = [k for k, v in TRUTH.items() if not v.get("Decision")]

A("# Prompt Brief — frederick_q4_commitments · prep")
A("> Built 2026-11-04 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md, "
  "01_Universe_Inject.sql (rev4), 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json and three blind fork "
  "sweeps (plan/blind_fork_sweep.md, plan/blind_fork_sweep_rev3.md, plan/blind_fork_sweep_rev4.md) · Persona view verified: all (check-sql PASS on "
  "168 load-bearing ids; every §5 fact found by a natural search as frederick_stone, §5a) · 03_Error_Async_Config.txt: "
  "Friction: none (error-async gate PASS) · no 02_Reference_Files_Manifest.md (no attachments)")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.")
A("")

# ---------------------------------------------------------------- 1
A("## 1 · Assignment fit")
A("")
A("| Axis | Assigned value | What it requires here (cited) |")
A("|---|---|---|")
A("| Business function | Executive | Maps to `task_categories.md` 'Founders / Exec / Strategy' (strategic decisions, priorities and executive coordination): a co-founder runs the company's vendor and partner commitments under the founders' runway rule while the CEO is away (hub " + HUB_MSG + ") |")
A(f"| Persona | Frederick Stone, {FRED}, Co-founder (roster frederick_stone; department Executive) | Voice: a co-founder handing his assistant a job Leonard gave him; plain, brief. Remit: he owns the vendor and partner relationships (Contacts 175c0d7bc72ed244b944cb90 'Commercial Lead, Marketing & Business Development'), most counterparties wrote to him ({IDS['threads']['Framewell']}, {IDS['threads']['Pingwise']}), he registered the Nintendo portal account (C07C2866011/1757011358.730529), and Leonard handed him the backlog by name ({HUB_MSG}). Read scope: Gmail own mailbox, Slack #executives C07C2866011 and DM D05S58U4SAK, his calendar, Drive he owns or is shared; Trello, Linear, Contacts unscoped |")
A(f"| Competency | Corporate Ops | Taxonomy screen 8: 'Fundraising, board, legal/contracts, vendor, HR'; outputs spreadsheets, memos. Here: vendor and partner commitments (vendor) and signature/counsel routing under ESG Law's signing note (legal/contracts, {IDS['msg']['esg_note']}); the output is a spreadsheet log in his folder {I['q4_folder']} |")
A(f"| Task skill | Actions (stacked: Retrieval, Analysis and Synthesis) | Screen 10 'Create or update records in a connector … changing system state': a new sheet, ~31 written answers and cancellations, 7 Trello cards on board {BOARD}, 3 ESG intake emails, ~32 Contacts, ~14 calendar reminders and one reply on the hub thread; each write follows a per-company decision that needs reading and reconciling records across services |")
A(f"| Task type | long-horizon (Long Horizon → extreme profile) | 10 services carry weight (manifest services; hardness_gate PASS in the dossier): Gmail (36 company threads, 47 seeded threads), Drive/Docs/Slides (36 papers in {IDS['paperwork_folder']}), Sheets (template, tracker), Slack (#executives Sep, DM), Trello (board {BOARD}), Linear (ZOM-567), Calendar (3 events), Contacts (170 base + 4). Call budget 237 planned (manifest call_budget, volume_exception floor 200); a lean correct run is ~150 calls (requester target > 130 per run) |")
A("")

# ---------------------------------------------------------------- 2
A("## 2 · Situation")
A("")
A("| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |")
A("|---|---|---|---|")
A(f"| Leonard is in LA from Oct 1 and has handed Frederick the vendor and partner backlog: every outside company with an offer, trial, quote, terms or ask waiting on Harmony Games must be logged, decided under the founders' runway guardrails and answered this week, with signatures routed to Leonard or Arthur | Frederick (To, INBOX) | hub {HUB_MSG} (thread {I['hub_thread']}), Tue Sep 30 23:20Z (4:20 PM PT) | Leonard's, Robert's and Arthur's own mailbox and calendar copies (companions only; never needed); #admin_foundersonly C04UEQVDVB7 (NO, not used) |")
A("")

# ---------------------------------------------------------------- 3
A("## 3 · Investigation → action")
A("")
A("Questions the run must resolve (answers only in §5 and the records, never in the prompt):")
A(f"1. Which outside companies fall inside Leonard's scope (an offer, trial, quote, terms or ask in front of us that one of us engaged with), and which his exclusions take out ({HUB_MSG}).")
A(f"2. For each, has one of the founders already answered it (in-thread, on a call, in Slack or a DM), who, and was the answer 'later' ({I['guardrails_doc']} step 1).")
A("3. Would it cost cash between Oct 1 and Dec 31 — including trials or pilots that convert, offers that must be taken up before January, and travel a partner books (the Monday change) — and how must it be cancelled.")
A(f"4. Is it on Arthur's keep-running list ({I['keep_card']}).")
A(f"5. Does taking it need someone to accept terms or sign, and does ESG Law need to review it ({IDS['msg']['esg_note']}).")
A(f"6. The README's Next date for each ({I['readme_doc']}), the January review date ({I['review_event']}), and each company's contact and the address an answer must go to.")
A("")
A("Writes those answers feed (each depends on the company's decision):")
A(f"- the log sheet in {I['q4_folder']} (rows, decisions, dates);")
A("- a written answer to each company waiting (reply on its thread, or the address its paper or notice names);")
A(f"- a card on the To Do list {TODO_LIST} of board {BOARD} for each Sign row; an ESG intake email to {ESG_INTAKE} for each agreement ESG must review;")
A("- a Contacts entry for each company's person not already in Contacts; calendar reminders on the January review date for parked rows and 'later' answers;")
A(f"- one reply on the hub thread {I['hub_thread']} with what we keep and what waits on a signature.")
A("")

# ---------------------------------------------------------------- 4
A("## 4 · Pinned final state (UGT anchor)")
A("")
A("| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |")
A("|---|---|---|---|---|---|")
A(f"| D1 log sheet | one native Google Sheet named per the README ('Q4 commitments log'), header copied from the template ({I['template_sheet']}): Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date; one row per in-scope company ({len(IN)} rows) | folder {I['q4_folder']} (anchor A2) | — | gsheets_create_spreadsheet + gsheets_values_update (+ gdrive_move_file into the folder) | {I['readme_doc']}, {I['guardrails_doc']}, every company's records |")
A(f"| D2 written answers | one written answer per company waiting to hear from us ({len(groups['written_answer'])}), matching its decision: End = no / cancellation in writing; Keep = staying; Sign = with Leonard or Arthur (and counsel where ESG reviews); Park = picking it up in January | each company's own thread (reply) or the address its paper or notice names; Clipforge: billing@paylane.io ({IDS['msg']['clipforge_notice']}) | the counterparty | gmail_reply_to_message / gmail_send_message | {I['guardrails_doc']} 'Answers', {HUB_MSG} |")
A(f"| D3 signature cards | one card per Sign row ({len(groups['card'])}) with the company's name in the title | To Do list {TODO_LIST} on board {BOARD} | — | trello_create_card | {IDS['msg']['esg_ack']} |")
A(f"| D4 ESG intake emails | one email per agreement ESG must review ({len(groups['esg'])}), with the checklist's items | ESG Law intake, Contacts {ESG_INTAKE} (PERSON_2599_EMAIL) | ESG Law intake | gmail_send_message | {IDS['msg']['esg_note']}, {I['esg_checklist_doc']} |")
A(f"| D5 contacts | a contact for each company's person not already in Contacts ({len(groups['contact_add'])}), company in the job field | Contacts | — | contacts_add_new_contact | {HUB_MSG}, {I['readme_doc']} 'Contacts' |")
A(f"| D6 January reminders | a reminder on the January review date for each parked company and each 'later' answer ({len(groups['revisit'])} companies) | Frederick's calendar ({FRED}) on Mon Jan 5, 2026 ({I['review_event']}) | — | gcal_create_event | {I['guardrails_doc']} steps 1 and 5, {I['review_event']} |")
A(f"| D7 report to Leonard | what we're keeping (Keep rows) and what's waiting on Arthur or Leonard to sign (Sign rows) | reply on the hub thread {I['hub_thread']} | leonard.hayes@harmonygames.co (reply or reply-all) | gmail_reply_to_message | {HUB_MSG} |")
A("")
A("Alternatives a careful run could defend, and how each is settled:")
A(f"- D1 destination: created in the folder or created elsewhere and moved there (both end in {I['q4_folder']}); a tab name other than the template's 'Log' is representational.")
A(f"- D2 Clipforge: the cancellation must go to billing@paylane.io (notice {IDS['msg']['clipforge_notice']}: 'write to billing@paylane.io by Oct 15'; 'This mailbox isn't monitored'); Priya also gets a written answer on her thread ({IDS['threads']['Clipforge']}): her Sep 22 mail asks 'If you're not carrying on after the pilot, let me know here too' (rev4; the rev3 /prompt review read it the same way, its F5).")
A(f"- D2 reply vs new email to the same person: both are a written answer to that company (the guardrails ask for an answer, not a channel); Reviewly's cancellation may be the written reply to Hana ({IDS['papers']['Reviewly']}: 'by email to your onboarding contact').")
A(f"- D2 Orbit Store: acceptance is in the partner portal, but Mateo writes personally and nudged on Sep 30 ({IDS['threads']['Orbit Store']}) — a written answer is owed; the 'Portals and no-reply notices' line covers Nintendo's portal mails ({BASE['nintendo_ndareq']}) and the Paylane notice only.")
A(f"- D6 form: one event per company on the January review day, as 04_Prompt.txt asks ('one per company'); a single event listing the companies does not follow the prompt; the time of day is representational (the review itself is {I['review_event']}).")
A(f"- D7 reply vs reply-all on {I['hub_thread']}: both reach Leonard; extra lines (what ended, what parked) are allowed.")
A(f"- Who sends: every write is the agent's on Frederick's behalf (the hub {HUB_MSG} is addressed to Frederick; no 'I'll' split).")
A("")
A("### 4b · Canonical outcome (all fair outcomes)")
A("")
A("| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by | Allowed equivalence class | Material / representational |")
A("|---|---|---|---|---|---|")
A(f"| D1 | location | final parent {I['q4_folder']} | — | created there or moved there | material |")
A(f"| D1 | name | 'Q4 commitments log' ({I['readme_doc']}) | — | any name carrying commitments, Q4, vendor or partner | representational |")
A(f"| D1 | header | Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date ({I['template_sheet']}) | — | same seven names, same order | material |")
A(f"| D1 | membership | exactly these {len(IN)} (scope: {HUB_MSG}): {', '.join(sorted(IN))} | — | record spelling or obvious short forms (Lanternfly, Pixel Harbor, Streamcast, Orbit, Nintendo / Nintendo Developer Portal) | material |")
A(f"| D1 | excluded | {', '.join(sorted(OUT))}; PlayableX and Craftsman+ (named in {HUB_MSG}); every cold pitch nobody answered | — | absent | material |")
for cls in ("Answered", "End", "Keep", "Sign", "Park"):
    A(f"| D1 | Decision = {cls} | {', '.join(sorted(by_class[cls]))} (rules: {I['guardrails_doc']}) | — | the README's word ({cls}) | material |")
A(f"| D1 | Answered by | Lanternfly Publishing = Leonard (D05S58U4SAK/1759174260.052645); Balancy = Leonard ({BASE['balancy_thread']}); Motive Forge = Arthur ({I['motive_thread']}); Spotlight Fest = Robert (C07C2866011/1758134460.899858, evt_564a16d0f5f6598d0360d5); blank on every other row | — | first name or full name | material |")
nd = collections.defaultdict(list)
for k in IN:
    nd[TRUTH[k].get("Next date")].append(k)
for d in sorted(nd, key=lambda x: (x is None, x or "")):
    A(f"| D1 | Next date = {dname(d)} | {', '.join(sorted(nd[d]))} (definitions: {I['readme_doc']}) | — | {'any date form for the same day' if d else 'blank, or a dash / n/a'} | material |")
A(f"| D1 | What we told them | free text consistent with the decision ({I['guardrails_doc']}); Pixel Harbor Events, Soundvault and Wishwave: declined / said no; Lanternfly Publishing: what Leonard told them in the DM (Southeast Asia waits until after the raise; January); Kinetic Arcade: with counsel (ESG) | — | any wording carrying that meaning | material for those five rows, representational elsewhere |")
A(f"| D1 | Contact, What's waiting | the company's person (from its thread) and the thing waiting (from its paper in {IDS['paperwork_folder']}); Nintendo: blank or the portal | — | any wording | representational |")
A(f"| D2 | recipients ({HUB_MSG}) | the {len(groups['written_answer'])} companies whose decision is End, Keep, Sign (not Nintendo) or Park; no new answer to Lanternfly Publishing, Balancy, Motive Forge, Spotlight Fest (already answered) | — | reply on the thread or new mail to the same person | material |")
A(f"| D2 | Clipforge cancellation | in writing to billing@paylane.io by Oct 15 ({IDS['msg']['clipforge_notice']}) | — | gmail send (to the address) plus a written answer to Priya on her thread (her Sep 22 ask) | material (both writes) |")
A(f"| D2 | content ({I['guardrails_doc']}) | End: no / cancel; Keep: staying; Sign: with Leonard or Arthur (counsel first for Kinetic Arcade, Lumencloud, Bundlehouse); Park: picking it up in January | 'Everyone who is waiting to hear from us should get a written answer' (hub); Sign: 'Tell them it's with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it' (guardrails step 4) | any polite wording | representational beyond the decision |")
A(f"| D3 | cards | {', '.join(sorted(groups['card']))}: company name in the card title, on list {TODO_LIST} | 'put it on our founders' board To Do list with the company's name in the card title' ({IDS['msg']['esg_ack']}) | any title that names the company | material (list and title) |")
A(f"| D4 | ESG emails | one each for {', '.join(sorted(groups['esg']))} to PERSON_2599_EMAIL (Contacts {ESG_INTAKE}) | 'one email per agreement' ({IDS['msg']['esg_note']}) | checklist items in any order; signer 'Leonard or Arthur' or either name | material (recipient, one per agreement) |")
A(f"| D1 | when answered (Answered rows, in What we told them or Answered by) | Lanternfly Publishing Sat Sep 27 (DM: 'on Saturday'); Balancy Thu Sep 11 PT (Sep 12 UTC); Motive Forge Fri Sep 19; Spotlight Fest Wed Sep 17 | 'Note who answered and when' ({I['guardrails_doc']}) | Pacific or UTC date | representational |")
A(f"| D5 | contacts | the company's person for every in-scope company except Kinetic Arcade, Lumencloud, Markward (already in Contacts) and Nintendo (no person); job = the company | 'only add a person who isn't in Contacts already (portals and no-reply senders don't get one)' ({I['readme_doc']}) | name as written in the thread (Balancy: PERSON_0527_NAME, or the name in his signature's booking link) | material (who, job) |")
A(f"| D6 | reminders | {', '.join(sorted(groups['revisit']))} on Mon Jan 5, 2026 ({I['review_event']}) | — | one event per company, as 04_Prompt.txt asks ('one per company'), any time that day; title or description names the company | material (date, companies, one each) |")
A(f"| D7 | report | keeping: {', '.join(sorted(by_class['Keep']))}; waiting on Arthur or Leonard to sign: {', '.join(sorted(by_class['Sign']))} | 'reply here with what we're keeping and what's waiting on Arthur or me to sign' ({HUB_MSG}) | lists in any order; extra context allowed | material (both lists complete) |")
A("")

# ---------------------------------------------------------------- 5
FACT = {
    "F1": ("hub ask", "scope, exclusions (ad networks, PlayableX, Craftsman+, Singular, investors, Mattel), guardrails + Monday change, ESG's note, written answers this week, Contacts, log in the Q4 folder per README, reply with keep + sign lists", HUB_MSG, "YES (To, INBOX)", "met first", "none", "Yes: Leonard's vendor and partner email (anchor A1)"),
    "F2": ("runway guardrails doc", "5 ordered steps; answers rule", I["guardrails_doc"], "YES (shared)", "met second (named by the hub); overturned in part by F13 (travel)", "first-framing latch on F3", "No"),
    "F3": ("UA spend buckets doc (decoy)", "UA spend only (team scope)", I["ua_buckets_doc"], "YES (owner)", "met first by a 'buckets' / 'UA' search", "decoy", "No"),
    "F4": ("ESG's signing note", "officer accepts; ESG review triggers; one email per agreement", IDS["msg"]["esg_note"], "YES (cc)", "named by the hub; overturns F12", "stops at the note, misses the reply below it", "No"),
    "F5": ("ESG intake checklist", "six items for each intake email", I["esg_checklist_doc"], "YES (shared)", "named by Leonard's ack " + IDS["msg"]["esg_ack"], "—", "No"),
    "F6": ("ESG Law intake contact", "PERSON_2599_EMAIL", I["esg_intake_contact"], "YES (unscoped)", "named by F4", "—", "No"),
    "F7": ("Q4 commitments folder", "Frederick's folder, holds README + template", I["q4_folder"], "YES (owner)", "named by the hub", "—", "Yes: my Q4 commitments folder (anchor A2)"),
    "F8": ("README", "sheet name, columns, Next date definitions, Contacts rule", I["readme_doc"], "YES (shared)", "named by the hub", "—", "No"),
    "F9": ("template sheet", "the header row", I["template_sheet"], "YES (shared)", "named by F8", "—", "No"),
    "F10": ("keep-running card", "Arthur's list, Doing", I["keep_card"], "YES (unscoped)", "named by F2 step 3; decoy base card " + BASE["browserstack_card"], "—", "No"),
    "F11": ("night pager item", "'the night pager for backend outages' = Pingwise by function", IDS["keep_items"][2], "YES (unscoped)", "overturns Pingwise's End reading", "join by function, not name", "No"),
    "F12": ("Leonard's July signing note", "Frederick may accept small terms himself", I["july_sign_note"], "YES (member)", "met first; overturned by F4 + ack", "stops at the first Slack hit", "No"),
    "F13": ("the Monday change", "travel counts as cash even when a partner books", I["amendment_root"], "YES (member)", "overturns F2's travel clause", "hub names it only by day and channel", "No"),
    "F14": ("Framewell waiver (thread reply)", "Maren: the Pro plan at no charge until Feb 1, nothing to sign before then", I["framewell_waiver_reply"], "YES (member)", "overturns the order form " + IDS["papers"]["Framewell"], "reply under another vendor's root, names the contact (Maren) not the company; history shows roots only", "No"),
    "F15": ("Playtestcloud root", "Leonard, Sep 21 PT; container of F14", BASE["playtestcloud_root"], "YES (member)", "container", "—", "No"),
    "F16": ("Leonard's DM thread reply on Lanternfly", "rang Wen back Sat Sep 27 about their Southeast Asia deal; Southeast Asia waits until after the raise; January", I["lanternfly_dm"], "YES (DM member)", "overturns Wen's open follow-up", "a reply under Leonard's Sep 17 DM root (history shows roots only); names Wen, not the company", "No"),
    "F17": ("Robert's cancel-all post", "a non-authoritative instruction", I["robert_cancel_all"], "YES (member)", "distractor", "sounds like a decision", "No"),
    "F18": ("Robert's Spotlight note", "had the call about the Dec 5 indie showcase; sitting this one out; let Rina know", IDS["spotlight_note"], "YES (member)", "settles Spotlight answered by Robert", "names the showcase and Rina, not the fest", "No"),
    "F19": ("ZOM-567 + Arthur's comment", "officer must accept the Global ToS and NDA by Oct 15; no fee/exclusivity/IP; kits wait", "ZOM-567, " + I["zom567_cmt"], "YES (unscoped)", "overturns F20/F21's 'done'", "comments need their own read", "No"),
    "F20": ("Nintendo portal mails", "ToS & NDA acceptance required; Registration Completed (NDA Effective 09/04)", f"{BASE['nintendo_ndareq']}, {BASE['nintendo_regdone']}", "YES (To)", "met first", "stops at 'Completed'", "No"),
    "F21": ("Frederick's Nintendo post", "'I registered an account'", BASE["fred_nintendo_post"], "YES (member)", "met first", "—", "No"),
    "F22": ("Paylane notice (workspace HG-2291)", "pilot ends Oct 15; $1,800/month from Oct 16; cancel to billing@paylane.io", IDS["msg"]["clipforge_notice"], "YES (To)", "overturns the pilot agreement and the July tracker", "names no company", "No"),
    "F23": ("Clipforge thread + pilot agreement", "workspace HG-2291; free through Jan 15 unless the cap is reached", f"{I['clipforge_thread']}, {IDS['papers']['Clipforge']}", "YES (To; owner)", "met first", "—", "No"),
    "F24": ("UGC Studio kickoff", "joins HG-2291 to Clipforge (Priya)", I["clipforge_kickoff"], "YES (own calendar)", "join", "—", "No"),
    "F25": ("July vendor tracker", "stale summary (Jul 31)", I["tracker_sheet"], "YES (owner)", "met first; overturned by F22 for Clipforge", "stale", "No"),
    "F26": ("Pixel Harbor booth quote (June)", "deposit $2,400 by Oct 10", f"{I['pixel_thread']}, {IDS['papers']['Pixel Harbor Events']}", "YES (To; owner)", "outside a September search window", "date-filtered search misses it", "No"),
    "F27": ("January review event", "Mon Jan 5, 2026 17:00Z", I["review_event"], "YES (own copy)", "dates the January review", "—", "No"),
    "F28": ("Spotlight call event", "Sep 17, Robert organizer; description 'Showcase slot call with Rina.' (no answer)", I["spotlight_call"], "YES (own copy)", "supporting (dates the call)", "—", "No"),
    "F29": ("Balancy thread", "Leonard's Sep 11 'circle back' answer", BASE["balancy_thread"], "YES (cc)", "settles Answered by Leonard, later", "—", "No"),
    "F30": ("Rayking forward", "Frederick's 'reply' went to Leonard", BASE["rayking_thread"], "YES (own)", "boundary", "looks engaged", "No"),
    "F31": ("Playable Factory", "cold pitch nobody answered", BASE["playable_factory_thread"], "YES (To)", "boundary", "unanswered follow-up", "No"),
    "F32": ("Nova Rewards", "offer withdrawn Sep 23", I["nova_thread"], "YES (To)", "boundary", "—", "No"),
    "F33": ("paperwork folder", "Frederick's filed copies of the papers", IDS["paperwork_folder"], "YES (owner)", "container", "—", "No"),
    "F34": ("Motive Forge thread", "Arthur's plain no (Sep 19)", I["motive_thread"], "YES (To/cc)", "settles Answered by Arthur", "—", "No"),
    "F35": ("Spotlight Fest thread", "invitation + paper ($750 stand fee)", I["spotlight_thread"], "YES (To)", "met first; settled by F18", "—", "No"),
}
A("## 5 · Discovery map")
A("")
A("Root causes and corrections appear only here and are never in the prompt.")
A("")
A("| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |")
A("|---|---|---|---|---|---|---|")
for fid in [f"F{i}" for i in range(1, 36)]:
    f = FACT[fid]
    A(f"| {fid} {f[0]} | {f[1]} | {f[2]} | {f[3]} | {f[4]} | {f[5]} | {f[6]} |")
for fid, r in SRCH.items():
    if not fid.startswith("C:"):
        continue
    k = fid[2:]
    m, t = M[k], TRUTH[k]
    loc = ", ".join(x for x in (IDS["threads"].get(k), IDS["papers"].get(k)) if x)
    A(f"| {fid} {k} | {m['kind']}: {t['Decision']}, next date {t['Next date'] or 'blank'} | {loc} | YES (To; paper owned) | per-company paper + thread | {'no company name in the mail (tokenized sender): joined through the paper' if r['service'] == 'gdocs' else 'one of 36 threads'} | No |")
A("")

# ---------------------------------------------------------------- 5a
A("## 5a · Search-as-persona proof")
A("")
A("`persona_view.py search` reads the base only; seeded hits are counted from the SQL rows Frederick can see (the same "
  "rows check-sql proves visible). One row per §5 fact.")
A("")
A("| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |")
A("|---|---|---|---|---|---|---|")
for fid, r in SRCH.items():
    label = FACT[fid][0] if fid in FACT else fid[2:]
    A(f"| {fid} {label} | {r['service']} | \"{r['query']}\" | base {r['base']}; seeded {r['seeded']} | {r['hidden']} | {r['first']} | {r['found']} |")
A("")
A("Pasted `persona_view.py search` outputs (verbatim, every query above):")
A("")
A("```")
A(rd("brief_searches.txt"))
A("```")
A("")

# ---------------------------------------------------------------- 6
A("## 6 · Triggers, incorporation and implicit requirements")
A("")
A("| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |")
A("|---|---|---|---|---|")
rows6 = [
    ("R1 log population (scope + exclusions)", HUB_MSG, "deliverable: the log Leonard asked for", f"{HUB_MSG} · YES · 'Leonard's vendor and partner email' is the only one · states the scope rule, not the list"),
    ("R2 decisions (cash test, Park, Monday change)", f"{I['guardrails_doc']}, {I['amendment_root']}", "scope: do what Leonard's email says", f"{HUB_MSG} → '{B.Q['hub_guardrails']}, {B.Q['hub_amend']}' · YES · unique doc and post · rules, no decisions"),
    ("R3 keep-running exemption", f"{I['guardrails_doc']} step 3, {I['keep_card']}", "same", f"{I['guardrails_doc']} names 'Arthur's keep-running list on our board' · YES · one card · a list, not the answer"),
    ("R4 already answered (who, later)", f"{I['guardrails_doc']} step 1", "same", f"{I['guardrails_doc']} · YES · · rule only"),
    ("R5 written answers", HUB_MSG, "same", f"{HUB_MSG} '{B.Q['hub_answer']}' · YES · · instruction"),
    ("R6 signatures: cards + ESG intake", f"{IDS['msg']['esg_note']}, {IDS['msg']['esg_ack']}", "same", f"{HUB_MSG} '{B.Q['hub_esg']}' → the ESG thread {I['esg_thread']} (note + Leonard's reply) · YES · one thread · rules"),
    ("R7 January reminders on Frederick's calendar", f"{I['guardrails_doc']} (the review), {I['review_event']}", "deliverable: the prompt must ask for the reminders (no record asks Frederick to make them)", "the prompt itself (gotcha otherwise: the guardrails only say parked items come back at the review Leonard puts on the calendars)"),
    ("R8 contacts", f"{HUB_MSG}, {I['readme_doc']}", "same", f"{HUB_MSG} '{B.Q['hub_contacts']}' + README 'Contacts' · YES · · instruction"),
    ("R9 log location and columns", f"{I['q4_folder']}, {I['readme_doc']}", "destination: my Q4 commitments folder", f"{HUB_MSG} 'Log it all in a sheet in the Q4 commitments folder, {B.Q['hub_readme']}' · YES · one folder · columns, not values"),
    ("R10 reply on the hub", HUB_MSG, "deliverable: the reply Leonard asked for", f"{HUB_MSG} '{B.Q['hub_report']}' · YES · · instruction"),
]
for r in rows6:
    inf = "gotcha → needs the prompt trigger" if r[0].startswith("R7") else "yes (incorporated through the hub)"
    A(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {inf} |")
A("")
A("| Anchor | May be named (noun phrases only) | Record |")
A("|---|---|---|")
A(f"| A1 | Leonard's vendor and partner email; Leonard's email from yesterday | {I['hub_thread']} |")
A(f"| A2 | my Q4 commitments folder; the Q4 commitments folder | {I['q4_folder']} |")
A(f"| A3 | the Harmony Games board; our Harmony Games board | {BOARD} |")
A(f"| A4 | the January commitments review; the January review | {I['review_event']} |")
A("")
A(f"A3 pins 'our founders' board' ({IDS['msg']['esg_ack']}): five boards exist and none is titled 'founders' (Welcome Board 535af5816ca07f261e8cd420 closed, Harmony Games {BOARD}, DD Product Roadmap 65eb4ec525346c8070ca638f, UA/BD 66da196af476ab78deaa0cef, ZM ROADMAP 6851a6569f3bf818760632ab); the keep-running card sits on {BOARD}. A4 is the destination date of R7 (named in the guardrails; the prompt may refer to it).")
A("")

# ---------------------------------------------------------------- 7
A("## 7 · Dates and constraints")
A("")
A("| Item | Absolute date or value | Source | Past fact or deadline |")
A("|---|---|---|---|")
for item, val, src, kind in [
    ("Frederick's today", "Wed Oct 1, 2025 (clock 2025-10-01 00:00 PT / 07:00 UTC)", f"00_Task_Context.json universe.persona_today; the day after {HUB_MSG}", "now"),
    ("Leonard's email", "Tue Sep 30, 2025 23:20Z (4:20 PM PT)", HUB_MSG, "past"),
    ("'this week' for the written answers", "the week of Mon Sep 29 – Sun Oct 5, 2025 (Frederick's Oct 1–3 working days)", HUB_MSG, "deadline"),
    ("the Monday change", "Mon Sep 29, 2025 17:15Z", I["amendment_root"], "past"),
    ("guardrails doc", "Fri Sep 26, 2025", I["guardrails_doc"], "past"),
    ("ESG note / Leonard's reply", "Wed Sep 24 20:05Z / Thu Sep 25 16:30Z, 2025", f"{IDS['msg']['esg_note']}, {IDS['msg']['esg_ack']}", "past"),
    ("README", "Tue Sep 30, 2025 22:40Z", I["readme_doc"], "past"),
    ("January review", "Mon Jan 5, 2026 17:00–17:45Z (9:00 AM PT)", I["review_event"], "future plan field"),
    ("Brightlane, Ascendo confirm-by", "Wed Oct 1, 2025", f"{IDS['threads']['Brightlane Studio']}, {IDS['threads']['Ascendo']}", "deadline"),
    ("Lingora quote", "Fri Oct 3, 2025", IDS["papers"]["Lingora"], "deadline"),
    ("Panelpulse confirm-by", "Mon Oct 6, 2025", IDS["papers"]["Panelpulse"], "deadline"),
    ("Playfuse NDA", "by Wed Oct 8, 2025", IDS["papers"]["Playfuse"], "deadline"),
    ("Pixel Harbor deposit", "Fri Oct 10, 2025", IDS["papers"]["Pixel Harbor Events"], "deadline"),
    ("Vaultline renewal", "Sun Oct 12, 2025", IDS["papers"]["Vaultline"], "deadline"),
    ("Clipforge cancel-by / Soundvault quote / Nintendo acceptance", "Wed Oct 15, 2025", f"{IDS['msg']['clipforge_notice']}, {IDS['papers']['Soundvault']}, {I['zom567_cmt']}", "deadline"),
    ("Wishwave confirm-by", "Fri Oct 17, 2025", IDS["papers"]["Wishwave"], "deadline"),
    ("Reviewly cancel-by", "Sun Oct 19, 2025", IDS["papers"]["Reviewly"], "deadline"),
    ("Certwell renewal / Kinetic Arcade signature", "Mon Oct 20, 2025", f"{IDS['papers']['Certwell']}, {IDS['papers']['Kinetic Arcade']}", "deadline"),
    ("Orbit Store acceptance", "Fri Oct 24, 2025", IDS["papers"]["Orbit Store"], "deadline"),
    ("Streamcast book-by / Lumencloud apply-by", "Fri Oct 31, 2025", f"{IDS['papers']['Streamcast Talent']}, {IDS['papers']['Lumencloud']}", "deadline"),
    ("Pingwise bills / Bundlehouse signature", "Sat Nov 1, 2025", f"{IDS['papers']['Pingwise']}, {IDS['papers']['Bundlehouse']}", "deadline"),
]:
    A(f"| {item} | {val} | {src} | {kind} |")
A("")

# ---------------------------------------------------------------- 8
A("## 8 · Difficulty levers")
A("")
A("| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |")
A("|---|---|---|---|---|")
A(f"| Ambiguity | yes | yes | the deciding facts sit in a Slack thread reply ({I['framewell_waiver_reply']}), a DM ({I['lanternfly_dm']}), a Linear comment ({I['zom567_cmt']}), a Trello checklist item ({IDS['keep_items'][2]}), a notice naming no company ({IDS['msg']['clipforge_notice']}) and a June thread ({I['pixel_thread']}) | the prompt is clear about the job and vague about where the answers live; it names only the hub, the folder, the board and the January review |")
A(f"| Dynamic change | yes | yes | superseded claims met first: the order form, the pilot agreement/tracker, the July note, the guardrails' travel clause, the portal's 'Completed' (T1, T2, T5, T7, T9) | the prompt gives no reason beyond Leonard's email and names neither the first summary nor the correction |")
A("| Multi-source | yes | yes | 10 services (Gmail, Drive, Docs, Sheets, Slides, Slack, Trello, Linear, Calendar, Contacts) | no source named as an exact artifact beyond the anchors |")
A("| Async | no | — | — | no wait configured (03_Error_Async_Config.txt: Friction: none) |")
A("| Error recovery | no | — | — | no forced error |")
A("| Access control | no | — | — | every deciding record is Frederick-visible (§5a) |")
A("")

# ---------------------------------------------------------------- 9
A("## 9 · Must not appear in the prompt")
A("")
A("- Tool and server names (`Evals/references/tools/catalog.json`): gmail_search_messages, gmail_get_thread, gmail_reply_to_message, gmail_send_message, gdrive_search, gdrive_move_file, gdocs_get_document, gsheets_create_spreadsheet, gsheets_values_update, gslides_get_presentation, slack_conversations_search_messages, slack_read_thread, trello_get_checklists_on_board, trello_create_card, linear_list_comments, gcal_list_events, gcal_create_event, contacts_search_contacts, contacts_add_new_contact, and every other catalog name; no MCP server name, no 'the X tool'.")
A(f"- Ids and opaque names: any f_/d_/evt_ id, thread or message id, Slack channel id or ts, ZOM-567, card or list ids, HG-2291, billing@paylane.io, PERSON_ tokens.")
A("- Root causes and findings (from §5): Leonard's DM about Lanternfly, his reply under the Playtestcloud post, Arthur's ZOM-567 comment, the keep-running card and its night-pager item, the Paylane notice, Pixel Harbor's June quote, the Monday travel change, ESG's reply superseding the July note, Robert's Spotlight note.")
A("- The rules themselves: the guardrails' steps, the README's columns and Next date definitions, ESG's triggers, the checklist, the scope and exclusion list (PlayableX, Craftsman+, ad networks, Singular, Mattel).")
A("- Any company name, decision, date, amount or count (36 rows, 31 answers, 7 cards, 3 ESG emails, 32 contacts, 14 reminders).")
A("- 'While I'm in LA' / 'before LA' framing (dataset-duplicate risk: memory prompt-dataset-duplicate-gate).")
A("- Markdown, numbered steps, per-deliverable content lists or format rules (they belong in the README and the guardrails).")
A("")

# ---------------------------------------------------------------- 10
A("## 10 · Entity traps")
A("")
A("```")
A(rd("entity_brief.txt"))
A("```")
A("")
A("| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |")
A("|---|---|---|---|")
A("| Leonard Hayes | Leonard's Gmail files are named leonard@ | one person | leonard.hayes@harmonygames.co |")
A("| Arthur Blake | blake@ file alias; Trello 'Keep-running' author | one person | arthur.blake@harmonygames.co |")
A("| Robert | no surname in any service | one person | robert@harmonygames.co |")
A(f"| Frederick Stone | GitHub display name 'Ryan' (S04); frederick@ file alias | GitHub not used | {FRED} |")
A(f"| Harmony Games board (founders') | DD Product Roadmap, UA/BD, ZM ROADMAP, closed Welcome Board; several 'To Do' lists | the keep-running card's board | {BOARD} (list {TODO_LIST}) |")
A(f"| runway guardrails doc | UA spend buckets doc | scope: vendors vs UA spend | {I['guardrails_doc']} vs {I['ua_buckets_doc']} |")
A(f"| Clipforge | Paylane (payments partner), UGC Studio (product), HG-2291 (workspace) | one company, one row | {I['clipforge_thread']}, {IDS['msg']['clipforge_notice']} |")
A(f"| Lanternfly Publishing | 'Lanternfly' short form | one company | {IDS['threads']['Lanternfly Publishing']} |")
A(f"| Playable Factory, PlayableX | both playable-ad vendors | both off the log (cold pitch; named exclusion) | {BASE['playable_factory_thread']}; C08H78VJG80 |")
A("")

# ---------------------------------------------------------------- 11
A("## 11 · Pre-submit checklist")
A("")
for box in [
    "Persona voice: an ordinary request from Frederick to his assistant; clean spelling; no spec-sheet layout",
    "Names Leonard's vendor and partner email (A1) as the source of the job, not its rules",
    "Names my Q4 commitments folder (A2) for the log, the Harmony Games board (A3) for the cards, and asks for reminders for the January review (A4, R7 trigger)",
    "Asks for the reply on Leonard's thread when done (R10)",
    "No company name, decision, count, date, amount, rule, id or tool name (§9)",
    "No hint, riddle, hedge, if-chain or audit-form wording; no 'while I'm in LA' framing",
    "Every deliverable in §4 is reachable from the prompt or Leonard's email",
    "hardness_v2_check RULE_IN_PROMPT clean; word count 20–4,000",
]:
    A(f"- [ ] {box}")
A("")

# ---------------------------------------------------------------- 12
A("## 12 · Blockers and routed defects")
A("")
A("- Routed to `/create-injection` and done in this stage: rev3 (`run_forensics/rev3/01_Universe_Inject.sql`) settles every fork the first blind sweep left open (`plan/blind_fork_sweep.md`; list in the dossier's 'Rev3' section). The platform /injection review must pass rev3 before /prompt.")
A("- Second blind sweep on rev3 (`plan/blind_fork_sweep_rev3.md`): independent log identical to the solver (36 rows); its 5 open forks are representational and accepted in §4b, and the Sign-answer gap is settled in the guardrails (final rev3 build).")
A("- Rev4 (after the rev3 Opus pre-check, `01a_Hardening_Report.md`): the Framewell, Lanternfly and Spotlight corrections no longer name their companies (Maren, Wen, the Dec 5 indie showcase and Rina), the Lanternfly answer is a DM thread reply, and Hootline sits outside the inbox-window/folder filter. A third blind sweep on rev4 (`plan/blind_fork_sweep_rev4.md`) matched the solver row for row (36 rows) and tied every alias to one company; its three material forks (Lanternfly told, a written answer to Priya, no Nintendo contact) were settled in records in the final rev4 build. The platform /injection review must pass rev4 before /prompt.")
A("- R7 needs the prompt trigger (no record asks Frederick to create reminders).")
A("- Unverified: none load-bearing (rev4 removed the answer from the Spotlight call's description; Robert's Slack note is the only carrier).")
A("")

A("## 13 · Self-review")
A("")
A("Re-read as Eval 1 Phases 1–3 against this brief (brief mode). Every load-bearing value above was re-read from the rev4 SQL or through `tools/hg.py` in this run (§5a outputs, `plan/record_dump_*.md`, check-sql in the dossier). Three independent blind fork sweeps read only Frederick-visible records (no solver, manifest or surface): the first (`plan/blind_fork_sweep.md`, 41 forks, 18 unsettled) drove rev3; the second (`plan/blind_fork_sweep_rev3.md`, 46 forks, 5 unsettled — all representational and accepted in §4b, one settled in the guardrails) produced the solver's 36 rows, classes, cards, ESG emails, reminders and contacts exactly.")
A("")
A("| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |")
A("|---|---|---|---|")
CR = [
    ("Fair readings (UGT)", "Log membership is graded exactly; a careful run could add PlayableX or Craftsman+ (UA vendors Frederick engaged with) or drop Nintendo and Balancy (base-only records)", f"the rev3 hub {HUB_MSG} names PlayableX and Craftsman+ in the UA exclusion; Nintendo's terms wait on an officer (cmt_c9a6660d81e067ad1de7), Balancy was engaged and answered later ({BASE['balancy_thread']}); the second blind sweep listed the same 36 rows", "holds"),
    ("Fair readings (UGT)", "the rev4 de-named corrections (Maren, Wen, the Dec 5 indie showcase and Rina) could tie to another company", f"each name signs its own company's thread (Framewell {IDS['threads']['Framewell']}, Lanternfly {IDS['threads']['Lanternfly Publishing']}, Spotlight Fest {I['spotlight_thread']}); the rev4 blind sweep (plan/blind_fork_sweep_rev4.md) tied each to exactly one company", "holds"),
    ("Fair readings (UGT)", "Framewell could be Sign (it sent an order form) and the pay-when-you-order quotes could be End", f"Leonard's reply {I['framewell_waiver_reply']}: 'with nothing to sign before then'; the guardrails {I['guardrails_doc']}: an offer we would have to take up and pay for before January counts as cash, Park covers offers we could still take up after that", "holds"),
    ("Fair readings (UGT)", "Motive Forge's and Spotlight Fest's answers could be 'later' answers (January reminder, Jan 5 next date)", f"Arthur's reply in {I['motive_thread']}: 'we'll pass on this one'; Robert's note {IDS['spotlight_note']}: 'we're sitting this one out this year, I let Rina know' — plain noes", "holds"),
    ("Clarity", "The reminders could be one event or fourteen, and the cards could land on another board's To Do list", "04_Prompt.txt settles the form ('put a reminder on my calendar for that day, one per company'; §4b D6) and names the Harmony Games board (A3, " + BOARD + ") — five boards exist and none is titled 'founders'", "holds"),
    ("Incorporation", "R7 (January reminders) is graded but no record asks Frederick to create them, so a criterion on it would be unauthorized", f"§6 routes R7 to the prompt as a deliverable trigger; the date comes from {I['review_event']} named by the guardrails", "holds only with the trigger in 04_Prompt.txt"),
    ("Incorporation", "The hub points at 'ESG's note', but the card instruction is Leonard's reply under it, not ESG's words", f"the reply {IDS['msg']['esg_ack']} is Leonard's own instruction to Fred and Arthur in the thread the hub names ({I['esg_thread']}); both sweeps followed it to 7 cards on the board", "holds"),
    ("Truthfulness", "A prompt premise such as 'Leonard emailed yesterday' or 'he's in LA' could be off", f"the hub is Tue Sep 30 23:20Z = 4:20 PM PT, the persona's yesterday (Wed Oct 1 today); 'in LA from tomorrow' is Leonard's own claim in {HUB_MSG} (and base C07C2866011/1758739727.864319) — the prompt should still avoid the LA framing (duplicate risk, §9)", "holds"),
    ("Feasibility / ACL", "A deciding record could sit outside Frederick's view (another mailbox, a private channel)", "check-sql PASS on 168 load-bearing ids (dossier 1.E); §5a: 65 of 65 facts found by a natural search as frederick_stone; nine counterparties name their company only on the Drive paper, found by a Docs search", "holds"),
    ("Feasibility / ACL", "Mails say 'attached' but attachment bytes never reach the agent", f"each paper is Frederick's filed copy in {IDS['paperwork_folder']} (Docs/Slides, readable), created 10–15 minutes after its mail; no fact depends on an attachment", "holds"),
    ("Contrived register", "Naming the folder, the board and the January review in the prompt could read as hints or a spec sheet", "they are destinations the persona knows from records he received (hub, ESG reply, guardrails); no trap resolver, rule, company or count is named (§9); the asks stay in Leonard's email", "holds"),
]
for c in CR:
    A(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} |")
A("")
A("Unresolved: the ESG signer wording ('Leonard or Arthur' or either name) and the reminder time of day stay open by design (accepted both ways in §4b; rev4 sweep F36, F41). 04_Prompt.txt (drafted 2026-11-04) carries the R7 trigger and the board name; D6 is narrowed to one event per company to match it.")
A("")

out = os.path.join(WF, "04_Prompt_Writing_Brief.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, len(L), "lines")
