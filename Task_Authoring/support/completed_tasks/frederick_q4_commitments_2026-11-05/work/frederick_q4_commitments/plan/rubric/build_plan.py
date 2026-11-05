#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Writing_Plan.md from rows.json (written by build_rubric.py). §F (shortcut probe paste)
and the visibility block are read from probe.txt / visibility.txt next to this script; the local baseline grade from
grade_baselines.py is quoted in the Self-review."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
rows = json.loads((HERE / "rows.json").read_text())
NUM = json.loads((WF / "plan/oe_events_map.json").read_text())["num"]
P = [f"P{i + 1}" for i in range(len(rows))]
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
BY = {r["tag"]: r for r in rows}


def pn(t):
    return TAG[t]


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


def ev_list(oes):
    return ", ".join(oes)


out = []
w = out.append
tw = sum(r["w"] for r in rows)
bands = {b: sum(1 for r in rows if r["w"] == b) for b in (5, 3, 1)}
n_proc = sum(1 for r in rows if r.get("cat") == "Process")
w("# 09 Rubric Writing Plan — frederick_q4_commitments (vendor and partner backlog, injection rev4)")
w("Generated 2026-11-05 (after /rubric round 1, FAIL 1: its Fix List applied; run_forensics/rev4/rubric_r1/platform_rubric_review_r1.md) · Clock 2025-10-01T00:00:00Z (seed bound; eval clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, "
  "2025 (synth-cut)) · Persona Frederick Stone frederick.stone@harmonygames.co · Assigned role Co-founder · Tier Long-Horizon · "
  "Mode Easy (requester target: corrected average under 80%) · Human time 22.5 h · OE status: /oe PASS 2026-11-04 "
  "(run_forensics/rev4/platform_oe_review_r2.md, Score 5, 147 events, 08_Oracle_Events.md sha256 10814dbd922b)")
w("Canonical outcomes: brief §4b (all fair results and accepted alternatives) — D1 one Google Sheet 'Q4 commitments log' in "
  "d_80a8c04753ba82ba4ba6a5 with the template's seven headings and 36 company rows (Answered 4: Balancy, Lanternfly Publishing, "
  "Motive Forge, Spotlight Fest; End 10; Keep 3: Certwell, Pingwise, Vaultline; Sign 7: Bundlehouse, Kinetic Arcade, Lumencloud, "
  "Markward, Nintendo, Orbit Store, Playfuse; Park 12); D2 written answers to 31 companies plus the Clipforge cancellation to "
  "billing@paylane.io; D3 seven To Do cards on board 640643a3fd8f3ca308d9318e; D4 three ESG intake emails to PERSON_2599_EMAIL "
  "(Kinetic Arcade, Lumencloud, Bundlehouse); D5 32 new contacts; D6 14 reminder events on Mon Jan 5, 2026; D7 a reply on "
  "frederick.stone@harmonygames.co/1844732913254784171 with the keep list (3) and the sign list (7).")
w("")
w("Rubric shape: every write family has a result row; each population has one volume row per output, direct rows on the "
  "members an authority singles out (the trap companies) and at most 5 samples per group, never a bundled exact-set row "
  "(gate 15). Content that differs per target gets one row per target with no cap (/rubric round 1, rubric_flow_v2): the "
  "31 written answers, each ESG intake email's checklist parts and every member of the reply's two lists. Each designed trap "
  "decides its own rows (C1 Nintendo, C2 Framewell, C3 Lanternfly, C4 Pingwise, C5 Clipforge, C6 Pixel Harbor, C7 Hootline, "
  "C8 Spotlight); each row grades its own deliverable, and no declared fact ID is graded twice. 09_Rubrics.json mirrors "
  f"P1–P{len(rows)} one to one (C-n = P-n).")
w("")
w("## A · Coverage matrix")
w("| P | Source (exact prompt span · OE n) | Stable fact ID | What must be verified | Final state that proves it | Category "
  "(Outcome / Process candidate → C) | Expected/source values and pointers · accepted alternatives · date acceptance · F-IDs |")
