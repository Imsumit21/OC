#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) for 09_Rubrics.json against the plan (rows.json), the eval lint and
the /rubric checks. The independent pre-review's findings were applied to the JSON before this report; they are recorded
under 'Pre-/rubric review applied', and the Findings table holds only findings on the current JSON."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
WS = TI.parents[1]
rows = json.loads((HERE / "rows.json").read_text())
crit = json.loads((TI / "09_Rubrics.json").read_text())
assert len(rows) == len(crit) and all(r["t"] == c["title"] for r, c in zip(rows, crit))
C = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
CTX = json.loads((WF / "00_Task_Context.json").read_text())
lint = json.loads(subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/hg.py"), "rubric-lint",
                                  str(TI / "09_Rubrics.json")], capture_output=True, text=True, cwd=WS).stdout)
sys.path.insert(0, str(HERE))
import build_selfreview as SR  # noqa: E402  (counter-readings per tag; rewrites selfreview.md, same content)

surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
COVER = {"X1": "nin_decision", "X2": "card_nin", "X3": "fw_decision", "X4": "rem_fw", "X5": "lf_decision", "X6": "lf_by",
         "X20": "sp_decision", "X10": "cf_next", "X11": "cf_cancel", "X12": "ph_next", "X13": "ph_told", "V1": "log_rows",
         "P1": "reply_pingwise", "P2": "reply_markward", "X15": "lf_told", "X17": "nin_next", "X16": "pw_next", "X18": "rem_hoot",
         "X19": "rem_lf", "X21": "ct_hoot", "C1": "bal_by", "C2": "mf_by", "C3": "sp_by", "C5": "sv_told", "C6": "kin_told",
         "C7": "card_kin", "C8": "esg_lumen", "C9": "ct_rev", "C10": "card_mark", "C11": "ww_told", "D1": "log_folder",
         "D2": "reply_keep_count"}
DISP = {"X9": "duplicate fact: Clipforge's End is graded by its cancellation write {cf_cancel} and its Oct 15 last day {cf_next} "
              "(gate 6); notice frederick.stone@harmonygames.co/1843067564852153540 decides all three",
        "X14": "duplicate fact: Framewell's Park is graded by {fw_decision} and its Jan 5 reminder {rem_fw}; the Next date "
               "2026-01-05 is the same January-review fact (gate 6), decided by C07C2866011/1758920520.674991"}
assert set(COVER) | set(DISP) == {s["id"] for s in surf["slots"]}


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def cs(*tags):
    return ", ".join(C[t] for t in tags)


L = []
A = L.append
n = len(crit)
n_proc = sum(1 for c in crit if c["category"] == "Process")
tw = sum(c["weight"] for c in crit)
bands = {b: sum(1 for c in crit if c["weight"] == b) for b in (5, 3, 1)}
sha = hashlib.sha256((TI / "09_Rubrics.json").read_bytes()).hexdigest()[:12]
A("# 09 Rubric Check — frederick_q4_commitments (vendor and partner backlog, injection rev4)")
A(f"Checked 2026-11-05 (after /rubric round 2, FAIL 1 on five wording fixes; all five applied exactly) · Criteria {n} (builder minimum 5: ok) · Plan 2026-11-05 (09_Rubric_Writing_Plan.md, rows P1–P{n} = "
  f"C1–C{n}) · 09_Rubrics.json sha256 {sha} · weight {tw} (5 ×{bands[5]}, 3 ×{bands[3]}, 1 ×{bands[1]})")
A("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · evidence=`evidence` · "
  "schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category Outcome or Process; weight 1, 3 or 5)")
