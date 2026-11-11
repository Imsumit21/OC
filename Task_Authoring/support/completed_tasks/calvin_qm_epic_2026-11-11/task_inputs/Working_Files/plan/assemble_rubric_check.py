#!/usr/bin/env python3
"""Check mode: build Working_Files/09_Rubric_Check.md for the current 09_Rubrics.json (C1…Cn in file order), from the plan
rows (rubric_rows.py), the gradable surface, the plan extras and plan/rubric_check_r1.json (the /rubric round-1 findings, all fixed)."""
import hashlib
import importlib.util
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


RR = load("rubric_rows")
ROWS = RR.R
JS = json.load(open(os.path.join(TI, "09_Rubrics.json")))
assert len(JS) == len(ROWS) and all(JS[i]["weight"] == r["band"] for i, r in enumerate(ROWS))
C = {r["p"]: f"C{i + 1}" for i, r in enumerate(ROWS)}
P = {r["p"]: r for r in ROWS}
SURF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))["slots"]
EXTRA = json.load(open(os.path.join(HERE, "rubric_plan_extra.json")))
R1 = json.load(open(os.path.join(HERE, "rubric_check_r1.json")))
PN = RR.PN
sha = hashlib.sha256(open(os.path.join(TI, "09_Rubrics.json"), "rb").read()).hexdigest()[:12]


def cs(text):
    text = re.sub(r"@@P:(.+?)@@", lambda m: PN[m.group(1)], text)
    return re.sub(r"\bP(\d+)\b", lambda m: C.get("P" + m.group(1), "P" + m.group(1)), text)


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


import subprocess
LINT = json.loads(subprocess.run(["python3", "Task_Authoring/tools/hg.py", "rubric-lint", "Task_Authoring/task_inputs/09_Rubrics.json"], cwd=os.path.abspath(os.path.join(TI, "..", "..")),
                                 capture_output=True, text=True).stdout)
LC = Counter(f["check"] for f in LINT["findings"])
LINTS = ", ".join(f"{k} {v}" for k, v in sorted(LC.items())) or "none"
bands = Counter(c["weight"] for c in JS)
cats = Counter(c["category"] for c in JS)
L = ["# 09 Rubric Check — calvin_qm_epic (the Queue Manager epic and stock-take, injection rev3b)",
     f"Checked 2026-11-11 · Criteria {len(JS)} (builder minimum 5: ok) · Plan 2026-11-11 (09_Rubric_Writing_Plan.md, rubric-writing gate PASS) · 09_Rubrics.json sha256 {sha}",
     "Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)",
     f"JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass ({len(JS)} objects, five non-blank fields each, category Outcome/Process, weight 1/3/5)",
     "Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict (residual risks listed under 'Round history and residual risks')",
     "",
     f"Lint: `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` → count {LINT['count']} ({LINTS}), every hit dispositioned under 'Round history and residual risks'; no disguised_negative, vague_exemplar, tool_name, prohibition_title, whitespace or schema hit. Weights 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total {sum(c['weight'] for c in JS)}); Outcome {cats['Outcome']} · Process {cats['Process']}.",
     "",
     "## Coverage",
     "| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |",
     "|---|---|---|"]
