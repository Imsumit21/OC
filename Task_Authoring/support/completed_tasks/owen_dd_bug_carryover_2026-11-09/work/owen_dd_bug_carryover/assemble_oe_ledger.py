#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep) for owen_dd_bug_carryover (rev9 SQL ea5b542897c8).
Seeded rows are parsed from the SQL (never executed); base records come from plan/oe_base.json (fresh hg.py reads, plan/oe_reads.py)
and plan/oe_defer.json (plan/oe_defer.py). Facts and dependency edges only; no event text.
Every quote is asserted as a substring of its record, so a wrong value stops the build."""
import datetime as dt
import hashlib
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
PERSONA = "owen_baker"
TDREL = "Task_Authoring/task_inputs"
PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQL_PATH).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
COH = json.load(open(os.path.join(HERE, "cohort.json")))
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


def ts_iso(ts):
    return dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def when(iso):
    d = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M%p').replace('AM', 'am').replace('PM', 'pm')} {p.tzname()} ({d.strftime('%Y-%m-%dT%H:%M:%SZ')})"


def safe(s):
    """Record text inside a backtick quote: no backticks, no pipes, no newlines; boxes spelled out."""
    return s.replace("`", "'").replace("|", "/").replace("\n", " / ").replace("☐", "(unticked box)").replace("☑", "(ticked box)").strip()


def must(text, *quotes):
    for q in quotes:
        assert q in text, (q, text[:300])
    return " · ".join("`" + safe(q) + "`" for q in quotes)


def tools(*names):
    for n in names:
        assert n in CATALOG, n
    return ", ".join(names)


FACTS, fid_of = [], {}


def fact(key, value, service, tl, locator, origin, expected, result, visible, depends, source):
    assert source
    n = f"F{len(FACTS) + 1}"
    fid_of[key] = n
    FACTS.append([n, value, service, tl, locator, origin, expected, result, visible, depends, source])
    return n


def dep(*keys):
    return ", ".join(fid_of[k] for k in keys) or "—"


F = dep
UNSC = "unscoped service; natural pointer in the Locator origin column"
SY = "YES (proof below)"

# ---------------------------------------------------------------- base Slack, indexed
SLK = {}
for f, recs in OB["slack_files"].items():
    for i, m in enumerate(recs):
        SLK[f"{m['channel']}/{m['ts']}"] = {"file": f.split("/", 1)[1].split("/", 1)[1], "pointer": f"/{i}", "rec": m}
for k, v in OB["slack"].items():
    SLK[k] = {"file": v["file"].split("/")[-1], "pointer": v["pointer"], "rec": v["rec"]}


def bt(k):
    return SLK[k]["rec"]["text"]


def bsrc(k):
    return f"{k} (slack {SLK[k]['file']} {SLK[k]['pointer']})"


SM = {f"{r['channel_id']}/{r['ts']}": r for r in rows("slack.slack_messages")}


def st(k):
    return clean(SM[k]["text"])


# ================================================================ the request and its incorporated rules
HUB = "D05S1S2AB5M/1770937805.214409"
HUBQ = ["I want the whole list moved over, the fixed ones too", "How we call each one is in the carry-over notes doc I shared with you",
        "While you're in there bring the UI Changes tree up to date, it never got closed out, and leave a line on every child saying where it landed",
        "Put a sheet in your DD bug carry-over folder so I can look things up, and share it with everyone on Sunday's bug review",
        "Then tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done"]
fact("hub", "Arthur's DM: the request", "Slack (Owen's DM with Arthur)", tools("slack_search_public_and_private", "slack_read_channel"),
     "Owen's 1:1 DM with Arthur Blake, Arthur's message of Thursday", 'prompt ("Arthur sent me a DM on Thursday")',
     f"{HUB}, sent {when(ts_iso('1770937805.214409'))} by Arthur Blake (Thursday 3:10pm PT). Quotes: " + must(st(HUB), *HUBQ),
     "VERIFIED: every quote cut from the message text", SY, "—", f"{HUB}, {L(HUB)}")

DOC = "f_3ca9e15d7b20f4e681ad52"
doc = clean(rows("gdocs.docs_documents", document_id=DOC)[0]["body_text"])
docf = rows("gdrive.drive_files", id=DOC)[0]
DOCQ_SCOPE = ["every ticked or unticked line in the comment channel of Vincent's Android canvas, and every bug posted in the bug channel after the last line in that comment channel",
              "A comment whose line was deleted has nothing to carry over.", "In the bug channel a follow-up on a bug already posted is part of that bug, and a design question for Leonard or a post that points at a QA doc isn't a bug post.",
              "Robert's reports in the sub-250 channel aren't part of this", "The economy canvas and the ZM canvases stay where they are."]
DOCQ_OUT = ["One Linear record per canvas line and one per bug posted after it.", "A canvas line and a later post stay separate even where they read alike.", "Take the first outcome that fits.",
            "Fixed: the tick stands, or a later record says it was fixed. File it as Done.", "Gone: it isn't fixed and it's a bug in something the build players have no longer has. File it as Canceled.",
            "Covered: it isn't fixed and an open ticket already covers it. Don't file a new one, add a note on that ticket with the canvas wording.", "Vincent tied a few lines to tickets before he left.",
            "Broken: anything else. File it as Bugs."]
DOCQ_COUNT = ["we go by the Android build players have, 0.3.310, which came off the economy line, not by develop", "A tick on the canvas stands unless a later record about that bug says otherwise.",
              "An unticked line, or a bug nobody closed, stays open unless a later record says it was fixed, and a commit named for the bug counts as that record if nothing later says otherwise.",
              "A fix only counts once it is in that build.", "A PR that never made it into that build doesn't count."]
DOCQ_TICKET = ["Engineering team, Bug label, parent ENG-2401, title is the line without its tick box, or the first line of the post, as it was written, no assignee, nothing in the description",
               "If anything changes after this I'll put it on the master ticket."]
DOCQ_TREE = ["every open child goes Done unless a record shows a piece of its UI work never made it into that build or the screen is switched off there. Then it stays where it is.",
             "Children already Done stay Done and the masters stay as they are.", "A bug on a screen doesn't hold its child, that's what the bug ticket is for.",
             "Brian and Oliver left notes on some of the open children.", "Brian's closing rule from the UI work applies to the line on every child, Done or not."]
DOCQ_SHEET = ["Sheet columns: Bug, Outcome, Ticket, Why.", "When you report back, Covered ones count as still broken."]
fact("rules", "The carry-over notes: scope, the first-fit outcomes, what counts, ticket fields, the tree rule, the sheet columns", "Google Docs (Drive)",
     tools("gdrive_search", "gdocs_get_document_text"), "the Doc titled 'DD bug carry-over notes' shared with Owen",
     'prompt ("Can you take care of everything he asked for, the way he lays it out?": the DM it hands over says "How we call each one is in the carry-over notes doc I shared with you"); ' + dep("hub"),
     f"{DOC}, '{docf['name']}', owner {docf['owner_email']}, created {when(docf['created_time'])}. Scope: " + must(doc, *DOCQ_SCOPE) + ". Outcomes: " + must(doc, *DOCQ_OUT)
     + ". What counts: " + must(doc, *DOCQ_COUNT) + ". New tickets: " + must(doc, *DOCQ_TICKET) + ". UI tree: " + must(doc, *DOCQ_TREE) + ". " + must(doc, *DOCQ_SHEET),
     "VERIFIED: every quote cut from body_text", SY, dep("hub"), f"{DOC}, {L(DOC)}")

amend = rows("linear.linear_comments", issue_id="ENG-2401")[0]
fact("amend", "The later change on the master ticket: the [2231] title prefix", "Linear", tools("linear_get_issue", "linear_list_comments"),
     "the comments on the UI Changes master ticket", 'prompt ("the UI Changes master ticket"); ' + dep("rules") + ' ("I\'ll put it on the master ticket")',
     f"ENG-2401 ('{OB['linear']['ENG-2401']['rec']['title']}', state {OB['linear']['ENG-2401']['rec']['state_id']}), comment {amend['id']} by Arthur Blake, created {when(amend['created_at'])}: "
     + must(clean(amend["body"]), "put [2231] at the front of every title you file so I can filter them"),
     "VERIFIED: quote cut from the comment body; issue title and state read through hg.py", UNSC, dep("rules"), f"ENG-2401, {L(amend['id'])}, linear data.json {OB['linear']['ENG-2401']['pointer']}")

card = rows("trello.trello_cards", id="690b27282f4c1b7a6e93d512")[0]
rule = rows("trello.trello_actions", id="690b29bc3c7d2e51b0f86a47")[0]
rtext = json.loads(rule["data_json"])["text"]
fact("closing", "Brian's closing rule: every child's note names the current public build", "Trello", tools("trello_search", "trello_get_card", "trello_get_card_actions"),
     "the card 'UI optimization pass' on the DD Product Roadmap board, its comments", dep("rules") + ' ("Brian\'s closing rule from the UI work"); search "UI optimization pass"',
     f"Card 690b27282f4c1b7a6e93d512 '{card['name']}' (desc " + must(clean(card["desc"]), "Tickets are under the UI Changes master.") + f"); comment 690b29bc3c7d2e51b0f86a47 by Brian Foster, created {when(rule['date'])}: "
     + must(rtext, "every one gets a note naming the current public build"),
     "VERIFIED: quotes cut from the card desc and the comment text", UNSC, dep("rules"), f"690b29bc3c7d2e51b0f86a47, {L('690b29bc3c7d2e51b0f86a47')}")

FOLDER = "d_9b41e7c2a05d36f8e1c7a4"
fo = rows("gdrive.drive_files", id=FOLDER)[0]
fact("folder", "Owen's 'DD bug carry-over' folder (the sheet's destination)", "Google Drive", tools("gdrive_search", "gdrive_move_file", "gdrive_create_file"),
     "the folder named 'DD bug carry-over' in Owen's Drive", 'prompt ("the sheet in my DD bug carry-over folder")',
     f"{FOLDER}, '{fo['name']}', {fo['mime_type']}, owner {fo['owner_email']}, created {when(fo['created_time'])}; empty before the run",
     "VERIFIED: name, type and owner read from the drive_files row", SY, "—", f"{FOLDER}, {L(FOLDER)}")

EVT = "evt_6e2c91d4b07f3a58c1d2e4"
ev = rows("gcal.gcal_events", event_id=EVT)[0]
att = [a["email"] for a in json.loads(ev["attendees_json"])]
fact("review", "Sunday's bug review: who is on it", "Google Calendar (Owen's calendar)", tools("gcal_list_events", "gcal_get_event"),
     "the event 'DD bug review' on Owen's calendar, Sunday Feb 15", 'prompt ("everyone on the review"); ' + dep("hub") + ' ("everyone on Sunday\'s bug review")',
     f"{EVT}, '{ev['summary']}', organizer {ev['organizer_email']}, starts {when(ev['start_ts'])}, created {when(ev['created'])} (semantic future date: the review has not happened). Attendees: " + ", ".join(att)
     + ". Everyone on it other than Owen: arthur.blake@harmonygames.co, robert@harmonygames.co, oliver.brooks@harmonygames.co",
     "VERIFIED: summary, start and attendees read from the event row", SY, dep("hub"), f"{EVT}, {L(EVT)}")
assert att == ["arthur.blake@harmonygames.co", "robert@harmonygames.co", "oliver.brooks@harmonygames.co", "owen.baker@harmonygames.co"]

ct = OB["contacts"]
fact("emails", "The three reviewers' addresses", "Contacts", tools("contacts_search_contacts"), "contacts for Arthur Blake, Robert and Oliver Brooks", dep("review") + " (attendee addresses)",
     "; ".join(f"{e}: {ct[e]['rec']['first_name']} {ct[e]['rec']['last_name']}".strip() for e in ct) + " (the same addresses as the event's attendees)",
     "VERIFIED: names and addresses read from contacts.json", UNSC, dep("review"), ", ".join(f"contacts.json {ct[e]['pointer']}" for e in ct))

# ---------------------------------------------------------------- the population
CV = OB["slack_files"]["messages/CE156FDFB428/2025-11.json"]
roots = [m for m in CV if m.get("subtype") == "document_comment_root"]
lines = [m for m in roots if m["text"].strip()]
empty = [m for m in roots if not m["text"].strip()]
canvas_ids = [b["id"] for b in COH["bugs"] if b["kind"] == "canvas_line"]
assert len(roots) == 69 and len(lines) == 63 and len(empty) == 6 and {f"CE156FDFB428/{m['ts']}" for m in lines} == set(canvas_ids)
last = max(m["ts"] for m in lines)
fact("canvas", "The canvas comment channel: 63 lines (6 more root comments are empty: their lines were deleted)", "Slack (canvas comment channel)",
     tools("slack_search_channels", "slack_read_channel", "slack_read_thread"), "the comment channel of Vincent's Android canvas, 'Bugs on Android 2231'",
     'prompt ("getting DD\'s bug list out of Slack"); ' + dep("rules") + ' ("the comment channel of Vincent\'s Android canvas")',
     f"69 document_comment_root posts, Nov 13 to Nov 21 2025; 63 carry a line (the first CE156FDFB428/{lines[0]['ts']}, the last CE156FDFB428/{last}, posted {when(ts_iso(last))}); "
     f"6 have empty text (CE156FDFB428/{empty[0]['ts']}, CE156FDFB428/{empty[1]['ts']}, CE156FDFB428/{empty[2]['ts']}, CE156FDFB428/{empty[3]['ts']}, CE156FDFB428/{empty[4]['ts']}, CE156FDFB428/{empty[5]['ts']}). Each line starts with a ticked or unticked box: "
     f"{sum(1 for m in lines if m['text'].startswith('☑'))} ticked, {sum(1 for m in lines if m['text'].startswith('☐'))} unticked",
     "VERIFIED: 69 roots counted in the channel's only month file (272 records, read whole through hg.py); texts and boxes read on each", SY, dep("rules"),
     f"CE156FDFB428/{lines[0]['ts']} (slack 2025-11.json, 272 records)")

POSTS = [b for b in COH["bugs"] if b["kind"] == "later_bug"]
BUGCH = []
for f in ["messages/C05V5FNLB9V/2025-11.json", "messages/C05V5FNLB9V/2025-12.json", "messages/C05V5FNLB9V/2026-02.json"]:
    BUGCH += [m for m in OB["slack_files"][f] if (not m.get("thread_ts") or m["thread_ts"] == m["ts"]) and float(m["ts"]) > float(last)]
BAR1, BAR2 = "C05V5FNLB9V/1766415211.386389", "C05V5FNLB9V/1766415326.501939"
CLASS = {"1764091385.285289": "chatter (where the canvases are)", "1764091406.099819": "chatter", "1764091558.839139": "chatter", "1764094440.288629": "chatter (asks for a build to test)",
         "1764094458.697489": "chatter", "1764256319.497399": "follow-up on the mega tile post (asks about the new symbols)", "1764659554.897599": "follow-up on the flickering post ('Happened twice in the video')",
         "1764662837.138929": "points at a QA doc ('tested your build for the most part' with a doc link)", "1766415326.501939": "second message of the bottom bar post (its thread holds the 60 replies)",
         "1767191512.428539": "a design question for Leonard (no-ads and rewarded video)", "1767197458.963919": "Leonard's answer", "1767197512.579159": "Leonard's answer"}
bug_ts = {b["id"].split("/")[1] for b in POSTS} | {"1766415211.386389"}
listing = []
for m in BUGCH:
    if m.get("subtype") in ("tabbed_canvas_updated", "channel_leave", "channel_join"):
        continue
    if m["ts"] in bug_ts and m["ts"] != "1766415326.501939":
        continue
    listing.append(f"C05V5FNLB9V/{m['ts']} {CLASS[m['ts']]}")
fact("posts", "The bug channel after the last canvas line: 7 bug posts", "Slack (#god-bugs)", tools("slack_read_channel", "slack_read_thread", "slack_conversations_search_messages"),
     "the bug channel #god-bugs, top-level posts after the last canvas line", 'prompt ("getting DD\'s bug list out of Slack"); ' + dep("rules", "canvas") + ' ("every bug posted in the bug channel after the last line")',
     "Bug posts (first line of each): " + "; ".join(f"{b['id'] if b['id'] != 'C05V5FNLB9V/1766415326.501939' else BAR1} `{safe(bt(b['id'] if b['id'] != 'C05V5FNLB9V/1766415326.501939' else BAR1).split(chr(10))[0][:90])}`" for b in POSTS)
     + ". Not bug posts: " + "; ".join(listing) + "; plus canvas-update, leave and join rows",
     "VERIFIED: every top-level row after the last line read in the Nov, Dec and Feb month files (Jan has no file); 7 counted by the rule doc's tests", SY, dep("rules", "canvas"),
     f"{BAR1} (slack 2025-12.json), C05V5FNLB9V/1764256187.655299 (slack 2025-11.json)")

# ---------------------------------------------------------------- the deciding records
fact("lives", "Lives are gone from the economy line", "Slack (shared publishing channel) + Google Docs", tools("slack_read_channel", "gdocs_get_document_text"),
     "Leonard Hayes's Dec 2 update in the shared publishing channel and the 'Economy Changes for Domino Delights' doc", dep("rules") + ' ("the build players have ... came off the economy line"); search "removing lives"',
     f"C09SWTHEMEW/1764659626.614679, posted {when(ts_iso('1764659626.614679'))}: " + must(bt("C09SWTHEMEW/1764659626.614679"), "We are removing lives feature from the game and replacing it with a ticket system")
     + f". Doc f_948768f5a462e7037d17c9 '{OB['gdocs']['f_948768f5a462e7037d17c9']['rec']['title']}': " + must(OB['gdocs']['f_948768f5a462e7037d17c9']['rec']['body_text'], "lives system and replacing it with tickets"),
     "VERIFIED: quotes cut from the message and the doc body", SY, dep("rules"), f"{bsrc('C09SWTHEMEW/1764659626.614679')}, f_948768f5a462e7037d17c9 (gdocs data.json {OB['gdocs']['f_948768f5a462e7037d17c9']['pointer']})")

WC = ["C9CA62B5180A/1765927350.212199", "C9CA62B5180A/1765927876.696389", "C9CA62B5180A/1765928003.630799"]
fact("wc", "Win & Collect is switched off on the economy line", "Slack (group DM)", tools("slack_search_public_and_private", "slack_read_channel"),
     "the group DM with Leonard, Brian and Arthur, Dec 16", dep("rules") + ' ("the screen is switched off there"); search "disable WC"',
     f"{WC[0]} (Arthur, {when(ts_iso('1765927350.212199'))}): " + must(bt(WC[0]), "can you disable WC and I'll start deploying stuff to prod")
     + f"; {WC[1]} (Owen, {when(ts_iso('1765927876.696389'))}): " + must(bt(WC[1]), "event disabled") + f"; {WC[2]} (Owen): " + must(bt(WC[2]), "pushed to EconomyChanges branch"),
     "VERIFIED: quotes cut from the three base records read through hg.py", SY, dep("rules"), ", ".join(bsrc(x) for x in WC))

pr = OB["github"]["harmonygames-Games/GameOfDominoes#1913"]["rec"]
fact("pr1913", "The window fix never merged", "GitHub", tools("github_list_pull_requests", "github_get_pull_request"), "PR 'Fixing window in tile dozer scene' in GameOfDominoes",
     dep("rules") + ' ("A PR that never made it into that build doesn\'t count"); search "Fixing window in tile dozer"',
     f"harmonygames-Games/GameOfDominoes#1913 '{pr['title']}', state {pr['state']}, merged {pr['merged']}, base {pr['base_ref']}, head {pr['head_ref']}, created {when(pr['created_at'])}",
     "VERIFIED: title, state, merged and refs read from the pull_requests record", UNSC, dep("rules"), f"harmonygames-Games/GameOfDominoes#1913 (github data.json {OB['github']['harmonygames-Games/GameOfDominoes#1913']['pointer']})")

fact("window_claim", "Marcus's 'fixed it' reply on the window post", "Slack (#god-bugs)", tools("slack_read_thread"), "the thread under the tile dozer window post", dep("posts"),
     f"C05V5FNLB9V/1764329192.159229, {when(ts_iso('1764329192.159229'))}: " + must(bt("C05V5FNLB9V/1764329192.159229"), "Ok i fixed it and did a PR") + "; nothing later in the thread",
     "VERIFIED: quote cut from the reply; the thread holds one reply (reply_count 1)", SY, dep("posts"), bsrc("C05V5FNLB9V/1764329192.159229"))

SHOP = "C09Q4S613CN/1764606918.318209"
fact("shop", "The shop icons came back (Dec 1)", "Slack (#dd-road-to-sub-250mb)", tools("slack_search_public_and_private", "slack_read_thread"),
     "Brian's reply under the gems post in the sub-250 channel", dep("rules") + ' ("unless a later record about that bug says otherwise"); search "shop prefabs"',
     f"{SHOP}, Brian Foster, {when(SM[SHOP]['created_at'])}, a reply under C09Q4S613CN/1764042435.541279 (`{safe(bt('C09Q4S613CN/1764042435.541279'))}`): "
     + must(st(SHOP), "the round icons on the River Tile and Memory Tile shops are there again on the current build, so don't trust that tick"),
     "VERIFIED: quote cut from the seeded reply; parent text read through hg.py", SY, dep("rules"), f"{SHOP}, {L(SHOP)}, {bsrc('C09Q4S613CN/1764042435.541279')}")

TAV = "D05USBTQY1F/1765452012.418229"
fact("tavern", "The Tavern frame went again (Dec 11)", "Slack (Owen's DM with Marcus)", tools("slack_search_public_and_private", "slack_read_channel"),
     "Marcus Bennett's DM to Owen, Dec 11", dep("rules") + ' ("unless a later record about that bug says otherwise"); search "Tavern buttons"',
     f"{TAV}, Marcus Bennett, {when(SM[TAV]['created_at'])}: " + must(st(TAV), "the Tavern buttons lost their frame again on last night's Android build", "Brian's fix didn't hold"),
     "VERIFIED: quotes cut from the seeded message", SY, dep("rules"), f"{TAV}, {L(TAV)}")

VR = {"train": ("CE156FDFB428/1763845212.507119", "train level backgrounds are broken", ["the snow train is still off", "leaving this one open"]),
      "team": ("CE156FDFB428/1763742012.611229", "When I created a team and quitted it the", ["the navigation bar still goes after quitting"]),
      "lives1": ("CE156FDFB428/1763845812.703339", "I found the issue lives are not decreased after", ["a loss still doesn't take a life"]),
      "lives2": ("CE156FDFB428/1763845872.804449", "Lives are only decreased after losing twice in a", ["it still only drops on the second loss"])}
for k, (rid, bug, qs) in VR.items():
    fact(f"vr_{k}", f"Vincent's later reply: the {k.rstrip('12')} line is not fixed", "Slack (canvas comment channel)", tools("slack_read_thread"), "Vincent's reply in the line's thread", dep("canvas"),
         f"{rid}, Vincent Parker, {when(SM[rid]['created_at'])}: " + must(st(rid), *qs), "VERIFIED: quotes cut from the seeded reply", SY, dep("canvas"), f"{rid}, {L(rid)}")

TIP = "CE156FDFB428/1763845512.559339"
fact("tooltips", "The tooltips thread ends on a closed gap", "Slack (canvas comment channel)", tools("slack_read_thread"), "the thread under the navigation bar tooltips line", dep("canvas"),
     f"{TIP}, Vincent Parker, {when(SM[TIP]['created_at'])}, the last reply in the thread: " + must(st(TIP), "the 1 pixel gap is gone and the tooltips look right on my android now"),
     "VERIFIED: quote cut from the seeded reply (thread reply_count 7 after the UPDATE)", SY, dep("canvas"), f"{TIP}, {L(TIP)}")

TAVFIX = [k for k, v in SLK.items() if k.startswith("CE156FDFB428/") and v["rec"].get("thread_ts") == "1763642831.967359" and v["rec"]["text"] == "I send the fix"][0]
fact("tavern_fix", "Brian's fix reply under the Tavern line (Nov 20)", "Slack (canvas comment channel)", tools("slack_read_thread"), "the thread under the Tavern buttons line", dep("canvas"),
     f"{TAVFIX}, Brian Foster, {when(ts_iso(TAVFIX.split('/')[1]))}: " + must(bt(TAVFIX), "I send the fix") + "; earlier than Marcus's DM (F-row for the Tavern frame)",
     "VERIFIED: quote cut from the base reply; author EMPLOYEE_0026 = Brian Foster", SY, dep("canvas"), bsrc(TAVFIX))
ARF = "CE156FDFB428/1763671462.192489"
fact("train_fixed", "Arthur's 'fixed' in the train line's thread (Nov 20)", "Slack (canvas comment channel)", tools("slack_read_thread"), "the thread under the train backgrounds line", dep("canvas"),
     f"{ARF}, Arthur Blake, {when(ts_iso('1763671462.192489'))}: " + must(bt(ARF), "fixed") + "; earlier than Vincent's Nov 22 reply that leaves the line open",
     "VERIFIED: quote cut from the base reply; author EMPLOYEE_0025 = Arthur Blake", SY, dep("canvas"), bsrc(ARF))
PT_LAST = {"C05V5FNLB9V/1764695707.749049": ("flickering", "testing a fix now, I'll let you guys know how it goes."), "C05V5FNLB9V/1764695726.782669": ("music", "thanks for the info, I'll check this issue next."),
           "C05V5FNLB9V/1764694672.078619": ("acid", "I'm checking"), "C05V5FNLB9V/1764694629.652379": ("treasure button", "Thanks")}
fact("post_last", "The last replies in the flickering, music, acid and treasure button threads", "Slack (#god-bugs)", tools("slack_read_thread"), "the threads under those four posts", dep("posts"),
     "; ".join(f"{k} ({w}), {when(ts_iso(k.split('/')[1]))}: " + must(bt(k), qq) for k, (w, qq) in PT_LAST.items()) + " (authors: Owen, Owen, Brian Foster, Robert)",
     "VERIFIED: quotes cut from the base replies; each is its thread's latest_reply", SY, dep("posts"), ", ".join(bsrc(k) for k in PT_LAST))

MAIL = "owen.baker@harmonygames.co/1849333980856689601"
mail = [r for r in rows("gmail.gmail_messages") if r["thread_id"] == MAIL][0]
fact("apple", "Vincent tied the Apple sync line to ENG-2073", "Gmail (Owen's inbox)", tools("gmail_search_messages", "gmail_get_message"), "Vincent Parker's mail to Owen, 'sign in lines on my list'",
     dep("rules") + ' ("Vincent tied a few lines to tickets before he left"); search "sign in lines"',
     f"thread {MAIL}, from {mail['from_email']}, to Owen, sent {when(mail['date'])}, subject '{mail['subject']}', labels INBOX: " + must(clean(mail["body_text"]), "The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new."),
     "VERIFIED: quote cut from body_text", SY, dep("rules"), f"{MAIL}, {L(MAIL)}")
e2073 = OB["linear"]["ENG-2073"]["rec"]
fact("eng2073", "ENG-2073 is an open ticket", "Linear", tools("linear_get_issue"), "the ticket the mail names", dep("apple") + " (the mail names it)",
     f"ENG-2073 '{e2073['title']}', state {e2073['state_id']} (open), team {e2073['team_id']}", "VERIFIED: title and state read through hg.py", UNSC, dep("apple"), f"ENG-2073 (linear data.json {OB['linear']['ENG-2073']['pointer']})")

ali = rows("linear.linear_comments", issue_id="ENG-2363")[0]
e2363 = OB["linear"]["ENG-2363"]["rec"]
fact("signin", "Vincent tied the manual sign-in line to ENG-2363", "Linear", tools("linear_search_issues" if "linear_search_issues" in CATALOG else "linear_list_issues", "linear_list_comments"),
     "Vincent's comment on the open ticket about getting stuck after signing in", dep("rules") + ' ("Vincent tied a few lines to tickets"); search "stuck at splash screen"',
     f"ENG-2363 '{e2363['title']}', state {e2363['state_id']} (open); comment {ali['id']} by Vincent Parker, created {when(ali['created_at'])}: "
     + must(clean(ali["body"]), "the manual sign-in line on my list gets stuck on loading after signing in, same thing as here"),
     "VERIFIED: quote cut from the comment; title and state read through hg.py", UNSC, dep("rules"), f"ENG-2363, {L(ali['id'])}")

NMK = ["ENG-2406", "ENG-2181", "ENG-2351", "ENG-2280", "ENG-2281", "ENG-2398"]
NMC = {k: rows("linear.linear_comments", issue_id=k)[0] for k in NMK}
fact("near_miss", "Six open near-miss tickets, each narrowed by Arthur (Nov 20): none covers the seven unfixed items", "Linear", tools("linear_list_issues", "linear_list_comments"),
     "the open ENG tickets (Bugs, Todo) that read like a canvas line or a bug post", dep("rules") + ' ("an open ticket already covers it")',
     "; ".join(f"{k} '{OB['linear'][k]['rec']['title']}' ({OB['linear'][k]['rec']['state_id']}), comment {NMC[k]['id']} by Arthur Blake, {when(NMC[k]['created_at'])}: " + must(clean(NMC[k]["body"]), clean(NMC[k]["body"])) for k in NMK),
     "VERIFIED: titles and states read through hg.py; comment quotes cut from the SQL rows; that none covers the seven is not_a_claim (derived from each comment's scope)", UNSC, dep("rules"),
     ", ".join(L(NMC[k]["id"]) for k in NMK))
FLK = "C09Q4S613CN/1766164222.418229"
fact("flicker", "Robert says both flickers are gone; the fix is on the economy line", "Slack (#dd-road-to-sub-250mb + #builds)", tools("slack_read_thread", "slack_read_channel"),
     "Robert's reply under his own flickering report, and the EconomyChanges build line in #builds", dep("posts") + '; search "flickering"',
     f"{FLK}, Robert, {when(SM[FLK]['created_at'])}, a reply under C09Q4S613CN/1764013100.931229 (`{safe(bt('C09Q4S613CN/1764013100.931229'))}`): "
     + must(st(FLK), "the flickering is gone on this week's build, both on the play button and coming out of a level")
     + "; C05433XK267/1765310004.760809, " + when(ts_iso("1765310004.760809")) + ": " + must(json.dumps(SLK["C05433XK267/1765310004.760809"]["rec"]["attachments"]), "EconomyChanges Changes:", "Fix for EndLevelPopup flickering on Tap Anywhere clicked"),
     "VERIFIED: quotes cut from the seeded reply and the #builds attachment", SY, dep("posts"), f"{FLK}, {L(FLK)}, {bsrc('C05433XK267/1765310004.760809')}")

B2297 = json.dumps(SLK["C05433XK267/1765310444.095399"]["rec"]["attachments"], ensure_ascii=False)
B2299 = json.dumps(SLK["C05433XK267/1765397569.397939"]["rec"]["attachments"], ensure_ascii=False)
fact("econ_builds", "Android EconomyChanges builds carry the flicker, acid and music fixes and the lives removal", "Slack (#builds)", tools("slack_search_public_and_private", "slack_read_channel"),
     "the Android EconomyChanges build lines in #builds, Dec 9 and 10", dep("wc") + ' (the branch name); search "EconomyChanges"',
     f"C05433XK267/1765310444.095399, {when(ts_iso('1765310444.095399'))}: " + must(B2297, "DD Android - #2297 - EconomyChanges - (?MB) Still Failing after 15 min", "Fix for EndLevelPopup flickering on Tap Anywhere clicked [Arthur Blake]", "Nathan Animation Fix [Arthur Blake]", "Updated URLAudioPlayer to fully download clip if needed [Arthur Blake]")
     + f"; C05433XK267/1765397569.397939, {when(ts_iso('1765397569.397939'))}: " + must(B2299, "DD Android - #2299 - EconomyChanges - (220MB) Success", "Removed life pop-up from end screen"),
     "VERIFIED: quotes cut from the bot attachments read through hg.py; #2297 failed, so its changes list shows what is on the branch, and #2299 on the same branch succeeded", SY, dep("wc"), f"{bsrc('C05433XK267/1765310444.095399')}, {bsrc('C05433XK267/1765397569.397939')}")
TRC = json.dumps(SLK["C050WGU41HR/1764694580.083459"]["rec"]["attachments"], ensure_ascii=False)
fact("treasure_commit", "The treasure button fix commit on develop (Dec 2)", "Slack (#engineering-bots)", tools("slack_search_public_and_private"), "the GitHub push notice in #engineering-bots",
     dep("posts") + '; search "Treasure button"',
     f"C050WGU41HR/1764694580.083459, {when(ts_iso('1764694580.083459'))}: " + must(TRC, "1 new commit pushed to _develop_ by brian.foster", "fbe7bdea", "Fix issue opening Axe Arena panel from Nate Treasure button")
     + "; earlier than Owen's Dec 2 4:29pm PST post starting the EconomyChanges branch (F-row for the group DM)",
     "VERIFIED: quotes cut from the bot attachment; persona_view search 'Treasure button' has 2 hits", SY, dep("posts"), bsrc("C050WGU41HR/1764694580.083459"))
BR3, OUT17 = "C9CA62B5180A/1764721779.638599", "C9CA62B5180A/1765933143.608699"
fact("econ_branch", "Owen started the EconomyChanges branch (Dec 2); Leonard's notes say lives are out (Dec 16)", "Slack (group DM)", tools("slack_read_channel"), "the group DM with Leonard, Brian and Arthur, December", dep("lives") + " (a hit of the lives search)",
     f"{BR3}, Owen, {when(ts_iso('1764721779.638599'))}: " + must(bt(BR3), "I suggest we all work on a feature branch", "Working branch is `EconomyChanges`")
     + f"; {OUT17}, Leonard Hayes, {when(ts_iso('1765933143.608699'))}: " + must(bt(OUT17), "Lives are out, now you can enter using", "the lives counter is removed"),
     "VERIFIED: quotes cut from the base messages; users EMPLOYEE_0021 Owen and EMPLOYEE_0038 Leonard Hayes", SY, dep("lives"), f"{bsrc(BR3)}, {bsrc(OUT17)}")

CMG = OB["commit_merge"]
fact("merge", "develop merged into EconomyChanges (Dec 17)", "GitHub", tools("github_search_commits", "github_get_commit"), "the merge commit on EconomyChanges", dep("econ_branch") + ' (the branch name); search "into EconomyChanges"',
     f"commit {CMG['sha']} by {CMG['author_name']}, authored {when(CMG['authored_date'])}: " + must(CMG["message"], "Merge remote-tracking branch 'origin/develop' into EconomyChanges"),
     "VERIFIED: sha, author and message read through hg.py github data.json /commits/252", UNSC, dep("econ_branch"), "github data.json /commits/252")
MUS = "D07E9PSQB6W/1765206644.602119"
fact("music", "Brian: music and the acid throw are sorted (Dec 8)", "Slack (Owen's DM with Brian)", tools("slack_read_channel", "slack_search_public_and_private"), "Brian Foster's DM to Owen, Dec 8",
     dep("posts") + '; search "music plays normally"',
     f"{MUS}, Brian Foster, {when(SM[MUS]['created_at'])}: " + must(st(MUS), "music plays normally on my side since your audio player change", "Nate's acid throw lines up again after my animation fix", "Robert's two are sorted"),
     "VERIFIED: quotes cut from the seeded message", SY, dep("posts"), f"{MUS}, {L(MUS)}")

BAR = "C05V5FNLB9V/1767021345.207719"
fact("bar", "Brian closed the bottom bar thread (Dec 29)", "Slack (#god-bugs)", tools("slack_read_thread"), "the last reply in the bottom bar thread", dep("posts"),
     f"{BAR}, Brian Foster, {when(SM[BAR]['created_at'])}, reply 61 under {BAR2}: " + must(st(BAR), "the bottom bar and the top panel both show on the devices I have here, closing this one"),
     "VERIFIED: quote cut from the seeded reply", SY, dep("posts"), f"{BAR}, {L(BAR)}")

p16 = OB["github"]["harmonygames-Games/GameOfDominoes#1916"]["rec"]
c16 = rows("github.github_pr_comments", id="harmonygames-Games/GameOfDominoes#1916#c_2")[0]
fact("pr1916", "The camera PR merged into EconomyChanges (Dec 26)", "GitHub", tools("github_search_pull_requests", "github_get_pull_request", "github_get_pull_request_comments"), "the PR 'New core game camera config'",
     dep("bar") + ' ("the new camera setup fixed it"); search "camera"',
     f"harmonygames-Games/GameOfDominoes#1916 '{p16['title']}', base {p16['base_ref']}, head {p16['head_ref']}, merged {when(p16['merged_at'])}; comment harmonygames-Games/GameOfDominoes#1916#c_2 by Arthur Blake, {when(c16['created_at'])}: "
     + must(clean(c16["body"]), "Same here, into EconomyChanges for the next BoomBit drop."),
     "VERIFIED: PR fields read through hg.py; comment quote cut from the SQL row", UNSC, dep("bar"), f"harmonygames-Games/GameOfDominoes#1916 (github data.json {OB['github']['harmonygames-Games/GameOfDominoes#1916']['pointer']}), {L('harmonygames-Games/GameOfDominoes#1916#c_2')}")
fact("treasure", "Brian sent the treasure button fix", "Slack (#god-bugs)", tools("slack_read_thread"), "the thread under the treasure button post", dep("posts"),
     f"C05V5FNLB9V/1764694606.476379, {when(ts_iso('1764694606.476379'))}: " + must(bt("C05V5FNLB9V/1764694606.476379"), "I send the fix") + "; then `Thanks` (C05V5FNLB9V/1764694629.652379), the last reply",
     "VERIFIED: quotes cut from the replies read through hg.py", SY, dep("posts"), bsrc("C05V5FNLB9V/1764694606.476379"))

MEGA = "C05V5FNLB9V/1764331830.705279"
fact("mega", "The mega tile bug is still there (Nov 28)", "Slack (#god-bugs)", tools("slack_read_thread"), "the thread under the mega tile post", dep("posts"),
     f"{MEGA}, Marcus Bennett, {when(SM[MEGA]['created_at'])}: " + must(st(MEGA), "still happens on today's build") + "; the last reply in the thread",
     "VERIFIED: quote cut from the seeded reply", SY, dep("posts"), f"{MEGA}, {L(MEGA)}")

POP = "D07E9PSQB6W/1765471563.704419"
rc = {n: rows("github.github_review_comments", id=f"harmonygames-Games/GameOfDominoes#{n}#rc_1")[0] for n in (1905, 1908)}
for n, k, q in ((1905, "td", "the Tile Dozer how-to-play popup still points at the old sprites"), (1908, "axe", "the Axe Arena info popup keeps the old frame")):
    p = OB["github"][f"harmonygames-Games/GameOfDominoes#{n}"]["rec"]
    fact(f"inline_{k}", f"Arthur's inline review on #{n}: a popup never got swapped", "GitHub", tools("github_get_pull_request_comments", "github_get_pull_request_reviews"),
         f"the review comment on the PR '{p['title'].split(': ', 1)[1]}'", dep("rules") + ' ("a piece of its UI work never made it")',
         f"harmonygames-Games/GameOfDominoes#{n} '{p['title']}', merged {p['merged_at']}; review comment harmonygames-Games/GameOfDominoes#{n}#rc_1 by Arthur Blake, created {when(rc[n]['created_at'])}: " + must(clean(rc[n]["body"]), q),
         "VERIFIED: quote cut from the review comment; PR title and merge time read through hg.py", UNSC, dep("rules"), f"harmonygames-Games/GameOfDominoes#{n}#rc_1, {L(f'harmonygames-Games/GameOfDominoes#{n}#rc_1')}")
fact("popups_dm", "Brian: the two popups never got their pass (Dec 11)", "Slack (Owen's DM with Brian)", tools("slack_read_channel"), "Brian Foster's DM to Owen, Dec 11", dep("music") + " (the same DM)",
     f"{POP}, Brian Foster, {when(SM[POP]['created_at'])}: " + must(st(POP), "the Axe Arena info popup still has the old frame", "the Tile Dozer how-to-play popup still points at the old sprites"),
     "VERIFIED: quotes cut from the seeded message (a second record for the two holds above)", SY, dep("music"), f"{POP}, {L(POP)}")

sea = rows("linear.linear_comments", issue_id="ENG-2428")[0]
fact("season", "Oliver: the Season Pass reward track still uses the old frames", "Linear", tools("linear_list_comments"), "Oliver's comment on the Season Pass child", dep("rules") + ' ("Brian and Oliver left notes on some of the open children")',
     f"ENG-2428 comment {sea['id']} by Oliver Brooks, created {when(sea['created_at'])}: " + must(clean(sea["body"]), "the reward track still uses the old frames, this isn't finished"),
     "VERIFIED: quote cut from the comment", UNSC, dep("rules"), f"ENG-2428, {L(sea['id'])}")

NOV19 = "D07E9PSQB6W/1763585860.227679"
fact("brian_nov19", "Brian's Nov 19 plan for Daily Gift (superseded by his Dec 11 line)", "Slack (Owen's DM with Brian)", tools("slack_read_channel"), "Brian Foster's DM to Owen, Nov 19", dep("music") + " (the same DM)",
     f"{NOV19}, Brian Foster, {when(ts_iso('1763585860.227679'))}: " + must(bt(NOV19), "I just need to go over the Daily Gift one more time. I’ll finish that tomorrow morning, so it’ll be done before the meeting."),
     "VERIFIED: quote cut from the base message", SY, dep("music"), bsrc(NOV19))
CHK = {k: rows("linear.linear_comments", issue_id=k)[0] for k in ("ENG-2410", "ENG-2429", "ENG-2430")}
fact("checks", "Brian's check notes on three open children (no hold)", "Linear", tools("linear_list_comments"), "the comments on the Shop, Remove Ad and Offers children", dep("rules"),
     "; ".join(f"{k} comment {c['id']} by Brian Foster, created {when(c['created_at'])}: " + must(clean(c["body"]), clean(c["body"])) for k, c in CHK.items())
     + ". With Oliver's ENG-2428 note these are the only comments on any of the 28 children (none in the base; four in the SQL)",
     "VERIFIED: quotes cut from the comments; ABSENCE evidence_check: hg.py lookup linear data.json /comments key issue_id over ENG-2409 to ENG-2437 found 0 base comments (scan complete), and the SQL holds exactly these four on children", UNSC, dep("rules"),
     ", ".join(L(c["id"]) for c in CHK.values()))
GIFT = "D07E9PSQB6W/1765471651.208713"
fact("gift", "Brian: Daily Gift never got its last pass (Dec 11)", "Slack (Owen's DM with Brian)", tools("slack_read_channel"), "Brian Foster's DM to Owen, Dec 11", dep("music") + " (the same DM)",
     f"{GIFT}, Brian Foster, {when(SM[GIFT]['created_at'])}: " + must(st(GIFT), "Daily Gift isn't finished either, the panel never got its last pass."),
     "VERIFIED: quote cut from the seeded message", SY, dep("music"), f"{GIFT}, {L(GIFT)}")

# ---------------------------------------------------------------- the decoys the run meets first
dk = " ".join(clean(r.get("text") or "") for r in rows("gslides.slides_page_elements"))
fact("deck", "Superseded: Brian's wrap deck says the pass wrapped up", "Google Slides (Drive)", tools("gslides_get_presentation_text"), "the deck 'UI optimization wrap'", 'search "UI optimization wrap"',
     "f_d15a8c70e3f2b94a61c8d3, created " + when(rows("gdrive.drive_files", id="f_d15a8c70e3f2b94a61c8d3")[0]["created_time"]) + ": " + must(dk, "UI pass wrapped up."),
     "VERIFIED: quote cut from a slide text element; overturned by F-rows for ENG-2426, ENG-2428, ENG-2434, ENG-2437", SY, "—", f"f_d15a8c70e3f2b94a61c8d3, {L('f_d15a8c70e3f2b94a61c8d3')}")
chk = rows("trello.trello_check_items")
fact("checklist", "Superseded: the card's screen checklist", "Trello", tools("trello_get_checklist"), "the checklist on the card 'UI optimization pass'", dep("closing") + " (the same card)",
     f"28 items: {sum(1 for c in chk if c['state'] == 'complete')} complete, {sum(1 for c in chk if c['state'] != 'complete')} incomplete (Daily Gift); Axe Arena, Tile Dozer and Season Pass are ticked complete",
     "VERIFIED: counted from the 28 check_items rows; overturned by the review comments and Oliver's note", UNSC, dep("closing"), f"690b27285bfa8e197220e1d5, {L('690b27285bfa8e197220e1d5')}")
assert len(chk) == 28
zm = rows("gdocs.docs_documents", document_id="f_72e0b4c3d91a5f68c2b7e4")[0]
zc = json.loads(rows("trello.trello_actions", id="68d284b84b7e9a3c5d16e208")[0]["data_json"])["text"]
fact("zm", "Lookalikes for another game: the Zombie Match notes and close-out card", "Google Docs + Trello", tools("gdocs_get_document_text", "trello_get_card_actions"),
     "the Doc 'Zombie Match bug list notes' and the card 'ZM bug list close-outs'", 'search "bug list notes"',
     "f_72e0b4c3d91a5f68c2b7e4: " + must(clean(zm["body_text"]), "ZM bugs go on the ZOM team.") + "; 68d284b84b7e9a3c5d16e208: " + must(zc, "ZM close-outs just need the ticket state, no note."),
     "VERIFIED: quotes cut from the doc and the comment; both are about Zombie Match, not DD", SY, "—", f"f_72e0b4c3d91a5f68c2b7e4, {L('f_72e0b4c3d91a5f68c2b7e4')}, 68d284b84b7e9a3c5d16e208")

# ---------------------------------------------------------------- one fact per bug
STATE = {"Fixed": "Done", "Gone": "Canceled", "Broken": "Bugs"}
DECIDE = {"Tavern buttons lost its frame": ("tavern", "near_miss"), "shops from rivertile and memory tile has weird shop": ("shop", "near_miss"), "train level backgrounds are broken": ("vr_train", "near_miss"),
          "When I created a team and quitted it the": ("vr_team", "near_miss"), "When I lost a level I got some backend": ("near_miss",), "I found the issue lives are not decreased after": ("vr_lives1", "lives", "econ_builds", "econ_branch"),
          "Lives are only decreased after losing twice in a": ("vr_lives2", "lives", "econ_builds", "econ_branch"), "When I change the character it just adds 1": ("lives", "econ_builds", "econ_branch"),
          "In general I cannot sync and sign in with": ("apple", "eng2073"), "On android manual sign-in has an issue after the": ("signin",),
          "navigation bar tooltips": ("tooltips",), "tile dozer window background": ("window_claim", "pr1913", "near_miss"), "mega tile missing a face": ("mega", "near_miss"),
          "flickering": ("flicker", "econ_builds"), "music plays only sometimes": ("music", "econ_builds"), "acid animation delay": ("music", "econ_builds"), "treasure button opens axe arena": ("treasure", "treasure_commit", "econ_branch", "merge"),
          "android bottom bar invisible": ("bar", "pr1916")}
bug_facts, n_new = [], 0
for i, b in enumerate(COH["bugs"], 1):
    k, t = b["key"], TRUTH[b["key"]]
    rid = b["id"] if b["id"] != BAR2 else BAR1
    text = bt(rid)
    if b["kind"] == "canvas_line":
        assert re.sub(r"<@\w+>|@\w+ \w+", "@", text) == re.sub(r"<@\w+>|@\w+ \w+", "@", b["line"]), k   # mentions render either way
        box = "ticked" if text.startswith("☑") else "unticked"
        title = text[1:].strip() if text[:1] in "☑☐" else text
        where = f"canvas line {i}, {box}"
        dk_ = ("canvas",)
    else:
        box = "a post"
        title = text.split("\n")[0].strip()
        where = f"bug post {i - 63} of 7"
        dk_ = ("posts",)
    deciders = DECIDE.get(k, ())
    out = t["Outcome"]
    if out == "Covered":
        write = f"no new ticket; a note with the canvas wording on {t['Ticket']}"
    else:
        write = f"new ticket in state {STATE[out]}, title `[2231] {safe(title)}`"
        n_new += 1
    why = t["Why"]
    fact(f"bug:{k}", f"Bug {i}: {where} → {out}", "Slack (" + ("canvas comment channel" if b["kind"] == "canvas_line" else "#god-bugs") + ")",
         tools("slack_read_channel", "slack_read_thread"), "the line's root comment and its thread" if b["kind"] == "canvas_line" else "the post and its thread", dep(*dk_),
         f"{rid}, posted {when(ts_iso(rid.split('/')[1]))}. Text: " + must(text, text.strip() if b['kind'] == 'canvas_line' else title) + f". Outcome {out} ({safe(why)}" + (f"; deciding record {dep(*deciders)}" if deciders else "") + f"): {write}",
         "VERIFIED: text read from the root through hg.py; outcome not_a_claim (derived under the rule doc's first-fit order" + (f" from {dep(*deciders)})" if deciders else ": the tick or the open line stands, no later record about it)"),
         SY, dep(*(dk_ + ("rules",) + deciders)), bsrc(rid))
    bug_facts.append(fid_of[f"bug:{k}"])
assert n_new == 68

# ---------------------------------------------------------------- one fact per UI child
HOLD = {"ENG-2424": ("wc",), "ENG-2426": ("inline_axe", "popups_dm"), "ENG-2428": ("season",), "ENG-2434": ("inline_td", "popups_dm"), "ENG-2437": ("gift",)}
GROUP = {"ENG-2403": "Core", "ENG-2404": "Live-Ops", "ENG-2405": "Mini-Games"}
kid_facts = []
for c in COH["children"]:
    k = c["key"]
    r = OB["linear"][k]["rec"]
    t = TRUTH[k]
    if c["already_done"]:
        end = "already Done: stays Done; gets a line naming 0.3.310"
        assert r["state_id"] == "Done"
    elif k in HOLD:
        end = f"stays {r['state_id']} (held by {dep(*HOLD[k])}); gets a line naming 0.3.310 and why it stays"
        assert t["Outcome"] == "Held"
    else:
        end = f"moves {r['state_id']} → Done; gets a line naming 0.3.310"
        assert t["Outcome"] == "Done"
    fact(f"kid:{k}", f"UI child {k} ({r['title']}) → {'Held' if k in HOLD else 'Done'}", "Linear", tools("linear_list_issues", "linear_get_issue", "linear_list_comments"),
         f"child of the {GROUP[r['parent_id']]} group under the master ticket", 'prompt ("a line on every UI child"; "the tree under the UI Changes master ticket")',
         f"{k} '{r['title']}', parent {r['parent_id']} ({GROUP[r['parent_id']]}), state {r['state_id']}, updated {when(r['updated_at'])}: {end}",
         "VERIFIED: title, parent and state read through hg.py (no SQL row changes a state); end state not_a_claim (derived under the tree rule)", UNSC,
         dep(*(("rules", "closing") + HOLD.get(k, ()))), f"{k} (linear data.json {OB['linear'][k]['pointer']})")
    kid_facts.append(fid_of[f"kid:{k}"])
assert len(kid_facts) == 28
masters = {k: OB["linear"][k]["rec"]["state_id"] for k in ("ENG-2401", "ENG-2403", "ENG-2404", "ENG-2405")}
fact("tree", "The UI tree: 3 groups, 28 children; 9 Done, 19 open", "Linear", tools("linear_list_issues"), "the master ticket's tree", 'prompt ("the tree under the UI Changes master ticket")',
     "Masters: " + ", ".join(f"{k} {v}" for k, v in masters.items()) + ". Children: ENG-2409 to ENG-2437 except ENG-2436 (28). Done 9: ENG-2409, ENG-2411, ENG-2412, ENG-2413, ENG-2416, ENG-2420, ENG-2421, ENG-2422, ENG-2423; the other 19 in PR, Validation or In Progress",
     "VERIFIED: parent and state read on all 28 children and the 4 masters through hg.py", UNSC, dep("amend"), "ENG-2401, ENG-2403, ENG-2404, ENG-2405 (linear data.json)")

# ---------------------------------------------------------------- derived counts
cnt = {o: sum(1 for b in COH["bugs"] if TRUTH[b["key"]]["Outcome"] == o) for o in ("Fixed", "Broken", "Gone", "Covered")}
assert cnt == {"Fixed": 58, "Broken": 7, "Gone": 3, "Covered": 2}
fact("totals", "The three numbers Arthur asked for and the sheet's tally", "derived (Slack, Linear, Gmail, GitHub)", "none (calculation over the rows)", "the 70 bug rows and 28 child rows above",
     dep("rules", "canvas", "posts", "tree"),
     "Sheet rows 70: Fixed 58, Broken 7, Gone 3, Covered 2. New tickets 68 (58 Done + 7 Bugs + 3 Canceled; the 2 Covered lines get notes, not tickets). Still broken 9 (7 Broken + 2 Covered, per the rule doc's report-back line). UI children Done 23 of 28 (9 already Done + 14 moved; ENG-2424, ENG-2426, ENG-2428, ENG-2434, ENG-2437 stay)",
     "not_a_claim (derived): 58 + 7 + 3 + 2 = 70; 58 + 7 + 3 = 68; 7 + 2 = 9; 9 + 14 = 23", "derived", ", ".join(bug_facts[:1] + kid_facts[:1]) + " … (all bug and child rows)",
     f"solver/truth.json, {HUB}")
FACTS[-1][9] = dep("rules", "canvas", "posts", "tree")


# ---------------------------------------------------------------- requirements
def span(s):
    assert s in PROMPT, s
    return s


ALLB, ALLK = f"{bug_facts[0]} to {bug_facts[-1]}", f"{kid_facts[0]} to {kid_facts[-1]}"
REQ = [
    (span("Arthur sent me a DM on Thursday about getting DD's bug list out of Slack and into Linear before Slack drops to the free plan"), "Discovery — Arthur's Thursday DM is the source of every ask", "Explicit", F("hub")),
    (span("Can you take care of everything he asked for, the way he lays it out?"), "Discovery — the DM's incorporated records: the carry-over notes, the master ticket's change, Brian's closing rule, the folder, the review", "Implicit (through F1)",
     F("hub", "rules", "amend", "closing", "folder", "review")),
    (span("getting DD's bug list out of Slack and into Linear"), "Discovery — the population: 63 canvas lines and 7 later bug posts, each decided under the first-fit order with its later records",
     "Explicit (population and rules through F2)", F("canvas", "posts", "lives", "wc", "pr1913", "window_claim", "shop", "tavern", "vr_train", "vr_team", "vr_lives1", "vr_lives2", "tooltips", "apple", "eng2073", "signin", "flicker", "econ_builds", "econ_branch", "treasure_commit", "merge", "pr1916", "near_miss", "music", "bar", "treasure", "mega") + ", " + ALLB),
    (span("That covers the Linear tickets"), "Write — 68 new tickets (team, label, parent, [2231] title, state per outcome) and a note on each of the 2 reused tickets", "Explicit (fields through F2 and F3)", F("rules", "amend", "eng2073", "signin") + ", " + ALLB),
    (span("bringing the tree under the UI Changes master ticket up to date"), "Write — 14 open children move to Done; 5 stay; 9 already Done stay", "Explicit (rule through F2)",
     F("tree", "wc", "inline_axe", "inline_td", "popups_dm", "season", "gift", "deck", "checklist") + ", " + ALLK),
    (span("a line on every UI child"), "Write — a line on each of the 28 children saying where it landed and naming the public build 0.3.310", "Explicit (build through F4 and F2)", F("closing", "rules") + ", " + ALLK),
    (span("the sheet in my DD bug carry-over folder"), "Write — a sheet in the folder with columns Bug, Outcome, Ticket, Why and one row per bug (70)", "Explicit (columns through F2)", F("folder", "rules", "totals") + ", " + ALLB),
    (span("shared with everyone on the review"), "Write — share the sheet with Arthur, Robert and Oliver", "Explicit", F("review", "emails")),
    (span("Then reply to him in that DM thread with the numbers he wanted."), "Write and Tell — a thread reply under Arthur's DM: 9 still broken, 68 new tickets, 23 of 28 children Done", "Explicit (numbers through F1)", F("hub", "totals")),
    (span("I want it all finished before Sunday's bug review."), "Constraint — every write is done now, before the review of Sun Feb 15", "Explicit", F("review")),
]

# ---------------------------------------------------------------- write capability and the defer search
late = []
for k, v in DEF.items():
    if k == "sql":
        continue
    for h in v.get("feb_2026", []):
        late.append((k, h["file"], h["pointer"], (h["text"] or "")[:80]))
for k, v in DEF.items():
    if k != "sql":
        assert v["complete"] in (True, None) or v["complete"], k
        assert not v["hit_limit"], k


def dcount(pfx):
    return sum(v["visible"] for k, v in DEF.items() if k.startswith(pfx))


DEFER = ("slack · gmail · linear · trello (Owen's channels, DMs and mailbox through persona_view search; all of Linear and Trello through hg.py search; the seeded SQL rows by text): "
         "'hold off', 'not yet', 'don't move', 'wait for', 'wait until', 'on hold', 'don't close', 'leave it open', 'don't file', 'keep it open', 'before you close' (limit 3000, no search hit its limit) — population complete: "
         f"slack {dcount('slack:')} hits, gmail {dcount('gmail:')}, linear {dcount('linear:')}, trello {dcount('trello:')}, SQL {sum(DEF['sql'].values())}; "
         f"{len(late)} hits dated Feb 12 to 13 2026 (each read, Self-review); governing version: Arthur's DM {HUB} (Feb 12 23:10Z) and the master-ticket change (Feb 13 00:40Z) are the latest instructions and neither holds a write; result: no defer")
WR = [
    ("R4", "Create one ticket per bug that is not Covered (68)", '"That covers the Linear tickets"', tools("linear_create_issue") + " (exists)", "team, title (+ labels, parentId, state)", ALLB,
     "68 issues under ENG-2401 in team Engineering with label Bug, no assignee, no description; 58 Done, 7 Bugs, 3 Canceled (new issues: state_history_json an empty array at load)", "title `[2231] ` + the line without its box, or the post's first line"),
    ("R4", "Add the canvas wording on each reused ticket (2)", '"That covers the Linear tickets"', tools("linear_create_comment") + " (exists)", "issueId, body", F("eng2073", "signin"),
     "one comment on ENG-2073 and one on ENG-2363", "the canvas line's wording"),
    ("R5", "Move each open child that has no hold to Done (14)", '"bringing the tree under the UI Changes master ticket up to date"', tools("linear_update_issue") + " (exists)", "id, state", ALLK,
     "ENG-2410, ENG-2414, ENG-2415, ENG-2417, ENG-2418, ENG-2419, ENG-2425, ENG-2427, ENG-2429, ENG-2430, ENG-2431, ENG-2432, ENG-2433, ENG-2435 in state Done", "state only"),
    ("R6", "Leave a line on every child (28)", '"a line on every UI child"', tools("linear_create_comment") + " (exists)", "issueId, body", ALLK, "one comment on each of the 28 children", "where it landed and the public build 0.3.310"),
    ("R7", "Create the sheet in the folder and write its rows", '"the sheet in my DD bug carry-over folder"', tools("gsheets_create_spreadsheet", "gsheets_values_update", "gdrive_move_file") + " (exist)",
     "title; spreadsheetId, range, values; fileId, newParentId", F("folder", "totals"), f"a native sheet whose parent is {FOLDER}, header + 70 rows", "columns Bug, Outcome, Ticket, Why"),
    ("R8", "Share the sheet with the three reviewers (3)", '"shared with everyone on the review"', tools("gdrive_share_file") + " (exists)", "fileId, emailAddress, role", F("emails"), "each address holds a permission on the sheet", "—"),
    ("R9", "Reply to Arthur in the DM thread", '"Then reply to him in that DM thread"', tools("slack_send_message") + " (exists)", "channel, text, thread_ts", F("hub", "totals"),
     f"posted under {HUB} (thread_ts 1770937805.214409), after the other writes", "how many are still broken (9), how many new tickets (68), how many of the 28 children are Done (23)"),
]

TRAPS = [
    ("T1", "The Tavern line is ticked and Brian sent the fix in its thread (CE156FDFB428/1763642831.967359)", F("tavern"), f"Marcus's DM {TAV}, Dec 11, later than the tick (Nov 20)"),
    ("T2", "The shop icons line is ticked (CE156FDFB428/1763549455.195819)", F("shop"), f"Brian's reply {SHOP}, Dec 1, under an unrelated gems post"),
    ("T3", "The Apple sync line is unticked and no ticket title uses its words (CE156FDFB428/1763041538.186339)", F("apple", "eng2073"), f"Vincent's mail {MAIL}, Nov 20, names ENG-2073"),
    ("T4", "The manual sign-in line, unticked (CE156FDFB428/1763132009.017599)", F("signin"), "Vincent's comment on ENG-2363, Nov 20: 'same thing as here'"),
    ("T5", "Marcus 'fixed it and did a PR' on the window post (C05V5FNLB9V/1764329192.159229)", F("pr1913"), "harmonygames-Games/GameOfDominoes#1913 is open, base develop"),
    ("T6", "#1905 and #1908 merged, the checklist ticks Axe Arena and Tile Dozer, the deck says wrapped (f_d15a8c70e3f2b94a61c8d3)", F("inline_axe", "inline_td", "popups_dm"),
     "Arthur's review comments harmonygames-Games/GameOfDominoes#1905#rc_1 and #1908#rc_1; Brian's DM D07E9PSQB6W/1765471563.704419"),
    ("T7", "The deck and the checklist count Season Pass done (690b27285bfa8e197220e1d5)", F("season"), "Oliver's comment on ENG-2428, Dec 5"),
    ("T8", "Daily Gift reads as nearly done: Brian's Nov 19 DM D07E9PSQB6W/1763585860.227679 " + must(bt("D07E9PSQB6W/1763585860.227679"), "I just need to go over the Daily Gift one more time", "it’ll be done before the meeting"), F("gift"), f"Brian's DM {GIFT}, Dec 11, later"),
    ("T9", "ENG-2424 (Collect&win) sits in PR and the checklist ticks Collect & Win complete (690b27285bfa8e197220e1d5)", F("wc"), "C9CA62B5180A/1765927876.696389, Dec 16: 'event disabled', pushed to EconomyChanges"),
    ("T10", "The three lives lines read as open bugs (CE156FDFB428/1763548856.943389)", F("lives"), "C09SWTHEMEW/1764659626.614679: lives removed; the doc's Gone outcome comes before Broken"),
    ("T11", "The train line's thread has Arthur's CE156FDFB428/1763671462.192489 " + must(SLK["CE156FDFB428/1763671462.192489"]["rec"]["text"], "fixed") + " (Nov 20); the team line's fix covered the leave-team popup", F("vr_train", "vr_team"), "Vincent's later replies CE156FDFB428/1763845212.507119 (Nov 22) and CE156FDFB428/1763742012.611229 (Nov 21): still off, the navigation bar still goes"),
    ("T12", "The ZM notes doc and ZM card say no note is needed (68d284b84b7e9a3c5d16e208)", F("closing"), "they are about Zombie Match; Brian's DD rule 690b29bc3c7d2e51b0f86a47 asks for the build"),
    ("T13", "Six empty canvas roots and the chatter, follow-ups, QA-doc pointer and design question in the bug channel (C05V5FNLB9V/1767191512.428539)", F("canvas", "posts"), f"the rule doc's scope sentences ({DOC})"),
]
RISKS = [
    ("1", "Title rendering of Slack mentions and emoji codes (e.g. the Tavern line's mention, ':warning:') varies by tool; brief 4b accepts either rendering", ALLB, "rubric / OE accuracy", "grade the [2231] prefix and the wording, not one rendering"),
    ("2", "The sheet may be created in the folder directly (gdrive_create_file with a parent) or created then moved; both end with the folder as parent", F("folder"), "OE accuracy", "name the end state, not one route"),
    ("3", "Share role is free (reader, commenter or writer); /prompt asked to accept any role", F("emails"), "rubric", "accept any role"),
    ("4", "The reply may go in the thread or as a new message in the same DM; /prompt accepted both", F("hub"), "rubric", "accept either"),
    ("5", "Covered counts as still broken (9); a run may also give the 7 + 2 split", F("totals"), "rubric", "accept 9 with or without the split"),
    ("6", "The bottom bar bug's title is the first line of its first post (C05V5FNLB9V/1766415211.386389), not of the message that holds the thread", fid_of["bug:android bottom bar invisible"], "rubric", "accept the first line of the first post"),
    ("7", "Owen left the canvas channel and three others on Feb 11 and rejoined on Feb 12 (SQL); every read above is at the clock, after the rejoin", F("canvas", "posts"), "feasibility (settled)", "none"),
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
A("# 08 OE Writing Ledger — owen_dd_bug_carryover (DD bug list into Linear and the UI tree close-out, injection rev9)")
A(f"Generated 2026-11-08 · Clock {clock} · seed bound {freeze} · Persona Owen Baker owen.baker@harmonygames.co (Game Engineer (Unity)) · Tier Long-Horizon · Mode Medium")
A(f"Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all {len(WR)} write families map to cataloged tools, friction is none")
A(f"Inputs read: 04_Prompt.txt — present (sha256 {sha(os.path.join(TI, '04_Prompt.txt'))}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present (rev9, sha256 {sha(SQL_PATH)}) · 01_Grounding_Dossier.md — present (leads only) · 01_Scenario_Design.md + 01_Hardness_Manifest.json — present (leads only) · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files — none · 04_Prompt_Writing_Brief.md — present (§4b for SQL ea5b542897c8)")
A("")
A("Persona binding: roster entry owen_baker, Owen Baker, Game Engineer (Unity), owen.baker@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of the canvas comment channel 'Bugs on Android 2231', #god-bugs, #dd-road-to-sub-250mb, #builds and the shared publishing channel after the Feb 12 rejoin, the group DM with Leonard, Brian and Arthur, and his DMs with Arthur, Marcus and Brian), Calendar (own calendar), Drive, Docs, Sheets and Slides (files shared with him and his own folders). Unscoped: Linear, Trello, GitHub, Contacts.")
A("")
A("Dates: Pacific first, UTC beside it. 'sent', 'created', 'posted', 'merged' and 'updated' mark record times; every record time below is at or before the seed bound. Semantic future date: Sunday's bug review (starts Sun Feb 15 2026 9:00am PST, 17:00Z) — not expected as done.")
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
nn = sum(1 for f in FACTS if "not_a_claim" in f[7] and "VERIFIED" not in f[7])
na = sum(1 for f in FACTS if "ABSENCE" in f[7])
A(f"Requirements {len(REQ)} · facts {len(FACTS)} · writes {len(WR)} (feasible {len(WR)}) · friction items 0 · expected values {len(FACTS)} (quoted {nq} · not_a_claim {nn} · ABSENCE-checked {na}) · unverified visibility 0 · blocking 0")
A("")
A("## Self-review")
A("")
A("Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every §B value was re-verified in this run: seeded values from the parsed SQL rows, base values through tools/hg.py (plan/oe_reads.py: the canvas channel's month file and the bug channel's Nov, Dec and Feb files read whole, 10 more Slack posts by lookup + get-many, 34 Linear issues field by field, 3 pull requests, 3 contacts, the economy doc), with each quote asserted as a substring of its record by plan/assemble_oe_ledger.py. The per-bug outcomes are derived, not quoted: each is the rule doc's first fitting outcome given the line's box and the deciding rows it cites, and solver/truth.json reproduces all 70. The no-event-text scan passes: §B holds facts and dependency edges, no event wording.")
A("")
A("Defer search, hits dated Feb 12 to 13 2026 read one by one: " + ("; ".join(f"{k}: {p}, '{t}' (not a hold on any write this task makes)" for k, f, p, t in late) if late else "none") + ".")
A("")
A("| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |")
A("|---|---|---|---|")
CRS = [
    ("R1", "'on Thursday' could mean another Arthur DM, or Thursday in UTC", f"the DM {HUB} is Feb 12 23:10Z = Thu Feb 12 3:10pm PST and is about moving DD's bug list into Linear ({fid_of['hub']})", "holds"),
    ("R2", "'the way he lays it out' could stop at the DM's own words", f"the DM hands the calls to the carry-over notes ({fid_of['rules']}), which point at the master ticket and Brian's rule ({fid_of['amend']}, {fid_of['closing']})", "holds"),
    ("R3", "the population could include the 6 empty canvas roots, Robert's sub-250 reports or the bug channel's chatter", f"the notes: 'A comment whose line was deleted has nothing to carry over', 'Robert's reports in the sub-250 channel aren't part of this', and the bug-post tests ({fid_of['canvas']}, {fid_of['posts']})", "holds (70)"),
    ("R4", "the two tied lines could get their own tickets, and titles could drop the prefix", f"Covered: 'Don't file a new one, add a note on that ticket' ({fid_of['rules']}); the master-ticket change ({fid_of['amend']})", "holds (68 + 2 notes)"),
    ("R5", "every open child could go Done because its PR merged and the checklist ticks it", f"the tree rule: a piece of UI work that never made the build, or a switched-off screen, holds the child ({fid_of['inline_axe']}, {fid_of['inline_td']}, {fid_of['season']}, {fid_of['gift']}, {fid_of['wc']})", "holds (14 moved, 5 stay)"),
    ("R6", "the line could go only on the children that move, and need not name a build", f"the DM: 'a line on every child'; Brian's rule: 'every one gets a note naming the current public build' ({fid_of['closing']}); the ZM card's 'no note' is another game ({fid_of['zm']})", "holds (28 lines, 0.3.310)"),
    ("R7", "the sheet could live in Owen's root or carry the canvas only", f"the DM and prompt name the folder ({fid_of['folder']}); the notes give the columns and one row per bug ({fid_of['rules']})", "holds (70 rows in the folder)"),
    ("R8", "'everyone on the review' could include Owen or only Arthur", f"the event's attendees other than Owen ({fid_of['review']})", "holds (3)"),
    ("R9", "'still broken' could be the Bugs count (7)", f"the notes: 'When you report back, Covered ones count as still broken' ({fid_of['rules']})", "holds (9)"),
    ("R10", "'before Sunday's bug review' could be a deadline the agent waits for", f"the review starts Sun Feb 15 17:00Z ({fid_of['review']}), after the clock; nothing holds a write until then", "holds"),
]
assert len(CRS) == len(REQ)
for r in CRS:
    A("| " + " | ".join(r) + " |")
A("")
A("Unresolved: none blocking. Open risks §F 1 to 7 go to the draft and rubric stages (title rendering, the sheet's route into the folder, share role, reply placement, the still-broken split, the bottom bar title, the Feb 11 to 12 channel rejoin).")
A("")
open(os.path.join(WF, "08_OE_Writing_Ledger.md"), "w").write("\n".join(O) + "\n")
json.dump({"fid": fid_of, "seeded": seeded, "base": base}, open(os.path.join(HERE, "oe_ledger_ids.json"), "w"), indent=1)
print("facts", len(FACTS), "req", len(REQ), "seeded ids", len(seeded), "base ids", len(base), "yes rows", len(yes_rows), "late defer hits", len(late))
