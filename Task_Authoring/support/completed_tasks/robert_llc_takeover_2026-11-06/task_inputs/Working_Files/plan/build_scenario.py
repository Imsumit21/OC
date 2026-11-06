#!/usr/bin/env python3
"""Scenario builder (design stage) for Robert · the LLC take-over plan for Combo Fighter (March-May 2026).

Writes Working_Files/01_Hardness_Manifest.draft.json, Working_Files/01_Gradable_Surface.json, plan/ids.json,
plan/wording.json and plan/tables/*.md (tables pasted into 01_Scenario_Design.md).
Design only: the seeded texts here are the planned wording /create-injection must use verbatim (delegation quotes are
exact substrings of them). Ids are minted deterministically from a label and checked against the base by
plan/check_ids.py. Never executes SQL; reads nothing but 00_Task_Context.json.
"""
import hashlib, json, os, re
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
SALT = "hg-robert-llc-takeover|"
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"


def hx(label, n):
    return hashlib.sha256((SALT + label).encode()).hexdigest()[:n]


def ep(iso):
    return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def slack_ts(label, iso):
    return f"{ep(iso)}.{int(hx(label, 8), 16) % 1000000:06d}"


def drive(label):
    return "f_" + hx(label, 22)


def evt(label):
    return "evt_" + hx(label, 22)


def trello_id(label, iso):
    return "%08x" % ep(iso) + hx(label, 16)


def thread(label, iso):
    return str(((ep(iso) * 1000) << 20) + (int(hx(label, 8), 16) & 0xFFFFF))


def uuid(label):
    h = hx(label, 32)
    return f"{h[:8]}-{h[8:12]}-4{h[13:16]}-a{h[17:20]}-{h[20:32]}"


# ---------------------------------------------------------------- base records the design relies on (all YES for Robert)
WD, EXEC, PROTO, CI, ADM, FND = "C0ADGSZKR3R", "C07C2866011", "C09UHHN6PFZ", "C05KNDCHAAG", "C04UEQVDVB7", "C04UTBZL6AX"
DM_LR, DM_RA, DM_RO, BOOMBIT = "D04UP2L3E3S", "D04V95AAAHW", "D07H86MV4DN", "C09SWTHEMEW"
BASE = {
    "dd_aws_1k": f"{WD}/1770680984.725779", "dd_aws_300": f"{WD}/1770682219.100789", "dd_less_1k": f"{WD}/1770686243.781429",
    "dd_lights": f"{WD}/1770686219.875929", "helpshift_feb28": f"{WD}/1770789534.434749", "figma_sep11": f"{WD}/1770859313.592649",
    "data_offer": f"{WD}/1770911000.728559", "pay_svb": f"{WD}/1770927223.969899", "appsflyer": f"{WD}/1770932709.222409",
    "checklist": f"{WD}/1770933450.410449", "keep_list": f"{WD}/1770933601.686309", "action_items": f"{WD}/1770933903.645709",
    "arthur_kub": f"{WD}/1770937232.664809", "leapblock": f"{WD}/1770922731.444009", "angels": f"{WD}/1770934638.035469",
    "lifestyle": f"{EXEC}/1770612982.268919", "auction": f"{EXEC}/1770850800.723979", "buy_back": f"{EXEC}/1770839149.629569",
    "cf_3_6_months": f"{EXEC}/1770237771.839399", "self_sustaining": f"{EXEC}/1770084297.911029", "keep_live": f"{EXEC}/1770489896.754049",
    "recap_25k": f"{EXEC}/1767730784.379929", "recap_proforma": f"{EXEC}/1768417784.194359",
    "vo_root": f"{PROTO}/1770404397.819789", "vo_budget": f"{PROTO}/1770404445.795829", "layer_mar3": f"{PROTO}/1770837702.167889",
    "unity_100": f"{PROTO}/1770845002.610529", "vo_off_q": f"{EXEC}/1770438169.228649", "guests": f"{PROTO}/1770842566.250369", "dd_boombit": f"{PROTO}/1770844309.583109",
    "repos_llc": f"{CI}/1770842137.835489", "archive_feb15": f"{CI}/1770839984.194409",
    "budget_missing": f"{DM_RO}/1770873696.684969", "dm_ra_root": f"{DM_RA}/1770056235.480619",
    "boombit_retention": f"{BOOMBIT}/1770725775.479449",
    "calm_owned": f"{ADM}/1701383740.580749", "calm_sub": f"{ADM}/1703492127.063049", "calm_future": f"{FND}/1701126533.617549",
    "calm_tax": f"{ADM}/1747349657.711009", "calm_agent": f"{ADM}/1759615469.061409",
    "zm_transfer": f"{EXEC}/1752548116.304169", "zm_apple_done": f"{EXEC}/1752622453.361899", "zm_android_done": f"{EXEC}/1752726128.862409",
    "aws_guide": "confluence:page_aws_infra", "revenue": "snowflake:ANALYTICS.MONETIZATION.REVENUE_DAILY",
    "deel_due": f"{ROB}/1855892533860895614", "svb_paid": f"{ROB}/1856009245020615882", "dd_review_oct30": f"{ROB}/gmail threads/00015817.json",
    "robert_root": "d_9f7ba94f7526d54d8482ba", "founders_board": "640643a3fd8f3ca308d9318e", "todo_list": "640643a3fd8f3ca308d93195",
}

# ---------------------------------------------------------------- seeded timestamps (UTC), all before Feb 13 10:03Z (NB-6)
T = {
    "cf_deck": "2026-02-08T03:00:00Z", "notes_doc": "2026-02-09T23:55:00Z", "draft_sheet": "2026-02-10T18:30:00Z",
    "pr_open": "2026-02-12T18:05:00Z", "pr_merge": "2026-02-12T21:10:00Z", "dd_submit_build": "2026-02-12T21:40:00Z",
    "vo_status": "2026-02-12T23:20:00Z", "ground_rules": "2026-02-12T23:46:00Z", "trello_card": "2026-02-12T23:42:00Z",
    "project": "2026-02-12T23:24:00Z", "issue0": "2026-02-12T23:25:00Z",
    "c_dd_prod": "2026-02-13T00:48:00Z", "c_metabase": "2026-02-13T00:52:00Z", "c_cf_backend": "2026-02-13T00:58:00Z",
    "c_figma": "2026-02-13T01:04:00Z", "c_build": "2026-02-13T01:07:00Z", "c_calm": "2026-02-12T23:41:00Z", "c_support": "2026-02-13T01:30:00Z",
    "c_kapwing": "2026-02-13T01:34:00Z", "c_zm_account": "2026-02-13T01:37:00Z", "dd_build_result": "2026-02-12T21:49:30Z",
    "arthur_mail": "2026-02-13T02:35:00Z", "arthur_dm": "2026-02-13T03:10:00Z", "hub": "2026-02-13T05:40:00Z",
    "monday_created": "2026-02-13T05:45:00Z", "monday_start": "2026-02-16T18:00:00Z", "split_mail": "2026-02-13T06:10:00Z",
    "asc_notice": "2026-02-13T07:30:00Z",
    "layer_reply": "2026-02-12T19:15:00Z", "jenkins_mail": "2026-02-13T04:20:00Z", "c_layer": "2026-02-13T00:37:00Z",
}

IDS = {
    "hub": f"{DM_LR}/{slack_ts('hub', T['hub'])}",
    "arthur_dm": f"{DM_RA}/{slack_ts('arthur_dm', T['arthur_dm'])}",
    "vo_status": f"{PROTO}/{slack_ts('vo_status', T['vo_status'])}",
    "ground_rules": drive("ground_rules_doc"), "notes_doc": drive("lifestyle_notes_doc"), "draft_sheet": drive("draft_sheet"),
    "cf_deck": drive("cf_90_day_deck"),
    "split_thread": f"{ROB}/{thread('split_mail', T['split_mail'])}", "arthur_thread": f"{ROB}/{thread('arthur_mail', T['arthur_mail'])}",
    "asc_thread": f"{ROB}/{thread('asc_notice', T['asc_notice'])}",
    "monday_evt": evt("monday_call"), "trello_card": trello_id("llc_card", T["trello_card"]),
    "project": uuid("llc_project"), "pr": "harmonygames-Games/GameOfDominoes#1917",
    "builds_start": f"C05433XK267/{slack_ts('builds_start', T['dd_submit_build'])}",
    "builds_result": f"C05433XK267/{slack_ts('builds_result', T['dd_build_result'])}",
    "layer_reply": f"{PROTO}/{slack_ts('layer_reply', T['layer_reply'])}",
    "jenkins_thread": f"{ROB}/{thread('jenkins_mail', T['jenkins_mail'])}",
}
for k, iso in (("c_dd_prod", T["c_dd_prod"]), ("c_metabase", T["c_metabase"]), ("c_cf_backend", T["c_cf_backend"]),
               ("c_calm", T["c_calm"]), ("c_support", T["c_support"]), ("c_figma", T["c_figma"]), ("c_build", T["c_build"]),
               ("c_kapwing", T["c_kapwing"]), ("c_zm_account", T["c_zm_account"])):
    IDS[k] = "comment_" + hx(k, 32)

