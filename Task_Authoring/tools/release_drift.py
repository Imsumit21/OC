#!/usr/bin/env python3
"""release_drift.py - tell the author when a platform report cites rules the local bundle does not have (plan WS0).

The platform's current Evals/ release cannot be obtained, so the platform review reports are the only record of the
rules it applies. This tool reads those reports and compares what each one cites with
  (a) the local bundle (Evals/ and claude/), and
  (b) the register references/platform_rule_delta.json, which lists what earlier reports cited.

What it reads from a report
  release fingerprint   the "Eval release SHA-256: <hex>" line
  spec hashes           an Evals/ file cited with a SHA-256, e.g. `Evals/1A_Hardness_Eval.md` (SHA-256 `576f1870…e627`)
                        or "Eval 1 SHA-256 `a53a4412…`", or a header list such as "WORKFLOW `ee4cd8e1…`;
                        scoring.json `c14873e6…`". A label is resolved through the local file names and the
                        register's spec_aliases (label -> file), which a reviewer may extend
  review date           "Actual review time | 2026-11-08", "Actual review date | ...", "review date 2026-11-05"
  cited names           versioned ids (count-bundle-v1), Evals/ paths, `hg_x.py sub-command`, and backticked
                        letter-only names on a line that mentions a lint or a helper run (check names)
A cited name is known when the local bundle contains it, the register lists it, or (check names only) it is a table
or column of the universe schema.

Commands
  scan PATH...      read-only. Print what is new. Exit 1 when anything is new, 0 otherwise. Backticked check names
                    are listed but change the exit code only with --strict (they are lexical candidates).
  record PATH...    scan, then add the new items to the register with status "unreviewed".
  rebuild PATH...   rebuild the register's mechanical parts (reports, releases, spec hashes, names) from the given
                    folders with status "baseline". Curated rules and statuses set by a reviewer are kept.
  status            summarise the register: releases by date, spec hashes per file, items awaiting review.
PATH is a report file, a folder of reports, or a folder above them: every eval_reports/, plateform_reports/ and
platform_reports/ folder beneath it (singular spellings too) is read. A file that contains the local bundle fingerprint is a local review
output and is skipped.

Statuses: baseline (present when the register was built), unreviewed (added by record), rule:<id> (belongs to a
curated rule; set automatically from the rule's id and aliases), not_a_rule (set by a reviewer, kept).

Limits: a rule the platform never cited by name is invisible here. Stdlib only. Writes only the register (record,
rebuild); never writes Evals/ or claude/.

Usage:
  python3 -B Task_Authoring/tools/release_drift.py scan Task_Authoring/task_inputsS2
  python3 -B Task_Authoring/tools/release_drift.py record Task_Authoring/task_inputsS2/plateform_reports/x_3_rubric.md
  python3 -B Task_Authoring/tools/release_drift.py rebuild Task_Authoring/support/completed_tasks Task_Authoring
  python3 -B Task_Authoring/tools/release_drift.py status
  python3 -B Task_Authoring/tools/release_drift.py --selftest
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
REPO = BUNDLE.parent
REGISTER = BUNDLE / "references" / "platform_rule_delta.json"
SCHEMA = "platform-rule-delta-v1"
REPORT_DIRS = ("eval_reports", "plateform_reports", "platform_reports", "plateform_report", "platform_report")
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt"}
SKIP_PARTS = {".cache", "__pycache__", "task_inputs", "universes"}   # input store, caches and universe indexes
MAX_LOCAL_BYTES = 5_000_000

RX_RELEASE = re.compile(r"Eval release SHA-256:\s*`?([0-9a-f]{8,64})")
RX_DATE = re.compile(r"(?i)\breview(?:ed| time| date)\b[^0-9\n]{0,12}(20\d\d-\d\d-\d\d)")
RX_SPEC = re.compile(r"`?(Evals/[\w./-]+\.(?:md|json|py))`?[^`\n|]{0,40}?(?i:sha-?256)[^`\n|]{0,12}?[`\s:]"
                     r"([0-9a-f]{8,64})(?:(?:…|\.\.\.)([0-9a-f]{2,64}))?")
RX_SPEC_ALIAS = re.compile(r"\bEval (0|1A|1B|1|2|3)\b[^`\n|]{0,20}?(?i:sha-?256)[^`\n|]{0,12}?[`\s:]"
                           r"([0-9a-f]{8,64})(?:(?:…|\.\.\.)([0-9a-f]{2,64}))?")
# "<label> [SHA-256] `<hash>`": the label is an Eval number, a path, a file name or a known bare name.
RX_HASH_CITE = re.compile(r"(?P<label>Eval (?:0|1A|1B|1|2|3)|`?[\w./-]+`?)\s*\(?(?:(?i:sha-?256)\)?[\s:]*)?"
                          r"`(?P<h>[0-9a-f]{8,64})(?:(?:…|\.\.\.)(?P<s>[0-9a-f]{2,64})?)?`")
DEFAULT_SPEC_ALIASES = {"roster": "Evals/references/persona/roster.json", "acl": "Evals/references/persona/acl.md",
                        "known_base_issues": "Evals/references/known_base_issues.md",
                        "known_base_issues.md": "Evals/references/known_base_issues.md"}
SPEC_ALIAS = {"0": "Evals/0_Injection_Quality_Eval.md", "1": "Evals/1_Prompt_Eval.md",
              "1A": "Evals/1A_Hardness_Eval.md", "1B": "Evals/1B_Haiku_Prediction_Eval.md",
              "2": "Evals/2_Oracle_Events_Eval.md", "3": "Evals/3_Rubrics_Eval.md"}
RX_VERSIONED = re.compile(r"(?<![\w-])[a-z][a-z0-9]*(?:-[a-z0-9]+)*-v\d+(?![\w-])")
RX_PATH = re.compile(r"Evals/[\w./-]+\.(?:md|json|py|txt)")
RX_TOOL_CMD = re.compile(r"`(hg_[a-z0-9_]+\.py)(?: ([a-z][a-z0-9_-]+))?[^`\n]*`")
RX_CHECK = re.compile(r"`([a-z]+(?:_[a-z]+)+)`")          # letters only: record ids carry digits
# A backticked name is a check-name candidate only on a line that talks about a lint or a helper run.
RX_RULE_LINE = re.compile(r"(?i)\blint\b|hg_[a-z0-9_]+\.py|\bflagged\b|\bhits?\b|\bcode checks?\b")
RX_DATED_ID = re.compile(r"\d{4}-\d{2}-\d{2}")            # hg4-2026-08-31-v37 is a universe label, not a rule
RX_WORD = re.compile(r"[A-Za-z][A-Za-z0-9_]+")
RX_KIND_NAME = re.compile(r"(?i)(?:^|[_\s/])(0_injection|1_prompt|1a_hardness|1b_hardness|1b_haiku|2_oe|3_rubric)")
RX_KIND_SPEC = re.compile(r"Evals/(0_Injection_Quality_Eval|1_Prompt_Eval|1A_Hardness_Eval|1B_Haiku_Prediction_Eval|"
                          r"2_Oracle_Events_Eval|3_Rubrics_Eval)\.md")
KIND = {"0_injection": "/injection", "1_prompt": "/prompt", "1a_hardness": "/hardness", "1b_hardness": "/hardness",
        "1b_haiku": "/hardness", "2_oe": "/oe", "3_rubric": "/rubric",
        "0_Injection_Quality_Eval": "/injection", "1_Prompt_Eval": "/prompt", "1A_Hardness_Eval": "/hardness",
        "1B_Haiku_Prediction_Eval": "/hardness", "2_Oracle_Events_Eval": "/oe", "3_Rubrics_Eval": "/rubric"}
NAME_KINDS = ("versioned_id", "evals_path", "tool_command", "check_name")
FINDING_LABEL = {"release": "NEW RELEASE", "spec_hash": "NEW SPEC HASH", "versioned_id": "UNKNOWN RULE ID",
                 "evals_path": "UNKNOWN FILE", "tool_command": "UNKNOWN TOOL COMMAND",
                 "check_name": "POSSIBLE CHECK NAME"}


# ---------------------------------------------------------------- local bundle

class Local:
    """What the local Evals/ and claude/ copies contain."""

    def __init__(self, repo, schema_file=None, spec_aliases=None):
        self.repo = Path(repo)
        self.words, self.versioned, self._sha, self._text = set(), set(), {}, {}
        self.aliases = dict(DEFAULT_SPEC_ALIASES, **(spec_aliases or {}))
        names = {}
        for root in (self.repo / "Evals", self.repo / "claude"):
            if not root.is_dir():
                continue
            for f in sorted(root.rglob("*")):
                if (not f.is_file() or f.suffix not in TEXT_SUFFIXES
                        or SKIP_PARTS & set(f.relative_to(root).parts) or f.stat().st_size > MAX_LOCAL_BYTES):
                    continue
                text = f.read_text(errors="ignore")
                if root.name == "Evals":
                    rel = f.relative_to(self.repo).as_posix()
                    names.setdefault(f.name, set()).add(rel)
                self.words.update(RX_WORD.findall(text))
                self.versioned.update(RX_VERSIONED.findall(text))
        self.spec_names = {k: next(iter(v)) for k, v in names.items() if len(v) == 1}   # unambiguous names only
        for name, rel in list(self.spec_names.items()):     # WORKFLOW, ENVIRONMENT, SEARCH: top-level specs by stem
            if rel == f"Evals/{name}" and name.endswith(".md") and name[:-3].isupper():
                self.spec_names[name[:-3]] = rel
        self.schema_words = set()
        if schema_file and Path(schema_file).is_file():
            self.schema_words = set(RX_WORD.findall(Path(schema_file).read_text(errors="ignore")))

    def sha(self, rel):
        if rel not in self._sha:
            p = self.repo / rel
            self._sha[rel] = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
        return self._sha[rel]

    def matches(self, rel, prefix, suffix):
        """True/False when the local file exists, None when it does not."""
        digest = self.sha(rel)
        if digest is None:
            return None
        # The prefix decides. Reports abbreviate by hand and their suffixes are not reliable: the same SEARCH.md
        # hash is printed as cab83c61…a5cbc in one report and cab83c61…c9d3a45c in another.
        return digest.startswith(prefix)

    def resolve_spec(self, label):
        """The spec file a cited label stands for, or None when the label is not a known spec name."""
        label = label.strip("`")
        if label.startswith("Eval ") and label[5:] in SPEC_ALIAS:
            return SPEC_ALIAS[label[5:]]
        if label in self.aliases:
            return self.aliases[label]
        if label.startswith("Evals/"):
            return label if label.endswith((".md", ".json", ".py")) else None
        return self.spec_names.get(label)

    def has_tool_command(self, tool, sub):
        rel = f"Evals/tools/{tool}"
        p = self.repo / rel
        if not p.is_file():
            return False
        if not sub:
            return True
        if rel not in self._text:
            self._text[rel] = p.read_text(errors="ignore")
        # A sub-command is a quoted word of its own in the tool's source; 'fixcheck/x.json' is a path, not one.
        return re.search(r"""['"]""" + re.escape(sub) + r"""['"]""", self._text[rel]) is not None

    def knows(self, kind, name):
        if kind == "versioned_id":
            return name in self.versioned
        if kind == "evals_path":
            return (self.repo / name).exists()
        if kind == "tool_command":
            tool, _, sub = name.partition(" ")
            return self.has_tool_command(tool, sub)
        return name in self.words or name in self.schema_words


