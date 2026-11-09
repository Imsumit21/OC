#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and rows.json (input to build_plan.py) for samuel_zm_beta_messages (rev6).
Every quoted source value is read from its record here: seeded rows via base_check.parse_sql (never executed), base records via
hg.py get-many. Run from anywhere."""
import json
import subprocess
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[5]
TI = WS / "Task_Authoring/task_inputsK"
WF = TI / "Working_Files"
sys.path.insert(0, str(WS / "Task_Authoring/tools"))
from base_check import parse_sql  # noqa: E402

SQL = parse_sql((TI / "01_Universe_Inject.sql").read_text())
CTX = json.loads((WF / "00_Task_Context.json").read_text())
ROOTS = CTX["source"]["paths"]
TRUTH = {k: v for k, v in json.loads((WF / "solver/truth.json").read_text()).items() if isinstance(v, dict) and v.get("Call")}
FID = json.loads((WF / "plan/oe_ledger_ids.json").read_text())["fid"]
NUM = json.loads((WF / "plan/oe_events_index.json").read_text())["index"]
SAM = "samuel.turner@harmonygames.co"
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"
SNAP = ("The synth-cut snapshot is cut at the freeze (2025-09-30 23:59:59 PT); the record's own last change is before the freeze, "
        "so its exported content is its state at the freeze. ")
ENV = {"TASK_AUTHORING_TASK_DIR": str(TI)}


def rows_of(table):
    return [x["row"] for x in SQL if x["table"] == table and x["op"] == "insert"]


def sql_row(table, identity):
    r = [x for x in rows_of(table) if all(x.get(k) == v for k, v in identity.items())]
    assert len(r) == 1, (table, identity, len(r))
    return r[0]


def get_json(service, rel, pointer):
    req = {"items": [{"service": service, "file": rel, "id": "v", "pointer": pointer, "max_chars": 65536}]}
    out = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "search", "get-many", "--request", "-",
                          "--task-dir", str(TI)], input=json.dumps(req), capture_output=True, text=True, cwd=WS)
    item = json.loads(out.stdout)["items"]["v"]
    assert item.get("encoding") == "rendered-json" and item.get("truncated") is False, (rel, pointer, item)
    return json.loads(item["text"])


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def review(ids, why):
    return {"reviewer": REVIEWER, "rationale": why, "evidence_ids": ids}


def S_sql(service, rid, table, identity, column, rec_col, hops, why, semantics="fact", mutable=False, rev=None):
    row = sql_row(table, identity)
    src = {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": identity,
           "column": column, "source_value": row[column], "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": semantics, "mutable_state": mutable, "recorded_at_column": rec_col,
                                 "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


def S_json(service, rid, rel, pointer, rec_pointer, hops, why, mutable=False, rev=None):
    value = get_json(service, rel, pointer)
    recorded = get_json(service, rel, rec_pointer)
    src = {"service": service, "id": rid, "source_file": str((Path(ROOTS[service]) / rel).relative_to(WS)), "pointer": pointer,
           "source_value": value, "evidence_path": path(*hops), "reachability_rationale": why,
           "temporal_evidence": {"value_semantics": "fact", "mutable_state": mutable, "recorded_at_pointer": rec_pointer,
                                 "rationale": f"Base record; {rec_pointer} = {recorded} (before the freeze)."}}
    if mutable:
        src["temporal_evidence"]["state_at_freeze_review"] = rev
    return src


def S_contact(email, idx):
    rel = "contacts.json"
    v = get_json("contacts", rel, f"/contacts/{idx}/email")
    assert v == email, (v, email)
    return {"service": "contacts", "id": email, "source_file": str((Path(ROOTS["contacts"]) / rel).relative_to(WS)),
            "pointer": f"/contacts/{idx}/email", "source_value": v, "evidence_path": path(("contacts", email)),
            "reachability_rationale": "Contacts is unscoped; the address is the Contacts entry of the person who filed the ask.",
            "temporal_evidence": {"value_semantics": "directory_identity", "mutable_state": False,
                                  "rationale": "A directory address; it establishes who to write to, not an earlier state."}}


def q(text, sub):
    assert sub in text, sub
    return sub


def cut(s, n):
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0]


# ---- reusable sources --------------------------------------------------------------------------------------------
HUB = ("slack", "D06L58XCVKK/1759264851.763895")
RULE = ("gdocs", "f_dc45e0e5a8b8635c1b82b2")
hub_row = sql_row("slack.slack_messages", {"ts": "1759264851.763895"})
HUB_TXT = hub_row["text"]
rule_row = sql_row("gdocs.docs_documents", {"document_id": RULE[1]})
RULE_TXT = rule_row["body_text"]
s_hub = S_sql("slack", HUB[1], "slack.slack_messages", {"id": hub_row["id"]}, "text", "created_at", [HUB],
              "The prompt names Leonard's DM to Samuel from yesterday.")
s_rule = S_sql("gdocs", RULE[1], "gdocs.docs_documents", {"document_id": RULE[1]}, "body_text", "modified_time", [HUB, RULE],
               "Leonard's DM: 'make a call on each one using the message rule doc'; the doc is shared with Samuel.", mutable=True,
               rev=review([RULE[1], HUB[1]], SNAP + "Leonard's Sep 30 DM, later than the doc's 2025-09-26T17:10:54Z change, points "
                          "to it as the rule in force."))


def s_slack(rid, ts, why):
    row = sql_row("slack.slack_messages", {"ts": ts})
    return S_sql("slack", rid, "slack.slack_messages", {"id": row["id"]}, "text", "created_at", [HUB, RULE, ("slack", rid)], why), row["text"]


s_pull, PULL_TXT = s_slack("C0880U9751A/1759245146.720608", "1759245146.720608",
                           "Vincent's root post in #zombie-match3d (Samuel is a member); the rule doc names Vincent as the check.")
s_qareply, QAREPLY_TXT = s_slack("D06UFE81RF0/1759174846.723833", "1759174846.723833",
                                 "Vincent's reply in Samuel's own DM with him; the rule doc names Vincent as the check.")
s_ask, ASK_TXT = s_slack("C0880U9751A/1759167608.326578", "1759167608.326578",
                         "Robert's post in #zombie-match3d; the rule doc: 'The permission ask is Robert's call.'")
s_askreply, ASKREPLY_TXT = s_slack("C0880U9751A/1759170096.924778", "1759170096.924778",
                                   "Arthur's reply under Robert's post in #zombie-match3d.")
s_line2, LINE2_TXT = s_slack("C08R8CHB0QL/1759169129.445834", "1759169129.445834",
                             "Leonard's reply in #zombie-art (Samuel is a member); the rule doc: 'the latest line I've called'.")
QA_ID = f"{SAM}/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com>"
s_qa = S_sql("gmail", QA_ID, "gmail.gmail_messages", {"id": QA_ID}, "body_text", "date", [HUB, RULE, ("gmail", QA_ID)],
             "The rule doc: 'What Vincent counts as seen is in his QA note'; the mail is in Samuel's mailbox.")
QA_TXT = s_qa["source_value"]
COV_ID = f"{SAM}/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com>"
s_cov = S_sql("gmail", COV_ID, "gmail.gmail_messages", {"id": COV_ID}, "body_text", "date", [HUB, RULE, ("gmail", COV_ID)],
              "The cancellation mail in Samuel's mailbox; a Gmail search for 'lapsed' finds it.")
COV_TXT = s_cov["source_value"]
EVT = "evt_f2c03e69f50acf62c9d1c3"
s_line3 = S_sql("gcal", EVT, "gcal.gcal_events", {"event_id": EVT, "calendar_id": SAM}, "description", "updated",
                [HUB, RULE, ("gcal", EVT)], "The event sits on Samuel's calendar; a calendar search for 'Lapsed' finds it.")
LINE3_TXT = s_line3["source_value"]
s_log = S_sql("gsheets", "f_8eb8c04713ff6a6ef4a265", "gsheets.sheets_spreadsheets", {"spreadsheet_id": "f_8eb8c04713ff6a6ef4a265"},
              "title", "modified_time", [HUB, RULE, ("gsheets", "f_8eb8c04713ff6a6ef4a265")],
              "Vincent's QA note: 'Passes go in the Phone message checks sheet'; shared with Samuel.", mutable=True,
              rev=review(["f_8eb8c04713ff6a6ef4a265", RULE[1]], SNAP + "Last changed 2025-09-24T15:00:05Z."))
PR = "harmonygames-Games/match3d#248"
s_rc18 = S_sql("github", PR, "github.github_review_comments", {"id": PR + "#rc_18"}, "body", "created_at", [HUB, RULE, ("github", PR)],
               "Arthur's review comment on PR #248, the PR each of DES-315 to DES-320 names ('Built in match3d #248.').")
RC18_TXT = s_rc18["source_value"]
s_client = S_json("github", PR, "data.json", "/review_comments/599/diff_hunk", "/review_comments/599/created_at",
                  [HUB, RULE, ("github", PR)], "The hunk of NotificationManager.cs on PR #248; GitHub is unscoped.")
CLIENT_TXT = s_client["source_value"]
PNCARD = "6851a769c65dc0017a227bb7"
TECH = "68d1eb90bef538c7c5c5599d"
s_pncard = S_json("trello", PNCARD, "data.json", "/cards/705/name", "/cards/705/dateLastActivity", [("trello", PNCARD)],
                  "The prompt names 'our push notifications card'; Trello is unscoped.", mutable=True,
                  rev=review([PNCARD], SNAP + "The card name is what the prompt's words find."))
s_tech = S_json("trello", TECH, "data.json", "/cards/802/name", "/cards/802/dateLastActivity", [HUB, RULE, ("trello", TECH)],
                "The rule doc: 'Hold tickets go back to Todo unless the roadmap says otherwise'; the card is on ZM ROADMAP's BETA "
                "list. Its description (Trello action 68dae8c7d95e24b55b69bf80) is seeded and is named in the row's evidence; the "
                "base card is the record the V3 check can resolve.", mutable=True,
                rev=review([TECH, RULE[1]], SNAP + "The base card name; the seeded description is dated 2025-09-29T20:15:03Z."))
LIVE = ("confluence", "page_liveops_calendar")
LIVE_TXT = get_json("confluence", "confluence_working.json", "/pages/27/body")
DESC_FREEZE = [x for x in SQL if x["table"] == "trello.trello_cards" and x["op"] == "update" and x["where"].get("id") == TECH][0]["set"]["desc"]
ZOMC = {"Boss Arena attempts refilled": ("ZOM-542", "cmt_f1b8a109dfa70cdc4565"), "Daily gift about to reset": ("ZOM-556", "cmt_2b519285937e7fa79453"),
        "Teammate sent lives": ("ZOM-563", "cmt_eabac5435f2b3a575aad"), "Infinite lives ending": ("ZOM-483", "cmt_e2e2926a2080ca53c4ea")}


def s_zom(name):
    z, c = ZOMC[name]
    return S_sql("linear", z, "linear.linear_comments", {"id": c}, "body", "created_at", [HUB, ("linear", z)],
                 f"A comment on {z}, updated after DES-314 opened; a list of Linear tickets by updatedAt reaches it (OE 9).")


COMMENTS = {}
for c in rows_of("linear.linear_comments"):
    COMMENTS.setdefault(c["issue_id"], []).append(c)
for v in COMMENTS.values():
    v.sort(key=lambda c: c["created_at"])
ISSUES = {i["identifier"]: i for i in rows_of("linear.linear_issues")}
ARTHUR = "usr_" + next(c["author_id"] for c in COMMENTS["DES-321"] if "NotificationManager" in c["body"]).split("_", 1)[1]


def note(key):
    """The ticket comment that settles test 2 or 3, quoted whole."""
    cs = COMMENTS[key]
    arth = [c for c in cs if c["author_id"] == ARTHUR]
    return (arth or cs)[-1]


def who(key):
    return COMMENTS[key][0]


PEOPLE = {"brian": ("Brian Foster", "brian.foster@harmonygames.co", 160), "calvin": ("Calvin Price", "calvin.price@harmonygames.co", 134),
          "douglas": ("Douglas", "douglas@harmonygames.co", 136), "julia": ("Julia Lawson", "julia.lawson@harmonygames.co", 140),
          "martin": ("Martin Walsh", "martin.walsh@harmonygames.co", 141), "oliver": ("Oliver Brooks", "oliver.brooks@harmonygames.co", 157),
          "owen": ("Owen Baker", "owen.baker@harmonygames.co", 153), "robert": ("Robert", "robert@harmonygames.co", 107)}
S_CONTACT = {k: S_contact(v[1], v[2]) for k, v in PEOPLE.items()}
WHO_FID = {"brian": "F73", "calvin": "F74", "douglas": "F75", "julia": "F76", "martin": "F77", "oliver": "F78", "owen": "F79", "robert": "F80"}

SP_JOB = "His DM to me from yesterday has the whole job in it"
SP_FOLDER = "The new sheet and the one-page note go in my Drive folder"
SP_CHECK = "the checklist goes on our push notifications card"
SP_TICKETS = "He also wants things done on the tickets"
SP_MAIL = "some emails sent"
SP_DM = "When it's all finished tell him the counts in that same DM"
for s in (SP_JOB, SP_FOLDER, SP_CHECK, SP_TICKETS, SP_MAIL, SP_DM):
    assert s in (TI / "04_Prompt.txt").read_text()

FOLDER = "d_caafeec2804b3a67ce46aa"
FOLDER_NAME = f"Samuel's Drive folder {SAM} ({FOLDER})"
SHEET_ROW = "its calls sheet"
NOTE = "its one-page note"
Q_GO = q(RULE_TXT, "Go: it passes all six.")
Q_HOLD = q(RULE_TXT, "Hold: anything else, and name the test it failed.")
Q_DROP = q(RULE_TXT, "Drop: it fails test 1, or the client already covers it under another message, then name that message.")
Q_T2 = q(RULE_TXT, "2. The client can send it without a server.")
Q_T3 = q(RULE_TXT, "3. The client already schedules it.")
Q_T1 = q(RULE_TXT, "1. The feature behind it is in the beta.")
Q_T4 = q(RULE_TXT, "A player only counts once our own permission ask has happened, the settings toggle doesn't count.")
Q_T5 = q(RULE_TXT, "5. It fires on the right day.")
Q_T6 = q(RULE_TXT, "6. Vincent has seen it arrive on both iOS and Android.")
Q_MOVE = q(RULE_TXT, "Drop tickets go to Canceled, Go tickets stay as they are, Hold tickets go back to Todo unless the roadmap says otherwise.")
Q_FREEZE = q(DESC_FREEZE, "Held tickets sit in Backlog, unassigned.")
Q_SEEN = q(QA_TXT, "Seen only counts on a store build, on a real iOS device and a real Android device.")
Q_TIMERS = q(QA_TXT, "A build with shortened timers doesn't count, it only proves the code path.")
Q_PULL = q(PULL_TXT, "taking my tick off Full Ammo until I've seen it land")
Q_STILL = q(PULL_TXT, "the lapsed ones are still coming through")
Q_RACE = q(QAREPLY_TXT, "that iPhone was still on the 5-minute timers build when I ticked it, so scratch iOS.")
Q_ASK = q(ASK_TXT, "leaving our own ask after level 20")
Q_POPUP = q(ASKREPLY_TXT, "NotificationManager only schedules once our own ask has run or they switch it on from settings")
Q_RC18 = q(RC18_TXT, "This counts seven days from the day they last left the game, so it isn't tied to the rollover.")
Q_COV = q(COV_TXT, "The weekly one repeats for four weeks, so day 14 is already covered.")
Q_LINE3 = q(LINE3_TXT, 'Final for the 7 day one is "Your Squad Is Waiting", body stays. That replaces what I said in the art thread.')
Q_LINE2 = q(LINE2_TXT, 'make it "Your Squad Needs You Back", body stays')
Q_FOLD = q(HUB_TXT, "Put it in one sheet in your Drive folder, one row per message: Message, Ticket, Call, What's missing, Audience, Final headline, String change.")
Q_NOTE = q(HUB_TXT, "Next to it a one-page note for the team: start with D1 and D7 for the Sep 15 cohort week from the warehouse, iOS and Android separately, then the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why.")
Q_SCOPE = q(HUB_TXT, "Take every row on the PNs Beta tab plus every ask for a new phone message that's been filed on a ticket or a card up to today, and make a call on each one using the message rule doc.")
Q_CMT = q(HUB_TXT, "Leave the call as a comment on each ticket and move the ticket to match.")
Q_NEW = q(HUB_TXT, "Anything with no ticket gets one, but don't make a second one for something that already has a ticket under whatever name.")
Q_GOLIST = q(HUB_TXT, "Every Go goes on a checklist on our push notifications card so Vincent can tick it off.")
Q_MAIL = q(HUB_TXT, "Email each person who asked for something, apart from me, to say what happened to their asks.")
Q_COUNT = q(HUB_TXT, "When it's done tell me here how many Go, Hold and Drop.")
Q_STR = q(RULE_TXT, "A line that differs from what the client ships needs a string ticket under DES-314, because the strings are hard-coded, so open one when you make the call.")
Q_ONLYGO = q(RULE_TXT, "Final headline and String change are only for Go rows.")
Q_LATEST = q(RULE_TXT, "The final headline is the latest line I've called.")
Q_AUD = q(RULE_TXT, "Audience is who the ask says it's for.")
Q_LOOP = q(CLIENT_TXT, "DateTime fireTime = referenceDate.AddDays(i * 7);")
Q_BATCH = q(CLIENT_TXT, "BatchScheduleWeeklyNotifications(WeeklyReminderTitle, WeeklyReminderMessage, 4, serverToday);")
Q_DAY1 = q(CLIENT_TXT, "DailyNotifications(OneDayLapsedTitle, OneDayLapsedMessage, serverToday);")
Q_ALIAS = q(LIVE_TXT, "under a different name")

R = []


def oe(*keys):
    out = []
    for k in keys:
        n = f"OE {NUM[k]}"
        if n not in out:
            out.append(n)
    return out


def F(*keys):
    return " ".join(dict.fromkeys(FID[k] for k in keys))


def add(**kw):
    kw.setdefault("cat", "Outcome")
    kw.setdefault("dist", "—")
    kw.setdefault("grp", "—")
    kw.setdefault("just", f"{kw['kind'].capitalize()}: {kw['why']}.")
    body = kw["t"].split("The Agent ", 1)[1]
    kw["acc"] = [body]
    kw["ev"] = kw["ev"].replace("rule doc ('", f"rule doc {RULE[1]} ('").rstrip(".") + f". Accept: the Agent {body}."
    R.append(kw)


ITEMS = list(TRUTH.items())
TEST = {}  # message -> (test label, OE key)
for name, v in ITEMS:
    m = v["What's missing"]
    if name in ("Lives recharged", "Plague Race"):
        TEST[name] = ("test 6", "c6")
    elif name == "Weekly Leaderboard reset":
        TEST[name] = ("test 5", "c5")
    elif name == "Finish first mission":
        TEST[name] = ("test 4", "c4")
    elif v["Call"] == "Go":
        TEST[name] = ("all six", "c6")
    elif name == "Lapsed 14 days":
        TEST[name] = ("covered", "c3")
    elif v["Call"] == "Drop":
        TEST[name] = ("test 1", "c1")
    elif m == "needs a server send":
        TEST[name] = ("test 2", "c2")
    else:
        TEST[name] = ("test 3", "c3")

TRAPS = {"Lives recharged": "T5", "Plague Race": "T4", "Weekly Leaderboard reset": "T1", "Finish first mission": "T3",
         "Win & Collect start": "T6", "Lapsed 14 days": "T9", "Lapsed 7 days": "T2"}
ASKS = list(ZOMC)
ASK_T = "T7"
ASK_WORD = {"Boss Arena attempts refilled": "a phone reminder once the daily Boss Arena attempts refill",
            "Daily gift about to reset": "a phone reminder the evening before the daily gift streak resets",
            "Teammate sent lives": "a phone message when a teammate sends you lives",
            "Infinite lives ending": "a phone reminder when infinite lives are about to run out"}


def tag(name):
    return name.lower().replace("&", "and").replace("'", "").replace(" ", "_")


def fmsg(name):
    return FID.get("msg:" + name) or FID["ask:" + name]


def key_of(name):
    return TRUTH[name]["Ticket"]


def lab(name):
    k = key_of(name)
    return f"{k} ({name})" if k else name


DROP_TXT = {"Hourly Coins": "ZM ROADMAP Backlog list card 68c45bba5d2c25a3a5c26a8c ('Hourly Collection')",
            "Nathan's Treasure Hunt": "Confluence page_liveops_calendar (Nathan's Treasure Hunt is on Domino Delights)",
            "Streak Fever": "Confluence page_liveops_calendar (Streak Fever is on Domino Delights)",
            "Axe Arena": "ZM ROADMAP Oct 21 list card 6851a7a6c31a93809acded72 ('Axe Arena (Win streak multiplier scoring)'), Slack C05KNDCHAAG/1758558164.541689 ('We\u2019ve decided to postpone Axe Arena for the beta release.')"}


def src_txt(name):
    """Evidence text naming the ticket records behind a message's call."""
    k = key_of(name)
    if name in DROP_TXT:
        return DROP_TXT[name]
    if name == "Comeback gift":
        return f"Linear DES-345 comment {COMMENTS['DES-345'][-1]['id']} ('{q(COMMENTS['DES-345'][-1]['body'], 'A reward on tap is a version 2 idea, it isn' + chr(39) + 't in the beta.')}')"
    if name == "Lapsed 14 days":
        return f"Gmail {COV_ID} ('{Q_COV}')"
    if name == "Win & Collect start":
        return f"Linear DES-313 comment {note('DES-313')['id']} ('{cut(note('DES-313')['body'], 90)}')"
    if not k:
        z, c = ZOMC[name]
        return f"Linear {z} comment {c} ('{q(sql_row('linear.linear_comments', {'id': c})['body'], ASK_QUOTE[name])}')"
    n = note(k)
    return f"Linear {k} comment {n['id']} ('{cut(n['body'], 120)}')"


