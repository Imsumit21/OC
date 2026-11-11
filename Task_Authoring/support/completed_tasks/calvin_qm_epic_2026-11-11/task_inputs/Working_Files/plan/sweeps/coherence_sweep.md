# Coherence sweep (synth-cut, clock Wed 1 Oct 2025)

Reviewer: independent, read-only through `hg.py search`. Pointers are `service file pointer`.
Slack files are `messages/<channel>/2025-09.json`. Severity: **B** = blocking contradiction, **S** = should fix, **F** = fine.

## Summary

The plan does not pass. Nine blocking findings:

1. **B1 Ticket numbers are out of order.** The last base ticket is ZOM-566, created 2025-09-30T16:26:02Z (linear `data.json /issues/3643`). Base numbers rise with creation time (ZOM-555 09-22 … ZOM-565 09-25 … ZOM-566 09-30). Seeds date ZOM-573 at 09-26T13:20Z and ZOM-578 at 09-23T19:30Z, and Vincent's comments on them at 09-29. All of ZOM-567…586 must be created after 09-30T16:26:02Z.
2. **B2 Sheet cites a build that did not exist yet.** Rows 31 and 33 say "ok iOS Internal #1757". That build finished 09-30T18:43:07Z; the sheet is dated 17:40Z. The main build that first held PR #475 is iOS Internal #1756 (16:14:48Z, `C05433XK267 /1115`) or Android #2025 (16:16:41Z, `/1116`).
3. **B3 The review premise is contradicted by three base records of the same afternoon.** Leonard marked the Trello card "Win and Collect" complete at 09-30T16:40:13Z (trello action `68dc07ed32024df62d868ca6`). Vincent wrote at 16:47:38Z "none of them blockers and doesn't affect the submission" about the open Collect & Win bugs (`C09EVVCFHKR /98`). Arthur started iOS Submission #50 at 18:43:32Z and Android Submission #135 at 18:45:34Z, and #135's change list contains "Collect And Win (#468)" (`C05433XK267 /1120, /1122, /1124`). An invitation sent at 17:22Z saying open Collect & Win items hold the publish sits between these.
4. **B4 Vincent and Brian already keep real QA lists, as Slack canvases.** "Bug Checklist" (F09BZ9R1NFM, channel `CF4EDAF93359`), which Vincent called the up-to-date list on 09-30T16:38:58Z (`C09EVVCFHKR /95`), and "Collect&Win issues - zm - ios 1730" (F09FNQM8EBZ, channel `C3DD99314033`). The hub's "everything else is in chats and in Vincent's pass sheet" and the note's "His sheet is his whole list" contradict them. They also hold reports that fit the scope sentence and are not among the 40 rows (see Other contradictions).
5. **B5 Rows 15 and 16 were first logged on 09-26, not on Android #2004 (09-29).** Canvas items `C3DD99314033 /69` (14:37:25Z) and `/72` (14:37:39Z) are these two reports word for word. The legend defines "Found on" as the first build.
6. **B6 Planned comment on PR #475 contradicts the PR's own walkthrough.** "The close lock is only on the last pack's reveal" against github `/pull_request_comments/658`: "CloseScreen now starts coroutine and disables close button", with the disable drawn for every close.
7. **B7 Gmail ids carry their time, and one lands after the clock.** Base ids decode exactly (id >> 20 = ms; thread 1842050583560498707 → 2025-09-01T08:45:31Z, header date 08:45:30Z). INV2 1844792240663158803 → **2025-10-01T15:02:59Z**. INV1 → 09-27T15:35:07Z (planned 09-26T18:05Z). Robert's mail → 09-29T15:22:45Z (planned 09-28T19:40Z).
8. **B8 Arthur Blake has never acted on Trello.** 0 of 5,252 base actions are his (member `2162c1ba310341bf318f48b7`). The rule that decides which passes count is planned as his card and comment.
9. **B9 Linear has no comments at all in the base** (`/comments` is `[]`). The epic note and both alias comments would be the only three. A base message even refers to a Linear comment that is not in the export (`D05U73FNDDL /131`).

