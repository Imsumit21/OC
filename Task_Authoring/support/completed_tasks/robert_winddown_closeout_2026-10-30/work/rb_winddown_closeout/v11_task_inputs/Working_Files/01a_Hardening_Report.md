# 01a Hardening Report — rb-winddown-closeout
MODE B (baseline trajectories present; verifier results and difficulty stats not yet produced) · plan only, no SQL changed in this revision · 2026-10-29

## 1 · Mode, inputs, run validity
Inputs read: `00_Assigments.md`, `01_Universe_Inject.sql` (sha 50f6a195de7e, /injection PASS r9), `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json` (25 traps), `04_Prompt.txt` (/prompt NON-FAIL r5), `08_Oracle_Events.md` (/oe PASS r3), `06_PreCheck_Trajectory/trajectory.json`, `07_Baseline_Trajectories/` (6 files).
Inputs missing: `10_Baseline_Verifier_Results.md` (empty) and `12_Difficulty_Stats.txt` (absent) — the platform verifier has not been run. Every pass rate below is therefore a **projection from a modelled rubric**, not a number of record; gate 6 numbers come from `12` once it exists.

| Rollout file | Model (main / subagents) | Calls | Completed export | Compaction / truncation | Injection re-applied | Final write |
|---|---|---|---|---|---|---|
| trajectory-run-1 (1).json → run-1 | claude-opus-5-5 / none | 215 | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-1 · call 16) | slack_send_message, run-1 · call 215 |
| trajectory-run-2.json → run-2 | claude-opus-5-5 / none | 230 | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-2 · call 14) | slack_send_message, run-2 · call 230 |
| trajectory-run-3.json → run-3 | claude-opus-5-5 / none | 210 | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-3 · call 13) | slack_send_message, run-3 · call 210 |
| trajectory-run-4.json → run-4 | claude-opus-5-5 / none | 208 | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-4 · call 16) | slack_send_message, run-4 · call 208 |
| trajectory-run-5.json → run-5 | claude-opus-5-5 / none | 215 | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-5 · call 15) | slack_send_message, run-5 · call 215 |
| trajectory-run-6.json → run-6 | claude-opus-5-5 / none | 205 | yes (result event present) | none seen; large reads spilled to files and were re-read with Bash | yes — seeded ask, keep-list thread, conventions doc and Sunset thread returned (run-6 · call 14) | slack_send_message, run-6 · call 205 |

