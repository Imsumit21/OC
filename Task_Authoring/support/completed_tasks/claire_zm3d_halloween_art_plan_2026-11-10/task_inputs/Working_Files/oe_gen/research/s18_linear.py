import sys, json, re
sys.path.insert(0, ".")
import traj_lib as T
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] == "linear_list_issues":
            d = T.unwrap(c["out"])
            sp = (c["out"] or "").startswith("Error: result (")
            print(f"--- {r}#{c['seq']}", json.dumps(c["input"]))
            if sp:
                print("   SPILL:", (c["out"] or "")[:60])
                # follow-up Bash output
                nxt = calls[c["seq"]+1]
                print("   next:", nxt["name"], json.dumps(nxt["input"])[:260]); print("   nextout:", T.text(nxt["out"])[:260].replace("\n"," / "))
                continue
            if isinstance(d, dict):
                iss = d.get("issues", [])
                ids = [i.get("id") or i.get("identifier") for i in iss]
                print("   n", len(iss), "hasNextPage", d.get("hasNextPage"), "cursor", d.get("cursor"), "keys", list(d.keys()))
                print("   first", ids[:6], "last", ids[-4:], "has826", "ART-826" in ids, "has831", "ART-831" in ids)
                if iss: print("   sample", json.dumps(iss[0], ensure_ascii=False)[:520])
            else:
                print("   raw", T.text(c["out"])[:200])
