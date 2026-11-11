# S7 — Backend config & GitHub tool semantics

Clock: 2025-10-01 00:00 PT (07:00Z). Universe: synth-cut.

## 1. match3d-backend repository tree

**How the tree was read.** `python3 Task_Authoring/tools/hg.py reference routes github` returns only
`data.json` + `root/`; `data.json` array pointers are
`/users,/repositories,/labels,/tags,/releases,/branches,/commits,/commit_map,/pull_requests,/pull_request_commits,/reviews,/review_comments,/pull_request_comments,/timeline_events,/issues`
— there is **no per-commit file list** (a `commits[]` record has 13 keys:
`sha, repo_id, message, authored_date, committed_date, author_login, author_name, author_email,
committer_login, committer_name, committer_email, parent_shas`), and `commit_map` is only
`{repo_id, old_sha, new_sha}` sha renaming. So the tree itself was read from the exported working
copy of the git pack:
`Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/match3d-backend/`
(328 files, `.git` excluded). No git command was run. `match3d-backend` default branch `main`,
`pushed_at 2025-09-29T15:43:53Z` (`repositories[]`); last commit before the clock is
`9623dfea0a` `2025-08-13T17:07:46Z` "Included stats in the player's profile response"
(`commits[]`, newest of the 208 backend commits).

**It is not a CDK-only repo — it is an Elixir/Phoenix app** with the CDK in a subfolder.
Top level: `.check.exs .credo.exs .dockerignore .editorconfig .formatter.exs .github/workflows/check.yml
.tool-versions Dockerfile README.md mix.exs mix.lock docker-compose.yml remote.sh config/ lib/ priv/
test/ rel/ assets/ http-collection/ nakama/ zombies-game-cdk/`.
Sub-trees: `lib/zombies_game/` (events, leaderboards, leagues, plague_race{,.server}, season_pass{,.monthly_server},
win_and_collect{,.group_1_server,.group_2_server,.group_3_server}, endless_monster{,.daily_server,.weekly_server},
boss_arena{,.daily_server,.weekly_server}, daily_reward, chest_reward, zombie_lane, scheduler, rewards, debug, google/sheets),
`lib/zombies_game_web/` (controllers + `schemas/` + `live/admin/`), `priv/repo/migrations/` (18 files),
`zombies-game-cdk/lib/{zombies-game-cdk-stack.ts,nakama-stack.ts,constructs/{database,nakama,util}.ts}`.

### Files that define live-ops event windows / schedules / reward tables

