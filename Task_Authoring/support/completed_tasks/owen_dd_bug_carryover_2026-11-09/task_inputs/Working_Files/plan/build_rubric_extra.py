#!/usr/bin/env python3
"""Regenerate plan/rubric_plan_extra.json (spot-check groups and gradable-surface coverage) from the fact ids of rubric_rows.py,
so the P numbers follow the rows. Keeps the 'diversity' and 'shortcut_ok' entries already in the file (shortcut_ok P numbers are
written as @@P:<fact>@@ tokens in plan/shortcut_ok.txt and resolved here)."""
import importlib.util
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rubric_rows", os.path.join(HERE, "rubric_rows.py"))
RR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RR)
PN = RR.PN
EX = os.path.join(HERE, "rubric_plan_extra.json")
old = json.load(open(EX))


def P(*facts):
    return ", ".join(PN[f] for f in facts)


def res(s):
    return re.sub(r"@@P:(.+?)@@", lambda m: PN[m.group(1)], s)


TICKF = [r["fact"] for r in RR.R if r["fact"].startswith("state:") and r["final"] == "that issue is in Done"]
BUGSF = [r["fact"] for r in RR.R if r["fact"].startswith("state:") and r["final"] == "that issue is in Bugs"]
LINEF = [r["fact"] for r in RR.R if r["fact"].startswith("line:")]
assert len(TICKF) == 58 and len(BUGSF) == 7 and len(LINEF) == 28, (len(TICKF), len(BUGSF), len(LINEF))
RUB1 = "/rubric round 1 (run_forensics/rev9/3_rubric_FAIL1_r1.md)"

groups = []
for g, field, fact, edge in (("G1a", "the [2231] title prefix", "prefix:In profile", "an ordinary ticked line"),
                             ("G1b", "the title text (the line or the post's first line, as written)", "titletext:flickering", "a post"),
                             ("G1c", "the Engineering team", "team:music", "a post"),
                             ("G1d", "the Bug label", "label:bar", "a post split over two messages"),
                             ("G1e", "the parent ENG-2401", "parent:mega", "a post that opens with a mention"),
                             ("G1f", "no assignee", "assignee:top hud", "the shortest line"),
                             ("G1g", "an empty description", "desc:In chapter selection", "a line continued on the next one")):
    groups.append({"g": g, "items": f"The 68 new issues' template field: {field} (one property on one output; the issues are created in the run, so there are no prior keys)",
                   "samples": f"{P(fact)} ({edge})", "volume": P("new_count") + " (states the template)",
                   "core": f"no — one template field of template-identical creations ({RUB1}: each sample its own property group sharing {P('new_count')} as the control); every item's state has its own row"})
groups.append({"g": "G4", "items": "UI children moved to Done, 14: " + " ".join(f"`{k}`" for k in ("ENG-2410", "ENG-2414", "ENG-2415", "ENG-2417", "ENG-2418", "ENG-2419", "ENG-2425", "ENG-2427", "ENG-2429", "ENG-2430", "ENG-2431", "ENG-2432", "ENG-2433", "ENG-2435")),
               "samples": f"{P('move:ENG-2417')} ENG-2417 (ordinary), {P('move:ENG-2418')} ENG-2418, {P('move:ENG-2433')} ENG-2433 (edge: the shop regression is on its screen), {P('move:ENG-2432')} ENG-2432 (edge: same), {P('move:ENG-2410')} ENG-2410 (edge: the shop regression against a Validation-state child)",
               "volume": P("moves_count"), "core": f"no — repetitive moves of equal importance (the one template {RUB1} accepted); the five holds are direct rows ({P('hold:ENG-2434')}–{P('hold:ENG-2437')})"})
groups.append({"g": "G7", "items": "Sheet Outcome cells, 70 (one per bug row of the ledger, F48 to F117)",
               "samples": f"{P('sheet:tavern')} Tavern (edge: a tick overturned), {P('sheet:window')} tile dozer window (edge: an unmerged PR), {P('sheet:lives1')} a lives line (edge: Gone), {P('sheet_outcome:sides')} sides of event icons (ordinary Fixed), {P('sheet_outcome:apple')} Apple sync line (edge: Covered)",
               "volume": P("sheet_rows"), "core": "no — each Outcome cell repeats its item's decision, which the item's own Linear state row grades"})
groups.append({"g": "G8", "items": "Sheet Ticket cells, 70 (one per bug row of the ledger, F48 to F117)",
               "samples": f"{P('sheet_ticket:sides')} sides of event icons (ordinary: the run's own key), {P('sheet:apple')} Apple sync line (edge: Covered, ENG-2073), {P('sheet:signin')} manual sign-in line (edge: Covered, ENG-2363)",
               "volume": P("sheet_rows"), "core": "no — each Ticket cell repeats the key of its item's ticket"})
groups.append({"g": "G9", "items": "Sheet Why cells, 70 (one per bug row of the ledger, F48 to F117)",
               "samples": f"{P('sheet_why:tavern')} Tavern (edge: the later DM over the tick), {P('sheet_why:sides')} sides of event icons (ordinary: the tick stands)",
               "volume": P("sheet_rows"), "core": "no — free-text reasons, one per row; the Why column itself is graded by the header row " + P("sheet_columns")})

S = {}


def cov(sid, fact, dec, facts):
    S[sid] = {"fact": fact, "dec": dec, "cov": P(*facts), "disp": "—"}


def disp(sid, fact, dec, why):
    S[sid] = {"fact": fact, "dec": dec, "cov": "—", "disp": why}


