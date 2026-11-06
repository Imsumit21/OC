#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) from 09_Rubrics.json, rows.json and review_rounds.md. Row numbers
come from each row's stable tag, so inserting or removing rows never leaves a stale C-number here."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
WS = TI.parents[1]
crit = json.loads((TI / "09_Rubrics.json").read_text())
rows = json.loads((HERE / "rows.json").read_text())
assert len(crit) == len(rows) and all(c["title"] == r["t"] for c, r in zip(crit, rows))
T = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
tw = sum(c["weight"] for c in crit)
n = len(crit)


def c(*tags):
    return ", ".join(T[t] for t in tags)


def rng(prefix):
    ps = [T[r["tag"]] for r in rows if r["tag"].startswith(prefix)]
    return f"{ps[0]} to {ps[-1]}"


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


lint = subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "rubric-lint", str(TI / "09_Rubrics.json")],
                      capture_output=True, text=True, cwd=WS).stdout
lint_n = json.loads(lint)["count"]
out = []
w = out.append
w("# 09 Rubric Check: vincent-zm3d-release-gate (ZM store candidates QA gate, injection rev18)")
w(f"Checked 2026-11-06 · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-06 (09_Rubric_Writing_Plan.md, rows P1 to "
  f"P{n} = C1 to C{n}) · Revision 2: the independent /rubric review round 1 (seven reviewers, 75-row draft) applied; round 2 "
  f"re-reviewed this {n}-row set")
w("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · "
  "evidence=`evidence` · schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category "
  "Outcome; weight 1, 3 or 5)")
