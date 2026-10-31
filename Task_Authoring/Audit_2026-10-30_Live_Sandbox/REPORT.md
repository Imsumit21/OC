# Sandbox Discovery Report — sb-01M67A1CFD01X2FKTKP55V2NRV

## Identity
| Field | Value |
|---|---|
| Sandbox ID | sb-01M67A1CFD01X2FKTKP55V2NRV |
| Env ID | hg4-with-gsuite-bundle-1174 |
| Universe ID | hg4-synth-sep30cut |
| Modal host prefix | ta-01m67a1cfdpfzr6mwq3xpbhm9v |
| Gateway get_time (NOT the clock) | 2025-10-01T08:33:12Z |
| Freeze (clock) | **2025-10-01 07:00 UTC = 2025-10-01 00:00 PT** |
| Data cutoff | `2025-10-01T06:59:59Z` (Sep 30 23:59:59 PT) |
| Universe version | hg4-synth-sep30cut **v16** (truncated from hg4-2026-08-31 v36) |
| Fictional org | Harmony Games, Inc. (harmonygames.co) |

## Surfaces
1. pgweb 0.16.2 @ :8081 — full arbitrary-SQL REST (`/api/query`), PostgreSQL 16.15, db `agentenv`, role `agentenv` SUPERUSER, `default_transaction_read_only=off`, 10 GB. Endpoints: /api/info /api/connection /api/schemas /api/objects /api/tables/* /api/query /api/history /api/activity /api/bookmarks
2. MCP gateway @ :18765 — uvicorn; `POST /mcp` (server `hg` v1.30.0, proto 2024-11-05, Streamable HTTP + mcp-session-id); `GET /state` (full 358-tool introspection + changelog_id/roles/tool_name_clashes). resources/prompts/templates all EMPTY. All other paths 404.
3. Local repo baseline /Users/kaustubhbhargava/OC — documented expectations (298 tools / 144 tables / 17 personas).

## Database: 15 schemas / 148 tables / 1,471 columns / 6,168,869 rows
| schema | tables | rows |
|---|---:|---:|
| snowflake | 54 | 5,134,614 |
| slack | 8 | 658,726 |
| gmail | 8 | 188,561 |
| gdrive | 5 | 83,902 |
| github | 21 | 70,494 |
| gcal | 4 | 10,509 |
| linear | 16 | 8,041 |
| trello | 11 | 6,484 |
| gslides | 4 | 4,673 |
| gsheets | 3 | 1,730 |
| gdocs | 2 | 596 |
| contacts | 4 | 341 |
| confluence | 7 | 198 |
| public | 1 | 0 |
| agent_env_internal | 0 (1 seq) | - |

Metadata: 559 constraints, 283 indexes, 441 triggers, 0 enums, 0 views, 1 sequence,
extensions pg_trgm 1.6 (github schema) + plpgsql, 26 empty tables, TimeZone UTC.

## Audit mechanism
Every universe table carries `_changelog_trigger` (AFTER INSERT/UPDATE/DELETE) -> `public._changelog_trigger_fn()`,
which takes `pg_advisory_xact_lock(hashtext('public._changelog'))` and writes to `public._changelog`.
`public._install_changelog_triggers(schema)` installs them. **public._changelog = 0 rows** and
`/state.changelog_id = null` => universe is PRISTINE / unmutated.

## MCP: 358 tools / 14 servers
github 75, trello 51, linear 37, gmail 36, gcal 30, slack 30, confluence 28, gdrive 21,
contacts 16, gsheets 11, snowflake 9, gslides 7, gdocs 6, gateway 1 (get_time).
Async pattern: 8 `*_submit_*` + 8 `*_get_job_status` + 8 `*_get_job_result`.
Identity tools: only `confluence_get_current_user` + `contacts_get_current_user_details`.
No `*_health` tools exist live.

### Delta vs documented 298-tool catalog: +77 / -17
+19 gcal (ACL/calendar CRUD), +19 github (reviews, repo create/fork, issue_read/write),
+12 trello, +11 linear (attachments, labels), +9 contacts (groups), +4 gmail (drafts,
batch_delete), +2 gsheets (values_clear), +1 gdrive (copy_file).
Removed: all 13 `*_health`, plus contacts_show_data, linear_show_data,
slack_conversations_edit_message, trello_delete_list.

## Universe content — Harmony Games, Inc.
Remote-first hybrid-casual mobile game studio, founded March 2023, incorporated Delaware.
~19 people incl. 3 founders. Titles: **Domino Delights** (live, iOS+Android) and
**Zombie Match 3D** (beta, Oct 10 target). Competitor tracked: Match Factory.

- Slack: 610,468 messages across channels incl. founders, builds, game-design, executives,
  engineering-bots, god-bugs, zombie-match3d, investors, admin_foundersonly, analytics, product,
  ad_monetization, plus DMs/mpdm and FC: canvas files.
- Gmail: 95,161 messages / 81,404 threads across 27 mailboxes; 30+ labels
  (App Center/TestFlight, Stability Issues, Helpshift, Meta Ad Notifications, Finance/Receipts).
- Confluence: 4 spaces (ENG, PROD, COMPANY, OPS), 28 pages — Architecture Overview,
  AWS Infrastructure, Nakama Server Setup, Elixir/Phoenix Backend, QA Regression Runbook,
  Economy Design, Domino Delights GDD, Zombie Match 3D GDD, Product OKRs 2025 H1.
- GitHub: 15 private repos under harmonygames-Games (GameOfDominoes, match3d, match3d-backend,
  liveops, game-analytics-pipeline, harmony-gpt, auth-game-backend, website...);
  18,894 commits, 2,475 PRs (2,468 closed / 7 open).
- Linear: 5 teams (ENG 2366, ART 792, ZOM 566, DES 312, EPI 28), 3,687 issues, 2 projects
  (GoD - Beta, Zombie Match 3D).
- Trello: 5 boards — Harmony Games (449 cards), DD Product Roadmap (216), ZM ROADMAP (79),
  UA/BD (40), Welcome Board (19). Release trains named Baklava/Desire/Cookie/Elon/cappadocia.
- Drive: 53,631 files (27,029 json, 23,257 folders, 1,074 md, 595 gdocs, 409 pdf, 356 sheets,
  132 slides); Docs 595, Sheets (investor lists, level data, funnel analyses),
  Slides (BoD decks, pitch MASTER, studio intro).
- Calendar: 10,395 events, 2023-03-17 .. 2026-01-14; top organizers robert (5,121), leonard.hayes (3,893).
- Snowflake: 3 DBs / 6 schemas / 54 tables — ANALYTICS (GAME_EVENTS, MARKETING, MONETIZATION,
  RAW_TELEMETRY), FINANCE (EXPENSES), LIVE_OPS (EVENTS), + wh_information_schema mirror.
  Largest: virtual_currency_ledger & resource_flow_events 1,308,560 each; raw_events 694,634.

### Business state at freeze (FINANCE.EXPENSES)
Cash 2025-09-30: **$157,538**, net burn $58,170/mo, **runway 2.7 months**, headcount 12
(down from $1.26M cash / 15 heads in Oct 2024). Sep-2025 burn: salaries $43,740.61,
aws_hosting $2,325, tools $1,410, legal $780, other $10,438.
Peak DAU: domino_delights iOS 1,089 / Android 277. IAP: 885 txns / $4,341.15 (DD), 1 txn (ZM).
Live-ops: 508 DD events + 21 ZM events.

## Identities: 42 distinct @harmonygames.co
13 present in all 7 identity services (arthur.blake, brian.foster, calvin.price, claire.morgan,
douglas, frederick.stone, julia.lawson, marcus.bennett, oliver.brooks, owen.baker, robert,
samuel.turner, vincent.parker). 6-of-7: felix.young, leonard.hayes, martin.walsh, oscar.bennett,
thomas, victor.barnes. Also simon.walker, lucas, benjamin.clark, christopher.allen, elliot,
george.miller, josh.dempsey, lauren, marcus.lee, matthew.collins, megan.wilson, michelle.carter,
ozhan, patrick, thomas.baker, tim.steudler, victoria.lane, rachel, nathan, peter.lawson,
graham, stevencarter, employee_0024.
Confluence IDs: user_STAFF_1..11 + user_EMPLOYEE_00xx. Slack TZ America/Los_Angeles;
gcal TZs span America/LA, America/New_York, America/El_Salvador, Europe/Istanbul,
Europe/Bucharest, UTC+03:00.

## Freeze verification
| source | earliest | latest |
|---|---|---|
| slack_messages | 2023-03-02 01:40 | 2025-10-01 05:51 |
| gmail_messages | 2023-03-15 00:05 | 2025-10-01 06:25 |
| github_commits | 2023-03-23 18:22 | 2025-10-01 05:44 |
| linear_issues | 2023-03-22 19:11 | 2025-09-30 16:26 |
| drive_files | 2015-12-14 | 2025-09-30 17:50 |
| trello_actions | 2014-01-13 | 2025-09-30 17:09 |
| gcal_events | 2023-03-17 | 2026-01-14 (future meetings) |
Rows after freeze: slack 0, gmail 0, commits 0. Only 24 future calendar events. CLEAN CUT.

## Divergence vs documented baseline
| Dimension | Documented | Live | Delta |
|---|---|---|---|
| Schemas | 14 | 15 | +agent_env_internal |
| Tables | 144 | 148 | +4 (gdrive, gmail, linear, trello +1 each) |
| MCP tools | 298 | 358 | +77 / -17 |
| Services | 13 + gateway | 13 + gateway | same |
| Personas | 17 usable | 42 distinct emails | much wider |
| Freeze | 2025-10-01Z | confirmed | match |
Note: local reference DATA is the Feb-2026 freeze, so data divergence is expected by design.

## Data-quality / safety observations
1. **Anonymization leakage** — unsubstituted placeholders survive in live data:
   `EMPLOYEE_0032_EMAIL`, `PERSON_0242_EMAIL`, `SVC_2669_EMAIL`, `EMPLOYEE_0001_GITHUB_USERNAME`,
   `[SOURCE_ORG_0001]`, `[PERSON_NAME_0092]`, `[email_0049]`, `PERSON_6092_TRELLO_USERNAME`
   (in trello board URLs). Mixed with real-looking values in the same columns.
2. **DB is writable** — role `agentenv` is SUPERUSER with replication + bypassrls and
   `default_transaction_read_only=off`. pgweb gives unauthenticated arbitrary SQL. No auth on
   either port. Treat as fully privileged.
3. **Your activity is recorded** — pgweb `/api/history` retains every query; `/api/activity`
   shows live backends. pgweb `session_lock=true`.
4. `gmail.gmail_users.messages_total` (e.g. leonard.hayes 19,668) far exceeds stored
   `gmail_messages` rows (95,161 total) — counters describe the source mailbox, not the sample.
5. Duplicated snowflake projections (`revenue_daily` vs `revenue_daily_v2`,
   `ad_spend` vs `ad_spend_daily` vs `ua_spend_unified_v2`, `raw_game_events` vs
   `stg_events_enriched`) — intentional decoys per the RAW_TELEMETRY schema comment.
6. gcal events contain exact duplicate rows (POD: PROTOTYPE x15 at same timestamp).

## Corrections applied 2026-10-31

Four claims in the original draft were wrong and are corrected above:

1. **Freeze is `2025-10-01 07:00 UTC` (= 00:00 PT), not `00:00 UTC`.** Authority:
   `Evals/references/universes/synthcut/universe_manifest.json` -> `evaluation_clock`.
   Data cutoff is `2025-10-01T06:59:59Z`. The repo's old `11_V3_Changes.md` inverted the
   conversion; it has been fixed. 79 live rows sit in the 7-hour gap.
2. **The SynthCut provenance manifest DOES exist** - at
   `Evals/references/universes/synthcut/universe_manifest.json`, supplied by the
   2026-10-20 bundle. The repo was simply on the older flat reference layout.
3. **Gateway `get_time` is not the clock.** `Evals/ENVIRONMENT.md` states the fixed
   universe clock must not be replaced by machine clock, `get_time`, or export date.
4. **The 17-persona roster is policy, not a defect.** It is the approved roster; the 42
   addresses found in the database are observed identities. The roster was left untouched.

## Artifacts (this folder)
MANIFEST.json, Q1_tables_columns.json, Q2_constraints.json, Q3_indexes.json, Q4_enums.json,
Q5_triggers.json, Q6_rowcounts.json, X_extensions/views/sequences/roles/settings/tablesizes/
comments/dbsize.json, state_full.json, tools_raw.json, live_tool_names.json, tool_delta.json,
personas_crossservice.json, sbq.py, mcp.py, dump.py

---
*Collected 2026-10-30 against live sandbox `sb-01M67A1CFD01X2FKTKP55V2NRV`.
All access was strictly read-only: SQL helper rejected any non-SELECT statement and the MCP
helper rejected every write-verb tool. `public._changelog` remained 0 rows throughout,
confirming the universe was not mutated. Helper scripts `sbq.py` (SQL), `mcp.py` (MCP
tools/call) and `dump.py` (schema-aware printer) are reusable against any HG sandbox by
editing the base URL constant.*
