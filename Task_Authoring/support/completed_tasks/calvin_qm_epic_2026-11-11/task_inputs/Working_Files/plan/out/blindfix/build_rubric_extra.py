#!/usr/bin/env python3
"""Regenerate plan/rubric_plan_extra.json (spot-check groups and gradable-surface coverage) from the fact ids of rubric_rows.py."""
import importlib.util, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rubric_rows", os.path.join(HERE, "rubric_rows.py")); RR = importlib.util.module_from_spec(spec); spec.loader.exec_module(RR)
PN = RR.PN
def P(*facts): return ", ".join(PN[f] for f in facts)
def res(s): return re.sub(r"@@P:(.+?)@@", lambda m: PN[m.group(1)], s)
groups = [
 {"g": "G1", "items": "The ten children's state (template-identical creations; created in the run, so there are no prior keys)", "samples": f"{P('child_state:Zombie Lane')} Zombie Lane (edge: reads as Clear), {P('child_state:Boss Arena')} Boss Arena (edge: reads as Clear if the chat ok counts), {P('child_state:Tutorials')} Tutorials (ordinary)", "volume": P("child_count"), "core": "no — one state field on template-identical creations; every area's open count has its own row"},
 {"g": "G1b", "items": "The ten children's assignee (one template field)", "samples": f"{P('child_assignee:Tutorials')} Tutorials", "volume": P("child_count"), "core": "no — one template field of template-identical creations"},
 {"g": "G2a", "items": "The 17 new sub-issues' parent (one template field; created in the run)", "samples": f"{P('new_parent:3')} report 3 (ordinary), {P('new_parent:39')} Marcus's report (edge: no Area cell)", "volume": P("new_count") + " (states the template)", "core": "no — one template field; every sub-issue's state has its own row"},
 {"g": "G2b", "items": "The 17 new sub-issues' priority (one template field)", "samples": f"{P('new_priority:22')} report 22", "volume": P("new_count"), "core": "no — one template field of template-identical creations"},
 {"g": "G2c", "items": "The 17 new sub-issues' assignee (one template field)", "samples": f"{P('new_assignee:26')} report 26", "volume": P("new_count"), "core": "no — one template field of template-identical creations"},
 {"g": "G3", "items": "Existing tickets moved under a child, 22: " + " ".join(f"`ZOM-{k}`" for k in list(range(567, 587)) + [556, 560]), "samples": f"{P('move:11')} ZOM-556 (edge: not named in the sheet), {P('move:20')} ZOM-560 (edge: same), {P('move:4')} ZOM-567 (ordinary), {P('move:17')} ZOM-585, {P('move:24')} ZOM-586 (the two filed last)", "volume": P("moved_count") + " and the state-change count " + P("state_change_count"), "core": "no — repetitive moves of equal importance; every ticket's state and note has its own row"},
 {"g": "G4", "items": "Reports-tab Status cells, 39 (one per report fact of the ledger)", "samples": ", ".join(f"{P('sheet_status:%d' % n)} report {n}" for n in (1, 9, 38, 39, 3)) + " (four edges and one ordinary; all reports with no existing ticket, so no status is graded three times)", "volume": P("sheet_rows"), "core": "no — each Status cell repeats its report's decision, which the report's own Linear state row grades"},
 {"g": "G5", "items": "Reports-tab Ticket cells, 39", "samples": f"{P('sheet_ticket:11')} report 11 (edge: ZOM-556), {P('sheet_ticket:4')} report 4 (ordinary)", "volume": P("sheet_rows"), "core": "no — each Ticket cell repeats the key of its report's ticket"},
 {"g": "G6", "items": "Reports-tab Review list cells, 39", "samples": f"{P('sheet_review:17')} report 17 (edge: reads as passed), {P('sheet_review:6')} report 6 (edge: its area is only on the changed agenda), {P('sheet_review:36')} report 36 (ordinary)", "volume": P("review_marked:Level-end rewards") + ", " + P("review_marked:Collect & Win") + " (one count per agenda area)", "core": "no — a yes/no mark per row under one rule; each agenda area's count is graded on its own row"},
 {"g": "G7", "items": "Reports-tab Why cells, 39", "samples": f"{P('sheet_why:9')} report 9 (edge: a later record), {P('sheet_why:4')} report 4 (ordinary)", "volume": P("sheet_rows"), "core": "no — free-text reasons, one per row; the Why column itself is graded by the header row " + P("sheet_cols_reports")},
 {"g": "G9", "items": "The 22 notes' reason (the why; one free-text field per note)", "samples": f"{P('note_why:17')} ZOM-585, {P('note_why:24')} ZOM-586, {P('note_why:12')} ZOM-571, {P('note_why:6')} ZOM-568 (four edges), {P('note_why:34')} ZOM-582 (ordinary)", "volume": P("moved_count"), "core": "no — free-text reasons; every note's status has its own row"},
 {"g": "G10", "items": "Reports-tab Area cells, 39", "samples": f"{P('sheet_area:39')} Marcus's report (edge: no Area cell to copy), {P('sheet_area:9')} report 9 (ordinary)", "volume": P("sheet_rows"), "core": "no — the area is copied from Vincent's sheet for 38 of 39 rows"},
 {"g": "G8", "items": "Areas-tab Status cells, 10", "samples": f"{P('area_status:Zombie Lane')} Zombie Lane, {P('area_status:Boss Arena')} Boss Arena (the two areas that read as Clear from the sheet)", "volume": P("area_rows"), "core": "no — every area is Open; each area's open count has its own row"},
]
S = {}
def cov(sid, fact, dec, facts): S[sid] = {"fact": fact, "dec": dec, "cov": P(*facts), "disp": "—"}
for sid, key, dec in (("V1", "passed", "T1, T5, T6"), ("V2", "qa", "T1, T2, T3"), ("V3", "fix", "T2, T3, T5, T6, T11"), ("V4", "review", "T6, T9"), ("V5", "clear", "T6")): cov(sid, "count:" + key, dec, ["dm:" + key, "slide:" + key])
cov("V7", "area_open_count:Season Pass", "T11", ["area_open_count:Season Pass"])
cov("B1", "status:1", "T1", ["state:1", "sheet_status:1"]); cov("B2", "status:2", "T1", ["state:2"]); cov("B3", "status:25", "T1", ["state:25"]); cov("B4", "status:1", "T1", ["state:1"]); cov("B5", "area_open:Boss Arena", "T1", ["area_status:Boss Arena", "child_state:Boss Arena"])
cov("R1", "status:9", "T5", ["state:9", "sheet_status:9"]); cov("R2", "status:9", "T5", ["state:9"]); cov("R3", "sheet_why:9", "T5", ["sheet_why:9"])
cov("R4", "status:17", "T6", ["state:17", "note:17"]); cov("R5", "status:17", "T6", ["state:17", "state_change_count"]); cov("R6", "sheet_review:17", "T6", ["sheet_review:17"])
cov("K4B", "status:24", "T6", ["note:24", "note_why:24"]); cov("K5B", "area_open:Zombie Lane", "T6", ["child_state:Zombie Lane"])
cov("K1B", "status:29", "T5", ["state:29"]); cov("K2B", "status:29", "T5", ["state:29"]); cov("K3B", "area_open_count:Endless Mode", "T5", ["area_open_count:Endless Mode"])
cov("I1", "status:12", "T2", ["state:12", "note:12"]); cov("I2", "status:12", "T2", ["state:12"]); cov("I3", "status:12", "T2", ["note:12"]); cov("I4", "status:32", "T2", ["state:32", "note:32"]); cov("I5", "status:32", "T2", ["state:32"]); cov("I6", "status:15", "T2", ["state:15", "note:15"]); cov("I7", "status:15", "T2", ["state:15"])
cov("E1", "status:13", "T3", ["state:13", "note:13"]); cov("E2", "status:38", "T3", ["state:38", "sheet_status:38"]); cov("E3", "status:13", "T3", ["note:13"]); cov("E4", "status:13", "T3", ["state:13"]); cov("E5", "status:14", "T3", ["state:14", "note:14"]); cov("E6", "status:37", "T3", ["state:37", "note:37"])
cov("E7", "status:6", "T4", ["state:6", "note:6"]); cov("E9", "status:6", "T4", ["state:6"])
cov("F1", "status:39", "T11", ["sheet_status:39", "sheet_rows"]); cov("F2", "status:39", "T11", ["state:39"]); cov("F3", "new_parent:39", "T11", ["new_parent:39"])
cov("A1", "sheet_ticket:11", "T10", ["sheet_ticket:11"]); cov("A2", "move:20", "T10", ["move:20"]); cov("A3", "status:11", "T10", ["note:11"])
S["G1"] = {"fact": "sheet_review:10", "dec": "T9", "cov": "—", "disp": f"sampled out: a row graded as 'not marked' is an absence row (gate 7); the agenda change is graded on its positive side by report 6's mark ({P('sheet_review:6')}), a Level-end rewards row that only the changed card 68daad83bacf52c6ea7e1593 puts on the list"}
cov("G2", "sheet_review:6", "T9", ["sheet_review:6", "review_marked:Level-end rewards"])
for sid, n in (("K1", 16), ("K2", 21), ("K3", 30), ("K4", 34), ("K14", 27), ("K5", 28), ("K6", 5), ("K7", 33), ("K8", 18), ("K11", 5)): cov(sid, f"status:{n}", {34: "T8", 18: "T8", 27: "T7"}.get(n, "—"), [f"state:{n}" if f"state:{n}" in PN else f"note:{n}"])
cov("K9", "area_open:Zombie Lane", "T6", ["area_status:Zombie Lane"]); cov("K10", "child_count", "—", ["child_count"]); cov("K12", "moved_count", "—", ["moved_count"]); cov("K13", "sheet_ticket:4", "—", ["sheet_ticket:4"])
cov("D1", "sheet_folder", "—", ["sheet_folder"]); cov("D2", "share:leonard.hayes", "—", ["share:leonard.hayes"]); cov("D3", "dm_place", "—", ["dm_place"]); cov("D4", "count:review", "T6, T9", ["slide:review"])
SURF = json.load(open(os.path.join(os.path.dirname(HERE), "01_Gradable_Surface.json")))["slots"]
assert {s["id"] for s in SURF} == set(S), {s["id"] for s in SURF} ^ set(S)
ok_src = os.path.join(HERE, "shortcut_ok.txt")
sok = [res(x) for x in open(ok_src).read().splitlines() if x.strip()] if os.path.exists(ok_src) else []
json.dump({"groups": groups, "surface": {s["id"]: S[s["id"]] for s in SURF}, "surface_covered": sum(1 for v in S.values() if v["cov"] != "—"), "shortcut_ok": sok}, open(os.path.join(HERE, "rubric_plan_extra.json"), "w"), indent=1, ensure_ascii=False)
print("groups", len(groups), "surface covered", sum(1 for v in S.values() if v["cov"] != "—"), "of", len(SURF), "shortcut_ok", len(sok))
