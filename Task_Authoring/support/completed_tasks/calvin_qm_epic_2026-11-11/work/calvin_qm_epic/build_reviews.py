#!/usr/bin/env python3
"""Writes Working_Files/hardness_reviews/scenario.json and 00_V3_Authoring_Evidence.json for the scenario stage.
Run after assemble_design.py. Evidence points at task-local files by sha256 (Guide/Readiness_And_Evidence.md)."""
import hashlib, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TD = os.path.dirname(WF); WS = os.path.dirname(os.path.dirname(TD))
sys.path.insert(0, os.path.join(WS, "Task_Authoring", "tools"))
import design_readiness as dr, stage_evidence as ev
from pathlib import Path
M = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json"))); SF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
SEED = json.load(open(os.path.join(HERE, "seed_text.json"))); ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
def ref(rel):
    return {"path": rel, "sha256": hashlib.sha256(open(os.path.join(TD, rel), "rb").read()).hexdigest()}
SEEDS, TRUTH, REACH, MODEL, RPT = (ref("Working_Files/plan/" + f) for f in ("seed_text.json", "truth_sketch.json", "out/reach_lb.txt", "policy_model_output.txt", "reports.py"))
pr = lambda reason, *refs, **kw: {"reason": reason, "evidence": list(refs), **kw}
sid = lambda k: SEED[k]["id"]
SEL = ["BRANCH", "INLINE", "REOPEN", "BACK", "ELSE", "FILT"]
D = {
 "BRANCH": dict(init="Rows 1, 2 and 25 read as Passed: the sheet says 'ok, chat' and Vincent wrote 'Looks ok to me' and 'Boss arena as well' in the chat.", dec=("C05433XK267/1758817549.151639", "The #builds post for Match 3D iOS Internal #1718 names Calvin's QueueManager branch; Arthur's planned rule counts only builds of the main branch."),
   chron="Arthur's rule is dated 12 Sep, the build post 25 Sep 16:25 UTC and Vincent's ok 25 Sep 17:15 UTC; Arthur merges and cuts submission builds, so his rule on which builds count governs.", path="Sheet row says 'ok, chat'; the legend sends the reader to the QA chat; Calvin's line there names #1718; a search for 1718 in #builds returns the post.",
   before="Passed", after="Waiting on QA", slots=["B1", "B2", "B3", "B4", "B5", "V1", "V2"], pair=["B1", "B3"], l="row 1 looked up against its chat line and row 25 taken from the sheet", r="row 25 looked up and row 1 taken from the sheet", kind="judgment"),
 "INLINE": dict(init="Rows 12 and 32 read as Waiting on QA: the sheet names #472 and #475, both merged, and their tickets are In Validation.", dec=(sid("inline"), "Arthur's inline review comments on #472 and #475 say the fix is not in that PR."),
   chron="The tickets and the sheet are from 30 Sep after 16:40 UTC and repeat what the dev told Vincent; Arthur's comments are separate review comments right after his approvals and merges (15:53 and 16:09 UTC; the base approval mails in Calvin's mailbox carry no comment), and he merged both PRs.", path="Brian's note asks whether a fix is in main; each PR's inline review comments, their GitHub mails in Calvin's inbox and the #zombie-prs copies return Arthur's line.",
   before="Waiting on QA", after="Waiting on a fix", slots=["I1", "I2", "I3", "I4", "I5", "V2", "V3"], pair=["I1", "I4"], l="#472's inline comments read and #475's not", r="#475's inline comments read and #472's not", kind="judgment"),
 "REOPEN": dict(init="Row 9 reads as Passed: nr on main build #1745.", dec=(sid("reopen"), "Vincent's later reply under his Sep 15 submission-issues thread says the pass popup came up on top of the gift again on Android Submission 135."),
   chron="The sheet is last changed 30 Sep 19:30 UTC, Submission #135 posts at 20:13 UTC and the reply is 21:20 UTC, on a newer build than the pass.", path="Arthur's note says a pass stands until somebody sees the bug again on a main build made after the one it passed on; Vincent's recent messages or a search for 'gift' return the reply.",
   before="Passed", after="Waiting on a fix", slots=["R1", "R2", "R3", "V1", "V3"], pair=["R1", "R3"], l="status corrected but the Why leaves the build out", r="Why names the build while the row keeps Passed", kind="judgment"),
 "BACK": dict(init="Row 29 reads as Passed: ok on main build #1750.", dec=(sid("back"), "Robert's later reply under his Sep 10 endless thread in #zombie-bugs says the home intro played again every time on Android Submission 135."),
   chron="Row 29's ok is on a 30 Sep 01:55 UTC build; Submission #135 posts at 20:13 UTC and Robert writes at 21:44 UTC.", path="The same sentence of Brian's note; a search for 'intro' or 'endless', or Robert's recent posts, return it.",
   before="Passed", after="Waiting on a fix", slots=["K1B", "K2B", "K3B", "V1", "V3"], pair=["K1B", "K3B"], l="row corrected while the area count stays at 3", r="area count right while the row keeps Passed", kind="judgment"),
 "ELSE": dict(init="Rows 13 and 38 read as Waiting on a fix: no fix named in the sheet and ZOM-572 is Todo.", dec=(sid("else_pr"), "Oliver's comment on his own PR #473 says it also has both fixes; #473 merged 30 Sep 15:41 UTC."),
   chron="Oliver comments at 15:42 UTC, right after merging; he is the dev, and Brian's note asks whether a fix is in main, and the dev says on his own merged PR that it is. Vincent's sheet, later that day, does not know it.", path="Brian's note gives the reason to read the PRs merged since the 24th; #473's conversation, or its GitHub-app copy in #zombie-prs, returns the comment.",
   before="Waiting on a fix", after="Waiting on QA", slots=["E1", "E2", "E3", "E4", "V2", "V3"], pair=["E1", "E2"], l="row 13 matched to Oliver's comment and row 38 not", r="row 38 matched and row 13 not", kind="judgment"),
 "FILT": dict(init="The report list is the 38 sheet rows.", dec=(sid("filt_dm"), "Marcus's line in his chat with Calvin on 30 Sep reports the pass icon glow staying on."),
   chron="Brian's note of 30 Sep includes any bug somebody else saw in a build and told Calvin about in a DM since the 26th; Marcus writes on 30 Sep about that day's main build.", path="The scope sentence gives the reason to read Calvin's recent 1:1 chats; the newest lines of the chat with Marcus return it.",
   before="38 reports, Season Pass with 4 open", after="the icon glow report is in, Season Pass with 5 open", slots=["F1", "F2", "F3", "V3", "V7"], pair=["F1", "F2"], l="report listed in the sheet with no sub-issue", r="sub-issue filed and the sheet row left out", kind="judgment"),
 "ALIAS": dict(init="Rows 11 and 20 have no key in the sheet, so each needs a new sub-issue.", dec=(sid("alias_gift"), "Vincent's notes on base tickets ZOM-556 and ZOM-560 tie his rows to those tickets."),
   chron="Both notes are 30 Sep around 18:05 UTC, on tickets Vincent himself filed on 22 Sep.", path="Brian's note says to move a ticket that already has the report; a Linear search by area returns both tickets and their comments carry the tie.",
   before="new sub-issue", after="note on the existing ticket", slots=["A1", "A2", "A3"], pair=None, kind="judgment"),
 "GATE": dict(init="Collect & Win and Daily Gift are the review's areas, as Brian wrote on 29 Sep and the first invitation repeats.", dec=(sid("rev_card_update"), "Leonard changed his review card on 30 Sep: Collect & Win and Level-end rewards."),
   chron="first invitation 29 Sep 16:05 UTC, Brian's line 29 Sep 16:41 UTC, card changed 30 Sep 17:22 UTC; the updated invitation says the agenda is on the roadmap card.", path="Brian's note names the agenda of Thursday's review, and the updated invitation says the agenda is on the roadmap card; a Trello search for the review returns it, and the updated invitation says the card changed.",
   before="not on the review list", after="on the review list", slots=["G1", "G2", "V4"], pair=None, kind="judgment"),
}
mech = {}
for m, d in D.items():
    row = {
     "initial_plausible_answer": pr(d["init"], RPT, SEEDS),
     "deciding_evidence": pr(d["dec"][1], SEEDS, REACH, record_id=d["dec"][0]),
     "authority_chronology": pr(d["chron"], SEEDS),
     "fair_discovery_path": pr(d["path"], SEEDS, REACH),
     "changed_outcome": pr("The planned truth and the natural reading differ on the slots listed.", TRUTH, before=d["before"], after=d["after"]),
     "independent_operation": pr("Its deciding record is in a different container by a different author from every other channel; missing it changes only its own rows and the counts.", SEEDS, MODEL, others_solvable_if_missed=[x for x in SEL if x != m]),
     "outcome_slots": d["slots"], "channel_kind": d["kind"],
     "access": {"status": "deferred", "required_at": "injection"}, "natural_retrieval": {"status": "deferred", "required_at": "injection"},
    }
    if d["pair"]:
        row["outcome_pair"] = pr("The two slots are separate facts; one can be right while the other is wrong.", TRUTH, slots=d["pair"], left_pass_right_fail=d["l"], right_pass_left_fail=d["r"])
    mech[m] = row
