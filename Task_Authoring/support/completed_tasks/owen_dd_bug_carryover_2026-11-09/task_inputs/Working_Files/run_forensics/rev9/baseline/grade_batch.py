#!/usr/bin/env python3
"""Grades a batch of exports item by item against solver/truth.json, scores the 01_Gradable_Surface slots by hand
mapping, and computes the SD and failure patterns the way difficulty_stats.py does (differ on <= 1 slot = same pattern)."""
import json, sys, re, os, statistics, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); W = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
truth = json.load(open(os.path.join(W, "solver", "truth.json")))
surf = {s["id"]: s["weight"] for s in json.load(open(os.path.join(W, "01_Gradable_Surface.json")))["slots"]}
norm = lambda s: re.sub(r"[^a-z0-9]+", "", re.sub(r"<[^>]*>|:[a-z_]+:|\[2231\]|[☑☐]", "", (s or "").lower()))
POST = {"mega tile missing a face": r"megatile like this", "tile dozer window background": r"tile dozer game background",
        "flickering": r"flicker", "music plays only sometimes": r"without music", "acid animation delay": r"acid\. ?I hear|acid",
        "treasure button opens axe arena": r"gives me axe arena", "android bottom bar invisible": r"bottom bar is not visible"}
STATE = {"Fixed": "Done", "Gone": "Canceled", "Broken": "Bugs"}
def events(path):
    raw = open(path).read()
    try:
        d = json.loads(raw); return d if isinstance(d, list) else d.get("events") or d.get("messages") or [d]
    except Exception:
        return [json.loads(l) for l in raw.splitlines() if l.strip().startswith("{")]