# ---------------------------------------------------------------- reading reports

def report_files(paths):
    """Report files under the given paths, in a stable order, without duplicates."""
    out, seen = [], set()
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            found = [p]
        elif p.is_dir() and p.name in REPORT_DIRS:
            found = sorted(f for f in p.iterdir() if f.is_file())
        elif p.is_dir():
            found = sorted(f for d in sorted(p.rglob("*")) if d.is_dir() and d.name in REPORT_DIRS
                           for f in d.iterdir() if f.is_file())
            if not found:                                   # a plain folder: only files named like a report
                found = sorted(f for f in p.iterdir() if f.is_file() and RX_KIND_NAME.search(f.name))
        else:
            raise SystemExit(f"release_drift: no such file or folder: {raw}")
        for f in found:
            key = f.resolve()
            if f.suffix == ".md" and key not in seen:
                seen.add(key)
                out.append(f)
    return out


def rel_path(path, repo):
    try:
        return Path(path).resolve().relative_to(Path(repo).resolve()).as_posix()
    except ValueError:
        return str(path)


def read_report(path, local, local_fingerprint):
    """Everything this tool takes from one report. None for a local review output."""
    data = path.read_bytes()
    text = data.decode("utf-8", errors="ignore")
    if local_fingerprint and local_fingerprint in text:
        return None
    lines = text.splitlines()
    where = rel_path(path, local.repo)

    def cite(i):
        return {"at": f"{where}:{i + 1}", "text": " ".join(lines[i].split())[:200]}

    by_name, by_spec = RX_KIND_NAME.search(path.name), RX_KIND_SPEC.search(text)
    kind = KIND[by_name.group(1).lower()] if by_name else KIND[by_spec.group(1)] if by_spec else "unknown"
    dates = RX_DATE.findall(text)
    rep = {"id": hashlib.sha256(data).hexdigest()[:16], "path": where, "eval": kind,
           "date": dates[0] if dates else None, "release": None, "specs": [], "names": {}}
    for i, line in enumerate(lines):
        r = RX_RELEASE.search(line)
        if r and rep["release"] is None:
            rep["release"] = {"fingerprint": r.group(1), **cite(i)}
        cited = [(s.group(1), s.group(2), s.group(3) or "") for s in RX_SPEC.finditer(line)]
        cited += [(SPEC_ALIAS[s.group(1)], s.group(2), s.group(3) or "") for s in RX_SPEC_ALIAS.finditer(line)]
        cited += [(local.resolve_spec(s.group("label")), s.group("h"), s.group("s") or "")
                  for s in RX_HASH_CITE.finditer(line)]
        for rel, prefix, suffix in cited:
            if not rel or "/task_inputs/" in rel or "/universes/" in rel or "/.cache/" in rel:
                continue
            shown = prefix if not suffix else f"{prefix}…{suffix}"
            if not any(x["file"] == rel and x["hash"][:8] == prefix[:8] for x in rep["specs"]):
                rep["specs"].append({"file": rel, "hash": shown, "matches_local": local.matches(rel, prefix, suffix),
                                     **cite(i)})
        found = [("versioned_id", v) for v in RX_VERSIONED.findall(line) if not RX_DATED_ID.search(v)]
        found += [("evals_path", p) for p in RX_PATH.findall(line)
                  if "/task_inputs/" not in p and "/universes/" not in p and "/.cache/" not in p]
        found += [("tool_command", f"{t} {sub}".strip()) for t, sub in RX_TOOL_CMD.findall(line)]
        if RX_RULE_LINE.search(line):
            found += [("check_name", c) for c in RX_CHECK.findall(line)]
        for kind, name in found:
            if name not in rep["names"] and not local.knows(kind, name):
                rep["names"][name] = {"kind": kind, **cite(i)}
    return rep