Should-fix items follow per seed. Sheets, Docs and Slides checks are in "Other contradictions".

## Per-seed findings table

| Seed | Sev | Finding | Base pointer |
|---|---|---|---|
| hub | B | "everything else is in chats and in Vincent's pass sheet": two live canvases exist (B4) | `C09EVVCFHKR /94–/101`, `CF4EDAF93359 /107–/127` |
| hub | S | 23:10Z is 02:10 for Brian (calendar zone UTC+03:00). His 234 September messages in six channels all fall 10:00–21:11Z | gcal `/calendars` brian.foster; `D0770ET6WBW /216–/267` |
| epic_note | B | Only Linear comments in the universe (B9); id format cannot be checked against any base row | linear `/comments` |
| epic_note | B | Scope sentence "anything somebody else … raised since the 24th … wherever they wrote it" pulls in base canvas reports outside the 40 rows | see Other contradictions |
| epic_note | S | 22:48Z is 01:48 for Brian | as hub |
| epic_note | S | "went to main on the 24th": PR #459 merged 09-24T23:06:25Z, which is the 25th 02:06 in Brian's zone | github `/pull_requests/2362` |
| epic_note | S | "Julia's point about your tickets" covers priority only, not assignee | `D05HYDTG5TJ /0` |
| epic_note | F | "The input blocker I already parked" fits Brian's 09-25 message | `D0770ET6WBW /256` |
| epic_note | F | "Oliver's tutorial skip work": branch `tutorial/skip` builds and skip button are Oliver's | `C05433XK267 /931`, `C08R27X0EAH /1046` |
| gate_old | S | 15:10:12Z sits inside a burst of Brian's real posts in #zm-collect-win at 15:09:29, 15:10:00, 15:10:14, 15:10:28 | `C09EVVCFHKR /89–/92` |
| gate_old | S | "the C&W review on Friday" is written on Friday 09-26 and means Oct 3; the first invitation comes 3 h later | — |
| gate_old | S | 43 s earlier Brian wrote "The blockers in the Collect&Win event have been resolved" | `C09EVVCFHKR /89` |
| sheet | B | Rows 31, 33 re-test on #1757 (B2) | `C05433XK267 /1119` |
| sheet | B | Ticket column needs ZOM-567…586 to exist; they can only exist after 16:26:02Z (B1) | linear `/issues/3643` |
| sheet | B | Rows 15, 16 "Found on Android #2004" (B5) | `C3DD99314033 /69, /72` |
| sheet | S | Row 5 "ok, chat": Vincent's ok in chat is about the tutorials and Boss Arena. He never says ok on the coin replay; Calvin pointed him to #1716 for it and got "Thanks" | `D06UPGF5PQV /156, /157, /169, /170` |
| sheet | S | Rows 1, 2, 5 "Found on #1710 / #1974": Vincent reported them 09-24T21:33–22:00Z on branch builds, before #1710 (23:11:47Z) and #1974 (23:13:29Z) existed | `D06UPGF5PQV /133, /134, /138, /140` |
| sheet | S | Row 3 (hand pointer on Zombie Lane close button, Passed): Vincent logged "Hand pointing to close button on Zombie lane is not triggered after inactivity" on 09-30T12:50:24Z. Reads as "it is back" under the note's rule | `CF4EDAF93359 /109` |
| sheet | S | Row 20 "Nathan's chest": Nathan is a Domino Delights character (ENG tickets, DD build notes). No ZM channel mentions him; the ZM win streak event is "Axe Arena" | linear `/issues/2630`; `C05433XK267 /51`; trello card `6851a7a6c31a93809acded72` |
| sheet | S | Rows 31–33 found on iOS #1746: Calvin asked Brian, not Vincent, to test that build, and Brian put it off to the next day | `D0770ET6WBW /262–/267` |
| sheet | F | Rows 1, 25 "ok, chat" are backed: "#1718 already tested", "Looks ok to me", "Boss arena as well" | `D06UPGF5PQV /158, /169, /170` |
| legend, dd_legend | — | see Other contradictions (Docs check) | — |
| rule_card, rule_comment | B | Arthur has no Trello history (B8). ZM ROADMAP actors: Leonard 308 actions, three unnamed members 191; all 12 comments by one unnamed member | trello `/actions` |
| rule_card, rule_comment | S | Trello ids carry their time and base ids match the action date to the second (`68dc07ed…` = 16:40:13Z). Planned: card id → 22:42:24Z vs 22:20:00Z; comment id → 22:51:30Z vs 22:29:06Z | trello `/actions` |
| rule_card | S | ZM ROADMAP holds feature cards in date lists only; a rule card is out of place. Its list would be the SC-13 list | trello `/lists` |
| dd_card, dd_comment | B/S | Same author problem. Ids → 14:48:00Z vs 14:40:00Z and 14:57:12Z vs 14:49:12Z | trello `/actions` |
| invite_v1, invite_v2 | B | Ids (B7) and premise (B3). No base record of any Collect & Win review or go/no-go: 0 hits for "go/no-go" in Calvin's 8,142 threads, 9 hits for "Collect & Win" in all Gmail, all 2024 Domino Delights | gmail full scan |
| invite_v1, invite_v2 | S | Subject format. Every 2024–2025 invitation subject read in Calvin's mailbox (about 30 of 225 hits) ends "(CST) (calvin.price@harmonygames.co)", in his own zone. Planned subjects use "(PDT)" and no mailbox suffix. 10am PDT is 11am CST | gmail `threads/calvin@harmonygames.co_1842050583560498707.json /messages/0/subject` |
| invite_v1, invite_v2 | F | Leonard does send Calvin invitations (23 threads from him since June) | gmail `threads/calvin@harmonygames.co_1841533623069695540.json` |
| event | S | Base keeps one event row per attendee calendar, each with its own `event_id`; the plan has one row for six people | gcal `/events/373, /1368, /4784, /7398` |
| event | F | Start 2025-10-02T17:00Z is after the cut, but the base also holds events on 2025-10-01 (20:30Z, 21:30Z). Nothing in the base sits on Oct 2 or Oct 3, so no clash | gcal full scan: 0 hits for `2025-10-02T`, `2025-10-03T` |
| claim | F | 3.6 min after PR #472 opened (22:36:36Z); no neighbouring message in the chat (last base message 09-25T17:31Z) | `D06UPGF5PQV /176` |
| inline | S | No mirror in #zombie-prs: the #472 thread has three replies (comment, "Review approved", merged) | `C093LEZGF6J /589, /590, /619, /621` |
| inline | S | Arthur approved #470, #471, #472 within 112 s (15:51:06, 15:52:17, 15:52:58) and merged #472 six seconds later. His real inline comments are one line ("Seems important") | github `/reviews/2176, /2179`; `…#390#rc_6` |
| inline | F | Id `#472#rc_1` is free; time equals review `#472#rev_1`; nothing in the PR says the pass tokens were separated | github `/pull_request_comments/655` |
| inline2 | B | Contradicts the walkthrough (B6). Also the PR summary: "Temporarily disables the close button during transitions" | github `/pull_requests/2380`, `/pull_request_comments/658` |
| inline2 | S | No mirror in #zombie-prs; same voice issue | `C093LEZGF6J /622–/626` |
| reopen | F | Thread is Vincent's own, already turned to a shader problem; 67 min after Submission #135 finished. Root `reply_count` 4 and `latest_reply` need updating | `C08R27X0EAH /1091–/1096` |
| else_dm | F | Matches PR #470 bullets 2 and 4, merged by Arthur 15:51:15Z, 34 min earlier. Spanish and register fit | github `/pull_requests/2375`; `D05S1S2H55M /120–/129` |
| filt_dm | F | Main builds with #475 exist before 18:30Z (iOS #1756, Android #2025). Register fits | `C05433XK267 /1115, /1116` |
| filt_dm | S | Row 40 has candidate existing tickets: ZOM-541 "Cards Collect Vfx animation" (cards fly to the inventory) and ZOM-528 "Claimed Cards traveling to inventory section" (SC-15) | linear `/issues/3616`, ZOM-528 |
| mail | S | Robert never mails Calvin in person. All six threads from him since June 2025 are calendar invitations; he reports in Slack | gmail `threads/calvin@harmonygames.co_1842730511532657146.json`; `C08R27X0EAH /923` |
| mail | S | Id time (B7) | — |
| alias_gift, alias_streak | B | Dated 09-29 on tickets that cannot exist before 09-30T16:26:02Z (B1); comments (B9) | linear `/issues/3643` |
| zom573, zom578 | B | Creation dates (B1) | linear `/issues/3643` |
| deck, folder | — | see Other contradictions | — |