ASK_QUOTE = {"Boss Arena attempts refilled": "can we get a phone reminder once the daily Boss Arena attempts refill?",
             "Daily gift about to reset": "could we also send a phone reminder the evening before the daily gift streak resets?",
             "Teammate sent lives": "could we get a phone message when a teammate sends you lives?",
             "Infinite lives ending": "could we also remind players on their phone when their infinite lives are about to run out?"}
TRAP_SRC = {
    "Lives recharged": ([s_pull, s_qa], f"Slack C0880U9751A/1759245146.720608 ('{Q_PULL}'), Linear DES-315 Vincent's Sep 24 pass "
                        "cmt_51e018b23e18c2f680cd, Gmail QA note", F("msg:Lives recharged", "pull"), "T5"),
    "Plague Race": ([s_qareply, s_qa], f"Slack D06UFE81RF0/1759174846.723833 ('{Q_RACE}'), Gmail QA note ('{Q_TIMERS}')",
                    F("msg:Plague Race", "qa_reply"), "T4"),
    "Weekly Leaderboard reset": ([s_rc18, s_client], f"GitHub PR #248 review comment rc_18 ('{Q_RC18}'), NotificationManager.cs ('{Q_LOOP}')",
                                 F("msg:Weekly Leaderboard reset", "rc18"), "T1"),
    "Finish first mission": ([s_ask, s_askreply], f"Slack C0880U9751A/1759167608.326578 ('{Q_ASK}'), reply C0880U9751A/1759170096.924778 "
                             f"('{Q_POPUP}'), Linear DES-318 audience comment {who('DES-318')['id']} ('{cut(who('DES-318')['body'], 60)}'), "
                             f"rule doc ('{Q_T4}')", F("msg:Finish first mission", "ask", "ask_reply"), "T3"),
}
GO_SRC = ([s_qa, s_pull, s_client], f"NotificationManager.cs ('{Q_DAY1}'; '{Q_BATCH}'), Gmail QA note ('{Q_SEEN}'), Phone message checks "
          f"sheet f_8eb8c04713ff6a6ef4a265 (Sep 24 pass), Slack C0880U9751A/1759245146.720608 ('{Q_STILL}')")

# ================================================================ sheet
add(tag="sheet_folder", t=f"The Agent puts {SHEET_ROW} in {FOLDER_NAME}, created there or moved there", w=1, kind="lookup",
    why="the prompt names the folder and it is Samuel's own Drive root folder", fact="sheet_folder", span=SP_FOLDER,
    oe=oe("folder", "w_sheet", "w_mv1"), fids=F("folder", "hub"), vals=f"`{FOLDER}`", verify="Sheet location", final="Sheet's final parent",
    acc=[f"the Agent's calls sheet has the final parent {FOLDER}, whether created there or moved there"],
    alt="Any other parent fails; a file created there or moved there both pass.", srcs=[s_hub],
    ev=f"Sources: Drive folder {FOLDER} (name {SAM}, owner {SAM}); Leonard's DM {HUB[1]} ('{cut(Q_FOLD, 45)}')", dec="F32", grp="—",
    valid="Sheet created in the root then moved into the folder", idle="No sheet created")
add(tag="sheet_header", t=f"The Agent heads {SHEET_ROW} with the seven columns Message, Ticket, Call, What's missing, Audience, Final headline and "
    "String change (any letter case)", w=1, kind="lookup", why="the seven names are copied from one sentence of Leonard's DM", fact="sheet_header",
    span=SP_JOB, oe=oe("hub", "w_rows"), fids=F("hub"), vals="`What's missing` `String change`", verify="Header row", final="First row of the sheet",
    acc=["a header row with Message, Ticket, Call, What's missing, Audience, Final headline and String change in that order, any letter case"],
    alt="Missing or reordered columns fail; letter case is free.", srcs=[s_hub], ev=f"Source: Leonard's DM {HUB[1]} ('{Q_FOLD}')", dec="F1",
    valid="Header Message, Ticket, Call, What's missing, Audience, Final headline, String change", idle="No sheet created")
add(tag="sheet_rows", t=f"The Agent writes exactly 36 message rows under the header of {SHEET_ROW}, one per message (the PNs Beta rows plus the filed asks)", w=5, kind="multi-source",
    why="the count only comes out of the whole audit: the PN sheet, DES-314's children, DES-313's alias and the comment asks on four ZOM tickets",
    fact="sheet_volume", span=SP_JOB, oe=oe("sheet", "kids", "pop", "ask:Boss Arena attempts refilled", "ask:Daily gift about to reset",
                                            "ask:Teammate sent lives", "ask:Infinite lives ending", "w_rows"),
    fids=F("counts", "sheet", "parent", "pop"), vals="`36`", verify="Row count", final="Rows under the header",
    acc=["exactly 36 data rows under the header, one per message"], alt="32 rows (asks under DES-314 only) fails; so does any added decoy row.",
    srcs=[s_hub, s_zom("Boss Arena attempts refilled")],
    ev=f"Sources: PN sheet f_a325dd4af80afc5994d5dc tab PNs Beta (14 rows), Linear DES-314 (18 asks among its 31 children), Linear ZOM-542, ZOM-556, "
       f"ZOM-563 and ZOM-483 comments (4 asks); Leonard's DM {HUB[1]} ('{Q_SCOPE}')", dec="T7", grp="G1 sheet rows volume",
    valid="36 data rows, one per message", idle="No sheet created")


