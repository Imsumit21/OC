# HarmonyGames — Universe Brief (Spec V2)

> **V3 use:** both freeze dates use the same local universe data. This orientation
> spans events on both sides of an October freeze. Normalize the assignment and pass
> `task_context.py --task-dir <task_dir> --write --require-source` before grounding.
> Use the shared source/KB as leads and validate each fact at the assigned freeze.
> Later events cannot be completed facts; later-edited bodies need dated earlier
> evidence. No separate October dataset/KB build is required. V3 overrides old rules.

> One reference replacing V1's `0_Universe_One-Pager.md`, `1_Universe_Summary.md`, `3_Task_Categories_Business_Functions.md` and `5_Reference_Sheet.md`. Refreshed 2026-10-03: clock, service count, persona count, Gmail send capability, Snowflake/Confluence and GCal/GSlides corrected; counts re-measured where marked ✓. Orientation only — verify anything a task relies on with `Task_Authoring/tools/hg.py search`.

## The company

HarmonyGames is a small, founder-led mobile game studio building casual puzzle
games. Founded 2023; the founders rejected an NFT concept and pivoted to a
domino-matcher — **Game of Dominoes**, shipped as **Domino Delights** — then raised a
**$3M Series Seed at $10M post** led by **Griffin Gaming Partners**. **Zombie Match 3D**
(`match3d`) followed in 2025, and **Combo Fighter** (fighting-meets-match-3) is the
most recently launched title. Late 2025 into early 2026 is existential: runway
collapse, a **failed $2.5M bridge round**, a run of prototypes (Combo Fighter,
Zombie Match Lite, a Barbie/Mattel pitch, a 4X crypto concept), and a wind-down
under way by February 2026. Many arcs end unresolved — good material for
"reconstruct what actually happened / what is still open" tasks.

