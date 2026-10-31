#!/usr/bin/env python3
"""stage_gate.py - mechanical stage gates for the Task_Authoring harness (Spec V2/V3).

A stage is not handed off because its author says it is done. This tool reads the stage's
output artifact(s) and blocks handoff unless the artifact is complete, fresh, evidenced,
self-reviewed and, where the stage needs it, proven from
the persona's view and the universe knowledge base. Deterministic, read-only on every
input, stdlib only (Python 3.9). Run from the workspace root:

  python3 Task_Authoring/tools/stage_gate.py <stage> <task_dir> [--json] [--rerun all|lint] [--paste]
  python3 Task_Authoring/tools/stage_gate.py --list
  python3 Task_Authoring/tools/stage_gate.py --self-test     (reruns itself inside a tools/selftest_sandbox.py
              workspace, so the cache writers it reaches never write a shared file; scratch: support/scratch/)

<stage>     scenario · injection · hardening · reference-files · error-async · prompt-writing ·
            prompt-check · humantime · oe-writing · oe-check · rubric-writing · rubric-check ·
            allfail · difficulty · release
<task_dir>  the task folder holding the slots (normally Task_Authoring/task_inputs).

CHECK FAMILIES (each check prints PASS / FAIL / WARN / SKIP with file:line locations)
  structure.*   required outputs and inputs exist; every output is newer than every input
                it was built from (staleness); required headings present and non-empty; no
                placeholders (<...> template slots, TODO/TBD/FIXME, empty table rows,
                unchecked boxes, unresolved [ a | b ] choices).
  evidence.*    every factual row in the named sections carries a source pointer or record
                id (Slack C.../ts, f_/d_+22 hex, evt_, ENG-n, repo#n, mailbox/id, page_, cmt_,
                24-hex Trello/Contacts ids, JSON pointers, SQL lines, F-ids ...) at the
                stage's minimum ratio; quoted spans are exact substrings of the human file.
  tool.*        tool outputs pasted verbatim where the playbook requires them, re-run and
                compared when cheap: sql_lint, injection lint (hg.py lint, the eval's static
                linter: any FAIL, error payload, stale sha256 or undispositioned CHECK blocks),
                base_check, hardness_gate, difficulty_stats, persona_view reach / check-sql /
                can-see, entity.py output.
  review.*      a Self-review section exists, holds >= N evidenced counter-readings (N
                scales with the artifact), names what the stage must cover, lists unresolved.
  reach.*       every load-bearing scoped record (rows in reach sections, Facts for the human,
                discovery map, ledger B, rows marked `LB`) is YES for the assigned persona via
                persona_view (check-sql semantics when the SQL exists). NO blocks unless the
                row carries `DENIAL-INTENDED: <reason>`; UNVERIFIED blocks unless it carries
                `UNVERIFIED-OK: <reason>`. Either marker makes the row a probe, never load-bearing:
                it must also list `alternate_evidence_ids: <ids>` that are all YES, and must not
                carry `LB` (red team A, R1 #3).
  anchor naming boundary.anchor_naming (scenario, injection, prompt-writing): every anchor-naming entry
                (a table column 'anchor name' / 'may be named' / 'noun phrase', an 'Anchor An name:'
                line, the manifest's anchors[].prompt_reference) is a noun phrase of <= 6 words — no
                imperative verb at the start, no second-person request (red team A, R2 #3).
  revision      scenario writes 01_Hardness_Manifest.draft.json; injection writes the final
                01_Hardness_Manifest.json, which keeps every draft id or records it in `design_delta`
                (structure.design_delta). Hardening is revision N+1: its gate re-runs the injection
                checks on the current SQL + manifest (revision.injection) and certifies their digests.
  kb.*          universe KB use: coherence_hazards ids (validated) per QC category, activity
                status for every seeded speaker, integrations companions per seeded service,
                cohorts / trap_catalog / timeline citations, conventions, entity collisions.
                Honors source.kb_status: bound = blocking membership; reference-only = membership
                WARNs ("cite record locators"); unavailable = membership skipped with a WARN and
                evidence.kb_locators requires a record locator in every KB-dependent section.
  chain.*       the upstream stage's artifact carries a pasted `STAGE GATE <stage>: PASS`
                block whose digests still match the files (stale upstream = blocked).
  handoff.*     this stage's own PASS block pasted into its Self-review (WARN until pasted;
                the next stage makes it blocking). `--paste` inserts it for you on PASS.
  tier.*        prompt-check: manifest present, its effective_profile fits the assignment's tier (Long Horizon →
                extreme; Normal → normal, or extreme with a recorded profile_exception), and the dossier's
                hardness_gate PASS for that profile pasted and current; re-run under --rerun all.
  provenance.*  oe-writing: every opaque §B locator traces to the prompt, an earlier fact's Expected data
                (topological Depends-on) or a natural `search "<query>"` re-run as the persona.
  validity.*    rubric-writing: predicted all-fail rows = 0; rubric-check: binary validity gate (incorrect /
                unauthorized / unobservable / contradiction / missing coverage / predicted all-fail block
                whatever the percentage tally).
  diversity.*   rubric-writing: no unit of discovery (authority or tool response, transitive) > 50% of weight.
  release.*     `release` stage (final, before submit): every certificate current, one bundle digest matching
                every stage-recorded digest, no PROVISIONAL/UNRESOLVED/UNVERIFIED marker, OE solvability
                SUPPORTED_BY_OE, difficulty gates clear, 06_PreCheck_Trajectory/trajectory.json present. Writes 13_Release_Gate.txt.

Fold-hardening families (plans/Fold_Hardening_Into_Scenario_And_Injection.md §4.2, §8):
  surface.*     scenario: Working_Files/01_Gradable_Surface.json present and valid under tools/gradable_surface.py
                (structure, 1/3/5 work-kind weights, <= 5 samples per group plus a volume row, exceptions an authority
                singles out, no fact in >= 3 slots, known mechanism ids: each printed with its basis). blocking
                The geometry (mechanism share, always-pass share) is reported, never gated.
  surface.coverage  rubric-writing / rubric-check: when the surface exists, every slot has a covering row or a
                written disposition (gate 17, following missing_coverage).                          blocking
  tool.redteam_dual  scenario: both reviews ran (a tool-error stub such as "set REDTEAM_MODEL" is not a review), or a
                `RED TEAM FALLBACK: <who reviewed instead and why>` line is recorded. No silent skip. blocking
  solver.* mutation.* geometry.*  injection: Working_Files/01c_Preflight_Report.json (tools/preflight_report.py) bound by
                sha256 to the current SQL, solver, surface, manifest and dispositions; solver contract PASS; a written
                disposition for every mutation result (01c_Dispositions.json); geometry U > 1 - cap. --rerun all re-runs
                the solver contract and the geometry in-process.                                  blocking
  geometry.margin · liveness.* · forecast.*  L_max >= (1 - cap) + 0.10, a written disposition for every liveness
                flag, a pre-registered forecast (UNCALIBRATED).                                    advisory (WARN)
  revise.*      scenario --revise (S0r): when a /create-hardening MODE B report exists, the design's revision-intake
                section dispositions every proposed node verdict, keeps every export BOUND on evidence to its own
                revision (trajectory_ledger.binding_ok: never an unchecked SINGLE) or marked historical, cites
                run steps (evidence.register_run_step) and meets the counter-reading minimum - both copied from
                `hardening`, which keeps them.                                                      blocking

Digests: `<file>#<12 hex>` = sha256 of the file with every STAGE GATE output line removed,
so pasting the block does not change the digest but any later edit does.

Exit: 0 PASS · 1 FAIL (any blocking check) or PARTIAL (--rerun lint skipped a re-run) · 2 usage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
KB = BUNDLE / "references" / "universe_kb"
SPEC = BUNDLE / "references" / "Hardness_Manifest_Spec.md"
FIXTURES = BUNDLE / "support" / "examples" / "calibration" / "stage_gate"
SELFTEST_TMP = BUNDLE / "support" / "scratch"     # the self-test scratch root: one mkdtemp folder per run, removed
PY = sys.executable or "python3"

# ------------------------------------------------------------------ patterns

RX_ID = re.compile("|".join([
    r"\b[CDG](?=[A-Z0-9]*\d)[A-Z0-9]{8,11}\b",              # Slack channel / DM
    r"\b\d{10}\.\d{6}\b",                                     # Slack ts
    r"\b[fd]_[0-9a-f]{22}\b",                                 # Drive family
    r"\bevt_[0-9a-f]{8,}\b",                                  # GCal
    r"\b(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}\b", r"\busr_[0-9a-f]{8,}\b", r"\bteam_[A-Z]{3}\b",  # Linear
    r"\b[\w.-]+#\d+(?:#(?:c|rev|rc|ev)_\d+)?", r"#(?:c|rev|rc|ev)_\d+\b",              # GitHub
    r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+/\S+", r"<[^<>\s|]+@[^<>\s|]+>",                    # Gmail
    r"[\w.+-]+@[\w.-]+_\d+\.json",                            # Gmail export file
    r"\b[0-9a-f]{24}\b", r"\b[0-9a-f]{32}\b",                 # Trello / Contacts · Slack message id
    r"\bpage_[\w-]+", r"\bcmt_\w+", r"\buser_[A-Z]+_\d+\b",  # Confluence
    r"\bwh_\w+", r"\bsnowflake\.\w+",                         # Snowflake
    r"[\w./-]+\.json\b\s*(?:#|:)?\s*/[\w/.~-]+", r"--pointer\s+\S+",                  # JSON pointers
    r"\bSQL\s*(?:line\s*|L)\d+", r"\.sql:\d+", r"\bline\s+\d+\b",                      # SQL lines
    r"\bINT-\d{2}\b",                                         # universe_kb integrations
]))
RX_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+|\b(?:PERSON|EMPLOYEE|SVC)_\d{4}_EMAIL\b")
RX_FID = re.compile(r"\bF\d{1,3}\b")
RX_EVID = re.compile(RX_ID.pattern + r"|§\s?\d|\b[FRPTKHCG]\d{1,3}\b|\brun-\d\b|\bL\d+\b|"
                     r"[\w-]+\.(?:json|md|sql|txt|csv)\b|\bcase[_ ]?\w*\d|\bhg\.py\b|\bpersona_view\b|"
                     r"\b[TSRQLI]\d{2}\b|\bEval\s*\d")
SCOPED = re.compile(r"(?P<gmail>[\w.+-]+@[\w-]+(?:\.[\w-]+)+/[^\s|`'\"),;\]]+)"
                    r"|(?P<gcal>\bevt_[0-9a-f]{10,}\b)"
                    r"|(?P<drive>\b[fd]_[0-9a-f]{22}\b)"
                    r"|(?P<slack>\b[CDG](?=[A-Z0-9]*\d)[A-Z0-9]{8,11}(?:/\d{10}\.\d{6})?\b)")
RX_CANSEE = re.compile(r"^\s*(?:[-*>]\s*)?`?([a-z_]+) (gmail|slack|gcal|gdrive|gdocs|gsheets|gslides) (\S+?):`? "
                       r"(YES|NO|UNVERIFIED)\b")
RX_CHECKSQL_ROW = re.compile(r"^\s*\[(YES|NO|UNVERIFIED)(?: LB)?\] (.+?) - ")
RX_GATE_LINE = re.compile(r"^\s*(?:STAGE GATE \S+: |\[(?:PASS|FAIL|WARN|SKIP|INFO)\] )")
RX_GATE_HEAD = re.compile(r"STAGE GATE (\S+): (PASS|FAIL|PARTIAL)\b(.*)$")
TOOL_HEAD = re.compile(r"^\s*(STAGE GATE |\[(?:PASS|FAIL|WARN|SKIP)\] |HARDNESS GATE |BASE CHECK |schemas touched \(|"
                       r"errors: \d|CHECK-SQL as |REACH  |SEARCH \w+ |SHARED_FIRST_NAMES|ENTITY |WHO-CAN-SEE |"
                       r"\| Rollout \||\| Gate \||FACT[ _]CHECK|SHORTCUT PROBE |"
                       r"[a-z_]+ (?:gmail|slack|gcal|gdrive|gdocs|gsheets|gslides) \S+: )",
                       re.I)
# opaque ids / high-information exact locators (locator provenance, 08 hard gate 12)
OPAQUE = re.compile("|".join([
    r"\b[CDG](?=[A-Z0-9]*\d)[A-Z0-9]{8,11}(?:/\d{10}\.\d{6})?\b", r"\b\d{10}\.\d{6}\b",
    r"\b[fd]_[0-9a-f]{22}\b", r"\bevt_[0-9a-f]{8,}\b", r"\b(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}\b", r"\busr_[0-9a-f]{8,}\b",
    r"\b[\w.-]+#\d+\b", r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+/[^\s|`'\"),;\]]+", r"\b[0-9a-f]{24}\b", r"\b[0-9a-f]{32}\b",
    r"\bpage_[\w-]+", r"\bcmt_\w+"]))
RX_SEARCH_ORIGIN = re.compile(r"\bsearch\s*:?\s*[\"“`]([^\"”`]+)[\"”`]", re.I)
ALLFAIL_BASES = re.compile(r"target_data_absent|required_tool_absent|filter_impossible|entity_unreachable")
VALIDITY_TYPES = {"incorrect", "unauthorized", "unobservable", "missing_coverage"}
SERVICE_WORDS = [("gmail", r"gmail|mail"), ("slack", r"slack"), ("gcal", r"gcal|calendar"), ("gdocs", r"\bdocs?\b|gdocs"),
                 ("gsheets", r"sheets?|gsheets"), ("gslides", r"slides|gslides"), ("gdrive", r"drive|gdrive")]

ERROR_FUNCS = {"slack_send_message", "slack_conversations_history", "slack_search_public_and_private",
               "gmail_search_messages", "gmail_get_message", "github_get_file_contents", "github_create_issue",
               "github_create_pull_request", "github_search_code", "linear_create_issue", "linear_list_issues",
               "trello_create_card", "gdrive_search", "gdrive_read_file", "gsheets_values_get", "gcal_list_events",
               "gdocs_get_document", "gslides_get_presentation"}
WAIT_FUNCS = {"gmail_submit_search_messages", "slack_submit_search", "gdrive_submit_search",
              "github_submit_search_code", "linear_submit_list_issues", "trello_submit_search"}
RUBRIC_TYPES = {"missing_coverage", "not_self_contained", "non_atomic", "incorrect", "unauthorized", "unobservable",
                "non_agent_centric", "overly_specific", "overly_broad", "duplicate", "category", "vague_exemplar",
                "harmless_specificity", "—", "-", "none"}
QC_CATS = [("temporal", r"temporal"), ("semantic", r"semantic|category"), ("referential", r"referential|cross-service"),
           ("quantitative", r"quantitative|reconciliation"), ("state/lifecycle", r"state|lifecycle"),
           ("identifier/format", r"identifier|format"), ("other", r"\bother\b")]
HAZ_CATS = {"T": "temporal", "S": "semantic", "R": "referential", "Q": "quantitative", "L": "state|lifecycle",
            "I": "identifier|format"}
INT_SOURCE_SCHEMA = {"github": "github", "linear": "linear", "gcal": "gcal", "google_drive": "gdrive", "slack": "slack",
                     "trello": "trello", "gmail": "gmail"}
SLOT_ORDER = ["00_Assigments.md", "01b_Redteam_Review.md", "01b_Redteam_Review.second.md",
              "01_Scenario_Design.md", "01_Hardness_Manifest.draft.json", "01_Gradable_Surface.json",
              "01_Universe_Inject.sql", "01_Hardness_Manifest.json", "01_Grounding_Dossier.md", "solver/solver.py",
              "01c_Dispositions.json", "01c_Preflight_Report.json", "01c_Preflight_Report.md",
              "01a_Hardening_Report.md", "03_Error_Async_Config.txt", "02_Reference_Files",
              "02_Reference_Files_Manifest.md", "04_Prompt_Writing_Brief.md", "04_Prompt.txt", "04_Prompt_Check.md",
              "06_PreCheck_Trajectory", "07_Baseline_Trajectories", "08_OE_Writing_Ledger.md",
              "08_Oracle_Events.md", "05_Human_Time_Worksheet.md", "08_OE_Check.md", "09_Rubric_Writing_Plan.md", "09_Rubrics.json",
              "09_Rubric_Check.md", "10_Baseline_Verifier_Results.md", "12_difficulty_input.json",
              "11_AF_Justification.md", "12_Difficulty_Stats.txt", "13_Release_Gate.txt"]
# The platform slots sit at the top of the task folder (references/Tasks_Template); every artifact the
# commands generate lives in WORK_DIR beside them.
TEMPLATE_SLOTS = {"00_Assigments.md", "01_Universe_Inject.sql", "02_Reference_Files", "03_Error_Async_Config.txt",
                  "04_Prompt.txt", "05_Human_Time.md", "06_PreCheck_Trajectory", "07_Baseline_Trajectories",
                  "08_Oracle_Events.md", "09_Rubrics.json", "10_Baseline_Verifier_Results.md", "11_AF_Justification.md",
                  "Audit-Report"}
WORK_DIR = "Working_Files"


def slot_path(task_dir, name) -> Path:
    """Template slots resolve at the top of the task folder, generated artifacts under WORK_DIR (a flat legacy
    layout is still read when only the top-level copy exists)."""
    td = Path(task_dir)
    head = str(name).split("/", 1)[0]
    if head in TEMPLATE_SLOTS or head == WORK_DIR:
        return td / name
    work, flat = td / WORK_DIR / name, td / name
    return flat if flat.exists() and not work.exists() else work

# ------------------------------------------------------------------ markdown model


def split_cells(line: str) -> list:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, tick = [], [], False
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur).strip())
    return cells


class Table:
    def __init__(self, header, rows):
        self.header = header          # list of cells
        self.rows = rows              # list of (line_idx, cells)

    def col(self, rx):
        for i, h in enumerate(self.header):
            if re.search(rx, h, re.I):
                return i
        return None

    def cell(self, cells, idx):
        return cells[idx] if idx is not None and idx < len(cells) else ""


class Doc:
    def __init__(self, path: Path, rel: str):
        self.path, self.rel = path, rel
        self.exists = path.is_file()
        self.text = path.read_text(errors="replace") if self.exists else ""
        self.lines = self.text.splitlines()
        n = len(self.lines)
        self.fence, self.toolfence = [False] * n, [False] * n
        i = 0
        while i < n:
            if self.lines[i].lstrip().startswith("```"):
                j = i + 1
                while j < n and not self.lines[j].lstrip().startswith("```"):
                    j += 1
                first = next((self.lines[k] for k in range(i + 1, min(j, n)) if self.lines[k].strip()), "")
                tool = bool(TOOL_HEAD.match(first))
                for k in range(i, min(j + 1, n)):
                    self.fence[k], self.toolfence[k] = True, tool
                i = j + 1
            else:
                i += 1
        # unfenced tool output blocks (a gate block pasted without fences, plain-text artifacts)
        for i, l in enumerate(self.lines):
            if not self.fence[i] and RX_GATE_LINE.match(l):
                self.toolfence[i] = True
        self.heads = []
        for i, l in enumerate(self.lines):
            if self.fence[i]:
                continue
            m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", l)
            if m:
                self.heads.append((i, len(m.group(1)), m.group(2)))
            elif re.match(r"^\s*Self[- ]review\s*:", l, re.I):
                self.heads.append((i, 2, "Self-review"))

    def loc(self, i):
        return f"{self.rel}:L{i + 1}"

    def sections(self, rx):
        out = []
        for k, (i, lv, t) in enumerate(self.heads):
            if re.search(rx, t, re.I):
                end = len(self.lines)
                for (j, lv2, _) in self.heads[k + 1:]:
                    if lv2 <= lv:
                        end = j
                        break
                out.append(Section(self, t, lv, i, end))
        return out

    def whole(self):
        return Section(self, "(whole file)", 0, -1, len(self.lines))


class Section:
    def __init__(self, doc, title, level, start, end):
        self.doc, self.title, self.level, self.start, self.end = doc, title, level, start, end

    def idx(self, tools=False):
        return [i for i in range(self.start + 1, self.end) if tools or not self.doc.toolfence[i]]

    def text(self, tools=True):
        return "\n".join(self.doc.lines[i] for i in self.idx(tools))

    def content_lines(self):
        out = []
        for i in self.idx(tools=True):
            l = self.doc.lines[i].strip()
            if not l or l.startswith("```") or re.match(r"^\|?\s*:?-{2,}", l) or re.match(r"^#{1,6}\s", l):
                continue
            if len(re.findall(r"[A-Za-z0-9]", l)) >= 3:
                out.append(i)
        return out

    def tables(self):
        out, cur = [], []
        for i in self.idx() + [None]:
            l = self.doc.lines[i].strip() if i is not None else ""
            if i is not None and l.startswith("|") and not self.doc.fence[i]:
                cur.append(i)
                continue
            if len(cur) >= 2 and re.match(r"^\|?\s*:?-{2,}", self.doc.lines[cur[1]].strip()):
                out.append(Table(split_cells(self.doc.lines[cur[0]]),
                                 [(j, split_cells(self.doc.lines[j])) for j in cur[2:]]))
            cur = []
        return out

    def rows(self):
        return [(i, c, t) for t in self.tables() for (i, c) in t.rows]

    def items(self):
        """table data rows + bullet / numbered list lines, as (line_idx, text)."""
        out = [(i, " | ".join(c)) for (i, c, _) in self.rows()]
        for i in self.idx():
            if self.doc.fence[i]:
                continue
            if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+\S", self.doc.lines[i]):
                out.append((i, self.doc.lines[i]))
        return sorted(out)


def strip_verbatim(s: str) -> str:
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"\"[^\"]*\"", " ", s)
    s = re.sub(r"“[^”]*”", " ", s)
    s = re.sub(r"<[^<>\s]+@[^<>\s]+>", " ", s)
    return s


def quoted_spans(cell: str) -> list:
    spans = re.findall(r"\"([^\"]+)\"|“([^”]+)”|`([^`]+)`", cell)
    out = [next(x for x in t if x) for t in spans]
    if not out:
        c = cell.strip()
        out = [c] if c else []
    frags = []
    for s in out:
        frags += [f.strip() for f in re.split(r"…|\.\.\.", s) if f.strip()]
    return frags


def digest_text(text: str) -> str:
    """sha256 over the non-blank lines that are not STAGE GATE output (fences left empty are dropped)."""
    lines = [l.strip() for l in text.splitlines() if l.strip() and not RX_GATE_LINE.match(l)]
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith("```") and i + 1 < len(lines) and lines[i + 1] == "```":
            i += 2
            continue
        out.append(lines[i])
        i += 1
    return hashlib.sha256("\n".join(out).encode()).hexdigest()[:12]


def file_digest(p: Path) -> str:
    if p.is_dir():
        h = hashlib.sha256()
        for f in sorted(x for x in p.rglob("*") if x.is_file()):
            h.update(f.name.encode() + f.read_bytes())
        return h.hexdigest()[:12]
    if p.suffix in (".md", ".txt"):
        return digest_text(p.read_text(errors="replace"))
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def mtime(p: Path) -> float:
    if p.is_dir():
        ts = [f.stat().st_mtime for f in p.rglob("*") if f.is_file() and f.name != ".DS_Store"]
        return max(ts) if ts else 0.0
    return p.stat().st_mtime


_KB = {}


def kb(name: str):
    if name not in _KB:
        data = json.loads((KB / name).read_text())
        if globals().get("TASK_CONTEXT"):
            from runtime_context import validate_kb
            data = validate_kb(data, globals())
        _KB[name] = data
    return _KB[name]

# ------------------------------------------------------------------ context


class Ctx:
    def __init__(self, stage, task_dir: Path, rerun="all", selftest=False):
        self.stage, self.td, self.rerun, self.selftest = stage, Path(task_dir), rerun, selftest
        self.res, self.docs = [], {}
        self._u, self._p, self._pv = None, False, None
        self.skipped = []
        self.context = None
        self.v3 = False

    def p(self, name):
        return slot_path(self.td, name)

    def doc(self, name) -> Doc:
        if name not in self.docs:
            self.docs[name] = Doc(self.p(name), name)
        return self.docs[name]

    def add(self, cid, ok, detail, locs=(), block=True, status=None):
        st = status or ("PASS" if ok else ("FAIL" if block else "WARN"))
        self.res.append({"id": cid, "status": st, "blocking": bool(block and st == "FAIL"), "detail": detail,
                         "locations": list(locs)[:25], "more": max(0, len(list(locs)) - 25)})

    def skip(self, cid, detail):
        self.skipped.append(cid)
        self.add(cid, True, detail, status="SKIP")

    # persona_view (in process; caches live in support/local_search/cache)
    def pv(self):
        if self._pv is None:
            sys.path.insert(0, str(HERE))
            import persona_view  # noqa: E402
            self._pv = persona_view
        return self._pv

    def universe(self):
        if self._u is None:
            self._u = self.pv().Universe()
        return self._u

    def persona(self):
        if self._p is False:
            self._p = None
            if self.context:
                self._p = self.pv().resolve_persona(self.context["persona_key"])
                return self._p
            d = self.doc("00_Assigments.md")
            for rx in (r"^\s*persona_key:\s*([a-z_]+)", r"^\s*email:\s*(\S+@\S+)", r"^\s*persona_name:\s*(.+?)\s*$"):
                m = re.search(rx, d.text, re.M)
                if m:
                    try:
                        self._p = self.pv().resolve_persona(m.group(1).strip())
                        break
                    except (SystemExit, KeyError, ValueError):
                        continue
        return self._p


def assignment_context(ctx):
    """V3 must be explicit; old calibration fixtures retain their documented legacy behavior."""
    text = ctx.doc("00_Assigments.md").text
    ctx.v3 = bool(re.search(r"^\s*spec_version:\s*V3\s*$|^# .*Inputs.*V3\b|^.*Difficulty Mode\s*$", text, re.M | re.I))
    try:
        from task_context import is_v3_assignment
        ctx.v3 = ctx.v3 or is_v3_assignment(text)
    except ImportError:
        pass
    if not ctx.v3:
        return True
    try:
        sys.path.insert(0, str(HERE))
        from task_context import load_context
        ctx.context = load_context(ctx.td, require_source=True)
        from runtime_context import activate
        activate(globals(), task_dir=ctx.td, require_source=True)
    except Exception as exc:
        ctx.add("assignment.v3_context", False, f"V3 assignment/source context unavailable: {exc}")
        return False
    ctx.add("assignment.v3_context", True,
            f"{ctx.context['persona_name']} / {ctx.context['persona_role']}; "
            f"{ctx.context['difficulty_mode']} cap <{ctx.context['difficulty_cap']:.0%}; "
            f"freeze {ctx.context['freeze_utc']}; selected universe available; record dates and freeze-state "
            f"evidence checked separately")
    source = ctx.context.get("source") or {}
    uni = ctx.context.get("universe") or {}
    mode = source.get("mode")
    key = uni.get("key") or source.get("universe")
    ok = mode in ("universe", "snapshot") and (mode != "universe" or bool(key))
    ctx.add("assignment.source_mode", ok,
            (f"source mode {mode!r} for universe {key or '?'}; "
             f"KB {source.get('kb_status') or 'bound'}; clock {uni.get('clock_line') or 'unset'}") if ok else
            (f"source mode 'shared-universe' is retired: use 'universe' with a universe block" if mode ==
             "shared-universe" else f"source mode {mode!r} is not a universe/snapshot source"
             + ("" if key else "; the universe key is unset")))
    return ok


def virtual_digests(ctx, stage):
    if not ctx.context:
        return {}
    from v3_artifact_checks import review_digest
    files = sorted(HERE.glob("*.py"))
    policy = hashlib.sha256(b"".join(p.read_bytes() for p in files)).hexdigest()[:12]
    return {"__context__": str(ctx.context["context_hash"])[:12],
            "__assignment__": str(ctx.context["assignment_hash"])[:12],
            "__policy__": str(ctx.context["policy_hash"])[:12],
            "__gate_policy__": policy, "__review__": review_digest(stage, ctx.td)}


def certificate_digests(ctx, stage=None):
    stage = stage or ctx.stage
    spec = STAGES[stage]
    names = spec["outputs"] + spec.get("digest_extra", [])
    if ctx.v3:
        names += spec["inputs"] + spec["optional"]
        if stage == "release":
            names += ["06_PreCheck_Trajectory", "07_Baseline_Trajectories", "10_Baseline_Verifier_Results.md",
                      "12_difficulty_input.json", "12_Difficulty_Stats.txt"]
    digs = {f: file_digest(ctx.p(f)) for f in dict.fromkeys(names) if ctx.p(f).exists()}
    digs.update(virtual_digests(ctx, stage))
    return digs


def certificate_staleness(ctx, stage, digs):
    virtual = virtual_digests(ctx, stage)
    stale = []
    for name, old in digs.items():
        now = virtual.get(name) if name.startswith("__") else (
            file_digest(ctx.p(name)) if ctx.p(name).exists() else None)
        if now != old:
            stale.append(f"{name} (pasted {old}, now {now or 'missing'})")
    if ctx.v3:
        required = certificate_digests(ctx, stage)
        stale += [f"{name} (not certified)" for name in required if name not in digs]
    return stale

# ------------------------------------------------------------------ generic checks


def files_exist(ctx, files, kind="output"):
    missing = [f for f in files if not ctx.p(f).exists()]
    ctx.add(f"structure.{kind}s", not missing,
            (f"missing {kind}(s): {', '.join(missing)} — stop and name it" if missing
             else f"{len(files)} {kind}(s) present: {', '.join(files)}"))
    return not missing


def staleness(ctx, outputs, inputs):
    outs = [f for f in outputs if ctx.p(f).exists()]
    ins = [f for f in inputs if ctx.p(f).exists()]
    if not outs or not ins:
        ctx.add("structure.fresh", True, "no input/output pair to compare")
        return
    stale = []
    for o in outs:
        for i in ins:
            if mtime(ctx.p(i)) > mtime(ctx.p(o)) + 1e-6:
                stale.append(f"{o} older than its input {i}")
    ctx.add("structure.fresh", not stale, "; ".join(stale) + " — re-run the stage on the current inputs" if stale
            else f"every output newer than its inputs ({', '.join(ins)})")


def sections_present(ctx, doc, specs):
    bad, locs = [], []
    for label, rx in specs:
        secs = doc.sections(rx)
        if not secs:
            bad.append(f"missing '{label}'")
            continue
        if not any(s.content_lines() for s in secs):
            bad.append(f"empty '{label}'")
            locs.append(doc.loc(secs[0].start))
    ctx.add("structure.sections", not bad, ("; ".join(bad) if bad else f"{len(specs)} required sections present and non-empty")
            + f" ({doc.rel})", locs)


HTML = re.compile(r"^/?(?:br|b|i|u|p|em|strong|code|pre|sub|sup|details|summary|div|span|a|ul|ol|li|table|tr|td|th|"
                  r"img|hr|kbd)\b", re.I)


def placeholders(ctx, doc, allow_boxes_rx=None):
    allowed = set()
    if allow_boxes_rx:
        for s in doc.sections(allow_boxes_rx):
            allowed.update(range(s.start, s.end))
    hits = []
    for i, raw in enumerate(doc.lines):
        if doc.toolfence[i]:
            continue
        line = re.sub(r"`[^`]*`", " ", raw)
        for m in re.finditer(r"<([^<>\n]{1,60})>", line):
            c = m.group(1).strip()
            if "@" in c or c[:1] in "@#!/=-" or HTML.match(c) or "=" in c or not re.search(r"[A-Za-z…]|\.\.\.", c):
                continue
            if c in ("…", "...") or re.fullmatch(r"[A-Za-z…][\w .,:/|'’…-]*", c):
                hits.append((i, f"template slot <{c}>"))
        if re.search(r"(?<![\w-])(?:TODO|TBD|FIXME|XXX)(?![\w-])", strip_verbatim(line)):
            hits.append((i, "TODO/TBD marker"))
        if i not in allowed and (re.search(r"^\s*[-*]\s*\[ \]", line) or "☐" in line):
            hits.append((i, "unchecked box"))
        if re.search(r"\[\s*\]|\[ *[\w/-]+(?: +\| +[\w/-]+)+ *\]", line) and not re.match(r"^\s*[-*]\s*\[ \]\s+\S", line):
            hits.append((i, "unresolved template choice [ … ]"))
        if raw.strip().startswith("|") and not doc.fence[i] and not re.match(r"^\|?\s*:?-{2,}", raw.strip()):
            cells = split_cells(raw)
            if cells and all(c in ("", "…", "...", "-", "—") for c in cells):
                hits.append((i, "empty table row"))
    ctx.add("structure.placeholders", not hits,
            (f"{len(hits)} placeholder(s) in {doc.rel}: " + "; ".join(f"L{i + 1} {w}" for i, w in hits[:8])) if hits
            else f"no placeholders in {doc.rel}", [doc.loc(i) for i, _ in hits])


def evidence(ctx, doc, label, rx, ratio=1.0, pattern=RX_ID, block=True, require=True, col=None):
    secs = doc.sections(rx)
    items = []
    for s in secs:
        if col:
            for (i, cells, t) in s.rows():
                c = t.col(col)
                items.append((i, t.cell(cells, c) if c is not None else " | ".join(cells)))
        else:
            items += s.items()
    if not items:
        ctx.add(f"evidence.{label}", not require, f"no rows/items found under '{rx}' in {doc.rel}", block=block)
        return
    bad = [(i, t) for i, t in items if not pattern.search(t)]
    got = 1 - len(bad) / len(items)
    ok = got + 1e-9 >= ratio
    ctx.add(f"evidence.{label}", ok,
            f"{len(items) - len(bad)}/{len(items)} items carry a source pointer (min {ratio:.0%})"
            + (f"; unsourced e.g. L{bad[0][0] + 1}: {bad[0][1][:90]!r}" if bad else ""),
            [doc.loc(i) for i, _ in bad] if not ok else [], block=block)


def self_review(ctx, doc, n_min, must_name=(), label="review"):
    secs = doc.sections(r"self[- ]review")
    if not secs:
        ctx.add(f"{label}.present", False, f"no Self-review section in {doc.rel}")
        return
    sec = secs[-1]
    items = sec.items()
    counter_tables = [t for t in sec.tables() if t.col(r"counter")]
    rows_ct = {i for t in counter_tables for (i, _) in t.rows}
    counters = [(i, t) for i, t in items if i in rows_ct or re.search(
        r"counter|strongest|false[- ]positive|false[- ]negative|best (?:case|argument|reading)|could (?:fail|pass)|"
        r"would (?:fail|pass)|\bargue", t, re.I)]
    evid = [(i, t) for i, t in counters if RX_EVID.search(t)]
    ctx.add(f"{label}.counter_readings", len(evid) >= n_min,
            f"{len(evid)} evidenced counter-readings (of {len(counters)} found; need ≥ {n_min}) in {doc.rel}",
            [doc.loc(i) for i, t in counters if not RX_EVID.search(t)])
    txt = "\n".join(l for l in sec.text(tools=True).splitlines() if not RX_GATE_LINE.match(l))
    missing = [name for name, rx in must_name if not re.search(rx, txt, re.I)]
    if must_name:
        ctx.add(f"{label}.coverage", not missing, ("self-review never addresses: " + ", ".join(missing)) if missing
                else f"self-review addresses all {len(must_name)} required items", [doc.loc(sec.start)] if missing else [])
    ctx.add(f"{label}.unresolved", bool(re.search(r"unresolved|left open|open items|unverified", txt, re.I)),
            "unresolved items listed (or 'none')" if re.search(r"unresolved|left open|open items|unverified", txt, re.I)
            else "self-review does not list unresolved items (write 'Unresolved: none' if there are none)",
            [doc.loc(sec.start)])


def pasted(ctx, doc, cid, rx, what, block=True):
    m = re.search(rx, doc.text, re.M)
    ctx.add(cid, bool(m), (f"{what} pasted ({doc.rel}:L{doc.text[:m.start()].count(chr(10)) + 1})" if m
                           else f"{what} not pasted verbatim in {doc.rel}"), block=block)
    return m


def run_tool(args, timeout=600):
    try:
        env = os.environ.copy()
        if not globals().get("TASK_CONTEXT"):
            env["TASK_AUTHORING_LEGACY_V2"] = "1"
        r = subprocess.run([PY] + [str(a) for a in args], cwd=str(WS), capture_output=True, text=True,
                           timeout=timeout, env=env)
        return r.returncode, r.stdout, r.stderr
    except (OSError, subprocess.TimeoutExpired) as e:
        return 99, "", str(e)


def lines_matching(doc, rx):
    return [(i, l) for i, l in enumerate(doc.lines) if rx.search(l)]

# ------------------------------------------------------------------ persona reach


def scoped_ids(text):
    out = []
    for m in SCOPED.finditer(text):
        svc = m.lastgroup
        v = m.group(0).rstrip(".")
        out.append(("gdrive" if svc == "drive" else svc, v))
    return out


def visibility(ctx, ids, sql_text=None):
    """{id: (verdict, reason)} for scoped ids; check-sql semantics when the SQL exists."""
    p, pv, u = ctx.persona(), ctx.pv(), ctx.universe()
    res = {}
    if sql_text:
        r = pv.check_sql(u, p, sql_text, set(i for _, i in ids), True)
        for row in r["rows"]:
            for k in row.get("keys", []):
                if k in {i for _, i in ids}:
                    res[k] = (row["verdict"], f"SQL L{row['line']} {row['table']}: {row['reason']}")
        for x in r["load_bearing_base_ids"]:
            res.setdefault(x["id"], (x["verdict"], x["reason"]))
    for svc, i in ids:
        if i not in res:
            try:
                v = pv.can_see(u, p, svc, i)
                res[i] = (v["verdict"], v["reason"])
            except SystemExit as e:
                res[i] = ("UNVERIFIED", str(e))
    return res


def reach_check(ctx, doc, label, line_idx, sql_text=None, planned_ok=False):
    """line_idx: line indices whose scoped ids are load-bearing."""
    if ctx.persona() is None:
        ctx.add(f"reach.{label}", False, "persona not resolvable from 00_Assigments.md (persona_key / email)")
        return {}
    per_line, alt_line = {}, {}
    for i in sorted(set(line_idx)):
        if doc.toolfence[i]:
            continue
        head, _, tail = doc.lines[i].partition("alternate_evidence_ids")
        ids = scoped_ids(head)
        if ids:
            per_line[i] = ids
        if tail:
            alt_line[i] = (scoped_ids(tail), RX_ID.findall(tail))
    allids = sorted({x for v in per_line.values() for x in v} | {x for v in alt_line.values() for x in v[0]})
    if not allids:
        ctx.add(f"reach.{label}", True, f"no scoped load-bearing ids in {doc.rel} (unscoped services are always readable)",
                status="PASS")
        return {}
    vis = visibility(ctx, allids, sql_text)
    bad, planned, probes = [], 0, 0
    for i, ids in per_line.items():
        line = doc.lines[i]
        for svc, x in ids:
            v, why = vis.get(x, ("UNVERIFIED", "?"))
            if v == "YES":
                continue
            if planned_ok and "(U4" in why:
                planned += 1
                continue
            if (v == "NO" and "DENIAL-INTENDED:" in line) or (v == "UNVERIFIED" and "UNVERIFIED-OK:" in line):
                # a probe is never load-bearing: YES alternates carry the dependency (red team A, R1 #3)
                sc, other = alt_line.get(i, ([], []))
                not_yes = [f"{a}={vis.get(a, ('UNVERIFIED',))[0]}" for _, a in sc if vis.get(a, ("UNVERIFIED",))[0] != "YES"]
                if re.search(r"(?<![\w-])LB(?![\w-])", line):
                    bad.append((i, f"{svc} {x}: {v} on a row marked LB — a denied/unverified probe is never load-bearing"))
                elif not (sc or other):
                    bad.append((i, f"{svc} {x}: {v} accepted only with alternate_evidence_ids: <ids> that are YES"))
                elif not_yes:
                    bad.append((i, f"{svc} {x}: {v}; alternate evidence not YES: {', '.join(not_yes[:3])}"))
                else:
                    probes += 1
                continue
            bad.append((i, f"{svc} {x}: {v} — {why[:110]}"))
    n = len(allids)
    ctx.add(f"reach.{label}", not bad,
            (f"{len(bad)} load-bearing record(s) not visible to {ctx.persona()['persona_key']}: "
             + "; ".join(f"L{i + 1} {w}" for i, w in bad[:5])) if bad
            else f"{n - probes} scoped load-bearing ids YES for {ctx.persona()['persona_key']}"
            + (f"; {probes} denied/unverified probe(s), not load-bearing, each with YES alternate_evidence_ids" if probes else "")
            + (f" ({planned} planned seeds not yet in base: verified at the injection gate)" if planned else ""),
            [doc.loc(i) for i, _ in bad])
    return vis


def pasted_cansee(ctx, doc, need_ids, sql_text=None, label="pasted_can_see"):
    """Pasted `persona_view.py can-see` lines: each re-verified; each id in need_ids must have one."""
    p = ctx.persona()
    if p is None:
        ctx.add(f"tool.{label}", False, "persona not resolvable")
        return
    lines = []   # (line, persona_key or None, service, id, pasted verdict)
    for i, l in enumerate(doc.lines):
        m = RX_CANSEE.match(l)
        if m:
            lines.append((i, m.group(1), m.group(2), m.group(3), m.group(4)))
            continue
        m = RX_CHECKSQL_ROW.match(l)   # a pasted check-sql row proves seeded (and base) ids
        if m:
            for svc, x in scoped_ids(m.group(2)):
                lines.append((i, None, svc, x, m.group(1)))
    pairs = sorted({(svc, x) for _, _, svc, x, _ in lines})
    vis = visibility(ctx, pairs, sql_text) if pairs else {}
    wrong = [(i, f"{x} pasted {v}, re-run {vis.get(x, ('?',))[0]}") for i, who, svc, x, v in lines
             if (who is not None and who != p["persona_key"]) or vis.get(x, ("?",))[0] != v]
    have = {x for _, _, _, x, v in lines if v == "YES"}
    missing = [x for x in sorted(need_ids) if x not in have]
    ok = not wrong and not missing
    ctx.add(f"tool.{label}", ok,
            (f"{len(lines)} pasted can-see line(s); " + (f"{len(wrong)} differ from the re-run or name another persona "
                                                         f"(e.g. {wrong[0][1]}); " if wrong else "")
             + (f"{len(missing)} scoped id(s) without a pasted YES line (e.g. {missing[0]})" if missing else ""))
            if not ok else f"{len(lines)} pasted can-see lines match the re-run; every required id has a YES line",
            [doc.loc(i) for i, _ in wrong])

# ------------------------------------------------------------------ KB checks

KB_STATUSES = ("bound", "reference-only", "unavailable")
# Universe-KB catalog ids are leads, never records: integrations INT-nn, trap_catalog [PNDCBXK]nn,
# coherence_hazards [TSRQLI]nn, cohorts <LIN|SL|GH|GC|GM|SF|TR|DOC>-*.
KB_CATALOG_ID = re.compile(r"\b(?:INT-\d{2}|[TSRQLI]\d{2}|[PNDCBXK]\d{2}|"
                           r"(?:LIN|SL|GH|GC|GM|SF|TR|DOC)-[\w.@-]+)\b")


def record_locator(text):
    """First locator in text that addresses a real exported record (RX_ID), never a universe-KB catalog id."""
    for m in RX_ID.finditer(text):
        tok = m.group(0).rstrip(".,;:)")
        if not KB_CATALOG_ID.fullmatch(tok):
            return tok
    return None


def source_status(ctx):
    """(source.kb_status, universe key) from the loaded context; legacy V2 fixtures behave as 'bound'."""
    ctxd = ctx.context or {}
    src = ctxd.get("source") or {}
    uni = ctxd.get("universe") or {}
    status = src.get("kb_status")
    if status not in KB_STATUSES:
        status = "bound"
    return status, uni.get("key") or src.get("universe") or "universe"


def kb_gate(ctx, cid, fn, *args):
    """One KB-membership check under the context's source.kb_status.

    bound: unchanged (a FAIL blocks). reference-only: KB ids are leads, never membership authority, so a FAIL
    becomes a WARN naming the universe. unavailable: the KB cannot answer at all, so the check is skipped with a
    WARN and evidence.kb_locators requires record locators instead."""
    status, key = source_status(ctx)
    if status == "unavailable":
        ctx.add(cid, False, f"KB unavailable for {key}: KB membership not checked — cite record locators", block=False)
        return
    before = len(ctx.res)
    fn(ctx, *args)
    if status == "reference-only":
        for r in ctx.res[before:]:
            if r["status"] == "FAIL":
                r["status"], r["blocking"] = "WARN", False
                r["detail"] = f"KB reference-only for {key}: cite record locators — {r['detail']}"


def kb_locators(ctx, doc, spec):
    """When the KB is not bound, every KB-dependent section must still point at real records (blocking)."""
    status, key = source_status(ctx)
    if status == "bound":
        return
    head = f"KB {'unavailable' if status == 'unavailable' else 'reference-only'} for {key}"
    probs, locs = [], []
    for name, rx in spec:
        secs = doc.sections(rx)
        if not secs:
            continue                            # sections_present already blocks a missing section
        items = [x for s in secs for x in s.items()]
        txt = "\n".join(s.text(tools=False) for s in secs)
        hits = [(i, t) for i, t in items if record_locator(t) or RX_EMAIL.search(t)]
        cited = bool(hits) or (not items and bool(record_locator(txt) or RX_EMAIL.search(txt)))
        if cited or re.search(r"no records? in scope", txt, re.I):
            continue
        if items:
            probs.append(f"{name}: no record locator in {len(items)} item(s)")
            locs.append(doc.loc(items[0][0]))
        else:
            probs.append(f"{name}: no record locator anywhere")
            locs.append(doc.loc(secs[0].start))
    ctx.add("evidence.kb_locators", not probs,
            (f"{head}: every KB-dependent section cites record locators" if not probs else
             f"{head}; record locators missing — " + "; ".join(probs[:4])), locs)


def kb_hazards(ctx, doc, rx):
    secs = doc.sections(rx)
    txt = "\n".join(s.text(tools=False) for s in secs)
    haz = {x["id"]: x["category"] for x in kb("coherence_hazards.json")["index"]}
    cited = set(re.findall(r"\b([TSRQLI]\d{2})\b", txt))
    # trap-register ids (T1..T28) share the T prefix: only a line that says "hazard" claims a hazard id
    unknown = sorted({c for l in txt.splitlines() if re.search(r"hazard", l, re.I)
                      for c in re.findall(r"\b([TSRQLI]\d{2})\b", l) if c not in haz})
    missing = []
    for pre, words in HAZ_CATS.items():
        if any(c.startswith(pre) for c in cited if c in haz):
            continue
        if re.search(rf"(?:{words})[^\n|]{{0,40}}(?:none in scope|no hazard in scope)", txt, re.I):
            continue
        missing.append(words.split("|")[0])
    mentions = "coherence_hazards" in txt
    ok = bool(secs) and mentions and not unknown and not missing
    ctx.add("kb.coherence_hazards", ok,
            ("no coherence audit section" if not secs else
             ("coherence audit never cites coherence_hazards.json; " if not mentions else "")
             + (f"unknown hazard ids {unknown} (not in coherence_hazards.json); " if unknown else "")
             + (f"no hazard id or explicit 'none in scope' for: {', '.join(missing)}" if missing else ""))
            if not ok else f"coherence audit cites {len(cited)} valid hazard ids covering all 6 hazard categories",
            [doc.loc(secs[0].start)] if secs and not ok else [])


def _people():
    a = kb("activity.json")["people"]
    by = {}
    for email, v in a.items():
        keys = {email.lower(), (v.get("name") or "").lower(), (v.get("slack_id") or "").lower()}
        for k in keys:
            if k:
                by[k] = (email, v)
    return a, by


def kb_activity_rows(ctx, doc, rx):
    """scenario: the active-speaker table names people with their true status_at_clock."""
    secs = doc.sections(rx)
    a, by = _people()
    rows = [(i, " | ".join(c)) for s in secs for (i, c, _) in s.rows()]
    txt = "\n".join(s.text(tools=False) for s in secs)
    bad, seen = [], 0
    for i, r in rows:
        hit = next((by[k] for k in (m.lower() for m in RX_EMAIL.findall(r)) if k in by), None)
        if hit is None:
            hit = next((by[n.lower()] for n in re.findall(r"[A-Z][a-z]+ [A-Z][a-z]+", r) if n.lower() in by), None)
        if hit is None:
            continue
        seen += 1
        if hit[1]["status_at_clock"] not in r:
            bad.append((i, f"{hit[0]} status is {hit[1]['status_at_clock']}"))
    ok = bool(secs) and "activity" in txt and seen > 0 and not bad
    ctx.add("kb.activity", ok,
            ("no active-speaker section" if not secs else "active-speaker section never cites activity.json"
             if "activity" not in txt else "no person row resolves in activity.json" if not seen
             else f"{len(bad)} row(s) misstate status_at_clock: " + "; ".join(w for _, w in bad[:4]))
            if not ok else f"{seen} speaker rows carry their activity.json status_at_clock",
            [doc.loc(i) for i, _ in bad])


def seeded_speakers(sql_text):
    sys.path.insert(0, str(HERE))
    try:
        from base_check import parse_sql  # noqa: E402
    except Exception:  # noqa: BLE001 - another agent may be mid-edit; report, do not crash
        return None
    ent = kb("entities.json")
    idmap = {}
    for e in ent.get("entities", []):
        emails = e.get("emails") or []
        if not emails:
            continue
        for svc, lst in (e.get("identities") or {}).items():
            for x in lst:
                for k in ("id", "login", "username", "account_id"):
                    if x.get(k):
                        idmap[str(x[k])] = emails[0]
    out = {}
    for s in parse_sql(sql_text):
        if s.get("op") != "insert":
            continue
        r, t = s.get("row") or {}, s["table"]
        who = (r.get("user_id") if t == "slack.slack_messages" else r.get("from_email") if t == "gmail.gmail_messages"
               else r.get("author_id") if t in ("linear.linear_comments", "confluence.confluence_page_versions")
               else r.get("author_login") if t.startswith("github.") else r.get("idMemberCreator") if t == "trello.trello_actions"
               else None)
        if not who:
            continue
        email = who if "@" in str(who) else idmap.get(str(who))
        out.setdefault(email or f"?{who}", set()).add(s["line"])
    return out


def kb_activity_seeded(ctx, doc, rx, sql_text):
    sp = seeded_speakers(sql_text)
    if sp is None:
        ctx.add("kb.activity", False, "could not parse the SQL with base_check.parse_sql to list seeded speakers")
        return
    a, by = _people()
    secs = doc.sections(rx)
    lines = [doc.lines[i] for s in secs for i in s.idx()]
    need = {e: v for e, v in sp.items() if e in a}
    bad = []
    for email, sqllines in sorted(need.items()):
        v = a[email]
        keys = [email, v.get("name") or "~", v.get("slack_id") or "~"]
        ok = any(any(k in l for k in keys) and "activity" in l and v["status_at_clock"] in l for l in lines)
        if not ok:
            bad.append(f"{email} ({v['status_at_clock']}, SQL L{min(sqllines)})")
    conv = any("conventions" in l for l in lines)
    ok = bool(secs) and not bad and conv
    ctx.add("kb.activity", ok,
            ("no voice/realism section" if not secs else
             (f"{len(bad)} seeded speaker(s) without an activity.json line (name/email + 'activity' + status_at_clock): "
              + ", ".join(bad[:5]) + "; " if bad else "") + ("" if conv else "voice section never cites conventions.json"))
            if not ok else f"{len(need)} seeded speakers each cited with activity.json status; conventions.json cited",
            [doc.loc(secs[0].start)] if secs and not ok else [])


def kb_integrations(ctx, doc, rx, services):
    ints = kb("integrations.json")["integrations"]
    valid = {x["id"] for x in ints}
    secs = doc.sections(rx)
    txt = "\n".join(s.text(tools=False) for s in secs)
    cited = set(re.findall(r"\bINT-\d{2}\b", txt))
    unknown = sorted(cited - valid)
    missing = []
    for svc in sorted(services):
        srcs = [x["id"] for x in ints if INT_SOURCE_SCHEMA.get(x["source"].split("+")[0]) == svc]
        if not srcs:
            continue
        if cited & set(srcs):
            continue
        if re.search(rf"\b{svc}\b[^\n]{{0,80}}(?:no companion|none|n/a)", txt, re.I):
            continue
        missing.append(f"{svc} ({'/'.join(srcs)})")
    ok = bool(secs) and not unknown and not missing
    ctx.add("kb.integrations", ok,
            ("no integrations/companions section" if not secs else
             (f"unknown INT ids {unknown}; " if unknown else "")
             + (f"seeded services with integrations but no INT id or 'none': {', '.join(missing)}" if missing else ""))
            if not ok else f"companions listed per integrations.json ({len(cited)} INT ids, services {sorted(services)})",
            [doc.loc(secs[0].start)] if secs and not ok else [])


def kb_storyline(ctx, doc):
    txt = "\n".join(doc.lines[i] for i in range(len(doc.lines)) if not doc.toolfence[i])
    cohorts = {x["id"] for x in kb("cohorts.json")["index"]}
    traps = {x["id"] for x in kb("trap_catalog.json")["index"]}
    cited_c = {c.rstrip(".,;:)") for c in re.findall(r"\b(?:LIN|SL|GH|GC|GM|SF|TR|DOC)-[\w.@-]+", txt)}
    good_c = cited_c & cohorts
    cited_t = set(re.findall(r"\b([PNDCBXK]\d{2})\b", txt))
    good_t = cited_t & traps
    probs = []
    if "timeline" not in txt:
        probs.append("never cites universe_kb timeline")
    if not good_c and not re.search(r"cohorts\.json[^\n]{0,40}(?:no fit|none fits|not used)", txt, re.I):
        probs.append("no valid cohorts.json id (or 'cohorts.json: no fit — reason')")
    if "trap_catalog" not in txt or not good_t:
        probs.append("no valid trap_catalog.json id cited")
    ctx.add("kb.storyline", not probs, "; ".join(probs) if probs
            else f"timeline cited; cohorts {sorted(good_c)[:4]}; trap_catalog {sorted(good_t)[:6]}")


def kb_entity(ctx, doc, rx):
    secs = doc.sections(rx)
    txt = "\n".join(s.text(tools=True) for s in secs)
    ok = bool(secs) and bool(re.search(r"SHARED_FIRST_NAMES|^\s*ENTITY ", txt, re.M))
    ctx.add("tool.entity", ok, "entity.py collisions/resolve output pasted in the identity-trap section" if ok
            else ("no identity-trap section" if not secs else "identity-trap section has no pasted entity.py output"
                  " (SHARED_FIRST_NAMES … or ENTITY …)"), [doc.loc(secs[0].start)] if secs and not ok else [])

# ------------------------------------------------------------------ chain / handoff


def gate_blocks(doc, stage):
    out = []
    for i, l in enumerate(doc.lines):
        m = RX_GATE_HEAD.search(l)
        if m and m.group(1) == stage:
            out.append((i, m.group(2), dict(re.findall(r"([\w./-]+)#([0-9a-f]{12})", m.group(3)))))
    return out


def chain(ctx, stage, file):
    doc = ctx.doc(file)
    if not doc.exists:
        ctx.add(f"chain.{stage}", False, f"upstream artifact {file} missing")
        return
    blocks = [b for b in gate_blocks(doc, stage) if b[1] == "PASS"]
    if not blocks:
        ctx.add(f"chain.{stage}", False, f"{file} carries no pasted 'STAGE GATE {stage}: PASS' block — "
                f"run tools/stage_gate.py {stage} and paste it into its Self-review")
        return
    i, _, digs = blocks[-1]
    stale = certificate_staleness(ctx, stage, digs)
    ctx.add(f"chain.{stage}", not stale and bool(digs),
            (f"upstream '{stage}' PASS is stale: " + "; ".join(stale)) if stale else
            (f"upstream '{stage}' PASS block has no digests" if not digs else
             f"upstream '{stage}' PASS pasted and current ({', '.join(f'{k}#{v}' for k, v in digs.items())})"),
            [doc.loc(i)])

# ------------------------------------------------------------------ re-run comparisons


def rerun_sql_lint(ctx, doc, sql):
    m_err = re.search(r"errors: (\d+)\s+warnings: (\d+)", doc.text)
    m_rows = re.search(r"total rows: (\d+)", doc.text)
    if not m_err:
        ctx.add("tool.sql_lint", False, f"sql_lint summary ('errors: N  warnings: M') not pasted in {doc.rel}")
        return None
    rc, out, err = run_tool([HERE / "sql_lint.py", ctx.p(sql), "--json"])
    try:
        r = json.loads(out)
    except ValueError:
        ctx.add("tool.sql_lint", False, f"sql_lint re-run failed: {err.strip()[:200]}")
        return None
    e, w, rows = len(r["errors"]), len(r["warnings"]), r["stats"]["total_rows"]
    pe, pw = int(m_err.group(1)), int(m_err.group(2))
    probs = []
    if e:
        probs.append(f"re-run has {e} error(s)")
    if (pe, pw) != (e, w):
        probs.append(f"pasted errors/warnings {pe}/{pw} ≠ re-run {e}/{w} (stale paste)")
    if m_rows and int(m_rows.group(1)) != rows:
        probs.append(f"pasted total rows {m_rows.group(1)} ≠ re-run {rows}")
    ctx.add("tool.sql_lint", not probs, "; ".join(probs) if probs else f"sql_lint re-run matches the paste: errors 0, "
            f"warnings {w}, rows {rows}")
    return r


def rerun_json_tool(ctx, cid, args, pasted_rx, doc, label):
    m = re.search(pasted_rx, doc.text, re.M)
    if not m:
        ctx.add(cid, False, f"{label} output not pasted verbatim in {doc.rel}")
        return
    if m.group(1) != "PASS":
        ctx.add(cid, False, f"pasted {label} verdict is {m.group(1)}")
        return
    if ctx.rerun != "all":
        ctx.skip(cid + "_rerun", f"{label} pasted PASS; re-run skipped (--rerun {ctx.rerun})")
        return
    rc, out, err = run_tool(args)
    try:
        v = json.loads(out)["verdict"]
    except (ValueError, KeyError):
        ctx.add(cid, False, f"{label} re-run failed: {(err or out).strip()[:200]}")
        return
    ctx.add(cid, v == "PASS", f"{label} pasted PASS; re-run {v}" + ("" if v == "PASS" else " — the paste is stale or false"))

def _json_stdout(out):
    """The tool's JSON payload, tolerating a leading line (hg.py writes caches to stderr, but stay tolerant)."""
    try:
        return json.loads(out)
    except (TypeError, ValueError):
        pass
    a, b = out.find("{"), out.rfind("}")
    if a >= 0 and b > a:
        try:
            return json.loads(out[a:b + 1])
        except ValueError:
            return None
    return None