# ---------------------------------------------------------------- planned wording (verbatim for /create-injection)
Q = {
    "hub": ("if you really want to keep combo fighter going, let's set the LLC up properly. I put everything we might "
            "need from HG into the LLC project in linear, one issue each. go through them and make the call on each one: "
            "what the LLC takes if Sunset can't sell it, what it costs us March through May, and who pays what. the ground "
            "rules doc has how we decide. lay the sheet out like my draft from Tuesday, keep it in your drive and share it "
            "with Blake and me. leave your call on each issue too so we can see it there. I'll email you how we split the "
            "money. then tell me here what you'd do and what it costs each of us a month. we decide on Monday's call"),
    "ground_rules": ("LLC ground rules (Combo Fighter and whatever else we take)\n"
                     "This is the lifestyle route I posted about in #executives. The LLC is the new one Blake and I are "
                     "setting up for the three of us, and anything Harmony Games owns (the games with their art and listings, and the equipment) comes to it only "
                     "through Sunset's sale, the way I wrote after the call on Wednesday. Services we keep running just move their billing to the LLC.\n"
                     "The plan runs March 1 to May 31.\n"
                     "Domino Delights and Zombie Match come over only if what each made in January, going by the warehouse's "
                     "daily revenue table, covers what its own hosting bills now, whatever we said about them before. Combo Fighter comes over either way, it's the reason we're doing this. "
                     "A game that comes over brings what it needs to keep running, its accounts and its player support.\n"
                     "Cost every item at what it bills now, going by whoever runs it, not by what HG used to pay.\n"
                     "What we already decided to keep or cancel for the shutdown in #winddown stays decided.\n"
                     "Pay for anyone who stays on is a separate conversation once we know the running cost; this plan is only what bills us every month, no one-offs or yearly fees.\n"
                     "How things move is on the LLC card on our board."),
    # rev4 (RB2): Done also covers an LLC item with nothing left to do, so a missed store notice flips ENG-2462 to Done
    "project_desc": ("One issue per thing the LLC might take from HG or pay for. Leave your call on each one as a comment and move it: "
                     "to Done if one of us pays it himself through May (even if HG still owns it) or if the LLC takes it and nothing is "
                     "left to do on it; to Todo if the LLC takes it and something is still to do, and assign whoever moves it; to "
                     "Canceled if it stays with HG."),
    "trello_desc": ("Robert makes the call on each item in the Linear project. Whoever runs an item today moves it. Anything "
                    "that comes through Sunset's sale moves when the sale closes. Anything that already has its own deadline keeps it; "
                    "everything else moves by March 1."),
    "split_mail": ("how we split it: each of the three of us carries a third of what the LLC costs a month, March through May. that's everything on "
                   "the plan that bills monthly, including what one of us already pays for it. whatever one of "
                   "us already pays personally counts toward his third, and he puts the difference in as cash. put the three "
                   "shares on the sheet per month."),
    "monday_desc": "Robert's plan sheet. We agree what we take and the shares.",
    "draft_header": ["Item", "Game", "Decision", "Monthly cost", "Paid by", "Next step", "Owner", "By"],
    "draft_rows": [["Combo Fighter", "CF", "LLC", "0", "", "", "Robert", ""],
                   ["DD servers", "DD", "?", "~1000 (Blake: maybe 300)", "", "", "Blake", ""],
                   ["Metabase + dbt", "", "?", "~300", "", "", "", ""],
                   ["Figma", "CF", "LLC", "0", "", "", "Robert", ""]],
    "notes_doc": ("LLC notes (Monday)\nIf we go the lifestyle route: Calm Play could hold it. DD and ZM both come with CF. "
                  "Servers about $1k a month, Blake is looking at it."),
    # trap carriers
    "c_dd_prod": "about $1k a month, Blake thinks he can get it to $300",
    "arthur_dm": ("fyi Domino's prod account is down to $140 a month now, one small task and the db at its floor. that's what it "
                  "bills from March. it's still on HG's AWS bill till then"),
    "c_metabase": "about $300 a month with dbt, more or less",
    "arthur_mail": ("github, dbt and metabase bill to my Kub card from the next bill. I dropped the extra metabase seats so it's the "
                    "$100 base now, dbt is $100 and github is back to the $48 team plan now that I dropped the extra seat and copilot is off, so $248 a month. I'll carry those through May as "
                    "my part. the github org itself stays HG's till the data's delivered, I'm just paying the bill, so count it as mine like the other two. "
                    "bigquery and firebase stay on HG's google account with GA until the data's out, and with CF's tiny volume they cost nothing after that, so there's nothing there for the LLC."),
    # rev4 (RB5): the issue comment carries Arthur's figure before his trim; his later Jenkins email gives what it bills now
    "c_cf_backend": "Combo Fighter's own account (its auth and backend stacks) runs about $95 a month on HG's AWS bill. CF stopped calling ZM's phoenix api, it doesn't need ZM's account. I keep an eye on them",
    "jenkins_subject": "jenkins",
    "jenkins_mail": ("moved our jenkins jobs to my own machine tonight. the build boxes are HG's, they can go with the laptops whenever the sale needs them.\n\n"
                     "while I was in there I shut down the extra copy of CF's backend that was still running from the January redeploy, so CF's own "
                     "account bills $62 a month now, just its live stacks. still on HG's AWS bill till March like Domino's."),
    # rev4 (RB4): the layer.ai issue note states only the cancellation; the art and its owner sit in a reply under the base access-date post
    "c_layer": "cancelled it on the 11th",
    "layer_reply": "<@EMPLOYEE_0016_SLACK_ID> the CF character concept art is only in layer.ai, can you pull it out yourself before then? the art goes with CF, there's nothing on the layer account for our new company to take, it just lapses",
    "c_support": "done, support goes to the email address now and Helpshift is out of DD (merged in #1917)",
    "pr_title": "Replace Helpshift with support email",
    "asc_subject": "We noticed an issue with your submission.",
    "asc_body": ("Hello [PERSON_NAME_0054],\n\nThank you for submitting your items for review. We appreciate your enthusiasm for Apple "
                 "platforms. As you know, we want to provide a safe experience for users to get apps and a great opportunity for all "
                 "developers to be successful. We do this by offering a highly curated App Store where every submission is reviewed "
                 "by experts and an editorial team helps users discover new apps every day.\n\nDuring our review, we noticed an issue "
                 "with your submission.\n\nApp Name: Domino Delights\nSubmission ID: [IDENTIFIER_{sid}]\n\nWe look forward to working with "
                 "you to resolve the issues with the following items:\n\nGuideline 1.5 - Safety - Developer Information\nThe support "
                 "option in the app only opens an email draft, and on a device without a mail account set up it does nothing, so users "
                 "can't reach you from the app. Please add a support URL or another way to contact you in the app.\n\nYou can "
                 "also view this information on the App Review page in App Store Connect.\n\nBest regards,\nApp Review"),
    "pr_body": ("Players reach support by email from the help button now instead of the Helpshift screen.\r\n"
                "- Removed the Helpshift SDK and its config\r\n- Help button opens a mail draft to the support address"),
    "split_subject": "LLC money",
    "arthur_subject": "billing moved to my card",
    "vo_status": ("of the meta campaigns only the VO one is still on (I paused the install one; the unity playable test just uses up the $100 left on unity). "
                  "it's set to $100/day capped at $3,000 a month, and that's what it runs at from March (it's still in learning this week). "
                  "it's on my card till the end of Feb and moves to our new company's card from March if we keep CF going, so count it as its own line in what we pay each month"),
    "c_kapwing": "cancelled, Pro runs to Feb 25",
    "c_zm_account": "ZM's account still runs phoenix, its nakama and the aurora cluster, nobody trimmed it. it bills every month on HG's AWS bill",
    "builds_start_text": "DD iOS Submission - #218 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/DD%20iOS%20Submission/218/display/redirect|Open>)",
    "builds_result_text": ("DD iOS Submission - #218 - Blake/boombitWithEcon Success after 9 min 12 sec (<http://blake.tplinkdns.com:9009/job/DD%20iOS%20Submission/218/display/redirect|Open>)\n"
                           "DD iOS Submission - #218 - Blake/boombitWithEcon Changes:\n- Replace Helpshift with support email. [Arthur Blake]"),
    "c_figma": "HG prepaid it to Sep 11, it stays HG's and just lapses then. nothing for the LLC to take or pay",
    "c_build": "the build boxes at my place are HG's, they go with the laptops in Sunset's sale. I'll move our jenkins jobs to my own machine before then, so the LLC doesn't need them",
    "c_calm": "Calm Play could just be our LLC, it already has the Singular org and its own Apple team",
    "cf_deck": ["Combo Fighter: next 90 days", "Run the VO campaign at $100/day (~$3k a month) through May",
                "No playables beyond the one in production until D1 is over 35%"],
}

# ---------------------------------------------------------------- the cohort: Leonard's 37 candidate issues + 1 outside item
# decision: LLC (the LLC takes it and pays) / Founder (one of us already carries it personally) / HG (stays with Harmony Games)
C = []


def item(key, game, decision, cost, paid_by, step, owner, by, deciding, role="control", channel=None, issue=True):
    C.append(dict(key=key, game=game, decision=decision, cost=cost, paid_by=paid_by, step=step, owner=owner, by=by,
                  deciding=deciding, role=role, channel=channel, issue=issue))


item("Combo Fighter", "CF", "LLC", 0, "-", "game, art and the App Store listing come through Sunset's sale", "Robert", "when the sale closes",
     "ground rules: Combo Fighter comes over either way")
item("Domino Delights", "DD", "LLC", 0, "-", "game and its listings come through Sunset's sale", "Leonard", "when the sale closes",
     "January income $183.11 (REVENUE_DAILY) covers the trimmed $140 hosting (Arthur's DM)", "trap", ["CORR", "AUTH"])
item("Zombie Match", "ZM", "HG", 0, "HG", "stays with Sunset's sale", "-", "-", "January income $0.00 cannot cover its hosting (Arthur's ZM account note: phoenix, nakama and aurora untrimmed, billing every month)", "trap", ["AUTH"])
item("Domino Delights production account (AWS)", "DD", "LLC", 140, "LLC", "billing moves to the LLC", "Arthur", "Mar 1",
     "Arthur's Feb 13 DM reply: $140 a month now", "trap", ["CORR"])
item("Domino Delights dev account (AWS)", "DD", "HG", 0, "HG", "shut down", "Arthur", "-", "Arthur's issue note: we don't need dev")
item("Zombie Match account (AWS)", "ZM", "HG", 0, "HG", "goes with ZM (still bills HG at full size)", "-", "-", "Arthur's issue note: phoenix, nakama and aurora untrimmed, billing every month on HG's AWS bill")
item("Analytics pipeline account (AWS)", "-", "HG", 0, "HG", "turned off", "Arthur", "-", "Arthur's issue note: feeds only the old dashboards")
item("Combo Fighter backend and auth stacks (AWS)", "CF", "LLC", 62, "LLC", "billing moves to the LLC", "Arthur", "Mar 1",
     "Arthur's Feb 13 Jenkins email: $62 a month now, after the issue comment's ~$95 (he shut down the extra backend copy)", "trap", ["STACKS"])
