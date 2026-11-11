# S1b — ZM3D live-ops follow-up (synth-cut, clock 2025-10-01 00:00 PT / 07:00Z)

Read-only follow-up to `S1_liveops_census.md`. Sources: `research/tx/*.txt` (channel-month dumps),
`research/raw/{trello_cards,trello_lists,confluence,linear_issues,gh_prs}.json`.
Quote convention: text after the locator is copied verbatim; `[…]` marks a dump-side truncation
(several tx lines end mid-word in the export itself, not in this report).

## 1 · Trello ZM ROADMAP board `6851a6569f3bf818760632ab`

79 open+closed cards on the board, 8 lists: `Jun 18th` `6851a6f765421ccbd3cbbe53`, `Jun 30th`
`6851a6608b76856437112e45`, `July 18` `6851a669fb9904d6d136b037`, `Jul 24` `6876878e769a212c7eb16c36`,
`July 30` `6851a66dee906874db0e9764`, `BETA: Oct 10` `6851a674975da1fe76e70d93`, `Oct 21`
`6851a677e090018224fb8c7f`, `Backlog` `68c451221ebabaf255a7d16b`.
No list is called "Live"/"Production"; the beta list is literally named **"BETA: Oct 10"** (i.e. the board's
own beta date is Oct 10, nine days after the clock).

| id | name | list | closed | dueComplete | badges.dueComplete | due | dateLastActivity | desc (first 200) |
|---|---|---|---|---|---|---|---|---|
| `6851a6fde24742cce9ad7b1c` | `[Live ops] Plague Race (AKA Mine Dash) - [PERSON_NAME_0022] (link)` | Jun 18th | false | **true** | true | null | 2025-06-23T20:05:52Z | "Plague race event unlocks at level {X}\n\n[PERSON_NAME_0040] will specify" |
| `6851a7abf7876721472dba99` | `Win and Collect - [PERSON_NAME_0092]/[PERSON_NAME_0067]` | BETA: Oct 10 | false | **true** | true | null | **2025-09-30T16:40:13Z** | (empty) |
| `686fcb6369c0fdc0b925a0ea` | `Win and collect` | BETA: Oct 10 | **true** | false | false | null | 2025-07-15T17:15:24Z | (empty) |
| `6851ab766fcaf894d0c0048b` | `Season Pass - ([PERSON_NAME_0092]/[PERSON_NAME_0022])` | BETA: Oct 10 | false | **true** | true | null | 2025-09-18T16:02:56Z | (empty) |
| `6851ab7090e82351a14e7837` | `Infinite HP Boss Mode - ([PERSON_NAME_0054]/[PERSON_NAME_0120])` | BETA: Oct 10 | false | **true** | true | null | 2025-09-18T16:02:53Z | "You need to make at least 3 levels!" |
| `6851a7a6c31a93809acded72` | `Axe Arena (Win streak multiplier scoring) (link) - ([PERSON_NAME_0092]/[PERSON_NAME_0022])` | Oct 21 | false | **false** | false | null | 2025-09-23T00:34:20Z | (empty) |
| `6851a724601a61857a1b202f` | `[Feature] Quests and Milestones and Achievements - [PERSON_NAME_0022]` | Jun 30th | false | true | true | null | 2025-06-30T16:56:34Z | "Live ops feature" |
| `68c452a03006277f55d9dc96` | `Add more quests and balance quest rewards - (Leonard/Douglas)` | BETA: Oct 10 | false | **false** | false | null | 2025-09-12T17:31:20Z | (empty) |
| `6851a7635cdbb7ca38654da8` | `[Feature] Daily Login - [PERSON_NAME_0029] + [PERSON_NAME_0092]` | July 18 | false | true | true | null | 2025-07-23T19:08:41Z | (empty) |
| `6851a769c65dc0017a227bb7` | `[Feature] Push Notifications - Samuel + Leonard` | Jun 30th | false | true | true | null | 2025-06-30T16:51:19Z | (empty) |
| `68811a200db080870ad8c8cb` | `Icon Management System (Show what live ops unlocks at what level) ([PERSON_NAME_0029])` | July 30 | false | true | true | null | 2025-09-12T17:31:00Z | (empty) |
| — | *(no Halloween card)* | — | — | — | — | — | — | — |
| `6851a7d6f0c13969bd1c39e1` | `[Feature] Endless Mode - [PERSON_NAME_0120]` *(context, not requested)* | Jul 24 | false | true | true | null | 2025-08-01T16:46:04Z | "Provide engineering estimate based on the Endless Mode GDD…" |

