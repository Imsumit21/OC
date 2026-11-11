#!/usr/bin/env python3
"""blind_review.py - prepare and record a local rehearsal of the platform's blind reviewer passes (plan RC4, WS5 item 3,
WS2 item 5, decision 4).

LOCAL REHEARSAL — not a platform verdict. Nothing this tool writes is a /prompt, /oe or /rubric result.

Why. The platform's /prompt, /oe and /rubric each end with blind passes run by fresh subagents that see only the
artifact and the data: P1-P4 for the prompt, O1-O3 for Oracle Events, and for the rubric two blind full reviewers
(F2, F3) plus seven single-topic passes (R1-R7), merged without voting (Evals/references/rules/deep_recheck.md,
rubric_flow_v2.md). Locally nothing reproduced them. This tool writes one brief per pass (the platform's own pass
text, read from Evals/ at run time, plus exactly the inputs that pass may see), records each reviewer's JSON reply
bound to the bytes it reviewed, and works out which rows changed between rounds. It never calls a model: the author's
session gives each brief to a fresh subagent and records the reply.

Commands
  plan    --task-dir T --stage prompt|oe|rubric|solver [--round N] [--full] [--write] [--json]
          One brief per pass in T/Working_Files/local_reviews/<stage>/round<N>/brief_<pass>.md, a copy of the inputs
          the passes may see in round<N>/inputs/, and round<N>/manifest.json (artifact sha256, per-row hashes, brief
          hashes, source ranges, scope and in-scope ids). Without --write nothing is written (dry run).
          Round: default is the latest round when nothing was recorded in it yet, else the next one.
          Scope: the first recorded round is `full`. A later round is `changed`: rows whose hash differs from the
          last round that has recorded output (edited or new), rows that had a scored finding there (re-checked
          even when unchanged, as the platform's RECHECK_FLAGGED), rows still in scope from an unfinished round,
          and their direct dependants. A change to a context input (task details, SQL, reference files, friction,
          and the prompt for oe/rubric, the OEs for rubric) makes the round `full` again, as hg_rubric_ledger does.
          --full forces `full`. Passes: every pass in a full round; in a changed round the platform's DELTA set
          (P1-P4; O1-O2 with O3's last inventory carried; R1-R7 without F2/F3).
  record  --task-dir T --stage S --round N --pass P --file OUT.json [--replace] [--json]
          Validate one reviewer reply and store it as round<N>/output_<P>.json. Refused when: not one JSON object;
          wrong pass; artifact_sha256 is not the planned bytes; a finding has no quote, or its quote is not a
          substring of the row, event or sentence it cites; a cited id does not exist; no cited row/event/sentence
          is in this round's scope; an unknown issue type or severity; an empty pass without `checked`.
  summary --task-dir T --stage S [--round N] [--json]
          Passes recorded or missing; every finding merged without voting (same ids and issue type become one entry
          listing every pass); the rehearsal verdict by the platform's aggregation rule for that eval (the rule is
          printed); for `solver` with Working_Files/01_Difficulty_Budget.json, per budget unit whether the cold solver
          opened the deciding record.
  --self-test

Pass table. PASS_TABLE (one constant) names every pass, the source file and line range of each text it is given,
the first line's expected start and a phrase the last line must contain. A range that no longer holds them stops
`plan` with an error naming the file, the line and where the heading is now. Briefs record path, range and sha256.

Direct dependants (heuristic, stated in the manifest):
  rubric  a row whose title shares a tight token (ticket id, record id, email, #channel, anonymised token, figure
          such as 16,428.57) with the title of an edited, new or removed row.
  oe      an event that cites (`OE n`) an edited or new event, or cited a removed one in the last round.
  prompt  the sentences next to an edited, new or removed sentence, and sentences sharing a tight token.
Row identity: rubric rows use the platform's hg_rubric_ledger.row_hash (title, weight, lower-cased category,
justification, evidence, whitespace-normalised). OE events hash their text without the leading `OE n` number.
Prompt sentences hash their whitespace-normalised text.

Solver stage (advisory and unmeasured). One cold-solver brief: the prompt, the persona and clock, local search over
base plus the injected rows; the reply lists the record ids opened and the answer. Its fidelity to the platform agent
is not measured; it never blocks.

Python API (no side effects): evaluate(task_dir, stage, round_no=None) -> the summary object;
plan(task_dir, stage, ..., write=False) and record(...) do the commands.
Exit: 0 PASS or WARN, 1 FAIL, 2 usage error. Stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

TOOL = "blind_review"
VERSION = 1
BANNER = "LOCAL REHEARSAL — not a platform verdict"
MANIFEST_SCHEMA = "blind-review-round-v1"
OUTPUT_SCHEMA = "blind-review-output-v1"
WORK_DIR = "Working_Files"
REVIEW_DIR = "local_reviews"
ASSIGNMENT = "00_Assigments.md"
SQL = "01_Universe_Inject.sql"
REFS = "02_Reference_Files"
FRICTION = "03_Error_Async_Config.txt"
PROMPT = "04_Prompt.txt"
OE = "08_Oracle_Events.md"
RUBRIC = "09_Rubrics.json"
BUDGET = "01_Difficulty_Budget.json"
REGISTER = BUNDLE / "references" / "platform_rule_delta.json"   # platform-only rules seen in stored reports (WS0)
REGISTER_EVAL = {"prompt": "/prompt", "oe": "/oe", "rubric": "/rubric"}
REGISTER_EXCERPT_CHARS = 360
TASK_COPY = "00_Task_Details.txt"
STAGES = ("prompt", "oe", "rubric", "solver")
SEVERITIES = ("Major", "Moderate", "Minor", "PLATFORM", "UNSURE", "INVENTORY")
NOT_SCORED = ("PLATFORM", "UNSURE", "INVENTORY")
PASS_VERDICTS = ("PASS", "NON-FAIL", "FAIL")
SOLVER_VERDICTS = ("DONE", "STOPPED")

_DR = "Evals/references/rules/deep_recheck.md"
_CE = "Evals/references/rules/common_errors.md"
_RF = "Evals/references/rules/rubric_flow_v2.md"
_RULES = "Evals/references/rules/"
_REFS_PASS = (_DR, _CE, "Evals/SEARCH.md", "Evals/references/persona/")
_REFS_FULL = _REFS_PASS + ("Evals/3_Rubrics_Eval.md", _RULES + "rubric_checks.md", _RULES + "rubric_factual_checks.md",
                           _RULES + "rubric_sampling.md", _RULES + "rubric_qc_examples.md", _RF, "Evals/Docs/")
_SEES_PROMPT = ("task", "prompt", "sql", "reference", "friction")
_SEES_RUBRIC = _SEES_PROMPT + ("oe", "rubric")
_DR_HEAD = ("dr.inputs", "dr.defects", "dr.work")


def _pass(pid, topic, runs, texts, sees, refs=_REFS_PASS, artifact=True, whole_set=False):
    return {"id": pid, "topic": topic, "runs": runs, "texts": texts, "sees": sees, "refs": refs,
            "artifact": artifact, "whole_set": whole_set}


# The one table of passes. "ranges": id -> (file under the workspace, first line, last line, the first line starts
# with, the last line contains). "stages": the passes of each stage. runs: "always" (full and changed rounds), "full"
# (full rounds only), "carried" (full rounds; a changed round reuses the last result, because the pass never sees the
# artifact). whole_set: a pass that still runs when rows were only removed (it checks the set, not single rows).
PASS_TABLE = {
    "ranges": {
        "dr.inputs": (_DR, 61, 67, "**Pass inputs.**", "or another pass's findings."),
        "dr.defects": (_DR, 69, 88, "**Known platform defects.**", "token-for-name difference as a factual"),
        "dr.work": (_DR, 90, 96, "**Pass work.**", "and the number of sentences, events or rows it checked."),
        "dr.P1": (_DR, 192, 223, "### P1 · Unique ground truth and clarity", "fork list comes from this."),
        "dr.P2": (_DR, 225, 255, "### P2 · Services, data and access", "one minor inconsistency (NON-FAIL)."),
        "dr.P3": (_DR, 257, 271, "### P3 · Truthfulness and clock", "apostrophes inside quoted strings are doubled."),
        "dr.P4": (_DR, 273, 283, "### P4 · Wording", "clean writing does not (Eval 1 §1.2, §2.7)."),
        "dr.oe": (_DR, 287, 289, "Each OE pass reads the prompt", "route covers it."),
        "dr.O1": (_DR, 291, 310, "### O1 · Accuracy", "a harmless imprecision is `MINOR`."),
        "dr.O2": (_DR, 312, 320, "### O2 · Completeness", "NON-FAIL 3, not a missing step."),
        "dr.O3": (_DR, 322, 334, "### O3 · Open-instruction inventory", "return `none` and the instruction count 0."),
        "dr.rubric": (_DR, 354, 355, "Each rubric pass reads the prompt only", "fills the section 4 line"),
        "dr.R1": (_DR, 357, 363, "### R1 · Overly specific and unauthorized", "only correct value is fine."),
        "dr.R2": (_DR, 365, 372, "### R2 · Incorrect", "`predicted_all_fail` entry."),
        "dr.R3": (_DR, 374, 380, "### R3 · Missing coverage and beyond-prompt rows", "sentence is beyond the prompt."),
        "dr.R4": (_DR, 382, 388, "### R4 · Duplicates, weights and process", "that no Outcome row can see."),
        "dr.R5": (_DR, 390, 395, "### R5 · Overly broad and destination", "place, not the final response."),
        "dr.R6": (_DR, 397, 403, "### R6 · Self-contained", "is the same failure."),
        "dr.R7": (_DR, 405, 414, "### R7 · Atomic", "(fields of one record that the prompt asks for together)."),
        "ce.s2": (_CE, 26, 55, "**The test.**", "cannot mean both close it and only comment."),
        "ce.s3": (_CE, 57, 73, "## 3 · Five lines", "doubled (`don''t`)."),
        "ce.s4": (_CE, 75, 87, "## 4 · One line per outcome", "It must point at the message or the cell."),
        "ce.s66": (_CE, 187, 195, "### 6.6 Tools, step lists, and bolt-ons", "- GOOD:"),
        "ce.s67": (_CE, 197, 203, "### 6.7 Investigation", "- GOOD:"),
        "ce.s68": (_CE, 205, 224, "### 6.8 Clock, assignment, universe, SQL", "inside a quoted string is a 2."),
        "ce.s79": (_CE, 336, 351, "### 7.9 Weights, process, and rows that always fail", "not that defect."),
        "rf.full": (_RF, 48, 61, "   > You are reviewer F<n>, one of three independent full", "rows checked."),
        "rf.scope": (_RF, 100, 114, "## Scope checklist", "noticing."),
    },
    "stages": {
        "prompt": {"eval": "/prompt", "artifact": PROMPT, "unit": "sentence", "passes": (
            _pass("P1", "Unique ground truth and clarity", "always", _DR_HEAD + ("dr.P1", "ce.s2"), _SEES_PROMPT,
                  whole_set=True),
            _pass("P2", "Services, data and access", "always", _DR_HEAD + ("dr.P2", "ce.s3"), _SEES_PROMPT),
            _pass("P3", "Truthfulness and clock", "always", _DR_HEAD + ("dr.P3", "ce.s68"), _SEES_PROMPT),
            _pass("P4", "Wording", "always", _DR_HEAD + ("dr.P4", "ce.s3", "ce.s66", "ce.s67"), _SEES_PROMPT),
        )},
        "oe": {"eval": "/oe", "artifact": OE, "unit": "event", "passes": (
            _pass("O1", "Accuracy", "always", _DR_HEAD + ("dr.oe", "dr.O1"), _SEES_PROMPT + ("oe",)),
            _pass("O2", "Completeness", "always", _DR_HEAD + ("dr.oe", "dr.O2"), _SEES_PROMPT + ("oe",),
                  whole_set=True),
            _pass("O3", "Open-instruction inventory", "carried", _DR_HEAD + ("dr.oe", "dr.O3"), _SEES_PROMPT,
                  artifact=False),
        )},
        "rubric": {"eval": "/rubric", "artifact": RUBRIC, "unit": "row", "passes": (
            _pass("F2", "Full review (reviewer F2)", "full", ("dr.inputs", "dr.defects", "rf.full", "rf.scope"),
                  _SEES_RUBRIC, refs=_REFS_FULL),
            _pass("F3", "Full review (reviewer F3)", "full", ("dr.inputs", "dr.defects", "rf.full", "rf.scope"),
                  _SEES_RUBRIC, refs=_REFS_FULL),
            _pass("R1", "Overly specific and unauthorized", "always", _DR_HEAD + ("dr.rubric", "dr.R1", "ce.s4"),
                  _SEES_RUBRIC),
            _pass("R2", "Incorrect", "always", _DR_HEAD + ("dr.rubric", "dr.R2", "ce.s4"), _SEES_RUBRIC),
            _pass("R3", "Missing coverage and beyond-prompt rows", "always",
                  _DR_HEAD + ("dr.rubric", "dr.R3", "ce.s4"), _SEES_RUBRIC, whole_set=True),
            _pass("R4", "Duplicates, weights and process", "always",
                  _DR_HEAD + ("dr.rubric", "dr.R4", "ce.s4", "ce.s79"), _SEES_RUBRIC, whole_set=True),
            _pass("R5", "Overly broad and destination", "always", _DR_HEAD + ("dr.rubric", "dr.R5", "ce.s4"),
                  _SEES_RUBRIC),
            _pass("R6", "Self-contained", "always", _DR_HEAD + ("dr.rubric", "dr.R6", "ce.s4"), _SEES_RUBRIC),
            _pass("R7", "Atomic", "always", _DR_HEAD + ("dr.rubric", "dr.R7", "ce.s4"), _SEES_RUBRIC),
        )},
        "solver": {"eval": "cold solver", "artifact": PROMPT, "unit": "sentence", "passes": (
            _pass("SOLVER", "Cold solver (advisory, unmeasured)", "full", (),
                  ("persona", "prompt", "sql", "reference", "friction"), refs=("Evals/SEARCH.md",)),
        )},
    },
}

# ---------------------------------------------------------------- platform rules used by `summary`

PROMPT_RULE = ("Eval 1 aggregation (Evals/1_Prompt_Eval.md:1305-1311; deep_recheck.md:135-137): the lowest "
               "sub-dimension decides; any fail-level finding fails the prompt; Minor findings give 3 only on Clarity, "
               "Persona and Originality, Business Function is 3 at worst, Cross-Service Coherence is 3 for one minor "
               "item and fails on two; every other dimension is binary, so a Minor finding there fails too.")
OE_RULE = ("Eval 2 aggregation (Evals/2_Oracle_Events_Eval.md:363-370; hg_oe_review.py:364-368): Completeness and "
           "Accuracy are each 5, 3 or 2; a Major finding (missing step, wrong field) is 2; a Minor, non-action, "
           "final-response or format finding is 3 (format, non-action and final-response never fail); overall is "
           "the lower of the two.")
RUBRIC_RULE = ("Eval 3 aggregation (hg_rubric_qc.py:15-22, 47-83, 262-345): score = min of six dimensions; severity "
               "comes from the issue type (Major or Moderate on any row fails Overall Quality; Minor rows on 5-10% of "
               "rows give 3, over 10% fail); a weight two levels off, or more than 10% of rows one level off, fails "
               "Criteria Weights, any one-level disagreement gives 4; zero Outcome rows fail Category Balance; an "
               "invalid Process row fails and one missing ordering check gives 3, two fail; a non-Agent title fails "
               "and off-pattern Agent titles give 3 up to 10% of rows; a prohibition row fails Negative; two or more "
               "predicted all-fail rows cap the score at 2.")
SOLVER_RULE = "No platform rule: the cold solver is advisory and unmeasured; its result never blocks."
REJECTION_NOTE = ("Every recorded finding stands here. On the platform the main session rejects a finding only when "
                  "its record or quote does not exist or does not say what it claims, it contradicts an explicit QC "
                  "rule or Local Override, or it is a duplicate (rubric_flow_v2.md:69-78; deep_recheck.md:103-112); "
                  "check each cited record yourself before acting on it.")

# Prompt sub-dimensions: key -> (name, kind). kind: binary (5 or fail), banded (Minor = 3), three (never below 3),
# one_minor (one Minor = 3, two fail).
PROMPT_DIMENSIONS = {
    "unique_ground_truth": ("Unique Ground Truth", "binary"),
    "feasibility": ("Feasibility", "binary"),
    "persona_acl": ("Persona ACL Reachability", "binary"),
    "explicit_tool_mention": ("Explicit Tool Mention", "binary"),
    "clarity": ("Prompt Clarity and Specificity", "banded"),
    "contrived": ("Contrived or Unnatural Prompt", "binary"),
    "todays_date": ("Alignment with Today's Date", "binary"),
    "originality": ("Originality / Sample Similarity", "banded"),
    "truthfulness": ("Truthfulness", "binary"),
    "cross_service_requirement": ("Tool Use and Cross-Service Requirement", "binary"),
    "investigation": ("Investigation", "binary"),
    "coherence": ("Coherence (bolt-on)", "binary"),
    "persona": ("Persona", "banded"),
    "business_function": ("Business Function", "three"),
    "competency": ("Assigned Competency", "binary"),
    "task_skill": ("Assigned Task Skill", "binary"),
    "complexity_seeding": ("Complexity Dimensions and Data Seeding", "binary"),
    "data_exists": ("Universe Feasibility (Data Exists)", "binary"),
    "cross_service_coherence": ("Cross-Service Coherence", "one_minor"),
}
PROMPT_ALIASES = {
    "ugt": "unique_ground_truth", "multiple_valid_answers": "unique_ground_truth",
    "prompt_clarity_and_specificity": "clarity", "clarity_and_specificity": "clarity", "major_clarity": "clarity",
    "action_decision_ambiguity": "clarity", "persona_acl_reachability": "persona_acl", "persona_access": "persona_acl",
    "acl": "persona_acl", "tool_mention": "explicit_tool_mention", "contrived_or_unnatural_prompt": "contrived",
    "naturalness": "contrived", "unnatural": "contrived", "wording": "contrived",
    "alignment_with_today_s_date": "todays_date", "today_s_date": "todays_date", "clock": "todays_date",
    "originality_sample_similarity": "originality", "tool_use_and_cross_service_requirement":
    "cross_service_requirement", "tool_use": "cross_service_requirement", "cross_service":
    "cross_service_requirement", "bolt_on": "coherence", "assigned_competency": "competency",
    "assigned_task_skill": "task_skill", "complexity_dimensions_and_data_seeding": "complexity_seeding",
    "complexity": "complexity_seeding", "data_seeding": "complexity_seeding", "universe_feasibility": "data_exists",
    "universe_feasibility_data_exists": "data_exists", "data_missing": "data_exists", "csc": "cross_service_coherence",
}
# OE issue types: key -> (component, cap). cap "Minor": never below 3 whatever the stated severity.
OE_TYPES = {
    "missing_step": ("completeness", None), "missing_write": ("completeness", None),
    "missing_dependency": ("completeness", None), "vague_step": ("completeness", None),
    "missing_recovery": ("completeness", None), "non_action_event": ("completeness", "Minor"),
    "final_response_event": ("completeness", "Minor"), "completeness": ("completeness", None),
    "open_instruction_item": ("completeness", None),
    "wrong_service": ("accuracy", None), "wrong_tool": ("accuracy", None), "wrong_parameter": ("accuracy", None),
    "wrong_identifier": ("accuracy", None), "wrong_expected_data": ("accuracy", None),
    "wrong_qualifier": ("accuracy", None), "invented_trap": ("accuracy", None),
    "unobservable_precision": ("accuracy", None), "after_clock": ("accuracy", None),
    "deferred_write": ("accuracy", None), "persona_inaccessible": ("accuracy", None),
    "forbidden_write": ("accuracy", None), "dependency_cycle": ("accuracy", None), "format": ("accuracy", "Minor"),
    "accuracy": ("accuracy", None),
}
# Rubric issue types: tallied ones carry the platform's fixed severity (hg_rubric_qc.py:15-22); the rest feed one
# dimension each.
RUBRIC_TALLIED = {
    "incorrect": "Major", "unauthorized": "Major", "unobservable": "Major", "non_atomic": "Major",
    "not_self_contained": "Major", "missing_coverage": "Major", "overly_specific": "Major",
    "non_agent_centric": "Major", "overly_broad": "Major", "contradiction": "Major",
    "duplicate": "Moderate", "category": "Moderate", "vague_exemplar": "Moderate", "harmless_specificity": "Minor",
}
RUBRIC_DIMENSION_ONLY = ("weight", "invalid_process", "missing_process_check", "nonstandard_agent_title",
                         "prohibition", "predicted_all_fail")
WEIGHT_LEVELS = (1, 3, 5)

CLOCKS = {"2026-02-14": "2026-02-14 00:00 UTC (normal universe, task date Feb 14, 2026)",
          "2025-10-01": "2025-10-01 00:00 PT (synth-cut universe, task date Oct 1, 2025)"}

# Tight tokens: what makes two rows, events or sentences about the same thing.
TIGHT = re.compile(r"""
    [\w.+-]+@[\w-]+(?:\.[\w-]+)+                 # email
  | \b[A-Z][A-Z0-9]{1,9}-\d{1,6}\b                # ENG-123
  | \bC[0-9A-Z]{8,12}(?:/\d{10}\.\d{6})?\b         # Slack channel id, with ts
  | \b\d{10}\.\d{6}\b                             # Slack ts
  | \b(?:f|d|evt)_[0-9A-Za-z]{6,}\b               # Drive file or folder, calendar event
  | \b[\w.-]+\#\d+\b                              # repo#12
  | \[?PERSON_(?:NAME_)?\d+(?:_NAME)?\]?          # anonymised token
  | \$?\d{1,3}(?:,\d{3})+(?:\.\d+)?               # 1,234 or 16,428.57
  | \$?\d+\.\d+                                   # 500.00
  | \b\d{5,}\b                                    # long numeric id
  | \#[a-z0-9][a-z0-9_-]{2,}                      # #channel
