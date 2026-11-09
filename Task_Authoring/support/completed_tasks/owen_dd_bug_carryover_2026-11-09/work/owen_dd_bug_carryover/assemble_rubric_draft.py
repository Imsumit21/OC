#!/usr/bin/env python3
"""Draft mode: write task_inputs/09_Rubrics.json from the plan rows (rubric_rows.py) and their criterion text (rubric_titles.py),
and record the V3 rubric_rows evidence in Working_Files/00_V3_Authoring_Evidence.json (owen_dd_bug_carryover, rev9).
Every source_value is re-read in this run: seeded fields from the parsed SQL (never executed), base fields from plan/oe_base.json
(tools/hg.py reads by oe_reads.py). A dated copy of each build is kept in run_forensics/rev9/rubric/."""
import hashlib
import importlib.util
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402
from pathlib import Path  # noqa: E402
import stage_gate as SG  # noqa: E402


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


RR, TT = load("rubric_rows"), load("rubric_titles")
ROWS, T = RR.R, TT.T
assert set(T) == {r["fact"] for r in ROWS}, set(T) ^ {r["fact"] for r in ROWS}
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
U = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data"
SLACK_ROOT, LINEAR, CONTACTS = f"{U}/slack", f"{U}/linear/data.json", f"{U}/contacts/contacts.json"
GITHUB = "Universe_Normal/Normal_HarmonyGames_GitHub/Services_Data/github/data.json"
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"
HUB_ID = "D05S1S2AB5M/1770937805.214409"
RULES_ID = "f_3ca9e15d7b20f4e681ad52"
HUB_STEP = {"service": "slack", "id": HUB_ID}
RULES_STEP = {"service": "gdocs", "id": RULES_ID}


def sqlrow(table, **ident):
    rs = [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rs) == 1, (table, ident, len(rs))
    return rs[0]


def sql_slack(chan, ts, why, path=None):
    r = sqlrow("slack.slack_messages", channel_id=chan, ts=ts)
    rid = f"{chan}/{ts}"
    steps = [HUB_STEP] + (path or []) + ([{"service": "slack", "id": rid}] if rid != HUB_ID else [])
    return {"service": "slack", "id": rid, "source_file": "01_Universe_Inject.sql", "table": "slack.slack_messages",
            "identity": {"channel_id": chan, "ts": ts}, "column": "text", "source_value": r["text"], "evidence_path": steps,
            "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "created_at",
                                  "rationale": f"Seeded Slack message; created_at {r['created_at']} is before the freeze 2026-02-14T00:00:00Z; a posted message with no edit."}}


def sql_on(service, rid, table, ident, column, recorded, why, path=None):
    """A seeded row cited on the base record it belongs to (a Linear comment on its issue, a review comment on its PR)."""
    r = sqlrow(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column,
            "source_value": r[column], "evidence_path": [HUB_STEP] + (path or []) + [{"service": service, "id": rid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": recorded,
                                  "rationale": f"Seeded {table} row on {rid}; {recorded} {r[recorded]} is before the freeze; a posted comment with no edit."}}


def sql_mutable(service, table, ident, column, rid, recorded, why, extra, path=None):
    r = sqlrow(table, **ident)
    steps = [HUB_STEP] + (path or []) + [{"service": service, "id": rid}]
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident,
            "column": column, "source_value": r[column], "evidence_path": steps, "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_column": recorded,
                                  "rationale": f"Seeded {table} row; {recorded} {r[recorded]} is before the freeze.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": extra, "evidence_ids": [rid, HUB_ID]}}}


SLK = {}
for f, recs in OB["slack_files"].items():
    for i, m in enumerate(recs):
        SLK[f"{m['channel']}/{m['ts']}"] = (f, f"/{i}", m)
for k, v in OB["slack"].items():
    SLK[k] = ("messages/" + k.split("/")[0] + "/" + v["file"].split("/")[-1], v["pointer"], v["rec"])


