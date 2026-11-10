#!/usr/bin/env python3
"""platform_delta_lint.py - apply the platform-only rules to the artifact itself (plan WS5, items 1 and 2).

Why. The local Evals/ copy is several releases behind the platform, so a local PASS does not predict /rubric, /oe or
/prompt. The rules the platform applies today are recorded only in its stored reports; they were collected into
references/platform_rule_delta.json (the register). This lint reads that register and runs the rules a program can
decide on the task's own files. A rule that needs judgement is never guessed: it is listed once under
`not_mechanised` with what a person or a reviewer subagent has to check.

Commands
  rubric --task-dir T [--rubric FILE] [--json]   every mechanised /rubric rule on 09_Rubrics.json (04_Prompt.txt,
                                                 08_Oracle_Events.md and Working_Files/01_Gradable_Surface.json are
                                                 read as context when present)
  prompt --task-dir T [--json]                   the /prompt rules that can be read off 04_Prompt.txt
  oe     --task-dir T [--json]                   the /oe rules that can be read off 08_Oracle_Events.md
  rules  [--json]                                every register rule: implemented or not, wording status
                                                 (verbatim / reconstructed), whether it contradicts a local rule
  backtest [--json] [--no-eval-lint]             run the lint on the archived rubrics and compare with the stored
                                                 platform verdicts (support/completed_tasks)
  --self-test

Severity. A finding from a rule whose wording is the platform's own sentence (register `wording: verbatim`) is
FAIL-severity; from a reconstructed rule it is WARN-severity. BACKTESTED (below) overrides that default in both
directions, and only with the backtest numbers written next to the override.

Output. `PLATFORM DELTA LINT (<artifact>): PASS|WARN|FAIL`, then one `[STATUS] delta.<rule id>: detail` line per
implemented rule, the findings under it, and the rules that were not mechanised. --json prints one object
(tool, version, verdict, bound_to, checks, findings, review, not_mechanised). Exit 0 PASS or WARN, 1 FAIL, 2 usage.

Limits. Word patterns only. The lint reads titles; it does not open the universe, so it cannot tell whether a
record holds a decoy, whether a count is right, whether writes really follow one template, or whether two parts of
one write come from different records. "Same place" (content-row-proves-write) and "names the container"
(table-spot-check-rule) are word matches. A count stated inside one reply or document is listed for review, never
flagged: the platform passed such counts when a record asked for them (owen R137) and failed them when nothing did
(claire a2r2 R6-R8), and only the records tell the two apart. Read-only: it writes nothing. Stdlib only.

Python API: evaluate(task_dir, artifact="rubric", rubric_path=None, register_path=None) -> dict (no side effects).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
sys.path.insert(0, str(HERE))

TOOL = "platform_delta_lint"
VERSION = 1
REGISTER = BUNDLE / "references" / "platform_rule_delta.json"
ARCHIVE = BUNDLE / "support" / "completed_tasks"
ARTIFACTS = {"rubric": ("/rubric", "09_Rubrics.json"), "prompt": ("/prompt", "04_Prompt.txt"),
             "oe": ("/oe", "08_Oracle_Events.md")}

# Module constants that are thresholds (none of them is in references/first_pass_policy.json yet).
TITLE_CAP_WORDS = 120      # register rule title-cap-120-words
SAMPLE_CAP = 5             # Evals/3_Rubrics_Eval.md: at most five samples in a spot-check group
MIN_LIST_TARGETS = 2       # a write row naming this many separate targets is a bundle
MIN_COUNT = 2              # "exactly one ..." is not a count over several writes

# ------------------------------------------------------------------------------------------------ backtest record
# Filled from `platform_delta_lint.py backtest` on 2026-11-11 (13 failing rounds with stored bytes, 1 round with a
# near copy, 6 final rubrics the platform passed). A reconstructed rule is raised to FAIL only when it reproduced
# platform findings and raised no false alarm on a passed final rubric; a verbatim rule is lowered to WARN only with
# a reason written here. hits = exact + related, false_alarms = FAIL-severity findings on passed finals whose pass
# is not older than the rule. `backtest` recomputes the numbers and says when this table no longer matches.
BACKTESTED = {
    # Reconstructed lint check. Every count joined to an id range, id list or named members in the stored rounds was
    # a confirmed platform finding: 12 of 12 platform rows flagged, none on a passed final, none on a row a failing
    # round left alone -> FAIL.
    "bundled_writes": {"severity": "FAIL", "hits": 12, "misses": 0, "false_alarms": 0,
                       "basis": "claire r1 R22 R45 R60; samuel r1 R92 R104-R107; bridge r1 R12 R18; llc r1 R37 R38"},
    # The platform's own sentence. The lint cannot see its condition (the parts come from different records), but in
    # the stored rounds every row it flagged was a platform finding (19 of 21 rows: winddown r1 R86-R108, samuel r2
    # R117-R120; missed owen r2 R3 and bridge r1 R1) and it flags nothing on a passed final -> stays FAIL. A false
    # FAIL costs one split row; a miss costs a platform round.
    "multi_part_write": {"severity": "FAIL", "hits": 19, "misses": 2, "false_alarms": 0,
                         "basis": "winddown r1 R86-R108, samuel r2 R117-R120 found; owen r2 R3, bridge r1 R1 missed"},
    # The platform's own sentence, scored Moderate (COMPLETELY_REDUNDANT), not Major. The lint reads "same place"
    # from words (thread, #channel, DM, key), so it cannot tell when the destination row grades something the content
    # rows do not (douglas R21 also graded the DM id and the thread choice; that pass is older than the rule). 2 of 3
    # platform rows found (winddown R111, julia r1 R58); llc R68 became redundant only after the report's own fix.
    # Deleting a needed destination row costs a missing_coverage Major -> WARN.
    "content-row-proves-write": {"severity": "WARN", "hits": 2, "misses": 1, "false_alarms": 0,
                                 "basis": "winddown r1 R111 and julia r1 R58 found; llc r1 R68 missed; douglas final "
                                          "R21 flagged on a pass older than the rule"},
}

# ------------------------------------------------------------------------------------------------ rule handling
# Every register rule of /rubric, /prompt and /oe is either implemented (IMPLEMENTED) or listed with the reason it
# is not (NOT_MECHANISED). A register rule in neither table (added later by release_drift.py) is reported as
# not mechanised with the note "not reviewed for this lint yet", so a new rule is never dropped silently.
IMPLEMENTED = {
    # /rubric
    "one-row-per-write": "a row that covers several separate writes (every / each / all, a list of targets, or a "
                         "count of comments or messages whose content differs per target)",
    "bundled_writes": "a count joined to a range, a list of targets or named members",
    "count-bundle-v1": "a count over separate writes that is not the one volume row of a sampled group",
    "count_bundle": "every count row over separate writes or items, with how the lint read it",
    "template-only-sampling": "a volume row over sampled writes that states no template",
    "scope_tail": "a write row that carries a restriction on other targets (also inside its acceptance note)",
    "no-guard-without-trap": "an exclusion-only or leave-alone guard row; other guard rows are listed for review",
    "multi_part_write": "one write row that states an action and a date, or a ticket's state and its assignee",
    "content-row-proves-write": "a row that only places a reply or comment when every content row names the same "
                                "place",
    "title-cap-120-words": "a title over 120 words",
    "deliverable_claim": "a row that claims a link",
    "table-spot-check-rule": "table rows and cells are exempt from one row per write; a table volume row that no "
                             "sample row backs is a finding",
    "self-containment-sibling-titles": "never flagged: the platform accepts acceptance values from sibling titles",
    # /prompt
    "acceptance-search-v1": "the prompt asks for a link, an attachment or an email recipient list",
    # /oe
    "hg_decision_forks.py": "hedge wording in the Oracle Events",
}
NOT_MECHANISED = {
    # /rubric
    "bare-count-guard": ("superseded", "Nothing to check. This wording stopped on 2026-11-07; count-bundle-v1 "
                         "replaced it. Do not add a bare count guard over separate writes."),
    "decision_fork": ("unknown trigger", "The reports never say what wording the platform check hits. A reviewer "
                      "reads each row for a decision the records leave open (deep-recheck 2.8, masks_decision_fork)."),
    "trajectory_only_outcome": ("unknown trigger", "Named once, never described. Nothing to check locally."),
    "hg_rubric_ledger.py fixcheck": ("platform tool", "Not available locally. Its three known parts are run here as "
                                     "delta.title-cap-120-words, delta.bundled_writes and delta.scope_tail."),
    "opposite-pair-test": ("judgement", "After every fix, check the opposite defect: a fix for too broad must not "
                           "make the row too narrow, and the other way round."),
    "fix-check-rounds": ("reviewer process", "Copy fixes marked (checked) word for word; rewrite rows marked "
                         "'revised after check' yourself and expect them to be re-reviewed."),
    "overly_broad-minor": ("severity note", "Nothing to check in the file: the platform scores overly_broad at "
                           "Minor, and absorbs it on a row that already has a Major."),
    "acceptance-search@rubric": ("needs the records", "For every count row and value row, search the universe for "
                                 "another candidate item or value and settle each one from a record."),
    # /prompt
    "base-data-v1": ("needs the records", "Check that no expected answer needs a value from a known Snowflake or "
                     "Confluence base conflict and no injected record builds on one."),
    "known_base_issues.md@prompt": ("no local copy", "The platform's list is not in the local bundle. Keep rubric "
                                    "rows and OEs off any base value a platform report listed as a known issue."),
    "ugt-fork-v1": ("needs the records", "List every in-scope item and name the dated record the persona can see "
                    "that settles it. 'Accept either' in the OE or rubric does not close a fork."),
    "ugt-boundary-v1": ("needs the records", "For every general rule, find the items at its edge and check a "
                        "record speaks to each; a category left open fails."),
    "STEP 0.6 Dataset Similarity": ("platform tool", "The platform compares the prompt with its task set (meaning "
                                    "score 0.80 or more is a duplicate). Compare by hand with earlier tasks of the "
                                    "same persona and scenario."),
    "hg_similarity.py check": ("platform tool", "Not available locally."),
    "tool_outputs.md@prompt": ("no local copy", "The reference file is not in the local bundle. Quoted so far: a "
                               "file the Agent creates returns its link (gdrive.web_view_link)."),
    # /oe
    "decision-forks-2.8": ("needs the records", "For every boundary item, name the record that settles it. The "
                           "hedge-wording half of this check runs as delta.hg_decision_forks.py."),
    "tool_outputs.md@oe": ("no local copy", "The reference file is not in the local bundle. Quoted so far: a fact "
                           "stated only in a Gmail attachment is reachable; a created Drive file has a link."),
}
# Register rules of the other evals: not this tool's job, listed by `rules` so nothing is hidden.
OTHER_EVAL = {
    "json_shape": "/injection lint check on *_json columns of the SQL, not a rubric rule. tools/sql_lint.py "
                  "(row_rules) already fails malformed *_json values and non-array values in array columns; the "
                  "platform's own shape table is not in the local schema snapshot.",
}


class UsageError(Exception):
    """A problem with the inputs (exit 2)."""


# ------------------------------------------------------------------------------------------------ register
def load_register(path=None) -> dict:
    """The register's rules by id. Raises UsageError when the file is missing or unreadable."""
    path = Path(path or REGISTER)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise UsageError(f"cannot read the rule register {path}: {error}")
    rules = {}
    for rule in data.get("rules", []):
        if isinstance(rule, dict) and rule.get("id"):
            rules[rule["id"]] = rule
    if not rules:
        raise UsageError(f"the rule register {path} lists no rules")
    return rules


def severity_of(rule_id, register) -> str:
    """FAIL for the platform's own wording, WARN for a reconstructed rule, unless BACKTESTED says otherwise."""
    override = (BACKTESTED.get(rule_id) or {}).get("severity")
    if override in ("FAIL", "WARN"):
        return override
    return "FAIL" if (register.get(rule_id) or {}).get("wording") == "verbatim" else "WARN"