## People and roles

| Person | Active late Sep | Planned place | Verdict |
|---|---|---|---|
| Brian Foster | yes, to 09-30T16:50Z | DM with Calvin, Linear tickets | Place fine; hours not (S). He creates ZOM tickets (ZOM-543, 555, 564, 566). He sends no mail in the plan, so SC-6 is not relied on |
| Vincent Parker | yes, to 09-30T17:42Z | #zombie-bugs thread, Linear, Sheets, Docs | Slack and Linear fine (he files most Bug tickets). His lists are Slack canvases (B4). 21:20Z is 00:20 for him, but he posted 21:31–22:04Z on 09-24 |
| Arthur Blake | yes | GitHub inline, Trello | GitHub fine (154 inline comments, 12 on match3d). Trello never (B8) |
| Leonard Hayes | yes | Calendar invitations | Fine; he organises the ZM meetings and runs the Trello board |
| Owen Baker | yes | Spanish DM | Fine |
| Marcus Bennett | yes | DM with Calvin | Fine |
| Robert | yes (Slack 09-28T17:41–17:59Z) | Mail to Calvin | Out of character (S) |
| Calvin Price | yes | DM with Vincent, Drive folder | Fine |
| Julia Lawson | 09-02 note in DM | cited only | Fine, partly (priority only) |

