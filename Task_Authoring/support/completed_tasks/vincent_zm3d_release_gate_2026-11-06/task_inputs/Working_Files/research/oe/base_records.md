# Base Records — synth-cut (clock 2025-10-01 07:00Z)

Persona: Vincent Parker, vincent.parker@harmonygames.co, Slack EMPLOYEE_0012_SLACK_ID.
Status: COMPLETE — all 8 items verified; see "Differences from the expected values" at the end.

## 1. Slack #builds C05433XK267

File: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/C05433XK267/2025-09.json` (root JSON array, 1133 records) and `2025-10.json` (4 records).
Author of bot posts: `user: "SLACK_BOT_0005_SLACK_ID"` (index 693, 694, 718, 719, 1120, 1123, 1126, 1128, 1130, 1131) or `user: null` + `subtype: "bot_message"` (index 692, 696, 724, 725, 1113, 1116, 1117, 1121, 1122, 1124, 1125, 1127, 1129, 1132). All text lives in `attachments[0].fallback` / `attachments[0].fields[0].value`; `text` is `""` on every post.

Visibility: `vincent_parker slack C05433XK267: YES` — reason: `persona EMPLOYEE_0012_SLACK_ID is in members of public builds`; evidence `channel=C05433XK267, name=builds, kind=public, members=31`.

### 1(a) 2025-09-22 — Android Submission #127 / iOS Submission #40

| Job | ts (message id) | UTC | verbatim "Started" line |
|---|---|---|---|
| Match3D Android Submission - #127 | `1758544243.280239` (`id 2baca0a9cc8618a8bdc382ff0f833e5d`, ptr `/692`) | 2025-09-22T12:30:43.280239Z | `Match3D Android Submission - #127 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match3D%20Android%20Submission/127/display/redirect|Open>)` |
| Match 3D iOS Submission - #40 | `1758544340.770929` (`id ed20f21250e1a53c5e74ea54a29ae427`, ptr `/693`) | 2025-09-22T12:32:20.770929Z | `Match 3D iOS Submission - #40 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/40/display/redirect|Open>)` |

- No explicit "Started at" clock string exists in these posts: the message `ts` **is** the start time (Jenkins start notice). No branch appears in the start posts.
- Completion posts (branch now stated): `/694` ts `1758544698.778509` (12:38:18Z) `Match 3D iOS Submission - #40 - main Success after 7 min 40 sec … Changes: - Fix pear and orange juice [Arthur Blake]`; `/696` ts `1758544783.817259` (12:39:43Z) `Match3D Android Submission - #127 - main  Success after 9 min 12 sec … Changes: - Fix pear and orange juice [Arthur Blake]` (note double space before `Success` in the Android variant).

### 1(b) 2025-09-30 — iOS Submission #50 / Android Submission #135

| Job | ts | UTC | verbatim "Started" line |
|---|---|---|---|
| Match 3D iOS Submission - #50 | `1759257812.041449` (ptr `/1120`, `id 4c476ced8987c764e1b52dd657acc9a6`, user `SLACK_BOT_0005_SLACK_ID`) | 2025-09-30T18:43:32.041449Z | `Match 3D iOS Submission - #50 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/50/display/redirect|Open>)` |
| Match3D Android Submission - #135 | `1759257934.076209` (ptr `/1122`, user null, `subtype: "bot_message"`, attachment `color: "daa038"`) | 2025-09-30T18:45:34.076209Z | `Match3D Android Submission - #135 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match3D%20Android%20Submission/135/display/redirect|Open>)` |

Both match the expected ts (1759257812.041449 / 1759257934.076209) and expected Started times (18:43:32Z / 18:45:34Z). Branch is `main` in both completion posts:

- `/1123` ts `1759259749.259909` (2025-09-30T19:15:49Z) — `Match 3D iOS Submission - #50 - main Success after 32 min (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/50/display/redirect|Open>)` + `Match 3D iOS Submission - #50 - main Changes:` + `- Bump max level for debug menu [Arthur Blake]`
- `/1124` ts `1759263189.219529` (2025-09-30T20:13:09Z) — `Match3D Android Submission - #135 - main  Success after 1 hr 28 min (…)` then `Match3D Android Submission - #135 - main  Changes:` and a long change list. Verbatim head of the Changes block:
  ```
  - Fixing UI Elements on Home screen [Samuel Turner]
  - updated tornado sprite [Samuel Turner]
  - Guard against none initialized managers [[PERSON_NAME_0068]]
  - Fixing UI Elements on Profile [Samuel Turner]
  - Collect And Win (#468) [noreply]
  - ensuring tutorial shape unsubscribes from tutorial manager event [[PERSON_NAME_0022]]
  - setting broom tutorial as skipable [[PERSON_NAME_0022]]
  - guard against NaN operation [[PERSON_NAME_0068]]
  - fix trampoline and glue count being set to 0 on game start [[PERSON_NAME_0022]]
  - Adding card pack animation [Calvin Price]
  ```
  The #135 Changes list is **not** truncated in source: `fallback` carries the complete 38-line block (36 change bullets), while only `fields[0].value` is renderer-truncated (ends `- Move Collect And Win Scroll to la…`). Tail of the complete block:
  ```
  - Bump max level for debug menu [Arthur Blake]
  - Hide stage number on claimed rewards, Updated CollectAndWin counter visibility for endless and infinite [[PERSON_NAME_0068]]
  - Minor bugs fixed [[PERSON_NAME_0068]]
  - Fixing UI Elements on Powerups popup [Samuel Turner]
  ```
  It does **not** contain the string `Fix season pass main screen instance from join popup` (it does contain the unrelated `- setting addressables for season pass objects [[PERSON_NAME_0022]]`). So the season-pass join-popup fix is absent from the last Submission build of both platforms.

### 1(c) Android build #2028 (2025-09-30) — dev build, not a Submission job

- `/1129` ts `1759268201.182309` (2025-09-30T21:36:41Z), user `null`, `subtype: "bot_message"`:
  `Match3D Android - #2028 Started by changes from [PERSON_NAME_0022] (2 file(s) changed) (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/2028/display/redirect|Open>)`
- `/1132` ts `1759268589.049939` (2025-09-30T21:43:09Z), user `null`, `subtype: "bot_message"`:
  ```
  Match3D Android - #2028 - main Success after 6 min 41 sec (<http://blake.tplinkdns.com:9009/job/Match3D%20Android/2028/display/redirect|Open>)
  Match3D Android - #2028 - main Changes:
  - Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]
  ```
  → Job is **`Match3D Android`** (the internal/CI dev job, URL path `job/Match3D%20Android/2028`), **not** `Match3D Android Submission`. Branch `main`. The Changes text **does** contain `Fix season pass main screen instance from join popup`. Same fix also landed in `Match 3D iOS Internal - #1759` at `/1131` ts `1759268526.402559` (21:42:06Z): `Match 3D iOS Internal - #1759 - main Success after 5 min 38 sec (…)` / `- Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]`.

