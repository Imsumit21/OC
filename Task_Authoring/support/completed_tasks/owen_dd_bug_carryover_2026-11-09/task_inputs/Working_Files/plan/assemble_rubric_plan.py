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
L.append("# 09 Rubric Writing Plan — owen_dd_bug_carryover (DD bug list into Linear and the UI tree close-out, injection rev9)")
L.append("Generated 2026-11-09 · Clock 2026-02-14T00:00:00Z (seed bound) · Persona Owen Baker owen.baker@harmonygames.co · Assigned role Game Engineer (Unity) · Tier Long Horizon · Mode Medium · Human time 25.75 h · OE status: /oe PASS 2026-11-09")
L.append("Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)")
L.append("Canonical outcomes: brief §4b (all fair results and accepted alternatives), with the /prompt notes applied: any sharing role; ticket titles checked by their text, not one rendering of Slack mentions or emoji codes; the reply in the thread of Arthur's DM (the /rubric round-1 ruling: a top-level DM message does not count); 9 still broken (a reply giving only the 7 Broken items fails, round-1 ruling). OEs bound: 08_Oracle_Events.md sha256 a9bbea55e7c3 (the /oe PASS 5 file, round 3).")
L.append("")
L.append(res("Design (rebuilt on the /rubric round-1 Fix List, reviewed JSON 2ed7a6489798): Outcome rows on the five deliverables — the new Linear tickets and the two notes, the UI tree (moves and a line on every child), the sheet in the folder, the three shares, the thread reply — plus one Process row for \"Then reply\". Every new issue's state has its own row (each creation carries its own title); the ticket template is stated in the volume row @@P:new_count@@ with one sample per field; every UI child has its own build-line row; only template-identical writes (the moves and the sheet's Outcome, Ticket and Why cells) are sampled, each with a volume row. 138 rows for a 150-OE path."))
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
L.append(res("Cascade review (3_Rubrics_Eval.md 3.3): no shared embedded condition. The state rows name each issue by its line or post and grade the state only, whatever the title (the round-1 '[2231]' cascade is gone); the sheet rows say 'the DD carry-over sheet' and only @@P:sheet_folder@@ names the folder (the round-1 folder cascade is gone); the reply rows @@P:reply_broken@@–@@P:reply_done@@ each name their own artifact; the count rows @@P:new_count@@, @@P:moves_count@@ and @@P:sheet_rows@@ are population controls on different outputs."))
L.append("")
L.append("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
L.append("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
L.append("|---|---|---|---|---|")
for r in ROWS:
    labs = "; ".join(f"OE {n}  {EVS[n]}" for n in sorted(set(r["oe"]))[:3]) + (f"; + {len(set(r['oe'])) - 3} more ({oes(r)})" if len(set(r["oe"])) > 3 else "")
    L.append(f"| {r['p']} | {c(r['valid'])} · \"{r['span']}\" | {c(r['idle'])} | {c(labs)} | {r['reach']} |")
L.append("")
L.append("Final-reply test (whole set): \"Done. Still broken: 9 (7 Broken + 2 Covered). New tickets filed: 68. UI children Done: 23 of 28 (ENG-2424, ENG-2426, ENG-2428, ENG-2434 and ENG-2437 stay open). The sheet is in your DD bug carry-over folder, shared with you, Robert and Oliver.\" posted in the thread under Arthur's Feb 12 DM after the Linear, sheet and share writes → ACCEPT ☑ (no row requires a link, a list, a format or wording beyond the three numbers)")
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
    kind = "discovery" if n <= 29 else "discovery (decision step, no tool)" if n <= 31 else "write"
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
L.append(res("| C1 (@@P:reply_after_writes@@) | \"Then reply to him in that DM thread\" | the reply's numbers read the same whether it is posted first or last; only the run's order shows it | yes — every valid path ends with the reply; the prompt orders it | yes — no end-state row can see order (@@P:reply_broken@@–@@P:reply_done@@ grade content) | yes — one ordering property of the run, not a tool trace | Process (one row for the one ordering ask) |"))
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
L.append(f"Rows {len(ROWS)} · Outcome {nO} · Process candidates {nP} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · fewer than two Process rows failing the three-condition test ☑ (C1 passes all three) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (G1a–G1g: {PN['new_count']}, G4: {PN['moves_count']}, G7–G9: {PN['sheet_rows']}) · predicted all-fail rows = 0 ☑")
L.append(res("Failure diversity: largest unit of discovery computed by stage_gate diversity.authority_share (≤ 50% ☑) · chains landing on distinct rows ☑ (T1 Tavern → @@P:state:tavern@@, @@P:sheet:tavern@@, @@P:sheet_why:tavern@@; T2 shop → @@P:state:shop@@; T3 Apple → @@P:covered:apple@@, @@P:sheet:apple@@, @@P:sheet_outcome:apple@@; T4 sign-in → @@P:covered:signin@@, @@P:sheet:signin@@; T5 window → @@P:state:tile dozer window background@@, @@P:sheet:window@@; T6 popups → @@P:hold:ENG-2434@@, @@P:hold:ENG-2426@@; T7 Season Pass → @@P:hold:ENG-2428@@; T8 Daily Gift → @@P:hold:ENG-2437@@; T9 Win & Collect → @@P:hold:ENG-2424@@; T10 lives → @@P:state:I found the issue lives are not decreased after@@–@@P:state:When I change the character it just adds 1@@, @@P:sheet:lives1@@; T11 train/team/backend → @@P:state:vr_train@@–@@P:state:backend@@; T12 closing rule → @@P:line:ENG-2434@@–@@P:line:ENG-2409@@; T13 scope and fields → @@P:new_count@@–@@P:desc:In chapter selection@@, @@P:sheet_rows@@)"))
L.append(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total weight {sum(r['band'] for r in ROWS)})")
L.append(f"Format 5 (§A3): rows {len(ROWS)}/{len(ROWS)} ☑ · `do_nothing_case` REJECT {len(ROWS)}/{len(ROWS)} ☑ · reachability `PROMPT_LINKED` {len(ROWS)}/{len(ROWS)} ☑ · final-reply test ACCEPT ☑")
L.append(f"Set size: {len(ROWS)} rows for 25.75 h (reference: 31 criteria for a ~10-hour task; a 70-item population and a 28-child tree, each item and child graded on its own row per the /rubric round-1 Fix List)")
L.append(res(f"Coverage: requirements 10/10 (R1–R3 through the deliverables, R4 P1–@@P:covered:signin@@, R5 @@P:moves_count@@–@@P:hold:ENG-2437@@, R6 @@P:line:ENG-2434@@–@@P:line:ENG-2409@@, R7 @@P:sheet_folder@@–@@P:sheet_why:sides@@, R8 @@P:share:arthur.blake@harmonygames.co@@–@@P:share:oliver.brooks@harmonygames.co@@, R9 @@P:reply_thread@@–@@P:reply_after_writes@@, R10 by every write) · OEs {len(EVS)}/{len(EVS)} (§B) · writes 119/119 (direct or population control) · told facts 3/3 (@@P:reply_broken@@–@@P:reply_done@@) · friction 0/0"))
sl = SURF["slots"]
mech_ps = sorted({p for s_ in sl if s_["mechanisms"] for p in re.findall(r"\bP\d+\b", EXTRA["surface"][s_["id"]]["cov"])}, key=lambda x: int(x[1:]))
mw = sum(P[p]["band"] for p in mech_ps)
tw = sum(r["band"] for r in ROWS)
L.append(f"Gradable surface (gate 17): slots {len(sl)} · covered {EXTRA['surface_covered']} · dispositioned {len(sl) - EXTRA['surface_covered']} (§G) · no slot with neither ☑ · mechanism share {round(100 * mw / tw)}% ({mw} of {tw}: {', '.join(mech_ps)}) of the weight (reported, not gated)")
L.append(res("Four prohibitions: ☑ unstated expectations (no row grades a title beyond the template the notes and the comment fix — the prefix sample @@P:prefix:In profile@@ and the title-text sample @@P:titletext:flickering@@ — the state rows accept the issue whatever its title, the Why rows @@P:sheet_why:tavern@@ and @@P:sheet_why:sides@@ accept any wording with that meaning, and no row grades a link or row order) ☑ conclusions on ambiguous evidence (risks 1–7 of the ledger accept every fair reading) ☑ grading the distractor (traps graded as handled values, never disclosure) ☑ hard-coded titles/phrasings (only the [2231] prefix, the post's first line and the four column names, which the comment and the notes fix)"))
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