LINT_DISPOSITION = re.compile(r"^\s*(?:[-*+]|\d+[.)])?\s*LINT\s+(\S+)\s+L(\d+)\s*:\s*(\S.*?)\s*$", re.M)


def _lint_flag(f):
    return f"{f.get('check') or '?'} L{f.get('line') if f.get('line') is not None else '?'} " \
           f"{f.get('table') or '?'}.{f.get('column') or '?'}"


def _flag_line(f):
    try:
        return int(f.get("line"))
    except (TypeError, ValueError):
        return -1


def _undispositioned_checks(doc, checks):
    """CHECK flags with no `LINT <check> L<line>: <disposition>` line in the Self-review.

    Every CHECK flag object needs its own line, keyed by that flag's own line; two flags of the same check on
    different lines need two lines. The only grouping is upstream: records folded into a flag's `also` field are
    covered by the parent flag's disposition (they are payload of that flag, not flags of their own)."""
    if not checks:
        return []
    secs = doc.sections(r"self[- ]review")
    txt = secs[-1].text(tools=True) if secs else ""
    # Count dispositions per (check, line): two distinct flags on one SQL line need two lines. Only byte-identical
    # duplicate reports collapse to one flag.
    disp = Counter((m.group(1), int(m.group(2))) for m in LINT_DISPOSITION.finditer(txt))
    out, seen = [], set()
    for f in checks:
        ident = json.dumps(f, sort_keys=True, default=str)   # the whole report, 'also' included
        if ident in seen:
            continue
        seen.add(ident)
        key = (str(f.get("check") or "?"), _flag_line(f))
        if disp[key] > 0:
            disp[key] -= 1
        else:
            out.append(f)
    return out