def sheet_call(name, w, kind, why, srcs, ev, fids, dec, grp, dist="—"):
    v = TRUTH[name]
    add(tag=f"call_{tag(name)}", t=f"The Agent enters {v['Call']} in the Call column of the {lab(name)} row of {SHEET_ROW}", w=w, kind=kind, why=why,
        fact=f"call:{name}", span=SP_JOB, oe=oe("cmts", TEST[name][1], "c7", "w_rows"), fids=fids, vals=f"`{v['Ticket']}` · {v['Call']}",
        verify=f"{name} Call cell", final="Call cell of that row", acc=[f"the row for {v['Ticket']} or {name} has {v['Call']} in the Call column"],
        alt=f"Any other call on that row fails.", srcs=srcs, ev=ev, dec=dec, grp=grp, dist=dist, valid=f"Row {v['Ticket']}: {v['Call']}", idle="No sheet created")


for name in ("Lives recharged", "Plague Race", "Weekly Leaderboard reset", "Finish first mission"):
    srcs, txt, fids, t = TRAP_SRC[name]
    sheet_call(name, 5, "multi-source", f"the {TEST[name][0]} failure joins records in different services against the ticket, the sheet's Ready "
               "status and Vincent's pass", srcs + [s_rule], f"Sources: {txt}; rule doc {RULE[1]} ('{Q_HOLD}')", fids + " F2", t, "direct exception")
for name in ("Lapsed 1 day", "Lapsed 7 days"):
    sheet_call(name, 5, "multi-source", "a Go has to pass all six tests, which join the client code, Vincent's QA note and checks sheet, and his "
               "later Slack post", GO_SRC[0] + [s_rule], f"Sources: {GO_SRC[1]}; rule doc {RULE[1]} ('{Q_GO}')",
               F("msg:" + name, "client", "qa", "log", "pull", "rule"), "H2", "direct (every Go)")
for name, why, ev in (
        ("Axe Arena", "test 1 read against the Oct 21 list of ZM ROADMAP", DROP_TXT["Axe Arena"]),
        ("Hourly Coins", "test 1 read against the Backlog list of ZM ROADMAP", DROP_TXT["Hourly Coins"]),
        ("Streak Fever", "test 1 read against the live-ops page, which puts it on Domino Delights", DROP_TXT["Streak Fever"])):
    sheet_call(name, 3, "interpretation", why, [s_rule], f"Sources: {ev}; rule doc {RULE[1]} ('{Q_T1}')", F("msg:" + name, "rule"), "H1", "G2 Call samples")
for name in ("Login Calendar update", "Quests rollover"):
    sheet_call(name, 3, "interpretation", "test 3 read against Arthur's note on one ticket", [s_rule], f"Sources: {src_txt(name)}; rule doc {RULE[1]} ('{Q_T3}')",
               F("msg:" + name, "rule"), "H1", "G2 Call samples")


def miss(name, text, w, kind, why, srcs, ev, fids, dec, grp, wrong):
    k = key_of(name)
    where = f"the {lab(name)} row of {SHEET_ROW}" if k else f"its row for the ask on {ZOMC[name][0]} ({name}) in {SHEET_ROW}"
    add(tag=f"miss_{tag(name)}", t=f"The Agent records in the What's missing column of {where} {text}", w=w, kind=kind, why=why, fact=f"why:{name}", span=SP_JOB,
        oe=oe(TEST[name][1], "w_rows"), fids=fids, vals=f"`{k or ZOMC[name][0]}` · {TEST[name][0]}", verify=f"{name} What's missing cell", final="What's missing cell of that row",
        acc=[f"the What's missing cell of that row says {text}"], alt=wrong, srcs=srcs, ev=ev, dec=dec, grp=grp, valid=f"{name}: {text}", idle="No sheet created")


T2_TXT = "that it needs a server send (naming test 2, or saying it needs a server)"
T3_TXT = "that the client has yet to schedule it (naming test 3, or saying it isn't scheduled in the client yet)"
M6 = "that it fails test 6, seen on both iOS and Android (naming test 6, or saying {x})"
miss("Lives recharged", M6.format(x="Vincent Parker's tick is off or it failed to arrive on iOS 0.3.49"), 5, "multi-source", "Vincent's Sep 30 post names the headline Full "
     "Ammo, so it has to be tied to the row and set against his Sep 24 pass", [s_pull, s_rule], f"Sources: {TRAP_SRC['Lives recharged'][1]}; rule doc ('{Q_T6}')",
     TRAP_SRC["Lives recharged"][2] + " F2", "T5", "direct exception", "A blank cell, or any other test, fails.")
miss("Plague Race", M6.format(x="the iOS pass was on the 5-minute timers build or it never showed up on the real iOS build"), 5, "multi-source", "Vincent's reply in Samuel's DM "
     "withdraws a pass the checks sheet still shows, and the QA note says a shortened-timer build doesn't count", [s_qareply, s_qa], f"Sources: {TRAP_SRC['Plague Race'][1]}; rule doc ('{Q_T6}')",
     TRAP_SRC["Plague Race"][2] + " F2", "T4", "direct exception", "A blank cell, or any other test, fails.")
miss("Weekly Leaderboard reset", "that it fires on the wrong day (naming test 5, or saying it counts from the last session and misses the weekly reset)", 5, "multi-source",
     "Arthur's review comment on PR #248 has to be read with the code loop against test 5", [s_rc18, s_client], f"Sources: {TRAP_SRC['Weekly Leaderboard reset'][1]}; rule doc ('{Q_T5}')",
     TRAP_SRC["Weekly Leaderboard reset"][2] + " F2", "T1", "direct exception", "A blank cell, or 'passes all six', fails.")
miss("Finish first mission", "that it can't reach its players (naming test 4, or saying its players below level 20 haven't had our own ask, which runs after level 20)", 5, "multi-source",
     "Robert's call and Arthur's reply in Slack have to be read with the ticket's audience and test 4", [s_ask, s_askreply], f"Sources: {TRAP_SRC['Finish first mission'][1]}",
     TRAP_SRC["Finish first mission"][2] + " F2", "T3", "direct exception", "A blank cell, or test 6, fails.")
miss("Lapsed 14 days", "that another message already covers it (naming Lapsed 7 days, DES-317 or the weekly batch)", 5, "multi-source", "the weekly batch's four runs in the code, read with Leonard's "
     "cancellation note, show day 14 is covered, and the rule says to name the message", [s_cov, s_client], f"Sources: Gmail {COV_ID} ('{Q_COV}'), NotificationManager.cs ('{Q_BATCH}'); rule doc ('{Q_DROP}')",
     F("msg:Lapsed 14 days", "covered", "client", "rule"), "T9", "direct exception", "A cell that names no covering message fails.")
for name in ASKS:
    txt = (T2_TXT if name == "Teammate sent lives" else T3_TXT)
    miss(name, txt, 5, "tracing", f"the ask sits in a comment on {ZOMC[name][0]}, off DES-314's children, and the rule is then applied to it",
         [s_zom(name), s_rule], f"Sources: {src_txt(name)}; rule doc ('{Q_T2 if name == 'Teammate sent lives' else Q_T3}')", F("ask:" + name, "pop", "rule"), "T7", "direct exception",
         "A sheet with no row for this ask fails; so does a row naming another test.")
miss("Plague Race result", T2_TXT, 3, "interpretation", "test 2 read against Arthur's note on one ticket", [s_rule],
     f"Sources: {src_txt('Plague Race result')}; rule doc ('{Q_T2}')", F("msg:Plague Race result", "rule"), "H1", "G3 What's missing samples", "A blank cell, or test 3, fails.")
miss("Login Calendar update", T3_TXT, 3, "interpretation", "test 3 read against Arthur's note on one ticket", [s_rule],
     f"Sources: {src_txt('Login Calendar update')}; rule doc ('{Q_T3}')", F("msg:Login Calendar update", "rule"), "H1", "G3 What's missing samples", "A blank cell, or test 2, fails.")


def aud(name, form):
    k = key_of(name)
    if k:
        c = who(k)
        quote, rec, where, fids, dec = cut(c["body"], 70), f"Linear {k} comment {c['id']}", f"the {lab(name)} row of {SHEET_ROW}", F("msg:" + name), fmsg(name)
    else:
        z, cid = ZOMC[name]
        quote, rec, where, fids, dec = q(sql_row("linear.linear_comments", {"id": cid})["body"], "for players on a team"), f"Linear {z} comment {cid}", f"its row for the ask on {z} ({name}) in {SHEET_ROW}", F("ask:" + name), "T7"
    add(tag=f"aud_{tag(name)}", t=f"The Agent enters {form} (any wording with that meaning) in the Audience column of {where}", w=1, kind="lookup",
        why="the audience is copied from the ask's own comment", fact=f"aud:{name}", span=SP_JOB, oe=oe("cmts", "w_rows") if k else oe("ask:" + name, "w_rows"), fids=fids, vals=f"`{k or ZOMC[name][0]}`",
        verify=f"{name} Audience cell", final="Audience cell of that row", acc=[], alt="A different group fails; a plain rewording passes.", srcs=[s_rule] if k else [s_zom(name), s_rule], ev=f"Sources: {rec} ('{quote}'); rule doc ('{Q_AUD}')",
        dec=dec, grp="G4 Audience samples", valid=f"{name}: {form}", idle="No sheet created")


aud("Boss Arena open", "players past the arena unlock")
aud("Plague Race result", "players in a race")
aud("Finish first mission", "new players below level 20")
aud("Win & Collect start", "players on the event")
aud("Teammate sent lives", "players on a team")

add(tag="ticket_wc", t=f"The Agent enters DES-313 (alone or with a title) in the Ticket column of the Win & Collect start row of {SHEET_ROW}", w=5, kind="tracing",
    why="no child of DES-314 has the name; the live-ops page ties Win & Collect to Collect & Win, the name on DES-313", fact="ticket:Win & Collect start", span=SP_JOB,
    oe=oe("liveops", "wc", "w_rows"), fids=F("wc", "liveops"), vals="`DES-313`", verify="Win & Collect Ticket cell", final="Ticket cell of that row",
    acc=["the Win & Collect start row has DES-313 in the Ticket column, alone or with a title"], alt="A new key, or a blank cell, fails.", srcs=[s_hub],
    ev=f"Sources: Confluence page_liveops_calendar ('{Q_ALIAS}'), Linear DES-313 '{ISSUES['DES-313']['title']}', sheet row 7 'Win & Collect event start'; Leonard's DM ('{Q_NEW}')",
    dec="T6", grp="direct exception", dist="T6: no child of DES-314 has the name → graded through the ticket key", valid="Win & Collect start: DES-313", idle="No sheet created")
name, row = "Lapsed 7 days", "Has not played in seven days."
k = key_of(name)
add(tag=f"ticket_{tag(name)}", t=f"The Agent enters {k} (alone or with a title) in the Ticket column of the {name} row of {SHEET_ROW} (the PN sheet's \"{row}\" row)", w=1, kind="lookup",
    why="the ticket's title names the sheet row", fact=f"ticket:{name}", span=SP_JOB, oe=oe("sheet", "kids", "w_rows"), fids=F("msg:" + name, "sheet"), vals=f"`{k}`",
    verify=f"{name} Ticket cell", final="Ticket cell of that row", acc=[], alt="Another key fails.", srcs=[s_hub],
    ev=f"Sources: Linear {k} '{ISSUES[k]['title']}', PN sheet f_a325dd4af80afc5994d5dc row '{row}'", dec=fmsg(name), grp="G5 Ticket samples", valid=f"{name}: {k}", idle="No sheet created")
add(tag="ticket_teammate_sent_lives", t=f"The Agent enters the key of its new ticket for the ask on ZOM-563 (Teammate sent lives) in the Ticket column of that ask's row of {SHEET_ROW}", w=3, kind="comparison",
    why="the row has to take the new ticket's key, not ZOM-563, the ticket holding the comment", fact="ticket:Teammate sent lives", span=SP_JOB, oe=oe("w_new:Teammate sent lives", "w_rows"), fids=F("ask:Teammate sent lives"), vals="`ZOM-563`",
    verify="Teammate sent lives Ticket cell", final="Ticket cell of that row", acc=[], alt="ZOM-563 in the cell fails; the new key alone or with a title passes.", srcs=[s_zom("Teammate sent lives")],
    ev=f"Sources: {src_txt('Teammate sent lives')}; Leonard's DM ('{Q_NEW}')", dec="T7", grp="G5 Ticket samples", valid="Teammate sent lives: its new key", idle="No sheet created")

