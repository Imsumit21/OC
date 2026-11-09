# Injection review C1: chronology, relationship and lifecycle half of Check C

**Result: PASS.** 145 of 145 data statements reviewed, none sampled. Demonstrated defects: 0. Advisories: 6. PENDING checks: 0.

- SQL: `Task_Authoring/task_inputsK/01_Universe_Inject.sql`, sha256 `0c1cf21627d5d9fb6303127c005cbaab216522c5ba1bf25a1e04573a44d24dad`, 147 statements (BEGIN, 137 INSERT, 8 UPDATE, COMMIT).
- Review version: `injection-static-v2`.
- Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).
- Base: `hg4-synth-sep30cut` v16, archive sha256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c`.
- Lint (`hg.py lint`): 0 FAIL, 0 CHECK, 0 INFO.
- Scope: this half only. Factual claims in text and Checks A and B belong to other reviewers.

SQL line numbers below are the line of the `INSERT` or `UPDATE` keyword. `parse_sql`'s own `line` value points at the section comment for the first row of a section, and it returns `None` for the literal `false` and leaves `E''` escapes undecoded. I checked those cases against the raw SQL.

## 1. Result by check

| # | Check | Result | Basis |
|---|---|---|---|
| 1 | Clock and agreement within each record | PASS | 290 ISO stamps across all statements: earliest 2025-06-26T20:58:14Z, latest 2025-09-30T20:40:51Z, none after the clock. No plan field is later than the clock. Slack `ts` equals `created_at` on 6 of 6. Trello id time equals `date` on 3 of 3. Gmail `internal_date`, `date` and header Date agree on 5 of 5. All 4 new thread ids decode to the first message time. Drive, Docs, Sheets and Slides stamps agree. GCal: created, then updated, then start, then end, on 2 of 2. Linear: created, started, completed in order on 34 of 34. `submitted_at` equals `created_at` on rev_7 and rc_18. |
| 2 | Replies, children and cited records follow their causes | PASS | Section 6 timeline. All 3 Slack replies follow parents in the same channel. All 32 children are created after DES-314. All 67 comments follow their issue. Every cited record existed when cited (section 3). |
| 3 | Parent counters and companions | PASS | Section 4 and section 5. Advisories A1, A2 and A5 cover companions that no rule requires. |
| 4 | State and lifecycle | PASS | Section 5. |
| 5 | Before and after values | PASS | Section 4. All 8 UPDATEs move forward, and nothing held by the base is lost. |
| 6 | Sibling consistency | PASS | Section 3. |

## 2. Demonstrated defects

None.

## 3. Citations and siblings checked

Each cited record against the moment it is cited:

| Citing record | Cites | Cited record's time | Result |
|---|---|---|---|
| L64 mail, L80 rc_18, L82 rev_7 (2025-06-26T20:58:14Z) | PR #248, open | opened 15:43:34Z, merged 21:23:32Z (`/pull_requests/2128`) | Before Arthur's APPROVED at 21:23:25Z, which fits "Fine to merge" |
| L58 and L62 mail (09-15T13:05:48Z) | Phone message checks sheet | created 09-15T12:51:17Z (L11) | Sheet is 14 minutes older |
| L28 deck text (09-19T18:30:26Z) | 6 Ready on the PN sheet | base sheet modified 2025-06-23, 6 Ready on tab PNs Beta (`/sheets_spreadsheets/220/sheets/1/grid`) | Holds |
| L95 DES-314 (09-23T16:40:12Z) | PNs Beta tab | as above | Holds |
| L167, L171, L175, L183, L189 and sheet L19 (09-24) | Android 0.3.127, iOS 0.3.40 store builds | Android published 09-22T21:04:40Z (`C07C2866011/2025-09 /908`); iOS released 09-23T16:02:13Z, version 0.3.40 (`D06477JGUKT/2025-09 /183`, `/186`); both set as required versions 09-23T16:02:45Z (`C0880U9751A/2025-09 /407`) | Builds are older than every pass |
| L11 sheet modified 09-24T15:00:05Z | Vincent's passes | last pass comment 14:50:51Z (L179) | Sheet is saved after the last pass |
| L14 doc (09-26T17:10:54Z) | DES-314, Vincent's QA note, ZM ROADMAP board | 09-23, 09-15, base | All older |
| L291 (09-26T13:27:41Z) | "the weekly board ping Robert filed", Arthur's local timer view | DES-330 filed 09-24T15:58:47Z, Arthur's comment 09-25T21:24:41Z | Both older |
| L293 (09-26T14:08:12Z) | "once this is fixed" on ZOM-556, Arthur's view | ZOM-556 is Todo in base and no fix found; Arthur's DES-338 comment 09-25T22:06:07Z | Holds |
| L143 DES-338 description (09-24T22:08:49Z) | DES-322 | created 09-23T16:56:55Z | Older |
| L31 Brian (09-26T18:02:19Z) | readiness deck | 09-19 | Older |
| L33 Robert (09-29T17:40:08Z) | "Leonard's right that we need PNs for retention" | Leonard, 09-23T20:41:40Z (`C07C2866011/2025-09 /968`) | Older |
| L37 Leonard (09-29T18:05:29Z) | "taken over" push | base sheet row and match3d #248 hunk | Older |
| L40 Vincent (09-29T19:40:46Z) | "the race one I passed" | L183, 09-24T14:30:22Z | Older |
| L43 Leonard (09-30T20:40:51Z) | DES-314 tickets, rule doc, PN sheet, push notifications card | all older | Last injected event, as a final ask should be |

Sibling records:

| Same fact | Records | Result |
|---|---|---|
| Doc, sheet and deck against their Drive rows | L7 and L14, L11 and L17, L9 and L22 | Title, owner, shares, visibility, created and modified all equal. Doc style run end 1410 equals the decoded body length. |
| Parent folders | L7, L9 in `d_63fffeb4fab5233ed5bb73` (Leonard root, `/drive_files/9030`); L11 in `d_65c76e0b87aa7e9b84d1df` (Vincent root, `/drive_files/9186`) | Each file sits in its owner's folder. |
| QA mail, sender and recipient copies | L58, L62 | Identical except id, thread, mailbox and labels (INBOX against SENT). Snippet is the first 140 characters of the normalised body on all 5 mails and equals the thread row on all 4 new threads. |
| Lapsed ladder review | L75, L77, L68, L72 | Both calendar rows match except event id, calendar and the `self` flag. `created` equals the invite time, `updated` equals the cancel time, and the Meet link, title, attendees and time agree. 10am El Salvador is 16:00Z, and Samuel's calendar zone is America/El_Salvador. |
| PR #248 review | L80, L82, L64 | Body is quoted verbatim in the mail, all three at 20:58:14Z. Review id 2963610417 falls between base 2963243580 (19:04Z) and 2963696884 (21:21Z). The author is Arthur (`merged_by_login`), and Samuel is the PR author, which fits "you authored the thread". |
| Vincent's passes | Sheet L19 against L167 to L189 | Versions, the Plague Race "iPhone" entry and the settings note match. |
| Linear relations | DES-330 and L295, DES-338 and L296 | Both sides present, in the base `{target, type}` shape. |

## 4. Before and after for every UPDATE

| SQL | Record | Column | Before (base) | After | Check |
|---|---|---|---|---|---|
| L39 | `a3e78e820b9f880ef4e3d941562110df` (`C08R8CHB0QL/2025-09 /255`) | reply_count | 3 | 4 | Replies /257, /258, /259 plus L37 |
| | | reply_users_count | 3 | 4 | Base repliers 0005, 0009, 0033, plus 0038 |
| | | latest_reply | 1759161266.305589 | 1759169129.445834 | Equals L37 `ts`, the newest reply |
| L42 | `c42902df5f54c75c1a6e3529cd25121c` (`D06UFE81RF0/2025-09 /24`) | reply_count | 0 | 1 | L40 |
| | | reply_users_count | 0 | 1 | Vincent |
| | | latest_reply | null | 1759174846.723833 | Equals L40 `ts` |
| | | thread_ts_legacy | null | 1759163970.141449 | Own `ts`, the base shape for a thread root |
| L48 | Card 7 `6851a769c65dc0017a227bb7` (`/cards/705`) | dueComplete | true | false | L46 action records the reopen, same shape as the 12 base reopens |
| L51 | Card 7 | badges_json | comments 1, dueComplete true | comments 2, dueComplete false | Other 14 keys unchanged; 2 commentCard actions exist after L49 |
| | | dateLastActivity | 2025-06-30T16:51:19Z | 2025-09-24T16:00:39Z | Equals L49, the last action |
| L54 | Card 79 `68d1eb90bef538c7c5c5599d` (`/cards/802`) | badges_json | comments 0 | comments 1 | Other 15 keys unchanged |
| | | dateLastActivity | 2025-09-23T00:36:35Z | 2025-09-29T20:15:03Z | Equals L52, the last action |
| L295 | ZOM-542 (`/issues/3617`) | relations_json | `[]` | `[{"target": "DES-330", "type": "relates"}]` | Nothing lost |
| | | updated_at | 2025-09-14T22:59:17Z | 2025-09-26T13:27:41Z | Forward; equals L291 |
| L296 | ZOM-556 (`/issues/3632`) | relations_json | `[]` | `[{"target": "DES-338", "type": "relates"}]` | Nothing lost |
| | | updated_at | 2025-09-22T14:44:06Z | 2025-09-26T14:08:12Z | Forward; equals L293 |
| L297 | team_DES | issue_counter | Not in the export; highest base DES number is 312 | 346 | Equals the highest new number; 34 new numbers run 313 to 346 with no gap |

## 5. State and lifecycle

**Linear, 34 issues.**

| State | Issues | Stamps | Result |
|---|---|---|---|
| Done | DES-315 to DES-320 | started and completed set, `updated_at` equals `completed_at`, no comment after completion | PASS |
| In Progress | DES-314 | started set, nothing completed | PASS |
| In Review | DES-313, DES-321 to DES-346 | started set, `completed_at` null, `updated_at` equals the latest stamp | PASS |

- `updated_at` equals the latest of created, started, completed and comment times on all 34.
- Numbers rise with `created_at`, and DES-313 follows base DES-312 (2025-05-07).
- Comment `sequence` runs 1, 2, 3 in time order on all 35 issues with comments.
- DES-314 `updated_at` stays at 09-23T16:41:35Z while children are added later. That matches the one base case where a parent has no later activity: DES-307 kept 19:30:46Z while DES-308 to DES-312 were created after it.
- Team membership: Calvin 09-17T15:02:44Z (first filing 15:20:37Z), Samuel 09-23T16:02:09Z (first assignment 16:40:12Z), Martin 09-23T16:03:31Z (DES-339, 09-25), Oliver 09-23T16:04:18Z (DES-332, 09-24). None of the four has an earlier base issue on DES, so the dates contradict nothing. Leonard, Brian, Robert, Julia, Owen, Arthur and Vincent are base DES members. Brian and Julia are base ZOM members for L291 and L293. All 11 Linear users are active.

**Trello.**

- Card 7 sequence: created 06-17, renamed 06-20, comment 06-23, complete 06-30, reopened 09-24T15:59:52Z (L46), comment 09-24T16:00:39Z (L49). Final state: `dueComplete` false on the card and in badges, comments 2, `dateLastActivity` on the last action. The reopen has its own action.
- Card 79 sequence: created 09-23, position change 09-23, comment 09-29T20:15:03Z (L52). Final state: comments 1, `dateLastActivity` on the last action.
- Both cards, both lists and the board are open. Board `dateLastActivity` 2025-09-30T17:09:07Z is later than all three actions, so it needs no change. Leonard is an active actor on this board (`/actions/5244`).

**Other.**

- PR #248: L80 and L82 fall before the merge at 21:23:32Z, and `updated_at` 21:23:32Z stays the latest stamp.
- L64 sits mid-thread in the base Gmail thread (between 12:04:30 and 14:21:49 PDT), neither first nor last, so the thread snippet needs no change whichever message it reflects.
- Event: cancelled 09-25, a day before the 09-26 start.
- Slack: #zombie-match3d and #zombie-art are not archived, and all five authors are members of the channels they post in. `D06L58XCVKK` is the Samuel and Leonard DM, and `D06UFE81RF0` the Samuel and Vincent DM.

## 6. Advisories (not defects)

**A1. L64: reply columns empty while the headers hold the reply pointer.** `in_reply_to` and `references` are NULL, but `headers_json` has In-Reply-To and References set to `<[SOURCE_ORG_0001]-Games/match3d/pull/248@github.com>`. All 8 base messages in `threads/samuel@harmonygames.co_1836006988541924555.json` fill both columns. `headers_json` also lacks the Cc and Reply-To values that `cc_json` and `reply_to_json` hold. This stays below the FAIL bar: `thread_id` places the row correctly, no value contradicts another, and no contract requires the columns. Smallest fix: set both columns to that value on L64.

**A2. PR #248 has 7 reviews and 6 `reviewed` timeline events after L82.** Base `/timeline_events/9736` to `/9741` hold 6 `reviewed` events for the 6 base reviews. The base tolerates a gap: 1,744 of 1,799 reviewed PRs match, 53 have more reviews than events and 2 have fewer. Optional fix: insert one `github.github_timeline_events` row, id `harmonygames-Games/match3d#248#ev_11`, event `reviewed`.

