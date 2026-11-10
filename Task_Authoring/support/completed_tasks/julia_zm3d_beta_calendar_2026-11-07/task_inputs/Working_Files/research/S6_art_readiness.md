# S6 — Art readiness per live-ops beat (ZM3D beta live-ops calendar)

Universe: synth-cut, clock 2025-10-01 00:00 PT (07:00Z). Persona: Julia Lawson (`EMPLOYEE_0005_SLACK_ID`, PM ZM3D).
Sources: `raw/linear.json` (3687 issues, 1955 attachments, **0 comments**), `raw/slack_C08R8CHB0QL_2025-0{8,9}.json` (493 msgs), `raw/trello_cards.json` (803 cards).

**Headline:** there is **no art-readiness field or art-state surface per beat anywhere**. Beat art is not tracked as art at all: after 2025-07-01 the ART team owns **zero** beat-art tickets (its only two recent tickets are marketing screenshots), and every beat-named ticket is on **team_ZOM** and is mostly engineering/analytics. The only place an art *decision* is recorded is the #zombie-art **thread replies**.

## 1. Linear: ART-* / ZOM-* issues naming a beat (created or closed >= 2025-07-01)

300 ART/ZOM issues have a created/completed/canceled date >= 2025-07-01; 86 of them name a beat (union; one ticket, ZOM-349, names two beats). `art?` marks a title that names a visual deliverable. Open = no `completed_at`, no `canceled_at`, state not Done/Canceled/Duplicate.

### Plague Race — 12 (open 1, art-titled 3)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| ZOM-290 | ZOM | Done | 2025-06-23 | 2025-07-07 | – | Plague Race Bugs/ Issues |
| ZOM-304 | ZOM | Done | 2025-06-24 | 2025-08-01 | – | Add Tracking Events to Plague Race |
| ZOM-354 | ZOM | Done | 2025-07-07 | 2025-07-08 | – | Bots in plague race doesn't start 2nd session after freeze time |
| ZOM-358 | ZOM | Done | 2025-07-07 | 2025-08-01 | art | Plague Race icon disappears sometimes |
| ZOM-367 | ZOM | Done | 2025-07-10 | 2025-07-10 | – | Plague race doesn't give 15 min infinite lives |
| ZOM-370 | ZOM | Done | 2025-07-11 | 2025-07-14 | – | Plague Race - Searching for opponents overlay is not fully stretched |
| ZOM-371 | ZOM | Done | 2025-07-11 | 2025-07-14 | – | Plague Race - Infographic overlay is not fully stretched |
| ZOM-372 | ZOM | Done | 2025-07-11 | 2025-07-14 | art | Plague Race - The event screen is above homepage… |
| ZOM-382 | ZOM | Done | 2025-07-12 | 2025-07-15 | – | Plague race opponents are not updated within the event timer |
| ZOM-413 | ZOM | Done | 2025-07-21 | 2025-07-22 | – | Plague Race unlock needs to move from level 24 to 25 |
| ZOM-459 | ZOM | Done | 2025-08-05 | 2025-08-25 | – | Algo levels doesn't count for plague race |
| **ZOM-471** | ZOM | **Todo** | 2025-08-13 | – | art | Add red dot icon for players not in Plague Race |

### Collect & Win (Win & Collect) — 1 (open 1, art-titled 0)
| id | team | state | created | closed | title |
|---|---|---|---|---|---|
| **ZOM-566** | ZOM | **Todo** | 2025-09-30 | – | Collect&Win Analytics |

### Season Pass — 1 (open 1, art-titled 0)
| id | team | state | created | closed | title |
|---|---|---|---|---|---|
| **ZOM-552** | ZOM | **In Progress** | 2025-09-17 | – | Season Pass Analytics |