def base_slack(rid, why, path=None):
    f, p, rec = SLK[rid]
    return {"service": "slack", "id": rid, "source_file": f"{SLACK_ROOT}/{f}", "pointer": f"{p}/text", "source_value": rec["text"],
            "evidence_path": [HUB_STEP] + (path or []) + [{"service": "slack", "id": rid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"{p}/ts",
                                  "rationale": f"Base Slack post; ts {rec['ts']} is before the freeze; a posted message."}}


def base_linear(k, why):
    p = OB["linear"][k]["pointer"]
    rec = OB["linear"][k]["rec"]
    return {"service": "linear", "id": k, "source_file": LINEAR, "pointer": f"{p}/state_id", "source_value": rec["state_id"],
            "evidence_path": [HUB_STEP, {"service": "linear", "id": k}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{p}/updated_at",
                                  "rationale": f"Base Linear issue; updated_at {rec['updated_at']} is before the freeze, so the exported state is its state at the freeze.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": f"No SQL row changes {k}'s state (SQL L336–L349 touch updated_at and two descriptions only); the base state_id is the state at the freeze.", "evidence_ids": [k]}}}


def contact(n, email, why):
    return {"service": "contacts", "id": email, "source_file": CONTACTS, "pointer": f"/contacts/{n}/email", "source_value": email,
            "evidence_path": [HUB_STEP, {"service": "contacts", "id": email}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "directory_identity", "mutable_state": False,
                                  "rationale": "Contacts identity field (email) of the person the row names; identity, not a business value."}}


def canvas(rid):
    return base_slack(rid, "The notes name 'the comment channel of Vincent's Android canvas'; Owen is a member of CE156FDFB428 (rejoined Feb 12).")


