"""Per run: first event whose tool result contains each deciding record's text, plus related calls."""
import json, re, sys, glob
from pathlib import Path
TI = Path("/home/sumit/Desktop/OC/Task_Authoring/task_inputs")
FILES = {f"run-{i}": f for i, f in enumerate(["trajectory-run-1 (2).json", "trajectory-run-2.json", "trajectory-run-3.json",
                                              "trajectory-run-4.json", "trajectory-run-5.json", "trajectory-run-6.json"], 1)}
PROBES = {
    "fw_waiver": "hold it at no charge until Feb 1",
    "lf_dm": "has to wait until after the raise",
    "sp_note": "sitting this one out",
    "nin_zom": "agreement approver",
    "nin_notice": "Registration Completed",
    "bal_thread": "as soon as we get some bandwidth",
    "review_evt": "Q4 commitments review",
}
def results(path):
    out = []
    for n, ev in enumerate(json.load(open(path))):
        if isinstance(ev, dict) and ev.get("type") == "user":
            for c in (ev.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    txt = c.get("content")
                    txt = json.dumps(txt) if not isinstance(txt, str) else txt
                    out.append((n, c.get("tool_use_id"), txt))
    return out
for run, f in FILES.items():
    res = results(TI / "07_Baseline_Trajectories" / f)
    calls = {json.loads(l)["id"]: json.loads(l) for l in open(TI / f"Working_Files/run_forensics/rev4/baseline/{run}/calls.jsonl")}
    print("==", run, "result events", len(res))
    for k, p in PROBES.items():
        hits = [(n, calls.get(tid, {}).get("tool", "?").replace("mcp__hg__", "")) for n, tid, t in res if p in t.replace("\\'", "'")]
        print(f"  {k}: {hits[:3] if hits else 'NEVER SEEN'}")
    for name, pat in (("slack calls", r"slack_"), ("linear calls", r"linear_")):
        cs = [(c["event"], c["tool"].replace("mcp__hg__", ""), json.dumps(c["input"])[:90]) for c in calls.values() if re.search(pat, c["tool"])]
        print(f"  {name} ({len(cs)}):", cs[:8])
    ns = [(c["event"], c["tool"].replace("mcp__hg__", ""), json.dumps(c["input"])[:80]) for c in calls.values()
          if re.search(r"nintendo|balancy", json.dumps(c["input"]), re.I)]
    print("  nintendo/balancy queries:", ns[:6])