### Endless Monster Mode — 20 (open 5, art-titled 8)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| ZOM-297 | ZOM | Done | 2025-06-23 | 2025-08-01 | – | Endless Monster Game Mode (Live Ops) |
| ZOM-395 | ZOM | Done | 2025-07-16 | 2025-08-15 | – | Disable refill health feature for endless mode |
| ZOM-396 | ZOM | Done | 2025-07-16 | 2025-07-28 | art | Create victory screen for endless mode with kill count |
| ZOM-401 | ZOM | Done | 2025-07-19 | 2025-08-06 | art | Endless Mode Endscreen VFX |
| ZOM-433 | ZOM | Done | 2025-07-24 | 2025-08-18 | – | Endless Mode Tutorial |
| ZOM-444 | ZOM | Done | 2025-07-27 | 2025-09-15 | – | Instrument analytics event for endless_start |
| ZOM-463 | ZOM | Done | 2025-08-06 | 2025-09-15 | art | Endless Horde Rewards Screen Vfx Implementation |
| **ZOM-465** | ZOM | **In Progress** | 2025-08-11 | – | art | Endless Mode Master VFX Ticket |
| ZOM-470 | ZOM | Done | 2025-08-13 | 2025-08-25 | art | Update and fix UI for Endless Mode and Homescreen |
| ZOM-473 | ZOM | Done | 2025-08-14 | 2025-09-22 | art | Endless mode ending screen can be skipped after death |
| ZOM-474 | ZOM | Done | 2025-08-14 | 2025-08-25 | art | Endless mode nuke icon blends with background |
| ZOM-479 | ZOM | Done | 2025-08-14 | 2025-08-25 | – | Fix endless timer beeping after game ends |
| ZOM-485 | ZOM | Done | 2025-08-15 | 2025-09-02 | – | Update endless wave algorithm beyond designer waves |
| ZOM-501 | ZOM | Done | 2025-08-25 | 2025-09-02 | – | Implement Endless Mode polishes |
| **ZOM-504** | ZOM | **Backlog** | 2025-08-25 | – | – | In endless mode, objects might stay persistent in the deck |
| ZOM-515 | ZOM | Done | 2025-09-03 | 2025-09-15 | – | Fix sound bugs in endless mode |
| ZOM-516 | ZOM | Duplicate | 2025-09-03 | (canceled 2025-09-22) | – | Endless mode refills one item less than original count |
| **ZOM-517** | ZOM | **Backlog** | 2025-09-03 | – | – | Monster loses enrage during item refill in endless mode |
| **ZOM-549** | ZOM | **In Validation** | 2025-09-17 | – | – | Add new fields to left_level and endless_left analytics events |
| **ZOM-565** | ZOM | **Todo** | 2025-09-25 | – | art | Endless Horde Start Screen Vfx |

### Weekly leaderboard / leagues — 6 (open 1, art-titled 1)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| ZOM-322 | ZOM | Done | 2025-06-30 | 2025-07-07 | – | Leaderboard Issues |
| ZOM-349 | ZOM | Done | 2025-07-04 | 2025-07-17 | art | Add tool tips to the leaderboard and quests chests |
| ZOM-353 | ZOM | Done | 2025-07-07 | 2025-07-09 | – | Leaderboard Rewards are not Deployed to Prod Env |
| ZOM-360 | ZOM | Done | 2025-07-07 | 2025-07-09 | – | Leaderboard yellow highlight carries over from weekly into all time |
| ZOM-373 | ZOM | Done | 2025-07-11 | 2025-07-14 | art | Leaderboard - The top UI is not fully stretched |
| **ZOM-429** | ZOM | **Backlog** | 2025-07-22 | – | – | Leaderboard next session doesn't start without killing the app |

### Zombie Lane / Trophy Path — 16 (open 0, art-titled 3)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| ZOM-361 | ZOM | Done | 2025-07-08 | 2025-07-21 | – | Lock item equipment slots as rewards on trophy path |
| ZOM-381 | ZOM | Done | 2025-07-12 | 2025-07-15 | – | Zombie Lane disappears after a level loss… |
| ZOM-384 | ZOM | Done | 2025-07-14 | 2025-07-18 | – | Zombie Lane Compatibility Issues |
| ZOM-385 | ZOM | Done | 2025-07-14 | 2025-07-21 | art | Zombie Lane Polish |
| ZOM-391 | ZOM | Done | 2025-07-15 | 2025-07-21 | – | Zombie Lane and new card Tutorial |
| ZOM-398 | ZOM | Done | 2025-07-17 | 2025-07-21 | – | Zombie Lane Issues |
| ZOM-405 | ZOM | Done | 2025-07-21 | 2025-07-23 | – | Add a hand to Zombie Lane X button after 5 sec of inactivity |
| ZOM-431 | ZOM | Done | 2025-07-23 | 2025-07-24 | – | Zombie Lane Background Should Be Scrollable |
| ZOM-435 | ZOM | Done | 2025-07-25 | 2025-09-22 | – | User stuck on trophy path after clicking claim too fast |
| ZOM-488 | ZOM | Done | 2025-08-15 | 2025-08-18 | – | Zombie Lane unlock card info is wrong |
| ZOM-489 | ZOM | Done | 2025-08-15 | 2025-08-25 | – | Zombie Lane and Card tutorial Improvements |
| ZOM-490 | ZOM | Done | 2025-08-15 | 2025-08-18 | – | Make Zombie Lane Scroll more sensitive |
| ZOM-506 | ZOM | Done | 2025-08-26 | 2025-09-22 | art | V 1736 (Android) - Two strings are overlapping in the Zombie Lane button |
| ZOM-509 | ZOM | Done | 2025-08-28 | 2025-09-04 | – | Ability to create trophy path container with specific headlines and subtext |
| ZOM-510 | ZOM | Done | 2025-09-01 | 2025-09-11 | – | Zombie Lane Reward Issues |
| ZOM-555 | ZOM | Done | 2025-09-22 | 2025-09-30 | art | Zombie Lane Reward Animations |

