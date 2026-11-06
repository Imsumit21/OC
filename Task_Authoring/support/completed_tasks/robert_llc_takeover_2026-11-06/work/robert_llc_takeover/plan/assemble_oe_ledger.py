#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep) for the Robert LLC take-over task (rev4 SQL f1a290ced176).
Seeded rows are parsed from the SQL (never executed); base records come from plan/oe_base.json (fresh hg.py reads,
plan/oe_reads.py) and plan/oe_defer.json (plan/oe_defer.py). Facts and dependency edges only; no event text.
Every quote is asserted as a substring of its record, so a wrong value stops the build."""
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from decimal import Decimal
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
import stage_gate as G  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
PERSONA = "robert"
TDREL = "Task_Authoring/task_inputs"
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQL_PATH).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
IDS = json.load(open(os.path.join(HERE, "ids.json")))
I, BASE, ISSUE = IDS["IDS"], IDS["BASE"], IDS["issues"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
DEF = json.load(open(os.path.join(HERE, "oe_defer.json")))
CATALOG = {t["name"] for t in json.load(open(os.path.join(WS, "Evals", "references", "tools", "catalog.json")))}
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": TDREL}


def run(args):
    return subprocess.run(args, cwd=WS, capture_output=True, text=True, env=ENV).stdout


CS = json.loads(run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, f"{TDREL}/01_Universe_Inject.sql", "--json"]))
LINE = {}
for r in CS["rows"]:
    for k in r["keys"]:
        LINE.setdefault(k, r["line"])
SQL_LINES = SQL.splitlines()


def sql_line(k):
    if k in LINE:
        return LINE[k]
    for i, ln in enumerate(SQL_LINES, 1):
        if f"'{k}'" in ln and ln.lstrip().startswith(("VALUES", "INSERT", "UPDATE")):
            return i
    return None


def L(*keys):
    out = []
    for k in keys:
        n = sql_line(k)
        assert n, k
        out.append(f"SQL L{n}")
    return ", ".join(out)


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")


def when(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M%p').replace('AM', 'am').replace('PM', 'pm')} {p.tzname()} ({d.strftime('%Y-%m-%dT%H:%M:%SZ')})"


def ts_iso(ts):
    return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def must(text, *quotes):
    for q in quotes:
        assert q in text, (q, text[:300])
    return " · ".join("'" + q + "'" for q in quotes)


def tools(*names):
    for n in names:
        assert n in CATALOG, n
    return ", ".join(names)


FACTS, fid_of = [], {}


def fact(key, value, service, tl, locator, origin, expected, result, visible, depends, source):
    assert source
    n = f"F{len(FACTS) + 1}"
    fid_of[key] = n
    FACTS.append((n, value, service, tl, locator, origin, expected, result, visible, depends, source))
    return n


def dep(*keys):
    return ", ".join(fid_of[k] for k in keys) or "—"


F = dep
UNSC = "unscoped service; natural pointer in the Locator origin column"
SY = "YES (proof below)"
SM = {f"{r['channel_id']}/{r['ts']}": r for r in rows("slack.slack_messages")}
GM = {r["id"]: r for r in rows("gmail.gmail_messages")}
BS = OB["slack"]


def base_msg(k):
    v = BS[k]
    return v["rec"], f"slack {v['file']}#{v['pointer']}"


def btext(k):
    return base_msg(k)[0]["text"]


# ---------------------------------------------------------------- the request and its incorporated rules
hub = SM[I["hub"]]
ht = clean(hub["text"])
HUBQ = ["let's set the LLC up properly", "I put everything we might need from HG into the LLC project in linear, one issue each",
        "go through them and make the call on each one: what the LLC takes if Sunset can't sell it, what it costs us March through May, and who pays what",
        "the ground rules doc has how we decide", "lay the sheet out like my draft from Tuesday, keep it in your drive and share it with Blake and me",
        "leave your call on each issue too so we can see it there", "I'll email you how we split the money",
        "then tell me here what you'd do and what it costs each of us a month", "we decide on Monday's call"]
fact("hub", "Leonard's DM: the request", "Slack (Robert's DM with Leonard)", tools("slack_conversations_search_messages", "slack_read_channel"),
     "Robert's 1:1 DM with Leonard Hayes, Leonard's message of Thursday night", 'prompt ("Leonard sent me a DM on Thursday night")',
     f"{I['hub']}, sent {when(ts_iso(hub['ts']))} by Leonard Hayes (Thursday 9:40pm PT). Quotes: " + must(ht, *HUBQ),
     "VERIFIED: every quote cut from the message text", SY, "—", f"{I['hub']}, {L(I['hub'])}")

proj = rows("linear.linear_projects")[0]
pd = clean(proj["description"])
PROJQ = ["One issue per thing the LLC might take from HG or pay for.", "Leave your call on each one as a comment and move it:",
         "to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it;",
         "to Todo if the LLC takes it and something is still to do, and assign whoever moves it;", "to Canceled if it stays with HG."]
iss = {r["id"]: r for r in rows("linear.linear_issues")}
assert len(iss) == 37 and all(r["project_id"] == proj["id"] and r["state_id"] == "Backlog" and r["assignee_id"] is None for r in iss.values())
fact("project", "The 'LLC take-over' project: scope, the move rule and its 37 issues", "Linear", tools("linear_list_projects", "linear_list_issues"),
     "the Linear project named 'LLC take-over', team ENG", 'prompt ("the LLC project in Linear"); ' + dep("hub") + ' ("the LLC project in linear")',
     f"Project {proj['id']}, '{proj['name']}', team {proj['team_id']}, created {when(proj['created_at'])}. Description quotes: " + must(pd, *PROJQ)
     + ". 37 issues: " + "; ".join(f"{k} {iss[k]['title']}" for k in sorted(iss, key=lambda x: int(x.split('-')[1]))) + f"; every one in state Backlog with no assignee, created by Leonard between {when(min(r['created_at'] for r in iss.values()))} and {when(max(r['created_at'] for r in iss.values()))}.",
     "VERIFIED: description cut from the project row; 37 counted from the issue rows (project_id), states and assignees read on each", UNSC, dep("hub"), f"{L(proj['id'])}, {L('ENG-2438')}")

gr = rows("gdocs.docs_documents", document_id=I["ground_rules"]) or [r for r in rows("gdocs.docs_documents") if I["ground_rules"] in json.dumps(r)]
grt = clean(gr[0]["body_text"])
GRQ = ["The LLC is the new one Blake and I are setting up for the three of us",
       "anything Harmony Games owns (the games with their art and listings, and the equipment) comes to it only through Sunset's sale",
       "Services we keep running just move their billing to the LLC.", "The plan runs March 1 to May 31.",
       "Domino Delights and Zombie Match come over only if what each made in January, going by the warehouse's daily revenue table, covers what its own hosting bills now, whatever we said about them before.",
       "Combo Fighter comes over either way, it's the reason we're doing this.", "A game that comes over brings what it needs to keep running, its accounts and its player support.",
       "Cost every item at what it bills now, going by whoever runs it, not by what HG used to pay.",
       "What we already decided to keep or cancel for the shutdown in #winddown stays decided.",
       "this plan is only what bills us every month, no one-offs or yearly fees.", "How things move is on the LLC card on our board."]
gdf = rows("gdrive.drive_files", id=I["ground_rules"])[0]
fact("rules", "The ground rules: vehicle, window, take test, costing, keep/cancel, monthly only", "Google Docs (Drive)", tools("gdrive_search", "gdocs_get_document_text"),
     "the Doc titled 'LLC ground rules (Combo Fighter and whatever else we take)'", 'prompt ("make the call on every item the way he lays it out": the DM it hands over says "the ground rules doc has how we decide"); ' + dep("hub") + ' ("the ground rules doc"); search "ground rules"',
     f"{I['ground_rules']}, '{gdf['name']}', owner {gdf['owner_email']}, modified {when(gdf['modified_time'])}. Quotes: " + must(grt, *GRQ),
     "VERIFIED: every quote cut from body_text", SY, dep("hub"), f"{I['ground_rules']}, {L(I['ground_rules'])}")

card = rows("trello.trello_cards", id=I["trello_card"])[0]
cd = clean(card["desc"])
CARDQ = ["Robert makes the call on each item in the Linear project.", "Whoever runs an item today moves it.",
         "Anything that comes through Sunset's sale moves when the sale closes.", "Anything that already has its own deadline keeps it; everything else moves by March 1."]
fact("card", "The LLC card: who moves an item and by when", "Trello", tools("trello_search", "trello_get_card"), "the card 'LLC: what we take from HG' on the Harmony Games board",
     dep("rules") + ' ("the LLC card on our board"); search "LLC: what we take"',
     f"Card {I['trello_card']}, '{card['name']}'. Quotes: " + must(cd, *CARDQ), "VERIFIED: quotes cut from the card desc", UNSC, dep("rules"), f"{I['trello_card']}, {L(I['trello_card'])}")

dsf = rows("gdrive.drive_files", id=I["draft_sheet"])[0]
grid = json.loads(rows("gsheets.sheets_sheets")[0]["grid_json"])
assert grid[0] == ["Item", "Game", "Decision", "Monthly cost", "Paid by", "Next step", "Owner", "By"]
fact("draft", "Leonard's draft: the layout (8 columns) and its stale numbers", "Google Sheets (Drive)", tools("gdrive_search", "gsheets_get_spreadsheet", "gsheets_values_get"),
     "the sheet 'LLC 90 days (draft)'", dep("hub") + ' ("my draft from Tuesday"); search "LLC 90 days"',
     f"{I['draft_sheet']}, '{dsf['name']}', owner {dsf['owner_email']}, created {when(dsf['created_time'])} (Tuesday). Header: " + " / ".join(grid[0]) + ". Rows: "
     + " ; ".join(" / ".join(c for c in r if c) for r in grid[1:]) + ".",
     "VERIFIED: header and cells read from grid_json; the ~1000, 300, ~300 and Figma LLC cells are superseded (F-rows below)", SY, dep("hub"), f"{I['draft_sheet']}, {L(I['draft_sheet'])}")

nd = rows("gdocs.docs_documents")
ndt = [clean(r["body_text"]) for r in nd if "LLC notes" in clean(r["body_text"])][0]
ndf = rows("gdrive.drive_files", id=I["notes_doc"])[0]
fact("notes", "Superseded: Leonard's Monday notes", "Google Docs (Drive)", tools("gdrive_search", "gdocs_get_document_text"), "the Doc titled 'LLC notes (Monday)'", 'search "LLC notes"',
     f"{I['notes_doc']}, created {when(ndf['created_time'])}. Quotes: " + must(ndt, "Calm Play could hold it.", "DD and ZM both come with CF.", "Servers about $1k a month, Blake is looking at it."),
     "VERIFIED: quotes cut from body_text; overturned by the later ground rules ('whatever we said about them before')", SY, "—", f"{I['notes_doc']}, {L(I['notes_doc'])}")

split = GM["robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>"]
SPQ = ["each of the three of us carries a third of what the LLC costs a month, March through May",
       "that's everything on the plan that bills monthly, including what one of us already pays for it",
       "whatever one of us already pays personally counts toward his third, and he puts the difference in as cash", "put the three shares on the sheet per month."]
fact("split", "The split rule: a third each, carried costs count toward a third", "Gmail (Robert's INBOX)", tools("gmail_search_messages", "gmail_get_message"),
     "the mail 'LLC money' from Leonard Hayes", dep("hub") + ' ("I\'ll email you how we split the money"); search "LLC money"',
     f"Thread {I['split_thread']}, sent {when(split['date'])} by leonard.hayes@harmonygames.co. Quotes: " + must(clean(split["body_text"]), *SPQ),
     "VERIFIED: quotes cut from body_text", SY, dep("hub"), f"{I['split_thread']}, {L(split['id'])}")

ev = rows("gcal.gcal_events", event_id="evt_f5f279f282d20ec86bb8e5")[0]
fact("monday", "Monday's call", "Google Calendar (Robert's calendar)", tools("gcal_search_events", "gcal_list_events"), "Robert's calendar, the event 'LLC: decide'", 'prompt ("Monday\'s call")',
     f"evt_f5f279f282d20ec86bb8e5, '{ev['summary']}', starts {when(ev['start_ts'])}, created {when(ev['created'])}. Quote: " + must(clean(ev["description"]), "Robert's plan sheet. We agree what we take and the shares."),
     "VERIFIED: fields from the SQL row; the start is a semantic future date after the clock", SY, "—", f"evt_f5f279f282d20ec86bb8e5, {L('evt_f5f279f282d20ec86bb8e5')}")

# ---------------------------------------------------------------- the take test and the costs
rv = OB["revenue_rows"]
tot = {}
for k, r in rv.items():
    if str(r["date"]).startswith("2026-01"):
        t = tot.setdefault(r["game_id"], [0, Decimal(0), Decimal(0), Decimal(0)])
        t[0] += 1
        t[1] += Decimal(str(r["total_revenue_usd"]))
        t[2] += Decimal(str(r["iap_revenue_usd"]))
        t[3] += Decimal(str(r["ad_revenue_usd"]))
assert tot["domino_delights"][0] == tot["zombie_match_3d"][0] == tot["combo_fighter"][0] == 62
from collections import Counter as _C
_pc = _C((r["game_id"], r["platform"]) for r in rv.values() if str(r["date"]).startswith("2026-01"))
assert set(_pc.values()) == {31} and len(_pc) == 6, _pc
assert str(tot["domino_delights"][1]) == "183.11" and tot["zombie_match_3d"][1] == 0 and str(tot["combo_fighter"][1]) == "7.36"
jan = sorted(int(k) for k, r in rv.items() if str(r["date"]).startswith("2026-01"))
fact("revenue", "January 2026 revenue per game (Snowflake only)", "Snowflake", tools("snowflake_describe_table", "snowflake_execute_query"),
     "ANALYTICS.MONETIZATION.REVENUE_DAILY, date 2026-01-01 to 2026-01-31, summed by game_id", dep("rules") + ' ("the warehouse\'s daily revenue table")',
     f"186 rows (62 per game, one per platform per day). Sum of total_revenue_usd: domino_delights 183.11 (iap 68.84 + ads 114.27); zombie_match_3d 0.00; combo_fighter 7.36.",
     f"VERIFIED: rows /tables/12/rows/{jan[0]} to /tables/12/rows/{jan[-1]} read through hg.py get-many; sums recomputed from the 186 rows by recorded calculation (NUMBER(38,2))", UNSC, dep("rules"),
     f"snowflake.json#/tables/12/rows/{jan[0]}, snowflake.json#/tables/12/rows/{jan[-1]}, ANALYTICS.MONETIZATION.REVENUE_DAILY")

ad = SM[I["arthur_dm"]]
r1, p1 = base_msg("dd_aws_1k")
r2, p2 = base_msg("dd_aws_300")
root, proot = base_msg("dm_ra_root")
fact("dd140", "DD's production account bills $140 a month (governing version)", "Slack (Robert's DM with Arthur)", tools("slack_conversations_search_messages", "slack_read_thread"),
     "Robert's DM with Arthur Blake, Arthur's thread reply of Thursday night", 'search "Domino\'s prod account"',
     f"Reply {I['arthur_dm']}, posted {when(ts_iso(ad['ts']))}, under Arthur's root {BASE['dm_ra_root']} of {when(ts_iso(root['ts']))} (a git question). Quote: "
     + must(clean(ad["text"]), "fyi Domino's prod account is down to $140 a month now, one small task and the db at its floor. that's what it bills from March. it's still on HG's AWS bill till then"),
     "VERIFIED: quote cut from the message; later than the three versions in the next fact", SY, "—", f"{I['arthur_dm']}, {L(I['arthur_dm'])}, {BASE['dm_ra_root']}")
c2441 = rows("linear.linear_comments", issue_id="ENG-2441")[0]
fact("dd1k", "Superseded DD hosting figures (~$1k, 300)", "Slack (#winddown) and Linear", tools("slack_read_channel", "linear_list_comments"), "#winddown, Arthur's posts of Feb 9, and the comment on the DD production account issue",
     'search "DD production account"',
     f"{BASE['dd_aws_1k']}, posted {when(ts_iso(r1['ts']))}: " + must(r1["text"], "Looks like DD production account costs ~$1k a month") + f"; {BASE['dd_aws_300']}, posted {when(ts_iso(r2['ts']))}: "
     + must(r2["text"], "Might be easy to get to 300") + f"; ENG-2441 comment {c2441['id']} (Leonard, {when(c2441['created_at'])}): " + must(clean(c2441["body"]), "about $1k a month, Blake thinks he can get it to $300"),
     "VERIFIED: quotes read through hg.py and from the SQL row; all earlier than Arthur's Feb 13 03:10Z reply", SY, "—", f"{BASE['dd_aws_1k']}, {p1}, {BASE['dd_aws_300']}, {p2}, {L(c2441['id'])}")

bill = GM["robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>"]
BQ = ["github, dbt and metabase bill to my Kub card from the next bill", "it's the $100 base now, dbt is $100 and github is back to the $48 team plan",
      "so $248 a month. I'll carry those through May as my part", "the github org itself stays HG's till the data's delivered, I'm just paying the bill, so count it as mine like the other two",
      "bigquery and firebase stay on HG's google account with GA until the data's out", "so there's nothing there for the LLC."]
fact("bill", "Arthur carries Metabase $100, dbt $100, GitHub $48 ($248) through May", "Gmail (Robert's INBOX)", tools("gmail_search_messages", "gmail_get_message"),
     "the mail 'billing moved to my card' from Arthur Blake", 'search "billing moved to my card"',
     f"Thread {I['arthur_thread']}, sent {when(bill['date'])} by arthur.blake@harmonygames.co. Quotes: " + must(clean(bill["body_text"]), *BQ),
     "VERIFIED: quotes cut from body_text; later than Leonard's ENG-2447 'about $300' (00:52Z)", SY, "—", f"{I['arthur_thread']}, {L(bill['id'])}")
rk, pk = base_msg("arthur_kub")
c2447 = rows("linear.linear_comments", issue_id="ENG-2447")[0]
fact("kub", "Arthur's #winddown note and Leonard's stale ~$300", "Slack (#winddown) and Linear", tools("slack_read_channel", "linear_list_comments"), "#winddown, Arthur's post of Feb 12, and the comment on the Metabase issue",
     dep("bill"), f"{BASE['arthur_kub']}, posted {when(ts_iso(rk['ts']))}: " + must(rk["text"], "I'll be moving github,", "and Metabase to my KubLLC card.")
     + f"; ENG-2447 comment {c2447['id']} ({when(c2447['created_at'])}): " + must(clean(c2447["body"]), "about $300 a month with dbt, more or less"),
     "VERIFIED: quotes read through hg.py and from the SQL row; the ~$300 is overturned by the Feb 13 02:35Z mail", SY, dep("bill"), f"{BASE['arthur_kub']}, {pk}, {L(c2447['id'])}")

jk = GM["robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>"]
c2445 = rows("linear.linear_comments", issue_id="ENG-2445")[0]
fact("cf62", "CF's own AWS account bills $62 a month (governing version; ENG-2445's $95 superseded)", "Gmail (Robert's INBOX) and Linear", tools("gmail_search_messages", "gmail_get_message", "linear_list_comments"),
     "the mail 'jenkins' from Arthur Blake, and the comment on the CF backend and auth stacks issue", 'search "jenkins"',
     f"Thread {I['jenkins_thread']}, sent {when(jk['date'])} by arthur.blake@harmonygames.co, cc leonard.hayes@harmonygames.co. Quotes: "
     + must(clean(jk["body_text"]), "moved our jenkins jobs to my own machine tonight. the build boxes are HG's, they can go with the laptops whenever the sale needs them.",
            "so CF's own account bills $62 a month now, just its live stacks. still on HG's AWS bill till March like Domino's.")
     + f" Earlier: ENG-2445 comment {c2445['id']} ({when(c2445['created_at'])}): " + must(clean(c2445["body"]), "runs about $95 a month on HG's AWS bill", "CF stopped calling ZM's phoenix api, it doesn't need ZM's account. I keep an eye on them"),
     "VERIFIED: quotes cut from body_text and the comment; the mail (04:20Z) is later than the comment (00:58Z) and gives the reason the figure fell", SY, "—", f"{I['jenkins_thread']}, {L(jk['id'])}, {L(c2445['id'])}")

# ---------------------------------------------------------------- the line outside Linear: the VO campaign
vr, vp = base_msg("vo_root")
vb, vbp = base_msg("vo_budget")
vo = SM[I["vo_status"]]
kl, klp = base_msg("keep_live")
fact("vo", "The Meta VO campaign: $3,000 a month cap from March, the new company's card, its own line", "Slack (#prototype)", tools("slack_conversations_search_messages", "slack_read_thread"),
     "#prototype, Leonard's thread under his 'VO campaign is created' post", 'search "VO campaign"',
     f"Root {BASE['vo_root']}, posted {when(ts_iso(vr['ts']))}: " + must(vr["text"], "VO campaign is created and will go live in the next few hours") + f"; {BASE['vo_budget']}: " + must(vb["text"], "Budget is $100/day")
     + f". Reply {I['vo_status']}, posted {when(ts_iso(vo['ts']))}: " + must(clean(vo["text"]), "of the meta campaigns only the VO one is still on", "it's set to $100/day capped at $3,000 a month, and that's what it runs at from March",
                                                                                "it's on my card till the end of Feb and moves to our new company's card from March if we keep CF going, so count it as its own line in what we pay each month")
     + f". Earlier, #executives {BASE['keep_live']} ({when(ts_iso(kl['ts']))}): " + must(kl["text"], "I will keep both campaigns live"),
     "VERIFIED: quotes read through hg.py and cut from the seeded reply; the reply (Feb 12 23:20Z) is the latest", SY, "—", f"{I['vo_status']}, {L(I['vo_status'])}, {BASE['vo_root']}, {vp}, {BASE['vo_budget']}, {vbp}, {BASE['keep_live']}, {klp}")

# ---------------------------------------------------------------- DD player support
asc = GM["robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>"]
c2462 = rows("linear.linear_comments", issue_id="ENG-2462")[0]
pr = rows("github.github_pull_requests")[0]
fact("asc", "App Review rejects Domino Delights' email-only support (governing version)", "Gmail (Robert's INBOX)", tools("gmail_search_messages", "gmail_get_message"),
     "the App Review mail 'We noticed an issue with your submission.' about Domino Delights", 'search "Domino Delights"',
     f"Thread {I['asc_thread']}, sent {when(asc['date'])}, signed 'App Review'. Quotes: " + must(clean(asc["body_text"]), "Best regards,\nApp Review", "App Name: Domino Delights", "Guideline 1.5 - Safety - Developer Information",
                                                                                       "The support option in the app only opens an email draft, and on a device without a mail account set up it does nothing, so users can't reach you from the app.",
                                                                                       "Please add a support URL or another way to contact you in the app."),
     "VERIFIED: quotes cut from body_text; later (07:30Z) than Arthur's 'done' (01:30Z)", SY, "—", f"{I['asc_thread']}, {L(asc['id'])}")
hs, hsp = base_msg("helpshift_feb28")
c2461 = rows("linear.linear_comments", issue_id="ENG-2461")[0]
fact("support", "DD player support: Arthur's 'done', PR #1917 and Helpshift's Feb 28", "Linear, GitHub and Slack (#winddown)", tools("linear_list_comments", "github_get_pull_request", "slack_read_channel"),
     "the comments on the 'Domino Delights player support' and 'Helpshift' issues, the GameOfDominoes pull request 'Replace Helpshift with support email', #winddown's Helpshift post", dep("project") + '; search "Helpshift"',
     f"ENG-2462 comment {c2462['id']} (Arthur, {when(c2462['created_at'])}): " + must(clean(c2462["body"]), "done, support goes to the email address now and Helpshift is out of DD (merged in #1917)")
     + f". {pr['id']} '{pr['title']}', merged {when(pr['merged_at'])}. ENG-2461 comment {c2461['id']} ({when(c2461['created_at'])}): " + must(clean(c2461["body"]), "DD and ZM have to be off it before Feb 28th", "CF was never on it")
     + f". {BASE['helpshift_feb28']} ({when(ts_iso(hs['ts']))}): " + must(hs["text"], "We gotta move domino delights and zombie match off Helpshift before Feb 28th."),
     "VERIFIED: quotes from the SQL rows and read through hg.py; the 'done' is overturned by the App Review mail of the fact above; Feb 28 is a semantic future deadline", SY, dep("project"),
     f"{L(c2462['id'])}, {L(pr['id'])}, {L(c2461['id'])}, {BASE['helpshift_feb28']}, {hsp}")

# ---------------------------------------------------------------- layer.ai, Calm Play, Figma, AppsFlyer, the #winddown decisions
lp = SM[BASE["layer_mar3"]] if BASE["layer_mar3"] in SM else None
lr, lrp = base_msg("layer_mar3")
lrep = SM[I["layer_reply"]]
c2454 = rows("linear.linear_comments", issue_id="ENG-2454")[0]
fact("layer", "layer.ai: access to Mar 3; Robert pulls CF's concept art out himself; the account just lapses", "Slack (#prototype) and Linear", tools("slack_read_channel", "slack_read_thread", "linear_list_comments"),
     "#prototype, Leonard's 'canceled layer.ai account' post and its thread, and the comment on the layer.ai issue", 'search "layer.ai"',
     f"Root {BASE['layer_mar3']}, posted {when(ts_iso(lr['ts']))}: " + must(lr["text"], "account", "we have access until March 3rd") + f". Reply {I['layer_reply']}, posted {when(ts_iso(lrep['ts']))}, mentioning Robert: "
     + must(clean(lrep["text"]), "the CF character concept art is only in layer.ai, can you pull it out yourself before then?", "the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses")
     + f". ENG-2454 comment {c2454['id']} ({when(c2454['created_at'])}): " + must(clean(c2454["body"]), "cancelled it on the 11th"),
     "VERIFIED: quotes read through hg.py and from the SQL rows; Mar 3 is a semantic future date (access end)", SY, "—", f"{BASE['layer_mar3']}, {lrp}, {I['layer_reply']}, {L(I['layer_reply'])}, {L(c2454['id'])}")
cs_, csp = base_msg("calm_sub")
c2472 = rows("linear.linear_comments", issue_id="ENG-2472")[0]
fact("calm", "Calm Play LLC is HG's subsidiary; the LLC is the new one", "Slack (#admin_foundersonly) and Linear", tools("slack_conversations_search_messages", "linear_list_comments"),
     "#admin_foundersonly, Leonard's Dec 2023 post on the Calm Play setup, and the comment on the Calm Play LLC issue", 'search "calm play"',
     f"{BASE['calm_sub']}, posted {when(ts_iso(cs_['ts']))}: " + must(cs_["text"], "make calm play full subsidiary of Harmony Games") + f". ENG-2472 comment {c2472['id']} ({when(c2472['created_at'])}): "
     + must(clean(c2472["body"]), "Calm Play could just be our LLC") + ". Overturned by the ground rules (F3): 'The LLC is the new one Blake and I are setting up for the three of us' (doc modified 23:46Z, after the comment at 23:41Z).",
     "VERIFIED: quotes read through hg.py and from the SQL row", SY, dep("rules"), f"{BASE['calm_sub']}, {csp}, {L(c2472['id'])}")
fg, fgp = base_msg("figma_sep11")
c2453 = rows("linear.linear_comments", issue_id="ENG-2453")[0]
fact("figma", "Figma stays HG's (prepaid to Sep 11); the draft's Figma LLC row is superseded", "Slack (#winddown) and Linear", tools("slack_read_channel", "linear_list_comments"), "#winddown, Robert's Figma post, and the comment on the Figma issue",
     dep("draft") + '; search "Figma"',
     f"{BASE['figma_sep11']}, posted {when(ts_iso(fg['ts']))}: " + must(fg["text"], "Our Figma is good until September 11th") + f". ENG-2453 comment {c2453['id']} ({when(c2453['created_at'])}): "
     + must(clean(c2453["body"]), "HG prepaid it to Sep 11, it stays HG's and just lapses then. nothing for the LLC to take or pay"),
     "VERIFIED: quotes read through hg.py and from the SQL row; later than the draft (Feb 10)", SY, dep("draft"), f"{BASE['figma_sep11']}, {fgp}, {L(c2453['id'])}")
af, afp = base_msg("appsflyer")
fact("appsflyer", "AppsFlyer free tier for CF, set up by Leonard", "Slack (#winddown) and Linear", tools("slack_read_channel", "linear_list_comments"), "#winddown, Leonard's attribution post, and the comment on the AppsFlyer issue", dep("project"),
     f"{BASE['appsflyer']}, posted {when(ts_iso(af['ts']))}: " + must(af["text"], "offers data for free up to 15K installs") + ". ENG-2451 comment: "
     + must(clean(rows("linear.linear_comments", issue_id="ENG-2451")[0]["body"]), "CF goes on appsflyer's free tier from March", "I'll set CF up on it"),
     "VERIFIED: quotes read through hg.py and from the SQL row", SY, dep("project"), f"{BASE['appsflyer']}, {afp}, {L(rows('linear.linear_comments', issue_id='ENG-2451')[0]['id'])}")
kp, kpp = base_msg("keep_list")
ai, aip = base_msg("action_items")
fact("winddown", "What #winddown already decided to keep or cancel", "Slack (#winddown)", tools("slack_read_channel"), "#winddown, Leonard's keep list and action items of Feb 12", dep("rules") + ' ("#winddown")',
     f"{BASE['keep_list']}, posted {when(ts_iso(kp['ts']))}: " + must(kp["text"], "During shutdown, let’s keep Deel, gusto, Intuit. I canceled other subscriptions under mine.", "linear we keep during transition")
     + f"; {BASE['action_items']}, posted {when(ts_iso(ai['ts']))}: " + must(ai["text"], "to cancel", "coderabbit, cursor", "We keep accounts that has our data such as Slack, google, google analytics, github under Harmony Games until the data is extracted"),
     "VERIFIED: quotes read through hg.py", SY, dep("rules"), f"{BASE['keep_list']}, {kpp}, {BASE['action_items']}, {aip}")
au, aup = base_msg("auction")
fact("auction", "HG's IP goes to auction; the LLC buys what is left", "Slack (#executives)", tools("slack_read_channel"), "#executives, Leonard's post after Wednesday's call", dep("rules") + ' ("the way I wrote after the call on Wednesday")',
     f"{BASE['auction']}, posted {when(ts_iso(au['ts']))}: " + must(au["text"], "we wil put our IP to auction and if no one buys it we can buy via our LLC"),
     "VERIFIED: quote read through hg.py (spelling as in the record)", SY, dep("rules"), f"{BASE['auction']}, {aup}")
ua, uap = base_msg("unity_100")
fact("oneoffs", "One-offs and non-monthly fees outside the plan: playable vendor $3,750, the Unity Ads $100, Carta's 8/15 renewal, Google Play's one-time fee", "Linear and Slack (#prototype)", tools("linear_list_comments", "slack_read_channel"),
     "the comments on the Playable vendor, Unity Ads balance, Carta and Google Play developer account issues, and #prototype's Unity post", dep("project"),
     "ENG-2474: " + must(clean(rows("linear.linear_comments", issue_id="ENG-2474")[0]["body"]), "$3,750 for the first playable, one-off") + "; ENG-2473: "
     + must(clean(rows("linear.linear_comments", issue_id="ENG-2473")[0]["body"]), "the $100 left on it goes on this week's playable test, then nothing") + "; ENG-2469: "
     + must(clean(rows("linear.linear_comments", issue_id="ENG-2469")[0]["body"]), "renewal is 8/15") + "; ENG-2471: " + must(clean(rows("linear.linear_comments", issue_id="ENG-2471")[0]["body"]), "one-time fee, nothing monthly")
     + f"; {BASE['unity_100']} ({when(ts_iso(ua['ts']))}): " + must(ua["text"], "happy to spend $100 we have on this"),
     "VERIFIED: quotes from the SQL rows and read through hg.py", SY, dep("project"), f"{L(rows('linear.linear_comments', issue_id='ENG-2474')[0]['id'])}, {L(rows('linear.linear_comments', issue_id='ENG-2473')[0]['id'])}, {BASE['unity_100']}, {uap}")

# ---------------------------------------------------------------- people and places
assert all(r["creator_id"] == "usr_63fffeb4fab5233e" for r in iss.values())
_cm = rows("linear.linear_comments")
nL = sum(1 for c in _cm if c["author_id"] == "usr_63fffeb4fab5233e")
nA = sum(1 for c in _cm if c["author_id"] == "usr_cc3e90160f490686")
assert nL + nA == 37
aiss = sorted({c["issue_id"] for c in _cm if c["author_id"] == "usr_cc3e90160f490686"}, key=lambda x: int(x.split("-")[1]))
ur, ul, ua_ = OB["misc"]["u_robert"]["rec"], OB["misc"]["u_leonard"]["rec"], OB["misc"]["u_arthur"]["rec"]
assert (ur["id"], ul["id"], ua_["id"]) == ("usr_Robert", "usr_63fffeb4fab5233e", "usr_cc3e90160f490686")
fact("users", "Linear users for the assignees", "Linear", tools("linear_list_users"), "Linear users Robert, Leonard Hayes, Arthur Blake", dep("project"),
     f"Robert: id {ur['id']}, {ur['email']}; Leonard: id {ul['id']}, {ul['email']}; Arthur: id {ua_['id']}, {ua_['email']}. On the 37 issues Leonard ({ul['id']}) is the creator of all 37 and wrote {nL} comments; Arthur ({ua_['id']}) wrote {nA} ({', '.join(aiss)}).",
     "VERIFIED: users read through hg.py (linear data.json /users/26, /users/13, /users/35)", UNSC, dep("project"), "linear data.json#/users/26, linear data.json#/users/13, linear data.json#/users/35")
fact("states", "The three target states exist for team ENG", "Linear", tools("linear_list_issue_statuses"), "team ENG's issue statuses", dep("project"),
     "State names 'Todo', 'Done' and 'Canceled' are live values on ENG issues in the base (e.g. linear data.json /issues/204 'Todo', /issues/0 'Done', /issues/40 'Canceled'); the 37 project issues start in 'Backlog'.",
     "VERIFIED: values read through hg.py search (linear, 'Todo' 102, 'Done' 196, 'Canceled' 200 state_id hits)", UNSC, dep("project"), "linear data.json#/issues/204/state_id, linear data.json#/issues/0/state_id, linear data.json#/issues/40/state_id")
cl, ca = OB["misc"]["c_leonard"]["rec"], OB["misc"]["c_arthur"]["rec"]
fact("emails", "The two people the sheet is shared with", "Contacts", tools("contacts_search_contacts"), "the contacts Leonard Hayes and Arthur Blake", dep("hub") + ' ("share it with Blake and me")',
     f"Leonard Hayes, {cl['job']}, {cl['email']}; Arthur Blake, {ca['job']}, {ca['email']} ('Blake' in the prompt and the DM).",
     "VERIFIED: read through hg.py (contacts.json /contacts/169, /contacts/168)", UNSC, dep("hub"), "contacts.json#/contacts/169, contacts.json#/contacts/168")
rt = OB["misc"]["root"]["rec"]
fact("root", "Robert's Drive (root folder)", "Google Drive", tools("gdrive_search", "gdrive_list_folder"), "Robert's own Drive root", 'prompt ("my Drive")',
     f"{rt['id']}, name {rt['name']}, {rt['mime_type']}, owner {rt['owner_email']}, no parent.", "VERIFIED: fields read through hg.py (gdrive data.json /drive_files/14368)", SY, "—", f"{rt['id']}, gdrive data.json#/drive_files/14368")

# ---------------------------------------------------------------- one fact per issue: the call and its end state
WHO = {"usr_63fffeb4fab5233e": "Leonard", "usr_cc3e90160f490686": "Arthur", "usr_Robert": "Robert"}
BASIS = {
    "ENG-2438": (["rules", "card", "auction"], "the ground rules: 'Combo Fighter comes over either way'; it comes through Sunset's sale"),
    "ENG-2439": (["rules", "revenue", "dd140", "card"], "January 183.11 covers the $140 DD prod bill"),
    "ENG-2440": (["rules", "revenue"], "January 0.00 covers no hosting; ENG-2443 says its account 'bills every month'"),
    "ENG-2441": (["dd140", "rules", "card"], "DD comes over and brings its accounts; $140 'still on HG's AWS bill till then', so the billing move is left"),
    "ENG-2442": (["rules"], "'nothing runs on dev anymore, shutting it down'"),
    "ENG-2443": (["revenue", "cf62"], "ZM stays; CF 'doesn't need ZM's account'"),
    "ENG-2444": (["rules"], "'kinesis and glue only ever carried DD and ZM events'"),
    "ENG-2445": (["cf62", "rules", "card"], "CF brings its accounts; $62 'still on HG's AWS bill till March', so the billing move is left"),
    "ENG-2446": (["cf62", "rules"], "HG equipment that goes with the laptops in Sunset's sale; the jenkins jobs moved to Arthur's machine"),
    "ENG-2447": (["bill"], "Arthur pays it himself through May ($100)"), "ENG-2448": (["bill"], "Arthur pays it himself through May ($100)"),
    "ENG-2449": (["bill"], "Arthur pays it himself through May ($48), 'count it as mine like the other two'; the project rule's 'even if HG still owns it'"),
    "ENG-2450": (["winddown"], "terminated in #winddown"), "ENG-2451": (["appsflyer", "card"], "the free tier, Leonard sets CF up on it"),
    "ENG-2452": (["winddown", "bill"], "kept under HG until the data is extracted; 'nothing there for the LLC'"),
    "ENG-2453": (["figma"], "prepaid to Sep 11, lapses"), "ENG-2454": (["layer"], "'nothing on the layer account for our new company to take, it just lapses'"),
    "ENG-2455": (["winddown"], "cancelled"), "ENG-2456": (["winddown"], "cancelled"), "ENG-2457": (["winddown"], "cancelled"), "ENG-2458": (["winddown"], "cancelled"),
    "ENG-2459": (["winddown"], "terminated; 'CF is fine on unity personal'"), "ENG-2460": (["winddown"], "cancelled"),
    "ENG-2461": (["support"], "cancelling; 'CF was never on it'"),
    "ENG-2462": (["asc", "support", "rules"], "DD brings its player support; App Review rejected the email-only support, so a support build is left before Feb 28"),
    "ENG-2463": (["winddown"], "kept for the data"), "ENG-2464": (["winddown"], "kept for the data; unused accounts archived after Feb 15"),
    "ENG-2465": (["winddown"], "kept during the transition"), "ENG-2466": (["winddown"], "kept during the shutdown"), "ENG-2467": (["winddown"], "kept during the shutdown"),
    "ENG-2468": (["winddown"], "kept during the shutdown"), "ENG-2469": (["oneoffs"], "HG's cap table; a renewal on 8/15, not a monthly bill"), "ENG-2470": (["rules"], "HG's account; CF's listing moves with the game"),
    "ENG-2471": (["oneoffs"], "a one-time fee"), "ENG-2472": (["calm", "rules"], "HG's subsidiary; the LLC is the new one"),
    "ENG-2473": (["oneoffs"], "a one-off"), "ENG-2474": (["oneoffs"], "a one-off"),
}
NAME = {v: k for k, v in ISSUE.items()}
issue_facts = []
for eng in sorted(iss, key=lambda x: int(x.split("-")[1])):
    r = iss[eng]
    t = TRUTH[NAME[eng]]
    st = {"LLC": "Todo", "Founder": "Done", "HG": "Canceled"}[t["Decision"]]
    cm = rows("linear.linear_comments", issue_id=eng)
    assert len(cm) == 1
    c = cm[0]
    basis_keys, why = BASIS[eng]
    owner = t["Owner"] if st == "Todo" else None
    tail = f"End state: {st}" + (f", assignee {owner}" if owner else "") + "."
    extra = ""
    if t["Monthly cost"]:
        extra += f" Monthly cost {t['Monthly cost']}, paid by {t['Paid by']}."
    if t["By"] not in ("-", ""):
        extra += f" Next step: {t['Next step']}; by {t['By']}."
    fact("issue:" + eng, f"{eng} {r['title']}: {t['Decision']}", "Linear", tools("linear_list_issues", "linear_list_comments"), f"the issue '{r['title']}' in the LLC take-over project", dep("project"),
         f"{eng} '{r['title']}', state Backlog, no assignee. Comment {c['id']} ({WHO.get(c['author_id'], c['author_id'])}, {when(c['created_at'])}): '{clean(c['body'])}'. Call: {t['Decision']} ({why}).{extra} {tail}",
         "VERIFIED: title, state and comment from the SQL rows; call and end state not_a_claim (derived from the Depends-on facts and the project rule)", UNSC,
         dep(*(["project"] + basis_keys)), f"{L(eng)}, {L(c['id'])}")
    issue_facts.append("issue:" + eng)

vt = TRUTH["Combo Fighter VO campaign"]
fact("vo_issue", "The missing plan line: a new issue for the CF VO campaign", "Linear (new issue)", tools("linear_create_issue"), "the LLC take-over project, team ENG", dep("project", "vo"),
     f"No issue among the 37 names the VO campaign (titles listed in F2's issues); the project holds 'One issue per thing the LLC might take from HG or pay for'. New issue: a title naming the VO / Meta campaign, project LLC take-over, team ENG, state Todo, assignee Leonard; monthly cost {vt['Monthly cost']}, paid by the LLC from March (Leonard's card through Feb).",
     "VERIFIED: the 37 titles read from the SQL rows (none names VO, Meta or a campaign); new-issue fields not_a_claim (derived from F2 and F14)", UNSC, dep("project", "vo"), f"{L(proj['id'])}, {I['vo_status']}, {L(I['vo_status'])}")
import re as _re
assert not any(_re.search(r"\bvo\b|\bmeta\b|campaign|\bads? campaign", r["title"].lower()) for r in iss.values())

tot_m = sum(TRUTH[k]["Monthly cost"] for k in TRUTH if isinstance(TRUTH[k], dict) and "Monthly cost" in TRUTH[k])
assert tot_m == 3450
fact("totals", "The monthly total and the three shares", "derived (Linear, Slack, Gmail)", "none (calculation over the rows)", "the 38 plan rows above", dep("split", "dd140", "cf62", "bill", "vo"),
     "Monthly lines: DD prod account 140 + CF backend and auth stacks 62 + CF VO campaign 3,000 + Metabase 100 + dbt 100 + GitHub 48 = 3,450 a month; every other row 0. A third each: 1,150. Arthur already carries 248, so he puts in 902 cash; Leonard 1,150 cash; Robert 1,150 cash. LLC-billed cash 3,202 a month (140 + 62 + 3,000). Decisions: LLC 7 rows, Arthur (founder) 3, HG 28.",
     "not_a_claim (derived): recomputed from the cited figures; 140 + 62 + 3000 + 100 + 100 + 48 = 3450; 3450 / 3 = 1150; 1150 - 248 = 902", "derived",
     ", ".join(fid_of[k] for k in ["split", "dd140", "cf62", "bill", "vo"] + issue_facts), f"solver/truth.json, {I['split_thread']}, {I['vo_status']}")

# ---------------------------------------------------------------- requirements
def span(s):
    assert s in PROMPT, s
    return s


ALLI = ", ".join(fid_of[k] for k in issue_facts)
REQ = [
    (span("Leonard sent me a DM on Thursday night about setting up the LLC so we can keep Combo Fighter going after the shutdown"), "Discovery — Leonard's Thursday-night DM is the source of every ask", "Explicit", F("hub")),
    (span("Can you take care of what he asked for?"), "Discovery — the DM's incorporated records: the ground rules, the draft's layout, the split mail, Drive, sharing, the reply", "Implicit (through F1)", F("hub", "rules", "draft", "split", "card")),
    (span("Go through the LLC project in Linear"), "Discovery — the 37 issues and each issue's comment", "Explicit", F("project") + ", " + ALLI),
    (span("make the call on every item the way he lays it out"), "Discovery — a call per item under the ground rules, the card and the project rule, with the governing version of every figure", "Implicit (incorporated through F1 and F3)",
     F("rules", "card", "revenue", "dd140", "dd1k", "bill", "kub", "cf62", "vo", "asc", "support", "layer", "calm", "figma", "appsflyer", "winddown", "auction", "oneoffs", "notes") + ", " + ALLI),
    (span("leave the call on each issue so he and Blake can see it there"), "Write — a comment with the call on each of the 37 issues (and on the new VO issue)", "Explicit", ALLI + ", " + F("vo_issue")),
    (span("Put the plan sheet in my Drive, laid out like his draft"), "Write — a new sheet in Robert's Drive with the draft's 8 columns, one row per item, and the three shares per month", "Explicit (shares through F7)", F("draft", "root", "split", "totals") + ", " + ALLI),
    (span("share it with both of them"), "Write — share the sheet with Leonard and Arthur", "Explicit", F("emails")),
    (span("When you're done, the project should match the sheet."), "Write — each issue moved per the project rule (Todo + assignee / Done / Canceled) and a new issue for the plan line the project lacks", "Explicit (rule through F2)",
     F("project", "users", "states", "vo_issue") + ", " + ALLI),
    (span("Then reply to him in that DM thread with what I'd do and what it costs each of us a month, with the link to the sheet."), "Write and Tell — a thread reply under Leonard's DM: Robert's calls, $1,150 each a month (Arthur $902 cash), the sheet link", "Explicit", F("hub", "totals", "revenue", "asc")),
    (span("I want my answer ready before Monday's call"), "Constraint — every write is done now, before the call of Mon Feb 16", "Explicit", F("monday")),
]

# ---------------------------------------------------------------- write capability and the defer search
def dcount(k):
    return DEF[k]["visible"]


late = []
for k, v in DEF.items():
    if k == "sql":
        continue
    for h in v.get("feb_2026", []):
        late.append((k, h["file"], h["pointer"], h["text"][:80]))
for k, v in DEF.items():
    if k != "sql":
        assert v["complete"] in (True, None) or v["complete"], k
        assert not v["hit_limit"], k
DEFER = ("slack · gmail · linear · trello (Robert's channels, DMs and mailbox through persona_view search; all of Linear and Trello through hg.py search; the seeded SQL rows by text): "
         "'hold off', 'not yet', 'don't move', 'wait for', 'wait until', 'don't share', 'don't reply', 'on hold', 'before you move' (limit 3000, no search hit its limit) — population complete: "
         f"slack {sum(dcount(k) for k in DEF if k.startswith('slack:'))} hits, gmail {sum(dcount(k) for k in DEF if k.startswith('gmail:'))}, linear {sum(dcount(k) for k in DEF if k.startswith('linear:'))}, trello {sum(dcount(k) for k in DEF if k.startswith('trello:'))}, SQL {sum(DEF['sql'].values())}; "
         f"linear's hits all on base issues outside the LLC project (its seeded rows carry none of the terms); {len(late)} hits dated Feb 12 to 13 2026, none about the LLC project, the plan sheet or the reply (each read, Self-review); governing version: Leonard's DM {I['hub']} (Feb 13 05:40Z) is the latest instruction and the split mail (06:10Z) adds no hold; result: no defer")
WR = [
    ("R5", "Comment the call on each issue (37) and on the new VO issue", '"leave the call on each issue so he and Blake can see it there"', tools("linear_create_comment") + " (exists)", "issueId, body", ALLI + ", " + F("vo_issue"),
     "one comment on each of ENG-2438 to ENG-2474, plus one on the new issue", "the call with its reason"),
    ("R6", "Create the plan sheet and write its rows", '"Put the plan sheet in my Drive, laid out like his draft"', tools("gsheets_create_spreadsheet", "gsheets_values_update") + " (exist)", "title; spreadsheetId, range, values",
     F("root", "draft", "totals"), f"a native sheet in Robert's Drive root ({rt['id']}; a sheet created with no folder lands there), header + 38 rows + the shares", "the 8 columns; one row per item; the three shares per month"),
    ("R7", "Share the sheet with Leonard and Arthur (2)", '"share it with both of them"', tools("gdrive_share_file") + " (exists)", "fileId, emailAddress, role", F("emails"), "both addresses hold a permission on the sheet", "—"),
    ("R8", "Move each issue to match the sheet (37)", '"When you\'re done, the project should match the sheet."', tools("linear_update_issue") + " (exists)", "id, state, assignee", ALLI + ", " + F("users", "states"),
     "7 LLC rows' issues (6 base + the new one) Todo with the mover assigned; ENG-2447, ENG-2448, ENG-2449 Done; the other 28 Canceled", "state and assignee only"),
    ("R8", "Create the missing VO campaign issue", '"When you\'re done, the project should match the sheet."', tools("linear_create_issue") + " (exists)", "team, title (+ project, state, assignee)", F("vo_issue", "users"),
     "created in the LLC take-over project, state Todo, assignee Leonard (new issue: state_history_json an empty array at load)", "a title naming the VO campaign"),
    ("R9", "Reply to Leonard in the DM thread", '"Then reply to him in that DM thread"', tools("slack_send_message") + " (exists)", "channel, text, thread_ts", F("hub", "totals"),
     f"posted under {I['hub']} (thread_ts 1770961200.890407), after the other writes", "what Robert would do; $1,150 each a month (Arthur's $902 cash optional); the sheet link"),
]

# ---------------------------------------------------------------- traps, risks
TRAPS = [
    ("T1", f"The project list has no VO campaign issue ({fid_of['project']}, {proj['id']})", F("vo"), f"Leonard's #prototype reply {I['vo_status']}: 'count it as its own line in what we pay each month'; the project scope 'or pay for'"),
    ("T2", f"ENG-2462's 'done' note and PR #1917 merged ({c2462['id']}, {pr['id']})", F("asc"), f"App Review mail {I['asc_thread']}, Feb 13 07:30Z, later than the note (01:30Z)"),
    ("T3", f"DD hosting ~$1k / 300 ({BASE['dd_aws_1k']}, {BASE['dd_aws_300']}, {c2441['id']}, the draft)", F("dd140"), f"Arthur's reply {I['arthur_dm']}, Feb 13 03:10Z: '$140 a month now'"),
    ("T4", f"CF stacks 'about $95' on ENG-2445 ({c2445['id']})", F("cf62"), f"Arthur's mail {I['jenkins_thread']}, Feb 13 04:20Z: 'bills $62 a month now'"),
    ("T5", f"Metabase + dbt ~$300 ({c2447['id']}, the draft)", F("bill"), f"Arthur's mail {I['arthur_thread']}, Feb 13 02:35Z: '$248 a month'"),
    ("T6", f"The draft's Figma LLC row ({I['draft_sheet']})", F("figma"), f"ENG-2453 {c2453['id']} and {BASE['figma_sep11']}: prepaid to Sep 11, stays HG's"),
    ("T7", f"'Calm Play could just be our LLC' ({c2472['id']}) and the notes doc ({I['notes_doc']})", F("calm", "rules"), f"{BASE['calm_sub']}: a full subsidiary of Harmony Games; the ground rules 'The LLC is the new one'"),
    ("T8", f"The notes doc's 'DD and ZM both come with CF' ({I['notes_doc']})", F("rules", "revenue"), f"ground rules {I['ground_rules']}: the January revenue test, 'whatever we said about them before'"),
    ("T9", f"ENG-2454's 'cancelled it on the 11th' with no step ({c2454['id']})", F("layer"), f"Leonard's reply {I['layer_reply']}: Robert pulls the art out before Mar 3"),
    ("T10", f"The playable vendor's $3,750 and the Unity Ads $100 ({BASE['unity_100']})", F("oneoffs", "rules"), f"ground rules {I['ground_rules']}: 'no one-offs or yearly fees'"),
    ("T11", f"BoomBit's DD test and retention update ({BASE['boombit_retention']}, {BASE['dd_boombit']})", F("issue:ENG-2439"), "ENG-2439: 'boombit's test doesn't change anything, the game is ours'"),
    ("T12", f"Arthur's $248 read as cost on top of a third ({I['split_thread']})", F("split", "totals"), f"split mail {I['split_thread']}: 'counts toward his third, and he puts the difference in as cash'"),
]
RISKS = [
    ("1", "The new VO issue's title is free; the brief accepts any title naming the VO / Meta campaign or CF ads", F("vo_issue"), "rubric", "grade the issue's project, state and assignee, not its title wording"),
    ("2", "The layer.ai export step may sit on the layer.ai row or the Combo Fighter row ('the art goes with CF'); brief 4b accepts either", F("layer", "issue:ENG-2454", "issue:ENG-2438"), "rubric / OE accuracy", "an OE that names one row does not exclude the other"),
    ("3", "Per-person cost: $1,150 each (a third); Arthur's $902 is cash after his $248, not his cost (platform /prompt rev3 DR1)", F("totals", "split"), "rubric", "accept $1,150 each with or without the cash split"),
    ("4", "GitHub reads either as Done (Arthur pays it through May) or Canceled (HG keeps the org); settled Done by the project rule's 'even if HG still owns it' and Arthur's 'count it as mine'", F("issue:ENG-2449", "bill"), "UGT (settled)", "none"),
    ("5", "Assignee values: the six baseline runs passed names, 'me', emails and usr_ ids to linear_update_issue and all succeeded", F("users"), "OE accuracy", "the OE names people, not a format"),
    ("6", "gsheets_create_spreadsheet has an optional driveFileId; with none the sheet lands in the owner's root; all six baseline sheets were created without one", F("root"), "OE accuracy", "name Robert's Drive root as the place"),
    ("7", "One baseline sent the reply with Leonard's user id as the channel and the right thread_ts; the DM channel is the one in F1's id", F("hub"), "OE accuracy", "name the DM thread under Leonard's message"),
    ("8", "The DD support By: Feb 28 is Helpshift's own deadline (ENG-2461, #winddown); brief 4b accepts any Feb 15 to 28 date or 'by/before Feb 28'", F("support", "issue:ENG-2462"), "rubric", "accept the window"),
]

# ---------------------------------------------------------------- visibility proof
brow = [" | ".join(str(c) for c in f) for f in FACTS]
need = sorted({x for r in brow for _, x in G.scoped_ids(r)})
seeded = [x for x in need if x in LINE]
base = [x for x in need if x not in LINE]
lbf = os.path.join(HERE, "oe_lb_ids.txt")
open(lbf, "w").write("\n".join(seeded) + "\n")
cs_txt = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "check-sql", PERSONA, f"{TDREL}/01_Universe_Inject.sql", "--load-bearing", f"{TDREL}/Working_Files/plan/oe_lb_ids.txt"])
yes_rows = [ln for ln in cs_txt.splitlines() if ln.startswith("[YES LB]") and any(x in ln for x in seeded)]
verdict = [ln for ln in cs_txt.splitlines() if ln.startswith("verdict:")]
svc_of = {x: s for r in brow for s, x in G.scoped_ids(r)}
base += [x for x in seeded if not any(x in ln for ln in yes_rows)]
cansee = []
for x in base:
    out = run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "can-see", PERSONA, svc_of[x], x]).splitlines()
    cansee.append(out[0] if out else f"{PERSONA} {svc_of[x]} {x}: UNVERIFIED")
bad = [c for c in cansee if ": YES" not in c]
assert not bad, bad

# ---------------------------------------------------------------- write
O = []
A = O.append
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
clock = ctx["universe"]["clock_line"].replace("Clock: ", "")
freeze = ctx.get("freeze_utc") or ctx["universe"].get("freeze_utc")
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]  # noqa: E731
A("# 08 OE Writing Ledger — robert_llc_takeover (LLC take-over of Combo Fighter, injection rev4)")
A(f"Generated 2026-11-06 · Clock {clock} · seed bound {freeze} · Persona Robert robert@harmonygames.co (Co-founder & Creative Director) · Tier Long-Horizon · Mode Easy")
A(f"Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all {len(WR)} write families map to cataloged tools, friction is none")
A(f"Inputs read: 04_Prompt.txt — present (sha256 {sha(os.path.join(TI, '04_Prompt.txt'))}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present (rev4, sha256 {sha(SQL_PATH)}) · 01_Grounding_Dossier.md — present (leads only) · 01_Scenario_Design.md + 01_Hardness_Manifest.json — present (leads only) · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files — none · 04_Prompt_Writing_Brief.md — present (§4b for SQL f1a290ced176)")
A("")
A("Persona binding: roster entry robert, Robert, Co-founder & Creative Director, robert@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of #winddown, #executives, #prototype, #admin_foundersonly and his DMs with Leonard and Arthur), Calendar (own calendar), Drive, Docs and Sheets (files shared with him and his own root). Unscoped: Linear, Trello, GitHub, Contacts, Snowflake.")
A("")
A("Dates: Pacific first, UTC beside it. 'sent', 'created', 'posted', 'modified' and 'merged' mark record times; every record time below is at or before the seed bound. Semantic future dates: Monday's call (starts Feb 16), the plan window (March 1 to May 31), Helpshift's Feb 28, layer.ai's access end Mar 3 — none is expected as done.")
A("")
A("## A · Requirements (traced to the prompt)")
A("| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |")
A("|---|---|---|---|---|")
for i, (s, typ, ex, fids) in enumerate(REQ, 1):
    A(f'| R{i} | "{s}" | {typ} | {ex} | {fids} |')
A("")
A("## B · Facts")
A('| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search "query text") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |')
A("|---|---|---|---|---|---|---|---|---|---|---|")
for f in FACTS:
    A("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in f) + " |")
A("")
A("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
A("")
A(f"`python3 Task_Authoring/tools/persona_view.py check-sql {PERSONA} {TDREL}/01_Universe_Inject.sql --load-bearing plan/oe_lb_ids.txt` ({len(seeded)} seeded ids; load-bearing rows and the verdict line kept):")
A("")
for ln in yes_rows + verdict:
    A(ln)
A("")
A(f"`python3 Task_Authoring/tools/persona_view.py can-see {PERSONA} (service) (id)` ({len(base)} base ids, first line of each):")
A("")
for ln in cansee:
    A(ln)
A("")
A("## C · Write capability")
A("| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |")
A("|---|---|---|---|---|---|---|---|---|---|")
for w in WR:
    A("| " + " | ".join(w) + f" | {DEFER} | yes |")
A("")
A("## D · Friction facts")
A("| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |")
A("|---|---|---|---|---|---|")
A("| none | Friction: none (03_Error_Async_Config.txt) | — | — | — | — |")
A("")
A("## E · Traps and distractors")
A("| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |")
A("|---|---|---|---|")
for t in TRAPS:
    A("| " + " | ".join(t) + " |")
A("")
A("## F · Open risks")
A("| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |")
A("|---|---|---|---|---|")
for r in RISKS:
    A("| " + " | ".join(r) + " |")
A("")
A("## G · Tally")
nq = sum(1 for f in FACTS if "VERIFIED" in f[7])
nn = sum(1 for f in FACTS if "not_a_claim" in f[7])
na = sum(1 for f in FACTS if "ABSENCE" in f[7])
A(f"Requirements {len(REQ)} · facts {len(FACTS)} · writes {len(WR)} (feasible {len(WR)}) · friction items 0 · expected values {len(FACTS)} (quoted {nq} · not_a_claim {nn} · ABSENCE-checked {na}) · unverified visibility 0 · blocking 0")
A("")
A("## Self-review")
A("")
A("Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every §B value was re-verified in this run: seeded values from the parsed SQL rows, base values through tools/hg.py (plan/oe_reads.py: lookup + get-many for 25 Slack posts, the 186 January REVENUE_DAILY rows, the Drive root, two contacts, three Linear users), with each quote asserted as a substring of its record by plan/assemble_oe_ledger.py. The no-event-text scan passes: §B holds facts and dependency edges, no event wording.")
A("")
WHYLATE = {"C07C2866011/1770928015.519659": "Leonard in #executives on the ad campaign's zero impressions (the posts before it: 'maybe Singular redirect links are fucked up somehow', 'it doesn’t make sense to have zero impressions'), not a hold on the LLC work"}
A("Defer search, hits dated Feb 12 to 13 2026 read one by one: " + ("; ".join(f"{k}: {p}, '{t}' ({WHYLATE.get(p, 'a bot status post in a gpt channel, not a hold on any write')})" for k, f, p, t in late) if late else "none") + ".")
A("")
A("| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |")
A("|---|---|---|---|")
CRS = [
    ("R1", "'Thursday night' could mean another Leonard DM, or Thursday Feb 12 in UTC", f"the DM {I['hub']} is Feb 13 05:40Z = Thu Feb 12 9:40pm PT, and it names the LLC project, the ground rules and the draft ({fid_of['hub']})", "holds"),
    ("R2", "'what he asked for' could stop at the Linear calls", f"the same DM also asks for the sheet ('lay the sheet out like my draft'), the shares and the reply ({fid_of['hub']})", "holds"),
    ("R3", "the population could be the issues plus Leonard's notes doc and draft rows", f"the project holds the 37 issues, 'one issue each' ({fid_of['project']}); the draft's rows are superseded figures, not more items ({fid_of['draft']})", "holds (37)"),
    ("R4", "the draft's figures or the notes doc could decide", f"the ground rules: 'Cost every item at what it bills now' and 'whatever we said about them before' ({fid_of['rules']}); each later figure has its own row ({fid_of['dd140']}, {fid_of['cf62']}, {fid_of['bill']})", "holds"),
    ("R5", "the call could go in the issue description instead of a comment", f"the project rule: 'Leave your call on each one as a comment' ({fid_of['project']})", "holds (37 comments + 1)"),
    ("R6", "the sheet could be a copy of Leonard's draft or a tab in it", f"the DM says 'keep it in your drive' and the prompt 'Put the plan sheet in my Drive' ({fid_of['hub']}, {fid_of['root']}); the draft is Leonard's file", "holds"),
    ("R7", "'both of them' could include only Leonard", "the prompt's 'so he and Blake can see it' and the DM's 'share it with Blake and me'", "holds (2)"),
    ("R8", "the VO campaign could stay sheet-only (no issue), and GitHub could be Canceled", f"the project scope 'or pay for' and 'the project should match the sheet' ({fid_of['vo_issue']}); the Done test 'even if HG still owns it' ({fid_of['issue:ENG-2449']})", "holds (new issue; GitHub Done)"),
    ("R9", "the cost each could be Arthur's $902, or the reply could be a new DM message", f"the split mail: a third each, carried costs count toward it ({fid_of['split']}, {fid_of['totals']}); the prompt says 'in that DM thread'", "holds ($1,150 each)"),
    ("R10", "'before Monday's call' could be a deadline after the clock that the agent waits for", f"the call starts Mon Feb 16 ({fid_of['monday']}), after the clock; nothing in the request holds a write until then", "holds"),
]
assert len(CRS) == len(REQ)
for r in CRS:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: none blocking. Open risks §F 1 to 8 go to the draft and rubric stages (VO issue title, the export row, the cost each, GitHub's state, assignee formats, the sheet's default location, the reply channel, the support By window).")
A("")
open(os.path.join(WF, "08_OE_Writing_Ledger.md"), "w").write("\n".join(O) + "\n")
json.dump({"fid": fid_of, "seeded": seeded, "base": base}, open(os.path.join(HERE, "oe_ledger_ids.json"), "w"), indent=1)
print("facts", len(FACTS), "req", len(REQ), "seeded ids", len(seeded), "base ids", len(base), "yes rows", len(yes_rows), "late defer hits", len(late))