### 1(extra) Any Submission job started between #50/#135 starts and 2025-10-01T07:00Z?

Scanned `2025-09.json` from `/1120` to end and all 4 records of `2025-10.json`. **No.** The only Submission-post messages after 18:43:32Z are the two *completion* posts (`/1123` iOS #50, `/1124` Android #135). Every start after them is a non-Submission job:
- `/1125` 1759267266.044859 (21:21:06Z) Match3D Android - #2027 Started by changes from [PERSON_NAME_0022] (9 file(s) changed)
- `/1126` 1759267359.156889 (21:22:39Z) Match 3D iOS Internal - #1758 Started by changes from [PERSON_NAME_0022] (991 file(s) changed)
- `/1127` 1759267655.279269 Match3D Android - #2027 - main Success after 6 min 43 sec
- `/1128` 1759267674.571789 Match 3D iOS Internal - #1758 - main Success after 7 min 2 sec
- `/1129` 1759268201.182309 Match3D Android - #2028 Started … (2 file(s) changed)
- `/1130` 1759268212.832329 (21:36:52Z) Match 3D iOS Internal - #1759 Started by changes from [PERSON_NAME_0022] (991 file(s) changed)
- `/1131` 1759268526.402559 Match 3D iOS Internal - #1759 - main Success after 5 min 38 sec
- `/1132` 1759268589.049939 Match3D Android - #2028 - main Success after 6 min 41 sec
- `2025-10.json` `/0` 1759297490.324099 (2025-10-01T05:44:50Z) Match3D Android - #2029 Started by changes from [PERSON_NAME_0022] (6 file(s) changed)
- `2025-10.json` `/1` 1759297516.262669 (05:45:16Z) Match 3D iOS Internal - #1760 Started …
- `2025-10.json` `/2` 1759297851.501209 Match 3D iOS Internal - #1760 - main Success after 6 min 15 sec
- `2025-10.json` `/3` 1759297904.607829 (05:51:44Z) Match3D Android - #2029 - main Success after 7 min 8 sec

## 2. Slack DM D079SNE2TL4

`channels.json` record (verbatim): `{"id": "D079SNE2TL4", "name": "D079SNE2TL4", "is_channel": false, "is_private": false, "is_im": true, "is_mpim": false, "is_archived": false, "is_general": false, "num_members": 5, "topic": "", "purpose": "", "created": "1719336375.000000", "creator": null, "members": [...]}`
Members (5): `EMPLOYEE_0012_SLACK_ID` (Vincent Parker), `EMPLOYEE_0031_SLACK_ID` (**Douglas**, douglas@harmonygames.co), `PERSON_6089_SLACK_ID` (unresolved placeholder, no email), `U05PX318739` (unresolved, no email), `U05Q79KJ160` (unresolved, no email).

Visibility: `vincent_parker slack D079SNE2TL4: YES` — reason: `persona EMPLOYEE_0012_SLACK_ID is in members of im D079SNE2TL4`; evidence `channel=D079SNE2TL4, name=D079SNE2TL4, kind=im, members=5`.

Source: `.../slack/messages/D079SNE2TL4/2025-09.json` (267 records), root array pointers as listed. All base messages 2025-09-29 → 2025-10-01 (there is no `2025-10.json` for this DM):

| ptr | ts | UTC | user | text (verbatim) |
|---|---|---|---|---|
| `/250` | `1759158658.916349` | 2025-09-29T15:10:58Z | EMPLOYEE_0012 (Vincent) | `hey Douglas` |
| `/251` | `1759158661.919799` | 15:11:01Z | Vincent | `have a nice week` |
| `/252` | `1759158676.100249` | 15:11:16Z | Vincent | `are you done with google setup for the google login` |
| `/253` | `1759160428.706709` | 15:40:28Z | Douglas | `Hello [PERSON_NAME_0050]! almost done, I just need to make a new deployment and test, probably it’s done in about 1 hour` |
| `/254` | `1759160473.008739` | 15:41:13Z | Vincent | `ok great` |
| `/255` | `1759160474.352449` | 15:41:14Z | Vincent | `[USERNAME_35317]` (reaction emoji token only) |
| `/256` | `1759164463.327349` | 16:47:43Z | Douglas | `Ok, the deployment is done, I will inform [PERSON_NAME_0120] and Blake as well` |
| `/257` | `1759164588.182699` | 16:49:48Z | Vincent | `[USERNAME_39669]` (emoji token only) |
| `/258` | `1759250246.134229` | 2025-09-30T16:37:26Z | Vincent | `hey Douglas` |
| `/259` | `1759250256.787659` | 16:37:36Z | Vincent | `after the data sycning for sign in` |
| `/260` | `1759250283.689209` | 16:38:03Z | Vincent | `can you have a look at the issue? <https://linear.app/harmonygames-games/issue/ZOM-563/teams-lives-golden-frames-and-names-not-working-on-prod-env>` (+ Linear unfurl: `ZOM-563 Teams' lives, golden frames and names not working on prod env` / `It works great in dev env, but in prod it doesn't.` / `*State*  Todo` / `*Assignee*  [PERSON_NAME_0612]`) |
| `/261` | `1759250935.558129` | 16:48:55Z | Douglas | `Ok [PERSON_NAME_0050] :[USERNAME_26053]:` |
| `/262` | `1759250957.169129` | 16:49:17Z | Vincent | `[USERNAME_35317]` (emoji token only) |
| `/263` | **`1759256193.859279`** | **2025-09-30T18:16:33Z** | Douglas | `Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues` |
| `/264` | `1759256806.682939` | 18:26:46Z | Vincent | ` Thankss will return to you` (leading space; reaction `pray` from Douglas) |
| `/265` | **`1759269524.769369`** | **2025-09-30T21:58:44Z** | Vincent | `Yep it works as expected ` (trailing space; reaction `100` from Douglas) |
| `/266` | `1759269903.971719` | 2025-09-30T22:05:03Z | Douglas | `Go to sleep [PERSON_NAME_0050] :sleeping:` (reaction `joy` from Vincent) |

Injected message (from `01_Universe_Inject.sql` line 126), ts `1759269712.483915` = 2025-09-30T22:01:52Z, i.e. it falls **between** Vincent's 21:58 `Yep it works as expected` (`/265`) and Douglas's 22:05 `Go to sleep` (`/266`):

```
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, ...) VALUES ('ea5e1f0622bf3da5154f00c7fe5426f7', '1759269712.483915', 'D079SNE2TL4', 'message', 'EMPLOYEE_0031_SLACK_ID', 'fyi #36 is rolled out to prod too, the container is up. that''s the code side', NULL, NULL, 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2025-09-30T22:01:52.483915Z', '{}');
```
Unescaped text: `fyi #36 is rolled out to prod too, the container is up. that's the code side` — author Douglas (`EMPLOYEE_0031_SLACK_ID`).

## 3. Slack D0770ET1HV2

`channels.json` verbatim: `{"id": "D0770ET1HV2", "name": "D0770ET1HV2", "is_channel": false, "is_private": false, "is_im": true, "is_mpim": false, "is_archived": false, "is_general": false, "num_members": 5, "topic": "", "purpose": "", "created": "1717692882.000000", "creator": null, ...}`

- Channel type: **IM (`is_im: true`)**, not a channel, not an mpim (`is_mpim: false`), `is_private: false`, 5 members.
- Full member list: `EMPLOYEE_0012_SLACK_ID` (**Vincent Parker**, confirmed), `EMPLOYEE_0026_SLACK_ID` (**Brian Foster**, confirmed), `PERSON_6089_SLACK_ID` (unresolved), `U05PX318739` (unresolved), `U076SL1V4BV` (unresolved).
- Confirmed: Vincent (`EMPLOYEE_0012`) **and** Brian (`EMPLOYEE_0026`, real_name `Brian Foster`) are both members. `num_members: 5` == len(members) 5.

Visibility: `vincent_parker slack D0770ET1HV2: YES` — reason: `persona EMPLOYEE_0012_SLACK_ID is in members of im D0770ET1HV2`; evidence `channel=D0770ET1HV2, name=D0770ET1HV2, kind=im, members=5`.

## 4. Slack #zombie-bugs C08R27X0EAH

`channels.json` verbatim: `{"id": "C08R27X0EAH", "name": "zombie-bugs", "is_channel": true, "is_private": true, "is_im": false, "is_mpim": false, "is_archived": false, "is_general": false, "num_members": 23, "topic": "", "purpose": "All things zombie bugs", "created": "1746543053.000000", "creator": "U05GU6KV231", ...}`
- Name/type: **zombie-bugs**, a **private channel** (`is_channel: true`, `is_private: true`, `is_im: false`), 23 members, purpose `All things zombie bugs`.
- Vincent is a member: `members` contains `EMPLOYEE_0012_SLACK_ID`.
- Visibility: `vincent_parker slack C08R27X0EAH: YES` — reason: `persona EMPLOYEE_0012_SLACK_ID is in members of private zombie-bugs`; evidence `channel=C08R27X0EAH, name=zombie-bugs, kind=private, members=23`.

### 4(a) Base messages 2025-09-29 .. 2025-09-30 mentioning ZOM- keys — NONE

`.../messages/C08R27X0EAH/` holds `2025-05…2025-09.json` (no `2025-10.json`); `2025-09.json` has 1097 records. Every `ZOM-` occurrence in the whole channel's `2025-09.json` file is a Linear unfurl/bot message, and the **latest is `ZOM-534` at ts `1757291682.062479` = 2025-09-08T00:34:42Z**:
```
/POST 1756937326.888839 (2025-09-03T22:08:46Z) [PERSON_NAME_0055] created a new issue ZOM-515 Fix sound bugs in endless mode
      1756937370.752349 (2025-09-03T22:09:30Z) [PERSON_NAME_0055] created a new issue ZOM-516 Endless mode refills one item less than original count
      1756938142.754179 (2025-09-03T22:22:22Z) [PERSON_NAME_0055] created a high priority issue ZOM-517 Monster loses enrage during item refill in endless mode
      1757269816.471559 (2025-09-07T18:30:16Z) [PERSON_NAME_0055] created an urgent issue ZOM-531 Items Unequip at the start of each new session
      1757269996.604199 (2025-09-07T18:33:16Z) [PERSON_NAME_0055] created an urgent issue ZOM-532 Investigate third equipment slot availability before level 75
      1757270077.228629 (2025-09-07T18:34:37Z) [PERSON_NAME_0055] created an urgent issue ZOM-533 Investigate third equipment slot availability before level 75
      1757291682.062479 (2025-09-08T00:34:42Z) [PERSON_NAME_0055] created an urgent issue ZOM-534 Quest points not resetting until app restart in production
```
The only base messages in the 2025-09-29…30 window are the shader thread — **none of them name a ZOM- key**:

| ptr | ts | UTC | user | text |
|---|---|---|---|---|
| `/1090` | `1759154496.651609` | 2025-09-29T14:01:36Z | PERSON_6089_SLACK_ID | (empty text; `subtype: "tabbed_canvas_updated"`) |
| `/1091` | `1759249488.495439` | 2025-09-30T16:24:48Z | Vincent | `i think we should squeeze in the fix for that issue if it's an easy fix. annoying and players can see that for 10 times in a day if they make it that far.` (thread parent, reply_count 4, 1 png attached `F09J3AU9YQL`) |
| `/1092` | `1759250924.694619` | 16:48:44Z | EMPLOYEE_0002 | `<@EMPLOYEE_0012_SLACK_ID> now i can see why you asked if this is Unity version problem, <@EMPLOYEE_0003_SLACK_ID> we have here the same issue like with the zombies. them old shaders dont deform no more the sprites with bones, so i had There a lightSweep Box Variant material that has a shader that used to work before now it doesnt deform the mesh no more :disappointed:. The material added a lightsweep across the gold edges part of the box making it more bling bling.` |
| `/1093` | `1759250986.434259` | 16:49:46Z | EMPLOYEE_0002 | `solution would be to fix the shader to include deformabile ui sprites some how, or just get rid of it and we dont have any lightsweep across the gold parts, it will be more dull but its gona be a quicker fix!` |
| `/1094` | `1759251240.639799` | 16:54:00Z | PERSON_6089_SLACK_ID | (empty text; `tabbed_canvas_updated`) |
| `/1095` | `1759254098.279269` | 17:41:38Z | EMPLOYEE_0003 | `will work on this asap` |
| `/1096` | `1759254162.721499` | 17:42:42Z | Vincent | `<@EMPLOYEE_0004_SLACK_ID> ı think [PERSON_NAME_0022] will handle the problem. It might be about the shader` |

So **every ZOM- mention in #zombie-bugs for 2025-09-29…30 comes from the injection**, not the base.

### 4(b) Injected #zombie-bugs messages (quoted from `01_Universe_Inject.sql`)

Line 118 — **Arthur's candidates post**, ts `1759263900.484190` = 2025-09-30T20:25:00Z, author `EMPLOYEE_0025_SLACK_ID` (Arthur Blake):
```
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, ...) VALUES ('4fa3fdf1ee07241aa316b91d1944af4d', '1759263900.484190', 'C08R27X0EAH', 'message', 'EMPLOYEE_0025_SLACK_ID', 'ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. <@EMPLOYEE_0012_SLACK_ID> QA gate before friday''s go/no-go please, details on ZOM-570', NULL, '1759263900.484190', 1, 1, '1759266600.265963', false, ...);
```
Text: `ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. <@EMPLOYEE_0012_SLACK_ID> QA gate before friday's go/no-go please, details on ZOM-570`

Line 119 — **Brian's reply**, ts `1759266600.265963` = 2025-09-30T21:10:00Z, author `EMPLOYEE_0026_SLACK_ID` (Brian Foster), threaded under `4fa3fdf1ee07241aa316b91d1944af4d` / `1759263900.484190`:
```
VALUES ('186d9d3e4abd5917770091ef4c255b03', '1759266600.265963', 'C08R27X0EAH', 'message', 'EMPLOYEE_0026_SLACK_ID', 'regression matrix green on #135 and #50 from my side :+1:', '4fa3fdf1ee07241aa316b91d1944af4d', '1759263900.484190', 0, 0, NULL, false, ...)
```
Text: `regression matrix green on #135 and #50 from my side :+1:`

Line 116 — ts `1759140300.935009` = 2025-09-29T10:05:00Z, author Vincent:
```
VALUES ('ae66526624c68d840fe3cd4eb15b876d', '1759140300.935009', 'C08R27X0EAH', 'message', 'EMPLOYEE_0012_SLACK_ID', 're-tested on Android #133 / iOS #49: trophy path claim spam is ok now (ZOM-435), consecutive login quest ok too (ZOM-557) :white_check_mark:', ...)
```
Text: `re-tested on Android #133 / iOS #49: trophy path claim spam is ok now (ZOM-435), consecutive login quest ok too (ZOM-557) :white_check_mark:`

Line 117 — ts `1758563100.005758` = 2025-09-22T17:45:00Z, author Vincent:
```
VALUES ('8a0191407ab4551634589a02f5900b7e', '1758563100.005758', 'C08R27X0EAH', 'message', 'EMPLOYEE_0012_SLACK_ID', 'gate for #127 / #40 done, Bug tickets only this time. tab is in my release sheet', ...)
```
Text: `gate for #127 / #40 done, Bug tickets only this time. tab is in my release sheet`

Line 121 — ts `1759274400.792657` = 2025-09-30T23:20:00Z, author Vincent:
```
VALUES ('d9ed6d99a7b4fef0175ab2e3277a8615', '1759274400.792657', 'C08R27X0EAH', 'message', 'EMPLOYEE_0012_SLACK_ID', 'checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 giving lives ok, ZOM-506 zombie lane text ok, ZOM-557 consecutive login ok, ZOM-561 low-end black surfaces ok, ZOM-434 no flying items after backgrounding during load, ZOM-558 weekly board says Level: now. rest tomorrow', ...)
```
Text: `checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 giving lives ok, ZOM-506 zombie lane text ok, ZOM-557 consecutive login ok, ZOM-561 low-end black surfaces ok, ZOM-434 no flying items after backgrounding during load, ZOM-558 weekly board says Level: now. rest tomorrow`

Also injected into this same channel-set (not requested but adjacent): line 120 `1759267800.858041` (2025-09-30T21:30:00Z, Brian) and line 122 `1759272300.342229` (2025-09-30T22:45:00Z, Brian, `update path satırlarını da bitirdim, bi dokümana yazdım seninle paylaştım`) and line 123 `1759160460.731000` (2025-09-29T15:41:00Z, Brian, Turkish ZOM-458 / ZOM-535 report) all target channel `D0770ET1HV2`, not `C08R27X0EAH`.

## 5. Confluence pages

Source file: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/confluence/confluence_working.json`, collection `/pages` (`body` is Confluence storage-format HTML; text below de-tagged, character-exact where quoted).
Visibility (all three): `vincent_parker confluence <page>: YES` — reason: `confluence is unscoped: every persona reads it (acl.md access matrix); existence not checked`; evidence `rule=unscoped`.

### 5.1 `page_qa_runbook` — pointer `/pages/7`

- `/pages/7/title` = `QA Regression Runbook`; `space_id` `space_ENG`, `parent_id` `page_eng_home`, `version` 2, `author_id` `user_EMPLOYEE_0025`, `created_at`/`updated_at` `2025-08-04T10:00:00Z`.

Update-path (N-1/N-2) — `/pages/7/body`, note macro near the top:
> **Test the UPDATE path, not just a fresh install.** The June 2025 progression losses were on **Domino Delights**, and nobody ever reproduced them - the leading hypothesis was the update path, which is why we test it. Every candidate must be installed *over* the last two shipped versions and checked for save/progression loss before we ship. If we only test fresh installs we will miss this entire class of bug again.

> Regression matrix

> Run each row on at least one iOS and one Android device. Both update rows are mandatory - N-1 and N-2 are the last two shipped store versions.
> `Area | Fresh install | Update from N-1 | Update from N-2 | Notes`
> `Save / progression | Pass | Pass | Pass | June 2025 wipe never reproduced in-house; update path is the leading hypothesis`

"If a check fails" (`<h3>If a check fails</h3>`, raw HTML: `<ul><li>File the bug with device, OS version, source build and repro steps, and link it here.</li><li>A failure in any UPDATE column blocks the release - fresh-install-only regressions do not pass the gate.</li>…`):
> - File the bug with device, OS version, source build and repro steps, and link it here.
> - A failure in any UPDATE column blocks the release - fresh-install-only regressions do not pass the gate.
(second bullet is plain `<li>` text with no inline markup; the hyphen is a plain ASCII `-`, not an en dash)

Also in the same page: `Owner … QA (Vincent Parker)`, and the intro clause `if something fails, file the bug and block the release, don't hand-wave it.`; sign-off section: `QA posts the completed matrix in #god-bugs (Domino Delights) or #zombie-bugs (ZM3D) and links it from the release ticket.`

### 5.2 `page_release_checklist` — pointer `/pages/26`

- `/pages/26/title` = `Release Checklist & Store Submission`; `space_id` `space_OPS`, `parent_id` `page_ops_home`, `version` 1, `author_id` `user_EMPLOYEE_0012` (Vincent Parker himself), `created_at`/`updated_at` `2025-07-26T08:50:17Z`.

Update-path warning — `/pages/26/body`, `ac:name="warning"` macro:
> **Always test the UPDATE path from the last two shipped versions (N-1 and N-2), not just a fresh install.** The June 2025 Domino Delights progression losses have not been reproduced and no cause has been established; the leading hypothesis is the update path. A fresh-install-only pass does not clear this gate.

Checklist bullet (Build & QA):
> Update path verified from N-1 *and* N-2: level, coins and unlocks survive the update; no save/progression loss.

Filing a bug with device / OS / source build — final paragraph of `/pages/26/body` (raw HTML `<p>When any check fails, block the release, file the bug with device / OS / source build, and do not ship until it is green.</p>`):
> When any check fails, block the release, file the bug with device / OS / source build, and do not ship until it is green.

(Also, intro: `Owner: Vincent Parker (QA) · Space: OPS. … Do not submit a build until every box below is ticked and QA has signed off — the checklist exists because every item on it maps to a real incident that shipped.`; incident row: `— | Progression wipe, June 2025 | Player progression wiped for real players in production; not reproduced in-house and no cause established. The update path is the leading hypothesis, which is why this gate tests it - a fresh-install-only pass does not clear it. | Test update from N-1 and N-2; confirm save/progression integrity.`)

### 5.3 `page_cicd_pipeline` — pointer `/pages/11`

- `/pages/11/title` = `CI/CD Pipeline & Branching`; `space_id` `space_ENG`, `parent_id` `page_eng_home`, `version` 2, `author_id` `user_EMPLOYEE_0031` (= Douglas), `created_at`/`updated_at` `2025-03-18T03:10:01Z`.

"CI stops" / deploy by hand — `/pages/11/body`, Pipeline table rows (raw HTML `…<td>Merge to main</td><td>The same <code>mix check</code> job runs again on push to main - there is no separate post-merge suite. <strong>CI stops here</strong> - the backend workflow (<code>match3d-backend/.github/workflows/check.yml</code>) runs compile and check on push/PR and has no deploy step.</td></tr><tr><td>Deploy</td><td><strong>Run by hand</strong>: rolling Fargate …`):
> **Merge to main** — The same `mix check` job runs again on push to main - there is no separate post-merge suite. **CI stops here** - the backend workflow (`match3d-backend/.github/workflows/check.yml`) runs compile and check on push/PR and has no deploy step.

> **Deploy** — **Run by hand**: rolling Fargate task-definition update via the `aws ecs update-service` command below; health checks gate promotion. The only CI-driven deploys in the org are the marketing site's S3 syncs (`website/.github/workflows/s3-deploy*.yml`).

Closing paragraph of the same page: `Client (Unity) builds are cut separately and go through staged store rollout - never 100% on day one. See the Ops release checklist.`

## 6. Trello card 68d1eb90bef538c7c5c5599d

Source: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/trello/data.json` — collections `/cards`, `/boards`, `/lists`, `/members`, `/actions`.
Visibility: `vincent_parker trello 68d1eb90bef538c7c5c5599d: YES` — reason: `trello is unscoped: every persona reads it (acl.md access matrix); existence not checked`; evidence `rule=unscoped`.

- Card `/cards/802`: `{"id": "68d1eb90bef538c7c5c5599d", "name": "Fix TECH ISSUES", "idBoard": "6851a6569f3bf818760632ab", "idList": "6851a674975da1fe76e70d93", "desc": "", "idShort": 79, "closed": false, "dateLastActivity": "2025-09-23T00:36:35Z", "idMembers": [], "badges.comments": 0, ...}` — no description, no members assigned, no labels.
- Board `/boards` id `6851a6569f3bf818760632ab` name **`ZM ROADMAP`** (`shortLink` `HSqnngwQ`, org `60c17332e5a2ea61e31cf55a`, base `dateLastActivity` `2025-09-30T17:09:07Z`).
- List `/lists` id `6851a674975da1fe76e70d93` name **`BETA: Oct 10`** in the base (pos 65536.0). ⚠ The *injected* comment actions' `data.list.name` says `BETA: Sep 30`, which does not match the base list name `BETA: Oct 10` — a discrepancy to reconcile.
- Base actions on this card (both by `PERSON_6094_TRELLO_USER_ID`): `/actions/5244` `createCard` `2025-09-23T00:36:32Z` (`data.list.name` `"BETA: Sep 30"` in that historical payload too) and `/actions/5245` `updateCard` `2025-09-23T00:36:35Z`.

### Name resolution

| id | member record | resolved name |
|---|---|---|
| `2162c1ba310341bf318f48b7` (`/members/6`) | `{"id": "2162c1ba310341bf318f48b7", "username": "arthur.blake", "fullName": "Arthur Blake", "initials": "AB", "url": "https://trello.com/arthur.blake"}` | **Arthur Blake** |
| `PERSON_6094_TRELLO_USER_ID` (`/members/2`) | `{"id": "PERSON_6094_TRELLO_USER_ID", "username": "leonard.hayes", "fullName": "Leonard Hayes", "url": "https://trello.com/leonard.hayes"}` | **Leonard Hayes** — yes, Leonard |
| `864e381ee6c844b2a3a7eaf8` (`/members/10`) | `{"username": "vincent.parker", "fullName": "Vincent Parker"}` | Vincent Parker (for reference) |

Action `68dc3ef455344e471b1d2ea9` — **injected** (`01_Universe_Inject.sql` line 277), author `2162c1ba310341bf318f48b7` = **Arthur Blake**:
```
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json) VALUES ('68dc3ef455344e471b1d2ea9', 'commentCard', '2025-09-30T20:35:00Z', '2162c1ba310341bf318f48b7', '6851a6569f3bf818760632ab', '68d1eb90bef538c7c5c5599d', '{"board":{"id":"6851a6569f3bf818760632ab","name":"ZM ROADMAP","shortLink":"HSqnngwQ"},"card":{"id":"68d1eb90bef538c7c5c5599d","idShort":79,"name":"Fix TECH ISSUES","shortLink":"pTbZYXdb"},"idCard":"68d1eb90bef538c7c5c5599d","list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"},"text":"store push: anything that blocks goes on ZOM-570 under the ticket that already exists, no duplicate tickets. only open a new one if nobody filed it yet","textData":{"emoji":{}}}');
```
Comment text: `store push: anything that blocks goes on ZOM-570 under the ticket that already exists, no duplicate tickets. only open a new one if nobody filed it yet`

Second injected comment on the same card (line 278), author `PERSON_6094_TRELLO_USER_ID` = **Leonard Hayes**, `2025-09-30T23:10:00Z`:
`68dc63484a5b2d0a869e758f` → `trophy path on android #135: tapped claim twice fast and got stuck on the path again, only killing the app got me out. same as ZOM-435`