def rule_table(register) -> list:
    """One entry per register rule: how this tool handles it."""
    out = []
    for rule_id in sorted(register, key=lambda r: (register[r].get("eval", ""), r)):
        rule = register[rule_id]
        entry = {"id": rule_id, "eval": rule.get("eval"), "wording": rule.get("wording"),
                 "local_status": rule.get("local_status"), "local_ref": rule.get("local_ref"),
                 "contradicts_local": rule.get("local_status") == "contradicted"}
        if rule_id in IMPLEMENTED:
            entry.update(handling="implemented", check="delta." + rule_id, severity=severity_of(rule_id, register),
                         what=IMPLEMENTED[rule_id], backtested=rule_id in BACKTESTED)
        elif rule_id in NOT_MECHANISED:
            entry.update(handling="not_mechanised", reason=NOT_MECHANISED[rule_id][0],
                         what=NOT_MECHANISED[rule_id][1])
        elif rule_id in OTHER_EVAL:
            entry.update(handling="other_tool", what=OTHER_EVAL[rule_id])
        elif rule.get("eval") in ("/rubric", "/prompt", "/oe"):
            entry.update(handling="not_mechanised", reason="not reviewed",
                         what="Added to the register after this lint was written; not reviewed for this lint yet.")
        else:
            entry.update(handling="out_of_scope", what=f"{rule.get('eval')} rule: this tool lints the rubric, the "
                                                       "prompt and the Oracle Events only.")
        out.append(entry)
    return out


# ------------------------------------------------------------------------------------------------ title reading
_NUM_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
              "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
              "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50}
_NUM = r"(?:\d{1,3}(?:,\d{3})+|\d+|" + "|".join(_NUM_WORDS) + r")"
_KEY = r"[A-Z][A-Z0-9]{1,9}-\d+"
RX_KEY = re.compile(r"\b" + _KEY + r"\b")
RX_KEY_RANGE = re.compile(r"\b(" + _KEY + r")\s*(?:to|through|thru|–|—)\s*(" + _KEY + r")\b")
RX_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
RX_AGENT = re.compile(r"^\s*(?:The\s+)?Agent\s+(\w+)", re.I)
RX_TABLE = re.compile(r"\b(?:sheets?|spreadsheets?|trackers?|registers?|ledgers?|tables?|tabs?|columns?|cells?|rows?|"
                      r"workbooks?|worksheets?|send list)\b", re.I)
RX_STATE = re.compile(r"\b(?:state|status)\b|\b(?:to|in|into|as)\s+(?:the\s+)?(?:Done|Todo|To Do|Backlog|Canceled|"
                      r"Cancelled|In Progress|In Review|Closed|Open|Triage|Duplicate)\b")
RX_EXACT = re.compile(r"\b(?:exactly|precisely|a total of)\s+(" + _NUM + r")\b(?:\s+of\s+(?:the|its|their|those|these)"
                      r"(?:\s+" + _NUM + r")?\b)?", re.I)
RX_N_OF_M = re.compile(r"\b(\d[\d,]*)\s+of\s+the\s+" + _NUM + r"\b", re.I)   # digits: "every one of the 37" is no count
RX_QUANT_N = re.compile(r"\b(?:all|both|each\s+of|every\s+one\s+of|each\s+one\s+of)\s+(?:of\s+)?(?:the\s+|its\s+|"
                        r"these\s+|those\s+)?(" + _NUM + r")\b", re.I)
RX_THE_N = re.compile(r"\bthe\s+(" + _NUM + r")\s+(?=[a-z])", re.I)
RX_QUANT = re.compile(r"\b(every|each|all|both)\b(?!\s+(?:of\s+)?(?:it|them|its|his|her|their)\b)", re.I)
RX_TEMPLATE = re.compile(r"\beach\b|\bone\s+(?:\w+\s+)?per\b", re.I)
RX_TEMPLATE_NOTE = re.compile(r"\b(?:named|titled)\b|\beach\s+(?:with|in|naming|carrying|titled|named|dated|"
                              r"addressed)\b", re.I)
RX_ORDER = re.compile(r"\b(?:only\s+)?(?:after|before|once|until|when)\b", re.I)
_STOP = {"to", "on", "in", "from", "for", "with", "under", "below", "above", "as", "by", "at", "into", "onto",
         "across", "among", "besides", "beside", "during", "that", "which", "who", "whose", "than", "after", "before",
         "about", "over", "within", "through", "until", "when", "where", "while", "saying", "naming", "carrying",
         "listed", "named", "moved", "apart", "other", "out", "and", "or", "it", "is", "are", "counted"}
_CONTAINER = {"holding", "containing", "listing", "covering", "cover", "totaling", "totalling", "naming"}
TABLE_UNITS = {"row", "cell", "column", "line", "tab", "entry", "item", "heading", "header"}

STRICT_VERBS = {
    "comments": "COMMENT", "moves": "MOVE", "closes": "MOVE", "cancels": "MOVE", "reopens": "MOVE",
    "archives": "MOVE", "resolves": "MOVE", "assigns": "ASSIGN", "reassigns": "ASSIGN", "unassigns": "ASSIGN",
    "emails": "SEND", "sends": "SEND", "replies": "SEND", "dms": "SEND", "messages": "SEND", "forwards": "SEND",
    "invites": "SEND", "files": "CREATE", "creates": "CREATE", "opens": "CREATE", "schedules": "CREATE",
    "books": "CREATE", "shares": "SHARE", "deletes": "EDIT", "renames": "EDIT", "updates": "EDIT", "edits": "EDIT",
}
MIXED_VERBS = {"adds", "leaves", "posts", "puts", "sets", "changes", "clears", "writes", "makes", "saves", "removes",
               "labels", "tags"}
SAY_VERBS = {"names", "lists", "states", "tells", "says", "reports", "shows", "records", "gives", "answers", "asks",
             "includes", "links", "enters", "fills", "marks", "heads", "dates", "values", "ties", "titles", "starts",
             "orders", "keeps", "holds", "addresses", "closes its", "has"}
WRITE_NAMES = {"COMMENT": "comment", "MOVE": "state change", "ASSIGN": "assignment", "SEND": "message",
               "CREATE": "creation", "SHARE": "share", "EDIT": "edit", "LABEL": "label"}


def to_int(token) -> int:
    token = str(token).lower().replace(",", "")
    return _NUM_WORDS[token] if token in _NUM_WORDS else int(token)


def main_clause(title) -> str:
    """The title without quoted spans and parentheticals: source lines and acceptance notes are not the predicate."""
    text = re.sub(r'(?<=\d)["”]', "in", str(title))                      # 12.9" is an inch mark, not a quote
    text = re.sub(r'“[^”]*”|"[^"]*"', " QUOTE ", text)
    text = re.sub(r"(?<![A-Za-z0-9])'[^']*'(?![A-Za-z0-9])", " QUOTE ", text)
    while True:
        shorter = re.sub(r"\([^()]*\)", " ", text)
        if shorter == text:
            break
        text = shorter
    return re.sub(r"\s+", " ", text).strip()


def _singular(word) -> str:
    word = re.sub(r"['’]s?$", "", word.lower())
    if word in ("people", "persons"):
        return "person"
    if word == "children":
        return "child"
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith("ses") and len(word) > 4:
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss") and len(word) > 3:
        return word[:-1]
    return word


def _head_noun(text) -> str:
    """The head noun of the noun phrase that starts `text` ("ZOM tickets from Done" -> "ticket")."""
    words = []
    for raw in re.findall(r"[A-Za-z][\w&'’/-]*|\S", text)[:8]:
        if RX_KEY.fullmatch(raw) or not re.match(r"[A-Za-z]", raw) or raw.lower() in _STOP:
            break
        words.append(raw)
    return _singular(words[-1]) if words else ""


def write_class(main, verb):
    """The kind of write a title's leading verb makes, or None for a row that grades content or a table."""
    verb = (verb or "").lower()
    head = " ".join(main.split()[:14])
    table = bool(RX_TABLE.search(main))
    if verb in STRICT_VERBS:
        return STRICT_VERBS[verb]
    if verb not in MIXED_VERBS:
        return None
    if re.search(r"\bcomments?\b", head) and verb in ("adds", "leaves", "posts", "writes", "puts"):
        return "COMMENT"
    if verb == "posts":
        return "SEND"
    if verb == "saves" and re.search(r"\bdraft", head):
        return "SEND"
    if re.search(r"\bassignee\b", head) and verb in ("sets", "clears", "removes", "changes"):
        return "ASSIGN"
    if table:
        return None
    if verb in ("sets", "changes", "puts") and RX_STATE.search(main):
        return "MOVE"
    if verb == "adds" and re.search(r"\bnew\b", head):
        return "CREATE"
    if verb == "makes" and re.search(r"\bchanges?\b", head):
        return "EDIT"
    if verb in ("labels", "tags"):
        return "LABEL"
    return None


def read_row(number, row) -> dict:
    """What the lint needs to know about one rubric row."""
    title = str(row.get("title") or "")
    main = main_clause(title)
    match = RX_AGENT.match(main)
    verb = match.group(1).lower() if match else ""
    info = {"n": number, "id": f"R{number}", "title": title, "main": main, "verb": verb,
            "category": str(row.get("category") or ""), "wclass": write_class(main, verb),
            "table": bool(RX_TABLE.search(main)), "keys": RX_KEY.findall(main), "keys_all": RX_KEY.findall(title),
            "ranges_all": RX_KEY_RANGE.findall(title), "count": None, "quant": None,
            "template": bool(RX_TEMPLATE.search(main)),
            "notes": " ".join(str(row.get(k) or "") for k in ("justification", "evidence"))}
    exact = RX_EXACT.search(main) or RX_N_OF_M.search(main)
    if exact:
        number_ = to_int(exact.group(1))
        before = main[:exact.start()].split()
        info["count"] = {"n": number_, "text": exact.group(0), "unit": _head_noun(main[exact.end():]),
                         "container": bool(before) and before[-1].lower() in _CONTAINER, "end": exact.end()}
        if info["wclass"] == "MOVE" and re.match(r"\s*new\b", main[exact.end():]):
            info["wclass"] = "CREATE"          # "puts 58 of the new issues in Done": a field of the creation
    else:
        quant = RX_QUANT_N.search(main) or RX_THE_N.search(main)
        if quant and to_int(quant.group(1)) >= MIN_COUNT:
            info["quant"] = {"n": to_int(quant.group(1)), "text": quant.group(0).strip(),
                             "unit": _head_noun(main[quant.end():])}
        else:
            for word in RX_QUANT.finditer(main):
                unit = _head_noun(main[word.end():])
                if unit:
                    info["quant"] = {"n": None, "text": word.group(0), "unit": unit}
                    break
    return info


def counts_writes(info) -> bool:
    """True when the row's count is a count over separate writes (not table rows, not items named in one reply)."""
    count = info["count"]
    if not count or count["n"] < MIN_COUNT or count["container"] or not info["wclass"]:
        return False
    if count["unit"] in TABLE_UNITS:
        return False
    return not (info["table"] and info["verb"] in MIXED_VERBS)


def target_key(info) -> str:
    """What makes two single-target rows the same target: the first record key, else the whole predicate."""
    return info["keys"][0] if info["keys"] else info["main"]


def siblings(info, rows) -> set:
    """Targets that have a row of their own for the same kind of write as `info` (rows with no count)."""
    out = set()
    for other in rows:
        if other is info or other["count"] or other["wclass"] != info["wclass"]:
            continue
        if other["category"].lower() == "process":
            continue
        out.add(target_key(other))
    return out


def _fmt_rows(ids, limit=12) -> str:
    ids = list(ids)
    return ", ".join(ids[:limit]) + (f" and {len(ids) - limit} more" if len(ids) > limit else "")


# ------------------------------------------------------------------------------------------------ /rubric checks
RX_PLURAL_OBJECT = re.compile(r"\b(?:the|its|all|these|those)\s+(?:new\s+|existing\s+)?(?:[\w&'’-]+\s+){0,4}?"
                              r"(issues|tickets|cards|comments|emails|messages|replies|events|reminders|contacts|"
                              r"children|drafts|invites)\b", re.I)
RX_CONTENT_MARK = re.compile(r"\b(?:that|saying|stating|naming|carrying|about|with\s+the)\b|:", re.I)
RX_SPEECH = re.compile(r"\bthat\b|:", re.I)       # what follows "that" is reported content, not a target
RX_KEY_LIST = re.compile(r"\b" + _KEY + r"(?:\s*,\s*" + _KEY + r")*\s*,?\s*(?:and|&|plus)\s+" + _KEY + r"\b")
WRITE_OBJECTS = {"issue", "ticket", "card", "comment", "email", "message", "reply", "event", "reminder", "contact",
                 "child", "draft", "invite", "task", "pr", "thread", "post", "dm", "document", "doc", "file"}