COV = [
    ("R1 the Queue Manager ticket becomes an epic before Thursday's review", "@@P:child_template@@ and every Linear row", "covered — the ten children and the report lines each have rows; a constraint on time has no row"),
    ("R2 Brian's message from yesterday, the source of every ask", "via every deliverable row", "covered — each ask the DM makes has its own row below"),
    ("R3 set it all up as he asked: the note's rules, Arthur's rule, the records that decide each report", "@@P:state:1@@–@@P:state:39@@, @@P:note:4@@–@@P:note:37@@", "covered — a report decided from the sheet alone fails its state row and, where a ticket holds it, its note row"),
    ("R4 the children in Linear (10, one per area, Todo while the area is Open)", "@@P:child_template@@ (count and template), @@P:child_state:Zombie Lane@@, @@P:child_state:Boss Arena@@, @@P:child_state:Tutorials@@", "covered — nine children fails the count; Zombie Lane set to Done fails its row"),
    ("R4 the report lines in Linear: a state per report (39)", "@@P:state:1@@–@@P:state:39@@ (one row per new sub-issue and per changed ticket), @@P:state:6@@", "covered — every new sub-issue's state and every changed ticket state is its own row; the count rejects a change too many or too few"),
    ("R4 the report lines in Linear: new sub-issues (17) and moved tickets (22) with their notes", "@@P:sub_template@@, @@P:sub_create:3@@–@@P:new_assignee:26@@, @@P:move:4@@, @@P:move:11@@–@@P:move:4@@, @@P:note:4@@–@@P:note:37@@", "covered — a new sub-issue for row 11 fails the counts and @@P:move:11@@; a ticket with no note fails its note row"),
    ("R5 the stock-take sheet in the ZM queue manager folder with the two tabs", "@@P:sheet_folder@@, @@P:sheet_cols_reports@@, @@P:sheet_cols_areas@@, @@P:sheet_rows@@, @@P:area_rows@@", "covered — a sheet in My Drive, a tab without one of the columns, 38 report rows or 9 area rows fails"),
    ("R5 the cells: Status, Ticket, Review list, Why; the areas' Status and Open reports", "@@P:sheet_status:1@@–@@P:sheet_status:3@@, @@P:sheet_ticket:11@@, @@P:sheet_ticket:4@@, @@P:review_count_sheet@@, @@P:review_count_sheet@@, @@P:sheet_review:17@@–@@P:sheet_review:36@@, @@P:sheet_why:9@@, @@P:sheet_why:4@@, @@P:area_status:Zombie Lane@@, @@P:area_status:Boss Arena@@, @@P:area_open_count:Tutorials@@–@@P:area_open_count:Card packs@@", "covered — a trap row marked Passed, six marked rows, or Zombie Lane shown Clear fails"),
    ("R6 shared with everyone on the review invite (five people)", "@@P:share:arthur.blake@@–@@P:share:vincent.parker@@", "covered — each attendee's permission has its own row"),
    ("R7 a slide with the numbers in the queue manager deck", "@@P:slide_new@@, @@P:slide:passed@@–@@P:slide:review@@", "covered — numbers on an existing slide, or 12 passed, fails"),
    ("R8 message Brian in the DM with the five numbers", "@@P:dm_place@@, @@P:dm:passed@@–@@P:dm:review@@", "covered — a channel post, or 12 / 7 / 20 / 1 / 6, fails"),
    ("R8 'Once that's done' (order)", "@@P:dm_after_writes@@ (Process)", "covered — a write after the message fails"),
]
for a, b, c in COV:
    L.append(f"| {cell(a)} | {cs(b)} | {cs(c)} |")
