# Grounding R1 — rev2 design (synth-cut, clock 2025-10-01T07:00Z)

Read-only research for injection rev2. No SQL executed, no base export modified.

## 1. Schema: review_comments / reviews column lists

`Evals/references/schema/injection.json` (array of 58 table objects; `table_schema` + `table_name` + `columns`).

`github.github_review_comments` — 11 declared columns:

| # | column | type | null | default |
|---|--------|------|------|---------|
| 1 | id | character varying | NO | – |
| 2 | pr_id | character varying | NO | – |
| 3 | author_login | character varying | YES | – |
| 4 | body | text | YES | – |
| 5 | path | character varying | YES | – |
| 6 | diff_hunk | text | YES | – |
| 7 | line | integer | YES | – |
| 8 | position | integer | YES | – |
| 9 | commit_id | character varying | YES | – |
| 10 | in_reply_to_id | character varying | YES | – |
| 11 | created_at | timestamp with time zone | YES | – |

`github.github_reviews` — 7 declared columns: `id` (varchar, NO), `pr_id` (varchar, NO), `author_login` (varchar, YES), `state` (varchar, YES), `body` (text, YES), `submitted_at` (timestamptz, YES), `commit_id` (varchar, YES).

**Live table is wider than injection.json.** The completed Douglas task SQL writes three columns that `injection.json` does not list: `seq` (reviews), and `seq`, `pull_request_review_id`, `side`, `subject_type` (review_comments). So `injection.json` is a *minimum/declared* set, not the physical set — the INSERT in §1.2 is the operative contract.

### 1.2 Completed Douglas task SQL (`Task_Authoring/support/completed_tasks/douglas_beta_server_signoff_2026-10-28/task_inputs/01_Universe_Inject.sql`)

Column list (review_comments, line 145 / 177 / 397):
`(id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, seq, pull_request_review_id, side, subject_type)`

Full INSERT (line 145):

```sql
INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, seq, pull_request_review_id, side, subject_type)
VALUES ('harmonygames-Games/match3d-backend#38#rc_1', 'harmonygames-Games/match3d-backend#38', 'PERSON_2967_GITHUB_USERNAME', 'looks right. one thing: standings come from the plague race table now, so 459 also needs the plague race table import on the backend. that import is part of 459''s server change, the count won''t change on prod without it', 'lib/zombies_game/plague_race.ex', E'@@ -31,4 +31,4 @@ defmodule ZombiesGame.PlagueRace do\n   def standings(race_id) do\n-    Repo.all(standings_query(race_id))\n+    Tables.fetch!(:plague_race, {race_id, :standings})\n   end', 34, NULL, 'b1388ff2f8d945f005ea87b236afbab0c14e6e64', NULL, '2025-08-25T09:20:00Z', 1, 'harmonygames-Games/match3d-backend#38#rev_2', 'RIGHT', 'line');
```

Column fill conventions in that file:
- `pull_request_review_id` = the review row id it hangs off (`…#38#rev_2`) — the same id Arthur's APPROVED review gets.
- `commit_id` = the PR head SHA (`b1388ff2…`), not NULL.
- `path` = a real repo path (`lib/zombies_game/plague_race.ex`).
- `line` = an int; `position` = NULL always.
- `diff_hunk` = a real `E'@@ … @@'` hunk starting at the surrounding context of that `line`.
- `in_reply_to_id` = NULL for a top-level comment.
- `side` = `'RIGHT'`, `subject_type` = `'line'`, `seq` = 1.
- `created_at` is exactly **5 minutes before** the parent review's `submitted_at` (38: rc 09:20 vs rev_2 09:20 — same minute here; 39: rc 15:20 vs rev_2 15:20). The archived review-history fix notes "Each created_at is exactly five minutes (300 seconds) before the submitted_at of its referenced `pull_request_review_id`" (`Task_Authoring/support/archive/.../finish_review.py`, `build_delta_report.py` line 96). **Check C risk: choose an offset that matches this house convention.**

Full INSERT (reviews, lines 143–144):

```sql
INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq)
VALUES ('harmonygames-Games/match3d-backend#38#rev_2', 'harmonygames-Games/match3d-backend#38', 'PERSON_2967_GITHUB_USERNAME', 'APPROVED', '', '2025-08-25T09:20:00Z', 'b1388ff2f8d945f005ea87b236afbab0c14e6e64', 2);
```

So the approved-with-empty-body shape is already the house pattern: `state 'APPROVED'`, `body ''`, `commit_id` = head sha, `seq` = 2.

