# Deep recheck P2: services, data and access

Task: Julia Lawson, ZM3D beta live-ops and push calendar. Clock 2025-10-01 00:00 PT (07:00 UTC).
Blind pass. Checked only P2 topics: Cross-Service Coherence, Feasibility, Persona access, Data exists, Tool use and cross-service, including hidden records, derived columns and date-slip severity.

## Summary

- No fail-level finding is established. No hidden record, no missing tool, no date slip, and no derived column is in the answer path.
- 4 findings, all low-impact as I read them. DR1 and DR2 carry an explicit escalation condition, stated in each entry. DR3 and DR4 change no graded value unless the Oracle Events or rubric require a dated hold or an exact URL.
- 5 advisory notes, none scored.

## Coverage

- Prompt: 6 of 6 sentences.
- Incorporated sources: 37 of 37 sentences (Frederick's DM 6, his thread reply 5, the working-rules brief 26).
- Injected records: 98 of 98 (72 INSERT rows, 26 UPDATE statements).

| Service | Rows |
|---|---|
| Slack | 8 INSERT, 4 UPDATE |
| Gmail | 6 threads, 6 messages |
| GCal | 4 |
| Drive | 4 |
| Docs | 1 |
| Slides | 7 |
| Sheets | 3 |
| GitHub | 6 INSERT, 1 UPDATE |
| Linear | 26 comments, 20 UPDATE |
| Trello | 1 INSERT, 1 UPDATE |

Line numbers below refer to `R/inputs/01_Universe_Inject.sql`, where R is the review folder. Base paths are relative to `Universe_SynthCut/`.

## Findings

### DR1

`DR1 | P2 | Coherence (6.8, Injection) | Source sentence, brief "Still to do": "what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it" | SQL line 144 harmonygames-Games/match3d#473#c_2 created 2025-09-30T16:16:33Z vs github/data.json #473 merged_at 2025-09-30T15:41:20Z | Cross-Service Coherence (State / Lifecycle) | Low-impact; escalation condition below`

- Injected side (line 144): "The Season Pass premium strip is still set to the October range. It needs the November range before that season opens, Oliver is taking the date change." Author Arthur, 2025-09-30T16:16:33Z. Lines 146 and 148 add the timeline event and bump `updated_at`.
- Base side, `SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json`:
  - #473 was opened 15:41:05Z and merged 15:41:20Z by its author, Oliver. There is no review on it.
  - `head_ref_deleted` is 2025-09-30T15:41:24Z. The note lands 35 minutes after merge, on a deleted branch.
- Base pattern:
  - In match3d, 0 of 4 human conversation comments and 0 of 29 human inline comments post-date the merge.
  - Arthur's only two match3d conversation comments are CodeRabbit commands (#262, #332).
  - Org-wide, 3 of 95 human conversation comments post-date the close, all in GameOfDominoes:
    - #333: 2024-02-06T17:29:07Z, 9 minutes after merge.
    - #611: 2024-05-09T16:33:26Z, 10 seconds after close.
    - #926: 2024-09-02T16:59:31Z, 41 minutes after merge.
- Why it matters: this comment is the only source of the Season Pass premium-strip still-to-do and its owner, so a graded row rests on it.
- Severity: low-impact. A post-merge note does not contradict the record's merged status, and the base has precedent. Escalation: §3.2 says a closed record with later activity always fails. If the main session reads a merged PR as that case, this becomes fail-level.
- Evidence limit: I could not confirm the claim itself. No "October" or "November" string appears in `Assets/Scripts`, `Assets/Prefabs`, `Assets/Resources` or `Assets/AddressableAssetsData` of match3d at HEAD. The Season Pass sprites are 130-byte LFS pointers, so a date baked into art cannot be inspected. No record contradicts the claim.
- Fix: move the note to a record that is still open when it is written, and keep the owner and the October-to-November content. #473 cannot take a pre-merge comment, because it was open for only 15 seconds.

### DR2

`DR2 | P2 | Coherence (3.2) | Source sentence, brief "Still to do": "Not what already shipped, not analytics, not polish nobody flagged." | SQL line 224 cmt_zom542_1 vs linear/data.json ZOM-542 state_id "Regression" | Cross-Service Coherence (State / Lifecycle) | Low-impact; escalation condition below`

- Injected side (line 224, Samuel, 2025-09-22T18:40:21Z): "Not in the build yet: the home screen and victory score changes for endless and boss arena are still at the mockup stage."
- Base side, `SynthCut_HarmonyGames_Other_Services/Services_Data/linear/data.json`: ZOM-542 has `state_id` "Regression", `started_at` null, and `updated_at` equal to `created_at` (2025-09-14). Line 225 updates only `updated_at`, so the state stays Regression.
- The issue: a status of Regression sits on a ticket whose own comment says the work never reached a build.
- Severity: low-impact. The state predates the SQL, ZOM-542 is a decoy that changes no graded value, and "Regression" is thinly defined here. Only 4 issues hold that state, and ZOM-542 entered it at creation. Escalation: §3.2 says a State / Lifecycle inconsistency always fails. If the main session treats this as a status contradicting activity, it is fail-level.
- Fix: either move ZOM-542 out of Regression in the same UPDATE, or reword the comment so it does not assert the work was never built.

### DR3

`DR3 | P2 | Section 3 data / 6.8 Missing fact | Source sentence, Frederick's DM: "Every beat players can see in those weeks: which windows it runs in, if anything is held and until when" | SQL line 132 header "Hold until (UTC)"; linear/data.json ZOM-429 due_date null, cycle_id null | Data exists / Feasibility | Low-impact; fail-level only if a dated instant is required`

- The only beat that meets the brief's hold test is the weekly leaderboard: Vincent's retest on line 19 ("I killed the app and reopened it twice ... my week is still last week one").
- No record gives an end date for that hold:
  - ZOM-429 is Backlog with no due date and no cycle.
  - The Oct 8 release (lines 82 to 88) covers only "server windows that are still on the DEV stack".
  - I found no leaderboard fix in any PR, commit, Slack message or mail.
- A careful run can only answer with a condition, meaning until a fix is verified on prod, with no date on record. That is a truthful answer. The brief itself uses a non-dated "until" ("off this calendar until the pivot call"), and the prompt's "leave a note on its ticket so the owner picks it up" fits an open-ended hold.
- Severity: low-impact provided a stated condition is accepted. If the Oracle Events or rubric require a UTC instant in "Hold until", no record supplies one and it is fail-level (Data exists).
- Fix: either keep every graded check on this cell condition-based, or add a dated, persona-visible record for the fix.

### DR4

`DR4 | P2 | Tool use / feasibility | "Once the sheet's done, link it on the calendar ticket" | SQL line 130 web_view_link NULL for f_e4a17c90b3d25f6a8c1d73 vs gdrive/data.json | Feasibility (Identifier / Format) | Low-impact`

- The injected calendar sheet has `web_view_link` NULL.
- In `gdrive/data.json`, 11 of Julia's 12 owned spreadsheets carry a link. The exception is `Rewind_.xlsx`.
- The explicit ask is to link this sheet, and no URL exists on its record. An agent can only build one from the spreadsheet id or cite the title and id. Catalog parameters do not show what `gdrive_get_file_metadata` returns, so tool output is an evidence limit.
- Severity: low-impact. The ask remains doable. It matters only if a check expects one exact URL.
- Fix: populate `web_view_link` on the sheet row, in the base's form for Drive files.

## Advisory notes (not scored)

- A1, deploy owner. The Sep 29 POD notes (`gmail/threads/frederick@harmonygames.co_1844625522638279032.json`) say "[PERSON_NAME_0612] will help Leonard Hayes to deploy the win and collect to pro servers". The injected release event has Douglas as organizer and does not invite Leonard. That mail is not in Julia's mailbox, so the owner she can read is Douglas. The token-to-name mapping is unproven, and no date conflicts.
- A2, Sep 30 prod update. Douglas told Vincent in DM D079SNE2TL4 at 18:16 UTC, "I updated the prod environment with the latest teams/social changes". That is 2.5 hours after Arthur's "next backend release" note. It is not a conflict: it names only teams/social, the Architecture page runs Nakama as "its own Fargate service", and Owen's Sep 26 "Igual no va para release ahora" supports the windows not having shipped. Julia cannot read that DM.
- A3, timeline order. `#468#ev_6` (line 142) is `reviewed` with null `created_at`, and it sorts after `merged` (ev_4) and `closed` (ev_5), although the review was submitted 37 minutes before merge. The shape matches base `reviewed` events, and a new id cannot sit earlier.
- A4, UA deck. Slide 2 says "scaled up week by week if the cohorts hold"; slide 3 says "hold the spend there until the pivot call". They reconcile if scaling follows the call. No calendar event dates the pivot call, and the answer does not need one.
- A5, Queue Manager. Calvin's ZOM-543 comment (line 173, 16:20:37Z) says "Queue manager is in progress", and ZOM-543 stays In Progress, while Leonard marked Trello card 63 complete at 16:40:22Z. Base Linear lag of the SC-16 kind. Not graded.

## Topic results

- Cross-Service Coherence: DR1 and DR2. No other inconsistency found.
- Feasibility: no fail-level finding. DR3 and DR4 are low-impact.
- Persona access: no finding.
- Data exists: no finding beyond DR3.
- Tool use and cross-service: no finding beyond DR4.
- Hidden records: no finding. Hidden-record line: none.
- Derived columns: no finding. No Snowflake table is in the answer path, and a Snowflake search for "Collect & Win" returned 0 matches with `scan_complete` true.
- Open-instruction scope: no finding. No fix-whatever-is-wrong instruction exists. The beat and push inventory is about 10 beats plus 10 push rows, not mismatches between sources.
- Date-slip severity: no finding. No wrong date or year in any record the answer relies on.
- Platform defects: none.

## Section 3 lines

**Two services.** Each of these changes a graded fact:

| Service | Graded fact it changes |
|---|---|
| Slack | Vincent's retest flips the leaderboard to held, against Douglas's Sep 16 "not blocking". Robert's DM removes Halloween. |
| GCal | The Oct 8 15:00 UTC release moves Collect & Win's first window to Fri Oct 10 00:00 UTC. |
| Gmail | Brian's correction replaces Oct 29 with Oct 31 07:00 UTC. |
| Confluence | The 24h lock falls at Oct 31 00:00 UTC, so the new date misses it. |
| Sheets | The PNs Beta statuses and copy decide each push. |
| GitHub | Which windows are DEV-only, plus the vial and premium-strip still-to-dos. |
| Linear | Icon animation still-to-do, the closed ZOM-432 and ZOM-344, and the ticket targets. |

**Hidden record.** None. Each required scoped read was checked for Julia:

| Record | Basis |
|---|---|
| D05SD5QLG94, D05GU6L0XFH | EMPLOYEE_0005 is a member |
| #zombie-match3d, #zombie-art | Member, with `channel_join` and no leave |
| Brief, deck | Shared as reader |
| Calendar sheet, ZM Live Ops folder | Owner |
| Push Notifications Zombie Match | Shared, domain visibility |
| GCal event | Copy on her own calendar |
| Both Brian mails | In her mailbox, and in Brian's and Frederick's |

Julia is not in #zombie-prs, but the mirrors are not required because GitHub is unscoped. Oliver's and Brian's private sheets are not needed.

## Feasibility

| Ask | Capability | Status |
|---|---|---|
| Read DM, brief, deck, push sheet | `slack_read_thread`, `gdocs_get_document_text`, `gslides_get_presentation_text`, `gsheets_values_get` | Supported |
| Read PR notes, CDK schedules | `github_get_pull_request_comments`, `github_get_pull_request_reviews`, `github_get_file_contents` | Supported |
| Write the sheet | `gsheets_values_update`, `gsheets_values_append` | Supported |
| Note on held ticket, link on ZOM-78 | `linear_create_comment` | Supported |
| Recommendation to Frederick | `slack_send_message` | Supported |
| Reply on Brian's mail (brief rule) | `gmail_reply_to_message` | Supported |

Dimensional check: both status fields ("Status" and "Status (NA, WIP, LIVE)"), the copy, and the When field all exist on PNs Beta. The four rows Frederick excludes are rows 3, 9, 11 and 12, leaving 10.

## Checked and consistent

**Slack**
- Every author is in the target channel. Ts values match `created_at`, and no id or ts collides.
- Thread counts are right: #470 16 to 17, #468 41 to 42, #473 2 to 3, the Halloween parent 0 to 1.
- `latest_reply` values are right. The attachment rewrites changed only the Reviewers value on #468 and the Comments value on #473.
- #468's Reviewers change matches the base pattern, because #470 also lists Arthur with no `review_requested` event.
- Mirror `pretext`, discussion ids and issue-comment ids follow the base order.

**Gmail**
- All 6 thread ids decode to the send time (`id >> 20` equals `internal_date`).
- Headers, the +03:00 offset, `Label_b19fb8d1b3` (Opened), Sent and Archived label sets, and the per-mailbox id shape match the base.
- All three mailboxes hold both mails.

**GCal**
- Event id and uid shapes match, and no id collides. There are 4 copies for 4 attendees, and the `self` flags are right.
- 18:00 Istanbul is 15:00 UTC, and Oct 8 is a Wednesday.

**Drive, Docs, Slides, Sheets**
- Ids and parents resolve, and `.docx` and `.xlsx` naming matches the base.
- All 9 `style_runs` offsets land on the brief's headings. Sheet headers have 9 and 7 columns.

**GitHub**
- rc_10, rev_3, rc_38, ev_6, c_2 and ev_5 are free ids. rc_10 shares the timestamp of Arthur's real approval, rev_9.
- rc_38 is pre-merge, and GameLoader.cs is in #468. Commit 648e2c7b is #468's head, present in `commits` and `commit_map`. Empty `diff_hunk` has base precedent (53 of 1387).
- "Vial" matches `collectAndWinVial` in code. Claire authored the Collect&Win items on Aug 8.

**Linear**
- All 10 authors exist. `updated_at` never regresses.
- Done with null `started_at` has precedent (907 tickets).
- PRs #471, #472 and #475 merged before the comments citing them. iOS 50 and Android 135 appear in #builds on Sep 30.
- ZOM-471 matches Leonard's "we don't need it", and ZOM-504 matches the bot-only repro in DM.
- ZOM-565 matches the base mail "mentioned you in a comment" on Sep 29.
- ZOM-465 matches PRs #454 and #456, which list no Collect & Win icon.
- The ZOM-442, ZOM-552 and ZOM-566 parameters and tabs exist in the Firebase dictionary.

**Linear notification mail**
- The mails that exist for touched tickets conflict with nothing.
- The SQL adds no comment or status mails of its own. That is a gap, not a contradiction.

**Trello**
- The action id's timestamp decodes to 2025-09-29T17:55:44Z, the author is Leonard, and the badge and `dateLastActivity` updates are right.
- The list name in the action matches later actions (SC-13, not relied on).

**Code and Confluence agree on every value the answer needs**
- `zombies-game-cdk-stack.ts` gives Collect & Win 2, 2 and 3 day groups, Season Pass on the 1st at 00:00 UTC, and Leagues and Endless weekly on Monday 00:00 UTC.
- Douglas's Sep 25 "prod -> 2 días, 2 días, 3 días" and the Confluence calendar agree.
- The Season Pass spec names Robert as Product and sets the 24h lock, and the calendar page reconciles the lock as "a process control". No value the answer needs conflicts in Confluence.

**Dates**
- All weekdays are correct. Oct 31 10:00 Istanbul is 07:00 UTC, after the Oct 31 00:00 UTC lock.
- The latest injected record is 2025-09-30T22:10:41Z, before the clock. Oct 8 and later dates are future events.

**Known base issues touched, none load-bearing except as noted**
- SC-13 (list name).
- SC-15 (the SQL repairs the ZOM-521 checklist with a comment trail).
- SC-38 (analytics is excluded by the brief, and the ship date is not used).
- SC-62 (import cadence is not needed).
