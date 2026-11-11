import sys, json
sys.path.insert(0, ".")
import traj_lib as T
BULK = {"linear_list_comments","linear_create_comment","linear_update_issue","gdrive_share_file","Bash","Read","gsheets_values_update"}
for r in T.RUNS:
    ev, calls = T.load(r)
    print("=====", r)
    for c in calls:
        if c["name"] in BULK: continue
        print(c["seq"], c["name"], json.dumps(c["input"], ensure_ascii=False)[:170], "=>", len(c["out"] or ""), "ERR" if c["err"] else "", "SPILL" if (c["out"] or "").startswith("Error: result (") else "")