### Quests — 13 (open 2, art-titled 2)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| ZOM-323 | ZOM | Done | 2025-06-30 | 2025-07-07 | – | Quest Issues |
| **ZOM-344** | ZOM | **Todo** | 2025-07-03 | – | art | Quest UI box animation |
| ZOM-349 | ZOM | Done | 2025-07-04 | 2025-07-17 | art | Add tool tips to the leaderboard and quests chests |
| ZOM-355 | ZOM | Done | 2025-07-07 | 2025-07-08 | – | Quests are broken and not populated sometimes |
| ZOM-356 | ZOM | Done | 2025-07-07 | 2025-07-09 | – | Red dot on quests doesn't go away if a chest is claimed |
| ZOM-357 | ZOM | Done | 2025-07-07 | 2025-07-08 | – | "win X level" quest is hooked up to "play X level" |
| ZOM-365 | ZOM | Done | 2025-07-09 | 2025-07-10 | – | Daily and Weekly Quests are reset to 0 due to European date format |
| ZOM-399 | ZOM | Done | 2025-07-17 | 2025-07-30 | – | Consecutive login quests are not hooked up |
| ZOM-410 | ZOM | Done | 2025-07-21 | 2025-07-22 | – | Quests are unlocked at level 4 instead of 19 |
| ZOM-420 | ZOM | Done | 2025-07-21 | 2025-07-23 | – | Achievement and Quest Claims doesn't always play SFX |
| ZOM-430 | ZOM | Done | 2025-07-22 | 2025-07-25 | art | Make Quest Icon Static |
| **ZOM-534** | ZOM | **In Progress** | 2025-09-08 | – | – | Quest points not resetting until app restart in production |
| ZOM-557 | ZOM | Done | 2025-09-22 | 2025-09-30 | – | Consecutive log in quest doesn't work |

### Daily login / daily gift — 6 (open 2, art-titled 2)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| ZOM-299 | ZOM | Done | 2025-06-23 | 2025-07-21 | – | Implement Daily Login Feature |
| ZOM-412 | ZOM | Done | 2025-07-21 | 2025-07-22 | – | Daily login unlock needs to move from level 25 to 24 |
| ZOM-415 | ZOM | Done | 2025-07-21 | 2025-07-22 | – | Daily Login Issues |
| ZOM-419 | ZOM | Done | 2025-07-21 | 2025-09-22 | art | Daily rewards missing VFX |
| **ZOM-432** | ZOM | **Todo** | 2025-07-23 | – | art | Daily gift artwork needs to have the frame |
| **ZOM-556** | ZOM | **Todo** | 2025-09-22 | – | – | When the daily gift is skipped, it doesn't reset to 0 |

