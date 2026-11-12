#!/usr/bin/env python3
"""MODE B forensics helper: what each run wrote (decoded by trajectory_ledger into run_forensics/rev1/<run>/writes.json),
summarised per deliverable so every failed surface slot can be confirmed against the payload. Data only (python -I).
Usage: python3 -I payloads.py <task_dir>   -> hardening_gen/out/payloads.json + a printed summary"""
import json, re, sys, collections
from pathlib import Path
TASK = Path(sys.argv[1]); R = TASK / "Working_Files" / "run_forensics" / "rev1"
RUNS = ["precheck"] + [f"run-{i}" for i in range(1, 7)]
SAMPLE = ["Refrigerator", "Retro TV", "Bathtub", "Iron", "Cactus Plant", "Cone", "Cello", "Trumpet", "Rocket sound", "Explosion sound", "Bow", "Dynamite", "Rolling Pin", "Fly Zapper", "Toy Airplane", "Music Keyboard", "Background music"]
out = {}
for run in RUNS:
    ws = json.load(open(R / run / "writes.json"))
    rec = {"n_writes": len(ws), "by_tool": dict(collections.Counter(w["tool"] for w in ws)), "failed_writes": [(w["event"], w["tool"]) for w in ws if w.get("ok") is False]}
    doc = next((w for w in ws if w["tool"] == "gdocs_create_document"), None)
    body = (doc["input"].get("bodyText") or "") if doc else ""
    for w in ws:
        if w["tool"] in ("gdocs_batch_update", "gdocs_insert_text", "gdocs_append_text"): body += "\n" + json.dumps(w.get("input"), ensure_ascii=False)
    rec["brief_event"] = doc["event"] if doc else None
    rec["brief_len"] = len(body)
    def ctx(word, n=170):
        m = re.search(word, body, re.I)
        return body[max(0, m.start() - 60): m.start() + n].replace("\n", " ") if m else None
    rec["brief"] = {"eight": ctx(r"\bBow\b|\bDynamite\b", 260), "has_bow": bool(re.search(r"\bBow\b", body)), "has_dynamite": bool(re.search(r"\bDynamite\b", body)),
                    "tray": ctx(r"7[- ]slot|seven slots|7 slots"), "lose": ctx(r"\blos[te]\b|\bfail", 200), "music": ctx(r"first (click|tap|interaction)"),
                    "start": ctx(r"3 Nov|Nov(ember)? 3|3rd"), "sound": ctx(r"Rocket sound|rocket", 260), "zombies": ctx(r"Party Girl", 120), "scenario": ctx(r"Scenario 1", 200)}
    rows = []
    for w in ws:
        if w["tool"] in ("gsheets_values_update", "gsheets_values_append", "gsheets_values_batch_update", "gsheets_batch_update_values"):
            rows += w.get("values") or (w.get("input") or {}).get("values") or []
    header = rows[0] if rows else []
    table = {str(r[0]): r for r in rows[1:] if r}
    rec["sheet"] = {"header": header, "rows": len(table), "states": dict(collections.Counter(str(r[3]) if len(r) > 3 else "?" for r in table.values())),
                    "who": dict(collections.Counter(str(r[5]) for r in table.values() if len(r) > 5 and r[5])),
                    "board": dict(collections.Counter(str(r[2]) if len(r) > 2 else "?" for r in table.values())),
                    "sample": {n: table.get(n, ["MISSING"])[1:7] for n in SAMPLE}}
    rec["shares"] = [(str(w.get("file_id"))[-6:], w.get("email"), w.get("role"), w.get("ok")) for w in ws if w["tool"] == "gdrive_share_file"]
    todo = [w.get("issue") for w in ws if w["tool"] == "linear_update_issue" and str(w.get("state") or "").lower() == "todo"]
    other_updates = [(w.get("issue"), w.get("state"), str(w.get("patch"))[:80]) for w in ws if w["tool"] == "linear_update_issue" and str(w.get("state") or "").lower() != "todo"]
    com = [w.get("issue") for w in ws if w["tool"] == "linear_create_comment"]
    rec["tickets"] = {"todo": len(set(todo)), "comments": len(set(com)), "other_updates": other_updates[:5], "todo_ids": sorted(set(todo)), "sample_comment": next((w.get("body") for w in ws if w["tool"] == "linear_create_comment" and w.get("issue") == "DES-367"), None),
                      "comment_ids": sorted(set(com))}
    rec["slack"] = [(w["event"], w.get("channel"), w.get("thread_ts"), (w.get("text") or "")[:900]) for w in ws if w["tool"] == "slack_send_message"]
    out[run] = rec
(TASK / "Working_Files" / "hardening_gen" / "out" / "payloads.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
for run, r in out.items():
    print(f"\n===== {run}: writes {r['n_writes']} {r['by_tool']} failed {r['failed_writes'][:4]}")
    b = r["brief"]; print(f"  brief ev {r['brief_event']} len {r['brief_len']} bow {b['has_bow']} dynamite {b['has_dynamite']} | eight: {b['eight']}")
    print(f"  tray: {b['tray']} | lose: {str(b['lose'])[:150]} | music: {str(b['music'])[:120]}")
    print(f"  sound: {str(b['sound'])[:300]}")
    s = r["sheet"]; print(f"  sheet rows {s['rows']} header {s['header']} states {s['states']} who {s['who']} board {s['board']}")
    for n in ("Refrigerator", "Bathtub", "Cactus Plant", "Cello", "Rocket sound", "Bow", "Dynamite", "Toy Airplane", "Background music"):
        print(f"     {n}: {[str(c)[:60] for c in s['sample'][n]]}")
    print(f"  shares {r['shares']}")
    print(f"  tickets todo {r['tickets']['todo']} comments {r['tickets']['comments']} other {r['tickets']['other_updates']} | DES-367 comment: {str(r['tickets']['sample_comment'])[:160]}")
    for ev, ch, th, t in r["slack"]: print(f"  slack ev {ev} {ch} thread {th}: {t[:420]!r}")