Time zones are from calendars, not Slack (SC-70).

## Dates and chronology

- PR merges: #459 09-24T23:06:25Z; #465 09-25T22:15:51Z; #468 09-29T16:13:50Z; #470 09-30T15:51:15Z; #472 15:53:04Z; #475 16:09:15Z (github `/pull_requests/2362, 2369, 2372, 2375, 2377, 2380`).
- Every "ok" re-test meant as Passed is on a main build after its fix merge, except rows 31 and 33 (B2).
- Rows 1, 5, 25 lean on iOS #1718 (branch, 09-25T16:25:49Z), before #465 merged. The coin fix was changed again after Vincent's ok: CodeRabbit reviewed a new RewardVFXManager commit at 21:43:05Z (github `/reviews/2163`).
- Vincent's reopen reply 21:20:12Z is after Submission #135 (20:13:09Z). Fine.
- Marcus 18:30:12Z is after #475 reached main builds. Fine.
- Owen 16:25:12Z is after the #470 merge. Fine.
- Calvin's claim 09-29T22:40:12Z is after PR #472 opened. Fine.
- Invitation v2 at 17:22Z: Leonard has a meeting at 17:30Z (gcal `/events/7398`); sending just before it is plausible. His other events that hour were not checked.
- Hub 23:10Z follows everything it names. PR #477 (SC-18) opened 22:26:30Z, 44 min before it.
- Slack collisions: only gate_old (see table). I read every base message around each planned Slack time in the four DMs written to and the #zombie-bugs thread; none shares a `ts` with a planned one.

## Builds and PR claims

All in slack `messages/C05433XK267/2025-09.json`, field `attachments/0/fallback`.

