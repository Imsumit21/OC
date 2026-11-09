#!/usr/bin/env python3
"""Draft 08_Oracle_Events.md (draft mode) for owen_dd_bug_carryover (rev9 SQL ea5b542897c8) from the OE ledger's facts.

Every quoted Expected value is re-read in this run: seeded rows are parsed from 01_Universe_Inject.sql (never executed), base records
come from plan/oe_base.json (plan/oe_reads.py, tools/hg.py). Each quote is asserted as a substring of its own record (whitespace-normalised)
before the file is written. One write per event; no final-response or non-action events."""
import datetime as dt
import json
import os
import re
import sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

PT = ZoneInfo("America/Los_Angeles")
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
COH = json.load(open(os.path.join(HERE, "cohort.json")))
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
SLK = {}
for f, recs in OB["slack_files"].items():
    for m in recs:
        SLK[f"{m['channel']}/{m['ts']}"] = m
for k, v in OB["slack"].items():
    SLK[k] = v["rec"]


def bt(k):
    return SLK[k]["text"]


def st(k):
    return clean(SM[k]["text"])


EV, N = [], {}


def short(t, n=70):
    if len(t) <= n:
        return t
    return t[:t.rfind(" ", 0, n)] + " …"


def ev(key, action, expected):
    EV.append((action, expected))
    N[key] = len(EV)


def n(*keys):
    return ", ".join(str(N[k]) for k in keys)


# ================================================================ discovery
HUB = "D05S1S2AB5M/1770937805.214409"
ev("hub", "Read Arthur's DM from Thursday in Slack (Owen's DM with Arthur Blake, his message of Thu Feb 12 2026)",
   f"Arthur, {pt(tsiso('1770937805.214409'))}, message ts 1770937805.214409: "
   + q(st(HUB), "I want the whole list moved over, the fixed ones too, that's the only record of what was done.", "How we call each one is in the carry-over notes doc I shared with you.",
       "While you're in there bring the UI Changes tree up to date, it never got closed out, and leave a line on every child saying where it landed.",
       "Put a sheet in your DD bug carry-over folder so I can look things up, and share it with everyone on Sunday's bug review.",
       "Then tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done."))

DOC = clean(rows("gdocs.docs_documents", document_id="f_3ca9e15d7b20f4e681ad52")[0]["body_text"])
ev("rules", "Find and read the carry-over notes doc in Drive (search \"carry-over notes\", named in OE «hub»; the Doc Arthur shared with Owen)",
   "Doc \"DD bug carry-over notes\", owner arthur.blake@harmonygames.co, created " + pt("2026-02-12T22:48:00Z") + ". Scope: "
   + q(DOC, "every ticked or unticked line in the comment channel of Vincent's Android canvas, and every bug posted in the bug channel after the last line in that comment channel.",
       "A comment whose line was deleted has nothing to carry over.", "In the bug channel a follow-up on a bug already posted is part of that bug, and a design question for Leonard or a post that points at a QA doc isn't a bug post.",
       "Robert's reports in the sub-250 channel aren't part of this")
   + " Outcomes: " + q(DOC, "Take the first outcome that fits.", "Fixed: the tick stands, or a later record says it was fixed. File it as Done.",
                     "Gone: it isn't fixed and it's a bug in something the build players have no longer has. File it as Canceled.",
                     "Covered: it isn't fixed and an open ticket already covers it. Don't file a new one, add a note on that ticket with the canvas wording.",
                     "Vincent tied a few lines to tickets before he left.", "Broken: anything else. File it as Bugs.")
   + " What counts: " + q(DOC, "we go by the Android build players have, 0.3.310, which came off the economy line, not by develop.", "A tick on the canvas stands unless a later record about that bug says otherwise.",
                         "An unticked line, or a bug nobody closed, stays open unless a later record says it was fixed, and a commit named for the bug counts as that record if nothing later says otherwise.", "A fix only counts once it is in that build.", "A PR that never made it into that build doesn't count.")
   + " New tickets: " + q(DOC, "Engineering team, Bug label, parent ENG-2401, title is the line without its tick box, or the first line of the post, as it was written, no assignee, nothing in the description.",
                         "If anything changes after this I'll put it on the master ticket.")
   + " UI tree: " + q(DOC, "every open child goes Done unless a record shows a piece of its UI work never made it into that build or the screen is switched off there. Then it stays where it is.",
                      "Children already Done stay Done and the masters stay as they are.", "A bug on a screen doesn't hold its child, that's what the bug ticket is for.", "Brian and Oliver left notes on some of the open children.",
                      "Brian's closing rule from the UI work applies to the line on every child, Done or not.")
   + " " + q(DOC, "Sheet columns: Bug, Outcome, Ticket, Why.", "When you report back, Covered ones count as still broken."))