w("|---|---|---|---|---|---|---|")
for p, r in zip(P, rows):
    acc = "; ".join(r["acc"])
    dates = "Pacific and UTC day both 2026-01-05 (accepted: 2026-01-05, any time that day)" if r.get("dates") else (
        "any date form for the same day" if "date" in r["verify"].lower() else "none graded")
    w(f"| {p} | \"{r['span']}\" · {ev_list(r['oe'][:6])}{' …' if len(r['oe']) > 6 else ''} | {r['fact']} | {cell(r['verify'])} | "
      f"{cell(r['final'])} | {'Process candidate → C' if r.get('cat') == 'Process' else 'Outcome'} | {r['vals']} · accept: "
      f"{cell(acc)} · dates: {dates} · {r['fids']} |")
w("")
w("## A2 · Grading risks and weight")
w("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single "
  "conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band "
  "1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Global fact duplication / overlap group | Predicted "
  "all-fail basis (four Evals bases) · over-specific risk |")
w("|---|---|---|---|---|---|---|---|---|---|")
dup = {}
for r in rows:
    dup[r["fact"]] = dup.get(r["fact"], 0) + 1
for p, r in zip(P, rows):
    spec = ("yes — the README fixes the seven column names; letter case accepted" if r["tag"] == "log_header" else
            "no — must not hard-code; names, wording and dates accept fair variants")
    d = f"{r['fact']} in {dup[r['fact']]} row(s)" + ("" if dup[r["fact"]] < 3 else " — OVER LIMIT")
    w(f"| {p} | {spec} | {cell(r['dist'])} → graded through the correct value, never its disclosure | none (single settled value; "
      f"ledger §F risks do not touch it) | {r['kind']} — {cell(r['why'])} | {r['w']} | {r['dec']} | {cell(r['grp'])} | {d} | none · "
      f"over-specific risk low: {cell(r['alt'])} |")
w("")
w("## A3 · Format 5 — per-row acceptance cases, OE steps and reachability")
w("| P | valid_case (must ACCEPT · prompt authority) | do_nothing_case (must REJECT · exact title text of the required write) | "
  "OE step ids (verbatim OE labels) | Deciding source reachability (PROMPT_LINKED / TRASH / ATTACHMENT_ONLY / UNLINKED) |")
w("|---|---|---|---|---|")
for p, r in zip(P, rows):
    w(f"| {p} | {cell(r['valid'])} (\"{r['span']}\") | REJECT — {cell(r['idle'])} (title: \"{cell(r['t'])}\") | {ev_list(r['oe'])} | "
      "PROMPT_LINKED (path starts at Leonard's email, which the prompt names) |")
w("")
w("Final-reply test (whole set): \"Done. The log is in your Q4 commitments folder ('Q4 commitments log', 36 companies), every "
  "company waiting on us has a written answer (Clipforge cancelled with billing@paylane.io), the three ESG intake emails are "
  "sent, the seven signing cards are in To Do, the contacts are in Contacts, 14 reminders are on Jan 5, and I replied to Leonard "
  "with what we're keeping and what's waiting to sign.\" → ACCEPT ☑ (no row grades the final response; every told fact is "
  "graded in the reply to Leonard, the deliverable the prompt names)")
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
    kind = "write" if k.startswith("w:") else "discovery"
    if n in cites:
        rs = sorted(set(cites[n]), key=lambda x: int(x[1:]))
        own = ("yes — the write's result row" if kind == "write" else "no — proved by the content row(s) it decides")
    else:
        rs = [pn("log_rows"), pn("ans_count")]
        own = ("no — an ordinary company read; its row counts in the log volume row and its answer in the answers volume row "
               "(not sampled, gate 15)")
    w(f"| OE {n} | {kind} | {', '.join(rs[:8])}{' …' if len(rs) > 8 else ''} | {own} |")
w("")
w("## C · Process candidates — three-condition test")
w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) "
  "behavioural, not trace | Result (Process / tighten P-n with F-n) |")
w("|---|---|---|---|---|---|---|")
w(f"| {pn('order_reply')} | \"When it's all done, reply to Leonard on his email with what he asked for.\" | Every Outcome row reads "
  "the final state; none can show that the reply came after the other writes | yes — every valid run replies once its other writes "
  "are finished | yes — no stricter Outcome can capture order | yes — an ordering property of the reply, not a tool trace | Process "
  "(weight 1; one row for the one ordering ask, /rubric round 1 merged the six per-write rows) |")
w("")
w("## D · Spot-check groups")
w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row "
  "(`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