add(tag="head_l7", t=f"The Agent enters \"Your Squad Is Waiting\" (with or without an emoji) in the Final headline column of the DES-317 (Lapsed 7 days) row of {SHEET_ROW}", w=5, kind="multi-source",
    why="Leonard's calendar note replaces his Slack line, which replaced the client's title", fact="headline:Lapsed 7 days", span=SP_JOB, oe=oe("line2", "line3", "c7", "w_rows"),
    fids=F("line_v3", "line_v2", "msg:Lapsed 7 days"), vals="`Your Squad Is Waiting`", verify="Lapsed 7 days Final headline", final="Final headline cell",
    acc=["that row's Final headline is Your Squad Is Waiting, with or without an emoji"], alt="\"Your Squad Needs You Back\" (the replaced line) or the client's line fails.",
    srcs=[s_line3, s_line2], ev=f"Sources: Calendar {EVT} ('{Q_LINE3}'), Slack C08R8CHB0QL/1759169129.445834 ('{Q_LINE2}'); rule doc ('{Q_LATEST}')", dec="T2", grp="direct (every Go)",
    dist="T2: Leonard's Sep 29 line → graded through the later line", valid="Your Squad Is Waiting", idle="No sheet created")
add(tag="head_l1", t=f"The Agent enters \"The Horde Is Growing…\" (with or without its emoji) in the Final headline column of the DES-316 (Lapsed 1 day) row of {SHEET_ROW}", w=1, kind="lookup",
    why="the line is copied from the client's title", fact="headline:Lapsed 1 day", span=SP_JOB, oe=oe("client", "c7", "w_rows"), fids=F("msg:Lapsed 1 day", "client"), vals="`The Horde Is Growing`",
    verify="Lapsed 1 day Final headline", final="Final headline cell", acc=["that row's Final headline is The Horde Is Growing…, with or without its emoji"], alt="Another line fails.",
    srcs=[s_client], ev="Sources: PN sheet f_a325dd4af80afc5994d5dc row 4 and NotificationManager.cs title 'The Horde Is Growing… 🧟‍♂️'", dec="F43", grp="direct (every Go)",
    valid="The Horde Is Growing…", idle="No sheet created")
add(tag="str_l7", t=f"The Agent records in the String change column of the DES-317 (Lapsed 7 days) row of {SHEET_ROW} that the line changes (Yes, the string ticket's key, or any wording with that meaning)", w=3, kind="comparison",
    why="the final line is compared with what the client ships", fact="string:Lapsed 7 days", span=SP_JOB, oe=oe("client", "c7", "w_rows"), fids=F("msg:Lapsed 7 days", "client", "rule"), vals="`DES-317` · Yes",
    verify="Lapsed 7 days String change", final="String change cell", acc=["that row's String change cell says Yes, alone or with a reason or ticket key"], alt="No, or a blank cell, fails.", srcs=[s_rule, s_client],
    ev=f"Sources: NotificationManager.cs title 'They’ve Taken Over… Can You Stop Them? 😱'; rule doc ('{Q_STR}')", dec="F44", grp="direct (every Go)", valid="Yes - DES-346", idle="No sheet created")
add(tag="str_l1", t=f"The Agent records in the String change column of the DES-316 (Lapsed 1 day) row of {SHEET_ROW} that the line stays as the client ships it (No, None, unchanged, or any wording with that meaning)", w=3, kind="comparison",
    why="the final line is compared with what the client ships, and emoji don't count", fact="string:Lapsed 1 day", span=SP_JOB, oe=oe("client", "c7", "w_rows"), fids=F("msg:Lapsed 1 day", "client", "rule"),
    vals="`DES-316` · No", verify="Lapsed 1 day String change", final="String change cell", acc=["that row's String change cell says No or None, alone or with a reason"], alt="Yes fails.", srcs=[s_rule, s_client],
    ev=f"Sources: NotificationManager.cs title 'The Horde Is Growing… 🧟‍♂️'; rule doc ('{q(RULE_TXT, chr(69) + 'moji don' + chr(39) + 't count as a different line.')}')", dec="F43", grp="direct (every Go)", valid="No", idle="No sheet created")
add(tag="head_count", t=f"The Agent fills the Final headline column on exactly two rows of {SHEET_ROW}", w=3, kind="comparison", why="the rule keeps the column to Go rows, so the count follows from the Call column",
    fact="headline_scope", span=SP_JOB, oe=oe("c7", "w_rows"), fids=F("rule", "counts"), vals="`Final headline`", verify="Rows with a Final headline", final="Final headline column",
    acc=[], alt="A headline on a Hold or Drop row makes three.", srcs=[s_rule], ev=f"Source: rule doc {RULE[1]} ('{Q_ONLYGO}')", dec="H1", grp="G1 sheet volume", valid="Headlines on Lapsed 1 day and Lapsed 7 days only", idle="No sheet created")
add(tag="str_count", t=f"The Agent fills the String change column on exactly two rows of {SHEET_ROW}", w=3, kind="comparison", why="the rule keeps the column to Go rows, so the count follows from the Call column",
    fact="string_scope", span=SP_JOB, oe=oe("c7", "w_rows"), fids=F("rule", "counts"), vals="`String change`", verify="Rows with a String change", final="String change column",
    acc=[], alt="A String change on a Hold or Drop row makes three.", srcs=[s_rule], ev=f"Source: rule doc {RULE[1]} ('{Q_ONLYGO}')", dec="H1", grp="G1 sheet volume", valid="String change on Lapsed 1 day and Lapsed 7 days only", idle="No sheet created")
EVID_COUNTS = "the calls on DES-313 and DES-315 to DES-345 (Linear) and on the asks in comments on ZOM-542, ZOM-556, ZOM-563 and ZOM-483"
for call, n in (("Go", 2), ("Hold", 28), ("Drop", 6)):
    add(tag=f"tally_{call.lower()}", t=f"The Agent enters {call} in the Call column of exactly {n} rows of {SHEET_ROW}", w=5, kind="multi-source", why=f"the {call} count comes out of all 36 calls", fact=f"count_{call.lower()}", span=SP_JOB, oe=oe("c7", "w_rows"), fids=F("counts", "rule"), vals=f"`{n}` · {call}",
        verify=f"{call} rows in the Call column", final="Call column", acc=[], alt="A count off by any row fails.", srcs=[s_rule], ev=f"Sources: {EVID_COUNTS}; rule doc ('{Q_GO if call == 'Go' else Q_HOLD if call == 'Hold' else Q_DROP}')", dec="T7" if call == "Hold" else "H1", grp="G1 sheet volume", valid=f"{n} rows called {call}", idle="No sheet created")

# ================================================================ note
add(tag="note_folder", t=f"The Agent puts {NOTE} for the team in {FOLDER_NAME}, created there or moved there", w=1, kind="lookup", why="the prompt names the folder", fact="note_folder", span=SP_FOLDER,
    oe=oe("folder", "w_note", "w_mv2"), fids=F("folder", "hub"), vals=f"`{FOLDER}`", verify="Note location", final="Note's final parent",
    acc=[f"the Agent's note has the final parent {FOLDER}, whether created there or moved there"], alt="Any other parent fails.", srcs=[s_hub],
    ev=f"Sources: Drive folder {FOLDER}; Leonard's DM {HUB[1]} ('{cut(Q_NOTE, 50)}')", dec="F32", valid="Note created then moved into the folder", idle="No note created")
add(tag="note_page", t="The Agent keeps its note for the team to one page", w=1, kind="lookup", why="a length the prompt states", fact="note_page", span=SP_FOLDER, oe=oe("w_note"), fids=F("hub"), vals="`one-page`",
    verify="Note length", final="Note body", acc=["a note whose body would fit on one printed page"], alt="A multi-page note fails; layout is free.", srcs=[s_hub],
    ev=f"Sources: the prompt ('the one-page note'); Leonard's DM {HUB[1]} ('{cut(Q_NOTE, 50)}')", dec="F1", valid="A note of about 500 words", idle="No note created")
add(tag="note_first", t=f"The Agent orders {NOTE} as the D1 and D7 figures, then the lapsed reminders, then the Holds (a title or short lead-in may come first)", w=1, kind="lookup",
    why="the order is stated in one sentence of Leonard's DM", fact="note_order", span=SP_JOB, oe=oe("w_note"), fids=F("hub"), vals="`D1` `D7`", verify="Order of the note's parts", final="Note body",
    acc=["the D1 and D7 figures come before the lapsed reminders and the Holds"], alt="Figures after the other parts fail; a title or lead-in passes.", srcs=[s_hub], ev=f"Source: Leonard's DM {HUB[1]} ('{Q_NOTE}')", dec="F1",
    valid="Title, then D1 and D7, then reminders, then Holds", idle="No note created")
WHROW = {"ios": 237, "android": 236}
for plat, label, col, val, alts in (("ios", "iOS", "D1", "31.65", "31.7% or 31.6%"), ("ios", "iOS", "D7", "9.28", "9.3%"), ("android", "Android", "D1", "37.86", "37.9%"), ("android", "Android", "D7", "10.68", "10.7%")):
    got = get_json("snowflake", "snowflake.json", f"/tables/10/rows/{WHROW[plat]}/{col.lower()}_ret")
    assert str(got) == val, (got, val)
    add(tag=f"note_{plat}_{col.lower()}", t=f"The Agent gives {label} {col} for the Sep 15 cohort week as {val}% ({alts} when rounded, with or without the % sign) in {NOTE}", w=1, kind="lookup", why="one value read off one warehouse row", fact=f"wh:{plat}:{col}",
        span=SP_JOB, oe=oe("whd", "wh", "w_note"), fids=F("wh"), vals=f"`{val}`", verify=f"{label} {col}", final="Note body", acc=[f"{label} {col} given as {val}% or {alts}, with or without the % sign"],
        alt="The other platform's figure, a pooled figure or another cohort week fails.", srcs=[s_hub],
        ev=f"Source: Snowflake ANALYTICS.GAME_EVENTS.USER_COHORT_RETENTION, game_id zombie_match_3d, cohort_week 2025-09-15, platform {plat}, {col.lower()}_ret {val}; Leonard's DM {HUB[1]} ('{cut(Q_NOTE, 120)}')", dec="F30", valid=f"{label} {col} {val}%", idle="No note created")
add(tag="note_ladder", t=f"The Agent lists the lapsed reminders the client schedules in {NOTE} as going out on days 1, 7, 14, 21 and 28 after the last session", w=3, kind="calculation", why="the days are worked out from the two scheduling calls and the loop in one file",
    fact="ladder", span=SP_JOB, oe=oe("client", "w_note"), fids=F("client"), vals="`AddDays(i * 7)`", verify="Lapsed reminder days", final="Note body", acc=["the note gives the lapsed reminders' days as 1, 7, 14, 21 and 28"], alt="A list stopping at day 7, or adding days 3 or 30, fails.",
    srcs=[s_client], ev=f"Source: NotificationManager.cs ('{Q_DAY1}'; '{Q_BATCH}'; '{Q_LOOP}')", dec="F16", valid="Day 1, then days 7, 14, 21 and 28", idle="No note created")


ALT_NAME = {"Lives recharged": "Full Ammo Reloaded!", "Plague Race": "Plague Race Is On!", "Weekly Leaderboard reset": "Weekly Rankings Reset!", "Finish first mission": "Finish Your First Mission!"}


def note_hold(name, text, srcs, ev, fids, dec):
    add(tag=f"nh_{tag(name)}", t=f"The Agent gives the reason {name} (or {ALT_NAME[name]}) is still a Hold in {NOTE}: {text}", w=5, kind="multi-source", why="the reason joins the same records as the call, and the note has to name it among what the client already schedules",
        fact=f"why:{name}", span=SP_JOB, oe=oe("client", TEST[name][1], "w_note"), fids=fids, vals=f"`{key_of(name)}` · {TEST[name][0]}", verify=f"{name} in the note's Holds", final="Note body", acc=[f"the note says {name} is still a Hold because {text}"],
        alt="Leaving it out, or calling it ready, fails.", srcs=srcs, ev=ev, dec=dec, grp="direct (the four Holds the client schedules)", valid=f"{name}: {text}", idle="No note created")


note_hold("Lives recharged", "it fails test 6, seen on both iOS and Android (naming test 6, or saying Vincent Parker's tick is off or it failed to arrive on iOS 0.3.49)", [s_pull, s_rule], f"Sources: {TRAP_SRC['Lives recharged'][1]}; rule doc ('{Q_T6}')", TRAP_SRC["Lives recharged"][2] + " F2 F16", "T5")
note_hold("Plague Race", "it fails test 6, seen on both iOS and Android (naming test 6, or saying the iOS pass was on the 5-minute timers build or it never showed up on the real iOS build)", [s_qareply, s_rule], f"Sources: {TRAP_SRC['Plague Race'][1]}; rule doc ('{Q_T6}')", TRAP_SRC["Plague Race"][2] + " F2 F16", "T4")
note_hold("Weekly Leaderboard reset", "it fires on the wrong day (naming test 5, or saying it counts from the last session and misses the weekly reset)", [s_rc18, s_rule], f"Sources: {TRAP_SRC['Weekly Leaderboard reset'][1]}; rule doc ('{Q_T5}')", TRAP_SRC["Weekly Leaderboard reset"][2] + " F2 F16", "T1")
note_hold("Finish first mission", "it can't reach its players (naming test 4, or saying its players below level 20 haven't had our own ask, which runs after level 20)", [s_ask, s_askreply], f"Sources: {TRAP_SRC['Finish first mission'][1]}", TRAP_SRC["Finish first mission"][2] + " F2 F16", "T3")
add(tag="note_count", t=f"The Agent names exactly four messages in {NOTE} as scheduled by the client and still a Hold", w=5, kind="multi-source", why="the count needs all four failures found among the six calls the client makes", fact="note_holds_volume", span=SP_JOB,
    oe=oe("client", "c4", "c5", "c6", "w_note"), fids=F("client", "msg:Lives recharged", "msg:Plague Race", "msg:Weekly Leaderboard reset", "msg:Finish first mission"), vals="`4`", verify="Count of client-scheduled Holds", final="Note body",
    acc=["the note's list of messages the client schedules that are still on Hold has exactly four members"], alt="Three (one passed as Go) or five fails.", srcs=[s_client, s_hub], ev=f"Sources: NotificationManager.cs (six scheduling calls; two Go, four Hold); Leonard's DM ('{q(Q_NOTE, "anything the client already schedules that" + chr(39) + "s still a Hold and why")}')",
    dec="H1", grp="G6 note volume", valid="Lives recharged, Plague Race, Finish first mission and Weekly Leaderboard reset", idle="No note created")