# ---------------------------------------------------------------- register

def empty_register():
    return {"schema": SCHEMA, "built": None, "updated": None, "local_bundle": {"fingerprint": None, "committed": None},
            "spec_aliases": {}, "reports": {}, "releases": [], "spec_hashes": [], "names": {}, "rules": []}


def load_register(path):
    path = Path(path)
    if not path.is_file():
        return empty_register()
    reg = json.loads(path.read_text())
    if reg.get("schema") != SCHEMA:
        raise SystemExit(f"release_drift: {path} has schema {reg.get('schema')!r}, expected {SCHEMA!r}")
    for key, default in empty_register().items():
        reg.setdefault(key, default)
    return reg


def rule_tokens(reg):
    out = {}
    for rule in reg.get("rules", []):
        for token in [rule.get("id")] + list(rule.get("aliases") or []):
            if token:
                out.setdefault(token, rule["id"])
    return out


def save_register(path, reg, today):
    tokens = rule_tokens(reg)
    for name, entry in reg["names"].items():
        if name in tokens:
            entry["status"] = f"rule:{tokens[name]}"
    reg["releases"].sort(key=lambda e: (e.get("first_seen") or "9999", e["fingerprint"]))
    reg["spec_hashes"].sort(key=lambda e: (e["file"], e.get("first_seen") or "9999", e["hash"]))
    reg["names"] = dict(sorted(reg["names"].items()))
    reg["reports"] = dict(sorted(reg["reports"].items(), key=lambda kv: (kv[1].get("date") or "9999", kv[1]["path"])))
    reg["built"] = reg.get("built") or today
    reg["updated"] = today
    Path(path).write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n")


