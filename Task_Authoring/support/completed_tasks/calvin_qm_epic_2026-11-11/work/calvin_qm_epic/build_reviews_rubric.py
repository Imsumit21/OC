#!/usr/bin/env python3
"""hardness_reviews/rubric.json: the prompt-stage review carried to the rubric stage, bound to 09_Rubrics.json, with the
surface-slot -> criterion coverage taken from the plan extras (rubric_plan_extra.json)."""
import hashlib, importlib.util, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TD = os.path.dirname(WF); WS = os.path.abspath(os.path.join(TD, "..", ".."))
sys.path.insert(0, os.path.join(WS, "Task_Authoring", "tools"))
import design_readiness as dr
spec = importlib.util.spec_from_file_location("rubric_rows", os.path.join(HERE, "rubric_rows.py")); RR = importlib.util.module_from_spec(spec); spec.loader.exec_module(RR)
IDX = {r["p"]: f"R{i}" for i, r in enumerate(RR.R, 1)}
ref = lambda rel: {"path": rel, "sha256": hashlib.sha256(open(os.path.join(TD, rel), "rb").read()).hexdigest()}
M = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json"))); SF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
SQL = open(os.path.join(TD, "01_Universe_Inject.sql")).read(); P = open(os.path.join(TD, "04_Prompt.txt")).read()
RUB = json.load(open(os.path.join(TD, "09_Rubrics.json"))); EXTRA = json.load(open(os.path.join(HERE, "rubric_plan_extra.json")))
R = json.load(open(os.path.join(WF, "hardness_reviews", "prompt.json")))
R["stage"] = "rubric"
R["reviewer"] = "Claude (Fable 5.2), rubric check (Working_Files/09_Rubric_Check.md) on top of the prompt review; REDTEAM_* unset"
R["input_hashes"] = dr.input_hashes("rubric", M, SF, sql_text=SQL, prompt=P, rubric=RUB)
cov = {}
for s in SF["slots"]:
    g = EXTRA["surface"][s["id"]]
    ps = re.findall(r"\bP\d+\b", g["cov"])
    if not ps:      # G1: the 'not marked' side has no row of its own; the exact count of marked rows grades it
        ps = [RR.PN["review_count_sheet"]]
    cov[s["id"]] = {"rubric_ids": [IDX[p] for p in ps]}
R["coverage"] = cov
os.makedirs(os.path.join(WF, "hardness_reviews"), exist_ok=True)
json.dump(R, open(os.path.join(WF, "hardness_reviews", "rubric.json"), "w"), indent=1)
cfg = json.load(open(os.path.join(WF, "00_Readiness_Config.json"))); ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
rep = dr.evaluate("rubric", M, SF, R, sql_text=SQL, prompt=P, rubric=RUB, task_dir=TD, task_id=R["task_id"], revision=cfg["revision"], difficulty_mode=ctx["difficulty_mode"])
print("rubric design review", rep["verdict"], len(rep["blockers"]), rep["blockers"][:12])
