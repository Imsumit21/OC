# Blind fork sweep — injection (Calvin Price, ZM queue manager epic, Oct 1 2025)

Independent solve from `01_Universe_Inject.sql` plus base reads through `hg.py search` only. No design, manifest, solver or truth file was read.

## 1. Summary

- **My five numbers:** Passed **12** · Waiting on QA **6** · Waiting on a fix **21** · Clear areas **1** · On the review list **6** (39 reports: 38 sheet rows + 1 DM report).
- **Forks:** 2 blocking, 7 moderate, 5 wording.
- Both blocking forks move one report between Waiting on QA and Waiting on a fix (6/21 → 5/22); one of them can also drop a report or clear Boss Arena under a third reading.
- Everything else resolved to one answer: every cited build's branch, every PR's merged state, the two "came back" posts, the two tickets under another name, the review card, the invite.

## 2. Row-by-row

Builds (all from #builds C05433XK267 `2025-09.json` result posts): iOS Internal #1713 `/913`, #1727 `/959`, #1745 `/1058`, #1750 `/1084`, #1754 `/1107`, #1757 `/1119` = **main**; Android #1974 `/902`, #1984 `/960`, #2006 `/1053`, #2010 `/1069`, #2013 `/1075` = **main**; Android Submission #129 `/972`, #135 `/1124` (finished 30 Sep 20:13 UTC) = **main**; iOS Internal #1698 `/854`, #1708 `/896`, #1716 `/922`, #1718 `/926` = `…/QueueManager` (feature); #1746 `/1068` = `…/AnimatedIcons` (feature).

PRs (github `data.json`): #465 `/pull_requests/2369` merged 25 Sep 22:15; #472 `/pull_requests/2377` merged 30 Sep 15:53; #473 `/pull_requests/2378` merged 30 Sep 15:41 by its author Oliver; #475 `/pull_requests/2380` merged 30 Sep 16:09.

| # | Area | Status | Ticket | Review list | Deciding records | Competing reading | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Tutorials | Waiting on QA | new sub-issue | no | "ok, chat" → Vincent DM D06UPGF5PQV `/158`–`/169`: build #1718 = feature branch, so no pass under Arthur's doc; #465 merged, body names the queued-tutorial fix | none found | single |
| 2 | Tutorials | Waiting on QA | new sub-issue | no | same chat (`/140`, `/169`), #1718 feature; #465 merged | none | single |
| 3 | Tutorials | Passed | new sub-issue | no | nr iOS #1745 main | none | single |
| 4 | Tutorials | Waiting on a fix | ZOM-567 | no | no PR; Oliver "can't get it on my phone yet" | dropped as "Oliver's tutorial … leave it out" (ZOM-567 is Oliver's tutorial ticket) | MODERATE (M2) |
| 5 | Level-end rewards | Passed | new sub-issue | no | ok iOS #1745 main | none | single |
| 6 | Level-end rewards | Waiting on a fix | ZOM-568 | **yes** | no PR, no re-test | none | single |
| 7 | Level-end rewards | Passed | new sub-issue | no | nr iOS #1745 main | none | single |
| 8 | Level-end rewards | Waiting on a fix | ZOM-569 | **yes** | no PR | none | single |
| 9 | Daily Gift | Waiting on a fix | new sub-issue | no | nr #1745 (29 Sep), then Vincent in #zombie-bugs thread `b156fdcd…` 30 Sep 21:20 on Android Submission #135 (main, newer): "not gone" | stays Passed: "#135" read as older than "#1745", or the post treated as one of Vincent's chats | MODERATE-low (M5) |
| 10 | Daily Gift | Waiting on a fix | ZOM-570 | no | no PR | on review list if Daily Gift is "listed" | MODERATE-low (M3) |
| 11 | Daily Gift | Waiting on a fix | **ZOM-556** (existing, Todo) | no | seeded comment `comment_b3c56083…` on ZOM-556 ("Same thing"); base title "When the daily gift is skipped, it doesn't reset to 0" | none (ZOM-557 is a different quest bug, Done) | single |
| 12 | Season Pass | Waiting on a fix | ZOM-571 | no | #472 merged, but Arthur's inline review `#472#rc_1`: not in this diff | none | single |
| 13 | Season Pass | Waiting on QA | ZOM-572 | no | no PR in sheet; Oliver's comment `#473#c_2` on his own merged #473 | none | single |
| 14 | Season Pass | Waiting on a fix | ZOM-573 | no | Oliver: "on my branch, no PR for it yet" | none | single |
| 15 | Collect & Win | Waiting on a fix | ZOM-574 | **yes** | no PR | none | single |
| 16 | Endless Mode | Waiting on a fix | ZOM-575 | no | no PR | none | single |
| 17 | Collect & Win | Passed | new sub-issue | no | ok iOS #1754 main (has the #472 merge) | none | single |
| 18 | Collect & Win | Waiting on QA | ZOM-576 | **yes** | Fix #472 merged; no re-test; the review disclaims only the icon restart | Waiting on a fix: review says the diff is "only the Collect & Win wait", which reads as row 17's wait fix alone | **BLOCKING (B1)** |
| 19 | Collect & Win | Waiting on a fix | ZOM-577 | **yes** | "fix locally … before I open the PR" | none | single |
| 20 | Win Streak | Waiting on a fix | **ZOM-560** (existing, Todo) | no | seeded comment `comment_9f28b3d8…` on ZOM-560 | none | single |
| 21 | Win Streak | Waiting on a fix | ZOM-578 | no | no PR | none | single |
| 22 | Zombie Lane | Passed | new sub-issue | no | nr Android #2006 main | none (ZOM-555 is a feature ticket, Done) | single |
| 23 | Zombie Lane | Passed | new sub-issue | no | ok Android #2006 main | none | single |
| 24 | Zombie Lane | Passed | new sub-issue | no | ok Android #2010 main | none | single |
| 25 | Boss Arena | Waiting on QA | new sub-issue | no | "ok, chat" → `/150`, `/164`, `/170`: build #1718 feature; Fix #465 merged, no review denies it | Waiting on a fix (the PR itself has no boss-arena fix; base DMs put that fix on Oliver's other branch), or left out as Oliver's tutorial work | **BLOCKING (B2)** |
| 26 | Boss Arena | Passed | new sub-issue | no | nr Android #2006 main | none | single |
| 27 | Boss Arena | Passed | new sub-issue | no | nr iOS #1745 main | none | single |
| 28 | Endless Mode | Waiting on a fix | ZOM-579 | no | no PR | none | single |
| 29 | Endless Mode | Waiting on a fix | new sub-issue | no | ok iOS #1750 (30 Sep 01:55), then `eca2df16…` in C0880U9751A 30 Sep 21:44 on Android Submission #135: played again every time | stays Passed if #135 is not seen as newer | MODERATE-low (M5) |
| 30 | Endless Mode | Waiting on a fix | ZOM-580 | no | no PR | none | single |
| 31 | Card packs | Passed | new sub-issue | no | ok iOS #1757 main | none | single |
| 32 | Card packs | Waiting on a fix | ZOM-581 | no | #475 merged, but Arthur's inline review `#475#rc_1`: pack sound stop not in here | none | single |
| 33 | Card packs | Passed | new sub-issue | no | ok iOS #1757 main | none | single |
| 34 | Card packs | Waiting on a fix | ZOM-582 | no | no PR | none | single |
| 35 | Tutorials | Passed | new sub-issue | no | nr iOS #1745 main | none | single |
| 36 | Level-end rewards | Waiting on a fix | ZOM-583 | **yes** | no PR | none | single |
| 37 | Win Streak | Waiting on a fix | ZOM-584 | no | no PR | none | single |
| 38 | Season Pass | Waiting on QA | new sub-issue | no | no PR in sheet; Oliver's `#473#c_2`: "the bar filling before the tokens land" | existing ticket ZOM-526 "Tokens traveling to live-ops" as "another name" | MODERATE-low (M4) |
| 39 | Season Pass | Waiting on a fix | new sub-issue | no | Marcus DM D05U73FNDDL `806f4a67…` + `bb5dd875…`, 30 Sep 17:10, "today's main build", "3 levels in a row" | same report as row 12 (pass icon animation), so not counted | MODERATE (M1) |

No other in-scope DM report exists in the base: every September DM file in which Calvin posts was read from 26 Sep on (D0770ET6WBW, D06UPGF5PQV, D05U73FNDDL, D05S1S2H55M, D051LNQSFGQ, D07GJJBK789, D07GCPNJPSA, and four with no messages after the 25th).

## 3. Areas

| Area | Rows | Status | Open reports | Child state |
|---|---|---|---|---|
| Tutorials | 1, 2, 3, 4, 35 | Open | 3 | Todo |
| Level-end rewards | 5, 6, 7, 8, 36 | Open | 3 | Todo |
| Daily Gift | 9, 10, 11 | Open | 3 | Todo |
| Season Pass | 12, 13, 14, 38, 39 | Open | 5 | Todo |
| Collect & Win | 15, 17, 18, 19 | Open | 3 | Todo |
| Win Streak | 20, 21, 37 | Open | 3 | Todo |
| Zombie Lane | 22, 23, 24 | **Clear** | 0 | Done |
| Boss Arena | 25, 26, 27 | Open | 1 | Todo |
| Endless Mode | 16, 28, 29, 30 | Open | 4 | Todo |
| Card packs | 31, 32, 33, 34 | Open | 2 | Todo |

- **Review list (6):** rows 6, 8, 36 (Level-end rewards) and 15, 18, 19 (Collect & Win), from the current description of Trello card `68daad83bacf52c6ea7e1593`.
- **State changes on existing tickets:** ZOM-571 In Validation → Todo; ZOM-581 In Validation → Todo; ZOM-572 Todo → In Validation. ZOM-576 stays In Validation. The other 16 (ZOM-556, 560, 567–570, 573–575, 577–580, 582–584) stay Todo.
- **New sub-issues (19):** Done for rows 3, 5, 7, 17, 22, 23, 24, 26, 27, 31, 33, 35; In Validation for 1, 2, 25, 38; Todo for 9, 29, 39.
- **Share list:** brian.foster, arthur.blake, julia.lawson, leonard.hayes, vincent.parker (gcal `evt_342a813cb7765d4a6fce8d` attendees minus Calvin, who owns the sheet).

## 4. Forks and fixes

### Blocking

**B1 — Row 18 / ZOM-576: does the #472 review exclude it?**
- Reading A (mine): Waiting on QA. The review names only the season pass icon restart as missing.
- Reading B: Waiting on a fix. `#472#rc_1` says "It isn't in this diff, only the Collect & Win wait." Row 17 is the wait report ("Reward animation waits too long…"); row 18 is a panel opening over the rewards. Brian's rule is "if the review on it says a fix is not in there, it is not", and "only the … wait" says the diff holds one thing.
- Changes: Waiting on QA 6 → 5, Waiting on a fix 21 → 22, ZOM-576 stays In Validation vs goes to Todo.
- Smallest fix: reword the sentence in all three copies (github `#472#rc_1`, Slack bot reply `061aadc8ec53d1d38f70a4a8268f35c2`, gmail message `…pull/472/review/3285698310@github.com`) to: "Flow sheet has the season pass icon restart against this PR. That one isn't in this diff, the two Collect & Win ones are. Needs its own PR."

**B2 — Row 25 (Boss arena tutorial plays again): is the fix merged, and is it in scope?**
- Reading A (mine): Waiting on QA. Sheet Fix = #465, #465 is merged, no review says the fix is missing; the chat "ok" was on feature build #1718.
- Reading B: Waiting on a fix. Brian says "check the PR itself". #465's body lists only the coin-replay fix and the queued-tutorials fix. In base DMs the replay fix is Oliver's `OneTimeTutorial` on another branch, "not yet I'll push today" (D07GCPNJPSA `/392`–`/402`), and Calvin himself says "I think it may got fixed as well, not sure" (D06UPGF5PQV `/152`, `/155`, `/164`). No merged PR is shown for Oliver's branch.
- Reading C: left out. "Oliver's tutorial skip work is his own thing, leave it out" can be applied to this row, since the base ties it to Oliver's tutorial branch. Boss Arena would then be Clear (clear areas 2, total 38).
- Changes: Waiting on QA 6 → 5 with Waiting on a fix 22 (B), or Waiting on QA 5 and clear areas 2 (C).
- I rate this blocking, though less clear-cut than B1: reading A follows the rule's letter, B follows "check the PR itself".
- Smallest fix: in `comment_faaa7924…` replace "so check the PR itself, and if the review on it says a fix is not in there, it is not" with "so check that the PR is merged; the fix counts as in it unless a review on that PR says it is not". Also anchor the exclusion (see M2).

### Moderate

**M1 — Marcus's DM vs row 12.** "pass icon glow stays on after i claimed everything" (D05U73FNDDL) and row 12 "Season pass icon animation restarts every time a panel closes" are both pass-icon animation state. "If it is already a row, don't count it twice" could merge them: total 38, Waiting on a fix 20, Season Pass open 4. Fix: make the symptom unmistakably different, for example "the red dot on the pass button stays after i claimed everything".

**M2 — The two "leave it out" sentences exclude nothing in scope.** Their grounding is before the 26th or outside DMs: the input blocker in Brian's DM of 25 Sep (D0770ET6WBW `/256`), Oliver's skip-tutorial in #zombie-bugs 26 Sep (C08R27X0EAH `/1057`, `/1079`–`/1081`). With nothing to exclude, a solver may apply "Oliver's tutorial …" to row 4 (ZOM-567, a tutorial ticket assigned to Oliver) or to row 25. Fix: "The skip-tutorial exception Vincent raised with Oliver in #zombie-bugs is not a flow report, leave it out", or delete both sentences.

**M3 — "an area Leonard's review card lists".** The card text also names Daily Gift ("Daily Gift moves to next week"). A literal reader gets 9 on the review list (adds rows 9, 10, 11). Fix: keep the description as "Walk through what is still not passed in: Collect & Win, Level-end rewards." and move the Daily Gift sentence to the calendar update note, or write "this week's areas on Leonard's card".

**M4 — Row 38 ticket.** Vincent's DM `cfee08a8…` says "I opened tickets for the open ones", yet row 38 is open with no ticket. That pushes a search for "another name", and base ZOM-526 "Tokens traveling to live-ops" (In Progress, mentions season passes) is the nearest hit. Fix: "I opened tickets for the open ones, except the pass bar one".

**M5 — "newer build" for rows 9 and 29.** Android Submission #135 against iOS Internal #1745 / #1750 is only newer by #builds timestamps; by number it looks older. Row 9's "back" also comes from Vincent in a channel thread, next to "don't add things from his chats". I hold Waiting on a fix as the only fair answer; the note could say "a build made later" to remove doubt.

**M6 — Share list.** The gmail invite's To header has four people plus Calvin; Leonard appears only as organizer in the body and in gcal attendees. A solver can land on 4 or 5 recipients. Five is right; adding "Leonard included" to Brian's DM would close it.

**M7 — Vincent's ticket comments contradict his sheet.** On ZOM-576 (17:39) and ZOM-571 (17:07) he says he is waiting for a main build with #472, but iOS #1754 (main, with the #472 merge, 16:01) existed and he re-tested row 17 on it. No status changes, but it invites doubt about row 17's pass. Fix for ZOM-576: "I was told #472 has this. Not re-tested yet, I need a fresh account for the first unlock."

### Wording

- **W1** Arthur's DM to Calvin at 26 Sep 00:56 UTC (D051LNQSFGQ `/52`, "the code looks like it plays both at the same time") falls on the 26th in UTC. It is a code remark, not a bug seen in a build, so not a report.
- **W2** Brian's seeded DM of 29 Sep 11:20 speaks of "the flow review on Friday" five hours before the card (16:02) and invite (16:05) were created.
- **W3** Several rows are "Found on" builds from 24–25 Sep and the "ok, chat" is from 25 Sep, before the sheet's creation and "started his pass on the 26th".
- **W4** The sheet writes "iOS Internal #n" / "Android #n" without the job prefix; only the Match 3D jobs carry those numbers in September, but DD jobs reuse #129–#135 in other months.
- **W5** Oliver's "the bar filling before the tokens land" does not say which bar; the PR being the season-pass one settles it for row 38.

## 5. What I could not check

- DM channels where Calvin never posted in September cannot be told apart from other people's DMs through the helper (no membership data read). A base DM to Calvin in such a channel would be missed.
- Slack canvases (Vincent's Bug Checklist, the Collect & Win canvas) were not read; the note says to leave them.
- "Somebody says later it is back" was swept in C08R27X0EAH, C0880U9751A, C09ATAJ220H from 26 Sep plus keyword searches across all September Slack files, not by reading every channel in full.
- Attachments, videos and images in the cited threads.
- SQL integrity (ids, foreign keys, parent folders) was not reviewed; this sweep covers answers only.
- Nothing under `Working_Files/` or `Evals/` data was read; I read the search-many usage lines of `Evals/SEARCH.md` once for the helper's request format.
