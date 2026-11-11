-- DRAFT ONLY - do not execute. LINEAR comments (22, one per cohort issue) + TRELLO commentCard action.
-- Universe: synth-cut · clock 2025-10-01 00:00 PT = 2025-10-01T07:00:00Z · seed bound 2025-10-01T00:00:00Z
-- Sources: IJ_C_linear_trello.md §1-§4; universe_schema_live.json (linear_comments 9 cols, trello_actions 7 cols,
--          trello_cards.badges_json); exemplar task_inputsH/01_Universe_Inject.sql lines 49-53, 397-409.
-- Base state of all 22 issues VERIFIED against the live synth-cut export
--   (hg.py search lookup linear --file data.json --pointer /issues --key identifier -> 22/22 found,
--    records_checked 3687, scan_complete true; fields read from Services_Data/linear/data.json).
-- Base state of the Trello card / member / action-id collision verified in Services_Data/trello/data.json.
-- Rules honoured: no state_id / description / title / completed_at changes; is_edited false; sequence 1;
--   parent_id NULL; timestamps exactly YYYY-MM-DDTHH:MM:SSZ, all weekdays, all > issue started_at|created_at
--   and <= clock; each issue's updated_at bumped to its comment instant (monotonic vs base updated_at).
-- Lint note: hg_injection_lint gives 0 FAIL on this fragment; its remaining `padding_comment` CHECKs are
--   raised only by the words in the required `-- role:` annotations and are content markers, not padding rows.
-- Author ids are real linear_users rows (linear/data.json users[].id). Never usr_EMPLOYEE_0032 (placeholder name).

--
-- BASE-STATE FINDINGS (differ from IJ_C §1.3 / worth knowing at integration):
--  1. The cohort is 22 issues, not the 15 in IJ_C §1.3: ZOM-387, 442, 521, 542, 543, 544, 546 are also live ZOM
--     issues in the export. All 22 ids resolved 22/22 via lookup (scan_complete true).
--  2. The 22nd id is cmt_zom471_1. ZOM-471 is "Add red dot icon for players not in Plague Race" (Todo, Samuel
--     Turner) - it is NOT the artwork PR that shipped the daily-gift frame (that is PR #471, a different key).
--     Do not conflate the two; cmt_zom432_1 deliberately never says "#471".
--  3. ZOM-465's base description ALREADY strikes "~~Idle Icon Animation~~". The distractor comment therefore
--     reinforces prior art (it adds only the animated-icons PR pointer) and stays silent on Collect & Win.
--  4. ZOM-432's base TITLE already reads "Daily gift artwork needs to have the frame", so the natural-reading
--     todo side is partly title-borne; the true fact is PR #471 merged 2025-09-30T15:52:24Z (hence 2025-09-24
--     for the comment, so it is stale rather than wrong).
--  5. ZOM-504 / 517 / 544 / 549 are assigned to usr_EMPLOYEE_0032, a placeholder account: never used as author.
--  6. ZOM-542 state_id is "Regression" and ZOM-526 assignee_id is NULL - both left exactly as they are.
--  7. ZOM-566 created_at 2025-09-30T16:26:02Z forces its comment to the same day after that instant (19:40Z).
--
-- ============================================================================
-- BLOCK 1 - linear.linear_comments : deciding / superseded-side cohort (10 rows)
-- ============================================================================

-- ZOM-429 (Backlog, started_at NULL, created 2025-07-22T15:14:49Z, base updated_at 2025-09-22T14:51:23Z)
-- deciding: carries the superseded "restart gets players in, not blocking" side (Tue 2025-09-23)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom429_1', 'ZOM-429', 'usr_cd7849ec043ab3da', NULL, 'Checked the weekly rollover - if a player force-closes and reopens, they land in the new week fine, so not blocking. Leaving as-is for now.', false, '2025-09-23T16:12:00Z', '2025-09-23T16:12:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-23T16:12:00Z' WHERE id = 'ZOM-429';

-- ZOM-556 (Todo, created 2025-09-22T14:44:06Z; description is the player report only, no status words)
-- deciding: claims the daily-login streak reward WORKS, counter display is cosmetic (Wed 2025-09-24)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom556_1', 'ZOM-556', 'usr_65c76e0b87aa7e9b', NULL, 'Claimed the daily gift on the submission build after skipping a day, it paid out and moved to the next day. The counter display on the main menu is cosmetic, the streak itself is fine.', false, '2025-09-24T15:20:00Z', '2025-09-24T15:20:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-24T15:20:00Z' WHERE id = 'ZOM-556';

