#!/usr/bin/env python3
"""Build the copy-ready /goal a fresh session needs to analyse one task before /create-scenario.

    python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --task-dir <task folder> [--note TEXT]...
    python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --task-dir <task folder> --stdout-only
    python3 -B Task_Authoring/skills/create-goal/scripts/build_goal.py --list

Facts come from the task's assignment through tools/task_context.py run without --write, the other task folders, the
workspace `learnings` file and the Evals input store (`hg_store_input.py list`); every helper runs with bytecode off, so
nothing is written outside the selected task. The wording comes from ../goal_rules.json, whose cited phrases are checked
against their sources on every run. The only file written is <task>/Working_Files/00_Session_Goal.md (none with
--stdout-only).

Exit codes: 0 PASS · 2 assignment or source not usable · 3 a required line's evidence is missing · 4 the task already
has a scenario design · 5 the goal failed a self-check · 6 the task folder or output path is not usable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
BUNDLE = SKILL.parents[1]
WS = BUNDLE.parent
RULES_PATH = SKILL / "goal_rules.json"
DEFAULT_TASK = BUNDLE / "task_inputs"
TASK_CONTEXT = BUNDLE / "tools" / "task_context.py"
STORE_TOOL = WS / "Evals" / "tools" / "hg_store_input.py"
LEARNINGS = WS / "learnings"
OUTPUT = "00_Session_Goal.md"
ANALYSIS = "00_Pre_Scenario_Analysis.md"
DESIGN = "01_Scenario_Design.md"
TEMPLATE_SQL_BYTES = 1000          # the template's 01_Universe_Inject.sql is a 616-byte header
MAX_SIBLINGS = 3                   # same-universe designs named in the goal; the rest are counted
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
TOKEN = re.compile(r"\{([a-z][a-z0-9_]*)\}")
LEFTOVER = re.compile(r"\{[^{}\s]{1,40}\}")      # any brace token, so a field the TOKEN pattern misses still fails
PRONOUN = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
REPO_PATH = re.compile(r"\b(?:Task_Authoring|Evals|claude)/[^\s,;:()\"]*")

class Stop(Exception):
    def __init__(self, code, message, draft=None):
        super().__init__(message)
        self.code = code
        self.draft = draft


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def rel(path):
    path = Path(path)
    try:
        return path.relative_to(WS).as_posix()
    except ValueError:
        return str(path)


def sha12(data):
    return hashlib.sha256(data).hexdigest()[:12]


def word_count(text):
    """Whitespace-delimited tokens that contain a letter or digit, so '·', '<' and '≥' are not words."""
    return sum(1 for token in text.split() if re.search(r"[^\W_]", token))


PATH_KEYS = ("workspace", "task_abs", "task_arg", "task_rel", "analysis_rel", "default_rel")   # default_rel may not exist


def without_paths(text, values):
    """The text with each known path value (which may contain spaces) replaced by one token."""
    for value in sorted((values.get(k) for k in PATH_KEYS if values.get(k)), key=len, reverse=True):
        text = text.replace(value, " PATH ")
    return text


def join_and(items):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def helper_env():
    """Bytecode off (nothing written beside Evals/ or tools/ code); no inherited task folder (every call names one)."""
    env = {k: v for k, v in os.environ.items() if k != "TASK_AUTHORING_TASK_DIR"}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def run_py(script, *args):
    return subprocess.run([sys.executable, "-B", str(script), *args], cwd=WS, env=helper_env(),
                          capture_output=True, text=True, timeout=300)


# --------------------------------------------------------------------------------------------- task folders

def resolve_task_dir(arg):
    if arg is None:
        arg = os.environ.get("TASK_AUTHORING_TASK_DIR")
    if arg is None:
        folders = task_folders()
        if len(folders) != 1:
            raise Stop(6, "name the task folder with --task-dir (see --list)")
        arg = str(folders[0])
    given = Path(arg).expanduser()
    found = next((c for c in ([given] if given.is_absolute() else [Path.cwd() / given, WS / given]) if c.is_dir()), None)
    if found is None:
        raise Stop(6, f"task folder not found: {arg}")
    real = found.resolve()
    if real == BUNDLE.resolve() or not real.is_relative_to(BUNDLE.resolve()):
        raise Stop(6, f"{arg} is not a task folder inside Task_Authoring/")
    if not (real / "00_Assigments.md").is_file():
        raise Stop(6, f"{rel(real)} has no 00_Assigments.md")
    return real


def task_folders():
    return sorted(p.resolve() for p in BUNDLE.glob("task_inputs*") if p.is_dir() and (p / "00_Assigments.md").is_file())


def task_context(folder):
    """The validated context, recomputed from the assignment (task_context.py without --write writes nothing)."""
    proc = run_py(TASK_CONTEXT, "--task-dir", str(folder), "--require-source")
    if proc.returncode != 0:
        lines = [line for line in proc.stderr.splitlines() if line.strip()]
        raise Stop(2, lines[-1] if lines else f"task_context.py exited {proc.returncode}")
    return json.loads(proc.stdout)


def sibling_context(folder):
    try:
        return task_context(folder), "recomputed"
    except (Stop, ValueError, subprocess.TimeoutExpired):
        try:
            saved = json.loads((folder / "Working_Files" / "00_Task_Context.json").read_text())
        except (OSError, ValueError):
            return None, "unreadable"
        usable = isinstance(saved, dict) and saved.get("persona_name") and saved.get("competency") and \
            isinstance(saved.get("universe"), dict) and saved["universe"].get("key")
        return (saved, "saved record") if usable else (None, "unreadable")


def design_slug(folder):
    try:
        with (folder / "Working_Files" / DESIGN).open(encoding="utf-8", errors="replace") as handle:
            first = handle.readline()
    except OSError:
        return None
    match = re.match(r"#\s*Scenario Design\s*[—-]\s*(\S+)", first)
    return match.group(1) if match else None


def stage_status(folder):
    have = []
    if (folder / "Working_Files" / ANALYSIS).is_file():
        have.append("a pre-scenario analysis")
    if (folder / "Working_Files" / DESIGN).is_file():
        have.append("a scenario design")
    sql = folder / "01_Universe_Inject.sql"
    if sql.is_file() and sql.stat().st_size > TEMPLATE_SQL_BYTES:
        have.append("injection SQL")
    if (folder / "Working_Files" / "01a_Hardening_Report.md").is_file():
        have.append("a hardening report")
    if (folder / "06_PreCheck_Trajectory" / "trajectory.json").is_file():
        have.append("a pre-check trajectory")
    runs = list((folder / "07_Baseline_Trajectories").glob("trajectory-run-*.json"))
    if runs:
        have.append(f"{len(runs)} baseline trajectories")
    return have


# --------------------------------------------------------------------------------------------- other inputs

def read_store():
    """The Evals input store as `hg_store_input.py list` reports it (read-only), or None."""
    try:
        proc = run_py(STORE_TOOL, "list")
        return json.loads(proc.stdout) if proc.returncode == 0 else None
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None


def store_holds(store, ctx, assignment_sha):
    """(text for the goal's store line or None, short state for the report). A saved file counts only when `list`
    reports its integrity OK: the index keeps the recorded sha256 after the file changes or disappears."""
    if not store:
        return "its state could not be read", "unknown (hg_store_input.py list failed)"
    intake = store.get("universe_intake") or {}
    selected = intake.get("state") == "SELECTED" and bool(intake.get("label"))
    label = intake["label"] if selected else "no task date selected"
    date_note = f"; its task date is {label}" if selected else ""
    entry = (store.get("inputs") or {}).get("task-details") or {}
    files = entry.get("files") or []
    if entry.get("state") != "saved" or not files:
        # an earlier bundle's file outside the index (its sha256 is computed fresh by `list`)
        legacy = (store.get("unindexed_local_inputs") or {}).get("task-details")
        if legacy:
            whose = "this task's" if legacy.get("sha256") == assignment_sha else "another task's"
            return f"it holds {whose} details, not indexed" + date_note, f"{whose} details unindexed, {label}"
        return "it holds no task details" + date_note, f"no task details, {label}"
    if any(f.get("integrity") != "OK" for f in files):
        return "its saved task details are changed or missing" + date_note, f"damaged task details, {label}"
    same_task = len(files) == 1 and files[0].get("sha256") == assignment_sha
    same_universe = selected and intake.get("key") == ctx["universe"]["key"]
    if same_task and same_universe:
        return None, f"this task, {label}"
    if same_task:
        return (f"its task date is {label}" if selected else "it has no task date selected"), \
            f"this task's inputs, {label}"
    return "it holds another task" + (f" dated {label}" if selected else ""), f"another task's inputs, {label}"


def learnings_max():
    try:
        text = LEARNINGS.read_text(encoding="utf-8")
    except OSError:
        return None
    sections = [int(n) for n in re.findall(r"^## (\d+)\. ", text, re.M)]
    return max(sections) if sections else None


def describe_default(siblings):
    """What sits in the tools' default task folder, for the goal's TASK_AUTHORING_TASK_DIR line."""
    default = next((s for s in siblings if s["folder"] == DEFAULT_TASK.resolve()), None)
    if default and default["first"]:
        return f"{default['first']}'s task"
    return "another task" if DEFAULT_TASK.is_dir() else "not present"


def pick_analysis(ctx, siblings):
    best = None
    for sib in siblings:
        path = sib["folder"] / "Working_Files" / ANALYSIS
        if not sib["ctx"] or not path.is_file():
            continue
        rank = 2 * (sib["universe"] == ctx["universe"]["key"]) + (sib["competency"] == ctx["competency"])
        if best is None or rank > best[0]:
            best = (rank, path, sib["first"])
    return (best[1], best[2]) if best else (None, None)


# --------------------------------------------------------------------------------------------- rules and text

def load_rules():
    try:
        return json.loads(RULES_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise Stop(3, f"cannot read {rel(RULES_PATH)}: {exc}") from exc


_SOURCES = {}


def missing_evidence(entry):
    missing = []
    for item in entry.get("evidence", []):
        path = item["path"]
        if path not in _SOURCES:
            try:
                _SOURCES[path] = norm((WS / path).read_text(encoding="utf-8", errors="replace"))
            except OSError:
                _SOURCES[path] = None
        if _SOURCES[path] is None or norm(item["contains"]) not in _SOURCES[path]:
            missing.append(f"{path}: {item['contains'][:80]!r}")
    return missing


def lookup(table, label, what):
    for key, entry in table.items():
        if label.casefold() in {x.casefold() for x in (key, *entry.get("labels", []))}:
            return key, entry
    raise Stop(3, f"goal_rules.json has no {what} entry for {label!r}; add it with its evidence")


def fill(template, values):
    def sub(match):
        if match.group(1) not in values:
            raise Stop(5, f"template field {{{match.group(1)}}} has no value")
        return str(values[match.group(1)])
    return TOKEN.sub(sub, template)


def first_name(ctx):
    return ctx["persona_name"].split()[0]


def today_text(universe):
    day = date.fromisoformat(universe["persona_today"])
    return f"{universe['persona_today_weekday']} {day.day} {MONTHS[day.month - 1]}"


def compose(ctx, rules, *, task_dir, siblings, store_line, analysis, learnings_n, default_owner, analysis_exists, notes):
    """The goal text plus warnings. Pure apart from reading the sources that goal_rules.json cites."""
    lines, warnings, used = rules["lines"], [], []

    def line(name, values):
        entry = lines[name]
        missing = missing_evidence(entry)
        if missing and entry.get("optional"):
            warnings.append(f"optional line {name!r} dropped; evidence missing: " + "; ".join(missing))
            return ""
        if missing:
            raise Stop(3, f"line {name!r}: evidence missing: " + "; ".join(missing))
        used.append(name)
        return fill(entry["text"], values)

    skill_key, skill = lookup(rules["skills"], ctx["task_skill"], "task skill")
    category, function = lookup(rules["functions"], ctx["business_function"], "business function")
    competency_key, competency = lookup(rules["competencies"], ctx["competency"], "competency")
    for name, entry in ((f"skill {skill_key}", skill), (f"function {category}", function),
                        (f"competency {competency_key}", competency)):
        missing = missing_evidence(entry)
        if missing:
            raise Stop(3, f"{name}: evidence missing: " + "; ".join(missing))

    first = first_name(ctx)
    extreme = ctx["horizon"] == "Long Horizon"          # GEN_EXECUTION §3a: Long Horizon → extreme profile
    cap = round(float(ctx["difficulty_cap"]) * 100)
    # only designed siblings have a storyline to stay distinct from; same competency first
    same_universe = sorted((s for s in siblings if s["ctx"] and s["slug"] and s["universe"] == ctx["universe"]["key"]),
                           key=lambda s: s["competency"] != ctx["competency"])
    named = same_universe[:MAX_SIBLINGS]
    sibling_items = [f"{s['first']}'s ({s['slug']})" for s in named]
    if len(same_universe) > len(named):
        sibling_items.append(f"{len(same_universe) - len(named)} more task folders")
    values = {
        "task_abs": str(task_dir), "workspace": str(WS), "task_rel": rel(task_dir),
        "task_arg": shlex.quote(rel(task_dir)), "named_siblings": [rel(s["folder"]) for s in named],
        "default_rel": rel(DEFAULT_TASK),
        "persona": ctx["persona_name"], "role": ctx["persona_role"], "first": first,
        "function": ctx["business_function"], "competency": ctx["competency"], "skill": ctx["task_skill"],
        "horizon": ctx["horizon"], "mode": ctx["difficulty_mode"].capitalize(), "universe": ctx["universe"]["label"],
        "today": today_text(ctx["universe"]), "cap": cap, "target": cap - 8,
        "calls": "≥ 100" if extreme else "50–100", "channels": 4 if ctx["difficulty_mode"] == "hard" else 3,
        "default_owner": default_owner, "store_holds": store_line or "",
        "category": category, "meaning": function["meaning"], "focus": competency["focus"],
        "verb": "update" if analysis_exists else "write",
        "learnings_max": learnings_n or "",
        "analysis_rel": rel(analysis[0]) if analysis[0] else "", "analysis_owner": analysis[1] or "",
        "siblings": join_and(sibling_items) if sibling_items else "",
    }
    values["skill_rule"] = fill(skill["text"], values)
    values["v2_traps"] = line("v2_traps", values)            # the hardness guide, references/Docs/13_Hardness_v2_Opus55.md
    values["v2_checks"] = line("v2_checks", values)
    values["distinct"] = line("distinct", values) if same_universe else ""
    values["volume"] = line("volume", values) if extreme else ""
    reads = ([line("read_learnings", values)] if learnings_n else []) + \
            ([line("read_analysis", values)] if analysis[0] else []) + \
            ["Task_Authoring/references/Scenario_Atlas.md", "Task_Authoring/playbooks/01_Scenario_Design.md"]
    values["read_items"] = join_and(reads)
    if not learnings_n:
        warnings.append("learnings not found at the workspace root; the goal does not cite it")

    setup = [line("start", values)]
    if task_dir != DEFAULT_TASK.resolve():
        setup.append(line("default_dir", values))
    if store_line:
        setup.append(line("store", values))
    setup.append(line("boundary", values))
    rule_names = ("rule_ugt", "rule_fit", "rule_injection", "rule_hardness", "rule_spread", "rule_writes",
                  "rule_align")
    blocks = [
        line("header", values),
        line("assignment", values) + " " + line("gate", values),
        " ".join(setup),
        line("read", values),
        "\n".join([line("rules_intro", values)] + [line(name, values) for name in rule_names]),
        line("deliverable", values),
    ]
    generated = "\n\n".join(blocks)
    note_lines = [lines["note"]["text"].replace("{note}", note) for note in notes]
    goal = generated + ("\n\n" + "\n".join(note_lines) if note_lines else "")
    return goal, generated, values, warnings, used


def self_check(goal, generated, values, rules, *, task_dir, siblings, store_line, extreme):
    problems, warnings = [], []
    # a path is one word; --note text counts only towards the warning
    words, total = word_count(without_paths(generated, values)), word_count(without_paths(goal, values))
    limits = rules.get("limits", {})
    ceiling, mark = limits.get("max_words", 560), limits.get("warn_words", 520)
    if words > ceiling:
        problems.append(f"{words} generated words, over the {ceiling}-word ceiling")
    elif total > mark:
        warnings.append(f"{total} words{' with the notes' if total != words else ''}, above the {mark}-word mark")
    leftover = LEFTOVER.findall(generated)       # notes are inserted verbatim and may contain braces
    if leftover:
        problems.append("unresolved template fields: " + ", ".join(sorted(set(leftover))))
    pronouns = PRONOUN.findall(generated)
    if pronouns:
        problems.append("pronoun in the generated text (use the name): " + ", ".join(sorted(set(pronouns))))
    scan = without_paths(generated, values)                      # known paths may contain spaces: checked whole
    for key in ("task_rel", "analysis_rel"):
        if values.get(key) and not (WS / values[key]).exists():
            problems.append(f"input path in the goal does not exist: {values[key]}")
    for path in sorted(set(REPO_PATH.findall(scan))):
        if not (WS / path.rstrip(".")).exists():
            problems.append(f"input path in the goal does not exist: {path}")
    if "learnings (§1–" in generated and not LEARNINGS.is_file():
        problems.append("the goal cites learnings, which is missing")
    if not (task_dir / "Working_Files" / ANALYSIS).resolve().is_relative_to(task_dir):
        problems.append("the analysis output would resolve outside the task folder")
    for label, present, expected in (
            ("TASK_AUTHORING_TASK_DIR line", "TASK_AUTHORING_TASK_DIR" in generated, task_dir != DEFAULT_TASK.resolve()),
            ("Evals store line", "Evals input store" in generated, bool(store_line)),
            ("volume decision", "volume exception" in generated, extreme)):
        if present != expected:
            problems.append(f"{label} {'present' if present else 'missing'} but expected {'yes' if expected else 'no'}")
    if any(s["folder"] == task_dir for s in siblings):
        problems.append("the task folder is listed as its own sibling")
    return problems, warnings


# --------------------------------------------------------------------------------------------- output

def write_output(task_dir, content):
    wf = task_dir / "Working_Files"
    out = wf / OUTPUT
    try:
        if wf.is_symlink():
            raise Stop(6, f"{rel(wf)} is a symlink; refusing to write through it")
        wf.mkdir(exist_ok=True)
        if wf.resolve().parent != task_dir:
            raise Stop(6, f"{rel(wf)} resolves outside the task folder")
        if out.is_symlink() or (out.exists() and not out.is_file()):
            raise Stop(6, f"{rel(out)} is a symlink or not a file; refusing to replace it")
        fd, temp = tempfile.mkstemp(dir=wf, prefix=OUTPUT + ".", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                os.fchmod(handle.fileno(), 0o644)
                handle.write(content)
            os.replace(temp, out)
        except BaseException:
            if os.path.lexists(temp):
                os.unlink(temp)
            raise
    except OSError as exc:
        raise Stop(6, f"cannot write {rel(out)}: {exc.strerror or exc}") from exc
    return out


def render_file(goal, ctx, words):
    script, rules = sha12(Path(__file__).read_bytes()), sha12(RULES_PATH.read_bytes())
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    title = " · ".join((ctx["persona_name"], ctx["business_function"], ctx["competency"], ctx["task_skill"],
                        ctx["horizon"], ctx["difficulty_mode"], ctx["universe"]["label"]))
    fence = "`" * max(3, 1 + max((len(run) for run in re.findall(r"`+", goal)), default=0))   # notes may hold fences
    return (f"# Session goal — {title}\n\n"
            f"Generated {stamp} by `/create-goal` (build_goal.py {script}, goal_rules.json {rules}, context "
            f"{str(ctx['context_hash'])[:12]}, {words} words). Paste the block into a fresh session opened at the "
            "workspace root, before `/create-scenario`. Regenerate after any change to the assignment, the other task "
            "folders or `learnings`. No stage gate reads this file.\n\n"
            f"{fence}text\n{goal}\n{fence}\n")


def cmd_list():
    for folder in task_folders():
        try:
            ctx = task_context(folder)
        except Stop as exc:
            print(f"{rel(folder)} · context not usable: {exc}")
            continue
        status = stage_status(folder) or ["not started"]
        goal = " · goal written" if (folder / "Working_Files" / OUTPUT).is_file() else ""
        print(" · ".join((rel(folder), ctx["persona_name"], ctx["business_function"], ctx["competency"],
                          ctx["task_skill"], ctx["horizon"], ctx["difficulty_mode"], ctx["universe"]["label"],
                          ", ".join(status))) + goal)
    return 0


# --------------------------------------------------------------------------------------------- main

def check_working_files(task_dir):
    """Working_Files/ must be absent or a real folder inside the task: the goal sends the new session there."""
    wf = task_dir / "Working_Files"
    if wf.is_symlink() or (wf.exists() and (not wf.is_dir() or wf.resolve().parent != task_dir)):
        raise Stop(6, f"{rel(wf)} is a symlink or not a folder inside the task; refusing to send work there")


def other_work(task_dir):
    """Working_Files entries no fresh task has (research notes, drafts): a sign another session is working here."""
    wf = task_dir / "Working_Files"
    expected = {"README.md", "00_Task_Context.json", OUTPUT, ANALYSIS}
    return sorted(p.name + ("/" if p.is_dir() else "") for p in wf.iterdir() if p.name not in expected) \
        if wf.is_dir() else []


def build(task_dir, notes, stdout_only):
    check_working_files(task_dir)
    have = stage_status(task_dir)
    if "a scenario design" in have:
        raise Stop(4, f"{rel(task_dir)} already has {join_and(have)}. /create-goal starts a task before "
                      "/create-scenario. Continue with the next stage (Task_Authoring/README.md, Commands); if an "
                      "Opus 5.5 run already failed the task, the route is /create-hardening (MODE B) then "
                      "/create-scenario --revise.")
    ctx = task_context(task_dir)
    rules = load_rules()
    siblings = []
    for folder in task_folders():
        if folder == task_dir:
            continue
        sib, how = sibling_context(folder)
        siblings.append({"folder": folder, "ctx": sib, "how": how, "slug": design_slug(folder),
                         "first": first_name(sib) if sib else None,
                         "universe": (sib or {}).get("universe", {}).get("key"),
                         "competency": (sib or {}).get("competency")})
    assignment_sha = hashlib.sha256((task_dir / "00_Assigments.md").read_bytes()).hexdigest()
    store_line, store_state = store_holds(read_store(), ctx, assignment_sha)
    analysis = pick_analysis(ctx, siblings)
    if any(not n.strip() for n in notes):                       # notes are kept exactly as given
        raise Stop(6, "--note is empty")
    goal, generated, values, warnings, used = compose(
        ctx, rules, task_dir=task_dir, siblings=siblings, store_line=store_line, analysis=analysis,
        learnings_n=learnings_max(), default_owner=describe_default(siblings),
        analysis_exists=(task_dir / "Working_Files" / ANALYSIS).is_file(), notes=notes)
    problems, more = self_check(goal, generated, values, rules, task_dir=task_dir, siblings=siblings,
                                store_line=store_line, extreme=ctx["horizon"] == "Long Horizon")
    warnings += more
    if problems:
        raise Stop(5, "self-check failed: " + " | ".join(problems), draft=goal)
    busy = other_work(task_dir)
    if busy:
        warnings.append("Working_Files already holds " + ", ".join(busy[:3])
                        + (f" (+{len(busy) - 3} more)" if len(busy) > 3 else "")
                        + ": another session may be working in this folder"
                        + ("" if stdout_only else "; the goal file was still written (use --stdout-only to avoid it)"))
    words, generated_words = word_count(without_paths(goal, values)), word_count(without_paths(generated, values))
    saved = task_dir / "Working_Files" / "00_Task_Context.json"
    try:
        saved_state = "current" if json.loads(saved.read_text()).get("context_hash") == ctx["context_hash"] else "stale"
    except (OSError, ValueError):
        saved_state = "missing"
    out = None if stdout_only else write_output(task_dir, render_file(goal, ctx, words))
    facts = {
        "task": rel(task_dir), "default_folder": task_dir == DEFAULT_TASK.resolve(),
        "assignment": {k: ctx[k] for k in ("persona_name", "persona_role", "business_function", "competency",
                                           "task_skill", "horizon", "difficulty_mode")},
        "universe": ctx["universe"]["label"], "today": values["today"],
        "context_hash": str(ctx["context_hash"])[:12], "saved_context": saved_state,
        "store": store_state,
        "siblings": [{"folder": rel(s["folder"]), "persona": (s["ctx"] or {}).get("persona_name"),
                      "universe": s["universe"], "design": s["slug"], "context": s["how"],
                      "named_in_goal": rel(s["folder"]) in values["named_siblings"]} for s in siblings],
        "analysis_cited": rel(analysis[0]) if analysis[0] else None, "other_work_in_folder": busy,
        "learnings_sections": values["learnings_max"] or None,
        "notes": notes, "words": words, "generated_words": generated_words, "lines_used": used,
        "output": rel(out) if out else None,
    }
    return goal, facts, warnings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--task-dir", help="the task folder (default: TASK_AUTHORING_TASK_DIR, or the only task folder)")
    ap.add_argument("--note", action="append", default=[],
                    help="a standing decision appended verbatim as 'Also: ...' (repeatable)")
    ap.add_argument("--stdout-only", action="store_true", help="print the goal and write nothing")
    ap.add_argument("--list", action="store_true", help="list the task folders and their stage")
    args = ap.parse_args(argv)
    try:
        if args.list:
            return cmd_list()
        goal, facts, warnings = build(resolve_task_dir(args.task_dir), args.note, args.stdout_only)
    except Stop as stop:
        if stop.draft:
            print("DRAFT (failed the self-check; not for use)\n" + stop.draft + "\n", file=sys.stderr)
        print(f"CREATE-GOAL: STOP ({stop.code}) — {stop}", file=sys.stderr)
        return stop.code
    print(goal)
    print()
    print("FACTS " + json.dumps(facts, ensure_ascii=False))
    for warning in warnings:
        print("WARN " + warning)
    print(f"CREATE-GOAL: PASS · {facts['output'] or 'stdout only'} · {facts['words']} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
