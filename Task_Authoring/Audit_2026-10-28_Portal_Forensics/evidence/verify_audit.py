#!/usr/bin/env python3
"""Verify report-source integrity and internal numeric consistency without changing originals."""
from pathlib import Path
import hashlib, json, re
from collections import Counter
from datetime import datetime, timezone

EVIDENCE = Path(__file__).resolve().parent
AUDIT = EVIDENCE.parent
ROOT = AUDIT.parents[1]
manifest = json.loads((EVIDENCE / "report_manifest.json").read_text())
artifact_manifest = json.loads((EVIDENCE / "artifact_version_manifest.json").read_text())
rule_manifest = json.loads((EVIDENCE / "source_rule_manifest.json").read_text())
matrix = json.loads((EVIDENCE / "task_matrix.json").read_text())
errors = []
counts = Counter()
paths = set()
for report in manifest["reports"]:
    counts[report["stage"], report["verdict"]] += 1
    for alias in report["aliases"]:
        path = ROOT / alias["path"]
        paths.add(alias["path"])
        if not path.is_file():
            errors.append(f"Missing original report: {alias['path']}")
            continue
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != report["sha256"]:
            errors.append(f"Changed original report: {alias['path']}")
        lines = raw.decode(errors="replace").splitlines()
        literal = lines[alias["verdict_line"] - 1]
        if not re.search(rf"FINAL VERDICT:\s*{report['verdict']}\b", literal):
            errors.append(f"Verdict source mismatch: {alias['path']}:{alias['verdict_line']}")
for artifact in artifact_manifest["artifacts"]:
    path = ROOT / artifact["path"]
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
        errors.append(f"Artifact changed/disappeared since inventory: {artifact['path']}")
for source in rule_manifest["sources"]:
    path = ROOT / source["path"]
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != source["sha256"]:
        errors.append(f"Rule/tool/provenance source changed since snapshot: {source['path']}")
expected = {(r["stage"], r["verdict"]): r["count"] for r in manifest["unique_report_summary"]}
if dict(counts) != expected:
    errors.append("Stage summary does not match source reports")
if len(manifest["reports"]) != 84 or len(paths) != 91 or sum(r["verdict"] == "FAIL" for r in manifest["reports"]) != 37:
    errors.append("Headline report count mismatch")
qualified = [g for g in matrix["groups"] if g["delivery"]["counted"]]
if len(qualified) != matrix["strict_verified_sent_task_fail_count"] or len(qualified) != 3:
    errors.append("Strict delivered-task count mismatch")
if any(not g["has_external_fail"] for g in qualified):
    errors.append("Counted task without imported FAIL")
if any(r["verdict"] == "FAIL" for r in manifest["reports"] if r["stage"] == "oe"):
    errors.append("OE zero-FAIL claim mismatch")
links_checked = 0
for doc in AUDIT.rglob("*.md"):
    if "/scratch/" in str(doc) or "/oe_scratch/" in str(doc):
        continue
    text = doc.read_text()
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"[a-z]+://", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0].strip("<>")
        path = Path(target) if target.startswith("/") else doc.parent / target
        if not path.exists():
            errors.append(f"Broken deliverable link in {doc.name}: {target}")
        links_checked += 1
result = {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "passed": not errors, "original_report_paths_verified": len(paths), "unique_reports": len(manifest["reports"]), "artifact_versions_verified": len(artifact_manifest["artifacts"]), "rule_tool_provenance_sources_verified": len(rule_manifest["sources"]), "qualified_sent_tasks": len(qualified), "relative_deliverable_links_checked": links_checked, "errors": errors, "method": "Re-read all inventoried original report/artifact/rule source bytes; verify SHA256, final verdict source lines, stage summaries and count matrix; check local Markdown deliverable links. No original writes, gate reruns, SQL or model evaluations."}
(EVIDENCE / "QA_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
