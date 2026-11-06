#!/usr/bin/env python3
"""Assembles Working_Files/01_Grounding_Dossier.md from the record ledger (records.json), the solver truth, the ids
and the pasted tool outputs in research/tool_out/. Run from the workspace root after the tools have been re-run:
    python3 -B Task_Authoring/task_inputs/Working_Files/scenario_gen/build_dossier.py
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
OUT = WF / "research" / "tool_out"
IDS = json.loads((HERE / "ids.json").read_text())
LEDGER = json.loads((HERE / "records.json").read_text())
TRUTH = json.loads((WF / "solver" / "truth.json").read_text())
TRUTH = TRUTH.get("rows", TRUTH)
VINCENT = "vincent.parker@harmonygames.co"


def tool(name: str) -> str:
    txt = (OUT / name).read_text().rstrip("\n").replace("'rejected': []", "'rejected': none").replace(
        "'liveness_dispositions_missing': []", "'liveness_dispositions_missing': none")
    return "```\n" + txt + "\n```\n"


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- generated tables
def ledger_rows():
    rows = []
    for n, r in enumerate(LEDGER, 1):
        carrier = "●" if r["service"] in ("linear", "slack", "gmail", "gdocs", "gsheets", "trello", "github") else "○"
        reach = ("unscoped" if r["service"] in ("linear", "trello", "github", "contacts") else
                 "Vincent's own mailbox / calendar / Drive or a channel he is in" if VINCENT in r["id"] or r["service"] in ("slack", "gdocs", "gsheets", "gdrive") or r["id"].startswith("evt_81e6") else
                 "another attendee's copy (companion, not needed by the run)")
        rows.append([n, r["service"], r["table"] + (" (update)" if r.get("op") == "update" else ""), r["id"],
                     r.get("container", ""), r.get("element", ""), carrier, reach, r.get("role", "")])
    return rows


def facts_rows():
    rows = []
    skip_prefix = ("leonard.hayes@", "brian.foster@", "robert@")
    for r in LEDGER:
        if r["id"].startswith(skip_prefix) or (r["service"] == "gcal" and not r["id"].startswith("evt_81e6")):
            continue
        if r.get("op") == "update" or r["table"] in ("github.github_timeline_events", "gsheets.sheets_sheets"):
            continue
        reach = {"linear": "unscoped (Linear)", "trello": "unscoped (Trello)", "github": "unscoped (GitHub)",
                 "contacts": "unscoped (Contacts)", "gmail": "Vincent's mailbox (INBOX)",
                 "gcal": "Vincent's calendar", "slack": "channel / DM Vincent is a member of",
                 "gdocs": "shared with or owned by Vincent", "gsheets": "shared with or owned by Vincent",
                 "gdrive": "shared with or owned by Vincent"}[r["service"]]
        rows.append([r["id"], "seeded", r.get("element", ""), f"{r.get('author', '')} {r.get('at', '')}", reach,
                     r.get("role", ""), "no"])
    base = [
        ("C05433XK267/1759257812.041449", "iOS Submission #50 job started 2025-09-30T18:43:32Z (Arthur)", "evidence"),
        ("C05433XK267/1759257934.076209", "Android Submission #135 job started 2025-09-30T18:45:34Z (Arthur)", "evidence"),
        ("C05433XK267/1759259749.259909", "iOS Submission #50 success from main", "evidence"),
        ("C05433XK267/1759263189.219529", "Android Submission #135 success from main, change list", "evidence"),
        ("C05433XK267/1759267266.044859", "Android #2027 started 21:21Z without the season pass fix", "evidence"),
        ("C05433XK267/1759268201.182309", "Android #2028 started 21:36Z by the commit carrying the season pass fix", "overturning evidence"),
        ("C05433XK267/1756826078.213299", "Android Submission #107 from release/1.3.24_HotFix (Sep 2)", "claim met first (T8)"),
        ("C08R27X0EAH/1758409417.505029", "'testflight 39 is the submission candidate' (Arthur, Sep 20)", "decoy (T9)"),
        ("C08R27X0EAH/1758485492.586459", "Leonard: orange juice not selectable, 'Submission blocker' (Sep 21)", "severity example (K11)"),
        ("D079SNE2TL4/1759256193.859279", "Douglas updated prod with the teams / social changes (ZOM-563), 18:16Z", "overturning evidence (T7)"),
        ("D079SNE2TL4/1759269524.769369", "Vincent: 'Yep it works as expected' 21:58Z", "overturning evidence (T7)"),
    ]
    for loc, fact, role in base:
        rows.append([loc, "base", fact, "2025-09", "channel / DM Vincent is a member of", role, "no"])
    for loc, fact, role in [("page_qa_runbook", "update rows mandatory; 'A failure in any UPDATE column blocks the release'", "authority (base)"),
                            ("page_release_checklist", "'file the bug with device / OS / source build'", "format (base)"),
                            ("page_cicd_pipeline", "'CI stops here' · deploy 'Run by hand'", "authority (base)"),
                            ("harmonygames-Games/match3d#466", "ZOM-564 fix merged 2025-09-26T15:14:44Z", "evidence (T15)"),
                            ("ZOM-562", "Orphan items in boss arena (Todo, Bug)", "alias target (T5)"),
                            ("ZOM-435", "User stuck on trophy path (Done 2025-09-22T13:53:29Z)", "claim met first (T3)"),
                            ("ZOM-473", "Endless end screen skippable (Done 2025-09-22T15:11:51Z)", "claim met first (T3b)"),
                            ("ZOM-563", "Teams' lives / frames not working on prod (In Progress)", "claim met first (T7)"),
                            ("ZOM-564", "Free label stays on boosters (Todo)", "claim met first (T15)"),
                            ("68c451141c69fb8af1b4568e", "Trello 'Minor Bugs to Fix' card (partial list)", "decoy (T14)")]:
        rows.append([loc, "base", fact, "-", "unscoped (Confluence / GitHub / Linear / Trello)", role, "re-verify Confluence after regeneration" if loc.startswith("page_") else "no"])
    return rows


def truth_rows():
    keys = ["ZOM-569", "ZOM-567", "ZOM-435", "ZOM-473", "ZOM-562", "ART-793", "DES-313", "ZOM-578", "ZOM-563",
            "ZOM-559", "ZOM-560", "ZOM-481", "ZOM-458", "ZOM-564", "ZOM-506", "ZOM-557", "ZOM-561", "ZOM-513", "ZOM-387"]
    return [[k, TRUTH[k]["call"], TRUTH[k]["build status"], TRUTH[k]["QA result"]] for k in keys]


def main():
    counts = {}
    for v in TRUTH.values():
        counts[v["call"]] = counts.get(v["call"], 0) + 1
    blockers = sorted(k for k, v in TRUTH.items() if v["call"] == "BLOCKER")
    doc = (HERE / "dossier_template.md").read_text()
    repl = {
        "@@LEDGER@@": table(["#", "service", "table", "id", "container", "manifest element", "carrier", "reach path",
                            "discovery role"], ledger_rows()),
        "@@FACTS_HUMAN@@": table(["locator", "base/seeded", "fact", "actor / UTC", "reach path", "role", "re-verify?"],
                                 facts_rows()),
        "@@TRUTH@@": table(["ticket", "call", "build status", "QA result"], truth_rows()),
        "@@COUNTS@@": ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f" ({len(TRUTH)} rows)",
        "@@BLOCKERS@@": ", ".join(blockers) + f" ({len(blockers)})",
        "@@SQL_LINT@@": tool("sql_lint.txt"), "@@BASE_CHECK@@": tool("base_check.txt"),
        "@@BASE_CLAIMS@@": tool("base_claims.txt"), "@@HARDNESS@@": tool("hardness_gate_sql.txt"),
        "@@FACT_CHECK@@": tool("fact_check.txt"), "@@CHECK_SQL@@": tool("check_sql.txt"),
        "@@ORACLE@@": tool("oracle.txt"), "@@MUTATION@@": tool("mutation.txt"), "@@PREFLIGHT@@": tool("preflight.txt"),
        "@@LIVENESS@@": tool("liveness_sql.txt"), "@@FORECAST@@": tool("forecast_inj_summary.txt"),
        "@@HGLINT@@": "```\n" + json.dumps(json.loads((OUT / "hglint.json").read_text()).get("counts")) + "\n```\n",
    }
    for k, v in IDS.items():
        repl[f"@@{k}@@"] = v
    for a, b in repl.items():
        doc = doc.replace(a, b)
    assert "@@" not in doc, doc[doc.index("@@") - 80: doc.index("@@") + 80]
    (WF / "01_Grounding_Dossier.md").write_text(doc)
    print("dossier written:", len(doc.splitlines()), "lines")


if __name__ == "__main__":
    main()
