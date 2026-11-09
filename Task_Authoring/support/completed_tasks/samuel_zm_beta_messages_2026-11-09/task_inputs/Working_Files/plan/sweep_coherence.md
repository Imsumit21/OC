# Coherence sweep: 01_Universe_Inject.sql against the synth-cut base

Clock 2025-10-01 07:00Z. Persona Samuel Turner. SQL read in full (131 INSERT, 7 UPDATE, matches its header).
Base read only through `hg.py search`. Slack citations are `messages/<channel>/<month>.json /<array index>`.
Channels: C0880U9751A #zombie-match3d, C08R27X0EAH #zombie-bugs, C08R8CHB0QL #zombie-art, C07C2866011 #executives, C05KNDCHAAG #company-internal.

Counts: **2 BLOCKER, 8 MAJOR, 12 MINOR.**

Severity used here:
- BLOCKER: a contradiction on a decision input, or a defect the QC form says always fails.
- MAJOR: a demonstrated inconsistency in task-touched data.
- MINOR: implausible, planted-looking or advisory. Some sit outside Eval 0's fail rules (working hours, voice) and are listed because this sweep asked for them.

---

## BLOCKER

### B1. "Nothing asks before that in the beta build" contradicts the base on iOS

**Seeded.** SQL line 34, Robert, #zombie-match3d, 2025-09-29T17:40Z: "Permission ask for beta: leaving it after level 20 ... Nothing asks before that in the beta build."

**Base.**
- `C0880U9751A/2025-09 /311` Vincent 09-18: "For ios, the permission happens at the start of the game".
- `C08R27X0EAH/2025-09 /855` Vincent 09-19: "On ios notfication pop ups are at the start of app not lvl 20".
- `C07C2866011/2025-09 /938` Leonard 09-23: "on ios we ask it upfront". `/949`: "We make the request at initial loading screen. On Android the request is indeed at level 20".
- `/952` Arthur: "In code we request at start (Unity itself is triggering this one), then after level 20 we trigger it again."
- `/958`-`/963` Arthur: the Unity one can be skipped "from the code side", as a possibility. `/965`-`/973`: Leonard and Robert leave the desired behaviour unsettled.
- No removal is recorded. All 149 match3d commits from 09-23 to 09-30 were listed: none concerns notifications or permission. A scan of #builds for September finds none either. iOS 0.3.49 shipped 09-29 21:55Z (`C0880U9751A/2025-09 /463`), after Robert's line, with no such change.

**Why it fails.** Rule test 4 and the note's "who actually hears from us" both hinge on when the ask happens. The base says iOS players are asked at launch, so "Finish first mission" does reach iOS players below level 20. Robert's line says it reaches nobody. Two records give two answers, and nothing supersedes the base. Cross-service Referential, on a deciding fact.

**Smallest fix.** Pick one:
- Keep the intended result: add one seeded Arthur reply dated before iOS Submission #49 (09-26 23:07Z), for example "Unity start-up ask is off from the next submission, level 20 is the only ask on both", under `/952` with its parent counters updated. A matching commit row would close the remaining gap.
- Keep the base: change Robert's last sentence to "Android asks nothing before that, iOS still gets Unity's ask at launch" and change the expected result for that row to an Android-only gap.

### B2. New activity on a completed Trello card

**Seeded.** SQL lines 45-46: Leonard's commentCard 2025-09-24T16:00Z on card 6851a769c65dc0017a227bb7, with `dateLastActivity` moved to 09-24 and `dueComplete: true` kept.

**Base.** Action 6862c0874151cf6318d91742 (2025-06-30T16:51:19Z) sets `dueComplete: true`, `dateCompleted` 2025-06-30. Card `dueComplete` true, list "Jun 30th", last activity 06-30.

**Why it fails.** A card closed out on Jun 30 gets a Sep 24 comment saying the beta list "goes on this card", and the task's required checklist write lands on it too. 1_Prompt_Eval §3.2: a closed ticket with later activity always fails and cannot take the low-impact Non-Fail. The card is a required open, so a reviewer will see it.

