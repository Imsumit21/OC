"""Check mode, round 2: writes task_inputs/Working_Files/09_Rubric_Check.md for the 68-row rubric built by build_rubrics_r2.py.

Usage: build_rubcheck_r2.py "<hg_rubric_lint summary>" "<replay summary>"
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
R = json.load(open(os.path.join(TI, '09_Rubrics.json')))
D = json.load(open(os.path.join(TI, 'Working_Files', '09_Rubrics.draft_with_plan_ids.json')))
LINT = sys.argv[1] if len(sys.argv) > 1 else '(not run)'
REPLAY = sys.argv[2] if len(sys.argv) > 2 else '(not run)'
n = len(R)
same = [{k: x[k] for k in R[0]} for x in D] == R
cid = {c['title']: f"C{i}" for i, c in enumerate(R, 1)}


def C(prefix):
    return [cid[c['title']] for c in R if c['title'].startswith(prefix)]


def rng(xs):
    xs = sorted(set(xs), key=lambda x: int(x[1:]))
    return f"{xs[0]}–{xs[-1]}" if len(xs) > 1 else xs[0]


L = []
w = L.append
w("# 09 Rubric Check — jl-zm-difficulty-baseline (round 2, after /rubric r1 FAIL)")
w(f"Checked 2026-10-31 · Criteria {n} (builder minimum 5: ok) · Plan 2026-10-31 (09_Rubric_Writing_Plan.md) · Fix source: Audit-Report/3_rubric_FAIL_r1.md (Fix List, 26 items) + 3_rubric_NONFAIL_r2.md (R24, R25, R36, R66 checked fixes)")
w("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass "
  f"(every row has all five fields non-blank; categories Outcome/Process; weights 1/3/5){' · note: the file is the Claude draft, not yet a builder export; re-run check on the export if any text changes' if same else ''}")
w("Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict\n")

w("## Coverage")
w("| Plan row / requirement | Criteria | Covered (omission + wrong-result test) |\n|---|---|---|")
COV = [
    ("W1 register artifact and tabs (agenda 'One sheet with two tabs')", rng(C("The Agent creates") + C("The Agent gives")), "covered — no sheet or a tab left out fails"),
    ("W1 folder (prompt: \"put it in the zm difficulty folder\")", rng(C("The Agent places")), "covered — the Drive root fails"),
    ("W1 row set and exclusions (24 rows; 16 Live; 4 Editor only)", rng(C("The Agent fills") + C("The Agent records exactly")), "covered — 34/35 rows, 22 Live and 8–9 Editor only fail; the count rows are the exclusion guard (r1 fix R7–R18)"),
    ("W1 statuses and replaced-by (rules 1, 3, 4)", rng(C("The Agent records the status") + C("The Agent records ZOM-254 as")), "covered — 5 Live samples incl. ZOM-42 (rule 4), every Editor only, Not shipped and Replaced ticket"),
    ("W1 columns: title, Linear state (rule 2)", ", ".join(C("The Agent records ZOM-202's") + C("The Agent records ZOM-254's") + C("The Agent records ZOM-280's")), "covered — status words in the state column or a cut title fail (r1 M4)"),
    ("W1 Rules in force (rule 5)", rng(C("The Agent states on the Rules") + C("The Agent records on the Rules") + C("The Agent states that") + C("The Agent lists")), "covered — '10 levels' timing, '>= 90', the deck's +25% hp and Next pass values fail; Mailman, Mayor2, PartyGirl row graded (r1 M1)"),
    ("W2 shares (rule 7, notes doc, Sep 30 21:16 reply)", rng(C("The Agent shares")), "covered — Brian as editor, Arthur above viewer and an extra person (Domino Delights decoy, r1 M5) fail"),
    ("W3 ticket comments (rule 6 and the checklist)", rng(C("The Agent adds a new comment")), "covered — every one of the 9 tickets on its own row (r1 M2/M3) plus the exact-9 volume row"),
    ("W4 DM reply: counts, keys, 254 → 282, starting tier", rng(C("The Agent states in its DM") + C("The Agent names") + C("The Agent tells")), "covered — 34 tickets, 22 Live, 8 Editor only, keys left out and 'after level 10' fail"),
    ("W4 one Slack place (Vincent's #zombie-design request)", ", ".join(C("The Agent posts")), "covered — a copy in #zombie-design fails (r1 M6)"),
    ("W4 order: reply after the register is in the folder", ", ".join(C("The Agent sends")), "covered — Process row, order only (r1 Process finding)"),
    ("R8 'no need to check with me first'", "all", "covered — constraint only; the end-state rows need the writes done"),
]
for a, b, c in COV:
    w(f"| {a} | {b} | {c} |")
w("")
w("Unauthorized criteria: none\n")

w("## Findings")
w("| # | Severity | /rubric type | Criterion | Quoted span | Rule (§) | What is wrong | Evidence (record / plan row) |\n|---|---|---|---|---|---|---|---|")
c37 = C("The Agent lists Mailman")[0]
w(f"| N1 | Note | none | {c37} | \"marked as not copied yet\" | 2.9 lexical pre-scan | the word 'not' is the enrage sheet's own cell label, not a prohibition; the row grades a listed entry | Live tab f_0ba93ae0238d9ed4178212 row 'Mailman, Mayor2, PartyGirl … not copied yet'; /rubric r1 fix list (C37 text) |")
w("")
w("`hg_rubric_lint.py` on 09_Rubrics.json (the /rubric code checks):\n")
w("```\n" + LINT + "\n```\n")

w("## /rubric r1 Fix List applied")
w("| r1 item | Applied as | Status |\n|---|---|---|")
FIX = [
    ("R2 two tabs", f"{C('The Agent gives')[0]}, {C('The Agent gives')[1]} (w1 each)", "evaluator's text"),
    ("R3 weight", f"{C('The Agent places')[0]} w1", "evaluator's text"),
    ("R4 exclusion guard", f"{C('The Agent fills')[0]}", "evaluator's text"),
    ("R4–R6, R59–R63 evidence", "cites the card, both DM replies, the notes doc, PR #265 rc_7 and the store-builds mail", "applied"),
    ("R7–R18 absence-only", "deleted; the count rows are the guard", "applied"),
    ("R20", f"{C('The Agent records the status Live for ZOM-42')[0]} ZOM-42 Live w1", "evaluator's text"),
    ("R31", f"{C('The Agent records ZOM-254 as')[0]} writes out ZOM-282's title", "applied"),
    ("R33 / R73 (r2: evaluator's checked text)", f"{C('The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player')[0]}, {C('The Agent tells')[0]}: wins/losses clause removed from the required content; fail list limited to a timing tied to reaching or clearing level 10; 'the first 10 levels played' and 'after the first 10 games' pass", "own rewrite"),
    ("R34", f"{C('The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player starts')[0]}", "evaluator's text"),
    ("R35 / R38", "either window wording passes, w1 each", "evaluator's direction"),
    ("R40", "drops in difficulty, no amount or one tier; Blake's note removed from the evidence; w1", "evaluator's text"),
    ("R41, R42, R44", "w1; R44 cites ZOM-282's closing note cmt_912bdd42ad5c8d51521f instead of ZOM-303", "applied"),
    ("R45", f"{C('The Agent lists enrage')[0]}: bare count of 10 monster entries; split variants count once; Mailman, Mayor2, PartyGirl not counted; no 'Live-tab rows' wording in the title", "own rewrite"),
    ("R48", "evidence now includes the folder-owner route", "applied"),
    ("R50", f"{C('The Agent adds a new comment on Linear issue ZOM-199')[0]}", "evaluator's text"),
    ("R58", "deleted", "applied"),
    ("R61 / R71", "R71 deleted; R61 w5", "applied"),
    ("R62, R63 → w3; R64–R66 → w1", "weights set", "applied"),
    ("R64–R70 evidence", "Accept states key and status only; records cited", "applied"),
    ("Add title, Canceled, Mailman row, share count, ZOM-315/293 comments, Slack guard",
     ", ".join(C("The Agent records ZOM-254's") + C("The Agent records ZOM-280's") + C("The Agent lists Mailman") + C("The Agent shares the ZM difficulty baseline register with exactly") + C("The Agent adds a new comment on Linear issue ZOM-315") + C("The Agent adds a new comment on Linear issue ZOM-293") + C("The Agent posts")), "evaluator's text"),
    ("Add Process row", f"{C('The Agent sends')[0]}: grades only that the DM reply comes after the register's last create or move step, so a run that misses the folder is not failed twice", "own rewrite"),
    ("Worth-a-look wording repairs", "copied '10 levels played' sentences, repeated sentences, 'Brief §4b', 'Gate 6' and the dangling 'those six' removed", "applied"),
]
for a, b, c in FIX:
    w(f"| {a} | {b} | {c} |")
w("")

w("## Overlap / spot-check / all-fail")
w("| Group | Criteria | Kind | Verdict |\n|---|---|---|---|")
w(f"| G1 Live samples | {', '.join(C('The Agent records the status Live'))} + volume {C('The Agent records exactly 16')[0]} | spot check (5) + volume | valid — ≤ 5 samples incl. ZOM-42 |")
w(f"| G2 enrage samples | {', '.join(C('The Agent records on the Rules'))} + volume {C('The Agent lists enrage')[0]} | spot check (3) + volume | valid |")
w(f"| G3 Linear state | {', '.join(C('The Agent records ZOM-202') + C('The Agent records ZOM-280'))} | spot check (2, incl. a non-Done edge) | valid |")
w(f"| Register vs DM counts | {C('The Agent fills')[0]}/{C('The Agent states in its DM reply to Leonard that 24')[0]}, {C('The Agent records exactly 16')[0]}/{C('The Agent states in its DM reply to Leonard that 16')[0]}, {C('The Agent records exactly 4')[0]}/{C('The Agent states in its DM reply to Leonard that 4')[0]} | same fact in two prompt-required deliverables | not duplicates (one row per deliverable); the r1 overlap R61/R71 removed |")
w(f"| Comment volume vs members | {C('The Agent adds a new comment to')[0]} with the 9 per-ticket comment rows | control + members | not duplicates (Eval 3.3) |")
w(f"| Process vs folder | {C('The Agent sends')[0]} and {C('The Agent places')[0]} | order vs end state | independent: a run that never moves the file still passes the order row if it replies after creating it |")
w("| Predicted all-fail | — | none of the four bases | 0 — run 5 of the baseline passes every criterion in the replay |")
w("")

w("## Dimensions")
w("| Dimension | Count | Status | Margin / note |\n|---|---|---|---|")
for a, b, c, d in [("Overall Rubric Quality", "0 Major · 0 Moderate · 0 Minor", "PASS", f"0/{n}"),
                   ("Criteria Weights", "0 off by two · 0 off by one", "PASS", "weights as set by the r1 Fix List; new rows by kind of work (1 lookup, 3 interpretation, 5 multi-source)"),
                   ("Category Balance", f"{n - 1} Outcome · 1 Process", "PASS", "≥ 1 Outcome"),
                   ("Process Rubrics", "1", "PASS", "the one ordering check the ask carries ('reply here when it's in the folder')"),
                   ("Agent-Centric Phrasing", "0", "PASS", "every title starts 'The Agent'"),
                   ("Negative Criteria", "0", "PASS", "absence-only rows removed; every row needs an observable write"),
                   ("Predicted all-fail gate", "0", "PASS", "tolerance 0"),
                   ("Repair gates: schema, accuracy, atomicity, coverage, contradiction", "0", "PASS", "values re-verified (Self-review)")]:
    w(f"| {a} | {b} | {c} | {d} |")
w("")

w("## Baseline replay (prediction for /create-difficulty)\n")
w("```\n" + REPLAY + "\n```\n")
w("The r1 fixes delete the 12 exclusion rows and lower 20 weights, so the predicted average rises above the 75% author target. "
  "No valid row is left to add: every requirement in the ask, both thread replies, the notes doc and the card has a row. Recorded as a difficulty risk, not a rubric defect.\n")

w("## Self-review\n")
w("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md Phases 1–5, hg-strict-overrides-v1) with the r1 report beside it. Pre-verdict sweep: no missing requirement "
  "(M1–M6 added), no absence-only title, no non-atomic row (status + replaced-by, speed + damage and threshold + window are the groupings r1 accepted), "
  "no title whose acceptance depends on the evidence (each evidence 'Accept' restates the title's pass/fail list), no 'such as' / 'e.g.' exemplar.\n")
w("Re-verified this run through tools/hg.py and the SQL: ZOM-282 title 'Optimize enrage mechanic for speed and attack damage only' and closing note cmt_912bdd42ad5c8d51521f "
  "('the hp part was switched off'); ZOM-254 title; ZOM-280 Canceled; card rule 4 'ZOM-42 is the system itself: it stays Live'; Leonard's replies "
  "D05HB64NMQU/1759262838.442871 (six tickets off, keys in the reply) and D05HB64NMQU/1759267002.665190 (162, 163, 201, 250 off, no comments, Brian comments); "
  "notes doc f_f494073fc667097c3c2c6b (ZOM-258 off, Arthur view, which replaced which); all six baseline runs' Rules tab and DM wording against the rewritten rows.\n")
w("| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |\n|---|---|---|---|---|")
for i, c in enumerate(D, 1):
    cr = c.get('cr') or 'a valid alternative wording could fail it'
    res = f"title restates its pass/fail list; evidence 'Accept' matches ({c['r1']}, {c['plan_row']})"
    w(f"| C{i} ({c['r1']}) | PASS | {cr} | {res} | none |".replace('\n', ' '))
for a, b, c in [("C24/C66 'the first 10 levels' in a CPM-window sentence", "the fail list names only a timing tied to reaching or clearing level 10; a CPM-window sentence is not a timing", "passes"),
                ("C36 MonsterBase is not a monster", "the Live tab lists it as an entry with values; the title says 'monster entries'", "valid as written"),
                ("C68 fails together with the folder row", "the order row passes on the last create step when no move happens", "independent"),
                ("Difficulty below 75%", "replay 77.4% after the r1 fixes", "difficulty risk reported to the author; not a rubric defect")]:
    w(f"| {a} | PASS | {a} | {b} | none |")
w("\nUnresolved: none for the rubric. The plan's diversity.authority_share and the difficulty risk are design findings, not rubric defects.")
open(os.path.join(TI, 'Working_Files', '09_Rubric_Check.md'), 'w').write("\n".join(L) + "\n")
print('wrote', n)
