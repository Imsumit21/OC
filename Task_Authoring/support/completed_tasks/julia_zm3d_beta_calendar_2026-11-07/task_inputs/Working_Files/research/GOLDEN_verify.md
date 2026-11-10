# GOLDEN ANSWER VERIFICATION — ZM3D Mon Oct 6 – Sun Nov 2 2025 (synth-cut, clock 2025-10-01 00:00 PT / 07:00Z)

> **Superseded in part by revision 2 (2026-11-06, after the 2026-11-05 /prompt FAIL).** This file verifies the revision-1 golden. Since then: Zombie Lane is off the calendar (Frederick's follow-up `D05SD5QLG94/1759263878.305127`), so the calendar has seven beats; the push plan is ten rows of the PNs Beta tab (Hourly Coins, Nathan's Treasure Hunt, Streak Fever and Axe Arena left off); Collect & Win is a late start, never a hold; the daily-gift frame is in both Sep 30 submission builds (iOS 50, Android 135). The current truth is `solver/truth.json`; the rows below are kept as the revision-1 record.
>
> **Revision 5 (2026-11-06).** Four of the checks below now rest on other records or other words, and the rows keep their revision-1 ids. The Collect & Win first window still rests on Arthur's `#470#rc_10`, which is now part of his base approval review (2025-09-30T15:51:06Z, before the merge), same words. The Collect & Win still-to-do names the final vial models (Claire) on `#468#rc_38`; the note was about vial sprites and sat on another PR here. The Daily Login check rests on Samuel's closing note `cmt_zom432_2` on ZOM-432, which is Done; nothing is seeded on #471 any more. The Quests still-to-do no longer exists: the quest note, now Leonard's on the open quests card, says the current set carries the first week. The five Slack messages people wrote and Brian's two mails have new ids (dossier §11, Revision 5). The current truth is `solver/truth.json`.
>
> **Revisions 6 and 7 (2026-11-06).** The golden values do not change: `solver/truth.json` is byte for byte the revision-5 file. The quest note now reads "More quests get added with the Mon Oct 13 rollover if they are ready. Nothing in the beta waits on them, the current quests keep running either way."
>
> **Revision 8 (2026-11-06).** The golden values do not change; one evidence id does. The Season Pass still-to-do rests on Arthur's inline note `#472#rc_1` (it was `#473#c_2`), and the quest note now reads "More quests get added with the Mon Oct 13 rollover if they are ready. The rollover does not wait on them, the current quests keep running either way."
>
> **Revision 9 (2026-11-06).** The golden values do not change, and neither does any evidence id: `solver/truth.json` is byte for byte the revision-8 file. The brief's still-to-do rule is closed (a held beat's fix plus what has been flagged for that beat as not done since the brief), and every still-to-do value fits it (dossier §11 Revision 9). Robert's withdrawal now says "the themed prop set I okayed in Martin's thread", and the quest note reads "More quests and the reward balance go in with the Mon Oct 13 rollover if they are ready. The rollover does not wait on them, the current quests keep running either way."
>
> **Revision 10 (2026-11-06).** Two golden changes, both deliberate, and no evidence id moves. Owners: Weekly Leagues' fix reads "(Douglas)" (it read "(league owner)"), and Collect & Win's server-windows item names Douglas. Weeks running: Quests and Daily Login read "All four weeks" (they were empty). Every other value is the revision-9 value. The current truth is `solver/truth.json`.
>
> **Revision 11 (2026-11-06).** No golden value changes. One evidence id is added: `cmt_zom465_3` (Brian: the Collect & Win icon has to land). Some quotes in the rows below are older than these words. Robert's approval now reads "for one week of the beta" and "if it lands in time", his withdrawal ends at "Sorry for the flip.", the brief says a date that misses the lock "moves to any time before it", and Collect & Win windows close "23:59 UTC on its last day", so W1's windows end Tue Oct 7 and Thu Oct 9 at 23:59 UTC. None of this moves Fri Oct 10 00:00 UTC. The current truth is `solver/truth.json`.
>
> **Revision 12 (2026-11-06).** Three golden cells that were empty are filled, all deliberate, and no evidence id moves. Weekly Leagues' First window reads Mon Oct 6 00:00 UTC and its Weeks running All four weeks (the brief's held-row sentence), and Season Pass's First window reads Mon Oct 6 00:00 UTC (the clip sentence). Every other value is the revision-11 value. Some quotes in the rows below are older than these words: the brief now closes every window at 23:59 UTC, says "windows and weeks", "(Login Calendar and Weekly Rankings are fine)" and "what its row is missing", and Arthur's vial note says the models "need to be in before the beta". The current truth is `solver/truth.json`.
>
> **Revision 13 (2026-11-06).** No golden value and no evidence id changes; `solver/truth.json` is the revision-12 file. Some quotes in the rows below are older than these words: Arthur's vial note now says the vials "still need their final models before the event runs. Not a blocker for this PR", and the brief says "the rotating shop" and "with which of those its row is missing".
>
> **Revision 14 (2026-11-06).** No golden value and no evidence id changes; `solver/truth.json` is the revision-13 file. Some quotes in the rows below are older than these words: the brief's lock rule now ends "and you tell its owner in a reply on the mail where they committed to it", and its span section adds "Endless goes down as its weekly windows, with the daily reset noted."