def _touch(entry, date, at):
    entry["reports"] = entry.get("reports", 0) + 1
    if date and (not entry.get("first_seen") or date < entry["first_seen"]):
        entry["first_seen"], entry["example"] = date, at
    if date and (not entry.get("last_seen") or date > entry["last_seen"]):
        entry["last_seen"] = date
    entry.setdefault("first_seen", None)
    entry.setdefault("last_seen", None)
    entry.setdefault("example", at)


def find_release(reg, fingerprint):
    for e in reg["releases"]:
        a, b = e["fingerprint"], fingerprint
        if a.startswith(b) or b.startswith(a):
            return e
    return None


def find_spec(reg, rel, shown):
    for e in reg["spec_hashes"]:
        if e["file"] == rel and e["hash"][:8] == shown[:8]:
            return e
    return None


def new_items(rep, reg):
    """What this report cites that the register does not hold yet."""
    out = []
    if rep["release"] and not find_release(reg, rep["release"]["fingerprint"]):
        known = [e for e in reg["releases"] if e.get("last_seen")]
        last = max(known, key=lambda e: e["last_seen"]) if known else None
        note = f"latest release with a printed date: {last['fingerprint'][:8]} (last seen {last['last_seen']})" \
            if last else "the register holds no dated release yet"
        out.append({"kind": "release", "name": rep["release"]["fingerprint"], "at": rep["release"]["at"],
                    "note": note})
    for s in rep["specs"]:
        if not find_spec(reg, s["file"], s["hash"]):
            same = [e for e in reg["spec_hashes"] if e["file"] == s["file"] and e.get("last_seen")]
            last = max(same, key=lambda e: e["last_seen"]) if same else None
            local = {True: "the local copy matches it", False: "the local copy differs",
                     None: "there is no local copy"}[s["matches_local"]]
            note = (f"last known {last['hash'][:8]} (seen {last['last_seen']}); " if last else "") + local
            out.append({"kind": "spec_hash", "name": f"{s['file']} {s['hash']}", "at": s["at"], "note": note})
    for name, info in rep["names"].items():
        if name not in reg["names"]:
            out.append({"kind": info["kind"], "name": name, "at": info["at"], "note": info["text"]})
    return out