-- ZOM-565 (Todo, created 2025-09-25T13:46:04Z; description = Marcus VFX spec, no ship/merge words)
-- deciding: "shipped with build #2023 (f7e971b0), can close" while state stays Todo (Mon 2025-09-29)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom565_1', 'ZOM-565', 'usr_c77c50cc15c5342d', NULL, 'The endless start screen vfx went in with build #2023 (commit f7e971b0). Claim button glow and the new bar are both live now, can close.', false, '2025-09-29T16:05:00Z', '2025-09-29T16:05:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-29T16:05:00Z' WHERE id = 'ZOM-565';

-- ZOM-543 (In Progress, started_at 2025-09-25T17:44:22Z; description = generic queue-manager spec)
-- deciding: current queue flow enumerated, C&W included (Mon 2025-09-29)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom543_1', 'ZOM-543', 'usr_49b9dfa5208d400d', NULL, 'Queue manager is in progress. Adding panel-order entries as each live-ops feature lands; current flow is level_end, daily_gift, season_pass, tutorial plus Collect and Win.', false, '2025-09-29T18:20:00Z', '2025-09-29T18:20:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-29T18:20:00Z' WHERE id = 'ZOM-543';

-- ZOM-526 (In Progress, started_at 2025-09-17T15:52:10Z; description says "part of the queue manager")
-- deciding: VFX path shipped, C&W trigger in, Season Pass still alongside (Wed 2025-09-24)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom526_1', 'ZOM-526', 'usr_fc22d5941b2aeb5c', NULL, 'Token-to-live-ops travel is in progress. The vfx path is shipped for Quests, Endless and Daily Gift and the Collect and Win trigger is in; finishing it alongside Season Pass.', false, '2025-09-24T17:30:00Z', '2025-09-24T17:30:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-24T17:30:00Z' WHERE id = 'ZOM-526';

-- ZOM-552 (In Progress, started_at 2025-09-18T18:50:36Z; description = event field lists)
-- deciding: redeem events already sending, remaining events being tagged (Fri 2025-09-26)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom552_1', 'ZOM-552', 'usr_bdf01b53c6a92c5e', NULL, 'Season pass redeem events are being sent, the release notes confirm them. Tagging the remaining events from the sheet now.', false, '2025-09-26T15:45:00Z', '2025-09-26T15:45:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-26T15:45:00Z' WHERE id = 'ZOM-552';

-- ZOM-534 (In Progress, started_at 2025-09-15T15:10:32Z; description = player report on prod)
-- deciding: rollover now syncs, one timing edge case being watched (Thu 2025-09-25)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom534_1', 'ZOM-534', 'usr_cd7849ec043ab3da', NULL, 'Quest points rollover now syncs quests-end with the client instead of waiting on a restart. Watching one backend timing edge case on the day boundary.', false, '2025-09-25T16:35:00Z', '2025-09-25T16:35:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-25T16:35:00Z' WHERE id = 'ZOM-534';

-- ZOM-432 (Todo, created 2025-07-23T09:48:01Z; description is a single image link, no text)
-- cohort: natural-reading "still todo" side; artwork actually merged in PR #471 on 2025-09-30 (NOT named here) (Wed 2025-09-24)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom432_1', 'ZOM-432', 'usr_49b9dfa5208d400d', NULL, 'Daily gift artwork still needs the frame. Card back and gift box are done, the frame is the last piece on my side.', false, '2025-09-24T16:10:00Z', '2025-09-24T16:10:00Z', 1);
-- role: distractor (natural-reading / superseded side)
UPDATE linear.linear_issues SET updated_at = '2025-09-24T16:10:00Z' WHERE id = 'ZOM-432';

-- ZOM-78 (Backlog, description NULL - stays NULL; the only carrier of "reuse this ticket")
-- deciding: calendar ticket reuse + sheet link ask (Tue 2025-09-30)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom78_1', 'ZOM-78', 'usr_175c0d7bc72ed244', NULL, 'Let us use this ticket for the ZM3D beta live-ops calendar instead of opening a new one. Link the sheet here when it is ready.', false, '2025-09-30T18:15:00Z', '2025-09-30T18:15:00Z', 1);
-- role: deciding
UPDATE linear.linear_issues SET updated_at = '2025-09-30T18:15:00Z' WHERE id = 'ZOM-78';

