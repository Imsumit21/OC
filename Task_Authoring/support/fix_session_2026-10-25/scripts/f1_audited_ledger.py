#!/usr/bin/env python3
"""Build the session-local, audited F1 provenance ledger from F1_PROVENANCE_AUDIT.txt.

The audit file is the record of the real `node_verdicts.py` rows the F1 provenance pools were read from. It holds 35
JSON lines and 28 unique records: 13 control, 5 channel, 10 verdict (the `== family tool_surface` section repeats the
five `tool_surface:register` channel rows, and two of the three r6 control rows are byte-identical). This builder keeps
the two kinds `hardness_forecast.channel_rate()` pools -- `control` and `channel` -- and writes 18 JSONL records
(13 control + 5 channel) that the forecast CLI can read through `--ledger`. Nothing is appended to
support/hardness_ledger/ledger.jsonl. (The task brief said "26 records"; the current audit file does not contain 26
unique records, and no row is dropped to reach that number. The eligible pools are unaffected: see --check.)

Fidelity choices, all visible in the output:
  - `model`, `run`, `revision`, `family`, `verdict`, `features.mixed_model` and channel `counts` are copied verbatim.
  - `features.mixed_model` is false only on the five r3 rows (the eligible pool); every other row carries true, so
    `channel_rate()` excludes it unless `--include-mixed`. This is the audit's own distinction, not a new filter.
  - a control row carries one member trial: `counts = {"unit": "member", "n": 1, "failed": <OVER-APPLIED>}`. The audit
    does not say which control member (SP-110/SP-119/SP-123) a row is, so no `key` is invented.
  - ids are `f1aud_<sha256 prefix>` over the row's identity plus its deciding event; they are session-local and are
    not real ledger ids (the real ledger is never touched).

Usage (workspace root):
  python3 -B Task_Authoring/support/fix_session_2026-10-25/scripts/f1_audited_ledger.py [--check]
  python3 -B .../f1_audited_ledger.py --audit PATH --out PATH [--report]
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

B = Path(__file__).resolve().parents[3]
S = B / "support" / "fix_session_2026-10-25" / "f1_acceptance"
AUDIT = S / "F1_PROVENANCE_AUDIT.txt"
OUT = S / "F1_AUDITED_LEDGER.jsonl"
MODEL = "claude-opus-4-8"
RUN_ORDER = {"pre": 0, "r1": 1, "r2": 2, "r3": 3, "r6": 4}


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def read_audit(path=AUDIT) -> dict:
    """{'unique': [...], 'lines': n, 'duplicates': n, 'kept': [...], 'ignored_kinds': {...}} from the audit text."""
    rows, seen, lines, duplicates = [], set(), 0, 0
    for ln in Path(path).read_text().splitlines():
        if not ln.startswith("{"):
            continue
        lines += 1
        rec = json.loads(ln)
        key = canonical(rec)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        rows.append(rec)
    kept = [r for r in rows if r["kind"] in ("control", "channel")]
    ignored = {}
    for r in rows:
        if r["kind"] not in ("control", "channel"):
            ignored[r["kind"]] = ignored.get(r["kind"], 0) + 1
    return {"unique": rows, "lines": lines, "duplicates": duplicates, "kept": kept, "ignored_kinds": ignored}


def _id(rec) -> str:
    ident = {k: rec.get(k) for k in ("kind", "task", "revision", "run", "node", "family", "model", "verdict", "counts")}
    ident["event"] = (rec.get("evidence") or {}).get("deciding_event")
    return "f1aud_" + hashlib.sha256(canonical(ident).encode()).hexdigest()[:16]


def to_ledger(rec: dict) -> dict:
    """One audit row as a ledger record. Control rows get the member unit explicit; channel counts are copied."""
    out = {
        "id": _id(rec),
        "kind": rec["kind"],
        "task": "season_pass",
        "revision": rec.get("revision") or "rev14",
        "run": rec.get("run"),
        "node": rec.get("node"),
        "family": rec.get("family"),
        "model": rec.get("model"),
        "verdict": rec.get("verdict"),
        "counts": rec.get("counts"),
        "features": dict(rec.get("features") or {}),
        "evidence": rec.get("evidence") or {},
        "source": "platform-baseline",
        "epistemic": "derived",
        "harness": {"name": "node_verdicts", "version": "1"},
        "audit": "F1_PROVENANCE_AUDIT.txt",
    }
    if rec["kind"] == "control":
        if rec.get("verdict") not in ("HELD", "OVER-APPLIED"):
            raise ValueError(f"control row {rec.get('run')} has verdict {rec.get('verdict')!r}")
        out["counts"] = {"unit": "member", "n": 1, "failed": int(rec["verdict"] == "OVER-APPLIED")}
        out["features"]["member_key_unrecorded"] = True       # the audit row names no control member; no key invented
    elif rec["kind"] == "channel":
        c = rec.get("counts") or {}
        if (c.get("unit") or "run") != "run" or int(c.get("n", 1)) != 1:
            raise ValueError(f"channel row {rec.get('run')}: unexpected counts {c}")
    return out


def records(audit=AUDIT) -> tuple:
    """(ledger records sorted, audit summary)."""
    a = read_audit(audit)
    recs = [to_ledger(r) for r in a["kept"]]
    recs.sort(key=lambda r: (RUN_ORDER.get(r["run"], 9), r["kind"], r["node"], r["id"]))
    ids = [r["id"] for r in recs]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate ledger ids while building the audited ledger")
    a["written"] = len(recs)
    a.pop("unique")
    a.pop("kept")
    return recs, a


def build(out=OUT, audit=AUDIT) -> dict:
    """Write the JSONL ledger and return {'path', 'sha256', 'written', 'lines', 'duplicates', 'ignored_kinds'}."""
    recs, a = records(audit)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(canonical(r) for r in recs) + "\n"
    out.write_text(text)
    return {"path": str(out), "sha256": hashlib.sha256(out.read_bytes()).hexdigest(), "written": len(recs),
            "lines": a["lines"], "duplicates": a["duplicates"], "ignored_kinds": a["ignored_kinds"],
            "audit": str(audit)}


# ------------------------------------------------------------------ pool report (consistency only, never validation)

CHANNELS = (("control:process_findings", "control", "A15"),
            ("tool_surface:register", "tool_surface", "tool_surface"),
            ("scale:groups", "scale", "scale"))
FORMER_OVERRIDES = {"control:process_findings": "1,13", "tool_surface:register": "3,3", "scale:groups": "4,266"}


def _beta(rate) -> dict | None:
    if not rate:
        return None
    return {"alpha": rate.get("alpha"), "beta": rate.get("beta"), "mean": rate.get("mean"),
            "n": rate.get("n"), "f": rate.get("f"), "unit": rate.get("unit"),
            "records": rate.get("records"), "dropped": rate.get("dropped") or []}


def report(ledger_path=OUT) -> list:
    """Per channel: the ledger pool, the former disclosed override and the Beta the run would use."""
    sys.path.insert(0, str(B / "tools"))
    import hardness_forecast as hf
    import hardness_ledger as hl
    led = hl.Ledger(ledger_path)
    out = []
    for cid, kind, family in CHANNELS:
        pooled = hf.channel_rate(led, MODEL, cid, kind, family, {})
        if pooled and pooled.get("alpha") is None:            # UNPARAMETERIZED: no eligible record after exclusions
            pooled = None
        try:
            override = hf.parse_rate(f"{cid}={FORMER_OVERRIDES[cid]}@former disclosed override")[1]
        except Exception:                                     # noqa: BLE001 - display only
            override = None
        out.append({"channel": cid, "kind": kind, "family": family, "ledger": _beta(pooled),
                    "former_override": _beta(override),
                    "used": "ledger" if pooled else ("former override" if override else "UNPARAMETERIZED"),
                    "used_beta": _beta(pooled or override)})
    return out


def print_report(rows) -> None:
    print("F1 provenance pools (session-local audited ledger; pools are IN-SAMPLE: r3 is one of the judged baselines)")
    for r in rows:
        led = r["ledger"]
        led_s = (f"Beta({led['alpha']:g},{led['beta']:g}) mean {led['mean']:.4f} n={led['n']} f={led['f']} "
                 f"[{led['unit']}; dropped {len(led['dropped'])}]" if led else "none (no eligible record)")
        ov = r["former_override"]
        ov_s = f"Beta({ov['alpha']:g},{ov['beta']:g}) mean {ov['mean']:.4f}" if ov else "none"
        used = r["used_beta"]
        used_s = f"Beta({used['alpha']:g},{used['beta']:g}) mean {used['mean']:.4f}" if used else "UNPARAMETERIZED"
        print(f"  {r['channel']:26} ledger-pooled {led_s} | former override {ov_s} | used {r['used']}: {used_s}")
    print("  'dropped' lists the records that would otherwise be this channel's trials but were excluded (mixed model "
          "or not a trial); it is channel-scoped (kind + family).")
    print("  consistency check, not validation: every pool is in-sample (r3 is one of the judged baselines).")


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="f1_audited_ledger.py")
    ap.add_argument("--audit", type=Path, default=AUDIT)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--check", action="store_true", help="refuse unless the pools are Beta(1,4) and Beta(2,1)")
    a = ap.parse_args(argv)
    info = build(a.out, a.audit)
    print(json.dumps(info, indent=1))
    rows = report(a.out)
    print_report(rows)
    if a.check:
        got = {r["channel"]: ((round(r["ledger"]["alpha"], 6), round(r["ledger"]["beta"], 6))
                              if r["ledger"] else None) for r in rows}
        want = {"control:process_findings": (1.0, 4.0), "tool_surface:register": (2.0, 1.0), "scale:groups": None}
        if got != want:
            print(f"AUDIT FAIL: pools {got} != expected {want}", file=sys.stderr)
            return 1
        print("AUDIT OK: control:process_findings Beta(1,4); tool_surface:register Beta(2,1); scale:groups none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