def add_report(rep, reg, status):
    """Record one report's citations. Returns False when the report is already recorded."""
    if rep["id"] in reg["reports"]:
        return False
    reg["reports"][rep["id"]] = {"path": rep["path"], "eval": rep["eval"], "date": rep["date"],
                                 "release": rep["release"]["fingerprint"][:8] if rep["release"] else None}
    if rep["release"]:
        entry = find_release(reg, rep["release"]["fingerprint"])
        if entry is None:
            entry = {"fingerprint": rep["release"]["fingerprint"], "status": status}
            reg["releases"].append(entry)
        elif len(rep["release"]["fingerprint"]) > len(entry["fingerprint"]):
            entry["fingerprint"] = rep["release"]["fingerprint"]
        _touch(entry, rep["date"], rep["release"]["at"])
    for s in rep["specs"]:
        entry = find_spec(reg, s["file"], s["hash"])
        if entry is None:
            entry = {"file": s["file"], "hash": s["hash"], "matches_local": s["matches_local"], "status": status}
            reg["spec_hashes"].append(entry)
        elif len(s["hash"]) > len(entry["hash"]):
            entry["hash"] = s["hash"]
        _touch(entry, rep["date"], s["at"])
    for name, info in rep["names"].items():
        entry = reg["names"].setdefault(name, {"kind": info["kind"], "status": status})
        _touch(entry, rep["date"], info["at"])
    return True


# ---------------------------------------------------------------- commands

def _local(args, reg):
    schema = Path(args.repo) / "Task_Authoring" / "references" / "universe_schema_live.json"
    return Local(args.repo, schema, reg.get("spec_aliases"))


def _read_all(paths, local, reg):
    reps, skipped = [], []
    for f in report_files(paths):
        rep = read_report(f, local, (reg.get("local_bundle") or {}).get("fingerprint"))
        if rep is None:
            skipped.append(rel_path(f, local.repo))
        else:
            reps.append(rep)
    return reps, skipped


def cmd_scan(args, record=False):
    reg = load_register(args.register)
    local = _local(args, reg)
    reps, skipped = _read_all(args.paths, local, reg)
    already, results = 0, []
    for rep in sorted(reps, key=lambda r: (r["date"] or "9999", r["path"])):
        if rep["id"] in reg["reports"]:
            already += 1
            continue
        items = new_items(rep, reg)
        results.append({"report": rep["path"], "eval": rep["eval"], "date": rep["date"], "new": items})
        # In memory only unless recording, so a later report in the same scan does not repeat the finding.
        add_report(rep, reg, "unreviewed")
    if record and results:
        save_register(args.register, reg, args.today)
    hard = sum(1 for r in results for i in r["new"] if i["kind"] != "check_name")
    soft = sum(1 for r in results for i in r["new"] if i["kind"] == "check_name")
    drift = hard > 0 or (args.strict and soft > 0)
    if args.json:
        print(json.dumps({"reports_read": len(reps), "already_recorded": already, "skipped_local": skipped,
                          "results": results, "new_hard": hard, "new_check_names": soft, "drift": drift}, indent=1))
        return 1 if drift else 0
    print(f"release_drift {'record' if record else 'scan'}: {len(reps)} platform reports read, {already} already in "
          f"the register, {len(skipped)} local review outputs skipped")
    for r in results:
        if not r["new"]:
            continue
        print(f"\n{r['report']}  ({r['eval']}, review date {r['date'] or 'not stated'})")
        for i in r["new"]:
            print(f"  {FINDING_LABEL[i['kind']]:<21} {i['name']}\n      {i['at']}: {i['note']}")
    verdict = "DRIFT" if drift else "NO DRIFT"
    print(f"\nRESULT: {verdict} - {hard} new release, spec, rule id, file or tool items; {soft} possible check names"
          + (f"; added to {rel_path(args.register, args.repo)} as unreviewed" if record and results else ""))
    if drift and not record:
        print("Next: read the cited lines, then run `record` so the register holds them for review.")
    return 1 if drift else 0