_TARGET_PREPS = {"on", "to", "for", "with", "across", "in", "into", "of"}
FIELD_VERBS = {"starts", "puts", "sets", "gives", "titles", "labels", "tags"}
REPORT_VERBS = {"names", "lists", "states", "tells", "says", "reports", "shows", "records", "answers", "asks",
                "includes", "links", "enters", "fills", "marks", "heads"}
_TARGET_NOUNS = {"issue", "ticket", "card", "channel", "tab", "sheet", "file", "doc", "document", "thread", "message",
                 "post", "email", "comment", "event", "page", "folder", "person", "recipient", "description", "board",
                 "project", "list", "calendar", "contact", "draft", "spreadsheet"}
RX_NO_OTHER = re.compile(r"\b(?:no|not\s+any|none\s+of\s+the)\s+other\s+((?:[\w&'’-]+\s*){1,4})", re.I)
RX_ELSE = re.compile(r"\b(?:and|but|with)\s+(?:nothing|nowhere|no\s+one|nobody|none)\s+else\b|\bnowhere\s+else\b", re.I)
RX_ONLY_PREP = re.compile(r"(?<!\bthe\s)(?<!\bits\s)\bonly\s+(?:in|on|to|into|for|as|with|under|inside|within)\b", re.I)
RX_EXCEPT = re.compile(r"\b(?:other\s+than|apart\s+from|except(?:\s+for)?|besides|aside\s+from|excluding)\b", re.I)
RX_ONLY_OTHER = re.compile(r"\bonly\s+(?:on|for|to|in|into|with)\b[^.;]*?\b(?:other\s+than|apart\s+from|except)\b", re.I)
RX_LEAVE_ALONE = re.compile(r"^\s*(?:The\s+)?Agent\s+(?:leaves|keeps)\s+(?:\S+\s+){1,4}?(?:off|out\s+of|untouched|"
                            r"unchanged|alone|as\s+it\s+(?:is|was))\b", re.I)    # julia r1 R7-R18 "leaves ZOM-30 off"
RX_PROHIBIT = re.compile(r"^\s*(?:The\s+)?Agent\s+(?:(?:does\s+not|doesn't|never|must\s+not|will\s+not)\s+\w+|"
                         r"(?:sends|creates|files|posts|adds|opens|makes|moves|assigns|shares|writes)\s+no\b|"
                         r"(?:avoids|refrains\s+from|declines\s+to)\b)", re.I)
_MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"
RX_ACTION_DATE = re.compile(r"\b(?:saying|that|stating)\s+((?:[^\s,;]+\s+){2,}?)(?:by|until|before|on\s+or\s+before|"
                            r"no\s+later\s+than|with)\s+(?:(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*\.?,?\s+)?" + _MONTH +
                            r"\s+\d{1,2}\b", re.I)
RX_WRITE_CONTEXT = re.compile(r"\b(?:in|on)\s+(?:its|the|a)\s+(?:new\s+)?(?:comment|reply|email|message|DM|note)\b",
                              re.I)
RX_LINK = re.compile(r"\b(?:links?|URLs?|hyperlinks?)\b", re.I)
# "each saying which change still has to go out": the content differs per target, so it is no template (douglas R43)
RX_VARYING = re.compile(r"\beach\s+(?:\w+\s+){0,2}?(?:saying|stating|naming|explaining|giving|listing|telling|"
                        r"with|carrying|citing)\s+(?:\w+\s+){0,2}?(?:which|what|why|how|whose|when|where|its\s+own|"
                        r"their\s+own|that\s+\w+['’]s|the\s+\w+['’]s)\b", re.I)
# a count joined to named members or named exclusions: "38 item rows, one per issue ... plus the Combo Fighter VO
# campaign" (llc R37), "exactly 7 rows ..., apart from the Metabase, dbt and GitHub rows" (llc R38)
RX_MEMBERSHIP = re.compile(r"\b(?:plus|including|as\s+well\s+as|together\s+with|apart\s+from|except(?:\s+for)?|"
                           r"other\s+than|aside\s+from|excluding)\s+(?:the\s+)?(?:[A-Z][\w&'’.-]*|" + _KEY + r")")
# a scope restriction inside an acceptance note: "(… writing the payee lines into Leonard's working sheet fails)"
RX_PAREN_TAIL = re.compile(r"\((?:[^()]*?[;,…]\s*)?(?:…\s*)?(?:writing|posting|putting|adding|filing|sending|moving|"
                           r"creating|commenting)\b[^()]*?\b(?:into|onto)\b[^()]*?\bfails?\b[^()]*\)", re.I)
# two fields of one write: the state and the assignee of a ticket (samuel r2 R117-R120)
RX_STATE_FIELD = re.compile(r"\b(?:in|to|into)\s+(?:the\s+)?(?:Backlog|Todo|To Do|Done|Canceled|Cancelled|In Progress|"
                            r"In Review|Triage)\b")
RX_ASSIGNEE_FIELD = re.compile(r"\b(?:with\s+no\s+assignee|unassigned|no\s+assignee|assigned\s+to\s+[A-Z]\w*|"
                               r"with\s+[A-Z]\w*\s+as\s+(?:the\s+)?assignee)\b")
# the container a table count counts in: "an Awaiting reply checklist", "its plan sheet"
RX_CONTAINER_NP = re.compile(r"\b(?:a|an|the|its|his|her|their)\s+((?:[\w&'’-]+\s+){0,3}?(?:checklist|sheet|spreadsheet|"
                             r"register|tracker|list|log|table|workbook|worksheet))\b", re.I)
# content-row-proves-write: a row that only puts a reply or comment somewhere, and the rows that grade its content
RX_DEST_CONTENT = re.compile(r"\b(?:that|saying|stating|naming|carrying|about|asking|telling|listing|giving|"
                             r"explaining|confirming|linking|announcing|noting|quoting|citing|answering|with\s+the)\b|:",
                             re.I)
RX_ITS_WRITE = re.compile(r"\b(?:its|the)\s+(?:new\s+)?(?:[\w#'’-]+\s+){0,3}?(?:reply|comment|message|email|post)\b",
                          re.I)
RX_ADDRESSEE = re.compile(r"\bto\s+([A-Z][\w'’-]+)")
RX_CHANNEL = re.compile(r"#[\w-]+")


def _finding(rule, info, text, detail) -> dict:
    return {"rule": rule, "check": "delta." + rule, "row": info["id"], "text": text, "detail": detail}


def _unsampled(info, holder, rows) -> bool:
    """True when no other row names the container a table count counts in (no sample row grades its items).

    A row names it when it holds the whole phrase, or the container noun and every capitalised word of the phrase
    ("Awaiting reply checklist" needs "checklist" and "Awaiting"; "server sign-off register" needs "register")."""
    phrase = re.sub(r"\s+", " ", holder).strip()
    words = phrase.split()
    noun, names = words[-1].lower(), [w for w in words[:-1] if w[:1].isupper()]
    for other in rows:
        if other is info:
            continue
        title = other["title"]
        if phrase.lower() in title.lower():
            return False
        if re.search(r"\b" + re.escape(noun), title, re.I) and all(re.search(r"\b" + re.escape(n) + r"\b", title)
                                                                   for n in names):
            return False
    return True


RX_ORDER_ROW = re.compile(r"\bonly\s+(?:after|once|when|before)\b", re.I)


def destination_rows(rows) -> list:
    """content-row-proves-write: rows that only place a reply or comment, when every row that grades the content of
    that reply or comment already names the same place (thread, #channel, DM, or the issue key).

    Returns [(info, [ids of the content rows])]. A destination row that pins something no content row names (the
    thread, a channel) is kept: the platform kept owen R134 (the content rows did not say "thread") and deleted
    winddown R111 (every content row said "#winddown thread reply")."""
    out = []
    for info in rows:
        if info["category"].lower() == "process" or info["count"] or info["quant"]:
            continue
        if info["wclass"] not in ("SEND", "COMMENT"):
            continue
        body = RX_AGENT.sub("", info["main"], 1)
        if RX_DEST_CONTENT.search(body) or RX_ORDER_ROW.search(body):
            continue
        keys, who = info["keys"], RX_ADDRESSEE.search(body)
        if not keys and not who:
            continue
        needs = (["thread"] if re.search(r"\bthread", body, re.I) else []) + RX_CHANNEL.findall(body) + \
            (["DM"] if re.search(r"\bDM\b", body) else [])
        content = []
        for other in rows:
            if other is info or other["category"].lower() == "process" or RX_ORDER_ROW.search(other["main"]):
                continue
            if not RX_ITS_WRITE.search(other["main"]):
                continue
            if keys and not any(key in other["main"] for key in keys):
                continue
            if not keys and not re.search(r"\b" + re.escape(who.group(1)) + r"\b", other["main"]):
                continue
            content.append(other)
        if content and all(_names_place(other["main"], needs) for other in content):
            out.append((info, [other["id"] for other in content]))
    return out


def _names_place(text, needs) -> bool:
    return all((re.search(r"\bthread", text, re.I) if need == "thread" else need in text) for need in needs)


def _bundle_text(info):
    """The words that make a no-count title cover several separate writes, or None."""
    if info["count"] or info["category"].lower() == "process" or info["verb"] in REPORT_VERBS:
        return None
    if not info["wclass"] and info["verb"] not in FIELD_VERBS:
        return None
    if info["table"] and info["verb"] in MIXED_VERBS | FIELD_VERBS:
        return None                                      # cells of a table: the table spot-check rule
    body = RX_AGENT.sub("", info["main"], 1)             # drop "The Agent <verb>"
    body = RX_SPEECH.split(body, 1)[0]
    quant = info["quant"]
    if quant and quant["text"].lower() in body.lower():
        before = body.lower().split(quant["text"].lower(), 1)[0].split()
        target = not before or before[-1] in _TARGET_PREPS
        if quant["unit"] in WRITE_OBJECTS or (quant["n"] and info["wclass"] and target
                                              and quant["unit"] not in TABLE_UNITS):
            return quant["text"] + (" " + quant["unit"] if quant["unit"] else "")
    keys = RX_KEY_LIST.search(body)
    if keys and len(set(RX_KEY.findall(keys.group(0)))) >= MIN_LIST_TARGETS:
        return keys.group(0)
    if info["wclass"] == "SHARE" and len(set(RX_EMAIL.findall(info["title"]))) >= MIN_LIST_TARGETS:
        return "shares with " + ", ".join(sorted(set(RX_EMAIL.findall(info["title"])))[:3])
    plural = RX_PLURAL_OBJECT.search(body)
    if plural and not RX_KEY.search(body[:plural.start()]):
        return plural.group(0)
    return None


