# S1 — ZM3D live-ops readiness census at the clock (synth-cut, 2025-10-01 00:00 PT)

Written by the build session from the S1 worker's verified findings (the worker ran out of steps before writing;
its findings are copied from its final report, locators unchanged). Items marked OPEN are completed in
`S1b_liveops_followup.md`.

## 0 · Push-notification sheet `f_a325dd4af80afc5994d5dc` ("Push Notifications Zombie Match", owner Resource, shared with Julia)

- Tab "PNs Beta": 14 data rows. Status **Ready**: lives recharged, 1-day lapse, 7-day lapse, D0-1 FTUE, **Plague Race**,
  **Weekly Leaderboard reset**. **Not Ready**: Quests, Hourly Coins, Win & Collect, Nathan's Treasure Hunt, Streak Fever,
  Axe Arena, Login Calendar, Season Pass. No Boss Arena, Endless or Zombie Lane row.
- Copy defects: the 1-day lapse and D0-1 FTUE rows say "Puzzles vs Zombies" (renamed 24 Jul 2025 per `page_zm3d_gdd`);
  the Plague Race row uses "🌊🚣 … outmatch rivals … Join Race" (River Rush-style copy). Every event row's
  "Status (NA, WIP, LIVE)" column = WIP.

## 1 · Snowflake `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE`

- 21 ZM3D rows: 20 Plague Race (EVT-0306 … EVT-0514, consistent 5-day windows, last 2025-09-22 → 09-26) and
  EVT-0527 Season Pass 2025-09-29 → 09-30 (61 participants, 32.8 %, $0). Degraded only EVT-0403 … EVT-0447 (ZOM-459).
- No ZM3D rows for Collect & Win, Boss Arena, Endless or leagues.

## 2 · Season Pass

- `page_season_pass_spec`: "Android 0.3.127 published Sep 22, iOS 0.3.49 released Sep 29 at $6.99"; "No Season Pass
  purchase has been recorded yet". Corroborated by Leonard `C0880U9751A/1759182908.627389` "I just released 0.3.49 on IOS"
  (VISIBLE). Known card SC-38 (ship date/analytics) applies.

## 3 · Beta date and scope (all VISIBLE)

- `C05KNDCHAAG/1757704290.799329` Leonard: "Beta target: Sep 30".
- `C090N54TG79/1758517286.431379` Leonard: "tech-stable beta in 15-20 days"; "Axe Arena is descoped".
- `C05KNDCHAAG/1758558164.541689` Brian: "postpone Axe Arena for the beta release".

## 4 · Plague Race rewards

- `C090N54TG79/1757478958.104989` Leonard (VISIBLE): "cut it in half … the last stage gives 250 instead of 500";
  reply `1757519586.231229` Vincent "60, 120, 250?"; reply `1757524860.067099` Leonard "sounds good".
- No Julia-visible completion record found (hidden: `C07C2866011` "plague stage rewards are fixed"; Brian→Douglas DM
  `D079SNE2TL4` request "Stage 1 - 60 Stage 2- 120 Stage 3- 250").

## 5 · Linear (state names)

ZOM-410 quests unlock → lvl 19 (Done) · ZOM-412 daily login → 24 (Done) · ZOM-413 Plague Race → 25 (Done) ·
ZOM-487 Infinite HP Boss Arena (Done 09-17) · ZOM-540 Boss Arena tutorial lvl 48 (Done) · ZOM-548/549 In Validation ·
ZOM-552 Season Pass Analytics In Progress · ZOM-553 Done 09-30 · ZOM-534 quest points prod bug In Progress ·
ZOM-556 daily gift Todo · ZOM-557 consecutive login quest Done 09-30 · ZOM-566 Collect&Win Analytics Todo ·
ZOM-353 leaderboard rewards not deployed to prod (Done) · ZOM-297 Endless (Done) · ZOM-510/555 Zombie Lane (Done) ·
ZOM-390 Axe Arena art (Backlog).

## 6 · GitHub

match3d#438 Season Pass merged 09-15 · #424 Infinite boss arena merged 09-12 · #468/#470/#472 Collect & Win merged
09-29/09-30 · #477 "Collect And Win Analytics and title change" OPEN (SC-18) · match3d-backend#16 weekly leagues merged ·
#19/#26 Endless daily/weekly merged · #10 Zombie Lane unmerged · #34 "Endless Monster Mode mix real players" OPEN ·
no Boss Arena backend PR; Douglas `C08R6BF4ENN/1756747348.667629` "BossArena API Endpoints are ready for testing on dev"
(VISIBLE) — SC-68 applies to any Boss Arena prod date.

## 7 · OPEN (see S1b)

Trello ZM ROADMAP evidence and the "Mine Dash" alias card; DM evidence (Robert, Frederick, Brian, Douglas, Vincent) on
calendar ownership and live/prod statements; Boss Arena / Collect & Win prod state; Halloween one-off; summary table.