# ================================================================ ticket comments
BOSS = ("Boss Arena open", "Boss Arena last hours")
for name, v in ITEMS:
    k = v["Ticket"]
    if not k:
        continue
    if name in TRAP_SRC:
        srcs, txt, fids, dec = TRAP_SRC[name]
        w, kind, why = 5, "multi-source", f"the {TEST[name][0]} failure joins records in different services"
        srcs, ev, fids = srcs + [s_rule], f"Sources: {txt}", fids + " F2"
    elif v["Call"] == "Go":
        w, kind, why, dec = 5, "multi-source", "a Go has to pass all six tests, which join the code, the QA note, the checks sheet and Slack", "H2"
        srcs, ev, fids = GO_SRC[0] + [s_rule], f"Sources: {GO_SRC[1]}", F("msg:" + name, "client", "qa", "log", "pull", "rule")
    elif name == "Win & Collect start":
        w, kind, why, dec = 5, "tracing", "the ticket has no parent and another name, so it is found through the live-ops page before test 3 is read", "T6"
        srcs, ev, fids = [s_rule], f"Sources: {src_txt(name)}, Confluence page_liveops_calendar ('{Q_ALIAS}'); rule doc ('{Q_T3}')", F("msg:" + name, "wc", "liveops", "rule")
    elif name == "Lapsed 14 days":
        w, kind, why, dec = 5, "multi-source", "the weekly batch in the code, read with Leonard's cancellation note, covers day 14", "T9"
        srcs, ev, fids = [s_cov, s_rule], f"Sources: Gmail {COV_ID} ('{Q_COV}'), NotificationManager.cs ('{Q_BATCH}'); rule doc ('{Q_DROP}')", F("msg:" + name, "covered", "client", "rule")
    elif name in BOSS:
        w, kind, why, dec = 5, "tracing", "Boss Arena's place in the beta rests on tying ZOM-487 to the BETA list's Infinite HP Boss Mode, before test 3 is read on the ticket", "H1"
        srcs, ev, fids = [s_rule], f"Sources: {src_txt(name)}, Linear ZOM-487 'Infinite HP Boss Arena', ZM ROADMAP card 'Infinite HP Boss Mode'; rule doc ('{Q_T3}')", F("msg:" + name, "livefeat", "rule")
    else:
        t = TEST[name][0]
        rq = {"test 1": Q_T1, "test 2": Q_T2, "test 3": Q_T3}[t]
        w, kind, why, dec = 3, "interpretation", (f"{t} of the rule read against the roadmap, the live-ops page or the ticket" if t == "test 1" else f"{t} of the rule read against one ticket's note"), "H1"
        srcs, ev, fids = [s_rule], f"Sources: {src_txt(name)}; rule doc ('{rq}')", F("msg:" + name, "rule")
    add(tag=f"cm_{tag(name)}", t=f"The Agent comments on {k} ({name}) with the call {v['Call']} (any wording carrying that call)", w=w, kind=kind, why=why, fact=f"call:{name}", span=SP_TICKETS,
        oe=oe("cmts", TEST[name][1], "wc:" + name), fids=fids, vals=f"`{k}` · {v['Call']}", verify=f"{k} comment", final=f"Comment on {k}", acc=[f"a comment on {k} that gives the call {v['Call']}, in any wording"],
        alt=f"A comment giving another call fails; so does no comment.", srcs=srcs, ev=ev, dec=dec, grp="G7 ticket comments (one row each)", valid=f"Comment on {k}: {v['Call']}, test or reason in any wording", idle=f"No comment on {k}",
        dist=(f"{TRAPS[name]}: graded through the call on the ticket" if name in TRAPS else "—"))
for name in ASKS:
    t = "test 2" if name == "Teammate sent lives" else "test 3"
    add(tag=f"cm_{tag(name)}", t=f"The Agent comments on its new ticket for the ask on {ZOMC[name][0]} ({name}) with the call Hold (any wording carrying that call)", w=5, kind="tracing", why=f"the ask sits in a comment on {ZOMC[name][0]}, off DES-314's children, then {t} is applied",
        fact=f"call:{name}", span=SP_TICKETS, oe=oe("ask:" + name, TEST[name][1], "w_new:" + name, "w_newc:" + name), fids=F("ask:" + name, "pop", "rule"), vals=f"`{ZOMC[name][0]}` · Hold", verify=f"Call on the new {name} ticket", final="Comment on the new ticket",
        acc=[f"the new ticket for the {name} ask carries the call Hold, in a comment or in its description"], alt="A new ticket with no comment, or no ticket, fails.", srcs=[s_zom(name), s_rule], ev=f"Sources: {src_txt(name)}; rule doc ('{Q_T2 if t == 'test 2' else Q_T3}')", dec="T7", grp="G7 ticket comments (one row each)",
        valid="New ticket with a comment saying Hold", idle="No ticket created")
add(tag="cm_count", t="The Agent leaves call comments on exactly 32 existing Design tickets, DES-313 and DES-315 to DES-345 (a comment on a ZOM ticket aside)", w=5, kind="tracing", why="DES-313 has to be added to the 31 children of DES-314, and DES-314 itself and the ZOM tickets stay out", fact="comment_volume", span=SP_TICKETS, oe=oe("kids", "wc", "wc:Win & Collect start", "wc:Comeback gift"),
    fids=F("parent", "wc"), vals="`DES-313` `DES-345`", verify="Count of existing tickets carrying a call", final="Comments on existing tickets", acc=["call comments on exactly 32 existing tickets, DES-313 and DES-315 to DES-345; a comment that only points to a new ticket is no call comment"], alt="A call left on DES-314 or a ZOM ticket instead fails.",
    srcs=[s_hub], ev=f"Sources: Linear DES-314 (31 children), DES-313; Leonard's DM ('{Q_CMT}')", dec="T6", grp="G7 ticket comments (volume)", valid="One call comment on each of the 32 tickets", idle="No comment made")

# ================================================================ moves


def move(name, state, w, kind, why, dec, grp, frm):
    k = key_of(name)
    end = f"to {state}"
    fids = F("msg:" + name, "freeze", "rule") if state == "Backlog" else F("msg:" + name, "rule")
    src = [s_tech, s_rule] if state == "Backlog" else [s_rule]
    ev = (f"Sources: Trello card {TECH} 'Fix TECH ISSUES' ('{Q_FREEZE}'; action 68dae8c7d95e24b55b69bf80); rule doc ('{Q_MOVE}'); {k} state {frm}" if state == "Backlog"
          else f"Sources: rule doc ('{Q_MOVE}'); {k} state {frm}")
    add(tag=f"mv_{tag(name)}", t=f"The Agent moves {k} ({name}) from {frm} {end}", w=w, kind=kind, why=why, fact=f"state:{name}", span=SP_TICKETS, oe=oe("freeze", "wm:" + name), fids=fids, vals=f"`{k}` · {state}",
        verify=f"{k} state", final=f"{k} state and assignee", acc=[f"{k} ends in {state}" + (" with no assignee" if state == "Backlog" else "")], alt=("Todo (the rule doc's default, which the roadmap card overrides) fails." if state == "Backlog" else "Any other state fails."),
        srcs=src, ev=ev, dec=dec, grp=grp, valid=f"{k} {state}", idle=f"{k} left {frm}", dist=("T8: the rule doc's Todo → graded through Backlog" if state == "Backlog" else "—"))


for name, frm in (("Lives recharged", "Done"), ("Plague Race", "Done"), ("Weekly Leaderboard reset", "Done"), ("Finish first mission", "Done")):
    move(name, "Backlog", 5, "multi-source", f"the move rests on the {TEST[name][0]} failure and on the roadmap card that overrides Todo", TRAP_SRC[name][3], "direct exception", frm)
move("Win & Collect start", "Backlog", 5, "tracing", "the ticket is found through the live-ops page, and the roadmap card overrides Todo", "T6", "direct exception", "In Review")
move("Lapsed 14 days", "Canceled", 5, "multi-source", "the Drop rests on the weekly batch and Leonard's cancellation note", "T9", "direct exception", "In Review")
for name in ("Quests rollover", "Season Pass start", "Endless weekly result"):
    move(name, "Backlog", 3, "comparison", "the rule's Todo is compared with the later roadmap card", "T8", "G8 move samples", "In Review")
for name in ("Hourly Coins", "Comeback gift"):
    move(name, "Canceled", 3, "interpretation", "a Drop under test 1 goes to Canceled by the rule", "H1", "G8 move samples", "In Review")
add(tag="mv_backlog", t="The Agent moves exactly 24 existing tickets to Backlog (the Hold tickets among DES-313 and DES-315 to DES-345)", w=5, kind="multi-source", why="the count comes out of all the calls, and the card overrides Todo", fact="state_backlog_volume", span=SP_TICKETS, oe=oe("freeze", "c7", "wm:Win & Collect start", "wm:Lapsed 30 days"),
    fids=F("counts", "freeze"), vals="`24`", verify="Count of tickets moved to Backlog", final="States of DES-313 and DES-315 to DES-345", acc=[], alt="A Go ticket moved, or a Hold ticket left in place, breaks the count.", srcs=[s_tech, s_rule],
    ev=f"Sources: Trello card {TECH} ('{Q_FREEZE}'); rule doc ('{Q_MOVE}')", dec="T8", grp="G8 moves (volume)", valid="24 Hold tickets in Backlog", idle="No ticket moved")
add(tag="mv_cancel", t="The Agent moves exactly 6 existing tickets to Canceled (the Drop tickets among DES-315 to DES-345)", w=5, kind="multi-source", why="the count comes out of test 1 and the covered Lapsed 14 days", fact="state_cancel_volume", span=SP_TICKETS, oe=oe("c1", "c3", "wm:Hourly Coins", "wm:Comeback gift"), fids=F("counts", "rule"), vals="`6`",
    verify="Count of tickets moved to Canceled", final="States of DES-315 to DES-345", acc=[], alt="A Hold ticket canceled, or a Drop ticket left in place, breaks the count.", srcs=[s_rule], ev=f"Source: rule doc ('{Q_MOVE}')", dec="H1", grp="G8 moves (volume)", valid="DES-324, DES-325, DES-326, DES-327, DES-344 and DES-345 in Canceled", idle="No ticket moved")
add(tag="mv_total", t="The Agent changes the state of exactly 30 of the tickets DES-313 and DES-315 to DES-345", w=5, kind="multi-source", why="Go tickets stay as they are, so the count is the 32 tickets less the two Go", fact="state_total_volume", span=SP_TICKETS, oe=oe("c7", "wm:Win & Collect start", "wm:Comeback gift"), fids=F("counts", "rule"), vals="`30`",
    verify="Count of tickets whose state changed", final="States of DES-313 and DES-315 to DES-345", acc=[], alt="A Go ticket moved to any state makes 31.", srcs=[s_rule], ev=f"Source: rule doc ('{Q_MOVE}')", dec="H1", grp="G8 moves (volume)", valid="The 30 Hold and Drop tickets moved, DES-316 and DES-317 as they were", idle="No ticket moved")
add(tag="mv_unassign", t="The Agent clears the assignee on exactly 24 of the tickets DES-313 and DES-315 to DES-345", w=3, kind="comparison", why="the roadmap card's 'unassigned' is read with the Hold tickets, which all carry an assignee", fact="unassign_volume", span=SP_TICKETS, oe=oe("freeze", "wm:Win & Collect start", "wm:Lapsed 30 days"), fids=F("freeze", "counts"), vals="`unassigned`",
    verify="Count of tickets unassigned", final="Assignees of DES-313 and DES-315 to DES-345", acc=[], alt="A state-only move leaves the assignee and fails.", srcs=[s_tech], ev=f"Source: Trello card {TECH} 'Fix TECH ISSUES' ('{Q_FREEZE}'; action 68dae8c7d95e24b55b69bf80)", dec="T8", grp="G8 moves (volume)", valid="The 24 Hold tickets unassigned", idle="No ticket moved")

# ================================================================ new tickets
add(tag="new_string", t="The Agent creates a ticket under DES-314 for the Lapsed 7 days string change, carrying the line \"Your Squad Is Waiting\" in its title or description (any state or assignee)", w=5, kind="multi-source", why="the line is the later of Leonard's two calls, and the rule asks for a string ticket under the parent", fact="string_ticket", span=SP_TICKETS, oe=oe("line3", "c7", "w_str"), fids=F("line_v3", "line_v2", "parent", "rule"),
    vals="`Your Squad Is Waiting`", verify="String ticket", final="New ticket with parent DES-314", acc=["a new ticket with parent DES-314 whose title or description carries Your Squad Is Waiting; any state, any assignee"], alt="A string ticket carrying \"Your Squad Needs You Back\" fails; its state and assignee are ungraded.", srcs=[s_line3, s_rule],
    ev=f"Sources: Calendar {EVT} ('{Q_LINE3}'); rule doc ('{Q_STR}')", dec="T2", dist="T2: Leonard's Sep 29 line → graded through the later line", valid="New child of DES-314 titled String: Lapsed 7 days, Your Squad Is Waiting", idle="No ticket created")
