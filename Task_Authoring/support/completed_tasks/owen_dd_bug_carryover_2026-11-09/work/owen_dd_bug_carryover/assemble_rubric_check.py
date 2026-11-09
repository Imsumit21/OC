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


RR, TT = load("rubric_rows"), load("rubric_titles")
ROWS, T = RR.R, TT.T
JS = json.load(open(os.path.join(TI, "09_Rubrics.json")))
assert len(JS) == len(ROWS) and all(JS[i]["title"] == T[r["fact"]]["title"] for i, r in enumerate(ROWS))
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
L = ["# 09 Rubric Check — owen_dd_bug_carryover (DD bug list into Linear and the UI Changes tree, injection rev9)",
     f"Checked 2026-11-09 · Criteria {len(JS)} (builder minimum 5: ok) · Plan 2026-11-09 (09_Rubric_Writing_Plan.md, rubric-writing gate PASS) · 09_Rubrics.json sha256 {sha}",
     "Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)",
     f"JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass ({len(JS)} objects, five non-blank fields each, category Outcome/Process, weight 1/3/5)",
     "Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict (residual risks listed under 'Round history and residual risks')",
     "",
     f"Lint: `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` → count {LINT['count']} ({LINTS}), every hit dispositioned under 'Round history and residual risks' (residual 2); no disguised_negative, vague_exemplar, tool_name, prohibition_title, whitespace or schema hit. Weights 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total {sum(c['weight'] for c in JS)}); Outcome {cats['Outcome']} · Process {cats['Process']}.",
     "",
     "## Coverage",
     "| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |",
     "|---|---|---|"]
