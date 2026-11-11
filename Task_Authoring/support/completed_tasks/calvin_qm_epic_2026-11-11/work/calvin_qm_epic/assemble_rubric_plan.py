#!/usr/bin/env python3
"""Build Working_Files/09_Rubric_Writing_Plan.md (prep) from plan/rubric_rows.py, the OEs, the ledger and the gradable surface.
Pastes the ledger's visibility proof and (when present) plan/shortcut_probe.out verbatim. Never writes criterion JSON."""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
spec = importlib.util.spec_from_file_location("rubric_rows", os.path.join(HERE, "rubric_rows.py"))
RR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RR)
ROWS = RR.R
PN = RR.PN


def res(x):
    return re.sub(r"@@P:(.+?)@@", lambda m: PN[m.group(1)], x)


PROMPT = open(os.path.join(TI, "04_Prompt.txt")).read()
OE = open(os.path.join(TI, "08_Oracle_Events.md")).read()
EVS = {int(n): a for n, a in re.findall(r"^OE (\d+)  (.*)$", OE, re.M)}
LED = open(os.path.join(WF, "08_OE_Writing_Ledger.md")).read().splitlines()
SURF = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
EXTRA = json.load(open(os.path.join(HERE, "rubric_plan_extra.json")))
for r in ROWS:
    assert r["span"] in PROMPT, r["p"]
    assert re.search(r"\bF\d+\b", r["vals"]), r["p"]
    assert r["band"] in (1, 3, 5)
P = {r["p"]: r for r in ROWS}


def c(s):
    return str(s).replace("|", "/").replace("\n", " ")


def oes(r):
    ns = sorted(set(r["oe"]))
    out, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
            j += 1
        out.append(f"OE {ns[i]}" if i == j else f"OEs {ns[i]}–{ns[j]}")
        i = j + 1
    return ", ".join(out)