am = rows("linear.linear_comments", issue_id="ENG-2401")[0]
ev("amend", "Read the comments on the UI Changes master ticket in Linear (ENG-2401 \"UI Changes Master Ticket\", named in the prompt; OE «rules» says changes go on it)",
   f"Arthur, {pt(am['created_at'])}: " + q(clean(am["body"]), "For the carry-over: put [2231] at the front of every title you file so I can filter them."))

card = rows("trello.trello_cards", id="690b27282f4c1b7a6e93d512")[0]
rtext = json.loads(rows("trello.trello_actions", id="690b29bc3c7d2e51b0f86a47")[0]["data_json"])["text"]
chk = rows("trello.trello_check_items")
ev("closing", "Find Brian's closing rule in Trello (search \"UI Changes\", the master's name from the prompt; the card \"UI optimization pass\" on the DD Product Roadmap board; read its comments and its checklist)",
   "Card description: " + q(clean(card["desc"]), "Tickets are under the UI Changes master.") + f" Brian Foster, {pt('2025-11-05T10:41:00Z')}: " + q(rtext, "When we close these UI tickets out every one gets a note naming the current public build, otherwise nobody can tell later what players actually had.")
   + f" The card's checklist has {len(chk)} screens, {sum(1 for c in chk if c['state'] == 'complete')} complete and Daily Gift incomplete.")
assert len(chk) == 28 and [c["name"] for c in chk if c["state"] != "complete"] == ["Daily Gift"]

fo = rows("gdrive.drive_files", id="d_9b41e7c2a05d36f8e1c7a4")[0]
ev("folder", "Find Owen's DD bug carry-over folder in Drive (search the folder name from the prompt)",
   f"Folder \"{fo['name']}\", id d_9b41e7c2a05d36f8e1c7a4, owner {fo['owner_email']}, created {pt(fo['created_time'])}.")

evt = rows("gcal.gcal_events", event_id="evt_6e2c91d4b07f3a58c1d2e4")[0]
att = [a["email"] for a in json.loads(evt["attendees_json"])]
ev("review", "Read Sunday's bug review on Owen's calendar (list his events for Sun Feb 15 2026; \"Sunday's bug review\" from the prompt and OE «hub»)",
   f"Event \"{evt['summary']}\", organizer {evt['organizer_email']}, starts {pt(evt['start_ts'])} (not yet held). Attendees: " + ", ".join(att) + ".")

CV = OB["slack_files"]["messages/CE156FDFB428/2025-11.json"]
roots = [m for m in CV if m.get("subtype") == "document_comment_root"]
lines = [m for m in roots if m["text"].strip()]
empty = [m for m in roots if not m["text"].strip()]
last = max(m["ts"] for m in lines)
ev("canvas_find", "Find the comment channel of Vincent's Android canvas in Slack (search channels \"Android\", from OE «rules»'s \"Vincent's Android canvas\")",
   "Channel \"FC:F09GAFM2DRR:Bugs on Android 2231 11_25_2025\", id CE156FDFB428.")
ev("canvas", "Read every root comment in that channel in Slack (channel from OE «canvas_find»; page through the whole history)",
   f"{len(roots)} root comments posted {pt(tsiso(roots[0]['ts']))} to {pt(tsiso(last))}. {len(empty)} are empty (their lines were deleted): ts "
   + ", ".join(m["ts"] for m in empty) + f". The other {len(lines)} are the lines, {sum(1 for m in lines if m['text'].startswith('☑'))} with a ticked box and {sum(1 for m in lines if m['text'].startswith('☐'))} unticked; each line's text is in its ticket event below (OEs «newc_first» to «newc_last»; lines 3 and 29, which get no ticket, in OEs «note:ENG-2073» and «note:ENG-2363»). The last line is ts {last}.")

par = {}
for r in rows("slack.slack_messages"):
    if r.get("thread_ts_legacy") and r["channel_id"] == "CE156FDFB428":
        par[f"CE156FDFB428/{r['ts']}"] = r["thread_ts_legacy"]
LN = {m["ts"]: i for i, m in enumerate(sorted(lines, key=lambda m: float(m["ts"])), 1)}
TIP, TRN, TEAM, LV1, LV2 = "CE156FDFB428/1763845512.559339", "CE156FDFB428/1763845212.507119", "CE156FDFB428/1763742012.611229", "CE156FDFB428/1763845812.703339", "CE156FDFB428/1763845872.804449"


def lno(rid):
    return LN[par[rid]]


