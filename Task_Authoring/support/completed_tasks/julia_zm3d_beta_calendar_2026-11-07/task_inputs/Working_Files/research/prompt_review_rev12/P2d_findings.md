# P2 deep recheck findings (Eval 1 Phase 5, blind)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL reviewed: sha256 b5ccbfa577fc9f2c8f6eb3098f8d62a16623d799f41d11285de8227f1bed60d3, read only, never run.

## Result

Cross-Service Coherence: one low-impact item (DR1), no fail-level item. On the rule given, that is NON-FAIL.
Feasibility, Persona access, Data exists, Tool use and cross-service: no finding.
A second confirmed low-impact item from any other pass would make coherence a FAIL, so DR1 should be fixed anyway.

Checked: 6 of 6 prompt sentences; 111 of 111 SQL statements (81 inserts, 30 updates); 32 Linear comments; 21 Linear issue updates; 12 Slack inserts and 8 Slack updates; 6 Gmail messages; 4 calendar events; 4 Drive files; 5 GitHub rows; 2 Trello rows. `hg.py lint` on this SQL: 0 FAIL, 0 CHECK, 0 INFO.

## Findings

Format: DR# | pass | checklist section | quoted text | record path, id and quoted value | dimension | severity

**DR1 | P2 | Eval 1 §3.2, Semantic / Category | Injected `github.github_review_comments` id `harmonygames-Games/match3d#468#rc_38` (Arthur, 2025-09-29T15:36:41Z, mirrored to #zombie-prs): "The Collect & Win vials that spawn in the levels are still the first-pass models. The final vial models are missing and need to be in before the beta, Claire has those on her list." | Other side below | Cross-Service Coherence | LOW-IMPACT**

Base evidence of the same work points the other way:
- Git, match3d: `a4872cfbec` 2025-08-08 claire "Collect&Win Items" added the vial prefabs. `741527de5c` 2025-08-14 claire then changed `Assets/MyAssets/3dModels/SmoothedModels/weapons/Skull_Potion.fbx`: LFS oid `c1fad70e...` to `80a6dd4e...`, size 59504 to 47600. No later model commit exists.
- Slack DM D076Y0SDV18 (Claire and Brian, Julia not in it): Claire 08-08 12:34 "Yaptım bile, sadece oyuna atmadım ama hızlıca koyabilirim acilse". Brian 08-12 asks to swap the skull icon. Claire 08-12 09:29 "değiştireyim sıkıntı değil", 11:51 "şimdi yeni objeler de var onlarla birlikte atarım". The Aug 14 commit is that delivery, so the repo holds a revised model, not a first pass.
- Claire's status the same day: Gemini notes `f_b7aae618602a7ccc0cc9a7` (Sep 29), "Claire Morgan: Um, I'm working on some leave objects." The notes and transcript never mention vials or bottles. #zombie-art 09-30 15:53 Claire: "Progress on new objects."

Why it counts: this one record creates a graded still-to-do item (Collect & Win, final vial models, owner Claire), and its descriptor does not match the asset's history. No other record, including Claire's own, says vial work is open.

Why it is only low-impact: no persona-visible record gives a different value, so there is no fork, and the task stays solvable. Limit: the FBX is an LFS pointer, so I cannot prove what changed in the model. "First-pass" is contradicted by inference, not by a quoted statement about the mesh.

Fix (plain description): remove the first-pass claim, and ground the ask in a new art need raised after Aug 14, or add a record from Claire that takes the item.

## Advisory only (not scored)

| # | Item | Both sides | Why advisory |
|---|---|---|---|
| A1 | Oct 8 release vs Sep 29 meeting | GCal `evt_5c1e83a7d94b02f6c8e31a` (created 09-24, updated 09-26): "go live with this release", 2025-10-08 15:00Z. Notes `f_b7aae618602a7ccc0cc9a7`: "for vin collect it needs to be deployed to pro servers" / "maybe that's something Douglas can help me with today" / next step "will help [..] to deploy the win and collect to pro servers" | The note is an undated plan and confirms it was not on prod on Sep 29. Later visible records settle the value: #470 rc_10 "still on the DEV stack only"; ZOM-563 18:17Z "the Collect & Win server windows wait for the Oct 8 release". The doc is Leonard-only. Small friction: the invite predates a meeting where nobody mentions it. Dating the invite after Sep 29 would remove it. |
| A2 | Season Pass strip art | #472 rc_1 "premium strip art still shows the October range". `git grep` for month or date-range fields in `Assets/Scripts/LiveOps/SeasonPass/` returns nothing; sprites are LFS pointers | Unsupported but not contradicted. A date baked into a bitmap cannot be disproved. |
| A3 | Private QA notes on Sep 30 | D07GMT8NVM2 Vincent 17:17 "sp is not opened after it's introduced", 17:18 "nothing serious ofc". Fix `93f45ebbfc` lands 21:36Z, after submission builds #50 and #135 started (18:43Z, 18:45Z). Self-DM D05QQ7YQTND 12:19 "Kill zombie quests don't work" | Not provably "cannot enter, score or claim on prod", not prod deploy, config or art, and hidden from Julia. No value depends on them. |
| A4 | Brian to Marcus DM | D076V3NB6P7 09-30 16:33 "Could you polish the bottle vfx for Collect&win?" | Polish, ordered after other work, not stated as needed for the beta. Hidden from Julia, and the brief's "still needed" test is not met. |
| A5 | Brief's change-request clause | "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it." The only CHANGES_REQUESTED since 2025-07-15 in any repo is match3d #303 rev_6 (CodeRabbit, 07-16). No record defines "Aug-Sep live-ops cohort" | Empty set, so no value changes. Wording belongs to P1. |
| A6 | SC-57 | Injected Douglas reply "Both tables are updated." sits in #zm-collect-win, `is_archived: true` | Known base issue. Julia is not a member, the matching ask is in the same channel, and no task value depends on it. Not scored. |
| A7 | Branch label | cmt_zom565_1 "Marcus/EndlessMode_Vfx"; export branch `marcus.bennett/EndlessMode_Vfx`; PR head_refs use `Marcus/...` | The base itself mixes both prefixes. No value depends on it. |
| A8 | PN wording | #zombie-bugs 09-18 Leonard "All our PNs are local"; PNs Beta row 2 is "Push Notification", LIVE | Base only. Row 2 is held on Not Ready either way. |

## Topic lines

- **Cross-Service Coherence:** DR1 only. No State / Lifecycle item, no Quantitative item.
- **Feasibility: no finding.** All 6 writes have a cataloged tool: `gsheets_values_update` (both tabs), `linear_create_comment` (ZOM-429 note, ZOM-78 link), `slack_send_message` with `thread_ts`, `gmail_reply_to_message`. No open instruction, so the over-15 scope rule does not apply. Every breakdown has a field: PNs Beta holds Status, What, When, Details, Segmentation, Status (NA, WIP, LIVE), Headline, Body.
- **Persona access: no finding.** Every scoped record the answer needs is open to `julia.lawson@harmonygames.co`: DM D05SD5QLG94 and D05GU6L0XFH (member); #zombie-art, #zombie-match3d, #zombie-bugs (member, no leave event); the brief and deck (shared, reader); her own sheet and folder; Push Notifications Zombie Match (shared list and domain); the Oct 8 event on her calendar; both Brian mails in her mailbox. Hidden record line: none.
- **Data exists: no finding.** All named records exist: ZOM-78, ZOM-429, PNs Beta with the four named rows, the 24h lock on the Season Pass spec, Collect & Win windows, Oct 8 15:00Z, both Brian dates.
- **Tool use and cross-service: no finding.** Two services line: Gmail (Oct 31 10:00 Istanbul misses the lock) and Calendar (release instant, sets the first window). Dropping either changes a graded fact. Linear, GitHub, Confluence, Sheets and Docs each also change one: the ZOM-429 note and ZOM-78 link; vial, icon and strip items; the 24h lock; the push decisions; the rules.
- **Derived columns:** none. The answer reads no Snowflake column. Snowflake has no ZM3D leaderboard rows, so it neither supports nor contradicts the hold.
- **Date-slip:** none. All 6 weekday-date pairs and both mail epochs are correct, and no injected timestamp is after the clock (latest 2025-09-30T22:10:41Z).

## Checked and consistent

Slack
- 12 inserts: ids and ts do not collide; ts equals created_at on all 12; every author is a channel member.
- 8 updates: thread counters match base plus injected. #470 16 to 17, #472 3 to 4, #468 41 to 42, d0dd 4 to 5, a3e7 3 to 4 with 4 users, 0069 2 to 3 with 2 users, and the two new threads (9025, ede9) 0 to 1.
- The #468 parent diff is only the added Reviewers entry. Mirror ts follow GitHub by 2 seconds, and the discussion ids increase with time.
- Robert's replies are in Martin's real threads: Halloween 09-17, and desert 09-29 with the Port theme post at 09-30 16:27. "Halloween" has no competing decision anywhere in Slack, Linear, Trello or Docs.

Gmail and Calendar
- 3 mailbox copies of each mail, no thread id collision in 81,404 threads. Epochs match headers. Istanbul +03 is right.
- Oct 29 to Oct 31 is the stated two days. Oct 31 07:00Z misses the Oct 31 00:00Z lock.
- 4 calendar copies, one per attendee. 15:00Z equals 18:00 Istanbul.

Drive, Docs, Slides, Sheets
- Parent folders are the real root folders of Julia and Frederick. `.docx` and `.xlsx` names on Google mime types match the base pattern.
- All 9 doc style-run offsets land on their headings.
- Deck weeks match the brief. The UA deck's carve-out of Unity retention campaigns covers the base Sep 27-30 spend.
- Translated tab holds the Domino set (Tiledozer and Luckydrop rows), as the brief says.

GitHub and git
- rc_10 and rc_1 sit on real Arthur approvals at the same second, before merge. rev_3 and rc_38 are 37 minutes before the #468 merge. No id collides, and the file paths are in each PR.
- ev_6 matches the base 'reviewed' shape (all 2,116 have null created_at).
- Icon claim holds: #454, #456 and #458 animate Quests, Season Pass, Endless, Zombie Lane, Plague Race and Infinite Boss. No Collect & Win clip exists in the repo.
- lightSweep: `25c6c66b6b` (21:20Z, Oliver) changes `lightSweep Box Variant.mat`, 26 minutes before Vincent's note, and after the submission builds, so "rides the next store build" holds.
- ZOM-534 fix is `47c65623e7` "sync quests end with client". Marcus comment matches `44988da015` ("still hidden"). #475 is the card pack animation. #471 touches the Daily Gift sprite.
- Backend CDK matches the brief: Collect & Win groups, `SEASON_PASS_SCHEDULE "0 0 1 * *"`, leagues Monday 00:00 UTC, Endless daily and weekly.

Linear
- All 32 comments post-date their issue, and all author ids resolve to the right person.
- All updated_at values move forward. Completed issues (ZOM-344, 432, 563) carry a matching comment and completed_at; none has later activity.
- ZOM-471 is true to base: Leonard 08-13 "yeah, we don't need it! cancel the ticket".
- ZOM-563 matches Douglas's base DM 09-30 18:16. ZOM-566 matches Owen 09-30 16:49 and PR #477.
- ZOM-521 ticks agree with ZOM-525, 526 and 528, which repairs SC-15. Open tickets ZOM-534 and ZOM-552 state why they stay open.

Other
- Trello: comment author is Leonard, the card's named owner. Oct 13 is a Monday.
- Confluence: Robert is Product, Frederick owns the calendar, the 24h freeze appears on both pages, and Collect & Win is "not yet live".
- Injected records agree with each other across all pairs: Oct 8 in GCal, ZOM-563 and #470; Oct 31 in the mail and Oct 29 superseded; approval and retraction order; ZOM-465 comments 1 to 3.
- Known issues touched, none load-bearing: SC-6, SC-13, SC-22, SC-38, SC-57, SC-71. SC-15 and SC-16 (ZOM-563) are repaired by the SQL.

## Evidence limits

- `catalog.json` has no return schemas. That `github_get_pull_request_comments` returns inline review comments is assumed. The #zombie-prs mirrors are a second route, but Julia is not a member of that public channel.
- LFS blobs are not readable, which limits DR1 and A2.

Platform defects: none.