`persona_view can-see vincent_parker trello 68dc3ef455344e471b1d2ea9` → `YES` (`trello is unscoped …`). After injection the card's `badges_json` is set to `"comments":2` and `dateLastActivity` `2025-09-30T23:10:00Z` (SQL line 279), board `dateLastActivity` `2025-09-30T23:10:00Z` (line 280).

## 7. Linear users

Source: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json`, `/users` (41 records). All records use the e-mail as `name` **and** `display_name` (no display names in this export), all `is_active: true`, all `updated_at: "2025-10-01T06:59:59Z"`.
Visibility: `vincent_parker linear <id>: YES` for the checked ids — `linear is unscoped: every persona reads it (acl.md access matrix); existence not checked`, `evidence: rule=unscoped`.

| linear user id | email | resolved person |
|---|---|---|
| `usr_65c76e0b87aa7e9b` | `vincent.parker@harmonygames.co` | **Vincent Parker** (the persona; creator of most ZOM tickets) |
| `usr_fc22d5941b2aeb5c` | `brian.foster@harmonygames.co` | **Brian Foster** |
| `usr_63fffeb4fab5233e` | `leonard.hayes@harmonygames.co` | **Leonard Hayes** |
| `usr_cd7849ec043ab3da` | `douglas@harmonygames.co` | **Douglas** (no surname in the export) |
| `usr_bdf01b53c6a92c5e` | `oliver.brooks@harmonygames.co` | **Oliver Brooks** (assignee of the ZOM bug tickets) |
| `usr_caafeec2804b3a67` | `samuel.turner@harmonygames.co` | **Samuel Turner** |
| `usr_cc3e90160f490686` | `arthur.blake@harmonygames.co` | **Arthur Blake** |

Raw records (identical shape):
```
{"id": "usr_65c76e0b87aa7e9b", "email": "vincent.parker@harmonygames.co", "name": "vincent.parker@harmonygames.co", "display_name": "vincent.parker@harmonygames.co", "avatar_url": null, "is_active": true, "created_at": "2024-04-15T21:29:22Z", "updated_at": "2025-10-01T06:59:59Z"}
{"id": "usr_fc22d5941b2aeb5c", "email": "brian.foster@harmonygames.co", ..., "created_at": "2023-08-04T20:24:28Z", ...}
{"id": "usr_63fffeb4fab5233e", "email": "leonard.hayes@harmonygames.co", ..., "created_at": "2023-08-02T05:31:02Z", ...}
{"id": "usr_cd7849ec043ab3da", "email": "douglas@harmonygames.co", ..., "created_at": "2023-08-08T06:56:56Z", ...}
{"id": "usr_bdf01b53c6a92c5e", "email": "oliver.brooks@harmonygames.co", ..., "created_at": "2024-07-01T13:36:02Z", ...}
{"id": "usr_caafeec2804b3a67", "email": "samuel.turner@harmonygames.co", ..., "created_at": "2024-02-22T20:49:38Z", ...}
{"id": "usr_cc3e90160f490686", "email": "arthur.blake@harmonygames.co", ..., "created_at": "2023-03-22T19:11:39Z", ...}
```
⚠ Two id→person mappings worth flagging for the OE: `usr_cd7849ec043ab3da` is **Douglas** (backend), not a dev, and `usr_cc3e90160f490686` is **Arthur Blake**, while `usr_bdf01b53c6a92c5e` is **Oliver Brooks** (the "fixed, in the build" developer on ZOM-569/ZOM-570-adjacent tickets).

## 8. Drive "submission" search

Command: `hg.py search search gdrive "submission" --limit 60` → `scan_complete: true`, `files_completed: 1` (`gdrive/data.json`, 53,631 `/drive_files` records), 6 match pointers = **3 distinct base files** (each matches on both `name` and `content_path`). No injected doc appears in the base (injection is text-only, never executed).

| drive file id | title | owner_email | shared_with | visibility | trashed | modified | pointer |
|---|---|---|---|---|---|---|---|
| `f_30a9b6ea6247986e819399` | `10_2_2024 Evening Submission Build Bugs.docx` | `robert@harmonygames.co` | 21 entries incl. Vincent (`shared_with_emails_json` populated — see note) | private | false | 2024-10-04T16:49:21Z | `/drive_files/29046` |
| `f_3f60e3ae19099393a03d24` | `6_18_2025 Submission Blocker for level testing.docx` | `robert@harmonygames.co` | `null` / 0 entries | private | false | 2025-08-21T18:07:02Z | `/drive_files/30804` |
| `f_660738f5e775ca939990e9` | `6_18_2025 Submission Blocker for level testing.json` | `robert@harmonygames.co` | `null` / 0 entries | private | false | 2025-08-21T18:07:02Z | `/drive_files/35512` |

Persona visibility:
```
vincent_parker gdrive f_30a9b6ea6247986e819399: YES
  reason:   file is shared with the persona (shared_with_emails)
  evidence: file=f_30a9b6ea6247986e819399, name=10_2_2024 Evening Submission Build Bugs.docx, mime=application/vnd.google-apps.document, owner=robert@harmonygames.co, shared_with=21, visibility=private, modified=2024-10-04T16:49:21Z