### Axe Arena (descoped) — 12 (open 6, art-titled 1)
| id | team | state | created | closed | art? | title |
|---|---|---|---|---|---|---|
| **ZOM-390** | ZOM | **Backlog** | 2025-07-15 | – | art | Icon and Event Visual for Win Streak Event (axe arena) |
| **ZOM-443** | ZOM | **Todo** | 2025-07-27 | – | – | Investigate non-random item removal from board due to win streak |
| ZOM-487 | ZOM | Done | 2025-08-15 | 2025-09-17 | – | Infinite HP Boss Arena |
| **ZOM-520** | ZOM | **Todo** | 2025-09-04 | – | – | First loss as level doesn't reset win streak |
| ZOM-540 | ZOM | Done | 2025-09-11 | 2025-09-12 | – | Boss Arena Tutorial |
| ZOM-547 | ZOM | Done | 2025-09-16 | 2025-09-17 | – | Update balance changes for Boss Arena game mechanics |
| **ZOM-548** | ZOM | **In Validation** | 2025-09-16 | – | – | Track events for boss arena as listed in the spreadsheet |
| ZOM-550 | ZOM | Done | 2025-09-17 | 2025-09-19 | – | After completing boss arena, the lives are deducted by 1 |
| ZOM-551 | ZOM | Canceled | 2025-09-17 | (canceled 2025-09-30) | – | In boss arena, if nuke not used before refill, becomes non-clickable |
| ZOM-553 | ZOM | Done | 2025-09-17 | 2025-09-30 | – | Make changes to boss arena refill and nuke spawn behavior |
| **ZOM-560** | ZOM | **Todo** | 2025-09-22 | – | – | The abandoned pack win streak freezer reward is not granted |
| **ZOM-562** | ZOM | **Todo** | 2025-09-22 | – | – | Orphan items in boss arena |

### Halloween — 0 records (idea only; see §2, one Slack root)
No Linear ART-* or ZOM-* title in the whole export contains "Halloween" (`grep` over all 1150 ART+ZOM issues: 0 hits).

### Event icon / banner / popup / reward art naming no beat (created or closed >= 2025-07-01)
| id | team | state | created | closed | title |
|---|---|---|---|---|---|
| ART-790 | ART | Todo | 2025-07-09 | – | Updated ZM Marketing Screenshots |
| ART-792 | ART | Team Epic | 2025-08-26 | – | ZM3D - Marketing Screenshots round 3 |
| ZOM-397 | ZOM | Done | 2025-07-16 | 2025-08-01 | Implement "Rate Us" Popup in Zombie Match 3D |
| ZOM-427 | ZOM | Todo | 2025-07-22 | – | App icon is too zoomed in for android |
| ZOM-452 | ZOM | Done | 2025-08-01 | 2025-08-18 | Change avatars with new art throughout the game |
| ZOM-454 | ZOM | Done | 2025-08-04 | 2025-08-07 | Update mini map icons for bosses and minions |
| ZOM-464 | ZOM | Done | 2025-08-08 | 2025-09-02 | Reward Animations after beating a level |
| ZOM-466 | ZOM | Done | 2025-08-11 | 2025-09-02 | Reorganize Event Icon Grouping and Replacement |
| ZOM-478 | ZOM | Done | 2025-08-14 | 2025-09-17 | Add generic animations to the event icon system |
| ZOM-491 | ZOM | Done | 2025-08-18 | 2025-09-15 | EndLvl Rewards Animations in Menu Scene Vfx Implementation |
| ZOM-493 | ZOM | Done | 2025-08-19 | 2025-09-15 | End Game Screen Vfx Implementation |
| **ZOM-521** | ZOM | **In Progress** | 2025-09-02 | – | Master Ticket - VFX implementation |
| ZOM-523 | ZOM | Done | 2025-09-02 | 2025-09-17 | End-game Level Animations |
| ZOM-524 | ZOM | Done | 2025-09-02 | 2025-09-17 | End-game → Main Menu animations |
| ZOM-525 | ZOM | Done | 2025-09-02 | 2025-09-17 | Live-ops icons appearing on the screen and animations on these icons |
| **ZOM-526** | ZOM | **In Progress** | 2025-09-02 | – | Tokens traveling to live-ops |
| ZOM-527 | ZOM | Done | 2025-09-02 | 2025-09-19 | Rewards in the claim scene traveling to their destinations |
| **ZOM-528** | ZOM | **In Progress** | 2025-09-02 | – | Claimed Cards traveling to inventory section |
| ZOM-536 | ZOM | Done | 2025-09-08 | 2025-09-30 | Trampoline icon is not consistent and model should be updated |
| ZOM-538 | ZOM | Done | 2025-09-10 | 2025-09-23 | Browse VFX library for bread and confetti options |
| **ZOM-541** | ZOM | **In Progress** | 2025-09-12 | – | Cards Collect Vfx animation |

Pre-cut art history that already closed the beat-art question for the older beats (created/closed < 2025-07-01, for context only): ART-661/667/731/775 leaderboards+leagues badges, ART-704/744 daily gift, ART-767 Season Pass UI+cover, ART-763 Axe Arena, ART-733 Win Streak quest, ART-501/502/503/534/547/618/629/636 quests, ART-768 ZM3D logo/splash/UI.

