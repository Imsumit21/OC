# Cohort Plan — Vincent Parker, ZM Store-Submission QA Gate (Oct 1, 2025)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Persona: Vincent Parker, QA / Game Systems Engineer.

## Scope

Gate for the Zombie Match 3D (Linear team ZOM) store-submission builds cut Sep 30:

- Android Submission **#135** — job start 2025-09-30T18:45:34Z, succeeded 20:13:09Z (`#builds` C05433XK267/1759263189.219529).
- iOS Submission **#50** — job start 2025-09-30T18:43:32Z, succeeded 19:15:49Z (`#builds` C05433XK267/1759259749.259909).
- Previous gate: Android **#127** / iOS **#40**, job start ~2025-09-22T12:30Z, finished 12:39:43Z (`#builds` C05433XK267/1758544783.817259).
- Inclusion rule: anything merged/committed to `main` before **2025-09-30T18:43:32Z** is in the candidate builds.
- Scope (a): every open ZOM ticket in Todo / Backlog / In Progress / In Validation / Regression, plus ZM tickets in other teams → **101 items** (99 ZOM + ART-790 + ART-792).
- Scope (b): every ZOM ticket moved to Done after 2025-09-22T12:30Z → **18 tickets**.
- Calls: BLOCKER (crash, freeze, stuck/unable to finish a level, lost progress/currency/items, broken purchase), KNOWN ISSUE (any other player-hit bug), NO CALL (art, VFX, analytics, tooling, backend, feature work), PERF-EXCLUDED (ZOM-359, ZOM-475).

## Method

