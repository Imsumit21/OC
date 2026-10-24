# HarmonyGames — Persona Briefs (Spec V2)

> **V3 use:** both freeze dates use the same local universe data. These briefs
> include events after October and are discovery leads. Verify role/remit/activity
> from dated records at the assigned freeze; later departures, pivots or wind-down
> facts cannot be October knowledge. No separate October dataset or KB review is needed.

> Fixed clock **2026-02-14T00:00:00Z** (Saturday). The taxonomy's 19 personas and their exact emails are in [`persona_roster_v2.json`](persona_roster_v2.json); read visibility is governed by [`Docs/4_Persona ACL Policy - V2.md`](Docs/4_Persona ACL Policy - V2.md). The briefs describe what people do across the storylines; they are orientation, not evidence — verify anything you rely on with `Task_Authoring/tools/hg.py search` from the persona's view.

> **Services:** 13 — Gmail, Slack, Google Calendar, Drive, Docs, Sheets, Slides (persona-scoped reads); GitHub, Linear, Trello, Contacts (shared); Confluence and Snowflake (unscoped and live; listed in the current agent system prompt). Writes are not governed by ACL; check `Evals/references/tools/catalog.json`. Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, CRM, Airtable, QuickBooks and Stripe are narrative systems — evidence about them lives in the 13 services.

> Refreshed 2026-10-03 from the V1 briefs: clock and service list corrected, Thomas and Tim Steudler added below with measured footprints. **Only 17 are usable**: the Evals roster omits `thomas` and `tim_steudler`, `/prompt` fails its identity gate for them, and their data cannot carry a task (`Scenario_Atlas.md`).

## How to read these

Each brief follows a consistent shape:
- **Active work** — what they own day to day
- **Key relationships** — internal + external
- **Open threads** — live storylines they sit on
- **Recent activity** — artifacts they've touched

---

## Task-visible personas (19)

Use the roster's exact email for identity configuration; never derive it from a
name. Universe Explorer is author god-mode, while the Agent Runner and Run
Verifiers share the same required persona and scoped read view. There is no
task-visible Finance persona or CFO.

### Leonard Hayes — Co-founder & Creative Director · `leonard.hayes@harmonygames.co` · Executive · `leonard_hayes`
**Active work:** The studio's primary operator. Drives product direction, live-ops strategy, difficulty tuning, the analytics stack, fundraising (2023 seed, 2024 board cadence, 2025 bridge round), and most external vendor/partner relationships. Owns the financial model and runway narrative.
**Key relationships:** Internal — Arthur Blake (co-founder/CTO), Robert (co-founder/design), Frederick Stone (BD/UA); leans on Douglas/Owen Baker/Oliver Brooks for engineering and Julia Lawson/Brian Foster for product. External — Griffin Gaming Partners, AppLovin (Marcus Lee), Solsten, Adjoe, Mattel (Barbie pitch), outside counsel.
**Open threads:** Failed $2.5M bridge round · Mattel "Dream Life Glow" pitch · Combo Fighter live experiment · Telegram DD port · Helpshift wind-down · company runway/wind-down.
**Recent activity:** Investor-update emails, board decks, pitch decks (Drive), most `#founders`/`#investors`/`#executives` decisions, GSheets performance models, and Metabase dashboard evidence referenced in available Slack/Drive artifacts.

### Arthur Blake — Co-founder & CTO · `arthur.blake@harmonygames.co` · Executive · `arthur_blake`
**Active work:** Owns engineering architecture and the internal tooling saga (puzzle editor, bot/sequencer, difficulty simulation, vision-bot QA). Built the financial model that anchored the seed pitch; co-signatory/secretary on the Carta advisor-equity program; personally bridge-funded the company via promissory notes. Reviews/merges most major PRs.
**Key relationships:** Internal — Leonard Hayes, Robert, Douglas (backend), Owen Baker/Oliver Brooks (Unity). External — Griffin counsel, Carta.
**Open threads:** WebGL build-size reduction for the CrazyGames deal · Combo Fighter backend (sign-in/leaderboards) · Telegram MiniApp WebGL work.
**Recent activity:** PRs across `GameOfDominoes`/`match3d`/`Combo-Fighters`, bot-balancing merges, `#engineering-bots`/`#builds` CI coordination.