File mapping is by content (each run's own sheet id and reply); verifier `Run #N` mapping is pending until `10` exists. No errored runs.

## 2 · Gate status (projected) beside the clean average
`12_Difficulty_Stats.txt` does not exist, so there is no number of record. The projection scores each rollout against a per-write rubric model shaped the way `/rubric` demanded on the Douglas task (one row per write target: 25 state rows, 45 comment rows; register action, status and by-when per account; totals in the sheet and the reply; weights 1/3/5 by kind of work). Model: `support/task_work/rb_winddown_closeout/hardening/proj.py`.

```
rows 179 weight 553
current data                       avg  95.1%  sd 0.024  runs 96.7 94.6 97.3 95.3 90.2 96.7
```
| Gate (GEN_EXECUTION §3) | Threshold | Projected on current data | Status |
|---|---|---|---|
| Average weighted score | < 75% (Evals) · < 90% (QC) · author < 80% | 95.1% | FAIL all three |
| Per-rollout SD | 0.1–0.3 | 0.024 | FAIL |
| pass@1 | ≤ 3 of 6 | 0 of 6 at a 100% bar (every run misses CodeRabbit) | PASS |
| Failure patterns | ≥ 2, largest ≤ 50% | runs 3 vs 2/4/5 differ on ≥ 2 rows; largest pattern (CodeRabbit-only) ≈ 1 run | PASS (weak) |
| Errored runs | ≤ 2 | 0 | PASS |
| Horizon (calls) | > 150 (author) | 205–230 | PASS |

Clean average: no CONFOUNDED criterion is counted in the model (the Helpshift third clash is scored as a failure only of the clash-scope row; see §7), so clean = raw = 95.1%. **Mechanism weight share:** rows whose result depends on a LANDED node = 12 of 553 weight (2.2%), far below the ~30% that Hardness_Mastery §11 (NF2) gives as the floor for an average under 75%.

## 3 · Predicted /hardness band (run closest to the median: run-4)
| Requirement (prompt / incorporated) | Result | Evidence |
|---|---|---|
| Register: 28 accounts, actions, by-when, owner, cost | MINOR_GAP (adjoe added; CodeRabbit status/by-when wrong) | run-4 · call 131 |
| Shared with Leonard and Arthur as editors | MET | run-4 · call 133–134 |
| Settle each Linear issue + a line on each | MATERIAL_FAIL on one issue (ENG-2474 left open, comment says Requested) | run-4 · call 150 |
| Reply with two totals and the clashes | MET totals; extra Helpshift clash (contested, §7) | run-4 · call 208 |

Band **3** (one consequential failure — the CodeRabbit chain, a single root cause repeated in the register, the state and the comment — with a bounded correction). Not 4: there is no second independent material failure; adjoe is a minor extra row whose cost leaves both totals unchanged. Not 2: the ENG-2474 state and the register status are wrong writes, not wording. This matches /hardness r1 NON-FAIL.

## 4 · Designed-difficulty register
Counts are out of 6 completed rollouts. Each citation is the first call in that run that returned the resolving record (keyword match in the tool result; `hardening/cite.py`), or the write that shows the outcome.

| T | Wrong reading designed | Verdict | LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED | Evidence (run · call) |
|---|---|---|---|---|
| T1 | keeps Gusto through the shutdown (Leonard's keep list) with a Feb 19 card move | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 6, run-2 · call 6, run-3 · call 6, run-4 · call 6, run-5 · call 5, run-6 · call 6 |
| T2 | plans the Slack downgrade to free (agreed Feb 11) without flagging it | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 25, run-2 · call 17, run-3 · call 24, run-4 · call 27, run-5 · call 69, run-6 · call 21 |
| T3 | puts Google Workspace down for archiving after Feb 15 (Leonard's action item) | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 25, run-2 · call 17, run-3 · call 24, run-4 · call 27, run-5 · call 69, run-6 · call 21 |
| T4 | holds Metabase for Sunset (first checklist) or leaves its card move open | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 22, run-2 · call 18, run-3 · call 22, run-4 · call 25, run-5 · call 67, run-6 · call 19 |
| T5 | stops at the first checklist: cancels Trello (paid plan ended Nov 2025), dbt and BigQuery | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 22, run-2 · call 18, run-3 · call 22, run-4 · call 25, run-5 · call 67, run-6 · call 19 |
| T6 | treats Arthur's 40 issues as the complete account list | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 88, run-2 · call 49, run-3 · call 41, run-4 · call 26, run-5 · call 105, run-6 · call 22 |
| T7 | one Sound row (or Soundly at $15) because the tab has one line | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 88, run-2 · call 49, run-3 · call 41, run-4 · call 26, run-5 · call 105, run-6 · call 22 |
| T8 | no UA account on the register (no issue for it, Frederick left in October) | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 29, run-2 · call 27, run-3 · call 35, run-4 · call 32, run-5 · call 74, run-6 · call 25 |
| T9 | no card deadline (Slack never dates the closure) or the 2023 move onto the SVB card read as current | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 118, run-2 · call 129, run-3 · call 121, run-4 · call 11, run-5 · call 98, run-6 · call 10 |
| T10 | applies Sherwood's 'cancel every subscription now except payroll and accounting' | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 5, run-2 · call 5, run-3 · call 5, run-4 · call 5, run-5 · call 4, run-6 · call 5 |
| T11 | costs Meta Ads at trailing 30-day spend or treats it closed once spend reads $0 | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 16, run-2 · call 14, run-3 · call 13, run-4 · call 16, run-5 · call 15, run-6 · call 14 |
| T12 | two rows (QuickBooks and Intuit) or Canceled on the older issue | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 57, run-2 · call 70, run-3 · call 65, run-4 · call 60, run-5 · call 39, run-6 · call 48 |
| T13 | Closed for CodeRabbit and Cursor because Arthur said they're cancelled (and Done in Linear) | LANDED | 6 · 0 · 0 · 0 · 0 | wrote Requested and left ENG-2474 open: run-1 · call 198, run-2 · call 228, run-3 · call 194, run-4 · call 150, run-5 · call 211, run-6 · call 182; resolving record read at run-1 · call 70, run-2 · call 82, run-3 · call 77, run-4 · call 73, run-5 · call 52, run-6 · call 60 |
| T14 | Hold rows with no date, Feb 15, or 'until Sunset confirms' | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 27, run-2 · call 20, run-3 · call 25, run-4 · call 31, run-5 · call 71, run-6 · call 23 |
| T15 | Helpshift deadline Feb 27 (export still pending) or no export check at all | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 17, run-2 · call 24, run-3 · call 14, run-4 · call 17, run-5 · call 14, run-6 · call 15 |
| T16 | Singular at 6,250 or 0, Figma at 0 or 1,212, Carta/Docusign/Linear at their annual price | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 9, run-2 · call 9, run-3 · call 10, run-4 · call 9, run-5 · call 9, run-6 · call 8 |
| T17 | keeps never-paid, one-off or pre-Feb-9 accounts, or drops Trello for its Nov 2025 downgrade | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 16, run-2 · call 14, run-3 · call 13, run-4 · call 16, run-5 · call 15, run-6 · call 14 |
| T18 | Leonard as Docusign's owner (the assignee) | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 11, run-2 · call 11, run-3 · call 11, run-4 · call 14, run-5 · call 10, run-6 · call 11 |
| T19 | iPostal as a Cancel row at $34.79 (Dec-25 on the tab) | LANDED | 1 · 0 · 5 · 0 · 0 | run-5 kept iPostal as a row: run-5 · call 139; ENG-2466 not Canceled (run-5 · call 208); resolving record read at run-1 · call 11, run-2 · call 11, run-3 · call 11, run-4 · call 14, run-5 · call 10, run-6 · call 11 |
| T20 | uses Arthur's 18-row 'Subscriptions' sheet (rounded figures) as the list | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 9, run-2 · call 9, run-3 · call 10, run-4 · call 9, run-5 · call 9, run-6 · call 8 |
| T21 | keeps Cursor for Oliver | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 5, run-2 · call 5, run-3 · call 5, run-4 · call 5, run-5 · call 4, run-6 · call 5 |
| T22 | Singular deadline Mar 14 (the past-due extension to Mar 15) | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 51, run-2 · call 72, run-3 · call 67, run-4 · call 54, run-5 · call 33, run-6 · call 50 |
| T23 | Helpshift at $1,500 / $300 (balances owed) instead of its monthly 150 | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 36, run-2 · call 74, run-3 · call 69, run-4 · call 39, run-5 · call 18, run-6 · call 52 |
| T24 | AWS at ~$1,550 (page) or ~$1k (Arthur's DD prod estimate) or 0 (tab) | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 87, run-2 · call 50, run-3 · call 40, run-4 · call 34, run-5 · call 106, run-6 · call 28 |
| T25 | costs read off the costs tab's December figures (Unity 2,172, Workspace 316.56, Slack 129.50, BigQuery 14.33, GitHub 86) | LEAKED | 0 · 0 · 6 · 0 · 0 | resolving record returned and applied: run-1 · call 35, run-2 · call 59, run-3 · call 54, run-4 · call 38, run-5 · call 17, run-6 · call 37 |
| E1 (emergent) | adjoe added from the UA line (stopped June 2025, rule 2) | LANDED | 1 · 0 · 5 · 0 · 0 | run-4 · call 105 (AD_SPEND_DAILY adjoe last 2025-06) then run-4 · call 131 sheet row |
| E2 (emergent) | Helpshift "no export" listed as a third clash | CONFOUNDED (fairness: contested reading) | 0 · 3 · 3 · 0 · 0 | run-1 · call 215, run-4 · call 208, run-6 · call 205 |
| E3 (emergent) | ElevenLabs by-when Jul 7 (prepaid to Jul 9 → Jul 8) | LANDED (minor) | 1 · 0 · 5 · 0 · 0 | run-2 · call 154 |

Verdict totals: LANDED 2 designed (T13 6/6, T19 1/6) + 2 emergent · LEAKED 23 · CONFOUNDED 1 emergent · BYPASSED 0 · NOT-REACHED 0.

## 5 · Per-rollout ledgers
Full call-by-call ledgers (every input and the first 300 characters of every result) were built with `hardening/ledger.py` and read before any verdict. Shape shared by all six runs:

| Phase | Calls (typical) | What came back | Decision |
|---|---|---|---|
| #winddown read + the one reply thread + keep-list thread | 1–7 | ask, keep list, Gusto reply, card moves, Feb 11 Slack plan, Leonard's action items | builds the keep/move/clash inputs |
| Linear project + 45 issues; Drive conventions doc + Wind Down folder | 8–17 | project rule, 45 issues (with `links`), rules 1–10 | applies the doc as a recipe |
| Gmail Sunset/SVB, calendar, card-terms hunt (Gmail, Drive, Slack, Confluence) then Trello | 18–130 | Sunset thread + correction, review call Mar 12, SVB card | 20–40 calls spent hunting the card terms before Trello |
| P&L sheets, Snowflake ledger + AD_SPEND_DAILY | ~40–110 | costs tab, Jan/Feb ledger lines | adds Meta, AppLovin, ElevenLabs |
| 45 × linear_list_comments | ~35–80 | every owner figure, date and status statement | register values copied from comments |
| vendor Gmail sweeps (OR-queries of every vendor name) | ~90–130 | receipts, Lucidchart/Google Ads notices, iPostal, Figma, Layer | statuses and prepaid periods |
| writes: sheet, 2 shares, 25 states, 45 comments, reply | last ~80 | — | — |

Never called by any run: any `github_*` tool, `trello_get_comments` / `trello_get_card_actions`, `linear_get_attachments`, `confluence_list_comments`. Slack outside #winddown was reached only by keyword search (run-1: SVB, card, terms, statement, bank, cancel*, coderabbit, subscription; run-6: cancel*, coderabbit, cursor, subscription; runs 2–5: SVB/card/statement, coderabbit, adjoe, elevenlabs, pond5, ipostal, meta ads).

## 6 · Friction, tool-defect and horizon checks
Friction: none configured (`03_Error_Async_Config.txt`), none observed. Unconfigured tool defects: `slack_read_channel` on #winddown exceeds the result limit in every run (run-1 · call 3) and the agent re-reads the spilled file with Bash; no outcome changed. Horizon: 205–230 calls, all before the final reply; about 115 of them are the per-issue Linear reads and writes.

## 7 · Verifier sanity (B3e)
No verifier output exists yet. Pre-checks for when it does: (a) E2 — the Helpshift export request is not on Sunset's account list, but rule 10's "Sunset's list" can be read to include it; a rubric row that fails a run for naming it as a third clash would be contested (route to `/create-rubric-writing`: grade the two clashes affirmatively, do not fail an extra). (b) Closed rows in runs 2 and 5 omit the source rule 5 asks for ("say where") — genuine, rule-incorporated.

## 8 · Why Opus passed
| Mechanism | Class | Evidence |
|---|---|---|
| Every register value is stated in the issue's own Linear comment (cost, date, status, owner hand-off) | universe leak (answer co-located with the work item) | 45 × linear_list_comments, e.g. run-1 · call 36 ($150 a month) |
| The conventions doc spells out all 10 decision rules; the agent applies it mechanically | genuine capability on a recipe | run-1 · call 16 |
| Sunset's correction sits in the same Gmail thread the first search opens | universe leak (correction met with the claim) | run-1 · call 22 |
| Trap decoys (Sherwood, old SVB card, Arthur's sheet) are named as superseded in records read first | universe leak | run-1 · call 5, call 9 |
| Gmail is swept with one OR-query of every vendor name, so any vendor email is found | genuine capability | run-3 · call 127, run-6 · call 80–85 |
| 70 of ~180 graded writes (states + comments) restate register cells, so one correct register passes ~40% of the weight | score shape | §2 model |

Score shape (B3b): **uniform success** (avg ≈ 95%, SD 0.024) — rules stated in the place Opus reads first, mechanical cohort, one rarely-opened source (GitHub).

## 9 · Purge list
| Node | Verdict | Why it adds nothing | Action |
|---|---|---|---|
| ENG-2441 OpenAI, 2443 Unity Asset Store, 2444 Veed, 2445 Kling, 2446 Hailuo, 2447 JetBrains, 2450 Adobe, 2452 Dailybot, 2453 Solsten, 2463 Calendly, 2472 Office 365, 2480 Notarize, 2481 UA Assets, 2470 Fondo, 2471 Insurance (15 issues) | FALSE (trivially satisfied) | each comment states its own exclusion reason in plain words; 6/6 runs Canceled all 15 (T17 LEAKED); 90 always-pass rows of state + comment | remove from the seeded project, keep Lucidchart, Google Ads, iPostal, Typecast, Intuit (live traps) |
| T20 Arthur's Subscriptions sheet | FALSE | the project description says it is replaced; never used by any run | keep (cheap), not counted |

## 10 · Candidates and selection (MODE B rebuilds)
Selection rule: a rule the conventions doc already incorporates, a decisive record on a surface no run opened, returned by the natural catalog call for that surface, one end state. Projected landing = the runs whose recorded searches would **not** return the record.

| # | Rule (anchor) | Record and surface | Coupling (rows that change) | Tool-surface proof | Projected misses | Risk |
|---|---|---|---|---|---|---|
| H1 | rule 5 bot notice | Cursor Bugbot comment on a Combo-Fighters PR (GitHub): Teams plan canceled Feb 12 | Cursor Requested→Closed, by Mar 4→dash, ENG-2475 Done, comment | github_get_pull_request_comments (same call as CodeRabbit) | 6/6 (no run opened GitHub) | same root cause as T13 — one /hardness cause |
| H2 | rule 5 in-app/bot notice | Unity build-service bot in #builds (public, existing bot traffic): org subscription terminated, seats end Feb 28 | Unity Requested→Closed, by Feb 18→dash, ENG-2438 Done, comment | slack_search_public_and_private "unity" / read #builds | 4/6 (runs 1, 6 searched cancel*/subscription) | Arthur's comment must not contradict |
| H3 | rule 5 bot notice | 1Password app message in #engineering-bots: Teams subscription canceled, access to Mar 8 | 1Password Open→Closed, by Mar 7→dash, ENG-2479 Done, comment | slack search "1password" | 4/6 | #engineering-bots is now mostly human traffic; coherence check |
| H4 | rule 5 vendor notice | AWS account-closure notice via the AWS chatbot integration in Slack | AWS Open→Closed, by Feb 28→dash, ENG-2455 Done, comment | slack search "aws" | 4/6 | usage billing after closure; ledger Feb line must stay coherent |
| H5 | rule 5 vendor email equivalent | AppLovin rep in the existing #applovin_ shared channel: ad account closed Feb 13 after final spend | AppLovin Open→Closed, by Feb 28→dash (no issue) | slack search "applovin" | 4/6 | register-only (2 rows) |
| H6 | "SVB's card terms" (named in the ask) | Leonard's comment on the SVB Trello card: closure moved to Feb 18, keep-rows off the card by EOD Feb 17 | Intuit, Workspace, Slack by Feb 19→Feb 17 + their 3 comments | trello_get_comments on the card; trello_search returns matching comment actions | 2/6 (runs 4, 6 never searched "SVB" in Trello) | natural text includes "SVB", so 4 runs may see it |
| H7 | rule 6 + SVB terms | same Trello comment also says recurring charges after the closure go to collections; conventions rule 6 changed to "the day before the next charge or SVB's deadline, whichever is first" | by-when of 11 non-Closed Cancel rows → Feb 17 + 9 comments | as H6 | 2–4/6 | changes the conventions doc and every by-when the OEs state; largest single lever |

Rejected: a thread reply in #winddown (every run opened every thread with replies: run-1 · call 6–10); Linear attachments (shown in `list_issues` `links`, run-2 · call 11); Google Doc comments (no catalog tool — unreachable); a Sunset update outside Gmail (Sunset's email pins changes to its thread: "If our engineers change anything on this list, we'll reply on this thread" — a Slack update would be unincorporated); new costs-tab lines (base xlsx cannot be changed).

Projection (`hardening/proj2.py`, landing sets as in the table):

```
rows 179 weight 553
current data                       avg  95.1%  sd 0.024  runs 96.7 94.6 97.3 95.3 90.2 96.7
+ H1 Cursor Bugbot (GitHub PR)     avg  93.0%  sd 0.024  runs 94.6 92.4 95.1 93.2 88.1 94.6
+ H2 Unity build-service bot (#builds) avg  91.6%  sd 0.030  runs 94.6 90.3 93.0 91.1 86.0 94.6
+ H3 1Password app (#engineering-bots) avg  90.2%  sd 0.037  runs 94.7 88.3 90.9 89.0 84.0 94.7
+ H4 AWS notice (Slack bot)        avg  88.9%  sd 0.046  runs 94.7 86.2 88.8 86.9 81.9 94.7
+ H5 AppLovin rep (#applovin_ shared) avg  88.2%  sd 0.050  runs 94.7 85.1 87.8 85.8 80.9 94.7
+ H6 SVB card comment (Trello)     avg  87.1%  sd 0.048  runs 94.7 85.1 87.8 82.7 80.9 91.5

A current scenario + H1-H6                   rows 183 avg  87.1% sd 0.048 | 94.7 85.1 87.8 82.7 80.9 91.5
B drop 15 trivial issues + H1-H6             rows 153 avg  84.7% sd 0.057 | 93.7 82.3 85.5 79.4 77.3 89.9
C A + H7 missed by runs [4, 6]               rows 183 avg  84.5% sd 0.058 | 94.7 85.1 87.8 76.3 80.9 82.5
D B + H7 missed by runs [4, 6]               rows 153 avg  81.6% sd 0.069 | 93.7 82.3 85.5 71.8 77.3 79.2
C A + H7 missed by runs [2, 4, 6]            rows 183 avg  83.0% sd 0.065 | 94.7 76.1 87.8 76.3 80.9 82.5
D B + H7 missed by runs [2, 4, 6]            rows 153 avg  79.8% sd 0.078 | 93.7 71.6 85.5 71.8 77.3 79.2
C A + H7 missed by runs [2, 3, 4, 6]         rows 183 avg  81.4% sd 0.064 | 94.7 76.1 78.2 76.3 80.9 82.5
D B + H7 missed by runs [2, 3, 4, 6]         rows 153 avg  77.9% sd 0.076 | 93.7 71.6 74.1 71.8 77.3 79.2
```

**Reading of the projection.** Hidden facts alone (A) stop at ~87%. Purging the 15 trivially-satisfied issues (B) and adding the SVB lever that moves every non-Closed Cancel deadline (H7) is the only fair combination that reaches the author target: **D lands at 77.9–79.8%** with runs spread 71.6–93.7. It still projects SD ≈ 0.077 (Evals needs ≥ 0.1) and does not reach the Evals < 75% gate. The landing sets are inferred from the searches each run made; a run that adds one Slack keyword search can find H2–H5, so the true average could sit several points higher.

## 11 · Routing
Universe changes (planned, not yet made — this revision is plan only): purge 15 issues (§9); seed H1–H6; implement H7 by editing conventions rule 6 and adding the Trello comment. Every changed fact for the human: Cursor, Unity, 1Password, AWS, AppLovin become Closed (5 more Done issues: ENG-2475, ENG-2438, ENG-2479, ENG-2455 + ENG-2474); by-when for Intuit, Workspace, Slack becomes Feb 17; by-when for every remaining non-Closed Cancel row becomes Feb 17; the Linear project shrinks from 45 to 30 issues; totals unchanged (no row added or removed from the register).
Prompt-side defects: none found that cause the ease (the prompt names sources the way the persona would; difficulty leaks from the universe).
Routed observations: `/create-rubric-writing` — E2 Helpshift extra clash must not be failed; rule 5 "say where" is a genuine row. `/create-oe-writing` — every OE that states a changed value must be regenerated after the SQL change.

## 12 · Self-review
| Check | Verdict | Strongest counter-reading | Resolution (evidence) | Unresolved |
|---|---|---|---|---|
| T13 LANDED | keep | tool: the GitHub notice was never returned, so the miss is a search gap, not judgement | 1A §3: for Opus a missed discoverable source is a genuine retrieval failure; the comment exists in SQL (`grep Combo-Fighters#38#c_1` → 1 row) and `github_get_pull_request_comments` returns PR comments; rule 5 names bot notices | none |
| T19 LANDED (1/6) | keep | fairness: iPostal's Jan 16 closure could be read as after the charge, so keeping it is defensible | rule 2 'anything cancelled before Feb 9'; the closure mail (robert@harmonygames.co/1854432461283937829) is dated Jan 16 2026 | none |
| E1 adjoe LANDED | keep | rule 3 says every account in a multi-vendor line gets a row, so adjoe belongs | rule 2 overrides: AD_SPEND_DAILY adjoe last row 2025-06-27 (run-4 · call 105), nothing in the Jan/Feb ledger | none |
| E2 Helpshift CONFOUNDED | keep | it is a real clash: Leonard posted 'we don't need to export any data' | rule 10 counts decisions Sunset's *list* undoes; the export request is outside the account list — contested, so never counted as landed | rubric must not fail it |
| E3 ElevenLabs date | keep minor | Jul 7 could be right if the prepaid year ends Jul 8 | receipt Jul 9 2025 annual → access to Jul 9 2026 → day before = Jul 8 (threads/00014566.json) | none |
| Projection D evidence | report as a projection | the D numbers are invented | computed by hardening/proj2.py from truth.json and the graded runs (grades.json); output pasted in §10 | none |
| Band 3 | keep | band 4: CodeRabbit wrong in three places is three failures | 1A §3: one root cause repeated in state, register and comment is one cause | none |
| Band 3 vs 2 | keep | band 2: everything core is right | the ENG-2474 state and register status are wrong writes, not wording | none |
| Projection D | report as a projection | the landing sets are guesses; runs may search Slack for each vendor | landing sets come from each run's recorded queries (§5); stated as a range and caveated in §10 | true numbers only after re-run |
| Purge is tuning | keep | deleting 15 issues to move the average is gate-4 tuning | B5 purges FALSE nodes (trivially satisfied, 6/6); no criterion is deleted or re-weighted — the universe is made leaner | none |
| H7 fairness | flag | changing rule 6 makes SVB govern Cancel rows, a second end state if the doc and card disagree | the doc change makes the rule explicit ('whichever is first'); the card comment is by the card's author after the description — one governing version | /prompt must re-check UGT |
| Re-verified records | done | values carried from the dossier | re-read via `tools/hg.py`: CodeRabbit notice only in SQL (slack search 'Final build settings' → 0 matches); #builds bot traffic and #applovin_ channel present in the base slack export; Lucidchart/Google Ads notices threads/00015599.json, 00015671.json | none |
| T1 LEAKED | keep, behaves as FALSE | the trap was never live, so it is FALSE not LEAKED (keeps Gusto through the shutdown (Leonard's keep list) with ) | resolving record returned at run-5 · call 5 (earliest), all six runs: run-1 · call 6, run-2 · call 6, run-3 · call 6, run-4 · call 6, run-5 · call 5, run-6 · call 6 — never live in practice (resolved before any wrong reading could form) | none |
| T2 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (plans the Slack downgrade to free (agreed Feb 11) without fl) | resolving record returned at run-2 · call 17 (earliest), all six runs: run-1 · call 25, run-2 · call 17, run-3 · call 24, run-4 · call 27, run-5 · call 69, run-6 · call 21 — live: the resolving record was met only after the agent had the claim | none |
| T3 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (puts Google Workspace down for archiving after Feb 15 (Leona) | resolving record returned at run-2 · call 17 (earliest), all six runs: run-1 · call 25, run-2 · call 17, run-3 · call 24, run-4 · call 27, run-5 · call 69, run-6 · call 21 — live: the resolving record was met only after the agent had the claim | none |
| T4 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (holds Metabase for Sunset (first checklist) or leaves its ca) | resolving record returned at run-2 · call 18 (earliest), all six runs: run-1 · call 22, run-2 · call 18, run-3 · call 22, run-4 · call 25, run-5 · call 67, run-6 · call 19 — live: the resolving record was met only after the agent had the claim | none |
| T5 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (stops at the first checklist: cancels Trello (paid plan ende) | resolving record returned at run-2 · call 18 (earliest), all six runs: run-1 · call 22, run-2 · call 18, run-3 · call 22, run-4 · call 25, run-5 · call 67, run-6 · call 19 — live: the resolving record was met only after the agent had the claim | none |
| T6 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (treats Arthur's 40 issues as the complete account list) | resolving record returned at run-6 · call 22 (earliest), all six runs: run-1 · call 88, run-2 · call 49, run-3 · call 41, run-4 · call 26, run-5 · call 105, run-6 · call 22 — live: the resolving record was met only after the agent had the claim | none |
| T7 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (one Sound row (or Soundly at $15) because the tab has one li) | resolving record returned at run-6 · call 22 (earliest), all six runs: run-1 · call 88, run-2 · call 49, run-3 · call 41, run-4 · call 26, run-5 · call 105, run-6 · call 22 — live: the resolving record was met only after the agent had the claim | none |
| T8 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (no UA account on the register (no issue for it, Frederick le) | resolving record returned at run-6 · call 25 (earliest), all six runs: run-1 · call 29, run-2 · call 27, run-3 · call 35, run-4 · call 32, run-5 · call 74, run-6 · call 25 — live: the resolving record was met only after the agent had the claim | none |
| T9 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (no card deadline (Slack never dates the closure) or the 2023) | resolving record returned at run-6 · call 10 (earliest), all six runs: run-1 · call 118, run-2 · call 129, run-3 · call 121, run-4 · call 11, run-5 · call 98, run-6 · call 10 — live: the resolving record was met only after the agent had the claim | none |
| T10 LEAKED | keep, behaves as FALSE | the trap was never live, so it is FALSE not LEAKED (applies Sherwood's 'cancel every subscription now except pay) | resolving record returned at run-5 · call 4 (earliest), all six runs: run-1 · call 5, run-2 · call 5, run-3 · call 5, run-4 · call 5, run-5 · call 4, run-6 · call 5 — never live in practice (resolved before any wrong reading could form) | none |
| T11 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (costs Meta Ads at trailing 30-day spend or treats it closed ) | resolving record returned at run-3 · call 13 (earliest), all six runs: run-1 · call 16, run-2 · call 14, run-3 · call 13, run-4 · call 16, run-5 · call 15, run-6 · call 14 — live: the resolving record was met only after the agent had the claim | none |
| T12 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (two rows (QuickBooks and Intuit) or Canceled on the older is) | resolving record returned at run-5 · call 39 (earliest), all six runs: run-1 · call 57, run-2 · call 70, run-3 · call 65, run-4 · call 60, run-5 · call 39, run-6 · call 48 — live: the resolving record was met only after the agent had the claim | none |
| T14 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (Hold rows with no date, Feb 15, or 'until Sunset confirms') | resolving record returned at run-2 · call 20 (earliest), all six runs: run-1 · call 27, run-2 · call 20, run-3 · call 25, run-4 · call 31, run-5 · call 71, run-6 · call 23 — live: the resolving record was met only after the agent had the claim | none |
| T15 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (Helpshift deadline Feb 27 (export still pending) or no expor) | resolving record returned at run-3 · call 14 (earliest), all six runs: run-1 · call 17, run-2 · call 24, run-3 · call 14, run-4 · call 17, run-5 · call 14, run-6 · call 15 — live: the resolving record was met only after the agent had the claim | none |
| T16 LEAKED | keep, behaves as FALSE | the trap was never live, so it is FALSE not LEAKED (Singular at 6,250 or 0, Figma at 0 or 1,212, Carta/Docusign/) | resolving record returned at run-6 · call 8 (earliest), all six runs: run-1 · call 9, run-2 · call 9, run-3 · call 10, run-4 · call 9, run-5 · call 9, run-6 · call 8 — never live in practice (resolved before any wrong reading could form) | none |
| T17 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (keeps never-paid, one-off or pre-Feb-9 accounts, or drops Tr) | resolving record returned at run-3 · call 13 (earliest), all six runs: run-1 · call 16, run-2 · call 14, run-3 · call 13, run-4 · call 16, run-5 · call 15, run-6 · call 14 — live: the resolving record was met only after the agent had the claim | none |
| T18 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (Leonard as Docusign's owner (the assignee)) | resolving record returned at run-5 · call 10 (earliest), all six runs: run-1 · call 11, run-2 · call 11, run-3 · call 11, run-4 · call 14, run-5 · call 10, run-6 · call 11 — live: the resolving record was met only after the agent had the claim | none |
| T20 LEAKED | keep, behaves as FALSE | the trap was never live, so it is FALSE not LEAKED (uses Arthur's 18-row 'Subscriptions' sheet (rounded figures)) | resolving record returned at run-6 · call 8 (earliest), all six runs: run-1 · call 9, run-2 · call 9, run-3 · call 10, run-4 · call 9, run-5 · call 9, run-6 · call 8 — never live in practice (resolved before any wrong reading could form) | none |
| T21 LEAKED | keep, behaves as FALSE | the trap was never live, so it is FALSE not LEAKED (keeps Cursor for Oliver) | resolving record returned at run-5 · call 4 (earliest), all six runs: run-1 · call 5, run-2 · call 5, run-3 · call 5, run-4 · call 5, run-5 · call 4, run-6 · call 5 — never live in practice (resolved before any wrong reading could form) | none |
| T22 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (Singular deadline Mar 14 (the past-due extension to Mar 15)) | resolving record returned at run-5 · call 33 (earliest), all six runs: run-1 · call 51, run-2 · call 72, run-3 · call 67, run-4 · call 54, run-5 · call 33, run-6 · call 50 — live: the resolving record was met only after the agent had the claim | none |
| T23 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (Helpshift at $1,500 / $300 (balances owed) instead of its mo) | resolving record returned at run-5 · call 18 (earliest), all six runs: run-1 · call 36, run-2 · call 74, run-3 · call 69, run-4 · call 39, run-5 · call 18, run-6 · call 52 — live: the resolving record was met only after the agent had the claim | none |
| T24 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (AWS at ~$1,550 (page) or ~$1k (Arthur's DD prod estimate) or) | resolving record returned at run-6 · call 28 (earliest), all six runs: run-1 · call 87, run-2 · call 50, run-3 · call 40, run-4 · call 34, run-5 · call 106, run-6 · call 28 — live: the resolving record was met only after the agent had the claim | none |
| T25 LEAKED | keep | the trap was never live, so it is FALSE not LEAKED (costs read off the costs tab's December figures (Unity 2,172) | resolving record returned at run-5 · call 17 (earliest), all six runs: run-1 · call 35, run-2 · call 59, run-3 · call 54, run-4 · call 38, run-5 · call 17, run-6 · call 37 — live: the resolving record was met only after the agent had the claim | none |

Neighbouring band argued above (3 vs 4, 3 vs 2). Unresolved: whether the projected landing sets hold, and H7's UGT check at /prompt.

```
STAGE GATE hardening: PASS — Task_Authoring-2/task_inputs · 01a_Hardening_Report.md#8a5da87ca788 · 01_Universe_Inject.sql#50f6a195de7e · 01_Hardness_Manifest.json#526f2a78d444 · blocking 0 · warnings 0 · checks 14
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#50f6a195de7e, 01_Hardness_Manifest.json#526f2a78d444, 01_Grounding_Dossier.md#7bf3e5461eb4)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 28/28 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 33 evidenced counter-readings (of 35 found; need ≥ 32) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

## 13 · Next steps
1. Decide on the plan (the human): D projects 77.9–79.8% average but SD ≈ 0.077 and does not meet the Evals < 75% gate; A/B/C stay above 80%.
2. If approved: `/create-injection` reads this report as the hardening request (purge + H1–H7), then `sql_lint`, `hardness_gate`, `stage_gate.py injection`, `/injection`.
3. Re-run `/prompt` (UGT on H7), regenerate the OEs (`/create-oe-writing`), `/oe`, then a new pre-check and baseline; measure with `/create-difficulty`.
