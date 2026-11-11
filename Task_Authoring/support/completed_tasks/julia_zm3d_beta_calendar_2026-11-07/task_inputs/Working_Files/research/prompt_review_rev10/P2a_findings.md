# P2 deep recheck: services, data and access (blind)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
SQL reviewed: 01_Universe_Inject.sql, sha256 ffbac4586fb91842ca16263c2b76987c26623c7ed689e00d33886c63f9331bdc (read, never executed)

## Result

| Severity | Count |
|---|---|
| Fail-level | 0 |
| Low-impact | 0 |
| Advisory only | 5 |

Checked: all 6 prompt sentences and all 107 SQL statements (78 inserts, 29 updates). That covers Slack 11 inserts and 7 updates, Gmail 6 threads and 6 messages, GCal 4, Drive 4, Docs 1, Slides 1/3/3, Sheets 1/2, GitHub 3 review comments, 1 review and 1 timeline event, Linear 30 comments and 21 updates, Trello 1 action and 1 card update.
`hg.py lint --sql`: 0 FAIL, 0 CHECK, 0 INFO.

I tried to break every injected record against its base. I found no contradiction that changes a value, set, order, recipient or destination the answer is graded on.

## Findings

All five are advisory. Under the deep_recheck main-session rule, an item stays advisory unless the record changes a graded value, set, order, recipient or destination. The main session should open DR1 to DR3 first, because a strict reader could argue those up: DR1 as an unresolved reference, DR2 on the State / Lifecycle "related records" wording, DR3 as a Semantic conflict inside one injected deck.

`DR# | pass | checklist section | quoted prompt sentence | record path, id and quoted value | Eval dimension | severity`

**DR1** | P2 | Data exists / referential | "What he wants in it is in his message, and his working rules for building it are in the brief he shared with me."
- Side A: SQL line 160, github_review_comments `harmonygames-Games/match3d#472#rc_1`: "the Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change."
- Side B: match3d HEAD 0ff577550e, `Assets/Scripts/LiveOps/SeasonPass/SeasonPassResponse.cs:8`: `[JsonProperty("end_time")] public DateTime EndDate;`. `git grep -i` for October, "oct N" and "premium strip" over `.cs`, `.prefab`, `.unity` and `.asset` returns nothing, and backend `git grep -i` for october/november returns nothing.
- The season end comes from the server, and no date-range field or "strip" object is findable in code. The nearest assets are `Assets/Sprites/Season Pass/bg - golden stripe.png` and `bg - cell golden stripe.png`, which are 130-byte pointers, so the art cannot be read and absence is not proven.
- This is an untraceable note, not a contradiction.
- Cross-Service Coherence | advisory. It would become a finding only if the sprite turned out to carry no date.

**DR2** | P2 | State / related records | "If a beat ends up held, leave a note on its ticket so the owner picks it up."
- Side A: post-SQL Linear ZOM-543 "Queue Manager" is `In Progress`. SQL line 182, `cmt_zom543_1`, 2025-09-30T16:20:37Z: "Queue manager is in progress. Adding panel-order entries as each live-ops feature lands".
- Side B: trello/data.json card idShort 63 "Queue Manager", action 2025-09-30T16:40:22Z, `updateCard`, `{"dueComplete": true}`, old `{"dueComplete": false}`.
- At the clock the roadmap card is complete and the ticket is open. The mismatch is in the base, since both statuses pre-exist. The injected comment explains the ticket staying open, and it sits 20 minutes before the tick.
- No beat, window, push or owner reads either status. ZOM-526 cmt_3 settles the Collect & Win part: "Collect and Win tokens go through the queue manager now (#472)."
- Cross-Service Coherence (State / Lifecycle wording, related records) | advisory.

**DR3** | P2 | Semantic, one artifact | "the four buy weeks that start Monday the 6th"
- Side A: SQL line 137, slide_b83e51a09d72: "Small scale at first, scaled up week by week if the cohorts hold."
- Side B: SQL line 140, slide_0c47d2e81b6f: "Once the stores approve we start buying users at small scale and hold the spend there until the pivot call."
- Slide 1 also says "Scaled beta-cohort buy". The lines reconcile if scale-up comes only after the pivot call, but no record dates that call. Frederick's calendar through Oct 14 shows no pivot event.
- The deck supplies only the week list to the calendar. Any spend posture in the recommendation is a P1 question.
- Cross-Service Coherence (Semantic) | advisory.