TAVF = [m for m in CV if m.get("thread_ts") == "1763642831.967359" and m["text"] == "I send the fix"][0]
ARF = [m for m in CV if m["ts"] == "1763671462.192489"][0]
ev("canvas_threads", "Read the thread under each line in Slack (the roots from OE «canvas» that have replies; read each thread to its last reply)",
   f"Line {LN['1763642831.967359']} (Tavern buttons): Brian, {pt(tsiso(TAVF['ts']))}: " + q(TAVF["text"], "I send the fix") + ". "
   + f"Line {lno(TIP)} (navigation bar tooltips), last reply, Vincent, {pt(SM[TIP]['created_at'])}: " + q(st(TIP), "checked Brian's second fix, the 1 pixel gap is gone and the tooltips look right on my android now") + ". "
   + f"Line {lno(TRN)} (train level backgrounds): Arthur, {pt(tsiso(ARF['ts']))}: " + q(ARF["text"], "fixed") + f"; then Vincent, {pt(SM[TRN]['created_at'])}: " + q(st(TRN), "better but the snow train is still off and the green shows, leaving this one open") + ". "
   + f"Line {lno(TEAM)} (team quit): Vincent, {pt(SM[TEAM]['created_at'])}: " + q(st(TEAM), "the leave team popup is fine now but the navigation bar still goes after quitting") + ". "
   + f"Line {lno(LV1)} (lives not decreased after a loss): Vincent, {pt(SM[LV1]['created_at'])}: " + q(st(LV1), "same after Oliver's change, a loss still doesn't take a life") + ". "
   + f"Line {lno(LV2)} (lives only decreased after losing twice): Vincent, {pt(SM[LV2]['created_at'])}: " + q(st(LV2), "same here, it still only drops on the second loss") + ".")

BAR1, BAR2 = "C05V5FNLB9V/1766415211.386389", "C05V5FNLB9V/1766415326.501939"
POSTS = ["C05V5FNLB9V/1764256187.655299", "C05V5FNLB9V/1764266442.497979", "C05V5FNLB9V/1764659550.713509", "C05V5FNLB9V/1764660142.352319",
         "C05V5FNLB9V/1764661312.152719", "C05V5FNLB9V/1764661921.018749", BAR1]
first = {p: bt(p).split("\n")[0].strip() for p in POSTS}
ev("posts", f"Read the bug channel #god-bugs in Slack from just after the last canvas line (ts {last}, OE «canvas») to the clock (the bug channel from OE «rules»)",
   "Seven bug posts: " + "; ".join(f"{pt(tsiso(p.split('/')[1]))} \"{short(first[p])}\"" for p in POSTS)
   + f". The bottom bar bug is one post in two messages ({BAR1.split('/')[1]} and {BAR2.split('/')[1]}; the replies sit under the second). Not bug posts: Arthur's \"is this related to the new symbols?\" "
   "(a follow-up on the mega tile post), Robert's \"Happened twice in the video\" (a follow-up on the flickering post), Robert's \"tested your build for the most part\" with a Google Doc link (points at a QA doc), "
   "Arthur's question to Leonard \"is purchasing no-ads supposed to turn off rewarded video ads too?\" and Leonard's two answers (a design question for Leonard), five Nov 25 chat messages (where the canvases are, asking for a build to test), and canvas, leave and join notices.")
for ln, rid in (("is this related to the new symbols?", "C05V5FNLB9V/1764256319.497399"), ("Happened twice in the video", "C05V5FNLB9V/1764659554.897599"),
                ("tested your build for the most part", "C05V5FNLB9V/1764662837.138929"), ("is purchasing no-ads supposed to turn off rewarded video ads too?", "C05V5FNLB9V/1767191512.428539")):
    q(bt(rid), ln)

MEGA, WIN, BAR = "C05V5FNLB9V/1764331830.705279", "C05V5FNLB9V/1764329192.159229", "C05V5FNLB9V/1767021345.207719"
ev("post_threads", "Read the thread under each of the seven posts in Slack (posts from OE «posts»; read each thread to its last reply)",
   f"Mega tile, last reply, Marcus, {pt(SM[MEGA]['created_at'])}: " + q(st(MEGA), "still happens on today's build") + ". "
   + f"Tile dozer window, the only reply, Marcus, {pt(tsiso(WIN.split('/')[1]))}: " + q(bt(WIN), "Ok i fixed it and did a PR") + ". "
   + f"Flickering, last reply, Owen, {pt(tsiso('1764695707.749049'))}: " + q(bt("C05V5FNLB9V/1764695707.749049"), "testing a fix now, I'll let you guys know how it goes.") + ". "
   + f"Music, last reply, Owen, {pt(tsiso('1764695726.782669'))}: " + q(bt("C05V5FNLB9V/1764695726.782669"), "thanks for the info, I'll check this issue next.") + ". "
   + f"Acid, last reply, Brian, {pt(tsiso('1764694672.078619'))}: " + q(bt("C05V5FNLB9V/1764694672.078619"), "I'm checking") + ". "
   + f"Treasure button, Brian, {pt(tsiso('1764694606.476379'))}: " + q(bt("C05V5FNLB9V/1764694606.476379"), "I send the fix") + ", then Robert: " + q(bt("C05V5FNLB9V/1764694629.652379"), "Thanks") + ". "
   + f"Bottom bar, reply 61 and last, Brian, {pt(SM[BAR]['created_at'])}: " + q(st(BAR), "the new camera setup fixed it, the bottom bar and the top panel both show on the devices I have here, closing this one") + ".")