def cmd_rebuild(args):
    old = load_register(args.register)
    kept = {("release", e["fingerprint"][:8]): e for e in old["releases"]}
    kept.update({("spec", e["file"], e["hash"][:8]): e for e in old["spec_hashes"]})
    kept.update({("name", n): e for n, e in old["names"].items()})
    reg = empty_register()
    reg.update({"built": old.get("built"), "local_bundle": old.get("local_bundle") or reg["local_bundle"],
                "spec_aliases": old.get("spec_aliases", {}), "rules": old.get("rules", [])})
    for key in old:                                         # curated extras a reviewer added stay
        reg.setdefault(key, old[key])
    local = _local(args, reg)
    reps, skipped = _read_all(args.paths, local, reg)
    for rep in sorted(reps, key=lambda r: (r["date"] or "9999", r["path"])):
        add_report(rep, reg, "baseline")

    def restore(entry, key):                                # a reviewer's status and note outlive a rebuild
        before = kept.get(key) or {}
        if before.get("status") in ("unreviewed", "not_a_rule"):
            entry["status"] = before["status"]
        if before.get("note"):
            entry["note"] = before["note"]
    for e in reg["releases"]:
        restore(e, ("release", e["fingerprint"][:8]))
    for e in reg["spec_hashes"]:
        restore(e, ("spec", e["file"], e["hash"][:8]))
    for n, e in reg["names"].items():
        restore(e, ("name", n))
    save_register(args.register, reg, args.today)
    undated = sum(1 for r in reg["reports"].values() if not r["date"])
    kinds = {k: sum(1 for e in reg["names"].values() if e["kind"] == k) for k in NAME_KINDS}
    print(f"release_drift rebuild: {len(reg['reports'])} platform reports ({undated} without a review date), "
          f"{len(skipped)} local review outputs skipped")
    print(f"  releases {len(reg['releases'])}, spec hashes {len(reg['spec_hashes'])}, names absent from the local "
          f"bundle {len(reg['names'])} ({', '.join(f'{k} {v}' for k, v in kinds.items())}), curated rules "
          f"{len(reg['rules'])}")
    print(f"  written: {rel_path(args.register, args.repo)}")
    return 0


def cmd_status(args):
    reg = load_register(args.register)
    reports = reg["reports"].values()
    dates = sorted(r["date"] for r in reports if r["date"])
    by_eval = {}
    for r in reports:
        by_eval[r["eval"]] = by_eval.get(r["eval"], 0) + 1
    print(f"register {rel_path(args.register, args.repo)} (built {reg.get('built')}, updated {reg.get('updated')})")
    print(f"local bundle fingerprint: {(reg.get('local_bundle') or {}).get('fingerprint')}")
    print(f"platform reports: {len(reg['reports'])}" + (f", review dates {dates[0]} to {dates[-1]}" if dates else "")
          + "; " + ", ".join(f"{k} {v}" for k, v in sorted(by_eval.items())))
    print("\nreleases (oldest first):")
    for e in reg["releases"]:
        print(f"  {e['fingerprint'][:12]}  {e.get('first_seen')} to {e.get('last_seen')}  {e['reports']} reports"
              f"  [{e.get('status')}]" + (f"  note: {e['note']}" if e.get("note") else ""))
    print("\nspec files cited with a hash:")
    files = sorted({e["file"] for e in reg["spec_hashes"]})
    for f in files:
        rows = [e for e in reg["spec_hashes"] if e["file"] == f]
        latest = max(rows, key=lambda e: e.get("last_seen") or "")
        state = {True: "local copy matches the latest hash seen", False: "local copy differs from the latest hash seen",
                 None: "no local copy"}[latest.get("matches_local")]
        print(f"  {f}: {len(rows)} hashes; {state}")
        for e in rows:
            print(f"      {e['hash'][:14]:<14} {e.get('first_seen')} to {e.get('last_seen')}  {e['reports']} reports"
                  f"{'  = local' if e.get('matches_local') else ''}")
    rules = reg.get("rules", [])
    per = {}
    for r in rules:
        per[r.get("eval", "?")] = per.get(r.get("eval", "?"), 0) + 1
    print(f"\ncurated platform-only rules: {len(rules)}" + ("; " + ", ".join(f"{k} {v}" for k, v in sorted(per.items()))
                                                           if rules else ""))
    waiting = [("release", e["fingerprint"][:12], e.get("example")) for e in reg["releases"]
               if e.get("status") == "unreviewed"]
    waiting += [("spec hash", f"{e['file']} {e['hash'][:12]}", e.get("example")) for e in reg["spec_hashes"]
                if e.get("status") == "unreviewed"]
    waiting += [(e["kind"], n, e.get("example")) for n, e in reg["names"].items() if e.get("status") == "unreviewed"]
    print(f"\nawaiting review: {len(waiting)}")
    for kind, name, at in waiting:
        print(f"  {kind}: {name}  ({at})")
    return 0


# ---------------------------------------------------------------- self-test