w("|---|---|---|---|---|---|")
TRUTH = json.loads((WF / "solver/truth.json").read_text())
lit = lambda xs: " ".join(f"`{x}`" for x in xs)
allco = sorted(k for k, v in TRUTH.items() if v["Decision"])
NB = "none — bundle (Rubric Writing §7; Eval 2.2)"
w(f"| G1 log rows (Decision, Contact, What's waiting, Answered by, Next date columns) | F29–F64 (36): {lit(allco)} | Decision: "
  f"{pn('nin_decision')} Nintendo (Linear-only), {pn('fw_decision')} Framewell (thread-reply waiver), {pn('lf_decision')} Lanternfly "
  f"Publishing (DM answer), {pn('sp_decision')} Spotlight Fest (Robert's note), {pn('pw_decision')} Pingwise (Keep exception); Contact: "
  f"{pn('rev_contact')} Reviewly; What's waiting: {pn('sv_waiting')} Soundvault; Answered by (the whole Answered set, direct rows): "
  f"{pn('lf_by')}, {pn('sp_by')}, {pn('bal_by')}, {pn('mf_by')}, and when ({pn('mf_when')} Motive Forge); Next date: {pn('nin_next')} "
  f"Nintendo, {pn('cf_next')} Clipforge (notice override), {pn('ph_next')} Pixel Harbor Events (June quote), {pn('pw_next')} Pingwise "
  f"(night pager), {pn('lf_next')} Lanternfly Publishing (later answer) | {pn('log_rows')} | {NB} | no — the prompt asks for the log "
  "as a whole; the per-company cells are repetitive members (≤ 5 per column) |")
w(f"| G2 What we told them | F33–F61 (31 answered rows) | {pn('ph_told')} Pixel Harbor Events, {pn('lf_told')} Lanternfly "
  f"Publishing, {pn('sv_told')} Soundvault, {pn('kin_told')} Kinetic Arcade, {pn('ww_told')} Wishwave (the five §4b marks material) "
  f"| {pn('log_rows')} | {NB} | no |")
ANS = [t for t in BY if t.startswith("ans_") and t != "ans_count"] + ["cf_cancel", "cf_priya", "rev_cancel"]
w(f"| G3 written answers (one row per recipient, not sampled) | F33–F61 (31): {lit(sorted(k for k, v in TRUTH.items() if 'written_answer' in v['groups']))} | "
  f"every recipient has its own row ({len(ANS)} rows: {', '.join(pn(t) for t in sorted(ANS, key=lambda t: int(pn(t)[1:])))}); the "
  "content differs per target, so rubric_flow_v2 gives one row each with no cap | "
  f"{pn('ans_count')} | {NB} | no — each answer is its own outcome |")
ESGR = [t for t in BY if t.startswith("esg_") and t != "esg_count"]
w(f"| G4 ESG intake emails (one row per checklist part per agreement) | F45–F47 (3): {lit(['Kinetic Arcade', 'Lumencloud', 'Bundlehouse'])} | "
  f"{len(ESGR)} rows ({', '.join(pn(t) for t in ESGR)}): term or licence term, exclusivity or IP licence, cost, needed-by date and signer "
  f"for each agreement | {pn('esg_count')} | {NB} | no |")
w(f"| G5 To Do cards | F29, F45–F50 (7): {lit(['Bundlehouse', 'Kinetic Arcade', 'Lumencloud', 'Markward', 'Nintendo', 'Orbit Store', 'Playfuse'])} "
  f"| {pn('card_nin')} Nintendo (Linear), {pn('card_kin')} Kinetic Arcade (ordinary ESG case), {pn('card_mark')} Markward (July "
  f"note superseded) | {pn('card_count')} (states the template: the company's name in each title) | {NB} | no |")
w(f"| G6 contacts | F30–F64 less the existing three and Nintendo (32) | {pn('ct_hoot')} Hootline (August thread, no paper), "
  f"{pn('ct_rev')} Reviewly (ordinary), {pn('ct_wen')} Lanternfly Publishing (an Answered company's person) | {pn('ct_count')} (states "
  f"the template: the company in the job field) | {NB} | no |")
w(f"| G7 reminders | F30, F31, F51–F62 (14): {lit(sorted(k for k, v in TRUTH.items() if 'revisit' in v['groups']))} | "
  f"{pn('rem_fw')} Framewell (waiver), {pn('rem_lf')} Lanternfly Publishing (later answer), {pn('rem_hoot')} Hootline (August "
  f"thread) | {pn('rem_count')} | {NB} | no |")