| Build | Pointer, ts | Finished (UTC) | Branch | As planned? |
|---|---|---|---|---|
| iOS Internal #1710 | /901, 1758755507.343299 | 09-24 23:11:47 | main (merge #459) | yes |
| Android #1974 | /902, 1758755609.200489 | 09-24 23:13:29 | main | yes |
| iOS Internal #1718 | /926, 1758817549.151639 | 09-25 16:25:49 | Calvin's QueueManager branch | yes |
| iOS Internal #1727 | /959, 1758838873.487119 | 09-25 22:21:13 | main (merge #465) | yes |
| Android #1984 | /960, 1758838918.332289 | 09-25 22:21:58 | main | yes |
| Android Submission #129 | /972, 1758854356.576719 | 09-26 02:39:16 | main | yes |
| Android #2004 | /1048, 1759149639.741779 | 09-29 12:40:39 | Owen's winAndCollect branch, started by Brian | yes |
| Android #2006 | /1053, 1759160363.685759 | 09-29 15:39:23 | main | yes |
| iOS Internal #1745 | /1058, 1759162758.968639 | 09-29 16:19:18 | main (Collect And Win #468) | yes |
| iOS Internal #1746 | /1068, 1759173858.825639 | 09-29 19:24:18 | Calvin's AnimatedIcons branch | yes |
| Android #2010 | /1069, 1759173998.691929 | 09-29 19:26:38 | main, "No Changes" | yes |
| Android #2013 | /1075, 1759188882.419789 | 09-29 23:34:42 | main, "No Changes" | yes |
| iOS Internal #1750 | /1084, 1759197354.452939 | 09-30 01:55:54 | main (merge #469) | yes |
| iOS Internal #1754 | /1107, 1759248081.891639 | 09-30 16:01:21 | main (merge #472) | yes |
| iOS Internal #1757 | /1119, 1759257787.502039 | 09-30 18:43:07 | main | **no, after the sheet (B2)** |
| Android Submission #135 | /1124, 1759263189.219529 | 09-30 20:13:09 | main | yes |

All 16 build names exist; every MAIN_BUILDS / BRANCH_BUILDS ts matches; every branch is as assumed.

PR fit:
- **#465** (body: coin replay after kill; queued tutorials after the first). Rows 1, 5 fit directly. Rows 2, 25 fit the CodeRabbit summary ("stuck or repeated tutorials"). Row 3 (hand pointer) is not named in the PR; only Calvin's chat ties it to the same push (`D06UPGF5PQV /161`). Acceptable, since the Fix column is "what the dev told me".
- **#470** (body lists four bugs). Rows 15, 16 fit bullets 2 and 4. Reviews: CodeRabbit and Owen only, then Arthur APPROVED 15:51:06Z with an empty body.
- **#472** (waits for Collect & Win status; "Reduces unnecessary delays"). Rows 17, 18 fit. Row 12 is not in it. Note the walkthrough does touch `PlaySeasonPassToken` on the no-controller path, so "it is not in here" is slightly stronger than the diff supports (S, wording).
- **#475** (card pack prompt, close flow, last pack reveal). Rows 31, 33 fit. Row 32 is where B6 bites.

## Known-data cards touched

| Card | Near the plan? | Relied on? |
|---|---|---|
| SC-6 | Brian's address is the share target and an attendee | No. He sends no mail |
| SC-13 | Yes. The "Queue Manager" card (`68c453cd0ff184d95550bc58`) sits in list `6851a674975da1fe76e70d93`, named "BETA: Oct 10" in `/lists` and "BETA: Sep 30" in actions | Only if the rule card or a check reads that list name. Keep the rule card out of it |
| SC-14 | Card 58 "Minor Bugs to Fix - Vincent" is in the same list and shows the flag clash (`dueComplete` false, badge true). Card 63 "Queue Manager" is consistent (both true since 09-30T16:40:22Z) | No, but a solver looking for Vincent's list meets card 58 |
| SC-15 | Yes. ZOM-526 "Tokens traveling to live-ops" and ZOM-528 "Claimed Cards traveling to inventory section" are near rows 12 and 40 | **Risk**: row 40 can be filed on ZOM-528, which moves a card ticket |
| SC-16 | ZOM-564 (Brian, tutorial, created on the 24th) is near the scope sentence | No |
| SC-18 | PR #477 is the newest Collect & Win PR | No. Rows 15, 16 use #470 |
| SC-19 | Robert's "latest TestFlight" names no version | No |
| SC-30 | The epic and children repeat the parent/child pattern | No base value used |
| SC-32 | Plan uses "In Validation", which exists (ZOM-548, ZOM-549) and has no completion date | No |
| SC-38 | Season Pass area; ZOM-552 untouched; ZOM-529 unused and absent | No |
| SC-44 | Not touched | No |
| SC-56 | Builds are matched by number and branch, not commit title | No |
| SC-57 | **Yes.** #zm-collect-win holds the records behind B3 and B4 | The plan posts nothing there, but its truth is contradicted from there |
| SC-58, SC-67, SC-68 | Not touched | No |
| SC-70 | Used calendar zones for the hours findings | n/a |