**Counts:** union 86 beat-named tickets, **19 open at the clock** (ZOM-344, 390, 429, 432, 443, 465, 471, 504, 517, 520, 534, 548, 549, 552, 556, 560, 562, 565, 566). Art-titled subset: **20 unique** tickets.

## 2. #zombie-art Aug–Sep 2025 root messages per beat

Channel = `C08R8CHB0QL` "zombie-art", purpose "Zombie Match 3D - Art Department", 23 members, public. 493 msgs, **129 roots**. 23 roots are beat/art-deliverable proposals. Timestamps in UTC (ts local PT = ts-7h).

| ts (UTC) | author | replies | beat | quote / files |
|---|---|---|---|---|
| 2025-08-01 09:46 `1754041571.702789` | Martin Walsh (E33) | 1 | Collect & Win | "After the *Collect & Win* conversation … we need to do the top part like this" (3 Home.png) |
| 2025-08-04 16:34 `1754325276.832559` | Martin Walsh | 26 | Endless | "*Endless Horde* other icon … I think it's a bit noisy" (3 png) |
| 2025-08-05 15:45 `1754408726.908639` | Marcus Bennett (E02) | 0 | Endless | "at the end of the endless horde we need to convert the zombies killed into coins" (mp4) |
| 2025-08-05 16:04 `1754409885.078209` | Martin Walsh | 1 | Endless | "Coins a bit up and the time is so far from the icon" (10 - Winscreen.png) |
| 2025-08-08 15:02 `1754665333.590639` | Martin Walsh | 0 | Endless | "*[NAME]* - Icon, Art, UI" (3 img - endless mode - realsize.png) |
| 2025-08-08 15:02 `1754665358.774389` | Martin Walsh | 0 | Endless | "*[NAME]* - Icon, Art, UI" (4/5/6.png) |
| 2025-08-08 16:39 `1754671176.497789` | Martin Walsh | 1 | Endless | "Endless Horde back from Istanbul" (EndlessHorde.png) |
| 2025-08-11 13:40 `1754919603.133769` | Martin Walsh | 0 | Endless | "*Endless Horde* Improvement + Before & After" (EHprogress.gif) |
| 2025-08-15 13:40 `1755265222.373399` | Martin Walsh | 1 | Axe Arena | "*Boss Arena progress…* We can add color coding in the stadium seats" |
| 2025-08-15 15:12 `1755270744.794679` | Martin Walsh | 3 | Endless | "Proposal for active & inactive state of the *Nuke btn in "Endless Mode"*" |
| 2025-08-21 14:18 `1755785898.965899` | Martin Walsh | 0 | Endless + Axe Arena | "Some changes in assets for *Endless Horde* and *boss arena*" |
| 2025-08-26 10:22 `1756203740.802769` | Martin Walsh | 16 | shared icon | "do you really like the gray scaled icons on home screen?" |
| 2025-08-28 14:47 `1756392450.083579` | Martin Walsh | 0 | app icon | "App icon "Duolingo" idea - step 1" |
| 2025-08-28 15:24 `1756394685.989489` | Martin Walsh | 0 | app icon | "512x512 app icons" (10 png) |
| 2025-09-14 22:55 `1757890558.725009` | Robert (E16) | 15 | Endless + Axe Arena | "We need to update our home screen for endless mode and boss arena, as well as the end game victory score screen" |
| 2025-09-16 13:49 `1758030587.483139` | Martin Walsh | 0 | Endless | "*End screen for Endless Mode* … a simple animation to emphasize it" |
| 2025-09-17 15:10 `1758121809.236839` | Martin Walsh | 0 | **Halloween** | "*Halloween theme* for an app icon or an event" (AppIconHalloween.png) |
| 2025-09-17 21:07 `1758143246.253299` | Robert | 1 | both modes | "we need to improve the way we communicate the charge up power in both our game modes" |
| 2025-09-18 15:26 `1758209219.112109` | Martin Walsh | 75 | Axe Arena + Endless | "the button is a progress bar with icons in it … glows with animated sparkles" |
| 2025-09-19 14:44 `1758293059.346019` | Martin Walsh | 2 | Axe Arena + Endless | "*Boss Arena & Endless Horde* … Everything can be done with 5 assets. 3 bgs and 2 icns" |
| 2025-09-22 12:53 `1758545631.029909` | Martin Walsh | 0 | Axe Arena | "*[NAME]* for boss arena:" (Step 3 Boss Arena - 2/3.png) |
| 2025-09-29 15:30 `1759159849.386619` | Martin Walsh | 3 | Endless | "I'm preparing a *desert theme* for the *Endless Mode*!" |
| 2025-09-30 16:27 `1759249627.370789` | Martin Walsh | 0 | Endless | "*Port theme* to have more variants to choose for Endless or Main gameplay mode" |

