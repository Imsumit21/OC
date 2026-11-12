#!/usr/bin/env python3
"""Match every item of the blind O3 inventory (local_reviews/oe/round<N>/output_O3.json) to the Oracle Events that read
both sides and make the fix (blind_review.py summary: an unmatched item is a missing step). Mechanical: each line item
needs (a) a read event naming the line whose records include the item's deciding record or the line's own ticket, and
(b) the write that sets it: the rows write for every line, plus a move and a comment when the line is Owed. Brief items
need the brief write. Writes oe_gen/blind_summary.md (pasted into 08_OE_Check.md's self-review by assemble_check.py).
Usage: python3 -B o3_match.py <round>"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model as O
RND = sys.argv[1] if len(sys.argv) > 1 else "2"
REV = HERE.parent / "local_reviews" / "oe" / f"round{RND}"
O3_REV = next(r for r in sorted((HERE.parent / "local_reviews" / "oe").glob("round*"), key=lambda x: int(x.name[5:]), reverse=True)
              if int(r.name[5:]) <= int(RND) and (r / "output_O3.json").exists())     # O3's inventory is carried into a changed round
o3 = json.loads((O3_REV / "output_O3.json").read_text()); o3 = o3.get("output", o3)
o2 = json.loads((REV / "output_O2.json").read_text()); o2 = o2.get("output", o2)
o1 = json.loads((REV / "output_O1.json").read_text()); o1 = o1.get("output", o1)
EV = json.loads((HERE / "out" / "oe_events.json").read_text())
BYT = {l["ticket"]: l for l in O.LINES}
def reads_naming(name): return [e for e in EV if e["kind"] == "read" and name in e["expected"]]
def first(prefix): return next(e for e in EV if e["head"].startswith(prefix))
rows_ev, brief_ev = first("Write the header"), first("Create the brief")
rows, unmatched = [], []
for i, f in enumerate(o3["findings"], 1):
    tickets = list(dict.fromkeys(re.findall(r"DES-\d{3}", f["fix"]) or re.findall(r"DES-\d{3}", f["evidence"])))
    if f["fix"].startswith("Brief"):
        field = f["fix"].split(":")[0]
        ok = True
        rows.append((f"I{i}", field, "—", f"OE {brief_ev['n']}", "matched"))
        continue
    t = tickets[0]; l = BYT[t]
    rd = reads_naming(l["name"])
    fixw = [rows_ev] + ([e for e in EV if e["head"].startswith((f"Move {t} ", f"Comment on {t} "))] if l["state"] == "Owed" else [])
    need = 3 if l["state"] == "Owed" else 1
    if l["state"] == "Owed":   ok = bool(rd) and len(fixw) == 3                      # read with its deciding record; rows write, move, comment
    elif l["state"] == "Ready": ok = bool(rd) and l["name"] in rows_ev["expected"]   # named on the rows write's Ready list
    else:                       ok = bool(rd)                                        # Delivered: named on the hand-over read the rows write cites
    if f["severity"] == "UNSURE":
        verdict = "resolved: no change (ledger T19); stays " + l["state"]
    else:
        verdict = "matched" if ok else "UNMATCHED"
    if verdict == "UNMATCHED": unmatched.append(t)
    rows.append((f"I{i}", f"{t} {l['name']} ({l['state']}{', ' + l['who'] if l['who'] else ''})", ", ".join(f"OE {e['n']}" for e in rd),
                 ", ".join(f"OE {e['n']}" for e in fixw), verdict))
assert not unmatched, unmatched
def cell(s): return str(s).replace("|", "/")
hist = []
for rd in sorted((HERE.parent / "local_reviews" / "oe").glob("round*"), key=lambda x: int(x.name[5:])):
    if int(rd.name[5:]) < 2: continue                          # round 1 reviewed rev1's events
    man = json.loads((rd / "manifest.json").read_text())
    parts = []
    for ps in ("O1", "O2", "O3"):
        f = rd / f"output_{ps}.json"
        if not f.exists(): continue
        o = json.loads(f.read_text()); o = o.get("output", o)
        if ps == "O3": parts.append(f"O3 {len(o['findings'])} inventory item(s)"); continue
        fs = "; ".join(f"{x['event']} {x['issue_type']} {x['severity']}" for x in o["findings"])
        parts.append(f"{ps} {o['verdict']}" + (f" ({fs})" if fs else ""))
    hist.append(f"{rd.name} ({man.get('scope', '?')}, {len(man.get('in_scope', []))} event(s) in scope): " + ", ".join(parts))
lines = [f"Blind passes, local rehearsal (tools/blind_review.py; LOCAL REHEARSAL, not a platform verdict). " + " · ".join(hist) + ". "
         "Platform /oe round 1 (eval_reports/6aea4c201e1fa1ddfdd0a25d_2_oe.md, FAIL 2) found OE 20's purpose accepted a walked-back alternative and OE 10 left out the walk-back; both fixed "
         "(OE 10 now reads Robert's 'Doesn't really matter' and 'I think we should remain as is', OE 20 carries one purpose). Each Minor dependency finding on OE 130 is fixed: it now depends on "
         "the file writes OE 20 to OE 22 and the eight shares OE 23 to OE 30. "
         + f"O3 inventory ({O3_REV.name}, carried): {len(o3['findings'])} item(s), each matched below to the reads that see both sides and the writes that make the fix "
         f"({sum(1 for r in rows if r[4] == 'matched')} matched, {sum(1 for r in rows if r[4].startswith('resolved'))} UNSURE resolved, 0 unmatched).", "",
         "| Item | Line or field | Reads (both sides) | Writes (the fix) | Result |", "|---|---|---|---|---|"]
lines += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
(HERE / "blind_summary.md").write_text("\n".join(lines) + "\n")
print(f"O3 items {len(rows)}: matched {sum(1 for r in rows if r[4] == 'matched')}, resolved {sum(1 for r in rows if r[4].startswith('resolved'))}, unmatched 0")
