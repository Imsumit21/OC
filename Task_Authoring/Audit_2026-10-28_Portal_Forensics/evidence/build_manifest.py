#!/usr/bin/env python3
"""Read-only source inventory; writes only into this audit's evidence directory."""
from pathlib import Path
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
AUDIT = OUT.parent
REPORT_HEADER = re.compile(r"^#{1,6}\s*FINAL VERDICT:\s*(NON-FAIL|FAIL|PASS)\b", re.M | re.I)
STAGE_NAME = re.compile(r"[0-9a-f]{24}_(0_injection|1_prompt|1a_hardness|2_oe|3_rubric)", re.I)
STAGE_MAP = {"0_injection": "injection", "1_prompt": "prompt", "1a_hardness": "hardness", "2_oe": "oe", "3_rubric": "rubrics"}
PRUNE = {".git", "__pycache__", "node_modules", "support", "Evals", "claude", "HarmonyGames_GitHub", "HarmonyGames_Gmail", "HarmonyGames_Other_Services", AUDIT.name}

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def walk(root):
    import os
    for here, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in PRUNE]
        for name in files:
            yield Path(here) / name

def scope(p):
    rel = p.relative_to(ROOT)
    for part in rel.parts:
        if part.startswith("task_inputs_"):
            return part, part.removeprefix("task_inputs_")
    if rel.parts[0] == "completed_tasks":
        return "/".join(rel.parts[:2]), None
    if rel.parts[0] == "archived task":
        return "/".join(rel.parts[:2]), None
    if "task_inputs-skipped" in rel.parts:
        return "task_inputs-skipped", None
    return "task_inputs", None

def stage_for(p, t):
    m = STAGE_NAME.search(p.name)
    if m:
        return STAGE_MAP[m.group(1).lower()]
    name = p.name.lower()
    for needle, stage in [("hardness", "hardness"), ("injection", "injection"), ("rubric", "rubrics"), ("prompt", "prompt"), ("oe", "oe")]:
        if needle in name:
            return stage
    return "unknown"

artifacts = []
report_files = []
excluded = []
for base in [ROOT / "Task_Authoring", ROOT / "completed_tasks", ROOT / "archived task"]:
    for p in walk(base):
        rel = str(p.relative_to(ROOT))
        name = p.name.lower()
        is_artifact = (p.suffix.lower() == ".sql" and ("inject" in name or name.startswith("01_"))) or (name.startswith("04_") and "prompt" in name and p.suffix.lower() == ".txt") or (name.startswith("08_") and "oracle" in name and p.suffix.lower() == ".md") or (name.startswith("09_") and "rubric" in name and p.suffix.lower() == ".json")
        if is_artifact and (base.name != "Task_Authoring" or any(part.startswith("task_inputs") for part in p.relative_to(base).parts)):
            container, task_id = scope(p)
            artifacts.append({"path": rel, "sha256": digest(p), "bytes": p.stat().st_size, "container": container, "task_id_from_container": task_id})
        if p.suffix.lower() != ".md":
            continue
        t = p.read_text(errors="replace")
        matches = list(REPORT_HEADER.finditer(t))
        if not matches:
            continue
        # These report locations/names preserve imported Portal exports. Locally authored
        # review documents are listed separately, even when they use the same headings.
        imported = bool(STAGE_NAME.search(p.name)) or "/Plateform_reports/" in rel or "/plateform_reports/" in rel or "/eval_reports/" in rel or "/iteration_01/" in rel and p.name in {"injection eval.md", "prompt eval.md"}
        if not imported:
            excluded.append({"path": rel, "sha256": digest(p), "reason": "Local review/sandbox/audit rather than imported Portal export; not included in external verdict totals", "final_verdict_literals": [m.group(1).upper() for m in matches]})
            continue
        lines = t.splitlines()
        container, task_id = scope(p)
        verdict_m = matches[-1]
        verdict_line = t[:verdict_m.start()].count("\n") + 1
        hashes = []
        for line_n, line in enumerate(lines, 1):
            for h in sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", line, re.I))):
                hashes.append({"sha256": h.lower(), "line": line_n, "text": line})
        attempts = sorted(set(re.findall(r"\b[0-9a-f]{24}\b", "\n".join(lines[:45]) + "\n" + p.name)))
        review_context = [{"line": i, "text": line} for i, line in enumerate(lines, 1) if i <= 65 and re.search(r"review.*(?:2026|time|date)|clock|universe|eval.*(?:version|policy|release)", line, re.I)]
        final_block = [{"line": i, "text": lines[i-1]} for i in range(verdict_line, min(verdict_line + 18, len(lines) + 1))]
        report_files.append({"path": rel, "sha256": digest(p), "bytes": p.stat().st_size, "container": container, "task_id_from_container": task_id, "stage": stage_for(p, t), "verdict": verdict_m.group(1).upper(), "verdict_line": verdict_line, "verdict_evidence": lines[verdict_line - 1], "final_verdict_block": final_block, "attempt_or_other_ids_in_header": attempts, "review_context": review_context, "sha256_mentions": hashes})

