#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py). The visibility block
(visibility.txt), the shortcut probe paste (probe.txt) and the self-review (built here) sit next to this script."""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
rows = json.loads((HERE / "rows.json").read_text())
P = [f"P{i + 1}" for i in range(len(rows))]
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}


def pn(*tags):
    return ", ".join(TAG[t] for t in tags)


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def rng(prefix):
    ps = [TAG[r["tag"]] for r in rows if r["tag"].startswith(prefix)]
    return f"{ps[0]} to {ps[-1]}" if len(ps) > 1 else ps[0]


tw = sum(r["w"] for r in rows)
bands = Counter(r["w"] for r in rows)
out = []
w = out.append
w("# 09 Rubric Writing Plan: vincent-zm3d-release-gate (ZM store candidates QA gate, injection rev18)")
w("Generated 2026-11-06 · Clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut); seed bound "
  "2025-10-01T00:00:00Z · Persona Vincent Parker vincent.parker@harmonygames.co · Assigned role Game Systems Engineer · "
  "Tier Long-Horizon · Mode Easy · Human time: worksheet not yet written (set size judged against the 133-row register) · "
  "OE status: /oe PASS 2026-11-05 (platform report 6ae9909f7b5249d3148f3707_2_oe.md, Score 5, 35 events; em dashes "
  "replaced afterwards with no change of content, oe-check gate re-run PASS on the current file)")
w("Canonical outcomes: brief §4b (all fair results and accepted alternatives). D1 register: one new tab of ZM3D Release "
  "Gate f_0ebfccf33076f9dbf086bc named after the candidates, 133 ticket rows (112 open in-scope tickets, 20 moved to Done "
  "after the 2025-09-22 12:30:43 UTC cut, plus the ticket the run files), columns ticket, title, build status, QA result, "
  "call, evidence; calls 19 BLOCKER / 10 FIXED / 19 KNOWN ISSUE / 85 NO CALL. D2 the 19 blockers by key in ZOM-570's "
  "description, Arthur's text kept. D3 one new ZOM ticket for the iOS N-1 to iOS Submission #50 save reset with device "
  "iPhone 13, iOS 18.6, source build N-1 (App Store) and repro. D4 a reply in thread C08R27X0EAH/1759263900.484190 with "
  "the QA call no-go.")
w("")
w("Rubric shape: every write has a result row and a wrong-target guard (exactly one new tab, register rows only in that "
  "tab, 133 rows under Leonard's scope with its exclusions, the blocker list only on ZOM-570 and exactly 19 keys, exactly "
  "one new issue, the QA call only in Arthur's thread). The register's call column is graded in full for the BLOCKER class "
  "(19, the calls that decide the gate and feed ZOM-570); the 114 other calls form one group G1 with direct rows on the "
  "authority-decided exceptions (Leonard's two per-ticket rulings, the server fix confirmed on prod) and five samples. The "
  "other columns are sampled (G2 build status: three exception values plus three samples, G3 QA result 2, G4 evidence 2, "
  "G5 title 1) under the one volume row. The ZOM-570 blocker list is graded in full (19 rows plus its count). Revised "
  "after the independent review round 1 (seven reviewers): id-or-link evidence, launch in the repro, scope qualifier on "
  "the count, wrong-target guards, a timing row, the sampling cap on the call column. 09_Rubrics.json mirrors P1 to "
  f"P{len(rows)} one to one (C-n = P-n).")
w("")
w("## A · Coverage matrix")
w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | "
  "Category (Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date "
  "acceptance · F-IDs |")
w("|---|---|---|---|---|---|---|")
for p, r in zip(P, rows):
    acc = "; ".join(r["acc"])
    w(f"| {p} | \"{r['span']}\" · {', '.join(r['oe'])} | {r['fact']} | {cell(r['verify'])} | {cell(r['final'])} | Outcome | "
      f"{r['vals']} · accept: {cell(acc)} · dates: none graded · {r['fids']} |")
w("")
w("## A2 · Grading risks and weight")
w("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no "
  "single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason "
  "| Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | "
  "Predicted all-fail basis (four Evals bases) · over-specific risk |")
w("|---|---|---|---|---|---|---|---|---|---|")
dup = Counter(r["fact"] for r in rows)
for p, r in zip(P, rows):
    spec = ("yes: How we gate fixes the vocabulary (call values, build-status values) and names the tab after the "
            "candidates; meaning-equivalent wording accepted" if r["tag"].startswith(("bs_", "tabname")) else
            "no: titles of the tab, ticket and reply are free; only values are graded")
    w(f"| {p} | {spec} | {cell(r['dist'])} | none: the value is settled by the latest dated record (ledger §F risks 1 to 4 "
      f"do not touch it) | {r['kind']}: {cell(r['why'])} | {r['w']} | {r['dec']} | {cell(r['grp'])} | {r['fact']} in "
      f"{dup[r['fact']]} row(s) | none · over-specific risk low: {cell(r['alt'])} |")
w("")
w("## A3 · Format 5: per-row acceptance cases, OE steps and reachability")
w("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required "
  "write) | OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / "
  "UNLINKED) |")
w("|---|---|---|---|---|")
for p, r in zip(P, rows):
    w(f"| {p} | {cell(r['valid'])} (\"{r['span']}\") | REJECT: {cell(r['idle'])} (title: \"{cell(r['t'])}\") | "
      f"{', '.join(r['oe'])} | PROMPT_LINKED (path starts at Arthur's thread, the release gate sheet or the runbook, which "
      f"the prompt names) |")
w("")
w("Final-reply test (whole set): \"Done. QA call on Android #135 / iOS #50 is NO-GO: 19 blockers, all on ZOM-570, "
  "including ZOM-581, the iOS N-1 update save reset I filed; the register is in the new 'Sep 30 - Android #135 / iOS #50' "
  "tab and the call is in Arthur's thread.\" → ACCEPT ☑ (no row grades the final response; every graded value sits on "
  "the register, ZOM-570, the new issue or the thread reply)")
w("")
w("## B · OE trace")
w("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
w("|---|---|---|---|")
cites = {}
for p, r in zip(P, rows):
    for o in r["oe"]:
        cites.setdefault(int(o.split()[1]), []).append(p)
extra = {4: ([pn("count133")], "no: finds the two rule docs; their rules decide the calls and the scope"),
         30: ([pn("s_thread")], "no: the go/no-go starts 2025-10-03T16:00:00Z (evt_81e6dc4dbfd331f1a6a317), after the clock, "
                                "so every write in the run is before it; no row grades a time")}
for n in range(1, 36):
    kind = "write" if n in (31, 32, 33, 34, 35) else "discovery"
    if n in cites:
        rs = cites[n]
        own = ("yes: the write's result row" if kind == "write" else "no: proved by the content row(s) it decides")
    else:
        rs, own = extra[n]
    w(f"| OE {n} | {kind} | {', '.join(sorted(set(rs), key=lambda x: int(x[1:])))} | {own} |")
w("")
w("## C · Process candidates: three-condition test")
w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) "
  "behavioural, not trace | Result (Process / tighten P-n with F-n) |")
w("|---|---|---|---|---|---|---|")
w(f"| none | \"Reply in Arthur's candidates thread in #zombie-bugs with the QA call, before Friday's go/no-go\" | The prompt "
  f"sets a deadline, not an order between writes; the go/no-go (evt_81e6dc4dbfd331f1a6a317) is after the clock | fails: no "
  f"valid path needs the reply after the other writes | fails: {pn('s_thread', 's_call')} grade the reply's destination "
  f"and call | n/a | none: no Process row (F37) |")
w(f"| none | The new ticket must exist before ZOM-570 and the register can carry its key | {pn('z_new', 'reg_new')} require "
  f"the new key on ZOM-570 and in the register | yes | fails: the Outcome rows already need the key, so they capture the "
  f"order | n/a | none: tightened through {pn('z_new', 'reg_new')} (F40) |")
w("")
w("## D · Spot-check groups")
w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | "
  "Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
w("|---|---|---|---|---|---|")
KNOWN = "ZOM-237 ZOM-348 ZOM-427 ZOM-438 ZOM-443 ZOM-468 ZOM-481 ZOM-504 ZOM-505 ZOM-520 ZOM-534 ZOM-556 ZOM-568 ZOM-571 ZOM-572 ZOM-574 ZOM-579 ZOM-580 ART-793".split()
NOCALL = ("ZOM-16 ZOM-48 ZOM-56 ZOM-62 ZOM-64 ZOM-65 ZOM-66 ZOM-69 ZOM-70 ZOM-73 ZOM-76 ZOM-78 ZOM-97 ZOM-104 ZOM-112 "
          "ZOM-118 ZOM-119 ZOM-121 ZOM-122 ZOM-130 ZOM-137 ZOM-147 ZOM-148 ZOM-150 ZOM-151 ZOM-155 ZOM-168 ZOM-169 ZOM-171 "
          "ZOM-181 ZOM-182 ZOM-184 ZOM-202 ZOM-236 ZOM-239 ZOM-243 ZOM-255 ZOM-292 ZOM-311 ZOM-317 ZOM-342 ZOM-344 ZOM-386 "
          "ZOM-387 ZOM-390 ZOM-400 ZOM-419 ZOM-432 ZOM-439 ZOM-441 ZOM-442 ZOM-453 ZOM-465 ZOM-467 ZOM-471 ZOM-477 ZOM-482 "
          "ZOM-484 ZOM-498 ZOM-507 ZOM-508 ZOM-513 ZOM-514 ZOM-521 ZOM-526 ZOM-528 ZOM-536 ZOM-538 ZOM-539 ZOM-541 ZOM-542 "
          "ZOM-543 ZOM-544 ZOM-545 ZOM-548 ZOM-549 ZOM-552 ZOM-553 ZOM-555 ZOM-565 ZOM-566 ZOM-575 ZOM-577 ART-790 ART-792").split()
BLOCKERS = ("DES-313 ZOM-293 ZOM-435 ZOM-449 ZOM-458 ZOM-473 ZOM-483 ZOM-535 ZOM-546 ZOM-554 ZOM-559 ZOM-560 ZOM-562 "
            "ZOM-567 ZOM-569 ZOM-573 ZOM-576 ZOM-578").split()
FIXED = "ZOM-429 ZOM-434 ZOM-503 ZOM-506 ZOM-517 ZOM-557 ZOM-558 ZOM-561 ZOM-563 ZOM-564".split()
assert len(KNOWN) == 19 and len(NOCALL) == 85 and len(BLOCKERS) == 18 and len(FIXED) == 10
ALL = KNOWN + NOCALL + BLOCKERS + FIXED
assert len(set(ALL)) == 132
lit = lambda xs: " ".join(f"`{x}`" for x in xs)
w(f"| G1 register calls outside the BLOCKER class | F17 F19 F20 F22 F23 (114 of 132: 10 FIXED, 19 KNOWN ISSUE, 85 NO "
  f"CALL): {lit(FIXED + KNOWN + NOCALL)} | samples: {pn('fix_429')} ZOM-429 (edge: open in Linear, QA could not "
  f"reproduce), {pn('fix_563')} ZOM-563 (edge: server fix confirmed on prod while In Progress), {pn('smp_art793')} ART-793 (edge: "
  f"Art-team ticket brought in by the 'ZM in the title' rule), {pn('smp_481')} ZOM-481 (ordinary known issue), "
  f"{pn('smp_536')} ZOM-536 (edge: Bug label and Done after the cut, an art ask). Direct exception rows, not samples: "
  f"{pn('fix_558')} ZOM-558 and {pn('smp_477')} ZOM-477 (Leonard's per-ticket rulings). The BLOCKER class (19, {rng('reg_')}) is graded in full | {pn('count133')} | "
  f"none — bundle (Rubric Writing §7; Eval 2.2) | no: the prompt asks for the register as a whole; routine calls are "
  f"repetitive members |")
w(f"| G2 register build status | F9 F20 F31 F32 (133 rows) | samples: {pn('bs_473')} ZOM-473 (edge: in candidate by the "
  f"Done branch although the re-test fails), {pn('bs_429')} ZOM-429 (edge: in candidate by the QA-could-not-reproduce "
  f"branch), {pn('bs_477')} ZOM-477 (ordinary n/a, a no-call ticket). Direct exception rows, the three non-default values: "
  f"{pn('bs_569')} ZOM-569 (not in candidate: fix after the Started lines), {pn('bs_567')} ZOM-567 (server - not live: code "
  f"deployed, data load not run), {pn('bs_563')} ZOM-563 (server - live) | {pn('count133')} | none — bundle (Rubric "
  f"Writing §7; Eval 2.2) | no |")
w(f"| G3 register QA result | F18 (133 rows) | {pn('qa_449')} ZOM-449 (ordinary latest check), {pn('qa_559')} ZOM-559 "
  f"(edge: latest of three checks, the Sep 22 tab says 'not reproduced') | {pn('count133')} | none — bundle (Rubric "
  f"Writing §7; Eval 2.2) | no |")
w(f"| G4 register evidence | F11 F28 (133 rows) | {pn('ev_435')} ZOM-435 (deciding record on Trello), {pn('ev_563')} "
  f"ZOM-563 (deciding record a Slack DM that overrides the In Progress state) | {pn('count133')} | none — bundle (Rubric Writing §7; "
  f"Eval 2.2) | no |")
w(f"| G5 register title | F13 (133 rows) | {pn('title_546')} ZOM-546 (ordinary) | {pn('count133')} | none — bundle "
  f"(Rubric Writing §7; Eval 2.2) | no |")
w(f"| G6 ZOM-570 blocker list (graded in full, not sampled) | F39 (19): {lit(BLOCKERS)} plus the new ticket | all 19 members "
  f"have their own rows, {pn('z_293')} to {pn('z_des313')} and {pn('z_new')} | {pn('z_count')} | none — bundle "
  f"(Rubric Writing §7; Eval 2.2) | no sampling: every member is graded directly |")
w("")
n_out = len(rows)
w("## E · Summary")
w(f"Rows {len(rows)} · Outcome {n_out} · Process candidates 0 · ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · fewer than two "
  f"Process rows failing the three-condition test ☑ (none written; §C) · builder minimum 5 ☑ · one volume row per sampled "
  f"output, no bundled exact-set row ☑ ({pn('count133')} for G1 to G5, {pn('z_count')} for the blocker list) · predicted "
  f"all-fail rows = 0 ☑")
w("Failure diversity: largest unit of discovery reported by the gate line in the Self-review (≤ 50% ☒: Leonard's rules "
  "doc F6 is in the Depends-on closure of nearly every row, because its scope sentence defines the population every call "
  "row grades; it is named by ZOM-570 (the release ticket the prompt sends the run to), the task's hub, not a hidden "
  "discovery; the same structural finding recorded on the Robert, Douglas, Julia and Frederick tasks) · chains landing on "
  f"distinct rows ☑ (CH1 ZOM-569 {pn('reg_569', 'bs_569', 'z_569')}; CH2 ZOM-435 {pn('reg_435', 'ev_435', 'z_435')}; CH3 "
  f"update path {pn('new_issue', 'reg_new', 'z_new')}; CH4 ZOM-562 {pn('reg_562', 'z_562')}; CH5 ZOM-563 "
  f"{pn('fix_563', 'bs_563', 'ev_563')}; CH6 other-team tickets {pn('reg_des313', 'smp_art793', 'count133')}; the earlier baseline "
  "batch on this SQL measured differing failed-row sets across runs)")
w(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} · total weight {tw}")
w(f"Format 5 (§A3): rows {len(rows)}/{len(rows)} ☑ · `do_nothing_case` REJECT {len(rows)}/{len(rows)} ☑ · reachability "
  f"`PROMPT_LINKED` {len(rows)}/{len(rows)} ☑ · final-reply test ACCEPT ☑")
w(f"Set size: {len(rows)} rows for a 133-row register, a 19-key blocker list, one new ticket and one reply (reference: 31 "
  f"criteria for a ~10-hour task; ~60 signals duplicate grading, ~12 missing coverage). The size comes from grading the "
  f"two gate-deciding classes and the blocker list in full instead of sampling them; no fact is graded in three rows")
w("Coverage: requirements 7/7 (ledger R1 to R7, R7 timing by " + pn('s_time') + ") · OEs 35/35 (§B) · writes 5/5 (tab, "
  "register values, ZOM-570 description, new issue, thread reply), each with a wrong-target guard · told facts 1/1 (the QA "
  "call, in the reply the prompt names) · friction 0/0 (Friction: none)")
w("Gradable surface (gate 17): slots 33 · covered 27 · dispositioned 6 (§G: S24 to S29 sampled out, gate 15 cap) · no "
  "slot with neither ☑ · mechanism share reported in §G (not gated)")
w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; ZOM-570, its comment, the docs and card it "
  "names, the How we gate tab and the runbook are incorporated by the prompt) ☑ conclusions on ambiguous evidence (each "
  "graded value is settled by the latest dated record; 12 baseline runs agree on every non-trap call) ☑ grading the "
  "distractor (traps are graded through the correct value, never their disclosure) ☑ hard-coded titles/phrasings (only "
  "the How we gate vocabulary and the candidate build numbers in the tab name, which the sheet fixes)")
w("Blocking: none for validity: no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share is "
  "a structural finding (Leonard's rules doc), recorded under Unresolved.")
w("")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
w("")
vis = HERE / "visibility.txt"
w(vis.read_text().rstrip() if vis.exists() else "(pending)")
w("")
w("## F · Shortcut probe")
probe = HERE / "probe.txt"
w(probe.read_text().rstrip() if probe.exists() else "(pending)")
w("")
w("## G · Gradable-surface coverage")
w("| Slot | Stable fact ID | Selector · role / group | Work kind (band) | Mechanisms → Decided by | Covered by (P-n) | "
  "Disposition and reason (evidence) |")
w("|---|---|---|---|---|---|---|")
surf = json.loads((TI / "Working_Files/01_Gradable_Surface.json").read_text())
cover = {"S01": "reg_569", "T01": "z_569", "S03": "reg_567", "T02": "z_567", "S05": "reg_435", "T03": "z_435",
         "S07": "reg_473", "T05": "z_473", "B01": "new_issue", "S09": "reg_562", "T04": "z_562", "S11": "smp_art793",
         "S12": "reg_des313", "S13": "reg_578", "S14": "fix_563", "S31": "reg_458", "T06": "z_458", "S32": "reg_535",
         "T08": "z_535", "S30": "reg_293", "T07": "z_293", "S20": "reg_559", "S21": "reg_560", "S22": "smp_481",
         "V01": "count133", "D01": "s_thread", "D02": "s_call"}
SAMPLED_OUT = {"S24": ("ZOM-564", "fixed: Brian's check on both candidates, like ZOM-429 (" + pn('fix_429') + ")"),
               "S25": ("ZOM-506", "fixed by Vincent's Sep 30 re-check post C08R27X0EAH/1759274400.792657, an ordinary member"),
               "S26": ("ZOM-557", "fixed by Vincent's Sep 30 re-check post C08R27X0EAH/1759274400.792657, an ordinary member"),
               "S27": ("ZOM-561", "fixed by Vincent's Sep 30 re-check post C08R27X0EAH/1759274400.792657, an ordinary member"),
               "S28": ("ZOM-513", "an ordinary art-request no call, like ZOM-536 (" + pn('smp_536') + ")"),
               "S29": ("ZOM-387", "an ordinary analytics no call")}
mech_w = 0
for s in surf["slots"]:
    sel = cell(" ".join(map(str, s["selector"])))
    if s["id"] in SAMPLED_OUT:
        key, why = SAMPLED_OUT[s["id"]]
        w(f"| {s['id']} | {key}.call | {sel} · {s['role']} / {s.get('group') or 'none'} | {s['work_kind']} ({s['weight']}) | "
          f"{', '.join(s.get('mechanisms') or []) or 'none'} → H2 | none | sampled out: G1 holds five samples (ZOM-429, "
          f"ZOM-563, ART-793, ZOM-481, ZOM-536) plus two direct exception rows under gate 15's cap; {key} is {why}, and its row "
          f"still counts in {pn('count133')} |")
        continue
    t = cover[s["id"]]
    r = rows[int(TAG[t][1:]) - 1]
    if s.get("mechanisms"):
        mech_w += r["w"]
    w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {sel} · {s['role']} / {s.get('group') or 'none'} | {s['work_kind']} "
      f"({r['w']}) | {', '.join(s.get('mechanisms') or []) or 'none'} → {r['dec']} | {TAG[t]} | covered: the title rejects "
      f"both the omission and the trap value ({cell(r['alt'])}) |")
w(f"Mechanism share: {round(100 * mech_w / tw)}% of the weight sits on rows covering a slot a designed mechanism can flip "
  f"(reported, not gated)")
w("")
sr = HERE / "selfreview.md"
w(sr.read_text().rstrip() if sr.exists() else "## Self-review\n(pending)")
(TI / "Working_Files/09_Rubric_Writing_Plan.md").write_text("\n".join(out) + "\n")
print("plan written:", len(out), "lines; weight", tw, dict(bands))