def selftest():
    import selftest_sandbox
    with selftest_sandbox.scratch_tmp("release_drift_selftest_") as tmp:
        repo = Path(tmp) / "repo"
        (repo / "Evals" / "tools").mkdir(parents=True)
        (repo / "Evals" / "task_inputs").mkdir()
        (repo / "claude").mkdir()
        spec = repo / "Evals" / "1A_Hardness_Eval.md"
        spec.write_text("assessment version model-aware-v3; lint `known_check`\n")
        (repo / "Evals" / "WORKFLOW.md").write_text("workflow\n")
        (repo / "Evals" / "references").mkdir()
        (repo / "Evals" / "references" / "scoring.json").write_text("{}\n")
        (repo / "Evals" / "README.md").write_text("top\n")
        (repo / "Evals" / "references" / "README.md").write_text("schema notes\n")
        (repo / "Evals" / "tools" / "hg_rubric_ledger.py").write_text(
            "COMMANDS = ['plan', 'write', 'diff']\nCANDIDATE = 'fixcheck/rubric_candidate.json'\n")
        (repo / "Evals" / "task_inputs" / "note.md").write_text("store-only-v9 store_only_name\n")
        local_sha = hashlib.sha256(spec.read_bytes()).hexdigest()
        reports = repo / "Task_Authoring" / "task_x" / "eval_reports"
        reports.mkdir(parents=True)
        rel_a, rel_b = "a" * 64, "b" * 64
        (reports / "1a_hardness_FAIL_r1.md").write_text(
            "# /hardness\n| Eval | `Evals/1A_Hardness_Eval.md` (SHA-256 `%s…%s`), version `model-aware-v3` |\n"
            "| Actual review time | 2026-11-02T10:00Z |\n| Clock | 2025-10-01 |\n"
            "Rule `count-bundle-v1` and lint `bundled_writes`; `known_check` ran.\n"
            "Eval release SHA-256: %s\n" % (local_sha[:8], local_sha[-4:], rel_a))
        (reports / "3_rubric_local.md").write_text("local run, release LOCALFP000000\n`should_not_count`\n")
        report_b = reports / "x_3_rubric (1).md"
        report_b.write_text(
            "| Review | Chat review, audit mode, review date 2026-11-08 |\n"
            "| Eval | `Evals/1A_Hardness_Eval.md` sha256 `ffffffff11112222` |\n"
            "Applies ugt-fork-v1 and count-bundle-v1; see `Evals/references/known_base_issues.md`.\n"
            "Ran `hg_rubric_ledger.py fixcheck` and `hg_rubric_ledger.py plan`; table `sheets_cells`; `scope_tail`.\n"
            "| Eval version | Eval 1 SHA-256 `1234567890abcdef`; universe `hg4-2026-08-31-v37` |\n"
            "| References | WORKFLOW `aaaa1111…ff`; scoring.json `bbbb2222cccc…`; tool_outputs.md `dddd3333…`; "
            "Eval 0 report `eeee4444…`; `04_Prompt.txt` SHA-256 `ffff5555aaaa` |\n"
            "Read `evt_9c41e7a2d05b38f6` through `list_comments`, which returned `channel_not_found`.\n"
            "Eval release SHA-256: %s\n" % rel_b)
        register = repo / "Task_Authoring" / "references" / "platform_rule_delta.json"
        register.parent.mkdir(parents=True)
        (register.parent / "universe_schema_live.json").write_text('{"tables": ["sheets_cells"]}')
        seed = empty_register()
        seed["local_bundle"] = {"fingerprint": "LOCALFP000000", "committed": "2026-11-01"}
        seed["rules"] = [{"id": "count-bundle-v1", "eval": "/rubric", "aliases": ["bundled_writes"]}]
        seed["spec_aliases"] = {"tool_outputs.md": "Evals/references/tool_outputs.md"}
        register.write_text(json.dumps(seed))
        base = ["--repo", str(repo), "--register", str(register), "--today", "2026-11-10"]
        assert not Local(repo).knows("versioned_id", "store-only-v9"), "the input store is not the local bundle"
        assert Local(repo).resolve_spec("README") is None and Local(repo).resolve_spec("`README.md`") is None
        assert Local(repo).resolve_spec("WORKFLOW") == "Evals/WORKFLOW.md"

        # 1. rebuild from report A only: the local output is skipped, known names are not listed
        report_b.rename(Path(tmp) / "held_back.md")
        assert main(["rebuild", str(repo / "Task_Authoring")] + base) == 0
        reg = json.loads(register.read_text())
        assert len(reg["reports"]) == 1 and [e["fingerprint"] for e in reg["releases"]] == [rel_a], reg["releases"]
        only = next(iter(reg["reports"].values()))
        assert only["eval"] == "/hardness" and only["date"] == "2026-11-02", only
        assert reg["spec_hashes"][0]["matches_local"] is True and reg["spec_hashes"][0]["first_seen"] == "2026-11-02"
        assert set(reg["names"]) == {"count-bundle-v1", "bundled_writes"}, set(reg["names"])
        assert reg["names"]["bundled_writes"]["status"] == "rule:count-bundle-v1"
        assert reg["rules"] == seed["rules"], "curated rules must survive a rebuild"

        # 2. scan report B: read-only, finds exactly the new items
        (Path(tmp) / "held_back.md").rename(report_b)
        before = register.read_bytes()
        assert main(["scan", str(report_b), "--json"] + base) == 1
        assert register.read_bytes() == before, "scan must not write"
        rep = read_report(report_b, Local(repo, register.parent / "universe_schema_live.json", seed["spec_aliases"]),
                          "LOCALFP000000")
        got = {(i["kind"], i["name"]) for i in new_items(rep, reg)}
        assert got == {("release", rel_b), ("spec_hash", "Evals/1A_Hardness_Eval.md ffffffff11112222"),
                       ("spec_hash", "Evals/1_Prompt_Eval.md 1234567890abcdef"),
                       ("spec_hash", "Evals/WORKFLOW.md aaaa1111…ff"),
                       ("spec_hash", "Evals/references/scoring.json bbbb2222cccc"),
                       ("spec_hash", "Evals/references/tool_outputs.md dddd3333"),
                       ("versioned_id", "ugt-fork-v1"), ("evals_path", "Evals/references/known_base_issues.md"),
                       ("tool_command", "hg_rubric_ledger.py fixcheck"), ("check_name", "scope_tail")}, got
        assert rep["eval"] == "/rubric" and rep["date"] == "2026-11-08" and rep["specs"][0]["matches_local"] is False
        assert rep["specs"][1]["matches_local"] is None, "no local copy of that spec in the self-test repo"
        for line in ("| Actual review time | 2026-11-08T10:00Z |", "| Actual review date | 2026-10-26 |",
                     "audit mode, review date 2026-11-05.", "`/oe` audit, reviewed 2026-11-07",
                     "Actual review time: 2026-11-08T09:10Z"):
            assert RX_DATE.search(line), line
        assert not RX_DATE.search("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC)")
        assert report_files([repo / "Task_Authoring" / "references"]) == [], "a plain folder without reports reads none"

        # 3. record B, then the same scan is quiet; a task-folder path finds both report folders
        assert main(["record", str(report_b)] + base) == 1
        reg = json.loads(register.read_text())
        assert reg["names"]["ugt-fork-v1"]["status"] == "unreviewed" and len(reg["reports"]) == 2
        assert reg["names"]["count-bundle-v1"]["reports"] == 2 and reg["names"]["count-bundle-v1"]["last_seen"] == "2026-11-08"
        assert main(["scan", str(repo / "Task_Authoring" / "task_x")] + base) == 0

        # 4. a reviewer's not_a_rule survives a rebuild; an unreviewed item stays unreviewed
        reg["names"]["scope_tail"]["status"] = "not_a_rule"
        reg["releases"][0]["note"] = "kept note"
        register.write_text(json.dumps(reg))
        assert main(["rebuild", str(repo / "Task_Authoring")] + base) == 0
        reg = json.loads(register.read_text())
        assert reg["names"]["scope_tail"]["status"] == "not_a_rule" and reg["names"]["ugt-fork-v1"]["status"] == "unreviewed"
        assert len(reg["reports"]) == 2 and len(reg["releases"]) == 2 and len(reg["spec_hashes"]) == 6
        assert reg["releases"][0].get("note") == "kept note" and reg["spec_aliases"] == seed["spec_aliases"]
        assert main(["status"] + base) == 0

        # 5. check names alone do not flip the exit code unless --strict
        soft = reports / "2_oe_PASS_r3.md"
        soft.write_text("review date 2026-11-09\nlint `brand_new_check`\nEval release SHA-256: %s\n" % rel_b)
        assert main(["scan", str(soft)] + base) == 0
        assert main(["scan", str(soft), "--strict"] + base) == 1
    print("release_drift selftest: PASS")
    return 0


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="release_drift.py", description="platform eval-release drift (see docstring)")
    ap.add_argument("command", nargs="?", choices=("scan", "record", "rebuild", "status"))
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--register", default=str(REGISTER))
    ap.add_argument("--repo", default=str(REPO), help="folder that holds Evals/ and claude/")
    ap.add_argument("--today", default=None, help="date written to the register (default: today)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true", help="possible check names also count as drift")
    ap.add_argument("--selftest", "--self-test", dest="selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.command:
        ap.error("a command is required: scan, record, rebuild or status")
    if args.command != "status" and not args.paths:
        ap.error(f"{args.command} needs at least one report file or folder")
    if args.today is None:
        from datetime import date
        args.today = date.today().isoformat()
    if args.command == "scan":
        return cmd_scan(args)
    if args.command == "record":
        return cmd_scan(args, record=True)
    if args.command == "rebuild":
        return cmd_rebuild(args)
    return cmd_status(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