pr = OB["github"]["harmonygames-Games/GameOfDominoes#1913"]["rec"]
ev("pr1913", "Find and read Marcus's window PR in GitHub (search pull requests \"tile dozer\" in harmonygames-Games/GameOfDominoes, from the post and Marcus's \"did a PR\" in OE «post_threads»)",
   f"PR #1913 \"{pr['title']}\", state {pr['state']}, not merged, base {pr['base_ref']}, head {pr['head_ref']}, created {pt(pr['created_at'])}.")

SHOP = "C09Q4S613CN/1764606918.318209"
ev("shop", "Search Slack for later records on the shop icons line (search \"Memory Tile\", from the line \"shops from rivertile and memory tile has weird shop icons\" in OE «canvas»; open the hit's thread)",
   f"Brian's reply in #dd-road-to-sub-250mb, {pt(SM[SHOP]['created_at'])}, the 8th reply under Robert's post " + q(bt("C09Q4S613CN/1764042435.541279"), "Are these the right asset for the gems?") + f" ({pt(tsiso('1764042435.541279'))}): "
   + q(st(SHOP), "I was back in the shop prefabs today, the round icons on the River Tile and Memory Tile shops are there again on the current build, so don't trust that tick") + f". Later than the line itself (posted {pt(tsiso('1763549455.195819'))}).")

TAV = "D05USBTQY1F/1765452012.418229"
ev("tavern", "Search Slack for later records on the Tavern line (search \"Tavern\", from the line \"Tavern buttons lost its frame\" in OE «canvas»)",
   f"Marcus's DM to Owen, {pt(SM[TAV]['created_at'])}: " + q(st(TAV), "the Tavern buttons lost their frame again on last night's Android build, I looked at the prefab and Brian's fix didn't hold") + f". Later than the line (posted {pt(tsiso('1763642831.967359'))}) and Brian's fix in its thread (OE «canvas_threads»).")

LIV = "C09SWTHEMEW/1764659626.614679"
ev("lives", "Search Slack for the lives change (search \"lives\", from the three lives lines in OE «canvas»; look from Nov 22 2025 on)",
   f"Leonard Hayes in the shared publishing channel, {pt(tsiso(LIV.split('/')[1]))}: " + q(bt(LIV), "We are removing lives feature from the game and replacing it with a ticket system similar to Domino Dreams.")
   + " Other hits include Dec 2 and Dec 3 posts in the group DM with Leonard, Brian and Arthur, where the economy-line work is discussed.")

WC = ["C9CA62B5180A/1765927350.212199", "C9CA62B5180A/1765927876.696389", "C9CA62B5180A/1765928003.630799"]
BR3, OUT17 = "C9CA62B5180A/1764721779.638599", "C9CA62B5180A/1765933143.608699"
ev("wc", "Read the December posts in the group DM with Leonard, Brian and Arthur in Slack (the channel from OE «lives»'s hits)",
   f"Owen, {pt(tsiso('1764721779.638599'))}: " + q(bt(BR3), "I suggest we all work on a feature branch, and once the economy changes are completed we can move it to develop if need it.", "Working branch is `EconomyChanges`")
   + f". Arthur, {pt(tsiso('1765927350.212199'))}: " + q(bt(WC[0]), "can you disable WC and I'll start deploying stuff to prod") + f"; Owen, {pt(tsiso('1765927876.696389'))}: " + q(bt(WC[1]), "event disabled")
   + "; Owen: " + q(bt(WC[2]), "pushed to EconomyChanges branch") + f". Leonard's update notes, {pt(tsiso('1765933143.608699'))}: " + q(bt(OUT17), "Lives are out, now you can enter using", "the lives counter is removed") + ". Win & Collect is the Collect&win screen of ENG-2424.")

B2297 = json.dumps(OB["slack"]["C05433XK267/1765310444.095399"]["rec"]["attachments"], ensure_ascii=False)
B2299 = json.dumps(OB["slack"]["C05433XK267/1765397569.397939"]["rec"]["attachments"], ensure_ascii=False)
ev("builds", "Read the Android EconomyChanges build lines in #builds in Slack (search \"EconomyChanges\", the branch named in OE «wc»; Dec 2025)",
   f"{pt(tsiso('1765310444.095399'))}: " + q(B2297, "DD Android - #2297 - EconomyChanges - (?MB) Still Failing after 15 min") + " (the build failed; its list shows what is on the branch) with changes " + q(B2297, "Fix for EndLevelPopup flickering on Tap Anywhere clicked [Arthur Blake]", "Nathan Animation Fix [Arthur Blake]", "Updated URLAudioPlayer to fully download clip if needed [Arthur Blake]")
   + f". {pt(tsiso('1765397569.397939'))}: " + q(B2299, "DD Android - #2299 - EconomyChanges - (220MB) Success") + " with changes " + q(B2299, "Removed life pop-up from end screen") + ".")

