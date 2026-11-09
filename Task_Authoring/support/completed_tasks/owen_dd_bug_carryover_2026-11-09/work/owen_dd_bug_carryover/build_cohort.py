#!/usr/bin/env python3
"""Writes plan/cohort.json from plan/truth_sketch.json: one short key per bug, the 28 UI children, and the fields the solver starts from.
Keys match the surface key_regex. A later-bug key is the short label in the truth sketch."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "truth_sketch.json")))
KRX = r"(?:Bug 1|[A-Za-z][A-Za-z0-9 .()&/-]*)"


def key_of(text):
    t = re.sub(r"^[☐☑]\s*", "", text)
    t = re.sub(r":[a-z_]+:", " ", t)
    t = re.sub(r"<@[^>]+>|@[A-Z][a-z]+ [A-Z][a-z]+", " ", t)
    t = t.replace("[PERSON_NAME_1711]'s", "Nate's").replace("[USERNAME_20421]", "Rush").replace("[USERNAME_20422]", "")
    t = re.sub(r"[^A-Za-z0-9 .()&/-]", " ", t)
    t = re.sub(r"\s+", " ", t).strip(" .")
    t = re.sub(r"^P\.S ", "", t)
    words = t.split()
    return " ".join(words[:9])


bugs, seen = [], set()
for x in T:
    if x["kind"] == "tree_child":
        continue
    k = key_of(x["text"]) if x["kind"] == "canvas_line" else x["text"]
    assert re.fullmatch(KRX, k), k
    n, base = 2, k
    while k in seen:
        k = f"{base} {n}"
        n += 1
    seen.add(k)
    bugs.append({"key": k, "id": x["id"], "line": x["text"], "kind": x["kind"], "ticked": x.get("ticked"), "outcome": x["outcome"], "why": x.get("why")})
DONE9 = ["ENG-2409", "ENG-2411", "ENG-2412", "ENG-2413", "ENG-2416", "ENG-2420", "ENG-2421", "ENG-2422", "ENG-2423"]
kids = [{"key": k, "already_done": True} for k in DONE9] + [{"key": x["id"], "already_done": False, "plan": x["outcome"]} for x in T if x["kind"] == "tree_child"]
json.dump({"bugs": bugs, "children": kids}, open(os.path.join(HERE, "cohort.json"), "w"), indent=1, ensure_ascii=False)
print(len(bugs), len(kids))
for b in bugs:
    print(b["outcome"][:7].ljust(8), b["key"])