Open-ticket text, labels, state and parent came from the Linear ZOM extract (553 issues, 99 open). Each Bug-labelled ticket and each unlabelled-but-player-facing ticket was cross-checked against Sep 2025 Slack (#builds C05433XK267, #zombie-bugs C08R27X0EAH, #zombie-match3d C0880U9751A, the PR/commit feed C093LEZGF6J and the Vincent DMs D079SNE2TL4 / D07GK9QQG7M / D07GJJBFHA5 / D07GMT8NVM2) by ticket key and by distinctive title words. Done-since-gate tickets were matched to a match3d PR branch/title/body, a commit subject from the PR feed, or a `#builds` change-list line; Linear base data contains 0 comments, so no ticket already carries a QA note.

Confidence `clear` = the ticket text/label decides the call; `ambiguous` = text alone cannot separate BLOCKER from KNOWN ISSUE (or NO CALL), and a seeded QA comment is required to settle it. All 15 ambiguous tickets have a proposed observation on a named build, dated Sep 24–30 2025, written as a raw observation (never the verdict word).

## Open Tickets (101)

| id | state | labels | title | call | conf |
|---|---|---|---|---|---|
| ZOM-16 | Backlog | VFX, Improvement | Liquid Impact | **NO CALL** | clear |
| ZOM-48 | Backlog | (ZM) Game Design, VFX, Core Game | Reward Animations | **NO CALL** | clear |
| ZOM-56 | Backlog | VFX | Glued VFX | **NO CALL** | clear |
| ZOM-62 | Todo | (ZM) Game Design, 30 June | Zombie Ops #3 Spec (Dead Eye) | **NO CALL** | clear |
| ZOM-64 | Backlog | VFX | Experiment with VFX when matching boss busters off the board | **NO CALL** | clear |
| ZOM-65 | Backlog | server-api | Profile page endpoints | **NO CALL** | clear |
| ZOM-66 | Backlog | server-api | Stats endpoints | **NO CALL** | clear |
| ZOM-69 | Backlog | server-api | Bot system | **NO CALL** | clear |
| ZOM-70 | Backlog | server-api | Rewards system | **NO CALL** | clear |
| ZOM-73 | Backlog | (ZM) Game Design | A/B Test Item Sizes | **NO CALL** | clear |
| ZOM-76 | Backlog | Engineering, VFX | [PERSON_NAME_0120] to implement this VFX | **NO CALL** | clear |
| ZOM-78 | Backlog | Backend Engineering | Event Calendar For Zombie Match 3D | **NO CALL** | clear |
| ZOM-97 | Todo | 3D Art, Improvement | REVISION FOR ITEMS | **NO CALL** | clear |
| ZOM-104 | Backlog | 3D Art, Improvement | Gas Can improvement | **NO CALL** | clear |
| ZOM-118 | Todo | VFX | Shop Animations Master Ticket | **NO CALL** | clear |
| ZOM-119 | Backlog | VFX | Shine for gold and gem piles. | **NO CALL** | clear |
| ZOM-121 | Backlog | VFX | Card pack animation in the shop | **NO CALL** | clear |
| ZOM-122 | Backlog | VFX | Simple animations for offers bands and labels. | **NO CALL** | clear |
| ZOM-130 | Todo | — | Create an out of moves screen flow with offers | **NO CALL** | clear |
| ZOM-137 | Backlog | 3D Art | FOOD ITEMS | **NO CALL** | clear |
| ZOM-147 | Backlog | — | Peach | **NO CALL** | clear |
| ZOM-148 | Backlog | — | Plum | **NO CALL** | clear |
| ZOM-150 | Backlog | — | Cherries | **NO CALL** | clear |
| ZOM-151 | Backlog | — | Cucumbers | **NO CALL** | clear |
| ZOM-155 | Backlog | — | Squash | **NO CALL** | clear |
| ZOM-168 | Backlog | Core Game | 5th In-game Boost Double Damage | **NO CALL** | clear |
| ZOM-171 | Todo | UI | Icon for double damage in-game boost | **NO CALL** | clear |
| ZOM-181 | Todo | — | 8. Vaious Solid color Plates/cups/mugs/egg on plates | **NO CALL** | clear |
| ZOM-182 | Todo | — | 9. Bagel | **NO CALL** | clear |
| ZOM-184 | Todo | — | 11.Curling Iron (Maybe Drop the item) | **NO CALL** | clear |
| ZOM-202 | In Progress | Improvement | Minimize or migrate selection panel for easier difficulty tab comparis | **NO CALL** | clear |
| ZOM-236 | Backlog | VFX Integration, VFX, Improvement | Shop Pack Idle animation | **NO CALL** | clear |
| ZOM-237 | Backlog | VFX, Bug, SFX | packs animations bugs | **KNOWN ISSUE** | ambiguous |
| ZOM-243 | Backlog | VFX | Poison/Fire/Shock Death Vfx Animations | **NO CALL** | clear |
| ZOM-255 | Backlog | Feature | Tap to skip kill cam + Dimming the board area and only keeping the top | **NO CALL** | clear |
| ZOM-292 | Todo | Level Editor, Improvement, 30 June | Level Editor Improvements 2.0 | **NO CALL** | clear |
| ZOM-293 | Todo | 30 June | Dynamic Difficulty Tiering Down Issue | **NO CALL** | clear |
| ZOM-311 | In Progress | — | Consider migrating the list of items and list of monsters to be added to a third display. Freeing up the entire primary display for list of items and list of monsters when editing the monster or item tabs. | **NO CALL** | clear |
| ZOM-317 | Backlog | Improvement | Martin to polish UI assets in FIGMA | **NO CALL** | clear |
| ZOM-342 | Todo | — | Indoor Plant | **NO CALL** | clear |
| ZOM-344 | Todo | VFX, Improvement, Hot Fix - Global Launch | Quest UI box animation | **NO CALL** | clear |
| ZOM-348 | Todo | 15 July, Bug | Rotating Shop Discount Issues | **KNOWN ISSUE** | ambiguous |
| ZOM-386 | Todo | Inventory, Data | Track Player Card Inventory and Sync to BigQuery | **NO CALL** | clear |
| ZOM-387 | Todo | Inventory, Analytics | Giant Analytics Ticket | **NO CALL** | clear |
| ZOM-390 | Backlog | — | Icon and Event Visual for Win Streak Event (axe arena) | **NO CALL** | clear |
| ZOM-400 | Todo | — | We want to add a new field to left_level event to track what unique items they bring to the battl... | **NO CALL** | clear |
| ZOM-427 | Todo | — | App icon is too zoomed in for android | **KNOWN ISSUE** | clear |
| ZOM-429 | Backlog | Bug | Leaderboard next session doesn't start without killing the app | **KNOWN ISSUE** | clear |
| ZOM-432 | Todo | Improvement | Daily gift artwork needs to have the frame | **NO CALL** | clear |
| ZOM-438 | Todo | Bug | Investigate why some zombie tracks do not spawn | **KNOWN ISSUE** | ambiguous |
| ZOM-439 | Todo | — | Investigate card_upgrade event not recording correctly | **NO CALL** | clear |
| ZOM-441 | Todo | — | Fix reward_str and chest_content_str sending issue | **NO CALL** | clear |
| ZOM-442 | In Validation | — | Analytics Instrumentation for Tropy Reward Redeem | **NO CALL** | clear |
| ZOM-443 | Todo | Bug | Investigate non-random item removal from board due to win streak | **KNOWN ISSUE** | ambiguous |
| ZOM-449 | Backlog | — | Some items are acting weird in low-end android device | **BLOCKER** | ambiguous |
| ZOM-453 | Todo | — | Fix text inconsistency | **KNOWN ISSUE** | clear |
| ZOM-458 | Todo | Bug | Quitting algo levels still makes the level change animation | **KNOWN ISSUE** | clear |
| ZOM-465 | In Progress | VFX | Endless Mode Master VFX Ticket | **NO CALL** | clear |
| ZOM-467 | In Progress | Marketing | Zombie Match 3d - Marketing Videos | **NO CALL** | clear |
| ZOM-468 | Todo | Bug | Low-end devices rendering issues | **KNOWN ISSUE** | ambiguous |
| ZOM-471 | Todo | Improvement, Hot Fix - Global Launch | Add red dot icon for players not in Plague Race | **NO CALL** | clear |
| ZOM-477 | Todo | Improvement | DOT kills can take too long and cause perceived unresponsivenes | **NO CALL** | clear |
| ZOM-481 | Todo | Bug | Zombie Health bar persists too long after death. | **KNOWN ISSUE** | ambiguous |
| ZOM-482 | Backlog | Improvement | Make "Fast-forwarding" another boolean properties in zombies | **NO CALL** | clear |
| ZOM-483 | Todo | Bug | Infinite lives from new-install are not granted, rewards 30 min in the next session start. | **KNOWN ISSUE** | ambiguous |
| ZOM-484 | Todo | — | Info Screen Animations | **NO CALL** | clear |
| ZOM-504 | Backlog | Bug | In endless mode, objects might stay persistent in the deck after match | **KNOWN ISSUE** | ambiguous |
| ZOM-505 | Backlog | — | Tutorial repeats at level 19 in V 1736 Android version | **BLOCKER** | ambiguous |
| ZOM-508 | Todo | FTUE, Improvement | Assisted Start | **NO CALL** | clear |
| ZOM-513 | In Progress | 3D Art, Improvement | Convert Maracas into multi-color variant-enabled | **NO CALL** | clear |
| ZOM-514 | In Progress | 3D Art | Request to add motorcycle helmet as a survival item | **NO CALL** | clear |
| ZOM-517 | Backlog | Bug | Monster loses enrage during item refill in endless mode | **KNOWN ISSUE** | clear |
| ZOM-520 | Todo | Bug | First loss as level doesn't reset win streak | **KNOWN ISSUE** | clear |
| ZOM-521 | In Progress | VFX Integration, VFX | Master Ticket - VFX implementation | **NO CALL** | clear |
| ZOM-526 | In Progress | VFX Integration | Tokens traveling to live-ops | **NO CALL** | clear |
| ZOM-528 | In Progress | VFX Integration | Claimed Cards traveling to inventory section | **NO CALL** | clear |
| ZOM-534 | In Progress | Bug | Quest points not resetting until app restart in production | **KNOWN ISSUE** | ambiguous |
| ZOM-535 | Todo | Bug | Fast matching might target an already-dead zombie | **KNOWN ISSUE** | clear |
| ZOM-539 | Todo | Improvement, Hot Fix - Global Launch | Implement Red Dot for Cards and Shop | **NO CALL** | clear |
| ZOM-541 | In Progress | VFX Integration, VFX | Cards Collect Vfx animation | **NO CALL** | clear |
| ZOM-542 | Regression | Improvement, Hot Fix - Global Launch | Update home screen and victory score screen for game modes | **NO CALL** | clear |
| ZOM-543 | In Progress | — | Queue Manager | **NO CALL** | clear |
| ZOM-544 | In Progress | — | Implement Google Apple Login | **NO CALL** | clear |
| ZOM-545 | Todo | Improvement, Hot Fix - Global Launch | Ingest bot params from a spreadsheet | **NO CALL** | clear |
| ZOM-546 | Todo | Bug | Bug: refill algorithm spawns fewer items over time | **BLOCKER** | clear |
| ZOM-548 | In Validation | Improvement, Analytics | Track events for boss arena as listed in the spreadsheet | **NO CALL** | clear |
| ZOM-549 | In Validation | Improvement, Analytics | Add new fields to left_level and endless_left analytics events | **NO CALL** | clear |
| ZOM-552 | In Progress | Analytics | Season Pass Analytics | **NO CALL** | clear |
| ZOM-554 | Todo | Bug | Quiting level mid tornado boost breaks the object physics | **BLOCKER** | ambiguous |
| ZOM-556 | Todo | Bug | When the daily gift is skipped, it doesn't reset to 0. | **KNOWN ISSUE** | ambiguous |
| ZOM-559 | Todo | Bug | Homing out on android(samsung), sound disappears. | **BLOCKER** | ambiguous |
| ZOM-560 | Todo | Bug | The abandoned pack win streak freezer reward is not granted. | **BLOCKER** | clear |
| ZOM-562 | Todo | Bug | Orphan items in boss arena | **BLOCKER** | ambiguous |
| ZOM-563 | In Progress | Bug | Teams' lives, golden frames and names not working on prod env | **NO CALL** | clear |
| ZOM-564 | Todo | Bug | "Free" label stays on boosters after Tutorial | **NO CALL** | clear |
| ZOM-565 | Todo | VFX Integration, VFX | Endless Horde Start Screen Vfx | **NO CALL** | clear |
| ZOM-566 | Todo | — | Collect&Win Analytics | **NO CALL** | clear |
| ART-790 | Todo | — | Updated ZM Marketing Screenshots | **NO CALL** | clear |
| ART-792 | Team Epic | — | ZM3D - Marketing Screenshots round 3 | **NO CALL** | clear |
| ZOM-359 | Regression | Bug, Hot Fix - Global Launch | Phone heating up too much after playing 15 to 20 levels. | **PERF-EXCLUDED** | clear |
| ZOM-475 | Todo | Bug | Consecutive glass impact sfx/vfx causes crash on android | **PERF-EXCLUDED** | clear |

### Blockers (7)

- **ZOM-449 — Some items are acting weird in low-end android device** (ambiguous): Linear ZOM-449: no labels; low-end Android 1449: 'Level 3 tutorial is broken, it starts before loading the scene', device unresponsive afterwards, fixed only by killing the app; long artifact list (MF5 keyboard, MF11 microwaves, MF12 controller, main L14/L16 grenade) and screen flicker
- **ZOM-505 — Tutorial repeats at level 19 in V 1736 Android version** (ambiguous): Linear ZOM-505: no labels; quotes Martin Walsh 'At level 19 you can't proceed because the tutorial is repeating'
- **ZOM-546 — Bug: refill algorithm spawns fewer items over time** (clear): Linear ZOM-546: label Bug; quoted description 'the refill algorithm over time is spawning less and less item each refill. Eventually with not a lot of items on the board' - board drains until no useful match remains
- **ZOM-554 — Quiting level mid tornado boost breaks the object physics** (ambiguous): Linear ZOM-554: label Bug; 'When I quit the level while the Tornado booster is active, all the objects in the following levels float around the board as if they're drifting in space... it also affects the objects in the following levels. To fix it, I had to kill the game' (recording [[URL_52862]])
- **ZOM-559 — Homing out on android(samsung), sound disappears.** (ambiguous): Linear ZOM-559: label Bug; 'if I home out during a level, and home back in, my sound completely disappears. And if I were to finish a level, I hard freeze at end game victory screen'; reporter note 'Doesn't happen to me... might be a Samsung issue but I need to see video'
- **ZOM-560 — The abandoned pack win streak freezer reward is not granted.** (clear): Linear ZOM-560: label Bug; 'In the abandoned pack, the time boost of win streak freezer is not granted. The other rewards are given without any problem' (recording [[URL_52866]]) - a bought pack fails to deliver a paid reward
- **ZOM-562 — Orphan items in boss arena** (ambiguous): Linear ZOM-562: label Bug; after refills objects are not spawned in sets of 3, leaving orphan items; 'expected behavior is to refill objects by 3 items (1 set) not one by one' (two recordings)

### Known Issues (17)

- **ZOM-237 — packs animations bugs** (ambiguous): Linear ZOM-237: labels VFX,Bug,SFX; description reports the new banner animation plays twice per card and banner/multiplier SFX play even when the banner is absent
- **ZOM-348 — Rotating Shop Discount Issues** (ambiguous): Linear ZOM-348: label Bug; rotating-shop common packs show no discount badge and boost discounts do not match value
- **ZOM-427 — App icon is too zoomed in for android** (clear): Linear ZOM-427: no labels; description 'App icon is too zoomed in for android, I couldn't see the icon on ios yet' with before/after screenshots [[URL_52733]]/[[URL_52732]]; player- and store-facing visual defect on the submitted icon
- **ZOM-429 — Leaderboard next session doesn't start without killing the app** (clear): Linear ZOM-429: label Bug; weekly leaderboard does not roll over and rewards cannot be claimed until the app is killed and relaunched
- **ZOM-438 — Investigate why some zombie tracks do not spawn** (ambiguous): Linear ZOM-438: label Bug; level C_0120 has 17 monsters but repeated simulations spawn 11-14, 'never all 17', possibly DOTS-related; no progression loss described
- **ZOM-443 — Investigate non-random item removal from board due to win streak** (ambiguous): Linear ZOM-443: label Bug; 'Win streak level induced item removal from board is not random'
- **ZOM-453 — Fix text inconsistency** (clear): Linear ZOM-453: child of ZOM-450; 'make a list of all uppercase, lowercase text placement and standardize the infographic screens' - player-visible copy inconsistency
- **ZOM-458 — Quitting algo levels still makes the level change animation** (clear): Linear ZOM-458: label Bug; quitting an algo level without passing still plays the home-screen level-pass animation (screen recording [[URL_52765]])
- **ZOM-468 — Low-end devices rendering issues** (ambiguous): Linear ZOM-468: child of ZOM-449; label Bug; on low-end devices the boss buster item is partly invisible and objects fail to render while opening a pack (screenshots [[URL_52782]]/[[URL_52780]])
- **ZOM-481 — Zombie Health bar persists too long after death.** (ambiguous): Linear ZOM-481: label Bug; health bar lingers ~1s after death and 'might also cause mistargets' - fast matches can still target the dead zombie, wasting items
- **ZOM-483 — Infinite lives from new-install are not granted, rewards 30 min in the next session start.** (ambiguous): Linear ZOM-483: label Bug; second session resets new-install infinite lives to 30 min regardless of remaining duration (recording [[URL_52798]])
- **ZOM-504 — In endless mode, objects might stay persistent in the deck after match** (ambiguous): Linear ZOM-504: label Bug; endless-mode objects can stay visible after being thrown; 'I couldn't notice anything particularly' beyond the visual (two recordings)
- **ZOM-517 — Monster loses enrage during item refill in endless mode** (clear): Linear ZOM-517: label Bug; enraged monster on the board loses enrage when a refill happens
- **ZOM-520 — First loss as level doesn't reset win streak** (clear): Linear ZOM-520: label Bug; first loss on level 21 does not reset win streak to 0, later levels do (recording [[URL_52834]])
- **ZOM-534 — Quest points not resetting until app restart in production** (ambiguous): Linear ZOM-534: label Bug; quest points do not reset after finishing the day while online, only after killing and restarting the app; explicitly 'this is on production'
- **ZOM-535 — Fast matching might target an already-dead zombie** (clear): Linear ZOM-535: label Bug; at 120 CPM items fly at already-killed monsters, wasting items and ending with the nuke while a 75 CPM player keeps items; slow-mo recording [[URL_52841]]
- **ZOM-556 — When the daily gift is skipped, it doesn't reset to 0.** (ambiguous): Linear ZOM-556: label Bug; skipping a day does not reset the daily-gift streak to day 1 (screenshot [[URL_52863]])

### Settling observations for ambiguous tickets (15)

Each is a proposed Linear comment by Vincent Parker or Brian Foster, dated 2025-09-24..2025-09-30 (before 2025-10-01T00:00Z), naming the build observed. None of them contradicts a base record found; where base evidence already exists it is listed in the evidence column.

- **ZOM-237** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-27, tested on Android Submission #133 / iOS #49: 'Opened a 10-card pack from the shop. On the second card the red NEW banner was already visible when the card flipped and then replayed its pop-in; the banner SFX fired on the 4th and 7th cards where no banner was shown. No effect on claiming the cards.'
- **ZOM-348** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, tested on Android Submission #133 / iOS #49: 'Rotating shop: the 1000-coin common pack showed no discount ribbon, the 80-bone pack showed none either, and the catapult offer showed -25% against a 100-gem list price. Tapping buy opened the store sheet with the discounted price that was shown, so the purchase itself completed.'
- **ZOM-438** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49: 'Ran C_0120 five times. Monster count at level end was 12, 13, 11, 14, 12; the missing zombies never appeared, but the level still completed normally every run.'
- **ZOM-443** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49: 'On a win-streak bonus level the removed items came from the same three columns on four consecutive streaks (centre and right), while an off-streak level removed a mixed set. Play continued normally.'
- **ZOM-449** — call BLOCKER. Proposed Linear comment, Brian Foster, 2025-09-29, on Android Submission #133 on a low-end Android device: 'Cold start into level 3: the tutorial highlight drew over the loading screen before the board appeared and the device stopped responding to taps for about 40 seconds; force-quit and relaunch got past it. MF11 microwave and MF12 controller still render with missing surfaces.'
- **ZOM-468** — call KNOWN ISSUE. Proposed Linear comment, Brian Foster, 2025-09-29, on Android Submission #133 on a low-end Android device: 'Boss buster rendered with half its body missing; opening a 3-card pack showed two empty card slots until the pack was closed and reopened. Gameplay and claims were unaffected.'
- **ZOM-481** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49: 'At 120 CPM the health bar stayed about a second after the death animation and two matched items flew at the corpse without dealing damage. Board still cleared and the level finished.'
- **ZOM-483** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49: 'Fresh install granted the infinite-lives banner; after killing and relaunching, the banner read 30 min even though 27 min were left before the restart. No coins were charged for the lost time.'
- **ZOM-504** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49: 'In endless horde a matched item stayed drawn on its old cell for two refills before disappearing; the cell still accepted matches and no input was lost.'
- **ZOM-505** — call BLOCKER. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133: 'Failed level 19 three times on purpose. Each retry reopened the tutorial panel over the pre-level screen; after tapping through all four steps the level started and could be played and finished. Reproduced on a second install; no case where the level could not be started.'
- **ZOM-534** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49 against prod: 'Completed the daily quest and stayed in the quest panel; the points stayed at 5/5 and the chest stayed locked until the app was force-quit and reopened, when it reset. No quest rewards were lost.'
- **ZOM-554** — call BLOCKER. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133: 'Quit level 41 with the tornado booster mid-spin. On the next level the objects hung above their cells and drifted; matches did not register on the floating pieces and the level could not be played until I force-quit and relaunched. Repeated once on iOS #49, same result.'
- **ZOM-556** — call KNOWN ISSUE. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133 / iOS #49: 'Claimed day 3, then skipped a day. On the next launch the panel still highlighted day 4 instead of resetting to day 1. Claiming that day advanced the streak rather than restarting it.'
- **ZOM-559** — call BLOCKER. Proposed Linear comment, Brian Foster, 2025-09-28, on Android Submission #133 on Samsung S22: 'Home out mid-level, return, then finish the level: SFX were silent for the rest of the level and the victory screen froze with the reward panel half-drawn for about 20 seconds; force-quit and relaunch recovered the level reward.'
- **ZOM-562** — call BLOCKER. Proposed Linear comment, Vincent Parker, 2025-09-28, on Android Submission #133: 'Boss arena, after the 30s refill: two single items spawned with no matching partners and sat on the board. No pair for either appeared for the rest of the run, the board could not be cleared and the boss timer ran out with three singles still orphaned.'

### Non-Bug-labelled player-facing defects

| id | labels | why it is a defect, not art/feature |
|---|---|---|
| ZOM-427 | — | App icon is visibly zoomed/cropped on Android; this is the store-listing icon for the very build under submission (`[[URL_52733]]` vs `[[URL_52732]]`). KNOWN ISSUE. |
| ZOM-449 | — | Low-end Android: level-3 tutorial starts before the scene loads and the device stops responding; long artifact list; recoverable only by killing the app. BLOCKER (ambiguous). |
| ZOM-453 | — | Uppercase/lowercase copy is inconsistent across screens and infographic screens are not standardised — player-visible text, not new art. KNOWN ISSUE. |
| ZOM-505 | — | Level 19 tutorial repeats; the quoted report says the player cannot proceed. Base Slack partly contradicts (see warnings). BLOCKER (ambiguous). |

ZOM-468 and ZOM-458 read like unlabelled bugs but both do carry `Bug`; ZOM-237 carries `Bug` plus `VFX,SFX`.

### Done since the previous gate (18)

| id | title | fix evidence (PR / commit / #builds line) | fix time | in candidate (<18:43:32Z Sep 30) |
|---|---|---|---|---|
| ZOM-112 | Infinite Lives animation (currently inactive) | Linear ZOM-112 completed 2025-09-23T14:17:19Z <br> PR match3d#229 'Marcus/InfiniteLifes_Animation / Infinite Lifes Animation' merged 2025-06-10T16:32:32Z (asset only - the ticket says the animation is currently inactive, and no activation change was found) | 2025-06-10T16:32:32Z | **true** |
| ZOM-169 | Upgrade FTUE dialogue to support image | Linear ZOM-169 completed 2025-09-22T15:09:46Z (bulk close with ZOM-239/419/473/503/506/507) <br> No matching match3d PR or #builds change-list line found; nearest tutorial work is PR #466 merged 2025-09-26T15:14:44Z (after the close) and PR #437 ftue/effects-popup merged 2025-09-15T22:07:01Z | unknown | **unknown** |
| ZOM-239 | Infinite Lifes Animation Implementation | Linear ZOM-239 completed 2025-09-22T15:13:14Z <br> PR match3d#229 'Marcus/InfiniteLifes_Animation' merged 2025-06-10T16:32:32Z | 2025-06-10T16:32:32Z | **true** |
| ZOM-419 | Daily rewards missing VFX | Linear ZOM-419 completed 2025-09-22T15:12:31Z <br> PR match3d#408 '[PERSON_NAME_0029]/vfx implementation' merged 2025-09-11T13:15:16Z covers daily_gift reward VFX; PR #447 'vfx fixes' merged 2025-09-17T00:59:46Z adds 'Corrected boost reward...' fixes | 2025-09-11T13:15:16Z | **true** |
| ZOM-434 | I can actually replicate this. If you put the app in the background while the scene is loading yo... | Linear ZOM-434 completed 2025-09-22T13:53:48Z <br> Slack C0880U9751A/1758549228.782499 Oliver Brooks changed status to Done <br> No PR or change-list line found that names backgrounding-during-load item scatter | 2025-09-22T13:53:48Z | **unknown** |
| ZOM-435 | User stuck on trophy path after clicking claim button too fast | Linear ZOM-435 completed 2025-09-22T13:53:29Z <br> Slack C0880U9751A/1758549209.577599 Oliver Brooks changed status to Done <br> Candidate fix: PR #440/#447 reward-claim guards ('Fixing rewards not being claimed sometimes' ab89efef; input block during reward VFX) merged 2025-09-16/17 | 2025-09-17T00:59:46Z | **unknown** |
| ZOM-473 | Endless mode ending screen can be skipped after death | Linear ZOM-473 completed 2025-09-22T15:11:51Z <br> Commit c6cf8317 'Adding input blocker during Level-end animations' pushed to main 2025-09-24T23:06:27Z, shipped in PR #465 queue manager (merged 2025-09-25T22:15:51Z) <br> Note: the ticket was closed 2025-09-22, three days before this input-blocker commit landed | 2025-09-24T23:06:27Z | **true** |
| ZOM-498 | Fixing UI Elements on Home screen | Linear ZOM-498 completed 2025-09-30T12:40:29Z <br> PR match3d#471 'Samuel/ZOM-498-536' merged 2025-09-30T15:52:24Z, commit 0e5a3c9d 'Fixing UI Elements on Home screen' <br> Slack C093LEZGF6J/1759183258.562409 links #471 to ZOM-498 <br> #builds Android Submission #135 change list line 'Fixing UI Elements on Home screen [Samuel Turner]' (C05433XK267/1759263189.219529) | 2025-09-30T15:52:24Z | **true** |
| ZOM-503 | Giving lives in teams are unresponsive | Linear ZOM-503 completed 2025-09-22T15:11:03Z <br> PR match3d#422 '[PERSON_NAME_0067]/askLivesFix / Giving lives in teams fix and Popup animations' merged 2025-09-09T14:39:02Z | 2025-09-09T14:39:02Z | **true** |
| ZOM-506 | V 1736 (Android) - Two strings are overlapping in the Zombie Lane button at home screen, top righ... | Linear ZOM-506 completed 2025-09-22T15:14:05Z <br> Commit 58b73e34 'fix level text aligment on zombielane' in PR #471 merged 2025-09-30T15:52:26Z; #builds #135 line 'fix level text aligment on zombielane [Samuel Turner]' | 2025-09-30T15:52:26Z | **true** |
| ZOM-507 | Create an extra camera to display effect videos | Linear ZOM-507 completed 2025-09-22T15:09:14Z <br> No matching PR or change-list line; effects-popup camera work is PR #437 (2025-09-15T22:07:01Z) and #415 (2025-09-05T20:53:01Z) | unknown | **unknown** |
| ZOM-536 | Trampoline icon is not consistent and model should be updated. | Linear ZOM-536 completed 2025-09-30T12:40:23Z <br> Commit 294d009f 'Update trampoline icon' in PR #471 merged 2025-09-30T15:52:24Z <br> #builds #135 line 'Update trampoline icon [Samuel Turner]' | 2025-09-30T15:52:24Z | **true** |
| ZOM-538 | Browse VFX library for bread and confetti options | Linear ZOM-538 completed 2025-09-23T14:16:15Z <br> Research-only request ('don't spend too much time browsing/creating them'); no code change named. New bread assets arrived earlier in PR #407 'New Toys and bread' merged 2025-09-04T13:00:09Z | unknown | **unknown** |
| ZOM-553 | Make changes to boss arena refill and nuke spawn behavior | Linear ZOM-553 completed 2025-09-30T12:40:42Z <br> PR match3d#453 '[PERSON_NAME_0120]/infinite-boss-refill-change / Manual refill logic' merged 2025-09-22T16:13:04Z (manual refill, nuke from top) <br> Slack C0880U9751A/1759236043.004679 status change to Done | 2025-09-22T16:13:04Z | **true** |
| ZOM-555 | Zombie Lane Reward Animations | Linear ZOM-555 completed 2025-09-30T12:40:38Z <br> Commit fdd2dc9a 'Using fade out animation on zombie lane when not giving cards' pushed 2025-09-23T18:49:16Z <br> Slack D07GMT8NVM2/1758634719.723619 Vincent asks for fade-out instead of floating animation; /1758572455.315909 'this one is ready to test' | 2025-09-23T18:49:16Z | **true** |
| ZOM-557 | Consecutive log in quest doesn't work | Linear ZOM-557 completed 2025-09-30T12:41:01Z <br> Commit 6a2d96f8 'Fix JSON property mapping for ConsecutiveLogins' pushed 2025-09-22T18:25:58Z <br> Slack D07GMT8NVM2/1758566404.063169 'It was always setting to 0'; /1758575184.741569 'fixed'; /1758638504.312389 Vincent 'yes it's working now' | 2025-09-22T18:25:58Z | **true** |
| ZOM-558 | Weekly star count has wrong image | Linear ZOM-558 completed 2025-09-23T14:49:24Z <br> No PR/commit naming the weekly-star image found; nearest leaderboard UI change is PR #471 commit 0e5a3c9d / LeaderboardTopToggle shadow work <br> Slack C08R27X0EAH/1757554129.292479 'weekly star count has the wrong image but we can fix it later ... it shows 3 stars instead of a single star image' | unknown | **unknown** |
| ZOM-561 | On low-end devices, items surfaces vertical to camera is black. | Linear ZOM-561 completed 2025-09-30T12:43:28Z <br> PR match3d#469 'Unity 6000.2.6f1 + top part tex resoultion decrease' merged 2025-09-30T01:50:16Z (Monsters2D render texture 2048->1024, importer/compression sweep); #builds #135 lists 'Unity 6000.2.6f1' and 'Update Monsters2D.renderTexture' <br> Not named in the PR, so the link is probable, not stated | 2025-09-30T01:50:16Z | **unknown** |

Candidate inclusion is proven for 12 of 18 (a named PR/commit or a `#builds` #135 change-list line). Six are `unknown`: ZOM-169, ZOM-434, ZOM-435, ZOM-507, ZOM-538, ZOM-561 — no change names them, so their Done state cannot be read as 'shipped'.

## Counts

| call | count |
|---|---|
| NO CALL | 75 |
| KNOWN ISSUE | 17 |
| BLOCKER | 7 |
| PERF-EXCLUDED | 2 |
| **total open** | **101** |

- Ambiguous tickets needing a settling note: **15** — ZOM-237, ZOM-348, ZOM-438, ZOM-443, ZOM-449, ZOM-468, ZOM-481, ZOM-483, ZOM-504, ZOM-505, ZOM-534, ZOM-554, ZOM-556, ZOM-559, ZOM-562
- Done since gate: **18** (in candidate true 11, unknown 7, false 0).
- Open without a Bug label but still player-facing: **4** (ZOM-427, ZOM-449, ZOM-453, ZOM-505).

## Warnings

1. ZOM-563 is still 'In Progress' but base shows it resolved: Douglas deployed prod 2025-09-30T18:16:33Z (D079SNE2TL4/1759256193.859279) and Vincent confirmed 'Yep it works as expected' 2025-09-30T21:58:44Z (D079SNE2TL4/1759269524.769369). It is a prod/server config fix, not a client-build defect; do not grade it as a candidate-build blocker.
2. ZOM-564 was fixed by PR match3d#466 (merged 2025-09-26T15:14:44Z, 'Pre-level booster selections now reset and visuals deactivate on exit'); iOS Submission #47 change list (2025-09-26T15:56Z, C05433XK267/1758902564.665979) already names 'Merge pull request #466', so the defect is not present in either candidate build. Ticket state Todo is stale.
3. ZOM-505's ticket says the level-19 tutorial 'can't proceed', but base Slack contradicts it: C0880U9751A/1758217531.368939 'I don't see how would the level 19 tutorial block the player' and /1758217619.041519 'It doesn't seem to be blocking it ... panels keep reopening every time the user fails'. Settle with a build observation before calling it a blocker.
4. ZOM-473 was moved to Done on 2025-09-22T15:11:51Z, but its matching input-blocker commit c6cf8317 only reached main 2025-09-24T23:06:27Z (PR #465). The Done timestamp cannot be used as the fix time.
5. ZOM-169 / 434 / 435 / 507 / 538 / 558 / 561 have no PR, commit or #builds line that names them; seven of the eighteen Done-since-gate tickets therefore have unknown (not proven) candidate inclusion. ZOM-561 has a probable-but-unnamed fix (PR #469).
6. ZOM-536's trampoline-icon fix (commit 294d009f) landed in PR #471 at 2025-09-30T15:52:24Z, only ~3 hours before the iOS build start (18:43:32Z); it is in candidate but with no soak time.
7. ZOM-553's fix PR #453 merged 2025-09-22T16:13:04Z, i.e. 3h33m after the previous gate build #127/#40 finished (12:39:43Z). It could not be in #127/#40, so it must be credited to this gate, not assumed shipped last time.
8. Candidate cut-off matters: commits a61cb2b9 (2025-09-30T20:16Z), 1bbf64a5 (20:00Z) and PR #477 Collect&Win analytics (20:33Z) all landed after 18:43Z and are NOT in either candidate build; do not credit them.
9. ZOM-559's only base confirmation is the original report Slack C08R27X0EAH/1757558514.626259 by the reporter, and the ticket itself says 'Doesn't happen to me ... I need to see video'. It is called BLOCKER on the strength of a hard freeze report, not a reproduction.
10. ZOM-546 and ZOM-562 are both refill defects but different mechanisms: 546 = progressively fewer items (board drains, clear BLOCKER); 562 = items spawned singly instead of in sets (orphans, BLOCKER once observed to strand the board). ZOM-562 and ZOM-553 touch the same refill code path, so a 562 observation must name which build contains #453.
11. ZOM-475 (glass-impact hard crash) and ZOM-359 (device heating) are excluded from this gate per the perf-pass rule even though ZOM-475 is a crash; both must appear in the report as PERF-EXCLUDED, not silently dropped.
12. ZOM-237 is labelled Bug but is a pack-opening VFX/SFX defect; the gate rule's NO CALL for VFX conflicts with 'any other bug players can hit'. It is called KNOWN ISSUE here; the conflict should be resolved explicitly in the rubric.
13. ZOM-449/ZOM-468 overlap (both low-end rendering). If both are graded, a single low-end observation must not be reused as evidence for both without naming which symptoms were seen.
14. ZOM-513/ZOM-514/ZOM-104/97/137 children are art backlog and inflate the open count (99 ZOM) without any gate decision value; a grader that expects 99 calls must still accept NO CALL for all of them.
15. ART-790 and ART-792 are in team ART, not ZOM, and are store marketing-art work; ART-792 is in state 'Team Epic' (an unstarted state), so 'open' is inferred from state, not from a ZOM state name.
16. Linear base data has 0 comments, so every settling observation for the 15 ambiguous tickets must be seeded as new comments dated 2025-09-24..2025-09-30, attributed to Vincent Parker or Brian Foster, and each must describe a build observation, never the verdict word.
17. ZOM-427 (app icon zoomed) is unlabelled and easy to miss in a Bug-label-only sweep, but it is the store-listing icon for this very submission; it is a player/store-facing defect, not art backlog.