**(1) `zombies-game-cdk/lib/zombies-game-cdk-stack.ts` — the production cron table (one env var per event).**
Clock-relevant quotes (lines 139–200):
- `LEAGUES_SCHEDULE: props.production ? "0 0 * * 1" : "*/30 * * * *",` (139) — comment line 137: `// PROD: every monday at 00:00 AM UTC`
- `PLAGUE_RACE_SCHEDULE: props.production ? "0 0 * * *" : "0 */2 * * *",` (143) — comment 141: `// PROD: every day at 00:00 AM UTC`
- `ENDLESS_MONSTER_DAILY_SCHEDULE: props.production ? "0 0 * * *" : "*/5 * * * *"` (147–149)
- `ENDLESS_MONSTER_WEEKLY_SCHEDULE: props.production ? "0 0 * * 1" : "*/10 * * * *"` (153–155)
- `BOSS_ARENA_DAILY_SCHEDULE: props.production ? "0 0 * * *" : "*/5 * * * *"` (159–161)
- `BOSS_ARENA_WEEKLY_SCHEDULE: props.production ? "0 0 * * 1" : "*/10 * * * *"` (165–167)
- `WIN_AND_COLLECT_GROUP_1_SCHEDULE: props.production ? "0 0 * * 1,2" : "0 * * * *"` (171–173)
- `WIN_AND_COLLECT_GROUP_2_SCHEDULE: props.production ? "0 0 * * 3,4" : "0 * * * *"` (177–179)
- `WIN_AND_COLLECT_GROUP_3_SCHEDULE: props.production ? "0 0 * * 5,6,0" : "0 * * * *"` (183–185)
- `SEASON_PASS_SCHEDULE: props.production ? "0 0 1 * *" : "*/30 * * * *",` (189) — comment 187: `// PROD: every first day of the month at 00:00 AM UTC`
- `DAILY_CLAIM_COOLDOWN_MINUTES: props.production ? "1440" : "5",` (191); `DAILY_STREAK_RESET_MINUTES: props.production ? "2880" : "240",` (193)
- `IMPORT_REWARDS_SCHEDULE: props.production ? "*/5 * * * *" : "*/5 * * * *",` (196–198)
- Sheet names: `ZOMBIE_LANE_SHEET_NAME: props.production ? "Zombie Lane Trophy Path" : "(DEV) Zombie Lane Trophy Path"` (~200).
No EventBridge rule is declared here — the crons are **application-level (Quantum) schedules passed as ECS task environment variables**, not AWS EventBridge rules (`grep "EventBridge\|events.Rule" zombies-game-cdk/lib` returns nothing).
*Last touched (inferred):* no file-level commit data exists (see above), so this is message-based:
PR #2 "Created new env for production" (merged 2025-06-01, branch `create-prod-env`) created the
`props.production ? … : …` split, and PR #14 commit `bd2615e8` "Use env vars to manage schedules"
(2025-06-27) moved the crons into env vars; PR #19 `82fb8995` "Add schedule for daily EMM event"
(2025-07-12) and PR #26 `8b116d77` "Add config for weekly event" (2025-07-11) added the EMM/Arena
vars. Evidence level: **inferred from PR/commit messages** (no path attribution in the export).

**(2) `config/runtime.exs` — the same table as defaults.**
- Leagues `schedule: System.get_env("LEAGUES_SCHEDULE") || raise("environment variable LEAGUES_SCHEDULE is missing.")` (157–173); same raise-pattern for `PLAGUE_RACE_SCHEDULE` (175–181), `ENDLESS_MONSTER_DAILY_SCHEDULE` / `_WEEKLY_` (183–193), `BOSS_ARENA_DAILY_/WEEKLY_` (195–205), `SEASON_PASS_SCHEDULE` (240–247).
- **Hardcoded (no env var needed) Win&Collect windows** — the only literal cron strings in app config:
  `group_1_schedule: System.get_env("WIN_AND_COLLECT_GROUP_1_SCHEDULE") || "0 0 * * 3",  # Wednesday midnight (end of Tuesday)` (214–215),
  `group_2_schedule: … || "0 0 * * 5",  # Friday midnight (end of Thursday)` (216–217),
  `group_3_schedule: … || "0 0 * * 1",  # Monday midnight (end of Sunday)` (218–219).
- Daily login: `daily_claim_cooldown_minutes` (249) and `daily_streak_reset_minutes` (255) are env-driven, defaulted in CDK to 1440 / 2880.
- Quantum import jobs at 276–296, all `IMPORT_REWARDS_SCHEDULE` default `"0 * * * *"`, tasks `ZombieLane/DailyReward/ChestReward/WinAndCollect.import_rewards`.
*Last touched (inferred):* PR #17 "Observability: Send server telemetry metrics to Cloudwatch" is the only
PR with **path-level** evidence for this file (`review_comments[].path = config/runtime.exs`, PR #17,
commits `cb269342` "Refactor cloudwatch telemetry config", `438ac340`, `3fc89e0f`, `c75e8849`, merged 2025-07-08);
the event blocks themselves came from PR #14 (`bd2615e8` "Use env vars to manage schedules"),
#19 (`82fb8995`, `aae86cc8`), #26 (`8b116d77` "Add config for weekly event") — message-inferred.

