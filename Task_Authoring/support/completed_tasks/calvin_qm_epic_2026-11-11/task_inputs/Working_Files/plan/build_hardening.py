#!/usr/bin/env python3
"""MODE B (pre-check) artifacts for rev1: reviewed proxy matrix, export review receipt, mode_b_request.json,
dispositioned ledger records and Working_Files/01a_Hardening_Report.md. Proposes only; /create-scenario --revise decides."""
import json, os, sys, hashlib, subprocess
from pathlib import Path
HERE = Path(__file__).resolve().parent; WF = HERE.parent; TD = WF.parent; WS = TD.parent.parent
sys.path.insert(0, str(WS / "Task_Authoring" / "tools"))
import difficulty_stats as st, trajectory_ledger as tl, stage_evidence as ev
from design_readiness import digest
RF = WF / "run_forensics" / "rev1"; TRJ = TD / "06_PreCheck_Trajectory" / "trajectory.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
ref = lambda rel: {"path": rel, "sha256": sha(TD / rel)}
ctx = json.load(open(WF / "00_Task_Context.json")); cfg = json.load(open(WF / "00_Readiness_Config.json"))
SF = json.load(open(WF / "01_Gradable_Surface.json")); slots = SF["slots"]
calls = [json.loads(l) for l in open(RF / "precheck" / "calls.jsonl")]
EXP = json.load(open(TRJ)); ESHA = sha(TRJ)
status, _, det = st.read_trajectory(TRJ)
# hand-reviewed results: the local decoder read only the last sheet update (the Areas tab) and reworded titles, so its 21 failures
# were checked against the write payloads (writes.json) and the platform /hardness requirement map; all 51 slots are met (D3, the reply's destination, is the DM D0770ET6WBW at event 502).
results = {s["id"]: True for s in slots}
data = {"spec_version": ctx["spec_version"], "difficulty_mode": ctx["difficulty_mode"], "task_type": ctx["task_type"],
        "rubrics": [{"id": s["id"], "title": s["id"] + " " + json.dumps(s["selector"])[:80], "weight": s["weight"]} for s in slots],
        "rollouts": [{"id": "run-1", "status": status, "tool_calls": det["counted"], "models": st.trajectory_models(TRJ), "results": results}]}
(RF / "precheck.matrix.json").write_text(json.dumps(data, indent=1))
bundle = tl.binding_bundle_hash(TD, stage="precheck"); task_id = ev.task_identity(TD)
REFS = [ref("06_PreCheck_Trajectory/trajectory.json"), ref("Working_Files/run_forensics/rev1/precheck/writes.json"), ref("Working_Files/platform_reports/hardness_rev1_FAIL2.md")]
receipt = {"kind": "PRECHECK_EXPORT_REVIEW", "schema_version": 1, "task_id": task_id, "revision": cfg["revision"], "bundle_hash": bundle,
           "reviewer": "Claude (Fable 5.2), full read of the call ledger and write payloads, cross-checked with the platform /hardness report",
           "reason": "The export is one complete Opus 5.5 run bound to rev1 by seeded content; every surface slot was checked against the decoded write payloads, and the local decoder's 21 failures are all decoder defects.",
           "evidence": REFS, "export_sha256": ESHA, "source_matrix_sha256": digest(data)}
(RF / "precheck.receipt.json").write_text(json.dumps(receipt, indent=1))
def res_event(n):
    return calls[n - 1]["result_event"]
def evq(n, quote):
    i = res_event(n); assert quote in json.dumps(EXP[i], ensure_ascii=False), (n, quote)
    return {"run": "run-1", "export_sha256": ESHA, "event": i, "quote": quote}
