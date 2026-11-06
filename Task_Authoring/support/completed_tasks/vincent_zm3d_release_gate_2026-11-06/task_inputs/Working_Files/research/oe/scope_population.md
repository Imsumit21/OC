# Scope Population Research — SynthCut (clock 2025-10-01 07:00Z)

Status: COMPLETE.

## 0. Method / sources

| Item | Value |
|---|---|
| Universe | synth-cut (clock 2025-10-01 07:00Z) |
| Base Linear export | `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json` — top-level keys `users` (41), `teams` (5), `projects` (2), `issues` (3687), `comments` (0), `team_memberships` (76), `attachments` (1955) |
| Overlay | `Task_Authoring/task_inputs/01_Universe_Inject.sql` — read as text, never executed. For Linear it does **16** `INSERT INTO linear.linear_issues` (ZOM-567…ZOM-580 = 14, plus ART-793, DES-313), **58** `INSERT INTO linear.linear_comments` (`cmt_*`, all ids unique), and **26** `UPDATE linear.linear_issues SET updated_at = …` only. No `state_id`, `completed_at`, `labels` or `team_id` is changed by any UPDATE. |
| Combined population | 3703 issues (3687 base + 16 overlay). No id collisions between base and overlay (`base_ids ∩ overlay_ids = ∅`). |
| Slack source (cut instant) | `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/messages/C05433XK267/2025-09.json`, channel `C05433XK267` = **#builds** (31 members) |
| Expected answer set | `Task_Authoring/task_inputs/Working_Files/solver/truth.json` — 132 keys |

Note on comments: the base export's top-level `linear.comments` is **empty (0 rows)**; every Linear comment in this universe comes from the overlay (`cmt_*`). Base issue records carry no nested comment array.

### The cut instant (verified in Slack, not assumed)

Scope rule quote (Leonard): "Scope: every ZM ticket that's still open (any state but Done, Canceled or Duplicate), whatever team or label (ART or DES tickets with ZM in the title count too), plus everything that moved to Done after the last gate's builds were cut (Android #127 / iOS #40 on Sep 22). Release tickets, ZOM-359 and ZOM-475 stay out, that work is separate. From the next gate on, tickets filed while the gate is running get a row too, including the ones you file yourself."

Jenkins bot posts in #builds, `2025-09.json`, message `ts` → UTC:

**Android Submission #127 — Started (earlier)**
- `ts` = `1758544243.280239` → **2025-09-22 12:30:43.280239 UTC**
- msg id `2baca0a9cc8618a8bdc382ff0f833e5d`, `subtype: bot_message`, `attachments[0].fallback` =
  `Match3D Android Submission - #127 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match3D%20Android%20Submission/127/display/redirect|Open>)`
- Its Success post: `ts 1758544783.817259` → 2025-09-22 12:39:43Z, `Match3D Android Submission - #127 - main  Success after 9 min 12 sec`, changes "Fix pear and orange juice [Arthur Blake]".

**iOS Submission #40 — Started (later by 97 s)**
- `ts` = `1758544340.770929` → **2025-09-22 12:32:20.770929 UTC**
- msg id `ed20f21250e1a53c5e74ea54a29ae427`, `user: SLACK_BOT_0005_SLACK_ID`, `attachments[0].fallback` =
  `Match 3D iOS Submission - #40 Started by user Arthur Blake (<http://blake.tplinkdns.com:9009/job/Match%203D%20iOS%20Submission/40/display/redirect|Open>)`
- Its Success post: `ts 1758544698.778509` → 2025-09-22 12:38:18Z, `Match 3D iOS Submission - #40 - main Success after 7 min 40 sec`, changes "Fix pear and orange juice".

**Which is earlier: Android #127 at 12:30:43Z.** The brief's 12:30:43Z is confirmed exactly. I used `completed_at > 2025-09-22T12:30:43Z` as the cut test; the 97-second gap to the iOS Started line is immaterial — **zero** in-scope Done issues fall strictly inside `(12:30:43Z, 12:32:20Z)`, so either reading yields the same set. (Note the deploy is `Match3D …`/`Match 3D …` — two spellings, same Jenkins job pair.)

## 1. ZOM population by state (base + overlay)

