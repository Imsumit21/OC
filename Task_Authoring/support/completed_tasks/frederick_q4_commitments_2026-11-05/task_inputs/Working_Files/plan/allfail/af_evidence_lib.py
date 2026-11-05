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