| Fact | Value |
|---|---|
| Fixed clock | **2026-02-14T00:00:00Z**, a Saturday. Nothing on or after it has happened |
| Domain | `harmonygames.co`; GitHub org `harmonygames-Games` |
| Task personas | 17 usable (`Evals/references/persona/roster.json`); the taxonomy lists 19 (`persona_roster_v2.json`) — `thomas` and `tim_steudler` fail `/prompt`'s identity gate; briefs in `Persona_Briefs.md` |
| Assignment axes (V2) | Business function (the persona's department: Design, Engineering, Executive, Product, Sales) · Competency (Product Management, Engineering Ops, Marketing and GTM, Corporate Ops, Finance) · Task skill (Retrieval, Analysis and Synthesis, Planning and Decision Support, Authoring, Actions) · Task type (normal, long-horizon) |
| Environment | `env_id` `hg4-with-gsuite-bundle-1174`, `universe_id` `hg4-2026-08-31` (from the V2 upload template) |

V1's six weighted "business functions" (Engineering & Live-Ops 25%, …) are retired.
In V2 the business function is the persona's department and the kind of work is
set by the competency, which need not be the obvious match for the job title.

## The thirteen services

| Service | Size | Read scope | What it is good for |
|---|---|---|---|
| Slack | 985 channels, 219 users, ~586K messages | Scoped | Decisions, running commentary, the richest source of evidence and distractors |
| Gmail | ~24.7K messages / ~21.2K threads | Scoped | The external view: investors, counsel, vendors, partners. Can send, reply and draft |
| Google Drive | ~30K files | Scoped | Where written deliverables land; uploads and exports |
| Google Docs | 633 docs ✓ | Scoped (Drive ACL) | GDDs, specs, legal, board updates, meeting notes |
| Google Sheets | 398 files / 1,553 tabs | Scoped (Drive ACL) | Financial models, economy grids, analytics exports |
| Google Slides | 164 decks ✓ | Scoped (Drive ACL) | Weekly updates, pitch and board decks |
| Google Calendar | 39 calendars, 11,233 events ✓ | Scoped | Ordering evidence, deadlines, who met whom |
| Contacts | 171 records ✓ | Shared | Resolving "whoever owns it" to an address; records are sparse |
| GitHub | 16 repos, 2,629 PRs, 12,687 commits ✓ | Shared | What actually shipped and when; reviews are often CodeRabbit-only |
| Linear | 5 teams, 2 projects, 3,852 issues ✓ | Shared | Work-of-record and the usual destination for follow-ups |
| Trello | 5 boards, 803 cards ✓ | Shared | Roadmap and prototype planning, often stale against Linear |
| Confluence | 4 spaces, 31 pages ✓ | Unscoped (live) | Policies, runbooks, specs an agent should apply |
| Snowflake | 3 databases, 40 tables | Unscoped (live) | Figures that must be derived by query (spend, installs, revenue, burn) |

Confluence and Snowflake are confirmed live and unscoped (`Evals/ENVIRONMENT.md`,
`service-availability-v1`). The current agent system prompt lists all 13 "available
systems", Confluence and Snowflake included (the V1-era prompt listed 11).

Exact tools and parameters: `Evals/references/tools/catalog.json` (298 tools).
Narrative-only systems (no tools): Firebase, BigQuery, Metabase, App Store Connect,
Google Play, AppLovin, Singular, Figma, Carta, CRM, Airtable, QuickBooks, Stripe —
evidence about them lives in the thirteen services.

## Write surfaces (from the catalog)

Slack (post, reply, edit, schedule, draft, react, create conversations) · Gmail
(send, reply, drafts; labels, archive, trash, delete) · Linear (issues, comments,
projects) · GitHub (issues, comments, PRs, reviews, branches, files, labels) ·
Trello (cards, comments, members, labels, lists, checklists) · Drive (create, update,
move, share, trash) · Docs / Sheets / Slides (create, batch-update, append) ·
Calendar (create, update, delete events, RSVP) · Contacts (add, edit, delete) ·
Confluence (create/update pages and spaces, comments). Writes are never governed
by the persona ACL; a write the catalog cannot do makes a task infeasible.

## Systems of record

A feature's truth is rarely in one place: a Slack decision → a Linear ticket → a
GitHub PR → a Drive spec → sometimes a Gmail vendor thread → the numbers in
Snowflake. Tasks that read only Slack and Gmail miss half the story.

- **Linear** — what shipped vs stalled (keys `ENG-`, `ART-`, `DES-`, `EPI-`, `ZOM-`; `ENG-####` and `ZOM-###` are different series). Issues carry **no PR link** (`links` is empty on all 3,852 ✓): reconciling Linear with GitHub goes through titles, branches or commit messages — real friction.
- **GitHub** — code-of-record; PR state, reviews, branches. Many PRs were "reviewed" only by the CodeRabbit bot — be careful with criteria about human approval.
- **Trello** — roadmap-of-record, frequently out of date relative to Linear.
- **Drive family** — design-of-record (GDDs), money-of-record (models, board decks, notes, cap-table docs), pitch-of-record.
- **Gmail** — external-of-record: commitments, closings, vendor contracts and invoices.
- **Snowflake** — derived figures; answers usually need a query and an aggregation.
- **Confluence** — conventions and process documents that can resolve an otherwise ambiguous instruction.

## Storylines (76 across 10 lenses)

- **founders-exec (5)** — vetting Arthur Blake and sizing founding bets · contractor pay cadence / equity philosophy / Delaware incorporation · cash-conscious retreat planning · NFT/hypercasual pivot debate · the Mattel Barbie "Dream Life Glow" pitch.
- **fundraising-finance-legal (8)** — 2023 seed model · competing term sheets, Griffin wins · Series Seed close (SPA/IRA/voting) · founder bridge loans · Superplay/TYZ Law patent threat · advisor equity via Carta · 2024 board cadence and investor reporting · 2025 Crownfall crypto pivot and the failed bridge.
- **marketing-growth-gtm (8)** — female-35+ TAM thesis via Solsten · naming Domino Delights · harmonygames.co build · inbound BD after the seed · Marcus Bennett's in-house UA video pipeline · AppLovin soft launch (AU/NZ/CA) · ASO readiness and Node-managed UA · Zombie Match 3D naming, store assets, alpha→beta.
- **analytics-data-stack (8)** — Firebase→BigQuery pipeline · S3→BigQuery · Singular attribution and the cross-platform discrepancy hunt · Remote Config A/B infra · funnel-driven tutorial redesign · stalled player-compensation tool · Bayesian pity/win-rate optimisation · rebuilding match3d instrumentation.
- **live-ops-events-economy (8)** — Quests · Collect & Win · Win Streak "Nathan's Treasure" · Leaderboards (Dec 2024) · offers/IAP store · ad monetisation · Season Pass (GoD → match3d) · match3d daily login rewards.
- **product-prototypes (7)** — Tile Dozer · Dominoes & Dragons RPG · River Rush · 4X Crypto Conquerors · Barbie "Dream Life Glow" · Zombie Match Lite · Combo Fighter.
- **gmail (9)** — Solsten · AppLovin (deal → sunset) · TYZ Law · Google Ads onboarding · Node Media playables · PlayableX · Mattel licensing · web-distribution negotiation · Adjoe incentivised UA.
- **designart (7)** — designing Sophie · character selection/profile UI · Sophie/Nathan ability VFX · scaling the puzzle pipeline to 1,200 levels · freelancer Ozhan for ZM3D · adaptive difficulty · Progression Philosophy GDD.
- **epics (8)** — Arthur Blake's puzzle editor and bot tooling · backend infra from scratch · Quests backend (Felix + Douglas) · Tutorial Editor backlog · VFX handoff (match3d PR #408) · match3d vision bot for QA · Telegram Domino Delights mini-app · UI sprite optimisation for the CrazyGames WebGL deal.
- **hrfinance (8)** — Deel for contractor payroll · Elliot Mercer termination and backfill · Leapblock art vendor · hiring Douglas · pay-per-prototype build-vs-buy · Samuel Galdámez referral · two Unity hires (Aug 2024) · Helpshift adopt/expand/terminate.

## Traps worth knowing before you seed or write

- **Shared first names.** Three Marcuses (Marcus Bennett, Marcus Lee, a `marcus@` address) plus Oscar Bennett; "Thomas" the persona vs Thomas Baker (Orrick). Verify against emails, never memory.
- **Redacted tokens.** Some actors survive only as `PERSON_####` / `EMPLOYEE_####` tokens. Do not build unique ground truth on an unresolvable token.
- **Similar channels.** Partner and per-title channels cover the same windows for different games.
- **Latest is not automatically right.** In the ML-selected example (`Evals/Docs/Original_Conference_Guidelines_Example_Task.pdf` (the ML-selected example task)) the newest, most senior message is the wrong one.
- **Search is fuzzy; fetch is exact.** Naming an artifact collapses discovery to one fetch.