def injection_lint(ctx, doc, sql):
    """hg.py lint - the eval's static injection linter - on the current SQL.

    The eval linter exits 0 even with FAIL flags, so the gate reads counts/flags itself: an error payload, any
    FAIL, a sha256 that is not the current SQL (stale output) or a CHECK flag without a Self-review disposition
    line blocks. INFO flags are reported, never gated."""
    if not ctx.v3:
        ctx.skip("tool.injection_lint", "legacy (pre-V3) task: hg.py lint needs the selected universe")
        return None
    sql_path = ctx.p(sql)
    rc, out, err = run_tool([HERE / "hg.py", "lint", "--task-dir", ctx.td])
    r = _json_stdout(out)
    if rc != 0:                            # 2 = error payload, 1 = tokenizer error; any non-zero exit blocks
        msg = (r.get("error") if isinstance(r, dict) else None) or \
              ((err or out).strip().splitlines() or [""])[-1]
        ctx.add("tool.injection_lint", False,
                f"hg.py lint exited {rc}" + (f": {str(msg)[:200]}" if msg else ""))
        return None
    if not isinstance(r, dict):
        tail = (err or out).strip().splitlines()
        ctx.add("tool.injection_lint", False,
                f"hg.py lint printed no JSON (exit {rc}): {tail[-1][:200] if tail else 'no output'}")
        return None
    if r.get("error"):
        q = r.get("question")
        ctx.add("tool.injection_lint", False, f"hg.py lint error: {r['error']}" + (f" — {q}" if q else ""))
        return None
    flags = [f for f in r.get("flags") or [] if isinstance(f, dict)]
    counts = r.get("counts") or {}
    fails = [f for f in flags if str(f.get("severity") or "").upper() == "FAIL"]
    checks = [f for f in flags if str(f.get("severity") or "").upper() == "CHECK"]
    try:
        n_fail = int(counts.get("FAIL") or 0)
    except (TypeError, ValueError):
        n_fail = 0
    try:
        n_check = int(counts.get("CHECK") or 0)
    except (TypeError, ValueError):
        n_check = 0
    try:
        n_info = int(counts.get("INFO") or 0)
    except (TypeError, ValueError):
        n_info = 0
    n_fail, n_check, n_info = n_fail or len(fails), n_check or len(checks), n_info or len(r.get("info") or [])
    probs = []
    if n_fail:
        probs.append(f"{n_fail} FAIL flag(s): " + "; ".join(_lint_flag(f) for f in (fails or flags)[:3]))
    digest = hashlib.sha256(sql_path.read_bytes()).hexdigest() if sql_path.exists() else ""
    got = str(r.get("sha256") or "").strip().lower()
    if not digest:
        probs.append(f"{sql} is missing, so the lint output cannot be bound to it")
    elif got != digest:
        probs.append(f"lint sha256 {got[:12] or '?'} does not match the full sha256 of the current {sql} "
                     f"({digest[:12]}): the lint output is stale")
    undisp = _undispositioned_checks(doc, checks)
    if undisp:
        probs.append(f"{len(undisp)} CHECK flag(s) without a 'LINT <check> L<line>:' line in the Self-review: "
                     + ", ".join(f"{f.get('check') or '?'} L{f.get('line')}" for f in undisp[:4]))
    elif len(checks) < n_check:
        probs.append(f"counts report {n_check} CHECK flag(s) but the payload carries {len(checks)}")
    ctx.add("tool.injection_lint", not probs,
            "; ".join(probs) if probs else
            f"hg.py lint: 0 FAIL, {n_check} CHECK dispositioned, {n_info} INFO; sha256 {digest[:12]} matches {sql}")
    return r


# ------------------------------------------------------------------ stage helpers


def table_in(doc, rx):
    out = []
    for s in doc.sections(rx):
        out += s.tables()
    return out


def rows_in(doc, rx):
    return [(i, c, t) for s in doc.sections(rx) for (i, c, t) in s.rows()]


def substr_check(ctx, cid, doc, rows, colrx, source_text, source_name, require_quote=False):
    bad, n = [], 0
    for i, cells, t in rows:
        c = t.col(colrx)
        if c is None:
            continue
        cell = t.cell(cells, c)
        if not cell or cell.lower() in ("—", "-", "n/a", "implicit"):
            continue
        frags = quoted_spans(cell)
        if require_quote and not re.search(r"[\"“`]", cell):
            continue
        for f in frags:
            n += 1
            if f not in source_text:
                bad.append((i, f[:60]))
    ctx.add(cid, not bad, (f"{len(bad)} quoted span(s) are not exact substrings of {source_name}: "
                           + "; ".join(f"L{i + 1} {f!r}" for i, f in bad[:4])) if bad
            else f"{n} quoted span(s) verified as exact substrings of {source_name}", [doc.loc(i) for i, _ in bad])


def lb_lines(doc, section_rxs):
    idx = set()
    for rx in section_rxs:
        for s in doc.sections(rx):
            idx.update(s.idx())
    for i, l in enumerate(doc.lines):
        if re.search(r"(?<![\w-])LB(?![\w-])|load-bearing", l) and not doc.toolfence[i]:
            idx.add(i)
    return idx


def own_paste(ctx, primary, outputs):
    doc = ctx.doc(primary)
    blocks = gate_blocks(doc, ctx.stage)
    if not blocks:
        ctx.add("handoff.pasted", False, f"paste this gate's PASS output into {primary}'s Self-review (or use --paste); "
                "the next stage blocks without it", block=False)
        return
    i, verdict, digs = blocks[-1]
    stale = certificate_staleness(ctx, ctx.stage, digs)
    ctx.add("handoff.pasted", verdict == "PASS" and not stale,
            f"pasted block at {primary}:L{i + 1} is {verdict}" + (f", stale for {stale}" if stale else ", current"),
            block=False)

# ------------------------------------------------------------------ prompt / OE / rubric / release checks
# (harness red team B, 2026-10-04: support/examples/calibration/harness_redteam/B_prompt_oe_rubric*.md)


ANCHOR_VERB = re.compile(
    r"^(?:please\s+|pls\s+|can\s+you\s+|could\s+you\s+)?(?:pull|put|find|draft|send|go|figure|make|get|check|write|create|"
    r"compile|review|prepare|look|dig|sort|build|post|email|reach|update|fix|list|give|tell|let|grab|ping|share|chase|"
    r"confirm|loop|use|follow|read|open|search|see|ask|run|collect|gather|verify|handle|work|do|finish|complete|start|"
    r"track|file|flag|move|close|add|remove|drop|note|reply|forward|schedule|book|set|keep|ensure|pin|attach|upload|"
    r"cross-check|reconcile|identify|determine|summari[sz]e|report)\b", re.I)
SECOND_PERSON = re.compile(r"(?<![\w'’-])(?:you|your|yours|you're|you’re|please|pls)(?![\w'’-])", re.I)


def load_manifest(ctx, name="01_Hardness_Manifest.json"):
    try:
        return json.loads(ctx.p(name).read_text())
    except (OSError, ValueError):
        return None


def anchor_naming(ctx, doc, manifest_name=None, required=False):
    """Anchors are named by noun phrases only (red team A, R2 #3): no imperative verb at the start, no second-person
    request, at most 6 words. Entries: table columns 'anchor name' / 'may be named' / 'noun phrase', 'Anchor An name:'
    lines, and the manifest's anchors[].prompt_reference."""
    entries = []
    for tb in doc.whole().tables():
        c = tb.col(r"anchor name|may be named|noun phrase")
        if c is None:
            continue
        for i, cells in tb.rows:
            entries.append((doc.rel, i, tb.cell(cells, c)))
    for i, l in enumerate(doc.lines):
        if doc.toolfence[i]:
            continue
        m = re.match(r"^\s*(?:[-*]\s*)?(?:\*\*)?Anchor\s+A\d+(?:\*\*)?\s+(?:name[sd]?|may be named)\s*[:—–-]\s*(.+)$", l, re.I)
        if m:
            entries.append((doc.rel, i, m.group(1)))
    man = load_manifest(ctx, manifest_name) if manifest_name else None
    for a in (man or {}).get("anchors", []) or []:
        entries.append((manifest_name, None, str(a.get("prompt_reference") or "")))
    hits = []
    for where, i, cell in entries:
        for ph in re.split(r"\s*;\s*|\s+/\s+|\s*\|\s*", cell):
            ph = ph.strip().strip("`\"“”'*_ .").strip()
            if not ph or ph in ("—", "-"):
                continue
            n = len(ph.split())
            why = ("imperative verb at the start" if ANCHOR_VERB.match(ph) else
                   "second-person request" if SECOND_PERSON.search(ph) else
                   f"{n} words (> 6)" if n > 6 else None)
            if why:
                hits.append((where, i, f"{ph[:60]!r}: {why}"))
    if required and not entries:
        ctx.add("boundary.anchor_naming", False, f"no anchor-naming entry found ({doc.rel} anchor-name column / manifest "
                f"anchors[].prompt_reference) — name each anchor by a noun phrase")
        return
    ctx.add("boundary.anchor_naming", not hits,
            (f"{len(hits)} anchor-naming entr{'y' if len(hits) == 1 else 'ies'} not a noun phrase of ≤ 6 words: "
             + "; ".join(f"{w}{'' if i is None else ':L' + str(i + 1)} {x}" for w, i, x in hits[:5])) if hits
            else f"{len(entries)} anchor-naming entr{'y' if len(entries) == 1 else 'ies'}, each a noun phrase of ≤ 6 words",
            [doc.loc(i) if w == doc.rel else w for w, i, _ in hits])


def design_ids(m: dict) -> set:
    out = set()
    reqs = m.get("requirements") or {}
    out |= {("requirements", str(k)) for k in (reqs if isinstance(reqs, dict) else
                                                [r.get("id") if isinstance(r, dict) else r for r in reqs])}
    for sec in ("anchors", "ask_fragments", "authorities", "chains", "traps", "denied_probes"):
        for it in m.get(sec, []) or []:
            if isinstance(it, dict) and (it.get("id") or it.get("record")):
                out.add((sec, str(it.get("id") or it.get("record"))))
    return out


def design_delta(ctx):
    """injection: the final manifest keeps every draft id, or records each change in design_delta [{id, change, reason}]."""
    draft, final = load_manifest(ctx, "01_Hardness_Manifest.draft.json"), load_manifest(ctx)
    if draft is None or final is None:
        ctx.add("structure.design_delta", False, "01_Hardness_Manifest.draft.json or 01_Hardness_Manifest.json missing or not JSON")
        return
    missing = sorted(design_ids(draft) - design_ids(final))
    delta = {str(d.get("id")) for d in final.get("design_delta", []) or [] if isinstance(d, dict) and str(d.get("reason") or "").strip()}
    unexplained = [f"{s}:{i}" for s, i in missing if i not in delta]
    ctx.add("structure.design_delta", not unexplained,
            (f"draft ids missing from the final manifest without a design_delta entry {{id, change, reason}}: {unexplained[:8]}"
             if unexplained else f"final manifest keeps all {len(design_ids(draft))} draft ids"
             + (f" ({len(missing)} changed, each in design_delta)" if missing else "")))


def manifest_profile(ctx, name="01_Hardness_Manifest.json"):
    m = load_manifest(ctx, name) or {}
    return m.get("effective_profile") if m.get("effective_profile") in ("extreme", "normal") else "extreme"


def tier_profile(ctx):
    if ctx.context:
        h = ctx.context["horizon"]
    else:
        m = re.search(r"^\s*horizon:\s*(.+?)\s*$", ctx.doc("00_Assigments.md").text, re.M | re.I)
        if not m:
            return None, None
        h = m.group(1)
    return h, ("paused" if re.search(r"super", h, re.I) else "extreme" if re.search(r"long", h, re.I)
               else "normal" if re.search(r"normal", h, re.I) else None)


def tier_hardness(ctx):
    """prompt-check: the tier's breadth/hardness is certified — manifest present, hardness_gate PASS for the tier's
    profile pasted in the dossier, and that paste still current (the dossier's injection PASS block matches)."""
    horizon, prof = tier_profile(ctx)
    probs = []
    if prof is None:
        probs.append("00_Assigments.md has no 'horizon:' line naming Long or Normal Horizon")
    elif prof == "paused":
        probs.append(f"horizon '{horizon}' is paused (Super-Long Horizon)")
    man = ctx.p("01_Hardness_Manifest.json")
    if not man.exists():
        probs.append("01_Hardness_Manifest.json missing — the tier's breadth and hardness are not certified")
    else:
        try:
            mj = json.loads(man.read_text())
        except ValueError:
            mj = {}
        mp = mj.get("effective_profile")
        ex = mj.get("profile_exception") or {}
        if mp not in ("extreme", "normal"):
            probs.append(f"manifest effective_profile {mp!r} missing or invalid")
        elif prof == "extreme" and mp != "extreme":
            probs.append(f"manifest effective_profile '{mp}' on a {horizon} task (needs extreme)")
        elif prof == "normal" and mp == "extreme" and not (isinstance(ex, dict) and ex.get("requester_confirmation")):
            probs.append(f"manifest effective_profile 'extreme' on a {horizon} task without profile_exception.requester_confirmation")
        if mj.get("horizon") and horizon and mj.get("horizon").lower() != horizon.lower():
            probs.append(f"manifest horizon '{mj.get('horizon')}' ≠ the assignment's '{horizon}'")
        if mp in ("extreme", "normal"):
            prof = mp if prof in ("extreme", "normal") else prof
    dos = ctx.doc("01_Grounding_Dossier.md")
    paste = re.findall(r"HARDNESS GATE \((extreme|normal)\): (PASS|FAIL)", dos.text)
    if not dos.exists:
        probs.append("01_Grounding_Dossier.md missing")
    elif not paste:
        probs.append("no 'HARDNESS GATE (<profile>): PASS' pasted in 01_Grounding_Dossier.md")
    else:
        pp, pverdict = paste[-1]
        if pverdict != "PASS":
            probs.append(f"pasted hardness_gate ({pp}) is {pverdict}")
        if prof in ("extreme", "normal") and pp != prof:
            probs.append(f"the dossier pastes hardness_gate --profile {pp}; a {horizon} task needs --profile {prof}")
        blocks = [b for b in gate_blocks(dos, "injection") if b[1] == "PASS"]
        if not blocks:
            probs.append("the dossier carries no 'STAGE GATE injection: PASS' block, so its hardness paste is not certified")
        else:
            digs = blocks[-1][2]
            miss = [f for f in ("01_Hardness_Manifest.json", "01_Universe_Inject.sql") if f not in digs]
            stale = certificate_staleness(ctx, "injection", digs)
            if miss:
                probs.append(f"the injection PASS block records no digest for {miss}")
            if stale:
                probs.append(f"the injection PASS block is stale for {stale} (edited after the injection gate)")
    ctx.add("tier.hardness", not probs, "; ".join(probs) if probs else
            f"{horizon} → --profile {prof}: manifest present, hardness_gate PASS pasted in the dossier and current")
    if probs:
        return
    if ctx.rerun != "all":
        ctx.skip("tier.hardness_rerun", f"hardness_gate --profile {prof} re-run skipped (--rerun {ctx.rerun})")
        return
    rc, out, err = run_tool([HERE / "hardness_gate.py", man, ctx.p("01_Universe_Inject.sql"), "--profile", prof, "--json"])
    try:
        v = json.loads(out)["verdict"]
    except (ValueError, KeyError):
        v = f"re-run failed: {(err or out).strip()[:160]}"
    ctx.add("tier.hardness_rerun", v == "PASS", f"hardness_gate --profile {prof} re-run on the current manifest + SQL: {v}")


