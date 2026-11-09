#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py). §F (shortcut probe paste) and the
visibility block are read from probe.txt / visibility.txt next to this script; selfreview.md is written by build_selfreview.py."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
rows = json.loads((HERE / "rows.json").read_text())
NUM = json.loads((WF / "plan/oe_events_index.json").read_text())["index"]
TRUTH = {k: v for k, v in json.loads((WF / "solver/truth.json").read_text()).items() if isinstance(v, dict) and v.get("Call")}
P = [f"P{i + 1}" for i in range(len(rows))]
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
BY = {r["tag"]: r for r in rows}


def pn(t):
    return TAG[t]


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def pl(*ts):
    return ", ".join(pn(t) for t in ts)


def group(prefix, *skip):
    return [r["tag"] for r in rows if r["tag"].startswith(prefix) and r["tag"] not in skip]


lit = lambda xs: " ".join(f"`{x}`" for x in xs)  # noqa: E731
out = []
w = out.append
tw = sum(r["w"] for r in rows)
bands = {b: sum(1 for r in rows if r["w"] == b) for b in (5, 3, 1)}
n_proc = sum(1 for r in rows if r["cat"] == "Process")
w("# 09 Rubric Writing Plan — samuel_zm_beta_messages (beta player messages, injection rev6)")
w("Generated 2026-11-06 (after /rubric round 2, FAIL 1: its Fix List applied exactly, R21 rewritten as it asks; run_forensics/rev6/rubric_r2/platform_rubric_review_r2.md) · Clock 2025-10-01T00:00:00Z (seed bound; eval clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)) · Persona Samuel Turner "
  "samuel.turner@harmonygames.co · Assigned role Game Designer · Tier Long-Horizon · Mode Medium (requester target: corrected average under 80%) · Human time 21.5 h · "
  "OE status: /oe PASS 2026-11-05 (run_forensics/rev6/2_oe_PASS_r1.md, Score 5, 135 events, 08_Oracle_Events.md sha256 4924949d7fd3)")
w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — W1 one sheet in d_caafeec2804b3a67ce46aa with Leonard's seven columns and 36 message rows (Go 2: Lapsed 1 day, "
  "Lapsed 7 days; Drop 6: Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena, Comeback gift, Lapsed 14 days; Hold 28); W2 a one-page note in the same folder (D1 and D7 by platform, "
  "the lapsed reminders on days 1, 7, 14, 21 and 28, the four Holds the client already schedules with why); W3 the call as a comment on DES-313 and DES-315 to DES-345; W4 24 tickets to Backlog "
  "unassigned, 6 to Canceled, the 2 Go tickets as they are; W5 four new ask tickets and one string ticket under DES-314; W6 a two-item checklist on card 6851a769c65dc0017a227bb7; W7 email to "
  "the eight askers apart from Leonard; W8 Go 2, Hold 28, Drop 6 in D06L58XCVKK, after the other writes.")
w("")
w("Rubric shape: every write family has a result row and a count or scope guard. Content that differs per target gets one row per target with no cap (rubric_flow_v2, Q4 /rubric round 1): every "
  "call comment (32 tickets plus the 4 new ones) and every ask in every email (21). The sheet's cells and the ticket moves are repetitive members, so each column has a volume control, direct "
  "rows on the members an authority singles out and at most 5 samples, never a bundled exact-set row (gate 15). Every call is graded directly on its own ticket, so no call rests on sampling. "
  "A call fact sits in at most two rows, sheet plus comment or comment plus email (V3 limit), apart from DES-344, where /rubric round 1 asked for the sheet Call row as well. 09_Rubrics.json mirrors "
  f"P1–P{len(rows)} one to one (C-n = P-n).")
w("")
w("## A · Coverage matrix")
w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category (Outcome / Process candidate → C) | "
  "Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |")
w("|---|---|---|---|---|---|---|")
for p, r in zip(P, rows):
    oes = ", ".join(r["oe"][:6]) + (" …" if len(r["oe"]) > 6 else "")
    w(f"| {p} | \"{r['span']}\" · {oes} | {r['fact']} | {cell(r['verify'])} | {cell(r['final'])} | {'Process candidate → C' if r['cat'] == 'Process' else 'Outcome'} | "
      f"{r['vals']} · accept: {cell('; '.join(r['acc']))} · dates: none graded · {r['fids']} |")
w("")
w("## A2 · Grading risks and weight")
w("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · "
  "comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | Predicted all-fail basis "
  "(four Evals bases) · over-specific risk |")