-- ZOM-465 (In Progress, started_at 2025-09-23T14:16:25Z; description already strikes "Idle Icon Animation")
-- cohort: "every event icon animates" side, deliberately silent on Collect & Win (Fri 2025-09-26)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom465_1', 'ZOM-465', 'usr_c77c50cc15c5342d', NULL, 'Idle icon animations for the event icons are done and in the animated-icons PRs, so every event icon animates at idle now.', false, '2025-09-26T18:10:00Z', '2025-09-26T18:10:00Z', 1);
-- role: distractor (natural-reading / superseded side)
UPDATE linear.linear_issues SET updated_at = '2025-09-26T18:10:00Z' WHERE id = 'ZOM-465';

-- ============================================================================
-- BLOCK 2 - linear.linear_comments : certify-absence cohort (12 rows)
-- Each note is a routine progress / review / analytics-in-flight line for its own issue.
-- None names a player-facing calendar hold, a still-to-do the calendar must act on, or a deciding fact.
-- ============================================================================

-- ZOM-344 (Todo, created 2025-07-03T12:28:16Z; quest UI box animation spec)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom344_1', 'ZOM-344', 'usr_c77c50cc15c5342d', NULL, 'Quest box open and close animation reuses the endless chest curve and reads well on the hub. Art side is signed off on my end.', false, '2025-09-16T16:20:00Z', '2025-09-16T16:20:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-16T16:20:00Z' WHERE id = 'ZOM-344';

-- ZOM-387 (Todo, created 2025-07-15T06:26:50Z, updated 2025-07-27T20:46:47Z; giant analytics ticket)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom387_1', 'ZOM-387', 'usr_4e13bd40cc73d0fc', NULL, 'Working down the event list from the sheet tab by tab. The three events we already had are unchanged, everything new is additive.', false, '2025-09-11T17:05:00Z', '2025-09-11T17:05:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-11T17:05:00Z' WHERE id = 'ZOM-387';

-- ZOM-442 (In Validation, started_at 2025-07-30T18:02:11Z; trophy reward redeem instrumentation)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom442_1', 'ZOM-442', 'usr_bdf01b53c6a92c5e', NULL, 'Trophy reward redeem fires with the super properties attached, and the validation query against the sheet comes back clean.', false, '2025-09-19T15:10:00Z', '2025-09-19T15:10:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-19T15:10:00Z' WHERE id = 'ZOM-442';

-- ZOM-471 (Todo, created 2025-08-13T18:01:16Z; red dot icon for players not in Plague Race)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom471_1', 'ZOM-471', 'usr_caafeec2804b3a67', NULL, 'Red dot asset is ready and wired to the Plague Race state check, it only shows while the player is outside a race.', false, '2025-09-17T16:45:00Z', '2025-09-17T16:45:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-17T16:45:00Z' WHERE id = 'ZOM-471';

-- ZOM-504 (Backlog, created 2025-08-25T12:54:47Z, updated 2025-09-15T15:10:41Z; persistent objects in endless)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom504_1', 'ZOM-504', 'usr_65c76e0b87aa7e9b', NULL, 'Tried to reproduce across a long endless session. Saw it once, and the object clears on the next throw. Visual only, no board state affected.', false, '2025-09-22T15:30:00Z', '2025-09-22T15:30:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-22T15:30:00Z' WHERE id = 'ZOM-504';

-- ZOM-517 (Backlog, created 2025-09-03T22:22:22Z; monster loses enrage during item refill)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom517_1', 'ZOM-517', 'usr_Robert', NULL, 'Enrage state is reapplied after an item refill when the refill flag is on. Could not get the monster to lose it while walking in the test board.', false, '2025-09-18T14:50:00Z', '2025-09-18T14:50:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-18T14:50:00Z' WHERE id = 'ZOM-517';

-- ZOM-521 (In Progress, started_at 2025-09-17T15:50:49Z; master VFX checklist)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom521_1', 'ZOM-521', 'usr_49b9dfa5208d400d', NULL, 'Master VFX checklist is down to the last two items, both polish on existing effects. Everything the live-ops side asked for is in.', false, '2025-09-26T17:25:00Z', '2025-09-26T17:25:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-26T17:25:00Z' WHERE id = 'ZOM-521';

-- ZOM-542 (Regression, created 2025-09-14T22:59:17Z; home screen + victory score for game modes)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom542_1', 'ZOM-542', 'usr_caafeec2804b3a67', NULL, 'Home screen and victory score layouts are in for endless and boss arena. Regression pass on the mode switch looks clean.', false, '2025-09-22T18:40:00Z', '2025-09-22T18:40:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-22T18:40:00Z' WHERE id = 'ZOM-542';