def canonical_outcome(ctx, doc):
    """prompt-writing: brief §4 carries the canonical outcome table (one acceptance class)."""
    if ctx.v3:
        # V3 explicitly allows several fair readings. The current, content-bound outcomes review
        # is checked separately; this V2 table must not force one acceptance class.
        ctx.add("structure.accepted_outcomes", True, "V3 accepts multiple fair outcomes; see v3.fair_outcomes_review")
        return
    tabs = [t for s in doc.sections(r"pinned final state|canonical outcome") for t in s.tables()
            if t.col(r"equivalence") is not None and t.col(r"material") is not None and t.col(r"delegat") is not None]
    rows = sorted({i: (i, c, t) for t in tabs for (i, c) in t.rows}.values(), key=lambda x: x[0])
    bad = [(i, c) for i, c, t in rows if not t.cell(c, t.col(r"fixed")).strip("—- ") and
           not t.cell(c, t.col(r"delegat")).strip("—- ")]
    ctx.add("structure.canonical_outcome", bool(rows) and not bad,
            ("§4 has no canonical outcome table (Field · Fixed value · Delegated by · Allowed equivalence class · "
             "Material / representational)" if not rows else
             f"{len(bad)} canonical-outcome field(s) neither fixed nor delegated")
            if not rows or bad else f"canonical outcome table: {len(rows)} field(s), each fixed or delegated",
            [doc.loc(i) for i, _ in bad])


def ledger_facts(doc):
    """fid -> row facts of ledger §B (order, locator, origin, expected, value, depends, service, text)."""
    facts = {}
    for order, (i, c, t) in enumerate(rows_in(doc, r"^B\b")):
        m = re.match(r"\s*(F\d+)", c[0] if c else "")
        if not m:
            continue
        li = next((k for k, h in enumerate(t.header) if re.fullmatch(r"\s*locator\s*", h, re.I)), t.col(r"locator"))
        facts[m.group(1)] = dict(order=order, line=i, table=t, locator=t.cell(c, li), origin=t.cell(c, t.col(r"origin")),
                                 expected=t.cell(c, t.col(r"expected")), value=t.cell(c, t.col(r"value")),
                                 depends=t.cell(c, t.col(r"depends")), service=t.cell(c, t.col(r"^\s*service")),
                                 text=" ".join(c), has_origin=t.col(r"origin") is not None)
    return facts


def _scoped_service(cell):
    if re.search(r"confluence|linear|github|trello|contacts|snowflake", cell, re.I):
        return None
    return next((s for s, rx in SERVICE_WORDS if re.search(rx, cell, re.I)), None)


def locator_provenance(ctx, doc, facts, prompt, sql_text):
    """oe-writing: every opaque id in a §B Locator comes from the prompt, from an earlier fact's Expected data
    (Depends on / Locator origin F-n), or from a natural search ('search "<query>"' origin, id-free query)."""
    if not facts:
        ctx.add("provenance.locators", False, "ledger §B has no F rows")
        return
    pl = prompt.casefold()
    bad, searches = [], []
    if not any(f["has_origin"] for f in facts.values()):
        bad.append((next(iter(facts.values()))["line"], "§B has no 'Locator origin' column (prompt · F-n · search \"<query>\")"))
    for fid, f in facts.items():
        deps = (set(RX_FID.findall(f["depends"])) | set(RX_FID.findall(f["origin"]))) - {fid}
        late = sorted(d for d in deps if d not in facts or facts[d]["order"] >= f["order"])
        if late:
            bad.append((f["line"], f"{fid} depends on {late}: not an earlier §B fact (dependencies must be topological)"))
        src = " ".join(facts[d]["expected"] + " " + facts[d]["value"] for d in deps if d in facts and d not in late).casefold()
        q = RX_SEARCH_ORIGIN.search(f["origin"]) or RX_SEARCH_ORIGIN.search(f["locator"])
        for x in dict.fromkeys(m.group(0) for m in OPAQUE.finditer(f["locator"])):
            if x.casefold() in pl or x.casefold() in src:
                continue
            if q and not OPAQUE.search(q.group(1)):
                searches.append((fid, x, q.group(1)))
                continue
            bad.append((f["line"], f"{fid} locator {x}: " + ("its search query carries an opaque id" if q else
                        "not in 04_Prompt.txt, not in a Depends-on fact's Expected data, no search \"<query>\" origin")))
    ctx.add("provenance.locators", not bad,
            (f"{len(bad)} locator(s) the agent cannot obtain from the prompt or an earlier tool result: "
             + "; ".join(w for _, w in bad[:4])) if bad else
            f"every opaque locator in {len(facts)} §B facts traces to the prompt, an upstream fact or a natural search "
            f"({len(searches)} search origin(s))", [doc.loc(i) for i, _ in bad])
    if not searches:
        return
    if ctx.rerun != "all":
        ctx.skip("provenance.search", f"{len(searches)} search origin(s) not re-run (--rerun {ctx.rerun})")
        return
    p, pv = ctx.persona(), ctx.pv()
    stmts = []
    if sql_text:
        sys.path.insert(0, str(HERE))
        from base_check import parse_sql  # noqa: E402
        stmts = [s.get("row") or {} for s in parse_sql(sql_text) if s.get("op") == "insert"]
    cache, bad2 = {}, []
    for fid, x, q in searches:
        f = facts[fid]
        svc = _scoped_service(f["service"])
        if svc is None:
            su = next((s for s in ("confluence", "linear", "github", "trello", "contacts", "snowflake")
                       if s in f["service"].lower()), None)
            if su is None:
                bad2.append((f["line"], f"{fid}: service '{f['service']}' not recognised"))
                continue
            if (su, q) not in cache:
                rc, out, err = run_tool([HERE / "hg.py", "search", "search", su, q, "--limit", "1"])
                try:
                    cache[(su, q)] = bool(json.loads(out).get("matches"))
                except ValueError:
                    cache[(su, q)] = False
            if not cache[(su, q)]:
                bad2.append((f["line"], f"{fid}: search \"{q}\" finds nothing in {su}"))
            continue
        if p is None:
            bad2.append((f["line"], "persona not resolvable"))
            continue
        if (svc, q) not in cache:
            try:
                cache[(svc, q)] = {str(h["id"]) for h in pv.search(ctx.universe(), p, svc, q, 10 ** 7, False)["visible"]}
            except SystemExit as e:
                cache[(svc, q)] = set()
                bad2.append((f["line"], f"{fid}: search failed: {e}"))
        ids = cache[(svc, q)]
        found = x in ids or any(i.startswith(x + "/") for i in ids)
        if not found and svc == "gmail":   # a message id: its thread must be among the hits
            tid = ctx.universe().gmail_message_thread(x)
            found = bool(tid and tid in ids)
        if not found:
            parts = x.split("/")
            found = any(all(pt in {str(v) for v in r.values()} for pt in parts) and
                        q.casefold() in " ".join(str(v) for v in r.values()).casefold() for r in stmts)
        if not found:
            bad2.append((f["line"], f"{fid}: search \"{q}\" as {p['persona_key']} does not reach {x}"))
    ctx.add("provenance.search", not bad2, ("; ".join(w for _, w in bad2[:4])) if bad2 else
            f"{len(searches)} search origin(s) reach their record as the persona", [doc.loc(i) for i, _ in bad2])


def scoped_fact_ids(ctx, doc, facts):
    """oe-writing: a §B fact on a scoped service names the record id the visibility check runs on."""
    bad = [(f["line"], fid) for fid, f in facts.items() if _scoped_service(f["service"]) and not scoped_ids(f["text"])
           and not re.search(r"DENIAL-INTENDED:|UNVERIFIED-OK:", f["text"])]
    ctx.add("reach.ledger_B_ids", not bad, (f"{len(bad)} scoped §B fact(s) without a record id, so visibility is never "
                                            f"checked: {', '.join(x for _, x in bad[:6])}") if bad else
            "every scoped §B fact carries a record id; all of them are re-checked with persona_view",
            [doc.loc(i) for i, _ in bad])


def defer_search(ctx, doc):
    """oe-writing: the act-vs-defer search covers the governing services, its population and versions."""
    C = rows_in(doc, r"^C\b|write capability")
    bad = []
    for i, c, t in C:
        cell = t.cell(c, t.col(r"defer"))
        if re.search(r"\bUNRESOLVED\b", cell):
            continue
        miss = []
        if not RX_ID.search(cell):
            miss.append("record pointer")
        if len(set(m.lower() for m in re.findall(r"slack|gmail|linear|confluence|gdocs|docs|drive|github|trello|gcal|"
                                                    r"calendar|sheets|snowflake", cell, re.I))) < 2:
            miss.append("≥ 2 governing services")
        if not re.search(r"\bcomplete\b", cell, re.I):
            miss.append("'complete' (population + pagination)")
        if not re.search(r"\bversion", cell, re.I):
            miss.append("version resolution")
        if miss:
            bad.append((i, f"L{i + 1} defer search lacks {', '.join(miss)}"))
    ctx.add("evidence.defer_search", not bad, ("; ".join(w for _, w in bad[:4]) + " — or mark it UNRESOLVED") if bad
            else f"{len(C)} write(s): defer search names services, a pointer, a complete population and the governing version",
            [doc.loc(i) for i, _ in bad])


def plan_reach(ctx, doc, cited, facts, sql_text):
    """rubric-writing: every scoped id behind every cited F-id is re-checked with persona_view (not only pasted ones)."""
    pairs = sorted({(svc, x) for f in cited if f in facts for svc, x in scoped_ids(facts[f]["text"])})
    if not pairs:
        ctx.add("reach.plan_fids", True, "no scoped record behind the plan's F-ids (unscoped services are readable)")
        return
    if ctx.persona() is None:
        ctx.add("reach.plan_fids", False, "persona not resolvable from 00_Assigments.md")
        return
    vis = visibility(ctx, pairs, sql_text)
    bad = []
    for f in sorted(cited):
        if f not in facts:
            continue
        txt = facts[f]["text"]
        for svc, x in scoped_ids(txt):
            v, why = vis.get(x, ("UNVERIFIED", "?"))
            if v == "YES" or (v == "NO" and "DENIAL-INTENDED:" in txt) or (v == "UNVERIFIED" and "UNVERIFIED-OK:" in txt):
                continue
            bad.append(f"{f} {svc} {x}: {v} — {why[:90]}")
    ctx.add("reach.plan_fids", not bad, (f"{len(bad)} record(s) behind cited F-ids not visible to "
                                         f"{ctx.persona()['persona_key']}: " + "; ".join(bad[:4])) if bad else
            f"{len(pairs)} scoped id(s) behind {len(cited)} cited F-ids YES for {ctx.persona()['persona_key']}")


def plan_allfail(ctx, doc, A2):
    """rubric-writing: predicted all-fail tolerance 0 (stricter than /rubric, which fails at ≥ 2)."""
    probs, locs = [], []
    for i, c, t in A2:
        cell = t.cell(c, t.col(r"all-fail"))
        if ALLFAIL_BASES.search(cell):
            probs.append(f"L{i + 1} {ALLFAIL_BASES.search(cell).group(0)}")
            locs.append(doc.loc(i))
    E = "\n".join(s.text(tools=False) for s in doc.sections(r"summary"))
    m = re.search(r"predicted all-fail rows\D{0,8}?(\d+)", E, re.I)
    if not m:
        probs.append("summary does not state 'predicted all-fail rows N'")
    elif int(m.group(1)):
        probs.append(f"summary counts {m.group(1)} predicted all-fail row(s)")
    ctx.add("validity.predicted_allfail", not probs, ("; ".join(probs) + " — tolerance is 0 (the harness is stricter than "
                                                      "/rubric, which fails at ≥ 2)") if probs else
            "0 predicted all-fail rows (tolerance 0)", locs)


def plan_diversity(ctx, doc, A, A2, facts):
    """rubric-writing gate 12: weight share per unit of discovery (one authority or one tool response), computed
    transitively over the ledger's Depends-on edges; prompt-origin facts are handed over, not discovered."""
    pa = {}
    for i, c, t in A:
        m = re.match(r"\s*(P\d+)", c[0] if c else "")
        if m:
            pa[m.group(1)] = set(RX_FID.findall(t.cell(c, t.col(r"values"))))

    def closure(fs):
        out, stack = set(), list(fs)
        while stack:
            f = stack.pop()
            if f in out:
                continue
            out.add(f)
            if f in facts:
                stack += RX_FID.findall(facts[f]["depends"]) + RX_FID.findall(facts[f]["origin"])
        return out

    def response(f):
        if f not in facts:
            return f
        ids = [m.group(0) for m in OPAQUE.finditer(facts[f]["locator"])]
        return ids[0] if ids else (facts[f]["locator"].strip().lower() or f)

    weight, units = {}, {}
    for i, c, t in A2:
        m = re.match(r"\s*(P\d+)", c[0] if c else "")
        band = t.cell(c, t.col(r"band")).strip()
        if not m or band not in ("1", "3", "5"):
            continue
        P = m.group(1)
        dec = t.cell(c, t.col(r"decided"))
        us = {f"authority {x}" for x in re.findall(r"\b[A-Z]{1,3}\d{1,3}\b", dec) if not re.fullmatch(r"[FP]\d+", x)}
        for f in closure(pa.get(P, set()) | set(RX_FID.findall(dec))):
            if f in facts and re.match(r"\s*prompt\b", facts[f]["origin"], re.I):
                continue
            us.add(f"response {response(f)}")
        weight[P], units[P] = int(band), us
    total = sum(weight.values())
    share = {}
    for P, us in units.items():
        for u in us:
            share[u] = share.get(u, 0) + weight[P]
    over = sorted(((u, s) for u, s in share.items() if 2 * s > total), key=lambda x: -x[1])
    top = max(share.items(), key=lambda x: x[1]) if share else ("none", 0)
    ctx.add("diversity.authority_share", total > 0 and not over,
            ("no A2 rows with a 1/3/5 band" if not total else
             f"{len(over)} unit(s) of discovery decide > 50% of the weight: "
             + "; ".join(f"{u} {100 * s / total:.0f}%" for u, s in over[:4]))
            if not total or over else
            f"largest unit of discovery {top[0]} decides {100 * top[1] / total:.0f}% of {total} weight (≤ 50%; "
            f"transitive over Depends-on, {len(share)} units)")


RX_SEPARATE_RECORDS = re.compile(r"^\s*none\b.*(?:separate (?:records|writes)|2\.2|bundl|§\s?7)", re.I)


def plan_exact_set(ctx, doc, A):
    """rubric-writing: every spot-checked population names its exact-set Outcome row, or declares
    'none — bundle (Rubric Writing §7; Eval 2.2)' with a volume row. An exact set over many items bundles
    independently variable assertions — over separate writes (3_Rubrics_Eval.md 2.2) and over one artifact alike
    (Rubric Writing §7's worst case is "eleven assertions about one artifact") — so the default is the volume
    row, direct rows on every exception, and ≤ 5 samples; controls do not waive atomicity (qc_rubric_v10)."""
    ps = {m.group(1) for i, c, t in A for m in [re.match(r"\s*(P\d+)", c[0] if c else "")] if m}
    bad, separate = [], 0
    for i, c, t in rows_in(doc, r"spot-check"):
        col = t.col(r"exact")
        cell = t.cell(c, col) if col is not None else ""
        if col is not None and RX_SEPARATE_RECORDS.match(cell):
            vcol = t.col(r"volume")
            vol = re.findall(r"\bP\d+\b", t.cell(c, vcol) if vcol is not None else "")
            if not vol or any(g not in ps for g in vol):
                bad.append((i, "separate-records population names no §A volume row"))
            separate += 1
            continue
        got = re.findall(r"\bP\d+\b", cell)
        if col is None or not got or any(g not in ps for g in got):
            bad.append((i, "no 'Exact-set row' column" if col is None else f"exact-set row {cell!r} names no §A row "
                        "(or 'none — separate records (Eval 2.2)' with a volume row)"))
    ctx.add("structure.exact_set_rows", not bad, ("; ".join(f"L{i + 1} {w}" for i, w in bad[:4])) if bad else
            "every spot-check population names its exact-set Outcome row or is declared separate records with a "
            f"volume row ({separate} separate-records population(s); or no population is sampled)",
            [doc.loc(i) for i, _ in bad])


RX_PROBE = re.compile(r"^SHORTCUT PROBE as (\S+) <([^>]+)> · values (\S+) \((\d+) values, (\d+) populations, sha "
                      r"([0-9a-f]{12})\) · k (\d+) · services (\S+) · sql (\S+)", re.M)


def shortcut_check(ctx, doc):
    """rubric-writing: tools/shortcut_probe.py pasted, current, re-run, and every hit dispositioned SHORTCUT-OK."""
    m = RX_PROBE.search(doc.text)
    if not m:
        ctx.add("tool.shortcut_probe", False, "shortcut_probe.py output not pasted (python3 Task_Authoring/tools/"
                "shortcut_probe.py <persona> Task_Authoring/task_inputs/Working_Files/09_Rubric_Writing_Plan.md)")
        return
    sys.path.insert(0, str(HERE))
    import shortcut_probe as sp  # noqa: E402
    probs, p = [], ctx.persona()
    if p is None or m.group(1) != p["persona_key"]:
        probs.append(f"probe ran as {m.group(1)}, assignment persona is {p['persona_key'] if p else '?'}")
    vf = ctx.p(m.group(3))
    if not vf.is_file():
        probs.append(f"values file {m.group(3)} is not in the task folder")
    else:
        vals, pops, _ = sp.load_values(vf)
        sha = sp.values_sha(vals, pops)
        if sha != m.group(6):
            probs.append(f"pasted values sha {m.group(6)} ≠ current {sha} (acceptance values changed: re-run the probe)")
    if int(m.group(7)) > 3:
        probs.append(f"k = {m.group(7)} (the probe's k may not exceed 3)")
    if m.group(8) != "all":
        probs.append(f"probe restricted to services {m.group(8)} (run it on all)")
    want_sql = "01_Universe_Inject.sql" if ctx.p("01_Universe_Inject.sql").exists() else "none"
    if m.group(9) != want_sql:
        probs.append(f"probe sql overlay {m.group(9)} ≠ {want_sql}")
    start = doc.text[:m.start()].count("\n")
    hits, inc, verdict = [], [], None
    for l in doc.lines[start + 1:]:
        if l.strip().startswith("```") or RX_GATE_LINE.match(l):
            break
        h = re.match(r"^HIT (\S+) (\S+) ", l)
        x = re.match(r'^INCOMPLETE (\S+) value:"(.*)" \(', l)
        v = re.match(r"^verdict: (CLEAR|HITS|INCOMPLETE)\b", l)
        if h:
            hits.append((h.group(1), h.group(2)))
        elif x:
            inc.append((x.group(1), x.group(2)))
        elif v:
            verdict = v.group(1)
    if verdict is None:
        probs.append("pasted probe output has no 'verdict:' line")
    oks = [doc.lines[i] for i in range(len(doc.lines)) if not doc.toolfence[i] and "SHORTCUT-OK:" in doc.lines[i]]

    def dispositioned(svc, key):
        for l in oks:
            if key in l and svc in l and len(l.split(key, 1)[1].strip(" —-:|").split()) >= 3:
                return True
        return False
    undisp = [f"{s} {r}" for s, r in hits if not dispositioned(s, r)] + \
             [f"{s} value:\"{v}\"" for s, v in inc if not dispositioned(s, f'value:"{v}"')]
    if undisp:
        probs.append(f"{len(undisp)} shortcut hit(s) not dispositioned 'SHORTCUT-OK: <service> <record> — <reason>': "
                     + "; ".join(undisp[:4]))
    ctx.add("tool.shortcut_probe", not probs, "; ".join(probs) if probs else
            f"shortcut_probe pasted ({m.group(4)} values, {m.group(5)} populations, k {m.group(7)}, verdict {verdict}); "
            f"{len(hits) + len(inc)} reported item(s), all dispositioned")
    if probs:
        return
    if ctx.rerun != "all":
        ctx.skip("tool.shortcut_probe_rerun", f"shortcut_probe re-run skipped (--rerun {ctx.rerun})")
        return
    r, _ = sp.run(m.group(1), vf, int(m.group(7)), sp.ALL, str(ctx.p(want_sql)) if want_sql != "none" else "none")
    got_h = {(h["service"], h["record"]) for h in r["hits"]}
    got_i = {(x["service"], x["value"]) for x in r["incomplete"]}
    ok = got_h == set(hits) and got_i == set(inc)
    ctx.add("tool.shortcut_probe_rerun", ok, "re-run matches the paste" if ok else
            f"re-run differs from the paste (hits {sorted(got_h ^ set(hits))[:3]}, incomplete "
            f"{sorted(got_i ^ set(inc))[:3]}) — the paste is stale or false")


def rubric_validity(ctx, doc):
    """rubric-check: binary validity gate — any validity defect blocks regardless of the percentage tally."""
    probs, locs = [], []
    for i, c, t in rows_in(doc, r"findings"):
        typ = t.cell(c, t.col(r"/rubric. type|type")).strip("` ").lower()
        sev = t.cell(c, t.col(r"severity"))
        if re.search(r"UNRESOLVED", sev):
            continue
        if typ in VALIDITY_TYPES or re.search(r"\bcontradict(?:ion|ory)\b", " ".join(c), re.I):
            probs.append(f"finding L{i + 1} {typ or '?'}" + (" (contradiction)" if typ not in VALIDITY_TYPES else ""))
            locs.append(doc.loc(i))
    for i, c, t in rows_in(doc, r"^coverage"):
        cell = t.cell(c, t.col(r"covered|gap"))
        if re.search(r"\bgap\b|\bmissing\b|\buncovered\b|\bpartial\b", cell, re.I):
            probs.append(f"coverage gap L{i + 1}")
            locs.append(doc.loc(i))
    mu = re.search(r"Unauthorized criteria:\s*(.*)", doc.text)
    if mu and re.search(r"\bC\d+\b", mu.group(1)):
        probs.append(f"unauthorized criteria {mu.group(1).strip()[:40]}")
    for i, c, t in rows_in(doc, r"overlap|predicted all-fail"):
        if ALLFAIL_BASES.search(" ".join(c)):
            probs.append(f"predicted all-fail row L{i + 1} ({ALLFAIL_BASES.search(' '.join(c)).group(0)})")
            locs.append(doc.loc(i))
    for i, c, t in rows_in(doc, r"dimensions"):
        dim, cnt, status = c[0] if c else "", t.cell(c, t.col(r"count")), t.cell(c, t.col(r"status"))
        n = re.match(r"\s*(\d+)", cnt)
        if re.search(r"predicted all-fail", dim, re.I) and n and int(n.group(1)):
            probs.append(f"Predicted all-fail = {n.group(1)} (tolerance 0)")
            locs.append(doc.loc(i))
        elif re.search(r"contradiction|schema|coverage|accuracy", dim, re.I) and re.search(r"\bFAIL\b", status) \
                and not re.search(r"NON-FAIL", status):
            probs.append(f"repair gate '{dim}' {status}")
            locs.append(doc.loc(i))
    ctx.add("validity.rubric", not probs, (f"{len(probs)} validity defect(s) block handoff whatever the tally "
                                           "(incorrect / unauthorized / unobservable / contradiction / missing coverage / "
                                           "predicted all-fail): " + "; ".join(probs[:5])) if probs else
            "binary validity gate clean: no incorrect, unauthorized, unobservable, contradictory, uncovered or "
            "predicted all-fail item", locs)

# ------------------------------------------------------------------ release

RELEASE_STAGES = [("scenario", "01_Scenario_Design.md", True), ("injection", "01_Grounding_Dossier.md", True),
                  ("hardening", "01a_Hardening_Report.md", False), ("reference-files", "02_Reference_Files_Manifest.md", False),
                  ("error-async", "03_Error_Async_Config.txt", False), ("prompt-writing", "04_Prompt_Writing_Brief.md", True),
                  ("prompt-check", "04_Prompt_Check.md", True), ("humantime", "05_Human_Time_Worksheet.md", True),
                  ("oe-writing", "08_OE_Writing_Ledger.md", True), ("oe-check", "08_OE_Check.md", True),
                  ("rubric-writing", "09_Rubric_Writing_Plan.md", True), ("rubric-check", "09_Rubric_Check.md", True),
                  ("allfail", "11_AF_Justification.md", False), ("difficulty", "12_Difficulty_Stats.txt", True)]
BUNDLE_FILES = ["04_Prompt.txt", "08_Oracle_Events.md", "09_Rubrics.json", "01_Universe_Inject.sql", "02_Reference_Files",
                "03_Error_Async_Config.txt", "01_Hardness_Manifest.json", "00_Assigments.md"]
BUNDLE_REQUIRED = {"04_Prompt.txt": "prompt-check", "08_Oracle_Events.md": "oe-check", "09_Rubrics.json": "rubric-check",
                   "01_Universe_Inject.sql": "injection", "01_Hardness_Manifest.json": "injection"}
