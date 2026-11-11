#!/usr/bin/env python3
"""Writes the pre-scenario sketch (sketch_manifest.json, sketch_surface.json) for hardness_v2_check.py and the policy model.
Not the /create-scenario manifest or surface. Ids prefixed NEW- are planned seeds, not yet checked against the whole universe."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
def vr(service, id_, container, at, seeded=False):
    return {"service": service, "id": id_, "container": container, "seeded": seeded, "at": at}
AD = "C04UEQVDVB7"
traps = [
 {"id": "T_RET", "family": "done_gap", "mechanism": "A24", "services": ["gmail", "slack"], "requirement": "R2",
  "expected_wrong_reading": "SVB's Payment Processed notice of Apr 3, 2024 means $4,032 went to the contractor, so the payee's total is $41,088",
  "resolver": "Leonard's #admin_foundersonly note of Apr 12, 2024: the wire went to a wrong account and the bank returned the money; the payee's recipient record changed on Apr 5 and the payment was re-sent",
  "version_records": [vr("gmail", "threads/00004088.json", "gmail:00004088", "2024-04-03T03:32:00Z"),
                      vr("slack", f"{AD}/1712901800.684259", f"slack:{AD}/1712901800.684259", "2024-04-12T06:03:20Z")]},
 {"id": "T_OFF", "family": "exact_predicate", "mechanism": "A17", "services": ["gmail", "slack"], "requirement": "R3",
  "expected_wrong_reading": "The bank notices hold every payment to the mini-game developer, so he cost $6,450",
  "resolver": "Five Western Union receipts in Robert's mailbox (May-Aug 2024, $7,525) paid on the company card, tied to him by the #admin_foundersonly thread; the method brings in contractors paid that way",
  "version_records": []},
 {"id": "T_ORPH", "family": "cross_reference_gap", "mechanism": "A13", "services": ["gmail", "slack"], "requirement": "R3",
  "expected_wrong_reading": "Leapblock's total is the 29 Processed notices, $374,654; the Sep 2023 $33,290 never left because it has no Processed notice",
  "resolver": "NEW Leapblock's closing statement in #leapblock lists every receipt including the Sep 2023 $33,290; Arthur's base 'Done!' (Sep 2023) agrees",
  "version_records": [vr("gmail", "threads/00001577.json", "gmail:00001577", "2023-09-13T17:00:00Z"),
                      vr("slack", "C05URGU759U/NEW-leapblock-statement", "slack:C05URGU759U/NEW-leapblock-statement", "2026-02-13T08:40:00Z", True)]},
 {"id": "T_CORR", "family": "superseding", "mechanism": "A11", "services": ["gmail", "linear"], "requirement": "R4",
  "expected_wrong_reading": "The $4,000 to the JPMorgan account in Aug 2024 is a Domino Delights cost like every other wire of that month",
  "resolver": "NEW Arthur's mail to the founders about closing Chase: the Aug 2024 wire topped up the company's own Chase account for Carta, so it is a transfer, not a cost",
  "version_records": [vr("linear", "NEW-issue-jpmorgan", "linear:NEW-issue-jpmorgan", "2026-02-12T23:30:00Z", True),
                      vr("gmail", "NEW-arthur-chase-mail", "gmail:NEW-arthur-chase-mail", "2026-02-13T03:10:00Z", True)]},
 {"id": "T_ALIAS", "family": "scope_alias", "mechanism": "A7", "services": ["gmail", "slack"], "requirement": "R3",
  "expected_wrong_reading": "The $16,428.57 LLC on the Jan 2, 2025 wire and BANCO DE AMERICA are build vendors of unknown kind",
  "resolver": "Node Media's own mail gives the exact monthly amounts behind $16,428.57 (a UA agency, so outside build cost); Arthur's #admin_foundersonly note ties the BANCO payments to MotMot",
  "version_records": []},
 {"id": "T_OVR", "family": "authority", "mechanism": "A15", "services": ["slack", "gmail"], "requirement": "R5",
  "expected_wrong_reading": "Payments from Oct 2025 to Jan 2026 follow the calendar, so the Telegram contractor's $1,500 lands in Zombie Match and Combo Fighter",
  "resolver": "The method's sentence on work tied to one game, plus #executives Oct 2025: the contract is the Domino Delights Telegram port",
  "version_records": []},
 {"id": "T_CURR", "family": "unit_or_timezone", "mechanism": "A10", "services": ["gmail", "gsheets"], "requirement": "R6",
  "expected_wrong_reading": "Oct 30, 2025 Martin payment reads as $1,999 of build cost",
  "resolver": "The notice is in BGN; #admin_foundersonly says it reimbursed a laptop; the P&L costs tab carries the USD equipment line",
  "version_records": []},
]
portfolio = [
 {"id": "RET", "mechanism": "A24", "prior_family": "done_gap", "prior_family_reason": "bank 'processed' is the done source; the returned wire is the missing piece in another service", "nodes": ["T_RET"], "requirement": "R2", "natural_reading": "every Processed notice is money that stayed out"},
 {"id": "OFF", "mechanism": "A17", "prior_family": "exact_predicate", "prior_family_reason": "in-scope payments outside the obvious bank-notice search", "nodes": ["T_OFF"], "requirement": "R3", "natural_reading": "the bank notices are the whole population"},
 {"id": "ORPH", "mechanism": "A13", "prior_family": "superseding", "prior_family_reason": "a real payment the notice trail lost; a rarely-opened statement settles it", "nodes": ["T_ORPH"], "requirement": "R3b", "natural_reading": "no Processed notice means no payment"},
 {"id": "CORR", "mechanism": "A11", "prior_family": "superseding", "prior_family_reason": "a dated correction in another service changes one input", "nodes": ["T_CORR"], "requirement": "R4", "natural_reading": "every wire is a cost"},
 {"id": "ALIAS", "mechanism": "A7", "prior_family": "exact_predicate", "prior_family_reason": "payee names on the bank differ from the names in the records", "nodes": ["T_ALIAS"], "requirement": "R3c", "natural_reading": "the bank's payee name tells you what the payee is"},
 {"id": "OVR", "mechanism": "A15", "prior_family": "exact_predicate", "prior_family_reason": "an exception in records overrides the calendar", "nodes": ["T_OVR"], "requirement": "R5", "natural_reading": "the payment date decides the game"},
 {"id": "CURR", "mechanism": "A10", "prior_family": "exact_predicate", "prior_family_reason": "unit on one notice changes a line", "nodes": ["T_CURR"], "requirement": "R6", "natural_reading": "every notice is USD and every person paid is build cost"},
]
manifest = {"_note": "PRE-SCENARIO SKETCH for hardness_v2_check.py only (recommended storyline A: the seed, bet by bet). Not the /create-scenario draft manifest. NEW- ids are planned seeds.",
 "effective_profile": "extreme", "horizon": "Long Horizon",
 "anchors": [{"id": "AN1", "locator": "slack:C0ADGSZKR3R/NEW-leonard-angel-ask", "prompt_reference": "Leonard's ask in #winddown"},
             {"id": "AN2", "locator": "linear:NEW-payee-project", "prompt_reference": "the payee project in Linear"}],
 "ask_fragments": [{"id": "F1", "seeded_ids": ["NEW-leonard-angel-ask"], "delegated_by_record": "NEW-leonard-angel-ask", "requirement_ids": ["R1", "R2", "R3", "R4", "R5", "R6"]},
                   {"id": "F2", "seeded_ids": ["NEW-method-doc"], "delegated_by_record": "NEW-leonard-angel-ask", "requirement_ids": ["R1", "R2", "R3", "R5", "R6"]},
                   {"id": "F3", "seeded_ids": ["NEW-issue-jpmorgan"], "delegated_by_record": "NEW-payee-project", "requirement_ids": ["R4"]}],
 "traps": traps, "mechanism_portfolio": portfolio}
S = []
def slot(id_, w, cls, mech, note, role="core", group=None):
    S.append({"id": id_, "weight": w, "class": cls, "mechanisms": mech, "role": role, "group": group, "note": note})
# exceptions an authority singles out
slot("X1_motmot_net", 5, "direct", ["RET"], "MotMot paid $37,056 net, not $41,088", "exception")
slot("X2_motmot_named", 3, "direct", ["ALIAS"], "BANCO DE AMERICA is MotMot", "exception")
slot("X3_lucas_total", 5, "direct", ["OFF"], "Lucas cost $13,975 with the card-paid transfers", "exception")
slot("X4_leapblock_total", 5, "direct", ["ORPH"], "Leapblock received $407,944", "exception")
slot("X5_jpm_not_cost", 5, "direct", ["CORR"], "Aug 2024 $4,000 is a transfer, left out of cost", "exception")
slot("X6_node_identified", 5, "direct", ["ALIAS"], "The $16,428.57 LLC is Node Media, a UA agency, outside build cost", "exception")
slot("X7_playable_out", 3, "direct", ["ALIAS"], "Creative X ($3,750) is ad creative, outside build cost", "exception")
slot("X8_telegram_dd", 5, "direct", ["OVR"], "Telegram contractor's $1,500 sits in Domino Delights", "exception")
slot("X9_laptop", 3, "direct", ["CURR"], "Martin's payment is a BGN laptop reimbursement, about $1,209.89, a company line", "exception")
# bet totals
slot("B1_dd_build", 5, "aggregate", ["RET", "OFF", "ORPH", "CORR", "ALIAS"], "Domino Delights build cost")
slot("B2_zm_build", 5, "aggregate", ["OVR", "ALIAS", "CURR"], "Zombie Match build cost")
slot("B3_cf_build", 5, "aggregate", ["OVR"], "Combo Fighter build cost")
slot("B4_company_line", 3, "aggregate", ["CURR", "CORR"], "Company line (not a bet)")
# revenue and return
slot("V1_dd_revenue", 3, "direct", [], "Domino Delights lifetime revenue, warehouse")
slot("V2_zm_revenue", 3, "direct", [], "Zombie Match lifetime revenue, warehouse")
slot("V3_cf_revenue", 3, "direct", [], "Combo Fighter lifetime revenue, warehouse")
slot("V4_return_line", 3, "write_content", [], "Lifetime revenue as a share of build cost by bet, within tolerance")
# routine payees: <= 5 samples + one volume row
for i, (n, w) in enumerate([("Deel both spellings $1,015,347.19", 3), ("Eveline Art $93,171.50", 3), ("Graham Porter $5,000", 1), ("Trademark lawyer $7,175", 3), ("Adjoe outside build", 3)], 1):
    slot(f"S{i}_payee", w, "direct", [], n, "sample", "payees")
slot("S6_payee_rows", 1, "aggregate", [], "Output volume: one row per real payee", "volume", "payees")
# follow-through writes (comment differs per target: one row each)
slot("C1_comment_motmot", 3, "write_content", ["RET"], "Comment on the payee's issue saying why the figure differs", "core")
slot("C2_comment_lucas", 3, "write_content", ["OFF"], "Comment on the issue: the card-paid transfers", "core")
slot("C3_comment_leapblock", 3, "write_content", ["ORPH"], "Comment on the issue: the Sep 2023 wire", "core")
slot("C4_comment_jpm", 3, "write_content", ["CORR"], "Comment on the issue: a transfer, not a cost", "core")
# template-identical closes: <= 5 samples + volume
for i in range(1, 6):
    slot(f"L{i}_closed", 1, "delivery", [], "A sampled payee issue is closed", "sample", "closes")
slot("L6_closed_count", 1, "delivery", [], "Every payee issue closed", "volume", "closes")
# delivery
slot("D1_sheet_home", 1, "delivery", [], "Sheet in Robert's Drive")
slot("D2_share_leonard", 1, "delivery", [], "Shared with Leonard")
slot("D3_share_arthur", 1, "delivery", [], "Shared with Arthur")
slot("D4_reply_thread", 1, "delivery", [], "Reply in Leonard's thread with the link")
slot("D5_reply_lines", 3, "write_content", ["RET", "ORPH"], "Reply gives the build cost of the largest bet and its share")
json.dump(manifest, open(os.path.join(H, "sketch_manifest.json"), "w"), indent=1)
json.dump({"_note": "PRE-SCENARIO SKETCH, not the gradable surface", "slots": S}, open(os.path.join(H, "sketch_surface.json"), "w"), indent=1)
print(len(S), sum(s["weight"] for s in S), sum(s["weight"] for s in S if s["mechanisms"]))
