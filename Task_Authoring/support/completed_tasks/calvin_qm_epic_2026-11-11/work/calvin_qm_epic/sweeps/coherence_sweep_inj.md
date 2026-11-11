# Coherence sweep — injected records (`01_Universe_Inject.sql`)

Clock: 2025-10-01 07:00 UTC (Oct 1, 2025 synth-cut universe).
Reviewer: independent, did not author the SQL. Base read only through `Task_Authoring/tools/hg.py search`.
Not read: `Working_Files/` (design, manifest, plan, solver), `Evals/`, other tasks.

Scope: 120 INSERT + 8 UPDATE across gdrive, gdocs, gsheets, gslides, slack, trello, gcal, gmail, github, linear.

Result: **2 BLOCKING, 8 MODERATE, 14 MINOR.**

---

## BLOCKING

### B1 — Deck says Collect & Win is already in the queue, one week before it was (temporal + semantic)
- **Seeded:** `gdrive.drive_files f_637e63ae6c1b4a7eb016aa` and `gslides.slides_presentations f_637e63ae6c1b4a7eb016aa` (created = modified = 2025-09-23T16:20:00Z); element `el_5d0ae0441e73`: "A new Live-Op adds its own order to the queue with EnqueueEvent. Collect & Win went in this way."
- **Base:**
  - slack `messages/D0770ET6WBW/2025-09.json` `/252` (Brian, 2025-09-24 16:22Z): "collect&amp;win event is almost ready to merge, we need to integrate it to queue manager too"; `/253` (Calvin): "I'll need to add it to the queue manager once is merged"; `/256` (Sep 25): "after adding collect&amp;win to queuemanager".
  - github `/pull_requests/2372` (#468 Collect And Win) merged 2025-09-29T16:13:50Z; `/pull_requests/2377` (#472 Implement Win&Collect into Queue Manager) created 2025-09-29T22:36:36Z, merged 2025-09-30T15:53:04Z.
  - github `/pull_request_comments/655` (CodeRabbit walkthrough of #472): the change is in `RewardVFXManager.cs` (awaits `GetCollectAndWinStatusRoutine`) and `CollectAndWinProgressController.cs`; no `EnqueueEvent` call is added for Collect & Win.
- **Conflict:** a deck last modified Sep 23 states in the past tense something that happened Sep 29–30. It also says Collect & Win was added "with EnqueueEvent", while the base PR gates it inside the reward VFX coroutine.
- **Smallest fix:** change the body of `el_5d0ae0441e73` to "A new Live-Op adds its own order to the queue with EnqueueEvent. Collect & Win is next." (keeps the Sep 23 dates and matches Brian's Sep 19/24 chat). Alternative: keep the text minus "with EnqueueEvent … this way" and set `modified_time` on both the drive row and the presentation row to after 2025-09-30T15:53:04Z.

### B2 — Vincent says he is waiting for a main build that already exists and that his own sheet uses
- **Seeded:** `linear.linear_comments comment_50cf911b05625950a80c7a90de50b5f3` on ZOM-576 (2025-09-30T17:39:55Z): "I was told #472 has this. Waiting for a main build to check it."; `comment_0382ec127c135a8e78e6e46d3ae6bde7` on ZOM-571 (17:07:57Z): "I will check it when it is in a main build."; sheet `f_cb40955893624e1acb8500` row 17: Fix `#472`, Re-test `ok iOS Internal #1754`.
- **Base:** slack `messages/C05433XK267/2025-09.json` `/1107` (2025-09-30 16:01:21Z): "Match 3D iOS Internal - #1754 - main Success … Merge pull request #472".
- **Conflict:** at 17:07 and 17:39 the main build with #472 had existed for over an hour, and the same author records a pass of another #472 row on that exact build. The two comments contradict both the base build log and the seeded sheet.
- **Smallest fix:** reword both comments so they do not claim a missing build: ZOM-571 "I was told this went into #472. Not re-tested yet."; ZOM-576 "I was told #472 has this. Not re-tested yet."

---

## MODERATE

### M1 — Seeded reviews are numbered after base reviews they precede
- **Seeded:** `github.github_reviews harmonygames-Games/match3d#472#rev_2` (submitted 2025-09-30T15:51:43Z, seq 2) and `…#475#rev_2` (16:08:21Z, seq 2), with `…#472#rc_1`, `…#475#rc_1`.
- **Base:** `/reviews/2179` `…#472#rev_1` APPROVED 2025-09-30T15:52:58Z; `/reviews/2180` `…#475#rev_1` APPROVED 16:09:09Z. Base numbering is strictly chronological (`…#470#rev_1`…`rev_9`, `/reviews/2168`–`2176`).
- **Conflict:** rev_2 is earlier than rev_1 on both PRs.
- **Smallest fix:** move both seeded comments to just after the base approval/merge (for example #472 at 15:53:40Z, #475 at 16:09:50Z) and carry the new time into: review + review_comment rows, the two Slack copies (`061aadc8…`, `4fafdea4…`: `ts`, `created_at`, attachment `ts`, and the id, which is `sha256(channel|ts)[:32]`), the parents' `latest_reply` (then the seeded reply is the latest), and the two Gmail rows (`internal_date`, `date`, Date header). Brian's rule ("if the review on it says a fix is not in there") still holds.

### M2 — Arthur's seeded #472 comment lands in the middle of his merge run on other PRs
- **Seeded:** `…#472#rc_1` at 15:51:43Z.
- **Base:** Arthur approves/merges #470 at 15:51:06/15:51:15 (`/reviews/2176`, `/timeline_events/10964`), #471 at 15:52:15/15:52:24 (`/reviews/2178`), #472 at 15:52:58/15:53:04.
- **Conflict:** a considered inline comment on #472, citing the QA sheet, appears 28 s after he merged #470 and 32 s before he approved #471, then he returns to #472. Same pattern for #475 (comment 48 s before approval) is fine on its own.
- **Smallest fix:** same shift as M1 (post-merge comment).

### M3 — Brian mentions "the flow review on Friday" before the review existed
- **Seeded:** `slack.slack_messages 62f56e59f20df00440a47d6c851af3af` (D0770ET6WBW, 2025-09-29T11:20:12Z).
- **Seeded siblings:** card `68daad83bacf52c6ea7e1593` created 16:02:11Z; gcal events created 16:05:05Z; invite mails 16:05:14Z.
- **Base:** Brian's posts in this DM in the last two weeks start at 13:58Z or later (`/255`, `/247`, `/217`); KB core window 15:00–00:00 local (UTC+3).
- **Conflict:** he cites the meeting and its agenda 4 h 42 min before any record of it, at an hour he does not post in this DM.
- **Smallest fix:** move the message to 2025-09-29 after 16:05Z, for example 16:41:12Z (new `ts`, `created_at`, and id = sha256 of `D0770ET6WBW|<ts>`). It still precedes his base 19:24Z messages.

### M4 — ZOM-581 comment promises a re-test on the next main build; the sheet shows he was on that build and left the row blank
- **Seeded:** `comment_c757724005e45903d91d6a340d34bab9` on ZOM-581 (18:22:34Z): "I will re-test on the next main build."; sheet rows 31 and 33 `ok iOS Internal #1757`, row 32 (the ZOM-581 row, same pack screen) Re-test blank; sheet modified 19:30Z.
- **Base:** `messages/C05433XK267/2025-09.json` `/1119`: iOS Internal #1757 main, 2025-09-30 18:43:07Z.
- **Conflict:** he re-tested two card-pack rows on #1757, the next main build, yet the sound row from the same screen has no result ("again" would be expected under his own legend).
- **Smallest fix:** reword the comment to "I was told #475 has it. Not re-tested yet." (no promise tied to the next build).

### M5 — Brian's two long instructions are out of voice and read as a specification
- **Seeded:** `linear.linear_comments comment_faaa792418a942cd40be046d8d217a7d` on ZOM-543 (about 2,400 characters of decision rules, status definitions, sheet tab names and columns); `slack 446ba45665ed73d2f06caca6963c6ffc` (one 620-character message).
- **Base:** Brian's DM messages are short and split over several posts (`messages/D0770ET6WBW/2025-09.json` `/247`–`/252`, `/255`–`/258`, `/263`–`/267`; KB median 41 chars, IM p99 354). His longest base texts are short bullet lists on a canvas (`messages/CF4EDAF93359/2025-09.json` `/91`). The base Linear export has no comments at all (`/comments` is `[]`), so there is no base precedent for Brian commenting in Linear.
- **Conflict:** voice and realism; the comment states every rule a grader would need in one place.
- **Smallest fix:** split the DM into 3–4 consecutive short posts a few seconds apart; split the Linear note into 3–4 comments posted over a few minutes and loosen the wording (short sentences, his "collect&win" spelling, fewer defined terms).

### M6 — Arthur's two rule docs do not look like anything he keeps
- **Seeded:** `f_6d0326fa006b136f1bbf82` "ZM builds and QA passes" (2025-09-12) and `f_ea7517885d11570b54bf13` "DD hotfix builds and QA passes" (2025-07-10), each a title plus two or three sentences, shared with eight people.
- **Base:** Arthur's Drive documents are uploaded `.docx` files, mostly 2023 legal papers (`/drive_files/53491`, `/52449`, `/51938`), unshared or shared with two people. No base message states a rule that a QA pass needs a main build; the base practice is the opposite order (Vincent passes the feature-branch build, then Calvin merges: `messages/D06UPGF5PQV/2025-09.json` `/126`, `/158`, `/169`–`/172`; `messages/D051LNQSFGQ/2025-09.json` "[Vincent] just tested and seems okay").
- **Conflict:** tool/realism; a two-sentence policy doc with a matched decoy twin reads as planted, and nothing in the base refers to it.
- **Smallest fix:** give the ZM doc a little ordinary surrounding content (job names, who triggers builds) or move the rule to a place Arthur writes in the base (a #zombie-match3d post around Sep 12). Keep the decoy only if it has similar body.

### M7 — Human PR comment on match3d gets a Slack copy, against the base rate
- **Seeded:** `slack 66dd5332dde5b7312c0ae201c285a323` (copy of `…#473#c_2`, Oliver).
- **Base:** KB `integrations.md` copy rates: `match3d/human: 0 / 2` (human issue comments on match3d have no Slack copy); inline review comments by humans are copied (`messages/C093LEZGF6J/2025-09.json` `/596`).
- **Conflict:** the only two human issue comments in the base were not mirrored; the seed mirrors one.
- **Smallest fix:** accept (sample of 2) or drop the Slack copy and the parent `reply_count`/`latest_reply` update for `d05a2f8a…`; the GitHub row alone carries the fact.

### M8 — Vincent files ZOM-572 as Todo 90 minutes after the assignee wrote that it is fixed, and the assignee says nothing
- **Seeded:** `…#473#c_2` (Oliver, 15:42:10Z: "has the fix for the pass start popup coming back after every level"); ZOM-572 created 17:13:09Z assigned to Oliver, Todo; Oliver comments on ZOM-567 (17:41Z) and ZOM-573 (18:06Z) but not on ZOM-572.
- **Conflict:** not a hard contradiction, but Oliver answers the tickets around it and stays silent on the one he says he fixed. A reader sees an open ticket and a "fixed" claim by the same owner within two hours.
- **Smallest fix:** none required if this is the intended trap; otherwise add a one-line Oliver comment on ZOM-572 pointing at #473, or note it as accepted.

---

## MINOR

| # | Category | Seeded record | Base / detail | Fix |
|---|---|---|---|---|
| m1 | Identifier | Slack `66dd5332…` pretext `issuecomment-3352791644` (comment at 15:42:10Z) | Base ids rise with time: `3352799089` at 15:41:13Z (`/606`), `3352800975` at 15:41:50Z (`/610`), `3352864685` at 15:59Z (`/623`) | Use an id between 3352800975 and 3352864685, e.g. `3352803412` |
| m2 | Format | `gslides` pages/elements: layout `TITLE_AND_BODY`, kind `SHAPE`, placeholder `TITLE`/`BODY` | No base slide uses these values (0 hits); base is `BLANK` / `TEXT_BOX` / null placeholder, one full-page element (0,0,9144000,5143500) | Optional: one `TEXT_BOX` per page, layout `BLANK` |
| m3 | Format | Gmail invite rows: `attachments_meta_json '[]'`, no "Join by phone" / "View all guest info" blocks | Base invites carry one `.ics` attachment and those blocks (`threads/vincent@harmonygames.co_1841731360839916865.json`, `threads/calvin@harmonygames.co_1842730511532657146.json`) | Optional: add the blocks; attachment meta if the table allows |
| m4 | Format | Invite bodies list `julia.lawson@harmonygames.co` under Guests | Base guest lists show her as `[PERSON_NAME_0043]` (`calvin@…_1842730511532657146.json`); the seeded subject in Julia's mailbox already uses that token | Replace the guest line with `[PERSON_NAME_0043]` |
| m5 | Format | GitHub notification mails: body ends `…/review/3285698310@github.com>`; `in_reply_to`/`references` NULL; Date header `+0000` | Base bodies mask the id (`…/review/[EMAIL_27678]>`), rows carry `in_reply_to` and `references`, Date is `-0700` (`calvin@…_1844639618018823785.json` `/messages/0`) | Fill `in_reply_to`/`references`; mask the body id |
| m6 | Format | Trello card `url` slug `…-fri-oct-3` while name is "Thu Oct 2" | Real Trello re-slugs on rename; base cannot confirm either way | Slug `80-zm-home-screen-flow-review-thu-oct-2` |
| m7 | Identifier | Trello createCard action id `68daad83e56b4cde943fa23d` vs card `68daad83bacf52c6ea7e1593` | Base pairs share the first 20 hex chars (`68d1eb90bef538c7c5c5599d` / `…59bc`, `/actions/5244`) | Action id `68daad83bacf52c6ea7e15b2` style |
| m8 | Semantic | Meeting-agenda card on ZM ROADMAP → Backlog | Backlog cards are feature ideas ("Fake PvE Coop", "Revisit All Boosters", `/actions/5190`, `/5176`); Leonard does create cards there | Accept |
| m9 | Voice | Sheet/meeting name "home screen flow" | Brian and Vincent say "main menu" / "homepage" (ZOM-543 description; canvas `C3DD99314033` `/48`); Robert and Samuel say "home screen" | Accept or rename "ZM main menu flow pass" consistently |
| m10 | Voice | ZOM-556 comment "Saw this again in my home screen pass" | Base: Vincent "couldn't test it, it's Leonard's feedback" (`D06UPGF5PQV` `/95`) | "Saw this one myself in my home screen pass on 1727…" |
| m11 | Temporal | Vincent thread reply `b156fdcd…` at 21:20Z (00:20 local) | Outside his KB core window (13:00–22:00 local); he does post at 21:31–22:04Z on Sep 24 | Accept |
| m12 | Realism | 39 seeded Linear comments | Base `/comments` is empty although Slack mentions Linear comments (`D05U73FNDDL` `/131`); the seeded ones would be the only comments in the workspace and their id format cannot be checked | Accept; note in dossier |
| m13 | Realism | Rows 1, 2, 5, 25 etc. cite builds from Sep 24–25 | Sheet created Sep 26 09:12Z; back-filled rows are plausible but the DM says "I started a sheet for it today" | Accept |
| m14 | Format | gcal copies set `"self": true` on each owner's own attendee entry | Base copies checked show `self` only on the organizer in the organizer's calendar (`/events/1055`); attendee copies not verified | Accept |

---

## Known data issues touched (SC cards)

- **SC-6** (brian.foster@ address also used by Node's CEO): the seeds share files with and write invite mails into `brian.foster@harmonygames.co`. They use the address only as the HG engineer; nothing depends on the ambiguity. No change needed, but no deliverable should ask "who is Brian".
- **SC-13 / SC-14** (ZM ROADMAP "BETA" list name and dueComplete flags): the seeded card is on the same board but on the Backlog list (`68c451221ebabaf255a7d16b`); it does not touch the BETA list or cards 54/56/58/67. The base Sep 30 16:40–17:09Z actions on that board are Leonard's, which supports him being on the board at 17:22Z.
- **SC-16 / SC-30** (Linear state is not proof of shipping; Done parents with open children): Brian's note decides status from PRs and builds, not Linear state, which avoids SC-16. The epic the task creates will have a parent and children; do not grade the parent's state as implying the children's.
- **SC-18** (#477 state): not used. #473 carries the same CodeRabbit "pull request is closed" text, but #473 is merged in both the PR row and timeline, so the seeded comment on it is safe.
- **SC-38** (Season Pass ship date / analytics): seeded Season Pass rows are bug reports only; Owen's "after the analytics ticket" refers to ZOM-566 (Collect&Win Analytics, assigned to Owen), not ZOM-552.
- **SC-57** (#zm-collect-win archived but active): not used.
- **SC-70** (time zones): invite mails rely on calendar zones. Calvin CST, Arthur EDT and Vincent "Türkiye Time" match base invites; Brian's and Julia's could not be matched to a base 2025 invite.
- No seeded record touches SC-8, SC-15, SC-22, SC-26, SC-56, SC-67 or the finance/investor cards.

---

## Verified consistent

**Builds (#builds C05433XK267, 2025-09).** Every cited build exists with a result post before the record that cites it: iOS Internal #1698 (Sep 24 18:07Z, QueueManager branch), #1713 (Sep 25 11:27Z, main), #1727 (Sep 25 22:21Z, main, merge of #465), #1745 (Sep 29 16:19Z, main), #1746 (Sep 29 19:24Z, AnimatedIcons branch), #1750 (Sep 30 01:55Z, main), #1754 (Sep 30 16:01Z, main, merge of #472), #1757 (Sep 30 18:43Z, main); Android #1974, #1984, #2006, #2010, #2013 (all main); Android Submission #129 (Sep 26 02:39Z), #135 (Sep 30 20:13Z). Each "Found on" precedes its "Re-test" build. Sheet "Found on" matches each ticket's "Seen on" line for all 18 tickets. The "ok, chat" rows (1, 2, 25) resolve to Vincent's base "Looks ok to me / Boss arena as well" on iOS Internal #1718, a QueueManager branch build (`D06UPGF5PQV` `/158`, `/169`, `/170`; `C05433XK267` `/926`).

**Bug facts against base PRs and chats.** #465 body covers coin replay and back-to-back tutorials (rows 1, 2, 5); #475 body covers the "Tap anywhere to collect" prompt and last-pack reveal (rows 31, 33) and no sound change (matches Arthur's comment); #472 walkthrough covers only the Collect & Win wait (matches Arthur's comment); #456 (animated icons incl. Season Pass icon) merged Sep 24, before Android #1984 (row 12); #468 Collect And Win merged Sep 29 16:13Z, before every Collect & Win row's build. Level-20 win streak tutorial freeze matches Calvin's Sep 23 chat. "Input blocker parked" matches Brian's Sep 25 message. "Oliver's tutorial skip work" matches #466/#467/#474. Both canvases Brian names exist (`FC:F09BZ9R1NFM:Bug Checklist`, `FC:F09FNQM8EBZ:Collect&Win issues - zm - ios 1730`). ZOM-556 and ZOM-560 are the daily-gift and abandoned-pack freezer tickets, created by Vincent. Slide 2 repeats the ZOM-543 description; `EnqueueEvent` exists in the base QueueManager.

**Linear.** ZOM-566 is the last base ticket (created Sep 30 16:26:02Z); ZOM-567…584 are created 16:43–18:44Z in number order; every `updated_at` equals the last seeded comment; ZOM-543/556/560 `updated_at` moves forward. User ids resolve (Vincent, Calvin, Oliver, Owen, Samuel, Brian). "In Validation" is a base ZOM state; "Bug" is a base label. Sheet has 18 ticket keys = 18 tickets; 10 areas in the sheet = 10 children in Brian's note.

**GitHub / Slack copies / Gmail.** PR ids, authors (Calvin authored #472 and #475, Oliver #473), merged states and file paths match. `…#473#c_2` and `ev_5` follow base `c_1` and `ev_4`. Slack copies match the base bot shape field for field, use the commenter in the pretext as the base does, thread under the right "opened" parents, and the three parent counters are right (3→4, 2→3, 3→4; `latest_reply` kept where a later base reply exists). `discussion_r` ids fall between base ids of the same day. All 12 Slack ids equal `sha256(channel|ts)[:32]`; `created_at` equals `ts`. Gmail thread ids exist for #472 and #475 in Calvin's mailbox, encode the right times, and the "@login commented on this pull request." form matches 2025 base mails.

**Slack humans.** DM channels are the right pairs (Brian, Vincent, Marcus with Calvin). #zombie-bugs thread `d0dd5d3a…` had 4 replies from 3 users including Vincent; seeded counters 5/3 and `latest_reply` are right. Robert posts in #zombie-match3d at similar hours. No base DM to Calvin since Sep 26 reports a home-screen bug, so Marcus's seeded DM is the only one of its kind.

**Trello.** Board, list and member ids resolve (PERSON_6094 is Leonard, who creates cards on this board); idShort 80 follows base 79; object ids encode the action dates; `pos` and board `dateLastActivity` move forward.

**Calendar and invites.** Oct 2, 2025 is a Thursday and Oct 3 a Friday; 18:00Z is 12pm CST, 2pm EDT, 9pm UTC+3. Six per-calendar copies with one `ical_uid` match the base pattern. Card (16:02Z) → event (16:05:05Z) → mail (16:05:14Z); card edit (17:22Z) → event update (17:24:03Z) → mail (17:24:09Z). "Changed: time, description" matches the two descriptions. Organizer block and note layout match base Leonard invites. No base event named for a flow review or queue manager competes.

**Drive / Docs / Sheets.** The three parent folders exist and are the owners' roots; ids follow `f_`/`d_` + 22 hex; doc ids equal drive ids; `style_runs` end offsets equal body lengths (430, 296, 146). Vincent owns 48 base sheets, Calvin 3 decks.

---

## Could not check

- Brian's and Julia's calendar time-zone label ("Türkiye Time") against a base 2025 invite in their own mailboxes (none found by the file-name pattern used).
- "Julia's point about your tickets" (no priority / no assignee): no base record located; treat as unsupported background.
- GitHub review ids in the mail Message-IDs (3285698310, 3285755391) against base numbering.
- Whether any recurring base meeting overlaps Thu Oct 2 18:00–18:30Z for the six attendees (recurring events are stored by rule, not by instance).
- Full text of the two canvases (the export holds comment threads, not the canvas body); the visible items do not overlap a sheet row.
- Whether Arthur or Vincent created any Google-native doc or sheet in Jul–Sep 2025 (listing did not finish); findings M6 and m13 rest on the newest rows sampled.
- Slack/Linear/Gmail SQL columns that have no JSON counterpart in the export (`thread_ts_legacy`, `seq`, `sequence`, `history_id`, `size_estimate`).