for name in ASKS:
    z = ZOMC[name][0]
    add(tag=f"new_{tag(name)}", t=f"The Agent creates a new ticket for the ask on {z} for {ASK_WORD[name]} (any title, any team)", w=5, kind="tracing", why=f"the ask sits in a comment on {z}, off the parent's children", fact=f"ask_ticket:{name}", span=SP_TICKETS, oe=oe("pop", "ask:" + name, "w_new:" + name), fids=F("ask:" + name, "pop"), vals=f"`{z}`",
        verify=f"New ticket for {name}", final="New ticket", acc=[f"a new ticket for that message, any title, in Design or Zombie Match 3D"], alt="No ticket, or a ticket for another message, fails.", srcs=[s_zom(name)], ev=f"Sources: {src_txt(name)}; Leonard's DM ('{Q_NEW}')", dec="T7", grp="direct exception", valid=f"Ticket titled PN: {name}", idle="No ticket created",
        dist="T7: the ask list looks complete at DES-314's children → graded through the new ticket")
add(tag="new_count", t="The Agent creates exactly five new tickets for the job (its ask tickets and its string ticket)", w=5, kind="multi-source", why="the count needs the four asks found and DES-313 seen as Win & Collect's ticket, so no second one is opened", fact="new_ticket_volume", span=SP_TICKETS, oe=oe("wc", "pop", "w_str", "w_new:Infinite lives ending"), fids=F("wc", "pop", "rule"), vals="`5`",
    verify="Count of new tickets", final="New Linear tickets", acc=[], alt="A second ticket for Win & Collect makes six; missing the asks leaves one.", srcs=[s_hub, s_zom("Teammate sent lives")], ev=f"Sources: Linear DES-313, ZOM-542, ZOM-556, ZOM-563, ZOM-483; Leonard's DM ('{Q_NEW}')", dec="T6", grp="G9 new tickets (volume)", valid="Four ask tickets and one string ticket", idle="No ticket created")
add(tag="new_state", t="The Agent files exactly four new ask tickets in Backlog, unassigned", w=3, kind="comparison", why="the asks are Holds, and the roadmap card puts held tickets in Backlog, unassigned", fact="new_state_volume", span=SP_TICKETS, oe=oe("freeze", "w_new:Boss Arena attempts refilled", "w_new:Infinite lives ending"), fids=F("freeze", "pop"), vals="`Backlog`",
    verify="State of the new ask tickets", final="New Linear tickets", acc=[], alt="A new ask ticket in Todo fails.", srcs=[s_tech, s_zom("Boss Arena attempts refilled")], ev=f"Sources: Trello card {TECH} ('{Q_FREEZE}'); Linear ZOM-542, ZOM-556, ZOM-563, ZOM-483 comments", dec="T7", grp="G9 new tickets (volume)", valid="Four new tickets in Backlog with no assignee", idle="No ticket created")

# ================================================================ checklist
CARD = f"the Push Notifications card on ZM ROADMAP ({PNCARD})"
CHK = {"Lapsed 1 day": 'DES-316, Lapsed 1 day, the PN sheet\'s "Has not played in 24 hours" or The Horde Is Growing…', "Lapsed 7 days": 'DES-317, Lapsed 7 days, the PN sheet\'s "Has not played in seven days." or Your Squad Is Waiting'}
for name in ("Lapsed 1 day", "Lapsed 7 days"):
    add(tag=f"chk_{tag(name)}", t=f"The Agent adds {name} (named by {CHK[name]}) as an item on a checklist on {CARD}", w=5, kind="multi-source", why="the item is a Go, which only the six tests produce, and the card is named by the prompt", fact=f"checklist:{name}", span=SP_CHECK, oe=oe("pncard", "w_chk", "w_i1" if name == "Lapsed 1 day" else "w_i2"), fids=F("msg:" + name, "pncard", "rule"), vals=f"`{PNCARD}` `{name}`",
        verify=f"Checklist item {name}", final="Checklist on the card", acc=[f"a check item naming {name} (or {key_of(name)}) on a checklist on card {PNCARD}"], alt="An item on another card fails.", srcs=[s_pncard, s_rule], ev=f"Sources: Trello card {PNCARD} (Leonard's comment 68d415a716abcb84070a8e2a), {GO_SRC[1]}; Leonard's DM ('{Q_GOLIST}')", dec="H2", grp="direct (every Go)", valid=f"Check item: {name}", idle="No checklist created")
add(tag="chk_count", t=f"The Agent puts exactly two items on its checklist on {CARD}", w=5, kind="multi-source", why="the count is the Go set, which only the six tests produce", fact="checklist_volume", span=SP_CHECK, oe=oe("c7", "w_i1", "w_i2"), fids=F("pncard", "counts"), vals="`2`", verify="Checklist item count", final="Checklist on the card", acc=["exactly two check items on that checklist"], alt="A Hold message on the checklist makes three.",
    srcs=[s_pncard, s_rule], ev=f"Sources: Trello card {PNCARD}; Leonard's DM ('{Q_GOLIST}'); rule doc ('{Q_GO}')", dec="H1", grp="G10 checklist (volume)", valid="Lapsed 1 day and Lapsed 7 days", idle="No checklist created")

# ================================================================ emails
ASKERS = {}
for name, v in ITEMS:
    for g in v["groups"]:
        if g.startswith("asker_"):
            ASKERS.setdefault(g[6:], []).append(name)
ASKERS.setdefault("calvin", []).append("Win & Collect start")
for p, names in ASKERS.items():
    nm, em, _ = PEOPLE[p]
    for name in names:
        v = TRUTH[name]
        call = v["Call"]
        say = {"Hold": "on Hold (held, or any wording with that meaning)", "Drop": "a Drop (dropped or canceled, or any wording with that meaning)"}[call]
        what = f"{v['Ticket']} ({name}, by key or name)" if v["Ticket"] else f"the ask on {ZOMC[name][0]} ({name})"
        if name in ASKS:
            w, kind, why, dec, srcs, fids = 5, "tracing", "the ask sits in a comment on a ZOM ticket, and the asker comes from that comment", "T7", [s_zom(name), S_CONTACT[p]], F("ask:" + name, "pop") + " " + WHO_FID[p]
        elif name == "Lapsed 14 days":
            w, kind, why, dec, srcs, fids = 5, "multi-source", "the Drop rests on the weekly batch and Leonard's cancellation note", "T9", [s_cov, S_CONTACT[p]], F("msg:" + name, "covered") + " " + WHO_FID[p]
        elif name == "Win & Collect start":
            w, kind, why, dec, srcs, fids = 5, "tracing", "DES-313 sits outside DES-314's children under another name, and Calvin Price filed it", "T6", [S_CONTACT[p], s_rule], F("msg:" + name, "wc") + " " + WHO_FID[p]
        elif name in BOSS:
            w, kind, why, dec, srcs, fids = 5, "tracing", "Boss Arena's place in the beta rests on tying ZOM-487 to the BETA list's Infinite HP Boss Mode", "H1", [S_CONTACT[p], s_rule], F("msg:" + name, "livefeat") + " " + WHO_FID[p]
        else:
            w, kind, why, dec, srcs, fids = 3, "interpretation", f"{TEST[name][0]} of the rule applied to that ask, with the address from Contacts", "H1", [S_CONTACT[p], s_rule], F("msg:" + name, "rule") + " " + WHO_FID[p]
        add(tag=f"em_{p}_{tag(name)}", t=f"The Agent emails {nm} ({em}) that {what} is {say}", w=w, kind=kind, why=why, fact=f"call:{name}", span=SP_MAIL, oe=oe("addr", "wmail:" + em.split("@")[0]), fids=fids, vals=f"`{v['Ticket'] or ZOMC[name][0]}` · {em} · {call}", verify=f"{nm} told about {name}", final=f"Sent email to {em}",
            acc=[], alt="A draft, or an email giving another call, fails.", srcs=srcs, ev=f"Sources: {src_txt(name)}, Contacts {em}; Leonard's DM ('{Q_MAIL}')", dec=dec, grp="G11 asker emails (one row per ask)", valid=f"Email to {em}: {name}: {call}", idle="No email sent")
add(tag="em_count", t="The Agent sends its emails about the asks to exactly eight people, the askers apart from Leonard Hayes", w=5, kind="multi-source", why="the askers come from the ticket creators, and Douglas only from a comment on ZOM-563", fact="email_volume", span=SP_MAIL, oe=oe("addr", "wmail:brian.foster", "wmail:robert"), fids=" ".join(WHO_FID.values()), vals="`8`",
    verify="Count of people emailed", final="Sent emails", acc=["sent emails to exactly eight people, with Leonard Hayes among no recipients"], alt="Seven (Douglas missing) or nine (Leonard added) fails.", srcs=[S_CONTACT["douglas"], s_hub], ev=f"Sources: Contacts for the eight askers, Linear ZOM-563 comment cmt_eabac5435f2b3a575aad; Leonard's DM ('{Q_MAIL}')", dec="T7", grp="G11 asker emails (volume)", valid="One email each to the eight askers", idle="No email sent")

# ================================================================ DM
for call, n in (("Go", 2), ("Hold", 28), ("Drop", 6)):
    add(tag=f"dm_{call.lower()}", t=f"The Agent tells Leonard Hayes in his DM with Samuel (D06L58XCVKK) that {n} messages are {call} (any wording with that number)", w=5, kind="multi-source", why=f"the {call} count comes out of all 36 calls", fact=f"count_{call.lower()}", span=SP_DM, oe=oe("c7", "wdm"), fids=F("counts", "hub"), vals=f"`{n}` · {call}", verify=f"{call} count", final="Message in the DM", acc=[f"a message in D06L58XCVKK saying {n} {call}, any order or wording"], alt="Another count fails; so does a message in a channel.",
        srcs=[s_hub], ev=f"Sources: {EVID_COUNTS}; Leonard's DM {HUB[1]} ('{Q_COUNT}')", dec="T7" if call == "Hold" else "H1", valid=f"Go 2, Hold 28, Drop 6", idle="No message sent")
add(tag="order_dm", t="The Agent posts the counts in Leonard's DM after all of its other writes for the job (the calls sheet, the note, the ticket comments, the ticket moves, the new tickets, the checklist and the emails), with none of them after the post", w=1, cat="Process", kind="lookup", why="one ordering condition read from the prompt's 'When it's all finished'", fact="dm_order", span=SP_DM, oe=oe("w_rows", "w_note", "wc:Comeback gift", "wm:Comeback gift", "w_str", "w_i2", "wmail:robert", "wdm"), fids=F("hub"), vals="`D06L58XCVKK` · prompt order: When it's all finished", verify="Order: DM after every other write", final="Order of the post and the other writes",
    acc=["the counts post in D06L58XCVKK comes after every sheet, note, ticket comment, ticket move, new ticket, checklist and email write the Agent makes for the job"], alt="Any sheet, note, comment, move, new ticket, checklist or email write after the post fails.", srcs=[s_hub], just="Lookup: the prompt says 'When it's all finished tell him the counts in that same DM'; no Outcome row can show the order.", ev=f"Source: the prompt ('{SP_DM}'); Leonard's DM {HUB[1]}", dec="F1", valid="Every other write first, then the post", idle="No message sent")

# ================================================================ platform /rubric round 1 (FAIL 1, 2026-11-06)
# run_forensics/rev6/rubric_r1/platform_rubric_review_r1.md, reviewed sha 3911b7d5f4de. Titles and weights are copied exactly from its Fix
# List; every other row stays byte-identical to the JSON it reviewed, so DELTA keeps it locked. The assertions below hold both to that.
REPORT = (WF / "run_forensics/rev6/rubric_r1/platform_rubric_review_r1.md").read_text()
BASE = [r["tag"] for r in R]
BYTAG = {r["tag"]: r for r in R}


def retitle(tag, title, **kw):
    assert title in REPORT, title
    r = BYTAG[tag]
    r["t"] = title
    r.update(kw)
    body = title.split("The Agent ", 1)[1]
    r["acc"] = [body]
    r["ev"] = r["ev"].split(" Accept: ")[0].rstrip(".") + f". Accept: the Agent {body}."


def fixed(title):
    assert title in REPORT, title
    return title


# R3: a Message row
add(tag="msg_lapsed_1_day", t=fixed("The Agent enters Lapsed 1 day (or the PN sheet's \"Has not played in 24 hours\", any wording naming that message) in the Message column of the DES-316 row of its calls sheet"), w=1, kind="lookup",
    why="the name is read from the sheet row or the ticket", fact="message:Lapsed 1 day", span=SP_JOB, oe=oe("sheet", "kids", "w_rows"), fids=F("msg:Lapsed 1 day", "sheet"), vals="`Has not played in 24 hours`", verify="Lapsed 1 day Message cell",
    final="Message cell of that row", acc=[], alt="A blank cell fails; either name passes.", srcs=[s_hub], ev=f"Sources: PN sheet f_a325dd4af80afc5994d5dc row 4 'Has not played in 24 hours', Linear DES-316 '{ISSUES['DES-316']['title']}'; Leonard's DM ('{Q_FOLD}')", dec="F43", grp="G12 Message sample", valid="Lapsed 1 day", idle="No sheet created")
# R12: a Call row for the covered Drop
sheet_call("Lapsed 14 days", 5, "multi-source", "the weekly batch's four runs in the code, read with Leonard's cancellation note, show day 14 is covered, and the rule makes that a Drop", [s_cov, s_rule],
           f"Sources: Gmail {COV_ID} ('{Q_COV}'), NotificationManager.cs ('{Q_BATCH}'); rule doc ('{Q_DROP}')", F("msg:Lapsed 14 days", "covered", "client", "rule"), "T9", "direct exception")