**A3. rev_7 and rc_18 carry the highest `seq` but are earlier than rev_5, rev_6 and rc_17.** A reader sorting by id or `seq` sees them after the approval, though `submitted_at` and `created_at` put them before it. The numbering has no ID contract, and fixing it would mean renumbering base rows. No fix needed.

**A4. L58 and L62: no copy in the mailboxes of Oliver and Owen.** Both are in `to_json` and have mailboxes (`gmail/users.json`, 1,971 and 1,444 messages). I could not establish a per-recipient copy pattern: my base samples returned calendar mail, and the scans hit their limits. No rule requires the copies. Optional fix: add two INBOX copies and thread rows.

**A5. Gmail mailbox counters unchanged.** The SQL adds 4 messages to Samuel and 1 to Vincent without touching `gmail_users` or `gmail_labels` totals (Samuel 4,504, Vincent 1,367 in `users.json`). I did not test whether those totals are exact, so no mismatch is shown.

**A6. rc_18 `diff_hunk` shows the 19:04Z file state.** The hunk is a verbatim 9,721-character prefix of base rc_16 (`@@ -0,0 +1,537 @@`). At 20:58:14Z the newest authored commit was `819b083d` (19:20:56Z). `commit_id` is NULL and blobs are unreadable, so I cannot show the text differs, and a comment on a slightly stale diff is possible. No fix demonstrated.

## 7. Pre-existing context (not caused or worsened by the SQL)

- **SC-13:** L52 names the list "BETA: Sep 30", matching base actions `/actions/5244` and `/5245`, while the list row says "BETA: Oct 10". The doc says only "BETA list", so no text depends on the date.
- **SC-32:** the 12 base In Review tickets carry `completed_at`. The 27 injected ones do not, so state and stamp agree in the SQL.
- **SC-14 and SC-16:** neither lists card 7, card 79, ZOM-542 or ZOM-556. L48 and L51 keep both complete flags on card 7 in step.
- **Linear export:** `/comments` is empty, although ZOM-542 has attachments with surface `comment`. No base comment can collide with L291, and no state history exists to compare with `state_history_json = '[]'`, which the Eval allows for a new issue.
- **ZOM-542:** state Regression with `started_at` null is base data.
- **Trello card 7:** `dueComplete` with `due` null is base data.

Two readings I tested and did not count:

- L72's note says day 14 is "already covered" a day before Robert files DES-344 (09-26T14:22:31Z). Nothing cites DES-344 and a later ask can ignore an earlier note, so the order is possible.
- L43 says tickets exist for the sheet rows under DES-314, but the Win & Collect row's ticket is parentless DES-313. The same message covers a ticket "under whatever name". This belongs to the fact reviewer.

