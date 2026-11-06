#!/usr/bin/env python3
"""Draft mode: write task_inputs/09_Rubrics.json from the plan rows (rubric_rows.py) and their criterion text
(rubric_titles.py), and record the V3 rubric_rows evidence in Working_Files/00_V3_Authoring_Evidence.json.
Every source_value is re-read in this run: seeded fields from the parsed SQL (never executed), base fields from
plan/oe_base.json (tools/hg.py get-many via oe_reads.py). A dated copy of each build is kept in run_forensics/rev4/rubric/."""
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
assert set(T) == {r["p"] for r in ROWS}, set(T) ^ {r["p"] for r in ROWS}
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
SLACK_ROOT = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack"
CONTACTS = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/contacts/contacts.json"
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"


def sqlrow(table, **ident):
    rs = [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rs) == 1, (table, ident, len(rs))
    return rs[0]


HUB_ID = "D04UP2L3E3S/1770961200.890407"
RULES_ID = "f_1e468a9d69ea0f0a2001f5"
HUB_STEP = {"service": "slack", "id": HUB_ID}


def sql_slack(chan, ts, why, path=None):
    r = sqlrow("slack.slack_messages", channel_id=chan, ts=ts)
    rid = f"{chan}/{ts}"
    steps = [HUB_STEP] + (path or []) + ([{"service": "slack", "id": rid}] if rid != HUB_ID else [])
    return {"service": "slack", "id": rid, "source_file": "01_Universe_Inject.sql", "table": "slack.slack_messages",
            "identity": {"channel_id": chan, "ts": ts}, "column": "text", "source_value": r["text"], "evidence_path": steps,
            "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "created_at",
                                  "rationale": f"Seeded Slack message; created_at {r['created_at']} is before the freeze 2026-02-14T00:00:00Z; a posted message with no edit."}}


def sql_gmail(mid, why):
    r = sqlrow("gmail.gmail_messages", id=mid)
    return {"service": "gmail", "id": mid, "source_file": "01_Universe_Inject.sql", "table": "gmail.gmail_messages",
            "identity": {"id": mid}, "column": "body_text", "source_value": r["body_text"],
            "evidence_path": [HUB_STEP, {"service": "gmail", "id": mid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "date",
                                  "rationale": f"Seeded mail in Robert's mailbox; date {r['date']} is before the freeze; a sent mail does not change."}}


def sql_mutable(service, table, ident, column, rid, why, extra):
    r = sqlrow(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident,
            "column": column, "source_value": r[column], "evidence_path": [HUB_STEP, {"service": service, "id": rid}],
            "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_column": "modified_time",
                                  "rationale": f"Seeded {table} row; modified_time {r['modified_time']} is before the freeze.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": extra, "evidence_ids": [rid, HUB_ID]}}}


def base_slack(key, why, via_rules=False):
    v = OB["slack"][key]
    rec, (f, p) = v["rec"], OB["ptr"][key]
    chan = f.split("/")[1]
    rid = f"{chan}/{rec['ts']}"
    steps = [HUB_STEP] + ([{"service": "gdocs", "id": RULES_ID}] if via_rules else []) + [{"service": "slack", "id": rid}]
    return {"service": "slack", "id": rid, "source_file": f"{SLACK_ROOT}/{f}", "pointer": f"{p}/text", "source_value": rec["text"],
            "evidence_path": steps, "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"{p}/ts",
                                  "rationale": f"Base Slack post; ts {rec['ts']} is before the freeze; a posted message."}}


def contact(n, email, why):
    return {"service": "contacts", "id": email, "source_file": CONTACTS, "pointer": f"/contacts/{n}/email", "source_value": email,
            "evidence_path": [HUB_STEP, {"service": "contacts", "id": email}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "directory_identity", "mutable_state": False,
                                  "rationale": "Contacts identity field (email) of the person the row names; identity, not a business value."}}