**(3) `config/config.exs` — Quantum scheduler + Google-Sheets reward sources.**
- `config :zombies_game, ZombiesGame.Scheduler, overlap: false, run_strategy: Quantum.RunStrategy.Local, jobs: [ import_zombie_lane_rewards: [schedule: "0 * * * *", task: {ZombiesGame.ZombieLane, :import_rewards, []}], … ]` (126–150; hourly import of Zombie Lane, Season Pass, Daily Reward, Chest Reward).
- **Reward tables are not in the repo** — they are Google Sheets ranges: `spreadsheet_id: "1UEpyibxuQSB2-ib7UgppYDeeHtmkmM1fhSKNbQ_t_Sk"` with
  `sheet_name: "Zombie Lane Trophy Path", range: "A1:M101"` (93–97),
  `"Season Pass - Free" / "Season Pass - Premium", range: "B47:AE78"` (99–109),
  `"daily gift-day rewards", range: "B47:AE54"` (113–117),
  `"daily gift-Chest rewards", range: "B47:AE51"` (120–124).
  Production runtime passes `"Collect&Win - Day 2"` / `"Collect&Win - Day 3"` (`config/runtime.exs:221–225`).
  ⇒ Daily login, chest, season pass, Zombie Lane, Collect&Win reward **numbers** live in that Sheet, not in git.
*Last touched:* PR #14 (`review_comments[].path = config/dev.exs`, `lib/zombies_game/google/sheets.ex`,
`lib/zombies_game/zombie_lane.ex`, 2025-06-24/27) and PR #17 (`path = config/config.exs`, 2025-07-08) — **path-verified**.

**(4) `lib/zombies_game/scheduler.ex`** = 6 lines, just `use Quantum, otp_app: :zombies_game` — no jobs.

**(5) `lib/zombies_game/leaderboards.ex:292–372` — `default_leaderboards/0`, the per-event record shape.**
`"plague_race" => %{type: :increment, order: :desc, schedule: "0 * * * *", metadata: %{"current_stage" => 1, "event_state" => "active"}}` (297–305) —
note this **hourly** literal conflicts with the prod env `PLAGUE_RACE_SCHEDULE="0 0 * * *"` (CDK 143);
`"season_pass" => %{…, schedule: SeasonPass.config() |> Keyword.get(:schedule), …}` (313–317);
`zombie_lane`, `daily_reward`, `chest_reward`, `endless_monster_daily`, `endless_monster_weekly` (306–327).
Windows are evaluated by parsing the cron on every read: `def get_next_reset_date(schedule) do schedule |> Crontab.CronExpression.Parser.parse!() |> Crontab.Scheduler.get_next_run_date!() |> DateTime.from_naive!("Etc/UTC") end` (278–284).
*Last touched (inferred):* PR #19 `6bdc1ed9` "Add endless_monster mode to default leaderboards", PR #4 `8c40f919` "Reuse Leaderboard tables for PlagueRace events".

**(6) `lib/zombies_game/plague_race.ex` — Plague Race stage table (numbers are in the repo).**
`event_metadata/0` (437–472): stage 0 `"total_level" => 5, "city" => "new_york", "victory_rewards" => [%{"type" => "coins", "quantity" => 60}], "total_players" => 5`;
stage 1 `"total_level" => 10, "city" => "london", … "quantity" => 120`;
stage 2 `"total_level" => 15, "city" => "paris", … "quantity" => 250`;
`"defeat_rewards" => [@defeat_rewards]` where `@defeat_rewards %{"type" => "coins", "quantity" => 60}` (24).
*Last touched:* PR #12 "Adjustment in plague race defeat reward" (commit `d9e7bdb4`, 2025-06-27) and PR #13 "Centralising stage constants to avoid triple edits next time" (commit `aa9b1f54`, 2025-06-27, branch `centralising-stage-constants` = `652621a7…`) — message-inferred but unambiguous.

**(7) `lib/zombies_game/win_and_collect.ex` — Collect & Win three-group windows.** Module doc (lines 3–7):
`- Group 1: Monday-Tuesday / - Group 2: Wednesday-Thursday / - Group 3: Friday-Sunday`;
`current_group/0` (45–95) computes prod group from `hours_since_monday` (`< 48 -> 1`, `< 96 -> 2`, else 3) with `monday_start = DateTime.new!(monday_of_week, ~T[00:00:00], "Etc/UTC")` (64–70); dev cycles every 3 hours. Stage rewards come from `get_rewards()` → Sheets.

