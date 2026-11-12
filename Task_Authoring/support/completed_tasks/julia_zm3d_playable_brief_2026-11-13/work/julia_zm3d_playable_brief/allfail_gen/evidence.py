#!/usr/bin/env python3
"""Per-run evidence for the all-fail rows (stage 11). Reads the six exports in 07_Baseline_Trajectories (the batch
bound to the verifier in Working_Files/verifier_binding.json) and the task model; writes allfail_gen/out/evidence.json.
Event numbers are 0-based indexes into the export's event list (the trajectory_ledger convention, event_base 0)."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent; TASK = WF.parent
sys.path.insert(0, str(WF / "oe_gen"))
import model as M  # noqa: E402

CLS = {l["ticket"]: l["cls"] for l in M.LINES}
NAME = {l["ticket"]: l["name"] for l in M.LINES}
TICKET = {l["name"]: l["ticket"] for l in M.LINES}
OWED = {l["ticket"] for l in M.LINES if l["state"] == "Owed"}
DECIDERS = {   # label -> (record id, a phrase only that record's text carries)
    "A1 Marcus's post C0880U9751A/1758906517.912099": "are the text kind",
    "A2 Robert's note D05GU6L0XFH/1759178332.042459": "redoing the UVs on the bathroom objects",
    "C4 Brian's log f_faf4d7c167d14a1127dcc3": "got cut off on upload",
    "C2 Calvin's sheet f_b2387e31d46d3a7b3fa2a9": "Soundly library",
    "C1 Brian's log, recoloured models sent again": "sent the three recoloured models again",
    "C1 Robert's recolour message": None,   # filled below from the SQL
    "notes f_8c1d0bca1d1d5fde4c5008": "State is one of three words",
    "PlayableX format rule C08H78VJG80/1758022459.227279": "exported in *Binary format",
}

def blocks(ev):
    msg = ev.get("message") if isinstance(ev, dict) else None
    c = msg.get("content") if isinstance(msg, dict) else None
    return c if isinstance(c, list) else []

def text_of(x):
    if isinstance(x, str): return x
    if isinstance(x, list): return "\n".join(text_of(i) for i in x)
    if isinstance(x, dict): return "\n".join(text_of(v) for v in x.values())
    return "" if x is None else str(x)

def run(n):
    path = TASK / "07_Baseline_Trajectories" / f"trajectory-run-{n}.json"
    events = json.loads(path.read_text())
    uses, results, says = {}, {}, []
    for i, ev in enumerate(events):
        for b in blocks(ev):
            if not isinstance(b, dict): continue
            if b.get("type") == "tool_use":
                uses[b["id"]] = (i, b.get("name", ""), b.get("input") or {}, bool(ev.get("parent_tool_use_id")))
            elif b.get("type") == "tool_result":
                results[b.get("tool_use_id")] = (i, text_of(b.get("content")), bool(b.get("is_error")))
            elif b.get("type") == "text" and ev.get("type") == "assistant":
                says.append((i, b.get("text", "")))
    moves, comments, dm, sheet, other_state = [], [], [], None, []
    for uid, (i, name, inp, sub) in sorted(uses.items(), key=lambda kv: kv[1][0]):
        res = results.get(uid, (None, "", True))
        short = name.split("__")[-1]
        if short == "linear_update_issue":
            issue = inp.get("id") or inp.get("issueId") or inp.get("issue") or ""
            st = inp.get("state") or inp.get("stateId") or inp.get("status") or ""
            rec = {"event": i, "result_event": res[0], "ticket": issue, "state": st, "ok": not res[2]}
            (moves if str(st).lower() == "todo" else other_state).append(rec)
        elif short == "linear_create_comment":
            comments.append({"event": i, "ticket": inp.get("issueId") or inp.get("issue") or "", "body": inp.get("body", ""), "ok": not res[2]})
        elif short == "slack_send_message":
            dm.append({"event": i, "result_event": res[0], "channel": inp.get("channel_id") or inp.get("channel"), "thread_ts": inp.get("thread_ts"),
                       "text": inp.get("text") or inp.get("message") or "", "ok": not res[2]})
        elif short in ("gsheets_values_update", "gsheets_values_append", "gsheets_batch_update_values"):
            vals = inp.get("values") or []
            if vals and len(vals) > 50: sheet = {"event": i, "rows": vals}
    seen = {}
    for label, phrase in DECIDERS.items():
        if not phrase: continue
        hits = []
        for uid, (ri, txt, err) in results.items():
            if phrase in txt and uid in uses:
                ui, name, inp, sub = uses[uid]
                hits.append({"call_event": ui, "result_event": ri, "tool": name.split("__")[-1], "input": {k: (v if len(str(v)) < 120 else str(v)[:120]) for k, v in inp.items()}})
        seen[label] = sorted(hits, key=lambda h: h["call_event"])
    by_cls = {}
    for m in moves:
        if m["ok"]: by_cls.setdefault(CLS.get(m["ticket"], "?"), []).append(m["ticket"])
    moved = {m["ticket"] for m in moves if m["ok"]}
    states = {}
    if sheet:
        hdr = sheet["rows"][0]; si = hdr.index("State") if "State" in hdr else None; li = hdr.index("Line") if "Line" in hdr else 0
        for r in sheet["rows"][1:]:
            if si is not None and len(r) > si and r[li] in TICKET: states[TICKET[r[li]]] = r[si]
    sheet_by_cls = {}
    for t, s in states.items(): sheet_by_cls.setdefault(CLS[t], {}).setdefault(s, 0); sheet_by_cls[CLS[t]][s] += 1
    return {"run": n, "file": path.name, "events": len(events),
            "todo_moves": {"count": len(moved), "first_event": min((m["event"] for m in moves), default=None), "last_event": max((m["event"] for m in moves), default=None),
                           "failed_calls": [m for m in moves if not m["ok"]], "by_class": {k: len(v) for k, v in sorted(by_cls.items())},
                           "owed_moved": len(moved & OWED), "not_owed_moved": sorted(NAME[t] + " " + t for t in moved - OWED),
                           "owed_not_moved_by_class": {c: sum(1 for t in OWED - moved if CLS[t] == c) for c in ("A1", "A2", "C4", "C2", "VIS")}},
            "other_state_changes": other_state,
            "sheet": {"event": sheet["event"] if sheet else None, "state_counts": {s: sum(1 for v in states.values() if v == s) for s in sorted(set(states.values()))},
                      "by_class": sheet_by_cls},
            "comments": len([c for c in comments if c["ok"]]),
            "slack_posts": dm, "deciders_seen": seen,
            "says": [(i, t) for i, t in says if re.search(r"text kind|ASCII|UV|cut off|unpack|instrument|recolou?r|Marcus", t)][:40]}

out = {"runs": [run(n) for n in range(1, 7)],
       "truth": {"counts": M.COUNTS, "owed_by_class": {k: len(ls) for k, _h, ls in M.OWED_GROUPS}}}
(HERE / "out" / "evidence.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
for r in out["runs"]:
    tm = r["todo_moves"]
    print(f"run-{r['run']}: events {r['events']} · Todo moves {tm['count']} (events {tm['first_event']}–{tm['last_event']}; by class {tm['by_class']}; "
          f"Owed moved {tm['owed_moved']}; not-Owed moved {tm['not_owed_moved']}; Owed left {tm['owed_not_moved_by_class']}) · failed move calls {len(tm['failed_calls'])} "
          f"· other state changes {len(r['other_state_changes'])}")
    print(f"   sheet event {r['sheet']['event']}: {r['sheet']['state_counts']} · by class {r['sheet']['by_class']}")
    for p in r["slack_posts"]:
        m = re.findall(r"(Delivered|Ready|Owed)\W{0,6}(\d+)|(\d+)\W{0,3}(Delivered|Ready|Owed)", p["text"])
        print(f"   slack event {p['event']} → {p['channel']} thread {p['thread_ts']} ok={p['ok']}: counts {m} | {p['text'][:160]!r}")
    for label, hits in r["deciders_seen"].items():
        print(f"   seen {label}: {[(h['call_event'], h['result_event'], h['tool']) for h in hits][:6]}")
