# K3 carrier check: match3d PR #476 "Vision bot" (synth-cut, clock 2025-10-01 07:00 UTC)

Status: COMPLETE. **Verdict: USE WITH CHANGES.** #476 fixes the post-merge problem, but three section 10 plans no longer work (section 7). No SQL was run. No universe git was touched. Times are UTC.

## 1. True state at the clock: OPEN
- data.json: `state open, merged false, merged_at null, closed_at null`, updated 09-30T19:03:57Z. Head 077e1ccf "Add vision bot to scene list". #zombie-prs has the opened root and no merged reply; #builds has no merge signal.
- The KB line is wrong at this clock. It is `orientation_only`, built from the Normal universe: Normal has merged 2025-10-02T16:40:52Z (ev_12, ev_13).
- Confluence: `page_qa_runbook` is cited as KB evidence but does not mention the bot or #476 ("vision" and "476" searches miss page 7). Last updated 2025-08-04, before the PR.
- Cut residue, on no SC card: timeline ev_4 to ev_7, ev_10, ev_11 are undated `reviewed` rows on 3 SHAs missing from commits (25fd8304, bb2e3318, fa7b7012). ev_8, ev_9 are absent. Same family as SC-18. No text in #476 says closed. SC-50 applies to bot authors. No other card touches it.

