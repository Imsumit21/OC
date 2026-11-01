# Human Time Worksheet — rb-winddown-closeout

Pass: first        Tier: Long-Horizon
Hours: 19.75

Built 2026-10-28 from 04_Prompt.txt (sha256 cfab17798d35), 00_Assigments.md, 01_Grounding_Dossier.md, 01_Hardness_Manifest.json,
04_Prompt_Writing_Brief.md, 03_Error_Async_Config.txt (Friction: none), against 01_Universe_Inject.sql sha256 50f6a195de7e (/injection PASS,
/prompt NON-FAIL). Manual effort only: Robert scrolls #winddown, opens each Linear issue and its comments, finds the billing mail in his own
mailbox, reads the costs tab and the ledger, converts annual and quarterly charges and adds the totals by hand. Volumes are from Robert's view
(scoped services filtered to his channels, mailbox, calendar and the files shared with him).

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read Leonard's ask and the February #winddown history: the keep-list thread and Arthur's Gusto reply, Leonard's subscriptions table, Arthur's LLC card moves, the Slack and Google decisions | read | C0ADGSZKR3R: 206 base messages in Feb 2026 + 3 seeded (the ask, the Gusto reply, Arthur's note) | skim ≈ 3,000/h (4 min) + ask 10 + one decisive thread past its parent 20 + table 10 + decisions 11 | 55 |
| Read the conventions doc | read | 1 doc, 10 rules (f_1326e66bcabfda8fd29e4a) | careful read of a rule doc | 15 |
| Open the Linear project, read its description and list its issues | read | 1 project "Shutdown – accounts", 45 issues (ENG-2438…ENG-2483, no ENG-2459) | short description + issue list | 10 |
| Find Sunset's checklist and its in-thread correction, and pass over the Sherwood checklist | read | robert mailbox: 250 threads last touched in Feb 2026 (persona_view reach robert) + 2 thread reads | triage ≈ 450/h (33) + 2 reads (12) | 45 |
| Find SVB's card terms on the founders' board | read | board 640643a3fd8f3ca308d9318e: 177 open cards (449 total); 9 "SVB card" hits + the seeded card | title scan + 2 card reads | 10 |
| Find the review call on the calendar | read | 4 events in Feb 2026 on Robert's calendar (persona_view reach robert) + the seeded Mar 12 review copy | list scan | 5 |
| Read the HG Costs tab, split the shared Sound and UA lines, match lines to issues | read | f_605121f4a36752645e0ac3 "HG Costs": 75 rows, 62 labelled lines, against 45 issues | dense sheet ≈ 30 min | 30 |
| Pull the January and February finance-ledger lines | read | FINANCE_LEDGER FIN-000686…FIN-000704: 19 rows | query + read | 15 |
| Decide each account that stays on the register: read the issue's comments, apply rules 4–8, check the mail or Slack it points to | read | 25 issues on the register (39 seeded comments across the 45 issues) | ≈ 10 min per record across 2–3 surfaces (V1 8–15 min) | 250 |
| Decide each issue that leaves the register (rule 1 duplicate, rule 2 exclusions) | read | 20 issues (19 left out + ENG-2461 duplicate) | ≈ 4 min each: comment + rule 2 + costs history | 80 |
| Add the accounts the project misses (rule 3): the Sound line's ElevenLabs, the ledger's Meta and AppLovin | read | 3 accounts (Sound line; FIN-000688/689 Jan, 699/700 Feb) | ≈ 10 min per record | 30 |
| Find each vendor's billing mail in the mailbox | read | 8 vendors (Figma, Layer, Pond5, Soundly, Workspace, ElevenLabs, Singular, iPostal) in 16,233 threads | ≈ 6 min each: find by sender, open, read the date and amount | 48 |
| Read Singular's billing thread to the end (quarterly invoice vs the past-due extension) | read | 1 thread + 2 dunning mails | one decisive thread ≈ 20 min | 20 |
| Side reads: Leonard's Layer note in #prototype, the Typecast cancel and Trello downgrade in #admin_foundersonly, CodeRabbit's notice on Combo-Fighters#38 | read | C09UHHN6PFZ 727 msgs Feb 2026; C04UEQVDVB7 88 (Jul 2025) + 64 (Nov 2025); 1 PR comment | skim ≈ 3,000/h (18) + 3 reads (12) | 30 |
| Dead ends: the keep list before the Gusto reply, the Slack free plan and Google archive plans, Metabase on the first checklist, the uncorrected checklist, Arthur's issue list as complete, one Sound row, no UA account, the 2023 SVB card move, Sherwood, the Growth/UA page, Intuit as a second row, "cancelled" in Slack read as Closed, Hold rows undated, Helpshift's pending export, annual prices as monthly, never-paid accounts kept, Docusign's assignee, iPostal on the tab, Arthur's old sheet, Cursor for Oliver, Singular's Mar 15, Helpshift's $1,500 balance, AWS ~$1,550, the tab's December figures | dead end | 25 traps (01_Hardness_Manifest.json traps T1–T25) | ≈ 4 min per trap | 100 |
| Re-read rows a later record overturns: Sunset's correction (Trello, Metabase, dbt, BigQuery), the Gusto reply, the SVB card moves, the clashes | re-read | ≈ 10 rows | ≈ 4 min each | 40 |
| Convert annual and quarterly charges to a month and add the two totals by hand | read | 28 rows, 2 totals (Figma 1,212/12, Carta 3,852/12, Linear 1,832.65/12, Docusign 300/12, ElevenLabs 50/12, Singular 6,250/3) | ≈ 20 min | 20 |
| Write the register: account, action, status, by when, owner, monthly cost, then the two totals | write | 1 sheet, 28 rows × 6 columns + 2 totals | ≈ 3 min per row + 6 min setup | 90 |
| Share the register with Leonard and Arthur as editors | write | 2 shares (leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co) | ≈ 2–3 min each | 5 |
| Comment on every issue with what happens and by when | write | 45 comments | ≈ 5 min per tailored comment (V1 5–10 min) | 225 |
| Settle each issue's state | write | 25 state changes (5 Done, 20 Canceled) | ≈ 1 min each | 25 |
| Raise an issue for each account the project lacks | write | 3 new issues (ElevenLabs, Meta Ads, AppLovin (UA)) | ≈ 7 min each | 21 |
| Reply in Leonard's thread with the two totals and the clashes | write | 1 message (2 totals, the Slack and Google clashes) | ≈ 16 min tailored message | 16 |
| Total | | | | 1185 = 19.75 h |

Tier check: in band — Long-Horizon review triggers are below 5 h or above 120 h; 19.75 h sits above the 10 h Long-Horizon worked example and
under the V1 24 h Long example (~338 calls). No trigger, no re-measurement needed.
Condensed breakdown length: 1075 characters (field accepts 50–2,000), one short line per grouped sub-task (what, volume, minutes) plus the total.
Sources measured: `persona_view.py reach robert` (mailbox 16,233 threads, 250 last touched Feb 2026; calendar Feb 2026 events 4; 224 visible Slack
channels); `persona_view.py search robert gmail "checklist"` (50 visible hits); `persona_view.py search robert trello "SVB card"` (9 hits);
exports read through hg.py's sources: slack messages C0ADGSZKR3R 2026-02 (206), C09UHHN6PFZ 2026-02 (727), C04UEQVDVB7 2025-07 (88) and 2025-11
(64); trello data.json board 640643a3fd8f3ca308d9318e (449 cards, 177 open); gsheets data.json f_605121f4a36752645e0ac3 HG Costs (75 rows, 62
labelled); snowflake FINANCE_LEDGER FIN-000686…FIN-000704 (19 rows); 01_Universe_Inject.sql (45 linear_issues, 39 linear_comments, 3
slack_messages); truth.json (28 rows, 5 Done, 20 Canceled, 3 new issues).

## Self-review

Walked `10_Long Horizon Guidelines - V2.md` §5 (sub-tasks, dead ends, workarounds, re-reading) and §10, the Pre-QC "Difficulty and submission"
list ("justified sub-task by sub-task and the arithmetic adds up") and the field text (50–2,000 characters, typed by hand, forced-error workaround
time). Result per check: sub-tasks present with measured volumes; dead-end and re-read lines present; no forced error (03_Error_Async_Config.txt
Friction: none), so no workaround line; writes counted per write (45 comments, 25 state changes, 3 issues, 2 shares, 1 sheet, 1 reply); 1185 min =
19.75 h on a 0.25 step; 1075 characters.

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 250 min for the register accounts is a lot | each of the 25 accounts needs its issue comments plus the rule that applies and the record it points to (e.g. ENG-2454 Singular: comment + robert@harmonygames.co/1850283027022457279 + rule 6; ENG-2464 Workspace: comment + Sunset's list + SVB card); 10 min sits inside the V1 8–15 min anchor for a record across 2–3 surfaces |
| Counter (inflated): 225 min for 45 Linear comments | the project rule asks for "a comment on each with what happens and by when" (L_PROJECT description in 01_Universe_Inject.sql), so each is tailored; 5 min is the low end of the V1 5–10 min per write anchor |
| Counter (solution-path estimate): written as if Robert knew where the rules were | discovery lines cover finding Sunset's mail among 250 February threads, the SVB card among 177 open cards, the review call on the calendar, the costs tab and the ledger the doc points to; every manifest trap (T1–T25) has a dead-end share |
| Counter (evaluator-wide volume): Slack and mail counts include channels or mailboxes Robert can't see | every Slack count is from channels Robert is in (C0ADGSZKR3R, C09UHHN6PFZ, C04UEQVDVB7 — dossier §1.E check-sql PASS); mailbox and calendar counts come from `persona_view.py reach robert` |
| Counter (tier mismatch): 19.75 h could look high for a register task | Long-Horizon triggers are < 5 h or > 120 h; the call budget is 157 (01_Hardness_Manifest.json call_budget), near the V1 Long examples; the hours follow the 45-issue cohort and 70 Linear writes, not the tier |
| Counter (linter reading): from the prompt alone, "build a register, settle the issues, reply" looks like 4–6 h | the reasoning names the volumes the SQL shows (45 issues with 39 comments, 25 state changes, 45 comments, a 28-row register, 8 vendors' billing mail, 25 traps); 19.75 h is within 3× of a 7–10 h reading even before the dead ends |

Re-verified this run: #winddown Feb 2026 (206), #prototype Feb 2026 (727), #admin_foundersonly Jul/Nov 2025 (88/64) from the base message files;
the founders' board (449 cards, 177 open) from trello data.json; HG Costs (75 rows) from gsheets data.json; Robert's reach from persona_view;
the 45 issues, 39 comments and 3 Slack inserts from 01_Universe_Inject.sql; the writes from truth.json. Sum recomputed: 55 + 15 + 10 + 45 + 10 + 5
+ 30 + 15 + 250 + 80 + 30 + 48 + 20 + 30 + 100 + 40 + 20 + 90 + 5 + 225 + 25 + 21 + 16 = 1185.

Unresolved: none. The human types the reasoning on Screen 25 in their own words (pasting and copying are blocked).

```
STAGE GATE humantime: PASS — Task_Authoring-2/task_inputs · 05_Human_Time_Worksheet.md#5f8dc6bec5e9 · blocking 0 · warnings 0 · checks 15
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#46ca188fe4cd, 04_Prompt.txt#4c4f0951f3c1)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 23 sub-tasks sum to 1185 min = 19.75 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 1075 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 5 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