**Smallest fix.** Add one updateCard action just before the comment (2025-09-24T15:59Z, Leonard, `old: {dueComplete: true}`), set `trello_cards.dueComplete = false`, and set `dueComplete: false` in the badges UPDATE already on line 46.

---

## MAJOR

### M1. Seeded action says "BETA: Oct 10" between actions that say "BETA: Sep 30"

**Seeded.** SQL line 48, action 68dae8c4d95e24b55b69bf80 dated 2025-09-29: `"list": {"name": "BETA: Oct 10"}`.

**Base.** Every action on list 6851a674975da1fe76e70d93 reads "BETA: Sep 30", from 09-12 through 2025-09-30T17:09:07Z, including the two on this same card (09-23). `C05KNDCHAAG/2025-09 /21`: "Beta target: Sep 30." Only the list table reads Oct 10 (known card SC-13).

**Why it fails.** The Sep 29 action sits between Sep 23 and Sep 30 actions carrying the other name, with no rename action. It extends a known conflict into seeded data on a list the rule doc points the solver to.

**Smallest fix.** Change that JSON value to "BETA: Sep 30".

### M2. "Nothing new lands in anyone's Todo" is broken by a base ticket

**Seeded.** SQL line 48, Leonard, 2025-09-29T20:15Z: "Until the beta build is out nothing new lands in anyone's Todo. Held work sits in Backlog, unassigned."

