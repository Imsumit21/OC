# Coherence sweep, rev2 overlay

Clock: Oct 1, 2025 00:00 Pacific (07:00 UTC), synth-cut universe.
Overlay read: `Task_Authoring/task_inputs/01_Universe_Inject.sql`, all 122 INSERT and 11 UPDATE statements, as data only.
Base read: only through `hg.py search` (search, search-many, get, get-many). No SQL was run. No universe file was opened directly.
Not read: `01_Scenario_Design.md` and everything under `Working_Files/`.

Result: no blocking finding. Three major findings, twelve minor ones. The records named in the brief (rows 18 and 34, ZOM-576, ZOM-582, both thread replies, both counter UPDATEs, the "Android 2006" post, Arthur's doc) all agree with the base on build branch, build time and PR merge time.

Pointers below are `service file pointer`. Slack channel files are `messages/<CHANNEL>/2025-09.json`.

## 1. Base facts the overlay depends on (all checked)

### Builds (#builds, C05433XK267, 2025-09.json)

| Build | Branch in post | Post time (UTC) | Pointer |
|---|---|---|---|
| iOS Internal #1698 | QueueManager (feature) | Sep 24 18:07:59 | /854 |
| Android #1974 | main | Sep 24 23:13:29 | /902 |
| iOS Internal #1713 | main | Sep 25 11:27:10 | /913 |
| iOS Internal #1718 | QueueManager (feature) | Sep 25 | /926 |
| iOS Internal #1727 | main (merge of #465) | Sep 25 22:21:13 | /959 |
| Android #1984 | main | Sep 25 22:21:58 | /960 |
| Android Submission #129 | main | Sep 26 02:39:16 | /972 |
| Android #2006 | main | Sep 29 15:39:23 | /1053 |
| iOS Internal #1745 | main (Collect And Win #468) | Sep 29 16:19:18 | /1058 |
| iOS Internal #1746 | AnimatedIcons (feature) | Sep 29 19:24:18 | /1068 |
| Android #2010 | main | Sep 29 19:26:38 | /1069 |
| Android #2013 | main | Sep 29 23:34:42 | /1075 |
| iOS Internal #1750 | main | Sep 30 01:55:54 | /1084 |
| iOS Internal #1754 | main (merge of #472) | Sep 30 16:01:21 | /1107 |
| iOS Internal #1756 | main (merge of #475) | Sep 30 16:14:48 | /1115 |
| iOS Internal #1757 | main | Sep 30 18:43:07 | /1119 |
| Android Submission #135 | main | Sep 30 20:13:09 (started 18:45:34) | /1124, /1122 |

### PRs (github data.json)

| PR | Author | Merged (UTC) | Pointer |
|---|---|---|---|
| #465 | Calvin | Sep 25 22:15:51 | /pull_requests/2369 |
| #472 | Calvin | Sep 30 15:53:04 (opened Sep 29 22:36:36) | /pull_requests/2377 |
| #473 | Oliver | Sep 30 15:41:20 (opened 15:41:05) | /pull_requests/2378 |
| #475 | Calvin | Sep 30 16:09:15 | /pull_requests/2380 |

### Thread roots and counters

- #zombie-bugs root ts 1757939514.864549 (id 90084203…, /651): author Vincent, base `reply_count` 11, `reply_users_count` 3, `latest_reply` 1757947882.581049. Replies /652–/662: nine by Vincent, one each by EMPLOYEE_0032 and EMPLOYEE_0033. The UPDATE to 12 / 3 is right; Vincent was already a replier.
- #zombie-bugs root ts 1757467270.178829 (id 51696f36…, /461): author Robert, base 4 / 1, all four replies by Robert (/462–/465). The UPDATE to 5 / 1 is right.
- #zombie-prs roots: #472 /589 base 3 / 1 → 4; #473 /605 base 2 / 1 → 3; #475 /622 base 3 / 1 → 4. All right.
- Trello board 6851a6569f3bf818760632ab base `dateLastActivity` 2025-09-30T17:09:07Z; the UPDATE to 17:22:36Z is later. idShort 80 is free on that board (highest is 79, /cards/802). PERSON_6094 is Leonard Hayes (/members/2).

### Membership

- Vincent (EMPLOYEE_0012), Robert (EMPLOYEE_0016) and Calvin (EMPLOYEE_0006) are all in #zombie-bugs (channels.json /127). Robert and Calvin are in #zombie-match3d (/108). The bot and Calvin are in #zombie-prs (/134).
- D0770ET6WBW is Brian–Calvin (/731), D06UPGF5PQV is Vincent–Calvin (/684), D05U73FNDDL is Marcus–Calvin (/571).

### Linear

- ZOM-566 is the highest base ZOM number, created 2025-09-30T16:26:02Z (/issues/3643). ZOM-567 at 16:43:18Z follows it. ZOM-567…584 do not exist in base.
- Base Linear has no comments collection, so every seeded `sequence` is free.
- ZOM-543 (/issues/3618), ZOM-556 (/issues/3632) and ZOM-560 (/issues/3637) exist with the titles the overlay assumes.

## 2. Major findings

### M1. Leonard organises and moves a review into days he said he is away

- Seeded: gcal `evt_0e5a1e82445aa0f1f7e4b9` and its five copies; the ten invite mails; Trello actions `68daad83bacf52c6ea7ee56b`, `68dc11bd3f45a368c395dca8`, `68dc11dceb76ad640995fd98`. Leonard creates the review for Fri Oct 3 and on Sep 30 moves it "up a day" to Thu Oct 2.
- Base: slack `messages/C07C2866011/2025-09.json` /506 (ts 1757792373.895399), Leonard: "tickets are booked - Oct 1st afternoon I'm leaving, coming back on Oct 3rd" (the Griffin event, /503–/505).
- Both dates fall inside that trip, and the move puts the meeting on the one full day he is away. He could dial in, but nothing says so.
- Repair: add a clause to the update note ("I'll join from the hotel"), or make Brian the organiser and keep Leonard as a guest.

### M2. Brian's "that sheet is the list" can be read as excluding Vincent's own Slack reply

- Seeded: Linear `comment_faaa792418a942cd40be046d8d217a7d` on ZOM-543: "For Vincent that sheet is the list, so don't add things from his chats". Slack `b156fdcd5fd89b8362d0e5fcf24975d1` (ts 1759267212.418339), Vincent re-seeing row 9 on Submission 135.
- Row 9 says "nr iOS Internal #1745". Under Arthur's doc the pass stops standing: Submission #135 is a main build from Sep 30 20:13, after #1745 on Sep 29 16:19. Under a plain reading of Brian's sentence a reader may keep row 9 Passed because the sheet is "the list" for Vincent.
- The two readings give different counts for Passed, Waiting on a fix and Daily Gift's area status.
- Repair: narrow Brian's sentence to new reports, for example "so don't add new reports from his chats".

### M3. The Fix column and four tickets say "the dev told me", but the dev is the persona and no such message exists

- Seeded: gdocs `f_d3a1aa5976285aac98ffda` ("Fix: the PR the dev told me it went into"); sheet rows 1, 2, 5, 12, 17, 18, 25, 31–34; Linear comments `comment_0382ec12…` (ZOM-571), `comment_50cf911b…` (ZOM-576), `comment_c7577240…` (ZOM-581), `comment_c1260bb5…` (ZOM-582), each "I was told".
- #465, #472 and #475 are all Calvin's PRs. The base Vincent–Calvin DM ends on Sep 25 17:31 (D06UPGF5PQV /176) and never gives a PR number. The overlay adds nothing from Calvin.
- Two of the attributions are wrong according to Arthur's own review comments (row 12 not in #472, row 32 not in #475). So the persona appears to have misinformed QA with no trace, and a solver playing Calvin cannot find what he said.
- Repair: change the legend and the comments to something Vincent can do alone, for example "Fix: the PR I matched it to in #zombie-prs", and "I think this went into #472".

## 3. Minor findings

### m1. Brian's comment refers to an ask he had not yet made
- `comment_faaa7924…` at 2025-09-30T20:25:37Z ends "Slide: the five numbers I asked you for". The ask is slack `446ba45665ed73d2f06caca6963c6ffc` at 20:40:05Z, 14 minutes later.
- Repair: list the five counts in the comment, or write "the five numbers I'll ask you for".

### m2. Row 10 is blank but its ticket says it was re-tested
- Sheet row 10 Re-test is empty; the legend says blank means not re-tested. Linear `comment_062192746d6b79d78445f5875195704c` on ZOM-570: "Still the same on Android 2013 today."
- Status does not change (Waiting on a fix either way).
- Repair: put "again Android #2013" in row 10, or drop the build from the comment.

### m3. ZOM-582 re-test comment is seven minutes after the build post
- `comment_c1260bb5e2f487f140864352f77ae1c5` at 18:50:28Z names iOS Internal 1757. The build post is at 18:43:07Z (/1119). Rows 31 and 33 were also tested on that build.
- Repair: move the comment and ZOM-582 `updated_at` to about 19:15Z, still before the sheet's 19:30:52Z.

### m4. Submission 135 play time is tight
- Robert `a40824773b7cad9681d141b916a5f558` at 21:44:12Z says he played "for an hour"; the build finished at 20:13:09Z, 91 minutes earlier. Vincent's reply is 67 minutes after it.
- Repair: move Robert's reply to about 23:30Z and its `latest_reply` with it.

### m5. Vincent's reply has no antecedent in the thread it sits under
- `b156fdcd…`: "the pass popup came up on top of the gift again. so that one is not gone". The Sep 15 list (/651–/660) never mentions that bug. Vincent opened a fresh #zombie-bugs thread the same day (/1091, 16:24Z) and told Calvin at 19:33Z that the sheet was up to date (`cfee08a8…`).
- Mitigation found in base: Vincent did reply 25 days late under an old thread (/920, Sep 22, under an Aug 28 root).
- Repair: drop "so that one is not gone", or make it self-contained ("couldn't get this one yesterday").

### m6. Robert's two posts sound like he has read the sheet
- `ecf80487a68281b5eb011679ad0e5004` ("I could still tap the arena entry button") and `a4082477…` ("Thought that was sorted"). The sheet is not shared with Robert, and the first post nearly repeats row 27. Robert reports bugs in #zombie-bugs in base; this one is in #zombie-match3d.
- Build naming is fine: base uses "android 1977", "Android submission 120".
- Repair: drop "still" and "Thought that was sorted".

### m7. Oliver's #473 comment reads as a pointer
- github `harmonygames-Games/match3d#473#c_2` at 15:42:10Z, 50 seconds after he merged his own PR: "For the flow list: this also has the fix for…". It is addressed to nobody, and base Oliver writes short lowercase lines.
- Repair: put it as a reply to Vincent on ZOM-572 in Oliver's voice ("this one went in with the addressables PR"), or lower-case it and drop "For the flow list:".

### m8. Arthur's review comments follow his own merge by 35 seconds
- `#472#rev_2` at 15:53:40Z (merge 15:53:04Z) and `#475#rev_2` at 16:09:50Z (merge 16:09:15Z). No `reviewed` timeline event is seeded, and the Slack copies lack the "Review comment by" companion that base reviews have (/586).
- Repair: vary the two gaps; optional timeline rows.

### m9. Brian's comment is far more fluent than base Brian
- Base Brian writes short, non-native lines (D0770ET6WBW /177, /256). Sentences such as "If it is already a row, don't count it twice" and "as it stands today, one of three" read like grading rules.
- He did write the structured ZOM-543 description, so a list is in character.
- Repair: shorten two or three sentences into his register.

### m10. Row 25 wording differs from the base report
- Sheet row 25: "Boss arena tutorial does not play when another tutorial is queued before it". Base D06UPGF5PQV /150 (ts 1758807944.593249): "the boss arena tutorial plays again even if ı completed it".
- The "ok, chat" link still resolves (/169–/170, "Looks ok to me" / "Boss arena as well", after #1718 on the QueueManager branch).
- Repair: reword row 25 to "Boss arena tutorial plays again after it was completed".

### m11. Arthur's Sep 12 doc sits two days after a "different branch for submission build"
- Base D0770ET6WBW /176 (Sep 10): Calvin says Blake told him there is a different branch for the submission build. The doc `f_6d0326fa006b136f1bbf82` says only main counts. Not a contradiction, since late-September submission builds are on main.
- "whoever saw it" is slightly anticipatory but reads as an engineer's rule. The job names and "the branch is in its #builds post" are true.
- Repair: none needed.

### m12. Small loose ends
- Sheet footer names "my pass sheet legend doc"; the doc title is "How to read my pass sheets".
- ZOM-567: Oliver "I'll try with a fresh account tomorrow". ZOM-578: Samuel "checking". Both leave the state clear.
- Nobody answers Robert's two posts or Arthur's two review comments.

## 4. Checks that passed

- Every seeded timestamp is before 2025-10-01T07:00Z. The latest is Robert's reply at 2025-09-30T21:44:12Z.
- Row 18: found on Android #2010 (Sep 29 19:26), "again Android #2013" (Sep 29 23:34), fix #472 merged Sep 30 15:53. The re-test predates the merge, and Arthur's comment confirms the two Collect & Win rows are in the diff. ZOM-576 agrees (In Validation, "My last try was Android 2013").
- Row 34: found on Android #2006 (Sep 29 15:39), "again iOS Internal #1757" (Sep 30 18:43), after #475 merged at 16:09. ZOM-582 agrees (Todo).
- Robert's "Android 2006" post: #2006 was built 40 minutes before iOS #1745, so row 27's pass stands under the doc. Robert's Submission 135 reply: after iOS #1750, so row 29 reopens.
- Every "Found on" build is older than its "Re-test" build. All recorded re-tests are on main builds. Only the three "ok, chat" rows rest on a feature-branch build (#1718).
- Sheet `modified_time` 19:30:52Z is after the last re-test build (18:43Z) and the last ticket it lists (ZOM-584, 18:44Z).
- All 18 ticket titles, "Seen on" builds and keys match their sheet rows. Each ticket's `updated_at` equals its last comment. Creation times rise with the numbers.
- Brian's anchors exist: the parked input blocker (D0770ET6WBW /256), Oliver's skip-tutorial exception thread (C08R27X0EAH /1057), Julia's point about Calvin's tickets (C090N54TG79 /84, copied to Calvin in D05HYDTG5TJ /0), Bug Checklist canvas (C08R27X0EAH /180), Collect&Win issues canvas (C09EVVCFHKR /35).
- No base DM to Calvin since Sep 26 reports a home-screen bug seen in a build, so Marcus's seeded DM is the only extra report. Checked: D051LNQSFGQ, D05S1S2H55M, D05U73FNDDL, D0770ET6WBW, D07GJJBK789.
- ZOM-556 comment "Saw this one myself" fits base: Vincent had said it was Leonard's feedback (D06UPGF5PQV /95).
- Agenda agrees across the Trello card, the update mail note and Brian's Sep 30 DM. The Sep 29 DM, first invite and first card description are consistently the older version.
- Meeting times agree across zones: 18:00Z is 12pm CST, 2pm EDT, 9pm Türkiye.
- Seeded GitHub ids do not collide; the issue-comment and discussion ids fall between base neighbours in time order. File paths in the diff hunks exist in base review text.
- Gmail threads for #472 and #475 exist for Calvin.

## 5. Not checked

- Slack message id and ts collisions across all history, and Gmail and gcal id collisions (lint scope).
- Whether Calvin can read the Trello board and the two docs' parent folders (persona reach).
- The contents of the Bug Checklist and Collect&Win canvases.