Current `01_Universe_Inject.sql` #36 block (lines 281–291) writes: PR #36 (closed, merged, Douglas author+merger), `pull_request_commits #36#c_0`, `reviews #36#rev_1` = Arthur `'APPROVED'`, body `'lgtm'`, `commit_id NULL`, `seq 1`; timeline `ev_1..ev_5`; repo `updated_at/pushed_at = 18:50Z`. **No review_comments row exists for #36 today, and `body='lgtm'` is what R1 wants emptied.**

## 2. Base precedent: human review_comments on match3d-backend PRs

Base `review_comments` object keys: `author_login, body, commit_id, created_at, diff_hunk, id, in_reply_to_id, line, path, position, pr_id`.

All four human (non-CodeRabbit) base review comments on `match3d-backend` — every one is on **PR #4** ("Reuse Leaderboard tables for PlagueRace events", created 2025-06-05T19:31:40Z):

```json
{"id": "harmonygames-Games/match3d-backend#4#rc_1", "pr_id": "harmonygames-Games/match3d-backend#4",
 "author_login": "PERSON_2967_GITHUB_USERNAME",
 "body": "```suggestion\r\ndefmodule ZombiesGame.Repo.Migrations.AddMetadataFieldToRecord\" do\r\n```",
 "path": "priv/repo/migrations/20250606054859_add-metadata-field-to-record.exs",
 "diff_hunk": "@@ -0,0 +1,9 @@\n+defmodule :\"Elixir.ZombiesGame.Repo.Migrations.Add-metadata-field-to-record\" do",
 "line": null, "position": null, "commit_id": null, "in_reply_to_id": null,
 "created_at": "2025-06-06T22:58:30Z"}
```

```json
{"id": "harmonygames-Games/match3d-backend#4#rc_2", "pr_id": "harmonygames-Games/match3d-backend#4",
 "author_login": "PERSON_2967_GITHUB_USERNAME",
 "body": "Remove the double quotes\r\n\r\n```suggestion\r\ndefmodule ZombiesGame.Repo.Migrations.AddMetadataFieldToRecord do\r\n```",
 "path": "priv/repo/migrations/20250606054859_add-metadata-field-to-record.exs",
 "diff_hunk": "@@ -0,0 +1,9 @@\n+defmodule :\"Elixir.ZombiesGame.Repo.Migrations.Add-metadata-field-to-record\" do",
 "line": null, "position": null, "commit_id": null, "in_reply_to_id": null,
 "created_at": "2025-06-10T01:13:57Z"}
```

```json
{"id": "harmonygames-Games/match3d-backend#4#rc_4", "pr_id": "harmonygames-Games/match3d-backend#4",
 "author_login": "PERSON_5760_GITHUB_USERNAME", "body": "Done!",
 "path": "lib/zombies_game_web/controllers/plaguerace_controller.ex", "diff_hunk": "",
 "line": null, "position": null, "commit_id": null, "in_reply_to_id": null,
 "created_at": "2025-06-10T13:31:03Z"}
```

(the third, `#4#rc_3`, `PERSON_2967`, body "For consistency, rename to `plague_race_controller.ex`", path `lib/zombies_game_web/controllers/plaguerace_controller.ex`, `diff_hunk ""`, all nulls, `2025-06-10T01:15:01Z`.)

Key precedents:
- The `id` pattern for a review comment is **`<pr_id>#rc_<n>`** → for #36 that is `harmonygames-Games/match3d-backend#36#rc_1`.
- Human reply-style comments in base leave `line`, `position`, `commit_id`, `in_reply_to_id` at null and often `diff_hunk` at `""`. The completed-task injection is the *stricter* variant (diff_hunk + line + commit_id + pull_request_review_id filled) — both shapes exist, so R1's inline comment is defensible but should follow the completed-task shape, not the bare base shape, because R1 wants an inline anchor.
- **Empty-body APPROVED reviews are the norm on match3d-backend: 30 of 30** APPROVED reviews on that repo have `body: ""` (and `commit_id: null`). Universe-wide 1663/1742 APPROVED reviews are empty. So emptying `rev_1` is *more* realistic than `'lgtm'`.
- Universe-wide only 3 human review comments exist on match3d-backend (all PERSON_2967) + 1 by PERSON_5760; 26 are CodeRabbit (`PERSON_6026_GITHUB_USERNAME`). A single added human inline comment is at the top of the observed rate, not outside it.

## 3. Realistic match3d-backend paths for a chest grant job and reward seeds

Base tree at `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/root/harmonygames-Games/match3d-backend/` and base commits give the naming.