""", re.X)
OE_HEAD = re.compile(r"(?m)^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?[ \t]*OE[ \t]*(\d+)\b")
OE_REF = re.compile(r"\bOE[ \t]*(\d+)\b")
SENTENCE_BREAK = re.compile(r"(?:(?<=[.!?])|(?<=[.!?][\"”’)]))\s+")
SQL_STATEMENT = re.compile(r"(?im)^\s*(?:INSERT|UPDATE|DELETE)\b")


class ReviewError(ValueError):
    """The request cannot be carried out (missing input, moved source range, bad round)."""


# ---------------------------------------------------------------- small helpers

def _sha(data) -> str:
    return hashlib.sha256(data if isinstance(data, bytes) else str(data).encode("utf-8")).hexdigest()


def _ws(text) -> str:
    return " ".join(str(text if text is not None else "").split())


def _loose(text) -> str:
    """Whitespace and typographic quotes normalised: how a quote is matched against the text it cites."""
    table = {"‘": "'", "’": "'", "“": '"', "”": '"', " ": " ", "–": "-", "—": "-"}
    return _ws("".join(table.get(ch, ch) for ch in str(text)))


def _rel(path, base=WS) -> str:
    path = Path(path).resolve()
    try:
        return path.relative_to(Path(base).resolve()).as_posix()
    except ValueError:
        return str(path)


def _key(text) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(text).casefold()).strip("_")


def _slot(task_dir, name) -> Path:
    from stage_gate import slot_path
    return slot_path(task_dir, name)


def _check(cid, status, detail) -> dict:
    return {"id": cid, "status": status, "detail": detail}


def _verdict(checks) -> str:
    states = {c["status"] for c in checks}
    return "FAIL" if "FAIL" in states else "WARN" if "WARN" in states else "PASS"


def _atomic_write(path: Path, data: bytes, what: str) -> None:
    from task_context import refuse_read_only
    refuse_read_only(path, what)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        os.replace(temp, path)
    except BaseException:
        if os.path.lexists(temp):
            os.unlink(temp)
        raise


def _dump(obj) -> bytes:
    return (json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


# ---------------------------------------------------------------- pass texts from Evals/

def stage_passes(stage) -> tuple:
    if stage not in PASS_TABLE["stages"]:
        raise ReviewError(f"unknown stage {stage!r}; use one of {', '.join(STAGES)}")
    return PASS_TABLE["stages"][stage]["passes"]


def load_ranges(ids, root=None) -> dict:
    """Read each range from its file under `root` (default: the workspace) and check its first and last lines.
    Stops with ReviewError naming the file, the line and where the expected heading is now."""
    root = Path(root or WS)
    out, cache = {}, {}
    for rid in ids:
        rel, start, end, starts, contains = PASS_TABLE["ranges"][rid]
        path = root / rel
        if rel not in cache:
            if not path.is_file():
                raise ReviewError(f"pass text {rid}: {rel} not found under {root}; the brief cannot be built")
            raw = path.read_bytes()
            cache[rel] = (raw, raw.decode("utf-8").split("\n"))
        raw, lines = cache[rel]
        first = lines[start - 1] if 0 < start <= len(lines) else None
        last = lines[end - 1] if 0 < end <= len(lines) else None
        if first is None or not first.startswith(starts) or last is None or contains not in last:
            where = [str(i) for i, line in enumerate(lines, 1) if line.startswith(starts)]
            moved = (f"; the expected first line now starts at line {', '.join(where)}" if where
                     else "; the expected first line is no longer in the file")
            got = "missing" if first is None else repr(first[:70])
            raise ReviewError(f"pass text {rid}: {rel}:{start}-{end} no longer holds it (line {start} should start "
                              f"{starts!r}, found {got}; line {end} should contain {contains!r}){moved}. Update "
                              f"PASS_TABLE in blind_review.py after reading the new text; no brief was written.")
        text = "\n".join(lines[start - 1:end])
        out[rid] = {"id": rid, "file": rel, "lines": [start, end], "sha256": _sha(text.encode("utf-8")),
                    "file_sha256": _sha(raw), "text": text}
    return out


def _range_ids(stage) -> list:
    ids = []
    for entry in stage_passes(stage):
        for rid in entry["texts"]:
            if rid not in ids:
                ids.append(rid)
    return ids


# ---------------------------------------------------------------- task inputs

def read_assignment(task_dir) -> dict:
    """The platform assignment block (what the platform saves as task details) and the resolved fields."""
    path = Path(task_dir) / ASSIGNMENT
    if not path.is_file():
        raise ReviewError(f"{ASSIGNMENT} not found in {task_dir}; the briefs need the assignment fields")
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```[^\n]*\n(.*?)```", text, re.S)
    heading = re.search(r"(?im)^#+\s*Platform assignment\s*$", text)
    platform = None
    if heading:
        after = re.findall(r"```[^\n]*\n(.*?)```", text[heading.end():], re.S)
        platform = after[0] if after else None
    if platform is None and blocks:
        platform = blocks[0]
    if not platform or not platform.strip():
        raise ReviewError(f"{ASSIGNMENT} has no fenced assignment block")
    fields = {}
    for block in blocks:
        for line in block.splitlines():
            match = re.match(r"^\s*([a-z_]+):\s+(.+?)\s*$", line)
            if match:
                fields.setdefault(match.group(1), match.group(2))
    block = platform.strip("\n")
    return {"block": block, "fields": fields, "sha256": _sha(_ws(block))}


def _clock(assignment) -> str:
    key = assignment["fields"].get("universe_date_key", "")
    if key in CLOCKS:
        return CLOCKS[key]
    text = assignment["block"]
    if re.search(r"(?i)february\s+14,?\s+2026|2026-02-14|feb\s+14,?\s+2026", text):
        return CLOCKS["2026-02-14"]
    if re.search(r"(?i)october\s+1,?\s+2025|2025-10-01|oct\s+1,?\s+2025", text):
        return CLOCKS["2025-10-01"]
    return assignment["fields"].get("universe_date", "not stated in the assignment")


def read_sql(task_dir):
    path = Path(task_dir) / SQL
    if not path.is_file():
        return None
    raw = path.read_bytes()
    return raw if SQL_STATEMENT.search(raw.decode("utf-8", "replace")) else None


def read_friction(task_dir):
    """The friction picker block when friction is configured, else None (the platform stores picker values)."""
    path = Path(task_dir) / FRICTION
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    for block in re.findall(r"```[^\n]*\n(.*?)```", text, re.S) or [text]:
        match = re.search(r"(?im)^\s*Friction:\s*(.*?)\s*$", block)
        if match:
            return None if match.group(1).strip().casefold() in ("", "none", "no") else block.strip("\n") + "\n"
    return None


def read_refs(task_dir) -> list:
    folder = Path(task_dir) / REFS
    if not folder.is_dir():
        return []
    return [p for p in sorted(folder.iterdir()) if p.is_file() and not p.name.startswith(".")
            and p.name.casefold() != "readme.md"]


# ---------------------------------------------------------------- rows, events, sentences

def tokens_of(text) -> list:
    found = set()
    for match in TIGHT.finditer(str(text)):
        token = match.group(0).strip("[]$").casefold()
        if re.fullmatch(r"[\d,.]+", token):
            token = token.replace(",", "")
        found.add(token)
    return sorted(found)


def prompt_items(text) -> list:
    items = []
    for para in re.split(r"\n\s*\n|\n", text):
        for piece in SENTENCE_BREAK.split(para.strip()):
            piece = piece.strip()
            if piece:
                items.append({"id": f"S{len(items) + 1}", "text": piece, "sha256": _sha(_ws(piece)),
                              "tokens": tokens_of(piece)})
    return items


def oe_items(text) -> list:
    heads = list(OE_HEAD.finditer(text))
    items, seen = [], {}
    pre = text[:heads[0].start()] if heads else text
    if pre.strip():
        items.append({"id": "OE-PRE", "num": 0, "text": pre.strip("\n"), "sha256": _sha(_ws(pre)), "refs": []})
    for index, head in enumerate(heads):
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        block = text[head.start():end].rstrip()
        num = int(head.group(1))
        seen[num] = seen.get(num, 0) + 1
        oid = f"OE {num}" if seen[num] == 1 else f"OE {num}.{seen[num]}"
        body = block[head.end() - head.start():]
        identity = block[:head.start(1) - head.start()] + "#" + body
        items.append({"id": oid, "num": num, "text": block, "sha256": _sha(_ws(identity)),
                      "refs": sorted({int(n) for n in OE_REF.findall(body)} - {num})})
    return items


def read_rubric(raw: bytes) -> list:
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise ReviewError(f"{RUBRIC} is not valid JSON: {exc}")
    if isinstance(data, dict):
        data = data.get("criteria") or data.get("rubric") or []
    if not isinstance(data, list) or not data or not all(isinstance(r, dict) for r in data):
        raise ReviewError(f"{RUBRIC} is not a non-empty array of criteria")
    return data


def _field(row, name) -> str:
    annotations = row.get("annotations") or {}
    if name == "category":
        value = row.get("category", annotations.get("rubric_category", ""))
    else:
        value = row.get(name, annotations.get(name, ""))
    return " ".join(str(value if value is not None else "").split())


def row_hash(row) -> str:
    """Same identity as the platform's Evals/tools/hg_rubric_ledger.py row_hash."""
    graded = {name: _field(row, name) for name in ("title", "weight", "category", "justification", "evidence")}
    graded["category"] = graded["category"].lower()
    return _sha(json.dumps(graded, sort_keys=True, ensure_ascii=False))


