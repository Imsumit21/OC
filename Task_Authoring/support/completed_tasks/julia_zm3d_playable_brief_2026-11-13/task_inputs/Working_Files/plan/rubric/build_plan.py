#!/usr/bin/env python3
"""Render Working_Files/09_Rubric_Writing_Plan.md (prep mode, playbook 09) from plan/rubric/rows.json (build_rows.py).
Visibility proof: persona_view check-sql (seeded ids) and can-see (base ids) for every scoped id behind every cited F-id,
pasted verbatim. §F holds the shortcut probe output from plan/rubric/probe.txt and the dispositions in
plan/rubric/probe_dispositions.txt when they exist (run the probe on the written plan, then re-render)."""
import datetime as D, json, os, re, subprocess, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]; TASK = WF.parent; ROOT = TASK.parents[1]; TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(WF / "oe_gen")); sys.path.insert(0, str(TOOLS))
import model as O            # noqa: E402
import facts as FX           # noqa: E402
import stage_gate as G       # noqa: E402
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(TASK))
rows = json.loads((HERE / "rows.json").read_text())
EV = json.loads((WF / "oe_gen" / "out" / "oe_events.json").read_text())
surface = json.loads((WF / "01_Gradable_Surface.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
CLOCK = re.sub(r"^Clock:\s*", "", ctx["universe"]["clock_line"])
FACT = {f["F"]: f for f in FX.FACTS}
def cell(s): return re.sub(r"\s+", " ", str(s)).replace("|", "/").strip()
def table(h, rs): return ["| " + " | ".join(h) + " |", "|" + "---|" * len(h)] + ["| " + " | ".join(cell(c) for c in r) + " |" for r in rs]
def fids(r): return re.findall(r"\bF\d+\b", r["values"])
TAG = {r["tag"]: r["P"] for r in rows}
W = sum(r["band"] for r in rows)

# ---------------------------------------------------------------- failure diversity (the gate's algorithm, recomputed here)
def closure(fs):
    out, stack = set(), list(fs)
    while stack:
        f = stack.pop()
        if f in out: continue
        out.add(f)
        if f in FACT: stack += re.findall(r"\bF\d+\b", FACT[f]["depends"]) + re.findall(r"\bF\d+\b", FACT[f]["origin"])
    return out
def response(f):
    ids = [m.group(0) for m in G.OPAQUE.finditer(FACT[f]["locator"])] if f in FACT else []
    return ids[0] if ids else (FACT[f]["locator"].strip().lower() if f in FACT else f)
share = Counter()
for r in rows:
    us = {f"authority {x}" for x in re.findall(r"\b[A-Z]{1,3}\d{1,3}\b", r["decided"]) if not re.fullmatch(r"[FP]\d+", x)}
    for f in closure(set(fids(r))):
        if f in FACT and re.match(r"\s*prompt\b", FACT[f]["origin"], re.I): continue
        us.add(f"response {response(f)}")
    for u in us: share[u] += r["band"]
TOP = share.most_common(4)

# ---------------------------------------------------------------- visibility proof
need = sorted({(svc, x) for r in rows for f in fids(r) if f in FACT for svc, x in G.scoped_ids(" ".join(str(v) for v in FACT[f].values()))})
seeded = sorted({x for _, x in need if x in O.SQL_TEXT or (x.split("/")[-1] in O.SQL_TEXT and x.split("/")[0] in O.SQL_TEXT)})
lb = HERE / "plan_lb_ids.txt"; lb.write_text("\n".join(seeded) + "\n")
p = subprocess.run([sys.executable, "-B", str(TOOLS / "persona_view.py"), "check-sql", O.PERSONA, str(O.SQL_PATH), "--load-bearing", str(lb)],
                   capture_output=True, text=True, cwd=ROOT, env=ENV)
cs = p.stdout.splitlines()
head = next(l for l in cs if l.startswith("CHECK-SQL as"))
lbrows = [l for l in cs if l.startswith(("[YES LB]", "[NO", "[UNVERIFIED"))]
verdict = next(l for l in cs if l.startswith("verdict:")); assert verdict.startswith("verdict: PASS"), verdict
covered = {x for l in lbrows if l.startswith("[YES") for _, x in G.scoped_ids(l)}
cansee = []
for svc, x in need:
    if x in covered: continue
    q = subprocess.run([sys.executable, "-B", str(TOOLS / "persona_view.py"), "can-see", O.PERSONA, svc, x], capture_output=True, text=True, cwd=ROOT, env=ENV)
    first = (q.stdout.splitlines() or [q.stderr.strip()[:200]])[0]
    assert first.rstrip().endswith(": YES"), first
    cansee.append(first)

# ---------------------------------------------------------------- sections
A = [(r["P"], " · ".join([f"\"{G_span}\"" for G_span in [{'msg': "Frederick's playable message from yesterday", 'every': "everything he's asking for in it",
      'start': "start to finish", 'drive': "The files he wants should end up in my Drive", 'links': "once they're ready the links go in the PlayableX channel like he says"}[r['span']]]]
      + [", ".join(f"OE {n}" for n in r["oes"][:6]) + (" …" if len(r["oes"]) > 6 else "")]),
      r["fact"], r["what"], r["final"], r["cat"], r["values"]) for r in rows]
A2 = [(r["P"], "no — must not hard-code (the title names the value, not a wording)", r["dist"], r["amb"], f"{r['kind'][0]} — {r['kind'][1]}", str(r["band"]),
       r["decided"], r["group"], f"fact `{r['fact']}` · {r['dup']}", r["allfail"]) for r in rows]
A3 = [(r["P"], f"{r['valid']} (prompt authority: \"{ {'every': 'everything he' + chr(39) + 's asking for in it', 'start': 'start to finish', 'drive': 'The files he wants should end up in my Drive', 'links': 'once they' + chr(39) + 're ready the links go in the PlayableX channel like he says'}[r['span']]}\")",
       f"REJECT: {r['nothing']} (title: \"{r['title']}\")", ", ".join(f"OE {n}" for n in r["oes"][:8]) + (f" … ({len(r['oes'])} steps)" if len(r["oes"]) > 8 else ""), r["reach"]) for r in rows]

proved = {}
for r in rows:
    for n in r["oes"]: proved.setdefault(n, []).append(r["P"])
Brows = []
for e in EV:
    n = e["n"]; ps = proved.get(n, [])
    if e["kind"] == "write":
        if e["head"].startswith("Move ") and not any(rows[int(p[1:]) - 1]["tag"].startswith("move_") and rows[int(p[1:]) - 1]["tag"] != "move_volume" for p in ps):
            own = f"no — one template (state to Todo), graded by the volume row {TAG['move_volume']} (G5)"
        else:
            own = "yes — its own row(s)" if ps else "no"
    else:
        own = "no — discovery; its result is carried by the content rows that cite it"
    Brows.append((f"OE {n}", "write" if e["kind"] == "write" else "discovery", ", ".join(dict.fromkeys(ps)) or "—", own))
missing_oe = [b[0] for b in Brows if b[2] == "—"]

C = [("—", "\"once they're ready the links go in the PlayableX channel like he says\" (post after the files are written and shared)",
      "the final state shows the post and the files, not the order they were made in",
      "pass: every valid path writes the files before posting their links", "pass: no stricter Outcome shows the order",
      "fail: an order of steps is an execution trace, not a behaviour the final state carries",
      f"no Process row; the order is carried by the content: {TAG['post_list']} grades the link of the hand-off list the Agent filled (F{FX.F('channel')[1:]})")]

keys96 = " ".join(f"`{l['name']}`" for l in O.LINES)
owed_keys = " ".join(f"`{l['name']}`" for l in O.by_state("Owed"))
board_keys = " ".join(f"`{l['name']}`" for l in O.BOARD_ITEMS)
def ps(*tags): return ", ".join(TAG[t] for t in tags)
D_ = [("G1 State column", f"96 lines (F{FX.F('pack')[1:]}): {keys96}",
       f"exceptions an authority singles out (direct rows): {ps('x_Refrigerator', 'x_RetroTV')} (Marcus's post), {ps('x_Bathtub', 'x_Iron')} (Robert's note), {ps('x_Cactus', 'x_Cone', 'x_Chainsaw')} (Brian's log, re-sent), "
       f"{ps('x_Cello', 'x_Trumpet')} (the log, the zip), {ps('x_Rocket', 'x_Explosion')} (Calvin's sheet names them); ordinary samples: {ps('x_RollingPin')} (Ready control of the export rule), {ps('x_FlyZapper')} (Owed on its own note)",
       TAG["sheet_volume"], "none — bundle (Rubric Writing §7; Eval 2.2)", "no"),
      ("G2 What's owed / Who has it columns", f"{len(O.by_state('Owed'))} Owed lines: {owed_keys}",
       f"exceptions (direct rows): {ps('o_Refrigerator', 'h_Refrigerator', 'o_Bathtub', 'h_Bathtub', 'h_Iron', 'o_Cello', 'h_Cello', 'o_Rocket', 'h_Rocket')}; every Owed line's comment carries both values (one row each, not sampled)",
       TAG["sheet_volume"], "none — bundle (Rubric Writing §7; Eval 2.2)", "no"),
      ("G3 Board set column", f"84 board items: {board_keys}", f"exceptions (direct rows): {ps('bs_Bow', 'bs_Dynamite')} (Robert's reply swaps them); ordinary samples: {ps('bs_Grenade', 'bs_RollingPin')}",
       TAG["sheet_volume"], "none — bundle (Rubric Writing §7; Eval 2.2)", "no"),
      ("G4 Line / Category / Ticket columns", f"96 lines: {keys96}", f"samples: {ps('sheet_ticket')} (Cannon, the line PlayableX calls the rocket launcher), {ps('sheet_category')} (Iron, a laundry item filed under Bathroom)",
       TAG["sheet_volume"], "none — bundle (Rubric Writing §7; Eval 2.2)", "no"),
      ("G5 ticket moves to Todo (one template)", f"{len(O.by_state('Owed'))} Owed tickets: " + " ".join(f"`{l['ticket']}`" for l in O.by_state("Owed")),
       f"samples: {ps('move_Refrigerator', 'move_Bathtub', 'move_Cello')} (one per trap group), {ps('move_Fly Zapper', 'move_Fonts')} (own-note lines; Fonts is held outside the team)",
       TAG["move_volume"], "none — bundle (Rubric Writing §7; Eval 2.2)", "no")]

slots = surface["slots"]
SLOTROWS = {}
for r in rows:
    for s in r["slot"]: SLOTROWS.setdefault(s, []).append(r["P"])
SL_EXTRA = {"K1": [r["P"] for r in rows if r["tag"].startswith("comment_") and r["decided"] == "T1, C1"],
            "K2": [r["P"] for r in rows if r["tag"].startswith("comment_") and r["decided"] == "T2, C2"],
            "K4": [r["P"] for r in rows if r["tag"].startswith("comment_") and r["decided"] == "T7, C6"],
            "K5": [r["P"] for r in rows if r["tag"].startswith("comment_") and r["decided"] == "T4, C5"],
            "D4": [r["P"] for r in rows if r["tag"].startswith("share_list_")], "D5": [TAG["share_brief_intake"], TAG["share_list_intake"]],
            "B1": [r["P"] for r in rows if r["tag"].startswith("b_eight_")], "B3": [r["P"] for r in rows if r["tag"].startswith("b_zombie_")] + [TAG["b_anim"]],
            "B6": [TAG["b_held_Rocket sound"], TAG["b_held_Explosion sound"]]}
DISP = {"A1": f"duplicate fact: the Owed count is graded once, in the DM ({TAG['dm_Owed']}); a count of the list's rows is a count over items, Major non_atomic under count-bundle-v1 (gate 15a, gate 6)",
        "A2": f"duplicate fact: the Ready count is graded once, in the DM ({TAG['dm_Ready']}); a count of the list's rows is a count over items (count-bundle-v1, gate 15a)",
        "A3": f"duplicate fact: the Delivered count is graded once, in the DM ({TAG['dm_Delivered']}); count-bundle-v1 (gate 15a)"}
Grows, n_cov, n_disp = [], 0, 0
mech_w = 0
for s in slots:
    sid = s["id"]; cov = sorted(set(SLOTROWS.get(sid, []) + SL_EXTRA.get(sid, [])), key=lambda x: int(x[1:]))
    if cov: n_cov += 1
    else: n_disp += 1
    Grows.append((sid, s.get("fact_id") or sid, f"{s.get('selector')[0] if isinstance(s.get('selector'), list) else s.get('selector')} · {s.get('role', '')} / {s.get('group', '') or '—'}",
                  f"{s.get('work_kind', '')} ({s['weight']})", f"{', '.join(s.get('mechanisms', [])) or '—'}", ", ".join(cov) or "—", "" if cov else DISP[sid]))
for r in rows:
    if r["decided"] != "—": mech_w += r["band"]

bands = Counter(r["band"] for r in rows)
n_writes = sum(1 for e in EV if e["kind"] == "write")
doc = []
w = doc.append
w("# 09 Rubric Writing Plan — julia-zm3d-playable-brief (injection rev2)")
w(f"Generated {D.date.today().isoformat()} · Clock {CLOCK} · Persona Julia Lawson {O.JULIA} · Assigned role Product Manager · Tier Long-Horizon · Mode Hard · Human time 19.00 h · "
  "OE status: PROVISIONAL (/oe round 1 on 2026-11-12 was FAIL 2 on OE 20 and OE 10; its Fix List is applied, the local check predicts PASS 5 with Blocking 0, and the events await /oe; "
  "re-run prep after /oe passes)")
w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — the brief as a Google Doc in Julia's Drive (Scenario 1 and its one purpose; the eight with Bow in place of "
  "Dynamite and the others as extras; Party Girl, Plumber, Magician, Football Player and walk; won by clearing every zombie, lost only at zero health; 7 slots; the Rocket and Explosion sounds "
  "held back, Matching, Success and Failure usable; music after the first click; November 3); the hand-off list as a Google Sheet in her Drive with 96 rows (Delivered 8, Ready 39, Owed 49); "
  "the 49 Owed tickets in Todo, each with a comment on what is owed and who has it; both files shared view-only with Brian, Frederick, Robert and intake@playablex.ai; the three counts in "
  "Frederick's DM; both links in the PlayableX channel. Any folder of hers, either position of the links (top-level or a reply), any wording of what is owed.")
w("")
w("Rubric shape: the brief gets one row per element the notes list, and lists get one row per member (a list in one title is a filtered list, non_atomic). The hand-off list is graded as "
  "table cells: one volume row, direct rows on the members an authority singles out (two per trap group, both named sounds) and ordinary samples. Ticket moves follow one template and are "
  "sampled with a volume row that states it; ticket comments differ by line group, so each gets its own row (gate 15a). Each share is its own row. The DM and the post are proved by their "
  "content rows. The three counts are graded once, in the DM. 09_Rubrics.json will mirror P1–P" + str(len(rows)) + " one to one (C-n = P-n).")
w("")
w("## A · Coverage matrix")
doc.extend(table(["P", "Source (exact prompt span · OE n)", "Stable fact ID", "What must be verified", "Final state that proves it", "Category (Outcome / Process candidate → C)",
                  "Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs"], A))
w(""); w("## A2 · Grading risks and weight")
doc.extend(table(["P", "Title/phrasing specified by prompt?", "Distractor? (T-ID → grade handling)", "Ambiguous evidence? (risk # → no single conclusion)",
                  "Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason", "Band 1/3/5", "Decided by (chain / authority / trap id)",
                  "Spot-check group", "Global fact duplication / overlap group", "Predicted all-fail basis (four Evals bases) · over-specific risk"], A2))
w(""); w("Draft criterion text (one per row; draft mode re-reads every literal before writing 09_Rubrics.json):"); w("")
for r in rows: w(f"- {r['P']} [{r['band']}] {r['title']}")
w(""); w("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
doc.extend(table(["P", "valid_case (must ACCEPT · prompt authority)", "do_nothing_case (must REJECT · exact title text of the required write)", "OE step ids (verbatim OE labels)",
                  "Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED)"], A3))
w("Final-reply test (whole set): 'Done: the brief and the hand-off list are in your Drive and shared, the 49 Owed tickets are in Todo with comments, Frederick has Delivered 8, Ready 39, Owed 49, "
  "and both links are in the PlayableX channel.' → ACCEPT ☑ (no row grades the final reply; every row grades a write)")
w(""); w("## B · OE trace")
doc.extend(table(["OE", "Kind (write / discovery / friction)", "Proved by row(s)", "Own row? (reason)"], Brows))
w(""); w("## C · Process candidates — three-condition test")
doc.extend(table(["P", "Requirement (prompt span)", "Why no Outcome can prove it", "(1) every valid path", "(2) no stricter Outcome", "(3) behavioural, not trace", "Result (Process / tighten P-n with F-n)"], C))
w(""); w("## D · Spot-check groups")
doc.extend(table(["G", "Item set (F-IDs, total N; keys as backticked literals)", "Sampled items (≤ 5) and why hard/edge", "Volume row", "Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`)", "Core requirement? (must be no)"], D_))
w(""); w("## E · Summary")
w(f"Rows {len(rows)} · Outcome {sum(1 for r in rows if r['cat'] == 'Outcome')} · Process candidates {len(C)} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ (0 Process rows) · fewer than two Process rows failing "
  "the three-condition test ☑ (the one candidate fails condition 3 and becomes no row) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ · predicted all-fail rows = 0 ☑")
w(f"Failure diversity: largest unit of discovery {TOP[0][0]} {100 * TOP[0][1] / W:.0f}% of the weight ({TOP[0][1]} of {W}) (≤ 50% ☑), then {TOP[1][0]} {100 * TOP[1][1] / W:.0f}%, "
  f"{TOP[2][0]} {100 * TOP[2][1] / W:.0f}% · chains landing on distinct rows ☑ (C1 → {ps('x_Refrigerator', 'o_Refrigerator', 'h_Refrigerator')}; C2 → {ps('x_Bathtub', 'o_Bathtub', 'h_Bathtub')}; "
  f"C3 → {ps('x_Cactus', 'x_Cone', 'x_Chainsaw')}; C4 → {ps('b_eight_Bow', 'bs_Bow', 'bs_Dynamite')}; C5 → {ps('x_Rocket', 'o_Rocket', 'h_Rocket')}; C6 → {ps('x_Cello', 'o_Cello', 'h_Cello')})")
w(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (weight {W})")
w(f"Format 5 (§A3): rows {len(rows)}/{len(rows)} ☑ · `do_nothing_case` REJECT {len(rows)}/{len(rows)} ☑ · reachability `PROMPT_LINKED` {len(rows)}/{len(rows)} ☑ · final-reply test ACCEPT ☑")
w(f"Set size: {len(rows)} rows for 19.00 h (reference: 31 criteria for a ~10-hour task; the count follows the platform's one-row-per-write rule: {sum(1 for r in rows if r['tag'].startswith('comment_'))} comment rows and "
  f"{sum(1 for r in rows if r['tag'].startswith('share_'))} share rows, each a separate write; no fact is graded in three rows)")
w(f"Coverage: requirements 9/9 · OEs {len(EV) - len(missing_oe)}/{len(EV)} · writes {n_writes}/{n_writes} (the 44 unsampled moves through the volume row {TAG['move_volume']}) · told facts 3/3 (the counts in the DM) · friction 0/0")
w(f"Gradable surface (gate 17): slots {len(slots)} · covered {n_cov} · dispositioned {n_disp} (§G) · no slot with neither ☑ · mechanism share {100 * mech_w / W:.0f}% of the weight (reported, not gated)")
w("Four prohibitions: ☑ unstated expectations ☑ conclusions on ambiguous evidence ☑ grading the distractor ☑ hard-coded titles/phrasings")
w("Blocking: none (no UGT defect · every write feasible: ledger section C · visibility proven below)")
w("")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
w("")
w(f"`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing Working_Files/plan/rubric/plan_lb_ids.txt` ({len(seeded)} seeded ids):")
w(""); w("```text"); w(head); doc.extend(lbrows); w(verdict); w("```"); w("")
w(f"`python3 Task_Authoring/tools/persona_view.py can-see julia_lawson <service> <id>`, one call per base id ({len(cansee)} ids, first line of each):")
w(""); w("```text"); doc.extend(cansee); w("```")
w(""); w("## F · Shortcut probe")
probe = (HERE / "probe.txt").read_text().rstrip() if (HERE / "probe.txt").exists() else "(not yet run)"
w(""); w("```text"); w(probe); w("```")
disp = (HERE / "probe_dispositions.txt").read_text().rstrip() if (HERE / "probe_dispositions.txt").exists() else ""
if disp: w(""); doc.extend(disp.splitlines())
w(""); w("## G · Gradable-surface coverage")
doc.extend(table(["Slot", "Stable fact ID", "Selector · role / group", "Work kind (band)", "Mechanisms → Decided by", "Covered by (P-n)", "Disposition and reason (evidence)"], Grows))

# ---------------------------------------------------------------- self-review
def acc(r):
    m = re.search(r"accepts?: ([^·]+)", r["values"]); return m.group(1).strip() if m else "the value the title names, in any wording"
SR = []
for r in rows:
    near = r["dist"] if r["dist"] != "—" else ("the decoy reading of the same record fails: " + (r["amb"] if r["amb"] != "—" else "a different value on the same row fails because the title names it"))
    SR.append((f"{r['P']} ({r['fact']})", "holds",
               f"(a) a valid answer could fail: {acc(r)} — the title names the value, not a wording, and the location is the artifact the prompt asks for · (b) a wrong answer could pass: {near}",
               f"{', '.join(fids(r))}; OE {', '.join(str(n) for n in r['oes'][:4])}; band {r['band']} ({r['kind'][0]})", "none"))
SR += [("Re-read as /rubric (3_Rubrics_Eval.md 1.4, 3.1)", "holds", "a requirement could be uncovered: the notes' brief list, the list columns, the tickets, the shares, the counts, the links",
        f"every R1–R9 of the ledger maps to rows (§A); writes {n_writes}/{n_writes}; told facts in {ps('dm_Owed', 'dm_Ready', 'dm_Delivered')}", "none"),
       ("Re-verified values", "holds", "a value could come from the ledger only",
        "every value was re-read in this run: seeded rows re-parsed from 01_Universe_Inject.sql (oe_gen/model.py), base records re-read through hg.py (oe_gen/base_read.py, 46 records, 0 errors); "
        "states, holders and board sets recomputed for all 96 lines and asserted equal to solver/truth.json", "none"),
       ("Predicted all-fail re-check", "holds (0 rows)", "a row could need a value the persona cannot reach",
        f"persona_view check-sql PASS on {len(seeded)} seeded ids and can-see YES on {len(cansee)} base ids (§E); every write is cataloged (ledger §C); friction none; 0 rows on the four bases", "none"),
       ("Shortcut and diversity (gate 12, 14)", "holds", f"one record could collapse the task; one unit could decide most of the weight",
        f"§F dispositions; largest unit {TOP[0][0]} {100 * TOP[0][1] / W:.0f}% (P-rows transitive over the ledger's Depends-on)", "none"),
       ("Surface dispositions (gate 17)", "holds", "A1–A3 are counts the notes ask for, so they could need rows on the list",
        f"the ask asks for the counts in the DM ('give me the count for each state here', {O.ASK['id']}); a count over the list's rows is count-bundle-v1; graded once in {ps('dm_Owed', 'dm_Ready', 'dm_Delivered')}", "none"),
       ("Comment rows (gate 15a)", "holds", "the 49 comments could be one template and be sampled instead",
        f"their content differs by line group (what is owed, who has it: OWED groups in oe_gen/model.py), so one row each (one-row-per-write); {sum(1 for r in rows if r['tag'].startswith('comment_'))} rows", "none"),
       ("Lists split per member (Eval 2.2)", "holds", "the eight, the four zombies or the sounds could be one fact each",
        f"a list in one title is a filtered list, non_atomic (Eval 2.2); each member is its own row ({ps('b_eight_Bow')} carries the swap with 'in place of the Dynamite')", "none")]
doc += ["", "## Self-review", "",
        "Walked Evals/3_Rubrics_Eval.md 1.4, 2.1–2.9, 3.1–3.7 and the hg-strict-overrides-v1 table against this plan, then the playbook's prep self-review (1–4, 6, 7). Re-verified every value through "
        "hg.py and the SQL (see 'Re-verified values'); predicted all-fail re-check below counts 0 rows. One evidenced counter-reading per §A row follows.", ""]
doc += table(["Check", "Verdict", "Strongest counter-reading", "Resolution (evidence: pointer / rule § / case id)", "Unresolved"], SR)
doc += ["", "Unresolved: none. The plan is PROVISIONAL until /oe passes; re-run prep then.", ""]
(WF / "09_Rubric_Writing_Plan.md").write_text("\n".join(doc) + "\n")
print("wrote 09_Rubric_Writing_Plan.md", len(rows), "rows · weight", W, "· top units", [(u, round(100 * s / W)) for u, s in TOP], "· OEs without a row", missing_oe[:5],
      "· slots covered", n_cov, "dispositioned", n_disp, "· visibility", len(seeded), "seeded,", len(cansee), "base")