Grant/import job (real, exists):
- `lib/zombies_game/zombie_lane.ex` — `def import_rewards()` → `Logger.info("Importing Zombie Lane rewards from spreadsheet")`; `def update_rewards()`; `def rewards_from_spreadsheet()` → `Sheets.table_data(spreadsheet_id, sheet_name, range)`.
- `lib/zombies_game/scheduler.ex` — `defmodule ZombiesGame.Scheduler do … use Quantum, otp_app: :zombies_game`.
- `config/prod.exs` (lines 43–59) — the cron block:
  ```
  config :zombies_game, ZombiesGame.Scheduler,
    overlap: false,
    run_strategy: Quantum.RunStrategy.Local,
    jobs: [
      import_zombie_lane_rewards: [
        schedule: System.get_env("IMPORT_REWARDS_SCHEDULE", "0 * * * *"),
        task: {ZombiesGame.ZombieLane, :import_rewards, []}
      ],
      import_chest_reward_rewards: [
        schedule: System.get_env("IMPORT_REWARDS_SCHEDULE", "0 * * * *"),
        task: {ZombiesGame.ChestReward, :import_rewards, []}
      ]
  ```
- `lib/zombies_game/chest_reward.ex` — `defmodule ZombiesGame.ChestReward`, `alias ZombiesGame.Inventory`, `@leaderboard_id :chest_reward`, `def create_chest_reward(%Player{}, %Leaderboard{})`.
- `lib/zombies_game/inventory.ex` — `defmodule ZombiesGame.Inventory`, `set_player_item/2`, `get_player_item/2`, `list_player_items/1` (the grant sink).
- `lib/zombies_game_web/controllers/debug_controller.ex` — `summary: "Refreshes Zombie Lane rewards from spreadsheet"` (manual refresh path).
- Commits (real): `240f021343` 2025-06-27T21:40:54Z "Add job to import zombie lane rewards every hour"; `e82d1739ec` "Refactor ZombieLane to use cache for rewards"; `14bee494df` "Update zombie lane to use new rewards structure"; `0e727dcca9` "Simplify level rewards logic". PR #14 "ZombieLane: Import rewards from spreadsheet" (`events-zombie-lane-import`, merged 2025-06-30T22:24:12Z).

Reward data / seeds / migrations:
- `priv/repo/seeds.exs` (real file; `# Script for populating the database. You can run it as: # mix run priv/repo/seeds.exs`).
- `priv/repo/migrations/` — real names, e.g. `20250606054859_add-metadata-field-to-record.exs`, `20250725152018_add_login_information_fields_to_player_table.exs`, `20250903005750_add_is_premium_to_players.exs`, `20250903230418_remove_is_premium_from_players.exs`.
- Base review-comment path precedent for a migration: `priv/repo/migrations/20250606054859_add-metadata-field-to-record.exs` (`#4#rc_1`/`rc_2`), and for a controller `lib/zombies_game_web/controllers/plaguerace_controller.ex`.

→ For R1, use a path under `priv/repo/migrations/` or `priv/repo/seeds/` for "reward rows", and `lib/zombies_game/zombie_lane.ex` / `lib/zombies_game/chest_reward.ex` for the grant code. A migration filename must sort after the newest base one (`20250903230418`) if it is new, e.g. `priv/repo/migrations/20250930160000_add_zombie_lane_reward_rows.exs`.

## 4. Confluence + Douglas DM reward-refresh facts