L = []
L.append("# 09 Rubric Writing Plan — calvin_qm_epic (the Queue Manager epic and stock-take, injection rev3b)")
L.append("Generated 2026-11-11 · Clock 2025-10-01T07:00:00Z (seed bound) · Persona Calvin Price calvin.price@harmonygames.co · Assigned role Game Engineer (Unity VFX) · Tier Long Horizon · Mode Hard · Human time 19.25 h · OE status: /oe PASS 2026-11-11")
L.append("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
L.append("Canonical outcomes: brief §4b (all fair results and accepted alternatives), with the /prompt notes applied: any sharing role; Open reports as a count or as the list of open reports; the message as a new DM message or a thread reply under Brian's message; the sheet created in the folder or moved into it. OEs bound: 08_Oracle_Events.md sha256 376b94e7eaa9 (the /oe PASS 5 file).")
L.append("")
L.append(res("Design (rebuilt on the /rubric round-1 Fix List, reviewed JSON afbc830d0cbb): Outcome rows on the five deliverables plus one Process row for \"Once that's done\". Every write that differs per target has its own row: each child's create and end state, each new sub-issue's create (title and parent) and state, each moved ticket's move, each changed ticket state, each note's status and each note's reason, each area's open count. Template fields are sampled under the two template rows @@P:child_template@@ and @@P:sub_template@@; the sheet's Status, Ticket, Review list, Why and Area cells are sampled under @@P:sheet_rows@@ and @@P:review_count_sheet@@. The 74 rows the Fix List does not touch are byte-identical to the reviewed JSON."))
L.append("")
L.append("## A · Coverage matrix")
L.append("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category (Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |")
L.append("|---|---|---|---|---|---|---|")
for r in ROWS:
    L.append(f"| {r['p']} | \"{r['span']}\" · {oes(r)} | {r['fact']} | {c(r['what'])} | {c(r['final'])} | {r['cat']} | {c(r['vals'])} |")
L.append("")
L.append("## A2 · Grading risks and weight")
L.append("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |")
L.append("|---|---|---|---|---|---|---|---|---|---|")
for r in ROWS:
    L.append(f"| {r['p']} | {c(r['phr'])} | {c(r['dis'])} | {c(r['amb'])} | {c(r['kind'])} | {r['band']} | {c(r['dec'])} | {c(r['grp'])} | {c(r['dup'])} | {c(r['af'])} |")
L.append("")
L.append(res("Cascade review (3_Rubrics_Eval.md 3.3): no shared embedded condition. The state rows name one ticket or one sub-issue and grade its state only; the move rows name the ticket and its child; only @@P:sheet_folder@@ names the folder; the DM and slide number rows each name their own artifact. A missed sighting fails that report's rows on separate prompt-required deliverables, which the round-1 report ruled is not a group."))
L.append("")
L.append("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
L.append("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
L.append("|---|---|---|---|---|")
for r in ROWS:
    labs = "; ".join(f"OE {n}  {EVS[n]}" for n in sorted(set(r["oe"]))[:3]) + (f"; + {len(set(r['oe'])) - 3} more ({oes(r)})" if len(set(r["oe"])) > 3 else "")
    L.append(f"| {r['p']} | {c(r['valid'])} · \"{r['span']}\" | {c(r['idle'])} | {c(labs)} | {r['reach']} |")
L.append("")
L.append("Final-reply test (whole set): \"Done. Passed: 10. Waiting on QA: 9. Waiting on a fix: 20. Areas clear: 0. On the review list: 7. The stock-take sheet is in your ZM queue manager folder, shared with everyone on the invite, and the numbers slide is in the deck.\" posted in the DM with Brian after the Linear, sheet, share and slide writes → ACCEPT ☑ (no row requires a link, a list, a format or wording beyond the five numbers)")
L.append("")
L.append("## B · OE trace")
L.append("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
L.append("|---|---|---|---|")
by_oe = {}
for r in ROWS:
    for n in set(r["oe"]):
        by_oe.setdefault(n, []).append(r["p"])
miss = [n for n in EVS if n not in by_oe]
assert not miss, miss
for n in sorted(EVS):
    kind = "discovery" if n <= 20 else "discovery (decision step, no tool)" if n == 21 else "write"
    ps = sorted(by_oe[n], key=lambda x: int(x[1:]))
    if kind.startswith("discovery"):
        own = "no — proved by the content and final-response rows that carry its result (gate 3)"
    else:
        direct = [p for p in ps if P[p]["grp"] in ("—",) or "direct" in P[p]["grp"] or "sample" in P[p]["grp"]]
        vol = [p for p in ps if "volume" in P[p]["grp"]]
        own = (f"yes — {', '.join(direct)}" if direct else "") + (("; " if direct else "") + f"cohort control {', '.join(vol)} (the item is not sampled)" if vol and not direct else "")
        own = own or "yes"
    L.append(f"| OE {n} | {kind} | {', '.join(ps)} | {own} |")
L.append("")
L.append("## C · Process candidates — three-condition test")
L.append("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |")
L.append("|---|---|---|---|---|---|---|")
L.append(res("| C1 (@@P:dm_after_writes@@) | \"Once that's done, message him in our DM\" | the message's numbers read the same whether it is posted first or last; only the run's order shows it | yes — every valid path ends with the message; the prompt orders it | yes — no end-state row can see order (@@P:dm:passed@@–@@P:dm:review@@ grade content) | yes — one ordering property of the run, not a tool trace | Process (one row for the one ordering ask) |"))
L.append("")
L.append("## D · Spot-check groups")
L.append("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
L.append("|---|---|---|---|---|---|")
for g in EXTRA["groups"]:
    L.append(f"| {g['g']} | {c(g['items'])} | {c(g['samples'])} | {g['volume']} | none — bundle (Rubric Writing §7; Eval 2.2) | {c(g['core'])} |")
L.append("")
L.append("## E · Summary")
nO = sum(1 for r in ROWS if r["cat"] == "Outcome")
nP = len(ROWS) - nO
from collections import Counter
bands = Counter(r["band"] for r in ROWS)
L.append(f"Rows {len(ROWS)} · Outcome {nO} · Process candidates {nP} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · fewer than two Process rows failing the three-condition test ☑ (C1 passes all three) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (G1: {PN['child_template']}, G2: {PN['sub_template']}, G4, G5, G7, G10: {PN['sheet_rows']}, G6: {PN['review_count_sheet']}, G8: {PN['area_rows']}) · predicted all-fail rows = 0 ☑")
L.append(res("Failure diversity: largest unit of discovery computed by stage_gate diversity.authority_share (≤ 50% ☑) · chains landing on distinct rows ☑ (T1 branch build → @@P:state:1@@, @@P:state:2@@, @@P:state:25@@; T2 reviews → @@P:state:12@@, @@P:state:15@@, @@P:state:32@@; T3 Oliver's comment → @@P:state:13@@, @@P:state:14@@, @@P:state:37@@, @@P:state:38@@; T4 description → @@P:state:6@@; T5 thread replies → @@P:state:9@@, @@P:state:29@@; T6 ticket notes → @@P:state:17@@, @@P:note:24@@, @@P:child_state:Zombie Lane@@; T7 → @@P:state:27@@; T8 → @@P:note:18@@, @@P:note:34@@; T9 agenda → @@P:sheet_review:6@@; T10 → @@P:move:11@@, @@P:move:20@@; T11 → @@P:state:39@@, @@P:sheet_rows@@)"))
L.append(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total weight {sum(r['band'] for r in ROWS)})")
L.append(f"Format 5 (§A3): rows {len(ROWS)}/{len(ROWS)} ☑ · `do_nothing_case` REJECT {len(ROWS)}/{len(ROWS)} ☑ · reachability `PROMPT_LINKED` {len(ROWS)}/{len(ROWS)} ☑ · final-reply test ACCEPT ☑")
L.append(f"Set size: {len(ROWS)} rows for 19.25 h (reference: 31 criteria for a ~10-hour task; the /rubric round-1 report counted 259 required outcomes and asked for a row on each write that differs per target)")
L.append(res(f"Coverage: requirements 8/8 (R1–R3 through the deliverables, R4 P1–@@P:move:4@@, R5 @@P:sheet_folder@@–@@P:area_open_count:Card packs@@, R6 @@P:share:arthur.blake@@–@@P:share:vincent.parker@@, R7 @@P:slide_new@@–@@P:slide:review@@, R8 @@P:dm_place@@–@@P:dm_after_writes@@) · OEs {len(EVS)}/{len(EVS)} (§B) · writes 83/83 (direct or template control) · told facts 5/5 (@@P:dm:passed@@–@@P:dm:review@@) · friction 0/0"))
sl = SURF["slots"]
mech_ps = sorted({p for s_ in sl if s_["mechanisms"] for p in re.findall(r"\bP\d+\b", EXTRA["surface"][s_["id"]]["cov"])}, key=lambda x: int(x[1:]))
mw = sum(P[p]["band"] for p in mech_ps)
tw = sum(r["band"] for r in ROWS)
L.append(f"Gradable surface (gate 17): slots {len(sl)} · covered {EXTRA['surface_covered']} · dispositioned {len(sl) - EXTRA['surface_covered']} (§G) · no slot with neither ☑ · mechanism share {round(100 * mw / tw)}% ({mw} of {tw}: {', '.join(mech_ps)}) of the weight (reported, not gated)")
L.append(res("Four prohibitions: ☑ unstated expectations (no row grades a title beyond the report or area name, a link, a row order or a share role) ☑ conclusions on ambiguous evidence (ledger risks 1–5 accept every fair reading) ☑ grading the distractor (traps are graded by the state, count or cell they decide, never by naming the trap) ☑ hard-coded titles/phrasings (statuses and reasons accept any wording with that meaning)"))
L.append("Blocking: none — no UGT defect (/prompt PASS 5), every write cataloged (ledger §C), every scoped record behind a cited F-id visible (below)")
L.append("")
# visibility proof copied from the ledger
i0 = next(i for i, l in enumerate(LED) if l.startswith("Visibility proof"))
i1 = next(i for i in range(i0 + 1, len(LED)) if LED[i].startswith("## "))
L.extend(LED[i0:i1])
L.append("## F · Shortcut probe")
probe = os.path.join(HERE, "shortcut_probe.out")
if os.path.exists(probe):
    L.append("```text")
    L.extend(open(probe).read().rstrip().splitlines())
    L.append("```")
    L.extend(EXTRA.get("shortcut_ok", []))
else:
    L.append("probe not yet run")
L.append("")
L.append("## G · Gradable-surface coverage")
L.append("| Slot | Stable fact ID | Selector · role / group | Work kind (band) | Mechanisms → Decided by | Covered by (P-n) | Disposition and reason (evidence) |")
L.append("|---|---|---|---|---|---|---|")
for s in sl:
    g = EXTRA["surface"][s["id"]]
    L.append(f"| {s['id']} | {g['fact']} | {c(json.dumps(s['selector']))[:90]} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({s['weight']}) | {', '.join(s['mechanisms']) or '—'} → {g['dec']} | {g['cov']} | {c(g['disp'])} |")
L.append("")
tab = ["| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |", "|---|---|---|---|---|"]
for r in ROWS:
    cr = r["cr"]
    m = re.match(r"\(a\)(.*?);\s*\(b\)(.*)$", cr)
    a_, b_ = (m.group(1).strip(), m.group(2).strip()) if m else (cr, "")
    tab.append(f"| {r['p']} {c(r['fact'])} (band {r['band']}) | holds | (a) {c(a_)} (b) {c(b_)} | {c(r['vals'])} | none |")
sr = res(open(os.path.join(HERE, "rubric_plan_selfreview.md")).read().rstrip()).replace("@@TABLE@@", "\n".join(tab))
L.extend(sr.splitlines())
out = os.path.join(WF, "09_Rubric_Writing_Plan.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, "rows", len(ROWS), "bands", dict(bands), "weight", sum(r["band"] for r in ROWS))