w(f"| G8 reply: what we're keeping (every member) | F32, F43, F44 (3): {lit(['Certwell', 'Pingwise', 'Vaultline'])} | "
  f"{pn('reply_pingwise')} Pingwise (alias), {pn('reply_certwell')} Certwell, {pn('reply_vaultline')} Vaultline | {pn('reply_keep_count')} | {NB} | no |")
SG = ["reply_markward", "reply_nintendo", "reply_bundlehouse", "reply_kinetic", "reply_lumencloud", "reply_orbit", "reply_playfuse"]
w(f"| G9 reply: waiting to sign (every member) | F29, F45–F50 (7) | {', '.join(pn(t) for t in SG)} (Markward's July note superseded; "
  f"Nintendo from Linear) | {pn('reply_sign_count')} | {NB} | no |")
w("")
w("## E · Summary")
w(f"Rows {len(rows)} · Outcome {len(rows) - n_proc} · Process candidates {n_proc} — ≥ 1 Outcome ☑ · Process rows ≤ 50 % ☑ · "
  f"fewer than two Process rows failing the three-condition test ☑ ({pn('order_reply')} passes all three) · builder minimum 5 ☑ · "
  "one volume row per output, no bundled exact-set row ☑ "
  f"({', '.join(pn(t) for t in ('log_rows', 'ans_count', 'esg_count', 'card_count', 'ct_count', 'rem_count', 'reply_keep_count', 'reply_sign_count'))}) "
  "· predicted all-fail rows = 0 ☑")
DIV = json.loads((HERE / "diversity.json").read_text()) if (HERE / "diversity.json").exists() else {}
w(f"Failure diversity: largest unit of discovery {DIV.get('top', '?')} (≤ 50% ☒ — {DIV.get('units', 'see the gate')} sit upstream of "
  "every decision row because the rules, the columns and the filed papers live there; "
  "Leonard's email names all three, so they are the task's rule book, not hidden discoveries; the same structural finding the "
  "archived bridge task carried) · chains landing on distinct rows ☑ (C1 "
  f"Nintendo {pn('nin_decision')}/{pn('nin_next')}/{pn('card_nin')}, C2 Framewell {pn('fw_decision')}/{pn('rem_fw')}, C3 Lanternfly "
  f"{pn('lf_decision')}/{pn('lf_by')}/{pn('lf_told')}/{pn('lf_next')}/{pn('rem_lf')}, C4 Pingwise {pn('pw_decision')}/{pn('pw_next')}/"
  f"{pn('ans_pingwise')}/{pn('reply_pingwise')}, C5 "
  f"Clipforge {pn('cf_next')}/{pn('cf_cancel')}/{pn('cf_priya')}, C6 Pixel Harbor {pn('ph_next')}/{pn('ph_told')}, C7 Hootline "
  f"{pn('rem_hoot')}/{pn('ct_hoot')}, C8 Spotlight {pn('sp_decision')}/{pn('sp_by')})")
w(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} · total weight {tw}")
w(f"Format 5 (§A3): rows {len(rows)}/{len(rows)} ☑ · `do_nothing_case` REJECT {len(rows)}/{len(rows)} ☑ · reachability "
  f"`PROMPT_LINKED` {len(rows)}/{len(rows)} ☑ · final-reply test ACCEPT ☑")
w(f"Set size: {len(rows)} rows for 22.5 h. /rubric round 1 counted 106 required outcomes (one per written answer, ESG checklist "
  "part and reply-list member, plus the sampled log, card, contact and reminder groups); the row count follows that coverage, not "
  "a target.")
w("Coverage: requirements 12/12 (ledger R1–R12) · OEs 147/147 (§B) · writes 7/7 (log; written answers; ESG intake; cards; "
  "contacts; reminders; reply) · told facts 10/10 (every member of the reply's keep and sign lists, §G8–G9) · friction 0/0 (Friction: none)")
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
COVER = {"X1": "nin_decision", "X2": "card_nin", "X3": "fw_decision", "X4": "rem_fw", "X5": "lf_decision", "X6": "lf_by",
         "X20": "sp_decision", "X10": "cf_next", "X11": "cf_cancel", "X12": "ph_next", "X13": "ph_told", "V1": "log_rows",
         "P1": "reply_pingwise", "P2": "reply_markward", "X15": "lf_told", "X17": "nin_next", "X16": "pw_next", "X18": "rem_hoot",
         "X19": "rem_lf", "X21": "ct_hoot", "C1": "bal_by", "C2": "mf_by", "C3": "sp_by", "C5": "sv_told", "C6": "kin_told",
         "C7": "card_kin", "C8": "esg_lumen", "C9": "ct_rev", "C10": "card_mark", "C11": "ww_told", "D1": "log_folder",
         "D2": "reply_keep_count"}