FLK = "C09Q4S613CN/1766164222.418229"
ev("flicker", "Search Slack for later records on the flickering post (search \"flickering\", from the post in OE «posts»; open the hit's thread)",
   f"Robert's reply in #dd-road-to-sub-250mb, {pt(SM[FLK]['created_at'])}, under his own report " + q(bt("C09Q4S613CN/1764013100.931229"), "Not game breaker, but some flickering when I hit play button or when I exit a level") + ": "
   + q(st(FLK), "the flickering is gone on this week's build, both on the play button and coming out of a level") + ". Later than the thread's last reply (OE «post_threads»).")

TRC = json.dumps(OB["slack"]["C050WGU41HR/1764694580.083459"]["rec"]["attachments"], ensure_ascii=False)
ev("treasure_commit", "Search Slack for the treasure button fix (search \"Treasure button\", from the post in OE «posts»)",
   f"#engineering-bots, {pt(tsiso('1764694580.083459'))}: a commit pushed to develop by brian.foster, " + q(TRC, "fbe7bdea", "Fix issue opening Axe Arena panel from Nate Treasure button")
   + ", earlier the same day than Owen's post starting the EconomyChanges branch (4:29 PM PT, OE «wc»).")
CM = OB["commit_merge"]
ev("merge", "Search GitHub commits for develop merged into EconomyChanges (search commits \"into EconomyChanges\" in harmonygames-Games/GameOfDominoes, the branch from OE «wc»)",
   f"Commit {CM['sha'][:8]} by Arthur Blake, {pt(CM['authored_date'])}: " + q(CM["message"], "Merge remote-tracking branch 'origin/develop' into EconomyChanges")
   + ". It brings develop, which has the Dec 2 treasure button fix (OE «treasure_commit»), into EconomyChanges.")
p16 = OB["github"]["harmonygames-Games/GameOfDominoes#1916"]["rec"]
c16 = rows("github.github_pr_comments", id="harmonygames-Games/GameOfDominoes#1916#c_2")[0]
ev("pr1916", "Find and read the camera PR in GitHub (search pull requests \"camera\" in harmonygames-Games/GameOfDominoes, from Brian's \"the new camera setup fixed it\" in OE «post_threads»; the one merged in Dec 2025)",
   f"PR #1916 \"{p16['title']}\", base {p16['base_ref']}, head {p16['head_ref']}, merged {pt(p16['merged_at'])}; Arthur's comment, {pt(c16['created_at'])}: " + q(clean(c16["body"]), "Same here, into EconomyChanges for the next BoomBit drop."))

MUS, POP, GIFT, NOV19 = "D07E9PSQB6W/1765206644.602119", "D07E9PSQB6W/1765471563.704419", "D07E9PSQB6W/1765471651.208713", "D07E9PSQB6W/1763585860.227679"
ev("brian_dm", "Read Owen's DM with Brian Foster in Slack from Nov 19 2025 on (Brian owns the UI card in OE «closing», and the acid post's last reply is his \"I'm checking\" in OE «post_threads»)",
   f"Brian, {pt(tsiso(NOV19.split('/')[1]))}: " + q(bt(NOV19), "I just need to go over the Daily Gift one more time. I’ll finish that tomorrow morning, so it’ll be done before the meeting.")
   + f" Brian, {pt(SM[MUS]['created_at'])}: " + q(st(MUS), "music plays normally on my side since your audio player change, and Nate's acid throw lines up again after my animation fix, Robert's two are sorted")
   + f". Brian, {pt(SM[POP]['created_at'])}: " + q(st(POP), "I never got back to the two popups from Arthur's reviews: the Axe Arena info popup still has the old frame and the Tile Dozer how-to-play popup still points at the old sprites.")
   + f" Brian, {pt(SM[GIFT]['created_at'])}: " + q(st(GIFT), "Daily Gift isn't finished either, the panel never got its last pass."))

mail = [r for r in rows("gmail.gmail_messages") if r["thread_id"] == "owen.baker@harmonygames.co/1849333980856689601"][0]
ev("apple", "Search Owen's mail for messages from Vincent Parker about signing in, in Gmail (OE «rules» says Vincent tied lines to tickets; the unticked Apple and manual sign-in lines read in OE «canvas» are about signing in) and read his \"sign in lines on my list\"",
   f"Vincent to Owen, {pt(mail['date'])}, subject \"{mail['subject']}\", in the inbox: " + q(clean(mail["body_text"]), "The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new."))

