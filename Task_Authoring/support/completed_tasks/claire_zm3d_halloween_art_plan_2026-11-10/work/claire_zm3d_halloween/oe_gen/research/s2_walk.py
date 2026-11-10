import sys, json
sys.path.insert(0, ".")
import traj_lib as T
run = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 200
ev, calls = T.load(run)
# first user event = prompt
for e in ev[:6]:
    if e.get("type") == "user":
        print("PROMPT:", T.flat(e["message"]["content"])[:3000]); break
print("keys sample", list(ev[1].keys())[:12] if len(ev)>1 else "")
for c in calls:
    if c["name"] in ("linear_list_comments","linear_create_comment","linear_update_issue","gdrive_share_file") and c["seq"]>12:
        continue
    print(c["seq"], c["name"], json.dumps(c["input"], ensure_ascii=False)[:n], "=>", len(c["out"] or ""), "ERR" if c["err"] else "")
