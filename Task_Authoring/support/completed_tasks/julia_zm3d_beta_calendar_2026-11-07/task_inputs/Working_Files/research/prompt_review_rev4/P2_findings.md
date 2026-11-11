# Deep Recheck: Pass P2 (Services, data and access)

Task date: Oct 1, 2025 (synth-cut). Clock: 2025-10-01 00:00 PT (07:00 UTC). Persona: Julia Lawson (julia.lawson@harmonygames.co, Slack EMPLOYEE_0005).

**What I checked:** 43 sentences. That is the 6 prompt sentences, the 11 sentences in Frederick's two injected DMs (6 + 5) and the 26 sentences of the injected brief. I also checked the 3 text boxes in the injected UA-plan deck. On the SQL side I checked all 106 statements in 01_Universe_Inject.sql: 75 inserted rows and 31 UPDATEs. Each one was compared with the base record it sits on or refers to, and with the other injected records.

## Findings

DR1 | P2 | common_errors §3 Hidden record and §6.8, Eval 1 §3.2 (State / Lifecycle, Temporal, Cross-service Referential) | Brief (incorporated by the prompt sentence "his working rules for building it are in the brief he shared with me"): "For each beat, what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not what already shipped, not analytics, not polish nobody flagged." | See the evidence below | Cross-Service Coherence | FAIL. Score 2. This is a State / Lifecycle inconsistency, so it cannot take the low-impact NON-FAIL.

- **Injected side** (01_Universe_Inject.sql lines 186-187):
  - `cmt_zom565_1` by usr_c77c50cc15c5342d (marcus.bennett), 2025-09-29T16:05:00Z: "The endless start screen vfx is in (commit f7e971b0). Claim button glow and the new bar are both live now, can close."
  - `UPDATE linear.linear_issues SET state_id = 'Done', completed_at = '2025-09-29T17:10:00Z'` on ZOM-565.
- **Base ticket** (linear/data.json /issues/3642, ZOM-565, created 2025-09-25T13:46:04Z, assignee calvin.price): the description says "I've let everthing on my branch Marcus/EndlessMode_Vfx because right now this its how it looks: the glow behind its on all and the bar its the old bar, not mine… mine it's in there but not active." So the ticket was written 21 minutes *after* the cited commit, and it says the new bar is still inactive and Calvin still has to wire it.
- **Base commits:**
  - github/data.json /commits/10852: f7e971b02d24206455637099b571115e35a0dab1, 2025-09-25T13:25:12Z, "Endless Mode start screen VFX" (marcus). This is the commit the injected comment cites, and it predates the ticket.
  - /commits/4253: 607ccb7f…, 2025-09-26T14:55:17Z, "Endless mode bar, and new bar that its customabile in unity". The new-bar work came after f7e971b0, so f7e971b0 cannot be what made "the new bar" live.
  - No match3d PR opened or merged between Sep 29 15:56Z and 17:10Z carries this work. The only PR opened in that window is #469 "Unity 6000.2.6f1 + top part tex resoultion decrease" (/pull_requests/2373, created 16:42, merged Sep 30 01:50).
- **Base DMs** (slack/messages/D05U73FNDDL/2025-09.json, Marcus ↔ Calvin):
  - Sep 26: `089cef19…` (Calvin) "no I haven't started yet on that" and `86573e8d…` "you can make the modify and will implement it later".
  - Sep 29 14:34:06Z: `15730d83…` (Marcus) "ok so i pushed a modifications on the prefab on my branch, Marcus/EndlessMode_Vfx".
  - 14:34:25Z: `105e75c9…` (Marcus) "<ZOM-565 link> <---- i wrote a comment on the linear task".
  - 15:53:47Z: `38aad037…` (Calvin) "Should I make another branch for those changes? and merge it".
  - 15:55:29Z: `669b4e26…` (Marcus) "u can get it in another branch do ya stuff and then Push it to main".

**Inconsistency:**
1. At 15:55 the work was still on Marcus's branch, and Calvin had not yet branched or merged it. Ten minutes later the injected comment says it is "live now", and an hour later the ticket is Done. Its own description and the commit chronology contradict that.
2. Marcus says he had already commented on ZOM-565 at 14:34. The only ZOM-565 comment in the universe is the injected one at 16:05, and it has different content. That is a time slip on a record the answer relies on.