e2073 = OB["linear"]["ENG-2073"]["rec"]
ev("eng2073", "Read ENG-2073 in Linear (named in OE «apple»)", f"ENG-2073 \"{e2073['title']}\", state {e2073['state_id']} (open).")

e2363 = OB["linear"]["ENG-2363"]["rec"]
ali = rows("linear.linear_comments", issue_id="ENG-2363")[0]
ev("signin", "Search Linear issues for \"signing\" (the manual sign-in line in OE «canvas» is about signing in) and read the comments on ENG-2363",
   f"ENG-2363 \"{e2363['title']}\", state {e2363['state_id']} (open). Vincent, {pt(ali['created_at'])}: " + q(clean(ali["body"]), "Android still hits this: the manual sign-in line on my list gets stuck on loading after signing in, same thing as here."))

NM = ["ENG-2406", "ENG-2181", "ENG-2351", "ENG-2280", "ENG-2281", "ENG-2398"]
nm = []
for k in NM:
    c = rows("linear.linear_comments", issue_id=k)[0]
    r = OB["linear"][k]["rec"]
    nm.append(f"{k} \"{r['title']}\" ({r['state_id']}), Arthur, {pt(c['created_at'])}: " + q(clean(c["body"]), clean(c["body"])))
ev("near_miss", "Check whether an open ticket covers any item that isn't fixed: list the open ENG tickets in Linear (any open state: Bugs, Todo, In Progress, PR, Validation, Regression, Backlog) and read the comments on the ones that read like a canvas line or a bug post (the Covered test in OE «rules»)",
   "Six open tickets each carry a Nov 20 2025 comment from Arthur that narrows them: " + "; ".join(nm)
   + ". Each comment limits its ticket to something other than the shop icons, Tavern, train backgrounds, team-quit, backend-errors, mega tile and tile dozer window items, so none of those seven is Covered; the two covering tickets are ENG-2073 and ENG-2363 (OEs «apple» to «signin»).")
KIDS = [c["key"] for c in COH["children"]]
LIN = OB["linear"]
done9 = [k for k in KIDS if LIN[k]["rec"]["state_id"] == "Done"]
open19 = [k for k in KIDS if k not in done9]
grp = {"ENG-2403": [], "ENG-2404": [], "ENG-2405": []}
for k in sorted(KIDS):
    grp[LIN[k]["rec"]["parent_id"]].append(k)
ev("tree", "List the UI tree under the master ticket in Linear (children of ENG-2401, then the children of each group)",
   "Groups ENG-2403 Core Game, ENG-2404 Live-Ops, ENG-2405 Mini-Games, all Todo; ENG-2401 Todo. 28 children: "
   + "; ".join(f"{g}: " + ", ".join(f"{k} {LIN[k]['rec']['title'].replace(' UI Optimization', '').replace(' - UI Optimization', '').strip(' -')} ({LIN[k]['rec']['state_id']})" for k in grp[g]) for g in grp) + f". {len(done9)} Done, {len(open19)} open.")
assert len(done9) == 9 and len(open19) == 19

com = {r["issue_id"]: r for r in rows("linear.linear_comments")}
sea = com["ENG-2428"]
ev("kid_notes", "Read the comments on each of the 19 open children in Linear (list from OE «tree»)",
   f"Four comments in all. ENG-2428, Oliver Brooks, {pt(sea['created_at'])}: " + q(clean(sea["body"]), "The illustrations went in but the reward track still uses the old frames, this isn't finished.")
   + f" ENG-2410, Brian, {pt(com['ENG-2410']['created_at'])}: " + q(clean(com["ENG-2410"]["body"]), "Checked the Shop screen after the merge, looks right on android.")
   + f" ENG-2429, Brian: " + q(clean(com["ENG-2429"]["body"]), "Checked the Remove Ad pop up on today's build, looks right on android.")
   + f" ENG-2430, Brian: " + q(clean(com["ENG-2430"]["body"]), "Checked the Offers on today's build, looks right on android."))

rc = {k: rows("github.github_review_comments", id=f"harmonygames-Games/GameOfDominoes#{k}#rc_1")[0] for k in (1905, 1908)}
p05, p08 = OB["github"]["harmonygames-Games/GameOfDominoes#1905"]["rec"], OB["github"]["harmonygames-Games/GameOfDominoes#1908"]["rec"]
ev("inline", "Read the review comments on the UI optimization PRs in GitHub (search pull requests \"UI Optimization\" in harmonygames-Games/GameOfDominoes, the children's titles from OE «tree»)",
   f"PR #1905 \"{p05['title']}\", merged {pt(p05['merged_at'])}; Arthur's review comment, {pt(rc[1905]['created_at'])}: " + q(clean(rc[1905]["body"]), "the Tile Dozer how-to-play popup still points at the old sprites in this PR. That has to be swapped before the Tile Dozer ticket can close.")
   + f" PR #1908 \"{p08['title']}\", merged {pt(p08['merged_at'])}; Arthur's review comment, {pt(rc[1908]['created_at'])}: " + q(clean(rc[1908]["body"]), "the Axe Arena info popup keeps the old frame here. Needs doing before the Axe Arena ticket can close."))