# Recognize preservation copies by exact bytes even if their filename/location is
# a local sandbox. The source report remains external; authored sandbox reports do not.
known_report_hashes = {r["sha256"] for r in report_files}
still_excluded = []
for row in excluded:
    if row["sha256"] in known_report_hashes:
        original = next(r for r in report_files if r["sha256"] == row["sha256"])
        copy = original.copy()
        copy["path"] = row["path"]
        copy["preservation_copy"] = True
        report_files.append(copy)
    else:
        still_excluded.append(row)
excluded = still_excluded

artifact_by_hash = defaultdict(list)
for a in artifacts:
    artifact_by_hash[a["sha256"]].append(a["path"])
reports_by_hash = defaultdict(list)
for r in report_files:
    reports_by_hash[r["sha256"]].append(r)
reports = []
for h, rows in reports_by_hash.items():
    rows.sort(key=lambda r: ("/received/" not in r["path"], len(r["path"]), r["path"]))
    entry = rows[0].copy()
    entry["aliases"] = [{"path": r["path"], "verdict_line": r["verdict_line"]} for r in rows]
    for mention in entry["sha256_mentions"]:
        mention["local_artifact_matches"] = artifact_by_hash.get(mention["sha256"], [])
    entry["provenance_limit"] = "Preserved imported report; delivery/source identity requires receipt or mailbox evidence. A report verdict applies to its reviewed bytes, not automatically to the current canonical artifact."
    reports.append(entry)
reports.sort(key=lambda r: (r["container"], r["stage"], r["path"]))
summary = Counter((r["stage"], r["verdict"]) for r in reports)
result = {
    "schema_version": 1,
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Imported Portal report exports found in Task_Authoring task directories, completed_tasks, archived task; official skill/tool fixtures and local simulated reviews excluded.",
    "method": "Deduplicate external reports by full SHA-256; only final explicit FINAL VERDICT heading determines verdict. This inventory is not a count of delivered tasks.",
    "report_file_count": len(report_files),
    "unique_report_count": len(reports),
    "unique_report_summary": [{"stage": k[0], "verdict": k[1], "count": v} for k, v in sorted(summary.items())],
    "reports": reports,
}
(OUT / "report_manifest.json").write_text(json.dumps(result, indent=2) + "\n")
(OUT / "artifact_version_manifest.json").write_text(json.dumps({"schema_version": 1, "artifacts": sorted(artifacts, key=lambda a: a["path"]), "limit": "Named SQL/prompt/OE/rubric versions only, excludes tool fixtures, copied Evals/data trees and audit outputs; exact SHA matches do not establish who generated an artifact."}, indent=2) + "\n")
(OUT / "excluded_local_reviews.json").write_text(json.dumps(excluded, indent=2) + "\n")
table = ["# Imported Portal report inventory", "", "Counts below are report documents after byte deduplication, not distinct task deliveries.", "", "| Stage | PASS | NON-FAIL | FAIL |", "|---|---:|---:|---:|"]
for stage in ["injection", "prompt", "hardness", "oe", "rubrics"]:
    table.append(f"| {stage} | {summary[stage, 'PASS']} | {summary[stage, 'NON-FAIL']} | {summary[stage, 'FAIL']} |")
table += ["", f"Imported source files: {len(report_files)}. Unique full SHA-256 reports: {len(reports)}. Named artifact versions hashed: {len(artifacts)}.", "", "| Container | Stage | Verdict | Evidence | Report SHA-256 |", "|---|---|---|---|---|"]
for r in reports:
    table.append(f"| {r['container']} | {r['stage']} | {r['verdict']} | `{r['path']}:{r['verdict_line']}` | `{r['sha256']}` |")
(OUT / "REPORT_INVENTORY.md").write_text("\n".join(table) + "\n")
print(json.dumps({"files": len(report_files), "unique": len(reports), "artifacts": len(artifacts), "summary": result["unique_report_summary"]}, indent=2))
