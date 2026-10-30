# Prompt Brief — dd-q4-claims-register · prep

> Built 29 Oct 2026 from `00_Assigments.md`, `Working_Files/00_Task_Context.json`, `01_Scenario_Design.md`, `01_Hardness_Manifest.json`, `01_Grounding_Dossier.md`, `01_Universe_Inject.sql`, `01c_Preflight_Report.md`, `03_Error_Async_Config.txt`, `02_Reference_Files_Manifest.md` (absent: no reference files), `01a_Hardening_Report.md` (absent: no revision yet) · Persona view verified: all (see §5a; six scoped load-bearing seeds are check-sql YES, the seventh scoped base file is can-see YES).
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.
> Friction: none configured (`03_Error_Async_Config.txt` carries the empty template). No async wait, no forced error, no alternate-path obligation.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Product (mapped to **Product & Design**, `Evals/references/rules/task_categories.md`) | Product-claim certification for a game's Q4 external pack: a product decision backed by production evidence, not engineering delivery or finance. |
| Persona | Julia Lawson, Product Manager, julia.lawson@harmonygames.co, Product (`00_Task_Context.json`; `Evals/references/persona/roster.json`) | Voice: short first-person declarative notes, 90–220 chars (`slack:C090N54TG79/1758689839.300009`). Remit: owns Domino Delights progression/economy design, the puzzle-layout pipeline and FTUE requirements (`Task_Authoring/references/Persona_Briefs.md:61–63`); owns the claims draft `gdrive:f_5a1b2c3d4e5f60718293a4` and the register workbook `gsheets:f_6b2c3d4e5f60718293a4b5`. Read scope: 158 Slack channels, 304 Gmail threads, 45 owned + 169 shared Drive items (reach census in `01_Scenario_Design.md` §0). |
| Competency | Product Management | The work is the PM's pre-pack certification: locate each claim's production evidence, classify it against a product rule, decide keep/qualify/drop, and write the external register. |
| Task skill | Retrieval | Per-claim retrieval across 11 services: the claim set, the three rules, the per-record production facts, the count surfaces, and the delivery records. |
| Task type | normal · Normal Horizon · hard (cap < 0.70) | Manifest `effective_profile: normal`; 67 unconditional calls over 11 services, 25 per-record calls (`01_Hardness_Manifest.json`; dossier `HARDNESS GATE (normal): PASS`). |

**Remit argument.** Julia authors the Domino Delights economy page (`confluence:page_economy_design`, v3 2025-09-21) and owns progression, level content and live-ops product decisions; she is the person who wrote the claims list and the register workbook. A CEO request to certify the pack's claims before an external send lands squarely inside a PM's prepare/review remit. The work is retrieval first and product judgment second, not finance, incident response or engineering ops.

## 2 · Situation

| Element | Fact | Locator |
|---|---|---|
| Visible symptom | The Q4 claims draft's header says all 13 items are verified live, and the Q4 page repeats that all 13 are live | `gdrive:f_5a1b2c3d4e5f60718293a4`; `confluence:page_q4_product_claims` |
| Who sees it | Julia, who wrote the draft and owns the register and page | `gdrive:f_5a1b2c3d4e5f60718293a4` (owner); `confluence:page_q4_product_claims` (author `user_EMPLOYEE_0005`) |
| Where it shows | The draft's numbered list and its "all 13 items verified live" status line; the page's status paragraph | `gdrive:f_5a1b2c3d4e5f60718293a4`; `confluence:page_q4_product_claims` |
| Request | Leonard asks Julia to check the claims against what is actually live before the Q4 pack goes out | `slack:C1CB3D58E38B/1759248600.000100` |
| Records the persona cannot see | None load-bearing: every scoped record is Julia's own or shared with her; unscoped services are always readable | check-sql block in §5a; `persona_view.py can-see` for `f_c57724584820a26f3bbe54` |

No cause appears in this section: the draft and the page state a conclusion, and the reasons are in §5 only.

## 3 · Investigation → action

**Questions to resolve (no answers here).**

1. Which lines are the claim set, and which near-duplicate list is stale? (`gdrive:f_5a1b2c3d4e5f60718293a4` vs `f_5a1b2c3d4e5f60718293a5`)
2. What is the rule that decides "live", and where did the team agree it? (`slack:C1CB3D58E38B/1759248600.000100` names it by role)
3. Which claims are enabled for all production players, which for a subset, which for none, and which are not player-facing at all?
4. What wording is allowed for each status, and what must a numeric claim state?
5. For every claim whose sources disagree, what are both values and which one governs?
6. Which claims cannot be supported, and where do they get recorded?
7. What are the corrected counts, and where do they go?

**Writes those answers feed.**

| Write | Depends on | Destination |
|---|---|---|
| Register rows (one per claim, all columns) | Q1–Q5 | `gsheets:f_6b2c3d4e5f60718293a4b5`, Register tab |
| Summary counts post | Q3, Q7 | Slack thread `C1CB3D58E38B/1759248600.000100` |
| Corrected claims-page status and dropped list | Q3, Q5 | `confluence:page_q4_product_claims` |
| Follow-up ticket for unsupported claims | Q3, Q6 | new Linear issue linked to `linear:ENG-2375` |

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| D1 register | One row per claim `C01`–`C13`, every seeded column filled: `claim_id`, `claim`, `feature`, `scope`, `status`, `decision`, `qualifier`, `evidence`, `evidence_date`, `conflict`, `owner`, `action` | the existing `Register` tab of `gsheets:f_6b2c3d4e5f60718293a4b5` (headers at SQL L124) | — (file write; shared with `leonard.hayes@harmonygames.co`) | `gsheets_values_update` | R1, R2, R3, R4, R5, R6 |
| D2 summary | Status counts and decision counts only, derived from D1 | reply in the mpim thread `slack:C1CB3D58E38B/1759248600.000100` | Leonard Hayes, Brian Foster (mpim members) | `slack_send_message` | R7 |
| D3 page | Corrected status paragraph plus the list of dropped claims | `confluence:page_q4_product_claims` (seeded "All 13 product claims are live") | readers of the Q4 page | `confluence_update_page` | R5 |
| D4 ticket | One new issue listing the unsupported claims with their evidence, linked to the claims review ticket | new ENG issue; link to `linear:ENG-2375` ("Q4 product claims review") | Leonard Hayes, Brian Foster (ticket assignee/creator context) | `linear_create_issue` | R8 |