Answers to the two directed questions:

- **Card `6851a6fde24742cce9ad7b1c` — does its name contain "Mine Dash"? YES.** Name verbatim:
  "`[Live ops] Plague Race (AKA Mine Dash) - [PERSON_NAME_0022] (link)`". So "Mine Dash" is a Trello-only
  alias for Plague Race, recorded 2025-06-23, and the card is `dueComplete: true` with `due: null`.
- **Halloween: there is no Halloween card.** `'halloween'` appears in **0 of the 803** card names+descs across
  every board in the export; the only near-match is a `witch` false positive in
  "`two tasks for Leonard 1- Add platform expansion…`" (board `640643a3fd8f3ca308d9318e`) and the
  "`switch`" false positives. There is also no Halloween page in Confluence (`confluence.json` page titles).
- **"Win and Collect" appears twice on BETA: Oct 10**: the live card `6851a7ab…` (dueComplete true, touched
  **the same afternoon as the clock-1 day, 09-30 16:40Z**) and a `closed: true` stub `686fcb63…` from 07-15.
- **Event icons**: only the Icon Management System card (`68811a200db080870ad8c8cb`, ready 09-12) — it is the
  *unlock-level* plan for the icons. Ownership is assigned to `[PERSON_NAME_0029]` in chat:
  `C090N54TG79/1755020337.373689` Julia: "`[PERSON_NAME_0029]` will bring the generic animations to the icons via the event icon management system so Marcus can focus on some other polishes".
- **`dueComplete: true` here does not mean shipped.** Every row above has `due: null`, so `dueComplete` was
  ticked by hand on cards with no due date; treat it as "owner says done", not as a ship date.

## 2 · Live-ops / prod / schedule statements in the tx files

`grep -inE "prod|deploy|dev |cron|schedule|window|calendar|live ops|liveops|beta|halloween|season|boss arena|collect|plague|push|notification"`
over all 26 channel-month dumps, keeping only lines that place a ZM3D live-ops feature on prod/dev/live,
name the live-ops calendar owner, or set the beta/UA/store date. ~35 lines, most relevant first.
(#channels with no usable dump: `#zombie-ops` `C08R6BF4ENN` has **no tx file**; `#builds` `C05433XK267` Sep
is 1133 bot lines with empty text, so no release/version content can be cited from it.)

**What is actually live for players (direct statements)**

