#!/usr/bin/env python3
"""One-off D3 / rev2 edit of plan/assemble_dossier.py: the forecasts paragraph reads its figures from the forecast and
budget outputs instead of carrying D2's numbers. Idempotent."""
import re
from pathlib import Path
P = Path(__file__).resolve().parent / "assemble_dossier.py"
s = P.read_text()
start = s.index("**Forecasts (advisory, UNCALIBRATED, pre-registered).**")
end = s.index('""" + code("\\n".join(l for l in read(OUT / "forecast_injection.txt")', start)
NEW = ('**Forecasts (advisory, UNCALIBRATED, pre-registered).** Four figures, which measure different things; none is a measurement. '
       '(1) Design stage, `{FC_DESIGN_ID}`, on declared attributions for every slot and the ledger\'s family priors (which now include the seven rev1 runs): {FC_DESIGN}. '
       'Its completion_elsewhere prior still holds the rev1 runs that found Brian\'s log through the search for \'sound\', which rev2 removes, so it is pessimistic for this revision. '
       '(2) Injection stage, this SQL (`{FC_INJ_ID}`, block below): the tool evaluates only the slots the solver can compute (list cells and totals); the slots graded from written text '
       '(reasons, ticket comments, the brief, the reply, the shares) count as always passing, so its averages are upper bounds and its P(all gates) near zero says only that list cells alone '
       'would not bring the average under 70 %. A first injection forecast of this revision (`hev_b59c9f65ca1510cb`) ran on the SQL before the log stopped naming the chainsaw and the cone '
       '(path exposure) and is superseded by the one below. (3) The difficulty budget on the rubric skeleton, with find rates measured in the rev1 runs (`plan/out/policy_scores.txt`): {FC_BUDGET}. '
       '(4) The MODE B simulation of rev1 habits (`hardening_gen/simulate.py`): E[average] 0.47 to 0.61 for these four changes. The next pre-check is the first measurement of rev2.\n\n')
s = s[:start] + NEW + s[end:]
if "FC_DESIGN_ID =" not in s:
    anchor = "P = []\n"
    helper = '''def _fc(path):
    t = read(path)
    m = re.search(r"'id': '(hev_[0-9a-f]+)'", t)
    e = sorted(float(x) for x in re.findall(r"E\\[avg\\] ([0-9.]+)", t))
    p = re.search(r"P\\(all four difficulty gates\\) ([0-9.]+-[0-9.]+)", t)
    return (m.group(1) if m else "?"), (f"E[average] {e[0]:.3f} to {e[-1]:.3f}, P(all four difficulty gates) {p.group(1)}" if e and p else "see the output")
FC_DESIGN_ID, FC_DESIGN = _fc(OUT / "forecast.txt")
FC_INJ_ID, _ = _fc(OUT / "forecast_injection.txt")
_rows = {l.split()[0] + (" " + l.split()[1] if l.split()[0] in ("low", "high") else ""): l.split() for l in read(OUT / "policy_scores.txt").splitlines() if l.strip().startswith(("low find", "midpoint", "high find"))}
FC_BUDGET = "; ".join(f"{k}: E[average] {v[-7] if k == 'midpoint' else v[-7]} %, P(average under 70 %) {v[-6]}, P(spread in band) {v[-4]}, P(all gates) {v[-2]}" for k, v in _rows.items())
'''
    s = s.replace(anchor, helper + anchor, 1)
if "\nimport re" not in s and "import json, re" not in s:
    s = s.replace("import json", "import json, re", 1)
P.write_text(s)
print("forecast paragraph rewritten")
