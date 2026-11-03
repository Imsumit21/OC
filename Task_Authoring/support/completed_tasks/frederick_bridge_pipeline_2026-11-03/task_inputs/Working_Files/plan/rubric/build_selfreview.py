#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = json.loads((HERE / "rows.json").read_text())
tw = sum(r["w"] for r in rows)
T = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
ones = ", ".join(T[r["tag"]] for r in rows if r["w"] == 1)
out = ['## Self-review', '', 'Prep self-review (playbook §Self-review, GEN_EXECUTION §6a):', '',
       '1. Re-read as /rubric (3_Rubrics_Eval.md 1.4 and 3.1): every prompt requirement (ledger R1–R12), every write '
       '(sheet create/move/rows, 4 checklists, 25 items, 18 cards, the comment, the reply), every told fact (four group '
       f'counts), the ordering requirement ("Once it\'s done reply here": {T["order_file"]} after the send list writes, '
       f'{T["order_checklists"]} after the checklist writes, {T["order_cards"]} after the new To Do cards, '
       f'{T["order_comment"]} after the Anel card comment, one write kind each) and every exclusion (Paul, the six named '
       'nos, the 48 off-list names, Dentsu and Makers cards) has a row on the correct artifact; exclusions are graded as '
       f'exact counts or scopes on required writes ({T["count25"]}, {T["angels"]}, {T["cl_keep_warm"]}, {T["cl_new_investor"]}, '
       f'{T["cl_in_talks"]}, {T["cl_awaiting_reply"]}, {T["cards18"]}), never as leave-alone rows.',
       '2. Counter-readings per row (a = could a valid answer fail; b = could a wrong answer pass):', '',
       '| Row | Counter-reading | Resolution (evidence) |', '|---|---|---|']
for k, r in enumerate(rows, 1):
    out.append(f"| P{k} | (a) a valid run writes {r['valid']} — the title accepts {'; '.join(r['acc'])}. (b) strongest "
               f"wrong answer: {r['alt']} | Rejected by the title's value {r['vals']}; deciding records {r['fids']} "
               f"re-verified through hg.py / SQL ({', '.join(r['oe'][:2])}) |")
out += ['',
        '3. Re-verify: every source value in 00_V3_Authoring_Evidence.json rubric_rows was read in this run by '
        'plan/rubric/build_rubric.py — seeded rows through base_check.parse_sql of 01_Universe_Inject.sql, base records '
        'through `hg.py search get-many` (calendar events /events/1368, /1525, /5523, /8468, /9414; #bridge-pitch /33, '
        '/89, /159, /252; Trello /cards/801, /boards/1; Gmail threads 1832208184829815962 and 1843473831194478743). '
        'C27\'s evidence names the Dentsu calendar entry evt_3671b9a924ccba550e51fa as /rubric round 1 asked; it was '
        'created 2025-10-01T00:02:03Z, after the 00:00Z seed bound, so its dated source record is Leonard\'s Sep 25 '
        'Dentsu mail (thread 1843473831194478743), which books the same meeting. The 327 MB '
        'Sheets export is not cited as a source record (its bounded reads exceed the checker\'s 120 s limit); the 2025 list '
        'facts it holds (Sony Mobile No. 83 Latest Status, GFR Fund\'s Partner, the five angels) were re-read from the '
        'seeded grid UPDATE in 01_Universe_Inject.sql and are cited through the records that carry the same fact. Counts recomputed from rows: 25 = 1 + 7 + 14 + 3; 18 = 21 − '
        'NCsoft − Dentsu − Makers; the batch-2 replay (run_forensics/rev12/baseline2) confirms every sampled card, item, '
        'reply count and the reply order on a correct run.',
        '4. Predicted all-fail re-check: 0 rows. Every scoped record behind the cited F-ids has a persona_view YES line '
        '(pasted under §E); every write maps to a cataloged tool (gsheets_create_spreadsheet, gdrive_move_file, '
        'gsheets_values_update, trello_create_checklist, trello_create_check_item, trello_create_card, trello_add_comment, '
        'gmail_reply_to_message); Friction: none, so no rate-1.0 retry; no row needs evidence outside Frederick\'s view. '
        'Batch 2 run 6 passes every row.',
        '5. Shortcut and diversity: the §F probe hits are the population sources the task requires (the 2025 list and the '
        '#bridge-pitch status posts hold names, not groups, amounts or build access); counter-reading: could a run answer '
        'from the 2025 list alone? No — SciPlay, Hiro, Homa, Brightwater, Paul, Anton\'s amount and build access all need '
        'other records (F13, F17, F19–F21, F42). Diversity: the send-list doc F2 sits in the Depends-on closure of most rows '
        '(structural, see Unresolved).',
        '6. Surface dispositions: 20 of 21 slots of 01_Gradable_Surface.json are covered by a row; ST5 (LVP Keep warm) is '
        'sampled out because G1 already grades five members (SciPlay, Hiro, Treo VC as samples; Homa, Brightwater as '
        'direct rows). Strongest case for a row: LVP is a control in the CORR portfolio entry; resolution: LVP is not core '
        f'(no prompt span names it) and its Keep warm placement still counts in {T["cl_keep_warm"]} and {T["cnt_keep_warm"]}.',
        f'7. Weights by kind of work (1 lookup · 3 interpretation · 5 multi-source): every group, item, card, count and '
        f'volume row is 5 because each joins records from two or more services (calendar, Slack, Gmail, the doc rule, the '
        f'card rule); /rubric round 1 raised the former 3s (Treo VC, a16z, Anton\'s group, the SciPlay and Homa items, the '
        f'GFR, BBQ and Brightwater cards) to 5 on that ground, and no row is left at 3; {ones} are 1 (one record or one '
        f'stated order). Total {tw}; the replay of batch 2 under these weights keeps every difficulty gate (average 77.7%, '
        f'SD 0.106, largest pattern 40%, 1 full pass; run_forensics/rev12/baseline2/difficulty_projection_draft3.json).',
        '8. No-criterion-text scan: criterion titles live in 09_Rubrics.json (draft mode); the plan carries them only as '
        'the do_nothing_case quotes in §A3.', '',
        'Unresolved: (1) diversity.authority_share — the send-list doc (F2) decides most of the weight by construction '
        '(every group rule lives in it); a design finding for the human to accept, as on the Robert, Douglas and Julia '
        'tasks. (2) Human time 19.25 h comes from an earlier revision\'s worksheet; /create-humantime refresh is pending and '
        'does not change any row.']
(HERE / "selfreview.md").write_text("\n".join(out) + "\n")
print("selfreview rows", len(rows))