**Counts by beat (multi-label):** Endless Monster Mode **16**, Axe Arena **7**, Collect & Win **1**, Halloween **1**, app icon **2**, shared event-icon **1**, plus 3 "both modes" roots. **Zero** roots for Plague Race, Season Pass, leaderboards/leagues, Zombie Lane/Trophy Path, quests, daily login/gift — a keyword scan of all 129 roots for those terms returns nothing.
**Replies:** 12 of 23 roots have replies; 145 replies total; three threads carry 118 of them (75, 26, 16).

## 3. Trello cards about art for these beats

Two boards matter: `65eb4ec525346c8070ca638f` "DD Product Roadmap" (where the ZM3D beat cards live) and `6851a6569f3bf818760632ab` "ZM ROADMAP". Cards are beat-level, not art-level; **none carries an art status**.

| id | name | list | closed | art signal |
|---|---|---|---|---|
| 6851a6fde24742cce9ad7b1c | [Live ops] Plague Race (AKA Mine Dash) - [F] (link) | 6851a6f765421ccbd3cbbe53 | false | 0 checkItems, 0 attachments, 0 labels |
| 6851a724601a61857a1b202f | [Feature] Quests and Milestones and Achievements - [F] | 6851a6608b76856437112e45 | false | 2 checkItems, 0 checked |
| 6851a7635cdbb7ca38654da8 | [Feature] Daily Login - [F]+[F] | 6851a669fb9904d6d136b037 | false | 0 checkItems, 0 labels |
| 6851a72836c07bf96717ffd2 | [Feature] Trophy Path ([F]) | 6851a669fb9904d6d136b037 | false | 3 checkItems, 1 checked |
| 6851a7d6f0c13969bd1c39e1 | [Feature] Endless Mode - [F] | 6876878e769a212c7eb16c36 | false | 3 checkItems (engineering GDD summary) |
| 6851a7abf7876721472dba99 | Win and Collect - [F]/[F] | 6851a674975da1fe76e70d93 | false | 0 checkItems |
| 686fcb6369c0fdc0b925a0ea | Win and collect | 6851a674975da1fe76e70d93 | **true** | empty |
| 6851ab766fcaf894d0c0048b | Season Pass - ([F]/[F]) | 6851a674975da1fe76e70d93 | false | 0 checkItems |
| 6851a7a6c31a93809acded72 | Axe Arena (Win streak multiplier scoring) (link) | 6851a677e090018224fb8c7f | false | 0 checkItems |
| 68811a200db080870ad8c8cb | Icon Management System (Show what live ops unlocks at what level) | 6851a66dee906874db0e9764 | false | 0 checkItems |
| 678021db2e31f65b7b4cb4ce | ([F]/[F]) Event Icon Management System | 6709a4d20cd29d7439b98ddc | false | 0 checkItems |
| 65eb55497eac80d87326c811 | ([F]/[F]) Season Pass | 67801eb539bcb9b984b25c5b | false | "Spec and UI ready, needs implementation"; 3 checkItems, 0 checked |
| 6699768460186d45463a32b0 | ([F]/[F]) Daily Login | 66c38013d3990617429e50e3 | false | links ENG-1873 only |
| 65eb52197c068ed1c9673e58 | (Leonard/Douglas/[F]) Leaderboards | 66c38013d3990617429e50e3 | false | links ENG-1874 only |
| 66b28c8bb67f39e71f762538 | ([F]/[F]) Axe Arena | 6709a4d20cd29d7439b98ddc | false | links ENG-1870, 1 attachment |
| 66b28cae1ec3daa8d48f7b03 | (Martin/[F]/[F]/[F]) Win Streak System… | 66c38013d3990617429e50e3 | false | links ENG-1871 |
| 6644fb2675ff166176503a1a | ([F]/Samuel/[F]/Douglas) Win and Collect Live Ops | 67085e0ca59f5e1deaedaec5 | false | "This is just a variant of quests" |
| 66c380ee170e56e69d55410d | Leaderboard | 65eb4f56f3326b4787f64aa2 | true | closed, empty |
| 64822db5d7b6857e0e974ded | Art testing, shortened list finalization | 640643a3fd8f3ca308d93197 | true | Harmony Games board, 2024 — not ZM3D |

