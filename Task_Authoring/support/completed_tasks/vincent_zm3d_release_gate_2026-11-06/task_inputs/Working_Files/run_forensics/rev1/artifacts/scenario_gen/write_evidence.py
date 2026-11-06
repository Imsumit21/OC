#!/usr/bin/env python3
"""Writes Working_Files/00_V3_Authoring_Evidence.json (role_reviews.scenario) bound to the current design hash."""
import json
import subprocess
import sys
from pathlib import Path

TASK = Path(__file__).resolve().parents[2]
WF = TASK / "Working_Files"
ctx = json.loads((WF / "00_Task_Context.json").read_text())
h = subprocess.run([sys.executable, "Task_Authoring/tools/stage_gate.py", "--artifact-hash",
                    str(WF / "01_Scenario_Design.md")], capture_output=True, text=True).stdout.strip().splitlines()[-1]
path = WF / "00_V3_Authoring_Evidence.json"
data = json.loads(path.read_text()) if path.exists() else {}
data.update(spec_version="V3", context_hash=ctx["context_hash"])
data.setdefault("role_reviews", {})["scenario"] = {
    "reviewer": "Claude (build lane), scenario stage",
    "rationale": ("Vincent Parker is the Game Systems Engineer who owns QA for both games: the QA regression runbook "
                  "names him as its owner, he files most ZM bug tickets and he re-tests builds in #zombie-bugs and in "
                  "his DMs with Douglas and Brian. Gating the Sep 30 Zombie Match 3D submission builds (Android "
                  "Submission #135 / iOS Submission #50) is the QA sign-off the runbook and the release checklist "
                  "assign to him: triage every open ZM ticket and every fix since the Sep 22 gate, record the call per "
                  "ticket in his own gate sheet, list blockers on the release ticket, file the failed update-path bug "
                  "and reply in the candidate thread. The work is Engineering Ops analysis and synthesis at the freeze "
                  "(all evidence dated before 2025-10-01T00:00Z), uses only services he can see, and needs no founder "
                  "or admin rights."),
    "artifact": "01_Scenario_Design.md",
    "artifact_hash": h,
    "persona_role": ctx["persona_role"],
    "source_ids": ["confluence:page_qa_runbook", "confluence:page_release_checklist", "confluence:page_cicd_pipeline",
                   "slack:C05433XK267/1759257934.076209", "slack:C05433XK267/1759257812.041449",
                   "slack:C05433XK267/1759268201.182309", "slack:C08R27X0EAH/1758485492.586459",
                   "slack:D079SNE2TL4/1759256193.859279", "slack:D079SNE2TL4/1759269524.769369",
                   "linear:ZOM-562", "linear:ZOM-563", "linear:ZOM-435", "linear:ZOM-473", "linear:ZOM-559",
                   "github:harmonygames-Games/match3d#466", "trello:68d1eb90bef538c7c5c5599d"],
}


def ahash(name):
    f = WF / name if (WF / name).exists() else TASK / name
    return subprocess.run([sys.executable, "Task_Authoring/tools/stage_gate.py", "--artifact-hash", str(f)],
                          capture_output=True, text=True).stdout.strip().splitlines()[-1]


ACCEPTED = [
    "Register: a new tab of the ZM3D Release Gate sheet with one row per in-scope ticket (the 132 keys of solver/truth.json) and its call, plus a BLOCKER row for the new update-path ticket (Leonard's Sep 23 rules: from the next gate on, tickets filed while the gate is running get a row); extra columns, any row order, any tab name, call words in any case",
    "Blocker list in the ZOM-570 description by key, reusing the existing ticket where there is one, plus the new update-path ticket (below Arthur's text or with the description rewritten around it)",
    "One new Linear ticket (team ZOM) for the failed update from store build 1.3.24 to iOS Submission #50 with device, OS and source build; any title and wording",
    "Sign-off as a reply in Arthur's thread C08R27X0EAH/1759263900.484190 (also sent to the channel allowed) calling the candidates not ready / no-go, with or without the blocker keys",
    "Ungraded register rows with a second fair call: ZOM-429 / ZOM-517 FIXED or KNOWN ISSUE ('can't reproduce' on the candidates)",
]
ALTERNATIVES = [
    "Blocker list as a ZOM-570 comment instead of the description: rejected, the prompt asks for the release ticket's description",
    "A top-level #zombie-bugs post instead of a thread reply: rejected, the prompt names Arthur's candidates thread",
    "A new spreadsheet for the register: rejected, the prompt asks for a new tab of the gate sheet",
    "A new ticket for the vendor's boss-fight report: rejected, it maps to the existing ZOM-562 and the reuse rule forbids duplicates",
    "Only Bug-labelled ZOM tickets in the register: rejected, Leonard's rules doc covers every ZM ticket still open, in any team or label",
]
data.setdefault("outcome_reviews", {})["prompt-writing"] = {
    "reviewer": "Claude (build lane), prompt-writing stage",
    "rationale": ("The brief pins four deliverables named in the prompt and the records: the register in a new tab of "
                  "Vincent's gate sheet, the blocker list on the release ticket, one new ticket for the unfiled "
                  "update-path failure and the sign-off reply in Arthur's thread. Each fair alternative was tested "
                  "against the record that settles it (release ticket text, Leonard's rules doc, the reuse comment, "
                  "Leonard's push note); the prompt pins the blocker list to the release ticket's description."),
    "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": ahash("04_Prompt_Writing_Brief.md"),
    "accepted_outcomes": ACCEPTED, "alternatives_considered": ALTERNATIVES}
if (TASK / "04_Prompt.txt").exists() and (WF / "04_Prompt_Check.md").exists():
    data["outcome_reviews"]["prompt-check"] = {
        "reviewer": "Claude (build lane), prompt-check stage",
        "rationale": ("Checked 04_Prompt.txt against the brief: every deliverable has one destination the persona "
                      "knows, and the strongest alternative per deliverable is either accepted (comment vs "
                      "description) or settled by a record (thread reply, new tab, existing-key reuse)."),
        "artifact": "04_Prompt.txt", "artifact_hash": ahash("04_Prompt.txt"),
        "accepted_outcomes": ACCEPTED, "alternatives_considered": ALTERNATIVES}
    data.setdefault("role_reviews", {})["prompt-check"] = {
        "reviewer": "Claude (build lane), prompt-check stage",
        "rationale": ("Vincent Parker owns QA for both games (page_qa_runbook owner line; page_release_checklist "
                      "'Owner: Vincent Parker (QA)') and Arthur's release ticket ZOM-570 assigns him the gate; asking an "
                      "assistant to run the store gate on Arthur's candidates, write the register in his own sheet, list "
                      "blockers, file the unfiled failure and sign off in #zombie-bugs is ordinary work for his role at "
                      "the freeze (all records dated before 2025-10-01T00:00Z)."),
        "artifact": "04_Prompt.txt", "artifact_hash": ahash("04_Prompt.txt"), "persona_role": ctx["persona_role"],
        "source_ids": ["confluence:page_qa_runbook", "confluence:page_release_checklist", "linear:ZOM-570",
                       "slack:C08R27X0EAH/1759263900.484190", "slack:C05433XK267/1759257934.076209",
                       "slack:C05433XK267/1759257812.041449"]}
path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
print("evidence written, scenario hash", h)