## 2. EMPLOYEE_0025 is Arthur Blake, CTO (github users, commit author, branch `Blake/visionBot`)
- 12 inline comments in match3d, all pre-merge, short and plain. 4 are on his own PRs: #265 rc_3 "I'll do this in a later PR...", rc_5 "Yes.", #281 rc_2, #395 rc_4 "This is intentional as I want it to simulate more when timescale is high."
- All 4 own-PR comments answer a bot point, and CodeRabbit replied 26 to 66 seconds later (rc_4, rc_6, #281 rc_3, #395 rc_5). So the author is the right host: an own-PR note is base behaviour.
- 11 of 12 have a same-second or 1-second empty COMMENTED or APPROVED review row (exception: #336 rc_30). This is the same shape as #470 rev_3 and rev_5.
- Other humans do not fit. Vincent Parker (EMPLOYEE_0012) has 0 inline and 0 reviews in match3d. Samuel Turner (EMPLOYEE_0004), who co-built the bot, has 0 inline and 1 approval. Nobody reviewed bot PRs #298, #355, #368, and #395 has only Arthur's own row. Vincent wrote the test content; he should not be the commenter.

## 3. What the bot tests: Unity editor only, no device in any record
- PR body: "A computer vision bot that plays through the game based on a QA provided regression test list." and "Editor runners/CLI for bot plans".
- VisionBatchCLI.cs (rc_5 hunk) opens `#if UNITY_EDITOR`; `Fail` calls `EditorApplication.Exit`.
- Arthur, D06KV30TPL4 1758049994.128899 (Samuel): "1. Run Unity editor from command line 2. It runs the first instruction a. It puts editor in play mode".
- Arthur, D07H86MU8JC 1758753622.966709 (Oliver): "It's a separate jenkins job that does automated testing". #builds run #5 change: "Load vision bot scene on start of vision bot cli".
- Tech Stack doc (`f_edf29b87f8329072f6399d`): "Currently runs locally." Julia reach UNVERIFIED.
- Test list (D06477JGUKT 1757678809.625329): core game, Plague Race, Buy Premium Pack. No device field.
- Nothing names Samsung, a handset or a device farm with the bot (Sep Slack search; other months give 3 unrelated bot hits). Supported: "ran in the editor, no phone". Absence plus code, so "no device" is an inference, and "did not run on Samsung hardware" is a true subset of it.
- Soft tension: Gemini notes of Sep 19 (gmail threads/00015385.json, robert@ copy, auto-generated) say "integrated into their build system for nightly QA runs". No device claim, but #builds shows no nightly pattern, so never call the runs nightly. Gmail "regression test" scan stopped at its limit (47,381 of 81,406 files); "vision bot" and "visionbot" scans were complete.
- Do NOT say it cannot run on a device: head commit adds the scene to build settings, and commands pass `-buildTarget Android` (an editor flag; a misread risk).
- Julia reach: PR YES, #builds YES, runbook YES. All DMs and #executives NO, so those quotes are grounding only.
- Base runbook is a second route (Julia-visible): "Manual QA regression pass", "on real devices, not just the emulator", device lab "current-gen Samsung / Pixel", sign-off is a matrix in #zombie-bugs. "matrix" has 0 hits in Sep Slack.

## 4. Ticket and date coherence: works, with limits on what a "pass" can be
- Vision Bot job, #builds C05433XK267, 13 results: #1 Failure (09-23); Success #4, #5, #6, #8, #11, #12, #14, #15; **#13 on main Failure after 51 min** (1758749934.741359). Last run: **#15 Success 09-25 12:31Z, 8 min 4 sec, `Blake/visionBot`** (1758803475.436309).
- No bot run in #builds for the five days before the last row (09-30 21:43Z). The bot never passed on main. Runs from #11 follow "Add simpler test set for vision bot instructions".
- So a pass exists only as #15 or earlier, branch only, before Sub #49/#133 (09-26). Citing it as covering any build or as a full regression contradicts base.
- A Sep 30 pass would need a seeded #16 Started + result pair (INT-06). Not recommended; #15 needs no seed.
- Order works with no out-of-order close: ZOM-567 created after 16:26:02Z, comment after 19:04Z, before 00:00Z. If the ticket names #476 it must close after 18:54:32Z, when the PR first exists. If it names only the job or branch, any close from 16:27Z works.

## 5. Mechanics
- **GitHub rows:** `harmonygames-Games/match3d#476#rc_27` (seq 27); `#rev_3` (seq 3) COMMENTED, empty, same timestamp; UPDATE `updated_at`. Next free timeline id ev_12 in synth-cut; optional, Julia's seeded reviews had none.
- **Placement:** path `Assets/Scripts/Utils/Bot/Editor/VisionBatchCLI.cs`, hunk `@@ -0,0 +1,191 @@\n+#if UNITY_EDITOR`, line 1, commit 077e1ccfa22de4346c16360441bd35badaaeea46, side RIGHT, subject_type line. Same shape as Julia rc_7. Leave `in_reply_to_id` NULL (0 of 1387 in base).
- **Container:** not structurally required, but 11 of 12 base rows have one. Keep it (section 7).
- **Mirror:** root C093LEZGF6J 1759258475.735779, row id 637fc98bc66d41b104fe243006fdcf98, reply_count 29, reply_users_count 1, latest_reply 1759259047.051159.
- **Base does mirror human inline:** #470 rc_3 and rc_5 are rows 596 and 598, so "0 of 2" in 00_Base_Feasibility.md section 6 is wrong here. Shape: fallback "[harmonygames-Games/match3d] Comment on #476", pretext `...#discussion_r...|Comment> on pull request by ...`. The empty human review gets no copy in base.
- **Window:** INT-01 match3d ends 2025-09-30T22:33:40.631809Z. `base_check.py` needs a copy only inside it. Inside, both rc_27 and rev_3 want a copy: add one row and declare rev_3 in `integration_exceptions` (cite #470 rev_3). Lint has no same-timestamp rule, so test this.
- **Bot reply:** CodeRabbit's reply (rc_28, empty bot review, mirror) is optional. Julia rc_7 passed without one; 4 of 4 base own-PR comments had one.

## 6. Discovery
- `github_get_pull_request_comments` on #476 returns inline comments only. Raw body + hunk is 266,086 chars before JSON overhead, so it **will exceed the limit and spill to a file** (seen at 102,690 chars on #346, J r6 event 925, where the run moved on without using it).
- Order: base rows run rc_1 upward; the one stored seeded row on a multi-comment PR came first (rc_7 of 7 on #265, with seq 7 and a review id). Sort key still unknown. Predict rc_27 is the first record of the spill, not buried; do not rely on burial.
- Flags: `comments` on the PR counts conversation only (1). No body or count reveals it. Bot "posted: 23" points to bots. rev_3 would be the only human review row, which is a real cue, though it is exactly the base shape.
- Search: "regression" and "QA" match **only #476** in match3d title/body (org-wide 6 and 4 PRs). Title and branch contain neither; the body does. Hardness_Mastery line 255 says unqualified search matches title/body; I did not run it on the live tool. Finding the PR is easy; the hard step is opening the spill.

## 7. Verdict: USE WITH CHANGES
**Placement spec**
- Author: Arthur Blake, own PR. Review container: yes.
- Time: primary **22:40 to 23:50Z Sep 30**, past the INT-01 window, so no mirror, no Slack route, no exception. Fallback 20:00 to 22:30Z with mirror.
- File: VisionBatchCLI.cs, section 5 values.
- Comment must establish: the job's pass comes from editor play mode on the Jenkins machine, no phone in the loop, so green says nothing about device-specific behaviour. Short, plain, Arthur's register. In the fallback window, avoid the word "Samsung", which the mirror would expose to a Slack search. No fix, branch, build, schedule or "cannot run on device" claim.
- Ticket: ZOM-567+, created after 16:26:02Z, closed before the comment, level-20 Samsung scope, closed as not reproduced. Cite the bot run as Vision Bot #15 green; name the job or branch, not #476. No review, note, comment, device or editor words. Never "full regression", "QA sign-off", a build number, or "on main". ZOM-559 stays Todo.

**Section 10 items this replaces**
- Cite Owen Baker: void. #476 has no human reviewer; the reviewer pattern does not carry.
- Date Sep 27 to 29 past page 1: impossible. The PR opened Sep 30, and any mirror sits in the newest thread.
- Rule record: change "a QA owner's limits" to the tool owner, because Arthur is not QA.
- "One out-of-order ticket close": no longer needed.

**Residual risks**
- /injection: a no-mirror comment 7 minutes past the last channel row is defensible from the measured window, but a reviewer may call it an INT-01 gap. Use the fallback if so. Run lint on rev_3 first.
- /injection: CodeRabbit silence on an own-PR note departs from 4 of 4; Julia rc_7 is the cover.
- /prompt: the runbook lets a careful run doubt a bot-only pass with no PR read. Fair, but K3 find odds rise; re-forecast.
- /hardness: spill handling is one observation. It could turn into all-miss, so the rule must imply the PR review record, and an alternate read (`github_pull_request_read get_review_comments`) is untested for pagination.
- Grading: state "open" is safe from data.json. Do not grade the undated timeline rows or the KB line.
