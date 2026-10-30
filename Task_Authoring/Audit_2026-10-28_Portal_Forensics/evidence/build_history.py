#!/usr/bin/env python3
"""Derive chronological report history and delivered-task matrix from audited sources."""
from pathlib import Path
import json, re, hashlib
from collections import defaultdict
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parent
AUDIT = OUT.parent
ROOT = AUDIT.parents[1]
data = json.loads((OUT / "report_manifest.json").read_text())
groups = defaultdict(list)
for r in data["reports"]:
    groups[r["container"]].append(r)

def order(r):
    aliases = [a["path"] for a in r["aliases"]]
    iterations = [(int(m.group(1)), p) for p in aliases if (m := re.search(r"/iteration_(\d+)", p))]
    p = min(iterations)[1] if iterations else r["path"]
    if iterations:
        major = min(iterations)[0]
    else:
        m = re.search(r"(?:^|/)(\d+)[_A-Za-z]", p)
        major = int(m.group(1)) if m else 0
    suffix = re.findall(r"\((\d+)\)", Path(p).name)
    minor = int(suffix[0]) if suffix else 0
    return major, minor, p

def final_value(r, key):
    for line in r["final_verdict_block"]:
        if line["text"].lower().startswith(key.lower() + ":"):
            return line["text"].split(":", 1)[1].strip()
    return "not stated in final block"

delivery = {
    "task_inputs_TASK_A": {"reviewer": "Reviewer A", "counted": True, "reason": "Named sent ZIP and matched original prompt FAIL", "send": "1a1651bb5faa35cc", "return": "1a165886cf553937"},
    "task_inputs_TASK_B": {"reviewer": "Reviewer B", "counted": True, "reason": "Corrected-address send and matched original prompt FAIL", "send": "1a1651d8ff7b6ec0", "return": "1a16801780280b16"},
    "task_inputs_TASK_C": {"reviewer": "Reviewer C", "counted": True, "reason": "Named sent ZIP and matched original injection FAIL", "send": "1a168c1b9bd234c8", "return": "1a168e821077954f"},
    "task_inputs_TASK_D": {"reviewer": "Reviewer D", "counted": False, "reason": "Genuine returned hardness FAIL belongs to changed scenario; no confirmed reassignment/task binding", "send": "1a1651bb5faa35cc", "return": "1a16ed677b050dd3"},
    "task_inputs_TASK_E": {"reviewer": "Reviewer E", "counted": False, "reason": "Delivered; no returned external report found; active loop cancelled", "send": "1a165b1d2f04e149", "return": None},
}
matrix = []
for group in sorted(set(groups) | set(delivery)):
    rows = groups.get(group, [])
    stages = {}
    for stage in ["injection", "prompt", "hardness", "oe", "rubrics"]:
        stages[stage] = [{"verdict": r["verdict"], "score": final_value(r, "Score"), "execution_status": final_value(r, "Execution status"), "report_sha256": r["sha256"], "evidence": f"{r['path']}:{r['verdict_line']}"} for r in sorted(rows, key=order) if r["stage"] == stage]
    matrix.append({"container": group, "delivery": delivery.get(group, {"counted": False, "reason": "External report exists locally, contributor delivery/canonical ID mapping not verified"}), "unique_reports": len(rows), "has_external_fail": any(r["verdict"] == "FAIL" for r in rows), "stage_history": stages})
(OUT / "task_matrix.json").write_text(json.dumps({"strict_verified_sent_task_fail_count": 3, "definition": "Distinct canonical delivered task IDs with at least one attributable external FAIL; see MAILBOX_PROVENANCE.md", "groups": matrix}, indent=2) + "\n")

doc = ["# Per-task and per-stage verdict history", "", "Source: immutable report exports indexed in `evidence/report_manifest.json`. Only the final overall verdict is shown; findings inside a PASS do not change that verdict. Byte-identical copies count once. These are **84 unique report documents**, not necessarily 84 independent review executions. Reports with PARTIAL status remain visibly PARTIAL.", "", "Ordering uses explicit iteration numbers, or report filename revision suffixes where no iteration folder exists. It is the preserved local sequence, not an invented exact review timestamp. Full reviewed-input hashes and matching local artifact paths are retained in the machine manifest. Report dates, policy versions and clocks remain as stated by the report; inconsistent source clocks are not silently normalized.", "", "## Delivery-qualified count", "", "Three canonical tasks qualify: Reviewer A `...TASK_A`, Reviewer B `...TASK_B`, Reviewer C `...TASK_C`. Reviewer D's different-scenario FAIL stays unbound; Reviewer E has no preserved returned report. Other local report groups have no verified contributor-delivery mapping in this audit. See [mailbox evidence](evidence/MAILBOX_PROVENANCE.md).", ""]
for item in matrix:
    group = item["container"]
    rows = groups.get(group, [])
    doc += [f"## {group}", "", item["delivery"]["reason"] + ".", "", "| Stage | Preserved sequence of overall verdicts |", "|---|---|"]
    for stage, history in item["stage_history"].items():
        seq = " → ".join(h["verdict"] + (" (PARTIAL)" if h["execution_status"].upper() == "PARTIAL" else "") for h in history) or "No original external report preserved"
        doc.append(f"| {stage} | {seq} |")
    if rows:
        doc += ["", "| Order / stage | Overall verdict | Execution status / score as reported | Original evidence | SHA-256 |", "|---|---|---|---|---|"]
        for r in sorted(rows, key=lambda r: (r["stage"], order(r))):
            major, minor, p = order(r)
            label = f"iteration {major}" if "/iteration_" in p else f"filename revision {minor or 'base'}"
            doc.append(f"| {label} / {r['stage']} | {r['verdict']} | {final_value(r, 'Execution status')} / {final_value(r, 'Score')} | `{r['path']}:{r['verdict_line']}` | `{r['sha256'][:12]}` |")
    doc.append("")
(AUDIT / "TASK_VERDICT_HISTORY.md").write_text("\n".join(doc) + "\n")

# Point-in-time canonical-slot observations; missing current files are observations,
# not inferences about who changed them or whether a historical copy operation ran.
snapshot = []
for task_dir in sorted((ROOT / "Task_Authoring").glob("task_inputs*")):
    if not task_dir.is_dir():
        continue
    for name in ["01_Universe_Inject.sql", "04_Prompt.txt", "08_Oracle_Events.md", "09_Rubrics.json"]:
        p = task_dir / name
        row = {"path": str(p.relative_to(ROOT)), "exists": p.is_file()}
        if p.is_file():
            b = p.read_bytes()
            row.update(sha256=hashlib.sha256(b).hexdigest(), bytes=len(b))
        snapshot.append(row)
(OUT / "canonical_slot_snapshot.json").write_text(json.dumps({"observed_utc": datetime.now(timezone.utc).isoformat(), "read_only_observation": True, "slots": snapshot}, indent=2) + "\n")
print(f"Wrote {len(matrix)} task groups and {sum(len(v) for v in groups.values())} report history rows")
