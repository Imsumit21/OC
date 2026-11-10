# P2 deep recheck: services, data and access

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL reviewed: sha256 1348d287ac4a105c41b9f0bf511c6664e306adcc3cf42406688a228fd4b684e7 (confirmed). Never executed.
Persona: Julia Lawson, julia.lawson@harmonygames.co (roster match).

**Result: 1 low-impact finding, 1 advisory, 0 fail-level.** From this pass, Cross-Service Coherence is NON-FAIL 3 (one low-impact item). Feasibility, Persona access, Data exists and Tool use and cross-service are clean.

Checked: 6 of 6 prompt sentences, 110 of 110 SQL statements (80 inserts, 30 updates), plus Frederick's 2 messages and all 8 sections of the brief. `hg.py lint`: FAIL 0, CHECK 0.

## Findings

Format: `DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension or issue type | proposed score or severity`

**DR1 | P2 | deep_recheck P2, Eval 1 §3.2 | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me." (brief: "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC") | records below | Cross-service Referential Inconsistency | LOW-IMPACT (one item, NON-FAIL 3)**

Value it sits on: Collect & Win first window, Fri Oct 10 00:00 UTC, and the still-to-do "prod deploy, Douglas". If the windows had gone out on Sep 29 or 30, the first window would be Mon Oct 6 00:00 UTC.