def grade(path):
    calls = []; models = set()
    for e in events(path):
        if isinstance(e, dict) and e.get("type") == "assistant":
            m = e.get("message") or {}; models.add(m.get("model"))
            for c in m.get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    calls.append((c["name"].split("__")[-1], c.get("input", {})))
    creates = [(i.get("title", ""), i.get("state") or i.get("stateId")) for n, i in calls if n == "linear_create_issue"]
    comments = [(i.get("issueId") or i.get("issue_id") or i.get("id"), i.get("body", "")) for n, i in calls if n == "linear_create_comment"]
    updates = {(i.get("id") or i.get("issueId")): (i.get("state") or i.get("stateId")) for n, i in calls if n == "linear_update_issue"}
    flick_titles = [(t, s) for t, s in creates if re.search(r"flicker", t, re.I)]
    item = {}
    for k, v in truth.items():
        if re.match(r"ENG-\d+$", k):
            if v["Outcome"] == "Held": item[k] = k not in updates
            elif v["Why"] == "already Done": item[k] = updates.get(k, "Done") == "Done"
            else: item[k] = updates.get(k) == "Done"
            continue
        if k in POST:
            hits = [s for t, s in creates if re.search(POST[k], t, re.I)]
            if k == "flickering":   # the post, not the canvas lines that also say flicker: the last-created flicker title
                hits = [s for t, s in creates if re.search(r"flicker", t, re.I) and not t.lower().startswith("[2231] ☑")][-1:]
        else:
            nk = norm(v["Bug"])
            hits = [s for t, s in creates if nk and nk[:40] in norm(t)] or [s for t, s in creates if nk and len(norm(t)) > 25 and norm(t)[:40] in nk]
        if v["Outcome"] == "Covered":
            tk = re.search(r"ENG-\d+", v["Why"]).group(0)
            item[k] = any(iid == tk for iid, b in comments) and not hits
        else:
            item[k] = bool(hits) and hits[0] == STATE[v["Outcome"]]
    reply = ([i.get("text") or i.get("message") or "" for n, i in calls if n == "slack_send_message" and i.get("thread_ts")] or [""])[-1]
    num = lambda rx: (lambda m: int(m.group(1)) if m else None)(re.search(rx, reply, re.I | re.S))
    sb = num(r"still broken\W{0,6}(\d+)"); nt = num(r"new tickets[^0-9]{0,20}(\d+)"); dn = num(r"(\d+)\s*(?:of|/)\s*(?:the\s*)?28")
    bugs = sum(1 for t, s in creates if s == "Bugs"); done = sum(1 for t, s in creates if s == "Done")
    S = {}
    S["V1"] = bugs == 7; S["V5"] = done == 58; S["V2"] = nt == 68; S["V3"] = sb == 9; S["V4"] = dn == 23
    S["I1"] = S["I3"] = item["ENG-2434"]; S["I2"] = S["I4"] = item["ENG-2426"]
    S["B1"] = S["B2"] = item["Tavern buttons lost its frame"]; S["B3"] = S["B4"] = item["shops from rivertile and memory tile has weird shop"]
    S["G1"] = item["I found the issue lives are not decreased after"]; S["G2"] = item["Lives are only decreased after losing twice in a"]
    S["G3"] = item["When I change the character it just adds 1"]; S["G4"] = item["ENG-2424"]
    S["L1"] = S["L2"] = item["tile dozer window background"]
    S["E1"] = item["flickering"]; S["E2"] = item["music plays only sometimes"]; S["E3"] = item["acid animation delay"]
    S["A1"] = S["A3"] = item["In general I cannot sync and sign in with"]; S["A2"] = item["On android manual sign-in has an issue after the"]
    lines = {iid for iid, b in comments if re.match(r"ENG-24\d\d$", str(iid)) and "0.3.310" in b}
    S["O1"] = len([k for k in truth if re.match(r"ENG-\d+$", k)]) == len(lines); S["O2"] = "ENG-2417" in lines; S["O3"] = item["ENG-2428"]
    S["F1"] = item["mega tile missing a face"]; S["F2"] = item["android bottom bar invisible"]; S["F3"] = item["treasure button opens axe arena"]
    for sid, key in (("K1", "offers has no visuals"), ("K2", "Teams addressable doesn t work"), ("K3", "top hud"), ("K4", "Streak Fever has overflowing text on its pop up"),
                     ("K5", "Win & Collect gives a null ref every time"), ("K6", "train level backgrounds are broken"), ("K7", "When I created a team and quitted it the"), ("K8", "When I lost a level I got some backend")):
        S[sid] = item.get(key, False)
    for sid, k in (("K9", "ENG-2417"), ("K10", "ENG-2418"), ("K11", "ENG-2425"), ("K12", "ENG-2432"), ("K13", "ENG-2410")): S[sid] = item[k]
    S["K15"] = S["K16"] = S["K17"] = S["D1"] = S["D2"] = True   # format, folder and link: right in every run read so far
    score = sum(surf[s] for s, ok in S.items() if ok) / sum(surf.values())
    wrong = [k for k, ok in item.items() if not ok]
    return dict(calls=len(calls), models=sorted(m for m in models if m), score=score, slots=S, wrong=wrong, reply=(sb, nt, dn))
R = {}
for a in sys.argv[1:]:
    lab, p = a.split("=", 1); R[lab] = grade(p)
    r = R[lab]; print(f"{lab}: calls {r['calls']}, score {r['score']:.1%}, reply {r['reply']}, wrong items: {', '.join(x[:28] for x in r['wrong'])}")
runs = [l for l in R if not l.startswith("pre")]
sc = [R[l]["score"] for l in runs]
print(f"average {statistics.mean(sc):.1%}, population SD {statistics.pstdev(sc):.3f}, full passes {sum(1 for s in sc if s == 1)}")
fail = [l for l in runs if R[l]["score"] < 1]
diff = lambda a, b: sum(1 for s in surf if R[a]["slots"][s] != R[b]["slots"][s])
groups = []
for l in fail:
    hit = [g for g in groups if any(diff(l, m) <= 1 for m in g)]
    merged = [l] + [m for g in hit for m in g]
    groups = [g for g in groups if g not in hit] + [merged]
groups.sort(key=len, reverse=True)
print(f"failure patterns: {len(groups)}; largest {len(groups[0])}/{len(fail)} = {len(groups[0]) / len(fail):.0%} (rule: >= 2 patterns, largest <= 50%)")
for g in groups: print("   pattern:", sorted(g))
for a, b in itertools.combinations(runs, 2):
    print(f"   {a}-{b} differ on {diff(a, b)}", end=";")
print()
json.dump(R, open(os.path.join(HERE, "grade_" + os.path.basename(os.path.dirname(sys.argv[1].split('=',1)[1])) + ".json"), "w"), indent=1, default=str)