RX_MARKER = re.compile(r"\b(PROVISIONAL|UNRESOLVED|UNVERIFIED)\b(?!-OK)(?!\s*[:=(—-]?\s*(?:none|0)\b)")


def release_markers(ctx):
    hits = []
    for name in SLOT_ORDER:
        if not name.endswith((".md", ".txt")) or name.startswith(("10_", "13_")) or not ctx.p(name).is_file():
            continue
        d = ctx.doc(name)
        for i, l in enumerate(d.lines):
            if d.toolfence[i] or re.match(r"^\|?\s*:?-{2,}", l.strip()):
                continue
            m = RX_MARKER.search(l)
            if m:
                hits.append(f"{name}:L{i + 1} {m.group(1)}")
            mu = re.match(r"^\s*Unresolved:\s*(\S.*)$", l, re.I)
            if mu and not re.match(r"none\b", mu.group(1), re.I):
                hits.append(f"{name}:L{i + 1} Unresolved: {mu.group(1)[:40]}")
        for s in [d.whole()]:
            for t in s.tables():
                cu = t.col(r"^\s*unresolved\s*$")
                if cu is None:
                    continue
                for i, c in t.rows:
                    v = t.cell(c, cu).strip().strip(".").lower()
                    if v not in ("", "none", "—", "-", "n/a", "0"):
                        hits.append(f"{name}:L{i + 1} Unresolved cell '{t.cell(c, cu)[:30]}'")
    ctx.add("release.markers", not hits, (f"{len(hits)} open marker(s) remain: " + "; ".join(hits[:6])) if hits else
            "no PROVISIONAL / UNRESOLVED / UNVERIFIED marker or open Unresolved item in any artifact", hits)


def difficulty_command(ctx, *args):
    command = [HERE / "difficulty_stats.py", *args]
    return command + (["--task-dir", ctx.td] if ctx.v3 else ["--legacy-v2"])


def v3_precheck(ctx):
    from difficulty_stats import precheck_provenance, trajectory_models, read_trajectory   # one owner
    trajectory = ctx.p("06_PreCheck_Trajectory") / "trajectory.json"
    try:
        data = json.loads(trajectory.read_text())
        models = trajectory_models(trajectory)
        precheck = precheck_provenance(data if isinstance(data, list) else [])
        status, reason, _ = read_trajectory(trajectory)
        ok = bool(data) and status == "completed" and precheck["ok"]
    except (OSError, ValueError, TypeError) as exc:
        models, ok = [], False
        ctx.add("v3.precheck_model", False, f"pre-check trajectory cannot be verified: {exc}")
        return
    ctx.add("v3.precheck_model", ok,
            f"actual pre-check trajectory model metadata: {models}" if ok else
            f"pre-check must be complete with actual Opus 5.5 model metadata; "
            f"observed {models or 'missing'}, status {status} {reason}")


def v3_checks(ctx):
    from v3_artifact_checks import check_evidence
    sql = ctx.p("01_Universe_Inject.sql")
    sql_text = sql.read_text(errors="replace") if sql.is_file() else None
    manifests = {"scenario": "01_Hardness_Manifest.draft.json", "injection": "01_Hardness_Manifest.json",
                 "hardening": "01_Hardness_Manifest.json", "prompt-check": "01_Hardness_Manifest.json"}
    if ctx.stage in manifests:
        name = manifests[ctx.stage]
        keys = ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")
        try:
            actual = json.loads(ctx.p(name).read_text()).get("assignment_context", {})
            mismatched = [key for key in keys if actual.get(key) != ctx.context[key]]
        except (OSError, ValueError, AttributeError) as exc:
            mismatched = [str(exc)]
        ctx.add("v3.manifest_context", not mismatched,
                f"{name} assignment_context missing/mismatched: {mismatched}" if mismatched else
                f"{name} is bound to the current assignment, policy, source context and freeze")

    def reachable(service, record):
        if service in ("gmail", "slack", "gcal", "gdrive", "gdocs", "gsheets", "gslides"):
            result = visibility(ctx, [(service, record)], sql_text).get(record, ("UNVERIFIED", "missing proof"))
            return result[0] == "YES", result[1]
        if service not in ("contacts", "github", "trello", "linear", "snowflake", "confluence"):
            return False, "unsupported evidence service"
        result = ctx.pv().search(ctx.universe(), ctx.persona(), service, record, limit=1, hidden=False)
        return bool(result.get("visible_total")), "record-id lookup in the selected source"

    for cid, ok, detail in check_evidence(ctx.stage, ctx.td, ctx.context,
                                         lambda name: file_digest(ctx.p(name)) if ctx.p(name).exists() else None,
                                         reachable, WS):
        ctx.add(cid, ok, detail)
    # the pre-check model check stays on the release path only (plan §8): in revision intake it would block a repair on a
    # historical export
    if ctx.stage == "release":
        v3_precheck(ctx)


def st_release(ctx):
    present = []
    for stage, f, required in RELEASE_STAGES:
        if required or ctx.p(f).exists():
            chain(ctx, stage, f)
            present.append((stage, f))
    # bundle digest, cross-checked against every digest a stage certificate recorded for a bundle component
    comps = [f for f in BUNDLE_FILES if ctx.p(f).exists()]
    cur = {f: file_digest(ctx.p(f)) for f in comps}
    p = ctx.persona()
    probs = [f"{f} missing" for f in BUNDLE_REQUIRED if f not in cur]
    recorded = {}
    for stage, f in present:
        blocks = [b for b in gate_blocks(ctx.doc(f), stage) if b[1] == "PASS"]
        for name, dg in (blocks[-1][2] if blocks else {}).items():
            if name in cur:
                recorded.setdefault(name, []).append((stage, dg))
    for name, stage in BUNDLE_REQUIRED.items():
        if name in cur and not any(s == stage for s, _ in recorded.get(name, [])):
            probs.append(f"{name} is not certified by the {stage} PASS block")
    for name, recs in recorded.items():
        for stage, dg in recs:
            if dg != cur[name]:
                probs.append(f"{name}: {stage} certified #{dg}, bundle has #{cur[name]}")
    if p is None:
        probs.append("persona not resolvable from 00_Assigments.md")
    canon = "\n".join(f"{f}#{cur[f]}" for f in comps) + f"\npersona#{p['persona_key'] if p else '?'}/{p['email'] if p else '?'}"
    bundle = hashlib.sha256(canon.encode()).hexdigest()[:12]
    ctx.add("release.bundle_digest", not probs, ("; ".join(probs[:5])) if probs else
            f"bundle#{bundle} over {len(comps)} components ({', '.join(comps)}) + persona "
            f"{p['persona_key']}; every stage-recorded component digest matches")
    # each certified stage still newer than its required inputs
    stale = []
    for stage, f in present:
        spec = STAGES[stage]
        for o in spec["outputs"]:
            for i in spec["inputs"]:
                if ctx.p(o).exists() and ctx.p(i).exists() and mtime(ctx.p(i)) > mtime(ctx.p(o)) + 1e-6:
                    stale.append(f"{stage}: {o} older than {i}")
    ctx.add("release.stage_inputs", not stale, ("; ".join(stale[:5]) + " — re-run those stages") if stale else
            f"{len(present)} certified stages each newer than their inputs")
    release_markers(ctx)
    oc = ctx.doc("08_OE_Check.md").text
    sol = re.search(r"Task solvability\s*:?\s*([A-Z_]+)", oc)
    feas = re.search(r"Path feasibility\s*:?\s*([A-Z_]+)", oc)
    blk = re.search(r"^Blocking (\d+)", oc, re.M)
    ok = bool(sol and sol.group(1) == "SUPPORTED_BY_OE" and feas and feas.group(1) == "SUPPORTED" and blk
              and blk.group(1) == "0")
    ctx.add("release.oe_solvability", ok, "OE check: Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE · "
            "Blocking 0" if ok else f"OE check reports Path feasibility {feas.group(1) if feas else '?'} · Task solvability "
            f"{sol.group(1) if sol else '?'} · Blocking {blk.group(1) if blk else '?'} (needs SUPPORTED / SUPPORTED_BY_OE / 0)")
    inp = ctx.p("12_difficulty_input.json")
    rc, out, err = run_tool(difficulty_command(ctx, inp, "--json")) if inp.exists() else (2, "", "missing")
    try:
        blocking = json.loads(out)["blocking"]
    except (ValueError, KeyError):
        blocking = [f"difficulty_stats re-run failed: {(err or out).strip()[:120]}"]
    st = ctx.doc("12_Difficulty_Stats.txt").text
    pasted_none = bool(re.search(r"^Blocking gates:\s*none\b", st, re.M))
    ctx.add("release.difficulty", not blocking and pasted_none, "difficulty gates PASS (difficulty_stats re-run: no "
            "blocking gate; 12_Difficulty_Stats.txt 'Blocking gates: none')" if not blocking and pasted_none else
            f"difficulty gates not clear: re-run blocking {blocking[:4]}; pasted 'Blocking gates: none' "
            f"{'present' if pasted_none else 'missing'}")
    tr = ctx.p("06_PreCheck_Trajectory") / "trajectory.json"
    try:
        okt = tr.is_file() and bool(json.loads(tr.read_text()))
    except ValueError:
        okt = False
    ctx.add("release.precheck_trajectory", okt, "06_PreCheck_Trajectory/trajectory.json present (model provenance checked separately for V3)" if okt else
            "06_PreCheck_Trajectory/trajectory.json missing, empty or not JSON — the pre-check run is required before release")

# ------------------------------------------------------------------ fold-hardening families (plan §4.2, §8)

SURFACE = "01_Gradable_Surface.json"
PREFLIGHT = "01c_Preflight_Report.json"
DISPOSITIONS = "01c_Dispositions.json"
RX_REDTEAM_STUB = re.compile(r"set REDTEAM_MODEL|pass --model|budget_exceeded|\bHTTP \d{3}\b|^redteam_review:\s*(?:error|failed)",
                             re.I | re.M)
RX_REDTEAM_FALLBACK = re.compile(r"^\s*(?:[-*>]\s*)?RED TEAM FALLBACK:\s*(\S.{24,})$", re.M)
RX_LEDGER_ID = re.compile(r"\bhev_[0-9a-f]{16}\b")
REVISE_DISPOSITIONS = re.compile(r"\b(?:keep|purge|rebuild)\b", re.I)


def fold_tool(name):
    """A fold-hardening tool imported in-process (they live beside this file in tools/)."""
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    return __import__(name)