### Robert — Co-Founder & Creative Director · `robert@harmonygames.co` · Executive · `robert`
**Active work:** Game design & art direction lead. Sets the puzzle-design philosophy, difficulty curves, character/VFX quality bar (Sophie/Nathan), the progression/card economy, and UX. Runs competitor benchmarking. Co-drove the seed fundraise.
**Key relationships:** Internal — Leonard Hayes, Arthur Blake, Marcus Bennett/Claire Morgan/Victor Barnes (art), Julia Lawson/Brian Foster (product), Martin Walsh (UI). External — early art contractors, Lucas (Tile Dozer).
**Open threads:** Combo Fighter design/live tuning · Progression Philosophy GDD · character-ability VFX debates.
**Recent activity:** GDDs and design docs (Drive), `#game-design`/`#god-gameart`/`#god-vfx`/`#prototype` threads, level-balance decisions.

### Frederick Stone — Co-founder · `frederick.stone@harmonygames.co` · Executive · `frederick_stone`
**Active work:** Owns the external UA/ad-network and creative-vendor portfolio end-to-end — AppLovin, Google Ads, Adjoe, Node Media, PlayableX, Solsten — plus brand naming/trademark and the ad-monetization rollout. Runs soft-launch campaigns and attribution setup.
**Key relationships:** Internal — Leonard Hayes, Robert, Marcus Lee/George Miller (UA), Marcus Bennett (creative). External — AppLovin, Adjoe, Node Media, PlayableX, Google.
**Open threads:** Domino Delights sunset & pivot to a new title's UA · PlayableX ZM3D playable (stalled) · fundraising-metrics pressure.
**Recent activity:** Vendor Slack channels (`#node-external`, AppLovin/Adjoe channels), UA campaign setup, ASO/store-listing work, Gmail vendor threads.

### Brian Foster — Game Engineer · `brian.foster@harmonygames.co` · Engineering · `brian_foster`
**Active work:** Drives cross-title live-ops features (Win Streak, Leaderboards, Collect & Win, Season Pass, Daily Login/Gift) and difficulty-tuning workstreams across GoD and match3d. Owns live-ops UI optimization tickets.
**Key relationships:** Owen Baker, Oliver Brooks, Calvin Price, Douglas (engineering); Martin Walsh/Marcus Bennett (art); Leonard Hayes/Robert (product direction).
**Open threads:** Live-ops UI optimization (ENG-2404) · Collect & Win Magical Wings tuning · Combo Fighter UX proposal.
**Recent activity:** `#winandcollect`/`#season-pass`/`#zm-collect-win` threads, Linear ENG/ZOM live-ops tickets, reward-table specs (Sheets).

### Julia Lawson — Product Manager · `julia.lawson@harmonygames.co` · Product · `julia_lawson`
**Active work:** Product/design decisions across Domino Delights and GoD — TAM validation, FTUE/tutorial tooling requirements, puzzle difficulty tuning, progression/card-economy design. Owns the puzzle-layout pipeline (1200 levels) and drove the Mattel pitch deck + Q&A prep.
**Key relationships:** Arthur Blake (ships her tooling), Robert/Leonard Hayes (design), Martin Walsh/Claire Morgan (art), Brian Foster (live-ops).
**Open threads:** Mattel "Dream Life Glow" deck & anticipated-Q&A · Zombie Match Lite scoping · tutorial-editor backlog.
**Recent activity:** `#mattel_proposal`/`#game-design`/`#zombie-design` threads, DES/ENG Linear tickets, GDDs and pitch decks (Drive).

### Vincent Parker — Game Systems Engineer · `vincent.parker@harmonygames.co` · Engineering · `vincent_parker`
**Active work:** QA and systems engineering across live-ops features — structured QA passes (Season Pass, Daily Login, River Rush, Collect & Win), event/economy tickets, and 4X-crypto tokenomics design. Files many of the ZOM live bugs.
**Key relationships:** Owen Baker, Calvin Price, Oliver Brooks, Samuel Turner (engineering/QA); Brian Foster (product).
**Open threads:** ZOM live-bug triage (daily login resets, tornado-boost physics, win-streak-freezer) · 4X proposal economy.
**Recent activity:** Linear ZOM bug tickets, `#zombie-bugs`/`#4xgameproposal` threads, QA canvases.