item("Build machines", "-", "HG", 0, "HG", "go through Sunset's sale", "-", "-", "#executives Feb 11: Sunset liquidates laptops and build machines; Arthur's issue note (the Jenkins jobs move to his own machine)")
item("Metabase", "CF", "Founder", 100, "Arthur", "already on Arthur's Kub card", "Arthur", "-", "Arthur's Feb 13 email: $100, carried through May", "trap", ["COMPLETE"])
item("dbt", "CF", "Founder", 100, "Arthur", "already on Arthur's Kub card", "Arthur", "-", "Arthur's Feb 13 email: $100, carried through May", "trap", ["COMPLETE"])
item("GitHub", "CF", "Founder", 48, "Arthur", "already on Arthur's Kub card; repos transfer after the data is delivered", "Arthur", "-",
     "Arthur's Feb 13 email: $48 team plan; checklist: transfer after the data is sold", "trap", ["COMPLETE"])
item("Singular", "-", "HG", 0, "HG", "terminated", "-", "-", "#winddown Feb 12: termination sent")
item("AppsFlyer", "CF", "LLC", 0, "LLC", "set up the free tier for attribution", "Leonard", "Mar 1", "#winddown Feb 12: free up to 15K installs")
item("Google Analytics", "-", "HG", 0, "HG", "stays with HG until the data is out", "-", "-", "#winddown Feb 12 action items")
item("Figma", "-", "HG", 0, "HG", "HG's prepaid plan, lapses Sep 11", "-", "-", "Leonard's issue note; Robert, #winddown Feb 12: good until September 11th")
item("layer.ai", "CF", "HG", 0, "HG", "export Combo Fighter's art before access ends Mar 3", "Robert", "by Mar 3",
     "#prototype Feb 11: cancelled, access until March 3rd; Leonard's Feb 12 reply under it: CF's character concept art is only in layer.ai, Robert to pull it out himself", "trap", ["DATE"])
item("Soundly", "-", "HG", 0, "HG", "cancelled", "-", "-", "Robert, #winddown Feb 11: Soundly canceled")
item("Kapwing", "-", "HG", 0, "HG", "cancelled (Pro to Feb 25)", "-", "-", "Arthur's issue note, matching Kapwing's Feb 12 notice in his mailbox")
item("Cursor", "-", "HG", 0, "HG", "cancelled", "-", "-", "Arthur, #winddown Feb 12: cursor cancelled")
item("CodeRabbit", "-", "HG", 0, "HG", "cancelled", "-", "-", "Arthur, #winddown Feb 12: coderabbit is cancelled")
item("Unity Pro", "-", "HG", 0, "HG", "terminated", "-", "-", "Leonard's Feb 12 note to Unity: terminating effective immediately")
item("Zapier", "-", "HG", 0, "HG", "cancelled", "-", "-", "checklist: Zapier (Leonard) done")
item("Helpshift", "-", "HG", 0, "HG", "cancelled", "-", "-", "#winddown Feb 11: cancelling without a hassle")
item("Domino Delights player support", "DD", "LLC", 0, "LLC", "get a support build approved and released before Helpshift stops on Feb 28", "Arthur", "by Feb 28",
     "App Store Connect Feb 13: the submission with the change was not approved, so work is left (Todo, not Done)", "trap", ["DONE", "CORR", "AUTH"])
item("Slack", "-", "HG", 0, "HG", "three paid members, kept for the data", "-", "-", "checklist: Slack down to 3 FT members")
item("Google Workspace", "-", "HG", 0, "HG", "archive unused accounts after Feb 15", "-", "-", "checklist: Google")
item("Linear", "-", "HG", 0, "HG", "kept during the transition", "-", "-", "#winddown Feb 12: linear we keep during transition")
item("Deel", "-", "HG", 0, "HG", "kept during the shutdown", "-", "-", "#winddown Feb 12 keep list")
item("Gusto", "-", "HG", 0, "HG", "kept during the shutdown", "-", "-", "#winddown Feb 12 keep list")
item("Intuit", "-", "HG", 0, "HG", "kept for the next two months", "-", "-", "#winddown Feb 12 keep list")
item("Carta", "-", "HG", 0, "HG", "renewal 8/15, no rush", "-", "-", "checklist: Carta")
item("Apple developer account", "-", "HG", 0, "HG", "stays with HG; Combo Fighter's listing moves out of it", "-", "-", "Leonard's issue note")
item("Google Play developer account", "-", "HG", 0, "HG", "stays with HG", "-", "-", "Leonard's issue note")
item("Calm Play LLC", "-", "HG", 0, "HG", "goes with Sunset's sale (a Harmony Games subsidiary)", "-", "-",
     "ground rules: the LLC is the new one Leonard and Arthur set up; #admin_foundersonly 2023: a fully owned HG subsidiary (rev4: EXC purged, a control row)")
item("Unity Ads balance", "CF", "HG", 0, "HG", "one-off $100 for this week's playable test", "-", "-", "#prototype Feb 11: the $100 we have")
item("Playable vendor", "CF", "HG", 0, "HG", "one-off, not monthly", "-", "-", "#executives Feb 3: $3,750 for the first playable")
item("Combo Fighter VO campaign", "CF", "LLC", 3000, "LLC", "billing moves from Leonard's card to the LLC", "Leonard", "Mar 1",
     "#prototype Feb 6 ($100/day), #executives Feb 7 (kept live), Leonard's Feb 12 status ($3,000 a month cap)", "trap", ["FILT"], issue=False)
LOOKED_AT_OUT = [("BoomBit publishing test", "a publishing test, not a charge"), ("CrazyGames web licence", "a licence, not a charge")]

ISSUES = [m for m in C if m["issue"]]
for n, m in enumerate(ISSUES):
    m["linear"] = f"ENG-{2438 + n}"
CASH = sum(m["cost"] for m in C if m["decision"] == "LLC")
CARRIED = sum(m["cost"] for m in C if m["decision"] == "Founder")
TOTAL = CASH + CARRIED
THIRD = TOTAL / 3
SHARES = {"Leonard": THIRD, "Robert": THIRD, "Arthur": THIRD - CARRIED}
COUNTS = {d: sum(1 for m in C if m["decision"] == d) for d in ("LLC", "Founder", "HG")}
assert (CASH, CARRIED, TOTAL, THIRD) == (3202, 248, 3450, 1150), (CASH, CARRIED, TOTAL, THIRD)
assert len(ISSUES) == 37 and len(C) == 38 and COUNTS == {"LLC": 7, "Founder": 3, "HG": 28}, COUNTS
assert 183.11 >= 140 and 183.11 < 300   # the take test flips on the hosting figure
for m in C:
    if m["linear"] if m["issue"] else False:
        pass


def write(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=1)
        f.write("\n")