PR = "harmonygames-Games/GameOfDominoes"
p1913 = OB["github"][f"{PR}#1913"]["pointer"]
CAT = {
    "HUB": sql_slack("D05S1S2AB5M", "1770937805.214409", "The prompt names Arthur's Thursday DM; Owen is a party to D05S1S2AB5M."),
    "RULES": sql_mutable("gdocs", "gdocs.docs_documents", {"document_id": RULES_ID}, "body_text", RULES_ID, "modified_time",
                         "The DM says 'How we call each one is in the carry-over notes doc I shared with you'; the doc is shared with Owen.",
                         "The doc's created and modified times are both 2026-02-12T22:48:00Z, before the freeze, so the exported body is its state at the freeze; Arthur's DM (23:10Z the same day) points to it."),
    "AMEND": sql_on("linear", "ENG-2401", "linear.linear_comments", {"id": "comment_49b5ac4788465f72ddf245e34f2b7034"}, "body", "created_at",
                    "The prompt names the UI Changes master ticket and the notes say changes go on it; the comment sits on ENG-2401."),
    "APPLE": {**sql_on("gmail", "owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com>", "gmail.gmail_messages",
                       {"id": "owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com>"}, "body_text", "date",
                       "The notes say Vincent tied lines to tickets; his mail is in Owen's inbox.")},
    "SIGNIN": sql_on("linear", "ENG-2363", "linear.linear_comments", {"id": "comment_7ab5299cbb609d95ba12249d315daedc"}, "body", "created_at",
                     "The notes say Vincent tied lines to tickets; a Linear search for signing in reaches ENG-2363 and its comments."),
    "SEASON": sql_on("linear", "ENG-2428", "linear.linear_comments", {"id": "comment_d6aee2099bd71050facc422ccef8f809"}, "body", "created_at",
                     "The notes say Brian and Oliver left notes on some open children; the comment sits on ENG-2428."),
    "INLINE_TD": sql_on("github", f"{PR}#1905", "github.github_review_comments", {"id": f"{PR}#1905#rc_1"}, "body", "created_at",
                        "The tree rule asks whether a piece of each child's UI work made the build; the children's UI optimization PRs carry the review comments."),
    "INLINE_AXE": sql_on("github", f"{PR}#1908", "github.github_review_comments", {"id": f"{PR}#1908#rc_1"}, "body", "created_at",
                         "The tree rule asks whether a piece of each child's UI work made the build; the children's UI optimization PRs carry the review comments."),
    "TAVERN": sql_slack("D05USBTQY1F", "1765452012.418229", "The notes say a later record about a bug can overturn its tick; a Slack search for 'Tavern' reaches Marcus's DM to Owen."),
    "SHOP": sql_slack("C09Q4S613CN", "1764606918.318209", "The notes say a later record can overturn a tick; a Slack search for 'Memory Tile' reaches Brian's reply in #dd-road-to-sub-250mb, which Owen can read."),
    "TRAIN": sql_slack("CE156FDFB428", "1763845212.507119", "Vincent's reply sits in the train line's own thread in the canvas comment channel."),
    "TEAM": sql_slack("CE156FDFB428", "1763742012.611229", "Vincent's reply sits in the team-quit line's own thread."),
    "LIVES1": sql_slack("CE156FDFB428", "1763845812.703339", "Vincent's reply sits in the lives line's own thread."),
    "LIVES2": sql_slack("CE156FDFB428", "1763845872.804449", "Vincent's reply sits in the lives line's own thread."),
    "TIP": sql_slack("CE156FDFB428", "1763845512.559339", "Vincent's reply is the last in the tooltips line's own thread."),
    "MEGA": sql_slack("C05V5FNLB9V", "1764331830.705279", "Marcus's reply is the last in the mega tile post's thread in #god-bugs."),
    "BAR": sql_slack("C05V5FNLB9V", "1767021345.207719", "Brian's reply is the last in the bottom bar post's thread in #god-bugs."),
    "FLICK": sql_slack("C09Q4S613CN", "1766164222.418229", "A Slack search for 'flickering' (the post's word) reaches Robert's reply under his own report in #dd-road-to-sub-250mb."),
    "MUSIC": sql_slack("D07E9PSQB6W", "1765206644.602119", "Brian owns the UI card and the acid post's last reply is his; his DM with Owen holds the Dec 8 line."),
    "POPUPS": sql_slack("D07E9PSQB6W", "1765471563.704419", "Brian's DM with Owen holds the Dec 11 popups line."),
    "GIFT": sql_slack("D07E9PSQB6W", "1765471651.208713", "Brian's DM with Owen holds the Dec 11 Daily Gift line."),
    "WC": base_slack("C9CA62B5180A/1765927876.696389", "The tree rule names a screen switched off in the build; a Slack search for 'lives' reaches the economy-line group DM Owen is in, which holds the Dec 16 disable."),
    "LIVES": base_slack("C09SWTHEMEW/1764659626.614679", "A Slack search for 'lives' (the three lives lines) reaches Leonard's Dec 2 update in a channel Owen rejoined."),
    "WINCLAIM": base_slack("C05V5FNLB9V/1764329192.159229", "Marcus's reply is the only one under the tile dozer window post."),
    "TREASURE": base_slack("C05V5FNLB9V/1764694606.476379", "Brian's reply sits in the treasure button post's thread."),
    "PR1913": {"service": "github", "id": f"{PR}#1913", "source_file": GITHUB, "pointer": f"{p1913}/state", "source_value": OB["github"][f"{PR}#1913"]["rec"]["state"],
               "evidence_path": [HUB_STEP, {"service": "github", "id": f"{PR}#1913"}],
               "reachability_rationale": "Marcus's 'Ok i fixed it and did a PR' sends the agent to the repo's pull requests; a search for 'tile dozer' reaches #1913.",
               "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{p1913}/updated_at",
                                     "rationale": "Base pull request; updated_at 2025-11-28T11:25:58Z is before the freeze and the export is its state at the freeze.",
                                     "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": "#1913 was opened Nov 28 and never updated after; no SQL row touches it, so 'open' is its state at the freeze.", "evidence_ids": [f"{PR}#1913"]}}},
    "ENG2073": base_linear("ENG-2073", "Vincent's mail names ENG-2073."),
    "ENG2363": base_linear("ENG-2363", "A Linear search for signing in reaches ENG-2363."),
    "FOLDER": sql_mutable("gdrive", "gdrive.drive_files", {"id": "d_9b41e7c2a05d36f8e1c7a4"}, "name", "d_9b41e7c2a05d36f8e1c7a4", "modified_time",
                          "The prompt and the DM name 'my DD bug carry-over folder'; Owen owns it.",
                          "The folder was created and last modified 2026-02-12T23:00:00Z, before the freeze, and it is empty."),
    "EVT": sql_mutable("gcal", "gcal.gcal_events", {"event_id": "evt_6e2c91d4b07f3a58c1d2e4"}, "attendees_json", "evt_6e2c91d4b07f3a58c1d2e4", "created",
                       "The prompt and the DM name 'everyone on Sunday's bug review'; the event is on Owen's calendar.",
                       "The event was created and last updated 2026-02-12T23:05:00Z, before the freeze, so its attendee list is the list at the freeze; the review itself starts after the clock."),
    "CT_ARTHUR": contact(168, "arthur.blake@harmonygames.co", "The review event lists Arthur Blake; Contacts give his address."),
    "CT_ROBERT": contact(107, "robert@harmonygames.co", "The review event lists Robert; Contacts give his address."),
    "CT_OLIVER": contact(157, "oliver.brooks@harmonygames.co", "The review event lists Oliver Brooks; Contacts give his address."),
}
for key, rid in (("C_OFFERS", "CE156FDFB428/1763042129.025459"), ("C_TEAMS", "CE156FDFB428/1763394586.704949"), ("C_HUD", "CE156FDFB428/1763394911.691209"),
                 ("C_STREAK", "CE156FDFB428/1763643072.577249"), ("C_WCNULL", "CE156FDFB428/1763548890.165949"), ("C_BACKEND", "CE156FDFB428/1763042058.918579"),
                 ("C_CHAR", "CE156FDFB428/1763642659.467529")):
    CAT[key] = canvas(rid)
