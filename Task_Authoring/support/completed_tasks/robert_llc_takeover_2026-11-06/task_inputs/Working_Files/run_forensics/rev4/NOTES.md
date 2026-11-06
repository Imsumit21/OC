# rev4: platform verdicts (attempt 6adfee3b47f7621feba5b96c, 2026-11-05/06)

- SQL `01_Universe_Inject.sql` sha256 f1a290ced176 (136 INSERT + 3 UPDATE; the platform calls it revision 9). Byte-identical to the task folder's SQL.
- Prompt `04_Prompt.txt` sha256 ccd229a59a17 (unchanged since rev2; the platform calls it revision 10).
- `/injection` (injection-static-v2): **PASS**, Checks A–C (`0_injection_PASS_r4.md`, sha256 3eddbcacb480).
  - Lint shows 0 FAIL, 0 CHECK and 0 INFO. There are no demonstrated defects.
  - Reused advisories: A-2, A-3, A-4, A-6, A-7 and A-8.
  - A-5 is updated: the Calm Play comment now comes before the ground-rules doc.
  - A-9 is new: CF AWS is $95 in ENG-2445 and $62 in the later "jenkins" email, so the answer is $62. Keep the rubric off Snowflake's HG-wide AWS totals (NB-2).
- `/prompt` (task-quality-v1): **PASS, score 5**, with every sub-dimension at 5 (`1_prompt_PASS_r4.md`, sha256 2064e5cf6bcb).
  - Dataset similarity PASS; the nearest neighbour is 0.776 (same scenario).
  - Deep recheck: 15 findings, none confirmed. All forks F1–F6 are settled, including ENG-2454 layer.ai Canceled, which the rev4 fix targeted.
  - Platform defect: FD-2880 (PR #1917's base_sha isn't in the commits export; not scored).
  - The decision sweep matches solver/truth.json:
    - 6 base Todo: ENG-2438 Robert, 2439 Leonard, 2441 Arthur, 2445 Arthur, 2451 Leonard, 2462 Arthur.
    - The new Meta VO campaign issue: Todo, Leonard.
    - Done: 2447, 2448, 2449.
    - Canceled: the other 28, including ENG-2452 and ENG-2454.
    - Money: $3,450 a month, $1,150 each, Arthur $902 cash.
- `/hardness` (model-aware-v3, OPUS_OBSERVED): **PASS, score 5, Really hard, PROCEED** (`precheck/1a_hardness_PASS_r4.md`, sha256 5e1620a64ec3).
  - This was pre-check 2 of 2. The run is `precheck/trajectory.json` (sha256 cb1259b5b2fd, 1,801,435 bytes; Downloads `trajectory-run-1 (1).json`). It is also copied to `06_PreCheck_Trajectory/trajectory.json`; the rev3 run is kept in `rev3/precheck/`.
  - Two independent causes:
    - F1: the run missed the Meta VO campaign (#prototype reply 6908b2f1). It reported $450 a month and $150 each, and had Arthur paid back $98.
    - F2: it set ENG-2462 to Done. It never opened the Apple App Review email.
  - Narrow miss: NO. Failure-pattern risk: YES. T1 (VO) decides about 33 % of the answer, and T1–T4 all feed the total, shares and reply rows.
  - Tool calls: 157, confirmed locally by counting tool_use blocks. 111 of them are the per-issue triple (37 list_comments, 37 create_comment, 37 update_issue).

Carry forward to /create-humantime, /create-oe-writing, /create-rubric-writing and /create-difficulty:

1. Expect the six base Todo issues with the assignees above, Done for Metabase, dbt and GitHub, and the new "Meta VO campaign" issue (Todo, Leonard) with its own comment.
2. CF AWS is $62, not ENG-2445's $95.
3. Per-person cost is $1,150 each. Arthur's $248 counts toward his third, so he adds $902 cash. $902 is his cash, not his cost.
4. Accept DD player support's By "before Feb 28" as written (the Helpshift deadline).
5. Don't grade:
   - Robert's exact wording, the sheet's row order or exact branch names (NB-13);
   - Snowflake AWS totals (NB-2), or NB-5/8/9/17/19.
6. Per the /hardness advice, the rubric must check each trap on its own item row, so runs split by item instead of failing the same total, share and reply rows:
   - the VO row and the VO issue;
   - ENG-2445's $62;
   - the playable vendor's exclusion;
   - DD's row;
   - ENG-2462's state.
7. The requester wants over 130 calls in every run. This run reached 157 only through the 37 per-issue comment reads. A run that skips them lands at about 120, so watch the per-run minimum in the baseline. A run that finds the VO adds a linear_create_issue and a comment.
8. Not acted on:
   - A-3 (realism: Arthur's $140 reply under the Feb 2 root; it is the CORR trap's placement).
   - The schema-snapshot columns (links_json and the gslides notes/table_json/ordinal), which loaded fine before.
   - The optional "Then" wording note.

   Changing any of them would mean re-running /injection, /prompt, /hardness, /oe and /rubric.

## /oe — PASS 5 (2026-11-06)
- Verdict saved here as `2_oe_PASS_r4.md` (sha256 ead6b8ca7e52):
  - Completeness 5, Accuracy 5;
  - Path feasibility SUPPORTED, Task solvability SUPPORTED_BY_OE;
  - Issues found: none; deep recheck O1–O3 confirmed 0;
  - Prompt follow-up: NONE.
- Bound to:
  - OE sha e210cd02c49e (copy: `08_Oracle_Events_oe_PASS.md`; identical to task_inputs/08_Oracle_Events.md);
  - prompt ccd229a59a17;
  - SQL f1a290ced176.
  Do not edit 08_Oracle_Events.md from here on: any edit stales this PASS and the rubric review that cites the OE labels.
- Carry into the rubric (optional notes 1–2 and O3's settled forks):
  1. Sheet location: require only "in Robert's Drive", not the top level; a subfolder of his Drive still passes. Leave OE 100's wording as it is.
  2. Revenue table: accept REVENUE_DAILY or REVENUE_DAILY_V2 (same January sums: 183.11 / 0.00 / 7.36).
  3. Settled forks to grade as settled:
     - ENG-2438 assignee Robert;
     - total revenue, not IAP only;
     - analytics pipeline stays with HG;
     - DD support before Feb 28;
     - playable vendor stays with HG.
  4. Accepted variants:
     - Metabase and dbt on one row or two;
     - an HG row's Paid by blank or HG;
     - the layer.ai art step on the layer.ai or the Combo Fighter row;
     - any share role.
