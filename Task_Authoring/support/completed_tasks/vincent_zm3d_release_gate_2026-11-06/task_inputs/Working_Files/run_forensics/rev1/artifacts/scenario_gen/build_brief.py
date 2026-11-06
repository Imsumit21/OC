#!/usr/bin/env python3
"""Assembles Working_Files/04_Prompt_Writing_Brief.md from brief_template.md, the persona_view search outputs in
research/tool_out/sap/, the solver truth and the ids. Run from the workspace root:
    python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_brief.py
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
SAP = WF / "research" / "tool_out" / "sap"
IDS = json.loads((HERE / "ids.json").read_text())
TRUTH = json.loads((WF / "solver" / "truth.json").read_text())
TRUTH = TRUTH.get("rows", TRUTH)

# (§5 row, label, service, query file, seeded?, first-hit override)
ROWS = [
    (1, "Store release ticket `ZOM-570`", "01_linear", True), (2, "Arthur's candidate post `C08R27X0EAH/1759263900.484190`", "02_slack", True),
    (3, f"Leonard's rules H2 `{IDS['doc_h2']}`", "03_gdrive", True), (4, f"Arthur's build rules H1 `{IDS['doc_h1']}`", "04_gdrive", True),
    (5, f"Sep 2 hotfix doc `{IDS['doc_h1_decoy']}`", "05_gdrive", True), (6, f"July beta-drop doc `{IDS['doc_h2_decoy']}`", "06_gdrive", True),
    (7, f"Gate sheet `{IDS['gate_sheet']}`", "07_gdrive", True),
    (8, "Submission job starts `C05433XK267/1759257934.076209`", "08_slack", False),
    (9, "The post-cut fix `C05433XK267/1759268589.049939`", "09_slack", False),
    (10, "ZOM-569 Done `ZOM-569`", "10_linear", True), (11, "Backend PR approval `harmonygames-Games/match3d-backend#36`", "11_github", True),
    (12, "Arthur's withdrawal `C08R6BF4ENN/1759261800.335275`", "12_slack", True), (13, "CI/CD page `page_cicd_pipeline`", "13_confluence", False),
    (14, "Vincent's #133 pass `C08R27X0EAH/1759140300.935009`", "14_slack", True), (15, "Leonard's Trello re-test `68dc63484a5b2d0a869e758f`", "15_trello", True),
    (16, "Brian's DM re-test `D0770ET1HV2/1759267800.858041`", "16_slack", True), (17, "Brian's green reply `C08R27X0EAH/1759266600.265963`", "17_slack", True),
    (18, f"Update-path log `{IDS['update_log']}`", "18_gdrive", True), (19, "Runbook update rule `page_qa_runbook`", "19_confluence", False),
    (20, "Vendor session notes `vincent.parker@harmonygames.co/1844730396672762606`", "20_gmail", True),
    (21, "Vendor contact `29016e2ba1a844a2509b847b`", "21_contacts", True), (22, "ZOM-562 `ZOM-562`", "22_linear", False),
    (23, "Other-team ZM tickets `ART-793`, `DES-313`", "23_linear", True), (24, "ZOM-563 on prod `D079SNE2TL4/1759269524.769369`", "24_slack", False),
    (25, "Reuse rule `68dc3ef455344e471b1d2ea9`", "25_trello", True), (26, "Per-ticket QA notes `cmt_zom559_1`", "26_linear", True),
    (27, "Leonard's push note `cmt_zom570_1`", "27_linear", True), (28, "Go/no-go `evt_81e6dc4dbfd331f1a6a317`", "28_gcal", True),
]
UNSCOPED = ("linear", "trello", "github", "contacts", "confluence")


def first_hit(lines):
    for ln in lines[2:]:
        ln = ln.strip()
        if not ln.startswith("{"):
            continue
        try:
            d = json.loads(ln)
        except ValueError:
            continue
        if d.get("id"):
            return f"`{d['id']}`"
        if d.get("pointer"):
            return f"`{d.get('service_file')} {d['parent_pointer'] if d.get('parent_pointer') else d['pointer']}`"
    return None


def main():
    table = ["| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    pastes = []
    for n, label, fname, seeded in ROWS:
        txt = (SAP / f"{fname}.txt").read_text()
        lines = txt.splitlines()
        head = lines[0] if lines else ""
        m = re.match(r"SEARCH (\w+) (['\"])(.*)\2 as", head)
        svc, query = (m.group(1), m.group(3)) if m else (fname.split("_")[1], "?")
        vm = re.search(r"visible hits=(\d+) \(showing (\d+)\)\s+hidden by ACL=(\S+) in (\d+) containers", txt)
        vis = f"{vm.group(1)} (showing {vm.group(2)})" if vm else "?"
        hid = (f"{vm.group(3)} in {vm.group(4)} containers" if vm and vm.group(3) != "None" else "not scanned (--no-hidden)")
        fh = first_hit(lines)
        svc_cell = svc + (" — unscoped (not ACL-scoped)" if svc in UNSCOPED else "")
        if fh and not seeded:
            found = f"YES — base record {fh}"
        elif fh and seeded:
            found = f"YES — base neighbours ({fh}); the seeded record itself is in the SQL overlay (check-sql YES), routed"
        else:
            found = "NO in base search — seeded by /create-injection (check-sql YES); routed"
        table.append(f"| {n} · {label} | {svc_cell} | `{query}` | {vis} | {hid} | {fh or '— (0 hits)'} | {found} |")
        keep = [lines[0], lines[1]] + [ln[:300] for ln in lines[2:5]] if len(lines) > 1 else lines
        pastes.append(f"§5 row {n} — {svc} — `{query}`\n\n```\n" + "\n".join(keep) + "\n```\n")
    blockers = sorted(k for k, v in TRUTH.items() if v["call"] == "BLOCKER")
    out = WF / "research" / "tool_out"
    doc = (HERE / "brief_template.md").read_text()
    repl = {"@@SAP_TABLE@@": "\n".join(table), "@@SAP_PASTES@@": "\n".join(pastes),
            "@@BLOCKERS@@": ", ".join(blockers) + f" ({len(blockers)})",
            "@@SQLSHA@@": hashlib.sha256((TASK / "01_Universe_Inject.sql").read_bytes()).hexdigest()[:12],
            "@@COLLISIONS@@": (out / "collisions_head.txt").read_text().rstrip("\n"),
            "@@RESOLVE@@": (out / "resolve.txt").read_text().rstrip("\n")}
    for k, v in IDS.items():
        repl[f"@@{k}@@"] = v
    for a, b in repl.items():
        doc = doc.replace(a, b)
    assert "@@" not in doc, doc[doc.index("@@") - 60: doc.index("@@") + 60]
    (WF / "04_Prompt_Writing_Brief.md").write_text(doc)
    print("brief written:", len(doc.splitlines()), "lines;", len(blockers), "blockers")


if __name__ == "__main__":
    main()