Field names that carry the scope-relevant facts (base JSON record schema; the overlay's SQL columns `labels_json` / `links_json` / `relations_json` / `state_history_json` land in the same record as `labels` / `links` / `relations`):

| Fact | Field | Notes |
|---|---|---|
| State | **`state_id`** | Plain state name text, e.g. `"Todo"`, `"Done"`, `"In Validation"` — not an id. There is no separate `state`/`status` field. |
| Completed | **`completed_at`** | ISO-8601 UTC text with `Z`, e.g. `2025-09-22T13:53:29Z`; `null` for every non-Done issue. |
| Canceled | `canceled_at` | ISO-8601 text; non-null on all 20 Canceled ZOM issues. |
| Labels | **`labels`** (overlay column `labels_json`) | Array of strings, e.g. `["Bug","Hot Fix - Global Launch"]`; `[]` when unlabeled. |
| Team | **`team_id`** | `team_ZOM` / `team_ART` / `team_DES` / `team_ENG` / `team_EPI`; `teams[].key` gives `ZOM`/`ART`/`DES`. Also mirrored in `identifier` prefix and `number`. |
| Other | `started_at`, `created_at`, `updated_at`, `archived_at`, `is_archived`, `time_in_status_minutes`, `priority`, `relations[]` (target/type) | `updated_at` is the only field the overlay UPDATEs. |

Team ZOM, all combined: **567 issues** (base 553 + 14 overlay).

| state_id | count |
|---|---|
| Done | **429** |
| Todo | **55** |
| Backlog | **35** |
| Canceled | **20** |
| In Progress | **16** |
| Duplicate | **7** |
| In Validation | **3** |
| Regression | **2** |
| **TOTAL** | **567** |

There are no ZOM issues in `In Review`, `Team Epic`, `Bugs`. Across all teams the universe also uses `In Review` (12), `Team Epic` (4), `Bugs` (16) — all on ART/DES/ENG/EPI.

The 7 ZOM `Duplicate` rows (all excluded by the rule, all `completed_at: null`, `canceled_at` set): ZOM-55, ZOM-203, ZOM-248, ZOM-276, ZOM-298, ZOM-368, ZOM-516.

## 2. The OPEN set (112 keys)

Definition applied verbatim: `state_id ∉ {Done, Canceled, Duplicate}` **and** (`team_id = team_ZOM` **or** (`team_id ∈ {team_ART, team_DES}` **and** `"ZM"` case-sensitive substring of `title`)), **minus** `ZOM-570`, `ZOM-359`, `ZOM-475`.

Raw ZOM open = 111 → minus the 3 exclusions = **108 ZOM**. Plus **4** ART/DES ZM-titled open = **112**.

Breakdown by state (112):

| state_id | count |
|---|---|
| Todo | 57 |
| Backlog | 35 |
| In Progress | 15 |
| In Validation | 3 |
| Team Epic | 1 |
| Regression | 1 |
| **TOTAL** | **112** |

ZOM-only 108: Todo 54, Backlog 35, In Progress 15, In Validation 3, Regression 1.

ART/DES ZM-titled scan (whole team, all states):

| Key | Team | state_id | Title |
|---|---|---|---|
| ART-790 | ART | Todo | Updated ZM Marketing Screenshots |
| ART-792 | ART | **Team Epic** | ZM3D - Marketing Screenshots round 3 |
| ART-793 | ART | Todo | ZM3D - boss arena background flickers on iPhone 12 *(overlay insert, created 2025-09-29T15:00:00Z)* |
| DES-313 | DES | Todo | ZM level 214 can't be completed *(overlay insert, created 2025-09-29T15:20:00Z)* |

Only these 4 have a case-sensitive `"ZM"` in the title; all 4 are open, so 4 of 4 enter the set. `ART-792` is the only `Team Epic`-state member — it is **not** Done/Canceled/Duplicate, so the literal rule keeps it, and truth.json agrees.

Case-variant audit for ART/DES titles (asked for explicitly):
- lowercase `zm` substring: **0** matches in ART or DES titles.
- `"Zombie Match"` in ART titles: **4**, all **Done** and therefore out of scope anyway — ART-768 "Zombie Match 3D - Logo, Splash screen, UI + assets" (2025-04-15T13:19:10Z), ART-774 "Zombie Match 3D - Marketing Screenshots" (2025-04-15T13:21:51Z), ART-775 "Zombie Match 3D - Leaderboards" (2025-04-15T13:18:36Z), ART-776 "Zombie Match 3D - Profile feature" (2025-04-15T13:18:27Z). No `"Zombie Match"` titles on DES.
- `ZombieMatch`, `Zombie_Lane`: 0 matches.
- Open ART/DES issues that mention `"ZM"` in the **description** but not the title: **0**. So the title-only rule loses nothing on this population.
- For calibration: ART+DES have 46 open issues in total; the ZM-title filter cuts that to 4, so the team scan is not accidentally sweeping unrelated art/design work.

Full 108-key ZOM open list (key | state | title):

```
ZOM-16   | Backlog       | Liquid Impact
ZOM-48   | Backlog       | Reward Animations
ZOM-56   | Backlog       | Glued VFX
ZOM-62   | Todo          | Zombie Ops #3 Spec (Dead Eye)
ZOM-64   | Backlog       | Experiment with VFX when matching boss busters off the board
ZOM-65   | Backlog       | Profile page endpoints
ZOM-66   | Backlog       | Stats endpoints
ZOM-69   | Backlog       | Bot system
ZOM-70   | Backlog       | Rewards system
ZOM-73   | Backlog       | A/B Test Item Sizes
ZOM-76   | Backlog       | [PERSON_NAME_0120] to implement this VFX
ZOM-78   | Backlog       | Event Calendar For Zombie Match 3D
ZOM-97   | Todo          | REVISION FOR ITEMS
ZOM-104  | Backlog       | Gas Can improvement
ZOM-118  | Todo          | Shop Animations Master Ticket
ZOM-119  | Backlog       | Shine for gold and gem piles.
ZOM-121  | Backlog       | Card pack animation in the shop
ZOM-122  | Backlog       | Simple animations for offers bands and labels.
ZOM-130  | Todo          | Create an out of moves screen flow with offers
ZOM-137  | Backlog       | FOOD ITEMS
ZOM-147  | Backlog       | Peach
ZOM-148  | Backlog       | Plum
ZOM-150  | Backlog       | Cherries
ZOM-151  | Backlog       | Cucumbers
ZOM-155  | Backlog       | Squash
ZOM-168  | Backlog       | 5th In-game Boost Double Damage
ZOM-171  | Todo          | Icon for double damage in-game boost
ZOM-181  | Todo          | 8. Vaious Solid color Plates/cups/mugs/egg on plates
ZOM-182  | Todo          | 9. Bagel
ZOM-184  | Todo          | 11.Curling Iron (Maybe Drop the item)
ZOM-202  | In Progress   | Minimize or migrate selection panel for easier difficulty tab comparison
ZOM-236  | Backlog       | Shop Pack Idle animation
ZOM-237  | Backlog       | packs animations bugs
ZOM-243  | Backlog       | Poison/Fire/Shock Death Vfx Animations
ZOM-255  | Backlog       | Tap to skip kill cam + Dimming the board area and only keeping the top portion lit.
ZOM-292  | Todo          | Level Editor Improvements 2.0
ZOM-293  | Todo          | Dynamic Difficulty Tiering Down Issue
ZOM-311  | In Progress   | Consider migrating the list of items and list of monsters to be added to a third display. Freeing up the entire primary display for list of items and list of monsters when editing the monster or item tabs.
ZOM-317  | Backlog       | Martin to polish UI assets in FIGMA
ZOM-342  | Todo          | Indoor Plant
ZOM-344  | Todo          | Quest UI box animation
ZOM-348  | Todo          | Rotating Shop Discount Issues
ZOM-386  | Todo          | Track Player Card Inventory and Sync to BigQuery
ZOM-387  | Todo          | Giant Analytics Ticket
ZOM-390  | Backlog       | Icon and Event Visual for Win Streak Event (axe arena)
ZOM-400  | Todo          | We want to add a new field to left_level event to track what unique items they bring to the battl...
ZOM-427  | Todo          | App icon is too zoomed in for android
ZOM-429  | Backlog       | Leaderboard next session doesn't start without killing the app
ZOM-432  | Todo          | Daily gift artwork needs to have the frame
ZOM-438  | Todo          | Investigate why some zombie tracks do not spawn
ZOM-439  | Todo          | Investigate card_upgrade event not recording correctly
ZOM-441  | Todo          | Fix reward_str and chest_content_str sending issue
ZOM-442  | In Validation | Analytics Instrumentation for Tropy Reward Redeem
ZOM-443  | Todo          | Investigate non-random item removal from board due to win streak
ZOM-449  | Backlog       | Some items are acting weird in low-end android device
ZOM-453  | Todo          | Fix text inconsistency
ZOM-458  | Todo          | Quitting algo levels still makes the level change animation
ZOM-465  | In Progress   | Endless Mode Master VFX Ticket
ZOM-467  | In Progress   | Zombie Match 3d - Marketing Videos
ZOM-468  | Todo          | Low-end devices rendering issues
ZOM-471  | Todo          | Add red dot icon for players not in Plague Race
ZOM-477  | Todo          | DOT kills can take too long and cause perceived unresponsivenes
ZOM-481  | Todo          | Zombie Health bar persists too long after death.
ZOM-482  | Backlog       | Make "Fast-forwarding" another boolean properties in zombies
ZOM-483  | Todo          | Infinite lives from new-install are not granted, rewards 30 min in the next session start.
ZOM-484  | Todo          | Info Screen Animations
ZOM-504  | Backlog       | In endless mode, objects might stay persistent in the deck after match
ZOM-505  | Backlog       | Tutorial repeats at level 19 in V 1736 Android version
ZOM-508  | Todo          | Assisted Start
ZOM-513  | In Progress   | Convert Maracas into multi-color variant-enabled
ZOM-514  | In Progress   | Request to add motorcycle helmet as a survival item
ZOM-517  | Backlog       | Monster loses enrage during item refill in endless mode
ZOM-520  | Todo          | First loss as level doesn't reset win streak
ZOM-521  | In Progress   | Master Ticket - VFX implementation
ZOM-526  | In Progress   | Tokens traveling to live-ops
ZOM-528  | In Progress   | Claimed Cards traveling to inventory section
ZOM-534  | In Progress   | Quest points not resetting until app restart in production
ZOM-535  | Todo          | Fast matching might target an already-dead zombie
ZOM-539  | Todo          | Implement Red Dot for Cards and Shop
ZOM-541  | In Progress   | Cards Collect Vfx animation
ZOM-542  | Regression    | Update home screen and victory score screen for game modes
ZOM-543  | In Progress   | Queue Manager
ZOM-544  | In Progress   | Implement Google Apple Login
ZOM-545  | Todo          | Ingest bot params from a spreadsheet
ZOM-546  | Todo          | Bug: refill algorithm spawns fewer items over time
ZOM-548  | In Validation | Track events for boss arena as listed in the spreadsheet
ZOM-549  | In Validation | Add new fields to left_level and endless_left analytics events
ZOM-552  | In Progress   | Season Pass Analytics
ZOM-554  | Todo          | Quiting level mid tornado boost breaks the object physics
ZOM-556  | Todo          | When the daily gift is skipped, it doesn't reset to 0.
ZOM-559  | Todo          | Homing out on android(samsung), sound disappears.
ZOM-560  | Todo          | The abandoned pack win streak freezer reward is not granted.
ZOM-562  | Todo          | Orphan items in boss arena
ZOM-563  | In Progress   | Teams' lives, golden frames and names not working on prod env
ZOM-564  | Todo          | "Free" label stays on boosters after Tutorial
ZOM-565  | Todo          | Endless Horde Start Screen Vfx
ZOM-566  | Todo          | Collect&Win Analytics
ZOM-568  | Todo          | Settings language list jumps back to the top while scrolling
ZOM-571  | Todo          | Gem pack price shows $0.00 for a second when the shop opens
ZOM-572  | Todo          | Win streak freezer counter shows 2 after using the last one
ZOM-573  | Todo          | Collect&Win: claiming the 5th chest crashes the app
ZOM-574  | Todo          | Zombie Lane info popup text is cut off in German
ZOM-575  | Backlog       | Add a haptics toggle to settings
ZOM-576  | Todo          | Season Pass premium tier claim drops the booster bundle
ZOM-577  | Todo          | level_fail event is missing the booster_used param
ZOM-578  | Todo          | Tutorial stuck at step 3 on a fresh install
ZOM-579  | Todo          | Boss arena hit VFX plays behind the board on iPad
ZOM-580  | Todo          | Daily gift popup shows twice after the midnight reset
```

Plus ART-790 (Todo), ART-792 (Team Epic), ART-793 (Todo), DES-313 (Todo) → 112.

*Three titles are truncated in the export itself and keep their literal trailing `...`: ZOM-400 (`…to the battl...`), ZOM-434 (`…scene is loading yo...`), ZOM-506 (`…top righ...`).*

## 3. The DONE-AFTER-CUT set (20 keys)

Filter: `state_id = "Done"` **and** (`team_ZOM` **or** ART/DES with `"ZM"` in title) **and** `completed_at > 2025-09-22T12:30:43Z`. In-scope Done of all time = 429, of which 20 qualify. Every in-scope Done row has a non-null `completed_at`.

| Key | completed_at (exact text) | Title | Note |
|---|---|---|---|
| ZOM-435 | `2025-09-22T13:53:29Z` | User stuck on trophy path after clicking claim button too fast | **earliest** after cut |
| ZOM-434 | `2025-09-22T13:53:48Z` | I can actually replicate this. If you put the app in the background while the scene is loading yo... | |
| ZOM-507 | `2025-09-22T15:09:14Z` | Create an extra camera to display effect videos | |
| ZOM-169 | `2025-09-22T15:09:46Z` | Upgrade FTUE dialogue to support image | |
| ZOM-503 | `2025-09-22T15:11:03Z` | Giving lives in teams are unresponsive | |
| ZOM-473 | `2025-09-22T15:11:51Z` | Endless mode ending screen can be skipped after death | |
| ZOM-419 | `2025-09-22T15:12:31Z` | Daily rewards missing VFX | |
| ZOM-239 | `2025-09-22T15:13:14Z` | Infinite Lifes Animation Implementation | |
| ZOM-506 | `2025-09-22T15:14:05Z` | V 1736 (Android) - Two strings are overlapping in the Zombie Lane button at ho... | |
| ZOM-538 | `2025-09-23T14:16:15Z` | Browse VFX library for bread and confetti options | |
| ZOM-112 | `2025-09-23T14:17:19Z` | Infinite Lives animation (currently inactive) | |
| ZOM-558 | `2025-09-23T14:49:24Z` | Weekly star count has wrong image | |
| ZOM-536 | `2025-09-30T12:40:23Z` | Trampoline icon is not consistent and model should be updated. | |
| ZOM-498 | `2025-09-30T12:40:29Z` | Fixing UI Elements on Home screen | |
| ZOM-555 | `2025-09-30T12:40:38Z` | Zombie Lane Reward Animations | |
| ZOM-553 | `2025-09-30T12:40:42Z` | Make changes to boss arena refill and nuke spawn behavior | |
| ZOM-557 | `2025-09-30T12:41:01Z` | Consecutive log in quest doesn't work | |
| ZOM-561 | `2025-09-30T12:43:28Z` | On low-end devices, items surfaces vertical to camera is black. | |
| ZOM-569 | `2025-09-30T18:05:00Z` | Season Pass opens twice from the join popup and leaves an empty screen | overlay insert |
| ZOM-567 | `2025-09-30T19:00:00Z` | Zombie Lane chests claimed on prod don't land in the inventory | overlay insert |

Boundary checks:
- **Done between `2025-09-22T00:00:00Z` and the cut: 0 issues.** There is a clean 25-hour gap — no ticket lands on the cut boundary to adjudicate.
- Done strictly between the Android Started (12:30:43Z) and iOS Started (12:32:20Z): **0**.
- Earliest in-scope Done overall (all time): **ZOM-10 "Get everyone into linear for ZM3D", `2025-04-21T16:20:03Z`**.
- Earliest in the done-after-cut set: **ZOM-435 `2025-09-22T13:53:29Z`** (1 h 22 min 46 s after the cut).
- No ART/DES ZM-titled issue is Done at all (all four are open), so the done-after-cut set is 100% ZOM.

## 4. Diff vs truth.json (132 keys)

| Comparison | Result |
|---|---|
| computed = open (112) ∪ done-after-cut (20) | **132** |
| truth.json keys | **132** |
| **Missing** (in truth, not computed) | **none** |
| **Extra** (computed, not in truth) | **none** |
| open ∩ done-after-cut | ∅ |

The two constructions agree **exactly, key for key** — no explanation needed for any key. Corroborating facts:
- The 4 non-ZOM truth keys are exactly the ZM-titled ART/DES open issues: ART-790 (Todo), ART-792 (Team Epic), ART-793 (Todo), DES-313 (Todo).
- No truth key is Canceled or Duplicate; no truth key is Done with `completed_at ≤ 2025-09-22T12:30:43Z`.
- ZOM-570, ZOM-359, ZOM-475 appear in neither set (they are open but excluded), confirming the exclusions are load-bearing: without them the computed union would be 135.

## 5. Specific tickets

### ZOM-435 — boundary case, in scope
- `state_id`: **`Done`**
- `completed_at`: **`2025-09-22T13:53:29Z`**
- `canceled_at`: `null`; `created_at` `2025-07-25T01:59:02Z`; `updated_at` `2025-09-22T13:53:29Z`; labels `[]`
- Title: "User stuck on trophy path after clicking claim button too fast"
- Verdict: **1 h 22 min 46 s after the cut** → in the done-after-cut set, and it is the earliest such ticket. Nothing ambiguous: it is on the right side of the boundary by a wide margin.

### ZOM-473 — in scope
- `state_id`: **`Done`**
- `completed_at`: **`2025-09-22T15:11:51Z`**
- `canceled_at`: `null`; `created_at` `2025-08-14T08:24:51Z`; `updated_at` `2025-09-22T15:11:51Z`; labels `["Bug"]`
- Title: "Endless mode ending screen can be skipped after death"
- Verdict: 2 h 41 min after the cut → in scope. (It also has an overlay comment `cmt_zom473_0` referencing "#127: the endless end…", i.e. it was re-tested on the #127 build.)

### ZOM-359 — excluded
- Title: **"Phone heating up too much after playing 15 to 20 levels."**
- `state_id`: **`Regression`** (open state — it *would* be in scope by the state test)
- `completed_at`: `null`; `canceled_at`: `null`; created `2025-07-07T12:46:44Z`; labels `["Bug","Hot Fix - Global Launch"]`
- Why excluded: named explicitly in the scope rule — "Release tickets, ZOM-359 and ZOM-475 stay out, that work is separate." Not a state-based exclusion.

### ZOM-475 — excluded
- Title: **"Consecutive glass impact sfx/vfx causes crash on android"**
- `state_id`: **`Todo`** (open state — *would* be in scope by the state test)
- `completed_at`: `null`; `canceled_at`: `null`; created `2025-08-14T08:56:20Z`; labels `["Bug"]`
- Why excluded: named explicitly in the scope rule, same sentence as ZOM-359. Not a state-based exclusion.

Both exclusions are therefore **rule-driven, not data-driven** — an agent that only applies the state rule will wrongly emit 135 keys.

### ZOM-424 — the "existing ticket?" candidate
- `state_id`: **`Done`**
- `completed_at`: **`2025-07-23T11:23:10Z`** (created `2025-07-21T15:37:24Z`) — 61 days **before** the cut, so it is **not** in the done-after-cut set and contributes no key.
- Title: **"Updating the game from earlier build breaks the core game."**
- labels: `["Bug"]`
- Description, first 300 characters (verbatim):

```
If I have more than 1 items equipped, after updating the game to the latest version, the core game breaks.

* objects are not matcheble
* Zombies don’t move
* The bottom boosts aren’t visible
* And the items I had is vanished.

This is primarily because of the object id changes. We should find a way
```

- Full description continues: "…to update the game without causing any item loss on players' end." plus two screen recordings, then: "When I made it after level 90, where all slots are unlocked, the game doesn't break but I lost the already acquired items."
- **Verdict: adjacent, NOT the same bug.** ZOM-424 is about an in-place update breaking the board because of **object-id changes** — symptoms are un-matchable objects, frozen zombies, missing bottom boosts, and loss of equipped/inventory items; the reporter is past **level 90** and stays there, never "back to level 1". It never mentions save/cloud state, currency amounts (no "500 coins"), iOS, App Store vs TestFlight, or N-1/N-2. It is Done and closed 2025-07-23. It does not describe "updating from the N-1 App Store build to iOS Submission #50 resets the save to level 1 with 500 coins."
- Practical consequence for the task: ZOM-424 is a plausible **decoy** for the reuse rule ("any existing ticket if there is one"), not the matching ticket. Treating it as the duplicate would be wrong on symptom, platform, currency and state.

## 6. Duplicate search — update-from-store / save reset / N-1

**Population searched: all 3703 Linear issues (3687 base + 16 overlay), every team (ZOM, ART, DES, ENG, EPI), every state (Done 3060 / Canceled 372 / Todo 125 / Backlog 76 / In Progress 22 / Bugs 16 / In Review 12 / Duplicate 9 / Team Epic 4 / Regression 4 / In Validation 3).** Fields searched: `title` + `description` (full text, no truncation). Comments were **not** a searchable field because base `linear.comments` is empty and the overlay only adds `cmt_*` rows keyed to known issues — those were read separately (see 6c).

Terms actually run (regex, case-insensitive unless noted): `\bsav(e|es|ed|ing)\b`, `progress`, `reset`, `\bN-1\b`, `level\s*1\b`, `500\s*coins?`, `coins?`, `store\s*build`, `updat(e|ing)\s+(the\s+)?(game\s+)?from`, `app\s*store`, `restor`, `wipe`, `\blost\b`. A row was a candidate if it had {save|progress} × {reset|lost}, or update-from × {save|progress}, or `500 coins`, or level-1 × reset, or `N-1`.

Raw term frequencies in the population (issues with ≥1 hit in title+description):

| term | issues |
|---|---|
| `save` (save/saves/saved/saving) | 67 |
| `progress` | 131 |
| `reset` | 74 |
| `level 1` | 67 |
| `coin(s)` | 179 |
| `lost` | 33 |
| `app store` / `appstore` | 12 |
| `500 coins` (literal) | 4 (10 issues have `500` and `coin` anywhere) |
| `restore` | 4 |
| `wipe` | 3 |
| `update from` | 2 |
| `N-1` | **0** |
| `store build` | **0** |

Title containing `updat|upgrad`: **173**.

### 6a. Candidates (closest first)

| Key | state | created_at | Why it surfaced | Same bug? |
|---|---|---|---|---|
| **ZOM-424** | Done | 2025-07-21T15:37:24Z | *only* ZOM ticket whose title is an update-from-earlier-build regression; description says "items I had is vanished" | **No** — object-id breakage; no save reset, no level 1, no coins, no iOS |
| ZOM-544 | In Progress | 2025-09-15T15:28:14Z | "Implement Google Apple Login" — wants to store levels/currencies server-side; mentions "update from" | No — feature work for cloud save, not a regression report |
| ZOM-483 | Todo | 2025-08-14T18:57:28Z | infinite lives duration resets to 30 min on the second session after a new install | No — timer reset on a new install, not an N-1 store update resetting save |
| ENG-2009 | Done | 2024-12-15T23:35:25Z | contains both "level 1" and "500 coins" — economy values table | No — a balance/adjustment doc for a different title; no save reset |
| ENG-2284 | Done | 2025-04-16T12:12:28Z | "free 500 coins" shop copy | No — copy/localization list |
| ENG-2276 | Done | 2025-04-11T15:41:48Z | "1 free 500 coin refresh" infinitely claimable on android | No — exploit, different title |
| ENG-1576 | Done | 2024-09-29T18:21:16Z | "Currency Balance reset to 0 with every scene update or restarting the app" | **Closest symptom match but wrong product** — ENG team, 2024, balance→0, not level 1 / 500 coins, not an N-1 store update |
| ENG-2114 | Bugs | 2025-01-27T16:27:05Z | "Quest Chest Progression Reset to 0 after reinstall with signed-in account" | No — quest chest, reinstall, different title |
| ENG-2280 | Bugs | 2025-04-15T15:40:20Z | "Sign in Issues for loading a prior data" | No — sign-in load path |
| ENG-1617 | Done | 2024-10-02T15:12:51Z | "The level progression is lost without stable internet connection" | No — offline, different title |
| ENG-1570 | Done | 2024-09-29T17:47:29Z | "The character's unlock state is lost after killing the app" | No — unlock state, app kill |
| ENG-2248 | Done | 2025-03-31T14:05:14Z | "Sophie's Favor is reset after killing the app in saga map" | No — event progress, app kill |
| ENG-1857 | Done | 2024-11-07T16:53:48Z | "On android, single quest progression is reset with every new session" | No — quest progression per session |
| ENG-2315 | Done | 2024-04-28T17:49:27Z | "Changing language resets quest chest progression to 0" | No — language toggle |
| ENG-2313 | Done | 2025-04-28T17:41:12Z | "Retry Prelevel Dialogue Error" | No |
| ENG-2109 | Backlog | 2025-01-24T15:25:59Z | "Quest Inıt Issue Persist on some users" | No |
| ENG-2073 / ENG-2227 / ENG-2363 / ENG-478 / ENG-615 / ENG-771 / ENG-213 / ENG-1081 / ENG-272 / ENG-1267 / ENG-1640 / ENG-1750 / ENG-1888 / ENG-1977 / ENG-2091 / ENG-2113 / ENG-2153 / ENG-2312 / ENG-1373 / ENG-1661 / ENG-1839 / ENG-2056 / ENG-1107 / ENG-1058 / ENG-1061 / ENG-1095 / ENG-1116 / ENG-1131 / ENG-1268 / ENG-1477 / ENG-1498 / ENG-1551 / ENG-1593 / ENG-1611 / ENG-1614 / ENG-1656 / ENG-1727 / ENG-1961 / ENG-2009 / ENG-2042 / ENG-877 / ZOM-365 / ZOM-40 | mixed | various | hit on one or two generic terms only (reset / coins / level 1) | No — coin-cost tables, quest-reset-by-date, offline progress, tutorial replay, etc. |

Full candidate list from the initial pass was 54 rows; every one outside the table above matched on a single generic term (`reset`, `coins`, `progress`) with no update-from-store context.

### 6b. Absence checks (scope-bounded)
- `N-1` as a literal token: **0 of 3703** issues. The only place "N-1" exists in this universe's Linear data is the **overlay's GSheet** QA matrix row (`Update from N-1` column, `01_Universe_Inject.sql` line ~261/269) — not a Linear issue.
- `500 coins` + `level 1` in the same issue: **0**. The 4 issues with the literal phrase "500 coins" are all economy/copy tickets — ENG-1961 ("up to 2500 coins" ad copy), ENG-2009 (economy value table: 150→500 coins for Infinite Rewind), ENG-2276 (free 500-coin shop refresh exploit on Android), ENG-2284 (shop copy checklist). None mentions a save, a level reset, or an update.
- Tickets that mention an **App Store / TestFlight / store-build install over an older build**: **0**. `store build` literal = 0 hits. `TestFlight` appears in 13 ENG tickets, all build/QA-pipeline chores for a different title. The 12 `app store`/`appstore` hits are marketing metadata (ART-307 "ART:MARKETING>APP STORE ICON", ART-631, ART-722 "Appstore Description Localization", ART-724, ART-726, ART-774 screenshots), bundle/package plumbing (ENG-1212, ENG-1464, ZOM-226 "Create Bundle Ids in the Appstore"), a store-submission chore (ENG-2366 for DD), a rating prompt (ENG-633), and one gem exploit (ENG-2296). None is about installing a store build over an older one.
- Therefore: **no pre-existing Linear ticket describes "updating from the N-1 App Store build to iOS Submission #50 resets the save to level 1 with 500 coins."** The claim in the QA matrix row (iOS 18.6, N-1 → iOS Submission #50, FAIL, save back at level 1 with 500 coins vs level 212 / 18,400 coins, relaunch did not recover) is **new** — it has no Linear home in the base export.

### 6c. Reuse-rule context read from the overlay (not a duplicate, but it governs the decision)
- ZOM-570 description: "store push: anything that blocks goes on ZOM-570 under the ticket that already exists, no duplicate tickets. only open a new one if nobody filed it yet".
- Overlay header comment line 15: "Blockers go on this ticket by key, the existing ticket if there is one (I'm putting the reuse rule on the tech-issues card). I'll post the candidates in #zombie-bugs."
- Overlay comment `cmt_zom570_1` (2025-09-30T20:52:00Z): "sign-off as a reply on Arthur's candidate thread in #zombie-bugs please, not a new post, so it stays on the candidate post".
- Implication: the "existing ticket" the rules point at is a **candidate to be judged**, and the only Linear row that can plausibly be offered is ZOM-424 — which fails the symptom test (see §5). So the correct outcome is a **new** bug ticket for the iOS N-1 save reset; ZOM-424 must not be cited as the covering ticket.

## 7. Summary

**Counts**
- ZOM population (base + overlay): **567** total — Done 429, Todo 55, Backlog 35, Canceled 20, In Progress 16, Duplicate 7, In Validation 3, Regression 2.
- **Open N = 112** (108 ZOM + ART-790, ART-792, ART-793, DES-313). Raw ZOM open was 111; the 3 named exclusions bring ZOM to 108.
- **Done-after-cut N = 20** (all ZOM), earliest ZOM-435 `2025-09-22T13:53:29Z`; **0** in-scope Done between 2025-09-22T00:00Z and the cut; **0** inside the 97-second Android→iOS gap.
- **Total N = 132.**

**Diff vs truth.json**: 132 vs 132 — **zero missing, zero extra, exact key-for-key match.** The scope rule as written reproduces the solver's expected population with no adjudication needed.

**Cut instant**: Android Submission #127 Started `ts 1758544243.280239` = **2025-09-22T12:30:43Z** (earlier); iOS Submission #40 Started `ts 1758544340.770929` = 2025-09-22T12:32:20Z. The documented 12:30:43Z is the Android post and is exact.

**ZOM-424 / duplicate verdict**: ZOM-424 "Updating the game from earlier build breaks the core game." is `Done` at `2025-07-23T11:23:10Z` — outside the done-after-cut set and outside the open set, so it is not a scope key. It describes an object-id-change breakage on update (un-matchable objects, frozen zombies, missing boosts, lost equipped items, reporter past level 90), **not** a save reset to level 1 with 500 coins on an N-1 App Store → iOS Submission #50 update. **It is not the duplicate.** A 3703-issue title+description search for `N-1`, `save`, `progress`, `reset`, `level 1`, `500 coins`, `store build`, `update from`, `app store`, `restore`, `wipe`, `lost` finds **no** existing Linear ticket for the iOS N-1 save-reset claim — so the finding has no existing ticket to be filed under and (per the reuse rule) warrants a **new** ticket on ZOM-570.
