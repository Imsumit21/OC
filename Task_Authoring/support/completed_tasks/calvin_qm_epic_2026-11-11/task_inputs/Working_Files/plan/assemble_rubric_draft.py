#!/usr/bin/env python3
"""Draft mode: write task_inputs/09_Rubrics.json from the plan rows (rubric_rows.py) and record the V3 rubric_rows evidence in
Working_Files/00_V3_Authoring_Evidence.json (calvin_qm_epic, rev3b). Every source_value is re-read in this run: seeded fields from
the parsed SQL (never executed), base fields from plan/oe_base.json (tools/hg.py reads by oe_reads.py)."""
import hashlib, importlib.util, json, os, re, shutil, sys
from collections import Counter
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF)
sys.path.insert(0, os.path.join(TI, "..", "tools")); sys.path.insert(0, HERE)
from base_check import parse_sql
import stage_gate as SG
import reports as RP
spec = importlib.util.spec_from_file_location("rubric_rows", os.path.join(HERE, "rubric_rows.py")); RR = importlib.util.module_from_spec(spec); spec.loader.exec_module(RR)
ROWS = RR.R
ST = [x for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()) if x["op"] == "insert"]
OB = json.load(open(os.path.join(HERE, "oe_base.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json"))); ID = {k: v["id"] for k, v in SEED.items()}
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
T = {r["n"]: r for r in RP.truth()}
def tr(n): return TRUTH[T[n]["report"]]
REVIEWER = "Claude (model-drafted under GEN_EXECUTION §2; for the human author's review)"
HUB_ID = ID["hub"]; HUB_STEP = {"service": "slack", "id": HUB_ID}
NOTE_STEP = {"service": "linear", "id": "ZOM-543"}
FREEZE = "the freeze 2025-10-01T07:00:00Z"
def sqlrow(table, **ident):
    rs = [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rs) == 1, (table, ident, len(rs)); return rs[0]
def sql_slack(rid, why, path=None):
    chan, ts = rid.split("/"); r = sqlrow("slack.slack_messages", channel_id=chan, ts=ts)
    return {"service": "slack", "id": rid, "source_file": "01_Universe_Inject.sql", "table": "slack.slack_messages", "identity": {"channel_id": chan, "ts": ts}, "column": "text", "source_value": r["text"],
            "evidence_path": [HUB_STEP] + (path or []) + ([{"service": "slack", "id": rid}] if rid != HUB_ID else []), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "created_at", "rationale": f"Seeded Slack message; created_at {r['created_at']} is before {FREEZE}; a posted message with no edit."}}
def sql_on(service, rid, table, ident, column, recorded, why, path=None):
    r = sqlrow(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column, "source_value": r[column], "evidence_path": [HUB_STEP] + (path or []) + [{"service": service, "id": rid}],
            "reachability_rationale": why, "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": recorded, "rationale": f"Seeded {table} row on {rid}; {recorded} {r[recorded]} is before {FREEZE}; a posted record with no edit."}}