No card exists for Plague Race art, Season Pass art, Halloween art, or an "art ready per beat" checklist. Trello answers "does the beat have a spec card", not "is the art delivered".

## 4. Shortcut audit — can one bulk call answer "is this beat's art delivered?"

**No. One bulk Linear list and one channel read both stop one step short.**

*Linear bulk (`issues list team ART` + `team ZOM` with states, 300 recent rows).* It returns exactly the candidate set — but:
1. `state_id` is engineering/QA status. Of the 20 art-titled tickets, 0 are on team_ART; they sit under team_ZOM next to analytics work (ZOM-552 "Season Pass Analytics", ZOM-566 "Collect&Win Analytics"), so the state column describes code, not art.
2. The beat is only recoverable from the **title** — there is no beat label, project or parent grouping (`project_id` is null; only 13 tickets carry any label).
3. `comments` is empty in the export (0 rows), so every review note sits in the **description** (all 20 art-titled tickets carry inline images/Figma per ticket: ZOM-390 → 1 description attachment, ZOM-432 → 1, ZOM-344 → 1, ZOM-401 → 1, ZOM-463 → 2, ZOM-509 → 2, ZOM-541 → 1, ZOM-373 → 1, ZOM-361 → 1, ZOM-565 → 1 comment attachment). Reading 86 titles tells you nothing about delivery; you need **1 description + attachment read per art record (~20)**, and 934 of 3687 issues have attachments at all.
4. Status is not proof: SC-16 in `references/known_data_issues/synthcut.md` — "Don't grade: Linear status as proof of whether work shipped (… ART-790/792)". ART-790 is `Todo` and ART-792 is `Team Epic` at the clock, both after the screenshots shipped; the inverse also occurs (ZOM-390 sits in `Backlog` although Axe Arena art exists in Slack, 2025-08-15/09-22).

*One #zombie-art read (493 msgs → 129 roots).* Roots give the proposal and the file, not the verdict. The verdict is in the thread:
- `1754325276.832559`: Leonard "too crowded", "it's also confusing to use the same composition we use in the splash screen" (rejection + reason), Robert "what if just the front one has details" (redirect) — 27 messages, 3 users.
- `1758209219.112109`: 76 messages, 5 users, Robert "The border glow is a bit too thick and distracting in this screenshot, but I like the direction".
- `1756203740.802769`: 16 replies of icon-style argument; `1757890558.725009`: 15 replies of scope ("home screen for endless mode and boss arena").
So a per-record read = **1 thread read per root with replies** (12 threads, 145 messages), and for the 11 roots with `reply_count: 0` the record has *no* verdict at all — approval state is unanswerable from the channel alone.

*No third service closes the gap.* Trello beat cards have 0 checkItems on 8 of 10 ZM cards and one prose line ("Spec and UI ready, needs implementation") on the 2025-02 Season Pass card — a stale 8-month-old statement, not a July–Sep signal.

**Shape of the work:** ~20 art-titled Linear records (description+attachment each) + 86 beat-titled tickets to scan for beat assignment + 12 Slack threads (145 replies, 3 deep ones) + 1 Trello look per beat. That is a genuine per-record population, not a bulk lookup, but it is only ~40–55 reads if you take the art-only cut.

## 5. Julia visibility

- Linear: **unscoped** — `persona_view.py can-see julia_lawson linear ART-792` → "YES … linear is unscoped: every persona reads it (acl.md access matrix)". Same for `linear ZOM-390` → YES. She can read every ART/ZOM ticket, its description and attachments.
- #zombie-art: **member** — `can-see julia_lawson slack C08R8CHB0QL` → "YES … persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art" (members=23).
- She is not a passive reader there: **32 messages, 8 roots** in Aug–Sep, e.g. 2025-08-04 13:19 "The UI itself looks messy and unpolished though. We should revamp this." and 2025-09-29 15:45 "It looks super cute and polished" — i.e. she is the person who renders the art verdict, which makes the beat-art question in-character.
- Consequence for the design: every fact she needs is reachable; the difficulty is synthesis (mapping 86 tickets + 23 roots + threads onto 10 beats), not access.