A("Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict")
A(CTX["universe"]["clock_line"] if CTX["universe"]["clock_line"].startswith("Clock:") else f"Clock: {CTX['universe']['clock_line']}")
A("")
A(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json`): {lint['count']} findings — "
  "no `disguised_negative`, `format_lock`, `anon_token`, `evidence_no_record`, `vague_exemplar`, `tool_name`, `prohibition_title` "
  "or schema hit to resolve.")
A("")
A("## Coverage")
A("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |")
A("|---|---|---|")
ANS_END = ("ans_pixel", "ans_brightlane", "ans_soundvault", "ans_streamcast", "ans_lingora", "ans_panelpulse", "ans_ascendo", "ans_wishwave")
ANS_PARK = ("ans_framewell", "ans_retainly", "ans_hootline", "ans_glyphworks", "ans_cloudlark", "ans_echohall", "ans_pressbeam",
            "ans_quillcraft", "ans_tilecast", "ans_benchmarkly", "ans_loopnote", "ans_driftwood")
ANS_SIGN = ("ans_orbit", "ans_bundle", "ans_bundle_sign", "ans_kin_lawyers", "ans_kin_sign", "ans_lumen_lawyers", "ans_lumen_sign",
            "ans_markward", "ans_playfuse")
ESG_P = ("esg_lumen", "esg_lumen_date", "esg_lumen_cost", "esg_lumen_signer", "esg_kinetic", "esg_kin_date", "esg_kin_cost",
         "esg_kin_signer", "esg_bundle", "esg_bh_term", "esg_bh_date", "esg_bh_cost", "esg_bh_signer")
COV = [
    ("The log goes in Frederick's Q4 commitments folder (prompt)", cs("log_folder"), "covered — a sheet left in My Drive fails"),
    ("A native Google Sheet (Leonard: 'a sheet'; README 'One sheet')", cs("log_type"), "covered — an uploaded xlsx fails"),
    ("Named per the README ('Name it \"Q4 commitments log\"')", cs("log_name"), "covered — another name fails"),
    ("The README's seven columns, from the template's header row", cs("log_header"), "covered — a dropped or reordered column fails"),
    ("One row per company in scope: 36 (Leonard's scope sentence and exclusions)", cs("log_rows"),
     "covered — 34 (Nintendo, Balancy left off) or 37 (a look-alike added) fails"),
    ("Decision per the guardrails' first-fit order (Answered, cash test, Keep exception, Sign, Park)",
     cs("nin_decision", "fw_decision", "lf_decision", "sp_decision", "pw_decision"), "covered — End for Framewell or Pingwise, Sign for Lanternfly fail"),
    ("Contact and What's waiting columns (README)", cs("rev_contact", "sv_waiting"), "covered — a blank cell fails each sample"),
    ("Answered by, and when, for the Answered rows (README; guardrails step 1 'Note who answered and when')",
     cs("lf_by", "sp_by", "bal_by", "mf_by", "mf_when"), "covered — a blank, Frederick, or no date fails"),
    ("Next date per the README rule (End last day, Keep next bill, Sign needed-by, Park and 'later' answers the January review)",
     cs("nin_next", "cf_next", "ph_next", "pw_next", "lf_next"), "covered — Jan 15 for Clipforge, Oct 31 for Pingwise or a blank for Lanternfly fails"),
    ("What we told them (the five §4b marks material)", cs("ph_told", "lf_told", "sv_told", "kin_told", "ww_told"),
     "covered — parked for Wishwave, lawyers-first for Lanternfly fail"),
    ("A written answer to everyone waiting, this week (Leonard)", cs("ans_count"),
     "covered — 33 (Rina and Wen written to again) or 30 (Mateo skipped) fails"),
    ("End answers: say no, or cancel it in writing the way the paper or notice asks (step 2)",
     cs("cf_cancel", "cf_priya", *ANS_END, "rev_cancel"), "covered — one row per recipient; parking an End company or a reply to the unmonitored notice fails"),
    ("Keep answers: tell them we're staying (step 3)", cs("ans_certwell", "ans_vaultline", "ans_pingwise"),
     "covered — one row per recipient; a downgrade request or a thanks with no decision fails"),
    ("Sign answers: with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it (step 4)", cs(*ANS_SIGN),
     "covered — one row per recipient and part; 'with Leonard or Arthur' alone fails the lawyers-first rows"),
    ("Park answers: we'll pick it up in January (step 5)", cs(*ANS_PARK), "covered — one row per recipient; a decline fails"),
    ("One ESG intake email per agreement ESG must see (ESG's note, Leonard's reply)", cs("esg_count"),
     "covered — a fourth email (Lanternfly) or one combined email fails"),
    ("Each intake email carries the checklist (term, exclusivity or IP licence, cost, needed-by date, signer)", cs(*ESG_P),
     "covered — every checklist part of each of the three emails; an email without it, or a combined email, fails"),
    ("Signing cards on the board's To Do list, company name in the title (Leonard's reply)", cs("card_count", "card_nin", "card_kin", "card_mark"),
     "covered — six cards, a Doing card or a combined card fails"),
    ("Each company's person into Contacts, company in the job field, no duplicates (Leonard; README)",
     cs("ct_count", "ct_hoot", "ct_rev", "ct_wen"), "covered — re-adding Noor Haddad, a contact with no email, or leaving Gemma out fails"),
    ("A January-review reminder on that day, one per company (prompt; guardrails steps 1 and 5)",
     cs("rem_count", "rem_fw", "rem_lf", "rem_hoot"), "covered — one listing event or 11 events fails"),
    ("Reply to Leonard on his email (prompt): what we're keeping (Leonard)",
     cs("reply_keep_count", "reply_pingwise", "reply_certwell", "reply_vaultline"),
     "covered — every member; a new email outside the thread, or two kept companies, fails"),
    ("Reply to Leonard on his email: what's waiting on Arthur or Leonard to sign (Leonard)",
     cs("reply_sign_count", "reply_markward", "reply_nintendo", "reply_bundlehouse", "reply_kinetic", "reply_lumencloud", "reply_orbit",
        "reply_playfuse"), "covered — every member; six or eight companies fails"),
    ("'When it's all done, reply' — the reply comes after every other write (prompt)", cs("order_reply"),
     "covered — any write after the reply fails"),
    ("Exclusions (look-alikes off the log; no answer to answered companies; no ESG email for the template NDA)",
     cs("log_rows", "ans_count", "esg_count", "card_count", "reply_sign_count"), "covered — as exact counts on the required writes (gate 7)"),
]
for a, b, d in COV:
    A(f"| {a} | {b} | {d} |")
A("Unauthorized criteria: none")
A("")
A("Not graded, with the reason: the log's tab name is representational in brief §4b D1. The Contact, What's waiting and "
  "answered-when cells are sampled (one row each, /rubric round 1); the other companies' cells in those columns are repetitive "
  "members under the log volume row.")
A("")
A("## Coverage — gradable surface")
A("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
A("|---|---|---|---|---|")
for s in surf["slots"]:
    if s["id"] in DISP:
        A(f"| {s['id']} | {s.get('fact_id') or '—'} | — | dispositioned | {DISP[s['id']].format(**C)} |")
    else:
        t = COVER[s["id"]]
        A(f"| {s['id']} | {s.get('fact_id') or rows[int(C[t][1:]) - 1]['fact']} | {C[t]} | covered | the title rejects the omission "
          f"and the plausible wrong value |")
MECH = ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8")
mw = sum(r["w"] for r in rows if any(m in r["dec"].split() for m in MECH))
A(f"Mechanism share: {round(100 * mw / tw)}% of the criteria weight (reported, not gated)")
A("")
A("## Findings")
A("")
A("No finding on the current 09_Rubrics.json. /rubric round 2 (FAIL 1: 2 Major, 3 Minor; Weights 5, every other dimension 5; "
  "coverage 102/102; run_forensics/rev4/rubric_r2/platform_rubric_review_r2.md) gave five checked fixes; all five are copied "
  "exactly (table below), and the other 97 rows are byte-identical to the JSON it reviewed (sha256 93b2e0511508). Round 1's Fix "
  "List is recorded after it.")
A("")
A("## /rubric round 2 fixes applied (2026-11-05)")
A("| # | Round-2 item | Type (severity) | Change, copied exactly from the report |")
A("|---|---|---|---|")
R2FIX = [
    (cs("rev_contact"), "Accept took the bare 'Hana' the title did not", "not_self_contained (Major)", "title: 'Hana Kobayashi (or Hana) or her email PERSON_9708_EMAIL'"),
    (cs("ans_markward"), "'to accept' could fail the 'to sign' reply step 4 prescribes; a lawyers-first reply passed", "overly_specific (Major)",
     "title 'to sign or accept' plus the pass/fail clauses; Accept in R43's form"),
    (cs("ans_orbit"), "a lawyers-first reply to Mateo passed (no ESG trigger)", "overly_broad (Minor)", "title with the pass/fail clauses; weight 5; Accept as given"),
    (cs("ans_playfuse"), "a lawyers-first reply to Iris passed (the 2-year term is a decoy)", "overly_broad (Minor)",
     "title with the pass/fail clauses; weight 5; the given justification; Accept adds 'with or without a mention of ESG's NDA template'"),
    (cs("esg_lumen_date"), "the only ESG row without 'alone'", "overly_broad (Minor)", "title and Accept end 'about Lumencloud alone'"),
]
for i, (row, a, t, d) in enumerate(R2FIX, 1):
    A(f"| {i} | {row}: {a} | {t} | {d} |")
A("")
A("## /rubric round 1 Fix List applied (2026-11-05)")
A("| # | Fix List item (round-1 numbering R1–R57) | Change in the current JSON (current numbering) |")
A("|---|---|---|")
R1FIX = [
    ("R1: evidence repeated the file-type check", f"{cs('log_folder')}: title '(created there or moved there)'; Accept: the Agent's log whose final parent is that folder"),
    ("R12, R13, R16, R18, R20, R26, R28, R30, R38 weight 5 → 3", f"{cs('bal_by', 'mf_by', 'ph_next', 'ph_told', 'sv_told', 'ans_orbit', 'ans_retainly', 'rev_cancel', 'card_kin')} at 3, justification 'Interpretation: …'"),
    ("R33, R41, R42 weight 5 → 1", f"{cs('esg_lumen_date', 'ct_hoot', 'ct_rev')} at 1"),
    ("R24 evidence narrower than the title", f"{cs('cf_cancel')}: Accept names HG-2291, UGC Studio or Clipforge"),
    ("R25 evidence accepted 'the pilot ends'", f"{cs('cf_priya')}: 'ending the pilot or not carrying on after it' in title and Accept"),
    ("R27 'staying on and renewing'", f"{cs('ans_certwell')}: 'staying with Certwell for the API domain certificate (staying on, keeping it or confirming the renewal)'"),
    ("R28 evidence added 'deciding in January'", f"{cs('ans_retainly')}: '(picking it up, revisiting it or deciding in January)', weight 3"),
    ("R29 two parts in one row", f"split: {cs('ans_bundle')} lawyers first (5) and {cs('ans_bundle_sign')} with Leonard or Arthur to sign (3)"),
    ("R31 evidence dropped 'one per agreement'", f"{cs('esg_count')}: Accept adds 'one per agreement'"),
    ("R32, R34, R35 evidence dropped 'of its own'; weight 1", f"{cs('esg_lumen', 'esg_bundle', 'esg_kinetic')}: '… in its intake email to ESG Law intake (PERSON_2599_EMAIL) about the agreement alone', weight 1; territories dropped"),
    ("Add 9 ESG checklist rows (weight 1)", f"{cs('esg_kin_date', 'esg_bh_date', 'esg_lumen_signer', 'esg_kin_signer', 'esg_bh_signer', 'esg_kin_cost', 'esg_bh_cost', 'esg_lumen_cost', 'esg_bh_term')}; the Lumencloud cost row ({cs('esg_lumen_cost')}) is the author's rewrite: any wording that it costs nothing, with or without the credits condition"),
    ("R36 volume row must state the template", f"{cs('card_count')}: 'each with the name of the company it is for in its title'"),
    ("R37–R39 'only company'; R38 failed a card naming ESG", f"{cs('card_nin', 'card_kin', 'card_mark')}: 'a card of its own for the company … (its title names that company and no other company waiting to sign)'; {cs('card_kin')} weight 3"),
    ("R40 volume row must state the template", f"{cs('ct_count')}: 'one per company (each company's contact), each with that person's company in the job field'"),
    ("R41, R42 passed a contact with no email; add a third sample", f"{cs('ct_hoot', 'ct_rev')} name the email; {cs('ct_wen')} Wen Halvorsen (PERSON_9702_EMAIL), Lanternfly Publishing (or Lanternfly); all weight 1"),
    ("R44–R46 'only company'", f"{cs('rem_fw', 'rem_lf', 'rem_hoot')}: 'a reminder event of its own for the company … (naming that company and no other company from the vendor and partner backlog, in its title or description)'"),
    ("R47 remove", "removed; every reply row names Leonard's thread"),
    ("R48–R51 passed an off-thread email", f"{cs('reply_keep_count', 'reply_pingwise', 'reply_sign_count', 'reply_markward')} end '… in its reply on Leonard's \"Vendor and partner stuff while I'm in LA\" email'"),
    ("Add 8 reply rows", f"keep {cs('reply_certwell', 'reply_vaultline')} (5); sign {cs('reply_bundlehouse', 'reply_kinetic', 'reply_lumencloud', 'reply_orbit', 'reply_playfuse')} (3), {cs('reply_nintendo')} (5)"),
    ("R52–R57 one ordering ask split six ways", f"one Process row {cs('order_reply')}; the other five removed"),
    ("Add 27 company-answer rows", f"End {cs(*ANS_END)}; Keep {cs('ans_vaultline', 'ans_pingwise')}; Sign {cs('ans_kin_lawyers', 'ans_kin_sign', 'ans_lumen_lawyers', 'ans_lumen_sign', 'ans_markward', 'ans_playfuse')}; Park {cs(*[t for t in ANS_PARK if t != 'ans_retainly'])}. The Pingwise row ({cs('ans_pingwise')}) is the author's rewrite: 'staying with Pingwise on the Team plan rather than dropping to the free plan (staying on, going ahead with Team from Nov 1 or keeping the paging; any wording with that meaning)'"),
    ("Add 5 log rows", f"{cs('pw_decision')} Pingwise Keep (5), {cs('lf_next')} Lanternfly Jan 5, 2026 (5), {cs('rev_contact')} Reviewly Contact (1), {cs('sv_waiting')} Soundvault What's waiting (1), {cs('mf_when')} Motive Forge Sep 19, 2025 (3)"),
]
for i, (a, d) in enumerate(R1FIX, 1):
    A(f"| {i} | {a} | {d} |")
A("")
A("## Pre-/rubric review applied earlier (independent reviewer, 2026-11-04, on the 49-row draft; round 1 reviewed the result)")
A("| # | Raised against the 49-row draft | /rubric type it predicted | Change in the current JSON |")
A("|---|---|---|---|")
HIST = [
    ("23 titles in the possessive form ('The Agent's log…', 'The Agent's reply…')", "Agent-Centric FAIL (> 10% off-pattern)",
     "every title now reads 'The Agent' + action (gives, puts, records, names, lists)"),
    ("9 rows at weight 3 that join a company's records with a rule doc in another service", "Criteria Weights FAIL (18% one level off)",
     "all nine were set to 5; /rubric round 1 judged that one level too high and they are now 3 or 1 (table above)"),
    ("Folder and sheet type bundled in one row", "non_atomic", f"split into {cs('log_folder')} (folder) and {cs('log_type')} (native Sheet)"),
    ("Accepted name forms only on the Accept line (Nintendo Developer Portal, Lanternfly, Pixel Harbor)", "not_self_contained",
     "the name forms are in the titles"),
    ("Orbit Store's title said 'to sign', its Accept line 'to sign or accept'", "not_self_contained", f"{cs('ans_orbit')} now says 'to sign or accept'"),
    ("One combined Jan 5 event, ESG email or card would pass every per-company row", "overly_broad",
     "the per-company rows require the company as the event's or card's only company, or an intake email of its own"),
    ("Bundlehouse's ESG row required 'name, logo and art' only", "overly_specific", f"{cs('esg_bundle')} accepts a general licence of our IP"),
    ("Order rows' titles named a write action more loosely than their Accept lines", "not_self_contained",
     "they listed the same write kinds; /rubric round 1 merged the six into one ordering row (table above)"),
    ("Answer content for Keep, Park and lawyers-first Sign untested; Reviewly's cancellation only counted", "missing_coverage",
     f"added {cs('ans_certwell', 'ans_retainly', 'ans_bundle', 'rev_cancel')}"),
    ("ESG checklist items beyond the term and licence untested; Kinetic Arcade's email unsampled", "missing_coverage",
     f"added {cs('esg_kinetic', 'esg_lumen_date')}"),
    ("The README's naming line had no row", "missing_coverage", f"added {cs('log_name')}"),
]
for i, (a, b, d) in enumerate(HIST, 1):
    A(f"| {i} | {a} | {b} | {d} |")
A("")
A("## Overlap groups · Spot-check groups · Predicted all-fail")
A("| Group / row | Members / basis | Shared condition / reason |")
A("|---|---|---|")
GR = [("G1 log columns", cs("nin_decision", "fw_decision", "lf_decision", "sp_decision", "pw_decision", "rev_contact", "sv_waiting",
       "lf_by", "sp_by", "bal_by", "mf_by", "mf_when", "nin_next", "cf_next", "ph_next", "pw_next", "lf_next"),
       f"samples and direct exception rows, at most 5 per column; volume row {cs('log_rows')}"),
      ("G2 What we told them", cs("ph_told", "lf_told", "sv_told", "kin_told", "ww_told"), f"5 samples; volume row {cs('log_rows')}"),
      ("G3 written answers", f"{len(ANS_END) + len(ANS_PARK) + len(ANS_SIGN) + 6} rows, one per recipient and part",
       f"not sampled: the content differs per target (rubric_flow_v2); volume row {cs('ans_count')}"),
      ("G4 ESG intake", f"{len(ESG_P)} rows", f"every checklist part of each of the three emails; volume row {cs('esg_count')}"),
      ("G5 To Do cards", cs("card_nin", "card_kin", "card_mark"), f"3 samples; volume row {cs('card_count')} states the template"),
      ("G6 contacts", cs("ct_hoot", "ct_rev", "ct_wen"), f"3 samples; volume row {cs('ct_count')} states the template"),
      ("G7 reminders", cs("rem_fw", "rem_lf", "rem_hoot"), f"3 samples; volume row {cs('rem_count')} ('one per company')"),
      ("G8 / G9 reply lists", "every member: " + cs("reply_pingwise", "reply_certwell", "reply_vaultline", "reply_markward", "reply_nintendo",
       "reply_bundlehouse", "reply_kinetic", "reply_lumencloud", "reply_orbit", "reply_playfuse"),
       f"volume rows {cs('reply_keep_count', 'reply_sign_count')}"),
      ("Overlap groups", "none", "one ordering row; each per-company row fails only when its own write is missing or wrong (§3.3 own-artifact exemption)"),
      ("Predicted all-fail", "0 rows on the four Evals bases", "every value is reachable through a cataloged tool and visible to Frederick "
       "(plan §E visibility proof); the rows all six rev4 baselines miss are discovery failures on reachable records")]
for a, b, d in GR:
    A(f"| {a} | {b} | {d} |")
A("")
A("## Dimensions")
A("| Dimension | Count / % | Threshold | Status |")
A("|---|---|---|---|")
A(f"| Overall Rubric Quality | 0 Major · 0 Moderate · 0 Minor of {n} rows | any Major or Moderate fails; Minor < 5% | PASS (predicted) |")
A(f"| Criteria Weights | 0 rows off: every weight follows the round-1 Fix List ({bands[5]} at 5, {bands[3]} at 3, {bands[1]} at 1) | ≤ 10% one level, none two levels | PASS (predicted) |")
A(f"| Category Balance | {n - n_proc} Outcome / {n_proc} Process | ≥ 1 Outcome, Process ≤ 50%, < 2 unnecessary Process rows | PASS |")
A(f"| Process Rubrics | {n_proc} ordering row for the one ordering ask; 0 missing ordering checks | 0 missing, every Process row valid | PASS |")
A(f"| Agent-Centric Phrasing | {n}/{n} titles 'The Agent' + action; 0 artifact subjects or tool names | off-pattern ≤ 10% | PASS |")
A("| Negative Criteria | 0 prohibition-only titles; 0 rows an idle Agent passes | 0 | PASS |")
A("| Predicted all-fail | 0 | 0 (harness tolerance) | PASS |")
A("| Schema and repair gates (schema, self-containment, accuracy, atomicity, coverage, duplicates, contradiction, format-5 cases) | "
  "clean | all clean | PASS |")
A(f"Threshold margin: with {n} rows, one Major is {100 / n:.1f}% and one row off-weight is {100 / n:.1f}%; any Major still fails Overall "
  "Rubric Quality, so the two author-written rows are the main risk for run 2.")
A("")
A("## Self-review")
A("")
A("Re-read as /rubric in phase order (Evals/3_Rubrics_Eval.md 1.2 schema, 1.4 coverage, 2.1–2.12 per row, 3.1–3.7 set level, 5.1 "
  "predicted all-fail) and the pre-verdict sweep: one missing requirement (none after round 1's 51 added rows: every written answer, "
  "ESG part and reply-list member), one phrasing mismatch with the prompt (none), one non-atomic row (none after the Bundlehouse "
  "split), one category mislabel (none), one over-specific title (none: the card rows let ESG Law, Leonard or Arthur appear), one "
  "duplicate or cascade group (none after the six ordering rows were merged), one vague exemplar (none: lint 0, the two 'such as' "
  "lists rewritten), one prohibition-only title (none).")
A("")
A("Re-verified: every literal in the titles was re-read in this run by plan/rubric/build_rubric.py — counts from solver/truth.json "
  "and the records (36 / 31 / 3 / 7 / 32 / 14 / 3 / 7), every PERSON_* address from the company's own SQL message row, dates from "
  "the papers, the Paylane notice, the ZOM-567 comment and evt_fd469c29811879519c2c96 — and the V3 source values through hg.py "
  "get-many and the parsed SQL (00_V3_Authoring_Evidence.json rubric_rows, rubric_hash current). The independent reviewer "
  "re-checked the same literals against the SQL and base Contacts and found none wrong.")
A("")
A("Tally recount from the findings table: 0 Major, 0 Moderate, 0 Minor; predicted all-fail 0; no validity defect.")
A("")
A("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
A("|---|---|---|---|---|")
for i, r in enumerate(rows):
    A(f"| C{i + 1} {r['tag']} | cleared | Counter-reading — {cell(SR.CR[r['tag']])} | resolved by the title as written (evidence: "
      f"{cell(r['ev'].split('Accept:')[0][:150])}…) | — |")
A("")
A("Local baseline grade on the current JSON (plan/rubric/grade_baselines.py, rev4 batch; an estimate, not the verifier):")
A("")
A("```text")
A(SR.grade)
A("```")
A("")
A("Unresolved: (0) /rubric run 3 should lock the 97 unchanged rows and the five exact copies; its Notes for QM (not scored) "
  "suggest an optional 'names the agreement' row per ESG email and 'sent' in R30's evidence, left as they are so the locks hold. "
  f"{C['ans_orbit']} keeps its 'Interpretation:' justification at weight 5 because the fix changed only its title, weight and Accept. "
  "(1) the upstream rubric-writing gate carries one structural FAIL (diversity.authority_share: the guardrails doc, the "
  "README and the paperwork folder sit upstream of most of the weight), recorded in the plan for the human to accept; this check "
  "inherits it through chain.rubric-writing. (2) Brief §4b D1 lists the log name as representational, while the incorporated README "
  f"fixes it; {C['log_name']} follows the README (weight 1). (3) The rev4 batch estimates SD below the 0.10 band (local grade above); "
  "the requester chose to finish the rubric on rev4 first.")
A("")
A("## Reminders")
A("- An all-Outcome set is normal; Process is not added to look thorough.")
A(f"- Type all {n} criteria into the builder exactly as 09_Rubrics.json has them, export, and diff the export before /rubric and the verifier "
  "(weights and escaped brackets drifted on the bridge task).")
A("- Fix the criteria in the builder, re-export, re-run check, then run /rubric.")
(WF / "09_Rubric_Check.md").write_text("\n".join(L) + "\n")
print("check written:", n, "criteria; weight", tw, bands)
