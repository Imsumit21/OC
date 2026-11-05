#!/usr/bin/env python3
"""Draft task_inputs/08_Oracle_Events.md (draft mode) from the OE ledger's facts.

Every quoted Expected value is re-read in this run: seeded rows are parsed from 01_Universe_Inject.sql (never
executed) and base records are read through tools/hg.py. Each quote is asserted as a substring of its own record
(whitespace-normalised) before the file is written. One write per event; no final-response or non-action events."""
import datetime as dt
import json
import os
import re
import subprocess
import sys
from email.utils import parsedate_to_datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
FRED = "frederick.stone@harmonygames.co"
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
CHECKS = []  # (event key, quote) for the self-review count


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")


def norm(s):
    return re.sub(r"\s+", " ", clean(s)).strip()


def hg_get(svc, f):
    out, off = "", 0
    while True:
        a = ["python3", "-B", "Task_Authoring/tools/hg.py", "search", "get", svc, "--file", f, "--pointer", ""]
        if off:
            a += ["--offset", str(off)]
        p = subprocess.run(a, cwd=WS, capture_output=True, text=True,
                           env={**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"})
        d = json.loads(p.stdout)
        out += d["text"]
        if not d["truncated"]:
            return json.loads(out)
        off = d["next_offset"]


def pt(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")) if re.match(r"\d{4}-", iso) else parsedate_to_datetime(iso)
    p = d.astimezone(PT)
    s = p.strftime("%a %b %-d %Y %-I:%M %p") + " PT"
    u = d.astimezone(dt.timezone.utc)
    if u.date() != p.date():
        s += f" ({u.strftime('%b %-d %H:%M')} UTC)"
    return s


def day(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")) if re.match(r"\d{4}-", iso) else parsedate_to_datetime(iso)
    return d.astimezone(PT).strftime("%a %b %-d")


class Src:
    """A record's text; q() returns a quoted span after asserting it is in this record."""

    def __init__(self, label, text):
        self.label, self.text = label, norm(text)

    def q(self, s):
        assert norm(s) in self.text, f"quote not in {self.label}: {s!r}"
        CHECKS.append((self.label, s))
        return f'"{s}"'


def msgs(tid):
    return sorted(rows("gmail.gmail_messages", thread_id=tid, user_email=FRED), key=lambda r: int(r["internal_date"]))


def paper(pid):
    d = rows("gdocs.docs_documents", document_id=pid)
    if d:
        return d[0]["title"], Src(pid, d[0]["body_text"])
    els = [e for e in rows("gslides.slides_page_elements", presentation_id=pid) if e.get("text")]
    pres = rows("gslides.slides_presentations", presentation_id=pid)
    return pres[0]["title"], Src(pid, "\n".join(clean(e["text"]) for e in els))


# ------------------------------------------------------------------ rule records
hub = rows("gmail.gmail_messages", id=IDS["msg"]["hub"])[0]
HUB = Src("hub", hub["body_text"])
gr = rows("gdocs.docs_documents", document_id="f_b98287f6f80fe431a71209")[0]
GR = Src("guardrails", gr["body_text"])
amend = [r for r in rows("slack.slack_messages", channel_id="C07C2866011") if "one change to the runway guardrails" in r["text"]][0]
AM = Src("amend", amend["text"])
esg = rows("gmail.gmail_messages", id=IDS["msg"]["esg_note"])[0]
ESG = Src("esg_note", esg["body_text"])
ack = rows("gmail.gmail_messages", id=IDS["msg"]["esg_ack"])[0]
ACK = Src("esg_ack", ack["body_text"])
ck = rows("gdocs.docs_documents", document_id="f_3b06917a41dd59308d890b")[0]
CK = Src("checklist", ck["body_text"])
esgc = rows("contacts.contacts", contact_id="9b0185e445572aeee9f27d35")[0]
fold = rows("gdrive.drive_files", id="d_80a8c04753ba82ba4ba6a5")[0]
rd = rows("gdocs.docs_documents", document_id="f_846ddc38b2aab3d2ed3fcb")[0]
RD = Src("readme", rd["body_text"])
tpl = rows("gsheets.sheets_spreadsheets", spreadsheet_id="f_05f0a451b29b19a1c0b90f")[0]
tsh = rows("gsheets.sheets_sheets", spreadsheet_id="f_05f0a451b29b19a1c0b90f")[0]
HDR = json.loads(clean(tsh.get("grid_json") or tsh.get("values_json") or "[]"))[0]
assert HDR == ["Company", "Contact", "What's waiting", "Decision", "Answered by", "What we told them", "Next date"], HDR
card = rows("trello.trello_cards")[0]
CARD = Src("keepcard", card["name"] + "\n" + card["desc"] + "\n" + "\n".join(r["name"] for r in rows("trello.trello_check_items")))
rev = rows("gcal.gcal_events", event_id="evt_fd469c29811879519c2c96")[0]
REV = Src("review", rev["summary"] + "\n" + rev["description"])
pw = rows("gdrive.drive_files", id=IDS["paperwork_folder"])[0]
papers = [r for r in rows("gdrive.drive_files") if r.get("parents_json") and IDS["paperwork_folder"] in r["parents_json"]]
assert len(papers) == 33, len(papers)
zom = rows("linear.linear_issues", id="ZOM-567")[0]
zc = rows("linear.linear_comments", id="cmt_c9a6660d81e067ad1de7")[0]
ZC = Src("zom_comment", zc["body"])
SLK = {r["id"]: r for r in rows("slack.slack_messages")}
WAIV = Src("waiver", [r for r in SLK.values() if r["text"].startswith("side note, Maren")][0]["text"])
waiv = [r for r in SLK.values() if r["text"].startswith("side note, Maren")][0]
dmr = [r for r in SLK.values() if r["text"].startswith("on localization")][0]
DM = Src("lf_dm", dmr["text"])
spn = [r for r in SLK.values() if "indie showcase" in r["text"]][0]
SPN = Src("sp_note", spn["text"])
nt = rows("gmail.gmail_messages", id=IDS["msg"]["clipforge_notice"])[0]
NT = Src("notice", nt["body_text"])
NTS = Src("notice_subject", nt["subject"])
nova = msgs(IDS["threads"]["Nova Rewards"])[-1]
NOVA = Src("nova", nova["body_text"])

# base records, re-read through hg.py in this run
nin_req = hg_get("gmail", "threads/frederick@harmonygames.co_1842358947604469113.json")["messages"][0]
nin_done = hg_get("gmail", "threads/frederick@harmonygames.co_1842359398719557772.json")["messages"][0]
NR, ND = Src("nin_req", nin_req["subject"]), Src("nin_done", nin_done["subject"] + "\n" + nin_done["body"])
bal = hg_get("gmail", "threads/frederick@harmonygames.co_1840501641217286806.json")["messages"]
bal_lv = [m for m in bal if m["date"].startswith("Thu, 11 Sep 2025 17:21")][0]
bal_ask = [m for m in bal if m["date"].startswith("Thu, 11 Sep 2025 14:54")][0]
bal_last = bal[0]
BLV, BASK, BLAST = Src("bal_lv", bal_lv["body"]), Src("bal_ask", bal_ask["body"]), Src("bal_last", bal_last["body"])
assert bal_last["date"].startswith("Mon, 15 Sep 2025") and "PERSON_0527_EMAIL" in bal_last["from"]
BND = {}
for key, tid in [("rayking", "1842348778705877030"), ("playable", "1843000993076735547"), ("gamesforum", "1842890197572292911"),
                 ("interco", "1841620870486605150"), ("google", "1817715521687421486"), ("singular", "1837914783244638008"),
                 ("ncsoft", "1842898562278009736"), ("dentsu", "1843473831194478743")]:
    BND[key] = hg_get("gmail", f"threads/frederick@harmonygames.co_{tid}.json")["messages"]
for key in ("playable", "gamesforum", "interco"):  # nobody on our side wrote in these threads
    assert all("harmonygames.co" not in m["from"] for m in BND[key]), key
assert all("leonard.hayes" in m["to"] for m in BND["rayking"] if "frederick" in m["from"]), "rayking reply went to Leonard only"
assert len(BND["playable"]) == 2 and len(BND["gamesforum"]) == 1 and len(BND["interco"]) == 3
RAY = Src("rayking", "\n".join(m["body"] for m in BND["rayking"]))
ncs = [m for m in hg_get("gmail", "threads/frederick@harmonygames.co_1832208184829815962.json")["messages"] if m["date"].startswith("Thu, 25 Sep 2025 07:54")][0]
den = [m for m in BND["dentsu"] if m["date"].startswith("Tue, 23 Sep 2025 18:52")][0]
NCS, DEN = Src("ncsoft", ncs["body"]), Src("dentsu", den["body"])
ray_draft = [m for m in BND["rayking"] if "frederick" in m["from"]][0]
RAYL = Src("rayking_labels", [h["value"] for h in ray_draft["headers"] if h["name"] == "X-Gmail-Labels"][0])
APO = hg_get("gmail", "threads/frederick@harmonygames.co_1830012626042968381.json")["messages"]
apo_fred = sorted((m for m in APO if "frederick" in m["from"]), key=lambda m: parsedate_to_datetime(m["date"]))
apo_last = max(APO, key=lambda m: parsedate_to_datetime(m["date"]))
assert "frederick" not in apo_last["from"] and len(apo_fred) == 2
APL = Src("appodeal_last", apo_last["body"])
APT = Src("appodeal_terms", "\n".join(m["body"] for m in APO if "frederick" not in m["from"]))
ACMP = hg_get("gmail", "threads/frederick@harmonygames.co_1833464394449700499.json")["messages"]
acmp_fred = [m for m in ACMP if "frederick" in m["from"]][0]
ACF, ACI = Src("appcamp_fred", acmp_fred["body"]), Src("appcamp_invite", "\n".join(m["body"] for m in ACMP if "frederick" not in m["from"]))
SING = Src("singular", BND["singular"][0]["subject"])
ptr = hg_get("slack", "messages/C07C2866011/2025-09.json")[866]
dmroot = hg_get("slack", "messages/D05S58U4SAK/2025-09.json")[100]
PTR, DMR = Src("pt_root", ptr["text"]), Src("dm_root", dmroot["text"])
assert ptr["ts"] == "1758513190.847889" and dmroot["ts"] == "1758151772.570449", (ptr["ts"], dmroot["ts"])
bal_call = [m for m in bal if m["date"].startswith("Sun, 17 Aug 2025 12:16")][0]
BCALL = Src("bal_call", bal_call["body"])

# ------------------------------------------------------------------ the 36 companies
# per company: the asks quoted from its latest inbound message (or named message), the paper lines, and the analysis
CO = {
    "Lanternfly Publishing": (["Any news on the proposal? We're planning our Q4 slate and would love to include Domino Delights."],
                              ["Revenue share 70/30 after store fees", "No upfront fee", "2-year term, exclusive for Southeast Asia"],
                              "The next event shows Leonard already answered."),
    "Motive Forge": (None, ["Price: $6,400, 50% on kickoff"], None),
    "Spotlight Fest": (["We'd love Zombie Match 3D in the Spotlight Fest indie showcase on Dec 5. The stand fee is $750. Could we set up a quick call?"],
                       ["Indie showcase, Dec 5, 2025", "Stand fee: $750"],
                       "The next event shows Robert already answered."),
    "Clipforge": (["If you're not carrying on after the pilot, let me know here too so I can plan the team's time."],
                  ["Workspace: HG-2291", "Pilot: no charge through Jan 15, 2026, up to 20 delivered videos",
                   "If the 20-video cap is reached early, the pilot ends at the end of that cycle and the Studio plan starts the next day",
                   "Cancel in writing to the billing address on your notice before the Studio plan starts"],
                  "The billing notice for this workspace is read next."),
    "Pixel Harbor Events": (["Quote attached: $4,800, with a $2,400 deposit due by Oct 10 to keep the hold."],
                            ["Price: $4,800; deposit $2,400 due by Oct 10, 2025 to hold the booth; balance by Oct 20", "Cancellation: free before the deposit is paid"],
                            "The deposit and the booth are cash inside Oct 1 to Dec 31 (guardrails step 2): End, say no. Next date Oct 10, 2025."),
    "Brightlane Studio": (["Can you confirm by Oct 1 so I can book the team for October?"],
                          ["Fee: $3,500/month, invoiced on the 1st", "Start: Oct 1, 2025; 3-month minimum"],
                          "Monthly fees from Oct 1 fail the cash test: End, say no. Next date Oct 1, 2025."),
    "Soundvault": (["just a reminder the trailer pack quote runs out on Oct 15. Want me to send the licence for signature?"],
                   ["Price: $1,188, paid in full on signature", "Quote valid until Oct 15, 2025"],
                   "Taking it means paying before January (step 2): End, say no. Next date Oct 15, 2025."),
    "Reviewly": (["how's the trial going?"],
                 ["After the trial the account moves to Growth at $79/month on Oct 20, 2025 unless cancelled by Oct 19, 2025",
                  "Cancel: in the app or by email to your onboarding contact"],
                 "A trial that turns paid inside the window counts as cash: End, cancel in writing to Hana. Next date Oct 19, 2025."),
    "Streamcast Talent": (["want me to pencil in the November slot?"],
                          ["Budget: $8,000; 50% deposit ($4,000) on booking, balance on delivery", "Book by Oct 31, 2025"],
                          "A November campaign paid on booking fails the cash test: End, say no. Next date Oct 31, 2025."),
    "Lingora": (["any update? Send the PO and we can start Monday."],
                ["Price: $2,640, invoiced on delivery", "Delivery: two weeks from the PO", "Quote valid until Oct 3, 2025"],
                "Taking it means paying before January: End, say no. Next date Oct 3, 2025."),
    "Panelpulse": (["still keen on the Oct 14 panel? Recruiting closes Oct 6."],
                   ["Price: $1,200, prepaid on confirmation", "Confirm by Oct 6, 2025"],
                   "Prepaid for an Oct 14 panel: End, say no. Next date Oct 6, 2025."),
    "Ascendo": (["can you confirm by Oct 1 so we can kick off?"],
                ["Fee: $900/month from Oct 1, 2025, month to month after a 3-month start"],
                "Monthly fees from Oct 1: End, say no. Next date Oct 1, 2025."),
    "Wishwave": (["can you confirm by Oct 17 so I can book travel while fares are low?"],
                 ["Event: Seattle Indie Expo, Nov 7, 2025",
                  "Harmony Games covers: travel and hotel for two, booked by Wishwave and invoiced at cost (about $1,600)", "Confirm by Oct 17, 2025"],
                 "Travel a partner books and bills us counts as cash after Monday's change (@@amend@@): End, say no. Next date Oct 17, 2025."),
    "Vaultline": (["your nightly database backups move to Standard ($19/month) when the plan renews on Oct 12. Can you confirm you want to keep them running?"],
                  ["Price: $19/month, renews Oct 12, 2025", "The existing terms carry over; nothing new to sign"],
                  "It costs money but is on Arthur's keep-running list (\"Vaultline nightly DB backups\", @@keepcard@@): Keep, tell them we're staying. Next date Oct 12, 2025."),
    "Certwell": (["The renewal is $89 for the year. Reply to confirm and we'll reissue it; otherwise it lapses on the 20th."],
                 ["Renewal: $89/year, due Oct 20, 2025", "Same terms as the current certificate; nothing new to sign"],
                 "On the keep-running list (\"Certwell SSL cert for the API domain\", @@keepcard@@): Keep, confirm the renewal. Next date Oct 20, 2025."),
    "Pingwise": (["From Nov 1 the account moves to Team ($29/month) under your existing agreement, so phone and SMS paging keep working for your on-call rota.",
                  "Free has email alerts only, no paging."],
                 ["Service: uptime monitoring and on-call alerting for your API and backend endpoints (1-minute checks, phone and SMS paging)",
                  "Price: $29/month from Nov 1, 2025, billed monthly"],
                 "Pingwise is the paging service, so it is the list's \"the night pager for backend outages (whatever wakes me up at 3am)\" (@@keepcard@@): Keep, tell Dana we're staying on Team. Next date Nov 1, 2025."),
    "Kinetic Arcade": (["any thoughts on the LOI? Oct 20 is our internal deadline."],
                       ["Territories: Japan and Korea", "Model: revenue share, no fees to Harmony Games",
                        "Exclusivity: 12 months from signature for those territories", "Signature needed by Oct 20, 2025"],
                       "No cost, but it needs a signature and carries exclusivity, so ESG sees it first (@@esg@@): Sign, an ESG intake email, a card. Next date Oct 20, 2025."),
    "Lumencloud": (["just checking you saw this one, the cohort closes Oct 31."],
                   ["Credits: $25,000, usable over 36 months", "Term: 36 months from signature", "No charges while credits last", "Sign by Oct 31, 2025 (cohort closes)"],
                   "No cost, but a 36-month term is over 12 months, so ESG sees it first (@@esg@@): Sign, an ESG intake email, a card. Next date Oct 31, 2025."),
    "Bundlehouse": (["The participation agreement needs signing by Nov 1."],
                    ["No cost to join", "Revenue share on bundle sales",
                     "Bundlehouse may use your game's name, logo and art in bundle marketing for 18 months",
                     "Sign the participation agreement (it carries the licence) by Nov 1, 2025"],
                    "No cost, but it licenses our IP, so ESG sees it first (@@esg@@): Sign, an ESG intake email, a card. Next date Nov 1, 2025."),
    "Orbit Store": (["gentle nudge on the featuring agreement, Oct 24 is the cut-off."],
                    ["Fees: none", "Term: the promotion only", "Acceptance: by an authorised signatory in the Orbit partner portal by Oct 24, 2025"],
                    "No cost and no ESG trigger, but an officer must accept: Sign, a card; Mateo writes to us himself, so he gets an answer. Next date Oct 24, 2025."),
    "Markward": (["the free tier is ready whenever you accept the terms in the dashboard. Shall I keep the setup on hold for you?"],
                 ["Price: free, no payment details", "Term: none, switch it off any time", "Activation: accept the terms in the Markward dashboard"],
                 "Click-through terms still need an officer (@@esg@@): Sign, a card, no ESG trigger. The paper and Leah's two mails give no date, so Next date is blank."),
    "Playfuse": (["Could someone on your side sign a mutual NDA? Happy to use your lawyers' template."],
                 ["Term: 2 years", "Signature: an officer of each party, by Oct 8, 2025 (before our call that day)"],
                 "A mutual NDA on our lawyers' template needs no ESG review whatever its term (@@esg@@): Sign, a card. Next date Oct 8, 2025."),
    "Framewell": (["Can you let me know by mid-October if we should set it up?"],
                  ["Price: $149/month, billed monthly", "Billing starts: Nov 1, 2025"],
                  "On the order form alone, billing from Nov 1 would fail the cash test; the next event changes that."),
    "Hootline": (None, None, None),
    "Glyphworks": (["any decision on the fonts?"], ["Price: $640, payable when ordered", "Quote valid until Jan 31, 2026"],
                   "Nothing is owed unless we order, and the quote can still be taken up after January: Park."),
    "Cloudlark": (["Would you like to activate now or later?"], ["Held until Feb 28, 2026", "Activation: when you're ready; nothing owed"],
                  "Free, and can be taken up after January: Park."),
    "Echohall": (["The free plan carries on as it is until then."], ["Pro: $49/month from the day you upgrade", "Free plan: continues as it is until you choose to upgrade"],
                 "Nothing is owed unless we upgrade: Park."),
    "Pressbeam": (["$1,200 when you book. No travel, all remote, and you can book any time before launch."], ["Price: $1,200, paid when booked", "No travel; book any time before launch"],
                  "Nothing is owed unless we book, and it can be booked after January: Park."),
    "Retainly": (["It runs free until Jan 12, then Growth is $99/month. Could you let me know whether you plan to stay on after the trial?"],
                 ["After the trial: Growth at $99/month unless cancelled before Jan 12, 2026"],
                 "Free until January (the Jan 5 review comes first): Park."),
    "Quillcraft": (["would you join a 30-minute feedback call next week?"], ["Beta: free through January 31, 2026", "Paid plans from February 2026"],
                   "Free until January: Park."),
    "Tilecast": (["We can offer a free pilot slot in February for the interactive demo widget on your website. Want me to hold it?"],
                 ["Free pilot slot: February 2026", "No cost during the pilot"], "Free, and it starts after January: Park."),
    "Benchmarkly": (["The full set is a $300/month subscription from February if you want it."],
                    ["Sample report: free", "Full benchmark set: $300/month, starting February 2026 if you subscribe"],
                    "Free until January, and the subscription would start after it: Park."),
    "Loopnote": (["want me to add the rest of your team to the trial?"], ["Team trial: free until Feb 1, 2026", "After the trial: $8 per user per month if you continue"],
                 "Free until January: Park."),
    "Driftwood Audio": (["$950 for the trailer VO, paid when you book a session. The quote is good until Feb 28."],
                        ["Price: $950, paid when you book a session", "Quote valid until Feb 28, 2026"],
                        "Nothing is owed unless we book, and the quote can be taken up after January: Park."),
}
ORDER = {"Answered": ["Lanternfly Publishing", "Balancy", "Motive Forge", "Spotlight Fest"],
         "End": ["Clipforge", "Pixel Harbor Events", "Brightlane Studio", "Soundvault", "Reviewly", "Streamcast Talent", "Lingora", "Panelpulse", "Ascendo", "Wishwave"],
         "Keep": ["Vaultline", "Certwell", "Pingwise"],
         "Sign": ["Nintendo", "Kinetic Arcade", "Lumencloud", "Bundlehouse", "Orbit Store", "Markward", "Playfuse"],
         "Park": ["Framewell", "Hootline", "Glyphworks", "Cloudlark", "Echohall", "Pressbeam", "Retainly", "Quillcraft", "Tilecast", "Benchmarkly", "Loopnote", "Driftwood Audio"]}
for d, ks in ORDER.items():
    assert sorted(ks) == sorted(k for k, v in TRUTH.items() if v["Decision"] == d), d
PARK_NOTE = "Next date Jan 5, 2026 (the review, @@review@@)."
HOLD = {"Pixel Harbor Events": "I'll come back to you on this", "Lanternfly Publishing": "we'll take a look and get back to you"}

EV = []


def ev(key, head, exp):
    EV.append((key, head, exp))


# person per company: name and address as the thread shows them
PERSON = {}
for k, v in TRUTH.items():
    if not v["Decision"] or k in ("Nintendo", "Balancy"):
        continue
    ms = msgs(IDS["threads"][k])
    them = [m for m in ms if not m["from_email"].endswith("@harmonygames.co")]
    assert them and them[-1]["from_name"] == v["Contact"], (k, v["Contact"])
    PERSON[k] = (them[-1]["from_name"], them[-1]["from_email"])
PERSON["Balancy"] = ("PERSON_0527_NAME", "PERSON_0527_EMAIL")

# ------------------------------------------------------------------ discovery: rules and destinations
ev("hub", "Find Leonard's email from yesterday in Frederick's Gmail and read it (search \"vendor and partner\", from Leonard Hayes)",
   f"One message, subject \"{hub['subject']}\", sent {pt(hub['date'])} by Leonard Hayes to Frederick only. "
   + HUB.q("can you take over the vendor and partner backlog this week?") + " In scope: "
   + HUB.q("anyone outside the investor work who has an offer, a trial, a quote, terms or an ask in front of us and that one of us has actually engaged with: a call, a reply, a sign-up or paper") + ". "
   + HUB.q("Cold pitches nobody answered, including ones we only forwarded around internally, stay off it") + ", "
   + HUB.q("and so do the ad networks, PlayableX, Craftsman+ and Singular (they all stay on the UA budget call), the investors, and Mattel, which I'm keeping") + ". "
   + HUB.q("Go by the runway guardrails doc for what we do with each one, plus the one change I posted in #executives on Monday") + "; "
   + HUB.q("Anything that needs signing goes the way ESG's note about signing says") + "; "
   + HUB.q("Everyone who is waiting to hear from us should get a written answer this week") + "; "
   + HUB.q("Get each company's contact into Contacts so we're not digging through mail next time") + "; "
   + HUB.q("Log it all in a sheet in the Q4 commitments folder, the README in the folder has the columns") + "; "
   + HUB.q("Then reply here with what we're keeping and what's waiting on Arthur or me to sign") + ".")
ev("guardrails", f"Read the runway guardrails doc in Drive/Docs (search \"runway guardrails\"; doc \"{gr['title']}\")",
   f"Doc by Leonard, created {pt(gr['created_time'])}. " + GR.q("Go top to bottom and stop at the first one that fits.") + " "
   + GR.q("1. Already answered. If one of us has already given them an answer, don't write to them again. Note who answered and when.") + " "
   + GR.q("If the answer was \"later\", it comes back at the January commitments review") + ". "
   + GR.q("2. Cash test. Anything that would cost us cash between Oct 1 and Dec 31 ends now: say no, or cancel it in writing the way their paper or notice asks.") + " "
   + GR.q("A trial or pilot that turns into a paid plan inside that window counts as cash, and so does an offer we would have to take up and pay for before January. Travel and event costs count only when we book them ourselves.") + " "
   + GR.q("3. Keep. The cash test has one exception: anything on Arthur's keep-running list on our board stays, even if it costs money. Tell them we're staying.") + " "
   + GR.q("4. Sign. If it costs nothing before January but taking it means someone has to accept terms or sign for the company, it goes the way ESG's note says.") + " "
   + GR.q("Tell them it's with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it.") + " "
   + GR.q("5. Park. Everything else that's free until January, including offers we could still take up after that. Tell them we'll pick it up in January") + ". "
   + GR.q("Everyone who is waiting to hear from us gets a written answer. Portals and no-reply notices don't need one."))
ev("amend", "Find Leonard's Monday change in Slack #executives (search \"runway guardrails\")",
   f"Leonard, {pt(amend['created_at'][:19] + 'Z')}: " + AM.q(clean(amend["text"])) + ". It replaces the doc's rule that travel counts only when we book it.")
ev("esg", f"Read ESG's note about signing and Leonard's reply in Frederick's Gmail (search \"Signing and review\"; thread \"{esg['subject']}\")",
   f"ESG Law's note to Leonard, cc Frederick, Robert and Arthur, {pt(esg['date'])}: " + ESG.q("Only an officer, you or Arthur, accepts terms or signs for Harmony Games, whatever the amount. That includes click-through terms and portal NDAs.") + " "
   + ESG.q("Anything with an automatic renewal, exclusivity, a licence of your IP or a term over 12 months comes to us before anyone signs.") + " "
   + ESG.q("Mutual NDAs on our template don't need review, whatever their term. An officer can sign them.") + " Intake is " + ESG.q("one email per agreement") + ". "
   + f"Leonard's reply, {pt(ack['date'])}: " + ACK.q("This replaces what I said in July about Fred signing small stuff himself.") + " "
   + ACK.q("anything waiting on Arthur or me to sign, put it on our founders' board To Do list with the company's name in the card title, including the ones that go to ESG") + "; "
   + ACK.q("For the intake emails, what to include is in the intake checklist I shared."))
ev("checklist", f"Read the ESG intake checklist in Drive/Docs (search \"intake checklist\"; doc \"{ck['title']}\")",
   CK.q("One email per agreement to ESG Law intake.") + " Include: " + "; ".join(CK.q(x) for x in (
       "the company and what the agreement is", "the term and any automatic renewal", "any exclusivity or licence of our IP",
       "what it costs us, if anything", "the date they need it by", "who would sign it (Leonard or Arthur)")) + ".")
ev("esg_contact", "Look up ESG Law intake in Contacts (search \"ESG Law\")",
   f"Contact \"{esgc['first_name']} {esgc['last_name']}\", email {esgc['email']}, job \"{esgc['job']}\".")
ev("folder", "Find Frederick's Q4 commitments folder in Drive and list it (search \"Q4 commitments\")",
   f"Folder \"{fold['name']}\", owner Frederick, shared with Leonard, created {pt(fold['created_time'])}. It holds the doc \"{rd['title']}\" and the sheet \"{tpl['title']}\".")
ev("readme", f"Read the README in the folder in Docs (doc \"{rd['title']}\" from @@folder@@)",
   RD.q("Name it \"Q4 commitments log\"; to start, copy the header row from the template sheet.") + " Columns: "
   + RD.q("Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date") + ". "
   + RD.q("Decision is one of: Answered, End, Keep, Sign, Park (the guardrails doc says which).") + " "
   + RD.q("Answered by: who on our side already answered them, for Answered rows.") + " "
   + RD.q("Next date: for End, the last day to cancel or say no; for Park and for \"later\" answers, the January review; for Keep, when it next bills; for Sign, the date they need it by, if any.") + " Contacts: "
   + RD.q("Put the company in the job field, and only add a person who isn't in Contacts already (portals and no-reply senders don't get one)."))
ev("template", f"Read the header row of the template sheet in Sheets (sheet \"{tpl['title']}\" from @@folder@@, tab \"{tsh['title']}\")",
   "Row 1: " + ", ".join(f'"{h}"' for h in HDR) + ".")
ev("board", "Find the Harmony Games board in Trello and list its lists",
   "Board \"Harmony Games\" (the board the prompt names, which Leonard calls our founders' board in OE 4). Open lists: \"To Do\", \"Doing\", \"Done\", \"Backlog\".")
ev("keepcard", f"Read Arthur's keep-running card on the board in Trello (card \"{card['name']}\")",
   CARD.q(card["desc"]) + " Checklist: " + "; ".join(CARD.q(r["name"]) for r in sorted(rows("trello.trello_check_items"), key=lambda r: float(r.get("pos") or 0))) + ".")
ev("review", "Find the January commitments review on Frederick's calendar in Google Calendar (search \"Q4 commitments review\")",
   f"Event \"{rev['summary']}\", organizer Leonard, starts {pt(rev['start_ts'])} (a future date), created {pt(rev['created'])}; description " + REV.q(rev["description"]) + " This is the January review date.")
PNAMES = sorted(re.sub(r" - .*$", "", r["name"]) for r in papers)
ev("papers", f"List Frederick's paperwork folder in Drive (search \"paperwork\"; folder \"{pw['name']}\")",
   f"33 files, each named for its company: " + ", ".join(PNAMES) + ".")
assert PNAMES == sorted(k for k in IDS["papers"]), PNAMES
ev("sweep", "Find every other outside company in Frederick's Gmail with an offer, a trial, a quote, terms or an ask that one of us engaged with (scope from @@hub@@): search the whole inbox up to Sep 30 2025 and read the threads that look like one",
   "Each company in @@papers@@ has its own thread with that company. Three more are in scope with nothing in the paperwork folder: Hootline (thread \"Your Hootline promo\", Aug 5 and Aug 12; "
   + Src("hoot0", msgs(IDS["threads"]["Hootline"])[0]["body_text"]).q("Your three social profiles are connected") + "), "
   + "Balancy (thread \"[SOURCE_ORG_0001] & Balancy\", Frederick on every message; Leonard after a call with them: " + BCALL.q("Thank you again for your time on Thursday.") + ") and Nintendo (two no-reply Nintendo Developer Portal notices to Frederick, Thu Sep 4: "
   + NR.q(nin_req["subject"]) + " and " + ND.q(nin_done["subject"]) + ", which shows " + ND.q("NDA Effective: 09/04/2025") + " and says "
   + ND.q("This is an automatically generated email. Please do not reply.") + "). Stay off the log: Rayking Game (Leonard's forward " + RAY.q("Should we explore for DD?")
   + "; Frederick's reply to it is an unsent draft addressed to Leonard, labelled " + RAYL.q("Opened,Drafts") + ", so nobody answered Rayking), "
   + "Appodeal's publishing program (Frederick replied " + day(apo_fred[0]["date"]) + " and " + day(apo_fred[1]["date"]) + "; their last mail, " + day(apo_last["date"]) + ": "
   + APL.q("Just checking in to see if you’ve had a chance to consider our proposal") + "), which is ad-monetization and UA work (" + APT.q("ROAS-focused testing") + "; " + APT.q("Since we support parallel UA")
   + "), so it stays with the ad networks on the UA budget call (@@hub@@), AppCamp (an invite Frederick declined on " + day(acmp_fred["date"]) + ", " + ACF.q("I won't be able to make it")
   + "; the event was " + ACI.q("August 6–8, 2025") + "), Playable Factory (the thread holds only their two pitches, Sep 11 and Sep 24), Gamesforum SF (a Sep 10 speaker invite whose thread holds only that message; their other mails are newsletters), "
   + "InterCo Digital (the thread holds only their three mails, Aug 27 to Sep 18), the Google check-in (an ad network), Singular (" + SING.q(BND["singular"][0]["subject"]) + "; named in @@hub@@), "
   + "NCsoft and Dentsu (investor talks, which @@hub@@ keeps off: Leonard to NCsoft, " + day(ncs["date"]) + ", " + NCS.q("conversations with other VCs and companies are moving along")
   + ", and to Dentsu, " + day(den["date"]) + ", " + DEN.q("Dentsu’s investment focus across games, transmedia, and AI-powered game development tools") + ") and Nova Rewards, which withdrew on " + day(nova["date"]) + ": "
   + NOVA.q("I'm withdrawing this offer for now") + ". 36 companies in all.")


# ------------------------------------------------------------------ the companies
def company_event(k):
    t = TRUTH[k]
    tid = IDS["threads"][k]
    ms = msgs(tid)
    first = ms[0]
    them = [m for m in ms if not m["from_email"].endswith("@harmonygames.co")]
    ask = them[-1]
    name, mail = PERSON[k]
    asks, plines, why = CO[k]
    ttl, P = paper(IDS["papers"][k])
    A = Src(f"{k}:ask", ask["body_text"])
    if first["from_email"] == FRED:
        lead = f"Frederick wrote to {name} first, {day(first['date'])}; {name} ({mail}), {pt(ask['date'])}: "
    else:
        lead = f"{name} ({mail}), {pt(ask['date'])}: "
    exp = lead + " ".join(A.q(a) for a in asks) + " Paper: " + "; ".join(P.q(x) for x in plines) + ". "
    if k in HOLD:
        fm = [m for m in ms if m["from_email"] == FRED and HOLD[k] in clean(m["body_text"])][0]
        exp += f"Frederick's reply, {day(fm['date'])}, " + Src(k + ":hold", fm["body_text"]).q(HOLD[k]) + ", is a holding reply, not an answer. "
    exp += why
    if t["Decision"] == "Park" and k != "Framewell":
        exp += " " + PARK_NOTE
    where = "its deck in Drive/Slides" if not rows("gdocs.docs_documents", document_id=IDS["papers"][k]) else "its paper in Drive"
    ev("co:" + k, f"Read the {k} thread in Gmail (subject \"{first['subject']}\") and {where} (\"{ttl}\")", exp)


for d in ("Answered", "End", "Keep", "Sign", "Park"):
    for k in ORDER[d]:
        if k == "Balancy":
            ev("co:Balancy", "Read the Balancy thread in Frederick's Gmail (search \"Balancy\")",
               f"Seven messages. Balancy's rep PERSON_0527_NAME (PERSON_0527_EMAIL), {pt(bal_ask['date'])}: " + BASK.q("We offer a 1-month trial to integrate and test features.")
               + f" Leonard's answer, {pt(bal_lv['date'])}: " + BLV.q("We are still interested in your product but company priorities have shifted a bit for the next few months - we'll circle back with you as soon as we get some bandwidth.")
               + f" The rep's last mail, {day(bal_last['date'])}: " + BLAST.q("Absolutely, thank you for the update.")
               + " Already answered by Leonard on Thu Sep 11, and the answer was later (guardrails step 1): Answered, no new answer, it comes back at the January review. Next date Jan 5, 2026 (@@review@@).")
            continue
        if k == "Motive Forge":
            ms = msgs(IDS["threads"][k])
            hugo, art = ms[0], ms[-1]
            ttl, P = paper(IDS["papers"][k])
            ev("co:Motive Forge", f"Read the Motive Forge thread in Frederick's Gmail (search \"Motive Forge\"; subject \"{hugo['subject']}\") and its paper in the paperwork folder (\"{ttl}\")",
               f"Hugo Lambert ({hugo['from_email']}) to Frederick, Arthur cc, {pt(hugo['date'])}: " + Src("mf0", hugo["body_text"]).q("$6,400, four weeks from kickoff")
               + "; paper " + P.q("Price: $6,400, 50% on kickoff") + f". Arthur Blake's reply, {pt(art['date'])}: " + Src("mf1", art["body_text"]).q("Thanks Hugo, we're keeping the art in-house, so we'll pass on this one.")
               + " Already answered by Arthur on Fri Sep 19, and not a later (step 1): Answered, no new answer, no reminder; Next date blank.")
            continue
        if k == "Hootline":
            h0, h1 = msgs(IDS["threads"][k])
            ev("co:Hootline", f"Read the Hootline thread in Frederick's Gmail (search \"Hootline\"; subject \"{h0['subject']}\"; no paper)",
               f"Gemma Doyle ({h0['from_email']}), {pt(h0['date'])}: " + Src("h0", h0["body_text"]).q("the startup promo keeps the account free until Jan 31, 2026. After that it's $39/month unless you cancel.")
               + f" Gemma, {pt(h1['date'])}: " + Src("h1", h1["body_text"]).q("when the startup promo ends on Jan 31, would you like to keep the scheduler after that?")
               + " Free until January: Park. " + PARK_NOTE)
            continue
        if k == "Nintendo":
            ev("co:Nintendo", "Find Nintendo in Linear (search \"Nintendo\"; the portal registration from @@sweep@@)",
               f"Issue {zom['identifier']} \"{zom['title']}\"; Arthur's comment, created {zc['created_at']}: "
               + ZC.q("the Global ToS and NDA still needs our agreement approver to accept it, and that has to be a company officer from their own login") + "; "
               + ZC.q("no fee, no fixed term, no exclusivity, nothing about our IP, and either side can end it") + "; " + ZC.q("It has to be accepted by Oct 15 or the request lapses.")
               + " So despite the Registration Completed notice it still waits on an officer: Sign, a card, no ESG trigger. The portal is a no-reply sender: no written answer and no contact. Next date Oct 15, 2025.")
            continue
        company_event(k)
        if k == "Lanternfly Publishing":
            ev("lf_dm", "Search Slack for \"Southeast Asia\" (from the Lanternfly deck) and open the reply in Frederick's DM with Leonard",
               f"A reply by Leonard in the DM thread under his {day(dt.datetime.fromtimestamp(float(dmroot['ts']), dt.timezone.utc).isoformat())} message " + DMR.q("we have no localization though") + f", posted {pt(dmr['created_at'][:19] + 'Z')}: " + DM.q(clean(dmr["text"]))
               + ". Wen is Lanternfly's contact (@@co:Lanternfly Publishing@@) and Saturday was Sep 27. Already answered by Leonard, and the answer was later (step 1): Answered, no new answer to Wen, it comes back at the January review. Next date Jan 5, 2026 (@@review@@).")
        if k == "Spotlight Fest":
            ev("sp_note", "Search Slack #executives for \"indie showcase\" (Spotlight Fest's Dec 5 showcase)",
               f"Robert, {pt(spn['created_at'][:19] + 'Z')}: " + SPN.q(clean(spn["text"]))
               + ". Rina and the Dec 5 showcase are Spotlight Fest's (@@co:Spotlight Fest@@). Already answered by Robert on Wed Sep 17, and not a later: Answered, no new answer, no reminder; Next date blank.")
        if k == "Clipforge":
            ev("notice", "Search Frederick's Gmail for \"HG-2291\" (the workspace on the Clipforge paper) and read the notice",
               f"A notice from {nt['from_name']} ({nt['from_email']}), {pt(nt['date'])}, subject " + NTS.q(nt["subject"]) + ": "
               + NT.q("Under your agreement the pilot now ends on Oct 15, 2025 and the Studio plan starts on Oct 16 at $1,800/month.") + " "
               + NT.q("To cancel before the plan starts, write to billing@paylane.io by Oct 15. Replies to this email aren't monitored.")
               + " The paid plan now starts inside Oct 1 to Dec 31 (step 2): End. Cancel in writing to billing@paylane.io, and answer Priya, who asked to be told. Next date Oct 15, 2025.")
        if k == "Framewell":
            ev("waiver", "Search Slack for \"Maren\" (Framewell's contact) and open the thread reply it finds",
               f"Leonard's reply in the #executives thread under his {day(ptr['ts'] and dt.datetime.fromtimestamp(float(ptr['ts']), dt.timezone.utc).isoformat())} post " + PTR.q("Playtestcloud results are in") + f", posted {pt(waiv['created_at'][:19] + 'Z')}: " + WAIV.q(clean(waiv["text"]))
               + ". So nothing is owed before January: Park, not End. " + PARK_NOTE)

# ------------------------------------------------------------------ writes: the log
ev("w:create", "Create the log spreadsheet in Google Sheets (title from @@readme@@)", "A new spreadsheet named \"Q4 commitments log\".")
ROWLIST = ("Answered: Balancy (Leonard, Thu Sep 11; Next date Jan 5, 2026), Lanternfly Publishing (Leonard, Sat Sep 27; Jan 5, 2026), Motive Forge (Arthur, Fri Sep 19; blank), "
           "Spotlight Fest (Robert, Wed Sep 17; blank). End: Ascendo Oct 1, Brightlane Studio Oct 1, Lingora Oct 3, Panelpulse Oct 6, Pixel Harbor Events Oct 10, "
           "Clipforge Oct 15, Soundvault Oct 15, Wishwave Oct 17, Reviewly Oct 19, Streamcast Talent Oct 31. Keep: Vaultline Oct 12, Certwell Oct 20, Pingwise Nov 1. "
           "Sign: Playfuse Oct 8, Nintendo Oct 15, Kinetic Arcade Oct 20, Orbit Store Oct 24, Lumencloud Oct 31, Bundlehouse Nov 1, Markward blank. "
           "Park, all Jan 5, 2026: Benchmarkly, Cloudlark, Driftwood Audio, Echohall, Framewell, Glyphworks, Hootline, Loopnote, Pressbeam, Quillcraft, Retainly, Tilecast. "
           "Contact is each company's person (blank for Nintendo); What we told them matches the decision, with Lanternfly's row giving Leonard's answer (Southeast Asia waits until after the raise; January) "
           "and Kinetic Arcade's, Lumencloud's and Bundlehouse's saying it is with our lawyers first.")
ev("w:rows", "Write the header and one row per company into the new log in Sheets (rows from @@co:Lanternfly Publishing@@ to @@co:Driftwood Audio@@)",
   "Row 1 is the template header (@@template@@); then 36 rows, all dates in 2025 unless shown. " + ROWLIST)
ev("w:move", "Move the log into the Q4 commitments folder in Drive (folder from @@folder@@)", f"The log's parent is the folder \"{fold['name']}\".")

# ------------------------------------------------------------------ writes: written answers
SAY = {"End": "saying we're not going ahead", "Keep": "saying we're staying", "Park": "saying we'll pick it up in January",
       "Sign": "saying it's with Leonard or Arthur to sign"}
SPECIAL = {"Reviewly": "cancelling the trial before it moves to Growth (by Oct 19)",
           "Vaultline": "saying we're staying and to keep the backups running on Standard",
           "Certwell": "saying we're staying and confirming the renewal",
           "Pingwise": "saying we're staying on Team, no downgrade",
           "Kinetic Arcade": "saying it's with our lawyers first, then Leonard or Arthur to sign",
           "Lumencloud": "saying it's with our lawyers first, then Leonard or Arthur to sign",
           "Bundlehouse": "saying it's with our lawyers first, then Leonard or Arthur to sign",
           "Clipforge": "saying we're not carrying on after the pilot"}
ev("w:paylane", "Email billing@paylane.io to cancel the Clipforge workspace in Gmail (address from @@notice@@)",
   "A sent email to billing@paylane.io cancelling workspace HG-2291 (UGC Studio) before the Studio plan starts on Oct 16.")
for d in ("End", "Keep", "Sign", "Park"):
    for k in ORDER[d]:
        if k == "Nintendo":
            continue
        name, mail = PERSON[k]
        ev("w:ans:" + k, f"Reply to {name} on the {k} thread in Gmail (@@co:{k}@@)",
           f"A sent reply to {mail} {SPECIAL.get(k, SAY[d])}.")

# ------------------------------------------------------------------ writes: ESG intake
ESGX = {"Kinetic Arcade": "the publishing letter of intent for Japan and Korea; exclusivity for 12 months from signature for those territories, and the letter mentions no automatic renewal; no fees to us (revenue share); needed by Oct 20, 2025",
        "Lumencloud": "the Startup Program Agreement ($25,000 of credits); term 36 months from signature, and the agreement mentions no automatic renewal; no charges while credits last; needed by Oct 31, 2025",
        "Bundlehouse": "the participation agreement for the Holiday Puzzle Bundle; a licence to use our game's name, logo and art in bundle marketing for 18 months, and the proposal mentions no automatic renewal; no cost to join (revenue share); needed by Nov 1, 2025"}
for k, x in ESGX.items():
    ev("w:esg:" + k, f"Email ESG Law intake about the {k} agreement in Gmail (new message to the contact from @@esg_contact@@)",
       f"A sent email to {esgc['email']} with the checklist items (@@checklist@@) for {k}: {x}; signer Leonard or Arthur.")

# ------------------------------------------------------------------ writes: cards
for k in sorted(ORDER["Sign"]):
    ev("w:card:" + k, f"Create the {k} card in the To Do list in Trello (@@board@@)",
       f"A new card in \"To Do\" with \"{k}\" in its title.")

# ------------------------------------------------------------------ writes: contacts
ex = [r for r in rows("contacts.contacts") if r["contact_id"] != "9b0185e445572aeee9f27d35"]
EXN = {r["job"]: f"{r['first_name']} {r['last_name']}" for r in ex}
ev("contacts_check", "Search Contacts for each company's person (names from the company events)",
   "Already in Contacts: " + ", ".join(f"{EXN[j]} (job \"{j}\")" for j in ("Kinetic Arcade", "Lumencloud", "Markward"))
   + ". None of the other 32 people is there yet; Nintendo has no person.")
ADD = sorted(k for k, v in TRUTH.items() if "contact_add" in v["groups"])
assert len(ADD) == 32
_q = [{"id": "ctl", "query": "Hayes", "limit": 5}] + [{"id": k, "query": PERSON[k][1] if PERSON[k][0].startswith("PERSON") else PERSON[k][0].split()[-1], "limit": 5} for k in ADD]
_p = subprocess.run(["python3", "-B", "Task_Authoring/tools/hg.py", "search", "search-many", "--request", "-", "--compact"], cwd=WS, capture_output=True, text=True,
                    input=json.dumps({"service": "contacts", "file": "contacts.json", "queries": _q}),
                    env={**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"})
_r = json.loads(_p.stdout)["queries"]
assert _r["ctl"]["matches"] and all(_r[k]["scan_complete"] and not _r[k]["matches"] for k in ADD), "contacts absence check"
assert all(PERSON[k][0] not in EXN.values() for k in ADD)
for k in ADD:
    name, mail = PERSON[k]
    ev("w:contact:" + k, f"Add {name} to Contacts", f"A new contact {name}, email {mail}, job \"{k}\".")

# ------------------------------------------------------------------ writes: January reminders
REVK = sorted(k for k, v in TRUTH.items() if "revisit" in v["groups"])
assert len(REVK) == 14
for k in REVK:
    ev("w:rem:" + k, f"Add a {k} reminder to Frederick's calendar on the review day (Calendar; @@review@@)",
       f"A new event on Mon Jan 5, 2026 with \"{k}\" in its title.")

# ------------------------------------------------------------------ write: the reply to Leonard
ev("w:hub", "Reply to Leonard on his email in Gmail (message from @@hub@@)",
   f"A sent reply in the thread \"{hub['subject']}\" to leonard.hayes@harmonygames.co: keeping Certwell, Pingwise and Vaultline; waiting on Arthur or Leonard to sign "
   "Bundlehouse, Kinetic Arcade, Lumencloud, Markward, Nintendo, Orbit Store and Playfuse.")

# ------------------------------------------------------------------ number and render
NUM = {k: i + 1 for i, (k, _, _) in enumerate(EV)}
assert len(NUM) == len(EV), "duplicate event keys"


def refs(s):
    def r(m):
        return f"OE {NUM[m.group(1)]}"
    return re.sub(r"@@(.+?)@@", r, s)


out = []
for k, head, exp in EV:
    out.append(f"OE {NUM[k]}  {refs(head)}\nExpected: {refs(exp)}\n")
text = "\n".join(out)
assert "@@" not in text and "<" not in text.replace("<>", ""), "unresolved ref or angle bracket"
open(os.path.join(TI, "08_Oracle_Events.md"), "w").write(text)
nw = sum(1 for k, _, _ in EV if k.startswith("w:"))
json.dump({"events": len(EV), "writes": nw, "chars": len(text), "quotes_checked": len(CHECKS), "num": NUM, "checks": CHECKS,
           "events_text": {k: refs(exp) for k, _, exp in EV}},
          open(os.path.join(HERE, "oe_events_map.json"), "w"), indent=1)
print(f"wrote 08_Oracle_Events.md: {len(EV)} events ({nw} writes), {len(text)} chars, {len(CHECKS)} quotes asserted")
