import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
W = ["gdocs_create_document","gsheets_create_spreadsheet","gsheets_values_update","gsheets_batch_update","gdocs_batch_update","gsheets_values_batch_clear","gdrive_share_file","linear_create_comment","linear_update_issue","linear_create_issue","slack_send_message"]
fails = []
shapes = collections.defaultdict(collections.Counter)
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] not in W: continue
        shapes[c["name"]][tuple(sorted((c["input"] or {}).keys()))] += 1
        t = T.text(c["out"]); d = T.unwrap(c["out"])
        bad = c["err"] or (isinstance(d, dict) and (d.get("error") or d.get("ok") is False or d.get("success") is False)) or t.lower().startswith("error")
        if bad:
            fails.append((r, c["seq"], c["name"], json.dumps(c["input"], ensure_ascii=False)[:300], t[:400]))
print("=== write input key forms")
for n in W:
    print(n)
    for k, v in shapes[n].most_common(): print("   ", v, k)
print("\n=== failures", len(fails))
for f in fails: print(f)
