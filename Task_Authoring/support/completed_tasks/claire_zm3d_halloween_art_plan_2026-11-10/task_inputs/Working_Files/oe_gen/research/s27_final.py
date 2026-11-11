import sys, json, re, collections, base64
sys.path.insert(0, ".")
import traj_lib as T
ev, c1 = T.load("B1")
print("=== tool roster (hg) in init")
tools = ev[0]["tools"]; hg = sorted(t.replace("mcp__hg__","") for t in tools if t.startswith("mcp__hg__"))
print(len(hg)); print(hg)
print("named check:", {n:(n in hg) for n in ["gsheets_get_spreadsheet","trello_get_board_actions","gsheets_values_get","gdrive_read_sheet_range","slack_read_user_profile","slack_conversations_replies","linear_list_comments"]})
print("=== profile calls", [ (r, c["input"]) for r in T.RUNS for c in T.load(r)[1] if c["name"]=="slack_read_user_profile"])
print("=== multiword slack B1#93", c1[93]["input"])
d = T.unwrap(c1[93]["out"]); ms = d["messages"]
both = sum(1 for m in ms if "ipad" in m["text"].lower() and "screenshot" in m["text"].lower())
print("n", len(ms), "both", both, "only ipad", sum(1 for m in ms if "ipad" in m["text"].lower() and "screenshot" not in m["text"].lower()), "only screenshot", sum(1 for m in ms if "screenshot" in m["text"].lower() and "ipad" not in m["text"].lower()), {k:v for k,v in d.items() if k!="messages"})
print("  sample", [m["text"][:90] for m in ms[:3]])
print("order desc:", all(float(ms[i]["ts"])>=float(ms[i+1]["ts"]) for i in range(len(ms)-1)))
print("=== read_channel: any reply rows?")
for r in T.RUNS:
    for c in T.load(r)[1]:
        if c["name"]=="slack_read_channel":
            dd = T.unwrap(c["out"]); m = dd["messages"]
            rep = [x["ts"] for x in m if x.get("thread_ts") and x.get("thread_ts")!=x["ts"]]
            print(r, c["seq"], c["input"], "n", len(m), "reply rows", len(rep), "desc", all(float(m[i]["ts"])>=float(m[i+1]["ts"]) for i in range(len(m)-1)))
print("=== full-format parent w/ reply_count in read_channel")
dd = T.unwrap(c1[3]["out"])
x = [m for m in dd["messages"] if m.get("reply_count")][:1]
print(json.dumps({k:v for k,v in x[0].items() if k in ("ts","thread_ts","reply_count","reply_users_count","latest_reply","latest_reply_time")}) if x else None)
print("=== linear default order by updatedAt B2#24")
ev2, c2 = T.load("B2")
iss = T.unwrap(c2[24]["out"])["issues"]; print([(i["id"], i["updatedAt"]) for i in iss])
print("=== ART-792 vs createdAt filter (B4#28)")
ev4, c4 = T.load("B4")
iss = T.unwrap(c4[28]["out"])["issues"]
print([(i["id"], i["createdAt"]) for i in iss if i["id"] in ("ART-793","ART-792","ART-791","ART-790")])
print("=== B3#16 batch body? / B5#13")
ev3, c3 = T.load("B3"); ev5, c5 = T.load("B5")
for lbl, c in (("B3#16", c3[16]), ("B5#13", c5[13]), ("B4#12", c4[12])):
    d = T.unwrap(c["out"]); m = d["messages"][0]; p = m.get("payload", {})
    print(lbl, "format", c["input"].get("format"), "payload keys", list(p.keys()), "body", json.dumps(p.get("body"))[:90], "not_found", d.get("not_found"))
print("=== Oct 10 origin")
for r, s in (("B1",122),("B2",113),("B3",101)):
    c = T.load(r)[1][s]; t = json.dumps(c["input"], ensure_ascii=False)
    for m in list(re.finditer(r"Oct 10|not the 15th", t))[:2]: print(r, s, "...", t[max(0,m.start()-120):m.end()+90])
print("=== #1935 comment source")
c = c1[84]; print(c["input"], [x["body"] for x in T.unwrap(c["out"])["comments"]])
c = c1[85]; print(c["input"], [x["body"] for x in T.unwrap(c["out"])["comments"]])
c = c1[83]; print(c["input"], [x["body"] for x in T.unwrap(c["out"])["comments"]])
for t in ("ART-795","ART-805","ART-797"):
    c = [x for x in c1 if x["name"]=="linear_list_comments" and x["input"].get("issueId")==t][0]
    print(t, [x["body"] for x in T.unwrap(c["out"])["comments"]])
print("=== per-run write coverage")
for r in T.RUNS:
    calls = T.load(r)[1]
    cm = [c for c in calls if c["name"]=="linear_create_comment" and not c["err"]]
    ids = {c["input"]["issueId"] for c in cm}; exp = {f"ART-{n}" for n in range(793,855)} - {"ART-836","ART-837","ART-838","ART-839"}
    up = [c for c in calls if c["name"]=="linear_update_issue"]
    a = collections.Counter(c["input"].get("assignee") for c in up)
    print(r, "comments ok", len(cm), "unique", len(ids), "missing", sorted(exp-ids), "extra", sorted(ids-exp), "| updates", len(up), dict(a), "state set", sum(1 for c in up if "state" in c["input"]), "| final", [ (c["input"]["id"]) for c in up if "ART-826"==c["input"]["id"]])
print("=== B4 values_get", c4[119]["input"], T.text(c4[119]["out"])[:342])
print("=== B5 batch_clear", c5[105]["input"], T.text(c5[105]["out"]))
print("=== non-RAW values_update examples")
for r in T.RUNS:
    for c in T.load(r)[1]:
        if c["name"]=="gsheets_values_update" and c["input"].get("valueInputOption")=="USER_ENTERED":
            print(r, c["seq"], c["input"]["range"], json.dumps(c["input"]["values"])[:130], "->", T.unwrap(c["out"]).get("updatedRange"))
print("=== Key dates!A1 unquoted")
for r in T.RUNS:
    for c in T.load(r)[1]:
        if c["name"]=="gsheets_values_update" and c["input"]["range"]=="Key dates!A1":
            print(r, c["seq"], T.text(c["out"])[:230])
print("=== B6 base64 bash", json.dumps(T.load("B6")[1][19]["input"])[:200])
print("=== confluence", [ (r, c["name"], c["input"], len(c["out"])) for r in T.RUNS for c in T.load(r)[1] if c["name"].startswith("confluence")])
