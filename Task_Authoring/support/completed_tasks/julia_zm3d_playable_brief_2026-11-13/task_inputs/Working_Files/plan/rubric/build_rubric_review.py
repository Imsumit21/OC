#!/usr/bin/env python3
"""Write Working_Files/hardness_reviews/rubric.json: the prompt-stage design review carried to the final 153-row rubric.

Adds what the rubric stage requires (tools/design_readiness.py): the rubric input hash, the coverage of every surface
slot by final criteria (or its sampled-out record), and outcome pairs whose two sides are graded by different criteria.
Two pairs change because the platform's round 1 Fix List cut the State samples they used (Cello and Rocket sound)."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_model as C                    # noqa: E402
import build_check as B                    # noqa: E402  (re-writes the check report and evidence; same inputs, same bytes)
import design_readiness as DR              # noqa: E402
import stage_gate as SG, readiness_controls as RC   # noqa: E402
TASK, WF = C.TASK, C.WF
sha = lambda p: hashlib.sha256((TASK / p).read_bytes()).hexdigest()
ref = lambda p: {"path": p, "sha256": sha(p)}

review = json.loads((WF / "hardness_reviews" / "prompt.json").read_text())
manifest = json.loads((WF / "01_Hardness_Manifest.json").read_text())
surface = json.loads((WF / "01_Gradable_Surface.json").read_text())
rubric = json.loads((TASK / "09_Rubrics.json").read_text())
review["stage"] = "rubric"
review["reviewer"] = ("build agent (Claude), /create-rubric-writing check on 2026-11-13, on top of the prompt-stage review; the rubric itself was reviewed by the "
                      "platform /rubric (round 2, NON-FAIL 3) and graded by the baseline verifier before this local check")
review["input_hashes"] = DR.input_hashes("rubric", manifest, surface, sql_text=(TASK / "01_Universe_Inject.sql").read_text(),
                                         prompt=(TASK / "04_Prompt.txt").read_text(), rubric=rubric)
PAIR_EV = [ref("01_Universe_Inject.sql"), ref("09_Rubrics.json"), ref("Working_Files/oe_gen/model.py")]
review["mechanisms"]["AUDIO"]["outcome_pair"] = {
    "reason": "What is owed for the Rocket sound and who has it are separate cells of the hand-off list and separate facts on Calvin's sheet: the Replacement column says 'not made yet, Calvin', the source column names Robert's library seat. One can be right while the other is wrong. The earlier pair used the Rocket sound State cell, whose row the platform's round 1 Fix List cut when it reduced the State group to five samples.",
    "evidence": PAIR_EV, "slots": ["X10", "X12"],
    "left_pass_right_fail": "the list says our own version of the Rocket sound is owed and names Robert, whose library seat the cue came from, as who has it",
    "right_pass_left_fail": "the list names Calvin as who has it and gives 'the .wav again' as what is owed"}
review["mechanisms"]["ZIP"]["outcome_pair"] = {
    "reason": "What is owed for Cello and who has it are separate cells and separate statements in Brian's log: the zip 'got cut off on upload' and 'I still have Claire's files, I'll put them back'. One can be right while the other is wrong. The earlier pair used the Cello State cell, whose row the platform's round 1 Fix List cut when it reduced the State group to five samples.",
    "evidence": PAIR_EV, "slots": ["X9", "X17"],
    "left_pass_right_fail": "the list says the Cello file has to go back in the outgoing folder and names Claire, whose files they were, as who has it",
    "right_pass_left_fail": "the list names Brian as who has it and gives a binary re-export, the reason for the Thursday saves, as what is owed"}

SAMPLE_EV = [ref("eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric.md"), ref("Working_Files/plan/rubric/fix_round1_map.json"), ref("09_Rubrics.json")]
coverage = {}
for line in B.surface_lines:
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    sid, crit, state, reason = c[0], c[2], c[3], c[4]
    ks = [int(x) for x in re.findall(r"C(\d+)", crit)]
    if state == "covered":
        coverage[sid] = {"rubric_ids": [f"R{k}" for k in ks]}
    elif sid in B.SAMPLED_OUT:
        coverage[sid] = {"status": "sampled_out", "reason": reason, "evidence": SAMPLE_EV}
    elif sid == "B6":
        coverage[sid] = {"rubric_ids": ["R21", "R22", "R23"],
                         "note": "The three usable-sound rows grade what the brief says PlayableX can use. The held-back half of the section has no brief row (it would accept by absence); it is graded on the list and the tickets, and /rubric round 2 scores the brief side as a Minor overly_broad note."}
    else:   # the three count slots on the list: the count is graded once, in the DM
        ids = [f"R{k}" for k in sorted({int(x) for x in re.findall(r"C(\d+)", reason)})]
        assert ids, sid
        coverage[sid] = {"rubric_ids": ids, "note": reason}
review["coverage"] = coverage
out = WF / "hardness_reviews" / "rubric.json"
out.write_text(json.dumps(review, indent=1, ensure_ascii=False) + "\n")

ctx = SG.Ctx("rubric-check", TASK.resolve())
assert SG.assignment_context(ctx)
res = RC.design_review(SG, ctx, "rubric")
print("design review (rubric):", res["verdict"], "| blockers:", res["blockers"][:12], "| deferred:", res["deferred"])
print("coverage:", sum(1 for v in coverage.values() if "rubric_ids" in v), "direct,", sum(1 for v in coverage.values() if v.get("status") == "sampled_out"), "sampled out")
