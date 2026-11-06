# rev2 change list (single source of truth for the doc updates)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Generated SQL: `Task_Authoring/task_inputs/01_Universe_Inject.sql` (rev2, 130 inserts + 29 updates; stored at `Working_Files/run_forensics/rev2/01_Universe_Inject.sql`). rev1 (platform pre-check, `/hardness` score 1) stays stored at `Working_Files/run_forensics/rev1/` with its artifacts.

Why: the rev1 Opus 5.5 pre-check solved everything (`Working_Files/01a_Hardening_Report.md`). Every correction sat on a delegation path, in a post-candidate sweep (Slack after Sep 30 18:30Z, Gmail after Sep 29), or in a comment on a bug-looking ticket. rev2 moves deciding facts to places that run never read: a backend PR's inline review comment, an older group-DM message, and a comment on a ticket that doesn't look like a bug. There are no new tickets, rows, deliverables or steps, and the prompt is unchanged.

## R1 — ZOM-567 (T2, rule R_DONE_SERVER): deployed, but a piece is missing on prod
- **Deleted:**
  - Arthur's #zombie-ops withdrawal `C08R6BF4ENN/1759261800.335275`.
  - Douglas's reply `C08R6BF4ENN/1759262520.892033` ("ok, #36 stays on dev for now").
  - After this, the SQL has no #zombie-ops rows at all.
- **Changed:**
  - Arthur's APPROVED review `harmonygames-Games/match3d-backend#36#rev_1` (18:42Z) now has an empty body; it was 'lgtm'. All 30 base APPROVED reviews on match3d-backend have empty bodies.
  - PR #36 `updated_at` → 2025-09-30T22:40Z.
- **Added:**
  - Douglas's message in DM D079SNE2TL4 at ts `1759269712.483915` (2025-09-30T22:01:52Z, between Vincent's 21:58:44Z "Yep it works as expected" and Douglas's 22:05:03Z "Go to sleep"): "fyi #36 is rolled out to prod too, the container is up. that's the code side". This is the "done" source.
  - Arthur's COMMENTED review `…#36#rev_2` (22:40Z, empty body, commit = #36 head).
  - Arthur's inline review comment `harmonygames-Games/match3d-backend#36#rc_1`, at 22:35Z on `priv/repo/data/load_zombie_lane_chest_rows.exs` line 2 (a new file the PR adds; its header says "Loads the chest rows the Zombie Lane grant reads. Run by hand per environment"): "checked prod after Douglas rolled this out: claimed a chest on my prod account and nothing landed. the migration only creates the empty zombie_lane_chest_rows table, the rows the grant reads come from this load, which runs by hand per environment and hasn't been run on prod. so the new grant path does nothing on prod yet. I'm holding the prod load until after the store push". The wording follows the base backend code: `rel/overlays/bin/server` runs `./zombies_game eval ZombiesGame.Release.migrate` on every container start (Dockerfile `CMD ["/app/bin/server"]`), and base `mix.exs` line 91 keeps seeds and data on `ecto.setup` only.
  - A timeline event "reviewed (commented)" at 22:40Z.
- **Grounding:**
  - The base backend code, not Confluence: `rel/overlays/bin/server` runs `./zombies_game eval ZombiesGame.Release.migrate` on every container start (Dockerfile `CMD ["/app/bin/server"]`), so the migration's empty table exists on prod; base `mix.exs` line 91 keeps seeds and data on `ecto.setup` only, so the load that fills it never runs on start.
  - `page_cicd_pipeline`: deploy "Run by hand", "CI stops here".
  - `page_aws_infra`: data migrations escalate to Arthur.
  - How we gate: "server - not live" = a server-side fix with any part not on prod yet, even if its code is deployed; "server - live" includes any migration or data it needs.
  - `page_backend_services` stays a base page but is not a resolver: its "Migrations do not run on boot" contradicts the container start script (SC-45).
  - match3d-backend is not mirrored to Slack (INT-01), so no Slack copy of the inline comment exists and the post-candidate Slack sweep can't return it.
- **Truth unchanged:** ZOM-567 BLOCKER, server - not live.
- **Natural wrong reading:** Done, plus approved, merged and rolled out, means fixed (not re-checked) and server - live.
- **Why the rev1 run would miss it:** it never read a PR comment or review (0 of 151 calls).