for k in [x for x in OB["linear"] if "ENG-2409" <= x <= "ENG-2437"]:
    CAT["K_" + k] = base_linear(k, "The prompt names the tree under the UI Changes master ticket; the child is listed under its group.")
for key, v in TT.TRUTH.items():
    ev_ = (v.get("evidence") or {}).get("Outcome") or []
    if ev_ and ev_[0].startswith("CE156FDFB428/") and v["Bug"][:1] in "\u2610\u2611" and TT.ckey(key) not in CAT and f"CE156FDFB428/{TT.ts_of(key)}" in SLK:
        CAT[TT.ckey(key)] = canvas(f"CE156FDFB428/{TT.ts_of(key)}")
CAT["OFFERS_CLOSE"] = base_slack("CE156FDFB428/1763606525.993489", "Arthur's reply is the last in the offers line's own thread in the canvas comment channel.")
CAT["LC_CLOSE"] = base_slack("CE156FDFB428/1763074145.483099", "The reply sits in the level-completed line's own thread in the canvas comment channel.")
CAT["SAGA_CLOSE"] = base_slack("CE156FDFB428/1763747143.093969", "The reply sits in the saga map line's own thread in the canvas comment channel.")
CAT["B2299"] = base_slack("C05433XK267/1765397569.397939", "The notes name the economy-line build players have; a Slack search for 'EconomyChanges' reaches the #builds lines.")
CAT["B2297"] = base_slack("C05433XK267/1765310444.095399", "The notes name the economy-line build players have; a Slack search for 'EconomyChanges' reaches the #builds lines.")
for key_, rid_, why_ in (("P_FLICK", "C05V5FNLB9V/1764659550.713509", "The notes name every bug posted in the bug channel after the canvas; the flickering post is one."),
                         ("P_MUSIC", "C05V5FNLB9V/1764660142.352319", "The notes name every bug posted in the bug channel after the canvas; the music post is one."),
                         ("P_BAR", "C05V5FNLB9V/1766415211.386389", "The notes name every bug posted in the bug channel after the canvas; the bottom bar post is one."),
                         ("P_MEGA", "C05V5FNLB9V/1764256187.655299", "The notes name every bug posted in the bug channel after the canvas; the mega tile post is one.")):
    CAT[key_] = base_slack(rid_, why_)