1. `C090N54TG79/1759173389.051889` 09-29 19:16Z Vincent Parker: "The only casual live ops implemented is plague race [USERNAME_44360]. Quests can be more all around." → as of 09-29, Plague Race is the only *casual* live-ops implemented.
2. `C090N54TG79/1759173457.020249` 09-29 19:17Z Robert: "yeah, [USERNAME_15751] is not a casual/hardcore live ops, and we have boss arena/endless mode/leaderboards/quests, those are all standard.."
3. `C08R27X0EAH/1756479479.210449` 08-29 14:57Z Vincent Parker: "As I've checked the live build on android, all liveops seem fine. But those problems above happen at D1 so I need to test at midnight UTC to tell if it's really live or not."
4. `C0880U9751A/1754584405.631159` 08-07 16:33Z Leonard Hayes: "• plague-race on prod gets stuck at level 2 and doesn't progress • endless mode gets stuck on day 2 and you can't pass the claim button and restart" → Plague Race **and** Endless are on prod by 08-07.
5. `C08R27X0EAH/1754561478.754139` 08-07 10:11Z Vincent Parker: "Both plague race and endless mode problems about the daily reset happens only in prod. So the changes should be deployed to prod and I don't think it requires client update."
6. `C08R27X0EAH/1756111564.591469` 08-25 08:46Z Vincent Parker: "Looks like plague race and endless mode doesn't refresh in production servers. It was a dev build, I tried the same build with dev servers and both event refreshed successfully so it must be related to backend".
7. `C08R27X0EAH/1756460310.538629` 08-29 09:38Z Vincent Parker: "ios 1504 prod env • Endless mode didnt refresh daily - cannot open the event page. • plague race didn't refresh daily either - it shows yesterday's race with ended text • Leaderboard is also ended".
8. `C08R27X0EAH/1754669246.962529` 08-08 16:07Z Douglas: "the scheduler job responsible for resetting the state of the events in production didn't start correctly after the last deployment to production. […] I will check the jobs on prod after every deployment" → the reset cron is a manual post-deploy check.
9. `C08R27X0EAH/1757289825.998289` 09-08 00:03Z Leonard Hayes: "My quest points didn't reset after I completed the day while still being online. They only got reset after I kill the app and restarted it […] this is on production" → bot reply `C08R27X0EAH/1757291682.062479`: "`[PERSON_NAME_0055]` created an urgent issue ZOM-534 Quest points not resetting until app restart in production".
10. `C08R27X0EAH/1758420497.482989` 09-21 02:08Z Leonard Hayes: "Bug endless mode. Tried to use [USERNAME_25225] the screen froze. Samsung galaxy s23 ultra - production build".
11. `C08R27X0EAH/1757478773.396819` 09-10 04:32Z Leonard Hayes: "At level 112 live ops buttons disappeared"; Douglas `…/1757521981.511819` "probably There was a network error/lag that caused the issue" → live-ops buttons fail *silently* on a network blip at high level.
12. `C090N54TG79/1758081958.128639` 09-17 04:05Z Leonard Hayes: "she didn't click any of the liveops icons once lol" (playtest of the live icon row).
13. `C0880U9751A/1758062399.419489` 09-16 22:39Z Robert: "I mean it LOOKS done but the event name is liveops_completion, which seemed a bit generic"; and `…/1758063971.551409` "But in that actual sheet, the event name is "liveops_completion"" → the analytics event name is generic per-event, not per feature.