**DR4** | P2 | Known base card SC-13 | "Frederick messaged me yesterday asking for the live-ops and push calendar for the Zombie Match 3D beta"
- Side A: SQL line 253, Trello action 68dac8204f1e9a3b7c2d5e61: `"list":{"id":"6851a674975da1fe76e70d93","name":"BETA: Sep 30"}`.
- Side B: trello/data.json list 6851a674975da1fe76e70d93: name "BETA: Oct 10".
- The injected action follows every base action on that list, so it repeats the known SC-13 mismatch and adds nothing new.
- No graded fact uses the list name. The beta span comes from Frederick's message and the brief.
- Cross-Service Coherence (Referential) | advisory.

**DR5** | P2 | Rule with no triggering record | "his working rules for building it are in the brief he shared with me"
- Side A: SQL line 115, brief: "An unresolved change-request review blocker on an in-scope live-ops PR from that cohort does hold it."
- Side B: github/data.json `reviews`: since 2025-06-01 only three rows have state CHANGES_REQUESTED, match3d-backend#4 (2025-06-06, 2025-06-10) and match3d#303 (2025-07-16). Both PRs are merged. No Aug-Sep row exists in any repo. A search of Confluence and Slack (Jun-Oct 2025) finds no definition of "Aug-Sep live-ops cohort".
- The rule is inert for holds, which is not an inconsistency. The undefined term is a P1 clarity lead.
- Data exists | advisory.

## Per topic

| Topic | Result |
|---|---|
| Cross-Service Coherence | No finding at fail or low-impact level. DR1 to DR4 are advisory. No status contradicts its own record's activity. No hidden-record case. |
| Feasibility | No finding. All asks map to cataloged tools (table below). No open instruction, so the 15-item scope rule does not apply. No per-X breakdown lacks a field. |
| Persona access | No finding. Every required scoped read is visible to julia.lawson@harmonygames.co (table below). |
| Data exists | No finding. Every needed fact has a record. DR5 notes a rule with no matching record. |
| Tool use and cross-service | No finding. Each service below changes a graded fact. |
| Hidden records | None. No channel_leave for Julia, Robert, Vincent or Leonard in the channels used. Brian's mails sit in all three mailboxes (Brian, Julia, Frederick). The GCal event has a copy on all four attendee calendars. |
| Derived columns | None. The answer reads no Snowflake table. Tag FD-3785 not used. |
| Date-slip severity | No finding. Every weekday and date in injected text checks out (list below). |
| Platform defects | No PLATFORM:FD-2880 or FD-3785 hit. Anonymized-token note: PNs Beta rows 7 and 14 carry `[PERSON_NAME_2549]` in the English copy. This is the source string; do not score it. |

## Section 3 lines

- Two services: see the drop test below. Slack and Gmail alone already change graded facts, and six more services do too.
- Hidden record: none.

| Service | Record | Graded fact that changes if dropped |
|---|---|---|
| Slack | Frederick DM D05SD5QLG94; Robert DM D05GU6L0XFH 669d15f6; Vincent C0880U9751A b5f2955c | Ask and row scope; Halloween off the calendar; Weekly Leaderboard hold |
| Docs | Brief f_7c3e91a4d2b85f60e1a9c4 | All rules |
| Sheets | Push Notifications Zombie Match, tab PNs Beta; f_e4a17c90b3d25f6a8c1d73 | Push send/hold; destination |
| GCal | evt_5c1e83a7d94b02f6c8e31a, 2025-10-08 15:00 UTC | Collect & Win first window |
| GitHub | #470 rc_10; #468 rc_38; #472 rc_1; CDK stack | Which windows wait on the release; vial and strip still-to-do; cadences |
| Gmail | Brian's Sep 22 and Sep 26 mails | Committed date; reply target |
| Confluence | page_season_pass_spec: "locked 24h before each season opens"; page_liveops_calendar | Lock instant; Product approval; Collect & Win name |
| Linear | ZOM-429, ZOM-465, ZOM-78 | Hold ticket and owner; icon animation; calendar ticket |
| Trello | Card 61 comment | Quests still-to-do decoy |

## Feasibility table