def _sha_file(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None


def redteam(ctx, doc):
    files = [ctx.p("01b_Redteam_Review.md"), ctx.p("01b_Redteam_Review.second.md")]
    missing = [p.name for p in files if not p.exists()]
    stubs = [p.name for p in files if p.exists() and RX_REDTEAM_STUB.search(p.read_text(errors="replace")[:4000])]
    fallback = RX_REDTEAM_FALLBACK.search(doc.text)
    ran = not missing and not stubs
    why = "; ".join(([f"missing {', '.join(missing)}"] if missing else []) +
                    ([f"tool-error stub instead of a review in {', '.join(stubs)}"] if stubs else []))
    ctx.add("tool.redteam_dual", ran or bool(fallback),
            "dual red team present (01b_Redteam_Review.md + .second.md)" if ran else
            (f"red team did not run ({why}); explicit fallback recorded: {fallback.group(1)[:90]}" if fallback else
             f"red team did not run ({why}) — run tools/redteam_review.py --dual with REDTEAM_* set, or record "
             f"'RED TEAM FALLBACK: <who reviewed instead, and why>' in the design (no silent skip, plan §4.2)"))


def surface_check(ctx):
    gs = fold_tool("gradable_surface")
    try:
        surface = gs.load(ctx.p(SURFACE))
    except (OSError, ValueError) as exc:
        ctx.add("surface.valid", False, f"{SURFACE} unreadable: {exc}")
        return
    r = gs.validate(surface, load_manifest(ctx, "01_Hardness_Manifest.draft.json"))
    fails = [f for f in r["findings"] if f["severity"] == "FAIL"]
    rep = r["report"]
    # blocks on the V3 rubric rules (structure, weights, duplicates, sampling, exceptions, mechanisms), each with its
    # basis; the geometry (mechanism share, always-pass share) is reported and never gated (decision 2026-10-25)
    fams = sorted({f["check"].split(".")[0] for f in fails})
    ctx.add("surface.valid", not fails,
            (f"{len(fails)} gradable-surface defect(s): " + "; ".join(
                f"{f['check']}{' ' + f['slot'] if f['slot'] else ''}: {f['detail'][:90]}" for f in fails[:4])
             + (f"; also {', '.join(sorted({f['check'] for f in fails[4:]}))}" if len(fails) > 4 else "")
             + " — basis: " + " | ".join(f"{fam}: {gs.FAMILY_BASIS[fam]}" for fam in fams)) if fails else
            f"{rep['slots']} slots, weight {rep['total_weight']}; geometry report-only, never gated: mechanism share "
            f"{rep['mechanism_share']:.0%}, always-pass share {rep['always_pass_share_if_no_mechanism_lands']:.0%}")


SURFACE_DISPOSITIONS = ("sampled out", "duplicate fact", "not incorporated", "unobservable")
RX_SURFACE_ROW = {"plan": re.compile(r"\bP-?\d+\b"), "check": re.compile(r"\bC-?\d+\b")}
RX_PLACEHOLDER_CELL = re.compile(r"^\s*(?:—|–|-|n/?a|none|tbd|covered|dispositioned|\.\.\.|…)?\s*$", re.I)


def surface_coverage(ctx, doc, mode):
    """Gate 17 (plan §4.6, following missing_coverage): when Working_Files/01_Gradable_Surface.json exists, every slot
    has a line naming a covering row (plan §G: P-n; check `Coverage — gradable surface`: C-n) or a written disposition
    with its reason: sampled out, duplicate fact, not incorporated, unobservable (each followed by why), or another
    reason with its evidence (a record id, row id or gate number). A slot with neither, a `gap`, a slot the table
    misses and a line for a slot the surface doesn't have all block. The mechanism share is reported by the author,
    never gated."""
    sp = ctx.p(SURFACE)
    if not sp.exists():
        ctx.add("surface.coverage", True, f"no {SURFACE}: no slot to account for (gate 17)", status="SKIP")
        return
    try:
        surface = fold_tool("gradable_surface").load(sp)
    except (OSError, ValueError) as exc:
        ctx.add("surface.coverage", False, f"{SURFACE} unreadable: {exc}")
        return
    want = [s.get("id") for s in surface.get("slots") or [] if s.get("id")]
    rx = r"gradable-surface coverage" if mode == "plan" else r"coverage\W+gradable surface"
    where = "§G" if mode == "plan" else "'Coverage — gradable surface'"
    lines, unknown = {}, []
    for i, c, t in rows_in(doc, rx):
        sid = (c[0] if c else "").strip(" `*")
        if sid in want:
            lines.setdefault(sid, []).append((i, c, t))
        elif sid:
            unknown.append(sid)
    covered, disposed, bad = [], [], []
    for sid in want:
        verdicts = []
        for i, c, t in lines.get(sid, []):
            if mode == "plan":
                cov, disp, state = t.cell(c, t.col(r"covered by")), t.cell(c, t.col(r"disposition")), ""
            else:
                cov, disp = t.cell(c, t.col(r"^criteria")), t.cell(c, t.col(r"reason"))
                state = t.cell(c, t.col(r"covered|gap"))
            if re.search(r"\bgap\b|\bmissing\b|\buncovered\b", state, re.I):
                verdicts.append("gap")
            elif RX_SURFACE_ROW[mode].search(cov) and not re.search(r"dispositioned", state, re.I):
                verdicts.append("covered")
            elif not RX_PLACEHOLDER_CELL.match(disp):
                label = next((d for d in SURFACE_DISPOSITIONS if d in disp.lower()), None)
                rest = disp.lower().replace(label, " ") if label else disp
                words = len(re.findall(r"[A-Za-z]{2,}", rest))
                evidenced = bool(RX_ID.search(disp) or re.search(r"\bgate\s*\d+|\b[PCSF]-?\d+\b", disp))
                verdicts.append("dispositioned" if words >= 3 and (label or evidenced) else "reasonless")
            else:
                verdicts.append("neither")
        if "covered" in verdicts:
            covered.append(sid)
        elif "dispositioned" in verdicts:
            disposed.append(sid)
        else:
            bad.append(f"{sid} ({verdicts[0] if verdicts else 'no line'})")
    ok = not bad and not unknown
    ctx.add("surface.coverage", ok,
            f"{len(want)} surface slot(s): {len(covered)} covered, {len(disposed)} dispositioned in {where} (gate 17)"
            if ok else (f"gate 17 (missing_coverage): slots neither covered nor dispositioned with a reason in {where}: "
                        f"{bad[:6]}" + (f"; lines for slots the surface doesn't have (stale): {unknown[:4]}" if unknown
                                        else "")),
            [doc.loc(i) for sid in lines for i, _, _ in lines[sid]][:6])


def ledger_has(ids, kind):
    try:
        led = fold_tool("hardness_ledger").Ledger()
    except Exception as exc:  # noqa: BLE001 - an unreadable ledger is reported, not raised
        return set(), f"ledger unreadable: {exc}"
    return {i for i in ids if (led.by_id.get(i) or {}).get("kind") == kind}, None


def prior_forecast(ctx, doc):
    found, err = ledger_has(set(RX_LEDGER_ID.findall(doc.text)), "forecast")
    ctx.add("forecast.preregistered", bool(found),
            f"prior forecast pre-registered in the ledger: {sorted(found)[:2]} (UNCALIBRATED, advisory)" if found else
            (err or "no pre-registered forecast id (hev_…) cited: run tools/hardness_forecast.py forecast --design "
                    "--preregister (S9b, advisory)"), block=False)


def revise(ctx, doc):
    """S0r: copied from st_hardening (register run steps, counter-reading minimum) plus verdict dispositions and
    revision binding. Returns the LANDED/LEAKED count the self-review minimum is raised to cover."""
    rep = ctx.doc("01a_Hardening_Report.md")
    mm = re.search(r"MODE\s*([AB])", rep.text) if rep.exists else None
    secs = [s for s in doc.sections(r"revision intake") if s.content_lines()]
    if not (mm and mm.group(1) == "B") and not secs:
        ctx.add("revise.intake", True, "no MODE B report and no revision-intake section: nothing to take in", status="SKIP")
        return 0
    if not secs:
        ctx.add("revise.intake", False, "a /create-hardening MODE B report exists: 01_Scenario_Design.md needs a "
                "'Revision intake' section (S0r) that dispositions its proposed verdicts")
        return 0
    text = "\n".join(s.text(tools=False) for s in secs)
    vm = re.search(r"([\w./-]*node_verdicts[\w.-]*\.json)", text)
    verdicts = None
    if vm:
        try:
            verdicts = json.loads(ctx.p(vm.group(1)).read_text())
        except (OSError, ValueError):
            verdicts = None
    ctx.add("revise.intake", verdicts is not None,
            f"revision intake consumes {vm.group(1)}" if verdicts is not None else
            "the revision-intake section must name the node_verdicts.json it dispositions (run_forensics/<revision>/), "
            "and the file must exist")
    if verdicts is None:
        return 0
    rows = {}
    for s in secs:
        for t in s.tables():
            for i, cells in t.rows:
                line = " | ".join(cells)
                for rule in {r for run in verdicts.get("runs", {}).values() for r in run.get("rules", {})}:
                    if re.search(r"(?<![\w-])" + re.escape(rule) + r"(?![\w-])", line):
                        rows.setdefault(rule, []).append((i, line))
    rules = sorted({r for run in verdicts.get("runs", {}).values() for r in run.get("rules", {})})
    flagged = sorted({r for run in verdicts.get("runs", {}).values() for r, v in run.get("rules", {}).items() if v.get("flags")})
    missing = [r for r in rules if r not in rows]
    undisposed = [r for r in rules if r in rows and not any(REVISE_DISPOSITIONS.search(l) for _, l in rows[r])]
    unconfirmed = [r for r in flagged if r in rows and not any(re.search(r"confounded", l, re.I) for _, l in rows[r])]
    ctx.add("revise.verdict_dispositions", not (missing or undisposed or unconfirmed),
            (f"node verdicts without a disposition row: {missing[:6]}; rows without keep/purge/rebuild: {undisposed[:6]}; "
             f"CONFOUNDED candidates neither confirmed nor rejected: {unconfirmed[:6]}") if (missing or undisposed or unconfirmed)
            else f"{len(rules)} proposed node verdict(s) dispositioned; {len(flagged)} CONFOUNDED candidate(s) addressed")
    # bound on evidence only (trajectory_ledger.binding_ok owns the rule): an unchecked SINGLE, a BOUND without its
    # basis and seen needles, INSUFFICIENT, AMBIGUOUS and UNBOUND all need the export marked historical
    tl = fold_tool("trajectory_ledger")
    loose = []
    for lab, run in verdicts.get("runs", {}).items():
        ok_, why = tl.binding_ok(run.get("binding"))
        if not ok_ and not re.search(re.escape(lab) + r"[^\n]*historical|historical[^\n]*" + re.escape(lab), text, re.I):
            loose.append(f"{lab}: {why}")
    ctx.add("revise.revision_binding", not loose,
            f"exports not bound to their revision on evidence and not marked historical: {loose[:4]}" if loose else
            "every export is bound on evidence to the revision it ran on, or marked historical (historical evidence "
            "never certifies a revision)")
    evidence(ctx, doc, "register_run_step", r"revision intake", 1.0,
             pattern=re.compile(r"(?:run-?\d|rollout\s*\d|opus|precheck)[^|]*?(?:step|event|call)\s*#?\d+|"
                                r"(?:step|event|call)\s*#?\d+[^|]*?(?:run-?\d|rollout\s*\d|opus|precheck)", re.I))
    return len(re.findall(r"\b(?:LANDED|LEAKED)\b", text))


def _view(ctx):
    return ("V3", ctx.context["difficulty_mode"]) if ctx.v3 and ctx.context else ("V2", None)


def preflight_checks(ctx):
    try:
        rep = json.loads(ctx.p(PREFLIGHT).read_text())
    except (OSError, ValueError) as exc:
        ctx.add("structure.preflight", False, f"{PREFLIGHT} unreadable: {exc} — run tools/preflight_report.py --task-dir")
        return
    if rep.get("kind") != "PREFLIGHT_REPORT":
        ctx.add("structure.preflight", False, f"{PREFLIGHT} is not a PREFLIGHT_REPORT")
        return
    files = {"sql": "01_Universe_Inject.sql", "solver": "solver/solver.py", "surface": SURFACE,
             "manifest": "01_Hardness_Manifest.json", "dispositions": DISPOSITIONS}
    bound = rep.get("bound_to") or {}
    stale = [f"{k} ({'missing' if _sha_file(ctx.p(f)) is None else 'changed'} since the preflight)"
             for k, f in files.items() if (bound.get(k) or {}).get("sha256") != _sha_file(ctx.p(f))]
    ctx.add("structure.preflight", not stale, ("preflight is stale: " + "; ".join(stale) + " — re-run "
                                                "tools/preflight_report.py") if stale else
            f"{PREFLIGHT} bound by sha256 to the current SQL, solver, surface, manifest and dispositions")
    # S4b solver contract (blocking)
    sc = rep.get("solver_contract") or {}
    ok, detail = sc.get("verdict") == "PASS", f"solver contract {sc.get('verdict')} in the preflight"
    if ok and ctx.rerun == "all":
        ok_ = fold_tool("oracle_kit")
        r = ok_.contract(ctx.p("solver/solver.py"), ctx.p("01_Universe_Inject.sql").read_text(),
                         manifest=load_manifest(ctx), surface=json.loads(ctx.p(SURFACE).read_text()), task_dir=ctx.td)
        ok, detail = r["verdict"] == "PASS", f"solver contract re-run {r['verdict']}" + (
            "" if r["verdict"] == "PASS" else ": " + "; ".join(c["check"] for c in r["checks"] if c["status"] == "FAIL"))
    elif not ok:
        detail += ": " + "; ".join(c["check"] for c in sc.get("checks") or [] if c.get("status") == "FAIL")
    ctx.add("solver.contract", ok, detail)
    # S5b every mutation result dispositioned (blocking), recomputed from the author's file
    dm = fold_tool("difficulty_mutation")
    required = ((rep.get("mutation") or {}).get("dispositions") or {}).get("required") or []
    try:
        recorded = json.loads(ctx.p(DISPOSITIONS).read_text())
    except (OSError, ValueError):
        recorded = {}
    mut = recorded.get("mutation") or {}
    missing = [i for i in required if i not in mut]
    bad = [i for i in required if i in mut and (not isinstance(mut[i], dict) or mut[i].get("disposition") not in dm.DISPOSITIONS
                                                or not str(mut[i].get("reason") or "").strip())]
    ctx.add("mutation.dispositions", bool(required) and not missing and not bad,
            (f"{len(missing)} mutation result(s) without a written disposition: {missing[:6]}" if missing else "")
            + (f"; malformed (needs one of {dm.DISPOSITIONS} and a reason): {bad[:4]}" if bad else "")
            + ("the preflight lists no mutation results" if not required else "") if (missing or bad or not required) else
            f"{len(required)} mutation and intervention results each carry a written disposition ({DISPOSITIONS})")
    # S5b' geometry (U blocking, L_max advisory) in the task's gate view
    view, mode = _view(ctx)
    geo = rep.get("geometry") or {}
    gv = (geo.get("views") or {}).get(view)
    gdisp = recorded.get("geometry") or {}

    def u_ok(v):                       # M2: an UNVERIFIED U passes only with its written disposition (geometry.U)
        return v["U"]["verdict"] == "PASS" or (v["U"]["verdict"] == "UNVERIFIED" and not dm.geometry_dispositions(
            {"views": {view: v}}, gdisp)["missing"])
    ok = bool(gv) and u_ok(gv)
    detail = (f"U {geo.get('U', 0):.3f} ({geo.get('flippable_weight')}/{geo.get('total_weight')}) vs 1 - cap "
              f"{gv['needs_loss_above']:.2f} ({view}{' ' + mode if mode else ''}): {gv['U']['verdict']} "
              f"(bound {gv['U'].get('bound_verdict')})") if gv else (
        f"the preflight has no {view} geometry view")
    if gv and ctx.rerun == "all":
        mod = fold_tool("oracle_kit").load_solver(ctx.p("solver/solver.py"))
        eng = dm.Engine(mod, ctx.p("01_Universe_Inject.sql").read_text())
        surface = json.loads(ctx.p(SURFACE).read_text())
        g = dm.geometry(eng, dm.Slots(surface["slots"], surface), surface,
                        dm.caps_for(view.lower(), ctx.context if ctx.v3 else None))
        ok = u_ok(g["views"][view])
        detail += (f"; re-run U {g['U']:.3f} {g['views'][view]['U']['verdict']} "
                   f"(bound {g['views'][view]['U'].get('bound_verdict')})")
    ctx.add("geometry.upper_bound", ok, detail)
    lm = (gv or {}).get("L_max", {}).get("verdict")
    ctx.add("geometry.margin", lm == "OK", f"L_max {(geo.get('L_max') or {}).get('value')} vs (1 - cap) + 0.10: {lm} "
            "(advisory: the margin is a judgment, not a proof)", block=False)
    live = (rep.get("liveness") or {}).get("dispositions") or {}
    lrec = recorded.get("liveness") or {}
    lmiss = [i for i in live.get("required") or [] if i not in lrec]
    ctx.add("liveness.dispositions", not lmiss, f"{len(lmiss)} liveness flag(s) without a written disposition: "
            f"{lmiss[:6]} (advisory; redesign the difficulty, never remove a fairness link)" if lmiss else
            f"every liveness flag dispositioned ({len(live.get('required') or [])} flag(s))", block=False)
    fc = rep.get("forecast") or {}
    pid = (fc.get("preregistration") or {}).get("id") if isinstance(fc.get("preregistration"), dict) else None
    found, err = ledger_has({pid} if pid else set(), "forecast")
    ctx.add("forecast.preregistered", bool(found), f"forecast {pid} pre-registered in the ledger (UNCALIBRATED)" if found
            else (err or f"forecast {fc.get('status', 'not run')}: pre-register it with tools/hardness_forecast.py "
                         "--preregister before the platform run (advisory)"), block=False)

# ------------------------------------------------------------------ stages


def st_scenario(ctx):
    doc = ctx.doc("01_Scenario_Design.md")
    sections_present(ctx, doc, [
        ("assignment / persona census", r"assignment|census"), ("storyline", r"storyline"),
        ("coherence audit", r"coherence"), ("active speakers", r"active|speaker"),
        ("identity traps", r"identity|entity"), ("cohort spine", r"cohort"), ("hidden authorities", r"hidden authorit"),
        ("delegation lattice", r"delegation"), ("chains / trap register", r"chains|trap register"),
        ("failure-diversity plan", r"failure.diversity"), ("deliverables", r"deliverable"),
        ("service role map", r"service role"), ("call budget", r"call budget"), ("QC rails", r"qc rails"),
        ("reach table (load-bearing records)", r"reach table"),
        ("record plan", r"record plan"), ("integrations / companions", r"integration|companion"),
        ("red team", r"red.team"), ("self-review", r"self[- ]review")])
    placeholders(ctx, doc)
    evidence(ctx, doc, "storyline", r"storyline", 0.8)
    evidence(ctx, doc, "coherence_audit", r"coherence", 1.0)
    evidence(ctx, doc, "hidden_authorities", r"hidden authorit", 1.0)
    evidence(ctx, doc, "delegation", r"delegation", 0.9)
    evidence(ctx, doc, "trap_register", r"chains|trap register", 0.9)
    evidence(ctx, doc, "record_plan", r"record plan", 0.8)
    evidence(ctx, doc, "active_speakers", r"active|speaker", 1.0, pattern=RX_EMAIL)
    # tool outputs
    rx_design = r"HARDNESS GATE \((?:extreme|normal) \(design\)\): (PASS|FAIL)"
    # the profile is the draft manifest's effective_profile (one task property; hardness_gate fails a disagreeing CLI)
    rerun_json_tool(ctx, "tool.hardness_gate_design",
                    [HERE / "hardness_gate.py", ctx.p("01_Hardness_Manifest.draft.json"), "--design", "--json"],
                    rx_design, doc, "hardness_gate --design")
    census(ctx, doc)
    kb_entity(ctx, doc, r"identity|entity")
    kb_gate(ctx, "kb.coherence_hazards", kb_hazards, doc, r"coherence")
    kb_gate(ctx, "kb.activity", kb_activity_rows, doc, r"active|speaker")
    services = set(((load_manifest(ctx, "01_Hardness_Manifest.draft.json") or {}).get("services") or {}).keys())
    kb_gate(ctx, "kb.integrations", kb_integrations, doc, r"integration|companion", services)
    kb_gate(ctx, "kb.storyline", kb_storyline, doc)
    kb_locators(ctx, doc, [("coherence audit", r"coherence"), ("active speakers", r"active|speaker"),
                           ("integrations / companions", r"integration|companion"), ("storyline", r"storyline")])
    anchor_naming(ctx, doc, "01_Hardness_Manifest.draft.json", required=True)
    redteam(ctx, doc)
    surface_check(ctx)
    prior_forecast(ctx, doc)
    n_rev = revise(ctx, doc)
    reach_check(ctx, doc, "scenario", lb_lines(doc, [r"reach table|load-bearing"]), None, planned_ok=True)
    n_dp = len(rows_in(doc, r"two-reading|decision point"))
    self_review(ctx, doc, max(7 + n_dp, n_rev + 1),
                [(n, rx) for n, rx in QC_CATS] + [("hardness_gate output", r"HARDNESS GATE")])


def census(ctx, doc):
    secs = doc.sections(r"assignment|census")
    txt = "\n".join(s.text(tools=True) for s in secs)
    m = re.search(r"REACH\s+(.+?) <([^>]+)>", txt)
    p = ctx.persona()
    if not m:
        ctx.add("tool.persona_reach", False, "persona_view.py reach output not pasted in the census section")
        return
    if p is None or m.group(2) != p["email"]:
        ctx.add("tool.persona_reach", False, f"pasted reach is for {m.group(2)}, assignment persona is "
                f"{p['email'] if p else '?'}")
        return
    r = ctx.pv().reach(ctx.universe(), p, 3, False)
    s = r["services"]["slack"]
    probs = []
    mc = re.search(r"visible channels=(\d+)", txt)
    if not mc or int(mc.group(1)) != s["channels_visible"]:
        probs.append(f"visible channels pasted {mc.group(1) if mc else '?'} ≠ re-run {s['channels_visible']}")
    gm = r["services"]["gmail"]
    if gm.get("mailbox"):
        mt = re.search(r"mailbox=\S+ threads=(\d+)", txt)
        if not mt or int(mt.group(1)) != gm["threads"]:
            probs.append(f"gmail threads pasted {mt.group(1) if mt else '?'} ≠ re-run {gm['threads']}")
    ctx.add("tool.persona_reach", not probs, "; ".join(probs) if probs else
            f"persona_view reach pasted for {p['email']} and matches the re-run ({s['channels_visible']} channels)")


def st_injection(ctx):
    doc = ctx.doc("01_Grounding_Dossier.md")
    sql_text = ctx.p("01_Universe_Inject.sql").read_text(errors="replace")
    specs = [("1.A structural", r"1\.A|structural"), ("1.B entity", r"1\.B|entity"), ("1.C voice", r"1\.C|voice"),
             ("1.D keyword", r"1\.D|keyword"), ("1.E persona reach", r"1\.E|persona reach"),
             ("1.F collision", r"1\.F|collision"), ("record ledger", r"record ledger"),
             ("findability", r"findability"), ("self-validation", r"self-validation"),
             ("integrations / companions", r"integration|companion"), ("coherence census", r"coherence|touched-data"),
             ("intended disagreements", r"intended disagreement"),
             ("constraints for the brief", r"constraints for the prompt brief"),
             ("facts for the human", r"facts for the human"), ("platform follow-ups", r"platform follow"),
             ("self-review", r"self[- ]review")]
    facts_required = SPEC.exists() and re.search(r"[\"`]facts[\"`]", SPEC.read_text())
    if facts_required:
        specs.append(("fact sheet", r"fact sheet|facts manifest|fact_check"))
    sections_present(ctx, doc, specs)
    placeholders(ctx, doc)
    evidence(ctx, doc, "entity", r"1\.B|entity table", 0.9)
    evidence(ctx, doc, "keyword", r"1\.D|keyword", 1.0, pattern=re.compile(RX_ID.pattern + r"|NEW TERM"))
    evidence(ctx, doc, "persona_reach", r"1\.E|persona reach", 1.0)
    evidence(ctx, doc, "record_ledger", r"record ledger", 1.0)
    evidence(ctx, doc, "facts_for_human", r"facts for the human", 1.0)
    lint = rerun_sql_lint(ctx, doc, "01_Universe_Inject.sql")
    injection_lint(ctx, doc, "01_Universe_Inject.sql")
    if lint and lint["warnings"]:
        classes = {}
        for w in lint["warnings"]:
            msg = w["msg"]
            key = ("weekend" if "weekend" in msg else "clock" if "clock" in msg or "deadline" in msg
                   else "confluence" if "Confluence" in msg or "Snowflake" in msg else "delete" if "DELETE" in msg else
                   re.sub(r"[\d.:TZ-]{6,}", "#", msg)[:40])
            classes.setdefault(key, 0)
            classes[key] += 1
        kw = {"weekend": r"weekend", "clock": r"deadline|after the clock|future|not-yet", "confluence":
              r"confluence|snowflake", "delete": r"delete"}
        undisp = [k for k in classes if not re.search(rf"(?:{kw.get(k, re.escape(k))})[^\n]*(?:warn|disposition)|"
                                                       rf"(?:warn|disposition)[^\n]*(?:{kw.get(k, re.escape(k))})",
                                                       doc.text, re.I)]
        ctx.add("review.warning_dispositions", not undisp,
                f"sql_lint warning classes without a disposition line: {undisp}" if undisp else
                f"every sql_lint warning class dispositioned ({', '.join(f'{k}×{v}' for k, v in classes.items())})")
    rerun_json_tool(ctx, "tool.base_check", [HERE / "base_check.py", ctx.p("01_Universe_Inject.sql"), "--json"],
                    r"BASE CHECK \(/injection A \+ C, static\): (PASS|FAIL)", doc, "base_check")
    prof = manifest_profile(ctx)
    pasted_prof = re.findall(r"HARDNESS GATE \((extreme|normal)\): (?:PASS|FAIL)", doc.text)
    if pasted_prof and pasted_prof[-1] != prof:
        ctx.add("tool.hardness_gate_profile", False, f"the dossier pastes hardness_gate ({pasted_prof[-1]}); the manifest's "
                f"effective_profile is {prof}")
    rerun_json_tool(ctx, "tool.hardness_gate",
                    [HERE / "hardness_gate.py", ctx.p("01_Hardness_Manifest.json"), ctx.p("01_Universe_Inject.sql"),
                     "--profile", prof, "--json"], r"HARDNESS GATE \((?:extreme|normal)\): (PASS|FAIL)", doc,
                    "hardness_gate (SQL)")
    design_delta(ctx)
    preflight_checks(ctx)
    # persona_view check-sql
    m = re.search(r"CHECK-SQL as \S+ <([^>]+)>", doc.text)
    mv = re.search(r"^verdict: (PASS|FAIL|REPORT-ONLY)", doc.text, re.M)
    p = ctx.persona()
    ok = bool(m and mv and mv.group(1) == "PASS" and p and m.group(1) == p["email"])
    ctx.add("tool.check_sql_pasted", ok, "persona_view check-sql --load-bearing output pasted with verdict PASS" if ok else
            ("check-sql output not pasted" if not m else f"pasted check-sql verdict is "
             f"{mv.group(1) if mv else '?'} (needs --load-bearing and PASS) or persona differs"))
    reach_check(ctx, doc, "injection", lb_lines(doc, [r"1\.E|persona reach", r"facts for the human"]), sql_text)
    if facts_required:
        try:
            facts = json.loads(ctx.p("01_Hardness_Manifest.json").read_text()).get("facts")
        except ValueError:
            facts = None
        ctx.add("structure.facts_declared", bool(facts),
                f"manifest declares {len(facts)} load-bearing fact(s) in `facts`" if facts else
                "manifest has no `facts` — declare every load-bearing fact; tools/fact_check.py verifies them")
        rerun_json_tool(ctx, "tool.fact_check",
                        [HERE / "fact_check.py", ctx.p("01_Universe_Inject.sql"), "--manifest",
                         ctx.p("01_Hardness_Manifest.json"), "--no-leak", "--json"], r"FACT CHECK: (PASS|FAIL)", doc,
                        "fact_check --no-leak")
    else:
        ctx.add("tool.fact_check", True, "manifest spec has no `facts` field yet — fact_check not required", status="SKIP")
    kb_gate(ctx, "kb.coherence_hazards", kb_hazards, doc, r"coherence|touched-data")
    kb_gate(ctx, "kb.activity", kb_activity_seeded, doc, r"1\.C|voice|realism|speaker", sql_text)
    services = set()
    if lint:
        services = set(lint["stats"]["schemas_touched"])
    kb_gate(ctx, "kb.integrations", kb_integrations, doc, r"integration|companion", services)
    kb_locators(ctx, doc, [("coherence census", r"coherence|touched-data"), ("voice", r"1\.C|voice|realism|speaker"),
                           ("integrations / companions", r"integration|companion"), ("record ledger", r"record ledger")])
    anchor_naming(ctx, doc, "01_Hardness_Manifest.json", required=True)
    n_dis = len(rows_in(doc, r"intended disagreement")) or len([x for s in doc.sections(r"intended disagreement")
                                                                 for x in s.items()])
    self_review(ctx, doc, 7 + n_dis, [(n, rx) for n, rx in QC_CATS] + [("Checks A–C walk", r"check\s*A"),
                                                                       ("touched-data census", r"touched|census")])


def st_hardening(ctx):
    doc = ctx.doc("01a_Hardening_Report.md")
    sections_present(ctx, doc, [("mode / inputs / run validity", r"mode|run validity"), ("register", r"register"),
                                ("routing", r"routing"), ("purge", r"purge"), ("self-review", r"self[- ]review"),
                                ("next steps", r"next step")])
    placeholders(ctx, doc)
    mm = re.search(r"MODE\s*([AB])", doc.text)   # the first mention (section 1) declares the mode
    mode_b = bool(mm and mm.group(1) == "B")
    ctx.add("structure.mode", bool(mm), f"MODE {mm.group(1)} declared" if mm else "report names neither MODE A nor MODE B")
    if mode_b:
        evidence(ctx, doc, "register_run_step", r"register", 1.0,
                 pattern=re.compile(r"(?:run-?\d|rollout\s*\d|opus)[^|]*?(?:step|event|call)\s*#?\d+|"
                                    r"(?:step|event|call)\s*#?\d+[^|]*?(?:run-?\d|rollout\s*\d|opus)", re.I))
        sections_present(ctx, doc, [("predicted band", r"band"), ("per-rollout ledgers", r"ledger"),
                                    ("friction / horizon", r"friction|horizon"), ("why Opus passed", r"why opus")])
    else:
        evidence(ctx, doc, "candidates", r"candidate", 1.0)
    # hardening is revision N+1 (red team A, R1 #18): its gate re-runs the injection checks on the current SQL + manifest
    # and its PASS certifies their digests, so no injection input ever depends on a hardening output (no freshness cycle)
    sub = run_stage("injection", ctx.td, ctx.rerun, ctx.selftest)
    sv = verdict_of(sub, allow_partial=ctx.rerun != "all")
    blocking = [r["id"] for r in sub.res if r["blocking"]]
    ctx.add("revision.injection", sv == "PASS", f"injection checks re-run on revision N+1 (current SQL + manifest + dossier): {sv}"
            + (f"; blocking: {blocking[:6]}" if blocking else ""))
    reg = "\n".join(s.text(tools=False) for s in doc.sections(r"register"))
    n = len(re.findall(r"\b(?:LANDED|LEAKED)\b", reg))
    self_review(ctx, doc, n + 1, [("neighbouring band", r"band|neighbo"), ("re-verified records", r"re-?verif|hg\.py")])


def st_reference_files(ctx):
    doc = ctx.doc("02_Reference_Files_Manifest.md")
    folder = ctx.p("02_Reference_Files")
    files = sorted(f for f in folder.iterdir() if f.name != ".DS_Store") if folder.is_dir() else []
    none = bool(re.search(r"Reference files:\s*none", doc.text, re.I))
    placeholders(ctx, doc)
    if none:
        ctx.add("structure.folder", not files, "Reference files: none and the folder is empty" if not files else
                f"manifest says none but the folder holds {[f.name for f in files]}")
        self_review(ctx, doc, 2)
        return
    probs = [f.name for f in files if f.name.lower() == "readme.md" or f.is_dir() or f.suffix.lower() == ".zip"]
    unnamed = [f.name for f in files if f.is_file() and f.name not in doc.text]
    ctx.add("structure.folder", bool(files) and not probs and not unnamed,
            ("folder empty but manifest lists files" if not files else "") + (f" forbidden entries (README/subfolder/zip): "
                                                                          f"{probs};" if probs else "")
            + (f" files not described in the manifest: {unnamed}" if unnamed else "")
            or f"{len(files)} flat task file(s), each described in the manifest")
    fields = ["File:", "Role:", "Native model:", "Grounded in:", "Deliberate inaccuracies:", "Incorporated?",
              "How the persona would refer", "Must not appear", "Facts for the human"]
    short = [f for f in fields if doc.text.count(f) < max(1, len(files))]
    ctx.add("structure.fields", not short, f"per-file fields missing or not repeated per file: {short}" if short else
            f"all {len(fields)} per-file fields present for {len(files)} file(s)")
    gl = [(i, l) for i, l in enumerate(doc.lines) if "Grounded in:" in l]
    bad = [(i, l) for i, l in gl if not RX_ID.search(l)]
    ctx.add("evidence.grounded_in", not bad, f"{len(bad)} 'Grounded in' line(s) without a record pointer" if bad
            else f"{len(gl)} 'Grounded in' lines cite records", [doc.loc(i) for i, _ in bad])
    for lab, rx in (("folder listing", r"folder listing"), ("readability check", r"readability check")):
        ctx.add(f"structure.{lab.replace(' ', '_')}", bool(re.search(rx, doc.text, re.I)), f"footer '{lab}' "
                + ("present" if re.search(rx, doc.text, re.I) else "missing"))
    self_review(ctx, doc, max(5, len(files)), [("second file fits a reference", r"second file|lookalike"),
                                               ("re-verified", r"re-?verif|hg\.py")])


def st_error_async(ctx):
    doc = ctx.doc("03_Error_Async_Config.txt")
    placeholders(ctx, doc)
    m = re.search(r"^\s*Friction:\s*(none|configured)\b", doc.text, re.M | re.I)
    if not m:
        ctx.add("structure.friction", False, "no 'Friction: none|configured' line")
        return
    def field(name):
        mm = re.search(rf"^[ \t]*{name}:[ \t]*(.*?)[ \t]*(?:#.*)?$", doc.text, re.M)
        v = (mm.group(1) if mm else "").strip().strip("[]").strip()
        return [x.strip() for x in re.split(r"[,\s]+", v) if x.strip()]
    ef, wf = field("error_functions"), field("wait_functions")
    mode, rate = (field("error_mode") or [""])[0].lower(), (field("error_rate") or [""])[0]
    if m.group(1).lower() == "none":
        ctx.add("structure.fields", not ef and not wf, "Friction: none with every field empty" if not ef and not wf
                else f"Friction: none but functions set: {ef + wf}")
        self_review(ctx, doc, 2, [("is the scenario about an outage", r"outage")])
        return
    bad = [f for f in ef if f not in ERROR_FUNCS] + [f for f in wf if f not in WAIT_FUNCS]
    ctx.add("structure.picker_values", not bad and bool(ef or wf), f"not selectable on screen 16: {bad}" if bad else
            ("configured but no function chosen" if not (ef or wf) else f"{len(ef)} error / {len(wf)} wait functions valid"))
    if ef:
        try:
            r = float(rate or "1.0")
        except ValueError:
            r = -1
        okm = (mode in ("", "persistent") and r == 1.0) or (mode == "transient" and 0.1 <= r < 1.0) or \
              (mode == "transient" and r == 1.0)
        ctx.add("structure.mode_rate", okm and 0.1 <= r <= 1.0, f"mode {mode or 'persistent'} / rate {rate or '1.0'} "
                + ("consistent" if okm else "contradictory (persistent below 1.0 is marked transient by the platform)"))
        alt = rows_in(doc, r"alternate path")
        cov = [f for f in ef if not any(f in " ".join(c) for _, c, _ in alt)]
        ctx.add("structure.alternate_rows", not cov, f"errored functions with no alternate-path row: {cov}" if cov
                else f"{len(ef)} errored functions each have an alternate-path row")
        evidence(ctx, doc, "alternate_path", r"alternate path", 1.0)
    if wf:
        dis = rows_in(doc, r"discovery the async")
        ctx.add("structure.async_rows", len(dis) >= len(wf), f"{len(dis)} async discovery rows for {len(wf)} wait "
                "functions")
    self_review(ctx, doc, 6, [("async twin", r"twin"), ("verifier reads", r"verifier"), ("re-verified", r"re-?verif|hg\.py")])


def st_prompt_brief(ctx):
    doc = ctx.doc("04_Prompt_Writing_Brief.md")
    sql = ctx.p("01_Universe_Inject.sql")
    sql_text = sql.read_text(errors="replace") if sql.exists() else None
    sections_present(ctx, doc, [
        ("1 assignment fit", r"assignment fit"), ("2 situation", r"situation"), ("3 investigation", r"investigation"),
        ("4 pinned final state", r"pinned final state"), ("5 discovery map", r"discovery map"),
        ("5a search-as-persona", r"search.as.persona"), ("6 triggers", r"triggers"), ("7 dates", r"dates and constraints"),
        ("8 levers", r"levers"), ("9 must not appear", r"must not appear"), ("10 entity traps", r"entity traps"),
        ("11 pre-submit", r"pre-submit"), ("12 blockers", r"blockers"), ("13 self-review", r"self[- ]review")])
    placeholders(ctx, doc, allow_boxes_rx=r"pre-submit")
    evidence(ctx, doc, "situation", r"situation", 1.0)
    evidence(ctx, doc, "final_state", r"pinned final state", 1.0, pattern=re.compile(RX_ID.pattern + "|" + RX_EMAIL.pattern))
    evidence(ctx, doc, "discovery_map", r"discovery map", 1.0)
    evidence(ctx, doc, "dates", r"dates and constraints", 1.0)
    evidence(ctx, doc, "entity_traps", r"entity traps", 1.0, pattern=re.compile(RX_ID.pattern + "|" + RX_EMAIL.pattern))
    # search-as-persona
    disc = rows_in(doc, r"discovery map")
    sap = rows_in(doc, r"search.as.persona")
    p = ctx.persona()
    pasted_s = re.findall(r"^\s*SEARCH \w+ .+? as (\S+)\s+scope:", doc.text, re.M)
    probs = []
    if len(sap) < len(disc):
        probs.append(f"{len(sap)} search-as-persona rows for {len(disc)} discovery-map facts")
    if not pasted_s:
        probs.append("no persona_view.py search output pasted")
    elif p and any(x != p["persona_key"] for x in pasted_s):
        probs.append(f"pasted searches run as {sorted(set(pasted_s))}, assignment persona is {p['persona_key']}")
    notfound = [(i, c) for i, c, t in sap if re.search(r"\bNO\b|not found", t.cell(c, t.col(r"found"))) and
                not re.search(r"routed", " ".join(c), re.I)]
    if notfound:
        probs.append(f"{len(notfound)} fact(s) the persona cannot find with a natural search and not routed")
    ctx.add("tool.search_as_persona", not probs, "; ".join(probs) if probs else
            f"{len(sap)} facts proven findable by persona_view search as {p['persona_key'] if p else '?'}",
            [doc.loc(i) for i, _ in notfound])
    hit_lines = [i for i, c, t in sap]
    reach_check(ctx, doc, "brief", lb_lines(doc, [r"discovery map", r"search.as.persona"]) | set(hit_lines), sql_text)
    kb_entity(ctx, doc, r"entity traps")
    kb_locators(ctx, doc, [("entity traps", r"entity traps")])
    canonical_outcome(ctx, doc)
    anchor_naming(ctx, doc)
    self_review(ctx, doc, 6, [("fair readings" if ctx.v3 else "UGT", r"fair (?:readings|outcomes)|accepted outcomes" if ctx.v3 else r"\bUGT\b|unique ground truth"), ("clarity", r"clarity"),
                              ("incorporation", r"incorporat"), ("truthfulness", r"truthful"),
                              ("feasibility / ACL", r"feasib|\bACL\b"), ("contrived register", r"contrived")])


def st_prompt_check(ctx):
    doc = ctx.doc("04_Prompt_Check.md")
    prompt = ctx.p("04_Prompt.txt").read_text(errors="replace") if ctx.p("04_Prompt.txt").exists() else ""
    sections_present(ctx, doc, [("summary", r"summary"), ("findings", r"findings"),
                                ("fair readings" if ctx.v3 else "UGT readings", r"fair readings|accepted outcomes|ugt" if ctx.v3 else r"ugt"),
                                ("verification log", r"verification log"), ("brief coverage", r"brief coverage"),
                                ("self-review", r"self[- ]review"), ("route", r"route")])
    placeholders(ctx, doc)
    m = re.search(r"Prompt: 04_Prompt\.txt · (\d+) words · sha256 ([0-9a-f]{12})", doc.text)
    wc, sha = len(prompt.split()), hashlib.sha256(prompt.encode()).hexdigest()[:12]
    ctx.add("structure.prompt_hash", bool(m) and int(m.group(1)) == wc and m.group(2) == sha,
            f"header ties the report to 04_Prompt.txt ({wc} words, sha256 {sha})" if m and int(m.group(1)) == wc and
            m.group(2) == sha else (f"header missing 'Prompt: 04_Prompt.txt · N words · sha256 X'" if not m else
                                    f"header says {m.group(1)} words / {m.group(2)}, file is {wc} / {sha} — stale check"))
    substr_check(ctx, "evidence.quoted_spans", doc, rows_in(doc, r"findings"), r"quoted span", prompt, "04_Prompt.txt")
    substr_check(ctx, "evidence.coverage_spans", doc, rows_in(doc, r"brief coverage"), r"present|span", prompt,
                 "04_Prompt.txt", require_quote=True)
    missing = [f"C{k}" for k in range(1, 25) if not re.search(rf"\bC{k}\b", doc.text)]
    ctx.add("structure.c_checks", not missing, f"checks with no result anywhere: {missing}" if missing
            else "every C1–C24 has a recorded result")
    evidence(ctx, doc, "verification_log", r"verification log", 1.0,
             pattern=re.compile(RX_ID.pattern + "|" + RX_EMAIL.pattern + r"|UNVERIFIED|hg\.py"))
    for lab, rx in (("band", r"predicted /prompt band|band:"), ("status", r"BLOCKED|UNRESOLVED|READY FOR /prompt")):
        ctx.add(f"structure.summary_{lab}", bool(re.search(rx, doc.text, re.I)), f"summary {lab} "
                + ("present" if re.search(rx, doc.text, re.I) else "missing"))
    clock_check(ctx, doc)
    tier_hardness(ctx)
    self_review(ctx, doc, 24, [(f"C{k}", rf"\bC{k}\b") for k in range(1, 25)])


def st_humantime(ctx):
    doc = ctx.doc("05_Human_Time_Worksheet.md")
    placeholders(ctx, doc)
    m = re.search(r"^\s*Hours:\s*([\d.]+)", doc.text, re.M)
    rows = [(i, c, t) for t in doc.whole().tables() if t.col(r"minutes") is not None for (i, c) in t.rows]
    if not m or not rows:
        ctx.add("structure.worksheet", False, "no 'Hours:' line or no sub-task table with a Minutes column")
        return
    hours = float(m.group(1))
    total, data, bad_vol = None, [], []
    for i, c, t in rows:
        mins = re.findall(r"[\d.]+", t.cell(c, t.col(r"minutes")))
        if c and c[0].lower().startswith("total"):
            total = (i, mins)
            continue
        data.append((i, c, t, float(mins[0]) if mins else None))
        if not re.search(r"\d", t.cell(c, t.col(r"volume"))):
            bad_vol.append(i)
    s = sum(x[3] or 0 for x in data)
    probs = []
    if any(x[3] is None for x in data):
        probs.append("a sub-task row has no minutes")
    if abs(hours * 4 - round(hours * 4)) > 1e-9:
        probs.append(f"hours {hours} not on a 0.25 step")
    if abs(s - hours * 60) > 1e-6:
        probs.append(f"sub-task minutes sum to {s:g} ≠ {hours} h × 60 = {hours * 60:g}")
    ctx.add("structure.arithmetic", not probs, "; ".join(probs) if probs else f"{len(data)} sub-tasks sum to {s:g} min = {hours} h")
    ctx.add("evidence.volumes", not bad_vol, f"{len(bad_vol)} row(s) with no measured volume" if bad_vol
            else f"every sub-task has a measured volume", [doc.loc(i) for i in bad_vol])
    kinds = " ".join(t.cell(c, t.col(r"kind")) for _, c, t, _ in data).lower()
    need = []
    if ctx.p("01_Hardness_Manifest.json").exists() and "dead end" not in kinds:
        need.append("dead end (manifest traps exist)")
    cfg = ctx.p("03_Error_Async_Config.txt")
    if cfg.exists() and re.search(r"Friction:\s*configured", cfg.read_text(), re.I) and "workaround" not in kinds:
        need.append("workaround (friction configured)")
    if "write" not in kinds:
        need.append("write")
    ctx.add("structure.kinds", not need, f"missing sub-task kinds: {need}" if need else "dead-end / workaround / write lines present")
    cl = re.search(r"Condensed breakdown length:\s*(\d+)", doc.text)
    ctx.add("structure.field_length", bool(cl) and 50 <= int(cl.group(1)) <= 2000,
            f"condensed breakdown {cl.group(1)} characters" if cl else "no 'Condensed breakdown length: N' line")
    src = re.search(r"Sources measured:\s*(.+)", doc.text)
    ctx.add("evidence.sources", bool(src) and bool(re.search(r"hg\.py|persona_view", src.group(1) if src else "")),
            "volume sources name the hg.py / persona_view queries" if src and re.search(r"hg\.py|persona_view", src.group(1))
            else "'Sources measured:' missing or names no hg.py / persona_view query")
    ctx.add("structure.tier_check", bool(re.search(r"^\s*Tier check:\s*\S", doc.text, re.M)), "tier check line "
            + ("present" if re.search(r"^\s*Tier check:\s*\S", doc.text, re.M) else "missing"))
    self_review(ctx, doc, 5, [("inflated", r"inflat"), ("solution-path", r"solution"), ("evaluator-wide", r"evaluator"),
                              ("tier mismatch", r"tier"), ("linter reading", r"linter")])


def st_oe_ledger(ctx):
    doc = ctx.doc("08_OE_Writing_Ledger.md")
    prompt = ctx.p("04_Prompt.txt").read_text(errors="replace")
    sql = ctx.p("01_Universe_Inject.sql")
    sql_text = sql.read_text(errors="replace") if sql.exists() else None
    sections_present(ctx, doc, [("A requirements", r"^A\b"), ("B facts", r"^B\b"),
                                ("C write capability", r"^C\b|write capability"), ("D friction", r"^D\b"),
                                ("E traps", r"^E\b"), ("F open risks", r"^F\b|open risks"), ("G tally", r"^G\b|tally"),
                                ("self-review", r"self[- ]review")])
    placeholders(ctx, doc)
    ctx.add("structure.status", bool(re.search(r"^Status:\s*(READY|BLOCKED)", doc.text, re.M)),
            "Status line " + ("present" if re.search(r"^Status:\s*(READY|BLOCKED)", doc.text, re.M) else "missing"))
    A, B = rows_in(doc, r"^A\b"), rows_in(doc, r"^B\b")
    substr_check(ctx, "evidence.prompt_spans", doc, A, r"prompt span", prompt, "04_Prompt.txt")
    evidence(ctx, doc, "facts_sourced", r"^B\b", 1.0, col=r"source pointer")
    evidence(ctx, doc, "traps_sourced", r"^E\b", 1.0, require=False)
    # visibility per B row
    need, idx = set(), set()
    for i, c, t in B:
        ids = scoped_ids(" ".join(c))
        if ids:
            idx.add(i)
            need.update(x for _, x in ids)
    reach_check(ctx, doc, "ledger_B", idx | lb_lines(doc, []), sql_text)
    pasted_cansee(ctx, doc, need, sql_text)
    facts = ledger_facts(doc)
    scoped_fact_ids(ctx, doc, facts)
    locator_provenance(ctx, doc, facts, prompt, sql_text)
    defer_search(ctx, doc)
    tally = re.search(r"Requirements (\d+) · facts (\d+)", doc.text)
    ok = bool(tally) and int(tally.group(1)) == len(A) and int(tally.group(2)) == len(B)
    ctx.add("structure.tally", ok, f"tally matches the tables ({len(A)} requirements, {len(B)} facts)" if ok else
            f"tally {'missing' if not tally else tally.group(0)} vs tables: {len(A)} requirements, {len(B)} facts")
    self_review(ctx, doc, max(1, len(A)), [("no-event-text scan", r"event.text"), ("re-verified", r"re-?verif|hg\.py")])


def universe_clock_line(ctx):
    """universe.clock_line (as hg_universe.report_line emits it: 'Clock: <clock_text>, <label>')."""
    u = (ctx.context or {}).get("universe") or {}
    s = re.sub(r"\s+", " ", str(u.get("clock_line") or "")).strip()
    return re.sub(r"^Clock:\s*", "", s, flags=re.I)


def clock_check(ctx, doc, required=False):
    """The eval's `Clock:` line. Required where the playbook template carries it; elsewhere a present line
    must still agree with universe.clock_line. No check when the context has no universe clock."""
    want = universe_clock_line(ctx)
    if not want:
        return
    m = re.search(r"^\s*Clock:\s*(.+?)\s*$", doc.text, re.M)
    got = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    if not m and not required:
        return
    ok = bool(m) and got == want
    ctx.add("structure.clock", ok,
            (f"'Clock: {want}' matches the universe" if ok else
             f"Clock line {got!r} does not match universe.clock_line {want!r}" if m else
             f"no 'Clock: {want}' line in {doc.rel}"))


def st_oe_check(ctx):
    doc = ctx.doc("08_OE_Check.md")
    oe = ctx.p("08_Oracle_Events.md").read_text(errors="replace")
    sections_present(ctx, doc, [("inventory", r"inventory"), ("coverage", r"coverage"),
                                ("expected-data sign-off", r"sign-off"), ("findings", r"findings"),
                                ("pre-verdict sweep", r"pre-verdict"), ("tally", r"tally"),
                                ("self-review", r"self[- ]review")])
    placeholders(ctx, doc)
    m = re.search(r"Events (\d+) · Characters (\d+)", doc.text)
    n_ev = len(re.findall(r"^\s*(?:#+\s*)?(?:\*\*)?OE\s*\d+", oe, re.M))
    okm = bool(m) and int(m.group(1)) == n_ev and abs(int(m.group(2)) - len(oe)) <= 2
    ctx.add("structure.header_counts", okm, f"header matches 08_Oracle_Events.md ({n_ev} events, {len(oe)} chars)" if okm
            else f"header {'missing' if not m else m.group(0)} vs file: {n_ev} events, {len(oe)} characters — stale check")
    ctx.add("structure.prediction", bool(re.search(r"/oe prediction[^\n]*(FAIL 2|NON-FAIL 3|PASS 5|PARTIAL)", doc.text)),
            "/oe prediction line " + ("present" if re.search(r"/oe prediction", doc.text) else "missing"))
    clock_check(ctx, doc)
    F = rows_in(doc, r"findings")
    substr_check(ctx, "evidence.quoted_spans", doc, F, r"quoted span", oe, "08_Oracle_Events.md")
    evidence(ctx, doc, "findings_evidence", r"findings", 1.0, col=r"evidence",
             pattern=re.compile(RX_ID.pattern + r"|\bF\d+\b"), require=False)
    evidence(ctx, doc, "signoff_reread", r"sign-off", 1.0, col=r"source re-read|re-read",
             pattern=re.compile(RX_ID.pattern + r"|hg\.py"))
    sweep = rows_in(doc, r"pre-verdict")
    ctx.add("structure.sweep", len(sweep) >= 7, f"pre-verdict sweep has {len(sweep)}/7 rows")
    tl = re.search(r"Blocking (\d+)", doc.text)
    nb = sum(1 for _, c, t in F if "BLOCKING" in t.cell(c, t.col(r"severity")).upper())
    ctx.add("structure.tally", bool(tl) and int(tl.group(1)) == nb, f"tally Blocking {tl.group(1) if tl else '?'} vs "
            f"{nb} BLOCKING findings")
    cov = rows_in(doc, r"coverage")
    self_review(ctx, doc, len(cov) + len(F), [("re-verified", r"re-?verif|hg\.py")])


def st_rubric_plan(ctx):
    doc = ctx.doc("09_Rubric_Writing_Plan.md")
    prompt = ctx.p("04_Prompt.txt").read_text(errors="replace")
    led = ctx.doc("08_OE_Writing_Ledger.md")
    sql = ctx.p("01_Universe_Inject.sql")
    sql_text = sql.read_text(errors="replace") if sql.exists() else None
    sections_present(ctx, doc, [("A coverage matrix", r"coverage matrix"), ("A2 grading risks", r"grading risks"),
                                ("B OE trace", r"oe trace"), ("C process candidates", r"process candidates"),
                                ("D spot-check groups", r"spot-check"), ("E summary", r"summary"),
                                ("self-review", r"self[- ]review")])
    placeholders(ctx, doc)
    ctx.add("structure.oe_status", bool(re.search(r"OE status:\s*(?:/oe PASS|PROVISIONAL)", doc.text)),
            "OE status line " + ("present" if re.search(r"OE status:", doc.text) else "missing"))
    A = rows_in(doc, r"coverage matrix")
    A2 = rows_in(doc, r"grading risks")
    substr_check(ctx, "evidence.prompt_spans", doc, A, r"source", prompt, "04_Prompt.txt", require_quote=True)
    evidence(ctx, doc, "values_fids", r"coverage matrix", 1.0, col=r"values", pattern=RX_FID)
    ledger_f = {}
    for i, c, t in rows_in(led, r"^B\b"):
        m = re.match(r"\s*(F\d+)", c[0] if c else "")
        if m:
            ledger_f[m.group(1)] = " ".join(c)
    cited = {f for _, c, t in A for f in RX_FID.findall(t.cell(c, t.col(r"values")))}
    unknown = sorted(cited - set(ledger_f))
    ctx.add("evidence.fids_in_ledger", not unknown, f"F-ids not in the ledger: {unknown}" if unknown
            else f"{len(cited)} F-ids resolve to ledger rows")
    bad_band = [i for i, c, t in A2 if t.cell(c, t.col(r"band")).strip() not in ("1", "3", "5")]
    ctx.add("structure.bands", not bad_band and len(A2) == len(A),
            f"{len(A2)} A2 rows for {len(A)} A rows; {len(bad_band)} band(s) not 1/3/5", [doc.loc(i) for i in bad_band])
    rn = re.search(r"Rows (\d+)", doc.text)
    ctx.add("structure.summary_rows", bool(rn) and int(rn.group(1)) == len(A), f"summary Rows "
            f"{rn.group(1) if rn else '?'} vs {len(A)} matrix rows")
    need = {x for f in cited if f in ledger_f for _, x in scoped_ids(ledger_f[f])}
    pasted_cansee(ctx, doc, need, sql_text, "visibility_proof")
    facts = ledger_facts(led)
    plan_reach(ctx, doc, cited, facts, sql_text)
    plan_allfail(ctx, doc, A2)
    plan_diversity(ctx, doc, A, A2, facts)
    plan_exact_set(ctx, doc, A)
    shortcut_check(ctx, doc)
    surface_coverage(ctx, doc, "plan")
    self_review(ctx, doc, max(1, len(A)), [("predicted all-fail re-check", r"all-fail"),
                                           ("re-verified", r"re-?verif|hg\.py")])


def st_rubric_check(ctx):
    doc = ctx.doc("09_Rubric_Check.md")
    try:
        crit = json.loads(ctx.p("09_Rubrics.json").read_text())
    except ValueError:
        crit = None
    sections_present(ctx, doc, [("coverage", r"coverage"), ("findings", r"findings"),
                                ("overlap / spot-check / all-fail", r"overlap"), ("dimensions", r"dimensions"),
                                ("self-review", r"self[- ]review")])
    placeholders(ctx, doc)
    n = len(crit) if isinstance(crit, list) else None
    m = re.search(r"Criteria (\d+)", doc.text)
    ctx.add("structure.criteria_count", bool(m) and n is not None and int(m.group(1)) == n,
            f"header Criteria {m.group(1) if m else '?'} vs 09_Rubrics.json {n if n is not None else 'unparseable'}")
    src = "\n".join(str(v) for c in (crit or []) if isinstance(c, dict) for v in c.values())
    F = rows_in(doc, r"findings")
    substr_check(ctx, "evidence.quoted_spans", doc, F, r"quoted span", src, "09_Rubrics.json")
    badt = [i for i, c, t in F if t.cell(c, t.col(r"/rubric. type|type")).strip("` ") not in RUBRIC_TYPES]
    ctx.add("structure.issue_types", not badt, f"{len(badt)} finding(s) with a type outside /rubric's taxonomy" if badt
            else "every finding uses a /rubric issue type", [doc.loc(i) for i in badt])
    dims = rows_in(doc, r"dimensions")
    ctx.add("structure.dimensions", len(dims) >= 7, f"dimension table has {len(dims)}/7+ rows")
    ctx.add("structure.readiness", bool(re.search(r"Readiness for /rubric:\s*(FAIL-RISK|NON-FAIL-RISK|CLEAN)", doc.text)),
            "readiness line " + ("present" if re.search(r"Readiness for /rubric:", doc.text) else "missing"))
    rubric_validity(ctx, doc)
    surface_coverage(ctx, doc, "check")
    self_review(ctx, doc, n or 1, [(f"C{k}", rf"\bC{k}\b") for k in range(1, (n or 0) + 1)] +
                [("re-verified", r"re-?verif|hg\.py")])


def st_allfail(ctx):
    doc = ctx.doc("11_AF_Justification.md")
    rub = ctx.p("09_Rubrics.json").read_text(errors="replace") if ctx.p("09_Rubrics.json").exists() else ""
    placeholders(ctx, doc)
    mc = re.search(r"Completed rollouts:\s*(\d+)/6", doc.text)
    ma = re.search(r"All-fail rubrics:\s*(.+)", doc.text)
    if not mc or not ma:
        ctx.add("structure.header", False, "missing 'Completed rollouts: n/6' or 'All-fail rubrics:' line")
        return
    listed = set(re.findall(r"\bR\d+\b", ma.group(1)))
    inp = ctx.p("12_difficulty_input.json")
    if inp.exists():
        rc, out, err = run_tool(difficulty_command(ctx, inp, "--json"))
        try:
            calc = set(json.loads(out)["all_fail_rubrics"])
            ctx.add("tool.difficulty_stats", calc == listed, f"all-fail list {sorted(listed)} "
                    + ("matches" if calc == listed else f"≠ calculator {sorted(calc)}"))
        except (ValueError, KeyError):
            ctx.add("tool.difficulty_stats", False, f"difficulty_stats re-run failed: {(err or out)[:200]}")
    else:
        ctx.add("tool.difficulty_stats", False, "12_difficulty_input.json missing — build it with difficulty_stats.py "
                "--build (playbook Step 1) so the all-fail list can be recomputed")
    blocks = [(i, m.group(1), m.group(2)) for i, l in enumerate(doc.lines)
              for m in [re.match(r"^#{2,4}\s*(R\d+)\s*—\s*(VALID|INVALID — rubric|INVALID — environment|JUDGE ERROR|"
                                 r"UNRESOLVED)", l)] if m]
    ctx.add("structure.blocks", {b[1] for b in blocks} == listed, f"{len(blocks)} verdict blocks for all-fail {sorted(listed)}")
    completed = int(mc.group(1))
    tests = ["authority", "grounding", "reachability", "capability", "atomicity", "precision", "phrasing", "friction"]
    probs = []
    for k, (i, rid, verdict) in enumerate(blocks):
        end = blocks[k + 1][0] if k + 1 < len(blocks) else next(
            (j for j in range(i + 1, len(doc.lines)) if re.match(r"^(?:Summary:|#+\s*Self)", doc.lines[j])), len(doc.lines))
        body = "\n".join(doc.lines[i:end])
        cq = re.search(r"Criterion:\s*\"(.+?)\"\s*$", body, re.M)
        if not cq or cq.group(1) not in rub:
            probs.append(f"{rid}: criterion quote not an exact substring of 09_Rubrics.json")
        ev = re.search(r"Per-run evidence:(.+?)(?=\n(?:Tests|Causation|Shared root cause|Justification|Finding)[^:\n]*:|\Z)",
                       body, re.S)
        runs = set(re.findall(r"run-(\d+)", ev.group(1) if ev else ""))
        if len(runs) < completed or not re.search(r"event \d+|step \d+", ev.group(1) if ev else ""):
            probs.append(f"{rid}: per-run evidence covers {len(runs)}/{completed} runs or lacks event/step locators")
        tl = re.search(r"Tests:(.+)", body)
        miss = [t for t in tests if not tl or t not in tl.group(1).lower()]
        if miss:
            probs.append(f"{rid}: tests not answered: {miss}")
        if verdict == "VALID":
            j = re.search(r"Justification[^:]*:\s*(.+)", body)
            if not j or len(re.findall(r"[.!?](?:\s|$)", j.group(1))) > 2 or len(j.group(1).split()) < 8:
                probs.append(f"{rid}: VALID needs a 1–2 sentence justification")
        elif not re.search(r"Finding[^:]*:\s*\S", body):
            probs.append(f"{rid}: {verdict} needs a Finding line")
    ctx.add("structure.block_fields", not probs, "; ".join(probs[:6]) if probs else f"{len(blocks)} blocks complete")
    for lab in ("Summary:", "Hand-off to /create-difficulty:"):
        ctx.add(f"structure.{lab.split()[0].strip(':').lower()}", lab in doc.text, f"'{lab}' line "
                + ("present" if lab in doc.text else "missing"))
    clock_check(ctx, doc)
    self_review(ctx, doc, len(blocks) + 1, [("recomputed list", r"recompute"), ("re-verified", r"re-?verif|hg\.py")])


def st_difficulty(ctx):
    doc = ctx.doc("12_Difficulty_Stats.txt")
    placeholders(ctx, doc)
    rc, out, err = run_tool(difficulty_command(ctx, ctx.p("12_difficulty_input.json")))
    if rc not in (0, 1) or "| Gate |" not in out:
        ctx.add("tool.difficulty_stats", False, f"difficulty_stats re-run failed: {(err or out)[:200]}")
    else:
        want = [l.rstrip() for l in out.splitlines() if re.match(r"^\| (?:errored_runs|pass_at_1|avg_weighted|per_rollout|"
                                                                  r"failure_patterns|horizon|baseline_models)", l) or
                l.startswith("All-fail rubrics")]
        have = {l.rstrip() for l in doc.lines}
        miss = [w for w in want if w not in have]
        ctx.add("tool.difficulty_stats", not miss, f"{len(miss)} calculator line(s) not pasted unchanged, e.g. "
                f"{miss[0][:80]!r}" if miss else f"{len(want)} gate lines match the re-run verbatim")
    labels = ["Task type:", "Readings:", "Tool-call notes:", "Friction check:", "Screen 60 comparison:", "Diagnosis:",
              "Screen 61:"]
    if ctx.v3:                      # the eval report template carries the universe clock line; V2 fixtures predate it
        labels.insert(2, "Clock:")
    miss = [l for l in labels if l not in doc.text]
    ctx.add("structure.labels", not miss, f"missing report lines: {miss}" if miss else "all report lines present")
    clock_check(ctx, doc, required=True)
    af = ctx.p("11_AF_Justification.md")
    if af.exists():
        h = re.search(r"--invalid\s+([\w,]+)", af.read_text())
        inv = set((h.group(1) if h else "").split(",")) - {"", "none"}
        mi = re.search(r"Invalid rubrics:\s*([^\n]*?)(?:\s{2,}|$)", doc.text, re.M)
        got = set(re.findall(r"R\d+", mi.group(1) if mi else ""))
        try:
            marked = {r["id"] for r in json.loads(ctx.p("12_difficulty_input.json").read_text()).get("rubrics", [])
                      if r.get("valid") is False}
        except (ValueError, OSError):
            marked = None
        ctx.add("structure.handoff_match", inv == got and marked == inv,
                f"Invalid rubrics {sorted(got)} vs 11 hand-off {sorted(inv)} vs valid:false in the input JSON "
                f"{sorted(marked) if marked is not None else 'unreadable'}")
    self_review(ctx, doc, 6, [("errored", r"errored"), ("pass@1", r"pass@1"), ("average", r"average"), ("SD", r"\bSD\b"),
                              ("patterns", r"pattern"), ("horizon", r"horizon")]
                + ([("actual baseline model metadata", r"model|Opus 5\.5")] if ctx.v3 else []))


STAGES = {
    "scenario": dict(fn=st_scenario, primary="01_Scenario_Design.md",
                     outputs=["01_Scenario_Design.md", "01_Hardness_Manifest.draft.json", SURFACE],
                     inputs=["00_Assigments.md"], optional=[], upstream=[]),
    # injection reads only upstream design slots: never reference-files / error-async / hardening outputs (their stages
    # need an injection PASS, so consuming them would make a freshness cycle — red team A, R1 #18). For the same reason
    # injection never rewrites the scenario's gradable surface: expected values and flipped_by go into the preflight.
    "injection": dict(fn=st_injection, primary="01_Grounding_Dossier.md",
                      outputs=["01_Universe_Inject.sql", "01_Hardness_Manifest.json", "01_Grounding_Dossier.md",
                               "solver/solver.py", DISPOSITIONS, PREFLIGHT],
                      inputs=["00_Assigments.md", "01_Scenario_Design.md", "01_Hardness_Manifest.draft.json", SURFACE],
                      optional=[], upstream=[("scenario", "01_Scenario_Design.md")]),
    "hardening": dict(fn=st_hardening, primary="01a_Hardening_Report.md", outputs=["01a_Hardening_Report.md"],
                      inputs=["00_Assigments.md", "01_Grounding_Dossier.md"],
                      optional=["06_PreCheck_Trajectory", "07_Baseline_Trajectories", "10_Baseline_Verifier_Results.md",
                                "12_Difficulty_Stats.txt"], upstream=[("injection", "01_Grounding_Dossier.md")],
                      digest_extra=["01_Universe_Inject.sql", "01_Hardness_Manifest.json"]),
    "reference-files": dict(fn=st_reference_files, primary="02_Reference_Files_Manifest.md",
                            outputs=["02_Reference_Files_Manifest.md"],
                            inputs=["00_Assigments.md", "01_Grounding_Dossier.md", "01_Universe_Inject.sql"],
                            optional=["03_Error_Async_Config.txt"], upstream=[("injection", "01_Grounding_Dossier.md")]),
    "error-async": dict(fn=st_error_async, primary="03_Error_Async_Config.txt", outputs=["03_Error_Async_Config.txt"],
                        inputs=["00_Assigments.md", "01_Grounding_Dossier.md", "01_Universe_Inject.sql"],
                        optional=[], upstream=[("injection", "01_Grounding_Dossier.md")]),
    "prompt-writing": dict(fn=st_prompt_brief, primary="04_Prompt_Writing_Brief.md", outputs=["04_Prompt_Writing_Brief.md"],
                         inputs=["00_Assigments.md", "01_Grounding_Dossier.md", "01_Universe_Inject.sql"],
                         optional=["03_Error_Async_Config.txt", "02_Reference_Files_Manifest.md",
                                   "01a_Hardening_Report.md"],
                         upstream=[("injection", "01_Grounding_Dossier.md"),
                                   ("error-async", "03_Error_Async_Config.txt?"),
                                   ("reference-files", "02_Reference_Files_Manifest.md?")]),
    "prompt-check": dict(fn=st_prompt_check, primary="04_Prompt_Check.md", outputs=["04_Prompt_Check.md"],
                         inputs=["04_Prompt.txt", "04_Prompt_Writing_Brief.md"], optional=[],
                         upstream=[("prompt-writing", "04_Prompt_Writing_Brief.md")], digest_extra=["04_Prompt.txt"]),
    "humantime": dict(fn=st_humantime, primary="05_Human_Time_Worksheet.md", outputs=["05_Human_Time_Worksheet.md"],
                      inputs=["04_Prompt.txt", "00_Assigments.md"],
                      optional=["08_Oracle_Events.md", "07_Baseline_Trajectories", "12_Difficulty_Stats.txt"],
                      upstream=[("prompt-check", "04_Prompt_Check.md")]),
    "oe-writing": dict(fn=st_oe_ledger, primary="08_OE_Writing_Ledger.md", outputs=["08_OE_Writing_Ledger.md"],
                      inputs=["00_Assigments.md", "04_Prompt.txt"],
                      optional=["01_Grounding_Dossier.md", "01_Universe_Inject.sql", "03_Error_Async_Config.txt",
                                "02_Reference_Files_Manifest.md"],
                      upstream=[("prompt-check", "04_Prompt_Check.md")]),
    "oe-check": dict(fn=st_oe_check, primary="08_OE_Check.md", outputs=["08_OE_Check.md"],
                     inputs=["08_Oracle_Events.md", "08_OE_Writing_Ledger.md"], optional=[],
                     upstream=[("oe-writing", "08_OE_Writing_Ledger.md")], digest_extra=["08_Oracle_Events.md"]),
    "rubric-writing": dict(fn=st_rubric_plan, primary="09_Rubric_Writing_Plan.md", outputs=["09_Rubric_Writing_Plan.md"],
                        inputs=["04_Prompt.txt", "08_Oracle_Events.md", "08_OE_Writing_Ledger.md"], optional=[],
                        upstream=[("oe-writing", "08_OE_Writing_Ledger.md"), ("oe-check", "08_OE_Check.md")]),
    "rubric-check": dict(fn=st_rubric_check, primary="09_Rubric_Check.md", outputs=["09_Rubric_Check.md"],
                         inputs=["09_Rubrics.json", "09_Rubric_Writing_Plan.md"], optional=[],
                         upstream=[("rubric-writing", "09_Rubric_Writing_Plan.md")], digest_extra=["09_Rubrics.json"]),
    "allfail": dict(fn=st_allfail, primary="11_AF_Justification.md",
                    outputs=["11_AF_Justification.md"],
                    inputs=["10_Baseline_Verifier_Results.md", "09_Rubrics.json", "07_Baseline_Trajectories"],
                    optional=[], upstream=[("rubric-check", "09_Rubric_Check.md")]),
    "difficulty": dict(fn=st_difficulty, primary="12_Difficulty_Stats.txt", outputs=["12_Difficulty_Stats.txt"],
                       inputs=["12_difficulty_input.json", "10_Baseline_Verifier_Results.md", "09_Rubrics.json",
                               "07_Baseline_Trajectories"], digest_extra=["12_difficulty_input.json"],
                       optional=["11_AF_Justification.md"],
                       upstream=[("allfail", "11_AF_Justification.md?")]),
    "release": dict(fn=st_release, primary="13_Release_Gate.txt", outputs=[],
                    inputs=["00_Assigments.md", "04_Prompt.txt", "08_Oracle_Events.md", "09_Rubrics.json",
                            "01_Hardness_Manifest.json", "01_Universe_Inject.sql"], optional=[], upstream=[],
                    digest_extra=BUNDLE_FILES),
}


def run_stage(stage, task_dir, rerun="all", selftest=False):
    spec = STAGES[stage]
    ctx = Ctx(stage, task_dir, rerun, selftest)
    if not Path(task_dir).is_dir():
        ctx.add("structure.task_dir", False, f"{task_dir} is not a directory")
        return ctx
    # Validate the assignment and selected historical source before opening any base data.
    if not assignment_context(ctx):
        return ctx
    have_out = files_exist(ctx, spec["outputs"], "output")
    have_in = files_exist(ctx, spec["inputs"], "input")
    staleness(ctx, spec["outputs"], spec["inputs"] + spec["optional"])
    for up, f in spec["upstream"]:
        if f.endswith("?"):
            f = f[:-1]
            if not ctx.p(f).exists():
                continue
        chain(ctx, up, f)
    if have_out and have_in:
        try:
            spec["fn"](ctx)
            if ctx.v3:
                v3_checks(ctx)
        except Exception as e:  # noqa: BLE001 - a crash must block, never pass
            ctx.add("internal.error", False, f"{type(e).__name__}: {e}")
        own_paste(ctx, spec["primary"], spec["outputs"])
    return ctx


def verdict_of(ctx, allow_partial=False):
    if any(r["blocking"] for r in ctx.res):
        return "FAIL"
    if ctx.skipped and not allow_partial:
        return "PARTIAL"
    return "PASS"


def render(ctx, verdict):
    spec = STAGES[ctx.stage]
    digs = " · ".join(f"{f}#{dg}" for f, dg in certificate_digests(ctx).items()) or "no outputs"
    nb = sum(1 for r in ctx.res if r["blocking"])
    nw = sum(1 for r in ctx.res if r["status"] == "WARN")
    try:
        td = ctx.td.resolve().relative_to(WS)
    except ValueError:
        td = ctx.td
    out = [f"STAGE GATE {ctx.stage}: {verdict} — {td} · {digs} · blocking {nb} · warnings {nw} · checks {len(ctx.res)}"]
    for r in ctx.res:
        line = f"[{r['status']}] {r['id']}: {r['detail']}"
        if r["status"] in ("FAIL", "WARN") and r["locations"]:
            line += "  @ " + ", ".join(r["locations"][:6]) + (f" (+{len(r['locations']) - 6 + r['more']} more)"
                                                             if len(r["locations"]) > 6 or r["more"] else "")
        out.append(line)
    return "\n".join(out)


def paste_block(ctx, text):
    """Insert/replace this stage's gate block at the end of the primary artifact's Self-review section."""
    spec = STAGES[ctx.stage]
    p = ctx.p(spec["primary"])
    lines = p.read_text().splitlines() if p.exists() else [
        f"# {spec['primary']} — written by stage_gate.py {ctx.stage} --paste", "",
        "The certificate below records the bundle digest the task is submitted with; any later edit to a bundle "
        "file makes it stale."]
    # drop an older block for this stage
    keep, i = [], 0
    while i < len(lines):
        if lines[i].strip() == "```" and i + 1 < len(lines) and lines[i + 1].startswith(f"STAGE GATE {ctx.stage}: "):
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            i = j + 1
            continue
        keep.append(lines[i])
        i += 1
    doc_heads = [k for k, l in enumerate(keep) if re.match(r"^#{1,6}\s+.*self[- ]review", l, re.I) or
                 re.match(r"^\s*Self[- ]review\s*:", l, re.I)]
    block = ["", "```", *text.splitlines(), "```"]
    if doc_heads:
        h = doc_heads[-1]
        lvl = len(re.match(r"^(#*)", keep[h]).group(1)) or 7
        end = next((k for k in range(h + 1, len(keep)) if re.match(r"^(#{1,6})\s", keep[k]) and
                    len(re.match(r"^(#{1,6})", keep[k]).group(1)) <= lvl), len(keep))
        while end > h + 1 and not keep[end - 1].strip():
            end -= 1
        keep[end:end] = block
    else:
        keep += ["", "## Self-review"] + block
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(keep) + "\n")