## R2 — ZOM-569 (T1, rule R_DONE_BUILD): closed before the cut, fixed on main after it
- **Changed:**
  - ZOM-569 `completed_at` / `updated_at`: 21:45Z → **18:05Z**, before both Started lines (iOS #50 18:43:32Z, Android #135 18:45:34Z).
  - Oliver's `cmt_zom569_1`: 21:40Z "fix is on main now…" → **18:02Z "fixed on my branch, the join popup only opens one SP screen now"**.
- **Deciding record (base, unchanged):** #builds Android #2028 (21:36Z) / iOS Internal #1759: "Fix season pass main screen instance from join popup". How we gate: go by the close time only if nothing shows when the fix landed.
- **Decoy (base):** PR #473 "Addressables/sp" (merged 15:41Z), which is season-pass async loading, not this fix.
- **Truth unchanged:** BLOCKER, not in candidate.

## R3a — ZOM-458 and ZOM-535 (new trap T16, new rule R_OLD_NOTE, mechanism A14): worse than they look, in an older DM
- **Added:** Brian's top-level message in D0770ET1HV2, a five-member group DM with Vincent and Brian, at ts `1759160460.731000` (**2025-09-29T15:41Z**, on #133 / #49; earlier than the run's DM read floor of Sep 30 02:40Z and its Slack date floor of Sep 30 18:30Z). It's in Turkish:
  - ZOM-458: quitting an algo level without winning marks the level passed and its chest claimed, nothing lands in the inventory, and relaunching doesn't restore it. That's lost items, so **BLOCKER**.
  - ZOM-535: at 120 cpm the boss-arena nuke goes to a dead zombie, the boss takes no damage and the arena can't be finished in 3 tries. That's can't finish a level, so **BLOCKER**.