| Ask | Capability | Status |
|---|---|---|
| Read Frederick's message and thread reply | slack_read_thread, slack_conversations_replies | SUPPORTED |
| Read the brief | gdocs_get_document_text | SUPPORTED |
| Fill the sheet | gsheets_values_update (Calendar 200x9, Pushes 200x7, Julia is owner) | SUPPORTED |
| Note on a held beat's ticket | linear_create_comment (ZOM-429, assignee Douglas) | SUPPORTED |
| Link the sheet on the ticket | drive web_view_link present; linear_create_comment on ZOM-78 | SUPPORTED |
| Send the recommendation | slack_send_message to D05SD5QLG94 | SUPPORTED |
| Brief's mail reply | gmail_reply_to_message; id shape `user/<Message-ID>` matches base | SUPPORTED |

Evidence limit: the catalog gives tool names and parameters only, so return rendering is unverified.

## Persona access table

| Required read | Service | Basis | Verdict |
|---|---|---|---|
| Frederick DM | Slack | Julia in members; D05SD5QLG94 | Visible |
| Robert retraction DM | Slack | Julia in members; D05GU6L0XFH | Visible |
| Halloween thread, #zombie-art | Slack | Member, joined 2025-05-06, no leave | Visible |
| Vincent retest, #zombie-match3d | Slack | Member, joined 2025-01-12, no leave | Visible |
| Leonard and lightSweep replies, #zombie-bugs | Slack | Member, joined 2025-05-06, no leave | Visible |
| Brian's two mails | Gmail | Julia's mailbox copies in INBOX | Visible |
| Release event | GCal | Own calendar copy | Visible |
| Brief and UA deck | Docs, Slides | shared_with Julia, reader | Visible |
| Calendar sheet | Sheets | Owner | Visible |
| Push sheet | Sheets | Shared with Julia, domain | Visible |
| GitHub, Linear, Trello, Confluence | Unscoped | acl.md matrix | Visible |

Julia is not in #zombie-prs, but no answer needs it: the mirrors repeat GitHub, which is unscoped. Brian's private `[live-ops] ZM collect&Win.docx` and #zm-collect-win are also not needed, since ZOM-566 and the brief carry the content.

## Checked and consistent

**Slack**
- All 11 ts values match created_at. No id or ts collision. Every parent id exists exactly.
- Reply counts follow base plus one. a3e78e82 has 4 users (Julia, Claire, Martin, Robert).
- All authors are channel members.
- Robert's desert/port reply (16:41:08) follows Martin's port post (16:27:07).
- lightSweep: Vincent's 21:46:15 note follows commit 25c6c66b6b (21:20:26Z), which changes `lightSweep Box Variant.mat`.
- Martin's Halloween parent 2025-09-17 is intact. "Martin's thread" resolves.

**#zombie-prs mirrors**
- Commenter-in-pretext convention matches base. Times are +2s. discussion_r numbers are monotonic.
- #470 and #472 mirrors sit before the base "Review approved" and "merged" posts.
- The 4b7c4127 attachment update differs from base only in Reviewers. Thread counts are correct.

**GitHub**
- All three notes sit before merge: #468 15:36:41 vs 16:13:50; #470 15:51:06 vs 15:51:15; #472 15:52:58 vs 15:53:04.
- rc and rev numbers extend base with no collision. rc_10 and rc_1 attach to Arthur's real APPROVED reviews at the same second.
- ev_6 uses #468's head_sha. Files are in the PRs.
- Null commit_id and line match all 1,387 base rows. 53 base rows also have an empty diff_hunk.

**"DEV stack only" against base**
- Confluence: "not yet live".
- Owen, 2025-09-26: "Igual no va para release ahora".
- CDK prod schedules for leagues, Plague Race, Endless and Season Pass exist.
- Douglas's Sep 16 "Deployments are done" names no Collect & Win. No record says it reached prod.
- Prod state itself is not in any export.

**Linear lifecycle after UPDATEs**
- ZOM-432: Done, completed_at equals the closing comment. #471 merged, its commit "Fixing UI Elements on Daily Gift" exists, and iOS Submission #50 and Android Submission #135 are in #builds before 21:07:26Z.
- ZOM-563: Done. Douglas's 18:16:33 prod update and Vincent's 21:58:44 "Yep it works as expected" come first.
- ZOM-566: In Progress. started_at 17:20:13 precedes both comments and PR #477.
- ZOM-344: Done with null started_at, as on 120 of 427 base Done tickets.
- ZOM-521: checklist untick matches ZOM-526 and ZOM-528 In Progress.
- updated_at equals the last comment on all 21 updates. ZOM-429 correctly stays at the later base value. No comment predates its issue.

