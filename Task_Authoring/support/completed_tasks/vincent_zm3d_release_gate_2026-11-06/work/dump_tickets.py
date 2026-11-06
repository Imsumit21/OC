import json, sys, re
WS = "/Users/sumitkumar/Source/Outlier/OC"
sys.path.insert(0, f"{WS}/Task_Authoring/tools")
from base_check import parse_sql
SQL = parse_sql(open(f"{WS}/Task_Authoring/task_inputs/01_Universe_Inject.sql").read())
d = json.load(open(f"{WS}/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json"))
base = {i["id"]: (idx, i) for idx, i in enumerate(d["issues"])}
seed_iss = {r["row"]["id"]: r["row"] for r in SQL if r["table"] == "linear.linear_issues" and r["op"] == "insert"}
upd = [r for r in SQL if r["table"] == "linear.linear_issues" and r["op"] != "insert"]
print("issue updates in SQL:", [(u.get("op"), u.get("row", {}).get("id") or u.get("where")) for u in upd][:20])
comments = {}
for r in SQL:
    if r["table"] == "linear.linear_comments" and r["op"] == "insert":
        c = r["row"]; comments.setdefault(c["issue_id"], []).append(c)
users = {u["id"]: u.get("email") or u.get("name") for u in d["users"]}
keys = json.load(open(f"{WS}/Task_Authoring/task_inputs/Working_Files/01_Gradable_Surface.json"))["truth_keys"]
out = {}
for k in keys:
    if k in seed_iss:
        i = seed_iss[k]; src = "SQL"; ptr = None
    else:
        idx, i = base[k]; src = "base"; ptr = f"/issues/{idx}"
    out[k] = {"src": src, "ptr": ptr, "title": i.get("title"), "state": i.get("state_id"), "team": i.get("team_id"),
              "labels": i.get("labels") or i.get("labels_json"), "completed": i.get("completed_at"),
              "desc": (i.get("description") or "")[:400],
              "comments": [(c["id"], users.get(c["author_id"], c["author_id"]), c["created_at"], c["body"][:300]) for c in sorted(comments.get(k, []), key=lambda c: c["created_at"])]}
json.dump(out, open("/tmp/rubricwork/tickets.json", "w"), indent=1, ensure_ascii=False)
for k in sys.argv[1:]:
    print(k, json.dumps(out[k], ensure_ascii=False, indent=1))
