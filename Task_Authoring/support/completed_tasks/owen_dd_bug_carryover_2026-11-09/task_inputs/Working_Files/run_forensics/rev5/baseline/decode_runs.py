#!/usr/bin/env python3
"""Decodes every write in the pre-check and six baseline exports and compares it with solver/truth.json, item by item."""
import json, sys, re, collections, os
HERE = os.path.dirname(os.path.abspath(__file__)); W = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
truth = json.load(open(os.path.join(W, "solver", "truth.json")))
norm = lambda s: re.sub(r"[^a-z0-9]+", "", re.sub(r"<[^>]*>|:[a-z_]+:|\[2231\]|[☑☐]", "", (s or "").lower()))
bugs = {k: v for k, v in truth.items() if not re.match(r"ENG-\d+$", k)}
kids = {k: v for k, v in truth.items() if re.match(r"ENG-\d+$", k)}
STATE = {"Fixed": "Done", "Gone": "Canceled", "Broken": "Bugs"}
def events(path):
    raw = open(path).read()
    try:
        d = json.loads(raw); return d if isinstance(d, list) else d.get("events") or d.get("messages") or [d]
    except Exception:
        return [json.loads(l) for l in raw.splitlines() if l.strip().startswith("{")]
def decode(path):
    calls = []
    for e in events(path):
        if isinstance(e, dict) and e.get("type") == "assistant":
            for c in (e.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    calls.append((c["name"].split("__")[-1], c.get("input", {})))
    return calls
out = {}
for label, path in [a.split("=", 1) for a in sys.argv[1:]]:
    calls = decode(path)
    creates = [(i.get("title", ""), i.get("state") or i.get("stateId")) for n, i in calls if n == "linear_create_issue"]
    comments = [(i.get("issueId") or i.get("issue_id") or i.get("id"), i.get("body", "")) for n, i in calls if n == "linear_create_comment"]
    updates = {}
    for n, i in calls:
        if n == "linear_update_issue":
            updates[i.get("id") or i.get("issueId")] = i.get("state") or i.get("stateId")
    res = {}
    for k, v in bugs.items():
        nk = norm(v["Bug"])[:60]
        kk = norm(k)
        hit = [s for t, s in creates if nk and (nk[:40] in norm(t) or norm(t)[:40] in nk or (len(kk) > 12 and kk in norm(t)))]
        if v["Outcome"] == "Covered":
            tk = re.search(r"ENG-\d+", v["Why"]).group(0)
            noted = any(iid == tk for iid, b in comments)
            res[k] = ("ok" if noted and not hit else "WRONG", "note" if noted else "-", hit[:1])
        else:
            res[k] = ("ok" if hit and hit[0] == STATE[v["Outcome"]] else "WRONG", STATE[v["Outcome"]], hit[:1])
    kid = {}
    for k, v in kids.items():
        exp = v["Outcome"]
        got = updates.get(k, "(unchanged)")
        if exp == "Held":
            kid[k] = ("ok" if k not in updates else "WRONG", "stay", got)
        elif v["Why"] == "already Done":
            kid[k] = ("ok" if k not in updates or updates[k] == "Done" else "WRONG", "Done", got)
        else:
            kid[k] = ("ok" if updates.get(k) == "Done" else "WRONG", "Done", got)
    lines = collections.Counter(iid for iid, b in comments if iid in kids)
    line310 = sum(1 for iid, b in comments if iid in kids and "0.3.310" in b)
    reply = [i.get("text", "") for n, i in calls if n == "slack_send_message" and i.get("thread_ts")]
    shares = [(i.get("email") or i.get("emailAddress") or i.get("emails") or i.get("recipients"), i.get("role")) for n, i in calls if n == "gdrive_share_file"]
    out[label] = dict(calls=len(calls), creates=len(creates), wrong_bugs={k: r for k, r in res.items() if r[0] != "ok"}, wrong_kids={k: r for k, r in kid.items() if r[0] != "ok"},
                      child_lines=len(lines), child_lines_310=line310, shares=shares, reply=reply[-1][:600] if reply else None)
    print(f"== {label}: calls {len(calls)}, creates {len(creates)}, wrong bugs {len(out[label]['wrong_bugs'])}, wrong children {len(out[label]['wrong_kids'])}, child lines {len(lines)} ({line310} name 0.3.310), shares {shares}")
    for k, r in out[label]["wrong_bugs"].items(): print("   bug", r[0], "expected", r[1], "got", r[2], "|", k[:60])
    for k, r in out[label]["wrong_kids"].items(): print("   child", k, "expected", r[1], "got", r[2])
json.dump(out, open(os.path.join(HERE, "decoded_runs.json"), "w"), indent=1, ensure_ascii=False)