**(8) Leagues:** `lib/zombies_game/leagues.ex:240–290` — ten leagues `wood, iron, bronze, silver, gold, platinum, expert, master, lord, king` (241–252), each `%{schema: cron from config, metadata: %{"rule" => "stars"}}`; promotion counts in `config/runtime.exs:157–166` (`promote_count: 5, relegate_count: 5, league_size: 20`, `unlock_level: 21`).

**(9) Quests:** there is no quests module in this repo — quests live in the separate
`harmonygames-Games/match3d-quests` repo (`repositories[]`, `main`, `pushed_at: null`) and the client
(`Assets/Scripts/LiveOps/Quests/`). The only quest surface in match3d-backend is the lifetime
leaderboard `"quests_completed"` (`lib/zombies_game/leaderboards.ex:349–351`).

**Net answer:** yes — there is a natural per-event config: the **cron per event in
`zombies-game-cdk/lib/zombies-game-cdk-stack.ts:139–189` + `config/runtime.exs:157–247`**, and event
windows are *derived* from those crons at request time via `Leaderboards.get_next_reset_date/1`
(`lib/zombies_game/leaderboards.ex:278–284`, `Etc/UTC`).

## 2. match3d client repo

**Answer: no. The Unity client has no per-event config asset with windows or rewards.** All windows
and reward numbers are deserialised from backend JSON at runtime; the only literals in the client are
test-mode overrides.

- Client tree (`root/harmonygames-Games/match3d/`, default branch `main`, `pushed_at 2025-10-01T05:44:17Z`):
  `Assets/ Scripts/…` with `Assets/Scripts/LiveOps/{PlagueRace,Endless,InfiniteBoss,DailyLogin,CollectAndWin,LeaderBoards,Quests,SeasonPass,Profile}` and
  `Assets/Scripts/Backend/APIs/GameAPI.cs` (the API surface). No `*EventConfig*.asset` / event JSON exists —
  `find Assets -name '*Event*.asset' -o -name '*Config*.asset'` returns only
  `Assets/Feel/MMFeedbacks/Editor/Resources/MMFeedbacksConfiguration.asset` and
  `…/MMF_PlayerConfiguration.asset` (both unrelated Feel tooling). The only JSON under `Assets/` is
  IAP/billing/dev-quality/Firebase config (`Assets/Resources/IAPProductCatalog.json`,
  `Assets/Store/Store/Store/IAPPayouts.json`, `Assets/Data/device_quality.json`).
- **Rewards**: `Assets/Scripts/LiveOps/PlagueRace/PlagueRaceStageInfo.cs:12–17`
  `[JsonProperty("victory_coins")] public int RewardCoinsAmount;` / `[JsonProperty("defeat_coins")] …` /
  `[JsonProperty("total_level")] public int TotalLevels;` — i.e. the client just binds the server values
  (60/120/250 coins, 5/10/15 levels from `lib/zombies_game/plague_race.ex:437–472`).
- **Windows**: `Assets/Scripts/LiveOps/Endless/EndlessEvent.cs:283`
  `Blob.EndDate = DateTimeOffset.FromUnixTimeSeconds(response.EndTime).UtcDateTime;`
  (same pattern `InfiniteBossEvent.cs:276`, `SeasonPass/SeasonPassController.cs:202` `EndDate = response.EndDate`).
  `Assets/Scripts/LiveOps/LiveOpsEventBlob.cs:11–12` holds `public DateTime StartDate; public DateTime EndDate;` — filled from responses, never from an asset.
- **Only local literals are test-mode**: `Assets/Scripts/LiveOps/PlagueRace/PlagueRaceEvent.cs:17–18,45`
  `public int EventDurationInMinutes; public int StageDurationInMinutes;` …
  `EndDate = DateTime.UtcNow.AddMinutes(EventDurationInMinutes),` and it is gated by
  `[SerializeField] private bool _testMode;` (line 27, used at 39/106/227/300) — a serialized inspector
  value, not a checked-in per-event table.