def lint_rubric(rubric, context=None) -> dict:
    """Run the mechanised /rubric rules. Returns {"findings": [...], "review": [...], "notes": {rule: text}}."""
    context = context or {}
    rows = [read_row(number, row if isinstance(row, dict) else {}) for number, row in enumerate(rubric, 1)]
    findings, review, notes = [], [], {}
    prompt = context.get("prompt") or ""

    # ---- count rows: which are counts over separate writes, and how each one reads
    write_counts = [info for info in rows if counts_writes(info)]
    largest = {}
    for info in write_counts:
        key = (info["wclass"], info["count"]["unit"])
        if key not in largest or info["count"]["n"] > largest[key]["count"]["n"]:
            largest[key] = info
    accepted, table_counts, content_counts, by_table = [], [], [], {}
    for info in rows:
        count = info["count"]
        if not count:
            continue
        named = re.search(r":\s*(?:the\s+)?[A-Z]", info["main"][count["end"]:])      # "exactly one angel: Anton ..."
        if count["n"] < MIN_COUNT:
            if named and info["category"].lower() != "process":
                findings.append(_finding("bundled_writes", info, count["text"], f"{info['id']} joins a count to "
                                         "the identity of what is counted. Keep the count bare and grade the "
                                         "named item in its own row."))
            continue
        listed = bool(info["ranges_all"]) or len(set(info["keys_all"])) >= MIN_LIST_TARGETS or bool(named) \
            or len(set(RX_EMAIL.findall(info["title"]))) >= MIN_LIST_TARGETS \
            or bool(RX_MEMBERSHIP.search(info["main"][count["end"]:]))
        if info not in write_counts:
            table = info["table"] or count["unit"] in TABLE_UNITS or count["container"]
            (table_counts if table else content_counts).append(info)
            nouns = RX_TABLE.findall(info["main"])
            if table and nouns and not count["container"] and not listed:
                by_table.setdefault(_singular(nouns[-1]), []).append(info)
            if listed and (info["wclass"] or table):
                where = "" if info["wclass"] else (" It grades table cells, which fall under the table rule, but the "
                                                   "platform still scored a count joined to membership as non_atomic.")
                findings.append(_finding("bundled_writes", info, count["text"], f"{info['id']} joins a count to a "
                                         "range, a list of ids or named members. Keep the count bare and grade each "
                                         "target in its own row." + where))
            continue
        kind = WRITE_NAMES.get(info["wclass"], "write")
        own = siblings(info, rows)
        what = f"{info['id']} counts {count['n']} separate {kind}s"
        first = largest[(info["wclass"], count["unit"])]
        varying = RX_VARYING.search(info["main"]) if info["wclass"] in ("COMMENT", "SEND") else None
        if listed:
            findings.append(_finding("bundled_writes", info, count["text"], f"{what} and joins the count to a range, "
                                     "a list or named members. Delete the id list; grade each target in its own row."))
        elif varying:
            findings.append(_finding("one-row-per-write", info, count["text"], f"{what}, each with content that "
                                     f"differs per target (\"{varying.group(0)}\"). Comments and messages whose "
                                     "content differs per target get one row each, with no cap; they are never "
                                     "sampled, so this is no template."))
        elif first is not info:
            findings.append(_finding("count-bundle-v1", info, count["text"], f"{what}; {first['id']} already counts "
                                     "the same kind of write. One sampled group keeps one volume row; delete this "
                                     "one (the per-target rows carry the number)."))
        elif info["template"] or RX_TEMPLATE_NOTE.search(info["title"]):
            accepted.append((info, "it states a template"))
        elif info["wclass"] in ("MOVE", "ASSIGN") and 1 <= len(own) <= SAMPLE_CAP and len(own) < count["n"]:
            accepted.append((info, f"{len(own)} sample rows, one state for all"))
        elif info["wclass"] in ("MOVE", "ASSIGN") and len(own) < count["n"]:
            rows_seen = (f"only {len(own)} have a row of their own: more than {SAMPLE_CAP} samples and fewer than "
                         "one row per target") if own else "no row grades any single target"
            findings.append(_finding("one-row-per-write", info, count["text"], f"{what} and {rows_seen}. State "
                                     "changes and other writes get one row per target; a group may be sampled "
                                     f"(up to {SAMPLE_CAP} rows plus this volume row) only when every write follows "
                                     "one template."))
        elif info["wclass"] == "CREATE" and 1 <= len(own) <= SAMPLE_CAP and len(own) < count["n"]:
            findings.append(_finding("template-only-sampling", info, count["text"], f"{what}, sampled by {len(own)} "
                                     "rows, and states no template. Writes are sampled only when every one follows "
                                     "one template and the volume row states it (\"..., each with ...\"); otherwise "
                                     "give each write its own row."))
        else:
            beside = f" beside {len(own)} rows that grade single targets" if own else ""
            findings.append(_finding("count-bundle-v1", info, count["text"], f"{what}{beside} and states no "
                                     "template, so it reads as a count guard, not a volume row. The platform fails "
                                     "a count over separate writes even beside per-item rows; delete it (per-target "
                                     "rows carry the number), or state the one template every write follows."))
    for noun, group in sorted(by_table.items()):
        keep = max(group, key=lambda i: i["count"]["n"])
        for info in group:
            if info is not keep:
                findings.append(_finding("count-bundle-v1", info, info["count"]["text"], f"{info['id']} is a second "
                                         f"count over the {noun} ({keep['id']} is its volume row). One output keeps "
                                         "one volume row; the platform scored further counts over its items as "
                                         "non_atomic. Delete it; sample cells carry the values."))
    flagged_ids = {f["row"] for f in findings}
    for info in table_counts:
        if info["id"] in flagged_ids or info["count"]["n"] < MIN_COUNT:
            continue
        holder = RX_CONTAINER_NP.search(info["main"])
        if not holder or not _unsampled(info, holder.group(1), rows):
            continue
        phrase = re.sub(r"\s+", " ", holder.group(1)).strip()
        findings.append(_finding("table-spot-check-rule", info, phrase, f"{info['id']} is a volume row over "
                                 f"{info['count']['n']} items of the {phrase}, and no other row names that "
                                 "container, so no row grades any of its items. The table rule keeps sample rows "
                                 f"(up to {SAMPLE_CAP}: hard and edge items) beside the one volume row; add sample "
                                 "rows that name items on it."))
    for info in content_counts:
        review.append({"rule": "count_bundle", "row": info["id"], "detail": "a count or total stated inside one "
                       "reply, comment or document: it stays only when the prompt or a record the task follows "
                       "asks for that total."})
    for info, why in accepted:
        review.append({"rule": "count_bundle", "row": info["id"], "detail": f"count over separate writes read as "
                       f"the group's one volume row ({why}); the platform lint hits it and a reviewer confirms it."})
    parts = []
    if accepted:
        parts.append(f"{len(accepted)} read as a sampled group's volume row ({_fmt_rows(i['id'] for i, _ in accepted)})")
    if table_counts:
        parts.append(f"{len(table_counts)} count table rows or cells ({_fmt_rows(i['id'] for i in table_counts)})")
    if content_counts:
        parts.append(f"{len(content_counts)} count items inside one reply, comment or list "
                     f"({_fmt_rows(i['id'] for i in content_counts)})")
    surface = context.get("surface") or {}
    volume_slots = [slot for slot in surface.get("slots") or [] if isinstance(slot, dict) and slot.get("role") == "volume"]
    if surface:
        parts.append(f"the gradable surface declares {len(volume_slots)} volume slot(s)")
    notes["count_bundle"] = "; ".join(parts) if parts else "no count row"
    notes["table-spot-check-rule"] = (f"{len(table_counts)} count row(s) grade table rows or cells and are not "
                                      "treated as counts over separate writes" if table_counts
                                      else "no count row grades table rows or cells")
    notes["self-containment-sibling-titles"] = ("not flagged: the platform reads acceptance values from the title, "
                                                "the prompt or sibling titles (the local rule is title-only)")

    any_flag = {f["row"] for f in findings}
    for info in rows:
        main = info["main"]
        process = info["category"].lower() == "process"
        is_write = bool(info["wclass"]) or counts_writes(info)
        # ---- guard rows an idle Agent passes
        idle = None if process else \
            (RX_ONLY_OTHER.search(main) or RX_PROHIBIT.search(main) or RX_LEAVE_ALONE.search(main))
        if idle and info["id"] not in any_flag:
            findings.append(_finding("no-guard-without-trap", info, idle.group(0)[:80], f"{info['id']} is an "
                                     "exclusion-only guard row: an Agent that writes nothing passes it. A guard is "
                                     "allowed only where a record holds a real decoy, and a decoy no required reply "
                                     "or report can carry gets no row. Delete it or grade the required write."))
            any_flag.add(info["id"])
        # ---- one row per separate write: a title that covers several writes without counting them
        bundle = _bundle_text(info)
        if bundle and info["id"] not in any_flag:
            findings.append(_finding("one-row-per-write", info, bundle, f"{info['id']} covers several separate "
                                     f"writes in one row (\"{bundle}\"). State changes, comments, messages and other "
                                     "writes get one row per target; a group may be sampled only when every write "
                                     "follows one template and one volume row states it."))
            any_flag.add(info["id"])
        # ---- scope tail: a write plus a restriction on other targets
        tail = None
        acts = is_write or info["verb"] in MIXED_VERBS | FIELD_VERBS
        if not process and info["verb"] not in REPORT_VERBS:
            other = RX_NO_OTHER.search(main)
            only = RX_ONLY_PREP.search(main)
            if other and {_singular(w) for w in re.findall(r"[A-Za-z]+", other.group(1))} & _TARGET_NOUNS:
                tail = other.group(0).strip()
            elif RX_ELSE.search(main):
                tail = RX_ELSE.search(main).group(0)
            elif acts and only:
                tail = only.group(0)
            elif is_write and RX_EXCEPT.search(main) and (info["count"] or info["quant"] or len(info["keys"]) >= 2):
                tail = RX_EXCEPT.search(main).group(0)
            elif acts and RX_PAREN_TAIL.search(info["title"]):
                tail = RX_PAREN_TAIL.search(info["title"]).group(0)[:90]
        if tail and info["id"] not in any_flag:
            findings.append(_finding("scope_tail", info, tail, f"{info['id']} joins a write to a restriction on "
                                     f"other targets (\"{tail}\"). Grade the required write alone; the platform "
                                     "scores a confirmed scope tail as non_atomic."))
        # ---- parts of one write from different sources
        if (info["wclass"] in ("COMMENT", "SEND") or RX_WRITE_CONTEXT.search(main)) and not process:
            parts_hit = RX_ACTION_DATE.search(main)
            if parts_hit:
                findings.append(_finding("multi_part_write", info, parts_hit.group(0)[:90], f"{info['id']} states "
                                         "what happens and a date in one row. When the two come from different "
                                         "records they are independent results: one row for the action, one for "
                                         "the date."))
        state, assignee = RX_STATE_FIELD.search(main), RX_ASSIGNEE_FIELD.search(main)
        if state and assignee and not process and info["wclass"] in ("CREATE", "MOVE") \
                and not info["count"] and not info["quant"]:
            findings.append(_finding("multi_part_write", info, f"{state.group(0)} … {assignee.group(0)}",
                                     f"{info['id']} grades two fields of one write, its state (\"{state.group(0)}\") "
                                     f"and its assignee (\"{assignee.group(0)}\"). A write with the right state and "
                                     "the wrong assignee fails the whole row: give each field its own row."))
        # ---- title cap
        words = len(info["title"].split())
        if words > TITLE_CAP_WORDS:
            findings.append(_finding("title-cap-120-words", info, f"{words} words", f"{info['id']} has a title of "
                                     f"{words} words; the platform's fixcheck caps a title at {TITLE_CAP_WORDS}. "
                                     "Split the row or move wording that grades nothing out of the title."))
        # ---- review lists (never findings)
        if RX_LINK.search(main):
            review.append({"rule": "deliverable_claim", "row": info["id"], "detail": "claims a link: supported when "
                           "it links a file the Agent creates (a created Drive file returns its link)."})
        count = info["count"]
        guard = (count and count["n"] == 1 and info["wclass"] and not count["container"]) \
            or re.search(r"\bguard\b", info["notes"], re.I)
        if guard and info["id"] not in any_flag and not process:
            review.append({"rule": "no-guard-without-trap", "row": info["id"], "detail": "reads as a wrong-target "
                           "guard: name the record that holds the real decoy; with none, delete the row."})
    for info, content in destination_rows(rows):
        if info["id"] in any_flag:
            continue
        kind = "comment" if info["wclass"] == "COMMENT" else "reply"
        findings.append(_finding("content-row-proves-write", info, info["main"][:80], f"{info['id']} only puts the "
                                 f"{kind} in place, and every row that grades its content ({_fmt_rows(content)}) "
                                 "already names the same place, so each of them proves the write. The platform "
                                 "deleted such a row as COMPLETELY_REDUNDANT (Moderate). Delete it, or make the "
                                 "content rows drop the place only if this row grades something they do not."))
    if prompt:
        for finding in findings:
            if finding["rule"] in ("count-bundle-v1", "bundled_writes"):
                number = re.search(_NUM, finding["text"], re.I)
                if number and re.search(r"(?<![\w.,])" + re.escape(number.group(0)) + r"(?![\w.,]*\d)", prompt, re.I):
                    finding["detail"] += " (The prompt text contains this number; check whether it asks for it.)"
    order = {info["id"]: info["n"] for info in rows}
    findings.sort(key=lambda f: (list(IMPLEMENTED).index(f["rule"]), order[f["row"]]))
    review.sort(key=lambda r: (list(IMPLEMENTED).index(r["rule"]), order[r["row"]]))
    return {"findings": findings, "review": review, "notes": notes, "rows": len(rows)}