def rubric_items(rows) -> list:
    items = []
    for number, row in enumerate(rows, 1):
        fields = {name: _field(row, name) for name in ("title", "category", "weight", "justification", "evidence")}
        # A #channel is the shared destination of many rows (every reply row names it), not a value two rows can
        # cascade or contradict on, so it does not link rubric rows.
        tokens = [t for t in tokens_of(fields["title"]) if not t.startswith("#")]
        items.append({"id": f"R{number}", "sha256": row_hash(row), "title_sha256": _sha(fields["title"]),
                      "fields": fields, "weight": row.get("weight"), "tokens": tokens})
    return items


def artifact_items(stage, raw: bytes) -> list:
    if stage == "rubric":
        return rubric_items(read_rubric(raw))
    text = raw.decode("utf-8", "replace")
    if stage == "oe":
        items = oe_items(text)
        if not any(i["id"] != "OE-PRE" for i in items):
            raise ReviewError(f"{OE} has no `OE n` event headers")
        return items
    items = prompt_items(text)
    if not items:
        raise ReviewError(f"{PROMPT} is empty")
    return items


def _item_texts(stage, item) -> list:
    if stage == "rubric":
        return [v for v in item["fields"].values() if v]
    return [item["text"]]


def _manifest_item(stage, item) -> dict:
    keep = {"id": item["id"], "sha256": item["sha256"]}
    if stage == "rubric":
        keep.update(title_sha256=item["title_sha256"], tokens=item["tokens"])
    elif stage == "oe":
        keep.update(num=item["num"], refs=item["refs"])
    else:
        keep.update(tokens=item["tokens"])
    return keep


# ---------------------------------------------------------------- rounds on disk

def review_dir(task_dir, stage) -> Path:
    return Path(task_dir) / WORK_DIR / REVIEW_DIR / stage


def round_dir(task_dir, stage, number) -> Path:
    return review_dir(task_dir, stage) / f"round{number}"


def rounds(task_dir, stage) -> list:
    folder = review_dir(task_dir, stage)
    if not folder.is_dir():
        return []
    found = []
    for child in folder.iterdir():
        match = re.fullmatch(r"round(\d+)", child.name)
        if match and (child / "manifest.json").is_file():
            found.append(int(match.group(1)))
    return sorted(found)


def load_manifest(task_dir, stage, number) -> dict:
    path = round_dir(task_dir, stage, number) / "manifest.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ReviewError(f"round {number} of {stage} has no readable manifest ({exc})")
    if manifest.get("schema") != MANIFEST_SCHEMA:
        raise ReviewError(f"{_rel(path)} is not a {MANIFEST_SCHEMA} manifest")
    return manifest


def recorded_outputs(task_dir, stage, number) -> dict:
    folder = round_dir(task_dir, stage, number)
    out = {}
    if folder.is_dir():
        for path in sorted(folder.glob("output_*.json")):
            out[path.stem[len("output_"):]] = path
    return out


def _load_output(path) -> dict:
    try:
        stored = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ReviewError(f"{path} is not readable JSON ({exc})")
    if stored.get("schema") != OUTPUT_SCHEMA or not isinstance(stored.get("output"), dict):
        raise ReviewError(f"{path} is not a recorded {OUTPUT_SCHEMA} output")
    return stored


# ---------------------------------------------------------------- the inputs a round was planned on

def gather(task_dir, stage) -> dict:
    """Everything a round needs from the task folder: artifact bytes and items, context hashes, visible inputs."""
    task_dir = Path(task_dir)
    entry = PASS_TABLE["stages"][stage]
    art_path = task_dir / entry["artifact"]
    if not art_path.is_file():
        raise ReviewError(f"{entry['artifact']} not found in {_rel(task_dir)}; nothing to review at the {stage} stage")
    raw = art_path.read_bytes()
    items = artifact_items(stage, raw)
    assignment = read_assignment(task_dir)
    sql = read_sql(task_dir)
    friction = read_friction(task_dir)
    refs = read_refs(task_dir)
    prompt_path = task_dir / PROMPT
    prompt_raw = prompt_path.read_bytes() if prompt_path.is_file() else None
    oe_path = task_dir / OE
    oe_raw = oe_path.read_bytes() if oe_path.is_file() else None
    if stage in ("oe", "rubric") and prompt_raw is None:
        raise ReviewError(f"{PROMPT} not found: the {stage} passes read the prompt")
    context = {"task-details": assignment["sha256"],
               "injection": _sha(sql) if sql else "none",
               "reference": _sha("".join(f"{p.name}:{_sha(p.read_bytes())}\n" for p in refs)) if refs else "none",
               "error-async": _sha(friction) if friction else "none"}
    if stage in ("oe", "rubric"):
        context["prompt"] = _sha(prompt_raw)
    if stage == "rubric":
        context["oe"] = _sha(oe_raw) if oe_raw is not None else "none"
    return {"task_dir": task_dir, "stage": stage, "artifact_name": entry["artifact"], "raw": raw,
            "sha256": _sha(raw), "items": items, "assignment": assignment, "sql": sql, "friction": friction,
            "refs": refs, "prompt_raw": prompt_raw, "oe_raw": oe_raw, "context": context}


def _input_files(g) -> dict:
    """Published path inside round<N>/ -> bytes, for every input any pass of the stage may see."""
    files = {f"inputs/artifact/{g['artifact_name']}": g["raw"],
             f"inputs/{TASK_COPY}": (g["assignment"]["block"] + "\n").encode("utf-8")}
    if g["stage"] in ("oe", "rubric"):
        files[f"inputs/{PROMPT}"] = g["prompt_raw"]
    if g["stage"] == "rubric" and g["oe_raw"] is not None:
        files[f"inputs/{OE}"] = g["oe_raw"]
    if g["sql"]:
        files[f"inputs/{SQL}"] = g["sql"]
    if g["friction"]:
        files[f"inputs/{FRICTION}"] = g["friction"].encode("utf-8")
    for path in g["refs"]:
        files[f"inputs/reference/{path.name}"] = path.read_bytes()
    return files


# ---------------------------------------------------------------- change detection

def _flagged(task_dir, stage, manifest) -> set:
    """Ids that carried a scored finding in a round (the platform's RECHECK_FLAGGED)."""
    flagged = set()
    for path in recorded_outputs(task_dir, stage, manifest["round"]).values():
        try:
            output = _load_output(path)["output"]
        except ReviewError:
            continue
        for finding in output.get("findings") or []:
            if finding.get("severity") in NOT_SCORED:
                continue
            for key in ("row", "event", "span"):
                if key in finding:
                    flagged.update(_ids(finding[key], key) or [])
    return flagged


def _missing_passes(task_dir, stage, manifest) -> list:
    have = recorded_outputs(task_dir, stage, manifest["round"])
    return [p["pass"] for p in manifest.get("passes", []) if p["pass"] not in have]


def classify(stage, items, previous, flagged=(), carried=()) -> dict:
    """Compare the current items with a previous round's manifest items. Returns status per id, removed items and
    direct dependants. `flagged` and `carried` are previous-round ids."""
    prev_items = previous["items"]
    by_sha = {}
    for item in prev_items:
        by_sha.setdefault(item["sha256"], []).append(item)
    current_shas = {i["sha256"] for i in items}
    used, status, match = set(), {}, {}
    for item in items:
        prev = next((p for p in by_sha.get(item["sha256"], []) if p["id"] not in used), None)
        if prev:
            used.add(prev["id"])
            match[item["id"]] = prev["id"]
            status[item["id"]] = ("flagged" if prev["id"] in flagged else "carried" if prev["id"] in carried
                                  else "unchanged")
    for item in items:
        if item["id"] in status:
            continue
        similar = None
        if stage == "rubric":
            similar = next((p for p in prev_items if p["id"] not in used
                            and p.get("title_sha256") == item.get("title_sha256")), None)
        if similar is None:
            similar = next((p for p in prev_items if p["id"] == item["id"] and p["id"] not in used
                            and p["sha256"] not in current_shas), None)
        if similar is not None:
            used.add(similar["id"])
            match[item["id"]] = similar["id"]
            status[item["id"]] = "edited"
        else:
            status[item["id"]] = "new"
    removed = [p for p in prev_items if p["id"] not in used]
    seeds = [i for i in items if status[i["id"]] in ("edited", "new")]
    dependants = set()
    unchanged = [i for i in items if status[i["id"]] == "unchanged"]
    if stage == "oe":
        seed_nums = {i["num"] for i in seeds}
        removed_nums = {p.get("num") for p in removed}
        citing_removed = {p["id"] for p in prev_items if set(p.get("refs") or []) & removed_nums}
        for item in unchanged:
            if set(item["refs"]) & seed_nums or match.get(item["id"]) in citing_removed:
                dependants.add(item["id"])
    else:
        seed_tokens = set()
        for item in seeds:
            seed_tokens.update(item["tokens"])
        for prev in removed:
            seed_tokens.update(prev.get("tokens") or [])
        for item in unchanged:
            if set(item["tokens"]) & seed_tokens:
                dependants.add(item["id"])
        if stage in ("prompt", "solver"):
            position = {i["id"]: n for n, i in enumerate(items)}
            near = set()
            for item in seeds:
                near.update({position[item["id"]] - 1, position[item["id"]] + 1})
            back = {v: k for k, v in match.items()}
            prev_pos = {p["id"]: n for n, p in enumerate(prev_items)}
            for prev in removed:
                for n in (prev_pos[prev["id"]] - 1, prev_pos[prev["id"]] + 1):
                    if 0 <= n < len(prev_items) and prev_items[n]["id"] in back:
                        near.add(position[back[prev_items[n]["id"]]])
            for item in unchanged:
                if position[item["id"]] in near:
                    dependants.add(item["id"])
    for item_id in dependants:
        status[item_id] = "dependant"
    in_scope = [i["id"] for i in items if status[i["id"]] != "unchanged"]
    counts = {}
    for value in status.values():
        counts[value] = counts.get(value, 0) + 1
    return {"status": status, "match": match, "removed": [{"previous_id": p["id"], "sha256": p["sha256"]}
                                                          for p in removed],
            "in_scope": in_scope, "counts": counts}


def _scope(task_dir, stage, g, number, full) -> dict:
    """Decide the round's scope. Returns scope, reason, in_scope, previous round, classification, carried passes."""
    all_ids = [i["id"] for i in g["items"]]
    if stage == "solver":
        return {"scope": "full", "reason": "the cold solver always solves the whole task", "in_scope": all_ids,
                "previous_round": None, "classification": None, "carried": {}}
    previous = None
    for n in reversed([r for r in rounds(task_dir, stage) if r < number]):
        if recorded_outputs(task_dir, stage, n):
            previous = load_manifest(task_dir, stage, n)
            break
    if full:
        reason = "--full asked for"
    elif previous is None:
        reason = "first recorded round of this stage"
    else:
        changed = sorted(k for k in set(g["context"]) | set(previous.get("context") or {})
                         if g["context"].get(k) != (previous.get("context") or {}).get(k))
        missing = _missing_passes(task_dir, stage, previous)
        reason = None
        if changed:
            reason = f"context changed since round {previous['round']} ({', '.join(changed)})"
        elif missing and previous.get("scope") == "full":
            reason = f"round {previous['round']} did not finish (missing {', '.join(missing)})"
    if reason:
        return {"scope": "full", "reason": reason, "in_scope": all_ids,
                "previous_round": previous["round"] if previous else None, "classification": None, "carried": {}}
    flagged = _flagged(task_dir, stage, previous)
    missing = _missing_passes(task_dir, stage, previous)
    carried_ids = set(previous.get("in_scope") or []) if missing else set()
    result = classify(stage, g["items"], previous, flagged, carried_ids)
    carried = {}
    for entry in stage_passes(stage):
        if entry["runs"] == "carried":
            source = (previous.get("carried") or {}).get(entry["id"])
            if entry["id"] in recorded_outputs(task_dir, stage, previous["round"]):
                source = previous["round"]
            if source is not None:
                carried[entry["id"]] = source
    counts = result["counts"]
    parts = ", ".join(f"{k} {counts[k]}" for k in ("edited", "new", "flagged", "carried", "dependant") if counts.get(k))
    reason = (f"changed since round {previous['round']}: {len(result['in_scope'])} of {len(all_ids)} "
              f"{PASS_TABLE['stages'][stage]['unit']}s in scope ({parts or 'none changed'}"
              f"{'; removed ' + str(len(result['removed'])) if result['removed'] else ''})")
    return {"scope": "changed", "reason": reason, "in_scope": result["in_scope"],
            "previous_round": previous["round"], "classification": result, "carried": carried}


