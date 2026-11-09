#!/usr/bin/env python3
"""Pre-scenario sketch for hardness_v2_check.py and the policy model (recommended storyline: the stockholder close-out).
Not the /create-scenario manifest or surface. Ids prefixed NEW- are planned seeds, not yet checked against the whole universe.
Writes three row shapes: sampled, row-per-write (the planning shape: /rubric has asked for it on every task that tested it) and heavy."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
def vr(service, id_, container, at, seeded=False):
    return {"service": service, "id": id_, "container": container, "seeded": seeded, "at": at}
WD, DMR, DMS = "C0ADGSZKR3R", "D04UP2L3E3S", "D04UC0UEN2V"
traps = [
 {"id": "T_OPT", "family": "done_gap", "mechanism": "A24", "services": ["gdocs", "gmail"], "requirement": "R2",
  "expected_wrong_reading": "Options outstanding are the 268,772 on the January term sheet, or the grant sizes on the owner list",
  "resolver": "Carta's per-holder termination notices (Feb 12 and earlier): vested amounts, exercised 0, last day to exercise; six awards have lapsed",
  "version_records": [vr("gdocs", "f_11040fe5d66821bd6951aa", "file:f_11040fe5d66821bd6951aa", "2026-01-23T00:00:00Z"),
                      vr("gmail", "1856960478782792748", "gmail:1856960478782792748", "2026-02-12T22:31:54Z")]},
 {"id": "T_ADV", "family": "exact_predicate", "mechanism": "A17", "services": ["gmail", "gdocs"], "requirement": "R3",
  "expected_wrong_reading": "The owner list's 86,470, 81,383 and 31,536 lines are stock; the Carta termination notices are every option holder",
  "resolver": "The Due Diligence Disclosures advisor table: four angels also hold advisor options, on no termination notice; subtracting them is the only way the lines tie to 3,051,879",
  "version_records": []},
 {"id": "T_TOLD", "family": "completion_elsewhere", "mechanism": "A25", "services": ["slack", "gmail"], "requirement": "R4",
  "expected_wrong_reading": "Leonard's Feb 12 list says the angels are still to do, so every angel gets a first notice",
  "resolver": "Leonard's Feb 9 DM to Segerstrale, and NEW a founder's DM that one more holder already heard on a call",
  "version_records": [vr("slack", f"{WD}/1770934638.035469", f"slack:{WD}/1770934638.035469", "2026-02-12T22:17:18Z"),
                      vr("slack", f"{DMR}/NEW-robert-told", f"slack:{DMR}/NEW-robert-told", "2026-02-13T03:40:00Z", True)]},
 {"id": "T_SIDE", "family": "authority", "mechanism": "A15", "services": ["gdocs", "gmail"], "requirement": "R5",
  "expected_wrong_reading": "The side letter in Drive is the Aug 28 draft and binds Tor alone",
  "resolver": "The Aug-Sep 2023 mail chain: a later draft adds Segerstrale as a party and it was signed; notice terms carry a TLAS copy and rule out post",
  "version_records": [vr("gdocs", "f_6201c7027d02997bfb2c84", "file:f_6201c7027d02997bfb2c84", "2023-08-28T00:00:00Z"),
                      vr("gmail", "1777052222643175480", "gmail:1777052222643175480", "2023-09-20T00:00:00Z")]},
 {"id": "T_BOARD", "family": "superseding", "mechanism": "A11", "services": ["gdocs", "gmail"], "requirement": "R6",
  "expected_wrong_reading": "The board still includes Matthew Collins; with Griffin's director gone, Griffin need not sign anything",
  "resolver": "Matthew's May 1 2025 resignation in mail; the charter's protective provision is a stockholder vote that survives the director's resignation",
  "version_records": [vr("gdocs", "f_966445655f653d26dc8537", "file:f_966445655f653d26dc8537", "2023-06-21T00:00:00Z"),
                      vr("gmail", "1830959847543474636", "gmail:1830959847543474636", "2025-05-01T22:42:49Z")]},
 {"id": "T_ALIAS", "family": "scope_alias", "mechanism": "A7", "services": ["gmail", "slack"], "requirement": "R3b",
  "expected_wrong_reading": "The Disli family is one $75,000 holder; 'Patrick' is one person",
  "resolver": "Three individual holders at $25,000 ('they are holding shares individually'); the owner list and the wires separate the two Patricks",
  "version_records": []},
 {"id": "T_ASOF", "family": "effective_date", "mechanism": "A16", "services": ["gmail", "gdocs"], "requirement": "R8",
  "expected_wrong_reading": "The confirmation for Griffin's auditors uses today's holdings, or the 268,772 on the term sheet",
  "resolver": "NEW KPMG's FY25 request fixes an as-of date; Carta terminations entered in February carry earlier effective dates, so the option count and Griffin's fully diluted share at that date differ from both",
  "version_records": []},
 {"id": "T_FAM", "family": "entity_collision", "mechanism": "A8", "services": ["gmail", "slack"], "requirement": "R3c",
  "expected_wrong_reading": "Three record holders means three separate first-contact notes",
  "resolver": "Enes acts for the family in every record (supplies all three addresses, asks about wires for 'me and my brothers'); Eren has no mail at all. Rule not settled in the base: needs a seed",
  "version_records": []},
 {"id": "T_CAP", "family": "tool_surface", "mechanism": "A14", "services": ["gmail", "gdocs"], "requirement": "R7",
  "expected_wrong_reading": "Tor's counsel needs only the same note as every other holder",
  "resolver": "NEW counsel request deep in an old thread, under the side letter's cap-table-on-request term: a summary goes with Tor's note",
  "version_records": []},
]
def port(id_, mech, fam, why, req):
    return {"id": id_, "mechanism": mech, "prior_family": fam, "prior_family_reason": why, "nodes": ["T_" + id_], "requirement": req}
portfolio = [
 port("OPT", "A24", "done_gap", "the term sheet and owner list read as done; the termination notices show what is actually live", "R2"),
 port("ADV", "A17", "exact_predicate", "in-scope grants sit outside the obvious termination-notice search and inside merged lines", "R3"),
 port("TOLD", "A25", "superseding", "a completion record sits away from the list that says it is still to do", "R4"),
 port("SIDE", "A15", "exact_predicate", "a signed term changes the route for two holders", "R5"),
 port("BOARD", "A11", "superseding", "a resignation in mail overrides the board lists in documents", "R6"),
 port("ASOF", "A16", "exact_predicate", "an as-of date changes the inputs to a fully diluted share", "R8"),
 port("FAM", "A8", "exact_predicate", "one holder acts for two others, which changes three holders' calls", "R3c"),
 port("ALIAS", "A7", "exact_predicate", "holder names differ across mail, Slack and Carta", "R3b"),
 port("CAP", "A14", "exact_predicate", "a request buried in an old thread triggers a term", "R7"),
]
manifest = {"_note": "PRE-SCENARIO SKETCH for hardness_v2_check.py only. Not the /create-scenario draft manifest.",
 "effective_profile": "extreme", "horizon": "Long Horizon",
 "anchors": [{"id": "AN1", "locator": f"slack:{WD}/1770664700.848759", "prompt_reference": "Leonard's investor draft in #winddown"},
             {"id": "AN2", "locator": "linear:NEW-holder-project", "prompt_reference": "the holder project in Linear"}],
 "ask_fragments": [{"id": "F1", "seeded_ids": ["NEW-sunset-notice-list"], "delegated_by_record": "NEW-sunset-notice-list", "requirement_ids": ["R1", "R2", "R3", "R5", "R6"]},
                   {"id": "F2", "seeded_ids": ["NEW-holder-project"], "delegated_by_record": "NEW-sunset-notice-list", "requirement_ids": ["R3b", "R4", "R7"]}],
 "traps": traps, "mechanism_portfolio": portfolio}
def build(shape):
    S = []
    def slot(id_, w, cls, mech, note, role="core", group=None):
        S.append({"id": id_, "weight": w, "class": cls, "mechanisms": mech, "role": role, "group": group, "note": note})
    # holder sheet: stock
    slot("K1_seed_total", 5, "aggregate", ["ADV"], "Series Seed total ties to 3,051,879")
    for k, n in [("K2", "Griffin II 2,662,255"), ("K3", "Griffin Side Fund 84,438")]:
        slot(k, 3, "direct", [], n)
    for k, n in [("K4", "Collins stock 25,432"), ("K5", "Segerstrale stock 50,865"), ("K6", "Nebojsa stock 25,432"), ("K7", "Deepak stock 25,432")]:
        slot(k, 5, "direct", ["ADV"], n + " after taking out advisor options")
    slot("K8_adv_total", 3, "aggregate", ["ADV"], "Advisor options 103,764, four holders")
    for k, n in [("K9", "Enes Disli line"), ("K10", "Haktan Disli line"), ("K11", "Eren Disli line"), ("K12", "Bergmann apart from the Patrick line")]:
        slot(k, 3, "direct", ["ALIAS"], n)
    for i, n in enumerate(["Tor Capital 50,865", "Schaeppi 25,432", "A founder 2,000,000"], 13):
        slot(f"K{i}", 1, "direct", [], n, "sample", "stock")
    slot("K16_vol", 1, "aggregate", [], "Output volume: 15 stock lines", "volume", "stock")
    # holder sheet: options
    slot("P1_live_total", 5, "aggregate", ["OPT", "ADV"], "Live options at the clock 159,706")
    for e in ["ES2", "ES3", "ES5", "ES6", "ES16", "ES17"]:
        slot(f"P_lapsed_{e}", 3, "direct", ["OPT"], f"{e} lapsed")
    for e in ["ES1", "ES4", "ES7", "ES12", "ES13"]:
        slot(f"P_live_{e}", 1, "direct", ["OPT"], f"{e} vested figure and last day", "sample", "live")
    slot("P_live_vol", 1, "aggregate", ["OPT"], "Output volume: 14 option-only lines", "volume", "live")
    slot("P_first", 3, "direct", ["OPT"], "ES-14 closes first, Feb 21")
    # preference and rights
    slot("R1_griffin", 3, "direct", [], "Griffin 90.0 % of preferred")
    slot("R2_25k", 1, "direct", ["ADV"], "A $25K line at 0.83 % of preferred")
    # told and route
    slot("T1_seg", 5, "direct", ["TOLD"], "Segerstrale already told")
    slot("T2_second", 5, "direct", ["TOLD"], "NEW second holder already told")
    slot("T3_griffin", 1, "direct", [], "Griffin told")
    slot("T4_count", 3, "aggregate", ["TOLD"], "Count of holders still to tell")
    slot("T5_fu_seg", 3, "write_content", ["TOLD"], "Segerstrale gets a follow-up, not a first notice")
    slot("T6_fu_second", 3, "write_content", ["TOLD"], "Second told holder gets a follow-up, not a first notice")
    slot("S1_tor_route", 5, "direct", ["SIDE"], "Tor by email or courier, never post")
    slot("S2_tlas", 3, "direct", ["SIDE"], "Copy to TLAS")
    slot("S3_seg_party", 5, "direct", ["SIDE"], "Segerstrale is a party to the side letter")
    slot("S4_seg_route", 3, "write_content", ["SIDE"], "Segerstrale's notice follows the side letter route")
    slot("B1_directors", 5, "direct", ["BOARD"], "Directors at the clock, joined across Slack and mail")
    slot("B2_collins", 3, "write_content", ["BOARD"], "Collins is written to as a holder and advisor, not a director")
    slot("B3_fund1", 3, "direct", ["BOARD"], "Griffin II signs the holder consent")
    slot("B4_fund2", 3, "direct", ["BOARD"], "Side Fund signs the holder consent")
    # letter
    for k, n in [("L1", "Capital raised about $3.0M"), ("L3", "No distribution promised"), ("L4", "Write-off papers come through Sunset"), ("L5", "IP and data disposition")]:
        slot(k, 1, "write_content", [], n)
    slot("L2_pref", 3, "write_content", [], "1x non-participating")
    slot("L6_board", 5, "write_content", ["BOARD"], "Board at the clock")
    slot("L7_consent", 5, "write_content", ["BOARD"], "Griffin's vote as holder is still needed")
    slot("L8_window", 3, "write_content", ["OPT"], "Option paragraph matches the live set")
    slot("G1_draft", 1, "delivery", [], "Consent ask drafted to Griffin")
    slot("G2_vote", 3, "write_content", ["BOARD"], "Ask names the stockholder vote")
    # KPMG confirmation for Griffin's FY25 audit (NEW request on the base pattern)
    slot("A1_opts_asof", 5, "aggregate", ["ASOF"], "Options outstanding at the as-of date")
    slot("A2_fd_asof", 5, "aggregate", ["ASOF"], "Fully diluted count at the as-of date")
    slot("A3_g2_fd", 5, "write_content", ["ASOF"], "Griffin II fully diluted share at the as-of date")
    slot("A4_side_fd", 3, "write_content", ["ASOF"], "Side Fund fully diluted share at the as-of date")
    slot("A5_subsequent", 3, "write_content", ["ASOF"], "Discloses the shutdown as a later event")
    slot("A6_two_funds", 3, "direct", [], "Confirms each fund's shares and cost")
    slot("A7_no_round", 1, "direct", [], "No financing since the seed")
    slot("A8_replyall", 1, "delivery", [], "Reply goes to all recipients on KPMG's mail")
    # one personal note per untold stock holder
    notes = [("Collins", "ADV"), ("Nebojsa", "ADV"), ("Deepak", "ADV"), ("EnesD", "ALIAS"), ("HaktanD", "ALIAS"), ("ErenD", "ALIAS"), ("Bergmann", "ALIAS"), ("Tor", "SIDE")]
    for n, m in notes:
        slot(f"N_{n}", 1, "delivery", [], f"Personal note to {n}")
        slot(f"NC_{n}", 3, "write_content", [m], f"Note states {n}'s own holding")
    slot("N_count", 3, "aggregate", ["TOLD"], "Bare count of personal notes")
    slot("N_tlas", 3, "write_content", ["SIDE"], "Tor's note copies TLAS")
    slot("N_cap1", 3, "write_content", ["CAP"], "Tor's note carries the cap summary")
    slot("N_cap2", 3, "write_content", ["CAP"], "Summary figures match the holder sheet")
    # option-holder notices
    for e in ["ES1", "ES4", "ES7", "ES12", "ES13", "ES14", "ES15", "ES18"]:
        slot(f"O_{e}", 1, "write_content", ["OPT"], f"Notice to {e} with its last day")
    for n in ["Collins", "Segerstrale", "Nebojsa", "Deepak"]:
        slot(f"OA_{n}", 3, "write_content", ["ADV"], f"{n}'s advisor options included")
    # per-holder project
    if shape == "sampled":
        for i in range(1, 6):
            slot(f"LC{i}", 1, "write_content", [], "Sampled holder issue comment", "sample", "lin")
        slot("LC_vol", 1, "aggregate", [], "Output volume: a comment on each holder issue", "volume", "lin")
        for i in range(1, 6):
            slot(f"LS{i}", 1, "delivery", [], "Sampled state move", "sample", "st")
        slot("LS_vol", 1, "aggregate", [], "Output volume: every issue moved", "volume", "st")
    else:
        keyed = {"ES2": "OPT", "ES3": "OPT", "ES5": "OPT", "ES6": "OPT", "ES16": "OPT", "ES17": "OPT", "Seg": "TOLD", "Second": "TOLD", "Tor": "SIDE", "Collins": "ADV", "Neb": "ADV", "Deepak": "ADV"}
        ids = list(keyed) + [f"plain{i}" for i in range(1, 15)]
        for x in ids:
            m = [keyed[x]] if x in keyed else []
            slot(f"LC_{x}", 1, "write_content", m, f"Comment on {x}'s issue")
        if shape == "heavy":
            for x in ids:
                m = [keyed[x]] if x in keyed else []
                slot(f"LS_{x}", 1, "delivery", m, f"State move on {x}'s issue")
        else:
            for i in range(1, 6):
                slot(f"LS{i}", 1, "delivery", [], "Sampled state move", "sample", "st")
            slot("LS_vol", 1, "aggregate", [], "Output volume: every issue moved", "volume", "st")
    # delivery
    for k, n in [("D1", "Letter doc in Leonard's Drive"), ("D2", "Holder sheet in Leonard's Drive"), ("D3", "Shared with Robert"), ("D4", "Shared with Arthur"), ("D5", "Thread reply with both links")]:
        slot(k, 1, "delivery", [], n)
    slot("D6_reply", 3, "write_content", ["TOLD", "OPT"], "Reply gives holders still to tell and the first deadline")
    return S
def variant_h():
    """Hard-leaning variant: drop rows that only dilute, and add a trap that changes three holders' calls.
    No per-option notices (the letter carries the option schedule); a comment only where a holder's answer differs from the owner list;
    Enes acts for the family, so the Disli rows move from ALIAS to FAM."""
    S = [dict(x) for x in build("rowperwrite")]
    S = [x for x in S if not x["id"].startswith("O_") and not x["id"].startswith("LC_plain")]
    for x in S:
        if x["id"] in ("K9", "K10", "K11", "N_EnesD", "N_HaktanD", "N_ErenD", "NC_EnesD", "NC_HaktanD", "NC_ErenD"):
            x["mechanisms"] = ["FAM"]
    S.append({"id": "F1_contact", "weight": 5, "class": "write_content", "mechanisms": ["FAM"], "role": "core", "group": None, "note": "One family contact, joined across mail and Slack"})
    S.append({"id": "F2_count", "weight": 3, "class": "aggregate", "mechanisms": ["FAM"], "role": "core", "group": None, "note": "Note count reflects the family contact"})
    S.append({"id": "F3_comment", "weight": 3, "class": "write_content", "mechanisms": ["FAM"], "role": "core", "group": None, "note": "Comment on the family's issues"})
    return S
S = variant_h()
json.dump({"_note": "PRE-SCENARIO SKETCH, hard-leaning variant H; not the gradable surface", "slots": S}, open(os.path.join(H, "sketch_surface_variantH.json"), "w"), indent=1)
t = sum(s["weight"] for s in S); f = sum(s["weight"] for s in S if s["mechanisms"])
print("variantH", len(S), "rows, weight", t, "flippable", f, f"{f/t:.1%}", "weight-5 rows", sum(1 for s in S if s["weight"] == 5))
json.dump(manifest, open(os.path.join(H, "sketch_manifest.json"), "w"), indent=1)
for shape in ["sampled", "rowperwrite", "heavy"]:
    S = build(shape)
    name = "sketch_surface.json" if shape == "rowperwrite" else f"sketch_surface_{shape}.json"
    json.dump({"_note": f"PRE-SCENARIO SKETCH, shape {shape}; not the gradable surface", "slots": S}, open(os.path.join(H, name), "w"), indent=1)
    t = sum(s["weight"] for s in S); f = sum(s["weight"] for s in S if s["mechanisms"])
    print(shape, len(S), "rows, weight", t, "flippable", f, f"{f/t:.1%}", "weight-5 rows", sum(1 for s in S if s["weight"] == 5))
