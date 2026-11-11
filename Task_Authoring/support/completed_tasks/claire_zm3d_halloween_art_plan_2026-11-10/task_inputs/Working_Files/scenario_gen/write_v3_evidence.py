#!/usr/bin/env python3
"""Write Working_Files/00_V3_Authoring_Evidence.json role_reviews.scenario bound to the current design hash.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/scenario_gen/write_v3_evidence.py
Re-run after every edit of 01_Scenario_Design.md (the artifact hash stales the review). Keeps other stages' entries.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
CTX = json.loads((WF / "00_Task_Context.json").read_text())
IDS = json.loads((HERE / "ids.json").read_text())["ids"]
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK.relative_to(ROOT)))

p = subprocess.run([sys.executable, "-B", str(ROOT / "Task_Authoring/tools/stage_gate.py"), "--artifact-hash",
                    str(WF / "01_Scenario_Design.md")], cwd=ROOT, env=ENV, capture_output=True, text=True)
digest = p.stdout.strip().split()[-1] if p.stdout.strip() else ""
if len(digest) != 12:
    raise SystemExit(f"could not read the artifact hash: {p.stdout!r} {p.stderr!r}")

path = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(path.read_text()) if path.exists() else {}
ev["spec_version"] = "V3"
ev["context_hash"] = CTX["context_hash"]
ev.setdefault("role_reviews", {})["scenario"] = {
    "reviewer": "Claude (build lane), scenario stage",
    "rationale": (
        "Claire Morgan is the Art Lead whose team makes Zombie Match 3D's marketing art: Martin Walsh (icon, store "
        "screens, statics) and Marcus Bennett (UA video, end cards) post their store and ad art in #zombie-art and "
        "#zombie_marketing, both channels she is in, and she already ships marketing assets herself (the playable asset "
        "pack for Brian on Sep 24 in D076Y0SDV18). Leonard asking her to own the art side of a seasonal marketing push - "
        "one call per live store surface and ad (Halloween version, refresh first, reuse, skip), reuse of art the studio "
        "owns, makers and due dates against the release cut and the UA flight, the call on each ad's ART ticket, makers "
        "assigned, tickets for new store art and the links before Thursday's review - is an Art Lead's planning and "
        "authoring work for Marketing and GTM, not engineering or UA buying. Every relied-on record is dated before "
        "2025-10-01T00:00Z; every scoped record is visible to her (persona_view YES, or a planned seed in a channel, "
        "mailbox, calendar or share she has); the writes need no admin rights: she creates and shares her own doc and "
        "sheet, Linear is unscoped and she is an ART team member, and she replies in a channel she is in."),
    "artifact": "01_Scenario_Design.md",
    "artifact_hash": digest,
    "persona_role": CTX["persona_role"],
    "source_ids": [
        f"slack:{IDS['slack_ask']['locator']}",
        "slack:C08R8CHB0QL/1759247618.321069",
        "slack:C08R8CHB0QL/1758121809.236839",
        "slack:D076Y0SDV18/1758716854.737049",
        "slack:C06DJBJL798/1756914854.743319",
        "slack:C06DJBJL798/1755114007.441789",
        "slack:C0880U9751A/1753820524.488479",
        f"gsheets:{IDS['sheet_live']}",
        f"gdocs:{IDS['doc_release']}",
        f"gslides:{IDS['deck_seasonal']['presentation']}",
        f"gmail:{IDS['gmail_fred_plan']['msg']}",
        "linear:ART-774",
        "linear:ART-793",
    ],
}
path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
print("role_reviews.scenario bound to", digest)