W5 = {m: [s["id"] for s in slots if s["weight"] == 5 and m in (s.get("mechanisms") or [])] for m in ("BRANCH", "INLINE", "REOPEN", "BACK", "ELSE", "FILT", "ALIAS", "GATE")}
DG = [
 ("DX-NOTE", "Brian's note on ZOM-543 states each resolver as a check to run (check the PR and its review, a dev's own merged PR, a later 'it is back', a ticket under another name, DMs since the 26th, Leonard's review card), so every trap became a lookup", sorted(set(W5["INLINE"] + W5["ELSE"] + W5["ALIAS"])), [evq(7, "How I want this epic"), evq(43, "in this diff"), evq(52, "bar filling before the tokens land")], "heavy_all_pass"),
 ("DX-SWEEP", "The come-back reports and the DM report sat in containers the run read whole: channel history since Sep 23, the thread under a Sep 30 root, and every DM after Sep 25", sorted(set(W5["REOPEN"] + W5["BACK"] + W5["FILT"])), [evq(29, "home intro animation played again"), evq(32, "came up on top of the gift again"), evq(37, "pass icon glow stays on")], "first_read_correction"),
 ("DX-BRANCH", "The note names Arthur's rule, the run kept looking until it found the doc, and one PR listing returned the head branch of #465; the chat line names build #1718", W5["BRANCH"], [evq(74, "only counts on a build of the main branch"), evq(39, "QueueManager")], "heavy_all_pass"),
 ("DX-GATE", "The note names Leonard's review card and one Trello search for 'review' returned the changed card", W5["GATE"], [evq(89, "Level-end rewards")], "heavy_all_pass"),
]
diagnoses = [{"id": i, "mechanism": m, "criteria": c, "trajectory_events": e, "observation": o, "reason": m, "evidence": REFS} for i, m, c, e, o in DG]
RR = ["scenario", "injection", "prompt-check", "precheck"]
RP = [
 ("RP1", "DX-NOTE", "resolver sentences inside Brian's note comment_faaa792418a942cd40be046d8d217a7d", "keep the note to plain definitions of the three statuses; let the facts settle rows 12, 32, 13 and 38 (Arthur's review comments, Oliver's comment) with no sentence telling the reader to check them", "placement", "a search for the row's own words in GitHub or #zombie-prs returns each comment; the status definition 'the fix is merged' is the reason to look"),
 ("RP2", "DX-SWEEP", "come-backs in a channel post and a thread reply dated Sep 30, inside the swept window", "record one come-back where the run did not read (a comment on the report's own ticket) and add one 'it is back' on a build older than the pass, which leaves the pass standing", "placement", "the ticket named in the row's own Ticket cell carries the comment; the build's post in #builds gives its time"),
 ("RP3", "DX-BRANCH", "three 'ok, chat' rows resolved by one rule doc and one build post", "add a done source with a missing piece (A24): a fix PR that is merged but whose re-test build predates the merge, or a merge into a branch that is not main, so 'merged' and 'on a main build' have to be checked per row", "done_gap", "the PR's merge time and base branch in GitHub, the build's time and branch in #builds"),
 ("RP4", "DX-GATE", "the note names Leonard's review card", "name only the review's agenda in the note; the updated invitation says the agenda moved to the roadmap card", "placement", "Calvin's updated invitation and calendar event point at the roadmap card"),
]
repairs = [{"id": i, "diagnosis": d, "artifact": "universe", "owner": "create-scenario --revise", "original_placement": o, "proposed_change": p, "change_kind": k,
            "affected_outcomes": next(x[2] for x in DG if x[0] == d), "scope_difference": {"reason_class": "difficulty", "before": o, "after": p},
            "fair_discovery_path": f, "required_reruns": RR, "reason": p, "evidence": REFS} for i, d, o, p, k, f in RP]
req = {"task_id": task_id, "revision": cfg["revision"], "bundle_hash": bundle, "precheck": True, "data_path": "Working_Files/run_forensics/rev1/precheck.matrix.json",
       "receipt": "Working_Files/run_forensics/rev1/precheck.receipt.json", "trajectories": ["06_PreCheck_Trajectory/trajectory.json"], "diagnoses": diagnoses, "repairs": repairs}
(WF / "mode_b_request.json").write_text(json.dumps(req, indent=1))
r = subprocess.run(["python3", "-B", "Task_Authoring/tools/mode_b_report.py", "--task-dir", str(TD), "--request", str(WF / "mode_b_request.json"), "--out", str(WF / "Mode_B_Diagnosis.json")], cwd=WS, capture_output=True, text=True)
MB = json.load(open(WF / "Mode_B_Diagnosis.json")) if (WF / "Mode_B_Diagnosis.json").exists() else {}
print("mode_b", MB.get("verdict"), MB.get("blockers"), r.stderr[-300:])
# dispositioned ledger records
recs = [json.loads(l) for l in open(RF / "precheck.proposals.jsonl")]
for x in recs:
    if x["kind"] == "verdict" and x["node"] == "FILT":
        x["verdict"] = "LEAKED"; x.setdefault("features", {})["disposition_note"] = "tool proposed BYPASSED because the run reworded the report's title; the payload at event 469 has the report, its area and status, found through the DM search at call 37"
    if x["kind"] == "verdict" and x["node"] == "ALIAS":
        x["features"]["disposed_by"] = "Claude (Fable 5.2): the pending key is a representation difference, the run wrote the new sub-issue's key ZOM-602 in the Ticket cell where the solver holds no key; not a mechanism error"
    x.setdefault("features", {})["reviewed_by"] = "Claude (Fable 5.2), build_hardening.py"
(RF / "precheck.dispositioned.jsonl").write_text("".join(json.dumps(x) + "\n" for x in recs))
json.dump({"calls": {k: res_event(v) for k, v in dict(NOTE=7, BACK=29, REOPEN=32, FILT=37, PRLIST=39, IN472=43, IN475=44, ELSE=52, RULE=74, CARD=89, ZOM556=93).items()}, "counted": det["counted"], "mode_b": MB.get("verdict")}, open(RF / "precheck.events.json", "w"))