Source: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json` (30 pages, 12 comments). All page ids below are real; quoting the stored `body` HTML.

### 4.1 `page_live_ops_engine` — "Live-Ops Event Engine" (space_ENG, version 1, updated 2025-08-01T08:11:12Z)

Intro sentence (the central authority that the engine imports the Zombie Lane reward table):
> "The Live-Ops Event Engine powers all recurring in-game events for Zombie Match 3D … It defines, schedules, and fires timed content — **Plague Race** and the Endless Monster Mode resets — **imports the reward table for the permanent, level-gated Zombie Lane track**, and drives the associated leaderboards."

Scheduler row of the component table:
> "Scheduler | Runs on hourly Quantum crons (`0 * * * *`); opens and closes events. … | Backend (Douglas)"

The warning callout (the deploy hazard — supports "merged is not live"):
> "**Scheduler is a single point of failure.** The scheduler runs as a supervised cluster-wide singleton, so a crashed process is restarted elsewhere; **what it does not survive is a deploy that leaves the job unscheduled**."

The July 2025 outage, by-hand enablement:
> "QA first reported it on **Sunday 29 June 2025** and **the events were enabled by hand in the database that day**".

### 4.2 `page_cicd_pipeline` — "CI/CD Pipeline & Branching" — the by-hand deploy

Pipeline table, Deploy row:
> "**Run by hand**: rolling Fargate task-definition update via the `aws ecs update-service` command below; health checks gate promotion. The only CI-driven deploys in the org are the marketing site's S3 syncs (`website/.github/workflows/s3-deploy*.yml`)."

Merge row (CI stops at build, so a merge deploys nothing):
> "The same `mix check` job runs again on push to main - there is no separate post-merge suite. **CI stops here** - the backend workflow (`match3d-backend/.github/workflows/check.yml`) runs compile and check on push/PR and **has no deploy step**."

Also: "Client (Unity) builds are cut separately and go through staged store rollout - never 100% on day one."

### 4.3 `page_backend_services` — "Backend Services — Elixir/Phoenix" — migrations are a separate manual step

> "**Migrations do not run on boot.** Run `bin/harmony_backend eval "HarmonyBackend.Release.migrate()"` as a one-off Fargate task before rolling the services, so a bad migration can't take down every task at once."

> "Owner: Douglas (Engineering). Ping in #engineering before schema changes to the shared Aurora cluster …"

This is the load-bearing page for R1: **code roll-out and data/migration roll-out are two separate manual acts.** A container on prod with the migration not yet run is exactly the documented failure shape.

### 4.4 `page_liveops_calendar` — "Live-Ops Event Calendar & Planning" — the hourly re-import

> "**There is no technical content lock.** Reward tables are re-imported from Google Sheets hourly in production (`IMPORT_REWARDS_SCHEDULE` defaults to `0 * * * *`), so a mid-window sheet edit reaches players within the hour."

### 4.5 Douglas's base DM messages about reward-sheet refresh / data import (D079SNE2TL4, Sep 2025)

All quotes verbatim, Douglas = `EMPLOYEE_0031_SLACK_ID`:

| ts | UTC | text |
|---|---|---|
| `1757350234.373819` | 2025-09-08 16:50:34 | "Yes! I'm making the deployment right now" |
| `1757351666.990529` | 2025-09-08 17:14:26 | "Whatever you want, sir, I can change it as well :slightly_smiling_face:" |
| `1757351687.236529` | 2025-09-08 17:14:47 | "I can change it to 5 mins right now, to be easier to test" |
| `1757351863.576949` | 2025-09-08 17:17:43 | "yes! just finished the deployment" |
| `1757352081.415329` | 2025-09-08 17:21:21 | "let me know any issue" |
| `1757532719.083269` | 2025-09-10 19:31 | "probably the data update caused the issue, let see if [PERSON_NAME_0029] finds something" |
| `1757955599.740879` | 2025-09-15 16:59 | "we can start from There, with tha spreadsheet" |
| `1757694151.482109` | 2025-09-12 16:22 | "yeah I will, sorry, I was implementing the season pass <-> teams integration" |

Vincent's framing turns in the same thread: "hi, can you let me know when you increase the row limit for prod reward sheet?" (`1757350210.055289`, 2025-09-08 16:50:10), "how often the prod rewards are updated? also 15 min?" (`1757351421.740279`), "can you let me know once you deployed the boss arena sheets?" (`1757693862.033889`).

**What this establishes:** Douglas routinely does prod **data/sheet** deployments by hand and *reports them explicitly in this DM* ("just finished the deployment"). The prod reward sheet exists and is re-imported on a schedule. So the DM history is a control: on Sep 30 Douglas reports only the **container**, and never reports a **data** deploy for the chest rows — the absence is the evidence, and it is only legible because he always announces data deploys here.

### 4.6 How the new "reward rows are dev-only" fact must be worded

Constraints from the base text above:

1. **Do not** say the prod import is broken, stale, or "hasn't run" — `page_liveops_calendar` says the prod import runs hourly, and Douglas demonstrably fixes/refreshes it in this very DM. A "the sheet hasn't been refreshed" phrasing contradicts both.
2. **Do not** say the reward data cannot reach prod until a code deploy — `page_backend_services` and the Sep-8 thread show data promotion is a separate manual act that does not wait on a code rollout.
3. The fact must be about **rows that do not exist in prod yet**, i.e. the new chest rows are only seeded/imported on dev because *the prod import for them is deliberately deferred until after the store push* (`ZOM-570` "ZM store push - Android Submission #135 / iOS Submission #50", In Progress; gate sheet `f_0ebfccf33076f9dbf086bc` tab "How we gate").
4. It must be attached to **Arthur** — `page_aws_infra`: "anything touching Aurora or a data migration escalates to Arthur Blake before any write action" — so Arthur stating the data deferral is in character and authoritative, and it explains why a *Done* ticket is not actually live.

Safe wording (used in §7): *"the chest reward rows ZOM-567 needs are still only on dev … the new grant path isn't active on prod … the prod import of those rows waits until after the store push."* That asserts only the state of the **rows** and the **deferral decision**, never the health of the import mechanism.

⚠️ Residual tension to accept knowingly: `page_liveops_calendar`'s "a mid-window sheet edit reaches players within the hour" means a reader can ask "then why not just add the rows to the prod sheet?" The answer is the deliberate deferral sentence — which is why the wording must include *"waits until after the store push"* rather than only *"still only on dev"*.

## 5. Douglas DM D079SNE2TL4 messages 2025-09-30T18:00Z → end

File: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/D079SNE2TL4/2025-09.json` (a JSON **array**; 267 messages in Sep 2025; only two participants: Vincent `EMPLOYEE_0012_SLACK_ID` 171 msgs, Douglas `EMPLOYEE_0031_SLACK_ID` 96 msgs).

