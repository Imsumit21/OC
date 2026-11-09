import json, re, sys, collections
WRITE = ("linear_create_issue", "linear_create_comment", "linear_update_issue", "gsheets_create_spreadsheet", "gsheets_values_update", "gsheets_values_append", "gdrive_move_file", "gdrive_share_file", "gdrive_create_file")
def calls_of(p):
    raw = open(p).read(); d = json.loads(raw); ev = d if isinstance(d, list) else d.get("events") or d.get("messages") or [d]
    out = []
    for e in ev:
        if isinstance(e, dict) and e.get("type") == "assistant":
            for c in (e.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use": out.append((c["name"].split("__")[-1], c.get("input", {})))
    return out
HELD = ["ENG-2434", "ENG-2426", "ENG-2424", "ENG-2428", "ENG-2437"]
KIDS = ["ENG-24%02d" % n for n in range(9, 38) if n != 36]
def check(p):
    C = calls_of(p); r = {}
    cr = [i for n, i in C if n == "linear_create_issue"]
    tmpl = lambda i: (str(i.get("team", "")).lower() in ("engineering", "eng") and "Bug" in (i.get("labels") or []) and i.get("parentId") == "ENG-2401"
                      and not (i.get("assignee") or i.get("assigneeId")) and not (i.get("description") or "").strip() and str(i.get("title", "")).startswith("[2231]"))
    bad = [i.get("title", "")[:50] for i in cr if not tmpl(i)]
    r["creates"] = len(cr); r["template_bad"] = len(bad); r["bad_eg"] = bad[:2]
    keys = collections.Counter(k for i in cr for k in i); r["create_keys"] = dict(keys)
    find = lambda rx: [i for i in cr if re.search(rx, i.get("title", ""), re.I)]
    r["profile_prefix"] = all(i["title"].startswith("[2231]") for i in find(r"^\[2231\]\s*In profile,?\s*$|^In profile")) and bool(find(r"In profile"))
    fl = [i for i in find(r"Any idea what might cause this flickering")]
    r["flicker_title"] = [i["title"] for i in fl]
    cm = [(i.get("issueId") or i.get("issue_id") or i.get("id"), i.get("body", "")) for n, i in C if n == "linear_create_comment"]
    by = collections.defaultdict(list)
    for k, b in cm: by[k].append(b)
    r["held_stays_open"] = {k: bool(re.search(r"stay|open|held|hold|not (yet )?(done|complete|finished)|remain|isn.t (done|finished|complete)|left (open|as)", " ".join(by.get(k, [])), re.I)) for k in HELD}
    r["build_lines"] = sum(1 for k in KIDS if any("0.3.310" in b for b in by.get(k, [])))
    r["missing_build"] = [k for k in KIDS if not any("0.3.310" in b for b in by.get(k, []))]
    rows = []
    for n, i in C:
        if n in ("gsheets_values_update", "gsheets_values_append"): rows += i.get("values") or []
    hdr = [x for x in rows if x and str(x[0]).strip().lower() == "bug"]
    body = [x for x in rows if x and str(x[0]).strip().lower() != "bug"]
    r["sheet_rows"] = len(body); r["header"] = hdr[:1]
    sides = [x for x in body if "sides of event icons" in str(x[0]).lower()]
    tav = [x for x in body if "tavern buttons" in str(x[0]).lower()]
    r["sides_row"] = sides[:1]; r["tavern_row"] = tav[:1]
    r["shares"] = sorted(i.get("emailAddress", "") for n, i in C if n == "gdrive_share_file")
    rep = [(idx, i) for idx, (n, i) in enumerate(C) if n == "slack_send_message"]
    r["reply_thread"] = [i.get("thread_ts") for _, i in rep]
    last = rep[-1][0] if rep else -1
    r["writes_after_reply"] = [n for n, i in C[last + 1:] if n in WRITE] if rep else "no reply"
    return r
for d in sys.argv[1:]:
    for n in range(1, 7):
        try: x = check(f"{d}/trajectory-run-{n}.json")
        except Exception as e: print(d, n, "ERR", e); continue
        print(d.split('/')[-1], n, json.dumps(x, ensure_ascii=False)[:1500]); print()