**Effect on the answer:** this changes the Endless row's "Still to do (owner)" value. ZOM-565 is player-facing art that its owner flagged, so under the brief it is a still-to-do (owner Calvin Price) unless it shipped. The injected Done/"live now" removes it.

The DM is not visible to Julia, but that does not clear the defect, for two reasons:
- The conflict between the ticket description and the injected comment, and the commit dates, sit in Linear and GitHub. Both are unscoped and readable by the persona.
- Coherence fails on the presence of an inconsistency.

**Fix:**
- *Option A:* drop both ZOM-565 statements (`cmt_zom565_1` and its Done UPDATE), so ZOM-565 stays Todo. Then carry "Endless start-screen bar and claim-glow integration, owner Calvin Price" into the Endless still-to-do expectations.
- *Option B:* keep a Done state only if the SQL also adds the integrating work dated after 2025-09-29T15:55:29Z: a Calvin commit or PR on match3d main, with the closing comment citing that record instead of f7e971b0. Also place a Marcus comment about the prefab changes at or before 2025-09-29T14:34:25Z, to match his DM.

DR2 | P2 | Eval 1 §3.2 (State / Lifecycle risk; Other Universe Inconsistency) | Brief: "For the quest rollover, the daily gift (the Login Calendar row on the push sheet) and Plague Race put down whether the beat is in and whether its push is ready, not its window dates." and "what still has to land before it runs … and who owns it" | See the evidence below | Cross-Service Coherence | Minor (NON-FAIL 3 on its own). If the main session reads a comment on a completed card as a lifecycle conflict, it is fail-level.

- **Injected side** (01_Universe_Inject.sql lines 255-260): trello_actions `68dac8204f1e9a3b7c2d5e61`, commentCard, 2025-09-29T17:55:44Z, by d1cd0fef645a6c978ae1f068 (Brian Foster): "Putting the new quest set in with the Mon Oct 13 rollover." It is posted on card `6851a724601a61857a1b202f`, and the same SQL sets that card's badges.comments to 2 and dateLastActivity to 2025-09-29.
- **Base card** (trello/data.json /cards/702, "[Feature] Quests and Milestones and Achievements - [PERSON_NAME_0022]", list "Jun 30th"): `"dueComplete": true` and `badges.dueComplete: true`. It was marked complete by action /actions/4880 (`6862c1c22b05395fb3e4c93c`, 2025-06-30T16:56:34Z, `"dateCompleted": "2025-06-30T16:56:34.857Z"`).
- **Base pattern:** 45 Trello cards carry a dateCompleted, and there are 0 commentCard actions after completion on any of them. The injected comment is the only post-completion activity in the universe. It plans new work on a card that says it is complete.

**Fix:** put Brian's Oct 13 quest-set note on an open record (an open quests ticket in Linear, or a Slack message in a channel Julia is in), or reopen the card in the same SQL. Keep the Mon Oct 13 date unchanged.

## Advisories (not scored; for the main session to compare with the OEs and rubric)