**Douglas's Slack user id: `EMPLOYEE_0031_SLACK_ID`** — `users.json`: `{"id":"EMPLOYEE_0031_SLACK_ID","name":"Douglas","real_name":"Douglas","display_name":"Douglas","email":"douglas@harmonygames.co","is_bot":false,"timezone":"America/Los_Angeles"}`. (Vincent = `EMPLOYEE_0012_SLACK_ID`, `vincent.parker@harmonygames.co`.)

Every message from 2025-09-30T18:00Z to the end of the export (4 total, the export ends here):

| ts | UTC | user | text |
|---|---|---|---|
| `1759256193.859279` | 18:16:33 | `EMPLOYEE_0031_SLACK_ID` (Douglas) | "Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues" |
| `1759256806.682939` | 18:26:46 | `EMPLOYEE_0012_SLACK_ID` (Vincent) | " Thankss will return to you" |
| `1759269524.769369` | 21:58:44 | `EMPLOYEE_0012_SLACK_ID` (Vincent) | "Yep it works as expected " |
| `1759269903.971719` | 22:05:03 | `EMPLOYEE_0031_SLACK_ID` (Douglas) | "Go to sleep [PERSON_NAME_0050] :sleeping:" (has a `joy` reaction from Vincent) |

Nothing else exists in this DM after 21:58:44Z except Douglas's own 22:05:03 "Go to sleep". **No third party, and no Vincent message, appears after 21:58:44Z** — so an inserted Douglas message at 22:2xZ is not contradicted by anyone.

Full JSON shape of a Douglas message (the 22:05:03 row, all 15 keys, verbatim):

```json
{
 "id": "fb5e394127f3d9feb030f38df900804a",
 "ts": "1759269903.971719",
 "type": "message",
 "user": "EMPLOYEE_0031_SLACK_ID",
 "text": "Go to sleep [PERSON_NAME_0050] :sleeping:",
 "channel": "D079SNE2TL4",
 "thread_ts": null,
 "reply_count": 0,
 "reply_users_count": 0,
 "latest_reply": null,
 "is_activity_message": false,
 "subtype": null,
 "reactions": [{"count": 1, "name": "joy", "users": ["EMPLOYEE_0012_SLACK_ID"]}],
 "files": [],
 "attachments": []
}
```

Key set is identical for Vincent's rows (checked: `sorted(V.keys()) == sorted(D.keys())` == `attachments, channel, files, id, is_activity_message, latest_reply, reactions, reply_count, reply_users_count, subtype, text, thread_ts, ts, type, user`). Injected rows therefore need `reactions '[]'`, `files '[]'`, `attachments '[]'`, `thread_ts NULL`, `reply_count 0`, `reply_users_count 0`, `latest_reply NULL`, `is_activity_message false`, `subtype NULL`.

**Conflict check for a Douglas message at ~22:2xZ saying the #36 container is on prod:**
- No base message in this DM after 21:58:44Z except Douglas's 22:05:03 "Go to sleep" → no factual clash with anyone else.
- The one soft wobble: Douglas tells Vincent to go to sleep at 22:05:03 and would then post again at 22:2xZ. Not a contradiction (Douglas is demonstrably still working — see below), but 22:01–22:04Z, i.e. between Vincent's 21:58:44Z reply and Douglas's 22:05:03Z sign-off, reads more naturally. Either is coherent; flagging both.
- Douglas is verifiably awake and working late: DM `D07GY332589` has Douglas messages at 22:01:45, 22:04:24, 22:29:41, 22:30:39, 22:32:07, 22:32:35, 22:38:32, 22:41:22, 22:53:03, 22:55:49, 22:58:42, 23:00:28, 23:01:01, 23:04:58, 23:31:49, 23:56:14 (all 2025-09-30). A 22:2xZ message is fully consistent.
- The 18:16:33Z prod deploy is Douglas's and lands **before** #36 merged at 18:50Z, so it cannot have carried #36 — that ordering is what keeps the 22:2x claim honest rather than duplicative.
- Vincent's 21:58:44Z "Yep it works as expected" answers the 18:16Z teams/social deploy for ZOM-563 (see his 16:38:03Z link: `https://linear.app/harmonygames-games/issue/ZOM-563/teams-lives-golden-frames-and-names-not-working-on-prod-env`). Douglas's new message must name #36 explicitly so it cannot be read as a continuation of ZOM-563.