# ---------------------------------------------------------------- manifest
ctx = {k: CTX[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")}
REQ = {
    "R1": "take test per game: Combo Fighter comes over either way; Domino Delights and Zombie Match only if January's warehouse income covers their own hosting (decision per game)",
    "R2": "transfer steps: owner and by-date for each item the LLC takes; an item's own deadline keeps it (Domino Delights player support before Feb 28, layer.ai export before Mar 3), everything else by March 1 (owner and by-date)",
    "R3": "monthly cost per item at what it bills now, going by whoever runs it (monthly cost)",
    "R4": "the split: each founder carries a third of the LLC's monthly cost; what one already pays personally counts toward his third and he puts the difference in as cash (three shares per month)",
    "R5": "the plan sheet in Robert's Drive, laid out like Leonard's draft (Item, Game, Decision, Monthly cost, Paid by, Next step, Owner, By), shared with Leonard and Arthur, with the three shares per month",
    "R6": "scope: every item that still bills each month for a game the LLC takes, including one the project lacks (a row and a new issue)",
    "R7": "the call recorded on each candidate issue: a comment and a state (Done when a founder pays it himself through May or the LLC takes it with nothing left to do; Todo with whoever moves it when the LLC takes it and something is still to do; Canceled when it stays with HG)",
    "R8": "the vehicle: the new LLC Leonard and Arthur are setting up; anything Harmony Games owns comes to it only through Sunset's sale (decision for HG-owned entities)",
    "R9": "a reply in Leonard's DM thread with what Robert would do, what it costs each founder a month and the sheet's link, before Monday's call",
    "R10": "January income per game from the warehouse revenue table (income compared with hosting)",
    "R11": "items a founder already pays personally, with their monthly amount (paid by)",
}
services = {
    "slack": {"role": "hub DM (anchor); #winddown keep list, checklist and Arthur's card moves; Arthur's DM correction under an unrelated root; Leonard's #prototype campaign status and his reply under the layer.ai access-date post; #executives lifestyle and auction posts; the reply", "weight_reason": "the ask, the stale hosting figures and the correction that beats them, the campaign outside every list and the reply live in Slack"},
    "linear": {"role": "the LLC project (anchor) with 37 candidate issues and owners' notes; the decision comment and state on each; the new campaign issue", "weight_reason": "the cohort, each item's own notes and the per-issue writes live only in Linear (no bulk comment read)"},
    "gdocs": {"role": "Leonard's ground rules doc (H1) and his superseded Feb 10 notes doc (same-service decoy)", "weight_reason": "the take test, the window, the costing rule and the vehicle rule"},
    "gmail": {"role": "Leonard's split email (H3); Arthur's billing email (completion elsewhere); Arthur's Jenkins email (CF's stacks at $62 now); the App Store Connect notice (the done gap's missing piece); base Deel and SVB notices (controls)", "weight_reason": "the split rule, Arthur's carried amount, CF's current stacks figure and the unreleased support build are only in mail"},
    "snowflake": {"role": "ANALYTICS.MONETIZATION.REVENUE_DAILY (H2), base only", "weight_reason": "January income per game decides the take test"},
    "gsheets": {"role": "Leonard's Feb 10 draft (layout source, stale numbers); the plan sheet (write)", "weight_reason": "the layout the hub asks for and the graded register"},
    "gdrive": {"role": "Robert's root folder (write home); Drive rows of the seeded docs, sheet and deck", "weight_reason": "the plan sheet must sit in Robert's own Drive"},
    "gcal": {"role": "Leonard's Monday decision call (deadline for the reply)", "weight_reason": "the reply's deadline and audience"},
    "trello": {"role": "Leonard's 'LLC: what we take from HG' card on the founders' board (the moving rule); read only", "weight_reason": "owners and by-dates come from the card's rule"},
    "github": {"role": "GameOfDominoes#1917 'Replace Helpshift with support email', merged by Arthur (the done claim's support)", "weight_reason": "the done claim cites the merge; only the store notice shows it never shipped"},
    "gslides": {"role": "Robert's Feb 5 'Combo Fighter: next 90 days' deck (campaign at $100/day through May)", "weight_reason": "a second record of the campaign's monthly rate for the window"},
    "confluence": {"role": "page_aws_infra cost note (estimates only; decoy for hosting)", "weight_reason": "the only record of the AWS account layout per title (dev/prod/analytics)"},
}
anchors = [
    {"id": "AN1", "service": "slack", "locator": IDS["hub"], "prompt_reference": "Leonard's DM from Thursday night", "requirement_ids": ["R5", "R7", "R9"]},
    {"id": "AN2", "service": "linear", "locator": f"linear:project/{IDS['project']}", "prompt_reference": "the LLC project in Linear", "requirement_ids": ["R7"]},
]


def frag(fid, service, container, kind, via, seeded, by, quote, reqs, names=None, base=None):
    return {"id": fid, "service": service, "container": container, "locator": container, "kind": kind,
            "incorporated_via": via, "seeded_ids": seeded, "base_pointers": base or [], "delegated_by_record": by,
            "delegation_quote": quote, "requirement_ids": reqs, "names_authorities": names or []}


H = IDS
fragments = [
    frag("K1", "slack", H["hub"], "delegation", ["AN1"], [H["hub"]], H["hub"], "go through them and make the call on each one",
         ["R5", "R6", "R7", "R9"], [{"id": "H1", "quote": "the ground rules doc"}, {"id": "H3", "quote": "how we split the money"}]),
    frag("K2", "gdocs", H["ground_rules"], "requirement", ["AN1", "K1"], [H["ground_rules"]], H["hub"], "the ground rules doc has how we decide",
         ["R1", "R3", "R8", "R10"], [{"id": "H2", "quote": "the warehouse's daily revenue table"}]),
    frag("K3", "linear", f"linear:project/{H['project']}", "requirement", ["AN1", "K1"], [H["project"]], H["hub"],
         "I put everything we might need from HG into the LLC project in linear, one issue each", ["R6", "R7"]),
    frag("K4", "gsheets", H["draft_sheet"], "format", ["AN1", "K1"], [H["draft_sheet"]], H["hub"], "lay the sheet out like my draft from Tuesday", ["R5"]),
    frag("K5", "gmail", H["split_thread"], "requirement", ["AN1", "K1"], [H["split_thread"]], H["hub"], "I'll email you how we split the money", ["R4", "R11"]),
    frag("K6", "trello", H["trello_card"], "requirement", ["AN1", "K1", "K2"], [H["trello_card"]], H["ground_rules"], "How things move is on the LLC card on our board", ["R2"]),
    frag("K7", "slack", BASE["keep_list"], "requirement", ["AN1", "K1", "K2"], [], H["ground_rules"], "What we already decided to keep or cancel for the shutdown in #winddown stays decided", ["R3"], base=[BASE["keep_list"]]),
    frag("K8", "slack", BASE["checklist"], "requirement", ["AN1", "K1", "K2"], [], H["ground_rules"], "What we already decided to keep or cancel for the shutdown in #winddown stays decided", ["R6"], base=[BASE["checklist"]]),
    frag("K9", "slack", BASE["lifestyle"], "requirement", ["AN1", "K1", "K2"], [], H["ground_rules"], "the lifestyle route I posted about in #executives", ["R8"], base=[BASE["lifestyle"]]),
    frag("K10", "slack", BASE["auction"], "requirement", ["AN1", "K1", "K2"], [], H["ground_rules"], "the way I wrote after the call on Wednesday", ["R8"], base=[BASE["auction"]]),
    frag("K11", "gcal", H["monday_evt"], "destination", ["AN1", "K1"], [H["monday_evt"]], H["hub"], "we decide on Monday's call", ["R9"]),
    frag("K12", "slack", BASE["helpshift_feb28"], "requirement", ["AN1", "K1", "K2", "K6"], [], H["trello_card"], "Anything that already has its own deadline keeps it", ["R2"], base=[BASE["helpshift_feb28"]]),
    frag("K13", "slack", BASE["layer_mar3"], "requirement", ["AN1", "K1", "K2", "K6"], [H["layer_reply"]], H["trello_card"], "Anything that already has its own deadline keeps it", ["R2"], base=[BASE["layer_mar3"]]),
]
authorities = [
    {"id": "H1", "name": "the ground rules doc", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R1", "R3", "R8"],
     "findable_query": "LLC ground rules", "seeded_ids": [H["ground_rules"]], "base_pointers": [],
     "decoy_seeded_ids": [H["notes_doc"]], "decoy_base_pointers": []},
    {"id": "H2", "name": "the warehouse's daily revenue table", "home_service": "snowflake", "decoy_service": "slack", "governs": ["R10"],
     "findable_query": "REVENUE_DAILY", "seeded_ids": [], "base_pointers": [BASE["revenue"]],
     "decoy_seeded_ids": [], "decoy_base_pointers": [BASE["boombit_retention"]],
     "decoy_scope": {"dimension": "issuer", "decoy": "BoomBit's publishing-test dashboard (retention, installs) for its own campaign",
                     "task": "Harmony Games' own January income per game in the warehouse"}},
    {"id": "H3", "name": "Leonard's split email", "home_service": "gmail", "decoy_service": "slack", "governs": ["R4"],
     "findable_query": "split", "seeded_ids": [H["split_thread"]], "base_pointers": [],
     "decoy_seeded_ids": [], "decoy_base_pointers": [BASE["recap_proforma"]]},
]
surfaces = [
    {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": 37, "seeded": True,
     "seeded_ids": [m["linear"] for m in ISSUES][:5], "requirement": "R3", "decides": "monthly cost",
     "why_no_bulk": "linear_list_issues returns titles and states but no comments; each issue's notes need its own linear_list_comments",
     "short_circuit": "each issue's owner notes carry that item's own status and figure; no other record lists all 37, so skipping the read leaves the row's cost and decision unsourced"},
    {"service": "slack", "tool": "slack_search_public_and_private (per item name)", "per_record_calls": 0.5, "records": 40,
     "requirement": "R6", "decides": "every item that still bills each month for a game the LLC takes",
     "why_no_bulk": "no channel holds every item's latest status; #winddown covers subscriptions only and DMs are not in any channel history read",
     "short_circuit": "the newer statement that changes an item (hosting, campaign, cancellations) sits in a DM or another channel per item; one search cannot return them all without the item's own name"},
    {"service": "gmail", "tool": "gmail_search_messages (per item name)", "per_record_calls": 0.3, "records": 40,
     "requirement": "R11", "decides": "paid by",
     "why_no_bulk": "gmail_search returns ids only; the vendor notices and Arthur's billing note are found per name",
     "short_circuit": "who already pays an item and the store notice for DD player support exist only in mail"},
]
cohort = {"definition": "every item in Leonard's LLC project (37 candidate issues) plus every monthly charge for a taken game found outside it (the Combo Fighter VO campaign) and two looked-at non-charges (BoomBit test, CrazyGames licence): 40 looked at, 38 graded rows",
          "definition_source": [H["hub"], H["project"], H["ground_rules"]], "key": "item", "size": 40, "evidence_surfaces": surfaces}

chains = [
    {"id": "C1", "root_cause": "A11", "ends_in": "R3", "hops": [
        {"service": "slack", "record": BASE["dd_aws_1k"], "finding": "Arthur Feb 9: DD production account costs ~$1k a month"},
        {"service": "slack", "record": BASE["dd_aws_300"], "finding": "Arthur Feb 10: might be easy to get to 300"},
        {"service": "linear", "record": H["c_dd_prod"], "finding": "Leonard's note on the DD production issue repeats ~$1k / $300"},
        {"service": "slack", "record": H["arthur_dm"], "finding": "Arthur Feb 13 (DM reply under a git-debugging root): $140 a month now"}]},
    {"id": "C2", "root_cause": "A13", "ends_in": "R1", "hops": [
        {"service": "gdocs", "record": H["ground_rules"], "finding": "take test: January income from the warehouse revenue table covers own hosting"},
        {"service": "snowflake", "record": BASE["revenue"], "finding": "January 2026: domino_delights $183.11, zombie_match_3d $0.00 (SUM over grain rows)"},
        {"service": "slack", "record": H["arthur_dm"], "finding": "DD hosting $140 < $183.11: DD comes over; ZM does not"}]},
    {"id": "C3", "root_cause": "A25", "ends_in": "R11", "hops": [
        {"service": "slack", "record": BASE["action_items"], "finding": "Leonard Feb 12: keep Metabase and dbt, ~$300/month"},
        {"service": "slack", "record": BASE["arthur_kub"], "finding": "Arthur Feb 12: I'll be moving github, dbt and Metabase to my KubLLC card"},
        {"service": "linear", "record": H["c_metabase"], "finding": "Leonard's Metabase note: about $300 a month with dbt"},
        {"service": "gmail", "record": H["arthur_thread"], "finding": "Arthur Feb 13: on my Kub card, $248 a month, I carry them through May as my part"}]},
    {"id": "C4", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "slack", "record": BASE["helpshift_feb28"], "finding": "Leonard Feb 11: move DD and ZM off Helpshift before Feb 28"},
        {"service": "linear", "record": H["c_support"], "finding": "Arthur's comment: done, support goes to email (merged in #1917)"},
        {"service": "github", "record": H["pr"], "finding": "#1917 merged Feb 12"},
        {"service": "gmail", "record": H["asc_thread"], "finding": "App Store Connect Feb 13: the DD submission with the change was not approved"},
        {"service": "linear", "record": f"linear:project/{H['project']}", "finding": "project description: Done only when nothing is left to do, so ENG-2462 stays Todo with Arthur"}]},
    {"id": "C5", "root_cause": "A17", "ends_in": "R6", "hops": [
        {"service": "slack", "record": BASE["vo_budget"], "finding": "Leonard Feb 6: VO campaign budget $100/day"},
        {"service": "slack", "record": BASE["keep_live"], "finding": "Leonard Feb 7: I will keep both campaigns live"},
        {"service": "gslides", "record": H["cf_deck"], "finding": "Robert's deck: run the VO campaign at $100/day (~$3k a month) through May"},
        {"service": "slack", "record": H["vo_status"], "finding": "Leonard Feb 12: only the VO campaign still runs, capped at $3,000 a month, on the LLC from March"}]},
    {"id": "C7", "root_cause": "A4", "ends_in": "R2", "hops": [
        {"service": "linear", "record": ISSUES[16]["linear"], "finding": "Leonard's note on the layer.ai issue: cancelled it on the 11th (reads as closed)"},
        {"service": "slack", "record": BASE["layer_mar3"], "finding": "Leonard Feb 11: layer.ai cancelled, access until March 3rd"},
        {"service": "slack", "record": H["layer_reply"], "finding": "Leonard Feb 12 reply under it: CF's character concept art is only in layer.ai, Robert to pull it out himself before then"},
        {"service": "trello", "record": H["trello_card"], "finding": "an item's own deadline keeps it: export by Mar 3, owner Robert"}]},
    {"id": "C8", "root_cause": "A11", "ends_in": "R3", "hops": [
        {"service": "linear", "record": H["c_cf_backend"], "finding": "Arthur's note on ENG-2445 (Feb 13 00:58Z): CF's own account about $95 a month"},
        {"service": "linear", "record": H["c_build"], "finding": "Arthur's note on ENG-2446 (01:07Z): the Jenkins jobs move to his own machine"},
        {"service": "gmail", "record": H["jenkins_thread"], "finding": "Arthur's Feb 13 04:20Z email 'jenkins': jobs moved; the extra CF backend copy shut down, CF's account bills $62 a month now"},
        {"service": "gdocs", "record": H["ground_rules"], "finding": "costing rule: what it bills now, going by whoever runs it"}]},
]