**Alternatives a careful run could defend.** (a) Update the `Old register` tab instead of `Register` — rejected by A1 "the tab we already use" plus the Register tab's full 12-column header; recorded in §4b as a rejected, not accepted, reading. (b) Create a new workbook — same rejection (reuse exclusion T14). (c) Comment on the claims review ticket instead of creating a linked issue — accepted only if the comment carries the same claim list and evidence; §4b accepts it as a representational variant of D4 because A1 says "put ... on the claims review ticket". (d) Post the summary as a new top-level message rather than a thread reply — accepted as representational; A1 says "in this thread", so a reply is best supported and a new message in the same mpim is accepted. (e) Use the record id or a human-readable record name in `evidence` — both accepted (`cmt_eng2136_1` / "ENG-2136 comment"); the id form is the solver truth.

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational |
|---|---|---|---|---|---|
| D1 | claim set | Exactly C01–C13, one row each (`gdrive:f_5a1b2c3d4e5f60718293a4`, 13 numbered lines) | "The claims draft you started is the set" (`slack:C1CB3D58E38B/1759248600.000100`) | claim text may be verbatim from the draft or trimmed of the trailing period; `feature` may be the feature name or a short noun phrase | material (13 keys) / representational (wording) |
| D1 | `status` | Per claim: C01 LIVE, C02 LIVE, C03 LIVE, C04 LIVE, C05 LIVE, C06 NOT_LIVE, C07 NOT_LIVE, C08 LIVE, C09 LIVE, C10 TESTING, C11 OUT_OF_SCOPE, C12 LIVE, C13 LIVE (rule on `trello:68daad004f5e6d7a8b9c0d10`; evidence in §5) | — (rule fixes it) | exact vocabulary only: `LIVE` / `TESTING` / `NOT_LIVE` / `OUT_OF_SCOPE`, case-insensitive; no synonym ("SHIPPED", "IN TEST") accepted | material |
| D1 | `decision` | C01 KEEP, C02 KEEP, C03 QUALIFY, C04 KEEP, C05 KEEP, C06 DROP, C07 DROP, C08 KEEP, C09 QUALIFY, C10 QUALIFY, C11 DROP, C12 QUALIFY, C13 QUALIFY (`trello:68d672304f5e6d7a8b9c0d11` fixes the wording; the old register shows KEEP at SQL L125; the prompt carries the keep/qualify/drop vocabulary so the register is decodable) | — | exact vocabulary `KEEP` / `QUALIFY` / `DROP`, case-insensitive | material |
| D1 | `qualifier` | C10 "in testing" + the 10% cohort and 48-hour behaviour; C09 exact count: four coin bundles plus the starter pack; C03 Mon/Wed/Fri not daily; C06 flag off / replaced by the $0.99 starter pack; C07 no build slot; C11 internal tooling; C12 4,755 live, 245 planned; C13 US 11 April 2025 and worldwide 6 May 2025, 14 April unsupported; others "none" (`linear:ENG-2323` comment, `linear:ENG-2371` comment, `linear:ENG-1385` comment, `linear:ENG-2136` comment, `slack:C1CB3D58E38B/1759251600.000400`, `linear:ENG-2370` comment, `confluence:page_domino_gdd`) | — | C10 must contain "in testing" and must not say live/available/launched (H2); C09 must state "four" and the starter pack; numeric values may be `4,755` or `4755`; dates may be ISO or written | material for C09/C10 qualifiers; representational for the rest |
| D1 | `scope` | `player-facing` for C01–C10 and C12–C13; `internal tooling` for C11 (`gmail:julia.lawson@harmonygames.co/1860000000000000001`; `linear:ENG-2370` comment) | — | `internal` / `internal tooling` / `engineering appendix` accepted for C11; `player` / `player-facing` / `external` accepted elsewhere | material (C11) / representational |
| D1 | `evidence` | The decisive record per claim: `cmt_eng2369_1`, `cmt_eng1874_1`, `cmt_eng1385_1`, `cmt_eng2373_1`, `cmt_eng2374_1`, `cmt_eng2136_1`, `dce0ca4cfe773cf514fdda4b59176f73`, `cmt_eng2372_1`, `cmt_eng2371_1`, `cmt_eng2323_1`, `page_live_ops_engine`, `page_domino_gdd`, `page_domino_gdd` (solver `truth.json`) | — | record id, ticket id + "comment", or a clear record name that resolves to the same record (e.g. "ENG-2136 comment", "GDD"); one record per row | representational |
| D1 | `evidence_date` | 2025-09-29T10:00:00Z, 2025-09-29T10:10:00Z, 2025-09-29T10:20:00Z, 2025-09-30T10:30:00Z, 2025-09-29T17:10:00Z, 2025-09-28T16:00:00Z, 2025-09-30T17:00:00Z, 2025-09-28T17:00:00Z, 2025-09-26T13:20:00Z, 2025-09-28T16:20:00Z, 2024-08-15, 2025-09-15, 2025-09-15 (solver `truth.json`; the per-record dates are the comment rows at SQL L139–L149, and the page dates are `confluence:page_live_ops_engine` v1 and `confluence:page_domino_gdd` v4) | — | ISO datetime, ISO date, or the same date written "29 Sep 2025"; the record's own date is material | representational |
| D1 | `conflict` | C06 and C13 only: both sources plus the governing one. C06: the draft says live; the readiness P0 and the 2025-09-28 config comment say not live; the config comment governs. C13: the draft says 14 April; the readiness doc says 23 April; the GDD governs (11 April soft launch / 6 May worldwide). All other rows "none" (`confluence:page_q4_claims_conflict_format`) | "If a claim's sources disagree, write both and say which one governs" (`slack:C1CB3D58E38B/1759248600.000100`) | either order of the two sources; "governs"/"governing" or an equivalent explicit statement; identifiers or names accepted | material (both sources + governing one) / representational |
| D1 | `owner` | C01/C02/C03/C04/C05 Live Ops; C06 Commerce; C07 Product; C08 Monetization; C09 Commerce; C10 Commerce; C11 Platform; C12 Design; C13 Product (solver `truth.json`; H2 "Every retained claim names an owner") | "Every retained claim names an owner" (`trello:68d672304f5e6d7a8b9c0d11`) | team name, or the team plus a named person; case-insensitive | representational |
| D1 | `action` | C01/C02/C04/C05/C08/C09/C10/C12/C13 "none" or "keep"; C03 "none" or "qualify"; C06/C07/C11 "none", "drop", "raise ticket", "follow-up ticket" or "linked to claims review" (solver `truth.json`; `slack:C1CB3D58E38B/1759248600.000100` "put anything we can't support on the claims review ticket") | "put anything we can't support on the claims review ticket" | any of the listed forms; a blank is not accepted for the three dropped claims | representational |
| D2 | counts | Status: LIVE 9, TESTING 1, NOT_LIVE 2, OUT_OF_SCOPE 1. Decisions: KEEP 5, QUALIFY 5, DROP 3 (sum over D1) | "Post the corrected counts in this thread" (`slack:C1CB3D58E38B/1759248600.000100`) | labels may be uppercase or lowercase, "claims" optional; all eight numbers must appear and be correct; a table, a list or one line accepted | material (the eight numbers) / representational (labels) |
| D3 | page status | "Season Pass is not live" plus the dropped claims (C06 Season Pass, C07 Collectibles, C11 live-ops engine) with the reason for each (`confluence:page_q4_product_claims`; solver `truth.json`) | — | "not live" or "is not live"; the three dropped claims named by feature; the "all 13 are live" sentence must go | material (Season Pass not live + the three) / representational |
| D4 | ticket body | The unsupported claims named by feature: Season Pass (flag default-off, no SKU), Collectibles (no build slot), live-ops engine (internal tooling); evidence per claim; linked to the claims review ticket (`linear:ENG-2375`) | "put anything we can't support on the claims review ticket" | title or body; "Season Pass" must appear; the other two may be in the body; the link may be a relation, a URL or an explicit mention | material (Season Pass + both others) / representational |
| All | delivery | D1 in the Register tab; D2 in the mpim thread; D3 on the Q4 page; D4 as a new ENG issue | A1 delegation quotes (`slack:C1CB3D58E38B/1759248600.000100`) | a read-back after each write is good practice, not required | material |

