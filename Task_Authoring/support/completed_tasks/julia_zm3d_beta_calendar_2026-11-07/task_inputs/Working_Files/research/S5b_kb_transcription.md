# S5b KB Transcription — ZM3D live-ops calendar + push notifications

Scope: Zombie Match 3D beta-weeks live-ops calendar (Plague Race, Collect & Win, Season Pass, Infinite HP Boss / Boss Arena, Endless, Zombie Lane, Daily Login, Quests) and player push notifications. Persona Julia Lawson (PM). Services: Slack #zombie-design C090N54TG79 + DMs, Linear ZOM, GitHub match3d / match3d-backend, Confluence page_liveops_calendar / page_season_pass_spec / page_zm3d_gdd, Trello ZM ROADMAP 6851a6569f3bf818760632ab, Google Sheets/Docs/Drive, GCal, Gmail, Snowflake LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE.

## 1. coherence_hazards.json

Six categories in the file: `temporal` (8), `semantic_category` (4), `cross_service_referential` (9), `quantitative` (8), `state_lifecycle` (12), `identifier_format` (18). Format: id · service · title (count/denominator) · example ids.

### temporal
- T01 · github · Timeline `reviewed` events have null created_at + empty actor (2,116/12,435) · ex `harmonygames-Games/GameOfDominoes#1#ev_2` — for match3d PR review timing use `github_reviews.submitted_at`, never the timeline.
- T02 · gmail · Thread files whose messages are not in chronological order (2,685/88,726) · ex `blake@harmonygames.co_1761203751812903443.json`.
- T03 · gmail · Messages with missing/unparseable date (4) · ex `douglas@harmonygames.co_1826866441814158`.
- T04 · linear+github · Issue completed >1 day before the first PR that names it merged (12/441) · ex `ART-538` + `GoD#568`; guidance: define whether Linear completion or PR merge is authoritative for "shipped" (applies to ZOM-### + match3d).
- T05 · linear · `updated_at` earlier than `completed_at` (1) · ex `ENG-127`.
- T06 · trello · Card has an action later than its `dateLastActivity` (10) · ex `6408e6b909dd38b8358eebd8` — ZM ROADMAP card activity order is not monotonic.
- T07 · none in scope (metadata/storyline YAML artifact ids, not this area).
- T08 · confluence · Edits/comments dated >30d after the author's last activity anywhere else (0) · guidance: Confluence authorship on `page_liveops_calendar` / `page_season_pass_spec` is not proof someone was active; check activity.json.

### semantic_category
- S01 · github+linear · match3d PRs citing `ENG-####` (Domino Delights keys) instead of `ZOM-###` (5/428) · ex `match3d#327`→`ENG-414`, `#330`→`ENG-420`, `#375`→`ENG-450`, `#379`→`ENG-470`, `#382`→`ENG-472`; never join ENG-n to ZOM-n on the number alone.
- S02 · linear · Issue whose parent is another team's epic (129) · ex `ART-117`, `ART-198`, `ART-206`; ZOM-team cohorts must state whether ART/DES children of EPI/ENG parents count.
- S03 · linear · 243-label vocabulary mixes sprint names, release codenames, platforms, categories · ex `Bug`, `Improvement`, `Baklava Hot Fix`, `Main Game` — label-only live-ops/Plague-Race filters are unreliable.
- S04 · github · GitHub display names that disagree with the person (3) · ex `PERSON_2314_GITHUB_USERNAME` shows "Ryan" — match3d PR authors by login/person id, not display name.

### cross_service_referential
- R01 · slack+linear · Slack messages citing Linear keys that do not exist (39/1,203 keys) · ex `ART-303` (slack:C05UQKDLGAU/1698741596.230299), `ENG-247` (slack:C04V7N09LE7/1696288738.358489) — do not chain a ZOM story through a #zombie-design mention without checking the issue exists.
- R02 · slack+github · Slack PR links not in the GitHub export (0/335 URL) — clean.
- R03 · gmail+github · GitHub notification mails with repo name redacted `[[SOURCE_ORG_0001]-Games/...` (201/4,036) · ex `gmail:calvin.price@harmonygames.co/<[SOURCE_ORG_0001]-Games/GameOfDominoes/pull/3@github.com>` — search repo name, not org.
- R04 · slack+drive · Slack links to Docs/Sheets/Slides carry Google-native ids, not `f_` ids (2,096; no examples listed) — resolve a linked calendar/spec by URL id, not by Drive name.
- R05 · github · Branch `head_sha` values are pre-rewrite SHAs, present only as `commit_map.old_sha` (0/2,011) — no bad rows, but do not join head_sha to commits.
- R06 · github+slack · GitHub-app Slack mirrors with no matching GitHub comment text (763) · ex `C050WGU41HR/1700593042.271909` → `GoD#132` — a #zombie-prs mirror paraphrases the PR; seed both sides together.
- R07 · github+slack · GitHub PR comments inside a mirrored repo's window with no Slack mirror copy (71; `match3d` is inside the window) · ex `GoD#1048#c_1` — mirror coverage is not 100%, so "every review comment is in Slack" is false.
- R08 · gmail+gcal · Dated invite/update/cancel mails with no GCal instance of same summary ±1 day (424/3,284) · ex `gmail:robert@harmonygames.co/<calendar-1e5e32d8-d738-43a2-94d3-8b7ec8c8ccb2@google.com>` — a "live-ops review" invite mail does not prove a GCal row.
- R09 · gmail+linear · Linear auto-close ("changed the status to Canceled") mails whose issue is not Canceled (0/24) — clean.

### quantitative
- Q01 · slack · Thread parent `reply_count` != replies in export (0/13,684 parents with counters) — counters consistent today; a seeded parent must keep them consistent.
- Q02 · slack · `reply_users_count` != distinct repliers (7) · ex `C05H8KVNU67/1712450268.112809` claimed 4 actual 5; `C05V5FNLB9V/1713565644.651319` claimed 5 actual 4.
- Q03 · slack · `latest_reply` != newest reply ts (0) — clean.
- Q04 · slack · Raw-shaped thread parents with no `reply_count`/`latest_reply` at all (1,526) — check the shape before trusting any counter (same rows as I01).
- Q05 · none in scope (MONTHLY_BURN vs finance ledger).
- Q09 · snowflake · Mirrored warehouse tables checked row-by-row, all agree (0 diffs) — list is AD_SPEND_DAILY/AD_SPEND/UA_SPEND_UNIFIED_V2, REVENUE_DAILY/_V2, DAU/DAILY_METRICS_AGG, HEADCOUNT/PAYROLL_ROSTER, APP_STORE_REVIEWS/STORE_REVIEWS, IAP/STORE_TRANSACTIONS; `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE` is not among them, but guidance holds: write a seeded row to every mirror and update count-quoting table comments.
- Q10 · gmail · Same RFC message stored in 2+ mailboxes with different content (686/2,837 pairs) · ex `EMPLOYEE_0011_EMAIL 00000000.json` — cross-mailbox copies of a player-comms mail may disagree; pick one mailbox as authority.
- Q11 · gcal · Calendar copies of one instance (same `ical_uid` + start) that disagree (857/1,666) · ex `evt_00009bfb80dabb15aa5bb5` vs `evt_05b5867b317edbb104b624` — per-attendee copies of one live-ops review can differ by field.

### state_lifecycle
- L01 · linear+github · Issue in state PR but a referencing PR merged (0/441) — clean.
- L02 · linear+github · Issue Canceled but a referencing PR merged (2/441) · ex `ENG-1730` / `GoD#1324`, `ENG-903` / `GoD#624` — no ZOM row today; rule still applies to "canceled but shipped" cards.
- L03 · linear+github · Issue Todo/Backlog but a referencing PR merged (3/441) · ex `ZOM-292` / `match3d#267`, `ZOM-387` / `match3d#319`, `ENG-1259`/`GoD#1071` — the direct "done across services, ticket still open" precedent.
- L04 · linear+github · Issue Done but every referencing PR unmerged (5/441) · ex `ENG-1502`/`GoD#1173`, `ART-550`/`GoD#582` — the mirror-image trap (Linear Done, nothing on prod).
- L05 · linear · `completed_at` set but state not Done (12/3,852) · ex `ART-424`, `ART-425`, `ART-426`, `ART-444`, `ART-513`.
- L06 · linear · Parent Done while child open (20/3,852) · ex `ART-384`, `ART-385`, `ART-541`, `ART-585`, `ART-655` — an epic-level "done" (e.g. Season Pass) can hide open ZOM children.
- L07 · linear · State `PR` (awaiting merge) (0) — clean.
- L08 · linear · Open issues assigned to quiet/departed people at the clock (13/248) · ex `ART-425 -> rachel@harmonygames.co (quiet_since_2024-09)` — an open ZOM assignee can be a dead end.
- L09 · github · Merged PRs with no review at all (574/2,498) · ex `GoD#1017`, `GoD#1028` — match3d merges may have no review to cite.
- L10 · github · Merged PRs whose only reviews are bot or COMMENTED, no human APPROVED (87) · ex `GoD#1141`, `GoD#1250` — "approved" on a match3d PR may mean CodeRabbit only.
- L11 · trello · Open card in a closed (archived) list (10) · ex `641f7190800a4c4ac7031494`, `65eb4ec525346c8070ca63e3` — ZM ROADMAP card "closed" is list-level, not card-level.
- L12 · trello · Card in Done list with incomplete checklist items (4) · ex `64064483b78c120c74aa10b7`, `640645191c08b2af2388e274`, `6408e6b909dd38b8358eebd8` — a Done-list card can still have unchecked items.

### identifier_format
- I01 · slack · Raw-shaped Slack records (no `id`, no `reply_count`; blocks + client_msg_id + user_profile) (81,036/687,230) · ex `C04RSEB8K0W/1681324370.119529` — counters and ids simply do not exist on these.
- I02 · slack · Message `id` != `sha256(channel|ts)[:32]` (14) · ex `C0B1220E9042/1745851012.192410`, `C127CE64C71B/1753437509.093580` — never recompute a Slack message id.
- I03 · gmail · Thread file name uses a mailbox alias different from `user_email` (46,532/88,726) · ex `leonard@harmonygames.co -> leonard.hayes@harmonygames.co` (15,339), `calvin@ -> calvin.price@` (8,142).
- I04 · gmail · Mixed RFC-2822 (72,512) vs ISO-Z (22,648) dates, 4 missing · no example ids.
- I05 · gmail · Mailboxes whose owner is a token (6) · ex `EMPLOYEE_0011_EMAIL`, `EMPLOYEE_0020_EMAIL`, `SVC_0009_EMAIL`.
- I06 · gmail · `Re:`/`Fwd:` subjects without `in_reply_to`/`references` (341) — do not build a reply chain from the subject line.
- I07 · github · Bot comment `author_login` differs from the paired timeline `actor_login` (595) · ex `GoD#1001#c_1` — CodeRabbit `PERSON_6026` vs `SVC_0321`, `linear[bot]` `PERSON_6028` vs `SVC_0323`; "comments by X" differs per table, and the Linear bot comment on a match3d PR carries the other actor id.
- I08 · github+slack · GitHub logins are tokens while the Slack GitHub-app mirror shows real logins (19) · ex `EMPLOYEE_0025_GITHUB_USERNAME -> arthur.blake`, `PERSON_0396 -> MarcusBennett`.
- I09 · slack · GitHub-app mirror copies with the org redacted `[SOURCE_ORG_0001]-Games/...` (134) · no example ids — search `match3d`, not the org string.
- I10 · linear · Linear user ids that are not `usr_<16hex>` (280) · ex `usr_Victor Barnes` (space), `usr_Robert`, `usr_EMPLOYEE_0024` (issues `ART-100`, `ART-101`, `ART-102`) — quote ids exactly, never derive.
- I11 · gcal · Same calendar holds two rows for one meeting start (recurring master + standalone) (762) · ex `martin.walsh@harmonygames.co` / `a58a8bb029ac801cd448630ad52461e3@hg4` / `2024-11-18T17:30:00Z`.
- I12 · gcal · `ical_uid` + start shared by *different* meetings (summary differs) (137) · ex `evt_007a50e82abbc685a1c59e` vs `evt_042d20f97a89130ca7f8e8`, `evt_05025c50ab8af2bdd9e2d0`.
- I13 · gcal · Instances with a copy on a calendar whose owner is not an attendee (44) · ex `evt_00526092fd842b17a6e433` (owners `julia.lawson@`, `leonard.hayes@`), `evt_00009bfb80dabb15aa5bb5`.
- I14 · drive · `owner_email` is not an email (`Resource: -6481757892984311338`) (2,530/53,866) · ex `d_002fd454dc96e2926abd76`, `d_00314aa906f107d6da533a` — do not filter Drive by owner email string.
- I15 · drive+docs+sheets · Drive name keeps the source extension while the Docs/Sheets title drops it (951) · ex `f_00da0af9039fdf198986af` = "Creative Concepts" vs "Creative Concepts.docx"; `f_00117462881159eceee63e` = "Company Stand Up (...)" vs `.html`.
- I16 · trello · Action ids whose embedded timestamp != action date (49; Welcome Board template rows) · ex `535af5816ca07f261e8cd441` — do not date a Trello action from the id prefix.
- I17 · trello · Trello list names and members redacted to tokens (6) · ex `[PERSON_NAME_35449]`, `[PERSON_NAME_56566] (Early November)`, `[PERSON_NAME_49938] (November 27th)` — a list name can be a person token plus a date.
- I18 · slack · In-place retractions written as `~strikethrough~` inside the same message (147) · ex `slack:C04UEQVDVB7:1683248435.748409`, `slack:C04UEQVDVB7:1698436632.335299` — a live-ops date claim can be withdrawn inside its own message; the struck text is not the answer.

## 2. trap_catalog.json

25 entries in 8 kinds (clock `2025-10-01T07:00:00Z`). Mapped to the seven requested precedents; format: id · kind · one line · example ids.

### done across services — merged/closed but a piece missing on prod/deploy
- C02 · superseded_claims · Thread parent states a resolution ("done", "fixed", "deployed") and another person replies it still fails (20) · ex `slack:C04UTBZL6AX:1687447802.692389` (reply 1687455881.102919), and the mpdm 1750275343.826629 "Deployment done…" → "still not working" case — the strongest natural precedent for "Linear Done + PR merged, but the prod piece is absent".
- B04 · bot_noise · Jenkins `#builds` rows whose `started`/`unknown` statuses read like outcomes (24,802 job + 8,217 build-script messages; `unknown` 1,646) · ex `C05433XK267/1690645565.203229`, `C05433XK267/1690647273.330659` — a green build message is not a deploy of the missing piece.

### correction somewhere else
- C01 · superseded_claims · Thread replies that correct/retract the parent, marker phrases, 100 strong markers since 2024 (from 1,352 hits) · ex `slack:C04UEQVDVB7:1733190395.838719` → reply `1733190455.167619` ("my bad"); `slack:C04UTBZL6AX:1708305311.860619` → `1708308395.088839` — the correction sits in a reply most runs never open.
- C03 · superseded_claims · In-place `~strikethrough~` retractions (147) · ex `slack:C04UEQVDVB7:1683248435.748409`, `slack:C04UM32UWKD:1685042781.204509`, `slack:C04UTBZL6AX:1696487724.527469` — withdrawn claim stands in the same message.
- C02 · also the "conclusion overturned in a reply" shape (see above).

### alias / different names
- P01 · lookalike_people · Shared first names across people and tokens (4 groups: claire / marcus / martin / thomas) · ex `Claire Morgan <claire.morgan@…> [persona]` vs `Claire <github:PERSON_2360>`; `Marcus Bennett` vs `Marcus Lee` vs `Marcus <trello:c48a210d5c5a4b59231c6873>`.
- P02 · lookalike_people · Shared surname groups (1 group: Bennett) · `Marcus Bennett <marcus.bennett@…>` vs `Oscar Bennett <oscar.bennett@…>`.
- P04 · lookalike_people · Tokenised GitHub contributors whose real login appears only in the Slack GitHub-app mirror (19) · `EMPLOYEE_0025_GITHUB_USERNAME -> arthur.blake` (1,567), `PERSON_0396 -> MarcusBennett` (81), `PERSON_5877 -> owen.baker` (717) — authorship needs the mirror join, and the mirror re-redacts sometimes (`[PERSON_NAME_0212]`, 32).
- X02 · redaction · Same token means different things per service and numbers do not align · `EMPLOYEE_0032` = Slack user + Gmail mailbox + Josh Dempsey in `PAYROLL_ROSTER` + a GitHub login; Brian is `EMPLOYEE_0026` in Slack but `PERSON_0180` in GitHub — join only on exact email/Slack id.
- K02 · lookalike_containers · App-name lineage: `Puzzles vs Zombies` / `Match 3D` / `Zombie Game 3D` → Zombie Match 3D (TestFlight "Puzzles vs Zombies" 2025-03..07) · ex `testflight 'Puzzles vs Zombies' 2025-03..07`, `gmail distribution 'GoD iOS' 2023-04` — name-based counts across eras undercount ZM3D.
- N01 · ticket_series_collision · `ENG-n` and `ZOM-n` both exist for 521 numbers (every ZOM number has an unrelated ENG twin) · ex `ENG-131` "New Algo Implementation" vs `ZOM-131` "Upgrade level editor to nest the color variants", `ENG-184` vs `ZOM-184` — a bare number lands on the wrong team's ticket.
- X04 · redaction · Company name masked unevenly across copies of the same mail ("Harmony Games" vs "[SOURCE_ORG_0001]") (361) · ex `EMPLOYEE_0011_EMAIL 00000008.json` vs `arthur.blake@…blake@…_1763472856296482546.json` — exact-quote criteria break by mailbox copy.

### items outside an obvious filter
- K01 · lookalike_containers · Canvas pseudo-channels `FC:<file id>:<title>` (32) and per-title channel families (`god-*` vs `zombie-*`), 90 archived channels (28) · ex `C3DD99314033 FC:F09FNQM8EBZ:Collect&Win issues - zm - ios 1730`, `C127CE64C71B FC:F09716QNHFT:Endless Horde Issues and Improvemen`, `C4208B207A1A FC:F0A2FSC416J:EconomyChanges Bugs` — searching "Collect & Win issues" returns a canvas channel, and `ios 1730` is a build number, not a date.
- N03 · ticket_series_collision · Branch keys without a hyphen (`ENG1229QuestCollectChapterRewards`) and redacted owners (`[PERSON_NAME_0067]/ENG-1622-1`) · ex `GoD#10` branch `[PERSON_NAME_0099]/HAR-67`, `GoD#1001` `[PERSON_NAME_0067]/ENG-1301` — regex `ENG-\d+` misses them, and `links_json` is empty on every issue.
- D05 · stale_vs_current · Drive title families with version markers (v1/v2/final/draft/copy of/updated, 32) · ex "Copy of Untitled document.docx" / "Untitled document(1..3).docx" (`f_4a304a4e4c0bd1e12ed24b`, `f_b043f93d1a3e458e59e92f`) — "final" is not the latest and latest is not authoritative.
- B01 · bot_noise · Slack bot volume by integration (72,497 rows; jenkins 24,802, qa_monkey_bot 14,690, github_app 11,653, jenkins_buildscript 8,217, standup_bot 5,412, linear_app 2,089, google_drive_app 722) — any channel-wide read that does not exclude bots is mostly noise.
- B02 · bot_noise · Gmail automated senders are tokens (63,452; `svc_0107` 44,109 Firebase, `svc_4131` 5,555 TestFlight, `svc_0251` 1,278 Linear, `svc_0248` 966 GitHub, `svc_0239`/Crashlytics 3,351 `svc_2398`) — sender-name filters fail; decode by subject pattern.
- B03 · bot_noise · GitHub bots: CodeRabbit `PERSON_6026` (266 PR comments, 833 review comments, 182 reviews) and `linear[bot]` (328 PR comments) · ex `GoD#1867#c_1`, `GoD#1000#c_1` — bot reviews look like approvals on match3d PRs.
- B05 · bot_noise · Helpshift via Zapier in `#issuefeed` with empty payloads ("author: ; Message:") (1,046) · ex `C083AEP6NBA/1732676141.928539` — Slack "issue" counts ≠ Helpshift mails.
- D03 · near_duplicate_documents · Slide decks sharing a title family (Weekly Update, publisher pitch decks, BoD decks; 5 groups) · ex "Netflix-Harmony Games - Jan 2025 v2", "Copy of Harmony Games BoD Jul 17 2024" — eleven 29-page publisher decks look alike.

### completion elsewhere
- D06 · stale_vs_current · Confluence pages with version history and edit messages, old bodies readable via `get_page_version`/diff (24 pages) · ex `page_eng_home` (2 versions), `page_arch_overview` (3, messages "Imported", "Reviewed against the stack/ports/counts pass…") — the rule that governs a live-ops date can be an older version of `page_liveops_calendar` / `page_season_pass_spec`.
- D01 · near_duplicate_documents · Drive titles that normalise to the same name under different owners (129 of 344 groups) · ex "untitled spreadsheet" owned by `Resource: -6481757892984311338`, `claire.morgan@…`, `julia.lawson@…` with different `f_` ids — the copy the persona can see may be the only readable one.
- D02 · near_duplicate_documents · Docs with identical bodies under different ids/owners (12) · ex `f_2887e38206f165c0712450` / `f_b6d910d181eb5824301e22` ("ES"), `f_3c75e7f2b847efc55a5288` / `f_abcc0419fca0ed2b2ced9d`.
- D04 · near_duplicate_documents · Spreadsheets with normalised-duplicate titles (P&L, investor lists, KPI exports; 26) · ex "Copy of DDA Simulator" vs "DDA Simulator" (`f_045a7dfe82031d129f64aa`, `f_8bdb3c6c7742bb481169a0`, owner `vincent.parker@…`).
- K01 · also the "work tracked in a sibling container" shape (see filter section).

### timezone / boundary dates
- none in scope: no trap id in this file covers timezones or boundary dates. The catalogue's 25 entries are people / number series / documents / claims / bots / redaction / containers. Clock is `2025-10-01T07:00:00Z`; take date formats and boundary rules from `conventions.json` (section 5).

### rule hidden in older records
- D06 · oldest-version rule (above) — effective-date regime: the page version in force at the record's date decides.
- D05 · supersession decided by an incorporated rule (latest closed month, owner), never by the "final"/"v2" label.
- X01 · redaction · Token inventory that hides older names (`[PERSON_NAME_n]` 46,422 in human Slack, `[SOURCE_ORG_n]` 338, `[EMAIL_n]` 742, `[IDENTIFIER_n]` 1,440) — searching "Harmony Games" misses `[SOURCE_ORG_0001]` copies, so an older-record search silently under-returns.

## 3. cohorts.json

175 cohorts. In-scope rows only; format: id · selection rule · count · hazards_inside.

### Linear (team ZOM)
- LIN-S02 · `team_id=team_ZOM AND state_id='Done'` · 427 · issue completed >1 day before first referencing PR merged (1: `ZOM-450`); sample `ZOM-10`, `ZOM-100`, `ZOM-101`.
- LIN-S06 · `team_ZOM AND state='Todo'` · 45 · parent Done while child open (3: `ZOM-293`, `ZOM-453`, `ZOM-458`); issue Todo/Backlog but referencing PR merged (2: `ZOM-292`, `ZOM-387`); sample `ZOM-118`, `ZOM-292`, `ZOM-293`.
- LIN-OPEN-ZOM · `team_ZOM AND state NOT IN (Done, Canceled, Duplicate)` · 99 · parent Done while child open (5: `ZOM-16`, `ZOM-293`, `ZOM-317`, `ZOM-453`, `ZOM-458`); Todo but PR merged (2: `ZOM-292`, `ZOM-387`); sample `ZOM-104`, `ZOM-118`, `ZOM-119`.
- LIN-L02 · `team_ZOM AND 'Bug' IN labels_json` · 171 · parent Done while child open (1: `ZOM-458`); sample `ZOM-106`, `ZOM-107`, `ZOM-108`.
- LIN-L04 · `team_ZOM AND 'Improvement' IN labels_json` · 137 · parent Done/child open (2: `ZOM-16`, `ZOM-317`); Todo but PR merged (1: `ZOM-292`); completed before PR (1: `ZOM-450`).
- LIN-L22 · `team_ZOM AND 'VFX' IN labels_json` · 49 · parent Done while child open (1: `ZOM-16`); sample `ZOM-11`, `ZOM-112`, `ZOM-113`.
- LIN-CQ11 · `team_ZOM AND created_at in 2025-Q2` · 317 · parent Done/child open (3: `ZOM-16`, `ZOM-293`, `ZOM-317`); Todo but PR merged (1: `ZOM-292`).
- LIN-CQ12 · `team_ZOM AND created_at in 2025-Q3` · 236 · parent Done/child open (2: `ZOM-453`, `ZOM-458`); Todo but PR merged (1: `ZOM-387`); completed before PR (1: `ZOM-450`); sample `ZOM-327`…`ZOM-336`.
- LIN-DQ12 · `team_ZOM AND state Done AND completed_at in 2025-Q2` · 199 · no hazards inside.
- LIN-DQ13 · `team_ZOM AND state Done AND completed_at in 2025-Q3` · 228 · completed >1 day before referencing PR merged (1: `ZOM-450`).
- LIN-UPD · `team IN (ENG,ZOM) AND updated_at >= 2025-08-13` (Hardness_Mastery §2.5 pattern 1) · 141 · no hazards inside; sample `ENG-2258`, `ZOM-112`, `ZOM-127`.
- LIN-ATT · `attachments.issue_identifier = issue AND created_at >= 2025-01-01` (ENG/ZOM) · 267 · parent Done/child open (1: `ENG-2289`); Todo but PR merged (1: `ZOM-292`); Done but all PRs unmerged (1: `ENG-2131`).
- Note: all LIN cohorts are `bulk` (list returns state/labels/assignee/parent/relations/description but never comments); only a seeded Linear comment costs an honest per-record call. Every LIN cohort lists 0 comments in the base.

### GitHub (match3d)
- GH-Q09 · `repo=match3d AND created_at in 2025-Q1` · 93 · merged with no review at all (85, e.g. `match3d#1`, `#10`, `#13`, `#14`, `#15`).
- GH-Q10 · `repo=match3d AND created_at in 2025-Q2` · 164 · no review at all (153); no human APPROVED, bot/comment-only (5: `#188`, `#244`, `#245`, `#247`, `#253`).
- GH-Q11 · `repo=match3d AND created_at in 2025-Q3` · 220 · no review (94: `#260`, `#264`, `#268`, `#272`…); bot/comment-only (49: `#259`, `#262`, `#263`, `#266`…); no Slack mirror for a GitHub comment (8: `#262`, `#291`, `#298`, `#308`, `#316`, `#319`, `#325`, `#332`); Todo but PR merged (2: `#267`, `#319`); completed >1 day before PR (4: `#327`, `#330`, `#375`).
- GH-KEYED · regex `(ENG|ZOM|ART|DES|EPI)-?\d+` in title, head_ref or body · 428 · no review (31); bot-only (11, incl. `match3d#244`, `#263`, `#271`, `#282`, `#319`); no Slack mirror (6, incl. `match3d#319`); Todo-but-merged (3: `GoD#1071`, `match3d#267`, `#319`); Done-but-unmerged (5: `GoD#1173`, `#1264`, `#1450`, `#1681`, `#582`); Canceled-but-merged (2: `GoD#1324`, `#624`); completed-before-PR (10, incl. `match3d#327`, `#330`, `#375`).
- GH-CRONLY · `merged AND every review author = PERSON_6026 (CodeRabbit)` · 50 · bot-only/no human APPROVED (all 50, incl. `match3d#244`, `#245`, `#247`, `#253`, `#259`, `#262`, `#263`, `#269`); no Slack mirror (5: `#262`, `#298`, `#308`, `#316`, `#319`); Todo-but-merged (1: `#319`). Surface note: match3d is a mirrored repo, so comments/reviews come from the `#zombie-prs` Slack mirror, not per-PR GitHub reads; timeline/files/commits are per-PR.

### Slack (ZM3D channels + persona DM)
- SL-T19 · `channel=C090N54TG79 (#zombie-design) AND thread_ts=ts AND >=1 reply AND not bot` · 152 · no hazards inside; sample `C090N54TG79/1751611091.140269`, `/1751611125.186979`.
- SL-T31 · `channel=CA2DFEA73CBC (FC:F09DYTUMW3S:Season Pass Issues - ZM) AND thread_ts=ts AND >=1 reply AND not bot` · 63 · none; sample `CA2DFEA73CBC/1756833540.001779`, `/1756833690.512809`.
- SL-T28 · `channel=C08R6BF4ENN (zombie-ops)` · 71 · none; sample `C08R6BF4ENN/1746563616.864339`.
- SL-T11 · `channel=C08R27X0EAH (zombie-bugs)` · 283 · none; sample `C08R27X0EAH/1747069723.464709`.
- SL-T14 · `channel=C08R8CHB0QL (zombie-art)` · 220 · none; sample `C08R8CHB0QL/1746550005.096679`.
- SL-T15 · `mpdm julia.lawson--brian.foster--vincent.parker`, human roots with replies · 192 · none (persona DM cohort).
- All SL cohorts are `bulk`-sweepable and honest-cost 0 — useful only as the A14 behavioural trap (a fact in a reply most runs never open).

### Snowflake
- SF-LEP · `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE`, selection `GROUP BY STATUS` · 529 · hazard "`L14`: completed rows during Slack-reported outages" — i.e. the table records COMPLETED runs for events that Slack says were pulled; the seeded row must be reconciled with the Slack retraction, not read as proof of a clean run. Bulk: one SQL query returns all rows; per-record surface is `row columns` + `FAILURE_NOTE`/`NOTES` text.

### Trello
- TR-B-0632ab · `idBoard=6851a6569f3bf818760632ab (ZM ROADMAP) AND closed=false` · 69 · no hazards inside; sample card ids `6851a6fde24742cce9ad7b1c`, `6851a713aa4e4da6cb2c2227`, `6851a718d6f9034235f9b7a3`; surfaces desc/comments/checklists/card actions, bulk via `trello_get_board_actions` (comment filter) and `trello_get_checklists_on_board`, honest 0.2–0.5 per record.

## 4. integrations.json

23 rows. Only the rows that touch this area; each entry gives the id, what it produces, base volume/window, and the companion rule (what else must exist).

### Slack message / thread reply (counters)
- No integration *creates* a human Slack message; counters are base-record properties (`Q01`–`Q04`, `I01`). A seeded thread parent needs `reply_count`, `reply_users_count` and `latest_reply` consistent with its replies (base is consistent: 0/13,684 mismatches on reply_count, 0 on latest_reply, 7 counter-vs-replier mismatches). Thread parents in the raw shape (`I01`, 81,036 records) carry **no** counter fields at all — do not add them to a raw-shaped row, and do not read a counter off one.
- Bot-produced parents use the integration shapes below; a reply seeded under a GitHub mirror parent must thread under that PR's "Pull request opened" parent (INT-01), not float top-level.

### Linear issue + comment (bot posts?)
- INT-03 · linear → github · `linear[bot]` comment on PRs whose title/branch names a Linear key · 328 comments on 327 PRs = 76.2% of the 428 keyed PRs · author `PERSON_6028_GITHUB_USERNAME` (type Organization) while the timeline event actor is `SVC_0323_GITHUB_USERNAME`; body is `<details><summary><a href="https://linear.app/harmonygames-games/issue/<KEY>/<slug>"><KEY> <title></a></summary>…`; Slack mirror text is "Comment on pull request by linear[bot]" + `<https://linear.app/…|KEY title>`. Companion rule: a seeded PR naming a key in a covered era normally carries the bot comment **plus** its `commented` timeline event with actor SVC_0323 **plus** the Slack mirror if the repo is mirrored; Linear `links_json` stays empty on every issue.
- INT-04 · linear → slack · Linear Slack app: personal DM feed `D05MBMJDAKV` (1,381) and team channels `#god-bugs` (272), `#zombie-match3d` (215), `#company-playtest` (88), `#zombie-bugs` (26), `#game-design` (25), `#analytics` (19), `#zombie-art` (8), `D04UGG61DUM` (4); 2,089 messages 2023-08-11..2025-09-30, bot user `SLACK_BOT_0007_SLACK_ID`; attachment fallback `[PERSON_NAME_n] - changed status to Done for ENG-291 <title>`, action mix `changed status to Done` 562 / `[no preview available]` 192 / `changed status to Canceled` 41. Companion rule: not every transition is posted (the DM feed is one subscriber's view), so a seeded Linear state change needs no Slack notice, but a seeded notice must match the issue's real state and time.
- INT-05 · linear → gmail · `svc_0251`/`svc_0257`: "N unread notifications on <workspace>" digests (1,028 + 204), `linear auto-closed <KEY>` notices (24), login/invite mails; 3,055 mails. Companion rule: digests are aggregate and a seeded Linear comment needs no mail; the 24 auto-close mails all match Canceled issues (0 conflicts, R09).

### GitHub PR comment / review → Slack mirror (#zombie-prs)
- INT-01 · github → slack · `#zombie-prs` = `C093LEZGF6J` for **match3d only**; `#engineering-bots` = `C050WGU41HR` for GameOfDominoes and game-of-dominoes-backend. match3d window **2025-06-30T21:35:55Z → 2025-09-30T22:33:40Z**; 477 PRs total, 222 in window, 220 with an "opened" mirror, 248 PR comments → 956 comment mirrors (one comment can render as several messages), 237 reviews → 210 review mirrors; PRs with no "opened" mirror: `match3d#256`, `match3d#308`. Bot user `SLACK_BOT_0004_SLACK_ID`; `attachments[0]` with `pretext` "<Event> by <github link|login>", `title` "#N <PR title>" linking to the PR, `footer` repo link, `text` = comment/review body; `'Pull request opened'` is the top-level parent, comments/reviews/merge/close are replies with `thread_ts` = that parent (merge posted as `thread_broadcast`), `'N new commit(s) pushed to <branch>'` is top-level. Mirror shows **real logins** (`arthur.blake`) while the GitHub export uses tokens (`EMPLOYEE_0025_GITHUB_USERNAME`).
- Companion rule (INT-01): a seeded PR comment/review/merge inside a repo's window needs its Slack copy threaded under the PR's "opened" parent with the real login; a repo outside the list/window must **not** get a mirror. `match3d-backend` is explicitly **not mirrored** (with `auth-game-backend`, `liveops`, `liveops-dashboard-buddy`). Copy rates: GoD bot 94%, human 89.4%, APPROVED reviews 98.6%, CHANGES_REQUESTED 100%, **COMMENTED reviews only 6.5%** (seeding_rule says ~17%) — so "every review is in Slack" is false, and matched windows matter (R07: 71 missing copies, incl. match3d).
- INT-02 · github → slack · top-level "N new commit(s) pushed to `develop|master|main` by <login>" · 3,510 messages, 0.1% ever threaded · seed one message per push, mirrored repos/branches only.
- INT-23 · coderabbit → github(+slack) · `PERSON_6026` (Organization, timeline actor `SVC_0321`): 266 PR comments, 833 review comments, 182 reviews, 229 PR bodies with an auto-generated `<!-- This is an auto-generated comment: release notes by coderabbit.ai -->` summary. Companion rule: mirrored to Slack like any comment in mirrored repos; seed only inside the tool's active window. Bot reviews count as reviews — exclude them from "human approved".

### GCal event (per-attendee copies, invitation mail)
- INT-11 · gcal → gmail · Google Calendar invitation/update/RSVP/cancellation mails, message id `<calendar-<uuid>@google.com>`; subjects `Invitation: <summary> @ <Ddd Mon D, YYYY h:mmam - h:mmam (TZ)> (<recipient>)`, `Updated invitation: …`, `Accepted: …`, `Declined: …`, `Canceled event[ with note]: …`; by kind Invitation 1,527 / Updated 2,333 (+159 with note) / Canceled 550 (+150 with note) / Accepted 1,636 / Declined 314; 3,284 dated invites, 2,860 matching a GCal instance (87.1%).
- Companion rule: invites and calendars only partly agree (R08, 424 unmatched) — a seeded meeting does **not** need an invitation mail, but a seeded invitation mail needs its GCal rows. Each attendee's calendar holds its own copy of the instance, and copies can disagree (Q11) or share `ical_uid` with a different meeting (I12); a non-attendee calendar can hold a copy (I13); a recurring master plus a standalone row can both exist for one start (I11).

### Drive / Sheets / Docs creation and sharing (share mail?)
- INT-13 · google_drive → slack · Drive Slack app **DMs only**: comments, access requests, shares; 722 messages 2023-03-02..2025-09-30, peak 2025-03 (61), channels `D04TJREVBMM` 382, `D04TWDMGAAH` 250, `D05PTJP56TE` 33, `D06S335C5B2` 26, `D04RYUMKG59` 7, `D05LC6TRMB9` 7, `D05UDNH9R8A` 6, `D07380H0Q7L` 5, `D04SNP31R5W` 3, `D0681KPDD7T` 2.
- Companion rule: DM-only, and a seeded doc comment needs no DM. There is **no** Drive→Gmail integration row: creating or sharing a Sheet/Doc produces no mail in this universe, so a "share notification mail" would be unsupported — the only share signal is the Drive DM. Drive links pasted in Slack carry Google-native ids, not `f_` ids (R04).

### Trello comment
- INT-21 · trello → slack · **no integration exists** (0 Trello bot messages, 0 human-pasted `trello.com/c/` links; `shortLink` is null on every card). Companion rule: never seed a Trello bot notification in Slack; a Trello comment exists only inside the card's `actions` and needs no cross-service copy. Card ids are 24-hex (`6851a6569f3bf818760632ab` is the board).

### Gmail send
- No integration row covers a user *sending* mail — sends are a native mailbox action, and the only rows that generate Gmail are inbound-style (INT-05/07/08/09/10/11/12/22). Slack→Gmail exists only as notification mail: INT-22 · `svc_0240` · "[Slack] <person> sent you a message", "You've got N unread messages", "[Slack] <person> mentioned you in #…", "[Slack] New messages from A and B in …" · 552 mails, seeding rule "optional; never load-bearing".
- Companion rule: a seeded outgoing mail lands in the sender's own mailbox thread (no notification mail to the sender); message/thread id conventions come from `conventions.json` (section 5). GitHub notification mail (INT-12, `svc_0248`, subject `[harmonygames-Games/<repo>] <PR title> (PR #<n>)`, 3,180 GoD / 655 match3d / 201 redacted-org, per-recipient copies) is the only way a match3d PR event appears in Gmail, and it is optional.

## 5. conventions.json

Sections present: slack, gmail, linear, github, trello, gcal, docs_sheets_slides_drive, confluence, snowflake, contacts.

### Slack ts and message ids
- `ts`: string with **6 decimals** (e.g. `1751611091.140269`), unique per channel. `message_id` = `sha256(channel_id + '|' + ts)[:32]` (holds except 18 base rows, I02). Channel ids: `C…` public/private, `D…` IM, mpdm = `C` + 11 hex, plus `FC:<file id>:<title>` canvas pseudo-channels. User ids `EMPLOYEE_00NN_SLACK_ID` / `PERSON_NNNN_SLACK_ID` / `U…`; **every Slack profile timezone is America/Los_Angeles**.
- Threads: 15,204 parents with replies; replies carry `thread_ts` = parent ts; `reply_count`, `reply_users_count`, `latest_reply` must be updated together; `thread_broadcast` subtype for a reply also sent to the channel.
- Writing conventions: bot shapes come from integrations.json (do not invent a shape); in-place retraction is `~text~` (147 rows); body length medians differ by channel type (public p50 51 chars, private p50 51, mpim p50 43).

### Linear ids
- Issue `id = identifier = <TEAM>-<n>` (`ZOM-###`, `ENG-###`, `ART-###`, `DES-###`, `EPI-###`); timestamps are varchar ISO-Z; `max_number` per team; users `usr_<16hex>` except `usr_Robert`, `usr_Lucas`, `usr_Victor Barnes`, `usr_EMPLOYEE_0024` (I10).
- ZOM states in use: Done 427, Todo 45, Backlog 34, Canceled 20, In Progress 15, Duplicate 7, In Validation 3, Regression 2. ENG: Done 1,917 / Canceled 257 / Todo 42 / Backlog 34 / Bugs 16 / Regression 2 / In Progress 2.
- **Linear comment ids: not specified in this file**, and the base has 0 Linear comments (cohorts note), so every comment is seeded — follow the export's per-record comment shape (`<ISSUE>#c_<n>`) and confirm with the Linear helper before writing one.
- Labels mix release codenames, sprints, platforms, categories: Django, Rebirth (June), Baklava (August), Desire (September – Beta Launch), Lava/Desire Lava Fix (Mid October), Nova, Destiny, Avengers (January), Cappadocia (February), Cookie, Pupusa, Grogu, Cheesecake (July), Elon (December 21st); sprint labels `Sprint <n> - <Month Dth>` including the double-space `Sprint 30 Cappadocia -  Feb 28th`.

### Drive file ids (f_)
- Files `f_<22hex>`, folders `d_<22hex>`; a Doc/Sheet/Slide's native id **equals** its Drive file id. Drive `name` keeps the source extension (`.docx/.xlsx/.html`), the native title does not (I15). Visibility: private 53,497 / domain 92 / anyone 42. MIME mix: json 27,029, folder 23,257, markdown 1,074, plain 599, Google Doc 595, pdf 409, Sheet 356, csv 172, Slides 132, doc 8.
- Consequence: quote `f_…` when naming a file; when quoting a title, drop the extension, and prefer the persona-readable copy of a duplicate (D01/D02).

### GCal event ids (evt_)
- `event_id` = `evt_<22hex>`; `ical_uid` = `<32hex>@hg4`; hangout link `https://meet.google.com/<xxx-xxxx-xxx>?hs=224`. 136 recurring series; attendees per event mean 5.7 (max 20); self response status needsAction 6,887 / accepted 2,248 / declined 125 / tentative 16.
- **Per-calendar timezones differ** (julia.lawson = `Europe/Istanbul`, leonard.hayes/frederick.stone = `America/Los_Angeles`, brian.foster/claire.morgan/martin.walsh = `UTC+03:00`, owen.baker/calvin.price/douglas = `America/El_Salvador`, oliver.brooks = `UTC-03:00`, oscar.bennett = `Europe/Sofia`, marcus.bennett = `Europe/Bucharest`) — a live-ops start time must be written with its tz, and Slack (always LA) is a different clock.
- Invitation mail message id is `<calendar-<uuid>@google.com>` (INT-11); the same instance exists once per attendee calendar, and copies can disagree (Q11) or share an `ical_uid` with another meeting (I12).

### Gmail message and thread ids
- Message record id = `<mailbox>/<RFC Message-ID incl. <>>`; thread = `<mailbox>/<19-digit X-GM-THRID>`; files are `NNNNNNNN.json` (robert + token mailboxes) or `<alias>@harmonygames.co_<thrid>.json`. Dates mix RFC-2822 (72,512) and ISO-Z (22,648), 4 missing. Bodies use `\r\n`; replies quote history with `>` after `On <date> <name> <addr> wrote:`. 2,176 internal sent messages exist (so a sent-mail scenario has precedent). Sender tokens (`svc_0107_email` etc.) must be decoded by subject pattern, not name.

### Trello action ids
- All ids are 24-hex ObjectIds; **first 8 hex = unix seconds of creation** — but 49 Welcome-Board template action ids break that (I16), so do not date an action from its prefix. Boards/cards/lists all 24-hex (`6851a6569f3bf818760632ab` = ZM ROADMAP board, cards e.g. `6851a6fde24742cce9ad7b1c`). Action types in use: updateCard 3,989, createCard 751, addMemberToCard 92, updateList 86, commentCard 56, updateCheckItemStateOnCard 53, addAttachmentToCard 48, createList 34, copyCard 34, addChecklistToCard 26, deleteCard 15, updateBoard 14 (+ rare ones). Card-name patterns: free text 618, `[Tag] name` 107, verb-first 78. `shortLink` is null on every card, so no `trello.com/c/` links exist.

### GitHub comment and review ids
- Record ids in the export are `<org>/<repo>#<PR>#c_<n>` for PR comments and review comments, and `<org>/<repo>#<PR>#ev_<n>` for timeline events (visible throughout the hazard example ids, e.g. `harmonygames-Games/match3d#319#c_1`, `GameOfDominoes#1#ev_2`); PR id is `<org>/<repo>#<N>`.
- Review states in base: APPROVED 1,742 / COMMENTED 412 / CHANGES_REQUESTED 74 / DISMISSED 2. PR titles: free text 1,707, `LINEARKEY: description` 194, `LINEARKEY description` 44, name/branch-style 318, redacted-name branch 209, conventional prefix 3. Branches: redacted owner `[PERSON_NAME_n]/<desc>` 1,011, `name/<desc>` 970, `feature|fix/<desc>` 10, other 484. PR labels: bug, documentation, draft, enhancement, invalid. 220 commits carry a Linear key; merge latency p50 2.4h, mean 19.9h, p99 185.4h. Timeline `reviewed` events have null `created_at` (T01) — timestamp reviews from `github_reviews.submitted_at`.

### Snowflake
- Row ids by table: `EVT-0001` (events), `REV-0000001`, `TXN-00000001`, `PLR-00096000`, `FIN-000001`, `ROSTER-0001`, **`PUSH-0000001`** (push stats), `INS-0000001`. Columns are UPPERCASE in the live DB (quote them) and lowercase in export rows.
- `LIVE_OPS.EVENTS.LIVE_EVENT_PERFORMANCE`: 529 runs, columns `event_id, game_id, event_name, start_date, end_date, participants, completions, completion_rate_pct, avg_score, revenue_generated_usd, status, failure_note`. **Event catalogue in the table: Axe Arena, Plague Race, River Rush, Season Pass, Streak Fever, Weekly Leaderboards, Weekly Quests, Win & Collect** — note "Collect & Win" appears here as **"Win & Collect"** (alias to reconcile), and there is no Infinite HP Boss / Boss Arena / Endless / Zombie Lane / Daily Login / Quest row name in the catalogue.
- `PUSH_NOTIFICATION_STATS`: 105 rows, `push_id, send_date, title_id, campaign_key, message_type, audience_segment, sent_count, open_count, click_count, conversion_count, opt_out_count, status, delivery_meta` — the only push-notification volume source; id form `PUSH-#######`.
- `DAILY_ACTIVE_USERS` (1,328 rows) has **no Zombie Match 3D rows — "ABSENT BY DESIGN", a fact about the company, not a gap**; ZM3D DAU must not be inferred from it. ZM3D revenue peak in `REVENUE_DAILY` is $1.99 on 2025-07-31; `LEVEL_PERFORMANCE` covers zombie_match_3d levels 1–300 with its own fail vocabulary.

### Confluence and contacts
- Confluence ids: `page_<slug>` (`page_liveops_calendar`, `page_season_pass_spec`, `page_zm3d_gdd`, `page_live_ops_engine`), `ver_<32hex>` or `ver_<slug>_vN`, `comment_<page>_cN`, `label_lNNN`, `att_aNN`, `user_EMPLOYEE_00NN` / `user_STAFF_N`. Confluence `version_messages_examples` show old bodies are readable (`page_api_reference` has "Add liveops events endpoint", "Align Nakama gRPC port to 7349", etc.) — a live-ops rule can live in a version message.
- Contacts: 24-hex ids (164) and `cnt_` ids (6).

## Summary

- Section 1: 57 in-scope hazard ids of 59 across all six categories (temporal 7 + T07 none, semantic 4, cross-service 9, quantitative 7 + Q05 none, lifecycle 12, identifier 18), each with count and example ids.
- Section 2: 24 of 25 trap ids mapped to the seven requested precedents (only N02, GoD-number overlap, is unused here); no timezone/boundary-date trap exists in the catalogue (clock 2025-10-01T07:00:00Z).
- Section 3: 25 in-scope cohorts — 12 Linear ZOM/ENG, 5 match3d/PR-keyed, 6 ZM3D Slack channels + persona mpdm, `SF-LEP` (529 LIVE_EVENT_PERFORMANCE runs), `TR-B-0632ab` (69 ZM ROADMAP cards).
- Section 4: 11 integration rows with windows and companion rules — match3d mirrors only to `#zombie-prs` C093LEZGF6J for 2025-06-30→2025-09-30; `match3d-backend` is not mirrored; no Trello→Slack and no Drive→Gmail integration exists.
- Section 5: id formats confirmed (Slack ts 6-dec + sha256 ids, `f_`/`d_` 22-hex, `evt_` 22-hex, Gmail mailbox/Message-ID + 19-digit thread, Trello 24-hex with 49 known prefix violations); Linear comment ids are unspecified and base-empty.
- Two facts that reshape the task: the event catalogue says "Win & Collect" not "Collect & Win", and ZM3D DAU is absent from `DAILY_ACTIVE_USERS` by design.

