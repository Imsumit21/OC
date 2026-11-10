# Deep Recheck P2: Services, data and access (blind)

Task: Julia Lawson, Product Manager. ZM3D beta live-ops and push calendar. Clock 2025-10-01 00:00 PT (07:00 UTC). Synth-cut universe.
Scope: Cross-Service Coherence, Feasibility, Persona access, Data exists, Tool use and cross-service. This includes hidden records, derived columns and date-slip severity.

## What I checked

- **Prompt:** all 6 sentences.
- **Frederick's DM** (parent `bca784379e7dbca9e64e79a64dfefbba` and reply `890dc27f56e8501bd7590ffdfc231057`, both in `D05SD5QLG94`): all 11 sentences.
- **The brief** (`f_7c3e91a4d2b85f60e1a9c4`): all 26 sentences plus the title and byline.
- **The UA plan** (`f_2b9d4e7a1c63f08d5e7b21`): 5 sentences and 4 week lines.
- **Other injected text:**
  - Robert's two messages
  - Vincent's retest
  - Brian's two emails
  - the GCal description
  - Arthur's three GitHub notes
  - all 24 Linear comments
  - the Trello comment
- **Injected records:** all 96 SQL statements, read but never executed. That is 70 inserted rows and 26 UPDATEs of base rows: 20 `linear_issues`, 4 `slack_messages`, 1 `github_pull_requests` and 1 `trello_cards`.
  - The SQL parses cleanly: quotes balance and every apostrophe inside a string is doubled.
  - No injected ID collides with base data. I checked Slack ids and ts, Gmail thread and Message-ID, GCal event_id and ical_uid, Drive, Docs, Sheets and Slides ids, the Trello action id, and the GitHub rc, rev, ev and c sequence numbers.

## Findings

**No finding is fail-level.** All four are advisory only. None changes a value, set, order, recipient or destination the answer is graded on.

**DR1 · P2 · Cross-Service Coherence, Other Universe Inconsistency (a mailbox lacks derived mail) · Advisory only**
- **Quote:** brief, "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC".
- **Injected side:** `gcal.gcal_events` rows `evt_9a4c2e7f1b3d58e06c7a2f`, `evt_5c1e83a7d94b02f6c8e31a`, `evt_a72f4d9e0c1b58d3e6f40b` and `evt_1d6b9a03e5c27f84b0d92c`.
  - Event "ZM3D backend release - live-ops server windows", organizer `douglas@harmonygames.co`, created `2025-09-24T16:05:37Z`.
  - Attendees: frederick.stone, julia.lawson, owen.baker.
  - No mail in any of those three mailboxes has a subject containing "Invitation" for this event.
- **Base side:** attendee mailboxes normally get invitation mail.
  - Of the attendee events created Aug–Sep 2025, an "Invitation…/Updated invitation…" mail exists for 16 of 22 in Frederick's mailbox, 4 of 4 in Owen's and 3 of 6 in Julia's.
  - Example: `frederick.stone@harmonygames.co` mail dated "Mon, 29 Sep 2025 21:53:33 +0000", subject "Invitation: Leonard Hayes and PERSON_0787_NAME @ Tue Sep 30, 2025 10:30am - 11am (PDT)".
- **Impact:** none on the answer. The event itself is on Julia's calendar copy and readable, and the release instant comes from `start_ts`.
- **Fix (optional):** add invitation mails for the event to the three attendee mailboxes, or leave as is.

**DR2 · P2 · Cross-Service Coherence, Cross-service Referential (informal references that resolve to no record) · Advisory only**
- **Quote:** brief, "A committed date that misses the lock moves earlier and its owner is told in a reply on the mail where they committed to it."
- **Injected side:**
  - Brian's mail `brian.foster@harmonygames.co/<CAPT--p4sBC8XnaA7qBDMtZkWqJPiXP0MT3deOQGPusOZhHF+vo@mail.gmail.com>` and its Julia and Frederick copies say: "Nothing else changes from the September handoff."
  - Also informal: `harmonygames-Games/match3d#468#rc_38`, "Claire has those on her list", and `cmt_zom565_1`, "the P1/P2 endless polish from the list Brian gave me".
- **Base side:**
  - No September Season Pass config-handoff mail exists in Brian's (297 threads), Julia's (253) or Frederick's mailbox. A subject scan for season pass, handoff or config finds only Linear notifications and promotional mail.
  - No Linear or Slack record holds Claire's vial-model list. A search for vial, bottle or potion in ZOM/ART issues since Aug 15 finds only ZOM-531.
- **Impact:** none. The answer needs Brian's Oct 31 commitment, which is on the Sep 26 mail, and Claire named as owner, which `rc_38` states directly.
- **Fix (optional):** drop "from the September handoff", or add that mail.