- Server config reaches the client through `api/client-info` (`Assets/Scripts/Backend/APIs/GameAPI.cs:24`
  `public GetClientInfoRequest() : base("api/client-info", ServerRequestMethod.Get)`), i.e. the
  `client_info` table `POST /client-info` created by PR #1 in match3d-backend.

## 3. GitHub tool semantics for PR comments

### 3.1 What the catalog says

`Evals/references/tools/github-tools.json` (57 tools) and `Evals/references/tools/catalog.json` carry
**names and parameter schemas only — no descriptions**. Signatures that matter:

- `github_get_issue_comments` — `owner*, repo*, issue_number* (integer), limit?, offset?`
  (`catalog.json:1611`). Note the parameter is **`issue_number`**, not `pullNumber`.
- `github_get_pull_request_comments` — `owner*, repo*, pullNumber*` (`catalog.json:1705`), **no paging params**.
- `github_get_pull_request_reviews` — `owner*, repo*, pullNumber*` (`catalog.json:1764`), **no paging params**.
- `github_get_pull_request` — `owner*, repo*, pullNumber*` (`catalog.json`, "github_get_pull_request").
- `github_get_pull_request_files` — `owner*, repo*, pullNumber*, page?, perPage?` (`catalog.json:1739`).
So (a) conversation/issue-style comments = `github_get_issue_comments`; (b) inline review comments =
`github_get_pull_request_comments`; (c) review containers = `github_get_pull_request_reviews`.

### 3.2 What the docs say (with the [U] markers)

`Task_Authoring/references/Ask_Carriers.md` §2.9 GitHub:

- Tables (a): "`github_pr_comments`: id!, pr_id!, author_login, body, created_at, updated_at." and
  "`github_review_comments`: id!, pr_id!, author_login, body, **path, diff_hunk, line, position,
  commit_id, in_reply_to_id**, created_at, **seq!**." and "`github_reviews`: … state, body,
  submitted_at, commit_id, **seq!**." — **"There is no issue-comments table."** (line ~557).
- Base counts [V]: "**0 issues, 0 tags, 0 releases.**" and "884 PR comments" / "1,614 review comments" /
  "2,421 reviews" (line 563 and the base counts above it) — i.e. every conversation comment in the corpus hangs off a **PR**.
- Read tools [C] (line 592): "Per PR: `github_get_pull_request`, `github_get_pull_request_comments`,
  `github_get_pull_request_reviews`. **Which tool returns the conversation comments and which returns the
  review (inline) comments is [U].**" and "Issues: … `github_get_issue_comments(…, limit, offset)`".
- Call cost (d), line 603: "each PR costs 5–7 calls (get, comments, reviews, files, commits, timeline, status),
  plus list or search pages."
- Integrity [V] (f), line 608: "`seq` is NOT NULL but not exported [U semantics]." — and the line that governs
  whether a PR number is legal in the issue endpoint: "The issue `number` must not collide with PR
  numbers **[U]**." (§2.9(f), line 612).
- So: **the [U] items are (i) which of the two per-PR tools is conversation vs inline, and (ii) whether
  a PR number is addressable as an issue number.**
- §6b "Verified tool behaviour (Oct 4 …)": "`github_search_pull_requests` / `github_search_issues` match
  title, body or branch by default … **but the `in:comments` qualifier searches comment text**" and
  "**The GitHub Slack app mirrors PR comments and reviews into Slack**" (`#zombie-prs` `C093LEZGF6J` for match3d).

### 3.3 Resolved by observation (not by me calling the tool — this session has no GitHub MCP tools)

Cross-task evidence, `Task_Authoring/task_inputsH/Working_Files/research/R3_opus_failure_modes.md`
(found with the required grep; the other matching paths are
`…/task_inputsH/Working_Files/01_Scenario_Design.md`, `…/01_Grounding_Dossier.md`,
`…/00_Pre_Scenario_Analysis.md`, `…/scenario_gen/dossier_template.md`,
`…/research/eval_rounds/round2/1_prompt.md`, `…/research/eval_rounds/round2/tmp/prompt/report_final.md`,
`…/Eval_Sandbox/Evals/task_inputs/tmp/prompt/main_review_notes.md`):