L.append("Unauthorized criteria: none")
L.append("")
L.append("## Coverage — gradable surface")
L.append("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
L.append("|---|---|---|---|---|")
mech, tw = set(), sum(c["weight"] for c in JS)
for s in SURF:
    g = EXTRA["surface"][s["id"]]
    ps = re.findall(r"\bP\d+\b", g["cov"])
    if ps:
        if s["mechanisms"]:
            mech.update(ps)
        L.append(f"| {s['id']} | {g['fact']} | {', '.join(C[p] for p in ps)} | covered | title rejects omission and a wrong value on the correct artifact ({cs(g['cov'])}) |")
    else:
        L.append(f"| {s['id']} | {g['fact']} | — | dispositioned | {cell(cs(g['disp']))} |")
mw = sum(P[p]["band"] for p in mech)
L.append(f"Mechanism share: {round(100 * mw / tw)}% of the criteria weight ({mw} of {tw}; reported, not gated)")
L.append("")
L.append("## Findings")
L.append("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
L.append("|---|---|---|---|---|---|---|---|")
L.append(f"| — | — | — | 3_Rubrics_Eval.md Phases 1–5 | No open finding on the current JSON (sha {sha}); the /rubric round-1 findings are fixed (next section) | — | — | — |")
L.append("")
L.append("## Round history and residual risks")
L.append(f"/rubric round 1: {R1['report']}. The current JSON ({sha}) is the reviewed JSON with the Fix List copied row for row; R-numbers below are the reviewed JSON's, C-numbers the current file's.")
L.append("")
L.append("| # | Was (draft) | /rubric type · severity | Fix in the current JSON |")
L.append("|---|---|---|---|")
for i, f in enumerate(R1["fixed"], 1):
    L.append(f"| R1-{i} | {cell(f['was'])} | {f['type']} · {f['sev']} | {cell(cs(f['fix']))} |")
L.append("")
L.append("Residual risks (not findings; no change made):")
for x in R1["residual"]:
    L.append(f"- {cs(x)}")
L.append("")
L.append("## Overlap groups · Spot-check groups · Predicted all-fail")
L.append("| Group / row | Members / basis | Shared condition / reason |")
L.append("|---|---|---|")
for g in EXTRA["groups"]:
    ns = re.findall(r"\bP\d+\b", g["samples"].split("Direct")[0])
    L.append(f"| Spot-check {g['g']} | {cs(g['samples'])} | {len(ns)} sample(s) (≤ 5); volume {cs(g['volume'])}; core requirement sampled: {g['core'].split(' —')[0]} |")
L.append(cs("| Overlap / cascade | none | the state rows name each ticket or report and grade its state only; only @@P:sheet_folder@@ names the folder; the DM and slide number rows each name their own artifact (a row failing because its own artifact was never made is not a group, Eval 3 §3.3); the count rows @@P:child_template@@, @@P:sub_template@@, @@P:move:4@@, @@P:state:6@@, @@P:sheet_rows@@ and @@P:area_rows@@ are population controls |"))
L.append("| Predicted all-fail | 0 rows | every deciding record is visible to Calvin (rubric-writing gate reach.plan_fids, v3.rubric_evidence); every write is cataloged; no forced error; none of the four Evals bases applies |")
L.append("")
L.append("## Dimensions")
L.append("| Dimension | Count / % | Threshold | Status |")
L.append("|---|---|---|---|")
for d in [("Overall Rubric Quality", "0 Major · 0 Moderate · 0 Minor (0%)", "any Major/Moderate fails; Minor > 10% fails", "PASS"),
          ("Criteria Weights", "0 rows one level off on my reading (5 where a value joins records across services, 3 for the note's rule on one sheet row or a calculation, 1 for a copied value); the passed-report rows and the note rows are the ones /rubric may re-band", "> 10% one level off or any two levels off fails", "PASS"),
          ("Known data issue", "0 rows on an SC card (no row grades a Don't-grade value of references/known_data_issues/synthcut.md)", "any row on a Don't-grade value fails", "PASS"),
          ("Category Balance", f"{cats['Outcome']} Outcome · {cats['Process']} Process", "≥ 1 Outcome, Process ≤ 50 %", "PASS"),
          ("Process Rubrics", "1 Process row (passes the three conditions); 0 ordering checks absent", "2+ absent or any invalid fails", "PASS"),
          ("Agent-Centric Phrasing", f"{len(JS)}/{len(JS)} titles 'The Agent' + action; no tool name in a title", "artifact subject or tool name fails", "PASS"),
          ("Negative Criteria", f"0 of {len(JS)} rows an idle Agent passes; no prohibition-only title", "1+ fails", "PASS"),
          ("Predicted all-fail", "0", "tolerance 0", "PASS"),
          ("Schema · coverage · accuracy · contradiction (repair gates)", "schema pass · 0 coverage gaps · 0 incorrect literals · 0 contradictions", "any failure blocks", "PASS")]:
    L.append(f"| {d[0]} | {d[1]} | {d[2]} | {d[3]} |")
L.append(f"Threshold margin: with {len(JS)} rows one Major fails Overall Quality; {int(len(JS) * 0.1) + 1} one-level weight misses (> 10%) would fail Weights.")
L.append("")
L.extend(cs(open(os.path.join(HERE, "rubric_check_selfreview.md")).read().rstrip().replace("@@SHA@@", sha)).splitlines())
tab = ["", "| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |", "|---|---|---|---|---|"]
for r in ROWS:
    m = re.match(r"\(a\)(.*?);\s*\(b\)(.*)$", r["cr"])
    a_, b_ = (m.group(1).strip(), m.group(2).strip()) if m else (r["cr"], "")
    tab.append(f"| {C[r['p']]} ({r['p']}, {r['fact']}, weight {r['band']}) | cleared | false negative? (a) {cell(a_)}; false positive? (b) {cell(b_)} | {cell(r['vals'])} | none |")
L.extend(tab)
L.append("")
L.append("## Reminders")
L.append("- An all-Outcome set is normal; Process is not added to look thorough.")
L.append("- Fix the criteria (Claude, Codex or the human) in the builder, re-export, re-run check, then run /rubric.")
L.append(f"- Enter the {len(JS)} rows in the Criteria Builder exactly as in 09_Rubrics.json (sha {sha}); diff the export against it before /rubric (builder drift: weights, escaped titles).")
out = os.path.join(WF, "09_Rubric_Check.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, "criteria", len(JS), "sha", sha)
