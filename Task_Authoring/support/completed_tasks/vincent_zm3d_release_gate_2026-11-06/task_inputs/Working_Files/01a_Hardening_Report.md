# 01a Hardening Report — Vincent Parker · ZM3D store gate (rev1)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · universe `Universe_SynthCut`, manifest `Evals/references/universes/synthcut/universe_manifest.json`

## 1. Mode, inputs and run validity

**MODE B (pre-check intake).** One platform Opus 5.5 pre-check exists; no baseline yet.

**Inputs read:**
- `00_Assigments.md`, `01_Universe_Inject.sql` (rev1, sha256 `d761d9819dfe…`) and `Working_Files/01_Grounding_Dossier.md`.
- `Working_Files/01_Scenario_Design.md`, `Working_Files/01_Hardness_Manifest.json`, `Working_Files/01_Gradable_Surface.json` and `Working_Files/solver/` (`truth.json`, `solver.py`).
- `03_Error_Async_Config.txt` (Friction: none) and `04_Prompt.txt` (sha256 `90ade78b…`; the platform's ingested copy is `e775405e…`, the same text).
- `06_PreCheck_Trajectory/trajectory.json`, copied byte for byte from the user's download (sha256 `f2b7862f93162316d09c7b2d2e528fed38749af8cc57da38d5e6395c06f83db9`, the hash the platform reports).
- The platform `/hardness` report: `plateform_report/6ae9909f7b5249d3148f3707_1a_hardness.md` (FAIL, score 1, Too easy, HOLD).
- The completed tasks under `support/completed_tasks/`, and the doctrine `references/Docs/13_Hardness_v2_Opus55.md` and `references/Hardness_Mastery.md` §13.

**Inputs missing (parts skipped):**
- No six-rollout baseline exists: `07_Baseline_Trajectories/`, `10_Baseline_Verifier_Results.md` and `12_Difficulty_Stats.txt` are empty or README-only.
- `08_Oracle_Events.md`, `09_Rubrics.json` and `11_AF_Justification.md` are empty, so this report has no rubric or verifier evidence.

**Run validity (B0, `trajectory_ledger.py`):**

| Check | Result |
|---|---|
| Model | Every message is `claude-opus-5-5`; the init block reads `claude-opus-5-5[1m]`. No subagents, no `model_refusal_fallback`. `mixed_model false`, `v3_valid true`, `valid_for_claude-opus-5-5 VALID` |
| Completeness | stream-json, 504 events, one result event (event 503: `success`, `terminal_reason completed`, 152 turns, $7.27, 8.5 min). No compaction, no events after the result |
| Revision binding | **BOUND: rev1** (`--sole-revision`: rev1 is the only revision ever deployed). The run read the rev1-only "build status means" row (event 24) and Leonard's ZOM-477 ruling (opus · event 446) |
| Hint status | The export carries no prompt. The run's first calls go to the prompt's anchors and nothing in it reads like a hint (the platform says the same) |
| Calls | 151 raw tool_use. **141 counted**: minus 8 Bash (harness) and 2 blocked (event 341 Gmail ECONNRESET, event 368 Snowflake query error); 0 repeats |
| Spills | Events 51, 99, 394 (Slack channel reads); each was recovered through Bash |

**Intake results (pre-check):**
1. **Binding:** BOUND rev1; not mixed-model; valid.
2. **Proposals:** 20 from `node_verdicts.py`, all dispositioned (`run_forensics/rev1/precheck.dispositioned.jsonl`). Review coverage: every call in the review queue (event 493) and all 151 calls were read through two forensic ledgers (`run_forensics/rev1/precheck/B1_ledger_part1.md` for events 0–250, `B1_ledger_part2.md` for 251–503).
3. **Deliverable diff:** `surface_grader.py` gives 97.2 %; only V01 failed. Corrected for the grader defect in §7, the result is **108/108 = 100 %**. Register: 0 call differences and 0 build-status differences over 132 keys, plus ZOM-581, the run's own ticket, which the rules require.
4. **Ledger:** 20 records appended (`hev_629850249f55e2d3` … `hev_ca4272a74d98fce0`; full list in §4).
5. **Posterior forecast:** pre-registered as `hev_a821dfc67699e7d6`. P(all four V3 gates) 0.000–0.574, E[average] 0.811–0.889 across views. **UNCALIBRATED.** Its priors still give every mechanism a 0.25–0.38 landing chance after a run that landed none, so it overstates difficulty (§3).
6. **Decision: NO-GO.** The V3 go rule fails on three of its four conditions: `/hardness` is 1, not ≥ 3; the corrected proxy is 100 %, not ≤ 85 %; and 0 independent loss channels failed, not ≥ 2. Only run validity holds. Do not spend the six-run baseline on rev1; go to `/create-scenario --revise`. This is the first platform pre-check on this scenario (the stop rule allows two).

## 2. Gate status

MODE B baseline only. There are no rollouts, so no numbers from `12` exist. The pre-check's corrected proxy (100 %) is not a gate statistic.

## 3. Predicted `/hardness` band

The band is observed, not predicted: the platform `/hardness` scored this run **1 (Too easy)**, and the local requirement map agrees.

| # | Requirement | Expected (source) | Observed (opus · event) | Outcome |
|---|---|---|---|---|
| R1 | Register scope (any team or label, open plus Done after the Sep 22 cut, plus tickets filed during the gate) | Leonard's doc `f_632c44650df44fe252ee59` | Read at opus · event 34; 133 rows written at event 493 | MET |
| R2 | New tab in the How we gate format | `f_0ebfccf33076f9dbf086bc` | Tab added at opus · event 472, rows at 493 | MET |
| R3 | Calls (BLOCKER / KNOWN ISSUE / FIXED / NO CALL) and build status | `truth.json` | 0 differences on either field (opus · event 493, decoded in ledger part 2 §3.1) | MET |
| R4 | Blockers on ZOM-570 by existing key | ZOM-570 plus the Trello reuse rule | 16 keys appended at opus · event 496 | MET |
| R5 | One new ticket for the unfiled runbook finding | Brian's update-path doc `f_5e40215b7d4d24b0455412` | ZOM-581 created at opus · event 462 | MET |
| R6 | NO-GO as a reply in Arthur's thread | `cmt_zom570_1` | Posted at opus · event 499 (thread_ts 1759263900.484190) | MET |

**Neighbouring band (2):** a 2 needs at least one minor defect that matters, or a narrow miss. The run's only defects were cosmetic: ZOM-581's description calls the issue "the June 2025 wipe hypothesis", and "@Brian Foster" in the reply is plain text. Neither touches a graded value, so 1 holds.

## 4. Designed-difficulty register

All counts are out of 1 completed rollout.

| Node (rule) | Mechanism | Verdict | LANDED · CONFOUNDED · LEAKED · BYPASSED · NOT-REACHED | Evidence (opus · event) | Ledger id |
|---|---|---|---|---|---|
| T1 ZOM-569 build cut (R_DONE_BUILD) | A24 done-check | LEAKED | 0 · 0 · 1 · 0 · 0 | Two things gave the timing away: the ticket's own `cmt_zom569_1` ("fix is on main now", 21:40Z), read at opus · event 158 (result 159), and the run's commit sweep at event 178, whose result (event 179) shows `a61cb2b` at 21:36Z, after both Started lines (event 57) | `hev_629850249f55e2d3` |
| T2 ZOM-567 not live (R_DONE_SERVER) | A24 done-check | LEAKED | 0 · 0 · 1 · 0 · 0 | Douglas's reply "#36 stays on dev" (ts 1759262520) came back from the `from:douglas` search at opus · event 294, and Arthur's withdrawal from the thread read at event 301. Both were also in the post-candidate sweep at event 386 | `hev_da8f703d3115e8e0` |
| T3 ZOM-435 Trello re-test (R_CORRECTION) | A11 correction elsewhere | LEAKED | 0 · 0 · 1 · 0 · 0 | Leonard's comment `68dc63484a5b2d0a869e758f` sits on the card ZOM-570 names. Read at opus · event 38, before Vincent's #133 pass (event 110) | `hev_fcae4e267ad7d452` |
| T3b ZOM-473 Turkish DM (R_CORRECTION) | A11 | LEAKED | 0 · 0 · 1 · 0 · 0 | D0770ET1HV2/1759267800.858041 came back in the `-in:#builds` sweep at opus · event 386 and in the DM read at event 394 | same record |
| T4 update path vs "matrix green" (R_UPDATE_RULE) | A15 | FALSE as a mechanism (no ablation changes a value) | — | B01 was met: Brian's DM pointer (opus · event 394) led to a Drive search by owner and date (event 396) and his doc (event 400) | `hev_8f613c1258c209c0` |
| T5 vendor alias → ZOM-562 (R_ALIAS) | A7 alias | LEAKED | 0 · 0 · 1 · 0 · 0 | `gmail_search after:2025/09/29` at opus · event 327 returned all 5 messages; the vendor mail was read and decoded at events 341–346 | `hev_a9d032847c594cf3` |
| T6 scope (R_FILTER) | A17 outside the filter | LEAKED | 0 · 0 · 1 · 0 · 0 | Leonard's scope sentence, verbatim at opus · event 34. The "ZM" query (event 77) listed ART-790/792/793 and DES-313 | `hev_95fae459cc9d282a` |
| T7 ZOM-563 live on prod (R_COMPLETION) | A25 | LEAKED | 0 · 0 · 1 · 0 · 0 | DM D079SNE2TL4 (base, ts 1759269524.769369), read at opus · event 303 | `hev_9f21d34afc03eb11` |
| T12 ZOM-559 stale Sep 22 tab | supersession | LEAKED | 0 · 0 · 1 · 0 · 0 | Old KNOWN ISSUE row read at opus · event 26; `cmt_zom559_1` (freeze) read at event 245 | — (not a solver rule) |
| Controls (12 trials: ZOM-506, 557, 561, 563, 504, 565, 566, ART-790, 534, 544) | — | HELD (12/12) | — | Register write at opus · event 493 | `hev_05bcd4663bee4d41` … `hev_e33250e8b3badf27` |
| Channel scale:comments | scale | HELD | — | 39 comment threads read (opus · event 28 through event 245), every comment-decided row right | `hev_ca4272a74d98fce0` |

`R_CORRECTION`'s two pending keys (ZOM-435, ZOM-473) differ from the truth only in the QA-result wording; call and build status match. They are dispositioned as **representation** (`features.disposed_by` recorded).

Reach: every load-bearing record was read except three decoys. K7 (go/no-go invite `evt_81e6dc4dbfd331f1a6a317`), K11 (`C08R27X0EAH/1758485492.586459`) and H2-decoy (the Jul 27 doc `f_5ae4332fb6927f84b3afdc`) were never on the path.

## 5. Per-rollout ledgers

- `run_forensics/rev1/precheck/calls.jsonl`, `writes.json`, `ledger.json`: mechanical, from `trajectory_ledger.py`.
- `run_forensics/rev1/precheck/B1_ledger_part1.md` (events 0–250) and `B1_ledger_part2.md` (events 251–503): one row per tool call (step · tool · input · what came back · decision · trap affected), a first-contact table per trap, ticket selection, search habits, sweep completeness and calls per phase.
- `run_forensics/rev1/precheck/unread_surfaces.md`: what the run never read.
- `run_forensics/rev1/precheck/transcript.md`: the readable export. Thinking is redacted in the source.

**What the run did** (opus · events, from the ledgers):
1. **Anchors first:** ZOM-570 (event 13), the runbook (15), Arthur's thread (17), the gate sheet (19–26), ZOM-570's comments (28), the Trello card ZOM-570 names (30/38) and both rule docs (34/36). **Every rule was in hand before any ticket was read.**
2. **Scope from list calls:** one 250-row team list (event 63), four per-state lists (69–75), a "ZM" keyword list (77) and team lists (82/84). No description came back in any list call.
3. **Comments on 39 of 132 tickets** (events 123–245), walked in the default newest-updated-first order. They followed the injected-comment group 33 times out of 38, skipping NO CALL-looking tickets and the six Done tickets Vincent's 23:20Z post covers.
4. **GitHub as lists only:** PR lists for both repos (events 171/173) and the match3d commits since Sep 22 (178). No PR comment, review or review-comment read in the whole run.
5. **Broad sweeps with date floors:**

   | Sweep | Event | Result |
   |---|---|---|
   | Slack `-in:#builds after:1759257000` | 385 and 420 | 66 of 66 messages: DMs, thread replies and #zombie-prs bot copies all included |
   | Gmail `after:2025/09/29` | 327 | 5 of 5 |
   | Trello `#135` | 329 | 0 (comment text isn't indexed) |
   | Trello board actions | 356 | Every post-Sep 22 comment on the ZM ROADMAP board |
   | Drive by Brian, modified after Sep 30 | 396 | 2 of 2 |
   | #zombie-ops, Douglas DM (from Sep 29), Brian DM (from Sep 30 02:40Z) | 305, 303, 394 | — |

6. **Writes:** ticket (event 462), tab (472), values (493), ZOM-570 append (496) and reply (499). No rework.

## 6. Friction, tool-defect and horizon checks

- **Friction:** none configured (`03_Error_Async_Config.txt`). No `*_submit_*` call appears.
- **Unconfigured tool defects:** three Slack channel reads spilled (events 51, 99, 394) and `jq` was missing (53). A concise channel read dropped the attachment text (96). Two searches returned 0 (46, 93). Gmail reset once (341, retried at 344) and one Snowflake query failed (368). None changed an outcome; every deciding record was re-fetched.
- **Horizon:**
  - 141 counted against the Long-Horizon floor of 100. This meets the requester's > 130 target, but with little margin: ledger part 2 counts about 9 wasted or recovery calls, and without them the necessary work is about 132.
  - The run read comments on 39 tickets. Reading every register ticket's comments, which the rules allow and a careful gate needs, would add about 93 calls.
  - Today the call count and the score don't move together: the economical run lost nothing. The rebuilds in §10 tie them, because the extra reads become the only way to find the deciding records.

## 7. Verifier sanity findings

No rubric or verifier exists yet. One design-proxy defect:

- **V01 is a grader defect (CONFOUNDED-fairness).** `register_keys_exact` compares against the 132 `truth_keys`. Leonard's scope sentence ("tickets filed while the gate is running get a row too, including the ones you file yourself") requires the run's own new ticket, ZOM-581 (written at opus · event 493). The fix is in `/create-scenario --revise` S6b: the expected key set is the static cohort plus qualifying tickets the run creates during the gate (matched to its `linear_create_issue` result), never unrestricted extra keys.
- The same allowance must reach the rubric's register-scope row later.

## 8. Why Opus passed

`hardness_v2_check.py` on rev1 (advisory; `run_forensics/rev1/precheck.v2_check.txt`):

| Check | Result |
|---|---|
| SAME_PLACE | CLEAN: 5 traps with two or more version records, 0 flagged |
| DONE_CHECK | CLEAN: an A24 / done-gap node exists |
| TWO_DECISIONS | CLEAN: cross-source rules decide 6 requirements |
| DECISION_FLIP | CLEAN: 7 of 7 rules can flip a weight-5 slot |
| INPUT_CHECK | CLEAN: 0 weight-5 totals |
| FILTER_CHECK | CLEAN: an in-scope item sits outside the obvious filter |
| RULE_IN_PROMPT | CLEAN |

**The static check was clean, and every trap still leaked.** The v2 failure kind per settled trap, read from the call ledger:

| Trap | v2 failure kind | Why it was never out of the way |
|---|---|---|
| T1 ZOM-569 | `same_container`: the timing was on the ticket itself, plus a bulk commit list | `cmt_zom569_1` at 21:40Z dated the fix after the cut, and the commit list carried the 21:36Z change |
| T2 ZOM-567 | broad sweep | Post-candidate Slack is fully swept (66/66). Douglas's "stays on dev" and Arthur's withdrawal sit after the run's date floor, by authors it searched (`from:douglas`) |
| T3 ZOM-435 | `on_delegation_path` | ZOM-570 says "I'm putting the reuse rule on the tech-issues card", and that card holds the re-test |
| T3b ZOM-473 | broad sweep | Brian's DM comes back in the post-candidate Slack sweep |
| T4 update path | broad sweep then pointer | Brian's own DM points to his doc, and Drive by owner and date finds it |
| T5 ZOM-562 | broad dated sweep | The mail is dated inside `after:2025/09/29` |
| T6 scope | first-read | The rule is verbatim in the doc ZOM-570 delegates to; v2 Part 4 "clear calls from visible evidence" |
| T7 ZOM-563 | broad sweep | The Douglas DM is read from Sep 29 |
| T12 ZOM-559 | per-ticket read on a bug-looking ticket | The comment-reading habit covers it |

**Heavy rows that passed (weight 5):** S01, T01, S03, T02, S05, T03, S07, T05, B01, S09, T04, S11, S12, S13, S14. That's all 15. These are the parts Opus 5.5 finds easy. The rebuilds must not add more of them; they must move the decision behind a carrier this run didn't open.

**What the completed tasks show beats Opus 5.5** (explore subagent `ses_e58b2fcdfffedWBoZAaZqNgQqn`, checked against each task's SQL and verifier results):

| Carrier that landed | Task | Miss rate | Why runs missed it |
|---|---|---|---|
| Inline review comment under an APPROVED review with an empty body, on a backend PR | Douglas (`match3d-backend#38/#39/#46`, SQL L146/L178/L398) | 5/6, 5/6, 6/6; about 20 % of 20 runs read inline comments | The empty APPROVED review reads as conclusive; runs read reviews and issue comments, not `github_get_pull_request_comments` |
| Reply-all deep in a Gmail thread the anchor names | Douglas (SQL L82) | 5/6 | `gmail_get_message` on the parent; only `gmail_get_thread` returns the reply |
| Post-merge PR review | Julia DD (SQL L49/L52/L56) | 5/6 | Runs stopped at the Linear notes |
| DM thread reply under an older parent | Julia ZM | 5/6, then 1/6 | `slack_read_channel` returns parents only |
| Notices re-dated so each run's own date window caught a different subset | Frederick handover | about 50 % find rate | SD went from 0.05 to 0.161 |

- **What didn't land:** judgment calls on visible evidence (Julia ZM: 0 landings in 28 runs), rules in records every run opens, same-thread corrections, and anything on a delegation path. Volume alone (dd-2024: 1,002 calls, 100 %) also failed to bring scores down.
- **What drives spread:** SD rose above 0.1 only when three or more carriers had partial find rates (about 0.4–0.6) and each decided at least about 10 % of the weight (Douglas: about 60 % over 3 habits, SD 0.117). A single all-fail carrier lowers the mean but flattens the spread (Robert, Julia DD).

## 9. Purge list (proposed; S0r decides)

| Item | Kind | Action | Evidence |
|---|---|---|---|
| R_UPDATE_RULE as a loss channel | FALSE | Keep B01 as a core write, but don't count the rule in projections or the mechanism portfolio | No ablation changes a value (mutation EQUIVALENT); opus · events 394–400 |
| `cmt_zom569_1` timing (21:40Z "fix is on main now") | LEAKED, not live | Rebuild per §10 R2 | opus · event 159 |
| Arthur's #zombie-ops withdrawal (`C08R6BF4ENN/1759261800.335275`) and Douglas's reply (`/1759262520.892033`) | LEAKED in the post-candidate sweep | Delete them, with their thread fields; rebuild per §10 R1 | opus · events 294, 301, 386 |
| Decoys never on the path: Jul 27 doc `f_5ae4332fb6927f84b3afdc`, K7 invite, K11 | FALSE as decoys | Keep them for realism, but don't count them as traps | `node_verdicts` reach: NOT-READ |
| T3 / T3b / T5 / T7 / T6 / T12 | LEAKED; every one is a check on the candidates, so it can't move before the run's date floors | Keep them as they are. Each still grades a real decision and none can be hidden fairly | §8 |

## 10. Proposed rebuilds (candidates for `/create-scenario --revise` S5a)

These are all Hardness v2 moves (§13.4): a correction moved out of the obvious place, a "done" source with a missing piece elsewhere, or an in-scope item outside the obvious filter. **No new rows, tickets, deliverables, steps or volume, and no prompt change.**

An independent review (oracle `ses_e589d1388ffe08iN7IefADFhHF`) checked each move. Its repairs are folded in below; it rejected the set as first drafted ("not decision-grade") for the reasons in the arithmetic at the end of this section.

### R1 — ZOM-567: deployed, but missing a piece on prod (v2 Part 3 #1, Part 9 example 2). Priority 1.

- **"Done" source, made believable:**
  - match3d-backend#36 merges before Douglas deploys. Arthur's APPROVED review keeps an empty body.
  - Douglas posts in D079SNE2TL4 **after 21:58Z** that "the #36 container/code is deployed". The later time means Vincent's 21:58Z "Yep it works as expected" can't be read as a check of ZOM-567, because it answers the 18:16Z teams/social deploy for ZOM-563.
  - `cmt_zom567_1` stays ("fix is in match3d-backend #36, merged"), so the ticket points to the PR.
- **Missing piece:** an **inline** review comment by Arthur on #36 (`github_review_comments` under the APPROVED review), dated after the rollout. It says ZOM-567's reward rows are still dev-only, the grant path isn't active on prod, claims still don't add the items, and the prod import waits until after the store push.
  - The oracle's repair: the comment must state the later prod state, not just a plan.
  - Grounding: the base backend code, not the Confluence page (SC-45): `rel/overlays/bin/server` runs `./zombies_game eval ZombiesGame.Release.migrate` on every container start (Dockerfile `CMD ["/app/bin/server"]`), so the migration's empty table exists on prod, while base `mix.exs` line 91 keeps seeds and data on `ecto.setup` only, so the load that fills it never runs on start; `page_cicd_pipeline` ("Run by hand") still carries the by-hand deploy, and `page_aws_infra` the escalation to Arthur.
- **Deciding rule:**
  - Leonard's doc: "Done in Linear or a dev saying fixed isn't enough".
  - Arthur's doc: "Merged is not live".
  - How we gate: "a server-side fix always takes a server value".
  - Result: BLOCKER, server - not live (truth unchanged).
- **Why this run's habits miss it:** 0 PR review or review-comment reads in 151 calls. match3d-backend has no Slack copy (INT-01 covers match3d only), so the post-candidate sweep can't return it.
- **Reachable:** `github_get_pull_request_comments` on #36. Douglas's runs on the same match3d-backend surface used it (`douglas_beta_server_signoff_2026-10-28/task_inputs/Working_Files/01a_Hardening_Report.md` line 232), which shows the tool returns the inline body in this harness.
- **Slots:** S03 and T02 (10 points).
- **Expected miss rate:** about 0.75 (Douglas 5/6–6/6).
- **Removes:** the withdrawal and the reply (§9).

### R3a — ZOM-458: a minor-looking symptom that actually loses a reward; the correction is in an older DM (v2 Part 3 #2). Priority 2.

- **Change:**
  - Brian posts a top-level message in D0770ET1HV2, a five-member group that includes Vincent, on **Sep 29**, on a build available that day. It names ZOM-458 and says quitting without winning advances the saved level and marks its chest claimed, nothing is added to inventory, and relaunching doesn't restore it.
  - Vincent's seeded #135 comment `cmt_zom458_1` becomes the oracle's continuity wording: "same repro and saved-state / reward outcome on #135 / #50 as Brian's Sep 29 check".
- **Deciding rule:** "lost … items" is a blocker, and "call it on how bad it is whatever the ticket says". The call moves from KNOWN ISSUE to BLOCKER. Adds slots S(ZOM-458) and T(ZOM-458 on ZOM-570).
- **Why this run misses it:** the Brian DM was read only from Sep 30 02:40Z (opus · event 394), and the run never searched Slack for a ticket key.
- **Reachable:** `slack_search` "ZOM-458", or reading Vincent's own DM history back one day.
- **Stronger variant (recommended):** the same Sep 29 message names a **second** open KNOWN ISSUE ticket whose seeded check is neutral (S5a picks from ZOM-535, ZOM-520, ZOM-556, ZOM-468 after a full read). Then one record decides 20 points. That's the Douglas L2 shape (one reply decided three tickets), and it's what lifts the spread.
- **Expected miss rate:** about 0.55.
- **Check C to verify:** the message is dated after each ticket's creation and on a build that existed on Sep 29. No base record calls the effect cosmetic. Grounding: `ground_P3_P4.md` §P3; the base DM has 144 messages on Sep 29 and threads are common there.

### R3b — ZOM-293: an in-scope bug outside the obvious filter (v2 Part 3 #7; the oracle's "single best data change"). Priority 3.

- **Change:**
  - ZOM-293, "Dynamic Difficulty Tiering Down Issue", is open (Todo). Its description only repeats the title, so it's NO CALL today under "a ticket that doesn't say what goes wrong". Vincent created it, and the run judged it from the description alone at opus · event 436 (`linear_get_issue`) without reading its comments.
  - Add Vincent's own comment as the reporter, dated **Jul 2025**, soon after he filed it, so `updated_at` stays far down the newest-updated-first list. The comment says what goes wrong: e.g. after the tier drops, the level reloads and the boosters and lives already used are gone.
- **Deciding rule:** the ticket now says what goes wrong. Lost boosters or lives is a blocker. The call moves from NO CALL to BLOCKER, build status n/a (an open bug nobody re-tested).
- **Why this run misses it:** it read comments only on bug-looking tickets (0 of the 86 NO CALL rows), and ZOM-293's title and description read as design.
- **Reachable:** `linear_list_comments` on ZOM-293, a register ticket. Reading every register ticket's comments is the gate's ordinary per-record work.
- **Fork to close in S5a:** "difficulty tiering is a design/tuning area, so no call". The comment must describe a defect (lost items), not a tuning wish. Settle the reading in the two-reading table.
- **Expected miss rate:** about 0.5.

### R2 — ZOM-569: closed before the cut, fixed after it (v2 Part 3 #1 / #4; the hardness report's suggestion 1). Control-weight only.

- **Change:**
  - Oliver's comment becomes "fixed locally, the join popup only opens one SP screen now", dated before 18:43:32Z.
  - `completed_at` and `updated_at` move before both Started lines.
  - The 21:40Z comment is removed, keeping the lifecycle check clean.
- **Deciding record:** base #builds Android #2028 / iOS Internal #1759 (21:36Z, "Fix season pass main screen instance from join popup"). How we gate: "if nothing shows when the fix landed, go by when the ticket was closed"; here something shows.
- **Decoy:** base PR #473 "Addressables/sp" (merged 15:41Z). Don't call it the fix: its summary is about asynchronous loading.
- **Expected miss rate:** low, about 0.25. The oracle notes the run found the 21:36Z change through its own commit sweep (opus · event 179). Don't count on it.

### R4 — ZOM-435 re-test moved to the "[Feature] Trophy Path" card (`6851a72836c07bf96717ffd2`). Not recommended as a loss channel.

- The run's board-actions call (opus · event 356, result 357) returned every post-Sep 22 comment on that board. A comment on another card of the same board comes back in the same call.
- If S0r moves it anyway, use the oracle's wording ("Android Submission #135") and update both cards' comment counts and activity.

### Arithmetic

| Move | Weight | P(miss) | Expected loss |
|---|---|---|---|
| R1 | 10 | 0.75 | 7.5 |
| R3a (two tickets in one message) | 20 | 0.55 | 11 |
| R3b | 10 | 0.5 | 5 |
| R2 | 10 | 0.25 | 2.5 |
| Residual on the 15 weight-5 rows that leaked | — | — | about 3 |
| **Total** | **≈ 138** (the 108 surface plus 30 new slot weight) | | **≈ 29** |

- That's about **79 %** expected. With R3a on one ticket only, it's about **81 %**.
- Independent channels give an SD of about 0.09. Habits that move together, which is what Douglas measured, push it above 0.1. That is unproven.
- **So the set reaches the < 80 % target only if the miss rates hold.** This is uncalibrated, and the oracle's verdict on the first draft was "do not represent the set as meeting < 80 %".
- **Decision rule for S0r:** if R3a can't carry two tickets fairly, S5a needs one more carrier that this run's habits miss, before the revision ships. The candidates are a second backend PR inline comment, or an in-scope NO CALL ticket that actually describes a defect.
- **Calls:**
  - Every rebuild sits behind a per-record read: PR comments for each Done fix, comments on every register ticket, ticket-key Slack searches. So a run that finds the deciding records needs about 230–280 calls.
  - A run as economical as this one stays near 130–141 and loses points.
  - The platform measures the horizon on the golden run, or else the average. So keep the > 130 target as a per-run expectation, not a guarantee; the oracle confirms one 141-call run sets no floor.
  - Never add calls to reach it.

## 11. Routing (proposed; S0r decides)

- **Universe changes** go to `/create-scenario --revise` (S5a, `design_delta`), then `/create-injection` as rev2, then `/injection` and `/prompt`. Facts they change:
  - **R1:** #36 merge time, timeline, PR-commit and repo push time. Douglas DM (+1 message). `github_review_comments` (+1 row). Delete `C08R6BF4ENN/1759261800.335275` and `/1759262520.892033` with their thread fields. Re-point the evidence in `truth.json` for ZOM-567.
  - **R2:** ZOM-569 `completed_at` / `updated_at`; `cmt_zom569_1` text and time.
  - **R3a:** Brian DM (+1 message); `cmt_zom458_1` text (and the second ticket's comment). Truth: ZOM-458 (and the second ticket) KNOWN ISSUE → BLOCKER. ZOM-570 blocker set grows from 15 to 16–17.
  - **R3b:** +1 Linear comment on ZOM-293, plus its `updated_at`. Truth: NO CALL → BLOCKER.
  - **Surface (S6b):** new S and T slots for ZOM-458, the second ticket and ZOM-293; the V01 allowance (§7). Freeze the slot map before any forecast.
- **Prompt-side defects:** none. The prompt scored 5 on `/prompt` and the run shows no prompt leak. It points to a natural start (ZOM-570) and states no rule, so it stays unchanged.
- **OE / rubric:** none written yet.
  - `/create-oe-writing` must use the rev2 records (Arthur's inline comment, Brian's Sep 29 DM, Vincent's ZOM-293 comment).
  - `/create-rubric-writing`: one condition per row, and weight 5 on the R1 / R3a / R3b rows. The scope rows must stay well under the 40 % share the platform flagged as a failure-pattern risk. The register row needs the self-filed-ticket allowance.
  - No row may predict an all-fail.

## 11a. Revision status (after `/create-scenario --revise` and `/create-injection`)

This report's forensics cover rev1 only: the export stays bound to `run_forensics/rev1/` (a copy is at `run_forensics/rev1/precheck_trajectory.json`). rev2 implements §10:
- R1, R2, R3a (on two tickets, ZOM-458 and ZOM-535) and R3b are in; R4 was not done.
- R_UPDATE_RULE is purged as a solver rule, and V01 now expects ZOM-581.
- The oracle's UGT fork on ZOM-567's build status is closed by rewording How we gate's server definitions.

rev2 is SQL sha256 `74a7f6a4f51d…`, stored at `run_forensics/rev2/`; the change list is in `run_forensics/rev2_design/REV2_CHANGES.md` and the design's §15 intake.
- Every local gate passes: scenario, injection, error-async, prompt-writing, prompt-check, sql_lint, base_check, base_claims, fact_check, hg.py lint, hardness gate, solver contract (with regression on rev1), mutation, preflight and v2.
- Graded on the rev2 surface (33 slots / 135), the rev1 run's own writes score 77.8 %.
- A new platform `/injection`, `/prompt` and Opus pre-check are needed. This report gets re-run on that export.
- Platform round on SQL `11e4fbbbfed9`: `/injection` PASS, `/prompt` FAIL 2. The failure was Cross-Service Coherence: Arthur's #36 comment repeated Confluence's "migrations don't run on boot" against the base `rel/overlays/bin/server`, which is SC-45. The comment now says the chest rows come from a hand-run load that hasn't been run on prod. No truth, slot or mutation value changed.
- Platform round on SQL `6b6a3793b01f` (r16): `/injection` PASS, `/prompt` FAIL 2 (Cross-Service Coherence: the update-path doc's 1.3.24 'current store build' label, P2-DR1; Leonard's 'every ZM store submission' cadence vs the ungated iOS #49 release, P2-DR2). r17 relabels the rows N-1 / N-2, drops the cadence clause, and from the sibling sweep fixes ZOM-576's reward and the vendor's old-name wording. No call, slot weight or mutation value changed.
- r17 gates were re-run on 2026-11-05 after `Task_Authoring/tools/hardness_gate.py` changed in another session (an optional `volume_exception.rows_floor`; not used here). The hardness gate still passes on the design and the SQL (tools hash `9b78441396d8`).
- Platform round on SQL `74a7f6a4f51d` (r17): `/injection` PASS; `/prompt` FAIL 2. Coherence scored 5 again, but Unique Ground Truth and Clarity scored 2 (P1-DR1): ZOM-435 / ZOM-473 build status could be in candidate or n/a. r18 (`5a8d995238f3`, gates re-run after the dossier rebuild) adds ", even if the re-test still shows the bug" to How we gate's "in candidate" clause. Truth and mutation results are unchanged.
- r17 regression check against r16: five SQL statements changed. Truth changed only ZOM-576's title (18 / 19 / 10 / 85 calls unchanged); mutation verdicts and geometry are unchanged; the solver contract passes, with 0 field differences on rev1's SQL. The rev1 run's writes, replayed on the r17 surface, still score 77.8 %.

## 12. Self-review

Counter-readings, one per LEAKED or FALSE verdict plus the band, each resolved with a pointer:

| # | Verdict | Strongest counter-reading | Resolution |
|---|---|---|---|
| 1 | T1 LEAKED | Never live (FALSE), since the ticket's own comment gave the timing | Partly true. It was live only for a run that skips ZOM-569's comments or the commit list; this one did both (opus · events 159, 179). Kept as LEAKED because the decision was real, and rebuilt in R2. Natural query → correction, met in the same container as the claim |
| 2 | T2 LEAKED | Tool: did the run get the withdrawal by luck? | No. The `from:douglas` search (opus · event 294) and the complete 66-message sweep (385/420) both returned it. Claim (#36 merged, event 173) met before the correction (294) |
| 3 | T3 LEAKED | Never live: the correction came before the claim | Yes. Read at opus · event 38, before Vincent's #133 pass at 110. Delegation path, so FALSE-like. Kept, because the call is still a real decision; not counted as a loss channel (§9) |
| 4 | T3b LEAKED | Did a bulk call carry it? | Yes: the `-in:#builds` sweep (opus · event 386) returned the DM text. LEAKED |
| 5 | T4 FALSE | Should it be LEAKED? | No ablation changes a value (mutation EQUIVALENT), so as a mechanism it's FALSE. B01 was met at opus · event 462 |
| 6 | T5 LEAKED | Was the decoy (known-issue ZOM-562) ever live? | The mail came back in a dated sweep (event 327), and the run mapped it by content (346). LEAKED |
| 7 | T6 LEAKED | Rule stated verbatim where the agent reads first? | Yes (event 34). Grade it, but don't count it as hardness |
| 8 | T7 LEAKED | Could the run have missed it? | It read the DM from Sep 29 (event 303). LEAKED |
| 9 | T12 LEAKED | Same-ticket supersession, so never live | Yes: the per-ticket read at event 245. LEAKED. A sample row, not a loss channel |
| 10 | V01 CONFOUNDED | A real scope error? | No. Leonard's sentence requires the self-filed key (opus · event 34), and the run filed ZOM-581 (event 462). Grader fix in §7 |
| 11 | Band 1 vs 2 | Do M1/M2 matter? | Neither touches a graded value (ZOM-581's call and blocker status are right; the reply's mention was not asked for). Band 1 stands (§3) |

- **Neighbouring band:** argued in §3 and row 11. No CONFOUNDED failure is counted (V01 is excluded), and no cascade is counted twice.
- **Write payloads grepped for designed flags:**
  - Register: 0 differences across 132 keys (opus · event 493).
  - ZOM-570: 16 keys (event 496).
  - New ticket fields: event 462.
  - Reply: NO-GO in the thread (event 499).
- **Re-verified records with `tools/hg.py`** (`run_forensics/rev1/precheck/reverify_hg.txt`):
  - Base #builds iOS Internal #1759 / Android #2028 "Fix season pass main screen instance from join popup" (`C05433XK267/2025-09.json` /1131, /1132).
  - Android Submission #135 Started (/1122).
  - Douglas DM "updated the prod environment with the latest teams/social changes" (/263) and "Yep it works as expected" (/265).
  - PR #473 "Addressables/sp" (github /pull_requests/2378).
  - The Trello card "[Feature] Trophy Path" (/cards/703).
  - ZOM-458 (/issues/3527) and ZOM-435 (/issues/3502).
  - Seeded deciding records (cmt_zom569_1, cmt_zom567_1, the #36 rows, `68dc63484a5b2d0a869e758f`, the withdrawal, `cmt_zom458_1`) were re-read in `01_Universe_Inject.sql` lines 8–31, 116–117, 273–291.
- **Mechanical re-runs:**
  - `trajectory_ledger.py`, `node_verdicts.py` and `surface_grader.py` were each run once on unchanged inputs.
  - `hardness_v2_check.py` was run on rev1.
  - The posterior forecast is pre-registered (`hev_a821dfc67699e7d6`).
  - `difficulty_stats.py` was not run: there's no rubric matrix.
- **Unresolved:**
  - (a) The §10 miss rates are uncalibrated estimates.
  - (b) A second ticket for R3a hasn't been selected.
  - (c) R3b's design/tuning fork must be settled in S5a.
  - (d) No independent check of the inline-body return in this exact harness beyond Douglas's runs.
  - (e) The oracle ran out of steps before checking an instantiated R3b.
  - CONFOUNDED findings are not softened: V01 stays a grader defect.

```
STAGE GATE hardening: PASS — Task_Authoring/task_inputs · 01a_Hardening_Report.md#795a1564ad1b · 01_Universe_Inject.sql#5a8d995238f3 · 01_Hardness_Manifest.json#01a3caa4a5bf · 00_Assigments.md#90d69427cab7 · 01_Grounding_Dossier.md#4f38db93303c · 06_PreCheck_Trajectory#ca58545f44a7 · 07_Baseline_Trajectories#ad7848c1ad99 · 10_Baseline_Verifier_Results.md#e3b0c44298fc · __context__#fb209f3058d7 · __assignment__#c2f3888d53bd · __policy__#dc4ab5df3cdd · __gate_policy__#9b78441396d8 · __review__#4c88e8308ed5 · blocking 0 · warnings 0 · checks 17
[PASS] assignment.v3_context: Vincent Parker / Game Systems Engineer; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 01a_Hardening_Report.md
[PASS] structure.inputs: 2 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 06_PreCheck_Trajectory, 07_Baseline_Trajectories, 10_Baseline_Verifier_Results.md)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#5a8d995238f3, 01_Hardness_Manifest.json#01a3caa4a5bf, 01_Grounding_Dossier.md#4f38db93303c, solver/solver.py#f7a6aeed38d8, 01c_Dispositions.json#0d69abd8f7ab, 01c_Preflight_Report.json#8fb3c8b8c94d, 00_Assigments.md#90d69427cab7, 01_Scenario_Design.md#087cccf519b5, 01_Hardness_Manifest.draft.json#35516411430b, 01_Gradable_Surface.json#e3001f0c8fa4, __context__#fb209f3058d7, __assignment__#c2f3888d53bd, __policy__#dc4ab5df3cdd, __gate_policy__#9b78441396d8, __review__#4c88e8308ed5)
[PASS] structure.sections: 6 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] structure.placeholders: no placeholders in 01a_Hardening_Report.md
[PASS] structure.mode: MODE B declared
[PASS] evidence.register_run_step: 11/11 items carry a source pointer (min 100%)
[PASS] structure.sections: 4 required sections present and non-empty (01a_Hardening_Report.md)
[PASS] revision.injection: injection checks re-run on revision N+1 (current SQL + manifest + dossier): PASS
[PASS] review.counter_readings: 11 evidenced counter-readings (of 12 found; need ≥ 11) in 01a_Hardening_Report.md
[PASS] review.coverage: self-review addresses all 2 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```






## 13. Next steps

1. `/create-scenario --revise` (S0r): disposition these verdicts, decide the purge, and design R1, R3a (two tickets if fair), R3b and R2 in S5a. Settle every fork in the two-reading table, then rebuild the surface (S6b) with the V01 allowance.
2. `/create-injection` as rev2. Store rev1 already sits in `run_forensics/rev1/`. Run all gates (sql_lint, base_check, hardness_gate, hg.py lint, solver contract, mutation and preflight).
3. The platform `/injection`, then `/prompt` (the prompt is unchanged, but the universe changed).
4. A new unhinted Opus 5.5 pre-check, then `/create-hardening` again. Go to the baseline only if `/hardness` ≥ 3 and at least 2 loss channels land. This is the second and last pre-check this scenario allows.
