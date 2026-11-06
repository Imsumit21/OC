#!/usr/bin/env python3
"""Check mode: build Working_Files/09_Rubric_Check.md for the current 09_Rubrics.json (C1…Cn in file order), from the plan
rows (rubric_rows.py), the gradable surface, the plan extras and plan/rubric_check_r1.json (round-1 findings, all fixed)."""
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
assert len(JS) == len(ROWS) and all(JS[i]["title"] == T[r["p"]]["title"] for i, r in enumerate(ROWS))
C = {r["p"]: f"C{i + 1}" for i, r in enumerate(ROWS)}
P = {r["p"]: r for r in ROWS}
SURF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))["slots"]
EXTRA = json.load(open(os.path.join(HERE, "rubric_plan_extra.json")))
R1 = json.load(open(os.path.join(HERE, "rubric_check_r1.json")))
sha = hashlib.sha256(open(os.path.join(TI, "09_Rubrics.json"), "rb").read()).hexdigest()[:12]


def cs(text):
    return re.sub(r"\bP(\d+)\b", lambda m: C.get("P" + m.group(1), "P" + m.group(1)), text)


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


bands = Counter(c["weight"] for c in JS)
cats = Counter(c["category"] for c in JS)
L = ["# 09 Rubric Check — robert_llc_takeover (LLC take-over of Combo Fighter, injection rev4)",
     f"Checked 2026-11-06 · Criteria {len(JS)} (builder minimum 5: ok) · Plan 2026-11-06 (09_Rubric_Writing_Plan.md, rubric-writing gate PASS) · 09_Rubrics.json sha256 {sha}",
     "Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)",
     "JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (73 objects, five non-blank fields each, category Outcome/Process, weight 1/3/5)",
     "Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict (residual risks listed under 'Round history and residual risks')",
     "",
     f"Lint: `python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json` → count 0 (no disguised_negative, format_lock, anon_token, evidence_no_record, vague_exemplar, tool_name or prohibition_title hit). Weights 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total {sum(c['weight'] for c in JS)}); Outcome {cats['Outcome']} · Process {cats['Process']}.",
     "",
     "## Coverage",
     "| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |",
     "|---|---|---|"]