**DR3 · P2 · Data exists (a breakdown with no dated field) · Advisory only**
- **Quote:** Frederick's DM, "if anything is held and until when". The injected sheet `f_e4a17c90b3d25f6a8c1d73`, tab Calendar, has the header "Hold until (UTC)".
- **Records:** the only beat the rules hold is the weekly leaderboard.
  - `b5f2955c2e154efc6835946ecfe1758e` in `#zombie-match3d` (`C0880U9751A`), 2025-09-30 20:50Z: "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice…"
  - Its ticket, ZOM-429, is in state Backlog with `due_date` null and no fix scheduled. No ZOM ticket or match3d PR since 2025-09-01 is a leaderboard fix.
  - The Oct 8 release event covers only "The server windows that are still on the DEV stack".
- **Impact:** no record gives an end date. A correct answer can only give an open-ended hold, until Douglas ships and verifies a fix.
- **Fix:** none needed in the data. Rubric and Oracle Events must not require a hold-until date.

**DR4 · P2 · Persona access / hidden records (owner-flagged polish only in records Julia cannot open) · Advisory only**
- **Quote:** brief, "Still to do… what still has to land before it runs for bought users (prod deploy, config, player-facing art an owner has flagged) and who owns it. Not … polish nobody flagged."
- **Record 1:** Brian → Marcus DM `D076V3NB6P7`, 2025-09-30 16:33Z, EMPLOYEE_0026: "After the boss arena and endless mode, Could you polish the bottle vfx for Collect&amp;win?"
  - Members: EMPLOYEE_0002, EMPLOYEE_0026, PERSON_6089, U05UDKGFX0B, U076SL1V4BV. Julia (EMPLOYEE_0005) is not one.
- **Record 2:** Bug Checklist canvas `CF4EDAF93359`, 2025-09-30 13:29Z, EMPLOYEE_0012: "the timing is off. Especially in the quest chests. It should be opened first, then the reward should be visible."
  - Members: Oliver, Vincent, Robert, Arthur, Brian, PERSON_6089. Julia is not one.
- **Related injected record:** the SQL closes ZOM-344 (`state_id='Done'`, `completed_at='2025-09-16T16:20:28Z'`) with the comment "Quest box open and close animation … reads well on the quest screen. Art side is signed off on my end."
  - The base Sep 30 note is about chest-open and reward timing on the code side.
  - Because Marcus limits his sign-off to "Art side", this is not a lifecycle contradiction.
- **Impact:** both items are VFX or animation polish. The brief says VFX gaps do not hold a beat. They are hidden from the persona, so they cannot be required ground truth (`acl.md`).
- **Fix:** none needed in the data. Rubric and Oracle Events must not require bottle VFX or quest-chest timing as a still-to-do.

## Topic lines

- **Cross-Service Coherence:** no fail-level or low-impact finding. Advisories are DR1 and DR2.
- **Feasibility:** no finding. Every explicit ask can be done with a catalog tool as Julia:
  - `gsheets_values_update` or `gsheets_values_append` on her own sheet `f_e4a17c90b3d25f6a8c1d73`
  - `linear_create_comment` on ZOM-429 (assignee Douglas)
  - `linear_update_issue` (`links`) or a comment on ZOM-78
  - `slack_send_message` to `D05SD5QLG94`, where Julia is a member
  - `gmail_reply_to_message` on Julia's copy of Brian's Sep 26 mail (`julia.lawson@harmonygames.co/<CAPT--p4a5fY9wd6vr+8JtjFXfffkxQOCEUYsuqSPy9HbQJu3Fs@mail.gmail.com>`)
  - The open set ("Every beat players can see"; "PNs Beta tab as it stands") is bounded: 10 push rows after the 4 named exclusions and about 8 beats, under the 15-item scope limit.
- **Persona access:** no finding. Advisory DR4 concerns non-required items. Every required read is visible to Julia:
  - DM `D05SD5QLG94` (members include EMPLOYEE_0005 and EMPLOYEE_0008)
  - `#zombie-art` `C08R8CHB0QL` and `#zombie-match3d` `C0880U9751A`: Julia, Robert and Vincent are members, and none has a leave event
  - DM `D05GU6L0XFH` (Julia and Robert)
  - The brief and the UA plan are shared with Julia as reader. The push sheet `f_a325dd4af80afc5994d5dc` lists Julia in `shared_with_emails`.
  - Brian's mails are delivered to Julia's mailbox, and the GCal event has a copy on Julia's calendar.
  - GitHub, Linear, Trello and Confluence are unscoped.
  - Julia is not in `#zombie-prs` `C093LEZGF6J`. The GitHub originals of the mirrored comments are unscoped, so nothing is hidden.