## Other contradictions

- **Reports outside the 40 that fit the scope sentence** (raised since the 24th, by someone other than Vincent or with Brian, about the home screen): "When the page opened, it shows placeholder images at first" and "The reward amounts are jiggling when I open up the event page" (`C3DD99314033 /71, /75`, 09-26, unticked); Brian's "In the main menu, the UI also looks quite short" (`C3DD99314033 /80`, repeated `CF4EDAF93359 /91` on 09-29); Vincent's "the timing is off. Especially in the quest chests" (`CF4EDAF93359 /124`, 09-30T13:29Z, with Calvin mentioned at `/123`). About 20 more Bug Checklist items of 09-29 and 09-30 have empty text in the export, so a solver cannot rule them in or out.
- **Existing tickets near rows**: ZOM-555 "Zombie Lane Reward Animations" (Done 09-30) against rows 22–24; ZOM-556 "When the daily gift is skipped…" (Todo, Calvin) is an open Daily Gift ticket outside the sheet; ZOM-560 (win streak freezer) against row 37; ZOM-540 "Boss Arena Tutorial" against row 25. None is the same report, but "use that ticket then" invites the match.
- **Epic ticket**: ZOM-543 "Queue Manager", In Progress, Brian → Calvin, no parent, no children (linear `/issues/3618`). Fits "right now it is one ticket". Leonard marked its Trello card complete on 09-30.
- **Builds that count for QA**: no base rule found ("branch build", "cut from main": no relevant hit). Visible practice is the opposite of the planned rule: Vincent passes branch builds and the dev merges on his word (`D06UPGF5PQV /126, /144`; `D05S1S2H55M /109, /111`). Not a contradiction, but the planned rule has no echo anywhere.
- **sheet, legend, dd_legend (F/S)**: no base sheet or doc is titled with "QA pass", "pass sheet", "home screen", "queue", "legend" or "How to read" (gsheets and gdocs title scans, complete). Vincent does own Sheets and Docs, including "ZM QA Checklist.docx" (gdrive `f_933e2d4147dc0fecd537aa`, 2025-06-02) and a "Regression Test Plan" sheet exists (gsheets `/sheets_spreadsheets/51`). So the medium is plausible, but "ZM QA Checklist" is one more real Vincent QA list next to the planned sheet (S), and dd_legend's "my regression list" has a real namesake whose owner and content I did not read.
- **deck (S)**: no "ZM weekly" deck exists (gslides title scan, complete, 0 hits). The base series is "Weekly Update <Mon DD>" on a shared drive (gslides `/slides_presentations/0, /25, /105`). Brian appears on decks only as a share target in the rows sampled; whether he owns any deck was not finished.
- **folder (S)**: Calvin's Drive has 10 folders, all created in 2023 (Invoices, Unorganized, BUILDT and its sub-folders), and one item modified in 2025 (gdrive `f_cccfcf7859b52dae552a09`, 2025-02-14). No name in Drive contains "queue". A working folder made on 09-23 is out of habit but contradicts nothing. Id `d_36cdb0374c4aad3b8bf741` is free.
- **Ids**: `f_cb40955893624e1acb8500`, `f_d3a1aa5976285aac98ffda`, `f_c1334d5f2914871accec45`, `f_7f0df2a516452e145d1a0f` are free in Drive; both Trello card ids and both action ids are free; `evt_342a813cb7765d4a6fce8d` is free; ZOM-567…589 are free.

Not checked: Vincent's and Brian's own sheet titles one by one (the scan was too slow to finish), Leonard's full calendar for 09-26 and 09-30, the unreadable canvas items.
