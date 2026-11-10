import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
ass = collections.Counter(); st = collections.Counter(); due = collections.Counter(); roles = collections.Counter(); vio = collections.Counter(); ranges = collections.Counter()
ostat = collections.Counter()
print("=== create_issue per run")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        i = c["input"]
        if c["name"] == "linear_update_issue":
            ass[i.get("assignee")] += 1; st[i.get("state")] += 1; due[i.get("dueDate")] += 1
            d = T.unwrap(c["out"])
            if isinstance(d, dict):
                ostat[(i.get("state"), d.get("status"), d.get("statusType"))] += 1
        if c["name"] == "gdrive_share_file": roles[i.get("role")] += 1
        if c["name"] == "gsheets_values_update":
            vio[i.get("valueInputOption")] += 1; ranges[i.get("range")] += 1
        if c["name"] == "linear_create_issue":
            d = T.unwrap(c["out"])
            print(r, c["seq"], {k:i.get(k) for k in ("team","assignee","dueDate","state","priority")}, "=>", d.get("identifier"), d.get("status"), d.get("statusType"), d.get("priority"), d.get("assignee"), d.get("dueDate"), d.get("team"), "| title:", i.get("title")[:60])
print("assignee", ass.most_common()); print("state", st.most_common()); print("due", due.most_common()); print("in/out status", ostat.most_common()); print("roles", roles.most_common()); print("valueInputOption", vio.most_common()); print("ranges", ranges.most_common(30))
print("\n=== slack_send, share, url source")
for r in T.RUNS:
    ev, calls = T.load(r)
    sh = [c for c in calls if c["name"] == "gdrive_share_file"]
    emails = collections.Counter(c["input"]["emailAddress"] for c in sh); files = collections.Counter(c["input"]["fileId"] for c in sh)
    s = [c for c in calls if c["name"] == "slack_send_message"][0]
    d = T.unwrap(s["out"])
    doc = [c for c in calls if c["name"] == "gdocs_create_document"][0]; sp = [c for c in calls if c["name"] == "gsheets_create_spreadsheet"][0]
    print(r, "send", s["input"]["channel_id"], s["input"]["thread_ts"], "ok", d.get("ok"), "ts", d.get("ts"), "| doc", T.unwrap(doc["out"]).get("documentId"), "| sheet", T.unwrap(sp["out"]).get("spreadsheetId"))
    print("    share files", dict(files)); print("    share emails", sorted(emails.keys()), "n", len(sh))
    print("    meta after create", [c["input"].get("fileId") for c in calls if c["name"] == "gdrive_get_file_metadata" and c["seq"] > doc["seq"]])
ev, calls = T.load("B3")
print("\n=== B3 retry around #164")
for s in (163, 164, 165, 166):
    c = calls[s]; print(s, c["name"], c["input"].get("issueId"), "err", c["err"], T.text(c["out"])[:120])
ev, calls = T.load("B1")
c = [c for c in calls if c["name"] == "linear_create_comment"][0]
print("\n=== create_comment tail"); print(T.text(c["out"])[-330:])
ev, calls = T.load("B2")
for s in (94,):
    print("\n=== B2 create_issue no state tail"); print(T.text(calls[s]["out"])[-520:])
u = [c for c in calls if c["name"] == "linear_update_issue" and "state" not in c["input"]][0]
print("\n=== update w/o state", json.dumps(u["input"])); d = T.unwrap(u["out"]); print({k: d.get(k) for k in ("id","status","statusType","assignee","assigneeId","dueDate","completedAt","updatedAt")}); print(json.dumps(d.get("stateHistory"))[:400])
print("\n=== values_update w/o valueInputOption")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] == "gsheets_values_update" and "valueInputOption" not in c["input"]:
            print(r, c["seq"], c["input"]["range"], json.dumps(c["input"]["values"])[:160], T.text(c["out"])[:300])