- **A1 (Data exists / Feasibility).** Frederick's DM asks "if anything is held and until when". The only beat the records hold is the weekly leaderboard / leagues:
  - ZOM-429 (Douglas, Sep 23): "they land in the new week fine, so not blocking".
  - Superseded by Vincent's injected #zombie-match3d message `fa3eee2c…` (Sep 30 20:50Z): "it still does not start a new week. I killed the app and reopened it twice".

  No record dates the end of that hold. I checked ZOM-429 relations and due dates, Linear issues with due dates from Oct 1 (none), Sep 2025 leaderboard PRs and commits (only #471's toggle UI) and Slack after Sep 22. "Hold until" can only be answered open-ended. That is fine only if no OE or rubric row expects a date.
- **A2 (Data exists).** The injected Pushes tab header asks for "Send (UTC)" on every row, and Frederick says "local notifications included". The PNs Beta rows for lives recharged, 1-day lapsed, 7-day lapsed and FTUE are trigger-based ("When lives are recharged", "Has not played in 24 hours" and so on). No record gives them a UTC instant, so expectations must accept a trigger in place of an instant.
- **A3 (possible reading).** Douglas's base DM D079SNE2TL4 `b650559b…` (Sep 30 18:16Z) says: "Ok, I updated the prod environment with the latest teams/social changes". This comes after Arthur's injected #470 review comment (Sep 30 16:04Z): "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release". I read Douglas's message as the ZOM-563 teams/social fix, not the C&W release. Base D05SG9H1CFM `ab057310…`/`b32738f4…` (Sep 26: "Ese merge con main significa que debo deployar a prod?" / "Igual no va para release ahora") supports C&W not being on prod. So the Oct 8 GCal release stands. I am not scoring it. If a grader read the 18:16 update as the release, the C&W first window would move.

## Topic lines

- **Cross-Service Coherence:** DR1 (fail-level) and DR2 (minor).
- **Feasibility: no finding.** Every write has a cataloged path:
  - gsheets_values_update / values_append / batch_update on the owned sheet f_e4a17c90b3d25f6a8c1d73.
  - linear_create_comment on ZOM-78 and on the held beat's ticket ZOM-429.
  - slack_send_message with thread_ts in D05SD5QLG94.
  - gmail_reply_to_message on Julia's copy of Brian's Sep 26 mail, which the brief's "Config locks" rule implies.

  There is no open instruction over more than 15 disagreeing items. A1 and A2 are advisories only.
- **Persona access: no finding.** Every record the answer needs is reachable by Julia:
  - **Slack:** D05SD5QLG94 and D05GU6L0XFH (both list EMPLOYEE_0005), #zombie-art C08R8CHB0QL and #zombie-match3d C0880U9751A (both list EMPLOYEE_0005; Robert and Vincent are members of the channels they post in).
  - **Gmail:** both Brian mails are in Julia's mailbox. Mailboxes are complete for From, To and Cc (Brian SENT, Julia INBOX, Frederick INBOX).
  - **GCal:** event `evt_5c1e83a7d94b02f6c8e31a` is on julia.lawson's calendar.
  - **Drive:** the brief and the deck are shared to Julia as reader. The calendar sheet is owned by Julia, inside "ZM Live Ops", whose parent d_8140f09bf9f1b94cb8ee2d is Julia's root. The Push Notifications Zombie Match sheet f_a325dd4af80afc5994d5dc lists julia.lawson in shared_with_emails.
  - **Unscoped services:** Linear, GitHub, Trello and Confluence.
  - **Hidden record: none.** The only persona-hidden record I used (D05U73FNDDL) is DR1's contradicting evidence, not a needed fact.
- **Data exists: no finding.** Every fact the answer needs is on a record:
  - **Windows:**
    - CDK (match3d-backend/zombies-game-cdk/lib/zombies-game-cdk-stack.ts): LEAGUES "0 0 * * 1", PLAGUE_RACE "0 0 * * *", ENDLESS daily "0 0 * * *" and weekly "0 0 * * 1", WIN_AND_COLLECT "0 0 * * 1,2" / "3,4" / "5,6,0", SEASON_PASS "0 0 1 * *".
    - These match Confluence page_liveops_calendar and the brief.
  - **Release instant:** GCal 2025-10-08 15:00Z, "18:00-19:00 Istanbul time".
  - **Season lock:** "locked 24h before each season opens" (page_season_pass_spec), against Brian's "Fri Oct 31, 10:00 Istanbul time" (07:00Z).
  - **Push rows:** PNs Beta tab rows 2-15. The four excluded rows exist exactly once each: Hourly Coins row 3, Nathan's Treasure Hunt row 9, Streak Fever row 11, Axe Arena row 12. The Login Calendar row is row 13. Both the "Status" (Ready/Not Ready) and "Status (NA, WIP, LIVE)" columns are present. "PN BETA Translated" holds the Domino copy.
  - **Owners:** Douglas (release), Claire (vial sprites, #468), Marcus (C&W icon, ZOM-465), Oliver (premium strip, #473), Brian (Nov config mail; quest set), Douglas (ZOM-429).
  - **Product:** "Owner: Robert (Product)" (page_season_pass_spec).
  - **Change-request rule:** no Aug–Sep CHANGES_REQUESTED review exists. The only recent ones are match3d#303 (July) and match3d-backend#4 (June), so the rule never fires.
- **Tool use and cross-service: no finding.** Each service changes a graded fact:
  - **Slack:** asks, row exclusions, leagues hold, Halloween pulled.
  - **Docs:** the rules.
  - **Sheets:** push rows.
  - **Linear:** owners, still-to-dos, note targets.
  - **GitHub:** C&W DEV-only status, vial sprites, Oliver, CDK windows.
  - **GCal:** release instant, which sets the C&W first window at Fri Oct 10 00:00Z.
  - **Gmail:** Oct 31 07:00Z misses the Oct 31 00:00Z lock.
  - **Confluence:** the 24h lock.
  - **Trello:** the Oct 13 quest set.

  The prompt names no tool.
- **Derived columns: N/A.** No Snowflake table is read. The Confluence values used (24h lock, Endless resets, C&W windows) agree with each other and with the CDK stack.
- **Date-slip severity:** the only slip is the 14:34Z "i wrote a comment" against the 16:05Z comment, folded into DR1. It is fail-level there because it changes the Endless still-to-do set. Every other date checks: weekdays for Oct 6/12/13/19/20/26/27, Oct 29/31, Nov 1/2, Oct 8 and Sep 22/26 are correct. All injected timestamps are before the 2025-10-01 07:00Z clock, and every ts matches its created_at.

## Checked and consistent

- **Slack threads:**
  - Frederick's DM pair: parent reply_count 1, latest_reply equals the reply's ts.
  - Robert's Sep 18 reply in the thread under Martin's Sep 17 "Halloween theme" post (9025d428…, base reply_count 0 → 1). Robert's Sep 30 22:10Z retraction in D05GU6L0XFH, with no later contrary message.
  - The four #zombie-prs bot mirrors. Each thread's base count plus 1 matches the SQL (16→17, 41→42, 2→3, 7→8). latest_reply is correct, and #468 keeps base 1759162433.383449. "Comment … by <commenter>" follows the base convention.
- **GitHub:**
  - #468 review at 15:36Z, before its 16:13Z merge.
  - Post-merge activity on #470, #471 and #473 matches the rare base pattern (4/2206 reviews, 11/643 PR comments and 5/1207 review comments come after merge).
  - Timeline "reviewed" events with an empty actor and null created_at match the base. Commit ids equal the PR head shas.
  - updated_at bumps are correct.
  - Samuel's "iOS 50 and Android 135" matches #builds C05433XK267 on Sep 30. Android #135's change list includes "Fixing UI Elements on Daily Gift [Samuel Turner]".
- **Linear:**
  - All comment authors resolve to real users (usr_Robert is a base id).
  - The ZOM-521 untick of items 4 and 6 matches the In Progress children ZOM-526 and ZOM-528, which repairs SC-15. Children 523, 524, 525 and 527 are Done.
  - ZOM-566 started 17:20Z, after it was created at 16:26Z.
  - ZOM-344, ZOM-471 and ZOM-542 Done, with no contrary later record found.
  - ZOM-465: the "C&W came in after my note" ordering matches PR #468 (opened Sep 26 20:16Z, after the 18:10Z note). The icon PRs #454, #456 and #458 cover no C&W icon.
  - The ZOM-429 → Vincent retest is an intended dated supersession.
- **Drive and Docs:**
  - The brief's style_runs offsets match its heading positions exactly.
  - Extension-named Google files (.docx/.xlsx) and null web_view_link follow the base pattern.
- **Gmail:** the Sep 26 mail is a separate thread ("…: new date"), as expected for a correction without In-Reply-To.
- **Deck:**
  - The four week ranges are correct.
  - Slide 2 "scaled up week by week if the cohorts hold" and slide 3 "hold the spend there until the pivot call" can be reconciled: the pivot call is undated, and Leonard set "by mid oct" in D04UP2L3E3S. No calendar value depends on them.
- **Known base issues touched, no effect:**
  - SC-6: brian.foster@ is used correctly for HG Brian.
  - SC-15: repaired consistently.
  - SC-38: ZOM-552 is analytics, which the brief excludes.
  - SC-22 (time_in_status on ZOM-429/ZOM-78) and SC-62 (reward-import cadence) are not read.

## Platform defects

- PLATFORM:FD-2880: the match3d main head 0ff577550e44578ebe472a5b4a64a05275968b7f is not in `commits`, so whether f7e971b0 reached main cannot be traced. DR1 does not rest on reachability. It rests on the ticket text, the commit dates and the DMs.