Accepted but not required: a short note to Leonard in the thread beyond the counts; a `status`/`decision` column order change inside the Register tab (headers stay); a drop list on the page expressed as a sentence rather than a list.

## 5 · Discovery map

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 claim set | 13 numbered claims, header "all 13 items verified live with the owning teams as of 29 September" | `gdrive:f_5a1b2c3d4e5f60718293a4` | YES (owner) | met first; overturned by the per-claim evidence and H1 | agents repeat the header as the answer (T1); the trailing unnumbered note is not a claim | Yes — anchor A2 "my Q4 claims draft" |
| F2 stale list | 9-claim September copy, same title family | `gdrive:f_5a1b2c3d4e5f60718293a5` | YES (owner) | same search; rejected by modified time (2025-09-12 vs 2025-09-30) | near-duplicate title (T12) | No |
| F3 register destination | Workbook with `Register` (12-column header) and `Old register` (9 stale rows) tabs | `gsheets:f_6b2c3d4e5f60718293a4b5` (SQL L124–L125) | YES (owner) | met as the write target; the Old tab is the distractor | copying the 9-row old tab (T10), creating a new workbook (T14) | Yes — "the claims register" as the deliverable destination |
| F4 request hub | Leonard's note naming the live-claim standard, the external wording rules, the scope note and the four destinations | `slack:C1CB3D58E38B/1759248600.000100` | YES (mpim member) | met first; the reply amends two claims | reading the parent and not the reply (T8) | Yes — "the thread where Leonard asked" |
| F5 correction | 2025-09-30 18:00 reply: `dd_season_pass` default-off, Collectibles has no build slot, "The rest stands" | `slack:C1CB3D58E38B/1759255200.000200` (SQL L15) | YES (mpim member) | met second, after the parent and the draft | the reply is not returned by the parent search; thread must be opened | No |
| F6 live-claim rule | Enabled for 100% of production players plus an active config row or a completed run/transaction; merged/Done/listing/design doc is not live; a positive subset is Testing; zero enablement is Not live | `trello:68daad004f5e6d7a8b9c0d10` (SQL L173) | YES (unscoped) | met after the request; the Confluence "Release Status Definitions" page is the decoy | the Engineering page is a plausible first hit (T2) | No |
| F7 wording rule | LIVE may say live/available; TESTING must say in testing and must not say live/available/launched; NOT_LIVE removed, not caveated; numeric/date claims state the exact value; every retained claim names an owner | `trello:68d672304f5e6d7a8b9c0d11` (SQL L174) | YES (unscoped) | met after the request; the same-service decoy and the Confluence messaging guide lose on issuer/scope | the decoy card allows "launched" for testing (T3) | No |
| F8 scope and launch rule | Player-facing Domino Delights claims only; internal tooling goes in the engineering appendix; launch-date lines use the soft-launch and worldwide dates in the current GDD, not 14 April | `gmail:julia.lawson@harmonygames.co/1860000000000000001` (SQL L25) | YES (Julia's INBOX) | met after the request; the Q4 narrative page is the decoy | the thread is in her mailbox; the alias `jlawson@` is the export filename (I03) | No |
| F9 Season Pass state | Ticket Done 2025-05-05, PR merged 2025-03-29, but `dd_season_pass` default=false, no SKU, no completed run, out-of-moves screen shows the $0.99 starter pack | `linear:ENG-2136`; `github:harmonygames-Games/GameOfDominoes#1755`; `linear:ENG-2136` comment (SQL L144); `gdocs:f_c57724584820a26f3bbe54` | YES (unscoped; gdoc shared) | ticket and PR met before the readiness doc; the config comment is the later decisive record | Done+merged reads as live (T5); PR state alone is not the rule | No |
| F10 Hero Offers state | Ticket Done, PR merged, `offer_rotation_v2` at a 10% cohort, 48-hour rotation is the enabled behaviour | `linear:ENG-2323`; `github:harmonygames-Games/GameOfDominoes#1838`; `linear:ENG-2323` comment (SQL L145) | YES (unscoped) | merged code met before the cohort comment | a subset read as live (C10) | No |
| F11 Collectibles state | Card in the October list, no ticket, no PR, no build slot; the 2025-09-30 message records the parking decision | `trello:67ec1f6021f4291d45f9c21e`; `slack:C1CB3D58E38B/1759251600.000400` (SQL L14) | YES (unscoped; mpim member) | card met first; the parking message overturns it | a card in a live list reads as shipping (T13) | No |
| F12 launch dates | GDD v4 2025-09-15: US soft launch 11 April 2025, worldwide 6 May 2025, ~4,755 levels across 160 chapters; the readiness doc says "April 23th"; installs from 2023-11-01 | `confluence:page_domino_gdd`; `gdocs:f_c57724584820a26f3bbe54`; `snowflake.ANALYTICS.MARKETING.INSTALL_EVENTS` comment | YES (unscoped; gdoc shared) | readiness date met second; the GDD governs the external value | three disagreeing dates (C13) | No |
| F13 counts | Sold DD SKUs: four coin bundles (`dd_coins_small/medium/large/mega`), `dd_starter_pack`, `dd_remove_ads`; no season-pass SKU; level manifest 4,755 active + 245 planned | `snowflake.ANALYTICS.MONETIZATION.IAP_TRANSACTIONS`; `gsheets:f_7c3d4e5f60718293a4b5c6` (SQL L126); `linear:DES-313` comment (SQL L149) | YES (unscoped; sheet owner) | the April card's "five" is met before the September SKU comment | counting table rows instead of features (T7); copying the April card (T6) | No |
| F14 internal tooling | The live-ops engine is a backend scheduler; the DD production comment says internal admin surface only, no player-facing surface | `confluence:page_live_ops_engine`; `linear:ENG-2370` comment (SQL L148); `gmail:julia.lawson@harmonygames.co/1860000000000000001` | YES (unscoped; INBOX) | the engine's existence reads as live; the scope note excludes it | a true internal system kept in the pack (T4) | No |
| F15 page to correct | "All 13 product claims are live. See the Q4 claims draft for the full list." | `confluence:page_q4_product_claims` (SQL L186) | YES (unscoped) | met as the write target, and it repeats F1's error | none; the page is a write target | Yes — "the claims page" as a deliverable |
| F16 claims review ticket | Issue `ENG-2375` "Q4 product claims review", In Progress, created 2025-09-29 | `linear:ENG-2375` (SQL L136) | YES (unscoped) | met as the link target for D4 | a different review ticket could be confused with the Q4 one | Yes — "the claims review ticket" as a destination |

## 5a · Search-as-persona proof

Natural searches run as `julia_lawson` (pasted verbatim below). For the six seeded facts the base export has no row until the injection overlay applies; the `check-sql` block after the table is their visibility proof and is the load-bearing evidence the gate re-runs.

| Fact (§5) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | gdrive | `claims` | 0 | 0 | — | YES — seeded `f_5a1b2c3d4e5f60718293a4`; check-sql L73 YES |
| F2 | gdrive | `claims` | 0 | 0 | — | YES — seeded `f_5a1b2c3d4e5f60718293a5`; check-sql L77 YES |
| F3 | gsheets | `register` | 1 (unrelated Loc files) | 3 | `f_b82d4d41386fe0a90da5bd` | YES — seeded `f_6b2c3d4e5f60718293a4b5`; check-sql L111/L116 YES |
| F4 | slack | `product claims` | 0 | 0 | — | YES — seeded `C1CB3D58E38B/1759248600.000100`; can-see mpim YES |
| F5 | slack | `product claims` | 0 | 0 | — | YES — seeded reply; check-sql L34/L25 covers the thread; can-see mpim YES |
| F6 | trello | `live-claim standard` | 0 | 0 | — | YES — seeded `68daad004f5e6d7a8b9c0d10`; Trello unscoped |
| F7 | trello | `external wording` | 0 | 0 | — | YES — seeded `68d672304f5e6d7a8b9c0d11`; Trello unscoped |
| F8 | gmail | `player-facing` | 0 | — | — | YES — seeded mailbox thread `julia.lawson@harmonygames.co/1860000000000000001`; check-sql L25 YES |
| F9 | linear | `Season Pass` | 6 | 0 | `harmonygames-Games/GameOfDominoes#1755`-related tickets; `ENG-2136` by lookup | YES — base `ENG-2136`, lookup `/issues/2057`; comment seeded |
| F10 | linear | `Hero Offers` | 6 | 0 | `ENG-2323` by lookup | YES — base `ENG-2323`, lookup `/issues/2262`; comment seeded |
| F11 | trello | `Collectibles` | 6 | 0 | `67ec1f6021f4291d45f9c21e` | YES |
| F12 | confluence | `Game Design Document` | 6 | 0 | `page_domino_gdd` (`/pages/15/title`) | YES |
| F13 | snowflake | bounded read `LIVE_EVENT_PERFORMANCE`, `IAP_TRANSACTIONS` | table rows | 0 (unscoped) | `EVT-0525`…`EVT-0533`; six DD SKUs | YES — unscoped; bounded table read |
| F14 | confluence | `Live-Ops Event Engine` | 1 | 0 | `page_live_ops_engine` (`/pages/6`) | YES |
| F15 | confluence | `Q4 Product Claims` | 0 | 0 | — | YES — seeded `page_q4_product_claims`; Confluence unscoped |
| F16 | linear | `claims review` | 0 | 0 | — | YES — seeded `ENG-2375`; Linear unscoped |

Pasted outputs (decisive):

```
SEARCH gdocs 'Global Launch Readiness' as julia_lawson  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_c57724584820a26f3bbe54", "name": "DD Global Launch Readiness.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "DD Global Launch Readiness"}
```

```
SEARCH confluence 'Game Design Document' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=6 (showing 6)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": ".../confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/15/title", "parent_pointer": "/pages/15", "encoding": "json", "text": "Domino Delights — Game Design Document", "truncated": false}
  {"file": ".../confluence_working.json", "service_file": "confluence_working.json", "pointer": "/pages/16/title", "parent_pointer": "/pages/16", "encoding": "json", "text": "Zombie Match 3D — Game Design Document", "truncated": false}
```

```
SEARCH trello 'Collectibles' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=6 (showing 6)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": ".../trello/data.json", "service_file": "data.json", "pointer": "/cards/672/name", "parent_pointer": "/cards/672", "encoding": "json", "text": "Collectibles (1 month)", "truncated": false}
```

```
SEARCH linear 'Season Pass' as julia_lawson  scope: hg.py search (unscoped: no ACL filter)
visible hits=6 (showing 6)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": ".../linear/data.json", "service_file": "data.json", "pointer": "/issues/575/title", "parent_pointer": "/issues/575", "encoding": "json", "text": "Season Pass - UI and \"cover\" Art", "truncated": false}
```

```
SEARCH gmail 'player-facing' as julia_lawson  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=0 (showing 0)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
note: --no-hidden: containers outside the persona's view were not scanned
```

```
SEARCH slack 'product claims' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
```

```
SEARCH gsheets 'register' as julia_lawson  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=1 (showing 1)  hidden by ACL=3 in 3 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_b82d4d41386fe0a90da5bd", "name": "Loc files.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)"}
```

Pasted visibility proof for the seeded scoped rows (`01_Grounding_Dossier.md` §1.E, re-run at injection):

```
CHECK-SQL as julia_lawson <julia.lawson@harmonygames.co>
[YES LB] L25 gmail.gmail_messages insert julia.lawson@harmonygames.co/<CAFQ4claims9x2m1@mail.gmail.com> - row user_email is the persona
[YES LB] L34 gmail.gmail_messages insert julia.lawson@harmonygames.co/<calendar-5c1a7e93b2d04f61a8e7b8@google.com> - row user_email is the persona
[YES LB] L64 gcal.gcal_events insert evt_5c1a7e93b2d04f61a8e7b8 - event is on the persona's own calendar
[YES LB] L69 gcal.gcal_events insert evt_7d2b8f04c3e15a69b8d1c3 - persona is an attendee and holds a copy
[YES LB] L71 gcal.gcal_events insert evt_8e3c9a15d4f26b7ac9e2d4 - persona is an attendee and holds a copy
[YES LB] L73 gdrive.drive_files insert f_5a1b2c3d4e5f60718293a4 - persona owns the file
[YES LB] L77 gdrive.drive_files insert f_5a1b2c3d4e5f60718293a5 - persona owns the file
[YES LB] L111 gdrive.drive_files insert f_6b2c3d4e5f60718293a4b5 - persona owns the file
[YES LB] L115 gdrive.drive_files insert f_7c3d4e5f60718293a4b5c6 - persona owns the file
[YES LB] L116 gsheets.sheets_spreadsheets insert f_6b2c3d4e5f60718293a4b5 - persona owns the file
[YES LB] L118 gsheets.sheets_spreadsheets insert f_7c3d4e5f60718293a4b5c6 - persona owns the file
verdict: PASS (0 load-bearing rows not visible)
```

```
julia_lawson gdocs f_c57724584820a26f3bbe54: YES
  reason:   file is shared with the persona (shared_with_emails)
  evidence: file=f_c57724584820a26f3bbe54, name=DD Global Launch Readiness.docx, mime=application/vnd.google-apps.document, owner=leonard.hayes@harmonygames.co, shared_with=21, visibility=private, modified=2025-05-05T15:42:14Z
julia_lawson slack C1CB3D58E38B: YES
  reason:   persona EMPLOYEE_0005_SLACK_ID is in members of mpim mpdm-leonard.hayes--julia.lawson--brian.foster-1
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| R1 status per claim | `trello:68daad004f5e6d7a8b9c0d10`; per-claim evidence | scope ("check against what's actually live") | `trello:68daad004f5e6d7a8b9c0d10` · YES · unique for the rule · states the rule, not any claim's status | no — the prompt must point at the standard by role |
| R2 decision and qualifier | `trello:68d672304f5e6d7a8b9c0d11` | constraint ("wording rules product signed off") | `trello:68d672304f5e6d7a8b9c0d11` · YES · unique within the task scope · states the rule | no |
| R3 scope per claim | `gmail:julia.lawson@harmonygames.co/1860000000000000001` | scope ("the scope note fixes which claims are in") | the thread · YES · unique · states the scope, not the classification | no |
| R4 evidence and date | per-claim records in Linear/GitHub | deliverable ("every column filled") | `gsheets:f_6b2c3d4e5f60718293a4b5` headers · YES · unique · names the columns | yes — an assistant filling a register fills the evidence columns |
| R5 conflict statement | `confluence:page_q4_claims_conflict_format`; `slack` A1 | constraint ("if a claim's sources disagree, write both and say which governs") | `slack:C1CB3D58E38B/1759248600.000100` and the format page · YES · unique · states the format | no |
| R6 register destination | `gsheets:f_6b2c3d4e5f60718293a4b5` | deliverable/destination ("the register, in the tab we already use") | A1 · YES · unique · states the destination by role | no |
| R7 counts | A1; D1 | deliverable ("post the corrected counts") | A1 · YES · unique · states the destination and the content kind | yes — counts follow from the register |
| R8 follow-up ticket | `linear:ENG-2375`; A1 | recipient/destination ("anything we can't support on the claims review ticket") | A1 · YES · unique · states the destination by role | no |

**Anchor-name table.**

| Anchor | May be named |
|---|---|
| A1 | Leonard's Q4 claims note; the request thread |
| A2 | my Q4 claims draft; the current claims list |

**Incorporation stance.** The prompt names the anchors, the three rules by role, the four deliverable kinds and the claims review ticket. It names no rule location, no ticket or PR id, no count, no classification and no authority home. Every graded requirement above is reached through an incorporated role pointer, and no record hands over a per-claim answer.

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Assigned freeze | 2025-10-01T00:00:00Z (displayed October 1, 2025 07:00) | `00_Task_Context.json`; `01_Universe_Inject.sql` line 3 | clock |
| Request note | 2025-09-30T16:10:00Z | `slack:C1CB3D58E38B/1759248600.000100` | past |
| Correction reply | 2025-09-30T18:00:00Z | `slack:C1CB3D58E38B/1759255200.000200` | past |
| Scope note | 2025-09-30T14:05:00Z | `gmail:julia.lawson@harmonygames.co/1860000000000000001` | past |
| Claims draft v2 | modified 2025-09-30T15:40:00Z | `gdrive:f_5a1b2c3d4e5f60718293a4` | past |
| Claims draft v1 | 2025-09-12T10:00:00Z | `gdrive:f_5a1b2c3d4e5f60718293a5` | past |
| Live-claim standard card | created 2025-09-29T16:00:00Z | `trello:68daad004f5e6d7a8b9c0d10` | past |
| Q4 claims review | 2025-09-29T15:00:00Z | `gcal:evt_5c1a7e93b2d04f61a8e7b8` | past |
| Board deadline | 14 October 2025 (future) | `gdrive:f_d03044b385b94f24b21ff4` ("Harmony Games BoD Oct 14 2025", created 2025-10-10) | future deadline, allowed |
| Launch dates | US soft launch 11 April 2025; worldwide 6 May 2025 | `confluence:page_domino_gdd` | past |
| Season Pass ticket | Done 2025-05-05; PR merged 2025-03-29 | `linear:ENG-2136`; `github:harmonygames-Games/GameOfDominoes#1755` | past |
| Level manifest | 4,755 live; 245 planned | `gsheets:f_7c3d4e5f60718293a4b5c6` | past |

The prompt uses one absolute deadline (14 October 2025). No seeded record or completed event is after 2025-10-01T00:00:00Z; the board deck is used only as a future deadline and is not described as existing.

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | Yes | Yes | Which rule governs, where the standard/wording/scope documents live, which tab, which of three launch dates | The prompt is vague about where the rules live, never about what is asked; the four destinations are pinned by role |
| Dynamic change | Yes | Yes | The 18:00 correction is met second, after the draft, the parent note and the ticket/PR state | The prompt gives no reason to distrust the draft's summary; the correction is not named |
| Multi-source | Yes | Yes | 11 services; the rule, the per-claim facts, the counts and the page | Three or more systems carry weight; no source is named as an exact artifact |
| Async | No | — | `03_Error_Async_Config.txt` empty | No waited search service named |
| Error recovery | No | — | no forced error | No failure mentioned |
| Access control | No | — | all scoped records are the persona's own or shared | No restriction to describe |

The two load-bearing levers are Ambiguity and Dynamic change; Multi-source is also load-bearing. `gcal`, `trello` and `gmail` (rarely opened) each hold a rule; `snowflake` holds the aggregate evidence. No single discovery decides more than half the weight (three authorities on separate requirement subsets; per-record facts split across Linear and GitHub).

## 9 · Must not appear in the prompt

| Item | Source |
|---|---|
| Tool names, parameters, MCP server names ("linear_create_issue", "gsheets_values_update", "slack_send_message", "confluence_update_page", "the … tool") | `Evals/references/tools/catalog.json`; C14 |
| Opaque ids: `C1CB3D58E38B`, `1759248600.000100`, `1759255200.000200`, `f_5a1b2c3d4e5f60718293a4`, `f_5a1b2c3d4e5f60718293a5`, `f_6b2c3d4e5f60718293a4b5`, `f_7c3d4e5f60718293a4b5c6`, `evt_5c1a7e93b2d04f61a8e7b8`, `68daad004f5e6d7a8b9c0d10`, `68d672304f5e6d7a8b9c0d11`, `68d6735c4f5e6d7a8b9c0d12`, `680222a04f5e6d7a8b9c0d13`, `67ec1f6021f4291d45f9c21e`, `page_q4_product_claims`, `page_q4_claims_conflict_format`, `page_domino_gdd`, `page_live_ops_engine`, `ENG-2136`, `ENG-2323`, `ENG-2375`, `ENG-2357`, `ENG-2369`–`ENG-2374`, `DES-313`, `#1755`, `#1838`, `EVT-0525`–`EVT-0533`, `cmt_eng*` | `01_Universe_Inject.sql`; dossier §1.F |
| The three rule locations (the Trello card, the Gmail thread, the calendar event) and their titles | `01_Scenario_Design.md` §3, §10 "Naturalness constraints" |
| The root cause and every finding: Season Pass not live, flag default-off, no SKU; Collectibles no build slot; live-ops engine internal; Hero Offers 10% cohort; four coin bundles; 4,755 levels; the true launch dates | `01_Grounding_Dossier.md` "Facts for the human"; C9 |
| The counts (9 live, 1 testing, 2 not live, 1 out of scope; 5 keep, 5 qualify, 3 drop) and the number of claims that are wrong | solver `truth.json`; C9 |
| The number of claims (13) as a stated count; "C01"–"C13" | `gdrive:f_5a1b2c3d4e5f60718293a4` discovery |
| The old register tab, the v1 draft and the decoy pages as named artifacts | §5 T10/T12/T2/T3 |
| Markdown, numbered steps, per-column lists or format rules | Prompt Writing §4.2; C15 |
| Reference-file paths and `/app/artifact` | `02_Reference_Files_Manifest.md` (no reference files) |
| Any forced-error or async-wait mention | `03_Error_Async_Config.txt` (none) |

## 10 · Entity traps

`python3 Task_Authoring/tools/entity.py collisions` (verbatim, trimmed to the classes that matter):

```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <marcus@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']
SHARED_LAST_NAMES (5)
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
```

`python3 Task_Authoring/tools/entity.py resolve "Julia Lawson"` and `"Leonard Hayes"` (verbatim, first lines):

```
ENTITY email:julia.lawson@harmonygames.co  name=Julia Lawson  kind=person  emails=['julia.lawson@harmonygames.co']
  persona: julia_lawson - Product Manager / Product
  slack      id=EMPLOYEE_0005_SLACK_ID, name=Julia Lawson, real_name=Julia Lawson, email=julia.lawson@harmonygames.co, is_bot=False, deleted=False
  gmail      mailbox=julia.lawson@harmonygames.co, threads=304 messages=359, thread_filename_alias=['jlawson@harmonygames.co']
  contacts   contact_id=8140f09bf9f1b94cb8ee2dd7, name=Julia Lawson, email=julia.lawson@harmonygames.co, job=Product Manager, is_user=False
ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False
```

| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Julia Lawson | Peter Lawson | different Lawson; no product role | julia.lawson@harmonygames.co vs peter.lawson@harmonygames.co |
| Julia's mailbox | `jlawson@` export alias | same person; alias is the thread filename, not a second identity | `gmail:julia.lawson@harmonygames.co/1860000000000000001`; I03 |
| Leonard Hayes | — | sole Leonard in the task; Co-founder & CEO in Contacts, Creative Director in the roster | leonard.hayes@harmonygames.co |
| Claire Morgan | `Claire` GitHub handle | different person; not a task participant | claire.morgan@harmonygames.co |
| Martin Walsh | Martin Lewis | different person; not a task participant | martin.walsh@harmonygames.co |
| Domino Delights | Game of Dominoes / GoD | same title; internal codename | `confluence:page_domino_gdd` |
| `ENG-####` | `ZOM-###` / `DES-###` | different team series; only ENG/DES in scope | `linear:ENG-2136`, `linear:DES-313` |
| Q4 claims review ticket | other review tickets | the Q4 one is `ENG-2375` "Q4 product claims review", In Progress | `linear:ENG-2375` |

The prompt names Julia's draft, Leonard's note and the claims review ticket in plain words; it carries no first-name-only reference and no id, so it introduces no ambiguity.

## 11 · Pre-submit checklist

- [ ] The prompt reads like Julia typing to her assistant, first person, plain prose, no markdown.
- [ ] It names no tool, no MCP server, no parameter.
- [ ] It states no root cause, no finding and no count.
- [ ] It names only the two anchors, the three rules by role, the four deliverable kinds and the claims review ticket.
- [ ] It pins all four destinations (register tab, thread reply, page, new linked ticket) and the 14 October 2025 deadline.
- [ ] Every sentence is load-bearing; no second task rides along.
- [ ] No id, opaque filename or channel id appears.
- [ ] It does not mention the correction, the old tab, the v1 list or any authority home.
- [ ] It gives a reason to check the draft without naming the summary line.
- [ ] Two careful runs end in the same universe state (all fair variants recorded in §4b).
- [ ] The 20–4,000-word field limit is respected.

## 12 · Blockers and routed defects

No blocking defects. Routed, non-blocking notes:

- **Rubric stage:** the `action` column's solver values are "none" for all 13 rows; the rubric must accept a ticket action for C06/C07/C11 (§4b), otherwise a correct run loses the action samples.
- **Rubric stage:** the summary selectors expect the literal forms "LIVE: 9 claims" and "QUALIFY: 5 claims"; the rubric must accept the eight counts in any labelled order (§4b), and the prompt asks for counts broken out by status and by decision.
- **Fact-check note:** `confluence:page_live_ops_engine` is a mutable page whose current version is dated 2025-11-30; the freeze state is v1 (2025-08-01), which describes a backend scheduler for Zombie Match 3D. C11's decisive record is the seeded `linear:ENG-2370` comment ("internal admin surface only, no player-facing surface") plus the scope note; the brief cites the page only as corroboration.
- **No injection change is requested.** All six seeded scoped records are visible; no fact is routed back to `/create-injection`.

## 13 · Self-review

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings (UGT) | A run could keep C11 as live because the engine exists, or keep C06 because the PR merged — both are defensible readings, so the task would have two acceptance classes | The rule `trello:68daad004f5e6d7a8b9c0d10` excludes merge state and puts a positive subset in Testing; the scope note `gmail:julia.lawson@harmonygames.co/1860000000000000001` excludes internal tooling. Both are incorporated, so the readings are settled by the records, not by taste | PASS |
| Fair readings (UGT) | The register destination could be a new workbook or the Old register tab | A1 says "the tab we already use"; the Register tab carries the 12-column header at SQL L124; the Old register has 9 stale rows at L125. T14/T10 are live distractors, not fair destinations | PASS |
| Clarity | "Post the counts" leaves the summary format open, so two runs could deliver different forms | `slack:C1CB3D58E38B/1759248600.000100` asks only for "the corrected counts in this thread"; §4b accepts any labelled form carrying the eight correct numbers, the numbers are material and the labels are representational. No competing write | PASS |
| Incorporation | The prompt names the standard/wording/scope only by role; a run could never find them | The request note `slack:C1CB3D58E38B/1759248600.000100` names each by the same role words, and each authority is a single record reachable by a natural search (§5a F6–F8) | PASS |
| Truthfulness | "The board on 14 October" could be a phantom event | `gdrive:f_d03044b385b94f24b21ff4` is titled "Harmony Games BoD Oct 14 2025"; it is future-dated (created 2025-10-10) and used only as a future deadline | PASS |
| Feasibility / ACL | A write target could be outside Julia's rights | All four writes are cataloged and Julia owns the sheet, page and mail; the mpim is hers; Linear is unscoped. check-sql PASS and can-see YES | PASS |
| Contrived register | Naming the claims page could be a hint that it is wrong | `confluence:page_q4_product_claims` is a deliverable to correct, not a discovery fact; the prompt says the pack must match reality, and the page's own text ("All 13 product claims are live") is the visible symptom | PASS |

**Unresolved: none.**

The stage-gate block is appended by `stage_gate.py prompt-writing --paste` below.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputs · 04_Prompt_Writing_Brief.md#b9b69bd9ec9f · 00_Assigments.md#f8550b78dd9d · 01_Grounding_Dossier.md#3a92d7fdeb22 · 01_Universe_Inject.sql#bc3abbdfb1d8 · 03_Error_Async_Config.txt#2253e9d33f13 · __context__#fee9c0ab9e8c · __assignment__#3f9540413be0 · __policy__#dc4ab5df3cdd · __gate_policy__#bf8e231eb5d9 · __review__#9b8edbb53b2e · blocking 0 · warnings 0 · checks 23
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; shared source available; record dates and freeze-state evidence checked separately
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#bc3abbdfb1d8, 01_Hardness_Manifest.json#cc9e8fdd561f, 01_Grounding_Dossier.md#3a92d7fdeb22, solver/solver.py#880e65cd119b, 01c_Dispositions.json#7d660f2eb68c, 01c_Preflight_Report.json#52985489dbc4, 00_Assigments.md#f8550b78dd9d, 01_Scenario_Design.md#5aefb2d5ce41, 01_Hardness_Manifest.draft.json#81b53550b53a, 01_Gradable_Surface.json#ed7f0476e12c, __context__#fee9c0ab9e8c, __assignment__#3f9540413be0, __policy__#dc4ab5df3cdd, __gate_policy__#bf8e231eb5d9, __review__#0519e1000740)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#2253e9d33f13, 00_Assigments.md#f8550b78dd9d, 01_Grounding_Dossier.md#3a92d7fdeb22, 01_Universe_Inject.sql#bc3abbdfb1d8, __context__#fee9c0ab9e8c, __assignment__#3f9540413be0, __policy__#dc4ab5df3cdd, __gate_policy__#bf8e231eb5d9, __review__#0519e1000740)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 5/5 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 16/16 items carry a source pointer (min 100%)
[PASS] evidence.dates: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 8/8 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 16 facts proven findable by persona_view search as julia_lawson
[PASS] reach.brief: 10 scoped load-bearing ids YES for julia_lawson
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 6 evidenced counter-readings (of 7 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```