# ================================================================ analysis
CANVAS = [b for b in COH["bugs"] if b["kind"] == "canvas_line"]
assert [b["id"].split("/")[1] for b in CANVAS] == sorted((m["ts"] for m in lines), key=float)
ev("decide", "Take the first outcome that fits for each of the 70 bugs (rules in OEs «rules» and «amend»; records in OEs «canvas» to «inline»)",
   "Fixed 58: the 53 ticked lines other than the shop icons and the Tavern line (the tick stands; for the tooltips line Vincent also confirmed the second fix, OE «canvas_threads»), "
   "the flickering post (Robert's reply, OE «flicker»; the fix is on EconomyChanges, listed in build #2297's changes: that build failed, and #2299 on the same branch succeeded on Dec 10, OE «builds»), the music and acid posts (Brian's Dec 8 line, OE «brian_dm»; both fixes are on EconomyChanges, listed in build #2297's changes, OE «builds»), the treasure button post (Brian's fix, OE «post_threads»; the commit went to develop, and develop was merged into EconomyChanges on Dec 17, OEs «treasure_commit» and «merge») and the bottom bar post (Brian closed it, OE «post_threads»; the camera PR merged into EconomyChanges, OE «pr1916»). "
   "Gone 3: the three lives lines, the two with Vincent's later replies (OE «canvas_threads») and \"When I change the character, it just adds 1 life back or reduced the timer by 20 min.\", since lives are removed on the economy line (OE «lives»; build #2299 and Leonard's Dec 16 update notes, OEs «builds» and «wc»). "
   "Covered 2: the Apple sync line (ENG-2073, OEs «apple» and «eng2073») and the manual sign-in line (ENG-2363, OE «signin»). "
   "Broken 7: the shop icons line (OE «shop»), the Tavern line (OE «tavern»), the train backgrounds line and the team-quit line (Vincent's replies, OE «canvas_threads»), the unticked backend-errors line (it stays open), the mega tile post (OE «post_threads») and the tile dozer window post (PR #1913 is still open, not merged, OE «pr1913»); no open ticket covers any of the seven (OE «near_miss»). "
   "So 68 new tickets (58 Done, 7 Bugs, 3 Canceled), each in team Engineering with label Bug, parent ENG-2401, no assignee, empty description, and title \"[2231] \" plus the line without its box or the post's first line as written (a Slack mention or emoji code may stay as written or show as a name).")
HOLD = {"ENG-2424": "Win & Collect is switched off on the economy line (OE «wc»)", "ENG-2426": "the Axe Arena info popup never got its pass (OEs «inline» and «brian_dm»)",
        "ENG-2428": "the reward track still uses the old frames (OE «kid_notes»)", "ENG-2434": "the Tile Dozer how-to-play popup never got swapped (OEs «inline» and «brian_dm»)",
        "ENG-2437": "the Daily Gift panel never got its last pass (OE «brian_dm», later than Brian's Nov 19 plan)"}
moves = [k for k in open19 if k not in HOLD]
assert len(moves) == 14
ev("decide_kids", "Decide each UI child under the tree rule (OE «rules»; tree from OE «tree», records from OEs «wc», «brian_dm», «kid_notes» and «inline»)",
   "Stay where they are: " + "; ".join(f"{k} ({LIN[k]['rec']['state_id']}): {v}" for k, v in HOLD.items()) + ". Move to Done: " + ", ".join(moves)
   + " (the shop icons regression on the River Tile and Memory Tile shops is a bug with its own ticket, and a bug on a screen doesn't hold its child, OE «rules»). 23 of 28 end Done: the 9 already Done and these 14. Every one of the 28 gets a line naming the public build 0.3.310 (OEs «rules» and «closing»).")

# ================================================================ writes: tickets and notes
STATE = {"Fixed": "Done", "Gone": "Canceled", "Broken": "Bugs"}
new = 0
for i, b in enumerate(COH["bugs"], 1):
    t = TRUTH[b["key"]]
    if t["Outcome"] == "Covered":
        continue
    rid = b["id"] if b["id"] != BAR2 else BAR1
    if b["kind"] == "canvas_line":
        text = bt(rid)
        title = text[1:].strip()
        what = f"canvas line {i}"
    else:
        title = first[rid]
        what = "the " + {"mega tile missing a face": "mega tile", "tile dozer window background": "tile dozer window", "flickering": "flickering", "music plays only sometimes": "music",
                         "acid animation delay": "acid", "treasure button opens axe arena": "treasure button", "android bottom bar invisible": "bottom bar"}[b["key"]] + " post"
    q(bt(rid), title)
    new += 1
    ev(f"new:{b['key']}", f"Create the ticket for {what} in Linear (fields from OE «decide»)", f"A new issue in state {STATE[t['Outcome']]}, title \"[2231] {title}\".")