vincent_parker gdrive f_3f60e3ae19099393a03d24: NO
  reason:   owned by robert@harmonygames.co; persona not in shared_with_emails (0 entries); visibility=private
  evidence: file=f_3f60e3ae19099393a03d24, name=6_18_2025 Submission Blocker for level testing.docx, mime=application/vnd.google-apps.document, owner=robert@harmonygames.co, shared_with=0, visibility=private, modified=2025-08-21T18:07:02Z
vincent_parker gdrive f_660738f5e775ca939990e9: NO
  reason:   owned by robert@harmonygames.co; persona not in shared_with_emails (0 entries); visibility=private
  evidence: file=f_660738f5e775ca939990e9, name=6_18_2025 Submission Blocker for level testing.json, mime=application/json, owner=robert@harmonygames.co, shared_with=0, visibility=private, modified=2025-08-21T18:07:02Z
```
Note: the raw `/drive_files/29046` record has `shared_with_emails_json: null` in the JSON yet `persona_view` reports `shared_with=21`; the ACL is derived, not stored on the record — do not read `shared_with_emails_json: null` as "not shared".

### 8(a) Injected docs named in the task (SQL lines 221–252; not in the base)

Base-collision check (`hg.py search lookup gdrive --file data.json --pointer /drive_files` over 53,631 records, `scan_complete: true`, `errors: []`): **no match for any of these 7 ids**, i.e. all new records.

| id | name | mime | owner_email | shared_with_emails_json | roles | created/modified | SQL line |
|---|---|---|---|---|---|---|---|
| `f_632c44650df44fe252ee59` | `ZM submission rules.docx` | google-apps.document | `leonard.hayes@harmonygames.co` | `["vincent.parker@harmonygames.co","arthur.blake@harmonygames.co","brian.foster@harmonygames.co"]` | owner Leonard; reader Vincent/Arthur/Brian | 2025-09-23T09:10:00Z | 221 / doc 222 |
| `f_a038a576ca8db6955fae95` | `How ZM submission builds are cut.docx` | google-apps.document | `arthur.blake@harmonygames.co` | `["vincent.parker@harmonygames.co","leonard.hayes@harmonygames.co"]` | owner Arthur; reader Vincent/Leonard | 2025-09-24T14:20:00Z | 234 / doc 235 |
| `f_fcb4f7c9b508088e0d5803` | `1.3.24 hotfix submissions.docx` | google-apps.document | `arthur.blake@harmonygames.co` | `["vincent.parker@harmonygames.co"]` | owner Arthur; reader Vincent | 2025-09-02T15:40:00Z | 243 / doc 244 |
| `f_5ae4332fb6927f84b3afdc` | `ZM beta drops - what blocks.docx` | google-apps.document | `leonard.hayes@harmonygames.co` | `["vincent.parker@harmonygames.co","brian.foster@harmonygames.co"]` | owner Leonard; reader Vincent/Brian | 2025-07-27T17:00:00Z | 248 / doc 249 |
| `f_0ebfccf33076f9dbf086bc` | `ZM3D Release Gate.xlsx` | google-apps.spreadsheet | `vincent.parker@harmonygames.co` | `[]` | owner Vincent | created 2025-09-22T17:05:00Z, modified 2025-09-23T10:05:00Z | 255–258 |
| `f_b91db376f65604b8602657` | `Regression matrix - Android #135 / iOS #50.xlsx` | google-apps.spreadsheet | `brian.foster@harmonygames.co` | `["vincent.parker@harmonygames.co"]` | owner Brian; reader Vincent | created 2025-09-30T20:35:00Z, modified 21:05:00Z | 259–261 |
| `f_5e40215b7d4d24b0455412` | `Update-path run - iOS #50 / Android #135.docx` | google-apps.document | `brian.foster@harmonygames.co` | `["vincent.parker@harmonygames.co"]` | owner Brian; reader Vincent | created 2025-09-30T22:05:00Z, modified 22:35:00Z | 262 / doc 263 |

