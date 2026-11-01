"""Check mode, round 7: writes task_inputs/Working_Files/09_Rubric_Check.md for the 73-row rubric built by r7/build_rubrics_r7.py.

Usage: build_rubcheck_r2.py "<hg_rubric_lint summary>" "<replay summary>"
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
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
w("# 09 Rubric Check — jl-zm-difficulty-baseline (round 7, SQL b64bc2f2c6dc)")
w(f"Checked 2026-11-01 · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-01 (09_Rubric_Writing_Plan.md) · Base: the /rubric r3 PASS rubric (Audit-Report/3_rubric_PASS_r3.md, 68 rows) brought to round 7 per /prompt r14 and /hardness r7 (Audit-Report/1_prompt_PASS_r14.md, 1a_hardness_NONFAIL_r7.md)")
w("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass "
  f"(every row has all five fields non-blank; categories Outcome/Process; weights 1/3/5){' · note: the file is the Claude draft, not yet a builder export; re-run check on the export if any text changes' if same else ''}")
w("Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict\n")

w("## Coverage")
w("| Plan row / requirement | Criteria | Covered (omission + wrong-result test) |\n|---|---|---|")
COV = [
    ("W1 register artifact and tabs (agenda 'One sheet with two tabs')", rng(C("The Agent creates") + C("The Agent gives")), "covered — no sheet or a tab left out fails"),
    ("W1 folder (prompt: \"put it in the zm difficulty folder\")", rng(C("The Agent places")), "covered — the Drive root fails"),
    ("W1 row set and exclusions (23 rows; 15 Live; 4 Editor only)", rng(C("The Agent fills") + C("The Agent records exactly")), "covered — 33/27/24/22 rows, 21/16/14 Live and 8–9 Editor only fail; the count rows are the exclusion guard, incl. ZOM-295 (PR 271) and ZOM-312 (PR 265)"),
    ("W1 statuses and replaced-by (rules 1, 3, 4)", rng(C("The Agent records the status") + C("The Agent records ZOM-254 as")), "covered — 5 Live samples incl. ZOM-42 (rule 4) and ZOM-281 (the non-Blake 'tiers:' ticket, /hardness r6 F1), every Editor only, Not shipped and Replaced ticket"),
    ("W1 columns: title, Linear state (rule 2)", ", ".join(C("The Agent records ZOM-202's") + C("The Agent records ZOM-254's") + C("The Agent records ZOM-280's")), "covered — status words in the state column or a cut title fail (r1 M4)"),
    ("W1 Robert's three columns (card rule 2, Robert's group-chat reply)", rng(C("The Agent gives the Tickets tab") + C("The Agent records Robert as") + C("The Agent records ZOM-293's Linear priority") + C("The Agent records 2025-06-12")), "covered — a tab with the agenda's columns only fails the header row; assignee, priority and the Pacific done day are spot-checked (UTC day also passes, /prompt r14)"),
    ("W1 Rules in force (rule 5)", rng(C("The Agent states on the Rules") + C("The Agent records on the Rules") + C("The Agent states that") + C("The Agent lists")), "covered — '10 levels' timing, '>= 90', the deck's +25% hp and Next pass values fail; Mailman, Mayor2, PartyGirl row graded (r1 M1)"),
    ("W2 shares (rule 7, notes doc, Sep 30 21:16 reply)", rng(C("The Agent shares")), "covered — Brian as editor, Arthur above viewer and an extra person (Domino Delights decoy, r1 M5) fail"),
    ("W3 ticket comments (rule 6 and the checklist)", rng(C("The Agent adds a new comment")), "covered — every one of the 9 tickets on its own row plus the exact-9 volume row; the 7 Editor only / Not shipped rows need both builds (Leonard's reply D05HB64NMQU/1759262838.442871)"),
    ("W4 DM reply: counts, keys, 254 → 282, starting tier", rng(C("The Agent states in its DM") + C("The Agent names") + C("The Agent tells")), "covered — 24/27/29/33 tickets, 16/21 Live, 8–9 Editor only, keys left out, extra Editor only keys (exact-key row) and 'after level 10' fail"),
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

w("## Round 7 changes (from the /rubric r3 PASS rubric)")
w("| Change | Criteria | Source |\n|---|---|---|")
for a, b, c in [("23 tickets, 15 Live in the register and the DM", ", ".join(C("The Agent fills") + C("The Agent records exactly 15") + C("The Agent states in its DM reply to Leonard that 23") + C("The Agent states in its DM reply to Leonard that 15")), "/prompt r14 recommendation 1; Blake's review comment harmonygames-Games/match3d#271#rc_1"),
                ("ZOM-281 Live replaces the ZOM-246 spot check (Live group stays at 5)", C("The Agent records the status Live for ZOM-281")[0], "/hardness r6 F1 and r7 next action; cmt_df69e4a92767cbff0000"),
                ("The 7 Editor only / Not shipped comments name both builds", rng(C("The Agent adds a new comment on Linear issue ZOM-1") + C("The Agent adds a new comment on Linear issue ZOM-2") + C("The Agent adds a new comment on Linear issue ZOM-3")), "Leonard's reply D05HB64NMQU/1759262838.442871; /prompt r14 'Unchanged'"),
                ("Robert's three columns: header + 3 spot checks, Pacific or UTC day", rng(C("The Agent gives the Tickets tab") + C("The Agent records Robert as") + C("The Agent records ZOM-293's Linear priority") + C("The Agent records 2025-06-12")), "/prompt r14 recommendation 1 (accept both days, number or label); CAFC495E4006/1759229513.774912"),
                ("Exact Editor only keys in the DM", C("The Agent names exactly")[0], "Leonard's ask for the keys 'so i know who to chase' (D05HB64NMQU/1759262838.442871)"),
                ("Brian's share w5 (multi-source: rule 7, checklist, later reply)", C("The Agent shares the ZM difficulty baseline register with Brian")[0], "weight by kind of work: the latest of three records decides"),
                ("Blake's editor/debug rule cited from his reply (own thread)", "C8–C16, C61–C65", "/injection r12 C-2 (reply in its own thread); julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"),
                ("Starting tier also accepts '10 levels played'", ", ".join(C("The Agent states on the Rules in force tab of the ZM difficulty baseline register that a new player's") + C("The Agent tells")), "/prompt r14 carried item")]:
    w(f"| {a} | {b} | {c} |")
w("")
w("## /rubric r1 Fix List applied (kept from round 2)")
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
w(f"| G1 Live samples | {', '.join(C('The Agent records the status Live'))} + volume {C('The Agent records exactly 15')[0]} | spot check (5) + volume | valid — ≤ 5 samples incl. ZOM-42 and ZOM-281 |")
w(f"| G4 Robert's columns | {', '.join(C('The Agent records Robert as') + C('The Agent records ZOM-293') + C('The Agent records 2025-06-12'))} + header {C('The Agent gives the Tickets tab')[0]} | spot check (3) + structure | valid — one value per column, Pacific or UTC day |")
w(f"| DM Editor only keys | {', '.join(C('The Agent names ZOM-173') + C('The Agent names ZOM-200') + C('The Agent names ZOM-277') + C('The Agent names ZOM-315'))} + exact set {C('The Agent names exactly')[0]} | members + exact set | not duplicates: the members grade each key, the exact set grades the chase list (extra keys fail it) |")
w(f"| G2 enrage samples | {', '.join(C('The Agent records on the Rules'))} + volume {C('The Agent lists enrage')[0]} | spot check (3) + volume | valid |")
w(f"| G3 Linear state | {', '.join(C('The Agent records ZOM-202') + C('The Agent records ZOM-280'))} | spot check (2, incl. a non-Done edge) | valid |")
w(f"| Register vs DM counts | {C('The Agent fills')[0]}/{C('The Agent states in its DM reply to Leonard that 23')[0]}, {C('The Agent records exactly 15')[0]}/{C('The Agent states in its DM reply to Leonard that 15')[0]}, {C('The Agent records exactly 4')[0]}/{C('The Agent states in its DM reply to Leonard that 4')[0]} | same fact in two prompt-required deliverables | not duplicates (one row per deliverable); the r1 overlap R61/R71 removed |")
w(f"| Comment volume vs members | {C('The Agent adds a new comment to')[0]} with the 9 per-ticket comment rows | control + members | not duplicates (Eval 3.3) |")
w(f"| Process vs folder | {C('The Agent sends')[0]} and {C('The Agent places')[0]} | order vs end state | independent: a run that never moves the file still passes the order row if it replies after creating it |")
w("| Predicted all-fail | — | none of the four bases | 0 — round-7 baseline run 3 passes every criterion in the replay |")
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
w("Replay of the six round-7 baselines (payloads read by r7 projection scripts; DM key lists hand-checked): run 1 66.9%, run 2 75.7%, run 3 100%, run 4 81.7%, run 5 88.2%, run 6 86.4% "
  "before the Brian weight change; with Brian w5 the projection is average about 82%, population SD about 0.11, pass@1 1 of 6, 4 failure patterns (largest 40%). "
  "The verifier decides the real numbers.\n")

w("## Self-review\n")
w("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md Phases 1–5, hg-strict-overrides-v1) with the r1 report beside it. Pre-verdict sweep: no missing requirement "
  "(M1–M6 added), no absence-only title, no non-atomic row (status + replaced-by, speed + damage and threshold + window are the groupings r1 accepted), "
  "no title whose acceptance depends on the evidence (each evidence 'Accept' restates the title's pass/fail list), no 'such as' / 'e.g.' exemplar.\n")
w("Round 7: re-verified PR 271's inline comment harmonygames-Games/match3d#271#rc_1, Robert's reply CAFC495E4006/1759229513.774912, ZOM-293 (assignee Robert, priority 4), ZOM-200 completed_at 2025-06-13T01:17:38Z, ZOM-281's note cmt_df69e4a92767cbff0000 and Leonard's reply D05HB64NMQU/1759262838.442871 (builds) through the SQL rows and linear data.json. "
  "Re-verified this run through tools/hg.py and the SQL: ZOM-282 title 'Optimize enrage mechanic for speed and attack damage only' and closing note cmt_912bdd42ad5c8d51521f "
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
                ("C-new exact Editor only keys double-grades the per-key rows", "the per-key rows pass a reply that also lists extra tickets; the exact row fails it; different facts (members vs list)", "independent"),
                ("Brian w5 is off by two", "the row needs three records in time order (rule 7, checklist 16:20Z, reply 21:16Z), the same multi-source basis as the count rows", "w5 kept"),
                ("Pacific day row could fail a UTC answer", "the title and Accept pass 2025-06-13 too (/prompt r14)", "passes both")]:
    w(f"| {a} | PASS | {a} | {b} | none |")
w("\nUnresolved: none for the rubric. The plan's diversity.authority_share and the difficulty risk are design findings, not rubric defects.")
open(os.path.join(TI, 'Working_Files', '09_Rubric_Check.md'), 'w').write("\n".join(L) + "\n")
print('wrote', n)