def _passes_for(stage, scope) -> list:
    """Full round: every pass. Changed round: the "always" passes (only the whole-set ones when rows were only
    removed), plus a "carried" pass that has no earlier result to carry."""
    entries = stage_passes(stage)
    if scope["scope"] == "full":
        return list(entries)
    chosen = [e for e in entries if e["runs"] == "always"]
    if not scope["in_scope"]:
        removed = (scope["classification"] or {}).get("removed")
        chosen = [e for e in chosen if e["whole_set"]] if removed else []
    uncarried = [e for e in entries if e["runs"] == "carried" and e["id"] not in scope["carried"]]
    return [e for e in entries if e in chosen or e in uncarried]


# ---------------------------------------------------------------- briefs

UNIVERSE_COMMANDS = """\
Run these from the workspace root (the folder that holds Evals/ and Task_Authoring/). They read the task's universe
as the platform tools would; they never write into Evals/:

    python3 Task_Authoring/tools/hg.py --task-dir {task} search inventory
    python3 Task_Authoring/tools/hg.py --task-dir {task} search search <service> "<terms>" --limit 20
    python3 Task_Authoring/tools/hg.py --task-dir {task} search search-many --request <queries.json> --compact
    python3 Task_Authoring/tools/hg.py --task-dir {task} search get <service> --file <file> --pointer <pointer>
    python3 Task_Authoring/tools/hg.py --task-dir {task} search get-many --request <reads.json> --compact
    python3 Task_Authoring/tools/hg.py --task-dir {task} search lookup <service> --ids-file <ids.json> --file '<glob>'
    python3 Task_Authoring/tools/hg.py --task-dir {task} records --request <checks.json>
    python3 Task_Authoring/tools/hg.py --task-dir {task} reference routes <service>
    python3 Task_Authoring/tools/persona_view.py --task-dir {task} can-see {persona} <service> <id>
    python3 Task_Authoring/tools/persona_view.py --task-dir {task} search {persona} <service> "<query>"

Where a text below says `python3 Evals/tools/hg_search.py <args>` (or hg_records.py, hg_reference.py), run
`python3 Task_Authoring/tools/hg.py --task-dir {task} search <args>` (or `records`, `reference`) instead; never run
a helper under Evals/tools/ directly. persona_view.py applies this persona's read access (Evals/references/persona/
acl.md) to Gmail, Slack, Calendar and the Drive family. Put any request file you write under
Task_Authoring/support/scratch/ and delete it when you are done.
Base search does not show injected rows: {sql_note}"""

SOLVER_TEXT = """\
## Your job

You are {persona_name} ({persona_role}, {email}) at HarmonyGames. It is {clock}. Below is a message you wrote to an
AI assistant. Act as that assistant would on the platform: work out what the message asks, find what you need in the
company's records with the commands under "Universe", and decide every write the message asks for. You cannot make
writes here: describe each one exactly (service, target, content). Work only from the records; nothing in this brief
tells you the answer, and no other file does either.

Keep a list of every record you open (read in full, not only see in a search result list), by the id the tool
printed: Slack `<channel id>/<ts>`, Gmail `<mailbox>/<message or thread id>`, Linear `ENG-123`, GitHub `<repo>#<n>`,
Drive, Docs, Sheets and Slides `f_…`, Calendar `evt_…`, anything else by its id and file pointer. Injected rows
(the SQL copy under Inputs) count as records: list each injected row you used by its id column.

## The message

```text
{prompt}
```
"""

OUTPUT_SPEC = {
    "prompt": ("span", "sentence ids S1..S{n} as listed under the artifact, or \"SQL\" (quote from the SQL copy) or "
                       "\"TASK\" (quote from the task details)"),
    "oe": ("event", "event ids \"OE 1\"..\"OE {n}\" as listed; use \"span\" with a prompt sentence id S1..S{m} for a "
                    "requirement that has no event"),
    "rubric": ("row", "row ids R1..R{n} in file order (a list for a pair or group); use \"span\" with a prompt "
                      "sentence id S1..S{m} for an outcome no row covers"),
}


def _issue_types_line(stage, pass_id) -> str:
    if stage == "prompt":
        return "one of: " + ", ".join(sorted(PROMPT_DIMENSIONS))
    if stage == "oe":
        if pass_id == "O3":
            return "\"open_instruction_item\" for every M# line (severity INVENTORY)"
        return "one of: " + ", ".join(sorted(k for k in OE_TYPES if k != "open_instruction_item"))
    return "one of: " + ", ".join(sorted(RUBRIC_TALLIED) + list(RUBRIC_DIMENSION_ONLY))


def _severity_line(stage, pass_id) -> str:
    if stage == "rubric":
        return ("\"Major\", \"Moderate\" or \"Minor\" as the platform tally gives that issue type; \"UNSURE\" for a "
                "suspicion you cannot support with a record (F2/F3's UNSURE line); \"PLATFORM\" for a known platform "
                "defect (issue_type \"PLATFORM:<id>\")")
    if pass_id == "O3":
        return "\"INVENTORY\" for each M# line; \"PLATFORM\" or \"UNSURE\" as below"
    return ("\"Major\" for a fail-level finding (score 1-2, or 2 on /oe), \"Minor\" for a non-fail one (3-4, or 3 "
            "on /oe); \"UNSURE\" for a suspicion you cannot support with a record; \"PLATFORM\" for a known platform "
            "defect (issue_type \"PLATFORM:<id>\")")


def _output_section(stage, entry, g) -> str:
    sha = g["sha256"]
    if stage == "solver":
        example = {"pass": "SOLVER", "artifact_sha256": sha, "opened": ["<record id>", "<record id>"],
                   "answer": "<your final reply to the requester, in full>",
                   "writes": [{"service": "<service>", "target": "<where>", "content": "<what>"}],
                   "verdict": "DONE"}
        return ("## Required output\n\nReturn one JSON object and nothing else:\n\n```json\n"
                + json.dumps(example, indent=1, ensure_ascii=False) + "\n```\n\n"
                "- `opened`: every record you opened, in the order you opened it.\n"
                "- `answer`: the reply you would send.\n- `writes`: every write you would make.\n"
                "- `verdict`: \"DONE\" when you finished, \"STOPPED\" when you could not.\n")
    key, ids = OUTPUT_SPEC[stage]
    n_items = len([i for i in g["items"] if i["id"] != "OE-PRE"])
    n_sent = len(prompt_items(g["prompt_raw"].decode("utf-8", "replace"))) if g["prompt_raw"] else 0
    if stage == "oe" and entry["id"] == "O3":
        key, ids = "span", f"prompt sentence ids S1..S{n_sent} (the open instruction's sentence)"
    ids = ids.format(n=n_items, m=n_sent)
    finding = {key: "<id>", "issue_type": "<type>", "severity": "<severity>",
               "quote": "<exact words copied from the cited item>",
               "evidence": "<record path, id and quoted value, or the quoted rule>", "fix": "<plain fix>"}
    if entry["id"] in ("F2", "F3", "R4"):
        finding["expected_weight"] = "<1, 3 or 5: only for issue_type weight>"
    if entry["id"] == "O3":
        finding["evidence"] = "<source A record path, id and value | source B record path, id and value>"
        finding["fix"] = ""
    example = {"pass": entry["id"], "artifact_sha256": sha, "checked": "<how many items you checked>",
               "findings": [finding], "verdict": "PASS | NON-FAIL | FAIL"}
    return ("## Required output\n\n"
            "Return one JSON object and nothing else. It carries the same content as the line format named in the "
            "platform text above, one finding per line you would have written:\n\n```json\n"
            + json.dumps(example, indent=1, ensure_ascii=False) + "\n```\n\n"
            f"- `artifact_sha256`: exactly `{sha}` (the bytes listed under the artifact).\n"
            f"- `{key}`: {ids}.\n"
            "- `quote`: the exact words of the cited item (a sentence, event or row). A finding without a quote is "
            "dropped.\n"
            f"- `issue_type`: {_issue_types_line(stage, entry['id'])}.\n"
            f"- `severity`: {_severity_line(stage, entry['id'])}.\n"
            "- `evidence`: the record path, id and quoted value behind the finding.\n"
            "- `fix`: a plain description of the fix (it may be empty for an inventory line).\n"
            "- `checked`: the number of sentences, events or rows you checked; required when `findings` is empty.\n"
            "- `verdict`: PASS when you have no finding, FAIL when any finding is fail-level, else NON-FAIL.\n")


def _render_items(stage, g, in_scope, scope) -> str:
    name, sha = g["artifact_name"], g["sha256"]
    lines = [f"## The artifact under review: {name} (sha256 {sha})", ""]
    if stage in ("prompt", "solver"):
        lines += ["```text", g["raw"].decode("utf-8", "replace").rstrip("\n"), "```", "",
                  "Sentence ids for findings:", ""]
        lines += [f"- {i['id']}: {i['text']}" for i in g["items"]]
    elif stage == "oe":
        for item in g["items"]:
            lines += [f"### {item['id']}", "", "````text", item["text"], "````", ""]
    else:
        for item in g["items"]:
            f = item["fields"]
            lines += [f"### {item['id']} · {f['category']} · weight {f['weight']}", "",
                      f"- title: {f['title']}", f"- justification: {f['justification']}",
                      f"- evidence: {f['evidence']}", ""]
    lines.append("")
    if scope == "full":
        lines.append(f"In scope this round: every {PASS_TABLE['stages'][stage]['unit']}.")
    else:
        lines.append("In scope this round: " + (", ".join(in_scope) if in_scope else "none (check the whole set)")
                     + ". The others are unchanged since an earlier round. Check the in-scope items; report a finding "
                       "on another item only when it also involves an in-scope item (a pair, a group, or coverage of "
                       "the whole set).")
    return "\n".join(lines) + "\n"