Sources read: `Task_Authoring/task_inputsS/01_Universe_Inject.sql` (sha256 `4c6328ab2e86…`, 59,953 B, mtime Nov 5 19:26 — **matches** the rev1 hash cited in `01c_Preflight_Report.md` line 3) for seeded rows, and the base exports (`TASK_AUTHORING_TASK_DIR` universe `Universe_SynthCut`) for base-only records (Confluence page, push sheet, Trello, PR bodies, Slack thread). Golden: `Task_Authoring/task_inputsS/Working_Files/solver/truth.json`. Base "brief" = `gdocs.docs_documents f_7c3e91a4d2b85f60e1a9c4` "ZM3D beta live-ops calendar - working rules" (Frederick, Sep 24).

---

## 1. Collect & Win first window = "Fri Oct 10 00:00 UTC" — **CONFIRM**

- Seeded `github.github_review_comments` id `harmonygames-Games/match3d#470#rc_10` (PR #470 "Collect And Win minor bugs fixes", author `EMPLOYEE_0025`, 2025-09-30T16:04:12Z):
  > "Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The client side in this PR is fine as it is."
- Seeded `gcal.gcal_events` id `evt_9a4c2e7f1b3d58e06c7a2f` (Douglas's calendar, also mirrored as `evt_5c1e83a7d94b02f6c8e31a` Julia / `evt_a72f4d9e0c1b58d3e6f40b` Owen / `evt_1d6b9a03e5c27f84b0d92c` Frederick):
  > summary "ZM3D backend release — live-ops server windows"; description "Prod backend deploy for the beta. The live-ops server windows go live with this release; release window 18:00-19:00 Istanbul time."; `start_ts` = `2025-10-08 15:00:00+00` (= 18:00 Istanbul, UTC+3 — self-consistent).
- Brief rule (`f_7c3e91a4d2b85f60e1a9c4`, "When a beat starts"):
  > "A beat starts with the first window that opens after its server windows are live on prod, the backend release instant read in UTC, not when its client PRs merged. Collect & Win runs Mon-Tue, Wed-Thu and Fri-Sun, each opening 00:00 UTC, so a window the release instant pre-empts does not count."
- Chain check: W1 windows are Mon Oct 6 00:00 → Wed Oct 8 00:00, Wed Oct 8 00:00 → Fri Oct 10 00:00, Fri Oct 10 00:00 → Mon Oct 13 00:00 (UTC). Release opens Wed **2025-10-08 15:00Z**, i.e. 15 h *inside* the already-open Wed-Thu window ⇒ that window is pre-empted and does not count. First window opening after 15:00Z = Fri Oct 10 00:00 UTC. Weekdays verified: 2025-10-08 = Wed, 2025-10-10 = Fri.
- Verdict: golden "Fri Oct 10 00:00 UTC" is correct; "Wed Oct 8" and "Mon Oct 13" are both wrong.

## 2. Weekly Leagues = Held — **CONFIRM** (and the earlier ZOM-429 read is now superseded)

- Seeded `linear.linear_comments` id `cmt_zom429_1` (ZOM-429, 2025-09-23T16:12:00Z):
  > "Checked the weekly rollover - if a player force-closes and reopens, they land in the new week fine, so not blocking. Leaving as-is for now."
- Seeded `slack.slack_messages` `C0880U9751A/1759265412.481907` (channel `C0880U9751A`, user `EMPLOYEE_0012_SLACK_ID`, created 2025-09-30T20:50:12Z) — the changed re-test, now in the SQL:
  > "Re-tested the weekly leaderboard on the current prod build: it still does not start a new week. I killed the app and reopened it twice, played a few levels, and my week is still last week one. Same on the second device."
- Brief hold rule (`f_7c3e91a4d2b85f60e1a9c4`, "Held or not"):
  > "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it; an unverified build or platform is a still-to-do, not a hold. Wrong counters, a reset that needs a restart, cosmetic, VFX and performance gaps and analytics gaps do not hold a beat, and neither does a change request outside the Aug-Sep live-ops cohort."
- Test against the rule: the re-test is (a) on **prod**, (b) repeated on a **second device**, (c) **after two restarts**, (d) a failure to enter/score the new week. That is precisely "provably cannot … on prod even after a restart" ⇒ Held is defensible. The DATED evidence beats `cmt_zom429_1` (Sep 23, "reopen … lands in the new week fine"): the Sep 30 prod re-test explicitly retests and contradicts the restart workaround, so ZOM-429's "not blocking" conclusion is **superseded**, not merely outranked.
- Note the residual tension: both records describe the *same* restart path and reach opposite conclusions. The golden read is only safe because the re-test is (i) later and (ii) more rigorous (current prod build, twice, two devices). If a grader required a disjoint mechanism this criterion would be arguable — it is not a refutation.

## 3. Plague Race = Runs, Weeks = "All four weeks" — **CONFIRM** (weeks value is derived, not quoted)

- Seeded `slack.slack_messages` `C08R8CHB0QL/1758213600.552913` (Robert, `EMPLOYEE_0016_SLACK_ID`, 2025-09-18T16:40:00Z):
  > "Halloween one-off: approved from my side for one of the beta weeks. It can take a recurring slot that week, one themed prop set only, no new mechanics, and I sign the object off if it lands before the cut."
- Seeded `slack.slack_messages` `D05GU6L0XFH/1759270200.638114` (Robert, 2025-09-30T22:10:00Z):
  > "Coming back on the Halloween one-off: pulling my ok. Take it off the beta calendar, we are not spending art time on a theme we may not ship at all. Sorry for the flip, my later word on this one is the one that counts."
- Brief rule (`f_7c3e91a4d2b85f60e1a9c4`, "One-offs"):
  > "A one-off may take a recurring beat slot only with Product latest dated approval, and if he takes that back his later word is the one that counts."
- Chain check: approval (Sep 18) is the *latest dated* approval at that time, but the Sep 30 withdrawal is later and by the same Product owner, and it both withdraws the ok and removes the event from the calendar ("Take it off the beta calendar") ⇒ no one-off displaces any Plague Race slot ⇒ Plague Race keeps all four weekly slots it holds, "All four weeks". Weekday/span check: Oct 6 – Nov 2 is exactly W1–W4 (Mon Oct 6, Mon Oct 13, Mon Oct 20, Mon Oct 27 starts; Nov 2 = Sun).
- Caveat: no single record states the phrase "all four weeks"; it is inferred from Plague Race being a recurring in-span beat with its one-off competitor withdrawn. Flagged as derived, not quoted.

## 4. Season Pass: Status Runs; premium strip → November; November config lands before Oct 31 00:00 UTC — **CONFIRM**, and the 24 h offset really is base-Confluence, not the brief

**(a) The 24 h rule lives in BASE Confluence `page_season_pass_spec`, not in the seeded brief.**
- Base record `confluence.pages` id **`page_season_pass_spec`**, title "ZM3D Season Pass — Spec", space `space_PROD`, parent `page_zm3d_gdd`, `version` 2, `updated_at` 2025-09-30T17:30:00Z:
  > "Season config (tiers, rewards, theme) is authored in the live-ops tool and **locked 24h before each season opens**; no hotfixes to reward tables mid-season without Product sign-off."
- The seeded brief contains only the lock *existence* + UTC + slip rule and **no offset**: "Every config a beat needs lands before its lock, read in server time (UTC). A committed date that misses the lock moves earlier and its owner is told."
  ⇒ **Deciding authority for the 24 h offset = `page_season_pass_spec` (base Confluence). The brief alone cannot yield 24 h.** Confirmed as stated.

**(b) Season 2 opens Sat Nov 1 00:00 UTC ⇒ lock = Fri Oct 31 00:00 UTC.**
- `page_season_pass_spec`: "production seasons reset monthly on the 1st at 00:00 UTC".
- Brief: "Season Pass seasons open on the 1st at 00:00 UTC."
- Seeded mail `julia.lawson@harmonygames.co/1844835127305531392` (Brian, 2025-09-26T07:40:00Z): "Season 2 opens on Sat Nov 1." 2025-11-01 = Sat ✓. Nov 1 00:00 UTC − 24 h = **Fri Oct 31 00:00 UTC** (= Thu Oct 30 17:00 PDT). ✓

**(c) Brian's slip is 7 h late.**
- Same mail (`julia.lawson@harmonygames.co/1844835127305531392`, `Message-ID <CAH4q9Zc8uV1nE5kJ2mRtP7aW3xQ9bLs@mail.gmail.com>`, In-Reply-To the Sep 22 handoff):
  > "Correction to my Sep 22 mail, Frederick in copy: the November Season Pass config handoff moves from Wed Oct 29 to Fri Oct 31, 10:00 Istanbul time. Same contents, same owner, I just need the two extra days on the premium track. Treat Fri Oct 31 as the date I am committing to and drop the Oct 29 one. Season 2 still opens on Sat Nov 1."
- 10:00 Istanbul (UTC+3, consistent with the release event "18:00-19:00 Istanbul" = 15:00Z) = **07:00 UTC** on Fri Oct 31, i.e. 7 h after the 00:00 UTC lock ⇒ miss ⇒ per brief "A committed date that misses the lock moves earlier and its owner is told" ⇒ still-to-do = config lands before Oct 31 00:00 UTC (Brian told). ✓
- Premium strip: seeded `harmonygames-Games/match3d#438#rc_74` (PR #438 "Feature/season pass", 2025-09-30T20:41:17Z):
  > "The Season Pass premium strip needs to move to the November range rather than the current one — Oliver is taking the date change." ✓ (matches golden owner "Oliver").

## 5. Collect & Win still-to-do also includes the event-icon animation — **CONFIRM**

- Seeded `github.github_pr_comments` id `harmonygames-Games/match3d#454#c_4` (PR #454 "Marcus/animated icons", author `PERSON_0396_GITHUB_USERNAME` = Marcus, 2025-09-30T18:05:52Z):
  > "The Collect & Win event icon animation is still to do on my side — the other menu icons in this PR are finished."
- BASE `github.github_pull_requests` id `harmonygames-Games/match3d#456` ("[PERSON_NAME_0029]/animated icons", merged 2025-09-24T14:30:39Z) body:
  > "Added Icon Animation for: — Quest Icon — Season Pass Icon — Zombie Lane Icon — Plague Race Icon — Endless Mode Icon — Infinite Boss Icon"
  ⇒ six icons enumerated, **Collect & Win omitted**. Corroborated by #456's own bot summary ("Animated attention indicators added to Endless, Plague Race, Quests, Season Pass, Zombie Lane, and Infinite Boss icons"). ZOM-465 (`cmt_zom465_1`, "every event icon animates at idle now") is the decoy that makes #454's "still to do on my side" decisive: it is later (Sep 30) and names the specific icon.
- Golden's other Collect & Win still-to-dos also hold: `harmonygames-Games/match3d#370#rc_1` "The final vial sprites are still missing for the Collect & Win set — Claire has those on her list."; plus the Oct 8 backend release from item 1.

## 6. Daily Login still-to-do = empty; Quests still-to-do = new quest set Mon Oct 13 (Brian) — **CONFIRM**

- Daily Login: seeded `github.github_pr_comments` id `harmonygames-Games/match3d#471#c_18` (PR #471 "Samuel/zom 498 536", 2025-09-30T21:07:26Z):
  > "The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed."
  This supersedes `cmt_zom432_1` "Daily gift artwork still needs the frame. Card back and gift box are done, the frame is the last piece on my side." (Sep 24) — the frame is now shipped ⇒ nothing left ⇒ still-to-do empty ✓. `cmt_zom556_1` independently shows the mechanic works ("Claimed the daily gift on the submission build after skipping a day, it paid out and moved to the next day. The counter display on the main menu is cosmetic").
- Quests: BASE `trello.trello_actions` id **`68dac8204f1e9a3b7c2d5e61`** (type `commentCard`, 2025-09-29T17:55:44Z, board "ZM ROADMAP", card `6851a724601a61857a1b202f` "[Feature] Quests and Milestones and Achievements"):
  > "Putting the new quest set in with the Mon Oct 13 rollover."
  2025-10-13 computes as **Monday** ✓ (and the card's `dateLastActivity` is bumped to the same instant).
- Note: `cmt_zom534_1` (quest points rollover syncing, "Watching one backend timing edge case on the day boundary") is a distractor — no prod entry/score/claim failure, so it is neither a hold nor a "flagged art is missing" still-to-do.

## 7. PUSHES — base sheet `f_a325dd4af80afc5994d5dc`, tab index 1 "PNs Beta" — **all six CONFIRM**

Spreadsheet title "Push Notifications Zombie Match"; tabs by index: 0 = "PNs" (22 rows), **1 = "PNs Beta" (987 rows, 26 cols)** ← used, 2 = "PN BETA Translated", 3 = "Deep Links (not used)". Header row 0 = `['', 'Status', 'Type', 'What', 'When', 'Details', 'Segmentation', 'Destination', 'Status (NA, WIP, LIVE)', 'Headline', 'Body', 'Action Button', …]`. Exactly **six** rows carry `Status = "Ready"`.

| Push (row locator) | `Status` | `Status (NA, WIP, LIVE)` | Copy | Golden | Verdict |
|---|---|---|---|---|---|
| (a) Lives recharged — Type `Core Game`, What `Local Notification`, When `Rollover`, Details `When lives are recharged` | `Ready` | **`LIVE`** | H "Full Ammo Reloaded! 🔫" / B "Your energy is fully charged! The zombies are closing in—jump back into the battle now and show them who's boss. 🧟⚔️" — **no other game named** | Send | **CONFIRM** |
| (b) 1-day lapse — Type `LAPSED`, When `1 Days Lapsed`, Details `Has not played in 24 hours` | `Ready` | **`LIVE`** | H "The Horde Is Growing… 🧟‍♂️" / B "The zombie outbreak won't stop on its own! **Return to Puzzles vs Zombies now** and continue your mission…" | Held (old title) | **CONFIRM** |
| (c) 7-day lapse — Type `LAPSED`, When `7 Days Lapsed`, Details `Has not played in seven days.` | `Ready` | **`LIVE`** | H "They've Taken Over… Can You Stop Them? 😱" / B "It's been a while, survivor. The undead are stronger than ever. Rally your gear and get back into the fray before it's too late! 🧟‍♀️💥" — clean | Send | **CONFIRM** |
| (d) D0-1 FTUE — Type `FTUE`, When `D0-1`, Details `Finish first tutorial` | `Ready` | **`LIVE`** | H "Finish Your First Mission! 🎯" / B "You're so close! [PERSON_NAME_2549] **your first mission in Puzzles vs Zombies** and unlock powerful tools to fight the undead…" | Held (old title) | **CONFIRM** |
| (e) Plague Race — Type `Event`, When `Event Start (server time)`, Details `Plague Race` | `Ready` | **`WIP`** | H "Plague Race Is On! 🌊🚣" / B "Compete in Plague Race now! …" (copy itself clean) | Held (not wired) | **CONFIRM** |
| (f) Weekly Leaderboard reset — Type `Event`, When `Weekly Rollover`, Details `Weekly Leaderboard reset` | `Ready` | **`WIP`** | H "Weekly Rankings Reset! 🧟‍♀️📈" / B "**New week, fresh shot at glory!** Climb the leaderboard and prove you're the ultimate zombie slayer. Ready to dominate? 💪" | Held (WIP) | **CONFIRM** |

- (f) is **WIP, not LIVE** — explicitly checked; it is the row most likely to be misread because its copy is clean and its "Status" column says Ready. Held for "not wired", not for copy. This also lands consistently with item 2 (Weekly Leagues Held).
- Brief push rule (`f_7c3e91a4d2b85f60e1a9c4`, "Push copy"): "A push goes out only if its row is **Ready and LIVE** and its English copy names the game only as **Zombie Match 3D** and events only by their ZM3D names. Anything else is held, with what is missing."
- **NOTE / doc correction:** the instruction "sheet index 0 is a different 'Domino Quest' tab" does not match the base export — index 0 is titled **"PNs"** (a 22-row, 10-col set whose Ready rows are *not* the ZM3D set; its first data rows are Quests "New Quests Await!", Hourly Coins, etc.). The ZM3D beta push set is unambiguously **index 1 "PNs Beta"**, so the golden values are unaffected, but the label in the prior brief is wrong.
- **NOTE (cosmetic):** base-export anonymisation left `[PERSON_NAME_2549]` where the word "Finish" belongs in the FTUE body. The old-title trigger ("Puzzles vs Zombies") is intact.

## 8. Endless Monster Mode = Runs; Zombie Lane = Runs — **CONFIRM**

Brief carve-out (`f_7c3e91a4d2b85f60e1a9c4`):
> "Hold a beat only when players provably cannot enter, score or claim on prod even after a restart. An established failure holds it; an unverified build or platform is a still-to-do, not a hold. Wrong counters, a reset that needs a restart, cosmetic, VFX and performance gaps and analytics gaps do not hold a beat…"

**Endless Monster Mode** — seeded `linear.linear_comments`:
- `cmt_zom565_1` (2025-09-29T16:05:00Z): "The endless start screen vfx went in with build #2023 (commit f7e971b0). Claim button glow and the new bar are both live now, can close." ⇒ VFX outstanding item is *shipped*, and VFX could not hold anyway.
- `cmt_zom504_1` (2025-09-22T15:30:00Z): "Tried to reproduce across a long endless session. Saw it once, and the object clears on the next throw. Visual only, no board state affected." ⇒ cosmetic, explicitly not a hold.
- `cmt_zom521_1`: "Master VFX checklist is down to the last two items, both polish on existing effects. Everything the live-ops side asked for is in." ⇒ polish, not a hold.
- Result: no entry/score/claim failure ⇒ **Runs**, empty still-to-do ✓.

**Zombie Lane** — the cited Slack record `C08R27X0EAH/1758903616.346579` exists (channel `C08R27X0EAH`, author `EMPLOYEE_0012_SLACK_ID`, 6 replies, 2 repliers, +1 reaction, one PNG `IMG_4696.png`) and is a **fixed-bug + iOS-build-pending** thread, i.e. exactly the "unverified platform = still-to-do, not a hold" case:
- parent `1758903616.346579`: "After I skipped the zombie lane tutorial, ı got the exception and skipping couldn't claim the ice cream."
- `1758913350.470119` (EMPLOYEE_0003): "sent a fix"
- `1758913366.419089`: "android 1977, can you test it please?"
- `1758913375.794899`: "I tested on my phone and its working"
- `1758917016.015499` (EMPLOYEE_0012): "Thank you!"
- `1758917022.439979`: "Checking it rn"
- `1758917074.996069` (**last reply**): "Can you trigger an ios build"
- Read: the claim failure was reproduced, fixed and verified on Android within the thread; the only open item is an iOS build ⇒ per the carve-out that is a still-to-do for an unverified platform, **not** a hold ⇒ **Runs** ✓. (Also note the failure needed "skipped the tutorial", a path the brief does not treat as an entry/score/claim block for players generally.)
- Supporting seeded records: `cmt_zom526_1` ("Token-to-live-ops travel is in progress… finishing it alongside Season Pass") and `cmt_zom542_1` ("Home screen and victory score layouts are in for endless and boss arena. Regression pass on the mode switch looks clean.") — the "in progress" travel work is not a hold trigger either.

---

## SUMMARY TABLE

| # | Field | Golden value (truth.json) | Verdict | Deciding record(s) + 1-line evidence |
|---|---|---|---|---|
| 1 | Collect & Win — First window (UTC) | `Fri Oct 10 00:00 UTC` | **CONFIRM** | `#470#rc_10` windows "DEV stack only … reach prod with the next backend release" + `evt_9a4c2e7f1b3d58e06c7a2f` start `2025-10-08 15:00Z`; 15:00Z falls inside the Wed-Thu window ⇒ pre-empted; next 00:00 UTC opening is Fri Oct 10 |
| 2 | Weekly Leagues — Status | `Held` | **CONFIRM** | `C0880U9751A/1759265412.481907` "still does not start a new week … killed the app … twice … Same on the second device" (prod, post-restart) supersedes `cmt_zom429_1` "if a player force-closes and reopens, they land in the new week fine" |
| 3 | Plague Race — Status / Weeks | `Runs` / `All four weeks` | **CONFIRM** (weeks derived) | `C08R8CHB0QL/1758213600.552913` approval withdrawn by `D05GU6L0XFH/1759270200.638114` "pulling my ok. Take it off the beta calendar … my later word on this one is the one that counts" ⇒ no one-off displaces a slot |
| 4 | Season Pass — Status / still-to-do | `Runs` / premium strip→Nov (`#438#rc_74`) + config before Oct 31 00:00 UTC | **CONFIRM** | base `page_season_pass_spec` "locked 24h before each season opens" + mail `julia.lawson@harmonygames.co/1844835127305531392` "Fri Oct 31, 10:00 Istanbul" = 07:00Z = 7 h past the Oct 31 00:00Z lock |
| 5 | Collect & Win — event-icon animation in still-to-do | included (Marcus) | **CONFIRM** | `#454#c_4` "The Collect & Win event icon animation is still to do on my side"; base `#456` body lists only Quest/Season Pass/Zombie Lane/Plague Race/Endless/Infinite Boss |
| 6 | Daily Login / Quests — still-to-do | empty / new quest set Mon Oct 13 (Brian) | **CONFIRM** | `#471#c_18` "daily-gift frame … in submission 135, so that one can be closed"; Trello `68dac8204f1e9a3b7c2d5e61` "with the Mon Oct 13 rollover" and 2025-10-13 = Monday |
| 7a | Lives recharged | `Send` | **CONFIRM** | PNs Beta: `Ready` + `LIVE`; body "Your energy is fully charged! The zombies are closing in…" names no other game |
| 7b | 1-day lapse | `Held` (old-title copy) | **CONFIRM** | PNs Beta: `Ready` + `LIVE`; body "Return to Puzzles vs Zombies now …" |
| 7c | 7-day lapse | `Send` | **CONFIRM** | PNs Beta: `Ready` + `LIVE`; body "It's been a while, survivor. The undead are stronger than ever…" clean |
| 7d | D0-1 FTUE | `Held` (old-title copy) | **CONFIRM** | PNs Beta: `Ready` + `LIVE`; body "… your first mission in Puzzles vs Zombies …" |
| 7e | Plague Race start | `Held` (not wired) | **CONFIRM** | PNs Beta: `Ready` + `WIP` |
| 7f | Weekly Leaderboard reset | `Held` (not wired) | **CONFIRM** | PNs Beta: `Ready` + **`WIP`** (not LIVE); body "New week, fresh shot at glory!…" |
| 8a | Endless Monster Mode | `Runs` | **CONFIRM** | `cmt_zom565_1` vfx "went in with build #2023 … can close"; `cmt_zom504_1` "Visual only, no board state affected" |
| 8b | Zombie Lane | `Runs` | **CONFIRM** | `C08R27X0EAH/1758903616.346579` thread: "sent a fix" → "android 1977" → "I tested on my phone and its working" → last reply "Can you trigger an ios build" (= unverified platform ⇒ still-to-do, not hold) |

**REFUTE / UNCERTAIN: none.** Every golden value in `truth.json` survived the record check. Two documentation defects (neither touches a golden value): (i) the push sheet's tab index 0 is titled **"PNs"**, not "Domino Quest" — the beta set is index 1 "PNs Beta" as assumed; (ii) Plague Race "All four weeks" is a derived value (no record states the phrase). Two flagged residuals: Weekly Leagues "Held" rests on a single (but later, on-prod, two-device, post-restart) re-test that directly contradicts `cmt_zom429_1`, and the 24 h Season Pass lock exists **only** in base Confluence `page_season_pass_spec` — if a graded criterion cites the brief for the 24 h offset it is ungrounded.