-- ZOM-544 (In Progress, started_at 2025-09-22T13:41:02Z; Google/Apple login, assignee is the EMPLOYEE_0032 placeholder - not used as author)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom544_1', 'ZOM-544', 'usr_65c76e0b87aa7e9b', NULL, 'Google Play and Apple sign-in framework is being built on the account layer first, so there is no visible change until the settings panel is ready for it.', false, '2025-09-29T15:35:00Z', '2025-09-29T15:35:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-29T15:35:00Z' WHERE id = 'ZOM-544';

-- ZOM-546 (Todo, created 2025-09-15T18:39:28Z; refill algorithm spawns fewer items over time)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom546_1', 'ZOM-546', 'usr_4e13bd40cc73d0fc', NULL, 'Refill counts hold level across a long endless run here, the board refills the same amount at the 40th refill as at the second.', false, '2025-09-24T14:05:00Z', '2025-09-24T14:05:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-24T14:05:00Z' WHERE id = 'ZOM-546';

-- ZOM-549 (In Validation, started_at 2025-09-22T13:40:39Z; new analytics fields, EMPLOYEE_0032 assignee not used as author)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom549_1', 'ZOM-549', 'usr_65c76e0b87aa7e9b', NULL, 'The new left_level and endless_left fields are in the payloads and the validation query returns them per the sheet.', false, '2025-09-26T16:50:00Z', '2025-09-26T16:50:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-26T16:50:00Z' WHERE id = 'ZOM-549';

-- ZOM-566 (Todo, created 2025-09-30T16:26:02Z - comment instant must be later on the same weekday)
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES ('cmt_zom566_1', 'ZOM-566', 'usr_4e13bd40cc73d0fc', NULL, 'Collect and Win event list is mapped to the sheet, the first events are landing in the pipeline ahead of the beta.', false, '2025-09-30T19:40:00Z', '2025-09-30T19:40:00Z', 1);
-- role: certify-absence
UPDATE linear.linear_issues SET updated_at = '2025-09-30T19:40:00Z' WHERE id = 'ZOM-566';

-- ============================================================================
-- BLOCK 3 - trello.trello_actions : Brian's quests-card comment (1 row)
-- id first-8-hex 68dac820 = 1759168544 = 2025-09-29T17:55:44Z (== date). Prefix 68dac820 has 0 hits
-- in the synth-cut trello export, so no collision. Card 6851a724601a61857a1b202f, board 6851a6569f3bf818760632ab,
-- list 6851a6608b76856437112e45 ("Jun 30th"). Member d1cd0fef645a6c978ae1f068 = brian.foster (verified).
-- INT-21 (Trello -> Slack) does not exist in synth-cut integrations.json: NO companion row anywhere.
-- Never write shortLink/shortUrl (NULL on all 803 base cards).
-- ============================================================================
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json) VALUES ('68dac8204f1e9a3b7c2d5e61', 'commentCard', '2025-09-29T17:55:44Z', 'd1cd0fef645a6c978ae1f068', '6851a6569f3bf818760632ab', '6851a724601a61857a1b202f', '{"board":{"id":"6851a6569f3bf818760632ab","name":"ZM ROADMAP","shortLink":"HSqnngwQ"},"card":{"id":"6851a724601a61857a1b202f","idShort":4,"name":"[Feature] Quests and Milestones and Achievements - [PERSON_NAME_0022]","shortLink":"bEsvQPP4"},"idCard":"6851a724601a61857a1b202f","list":{"id":"6851a6608b76856437112e45","name":"Jun 30th"},"text":"Putting the new quest set in with the Mon Oct 13 rollover.","textData":{"emoji":{}}}');

-- ============================================================================
-- BLOCK 4 - trello.trello_cards : badges comments 1 -> 2 + dateLastActivity (base 2025-06-30T16:56:34Z)
-- All 16 badge keys kept in base order; checkItems 2 / checkItemsChecked 0 / description true (desc non-empty)
-- / dueComplete true unchanged. No board/list/checklist/member writes.
-- ============================================================================
UPDATE trello.trello_cards
   SET badges_json = '{"attachments":0,"attachmentsByType":{"trello":{"board":0,"card":0}},"checkItems":2,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":2,"description":true,"due":null,"dueComplete":true,"externalSource":null,"fogbugz":"","lastUpdatedByAi":false,"location":false,"maliciousAttachments":0,"start":null,"votes":0}',
       "dateLastActivity" = '2025-09-29T17:55:44Z'
 WHERE id = '6851a724601a61857a1b202f';