**Base.** ZOM-566 "Collect&Win Analytics": state Todo, assignee Owen Baker, created 2025-09-30T16:26:02Z. That is 20 hours later and before the Sep 30 submissions (iOS #50 and Android #135 started 18:43Z and 18:45Z in #builds).

**Why it fails.** The rule is stated company-wide and a base ticket breaks it the next day. The line is also the override for every Hold ticket's state.

**Smallest fix.** Narrow it: "Until the beta build is out no new phone message work lands in anyone's Todo. Held messages sit in Backlog, unassigned."

### M3. Two seeded asks quote Arthur before Arthur's review exists

**Seeded.**
- SQL line 279, Brian on ZOM-542, 2025-09-24T13:10Z: "Arthur says a local timer is enough."
- SQL line 281, Julia on ZOM-556, 2025-09-25T11:45Z: "local timer per Arthur."

**Base and SQL.** Arthur's first seeded verdict is 2025-09-25T20:30Z (line 151). He has no comment on either ticket. His messages from 09-22 to 09-25 in eight checked channels and DMs (#zombie-match3d, #zombie-bugs, #zombie-art, #company-internal, #executives, #zombie-design, C09EVVCFHKR, D06477JGUKT) mention notifications once, about the permission prompt (`C07C2866011/2025-09 /943`). Other DMs were not checked.

**Why it fails.** Both records cite a judgement that first appears later than they do (31 hours and 9 hours), and it is the only source for rule test 2 on these two asks. Temporal, on required hidden asks.

**Smallest fix.** Move both comments after 2025-09-25T21:16Z and move the matching `updated_at` values on lines 282-283. Or add one Arthur comment on each ZOM ticket.

### M4. Leonard's ask DM makes three statements the records do not back

**Seeded.** SQL line 42, 2025-09-30T20:40Z.

| Statement | Records | Fix |
|---|---|---|
| "I made a ticket for each sheet row under DES-314" | The PNs Beta tab has 14 rows (`gsheets /sheets_spreadsheets/220`). DES-314 has 13 row children (DES-315 to DES-327). Row 7 "Win & Collect event start" has none, and DES-313 has `parent_id` NULL. | "I made tickets for the sheet rows under DES-314" |
| "filed on a ticket or a card" | No PN ask exists on any card. A search of all ZM ROADMAP cards, comments and check items finds only card 7 and an unrelated bug card. The two seeded Trello comments are not asks. | Drop "or a card", or seed one card ask |
| "we're about to put real money behind beta" | Paid traffic was already on: `C07C2866011/2025-09 /1153`-`/1154` Android 09-29, `/1166` iOS at $150/campaign/day, `/1191` Frederick 09-30 20:27Z "clicks are up today 5x". | "we're putting real money behind beta now" |

The Win & Collect row may be a deliberate duplicate trap. The sentence is still false as written, and it is the task brief.

### M5. Rule test 4 read literally also fails the rows meant to pass

**Seeded.** SQL line 15, test 4: "It can reach the players it is written for. A player only counts once the permission ask has happened". SQL line 34: nothing asks before level 20. Lines 153, 157, 161: "Who it's for: everyone", "everyone who has stopped".

**Why it fails.** Below-level-20 players sit inside "everyone" and, by the seeded line, have never been asked. The same test that fails "Finish first mission" therefore partly fails Lives recharged, Lapsed 1 day and Lapsed 7 days. The rule never says whether partial reach passes, so the Go count can move by three. Reasoning from the records, not a field contradiction, but it is an unsettled classification fork on the final counts.

**Smallest fix.** Add one sentence to test 4: "It only fails when none of the players it's written for have been asked."

### M6. DES-341 assumes a last level the game does not have

**Seeded.** SQL lines 137 and 259, Julia: "Tell players who finished the last level that new levels are in", "for players at the last level".

**Base.** `page_liveops_calendar`: "algorithmically generated levels - everything above level 100". ZOM-459 "Algo levels doesn't count for plague race". Trello #56 "Algo Levels V2.1" on the BETA list. Archived card #11 describes levels generated "after player finishes all manually designed levels". `C05KNDCHAAG/2025-09 /10`: Julia herself working on levels 120+.

**Why it fails.** Players do not run out of levels, and the ask comes from the person who builds them.

**Smallest fix.** Reword to "Tell players past the hand-made levels when new ones go in" and "for players past the hand-made levels".

### M7. Zombie Lane: the timer verdict does not fit, and DES-337 is the same feature

**Seeded.** SQL lines 127 and 241: "Zombie Lane is live. Ping when a reward on the lane is ready", Arthur "local timer is enough". SQL line 129: "Trophy Path is live", filed 4 minutes later by the same author.

**Base.**
- `page_liveops_calendar`: Zombie Lane is "Permanent (level-gated reward track)". No time element.
- ZOM-385: rewards are "unclaimed" items.
- ZOM-391 is titled "Zombie Lane and new card Tutorial", and its body says "trophy path main screen" then "zombie lane panel". The calendar has no Trophy Path row. They are one feature.

**Why it fails.** A level-gated reward becomes ready through play, and a closed game makes no progress, so a timer has nothing to count (reasoning from the records). Owen also files one feature twice with no sign he knows it. If that is a planned duplicate, the DM's "under whatever name" covers it, but the verdict still fails.

**Smallest fix.** Reword DES-336 to "Ping when a claimable reward has been sitting on the lane", or make Arthur's verdict "needs a server send". Keep DES-337 only if the duplicate is intended, and if so give it a comment that reads like one.

### M8. The PR #248 inline comment does not match the PR's state at 20:58Z

**Seeded.** SQL line 76, rc_18, created 2025-06-26T20:58:00Z. The time itself is fine: it falls after the PR opened (15:43:34Z) and before Arthur's approval (21:23:25Z) and the merge (21:23:32Z).

**Base.**
- The seeded `diff_hunk` is a verbatim prefix of rc_10 (`/review_comments/599`, 17:19:05Z): header `@@ -0,0 +1,487 @@`, public field `notificationsEnabled`, literal "PermissionGranted".
- rc_14 (17:36:19Z) already shows `+1,494`. rc_16 (`/review_comments/605`, 19:04:08Z) shows `+1,537`, `NotificationsEnabled { get; private set; }` and `PermissionGranted` constants.
- Head at 20:58Z was 7a6604b3 (18:58:24Z).
- Reviews on the PR are at 15:50:47, 17:19:04, 17:36:18, 19:04:08, 21:21:27, 21:23:25. None is near 20:58, and no timeline event matches.
- The seeded email id `review/2963610417` therefore resolves to no review.

**Why it fails.** The comment shows code two revisions older than its own timestamp, and an inline comment has no parent review while Gmail cites one. Note the code claim itself is correct: `referenceDate` is the server date at focus loss, and the anchor line is right.

**Smallest fix.** Rebuild the hunk from rc_16 up to the same `i * 7` line, then add `github.github_reviews` row `#rev_7` (Arthur, COMMENTED, 20:58Z). Moving `created_at` to between 17:19Z and 17:36Z fixes the hunk alone, but the review row is still needed.

---

## MINOR

1. **DES actors missing from the team.** SQL line 79 adds only Samuel. Calvin (creator of DES-313 and DES-338, assignee of DES-313), Martin (DES-339) and Oliver (DES-332) are not in team_DES. Every base DES creator and assignee is a member. Fix: three more membership rows dated before their first ticket.

2. **Implausible hours.** Eval 0 does not fail these alone.
   - Robert: DES-346 12:10Z, DES-330 12:58Z, DES-331 13:03Z, with comments to 13:06Z. He has 0 of 2,004 sampled September Slack messages in 08:00-13:59Z.
   - Owen: DES-336 and DES-337 09:14-09:21Z, about 03:15 El Salvador on his calendar zone. He has 0 of 42 Slack messages in 07:00-13:59Z and 1 of 440 commits in hour 09.
   - Calvin: DES-338 10:08-10:11Z, about 04:08 El Salvador. 0 of 1,275 commits in hour 10 (his commits sit under masked id PERSON_2137, matched through #builds "[Calvin Price]").
   - Slack figures come from ten September channels and DMs, not the whole export.
   - Fix: move these to the authors' afternoon.

3. **Machine cadence.** Arthur's 24 comments fall on every even minute from 20:30Z to 21:16Z and use four strings. The two "local timer" wordings alternate down the ticket list. Leonard's 13 row tickets are one minute apart with `started_at` exactly +5 minutes, and his "Who it's for" comments are one minute apart in ticket order. All 34 tickets are created on :00 seconds, as are all five Slack messages. Fix: jitter the times and let Arthur batch or vary.

4. **DES clashes with its base style.** No base DES ticket is dated after 2025-05-07, and none concerns ZM. ZM work sits in team_ZOM (553 tickets, still active to 09-30). The titles "PN:" / "PN ask:" and the "Fires: ... Headline: ..." template have no base precedent. Base Linear has zero comments across 3,687 issues, so the 67 seeded comments are the only ones. The 27 seeded In Review tickets have no `completed_at`, unlike all 12 base ones (SC-32). That is the cleaner state, so leave it. DES-344 to DES-346 sit In Review with no engineer comment, unlike the rest. Team placement is defensible for a designer; say why in DES-314 if kept.

5. **Corrections in unrelated threads.**
   - Line 36: Leonard's headline change sits under Martin's desert-theme thread and opens "random one while I'm here".
   - Line 39: Vincent's retraction sits under Samuel's build 2007 request. It is the only threaded message among 185 in that DM from June to September.
   - Line 32: Brian's only top-level post in #zombie-match3d in September; his other five are thread replies.
   - Counters are correct. These read as placed, not written. Fix: drop "random one while I'm here", and make Vincent's a top-level DM.

6. **Email.**
   - Vincent's note is his first ever mail to Samuel: 0 messages from him across Samuel's 3,870 thread files, complete scan.
   - Oliver and Owen are addressed and have mailboxes but get no copy.
   - The PR email's In-Reply-To points at CodeRabbit's review 2963243580, while all 8 base messages reply to the PR root and rc_18 has `in_reply_to_id` NULL. It also omits `Label_b19fb8d1b3`, carried by all 8.
   - Fix the header and label, and add the two copies or trim the To list.

7. **Calendar description.** 0 of 10,395 base events have a description. The two seeded events are the only ones. The note is already in the Gmail cancellation (line 68). Fix: set `description` NULL.

8. **Boss Arena "open" and "closes"** (DES-330, DES-331, both Robert). The GDD (`gdocs /docs_documents/563`) and the API (`C08R6BF4ENN/2025-09 /0`) describe daily entries and weekly boards, with no window. No record shows an opening or closing time. This is absence, not a contradiction, and "closes" could mean the daily reset. Separately, Brian says "attempts" where the GDD, API and his own DES-328 say "entries". Fix: "when today's entries are back", "before today's entries reset".

9. **ZOM-556 premise.** Julia asks for a reminder before the daily gift resets, on a ticket saying it "doesn't reset right now" (Todo, open). Fix: move the ask to ZOM-299's feature or a fresh ticket, or tie it to the daily rollover.

10. **Rule doc voice.** Leonard owns the doc yet writes "the latest line Leonard has called". "Neither status column on the sheet decides anything" and "the settings toggle doesn't count" read as trap disarming. No line describes a test or addresses a grader, so Eval 0's grader-language rule is not met. Fix: "the latest line I've called".

11. **Padding.** The "Beta readiness" deck (lines 10, 23-29) is cited by no seeded record or ask, and its one claim repeats the six-Ready count already in the sheet and the DM. Fix: remove it, or give it a purpose.

12. **SQL surface.** Line 1 "-- Are you planning to inject? Yes" is a form leftover; remove it. Advisory only: `seq`, `sequence` and `issue_counter` are outside the schema snapshot. Earlier submitted SQL used `sequence` as here. It used `seq` on review comments together with `pull_request_review_id`, `side` and `subject_type`, which line 75 omits.

---

## Sibling defects in records a correct run opens

None needs a SQL change beyond the above.
- **SC-13.** The BETA list name conflict stays visible to a reviewer. The task should not grade a beta date. See M1.
- **PN sheet bodies.** Rows 6, 8 and 13 carry mask tokens (`[PERSON_NAME_2549]`, `[PERSON_NAME_16313]`). Harmless while only headlines are required.
- **Twin sheet.** "Push Notifications Domino Adventure" also has a PNs Beta tab, but no Ready column, so "six Ready" selects the Zombie Match sheet.
- **Segmentation.** The sheet says Everyone for Plague Race, Leaderboard and Season Pass, while Leonard's comments say past the unlock. Settle which feeds the Audience column.
- **ZOM-542.** State Regression with `started_at` null is pre-existing.

## Checked, no finding

- **Builds.** Android 0.3.127 published 09-22 and iOS 0.3.40 released 09-23 (`D06477JGUKT/2025-09 /183`, `/186`), so Vincent's 09-24 checks stand. Later builds (Android 0.3.133, iOS 0.3.49) do not conflict.
- **Code strings.** All six client strings, the four-week repeat, `FirstTurorialFinished = 20` (rc_4), and the headline emoji differences against the sheet are as seeded. Commit titles after #248 add no new message. Blobs were not read, so "not in NotificationManager yet" rests on hunks and commit titles.
- **Feature states.** Hourly Collection in Backlog, Axe Arena and Rewarded Ads on Oct 21, Season Pass, Infinite HP Boss and Win and Collect on the BETA list, Collect & Win's three shared windows, Season Pass level 30, Endless daily entries.
- **Thread counters.** #zombie-art 3 to 4 replies and users, DM parent 0 to 1.
- **Speakers.** All four seeded Slack speakers are members of their channels. Both DMs are the right pairs.
- **Trello.** Badge counts, action id timestamps, card and list ids.
- **Gmail and Slack stamps.** `internal_date`, Slack `ts` against `created_at`, and weekdays.
- **Calendar.** The 10am CST invite equals 16:00Z in Samuel's El Salvador zone.
- **Linear lifecycle.** No comment after `completed_at`, no comment before creation, `updated_at` covers the last comment, sequences are contiguous, the counter is 346, relations are symmetric and ZOM `updated_at` moves forward.
- **Drive.** Parent folders exist, and doc length matches `style_runs`.
- **Absence.** No seeded author had left. No seeded act falls on an absence stated in #company-internal for September, and September calendar events show no out-of-office entry. Absences stated only in DMs were not swept.
- **Warehouse.** `USER_COHORT_RETENTION` has zombie_match_3d rows for 2025-09-15 on both platforms, with D1 and D7.