- **Changed (Vincent's Sep 30 re-checks, same ids and times):**
  - `cmt_zom458_1` (21:06Z) → "Still there on #135 / #50: quit an algo level without passing and the home screen plays the level-pass animation, same as Brian found on #133 / #49."
  - `cmt_zom535_1` (21:42Z) → "#135: fast matching still sends items at a zombie that just died, same as Brian found on #133."
  - Each keeps the visible symptom, which is the natural reading, and points to Brian's finding for continuity: the outcome is the same as his.
- **Deciding rule:** Leonard's doc: "call it on how bad it is whatever the ticket says"; lost items and can't finish a level are blockers.
- **Truth:** ZOM-458 KNOWN ISSUE → **BLOCKER**; ZOM-535 KNOWN ISSUE → **BLOCKER**. Build status n/a; QA result "reproduces on #135 / #50" and "reproduces on #135".
- **Controls:** ZOM-481 and ZOM-427 stay KNOWN ISSUE (over-application operator `over:every-cosmetic-is-worse`).
- **Natural wrong reading:** the ticket text and the latest check read cosmetic, so known issue.

## R3b — ZOM-293 (new trap T17, new rule R_SYMPTOM_NOTE, mechanism A17): an in-scope bug outside the obvious filter
- **Added:** Vincent's own comment `cmt_zom293_1` on ZOM-293 "Dynamic Difficulty Tiering Down Issue" (open, Todo, label "30 June", creator Vincent, description just "Dynamic Difficulty Tiering"), dated **2025-07-03T17:42Z**: "what goes wrong here: lost 4 in a row on level 63, it demoted me 1 -> 0 and reloaded into the tier 0 version (the tier drop itself works). but the glue + trampoline I'd picked for that retry were taken from my stock when the level started, and after the reload for the tier change neither was on the board. both gone, 600 coins worth. happened again on my next demotion".
- **Changed:** `updated_at` follows the comment (Jul 3), so it stays far down the newest-updated-first list.
- **Grounding:** ZOM-42 and ZOM-303 (demote and reload to tier 0, shipped in match3d PR #244 on Jun 25); the economy page (Glue 400 and Trampoline 200 coins, pre-level, one use).
- **Deciding rule:** "a ticket that doesn't say what goes wrong" is no call, but this one now says what goes wrong, and lost boosters / coins is a blocker.
- **Truth:** NO CALL → **BLOCKER**, build status n/a (open, nobody re-tested).
- **Controls:** ZOM-311 and ZOM-130 (bare tool and feature tickets) stay NO CALL (`over:every-vague-ticket-is-a-bug`).
- **Why the rev1 run missed it:** it read ZOM-293 only through `linear_get_issue` (event 436), which returns no comments.

## Other rev2 changes
- **How we gate, "build status means" row** (oracle UGT review, ZOM-567): `server - live` = "a server-side fix that's fully on prod, including any migration or data it needs" (was "…deployed to prod"); `server - not live` = "a server-side fix with any part not on prod yet, even if its code is deployed" (was "…isn't deployed"). This closes the server-live / server-not-live fork on ZOM-567. ZOM-563 stays server - live: it is confirmed working on prod.
- **Rule R_UPDATE_RULE removed from the solver and portfolio.** It was FALSE: no ablation changes a value. T4 and CH3 stay as a trap and chain, and B01 stays a core write slot with no mechanism. The solver now has 8 rules (R_DONE_BUILD, R_DONE_SERVER, R_CORRECTION, R_ALIAS, R_FILTER, R_COMPLETION, R_OLD_NOTE, R_SYMPTOM_NOTE).
- **V01** (register keys exact) now expects the 132 truth keys plus `ZOM-581`. That's the first ticket the run files (Linear numbers the next ZOM key), and Leonard's rules give tickets filed during the gate a row. This fixes the rev1 grader defect.
- **Surface: 33 slots, weight 135** (was 28 / 108):
  - Removed sample S23 (ZOM-458).
  - Added exception slots S31 (ZOM-458 call), T06 (release ticket lists ZOM-458), S32 (ZOM-535 call), T08 (lists ZOM-535), S30 (ZOM-293 call) and T07 (lists ZOM-293), all weight 5.
- **Truth:** 18 BLOCKER, 19 KNOWN ISSUE, 10 FIXED, 85 NO CALL (rev1: 15 / 21 / 10 / 86). The ZOM-570 blocker set is 18 keys plus the run's own new ticket.
- **Gates on rev2:**
  - sql_lint 0 errors; base_check, base_claims and fact_check PASS; hg.py lint 0/0/0.
  - check-sql PASS (0 load-bearing rows not visible).
  - Hardness gate (extreme) PASS; solver contract PASS, with regression against rev1 at 0 field differences.
  - Mutation: all 8 rules KILLED. Geometry U 0.8889, L_max 0.5037.
  - Preflight PASS; hardness_v2 all CLEAN.
- **Replay:** the rev1 run's own writes, graded on the rev2 surface, score **77.8 %** (it fails S30, T07, S31, T06, S32 and T08). That's an upper bound for a run with the same habits, because on rev2 the #zombie-ops withdrawal that gave it ZOM-567 no longer exists.
- `github_review_comments` row now carries only `seq` beyond the base columns (pull_request_review_id, side and subject_type dropped: platform /injection advisory 4, not in the schema snapshot).

## r17 (platform /prompt FAIL on r16)

Platform `/prompt` on SQL `6b6a3793b01f` (revision 16) passed `/injection` and failed Cross-Service Coherence (2). The generator is fixed; the SQL is now sha256 `74a7f6a4f51d…` (revision 17). No call, slot weight, mutation verdict or geometry value changes.

1. **Update-path log `f_5e40215b7d4d24b0455412` (P2-DR1).** The "Installed from store" cells now read just `N-1` and `N-2` (were "1.3.24 (N-1, current store build)" and "N-2 (store build before the hotfix)"), and the repro line reads "install the N-1 build from the App Store, play past level 200, install TestFlight 50 over it, launch". Results are unchanged: iOS #50 from N-1 FAIL, save back at level 1 with 500 coins; the other three rows pass. Reason: base shows newer store versions (App Store 1.3.38 by Sep 19 `#zombie-bugs` /860; required versions 0.3.127 / 0.3.40 on Sep 23 `#zombie-match3d` /407; iOS 0.3.49 released Sep 29 `#zombie-match3d` /463), and 1.3.24 is only the Sep 2–3 `release/1.3.24_HotFix` branch. The runbook defines "N-1 and N-2 are the last two shipped store versions", so the role labels need no number. Grounding: `run_forensics/rev2_design/ground_versions.md`.
2. **Slot B01.** The slot is "Filed bug covers the update from the N-1 store build to iOS Submission #50", selector `N-1|0\.3\.49|1\.3\.49|store (build|version)|App Store` (was `1\.3\.24`). The new ticket's expected content: the update from the N-1 store build (the App Store build) to iOS Submission #50 resets progress (level 1, 500 coins); device iPhone 13, iOS 18.6, source build N-1 (App Store), repro steps.
3. **Leonard's "ZM submission rules" `f_632c44650df44fe252ee59` (P2-DR2).** The first sentence now reads "After the orange juice one on Sunday I want the gate tighter, not just the Bug view in Linear." (dropped "for every ZM store submission from now on"). Reason: base shows five submissions released ungated between the Sep 22 gate and Sep 30 (Android #129 / #131 / #133, iOS #48 / #49; iOS 0.3.49 released Sep 29), so a cadence claim contradicts base. Scope ("the last gate's builds … Android #127 / iOS #40 on Sep 22") is unchanged. Grounding: `run_forensics/rev2_design/ground_ios49.md`.
4. **Sibling sweep (`run_forensics/rev2_design/sibling_sweep.md`).** ZOM-576 is retitled "Season Pass premium tier claim drops the booster bundle", with description "Tier 12 premium reward on iOS #50 (sandbox purchase) is a booster bundle plus gems: claiming shows both reward animations but only the gems land and the tier is marked claimed, so the boosters are gone." (was two chests; the Confluence page_season_pass_spec tier band 11-20 premium is "Booster bundles + gems", and "No Season Pass purchase has been recorded yet", so the purchase is a sandbox one). The call stays BLOCKER (lost boosters). The vendor email (Cobalt Playtesting, Sep 30) now says "Puzzles vs Zombies (still the name on our test plan)": the game was renamed Zombie Match 3D on 24 July 2025, and the old name stays because trap T5 maps an external report under the old name to ZOM-562.
5. **Solver.** Seeded tickets' titles are now read from the SQL (`load_state` collects `linear_issues` titles), so the regression check against the rev1 SQL stays at 0 field differences. Only ZOM-576's title changed; the calls stay 18 BLOCKER / 19 KNOWN ISSUE / 10 FIXED / 85 NO CALL, and the mutation verdicts and geometry are unchanged. All local gates pass. `seq` stays on `github_review_comments`: injection advisory 3 is rejected because the live schema `universe_schema_live.json` marks `seq` NOT NULL with no default, and the completed tasks `douglas_beta_server_signoff` and `julia_zm_difficulty_baseline` loaded review comments with `seq`.

## r18 (platform /prompt FAIL on r17, SQL 74a7f6a4f51d)
- **What failed.** Unique Ground Truth and Clarity scored 2 (P1-DR1, fork F1). ZOM-435 and ZOM-473 are Done on Sep 22, before the Sep 30 Started lines, and their re-tests on the candidates still fail. How we gate's build status fitted both "in candidate" (the clause "a Done bug whose fix was on main at the job's Started line") and "n/a" ("open bugs that still show up"). Coherence went back to 5, so the r17 version fix held.
- **Fix (one statement, the How we gate tab).** The "in candidate" definition now reads: "… or a Done bug whose fix was on main at the job's Started line, even if the re-test still shows the bug (if nothing shows when the fix landed, go by when the ticket was closed)". It states the general case, not the keys, so the run still has to find the failing re-tests (Leonard's Trello comment on #135; Brian's DM on iOS #50) to call both BLOCKER.
- **No regression.** Truth is unchanged: ZOM-435 and ZOM-473 stay BLOCKER / in candidate; every Done no-call ticket stays n/a ("no-call tickets"). Mutation verdicts and geometry are unchanged, and every local tool passes. SQL sha256 `5a8d995238f3`; r17 is stored at `run_forensics/rev2/platform_reviewed/`.
- **Why our local checks missed it.** The local `Evals/1_Prompt_Eval.md` (Oct 20) predates the platform's ugt-boundary-v1 / ugt-fork-v1 decision sweep, which checks every register cell, build status included, against every rule clause. Before resubmitting, an independent GPT oracle and red team ran that sweep from the platform report's own description.