assert BYTAG.get("call_lapsed_14_days") is None and R[-1]["t"] in REPORT
BYTAG = {r["tag"]: r for r in R}
BYTAG["em_robert_lapsed_14_days"]["fact"] = "told:Lapsed 14 days"
# R15, R16: wording
for t in ("miss_lives_recharged", "miss_plague_race"):
    new = BYTAG[t]["t"].replace("that it fails test 6, seen on both iOS and Android", "that it fails test 6, as Vincent has yet to see it arrive on both iOS and Android")
    assert new != BYTAG[t]["t"]
    BYTAG[t]["t"] = new
    body = new.split("The Agent ", 1)[1]
    BYTAG[t]["acc"] = [body]
    BYTAG[t]["ev"] = BYTAG[t]["ev"].split(" Accept: ")[0].rstrip(".") + f". Accept: the Agent {body}."
retitle("miss_lapsed_14_days", "The Agent records in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet that another message already covers it (naming Lapsed 7 days, DES-317, the weekly batch, the PN sheet's \"Has not played in seven days.\", or its line \"They’ve Taken Over… Can You Stop Them?\" or \"Your Squad Is Waiting\")")
# R33
BYTAG["ticket_teammate_sent_lives"].update(w=1, kind="lookup", just="Lookup: the key of the Agent's own new ticket for this ask (not ZOM-563).")
assert "Lookup: the key of the Agent's own new ticket for this ask (not ZOM-563)." in REPORT
# R38, R39
retitle("head_count", "The Agent keeps its Final headline entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry)", w=1, kind="lookup", why="the rule keeps the column to Go rows, read across the sheet's own Call column", just="Lookup: the rule keeps the column to Go rows, read across the sheet's own Call column.")
retitle("str_count", "The Agent keeps its String change entries to the rows it calls Go in its calls sheet (a blank cell, a dash or N/A on the other rows counts as no entry)", w=1, kind="lookup", why="the rule keeps the column to Go rows, read across the sheet's own Call column", just="Lookup: the rule keeps the column to Go rows, read across the sheet's own Call column.")
# R51-R54: the listing and the reason are separate rows
NH = {"Lives recharged": ("The Agent names Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) in its one-page note as a message the client already schedules that is still a Hold",
                          "The Agent gives test 6 as the reason Lives recharged (or DES-315, When lives are recharged, or Full Ammo Reloaded!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that Vincent Parker's tick is off, or that it failed to arrive on iOS 0.3.49)"),
      "Plague Race": ("The Agent names Plague Race (or DES-319, or Plague Race Is On!) in its one-page note as a message the client already schedules that is still a Hold",
                      "The Agent gives test 6 as the reason Plague Race (or DES-319, or Plague Race Is On!) is held in its one-page note (naming test 6, or saying Vincent has yet to see it arrive on both iOS and Android, that the iOS pass was on the 5-minute timers build, or that it never showed up on the real iOS build)"),
      "Weekly Leaderboard reset": ("The Agent names Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) in its one-page note as a message the client already schedules that is still a Hold",
                                   "The Agent gives test 5 as the reason Weekly Leaderboard reset (or DES-320, or Weekly Rankings Reset!) is held in its one-page note (naming test 5, or saying it fires on the wrong day, or that it counts from the last session and misses the weekly reset)"),
      "Finish first mission": ("The Agent names Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) in its one-page note as a message the client already schedules that is still a Hold",
                               "The Agent gives test 4 as the reason Finish first mission (or DES-318, Finish first tutorial, or Finish Your First Mission!) is held in its one-page note (naming test 4, or saying it can't reach its players, or that its players below level 20 haven't had our own ask, which runs after level 20)")}
for name, (t_name, t_why) in NH.items():
    base = BYTAG[f"nh_{tag(name)}"]
    srcs, txt, fids, dec = TRAP_SRC[name]
    add(tag=f"nhn_{tag(name)}", t=fixed(t_name), w=5, kind="multi-source", why="the message is one of the client's six scheduling calls, and its Hold joins records in other services", fact=f"note_hold:{name}", span=SP_JOB, oe=base["oe"], fids=base["fids"], vals=base["vals"].split(" · ")[0],
        verify=f"{name} named among the note's Holds", final="Note body", acc=[], alt="Leaving it out, or calling it ready, fails.", srcs=[s_client] + srcs[:1], ev=f"Sources: NotificationManager.cs (six scheduling calls), {txt}; Leonard's DM ('{q(Q_NOTE, 'anything the client already schedules that' + chr(39) + 's still a Hold and why')}')", dec=dec, grp="direct (the four Holds the client schedules)", valid=f"{name}, listed among the client's Holds", idle="No note created")
    retitle(f"nh_{tag(name)}", t_why, why="the reason joins the same records as the call", just="Multi-source: the reason joins the same records as the call.")
BYTAG = {r["tag"]: r for r in R}
# R92, R104-R107, R139, R143, R116: bare counts and name lists
retitle("cm_count", "The Agent leaves call comments on exactly 32 existing Design tickets")
retitle("mv_backlog", "The Agent moves exactly 24 existing tickets to Backlog")
retitle("mv_cancel", "The Agent moves exactly 6 existing tickets to Canceled")
retitle("mv_total", "The Agent changes the state of exactly 30 existing tickets")
retitle("mv_unassign", "The Agent clears the assignee on exactly 24 existing tickets", w=5, kind="multi-source", why="the count comes out of all the calls, read with the roadmap card's 'unassigned'", just="Multi-source: the count comes out of all the calls, read with the roadmap card's 'unassigned'.")
for name, w, kind, why in (("Win & Collect start", 5, "tracing", "the ticket is found through the live-ops page, it carries Calvin Price, and the roadmap card's 'unassigned' applies"),
                           ("Lives recharged", 5, "multi-source", "the clear rests on the test 6 failure and the roadmap card's 'unassigned'"),
                           ("Endless weekly result", 3, "comparison", "the rule's Todo is compared with the later roadmap card, which says unassigned")):
    k = key_of(name)
    a = "Calvin Price" if k == "DES-313" else "Samuel Turner"
    add(tag=f"un_{k.lower().replace('-', '')}", t=fixed(f"The Agent clears the assignee on {k} ({name})"), w=w, kind=kind, why=why, fact=f"assignee:{name}", span=SP_TICKETS, oe=oe("freeze", "wm:" + name), fids=F("msg:" + name, "freeze"), vals=f"`{k}`", verify=f"{k} assignee", final=f"{k} assignee", acc=[], alt=f"{k} left with {a} fails.", srcs=[s_tech],
        ev=f"Sources: Trello card {TECH} 'Fix TECH ISSUES' ('{Q_FREEZE}'; action 68dae8c7d95e24b55b69bf80); Linear {k} assignee {a}", dec="T8", grp="G8 assignee samples", valid=f"{k} unassigned", idle=f"{k} left with {a}")
# R114: one row per ask ticket
for name in ASKS:
    z = ZOMC[name][0]
    add(tag=f"news_{tag(name)}", t=fixed(f"The Agent files its new ticket for the ask on {z} ({name}) in Backlog with no assignee"), w=3, kind="comparison", why="the ask is a Hold, and the roadmap card puts held tickets in Backlog, unassigned", fact=f"new_state:{name}", span=SP_TICKETS, oe=oe("freeze", "w_new:" + name), fids=F("freeze", "ask:" + name), vals=f"`{z}`", verify=f"State of the new {name} ticket", final="New Linear ticket", acc=[], alt="That ticket in Todo, or given an assignee, fails.", srcs=[s_tech, s_zom(name)],
        ev=f"Sources: Trello card {TECH} ('{Q_FREEZE}'); Linear {z} comment {ZOMC[name][1]}", dec="T7", grp="G9 new ticket states (one row each)", valid="New ticket in Backlog with no assignee", idle="No ticket created")
retitle("chk_lapsed_7_days", "The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the PN sheet's \"Has not played in seven days.\", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)")
retitle("em_count", "The Agent sends its emails about the asks to exactly eight people")
retitle("order_dm", "The Agent posts the counts in Leonard's DM after all of its other writes for the job (the calls sheet, the note, the ticket comments, the ticket moves, the assignee clears, the new tickets, the checklist and the emails), with none of them after the post")
# 'Not scored, worth doing': supporting fields only
BYTAG["call_weekly_leaderboard_reset"]["just"] = "Multi-source: the test 5 failure joins Arthur's PR #248 review comment and the code loop against the ticket and the sheet's Ready status."
BYTAG["call_finish_first_mission"]["just"] = "Multi-source: the test 4 failure joins Robert's Slack post and Arthur's reply against the ticket's audience and the rule."
for t, rec in (("mv_lapsed_14_days", f"Gmail {COV_ID} ('{Q_COV}'), match3d Assets/Scripts/Notifications/NotificationManager.cs ('{Q_BATCH}')"), ("mv_hourly_coins", DROP_TXT["Hourly Coins"]), ("mv_comeback_gift", src_txt("Comeback gift"))):
    BYTAG[t]["ev"] = BYTAG[t]["ev"].replace("Sources: rule doc", f"Sources: {rec}; rule doc", 1)
    assert rec in BYTAG[t]["ev"]

GONE = {"miss_login_calendar_update", "tally_hold", "tally_drop", "mv_plague_race", "mv_quests_rollover", "mv_season_pass_start", "new_state"}
AFTER = {"sheet_rows": ["msg_lapsed_1_day"], "call_streak_fever": ["call_lapsed_14_days"], "mv_unassign": ["un_des313", "un_des315", "un_des329"]}
BEFORE = {f"nh_{tag(n)}": [f"nhn_{tag(n)}"] for n in NH}
order = []
for t in BASE:
    order += BEFORE.get(t, [])
    if t == "new_state":
        order += [f"news_{tag(n)}" for n in ASKS]
    if t not in GONE:
        order.append(t)
    order += AFTER.get(t, [])
BYTAG = {r["tag"]: r for r in R}
assert sorted(order) == sorted(t for t in BYTAG if t not in GONE), set(order) ^ set(t for t in BYTAG if t not in GONE)
R[:] = [BYTAG[t] for t in order]
POS = {t: i + 1 for i, t in enumerate(order)}
for t, n in {"msg_lapsed_1_day": 4, "call_lapsed_14_days": 14, "miss_lives_recharged": 17, "miss_plague_race": 18, "miss_lapsed_14_days": 21, "ticket_teammate_sent_lives": 34, "head_count": 39, "str_count": 40, "nhn_lives_recharged": 50, "nh_lives_recharged": 51,
             "nhn_plague_race": 52, "nh_plague_race": 53, "nhn_weekly_leaderboard_reset": 54, "nh_weekly_leaderboard_reset": 55, "nhn_finish_first_mission": 56, "nh_finish_first_mission": 57, "cm_count": 95, "mv_backlog": 104, "mv_cancel": 105, "mv_total": 106, "mv_unassign": 107,
             "un_des313": 108, "un_des315": 109, "un_des329": 110, "news_boss_arena_attempts_refilled": 117, "news_daily_gift_about_to_reset": 118, "news_teammate_sent_lives": 119, "news_infinite_lives_ending": 120, "chk_lapsed_7_days": 122, "em_count": 145, "order_dm": 149}.items():
    assert POS[t] == n, (t, POS[t], n)
assert len(R) == 149

# ================================================================ platform /rubric round 2 (FAIL 1, 2026-11-06)
# run_forensics/rev6/rubric_r2/platform_rubric_review_r2.md, reviewed sha d1cbadf710e9. Titles, weights and justifications are copied exactly from its
# Fix List; R21 is the author's rewrite it asks for. Every other row stays byte-identical, so DELTA keeps it locked.
REPORT = (WF / "run_forensics/rev6/rubric_r2/platform_rubric_review_r2.md").read_text()


def full(ev):
    return ev.replace("rule doc ('", f"rule doc {RULE[1]} ('").replace("NotificationManager.cs", "match3d Assets/Scripts/Notifications/NotificationManager.cs")


Q_CALL = q(CLIENT_TXT, "// Schedule Weekly reminder batch")
Q_LB = q(CLIENT_TXT, "BatchScheduleWeeklyLeaderboardNotifications(WeeklyLeaderboardTitle, WeeklyLeaderboardMessage, 4, serverToday);")
Q_HEAD7 = q(CLIENT_TXT, "They’ve Taken Over… Can You Stop Them?")
# R21: the rewrite the report leaves to the author
r = BYTAG["miss_lapsed_14_days"]
r["t"] = ("The Agent names Lapsed 7 days as the covering message in the What's missing column of the DES-344 (Lapsed 14 days) row of its calls sheet (the bare name passes, with or without \"covered by\", and so does DES-317, "
          "the PN sheet's \"Has not played in seven days.\", the client's \"Weekly reminder batch\" (WeeklyReminderTitle), Leonard's \"the weekly one\", its line \"They’ve Taken Over… Can You Stop Them?\" or \"Your Squad Is Waiting\", "
          "or any other wording that identifies Lapsed 7 days; a cell naming only the Weekly Leaderboard batch, DES-320 or \"Weekly Rankings Reset!\" fails)")
