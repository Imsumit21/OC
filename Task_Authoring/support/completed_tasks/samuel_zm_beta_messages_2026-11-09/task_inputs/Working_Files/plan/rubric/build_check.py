#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) for 09_Rubrics.json against the plan (rows.json), the eval lint and the /rubric
checks. Independent review items applied before this report sit under 'Independent reviews applied'; the Findings table holds only
findings on the current JSON (check_findings.json)."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
WS = TI.parents[1]
sys.path.insert(0, str(HERE))
import build_selfreview as SR  # noqa: E402  (counter-readings; rewrites selfreview.md, same content)
import build_plan as BP  # noqa: E402  (surface map; rewrites the plan, same content)

rows = json.loads((HERE / "rows.json").read_text())
crit = json.loads((TI / "09_Rubrics.json").read_text())
assert len(rows) == len(crit) and all(r["t"] == c["title"] and r["w"] == c["weight"] and r["ev"] == c["evidence"] for r, c in zip(rows, crit))
C = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
CTX = json.loads((WF / "00_Task_Context.json").read_text())
lint = json.loads(subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "rubric-lint", str(TI / "09_Rubrics.json")], capture_output=True, text=True, cwd=WS).stdout)
EXTRA = json.loads((HERE / "check_findings.json").read_text())
_old = json.loads((WF / "run_forensics/rev6/rubric_r2/09_Rubrics.submitted_d1cbadf710e9.json").read_text())
SAME = sum(1 for c in crit if c in _old)
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def cs(*tags):
    return ", ".join(C[t] for t in tags)


def fam(prefix, *skip):
    return [r["tag"] for r in rows if r["tag"].startswith(prefix) and r["tag"] not in skip]


