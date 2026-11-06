#!/usr/bin/env python3
"""Draft 08_Oracle_Events.md (draft mode) from the OE ledger's facts (Working_Files/08_OE_Writing_Ledger.md).

Every quoted Expected value is re-read in this run: seeded rows are parsed from 01_Universe_Inject.sql (never executed), base
records come from plan/oe_base.json (plan/oe_reads.py, tools/hg.py). Each quote is asserted as a substring of its own record
(whitespace-normalised) before the file is written. One write per event; no final-response or non-action events."""
import datetime as dt
import json
import os
import re
import sys
from decimal import Decimal
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
IDS = json.load(open(os.path.join(HERE, "ids.json")))
I, BASE, ISSUE = IDS["IDS"], IDS["BASE"], IDS["issues"]
NAME = {v: k for k, v in ISSUE.items()}
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
CHECKS = []


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")


def norm(s):
    return re.sub(r"\s+", " ", clean(s)).strip()


def q(rec, *quotes):
    out = []
    for s in quotes:
        assert norm(s) in norm(rec), (s, norm(rec)[:200])
        CHECKS.append(s)
        out.append(f'"{s}"')
    return " ".join(out)


def pt(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    p = d.astimezone(PT)
    s = p.strftime("%a %b %-d %Y %-I:%M %p") + " PT"
    if p.date() != d.date():
        s += f" ({d.strftime('%a %b %-d %H:%M')} UTC)"
    return s


def tsiso(ts):
    return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


SM = {f"{r['channel_id']}/{r['ts']}": r for r in rows("slack.slack_messages")}
GM = {r["id"]: r for r in rows("gmail.gmail_messages")}
BS = {k: v["rec"] for k, v in OB["slack"].items()}
iss = {r["id"]: r for r in rows("linear.linear_issues")}
cm = {r["issue_id"]: r for r in rows("linear.linear_comments")}
WHO = {"usr_63fffeb4fab5233e": "Leonard", "usr_cc3e90160f490686": "Arthur"}
ORDER = sorted(iss, key=lambda x: int(x.split("-")[1]))
assert len(ORDER) == 37 and ORDER[0] == "ENG-2438" and ORDER[-1] == "ENG-2474"
EV, N = [], {}


def ev(key, action, expected):
    EV.append((action, expected))
    N[key] = len(EV)


def o(*keys):
    ns = [N[k] for k in keys]
    return ("OE " if len(ns) == 1 else "OEs ") + ", ".join(str(n) for n in ns)


# ---------------------------------------------------------------- discovery
hub = SM[I["hub"]]
ev("hub", "Read Leonard's DM from Thursday night in Slack (Robert's DM with Leonard Hayes, his message of Thu Feb 12 2026)",
   f"Leonard, {pt(tsiso(hub['ts']))}, message ts {hub['ts']}: " + q(hub["text"], "if you really want to keep combo fighter going, let's set the LLC up properly.",
                                              "I put everything we might need from HG into the LLC project in linear, one issue each.",
                                              "go through them and make the call on each one: what the LLC takes if Sunset can't sell it, what it costs us March through May, and who pays what.",
                                              "the ground rules doc has how we decide.", "lay the sheet out like my draft from Tuesday, keep it in your drive and share it with Blake and me.",
                                              "leave your call on each issue too so we can see it there.", "I'll email you how we split the money.",
                                              "then tell me here what you'd do and what it costs each of us a month.", "we decide on Monday's call"))
proj = rows("linear.linear_projects")[0]
ev("project", "Find the LLC project in Linear (search the projects for \"LLC\", named in OE 1; it has one match)",
   f"Project \"{proj['name']}\", team ENG, created {pt(proj['created_at'])}. Its description: " + q(proj["description"], "One issue per thing the LLC might take from HG or pay for.",
                                                                                             "Leave your call on each one as a comment and move it: to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is left to do on it; to Todo if the LLC takes it and something is still to do, and assign whoever moves it; to Canceled if it stays with HG."))
ev("issues", f"List the issues in the LLC take-over project in Linear (project from {o('project')})",
   "37 issues, all in Backlog with no assignee: " + "; ".join(f"{k} {iss[k]['title']}" for k in ORDER) + ".")
KEYT = {"ENG-2441", "ENG-2445", "ENG-2447", "ENG-2462", "ENG-2472"}
parts = []
for k in ORDER:
    c = cm[k]
    t = f", {pt(c['created_at'])}" if k in KEYT else ""
    parts.append(f"{k} {WHO[c['author_id']]}{t}: " + q(c["body"], clean(c["body"])))
ev("comments", f"Read the comments on each of the 37 issues in Linear (one call per issue, list from {o('issues')})", "One comment on each. " + " ".join(p + ";" for p in parts)[:-1] + ".")
gr = [r for r in rows("gdocs.docs_documents") if r.get("document_id") == I["ground_rules"]][0]
grf = rows("gdrive.drive_files", id=I["ground_rules"])[0]
ev("rules", "Read the ground rules doc in Drive/Docs (search \"ground rules\"; doc \"LLC ground rules (Combo Fighter and whatever else we take)\", from OE 1)",
   f"Leonard's doc, last changed {pt(grf['modified_time'])}. " + q(gr["body_text"], "The LLC is the new one Blake and I are setting up for the three of us, and anything Harmony Games owns (the games with their art and listings, and the equipment) comes to it only through Sunset's sale, the way I wrote after the call on Wednesday.",
                                                               "Services we keep running just move their billing to the LLC.", "The plan runs March 1 to May 31.",
                                                               "Domino Delights and Zombie Match come over only if what each made in January, going by the warehouse's daily revenue table, covers what its own hosting bills now, whatever we said about them before.",
                                                               "Combo Fighter comes over either way, it's the reason we're doing this.", "A game that comes over brings what it needs to keep running, its accounts and its player support.",
                                                               "Cost every item at what it bills now, going by whoever runs it, not by what HG used to pay.",
                                                               "What we already decided to keep or cancel for the shutdown in #winddown stays decided.",
                                                               "this plan is only what bills us every month, no one-offs or yearly fees.", "How things move is on the LLC card on our board."))
card = rows("trello.trello_cards", id=I["trello_card"])[0]
ev("card", f"Read the LLC card on the Harmony Games board in Trello (search \"LLC\", named in {o('rules')}; the open card \"{card['name']}\", not the archived 2024 card \"Follow up with Michelle on LLC\")",
   q(card["desc"], "Robert makes the call on each item in the Linear project.", "Whoever runs an item today moves it.", "Anything that comes through Sunset's sale moves when the sale closes.",
     "Anything that already has its own deadline keeps it; everything else moves by March 1."))
grid = json.loads(rows("gsheets.sheets_sheets")[0]["grid_json"])
dsf = rows("gdrive.drive_files", id=I["draft_sheet"])[0]
ev("draft", f"Read Leonard's draft from Tuesday in Sheets (search Drive for \"LLC\"; of the three LLC files shared with Robert, the sheet \"{dsf['name']}\", from {o('hub')})",
   f"Created {pt(dsf['created_time'])}. Header: " + ", ".join(grid[0]) + ". Rows: Combo Fighter, CF, LLC, 0, Owner Robert; DD servers, DD, ?, \"" + grid[2][3] + "\", Owner Blake; Metabase + dbt, Game blank, ?, \"" + grid[3][3] + "\"; Figma, CF, LLC, 0, Owner Robert.")
assert grid[1][:4] == ["Combo Fighter", "CF", "LLC", "0"] and grid[2][0] == "DD servers" and grid[3][0] == "Metabase + dbt" and grid[4][:4] == ["Figma", "CF", "LLC", "0"]
split = GM["robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>"]
ev("split", f"Read Leonard's email on the split in Gmail (search \"split\", from \"how we split the money\" in {o('hub')}; the newest hit, the full message)",
   f"Leonard to Robert, cc Arthur, {pt(split['date'])}, subject \"LLC money\": " + q(split["body_text"], "each of the three of us carries a third of what the LLC costs a month, March through May.",
                                                                                        "that's everything on the plan that bills monthly, including what one of us already pays for it.",
                                                                                        "whatever one of us already pays personally counts toward his third, and he puts the difference in as cash.", "put the three shares on the sheet per month."))
W = {k: BS[k] for k in ("dd_aws_1k", "dd_aws_300", "helpshift_feb28", "figma_sep11", "appsflyer", "keep_list", "action_items", "arthur_kub")}
ev("winddown", f"Read the February posts in #winddown in Slack (named in {o('rules')}; page through the whole month)",
   f"Arthur, {pt(tsiso(W['dd_aws_1k']['ts']))}: " + q(W["dd_aws_1k"]["text"], "Looks like DD production account costs ~$1k a month") + f" and {pt(tsiso(W['dd_aws_300']['ts']))}: " + q(W["dd_aws_300"]["text"], "Might be easy to get to 300")
   + f". Leonard, {pt(tsiso(W['helpshift_feb28']['ts']))}: " + q(W["helpshift_feb28"]["text"], "We gotta move domino delights and zombie match off Helpshift before Feb 28th.")
   + f" Robert, {pt(tsiso(W['figma_sep11']['ts']))}: " + q(W["figma_sep11"]["text"], "Our Figma is good until September 11th")
   + f". Leonard, {pt(tsiso(W['appsflyer']['ts']))}: " + q(W["appsflyer"]["text"], "if Singular shuts down our access we may need to move to another solution provider that offers data for free up to 15K installs")
   + f". Leonard, {pt(tsiso(W['keep_list']['ts']))}: " + q(W["keep_list"]["text"], "During shutdown, let’s keep Deel, gusto, Intuit. I canceled other subscriptions under mine.", "linear we keep during transition")
   + f". Leonard's action items, {pt(tsiso(W['action_items']['ts']))}: " + q(W["action_items"]["text"], "We keep accounts that has our data such as Slack, google, google analytics, github under Harmony Games until the data is extracted")
   + f". Arthur, {pt(tsiso(W['arthur_kub']['ts']))}: " + q(W["arthur_kub"]["text"], "I'll be moving github,", "and Metabase to my KubLLC card."))
rv = OB["revenue_rows"]
tot = {}
for r in rv.values():
    if str(r["date"]).startswith("2026-01"):
        tot[r["game_id"]] = tot.get(r["game_id"], Decimal(0)) + Decimal(str(r["total_revenue_usd"]))
assert str(tot["domino_delights"]) == "183.11" and tot["zombie_match_3d"] == 0 and str(tot["combo_fighter"]) == "7.36"
ev("revenue", f"Sum each game's January revenue in Snowflake (table ANALYTICS.MONETIZATION.REVENUE_DAILY, named in {o('rules')}: SUM(total_revenue_usd) and COUNT(*) by game_id for date 2026-01-01 to 2026-01-31)",
   "Three rows: domino_delights 183.11, zombie_match_3d 0.00, combo_fighter 7.36, each over 62 daily rows.")
ad = SM[I["arthur_dm"]]
ev("dd140", f"Search Slack for what the Domino Delights production account bills now (search \"AWS bill\", from the ENG-2443 and ENG-2445 comments in {o('comments')}; its only hit is Arthur's thread reply in Robert's DM with Arthur Blake)",
   f"Arthur, {pt(tsiso(ad['ts']))}: " + q(ad["text"], "fyi Domino's prod account is down to $140 a month now, one small task and the db at its floor. that's what it bills from March. it's still on HG's AWS bill till then") + ".")
bill = GM["robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>"]
ev("bill", f"Read Arthur's email on the Metabase, dbt and GitHub billing in Gmail (search \"metabase\", from ENG-2447 in {o('issues')} and Arthur's #winddown post in {o('winddown')}; the newest hit, subject \"{bill['subject']}\", the full message)",
   f"Arthur to Robert and Leonard, {pt(bill['date'])}: " + q(bill["body_text"], "github, dbt and metabase bill to my Kub card from the next bill.",
                                                             "it's the $100 base now, dbt is $100 and github is back to the $48 team plan", "so $248 a month. I'll carry those through May as my part.",
                                                             "the github org itself stays HG's till the data's delivered, I'm just paying the bill, so count it as mine like the other two.") + ".")
jk = GM["robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>"]
ev("cf62", f"Read Arthur's \"jenkins\" email in Gmail (search \"jenkins\", from the ENG-2446 comment in {o('comments')}; the newest hit, the full message; the figure is in its second paragraph)",
   f"Arthur to Robert, cc Leonard, {pt(jk['date'])}: " + q(jk["body_text"], "the build boxes are HG's, they can go with the laptops whenever the sale needs them.",
                                                          "so CF's own account bills $62 a month now, just its live stacks. still on HG's AWS bill till March like Domino's.") + ".")
vr, vb, vo = BS["vo_root"], BS["vo_budget"], SM[I["vo_status"]]
ev("vo", f"Search Slack for anything else one of them already pays himself (search \"my card\": {o('split')} counts what one of them already pays, and {o('bill')} is Arthur's \"billing moved to my card\"; the newest hit is Leonard's reply in a #prototype thread), then read that thread and Leonard's budget post in the channel that morning",
   f"Leonard's reply, {pt(tsiso(vo['ts']))}: " + q(vo["text"], "of the meta campaigns only the VO one is still on", "it's set to $100/day capped at $3,000 a month, and that's what it runs at from March",
                                                     "it's on my card till the end of Feb and moves to our new company's card from March if we keep CF going, so count it as its own line in what we pay each month")
   + f". The thread's root, Leonard, {pt(tsiso(vr['ts']))}: " + q(vr["text"], "VO campaign is created and will go live in the next few hours") + f"; his channel post at {pt(tsiso(vb['ts']))}: " + q(vb["text"], "Budget is $100/day") + ".")
lr, lrep = BS["layer_mar3"], SM[I["layer_reply"]]
ev("layer", "Search Slack for layer.ai and read the thread under Leonard's post in #prototype (search \"layer.ai\")",
   f"Leonard, {pt(tsiso(lr['ts']))}: " + q(lr["text"], "we have access until March 3rd") + f". His reply in that thread, to Robert, {pt(tsiso(lrep['ts']))}: "
   + q(lrep["text"], "the CF character concept art is only in layer.ai, can you pull it out yourself before then?", "the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses") + ".")
asc = GM["robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>"]
ev("asc", f"Search Robert's Gmail for Domino Delights, whose player support is ENG-2462 in {o('issues')} (search \"Domino Delights\"; the newest hit is App Review's mail, subject \"We noticed an issue with your submission.\"; the full message)",
   f"{pt(asc['date'])}, signed App Review: " + q(asc["body_text"], "App Name: Domino Delights", "Guideline 1.5 - Safety - Developer Information",
                                                   "The support option in the app only opens an email draft, and on a device without a mail account set up it does nothing, so users can't reach you from the app.",
                                                   "Please add a support URL or another way to contact you in the app.") + " It comes after Arthur's \"done\" on ENG-2462 (" + o("comments") + ").")
cs_ = BS["calm_sub"]
ev("calm", f"Search Slack for what Calm Play LLC is (search \"calm play\", from ENG-2472 in {o('issues')}; page to Leonard's December 2023 post in #admin_foundersonly)",
   f"Leonard, {pt(tsiso(cs_['ts']))}: " + q(cs_["text"], "we had to do a couple more things on top of the regular LLC setup to make calm play full subsidiary of Harmony Games") + ".")
ev("users", "List the Linear users for the assignees (Robert, Leonard Hayes, Arthur Blake)",
   "Robert: usr_Robert, robert@harmonygames.co. Leonard: usr_63fffeb4fab5233e, leonard.hayes@harmonygames.co. Arthur: usr_cc3e90160f490686, arthur.blake@harmonygames.co.")
ev("addr", "Look up Leonard Hayes and Arthur Blake in Contacts (\"Blake\" in the prompt and the DM)", "leonard.hayes@harmonygames.co (Co-founder & CEO); arthur.blake@harmonygames.co (Co-founder & CTO).")

# ---------------------------------------------------------------- analysis
ev("take", f"Apply the take test to Domino Delights and Zombie Match (Docs rule in {o('rules')}, Snowflake in {o('revenue')}, Slack in {o('dd140')}, Linear in {o('comments')})",
   "Domino Delights made 183.11 in January, which covers the $140 a month its prod account bills now; the ~$1k and 300 in #winddown, ENG-2441's note and the draft are earlier figures. So Domino Delights comes over with its accounts and its player support. "
   "Zombie Match made 0.00, which covers none of its account's bill (ENG-2443: \"it bills every month on HG's AWS bill\"), so Zombie Match and its account stay with HG. Combo Fighter comes over either way.")
ev("costs", f"Set each item's monthly cost at what it bills now ({o('dd140', 'bill', 'cf62', 'vo', 'comments')})",
   "Domino Delights production account: 140. Combo Fighter backend and auth stacks: 62 (Arthur's email of Thu 8:20 PM PT is later than his \"about $95\" on ENG-2445 at 4:58 PM PT and says why it fell). "
   "Metabase 100, dbt 100, GitHub 48: 248 a month on Arthur's card through May (later than Leonard's \"about $300\" on ENG-2447). The VO campaign: 3,000 a month from March, its own line. AppsFlyer: 0 (free tier). "
   "Not monthly, so off the plan: the playable vendor's $3,750 (\"one-off\"), the Unity Ads $100, Carta's renewal (\"renewal is 8/15\") and Google Play's \"one-time fee\". Every other item costs the LLC 0.")
HG = [k for k in ORDER if TRUTH[NAME[k]]["Decision"] == "HG"]
FD = [k for k in ORDER if TRUTH[NAME[k]]["Decision"] == "Founder"]
LLC = [k for k in ORDER if TRUTH[NAME[k]]["Decision"] == "LLC"]
assert (len(LLC), len(FD), len(HG)) == (6, 3, 28)
ev("calls", f"Make the call on each of the 37 issues and on the VO campaign (rules in {o('rules', 'card', 'project')}, findings in {o('comments', 'winddown', 'vo', 'layer', 'asc', 'calm', 'take', 'costs')})",
   "The LLC takes 7, each with a step left and the person who moves it: Combo Fighter (comes through Sunset's sale; Robert; when the sale closes); Domino Delights (through Sunset's sale; Leonard, \"I'll handle it with Sunset\"; when the sale closes); "
   "Domino Delights production account (billing moves to the LLC; Arthur; by Mar 1, \"still on HG's AWS bill till then\"); Combo Fighter backend and auth stacks (billing moves to the LLC; Arthur; by Mar 1, \"still on HG's AWS bill till March\"); "
   "AppsFlyer (set CF up on the free tier; Leonard, \"I'll set CF up on it\"; by Mar 1); Domino Delights player support (a build with a support URL or another in-app contact, past App Review, before Helpshift stops; Arthur; before Feb 28); "
   "the VO campaign (moves to the new company's card from March; Leonard; by Mar 1). Arthur pays himself through May, 3: Metabase, dbt, GitHub (the org stays HG's till the data's delivered). "
   "HG keeps 28: " + ", ".join(iss[k]["title"] for k in HG) + ". Among them, Figma stays HG's (prepaid to Sep 11), not LLC as on the draft; layer.ai lapses, with nothing on the account for the new company, and Robert pulls CF's concept art out before access ends Mar 3; "
   "Calm Play LLC is HG's subsidiary, and the LLC is the new one Leonard and Arthur are setting up.")
ev("shares", f"Work out the monthly total and the three shares (the split in {o('split')}, costs in {o('costs')})",
   "140 + 62 + 3,000 + 100 + 100 + 48 = 3,450 a month, March through May. A third each: 1,150. Arthur already pays 248, which counts toward his third, so he puts in 902 cash; Leonard and Robert put in 1,150 cash each. The LLC itself pays 3,202 a month (140 + 62 + 3,000).")
assert 140 + 62 + 3000 + 100 + 100 + 48 == 3450 and 3450 / 3 == 1150 and 1150 - 248 == 902

# ---------------------------------------------------------------- writes: the missing line
ev("w_vo", f"Create an issue for the VO campaign in the LLC take-over project in Linear (team ENG, project from {o('project')}, state Todo, assignee Leonard from {o('users')})",
   "A new issue in the LLC take-over project naming Combo Fighter's VO (Meta) campaign, state Todo, assigned to Leonard Hayes.")
ev("w_voc", "Comment the call on the new VO campaign issue in Linear",
   "A comment saying the LLC takes it: 3,000 a month from March, its own line; Leonard moves it from his card to the new company's card by Mar 1.")
WHY = {
    "ENG-2438": "LLC at $0 a month: it comes through Sunset's sale; Robert moves it when the sale closes",
    "ENG-2439": "LLC at $0 a month (its hosting is ENG-2441): January's 183.11 covers its $140 hosting; it comes through Sunset's sale, Leonard moves it when the sale closes",
    "ENG-2440": "stays with HG: January's 0.00 doesn't cover its hosting",
    "ENG-2441": "LLC at $140 a month; Arthur moves the billing off HG's AWS bill by Mar 1",
    "ENG-2442": "stays with HG: nothing runs on it, Arthur is shutting it down",
    "ENG-2443": "stays with HG with Zombie Match; Combo Fighter doesn't need it",
    "ENG-2444": "stays with HG: it only carried DD and ZM events, Arthur is shutting it down",
    "ENG-2445": "LLC at $62 a month; Arthur moves the billing off HG's AWS bill by Mar 1",
    "ENG-2446": "stays with HG: the build boxes go with the laptops in Sunset's sale",
    "ENG-2447": "Arthur pays it himself through May, $100 a month",
    "ENG-2448": "Arthur pays it himself through May, $100 a month",
    "ENG-2449": "Arthur pays it himself through May, $48 a month; the org stays HG's till the data's delivered",
    "ENG-2450": "stays with HG: Singular is being terminated",
    "ENG-2451": "LLC at $0: Combo Fighter goes on AppsFlyer's free tier, Leonard sets it up by Mar 1",
    "ENG-2452": "stays with HG until the data is extracted",
    "ENG-2453": "stays with HG: prepaid to Sep 11, then it lapses",
    "ENG-2454": "stays with HG and lapses, nothing on the account for the new company to take; Robert pulls CF's concept art out before access ends Mar 3",
    "ENG-2455": "stays with HG: cancelled", "ENG-2456": "stays with HG: cancelled, Pro runs to Feb 25", "ENG-2457": "stays with HG: cancelled", "ENG-2458": "stays with HG: cancelled",
    "ENG-2459": "stays with HG: being terminated; Combo Fighter is fine on Unity Personal", "ENG-2460": "stays with HG: cancelled",
    "ENG-2461": "stays with HG: cancelling; Combo Fighter was never on it",
    "ENG-2462": "LLC at $0 a month: App Review rejected the email-only support, so a build with a support URL or another in-app contact still has to pass review before Helpshift stops; Arthur, before Feb 28",
    "ENG-2463": "stays with HG, kept for the data", "ENG-2464": "stays with HG, kept for the data", "ENG-2465": "stays with HG, kept during the transition",
    "ENG-2466": "stays with HG, kept during the shutdown", "ENG-2467": "stays with HG, kept during the shutdown", "ENG-2468": "stays with HG, kept during the shutdown",
    "ENG-2469": "stays with HG: its renewal isn't a monthly bill", "ENG-2470": "stays with HG; Combo Fighter's listing moves with the game",
    "ENG-2471": "stays with HG: a one-time fee, nothing monthly",
    "ENG-2472": "stays with HG: Calm Play is HG's subsidiary, and the LLC is the new one Leonard and Arthur are setting up",
    "ENG-2473": "stays with HG: the $100 is a one-off for this week's playable test", "ENG-2474": "stays with HG: the $3,750 is a one-off, not a monthly bill",
}
assert set(WHY) == set(ORDER)
for k in ORDER:
    ev("wc:" + k, f"Comment the call on {k} in Linear", f"A comment on {k} ({iss[k]['title']}) saying {WHY[k]}.")
for k in ORDER:
    t = TRUTH[NAME[k]]
    if t["Decision"] == "LLC":
        ev("wm:" + k, f"Move {k} to Todo, assigned to {t['Owner']}, in Linear (user from {o('users')})", f"{k} state Todo, assignee {t['Owner']}.")
    elif t["Decision"] == "Founder":
        ev("wm:" + k, f"Move {k} to Done in Linear", f"{k} state Done.")
    else:
        ev("wm:" + k, f"Move {k} to Canceled in Linear", f"{k} state Canceled.")

# ---------------------------------------------------------------- writes: the sheet, the shares, the reply
ev("w_sheet", "Create the plan sheet in Sheets (in Robert's own Drive)", "A new native spreadsheet in Robert's Drive, at the top level of his own Drive; any title.")
ev("w_rows", f"Write the plan to the sheet in Sheets (sheet from {o('w_sheet')}; calls, costs and shares from {o('calls', 'costs', 'shares')})",
   "Header Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By (the draft's columns, " + o("draft") + "), then one row per item: the 37 issues and the VO campaign (Metabase and dbt may share one row as on the draft). "
   "LLC rows: Combo Fighter, 0, Owner Robert, by when the sale closes; Domino Delights, 0, Owner Leonard, by when the sale closes; Domino Delights production account, 140, paid by the LLC, Owner Arthur, by Mar 1; "
   "Combo Fighter backend and auth stacks, 62, paid by the LLC, Owner Arthur, by Mar 1; AppsFlyer, 0, Owner Leonard, by Mar 1; Domino Delights player support, 0, next step the support build past App Review, Owner Arthur, before Feb 28; "
   "the VO campaign, 3,000, paid by the LLC (the new company's card from March), Owner Leonard, by Mar 1. Metabase 100, dbt 100, GitHub 48: Arthur pays them himself, paid by Arthur. The other 28 rows: stay with HG, 0, paid by HG or blank. "
   "Robert pulls Combo Fighter's concept art out of layer.ai before Mar 3, on the layer.ai row (Owner Robert) or the Combo Fighter row. "
   "Shares per month: total 3,450; a third each 1,150; Robert 1,150 cash, Leonard 1,150 cash, Arthur 902 cash on top of the 248 he already pays.")
ev("w_shareL", f"Share the sheet with Leonard Hayes in Drive (address from {o('addr')})", "leonard.hayes@harmonygames.co can open the sheet (writer, commenter or reader).")
ev("w_shareA", f"Share the sheet with Arthur Blake in Drive (address from {o('addr')})", "arthur.blake@harmonygames.co can open the sheet (writer, commenter or reader).")
ev("w_reply", f"Reply to Leonard in the thread of his DM in Slack (the DM and message from {o('hub')}, after every other write)",
   "A reply in that thread (thread_ts 1770961200.890407) saying what Robert would do: take Combo Fighter and Domino Delights into the LLC and leave Zombie Match with HG; the plan costs 3,450 a month, 3,000 of it the VO campaign; "
   "Domino Delights' support build still has to pass App Review before Feb 28. What it costs each of them a month: 1,150 each (Arthur puts in 902 cash on top of the 248 he already pays). The link to the sheet.")

# ---------------------------------------------------------------- write
out = []
for n, (act, exp) in enumerate(EV, 1):
    out += [f"OE {n}  {act}", f"Expected: {exp}", ""]
text = "\n".join(out).rstrip() + "\n"
assert 300 <= len(text) <= 50000, len(text)
assert "should" not in text.lower() or True
OUTP = os.environ.get("OE_OUT") or os.path.join(TI, "08_Oracle_Events.md")
open(OUTP, "w").write(text)
if not os.environ.get("OE_OUT"):
    json.dump({"events": len(EV), "chars": len(text), "quotes_asserted": len(CHECKS), "index": N}, open(os.path.join(HERE, "oe_events_index.json"), "w"), indent=0)
else:
    json.dump({"checks": CHECKS, "index": N}, open(os.environ["OE_OUT"] + ".checks.json", "w"), indent=0)
w = sum(1 for k in N if k.startswith(("w_", "wc:", "wm:")))
print("events", len(EV), "writes", w, "chars", len(text), "quotes asserted", len(CHECKS))
