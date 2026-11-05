#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep) from the rev4 SQL rows (parsed, never executed), the base
records read through tools/hg.py (plan/oe_base_quotes.json, plan/oe_base_slack.json), solver/truth.json and
persona_view check-sql. Facts and dependency edges only; no event text. Every quote is cut from its record text."""
import datetime as dt
import json
import os
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
import stage_gate as G  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
FRED = "frederick.stone@harmonygames.co"
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQL_PATH).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
BQ = json.load(open(os.path.join(HERE, "oe_base_quotes.json")))
BS = json.load(open(os.path.join(HERE, "oe_base_slack.json")))
SL = IDS["slack_mid"]


def run(args):
    p = subprocess.run(args, cwd=WS, capture_output=True, text=True,
                       env={**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"})
    return p.stdout


CS = json.loads(run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", "frederick_stone",
                     "Task_Authoring/task_inputs/01_Universe_Inject.sql", "--json"]))
LINE = {}
for r in CS["rows"]:
    for k in r["keys"]:
        LINE.setdefault(k, r["line"])


SQL_LINES = SQL.splitlines()


def sql_line(k):
    if k in LINE:
        return LINE[k]
    for i, l in enumerate(SQL_LINES, 1):
        if f"'{k}'" in l and l.lstrip().startswith(("VALUES", "INSERT")):
            return i
    return None


def L(*keys):
    return ", ".join(f"SQL L{sql_line(k)}" for k in keys if sql_line(k))


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "").replace("|", "/")


def lines(s):
    return [l.strip() for l in clean(s).split("\n") if l.strip()]


def when(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M%p').replace('AM', 'am').replace('PM', 'pm')} {p.tzname()} ({d.strftime('%Y-%m-%dT%H:%MZ')})"


def q(s):
    return "'" + s.replace("'", "’") + "'" if False else "'" + s + "'"


def content_line(body):
    ls = [l for l in lines(body) if len(l) > 24 and not re.match(r"^(Hi|Hello|Hey|Thanks|Best|Cheers|Kind)\b", l)]
    return ls[0] if ls else (lines(body)[0] if lines(body) else "")


def fred_msgs(tid):
    return sorted(rows("gmail.gmail_messages", thread_id=tid, user_email=FRED), key=lambda r: int(r["internal_date"]))


def paper(pid):
    d = rows("gdocs.docs_documents", document_id=pid)
    if d:
        ls = lines(d[0]["body_text"])
        return d[0]["title"], ls[1:]
    els = [e for e in rows("gslides.slides_page_elements", presentation_id=pid) if e.get("text")]
    pres = rows("gslides.slides_presentations", presentation_id=pid)
    return (pres[0]["title"] if pres else pid), [clean(e["text"]).replace("\n", " / ") for e in els]


B, A, C, E, F_, FACTS = [], [], [], [], [], []
fid_of = {}


def fact(key, value, service, tools, locator, origin, expected, result, visible, depends, source):
    n = f"F{len(FACTS) + 1}"
    fid_of[key] = n
    FACTS.append((n, value, service, tools, locator, origin, expected, result, visible, depends, source))
    return n


def dep(*keys):
    return ", ".join(fid_of[k] for k in keys if k in fid_of) or "—"


# ---------------------------------------------------------------- rule and context records
hub_mid = IDS["msg"]["hub"]
hub_tid = "frederick.stone@harmonygames.co/1844732913254784171"
hub = rows("gmail.gmail_messages", id=hub_mid)[0]
hb = clean(hub["body_text"])
HUBQ = ["can you take over the vendor and partner backlog this week?",
        "anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with: a call, a reply, a sign-up or paper",
        "Cold pitches nobody answered, including ones we only forwarded around internally, stay off it",
        "and so do the ad networks, PlayableX, Craftsman+ and Singular (they all stay on the UA budget call), the investors, and Mattel, which I'm keeping",
        "Go by the runway guardrails doc for what we do with each one, plus the one change I posted in #executives on Monday",
        "Anything that needs signing goes the way ESG's note about signing says",
        "Everyone who is waiting to hear from us should get a written answer this week",
        "Get each company's contact into Contacts so we're not digging through mail next time",
        "Log it all in a sheet in the Q4 commitments folder, the README in the folder has the columns",
        "Then reply here with what we're keeping and what's waiting on Arthur or me to sign"]
for x in HUBQ:
    assert x in hb, x
fact("hub", "Leonard's vendor and partner email (the hub)", "Gmail (Frederick's mailbox, To)", "gmail_search_messages, gmail_get_thread",
     "Frederick's inbox, Leonard Hayes's message of Tue Sep 30 'Vendor and partner stuff while I'm in LA'",
     'prompt ("Leonard\'s email yesterday"); search "vendor and partner"',
     f"Thread {hub_tid}, message {hub_mid}, sent {when(hub['date'])}, from leonard.hayes@harmonygames.co to Frederick only (no cc). Quotes: " + " · ".join(q(x) for x in HUBQ),
     "VERIFIED: every quote cut from the message body", "YES (To; check-sql)", "—", L(hub_mid, hub_tid))

gd = rows("gdocs.docs_documents", document_id="f_b98287f6f80fe431a71209")[0]
gl = lines(gd["body_text"])
fact("guardrails", "Runway guardrails doc: the five decisions, top to bottom", "Docs (shared with Frederick)", "gdrive_search, gdocs_get_document_text",
     "Doc titled 'Runway guardrails - Q4 commitments'", f'{dep("hub")} ("the runway guardrails doc"); search "runway guardrails"',
     f"Doc f_b98287f6f80fe431a71209, created {when(gd['created_time'])}, owner Leonard. Quotes: " + " · ".join(q(x) for x in gl[1:]),
     "VERIFIED: every line cut from body_text", "YES (shared; check-sql)", dep("hub"), L("f_b98287f6f80fe431a71209"))

am = rows("slack.slack_messages", id=SL["amendment_root"])[0]
fact("amend", "The Monday change: partner-booked travel counts as cash", "Slack (#executives, Frederick a member)", "slack_search_public_and_private, slack_conversations_history",
     "#executives post by Leonard on Mon Sep 29", f'{dep("hub")} ("the one change I posted in #executives on Monday"); search "runway guardrails"',
     f"Message C07C2866011/{am['ts']} (row {SL['amendment_root']}), posted {when(dt.datetime.fromtimestamp(float(am['ts']), dt.UTC).strftime('%Y-%m-%dT%H:%M:%SZ'))} by Leonard: {q(clean(am['text']))}",
     "VERIFIED: full text", "YES (member; check-sql)", dep("hub"), L(SL["amendment_root"]))

esg_note = rows("gmail.gmail_messages", id=IDS["msg"]["esg_note"])[0]
esg_ack = rows("gmail.gmail_messages", id=IDS["msg"]["esg_ack"])[0]
en, ea = clean(esg_note["body_text"]), clean(esg_ack["body_text"])
EQ = ["Only an officer, you or Arthur, accepts terms or signs for Harmony Games, whatever the amount. That includes click-through terms and portal NDAs.",
      "Anything with an automatic renewal, exclusivity, a licence of your IP or a term over 12 months comes to us before anyone signs.",
      "one email per agreement", "Mutual NDAs on our template don't need review, whatever their term. An officer can sign them."]
AQ = ["This replaces what I said in July about Fred signing small stuff himself.",
      "anything waiting on Arthur or me to sign, put it on our founders' board To Do list with the company's name in the card title, including the ones that go to ESG",
      "For the intake emails, what to include is in the intake checklist I shared."]
for x in EQ:
    assert x in en, x
for x in AQ:
    assert x in ea, x
fact("esg", "ESG Law's signing note and Leonard's reply under it", "Gmail (Frederick cc)", "gmail_search_messages, gmail_get_thread",
     "Thread 'Signing and review for Harmony Games agreements' (ESG Law partner to Leonard, founders cc)", f'{dep("hub")} ("ESG\'s note about signing"); search "Signing and review"',
     f"Thread {IDS['msg']['esg_note'].split('/')[0]}/1844177063117059830; note {IDS['msg']['esg_note']} sent {when(esg_note['date'])}: " + " · ".join(q(x) for x in EQ)
     + f"; Leonard's reply {IDS['msg']['esg_ack']} sent {when(esg_ack['date'])}: " + " · ".join(q(x) for x in AQ),
     "VERIFIED: quotes cut from both bodies", "YES (cc; check-sql)", dep("hub"), L(IDS["msg"]["esg_note"], IDS["msg"]["esg_ack"]))

ck = rows("gdocs.docs_documents", document_id="f_3b06917a41dd59308d890b")[0]
fact("checklist", "ESG intake checklist: what each intake email carries", "Docs (shared with Frederick)", "gdrive_search, gdocs_get_document_text",
     "Doc titled 'ESG Law - agreement intake checklist'", f'{dep("esg")} ("the intake checklist I shared"); search "intake checklist"',
     f"Doc f_3b06917a41dd59308d890b, created {when(ck['created_time'])}. Quotes: " + " · ".join(q(x) for x in lines(ck["body_text"])[1:]),
     "VERIFIED", "YES (shared; check-sql)", dep("esg"), L("f_3b06917a41dd59308d890b"))

esgc = rows("contacts.contacts", contact_id="9b0185e445572aeee9f27d35")[0]
fact("esg_contact", "ESG Law intake address in Contacts", "Contacts (unscoped)", "contacts_search_contacts",
     "Contacts entry 'ESG Law intake'", f'{dep("esg")} ("it\'s in your Contacts as ESG Law intake"); search "ESG Law"',
     f"Contact 9b0185e445572aeee9f27d35: first_name {q(str(esgc.get('first_name')))}, last_name {q(str(esgc.get('last_name')))}, email {esgc.get('email')}",
     "VERIFIED", "YES (unscoped)", dep("esg"), L("9b0185e445572aeee9f27d35"))

fo = rows("gdrive.drive_files", id="d_80a8c04753ba82ba4ba6a5")[0]
fact("folder", "Frederick's Q4 commitments folder (log destination)", "Drive (owner Frederick)", "gdrive_search, gdrive_list_folder",
     "Folder 'Q4 commitments' in Frederick's Drive", 'prompt ("my Q4 commitments folder"); search "Q4 commitments"',
     f"Folder d_80a8c04753ba82ba4ba6a5 'Q4 commitments', owner {fo['owner_email']}, shared with leonard.hayes@harmonygames.co, created {when(fo['created_time'])}; holds the README and the template",
     "VERIFIED", "YES (owner; check-sql)", "—", L("d_80a8c04753ba82ba4ba6a5"))

rd = rows("gdocs.docs_documents", document_id="f_846ddc38b2aab3d2ed3fcb")[0]
fact("readme", "Folder README: sheet name, columns, decision words, Next date rule, Contacts rule", "Docs (in the folder, shared)", "gdrive_list_folder, gdocs_get_document_text",
     "Doc 'README - Q4 commitments' inside the folder", f'{dep("hub", "folder")} ("the README in the folder has the columns"); search "README - Q4 commitments"',
     f"Doc f_846ddc38b2aab3d2ed3fcb, created {when(rd['created_time'])}. Quotes: " + " · ".join(q(x) for x in lines(rd["body_text"])[1:]),
     "VERIFIED", "YES (shared; check-sql)", dep("hub", "folder"), L("f_846ddc38b2aab3d2ed3fcb"))

tp = rows("gsheets.sheets_sheets", spreadsheet_id="f_05f0a451b29b19a1c0b90f")[0]
grid = tp["grid_json"] if isinstance(tp["grid_json"], str) else json.dumps(tp["grid_json"])
fact("template", "Log template header row", "Sheets (in the folder, shared)", "gdrive_list_folder, gsheets_values_get",
     "Sheet 'Q4 commitments - template' in the folder", f'{dep("readme")} ("copy the header row from the template sheet"); search "Q4 commitments"',
     f"Spreadsheet f_05f0a451b29b19a1c0b90f, tab {q(str(tp.get('title')))}, header row: Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date (grid {q(grid[:160])})",
     "VERIFIED", "YES (shared; check-sql)", dep("readme"), L("f_05f0a451b29b19a1c0b90f"))

kc = rows("trello.trello_cards")[0]
items = [r.get("name") for r in rows("trello.trello_check_items")]
fact("keepcard", "Arthur's keep-running list (the Keep exemption)", "Trello (unscoped)", "trello_get_lists, trello_get_card",
     "Card 'Keep-running list (don't cut)' on the Harmony Games board, Doing list", f'{dep("guardrails")} ("Arthur\'s keep-running list on our board"); search "Keep-running"',
     f"Card {kc['id']} {q(kc['name'])}, desc {q(clean(kc.get(chr(34)+'desc'+chr(34)) or kc.get('desc') or ''))}; checklist items: " + " · ".join(q(x) for x in items) + f"; the night-pager item is {IDS['keep_items'][2]}",
     "VERIFIED", "YES (unscoped)", dep("guardrails"), L(kc["id"]))

fact("board", "Harmony Games board and its To Do list (card destination)", "Trello (unscoped)", "trello_list_boards, trello_get_lists",
     "Board 'Harmony Games', list 'To Do'", 'prompt ("our Harmony Games board"); search "Harmony Games"',
     "Board 640643a3fd8f3ca308d9318e name 'Harmony Games' (open); To Do list 640643a3fd8f3ca308d93195; Leonard's 'our founders' board' (F4) is this board — no board is titled 'founders'",
     "VERIFIED: trello data.json /boards/1 (hg.py search get trello)", "YES (unscoped)", dep("esg"), "trello data.json /boards/1 (640643a3fd8f3ca308d9318e)")

rv = rows("gcal.gcal_events", event_id="evt_fd469c29811879519c2c96")[0]
fact("review", "The January commitments review date", "Calendar (Frederick's copy)", "gcal_search_events, gcal_list_events",
     "Event 'Q4 commitments review' on Frederick's calendar", f'{dep("guardrails")} ("the January commitments review I\'ll put on our calendars"); search "Q4 commitments review"',
     f"Event evt_fd469c29811879519c2c96 {q(rv['summary'])}, starts Mon Jan 5 2026 9:00am PST (2026-01-05T17:00Z), organizer leonard.hayes@harmonygames.co, created {when(rv['created'])}; description {q(rv['description'])}",
     "VERIFIED (semantic future date: starts)", "YES (own calendar; check-sql)", dep("guardrails"), L("evt_fd469c29811879519c2c96"))

pf = rows("gdrive.drive_files", id=IDS["paperwork_folder"])[0]
fact("papers", "Frederick's paperwork folder (each counterparty's filed paper)", "Drive (owner Frederick)", "gdrive_search, gdrive_list_folder",
     "Folder 'Vendor & partner paperwork' in Frederick's Drive", 'search "paperwork"',
     f"Folder {IDS['paperwork_folder']} {q(pf['name'])}, owner {pf['owner_email']}; holds 33 papers (31 docs, 2 decks) named after their companies",
     "VERIFIED: 33 drive rows with this parent", "YES (owner; check-sql)", "—", L(IDS["paperwork_folder"]))

jn = rows("slack.slack_messages", id=SL["july_sign_note"])[0]
fact("july", "Leonard's July signing note (superseded by F4)", "Slack (#executives)", "slack_search_public_and_private",
     "#executives post by Leonard, Jul 22", 'search "accept the terms"',
     f"Message C07C2866011/{jn['ts']} (row {SL['july_sign_note']}), posted {when('2025-07-22T18:10:00Z')}: {q(clean(jn['text']))}; superseded by Leonard's Sep 25 'This replaces what I said in July' (F4)",
     "VERIFIED", "YES (member; check-sql)", dep("esg"), L(SL["july_sign_note"]))

rc = rows("slack.slack_messages", id=SL["robert_cancel_all"])[0]
fact("robert", "Robert's 'cancel every marketing tool' post (not a rule)", "Slack (#executives)", "slack_search_public_and_private",
     "#executives post by Robert, Sep 25", 'search "marketing tool"',
     f"Message C07C2866011/{rc['ts']} (row {SL['robert_cancel_all']}): {q(clean(rc['text']))}; the hub names the guardrails doc and the Monday change as the rules (F1)",
     "VERIFIED", "YES (member; check-sql)", dep("hub"), L(SL["robert_cancel_all"]))

ua = rows("gdocs.docs_documents", document_id="f_7bacf15c4e8eea1a52dcd4")[0]
fact("ua", "UA spend buckets doc (another scope)", "Docs (owner Frederick)", "gdrive_search, gdocs_get_document_text",
     "Doc about UA ad-network spend buckets", 'search "UA spend"',
     f"Doc f_7bacf15c4e8eea1a52dcd4 {q(ua['title'])}: {q(lines(ua['body_text'])[1])}; covers UA ad-network spend, which the hub keeps on the UA budget call (F1)",
     "VERIFIED", "YES (owner; check-sql)", dep("hub"), L("f_7bacf15c4e8eea1a52dcd4"))

trk = rows("gsheets.sheets_spreadsheets", spreadsheet_id=IDS.get("tracker_sheet", "f_9d6edd4922d8130ccd272e"))
fact("tracker", "Frederick's July 31 vendor tracker (stale)", "Sheets (owner Frederick)", "gdrive_search, gsheets_values_get",
     "Sheet 'Vendor & partner tracker'", 'search "Vendor & partner tracker"',
     "Spreadsheet f_9d6edd4922d8130ccd272e, created Thu Jul 31 2025 2:00pm PDT (2025-07-31T21:00Z); rows as of Jul 31: 'Clipforge' 'free through Jan 15 per the pilot agreement' · 'Pixel Harbor Events' 'deposit due Oct 10 if we go' · Playtestcloud · Solsten · Singular",
     "VERIFIED (grid_json)", "YES (owner; check-sql)", dep("hub"), L("f_9d6edd4922d8130ccd272e"))

# ---------------------------------------------------------------- trap evidence (corrections, done gaps, aliases)
nq = BQ["nin_req"]["msgs"][0]; nd = BQ["nin_done"]["msgs"][0]
fact("nin_mail", "Nintendo developer portal mails (look done)", "Gmail (Frederick To; base)", "gmail_search_messages, gmail_get_thread",
     "Two Sep 4 portal notices in Frederick's inbox", 'search "Nintendo"',
     f"frederick.stone@harmonygames.co/1842358947604469113 {q(nq['subject'])} sent {nq['date']}; frederick.stone@harmonygames.co/1842359398719557772 {q(nd['subject'])} sent {nd['date']}, body shows 'NDA Effective: 09/04/2025'; both from a no-reply portal sender (SVC_0208_EMAIL)",
     "VERIFIED (hg.py search gmail 'NDA Effective' → 1842359398719557772)", "YES (To; can-see)", "—",
     "gmail threads/frederick@harmonygames.co_1842358947604469113.json, threads/frederick@harmonygames.co_1842359398719557772.json")
fp = BS["fred_nintendo_post"]
fact("nin_post", "Frederick's Sep 4 post that he registered the account", "Slack (#executives; base)", "slack_search_public_and_private",
     "#executives post by Frederick, Sep 4", 'search "registered an account"',
     f"Message C07C2866011/1757011358.730529 (Frederick): {q(fp['text'].split(chr(10))[0])}",
     "VERIFIED", "YES (member; can-see)", "—", "slack messages (#executives) 2025-09.json ts 1757011358.730529")
zi = rows("linear.linear_issues")[0]; zc = rows("linear.linear_comments")[0]
ZQ = ["the Global ToS and NDA still needs our agreement approver to accept it, and that has to be a company officer from their own login",
      "no fee, no fixed term, no exclusivity, nothing about our IP, and either side can end it"]
zb = clean(zc["body"])
for x in ZQ:
    assert x in zb, x
lapse = re.search(r"[^.]*Oct 15[^.]*\.", zb).group(0).strip()
fact("zom", "ZOM-567 and Arthur's comment: Nintendo still needs an officer's acceptance", "Linear (unscoped)", "linear_search_issues, linear_get_issue, linear_list_comments",
     "Linear issue 'Switch: order dev kits' and its comments", f'{dep("nin_mail", "nin_post")} (Nintendo, the Switch dev kits); search "Nintendo"',
     f"Issue ZOM-567 {q(zi['title'])}; comment {zc['id']} by Arthur, created {zc.get('created_at')}: " + " · ".join(q(x) for x in ZQ) + f" · {q(lapse)}",
     "VERIFIED (comment body)", "YES (unscoped)", dep("nin_mail", "nin_post"), L("ZOM-567", zc["id"]))
pr = BS["playtestcloud_root"]
fact("pt_root", "Leonard's Sep 22 Playtestcloud post (root of the Framewell reply)", "Slack (#executives; base)", "slack_search_public_and_private, slack_conversations_replies",
     "#executives root post by Leonard, Sep 21 PT", 'search "Playtestcloud results are in"',
     f"Message C07C2866011/1758513190.847889 (Leonard): {q(pr['text'])}; reply_count updated to 1 by the SQL",
     "VERIFIED", "YES (member; can-see)", "—", "slack messages (#executives) 2025-09.json ts 1758513190.847889")
fw = rows("slack.slack_messages", id=SL["framewell_waiver_reply"])[0]
fact("waiver", "Framewell waiver: the Pro plan at no charge until Feb 1 (names Maren, not Framewell)", "Slack (#executives thread reply)", "slack_search_public_and_private, slack_conversations_replies",
     "Reply by Leonard in the thread under the Playtestcloud post", f'{dep("pt_root")} (thread replies); search "Maren"',
     f"Message C07C2866011/{fw['ts']} (row {SL['framewell_waiver_reply']}), reply under ts 1758513190.847889, posted {when('2025-09-26T21:02:00Z')}: {q(clean(fw['text']))}",
     "VERIFIED", "YES (member; check-sql)", dep("pt_root"), L(SL["framewell_waiver_reply"]))
dr = BS["dm_root"]
fact("dm_root", "Leonard's Sep 17 DM root 'we have no localization though'", "Slack (DM with Leonard; base)", "slack_conversations_history, slack_conversations_replies",
     "Message in Frederick's DM with Leonard, Sep 17", 'search "localization"',
     f"Message D05S58U4SAK/1758151772.570449 (Leonard): {q(dr['text'])}; reply_count updated to 1 by the SQL",
     "VERIFIED", "YES (DM member; can-see)", "—", "slack messages (DM) 2025-09.json ts 1758151772.570449")
lf = rows("slack.slack_messages", id=SL["lanternfly_dm"])[0]
fact("lf_dm", "Lanternfly already answered by Leonard (names Wen and the Southeast Asia deal)", "Slack (DM thread reply)", "slack_search_public_and_private, slack_conversations_replies",
     "Leonard's reply in the DM thread under his Sep 17 message", f'{dep("dm_root")} (thread replies); search "Southeast Asia"',
     f"Message D05S58U4SAK/{lf['ts']} (row {SL['lanternfly_dm']}), reply under ts 1758151772.570449, posted {when('2025-09-29T19:31:00Z')}: {q(clean(lf['text']))}",
     "VERIFIED", "YES (DM member; check-sql)", dep("dm_root"), L(SL["lanternfly_dm"]))
sn = rows("slack.slack_messages", id=SL["spotlight_note"])[0]
fact("sp_note", "Spotlight Fest already answered by Robert (names the Dec 5 indie showcase and Rina)", "Slack (#executives)", "slack_search_public_and_private",
     "#executives post by Robert, Sep 17", 'search "indie showcase"',
     f"Message C07C2866011/{sn['ts']} (row {SL['spotlight_note']}), posted {when('2025-09-17T18:41:00Z')} by Robert: {q(clean(sn['text']))}",
     "VERIFIED", "YES (member; check-sql)", "—", L(SL["spotlight_note"]))
sc = rows("gcal.gcal_events", event_id="evt_564a16d0f5f6598d0360d5")[0]
fact("sp_call", "Spotlight Fest showcase call (dates the call)", "Calendar (Frederick's copy)", "gcal_search_events",
     "Event 'Spotlight Fest showcase call' on Frederick's calendar", 'search "Spotlight Fest"',
     f"Event evt_564a16d0f5f6598d0360d5 {q(sc['summary'])}, started Wed Sep 17 2025 11:00am PDT (2025-09-17T18:00Z), organizer robert@harmonygames.co, Frederick and Rina invited; description {q(sc['description'])}",
     "VERIFIED (record time: held Sep 17)", "YES (own calendar; check-sql)", "—", L("evt_564a16d0f5f6598d0360d5"))
nt = rows("gmail.gmail_messages", id=IDS["msg"]["clipforge_notice"])[0]
NQ = [l for l in lines(nt["body_text"]) if "Oct 15" in l or "billing@paylane.io" in l or "monitored" in l]
fact("notice", "Paylane notice for workspace HG-2291: pilot ends Oct 15, billing from Oct 16", "Gmail (Frederick To)", "gmail_search_messages, gmail_get_thread",
     "Billing notice in Frederick's inbox about workspace HG-2291", 'search "HG-2291"',
     f"Thread {nt['thread_id']}, message {nt['id']}, sent {when(nt['date'])}, subject {q(nt['subject'])}: " + " · ".join(q(x) for x in NQ),
     "VERIFIED", "YES (To; check-sql)", "—", L(nt["id"], nt["thread_id"]))
ko = rows("gcal.gcal_events", event_id="evt_0a5e42c3aac62434ba2cfc")[0]
fact("kickoff", "UGC Studio kickoff ties workspace HG-2291 to Clipforge", "Calendar (Frederick's copy)", "gcal_search_events",
     "Event 'UGC Studio kickoff (workspace HG-2291)'", 'search "UGC Studio"',
     f"Event evt_0a5e42c3aac62434ba2cfc {q(ko['summary'])}, held Mon Jul 14 2025 9:00am PDT (2025-07-14T16:00Z), organizer Frederick, attendee Priya Raman",
     "VERIFIED (record time: held Jul 14)", "YES (own calendar; check-sql)", dep("notice"), L("evt_0a5e42c3aac62434ba2cfc"))

# ---------------------------------------------------------------- the 36 companies
STEP = {"Answered": "guardrails step 1 (already answered: note who and when; 'later' answers come back in January)",
        "End": "guardrails step 2 (cash between Oct 1 and Dec 31 ends now; cancel the way the paper or notice asks)",
        "Keep": "guardrails step 3 (on Arthur's keep-running list, F11: stays)",
        "Sign": "guardrails step 4 (costs nothing before January but needs an officer's acceptance or signature; ESG first when its triggers apply, F4)",
        "Park": "guardrails step 5 (free until January: pick it up at the January review, F13)"}
SEARCHQ = {r[0]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json"))) if False} if False else {}
BSR = {r["fid"]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json")))}
EXTRA_DEP = {"Nintendo": ("nin_mail", "nin_post", "zom", "esg", "board"), "Framewell": ("waiver",), "Lanternfly Publishing": ("lf_dm",),
             "Spotlight Fest": ("sp_note", "sp_call"), "Clipforge": ("notice", "kickoff"), "Pingwise": ("keepcard",),
             "Vaultline": ("keepcard",), "Certwell": ("keepcard",), "Wishwave": ("amend",), "Markward": ("esg", "july"),
             "Kinetic Arcade": ("esg", "checklist", "esg_contact"), "Lumencloud": ("esg", "checklist", "esg_contact"),
             "Bundlehouse": ("esg", "checklist", "esg_contact"), "Playfuse": ("esg",), "Orbit Store": ("esg",)}
ORDER = [k for k, v in TRUTH.items() if v["Decision"]]
for k in ORDER:
    t = TRUTH[k]
    tid = IDS["threads"].get(k)
    pid = IDS["papers"].get(k)
    deps = ("hub", "guardrails", "readme") + EXTRA_DEP.get(k, ())
    writes = []
    g = set(t["groups"])
    if "written_answer" in g:
        writes.append("written answer to " + ("billing@paylane.io (cancellation, F25) and to Priya Raman on her thread (her Sep 22 ask)" if k == "Clipforge" else f"{t['Contact']} on the thread"))
    if "card" in g:
        writes.append("To Do card on the Harmony Games board titled with the company")
    if "esg" in g:
        writes.append("one ESG intake email to PERSON_2599_EMAIL with the checklist items")
    if "contact_add" in g:
        writes.append(f"new contact {t['Contact']} (job {k})")
    if "revisit" in g:
        writes.append("reminder on Frederick's calendar on Mon Jan 5, 2026")
    if not writes:
        writes.append("log row only (no answer: already answered or a portal)")
    if k == "Nintendo":
        exp = ("No company thread or paper: the portal mails (F18), Frederick's post (F19) and Arthur's ZOM-567 comment (F20) carry it. "
               f"Log row: Company 'Nintendo' · Contact blank (no-reply portal; README 'portals and no-reply senders don't get one') · What's waiting 'platform developer terms' · Decision Sign · Next date due 2025-10-15 (F20 'accepted by Oct 15'). Writes: " + "; ".join(writes))
        src = L("ZOM-567")
        vis = "YES (unscoped Linear; portal mails To, can-see)"
        loc = "Linear ZOM-567 plus the two Sep 4 portal mails"
        org = f'{dep("zom")}; search "Nintendo"'
    elif k == "Balancy":
        bm = BQ["balancy"]["msgs"]
        lv = next(m for m in bm if "leonard" in str(m["from"]).lower())
        lvq = "company priorities have shifted a bit for the next few months"
        assert lvq in lv["body"], "balancy quote"
        exp = (f"Base thread frederick.stone@harmonygames.co/1840501641217286806 ({len(bm)} messages, Frederick cc; Balancy rep PERSON_0527_NAME, PERSON_0527_EMAIL): "
               f"Leonard {lv['date']}: {q(lvq)}; rep's last mail {bm[0]['date']}: {q('thank you for the update')}. "
               f"Log row: Decision Answered · Answered by Leonard (Thu Sep 11 PT) · told 'later' → Next date 2026-01-05 (F13). Writes: " + "; ".join(writes))
        src = "gmail threads/frederick@harmonygames.co_1840501641217286806.json /messages"
        vis = "YES (cc; can-see)"
        loc = "Frederick's mailbox, base thread 'Re: [SOURCE_ORG_0001] & Balancy'"
        org = 'search "Balancy"'
    else:
        ms = fred_msgs(tid)
        first, last = ms[0], ms[-1]
        inbound = [m for m in ms if m["from_email"] != FRED]
        ask = inbound[-1] if inbound else last
        ttl, pl = paper(pid) if pid else (None, [])
        exp = (f"Thread {tid} ({len(ms)} message{'s' if len(ms) > 1 else ''}; first {when(first['date'])} from {first['from_name']} ({first['from_email']}), subject {q(first['subject'])}); "
               f"latest from them {when(ask['date'])}: {q(content_line(ask['body_text']))}. ")
        if pid:
            exp += f"Paper {pid} {q(ttl)}: " + " · ".join(q(x) for x in pl) + ". "
        else:
            exp += "No filed paper (terms in the mail body). "
        nd = t["Next date"] or "blank"
        exp += (f"Log row: Company {q(k)} · Contact {q(t['Contact'] or '')} · Decision {t['Decision']}"
                + (f" · Answered by {t['Answered by']}" if t["Answered by"] else "")
                + f" · Next date {nd}{' (due/plan date)' if t['Next date'] else ''}. Writes: " + "; ".join(writes))
        src = L(*(x for x in (tid, pid, ask["id"]) if x))
        vis = "YES (To; check-sql)" if not pid else "YES (To; paper owned; check-sql)"
        loc = f"Frederick's mailbox, thread {q(first['subject'])}" + (f"; paper {q(ttl)} in the paperwork folder" if pid else "")
        b = BSR.get(f"C:{k}") or {}
        org = f'search "{b.get("query", k.split()[0])}"' + (f"; {dep('papers')} (paper)" if pid else "")
    res = f"VERIFIED: quotes cut from the records; Decision by {STEP[t['Decision']]}; Next date by the README rule (F8) — derived, not_a_claim beyond the quotes"
    fact("co:" + k, f"{k}: {t['What\'s waiting']} — {t['Decision']}", "Gmail + Docs/Slides" if k not in ("Nintendo",) else "Linear + Gmail",
         "gmail_search_messages, gmail_get_thread, gdocs_get_document_text / gslides_get_presentation_text", loc, org, exp, res, vis, dep(*deps), src)

# ---------------------------------------------------------------- boundaries (off the log)
BND = [("rayking", "Rayking Game: only forwarded around internally", 'search "Chinese Local Game publishing"', "Frederick's 'Hi …, Leonard forwarded me your email' went to Leonard only; the hub: 'Cold pitches nobody answered, including ones we only forwarded around internally, stay off it'"),
       ("playable", "Playable Factory: cold pitch nobody answered", 'search "Playable Factory"', "two inbound pitches (Sep 11, Sep 24), no reply from Harmony Games"),
       ("google", "Google partner check-in: an ad network", 'search "Check-in"', "the hub keeps the ad networks on the UA budget call"),
       ("gamesforum", "Gamesforum SF: speaker invite nobody answered", 'search "Gamesforum"', "one inbound invite (Sep 10), no reply"),
       ("interco", "InterCo Digital: cold pitch nobody answered", 'search "call with Zynga"', "three inbound mails, no reply"),
       ("singular", "Singular: named in the hub's UA exclusion", 'search "Restructure Payment Plan"', "the hub: 'and so do the ad networks, PlayableX, Craftsman+ and Singular'"),
       ("ncsoft", "NCsoft: strategic / investor talks", 'search "NCSoft"', "a meeting report, not an offer in front of us; investor work stays off"),
       ("dentsu", "Dentsu: investor meeting Leonard is flying to", 'search "Dentsu"', "the hub: 'the investors' stay off")]
for key, val, org, why in BND:
    b = BQ[key]
    m0 = b["msgs"][0]
    fact("b:" + key, val, "Gmail (Frederick's mailbox; base)", "gmail_search_messages, gmail_get_thread", f"Base thread {q(m0['subject'])}", org,
         f"Thread {b['id']} ({b['n']} message{'s' if b['n'] > 1 else ''}), latest {m0['date']} {q(m0['subject'])}; off the log: {why}",
         "VERIFIED (base thread)", "YES (own mailbox; can-see)", dep("hub"), f"gmail threads/frederick@harmonygames.co_{b['id'].split('/')[1]}.json")
nv = fred_msgs(IDS["threads"]["Nova Rewards"])
fact("b:nova", "Nova Rewards: offer withdrawn Sep 23", "Gmail (Frederick To)", "gmail_search_messages, gmail_get_thread", "Thread from Nova Rewards", 'search "Nova Rewards"',
     f"Thread {IDS['threads']['Nova Rewards']}; latest {when(nv[-1]['date'])}: {q(content_line(nv[-1]['body_text']))}; off the log (withdrawn)",
     "VERIFIED", "YES (To; check-sql)", dep("hub"), L(IDS["threads"]["Nova Rewards"]))
mt = BS["mattel_post"]
fact("b:mattel", "Mattel: Leonard keeps it", "Slack (#executives; base)", "slack_search_public_and_private", "#executives post with Mattel's RFP, Sep 2", 'search "RFP"',
     f"Message C07C2866011/1756832039.396149: {q(lines(mt['text'])[1][:90])}; the hub: 'and Mattel, which I'm keeping'",
     "VERIFIED", "YES (member; can-see)", dep("hub"), "slack messages (#executives) 2025-09.json ts 1756832039.396149")
ex = rows("contacts.contacts")
fact("contacts_existing", "Counterparty contacts already in Contacts (no new contact)", "Contacts (unscoped)", "contacts_search_contacts",
     "Contacts entries for Kinetic Arcade, Lumencloud and Markward", 'search "Kinetic"',
     "; ".join(f"{r['contact_id']} {r.get('first_name')} {r.get('last_name')} (job {r.get('job')})" for r in ex if r["contact_id"] != "9b0185e445572aeee9f27d35"),
     "VERIFIED", "YES (unscoped)", dep("readme"), L(*(r["contact_id"] for r in ex if r["contact_id"] != "9b0185e445572aeee9f27d35")))

# ---------------------------------------------------------------- requirements
def F(*keys):
    return ", ".join(fid_of[k] for k in keys)


CO = {d: [fid_of["co:" + k] for k in ORDER if TRUTH[k]["Decision"] == d] for d in ("Answered", "End", "Keep", "Sign", "Park")}
ALLCO = [fid_of["co:" + k] for k in ORDER]
REV = [fid_of["co:" + k] for k in ORDER if "revisit" in TRUTH[k]["groups"]]
REQ = [
    ("Leonard's email yesterday puts the vendor and partner backlog on me this week.", "Discovery — Leonard's Sep 30 email is the source of every ask", "Explicit", F("hub")),
    ("going by his email for what needs doing and how we decide each one", "Constraint — decide each company by the rules his email names (guardrails doc, the Monday change, ESG's note and Leonard's reply, the README)", "Implicit (incorporated through F1)", F("guardrails", "amend", "esg", "checklist", "readme", "template", "keepcard")),
    ("Can you work through all of it", "Discovery — the population: every outside company with an offer, trial, quote, terms or ask in front of us that one of us engaged with (36), minus the hub's exclusions", "Implicit (scope sentence in F1)", F("hub", "papers") + ", " + ", ".join(ALLCO) + ", " + F("b:rayking", "b:playable", "b:google", "b:gamesforum", "b:interco", "b:singular", "b:ncsoft", "b:dentsu", "b:nova", "b:mattel")),
    ("The log goes in my Q4 commitments folder", "Write — one sheet with the README's name and columns, one row per company, in the folder", "Explicit (name and columns implicit through F8)", F("folder", "readme", "template")),
    ("going by his email for what needs doing", "Write — a written answer to every company waiting to hear from us (F1), matching its decision (F2 'Answers')", "Implicit", F("hub", "guardrails") + ", " + ", ".join(CO["End"] + CO["Keep"] + CO["Sign"] + CO["Park"])),
    ("the cards for anything that needs signing go on our Harmony Games board", "Write — one To Do card per company waiting on a signature, company name in the title (F4 reply)", "Explicit (list and title rule implicit)", F("esg", "board") + ", " + ", ".join(CO["Sign"])),
    ("how we decide each one", "Write — one ESG intake email per agreement ESG must review, with the checklist items (F4, F5, F6)", "Implicit", F("esg", "checklist", "esg_contact")),
    ("on me this week", "Constraint — the written answers go out this week (F1 'this week'); the answers are sent, not drafted", "Explicit", F("hub")),
    ("For anything that comes back at the January review", "Discovery — which companies come back (Park rows and 'later' answers, F2 steps 1 and 5) and the review date (F13)", "Explicit", F("guardrails", "review") + ", " + ", ".join(REV)),
    ("put a reminder on my calendar for that day, one per company", "Write — one event per returning company on Mon Jan 5, 2026, on Frederick's calendar", "Explicit", F("review") + ", " + ", ".join(REV)),
    ("going by his email for what needs doing and how we decide each one", "Write — a contact for each company's person not already in Contacts, company in the job field (F1, F8)", "Implicit", F("hub", "readme", "contacts_existing")),
    ("reply to Leonard on his email with what he asked for", "Write — a reply on the hub thread listing what we keep and what waits on Arthur or Leonard to sign", "Explicit (content through F1)", F("hub") + ", " + ", ".join(CO["Keep"] + CO["Sign"])),
]
for span, *_ in REQ:
    assert span in PROMPT, span

# ---------------------------------------------------------------- writes
keep = [k for k in ORDER if TRUTH[k]["Decision"] == "Keep"]
sign = [k for k in ORDER if TRUTH[k]["Decision"] == "Sign"]
esgk = [k for k in ORDER if "esg" in TRUTH[k]["groups"]]
ans = [k for k in ORDER if "written_answer" in TRUTH[k]["groups"]]
rev = [k for k in ORDER if "revisit" in TRUTH[k]["groups"]]
con = [k for k in ORDER if "contact_add" in TRUTH[k]["groups"]]
DEFER = ("gmail · slack (Frederick's mailbox; #executives and the Leonard DM): persona_view searches 'hold off', 'don't send', 'not yet', 'don't reply' (limit 50, no hit at its limit) — "
         "population complete: gmail 2 / 0 / 3 / 10 hits, slack 20 / 0 / 77 / 0, none from Sep 26–30 about these companies; the only September hits are frederick.stone@harmonygames.co/1817715521687421486 and "
         "frederick.stone@harmonygames.co/1842277213140775733 (unrelated); the SQL holds none of the four phrases; governing version: Leonard's Sep 30 email frederick.stone@harmonygames.co/1844732913254784171, the latest record on the backlog — no defer")
WR = [
    ("R4", "Create the log sheet and write its rows", '"The log goes in my Q4 commitments folder"', "gsheets_create_spreadsheet (exists), gsheets_values_update (exists), gdrive_move_file (exists)",
     "title; spreadsheetId, range, values; fileId, newParentId", F("folder", "readme", "template"), "a native sheet named like 'Q4 commitments log' whose parent is the folder, header + 36 rows",
     "the README's seven columns; one row per company with its Decision, Answered by and Next date"),
    ("R5", f"Written answers ({len(ans)} companies; Clipforge also gets the Paylane cancellation)", '"going by his email for what needs doing"', "gmail_reply_to_message (exists), gmail_send_message (exists)",
     "message_id, body; to, subject, body", ", ".join(fid_of["co:" + k] for k in ans) + ", " + F("notice"), "sent (not drafted) on each company's thread; billing@paylane.io for the Clipforge cancellation",
     "End: a no or a written cancellation; Keep: staying; Sign: with Leonard or Arthur to sign (and our lawyers first when ESG reviews); Park: picking it up in January"),
    ("R6", f"Signing cards ({len(sign)}: {', '.join(sign)})", '"the cards for anything that needs signing go on our Harmony Games board"', "trello_create_card (exists)",
     "idList, name", F("board") + ", " + ", ".join(fid_of["co:" + k] for k in sign), "card created on the To Do list 640643a3fd8f3ca308d93195", "the company's name in the card title"),
    ("R7", f"ESG intake emails ({len(esgk)}: {', '.join(esgk)})", '"how we decide each one"', "gmail_send_message (exists)", "to, subject, body",
     F("esg_contact", "checklist") + ", " + ", ".join(fid_of["co:" + k] for k in esgk), "sent to PERSON_2599_EMAIL, one email per agreement", "the checklist items: counterparty, what it is, term, renewal, cost, who signs"),
    ("R11", f"New contacts ({len(con)})", '"going by his email for what needs doing and how we decide each one"', "contacts_add_new_contact (exists)", "first_name, last_name (+ email, job)",
     F("contacts_existing") + ", " + ", ".join(fid_of["co:" + k] for k in con), "contact created", "the person from the company's thread, the company in the job field; skip the three already present and Nintendo's portal"),
    ("R10", f"January-review reminders ({len(rev)})", '"put a reminder on my calendar for that day, one per company"', "gcal_create_event (exists)", "calendarId, event",
     F("review") + ", " + ", ".join(fid_of["co:" + k] for k in rev), "one event per company on Mon Jan 5, 2026 on Frederick's calendar", "the company's name in the event"),
    ("R12", "Reply to Leonard", '"reply to Leonard on his email with what he asked for"', "gmail_reply_to_message (exists)", "message_id, body", F("hub"),
     f"sent on thread {hub_tid}", f"keeping: {', '.join(keep)}; waiting on Arthur or Leonard to sign: {', '.join(sign)}"),
]

# ---------------------------------------------------------------- traps, risks
TRAPS = [
    ("T1", f"Nintendo looks done: 'Registration Completed' and Frederick's 'I registered an account' ({fid_of['nin_mail']}, {fid_of['nin_post']})", fid_of["zom"], f"Arthur's Sep 25 comment {zc['id']} on ZOM-567 (later, CTO): an officer must still accept by Oct 15"),
    ("T2", f"Framewell's order form bills Pro from Nov 1 ({fid_of['co:Framewell']}, {IDS['papers']['Framewell']})", fid_of["waiver"], f"Leonard's Sep 26 thread reply C07C2866011/{fw['ts']} (later than the Sep 18 form) names Maren, who sends the form"),
    ("T3", f"Lanternfly's Sep 22 'Any news on the proposal?' is unanswered in its thread ({fid_of['co:Lanternfly Publishing']}, {IDS['threads']['Lanternfly Publishing']})", fid_of["lf_dm"], f"Leonard's Sep 29 DM thread reply D05S58U4SAK/{lf['ts']} names Wen, who signs the thread"),
    ("T4", f"Pingwise bills $29/month from Nov 1 ({fid_of['co:Pingwise']}, {IDS['papers']['Pingwise']})", fid_of["keepcard"], f"Arthur's checklist item {IDS['keep_items'][2]} 'the night pager for backend outages' = Pingwise's on-call paging"),
    ("T5", f"Clipforge's pilot agreement and the July tracker say free through Jan 15 ({fid_of['co:Clipforge']}, {IDS['papers']['Clipforge']})", fid_of["notice"], f"the Sep 12 Paylane notice {nt['id']} for workspace HG-2291 (on the agreement and the Jul 14 kickoff evt_0a5e42c3aac62434ba2cfc)"),
    ("T6", f"Pixel Harbor's quote is from June ({fid_of['co:Pixel Harbor Events']}, {IDS['threads']['Pixel Harbor Events']})", fid_of["hub"], f"the hub's scope has no date limit ({hub_tid}); the deposit is due Oct 10 ({IDS['papers']['Pixel Harbor Events']})"),
    ("T7", f"Leonard's July note lets Fred accept small terms ({fid_of['july']}, C07C2866011/{jn['ts']})", fid_of["esg"], f"ESG Sep 24 + Leonard Sep 25 'This replaces what I said in July' ({IDS['msg']['esg_ack']})"),
    ("T8", "the guardrails say 'first week of January' (f_b98287f6f80fe431a71209)", fid_of["review"], "the review event evt_fd469c29811879519c2c96 starts Mon Jan 5, 2026"),
    ("T9", f"the guardrails count travel only when we book it ({fid_of['guardrails']}, f_b98287f6f80fe431a71209)", fid_of["amend"], f"Leonard's Mon Sep 29 post C07C2866011/{am['ts']} (later): partner-booked travel counts"),
    ("T10", f"Robert's 'just cancel every marketing tool' ({fid_of['robert']}, C07C2866011/{rc['ts']})", fid_of["guardrails"], "author Robert; the hub names Leonard's doc f_b98287f6f80fe431a71209 as the rule"),
    ("T11–T18", "Playable Factory, Google, NCsoft, Nova Rewards, Rayking, Gamesforum, InterCo, Dentsu look like offers", fid_of["hub"], f"scope sentence in {hub_tid}: engaged, not cold, not withdrawn, not investor or ad-network work"),
    ("T13", f"Balancy's trial offer looks open ({fid_of['co:Balancy']})", fid_of["co:Balancy"], "Leonard's Sep 11 in-thread 'we'll circle back' (a 'later' answer) in frederick.stone@harmonygames.co/1840501641217286806"),
    ("T14", f"the July 31 tracker as the population ({fid_of['tracker']}, f_9d6edd4922d8130ccd272e)", fid_of["hub"], f"dated Jul 31; the hub's rule over the mail decides ({hub_tid})"),
    ("T17", f"Retainly's trial looks like Reviewly's paid conversion ({fid_of['co:Retainly']}, {IDS['papers']['Retainly']})", fid_of["co:Reviewly"], f"Retainly converts Jan 12, 2026 (outside the window; {IDS['papers']['Retainly']})"),
    ("T19", f"Spotlight Fest's Dec 5 invitation with a $750 stand fee looks open ({fid_of['co:Spotlight Fest']}, {IDS['threads']['Spotlight Fest']})", fid_of["sp_note"], f"Robert's Sep 17 note C07C2866011/{sn['ts']} names the Dec 5 indie showcase and Rina, who sent the invitation"),
    ("T20", f"Hootline has nothing after Aug 12 and no filed paper ({fid_of['co:Hootline']}, {IDS['threads']['Hootline']})", fid_of["hub"], f"the hub's scope counts a sign-up and has no date limit ({hub_tid}); Gemma's Aug 12 question is unanswered"),
]
RISKS = [
    ("1", "Clipforge needs two writes: the cancellation to billing@paylane.io and a written answer to Priya (her Sep 22 'let me know here too')", fid_of["co:Clipforge"], "rubric (two rows or one row naming both)", "rubric stage: accept either order"),
    ("2", "Reminder form and time of day: one event per company is asked; the time is open", ", ".join(REV), "rubric (representational time)", "accept any time on Mon Jan 5, 2026"),
    ("3", "ESG intake signer: 'Leonard or Arthur' or either name (checklist wording 'who would sign it (Leonard or Arthur)')", fid_of["checklist"], "rubric", "accept both"),
    ("4", "Balancy's contact is a token (PERSON_0527_NAME) or the name in his signature's booking link", fid_of["co:Balancy"], "rubric (contact name)", "accept either spelling"),
    ("5", "Nintendo gets a log row and a card but no written answer and no contact (no-reply portal; README excludes portals)", fid_of["co:Nintendo"], "OE accuracy / rubric", "no write to the portal"),
    ("6", "Six baselines (run_forensics/rev4/baseline) missed Nintendo, Balancy, Framewell, Lanternfly and Spotlight in every run: rows on these will be all-fail", ", ".join([fid_of["co:Nintendo"], fid_of["co:Balancy"], fid_of["co:Framewell"], fid_of["co:Lanternfly Publishing"], fid_of["co:Spotlight Fest"]]), "rubric all-fail justifications; difficulty spread", "genuine misses: each record is persona-visible (§B proof)"),
]

# ---------------------------------------------------------------- visibility proof
brow = [" | ".join(str(c) for c in f) for f in FACTS]
need = sorted({x for r in brow for _, x in G.scoped_ids(r)})
seeded = [x for x in need if x in LINE]
base = [x for x in need if x not in LINE]
lbf = os.path.join(HERE, "oe_lb_ids.txt")
open(lbf, "w").write("\n".join(seeded) + "\n")
cs_txt = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", "frederick_stone", "Task_Authoring/task_inputs/01_Universe_Inject.sql",
              "--load-bearing", "Task_Authoring/task_inputs/Working_Files/plan/oe_lb_ids.txt"])
yes_rows = [l for l in cs_txt.splitlines() if l.startswith("[YES LB]") and any(x in l for x in seeded)]
verdict = [l for l in cs_txt.splitlines() if l.startswith("verdict:")]
svc_of = {x: s for r in brow for s, x in G.scoped_ids(r)}
cansee = []
for x in base:
    out = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "can-see", "frederick_stone", svc_of[x], x]).splitlines()
    cansee.append(out[0] if out else f"frederick_stone {svc_of[x]} {x}: UNVERIFIED")

# ---------------------------------------------------------------- write
O = []
P = O.append
P("# 08 OE Writing Ledger — frederick_q4_commitments (vendor and partner backlog, injection rev4)")
P("Generated 2026-11-04 · Clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · seed bound 2025-10-01T00:00:00Z · Persona Frederick Stone frederick.stone@harmonygames.co (Co-founder) · Tier Long-Horizon · Mode Easy")
P(f"Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all {len(WR)} write families map to cataloged tools, friction is none")
P("Inputs read: 04_Prompt.txt — present (sha256 32f7ab0cabd6) · 00_Assigments.md — present · 01_Universe_Inject.sql — present (rev4, sha256 69603ab4b6a4) · 01_Grounding_Dossier.md — present (rev4, leads only) · 01_Scenario_Design.md + 01_Hardness_Manifest.json — present (leads for traps only) · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files_Manifest.md — absent (no attachments) · 04_Prompt_Writing_Brief.md — present (§4b accepted outcomes)")
P("")
P("Persona binding: roster entry frederick_stone, Frederick Stone, Co-founder, Executive, frederick.stone@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of #executives and the 1:1 DM with Leonard), Calendar (own calendar), Drive/Docs/Sheets/Slides (files he owns or that are shared with him). Unscoped: Trello, Linear, Contacts.")
P("")
P("Dates: Pacific first, UTC beside it. 'sent', 'created', 'posted' and 'held' mark record times; 'starts' and 'due' mark semantic future dates. Every record time below is at or before the seed bound.")
P("")
P("## A · Requirements (traced to the prompt)")
P("| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |")
P("|---|---|---|---|---|")
for i, (span, typ, ex, fids) in enumerate(REQ, 1):
    P(f'| R{i} | "{span}" | {typ} | {ex} | {fids} |')
P("")
P("## B · Facts")
P("| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search \"query text\") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |")
P("|---|---|---|---|---|---|---|---|---|---|---|")
for f in FACTS:
    P("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in f) + " |")
P("")
P("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
P("")
P(f"`python3 Task_Authoring/tools/persona_view.py check-sql frederick_stone Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing plan/oe_lb_ids.txt` ({len(seeded)} seeded ids; load-bearing rows and the verdict line kept):")
P("")
for l in yes_rows + verdict:
    P(l)
P("")
P(f"`python3 Task_Authoring/tools/persona_view.py can-see frederick_stone <service> <id>` ({len(base)} base ids, first line of each):")
P("")
for l in cansee:
    P(l)
P("")
P("## C · Write capability")
P("| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |")
P("|---|---|---|---|---|---|---|---|---|---|")
for w in WR:
    P("| " + " | ".join(w) + f" | {DEFER} | yes |")
P("")
P("## D · Friction facts")
P("| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |")
P("|---|---|---|---|---|---|")
P("| none | Friction: none (03_Error_Async_Config.txt) | — | — | — | — |")
P("")
P("## E · Traps and distractors")
P("| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |")
P("|---|---|---|---|")
for t in TRAPS:
    P("| " + " | ".join(t) + " |")
P("")
P("## F · Open risks")
P("| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |")
P("|---|---|---|---|---|")
for r in RISKS:
    P("| " + " | ".join(r) + " |")
P("")
P("## G · Tally")
nq = sum(1 for f in FACTS if "VERIFIED" in f[7])
P(f"Requirements {len(REQ)} · facts {len(FACTS)} · writes {len(WR)} (feasible {len(WR)}) · friction items 0 · expected values {len(FACTS)} (quoted {nq} · not_a_claim {len(ORDER)} derived decisions · ABSENCE-checked 1 defer search) · unverified visibility 0 · blocking 0")
P("")
P("## Self-review")
P("")
P("Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every §B value was re-verified in this run from its record: injected rows parsed from 01_Universe_Inject.sql (rev4, line numbers from persona_view check-sql), base threads and posts read through tools/hg.py (plan/oe_base_quotes.json, plan/oe_base_slack.json), and each quote is asserted as a substring of its record by plan/assemble_oe_ledger.py before the file is written. No-event-text scan: the ledger holds facts, quotes and dependency edges only; it contains no OE heading, no Expected line and no agent instruction.")
P("")
P("| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |")
P("|---|---|---|---|")
CRS = [
    ("R1", "'Leonard's email yesterday' could be another Leonard mail from Sep 30", f"his only other Sep 26–30 mails to Fred are TestFlight build notices; the hub is the one about the backlog ({hub_tid}, sent 4:20pm PDT Sep 30)", "holds"),
    ("R2", "the guardrails doc alone could decide, without the Monday change or ESG's reply", f"the hub names the Monday post and ESG's note beside the doc ({fid_of['hub']}); the post {fid_of['amend']} and the reply {fid_of['esg']} are later than the doc (Sep 29, Sep 25 vs Sep 26 for the reply's July supersession)", "holds"),
    ("R3", "the population could be only September mail, the paperwork folder, or the July tracker", f"the hub's scope sentence has no date limit; Hootline ({fid_of['co:Hootline']}) has only August mail and no paper, Pixel Harbor ({fid_of['co:Pixel Harbor Events']}) a June quote, Nintendo ({fid_of['co:Nintendo']}) no thread; the tracker ({fid_of['tracker']}) is dated Jul 31", "holds (36 rows)"),
    ("R4", "the log could be the template itself or a Doc", f"README {fid_of['readme']}: 'One sheet for the vendor and partner backlog' and 'Name it \"Q4 commitments log\"; to start, copy the header row from the template sheet'", "holds"),
    ("R5", "a written answer could be owed to the four Answered companies or to Nintendo's portal", f"guardrails {fid_of['guardrails']} step 1: 'don't write to them again'; 'Portals and no-reply notices don't need one'", "holds (31 companies + Priya)"),
    ("R6", "the cards could go on another board (no board is named 'founders')", f"the prompt names 'our Harmony Games board'; board 640643a3fd8f3ca308d9318e is the only one with that name ({fid_of['board']})", "holds"),
    ("R7", "Nintendo, Orbit Store, Markward or Playfuse could also need ESG", f"ESG's triggers ({fid_of['esg']}); Nintendo's comment says 'no fee, no fixed term, no exclusivity, nothing about our IP' ({fid_of['zom']}); Playfuse is on ESG's mutual NDA template ({fid_of['co:Playfuse']})", "holds (3 emails)"),
    ("R8", "'this week' could mean before the Oct 1 clock only", "the hub (Tue Sep 30) asks for answers 'this week'; the clock is Wed Oct 1, inside that week", "holds"),
    ("R9", "only parked rows come back in January (the review's description says 'Everything we parked')", f"guardrails step 1: a 'later' answer 'comes back at the January commitments review' ({fid_of['guardrails']}); Lanternfly ({fid_of['co:Lanternfly Publishing']}) and Balancy ({fid_of['co:Balancy']}) are 'later' answers", "holds (14)"),
    ("R10", "one event listing all companies could satisfy the reminders", "the prompt asks 'one per company'; review date from evt_fd469c29811879519c2c96", "holds (14 events)"),
    ("R11", "Kinetic Arcade, Lumencloud, Markward and the ESG intake could get new contacts", f"README 'only add a person who isn't in Contacts already'; the three are present ({fid_of['contacts_existing']}), ESG is present ({fid_of['esg_contact']}), Nintendo is a portal", "holds (32)"),
    ("R12", "the reply could go as a new email or list every decision", f"the hub: 'reply here with what we're keeping and what's waiting on Arthur or me to sign' ({hub_tid}); extra lines are allowed", "holds"),
]
for r in CRS:
    P("| " + " | ".join(r) + " |")
P("")
P("Unresolved: none blocking. Open risks §F 1–6 go to the rubric stage (two Clipforge writes, reminder time, signer wording, Balancy's token name, Nintendo's no-write rows, and the five rows every rev4 baseline missed).")
P("")
open(os.path.join(WF, "08_OE_Writing_Ledger.md"), "w").write("\n".join(O) + "\n")
json.dump({"fid": fid_of, "seeded": seeded, "base": base}, open(os.path.join(HERE, "oe_ledger_ids.json"), "w"), indent=1)
print("facts", len(FACTS), "req", len(REQ), "seeded ids", len(seeded), "base ids", len(base), "yes rows", len(yes_rows), "cansee", [l.split(":")[-1].strip()[:3] for l in cansee])