def sql_mutable(service, table, ident, column, rid, recorded, why, extra, path=None):
    r = sqlrow(table, **ident)
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column, "source_value": r[column], "evidence_path": [HUB_STEP] + (path or []) + [{"service": service, "id": rid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_column": recorded, "rationale": f"Seeded {table} row; {recorded} {r[recorded]} is before {FREEZE}.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": extra, "evidence_ids": [rid, HUB_ID]}}}
def base_build(rid, why):
    v = OB["slack"][rid]
    return {"service": "slack", "id": rid, "source_file": v["file"], "pointer": f"{v['pointer']}/ts", "source_value": v["rec"]["ts"], "evidence_path": [HUB_STEP, NOTE_STEP, {"service": "slack", "id": rid}],
            "reachability_rationale": why + " The cited field is the post's ts (which build post, and when); the job, number and branch are the post's one line, which the Slack tools return with the message.", "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"{v['pointer']}/ts", "rationale": f"Base #builds post; ts {v['rec']['ts']} is before {FREEZE}; a posted bot message."}}
def base_pr(n, why):
    v = OB["github"][n]; rid = f"harmonygames-Games/match3d#{n}"
    return {"service": "github", "id": rid, "source_file": v["file"], "pointer": f"{v['pointer']}/merged_at", "source_value": v["rec"]["merged_at"], "evidence_path": [HUB_STEP, NOTE_STEP, {"service": "github", "id": rid}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{v['pointer']}/merged_at", "rationale": f"Base pull request; merged_at {v['rec']['merged_at']} is before {FREEZE}, and a merge does not change afterwards.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": f"#{n} was merged before the freeze; the SQL changes only its updated_at (and, for #472, its description), not the merge.", "evidence_ids": [rid]}}}
def base_linear(k, why):
    v = OB["linear"][k]
    return {"service": "linear", "id": k, "source_file": v["file"], "pointer": f"{v['pointer']}/state_id", "source_value": v["rec"]["state_id"], "evidence_path": [HUB_STEP, {"service": "linear", "id": k}], "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": f"{v['pointer']}/updated_at", "rationale": f"Base Linear issue; updated_at {v['rec']['updated_at']} is before {FREEZE}, so the exported state is its state at the freeze.",
                                  "state_at_freeze_review": {"reviewer": REVIEWER, "rationale": f"The SQL touches only {k}'s updated_at (a comment was added); the base state_id is the state at the freeze.", "evidence_ids": [k]}}}
SEEDED_T = {x["row"]["id"] for x in ST if x["table"] == "linear.linear_issues"}
W_NOTE = "The prompt names the Queue Manager ticket and Brian's DM says he left a note on it; the comment sits on ZOM-543."
SEEDED_NOTE = " The ticket is seeded by this task's SQL (team ZOM, where Calvin is a member), so the reach proof ends at Vincent's flow pass sheet, whose Ticket column names it; the cited field is the seeded Linear row."
SHEET_ID = ID["sheet"]
def lin_comment(key, issue, why):
    if issue in SEEDED_T: return sql_on("gsheets", SHEET_ID, "linear.linear_comments", {"id": ID[key]}, "body", "created_at", why + SEEDED_NOTE, [NOTE_STEP])
    return sql_on("linear", issue, "linear.linear_comments", {"id": ID[key]}, "body", "created_at", why, [NOTE_STEP] if issue != "ZOM-543" else None)
def tick(k): return sql_mutable("gsheets", "linear.linear_issues", {"id": k}, "state_id", SHEET_ID, "updated_at", f"Vincent's flow pass sheet names {k} in its Ticket column; the note sends the Agent to the tickets that already hold a report." + SEEDED_NOTE,
                                f"{k} was filed by Vincent on Sep 30 2025 and last touched before the freeze; its seeded state_id is its state at the freeze.", [NOTE_STEP])
CAT = {
 "HUB": sql_slack(HUB_ID, "The prompt names Brian's message from yesterday; Calvin is a party to the DM."),
 "NOTE": lin_comment("epic_note", "ZOM-543", W_NOTE),
 "SHEETF": sql_mutable("gsheets", "gdrive.drive_files", {"id": ID["sheet"]}, "name", ID["sheet"], "modified_time", "Brian's note names Vincent's flow pass sheet; it is shared with Calvin.", "The sheet was last modified 2025-09-30T19:30:52Z, before the freeze; the grid in the SQL is its content at the freeze.", [NOTE_STEP]),
 "RULE": sql_mutable("gdocs", "gdocs.docs_documents", {"document_id": ID["rule_doc"]}, "body_text", ID["rule_doc"], "modified_time", "Brian's note names Arthur's rule for QA passes; the doc is shared with Calvin.", "The doc's modified time is before the freeze, so its body is its state at the freeze.", [NOTE_STEP]),
 "INLINE": sql_on("github", "harmonygames-Games/match3d#472", "github.github_review_comments", {"id": ID["inline"]}, "body", "created_at", "The sheet's Fix column names #472 and the note asks whether a fix is in main; the review comment sits on that pull request.", [NOTE_STEP]),
 "INLINE2": sql_on("github", "harmonygames-Games/match3d#475", "github.github_review_comments", {"id": ID["inline2"]}, "body", "created_at", "The sheet's Fix column names #475 and the note asks whether a fix is in main; the review comment sits on that pull request.", [NOTE_STEP]),
 "ELSE": sql_on("github", "harmonygames-Games/match3d#473", "github.github_pr_comments", {"id": ID["else_pr"]}, "body", "created_at", "The note asks whether a fix is in main; #473 merged into main on Sep 30 and Oliver's comment sits in its conversation.", [NOTE_STEP]),
 "REOPEN": sql_slack(ID["reopen"], "Arthur's rule ends a pass when the bug is seen again on a later main build; Vincent's reply is in #zombie-bugs, which Calvin is in.", [NOTE_STEP]),
 "BACK": sql_slack(ID["back"], "Arthur's rule ends a pass when the bug is seen again on a later main build; Robert's reply is in #zombie-bugs, which Calvin is in.", [NOTE_STEP]),
 "OLDER": sql_slack(ID["older"], "Arthur's rule ends a pass only on a later main build; Robert's post is in #zombie-match3d, which Calvin is in.", [NOTE_STEP]),
 "GLOW": sql_slack(ID["filt_dm"], "Brian's note takes in a bug told to Calvin in a DM since the 26th; Marcus's message is in Calvin's DM with him.", [NOTE_STEP]),
 "REOPEN2": lin_comment("reopen2", "ZOM-585", "The sheet names ZOM-585 for row 17; Samuel's later note sits on that ticket."),
 "BACK2": lin_comment("back2", "ZOM-586", "The sheet names ZOM-586 for row 24; Owen's later note sits on that ticket."),
 "ALIAS_GIFT": lin_comment("alias_gift", "ZOM-556", "The note asks whether a ticket already has the report; Vincent's note on ZOM-556 ties row 11 to it."),
 "ALIAS_STREAK": lin_comment("alias_streak", "ZOM-560", "The note asks whether a ticket already has the report; Vincent's note on ZOM-560 ties row 20 to it."),
 "Z556": base_linear("ZOM-556", "A search of the ZM tickets for the daily gift reaches ZOM-556."), "Z560": base_linear("ZOM-560", "A search of the ZM tickets for the freezer reaches ZOM-560."),
 "B1718": base_build("C05433XK267/1758817549.151639", "Arthur's rule says the branch is in the build's #builds post; Calvin is in #builds."),
 "B135": base_build("C05433XK267/1759263189.219529", "The later sightings name Android Submission 135; its #builds post gives its branch and time."),
 "B2006": base_build("C05433XK267/1759160363.685759", "Robert's post names Android 2006; its #builds post gives its time."),
 "B2013": base_build("C05433XK267/1759188882.419789", "Row 18's re-test names Android #2013; its #builds post gives its time."),
 "B1757": base_build("C05433XK267/1759257787.502039", "Row 34's re-test names iOS Internal #1757; its #builds post gives its time."),
 "B1745": base_build("C05433XK267/1759162758.968639", "Several re-tests name iOS Internal #1745; its #builds post gives its branch."),
 "PR465": base_pr("465", "The sheet's Fix column names #465."), "PR472": base_pr("472", "The sheet's Fix column names #472."), "PR475": base_pr("475", "The sheet's Fix column names #475."), "PR473": base_pr("473", "#473 is one of the pull requests merged into main since the pass began."),
 "INVITE": sql_on("gmail", ID["invite_v2"], "gmail.gmail_messages", {"id": ID["invite_v2"]}, "body_text", "date", "The prompt and Brian's DM name the review invite; it is in Calvin's inbox."),
 "EVT": sql_mutable("gcal", "gcal.gcal_events", {"event_id": ID["event"]}, "attendees_json", ID["event"], "updated", "The prompt names everyone on the review invite; the event is on Calvin's calendar.", "The event was last updated 2025-09-30T17:24:03Z, before the freeze, so its attendee list is the list at the freeze; the review itself starts after the clock."),
 "FOLDER": sql_mutable("gdrive", "gdrive.drive_files", {"id": ID["folder"]}, "name", ID["folder"], "modified_time", "The prompt names 'my ZM queue manager folder'; Calvin owns it.", "The folder was created on Sep 23 2025 and not modified after; its name is its state at the freeze."),
 "DECK": sql_mutable("gslides", "gdrive.drive_files", {"id": ID["deck"]}, "name", ID["deck"], "modified_time", "The prompt names 'my queue manager deck'; Calvin owns it and it sits in that folder.", "The deck was last modified on Sep 23 2025, before the freeze."),
}
for k in [x["row"]["id"] for x in ST if x["table"] == "linear.linear_issues"]: CAT["K_" + k] = tick(k)
crit, rows = [], []
REV = json.load(open(os.path.join(HERE, "out", "09_Rubrics.draft1_afbc830d0cbb.json")))
for i, r in enumerate(ROWS, 1):
    assert r["title"].startswith("The Agent "), r["p"]
    c = {"title": r["title"], "category": "Process" if r["cat"].startswith("Process") else "Outcome", "weight": r["band"], "justification": r["just"], "evidence": r["evidence"]}
    if r.get("lock") and r["fact"] != "sub_create:39" and not r["title"].startswith("The Agent sets ZOM-"): assert c == REV[r["lock"] - 1], (r["p"], r["lock"])      # an untouched row is byte-identical to the reviewed row
    crit.append(c)
    rej = r["evidence"].split("Reject:")[-1].strip()
    rows.append({"criterion_id": f"C{i}", "plan_row": r["p"], "fact_id": r["dup"].split(" ×")[0] if "×2" in r["dup"] else r["fact"], "prompt_span": r["span"], "accepted_outcomes": [r["valid"]], "alternatives_review": "Reject: " + rej + " Counter-reading: " + r["cr"],
                 "source_records": [CAT[k] for k in dict.fromkeys(r["srcs"])], "oe_steps": [f"OE {n}" for n in sorted(set(r["oe"]))], "valid_case": r["valid"], "do_nothing_case": r["idle"], "reachability": r["reach"]})
assert len({c["title"] for c in crit}) == len(crit)
out = os.path.join(TI, "09_Rubrics.json")
open(out, "w").write(json.dumps(crit, indent=1, ensure_ascii=False) + "\n")
ev_path = os.path.join(WF, "00_V3_Authoring_Evidence.json"); ev = json.load(open(ev_path))
ev["rubric_hash"] = SG.file_digest(Path(out)); ev["prompt_hash"] = SG.file_digest(Path(TI) / "04_Prompt.txt"); ev["rubric_rows"] = rows
open(ev_path, "w").write(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
keep = os.path.join(WF, "run_forensics", "rev3", "rubric"); os.makedirs(keep, exist_ok=True)
sha = hashlib.sha256(open(out, "rb").read()).hexdigest()[:12]; shutil.copy(out, os.path.join(keep, f"09_Rubrics_{sha}.json"))
fc = Counter(x["fact_id"] for x in rows); assert max(fc.values()) <= 2, [k for k, v in fc.items() if v > 2]
print("criteria", len(crit), "weights", dict(Counter(c["weight"] for c in crit)), "total", sum(c["weight"] for c in crit), "process", sum(c["category"] == "Process" for c in crit), "sha", sha)