Injected side:
- `github_review_comments` `harmonygames-Games/match3d#470#rc_10`, 2025-09-30T15:51:06Z, Arthur: "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The Plague Race, leagues, Endless and Season Pass schedules are already running on prod."
- `gcal_events` `evt_5c1e83a7d94b02f6c8e31a` (Julia's copy), created 2025-09-24T16:05:37Z, updated 2025-09-26T17:20:09Z, start 2025-10-08 15:00 UTC: "Prod backend deploy for the beta. The server windows that are still on the DEV stack go live with this release; release window 18:00-19:00 Istanbul time."

Base side:
- gdocs `f_b7aae618602a7ccc0cc9a7`, "POD_ PROTOTYPE - 2025_09_29 08_56 PDT - Notes by G" (Leonard, private, `shared_with_emails` empty), transcript at 00:14:14:
  - [PERSON_NAME_9942]: "Uh for vin collect it needs to be deployed to pro servers."
  - [PERSON_NAME_0357]: "Okay, so maybe that's something Douglas can help me with today. Douglas, is There anything else on your plate? It doesn't sound like a full day task."
  - [PERSON_NAME_0612]: "Uh no it's not."
  - Speaker tokens are inferred: 9942 from the QA remarks (Vincent), 0612 because that speaker answers when Douglas is addressed.
- Same doc, next step: "[PERSON_NAME_0612] will help [PERSON_NAME_0357] to deploy the win and collect to pro servers and complete the configuration for Google Play login." The copy in Frederick's mailbox (`Notes: "POD: PROTOTYPE" Sep 29, 2025`, 2025-09-29 18:53Z) resolves [PERSON_NAME_0357] to Leonard Hayes.
- Slack DM `D079SNE2TL4` (Vincent and Douglas), 2025-09-30 18:16:33 UTC, 2h25 after Arthur's comment, Douglas: "Ok, I updated the prod environment with the latest teams/social changes, let me know if you are still getting those issues"
- `match3d-backend` git:
  - adb56ad (2025-09-01) adds `WIN_AND_COLLECT_GROUP_1_SCHEDULE: "0 0 * * 1,2"` with "// DEV: same as prod for testing".
  - d970303 (2025-09-05) is the first commit on any ref to add `SEASON_PASS_SCHEDULE`, directly below those lines. So no revision has the Season Pass schedule without the Collect & Win one.
  - `config/runtime.exs`: `config :zombies_game, ZombiesGame.WinAndCollect, enabled: true`.
  - `lib/zombies_game/leaderboards/supervisor.ex` lines 66 and 73-75 start `season_pass` and `win_and_collect_group_1..3` from the same event list.

The tension:
- Oct 8 had been on the calendar since Sep 24-26, with Douglas as organizer. On Sep 29 he agreed to a same-day prod deploy and nobody cited the Oct 8 release.
- Literally, the "next backend release" after Arthur's comment is Douglas's 18:16 prod update.
- "Season Pass on prod, Collect & Win DEV only" has no matching revision on main.

Why low-impact and not fail-level:
- No record says the windows reached prod. I searched Slack from July 2025 on (69,404 messages, every channel and DM), Julia's, Brian's and Frederick's mail, Docs, Confluence and git.
- These records support the injected side:
  - The same Sep 29 meeting says the deploy is still needed.
  - `D05SG9H1CFM`, 2025-09-26 20:48:47, Douglas: "Ese merge con main significa que debo deployar a prod?" Owen, 21:00:25: "Igual no va para release ahora".
  - `page_liveops_calendar`: "not yet live".
  - `page_api_reference` v4 (2025-09-29) lists no win-and-collect route.
- The Sep 30 deploy is scoped to "teams/social", so a slipped plan reconciles the records.
- It is not State / Lifecycle, because no status field or record claims the deploy happened.
- Julia cannot read the doc, the DM or Frederick's mail. Every record she can read agrees on Oct 8, so solvability is untouched.

Missing record: a dated record saying the Sep 29 Collect & Win prod deploy moved to the Oct 8 release and that the Sep 30 deploy did not carry it.

**DR2 | P2 | §3.2 | same sentence (brief: "An established failure holds it; an unverified one does not.") | injected Slack `e343557b2e94a1701251ebd079e6f0ce`, #zombie-bugs, 2025-09-29T23:17:41Z, Leonard: "Ran this again on an S23 Ultra in the cloud device farm, live Android build, a few endless runs with the airstrike. Could not get it to freeze, so I am leaving this one." vs base #admin_foundersonly, 2025-08-07 22:32:40, Leonard: "I canceled BrowserStack, just to make sure we don't get hit by another $49 for a service that I won't personally use every month" | Semantic / Category | ADVISORY ONLY**

The injected text does not name BrowserStack, and it is the only device farm in the base. On Sep 28 Leonard was using BlueStacks simulators (#executives, 02:10:20: "I tried a samsung simulator same problem"). Using a cloud device fits his friend's phone being the original S23 (#executives, 2025-09-21 05:13:46). Endless stays not held either way, so no task value depends on it. Not scored.

## Section 3 lines

- **Two services:** Slack and GitHub, plus Docs, Slides, Sheets, GCal, Gmail, Confluence and Linear. Each changes a graded fact:
  - Slack: ask, withdrawal, leaderboard retest.
  - GitHub: DEV stack, vials, November strip.
  - GCal: release instant.
  - Gmail: Oct 31 date.
  - Confluence: 24h lock.
  - Sheets: push rows.
  - Slides: buy weeks.
  - Linear: tickets and owners.
  - Trello is a decoy only.
- **Hidden record:** none. No required record is hidden from Julia.
- **Derived columns:** none. The answer reads no Snowflake table, so FD-3785 does not apply.
- **Open-instruction scope:** not an open-fix instruction. Scope is about 8 beats and 10 pushes, under the 15-item line.
- **Date-slip severity:** no wrong date in any relied-on record. All weekdays checked: Oct 6, 8, 10, 13, 29, 31, Nov 1, 2, Sep 22, 26, 30.

## No-finding lines by topic

- **Cross-Service Coherence:** DR1 and DR2 only.
- **Feasibility:** no finding. Every ask has a cataloged path and fits the data:
  - Sheet: `gsheets_values_update` or `gsheets_values_append`.
  - Ticket note and link: `linear_create_comment`.
  - Slack reply: `slack_send_message`.
  - Mail reply: `gmail_reply_to_message`.
  - The sheet columns (9 and 7) all have source data. No breakdown lacks a field.
- **Persona access:** no finding.
  - Julia is a member of `D05SD5QLG94`, `D05GU6L0XFH`, #zombie-match3d, #zombie-bugs and #zombie-art, with no leave events.
  - Brief and UA plan are shared with her, her sheet and folder are her own, and the push sheet is shared with her.
  - The mail is in her mailbox and the event is on her calendar.
  - She is not in #zm-collect-win or #zombie-prs, but neither is required. GitHub is unscoped, and "Both tables are updated." only closes a side request.
- **Data exists:** no finding. Lock: `page_season_pass_spec` "locked 24h before each season opens". Windows: Confluence and CDK. All 14 PNs Beta rows are present, and leaving out Frederick's 4 leaves 10.
- **Tool use and cross-service:** no finding. No single service answers the task.

## Eval 1 §3.2 table

| Prompt ask / source | Static evidence | Discovery / access evidence | Coherence |
|---|---|---|---|
| Frederick's ask + reply | NEW: ts = created_at, thread 1/1 | DM, Julia a member | PASS |
| Brief + UA plan | NEW: style offsets all land on headings | Shared reader, Frederick's root | PASS |
| Sheet + folder | NEW: parent = Julia's root, .xlsx/.docx names follow base | Owner Julia | PASS |
| Collect & Win start | NEW: release 15:00Z = 18:00 Istanbul | GCal + #470 | NON-FAIL (DR1) |
| Leaderboard hold | NEW: Vincent 2025-09-30 20:50 | ZOM-429, only open ZOM leaderboard ticket | PASS |
| Halloween one-off | NEW: thread 1/1, DM withdrawal | Member of both | PASS |
| November Season Pass | NEW: internal_date = Date header, per-mailbox THRID as base | Julia's copy, lock in Confluence | PASS |
| Push rows | Base + Frederick's reply | Zombie Match sheet shared | PASS |
| Decoys (Linear tickets, Slack threads, Trello card) | NEW: see list below | Linear and Trello unscoped | PASS |

## Checked and consistent

**Slack (12 inserts, 8 updates)**
- All ts = created_at. No id or ts collision in the 7 channels. All authors are members.
- reply_count and latest_reply match base + 1 on all parents: 17, 4, 42, 5, 4, 3. reply_users_count is right, including lightSweep staying at 3.
- The #468 attachment update changes only Reviewers.
- The mirror's "Comment on pull request by" naming the commenter follows base.

**Injected claims confirmed by base**
- lightSweep: commit 25c6c66b6b (Oliver, 21:20 UTC) touches `lightSweep Box Variant.mat`, 26 minutes before Vincent's reply.
- Port theme: Martin's post at 16:27:07 precedes Robert's 16:41:08 reply.
- ZOM-471: Leonard's "yeah, we don't need it! cancel the ticket" and Vincent's "it already has start button" are in the base thread.
- ZOM-534: 47c65623e7 "Using remaining-time endpoint to sync quests end with client". Quest reset is 00:00 UTC daily and Monday weekly, which matches "Mon Oct 13 rollover".
- ZOM-432: PR #471 touches `img - DailyGift.png`. iOS #50 and Android #135 are in #builds on Sep 30.
- ZOM-465: main has animators for Endless, Infinite Boss, Plague Race, Quests, Season Pass and Zombie Lane, and none for Collect & Win. PRs #454, #456 and #458 predate Sep 26, and #468 opened after Marcus's note.
- ZOM-521: #475 is the card pack animation. ZOM-528 and ZOM-541 are still open.
- ZOM-526: #472 merged before the comment.
- ZOM-565: 44988da015 at 14:33 UTC, and Marcus's base DM at 14:34:25 says he wrote the comment.
- ZOM-563: closed at 22:04:33, after Vincent's base "Yep it works as expected" at 21:58:44.
- ZOM-566: base "Analytics and name changes first", and #477 follows.
- ZOM-543: QueueManager.cs flow. ZOM-549: endless fields in, left_level not. ZOM-442: parameters. ZOM-552: `SeasonPass_redeem`.
- #468: `collectAndWinVial` in GameLoader.cs, and Claire's first models a4872cfbec on Aug 8.
- "Both tables are updated.": Douglas's Sep 29 transcript line "the new value should be There" agrees. Only the Gemini summary line is looser, and it is not a contradiction.

**Linear (31 comments, 21 updates)**
- Every author id resolves.
- Every issue's updated_at is at or after its last comment.
- No closed ticket has later activity (ZOM-344, 432, 563).
- started_at is before the first comment on ZOM-566.
- State values exist in base. Done with null started_at is normal (120 of 427 ZOM).

**Gmail (6 threads, 6 messages)**
- All 3 mailboxes have both mails.
- `Label_b19fb8d1b3` is "Opened", and the labels match X-Gmail-Labels.
- Headers match UTC.
- Different thread ids per mailbox match base.

**GCal (4 rows)**
- All four attendees hold a copy, with one shared ical_uid.
- No competing base event.

**Drive, Docs, Slides, Sheets**
- Parents resolve, and ids do not collide.
- Modified and created times agree across tables.
- The translated tab is Domino copy (44 hits, 0 Zombie).

**GitHub (5 rows)**
- rev and rc sequence numbers are correct.
- rev_9 and rev_1 are base reviews, and comment times equal the review times.
- The comment on #468 is before its merge.
- Empty diff_hunk is present in 53 base rows.
- ev_6 uses the base head sha.

**Trello**
- Leonard is the card's author. The comment badge and dateLastActivity are updated.

**Clock**
- The latest injected past record is 2025-09-30T22:10:41Z. Only the Oct 8 event is in the future, and it is a plan.

**Known issue cards, not scored (no task value depends on them)**
- SC-57: #zm-collect-win archived flag.
- SC-13: BETA list name.
- SC-6: Brian's address.
- SC-47: Domino quests row.
- SC-62: import cadence.
- SC-15 and SC-16 are resolved by the injection for ZOM-521 and ZOM-563.

**Change-request rule:** no CHANGES_REQUESTED review exists in the Aug-Sep cohort. The only recent one is #303 (Jul 16), so the rule holds nothing. Not a defect.

## Limits

- Season Pass sprites are LFS pointers, so the "October range" art cannot be viewed. No record contradicts it.
- Non-member reads of public channels are not provable locally. Neither channel is required.
- Linear status changes from the injection have no Slack bot echo. That is an absence, not a conflict.

## Platform defects

- Anonymized tokens in PNs Beta copy: `[PERSON_NAME_2549]` in the FTUE and Season Pass rows, `[PERSON_NAME_16313]` in the Nathan row. Source strings, not scored.
- PLATFORM:FD-2880 and PLATFORM:FD-3785 are not triggered.