## 6. INT-01 mirroring requirement for github PR events/reviews/review comments

**Answer: NO mirror for match3d-backend. Do not seed any Slack copy of #36's review, review comment or merge.**

`Task_Authoring/tools/base_check.py:1004`:
```python
MIRROR_CHANNELS = {"GameOfDominoes": "C050WGU41HR", "game-of-dominoes-backend": "C050WGU41HR", "match3d": "C093LEZGF6J"}
```
`match3d-backend` is **absent**, and the check only looks for `kind == "opened"` parents.

`Task_Authoring/references/universe_kb/by_universe/synthcut/integrations.md` (INT-01, line 8): "GitHub Slack app -> #engineering-bots (C050WGU41HR: GameOfDominoes, game-of-dominoes-backend) and #zombie-prs (C093LEZGF6J: match3d) … Repos outside that list/window must NOT get a mirror."

Coverage table (same file, lines 34–45):
```
| GameOfDominoes | 1857 | 2023-04-14 → 2025-08-01 | 1856 | 1843 | 1757 / 1741 | 386 / 881 | 1809 / 1595 |
| game-of-dominoes-backend | 79 | 2024-10-21 → 2025-09-10 | 78 | 78 | 75 / 75 | 2 / 33 | 80 / 78 |
| match3d | 477 | 2025-06-30 → 2025-09-30 | 222 | 220 | 212 / 210 | 248 / 956 | 237 / 210 |
| match3d-backend | 35 | not mirrored | 0 | 0 | 0 / 0 | 0 / 0 | 0 / 0 |
```

`integrations.json` INT-01 `window` has keys for `GameOfDominoes`, `game-of-dominoes-backend`, `match3d` only — no `match3d-backend` key; `match3d` window is `2025-06-30T21:35:55Z → 2025-09-30T22:33:40Z`.

Consequence for rev2:
- #36's review/comment/merge must **not** appear in `C093LEZGF6J` or `C050WGU41HR`.
- INT-02 push notices ("N new commit(s) pushed to `main`"): "Seed only for the mirrored repos/branches" — a match3d-backend push mirror would be a new coherence hazard. Keep the GitHub-side `updated_at/pushed_at` stamp only.
- The `#zombie-ops` withdrawal + Douglas reply are ordinary human Slack messages in a normal channel, not bot mirrors → unaffected by INT-01.
- Arthur's real login is `arthur.blake` in mirror messages (tokens in the GitHub export); moot here since there is no mirror.

## 7. Proposed exact row values and Check C contradiction risks

### 7.1 NEW `github.github_review_comments` row — Arthur's inline comment on #36

```sql
INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, seq, pull_request_review_id, side, subject_type)
VALUES ('harmonygames-Games/match3d-backend#36#rc_1', 'harmonygames-Games/match3d-backend#36', 'EMPLOYEE_0025_GITHUB_USERNAME', 'approving the code, but it does not fix it on its own. the chest reward rows ZOM-567 needs are still only on dev, and the new grant path is not active on prod, so claims on prod still will not add the items. i am not importing those rows to prod until after the store push, so do not mark it fixed on prod yet', 'lib/zombies_game/zombie_lane.ex', E'@@ -110,6 +110,9 @@ defmodule ZombiesGame.ZombieLane do\n   def import_rewards() do\n-    Logger.info("Importing Zombie Lane rewards from spreadsheet")\n+    Logger.info("Importing Zombie Lane rewards from spreadsheet and seeding chest rows")\n+    ChestReward.seed_reward_rows()\n     %{show_levels: show_levels} = update_rewards()', 114, NULL, '5fa55c7a2d2f25fe75b576c00061000610669d3c', NULL, '2025-09-30T18:37:00Z', 1, 'harmonygames-Games/match3d-backend#36#rev_1', 'RIGHT', 'line');
```