def trap(tid, family, services_, seeded, base, req, wrong, resolver, order=None, versions=None, dtype=None):
    t = {"id": tid, "family": family, "services": services_, "seeded_ids": seeded, "base_pointers": base, "requirement": req,
         "expected_wrong_reading": wrong, "resolver": resolver}
    if dtype:
        t["distractor_type"] = dtype
    if order:
        t["discovery_order"] = order
    if versions:
        t["version_records"] = sorted(versions, key=lambda r: r["at"])     # the records' real time order
    return t


def v(service, rid, seeded, at, container=None):
    r = {"service": service, ("id" if seeded else "base_pointer"): rid, "seeded": seeded, "at": at}
    if container:
        r["container"] = container
    return r


traps = [
    trap("T1", "superseding", ["slack", "gdocs", "gsheets", "linear"], [H["arthur_dm"], H["c_dd_prod"], H["notes_doc"], H["draft_sheet"]],
         [BASE["dd_aws_1k"], BASE["dd_aws_300"]], "R3",
         "Domino Delights' servers cost about $1k a month (or the $300 Arthur hoped for), so DD cannot cover its hosting and stays with HG",
         "Arthur's Feb 13 DM reply under an unrelated git-debugging root: the trimmed production account bills $140 a month from March; the costing rule makes the person who runs it the authority",
         order="#winddown (swept every run) and the issue note give ~$1k / $300; the DM reply sits under a Feb 2 root about git commands",
         versions=[v("slack", BASE["dd_aws_1k"], False, "2026-02-09T23:49:44Z", f"slack:{BASE['dd_aws_1k']}"),
                   v("slack", BASE["dd_aws_300"], False, "2026-02-10T00:10:19Z", f"slack:{BASE['dd_aws_300']}"),
                   v("gdocs", H["notes_doc"], True, T["notes_doc"], f"file:{H['notes_doc']}"),
                   v("gsheets", H["draft_sheet"], True, T["draft_sheet"], f"file:{H['draft_sheet']}"),
                   v("linear", H["c_dd_prod"], True, T["c_dd_prod"], f"linear:{ISSUES[3]['linear']}"),
                   v("slack", H["arthur_dm"], True, T["arthur_dm"], f"slack:{BASE['dm_ra_root']}")]),
    trap("T2", "exact_predicate", ["snowflake", "gdocs", "slack"], [H["ground_rules"]], [BASE["revenue"], BASE["dd_less_1k"]], "R10",
         "DD's income is guessed from 'we make way less than $1K', averaged over grain rows or taken from February's partial month",
         "REVENUE_DAILY summed for domino_delights over January 2026: $183.11 (zombie_match_3d $0.00); the ground rules name January and the table",
         order="Slack's vague figure is met first; the warehouse is opened only by a run that follows the ground rules to it"),
    trap("T3", "exact_predicate", ["slack", "gslides", "linear"], [H["vo_status"], H["cf_deck"]], [BASE["vo_budget"], BASE["keep_live"]], "R6",
         "the project's 37 issues and the #winddown lists are every monthly charge, so Combo Fighter costs only tools and hosting",
         "Combo Fighter's VO campaign ($100/day capped at $3,000 a month) still bills and is in no list; the ground rules count every monthly charge for a taken game, so it gets a row and a new issue",
         order="every list the run reads (project, keep list, checklist, Arthur's moves) omits it, and (rev4) no record that carries it uses the project word 'LLC'; it is in Feb 6-12 #prototype / #executives history and Robert's deck"),
    trap("T4", "completion_elsewhere", ["slack", "linear", "gmail"], [H["c_metabase"], H["arthur_thread"]], [BASE["action_items"], BASE["arthur_kub"]], "R11",
         "Metabase, dbt and GitHub are about $300 a month of LLC cash split three ways",
         "Arthur's Feb 13 email: they already bill his own card, $248 a month, and he carries them through May as his part, so they leave the cash need and count toward his third",
         order="the Metabase issue note and #winddown come first; the completion is in an email to Robert",
         versions=[v("slack", BASE["checklist"], False, "2026-02-12T21:57:30Z", f"slack:{BASE['checklist']}"),
                   v("slack", BASE["action_items"], False, "2026-02-12T22:05:03Z", f"slack:{BASE['action_items']}"),
                   v("slack", BASE["arthur_kub"], False, "2026-02-12T23:00:32Z", f"slack:{BASE['arthur_kub']}"),
                   v("linear", H["c_metabase"], True, T["c_metabase"], f"linear:{ISSUES[9]['linear']}"),
                   v("gmail", H["arthur_thread"], True, T["arthur_mail"], f"gmail:{H['arthur_thread'].split('/')[1]}")]),
    trap("T5", "done_gap", ["linear", "github", "gmail", "slack"], [H["c_support"], H["pr"], H["asc_thread"]], [BASE["helpshift_feb28"]], "R2",
         "DD player support is done: Arthur's comment says support goes to email and #1917 is merged, so nothing is left to do and the issue goes to Done",
         "the App Store Connect notice in Robert's mailbox: the DD submission with the change was not approved, so the live build still opens Helpshift; a release before Feb 28 is left to do, so the issue is Todo with Arthur",
         order="the issue comment and the merged PR read as done; the missing piece is a store notice among Robert's TestFlight mail",
         versions=[v("slack", BASE["helpshift_feb28"], False, "2026-02-11T05:58:54Z", f"slack:{BASE['helpshift_feb28']}"),
                   v("linear", H["c_support"], True, T["c_support"], f"linear:{ISSUES[24]['linear']}"),
                   v("gmail", H["asc_thread"], True, T["asc_notice"], f"gmail:{H['asc_thread'].split('/')[1]}")]),
    trap("T7", "exact_predicate", ["slack", "trello", "linear"], [H["trello_card"], H["layer_reply"]], [BASE["layer_mar3"]], "R2",
         "the layer.ai item is cancelled and closed (its issue note says only that), so it needs no step, or every step moves by March 1",
         "Leonard's Feb 11 #prototype post (access until March 3rd) and his Feb 12 reply under it (CF's character concept art is only in layer.ai; Robert to pull it out himself); the ground rules bring a game's art over and the card keeps an item's own deadline, so Robert exports the art by Mar 3",
         order="the issue note and the checklist read as closed; the art and the date are only in the #prototype post and its reply, found by an item-name search"),
    trap("T8", "stale_summary", ["gsheets"], [H["draft_sheet"]], [], "R3",
         "Leonard's Feb 10 draft holds the plan's numbers (DD servers ~1000, Metabase + dbt ~300)", "the draft predates Arthur's trim and moves; the hub uses it for layout only and the costing rule goes by whoever runs each item now",
         dtype="stale_summary"),
    trap("T9", "distractor", ["slack"], [], [BASE["unity_100"]], "R6",
         "the $100 left on Unity Ads is a monthly marketing line", "a one-off balance for one playable test, not a monthly charge", dtype="scope_adjacent"),
    trap("T10", "superseding", ["slack", "gmail"], [H["split_thread"]], [BASE["recap_25k"], BASE["recap_proforma"]], "R4",
         "each founder puts in $25K (Leonard's Jan 6 and Jan 14 recap plan)", "that was the recapitalisation of HG, dropped when the shutdown was decided; Leonard's Feb 13 split email governs the LLC (a third each, personal costs counted)",
         dtype="withdrawn_ask", order="the January #executives pro forma comes back from any 'founders invest' or '$25K' search; the split is in mail",
         versions=[v("slack", BASE["recap_25k"], False, "2026-01-06T20:19:44Z", f"slack:{BASE['recap_25k']}"),
                   v("slack", BASE["recap_proforma"], False, "2026-01-14T19:09:44Z", f"slack:{BASE['recap_proforma']}"),
                   v("gmail", H["split_thread"], True, T["split_mail"], f"gmail:{H['split_thread'].split('/')[1]}")]),
    trap("T16", "superseding", ["gslides", "slack"], [H["cf_deck"], H["vo_status"]], [BASE["vo_off_q"], BASE["keep_live"]], "R6",
         "Leonard turned the VO campaigns off on Feb 7 (he asked whether he should)", "the same day he kept both live, and his Feb 12 status says only the VO campaign still runs, capped at $3,000 a month",
         order="the turn-off question is the first campaign hit in #executives; the answer is a separate root that evening",
         versions=[v("gslides", H["cf_deck"], True, T["cf_deck"], f"file:{H['cf_deck']}"),
                   v("slack", BASE["vo_off_q"], False, "2026-02-07T04:22:49Z", f"slack:{BASE['vo_off_q']}"),
                   v("slack", BASE["keep_live"], False, "2026-02-07T18:44:56Z", f"slack:{BASE['keep_live']}"),
                   v("slack", H["vo_status"], True, T["vo_status"], f"slack:{BASE['vo_root']}")]),
    trap("T17", "superseding", ["slack"], [], [BASE["repos_llc"], BASE["checklist"]], "R2",
         "the repos move to Arthur's LLC now (his Feb 11 reply)", "Leonard's Feb 12 checklist: keep GitHub under HG until the data is sold, then transfer, so the repo step comes after the data is delivered",
         versions=[v("slack", BASE["repos_llc"], False, "2026-02-11T20:35:37Z", f"slack:{BASE['repos_llc']}"),
                   v("slack", BASE["checklist"], False, "2026-02-12T21:57:30Z", f"slack:{BASE['checklist']}")]),
    trap("T18", "distractor", ["slack"], [], [BASE["leapblock"]], "R3",
         "Leonard's ~$600 for Leapblock is an LLC monthly cost", "it is a one-time February gesture from HG to Martin's agency, not a charge for a game the LLC takes", dtype="other_title"),
    trap("T11", "distractor", ["slack"], [], [BASE["boombit_retention"]], "R10",
         "DD is doing better with BoomBit, so it pays its way", "BoomBit's test dashboard is the publisher's own campaign view; the take test reads January income in the warehouse", dtype="non_authoritative_instruction"),
    trap("T12", "distractor", ["snowflake"], [], [BASE["revenue"]], "R10",
         "February's $62.56 (to Feb 9) is DD's income", "the ground rules name January; February is a partial month", dtype="partial_listing"),
    trap("T13", "distractor", ["slack"], [], [BASE["calm_future"]], "R8",
         "'Calm Play is something we can also use in the future' (2023) makes it the founders' own vehicle", "the same founders made it a full HG subsidiary days later, and the ground rules name the new LLC; a distractor around the Calm Play control row (rev4: EXC purged)", dtype="lookalike_entity"),
    trap("T14", "near_miss_mention", ["slack"], [], [BASE["checklist"]], "R11",
         "the checklist's 'keep it until Robert stops caring about data' means HG keeps paying Metabase and dbt", "Arthur's later email: they bill his own card, carried through May"),
    trap("T15", "distractor", ["confluence"], [], [BASE["aws_guide"]], "R3",
         "the Confluence cost note (~$650 Fargate, ~$420 Aurora ...) is what hosting costs", "the page calls itself estimates only (Dec 31); Arthur's Feb 13 figure is what the account bills now", dtype="near_duplicate_record"),
    trap("T19", "superseding", ["linear", "gmail"], [H["c_cf_backend"], H["jenkins_thread"]], [], "R3",
         "Combo Fighter's backend and auth stacks cost about $95 a month (Arthur's own note on the issue)",
         "Arthur's later email 'jenkins' (Feb 13 04:20Z): he shut down the extra CF backend copy, so the account bills $62 a month now; the costing rule takes what it bills now from whoever runs it",
         order="the issue note is read on every run and looks final; the correction is the second paragraph of an email about the Jenkins move, whose snippet names neither CF's cost nor the project",
         versions=[v("linear", H["c_cf_backend"], True, T["c_cf_backend"], f"linear:{ISSUES[7]['linear']}"),
                   v("gmail", H["jenkins_thread"], True, T["jenkins_mail"], f"gmail:{H['jenkins_thread'].split('/')[1]}")]),
]
PRIOR_IDS = {  # hardness_ledger.py priors --model claude-opus-5-5 --family <f> --json, refreshed 2026-11-05 after the rev3 pre-check (rev4)
    "superseding": ["hev_e61e07235eadbd24", "hev_1ceea0e7e912f48b", "hev_ebc012c844829411", "hev_264798d24d59191e", "hev_ae63566d7b1dc917",
                    "hev_0791c57922eeb614", "hev_febd018417f4bd36", "hev_26ecd3a4fc80313c", "hev_7fb791c864fb2acd", "hev_3a71c99557336ba6"],
    "exact_predicate": ["hev_9c403cae42eb4df8", "hev_c2297d21ba5cbc7b", "hev_0148aad4d8a4eb2d", "hev_2da16037a402bf13", "hev_b76760802056e969"],
    "completion_elsewhere": ["hev_13d86dcf23442708", "hev_34b1b726275909e0", "hev_d2253957e65e0329"],
    "done_gap": ["hev_7f44d83eaad625e9", "hev_522f1ca2bc9062de", "hev_b8f28a892a74b855", "hev_fa790909c7cd5693", "hev_f9b2298b6c9739d4"],
    "boundary_date": ["hev_3d96146a0a8b19a5"]}