- **Data exists:** no fail-level finding. Advisory DR3. Every fact the rules need exists:
  - The Collect & Win windows (Mon-Tue, Wed-Thu, Fri-Sun) are in code, Confluence and Douglas's DM.
  - The release instant is 2025-10-08 15:00Z.
  - The season opens on the 1st at 00:00 UTC, per CDK `SEASON_PASS_SCHEDULE` `"0 0 1 * *"` and the Confluence spec.
  - The 24h config lock is in the Confluence `page_season_pass_spec`: "locked 24h before each season opens".
  - Brian's Oct 31 10:00 Istanbul commitment is 07:00Z, which misses the Oct 31 00:00Z lock.
  - "Product" is Robert per `page_season_pass_spec`: "Owner: Robert (Product)".
  - Push Ready/LIVE status is in two separate columns of the PNs Beta tab.
  - The game's old name "Puzzles vs Zombies" and the event's Domino name "Win & Collect" are documented: spec rename on 24 Jul 2025, and Confluence "Same feature as Win & Collect on Domino Delights, under a different name".
  - The rule's term "Aug-Sep live-ops cohort" has no defining record. It changes nothing: there are no CHANGES_REQUESTED reviews in Aug–Sep 2025 (the only one after 2025-07-15 is match3d#303, Jul 16).
- **Tool use and cross-service:** no finding. Each source changes a graded fact:
  - Slack: the asks and exclusions, Halloween pulled, the leaderboard held.
  - Docs: the rules.
  - Sheets: push rows, status and copy.
  - GCal: Collect & Win's first window moves to Fri Oct 10 00:00Z.
  - GitHub: Collect & Win DEV-only, vial models (Claire), November premium strip (Oliver).
  - Gmail: Oct 31 misses the lock, so a reply is needed.
  - Confluence: the lock, and Product = Robert.
  - Linear: the hold ticket ZOM-429, the calendar ticket ZOM-78, and several "not needed" decoys.
  - Trello: the new quest set on Oct 13.
  - The UA plan only repeats the week bounds in the DM and brief. It is not named in the prompt, so it is not a finding.
- **Hidden records:** none required.
- **Derived columns:** none. No Snowflake table is read, so no column needs recomputing.
- **Date-slip:** none. Every weekday and date checks out:
  - Mon Oct 6, Sun Oct 12, 19, 26 and Nov 2, Mon Oct 13, 20 and 27
  - Wed Oct 8, Fri Oct 10, Wed Oct 29, Fri Oct 31, Sat Nov 1
  - Mon Sep 22 and Fri Sep 26 (also matching the +0300 Date headers)
  - Every Slack ts and Trello action-id timestamp matches its `created_at` or `date`.
  - Every injected record is dated before the clock. The latest is `669d15f685f158633e56302160957f1e`, 2025-09-30T22:10:41Z.

## Checked and consistent

**Slack**
- **Frederick's DM:** parent and reply are at 20:20 and 20:24Z Sep 30, which is "yesterday". Thread fields are consistent: `reply_count` 1 and `latest_reply` set to the reply ts. Frederick is a member of `D05SD5QLG94`.
- **Robert's Halloween approval** (`933cee9f…`, Sep 18 16:40Z) replies to base `9025d428…` (Martin, Sep 17: "*Halloween theme* for an app icon or an event"). The UPDATE sets the parent to `thread_ts`=own ts, `reply_count` 1, as base parents are.
- **Robert's pull-back** (`D05GU6L0XFH`, 22:10Z) sits between base messages at 20:46Z and 2025-10-01 03:32Z.
- **Vincent's retest:** Vincent is a member of `#zombie-match3d`. The retest follows ZOM-429's "only after kill app" description and the base Sep 22 `#zombie-bugs` reports.
- **`#zombie-prs` mirror UPDATEs** change only the intended fields (I diffed them against base):
  - `4b7c41…`: Reviewers gains `<@EMPLOYEE_0025_SLACK_ID>`; `reply_count` goes from 41 to 42.
  - `d05a2f…`: Comments goes from "1" to "2"; `reply_count` goes from 2 to 3.
  - `c2b9…`: `reply_count` goes from 16 to 17.
  - Mirror shape ("Comment on pull request by arthur.blake", discussion and issuecomment id ordering, attachment ts) matches base.