def register_rules(stage, path=None) -> list:
    """The register's rules for this stage's eval: (id, wording, local_status, one excerpt), sorted by id.

    The local Evals/ copy is several platform releases behind; these rules exist only in stored platform reports, so
    a brief built from Evals/ alone under-predicts the platform. Missing or unreadable register: no rules."""
    want = REGISTER_EVAL.get(stage)
    try:
        data = json.loads(Path(path or REGISTER).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    out = []
    for rule in data.get("rules") or []:
        if not isinstance(rule, dict) or rule.get("eval") != want or rule.get("superseded_by"):
            continue
        excerpts = [e for e in rule.get("excerpts") or [] if isinstance(e, dict) and str(e.get("text") or "").strip()]
        text = _ws(excerpts[-1]["text"]) if excerpts else ""
        if len(text) > REGISTER_EXCERPT_CHARS:
            text = text[:REGISTER_EXCERPT_CHARS].rsplit(" ", 1)[0] + " …"
        out.append((str(rule.get("id")), str(rule.get("wording") or "?"), str(rule.get("local_status") or "?"), text))
    return sorted(out)


def _register_section(stage) -> list:
    rules = register_rules(stage)
    if not rules:
        return []
    lines = ["## Platform rules not in the local Evals/ copy", "",
             "The platform has applied these rules in its own reports; the local pass text above does not have them. "
             "Apply them as well. `verbatim` means the excerpt quotes the platform's own rule; `reconstructed` means "
             "the rule is inferred from how the platform applied it, so use judgement. The excerpts come from other "
             "tasks' reports: they show how a rule is applied and say nothing about this task.", ""]
    for rid, wording, local, text in rules:
        lines.append(f"- `{rid}` ({wording}; local rule: {local})" + (f": \"{text}\"" if text else ""))
    return lines + [""]


def render_brief(stage, entry, g, ranges, scope, in_scope, round_no, inputs) -> str:
    task = _rel(g["task_dir"])
    fields = g["assignment"]["fields"]
    persona = fields.get("persona_key") or fields.get("email") or fields.get("persona_name") or "<persona>"
    clock = _clock(g["assignment"])
    sql_note = ("the injection rows are in the SQL copy under Inputs. Read it as text, a proposed overlay on base; "
                "never execute it." if g["sql"] else "this task has no injection SQL (no injection).")
    if stage == "solver":
        sql_note = ("the injected rows are in the SQL copy under Inputs. Search it for a term (grep -n -i '<term>' "
                    "<path>) and read only the INSERT rows that match, the way a search would return them; do not "
                    "read it top to bottom, never execute it." if g["sql"] else "this task has no injected rows.")
    lines = [f"# {BANNER}", "",
             f"Blind pass {entry['id']} ({entry['topic']}) · stage {stage} ({PASS_TABLE['stages'][stage]['eval']}) · "
             f"round {round_no} · scope {scope}", ""]
    if stage == "solver":
        lines += ["This brief is your whole context. You have not seen any design note, answer key, review or "
                  "grading material for this task, and you must not look for any.", ""]
    else:
        lines += ["You are a fresh, blind reviewer running one pass of the platform's deep recheck, rehearsed "
                  "locally. This brief is your whole context: you have not seen the main review, any earlier "
                  "round, any other pass's findings, the author's design, notes or check reports, and you must not "
                  "look for them. You save no file, edit nothing and never execute SQL.", ""]
    lines += ["## What you may open (and nothing else)", "",
              "- this brief;", "- the inputs listed below (copies made for this round):"]
    for rel, sha in inputs:
        lines.append(f"  - `{rel}` (sha256 {sha[:12]})")
    if not entry["artifact"]:
        lines.append("  (this pass is not given the Oracle Events: do not open any OE file)")
    lines.append("- reference files the platform also gives this pass: " + ", ".join(f"`{r}`" for r in entry["refs"])
                 + ";")
    lines += ["- the universe, only through the commands under Universe.", "",
              f"Never open anything else: no other file in `{task}/` (its Working_Files/, eval_reports/, other rounds "
              f"or passes under `Working_Files/{REVIEW_DIR}/`), no other task folder, nothing under "
              "Task_Authoring/support/ except your own scratch files, Task_Authoring/archived_tasks/, the Evals "
              "input store (the task_inputs folder under Evals/) or any memory or notes file.", ""]
    if "task" in entry["sees"]:
        lines += ["## Task details (the assignment as the platform saves it)", "", "```text",
                  g["assignment"]["block"].strip("\n"), "```", "", f"Clock: {clock}.", f"Persona key for "
                  f"persona_view.py: `{persona}`.", ""]
    if stage == "solver":
        lines += [SOLVER_TEXT.format(persona_name=fields.get("persona_name", persona),
                                     persona_role=fields.get("persona_role", "employee"),
                                     email=fields.get("email", "email not stated"), clock=clock,
                                     prompt=g["raw"].decode("utf-8", "replace").rstrip("\n")), ""]
    injection = (f"Injection SQL: the `{SQL}` copy under the inputs above (sha256 {_sha(g['sql'])[:12]})."
                 if g["sql"] else "No injection: this task has no injection SQL.")
    friction = "the friction copy under the inputs above." if g["friction"] else "none."
    lines += ["## Injection", "", injection, "", "Friction (error and wait configuration): " + friction, ""]
    lines += ["## Universe", "", UNIVERSE_COMMANDS.format(task=task, persona=persona, sql_note=sql_note), ""]
    if stage != "solver" and entry["artifact"]:
        lines.append(_render_items(stage, g, in_scope, scope))
    elif stage != "solver":
        lines += ["## The artifact under review", "",
                  "Not given to this pass (deep_recheck.md: O3 is not given the OE file or any OE text).", ""]
    if entry["texts"]:
        lines += ["## Platform pass text (verbatim from the local Evals/ copy)", ""]
        for rid in entry["texts"]:
            source = ranges[rid]
            text = source["text"]
            if rid == "rf.full":
                text = "\n".join(re.sub(r"^\s*> ?", "", line) for line in text.split("\n"))
                text = text.replace("F<n>", entry["id"])
            lines += [f"### {source['file']}:{source['lines'][0]}-{source['lines'][1]} (sha256 "
                      f"{source['sha256'][:12]})", "", text, ""]
        lines += ["## Local differences from the platform", "",
                  "- The platform text asks for pipe-delimited lines (or `none` with a count). Return the same "
                  "content as the JSON object under Required output instead.",
                  "- Where it names the saved task inputs, read the copies listed above; where it names the Evals "
                  "search helpers, use the commands under Universe.",
                  "- Known platform defects: severity \"PLATFORM\", issue_type \"PLATFORM:<id>\"; they are not scored.",
                  ""]
        lines += _register_section(stage)
    lines.append(_output_section(stage, entry, g))
    return "\n".join(lines).rstrip("\n") + "\n"


# ---------------------------------------------------------------- plan

def _default_round(task_dir, stage) -> int:
    existing = rounds(task_dir, stage)
    if not existing:
        return 1
    last = existing[-1]
    return last if not recorded_outputs(task_dir, stage, last) else last + 1


def plan(task_dir, stage, round_no=None, full=False, write=False, root=None) -> dict:
    """Build the round: briefs, inputs and manifest. Writes only with write=True."""
    task_dir = Path(task_dir)
    stage_passes(stage)
    number = round_no or _default_round(task_dir, stage)
    if number < 1:
        raise ReviewError("--round must be 1 or more")
    target = round_dir(task_dir, stage, number)
    if recorded_outputs(task_dir, stage, number):
        raise ReviewError(f"round {number} of {stage} already has recorded output; plan round {number + 1} instead")
    g = gather(task_dir, stage)
    ranges = load_ranges(_range_ids(stage), root)
    scope = _scope(task_dir, stage, g, number, full)
    passes = _passes_for(stage, scope)
    files = _input_files(g)
    input_list = {rel: _sha(data) for rel, data in files.items()}
    base = target if target.is_absolute() else target.resolve()
    manifest_passes, briefs = [], {}
    for entry in passes:
        visible = []
        for rel, sha in sorted(input_list.items()):
            if rel.startswith("inputs/artifact/") and not entry["artifact"]:
                continue
            if rel == f"inputs/{TASK_COPY}" and "task" not in entry["sees"]:
                continue
            visible.append((_rel(base / rel), sha))
        text = render_brief(stage, entry, g, ranges, scope["scope"], scope["in_scope"], number, visible)
        name = f"brief_{entry['id']}.md"
        briefs[name] = text.encode("utf-8")
        manifest_passes.append({"pass": entry["id"], "topic": entry["topic"], "brief": name,
                                "brief_sha256": _sha(briefs[name]), "sees": list(entry["sees"]),
                                "artifact": entry["artifact"], "inputs": [r for r, _ in visible],
                                "sources": [{k: ranges[rid][k] for k in ("id", "file", "lines", "sha256",
                                                                         "file_sha256")} for rid in entry["texts"]]})
    classification = scope["classification"]
    manifest = {
        "schema": MANIFEST_SCHEMA, "tool": TOOL, "version": VERSION, "banner": BANNER, "stage": stage,
        "round": number, "scope": scope["scope"], "scope_reason": scope["reason"],
        "previous_round": scope["previous_round"], "in_scope": scope["in_scope"],
        "artifact": {"path": g["artifact_name"], "sha256": g["sha256"], "items": len(g["items"])},
        "context": g["context"], "items": [_manifest_item(stage, i) for i in g["items"]],
        "classification": None if classification is None else {
            "status": classification["status"], "removed": classification["removed"],
            "counts": classification["counts"]},
        "carried": scope["carried"], "passes": manifest_passes,
        "inputs": [{"path": rel, "sha256": sha} for rel, sha in sorted(input_list.items())],
        "dependants_rule": {"rubric": "title shares a tight token with an edited, new or removed row",
                            "oe": "cites an edited or new event, or cited a removed one",
                            "prompt": "next to, or shares a tight token with, an edited, new or removed sentence",
                            "solver": "not used: always full"}[stage],
    }
    sources = (f"{len(ranges)} pass texts resolve in the local Evals/ copy ("
               + ", ".join(sorted({Path(r['file']).name for r in ranges.values()})) + ")") if ranges else \
        "no platform text: the solver brief is authored by this tool"
    seen = ["the persona and clock" if stage == "solver" else "the task details", "the prompt",
            "the injection SQL" if g["sql"] else "no injection"]
    if g["refs"]:
        seen.append(f"{len(g['refs'])} reference file(s)")
    if g["friction"]:
        seen.append("the friction config")
    seen += {"oe": ["the OEs (not O3)"], "rubric": ["the OEs" if g["oe_raw"] is not None else "no OEs",
                                                    "the rubric"]}.get(stage, [])
    checks = [_check("plan.sources", "PASS", sources),
              _check("plan.artifact", "PASS", f"{g['artifact_name']} sha256 {g['sha256'][:12]} "
                     f"({len(g['items'])} {PASS_TABLE['stages'][stage]['unit']}s)"),
              _check("plan.inputs", "PASS", "passes see " + ", ".join(seen)),
              _check("plan.scope", "PASS", f"{scope['scope']}: {scope['reason']}")]
    if stage == "solver":
        checks.append(_check("plan.advisory", "PASS", "advisory and unmeasured: the cold solver's fidelity to the "
                             "platform agent is not measured; its result never blocks"))
    if scope["carried"]:
        checks.append(_check("plan.carried", "PASS", ", ".join(f"{k} carried from round {v} (it never sees the "
                                                               "artifact)" for k, v in scope["carried"].items())))
    if not passes:
        checks.append(_check("plan.passes", "PASS", f"nothing changed since round {scope['previous_round']}; no pass "
                             "to run, its result stands"))
    if write:
        files_out = {f"{name}": data for name, data in briefs.items()}
        files_out.update(files)
        files_out["manifest.json"] = _dump(manifest)
        _write_round(target, files_out)
        checks.append(_check("plan.write", "PASS", f"wrote {len(briefs)} brief(s), {len(files)} input copies and "
                             f"manifest.json to {_rel(target)}/"))
    else:
        checks.append(_check("plan.write", "SKIP", "dry run: nothing written; add --write"))
    bound = {g["artifact_name"]: g["sha256"]}
    return {"tool": TOOL, "version": VERSION, "verdict": _verdict(checks), "bound_to": bound, "checks": checks,
            "command": "plan", "stage": stage, "round": number, "scope": scope["scope"],
            "scope_reason": scope["reason"], "in_scope": scope["in_scope"], "written": bool(write),
            "round_dir": _rel(target), "passes": manifest_passes, "manifest": manifest, "banner": BANNER}


def _write_round(target: Path, files: dict) -> None:
    from task_context import refuse_read_only
    refuse_read_only(target, "local review round")
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent)))
    old = None
    try:
        for rel, data in files.items():
            path = temp / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        if target.exists():
            old = Path(tempfile.mkdtemp(prefix=target.name + ".", suffix=".old", dir=str(target.parent)))
            old.rmdir()
            os.replace(target, old)
        os.replace(temp, target)
    except BaseException:
        shutil.rmtree(temp, ignore_errors=True)
        if old is not None and old.exists() and not target.exists():
            os.replace(old, target)
        raise
    if old is not None:
        shutil.rmtree(old, ignore_errors=True)


# ---------------------------------------------------------------- record

def _ids(value, key):
    """Normalised ids for a locator value, or None when the value is not usable."""
    values = value if isinstance(value, list) else [value]
    out = []
    for raw in values:
        if isinstance(raw, bool) or not isinstance(raw, (str, int)):
            return None
        text = str(raw).strip()
        if key == "row":
            match = re.fullmatch(r"(?i)r?\s*(\d+)", text)
            if not match:
                return None
            out.append(f"R{int(match.group(1))}")
        elif key == "event":
            if text.upper() == "OE-PRE":
                out.append("OE-PRE")
                continue
            match = re.fullmatch(r"(?i)(?:oe)?\s*(\d+)(?:\.(\d+))?", text)
            if not match:
                return None
            out.append(f"OE {int(match.group(1))}" + (f".{match.group(2)}" if match.group(2) else ""))
        else:
            if text.upper() in ("SQL", "TASK"):
                out.append(text.upper())
                continue
            match = re.fullmatch(r"(?i)s?\s*(\d+)", text)
            if not match:
                return None
            out.append(f"S{int(match.group(1))}")
    return out or None


def _parse_reply(raw: bytes):
    text = raw.decode("utf-8-sig", "replace").strip()
    fence = re.fullmatch(r"```(?:json)?\s*\n(.*)\n```", text, re.S)
    if fence:
        text = fence.group(1)
    try:
        return json.loads(text), None
    except ValueError as exc:
        return None, f"not one JSON object ({exc})"


def _round_context(task_dir, stage, number) -> dict:
    """The planned bytes of a round, re-parsed from its inputs/ copies (never from the live task files)."""
    manifest = load_manifest(task_dir, stage, number)
    folder = round_dir(task_dir, stage, number)
    art = folder / "inputs" / "artifact" / manifest["artifact"]["path"]
    if not art.is_file() or _sha(art.read_bytes()) != manifest["artifact"]["sha256"]:
        raise ReviewError(f"{_rel(art)} is missing or differs from the bytes round {number} was planned on")
    items = artifact_items(stage, art.read_bytes())
    spans = {}
    prompt_copy = folder / "inputs" / PROMPT
    if stage in ("prompt", "solver"):
        spans = {i["id"]: [i["text"]] for i in items}
    elif prompt_copy.is_file():
        spans = {i["id"]: [i["text"]] for i in prompt_items(prompt_copy.read_text(encoding="utf-8"))}
    sql_copy, task_copy = folder / "inputs" / SQL, folder / "inputs" / TASK_COPY
    if sql_copy.is_file():
        spans["SQL"] = [sql_copy.read_text(encoding="utf-8", errors="replace")]
    if task_copy.is_file():
        spans["TASK"] = [task_copy.read_text(encoding="utf-8")]
    return {"manifest": manifest, "items": {i["id"]: i for i in items}, "spans": spans, "folder": folder}


def _issue_known(stage, issue_type) -> bool:
    key = _key(issue_type)
    if stage == "prompt":
        return key in PROMPT_DIMENSIONS or key in PROMPT_ALIASES
    if stage == "oe":
        return key in OE_TYPES
    return key in RUBRIC_TALLIED or key in RUBRIC_DIMENSION_ONLY