portfolio = [
    {"id": "CORR", "mechanism": "A11", "prior_family": "superseding", "prior_family_reason": "same mechanism: a dated correction outside the swept channel replaces a figure every run reads",
     "nodes": ["T1", "C1", "T8", "T15"], "requirement": "R3", "natural_reading": "DD hosting is the #winddown / issue / draft figure (~$1k or $300)",
     "decides": ["G2", "C2", "P7", "R1", "R3", "R4", "V1"], "controls": ["Combo Fighter backend and auth stacks (AWS)"],
     "over_application": "corr_over: rewrites the CF backend stacks' cost from an unrelated DM line ($140)", "source": "dm-thread-reply", "signature": "Domino prod account $140"},
    {"id": "AUTH", "mechanism": "A13", "prior_family": "exact_predicate", "prior_family_reason": "closest library family: the deciding value sits in a rarely opened structured service and the month/grain predicate decides it",
     "nodes": ["T2", "C2", "T11", "T12"], "requirement": "R10", "natural_reading": "DD's income is what Slack says about it",
     "decides": ["G2", "G3", "R4", "R7"], "controls": ["Combo Fighter"],
     "over_application": "auth_over: applies the take test to Combo Fighter and drops it for $7.36 of January income", "source": "warehouse", "signature": "REVENUE_DAILY January"},
    {"id": "FILT", "mechanism": "A17", "prior_family": "exact_predicate", "prior_family_reason": "same mechanism: an in-scope charge outside the obvious lists",
     "nodes": ["T3", "C5", "T9", "T16"], "requirement": "R6", "natural_reading": "the project and the #winddown lists are the population of monthly charges",
     "decides": ["C1", "L1", "P7", "R1", "R3", "R5", "V1"], "controls": ["Unity Ads balance", "Playable vendor"],
     "over_application": "filt_over: adds the one-off Unity Ads balance and the playable vendor as monthly LLC lines", "source": "channel-history", "signature": "VO campaign $100/day"},
    {"id": "COMPLETE", "mechanism": "A25", "prior_family": "completion_elsewhere", "prior_family_reason": "same mechanism: a completion note away from the request",
     "nodes": ["T4", "C3", "T14"], "requirement": "R11", "natural_reading": "everything on the keep list is LLC cash split three ways",
     "decides": ["I1", "P7", "R1", "R2", "L2"], "controls": ["Build machines"],
     "over_application": "complete_over: treats the build machines as Arthur's own because they sit at his house", "source": "mail-by-name", "signature": "Kub card $248 carried through May"},
    {"id": "DONE", "mechanism": "A24", "prior_family": "done_gap", "prior_family_reason": "same mechanism: a done claim on the issue and a merged PR, the missing piece in a store notice",
     "nodes": ["T5", "C4"], "requirement": "R2", "natural_reading": "Arthur's done and the merged PR mean the store build has it",
     "decides": ["C3", "R6"], "controls": ["Helpshift"],
     "over_application": "done_over: adds a release check to the Helpshift item, which is only cancelled", "source": "store-notice", "signature": "submission issue support option email draft does nothing"},
    {"id": "DATE", "mechanism": "A4", "prior_family": "boundary_date", "prior_family_reason": "same mechanism: base cut-offs bound step dates (no Opus 5.5 prior yet)",
     "nodes": ["T7", "C7", "T17"], "requirement": "R2", "natural_reading": "every step moves by March 1",
     "decides": ["C4", "C5"], "controls": ["AppsFlyer"],
     "over_application": "date_over: dates AppsFlyer to Feb 28 as if it carried Helpshift's deadline", "source": "channel-history", "signature": "layer access until March 3"},
    {"id": "STACKS", "mechanism": "A11", "prior_family": "superseding", "prior_family_reason": "same mechanism: the owner's later figure in another service replaces the figure on the issue every run reads",
     "nodes": ["T19", "C8"], "requirement": "R3", "natural_reading": "CF's backend and auth stacks cost the ~$95 Arthur noted on ENG-2445",
     "decides": ["P1", "R2", "R3"], "controls": ["Domino Delights production account (AWS)"],
     "over_application": "stacks_over: also costs DD's production account at the Jenkins email's $62 as if the trim covered it", "source": "mail-second-paragraph", "signature": "extra CF backend copy shut down $62"},
]
for p in portfolio:   # ledger priors (claude-opus-5-5, hardness_ledger.py priors), record ids from the ledger
    p["prior"] = {"superseding": {"alpha": 1.0, "beta": 5.0}, "exact_predicate": {"alpha": 2.0, "beta": 4.0},
                  "completion_elsewhere": {"alpha": 1.0, "beta": 4.0}, "done_gap": {"alpha": 3.0, "beta": 3.0},
                  "boundary_date": {"alpha": 2.0, "beta": 1.0}}[p["prior_family"]]
    p["prior"]["record_ids"] = PRIOR_IDS[p["prior_family"]]