p1916 = OB["github"][f"{PR}#1916"]["pointer"]
CAT["PR1916"] = {"service": "github", "id": f"{PR}#1916", "source_file": GITHUB, "pointer": f"{p1916}/base_ref", "source_value": OB["github"][f"{PR}#1916"]["rec"]["base_ref"],
                 "evidence_path": [HUB_STEP, {"service": "github", "id": f"{PR}#1916"}],
                 "reachability_rationale": "Brian's close in the bottom bar thread follows the camera change; a search for 'camera' in the repo's pull requests reaches #1916.",
                 "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{p1916}/updated_at",
                                       "rationale": "Base pull request; updated_at 2025-12-26T19:05:40Z (merged) is before the freeze, so the export is its state at the freeze.",
                                       "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": "#1916 was merged into EconomyChanges on Dec 26 and no SQL row touches it.", "evidence_ids": [f"{PR}#1916"]}}}
REV = json.load(open(os.path.join(HERE, "09_Rubrics.prev_2ed7a6489798.json")))

crit, rows = [], []
for i, r in enumerate(ROWS, 1):
    x = T[r["fact"]]
    assert x["title"].startswith("The Agent "), r["p"]
    if x.get("lock"):
        rv = REV[x["lock"] - 1]
        assert rv["title"] == x["title"], (r["p"], x["lock"])
        crit.append({"title": rv["title"], "category": rv["category"], "weight": r["band"],
                     "justification": x.get("just_new") or rv["justification"], "evidence": rv["evidence"]})
        assert x.get("just_new") or rv["weight"] == r["band"], (r["p"], "a locked row changes weight only with a new justification")
    else:
        accept = x.get("accept") or x["title"][len("The Agent "):]
        ev = f"Source: {x['src']} Accept: {accept}." + (f" Reject: {x['alt']}" if x["alt"] else "")
        crit.append({"title": x["title"], "category": "Process" if r["cat"].startswith("Process") else "Outcome",
                     "weight": r["band"], "justification": x["just"], "evidence": ev})
    rows.append({"criterion_id": f"C{i}", "plan_row": r["p"], "fact_id": r["fact"], "prompt_span": r["span"],
                 "accepted_outcomes": x["acc"], "alternatives_review": x["alt"] + " Counter-reading: " + r["cr"],
                 "source_records": [CAT[k] for k in x["srcs"]], "oe_steps": [f"OE {n}" for n in sorted(set(r["oe"]))],
                 "valid_case": r["valid"], "do_nothing_case": r["idle"], "reachability": r["reach"]})

out = os.path.join(TI, "09_Rubrics.json")
open(out, "w").write(json.dumps(crit, indent=1, ensure_ascii=False) + "\n")
ev_path = os.path.join(WF, "00_V3_Authoring_Evidence.json")
ev = json.load(open(ev_path))
ev["rubric_hash"] = SG.file_digest(Path(out))
ev["prompt_hash"] = SG.file_digest(Path(TI) / "04_Prompt.txt")
ev["rubric_rows"] = rows
open(ev_path, "w").write(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
keep = os.path.join(WF, "run_forensics", "rev9", "rubric")
os.makedirs(keep, exist_ok=True)
sha = hashlib.sha256(open(out, "rb").read()).hexdigest()[:12]
shutil.copy(out, os.path.join(keep, f"09_Rubrics_{sha}.json"))
from collections import Counter
print("criteria", len(crit), "weights", dict(Counter(c["weight"] for c in crit)), "total", sum(c["weight"] for c in crit),
      "process", sum(c["category"] == "Process" for c in crit), "sha", sha, "rubric_hash", ev["rubric_hash"])
