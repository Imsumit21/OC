import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
CALLS = {r: T.load(r)[1] for r in T.RUNS}
W = {"linear_create_comment","linear_update_issue","linear_create_issue","slack_send_message","gsheets_values_update","gdocs_create_document","gdocs_batch_update","gsheets_batch_update","Bash","Read","Agent","gsheets_values_get"}
print("(a) Fri Oct 10 in non-write outputs:", [(r,c["seq"],c["name"]) for r in T.RUNS for c in CALLS[r] if "Fri Oct 10" in T.text(c["out"]) and c["name"] not in W])
print("(a2) counts per tool:", {r: collections.Counter(c["name"] for c in CALLS[r] if "Fri Oct 10" in T.text(c["out"])) for r in T.RUNS})
print("(a3) 'Oct 10' any read:", [(r,c["seq"],c["name"]) for r in T.RUNS for c in CALLS[r] if re.search(r"\bOct(ober)? 10\b", T.text(c["out"])) and c["name"] not in W][:12])
tick = {}
for c in CALLS["B2"]:
    if c["name"]=="linear_list_comments": pass
titles = {i["id"]: i["title"] for i in T.unwrap(CALLS["B2"][88]["out"])["issues"]}
m = collections.Counter()
for r in T.RUNS:
    for c in CALLS[r]:
        if c["name"]=="linear_update_issue" and "martin" in c["input"]["assignee"]:
            m[titles.get(c["input"]["id"], c["input"]["id"])] += 1
print("(c) Martin-assigned:", m.most_common())
print("(m) deck in B4#20:", any(f["id"]=="f_5ebf55ad29e815d46243c8" for f in T.unwrap(CALLS["B4"][20]["out"])["files"]), "| B6#23 first", T.unwrap(CALLS["B6"][23]["out"])["files"][0]["name"])
print("(o) B1#28 tail:", T.text(CALLS["B1"][28]["out"])[-60:].replace("\n"," / "))
print("    has both B1#28:", "ART-826" in T.text(CALLS["B1"][28]["out"]), "ART-831" in T.text(CALLS["B1"][28]["out"]))
print("    B6#29 head/tail:", T.text(CALLS["B6"][29]["out"])[:60].replace("\n"," / "), "...", T.text(CALLS["B6"][29]["out"])[-60:].replace("\n"," / "), "has both", "ART-826" in T.text(CALLS["B6"][29]["out"]), "ART-831" in T.text(CALLS["B6"][29]["out"]))
print("    B5#22 has both:", "ART-826" in T.text(CALLS["B5"][22]["out"]), "ART-831" in T.text(CALLS["B5"][22]["out"]))
ev = T.load("B4")[0]
names = collections.Counter(b["name"] for e in ev if isinstance(e,dict) and e.get("parent_tool_use_id") and e.get("type")=="assistant" for b in e["message"]["content"] if isinstance(b,dict) and b.get("type")=="tool_use")
print("(ee) subagent tools:", names)
print("(zz) slack cursor inputs:", [(r,c["seq"]) for r in T.RUNS for c in CALLS[r] if c["name"].startswith("slack_") and "cursor" in (c["input"] or {})])
print("(id) sheet id lens:", {len(T.unwrap(c["out"])["spreadsheetId"]) for r in T.RUNS for c in CALLS[r] if c["name"]=="gsheets_create_spreadsheet"}, "doc id lens:", {len(T.unwrap(c["out"])["documentId"]) for r in T.RUNS for c in CALLS[r] if c["name"]=="gdocs_create_document"})
print("(lim) all limit>=250 calls:", [(r,c["seq"],len(c["out"]),(c["out"] or "")[:14]) for r in T.RUNS for c in CALLS[r] if c["name"]=="linear_list_issues" and c["input"].get("limit",0)>=250])
print("(users) ", [ (r,c["input"]) for r in T.RUNS for c in CALLS[r] if c["name"]=="linear_list_users"])
print("(hal) halloween hit 1758127951.679146 in all runs:", {r: any("1758127951.679146" in T.text(c["out"]) for c in CALLS[r] if "search" in c["name"]) for r in T.RUNS})
