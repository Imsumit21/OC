#!/usr/bin/env python3
"""Render a task's injection parts from its spec, validate them independently, publish only what changed.

  python3 Task_Authoring/generators/render.py validate   --task-dir T     context, spec, provenance, census, render in
                                                                         memory and every independent check; no writes
  python3 Task_Authoring/generators/render.py render     --task-dir T [--prune] [--accept-upgrade]
  python3 Task_Authoring/generators/render.py check      --task-dir T     regenerate in memory, diff with the published
                                                                         files and the pinned dependencies; no writes
  python3 Task_Authoring/generators/render.py parse-back --task-dir T [--sql P]
                                                                         grammar, eval-tokenizer parse, ordered compare
                                                                         with the spec, overlay, invariants, sql_lint;
                                                                         --sql checks another file (e.g. the assembled
                                                                         01_Universe_Inject.sql; a relative path is
                                                                         taken under T) for this spec's services
  python3 Task_Authoring/generators/render.py provenance --task-dir T     coverage, origins, fan-out, chronology, claims
  python3 Task_Authoring/generators/render.py explain    --task-dir T --row linear.linear_comments:<id>
  python3 Task_Authoring/generators/render.py store-revision --task-dir T --rev rev4 [--source 01_Universe_Inject.sql]
  python3 Task_Authoring/generators/render.py --self-test

Inputs: <T>/00_Assigments.md (V3 context, recomputed every run) and <T>/Working_Files/spec/ (spec.json + texts/).
Outputs: <T>/Working_Files/build/ (parts/<service>.sql, provenance.json, build_record.json). SQL is never executed.
--json keeps JSON on stdout and messages on stderr. Exit codes: 0 PASS, 1 FAIL or refused, 2 usage or setup error.
"""
from __future__ import annotations

import argparse
import json
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.pycache_prefix = "/dev/null/generators-no-bytecode"     # context.NO_BYTECODE: no __pycache__ is read or written
LIB = Path(__file__).resolve().parent
TA = LIB.parent
if str(TA) not in sys.path:
    sys.path.insert(0, str(TA))

import generators  # noqa: E402

generators.pin_script(__file__)                 # this script is part of the library hash; Python compiled it itself
from generators.core import context, output, pipeline  # noqa: E402
from generators.core.values import SpecError  # noqa: E402
from generators.services import registry  # noqa: E402


def _emit(obj, as_json: bool, text: str) -> None:
    if as_json:
        print(json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False, default=str))
    else:
        print(text)


def _validation_text(val: dict) -> str:
    lines = [f"verdict: {val['verdict']}", f"grammar: {len(val['grammar'])} problem(s)",
             f"parse-back: {val['parse_back']}", f"column types: {len(val.get('types', []))} problem(s)",
             f"compare: {len(val['compare'])} difference(s)", f"overlay: {len(val['overlay'])} error(s)"]
    for sev in ("FAIL", "WARN"):
        for rule, info in (val.get("invariants", {}).get(sev) or {}).items():
            lines.append(f"invariant {rule} {sev}: {info['count']}" + (f" — {info['first'][0]}" if info["first"] else ""))
    agree = val.get("agreement")
    if agree:
        lines.append(f"parser agreement: {agree['count']} value(s) local tools read differently (E'' escapes)")
        lines += [f"  {m}" for m in agree["first"]]
    lint = val.get("sql_lint") or {}
    if lint:
        lines.append(f"sql_lint: {lint['errors']['count']} error(s), {lint['warnings']['count']} warning(s)")
        lines += [f"  {m}" for m in lint["errors"]["first"]]
    for key in ("grammar", "types", "compare", "overlay"):
        lines += [f"  {key}: {m}" for m in val.get(key, [])[:pipeline.SHOW]]
    return "\n".join(lines)


def cmd_validate(args) -> int:
    res = pipeline.build(args.task_dir)
    val = pipeline.validate(res)
    report = {"validation": val, "operations": len(res.ops), "early_warnings": res.early_warnings,
              "conventions": res.conventions}
    _emit(report, args.json, _validation_text(val) + f"\noperations: {len(res.ops)}"
          + f"\nearly warnings: {len(res.early_warnings)}")
    return 0 if val["verdict"] == "PASS" else 1


def cmd_render(args) -> int:
    rep = pipeline.render(args.task_dir, prune=args.prune, accept_upgrade=args.accept_upgrade)
    text = _validation_text(rep["validation"])
    if rep["drift"]:
        text += "\npinned dependencies changed: " + ", ".join(rep["drift"])
        if rep["verdict"] == "REFUSED":
            text += "\nREFUSED: re-run with --accept-upgrade to record the upgrade"
    text += "".join(f"\n{c['status']:9} {c['path']}" for c in rep["changes"])
    _emit(rep, args.json, text)
    return 0 if rep["verdict"] == "PASS" else 1


def cmd_check(args) -> int:
    rep = pipeline.check(args.task_dir)
    text = _validation_text(rep["validation"]) + "".join(f"\n{s['status']:9} {s['path']}" for s in rep["stale"])
    if rep["drift"]:
        text += "\npinned dependencies changed: " + ", ".join(rep["drift"])
    if rep["inputs_changed"]:
        text += "\ninputs changed while checking: " + "; ".join(rep["inputs_changed"])
    text += f"\ncheck: {rep['verdict']}"
    _emit(rep, args.json, text)
    return 0 if rep["verdict"] == "PASS" else 1