# ------------------------------------------------------------------ self-test


def _prepare(dst: Path, src: Path, stage=None):
    """Copy the fixture as it stood when `stage` ran: slots later than the stage's primary are left out."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    if stage:
        cut = SLOT_ORDER.index(STAGES[stage]["primary"])
        keep = set(STAGES[stage]["outputs"]) | set(STAGES[stage]["inputs"])
        for name in SLOT_ORDER[cut + 1:]:
            p = slot_path(dst, name)
            if name not in keep and p.exists():
                shutil.rmtree(p) if p.is_dir() else p.unlink()
    base = 1_700_000_000.0
    for k, name in enumerate(SLOT_ORDER):
        p = slot_path(dst, name)
        if p.is_dir():
            for f in sorted(p.rglob("*")):
                os.utime(f, (base + k * 100, base + k * 100))
        elif p.exists():
            os.utime(p, (base + k * 100, base + k * 100))


def _apply(dst: Path, mut: dict):
    f = slot_path(dst, mut["file"]) if "file" in mut else None
    keep = f.stat().st_mtime if f is not None and f.exists() else None
    if "find" in mut:
        t = f.read_text()
        if mut["find"] not in t:
            raise AssertionError(f"mutation anchor not found in {mut['file']}: {mut['find'][:60]!r}")
        f.write_text(t.replace(mut["find"], mut["replace"], -1 if mut.get("all") else 1))
    if "append" in mut:
        f.write_text(f.read_text() + mut["append"])
    if "copy_from" in mut:
        shutil.copy(FIXTURES / "bad" / mut["copy_from"], f)
    if keep is not None and f.exists():
        os.utime(f, (keep, keep))   # content changes only; staleness is tested explicitly
    if "older_than" in mut:
        ref = mtime(slot_path(dst, mut["older_than"]))
        os.utime(f, (ref - 50, ref - 50))
    if "delete" in mut:
        p = slot_path(dst, mut["delete"])
        shutil.rmtree(p) if p.is_dir() else p.unlink()
    if "create" in mut:
        p = slot_path(dst, mut["create"])
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(mut.get("content", "x\n"))


def self_test(verbose=False) -> int:
    """Outside a sandbox, rerun inside one (tools/selftest_sandbox.py): persona_view, base_check and hg.py write caches,
    and the --rerun all cases start them as subprocesses. Inside, every scratch folder is a unique mkdtemp folder under
    SELFTEST_TMP, removed afterwards."""
    sb = fold_tool("selftest_sandbox")
    if not sb.in_sandbox(BUNDLE):
        return sb.run_isolated(["stage_gate.py", "--self-test"] + (["--verbose"] if verbose else []), source=BUNDLE)
    SELFTEST_TMP.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="stage_gate_selftest_", dir=SELFTEST_TMP))
    try:
        return _self_test_cases(tmp, verbose)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _self_test_cases(tmp: Path, verbose=False) -> int:
    good = FIXTURES / "good"
    cases = json.loads((FIXTURES / "bad" / "cases.json").read_text())["cases"]
    fails, n = [], 0
    g = tmp / "good"
    good_status, case_status = {}, {}
    for stage in STAGES:
        _prepare(g, good, stage)
        ctx = run_stage(stage, g, "lint", True)
        v = verdict_of(ctx, allow_partial=True)
        good_status[stage] = {r["id"]: r["status"] for r in ctx.res}
        n += 1
        if v != "PASS":
            fails.append(f"good/{stage}: {v} — " + "; ".join(f"{r['id']}: {r['detail'][:120]}" for r in ctx.res
                                                              if r["blocking"]))
        elif verbose:
            print(f"  ok  good/{stage} PASS ({len(ctx.res)} checks)")
    for case in cases:
        d = tmp / "bad"
        _prepare(d, good, case["stage"])
        for mut in case["mutate"]:
            _apply(d, mut)
        ctx = run_stage(case["stage"], d, "lint", True)
        v = verdict_of(ctx, allow_partial=True)
        failed = {r["id"] for r in ctx.res if r["blocking"]}
        status = case_status[case["name"]] = {r["id"]: r["status"] for r in ctx.res}
        expect = case.get("expect") or []
        missing = [e for e in expect if not any(f == e or f.startswith(e) for f in failed)]
        # expect_detail: substrings a blocking check's detail must hold (which family of a check blocked)
        details = " ".join(r["detail"] for r in ctx.res if r["blocking"])
        missing += [f"detail:{d}" for d in case.get("expect_detail", []) if d not in details]
        # expect_warn: the advisory check WARNs here and PASSes on the good stage (or a named baseline case), so
        # the mutation caused it; expect_pass: a control the check accepts
        base = case_status.get(case["baseline"], {}) if case.get("baseline") else good_status.get(case["stage"], {})
        missing += [f"warn:{e}" for e in case.get("expect_warn", []) if status.get(e) != "WARN"]
        missing += [f"baseline:{e} is {base.get(e)}" for e in case.get("expect_warn", []) if base.get(e) != "PASS"]
        missing += [f"pass:{e} is {status.get(e)}" for e in case.get("expect_pass", []) if status.get(e) != "PASS"]
        want = "FAIL" if expect else "PASS"
        n += 1
        if v != want or missing:
            fails.append(f"bad/{case['name']} ({case['stage']}): verdict {v} (want {want}), expected failing {expect} "
                         f"{case.get('expect_detail', '')}, WARN {case.get('expect_warn', [])}, PASS "
                         f"{case.get('expect_pass', [])}; got failing {sorted(failed)}; missing {missing}")
        elif verbose:
            print(f"  ok  bad/{case['name']} ({case['stage']}) " + (f"FAIL on {sorted(failed & set(expect)) or expect}"
                  if expect else f"PASS with WARN {case.get('expect_warn', [])} / PASS {case.get('expect_pass', [])}"))
    # re-run comparison: the good fixture pastes a hardness_gate PASS for a deliberately thin manifest; a full
    # re-run (--rerun all) must catch the false paste
    _prepare(g, good, "scenario")
    ctx = run_stage("scenario", g, "all", True)
    n += 1
    if not any(r["id"] == "tool.hardness_gate_design" and r["blocking"] for r in ctx.res):
        fails.append("rerun: a pasted hardness_gate PASS that the re-run contradicts was not caught")
    elif verbose:
        print("  ok  rerun/scenario: pasted hardness_gate --design PASS contradicted by the re-run → FAIL")
    # the same thin manifest must also fail the tier certificate that prompt-check re-runs (--profile extreme)
    _prepare(g, good, "prompt-check")
    ctx = run_stage("prompt-check", g, "all", True)
    n += 1
    if not any(r["id"] == "tier.hardness_rerun" and r["blocking"] for r in ctx.res):
        fails.append("rerun: prompt-check did not re-run hardness_gate for the tier's profile")
    elif verbose:
        print("  ok  rerun/prompt-check: tier hardness_gate --profile extreme re-run on the thin manifest → FAIL")
    # S0r: a revision intake that dispositions every proposed verdict, keeps exports bound and cites run steps passes
    _prepare(g, good, "scenario")
    _revise_fixture(g)
    ctx = run_stage("scenario", g, "lint", True)
    n += 1
    rev = [f"{r['id']}: {r['detail'][:100]}" for r in ctx.res if r["blocking"]]
    if rev or not any(r["id"] == "revise.verdict_dispositions" and r["status"] == "PASS" for r in ctx.res):
        fails.append(f"revise/scenario: a complete revision intake did not pass: {rev or 'revise checks did not run'}")
    elif verbose:
        print("  ok  revise/scenario: complete revision intake (dispositions, binding, run steps) → PASS")
    # S0r: an export that is not bound on evidence passes only when the intake marks it historical
    _prepare(g, good, "scenario")
    hist = {"runs": {"run-1": REVISE_VERDICTS["runs"]["run-1"],
                     "run-2": {"binding": {"verdict": "INSUFFICIENT", "bound_to": None, "basis": None,
                                           "evidence": {"discriminating_seen": 0, "shared_seen": 40}},
                               "rules": {"stale_count": {"verdict": "LEAKED", "flags": []}}}}}
    _revise_fixture(g, hist, REVISE_SECTION + "\nrun-2 is historical: a revision-1 export kept for its LEAKED reading; it "
                                              "certifies nothing about revision 2.\n")
    ctx = run_stage("scenario", g, "lint", True)
    n += 1
    rb = [r for r in ctx.res if r["id"] == "revise.revision_binding"]
    if not rb or rb[0]["blocking"]:
        fails.append(f"revise/scenario: an INSUFFICIENT export marked historical was not accepted: {rb}")
    elif verbose:
        print("  ok  revise/scenario: INSUFFICIENT export marked historical → revise.revision_binding PASS")
    # surface geometry is report-only: no slot mechanism at all (mechanism share 0 %) still passes surface.valid
    _prepare(g, good, "scenario")
    _apply(g, {"file": SURFACE, "find": ',\n   "mechanisms": ["stale_count"]}', "replace": "}"})
    ctx = run_stage("scenario", g, "lint", True)
    n += 1
    sv = [r for r in ctx.res if r["id"] == "surface.valid"]
    if not sv or sv[0]["blocking"] or "mechanism share 0%" not in sv[0]["detail"]:
        fails.append(f"surface/scenario: a surface with no mechanism (geometry only) blocked or was not reported: {sv}")
    elif verbose:
        print("  ok  surface/scenario: mechanism share 0 % (geometry) reported, surface.valid PASS (never gated)")
    # red team: a recorded fallback replaces a review that could not run; a silent skip never does (cases.json)
    _prepare(g, good, "scenario")
    _apply(g, {"delete": "01b_Redteam_Review.second.md"})
    _apply(g, {"file": "01_Scenario_Design.md", "append": "\nRED TEAM FALLBACK: REDTEAM_MODEL unavailable (HTTP 503); "
                                                         "a second author reviewed the shortcut audit by hand on 2026-10-25\n"})
    ctx = run_stage("scenario", g, "lint", True)
    n += 1
    red = [r for r in ctx.res if r["id"] == "tool.redteam_dual"]
    if not red or red[0]["blocking"]:
        fails.append("redteam/scenario: a recorded RED TEAM FALLBACK was not accepted")
    elif verbose:
        print("  ok  redteam/scenario: second review missing, explicit fallback recorded → tool.redteam_dual PASS")
    # digest invariance: pasting a gate block never changes the digest; an edit does
    t = "a\n\n## Self-review\nx\n"
    t2 = t + "\n```\nSTAGE GATE scenario: PASS — d · f#000000000000\n[PASS] x: y\n```\n"
    n += 1
    if digest_text(t) != digest_text(t2) or digest_text(t) == digest_text(t + "z\n"):
        fails.append("digest invariance")
    for f in fails:
        print("self-test FAIL - " + f)
    if not fails:
        nf = sum(1 for c in cases if c.get("expect"))
        print(f"self-test: ok ({n} cases: {len(STAGES)} good stages PASS, {nf} bad cases FAIL as expected, "
              f"{len(cases) - nf} WARN / control cases as expected, "
              "2 re-run contradictions caught, revision-intake, historical-export, surface-geometry and red-team "
              "fallback controls PASS, digest invariance)")
    return 1 if fails else 0


REVISE_BOUND = {"verdict": "BOUND", "bound_to": ["rev2"], "basis": "discriminating content",
                "evidence": {"discriminating_seen": 3, "shared_seen": 12}}
REVISE_VERDICTS = {"runs": {"run-1": {"binding": REVISE_BOUND,
                                      "rules": {"stale_count": {"verdict": "LANDED", "flags": []}}},
                            "run-2": {"binding": REVISE_BOUND,
                                      "rules": {"stale_count": {"verdict": "LEAKED", "flags": []}}}}}
REVISE_SECTION = ("\n## Revision intake (S0r)\n\nVerdicts consumed: run_forensics/rev2/node_verdicts.json (/create-hardening "
                  "MODE B, revision 2; both exports bound to revision 2).\n\n| Node | Runs | Proposed | Disposition | "
                  "Evidence |\n|---|---|---|---|---|\n| stale_count | run-1 LANDED, run-2 LEAKED | LANDED 1/2 | keep | "
                  "run-1 event 12 read ENG-2280 and still wrote the stale count |\n")


def _revise_fixture(d: Path, verdicts=None, section=None):
    """A MODE B report, its node verdicts and the design's revision-intake section (the S0r good case)."""
    _apply(d, {"create": "01a_Hardening_Report.md", "content": "# Hardening report\n\nMODE B (baseline), revision 2.\n"})
    _apply(d, {"create": "run_forensics/rev2/node_verdicts.json", "content": json.dumps(verdicts or REVISE_VERDICTS)})
    _apply(d, {"file": "01_Scenario_Design.md", "append": section or REVISE_SECTION})