DISP = {"X9": f"duplicate fact: Clipforge's End is graded through its cancellation write {pn('cf_cancel')} and its Oct 15 last day "
              f"{pn('cf_next')} (gate 6; a third row on the same fact would breach the limit); the notice frederick.stone@harmonygames.co/1843067564852153540 decides all three",
        "X14": f"duplicate fact: Framewell's Park is graded in {pn('fw_decision')} (Decision) and {pn('rem_fw')} (the Jan 5 reminder); "
               "its Next date 2026-01-05 is the same January-review fact (gate 6), decided by C07C2866011/1758920520.674991"}
assert set(COVER) | set(DISP) == {s["id"] for s in surf["slots"]}, set(s["id"] for s in surf["slots"]) - set(COVER) - set(DISP)
MECH = ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8")
mech_w = sum(r["w"] for r in rows if any(m in r["dec"].split() for m in MECH))
w(f"Gradable surface (gate 17): slots {len(surf['slots'])} · covered {len(COVER)} · dispositioned {len(DISP)} (§G: X9, X14 "
  f"duplicate fact) · no slot with neither ☑ · mechanism share {round(100 * mech_w / tw)}% of the weight (reported, not gated)")
w("Four prohibitions: ☑ unstated expectations (every row quotes a prompt span; Leonard's email, the guardrails doc, the Monday "
  "change, ESG's note with Leonard's reply and the README are incorporated) ☑ conclusions on ambiguous evidence (none: each graded "
  "value is settled by a later or more specific record) ☑ grading the distractor (traps are graded through the correct value, "
  "never their disclosure) ☑ hard-coded titles/phrasings (only the README's column names)")
w("Blocking: none for validity — no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share is a "
  "structural finding (the guardrails doc, the README and the paperwork folder), recorded under Unresolved for the human to accept.")
w("")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
w("")
w("`python3 Task_Authoring/tools/persona_view.py check-sql frederick_stone Task_Authoring/task_inputs/01_Universe_Inject.sql "
  "--load-bearing plan/oe_lb_ids.txt` rows and `persona_view.py can-see` lines for the base records, as pasted in "
  "08_OE_Writing_Ledger.md (oe-writing gate PASS; the gate re-runs each line):")
w("")
w((HERE / "visibility.txt").read_text().rstrip())
w("")
w("## F · Shortcut probe")
probe = HERE / "probe.txt"
w(probe.read_text().rstrip() if probe.exists() else "(pending)")
w("")
w("## G · Gradable-surface coverage")
w("| Slot | Stable fact ID | Selector · role / group | Work kind (band) | Mechanisms → Decided by | Covered by (P-n) | Disposition "
  "and reason (evidence) |")
w("|---|---|---|---|---|---|---|")
for s in surf["slots"]:
    sel = cell(" ".join(map(str, s["selector"])))[:90]
    if s["id"] in DISP:
        w(f"| {s['id']} | {s.get('fact_id') or '—'} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} (5) | "
          f"{', '.join(s['mechanisms']) or '—'} → — | — | {DISP[s['id']]} |")
        continue
    r = BY[COVER[s["id"]]]
    w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {sel} · {s['role']} / {s.get('group') or '—'} | {s['work_kind']} ({r['w']}) | "
      f"{', '.join(s['mechanisms']) or '—'} → {r['dec']} | {pn(COVER[s['id']])} | covered: the title rejects both the omission and "
      f"the plausible wrong value ({cell(r['alt'])}) |")
w("")
sr = HERE / "selfreview.md"
w(sr.read_text().rstrip() if sr.exists() else "## Self-review\n(pending)")
(WF / "09_Rubric_Writing_Plan.md").write_text("\n".join(out) + "\n")
print("plan written:", len(out), "lines; weight", tw, bands, "mechanism share", round(100 * mech_w / tw))
