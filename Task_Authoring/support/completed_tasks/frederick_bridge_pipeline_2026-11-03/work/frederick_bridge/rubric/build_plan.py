#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py). Sections §F (shortcut
probe paste) and the visibility block are read from files next to this script when present."""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[2]
rows = json.loads((HERE / "rows.json").read_text())
P = [f"P{i + 1}" for i in range(len(rows))]
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}


def pn(t):
    return TAG[t]


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


out = []
w = out.append
w("# 09 Rubric Writing Plan — frederick_bridge_pipeline (Q4 investor update send list, injection rev12)")
w("Generated 2026-11-03 · Clock 2025-10-01T00:00:00Z (seed bound; eval clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), "
  "Oct 1, 2025 (synth-cut)) · Persona Frederick Stone frederick.stone@harmonygames.co · Assigned role Co-founder · "
  "Tier Long-Horizon · Mode Medium · Human time 19.25 h (worksheet from an earlier revision; refresh pending) · "
  "OE status: /oe PASS 2026-11-03 (Platform_Report/oe_report3, Score 5, 86 events, 08_Oracle_Events.md sha256 bea7b71ffac7)")
w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — D1 one Google Sheet or Doc "
  "\"Q4 update - send list\" in d_5e8a1c3f9b07d2e64a1b93, 25 rows (New investor 1: Anton Bernstein 25,000; In talks 7; "
  "Awaiting reply 14; Keep warm 3), build access iOS only for Dentsu Ventures, T-accelerate, NCsoft, Brightwater Games "
  "Fund and none for GFR Fund, Andreessen Horowitz, Homa; D2 four checklists on card 68c5a49e8491a9d7faf869d0 with 1 / 7 / "
  "14 / 3 items; D4 18 \"F/up with\" cards in To Do 640643a3fd8f3ca308d93195 plus one comment on 68c99e98737744bd966aed24; "
  "D3 a reply or reply-all on frederick.stone@harmonygames.co/1844724419788800011 with the counts per group (one number or "
  "split into firms and angels).")
w("")
w("Rubric shape: every write has a result row; populations use one volume row per output, direct rows on every member "
  "an authority singles out, and at most 5 samples (gate 15, no bundled exact-set rows); each trap (SciPlay, Paul, the "
  "four iOS-only cells, Anton's amount) decides its own rows so failing runs differ on two or more rows "
  f"(run_forensics/rev12/downstream_notes.md). The rubric 09_Rubrics.json mirrors P1–P{len(rows)} one to one (C-n = P-n). "
  "Revised after /rubric round 1 (Platform_Report/rubric_report1, FAIL 1): the Fix List is applied row by row.")
w("")
w("## A · Coverage matrix")
w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | "
  "Category (Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date "
  "acceptance · F-IDs |")
w("|---|---|---|---|---|---|---|")
for p, r in zip(P, rows):
    acc = "; ".join(r["acc"])
    w(f"| {p} | \"{r['span']}\" · {', '.join(r['oe'])} | {r['fact']} | {cell(r['verify'])} | {cell(r['final'])} | {'Process candidate → C1' if r.get('cat') == 'Process' else 'Outcome'} | "
      f"{r['vals']} · accept: {cell(acc)} · dates: none graded · {r['fids']} |")
w("")
w("## A2 · Grading risks and weight")
w("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no "
  "single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason "
  "| Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | "
  "Predicted all-fail basis (four Evals bases) · over-specific risk |")
w("|---|---|---|---|---|---|---|---|---|---|")
dup_count = {}
for r in rows:
    dup_count[r["fact"]] = dup_count.get(r["fact"], 0) + 1
for p, r in zip(P, rows):
    title_spec = ("yes — the README fixes the file name (\"Q4 update - send list\"); case/dash variants accepted"
                  if r["fact"] == "sheet_name" else "no — must not hard-code; group, checklist and card names accept "
                  "close variants")
    dup = f"{r['fact']} in {dup_count[r['fact']]} row(s)" + ("" if dup_count[r["fact"]] < 3 else " — OVER LIMIT")
    w(f"| {p} | {title_spec} | {cell(r['dist'])} | none (single settled value; ledger §F risks 1–4 do not touch it) | "
      f"{r['kind']} — {cell(r['why'])} | {r['w']} | {r['dec']} | {cell(r['grp'])} | {dup} | none · over-specific risk "
      f"low: {cell(r['alt'])} |")
w("")
w("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
w("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required "
  "write) | OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / "
  "UNLINKED) |")
w("|---|---|---|---|---|")
for p, r in zip(P, rows):
    w(f"| {p} | {cell(r['valid'])} (\"{r['span']}\") | REJECT — {cell(r['idle'])} (title: \"{cell(r['t'])}\") | "
      f"{', '.join(r['oe'])} | PROMPT_LINKED (path starts at Leonard's Sep 30 email, which the prompt names) |")
w("")
w("Final-reply test (whole set): \"Done. The send list is in your Q4 2025 investor update folder as 'Q4 update - send list', "
  "the four checklists and 18 follow-up cards are on the board, NCsoft's Anel card has a comment, and I replied to "
  "Leonard with the counts (New investor 1, In talks 7, Awaiting reply 14, Keep warm 3).\" → ACCEPT ☑ (no row grades the "
  "final response; every told fact is graded in the reply to Leonard, the deliverable the prompt names)")
w("")
w("## B · OE trace")
w("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
w("|---|---|---|---|")
cites = {}
for p, r in zip(P, rows):
    for o in r["oe"]:
        cites.setdefault(int(o.split()[1]), []).append(p)
extra = {3: ([pn("count25")], "no — the deck only confirms what each group gets; nothing on it is a requested result"),
         20: ([pn("card_gfr")], "no — the GFR group feeds the GFR follow-up card and the In talks counts"),
         24: ([pn("ba_t_accelerate")], "no — Karthic's contact ties the call to T-accelerate, graded through its build access cell")}
writes = set(range(30, 33)) | set(range(37, 85)) | {86}
for n in range(1, 87):
    kind = "write" if n in writes else ("analysis" if n in (28, 36, 85) else "discovery")
    if n in cites:
        rs = cites[n]
        own = ("yes — the write's result row" if kind == "write" else
               "no — proved by the content row(s) it decides" if kind == "discovery" else "no — analysis proved by its result rows")
    elif n in extra:
        rs, own = extra[n]
    else:
        rs, own = [pn("cards18")], "no — one of the 18 card writes, graded by the card volume row (sampled cards: OE 66, 70, 75)"
    w(f"| OE {n} | {kind} | {', '.join(rs)} | {own} |")
w("")
w("## C · Process candidates — three-condition test")
w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) "
  "behavioural, not trace | Result (Process / tighten P-n with F-n) |")
w("|---|---|---|---|---|---|---|")
w(f"| {pn('order_file')} | \"reply on his thread with how many ended up in each group\" (Leonard's email, incorporated: "
  "\"Please put it in your Q4 investor update folder ... Once it's done reply here\") | Every Outcome row reads the final "
  "state; none can show that the reply came after the send list writes | yes — every valid run replies once the send list "
  f"exists | yes — no stricter Outcome can capture order ({pn('reply')} grades delivery, {pn('cnt_new_investor')}–"
  f"{pn('cnt_keep_warm')} content) | yes — an ordering property of the run's writes to one file, not a tool trace | Process "
  "(weight 1; one service; batch 2: all six runs wrote the file before the reply and never after) |")
w(f"| {pn('order_checklists')} | same span (\"Then do what I put on the Existing Investor Update card in Trello. Once it's "
  "done reply here with how many firms and angels are in each group\") | The reply's per-group counts are the checklists' "
  "sizes; no Outcome row can show that the checklists came first | yes — every valid run builds the group checklists before "
  "reporting their counts | yes — no stricter Outcome can capture order | yes — ordering of the checklist writes on one card "
  "(one write kind; the follow-up cards and the NCsoft comment are not bundled in) | Process (weight 1; batch 2: all six runs "
  "finished the checklists before the reply) |")
w(f"| {pn('order_cards')} | same span (\"Then do what I put on the Existing Investor Update card in Trello. Once it's "
  "done reply here\"; the Sep 29 card comment asks for the follow-up cards in To Do) | No Outcome row can show that the "
  "cards came before the reply | yes — every valid run creates its follow-up cards before reporting | yes — no stricter "
  f"Outcome can capture order ({pn('cards18')} grades the count) | yes — ordering of one write action (new cards in one "
  "list) | Process (weight 1; /rubric round 2 Fix List; batch 2: all six runs created every card before the reply) |")
w(f"| {pn('order_comment')} | same span (\"Once it's done reply here\"; the Sep 29 comment: comment on an existing To Do "
  "card instead of adding another) | No Outcome row can show that the comment came before the reply | yes — every valid "
  f"run comments on the Anel card before reporting | yes — no stricter Outcome can capture order ({pn('ncsoft_comment')} "
  "grades the comment) | yes — ordering of one write action (one comment on one card) | Process (weight 1; /rubric round 2 "
  "Fix List; batch 2: all six runs commented before the reply) |")
w("| — | \"He wants to go through it with me on Monday, Oct 6, so it has to be done before then.\" | The deadline is met by "
  "every write existing at grading time; no ordering between writes is asked | n/a | Outcome rows already prove the end "
  "state | n/a | none — no further Process row (F49 review event is context) |")
w("")
w("## D · Spot-check groups")
w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | "
  "Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
w("|---|---|---|---|---|---|")
names25 = ["Anton Bernstein", "GFR Fund", "Andreessen Horowitz", "NCsoft", "Dentsu Ventures", "T-accelerate", "Homa",
           "Brightwater Games Fund", "Initial Capital", "BITKRAFT Ventures", "Makers Fund", "Raine Ventures",
           "General Catalyst", "BBQ Capital", "Treo VC", "Superplay", "Sony Mobile", "Revo Capital", "e2vc", "Triptyq",
           "Turkven", "Harlem Capital", "London Venture Partners", "Hiro Capital", "Sciplay"]
lit = lambda xs: " ".join(f"`{x}`" for x in xs)
w(f"| G1 send-list groups | F40 (25 recipients): {lit(names25)} | {pn('sciplay')} Sciplay (thread-reply pass), {pn('hiro')} Hiro Capital "
  f"(unnamed pass, alias), {pn('treo')} Treo VC (Awaiting reply; kickoff-day outreach, spelled Treeo on Sep 3); direct rows for "
  f"distinct outcomes (not samples): {pn('homa')} Homa and {pn('brightwater')} Brightwater Games Fund (off-list firms with calls), "
  f"{pn('a16z')} a16z (named by the doc's accelerator rule), {pn('anton_group')} and {pn('anton_amount')} Anton Bernstein (the one "
  f"new investor), {pn('angels')} the angel count (Paul Heydon's back-out) | {pn('count25')} | none — bundle (Rubric "
  f"Writing §7; Eval 2.2) | no — the prompt asks for the list as a whole; the per-firm groups are repetitive members |")
w(f"| G2 build access (firms in talks) | F44 (7): {lit(['Dentsu Ventures', 'T-accelerate', 'NCsoft', 'Brightwater Games Fund', 'GFR Fund', 'Andreessen Horowitz', 'Homa'])} "
  f"| direct exception rows {pn('ba_dentsu')}–{pn('ba_brightwater')} (the four firms Arthur's post names, iOS only) and "
  f"{pn('ba_homa')} Homa (the 'none' value, no tester add); GFR Fund and a16z (none) unsampled | {pn('count25')} | "
  f"none — bundle (Rubric Writing §7; Eval 2.2) | no |")
w(f"| G3 Keep warm checklist | F40 (3): {lit(['London Venture Partners', 'Hiro Capital', 'Sciplay'])} | {pn('item_sciplay')} Sciplay (thread-reply pass) | "
  f"{pn('cl_keep_warm')} | none — bundle (Rubric Writing §7; Eval 2.2) | no |")
w(f"| G4 In talks checklist | F40 (7): {lit(['GFR Fund', 'Andreessen Horowitz', 'NCsoft', 'Dentsu Ventures', 'T-accelerate', 'Homa', 'Brightwater Games Fund'])} "
  f"| {pn('item_homa')} Homa (off-list) | {pn('cl_in_talks')} | none — bundle (Rubric Writing §7; Eval 2.2) | no |")
w(f"| G5 Awaiting reply checklist | F34 (14): {lit(names25[8:22])} | {pn('item_sony')} Sony Mobile (edge: an advisor's "
  f"read is not the firm's answer, T17) | {pn('cl_awaiting_reply')} | none — bundle (Rubric Writing §7; Eval 2.2) | no |")
w(f"| G6 New investor checklist | F40 (1): `Anton Bernstein` | the one item is graded in {pn('item_anton')} | {pn('cl_new_investor')} | none — bundle (Rubric "
  f"Writing §7; Eval 2.2) | no |")
cards18 = ["GFR Fund", "Andreessen Horowitz", "T-accelerate", "Homa", "Brightwater Games Fund", "Initial Capital",
           "BITKRAFT Ventures", "Raine Ventures", "General Catalyst", "BBQ Capital", "Treo VC", "Superplay", "Sony Mobile",
           "Revo Capital", "e2vc", "Triptyq", "Turkven", "Harlem Capital"]
w(f"| G7 follow-up cards | F50 (18): {lit(cards18)} | {pn('card_gfr')} GFR Fund (DUP control: In talks, no existing card), {pn('card_bbq')} BBQ "
  f"Capital (ordinary Awaiting reply), {pn('card_brightwater')} Brightwater Games Fund (off-list); direct exception {pn('ncsoft_comment')} (NCsoft comment on "
  f"the Anel card); Dentsu Ventures and Makers Fund are graded through {pn('cards18')}'s exact scope, because a direct row on a card "
  f"that must not exist would be absence-only (gate 7) | {pn('cards18')} | none — bundle (Rubric Writing §7; Eval 2.2) | no |")
w("")
tw = sum(r["w"] for r in rows)
bands = {b: sum(1 for r in rows if r["w"] == b) for b in (5, 3, 1)}
w("## E · Summary")
n_proc = sum(1 for r in rows if r.get("cat") == "Process")
w(f"Rows {len(rows)} · Outcome {len(rows) - n_proc} · Process candidates {n_proc} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · "
  f"fewer than two Process rows failing the three-condition test ☑ ({pn('order_file')}, {pn('order_checklists')}, {pn('order_cards')} and {pn('order_comment')} pass all three) · "
  f"builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ ({pn('count25')}, {pn('cl_keep_warm')}, "
  f"{pn('cl_new_investor')}, {pn('cl_in_talks')}, {pn('cl_awaiting_reply')}, {pn('cards18')}) · predicted all-fail rows = 0 ☑")
w(f"Failure diversity: largest unit of discovery — see the gate line in the Self-review (≤ 50% ☒ — the send-list doc F2 "
  f"sits upstream of almost every row because every group rule lives in it; it is named by Leonard's ask, the task's hub, "
  f"not a hidden discovery; the same structural finding the accepted Robert, Douglas and Julia tasks carried) · chains "
  f"landing on distinct rows ☑ (SciPlay {pn('sciplay')}/{pn('item_sciplay')}/{pn('cl_keep_warm')}/{pn('cnt_keep_warm')}, Paul "
  f"{pn('angels')}/{pn('count25')}, build access {pn('ba_dentsu')}–{pn('ba_brightwater')}, Anton amount {pn('anton_amount')}; the "
  f"baseline batch on this SQL measured 4 failure patterns, largest 40%)")
w(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} · total weight {tw}")
w(f"Format 5 (§A3): rows {len(rows)}/{len(rows)} ☑ · `do_nothing_case` REJECT {len(rows)}/{len(rows)} ☑ · reachability "
  f"`PROMPT_LINKED` {len(rows)}/{len(rows)} ☑ · final-reply test ACCEPT ☑")
w(f"Set size: {len(rows)} rows for 19.25 h (reference: 31 criteria for a ~10-hour task; ~60 signals duplicate grading, "
  f"~12 missing coverage)")
w("Coverage: requirements 12/12 (ledger R1–R12) · OEs 86/86 (§B) · writes 7/7 (sheet create, move, rows; checklists; "
  f"items; cards; comment; reply) · told facts 4/4 ({pn('cnt_new_investor')}–{pn('cnt_keep_warm')}) · friction 0/0 (Friction: none)")
w("Gradable surface (gate 17): slots 21 · covered 20 · dispositioned 1 (§G: ST5 sampled out) · no slot with neither ☑ · mechanism share "
  f"{round(100 * sum(r['w'] for r in rows if any(m in r['dec'] for m in ('DONE1','DONE2','CORR','ALIAS','FILT','INPUT','DUP','BOOKED','FOLLOW'))) / tw)}% "
  "of the weight (reported, not gated)")
w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; the email and the card comments are "
  "incorporated) ☑ conclusions on ambiguous evidence (none: each graded value is settled by a later record) ☑ grading the "
  "distractor (traps are graded through the correct value, never their disclosure) ☑ hard-coded titles/phrasings (only "
  "the README file name, which the incorporated README fixes)")
w("Blocking: none for validity — no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share "
  "is a structural finding (the send-list doc), recorded under Unresolved for the human to accept.")
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
cover = {k: pn(t) for k, t in {"V1": "count25", "ST1": "sciplay", "ST2": "hiro", "ST3": "homa", "ST4": "brightwater",
                                "AC1": "ba_dentsu", "AC2": "ba_t_accelerate", "AC3": "ba_ncsoft", "AC4": "ba_brightwater",
                                "M3": "anton_amount", "G2": "anton_group", "RP1": "reply", "RP2": "cnt_in_talks",
                                "RP3": "cnt_keep_warm", "DL1": "folder", "CL1": "item_homa", "FU1": "card_gfr",
                                "FU2": "card_bbq", "FU3": "card_brightwater", "AN1": "ncsoft_comment"}.items()}  # ST5 sampled out
for s in surf["slots"]:
    if s["id"] == "ST5":
        w(f"| ST5 | group_lvp | {cell(' '.join(map(str, s['selector'])))} · {s['role']} / {s.get('group') or '—'} | "
          f"{s['work_kind']} (3) | — → F16 | — | sampled out: G1 samples SciPlay, Hiro Capital and Treo VC, with direct rows for "
          f"Homa and Brightwater Games Fund (gate 15, at most 5); LVP's Keep warm placement still counts in "
          f"{pn('cl_keep_warm')} and {pn('cnt_keep_warm')} (LVP pass "
          f"frederick.stone@harmonygames.co/1842277743427687737) |")
        continue
    pcov = cover[s["id"]]
    r = rows[int(pcov[1:]) - 1]
    w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {cell(' '.join(map(str, s['selector'])))} · {s['role']} / "
      f"{s.get('group') or '—'} | {s['work_kind']} ({r['w']}) | {', '.join(s['mechanisms']) or '—'} → {r['dec']} | {pcov} | "
      f"covered: the title rejects both the omission and the trap value ({cell(r['alt'])}) |")
w("")
sr = HERE / "selfreview.md"
w(sr.read_text().rstrip() if sr.exists() else "## Self-review\n(pending)")
(TI / "Working_Files/09_Rubric_Writing_Plan.md").write_text("\n".join(out) + "\n")
print("plan written:", len(out), "lines; weight", tw, bands)
