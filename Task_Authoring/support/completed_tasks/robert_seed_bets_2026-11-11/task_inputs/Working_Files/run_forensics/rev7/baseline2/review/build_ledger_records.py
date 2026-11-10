#!/usr/bin/env python3
"""Write the hand-dispositioned ledger records for the six rev7 baseline runs (batch 2).

node_verdicts proposed BYPASSED for every node in every run because it cannot join the runs' free-text payee labels
to the register. The verdicts below follow the platform verifier rows (10_Baseline_Verifier_Results.md), the per-run
reads (review/run-N.md) and the bank-name register diff (review/register_diff.txt). Event numbers are 0-based
indexes into each bound export.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SQL = "40f90385e31e099d28a10e483f0a94490a34096c87f08c4ca35c97c3f311d37c"
BASE = dict(task="robert_seed_bets_s2", revision="rev7", sql_sha256=SQL, source="platform-baseline",
            harness={"name": "claude-code", "version": "2.1.280"}, epistemic="derived", weight=1.0,
            model="claude-opus-5-5")
BY = ("Claude (Fable 5.2), /create-hardening MODE B baseline, 2026-11-10; one full read per run (review/run-N.md), "
      "every cited quote re-checked against the bound export; verdicts follow the verifier rows and the bank-name "
      "register diff (review/register_diff.txt)")
RULES = {"RET": ("A24", "A24", "MotMot"), "OFF": ("A17", "A17", "Lucas"), "ORPH": ("A13", "A11", "Leapblock"),
         "CORR": ("A11", "A11", "JPMorgan"), "ALIAS": ("A7", "A17", "Node Media"),
         "CLASS": ("A15", "A15", "Lauren Brooks"), "CURR": ("A10", "A15", "Martin Walsh")}
CONTROLS = {"RET": ["Leapblock"], "OFF": ["Graham Porter"], "ORPH": ["Eveline Art"], "CORR": ["Singular"],
            "ALIAS": ["Adjoe", "Leapblock"], "CLASS": ["Graham Porter"], "CURR": ["Lauren Brooks"]}
WRITE = {"run-1": 575, "run-2": 413, "run-3": 346, "run-4": 393, "run-5": 377, "run-6": 678}
ROWS = {"RET": "R7, R32, R68", "OFF": "R8, R33, R69", "ORPH": "R6, R31, R67", "CORR": "R9, R10, R34, R70",
        "ALIAS": "R12", "CLASS": "R13, R20", "CURR": "R14, R15"}
# run -> rule -> (verdict, deciding events, v2 kind, why)
V = {
 "run-1": {
  "RET": ("LANDED", [575, 205], "off_path_correction", "Sheet row at event 575 keeps MotMot Domino Delights 32160 with the note '11 notices.'; truth 28128. The founders' channel C04UEQVDVB7 was never read or searched; the only returns search was Gmail at event 205 (19 ids, none opened). No comment on ENG-2442; reply gives $963,374.64 (event 650)."),
  "OFF": ("LEAKED", [440, 446, 500, 575, 593], "bulk_call_carried", "The wide notice search returned 434 ids; a batch fetched from that list held one Western Union receipt, which the main thread's parser listed at event 440. Named searches followed; five receipts parsed at event 500; 13975 written at 575; comment at 593."),
  "ORPH": ("LEAKED", [401, 402, 575, 591], "on_delegation_path", "Slack search 'received after:2026-01-20' (event 401) returned the close-out post first (402). 337594 written; comment at 591."),
  "CORR": ("LEAKED", [239, 255, 575, 597], "recent_mail_sweep", "The Chase records mail was the first thread of a search for other SVB mail (event 239) and was read at 255. Zero and no bucket written; comment at 597."),
  "ALIAS": ("LEAKED", [519, 524, 575], "token_search_resolves_alias", "Gmail search on the payee token and the amount (event 519) returned the Node Media invoice thread (524). Marketing written."),
  "CLASS": ("FALSE", [67, 575], "same_container", "The ENG-2455 note states the paid UA role on the first read (event 67)."),
  "CURR": ("FALSE", [347, 575], "first_read_bulk_field", "The currency is on the notice in the bulk parse (event 347)."),
 },
 "run-2": {
  "RET": ("LANDED", [413, 295, 300], "off_path_correction", "Sheet row at event 413 keeps MotMot Domino Delights 32160 with the note 'two accounts (3341, 8605)'. No Slack search for returns and no read of C04UEQVDVB7; its notice parse at events 295 and 300 showed the lone 4,032 wire to 8605. No comment on ENG-2442; reply gives $955,849.64 (event 481)."),
  "OFF": ("LANDED", [413, 169, 171, 338], "outside_obvious_filter", "Lucas written at 6450 (event 413). Three Gmail searches naming Lucas or receipt words (events 169, 171, 338) each returned one capped page of bare ids; none was opened and no page token was followed. No comment on ENG-2447."),
  "ORPH": ("LEAKED", [340, 343, 413, 425], "on_delegation_path", "Slack search 'received' after Feb 1 2026 (event 340) returned the close-out post (343). 337594 written; comment at 425."),
  "CORR": ("LEAKED", [154, 164, 413, 427], "token_join", "Gmail search on the account ending 3203 (event 154); the Chase records mail was read at 164. Zero and no bucket written; comment at 427."),
  "ALIAS": ("LEAKED", [365, 372, 413], "token_search_resolves_alias", "Gmail search on the payee token (event 365) returned the Node Media invoice thread (372). Marketing written."),
  "CLASS": ("FALSE", [113, 413], "same_container", "The ENG-2455 note states the paid UA role on the first read (event 113)."),
  "CURR": ("FALSE", [300, 413], "first_read_bulk_field", "The currency is on the notice in the bulk parse (event 300)."),
 },
 "run-3": {
  "RET": ("LEAKED", [257, 259, 346, 374], "one_search_on_rule_words", "Slack search 'wire came back' (event 257) returned Leonard's message alone (259). 28128 written; comment at 374."),
  "OFF": ("LANDED", [346, 153, 171, 276], "outside_obvious_filter", "Lucas written at 6450 with the note 'Sep to Nov 2024.' (event 346). Receipt searches at events 153 and 171 returned capped pages of bare ids, none opened; the one query naming Lucas (276) ANDed receipt words with eleven names. No comment on ENG-2447; reply gives $951,818 (426)."),
  "ORPH": ("LEAKED", [179, 181, 346, 372], "on_delegation_path", "Slack search 'received' after Jan 15 2026 (event 179) returned the close-out post first (181). 337594 written; comment at 372."),
  "CORR": ("LEAKED", [297, 302, 346, 376], "token_join", "Gmail search on 3203 (event 297); the Chase records thread was read at 302. Zero and no bucket written; comment at 376."),
  "ALIAS": ("LEAKED", [289, 292, 346], "token_search_resolves_alias", "Gmail search on the amount and the payee token (event 289) returned the Node Media invoice thread (292). Marketing written."),
  "CLASS": ("FALSE", [133, 346], "same_container", "The ENG-2455 note states the paid UA role on the first read (event 133)."),
  "CURR": ("FALSE", [85, 346], "first_read_bulk_field", "The currency is on the notice in the bulk parse (event 85)."),
 },
 "run-4": {
  "RET": ("LEAKED", [343, 344, 351, 393, 402], "one_search_on_rule_words", "Slack search 'wires' (event 343) returned Leonard's message as the second hit (344); a 'came back' search confirmed it (351). 28128 written; comment at 402."),
  "OFF": ("LANDED", [393, 163, 304, 344], "outside_obvious_filter", "Lucas written at 6450 with the note '3 notices, Sep-Nov 2024' (event 393). Receipt and name searches at events 163 and 304 returned capped pages of bare ids, none opened. The Slack result at 344 held Robert's own line 'Western Union? Or wire?' and the run did not follow it. No comment on ENG-2447; reply gives $951,817.64 (454)."),
  "ORPH": ("LEAKED", [305, 307, 393, 400], "on_delegation_path", "Slack search 'received' after Jan 1 2026 (event 305) returned the close-out post first (307). 337594 written; comment at 400."),
  "CORR": ("LEAKED", [136, 158, 393, 404], "token_join", "Gmail search 'JPMorgan OR Chase 3203' (event 136); the Chase records thread was read at 158. Zero and no bucket written; comment at 404."),
  "ALIAS": ("LEAKED", [327, 337, 393], "token_search_resolves_alias", "Gmail search on the payee token (event 327) returned the Node Media invoice thread (337). Marketing written."),
  "CLASS": ("FALSE", [61, 393], "same_container", "The ENG-2455 note states the paid UA role on the first read (event 61)."),
  "CURR": ("FALSE", [283, 393], "first_read_bulk_field", "The currency is on the notice in the bulk parse (event 283)."),
 },
 "run-5": {
  "RET": ("LEAKED", [265, 267, 277, 377, 386], "one_search_on_rule_words", "Slack search 'wires' (event 265) returned Leonard's message as the second hit (267); the channel read at 277 confirmed it. 28128 written; comment at 386."),
  "OFF": ("LANDED", [377, 267], "outside_obvious_filter", "Lucas written at 6450 with the note 'Matches the notices.' (event 377). No search was aimed at Lucas; the receipt searches were about Oleg. The Slack result at 267 held Robert's own line 'Western Union? Or wire?' and the run did not follow it. No comment on ENG-2447; reply gives $951,818 (438)."),
  "ORPH": ("LEAKED", [256, 257, 377, 384], "on_delegation_path", "Slack search 'received' after Jan 1 2026 (event 256) returned the close-out post first (257). 337594 written; comment at 384."),
  "CORR": ("LEAKED", [224, 240, 377, 390], "token_join", "Gmail search on 3203, chase and JPMorgan (event 224); the Chase records thread was read at 240. Zero and no bucket written; comment at 390."),
  "ALIAS": ("LANDED", [377, 294, 311, 322], "alias_unresolved", "Bucket Company with 16428.57 in the Company column and the note 'so Company' (event 377); truth is Marketing under Domino Delights. The payee token was searched in Linear (294) and Drive (322), never in Gmail or Slack; a Slack search for 'LLC' (311) was capped at its newest 40 hits. No result named Node Media."),
  "CLASS": ("FALSE", [61, 377], "same_container", "The ENG-2455 note states the paid UA role on the first read (event 61)."),
  "CURR": ("FALSE", [130, 377], "first_read_bulk_field", "The currency is on the notice in the bulk parse (event 130)."),
 },
 "run-6": {
  "RET": ("LEAKED", [456, 458, 678, 692], "one_search_on_rule_words", "Slack search for the phrase 'came back' (event 456) returned Leonard's message first (458). 28128 written; comment at 692."),
  "OFF": ("LANDED", [678, 157, 189, 351, 388], "outside_obvious_filter", "Lucas written at 6450 with the note '3 notices, Sep-Nov 2024.' (event 678). Four Gmail searches (events 157, 189, 351, 388) returned first pages of bare ids; no non-notice hit was opened and no page token followed. No comment on ENG-2447; reply gives $951,817.64 (747)."),
  "ORPH": ("LEAKED", [416, 417, 678, 690], "on_delegation_path", "Slack search 'received after:2026-01-25' (event 416) returned the close-out post first (417). 337594 written; comment at 690."),
  "CORR": ("LEAKED", [226, 247, 289, 678, 694], "recent_mail_sweep", "A sweep of mail after Jan 15 2026 (event 226) and a metadata batch (247) showed the Chase records snippet; the thread was read at 289. Zero and no bucket written; comment at 694."),
  "ALIAS": ("LEAKED", [625, 629, 678], "token_search_resolves_alias", "Gmail search on the payee token (event 625) returned the Node Media invoice thread (629). Marketing written."),
  "CLASS": ("FALSE", [67, 678], "same_container", "The ENG-2455 note states the paid UA role on the first read (event 67)."),
  "CURR": ("FALSE", [591, 678], "first_read_bulk_field", "The currency is on the notice in the bulk parse (event 591)."),
 },
}

verdicts, others = [], []
for run, rules in V.items():
    for rule, (verdict, events, kind, why) in rules.items():
        mech, fam, key = RULES[rule]
        verdicts.append(dict(BASE, run=run, kind="verdict", node=rule, mechanism=mech, family=fam, verdict=verdict,
            keys=[key],
            evidence={"producer": "hand (node_verdicts/1 proposed BYPASSED: it cannot join free-text payee labels to the register)",
                      "why": why, "verifier_rows": ROWS[rule],
                      "citations": {"register_write_events": [WRITE[run]], "deciding_events": events, "brief_events": []},
                      "tool_proposal": "BYPASSED (rejected: the row is in the sheet write)"},
            features={"mixed_model": False, "flags": [], "pending_review": [], "control_explained": [],
                      "observed_units": {"controls": 0, "channels": 0}, "deciding_models": ["claude-opus-5-5"],
                      "unknown_decisions": 0, "disposition": "DISPOSED", "disposed_by": BY, "v2_kind": kind,
                      "deciding_event": WRITE[run], "binding": "BOUND rev7 by discriminating content"}))
        for member in CONTROLS[rule]:
            others.append(dict(BASE, run=run, kind="control", node=rule, key=member, mechanism=mech, family=fam,
                verdict="HELD",
                evidence={"producer": "hand (bank-name register diff, review/register_diff.txt)",
                          "deciding_event": WRITE[run], "via": "register write", "briefs": [], "fields": [],
                          "written": {}, "truth": {}, "over_applied_value": None},
                features={"run_model": "claude-opus-5-5", "mixed_model": False, "error": False,
                          "deciding_model_unknown": False, "disposition": "DISPOSED", "disposed_by": BY}))
        failed = verdict == "LANDED"
        member = {"key": key, "deciding_event": WRITE[run], "deciding_model": "claude-opus-5-5", "via": "register write",
                  "briefs": [], "register_writes": [[WRITE[run], "claude-opus-5-5"]]}
        others.append(dict(BASE, run=run, kind="channel", node="CH-" + rule, mechanism="scale", family=fam,
            verdict="FAILED" if failed else "HELD", keys=[key],
            counts={"unit": "member", "n": 1, "failed": int(failed)},
            evidence={"producer": "hand (verifier rows " + ROWS[rule] + ")",
                      "failed_members": [member] if failed else [], "held_members": [] if failed else [member],
                      "failed_slots": [], "covered": {"members": 1, "observed": 1, "unobserved": 0},
                      "deciding_event": WRITE[run], "deciding_run": run, "sql_sha256": SQL},
            features={"run_model": "claude-opus-5-5", "deciding_models": ["claude-opus-5-5"], "unknown_decisions": 0,
                      "deciding_model_unknown": False, "model_is_fallback": False, "preregistered": True,
                      "mixed_model": False, "disposition": "DISPOSED", "disposed_by": BY}))

(HERE / "dispositioned.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in verdicts))
(HERE / "controls_channels.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in others))
print(len(verdicts), "verdict records;", len(others), "control and channel records")
