#!/usr/bin/env python3
"""Write Working_Files/mode_b_request.json for the rev7 six-run baseline (batch 2). Every quote was checked with
show.py against the bound export; hashes are computed here so a changed evidence file stales the request."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT.parent / "tools"))
import trajectory_ledger as tl  # noqa: E402

REV = "Working_Files/run_forensics/rev7/baseline2/"
sha = lambda rel: hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
EXPORT = {n: f"07_Baseline_Trajectories/trajectory-run-{n} (1).json" for n in range(1, 7)}
XSHA = {n: sha(p) for n, p in EXPORT.items()}


def ev(run, event, quote):
    return {"run": f"run-{run}", "event": event, "export_sha256": XSHA[run], "quote": quote}


def ref(*names):
    return [{"path": REV + n, "sha256": sha(REV + n)} for n in names]


diagnoses = [
 {"id": "D-OFF",
  "mechanism": "OFF: an in-scope item outside the obvious filter. Lucas was paid by five Western Union transfers before his first SVB notice; the receipts are in Robert's mail and the method counts them. Five of six runs wrote only the three notices.",
  "observation": "dominant_pattern", "criteria": ["R8", "R33", "R69"],
  "trajectory_events": [ev(2, 413, "Lucas, mini games dev."), ev(3, 346, "Sep to Nov 2024."), ev(4, 393, "3 notices, Sep-Nov 2024"),
                        ev(4, 344, "Western Union? Or wire?"), ev(5, 377, "Matches the notices."), ev(5, 267, "Western Union? Or wire?"),
                        ev(6, 678, "3 notices, Sep-Nov 2024."), ev(6, 351, "Oleg OR Ozhan OR MotMot OR Eveline OR PlayableX OR Lucas"),
                        ev(1, 575, "5 Western Union receipts in my mail")],
  "reason": "Runs 2, 3, 4 and 6 searched Gmail with broad receipt or multi-name queries, got one capped page of bare ids each, opened none and followed no page token; run 5 made no search aimed at Lucas. Runs 4 and 5 received Robert's own DM line about Western Union in a Slack result and did not follow it. Run 1 met a receipt in a bulk fetch of the wide notice search and then searched by name. The same three rows fail in five runs, and with run 5's single extra row they form four of the six failing runs.",
  "evidence": ref("review/run-2.md", "review/run-3.md", "review/run-4.md", "review/run-5.md", "review/run-6.md", "review/run-1.md", "review/rates_and_gates.md")},
 {"id": "D-RET",
  "mechanism": "RET: a done source with a missing piece elsewhere. The MotMot wire to account 8605 came back; Leonard says so in the founders' channel. Two runs kept all eleven notices; four found the message with one Slack search on the method's own words.",
  "observation": "first_read_correction", "criteria": ["R7", "R32", "R68"],
  "trajectory_events": [ev(1, 575, "11 notices."), ev(1, 205, "returned OR reversal OR recalled OR rejected"), ev(2, 413, "two accounts (3341, 8605)"),
                        ev(3, 257, "wire came back"), ev(3, 259, "Blake had the wrong number"), ev(4, 343, "wires"), ev(6, 456, "came back")],
  "reason": "Runs 1 and 2 never searched Slack for a return and never opened the founders' channel; run 1's only returns search was Gmail, 19 bare ids, none opened. Runs 3 to 6 each ran one short Slack search (wire came back, wires, came back) and Leonard's message came back first or second, because it carries the method doc's phrase.",
  "evidence": ref("review/run-1.md", "review/run-2.md", "review/run-3.md", "review/run-4.md", "review/run-5.md", "review/run-6.md")},
 {"id": "D-ALLFAIL",
  "mechanism": "Cascade: the Domino Delights build total on the sheet and in the reply is wrong whenever any Domino Delights build figure is wrong. Every run missed OFF or RET, so both rows failed six times on two different root causes.",
  "observation": "all_fail", "criteria": ["R25", "R58"],
  "trajectory_events": [ev(1, 650, "$963,374.64"), ev(2, 481, "$955,849.64"), ev(3, 426, "$951,818"), ev(4, 454, "$951,817.64"),
                        ev(5, 438, "$951,818"), ev(6, 747, "$951,817.64")],
  "reason": "Each written total differs from 959,342.64 by exactly 4,032.00 (MotMot kept in), 7,525.00 (Lucas left out) or both; the 22-payee register diff shows no other difference in any run.",
  "evidence": ref("review/all_fail_R25_R58.md", "review/register_diff.txt"),
  "fairness": {"reason": "The prompt asks for what each bet cost to build and delegates the counting to Leonard's doc; both adjustments are rules in that doc; one value fits the records; the rows accept any build-cost label and any rounding to $1K or finer; one of the 13 rev7 runs had both adjustments right.",
               "evidence": ref("review/all_fail_R25_R58.md", "review/rates_and_gates.md")},
  "readability": {"reason": "Leonard's message came back to four runs from one Slack search; the five receipts are in Robert's own mailbox and run 1 read them through ordinary Gmail calls. The runs that missed them took one capped page of bare ids and did not page or open it.",
                  "evidence": ref("review/all_fail_R25_R58.md", "review/run-1.md")},
  "grader_accuracy": {"reason": "For all twelve results the judge names the figure the run wrote, and it matches the write payload; no judge concedes the true figure and fails the row.",
                      "evidence": ref("review/all_fail_R25_R58.md")}},
 {"id": "D-CORR",
  "mechanism": "CORR: a wrong recollection on the issue, corrected by Arthur's Chase records mail. The mail names the payee and the account ending, so one token search joins it.",
  "observation": "heavy_all_pass", "criteria": ["R9", "R10", "R34"],
  "trajectory_events": [ev(2, 154, "3203"), ev(3, 297, "3203"), ev(4, 136, "JPMorgan OR Chase 3203"), ev(5, 224, "3203"),
                        ev(1, 255, "Chase records"), ev(6, 247, "Going through the Chase statements")],
  "reason": "Four runs searched Gmail for the account ending or the bank name from the issue and read the mail next; two met it in a sweep of recent mail. The note's own doubt sends every run looking, and the correction answers to the tokens on the issue.",
  "evidence": ref("review/run-2.md", "review/run-3.md", "review/run-4.md", "review/run-5.md", "review/run-1.md", "review/run-6.md")},
 {"id": "D-ORPH",
  "mechanism": "ORPH: Leapblock's close-out beats the notices and adds a wire with no Processed notice. The close-out post answers to the method's own word.",
  "observation": "heavy_all_pass", "criteria": ["R6", "R31"],
  "trajectory_events": [ev(1, 401, "received after:2026-01-20"), ev(2, 343, "Total 407,944 over 30 wires"), ev(3, 181, "Total 407,944 over 30 wires"),
                        ev(4, 307, "the first one 33,290"), ev(5, 257, "Total 407,944 over 30 wires"), ev(6, 417, "Total 407,944 over 30 wires")],
  "reason": "All six runs searched Slack for the word received with a recent date limit, and the close-out post was the first hit each time. The rule sentence and the record share the word, and the post is a day old.",
  "evidence": ref("review/run-1.md", "review/run-2.md", "review/run-3.md", "review/run-4.md", "review/run-5.md", "review/run-6.md")},
 {"id": "D-OLEG",
  "mechanism": "Oleg's returned wire is stated in the ENG-2459 note, in the same record as the claim.",
  "observation": "first_read_correction", "criteria": ["R11"],
  "trajectory_events": [ev(1, 75, "that wire came back the same day"), ev(2, 121, "that wire came back the same day"), ev(3, 141, "that wire came back the same day"),
                        ev(4, 69, "that wire came back the same day"), ev(5, 69, "that wire came back the same day"), ev(6, 75, "that wire came back the same day")],
  "reason": "Every run read the return in the issue's own note on its first pass over the comments; the Payoneer check took one search that returns two payment requests.",
  "evidence": ref("review/run-1.md", "review/run-3.md", "review/run-6.md")},
 {"id": "D-ZMCF",
  "mechanism": "ZM and Combo Fighter build totals: no decision that was missed in any run changes a ZM or Combo Fighter build figure.",
  "observation": "heavy_all_pass", "criteria": ["R26", "R27", "R59", "R60"],
  "trajectory_events": [ev(1, 650, "$544,433.44"), ev(1, 650, "$72,685.61"), ev(4, 454, "$544,433.44"), ev(6, 747, "$72,685.61"), ev(3, 426, "$544,433")],
  "reason": "Both missed adjustments (MotMot Apr 2024, Lucas Jun to Aug 2024) fall in the Domino Delights window. The ZM and Combo Fighter totals are sums of notices by date plus the Leapblock year split, which every run got from the close-out, and the Brooks bucket, which the ENG-2455 note states. Twenty weight points pass in every run.",
  "evidence": ref("review/all_fail_R25_R58.md", "review/register_diff.txt", "review/rates_and_gates.md")},
 {"id": "D-ALIAS",
  "mechanism": "ALIAS: a masked LLC on the bank is the UA agency Node Media. One run never resolved it and wrote Company; the miss changes one graded row, so that run stays in the Lucas pattern.",
  "observation": "transitive_bridge", "criteria": ["R12"],
  "trajectory_events": [ev(5, 377, "so Company"), ev(5, 294, "PERSON_4419_NAME"), ev(5, 322, "PERSON_4419_NAME"), ev(5, 311, "LLC"), ev(1, 524, "Node Media Invoices")],
  "reason": "Run 5 searched the payee token in Linear and Drive, never in Gmail or Slack, and put 16,428.57 in the Company column. Only the Bucket cell of that line is graded, so run 5 differs from runs 3, 4 and 6 on one row and joins their pattern: four of six.",
  "evidence": ref("review/run-5.md", "review/register_diff.txt", "review/rates_and_gates.md", "review/repairs.md")},
]

repairs = [
 {"id": "P-NODE", "diagnosis": "D-ALIAS", "artifact": "rubric", "owner": "create-rubric-writing",
  "change_kind": "outcome_coverage_row",
  "original_placement": "R12 grades only the Bucket cell of the PERSON_4419_NAME LLC line; the line's dollars are ungraded",
  "proposed_change": "One Outcome row for the dollars cell of that line (16,428.57 under Domino Delights; the Company or ZM column fails), entered as an exception row like R9 with R10. The rubric stage decides whether it stands as coverage.",
  "affected_outcomes": ["R12"],
  "scope_difference": {"reason_class": "difficulty", "rows_added": 1, "rows_removed": 0, "items_added": 0, "writes_added": 0},
  "fair_discovery_path": "The one notice to account 0115 is dated Jan 2 2025, inside the Domino Delights window; the method lists Marketing under its bet; the invoice thread in Robert's mail names Node Media.",
  "required_reruns": ["rubric-writing", "rubric-check", "verifier", "allfail", "difficulty"],
  "reason": "Run 5 and three batch-1 runs wrote Company with the dollars in the Company column. With both cells graded run 5 forms its own pattern and the largest pattern in this batch is three of six. Proposed after the baseline, so it stands only if the rubric stage accepts it as coverage.",
  "evidence": ref("review/repairs.md", "review/rates_and_gates.md")},
 {"id": "P-CORR2", "diagnosis": "D-CORR", "artifact": "universe", "owner": "create-scenario --revise",
  "change_kind": "alias_replaces_token_in_correction",
  "original_placement": "Arthur's Chase records mail of 2026-02-13 names JPMorgan and account ending 3203 (SQL lines 65 to 73)",
  "proposed_change": "The mail states the amount, the month, SVB to our Chase account and Carta's renewal, without the payee name or the account ending; subject, sender, date and Leonard's reply stay.",
  "affected_outcomes": ["R9", "R10", "R34", "R70", "R25", "R58"],
  "scope_difference": {"reason_class": "difficulty", "rows_added": 0, "rows_removed": 0, "items_added": 0, "writes_added": 0},
  "fair_discovery_path": "The method doc names Chase and says a transfer between own accounts is not spending; the mail is addressed to Robert, one day old, subject Chase records; a search on Chase, on the amount with the month, or a look at recent mail reaches it.",
  "required_reruns": ["scenario", "injection", "prompt-check", "precheck", "oe-writing", "oe-check", "rubric-check", "baseline", "verifier", "allfail", "difficulty"],
  "reason": "Four runs joined the mail on a token from the issue in one search. Behind an alias the join needs the bank's two names or the amount and month. Catch rate unmeasured; the stronger form (a confident wrong note) risks a new dominant pattern.",
  "evidence": ref("review/repairs.md", "review/rates_and_gates.md")},
]

request = {
 "precheck": False,
 "data_path": REV + "matrix.json",
 "verifier": "10_Baseline_Verifier_Results.md",
 "trajectories": [EXPORT[n] for n in range(1, 7)],
 "task_id": "6abcd0ca93b21819205e962481f3357a788ef9ee657375c805c11234f97a4a7e",
 "revision": "rev7",
 "bundle_hash": tl.binding_bundle_hash(ROOT, ROOT / "09_Rubrics.json", stage="baseline"),
 "receipt": REV + "verifier_binding.json",
 "diagnoses": diagnoses,
 "repairs": repairs,
}
(ROOT / "Working_Files/mode_b_request.json").write_text(json.dumps(request, indent=1, ensure_ascii=False) + "\n")
print("wrote Working_Files/mode_b_request.json:", len(diagnoses), "diagnoses,", len(repairs), "repairs; bundle", request["bundle_hash"][:12])
