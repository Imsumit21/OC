#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Check.md from prompt_gen/check_template.md with the prompt's word count, sha256
prefix and text, the brief's digest and the SQL hash. Never edits 04_Prompt.txt.

    python3 -B Task_Authoring/task_inputsN2/Working_Files/prompt_gen/build_check.py
"""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
sys.path.insert(0, str(TASK.parents[1] / "Task_Authoring" / "tools"))
from stage_gate import file_digest  # noqa: E402

prompt = (TASK / "04_Prompt.txt").read_text()
t = (HERE / "check_template.md").read_text()
out = (t.replace("@@WC@@", str(len(prompt.split()))).replace("@@SHA@@", hashlib.sha256(prompt.encode()).hexdigest()[:12])
        .replace("@@BRIEF@@", file_digest(WF / "04_Prompt_Writing_Brief.md"))
        .replace("@@SQL@@", hashlib.sha256((TASK / "01_Universe_Inject.sql").read_bytes()).hexdigest()[:12])
        .replace("@@PROMPT@@", prompt))
assert "@@" not in out
import re


def spans(section, stop, column):
    """every double-quoted fragment in one named column of the section's tables"""
    body = out.split(section)[1].split(stop)[0]
    head, found = None, []
    for line in body.splitlines():
        if not line.startswith("|") or set(line) <= set("| -"):
            continue
        cells = [c.strip() for c in line.strip("|").split(" | ")]
        if head is None or cells[0] in ("#", "Ask (quoted span)", "Brief item (§4 deliverables, §6 triggers)", "Rule"):
            head = cells
            continue
        found += re.findall(r'"([^"]+)"', cells[head.index(column)])
    return found


for span in (spans("## Findings", "## Asks against rev3", "Quoted span") + spans("## Asks against rev3", "## Fair readings", "Ask (quoted span)")
             + spans("### The six rev3 decisions", "## Verification log", "Prompt span that reaches it")
             + spans("## Brief coverage", "## Calibration", 'Present in the prompt (quoted span, or "absent")')):
    assert span == "absent" or span in prompt, span
assert hashlib.sha256(prompt.encode()).hexdigest().startswith("63d7c071"), "04_Prompt.txt changed"
(WF / "04_Prompt_Check.md").write_text(out)
print("wrote 04_Prompt_Check.md", len(out.splitlines()), "lines; prompt", len(prompt.split()), "words")