# ------------------------------------------------------------------ main


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="stage_gate.py", description="mechanical stage gates (see module docstring)")
    ap.add_argument("stage", nargs="?", choices=sorted(STAGES))
    ap.add_argument("task_dir", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rerun", choices=("all", "lint"), default="all",
                    help="all (default) re-runs sql_lint, base_check, hardness_gate, difficulty_stats and persona_view; "
                         "lint skips base_check/hardness_gate and can only reach PARTIAL")
    ap.add_argument("--paste", action="store_true", help="on PASS, insert this output into the artifact's Self-review")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--artifact-hash", type=Path, help="print the normalized content hash used by V3 review records")
    a = ap.parse_args(argv)
    if a.artifact_hash:
        if not a.artifact_hash.exists():
            print(f"artifact missing: {a.artifact_hash}", file=sys.stderr)
            return 2
        print(file_digest(a.artifact_hash))
        return 0
    if a.self_test:
        return self_test(a.verbose)
    if a.list:
        for s, spec in STAGES.items():
            print(f"{s:16} writes {', '.join(spec['outputs'])}  ← {', '.join(spec['inputs'])}"
                  + (f"  · upstream {', '.join(u for u, _ in spec['upstream'])}" if spec["upstream"] else ""))
        return 0
    if not a.stage or not a.task_dir:
        ap.print_usage(sys.stderr)
        return 2
    ctx = run_stage(a.stage, Path(a.task_dir), a.rerun)
    v = verdict_of(ctx)
    text = render(ctx, v)
    if a.json:
        print(json.dumps({"stage": a.stage, "task_dir": a.task_dir, "verdict": v, "checks": ctx.res}, indent=2,
                         ensure_ascii=False))
    else:
        print(text)
    if a.paste:
        if v == "PASS":
            for r in ctx.res:
                if r["id"] == "handoff.pasted":
                    r.update(status="PASS", blocking=False, detail="pasted into the Self-review by --paste", locations=[])
            paste_block(ctx, render(ctx, v))
            print(f"\n(pasted into {STAGES[a.stage]['primary']} Self-review)", file=sys.stderr)
        else:
            print("\n(--paste ignored: only a PASS is pasted)", file=sys.stderr)
    return 0 if v == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