### Victor Barnes — Game Engineer · `victor.barnes@harmonygames.co` · Engineering · `victor_barnes`
**Active work:** *(Roster: Engineering.)* In the storylines, leads the art/animation team — character-ability VFX quality bar, character-profile UI, outsourced art-vendor management (Leapblock, Martin Walsh), and Quests art. Supplies hero video and UA creative.
**Key relationships:** Marcus Bennett, Claire Morgan, Martin Walsh (art); Robert/Leonard Hayes (direction); Ozhan (freelance animator).
**Open threads:** Zombie animation roster (Ozhan) · marketing-asset production.
**Recent activity:** ART Linear tickets, `#god-gameart`/`#god-vfx` threads, and Figma art references/exports available through Linear, Slack, Drive, or GitHub.

### Marcus Bennett — Artist · `marcus.bennett@harmonygames.co` · Design · `marcus_bennett`
**Active work:** Character art, animation, and VFX across GoD and Zombie Match 3D — Sophie's UX-to-3D pipeline, custom character-ability VFX, an in-house UA video pipeline that outperformed agency creative, and End Game/Endless Mode VFX for match3d.
**Key relationships:** Robert, Victor Barnes, Claire Morgan, Calvin Price (VFX handoff), Frederick Stone (UA creative).
**Open threads:** match3d VFX integration (PR #408 handoff) · UA video refresh.
**Recent activity:** ART tickets, `#god-vfx`/`#zombie_marketing` threads, VFX PRs and marketing videos.

### Douglas — Software Engineer · `douglas@harmonygames.co` · Engineering · `douglas`
**Active work:** Backend lead. Built the original Python/FastAPI backend and AWS stack, the Firebase→BigQuery analytics pipeline, and the Quests and Leaderboards backends. Handles live-incident player compensation manually.
**Key relationships:** Felix Young (Quests backend), Arthur Blake, Owen Baker; Simon Walker (analytics contractor).
**Open threads:** Leaderboards scaling (Step Functions/cache) · stalled player-compensation tool.
**Recent activity:** Backend PRs (liveops repo), ENG Linear tickets, `#analytics`/`#engineering-bots` threads.

### Owen Baker — Game Engineer (Unity) · `owen.baker@harmonygames.co` · Engineering · `owen_baker`
**Active work:** Data infra (Firebase→BigQuery, Singular reconciliation, Remote Config A/B) plus live-ops feature delivery (Win Streak, Leaderboards, Collect & Win, IAP/offers) and R&D prototypes.
**Key relationships:** Arthur Blake, Douglas, Brian Foster, Vincent Parker.
**Open threads:** Win Streak / Collect & Win match3d ports · combo-leveling UI (Combo Fighter).
**Recent activity:** `GameOfDominoes`/`match3d` PRs, ENG/ZOM tickets.

### Oliver Brooks — Senior Game Engineer · `oliver.brooks@harmonygames.co` · Engineering · `oliver_brooks`
**Active work:** Senior Unity engineer (hired mid-2024 backfill). Built and shipped the full Season Pass (GoD then match3d), Win Streak/IAP fixes, FTUE, and Zombie Match Lite branch work; contributes to Combo Fighter.
**Key relationships:** Arthur Blake, Brian Foster, Calvin Price, EMPLOYEE_0032.
**Open threads:** Zombie Match Lite (stalled) · Combo Fighter combo rarity/leveling.
**Recent activity:** `match3d`/`Combo-Fighters` PRs (Season Pass PR #438), ZOM tickets, `#season-pass`/`#zombie-match-lite`.

### Calvin Price — Game Engineer (Unity VFX) · `calvin.price@harmonygames.co` · Engineering · `calvin_price`
**Active work:** Unity/live-ops engineer — Daily Login/Gift build, Helpshift integration, Season Pass QA builds, VFX integration.
**Key relationships:** Brian Foster, Oliver Brooks, Vincent Parker, Marcus Bennett.
**Open threads:** Daily login reset/refresh live bugs · Helpshift rollout.
**Recent activity:** `match3d` PRs, ZOM tickets, `#zombie-match3d` threads.

### Claire Morgan — Art Lead · `claire.morgan@harmonygames.co` · Design · `claire_morgan`
**Active work:** Art lead — Sophie expression/marketing art, coin/tile prefabs and collision meshes (Tile Dozer), Quests art, TAM/market research support.
**Key relationships:** Robert, Marcus Bennett, Victor Barnes, Martin Walsh.
**Recent activity:** ART tickets, `#god-gameart`, Drive art assets, and Figma references/exports linked from available services.

### Samuel Turner — Game Designer · `samuel.turner@harmonygames.co` · Design · `samuel_turner`
**Active work:** Client UI + tooling — Quests UI, vision-bot editor tooling, win-streak debug tooling, WinStreakFreeze unit-bug fix.
**Key relationships:** Arthur Blake (vision bot), Douglas (Quests), Vincent Parker, Robert.
**Recent activity:** `match3d`/`GameOfDominoes` PRs, ZOM/ENG tickets.

### Martin Walsh — Game Designer · `martin.walsh@harmonygames.co` · Design · `martin_walsh`
**Active work:** UI/UX art via Figma — marketing site, character select/profile UI, live-ops event UI (Season Pass, River Rush, Collect & Win), ASO screenshots. Engaged via the Leapblock outsourcing arc, retained individually.
**Key relationships:** Victor Barnes, Robert, Leonard Hayes, contractor-era leads.
**Recent activity:** ART tickets, `#god-ui-ux` threads, and Figma file references/exports linked from available services.

### Simon Walker — Data Analyst (Contractor) · `simon.walker@harmonygames.co` · Engineering · `simon_walker`
**Active work:** Stood up the BigQuery/dbt/Metabase analytics layer and the retention dashboards; drove Singular reconciliation and manual data-detective work. Evidence about these non-direct systems is available through Slack, Gmail, Drive, GSheets, GitHub, and Linear artifacts.
**Key relationships:** Leonard Hayes, Douglas, Arthur Blake, Owen Baker.
**Recent activity:** `#analytics` threads, dashboard/spreadsheet artifacts.

### Thomas — Game Developer · `thomas@harmonygames.co` · Engineering · `thomas` *(new in V2)*
**Footprint (measured 2026-10-03):** Slack user `EMPLOYEE_0018_SLACK_ID`; a primary calendar with ~2,900 events, mostly 2024 (company standups, art syncs, build readouts, all-hands) and ~350 in 2025. Contacts lists only first name and role.
**Use with care:** "Thomas" is ambiguous in the universe — Thomas Baker (Orrick, outside counsel) is a different person. Verify every reference against the email, not the first name.
**Before building:** map his Slack channels and Drive shares from his view; his scoped evidence is calendar-heavy and older than the 2026 window.

### Tim Steudler — Business Development Manager, Licensing · `tim.steudler@harmonygames.co` · Sales · `tim_steudler` *(new in V2)*
**Footprint (measured 2026-10-03):** Slack user `UBF5AB53C96`; a primary calendar with 5 events, all in 2025 (a meeting series with Leonard Hayes; the invite thread also copies Frederick Stone). In V1 storyline notes he was the Mattel-side licensing contact for the Barbie "Dream Life Glow" pitch; the universe now carries him with a HarmonyGames address.
**Use with care:** his persona-scoped footprint is thin. A task from his view must lean on shared services (GitHub, Linear, Trello, Contacts), on Confluence/Snowflake only after verifying access, or on seeded records his persona can read. Prove reach from his view before writing anything.

## Other internal storyline participants

The people below can appear in universe data but are not task-visible Persona
ACL identities. Do not select them as the required task persona.

### Felix Young — Feature Lead (Backend) · `felixyoung@harmonygames.co` · Engineering · `felix_young`
**Active work:** Co-built the Quests backend with Douglas (Google Sheets ingestion, endpoints, Lambda layers).
**Key relationships:** Douglas.
**Recent activity:** ENG-636 family tickets, liveops backend.

### Matthew Collins — Co-Founder & CEO · `matthew@harmonygames.co` · Executive · `matthew_collins`
**Active work:** In the storylines acts as advisor/board member and legal-response lead — quarterly board cadence, 2025 bridge round ($25K commit), and the Superplay/TYZ Law patent defense.
**Key relationships:** Leonard Hayes, Robert, Arthur Blake; TYZ Law; Griffin.
**Recent activity:** `#aa_boardmeeting_room`/`#investors` threads, board decks.

### Michelle Carter — General Counsel · `michelle.carter@harmonygames.co` · Executive · `michelle_carter`
**Active work:** Led the Series Seed legal close — Delaware C-corp conversion, SPA + ancillary docs (IRA, Voting Agreement, ROFR/Co-Sale, Disclosure Schedule) with Griffin.
**Recent activity:** Legal docs (Drive), Gmail closing threads.

---

## Marketing / UA, Sales / BD, and External / Redacted personas

These appear inside storylines (often vendor-facing) but rarely author internal tasks. Emails/IDs are canonical; several are redacted tokens.

| Name | Title | Dept | Email | ID |
|------|-------|------|-------|----|
| Marcus Lee | User Acquisition Manager | Marketing | marcus.lee@harmonygames.co | marcus_lee |
| George Miller | User Acquisition Manager | Marketing | george.miller@harmonygames.co | george_miller |
| Megan Wilson | User Acquisition Manager | Marketing | megan.wilson@harmonygames.co | megan_wilson |
| Victoria Lane | User Acquisition Manager | Marketing | victoria.lane@harmonygames.co | victoria_lane |
| Christopher Allen | Marketing Site Contractor | Marketing | christopherallen@harmonygames.co | christopher_allen |
| Marcus | Backend Engineer | Engineering | marcus.lee@harmonygames.co | marcus |
| Lucas | Game Developer (contractor) | Engineering | lucas@harmonygames.co | lucas |
| EMPLOYEE_0032 | Senior Unity Engineer | Engineering | employee_0032@harmonygames.co | person_0001 |
| Oscar Bennett | VFX / Character Ability Artist | Design | oscar@harmonygames.co | oscar_bennett |
| Ozhan | Freelance Character Animator | Design | ozhan@example.com | ozhan |
| patrick | BD / Partnerships Manager (Solsten) | Sales | patrick@harmonygames.co | patrick |
| Josh Dempsey | BD Manager (Solsten) | Product | josh.dempsey@example.com | josh_dempsey |
| Benjamin Clark | Outside Counsel (source profile: Co-Founder & CEO) | Executive | benjamin.clark@harmonygames.co | benjamin_clark |
| Thomas Baker | General Counsel (Orrick) — not the `thomas` persona | General | thomas.baker@harmonygames.co | thomas_baker |
| Person 5536 | BD / Partnerships (web distribution) | Sales | person_5536@example.com | person_0008 |
| Person 3937 / 6073 / 6078 | BD, Playable-Ads Partnerships (PlayableX) | Marketing | person_*@example.com | person_0009/10/11 |
| Olivia (6062) / Person 0498 / Person 3009 | UA / Vendor Managers (Node Media) | Marketing | person_*@example.com | person_0012/13/14 |
| Person 3086 / 3299 | UA Managers (Adjoe) | Marketing | person_*@example.com | person_0006/07 |
| Person 3011 / 2568 / 5402 / 3123 | BD / Operations / Legal-Ops Leads (Superplay/TYZ) | Operations | person_*@example.com | person_0002–0005 |
| Person 6072 | Game Developer (RPG prototype) | Engineering | person_6072_slack_id@example.com | person_0015 |

> **Source-data cleanup notes** (not Persona ACL roster values): `josh dempsey@example.com` → `josh.dempsey@example.com`; `olivia (person_6062)@example.com` is a placeholder. Calvin Price's source department shows as `VFX) / Engineering` (a split artifact) — the exact ACL roster value is **Engineering**. `Marcus` and `Marcus Lee` share `marcus.lee@harmonygames.co` in source service data — a storyline collision to reconcile.

---

## External companies, investors & vendors (appear in artifacts, never author tasks)

- **Investors / board:** Griffin Gaming Partners (lead, Series Seed), Sisu Capital & Play Ventures (competing 2023 term sheets), 1AM Gaming / a16z Games Speedrun / Turkish fund / GFR / General Catalyst (2025 bridge rejections), TOR Capital / Carta (angels, cap table).
- **Legal:** Rimon PC (Benjamin Clark), Orrick (Thomas Baker), TYZ Law (Superplay patent).
- **UA / ad vendors:** AppLovin (Marcus Lee, George Miller), Adjoe, Node Media, PlayableX, Google Ads, Singular (attribution), Solsten (player insights, Josh Dempsey/patrick).
- **Partners:** Mattel Game Studios (Barbie pitch; see Tim Steudler above), CrazyGames / BoomBit (web/mobile distribution), Big Time / Open Loot (4X crypto), Deel (payroll), Helpshift (support SaaS).
- **Competitors referenced:** Superplay ("Domino Dreams"), Royal Match, Match Factory, Solitaire Grand Harvest, Candy Crush.
