# Human Time Worksheet — dg-beta-server-signoff

Pass: first        Tier: Long-Horizon
Hours: 12.75

Built 2026-10-27 from 04_Prompt.txt (sha256 a0414d89216a), 00_Assigments.md, 01_Grounding_Dossier.md, 01_Hardness_Manifest.json,
04_Prompt_Writing_Brief.md, 03_Error_Async_Config.txt (Friction: none). Manual effort only: Douglas scrolls Slack, opens tickets and PRs one
by one and compares times by hand. Volumes are from Douglas's view (scoped services filtered to his DMs, channels, mailbox and calendar).

| Sub-task | Kind (read / dead end / workaround / re-read / write) | Volume (measured, persona view) | Rate | Minutes |
|---|---|---|---|---|
| Read Arthur's ask in the DM and the September context around it | read | DM D05QQF7V404: 27 messages in Sep 2025 (+2 seeded: the ask and Douglas's Sep 22 claim) | skim ≈ 3,000/h + careful read of the ask | 10 |
| Find the sign-off rules: the server card and its comment | read | 2 cards in the BETA: Oct 10 list (trello:68dabfe9bc2e8b969782e22d) + 1 comment | ≈ 7 min per card read in full | 15 |
| Read the prod deploys doc | read | 1 doc, 7 paragraphs (f_470ae81236d5bd39045dc1) | careful read of a rule doc | 10 |
| Find Leonard's request in the inbox and read his thread to the end (Arthur's two-point reply-all under it) | read | 69 threads last touched in Sep 2025 (persona_view reach, douglas mailbox) | triage ≈ 450/h + 2 reads, the second with two points to apply | 18 |
| Find the folder name on the ZM beta page and read its comments | read | 1 Confluence page (page_zm_beta_oct10) + 2 comments (QA question, Arthur's reply) | short page + 2 short comments | 6 |
| Find the freeze on the calendar | read | 12 events in Sep 2025 on Douglas's calendar (persona_view reach) + the freeze copy evt_0f489eb7fb46ada9660881 | list scan | 5 |
| Read the deploy log (cut row, imports) | read | 2 tabs, 8 + 10 rows (f_78bedc46245090a160d2dd) | dense sheet | 12 |
| Skim #zombie-match3d for server status and read the #50 thread past its parent | read | C0880U9751A: 473 base messages in Sep 2025 + 7 seeded; thread C0880U9751A/1758937233.118904 | ≈ 3,000/h (10 min) + one decisive thread ≈ 20 min | 30 |
| List ZOM tickets closed Aug–Sep and cut to the window after the prod cut | read | 110 ZOM tickets Done Aug–Sep 2025 → 73 after 2025-08-25 11:52 UTC (cohort.json) | triage ≈ 450/h | 15 |
| Read the comments on every candidate ticket to find the backend changes | read | 73 tickets, 73 comment threads (16 with a backend change) | ≈ 3 min per ticket (classify a note ≈ 2 min + open/close) | 219 |
| Check each backend PR: deploy notes, rollbacks, reviews, inline review comments and their times against the freeze | read | 15 PRs, harmonygames-Games/match3d-backend#38 … #54 (comments + reviews + inline review comments; Arthur's on #46) | ≈ 11 min per record across 3 surfaces (V1 8–15 min) | 165 |
| Dead ends: QA's "all on prod" summary, Douglas's own Sep 22 claim, the Monday freeze message, the client card and client-QA folder, the old Domino Delights page, the stale Prod deploys tab, Vincent's Sep 30 "works" in a 267-message DM | dead end | 7 traps (01_Hardness_Manifest.json traps T2, T4, T6, T7, T19, T22, T10); D079SNE2TL4 267 messages in Sep 2025 | ≈ 5–6 min per trap + DM skim ≈ 3,000/h | 45 |
| Re-check PRs once the approval, freeze and import rules are understood | re-read | 9 PRs whose answer turns on review timing, freeze, rollback or an import note (#38, #39, #41, #43, #44, #47, #50, #52, #54) | ≈ 4 min each | 36 |
| Write the register (17 rows: ticket, server change, on prod) | write | 1 sheet, 17 rows × 3 columns | ≈ 3 min per row + setup | 58 |
| Move the register into the beta sign-off folder and share it with Leonard (commenter) | write | 1 move + 1 share (d_69fcebc484d472907b0b5c; leonard.hayes@harmonygames.co) | ≈ 2–3 min each | 5 |
| Reply to Arthur in the DM with the count and the tickets not on prod | write | 1 message (2 on prod, 15 keys) | ≈ 10 min tailored message + 1 min for the longer list | 11 |
| Move each not-on-prod ticket back to Todo with a comment naming what still has to go out | write | 15 tickets × (1 state change + 1 comment) | ≈ 7 min per ticket (V1 5–10 min per write) | 105 |
| Total | | | | 765 = 12.75 h |

Tier check: in band — Long-Horizon review triggers are below 5 h or above 120 h; 12.75 h sits next to the 10 h Long-Horizon worked example and
the V1 10.5 h Long worksheet. No trigger, no re-measurement needed.
Condensed breakdown length: 980 characters (field accepts 50–2,000), one short line per grouped sub-task (what, volume, minutes) plus the total.
Sources measured: `persona_view.py reach douglas` (mailbox Sep 2025 threads 69; calendar Sep 2025 events 12); `persona_view.py search douglas slack "prod"` (1,589 visible hits, scope check); exports read through hg.py's sources: slack messages C0880U9751A / D05QQF7V404 / D079SNE2TL4 for Sep 2025 (473 / 27 / 267), linear issues ZOM Done Aug–Sep 2025 (110), cohort.json (73), the SQL rows for the 15 PRs, 2 cards, doc, log and page.

## Self-review

Walked `10_Long Horizon Guidelines - V2.md` §5 (sub-tasks, dead ends, workarounds, re-reading) and §10, the Pre-QC "Difficulty and submission"
list ("justified sub-task by sub-task and the arithmetic adds up") and the field text (50–2,000 characters, typed by hand, forced-error workaround
time). Result per check: sub-tasks present with volumes; dead-end and re-read lines present; no forced error (03_Error_Async_Config.txt
Friction: none), so no workaround line; writes counted per write; 765 min = 12.75 h on a 0.25 step; 980 characters.

| Counter-reading | Resolution (evidence) |
|---|---|
| Counter (inflated): 219 min for ticket comments is a lot | 73 comment threads must each be opened and read (16 of 73 hold a backend change, unpredictable — 01_Hardness_Manifest.json cohort); 3 min each sits inside the V1 "classify a reply ≈ 2 min" plus opening the ticket |
| Counter (inflated): 11 min per PR | each PR needs its deploy notes, its reviews and its inline review comments (Arthur's on #46 adds ZOM-537's import) compared by time against the freeze (harmonygames-Games/match3d-backend#50: Douglas APPROVED Sep 19, Arthur COMMENTED Sep 29, prod Sep 27); the V1 anchor for 2–3 surfaces is 8–15 min, and 3 surfaces sit at its upper half |
| Counter (solution-path estimate): written as if the person knew where the rules and the folder were | discovery lines cover finding the card from the DM, the doc from the card, the freeze from the doc, the folder from the beta page; the seven traps get a dead-end line (manifest T2, T4, T6, T7, T19, T22, T10) |
| Counter (evaluator-wide volume): Slack counts from channels Douglas can't see | every Slack count is from channels Douglas is in (C0880U9751A, D05QQF7V404, D079SNE2TL4 — dossier §1.E check-sql PASS); mailbox and calendar counts come from `persona_view.py reach douglas` |
| Counter (tier mismatch): Long-Horizon at 12.75 h might be thin for 130–150 calls | 12.75 h is in band (5–120 h) and next to the 10 h Long worked example; the call count is measured at the Opus pre-check, not tuned here (01_Hardness_Manifest.json call_budget: 175) |
| Counter (linter reading): from the prompt alone, 12.0 h for "a register and a reply" looks 3× high | the reasoning names the volumes (73 tickets, 15 PRs, 480 channel messages, 10 ticket moves), which 01_Universe_Inject.sql shows (404 rows over 10 services); a reviewer reading the SQL sees the 73 comment threads and 18 PRs |

Re-verified this run: Slack September counts from the base message files (473 / 27 / 267), the 110 ZOM Done Aug–Sep issues and the 73-ticket
window from the Linear export, the PR set and writes from the SQL and dossier §9.2. Sum recomputed: 10 + 15 + 10 + 18 + 6 + 5 + 12 + 30 + 15 +
219 + 165 + 45 + 36 + 58 + 5 + 11 + 105 = 765. Refreshed 2026-10-27 after hardening round 1 (01a_Hardening_Report.md §11):
the ZM beta page's two comments and two more Todo moves (ZOM-487, ZOM-537) are the new volume. Refreshed again after hardening round 2 (01a_Hardening_Report.md §11): Arthur's Slack thread reply is gone (DM line +2 seeded instead of +3) and each PR gets its inline review comments read (harmonygames-Games/match3d-backend#46#rc_1 carries ZOM-537's import), 10 → 11 min per PR, +15 min. Refreshed again after hardening round 3 (01a_Hardening_Report.md §11): 17 register rows and 15 Todo moves (+5 tickets: ZOM-444, ZOM-531, ZOM-459, ZOM-509, ZOM-436), a two-point reply-all, four more log rows and two more PRs to re-check: +45 min.

Unresolved: none. The human types the reasoning on Screen 25 in their own words (pasting and copying are blocked).

```
STAGE GATE humantime: PASS — Task_Authoring-2/task_inputs · 05_Human_Time_Worksheet.md#98d556714734 · blocking 0 · warnings 0 · checks 15
[PASS] structure.outputs: 1 output(s) present: 05_Human_Time_Worksheet.md
[PASS] structure.inputs: 2 input(s) present: 04_Prompt.txt, 00_Assigments.md
[PASS] structure.fresh: every output newer than its inputs (04_Prompt.txt, 00_Assigments.md, 08_Oracle_Events.md, 07_Baseline_Trajectories)
[PASS] chain.prompt-check: upstream 'prompt-check' PASS pasted and current (04_Prompt_Check.md#9b99574feb95, 04_Prompt.txt#f5f6a459f6df)
[PASS] structure.placeholders: no placeholders in 05_Human_Time_Worksheet.md
[PASS] structure.arithmetic: 17 sub-tasks sum to 765 min = 12.75 h
[PASS] evidence.volumes: every sub-task has a measured volume
[PASS] structure.kinds: dead-end / workaround / write lines present
[PASS] structure.field_length: condensed breakdown 980 characters
[PASS] evidence.sources: volume sources name the hg.py / persona_view queries
[PASS] structure.tier_check: tier check line present
[PASS] review.counter_readings: 6 evidenced counter-readings (of 6 found; need ≥ 5) in 05_Human_Time_Worksheet.md
[PASS] review.coverage: self-review addresses all 5 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```







