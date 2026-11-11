import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
print("=== first sighting of ART-826 / ART-831 per run (any non-write output)")
SKIP = {"linear_create_comment","linear_update_issue","linear_create_issue","slack_send_message","gsheets_values_update","gdocs_create_document"}
for r in T.RUNS:
    ev, calls = T.load(r)
    for tag in ("ART-826","ART-831"):
        first = None; lc = None; wc = None; gi = None
        for c in calls:
            t = T.text(c["out"]) or ""
            if first is None and tag in t and c["name"] not in SKIP:
                first = (c["seq"], c["name"], json.dumps(c["input"])[:110])
            if lc is None and c["name"]=="linear_list_comments" and c["input"].get("issueId")==tag: lc = c["seq"]
            if wc is None and c["name"]=="linear_create_comment" and c["input"].get("issueId")==tag: wc = c["seq"]
            if gi is None and c["name"]=="linear_get_issue" and c["input"].get("id")==tag: gi = c["seq"]
        print(r, tag, "first", first, "| get_issue", gi, "| list_comments", lc, "| create_comment", wc)
print("\n=== B5 21..23")
ev, calls = T.load("B5")
for s in (21,22,23):
    c = calls[s]; print(s, c["name"], json.dumps(c["input"])[:420]); print("  ->", T.text(c["out"])[:420].replace("\n"," / "))
print("\n=== halloween search hits (B1#13)")
ev, calls = T.load("B1")
d = T.unwrap(calls[13]["out"])
for m in d["messages"]:
    ci = m.get("channel_info") or {}
    print(m.get("ts"), "thread_ts", m.get("thread_ts"), ci.get("name") or m.get("channel"), (m.get("user_profile") or {}).get("name"), "|", (m.get("text") or "")[:140].replace("\n"," "), "| reply_count", m.get("reply_count"))
print("\n=== channels list B3#3 names of interest")
ev, calls = T.load("B3")
d = T.unwrap(calls[3]["out"])
print("n", len(d["channels"]), {k:v for k,v in d.items() if k!="channels"})
for ch in d["channels"]:
    if ch["id"] in ("C09ATAJ220H","C05KNDCHAAG","C0880U9751A","C08R8CHB0QL","C06DJBJL798") or re.search(r"zm|zombie|art|team|general|announce|vacation|ooo", ch["name"]):
        print(" ", ch["id"], ch["name"], "private" if ch.get("is_private") else "public", ch.get("num_members"), (ch.get("purpose") or {}).get("value"))
print("\n=== B2#89/#90 hits in C09ATAJ220H / C0880U9751A / C05KNDCHAAG")
ev, calls = T.load("B2")
for s in (89, 90):
    d = T.unwrap(calls[s]["out"]); print(s, calls[s]["input"], "n", len(d["messages"]), {k:v for k,v in d.items() if k!="messages"})
    for m in d["messages"]:
        ci = m.get("channel_info") or {}
        if m.get("channel") in ("C09ATAJ220H","C0880U9751A","C05KNDCHAAG"):
            print("   ", m.get("ts"), "thread", m.get("thread_ts"), ci.get("name"), (m.get("user_profile") or {}).get("name"), "|", (m.get("text") or "")[:150].replace("\n"," "))
print("\n=== B4 subagent events")
ev, calls = T.load("B4")
for e in ev:
    if isinstance(e, dict) and e.get("parent_tool_use_id") and e.get("type") in ("assistant","user"):
        c = e["message"]["content"]
        print(e["type"], json.dumps(c, ensure_ascii=False)[:230])