**GitHub**
- **#470:** `rc_10` hangs on `rev_9` (Arthur, APPROVED, 15:51:06Z) before the merge at 15:51:15Z. The path is the same file as base `rc_7` to `rc_9`.
- **#468:**
  - `rev_3` and `rc_38` are at 15:36:41Z, before the merge at 16:13:50Z. The path `GameLoader.cs` matches the vial-spawn code in `rc_1`.
  - `ev_6` `commit_id` equals the head_sha `648e2c7b…`.
  - A "reviewed" event placed after "closed" also occurs in 17 base PRs.
- **#473:** the comment on 30 Sep at 16:16:33Z comes after the merge. Base has 5 human comments made after a merge. The UPDATE sets `updated_at` to that comment's time.
- **ZOM-432 and PR #471:** PR #471 carries Samuel's "Fixing UI Elements on Daily Gift" commit (`41a0d814`, mapped from PR commit `f0bb8b48` in `commit_map`). That commit has the message line "update header image". iOS Submission #50 and Android Submission #135 were both built on Sep 30 from main after #471 merged.
- **Arthur's #470 note,** "Collect & Win … still on the DEV stack only", is consistent with:
  - backend `a0e4a21` (Sep 29), which sets the DEV crons for fast testing
  - Owen's Sep 26 reply in DM `D05SG9H1CFM`, "Igual no va para release ahora"
  - Confluence: "Collect & Win … not yet live"
- **"Plague Race, leagues, Endless and Season Pass … already running on prod"** is consistent with the prod crons in the CDK stack and the Confluence page.

**Linear**
- All 24 comments are dated after their issue's creation. Every UPDATE moves `updated_at` forward from the base value.
- Done tickets with a null `started_at` match base (120 of 427 ZOM Done tickets).
- **ZOM-521:** the description UPDATE unticks two items, matching its open children ZOM-526 and ZOM-528. This repairs known issue SC-15.
- **ZOM-471:** the comment matches the base Slack thread (Leonard: "yeah, we don't need it! cancel the ticket"; Vincent: "it already has start button").
- **ZOM-565:** the comment matches git commit `44988da0`, 2025-09-29 14:33Z: "a little change to the prefab in the engldess screen prefab in main menu, it's still hidden in there for you to use".
- **ZOM-544:** the comment matches Vincent's base Sep 25 Apple sign-in results.
- **ZOM-543:** the comment comes after PR #472 ("Implement Win&Collect into Queue Manager") merged.
- **ZOM-566:** In Progress with `started_at` after `created_at`, and before PR #477 opened.
- **ZOM-542:** the base "Regression" state with no `started_at` is a base oddity. The injected comment does not contradict it.

**Trello**
- The action id's hex prefix decodes to the action date.
- The member is Leonard (`PERSON_6094`).
- The list name in the action data is "BETA: Sep 30", matching later actions (SC-13).
- The comments badge goes from 0 to 1, which follows the base convention (badge = number of comment actions, 45 of 45).

**Gmail**
- There is one copy per mailbox, each with its own thread id, which is the base convention.
- The labels match the `X-Gmail-Labels` header. `Label_b19fb8d1b3` is "Opened".
- The +0300 headers match `internal_date` and Brian's calendar zone UTC+03:00.

**GCal**
- The event_id, ical_uid and per-attendee copies follow base conventions.
- 15:00Z is 18:00 Istanbul, matching the description.
- The organizer's calendar zone is America/El_Salvador. That is only a plausibility point.

**Drive, Docs, Sheets, Slides**
- Google Docs named `.docx`, sheets named `.xlsx`, and slides with no extension, which is the base convention.
- `content_path` includes the folder name ("ZM Live Ops/"), as 29,239 of 29,299 base subfolder files do.
- The parents `d_8140f09…` (Julia) and `d_175c0d7…` (Frederick) are the owners' root folders.
- The brief's `style_runs` offsets match its headings exactly.
- The Slides `TEXT_BOX` elements and the slide and element id formats match base.
- The translated tab holds the Domino copy ("Domino Adventures", "River Rush", "Tiledozer & Luckydrop"), as the brief says.
- The Domino Adventure sheet's PNs Beta tab differs: it has no Ready column and holds Domino rows.

**Code and Confluence**
- The Collect & Win group names (Group1Server "Monday-Tuesday"), the CDK comments, the Confluence pages and Douglas's DM ("prod -> 2 días, 2 días, 3 días") all agree.
- The CDK prod cron strings ("0 0 * * 1,2") are a base ambiguity that none of these sources contradicts.

**Known base issues touched, none load-bearing:**
- SC-6: the `brian.foster@` address is also used by Node's CEO. The reply recipient is the same either way.
- SC-13
- SC-15 (repaired)
- SC-38: the task does not depend on the ship date.
- SC-62: hourly vs every-5-minutes reward import. The lock is a 24h process control.
- SC-70
- SC-71

**Platform defects:** none.