def validate_output(obj, stage, pass_id, rc) -> list:
    """Every reason the reply cannot be recorded (empty when it can)."""
    manifest, items, spans = rc["manifest"], rc["items"], rc["spans"]
    errors = []
    if not isinstance(obj, dict):
        return ["the reply is not one JSON object"]
    if obj.get("pass") != pass_id:
        errors.append(f"`pass` is {obj.get('pass')!r}, expected {pass_id!r}")
    if obj.get("artifact_sha256") != manifest["artifact"]["sha256"]:
        errors.append(f"`artifact_sha256` is {str(obj.get('artifact_sha256'))[:16]!r}; round {manifest['round']} was "
                      f"planned on {manifest['artifact']['sha256'][:16]} (the reviewer saw other bytes)")
    if stage == "solver":
        if obj.get("verdict") not in SOLVER_VERDICTS:
            errors.append(f"`verdict` must be one of {', '.join(SOLVER_VERDICTS)}")
        opened = obj.get("opened")
        if not isinstance(opened, list) or not all(isinstance(o, str) and o.strip() for o in opened):
            errors.append("`opened` must be a list of record ids (strings)")
        if not isinstance(obj.get("answer"), str) or not obj["answer"].strip():
            errors.append("`answer` must be the solver's reply (a non-empty string)")
        if "writes" in obj and not isinstance(obj["writes"], list):
            errors.append("`writes` must be a list")
        return errors
    if obj.get("verdict") not in PASS_VERDICTS:
        errors.append(f"`verdict` must be one of {', '.join(PASS_VERDICTS)}")
    findings = obj.get("findings")
    if not isinstance(findings, list):
        return errors + ["`findings` must be a list (empty when the pass found nothing)"]
    if not findings and (isinstance(obj.get("checked"), bool) or not isinstance(obj.get("checked"), int)
                         or obj["checked"] < 0):
        errors.append("a pass with no findings returns `checked`: the number of items it checked "
                      "(deep_recheck.md: otherwise the pass has not run)")
    in_scope = None if manifest["scope"] == "full" else set(manifest["in_scope"])
    allowed_keys = {"prompt": ("span",), "oe": ("event", "span"), "rubric": ("row", "span")}[stage]
    if pass_id == "O3":
        allowed_keys = ("span",)
    scored = 0
    for n, finding in enumerate(findings, 1):
        where = f"finding {n}"
        if not isinstance(finding, dict):
            errors.append(f"{where}: not an object")
            continue
        keys = [k for k in ("row", "event", "span") if k in finding]
        if len(keys) != 1 or keys[0] not in allowed_keys:
            errors.append(f"{where}: give exactly one locator, one of {', '.join(allowed_keys)}")
            continue
        key = keys[0]
        ids = _ids(finding[key], key)
        if not ids:
            errors.append(f"{where}: `{key}` {finding[key]!r} is not an id")
            continue
        pool = spans if key == "span" else items
        unknown = [i for i in ids if i not in pool]
        if unknown:
            errors.append(f"{where}: {', '.join(unknown)} does not exist in the planned "
                          f"{'prompt' if key == 'span' else manifest['artifact']['path']}")
            continue
        severity = finding.get("severity")
        if severity not in SEVERITIES:
            errors.append(f"{where}: severity {severity!r} is not one of {', '.join(SEVERITIES)}")
        elif severity == "Moderate" and stage != "rubric":
            errors.append(f"{where}: Moderate is a rubric severity; use Major (fail-level) or Minor (non-fail)")
        elif severity == "INVENTORY" and pass_id != "O3":
            errors.append(f"{where}: INVENTORY is only for O3's open-instruction items")
        elif pass_id == "O3" and severity not in NOT_SCORED:
            errors.append(f"{where}: O3 returns inventory items (severity INVENTORY), not scored findings")
        if severity not in NOT_SCORED:
            scored += 1
        if in_scope is not None and severity not in ("PLATFORM", "UNSURE"):
            checked_ids = [i for i in ids if i not in ("SQL", "TASK")]
            if key == "span" and stage != "prompt":
                checked_ids = []
            if checked_ids and not set(checked_ids) & in_scope:
                errors.append(f"{where}: {', '.join(ids)} not in this round's scope ({len(in_scope)} in scope); a "
                              "finding must involve an in-scope item")
        issue = finding.get("issue_type")
        if not isinstance(issue, str) or not issue.strip():
            errors.append(f"{where}: `issue_type` is missing")
        elif severity not in ("PLATFORM", "UNSURE") and not _issue_known(stage, issue):
            errors.append(f"{where}: issue_type {issue!r} is unknown at the {stage} stage "
                          f"({_issue_types_line(stage, pass_id)})")
        quote = finding.get("quote")
        if not isinstance(quote, str) or not quote.strip():
            errors.append(f"{where}: no quote (a finding without a quote is dropped)")
        else:
            texts = [t for i in ids for t in (_item_texts(stage, pool[i]) if key != "span" else pool[i])]
            if not any(_loose(quote) in _loose(t) for t in texts):
                errors.append(f"{where}: the quote is not a substring of {', '.join(ids)}: {quote[:80]!r}")
        if not isinstance(finding.get("evidence"), str) or not finding["evidence"].strip():
            errors.append(f"{where}: `evidence` (record path, id and quoted value) is missing")
        if not isinstance(finding.get("fix"), str):
            errors.append(f"{where}: `fix` must be a string")
        if stage == "rubric" and _key(issue or "") == "weight":
            expected = finding.get("expected_weight")
            if expected not in WEIGHT_LEVELS or isinstance(expected, bool):
                errors.append(f"{where}: a weight finding needs expected_weight 1, 3 or 5")
            elif key == "row" and all(items[i]["weight"] == expected for i in ids):
                errors.append(f"{where}: expected_weight equals the row's weight")
    majors = [f for f in findings if isinstance(f, dict) and f.get("severity") in ("Major", "Moderate")]
    if obj.get("verdict") == "PASS" and majors and pass_id != "O3":
        errors.append("`verdict` PASS contradicts a Major or Moderate finding")
    if obj.get("verdict") == "FAIL" and not scored and pass_id != "O3":
        errors.append("`verdict` FAIL with no scored finding")
    return errors


def record(task_dir, stage, round_no, pass_id, file, replace=False) -> dict:
    task_dir = Path(task_dir)
    stage_passes(stage)
    rc = _round_context(task_dir, stage, round_no)
    planned = {p["pass"]: p for p in rc["manifest"]["passes"]}
    if pass_id not in planned:
        raise ReviewError(f"pass {pass_id} is not planned in round {round_no} of {stage} "
                          f"(planned: {', '.join(planned) or 'none'})")
    target = rc["folder"] / f"output_{pass_id}.json"
    if target.exists() and not replace:
        raise ReviewError(f"{_rel(target)} exists; a returned pass is final (add --replace to overwrite it)")
    raw = Path(file).read_bytes()
    obj, problem = _parse_reply(raw)
    errors = [problem] if problem else validate_output(obj, stage, pass_id, rc)
    checks = [_check(f"record.{n}", "FAIL", e) for n, e in enumerate(errors, 1)]
    if not errors:
        brief = rc["folder"] / planned[pass_id]["brief"]
        stored = {"schema": OUTPUT_SCHEMA, "banner": BANNER, "output": obj,
                  "binding": {"stage": stage, "round": round_no, "pass": pass_id,
                              "artifact_sha256": rc["manifest"]["artifact"]["sha256"],
                              "brief_sha256": _sha(brief.read_bytes()) if brief.is_file() else None,
                              "manifest_sha256": _sha((rc["folder"] / "manifest.json").read_bytes()),
                              "reply_sha256": _sha(raw)}}
        _atomic_write(target, _dump(stored), "recorded reviewer output")
        count = len(obj.get("findings") or obj.get("opened") or [])
        checks.append(_check("record.stored", "PASS", f"{pass_id}: {count} "
                             f"{'record(s) opened' if stage == 'solver' else 'finding(s)'} stored in {_rel(target)}"))
    return {"tool": TOOL, "version": VERSION, "verdict": _verdict(checks),
            "bound_to": {rc["manifest"]["artifact"]["path"]: rc["manifest"]["artifact"]["sha256"]},
            "checks": checks, "command": "record", "stage": stage, "round": round_no, "pass": pass_id,
            "banner": BANNER}


# ---------------------------------------------------------------- summary

def merge_findings(outputs: dict, stage) -> list:
    """Findings from every pass merged without voting: the same ids and issue type become one entry."""
    merged = {}
    for pass_id in sorted(outputs):
        for finding in outputs[pass_id].get("findings") or []:
            key_name = next(k for k in ("row", "event", "span") if k in finding)
            ids = sorted(_ids(finding[key_name], key_name) or [], key=_natural)
            issue = _key(finding.get("issue_type", ""))
            if stage == "prompt":
                issue = PROMPT_ALIASES.get(issue, issue)
            key = (key_name, tuple(ids), issue, finding.get("severity") in NOT_SCORED and finding.get("severity"))
            entry = merged.setdefault(key, {"locator": key_name, "ids": ids, "issue_type": issue,
                                            "severities": [], "passes": [], "quotes": [], "evidence": [],
                                            "fixes": [], "expected_weight": None})
            entry["passes"].append(pass_id)
            entry["severities"].append(finding.get("severity"))
            for field, name in (("quotes", "quote"), ("evidence", "evidence"), ("fixes", "fix")):
                value = finding.get(name)
                if isinstance(value, str) and value.strip() and value not in entry[field]:
                    entry[field].append(value)
            if finding.get("expected_weight") in WEIGHT_LEVELS:
                entry["expected_weight"] = finding["expected_weight"]
    order = {"Major": 0, "Moderate": 1, "Minor": 2, "INVENTORY": 3, "PLATFORM": 4, "UNSURE": 5}
    out = []
    for entry in merged.values():
        entry["severity"] = min(entry["severities"], key=lambda s: order.get(s, 9))
        out.append(entry)
    return sorted(out, key=lambda e: (order.get(e["severity"], 9), [_natural(i) for i in e["ids"]], e["issue_type"]))


def _natural(text):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", str(text))]


def _band(score) -> str:
    return "PASS" if score >= 5 else "NON-FAIL" if score >= 3 else "FAIL"


def aggregate(stage, findings, rows=None) -> dict:
    """The rehearsal verdict by the platform's aggregation rule for the stage."""
    scored = [f for f in findings if f["severity"] not in NOT_SCORED]
    if stage == "prompt":
        dims = {k: 5 for k in PROMPT_DIMENSIONS}
        minors = {}
        for f in scored:
            key = PROMPT_ALIASES.get(f["issue_type"], f["issue_type"])
            kind = PROMPT_DIMENSIONS.get(key, ("", "binary"))[1]
            major = f["severity"] == "Major"
            if kind == "three":
                score = 3
            elif kind == "binary":
                score = 2
            elif kind == "banded":
                score = 2 if major else 3
            else:
                minors[key] = minors.get(key, 0) + (0 if major else 1)
                score = 2 if major or minors[key] >= 2 else 3
            dims[key] = min(dims.get(key, 5), score)
        score = min(dims.values())
        return {"rule": PROMPT_RULE, "dimensions": dims, "score": score, "verdict": _band(score)}
    if stage == "oe":
        comp = {"completeness": 5, "accuracy": 5}
        for f in scored:
            component, cap = OE_TYPES.get(f["issue_type"], ("accuracy", None))
            score = 3 if cap == "Minor" or f["severity"] == "Minor" else 2
            comp[component] = min(comp[component], score)
        score = min(comp.values())
        return {"rule": OE_RULE, "dimensions": comp, "score": score, "verdict": _band(score)}
    if stage == "rubric":
        rows = rows or []
        n = max(len(rows), 1)
        row_level, missing = {}, 0
        weight_one, weight_two = set(), set()
        process_invalid = process_missing = 0
        prohibition = non_agent = False
        nonstandard, all_fail = set(), set()
        order = {"Major": 0, "Moderate": 1, "Minor": 2}
        weights = {f"R{i}": r.get("weight") for i, r in enumerate(rows, 1)}
        for f in scored:
            issue = f["issue_type"]
            ids = f["ids"] if f["locator"] == "row" else []
            if issue in RUBRIC_TALLIED:
                severity = RUBRIC_TALLIED[issue]
                if issue == "missing_coverage" and not ids:
                    missing += 1
                for i in ids:
                    if i not in row_level or order[severity] < order[row_level[i]]:
                        row_level[i] = severity
                non_agent = non_agent or issue == "non_agent_centric"
            elif issue == "weight" and f["expected_weight"] in WEIGHT_LEVELS:
                for i in ids:
                    if weights.get(i) in WEIGHT_LEVELS:
                        gap = abs(WEIGHT_LEVELS.index(weights[i]) - WEIGHT_LEVELS.index(f["expected_weight"]))
                        (weight_two if gap == 2 else weight_one if gap == 1 else set()).add(i)
            elif issue == "invalid_process":
                process_invalid += 1
            elif issue == "missing_process_check":
                process_missing += 1
            elif issue == "nonstandard_agent_title":
                nonstandard.update(ids)
            elif issue == "prohibition":
                prohibition = True
            elif issue == "predicted_all_fail":
                all_fail.update(ids)
        major = sum(1 for v in row_level.values() if v == "Major") + missing
        moderate = sum(1 for v in row_level.values() if v == "Moderate")
        minor = sum(1 for v in row_level.values() if v == "Minor")
        quality = 2 if major or moderate or minor * 100 > 10 * n else 3 if minor * 100 >= 5 * n else 5
        weight_one -= weight_two
        criteria = 2 if weight_two or len(weight_one) * 100 > 10 * n else 4 if weight_one else 5
        outcome = any(_field(r, "category").lower() == "outcome" for r in rows)
        process = 2 if process_invalid or process_missing >= 2 else 3 if process_missing == 1 else 5
        agent = 2 if non_agent or len(nonstandard) * 100 > 10 * n else 3 if nonstandard else 5
        dims = {"overall_quality": quality, "criteria_weights": criteria, "category_balance": 5 if outcome else 2,
                "process": process, "agent_centric": agent, "negative": 2 if prohibition else 5}
        score = min(dims.values())
        if len(all_fail) >= 2:
            score = min(score, 2)
        return {"rule": RUBRIC_RULE, "dimensions": dims, "score": score, "verdict": _band(score),
                "tally": {"rows": len(rows), "major_rows_and_missing_outcomes": major, "moderate_rows": moderate,
                          "minor_rows": minor, "weight_one_level": sorted(weight_one, key=_natural),
                          "weight_two_levels": sorted(weight_two, key=_natural),
                          "predicted_all_fail": sorted(all_fail, key=_natural)}}
    return {"rule": SOLVER_RULE, "dimensions": {}, "score": None, "verdict": "ADVISORY"}


def _match_id(decider, opened) -> bool:
    a, b = str(decider).strip().casefold(), str(opened).strip().casefold()
    if not a or not b:
        return False
    if a == b:
        return True
    for long, short in ((a, b), (b, a)):
        if len(short) >= 6 and re.search(r"(?:^|[^0-9a-z_])" + re.escape(short) + r"(?:$|[^0-9a-z_])", long):
            return True
    return False


def _solver_units(task_dir, opened) -> tuple:
    path = _slot(task_dir, BUDGET)
    if not path.is_file():
        return None, f"{_rel(path)} not found"
    try:
        budget = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return None, f"{BUDGET} is not JSON ({exc})"
    units = []
    for unit in budget.get("units") or []:
        if not isinstance(unit, dict) or unit.get("role") == "realism":
            continue
        decider = (unit.get("decider") or {}).get("record_id", "")
        hit = next((o for o in opened if _match_id(decider, o)), None)
        units.append({"unit": unit.get("id"), "role": unit.get("role"), "decider": decider,
                      "opened": hit is not None, "matched": hit})
    return units, None


