-- DRAFT: GitHub review/comment notes + timeline events + PR updated_at bumps + INT-01 #zombie-prs mirrors
-- Target: 01_Universe_Inject.sql (synth-cut, clock 2025-10-01T00:00:00 PT / 2025-10-01T07:00:00Z; seed bound 2025-10-01T00:00:00Z)
-- Sources: IJ_A_slack_github.md §2/§3/§4/§5, references/universe_schema_live.json, base export rows
--   (SynthCut_HarmonyGames_GitHub/.../github/data.json; slack/messages/C093LEZGF6J/*.json), exemplar task_inputsH.
-- NOT EXECUTED. Literal values only. Parents before children.
-- Live-schema deltas vs the brief (authoritative): github_reviews and github_review_comments and
--   github_pr_comments have NO author_name column (identity is author_login only); github_timeline_events has
--   NO seq column (it carries data_json). seq is written only where it is NOT NULL (reviews, review_comments).
-- H3: deciding text lives ONLY in review_comments/pr_comments; review bodies stay empty.

-- =====================================================================================
-- A · match3d#470 — Arthur inline note under his existing empty APPROVED review rev_9
--   deciding: S01 first-window (C&W server windows on DEV, prod next backend release)
-- =====================================================================================
-- base: rev_9 APPROVED, body '', submitted_at 2025-09-30T15:51:06Z; rc_1..rc_9 used; ev_1..ev_8 used
-- created_at is post-merge (merge 15:51:15Z) so the PR's updated_at stays monotone (>= merged_at)
INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, pull_request_review_id, side, start_line, start_side, subject_type, seq) VALUES ('harmonygames-Games/match3d#470#rc_10', 'harmonygames-Games/match3d#470', 'EMPLOYEE_0025_GITHUB_USERNAME', 'Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The client side in this PR is fine as it is.', 'Assets/Scripts/UI/CollectAndWin/CollectAndWinMainScreenController.cs', '', NULL, NULL, NULL, NULL, '2025-09-30T16:04:12Z', 'harmonygames-Games/match3d#470#rev_9', NULL, NULL, NULL, NULL, 10);
-- role: authored inline note (Arthur) that carries the DEV-only window fact; parent review rev_9 untouched (empty body)

INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES ('harmonygames-Games/match3d#470#ev_9', 'harmonygames-Games/match3d#470', 'commented', 'EMPLOYEE_0025_GITHUB_USERNAME', '2025-09-30T16:04:12Z', '{}');
-- role: matching timeline event for rc_10

UPDATE github.github_pull_requests SET updated_at = '2025-09-30T16:04:12Z' WHERE id = 'harmonygames-Games/match3d#470';
-- role: PR activity bump (was 2025-09-30T15:51:15Z)

-- =====================================================================================
-- B · match3d#370 — Arthur post-merge review + inline note (final vial sprites, owner Claire)
--   deciding: S08
-- =====================================================================================
-- base: #370 has no reviews and no review comments; merged 2025-08-13T16:12:18Z; ev_1..ev_4 used
INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq) VALUES ('harmonygames-Games/match3d#370#rev_1', 'harmonygames-Games/match3d#370', 'EMPLOYEE_0025_GITHUB_USERNAME', 'COMMENTED', '', '2025-09-30T19:48:33Z', NULL, 1);
-- role: post-merge review shell (state COMMENTED, empty body — H3)

INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, pull_request_review_id, side, start_line, start_side, subject_type, seq) VALUES ('harmonygames-Games/match3d#370#rc_1', 'harmonygames-Games/match3d#370', 'EMPLOYEE_0025_GITHUB_USERNAME', 'The final vial sprites are still missing for the Collect & Win set — Claire has those on her list. Everything else in this batch is settled from my side.', 'Assets/Prefabs/Objects/PowerUps/Collect&Win Item Potion Medium Blue2.prefab', '', NULL, NULL, NULL, NULL, '2025-09-30T19:48:33Z', 'harmonygames-Games/match3d#370#rev_1', NULL, NULL, NULL, NULL, 1);
-- role: authored inline note (Arthur) naming Claire as owner of the outstanding vial sprites

INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES ('harmonygames-Games/match3d#370#ev_5', 'harmonygames-Games/match3d#370', 'commented', 'EMPLOYEE_0025_GITHUB_USERNAME', '2025-09-30T19:48:33Z', '{}');
-- role: matching timeline event for rc_1

UPDATE github.github_pull_requests SET updated_at = '2025-09-30T19:48:33Z' WHERE id = 'harmonygames-Games/match3d#370';
-- role: PR activity bump (was 2025-08-13T16:12:18Z)

-- =====================================================================================
-- C · match3d#438 — Arthur post-merge review + inline note (premium strip -> November range, owner Oliver)
--   deciding: S09
-- =====================================================================================
-- base: rev_1..rev_3 used, rc_1..rc_73 used, ev_1..ev_8 used; merged 2025-09-15T23:09:34Z
INSERT INTO github.github_reviews (id, pr_id, author_login, state, body, submitted_at, commit_id, seq) VALUES ('harmonygames-Games/match3d#438#rev_4', 'harmonygames-Games/match3d#438', 'EMPLOYEE_0025_GITHUB_USERNAME', 'COMMENTED', '', '2025-09-30T20:41:17Z', NULL, 4);
-- role: post-merge review shell (state COMMENTED, empty body — H3)

INSERT INTO github.github_review_comments (id, pr_id, author_login, body, path, diff_hunk, line, position, commit_id, in_reply_to_id, created_at, pull_request_review_id, side, start_line, start_side, subject_type, seq) VALUES ('harmonygames-Games/match3d#438#rc_74', 'harmonygames-Games/match3d#438', 'EMPLOYEE_0025_GITHUB_USERNAME', 'The Season Pass premium strip needs to move to the November range rather than the current one — Oliver is taking the date change.', 'Assets/Scripts/LiveOps/SeasonPass/SeasonPassMainScreen.cs', '', NULL, NULL, NULL, NULL, '2025-09-30T20:41:17Z', 'harmonygames-Games/match3d#438#rev_4', NULL, NULL, NULL, NULL, 74);
-- role: authored inline note (Arthur) asking for the November premium strip, Oliver as owner

INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES ('harmonygames-Games/match3d#438#ev_9', 'harmonygames-Games/match3d#438', 'commented', 'EMPLOYEE_0025_GITHUB_USERNAME', '2025-09-30T20:41:17Z', '{}');
-- role: matching timeline event for rc_74

UPDATE github.github_pull_requests SET updated_at = '2025-09-30T20:41:17Z' WHERE id = 'harmonygames-Games/match3d#438';
-- role: PR activity bump (was 2025-09-15T23:17:40Z)

-- =====================================================================================
-- D · match3d#454 — Marcus conversation comment (C&W event icon animation outstanding)
--   deciding: S11
-- =====================================================================================
-- base: c_1 only (c_2/c_3 sit on pull_request_commits ids — different table, sidestepped); ev_1..ev_5 used
INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES ('harmonygames-Games/match3d#454#c_4', 'harmonygames-Games/match3d#454', 'PERSON_0396_GITHUB_USERNAME', 'The Collect & Win event icon animation is still to do on my side — the other menu icons in this PR are finished.', '2025-09-30T18:05:52Z', '2025-09-30T18:05:52Z');
-- role: authored conversation comment (Marcus Bennett) leaving the C&W icon animation open

INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES ('harmonygames-Games/match3d#454#ev_6', 'harmonygames-Games/match3d#454', 'commented', 'PERSON_0396_GITHUB_USERNAME', '2025-09-30T18:05:52Z', '{}');
-- role: matching timeline event for c_4

UPDATE github.github_pull_requests SET updated_at = '2025-09-30T18:05:52Z' WHERE id = 'harmonygames-Games/match3d#454';
-- role: PR activity bump (was 2025-09-19T17:50:52Z)

-- =====================================================================================
-- E · match3d#471 — Samuel conversation comment (daily-gift frame shipped here / Submission #135)
--   deciding: S07 done-elsewhere
-- =====================================================================================
-- base: c_1..c_2 used, ev_1..ev_7 used; merged 2025-09-30T15:52:24Z
INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES ('harmonygames-Games/match3d#471#c_18', 'harmonygames-Games/match3d#471', 'EMPLOYEE_0004_GITHUB_USERNAME', 'The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed.', '2025-09-30T21:07:26Z', '2025-09-30T21:07:26Z');
-- role: authored conversation comment (Samuel Turner) confirming the frame shipped elsewhere

INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES ('harmonygames-Games/match3d#471#ev_8', 'harmonygames-Games/match3d#471', 'commented', 'EMPLOYEE_0004_GITHUB_USERNAME', '2025-09-30T21:07:26Z', '{}');
-- role: matching timeline event for c_18

UPDATE github.github_pull_requests SET updated_at = '2025-09-30T21:07:26Z' WHERE id = 'harmonygames-Games/match3d#471';
-- role: PR activity bump (was 2025-09-30T15:52:24Z)

-- =====================================================================================
-- F · INT-01 companions — faithful GitHub->Slack mirrors in #zombie-prs (C093LEZGF6J)
--   bot SLACK_BOT_0004_SLACK_ID; text ''; per IJ_A §2 shape; every outer ts <= 1759271620
--   (2025-09-30T22:33:40Z = INT-01 match3d window close) and equal to the GitHub note instant.
--   Threaded under the existing PR roots; root counters bumped after each insert.
--   Non-load-bearing: Julia (EMPLOYEE_0005) is not a member of #zombie-prs.
-- =====================================================================================

-- F1 · mirror of #470#rc_10  (root c2b9c90355cf8c2c4326ab19d3a24f79 / 1759180973.545069)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('c778c9b9d8fff77f59c93ce8d7902953', '1759248252.248252', 'C093LEZGF6J', 'message', 'SLACK_BOT_0004_SLACK_ID', '', 'c2b9c90355cf8c2c4326ab19d3a24f79', '1759180973.545069', 0, 0, NULL, false, 'bot_message', '[]', '[]', '[{"color":"24292f","fallback":"[harmonygames-Games/match3d] Comment on #470","footer":"<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>","footer_icon":"https://slack.github.com/static/img/favicon-neutral.png","id":1,"mrkdwn_in":["text"],"pretext":"<https://github.com/harmonygames-Games/match3d/pull/470#discussion_r2389987213|Comment> on pull request by <https://github.com/EMPLOYEE_0025_GITHUB_USERNAME|EMPLOYEE_0025_GITHUB_USERNAME>","text":"Server-side windows for Collect & Win are still on the DEV stack only, they reach prod with the next backend release. The client side in this PR is fine as it is.","title":"<https://github.com/harmonygames-Games/match3d/pull/470|#470 Collect And Win minor bugs fixes>","ts":1759248252}]', '2025-09-30T16:04:12.248252Z', '{}');
-- role: INT-01 mirror of rc_10 (id = sha256('C093LEZGF6J|<ts>')[:32])

UPDATE slack.slack_messages SET reply_count = 17, latest_reply = '1759248252.248252' WHERE id = 'c2b9c90355cf8c2c4326ab19d3a24f79';
-- role: #470 thread root counter bump (was reply_count 16, latest_reply 1759247478.371389)

-- F2 · mirror of #370#rc_1  (root d648cbe9f00776a76405345c855ea190 / 1754659329.323899)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('408dca285b06b469679d08666344cc11', '1759261713.261713', 'C093LEZGF6J', 'message', 'SLACK_BOT_0004_SLACK_ID', '', 'd648cbe9f00776a76405345c855ea190', '1754659329.323899', 0, 0, NULL, false, 'bot_message', '[]', '[]', '[{"color":"24292f","fallback":"[harmonygames-Games/match3d] Comment on #370","footer":"<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>","footer_icon":"https://slack.github.com/static/img/favicon-neutral.png","id":1,"mrkdwn_in":["text"],"pretext":"<https://github.com/harmonygames-Games/match3d/pull/370#discussion_r2389987041|Comment> on pull request by <https://github.com/EMPLOYEE_0025_GITHUB_USERNAME|EMPLOYEE_0025_GITHUB_USERNAME>","text":"The final vial sprites are still missing for the Collect & Win set — Claire has those on her list. Everything else in this batch is settled from my side.","title":"<https://github.com/harmonygames-Games/match3d/pull/370|#370 Collect&Win Items>","ts":1759261713}]', '2025-09-30T19:48:33.261713Z', '{}');
-- role: INT-01 mirror of rc_1

UPDATE slack.slack_messages SET reply_count = 3, latest_reply = '1759261713.261713' WHERE id = 'd648cbe9f00776a76405345c855ea190';
-- role: #370 thread root counter bump (was reply_count 2, latest_reply 1755101541.049049)

-- F3 · mirror of #438#rc_74  (root 2f138acf24c126ea5e1fd20ec4fecc1e / 1757974048.424039)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('cc8ce0e4827971e4bee1fc5c5ea980d5', '1759264877.264877', 'C093LEZGF6J', 'message', 'SLACK_BOT_0004_SLACK_ID', '', '2f138acf24c126ea5e1fd20ec4fecc1e', '1757974048.424039', 0, 0, NULL, false, 'bot_message', '[]', '[]', '[{"color":"24292f","fallback":"[harmonygames-Games/match3d] Comment on #438","footer":"<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>","footer_icon":"https://slack.github.com/static/img/favicon-neutral.png","id":1,"mrkdwn_in":["text"],"pretext":"<https://github.com/harmonygames-Games/match3d/pull/438#discussion_r2389988096|Comment> on pull request by <https://github.com/EMPLOYEE_0025_GITHUB_USERNAME|EMPLOYEE_0025_GITHUB_USERNAME>","text":"The Season Pass premium strip needs to move to the November range rather than the current one — Oliver is taking the date change.","title":"<https://github.com/harmonygames-Games/match3d/pull/438|#438 Feature/season pass>","ts":1759264877}]', '2025-09-30T20:41:17.264877Z', '{}');
-- role: INT-01 mirror of rc_74

UPDATE slack.slack_messages SET reply_count = 79, latest_reply = '1759264877.264877' WHERE id = '2f138acf24c126ea5e1fd20ec4fecc1e';
-- role: #438 thread root counter bump (was reply_count 78, latest_reply 1757977776.618409)

-- F4 · mirror of #454#c_4  (root ef41446756d5e1929f95817baacb1e7b / 1758301168.081329)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('8a9a746604dc5435b6d3cd79d3f19b8d', '1759255552.255552', 'C093LEZGF6J', 'message', 'SLACK_BOT_0004_SLACK_ID', '', 'ef41446756d5e1929f95817baacb1e7b', '1758301168.081329', 0, 0, NULL, false, 'bot_message', '[]', '[]', '[{"color":"24292f","fallback":"[harmonygames-Games/match3d] Comment on #454","footer":"<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>","footer_icon":"https://slack.github.com/static/img/favicon-neutral.png","id":1,"mrkdwn_in":["text"],"pretext":"<https://github.com/harmonygames-Games/match3d/pull/454#issuecomment-3349327745|Comment> on pull request by <https://github.com/PERSON_0396_GITHUB_USERNAME|PERSON_0396_GITHUB_USERNAME>","text":"The Collect & Win event icon animation is still to do on my side — the other menu icons in this PR are finished.","title":"<https://github.com/harmonygames-Games/match3d/pull/454|#454 Marcus/animated icons>","ts":1759255552}]', '2025-09-30T18:05:52.255552Z', '{}');
-- role: INT-01 mirror of c_4 (conversation comment → #issuecomment- link)

UPDATE slack.slack_messages SET reply_count = 4, latest_reply = '1759255552.255552' WHERE id = 'ef41446756d5e1929f95817baacb1e7b';
-- role: #454 thread root counter bump (was reply_count 3, latest_reply 1758304254.635769)

-- F5 · mirror of #471#c_18  (root da3fe08c76cb0ac8a9337166c8a51d00 / 1759183256.557239)
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('a0c2677988d2041ff14477598ee60261', '1759266446.266446', 'C093LEZGF6J', 'message', 'SLACK_BOT_0004_SLACK_ID', '', 'da3fe08c76cb0ac8a9337166c8a51d00', '1759183256.557239', 0, 0, NULL, false, 'bot_message', '[]', '[]', '[{"color":"24292f","fallback":"[harmonygames-Games/match3d] Comment on #471","footer":"<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>","footer_icon":"https://slack.github.com/static/img/favicon-neutral.png","id":1,"mrkdwn_in":["text"],"pretext":"<https://github.com/harmonygames-Games/match3d/pull/471#issuecomment-3349327810|Comment> on pull request by <https://github.com/EMPLOYEE_0004_GITHUB_USERNAME|EMPLOYEE_0004_GITHUB_USERNAME>","text":"The daily-gift frame went out with this PR — it is in submission 135, so that one can be closed.","title":"<https://github.com/harmonygames-Games/match3d/pull/471|#471 Samuel/zom 498 536>","ts":1759266446}]', '2025-09-30T21:07:26.266446Z', '{}');
-- role: INT-01 mirror of c_18

UPDATE slack.slack_messages SET reply_count = 8, latest_reply = '1759266446.266446' WHERE id = 'da3fe08c76cb0ac8a9337166c8a51d00';
-- role: #471 thread root counter bump (was reply_count 7, latest_reply 1759247547.085249)

-- =====================================================================================
-- Open items for 01_Universe_Inject.sql assembly
--   * subtype: IJ_A §2 says bot_message; base mirror rows in C093LEZGF6J carry subtype NULL with
--     user_id = SLACK_BOT_0004_SLACK_ID (only the channel-subscription notices use bot_message).
--     bot_message chosen per IJ_A; flip to NULL if the eval linter compares against base rows.
--   * rc_10 references rev_9 (submitted 15:51:06Z) but is stamped post-merge (16:04:12Z) so
--     updated_at >= merged_at; alternatives were updated_at < merged_at or an out-of-order #ev_9.
--   * numeric GitHub comment ids inside the Slack pretexts (2389987213 / 2389987041 / 2389988096 /
--     3349327745 / 3349327810) are invented next-in-range values; they are display URLs only.
--   * review_comments.diff_hunk/position left ''/NULL as in base file-level comments (exemplar H)
--     — no code hunks fabricated.