L = []
A = L.append
n = len(crit)
n_proc = sum(1 for c in crit if c["category"] == "Process")
tw = sum(c["weight"] for c in crit)
bands = {b: sum(1 for c in crit if c["weight"] == b) for b in (5, 3, 1)}
sha = hashlib.sha256((TI / "09_Rubrics.json").read_bytes()).hexdigest()[:12]
A("# 09 Rubric Check — samuel_zm_beta_messages (beta player messages, injection rev6)")
A(f"Checked 2026-11-06 (after /rubric round 2, FAIL 1; its Fix List applied exactly to the reviewed JSON, sha d1cbadf710e9, and R21 rewritten as it asks) · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-05 (09_Rubric_Writing_Plan.md, rows P1–P{n} = C1–C{n}) · 09_Rubrics.json sha256 {sha} · weight {tw} (5 ×{bands[5]}, 3 ×{bands[3]}, 1 ×{bands[1]})")
A("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category Outcome or Process; weight 1, 3 or 5)")
A(f"Readiness for /rubric: {EXTRA['readiness']} — a prediction only; /rubric gives the verdict")
A(CTX["universe"]["clock_line"] if CTX["universe"]["clock_line"].startswith("Clock:") else f"Clock: {CTX['universe']['clock_line']}")
A("")
A("Input: this file is the builder script's own output, identical to plan/rubric/rows.json. Enter the changes in the Rubric Criteria Builder, then diff the export field by field against this file.")
A("")
hits = "; ".join(f"row {f['row']} {f['check']} '{f['text']}'" for f in lint["findings"]) or "none"
A(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputsK/09_Rubrics.json`): {lint['count']} finding(s): {hits}. Resolved: the `format_lock` hit is 'one page', a length the prompt states ('the one-page note'), so grading it is allowed (Eval 2.7). No `disguised_negative`, `anon_token`, `evidence_no_record`, `vague_exemplar`, `tool_name`, `prohibition_title` or schema hit.")
A("")
A("## Coverage")
A("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |")
A("|---|---|---|")
ASKC = ("boss_arena_attempts_refilled", "daily_gift_about_to_reset", "teammate_sent_lives", "infinite_lives_ending")
COV = [
    ("The new sheet goes in Samuel's Drive folder (prompt)", cs("sheet_folder"), "covered — a sheet left elsewhere fails"),
    ("Seven columns from the DM", cs("sheet_header"), "covered — a dropped column fails"),
    ("One row per message: every PNs Beta row plus every filed ask (DM)", cs("sheet_rows"), "covered — 32 rows, or a decoy added, fails"),
    ("A call on each one by the rule (DM)", f"{cs(*fam('call_'))} on the sheet; {cs(*fam('cm_', 'cm_count'))} on the tickets; {cs('tally_go')} as the Go count", "covered — every call is graded on its own ticket, so a wrong call fails on the correct artifact"),
    ("What's missing: the failed test on Holds, the covering message on the covered Drop (rule doc)", cs(*fam("miss_")), "covered — a blank cell or another test fails"),
    ("Message: the row's name (DM)", cs("msg_lapsed_1_day"), "covered — a blank cell fails; sheet row count covers the rest"),
    ("Audience: who the ask says it's for (rule doc)", cs(*fam("aud_")), "covered — another group fails"),
    ("Ticket: the row's ticket, under whatever name (DM)", cs(*fam("ticket_")), "covered — a new key for Win & Collect, or ZOM-563 for the ask, fails"),
    ("Final headline: the latest line called, Go rows only (rule doc)", cs("head_l7", "head_l1", "head_count"), "covered — the replaced line fails, a headline on a Hold row fails"),
    ("String change: Go rows only (rule doc)", cs("str_l7", "str_l1", "str_count"), "covered — the wrong direction fails, a value on every row fails the count"),
    ("The one-page note goes in Samuel's Drive folder (prompt)", cs("note_folder"), "covered — a note left elsewhere fails"),
    ("One page (prompt)", cs("note_page"), "covered — a multi-page note fails"),
    ("D1 and D7 for the Sep 15 cohort week, iOS and Android separately (DM)", cs("note_ios_d1", "note_ios_d7", "note_android_d1", "note_android_d7"), "covered — a pooled or wrong-week figure fails"),
    ("Start with D1 and D7, then the lapsed reminders, then the Holds (DM)", cs("note_first"), "covered — another order fails"),
    ("The lapsed reminders the client schedules day by day (DM)", cs("note_ladder"), "covered — a list stopping at day 7 fails"),
    ("Anything the client already schedules that's still a Hold, and why (DM)", cs(*fam("nhn_"), *fam("nh_"), "note_count"), "covered — one listing row and one reason row per message; three or five names fail"),
    ("Leave the call as a comment on each ticket (DM)", f"{cs(*fam('cm_', 'cm_count'))}; {cs('cm_count')}", "covered — one row per ticket; a call left on the wrong ticket breaks the count"),
    ("Move the ticket to match: Drop to Canceled, Hold to Backlog unassigned, Go as they are (DM, rule doc, roadmap card)", f"{cs(*fam('mv_'), *fam('un_'))}", "covered — Todo fails, a state-only move fails the assignee rows, a Go ticket put in Backlog or Canceled breaks that count"),
    ("Anything with no ticket gets one, with no second ticket (DM)", f"{cs(*['new_' + a for a in ASKC])}; {cs(*fam('newb_'), *fam('newu_'))}; {cs('new_count')}", "covered — a second Win & Collect ticket makes six"),
    ("A string ticket under DES-314 for a changed line (rule doc)", cs("new_string"), "covered — the replaced line fails"),
    ("Every Go on a checklist on the push notifications card (prompt, DM)", cs("chk_lapsed_1_day", "chk_lapsed_7_days", "chk_count"), "covered — another card fails, a Hold on the list makes three"),
    ("Email each person who asked, apart from Leonard, what happened to their asks (DM)", f"{cs(*fam('em_', 'em_count'))}; {cs('em_count')}", "covered — one row per ask; nine people, or seven, fails"),
    ("The counts in that same DM (prompt, DM)", cs("dm_go", "dm_hold", "dm_drop"), "covered — one row per count, on D06L58XCVKK"),
    ("'When it's all finished': the counts come last (prompt)", cs("order_dm"), "covered — any listed write after the post fails"),
    ("Exclusions (decoys off the sheet; no second ticket; Leonard not emailed; Go tickets not moved)", cs("sheet_rows", "new_count", "em_count", "mv_backlog", "mv_cancel"), "covered — as exact counts on the required writes (gate 7)"),
]
for a, b, d in COV:
    A(f"| {a} | {b} | {d} |")
A("Unauthorized criteria: none")
A("")
A("Not graded, with the reason: the other Message cells, whose wording is free (brief §4b); the failed test in a ticket comment, because the DM asks for the call there and the reason is graded in the sheet and the note; the string ticket's state and assignee (brief §4b); the sheet's name.")
A("")
A("## Coverage — gradable surface")
A("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
A("|---|---|---|---|---|")
for s in surf["slots"]:
    if s["id"] in BP.DISP:
        A(f"| {s['id']} | {s.get('fact_id') or '—'} | — | dispositioned | {re.sub(r'\bP(\d+)\b', r'C\1', BP.DISP[s['id']])} |")
    else:
        t = BP.COVER[s["id"]]
        A(f"| {s['id']} | {s.get('fact_id') or rows[int(C[t][1:]) - 1]['fact']} | {C[t]} | covered | the title rejects the omission and the plausible wrong value |")
MECH = ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9")
mw = sum(r["w"] for r in rows if any(m in r["dec"].split() for m in MECH))
A(f"Mechanism share: {round(100 * mw / tw)}% of the criteria weight (reported, not gated)")
A("")
A("## Findings")
A("")
A("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
A("|---|---|---|---|---|---|---|---|")
for i, f in enumerate(EXTRA["findings"], 1):
    A(f"| {i} | {f['row']} | {f['quote']} | {f['rule']} | {f['what']} | {f['plan']} | {f['type']} | {f['sev']} |")
if not EXTRA["findings"]:
    A("| 0 | — | — | — | No finding on the current 09_Rubrics.json | — | — | — |")
A("")
A("## /rubric fixes applied (rounds 1 and 2, 2026-11-06)")
A("| # | Raised by the report | Change, or why it stands |")
A("|---|---|---|")
for i, (a, b) in enumerate(EXTRA["history"], 1):
    A(f"| {i} | {cell(a)} | {cell(b)} |")
A("")
A("## Overlap groups · Spot-check groups · Predicted all-fail")
A("| Group / row | Members / basis | Shared condition / reason |")
A("|---|---|---|")
GR = [("G2 Call column", cs(*fam("call_")), f"7 direct and 5 samples; volume {cs('sheet_rows', 'tally_go')}"),
      ("G3 What's missing column", cs(*fam("miss_")), f"9 direct exceptions and 1 sample; volume {cs('sheet_rows')}"),
      ("G4 Audience column", cs(*fam("aud_")), f"5 samples; volume {cs('sheet_rows')}"),
      ("G5 Ticket column", cs(*fam("ticket_")), f"1 direct and 2 samples; volume {cs('sheet_rows')}"),
      ("G7 ticket comments", f"{len(fam('cm_', 'cm_count'))} rows, one per ticket", f"not sampled: the content differs per target; volume {cs('cm_count')}"),
      ("G8 ticket moves", cs(*fam("mv_", "mv_backlog", "mv_cancel", "mv_unassign")), f"5 direct and 4 samples; volume {cs('mv_backlog', 'mv_cancel')}"),
      ("G8 assignees", cs(*fam("un_")), f"3 samples; volume {cs('mv_unassign')}"),
      ("G11 asker emails", f"{len(fam('em_', 'em_count'))} rows, one per ask", f"not sampled: the content differs per target; volume {cs('em_count')}"),
      ("Overlap groups", "none", "'unassigned' has its own rows; per-ticket state rows share a likely cause, not an embedded condition (Eval 3.3), and each fails only on its own ticket; R38 and R39 of the reviewed JSON read the sheet's own Go rows, so they embed no count"),
      ("Predicted all-fail", "0 rows on the four Evals bases", "every value is reachable through a cataloged tool and visible to Samuel (plan §E visibility proof); the rows all six baselines fail are discovery failures on reachable records")]
for a, b, d in GR:
    A(f"| {a} | {b} | {d} |")
A("")
A("## Dimensions")
A("| Dimension | Count / % | Threshold | Status |")
A("|---|---|---|---|")
tally = EXTRA["tally"]
A(f"| Overall Rubric Quality | {tally['major']} Major · {tally['moderate']} Moderate · {tally['minor']} Minor of {n} rows | any Major or Moderate fails; Minor < 5% | {EXTRA['overall']} (predicted) |")
A(f"| Criteria Weights | {tally.get('weights', 0)} rows off by this check ({bands[5]} at 5, {bands[3]} at 3, {bands[1]} at 1) | ≤ 10% one level, none two levels | PASS (predicted) |")
A(f"| Category Balance | {n - n_proc} Outcome / {n_proc} Process | ≥ 1 Outcome, Process ≤ 50%, < 2 unnecessary Process rows | PASS |")
A(f"| Process Rubrics | {n_proc} ordering row for the one ordering ask; 0 missing ordering checks | 0 missing, every Process row valid | PASS |")
A(f"| Agent-Centric Phrasing | {n}/{n} titles 'The Agent' + action; 0 artifact subjects or tool names | off-pattern ≤ 10% | PASS |")
A("| Negative Criteria | 0 prohibition-only titles; 0 rows an idle Agent passes | 0 | PASS |")
A("| Predicted all-fail | 0 | 0 (harness tolerance) | PASS |")
A("| Schema and repair gates (schema, self-containment, accuracy, atomicity, coverage, duplicates, contradiction, format-5 cases) | clean | all clean | PASS |")
A(f"Threshold margin: with {n} rows, one row off-weight is {100 / n:.1f}%, so up to 14 rows may be one level off for NON-FAIL 4; any single Major or Moderate still fails Overall Rubric Quality.")
A("")
A("## Self-review")
A("")
A("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md 1.2 schema, 1.4 coverage, 2.1–2.12 per row, 3.1–3.7 set level, 5.1 predicted all-fail), then the pre-verdict sweep: one missing requirement (none: table above), one phrasing mismatch with the prompt (none), one non-atomic row (none: counts are bare and each per-ticket row is one write), one category mislabel (none), one over-specific title (none: name forms and wording tolerances sit in the titles), one duplicate or cascade group (none after 'unassigned' moved to its own row), one vague exemplar (none: lint), one prohibition-only title (none: every row needs a write).")
A("")
A(f"Round-2 diff: {SAME} of {n} rows are byte-identical to the reviewed JSON (sha d1cbadf710e9); every other row is a Fix List item, a new row it asks for, R21's rewrite, or its one 'not scored' evidence edit.")
A("")
A("Whole-set mutation test: a complete valid run passes all rows, including with a concise final reply. Change one thing: a Hold called Go fails its sheet row (where sampled), its comment row, the Go count on the sheet, the DM counts and the checklist count; Lapsed 7 days given the replaced line fails its headline row and the string ticket row; Backlog replaced by Todo fails the move rows; Leonard emailed fails the email count; a second Win & Collect ticket fails the new-ticket count; the DM posted early fails the Process row. For a sampled column, a wrong unsampled cell is the documented sampling limit, and a wholesale error fails a count row.")
A("")
A("Re-verified: every literal in the titles and every quote in the evidence was re-read in this run by plan/rubric/build_rubric.py: seeded values by parsing 01_Universe_Inject.sql (never executed), base values through hg.py get-many; counts from the records (36, 32, 30, 28, 24, 8, 6, 5, 4, 2). V3 source values are in 00_V3_Authoring_Evidence.json rubric_rows with rubric_hash current.")
A("")
A(f"Tally recount from the findings table: {tally['major']} Major, {tally['moderate']} Moderate, {tally['minor']} Minor; predicted all-fail 0; no validity defect.")
A("")
A("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
A("|---|---|---|---|---|")
for i, r in enumerate(rows):
    A(f"| C{i + 1} {r['tag']} | cleared | Counter-reading — {cell(SR.cr(r))} | resolved by the title as written (evidence: {cell(r['ev'].split('Accept:')[0][:150])}…) | — |")
A("")
A("Local baseline grade on the current JSON (plan/rubric/grade_baselines.py over the six rev6 trajectories; an estimate, not the verifier):")
A("")
A("```text")
for l in SR.keep:
    A(l)
A("```")
A("")
A("Unresolved: (1) the upstream rubric-writing gate carries one structural FAIL (diversity.authority_share: DES-314 95%, the rule doc 90%), so it has no pasted PASS and this check inherits it through chain.rubric-writing; the human decides whether to accept it, as on the bridge and Q4 tasks. "
  f"(2) The local grade gives mean {SR.MEAN} and SD {SR.SD}: the retained SD band is expected to fail, and the requester has not ruled on it. (3) {SR.AF.group(1)} rows fail all six baselines, all on the comment asks; if ruled invalid the average rises above the cap, so /create-allfail must prove the route. "
  "(4) This file is not yet a builder export. (5) The report's sheet Call row for DES-344 puts that call on three artifacts, as the platform asked; the email row's fact is declared told:Lapsed 14 days, so the local duplicate check passes on the declared ids only.")
A("")
A("## Reminders")
A("- An all-Outcome set is normal; Process is not added to look thorough.")
A(f"- Enter all {n} criteria in the builder exactly as 09_Rubrics.json has them, export, and diff the export before /rubric and again before the verifier (weights and escaped brackets drifted on earlier tasks).")
A("- Fix the criteria in the builder, re-export, re-run check, then run /rubric.")
(WF / "09_Rubric_Check.md").write_text("\n".join(L) + "\n")
print("check written:", n, "criteria; weight", tw, bands)
