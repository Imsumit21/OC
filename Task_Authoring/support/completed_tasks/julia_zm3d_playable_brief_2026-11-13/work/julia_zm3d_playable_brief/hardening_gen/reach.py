#!/usr/bin/env python3
"""MODE B forensics helper: for each run and each deciding record, the first event whose tool RESULT carries it, and the
call (tool, input) that returned it. Reads the exports as data only (python -I). Writes hardening_gen/out/reach.json.
Usage: python3 -I reach.py <task_dir>"""
import json, sys, collections
from pathlib import Path
TASK = Path(sys.argv[1])
OUT = TASK / "Working_Files" / "hardening_gen" / "out"
RUNS = {"precheck": TASK / "06_PreCheck_Trajectory" / "trajectory-run-1.json"}
RUNS.update({f"run-{i}": TASK / "07_Baseline_Trajectories" / f"trajectory-run-{i}.json" for i in range(1, 7)})
NEEDLES = {   # label -> (unit, [strings that prove the CONTENT was returned])
 "ask": ("hub", ["what you did for the Dominoes playable"]),
 "notes": ("hub", ["State is one of three words"]),
 "pack_list": ("hub", ["Went out"]),
 "pack_ticket": ("hub", ["kept in Design so it stays off the ZM3D board"]),
 "picks_25sep": ("PICKS", ["For the playable board, the 8"]),
 "PICKS reply (bow swap)": ("PICKS", ["in place of the last one on my list"]),
 "bow_parent": ("PICKS", ["Can we have arrow to go with the bow"]),
 "zpicks": ("hub", ["The 4 zombies: Party Girl"]),
 "EXPORT Marcus (text kind)": ("EXPORT", ["are the text kind"]),
 "formats (Binary, not ASCII)": ("EXPORT", ["not ASCII"]),
 "ARTHOLD Claire DM": ("ARTHOLD", ["banyo objelerinin"]),
 "REVISED Robert new colours": ("REVISED", ["new colored version of cactus"]),
 "REVISED PR462": ("REVISED", ["Objects Revisions and Changes"]),
 "AUDIO Calvin sheet": ("AUDIO", ["Soundly library"]),
 "ZIP Brian log": ("ZIP", ["got cut off on upload"]),
 "deck": ("hub", ["A mix, nothing fixed yet"]),
 "gdd": ("hub", ["the loss screen only appears at zero health"]),
 "hold": ("hub", ["ZM3D playable kickoff with PlayableX"]),
 "contact": ("hub", ["intake@playablex.ai"]),
 "music_rule": ("hub", ["music has to start after first click"]),
 "nov3": ("hub", ["new start date for the game on November 3rd"]),
 "scenario1": ("hub", ["lets go with Scenario 1"]),
 "trello_decoy": ("decoy", ["Parked until Nov 3"]),
 "toy_airplane_build_note": ("other", ["Toy Airplane Redone"]),
}
LISTED = {"ZIP Brian log": ["f_faf4d7c167d14a1127dcc3", "Outgoing folder"], "AUDIO Calvin sheet": ["f_b2387e31d46d3a7b3fa2a9", "ZM3D sound sources"],
          "PICKS reply (bow swap)": ["1758922879.243189"], "EXPORT Marcus (text kind)": ["1758906517.912099"], "ARTHOLD Claire DM": ["1759148152.833779"]}
def text_of(c):
    if isinstance(c, str): return c
    if isinstance(c, list): return "\n".join(text_of(x.get("text") if isinstance(x, dict) and "text" in x else (x.get("content") if isinstance(x, dict) else x)) for x in c)
    return json.dumps(c, ensure_ascii=False) if c is not None else ""
out = {}
for label, path in RUNS.items():
    ev = json.load(open(path))
    calls, order = {}, []
    res = []
    for i, e in enumerate(ev):
        m = e.get("message") if isinstance(e.get("message"), dict) else e
        c = m.get("content") if isinstance(m, dict) else None
        if not isinstance(c, list): continue
        for b in c:
            if not isinstance(b, dict): continue
            if b.get("type") == "tool_use":
                calls[b.get("id")] = {"event": i, "tool": (b.get("name") or "").split("__")[-1], "input": b.get("input"), "sub": bool(e.get("parent_tool_use_id"))}
                order.append(b.get("id"))
            elif b.get("type") == "tool_result":
                res.append((i, b.get("tool_use_id"), text_of(b.get("content"))))
    rec = {"events": len(ev), "tool_calls": len(order), "needles": {}, "listed": {}}
    def norm(s): return s.replace("\\u2019", "’").replace("\\n", "\n")
    for name, (unit, strs) in NEEDLES.items():
        hit = None; n_hits = 0
        for i, tid, t in res:
            if any(s in t or s in norm(t) for s in strs):
                n_hits += 1
                if hit is None:
                    c = calls.get(tid, {})
                    hit = {"event": i, "call_event": c.get("event"), "tool": c.get("tool"), "input": json.dumps(c.get("input"), ensure_ascii=False)[:300], "sub": c.get("sub")}
        rec["needles"][name] = {"unit": unit, "first": hit, "results_with_it": n_hits}
    for name, strs in LISTED.items():
        hit = None
        for i, tid, t in res:
            if any(s in t for s in strs):
                c = calls.get(tid, {})
                hit = {"event": i, "tool": c.get("tool"), "input": json.dumps(c.get("input"), ensure_ascii=False)[:300]}
                break
        rec["listed"][name] = hit
    tools = collections.Counter(calls[t]["tool"] for t in order)
    rec["tools"] = dict(tools.most_common())
    rec["reads"] = [{"event": calls[t]["event"], "tool": calls[t]["tool"], "input": json.dumps(calls[t]["input"], ensure_ascii=False)[:260]} for t in order
                    if calls[t]["tool"] not in ("linear_list_comments", "linear_update_issue", "linear_create_comment", "gdrive_share_file", "linear_save_comment", "linear_save_issue")]
    out[label] = rec
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "reach.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
names = list(NEEDLES)
print(f"{'record':32}" + "".join(f"{l:>10}" for l in RUNS))
for n in names:
    print(f"{n:32}" + "".join(f"{(str(out[l]['needles'][n]['first']['event']) if out[l]['needles'][n]['first'] else '—'):>10}" for l in RUNS))
print("listed only (id or title in a result):")
for n in LISTED:
    print(f"{n:32}" + "".join(f"{(str(out[l]['listed'][n]['event']) if out[l]['listed'][n] else '—'):>10}" for l in RUNS))
print(f"{'tool calls':32}" + "".join(f"{out[l]['tool_calls']:>10}" for l in RUNS))