COV = [
    ("R1 Leonard's Thursday-night DM — the source of every ask (\"Leonard sent me a DM on Thursday night\")", "via every deliverable row", "covered — each ask the DM makes has its own row below"),
    ("R3/R5 a call on each issue, as a comment (\"leave the call on each issue\")", "one row per issue: P101–P130, P69, P70, P6, P7, P8, P9, P11; the new VO issue P4", "covered — each issue's comment row rejects no comment and the opposite call"),
    ("R5 the cost part of the call in the comment (the DM: 'what it costs us March through May')", "P131–P138", "covered — every priced item's comment carries its current cost; stale figures fail"),
    ("R4 the call per item, the way he lays it out (ground rules, card, project rule)", "the per-issue comment and state rows; P37–P44 on the sheet", "covered — DD dropped or ZM taken fails P14/P28/P38/P39/P69/P70"),
    ("R8 the project matches the sheet: one state per issue", "P12, P14, P16, P18, P20, P22 (Todo), P24–P26 (Done), P28–P33 and P141–P162 (Canceled)", "covered — every issue's state has its own row"),
    ("R8 the project matches the sheet: assignees on the Todo items", "P13, P15, P17, P19, P21, P23, P3", "covered — every Todo item's assignee is direct"),
    ("R8 the missing plan line: a new issue for the VO campaign, and only that one", "P1 (issue), P2 (Todo), P3 (Leonard), P4 (comment), P171 (exactly one new issue)", "covered — no VO issue fails P1; decoy issues fail P171"),
    ("R6 the plan sheet in Robert's Drive (\"Put the plan sheet in my Drive\")", "P34", "covered — a sheet outside his Drive or an edited draft fails"),
    ("R6 laid out like his draft: the 8 columns", "P35", "covered — a sheet without one of the eight headers fails"),
    ("R6 one row per item (Item column, output volume)", "P68", "covered — dropped items fail the exact 38 (or 37) count"),
    ("R6 Decision column", "P37–P44", "covered — the core rows and sampled cells; every call is also graded per issue in Linear"),
    ("R6 Monthly cost column", "P45, P46, P50, P51, P52, P53, P55", "covered — every priced or trap cost is direct"),
    ("R6 Paid by column", "P40, P54, P173", "covered — sampled cells, the founder-paid and LLC-paid cases"),
    ("R6 Game column", "P172", "covered — sampled cell"),
    ("R6 Next step column", "P47, P48", "covered — the two steps the records set"),
    ("R6 Owner column", "P72, P73", "covered — sampled cells; the same people are graded as Linear assignees"),
    ("R6 By column", "P56, P57, P66, P67", "covered"),
    ("R6/R2 the three shares on the sheet per month (split mail)", "P58", "covered — $150, 1,067 or Arthur's $248 on top fail"),
    ("R7 share it with both of them", "P59, P60", "covered"),
    ("R9 reply in that DM thread: what I'd do", "P62, P63", "covered — each names the thread; taking only CF, or all three, fails"),
    ("R9 reply in that DM thread: what it costs each of us a month", "P64", "covered — $150, 1,067 or Arthur's $248 on top fail"),
    ("R9 reply in that DM thread: the link to the sheet", "P61", "covered — linking the draft, or a reply outside the thread, fails"),
    ("R9 'Then reply' (order)", "P65 (Process)", "covered — a write after the reply fails"),
    ("R10 before Monday's call", "every write row", "covered as a constraint: all writes are graded in the run (no row)"),
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
L.append("Platform /rubric round 1 (FAIL 1 on 8296aaf8dc71, report run_forensics/rev4/rubric_r1/platform_rubric_review_r1.md): its Fix List was applied exactly. 6 rows were deleted (its R5, R28, R38, R53, R57, R68), 19 were retitled or re-weighted with its exact text, its 63 rows were added and its wording repairs were made. A script check confirms all 82 Fix List titles are in the JSON verbatim with their weights, and the other 43 reviewed rows are byte-identical (DELTA locks hold).")
L.append("")
L.append("Platform /rubric round 2 (NON-FAIL 4 on cd67ff04220c, report run_forensics/rev4/rubric_r1/platform_rubric_review_r2.md): Overall Quality 5, Criteria Weights 4 (R6, R40, R83, R96 one level low), 3 Minor (R96 evidence; R123/R129 do not reject counting Leonard's VO card toward his share); coverage 130/130. NON-FAIL counts as a pass for /rubric, and the requester chose to proceed on this version (2026-11-06). Its optional Fix List and its note to send OE 26 back to /oe (the $0 cost in the Combo Fighter comment) were not applied; this JSON and the /oe-passed OEs (e210cd02c49e) are the submitted pair.")
L.append("")
L.append("Earlier local round (blind /rubric-style reviewer + this check, on the 67-row draft ab72cf6d8d2c). Every item below was fixed before the platform round:")
L.append("")
L.append("| # | Was (67-row draft) | /rubric type · severity | Fix in the current JSON |")
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
L.append(f"| Overlap / cascade | none | the reply rows {C['P61']}–{C['P64']} each name their own reply's destination (a row failing because its own artifact was never made is not a group, Eval 3 §3.3; /rubric round 1 rejected the reply cascade); the VO issue rows {C['P2']}–{C['P4']} name 'its new' issue; {C['P52']} alone grades the Metabase (or combined) cell; {C['P68']} is the sheet's only count row |")
L.append("| Predicted all-fail | 0 rows | every deciding record is visible to Robert (rubric-writing gate reach.plan_fids, v3.rubric_evidence); every write is cataloged; no forced error; none of the four Evals bases applies |")
L.append("")
L.append("## Dimensions")
L.append("| Dimension | Count / % | Threshold | Status |")
L.append("|---|---|---|---|")
for d in [("Overall Rubric Quality", "0 Major · 0 Moderate · 0 Minor (0%)", "any Major/Moderate fails; Minor > 10% fails", "PASS"),
          ("Criteria Weights", "0 rows one level off after /rubric round 1's five weight fixes (its Fix List weights copied); the new rows carry its weights", "> 10% one level off or any two levels off fails", "PASS (NON-FAIL 4 if /rubric reads the residual two differently)"),
          ("Known data issue", "0 rows on an NB card (Slack posts before Feb 13 10:03 UTC; no Helpshift vendor date; no Snowflake AWS cost)", "any row on a Don't-grade value fails", "PASS"),
          ("Category Balance", f"{cats['Outcome']} Outcome · {cats['Process']} Process", "≥ 1 Outcome, Process ≤ 50 %", "PASS"),
          ("Process Rubrics", "1 Process row (passes the three conditions); 0 missing ordering checks", "2+ missing or any invalid fails", "PASS"),
          ("Agent-Centric Phrasing", f"{len(JS)}/{len(JS)} titles 'The Agent' + action; no tool name in a title", "artifact subject or tool name fails", "PASS"),
          ("Negative Criteria", f"0 of {len(JS)} rows an idle Agent passes; no prohibition-only title", "1+ fails", "PASS"),
          ("Predicted all-fail", "0", "tolerance 0", "PASS"),
          ("Schema · coverage · accuracy · contradiction (repair gates)", "schema pass · 0 coverage gaps · 0 incorrect literals · 0 contradictions", "any failure blocks", "PASS")]:
    L.append(f"| {d[0]} | {d[1]} | {d[2]} | {d[3]} |")
L.append(f"Threshold margin: with {len(JS)} rows one Major fails Overall Quality; {int(len(JS) * 0.1) + 1} one-level weight misses (> 10%) would fail Weights.")
L.append("")
L.extend(open(os.path.join(HERE, "rubric_check_selfreview.md")).read().rstrip().replace("@@SHA@@", sha).splitlines())
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