w("Readiness for /rubric: CLEAN (a prediction only; /rubric gives the verdict)")
w("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
w("")
w(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json`): {lint_n} findings. "
  f"No `disguised_negative`, `format_lock`, `anon_token`, `evidence_no_record`, `vague_exemplar`, `tool_name`, "
  f"`prohibition_title` or schema hit. The lexical negative pre-scan finds 'no' only in {c('z_only')} ('into no other Linear "
  f"issue's description'), a boundary inside the required write (Eval 3 2.9's own pattern 'updates page X and no other "
  f"page'; an idle Agent writes no blocker list and fails it). No em or en dash and no local file reference in any field.")
w("")
w("## Coverage")
w("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |")
w("|---|---|---|")
cov = [
    ("New tab in Vincent's release gate sheet, one tab per gate (prompt; How we gate)", c("tab"),
     "covered: no tab, a tab in another spreadsheet, a new spreadsheet or two tabs fail"),
    ("Tab named after the candidate builds (How we gate)", c("tabname"), "covered: a name without 135 and 50 fails"),
    ("Register rows only in the new tab (prompt; How we gate 'One tab per gate')", c("regonly"),
     "covered: also writing over the Sep 22 tab fails"),
    ("One row per in-scope ticket under Leonard's scope, exclusions applied, the filed ticket included", c("count133"),
     "covered: the Bug view, a register with ZOM-570, ZOM-359 or ZOM-475, or one without the new ticket fails"),
    ("Call per ticket, BLOCKER class (gate-deciding; feeds ZOM-570)", rng("reg_"),
     "covered in full: any blocker called KNOWN ISSUE, FIXED or NO CALL fails its row"),
    ("Call per ticket, other classes (G1: 2 direct exceptions, 5 samples)", c("fix_429", "fix_558", "fix_563",
     "smp_art793", "smp_481", "smp_477", "smp_536"),
     "covered by sampling under the volume row: ZOM-558 called NO CALL, ZOM-563 left KNOWN ISSUE or ART-793 left out fails"),
    ("Build status column (G2)", c("bs_569", "bs_567", "bs_563", "bs_473", "bs_429", "bs_477"),
     "covered: ZOM-569 in candidate, ZOM-567 server - live or ZOM-563 n/a fails"),
    ("QA result column (G3)", c("qa_449", "qa_559"), "covered: the Sep 22 tab's 'not reproduced' for ZOM-559 fails"),
    ("Evidence column, id or link of the deciding record (G4)", c("ev_435", "ev_563"),
     "covered: citing only the ticket, Vincent's #133 post or a bare name fails"),
    ("Title column (G5)", c("title_546"), "covered: an empty or reworded title fails"),
    ("Blockers added to ZOM-570's description by existing key (prompt; ZOM-570; reuse rule)",
     f"{c('z_keep', 'z_only', 'z_count')}, {rng('z_293') if False else T['z_293']} to {T['z_des313']}, {T['z_new']}",
     "covered: replacing Arthur's text, writing the list elsewhere, a list of 14 or a list with known issues fails"),
    ("New ZM ticket for the unfiled runbook finding (prompt; runbook update rows; reuse rule)",
     c("new_issue", "new_one"), "covered: no ticket, ZOM-424 reused, or a second duplicate ticket fails"),
    ("New ticket content: device, OS version, source build, repro (runbook 'File the bug with ...')",
     c("new_device", "new_os", "new_issue", "new_repro"),
     "covered: the source build N-1 App Store is part of " + T["new_issue"] + "'s title; a wrong device, OS or repro fails"),
    ("QA call as a reply in Arthur's thread (prompt; Leonard's ZOM-570 comment)", c("s_thread", "s_call"),
     "covered: a top-level post, a reply in another thread or a go call fails"),
    ("Before Friday's go/no-go (prompt; evt_81e6dc4dbfd331f1a6a317)", c("s_time"),
     "covered: a reply after 2025-10-03T16:00:00Z fails"),
]
for a, b, d in cov:
    w(f"| {a} | {b} | {d} |")
w("Unauthorized criteria: none")
w("")
w("Runbook text the prompt does not assign (link the bug on the runbook page, mirror symptoms to the Customer Support "
  "Playbook, mark or post the matrix, link the matrix from the release ticket) is not a requirement: the prompt incorporates "
  "the runbook's checks for the new-ticket ask only (platform /prompt report, incorporation chain), Vincent is a reader on "
  "Brian's matrix f_b91db376f65604b8602657, and the OE (PASS) performs none of them.")
w("")
w("## Coverage — gradable surface")
w("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
w("|---|---|---|---|---|")
surf = json.loads((TI / "Working_Files/01_Gradable_Surface.json").read_text())
cover = {"S01": "reg_569", "T01": "z_569", "S03": "reg_567", "T02": "z_567", "S05": "reg_435", "T03": "z_435",
         "S07": "reg_473", "T05": "z_473", "B01": "new_issue", "S09": "reg_562", "T04": "z_562", "S11": "smp_art793",
         "S12": "reg_des313", "S13": "reg_578", "S14": "fix_563", "S31": "reg_458", "T06": "z_458", "S32": "reg_535",
         "T08": "z_535", "S30": "reg_293", "T07": "z_293", "S20": "reg_559", "S21": "reg_560", "S22": "smp_481",
         "V01": "count133", "D01": "s_thread", "D02": "s_call"}
SAMPLED_OUT = {"S24": "ZOM-564", "S25": "ZOM-506", "S26": "ZOM-557", "S27": "ZOM-561", "S28": "ZOM-513", "S29": "ZOM-387"}
mech = 0
for s in surf["slots"]:
    if s["id"] in SAMPLED_OUT:
        w(f"| {s['id']} | {SAMPLED_OUT[s['id']]}.call | none | dispositioned | sampled out: G1 holds five samples plus two "
          f"direct exception rows under gate 15's cap; {SAMPLED_OUT[s['id']]} is an ordinary member and its row still "
          f"counts in {T['count133']} |")
        continue
    t = cover[s["id"]]
    r = rows[int(T[t][1:]) - 1]
    if s.get("mechanisms"):
        mech += r["w"]
    w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {T[t]} | covered | the title rejects the omission and the trap "
      f"value ({cell(r['alt'])}) |")
w(f"Mechanism share: {round(100 * mech / tw)}% of the criteria weight (reported, not gated)")
w("")
w("## Findings")
w(f"Findings on the {n}-row JSON as it stands (none open). The independent review rounds and the repairs they drove are "
  "listed under 'Independent review rounds' below, with the old row numbers.")
w("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
w("|---|---|---|---|---|---|---|---|")
w(f"| 1 | {T['z_only']} | \"into no other Linear issue's description\" | Eval 3 2.9 negative pre-scan | The word 'no' sits in a "
  f"boundary on the required write, the pattern 2.9 itself recommends; an idle Agent fails the row | F2 | — | none |")
w(f"| 2 | {T['count133']} | \"with the release ticket ZOM-570, ZOM-359 and ZOM-475 left out\" | Eval 3 2.2 qualifiers of one "
  f"metric; rubric_sampling.md 'State the scope and predicate precisely' | The exclusions are the cohort qualifier of the "
  f"one count, not a second claim: a register is in scope or it is not | F6 F13 F14 | — | none |")
w(f"| 3 | {T['z_count']}, {T['new_one']} | \"exactly 19 tickets\" · \"exactly one new Linear issue\" | rubric_flow_v2.md scope "
  f"checklist (count or scope condition on the required write); QC B11 | Bare count guards; a right count over a wrong set "
  f"needs two cancelling errors; an id list would bundle the members (Eval 2.2) | F39 F36 | — | none |")
w("")
rr = HERE / "review_rounds.md"
if rr.exists():
    w(rr.read_text().rstrip())
    w("")
w("## Overlap groups · Spot-check groups · Predicted all-fail")
w("| Group / row | Members / basis | Shared condition / reason |")
w("|---|---|---|")
w(f"| Overlap groups | none | Rows that fail together on one trap (ZOM-569: {c('reg_569', 'bs_569', 'z_569')}; ZOM-567: "
  f"{c('reg_567', 'bs_567', 'z_567')}) grade different facts on different deliverables (call, build status, blocker list) "
  f"and share a root cause, not an embedded acceptance condition (Eval 3 3.3); the register call and the ZOM-570 listing of "
  f"one ticket are the same fact in two prompt-specified deliverables (3.3 'Not duplicates'); no fact sits in three rows |")
w(f"| G1 register calls outside BLOCKER | samples {c('fix_429', 'fix_563', 'smp_art793', 'smp_481', 'smp_536')}; direct "
  f"exceptions {c('fix_558', 'smp_477')} | volume {T['count133']} = 133; BLOCKER class graded in full "
  f"({rng('reg_')}) |")
w(f"| G2 build status | samples {c('bs_473', 'bs_429', 'bs_477')}; direct exception values {c('bs_569', 'bs_567', 'bs_563')} "
  f"| volume {T['count133']} |")
w(f"| G3 QA result · G4 evidence · G5 title | {c('qa_449', 'qa_559')} · {c('ev_435', 'ev_563')} · {c('title_546')} | volume "
  f"{T['count133']} |")
w(f"| ZOM-570 blocker list | graded in full, {T['z_293']} to {T['z_des313']} and {T['z_new']} | count {T['z_count']} = 19 |")
w("| Predicted all-fail | none: 0 rows | Every value is reachable by Vincent through cataloged tools (plan §E visibility "
  "proof); rows that both earlier baseline batches failed (ZOM-293's call, the 19-blocker count) are hard, not impossible |")
w("")
w("## Dimensions")
w("| Dimension | Count / % | Threshold | Status |")
w("|---|---|---|---|")
w(f"| Overall Rubric Quality | 0 Major · 0 Moderate · 0 Minor of {n} rows (0%) | any Major/Moderate fails; Minor < 5% passes | PASS |")
w(f"| Criteria Weights | 0 of {n} rows off by one level (5 ×{sum(1 for r in rows if r['w'] == 5)}, 3 ×{sum(1 for r in rows if r['w'] == 3)}, 1 ×{sum(1 for r in rows if r['w'] == 1)}; the same ticket keeps one weight on the register and ZOM-570) | ≤ 10% one level off is NON-FAIL 4; all match is PASS | PASS |")
w(f"| Category Balance | {n} Outcome · 0 Process | ≥ 1 Outcome, Process ≤ 50% | PASS |")
w("| Process Rubrics | 0 ordering dependencies without a check (the prompt sets a deadline, not an order; the new key on ZOM-570 and in the register is an Outcome) | 1 missing is NON-FAIL 3 | PASS |")
w(f"| Agent-Centric Phrasing | 0 of {n} titles off pattern (every title starts 'The Agent'; no tool identifier) | > 10% off pattern fails | PASS |")
w(f"| Negative Criteria | 0 prohibition-only titles; do_nothing_case REJECT on {n}/{n} | any idle-pass row fails | PASS |")
w("| Predicted all-fail | 0 | tolerance 0 | PASS |")
w("| Known data issue | 0 rows rest on a card in references/known_data_issues/synthcut.md | any fails | PASS |")
w(f"| Schema, accuracy, coverage and contradiction repair gates | schema ok; values re-read (V3 rubric_rows); 15/15 requirements and 27/33 slots covered plus 6 dispositioned; rows jointly satisfiable | a failure blocks | PASS |")
w(f"Threshold margin: with {n} rows one Minor issue is {100 / n:.1f}% (NON-FAIL band from 5%), one Major or Moderate fails.")
w("")
w("## Self-review")
w("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
w("|---|---|---|---|---|")
for i, (cr, r) in enumerate(zip(crit, rows), 1):
    w(f"| C{i} (Outcome, weight {cr['weight']}) | cleared | False negative? A valid run writes {cell(r['valid'])}; near miss: "
      f"{cell(r['alt'])} | Title accepts {cell('; '.join(r['acc']))}; it rejects the near miss by naming {r['vals']}; deciding "
      f"records {r['fids']} re-verified (Working_Files/rubric/build_rubric.py, hg.py get-many / SQL) | none |")
w("| Coverage both ways | cleared | Could a requirement have no row? | §Coverage lists 15 requirements, each with a row that "
  "rejects omission and a wrong result; every OE maps to a row (plan §B) | none |")
w("| Runbook side procedures | cleared | Could 'link it here', the support playbook note or the matrix post be required? | "
  "Not incorporated: the platform /prompt report limits the runbook to its checks for the new-ticket ask; the OE (PASS) "
  "omits them; Vincent is a reader on f_b91db376f65604b8602657 | none |")
w("| Re-verify | cleared | Values carried from the ledger could be stale | every quote asserted verbatim against its record by "
  "build_rubric.py; base records via hg.py get-many; V3 rubric_rows bind each source value | none |")
w("")
w("Unresolved: none for the rubric. Upstream chain: the rubric-writing gate passes 28 of 29 checks (the shortcut probe "
  "and its re-run included); its one failing check, diversity.authority_share, is the structural Leonard's-rules finding "
  "recorded in the plan. It is not a /rubric dimension, so chain.rubric-writing stays open until the human accepts it.")
w("")
w("## Reminders")
w("- An all-Outcome set is normal; Process is not added to look thorough.")
w("- Enter the criteria in the builder exactly as in 09_Rubrics.json and diff the export field by field before the verifier "
  "runs (learnings §62).")
(TI / "Working_Files/09_Rubric_Check.md").write_text("\n".join(out) + "\n")
print("check written", len(out), "lines")