All four named docs are `visibility: 'private'` with Vincent explicitly in `shared_with_emails_json` + role `reader`, so Vincent is intended to read them. Key injected body lines (verbatim from the SQL):
- `f_a038a576ca8db6955fae95`: `- Since the hotfix train ended on Sep 3, every store submission (the Match3D Android Submission and Match 3D iOS Submission jobs) is cut straight from main. The auth branch submission jobs are sign-in test builds, not store candidates.` / `- A submission has exactly what was on main when its job started (the Started line in #builds) and nothing that landed after, even if the build finishes an hour later. Don't go by the Changes block either: the iOS posts only ever print the newest change, Android prints the whole list.` / `- Backend is separate: match3d-backend changes reach players only when Douglas deploys the backend to prod, by hand (see the CI/CD page, CI stops at the build). Merged is not live.`
- `f_fcb4f7c9b508088e0d5803`: `The 1.3.24 hotfix submissions this week are cut from release/1.3.24_HotFix, not main. …` (historical, Sep 2 — the trap)
- `f_5ae4332fb6927f84b3afdc`: `For the TestFlight beta drops (not store builds): only crashes and progress wipes block a drop. Everything else goes in as a known issue and we ship the beta anyway, testers expect rough edges.` (beta-only — the decoy for a store gate)
- `f_632c44650df44fe252ee59` (Leonard's rules) — blocker definition: `Blocker = crash, freeze, player stuck or can't finish a level (like the orange juice one), lost progress / coins / lives (infinite-lives time included) / boosters / inventory items, or a purchase that doesn't deliver.` and `Blockers go on the release ticket. If in doubt ask me before the go/no-go, not after.`
- `f_5e40215b7d4d24b0455412` update-path table rows: `iPhone 13 | iOS 18.6 | N-1 | iOS Submission #50 | FAIL | After the update the save came back at level 1 with 500 coins; the account was on level 212 with 18,400 coins before. Relaunching didn't bring it back.` and `Pixel 6 | Android 14 | N-1 | Android Submission #135 | Pass | Level, coins and unlocks kept.`

### 8(b) No base duplicates of the four doc titles

`search-many` over `gdrive` (pointer `/drive_files`) and over `gdocs` both returned zero matches, `scan_complete: true`, for `ZM submission` / `beta drops` / `submission builds are cut` / `hotfix submissions`. (The `gdocs` "submission" query does hit ~20 unrelated legacy docs — e.g. `/docs_documents/103` `10_2_2024 Evening Submission Build Bugs`, `/docs_documents/150` `6_18_2025 Submission Blocker for level testing`, `/docs_documents/327` `Bug Checklist – v0.3.21 iOS Submission Candidate`, `/docs_documents/496` `Unclear Submission Boundaries` — none of which are the ZM store-gate rules and none named like the injected ones.)

## Summary Table

| item | id / ts | exact quote (short) | visible to vincent_parker |
|---|---|---|---|
| 1a #builds Android Submission #127 start | `1758544243.280239` / `/692` | `Match3D Android Submission - #127 Started by user Arthur Blake` | YES |
| 1a #builds iOS Submission #40 start | `1758544340.770929` / `/693` | `Match 3D iOS Submission - #40 Started by user Arthur Blake` | YES |
| 1a #40 completion (branch) | `1758544698.778509` / `/694` | `Match 3D iOS Submission - #40 - main Success after 7 min 40 sec` | YES |
| 1a #127 completion (branch) | `1758544783.817259` / `/696` | `Match3D Android Submission - #127 - main  Success after 9 min 12 sec` | YES |
| 1b iOS Submission #50 start | `1759257812.041449` / `/1120` | `Match 3D iOS Submission - #50 Started by user Arthur Blake` | YES |
| 1b Android Submission #135 start | `1759257934.076209` / `/1122` | `Match3D Android Submission - #135 Started by user Arthur Blake` | YES |
| 1b #50 completion | `1759259749.259909` / `/1123` | `Match 3D iOS Submission - #50 - main Success after 32 min` + `- Bump max level for debug menu [Arthur Blake]` | YES |
| 1b #135 completion | `1759263189.219529` / `/1124` | `Match3D Android Submission - #135 - main  Success after 1 hr 28 min` (36-bullet list, no season-pass join-popup fix) | YES |
| 1c Match3D **Android** (dev) #2028 start | `1759268201.182309` / `/1129` | `Match3D Android - #2028 Started by changes from [PERSON_NAME_0022] (2 file(s) changed)` | YES |
| 1c Match3D **Android** (dev) #2028 success | `1759268589.049939` / `/1132` | `- Fix season pass main screen instance from join popup [[PERSON_NAME_0022]]` | YES |
| 1c iOS Internal #1759 success | `1759268526.402559` / `/1131` | `Match 3D iOS Internal - #1759 - main Success after 5 min 38 sec` + same fix | YES |
| 2 DM D079SNE2TL4 Douglas prod deploy | `1759256193.859279` / `/263` | `Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues` | YES |
| 2 DM Vincent confirmation | `1759269524.769369` / `/265` | `Yep it works as expected ` (trailing space) | YES |
| 2 DM injected Douglas #36 (SQL 126) | `1759269712.483915` | `fyi #36 is rolled out to prod too, the container is up. that's the code side` | YES (injected DM) |
| 3 DM D0770ET1HV2 type + members | `D0770ET1HV2` | `is_im: true`, 5 members: EMPLOYEE_0012, EMPLOYEE_0026, PERSON_6089, U05PX318739, U076SL1V4BV | YES |
| 4 #zombie-bugs C08R27X0EAH | `C08R27X0EAH` | private channel, 23 members, purpose `All things zombie bugs` | YES |
| 4 base ZOM- in 09-29..09-30 | — | **none** (last base ZOM- mention is ZOM-534 at `1757291682.062479`, 2025-09-08) | YES |
| 4 injected Arthur candidates (SQL 118) | `1759263900.484190` | `ZM store candidates are up: Android Submission #135 and iOS Submission #50, both from main. …` | YES (injected) |
| 4 injected Brian reply (SQL 119) | `1759266600.265963` | `regression matrix green on #135 and #50 from my side :+1:` | YES (injected) |
| 4 injected Vincent re-test (SQL 116) | `1759140300.935009` | `re-tested on Android #133 / iOS #49: trophy path claim spam is ok now (ZOM-435) …` | YES (injected) |
| 4 injected Vincent gate done (SQL 117) | `1758563100.005758` | `gate for #127 / #40 done, Bug tickets only this time. tab is in my release sheet` | YES (injected) |
| 4 injected Vincent checks (SQL 121) | `1759274400.792657` | `checked the fixes since the sep 22 gate on #135 / #50: ZOM-503 … ZOM-558 weekly board says Level: now. rest tomorrow` | YES (injected) |
| 5 Confluence `page_qa_runbook` | `/pages/7` | `A failure in any UPDATE column blocks the release - fresh-install-only regressions do not pass the gate.` | YES (unscoped) |
| 5 Confluence `page_qa_runbook` bug filing | `/pages/7/body` | `File the bug with device, OS version, source build and repro steps, and link it here.` | YES |
| 5 Confluence `page_release_checklist` | `/pages/26` | `Always test the UPDATE path from the last two shipped versions (N-1 and N-2), not just a fresh install.` | YES (unscoped) |
| 5 Confluence `page_release_checklist` bug filing | `/pages/26/body` | `When any check fails, block the release, file the bug with device / OS / source build, and do not ship until it is green.` | YES |
| 5 Confluence `page_cicd_pipeline` | `/pages/11` | `CI stops here - the backend workflow (match3d-backend/.github/workflows/check.yml) runs compile and check on push/PR and has no deploy step.` / `Run by hand: rolling Fargate task-definition update…` | YES (unscoped) |
| 6 Trello card | `68d1eb90bef538c7c5c5599d` | card `Fix TECH ISSUES` (idShort 79) on board `ZM ROADMAP`, list `BETA: Oct 10` | YES (unscoped) |
| 6 Trello action author | `68dc3ef455344e471b1d2ea9` → `2162c1ba310341bf318f48b7` | **Arthur Blake** (`arthur.blake`); comment: `store push: anything that blocks goes on ZOM-570 under the ticket that already exists, no duplicate tickets. only open a new one if nobody filed it yet` | YES |
| 6 Trello `PERSON_6094_TRELLO_USER_ID` | `/members/2` | **Leonard Hayes** (`leonard.hayes`) — yes, Leonard | YES |
| 7 Linear `usr_65c76e0b87aa7e9b` | — | `vincent.parker@harmonygames.co` — Vincent Parker | YES (unscoped) |
| 7 Linear `usr_fc22d5941b2aeb5c` | — | `brian.foster@harmonygames.co` — Brian Foster | YES (unscoped) |
| 7 Linear `usr_63fffeb4fab5233e` | — | `leonard.hayes@harmonygames.co` — Leonard Hayes | YES (unscoped) |
| 7 Linear `usr_cd7849ec043ab3da` | — | `douglas@harmonygames.co` — Douglas | YES (unscoped) |
| 7 Linear `usr_bdf01b53c6a92c5e` | — | `oliver.brooks@harmonygames.co` — Oliver Brooks | YES (unscoped) |
| 7 Linear `usr_caafeec2804b3a67` | — | `samuel.turner@harmonygames.co` — Samuel Turner | YES (unscoped) |
| 7 Linear `usr_cc3e90160f490686` | — | `arthur.blake@harmonygames.co` — Arthur Blake | YES (unscoped) |
| 8 Drive base hit | `f_30a9b6ea6247986e819399` | `10_2_2024 Evening Submission Build Bugs.docx`, owner robert, shared_with 21 | YES |
| 8 Drive base hit | `f_3f60e3ae19099393a03d24` | `6_18_2025 Submission Blocker for level testing.docx`, owner robert, shared_with 0 | NO |
| 8 Drive base hit | `f_660738f5e775ca939990e9` | `6_18_2025 Submission Blocker for level testing.json`, owner robert, shared_with 0 | NO |
| 8 Drive injected | `f_632c44650df44fe252ee59` | `ZM submission rules.docx` — owner Leonard, reader Vincent/Arthur/Brian | YES (SQL) |
| 8 Drive injected | `f_a038a576ca8db6955fae95` | `How ZM submission builds are cut.docx` — owner Arthur, reader Vincent/Leonard | YES (SQL) |
| 8 Drive injected | `f_fcb4f7c9b508088e0d5803` | `1.3.24 hotfix submissions.docx` — owner Arthur, reader Vincent | YES (SQL) |
| 8 Drive injected | `f_5ae4332fb6927f84b3afdc` | `ZM beta drops - what blocks.docx` — owner Leonard, reader Vincent/Brian | YES (SQL) |

## Differences from the expected values (flagged)

1. Item 1a: the start posts carry **no "Started at" clock time and no branch** — the message `ts` is the start time (12:30:43Z / 12:32:20Z on 2025-09-22); branch `main` is only visible in the completion posts (`/694`, `/696`).
2. Item 1b: #135's `fields[0].value` is renderer-truncated; the full 36-bullet Changes block lives only in `fallback`. It does **not** contain `Fix season pass main screen instance from join popup`.
3. Item 1c: #2028 is the **`Match3D Android` dev job** (not `Match3D Android Submission`), started `by changes from [PERSON_NAME_0022]`, branch `main`, and it **does** contain the season-pass fix; the same fix also appears in `Match 3D iOS Internal - #1759`.
4. Item 1(extra): **no** Submission job started after 18:45:34Z; the last Submission posts are the two completions at 19:15:49Z and 20:13:09Z. Post-18:43 non-Submission starts: Match3D Android #2027/#2028/#2029, iOS Internal #1758/#1759/#1760.
5. Item 2: Vincent's confirmation text has a **trailing space** (`Yep it works as expected `) and there are emoji-only messages (`[USERNAME_35317]`, `[USERNAME_39669]`, `[USERNAME_26053]`) in the same window that a naive read can mistake for content. The injected `#36` line is at 22:01:52Z, before Douglas's base `Go to sleep` at 22:05:03Z.
6. Item 3: `D0770ET1HV2` is flagged `is_im: true` with `num_members: 5` despite being a group-style DM (`is_mpim: false`); three members are unresolved placeholders (`PERSON_6089_SLACK_ID`, `U05PX318739`, `U076SL1V4BV`) with `name`/`email` null.
7. Item 4: **no base #zombie-bugs message on 2025-09-29/30 mentions any ZOM- key** — all such mentions are injected. Also `PERSON_6089_SLACK_ID` posts empty `tabbed_canvas_updated` messages.
8. Item 4: the injected candidate post's `thread_parent_id` equals its own `ts` (`1759263900.484190`) with `thread_ts_legacy` also set — a thread root that is its own parent.
9. Item 6: the base list name is **`BETA: Oct 10`**, but the injected comment `data.list.name` says **`BETA: Sep 30`**.
10. Item 6: both comments on the card are injected; the card's base state has `badges.comments: 0` and `dateLastActivity` 2025-09-23T00:36:35Z.
11. Item 8: base "submission" hits are 3 files (all robert's), and **two of them are NOT visible to Vincent** (`f_3f60…`, `f_6607…`); only `f_30a9b6…` is shared. The `/drive_files/29046` record stores `shared_with_emails_json: null` although the ACL resolves to 21 sharees.
12. All 7 injected Drive ids are absent from the base (no collisions), and none of the four injected doc titles exists in base `gdrive` or `gdocs`.

