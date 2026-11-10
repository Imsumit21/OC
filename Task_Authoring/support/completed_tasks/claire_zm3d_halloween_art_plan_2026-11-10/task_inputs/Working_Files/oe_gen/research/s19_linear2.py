import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
ev, calls = T.load("B2")
d = T.unwrap(calls[88]["out"]); ids = [i["id"] for i in d["issues"]]
nums = sorted(int(x.split("-")[1]) for x in ids)
print("B2#88 ids range", nums[0], nums[-1], "contiguous", nums == list(range(793, 855)), "n", len(nums))
print(json.dumps(d["issues"][:3], ensure_ascii=False))
print("order first 12", ids[:12])
print("=== full issue object B2#24[0]"); d2 = T.unwrap(calls[24]["out"]); print(json.dumps(d2["issues"][0], ensure_ascii=False, indent=0)[:2300])
print("=== julia ids", [(i["id"], i["title"]) for i in d2["issues"]])
print("=== linear_get_issue ART-831 B2#82", calls[82]["input"]); print(T.text(calls[82]["out"]))
ev3, c3 = T.load("B3")
print("=== linear_get_issue ART-826 B3#79"); print(T.text(c3[79]["out"]))
print("=== B3 statuses", c3[99]["input"]); print(T.text(c3[99]["out"]))
print("=== B3 list_users", c3[98]["input"]); print(T.text(c3[98]["out"]))
ev4, c4 = T.load("B4")
print("=== B4 list_teams", c4[102]["input"]); print(T.text(c4[102]["out"]))
print("=== B4 list_users (first 500)", c4[103]["input"]); print(T.text(c4[103]["out"])[:500])
ev6, c6 = T.load("B6")
print("=== B6 list_teams", c6[26]["input"]); print(T.text(c6[26]["out"])[:1034])
print("=== linear_list_comments forms")
pc = collections.Counter()
for r in T.RUNS:
    ev, calls = T.load(r)
    forms = collections.Counter(); ids = []
    for c in calls:
        if c["name"] == "linear_list_comments":
            forms[tuple(sorted(c["input"].keys()))] += 1; ids.append(c["input"].get("issueId") or c["input"].get("id"))
    s = set(ids)
    exp = {f"ART-{n}" for n in range(793, 855)}
    print(r, dict(forms), "unique", len(s), "dupes", len(ids)-len(s), "826", "ART-826" in s, "831", "ART-831" in s, "missing of 793-854:", sorted(exp - s), "extra:", sorted(s - exp))
ev, calls = T.load("B3")
cc = [c for c in calls if c["name"] == "linear_list_comments"]
for c in cc:
    if c["input"].get("issueId") in ("ART-826", "ART-831", "ART-793"):
        print("###", c["seq"], json.dumps(c["input"])); print(T.text(c["out"]))
