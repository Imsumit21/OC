#!/usr/bin/env python3
"""Write Working_Files/09_Rubric_Check.md (check mode) from 09_Rubrics.json and rows.json. Row numbers come from each
row's stable tag (rows.json), so inserting or splitting rows never leaves a stale C-number here."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[2]
crit = json.loads((TI / "09_Rubrics.json").read_text())
rows = json.loads((HERE / "rows.json").read_text())
assert len(crit) == len(rows)
assert all(c["title"] == r["t"] for c, r in zip(crit, rows))
C = [f"C{i + 1}" for i in range(len(crit))]
T = {r["tag"]: f"C{i + 1}" for i, r in enumerate(rows)}
tw = sum(c["weight"] for c in crit)


def c(*tags):
    return ", ".join(T[t] for t in tags)


def span(a, b):
    return f"{T[a]}–{T[b]}"


def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


out = []
w = out.append
w("# 09 Rubric Check — frederick_bridge_pipeline (Q4 investor update send list, injection rev12)")
w(f"Checked 2026-11-03 · Criteria {len(crit)} (builder minimum 5: ok) · Plan 2026-11-03 (09_Rubric_Writing_Plan.md, rows "
  f"P1–P{len(rows)} = C1–C{len(crit)}) · Revision 3: /rubric round 2 (Platform_Report/rubric_report2, FAIL 2, reviewed "
  f"JSON 9f5b032d5ae0, 38 rows) Fix List applied on top of round 1 (Platform_Report/rubric_report1, FAIL 1, reviewed JSON "
  f"5875117a9b71, 33 rows)")
w("JSON field map: criterion=`title` · weight=`weight` · category=`category` · justification=`justification` · "
  "evidence=`evidence` · schema gate: pass (a JSON array of objects; every row has all five fields non-blank; category "
  "Outcome or Process; weight 1, 3 or 5)")
w("Readiness for /rubric: CLEAN — a prediction only; /rubric gives the verdict")
w("Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)")
w("")
w(f"Lint (`python3 Task_Authoring/tools/hg.py rubric-lint Task_Authoring/task_inputs/09_Rubrics.json`): 9 findings, all "
  f"`anon_token`: `[PERSON_NAME_0854]` on {c('homa', 'ba_homa', 'item_homa')} (title and evidence) and `[PERSON_NAME_2306]` "
  f"on {c('card_gfr')} (title and evidence). Resolved: each token is the source string for that name (Homa in Frederick's "
  f"mail; GFR Fund's Partner on the 2025 list), bound as LITERAL and accepted as shown beside the plain names (2.10; "
  f"rubric_factual_checks.md; /rubric round 1 resolved the same hits the same way). No `disguised_negative`, "
  f"`format_lock` or `evidence_no_record` hit; the lexical negative pre-scan of every title and the `such as` / `e.g.` / "
  f"`for example` scan of every field are clean.")
w("")
w("## Coverage")
w("| Plan row / requirement | Criteria | Covered / gap (omission + wrong-result test) |")
w("|---|---|---|")
cov = [
    ("Send list file in Frederick's Q4 2025 investor update folder (prompt)", c("folder"),
     f"covered — a file left in My Drive fails {T['folder']}"),
    ("A native Google Sheet or Doc (README 'Google Sheets or Docs only, no uploads')", c("native"),
     f"covered — an uploaded xlsx fails {T['native']} and still passes {T['folder']} (split per /rubric R1)"),
    ("File named per the folder README", c("name"), f"covered — another name (e.g. the doc's own title) fails {T['name']}"),
    ("Who gets the update: the list plus off-list callers, everyone else off; not the whole 2025 list (email, doc)",
     c("count25", "homa", "brightwater", "angels"), f"covered — 26 rows (Paul) or the whole list fails {T['count25']}; "
     f"leaving Homa or Brightwater off fails {c('homa', 'brightwater')}"),
    ("Group per recipient (doc's four groups)", span("sciplay", "anton_group"),
     f"covered — SciPlay In talks fails {T['sciplay']}; Hiro Awaiting reply fails {T['hiro']}; Treo off fails "
     f"{T['treo']}; a16z off fails {T['a16z']}; Anton In talks fails {T['anton_group']}"),
    ("Amount for the new investor (doc; email 'Get the new investors right')", c("anton_amount"),
     f"covered — 40,000 fails {T['anton_amount']}"),
    ("Angels who said yes but haven't signed (Paul's back-out)", c("angels"),
     f"covered — Paul In talks at 50,000 gives two angels and fails {T['angels']} (count only, per /rubric R12)"),
    ("Build access for firms in talks (doc: iOS only, Android only, iOS and Android, or none)", span("ba_dentsu", "ba_homa"),
     f"covered — 'iOS and Android' from ZOM-567 fails {span('ba_dentsu', 'ba_brightwater')}; a Homa value other than none "
     f"fails {T['ba_homa']}"),
    ("Keep warm checklist, one item per firm (card comment Sep 13)", c("cl_keep_warm", "item_sciplay"),
     "covered — 2 items or SciPlay elsewhere fails"),
    ("New investor / In talks / Awaiting reply checklists, one item per firm or angel (card comment Sep 29)",
     c("cl_new_investor", "item_anton", "cl_in_talks", "cl_awaiting_reply", "item_sony", "item_homa"),
     f"covered — Paul or SciPlay on In talks gives 8 or 9 and fails {T['cl_in_talks']}; a New investor item other than "
     f"Anton fails {T['item_anton']}; Sony left off Awaiting reply fails {T['item_sony']}; Homa omitted fails "
     f"{T['item_homa']}"),
    ("Follow-up cards in To Do for In talks and Awaiting reply (card comment Sep 29)", span("cards18", "card_brightwater"),
     f"covered — 19 or 20 cards fail {T['cards18']}; a GFR, BBQ or Brightwater card absent fails "
     f"{span('card_gfr', 'card_brightwater')}"),
    ("Comment on an existing To Do card instead of a second card (NCsoft / Anel)", c("ncsoft_comment"),
     f"covered — a new NCsoft card and no comment fails {T['ncsoft_comment']} (and {T['cards18']} at 19)"),
    ("No card for anyone with a call after Sep 30 (Dentsu, Makers)", c("cards18"),
     "covered — the exact scope 18 fails a run that adds a Dentsu or Makers card"),
    ("Reply on Leonard's thread (prompt)", c("reply"), f"covered — a draft or a new thread fails {T['reply']}"),
    ("How many firms and angels in each group (email)", span("cnt_new_investor", "cnt_keep_warm"),
     f"covered — In talks 8/1 fails {T['cnt_in_talks']}; Keep warm 2 fails {T['cnt_keep_warm']}"),
    ("Reply once the work is done ('Once it's done reply here')",
     c("order_file", "order_checklists", "order_cards", "order_comment"),
     f"covered — a send list write after the reply fails {T['order_file']}; a checklist write after the reply fails "
     f"{T['order_checklists']}; a new To Do card after the reply fails {T['order_cards']}; the Anel comment after the "
     f"reply fails {T['order_comment']} (one write action per row, per /rubric rounds 1 and 2)"),
]
for a, b, d in cov:
    w(f"| {a} | {b} | {d} |")
w("Unauthorized criteria: none")
w("")
w("## Coverage — gradable surface")
w("| Surface slot | Stable fact ID | Criteria | Covered / dispositioned / gap | Disposition reason (evidence) |")
w("|---|---|---|---|---|")
surf = json.loads((TI / "Working_Files/01_Gradable_Surface.json").read_text())
cover = {k: T[t] for k, t in {"V1": "count25", "ST1": "sciplay", "ST2": "hiro", "ST3": "homa", "ST4": "brightwater",
                              "AC1": "ba_dentsu", "AC2": "ba_t_accelerate", "AC3": "ba_ncsoft", "AC4": "ba_brightwater",
                              "M3": "anton_amount", "G2": "anton_group", "RP1": "reply", "RP2": "cnt_in_talks",
                              "RP3": "cnt_keep_warm", "DL1": "folder", "CL1": "item_homa", "FU1": "card_gfr",
                              "FU2": "card_bbq", "FU3": "card_brightwater", "AN1": "ncsoft_comment"}.items()}
for s in surf["slots"]:
    if s["id"] == "ST5":
        w(f"| ST5 | group_lvp | — | dispositioned (sampled out) | G1 grades five other members ({T['sciplay']} SciPlay, "
          f"{T['hiro']} Hiro, {T['treo']} Treo VC as samples; {T['homa']} Homa and {T['brightwater']} Brightwater as "
          f"direct rows; gate 15); LVP's Keep warm placement still counts in {c('cl_keep_warm', 'cnt_keep_warm')} (LVP "
          f"pass frederick.stone@harmonygames.co/1842277743427687737) |")
        continue
    cn = cover[s["id"]]
    r = rows[int(cn[1:]) - 1]
    w(f"| {s['id']} | {s.get('fact_id') or r['fact']} | {cn} | covered | the title rejects the omission and the trap value "
      f"({cell(r['alt'])}) |")
mech = sum(r["w"] for r in rows if any(m in r["dec"] for m in ("DONE1", "DONE2", "CORR", "ALIAS", "FILT", "INPUT", "DUP",
                                                               "BOOKED", "FOLLOW")))
w(f"Mechanism share: {round(100 * mech / tw)}% of the criteria weight (reported, not gated)")
w("")
w("## Findings")
w(f"Findings on the {len(crit)}-row JSON as it stands. /rubric round 1's findings (Platform_Report/rubric_report1, 33 rows) "
  "and their repairs are in the Round-1 Fix List section below; they quote the old wording, which this JSON no longer has.")
w("| # | Criterion | Quoted span | Rule (source §) | What is wrong | Plan row / ledger fact | `/rubric` type | Severity |")
w("|---|---|---|---|---|---|---|---|")
F = [
    (c("homa", "ba_homa", "item_homa", "card_gfr"), "\"[PERSON_NAME_0854]\" · \"[PERSON_NAME_2306]\"",
     "2.10 anonymized token; lint `anon_token`", "Lint flags the tokens; each is the source string for that name (Homa in "
     "Frederick's mail; GFR Fund's Partner on the 2025 list) and stands beside the plain names", "F20, F22", "—",
     "none (LITERAL, accepted as shown; round 1 resolved the same hits the same way)"),
    (c("order_file", "order_checklists", "order_cards", "order_comment"),
     "\"at least one such write comes before the reply and none after it\" · \"no checklist write of any kind on that card "
     "(adding, renaming, ticking or deleting a checklist or item) comes after it\"", "3.2 Process audit; 2.2 atomicity; "
     "2.10 self-contained", "Round 2's Fix List text, copied exactly: one order row per write action (send list file, "
     "checklists, follow-up cards, Anel comment); each Accept line names the same write kinds as its title, so no write "
     "after the reply passes the note and fails the title", "F1, F46, F47", "—",
     "none (round 2 checked each with the opposite-pair test)"),
    (c("cards18"), "\"Dentsu meeting evt_3671b9a924ccba550e51fa\"", "evidence citation; V3 dated source",
     "The deciding calendar entry is named as round 1 asked; it was created 2025-10-01T00:02:03Z, after the 00:00Z seed "
     "bound, so the V3 dated source record is Leonard's Sep 25 mail that books the same Oct 1 1:30pm PT meeting (the "
     "evidence names both)", "F49", "—", "none"),
]
for i, f in enumerate(F, 1):
    w(f"| {i} | {' | '.join(cell(x) for x in f)} |")
w("")
w("## Round-2 Fix List applied (Platform_Report/rubric_report2)")
w("Copied exactly from the report's Fix List; R-n are the 38-row rubric's numbers.")
w("| Fix | Now | Round-2 issue | Round-2 type and severity | Repair |")
w("|---|---|---|---|---|")
FX2 = [
    (T["order_file"], "R37's Accept line counted only create, move or rows while the title rejects any write after the "
     "reply", "not_self_contained, Major", "title and evidence list creating, moving, renaming or editing the file; "
     "Process, weight 1 and the justification kept"),
    (T["order_checklists"], "R38's Accept line counted only checklists or items added while the title rejects any "
     "checklist write after the reply", "not_self_contained, Major", "evidence: no checklist write of any kind (adding, "
     "renaming, ticking or deleting a checklist or item) after the reply; title kept"),
    (T["order_cards"], "No row ordered the follow-up cards before the reply", "Process Rubrics (missing ordering check)",
     "new Process row, weight 1, the report's title, justification and evidence"),
    (T["order_comment"], "No row ordered the NCsoft comment on the Anel card before the reply",
     "Process Rubrics (missing ordering check)", "new Process row, weight 1, the report's title, justification and "
     "evidence"),
    (T["card_bbq"], "Notes for QM (not scored): the justification put 'BBQ Capital (sent, no update)' on both posts",
     "wording only", "the Sep 3 post reads 'BBQ Capital (sent)' (#bridge-pitch /33); only the Sep 8 post (/89) has "
     "'(sent, no update)'"),
    (T["cards18"], "Notes for QM (not scored): the evidence said the Dentsu meeting was 'booked' in Leonard's Sep 25 mail",
     "wording only", "now 'confirmed in' Leonard's Sep 25 mail"),
]
for i, f in enumerate(FX2, 1):
    w(f"| {i} | {' | '.join(cell(x) for x in f)} |")
w("")
w("Round-2 items the report rejected and kept as they were: the 18-card volume row may state the 'F/up with' template; "
  "folding the cards into the checklist order row would join two write actions; the Sciplay, Homa, Brightwater, Paul, "
  "Anton and Treo/a16z/Sony groups share a root cause, not an embedded condition; the order rows check different "
  "conditions on different write actions; the group counts accept one number because the prompt asks how many ended up "
  "in each group.")
w("")
w("## Round-1 Fix List applied (Platform_Report/rubric_report1)")
w("Each repair uses the report's own wording where it gave one. R-n are the 33-row rubric's row numbers; the old wording "
  "quoted here is no longer in the JSON.")
w("| Fix | Now | Round-1 wording | Rule (source §) | Round-1 issue | Round-1 type and severity | Repair |")
w("|---|---|---|---|---|---|---|")
FX = [
    (c("folder", "native"), "R1 'as a Google Sheet or Google Doc inside Frederick's Drive folder'", "2.2 atomicity",
     "R1 bundled the folder (prompt) with the native type (README): an uploaded xlsx in the folder passes one and fails "
     "the other", "non_atomic, Major", "split; both weight 1"),
    (c("angels"), "R12 'exactly one angel on the bridge-round send list: Anton Bernstein'",
     "2.2 atomicity; 2.10 self-contained", "R12 bundled a count with an identity and never said who counts as an angel",
     "non_atomic + not_self_contained, Major", "bare count; the title defines an angel as an individual investor, not a "
     f"firm; Anton stays graded in {c('anton_group', 'anton_amount')}"),
    (c("cl_new_investor", "item_anton"), "R18 'holding exactly 1 item: Anton Bernstein'", "2.2 atomicity",
     "R18 bundled the item count with the item", "non_atomic, Major", "count row plus an Anton item row"),
    (c("card_gfr"), "R24 'named F/up with and GFR Fund or its contact's name'", "2.10 self-contained",
     "R24's contact was named nowhere a judge can see", "not_self_contained, Major",
     "the title names GFR Fund, GFR, PERSON_0787_NAME or [PERSON_NAME_2306], the call title and list Partner forms"),
    (c("order_file", "order_checklists"), "R33 'after its last write to the send list sheet and to the Harmony Games "
     "Trello board'", "2.2 atomicity; 3.2 Process audit", "R33 held two order checks across two services and said "
     "'sheet' though a Doc is valid", "non_atomic, Major (+ harmless_specificity Minor)",
     f"{T['order_file']} is the report's own send-list row; {T['order_checklists']} is the author's rewrite (Findings 2)"),
    (c("item_sony"), "R20 counted 14 Awaiting reply items and named none", "3.6 sampling; coverage",
     "No row named any Awaiting reply item, so a wrong member set with the right count passed", "missing_coverage, Major",
     "Sony Mobile item row, the advisor's-read edge case"),
    (c("treo", "a16z", "anton_group", "item_sciplay", "item_homa", "card_gfr", "card_bbq", "card_brightwater"),
     "weight 3", "2.12 weights by kind of work", "Each placement joins records across services (calendar, Slack, Gmail, "
     "doc and card rules); 8 of 33 rows one level low", "Criteria Weights", "all eight now 5"),
    (c("homa", "brightwater", "ba_dentsu", "ba_t_accelerate", "ba_brightwater", "treo"),
     "name forms only in the evidence", "2.10 self-contained", "Accepted name forms lived only in the evidence Accept line",
     "repair", "the forms are in each title, the report's wording"),
    (c("cl_keep_warm", "cl_in_talks", "cl_awaiting_reply", "cl_new_investor"), "'close variants of the name'",
     "2.10 self-contained; QC B12", "'Close variants' was undefined, and the evidence read 'a In talks', 'a Awaiting reply'",
     "repair", "Accept: a checklist whose name contains the group name, any letter case, spacing or plural, other words "
     "allowed"),
    (c("cards18"), "R23 'Dentsu mail frederick.stone@harmonygames.co/1843473831194478743'", "evidence citation",
     "The deciding record for the Dentsu exemption is the calendar event, not Leonard's mail", "evidence repair",
     "the evidence names evt_3671b9a924ccba550e51fa (Oct 1 1:30pm PT) and the Accept line names the card form (Findings 3 "
     "on the dated source)"),
    (c("ba_homa"), "R13–R16 all test 'iOS only'", "3.6 sampling selection (repair)", "The 'none' value was never sampled",
     "repair (optional)", "Homa 'none' row; the report counted it in its 38 rows"),
]
for i, f in enumerate(FX, 1):
    w(f"| {i} | {' | '.join(cell(x) for x in f)} |")
w("")
w("Round-1 items rejected by the report and kept as they were (not re-opened): R17/R19/R20 checklist plus count is one "
  "destination and one fact; R3–R16 destination defined by the folder row; 'Treeo VC' is the Sep 3 post's spelling; "
  "R29–R32 accept one number; R13–R16 are not a cascade; the two order rows check different conditions; an angel "
  "blank-cell row would fail Negative Criteria.")
w("")
w("## Overlap groups · Spot-check groups · Predicted all-fail")
w("| Group / row | Members / basis | Shared condition / reason |")
w("|---|---|---|")
w(f"| Overlap groups | none | The round-1 group `anton-listed` (R10, R12) is gone: {T['angels']} counts angels without "
  f"naming Anton. Rows that fail together on SciPlay's group ({c('sciplay', 'cl_keep_warm', 'cl_in_talks', 'item_sciplay', 'cards18', 'cnt_in_talks', 'cnt_keep_warm')}) "
  f"or Paul's back-out ({c('count25', 'angels', 'cl_in_talks', 'cards18', 'cnt_in_talks')}) share a likely root cause, not an "
  f"embedded acceptance condition: each grades a different count or record (3.3) |")
w(f"| G1 send-list groups | {c('sciplay', 'hiro', 'treo')} (samples) + {c('homa', 'brightwater', 'a16z', 'anton_group', 'anton_amount', 'angels')} "
  f"(direct rows for distinct outcomes) | volume {T['count25']} = 25 |")
w(f"| G2 build access | {span('ba_dentsu', 'ba_brightwater')} (iOS only, the four firms Arthur's post names) + "
  f"{T['ba_homa']} (none) | volume {T['count25']}; GFR and a16z unsampled |")
w(f"| G3–G6 checklists | {c('item_sciplay')} (Keep warm), {c('item_anton')} (New investor), {c('item_homa')} (In talks), "
  f"{c('item_sony')} (Awaiting reply) | volumes {T['cl_keep_warm']} = 3, {T['cl_new_investor']} = 1, {T['cl_in_talks']} = 7, "
  f"{T['cl_awaiting_reply']} = 14 |")
w(f"| G7 follow-up cards | {c('card_gfr', 'card_bbq', 'card_brightwater')} + direct exception {T['ncsoft_comment']} | "
  f"volume {T['cards18']} = 18 |")
w(f"| Predicted all-fail | none — 0 rows | Every value is reachable by Frederick through cataloged tools (plan §E visibility "
  f"proof; reach.plan_fids); batch-2 run 6 passes all {len(crit)} rows |")
w("")
w("## Dimensions")
w("| Dimension | Count / % | Threshold | Status |")
w("|---|---|---|---|")
n = len(crit)
n_proc = sum(1 for x in crit if x["category"] == "Process")
w(f"| Overall Rubric Quality | 0 Major · 0 Moderate · 0 Minor of {n} rows (0%) | any Major/Moderate fails; Minor < 5% "
  f"passes | PASS |")
w(f"| Criteria Weights | 0 of {n} rows off by one level | ≤ 10% one level off is NON-FAIL 4; all match is PASS | PASS |")
w(f"| Category Balance | {n - n_proc} Outcome · {n_proc} Process | ≥ 1 Outcome, Process ≤ 50% | PASS |")
w(f"| Process Rubrics | 0 ordering dependencies without a check; "
  f"{c('order_file', 'order_checklists', 'order_cards', 'order_comment')} pass the three-condition test, one write "
  f"action each (file, checklists, cards, comment) | 1 missing is NON-FAIL 3 | PASS |")
w(f"| Agent-Centric Phrasing | 0 of {n} titles off pattern (every title starts \"The Agent\"; no tool identifier) | > 10% "
  f"off pattern fails | PASS |")
w(f"| Negative Criteria | 0 prohibition-only titles; do_nothing_case REJECT on {n}/{n} | any idle-pass row fails | PASS |")
w("| Predicted all-fail | 0 | tolerance 0 | PASS |")
w("| Known data issue | 0 rows rest on a card in references/known_data_issues/synthcut.md | any fails | PASS |")
w("| Schema, accuracy, coverage and contradiction repair gates | schema ok; values re-read (V3 rubric_rows); 16/16 "
  "requirements and 20/21 slots covered plus ST5 dispositioned; rows jointly satisfiable (run 6) | a failure blocks | PASS |")
w(f"Threshold margin: with {n} rows one Minor issue is {100 / n:.1f}% (NON-FAIL band from 5%), one Major or Moderate fails.")
w("")
w("## Self-review")
w("| Check | Verdict | Strongest counter-reading | Resolution | Unresolved |")
w("|---|---|---|---|---|")
for cid, r, x in zip(C, rows, crit):
    w(f"| {cid} ({x['category']}, weight {x['weight']}) | cleared | False negative? A valid run writes {cell(r['valid'])}; "
      f"near miss: {cell(r['alt'])} | Title accepts {cell('; '.join(r['acc']))}; it rejects the near miss by naming "
      f"{cell(r['vals'])}; deciding records {r['fids']} re-verified (plan/rubric/build_rubric.py, hg.py get-many / SQL) | "
      f"none |")
w(f"| Fix 1–6 (round-1 Majors) | resolved | Could a split row now bundle again? | Each new row names one destination and "
  f"one value; the opposite-pair test passes: an uploaded xlsx in the folder passes {T['folder']} and fails {T['native']}; "
  f"Anton plus Paul fails {T['angels']} and passes {T['item_anton']}; Paul alone on New investor passes "
  f"{T['cl_new_investor']} and fails {T['item_anton']} | none |")
w(f"| Fix 7 (weights) | resolved | Could a raised 5 be a 3 (one rule on one record)? | Each joins two or more services; "
  f"no row is left at 3, which /rubric's own weight pass asked for; the batch-2 replay keeps every difficulty gate "
  f"(average 77.7%, SD 0.106, 4 patterns, largest 40%; difficulty_projection_draft3.json) | none |")
w(f"| Findings 2 ({c('order_file', 'order_checklists', 'order_cards', 'order_comment')}) | cleared | Does an Accept "
  f"line still count fewer writes than its title, or does a row bundle two write actions? | Each row is the round-2 Fix "
  f"List text: the file row lists creating, moving, renaming or editing in both title and Accept; the checklist row's "
  f"Accept rejects any checklist write after the reply; cards and the comment have their own rows. A run with none of "
  f"that work fails each row; batch-2 runs 1–6 wrote the file, checklists, cards and the Anel comment before the reply "
  f"(trajectory call order), so no valid run is rejected | none |")
w(f"| Fix 6 ({T['item_sony']}) | resolved | Is Sony a fair Awaiting reply member? | List No. 83 Latest Status 'Reached "
  f"out - no response as of 09/11' (seeded grid), no call on Fred's calendar, and the Sep 8 advisor read is not the "
  f"firm's answer (doc); all six batch-2 runs put Sony Mobile on the Awaiting reply checklist | none |")
w(f"| Fix 11 ({T['ba_homa']}) | resolved | Could a blank cell be fair for Homa? | The doc leaves blanks for angels "
  f"only and lists 'none' as a value for firms in talks; all six batch-2 runs wrote 'none' | none |")
w(f"| Findings 3 ({T['cards18']} dated source) | cleared | Does citing Leonard's mail undo round 1's evidence repair? | "
  f"The evidence still names the calendar entry evt_3671b9a924ccba550e51fa as the deciding record; the mail is the "
  f"pre-bound record of the same booked meeting, so the value 18 and the Dentsu exemption are unchanged | none |")
w(f"| Mutation test | cleared | Change one value at a time | SciPlay → In talks fails "
  f"{c('sciplay', 'cl_keep_warm', 'cl_in_talks', 'item_sciplay', 'cards18', 'cnt_in_talks', 'cnt_keep_warm')}; Paul added "
  f"fails {c('count25', 'angels', 'cl_in_talks', 'cards18', 'cnt_in_talks')}; one build cell 'iOS and Android' fails its "
  f"own row; Anton 40,000 fails {T['anton_amount']}; Sony dropped fails {c('cl_awaiting_reply', 'item_sony')}; reply first "
  f"fails {c('order_file', 'order_checklists', 'order_cards', 'order_comment')} | none |")
w("")
w("Re-verified: every literal through `hg.py search get-many` or the SQL (build_rubric.py reads each source value; "
  "00_V3_Authoring_Evidence.json rubric_rows); the Sony Mobile and GFR Fund list cells from the seeded grid in "
  "01_Universe_Inject.sql. Predicted all-fail recounted from recorded defects: 0. Tally recounted: 0 Major, 0 Moderate, "
  "0 Minor.")
w("Unresolved: the upstream rubric-writing gate carries one structural FAIL (diversity.authority_share, the send-list doc), "
  "recorded in the plan for the human to accept; this check inherits it through chain.rubric-writing.")
w("")
w("## Reminders")
w(f"- An all-Outcome set is normal; Process is not added to look thorough "
  f"({c('order_file', 'order_checklists', 'order_cards', 'order_comment')} are the real ordering requirement, one write "
  f"action each, as /rubric round 2 asked).")
w("- Fix the criteria in the builder, re-export, re-run check, then run /rubric.")
(TI / "Working_Files/09_Rubric_Check.md").write_text("\n".join(out) + "\n")
print("check written", len(out), "lines")
