# Claims audit — injected Linear comments, slice B

Scope: `linear.linear_comments` rows and the following `linear_issues` UPDATE for ZOM-387, 442, 471, 504, 517, 521, 542, 544, 546, 549, 566 (SQL lines 215–253). ZOM-565 skipped as instructed.
Universe: `Universe_SynthCut/`, clock 2025-10-01 07:00 UTC. Nothing was executed or written except this file.

Path shorthands used in locators:

- `SLACK/` = `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/` (locator = `<channel>/<YYYY-MM>.json #<array index>`, UTC time)
- `LINEAR` = `…/Other_Services/Services_Data/linear/data.json`
- `GH` = `Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json`
- `TREE/` = `…/github/root/harmonygames-Games/match3d/` (snapshot of `main`; contains Unity 6000.2.6f1 from PR #469 merged 09-30T01:50Z and Addressables from PR #473 merged 09-30T15:41Z, so it is `main` at or after 2025-09-30T15:41Z)
- `TRELLO` = `…/Other_Services/Services_Data/trello/data.json`
- `GDOCS` / `GSHEETS` = `…/gdocs/data.json`, `…/gsheets/data.json`

Result in one line: 7 of the 11 comments contradict base (ZOM-544, 566, 387, 471, 542, 549, 521), 1 asserts a mechanism that does not exist in base code (ZOM-517), 3 are not contradicted but carry a tension worth a wording tweak (ZOM-504, 442, 546).

---

## 1. Summary table

| Ticket | Comment id | Claim | Verdict | Evidence locator |
|---|---|---|---|---|
| ZOM-387 | cmt_zom387_1 | Owen Baker is the one working the ticket ("Working down the event list…") | CONTRADICTED | `SLACK/C069FF9Q57S/2025-07.json #16, #18`; `SLACK/D05MBMJDAKV/2025-07.json #37`; `GH pull_requests[2207]` (match3d#319 "ZOM-387", author Arthur Blake); `TRELLO cards[747]` |
| ZOM-387 | cmt_zom387_1 | Work is in progress on 2025-07-25 14:00Z | TIMING CONFLICT | PR #319 opened 07-19T00:40:58Z, merged 07-19T16:55:00Z; `SLACK/D04UGG61DUM/2025-07.json #363` "analytics is in pr" (07-19T01:19:55Z) |
| ZOM-387 | UPDATE | `started_at = 2025-07-25T13:20Z`, In Progress | TIMING CONFLICT | `GH commits[1268]` 1b538c1066 "More key analytics" 2025-07-18T14:59:39Z (Arthur Blake) |
| ZOM-387 | cmt_zom387_1 | "The three events we already had" | CONFIRMED | ticket description; `SLACK/D04UGG61DUM/2025-07.json #254` |
| ZOM-387 | cmt_zom387_1 | "…are unchanged, everything new is additive" | UNCONTRADICTED | PR #319 summary; ZOM-400 (new left_level field) still Todo |
| ZOM-442 | cmt_zom442_1 | Trophy reward redeem fires with super properties attached | CONFIRMED | `TREE/Assets/Scripts/LiveOps/Zombie Lane/Cells/ZombieLaneCellBase.cs:174, 220-229`; `TREE/Assets/Scripts/Utils/AnalyticsManager.cs:164-196, 270-288` |
| ZOM-442 | cmt_zom442_1 | "validation query against the sheet comes back clean" | UNCONTRADICTED (low-risk tension) | sheet tab "Super Properties" lists `player_level`, `ab_test_name`, `ab_test_group`; `GetSuperProperties()` sends none of them |
| ZOM-471 | cmt_zom471_1 | Red dot asset ready and wired to the Plague Race state check | CONTRADICTED | `TREE/Assets/Scripts/LiveOps/PlagueRace/PlagueRaceMenuIcon.cs` (no dot object, NotJoined only enables `_orangeStartButton`); `SLACK/C0880U9751A/2025-08.json #287, #288, #296` |
| ZOM-471 | UPDATE | Done, completed 2025-09-17T16:45Z | CONTRADICTED | no Samuel Turner commit between 09-09T21:25Z and 09-18T20:07Z (`GH commits`); `SLACK/D076PSEBC4D/2025-09.json #72`; `SLACK/D06KV30TPL4/2025-09.json #69-#74` |
| ZOM-504 | cmt_zom504_1 | "Tried to reproduce across a long endless session. Saw it once" | UNCONTRADICTED (tension) | description "it happens in every attempt"; `SLACK/D07GJJBFHA5/2025-09.json #13-#16` (09-03, "couldn't repro without bots") |
| ZOM-504 | cmt_zom504_1 | "object clears on the next throw", "Visual only" | UNCONTRADICTED | description ("stay visually after thrown") |
| ZOM-517 | cmt_zom517_1 | "Enrage state is reapplied after an item refill when the refill flag is on" | CONTRADICTED (mechanism absent in base code) | `TREE/Assets/Scripts/EndlessMode/EndlessObjectsSpawnManager.cs:69-135`; `TREE/Assets/Scripts/Monster/MonsterSpawner.cs:625-646` |
| ZOM-517 | cmt_zom517_1 | "Could not get the monster to lose it while walking in the test board" | UNCONTRADICTED | no retest evidence either way after `SLACK/C08R27X0EAH/2025-09.json #173` |
| ZOM-521 | UPDATE (description) | Tokens and Claimed Cards items unticked | CONFIRMED against children | `LINEAR` ZOM-526 In Progress (started 09-17T15:52:10Z), ZOM-528 In Progress (09-17T15:48:54Z) |
| ZOM-521 | cmt_zom521_1 | "down to the last two items" | CONFIRMED | same |
| ZOM-521 | cmt_zom521_1 | "both polish on existing effects" | CONTRADICTED | `SLACK/D0770ET6WBW/2025-09.json #199, #262`; `SLACK/D05U73FNDDL/2025-09.json #112`; `GH pull_requests[2380]` (#475 merged 09-30T16:09Z) |
| ZOM-521 | cmt_zom521_1 | "Everything the live-ops side asked for is in" | CONTRADICTED | `SLACK/D0770ET6WBW/2025-09.json #212, #252, #253, #259`; `GH pull_requests[2377]` (#472 merged 09-30T15:53Z) |
| ZOM-542 | cmt_zom542_1 | Home screen and victory score layouts are in for endless and boss arena | CONTRADICTED | `TREE/Assets/Scripts/EndlessMode/EndlessModeRewardScreen.cs`, `InfiniteBossModeRewardScreen.cs`, `TREE/Assets/Scripts/LiveOps/Endless/EndlessScreen.cs:42`, `…/InfiniteBoss/InfiniteBossScreen.cs:41` |
| ZOM-542 | UPDATE | Done, completed 2025-09-22T18:40Z | CONTRADICTED | `SLACK/C05KNDCHAAG/2025-09.json #32` (09-22T16:25:02Z); `GH commits` (Samuel Turner) |
| ZOM-542 | cmt_zom542_1 | "Regression pass on the mode switch looks clean" | UNCONTRADICTED (nothing bears on it) | — |
| ZOM-544 | cmt_zom544_1 | Framework "is being built on the account layer first" | CONTRADICTED | `SLACK/D07GJJBFHA5/2025-09.json #591, #760, #785`; `SLACK/CD843DBC4C3E/2025-09.json #20, #36` |
| ZOM-544 | cmt_zom544_1 | "no visible change until the settings panel is ready for it" | CONTRADICTED | same, plus `GDOCS` "POD_ PROTOTYPE - 2025_09_29 08_56 PDT" transcript 00:15:21-00:17:46 |
| ZOM-546 | cmt_zom546_1 | Refill counts hold level across a long endless run | UNCONTRADICTED | `TRELLO actions[5234]` (09-22 still lists the bug); PRs #453 (merged 09-22T16:13Z), #457 (09-23T16:38Z) |
| ZOM-546 | cmt_zom546_1 | Author Owen Baker tested it | UNCONTRADICTED (author tension) | `SLACK/C0880U9751A/2025-09.json #165` (creation unfurl: Assignee [PERSON_NAME_0121] = EMPLOYEE_0032), `#183` |
| ZOM-549 | cmt_zom549_1 | New left_level field is in the payload | CONTRADICTED | `TREE/Assets/Scripts/Utils/AnalyticsManager.cs:418-451`; `GH` PR match3d#451 (merged 09-17T14:55:02Z) |
| ZOM-549 | cmt_zom549_1 | New endless_left fields are in the payload | CONFIRMED for 3 of 4 | `AnalyticsManager.cs:473-511` (`endless_level`, `nuke_damage_total`, `total_equipped_power`; no `player_cpm`, only pre-existing `cpm`) |
| ZOM-549 | cmt_zom549_1 | "validation query returns them per the sheet" | CONTRADICTED for left_level | `GSHEETS` "Zombie Match Data Dictionary Firebase", tab `left_level`, row `total_equipped_power` |
| ZOM-566 | cmt_zom566_1 | Event list is mapped to the sheet | CONFIRMED | `GSHEETS` tabs `Collect&Win_start`, `Collect&Win_redeem`; `SLACK/D07E9PSQB6W/2025-09.json #5-#9` |
| ZOM-566 | cmt_zom566_1 | "the first events are landing in the pipeline" at 19:40Z | TIMING CONFLICT | `GH commits[2230]` 31ee4178bd 2025-09-30T22:23:02Z; `GH pull_requests[2382]` (#477 opened 22:26:30Z, still open); `SLACK/D05SG9H1CFM/2025-09.json #416` (22:08:45Z) |
| ZOM-566 | cmt_zom566_1 | "ahead of the beta" | CONFIRMED | `TRELLO` list "BETA: Oct 10" (cards[708], cards[778]) |
| ZOM-566 | UPDATE | In Progress, started 2025-09-30T17:20Z | CONFIRMED | `SLACK/C09EVVCFHKR/2025-09.json #99` (16:49:10Z); `SLACK/D05S1S2AB5M/2025-09.json #35` (17:13:12Z) |

---

## 2. Contradictions, ranked, with the smallest fix

### 1. ZOM-544 — comment contradicts the author's own base messages

Injected (Vincent Parker, 2025-09-29T15:35Z): "Google Play and Apple sign-in framework is being built on the account layer first, so there is no visible change until the settings panel is ready for it."

Base:

- `SLACK/D07GJJBFHA5/2025-09.json #591` 09-22T14:41:10Z, EMPLOYEE_0032: "made a build, probably not gonna work from first time, but please check / manual sign in from menu settings, build 1668"
- `#760` 09-24T11:18:14Z, Vincent Parker: "I was able to see the login pop up but then the issue you mentioned."
- `SLACK/CD843DBC4C3E/2025-09.json #20` 09-24T17:46:07Z, Vincent Parker: "I tested out the flow. I can sign in but my progress were not loaded after ı reinstalled the app."
- `#36` 09-25T14:52:11Z, Vincent Parker: "Based on my latest tests on Apple sign in here the situation about stored data. • Levels completed :no_entry: …"
- `SLACK/D07GJJBFHA5/2025-09.json #868` 09-26T13:50:35Z, EMPLOYEE_0032: "working on adding sync for levels and currencies"
- `GDOCS` "POD_ PROTOTYPE - 2025_09_29 08_56 PDT - Notes by G" (meeting 21 minutes after the comment): login works, cards are not synced, Google Play config pending on backend.

Sign-in was visible in the settings menu from 09-22 and Vincent had signed in by 09-24.

Fix (text only, same author and time): "Apple sign-in works from the settings menu on the auth branch, but progress does not restore yet: levels, currencies and cards are not synced. Google Play login is still waiting on the backend setup." True at 15:35Z: Vincent asks Douglas "are you done with google setup for the google login" at 15:11:16Z (`SLACK/D079SNE2TL4/2025-09.json #252`), and Douglas reports it done at 16:48:51Z (`SLACK/CD843DBC4C3E/2025-09.json #39`).

### 2. ZOM-566 — events "landing" before the code that sends them existed

Injected (Owen Baker, 2025-09-30T19:40Z): "…the first events are landing in the pipeline ahead of the beta."

Base:

- `SLACK/D05S1S2AB5M/2025-09.json #35` 17:13:12Z, Owen: "Do we have an analytics manager in zombie just like in DD?"
- `SLACK/D07J501DBNE/2025-09.json #30` 20:55:10Z, Owen: "I'll make this change and send it with the pr I'm working right now"
- `SLACK/D05SG9H1CFM/2025-09.json #416` 22:08:45Z, Owen: "estoy agregando eventos de analytics"
- `GH commits[2230]` 31ee4178bd, 2025-09-30T22:23:02Z, "Added analytics events to collect and win"
- `GH pull_requests[2382]` match3d#477 "Collect And Win Analytics and title change", created 22:26:30Z, state open, merged false at the clock
- `TREE/Assets/Scripts/UI/CollectAndWin/*.cs` on `main`: no `LogEvent` call at all

Same class of error as ZOM-565. The state change (In Progress, started 17:20Z) is fine.

Fix, either:

- keep 19:40Z and change the second clause: "Collect and Win event list is mapped to the sheet (start and redeem). Wiring both into the analytics manager now, ahead of the beta."; or
- move comment and `updated_at` to 2025-09-30T22:40:00Z and say "…mapped to the sheet, start and redeem events are up in PR #477 ahead of the beta."

### 3. ZOM-387 — wrong person and six days late

Injected (Owen Baker, 2025-07-25T14:00Z): "Working down the event list from the sheet tab by tab…"; UPDATE sets In Progress, `started_at = 2025-07-25T13:20Z`.

Base:

- `SLACK/C069FF9Q57S/2025-07.json #16` 07-15T02:33:50Z, Leonard Hayes: "I'm also working on a bigger analytics ticket that @Arthur Blake will complete over the next few days"; `#18` 06:28:53Z: "@Arthur Blake's giant analytics ticket is here"
- `GH commits[1268]` 1b538c1066 "More key analytics" 2025-07-18T14:59:39Z, `commits[5984]` "More IAP analytics." 15:07:15Z (Arthur Blake)
- `GH pull_requests[2207]` match3d#319, title "ZOM-387", head `Blake/ZOM-387`, author Arthur Blake, created 07-19T00:40:58Z, merged 07-19T16:55:00Z (also `SLACK/C093LEZGF6J/2025-07.json #589, #606`)
- `SLACK/D04UGG61DUM/2025-07.json #363` 07-19T01:19:55Z, Arthur: "analytics is in pr"
- `SLACK/C069FF9Q57S/2025-07.json #19-#20` 07-26T23:49Z, Leonard already charting the new events from app version 0.3.86
- Owen Baker on 07-25 is on the Teams feature only (`SLACK/C0880U9751A/2025-07.json #851` 04:58:53Z "Teams Latest builds"); a scan of every message by or to him 07-17…08-03 finds no analytics work
- `TRELLO cards[747]` "Adding Analytics for Missing Events (Leonard/Blake)", marked complete 2025-08-20 (`actions[5098]`)

Fix: `author_id = 'usr_cc3e90160f490686'` (Arthur Blake), comment `created_at`/`updated_at` = 2025-07-18T15:20:00Z, `started_at = '2025-07-18T14:40:00Z'`. Text can stay as is. If Owen must remain the author there is no date that makes the claim true.

### 4. ZOM-471 — marked Done for work base shows undone and argued against

Injected (Samuel Turner, 2025-09-17T16:45Z, state Done): "Red dot asset is ready and wired to the Plague Race state check, it only shows while the player is outside a race."

Base:

- `SLACK/C0880U9751A/2025-08.json #287` 08-13T18:20:02Z, Vincent Parker: "i think it's annoying, it already has start button"; `#288` 18:32:48Z, Leonard Hayes: "yeah, we don't need it! cancel the ticket @Robert lol"; `#296` 20:28:23Z: "I don't think we should do it"
- `TREE/Assets/Scripts/LiveOps/PlagueRace/PlagueRaceMenuIcon.cs` on `main` (after 09-30T15:41Z): no warning/dot field; `NotJoined` only does `_orangeStartButton.SetActive(true)`. The sibling icons do have one (`QuestIcon._warning`, `ZombieLaneIcon._warningDot`, `EndlessMenuIcon._exclamationMarkObject`).
- Samuel Turner has no commit between 7f8d8a5936 (09-09T21:25:56Z) and 9b1b71d3a6 (09-18T20:07:41Z, vision bot); `SLACK/D076PSEBC4D/2025-09.json #72` 09-15T17:05:14Z, Leonard: "Samuel Blake'a yardim ediyor" (Samuel is helping Blake); `SLACK/D06KV30TPL4/2025-09.json #69-#74` show him on the vision-bot CLI 09-16…09-18.
- Base ticket still Todo after the 2025-09-30T12:40Z grooming pass that closed his ZOM-498 and ZOM-536.

Caveat: a prefab-only change could not be checked; no asset in the tree references the `PlagueRaceMenuIcon` script GUID.

Fix: drop the state change (leave Todo, no `completed_at`) and replace the text with something base-true, e.g. "Not started. The icon already shows the Start button when the player is outside a race, so the red dot is not wired; waiting on the call from the Aug 13 thread."

### 5. ZOM-542 — marked Done; neither layout exists on `main` a week later

Injected (Samuel Turner, 2025-09-22T18:40Z, state Done): "Home screen and victory score layouts are in for endless and boss arena. Regression pass on the mode switch looks clean."

Base:

- The ticket asks for today's score + event total score + ranking on the home screen, and session / total / best score on the victory screen (`SLACK/C08R8CHB0QL/2025-09.json #89, #90`).
- On `main`: `EndlessScreen.cs:42` and `InfiniteBossScreen.cs:41` show only "Today's High Score: {blob.BestScore}"; `EndlessModeRewardScreen.cs` and `InfiniteBossModeRewardScreen.cs` show kills/damage, coins and time only. A case-insensitive search of every file under `TREE/Assets` for "best score", "total score", "event score", "new record", "session score" returns nothing.
- `SLACK/C05KNDCHAAG/2025-09.json #32` 09-22T16:25:02Z, Julia Lawson's status post two hours before the injected Done: "Samuel is fixing the list of bugs [Vincent] gave him."
- Samuel's only commits 09-10…09-22 are vision-bot tooling and one crash fix (9b1b71d3a6, 1f84a79866, 2bba1f3476). "Fixing UI Elements on Home screen" (0e5a3c9d1f, 09-23T00:12:31Z) is ZOM-498 (Play button and bins position).
- `SLACK/D05TZ6N23F1/2025-09.json #316` 09-26T11:29:20Z, Martin Walsh: the boss arena screens were implemented by EMPLOYEE_0032, not Samuel.

Fix: drop the state change and reword, e.g. "Martin's mockups are in the comments above. Home screen and victory score changes for endless and boss arena are not in the build yet, picking this up after the UI polish list."

### 6. ZOM-549 — left_level field is not in the payload

Injected (Vincent Parker, 2025-09-26T16:50Z): "The new left_level and endless_left fields are in the payloads and the validation query returns them per the sheet."

Base:

- `TREE/Assets/Scripts/Utils/AnalyticsManager.cs:418-451`: the `left_level` event has no `total_equipped_power`.
- `:473-511`: `endless_left` has `nuke_damage_total`, `endless_level`, `total_equipped_power`; it has `cpm` but no `player_cpm`.
- `GH` PR match3d#451 "Infinite/endless analytics, balance changes" (merged 09-17T14:55:02Z): "Endless: Nuke Damage Total, Level Name, Total Equipped Power. Boss Arena: …" — left_level not touched.
- `GSHEETS` tab `left_level` does list `total_equipped_power | total attack power equipped by the player | Float | 3556.3`.

Fix: "The new endless_left fields (endless_level, nuke_damage_total, total_equipped_power) are in the payload. left_level does not send total_equipped_power yet."

### 7. ZOM-521 — two sentences of the comment contradict Calvin's own DMs

Injected (Calvin Price, 2025-09-26T17:25Z): "…down to the last two items, both polish on existing effects. Everything the live-ops side asked for is in."

Base:

- `SLACK/D0770ET6WBW/2025-09.json #212` 09-18T17:10:03Z, Brian Foster's queue order: "2. Collect&Win tokens travelling the icon 3. Season Pass tokens travelling the icon 4. Axe arena tokens travelling the icon"
- `#252` 09-24T16:22:28Z, Brian: "Because collect&win event is almost ready to merge, we need to integrate it to queue manager too"; `#253` Calvin: "Yeah I'll need to add it to the queue manager once is merged"; `#259` 09-25T14:02:20Z, Calvin: "still waiting to implement on [Owen]'s branch"
- `GH pull_requests[2377]` match3d#472 "Implement Win&Collect into Queue Manager", merged 09-30T15:53:04Z
- Cards item: `SLACK/D05U73FNDDL/2025-09.json #112` 09-24T17:00:49Z, Calvin: "once I finish implementing the cards VFX"; `SLACK/D0770ET6WBW/2025-09.json #262` 09-29T19:20:08Z: first test build "for card animation VFX implementation. let me know if that's okay to make a PR later"; PR #475 "Adding card pack animation" merged 09-30T16:09:15Z.

The first clause and the description edit are fine (ZOM-526 and ZOM-528 are both In Progress in base).

Fix: "Master VFX checklist is down to the last two items: tokens traveling to live-ops and claimed cards traveling to inventory. Cards VFX is what I am on now."

### 8. ZOM-517 — "the refill flag" does not exist

Injected (Robert, 2025-09-18T14:50Z): "Enrage state is reapplied after an item refill when the refill flag is on."

Base: `EndlessObjectsSpawnManager.Refill()` never touches monsters or enrage; enrage is only set in `MonsterSpawner` (lines 329, 567, 626-641). There is no refill flag anywhere under `TREE/Assets/Scripts`.

Also weak on timing: at 14:48-14:58Z Robert is posting continuously in `SLACK/C096HFA5Z8W/2025-09.json #235-#247` (bridge-pitch).

Fix: make it an observation: "Retested on the endless test board. Enraged monsters kept their enrage through item refills, could not get one to lose it while walking." Optionally move it to a quieter slot, e.g. 2025-09-18T17:40Z.

### 9. ZOM-504 — tension with the description and the 09-03 DM (not a hard contradiction)

Description (same author): "it happens in every attempt". `SLACK/D07GJJBFHA5/2025-09.json #14-#16` 09-03: EMPLOYEE_0032 "did u run a level w bot?" — Vincent "yes, let me try without a bot" — "yeah, I couldn't repro without bots". The injected "Saw it once" ignores the bot finding.

Fix: "Still only shows up with the bot running; in manual play across a long endless session I could not get it. When it happens the object clears on the next throw. Visual only, no board state affected."

### 10. ZOM-442 — "comes back clean" is slightly stronger than base supports

The event, `trophy_level`, `chest_content` and six super properties are all in code. The sheet's Super Properties tab also lists `player_level`, `ab_test_name`, `ab_test_group`, which `GetSuperProperties()` does not send.

Fix (optional): "…fires with the super properties attached, trophy_level and chest_content match the sheet tab."

### 11. ZOM-546 — author is the Linear assignee, but base Slack shows someone else owning the bug

`LINEAR` has assignee Owen Baker; the creation unfurl shows Assignee [PERSON_NAME_0121] (= EMPLOYEE_0032), and `SLACK/C0880U9751A/2025-09.json #183` 09-16T12:44:52Z EMPLOYEE_0032: "i know, trying to fix it from friday". Owen's Slack 09-22…09-26 is Collect & Win only, and 14:05Z is outside his usual hours (first message that day 18:20Z).

No change strictly needed. Safer option: `author_id = 'usr_EMPLOYEE_0032'` with the same text, or move Owen's comment to about 19:00Z.

---

## 3. Per-ticket notes: base ticket fit, lifecycle, searches run

Common to all tickets: full-corpus regex scan of all 4,840 Slack message files for the eleven ticket ids (text and attachment JSON, which also covers URL slugs); the same id scan over GitHub PR titles/bodies/head refs, branches, commit messages, reviews, review comments and PR comments; id grep over Trello, Confluence, Docs, Sheets, Slides, Calendar and Gmail threads. Only Trello (ZOM-546) and one Gmail Slack-digest (ZOM-442) hit outside Slack/GitHub. Snowflake was grepped for the analytics event and field names (zero hits, so it has no bearing). Base `comments` array in Linear is empty.

**ZOM-387** — base: Todo, assignee Arthur Blake, creator Leonard Hayes, created 07-15T06:26:50Z, updated 07-27T20:46:47Z; children ZOM-442, ZOM-444. Post-SQL lifecycle is internally consistent but conflicts with base as in §2.3. Searches: `#analytics` 07-10…08-01 read in full; Arthur–Leonard DM `D04UGG61DUM` 07-14…07-28 read in full; all Owen Baker messages 07-23…07-29; regex `analytic|event list|super propert|instrument|firebase|sheet|tab|giant` over every message by, to or in a DM with Owen 07-17…08-03; Arthur Blake messages matching `analytic|event|super propert|instrument` 07-15…08-01; GitHub commits matching `analytic|redeem` since 07-15; Trello cards matching `analytic`.

**ZOM-442** — base: In Validation, assignee Oliver Brooks, started 07-30T18:02:11Z. Author is the assignee; only `updated_at` moves. Searches: Slack regex `trophy[_ ]re(ward|deem)|trophy_road|tropy|trophy_path|trophy…analytic` 07-15…10-01; Leonard–Brian DM `D076PSEBC4D` 09-17 read; Oliver Brooks messages 09-17…09-27 matching `analytic|event|trophy|validat|season|sheet|log`; repo grep for the three event-name spellings; GitHub commit, review and diff-hunk search for the same; sheet tabs `trophy_reward_redeem` and `Super Properties` read.

**ZOM-471** — base: Todo, assignee Samuel Turner, creator Robert, label Hot Fix - Global Launch. Searches: Slack regex `red[ -]?dot|warning ?dot|notification dot|punto rojo|kırmızı nokta` 08-01…10-01 (42 hits read); creating thread read in full; GitHub commits/PRs/branches matching `plague|race|dot|warning` since 08-01; all Samuel Turner commits since 09-05; every Samuel-related Slack message since 09-10 (131 read); repo grep `warning ?dot|_warning|reddot|exclamation`; `PlagueRaceMenuIcon.cs` read in full; PR #456 body and reviews.

**ZOM-504** — base: Backlog, priority 0, assignee EMPLOYEE_0032 (originally Arthur Blake), creator Vincent Parker, updated 09-15T15:10:41Z. Author is the creator. Searches: Slack regex `persist|stay(s|ed|ing)? (visual|on|in)|ghost|objects? (stay|remain)|after thrown|in the deck|kalıyor` 08-15…10-01 (33 hits read); Vincent–EMPLOYEE_0032 DM `D07GJJBFHA5` around 08-25, 09-03, 09-15/16 and all of 09-22…09-30; Trello "Minor Bugs to Fix" card (ZOM-504 not listed); pod meeting notes 09-01, 09-02, 09-04, 09-29.

**ZOM-517** — base: Backlog, assignee EMPLOYEE_0032, creator Robert, never updated. Author is the original reporter. Searches: Slack regex `enrage|ZOM-517|refill flag` 08-20…10-01 (49 hits read); creating thread; EMPLOYEE_0032 commits and PRs 09-01…10-01; repo grep `enrage` in EndlessMode and Monster scripts, `refill` with `flag|bool|enrage|reapply`; Docs and Confluence regex for enrage near refill (none).

**ZOM-521** — base: In Progress, assignee Calvin Price, creator Brian Foster, started and updated 09-17T15:50:49Z; children ZOM-523/524/525/527 Done, ZOM-526/528 In Progress. Author is the assignee. The base Slack unfurl at 09-17T15:51:55Z (`SLACK/D0770ET6WBW/2025-09.json #198`) shows Tokens ticked; the injected ZOM-526 comment (09-26T15:40Z, Brian) says he unticked it, so the description edit is coherent in time. Searches: Calvin–Brian DM 09-15…09-30 read in full; Marcus–Calvin DM `D05U73FNDDL` 09-24…09-30 read in full; Calvin's messages 09-26; PRs #459, #465, #472, #475 bodies; Trello card "Reward Animations (VFX)" (marked complete 09-18T15:39:07Z); "ZM VFX Polish 07.30.2025" doc; 09-29 pod transcript.

**ZOM-542** — base: state "Regression", assignee Samuel Turner (creation unfurl says Martin Walsh), creator Robert, never updated; 12 image attachments with `surface: comment`. In this workspace "Regression" is an unstarted triage state for bug reports, not a test phase. Searches: creating thread read in full; Slack regex `victory|score screen|best score|today's score|total score|win ?screen|home ?screen|ZOM-542` 09-12…10-01; `#zombie-art` and every DM/group DM containing Martin Walsh 09-15…09-30 for endless / boss arena / score / home screen; Samuel Turner commits and Slack as for ZOM-471; repo grep for the score labels across all assets; the four screen scripts read.

**ZOM-544** — base: In Progress, assignee EMPLOYEE_0032, creator Vincent Parker, started 09-22T13:41:02Z. Author is the creator. Searches: `D07GJJBFHA5` 09-16 and 09-22…09-30 read in full; sign-in group DM `CD843DBC4C3E` read in full; Slack regex `sign.?in|login|log in|auth|google play|apple` 09-22…09-30 across all other channels; EMPLOYEE_0032 commits (`Auth` 09-22T14:33:34Z, `Apple auth update` 09-24, `Test player restore` 09-25, Google Play 09-30); Trello card "Google/Apple Login"; 09-29 pod transcript; Confluence support playbook (no bearing).

**ZOM-546** — base: Todo, assignee Owen Baker in `LINEAR`, creator Robert, never updated. Searches: Slack regex `refill|spawn… (less|fewer)|less and less|fewer items|ZOM-546|ZOM-516|spawning algorithm` 09-01…10-01 (56 hits read); creating thread; Owen Baker messages 09-22…09-26; Vincent–Oliver DM around 09-25; Trello card history (`actions[5122…5250]`); PRs #453, #457; unfurl assignee extraction for ZOM-546/554/562.

**ZOM-549** — base: In Validation, assignee EMPLOYEE_0032, creator Leonard Hayes, started 09-22T13:40:39Z. Author is neither assignee nor creator but is the QA lead who ran the 09-22 grooming pass and uses Metabase. Searches: Slack regex `endless_left|left_level|equipped_power|nuke_damage|player_cpm|bossarena_|ZOM-549|ZOM-548|in validation|validation query|validate` 09-14…10-01; who runs queries in base (`metabase|bigquery|sql|query|validat` by author); GitHub PR bodies, reviews and comments for the field names; `AnalyticsManager.cs` both event blocks read; sheet tabs `left_level`, `endless_left`, `bossarena_left`.

**ZOM-566** — base: Todo, assignee Owen Baker, creator Brian Foster, created 09-30T16:26:02Z. Author is the assignee. Searches: every message by, to or in a DM with Owen and every `zm-collect-win` / Collect & Win message from 09-29T12:00Z to the clock (60 read); Owen's commits 09-30 and PRs #468, #470, #477; repo grep for analytics calls in the Collect and Win scripts; sheet tabs; Trello card "Win and Collect"; regex `beta` over late-September Slack and the Trello lists.

Statements in base that someone commented on or changed a ticket:

- ZOM-542: `SLACK/C08R8CHB0QL/2025-09.json #94` 09-15T16:24:21Z, Martin Walsh: "There are few comments with mockups in the ticket". Together with the 12 `surface: comment` attachments this means earlier comments existed, yet the injected comment has `sequence = 1`. Same for ZOM-471 (one `surface: comment` image, ticket "Synced with Slack"). Low risk because base exports no comments for any issue, but a reviewer could raise it.
- ZOM-521: `SLACK/D0770ET6WBW/2025-09.json #198` 09-17T15:51:55Z, Calvin: "I've updated the Master ticket VFX implementation and the remaining tickets" — matches base `updated_at` 15:50:49Z; nothing in base refers to a 09-26 comment.
- No such statement for the other tickets.

Not checked: Unity prefab and scene contents for ZOM-471 and ZOM-542 beyond text search (script GUIDs are not referenced in the exported tree), and the image attachments themselves.

## 4. Outside this slice, noticed in passing

`cmt_zom526_1` (Brian Foster, 2025-09-24T17:30Z) says "the Collect and Win trigger is in". Base one hour earlier (`SLACK/D0770ET6WBW/2025-09.json #252-#253`, 16:22-16:45Z) says it still has to be integrated once Collect & Win merges, and PR #472 only merged 09-30T15:53Z. Worth a look by whoever owns that ticket.