cov("V1", "bugs_count", "T1, T2, T5", BUGSF)
cov("V5", "done_count", "T1, T2", TICKF)
cov("V2", "reply_new", "T3, T4", ["reply_new"])
cov("V3", "reply_broken", "T1, T2, T3", ["reply_broken"])
cov("V4", "reply_done", "T6–T9", ["reply_done"])
cov("I1", "hold:ENG-2434", "T6", ["hold:ENG-2434"])
cov("I2", "hold:ENG-2426", "T6", ["hold:ENG-2426"])
for sid, k in (("I3", "ENG-2434"), ("I4", "ENG-2426")):
    disp(sid, "hold_reason:" + k, "T6", f"not incorporated: {RUB1} ruled the hold's reason is not asked for (R37–R41: Arthur's DM D05S1S2AB5M/1770937805.214409 asks 'saying where it landed'); the hold itself is graded as 'the ticket stays open' ({P('hold:' + k)})")
cov("B1", "sheet:tavern", "T1", ["sheet:tavern"])
cov("B2", "state:tavern", "T1", ["state:tavern"])
disp("B3", "sheet:shop", "T2", f"sampled out: {RUB1} deleted the shop Outcome sample (R49) to keep the Outcome group at five; the shop decision is graded on its Linear state {P('state:shop')} and inside the reply count {P('reply_broken')}")
cov("B4", "state:shop", "T2", ["state:shop"])
cov("G1", "gone:lives1", "T10", ["state:I found the issue lives are not decreased after", "sheet:lives1"])
cov("G2", "gone:lives2", "T10", ["state:Lives are only decreased after losing twice in a"])
cov("G3", "gone:charchange", "T10", ["state:When I change the character it just adds 1"])
cov("G4", "hold:ENG-2424", "T9", ["hold:ENG-2424"])
cov("L1", "window", "T5", ["state:tile dozer window background", "sheet:window"])
disp("L2", "sheet_why:window", "T5", f"sampled: {RUB1} set the Why samples on the Tavern and sides of event icons rows ({P('sheet_why:tavern')}, {P('sheet_why:sides')}); the window decision is graded on {P('state:tile dozer window background')} and {P('sheet:window')} (rubric_sampling: the choice of sample is a note, not a finding)")
cov("E1", "post:flickering", "T13", ["state:flickering"])
cov("E2", "post:music", "T13", ["state:music plays only sometimes"])
cov("E3", "post:acid", "T13", ["state:acid animation delay"])
cov("A1", "apple", "T3", ["sheet:apple"])
cov("A2", "signin", "T4", ["sheet:signin"])
cov("A3", "covered:apple", "T3", ["covered:apple"])
cov("O1", "lines_build", "T12", LINEF)
cov("O2", "line:ENG-2417", "T12", ["line:ENG-2417"])
cov("O3", "line:ENG-2428", "T7", ["line:ENG-2428", "hold:ENG-2428"])
cov("F1", "post:mega", "—", ["state:mega tile missing a face"])
cov("F2", "post:bar", "—", ["state:android bottom bar invisible"])
cov("F3", "post:treasure", "—", ["state:treasure button opens axe arena"])
for sid, k in (("K1", "offers has no visuals"), ("K2", "Teams addressable doesn t work"), ("K3", "top hud"), ("K4", "Streak Fever has overflowing text on its pop up"), ("K5", "Win & Collect gives a null ref every time")):
    cov(sid, "state:" + k, "—", ["state:" + k])
cov("K6", "state:vr_train", "T11", ["state:vr_train"])
cov("K7", "state:vr_team", "T11", ["state:vr_team"])
cov("K8", "state:backend", "T11", ["state:backend"])
cov("K9", "move:ENG-2417", "—", ["move:ENG-2417"])
cov("K10", "move:ENG-2418", "—", ["move:ENG-2418"])
disp("K11", "move:ENG-2425", "—", f"sampled out: {RUB1} swapped the ENG-2425 sample for ENG-2433, the other shop-icon child ({P('move:ENG-2433')}); the move stays under the exact count {P('moves_count')}")
cov("K12", "move:ENG-2432", "—", ["move:ENG-2432"])
cov("K13", "move:ENG-2410", "—", ["move:ENG-2410"])
cov("K15", "team", "—", ["team:music", "new_count"])
cov("K16", "title_prefix", "T13", ["prefix:In profile", "new_count"])
cov("K17", "sheet_ticket_keys", "—", ["sheet_ticket:sides"])
cov("D1", "sheet_folder", "—", ["sheet_folder"])
disp("D2", "reply_link", "—", "not incorporated (gate 3): neither the prompt nor Arthur's DM D05S1S2AB5M/1770937805.214409 asks for a link in the reply; it asks for the numbers")
SURF = json.load(open(os.path.join(os.path.dirname(HERE), "01_Gradable_Surface.json")))["slots"]
assert {s["id"] for s in SURF} == set(S), {s["id"] for s in SURF} ^ set(S)
ok_src = os.path.join(HERE, "shortcut_ok.txt")
sok = [res(x) for x in open(ok_src).read().splitlines() if x.strip()] if os.path.exists(ok_src) else old.get("shortcut_ok", [])
out = {"groups": groups, "surface": {s["id"]: S[s["id"]] for s in SURF}, "surface_covered": sum(1 for v in S.values() if v["cov"] != "—"),
       "diversity": old.get("diversity", "(computed by stage_gate diversity.authority_share)"), "shortcut_ok": sok}
json.dump(out, open(EX, "w"), indent=1, ensure_ascii=False)
print("groups", len(groups), "surface covered", out["surface_covered"], "of", len(SURF), "shortcut_ok", len(sok))