# ------------------------------------------------------------------------------------------------ /prompt and /oe
RX_PROMPT_ASK = re.compile(r"\b(link(?:s|ed)?|urls?|hyperlinks?|attach(?:ed|ment|ments|ing)?|cc(?:'d|ed)?|bcc|"
                           r"recipient list|distribution list|mailing list)\b", re.I)
RX_HEDGE = re.compile(r"\b(?:either(?:\s+is\s+fine|\s+one|\s+way)?|whichever|or\s+equivalent|or\s+similar|"
                      r"if\s+applicable|as\s+appropriate|optionally|may\s+or\s+may\s+not|both\s+are\s+fine|"
                      r"is\s+fine\s+too|or\s+alternatively|up\s+to\s+the\s+agent)\b", re.I)


def lint_prompt(text) -> dict:
    """The /prompt rules that can be read off the prompt text."""
    findings = []
    for number, line in enumerate(str(text).splitlines(), 1):
        for hit in RX_PROMPT_ASK.finditer(line):
            findings.append({"rule": "acceptance-search-v1", "check": "delta.acceptance-search-v1",
                             "row": f"L{number}", "text": hit.group(0),
                             "detail": f"line {number} mentions \"{hit.group(0)}\". If the task asks for a link, an "
                                       "attachment or an email recipient list, the platform checks it against its "
                                       "tool_outputs reference; the reports only show a task that asks for none. "
                                       "Have a reviewer confirm the tools return what is asked."})
            break
    notes = {"acceptance-search-v1": "the prompt mentions no link, attachment or email recipient list (the case the "
                                     "stored platform reports passed)"}
    return {"findings": findings, "review": [], "notes": notes, "rows": len(str(text).splitlines())}


def lint_oe(text) -> dict:
    """The /oe rules that can be read off the Oracle Events text."""
    findings = []
    for number, line in enumerate(str(text).splitlines(), 1):
        hit = RX_HEDGE.search(line)
        if hit:
            findings.append({"rule": "hg_decision_forks.py", "check": "delta.hg_decision_forks.py",
                             "row": f"L{number}", "text": hit.group(0),
                             "detail": f"line {number} hedges (\"{hit.group(0)}\"). The platform records a hedge "
                                       "that changes no state, destination or count as the same result; any other "
                                       "hedge is an open fork. Settle it with a record or drop the alternative."})
    notes = {"hg_decision_forks.py": "no hedge wording (the word list is this tool's; the platform's is not "
                                     "published)"}
    return {"findings": findings, "review": [], "notes": notes, "rows": len(str(text).splitlines())}


# ------------------------------------------------------------------------------------------------ evaluate
def _slot(task_dir, name) -> Path:
    """Where a task file lives: <task>/ or <task>/Working_Files/ (stage_gate.slot_path, with a plain fallback)."""
    try:
        from stage_gate import slot_path
        return Path(slot_path(task_dir, name))
    except Exception:                                    # stage_gate cannot be imported: same two places
        top, work = Path(task_dir) / name, Path(task_dir) / "Working_Files" / name
        return top if top.exists() or not work.exists() else work