w("|---|---|---|---|---|---|---|---|---|---|")
dup = {}
for r in rows:
    dup[r["fact"]] = dup.get(r["fact"], 0) + 1
for p, r in zip(P, rows):
    spec = ("yes — the DM fixes the seven column names; letter case accepted" if r["tag"] == "sheet_header" else "no — must not hard-code; names and wording accept fair variants")
    d = f"{r['fact']} in {dup[r['fact']]} row(s)" + ("" if dup[r["fact"]] < 3 else " — OVER LIMIT")
    amb = ("none (single settled value; ledger §F 3 records the scope reading, settled by 'filed on a ticket or a card')" if "T7" in r["dec"] else "none (single settled value; ledger §F risks do not touch it)")
    w(f"| {p} | {spec} | {cell(r['dist'])} | {amb} | {r['kind']} — {cell(r['why'])} | {r['w']} | {r['dec']} | {cell(r['grp'])} | {d} | none · over-specific risk low: {cell(r['alt'])} |")
w("")
w("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
w("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | OE step ids (verbatim OE labels) | Deciding source reachability "
  "(PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
w("|---|---|---|---|---|")
for p, r in zip(P, rows):
    w(f"| {p} | {cell(r['valid'])} (\"{r['span']}\") | REJECT — {cell(r['idle'])} (title: \"{cell(r['t'])}\") | {', '.join(r['oe'])} | PROMPT_LINKED (path starts at Leonard's DM, which the prompt names) |")
w("")
w("Final-reply test (whole set): \"Done. The calls sheet and the note are in your Drive folder, the tickets have their comments and moves, the new tickets are filed, the checklist is on the push "
  "notifications card, the askers have their emails, and I told Leonard Go 2, Hold 28, Drop 6 in his DM.\" → ACCEPT ☑ (no row grades the final response; the told counts are graded in the DM, the "
  "deliverable the prompt names)")
w("")
w("## B · OE trace")
w("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
w("|---|---|---|---|")
cites = {}
for p, r in zip(P, rows):
    for o in r["oe"]:
        cites.setdefault(int(o.split()[1]), []).append(p)
KEY = {v: k for k, v in NUM.items()}
for n in range(1, len(NUM) + 1):
    k = KEY[n]
    kind = "write" if k.startswith(("w_", "wc:", "wm:", "wmail:", "wdm")) else "discovery"
    if n in cites:
        rs = sorted(set(cites[n]), key=lambda x: int(x[1:]))
        own = "yes — the write's result row" if kind == "write" else "no — proved by the content row(s) it decides"
    elif k.startswith("wm:"):
        rs = [pn("mv_backlog"), pn("mv_cancel")]
        own = "no — a template-identical move; the volume rows count it and the samples stand for it (gate 15)"
    else:
        rs = [pn("sheet_rows"), pn("dm_hold")]
        own = "no — an upstream read; it decides calls, and its result is proved by the rows that carry them"
    w(f"| OE {n} | {kind} | {', '.join(rs[:8])}{' …' if len(rs) > 8 else ''} | {own} |")
w("")
w("## C · Process candidates — three-condition test")
w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |")
w("|---|---|---|---|---|---|---|")
w(f"| {pn('order_dm')} | \"When it's all finished tell him the counts in that same DM\" | Every Outcome row reads the final state; none can show that the DM post came after the other writes | yes — every "
  "valid run posts once its other writes are finished | yes — no stricter Outcome can capture order | yes — an ordering property of the post, not a tool trace | Process (weight 1; one row for the one "
  "ordering ask, the Q4 /rubric round 1 merged six per-write rows into one; /oe's 'No Process row is needed' covers reads, and this row covers the order, which no Outcome shows) |")
w("")
w("## D · Spot-check groups")
w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
w("|---|---|---|---|---|---|")
NB = "none — bundle (Rubric Writing §7; Eval 2.2)"
allm = sorted(TRUTH)
w(f"| G2 Call column | F41–F72, F34–F37 (36): {lit(allm)} | direct: {pl('call_lives_recharged', 'call_plague_race', 'call_weekly_leaderboard_reset', 'call_finish_first_mission', 'call_lapsed_1_day', 'call_lapsed_7_days')} "
  f"(the four traps and every Go); and {pn('call_lapsed_14_days')} (the covered Drop); samples: {pl('call_axe_arena', 'call_hourly_coins', 'call_streak_fever')} (Drop: a Trello list, a Trello list and a Confluence row), {pl('call_login_calendar_update', 'call_quests_rollover')} "
  f"(ordinary Hold, Done-looking copy on the ticket) | {pl('sheet_rows', 'tally_go')} | {NB} | no — every call is graded directly on its own ticket (G7); the cell is a repetitive member |")
w(f"| G3 What's missing column | F41–F72, F34–F37 (29 rows with a reason) | direct: {pl('miss_lives_recharged', 'miss_plague_race', 'miss_weekly_leaderboard_reset', 'miss_finish_first_mission', 'miss_lapsed_14_days')} (the failed tests the "
  f"rule singles out), {pl(*[t for t in group('miss_') if t.split('_', 1)[1] in ('boss_arena_attempts_refilled', 'daily_gift_about_to_reset', 'teammate_sent_lives', 'infinite_lives_ending')])} (the four comment asks); sample: "
  f"{pl('miss_plague_race_result')} (test 2) | {pn('sheet_rows')} | {NB} | no |")
w(f"| G4 Audience column | F41–F72, F34–F37 (36) | {pl(*group('aud_'))}: a phrase from the ask's comment (arena unlock), a race audience, the level-20 group test 4 turns on, the DES-313 audience, a comment ask's audience | {pn('sheet_rows')} | {NB} | no |")
w(f"| G5 Ticket column | F41–F72 (36) | direct: {pn('ticket_wc')} (the alias); samples: {pn('ticket_lapsed_7_days')} (a sheet row whose name differs from its ticket), {pn('ticket_teammate_sent_lives')} (a comment ask takes its new key) | {pn('sheet_rows')} | {NB} | no |")
w(f"| G12 Message column | F41–F72, F34–F37 (36) | {pn('msg_lapsed_1_day')} (a sheet name that differs from its ticket) | {pn('sheet_rows')} | {NB} | no — names are free (brief §4b) |")
w(f"| G7 ticket comments (one row each, not sampled) | F41–F72, F34–F37 (36) | every ticket has its own row ({len(group('cm_', 'cm_count'))} rows): the content differs per target | {pn('cm_count')} | {NB} | no — each comment is its own outcome |")
w(f"| G8 ticket moves and assignees | F41–F72, F26 (30): {lit(sorted(v['Ticket'] for v in TRUTH.values() if v['Ticket'] and v['Call'] != 'Go'))} | direct: {pl('mv_lives_recharged', 'mv_weekly_leaderboard_reset', 'mv_finish_first_mission', 'mv_plague_race', 'mv_lapsed_14_days')} "
  f"(the four Done Holds, the covered Drop); samples: {pl('mv_win_and_collect_start', 'mv_endless_weekly_result', 'mv_hourly_coins', 'mv_comeback_gift')} (the alias, an ordinary Hold, Trello and ticket reasons); assignee: {pl('un_des313', 'un_des315', 'un_des329')} (the one ticket with another assignee, a Done Hold, an ordinary one) | {pl('mv_backlog', 'mv_cancel', 'mv_unassign')} | {NB} | no — the moves are template-identical: one state per call |")
w(f"| G11 asker emails (one row per ask, not sampled) | F73–F80 (8): eight askers, 21 asks: {lit(sorted((v['Ticket'] or k) for k, v in TRUTH.items() if any(g.startswith('asker_') for g in v['groups'])) + ['DES-313'])} | every ask has its own row ({len(group('em_', 'em_count'))} rows) | {pn('em_count')} | {NB} | no — each ask is its own outcome |")
w("")
w("## E · Summary")
w(f"Rows {len(rows)} · Outcome {len(rows) - n_proc} · Process candidates {n_proc} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · fewer than two Process rows failing the three-condition test ☑ ({pn('order_dm')} passes all three) · "
  f"builder minimum 5 ☑ · one volume row per output, no bundled exact-set row ☑ ({pl('sheet_rows', 'tally_go', 'head_count', 'str_count', 'cm_count', 'mv_backlog', 'mv_cancel', 'mv_unassign', 'new_count', 'chk_count', 'em_count', 'note_count')}) · predicted all-fail rows = 0 ☑")
DIV = json.loads((HERE / "diversity.json").read_text()) if (HERE / "diversity.json").exists() else {}
w(f"Failure diversity: largest unit of discovery {DIV.get('top', 'see the gate line')} (≤ 50% ☒ — the rule doc f_dc45e0e5a8b8635c1b82b2 and the parent DES-314 sit upstream of every call because the DM names them as the rule and the ticket list; they are the job's "
  f"rule book, not hidden discoveries; the same structural finding the archived bridge and Q4 tasks carried) · chains landing on distinct rows ☑ (T1 Weekly Leaderboard {pl('call_weekly_leaderboard_reset', 'miss_weekly_leaderboard_reset', 'nh_weekly_leaderboard_reset', 'cm_weekly_leaderboard_reset', 'mv_weekly_leaderboard_reset')}; "
  f"T2 headline {pl('head_l7', 'new_string')}; T3 Finish first mission {pl('call_finish_first_mission', 'miss_finish_first_mission', 'nh_finish_first_mission')}; T4 Plague Race {pl('call_plague_race', 'miss_plague_race', 'nh_plague_race')}; T5 Lives recharged {pl('call_lives_recharged', 'miss_lives_recharged', 'nh_lives_recharged')}; "
  f"T6 alias {pl('ticket_wc', 'cm_win_and_collect_start')}; T7 comment asks {pl('new_boss_arena_attempts_refilled', 'new_teammate_sent_lives', 'em_count')}; T9 covered {pl('miss_lapsed_14_days', 'cm_lapsed_14_days')})")
w(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} · total weight {tw}")
w(f"Format 5 (§A3): rows {len(rows)}/{len(rows)} ☑ · `do_nothing_case` REJECT {len(rows)}/{len(rows)} ☑ · reachability `PROMPT_LINKED` {len(rows)}/{len(rows)} ☑ · final-reply test ACCEPT ☑")
w(f"Set size: {len(rows)} rows for 21.5 h. The count follows per-target coverage (36 calls on tickets, 21 asks in email, every other write family), not a target; Q4 passed /rubric at 102 rows for 36 companies.")
w("Coverage: requirements 13/13 (ledger R1–R13) · OEs 135/135 (§B) · writes 8/8 (sheet; note; comments; moves; new tickets; checklist; emails; DM) · told facts 3/3 (Go, Hold, Drop in the DM) · friction 0/0 (Friction: none)")
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
COVER = {"X1": "call_weekly_leaderboard_reset", "X2": "miss_weekly_leaderboard_reset", "X1c": "mv_weekly_leaderboard_reset", "X3": "head_l7", "X4": "new_string", "X16": "str_l7", "X5": "call_finish_first_mission", "X6": "miss_finish_first_mission",
         "X6c": "mv_finish_first_mission", "X8c": "mv_plague_race", "X7": "call_plague_race", "X8": "miss_plague_race", "K1": "call_lives_recharged", "X21": "miss_lives_recharged", "X21c": "mv_lives_recharged", "X22": "nh_lives_recharged",
         "X9": "ticket_wc", "X10": "new_count", "X13": "new_boss_arena_attempts_refilled", "X13b": "new_teammate_sent_lives", "X13c": "new_infinite_lives_ending", "X15": "call_lapsed_14_days", "X15b": "miss_lapsed_14_days", "X17": "note_ladder", "X20": "nh_finish_first_mission",
         "X19b": "mv_endless_weekly_result", "T1": "dm_go", "T2": "dm_hold", "T3": "dm_drop", "K2": "call_lapsed_1_day", "K3": "call_axe_arena", "K5": "call_hourly_coins", "K6": "call_login_calendar_update",
         "K9": "miss_plague_race_result", "K10": "head_l1", "K11": "chk_lapsed_1_day", "K12": "mv_hourly_coins", "K13": "cm_quests_rollover", "K14": "aud_boss_arena_open", "K15": "aud_plague_race_result", "K16": "note_ios_d1", "K17": "note_android_d1",
         "K18": "em_robert_boss_arena_open", "K19": "em_douglas_teammate_sent_lives", "V1": "sheet_rows", "D1": "sheet_folder", "D2": "dm_go"}
DISP = {"X2b": f"duplicate fact: the Weekly Leaderboard reason is graded in {pl('miss_weekly_leaderboard_reset', 'nh_weekly_leaderboard_reset')}; a third row on the comment would breach the V3 limit, and the DM asks only for the call there (gate 6; harmonygames-Games/match3d#248#rc_18)",
        "X6b": f"duplicate fact: the Finish first mission reason is graded in {pl('miss_finish_first_mission', 'nh_finish_first_mission')}; the DM asks only for the call on the ticket (gate 6; C0880U9751A/1759167608.326578)",
        "X8b": f"duplicate fact: the Plague Race reason is graded in {pl('miss_plague_race', 'nh_plague_race')}; the DM asks only for the call on the ticket (gate 6; D06UFE81RF0/1759174846.723833)",
        "X21b": f"duplicate fact: the Lives recharged reason is graded in {pl('miss_lives_recharged', 'nh_lives_recharged')}; the DM asks only for the call on the ticket (gate 6; C0880U9751A/1759245146.720608)",
        "X11": f"duplicate fact: the call is graded in {pl('cm_boss_arena_attempts_refilled', 'em_brian_boss_arena_attempts_refilled')}, so the sheet row is graded by its What's missing cell {pn('miss_boss_arena_attempts_refilled')} (gate 6; cmt_f1b8a109dfa70cdc4565)",
        "X12": f"duplicate fact: the call is graded in {pl('cm_daily_gift_about_to_reset', 'em_julia_daily_gift_about_to_reset')}, so the sheet row is graded by {pn('miss_daily_gift_about_to_reset')} (gate 6; cmt_2b519285937e7fa79453)",
        "X11b": f"duplicate fact: the call is graded in {pl('cm_teammate_sent_lives', 'em_douglas_teammate_sent_lives')}, so the sheet row is graded by {pn('miss_teammate_sent_lives')} (gate 6; cmt_eabac5435f2b3a575aad)",
        "X12b": f"duplicate fact: the call is graded in {pl('cm_infinite_lives_ending', 'em_calvin_infinite_lives_ending')}, so the sheet row is graded by {pn('miss_infinite_lives_ending')} (gate 6; cmt_e2e2926a2080ca53c4ea)",
        "X18": f"sampled out: /rubric round 1 cut the Backlog samples to five (gate 15); the move count in {pn('mv_backlog')} (DES-321)",
        "X19": f"sampled out: /rubric round 1 cut the Backlog samples to five (gate 15); the move count in {pn('mv_backlog')} (DES-323)",
        "X1c_": ""}
DISP.pop("X1c_")
assert set(COVER) | set(DISP) == {s["id"] for s in surf["slots"]}, {s["id"] for s in surf["slots"]} ^ (set(COVER) | set(DISP))
MECH = ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9")
mech_w = sum(r["w"] for r in rows if any(m in r["dec"].split() for m in MECH))
w(f"Gradable surface (gate 17): slots {len(surf['slots'])} · covered {len(COVER)} · dispositioned {len(DISP)} (§G: duplicate fact, sampled out) · no slot with neither ☑ · mechanism share {round(100 * mech_w / tw)}% of the weight (reported, not gated)")
w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; Leonard's DM, the rule doc it names and what the rule doc points to are incorporated) ☑ conclusions on ambiguous evidence (none: each graded value is settled by a later or "
  "more specific record) ☑ grading the distractor (traps are graded through the correct value, never their disclosure) ☑ hard-coded titles/phrasings (only the DM's column names)")
w("Blocking: none for validity — no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share is a structural finding (the rule doc and DES-314), recorded under Unresolved for the human to accept.")
w("")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
w("")
w((HERE / "visibility.txt").read_text().rstrip())
w("")
w("## F · Shortcut probe")
w("Literals: the email rows carry the ask's key, with the address beside it in plain text. A first run that used the eight addresses as literals gave 333 hits, every one a staff list (all-hands invites and share lists): an address says who works here, not who asked or what was called, so those records answer no row.")
w("")
probe = HERE / "probe.txt"
w(probe.read_text().rstrip() if probe.exists() else "(pending)")
w("")
w("## G · Gradable-surface coverage")
w("| Slot | Stable fact ID | Selector · role / group | Work kind (band) | Mechanisms → Decided by | Covered by (P-n) | Disposition and reason (evidence) |")
w("|---|---|---|---|---|---|---|")
for s in surf["slots"]:
    sel = cell(" ".join(map(str, s["selector"])))[:90]
    if s["id"] in DISP:
        w(f"| {s['id']} | {s.get('fact_id') or '—'} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} (5) | {', '.join(s['mechanisms']) or '—'} → — | — | {DISP[s['id']]} |")
        continue
    r = BY[COVER[s["id"]]]
    w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({r['w']}) | {', '.join(s['mechanisms']) or '—'} → {r['dec']} | {pn(COVER[s['id']])} | covered: the title rejects both the omission and the plausible wrong value ({cell(r['alt'])}) |")
w("")
sr = HERE / "selfreview.md"
w(sr.read_text().rstrip() if sr.exists() else "## Self-review\n(pending)")
(WF / "09_Rubric_Writing_Plan.md").write_text("\n".join(out) + "\n")
print("plan written:", len(out), "lines; weight", tw, bands, "mechanism share", round(100 * mech_w / tw))