Rationale for each field:
- `id` — base pattern is `<pr_id>#rc_<n>`; #36 has no rc yet → `…#36#rc_1`.
- `author_login` — `EMPLOYEE_0025_GITHUB_USERNAME` is Arthur (same actor as `#36#rev_1` and timeline `ev_3`).
- `path` — `lib/zombies_game/zombie_lane.ex` is a real base file whose `import_rewards/0` is quoted in §3. (Alternative, equally grounded: `priv/repo/migrations/20250930160000_add_zombie_lane_reward_rows.exs` — see §3 for the filename-ordering rule.)
- `diff_hunk` / `line` — the hunk must actually contain the line being commented on. Verified against the checkout: `def update_rewards()` at **94**, `def import_rewards()` at **112**, `Logger.info("Importing Zombie Lane rewards from spreadsheet")` at **113**, `def rewards_from_spreadsheet()` at **120**. Commenting on the added `ChestReward.seed_reward_rows()` line gives new-side `line = 114`; if the comment is anchored on the `Logger.info` line instead, use `113` and keep the hunk consistent. An off-by-N `line` with a mismatched hunk is a visible defect (Check C).
- `commit_id` — must be #36's head SHA `5fa55c7a2d2f25fe75b576c00061000610669d3c`, which **is** inserted into `github.github_commits` at line 282, so the FK holds.
- `pull_request_review_id` — `…#36#rev_1`, the review it belongs to.
- `position NULL`, `in_reply_to_id NULL` (top-level), `side 'RIGHT'`, `subject_type 'line'`, `seq 1`.
- `created_at` — 5 minutes before `rev_1.submitted_at` (18:42:00Z) → **18:37:00Z**. This matches the house convention documented in the archived review-history fix (§1.2).

### 7.2 CHANGED `github.github_reviews` row `…#36#rev_1`

```sql
INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq)
VALUES ('harmonygames-Games/match3d-backend#36#rev_1', 'harmonygames-Games/match3d-backend#36', 'EMPLOYEE_0025_GITHUB_USERNAME', 'APPROVED', '', '2025-09-30T18:42:00Z', NULL, 1);
```

Only `body` changes: `'lgtm'` → `''`. Every match3d-backend APPROVED review in base (30/30) has an empty body, so this is the more realistic shape and it also removes the only wording that asserted the fix was fine.

### 7.3 NEW `slack.slack_messages` row — Douglas in D079SNE2TL4

```sql
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json)
VALUES ('<32-hex>', '1759271000.482913', 'D079SNE2TL4', 'message', 'EMPLOYEE_0031_SLACK_ID', 'fyi #36 is rolled out to prod now, the container is up. that is the code side only.', NULL, NULL, 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2025-09-30T22:23:20.482913Z', '{}');
```

- `ts` `1759271000.482913` = **2025-09-30T22:23:20Z**, after Vincent's 21:58:44Z. (Nudge to `1759269700.xxxxxx` ≈ 22:01:40Z if the 22:05:03 "Go to sleep" ordering matters — see §5.)
- `thread_parent_id` / `thread_ts_legacy` NULL, no thread fields — matches every base row in this DM.
- Must **name #36** so it cannot be read as a ZOM-563 follow-up.

### 7.4 ROWS TO DELETE

Both current injected Slack rows in `C08R6BF4ENN` (only two exist in that channel; each references the other exactly once — verified by count):

| id | ts | channel | user | role |
|---|---|---|---|---|
| `9c14e45ff33fa29e54efe876ef6048fc` | `1759261800.335275` (19:50:00Z) | C08R6BF4ENN | `EMPLOYEE_0025_SLACK_ID` (Arthur) | the APPROVED-withdrawal parent ("taking my approve on backend #36 back … keep it on dev … we'll redo it next week") |
| `2f3ae3a5ecb8288ac60b8f9264af8070` | `1759262520.892033` (20:02:00Z) | C08R6BF4ENN | `EMPLOYEE_0031_SLACK_ID` (Douglas) | Douglas's reply "ok, #36 stays on dev for now" |

Thread-field cleanup: the parent's own fields (`reply_count 1`, `reply_users_count 1`, `latest_reply '1759262520.892033'`, `thread_ts_legacy '1759261800.335275'`) die with the parent — **no surviving parent needs its counts recomputed**, and no other injected row points at either id. Base `C08R6BF4ENN/2025-09.json` ends 2025-09-15T04:32:41Z, so after deletion the channel has **no injected rows at all** and needs no rollback of any last-message stamp (`slack_channels` has no ts columns and the SQL never writes it — columns: `id, name, is_channel, is_private, is_im, is_mpim, is_archived, is_general, num_members, topic, purpose, created_ts, creator_id, members_json`).

### 7.5 Check C contradiction risks (flagged, in priority order)