def _sha(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _rel(path, base) -> str:
    try:
        return Path(path).resolve().relative_to(Path(base).resolve()).as_posix()
    except ValueError:
        return Path(path).as_posix()


def load_rubric(path) -> list:
    """The rubric rows (a list, or the `criteria` list of an object). Raises ValueError when it is neither."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("criteria", data.get("rubrics"))
    if not isinstance(data, list) or any(not isinstance(row, dict) for row in data):
        raise ValueError("the rubric is not a list of criteria")
    return data


def _result(artifact, verdict, bound, checks, findings=(), review=(), not_mechanised=(), rows=0) -> dict:
    return {"tool": TOOL, "version": VERSION, "artifact": artifact, "verdict": verdict,
            "bound_to": dict(sorted(bound.items())), "checks": list(checks), "findings": list(findings),
            "review": list(review), "not_mechanised": list(not_mechanised), "rows": rows}


def evaluate(task_dir, artifact="rubric", rubric_path=None, register_path=None) -> dict:
    """Lint one artifact of a task folder against the register. No side effects; returns the JSON object."""
    if artifact not in ARTIFACTS:
        raise UsageError(f"unknown artifact {artifact!r}: use rubric, prompt or oe")
    register = load_register(register_path)
    task_dir = Path(task_dir)
    eval_name, file_name = ARTIFACTS[artifact]
    path = Path(rubric_path) if (artifact == "rubric" and rubric_path) else _slot(task_dir, file_name)
    bound = {_rel(register_path or REGISTER, WS): _sha(register_path or REGISTER)}
    table = [entry for entry in rule_table(register) if entry["eval"] == eval_name]
    not_mechanised = [{"rule": e["id"], "wording": e["wording"], "reason": e["reason"], "check": e["what"]}
                      for e in table if e["handling"] == "not_mechanised"]
    if not path.is_file():
        check = {"id": "delta.input", "status": "FAIL", "detail": f"{_rel(path, task_dir)} is missing"}
        return _result(artifact, "FAIL", bound, [check], not_mechanised=not_mechanised)
    bound[_rel(path, task_dir)] = _sha(path)
    context = {}
    try:
        if artifact == "rubric":
            rubric = load_rubric(path)
            for key, name in (("prompt", "04_Prompt.txt"), ("oe", "08_Oracle_Events.md"),
                              ("surface", "01_Gradable_Surface.json")):
                extra = _slot(task_dir, name)
                if extra.is_file():
                    bound[_rel(extra, task_dir)] = _sha(extra)
                    text = extra.read_text(encoding="utf-8", errors="replace")
                    context[key] = json.loads(text) if key == "surface" else text
            if not rubric:
                check = {"id": "delta.input", "status": "FAIL", "detail": f"{_rel(path, task_dir)} has no rows"}
                return _result(artifact, "FAIL", bound, [check], not_mechanised=not_mechanised)
            out = lint_rubric(rubric, context)
        else:
            text = path.read_text(encoding="utf-8", errors="replace")
            out = lint_prompt(text) if artifact == "prompt" else lint_oe(text)
    except (ValueError, OSError) as error:
        check = {"id": "delta.input", "status": "FAIL", "detail": f"cannot read {_rel(path, task_dir)}: {error}"}
        return _result(artifact, "FAIL", bound, [check], not_mechanised=not_mechanised)

    checks, findings = [], []
    for finding in out["findings"]:
        finding = dict(finding, severity=severity_of(finding["rule"], register),
                       wording=(register.get(finding["rule"]) or {}).get("wording"))
        findings.append(finding)
    for entry in table:
        if entry["handling"] != "implemented":
            continue
        rule_id = entry["id"]
        mine = [f for f in findings if f["rule"] == rule_id]
        look = [r for r in out["review"] if r["rule"] == rule_id]
        if mine:
            status = entry["severity"]
            detail = f"{len(mine)} finding(s): {_fmt_rows(f['row'] for f in mine)}. {entry['what'].capitalize()}."
        else:
            status = "PASS"
            detail = out["notes"].get(rule_id) or f"no finding ({entry['what']})"
        if look:
            detail += f" To review: {_fmt_rows(r['row'] for r in look)}."
        checks.append({"id": "delta." + rule_id, "status": status, "detail": detail})
    for rule_id in IMPLEMENTED:
        if ARTIFACT_OF.get(rule_id) == artifact and rule_id not in register:
            checks.append({"id": "delta." + rule_id, "status": "SKIP",
                           "detail": "the rule is not in the register any more; not applied"})
    verdict = "FAIL" if any(c["status"] == "FAIL" for c in checks) else \
        "WARN" if any(c["status"] == "WARN" for c in checks) else "PASS"
    return _result(artifact, verdict, bound, checks, findings, out["review"], not_mechanised, out["rows"])


ARTIFACT_OF = {rule: "rubric" for rule in IMPLEMENTED}
ARTIFACT_OF.update({"acceptance-search-v1": "prompt", "hg_decision_forks.py": "oe"})


def render_text(result) -> str:
    lines = [f"PLATFORM DELTA LINT ({result['artifact']}): {result['verdict']}"]
    by_check = {}
    for finding in result["findings"]:
        by_check.setdefault(finding["check"], []).append(finding)
    for check in result["checks"]:
        lines.append(f"[{check['status']}] {check['id']}: {check['detail']}")
        for finding in by_check.get(check["id"], []):
            lines.append(f"    {finding['row']} [{finding['severity']}] {finding['detail']}")
    if result["review"]:
        lines.append("To review (not findings):")
        lines += [f"    {item['row']} delta.{item['rule']}: {item['detail']}" for item in result["review"]]
    if result["not_mechanised"]:
        lines.append("Not mechanised (a person or a reviewer subagent checks these):")
        lines += [f"    {item['rule']} ({item['wording']}; {item['reason']}): {item['check']}"
                  for item in result["not_mechanised"]]
    return "\n".join(lines)


def render_rules(table) -> str:
    done = [e for e in table if e["handling"] == "implemented"]
    lines = [f"PLATFORM DELTA LINT (rules): {len(done)} of {len(table)} register rules implemented"]
    for entry in table:
        local = "contradicts " + str(entry["local_ref"]) if entry["contradicts_local"] else \
            "absent from the local bundle"
        if entry["handling"] == "implemented":
            tested = "backtested" if entry["backtested"] else "wording default"
            head = f"[implemented] delta.{entry['id']} ({entry['eval']}; {entry['wording']}; {local}; " \
                   f"{entry['severity']}-severity, {tested})"
        else:
            reason = f"; {entry['reason']}" if entry.get("reason") else ""
            head = f"[{entry['handling']}] {entry['id']} ({entry['eval']}; {entry['wording']}; {local}{reason})"
        lines.append(f"{head}: {entry['what']}")
    return "\n".join(lines)


# ------------------------------------------------------------------------------------------------ backtest data
# Platform /rubric rounds used by `backtest`. `bytes` is the rubric file that round reviewed (its SHA-256 must equal
# the report's "Reviewed JSON SHA-256"); None when the archive did not keep it. `set` says whether the round was
# read while the rules were written (dev) or only after they were frozen (holdout).
BACKTEST_ROUNDS = (
    ("claire_r1", "dev", "claire_zm3d_halloween_art_plan_2026-11-10",
     "eval_reports/attempt1_6aea4c1eea32a6fa98b9b1d9/3_rubric_FAIL_r1.md",
     "task_inputs/Working_Files/rubric_gen/review7/rubric_candidate.json"),
    ("douglas_r1", "dev", "douglas_beta_server_signoff_2026-10-28",
     "eval_reports/6ad90ea979eb9e5d89f8879f_3_rubric.md", "work/scratch_scoring/rub/09_Rubrics.v1.json"),
    ("owen_r1", "dev", "owen_dd_bug_carryover_2026-11-09", "eval_reports/3_rubric_FAIL1_r1.md",
     "task_inputs/Working_Files/run_forensics/rev9/rubric/09_Rubrics_2ed7a6489798.json"),
    ("owen_r2", "dev", "owen_dd_bug_carryover_2026-11-09", "eval_reports/3_rubric_FAIL_r2.md",
     "task_inputs/Working_Files/run_forensics/rev9/rubric/09_Rubrics_9f8ebad8c3e3.json"),
    ("winddown_r1", "dev", "robert_winddown_closeout_2026-10-30",
     "eval_reports/6adfee3f27ce6ca81b457137_3_rubric.md", "task_inputs/Working_Files/09_Rubrics.pre_rubric_r3.json"),
    ("samuel_r1", "dev", "samuel_zm_beta_messages_2026-11-09", "eval_reports/3_rubric_FAIL1_r1.md",
     "task_inputs/Working_Files/run_forensics/rev6/rubric_r1/09_Rubrics.reviewed_3911b7d5f4de.json"),
    ("claire_a2r1", "holdout", "claire_zm3d_halloween_art_plan_2026-11-10",
     "eval_reports/attempt2_6aeed825ea17fab7311d0896/6aeed825ea17fab7311d0896_3_rubric.md",
     "task_inputs/Working_Files/rubric_gen/platform_r3fix/09_Rubrics.reviewed_6e8624c28ac6.json"),
    ("claire_a2r2", "holdout", "claire_zm3d_halloween_art_plan_2026-11-10",
     "eval_reports/attempt2_6aeed825ea17fab7311d0896/6aeed825ea17fab7311d0896_3_rubric (1).md",
     "task_inputs/Working_Files/rubric_gen/platform_r4fix/09_Rubrics.reviewed_e70e93c35e19.json"),
    ("bridge_r1", "holdout", "frederick_bridge_pipeline_2026-11-03", "eval_reports/3_rubric_FAIL_r1.md",
     "task_inputs/Working_Files/run_forensics/rev12/09_Rubrics.draft2.json"),
    ("bridge_r2", "holdout", "frederick_bridge_pipeline_2026-11-03", "eval_reports/3_rubric_FAIL_r2.md",
     "task_inputs/Working_Files/run_forensics/rev12/09_Rubrics.draft4_38rows.json"),
    ("llc_r1", "holdout", "robert_llc_takeover_2026-11-06", "eval_reports/3_rubric_FAIL_r1.md",
     "task_inputs/Working_Files/run_forensics/rev4/rubric/09_Rubrics_8296aaf8dc71.json"),
    ("samuel_r2", "holdout", "samuel_zm_beta_messages_2026-11-09", "eval_reports/3_rubric_FAIL1_r2.md",
     "task_inputs/Working_Files/run_forensics/rev6/rubric_r2/09_Rubrics.submitted_d1cbadf710e9.json"),
    ("samuel_r3", "holdout", "samuel_zm_beta_messages_2026-11-09", "eval_reports/3_rubric_FAIL1_r3.md",
     "task_inputs/Working_Files/run_forensics/rev6/rubric_r3/09_Rubrics.submitted_5bf50637b0a1.json"),
    ("q4_r1", "no bytes", "frederick_q4_commitments_2026-11-05", "eval_reports/3_rubric_FAIL_r1.md", None),
    ("julia_r1", "near", "julia_zm_difficulty_baseline_2026-11-01", "eval_reports/3_rubric_FAIL_r1.md",
     "work/jl_difficulty/rubric_r1_base.json"),
    ("julia_r4", "no bytes", "julia_zm_difficulty_baseline_2026-11-01", "eval_reports/3_rubric_FAIL_r4.md", None),
    ("leonard_r1", "no bytes", "leonard_stockholder_closeout_2026-11-10",
     "eval_reports/6aed9d01a1cb8067d8ac7dee_3_rubric-round1.md", None),
    ("seed_r2", "no bytes", "robert_seed_bets_2026-11-11", "eval_reports/6aeed82596dcfe103f9f74d9_3_rubric-2.md",
     None),
    ("vincent_r1", "no bytes", "vincent_zm3d_release_gate_2026-11-06",
     "eval_reports/6ae9909f7b5249d3148f3707_3_rubric.md", None),
)
# Rounds whose stored file is not byte-identical to what the platform reviewed (its SHA-256 differs) but whose rows
# line up with everything the report says about them. Their results are kept apart ("near" column) and the reason is
# printed with them.
NEAR_BYTES = {
    "julia_r1": "work/jl_difficulty/rubric_r1_base.json differs from the reviewed SHA-256, but the report's R4 pass "
                "reads 73 rows as this file has, and its R7-R18 ('leaves ZOM-x off'), R20 (w5 beside R19 w3), R57 "
                "(the comment count), R58 (the bare reply row) and R61/R71 (the duplicate pair) are this file's rows",
}
# What the platform confirmed in each round, read from the report: (register rule, rows, report line[, other
# register rules the same finding also names]). Rows are the report's own R-numbers (1-based rows of the reviewed
# file). An empty row list is a missing-coverage finding: the rule was applied, but to rows that do not exist.
# Only findings that fall under a register rule are listed; value, weight and wording findings are not.
PLATFORM_FINDINGS = {
    "claire_r1": (("bundled_writes", "R22 R45 R60", 117), ("no-guard-without-trap", "R58 R59", 121, "count-bundle-v1"),
                  ("no-guard-without-trap", "R167 R168 R219", 125, "scope_tail")),
    "douglas_r1": (("one-row-per-write", "R43", 142), ("one-row-per-write", "", 150), ("one-row-per-write", "", 151)),
    "owen_r1": (("count-bundle-v1", "R1 R6 R7", 15, "scope_tail"), ("one-row-per-write", "R2 R3 R4 R5 R42", 16),
                ("one-row-per-write", "", 23)),
    "owen_r2": (("multi_part_write", "R3", 15),),
    "winddown_r1": (("multi_part_write", "R86 R87 R88 R89 R91 R92 R93 R95 R96 R97 R99 R101 R102 R106 R108", 187),
                    ("no-guard-without-trap", "R70", 183, "one-row-per-write count-bundle-v1"),
                    ("content-row-proves-write", "R111", 188)),
    "samuel_r1": (("bundled_writes", "R92 R104 R105 R106 R107", 71), ("one-row-per-write", "R114", 73),
                  ("scope_tail", "R139", 74, "count-bundle-v1")),
    "claire_a2r1": (("count-bundle-v1", "R57 R164 R215", 81), ("count-bundle-v1", "R23 R24 R40", 82)),
    "claire_a2r2": (("count-bundle-v1", "R6 R7 R8", 11),),
    "bridge_r1": (("multi_part_write", "R1", 87), ("bundled_writes", "R12 R18", 91),
                  ("one-row-per-write", "R20", 101)),
    "bridge_r2": (),
    "llc_r1": (("one-row-per-write", "R5 R28", 156), ("one-row-per-write", "", 159),
               ("bundled_writes", "R37 R38", 172), ("content-row-proves-write", "R68", 33)),
    "samuel_r2": (("multi_part_write", "R117 R118 R119 R120", 17),),
    "samuel_r3": (("template-only-sampling", "R105", 12),),
    "q4_r1": (("one-row-per-write", "", 94), ("template-only-sampling", "R36 R40", 100),
              ("multi_part_write", "R29", 111), ("content-row-proves-write", "R47", 29)),
    "julia_r1": (("no-guard-without-trap", "R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18", 98),
                 ("content-row-proves-write", "R58", 28), ("one-row-per-write", "", 93)),
    "julia_r4": (("multi_part_write", "R49 R50 R51 R52 R53 R54 R55", 90), ("bundled_writes", "R69", 21)),
    "leonard_r1": (("scope_tail", "R1", 74), ("no-guard-without-trap", "R122", 84)),
    "seed_r2": (("scope_tail", "R1", 79),),
    "vincent_r1": (("scope_tail", "R2 R41 R68", 101), ("bundled_writes", "R3", 102),
                   ("multi_part_write", "R62", 109)),
}
# Rows a report explicitly keeps as they are (a group's volume row, or a guard it ruled valid at the time).
PLATFORM_KEPT = {"owen_r1": "R31", "owen_r2": "R1 R79 R120", "douglas_r1": "R2 R33", "winddown_r1": "R2 R82",
                 "claire_a2r1": "R22", "claire_a2r2": "R24", "bridge_r1": "R17 R19", "bridge_r2": "R13 R20 R27",
                 "samuel_r2": "R106"}
# Missing-coverage findings (no row of the reviewed file) and the one row the report ties them to: the count row
# over the writes that have no row of their own. Such a finding counts as found when the lint flags that row under
# a rule of the "writes" group, because that finding tells the author to give each target its own row.
#   douglas_r1 150 "Ticket comments (6 x Major)" -> R43, the comment count; 151 "Todo moves (6 x Major)" -> R33, the
#   move count; owen_r1 23 "Missing: 47 rows" (new issues) -> R1, the creation count; llc_r1 159 "30 call comments
#   with no row of their own" -> R5, the every-issue comment row; julia_r1 93 "M2 / M3" (no rows for ZOM-315 and
#   ZOM-293, "R57 doesn't state the template") -> R57, the comment count.
MISSING_ANCHORS = {("douglas_r1", 150): "R43", ("douglas_r1", 151): "R33", ("owen_r1", 23): "R1",
                   ("llc_r1", 159): "R5", ("julia_r1", 93): "R57"}
# Rules whose findings answer the same defect: a platform finding counts as found when the lint flags the row
# under the same rule ("exact") or under another rule of the same group ("related").
RULE_GROUP = {"one-row-per-write": "writes", "bundled_writes": "writes", "count-bundle-v1": "writes",
              "template-only-sampling": "writes", "count_bundle": "writes", "table-spot-check-rule": "writes",
              "scope_tail": "guard", "no-guard-without-trap": "guard"}
RX_REPORT_SHA = re.compile(r"Reviewed JSON SHA-256:\s*([0-9a-f]{64})")
RX_REPORT_VERDICT = re.compile(r"FINAL VERDICT:\s*\**\s*(PASS|NON-FAIL|FAIL)")
RX_REPORT_RELEASE = re.compile(r"Eval release SHA-256:\s*`?([0-9a-f]{8,64})")
EVAL_LINT_FAILING = ("Major", "Moderate", "gate")       # hg_rubric_lint severities that score against a rubric


def _report_facts(path) -> dict:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    sha, verdict, release = RX_REPORT_SHA.search(text), RX_REPORT_VERDICT.search(text), RX_REPORT_RELEASE.search(text)
    return {"sha": sha.group(1) if sha else None, "verdict": verdict.group(1) if verdict else None,
            "release": release.group(1) if release else None}


def _final_rubrics(archive_root) -> list:
    """Each archived task's final 09_Rubrics.json with the platform report that reviewed those exact bytes."""
    out = []
    for task in sorted(p for p in Path(archive_root).iterdir() if p.is_dir()):
        final = task / "task_inputs" / "09_Rubrics.json"
        if not final.is_file():
            continue
        sha, match = _sha(final), None
        reports = sorted((task / "eval_reports").rglob("*rubric*.md")) if (task / "eval_reports").is_dir() else []
        for report in reports:
            facts = _report_facts(report)
            if facts["sha"] == sha:
                match = dict(facts, report=_rel(report, task))
        out.append({"task": task.name, "rubric": final, "sha": sha, "reports": len(reports), "match": match})
    return out


def _release_dates(register_path=None) -> dict:
    data = json.loads(Path(register_path or REGISTER).read_text(encoding="utf-8"))
    return {str(r.get("fingerprint")): (r.get("first_seen"), r.get("last_seen")) for r in data.get("releases", [])}


def _before_rule(rule, release, register, dates) -> bool:
    """True when the report's release was last seen before the rule was first seen (the pass predates the rule)."""
    first = (register.get(rule) or {}).get("first_seen")
    last = next((d[1] for fp, d in dates.items() if release and fp.startswith(release[:12])), None)
    return bool(first and last and last < first)


def _lint_file(path, task_inputs=None) -> dict:
    context = {}
    if task_inputs:
        for key, name in (("prompt", "04_Prompt.txt"), ("surface", "01_Gradable_Surface.json")):
            extra = _slot(task_inputs, name)
            if extra.is_file():
                text = extra.read_text(encoding="utf-8", errors="replace")
                try:
                    context[key] = json.loads(text) if key == "surface" else text
                except ValueError:
                    pass
    return lint_rubric(load_rubric(path), context)


def _eval_lint(path) -> dict:
    """Run the local eval lint (hg.py rubric-lint) on one rubric file; {"error": ...} when it cannot run."""
    try:
        done = subprocess.run([sys.executable, "-B", str(HERE / "hg.py"), "rubric-lint", str(path)],
                              capture_output=True, text=True, cwd=str(WS), timeout=300)
    except (OSError, subprocess.SubprocessError) as error:
        return {"error": str(error)[:200]}
    try:
        hits = json.loads(done.stdout).get("findings", [])
    except ValueError:
        first = ((done.stdout or done.stderr).strip().splitlines() or ["no output"])[0]
        return {"error": f"hg.py printed no JSON: {first[:160]}"}
    by_check = {}
    for hit in hits:
        entry = by_check.setdefault(hit.get("check"), {"severity": hit.get("severity"), "rows": set()})
        entry["rows"].add(hit.get("row"))
    summary = {check: {"severity": e["severity"], "rows": len(e["rows"])} for check, e in sorted(by_check.items())}
    return {"checks": summary, "fails": sorted(c for c, e in summary.items() if e["severity"] in EVAL_LINT_FAILING)}


def backtest(archive_root=None, register_path=None, eval_lint=True) -> dict:
    """Compare the rubric lint with the stored platform verdicts. Read-only."""
    archive_root = Path(archive_root or ARCHIVE)
    register = load_register(register_path)
    dates = _release_dates(register_path)
    rules = [r for r in IMPLEMENTED if ARTIFACT_OF.get(r) == "rubric"]
    rules += sorted({item[0] for items in PLATFORM_FINDINGS.values() for item in items} - set(rules))
    table = {r: {"rule": r, "wording": (register.get(r) or {}).get("wording"), "reports": 0, "rows": 0,
                 "exact": 0, "related": 0, "miss": 0, "dev": [0, 0], "holdout": [0, 0], "near": [0, 0],
                 "kept_flagged": [], "alarms": [], "alarms_before_rule": [], "warn_on_passed": [], "other_rows": []}
             for r in rules}
    # 1. final rubrics the platform passed
    finals, passed = _final_rubrics(archive_root), []
    for final in finals:
        match = final["match"]
        entry = {"task": final["task"], "verdict": match["verdict"] if match else None,
                 "report": match["report"] if match else None, "release": (match or {}).get("release")}
        if match and match["verdict"] in ("PASS", "NON-FAIL"):
            out = _lint_file(final["rubric"], final["rubric"].parent)
            entry["rows"] = out["rows"]
            entry["findings"] = [{"rule": f["rule"], "row": f["row"], "severity": severity_of(f["rule"], register),
                                  "text": f["text"]} for f in out["findings"]]
            if match["verdict"] == "PASS":
                for f in entry["findings"]:
                    where = f"{final['task']} {f['row']}"
                    if f["severity"] != "FAIL":
                        table[f["rule"]]["warn_on_passed"].append(where)
                    elif _before_rule(f["rule"], match["release"], register, dates):
                        table[f["rule"]]["alarms_before_rule"].append(where)
                    else:
                        table[f["rule"]]["alarms"].append(where)
            if eval_lint:
                entry["eval_lint"] = _eval_lint(final["rubric"])
            passed.append(entry)
        else:
            entry["note"] = ("no stored platform report reviewed these bytes" if not match
                             else "the last platform report on these bytes is a FAIL")
            passed.append(entry)
    # 2. failing rounds
    rounds = []
    for key, group, task, report, rubric in BACKTEST_ROUNDS:
        applied = PLATFORM_FINDINGS.get(key, ())
        for rule in {item[0] for item in applied}:
            table[rule]["reports"] += 1
        entry = {"round": key, "set": group, "report": f"{task}/{report}", "bytes": rubric, "platform": [],
                 "other_findings": []}
        report_path, flagged = archive_root / task / report, {}
        if rubric:
            rubric_path = archive_root / task / rubric
            if not report_path.is_file() or not rubric_path.is_file():
                entry["error"] = "report or rubric file not found"
            elif _report_facts(report_path)["sha"] != _sha(rubric_path) and key not in NEAR_BYTES:
                entry["error"] = "the rubric bytes do not match the report's Reviewed JSON SHA-256"
            else:
                if key in NEAR_BYTES:
                    entry["near"] = NEAR_BYTES[key]
                for f in _lint_file(rubric_path, archive_root / task / "task_inputs")["findings"]:
                    flagged.setdefault(f["row"], []).append(f["rule"])
        claimed = set()
        for item in applied:
            rule, rows, line = item[0], item[1].split(), item[2]
            also = set(item[3].split()) if len(item) > 3 else set()
            anchor = MISSING_ANCHORS.get((key, line)) if not rows else None
            claimed.update(rows + ([anchor] if anchor else []))
            if not rubric or "error" in entry:
                entry["platform"].append({"rule": rule, "rows": rows, "line": line, "checked": False,
                                          "anchor": anchor})
                continue
            if not rows and not anchor:
                entry["platform"].append({"rule": rule, "rows": rows, "line": line, "checked": False,
                                          "anchor": None})
                continue
            check_rows = rows or [anchor]
            exact = [r for r in check_rows if rule in flagged.get(r, ())]
            groups = {RULE_GROUP.get(name) for name in also | {rule}} - {None}
            related = [r for r in check_rows if r not in exact and any(
                x in also or RULE_GROUP.get(x) in groups for x in flagged.get(r, ()))]
            miss = [r for r in check_rows if r not in exact and r not in related]
            entry["platform"].append({"rule": rule, "rows": rows, "line": line, "checked": True, "exact": exact,
                                      "related": related, "miss": miss, "anchor": anchor})
            row = table[rule]
            row["rows"] += len(check_rows)
            row["exact"] += len(exact)
            row["related"] += len(related)
            row["miss"] += len(miss)
            if group in ("dev", "holdout", "near"):
                row[group][0] += len(exact) + len(related)
                row[group][1] += len(miss)
        kept = set(PLATFORM_KEPT.get(key, "").split())
        release = _report_facts(report_path)["release"] if report_path.is_file() else None
        for row_id, hit_rules in sorted(flagged.items(), key=lambda kv: int(kv[0][1:])):
            for rule in hit_rules:
                if row_id in claimed:
                    continue
                before = _before_rule(rule, release, register, dates)
                where = f"{key} {row_id}" + (" (round older than the rule)" if before else "")
                if row_id in kept:
                    table[rule]["kept_flagged"].append(where)
                else:
                    entry["other_findings"].append(f"{row_id} {rule}" + (" (older than the rule)" if before else ""))
                    table[rule]["other_rows"].append(where)
        rounds.append(entry)
    # 3. does the BACKTESTED table still match?
    stale = []
    for rule, record in sorted(BACKTESTED.items()):
        row = table.get(rule)
        if row and (record.get("hits"), record.get("misses"), record.get("false_alarms")) != \
                (row["exact"] + row["related"], row["miss"], len(row["alarms"])):
            stale.append(rule)
    ok = [e for e in passed if e.get("verdict") == "PASS"]
    alarms = sum(len(r["alarms"]) for r in table.values())
    summary = {"passed_finals": len(ok), "nonfail_finals": sum(1 for e in passed if e.get("verdict") == "NON-FAIL"),
               "rounds_with_bytes": sum(1 for r in rounds if r["bytes"] and "error" not in r and not r.get("near")),
               "rounds_near_bytes": sum(1 for r in rounds if r.get("near") and "error" not in r),
               "false_alarms_in_force": alarms,
               "alarms_before_rule": sum(len(r["alarms_before_rule"]) for r in table.values()),
               "eval_lint_failing": sorted(e["task"] for e in ok if (e.get("eval_lint") or {}).get("fails")),
               "backtested_table_stale": stale}
    return {"tool": TOOL, "version": VERSION, "verdict": "WARN" if alarms or stale else "PASS",
            "rules": [dict(table[r], severity=severity_of(r, register) if r in IMPLEMENTED else "n/a")
                      for r in rules], "finals": passed, "rounds": rounds, "summary": summary}


def render_backtest(result) -> str:
    s = result["summary"]
    lines = [f"PLATFORM DELTA LINT (backtest): {result['verdict']}",
             f"{s['passed_finals']} final rubrics the platform passed, {s['nonfail_finals']} it scored NON-FAIL, "
             f"{s['rounds_with_bytes']} failing rounds with stored rubric bytes, {s['rounds_near_bytes']} with a stored "
             "file whose rows match the report but whose SHA-256 does not.", "",
             "Per rule: reports = rounds where the platform applied it; rows = platform rows checked in rounds with "
             "bytes (a missing-coverage finding counts once, at the count row the report ties it to); exact / "
             "related = rows the lint flags under the same rule / under a rule of the same group; miss; other = lint "
             "findings on rows the failing round did not flag (round with the rule in force / older than the rule); "
             "kept = lint findings on rows the report kept; alarms = FAIL-severity findings on passed finals "
             "(rule in force / pass older than the rule).", "",
             f"{'rule':<32}{'wording':<15}{'sev':<6}{'reports':>8}{'rows':>6}{'exact':>7}{'related':>9}{'miss':>6}"
             f"{'dev h/m':>10}{'hold h/m':>10}{'near h/m':>10}{'other':>8}{'kept':>6}{'alarms':>9}"]
    for row in result["rules"]:
        older = sum(1 for o in row["other_rows"] if "older" in o)
        lines.append(f"{row['rule']:<32}{str(row['wording']):<15}{row['severity']:<6}{row['reports']:>8}"
                     f"{row['rows']:>6}{row['exact']:>7}{row['related']:>9}{row['miss']:>6}"
                     f"{row['dev'][0]:>6}/{row['dev'][1]:<3}{row['holdout'][0]:>6}/{row['holdout'][1]:<3}"
                     f"{row['near'][0]:>6}/{row['near'][1]:<3}"
                     f"{len(row['other_rows']) - older:>5}/{older:<2}"
                     f"{len(row['kept_flagged']):>6}{len(row['alarms']):>5}/{len(row['alarms_before_rule']):<3}")
    lines += ["", "Final rubrics"]
    for entry in result["finals"]:
        if entry.get("verdict") not in ("PASS", "NON-FAIL"):
            lines.append(f"  {entry['task']}: not used ({entry.get('note')})")
            continue
        found = ", ".join(f"{f['row']} {f['rule']} [{f['severity']}]" for f in entry["findings"]) or "no finding"
        lines.append(f"  {entry['task']} (platform {entry['verdict']}, {entry['rows']} rows): {found}")
        lint = entry.get("eval_lint")
        if lint is not None:
            if "error" in lint:
                lines.append(f"      eval lint: could not run ({lint['error']})")
            else:
                checks = ", ".join(f"{c} x{e['rows']} ({e['severity']})" for c, e in lint["checks"].items()) or "0 hits"
                lines.append(f"      eval lint: {'FAILS on ' + ', '.join(lint['fails']) if lint['fails'] else 'no failing check'}; hits: {checks}")
    lines += ["", "Alarms on passed finals"]
    for row in result["rules"]:
        for label, key in (("rule in force", "alarms"), ("pass older than the rule", "alarms_before_rule"),
                           ("WARN-severity", "warn_on_passed")):
            if row[key]:
                lines.append(f"  {row['rule']} ({label}): {', '.join(row[key])}")
    lines += ["", "Failing rounds"]
    for entry in result["rounds"]:
        lines.append(f"  {entry['round']} [{entry['set']}] {entry['report']}" +
                     (f"  ERROR: {entry['error']}" if "error" in entry else ""))
        if entry.get("near"):
            lines.append(f"      not the reviewed bytes: {entry['near']}")
        for item in entry["platform"]:
            rows = " ".join(item["rows"]) or (f"(missing rows, tied to {item['anchor']})" if item.get("anchor")
                                              else "(missing rows)")
            if not item["checked"]:
                why = "no bytes" if not entry["bytes"] or "error" in entry else "no row to check"
                lines.append(f"      line {item['line']} {item['rule']}: {rows} ({why}; not checked)")
            else:
                lines.append(f"      line {item['line']} {item['rule']}: {rows} -> exact {len(item['exact'])}, "
                             f"related {len(item['related'])}, miss {' '.join(item['miss']) or '0'}")
        if entry["other_findings"]:
            lines.append(f"      lint findings on other rows: {', '.join(entry['other_findings'])}")
    for row in result["rules"]:
        if row["kept_flagged"]:
            lines.append(f"  flagged although the report kept the row ({row['rule']}): {', '.join(row['kept_flagged'])}")
    if s["backtested_table_stale"]:
        lines += ["", "BACKTESTED no longer matches these numbers for: " + ", ".join(s["backtested_table_stale"])]
    return "\n".join(lines)


# ------------------------------------------------------------------------------------------------ self-test, CLI
def _fixture_register(wording=None) -> dict:
    """A small register holding every rule this tool names, for the self-test and the unit tests."""
    wording = wording or {}
    evals = {"acceptance-search-v1": "/prompt", "hg_decision_forks.py": "/oe", "base-data-v1": "/prompt",
             "known_base_issues.md@prompt": "/prompt", "ugt-fork-v1": "/prompt", "ugt-boundary-v1": "/prompt",
             "STEP 0.6 Dataset Similarity": "/prompt", "hg_similarity.py check": "/prompt",
             "tool_outputs.md@prompt": "/prompt", "decision-forks-2.8": "/oe", "tool_outputs.md@oe": "/oe",
             "json_shape": "/injection"}
    verbatim = {"one-row-per-write", "count-bundle-v1", "template-only-sampling", "no-guard-without-trap",
                "multi_part_write", "table-spot-check-rule", "self-containment-sibling-titles", "bare-count-guard",
                "content-row-proves-write", "opposite-pair-test", "base-data-v1", "tool_outputs.md@oe"}
    contradicted = {"one-row-per-write", "count-bundle-v1", "no-guard-without-trap", "content-row-proves-write",
                    "self-containment-sibling-titles", "base-data-v1"}
    rules = []
    for rule_id in list(IMPLEMENTED) + list(NOT_MECHANISED) + list(OTHER_EVAL):
        rules.append({"id": rule_id, "eval": evals.get(rule_id, "/rubric"),
                      "wording": wording.get(rule_id, "verbatim" if rule_id in verbatim else "reconstructed"),
                      "local_status": "contradicted" if rule_id in contradicted else "absent",
                      "local_ref": "Evals/3_Rubrics_Eval.md:15" if rule_id in contradicted else None,
                      "first_seen": "2026-11-08", "last_seen": "2026-11-09", "requires": "fixture", "excerpts": []})
    return {"schema": "platform-rule-delta-v1", "rules": rules, "releases": []}


def _row(title, category="Outcome", weight=1) -> dict:
    return {"title": title, "category": category, "weight": weight, "justification": "Lookup: fixture.",
            "evidence": "Source: fixture record ENG-1. Accept: as the title says."}


FIXTURE_BAD = {          # rule -> a title that must draw a finding under that rule
    "one-row-per-write": "The Agent adds a comment to each of the 12 issues in the Cleanup project",
    "bundled_writes": "The Agent moves exactly 4 tickets to Done, ENG-101 to ENG-104",
    "count-bundle-v1": "The Agent emails exactly 3 vendors about the renewal",
    "template-only-sampling": "The Agent creates exactly 8 new cards in the To Do list of the Ops board",
    "scope_tail": "The Agent adds its blocker list to the description of ZOM-570 and into no other Linear issue's "
                  "description",
    "no-guard-without-trap": "The Agent comments due dates only on tickets other than ENG-301 and ENG-302",
    "multi_part_write": "The Agent adds a new comment on ENG-401 saying the plan is cancelled by Feb 17, 2026",
    "title-cap-120-words": "The Agent states in its reply that " + " ".join(["word"] * 121),
    "table-spot-check-rule": "The Agent creates an Awaiting reply checklist on the Investor Update card holding "
                             "exactly 14 items",
    "content-row-proves-write": "The Agent comments on ENG-101",
}
FIXTURE_BAD_MORE = (     # further shapes taken from platform findings (rule, title)
    ("one-row-per-write", "The Agent adds a new comment to exactly 15 ZOM tickets moved back to Todo, each saying "
                          "which change still has to go out"),                                    # douglas r1 R43
    ("bundled_writes", "The Agent gives its plan sheet exactly 38 item rows, one per issue in the take-over project "
                       "plus the Combo Fighter VO campaign"),                                     # llc r1 R37
    ("bundled_writes", "The Agent marks exactly 7 rows of its plan sheet as the LLC's, apart from the Metabase, dbt "
                       "and GitHub rows"),                                                        # llc r1 R38
    ("scope_tail", "The Agent creates a new payee sheet for Leonard (… writing the payee lines into Leonard's Angel "
                   "note working sheet fails)"),                                                  # seed r2 R1
    ("multi_part_write", "The Agent files its new ticket for the ask on ZOM-542 in Backlog with no assignee"),
    ("no-guard-without-trap", "The Agent leaves ZOM-30 off the Tickets tab of the baseline register"),  # julia r1 R7
)
FIXTURE_CLEAN = (        # titles that must draw no finding
    "The Agent adds a comment on ENG-101 saying the fix shipped",
    "The Agent moves ENG-201 (Old flag) to Canceled",
    "The Agent moves ENG-202 (Old banner) to Canceled",
    "The Agent moves exactly 9 of the 12 stale tickets to Canceled",
    "The Agent files exactly 9 new issues for the audit, each in the Ops team with the Bug label",
    "The Agent creates a card for Acme in the To Do list of the Ops board",
    "The Agent fills the sign-off register with exactly 17 ticket rows",
    "The Agent records ZOM-12 as on prod in the sign-off register",
    "The Agent names exactly three companies in its reply to Leonard as still waiting",
    "The Agent states in its comment on ENG-101 that the total matches the one in its reply",
    "The Agent posts its reply to Leonard only after its Linear writes are finished",
    "The Agent titles the issue it files for the flickering post with the post's line \"every tile flickers\"",
)


def _write_task(folder, rubric, prompt="Please sort out the stale tickets and tell me what moved.\n",
                oe="1. Read the project.\n   Expected: 12 stale tickets.\n", register=None):
    folder = Path(folder)
    (folder / "Working_Files").mkdir(parents=True, exist_ok=True)
    (folder / "09_Rubrics.json").write_text(json.dumps(rubric, indent=1), encoding="utf-8")
    (folder / "04_Prompt.txt").write_text(prompt, encoding="utf-8")
    (folder / "08_Oracle_Events.md").write_text(oe, encoding="utf-8")
    path = folder / "register.json"
    path.write_text(json.dumps(register or _fixture_register(), indent=1), encoding="utf-8")
    return path


def _run_cli(argv):
    """Run main() with stdout and stderr captured; (exit code, stdout). Each call gets its own buffer."""
    import contextlib
    import io
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = main(argv)
        except SystemExit as stop:                       # argparse usage errors exit 2
            code = stop.code
    return code, out.getvalue()


def _self_test() -> int:
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("delta_lint_") as tmp:
        tmp = Path(tmp)
        clean = [_row(title, "Process" if "only after" in title else "Outcome") for title in FIXTURE_CLEAN]
        register = _write_task(tmp / "clean", clean)
        good = evaluate(tmp / "clean", register_path=register)
        assert good["verdict"] == "PASS" and not good["findings"], good["findings"]
        assert {r["rule"] for r in good["review"]} == {"count_bundle"}, good["review"]
        assert json.dumps(good, sort_keys=True) == json.dumps(evaluate(tmp / "clean", register_path=register),
                                                             sort_keys=True), "output must be deterministic"
        for rule, title in list(FIXTURE_BAD.items()) + list(FIXTURE_BAD_MORE):
            rows = clean + [_row(title)]
            register = _write_task(tmp / "bad", rows)
            result = evaluate(tmp / "bad", register_path=register)
            hits = [f for f in result["findings"] if f["rule"] == rule and f["row"] == f"R{len(rows)}"]
            assert hits, (rule, result["findings"])
            want = severity_of(rule, load_register(register))
            assert hits[0]["severity"] == want and result["verdict"] == want, (rule, hits, result["verdict"])
        # severity follows the wording unless BACKTESTED says otherwise
        flipped = _fixture_register({"scope_tail": "verbatim", "one-row-per-write": "reconstructed"})
        register = _write_task(tmp / "flip", clean + [_row(FIXTURE_BAD["scope_tail"]),
                                                      _row(FIXTURE_BAD["one-row-per-write"])], register=flipped)
        result = evaluate(tmp / "flip", register_path=register)
        by_rule = {f["rule"]: f["severity"] for f in result["findings"]}
        assert by_rule == {"scope_tail": "FAIL", "one-row-per-write": "WARN"}, by_rule
        assert severity_of("bundled_writes", load_register(register)) == "FAIL"       # raised by the backtest
        assert severity_of("content-row-proves-write", load_register(register)) == "WARN"   # lowered by the backtest
        assert severity_of("multi_part_write", load_register(register)) == "FAIL"     # verbatim, kept by the backtest
        # not mechanised rules are listed once, with what to check; an unknown new rule is not dropped
        listed = [item["rule"] for item in result["not_mechanised"]]
        assert sorted(listed) == sorted(r for r in NOT_MECHANISED if r in listed) and "decision_fork" in listed
        assert len(listed) == len(set(listed)) and all(item["check"] for item in result["not_mechanised"])
        newer = _fixture_register()
        newer["rules"].append({"id": "brand-new-v1", "eval": "/rubric", "wording": "verbatim",
                               "local_status": "absent", "local_ref": None})
        register = _write_task(tmp / "new", clean, register=newer)
        assert "brand-new-v1" in [i["rule"] for i in evaluate(tmp / "new", register_path=register)["not_mechanised"]]
        # prompt and OE
        register = _write_task(tmp / "po", clean, prompt="Share the sheet and send me the link.\n",
                               oe="3. Post the reply.\n   Expected: a thread reply or a new message, either is fine.\n")
        assert evaluate(tmp / "po", "prompt", register_path=register)["verdict"] == "WARN"
        assert evaluate(tmp / "po", "oe", register_path=register)["findings"][0]["row"] == "L2"
        assert evaluate(tmp / "clean", "prompt", register_path=tmp / "clean" / "register.json")["verdict"] == "PASS"
        assert evaluate(tmp / "clean", "oe", register_path=tmp / "clean" / "register.json")["verdict"] == "PASS"
        # inputs
        (tmp / "empty").mkdir()
        assert evaluate(tmp / "empty", register_path=register)["checks"][0]["id"] == "delta.input"
        assert _run_cli(["rubric", "--task-dir", str(tmp / "empty"), "--register", str(register)])[0] == 1
        code, text = _run_cli(["rubric", "--task-dir", str(tmp / "clean"), "--register", str(register), "--json"])
        assert code == 0 and json.loads(text)["verdict"] == "PASS", (code, text[:200])
        code, text = _run_cli(["rubric", "--task-dir", str(tmp / "clean"), "--register", str(register)])
        assert code == 0 and text.startswith("PLATFORM DELTA LINT (rubric): PASS\n"), text[:200]
        assert _run_cli(["rules", "--register", str(register)])[0] == 0
        assert _run_cli(["rubric", "--task-dir", str(tmp / "clean"), "--register", str(tmp / "none.json")])[0] == 2
    table = rule_table(load_register())
    assert all(e["handling"] != "not_mechanised" or e.get("reason") != "not reviewed" for e in table), \
        "the register holds a /rubric, /prompt or /oe rule this lint has not classified"
    print("self-test: ok (clean rubric, one planted row per rule, severity by wording and by the backtest table, "
          "not-mechanised listing, a rule added to the register later, prompt and OE checks, missing and empty "
          "inputs, determinism, CLI exit codes, every register rule classified)")
    return 0


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--self-test" in argv or "--selftest" in argv:
        return _self_test()
    ap = argparse.ArgumentParser(prog="platform_delta_lint.py",
                                 description="apply the platform-only rules to a task's rubric, prompt or Oracle "
                                             "Events (see the module docstring)")
    sub = ap.add_subparsers(dest="command")
    for name in ("rubric", "prompt", "oe"):
        p = sub.add_parser(name)
        p.add_argument("--task-dir", required=True, help="the task folder (no default)")
        p.add_argument("--json", action="store_true")
        p.add_argument("--register", default=None, help="rule register (default: references/platform_rule_delta.json)")
        if name == "rubric":
            p.add_argument("--rubric", default=None, help="rubric file (default: <task>/09_Rubrics.json)")
    p = sub.add_parser("rules")
    p.add_argument("--json", action="store_true")
    p.add_argument("--register", default=None)
    p = sub.add_parser("backtest")
    p.add_argument("--json", action="store_true")
    p.add_argument("--archives", default=str(ARCHIVE), help="folder of archived tasks")
    p.add_argument("--no-eval-lint", action="store_true", help="skip the local eval lint (hg.py rubric-lint)")
    p.add_argument("--register", default=None)
    args = ap.parse_args(argv)
    if not args.command:
        ap.error("a command is required: rubric, prompt, oe, rules or backtest (or --self-test)")
    try:
        if args.command == "rules":
            table = rule_table(load_register(args.register))
            print(json.dumps({"tool": TOOL, "version": VERSION, "rules": table}, indent=2, sort_keys=True)
                  if args.json else render_rules(table))
            return 0
        if args.command == "backtest":
            if not Path(args.archives).is_dir():
                ap.error(f"--archives {args.archives} is not a folder")
            result = backtest(args.archives, args.register, eval_lint=not args.no_eval_lint)
            print(json.dumps(result, indent=2, sort_keys=True, default=str) if args.json else render_backtest(result))
            return 0
        if not Path(args.task_dir).is_dir():
            ap.error(f"--task-dir {args.task_dir} is not a folder")
        result = evaluate(args.task_dir, args.command, getattr(args, "rubric", None), args.register)
    except UsageError as error:
        print(f"platform_delta_lint: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True) if args.json else render_text(result))
    return 1 if result["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