For the Check B reviewer, not judged here: `linear_teams.issue_counter`, `linear_comments.sequence`, `github_reviews.seq` and `github_review_comments.seq` are absent from the unverified schema snapshot.

## 8. Evidence limits

- Repository blobs are unreadable, so code-state claims rest on PR records and hunks.
- ZOM-556 fix search: complete scans for the exact id over Slack 2025-09 and GitHub `data.json`, plus the base state Todo. A fix that never names the ticket would not appear.
- The base export has no `issue_counter`, so L297's before value is unknown. The check is against the highest base number.
- Live database behaviour and tool ordering are outside this static review.

## 9. Combined timeline

SQL rows plus the base records they touch or cite, in UTC.

| Time (UTC) | Source | Record | Event |
|---|---|---|---|
| 2025-06-17T05:05:57Z | base gsheets /sheets_spreadsheets/220 | PN sheet | created (last modified 2025-06-23T07:02:43Z; tab "PNs Beta", 6 Ready) |
| 2025-06-17T17:35:37Z | base trello /actions/4672 | card 7 | createCard |
| 2025-06-23T16:57:59Z | base trello /actions/4816 | card 7 | commentCard, badge count 1 |
| 2025-06-26T15:43:34Z | base github /pull_requests/2128 | PR #248 | opened by Samuel |
| 2025-06-26T19:04:08Z | base github /reviews/1940 | PR #248 rev_4 | CodeRabbit review; review id 2963243580 in Gmail |
| 2025-06-26T20:58:14Z | L64 | samuel.turner mail | Re: [[SOURCE_ORG_0001]-Games/match3d] Push notification (PR  |
| 2025-06-26T20:58:14Z | L80 | rc_18 | Arthur review comment on PR #248 |
| 2025-06-26T21:21:27Z | base github /reviews/1941 | PR #248 rev_5 | CodeRabbit review; review id 2963696884 in Gmail |
| 2025-06-26T21:23:25Z | base github /reviews/1942 | PR #248 rev_6 | Arthur APPROVED |
| 2025-06-26T21:23:32Z | base github /pull_requests/2128 | PR #248 | merged and closed; updated_at |
| 2025-06-30T16:51:19Z | base trello /actions/4857 | card 7 | dueComplete true; dateLastActivity |
| 2025-09-14T22:59:17Z | base linear /issues/3617 | ZOM-542 | created, state Regression |
| 2025-09-15T12:51:17Z | L11 | Phone message checks | Drive file created |
| 2025-09-15T13:05:48Z | L58 | samuel.turner mail | Phone messages for beta |
| 2025-09-15T13:05:48Z | L62 | vincent.parker mail | Phone messages for beta |
| 2025-09-17T15:02:44Z | L85 | team_DES | Calvin joins Design |
| 2025-09-17T15:20:37Z | L93 | DES-313 | filed by Calvin: Ping when a Collect & Win window opens |
| 2025-09-17T15:25:18Z | L161 | DES-313 | comment by Calvin (cmt_7c6c0222) |
| 2025-09-17T15:51:15Z | L93 | DES-313 | started |
| 2025-09-19T18:30:26Z | L9 | Beta readiness | Drive file created |
| 2025-09-22T14:44:06Z | base linear /issues/3632 | ZOM-556 | created, state Todo |
| 2025-09-22T21:04:40Z | base slack C07C2866011/2025-09 /908 | Android 0.3.127 | published; iOS 0.3.40 in review |
| 2025-09-23T00:36:32Z | base trello /actions/5244 | card 79 | createCard |
| 2025-09-23T16:02:09Z | L87 | team_DES | Samuel joins Design |
| 2025-09-23T16:02:13Z | base slack D06477JGUKT/2025-09 /183 | iOS 0.3.40 | released (version named at /186) |
| 2025-09-23T16:03:31Z | L89 | team_DES | Martin joins Design |
| 2025-09-23T16:04:18Z | L91 | team_DES | Oliver joins Design |
| 2025-09-23T16:40:12Z | L95 | DES-314 | filed by Leonard: Beta player messages |
| 2025-09-23T16:41:35Z | L95 | DES-314 | started |
| 2025-09-23T16:42:38Z | L97 | DES-315 | filed by Leonard: PN: Lives recharged |
| 2025-09-23T16:44:28Z | L99 | DES-316 | filed by Leonard: PN: Lapsed 1 day |
| 2025-09-23T16:46:16Z | L101 | DES-317 | filed by Leonard: PN: Lapsed 7 days |
| 2025-09-23T16:47:15Z | L103 | DES-318 | filed by Leonard: PN: Finish first mission |
| 2025-09-23T16:49:15Z | L97 | DES-315 | started |
| 2025-09-23T16:50:24Z | L105 | DES-319 | filed by Leonard: PN: Plague Race |
| 2025-09-23T16:51:24Z | L107 | DES-320 | filed by Leonard: PN: Weekly Leaderboard reset |
| 2025-09-23T16:53:51Z | L109 | DES-321 | filed by Leonard: PN: Quests rollover |
| 2025-09-23T16:55:45Z | L99 | DES-316 | started |
| 2025-09-23T16:55:46Z | L103 | DES-318 | started |
| 2025-09-23T16:56:36Z | L107 | DES-320 | started |
| 2025-09-23T16:56:55Z | L111 | DES-322 | filed by Leonard: PN: Login Calendar update |
| 2025-09-23T16:57:32Z | L113 | DES-323 | filed by Leonard: PN: Season Pass start or reward |
| 2025-09-23T16:57:56Z | L101 | DES-317 | started |
| 2025-09-23T16:58:17Z | L115 | DES-324 | filed by Leonard: PN: Hourly Coins |
| 2025-09-23T16:58:30Z | L105 | DES-319 | started |
| 2025-09-23T17:01:26Z | L117 | DES-325 | filed by Leonard: PN: Nathan's Treasure Hunt start |
| 2025-09-23T17:02:38Z | L109 | DES-321 | started |
| 2025-09-23T17:04:23Z | L113 | DES-323 | started |
| 2025-09-23T17:04:33Z | L115 | DES-324 | started |
| 2025-09-23T17:05:03Z | L119 | DES-326 | filed by Leonard: PN: Streak Fever start |
| 2025-09-23T17:06:37Z | L121 | DES-327 | filed by Leonard: PN: Axe Arena start |
| 2025-09-23T17:07:38Z | L117 | DES-325 | started |
| 2025-09-23T17:08:33Z | L111 | DES-322 | started |
| 2025-09-23T17:12:18Z | L119 | DES-326 | started |
| 2025-09-23T17:16:43Z | L165 | DES-315 | comment by Leonard (cmt_2395189d) |
| 2025-09-23T17:19:03Z | L169 | DES-316 | comment by Leonard (cmt_d6bf99cc) |
| 2025-09-23T17:19:18Z | L121 | DES-327 | started |
| 2025-09-23T17:19:41Z | L173 | DES-317 | comment by Leonard (cmt_f64ebdf0) |
| 2025-09-23T17:22:44Z | L177 | DES-318 | comment by Leonard (cmt_886fb8b0) |
| 2025-09-23T17:24:51Z | L181 | DES-319 | comment by Leonard (cmt_10ae5518) |
| 2025-09-23T17:27:57Z | L187 | DES-320 | comment by Leonard (cmt_f1b42e3a) |
| 2025-09-23T17:28:43Z | L191 | DES-321 | comment by Leonard (cmt_4aa525e0) |
| 2025-09-23T17:29:27Z | L195 | DES-322 | comment by Leonard (cmt_8531c261) |
| 2025-09-23T17:33:35Z | L199 | DES-323 | comment by Leonard (cmt_3dabe2da) |
| 2025-09-23T17:36:03Z | L203 | DES-324 | comment by Leonard (cmt_144462e0) |
| 2025-09-23T17:37:20Z | L207 | DES-325 | comment by Leonard (cmt_4478b09d) |
| 2025-09-23T17:41:15Z | L211 | DES-326 | comment by Leonard (cmt_84609a55) |
| 2025-09-23T17:45:18Z | L215 | DES-327 | comment by Leonard (cmt_5a45fa6e) |
| 2025-09-23T18:10:27Z | L68 | samuel.turner mail | Invitation: Lapsed ladder review @ Fri Sep 26, 2025 10am - 1 |
| 2025-09-23T18:10:27Z | L75 | evt_b56d5b19 | event created on samuel.turner calendar |
| 2025-09-23T18:10:27Z | L77 | evt_8cad40bb | event created on leonard.hayes calendar |
| 2025-09-23T20:41:40Z | base slack C07C2866011/2025-09 /968 | Leonard | "not having any PN will hurt retention" |
| 2025-09-24T13:12:24Z | L123 | DES-328 | filed by Brian: PN ask: Endless entries are back |
| 2025-09-24T13:14:58Z | L219 | DES-328 | comment by Brian (cmt_55c7d795) |
| 2025-09-24T13:21:06Z | L123 | DES-328 | started |
| 2025-09-24T13:31:05Z | L125 | DES-329 | filed by Brian: PN ask: Endless weekly result |
| 2025-09-24T13:33:48Z | L223 | DES-329 | comment by Brian (cmt_6e27d2eb) |
| 2025-09-24T13:39:44Z | L125 | DES-329 | started |
| 2025-09-24T14:10:16Z | L167 | DES-315 | comment by Vincent (cmt_51e018b2) |
| 2025-09-24T14:16:43Z | L171 | DES-316 | comment by Vincent (cmt_5ab75e0e) |
| 2025-09-24T14:22:08Z | L175 | DES-317 | comment by Vincent (cmt_e4bb9fe9) |
| 2025-09-24T14:28:24Z | L97 | DES-315 | completed (Done) |
| 2025-09-24T14:30:22Z | L183 | DES-319 | comment by Vincent (cmt_fd950c41) |
| 2025-09-24T14:40:17Z | L101 | DES-317 | completed (Done) |
| 2025-09-24T14:40:35Z | L189 | DES-320 | comment by Vincent (cmt_f76672cf) |
| 2025-09-24T14:42:03Z | L99 | DES-316 | completed (Done) |
| 2025-09-24T14:50:51Z | L179 | DES-318 | comment by Vincent (cmt_f4960d3c) |
| 2025-09-24T14:59:00Z | L107 | DES-320 | completed (Done) |
| 2025-09-24T15:00:05Z | L11 | Phone message checks | Drive file modified |
| 2025-09-24T15:10:41Z | L185 | DES-319 | comment by Leonard (cmt_9338bb2c) |
| 2025-09-24T15:15:16Z | L103 | DES-318 | completed (Done) |
| 2025-09-24T15:31:06Z | L105 | DES-319 | completed (Done) |
| 2025-09-24T15:58:47Z | L127 | DES-330 | filed by Robert: PN ask: Boss Arena is open |
| 2025-09-24T15:59:52Z | L46 | Trello 68d41578 | updateCard by Leonard on card 7 |
| 2025-09-24T16:00:39Z | L49 | Trello 68d415a7 | commentCard by Leonard on card 7 |
| 2025-09-24T16:01:06Z | L227 | DES-330 | comment by Robert (cmt_c6a61568) |
| 2025-09-24T16:03:19Z | L129 | DES-331 | filed by Robert: PN ask: Boss Arena last hours |
| 2025-09-24T16:05:48Z | L231 | DES-331 | comment by Robert (cmt_d9f2d461) |
| 2025-09-24T16:12:06Z | L127 | DES-330 | started |
| 2025-09-24T16:15:09Z | L129 | DES-331 | started |
| 2025-09-24T17:05:33Z | L131 | DES-332 | filed by Oliver: PN ask: Season Pass last 48 hours |
| 2025-09-24T17:08:53Z | L235 | DES-332 | comment by Oliver (cmt_e911c52c) |
| 2025-09-24T17:15:50Z | L131 | DES-332 | started |
| 2025-09-24T18:40:11Z | L133 | DES-333 | filed by Brian: PN ask: Season Pass premium nudge |
| 2025-09-24T18:43:28Z | L239 | DES-333 | comment by Brian (cmt_2456f475) |
| 2025-09-24T18:49:57Z | L133 | DES-333 | started |
| 2025-09-24T19:22:52Z | L135 | DES-334 | filed by Julia: PN ask: Plague Race last hour |
| 2025-09-24T19:25:08Z | L243 | DES-334 | comment by Julia (cmt_abb99f26) |
| 2025-09-24T19:27:08Z | L137 | DES-335 | filed by Julia: PN ask: Plague Race result |
| 2025-09-24T19:30:04Z | L135 | DES-334 | started |
| 2025-09-24T19:30:55Z | L247 | DES-335 | comment by Julia (cmt_83e42df5) |
| 2025-09-24T19:39:53Z | L137 | DES-335 | started |
| 2025-09-24T21:14:36Z | L139 | DES-336 | filed by Owen: PN ask: Zombie Lane reward ready |
| 2025-09-24T21:18:02Z | L141 | DES-337 | filed by Owen: PN ask: Achievement reward waiting |
| 2025-09-24T21:18:09Z | L251 | DES-336 | comment by Owen (cmt_546a8f6d) |
| 2025-09-24T21:21:14Z | L139 | DES-336 | started |
| 2025-09-24T21:22:58Z | L255 | DES-337 | comment by Owen (cmt_cd8081a7) |
| 2025-09-24T21:27:44Z | L141 | DES-337 | started |
| 2025-09-24T22:08:49Z | L143 | DES-338 | filed by Calvin: PN ask: Daily chest ready |
| 2025-09-24T22:12:26Z | L259 | DES-338 | comment by Calvin (cmt_b770ad38) |
| 2025-09-24T22:18:23Z | L143 | DES-338 | started |
| 2025-09-25T09:44:15Z | L145 | DES-339 | filed by Martin: PN ask: Free shop coins ready |
| 2025-09-25T09:48:26Z | L263 | DES-339 | comment by Martin (cmt_e0e37d68) |
| 2025-09-25T09:58:11Z | L145 | DES-339 | started |
| 2025-09-25T15:00:33Z | L72 | samuel.turner mail | Canceled event with note: Lapsed ladder review @ Fri Sep 26, |
| 2025-09-25T15:00:33Z | L75 | evt_b56d5b19 | event cancelled on samuel.turner calendar |
| 2025-09-25T15:00:33Z | L77 | evt_8cad40bb | event cancelled on leonard.hayes calendar |
| 2025-09-25T16:26:27Z | L147 | DES-340 | filed by Owen: PN ask: Support reply waiting |
| 2025-09-25T16:28:59Z | L267 | DES-340 | comment by Owen (cmt_a6c862db) |
| 2025-09-25T16:39:11Z | L147 | DES-340 | started |
| 2025-09-25T16:50:58Z | L149 | DES-341 | filed by Julia: PN ask: New levels added |
| 2025-09-25T16:54:02Z | L271 | DES-341 | comment by Julia (cmt_904474de) |
| 2025-09-25T17:00:24Z | L149 | DES-341 | started |
| 2025-09-25T17:05:13Z | L151 | DES-342 | filed by Leonard: PN ask: Lapsed 3 days |
| 2025-09-25T17:07:35Z | L275 | DES-342 | comment by Leonard (cmt_1443f478) |
| 2025-09-25T17:09:40Z | L153 | DES-343 | filed by Leonard: PN ask: Lapsed 30 days |
| 2025-09-25T17:13:00Z | L151 | DES-342 | started |
| 2025-09-25T17:13:26Z | L279 | DES-343 | comment by Leonard (cmt_fe508712) |
| 2025-09-25T17:19:06Z | L153 | DES-343 | started |
| 2025-09-25T20:35:48Z | L163 | DES-313 | comment by Arthur (cmt_cb634ee4) |
| 2025-09-25T20:37:50Z | L193 | DES-321 | comment by Arthur (cmt_7b184259) |
| 2025-09-25T20:39:02Z | L197 | DES-322 | comment by Arthur (cmt_5acbc1a3) |
| 2025-09-25T20:43:50Z | L201 | DES-323 | comment by Arthur (cmt_181bcd11) |
| 2025-09-25T20:50:24Z | L205 | DES-324 | comment by Arthur (cmt_8c9ab0f7) |
| 2025-09-25T20:57:44Z | L209 | DES-325 | comment by Arthur (cmt_64fc795e) |
| 2025-09-25T21:04:01Z | L213 | DES-326 | comment by Arthur (cmt_5d85e7a9) |
| 2025-09-25T21:06:40Z | L217 | DES-327 | comment by Arthur (cmt_842c9cb4) |
| 2025-09-25T21:13:15Z | L221 | DES-328 | comment by Arthur (cmt_c6f09d16) |
| 2025-09-25T21:18:04Z | L225 | DES-329 | comment by Arthur (cmt_9d5748e1) |
| 2025-09-25T21:24:41Z | L229 | DES-330 | comment by Arthur (cmt_e4ac3398) |
| 2025-09-25T21:29:55Z | L233 | DES-331 | comment by Arthur (cmt_e1c7ebcf) |
| 2025-09-25T21:30:54Z | L237 | DES-332 | comment by Arthur (cmt_44a1117f) |
| 2025-09-25T21:36:42Z | L241 | DES-333 | comment by Arthur (cmt_ff7c43f0) |
| 2025-09-25T21:42:41Z | L245 | DES-334 | comment by Arthur (cmt_521d7e03) |
| 2025-09-25T21:48:54Z | L249 | DES-335 | comment by Arthur (cmt_fda157ba) |
| 2025-09-25T21:55:55Z | L253 | DES-336 | comment by Arthur (cmt_b55d6a0b) |
| 2025-09-25T21:59:46Z | L257 | DES-337 | comment by Arthur (cmt_4feec391) |
| 2025-09-25T22:06:07Z | L261 | DES-338 | comment by Arthur (cmt_32da06fe) |
| 2025-09-25T22:11:42Z | L265 | DES-339 | comment by Arthur (cmt_aa68a0b0) |
| 2025-09-25T22:18:15Z | L269 | DES-340 | comment by Arthur (cmt_31db977b) |
| 2025-09-25T22:21:06Z | L273 | DES-341 | comment by Arthur (cmt_96b8c0e1) |
| 2025-09-25T22:24:48Z | L277 | DES-342 | comment by Arthur (cmt_af799d59) |
| 2025-09-25T22:27:35Z | L281 | DES-343 | comment by Arthur (cmt_58672546) |
| 2025-09-26T13:27:41Z | L291 | ZOM-542 | comment by Brian (cmt_f1b8a109) |
| 2025-09-26T14:08:12Z | L293 | ZOM-556 | comment by Julia (cmt_2b519285) |
| 2025-09-26T14:22:31Z | L155 | DES-344 | filed by Robert: PN ask: Lapsed 14 days |
| 2025-09-26T14:27:26Z | L283 | DES-344 | comment by Robert (cmt_fd999360) |
| 2025-09-26T14:31:05Z | L155 | DES-344 | started |
| 2025-09-26T15:31:17Z | L157 | DES-345 | filed by Brian: PN ask: Comeback gift on tap |
| 2025-09-26T15:35:32Z | L285 | DES-345 | comment by Brian (cmt_8c95a627) |
| 2025-09-26T15:38:25Z | L157 | DES-345 | started |
| 2025-09-26T16:00:17Z | L287 | DES-345 | comment by Leonard (cmt_13477aa8) |
| 2025-09-26T17:10:54Z | L7 | Beta message rule | Drive file created |
| 2025-09-26T18:02:19Z | L31 | Slack 394f73aa | Brian message in #zombie-match3d |
| 2025-09-29T15:10:44Z | L159 | DES-346 | filed by Robert: PN ask: Rewarded ad ready |
| 2025-09-29T15:13:47Z | L289 | DES-346 | comment by Robert (cmt_bd206b06) |
| 2025-09-29T15:24:37Z | L159 | DES-346 | started |
| 2025-09-29T15:30:49Z | base slack C08R8CHB0QL/2025-09 /255 | a3e78e82 | thread parent; base replies to 15:54:26Z |
| 2025-09-29T16:39:30Z | base slack D06UFE81RF0/2025-09 /24 | c42902df | Samuel asks Vincent to test a build; later thread parent |
| 2025-09-29T17:40:08Z | L33 | Slack 37c5701a | Robert message in #zombie-match3d |
| 2025-09-29T18:05:29Z | L37 | Slack d2b16907 | Leonard reply in #zombie-art |
| 2025-09-29T18:21:36Z | L35 | Slack 09aae609 | Arthur reply in #zombie-match3d |
| 2025-09-29T19:40:46Z | L40 | Slack 4a5ee025 | Vincent reply in DM Samuel/Vincent |
| 2025-09-29T20:15:03Z | L52 | Trello 68dae8c7 | commentCard by Leonard on card 79 |
| 2025-09-29T21:55:08Z | base slack C0880U9751A/2025-09 /463 | iOS 0.3.49 | released by Leonard |
| 2025-09-30T17:09:07Z | base trello /boards | ZM ROADMAP | board dateLastActivity, later than every injected action |
| 2025-09-30T20:40:51Z | L43 | Slack 6fd96f3c | Leonard message in DM Samuel/Leonard |

## 10. Statement ledger

All 145 data statements in execution order.

| SQL | Table | Record | Stamps | Result |
|---|---|---|---|---|
| L7 | gdrive.drive_files | f_dc45e0e5a8b8635c1b82b2 | created 2025-09-26T17:10:54Z, modified 2025-09-26T17:10:54Z | created <= modified; parent folder and owner match base; PASS |
| L9 | gdrive.drive_files | f_de7a1ae20201816a67750d | created 2025-09-19T18:30:26Z, modified 2025-09-19T18:30:26Z | created <= modified; parent folder and owner match base; PASS |
| L11 | gdrive.drive_files | f_8eb8c04713ff6a6ef4a265 | created 2025-09-15T12:51:17Z, modified 2025-09-24T15:00:05Z | created <= modified; parent folder and owner match base; PASS |
| L14 | gdocs.docs_documents | f_dc45e0e5a8b8635c1b82b2 | created 2025-09-26T17:10:54Z, modified 2025-09-26T17:10:54Z | same stamps, title, owner, shares, visibility as Drive row; style run end 1410 = decoded body length; PASS |
| L17 | gsheets.sheets_spreadsheets | f_8eb8c04713ff6a6ef4a265 | created 2025-09-15T12:51:17Z, modified 2025-09-24T15:00:05Z | same stamps, title, owner, shares, visibility as Drive row; PASS |
| L19 | gsheets.sheets_sheets | f_8eb8c04713ff6a6ef4a265 tab Beta | no stamp; "Checked" = Sep 24 | build versions existed by Sep 23; sheet modified after last pass comment; PASS |
| L22 | gslides.slides_presentations | f_de7a1ae20201816a67750d | created 2025-09-19T18:30:26Z, modified 2025-09-19T18:30:26Z | same stamps, title, owner, shares, visibility as Drive row; PASS |
| L24 | gslides.slides_pages | slide_7cbfbffe1b54 | no stamp | parent deck inserted first; PASS |
| L26 | gslides.slides_page_elements | el_b78f5cefad1f | no stamp | parent page inserted first; "6 Ready" matches base PN sheet last modified 2025-06-23; PASS |
| L28 | gslides.slides_page_elements | el_9ecdf1278098 | no stamp | parent page inserted first; "6 Ready" matches base PN sheet last modified 2025-06-23; PASS |
| L31 | slack.slack_messages | 394f73aa43aa303a755bc81b2cf43840 | ts 1758909739.853209 = 2025-09-26T18:02:19.853209Z | ts equals created_at; author is a channel member; PASS |
| L33 | slack.slack_messages | 37c5701a1780374401d295e86884f276 | ts 1759167608.326578 = 2025-09-29T17:40:08.326578Z | ts equals created_at; author is a channel member; PASS |
| L35 | slack.slack_messages | 09aae609aa744fb23288c7dcbac9926c | ts 1759170096.924778 = 2025-09-29T18:21:36.924778Z | ts equals created_at; author is a channel member; reply after parent; PASS |
| L37 | slack.slack_messages | d2b16907dc8c10fe5052805751097b58 | ts 1759169129.445834 = 2025-09-29T18:05:29.445834Z | ts equals created_at; author is a channel member; reply after parent; PASS |
| L39 | slack.slack_messages UPDATE | a3e78e820b9f880ef4e3d941562110df | see before/after table | counters and latest_reply match the reply set; PASS |
| L40 | slack.slack_messages | 4a5ee02518ff2fbeacaef2fc6d5a9ef9 | ts 1759174846.723833 = 2025-09-29T19:40:46.723833Z | ts equals created_at; author is a channel member; reply after parent; PASS |
| L42 | slack.slack_messages UPDATE | c42902df5f54c75c1a6e3529cd25121c | see before/after table | counters and latest_reply match the reply set; PASS |
| L43 | slack.slack_messages | 6fd96f3c3977cee8345e685d31cbc177 | ts 1759264851.763895 = 2025-09-30T20:40:51.763895Z | ts equals created_at; author is a channel member; PASS |
| L46 | trello.trello_actions | 68d41578905712b474fbc0ca | date 2025-09-24T15:59:52Z | id-embedded time equals date; shape matches base; PASS |
| L48 | trello.trello_cards UPDATE | 6851a769c65dc0017a227bb7 | see before/after table | final state matches action sequence; PASS |
| L49 | trello.trello_actions | 68d415a716abcb84070a8e2a | date 2025-09-24T16:00:39Z | id-embedded time equals date; shape matches base; PASS |
| L51 | trello.trello_cards UPDATE | 6851a769c65dc0017a227bb7 | see before/after table | final state matches action sequence; PASS |
| L52 | trello.trello_actions | 68dae8c7d95e24b55b69bf80 | date 2025-09-29T20:15:03Z | id-embedded time equals date; shape matches base; PASS |
| L54 | trello.trello_cards UPDATE | 68d1eb90bef538c7c5c5599d | see before/after table | final state matches action sequence; PASS |
| L56 | gmail.gmail_threads | samuel.turner@harmonygames.co/1843335316636662321 | id high bits decode to first message time | one member message; snippet equals message snippet; PASS |
| L58 | gmail.gmail_messages | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JC | date 2025-09-15T13:05:48Z | internal_date = date = header Date; PASS |
| L60 | gmail.gmail_threads | vincent.parker@harmonygames.co/1843335316636098078 | id high bits decode to first message time | one member message; snippet equals message snippet; PASS |
| L62 | gmail.gmail_messages | vincent.parker@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8J | date 2025-09-15T13:05:48Z | internal_date = date = header Date; PASS |
| L64 | gmail.gmail_messages | samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/24 | date 2025-06-26T20:58:14Z | internal_date = date = header Date; sits inside base thread before merge; see A1; PASS |
| L66 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844079259288333361 | id high bits decode to first message time | one member message; snippet equals message snippet; PASS |
| L68 | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9b | date 2025-09-23T18:10:27Z | internal_date = date = header Date; PASS |
| L70 | gmail.gmail_threads | samuel.turner@harmonygames.co/1844248505745845006 | id high bits decode to first message time | one member message; snippet equals message snippet; PASS |
| L72 | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f206 | date 2025-09-25T15:00:33Z | internal_date = date = header Date; PASS |
| L75 | gcal.gcal_events | evt_b56d5b19baa0a573da4553 | created 2025-09-23T18:10:27Z, updated 2025-09-25T15:00:33Z, start 2025-09-26T16:00:00Z, end 2025-09-26T16:30:00Z | created = invite mail, updated = cancel mail, cancelled before start, end after start; PASS |
| L77 | gcal.gcal_events | evt_8cad40bb558f994b74576a | created 2025-09-23T18:10:27Z, updated 2025-09-25T15:00:33Z, start 2025-09-26T16:00:00Z, end 2025-09-26T16:30:00Z | created = invite mail, updated = cancel mail, cancelled before start, end after start; PASS |
| L80 | github.github_review_comments | harmonygames-Games/match3d#248#rc_18 | created 2025-06-26T20:58:14Z | equals rev_7 and mail time; before merge; hunk is a verbatim prefix of base rc_16; see A3, A6; PASS |
| L82 | github.github_reviews | harmonygames-Games/match3d#248#rev_7 | submitted 2025-06-26T20:58:14Z | equals rc_18; before APPROVED and merge; see A2, A3; PASS |
| L85 | linear.linear_team_memberships | tmem_team_DES_usr_49b9dfa5208d400d | created 2025-09-17T15:02:44Z | before the person first files or is assigned on DES; PASS |
| L87 | linear.linear_team_memberships | tmem_team_DES_usr_caafeec2804b3a67 | created 2025-09-23T16:02:09Z | before the person first files or is assigned on DES; PASS |
| L89 | linear.linear_team_memberships | tmem_team_DES_usr_51f5f16d46e8cf55 | created 2025-09-23T16:03:31Z | before the person first files or is assigned on DES; PASS |
| L91 | linear.linear_team_memberships | tmem_team_DES_usr_bdf01b53c6a92c5e | created 2025-09-23T16:04:18Z | before the person first files or is assigned on DES; PASS |
| L93 | linear.linear_issues | DES-313 | In Review; created 09-17T15:20:37, started 09-17T15:51:15, updated 09-25T20:35:48 | created <= started <= completed; updated = latest stamp; PASS |
| L95 | linear.linear_issues | DES-314 | In Progress; created 09-23T16:40:12, started 09-23T16:41:35, updated 09-23T16:41:35 | created <= started <= completed; updated = latest stamp; PASS |
| L97 | linear.linear_issues | DES-315 | Done; created 09-23T16:42:38, started 09-23T16:49:15, completed 09-24T14:28:24, updated 09-24T14:28:24 | created <= started <= completed; updated = latest stamp; PASS |
| L99 | linear.linear_issues | DES-316 | Done; created 09-23T16:44:28, started 09-23T16:55:45, completed 09-24T14:42:03, updated 09-24T14:42:03 | created <= started <= completed; updated = latest stamp; PASS |
| L101 | linear.linear_issues | DES-317 | Done; created 09-23T16:46:16, started 09-23T16:57:56, completed 09-24T14:40:17, updated 09-24T14:40:17 | created <= started <= completed; updated = latest stamp; PASS |
| L103 | linear.linear_issues | DES-318 | Done; created 09-23T16:47:15, started 09-23T16:55:46, completed 09-24T15:15:16, updated 09-24T15:15:16 | created <= started <= completed; updated = latest stamp; PASS |
| L105 | linear.linear_issues | DES-319 | Done; created 09-23T16:50:24, started 09-23T16:58:30, completed 09-24T15:31:06, updated 09-24T15:31:06 | created <= started <= completed; updated = latest stamp; PASS |
| L107 | linear.linear_issues | DES-320 | Done; created 09-23T16:51:24, started 09-23T16:56:36, completed 09-24T14:59:00, updated 09-24T14:59:00 | created <= started <= completed; updated = latest stamp; PASS |
| L109 | linear.linear_issues | DES-321 | In Review; created 09-23T16:53:51, started 09-23T17:02:38, updated 09-25T20:37:50 | created <= started <= completed; updated = latest stamp; PASS |
| L111 | linear.linear_issues | DES-322 | In Review; created 09-23T16:56:55, started 09-23T17:08:33, updated 09-25T20:39:02 | created <= started <= completed; updated = latest stamp; PASS |
| L113 | linear.linear_issues | DES-323 | In Review; created 09-23T16:57:32, started 09-23T17:04:23, updated 09-25T20:43:50 | created <= started <= completed; updated = latest stamp; PASS |
| L115 | linear.linear_issues | DES-324 | In Review; created 09-23T16:58:17, started 09-23T17:04:33, updated 09-25T20:50:24 | created <= started <= completed; updated = latest stamp; PASS |
| L117 | linear.linear_issues | DES-325 | In Review; created 09-23T17:01:26, started 09-23T17:07:38, updated 09-25T20:57:44 | created <= started <= completed; updated = latest stamp; PASS |
| L119 | linear.linear_issues | DES-326 | In Review; created 09-23T17:05:03, started 09-23T17:12:18, updated 09-25T21:04:01 | created <= started <= completed; updated = latest stamp; PASS |
| L121 | linear.linear_issues | DES-327 | In Review; created 09-23T17:06:37, started 09-23T17:19:18, updated 09-25T21:06:40 | created <= started <= completed; updated = latest stamp; PASS |
| L123 | linear.linear_issues | DES-328 | In Review; created 09-24T13:12:24, started 09-24T13:21:06, updated 09-25T21:13:15 | created <= started <= completed; updated = latest stamp; PASS |
| L125 | linear.linear_issues | DES-329 | In Review; created 09-24T13:31:05, started 09-24T13:39:44, updated 09-25T21:18:04 | created <= started <= completed; updated = latest stamp; PASS |
| L127 | linear.linear_issues | DES-330 | In Review; created 09-24T15:58:47, started 09-24T16:12:06, updated 09-25T21:24:41 | created <= started <= completed; updated = latest stamp; PASS |
| L129 | linear.linear_issues | DES-331 | In Review; created 09-24T16:03:19, started 09-24T16:15:09, updated 09-25T21:29:55 | created <= started <= completed; updated = latest stamp; PASS |
| L131 | linear.linear_issues | DES-332 | In Review; created 09-24T17:05:33, started 09-24T17:15:50, updated 09-25T21:30:54 | created <= started <= completed; updated = latest stamp; PASS |
| L133 | linear.linear_issues | DES-333 | In Review; created 09-24T18:40:11, started 09-24T18:49:57, updated 09-25T21:36:42 | created <= started <= completed; updated = latest stamp; PASS |
| L135 | linear.linear_issues | DES-334 | In Review; created 09-24T19:22:52, started 09-24T19:30:04, updated 09-25T21:42:41 | created <= started <= completed; updated = latest stamp; PASS |
| L137 | linear.linear_issues | DES-335 | In Review; created 09-24T19:27:08, started 09-24T19:39:53, updated 09-25T21:48:54 | created <= started <= completed; updated = latest stamp; PASS |
| L139 | linear.linear_issues | DES-336 | In Review; created 09-24T21:14:36, started 09-24T21:21:14, updated 09-25T21:55:55 | created <= started <= completed; updated = latest stamp; PASS |
| L141 | linear.linear_issues | DES-337 | In Review; created 09-24T21:18:02, started 09-24T21:27:44, updated 09-25T21:59:46 | created <= started <= completed; updated = latest stamp; PASS |
| L143 | linear.linear_issues | DES-338 | In Review; created 09-24T22:08:49, started 09-24T22:18:23, updated 09-25T22:06:07 | created <= started <= completed; updated = latest stamp; PASS |
| L145 | linear.linear_issues | DES-339 | In Review; created 09-25T09:44:15, started 09-25T09:58:11, updated 09-25T22:11:42 | created <= started <= completed; updated = latest stamp; PASS |
| L147 | linear.linear_issues | DES-340 | In Review; created 09-25T16:26:27, started 09-25T16:39:11, updated 09-25T22:18:15 | created <= started <= completed; updated = latest stamp; PASS |
| L149 | linear.linear_issues | DES-341 | In Review; created 09-25T16:50:58, started 09-25T17:00:24, updated 09-25T22:21:06 | created <= started <= completed; updated = latest stamp; PASS |
| L151 | linear.linear_issues | DES-342 | In Review; created 09-25T17:05:13, started 09-25T17:13:00, updated 09-25T22:24:48 | created <= started <= completed; updated = latest stamp; PASS |
| L153 | linear.linear_issues | DES-343 | In Review; created 09-25T17:09:40, started 09-25T17:19:06, updated 09-25T22:27:35 | created <= started <= completed; updated = latest stamp; PASS |
| L155 | linear.linear_issues | DES-344 | In Review; created 09-26T14:22:31, started 09-26T14:31:05, updated 09-26T14:31:05 | created <= started <= completed; updated = latest stamp; PASS |
| L157 | linear.linear_issues | DES-345 | In Review; created 09-26T15:31:17, started 09-26T15:38:25, updated 09-26T16:00:17 | created <= started <= completed; updated = latest stamp; PASS |
| L159 | linear.linear_issues | DES-346 | In Review; created 09-29T15:10:44, started 09-29T15:24:37, updated 09-29T15:24:37 | created <= started <= completed; updated = latest stamp; PASS |
| L161 | linear.linear_comments | cmt_7c6c022293a0505fbf85 | DES-313 at 2025-09-17T15:25:18Z, by Calvin | after issue created; not after completion; updated_at = created_at; PASS |
| L163 | linear.linear_comments | cmt_cb634ee40df2ae6c6022 | DES-313 at 2025-09-25T20:35:48Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L165 | linear.linear_comments | cmt_2395189dfd5e7d5c1e88 | DES-315 at 2025-09-23T17:16:43Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L167 | linear.linear_comments | cmt_51e018b23e18c2f680cd | DES-315 at 2025-09-24T14:10:16Z, by Vincent | after issue created; not after completion; updated_at = created_at; PASS |
| L169 | linear.linear_comments | cmt_d6bf99cc8b3e926c2569 | DES-316 at 2025-09-23T17:19:03Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L171 | linear.linear_comments | cmt_5ab75e0ee96e70745960 | DES-316 at 2025-09-24T14:16:43Z, by Vincent | after issue created; not after completion; updated_at = created_at; PASS |
| L173 | linear.linear_comments | cmt_f64ebdf08bef6b136513 | DES-317 at 2025-09-23T17:19:41Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L175 | linear.linear_comments | cmt_e4bb9fe925b86f52cf55 | DES-317 at 2025-09-24T14:22:08Z, by Vincent | after issue created; not after completion; updated_at = created_at; PASS |
| L177 | linear.linear_comments | cmt_886fb8b04e3b6ba66b57 | DES-318 at 2025-09-23T17:22:44Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L179 | linear.linear_comments | cmt_f4960d3c073493b6bfc6 | DES-318 at 2025-09-24T14:50:51Z, by Vincent | after issue created; not after completion; updated_at = created_at; PASS |
| L181 | linear.linear_comments | cmt_10ae5518084785a96cfc | DES-319 at 2025-09-23T17:24:51Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L183 | linear.linear_comments | cmt_fd950c410ed25c447c02 | DES-319 at 2025-09-24T14:30:22Z, by Vincent | after issue created; not after completion; updated_at = created_at; PASS |
| L185 | linear.linear_comments | cmt_9338bb2c286a6c207792 | DES-319 at 2025-09-24T15:10:41Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L187 | linear.linear_comments | cmt_f1b42e3a7c9cfa136439 | DES-320 at 2025-09-23T17:27:57Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L189 | linear.linear_comments | cmt_f76672cf21387ec1eeab | DES-320 at 2025-09-24T14:40:35Z, by Vincent | after issue created; not after completion; updated_at = created_at; PASS |
| L191 | linear.linear_comments | cmt_4aa525e0162ec9ef15f6 | DES-321 at 2025-09-23T17:28:43Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L193 | linear.linear_comments | cmt_7b184259cfbb33052325 | DES-321 at 2025-09-25T20:37:50Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L195 | linear.linear_comments | cmt_8531c2616065b39e5c26 | DES-322 at 2025-09-23T17:29:27Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L197 | linear.linear_comments | cmt_5acbc1a3f111af34e7ac | DES-322 at 2025-09-25T20:39:02Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L199 | linear.linear_comments | cmt_3dabe2da836af3cc9ba8 | DES-323 at 2025-09-23T17:33:35Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L201 | linear.linear_comments | cmt_181bcd11a979359893fb | DES-323 at 2025-09-25T20:43:50Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L203 | linear.linear_comments | cmt_144462e04c0e02c19d02 | DES-324 at 2025-09-23T17:36:03Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L205 | linear.linear_comments | cmt_8c9ab0f70f9ab1dc5d5f | DES-324 at 2025-09-25T20:50:24Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L207 | linear.linear_comments | cmt_4478b09dc764fe7e1cd1 | DES-325 at 2025-09-23T17:37:20Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L209 | linear.linear_comments | cmt_64fc795e9c80b7c68a7e | DES-325 at 2025-09-25T20:57:44Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L211 | linear.linear_comments | cmt_84609a55e9bb01533c18 | DES-326 at 2025-09-23T17:41:15Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L213 | linear.linear_comments | cmt_5d85e7a910a89f7e0eeb | DES-326 at 2025-09-25T21:04:01Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L215 | linear.linear_comments | cmt_5a45fa6ed829ce69c092 | DES-327 at 2025-09-23T17:45:18Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L217 | linear.linear_comments | cmt_842c9cb4757414e145d3 | DES-327 at 2025-09-25T21:06:40Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L219 | linear.linear_comments | cmt_55c7d795dc967c39c6a5 | DES-328 at 2025-09-24T13:14:58Z, by Brian | after issue created; not after completion; updated_at = created_at; PASS |
| L221 | linear.linear_comments | cmt_c6f09d1660c6a174811f | DES-328 at 2025-09-25T21:13:15Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L223 | linear.linear_comments | cmt_6e27d2eb839bbc66a95a | DES-329 at 2025-09-24T13:33:48Z, by Brian | after issue created; not after completion; updated_at = created_at; PASS |
| L225 | linear.linear_comments | cmt_9d5748e1540a9588ceb9 | DES-329 at 2025-09-25T21:18:04Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L227 | linear.linear_comments | cmt_c6a61568172ef0ebb990 | DES-330 at 2025-09-24T16:01:06Z, by Robert | after issue created; not after completion; updated_at = created_at; PASS |
| L229 | linear.linear_comments | cmt_e4ac33987005778b372e | DES-330 at 2025-09-25T21:24:41Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L231 | linear.linear_comments | cmt_d9f2d461e083b4a65263 | DES-331 at 2025-09-24T16:05:48Z, by Robert | after issue created; not after completion; updated_at = created_at; PASS |
| L233 | linear.linear_comments | cmt_e1c7ebcf5aa9ee4b4a8c | DES-331 at 2025-09-25T21:29:55Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L235 | linear.linear_comments | cmt_e911c52cf054cb3ed19b | DES-332 at 2025-09-24T17:08:53Z, by Oliver | after issue created; not after completion; updated_at = created_at; PASS |
| L237 | linear.linear_comments | cmt_44a1117f30fbb476c28c | DES-332 at 2025-09-25T21:30:54Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L239 | linear.linear_comments | cmt_2456f47526183e4e1161 | DES-333 at 2025-09-24T18:43:28Z, by Brian | after issue created; not after completion; updated_at = created_at; PASS |
| L241 | linear.linear_comments | cmt_ff7c43f0633261872ec7 | DES-333 at 2025-09-25T21:36:42Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L243 | linear.linear_comments | cmt_abb99f26dc3013206909 | DES-334 at 2025-09-24T19:25:08Z, by Julia | after issue created; not after completion; updated_at = created_at; PASS |
| L245 | linear.linear_comments | cmt_521d7e03d14d535f1d5b | DES-334 at 2025-09-25T21:42:41Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L247 | linear.linear_comments | cmt_83e42df52254cf27fe4d | DES-335 at 2025-09-24T19:30:55Z, by Julia | after issue created; not after completion; updated_at = created_at; PASS |
| L249 | linear.linear_comments | cmt_fda157bae8336585356a | DES-335 at 2025-09-25T21:48:54Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L251 | linear.linear_comments | cmt_546a8f6d521e2d00dc28 | DES-336 at 2025-09-24T21:18:09Z, by Owen | after issue created; not after completion; updated_at = created_at; PASS |
| L253 | linear.linear_comments | cmt_b55d6a0b35ae5242ffd4 | DES-336 at 2025-09-25T21:55:55Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L255 | linear.linear_comments | cmt_cd8081a714a205760ce7 | DES-337 at 2025-09-24T21:22:58Z, by Owen | after issue created; not after completion; updated_at = created_at; PASS |
| L257 | linear.linear_comments | cmt_4feec391e19bb4a4a16a | DES-337 at 2025-09-25T21:59:46Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L259 | linear.linear_comments | cmt_b770ad38987fc947c65f | DES-338 at 2025-09-24T22:12:26Z, by Calvin | after issue created; not after completion; updated_at = created_at; PASS |
| L261 | linear.linear_comments | cmt_32da06fe646ada57c7fa | DES-338 at 2025-09-25T22:06:07Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L263 | linear.linear_comments | cmt_e0e37d68814e1eae6002 | DES-339 at 2025-09-25T09:48:26Z, by Martin | after issue created; not after completion; updated_at = created_at; PASS |
| L265 | linear.linear_comments | cmt_aa68a0b0ee32e8e24c58 | DES-339 at 2025-09-25T22:11:42Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L267 | linear.linear_comments | cmt_a6c862db8697a973afc7 | DES-340 at 2025-09-25T16:28:59Z, by Owen | after issue created; not after completion; updated_at = created_at; PASS |
| L269 | linear.linear_comments | cmt_31db977b4adf091259da | DES-340 at 2025-09-25T22:18:15Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L271 | linear.linear_comments | cmt_904474dee7687823b700 | DES-341 at 2025-09-25T16:54:02Z, by Julia | after issue created; not after completion; updated_at = created_at; PASS |
| L273 | linear.linear_comments | cmt_96b8c0e10b3d2b20a982 | DES-341 at 2025-09-25T22:21:06Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L275 | linear.linear_comments | cmt_1443f47829522f8bb44e | DES-342 at 2025-09-25T17:07:35Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L277 | linear.linear_comments | cmt_af799d5941e425ad3e53 | DES-342 at 2025-09-25T22:24:48Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L279 | linear.linear_comments | cmt_fe5087128f529fdbb69f | DES-343 at 2025-09-25T17:13:26Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L281 | linear.linear_comments | cmt_58672546fb6435495753 | DES-343 at 2025-09-25T22:27:35Z, by Arthur | after issue created; not after completion; updated_at = created_at; PASS |
| L283 | linear.linear_comments | cmt_fd99936084694fa6d973 | DES-344 at 2025-09-26T14:27:26Z, by Robert | after issue created; not after completion; updated_at = created_at; PASS |
| L285 | linear.linear_comments | cmt_8c95a627941e0b32e091 | DES-345 at 2025-09-26T15:35:32Z, by Brian | after issue created; not after completion; updated_at = created_at; PASS |
| L287 | linear.linear_comments | cmt_13477aa8d1468ae11c9d | DES-345 at 2025-09-26T16:00:17Z, by Leonard | after issue created; not after completion; updated_at = created_at; PASS |
| L289 | linear.linear_comments | cmt_bd206b061637646ac5cb | DES-346 at 2025-09-29T15:13:47Z, by Robert | after issue created; not after completion; updated_at = created_at; PASS |
| L291 | linear.linear_comments | cmt_f1b8a109dfa70cdc4565 | ZOM-542 at 2025-09-26T13:27:41Z, by Brian | after issue created; not after completion; updated_at = created_at; PASS |
| L293 | linear.linear_comments | cmt_2b519285937e7fa79453 | ZOM-556 at 2025-09-26T14:08:12Z, by Julia | after issue created; not after completion; updated_at = created_at; PASS |
| L295 | linear.linear_issues UPDATE | ZOM-542 | see before/after table | later than base updated_at; nothing lost; PASS |
| L296 | linear.linear_issues UPDATE | ZOM-556 | see before/after table | later than base updated_at; nothing lost; PASS |
| L297 | linear.linear_teams UPDATE | team_DES | see before/after table | 346 = highest new number; base value not in export; PASS |