**Linear notes against code and Slack**
- ZOM-465: animated icon sets exist for Endless, Plague Race, Quests, Season Pass, Zombie Lane and Boss. None exists for Collect & Win.
- ZOM-543 flow matches QueueManager.cs lines 52 to 58.
- ZOM-549: total_equipped_power is sent only on endless and boss events, not left_level.
- ZOM-534: commit 47c65623e7 "sync quests end with client"; quests cron is MON 00:00.
- ZOM-442: trophy_level and chest_content are in code.
- ZOM-471: Leonard's "we don't need it! cancel the ticket" and Vincent's "it already has start button".
- ZOM-565: Marcus's commit 44988da015 is at 14:33:08Z, the comment at 14:34:12Z, and his DM "i wrote a comment on the linear task" at 14:34:25Z. Brian's list has "P1/P2 – Endless mode remaining VFX".
- ZOM-566: Brian's "Analytics and name changes first".
- ZOM-544 matches Vincent's Sep 25 sync list. Branch name "Marcus/..." matches merge messages; the export shows marcus.bennett/EndlessMode_Vfx, an anonymization artifact.

**Weekly Leaderboard**
- No git commit or ticket fixes the rollover.
- Sep 22 "cannot participate" was a different revert, confirmed fixed that day.
- ZOM-429 description matches Vincent's retest.

**Vials**
- Claire's commit a4872cfbec "Collect&Win Items" is the first pass. No later model record exists.

**Gmail**
- Thread ids decode to the message instant. internal_date, Date header (+0300) and mbox_from agree.
- Labels and X-Gmail-Labels pairs follow base patterns for sent and received mail.
- Base id, thread_id and user_email shapes match. Snippets are body prefixes.

**GCal**
- 15:00 UTC is 18:00 Istanbul. Distinct event_ids, shared `@hg4` ical_uid, self and organizer flags are correct.
- Missing invite mail is normal: Julia's mailbox holds no invitation mail after 2025-06.

**Drive family**
- Id shapes, parents (real root folders), `.docx`/`.xlsx` names with google mime, and drive_file_id equal to document id match base.
- web_view_link format matches base. All nine brief style_run offsets land on their headings.

**Trello**
- Action id prefix decodes to 2025-09-29T17:55:44Z. Badge comments is 1. dateLastActivity is updated.
- Member is Leonard. "Mon Oct 13" is a Monday and matches the weekly quest cron.

**Base facts behind the brief**
- Season Pass on the 1st at 00:00 UTC (spec, CDK, Douglas Sep 30).
- Collect & Win Mon-Tue, Wed-Thu, Fri-Sun (Confluence; Douglas "2 días, 2 días, 3 días").
- Zombie Lane has no schedule (CDK, zombie_lane.ex, Confluence "Permanent").
- Robert is Product (spec "Owner: Robert (Product)").
- Four named push rows exist. Translated tab is Domino copy.
- Unity retention campaigns are separate (Frederick Sep 30).

**Dates**
- Oct 6, 13, 27 Mon; Oct 8, 29 Wed; Oct 31 Fri; Nov 1 Sat; Nov 2 Sun; Sep 22 Mon; Sep 26 Fri; Sep 30 Tue.
- Oct 31 10:00 Istanbul is 07:00 UTC, after the Oct 31 00:00 UTC lock.
- Nothing seeded sits after the clock except the future Oct 8 event, which is a future plan created Sep 24.

**Also checked, no effect on any record**
- Two Sep 30 Vincent lines sit in DMs Julia cannot read, and the answer needs neither. "Kill zombie quests don't work" (D05QQ7YQTND) is one line of a QA list that names no build or prod. "quest point not found" (D0770ET1HV2) is his example of a console log that does not reach crash reporting, not a claim-failure report.
- ZOM-525 and ZOM-521 "[X] Live-ops icons" against the Collect & Win icon note: different work, and Marcus's note covers the timing.

## Evidence limits

- Sprite PNGs in the repo are pointers, so art content is unread (DR1).
- Prod deployment state exists only as human statements.
- Tool return rendering is unverified.