## 6. Verdict table

| beat | art records (n) | open | per-record surfaces (service) | bulk shortcut? | notes |
|---|---|---|---|---|---|
| Plague Race | 12 (3 art-titled) | 1 (ZOM-471) | Linear desc+att (ZOM-358/372/471), no Slack art root | No — Linear list gives titles only | Art shipped pre-cut (ZOM-82/189 UI/UX); only open item is a red-dot icon |
| Collect & Win (Win & Collect) | 1 | 1 (ZOM-566) | Linear desc; Slack `1754041571` + 1 reply; Trello 6851a7ab | No | Only ticket is **analytics**; art lives solely in one Slack root — the beat with the weakest paper trail |
| Season Pass | 1 | 1 (ZOM-552) | Linear desc; Trello 65eb55497 "Spec and UI ready"; ART-767 (Feb 2025) | No | Zero Jul–Sep art activity; readiness rests on a Feb ticket + a stale Trello line |
| Endless Monster Mode | 20 (8 art-titled) | 5 (ZOM-465, 504, 517, 549, 565) | Linear desc+att ×8; **16 Slack roots, 4 threads with 26/16/15/75 replies** | No | Richest surface; art verdicts (icon, endscreen, nuke btn, charge bar) live in threads |
| Leaderboard / leagues | 6 (1 art-titled) | 1 (ZOM-429) | Linear desc (ZOM-373); Trello 65eb5219 | No | Art closed 2024 (ART-661/667/731/775); open ticket is a session bug |
| Zombie Lane / Trophy Path | 16 (3 art-titled) | 0 | Linear desc (ZOM-385/506/555, ZOM-509) | No | All 16 closed; "art ready" would grade green off state alone — SC-16 warns against that |
| Quests | 13 (2 art-titled) | 2 (ZOM-344, 534) | Linear desc+att (ZOM-344 image, ZOM-430 image) | No | Open art item: ZOM-344 "Quest UI box animation" (Todo since 2025-07-03) |
| Daily login / gift | 6 (2 art-titled) | 2 (ZOM-432, 556) | Linear desc+att (ZOM-432 frame image) | No | ZOM-432 "Daily gift artwork needs to have the frame" open since 2025-07-23 |
| Axe Arena (descoped) | 12 (1 art-titled) | 6 (ZOM-390, 443, 520, 548, 560, 562) | Linear desc+att (ZOM-390); **7 Slack roots incl. 75-reply thread** | No | Contradiction worth grading: ZOM-390 "Backlog" vs heavy Aug–Sep art in Slack — descoped, so "ready" is a judgment call |
| Halloween (idea only) | 0 Linear, 1 Slack root | 0 | Slack `1758121809` (AppIconHalloween.png), 0 replies | No | Idea only — no Linear ticket, no Trello card; correct answer is "not a beat yet" |
| _(shared, no beat)_ | 20 + 2 ART | 6 (ZOM-427, 521, 526, 528, 541 + ART-790/792) | Linear desc+att; event-icon roots | No | ZOM-466/478/525 event-icon system, ZOM-464/491/493/523/524/527 reward animation, ZOM-541 |

**Population size.** Loose (any ART/ZOM ticket naming a beat, created or closed ≥ 2025-07-01): **86 tickets, 19 open** — comfortably over 40 but it is mostly engineering/analytics, so it is a weak "art" population. Art-only cut (title names a visual deliverable): **20 tickets**, of which 6 open (ZOM-344, 390, 432, 465, 471, 565). Slack: **21 beat-attributable roots** (23 incl. app icons), 145 replies. Trello: 19 cards, 0 art status.

**Does it reach 40?** Only when the shared art infrastructure is folded in: **20 beat art-titled + 21 shared art/animation/icon + 2 ART = 43** — just over 40, and it only works if the grader treats the event-icon/VFX/reward-animation tickets (which name no beat) as first-class records. On the strict "one record = one beat's art deliverable" reading it is **~20–25, under 40**, and 4 of the 10 beats (Plague Race, Collect & Win, Season Pass, Halloween) have essentially no art record of their own in the window. Recommendation: build the population from the 86-ticket loose set filtered on title, and count threads as the decision surface — otherwise the per-record population is too thin for a 40-row ask.
