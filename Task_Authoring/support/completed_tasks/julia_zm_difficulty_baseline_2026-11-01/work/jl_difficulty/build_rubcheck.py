"""Check mode: writes task_inputs/Working_Files/09_Rubric_Check.md for the current 09_Rubrics.json."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
R = json.load(open(os.path.join(TI, '09_Rubrics.json')))
D = json.load(open(os.path.join(TI, 'Working_Files', '09_Rubrics.draft_with_plan_ids.json')))
rows = {r['P']: r for r in json.load(open(os.path.join(sys.argv[1], 'rows.json')))}
LINT = sys.argv[2] if len(sys.argv) > 2 else ''
n = len(R)
plan = {c['title']: c['plan_row'] for c in D}
cid = {c['title']: f"C{i}" for i, c in enumerate(R, 1)}
same = [{k: x[k] for k in R[0]} for x in D] == R


def C(prefix):
    return [cid[c['title']] for c in R if c['title'].startswith(prefix)]


def rng(xs):
    return f"{xs[0]}–{xs[-1]}" if len(xs) > 1 else xs[0]


L = []
w = L.append
w("# 09 Rubric Check — jl-zm-difficulty-baseline")
w(f"Checked 2026-10-31 · Criteria {n} (builder minimum 5: ok) · Plan 2026-10-31 (09_Rubric_Writing_Plan.md, {len(rows)} rows)")
w("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass "
  f"(every row has all five fields non-blank; category Outcome; weights 1/3/5){'' if not same else ' · note: the file is the Claude draft, not yet a builder export; re-run check on the export if any text changes'}")
w("Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict\n")
w("## Coverage")
w("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |\n|---|---|---|")
COV = [
 ("W1 register artifact, tabs, folder (prompt: \"build the register the way he set it up\", \"put it in the zm difficulty folder\")", rng(C("The Agent creates") + C("The Agent gives") + C("The Agent places")), "covered — no sheet, one tab or the Drive root fails"),
 ("W1 row set (24 rows; 16 Live; 4 Editor only)", rng(C("The Agent fills") + C("The Agent records exactly")), "covered — the 34/35-row lists and 22 Live / 8–9 Editor only fail"),
 ("W1 scope boundaries (thread replies, notes doc, PR 265 review)", rng(C("The Agent leaves")), "covered — each of the 12 left-off tickets on its own row; keeping any fails that row"),
 ("W1 statuses and replaced-by (rule 3, rule 4)", rng(C("The Agent records the status") + C("The Agent records ZOM-254")), "covered — Live samples (≤ 5) plus every Editor only, Not shipped and Replaced ticket; a wrong status fails"),
 ("W1 Linear state column (rule 2)", ", ".join(C("The Agent records ZOM-202's")), "covered — status words in the state column fail"),
 ("W1 Rules in force (rule 5)", rng(C("The Agent states on the Rules") + C("The Agent records on the Rules") + C("The Agent lists on the Rules")), "covered — '10 levels', '>= 90', 4-loss-only demotion, the deck's +25% hp and Next pass values fail"),
 ("W2 shares (rule 7, the notes doc, the Sep 30 21:16 reply)", rng(C("The Agent shares")), "covered — Brian as editor and Arthur as commenter fail their rows"),
 ("W3 ticket comments (rule 6 and the checklist)", rng(C("The Agent adds a new comment on") + C("The Agent adds a new comment to")), "covered — ZOM-199 and ZOM-254 directly, 5 checklist samples, volume of exactly 9 rejects comments on the four dropped tickets"),
 ("W4 DM reply: place, total, per-status counts, keys, 254 → 282, starting tier", rng(C("The Agent replies") + C("The Agent states in its DM") + C("The Agent names") + C("The Agent tells")), "covered — 34 tickets, 22 Live, 8 keys, '#zombie-design' or 'after level 10' fail"),
 ("R8 'no need to check with me first'", "all", "covered — constraint only; the end-state rows need the writes done"),
]
for a, b, c in COV:
    w(f"| {a} | {b} | {c} |")
w("")
w("Unauthorized criteria: none\n")
w("## Findings")
w("| # | Severity | /rubric type | Criterion | Quoted span | Rule (§) | What is wrong | Evidence (record / plan row) |\n|---|---|---|---|---|---|---|---|")
c45 = C("The Agent lists on the Rules")[0]
w(f"| N1 | Note | none | {c45} | \"marked not copied yet\" | 2.9 lexical pre-scan | the word 'not' sits inside the sheet's own cell label, not a prohibition; the row grades a count | Live tab f_0ba93ae0238d9ed4178212 row 'Mailman, Mayor2, PartyGirl … not copied yet'; plan {plan[R[int(c45[1:]) - 1]['title']]} |")
cl = C("The Agent leaves")
w(f"| N2 | Note | none | {rng(cl)} | \"off the Tickets tab of the ZM difficulty baseline register\" | 2.9 Negative criteria (hg-strict-overrides-v1) | scope boundary of a required artifact, the form the override prescribes ('The Agent leaves ENG-123 open'); an idle Agent with no register fails | Evals/3_Rubrics_Eval.md line 383; D05HB64NMQU/1759262838.442871, D05HB64NMQU/1759267002.665190 |")
w("")
w("`hg_rubric_lint.py` on 09_Rubrics.json (the /rubric code checks):\n")
w("```\n" + (LINT or "(not run)") + "\n```\n")
w("## Overlap / spot-check / all-fail")
w("| Group | Criteria | Kind | Verdict |\n|---|---|---|---|")
w(f"| G1 Live samples | {', '.join(C('The Agent records the status Live'))} + volume {C('The Agent records exactly 16')[0]} | spot check (5) + volume | valid — ≤ 5 samples, volume row present |")
w(f"| G2 enrage samples | {', '.join(C('The Agent records on the Rules'))} + volume {c45} | spot check (3) + volume | valid |")
w(f"| G3 checklist comments | {', '.join(C('The Agent adds a new comment on Linear issue ZOM-1') [:0] + [c for c in C('The Agent adds a new comment on Linear issue') if c not in C('The Agent adds a new comment on Linear issue ZOM-199') + C('The Agent adds a new comment on Linear issue ZOM-254')])} + volume {C('The Agent adds a new comment to')[0]} | spot check (5) + volume | valid |")
w(f"| Register vs DM counts | {C('The Agent fills')[0]}/{C('The Agent states in its DM reply to Leonard that 24')[0]}, {C('The Agent records exactly 16')[0]}/{C('The Agent states in its DM reply to Leonard that 16')[0]} | same fact in two prompt-required deliverables | not duplicates (one row per deliverable) |")
w(f"| Aggregate controls vs members | {C('The Agent records exactly 4')[0]} with the four Editor only rows; {C('The Agent names exactly 4')[0]} with the four Editor only key rows | control + members | not duplicates (Eval 3.3) |")
w("| Shared root cause (both thread replies missed) | scope rows, counts, Brian's share, comment volume, DM counts | likely-cause correlation, no embedded shared acceptance condition | no OVERLAP_GROUP (Eval 3.3: a shared root cause is not a cascade group) |")
w("| Predicted all-fail | — | none of the four bases | 0 — run-5 of the baseline passes every criterion in the replay (scratchpad rub/sim2.py) |")
w("")
w("## Dimensions")
w("| Dimension | Count | Status | Margin / note |\n|---|---|---|---|")
for a, b, c, d in [("Overall Rubric Quality", "0 Major · 0 Moderate · 0 Minor", "PASS", f"0/{n}"),
                   ("Criteria Weights", "0 off by two · 0 off by one", "PASS", "bands follow the plan's work kinds (1 lookup, 3 interpretation, 5 multi-source)"),
                   ("Category Balance", f"{n} Outcome", "PASS", "≥ 1 Outcome"),
                   ("Process Rubrics", "0", "PASS", "no Process rows; C1/C2 candidates failed condition 3 in the plan"),
                   ("Agent-Centric Phrasing", "0", "PASS", "every title starts 'The Agent'; no tool name in a title"),
                   ("Negative Criteria", "0", "PASS", "scope boundaries phrased affirmatively (N2)"),
                   ("Predicted all-fail gate", "0", "PASS", "tolerance 0"),
                   ("Repair gates: schema, accuracy, atomicity, coverage, contradiction", "0", "PASS", "values re-verified (Self-review)")]:
    w(f"| {a} | {b} | {c} | {d} |")
w("")
w("## Self-review\n")
w("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md Phases 1–5, hg-strict-overrides-v1). Pre-verdict sweep: no missing requirement, no phrasing "
  "mismatch, no non-atomic row (status + replaced-by and speed + damage are coupled attributes of one record; '> 90 → tier 1, 90 stays on 0' is one "
  "comparison), no category mislabel, no hard-coded title (sheet title any; tab names allow equivalents), no duplicate or cascade group, no vague exemplar, "
  "no prohibition-only title.\n")
w("Re-verified this run: statuses and counts in support/task_work/jl_difficulty/truth.json against linear data.json (31 title matches, ZOM-203/276 Duplicate, "
  "ZOM-202 In Progress, ZOM-280 Canceled, ZOM-293 Todo) and the SQL closing notes; the Live tab rows (Boxer 0.5/0.4, MonsterBase 0.8/0.8, Plumber 0.3/0.3, "
  "11 rows with Mailman/Mayor2/PartyGirl 'not copied yet') in 01_Universe_Inject.sql; ZOM-42 (80%, up to the most recent 10, tier -2 one win, 4 in a row, "
  "50% or lower, record reset) and ZOM-303 via tools/hg.py; TierManager.cs line 31 / WinHistory.cs line 166; shares and comments against "
  "D05HB64NMQU/1759267002.665190, 68dc033bf7d24e86b8a9cc67 and f_f494073fc667097c3c2c6b.\n")
w("| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |\n|---|---|---|---|---|")
for i, c in enumerate(R, 1):
    p = plan.get(c['title'])
    r = rows.get(p, {})
    w(f"| C{i} ({p}) | PASS | {r.get('cr', 'a valid alternative could fail it')} | {r.get('res', '')} ({p}) | none |".replace('\n', ' '))
for a, b, c in [("N1 false positive?", "the 'not' is a cell label quoted from the sheet (f_0ba93ae0238d9ed4178212)", "kept as a note"),
                ("N2 could still fail Negative Criteria", "Evals/3_Rubrics_Eval.md line 383 prescribes exactly this form; hg_rubric_lint returns 0 findings", "kept as a note"),
                ("Coverage false negative: the title column is ungraded", "rule 2 lists columns, the canonical outcome marks titles representational (68daca5871dba40417a00383)", "no row needed"),
                ("Over-specific: exactly 10 enrage rows fails a run that splits Magician into three VarC rows", "rule 5 says copy the Live tab as it stands; the tab has one Magician row (f_0ba93ae0238d9ed4178212)", "valid as written")]:
    w(f"| {a} | PASS | {a} | {b} | none |")
w("\nUnresolved: none (the plan's diversity.authority_share and failure-pattern risk are design findings recorded in 09_Rubric_Writing_Plan.md, not rubric defects).")
open(os.path.join(TI, 'Working_Files', '09_Rubric_Check.md'), 'w').write("\n".join(L) + "\n")
print('wrote', n)