def evaluate(task_dir, stage, round_no=None, root=None) -> dict:
    """The summary of one round (default: the latest planned). Reads only."""
    task_dir = Path(task_dir)
    stage_passes(stage)
    existing = rounds(task_dir, stage)
    header = {"tool": TOOL, "version": VERSION, "command": "summary", "stage": stage, "banner": BANNER}
    if round_no is None and not existing:
        checks = [_check("rehearsal.complete", "WARN", f"no local rehearsal for {stage} yet: run "
                         f"`blind_review.py plan --task-dir {_rel(task_dir)} --stage {stage} --write`")]
        return dict(header, verdict="WARN", bound_to={}, checks=checks, round=None, rehearsal_verdict="NONE",
                    aggregation_rule=None, findings=[], passes={"recorded": [], "missing": []})
    number = round_no or existing[-1]
    try:
        return _summarize(task_dir, stage, number, root, header)
    except ReviewError as exc:
        checks = [_check("rehearsal.round", "FAIL", str(exc))]
        return dict(header, verdict="FAIL", bound_to={}, checks=checks, round=number, rehearsal_verdict="NONE",
                    aggregation_rule=None, findings=[], passes={"recorded": [], "missing": []})


def _summarize(task_dir, stage, number, root, header) -> dict:
    rc = _round_context(task_dir, stage, number)
    manifest = rc["manifest"]
    planned = [p["pass"] for p in manifest["passes"]]
    if not planned and manifest.get("previous_round"):
        # Nothing changed since the previous recorded round: its result stands (the platform's UNCHANGED mode).
        result = _summarize(task_dir, stage, manifest["previous_round"], root, header)
        note = _check("rehearsal.unchanged", "PASS", f"round {number}: nothing changed since round "
                      f"{manifest['previous_round']}; that round's result stands and is restated here")
        live = Path(task_dir) / manifest["artifact"]["path"]
        if not live.is_file() or _sha(live.read_bytes()) != manifest["artifact"]["sha256"]:
            note = _check("rehearsal.binding", "WARN", f"{manifest['artifact']['path']} changed after round "
                          f"{number} was planned: plan the next round")
        checks = [c for c in result["checks"] if c["id"] != "rehearsal.binding"] + [note]
        return dict(result, round=number, restated_from=manifest["previous_round"], checks=checks,
                    verdict=_verdict(checks))
    have = recorded_outputs(task_dir, stage, number)
    checks, outputs = [], {}
    for pass_id in planned:
        if pass_id not in have:
            continue
        try:
            stored = _load_output(have[pass_id])
        except ReviewError as exc:
            checks.append(_check("rehearsal.outputs", "FAIL", str(exc)))
            continue
        errors = validate_output(stored["output"], stage, pass_id, rc)
        if errors:
            checks.append(_check("rehearsal.outputs", "FAIL", f"{pass_id}: stored output no longer validates: "
                                 + "; ".join(errors[:3])))
            continue
        outputs[pass_id] = stored["output"]
    carried_from = {}
    for pass_id, source in sorted((manifest.get("carried") or {}).items()):
        path = recorded_outputs(task_dir, stage, source).get(pass_id)
        if path:
            try:
                outputs[pass_id] = _load_output(path)["output"]
                carried_from[pass_id] = source
            except ReviewError as exc:
                checks.append(_check("rehearsal.outputs", "FAIL", f"carried {pass_id} from round {source}: {exc}"))
    missing = [p for p in planned if p not in have]
    recorded = [p for p in planned if p in have]
    if missing:
        restart = "" if stage == "solver" else " (the platform restarts a pass until it returns)"
        checks.append(_check("rehearsal.complete", "WARN", f"{len(recorded)} of {len(planned)} passes recorded; "
                             f"missing {', '.join(missing)}{restart}"))
    else:
        carried_text = ", ".join(f"{k} from round {v}" for k, v in carried_from.items())
        checks.append(_check("rehearsal.complete", "PASS", f"all {len(planned)} planned passes recorded "
                             f"({', '.join(planned)})" + (f"; carried {carried_text}" if carried_from else "")))
    live = Path(task_dir) / manifest["artifact"]["path"]
    live_sha = _sha(live.read_bytes()) if live.is_file() else None
    stale_briefs = [p["pass"] for p in manifest["passes"]
                    if not (rc["folder"] / p["brief"]).is_file()
                    or _sha((rc["folder"] / p["brief"]).read_bytes()) != p["brief_sha256"]]
    if live_sha != manifest["artifact"]["sha256"]:
        checks.append(_check("rehearsal.binding", "WARN", f"{manifest['artifact']['path']} changed after round "
                             f"{number} "
                             f"was planned (planned {manifest['artifact']['sha256'][:12]}, now "
                             f"{(live_sha or 'missing')[:12]}); these findings are for the planned bytes: plan the "
                             f"next round"))
    elif stale_briefs:
        checks.append(_check("rehearsal.binding", "WARN", f"brief(s) {', '.join(stale_briefs)} differ from the planned "
                             "bytes; re-plan before recording more"))
    else:
        checks.append(_check("rehearsal.binding", "PASS", f"round {number} was planned on "
                             f"{manifest['artifact']['path']} sha256 {manifest['artifact']['sha256'][:12]}, the "
                             "current bytes; recorded outputs are bound to it"))
    try:
        ranges = load_ranges(sorted({s["id"] for p in manifest["passes"] for s in p["sources"]}), root)
        moved = [s["id"] for p in manifest["passes"] for s in p["sources"] if ranges[s["id"]]["sha256"] != s["sha256"]]
        checks.append(_check("rehearsal.sources", "WARN" if moved else "PASS",
                             f"pass text changed in Evals/ since planning: {', '.join(sorted(set(moved)))}" if moved
                             else "every pass text still reads as planned"))
    except ReviewError as exc:
        checks.append(_check("rehearsal.sources", "WARN", str(exc)))
    result = dict(header, round=number, scope=manifest["scope"], scope_reason=manifest["scope_reason"],
                  in_scope=manifest["in_scope"], passes={"planned": planned, "recorded": recorded, "missing": missing,
                                                         "carried": carried_from})
    if stage == "solver":
        out = outputs.get("SOLVER")
        opened = out.get("opened") if out else []
        units, problem = _solver_units(task_dir, opened or [])
        if out is None:
            checks.append(_check("solver.deciders", "SKIP", "no solver output recorded yet"))
        elif units is None:
            checks.append(_check("solver.deciders", "SKIP", f"no difficulty budget ({problem}); opened "
                                 f"{len(opened)} record(s)"))
        else:
            anchors = [u for u in units if u["role"] == "anchor" and u["opened"]]
            variance = [u for u in units if u["role"] == "variance"]
            detail = "; ".join(f"{u['unit']} ({u['role']}) {'OPENED' if u['opened'] else 'not opened'} {u['decider']}"
                               for u in units) or "no anchor or variance unit"
            checks.append(_check("solver.deciders", "WARN" if anchors else "PASS",
                                 (f"the cold solver opened the deciding record of anchor "
                                  f"{', '.join(u['unit'] for u in anchors)}; " if anchors else "")
                                 + f"{sum(u['opened'] for u in variance)} of {len(variance)} variance deciders "
                                   f"opened; {detail} (one sample: advisory, unmeasured)"))
        result.update(rehearsal_verdict="ADVISORY", aggregation_rule=SOLVER_RULE, units=units, opened=opened,
                      answer=(out or {}).get("answer"), findings=[])
    else:
        findings = merge_findings({k: v for k, v in outputs.items()}, stage)
        rows = read_rubric((rc["folder"] / "inputs" / "artifact" / RUBRIC).read_bytes()) if stage == "rubric" else None
        agg = aggregate(stage, findings, rows)
        fail_level = agg["verdict"] == "FAIL"
        verdict = agg["verdict"] if (not missing or fail_level) else "INCOMPLETE"
        inventory = [f for f in findings if f["severity"] == "INVENTORY"]
        standing = [f for f in findings if f["severity"] not in NOT_SCORED]
        if verdict == "PASS":
            checks.append(_check("rehearsal.findings", "PASS", f"no scored finding stands ({len(findings)} "
                                 "unscored note(s))" if findings else "no finding"))
        elif verdict == "INCOMPLETE":
            checks.append(_check("rehearsal.findings", "WARN" if standing else "PASS",
                                 f"{len(standing)} scored finding(s) so far; verdict waits for the missing passes"))
        else:
            worst = [f for f in standing if f["severity"] in ("Major", "Moderate")] or standing
            checks.append(_check("rehearsal.findings", "WARN",
                                 f"rehearsal verdict {verdict}: {len(standing)} scored finding(s) stand, e.g. "
                                 + "; ".join(f"{'/'.join(f['ids'])} {f['issue_type']} ({f['severity']}, "
                                             f"{', '.join(f['passes'])})" for f in worst[:3])))
        if stage == "oe":
            if inventory:
                checks.append(_check("rehearsal.o3_inventory", "WARN", f"O3 listed {len(inventory)} open-instruction "
                                     "item(s): match each to an OE that reads both sides and makes the fix; an "
                                     "unmatched item is a missing step (Completeness 2). This tool does not match "
                                     "them."))
            elif "O3" in outputs:
                checks.append(_check("rehearsal.o3_inventory", "PASS", "O3 found no open-instruction item"))
        result.update(rehearsal_verdict=verdict, aggregation_rule=agg["rule"], scores=agg["dimensions"],
                      score=agg["score"] if verdict != "INCOMPLETE" else None, tally=agg.get("tally"),
                      findings=findings, rejection_note=REJECTION_NOTE)
    result.update(verdict=_verdict(checks), checks=checks,
                  bound_to={manifest["artifact"]["path"]: manifest["artifact"]["sha256"],
                            _rel(rc["folder"] / "manifest.json", task_dir): _sha((rc["folder"] / "manifest.json")
                                                                                 .read_bytes())})
    return result


# ---------------------------------------------------------------- text output

def render(result) -> str:
    command = result.get("command")
    lines = []
    if command == "summary":
        lines.append(f"LOCAL REHEARSAL ({result['stage']}, round {result['round']}): {result['verdict']} — not a "
                     "platform verdict")
        if result.get("aggregation_rule"):
            score = result.get("score")
            lines.append(f"Rehearsal verdict: {result['rehearsal_verdict']}"
                         + (f" (score {score})" if score is not None else "") + f". Rule applied: "
                         f"{result['aggregation_rule']}")
    elif command == "plan":
        lines.append(f"BLIND REVIEW PLAN ({result['stage']}, round {result['round']}, {result['scope']}): "
                     f"{result['verdict']}")
        lines.append(BANNER)
    else:
        lines.append(f"BLIND REVIEW RECORD ({result['stage']}, round {result['round']}, {result['pass']}): "
                     f"{result['verdict']}")
    for check in result["checks"]:
        lines.append(f"[{check['status']}] {check['id']}: {check['detail']}")
    if command == "plan":
        for entry in result["passes"]:
            srcs = ", ".join(f"{Path(s['file']).name}:{s['lines'][0]}-{s['lines'][1]} {s['sha256'][:8]}"
                             for s in entry["sources"]) or "authored by blind_review.py"
            lines.append(f"  {entry['pass']:<6} {entry['brief']} {entry['brief_sha256'][:12]}  <- {srcs}")
        if result["scope"] == "changed":
            lines.append("In scope: " + (" ".join(result["in_scope"]) or "none"))
        if result["written"] and result["passes"]:
            lines.append(f"Next: give each brief to its own fresh subagent (the brief is its whole context), save the "
                         f"JSON reply, then: python3 Task_Authoring/tools/blind_review.py record --task-dir <task> "
                         f"--stage {result['stage']} --round {result['round']} --pass <P> --file <reply.json>")
    if command == "summary":
        passes = result.get("passes") or {}
        if passes.get("missing"):
            lines.append("Missing: " + ", ".join(passes["missing"]))
        for f in result.get("findings") or []:
            lines.append(f"  - {f['severity']:<9} {'/'.join(f['ids'])} {f['issue_type']} [{', '.join(f['passes'])}]"
                         + (f": {f['quotes'][0][:90]!r}" if f["quotes"] else ""))
        for unit in result.get("units") or []:
            lines.append(f"  - {unit['unit']} {unit['role']}: {'opened' if unit['opened'] else 'not opened'} "
                         f"{unit['decider']}")
        if result.get("rejection_note") and result.get("findings"):
            lines.append(result["rejection_note"])
    return "\n".join(lines)


# ---------------------------------------------------------------- self-test

def stub_sources(root: Path) -> None:
    """Write stand-in Evals/ files whose lines hold every PASS_TABLE range (for the self-test and unit tests)."""
    files = {}
    for rid, (rel, start, end, starts, contains) in PASS_TABLE["ranges"].items():
        lines = files.setdefault(rel, [])
        while len(lines) < end + 2:
            lines.append("")
        lines[start - 1] = starts + f" (stub {rid})"
        for n in range(start, end - 1):
            lines[n] = f"stub text of {rid}, line {n + 1}"
        if end > start:
            lines[end - 1] = f"stub end {contains}"
        else:
            lines[start - 1] += " " + contains
    for rel, lines in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


SELFTEST_ASSIGNMENT = """# Task Assigned Inputs — V3

## Platform assignment

```text
🏢 Business Function
Executive

🧑 Persona
Robert
Role: Co-founder & Creative Director

🎯 Competency
Finance

🛠️ Task Skill
Analysis and synthesis

📋 Task Type
long-horizon

🎚️ Difficulty Mode
easy

📅 Universe Date
February 14, 2026 00:00
```

## Resolved authoring inputs

```text
persona_name:       Robert
persona_role:       Co-founder & Creative Director
persona_key:        robert
email:              robert@harmonygames.co
universe_date_key:  2026-02-14
```
"""


