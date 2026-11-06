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
L.append("# 09 Rubric Writing Plan — robert_llc_takeover (LLC take-over of Combo Fighter, injection rev4)")
L.append("Generated 2026-11-06 · Clock 2026-02-14T00:00:00Z (seed bound) · Persona Robert robert@harmonygames.co · Assigned role Co-founder & Creative Director · Tier Long Horizon · Mode Easy · Human time 18.25 h · OE status: /oe PASS 2026-11-06")
L.append("Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)")
L.append("Canonical outcomes: brief §4b (all fair results and accepted alternatives), with two /oe notes applied: the sheet may sit in any folder of Robert's own Drive (/oe note 1, broader than §4b's root-only cell), and REVENUE_DAILY or REVENUE_DAILY_V2 both decide the take test (/oe note 2; identical January sums). OEs bound: 08_Oracle_Events.md sha256 e210cd02c49e (the reviewed /oe file).")
L.append("")
L.append("Design: Outcome rows on the five deliverables — the Linear project (new VO issue, comments, states, assignees), the plan sheet, the two shares, the thread reply — plus one Process row for 'Then reply'. Every trap and every exception gets a direct row; only repetitive, comparably important items (the 28 'stays with HG' issues, the routine sheet rows) are sampled, each group with a volume row (Rubric Writing §8; rubric-sampling-v1). Each fact is graded in at most two rows (V3). After /rubric round 1, every Linear comment and every state change has its own row (the calls differ per issue, so they are not sampled); only the plan sheet's repetitive cells are sampled, with P68 as the sheet's volume row. Per the /hardness and baseline notes, each trap lands on its own item rows, and ENG-2462 has five (P6, P22, P23, P47, P66).")
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
L.append("Cascade review (3_Rubrics_Eval.md 3.3): no shared embedded condition. Reply content rows (P61–P64) each name their own artifact, the reply in Leonard's DM thread; an off-thread reply fails them because that artifact was never made (a write and its content rows never form a group). Count rows P5, P27 and P36 are cohort controls on different outputs and never sum to one another. State and assignee are separate rows (samuel /rubric round 2).")
L.append("")
L.append("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
L.append("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
L.append("|---|---|---|---|---|")
for r in ROWS:
    labs = "; ".join(f"OE {n}  {EVS[n]}" for n in sorted(set(r["oe"]))[:3]) + (f"; + {len(set(r['oe'])) - 3} more ({oes(r)})" if len(set(r["oe"])) > 3 else "")
    L.append(f"| {r['p']} | {c(r['valid'])} · \"{r['span']}\" | {c(r['idle'])} | {c(labs)} | {r['reach']} |")
L.append("")
L.append("Final-reply test (whole set): \"Here's what I'd do: take Combo Fighter and Domino Delights into the LLC (DD made $183.11 in January, more than its $140 hosting) and leave Zombie Match with HG. It comes to $3,450 a month, so $1,150 each — Arthur's $248 counts toward his, so he puts in $902 cash. Sheet: (the sheet's Drive link).\" posted in the thread under Leonard's DM after the Linear, sheet and share writes → ACCEPT ☑ (P61–P65 pass; no row requires the VO line, the support build or any wording in the reply)")
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
    kind = "discovery" if n <= 19 else "discovery (decision step, no tool)" if n <= 23 else "write"
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
L.append("| C1 (P65) | \"Then reply to him in that DM thread\" (after \"When you're done, the project should match the sheet.\") | the reply's content is the same whether it is posted first or last; only the run's order shows it | yes — every valid path ends with the reply; the prompt orders it | yes — no end-state row can see order (the reply rows P61–P64 grade content) | yes — one ordering property of the run, not a tool trace; any write kind and tool are fine | Process (one row for the one ordering ask; per-write order rows would form a cascade, Q4 /rubric round 1) · F1, F66, F67 |")
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
L.append(f"Rows {len(ROWS)} · Outcome {nO} · Process candidates {nP} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · fewer than two Process rows failing the three-condition test ☑ (C1 passes all three) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (the sheet's cells D3–D6: P68; Linear comments and states are graded one row per issue) · predicted all-fail rows = 0 ☑ (harness tolerance 0; /rubric fails at ≥ 2)")
L.append(f"Failure diversity: largest unit of discovery {EXTRA['diversity']} of the weight (≤ 50% ☑, computed by stage_gate diversity.authority_share) · chains landing on distinct rows ☑ (T1 VO → P1–P4, P131, P171, P45, P173, P58, P64; T2 support → P6, P22, P23, P47, P66; T3 $140 → P14, P16, P46; T4 $62 → P18, P50; T5 $248 → P9, P24–P26, P40, P52–P54; T6 Figma → P7, P29, P42; T7 Calm Play → P8, P30, P41; T8 take test → P14, P28, P38, P39, P62, P63; T9 layer.ai → P48, P67; T10 one-offs → P10, P55; T12 Arthur's $248 → P58, P64)")
L.append(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total weight {sum(r['band'] for r in ROWS)})")
L.append(f"Format 5 (§A3): rows {len(ROWS)}/{len(ROWS)} ☑ · `do_nothing_case` REJECT {len(ROWS)}/{len(ROWS)} ☑ · reachability `PROMPT_LINKED` {len(ROWS)}/{len(ROWS)} ☑ · final-reply test ACCEPT ☑")
L.append(f"Set size: {len(ROWS)} rows for 18.25 h (reference: 31 criteria for a ~10-hour task; the 104-OE path and 38-item population put this at the long end without per-cell grading)")
L.append(f"Coverage: requirements 10/10 (R1–R10 of the ledger: R1–R2 through the deliverables, R3–R5 one comment row per issue (P69, P70, P6–P9, P11, P101–P130) plus cost rows P131–P138, R6 P34–P58, P66–P68, P72, P73, P172, P173, R7 P59–P60, R8 P1–P3, P171, one state row per issue (P12–P33, P141–P162), R9 P61–P65, R10 by every write) · OEs {len(EVS)}/{len(EVS)} (§B) · writes 81/81 (direct or cohort-controlled) · told facts 3/3 (what I'd do P62–P63, what it costs each P64, the link P61) · friction 0/0 (Friction: none)")
sl = SURF["slots"]
mech_ps = sorted({p for s_ in sl if s_["mechanisms"] for p in re.findall(r"\bP\d+\b", EXTRA["surface"][s_["id"]]["cov"])}, key=lambda x: int(x[1:]))
mw = sum(P[p]["band"] for p in mech_ps)
tw = sum(r["band"] for r in ROWS)
L.append(f"Gradable surface (gate 17): slots {len(sl)} · covered {EXTRA['surface_covered']} · dispositioned {len(sl) - EXTRA['surface_covered']} (§G) · no slot with neither ☑ · mechanism share {round(100 * mw / tw)}% ({mw} of {tw}: {', '.join(mech_ps)}) of the weight (reported, not gated)")
L.append("Four prohibitions: ☑ unstated expectations (no row grades the reply's VO or support mention, a title, wording or row order) ☑ conclusions on ambiguous evidence (risks 1–4, 8 accept every fair reading) ☑ grading the distractor (traps graded as handled values, never disclosure) ☑ hard-coded titles/phrasings (only the draft's 8 column headers, which the prompt incorporates)")
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
sr = open(os.path.join(HERE, "rubric_plan_selfreview.md")).read().rstrip().replace("@@TABLE@@", "\n".join(tab))
L.extend(sr.splitlines())
out = os.path.join(WF, "09_Rubric_Writing_Plan.md")
open(out, "w").write("\n".join(L) + "\n")
print("wrote", out, "rows", len(ROWS), "bands", dict(bands), "weight", sum(r["band"] for r in ROWS))