CAT = {
    "HUB": sql_slack("D04UP2L3E3S", "1770961200.890407", "The prompt names Leonard's Thursday-night DM; Robert is a party to D04UP2L3E3S."),
    "VO": sql_slack("C09UHHN6PFZ", "1770938400.370665", "After the split mail (what one already pays) and Arthur's 'billing moved to my card', a Slack search for 'my card' reaches Leonard's #prototype reply; Robert is a member of #prototype.",
                    [{"service": "gmail", "id": "robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>"}]),
    "LAYER": sql_slack("C09UHHN6PFZ", "1770923700.470906", "The layer.ai issue in the project leads to a Slack search for 'layer.ai'; Leonard's reply sits in the #prototype thread Robert can read."),
    "DD140": sql_slack("D04V95AAAHW", "1770952200.665739", "The AWS-bill comments on the project's issues lead to a Slack search for 'AWS bill'; the reply is in Robert's DM with Arthur."),
    "BILL": sql_gmail("robert@harmonygames.co/<CA-Uw65DzW6GZhghwWXCmpQysWcEB62uoyH4IRsz@mail.gmail.com>", "The Metabase issue and Arthur's KubLLC post lead to a Gmail search for 'metabase'; the mail is in Robert's inbox."),
    "SPLIT": sql_gmail("robert@harmonygames.co/<CAxkiKZL4oS6iKdMdUJ7kBsWYkh6dDRZy18PsQmK@mail.gmail.com>", "The DM says 'I'll email you how we split the money'; the mail is in Robert's inbox."),
    "JENK": sql_gmail("robert@harmonygames.co/<CAcq2o5fx1qiP_Mz3H-YKAP4-dEO1xiZLWrLKg1v@mail.gmail.com>", "The Build machines comment names jenkins; a Gmail search for 'jenkins' reaches Arthur's mail in Robert's inbox."),
    "ASC": sql_gmail("robert@harmonygames.co/<136285951.151027292.1770967800000@email.apple.com>", "Domino Delights' player support issue leads to a Gmail search for 'Domino Delights'; App Review's mail is the newest hit in Robert's inbox."),
    "RULES": sql_mutable("gdocs", "gdocs.docs_documents", {"document_id": RULES_ID}, "body_text", RULES_ID,
                         "The DM says 'the ground rules doc has how we decide'; the doc is shared with Robert.",
                         "The doc's created and modified times are both 2026-02-12T23:46:00Z, before the freeze, so the exported body is its state at the freeze; Leonard's DM (D04UP2L3E3S/1770961200.890407, later the same night) points to it as how they decide."),
    "DRAFT": sql_mutable("gdrive", "gdrive.drive_files", {"id": "f_d996e4c434ce160dc52596"}, "name", "f_d996e4c434ce160dc52596",
                         "The DM says 'lay the sheet out like my draft from Tuesday'; the draft is shared with Robert.",
                         "The draft's created and modified times are both 2026-02-10T18:30:00Z, before the freeze, so its header row (sheets_sheets grid_json, SQL L23) is its state at the freeze; Leonard's DM names it as the layout."),
    "WD134": base_slack("figma_sep11", "The ground rules make #winddown's keep/cancel decisions stand; Robert is a member.", True),
    "WD190": base_slack("action_items", "The ground rules make #winddown's keep/cancel decisions stand; Robert is a member.", True),
    "WD188": base_slack("keep_list", "The ground rules make #winddown's keep/cancel decisions stand; Robert is a member.", True),
    "WD57": base_slack("helpshift_feb28", "The ground rules make #winddown's decisions stand; Robert is a member.", True),
    "WD179": base_slack("appsflyer", "The ground rules make #winddown's decisions stand; Robert is a member.", True),
    "P575": base_slack("layer_mar3", "The layer.ai search reaches Leonard's #prototype post, the root of the thread with his reply; Robert is a member."),
    "P672": base_slack("unity_100", "The Unity Ads and playable issues lead to Leonard's #prototype post on this week's playable test; Robert is a member."),
    "DDB": base_slack("dd_boombit", "Leonard's #prototype post on Domino Delights' status; Robert is a member of #prototype."),
    "CALM": base_slack("calm_sub", "The Calm Play LLC issue leads to a Slack search for 'calm play'; Robert is a member of #admin_foundersonly."),
    "EX411": base_slack("auction", "The ground rules point to what Leonard wrote after Wednesday's call in #executives; Robert is a member.", True),
    "CL": contact(169, "leonard.hayes@harmonygames.co", "The prompt and DM name Leonard; Contacts give his address."),
    "CA": contact(168, "arthur.blake@harmonygames.co", "The prompt and DM name 'Blake'; Contacts resolve him to Arthur Blake."),
}

crit, rows = [], []
for i, r in enumerate(ROWS, 1):
    x = T[r["p"]]
    assert x["title"].startswith("The Agent "), r["p"]
    accept = x["title"][len("The Agent "):] + (f"; {x['acc_note']}" if x.get("acc_note") else "")
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
keep = os.path.join(WF, "run_forensics", "rev4", "rubric")
os.makedirs(keep, exist_ok=True)
sha = hashlib.sha256(open(out, "rb").read()).hexdigest()[:12]
shutil.copy(out, os.path.join(keep, f"09_Rubrics_{sha}.json"))
from collections import Counter
print("criteria", len(crit), "weights", dict(Counter(c["weight"] for c in crit)), "total", sum(c["weight"] for c in crit),
      "process", sum(c["category"] == "Process" for c in crit), "sha", sha, "rubric_hash", ev["rubric_hash"])