1. **"container on prod" vs the gate definition "server - live".** Gate sheet `f_0ebfccf33076f9dbf086bc` tab "How we gate" defines `server - live` as "a server-side fix that's deployed to prod" and `server - not live` as "a server-side fix that isn't deployed". A bare "the container is up" invites `server - live`. Must be paired with the code-only qualifier *and* Arthur's data sentence; the qualifier is what keeps it a hard inference rather than a contradiction. Do **not** use "it's live on prod".
2. **"rows still only on dev" vs "reward tables are re-imported hourly in production"** (`page_liveops_calendar`) **and** vs Douglas's Sep-8 "yes! just finished the deployment" / "I can change it to 5 mins". Only the *deferral* ("not importing them until after the store push") makes both true — see §4.6.
3. **Deleting the withdrawal removes the only Slack statement of the blocker.** After deletion, the truth rests on Arthur's inline comment + the gate sheet + `page_backend_services`/`page_cicd_pipeline`. If the inline comment is worded weakly, nothing else in the universe says "not deployed" — high grading risk.
4. **`review_comments.created_at` must be 5 min before the review's `submitted_at`** (§1.2 house convention). 18:37 vs 18:42 is correct; any other offset contradicts 128 archived rows.
5. **`line` / `diff_hunk` must match the real file.** In `lib/zombies_game/zombie_lane.ex` `import_rewards/0` starts at **112** and its `Logger.info(...)` is **113**; an off-by-N `line` with a mismatched hunk is a visible defect to any reviewer who opens the file.
6. **`review_comments.commit_id` FK.** It must be the inserted commit `5fa55c7a…`; `reviews.commit_id` for the same review stays `NULL` (base approvals are all NULL) — do not "fix" one to match the other.
7. **Linear `cmt_zom567_1`** says "it was the grant job on the backend, fix is in match3d-backend #36, merged" at 18:55:00Z. Literally true (merged ≠ deployed) and it is the seeded Done rationale, but it is the strongest pull toward "fixed". Keep it, and let Arthur's 18:37Z comment be the earlier, more specific statement (18:37 < 18:55 is consistent: he approved with a caveat, then Douglas moved the ticket).
8. **"friday's push" in the deleted withdrawal** — 2025-09-30 is a Tuesday and the actual push is `ZOM-570` "ZM store push - Android Submission #135 / iOS Submission #50" (freeze Oct 1). The row is being deleted, so the hazard goes with it; do not reuse "friday" in the replacement wording.
9. **Slack mirror.** Confirmed INT-01-safe (§6): no Slack copy of #36's review/comment/merge may exist in `C093LEZGF6J` or `C050WGU41HR`, and no push notice for `match3d-backend`.
10. **Real login vs token.** Arthur appears as `EMPLOYEE_0025_GITHUB_USERNAME` in GitHub and `EMPLOYEE_0025_SLACK_ID` in Slack. If any mirror message is ever added, it must use the real login (`arthur.blake`), not the token.

## Summary

1. `github_review_comments` = 11 declared columns in `Evals/references/schema/injection.json`; the completed Douglas task writes 15 (`+ seq, pull_request_review_id, side, subject_type`) — that INSERT is the operative contract.
2. `pull_request_review_id` points at the review row, `commit_id` is the PR head SHA, `path` a real repo path, `position` NULL, `side 'RIGHT'`, `subject_type 'line'`, `created_at` 5 min before the review.
3. Base precedent for a human inline comment on match3d-backend exists (`#4#rc_1`/`rc_2`/`rc_3`, `#4#rc_4`), id pattern `<pr>#rc_<n>` → `…#36#rc_1`.
4. All 30 base APPROVED reviews on match3d-backend have an empty body, so emptying `rev_1` from `'lgtm'` is more realistic, not less.
5. Real paths: `lib/zombies_game/zombie_lane.ex` (`import_rewards/0`), `lib/zombies_game/chest_reward.ex`, `lib/zombies_game/scheduler.ex`, `config/prod.exs`, `priv/repo/migrations/<ts>_*.exs`, `priv/repo/seeds.exs`.
6. Confluence says the engine "imports the reward table for the permanent, level-gated Zombie Lane track", deploys are "Run by hand" with "no deploy step" in CI, and "Migrations do not run on boot" — code and data are separate manual acts.
7. Douglas's Sep-8 DM messages ("I'm making the deployment right now", "yes! just finished the deployment") prove he always announces prod data deploys, and "reward tables are re-imported … hourly" rules out any "the import is stale" wording.
8. Douglas = `EMPLOYEE_0031_SLACK_ID`; the DM's last rows are Vincent 21:58:44Z and Douglas 22:05:03Z, so a 22:2xZ Douglas message conflicts with nobody (22:01–22:04Z reads better).
9. match3d-backend is "not mirrored" (INT-01, `MIRROR_CHANNELS`) — seed no Slack copy of #36 and no push notice.
10. Delete both `C08R6BF4ENN` rows (19:50Z Arthur, 20:02Z Douglas); the parent's thread counts die with it, and the top risks are "container" being read as `server - live` and losing the only Slack statement of the blocker.