assert len(r["t"].split()) <= 120
_body = r["t"].split("The Agent ", 1)[1]
r["acc"] = [_body]
r["ev"] = full(f"Sources: Gmail {COV_ID} ('{Q_COV}'), NotificationManager.cs ('{Q_CALL}'; '{Q_BATCH}'; title '{Q_HEAD7}'), PN sheet f_a325dd4af80afc5994d5dc row 'Has not played in seven days.'; the Weekly Leaderboard batch is a separate call for DES-320 ('{Q_LB}'); rule doc ('{Q_DROP}')") + f". Accept: the Agent {_body}."
# R24
BYTAG["miss_teammate_sent_lives"].update(w=3, kind="interpretation", just="Interpretation: test 2 read against the asker's own note on ZOM-563 that it would have to go out from the server.")
assert BYTAG["miss_teammate_sent_lives"]["just"] in REPORT
# R104, R105 out; the DES-319 move back
_p = BYTAG["mv_plague_race"]
assert _p["t"] in REPORT and _p["w"] == 5 and _p["just"] in REPORT
_p["ev"] = _p["ev"].replace("Sources: Trello card", f"Sources: Slack D06UFE81RF0/1759174846.723833 ('{Q_RACE}'), Trello card", 1)
assert "so scratch iOS" in _p["ev"] and "DES-319 state Done" in _p["ev"]
_p["srcs"] = [s_qareply] + _p["srcs"]
_p["grp"] = "direct (the four Done Holds)"
# R117-R120: state and assignee apart
J_B = "Comparison: the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo."
J_U = "Comparison: the ask is a Hold, and the roadmap card says held tickets sit unassigned."
assert J_B in REPORT and J_U in REPORT
for name in ASKS:
    z = ZOMC[name][0]
    base = dict(w=3, kind="comparison", span=SP_TICKETS, oe=oe("freeze", "w_new:" + name), fids=F("freeze", "ask:" + name), vals=f"`{z}`", final="New Linear ticket", acc=[], srcs=[s_tech, s_zom(name)], ev=f"Sources: Trello card {TECH} ('{Q_FREEZE}'); Linear {z} comment {ZOMC[name][1]}", dec="T7", idle="No ticket created")
    add(tag=f"newb_{tag(name)}", t=fixed(f"The Agent files its new ticket for the ask on {z} ({name}) in Backlog"), why="the ask is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo", just=J_B, fact=f"new_state:{name}", verify=f"State of the new {name} ticket", alt="That ticket in Todo fails.", grp="G9 new ticket states (one row each)", valid="New ticket in Backlog", **base)
    add(tag=f"newu_{tag(name)}", t=fixed(f"The Agent files its new ticket for the ask on {z} ({name}) unassigned"), why="the ask is a Hold, and the roadmap card says held tickets sit unassigned", just=J_U, fact=f"new_assignee:{name}", verify=f"Assignee of the new {name} ticket", alt="That ticket given an assignee fails.", grp="G9 new ticket assignees (one row each)", valid="New ticket unassigned", **base)
# R122
retitle("chk_lapsed_7_days", "The Agent adds Lapsed 7 days (named by DES-317, Lapsed 7 days, the client's \"Weekly reminder batch\" (WeeklyReminderTitle), the PN sheet's \"Has not played in seven days.\", Your Squad Is Waiting or They’ve Taken Over… Can You Stop Them?) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)")
_c = BYTAG["chk_lapsed_7_days"]
_c["ev"] = _c["ev"].replace("Sources: Trello card", f"Sources: match3d Assets/Scripts/Notifications/NotificationManager.cs call site ('{Q_CALL}'; '{Q_BATCH}', line 173), Trello card", 1)
assert Q_CALL in _c["ev"]
# not scored: the row number in R4's evidence
_m = BYTAG["msg_lapsed_1_day"]
assert "row 4 'Has not played in 24 hours'" in _m["ev"]
_m["ev"] = _m["ev"].replace("row 4 'Has not played in 24 hours'", "row 5 in the sheet, export grid index 4, 'Has not played in 24 hours'")

BYTAG = {r["tag"]: r for r in R}
BYTAG["mv_plague_race"] = _p
new_order = []
for t in order:
    if t in ("mv_backlog", "mv_cancel"):
        continue
    if t.startswith("news_"):
        k = t[5:]
        new_order += [f"newb_{k}", f"newu_{k}"]
        continue
    new_order.append(t)
    if t == "mv_finish_first_mission":
        new_order.append("mv_plague_race")
R[:] = [BYTAG[t] for t in new_order]
assert len(R) == 152 and len(set(new_order)) == 152

# ================================================================ platform /rubric round 3 (FAIL 1, 2026-11-06)
# run_forensics/rev6/rubric_r3/platform_rubric_review_r3.md, reviewed sha 5bf50637b0a1. Checked fixes are copied exactly (R105, R106, R116-R123);
# R21 and R125 are the author's rewrites it asks for, on one shared closed list of names. Every other row stays byte-identical, so DELTA keeps it locked.
REPORT = (WF / "run_forensics/rev6/rubric_r3/platform_rubric_review_r3.md").read_text()
# R105: back to one template volume row per target state; the "exactly 30" row goes (it is their sum)
retitle("mv_backlog", "The Agent moves exactly 24 pre-existing tickets to Backlog (its new tickets not counted)")
retitle("mv_cancel", "The Agent moves exactly 6 pre-existing tickets to Canceled")
assert BYTAG["mv_backlog"]["just"] == "Multi-source: the count comes out of all the calls, and the card overrides Todo." and BYTAG["mv_backlog"]["just"] in REPORT
assert BYTAG["mv_cancel"]["just"] == "Multi-source: the count comes out of test 1 and the covered Lapsed 14 days." and BYTAG["mv_cancel"]["just"] in REPORT
assert BYTAG["mv_backlog"]["w"] == 5 and BYTAG["mv_cancel"]["w"] == 5
# R106
retitle("mv_unassign", "The Agent clears the assignee on exactly 24 pre-existing tickets (its new tickets not counted)")
assert BYTAG["mv_unassign"]["w"] == 5
# R116-R123: read at the end of the run, weight 5
T_B3 = "The Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) in Backlog when it finishes, whether filed there or moved there"
T_U3 = "The Agent has its new ticket for the ask on ZOM-542 (Boss Arena attempts refilled) unassigned when it finishes, whether filed that way or cleared later"
W_B3 = "the ask sits in a comment on ZOM-542, off DES-314's children; it is a Hold, and the later roadmap card puts held tickets in Backlog over the rule doc's Todo"
W_U3 = "the ask sits in a comment on ZOM-542, off DES-314's children; it is a Hold, and the roadmap card says held tickets sit unassigned"
for _s in (T_B3, T_U3, f"Tracing: {W_B3}.", f"Tracing: {W_U3}."):
    assert _s in REPORT, _s
for name in ASKS:
    z, cid = ZOMC[name]
    assert f"{z} ({name})" in REPORT
    _ask = BYTAG[f"cm_{tag(name)}"]["ev"].split(" ('", 1)[1].split("')", 1)[0]
    for pre, tt, ww, extra in (("newb_", T_B3, W_B3, f"; rule doc {RULE[1]} ('{Q_MOVE}')"), ("newu_", T_U3, W_U3, "")):
        _t = tt.replace("ZOM-542 (Boss Arena attempts refilled)", f"{z} ({name})")
        _w = ww.replace("ZOM-542", z)
        _b = _t.split("The Agent ", 1)[1]
        BYTAG[pre + tag(name)].update(t=_t, w=5, kind="tracing", why=_w, just=f"Tracing: {_w}.", acc=[_b],
                                      ev=f"Sources: Trello card {TECH} ('{Q_FREEZE}'){extra}; Linear {z} comment {cid} ('{_ask}'). Accept: the Agent {_b}.")
# R21, R125: the author's rewrites. One closed list: every name the records use for this message, the report's list plus the body line.
Q_WHEN7, Q_SEG7 = "7 Days Lapsed", "7d lapse since last session"
Q_BODY7 = q(CLIENT_TXT, "It’s been a while, survivor.")
Q_TAKEN = q(LINE2_TXT, "the 'taken over' push")
Q_ONE7 = q(LINE3_TXT, "the 7 day one")
_PN = json.loads((WF / "plan/pn_rows.json").read_text())["5"]
assert _PN["when"] == Q_WHEN7 and _PN["seg"] == Q_SEG7 and _PN["details"] == "Has not played in seven days." and _PN["body"].startswith(Q_BODY7)
NAMES7 = ("Lapsed 7 days, DES-317, the PN sheet's \"7 Days Lapsed\", \"Has not played in seven days.\" or \"7d lapse since last session\", the client's \"Weekly reminder batch\" "
          "(WeeklyReminderTitle, WeeklyReminderMessage, BatchScheduleWeeklyNotifications, Notification_WeeklyReminder), Leonard's \"the weekly one\", \"the 7 day one\" or \"the 'taken over' push\", "
          "\"They’ve Taken Over… Can You Stop Them?\", \"It’s been a while, survivor.\", \"Your Squad Is Waiting\" or \"Your Squad Needs You Back\"")
PN7 = f"PN sheet f_a325dd4af80afc5994d5dc row 6 in the sheet, export grid index 5 (When '{Q_WHEN7}', Details 'Has not played in seven days.', Segmentation '{Q_SEG7}')"
SRC7 = f"GitHub {PR}#rc_8 ('LocalizationManager.GetTranslation(\"Notification_WeeklyReminder\")'), Calendar {EVT} ('{Q_LINE3}'), Slack C08R8CHB0QL/1759169129.445834 ('{Q_TAKEN}'; '{Q_LINE2}')"
r = BYTAG["miss_lapsed_14_days"]
r["t"] = ("The Agent names Lapsed 7 days as the covering message in the What's missing or Call cell of the DES-344 (Lapsed 14 days) row of its calls sheet (a bare name passes: "
          + NAMES7 + "; a cell naming the Weekly Leaderboard batch, DES-320 or \"Weekly Rankings Reset!\" as covering it fails, even alongside Lapsed 7 days)")
_body = r["t"].split("The Agent ", 1)[1]
r["acc"] = [_body]
r["ev"] = full(f"Sources: Gmail {COV_ID} ('{Q_COV}'), NotificationManager.cs ('{Q_CALL}'; '{Q_BATCH}'; title '{Q_HEAD7}'; message '{Q_BODY7}'), {PN7}, {SRC7}; the Weekly Leaderboard batch is a separate call for DES-320 ('{Q_LB}'); rule doc ('{Q_DROP}')") + f". Accept: the Agent {_body}."
_c = BYTAG["chk_lapsed_7_days"]
_c["t"] = f"The Agent adds Lapsed 7 days (named by {NAMES7}) as an item on a checklist on the Push Notifications card on ZM ROADMAP (6851a769c65dc0017a227bb7)"
_body = _c["t"].split("The Agent ", 1)[1]
_c["acc"] = [_body]
assert "', line 173)" in _c["ev"]
_c["ev"] = _c["ev"].replace("', line 173)", f"', lines 173–174; title '{Q_HEAD7}'; message '{Q_BODY7}'), Gmail {COV_ID} ('{Q_COV}'), {PN7}, {SRC7}", 1)
_c["ev"] = _c["ev"].split(" Accept: ")[0].rstrip(".") + f". Accept: the Agent {_body}."
for _r in (r, _c):
    assert len(_r["t"].split()) <= 120, len(_r["t"].split())
    for _n in ("7 Days Lapsed", "7d lapse since last session", "WeeklyReminderMessage", "BatchScheduleWeeklyNotifications", "Notification_WeeklyReminder", "the weekly one", "the 7 day one", "the 'taken over' push", "Your Squad Needs You Back"):
        assert _n in _r["t"] and _n.lower() in _r["ev"].lower(), _n

new_order = [x for t in new_order for x in (("mv_backlog", "mv_cancel") if t == "mv_total" else (t,))]
R[:] = [BYTAG[t] for t in new_order]
assert len(R) == 153 and len(set(new_order)) == 153
POS = {t: i + 1 for i, t in enumerate(new_order)}
for t, n in {"miss_lapsed_14_days": 21, "mv_backlog": 105, "mv_cancel": 106, "mv_unassign": 107, "new_count": 116, "newb_boss_arena_attempts_refilled": 117, "newu_infinite_lives_ending": 124, "chk_lapsed_1_day": 125, "chk_lapsed_7_days": 126, "chk_count": 127}.items():
    assert POS[t] == n, (t, POS[t], n)


tags = [r["tag"] for r in R]
assert len(tags) == len(set(tags)), [t for t in tags if tags.count(t) > 1]

# ---- outputs ---------------------------------------------------------------------------------------------------
rubric = [{"title": r["t"], "category": r["cat"], "weight": r["w"], "justification": r["just"], "evidence": r["ev"]} for r in R]
(TI / "09_Rubrics.json").write_text(json.dumps(rubric, indent=1, ensure_ascii=False) + "\n")


def ahash(p):
    return subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/stage_gate.py"), "--artifact-hash", str(p)], capture_output=True, text=True, cwd=WS).stdout.strip()


ev_path = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
ev["rubric_hash"] = ahash(TI / "09_Rubrics.json")
ev["prompt_hash"] = ahash(TI / "04_Prompt.txt")
ev["rubric_rows"] = [{"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"], "accepted_outcomes": r["acc"], "alternatives_review": r["alt"], "source_records": r["srcs"]} for i, r in enumerate(R)]
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(Path(__file__).with_name("rows.json"), "w"), indent=1, ensure_ascii=False)
print(len(R), "rows; weight", sum(r["w"] for r in R), "; bands", {b: sum(1 for r in R if r["w"] == b) for b in (5, 3, 1)}, "; rubric_hash", ev["rubric_hash"])
