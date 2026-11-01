# Hardening Report — fs-account-custody · round 2

## 1 · Mode, inputs and run validity

MODE B (baseline trajectories without verifier results): six Opus rollouts, verdicts per designed difficulty, a predicted `/hardness` band,
no gate statistics (the verifier and difficulty files are empty).

Inputs read: `00_Assigments.md` (Normal Horizon, Medium mode, Oct 1, 2025 universe), `01_Universe_Inject.sql` (as run: a9784ed111e9;
hardened: 53e2608eebbc, §11), `01_Grounding_Dossier.md`, `01_Hardness_Manifest.json`, `03_Error_Async_Config.txt` (Friction: none),
`04_Prompt.txt` (unchanged), `07_Baseline_Trajectories/` (six files, every tool call and result read), the round-1 report (backup in
`Working_Files/pre_hardening_r2/`). Inputs missing or empty: `10_Baseline_Verifier_Results.md`, `12_Difficulty_Stats.txt`,
`08_Oracle_Events.md`, `09_Rubrics.json`, so B3d (clean average) and B3e (verifier sanity) are skipped. `06_PreCheck_Trajectory/trajectory.json`
is still the round-0 pre-check (SQL c0b774238114) and is not evidence for this SQL.

User target for this round: six-rollout average under 80% (mode cap 85%), at least 70 tool calls per run.

Run validity (B0), per file:

| File | Calls | Model / subagents | Result | Injection applied (seeded record read) |
|---|---|---|---|---|
| trajectory-run-1 (2).json | 93 | claude-opus-5-5 only, none | success, 94 turns, no compaction | hub thread reply run-1 · call #50; YouTube Brand Account tab run-1 · call #49 |
| trajectory-run-2.json | 93 | claude-opus-5-5 only, none | success, 94 turns | reply run-2 · call #9; Brand Account tab run-2 · call #51 |
| trajectory-run-3.json | 99 | claude-opus-5-5 only, none | success, 100 turns | reply run-3 · call #8; Arthur's email run-3 · call #54 |
| trajectory-run-4.json | 88 | claude-opus-5-5 only, none | success, 89 turns | reply run-4 · call #9; Arthur's email run-4 · call #69 |
| trajectory-run-5.json | 87 | claude-opus-5-5 only, none | success, 88 turns | reply run-5 · call #49; Arthur's email run-5 · call #68 |
| trajectory-run-6.json | 92 | claude-opus-5-5 only, none | success, 93 turns | reply run-6 · call #50; old AdMob mail run-6 · call #72 |