**Who plans the live-ops calendar** — *not stated in any tx line.* Nothing in the dumps names a calendar owner;
the only "calendar" hits are PTO (`C05KNDCHAAG/1757071068.089219` "as in the Harmony Games Calendar") and a
rotation rule (`C0880U9751A/1757087510.020719` "The rotation is by calendar day, not how many times you've
entered the event"). The authoritative answer is in Confluence §3/§6 below.

**Beta scope and the Sep 30 builds**

14. `C05KNDCHAAG/1757704290.799329` 09-12 19:11Z Leonard Hayes: "<!here> We finalized the dev pipeline for the beta. […] If we ship *Win & Collect*, *Reward Animations*, *Season Pass*, and *Infinite HP Boss Mode by end of next week*, the beta goals are achievable. […] Every item has a clear *product owner*; if you're un[…]"
15. `C05KNDCHAAG/1758558164.541689` 09-22 16:22Z Brian Foster: "<!here> We've decided to postpone Axe Arena for the beta release. We'll be focusing on tech issues and bugs".
16. `C090N54TG79/1758517286.431379` 09-22 05:01Z Leonard Hayes: "Priorities: • Fix tech issues first. Axe Arena is descoped […]" (also "tech-stable beta in 15-20 days", per S1 §3).
17. `C090N54TG79/1757104901.003829` 09-05 20:41Z Brian Foster: "he mentioned that he's still working on Pass. In my last test, I encountered 1–2 major bugs, and since the development environment hasn't been updated, I wasn't able to test some scenarios […] we won't be able to run proper testing for Season P[ass]".
18. `C05KNDCHAAG_2025-08/1756479808.414869` 08-29 15:03Z `EMPLOYEE_0032_SLACK_ID`: "working on infinite boss live ops fake endpoints integration to speed up process when backend api will be ready" → Boss Arena was still on **fake endpoints** on 08-29.
19. `C0880U9751A/1758148677.056319` 09-17 22:37Z Robert: "Can you weigh in on A/B testing where There are 2 different versions of trophy path (AKA Zombie Lane) Where the item release schedule is different?" (Zombie Lane = Trophy Path/Trophy Road alias.)

**Store submission / UA start (the beta is not a store event on its own)**

20. `C0880U9751A/1757561483.446549` 09-11 03:31Z Leonard Hayes: "submitted to app store, when it's approved we'll start buying users at small scale" → **UA start is gated on store approval, not on a date**.
21. `C0880U9751A/1758124084.022179` 09-17 15:48Z Leonard Hayes: "IOS is submitted last night to the app stores - it's under review".
22. `C08R27X0EAH/1758081917.318539` 09-17 04:05Z Leonard Hayes: "but no other blockers - I'm submitting the build now to the app store to save some time".
23. `C08R27X0EAH/1758409417.505029` 09-20 23:03Z Arthur Blake: "testflight 39 is the submission candidate".
24. `C08R27X0EAH/1758767858.307829` 09-25 02:37Z Leonard Hayes: "Once it's merged we can trigger a testflight build and then can submit to Apple. It will take a few days to go live".
25. `C0880U9751A/1759182908.627389` 09-29 21:55Z Leonard Hayes: "I just released 0.3.49 on IOS" (the iOS Season Pass build; S1 §2).
26. `C090N54TG79/1757713193.398699` 09-12 21:39Z Leonard Hayes: "even if we want to fix it it will take us 3 days and approvals from app stores to fix it" → any post-submission fix slips the store date by ~3 days.

**Halloween** — only two tx lines exist in the whole dump set (see §4):
27. `C08R8CHB0QL/1758121809.236839` 09-17 15:10Z Martin Walsh: "*Halloween theme* for an app icon or an event: <@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0038_SLACK_ID> <@EMPLOYEE_0005_SLACK_ID>".
28. `C090N54TG79/1754327052.292539` 08-04 17:04Z Leonard Hayes: "I think we are leaning a bit too much into Halloween theme with these collectibles but that's just me" (about the **collectibles art**, not an event).

Negative pins (searched, absent): no tx line gives a ZM3D **Collect & Win** or **Boss Arena** prod/live date;
no line assigns live-ops calendar ownership; no `cron`/`window` scheduling statement for a ZM3D event aside
from the reset jobs in #8 and the D1/midnight-UTC testing in #3.

## 3 · Collect & Win vs Win & Collect, and the #477 "title change"

The two names are **not a rename — they are the same feature on two different games**, and both names are correct
for their own game. Three independent records:

1. **Confluence `page_liveops_calendar` ("Live-Ops Event Calendar & Planning", space OPS, version 3, updated
   2025-09-29T17:00:00Z)** — row: "`Collect & Win` | `Zombie Match 3D` | Recurring weekly, in three staggered
   windows (Mon-Tue, Wed-Thu, Fri-Sun) that all players share | Built for the end-of-September beta submission
   (QA blockers cleared 26 Sep 2025); **not yet live**. **Same feature as Win & Collect on Domino Delights, under
   a different name**". The same table's `Win & Collect` row is the *Domino Delights* entry: "Shipped Oct 2024 —
   Domino Delights' first live event".
2. **Linear `ZOM-60`** "Zombie Ops #2 Spec (Brain Chase)", state **Done** 2025-06-23T18:25:14Z: "This the
   collectibles-based LiveOps event, aka **zombie version of Win and Collect.** Working title is Brain Chase with
   the alternate event name Serum Therapy." → in ZOM the feature was internally the zombie port of Domino's
   Win and Collect, and the event name itself was still unsettled ("Brain Chase"/"Serum Therapy") on 06-23.
3. **GitHub `harmonygames-Games/match3d#468`** "Collect And Win", merged 2025-09-29T16:13:50Z: "Added "**Collect
   & Win**" live event: collect tokens in levels, track progress, claim stage rewards and a grand prize".

The `#477` "title change":

- **`match3d#477` title: "`Collect And Win Analytics and title change`"** — state **open**, created
  **2025-09-30T22:26:30Z** (five hours before the clock), head ref "`[PERSON_NAME_0067]/collectAndWinAnalytics`",
  base `main`, +97/−13. **Merged: none.** Body (CodeRabbit summary): "App emits and tracks Collect & Win start and
  reward-claimed events (includes event duration, stage, and reward details). […] Total event duration now computed
  from explicit start and end times […] Initial color/state corrected to avoid an unintended default on load."
  The PR says nothing about *which* string changed; its only "title" content is the analytics event naming, which
  matches Robert's complaint that the event name was "`liveops_completion`, which seemed a bit generic"
  (`C0880U9751A/1758062399.419489`). **Treat "the title change" as the analytics event title, not a player-facing
  rename** — no record anywhere states the player-facing name changed.
- Adjacent evidence that the player-facing string is "Collect & Win" and is stable: `#470` "Collect And Win minor
  bugs fixes" (merged 09-30T15:51:15Z) fixes "* In Boss arena and endless mode, the c&w UI is visible."; Trello
  card `6851a7abf7876721472dba99` is still named "Win and Collect" (the Domino name) while sitting on the ZM board.
- **Hazard:** a task that asks for "Win & Collect" on ZM3D is asking for the wrong artefact; the ZM3D name is
  **Collect & Win**, and the only open record touching the name (`#477`) is unmerged.

## 4 · Martin's Halloween post `C08R8CHB0QL/1758121809.236839` — replies and follow-ups

**No replies, no thread, no follow-up anywhere in the tx files. It is a standalone one-line post.**

- Full line: `1758121809.236839 09-17 15:10Z Martin Walsh: *Halloween theme* for an app icon or an event:
  <@EMPLOYEE_0016_SLACK_ID> <@EMPLOYEE_0038_SLACK_ID> <@EMPLOYEE_0005_SLACK_ID>`
  — the dump marks threads explicitly (`[thread N replies]` on the parent); this line has none.
- Reverse check: `grep -rn "1758121809" tx/` returns **only that line** — no message anywhere replies to it.
- It directly follows a skull-asset remark in the same channel, `C08R8CHB0QL/1758121796.411499` 09-17 15:09Z
  Martin Walsh: "May be the skull is too infant..." (reply to `1758115815.450659` "New items coming with this PR.
  These can have color variants.") — i.e. the Halloween line is a comment on the new item/VFX art, not an event brief.
- Follow-up search `grep -rin -e halloween -e pumpkin -e witch tx/` → 17 raw hits, of which the only genuine
  Halloween content is the post above plus `C090N54TG79/1754327052.292539` (08-04, Leonard: "leaning a bit too
  much into Halloween theme with these collectibles"), plus an unrelated art moodboard list at
  `C0880U9751A/1758300550.745699` 09-19 16:49Z Arthur Blake: "• *Halloween:* Pumpkin Lantern, Witch Hat, Candy
  Bucket, Skull, Cauldron." (a themed-asset brainstorm). All other hits are `switch`.
- Product-side: **no Halloween card** (§1), **no Halloween Confluence page**, **no ZOM issue** with Halloween in
  the title/description, and **no PN sheet row** (S1 §0 lists 14 rows, none seasonal/Halloween).
  → A Halloween event at the clock is an *idea in the art channel only*: no scope, no date, no owner, no calendar slot.

## 5 · Robert–Julia (`D05GU6L0XFH`) and Frederick–Julia (`D05SD5QLG94`) DMs, Sep 2025

**Robert–Julia, Sep 2025 (`D05GU6L0XFH_2025-09.txt`, 713 lines): almost no live-ops content.** The DM is level
design/CPM/bot balance end to end. Every line that even touches release/live status, in order:

| ts | quote |
|---|---|
| `1756753271.503299` 09-01 19:01Z R | "You can get started if you want, because we can still just check "Production" even if I am not done" (level-creation flag, not a live-ops switch) |
| `1757114092.160729` 09-05 23:14Z R | "screenshots all in Figma" (level screenshots) |
| `1757427451.179859` 09-09 14:17Z J | "It never went live, the change was on the pool sizing branch only." |
| `1757427516.894299` 09-09 14:18Z R | "Live as in it made it into a test build, Leonard's hands, designers tools" |
| `1757427537.117609` 09-09 14:18Z R | "Not live in appstore" |
| `1757610820.396329` 09-11 17:13Z R | "But I didn't uncheck "is production"" |
| `1757610828.618889` 09-11 17:13Z R | "So they ended up as 151-170 in this release" |
| `1758903086.698869` 09-26 16:11Z R | "the coffee table and books, are they clickable and is the level playable at least by human?" |

- Zero hits for `collect`, `season pass`, `plague`, `boss arena`, `endless`, `league`, `quest`, `beta`, `UA`,
  `event`, `calendar` in this DM. **Robert is not a live-ops or calendar source in Sep.**
- The only UA line in the whole Robert DM is August: `D05GU6L0XFH_2025-08.txt/1755192473.247309` 08-14 17:27Z
  Julia: "It does but it only has AB Group MF true or false. Will it have all variants once we start the UA?" →
  Robert `…/1755192544.327439` "That's actually a good question" (i.e. UA-readiness question left unanswered by him).
- **Hazard:** "Not live in appstore" (09-09) and "is production" here refer to *individual levels*, not to
  features; a search that greps this DM for "live"/"prod" will manufacture false live-ops facts.

**Frederick–Julia, Sep 2025 (`D05SD5QLG94_2025-09.txt`) — the entire month is 4 messages, all 09-18, all playable:**

| ts | quote |
|---|---|
| `1758220925.518329` 09-18 18:42Z Frederick Stone | "Hey [PERSON_NAME_0040], PlayableX is looking for these assets to build the ZM3D playable. Can I ask who the best person would be to grant them access? • *3D assets*: .fbx, .glb, or .blend […] • *2D assets*: .png […] • *Font*: .ttf or .woff2 • *Sound*: .m[…]" (dump-truncated) |
| `1758221343.478869` 09-18 18:49Z Julia Lawson | "Hey, [PERSON_NAME_0036]. [PERSON_NAME_0092] fished out the assets for the Domino playable before so I think he's your guy." |
| `1758221397.722469` 09-18 18:49Z Julia Lawson | "I would also ask Marcus if you're going to use 2D zombie animations because he'd made them with bones." |
| `1758221424.223519` 09-18 18:50Z Julia Lawson | "Last time we didn't give them access, we just put what they needed in a zip file and sent it over." |

- So the only **UA-side** Sep artefact in the Frederick DM is the **PlayableX ZM3D playable** asset request
  (09-18), handled by Robert + Marcus, with the precedent that the vendor gets a **zip, not repo/store access**.
  No beta date, no UA start date, no screenshots thread in Sep (the screenshot work is August:
  `D05SD5QLG94_2025-08.txt/1756234644.700299` Frederick: "I issued him a ticket. <…/ART-792/zm3d-marketing-screenshots-round-3>").
- **Frederick Stone owns the live-ops calendar** — but that fact lives in Confluence, not in this DM:
  `page_liveops_calendar` "Owner: Frederick Stone (Growth/UA). This page is the single source of truth for what
  live-ops events are scheduled…", and "Design, led by Julia Lawson, walks the coming weeks with Frederick Stone".

## 6 · Summary table

`PN row` = status of that row in the shared Push-Notifications/Zombie Match sheet (`f_a325dd4af80afc5994d5dc`,
S1 §0). `—` = no row on that sheet.

| feature (ZM3D) | in Sep 30 build (evidence) | live on prod (evidence) | PN row | open blocker | hazard |
|---|---|---|---|---|---|
| **Plague Race** (a.k.a. **Mine Dash**) | yes, long before: live on prod from ≤08-07 (`C0880U9751A/1754584405.631159` "plague-race on prod gets stuck at level 2"); 20 events EVT-0306…EVT-0514, last window 09-22→09-26 (S1 §1) | **yes** — the one casual event players actually had: `C090N54TG79/1759173389.051889` "The only casual live ops implemented is plague race" | **Ready** | reward re-tune in flight (`C090N54TG79/1757478958.104989` "cut it in half"; S1 §4); ZOM-459 algo-level scoring closed 08-25 | "Mine Dash" is a **Trello-only alias** (`6851a6fde24742cce9ad7b1c`); PN copy is River-Rush copy (S1 §0); daily-reset cron breaks on deploy (`C08R27X0EAH/1754669246.962529`) |
| **Collect & Win** (NOT "Win & Collect") | **merged but incomplete**: `match3d#468` merged 09-29T16:13Z, `#470` merged 09-30T15:51Z; `#477` analytics+title **still open** (created 09-30T22:26Z) | **no** — Confluence: "not yet live" | **Not Ready** (row named "Win & Collect") | `#477` open → no start/reward telemetry at launch; ZOM-566 "Collect&Win Analytics" **Todo**; c&w UI leaking into Boss Arena/Endless (`#470` body) | name collision with Domino's Win & Collect (`page_liveops_calendar`); two Trello cards, one closed stub |
| **Infinite HP Boss Mode / Boss Arena** | yes: `#424` merged 09-12, ZOM-487 Done 09-17, ZOM-540 tutorial @ lvl 48 Done 09-12, ZOM-553 Done 09-30T12:40Z; Trello `6851ab7090e82351a14e7837` dueComplete | **unproven** — only dev evidence, `C08R6BF4ENN/1756747348.667629` "BossArena API Endpoints are ready for testing on dev"; backend was on "fake endpoints" 08-29 (`C05KNDCHAAG_2025-08/1756479808.414869`) | **no row** | no Boss-Arena backend PR found (S1 §6); ZOM-548 analytics still In Validation | any prod date must survive SC-68; "Boss Arena" and "Infinite HP Boss Mode" are two names for one feature (Trello vs Linear) |
| **Season Pass** | yes: `#438` merged 09-15; Android 0.3.127 pub. 09-22, iOS 0.3.49 released 09-29 (`page_season_pass_spec`; `C0880U9751A/1759182908.627389` "I just released 0.3.49 on IOS") | **live and monetising from 09-29** — EVT-0527 2025-09-29→09-30, 61 participants (S1 §1) | **Not Ready** | ZOM-552 Season Pass Analytics **In Progress**; "No Season Pass purchase has been recorded yet" (`page_season_pass_spec`) | shipped with **$0 revenue and zero purchase**; PN copy still says "Puzzles vs Zombies" parity rows; 24h season-pass freeze is a process control, not code |
| **Quests** | yes: ZOM-410 unlock lvl 19 Done; ZOM-557 consecutive-login quest Done 09-30 | yes, **with a prod bug**: `C08R27X0EAH/1757289825.998289` "this is on production" → ZOM-534 | **Not Ready** | **ZOM-534 In Progress** (points don't reset until app restart) | quests are the only progression-side live-ops; Vincent: "Quests can be more all around" |
| **Daily Login / daily gift** | partial: ZOM-412 unlock 24 Done; login quest fixed 09-30 (ZOM-557) | yes as Login Calendar/daily gift | **Not Ready** (row "Login Calendar") | **ZOM-556 Todo** — "When the daily gift is skipped, it doesn't reset to 0" | card `6851a7635cdbb7ca38654da8` marked done 07-23 with `due:null`; streak logic still wrong at the clock |
| **Endless Monster Mode** | yes, older: ZOM-297 Done 08-01; reached players in Android 0.3.99 / iOS 0.3.11 (Aug) per `page_liveops_calendar` | **yes** — `C08R27X0EAH/1756479479.210449` live-build check; but prod-only refresh bugs 08-07/08-25/08-29 | **no row** | reset cron fragility (`C08R27X0EAH/1754669246.962529`); crash `C08R27X0EAH/1758420497.482989` "production build" freeze 09-21 | backend#34 "Endless Monster Mode mix real players" **OPEN**; calendar page: "permanent board mode, not a seasonal event" — do not treat as an event slot |
| **Leagues / weekly leaderboard** | yes: `match3d-backend#16` weekly leagues merged (S1 §6) | yes — `page_liveops_calendar`: ZM3D "overlaps Plague Race, Leagues and both Endless Monster resets" | **Ready** ("Weekly Leaderboard reset") | ZOM-353 leaderboard rewards were dev-only, closed 07-09 | "Leagues" and "Weekly Leaderboard" are the same surface under two names |
| **Zombie Lane (Trophy Path/Trophy Road)** | yes: ZOM-510 Done 09-11, ZOM-555 Done 09-30T12:40Z | yes as a permanent level-gated track (`page_liveops_calendar`: "Permanent (level-gated reward track) Live") | **no row** | `match3d-backend#10` Zombie Lane **unmerged** (S1 §6) | three names (`Zombie Lane` / `Trophy Path` / `Trophy Road`, cf. `C0880U9751A/1758148677.056319`), plus a live A/B on item release schedule |
| **Axe Arena** | **no — descoped**: `C05KNDCHAAG/1758558164.541689` "postpone Axe Arena for the beta release"; `C090N54TG79/1758517286.431379` "Axe Arena is descoped" | no | **Not Ready** | ZOM-390 art still **Backlog** 07-15 | Trello keeps it in `Oct 21` not `BETA: Oct 10`; any Sep-30 statement about Axe Arena is wrong by two sources |
| **Halloween event / icons** | **no artefact at all**: 0 Trello cards, 0 Confluence pages, 0 ZOM issues, 0 PN rows | no | **—** | none — nothing was scoped | sole source is a one-line art post with **no replies** (`C08R8CHB0QL/1758121809.236839`); an agent that "finds" a Halloween event is hallucinating it |
| **Event icon row / Icon Management** | yes: Trello `68811a200db080870ad8c8cb` dueComplete 09-12; `C090N54TG79/1755020337.373689` `[PERSON_NAME_0029]` "will bring the generic animations to the icons via the event icon management system" | live icons exist; **fail silently** — `C08R27X0EAH/1757478773.396819` "At level 112 live ops buttons disappeared" | n/a | none tracked | icon row is the one place all features surface, so one icon bug hides every event at once |

**Three conclusions the data forces**
1. *Live* and *shipped* are different facts on this board: Plague Race / Endless / Leagues / Zombie Lane /
   Season Pass are live; Collect & Win and Boss Arena are built-but-not-live; Axe Arena and Halloween are not built.
2. The board's beta date is **"BETA: Oct 10"**, while chat's beta target was Sep 30 — and store approval, not a
   date, gates UA ("when it's approved we'll start buying users at small scale").
3. Calendar ownership is **Frederick Stone** (Confluence `page_liveops_calendar`), with Julia walking the coming
   weeks with him — that is the only calendar-ownership record; no Slack line says it.
