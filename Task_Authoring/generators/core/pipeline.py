"""Render pipeline (plan §3.4): context -> spec -> pinned base -> expand -> SQL -> independent validation -> record.

Outputs, relative to the task folder:
  Working_Files/build/parts/<service>.sql   one service section: a banner line, then one statement per line
  Working_Files/build/provenance.json       every column of every operation with its origin and construction
  Working_Files/build/build_record.json     no timestamps: spec, context, snapshot, pinned dependencies, conventions,
                                            per-file sha256, validation verdicts
  Working_Files/build/upgrades.jsonl        append-only log of accepted dependency upgrades (not a build output)
A task's own assembler splices the parts into 01_Universe_Inject.sql; the existing gate tools then run unchanged.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from .. import LIBRARY_VERSION, changed_since_load as library_changed, ensure_current as ensure_library_current
from ..services import registry
from ..spec.load import load_spec
from ..validate import agreement, coltypes, compare, grammar, invariants, overlay, parse_back
from . import context, emitter, output
from .base import BaseSnapshot
from .context import TOOL_ROOTS, tool_closure  # noqa: F401 - re-exported: the tools/ closure the record pins
from .resolve import Resolver
from .values import SpecError, read_confined

LIB = Path(__file__).resolve().parents[1]
TA = LIB.parent
WS = TA.parent
SCHEMA_LIVE = TA / "references" / "universe_schema_live.json"
# What validation reads besides the library: the tools/ closure it runs (core/context.py) and the data files those
# read. An absent optional file is pinned as None.
DATA_FILES = {"schema_live": SCHEMA_LIVE,
              "constraints_live": TA / "references" / "universe_constraints_live.json",
              "injection_schema": TA / "references" / "injection.json",
              "eval_injection_schema": WS / "Evals" / "references" / "schema" / "injection.json"}
CENSUS_FORMAT = "hg-gen-census/1"
HIT_CLASSES = {"supports", "contradicts", "superseded", "irrelevant"}
SPEC_DIR = "Working_Files/spec"
BUILD = "Working_Files/build"
PROVENANCE = f"{BUILD}/provenance.json"
RECORD = f"{BUILD}/build_record.json"
UPGRADES = f"{BUILD}/upgrades.jsonl"
SHOW = 20                       # messages kept per rule in the build record (counts are always complete)


def part_path(service: str) -> str:
    return f"{BUILD}/parts/{service}.sql"


class BuildError(Exception):
    def __init__(self, stage: str, problems: list[str]):
        super().__init__(f"{stage}: {len(problems)} problem(s); first: {problems[0] if problems else ''}")
        self.stage, self.problems = stage, problems


def _sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha_file(path: Path) -> str:
    return _sha_bytes(Path(path).read_bytes())


def _json_bytes(obj) -> bytes:
    return (json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False, default=str) + "\n").encode("utf-8")


@dataclass
class Result:
    task_dir: Path
    ctx: dict
    spec: object
    base: BaseSnapshot
    resolver: Resolver
    ops: list
    ops_by_service: dict
    parts: dict
    files: dict
    conventions: list
    conventions_sha: str
    early_warnings: list
    inputs: dict = field(default_factory=dict)          # task-relative path -> sha256 every input was read with
    validation: dict = field(default_factory=dict)

    def full_sql(self) -> str:
        return emitter.render_full([], [self.parts[s] for s in sorted(self.parts)])


def _sha256_field(where: str, value) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        raise SpecError(where, "must be a sha256 (64 lower-case hex)")


def _census_doc(claim: str, raw: bytes) -> None:
    """The census evidence a claim needs (plan §3.2): scope with aliases, every service searched to the last page with
    query and result hashes, the hits classified, and a reviewer disposition that the claim holds."""
    where = f"census.{claim}"
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise SpecError(where, f"census file is not UTF-8 JSON: {exc}") from None
    need = {"format", "claim", "scope", "services", "hits", "disposition"}
    if not isinstance(doc, dict) or set(doc) != need:
        raise SpecError(where, f"census needs exactly the keys {sorted(need)}")
    if doc["format"] != CENSUS_FORMAT or doc["claim"] != claim:
        raise SpecError(where, f"census must be {CENSUS_FORMAT} for claim {claim!r}")
    scope = doc["scope"]
    if not (isinstance(scope, dict) and set(scope) == {"entity", "aliases"} and isinstance(scope["entity"], str)
            and scope["entity"] and isinstance(scope["aliases"], list)
            and all(isinstance(a, str) and a for a in scope["aliases"])):
        raise SpecError(f"{where}.scope", "needs entity (text) and aliases (list of text)")
    if not isinstance(doc["services"], list) or not doc["services"]:
        raise SpecError(f"{where}.services", "list every service searched")
    def text(v) -> bool:
        return isinstance(v, str) and bool(v.strip())

    for n, s in enumerate(doc["services"]):
        keys = {"service", "query", "query_sha256", "pages", "complete", "result_sha256"}
        if not isinstance(s, dict) or set(s) != keys or not text(s["service"]) or not text(s["query"]):
            raise SpecError(f"{where}.services[{n}]", f"needs exactly {sorted(keys)}; service and query as text")
        if s["complete"] is not True or type(s["pages"]) is not int or s["pages"] < 1:
            raise SpecError(f"{where}.services[{n}]", "pagination must be complete (complete: true, pages >= 1)")
        _sha256_field(f"{where}.services[{n}].query_sha256", s["query_sha256"])
        _sha256_field(f"{where}.services[{n}].result_sha256", s["result_sha256"])
    if not isinstance(doc["hits"], list):
        raise SpecError(f"{where}.hits", "must be a list")
    for n, h in enumerate(doc["hits"]):
        if not (isinstance(h, dict) and set(h) == {"locator", "classification"} and text(h["locator"])
                and h["classification"] in HIT_CLASSES):
            raise SpecError(f"{where}.hits[{n}]", f"needs locator and a classification in {sorted(HIT_CLASSES)}")
    d = doc["disposition"]
    if not (isinstance(d, dict) and set(d) == {"by", "verdict", "note"} and text(d["by"])
            and isinstance(d["note"], str)):
        raise SpecError(f"{where}.disposition", "needs by (text), verdict and note (text)")
    if d["verdict"] != "holds":
        raise SpecError(f"{where}.disposition", f"the reviewer's verdict is {d['verdict']!r}; a claim needs 'holds'")


def _check_census(spec) -> dict:
    """Every claim's census file, read once (load_spec gives each claim its own file), checked against its pin and
    the census format; returns {path: sha256} of what was read."""
    claims = sorted({c for r in spec.records for v in r["fields"].values() for c in v.claims})
    missing = [c for c in claims if c not in spec.census]
    if missing:
        raise SpecError("census", f"claims without census evidence: {missing}")
    extra = sorted(set(spec.census) - set(claims))
    if extra:
        raise SpecError("census", f"census entries no claim uses: {extra}")
    read = {}
    for claim, entry in spec.census.items():
        path = spec.dir / entry["file"]
        if spec.root:
            raw = read_confined(spec.root, path, f"census.{claim}")
        else:
            if path.is_symlink() or not path.is_file():
                raise SpecError(f"census.{claim}", f"{entry['file']} is not a regular file in the spec folder")
            raw = path.read_bytes()
        if _sha_bytes(raw) != entry["sha256"]:
            raise SpecError(f"census.{claim}", f"{entry['file']} sha256 differs from the spec pin")
        _census_doc(claim, raw)
        read[path] = entry["sha256"]
    return read


def _rel(task_dir: Path, path: Path) -> str:
    return os.path.relpath(os.path.abspath(path), os.path.abspath(task_dir)).replace(os.sep, "/")


def inputs_changed(res: Result) -> list[str]:
    """What this build read that is no longer the same on disk (empty: nothing): the task's inputs (assignment,
    spec.json, texts, census), the pinned base export and source manifest of every service it read, and the task
    context recomputed from scratch (assignment, policy, roster, universe and every service's source manifest)."""
    out = []
    for rel, sha in sorted(res.inputs.items()):
        try:
            now = output.task_sha256(res.task_dir, rel) or "missing"
        except (OSError, output.PublishError) as exc:
            now = f"unreadable ({exc})"
        if now != sha:
            out.append(f"{rel}: read as {sha[:12]}, now {now[:12]}")
    for path, sha in sorted(res.base.read.items()):
        try:
            now = _sha_file(Path(path))
        except OSError as exc:
            now = f"unreadable ({exc})"
        if now != sha:
            out.append(f"{path}: read as {sha[:12]}, now {now[:12]}")
    try:
        now = context.recompute(res.task_dir)["context_hash"]
    except (SpecError, context.ToolsChanged) as exc:     # a tools/ change is listed here and by _moved, not raised
        now = f"unavailable ({exc})"
    if now != res.ctx["context_hash"]:
        out.append(f"task context: built with {res.ctx['context_hash'][:12]}, now {now[:12]}")
    return out


def build(task_dir: Path, spec_dir: Path | None = None) -> Result:
    """Everything in memory; writes nothing. Raises SpecError or BuildError with the record key. The task path is
    resolved here, once; everything after works on that resolved path (see _build)."""
    return _build(Path(task_dir).resolve(), spec_dir)


def _build(task_dir: Path, spec_dir: Path | None = None) -> Result:
    """build() on a task path the caller resolved once: it is never resolved again, and every read of a task file goes
    through output's descriptor walk, which refuses a symlink swapped in anywhere on that path. render and check lock,
    build and publish one and the same path this way."""
    ctx = context.recompute(task_dir)
    spec_dir = Path(spec_dir) if spec_dir else task_dir / SPEC_DIR
    spec = load_spec(spec_dir, root=task_dir)
    context.check_spec_task(spec.task, ctx)
    base = BaseSnapshot(context.service_paths(ctx), spec.snapshot)
    for service in sorted(spec.snapshot):
        base.doc(service)
    conventions, conv_sha = registry.load_conventions()
    used = registry.conventions_used({r["kind"] for r in spec.records}, conventions, spec.overrides)
    census_read = _check_census(spec)
    resolver = Resolver(spec, base, registry.transforms())
    by_service = {}
    for service in spec.services():
        mod = registry.emitter(service, spec.emitters[service])
        try:
            by_service[service] = mod.expand([r for r in spec.records if r["service"] == service], resolver, base)
        except (TypeError, ValueError) as exc:          # a value of the wrong type for its column (core/ops.py)
            raise BuildError(f"{service} expand", [str(exc)]) from None
    computed = {fn for fn, f in registry.transforms().items() if f is None}
    unused = [f"{r['key']}.{n}" for r in spec.records for n, v in sorted(r["fields"].items())
              if (r["key"], n) not in resolver.cache and not (v.construction == "transform" and v.fn in computed)]
    if unused:
        raise SpecError("records", f"fields the emitter never read: {unused[:10]}")
    ops = [op for s in sorted(by_service) for op in by_service[s]]
    schema = emitter.load_schema()
    errors, warnings = [], []
    for op in ops:
        e, w = emitter.check_op(op, schema, ctx["freeze_utc"])
        errors += e
        warnings += w
    if errors:
        raise BuildError("early schema and row checks", errors)
    parts = {s: emitter.render_part(s, by_service[s]) for s in by_service}
    files = {part_path(s): text.encode("utf-8") for s, text in parts.items()}
    files[PROVENANCE] = _json_bytes(provenance_doc(spec, ops))
    inputs = {"00_Assigments.md": ctx["assignment_hash"], _rel(task_dir, spec_dir / "spec.json"): spec.sha256}
    inputs.update({_rel(task_dir, spec.dir / t): sha for t, sha in resolver.texts.items()})
    inputs.update({_rel(task_dir, p): sha for p, sha in census_read.items()})
    return Result(task_dir, ctx, spec, base, resolver, ops, by_service, parts, files, used, conv_sha, warnings,
                  inputs=inputs)


def provenance_doc(spec, ops) -> dict:
    out = []
    for n, op in enumerate(ops):
        out.append({"n": n, "table": op.table, "op": op.op, "key": [v for _, v in op.where] or [op.cols[0][1]],
                    "record": op.record, "columns": {c: p for c, p in op.prov}})
    return {"format": "hg-gen-provenance/1", "spec_sha256": spec.sha256, "ops": out}


LINT_TIMEOUT = 900                # seconds


def _lint(task_dir: Path, text: str) -> dict:
    """tools/sql_lint.py exactly as an author runs it, in its own process (its task-context globals stay there),
    reading the text from stdin. A run that cannot start, times out (it is killed) or does not finish with a
    consistent JSON report is a blocking error in the report (not an exception), so the other checks' findings stay
    visible."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("TASK_AUTHORING_")}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPYCACHEPREFIX"] = context.NO_BYTECODE      # compile tools/ and Evals/ imports from source
    cmd = [sys.executable, "-B", str(TA / "tools" / "sql_lint.py"), "/dev/stdin", "--json", "--task-dir", str(task_dir)]

    def blocked(why: str) -> dict:
        return {"errors": [{"line": 0, "msg": f"tools/sql_lint.py did not complete ({why})"}], "warnings": []}
    try:
        data = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return blocked(f"the text cannot be encoded as UTF-8: {exc}")
    try:
        p = subprocess.run(cmd, input=data, capture_output=True, env=env, cwd=str(WS), timeout=LINT_TIMEOUT)
    except subprocess.TimeoutExpired:
        return blocked(f"no report within {LINT_TIMEOUT} s; it was stopped")
    except OSError as exc:
        return blocked(f"it could not be started: {exc}")
    try:
        res = json.loads(p.stdout.decode("utf-8"))
    except ValueError:
        res = None
    if (not isinstance(res, dict) or not _lint_entries(res.get("errors")) or not _lint_entries(res.get("warnings"))
            or p.returncode not in (0, 1) or (p.returncode == 1) != bool(res["errors"])):
        tail = (p.stderr.decode("utf-8", "replace").strip().splitlines() or ["no output"])[-1]
        return blocked(f"exit {p.returncode}, no well-formed report: {tail}")
    return {"errors": res["errors"], "warnings": res["warnings"]}


def _lint_entries(entries) -> bool:
    """A list of sql_lint findings, each with an integer line and a text msg."""
    return isinstance(entries, list) and all(
        isinstance(e, dict) and type(e.get("line")) is int and isinstance(e.get("msg"), str) for e in entries)


def _shown(items: list[str]) -> dict:
    return {"count": len(items), "first": items[:SHOW]}


def validate(res: Result, text: str | None = None, *, foreign: bool = False) -> dict:
    """Independent checks on the rendered text (default: this build's parts), never on the emitter's own data.

    foreign=True checks a file the library did not write as a whole (e.g. the assembled 01_Universe_Inject.sql): the
    restricted grammar is then advisory, and only the operations on this spec's services are compared, in order."""
    text = res.full_sql() if text is None else text
    out = {"grammar": [], "parse_back": None, "types": [], "compare": [], "overlay": [], "invariants": {},
           "sql_lint": {}}
    out["grammar"] = [f"line {e.line}: {e.message}" for e in grammar.check_sql(text)]
    parsed = None
    try:
        parsed = parse_back.parse_ops(text, schema_path=SCHEMA_LIVE)
        out["parse_back"] = f"{len(parsed)} operations"
    except parse_back.ParseBackError as exc:
        out["parse_back"] = f"FAIL: {exc}"
    if parsed is not None:
        out["agreement"] = _shown(agreement.disagreements(text, parsed))
        mine = {op.table for op in res.ops}
        if foreign:
            parsed = [op for op in parsed if op.table.split(".")[0] in res.parts or op.table in mine]
        out["types"] = coltypes.check_ops(parsed, SCHEMA_LIVE)
        out["compare"] = [d.message for d in compare.compare_ops(res.ops, parsed)]
        if "linear" in res.parts:
            pin = res.spec.snapshot["linear"]
            data = context.service_paths(res.ctx)["linear"] / pin["file"]
            rows = overlay.load_linear_base(data, pin["sha256"])
            ov = overlay.apply(rows, [op for op in parsed if op.table.startswith("linear.")])
            out["overlay"] = list(ov.errors)
            findings = invariants.check_linear(ov, rows, freeze_utc=res.ctx["freeze_utc"])
            for sev in ("FAIL", "WARN"):
                per = {}
                for f in findings:
                    if f.severity == sev:
                        per.setdefault(f.rule, []).append(f"{f.table} {list(f.key)}: {f.message}")
                out["invariants"][sev] = {rule: _shown(msgs) for rule, msgs in sorted(per.items())}
    lint = _lint(res.task_dir, text)
    out["sql_lint"] = {"errors": _shown([f"line {e['line']}: {e['msg']}" for e in lint["errors"]]),
                       "warnings": _shown([f"line {e['line']}: {e['msg']}" for e in lint["warnings"]])}
    ensure_library_current()                # the library and tools/ code these checks ran is still the code on disk
    context.ensure_tools_current()
    failed = ((out["grammar"] and not foreign) or parsed is None or out["types"] or out["compare"] or out["overlay"]
              or out["invariants"].get("FAIL") or lint["errors"])
    out["verdict"] = "FAIL" if failed else "PASS"
    if not foreign:
        res.validation = out
    return out


_FACT_TOKENS = (("amount", r"\$\d[\d,]*(?:\.\d+)?"), ("date", r"\b\d{4}-\d{2}-\d{2}\b"),
                ("ticket", r"\b[A-Z]{2,5}-\d+\b"))
_PROSE_FIELDS = {"title", "name", "summary", "description", "body"}


def provenance_report(res: Result) -> dict:
    """Coverage, origins, base fan-out, chronology and cites checks, claims, and un-cited fact-like tokens."""
    origins, fanout, missing = Counter(), Counter(), []
    for op in res.ops:
        prov = dict(op.prov)
        for c, _ in op.cols:
            p = prov.get(c)
            if not p:
                missing.append(f"{op.table} {op.record}: {c}")
                continue
            origins[p["origin"]] += 1
            if p["origin"] == "base":
                b = p["base"]
                fanout[f"{b['service']}:{b['collection']}/{b['record']}{b['field']}"] += 1
    cited = {}
    for c in res.resolver.cite_checks:
        cited.setdefault(c["field"], set()).add(c["value"])
    flags = []
    for rec in res.spec.records:
        for name, v in sorted(rec["fields"].items()):
            if v.origin != "authored" or v.construction != "literal" or not (v.text or name in _PROSE_FIELDS):
                continue
            value, _ = res.resolver.cache.get((rec["key"], name), (None, None))
            if not isinstance(value, str):
                continue
            where = f"{rec['key']}.{name}"
            for kind, pattern in _FACT_TOKENS:
                for tok in sorted(set(re.findall(pattern, value))):
                    if not any(tok in s for s in cited.get(where, ())):
                        flags.append(f"{where}: un-cited {kind} {tok}")
    claims = sorted({c for r in res.spec.records for v in r["fields"].values() for c in v.claims})
    return {
        "operations": len(res.ops),
        "columns_without_provenance": missing,
        "origins": dict(sorted(origins.items())),
        "base_fanout": {k: n for k, n in sorted(fanout.items(), key=lambda kv: (-kv[1], kv[0])) if n > 1},
        "after_checks": len(res.resolver.after_checks),
        "cite_checks": len(res.resolver.cite_checks),
        "claims": {c: res.spec.census[c]["file"] for c in claims},
        "conventions": res.conventions,
        "texts": len(res.resolver.texts),
        "uncited_fact_tokens": _shown(flags),
        "verdict": "FAIL" if missing else "PASS",
    }


def _fingerprint(tools: dict) -> dict:
    lib = hashlib.sha256()
    for p in sorted(LIB.rglob("*")):
        rel = p.relative_to(LIB)
        if not p.is_file() or rel.parts[0] == "tests" or "__pycache__" in rel.parts or p.suffix not in (".py", ".json"):
            continue
        lib.update(f"{rel.as_posix()} {_sha_file(p)}\n".encode())
    data = {name: (_sha_file(path) if path.is_file() else None) for name, path in sorted(DATA_FILES.items())}
    return {"library": lib.hexdigest(), "library_version": LIBRARY_VERSION,
            "conventions": _sha_file(registry.CONVENTIONS_PATH), "data": data,
            "eval_parser": dict(parse_back.load_eval_parser().pins), "tools": dict(tools),
            "emitters": {s: m.VERSION for s, m in sorted(registry.EMITTERS.items())}}


def dependencies() -> dict:
    """Fingerprint of everything besides the task's inputs that a render reads. Its library and tools/ entries are
    the code this process runs, which must still be the code on disk (ensure_library_current, loaded with the
    package; context.load_tools and ensure_tools_current, which also refuse a modified DEPENDENCY_FILES entry).
    render() and check() take it before building and compare it with the disk again before they conclude."""
    ensure_library_current()
    tools = context.load_tools()
    context.ensure_tools_current()
    return _fingerprint(tools)


def _moved(before: dict) -> list[str]:
    """What changed on disk since `before` was taken (empty: nothing), listed rather than raised: a dependency whose
    bytes differ now, library or tools/ code this process runs that the disk no longer holds, and a file of the tools/
    closure or of context.DEPENDENCY_FILES modified at all since the closure loaded."""
    now = _fingerprint(before.get("tools") or {})       # the tools/ entry is compared by context.tools_changed
    out = [f"{k}: changed during this run" for k in sorted(set(before) | set(now)) if before.get(k) != now.get(k)]
    out += [f"library {m}" for m in library_changed()]
    out += [f"tools/ {m}" for m in context.tools_changed()]
    return out


def record(res: Result, deps: dict, stale_outputs: dict | None = None) -> dict:
    counts = Counter(f"{op.table} {op.op}" for op in res.ops)
    return {
        "format": "hg-gen-build/1",
        "spec": {"path": f"{SPEC_DIR}/spec.json", "sha256": res.spec.sha256, "records": len(res.spec.records),
                 "texts": dict(sorted(res.resolver.texts.items()))},
        "inputs": dict(sorted(res.inputs.items())),
        "stale_outputs": dict(sorted((stale_outputs or {}).items())),
        "task": {"slug": res.spec.task["slug"], "revision": res.spec.task["revision"]},
        "context": {"context_hash": res.ctx["context_hash"], "universe": res.ctx["universe"]["key"],
                    "freeze_utc": res.ctx["freeze_utc"], "clock_utc": res.ctx["universe"]["clock_utc"]},
        "snapshot": res.base.fingerprint,
        "dependencies": deps,
        "conventions": res.conventions,
        "operations": dict(sorted(counts.items())),
        "outputs": {rel: _sha_bytes(data) for rel, data in sorted(res.files.items())},
        "early_warnings": _shown(res.early_warnings),
        "checks": {"after": len(res.resolver.after_checks), "cites": len(res.resolver.cite_checks)},
        "provenance": {k: v for k, v in provenance_report(res).items()
                       if k in ("origins", "uncited_fact_tokens", "claims", "verdict")},
        "validation": res.validation,
    }


def drift(previous: dict | None, deps: dict) -> dict:
    if not previous:
        return {}
    old = previous.get("dependencies") or {}
    return {k: {"pinned": old.get(k), "now": deps.get(k)} for k in sorted(set(old) | set(deps))
            if old.get(k) != deps.get(k)}


_OWNED = re.compile(r"^Working_Files/build/(provenance\.json|parts/[a-z][a-z0-9_]*\.sql)$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def previous_record(task_dir: Path) -> dict | None:
    """The last build record, refused unless it has the shape this library writes. Every output it lists must be one
    of the library's own output paths (provenance.json, parts/<service>.sql), spelled canonically, with a sha256: the
    record is what --prune deletes by, so a hand-edited record must not be able to point it at any other file."""
    data = output.read_bytes(Path(task_dir), RECORD)
    if data is None:
        return None
    start_over = f"remove {RECORD} to start over"
    try:
        rec = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise BuildError("build record", [f"{RECORD} is not UTF-8 JSON ({exc}); {start_over}"]) from None
    if not isinstance(rec, dict) or rec.get("format") != "hg-gen-build/1":
        raise BuildError("build record", [f"{RECORD} is not a hg-gen-build/1 record; {start_over}"])
    problems = []
    for section in ("outputs", "stale_outputs"):
        entries = rec.get(section) or {}
        if not isinstance(entries, dict):
            problems.append(f"{section} is not an object")
            continue
        problems += [f"{section}: {rel!r} is not an output this library writes, with its sha256"
                     for rel, sha in entries.items()
                     if not (isinstance(rel, str) and _OWNED.match(rel)
                             and isinstance(sha, str) and _SHA256.match(sha))]
    if not isinstance(rec.get("dependencies"), dict):
        problems.append("dependencies is not an object")
    if problems:
        raise BuildError("build record", [f"{RECORD}: {p}; {start_over}" for p in problems])
    return rec


def _owned(prev: dict | None) -> dict:
    """Files earlier builds wrote and still own: their outputs plus stale outputs not yet pruned."""
    prev = prev or {}
    return {**(prev.get("stale_outputs") or {}), **(prev.get("outputs") or {})}


def _record_bytes(res: Result, deps: dict, prev: dict | None) -> bytes:
    """The build record as the disk is now: an earlier output this build does not produce stays owned (stale_outputs)
    for as long as the file exists, so neither a render without --prune nor an interrupted prune forgets it."""
    stale = {}
    for rel, sha in sorted(_owned(prev).items()):
        if rel not in res.files and rel != RECORD and output.task_sha256(res.task_dir, rel) is not None:
            stale[rel] = sha
    return _json_bytes(record(res, deps, stale))


def _changes(res: Result, deps: dict) -> list[str]:
    """Everything that makes this run's record untrue (empty: nothing): an input, base export, manifest or the task
    context differing from what the build read, a dependency moved (_moved), and conventions read with other bytes
    than the record pins."""
    out = inputs_changed(res) + _moved(deps)
    if res.conventions_sha != deps.get("conventions"):
        out.append(f"conventions: the build read {res.conventions_sha[:12]}, the record pins "
                   f"{str(deps.get('conventions'))[:12]}")
    return out


def _settle(res: Result, deps: dict, consequence: str) -> None:
    """Raise unless everything the build read is still the same on disk (_changes)."""
    moved = _changes(res, deps)
    if moved:
        raise BuildError(f"inputs or dependencies changed during the render; {consequence}; run it again", moved)


def render(task_dir: Path, *, prune: bool = False, accept_upgrade: bool = False) -> dict:
    """Build, validate, then publish per file (write-if-changed); returns a report.

    Nothing is published when validation fails, when a pinned dependency drifted without --accept-upgrade, or when
    anything the build read changed before publication. Other processes' edits cannot be prevented, only detected, so
    the same check runs again after the outputs are replaced and after the build record is written: a change found
    there fails the render and leaves the record disagreeing with the disk, and `check` fails for as long as the two
    disagree (a disagreement that begins while a check runs is reported by the next one). Any exception raised once
    the outputs are published carries a note listing the files already published. Files are written through
    folder descriptors opened without following symlinks, and the lock pins the task folder's identity, so nothing is
    written into another task; a task folder replaced while files are being published stops the publication, and the
    error lists what was already written into the original folder. An accepted upgrade is logged just before the
    record is written, once: a render repeated after a failure in between does not log it again."""
    task_dir = Path(task_dir).resolve()          # the one resolution: lock, build and publish use this path
    with output.TaskLock(task_dir):
        prev = previous_record(task_dir)
        deps = dependencies()                # before anything is read; re-checked before publishing
        res = _build(task_dir)
        if res.task_dir != task_dir:
            raise BuildError("task folder", [f"built {res.task_dir}, locked {task_dir}"])
        val = validate(res)
        changed = drift(prev, deps)
        report = {"verdict": val["verdict"], "validation": val, "drift": changed, "changes": []}
        if val["verdict"] != "PASS":
            return report
        if changed and not accept_upgrade:
            report["verdict"] = "REFUSED"
            return report
        # Two steps: the outputs (and any pruning) first, then the build record written from the resulting disk, so
        # a failure in between leaves the previous record, which still owns everything it listed.
        written = ("new", "changed", "removed")
        published: list[str] = []
        try:                                    # once anything is published, every way out names it
            b = output.Build(task_dir, res.spec.sha256[:12])
            try:
                for rel in sorted(res.files):
                    b.add(rel, res.files[rel])
                for rel, data in res.files.items():
                    if b.staged_bytes(rel) != data:
                        raise output.PublishError(f"{rel}: staged bytes differ from the validated bytes")
                _settle(res, deps, "nothing published")
                changes = b.publish(prune=prune, previous=_owned(prev))
                published += [c.path for c in changes if c.status in written]
            finally:
                b.discard()
            _settle(res, deps, "the outputs were replaced but the build record was not, so `check` fails")
            if changed:                         # logged before the record, once (a repeated line is not added again)
                output.append_line(task_dir, UPGRADES,
                                   json.dumps({"spec_sha256": res.spec.sha256, "upgrades": changed},
                                              sort_keys=True, ensure_ascii=False), skip_if_last=True)
            rb = output.Build(task_dir, res.spec.sha256[:12] + "-record")
            try:
                rb.add(RECORD, _record_bytes(res, deps, prev))
                record_changes = rb.publish()
                published += [c.path for c in record_changes if c.status in written]
            finally:
                rb.discard()
            changes += record_changes
            _settle(res, deps, "the build record was written but no longer matches the disk, so `check` fails")
        except BaseException as exc:            # any kind, interrupts included: type and message kept, list added
            if published:
                exc.add_note(f"files already published: {published}")
            raise
        report["changes"] = [{"path": c.path, "status": c.status} for c in changes]
        return report


def check(task_dir: Path) -> dict:
    """Regenerate in memory and diff against the published files; never writes."""
    task_dir = Path(task_dir).resolve()
    prev = previous_record(task_dir)
    deps = dependencies()
    res = _build(task_dir)
    val = validate(res)
    files = dict(res.files)
    files[RECORD] = _record_bytes(res, deps, prev)
    changes = output.check(task_dir, files, _owned(prev))
    stale = [{"path": c.path, "status": c.status} for c in changes if c.status != "unchanged"]
    changed = drift(prev, deps)
    moved = _changes(res, deps)          # something edited while this check ran: its verdict would be stale
    ok = val["verdict"] == "PASS" and not stale and not changed and not moved
    return {"verdict": "PASS" if ok else "FAIL", "validation": val, "drift": changed, "stale": stale,
            "inputs_changed": moved}
