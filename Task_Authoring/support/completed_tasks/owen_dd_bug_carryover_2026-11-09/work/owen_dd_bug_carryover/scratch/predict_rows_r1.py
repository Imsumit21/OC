import json, statistics, sys, importlib.util
B = "Working_Files/run_forensics/rev9/baseline/"
JS = json.load(open(sys.argv[1]))
W = [c["weight"] for c in JS]
spec = importlib.util.spec_from_file_location("rr", "Working_Files/plan/rubric_rows.py"); RR = importlib.util.module_from_spec(spec); spec.loader.exec_module(RR)
FACTS = [r["fact"] for r in RR.R]
assert len(FACTS) == len(W)
SLOT = {"state:offers has no visuals": "K1", "state:Teams addressable doesn t work": "K2", "state:top hud": "K3", "state:Streak Fever has overflowing text on its pop up": "K4",
        "state:Win & Collect gives a null ref every time": "K5", "state:vr_train": "K6", "state:vr_team": "K7", "state:backend": "K8",
        "state:I found the issue lives are not decreased after": "G1", "state:Lives are only decreased after losing twice in a": "G2", "state:When I change the character it just adds 1": "G3",
        "state:tile dozer window background": "L1", "state:mega tile missing a face": "F1", "state:flickering": "E1", "state:music plays only sometimes": "E2", "state:acid animation delay": "E3",
        "state:treasure button opens axe arena": "F3", "state:android bottom bar invisible": "F2", "covered:apple": "A3", "covered:signin": "A2",
        "move:ENG-2417": "K9", "move:ENG-2418": "K10", "move:ENG-2432": "K12", "move:ENG-2410": "K13", "hold:ENG-2434": "I1", "hold:ENG-2426": "I2", "hold:ENG-2424": "G4",
        "sheet_folder": "D1", "sheet_ticket:sides": "K17", "sheet:tavern": "B1", "sheet:apple": "A1", "sheet:signin": "A2", "sheet:window": "L1", "sheet:lives1": "G1",
        "sheet_outcome:apple": "A1", "sheet_why:tavern": "B1", "reply_broken": "V3", "reply_new": "V2", "reply_done": "V4", "prefix:In profile": "K16", "team:music": "K15"}
KEYFOR = {"state:tavern": "Tavern buttons lost its frame", "state:shop": "shops from rivertile and memory tile has weird shop", "move:ENG-2433": "ENG-2433",
          "hold:ENG-2428": "ENG-2428", "hold:ENG-2437": "ENG-2437"}
def rows(r):
    S, wrong = r["slots"], set(r["wrong"])
    ok = lambda k: k not in wrong
    out = []
    for f in FACTS:
        if f == "new_count": v = S["A1"] and S["A2"]
        elif f == "moves_count": v = all(ok(k) for k in ("ENG-2434", "ENG-2426", "ENG-2424", "ENG-2428", "ENG-2437", "ENG-2417", "ENG-2418", "ENG-2425", "ENG-2432", "ENG-2410", "ENG-2433"))
        elif f in SLOT: v = S[SLOT[f]]
        elif f in KEYFOR: v = ok(KEYFOR[f])
        elif f.startswith("state:"): v = ok(f[6:])
        elif f.startswith("line:"): v = S["O1"]
        else: v = True
        out.append(bool(v))
    return out
for f in ("grade_07_Baseline_Trajectories.json", "grade_baseline2.json"):
    R = json.load(open(B + f)); runs = [k for k in R if not k.startswith("pre")]
    V = {k: rows(R[k]) for k in runs}
    sc = [sum(w for w, p in zip(W, V[k]) if p) / sum(W) for k in runs]
    fail = [k for k, s in zip(runs, sc) if s < 1]
    diff = lambda a, b: sum(1 for x, y in zip(V[a], V[b]) if x != y)
    groups = []
    for l in fail:
        hit = [g for g in groups if any(diff(l, m) <= 1 for m in g)]
        groups = [g for g in groups if g not in hit] + [[l] + [m for g in hit for m in g]]
    groups.sort(key=len, reverse=True)
    print(f, " ".join(f"{k}:{s:.1%}" for k, s in zip(runs, sc)), f"| avg {statistics.mean(sc):.1%} SD {statistics.stdev(sc):.3f} (pop {statistics.pstdev(sc):.3f}) | patterns {len(groups)} largest {len(groups[0])}/{len(fail)}")