def make_fixture(task: Path) -> None:
    """A small task folder: prompt, SQL, OEs, rubric, budget and planted design secrets."""
    (task / WORK_DIR).mkdir(parents=True, exist_ok=True)
    (task / ASSIGNMENT).write_text(SELFTEST_ASSIGNMENT, encoding="utf-8")
    (task / PROMPT).write_text("Leonard asked for the page in #winddown. Build it as a sheet in my Drive and share it "
                               "with him. Then reply to him in #winddown with the totals for ENG-2444.\n",
                               encoding="utf-8")
    (task / SQL).write_text("-- header\nINSERT INTO slack_messages (ts, text) VALUES ('1770945859.212469', "
                            "'the wire came back');\n", encoding="utf-8")
    (task / OE).write_text("OE 1  Read Leonard's post in #winddown\nExpected: OE-ONLY-MARKER the ask.\n\n"
                           "OE 2  Read ENG-2444 (from OE 1)\nExpected: the note.\n\n"
                           "OE 3  Reply in #winddown (values from OE 2)\nExpected: posted.\n", encoding="utf-8")
    rows = [
        {"title": "The Agent creates a sheet in Robert's Drive", "category": "Outcome", "weight": 1,
         "justification": "Lookup.", "evidence": "Leonard's post C0ADGSZKR3R/1770945859.212469."},
        {"title": "The Agent shows 16,428.57 in the Domino Delights column of the ENG-2444 line", "category": "Outcome",
         "weight": 3, "justification": "Interpretation.", "evidence": "SVB notice."},
        {"title": "The Agent moves ENG-2444 to Done", "category": "Outcome", "weight": 1,
         "justification": "Lookup.", "evidence": "Linear ENG-2444."},
        {"title": "The Agent shares the sheet with leonard.hayes@harmonygames.co", "category": "Outcome", "weight": 1,
         "justification": "Lookup.", "evidence": "Contacts."},
        {"title": "The Agent tells Leonard in #winddown that Domino Delights cost 959,342.64", "category": "Outcome",
         "weight": 5, "justification": "Join.", "evidence": "Sheet."},
        {"title": "The Agent posts its comment on ENG-2439 before it moves ENG-2439 to Done", "category": "Process",
         "weight": 1, "justification": "Order.", "evidence": "Leonard's doc."},
    ]
    (task / RUBRIC).write_text(json.dumps(rows, indent=1), encoding="utf-8")
    (task / WORK_DIR / "01_Scenario_Design.md").write_text("SECRET-DESIGN the answer is 959,342.64\n", encoding="utf-8")
    budget = {"schema": "difficulty-budget-v1", "units": [
        {"id": "U1", "role": "anchor", "decider": {"service": "slack", "record_id": "C0ADGSZKR3R/1770945859.212469"}},
        {"id": "U2", "role": "variance", "decider": {"service": "gmail",
                                                       "record_id": "robert@harmonygames.co/1815095592611804295"}},
        {"id": "U3", "role": "realism", "decider": {"service": "linear", "record_id": "ENG-2450"}}],
        "note": "SECRET-BUDGET"}
    (task / WORK_DIR / BUDGET).write_text(json.dumps(budget), encoding="utf-8")


def _reply(path: Path, obj) -> Path:
    path.write_text(json.dumps(obj), encoding="utf-8")
    return path


def _self_test() -> int:
    import selftest_sandbox
    done = []

    def ok(label, condition, detail=""):
        if not condition:
            raise AssertionError(f"{label} {detail}")
        done.append(label)

    with selftest_sandbox.scratch_tmp("blind_review_") as tmp:
        tmp = Path(tmp)
        root = tmp / "ws"
        stub_sources(root)
        task = tmp / "task"
        make_fixture(task)
        # dry run writes nothing
        result = plan(task, "prompt", root=root)
        ok("dry run", not result["written"] and not review_dir(task, "prompt").exists())
        # prompt round 1: four briefs, banner, verbatim stub text, no secrets
        result = plan(task, "prompt", write=True, root=root)
        folder = round_dir(task, "prompt", 1)
        briefs = {p.name: p.read_text(encoding="utf-8") for p in folder.glob("brief_*.md")}
        ok("prompt briefs", sorted(briefs) == [f"brief_P{n}.md" for n in range(1, 5)], sorted(briefs))
        ok("banner", all(t.startswith("# " + BANNER) for t in briefs.values()))
        ok("verbatim text", "stub text of dr.P1" in briefs["brief_P1.md"] and "stub text of dr.P2" not in
           briefs["brief_P1.md"])
        ok("no secrets", not any("SECRET" in t for t in briefs.values()))
        manifest = load_manifest(task, "prompt", 1)
        ok("manifest", manifest["scope"] == "full" and len(manifest["items"]) == 3
           and all(p["brief_sha256"] == _sha((folder / p["brief"]).read_bytes()) for p in manifest["passes"]))
        sha = manifest["artifact"]["sha256"]
        # record: good, then planted-bad replies
        good = {"pass": "P1", "artifact_sha256": sha, "checked": 3, "verdict": "FAIL", "findings": [
            {"span": "S3", "issue_type": "unique_ground_truth", "severity": "Major",
             "quote": "reply to him in #winddown with the totals", "evidence": "two totals exist", "fix": "name one"}]}
        ok("record good", record(task, "prompt", 1, "P1", _reply(tmp / "p1.json", good))["verdict"] == "PASS")
        ok("record twice refused", _raises(lambda: record(task, "prompt", 1, "P1", tmp / "p1.json")))
        bad_cases = {
            "wrong sha": dict(good, artifact_sha256="0" * 64),
            "bad quote": dict(good, findings=[dict(good["findings"][0], quote="words not in the prompt")]),
            "no quote": dict(good, findings=[dict(good["findings"][0], quote="")]),
            "unknown id": dict(good, findings=[dict(good["findings"][0], span="S9")]),
            "bad issue": dict(good, findings=[dict(good["findings"][0], issue_type="vibes")]),
            "moderate on prompt": dict(good, findings=[dict(good["findings"][0], severity="Moderate")]),
            "empty without checked": {"pass": "P2", "artifact_sha256": sha, "findings": [], "verdict": "PASS"},
        }
        for label, reply in bad_cases.items():
            out = record(task, "prompt", 1, "P2", _reply(tmp / "bad.json", {**reply, "pass": "P2"}))
            ok(f"refused: {label}", out["verdict"] == "FAIL" and not (folder / "output_P2.json").exists())
        summary = evaluate(task, "prompt", root=root)
        ok("summary incomplete", summary["verdict"] == "WARN" and summary["passes"]["missing"] == ["P2", "P3", "P4"]
           and summary["rehearsal_verdict"] == "FAIL")
        for pid in ("P2", "P3", "P4"):
            record(task, "prompt", 1, pid, _reply(tmp / f"{pid}.json", {"pass": pid, "artifact_sha256": sha,
                                                                         "checked": 3, "findings": [],
                                                                         "verdict": "PASS"}))
        summary = evaluate(task, "prompt", root=root)
        ok("summary fail-level", summary["rehearsal_verdict"] == "FAIL" and summary["verdict"] == "WARN"
           and summary["scores"]["unique_ground_truth"] == 2)
        # rubric round 1 full, all clean
        plan(task, "rubric", write=True, root=root)
        rman = load_manifest(task, "rubric", 1)
        ok("rubric full passes", [p["pass"] for p in rman["passes"]] == ["F2", "F3"] + [f"R{n}" for n in range(1, 8)])
        for entry in rman["passes"]:
            pid = entry["pass"]
            reply = {"pass": pid, "artifact_sha256": rman["artifact"]["sha256"], "checked": 6, "findings": [],
                     "verdict": "PASS"}
            if pid == "R1":
                reply = dict(reply, verdict="FAIL", findings=[{
                    "row": "R5", "issue_type": "overly_specific", "severity": "Major", "quote": "Domino Delights cost",
                    "evidence": "the prompt allows rounding", "fix": "accept rounding"}])
            record(task, "rubric", 1, pid, _reply(tmp / f"r_{pid}.json", reply))
        rsum = evaluate(task, "rubric", root=root)
        ok("rubric verdict", rsum["rehearsal_verdict"] == "FAIL" and rsum["passes"]["missing"] == [])
        # edit one row -> round 2 changed: edited row, flagged R5, token dependant R3 (ENG-2444)
        rows = json.loads((task / RUBRIC).read_text(encoding="utf-8"))
        rows[1]["title"] = rows[1]["title"].replace("16,428.57", "16,428.58")
        (task / RUBRIC).write_text(json.dumps(rows, indent=1), encoding="utf-8")
        res2 = plan(task, "rubric", write=True, root=root)
        status = res2["manifest"]["classification"]["status"]
        ok("changed scope", res2["scope"] == "changed" and res2["in_scope"] == ["R2", "R3", "R5"]
           and status["R2"] == "edited" and status["R5"] == "flagged" and status["R3"] == "dependant", status)
        ok("delta passes", [p["pass"] for p in res2["passes"]] == [f"R{n}" for n in range(1, 8)])
        out_scope = {"pass": "R6", "artifact_sha256": res2["manifest"]["artifact"]["sha256"], "verdict": "FAIL",
                     "findings": [{"row": "R1", "issue_type": "not_self_contained", "severity": "Major",
                                   "quote": "creates a sheet", "evidence": "x", "fix": "y"}]}
        ok("out of scope refused", record(task, "rubric", 2, "R6", _reply(tmp / "r6.json", out_scope))["verdict"]
           == "FAIL")
        # context change -> full again
        record(task, "rubric", 2, "R1", _reply(tmp / "r1b.json", {"pass": "R1", "artifact_sha256": res2["manifest"]
                                                                   ["artifact"]["sha256"], "checked": 3,
                                                                   "findings": [], "verdict": "PASS"}))
        (task / PROMPT).write_text((task / PROMPT).read_text(encoding="utf-8") + "Thanks.\n", encoding="utf-8")
        res3 = plan(task, "rubric", write=True, root=root)
        ok("context change full", res3["scope"] == "full" and "prompt" in res3["scope_reason"], res3["scope_reason"])
        # oe: O3 brief has no OE text; changed round carries O3
        plan(task, "oe", write=True, root=root)
        o_folder = round_dir(task, "oe", 1)
        ok("O3 blind to OEs", "OE-ONLY-MARKER" not in (o_folder / "brief_O3.md").read_text(encoding="utf-8")
           and "OE-ONLY-MARKER" in (o_folder / "brief_O1.md").read_text(encoding="utf-8")
           and not any("artifact" in r for r in load_manifest(task, "oe", 1)["passes"][2]["inputs"]))
        oman = load_manifest(task, "oe", 1)
        for pid in ("O1", "O2", "O3"):
            record(task, "oe", 1, pid, _reply(tmp / f"{pid}.json", {"pass": pid, "artifact_sha256": oman["artifact"]
                                                                     ["sha256"], "checked": 3, "findings": [],
                                                                     "verdict": "PASS"}))
        text = (task / OE).read_text(encoding="utf-8").replace("Expected: the note.", "Expected: the two notes.")
        (task / OE).write_text(text, encoding="utf-8")
        ores = plan(task, "oe", write=True, root=root)
        ok("oe changed", ores["scope"] == "changed" and ores["in_scope"] == ["OE 2", "OE 3"]
           and [p["pass"] for p in ores["passes"]] == ["O1", "O2"] and ores["manifest"]["carried"] == {"O3": 1},
           ores["in_scope"])
        # drift: a moved heading stops the plan
        dr = root / _DR
        lines = dr.read_text(encoding="utf-8").split("\n")
        lines.insert(100, "an inserted line")
        dr.write_text("\n".join(lines), encoding="utf-8")
        ok("drift stops", _raises(lambda: plan(task, "prompt", root=root), "no longer holds it"))
        stub_sources(root)
        # solver: anchor opened -> WARN
        sres = plan(task, "solver", write=True, root=root)
        sbrief = (round_dir(task, "solver", 1) / "brief_SOLVER.md").read_text(encoding="utf-8")
        ok("solver brief", sbrief.startswith("# " + BANNER) and "SECRET" not in sbrief and "Difficulty Mode" not in
           sbrief and sres["scope"] == "full")
        record(task, "solver", 1, "SOLVER", _reply(tmp / "s.json", {
            "pass": "SOLVER", "artifact_sha256": sres["manifest"]["artifact"]["sha256"], "verdict": "DONE",
            "opened": ["C0ADGSZKR3R/1770945859.212469"], "answer": "done"}))
        ssum = evaluate(task, "solver", root=root)
        units = {u["unit"]: u["opened"] for u in ssum["units"]}
        ok("solver units", units == {"U1": True, "U2": False} and ssum["verdict"] == "WARN")
    print("self-test: ok (" + ", ".join(done) + ")")
    return 0


def _raises(fn, needle="") -> bool:
    try:
        fn()
    except ReviewError as exc:
        return needle in str(exc)
    return False


# ---------------------------------------------------------------- CLI

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="blind_review.py", description="local rehearsal of the platform's blind "
                                 "reviewer passes (see the docstring). " + BANNER)
    sub = ap.add_subparsers(dest="command")
    p_plan = sub.add_parser("plan", help="write one brief per pass and the round manifest")
    p_plan.add_argument("--round", type=int)
    p_plan.add_argument("--full", action="store_true", help="review every row, whatever changed")
    p_plan.add_argument("--write", action="store_true", help="write the round (default: dry run)")
    p_rec = sub.add_parser("record", help="validate and store one reviewer's JSON reply")
    p_rec.add_argument("--round", type=int, required=True)
    p_rec.add_argument("--pass", dest="pass_id", required=True)
    p_rec.add_argument("--file", required=True)
    p_rec.add_argument("--replace", action="store_true", help="overwrite an output already recorded for this pass")
    p_sum = sub.add_parser("summary", help="passes, merged findings and the rehearsal verdict")
    p_sum.add_argument("--round", type=int)
    for parser in (p_plan, p_rec, p_sum):
        parser.add_argument("--task-dir", required=True)
        parser.add_argument("--stage", required=True, choices=STAGES)
        parser.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: plan, record or summary")
    if not Path(args.task_dir).is_dir():
        ap.error(f"task folder not found: {args.task_dir}")
    if args.command == "record" and not Path(args.file).is_file():
        ap.error(f"reply file not found: {args.file}")
    from task_context import ContextError
    try:
        if args.command == "plan":
            result = plan(args.task_dir, args.stage, args.round, full=args.full, write=args.write)
        elif args.command == "record":
            result = record(args.task_dir, args.stage, args.round, args.pass_id, args.file, replace=args.replace)
        else:
            result = evaluate(args.task_dir, args.stage, args.round)
    except (ReviewError, ContextError, OSError) as exc:
        title = {"plan": "BLIND REVIEW PLAN", "record": "BLIND REVIEW RECORD"}.get(args.command, "LOCAL REHEARSAL")
        print(f"{title} ({args.stage}): FAIL\n[FAIL] {args.command}.error: {exc}")
        return 1
    if args.json:
        payload = {k: v for k, v in result.items() if k != "manifest"} if args.command == "plan" else result
        print(json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False))
    else:
        print(render(result))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
