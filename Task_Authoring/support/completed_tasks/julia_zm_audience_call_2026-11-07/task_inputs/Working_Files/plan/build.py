"""Assemble 01_Universe_Inject.sql from the per-service emitters. Run: python3 build.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import emitters as E

OUT = pathlib.Path(__file__).resolve().parents[2] / "01_Universe_Inject.sql"
parts, counts = [], {}
for name, fn in E.SERVICES:
    st = fn()
    counts[name] = st
    parts += st
ins = sum(1 for v in counts.values() for s in v if s.startswith("INSERT"))
upd = sum(1 for v in counts.values() for s in v if s.startswith("UPDATE"))
# Requester asked for comment-free SQL (2026-11-08). Line 1 stays: sql_lint.py requires the marker.
head = ["-- Are you planning to inject? Yes", "BEGIN;"]
body = parts + ["COMMIT;", ""]
OUT.write_text("\n".join(head + body), encoding="utf8", newline="\n")
CLEAN = pathlib.Path(__file__).resolve().parents[1] / "01_Universe_Inject.clean.sql"
CLEAN.write_text("\n".join(["BEGIN;"] + body), encoding="utf8", newline="\n")
print(OUT, {k.lower(): len(v) for k, v in counts.items()}, "insert", ins, "update", upd)