cfg = json.load(open(os.path.join(WF, "00_Readiness_Config.json")))
review = {"schema_version": 1, "stage": "scenario", "task_id": ev.task_identity(Path(TD)), "revision": cfg["revision"],
 "reviewer": "Claude (Fable 5.2), self-review with two blind fresh-agent sweeps (plan/sweeps); REDTEAM_* unset", "difficulty_mode": ctx["difficulty_mode"],
 "diversity_channels": SEL, "mechanisms": mech, "dispositions": {}, "forecast": {"ledger_id": "hev_629545c85e58f03d", "note": "UNCALIBRATED"},
 "input_hashes": dr.input_hashes("scenario", M, SF)}
os.makedirs(os.path.join(WF, "hardness_reviews"), exist_ok=True)
json.dump(review, open(os.path.join(WF, "hardness_reviews", "scenario.json"), "w"), indent=1)
rep = dr.evaluate("scenario", M, SF, review, task_dir=TD, task_id=review["task_id"], revision=cfg["revision"], difficulty_mode=ctx["difficulty_mode"])
print("design review", rep["verdict"], rep["blockers"][:8], "deferred", len(rep["deferred"]))
ah = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", os.path.join(WF, "01_Scenario_Design.md")], cwd=WS, capture_output=True, text=True).stdout.strip().split()[-1]
E3 = {"spec_version": "V3", "context_hash": ctx["context_hash"], "role_reviews": {"scenario": {
 "artifact": "01_Scenario_Design.md", "artifact_hash": ah,
 "reviewer": "Claude (Fable 5.2), self-review plus two independent fresh-agent sweeps (REDTEAM_* unset; design section 13)",
 "persona_role": ctx["persona_role"],
 "rationale": "Calvin is the Unity VFX and live-ops engineer who owns ZOM-543, the ZM Queue Manager. He wrote and merged match3d#459 and opened #465 and #472, Brian asked him to take the queue manager on (D0770ET6WBW/1758730948.999939), and QA reports its problems to him directly (D06UPGF5PQV/1758806199.381319). Turning his own ticket into an epic and saying where each QA report stands is engineering ticket work on his own feature, inside Engineering Ops. He is active at the clock: #472 merged on 30 Sep and his last chat line is D0770ET6WBW/1759173921.310649. Brian asked for the flow pass himself (D0770ET6WBW/1758658894.879649).",
 "source_ids": ["ZOM-543", "harmonygames-Games/match3d#459", "harmonygames-Games/match3d#472", "D0770ET6WBW/1758730948.999939", "D06UPGF5PQV/1758806199.381319", "D05HYDTG5TJ/1756838837.147599"]}}}
json.dump(E3, open(os.path.join(WF, "00_V3_Authoring_Evidence.json"), "w"), indent=1)
print("evidence written, artifact hash", ah)