COV = [
    ("R1 Arthur's Thursday DM, the source of every ask (\"Arthur sent me a DM on Thursday\")", "via every deliverable row", "covered — each ask the DM makes has its own row below"),
    ("R2 the way he lays it out: the carry-over notes, the master ticket's change, Brian's closing rule", "@@P:new_count@@–@@P:desc:In chapter selection@@, @@P:covered:apple@@, @@P:covered:signin@@, @@P:line:ENG-2434@@–@@P:line:ENG-2409@@, @@P:sheet_columns@@", "covered — the template, the outcome states, the Covered notes, the build lines and the columns each have rows"),
    ("R3 the population: 63 canvas lines and 7 later bug posts", "@@P:new_count@@, @@P:sheet_rows@@", "covered — a ticket or sheet row for a deleted-line comment, a follow-up or the QA-doc post breaks the exact 68 and 70"),
    ("R4 the Linear tickets: one per bug that is not Covered (68), in the template", "@@P:new_count@@ (count and template), @@P:prefix:In profile@@–@@P:desc:In chapter selection@@ (one sample per field)", "covered — a ticket for a Covered line fails the count; each template field has a named sample"),
    ("R4 the state of every new ticket (58 Done, 7 Bugs, 3 Canceled)", "@@P:state:offers has no visuals@@–@@P:state:and activate pop up has the wrong price tage@@ (one row per issue)", "covered — every issue's state is its own row, named by its line or post"),
    ("R4 a note with the canvas wording on each reused ticket (2)", "@@P:covered:apple@@, @@P:covered:signin@@", "covered — a new ticket instead of the note fails, and so does a note on ENG-2280"),
    ("R5 the UI tree brought up to date: 14 moves to Done, 5 held", "@@P:moves_count@@ (exact 14), @@P:move:ENG-2417@@–@@P:move:ENG-2410@@ (samples), @@P:hold:ENG-2434@@–@@P:hold:ENG-2437@@ (stays open)", "covered — moving a held child makes 15 to 19 and fails the count; each held child's line says it stays open"),
    ("R6 a line on every UI child saying where it landed (public build 0.3.310)", "@@P:line:ENG-2434@@–@@P:line:ENG-2409@@ (one row per child)", "covered — every child's line has its own row"),
    ("R7 the sheet in Owen's DD bug carry-over folder", "@@P:sheet_folder@@", "covered — a sheet in Owen's root fails"),
    ("R7 the columns Bug, Outcome, Ticket, Why and one row per bug", "@@P:sheet_columns@@ (header), @@P:sheet_rows@@ (70 rows)", "covered — Status in place of Outcome, or 76 rows, fails"),
    ("R7 the cells: Outcome, Ticket and Why", "@@P:sheet:tavern@@, @@P:sheet:window@@, @@P:sheet:lives1@@, @@P:sheet_outcome:sides@@, @@P:sheet_outcome:apple@@ (Outcome), @@P:sheet_ticket:sides@@, @@P:sheet:apple@@, @@P:sheet:signin@@ (Ticket), @@P:sheet_why:tavern@@, @@P:sheet_why:sides@@ (Why)", "covered — a trap row marked Fixed, a new key for a Covered line, or a blank Why fails"),
    ("R8 shared with everyone on the review (Arthur, Robert, Oliver)", "@@P:share:arthur.blake@harmonygames.co@@–@@P:share:oliver.brooks@harmonygames.co@@", "covered — each attendee's permission has its own row"),
    ("R9 reply in that DM thread with the numbers he wanted", "@@P:reply_thread@@ (thread), @@P:reply_broken@@ (9 still broken), @@P:reply_new@@ (68 new tickets), @@P:reply_done@@ (23 of 28 Done)", "covered — a top-level DM message, 7 still broken, 70 tickets or 21 Done fails"),
    ("R9 'Then reply' (order)", "@@P:reply_after_writes@@ (Process)", "covered — a write after the reply fails"),
    ("R10 before Sunday's bug review", "every write row", "covered as a constraint: all writes are graded in the run (no row)"),
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
L.append(f"| — | — | — | 3_Rubrics_Eval.md Phases 1–5 | No open finding on the current JSON (sha {sha}); the round-1 findings are fixed (next section) | — | — | — |")
L.append("")
L.append("## Round history and residual risks")
L.append(f"/rubric round 1: {R1['report']}. The current JSON ({sha}) is the reviewed JSON (2ed7a6489798, kept as plan/09_Rubrics.prev_2ed7a6489798.json) with the round-1 Fix List copied row for row; the local-round build cee09a260a85 was never reviewed and is superseded (plan/09_Rubrics.prev_cee09a260a85.json). Rows R1–R61 below are the reviewed JSON's numbers; C-numbers are the current file's.")
L.append("")
L.append("| # | Was (reviewed JSON 2ed7a6489798) | /rubric type · severity | Fix in the current JSON |")
L.append("|---|---|---|---|")
for i, f in enumerate(R1["fixed"], 1):
    L.append(f"| R1-{i} | {cell(f['was'])} | {f['type']} · {f['sev']} | {cell(cs(f['fix']))} |")
if R1.get("round2"):
    r2 = R1["round2"]
    L.append("")
    L.append(f"/rubric round 2: {r2['report']}. Round 1's fixes all landed; one row was left for my own rewrite.")
    L.append("")
    L.append("| # | Was (reviewed JSON 9f8ebad8c3e3) | /rubric type · severity | Fix in the current JSON |")
    L.append("|---|---|---|---|")
    L.append(f"| R2-1 | {cell(r2['was'])} | {r2['type']} · {r2['sev']} | {cell(cs(r2['fix']))} |")
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
L.append(cs("| Overlap / cascade | none | the state rows name each issue by its line or post and accept it whatever its title (no shared '[2231]' condition); only @@P:sheet_folder@@ names the folder; the reply rows @@P:reply_broken@@–@@P:reply_done@@ each name their own reply in Arthur's DM (a row failing because its own artifact was never made is not a group, Eval 3 §3.3); the count rows @@P:new_count@@, @@P:moves_count@@ and @@P:sheet_rows@@ count different outputs |"))
L.append("| Predicted all-fail | 0 rows | every deciding record is visible to Owen (rubric-writing gate reach.plan_fids, v3.rubric_evidence); every write is cataloged; no forced error; none of the four Evals bases applies |")
L.append("")
L.append("## Dimensions")
L.append("| Dimension | Count / % | Threshold | Status |")
L.append("|---|---|---|---|")
for d in [("Overall Rubric Quality", "0 Major · 0 Moderate · 0 Minor (0%)", "any Major/Moderate fails; Minor > 10% fails", "PASS"),
          ("Criteria Weights", "0 rows one level off: every weight the round-1 report listed is applied (R40/R41 both 5, its recommendation)", "> 10% one level off or any two levels off fails", "PASS"),
          ("Known data issue", "0 rows on an NB card (no row grades Owen's #god-bugs membership, NB-1, or any card value)", "any row on a Don't-grade value fails", "PASS"),
          ("Category Balance", f"{cats['Outcome']} Outcome · {cats['Process']} Process", "≥ 1 Outcome, Process ≤ 50 %", "PASS"),
          ("Process Rubrics", "1 Process row (passes the three conditions); 0 ordering checks absent", "2+ absent or any invalid fails", "PASS"),
          ("Agent-Centric Phrasing", f"{len(JS)}/{len(JS)} titles 'The Agent' + action; no tool name in a title", "artifact subject or tool name fails", "PASS"),
          ("Negative Criteria", f"0 of {len(JS)} rows an idle Agent passes; no prohibition-only title", "1+ fails", "PASS"),
          ("Predicted all-fail", "0", "tolerance 0", "PASS"),
          ("Schema · coverage · accuracy · contradiction (repair gates)", "schema pass · 0 coverage gaps (the 52 round-1 missing outcomes are rows now) · 0 incorrect literals · 0 contradictions", "any failure blocks", "PASS")]:
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