- Line 525–531: "**GitHub splits conversation comments, reviews and inline comments into three tools.**
  `github_search_pull_requests` returns `total_count`/`has_more`/`items` and its `comments` field counts
  conversation comments only (arthur run-1 `query:"scale-down"`: `total_count:3`); reviews and inline
  comments come only from `github_get_pull_request_reviews` / `github_get_pull_request_comments`
  (`learnings:595-603` §53). douglas run-1 called `github_get_issue_comments` 25× and
  `get_pull_request_reviews` 23× and **never** `get_pull_request_comments` — the exact 17-row miss in §2.5."
- Line 533–535: "**`github_get_issue_comments` / `trello_get_comments` / `confluence_search` all expose
  `total_count`+`has_more`** (douglas run-1: 25 and 1 and 3 hits), so completeness is provable but only if
  the agent pages."
  ⇒ **Yes, `github_get_issue_comments` accepts a PR number** (it was called 25× against PRs and returned
  hits with `total_count`/`has_more`); this is *observed*, and the doc's counterpart warning stays [U].
- `Task_Authoring/task_inputsH/Working_Files/01_Scenario_Design.md:225` plans the same pattern per record:
  "per PR: github_get_pull_request_reviews and github_get_pull_request_comments over the 12 object PRs
  (24 calls), and github_get_issue_comments on the PRs whose conversation holds more than CodeRabbit's
  summary (2; all 12 when no comment count is shown)".