File mapping: the run-1 file carries a browser-duplicate suffix "(2)"; its content is distinct (its own register 1YjN7e3LtkMaQj-wI9PPX8A6sUGbZdI53_WQyVWi9rqg
at call #85), so six distinct rollouts are present. Mapping to verifier `Run #N` is by content once `10` exists. Completeness: every export ends in a
`result` event after the final Slack reply; nothing reports after the answer. Horizon: 87–99 calls (mean 92); Normal floor 50 and the user's 70 met.

## 2 · Gate status

Not available: `10_Baseline_Verifier_Results.md` and `12_Difficulty_Stats.txt` are empty, so pass@1, the weighted average, the spread and the
failure patterns cannot be computed (gate 2: no estimate stands in for them). What the write payloads show (register rows, reply, checklist):

| Rollout | Register rows wrong (vs the round-1 key) | Reply | Checklist |
|---|---|---|---|
| run-1 | Google Ads 569 CLOSE (run-1 · call #85); 14th row AdMob pub-2341961509332343 | "14 accounts"; 2 TRANSFER; Node on 3 (run-1 · call #93) | TikTok, X (calls #91–#92) |
| run-2 | Google Ads 569 CLOSE (run-2 · call #83); 14th row pub-2341961509332343 | "14 accounts"; 2 TRANSFER (run-2 · call #93) | TikTok, X |
| run-3 | 14th row pub-2341961509332343 (run-3 · call #89) | "14 accounts" (run-3 · call #99) | TikTok, X |
| run-4 | 14th row pub-2341961509332343 (run-4 · call #81) | "14 accounts" (run-4 · call #88) | TikTok, X |
| run-5 | 14th row pub-2341961509332343 (run-5 · call #79) | "14 accounts" (run-5 · call #87) | TikTok, X |
| run-6 | none (run-6 · call #83) | 13 accounts (run-6 · call #92) | TikTok, X |

Every rollout got the other 12 rows, the TRANSFER count, the outsiders and the checklist right. Expect run-6 to verify as a full pass and a
high average.

## 3 · Predicted `/hardness` band

As run (SQL a9784ed111e9), median rollout run-4: requirement map R1 MINOR_GAP (one extra deactivated account, run-4 · call #81), R2–R8 MET
(holders, classes, money and actions at call #81; reply call #88; checklist calls #86–#87). Band **2** (HOLD): core correct, one bounded defect.
Not 3: the extra row is CLOSE and changes no count Leonard asked for. Run-1 and run-2 would band 3 (Google Ads 569 closed against Arthur's
email: one consequential, bounded failure).

Replay of run-4's own calls on the hardened SQL (only what each call would now return):

| Requirement | Replay outcome | Basis |
|---|---|---|
| TikTok class/action | MATERIAL_FAIL: SINGLE/TRANSFER instead of OUTSIDE ACCESS/REVOKE | run-4 · call #28 reads the export (now "Scope: Account logins"); its Gmail searches (call #64 to call #79) are dated after Jul 1–Aug 31 or name other vendors; the TikTok reminder is dated Sep 18 |
| YouTube class/action | MATERIAL_FAIL: SINGLE/TRANSFER instead of REVOKE | run-4 · calls #41–#42 read Permissions and Removed users (Node removed); the Brand Account tab is gone; the Google notice is dated Sep 9 |
| Instagram holders/class/action | MATERIAL_FAIL: no company holder/SINGLE/TRANSFER instead of Leonard + Fred/KEEP | run-4 · call #33 found the portfolio tab; it is gone; the Meta notice is dated Sep 15 (round 3), inside the call #67 "after:2025/08/20 (… instagram …)" window |
| TRANSFER count, checklist, outsiders (cascade) | MATERIAL_FAIL: 4 TRANSFER and four items instead of 1 (X); Node on Meta and Unity only | run-4 · calls #81, #86–#88 |
| Rest | unchanged (MET; pub-2341961509332343 MINOR_GAP) | run-4 · call #81 |

Predicted band on the hardened SQL: **4**. Material failures across the result: three rows, the reply's central number, the outsider list and the
checklist. They group into three root causes (three different vendor notices behind three different export scopes). Not 5: the
register, the folder, the reply and the checklist still exist, and 10 of 13 rows are right. Not 3: more than one bounded row moves.

Projection for the user's target (not a gate number; the rubric does not exist yet). The rows these traps decide are each worth 5. The three
shared deliverable facts (count, outsiders, checklist) fail if any one trap lands. If each new trap lands in about 60% of runs, a typical
rubric of about 75 points averages about 68–76%. If all three land in every run, about 55–60%. If all three leak, about 88–92% (the
round-1 level). Under 80% therefore needs at least one of the three to land in most runs.

## 4 · Designed-difficulty register (six rollouts on a9784ed111e9)

Counts are L·C·Le·B·NR out of 6 completed rollouts.

| Node | Mechanism | Verdict | Counts | Evidence |
|---|---|---|---|---|
| T1 Leonard "admin … covered" | claim met first | LEAKED | 0·0·6·0·0 | DM read run-1 · call #3; Meta and Unity REVOKE in every register (run-4 · call #81) |
| T2 page → card → comment → email | supersession chain | LANDED (email leg) | 2·0·4·0·0 | runs 1–2 never opened Arthur's email and closed Google Ads 569 (run-1 · call #85, run-2 · call #83); runs 3–6 read it (run-3 · call #54, run-4 · call #69, run-5 · call #68, run-6 · call #71) |
| T3 90-day remark | decoy supersession | BYPASSED | 0·0·0·6·0 | no run's result contains the remark ("last 90 days" 0 hits in all six files); doc found by "money moving" (run-6 · call #53) |
| T4 March logins sheet | partial listing | BYPASSED | 0·0·0·6·0 | f_4521c272960dd1836a5196 never opened in any run; register built from the folder (run-6 · call #13) |
| T5 engineering card | scope-adjacent | LEAKED | 0·0·6·0·0 | returned with the rules (run-6 · call #9); stores excluded in every register (run-6 · call #87) |
| T6 managers / shared login / personal address | exact predicate | LEAKED | 0·0·6·0·0 | Notes tab run-6 · call #87 (Leonard signs in with Fred's password; Instagram personal login) |
| T7 adjoe waiver | eliminating evidence | LEAKED | 0·0·6·0·0 | adjoe thread run-4 · call #74; adjoe CLOSE in all six |
| T8 two Google Ads accounts | entity collision | LEAKED | 0·0·6·0·0 | both rows in every register (run-2 · call #83) |
| T9 Meta Partners tab | tool surface | LEAKED | 0·0·6·0·0 | Partners tab read run-1 · call #46 … run-6 · call #41 |
| T10 stores and data tools | scope alias | LEAKED | 0·0·6·0·0 | excluded in every register (run-6 · call #87 "Excluded: App Store Connect, Play Console, Singular") |
| T11 reuse the handles card | reuse exclusion | LEAKED | 0·0·6·0·0 | checklist on 67cf1b506d78ad3c72e02a35 in every run (run-6 · call #89) |
| T12 PlayableX / Balancy | keyword distractor | BYPASSED | 0·0·0·6·0 | never returned (run-6 · call #1 to call #80) |
| T13 TikTok "doesn't exist" | stale summary | LEAKED | 0·0·6·0·0 | DM read carries the recovery (run-6 · call #5) |
| T14 Arthur "only youtube and tiktok" | stale summary | BYPASSED | 0·0·0·6·0 | "only youtube and tiktok" 0 hits in all six files; no #executives read (run-6 · call #1 to call #92) |
| T15 deactivation mail vs the live AdMob | entity collision | LEAKED | 0·0·6·0·0 | pub-3556282811018998 kept in every register (run-1 · call #85) |
| T16 YouTube Brand Account tab | tool surface | LEAKED | 0·0·6·0·0 | tab read run-1 · call #49, run-2 · call #51, run-3 · call #77, run-4 · call #42, run-5 · call #48, run-6 · call #48 |
| T17 Unity Ads advertiser tab | tool surface | LEAKED | 0·0·6·0·0 | tab read run-1 · call #47 … run-6 · call #44 |
| T18 Instagram portfolio tab | tool surface | LEAKED | 0·0·6·0·0 | tab read run-1 · call #43, run-2 · call #32, run-3 · call #32, run-4 · call #33, run-5 · call #42, run-6 · call #29 |
| T19 old AdMob export | cohort boundary | LANDED | 5·0·1·0·0 | 14th row in run-1 · call #85, run-2 · call #83, run-3 · call #89, run-4 · call #81, run-5 · call #79; run-6 · call #72 opened the Aug 24 deactivation mail and excluded it |
| T20 $100 thread reply | reply never opened | LEAKED | 0·0·6·0·0 | found by a "money moving" search or the thread read (run-2 · call #9, run-6 · call #50) |

## 5 · Per-rollout ledgers (condensed; all calls read)

All six runs share one skeleton; differences are noted per run.

| Step | Tool | Input | What came back | Decision | Requirement |
|---|---|---|---|---|---|
| run-6 · calls #1–#7 | slack profile, users, DM read, thread read, channels list | Leonard's DM | 80k-character DM, top level only; thread read fails on the user id (call #6) | hub quoted | R1, R6, R7 |
| run-6 · calls #8–#10 | trello list boards, search "handover", comments | — | both rules cards; socials comment | rules from the marketing card | R1–R5, R8 |
| run-6 · calls #11–#14 | gdrive search "sweep", "Company Ops", list folders | sweep folder | 17 exports incl. the old AdMob | the sweep is the list | R1 |
| run-6 · calls #15–#49 | read_file ×7, list_sheets ×14, read_sheet_range ×14 | every export | every tab of every export, incl. Partners, Linked managers, Brand Account, Unity Ads advertiser, portfolio | holders and outsiders from the exports | R2, R3 |
| run-6 · calls #50–#56 | slack/gmail/drive/confluence search "money moving", doc read | — | the $100 reply; the cash notes | definition | R4 |
| run-6 · calls #57–#62, #75–#76 | snowflake ×8 | AD_REVENUE, AD_SPEND_DAILY, FINANCE_LEDGER | admob 38.70, applovin 136.33 paid | money by network | R4 |
| run-6 · calls #63–#80 | gmail searches (all dated after Aug 25 / Sep 1 except the account-id and Calm Play ones) and batch reads | receipts, waivers, vendors | Meta $0.05, Arthur's email (#71), AdMob deactivation (#72) | money column; 569 KEEP; pub-2341 off | R1, R4, R5 |
| run-6 · calls #81–#92 | create sheet, move, values_update, share, checklist, items ×2, Slack reply | — | all ok | writes | R5–R8 |
| run-1 | same skeleton | Gmail searches dated after Aug 25/31 except "money moving" (run-1 · calls #51–#83) | Arthur's email never opened | 569 CLOSE; 14 rows | R1, R5 |
| run-2 | same skeleton | Gmail searches dated after Aug 15–31 (run-2 · calls #62–#79) | Arthur's email never opened | 569 CLOSE; 14 rows | R1, R5 |
| run-3 | same skeleton | partner/agency Gmail search (run-3 · call #57) returned nothing access-related | — | 14 rows | R1 |
| runs 4–5 | same skeleton | Arthur's email opened (run-4 · call #69, run-5 · call #68); deactivation mail not opened | — | 14 rows | R1 |

Searched: the DM, the rules cards, the sweep folder, every export tab, the cash notes, Snowflake, money mail, the adjoe thread. Skipped in
all six: #executives, the Node channel C08MCEP1B9B, any Gmail search for Node Media, access, ownership or partners (except run-3 · call #57),
any undated YouTube, TikTok or Instagram mail search. Every run committed to the exports as the holder authority.

## 6 · Friction, tool-defect and horizon checks

- Async / forced errors: none configured (Friction: none); none fired.
- Unconfigured tool behaviour: `slack_read_thread` with the user id fails (`channel_not_found`, run-6 · call #6); every run recovered with the DM
  id or a search (run-2 · call #9). `gdrive_read_file` returns the first tab only; every run used `gdrive_list_sheets` + `gdrive_read_sheet_range`
  (run-6 · calls #22–#49). Neither changed an outcome.
- Horizon: 87–99 calls; blocked or repeated calls (jq missing, the failed thread read) are 2–3 per run, so the effective count is 85–97. The
  hardened SQL removes two tab reads and adds the access searches a correct run needs (manifest budget 63; real runs run about 30 calls over budget).

## 7 · Verifier sanity findings

Not applicable: no verifier results yet.

## 8 · Why Opus passed

| Point | Mechanism | Class |
|---|---|---|
| Every outside party and portfolio holder | the deciding fact sat on a tab, and Opus now lists every tab of every export (run-6 · calls #22–#38) | universe leak: the trap lived on the first-read surface |
| AdMob $100 rule | the reply's own words contain "money moving", the search every run makes for the definition (run-6 · call #50) | universe leak (findable by the obvious query) |
| adjoe waiver, Meta billing, Unity campaigns | money searches are what every run does broadly (run-6 · calls #63–#80) | genuine capability |
| Rules, comment, Arthur's email (4 of 6) | card title search and Google Ads id searches (run-6 · call #68) | genuine capability |
| What failed | facts that need a search nobody thinks to make: a deactivation mail by publisher id (5/6 missed), Arthur's email outside the money window (2/6 missed) | the lever for round 2: deciding facts in mail that money searches and export reads do not return |

## 9 · Purge list

- T3 (90-day remark), T4 (March sheet), T12 (PlayableX / Balancy), T14 (Arthur's summary): BYPASSED in all six (§4). Kept as harmless context
  (they cost nothing and keep the universe realistic); no longer counted as designed difficulty.
- T16 and T18 as tab traps: LEAKED 6/6 because the facts sat on tabs every run lists. Rebuilt (§10): the tabs are removed and the facts moved into
  vendor notices in Fred's mailbox.
- T17 (Unity Ads advertiser tab) LEAKED 6/6 but stays. It is still the only record of Node's Unity access, and moving it would leave Leonard's
  Unity claim unresolvable from any export.

## 10 · Rebuilds in MODE B

| # | Anchor storyline (cited) | Coupling | Characteristic | Discovery-order proof | Reach | Findability term | Gradable fact | Services | Risks |
|---|---|---|---|---|---|---|---|---|---|
| T21 (new) | Node's Leadsie link asked for partner access to Facebook, Google and TikTok (C08MCEP1B9B/1728234009.536219, Oct 6, 2024); Node terminated Dec 20, 2024 (D05S58U4SAK/1734719973.099339); Fred's cleanup covered Google Ads and YouTube Studio only | TikTok export (Scope: account logins) reads SINGLE → the Business Center reminder makes it OUTSIDE ACCESS → REVOKE → TRANSFER count 2→1 → checklist loses TikTok → outsider list gains TikTok | A18 needle a topical (money) search cannot reach; reading past the export | export read first (run-6 · call #42); reminder dated Sep 18 (round 3): reached by undated or after-Aug 31 tiktok searches, not by money-only ones | YES (own mailbox, check-sql) | "Node Media", "tiktok" (undated), "partner" | TikTok REVOKE; 1 TRANSFER; Node on 4 | gmail, gsheets, slack, trello | a run that searches Gmail for "Node Media" finds it in one call |
| T16 (rebuilt) | Fred created the channel for Node's uploads (C08MCEP1B9B/1732203251.229079); Leonard "YouTube says I'm a manager and not the owner" (D05S58U4SAK/1759096868.688389) | Removed users (Node gone) looks conclusive → Google's Brand Account notice lists Node's address [EMAIL_126620] as Owner → OUTSIDE ACCESS → REVOKE | A10 exclusion settled within seconds + cross-source address join | the export's Removed users tab is met first (run-6 · call #47); notice dated Sep 9 | YES | "Brand Account", "youtube" (undated), "[EMAIL_126620]" | YouTube REVOKE | gmail, gsheets, trello | the export's Scope row and Leonard's DM line are fair cues; a cue-following run finds it |
| T18 (rebuilt) | Instagram sits in the company business portfolio ([SOURCE_ORG_0001]) (Node asked for Page access, C08MCEP1B9B/1728283242.648299) | the personal-login row (no company holder) looks conclusive → Meta's notice lists Leonard and Fred with full control → COMPANY-HELD → KEEP (off the checklist) | A13 evidence in a rarely-opened service; error in the opposite direction (over-transfer) | the export says "Login only" (run-6 · call #21); notice dated Sep 15 (round 3), inside the after-Aug 20 windows when the query has no money term | YES | "instagram" (undated), "full control", "business portfolio" | Instagram KEEP | gmail, gsheets, trello | a run may mark TRANSFER without looking further (that is the trap) |

Rejected, with reasons:
- Second "deactivated before the sweep" account (Google Ads 449): base cancels 449 on Oct 16, 2025 (frederick.stone@harmonygames.co/1846207913166171315) and keeps sending it notices through 2025. A September cancellation would contradict base.
- adjoe campaign still switched on: base says the adjoe rep paused it (C07UCC631A6/1757347560.891949).
- X deactivated before the sweep: logging in reactivates an X account, so Arthur could not have exported its access.
- A holder change after the sweep: two defensible dates.
- A second Leonard thread reply: four of six runs read the whole thread (run-2 · call #9), so it lands at most 2/6, the same runs as T2.

## 10a · Round 3 calibration (baseline on ee04dfd2f9fb)

Six Opus rollouts (run-1 · call #97, run-2 · call #85, run-3 · call #92, run-4 · call #72, run-5 · call #87, run-6 · call #85) on the round-2 SQL:

| Run | Wrong rows (vs the 13-row key) | Reply | Checklist | Est. pass rate |
|---|---|---|---|---|
| run-1 | TikTok, YouTube, Instagram TRANSFER; pub-2341 added (call #97 reply "14 accounts") | TRANSFER 4; Node on Meta, Unity | 4 items | ~60–65% |
| run-2 | same as run-1 | same | 4 items | ~60–65% |
| run-3 | same as run-1 | same | 4 items | ~60–65% |
| run-4 | same + Unity KEEP | TRANSFER 4; Node on Meta | 4 items | ~55–60% |
| run-5 | TikTok, YouTube, Instagram TRANSFER (13 rows) | TRANSFER 4; Node on Meta, Unity | 4 items | ~65–70% |
| run-6 | same as run-1 + Meta, Unity KEEP (first tabs only) | TRANSFER 4; "Outsider access: none" | 4 items | ~50–55% |

T16, T18 and T21 LANDED 6/6; no rollout opened a notice body (run-6 · call #65 returned the YouTube notice headers only). Average ~55–68% but over-hardened: the per-rollout
SD is ~0.05 and five rollouts differ on at most one criterion. Calibration: the notices move into September (YouTube Sep 9, Instagram Sep 15, TikTok Sep 18), text unchanged.
Replay of each rollout's own Gmail queries: run-2 · call #64, run-3 · call #63 and run-4 · call #46 reach all three; run-1 · call #69 and run-5 · call #65 carry money terms and reach none;
run-6 · call #64 reaches YouTube. Prediction: about half the rollouts find the notices (finders ~82–88%, others ~55–65%), average ~68–76%, SD ~0.12, two failure patterns
split on the notices. Risk: if five or six rollouts find them, the average rises to ~80–85%.

## 11 · Routing

Universe changes made (SQL a9784ed111e9 → 53e2608eebbc; 83 → 87 INSERTs; generator `support/task_work/fs_account_custody/r2/harden_r2.py`):
- `f_fc27672c5bfea8b760b074` YouTube: tab 2 'Brand Account' removed (tabs now Permissions, Removed users).
- `f_215ff8da73e4173f78515c` Instagram: tab 1 'Business portfolio access' removed; note now "Fred's personal gmail, not harmonygames.co. Login only".
- `f_2f0abe2f1f6726fef63f80` TikTok: new first row "Scope, Account logins".
- `frederick.stone@harmonygames.co/1842801580966444617` new Google notice (2025-09-09) "Review who can manage Harmony Games": Brand Account owners Fred (Primary owner) and [EMAIL_126620] (Owner).
- `frederick.stone@harmonygames.co/1843622639043434721` new TikTok for Business reminder (2025-09-18) "Partner reminder: Node Media LLC can manage @harmonygames": Admin, shared Oct 8, 2024.
- `frederick.stone@harmonygames.co/1843339075781206004` new Meta notice (2025-09-15) "People with full control of @harmonygames": Leonard Hayes (added Jan 22, 2024), Frederick Stone (added Sep 5, 2024); partners none.
- Manifest: T16, T18 reworked, T21 added, chains C4 (A10), C7 (A18), C8 (A13), budget and writes updated (generator `r2/manifest_r2.py`).

Facts that changed (re-check the prompt brief, Oracle Events and criteria against these):

| Account | Before (round 1) | After (round 2) |
|---|---|---|
| TikTok | SINGLE · TRANSFER | OUTSIDE ACCESS (Node Media LLC, Business Center Admin) · REVOKE |
| YouTube | OUTSIDE ACCESS · REVOKE (from the export tab) | unchanged answer; evidence now the Google notice |
| Instagram | COMPANY-HELD · KEEP (from the export tab) | unchanged answer; evidence now the Meta notice |
| Totals | REVOKE 3 · TRANSFER 2 · KEEP 5 · CLOSE 3 | REVOKE 4 · TRANSFER 1 · KEEP 5 · CLOSE 3 |
| Reply | 2 TRANSFER; Node on Meta, Unity, YouTube | 1 TRANSFER (X); Node on Meta, Unity Ads advertiser, YouTube Brand Account, TikTok |
| Checklist on 67cf1b506d78ad3c72e02a35 | TikTok, X | X only |

Mechanical checks on the hardened SQL: `sql_lint` errors 0 (2 Confluence warnings, unchanged disposition); `base_check` PASS; `fact_check
--no-leak` PASS (7 facts); `hardness_gate` (normal) PASS (21 traps / 11 families, 10 chains / 8 mechanisms); `persona_view check-sql` PASS
(YES 76, NO 4: Leonard's and Arthur's own copies of Arthur's email); `stage_gate injection` PASS (dossier Revision 6).

Prompt-side defects: none. "who actually holds it" and "anything an outsider still has access to" come from the hub, and the prompt hands the
DM's asks to the agent ("reply to him in that DM with what he asked for"). Card rules 2–4 define holders and outside access over any source, so
the three notices are incorporated without a prompt change.

| # | Quoted span | Rule (doc §) | Defect | Evidence (rollout · step) |
|---|---|---|---|---|
| — | none | — | no prompt-side defect found | every run took the asks from the hub (run-6 · call #5) |

Routed OE and rubric observations (for `/create-oe-writing` and the rubric, no criterion text here): the three ownership facts now come from
Gmail reads (the Google, TikTok and Meta notices). The TRANSFER count, the outsider list and the checklist are separate prompt-required
deliverables that share the TikTok cause. Grade each fact once per deliverable, and keep one unit of discovery under 50% of the weight
(diversity gate).

## 12 · Self-review

Paired eval walked in order: `Evals/1A_Hardness_Eval.md` §2 (six Opus runs, no subagents, no compaction), §3 (requirement map, incorporation
through the hub and the rules card, failures counted only when the evidence was returned by an ordinary call), §5 (bands). The deciding records
were re-read through `tools/hg.py` (base) and `persona_view.py check-sql` (seeded).

| Verdict / judgement | Strongest counter-reading | Resolution (evidence) |
|---|---|---|
| T1 LEAKED | never live: the Partners tab contradicts it on the same pass | it was live: the claim (D05S58U4SAK/1759187141.318207) is in the DM read (run-6 · call #5) before the Partners read (call #41) |
| T2 LANDED (runs 1–2) | tool cause: the email was never returned | run-1's dated search "(… "google ads" …) after:2025/08/31" (run-1 · call #66) matches the Sep 30 email body, which names the Google Ads account; run-2 · call #66 likewise; ordinary call, not opened; incorporated (subject = the card title, sender = the rules owner, frederick.stone@harmonygames.co/1844732985606656293) |
| T2 LEAKED (runs 3–6) | never live: one Google Ads search returns it | live: it overrides the card's CLOSE for 569 and two runs missed it; opened at run-3 · call #54 |
| T5 LEAKED | obviously wrong card | returned by the natural query (run-6 · call #9 result lists 68dc42f3095ad95194a711ae) and rejected on scope; live |
| T6 LEAKED | rules 2–3 state it verbatim | true; survives as a per-record check (run-6 · call #87 notes) |
| T7 LEAKED | the run was pointed to the thread | runs chose the thread themselves (run-4 · call #74 on C07UCC631A6/1757346020.196019) |
| T8 LEAKED | the exports name each account | the email names both ids (frederick.stone@harmonygames.co/1844732985606656293); rows kept apart (run-2 · call #83) |
| T9 LEAKED | not live: every run lists tabs | true now (run-6 · calls #22–#38); kept because it still needs a second read |
| T10 LEAKED | verbatim scope | true (68dc406c7b0d03e53b334bab rule 1; run-6 · call #87) |
| T11 LEAKED | the card name makes it a lookup | true (run-6 · call #88 found 67cf1b506d78ad3c72e02a35 by name) |
| T13 LEAKED | the DM carries the recovery | true (D05S58U4SAK/1759170013.491159 in run-6 · call #5) |
| T15 LEAKED | trivially different publisher ids | true (f_50ff132ac88169019feeca vs f_e239ffb975eb7c66d7287d); no run dropped the live AdMob |
| T16 LEAKED | the tab was a fair, findable record | yes, and that is why it leaked (run-6 · call #48); rebuilt into Gmail. Fairness of the rebuild: the export's Scope row says "Studio channel permissions" (f_fc27672c5bfea8b760b074 #0), the notice says Studio people are listed in Studio, and the same address [EMAIL_126620] links the notice to Node's row on the Removed users tab |
| T17 LEAKED | never live once tabs are listed | true (run-6 · call #44); kept for the reason in §9 |
| T18 LEAKED | as T16 | rebuilt; UGT: the notice says "Full control (admin)" on two harmonygames.co logins, so rules 2–3 give two company holders (frederick.stone@harmonygames.co/1843339075781206004) |
| T19 LANDED (5/6) | fairness: the deactivation is in an unlinked mail, and a deactivated account could still be "an account Fred is on" | card rule 1 says "An account that was deleted or deactivated before the sweep is off the list" (68dc406c7b0d03e53b334bab); the mail is in Fred's inbox (frederick.stone@harmonygames.co/1841349862518331350, Aug 24, base); run-4's search "after:2025/07/01 (admob OR …)" (run-4 · call #68) returns it and was not opened; run-6 found it (call #72). Genuine retrieval failure |
| T20 LEAKED | not live: the reply contains the search words | true (run-2 · call #9); kept, harmless |
| T21 UGT (new) | the reminder predates the sweep; Node may have been removed between Sep 18 and Sep 30 | no base or seeded record removes Node from TikTok; Fred's removals are dated Dec 20, 2024 (f_ab70b02c329d038a72fb9f #1, f_fc27672c5bfea8b760b074 #1), before the Sep 18 reminder (frederick.stone@harmonygames.co/1843622639043434721) |
| T21 tool (new) | the mock Gmail search may not return the notice for "Node Media" | the body and subject carry "Node Media LLC" verbatim (SQL, gmail_messages 25b931cc-8e32-759f… row); undated "Node Media" base hits are 59 2024 notices (dossier §1.D), so the 2025 reminder sorts newest |
| Band 2 (as run) vs 1 | no defect at all in the median run | run-4 · call #81 wrote a 14th row for a deactivated account; minor, so 2 not 1 |
| Predicted band 4 vs 3 / 5 | 3: one cause (Gmail not searched for access) bounds the correction; 5: the reply's central number is wrong | 1A §3 groups by root cause: three different notices behind three different export scopes are three causes, and they move three rows, the count, the outsider list and the checklist, so 4. The register and destinations stay right, so not 5. Replay only; a cascade counts once |
| Projection under 80% | runs may now search Gmail for access because the tabs are gone and the exports state their scope | that is the intended fair path; if all three leak, the average stays near round 1 (~90%). If all three land in every run, the spread may fall under 0.1 and the failure patterns may collapse into one. Both are named below |

Re-verified records: C08MCEP1B9B 2024-10 shard /62 (Leadsie request, attachment title "Node Media is requesting Partner Access to Facebook,
Google, TikTok and Shopify") and /107–/110 (Page access, "Should be done!") read through `tools/hg.py search get`; base Gmail "Brand Account"
0 hits, "[EMAIL_126620]" 0 hits, "full control" marketing copy only; sender tokens SVC_0065 (frederick.stone@harmonygames.co/1809398634936399225) SVC_0237 (threads/frederick@harmonygames.co_1830754709770522435.json) and SVC_5366
(threads/frederick@harmonygames.co_1834015308618319266.json); the three new thread ids and Message-ID stems 0 hits over 88,726 base thread files; the
three notices `check-sql` YES for frederick_stone.

Unresolved: (1) the under-80% projection is a replay, not a run. It needs the SQL re-applied, then `/injection`, `/prompt` and a new baseline (or
pre-check). (2) Over-hardening risk: if every run misses all three notices, the spread may fall under 0.1 and the failure patterns may collapse. The
fallback is to soften one cue, not to add volume. (3) `08`/`09` are not written; the rubric must grade the three new facts as facts (Node on
TikTok; Instagram's two portfolio admins) and stay under the 50% single-discovery cap. (4) The prompt brief and the human-time worksheet still
carry the round-1 key.

```
STAGE GATE hardening: PASS — Task_Authoring-2/task_inputs · 01a_Hardening_Report.md#13e92f3be916 · 01_Universe_Inject.sql#8d54ed2b4c0c · 01_Hardness_Manifest.json#30603d3b0e49 · blocking 0 · warnings 0 · checks 14
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#8d54ed2b4c0c, 01_Hardness_Manifest.json#30603d3b0e49, 01_Grounding_Dossier.md#357e494b5b92)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 20/20 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 21 evidenced counter-readings (of 22 found; need ≥ 17) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```





## 13 · Next steps

1. `/injection` on the hardened `01_Universe_Inject.sql` (53e2608eebbc), pasted as is.
2. `/prompt` on the unchanged `04_Prompt.txt` with the new SQL.
3. Re-apply the SQL on the platform and run the baseline again (or an Opus pre-check first, then `/hardness`).
4. Refresh `04_Prompt_Writing_Brief.md` and `05_Human_Time_Worksheet.md` for the new key, then `/create-oe-writing`.