assert new == 68
for k, line_key in (("ENG-2073", "In general I cannot sync and sign in with"), ("ENG-2363", "On android manual sign-in has an issue after the")):
    b = [x for x in COH["bugs"] if x["key"] == line_key][0]
    wording = bt(b["id"])[1:].strip()
    ev(f"note:{k}", f"Add the canvas wording on {k} in Linear (Covered, OE «decide»)", f"A comment on {k} carrying the line \"{q(wording, wording)[1:-1]}\".")

# ================================================================ writes: the UI tree
TITLE = {k: LIN[k]["rec"]["title"] for k in KIDS}
for k in moves:
    ev(f"move:{k}", f"Move {k} ({TITLE[k]}) to Done in Linear (OE «decide_kids»)", f"{k} state {LIN[k]['rec']['state_id']} → Done.")
for k in sorted(KIDS):
    if k in done9:
        say = "it is Done and landed in Android 0.3.310"
    elif k in HOLD:
        say = f"it stays {LIN[k]['rec']['state_id']} because {HOLD[k].split(' (OE')[0]}; public build 0.3.310"
    else:
        say = "it is Done and landed in Android 0.3.310"
    ev(f"line:{k}", f"Leave a line on {k} ({TITLE[k]}) in Linear (OE «decide_kids», Brian's rule in OE «closing»)", f"A comment on {k} saying {say}.")

# ================================================================ writes: the sheet, sharing and the reply
ev("sheet_create", "Create the sheet in Sheets (title free; it is for the folder from OE «folder»)", "A new Google Sheet in Owen's Drive.")
ev("sheet_move", "Move the sheet into the DD bug carry-over folder in Drive (sheet from OE «sheet_create», folder from OE «folder»)", "The sheet's parent is d_9b41e7c2a05d36f8e1c7a4 (DD bug carry-over).")
ev("sheet_rows", "Write the rows to the sheet in Sheets (sheet from OE «sheet_create»; outcomes from OE «decide», tickets from OEs «new_first» to «new_last»)",
   "Header Bug, Outcome, Ticket, Why (OE «rules»), then 70 rows, one per bug: its line or post, its outcome (58 Fixed, 7 Broken, 3 Gone, 2 Covered), its ticket (the new issue's key, or ENG-2073 and ENG-2363 for the two Covered lines) and why (the record from OEs «canvas» to «inline»).")
for e, who in (("arthur.blake@harmonygames.co", "Arthur Blake"), ("robert@harmonygames.co", "Robert"), ("oliver.brooks@harmonygames.co", "Oliver Brooks")):
    assert e in att
    ev(f"share:{e}", f"Share the sheet with {who} in Drive (address from OE «review»)", f"{e} can open the sheet (writer, commenter or reader).")
ev("reply", "Reply to Arthur in the thread of his DM in Slack (the DM and message from OE «hub», after every other write)",
   "A reply in that thread (thread_ts 1770937805.214409) with the numbers he asked for: 9 still broken (7 Broken plus 2 Covered, OE «rules»'s report-back rule), 68 new tickets filed, 23 of the 28 UI children Done.")

# ---------------------------------------------------------------- resolve the event numbers the text cites
newk = [k for k in N if k.startswith("new:")]
canv = [k for k in newk if [b for b in COH["bugs"] if b["key"] == k[4:]][0]["kind"] == "canvas_line"]
TOK = {**{k: str(v) for k, v in N.items()}, "new_first": str(N[newk[0]]), "new_last": str(N[newk[-1]]), "newc_first": str(N[canv[0]]), "newc_last": str(N[canv[-1]])}


def resolve(s):
    def sub(m):
        assert m.group(1) in TOK, m.group(1)
        return TOK[m.group(1)]
    return re.sub(r"«([a-z_0-9:A-Z-]+)»", sub, s)


EV = [(resolve(a), resolve(e)) for a, e in EV]
out = []
for i, (a, e) in enumerate(EV, 1):
    out.append(f"OE {i}  {a}\nExpected: {e}\n")
text = "\n".join(out)
open(os.path.join(TI, "08_Oracle_Events.md"), "w").write(text)
print("events", len(EV), "chars", len(text), "quotes checked", len(CHECKS))
print({k: v for k, v in N.items() if not k.startswith(("new:", "move:", "line:", "share:", "note:"))})
json.dump({"index": N, "first_line": {k: v for k, v in first.items()}}, open(os.path.join(HERE, "oe_events_index.json"), "w"), indent=1)
