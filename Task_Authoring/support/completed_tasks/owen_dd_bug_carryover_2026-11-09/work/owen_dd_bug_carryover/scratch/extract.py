import json, re, sys
def load(p):
    d = json.loads(open(p).read()); return d if isinstance(d, list) else d.get("events") or d.get("messages") or [d]
out = {}
for n in range(1, 7):
    ev = load(f"{sys.argv[1]}/trajectory-run-{n}.json")
    calls = []  # (event_idx, name, input, id)
    results = {}
    for i, e in enumerate(ev):
        if not isinstance(e, dict): continue
        if e.get("type") == "assistant":
            for c in (e.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    calls.append((i, c["name"].split("__")[-1], c.get("input", {}), c.get("id")))
        if e.get("type") == "user":
            for c in (e.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    v = c.get("content"); v = v if isinstance(v, str) else json.dumps(v)
                    results[c.get("tool_use_id")] = (i, v)
    r = {}
    cr = [(i, x) for i, nme, x, _ in calls if nme == "linear_create_issue"]
    r["creates"] = len(cr)
    r["apple_create"] = [(i, x.get("title"), x.get("state")) for i, x in cr if re.search(r"apple", x.get("title", ""), re.I)]
    r["signin_create"] = [(i, x.get("title"), x.get("state")) for i, x in cr if re.search(r"manual sign-in", x.get("title", ""), re.I)]
    r["tavern_create"] = [(i, x.get("title"), x.get("state")) for i, x in cr if re.search(r"tavern", x.get("title", ""), re.I)]
    cm = [(i, x.get("issueId") or x.get("id"), x.get("body", "")) for i, nme, x, _ in calls if nme == "linear_create_comment"]
    r["c2073"] = [(i, b[:160]) for i, k, b in cm if k == "ENG-2073"]
    r["c2363"] = [(i, b[:160]) for i, k, b in cm if k == "ENG-2363"]
    gm = [(i, nme, json.dumps(x)[:160]) for i, nme, x, _ in calls if nme.startswith("gmail")]
    r["gmail_calls"] = gm
    vin = [(i, nme) for i, nme, x, cid in calls if "CAK0a68e5711011904665cac8fb31fa" in json.dumps(x) or ("CAK0a68e5711011904665cac8fb31fa" in results.get(cid, (0, ""))[1])]
    r["vincent_mail_seen"] = vin[:3]
    dm = [(i, nme, json.dumps(x)[:120]) for i, nme, x, cid in calls if "D05USBTQY1F" in json.dumps(x)]
    r["marcus_dm_calls"] = dm[:3]
    tav_seen = [(i, nme, json.dumps(x)[:100]) for i, nme, x, cid in calls if "1765452012.418229" in results.get(cid, (0, ""))[1]]
    r["marcus_msg_in_results"] = tav_seen[:3]
    tq = [(i, json.dumps(x)[:100]) for i, nme, x, _ in calls if nme.startswith("slack_search") and re.search(r"tavern", json.dumps(x), re.I)]
    r["tavern_searches"] = tq
    rows, sheet_ev = [], []
    for i, nme, x, _ in calls:
        if nme in ("gsheets_values_update", "gsheets_values_append"):
            sheet_ev.append(i); rows += [(i, v) for v in (x.get("values") or [])]
    r["sheet_events"] = sheet_ev
    r["apple_row"] = [(i, v) for i, v in rows if v and re.search(r"apple", str(v[0]), re.I)]
    r["tavern_row"] = [(i, v) for i, v in rows if v and re.search(r"tavern", str(v[0]), re.I)]
    rep = [(i, x) for i, nme, x, _ in calls if nme == "slack_send_message"]
    r["reply"] = [(i, x.get("channel_id") or x.get("channel"), x.get("thread_ts"), (x.get("text") or x.get("message") or "")) for i, x in rep]
    out[n] = r
json.dump(out, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
for n, r in out.items():
    print("=== run", n, "creates", r["creates"])
    for k in ("apple_create", "signin_create", "tavern_create", "c2073", "c2363", "gmail_calls", "vincent_mail_seen", "marcus_dm_calls", "marcus_msg_in_results", "tavern_searches", "apple_row", "tavern_row", "sheet_events"):
        print(" ", k, json.dumps(r[k], ensure_ascii=False)[:420])
    for i, ch, th, t in r["reply"]:
        print("  reply ev", i, ch, th, "|", t[:700].replace("\n", " / "))
