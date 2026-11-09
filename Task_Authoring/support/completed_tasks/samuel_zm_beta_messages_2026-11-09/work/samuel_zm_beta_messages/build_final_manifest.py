#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.json (final, /create-injection) from the certified draft + the SQL ids.
Every draft id is kept; changes are listed in design_delta. Adds what only the SQL settles: row ids, the facts sheet with
home_ids, solver {path, digest} and gradable_surface. Re-run after any SQL or solver change. No preflight {report, digest}
is written here: preflight_report.py binds this manifest by sha256, so a digest written back would make it stale."""
import copy, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
draft = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json")))
ids = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
P = json.load(open(os.path.join(HERE, "ids.json")))
I, TK = P["ids"], P["tickets"]
man = copy.deepcopy(draft)
man["_note"] = "Final manifest (/create-injection rev6). The scenario-certified draft plus the ids, facts and bindings only the SQL settles; every change is in design_delta."
SAM = "samuel.turner@harmonygames.co"
SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
SLACK_ID, MSGS = {}, {}
for x in parse_sql(SQL_TEXT):
    if x.get("op") != "insert":
        continue
    r = x["row"]
    if x["table"] == "slack.slack_messages":
        SLACK_ID[f"{r['channel_id']}/{r['ts']}"] = r["id"]
    elif x["table"] == "gmail.gmail_messages":
        MSGS.setdefault(r["thread_id"], []).append(r)
QA_MSG = ids["qa_msg"]
sl = lambda x: SLACK_ID.get(x, x) if isinstance(x, str) else x       # noqa: E731
sll = lambda xs: [sl(x) for x in xs or []]                            # noqa: E731
qa = lambda xs: [m for t in xs for m in ([QA_MSG, t] if t == I["qa_thread"] else [t])]   # noqa: E731

for a in man["anchors"]:
    a["record"], a["locator"] = sl(a["record"]), sl(a["locator"])
for f in man["ask_fragments"]:
    f["seeded_ids"] = qa(sll(f.get("seeded_ids")))
    f["delegated_by_record"] = sl(f.get("delegated_by_record"))
    f["locator"], f["container"] = sl(f["locator"]), sl(f["container"])
    if f["service"] == "gmail":
        f["locator"] = QA_MSG
for a in man["authorities"]:
    a["seeded_ids"] = qa(sll(a.get("seeded_ids")))
    a["decoy_seeded_ids"] = sll(a.get("decoy_seeded_ids"))
for t in man["traps"]:
    t["seeded_ids"] = qa(sll(t.get("seeded_ids")))
    for v in t.get("version_records") or []:
        if v.get("seeded") and v.get("id") in SLACK_ID:
            v["id"] = SLACK_ID[v["id"]]
for c in man["chains"]:
    for hop in c["hops"]:
        hop["record"] = sl(hop["record"])
        if hop["record"] == I["qa_thread"]:
            hop["record"] = QA_MSG
for s_ in man["cohort"].get("evidence_surfaces", []):
    s_["seeded_ids"] = sll(s_.get("seeded_ids"))
delta = [{"id": "record ids (all elements)",
          "change": "Slack channel/ts pointers to seeded messages became the messages' 32-hex row ids; Vincent's QA note is cited by its message row with the thread kept alongside",
          "reason": "the gate reads text and timestamps from SQL rows: a Slack row is keyed by its id, and a Gmail thread row holds only a snippet"},
         {"id": "per-ticket note times",
          "change": "Arthur's pass runs from Sep 25 20:30Z, after the last ask of that day; 24 tickets carry his note in his own words, and the two filed after it do not",
          "reason": "ticket numbers rise with filing time, so a ticket filed after Lapsed 14 days cannot have been in a pass that missed Lapsed 14 days"}]
PN_DRIVE = "gdrive:data.json /drive_files/42750"     # the PN sheet's Drive row: the gate reads its modified_time here
for f in man["ask_fragments"]:
    if f["id"] == "K3":
        f["delegated_by_record"], f["delegation_quote"], f["incorporated_via"] = sl(I["hub"]), "every row on the PNs Beta tab", ["A1", "K1"]
for t in man["traps"]:
    for v in t.get("version_records") or []:
        if v.get("base_pointer") == P["base"]["pn_sheet"]:
            v["base_pointer"] = PN_DRIVE
delta += [{"id": "K3 delegation", "change": "delegated_by_record and delegation_quote now cite Leonard's DM ('every row on the PNs Beta tab'), not the sheet",
           "reason": "the sheet does not name itself: the words that delegate it are in the hub, and the gate reads them from the delegating record"},
          {"id": "T2 version_records[0]", "change": f"base_pointer {P['base']['pn_sheet']} -> {PN_DRIVE}",
           "reason": "same record, in the pointer form the gate can read a timestamp from"}]
delta.append({"id": "rev2 record wording", "change": "Arthur's reply now says messages are scheduled once our own ask has run or the player switches them on from settings; Brian is added to the Beta readiness deck's shares",
              "reason": "the /injection review of rev1 failed the unqualified 'only': harmonygames-Games/match3d#263#rc_4 shows the settings toggle calling EnableNotifications with no ask, and Vincent's comment on DES-318 shows a message arriving that way. Brian's post cites the deck he could not open"})
delta.append({"id": "rev4 record wording", "change": "the rule doc's string ticket sentence ends 'so open one when you make the call'",
              "reason": "an independent read of the prompt found a write-versus-no-write fork: the doc said a line needs a string ticket without saying who files it, and the prompt waives any check-in"})
delta.append({"id": "rev5 record wording", "change": "Leonard's DM: the note no longer asks who hears from us once they stop playing; it asks for D1 and D7 with iOS and Android separately, the lapsed reminders the client schedules day by day, and anything the client already schedules that's still a Hold and why. Slot X20 follows it. Leonard's comment on the Rewarded ad ready ticket now says no bonus ad is live today",
              "reason": "/prompt failed rev4 on Unique Ground Truth and Cross-Service Coherence (run_forensics/rev4/prompt_report_FAIL.md): Snowflake PUSH_NOTIFICATION_STATS shows weekly Firebase pushes to lapsed players against records saying every message is local, and Snowflake cannot be injected, so the question was removed. Per-platform and settings opt-in forks went with it. A blind sweep (plan/sweep_fork_rev5.md F1) then showed the warehouse's rewarded_video rows touch the rule's live prong, which Leonard's line left to inference; those rows use the rewarded_continue placement, with no bonus placement. No call, count or ticket state changes"})
delta.append({"id": "rev6 hardness moves", "change": "Plague Race reads like every other pass and Vincent's reply drops the store build wording; Vincent's channel post takes his pass off Lives recharged (Go 2); Leonard's calendar note replaces his Sep 29 line; the Hold rule moves from a card comment to the card's description; two more comment asks sit outside the parent, one from Douglas; one Trello action renames the list to BETA: Oct 10; the Rewarded ad ready ask is removed",
              "reason": "/hardness scored rev5 2 (run_forensics/rev5/hardness_report_FAIL_2.md): 188 calls, about 90% right, one independent cause. /prompt scored Coherence 3 on SC-13. Moves chosen from the run's own call ledger (01a_Hardening_Report.md §5, §10) under the requester's delegation. The blind sweep of rev6 (plan/sweep_fork_rev6.md F1) found AD_IMPRESSION_EVENTS can answer the rule's live-today test for the rewarded ask, the rev4 failure pattern, and Snowflake cannot be injected, so the ask goes; F2 moved Douglas's comment after his Sep 30 prod update, F3 and F4 fixed two timelines"})
delta.append({"id": "rev3 record wording", "change": "Leonard's comment on the Rewarded ad ready ticket; Julia's ask says the gift streak is live and is separate from Calvin's chest ping; the rule's in-the-beta test names Zombie Match; the hub says one email per person, apart from Leonard",
              "reason": "a blind fork sweep on rev2 (plan/sweep_fork_rev2.md) showed these four could each move Hold or Drop by one or leave the email count open, and /prompt fails on a classification fork no record settles"})
EXTRA = {"FILT": "Plague Race red dot (ZOM-471, in the game: off the plan)", "ALIAS": "Season Pass start (its own ticket)",
         "BUILT": "Lapsed 30 days (past the four-week batch: Hold)", "FOLLOW": "Axe Arena (Drop: Canceled either way)"}
m = ids["slack_mid"]
facts = [
    {"key": "Arthur's rollover note", "value": "isn't tied to the rollover", "kind": "status", "home_ids": [I["arthur_inline"], ids["arthur_mail"]]},
    {"key": "final line for the seven-day message", "value": P["new_line"], "kind": "status", "home_ids": [I["copy_check"], ids["evt"]["copy_leonard.hayes@harmonygames.co"]]},
    {"key": "interim line for the seven-day message", "value": P["slack_line"], "kind": "status", "home_ids": [m["corr_reply"]]},
    {"key": "Lives recharged pass withdrawn", "value": "taking my tick off Full Ammo", "kind": "status", "home_ids": [m["lives_pull"]]},
    {"key": "teammate lives ask", "value": "when a teammate sends you lives", "kind": "status", "home_ids": [I["team_ask"]]},
    {"key": "infinite lives ask", "value": "infinite lives are about to run out", "kind": "status", "home_ids": [I["inf_ask"]]},
    {"key": "permission ask for the beta build", "value": "leaving our own ask after level 20", "kind": "status", "home_ids": [m["ask_decision"]]},
    {"key": "what switches messages on", "value": "only schedules once our own ask has run", "kind": "status", "home_ids": [m["ask_reply"]]},
    {"key": "what counts as seen", "value": "Seen only counts on a store build", "kind": "status", "home_ids": [QA_MSG, QA_MSG.replace(SAM, "vincent.parker@harmonygames.co")]},
    {"key": "race pass withdrawn", "value": "5-minute timers build", "kind": "status", "home_ids": [m["qa_reply"]]},
    {"key": "roadmap freeze", "value": "Held tickets sit in Backlog", "kind": "status", "home_ids": [I["freeze_comment"], P["base"]["tech_card"]]},
    {"key": "day 14 already covered", "value": "day 14 is already covered", "kind": "status", "home_ids": [ids["cancel_mail"]]},
    {"key": "Boss Arena ask", "value": "once the daily Boss Arena attempts refill", "kind": "status", "home_ids": [I["boss_ask"]]},
    {"key": "daily gift ask", "value": "the evening before the daily gift streak resets", "kind": "status", "home_ids": [I["gift_ask"]]},
    {"key": "comeback gift scope", "value": "version 2 idea", "kind": "status", "home_ids": [I["gift_note"]]},
    {"key": "race timing", "value": "Daily is fine for this one", "kind": "status", "home_ids": [I["race_daily"]]},
    {"key": "reach test", "value": "the settings toggle doesn't count", "kind": "status", "home_ids": [I["rule_doc"]]},
    {"key": "emoji rule", "value": "Emoji don't count as a different line", "kind": "status", "home_ids": [I["rule_doc"]]},
    {"key": "stale deck count", "value": "6 Ready on the PN sheet", "kind": "status", "must_appear_in": [I["deck"]]},
]
man["facts"] = facts
for e in man["mechanism_portfolio"]:
    if e["id"] in EXTRA and EXTRA[e["id"]] not in e.get("controls", []):
        e["controls"] = list(e.get("controls") or []) + [EXTRA[e["id"]]]
        delta.append({"id": f"mechanism_portfolio.{e['id']}.controls", "change": f"added {EXTRA[e['id']].split(' (')[0]} as a control member",
                      "reason": "the draft's over_application already acts on this member; contract.controls needs the operator to move a declared control"})
man["solver"] = {"path": "Working_Files/solver/solver.py", "digest": hashlib.sha256(open(os.path.join(WF, "solver", "solver.py"), "rb").read()).hexdigest()}
man["gradable_surface"] = "01_Gradable_Surface.json"
man["design_delta"] = delta
json.dump(man, open(os.path.join(WF, "01_Hardness_Manifest.json"), "w"), indent=1, ensure_ascii=False)
open(os.path.join(WF, "01_Hardness_Manifest.json"), "a").write("\n")
body = "\n".join(l for l in SQL_TEXT.splitlines() if not l.startswith("--"))
miss = []
for sec in ("ask_fragments", "authorities", "traps"):
    for el in man[sec]:
        for k in ("seeded_ids", "decoy_seeded_ids"):
            for x in el.get(k) or []:
                if x and not re.search(r"(?<![\w-])" + re.escape(x) + r"(?![\w-])", body):
                    miss.append(f"{sec}:{el['id']}:{k}:{x}")
        for v in el.get("version_records") or []:
            if v.get("seeded") and not re.search(r"(?<![\w-])" + re.escape(str(v.get("id"))) + r"(?![\w-])", body):
                miss.append(f"{sec}:{el['id']}:version_records:{v.get('id')}")
print("facts", len(facts), "delta", len(delta), "seeded ids not in the SQL:", miss or "none")
