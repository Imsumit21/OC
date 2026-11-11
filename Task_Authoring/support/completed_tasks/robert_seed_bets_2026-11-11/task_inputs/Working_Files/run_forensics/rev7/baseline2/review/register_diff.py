#!/usr/bin/env python3
"""Hand-style register diff: each run's final sheet rows against solver/truth.json, joined on the bank-name text.

The proxy tools join rows on the payee label, which every run wrote as free text, so they read all 22 rows as
missing. This joins on the Name-on-the-bank cell (or the label) with one pattern per payee and compares amounts as
numbers. Build and Marketing payees are compared per bet column; Company payees on the Company column (truth keeps a
by-bet allocation for them that the method does not ask the sheet to show). Output: one line per difference.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TRUTH = json.loads((HERE.parents[3] / "Working_Files/solver/truth.json").read_text())
PAT = {"Deel": r"Deel", "Leapblock": r"Leapblock", "Eveline Art": r"Eveline", "Adjoe": r"Adjoe", "MotMot": r"BANCO",
       "Singular": r"Singular", "Node Media": r"4419", "TYZ Law Group": r"TYZ", "Trademark lawyer": r"7200|7393",
       "Lucas": r"36400|6577", "AppLovin": r"AppLovin", "Graham Porter": r"Graham", "JPMorgan": r"JPMorgan|3203",
       "Creative X": r"CREATIVE X", "JP (website)": r"0056|4020", "Nathan Price": r"Nathan", "Martin Walsh": r"7250|Walsh",
       "Lauren Brooks": r"7249|Brooks", "Ozhan": r"6074|16238|3307", "UX contractor": r"9100|1876", "4X helper": r"0131|3139",
       "Oleg": r"43315|9368"}
COLS = ["Domino Delights", "ZM", "Combo Fighter"]


def num(cell):
    if cell is None or str(cell).strip() in ("", "-", "—", "–"):
        return 0.0
    m = re.search(r"-?[\d,]+(?:\.\d+)?", str(cell))
    return float(m.group(0).replace(",", "")) if m else None


def sheet_rows(run):
    rows = {}
    for w in json.loads((HERE / run / "writes.json").read_text()):
        if not w["tool"].startswith("gsheets_values"):
            continue
        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "values" and isinstance(v, list) and v and isinstance(v[0], list):
                        yield v
                    else:
                        yield from walk(v)
            elif isinstance(o, list):
                for x in o:
                    yield from walk(x)
        for values in walk(w):
            for r in values:
                if len(r) >= 4:
                    rows[(str(r[0]), str(r[1]))] = (w["event"], [str(c) for c in r])
    return rows


def main(run):
    rows = sheet_rows(run)
    out = []
    for key, pat in PAT.items():
        t = TRUTH.get(key)
        hits = [(ev, r) for (a, b), (ev, r) in rows.items() if re.search(pat, a + " " + b)
                and not re.search(r"(?i)^(build|marketing|company|total|brought|cost to build|scope|how|basis|source|what each|check|reconcil)", a.strip())]
        if t is None:
            out.append(f"{key}: no truth row")
            continue
        if not hits:
            out.append(f"{key}: NO SHEET ROW")
            continue
        ev, r = hits[-1]
        r = r + [""] * (8 - len(r))
        bucket = r[2].strip()
        tb = t["Bucket"]
        if tb == "Company":
            ok_bucket = bool(re.search(r"(?i)company", bucket))
        elif key == "JPMorgan":
            ok_bucket = not re.search(r"(?i)^(build|marketing|company)$", bucket)
        else:
            ok_bucket = bucket.lower() == str(tb).lower()
        if not ok_bucket:
            out.append(f"{key}: bucket '{bucket}' vs '{tb}' (event {ev})")
        if tb == "Company" and key != "Martin Walsh":
            got = num(r[6])
            want = t.get("company_usd", t.get("Company"))
            if got is None or abs(got - want) > 0.005:
                out.append(f"{key}: Company {r[6]!r} vs {want} (event {ev})")
        elif key == "Martin Walsh":
            if "1,999" not in " ".join(r) and "1999" not in " ".join(r):
                out.append(f"{key}: no 1,999 BGN (event {ev})")
        else:
            for i, col in enumerate(COLS):
                got = num(r[3 + i])
                if got is None or abs(got - float(t[col])) > 0.005:
                    out.append(f"{key}: {col} {r[3 + i]!r} vs {t[col]} (event {ev})")
    print(f"{run}: {len(rows)} sheet rows read; {len(out)} difference(s)")
    for line in out:
        print("   " + line)


if __name__ == "__main__":
    for run in sys.argv[1:] or [f"run-{n}" for n in range(1, 7)]:
        main(run)