channels = [   # complexity channels as the solver declares them (solver.CHANNELS): degrade ch_miss = the member takes its rule's natural reading
    {"id": "CH-CORR", "kind": "scale", "rule": "CORR", "degrade": "ch_miss", "latent": "member", "family": "superseding", "source": "dm-thread-reply",
     "members": ["Domino Delights", "Domino Delights production account (AWS)", "Domino Delights player support"],
     "description": "Arthur's DM reply ($140, under an unrelated root) is not found: DD hosting stays ~$1k / $300"},
    {"id": "CH-AUTH", "kind": "scale", "rule": "AUTH", "degrade": "ch_miss", "latent": "member", "family": "exact_predicate", "source": "warehouse",
     "members": ["Domino Delights", "Zombie Match", "Zombie Match account (AWS)"],
     "description": "January income is not read from REVENUE_DAILY: DD is judged from Slack, ZM comes over"},
    {"id": "CH-FILT", "kind": "scale", "rule": "FILT", "degrade": "ch_miss", "latent": "member", "family": "exact_predicate", "source": "channel-history",
     "members": ["Combo Fighter VO campaign"], "description": "the VO campaign (in no list) is not found: no campaign row and no new issue"},
    {"id": "CH-COMPLETE", "kind": "scale", "rule": "COMPLETE", "degrade": "ch_miss", "latent": "member", "family": "completion_elsewhere",
     "source": "mail-by-name", "members": ["Metabase", "dbt", "GitHub"],
     "description": "Arthur's billing email is not found: Metabase and dbt become LLC cash"},
    {"id": "CH-DONE", "kind": "scale", "rule": "DONE", "degrade": "ch_miss", "latent": "member", "family": "done_gap", "source": "store-notice",
     "members": ["Domino Delights player support"], "description": "the App Store notice is not read: the support move looks finished"},
    {"id": "CH-DATE", "kind": "scale", "rule": "DATE", "degrade": "ch_miss", "latent": "member", "family": "boundary_date", "source": "channel-history",
     "members": ["layer.ai", "GitHub"], "description": "the item's own deadline is not applied: the layer export and the GitHub transfer get Mar 1"},
    {"id": "CH-STACKS", "kind": "scale", "rule": "STACKS", "degrade": "ch_miss", "latent": "member", "family": "superseding", "source": "mail-second-paragraph",
     "members": ["Combo Fighter backend and auth stacks (AWS)"], "description": "Arthur's Jenkins email is not read: CF's stacks stay at the issue note's ~$95"},
]

budget = [
    ("discovery", "slack", 12, "the hub DM, #winddown (3 pages: keep list, checklist, card moves), Feb #executives and #prototype, #company-internal, the Robert-Arthur and Robert-Oliver DMs"),
    ("rules", "gdocs", 2, "the ground rules doc (take test, window, costing and vehicle rules) and the notes doc it supersedes"),
    ("rules", "gsheets", 2, "Leonard's Feb 10 draft: the layout the hub asks for"),
    ("rules", "gmail", 3, "Leonard's split email; Arthur's billing email; the store notice"),
    ("rules", "trello", 2, "the LLC card on the founders' board (the moving rule)"),
    ("rules", "gcal", 2, "Monday's decision call (deadline and audience)"),
    ("rules", "linear", 3, "the project, its description (states) and the team's states"),
    ("rules", "snowflake", 4, "list, describe and the January revenue query per game"),
    ("per-record", "linear", 37, "each candidate issue's comments carry its own status and figure (no bulk comment read)"),
    ("per-record", "slack", 20, "a name search per item for a newer statement (hosting, campaign, cancellations) in DMs and other channels"),
    ("per-record", "gmail", 12, "a name search per item for who already pays it and its vendor or store notice"),
    ("reconciliation", "github", 2, "the repos per title and #1917 the done claim cites"),
    ("reconciliation", "confluence", 1, "the AWS account layout per title (dev, prod, analytics)"),
    ("reconciliation", "gdrive", 3, "Robert's root folder, the draft and the deck"),
    ("per-record", "linear", 37, "the decision comment on each candidate issue the hub asks for (no batch write)"),
    ("per-record", "linear", 37, "the state on each candidate issue the project description asks for (no batch write)"),
    ("writes", "linear", 1, "the new issue for the campaign the project lacks"),
    ("writes", "gsheets", 4, "create the plan sheet and write its rows and shares"),
    ("writes", "gdrive", 3, "move the sheet into Robert's root and share it with Leonard and Arthur"),
    ("writes", "slack", 1, "the reply in Leonard's DM thread"),
    ("read-back", "gsheets", 2, "read the plan back before replying"),
]
call_budget = [{"phase": ph, "service": s, "calls": c, "reason": r} for ph, s, c, r in budget]
TOTAL_BUDGET = sum(c for _, _, c, _ in budget)
PER_RECORD_SURF = round(sum(s["per_record_calls"] * s["records"] for s in surfaces))
writes = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 5, "depends_on": ["C1", "C2", "C3", "C5", "C7", "C8", "T3", "T4"], "requirements": ["R5", "R3", "R4", "R11"]},
    {"service": "gdrive", "tool": "gdrive_move_file+gdrive_share_file", "count": 3, "depends_on": ["K4"], "requirements": ["R5"]},
    {"service": "linear", "tool": "linear_create_comment+linear_update_issue", "count": 74, "depends_on": ["C1", "C3", "C4", "C7", "C8"], "requirements": ["R7", "R2"]},
    {"service": "linear", "tool": "linear_create_issue", "count": 1, "depends_on": ["C5", "T3"], "requirements": ["R6"]},
    {"service": "slack", "tool": "slack_send_message", "count": 1, "depends_on": ["C1", "C2", "C3", "C4", "C5", "C8"], "requirements": ["R9"]},
]
hazards = [
    {"hazard_id": "L13", "resolution": "excluded", "why_safe": "the work-after-announcement records (Combo-Fighters#37, the CodeRabbit comment, the unarchived repos) are neither modified nor cited; #1917 is a new dated merge that only adds to the same pattern"},
]
manifest = {
    "_note": "DRAFT manifest (scenario stage). Seeded ids are planned (minted in plan/build_scenario.py, collision-checked by plan/check_ids.py); /create-injection writes the final manifest.",
    "persona": "robert", "assignment_context": ctx, "horizon": "Long Horizon", "effective_profile": "extreme",
    "author_targets": {"counted_calls_every_run_gt": 130, "average_lt": 0.85, "design_E_avg_le": 0.77,
                       "source": "requester chat 2026-11-05 (delegated choices)"},
    "volume_exception": {"reason": "38 graded items (37 candidate issues and one outside charge); the per-issue read, decision comment and state give about 155-190 honest calls per run; reaching 500 would need padding, which fails on its own",
                         "requester_confirmation": "requester, Claude Code chat 2026-11-05: 'i want over 130 tool calls in each runs ... you can choose from your self which option is best fit for my requirements' (choice delegated; recorded in 00_Pre_Scenario_Analysis.md §10 decision 2)",
                         "call_budget_floor": 150, "per_record_floor": 60},
    "requirements": REQ, "services": services, "anchors": anchors, "ask_fragments": fragments, "authorities": authorities,
    "cohort": cohort, "chains": chains, "traps": traps, "mechanism_portfolio": portfolio, "channels": channels,
    "call_budget": call_budget, "writes": writes, "hazard_acknowledgements": hazards, "denied_probes": [],
    "gradable_surface": "01_Gradable_Surface.json",
}
write(os.path.join(WF, "01_Hardness_Manifest.draft.json"), manifest)

# ---------------------------------------------------------------- gradable surface
TRAP_GROUPS = {}
MS, CA, IN, LK, CO = "multi_source_reconciliation", "calculation", "interpretation", "lookup", "comparison"


def slot(sid, title, weight, kind, reason, cls, selector, role="core", group=None, mechs=(), fact=None, **kw):
    s = {"id": sid, "title": title, "weight": weight, "work_kind": kind, "work_reason": reason, "class": cls, "selector": selector,
         "role": role, "mechanisms": list(mechs)}
    if group:
        s["group"] = group
    if fact:
        s["fact_id"] = fact
    s.update(kw)
    return s


