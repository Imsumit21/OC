#!/usr/bin/env python3
"""Build the surface-format fixtures (G1, 2026-10-25): the minimal write payloads of all 12 Season Pass runs (revision
13: the pre-check and runs 1-6; revision 14: the pre-check and runs 1, 2, 3 and 6), each with the slot results its
full trajectory gets, so surface_grader's self-test re-grades every register, tracker and delivery format the
platform runs produced.

Read-only on the frozen copies (support/backtests/season_pass/rev13 and rev14; both SHA256SUMS are verified first).
Writes only this folder. Never executes SQL: the revision-14 truth comes from the frozen oracle imported as a library
(rev14/README.md, "Safe use"); the revision-13 truth is the frozen hardening_rev12/truth.after.json.

Before writing anything, two checks must hold:
  1. the full-run grades match the grades of record: revision 13 rev13/reference/proxy_scores.json (every slot and
     the score), revision 14 the failed-slot sets of rev14/README.md;
  2. each minimal fixture grades exactly like its full run, slot by slot.

A fixture keeps every call of the write tools the grader reads (KEEP), failed ones included, with its input as
written and its result cut to the fields the decoder reads (RESULT_KEYS); events keep their original numbers.

Usage (workspace root): python3 -B Task_Authoring/support/fixtures/surface_formats/build_fixtures.py [--check]
  --check   rebuild in memory and compare with the files here; writes nothing
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parents[2]
S = BUNDLE / "support" / "backtests" / "season_pass"
sys.path.insert(0, str(BUNDLE / "tools"))
import gradable_surface as gs  # noqa: E402
import surface_grader as sg  # noqa: E402
import trajectory_ledger as tl  # noqa: E402

VERSION = "surface_formats/1"
KEEP = ("gdrive_create_file", "gdrive_update_file", "gdrive_move_file", "gdrive_share_file",
        "gsheets_create_spreadsheet", "gsheets_values_update", "gsheets_values_append", "gsheets_values_batch_update",
        "linear_update_issue", "gslides_batch_update", "gmail_reply_to_message", "gmail_send_message",
        "slack_send_message", "slack_conversations_add_message")
RESULT_KEYS = ("id", "spreadsheetId", "error", "ok")
REVISIONS = {
    "rev13": {"surface": BUNDLE / "support/fixtures/season_pass_rev13/Working_Files/01_Gradable_Surface.json",
              "truth": S / "rev13/working_files/hardening_rev12/truth.after.json",
              "runs": [("precheck", "rev13/runs/06_PreCheck_Trajectory/trajectory-run-1.json")]
              + [(f"run-{i}", f"rev13/runs/07_Baseline_Trajectories/trajectory-run-{i}.json") for i in range(1, 7)]},
    "rev14": {"surface": S / "rev14/working_files/01_Gradable_Surface.json",
              "oracle": S / "rev14/working_files/hardening_rev14", "sql": S / "rev14/sql/01_Universe_Inject.sql",
              "runs": [("pre", "rev14/runs/06_PreCheck_Trajectory/trajectory-run-1.json")]
              + [(f"r{i}", f"rev14/runs/07_Baseline_Trajectories/trajectory-run-{i}.json") for i in (1, 2, 3, 6)]}}
REV14_RECORD = {"pre": ["S04", "S05", "S07", "S08", "S40"], "r1": ["S43", "S46", "S47", "S52"],
                "r2": ["S04", "S05", "S07", "S08"] + [f"S{i}" for i in range(38, 47)],
                "r3": ["S01", "S47", "S49", "S52", "S54"], "r6": ["S01"]}      # rev14/README.md, grades of record


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def rel(path: Path) -> str:
    return str(Path(path).resolve().relative_to(BUNDLE))


def verify_frozen() -> None:
    for rev in ("rev13", "rev14"):
        root = S / rev
        bad, n = [], 0
        for line in (root / "SHA256SUMS").read_text().splitlines():
            if not line.strip():
                continue
            want, name = line.split(None, 1)
            n += 1
            if sha256(root / name.strip().lstrip("*")) != want:
                bad.append(name.strip())
        if bad:
            raise SystemExit(f"{rev}: SHA256SUMS does not verify: {bad[:5]}")
        print(f"{rev} SHA256SUMS: {n} files verified")


def minimal(run: tl.Run) -> list:
    out = []
    for c in run.calls:
        if tl.short(c["name"]) not in KEEP:
            continue
        r = run.results.get(c["id"])
        item = {"type": "tool_use", "event": c["event"] + 1, "id": c["id"], "name": c["name"], "input": c["input"],
                "parent_tool_use_id": c["parent"], "result": {}}
        if r is not None:
            data = r.get("data")
            if isinstance(data, dict):
                data = {k: data[k] for k in RESULT_KEYS if k in data}
            elif data is not None:
                data = str(data)[:160]
            item["result"] = {"event": r["event"] + 1 if isinstance(r.get("event"), int) else None,
                              "error": bool(r.get("error")), "data": data}
        out.append(item)
    return out


def formats(run: tl.Run, d: dict) -> dict:
    """The formats a run exercises, for the README table and the coverage line of the self-test."""
    shapes = set()
    for c in d["tracker_updates"]:
        q, p = c["input"], sg._patch(c["input"])
        parts = (["description"] if q.get("description") is not None else []) \
            + ([f"patch:{type(p).__name__}"] if q.get("patch") is not None else []) \
            + (["state"] if q.get("state") or q.get("stateId") else [])
        shapes.add("+".join(parts) or "other")
    kept = [c for c in run.calls if tl.short(c["name"]) in KEEP]
    t = d["table"]
    return {"register": t["kind"], "register_candidates": [f"{c['kind']}:{c.get('rows')}" for c in t["candidates"]],
            "csv_base64": t["meta"].get("event") is not None and any(c.get("base64") for c in t["candidates"]
                                                                       if c.get("event") == t["meta"].get("event")),
            "appended_rows": t["meta"].get("appended_rows"), "tracker_updates": len(d["tracker_updates"]),
            "tracker_update_shapes": sorted(shapes),
            "slack_tools": sorted({tl.short(c["name"]) for c in kept if tl.short(c["name"]).startswith("slack_")
                                   and not tl.failed(run.results.get(c["id"]))}),
            "moved": bool(d["writes"].get("gdrive_move_file")),
            "failed_write_calls": sum(1 for c in kept if tl.failed(run.results.get(c["id"])))}


def score(surface: dict, res: dict) -> float:
    w = {s["id"]: s["weight"] for s in surface["slots"]}
    return round(sum(w[k] for k, v in res.items() if v) / sum(w.values()), 6)


def build() -> dict:
    """{file name: bytes} for every file this folder holds (README.md and this script aside)."""
    verify_frozen()
    files, manifest = {}, {"kind": "SURFACE_FORMAT_FIXTURES", "version": VERSION, "built_by": rel(Path(__file__)),
                           "rule": "each fixture keeps every call of the write tools the grader reads (failed ones "
                                   "included) with its input as written and its result cut to " + ", ".join(RESULT_KEYS)
                                   + "; expected results are the full run's, checked against the grades of record",
                           "keep_tools": list(KEEP), "revisions": {}, "fixtures": []}
    for rev, spec in REVISIONS.items():
        files[f"{rev}_surface.json"] = spec["surface"].read_bytes()
        surface = gs.load(spec["surface"])
        if rev == "rev13":
            files[f"{rev}_truth.json"] = spec["truth"].read_bytes()
            truth_source = {"truth": rel(spec["truth"]), "sha256": sha256(spec["truth"])}
        else:
            rows, prov = sg.load_truth(None, None, spec["oracle"], spec["sql"])
            files[f"{rev}_truth.json"] = (json.dumps(json.loads(json.dumps(rows)), indent=1, ensure_ascii=False)
                                          + "\n").encode()
            truth_source = {"oracle": rel(spec["oracle"] / "oracle.py"), "oracle_sha256": sha256(spec["oracle"] / "oracle.py"),
                            "sql": rel(spec["sql"]), "sql_sha256": sha256(spec["sql"]), "call": "solve(sql, new=True)"}
        truth = json.loads(files[f"{rev}_truth.json"])
        manifest["revisions"][rev] = {"surface": f"{rev}_surface.json", "surface_source": rel(spec["surface"]),
                                      "surface_sha256": sha256(spec["surface"]), "truth": f"{rev}_truth.json",
                                      "truth_source": truth_source,
                                      "truth_sha256": hashlib.sha256(files[f"{rev}_truth.json"]).hexdigest()}
        ref = json.loads((S / "rev13/reference/proxy_scores.json").read_text()) if rev == "rev13" else None
        for label, source in spec["runs"]:
            path = S / source
            run = tl.load(path, label)
            d = sg.decode(run, surface)
            res = sg.grade(surface, truth, d)
            failed = [k for k, v in res.items() if v is False]
            if any(v is None for v in res.values()):
                raise SystemExit(f"{rev} {label}: UNGRADED slots in a full run: {[k for k, v in res.items() if v is None]}")
            if ref is not None:                       # check 1, revision 13: every slot and the score of record
                diffs = [k for k in res if bool(ref[label]["results"].get(k)) != res[k]]
                if diffs or round(score(surface, res), 6) != round(ref[label]["score"], 6):
                    raise SystemExit(f"{rev} {label}: differs from proxy_scores.json: {diffs[:8]}")
            elif failed != REV14_RECORD[label]:      # check 1, revision 14: the failed-slot set of record
                raise SystemExit(f"{rev} {label}: failed {failed}, grades of record {REV14_RECORD[label]}")
            items = minimal(run)
            name = f"{rev}_{label}.calls.json"
            files[name] = (json.dumps(items, indent=1, ensure_ascii=False) + "\n").encode()
            mrun = tl.Run(label, HERE / name, "derived-calls", None, *_index(items))
            mres = sg.grade(surface, truth, sg.decode(mrun, surface))
            if mres != res:                           # check 2: the minimal payloads grade like the full run
                raise SystemExit(f"{rev} {label}: the minimal fixture grades differently: "
                                 f"{[k for k in res if mres.get(k) != res[k]][:8]}")
            manifest["fixtures"].append({"revision": rev, "label": label, "file": name,
                                         "sha256": hashlib.sha256(files[name]).hexdigest(), "source": rel(path),
                                         "source_sha256": sha256(path), "calls_kept": len(items),
                                         "score": score(surface, res), "failed_slots": failed, "results": res,
                                         "formats": formats(run, d)})
            print(f"{rev} {label}: {len(items)} calls kept, {len(files[name]) // 1024} KB, score "
                  f"{score(surface, res):.1%}, failed {failed}")
    files["MANIFEST.json"] = (json.dumps(manifest, indent=1, ensure_ascii=False) + "\n").encode()
    return files


def _index(items: list) -> tuple:
    """(calls, results) of a derived-calls list, exactly as trajectory_ledger.load() reads the file."""
    calls, results = [], {}
    for c in items:
        calls.append({"event": c["event"] - 1, "event_1b": c["event"], "id": c["id"], "name": c["name"],
                      "input": c["input"] or {}, "model": None, "parent": c["parent_tool_use_id"], "context": "unknown"})
        r = c["result"]
        if r:
            results[c["id"]] = {"event": r["event"] - 1 if isinstance(r.get("event"), int) else None,
                                "event_1b": r.get("event"), "error": r.get("error", False), "data": r.get("data")}
    return calls, results


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="build_fixtures.py", description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild in memory and compare; write nothing")
    a = ap.parse_args(argv)
    if not sys.dont_write_bytecode:
        print("build_fixtures: run with python3 -B (the frozen oracle must not get a __pycache__)", file=sys.stderr)
        return 2
    files = build()
    if a.check:
        diffs = [n for n, b in files.items() if not (HERE / n).is_file() or (HERE / n).read_bytes() != b]
        extra = sorted(p.name for p in HERE.iterdir() if p.is_file() and p.name not in files
                       and p.name not in ("README.md", Path(__file__).name))
        print(f"check: {len(files)} file(s) rebuilt; {len(diffs)} differ {diffs}; unexpected files {extra}")
        return 1 if diffs or extra else 0
    for n, b in files.items():
        (HERE / n).write_bytes(b)
    print(f"wrote {len(files)} file(s) to {rel(HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