def cmd_parse_back(args) -> int:
    res = pipeline.build(args.task_dir)
    if args.sql:
        path = Path(args.sql)
        path = path if path.is_absolute() else res.task_dir / path     # a relative --sql is taken under the task
        sql = path.read_bytes().decode("utf-8")                         # exact bytes: no newline translation
        val = pipeline.validate(res, sql, foreign=True)
    else:
        parts = {s: output.read_bytes(res.task_dir, pipeline.part_path(s)) for s in sorted(res.parts)}
        missing = [pipeline.part_path(s) for s, data in parts.items() if data is None]
        if missing:
            print(f"no published part {missing}; run render first", file=sys.stderr)
            return 1
        val = pipeline.validate(res, pipeline.emitter.render_full([], [d.decode("utf-8") for d in parts.values()]))
    _emit(val, args.json, _validation_text(val))
    return 0 if val["verdict"] == "PASS" else 1


def cmd_provenance(args) -> int:
    res = pipeline.build(args.task_dir)
    rep = pipeline.provenance_report(res)
    text = "\n".join([f"operations: {rep['operations']}", f"origins: {rep['origins']}",
                      f"columns without provenance: {len(rep['columns_without_provenance'])}",
                      f"base values used more than once: {len(rep['base_fanout'])}",
                      f"after checks: {rep['after_checks']}  cites checks: {rep['cite_checks']}  texts: {rep['texts']}",
                      f"claims: {rep['claims'] or 'none'}",
                      f"un-cited fact-like tokens (heuristic): {rep['uncited_fact_tokens']['count']}",
                      "conventions: " + ", ".join(f"{c['id']} ({c['status']})" for c in rep["conventions"]),
                      f"verdict: {rep['verdict']}"])
    _emit(rep, args.json, text)
    return 0 if rep["verdict"] == "PASS" else 1


def cmd_explain(args) -> int:
    table, _, key = args.row.partition(":")
    if not table or not key:
        print("--row must be <schema.table>:<key>", file=sys.stderr)
        return 2
    res = pipeline.build(args.task_dir)
    hits = []
    for op in res.ops:
        mod = registry.EMITTERS.get(op.table.split(".")[0])
        k = ":".join(str(v) for v in (mod.key_of(op) if mod else ()))
        if op.table == table and k == key:
            prov = dict(op.prov)
            hits.append({"table": op.table, "op": op.op, "record": op.record,
                         "columns": [{"column": c, "value": v, "provenance": prov.get(c)} for c, v in op.cols],
                         "where": [{"column": c, "value": v} for c, v in op.where]})
    if not hits:
        print(f"no operation on {table} with key {key}", file=sys.stderr)
        return 1
    text = []
    for h in hits:
        text.append(f"{h['op'].upper()} {h['table']} (record {h['record'] or 'derived'})")
        for c in h["columns"]:
            prov = json.dumps(c["provenance"], sort_keys=True, default=str)
            text.append(f"  {c['column']} = {c['value']!r}\n      {prov}")
    _emit(hits, args.json, "\n".join(text))
    return 0


def cmd_store_revision(args) -> int:
    task = Path(args.task_dir).resolve()
    with output.TaskLock(task):
        ch = output.store_revision(task, args.rev, args.source)
    _emit({"path": ch.path, "status": ch.status, "sha256": ch.sha256_new}, args.json, f"{ch.status:9} {ch.path}")
    return 0


def self_test() -> int:
    suite = unittest.defaultTestLoader.discover(start_dir=str(LIB / "tests"), pattern="test_*.py",
                                                top_level_dir=str(TA))
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
    ok = result.wasSuccessful()
    print(f"SELF-TEST {'PASS' if ok else 'FAIL'} ({result.testsRun} tests)")
    return 0 if ok else 1


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--self-test" in argv:
        return self_test()
    ap = argparse.ArgumentParser(prog="render.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    cmds = {"validate": cmd_validate, "render": cmd_render, "check": cmd_check, "parse-back": cmd_parse_back,
            "provenance": cmd_provenance, "explain": cmd_explain, "store-revision": cmd_store_revision}
    for name in cmds:
        sp = sub.add_parser(name)
        sp.add_argument("--task-dir", required=True, type=Path)
        sp.add_argument("--json", action="store_true")
        if name == "render":
            sp.add_argument("--prune", action="store_true")
            sp.add_argument("--accept-upgrade", action="store_true")
        if name == "parse-back":
            sp.add_argument("--sql")
        if name == "explain":
            sp.add_argument("--row", required=True)
        if name == "store-revision":
            sp.add_argument("--rev", required=True)
            sp.add_argument("--source", default="01_Universe_Inject.sql")
    args = ap.parse_args(argv)
    try:
        return cmds[args.cmd](args)
    except SpecError as exc:
        print(f"SPEC FAIL: {exc}", file=sys.stderr)
        return _notes(exc, 1)
    except pipeline.BuildError as exc:
        print(f"BUILD FAIL ({exc.stage}):", file=sys.stderr)
        for p in exc.problems[:50]:
            print(f"  {p}", file=sys.stderr)
        return _notes(exc, 1)
    except output.PublishError as exc:
        print(f"PUBLISH FAIL: {exc}", file=sys.stderr)
        return _notes(exc, 1)
    except context.ToolsChanged as exc:
        print(f"TOOLS CHANGED: {exc}", file=sys.stderr)
        return _notes(exc, 1)
    except generators.LibraryChanged as exc:
        print(f"LIBRARY CHANGED: {exc}", file=sys.stderr)
        return _notes(exc, 1)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return _notes(exc, 2)


def _notes(exc: BaseException, code: int) -> int:
    """Print the notes an error carries (render adds the files it had already published) and return `code`."""
    for note in getattr(exc, "__notes__", ()):
        print(f"  {note}", file=sys.stderr)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