hub_ts = IDS["hub"].split("/")[1]
ROW = r"[ -~\u00a0-\uffff]"   # rev4: one printable character other than a newline, so a plan pattern stays inside one sheet row (pre-check: C4 matched "Feb 25" on the next row)
slots = [
    slot("G1", "Combo Fighter decision", 1, LK, "the ground rules say it comes over either way", "direct", ["field", "Combo Fighter", "Decision"], "sample", "games"),
    slot("G2", "Domino Delights decision", 5, MS, "January warehouse income vs the trimmed hosting in Arthur's DM, under the ground rules' take test", "direct",
         ["field", "Domino Delights", "Decision"], "sample", "games", ["CORR", "AUTH"]),
    slot("G3", "Zombie Match decision", 3, CO, "January warehouse income ($0.00) against the take test", "direct", ["field", "Zombie Match", "Decision"], "sample", "games", ["AUTH"]),
    slot("I1", "Metabase decision", 5, MS, "issue note and #winddown vs Arthur's later email that he carries it", "direct", ["field", "Metabase", "Decision"], "sample", "items", ["COMPLETE"]),
    slot("I2", "Calm Play LLC decision", 3, IN, "Leonard's issue note read against the ground rules' vehicle sentence (rev4: EXC purged, a control row)", "direct", ["field", "Calm Play LLC", "Decision"], "sample", "items"),
    slot("I3", "Figma decision", 1, LK, "Leonard's issue note: HG's prepaid plan, stays HG's and lapses Sep 11", "direct", ["field", "Figma", "Decision"], "sample", "items"),
    slot("I4", "Helpshift decision", 1, LK, "#winddown: cancelled", "direct", ["field", "Helpshift", "Decision"], "sample", "items"),
    slot("I5", "Cursor decision", 1, LK, "#winddown: cancelled", "direct", ["field", "Cursor", "Decision"], "sample", "items"),
    slot("V1", "number of LLC rows", 3, CA, "count of the plan's LLC rows (7): depends on DD's decision, the campaign row and who already carries Metabase and dbt", "aggregate", ["total", "LLC"],
         "volume", None, ["CORR", "AUTH", "FILT", "COMPLETE"], volume_for=["games", "items", "costs"]),
    slot("C1", "campaign row at its monthly rate", 5, MS, "the campaign is in no list: #prototype / #executives history, Robert's deck and Leonard's status joined", "write_content",
         ["text", "plan", r"(campaign|video|ads)" + ROW + r"{0,200}[ $,]3,?000\b"], "core", None, ["FILT"], fact="campaign_row"),
    slot("C2", "DD production hosting at $140", 5, MS, "#winddown, issue note, draft and Confluence vs Arthur's DM reply", "write_content",
         ["text", "plan", r"(domino|DD)" + ROW + r"{0,160}[ $,]140\b"], "core", None, ["CORR"], fact="dd_hosting"),
    slot("C3", "DD player support release step before Feb 28", 5, MS, "Arthur's done claim and the merged PR vs the App Store Connect notice, dated by the card's rule", "write_content",
         ["text", "plan", r"(support|helpshift)" + ROW + r"{0,220}(release|build|ship|submi|approv)" + ROW + r"{0,120}feb[a-z]*\.? ?(2[0-8]|1[5-9])\b"], "core", None, ["DONE", "CORR", "AUTH"], fact="support_step"),
    slot("C4", "layer.ai art export dated before Mar 3", 5, MS, "the closed-looking issue note vs Leonard's #prototype post (access until March 3rd) and his reply under it (CF's art only lives there), dated by the card's rule", "write_content",
         ["text", "plan", r"(?:^|\n)(?=" + ROW + r"*layer)(?=" + ROW + r"*(export|download|sav(e|ing)|pull|back ?up|get))" + ROW + r"*?(mar[a-z]*\.? ?[123]\b|feb[a-z]*\.? ?2[0-9]\b|before" + ROW + r"{0,20}mar)"], "core", None, ["DATE"], fact="layer_step"),
    slot("C5", "GitHub repos transfer after the data is delivered", 3, IN, "Arthur's Feb 11 'transfer now' superseded by the Feb 12 checklist", "write_content",
         ["text", "plan", r"github" + ROW + r"{0,220}(after|once|when|until)" + ROW + r"{0,80}(data|sold|sale|deliver)"], "core", None, ["DATE"], fact="github_step"),
    slot("P1", "CF backend stacks at $62", 5, MS, "Arthur's ~$95 note on ENG-2445 vs his later Jenkins email (the extra backend copy shut down, $62 now), under the costing rule", "write_content",
         ["text", "plan", r"(backend|auth)" + ROW + r"{0,160}[ $,]62\b"], "core", None, ["STACKS"], fact="cf_stacks"),
    slot("P3", "AppsFlyer at $0", 1, LK, "#winddown Feb 12: free up to 15K installs", "write_content", ["text", "plan", r"appsflyer" + ROW + r"{0,120}([ $,]0\b|free)"], "sample", "costs"),
    slot("R2", "Arthur's monthly cash in the reply", 5, MS, "a third of $3,450 less the $248 he already carries (split email + billing email)", "write_content",
         ["text", "reply", r"([Aa]rthur|[Bb]lake).{0,120}[ $]902\b|[ $]902\b.{0,120}([Aa]rthur|[Bb]lake)"], "core", None, ["COMPLETE", "CORR", "FILT", "STACKS"], fact="arthur_share"),
    slot("R3", "Leonard's and Robert's monthly cash in the reply", 3, CA, "a third of the LLC's monthly cost under the split email", "write_content",
         ["text", "reply", r"\b1,?150\b"], "core", None, ["CORR", "FILT", "COMPLETE", "STACKS"], fact="even_share"),
    slot("R4", "recommendation takes DD", 3, IN, "the take test's outcome stated", "write_content",
         ["text", "reply", r"([Dd]omino|DD).{0,160}([Tt]ake|[Kk]eep|[Bb]ring|[Cc]omes? over|[Ww]orth)"], "core", None, ["CORR", "AUTH"], fact="dd_decision_reply"),
    slot("R6", "reply names the unreleased support build", 3, IN, "the store notice's open step", "write_content",
         ["text", "reply", r"([Ss]upport|[Hh]elpshift).{0,220}([Ff]eb[a-z]*\.? ?28|[Rr]elease|[Bb]uild|not approved|[Rr]ejected)"], "core", None, ["DONE", "CORR", "AUTH"], fact="support_reply"),
    slot("R7", "reply leaves Zombie Match with HG", 3, CO, "January income $0.00 under the take test", "write_content",
         ["text", "reply", r"([Zz]ombie|ZM).{0,160}([Ss]unset|HG|[Hh]armony|[Ss]tay|[Ll]eave|not)"], "core", None, ["AUTH"], fact="zm_reply"),
    slot("L1", "new issue for the campaign", 5, MS, "the campaign is outside the project; the ground rules bring it in", "write_content",
         ["text", "new_issue", r"([Cc]ampaign|[Vv]ideo|[Aa]ds|[Mm]eta)"], "core", None, ["FILT"], fact="campaign_issue"),
    slot("D1", "plan sheet in Robert's Drive root", 1, LK, "the hub: keep it in your drive", "delivery", ["delivery", "register_parent", BASE["robert_root"]]),
    slot("D2", "reply links the plan sheet", 1, LK, "the hub: share it and tell me here", "delivery", ["link", "reply"]),
    slot("D3", "reply in Leonard's DM thread", 1, LK, "the hub: tell me here", "delivery", ["delivery", "slack_thread", hub_ts]),
]
surface = {
    "kind": "GRADABLE_SURFACE", "version": 1, "task": "robert_llc_takeover", "revision": "design-2 (rev4)",
    "truth_keys": [m["key"] for m in C], "classes": ["LLC", "Founder", "HG"],
    "truth_fields": {"class": "Decision", "groups": "groups"},
    "deliverables": {
        "plan": {"kind": "table", "name_regex": r"(?i).*(llc|plan|take|combo|90).*", "key_column": "Item",
                 "key_regex": r"(?:Item 1|[A-Za-z][A-Za-z0-9 .()&/-]*)",
                 "columns": Q["draft_header"], "class_column": "Decision", "reason_column": "Next step", "comparators": {"Decision": "yes_no"},
                 # rev4: the Decision labels the project and the draft use are accepted spellings of the three classes (pre-check event 316)
                 "yes_no": {"LLC": ["LLC", "LLC takes it", "Take", "Takes", "Take it", "LLC pays"],
                            "Founder": ["Founder", "One of us", "Carried", "Already carried", "Arthur", "Blake", "Arthur carries it", "Blake carries it"],
                            "HG": ["HG", "Harmony Games", "Stays with HG", "Stays HG", "Not used", "Not taken", "Leave with HG", "Sunset"]}},
        "reply": {"kind": "json_text", "tool": "slack_send_message"},
        "new_issue": {"kind": "json_text", "tool": "linear_create_issue"},
        "comments": {"kind": "json_text", "tool": "linear_create_comment"},
    },
    "slots": slots,
}
write(os.path.join(WF, "01_Gradable_Surface.json"), surface)
# each portfolio rule's "decides" is the surface's own mechanism map, so the two never drift
_by = {}
for _s in slots:
    for _m in _s["mechanisms"]:
        _by.setdefault(_m, []).append(_s["id"])
for _e in portfolio:
    _e["decides"] = _by.get(_e["id"], [])
write(os.path.join(WF, "01_Hardness_Manifest.draft.json"), manifest)

# ---------------------------------------------------------------- ids, wording and tables for the design doc
write(os.path.join(HERE, "ids.json"), {"IDS": IDS, "BASE": BASE, "T": T, "issues": {m["key"]: m["linear"] for m in ISSUES}})
write(os.path.join(HERE, "wording.json"), Q)
write(os.path.join(HERE, "cohort.json"), C)


def md_table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


cohort_rows = []
for m in C:
    cohort_rows.append([m.get("linear", "new issue"), m["key"], m["game"], m["decision"], ("$%d" % m["cost"]) if m["cost"] else "$0",
                        m["paid_by"], m["step"], m["owner"], m["by"], m["deciding"], m["role"] + (" (" + ", ".join(m["channel"]) + ")" if m["channel"] else "")])
open(os.path.join(HERE, "tables", "cohort.md"), "w").write(md_table(
    ["Issue", "Item", "Game", "Decision", "Monthly cost", "Paid by", "Next step", "Owner", "By", "Deciding record", "Role"], cohort_rows))
open(os.path.join(HERE, "tables", "budget.md"), "w").write(md_table(
    ["Line", "March", "April", "May", "Source"],
    [["LLC cash need (DD hosting 140 + CF stacks 62 + campaign 3,000)", "3,202", "3,202", "3,202", "Arthur's DM; CF stacks issue; Leonard's status"],
     ["Carried personally (Arthur: Metabase 100 + dbt 100 + GitHub 48)", "248", "248", "248", "Arthur's Feb 13 email"],
     ["LLC monthly cost", "3,450", "3,450", "3,450", "sum"],
     ["Leonard (cash)", "1,150", "1,150", "1,150", "a third (split email)"],
     ["Robert (cash)", "1,150", "1,150", "1,150", "a third"],
     ["Arthur (cash)", "902", "902", "902", "a third less the 248 he carries"]]))
print(json.dumps({"cohort": len(C), "issues": len(ISSUES), "counts": COUNTS, "cash": CASH, "carried": CARRIED, "third": THIRD,
                  "shares": SHARES, "budget_total": TOTAL_BUDGET, "per_record_surfaces": PER_RECORD_SURF,
                  "slots": len(slots), "weight": sum(s["weight"] for s in slots)}, indent=1))