- `learnings` §53 (lines 596–598), verified against PR #1679: "`github_search_pull_requests` `comments`
  counts conversation comments only (#1679: 26 inline, `comments: 0`); `\"store build\" in:comments`
  returned 0 hits. Reviews and inline comments come back only from their own reads."

### 3.4 Ground truth shape of what each tool returns (from the export itself)

`raw/github.json`:
- `pull_request_comments` (687 total, 291 in the two match3d repos):
  `{"id": "harmonygames-Games/match3d#137#c_1", "pr_id": "…/match3d#137", "author_login": "EMPLOYEE_0016_GITHUB_USERNAME", "body": "Lock streak until level 19. Level difficulty adjustments 4-19", "created_at": "2025-04-15T02:25:19Z", "updated_at": null}`
  → conversation comment has **no `path`**.
- `review_comments` (1,387 total, 805 in the two match3d repos):
  `{"id": "…/match3d#188#rc_1", "body": "to name folders, always use PascalCase. \"WaitingForPlayers\"", "path": "Assets/Textures/UI/MainMenu/waitingForPlayers.meta", "diff_hunk": "", "line": null, "position": null, "commit_id": null, "in_reply_to_id": null}`
  → inline comment carries **`path` + `diff_hunk`**, and in this universe `line`/`position`/`commit_id`/`in_reply_to_id` are **all null**.
- `reviews`: `{"id": "…/match3d#11#rev_1", "author_login": "EMPLOYEE_0025_GITHUB_USERNAME", "state": "APPROVED", "body": "", "submitted_at": "2025-01-24T20:11:58Z", "commit_id": null}` — many review bodies are empty strings, so a review read alone is weak evidence; the inline comments carry the substance.

## 4. Summary

**4.1 Does a per-event backend config give a natural per-beat read? — Yes, one read covers every event
window in the game, but only half the reward numbers.**

- One file (`zombies-game-cdk/lib/zombies-game-cdk-stack.ts:139–200`, mirrored by
  `config/runtime.exs:157–247`) yields, in a single read, the production window for **13 event
  families / 11 distinct crons**: plague race `0 0 * * *`, endless daily `0 0 * * *`, endless weekly
  `0 0 * * 1`, boss arena daily `0 0 * * *`, boss arena weekly `0 0 * * 1`, Collect&Win G1 `0 0 * * 1,2`,
  G2 `0 0 * * 3,4`, G3 `0 0 * * 5,6,0`, season pass `0 0 1 * *`, leagues `0 0 * * 1` (10 tiers), plus the
  daily-login constants `1440` / `2880` minutes and the `*/5 * * * *` reward-import cron.
- The **conversion from cron → a concrete UTC timestamp is itself a graded step**
  (`lib/zombies_game/leaderboards.ex:278–284`, `Crontab.Scheduler.get_next_run_date!` →
  `DateTime.from_naive!("Etc/UTC")`), so a beat that asks "when does X end" is answerable from *this one
  file* but only by doing the cron arithmetic.
- A trap is built in: `leaderboards.ex:303` hardcodes plague race at `"0 * * * *"` (hourly) while prod
  overrides it to `"0 0 * * *"` (`cdk-stack.ts:143`) — an agent reading only the Elixir default gets a
  wrong window. Same shape for the Collect&Win defaults: `"0 0 * * 3"` in `runtime.exs:214` (Wednesday,
  "end of Tuesday") vs `"0 0 * * 1,2"` in the CDK (Monday **and** Tuesday) — the two disagree.
- **Reward numbers are only half in git.** Plague Race stages are in the repo
  (`plague_race.ex:437–472`: 5/10/15 levels → 60/120/250 coins, defeat 60, cities new_york/london/paris,
  `total_players: 5`). Daily login, chest, Season Pass, Zombie Lane and Collect&Win numbers are **not in
  git** — they are Google-Sheets ranges on spreadsheet `1UEpyibxuQSB2-ib7UgppYDeeHkmM1fhSKNbQ_t_Sk`
  (`config/config.exs:93–124`, `config/runtime.exs:220–225`). So a reward-table beat needs a second,
  different service surface; a window beat needs only the repo.
- Client has **no** per-event config to fall back on (section 2): a client-only reader sees endpoints
  (`PlagueRaceStageInfo.cs:12–17`) and never a number or a date.

**4.2 Cost of "read every review and comment on a PR" — 3 calls, or 2 if conversation comments are
unnecessary.**

| need | tool | evidence |
|---|---|---|
| review containers (state/body) | `github_get_pull_request_reviews(owner, repo, pullNumber)` | **verified** — tool exists with these exact params (`catalog.json:1764`) |
| inline review comments (body + `path` + `diff_hunk`) | `github_get_pull_request_comments(…)` | **verified** params (`catalog.json:1705`); **observed** as the inline surface (`learnings` §53; R3:525–531) |
| conversation (issue-style) comments | `github_get_issue_comments(owner, repo, issue_number, limit, offset)` | **observed** that a PR number works (douglas run-1, 25 calls with `total_count`/`has_more`, R3:530–535); doc-level **[U]** ("which tool returns the conversation comments … is [U]", Ask_Carriers §2.9(c); "issue `number` must not collide with PR numbers [U]", §2.9(f)) |

- Adding the PR itself (`github_get_pull_request`) makes 4; adding `…_files` makes 5 — matching the doc's
  "each PR costs 5–7 calls (get, comments, reviews, files, commits, timeline, status)".
- Caveat (**observed from the export**): neither `…_comments` nor `…_reviews` takes paging params, and
  inline volume is skewed — in the two match3d repos the per-PR maximum is **73 inline comments**
  (`harmonygames-Games/match3d#438`), 47 (#408), 42 (#317), against a median of 5; conversation comments
  max out at 3 per PR and reviews at 16 (#408). Review bodies are frequently empty
  (e.g. `…/match3d#11#rev_1` `"body": ""`), so "read every review and comment" must mean all three tools,
  and on the heavy PRs a single non-paged call is a truncation risk [U threshold].
- Evidence level overall: **verified** that three separate tools exist with those signatures;
  **observed** (cross-task trajectories, `learnings` §53, R3 report) for the conversation/inline mapping
  and for PR numbers being accepted by the issue-comments tool; **unverified [U]** for the doc's own
  statement of the mapping and for truncation behaviour on large PRs. I could not re-verify by calling
  the tools: this session exposes no GitHub MCP tools (only `google_search`, `opencode.*`,
  `provider_health`, `usage_report`, `verification_status`, `verify`).
