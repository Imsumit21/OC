# Unread surfaces: where the rev1 pre-check never looked

Run: `06_PreCheck_Trajectory/trajectory.json` (sha256 `f2b7862f…`), bound to rev1 (SQL `d761d9819dfe`). Clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut); manifest `Evals/references/universes/synthcut/universe_manifest.json`.
Source: research subagent `ses_e58b33ec2ffeucZPTBBj2exub4` (its step cap ended before it could write this file; the content below is its reply, kept as reported and re-checked where marked).

## 1. Linear

- From `calls.jsonl`: 39 distinct `linear_list_comments`, 25 distinct `linear_get_issue`, 16 in both, so 47 register tickets touched and **85 untouched**.
- The 85 untouched: NO CALL 79, FIXED 6. By state: Backlog 28, Todo 25, Done 13, In Progress 13, In Validation 3, other 3.
- All 13 untouched Done tickets closed after 2025-09-22T12:30Z. The 6 FIXED among them (ZOM-434, 503, 506, 557, 558, 561) are settled by Vincent's Sep 30 23:20Z #zombie-bugs post. Linear comments after `completed_at` fail `base_check` (learnings §50, §57), so a Done ticket can't carry a new Linear comment.
- `linear_get_issue` returns no comments (re-checked on the ZOM-571 result: its keys end at `stateHistory`).
- `linear_list_issues` returns `updatedAt` newest-first by default (event 63: ZOM-580 at 22:50Z on top). A seeded comment that bumps `updated_at` to Sep 30 or Oct 1 lands at the top of that list. That is how the run's comment reads tracked the commented tickets: 33 of the 38 (ledger part 1).

## 2. Slack

- Read or searched: #builds C05433XK267, #zombie-bugs C08R27X0EAH, #zombie-ops C08R6BF4ENN (plus thread 1759261800.335275), D079SNE2TL4 (from ts 1759150000), D0770ET1HV2 (from ts 1759200000), the D07GMT8NVM2 thread, and #zombie-prs C093LEZGF6J (metadata only). 11 search queries in all.
- `slack_search_public_and_private` returns DM messages and thread replies: the `-in:#builds after:1759257000` results included D0770ET1HV2/1759267800.858041 and D07GMT8NVM2 replies.
- After 2025-09-30T18:30Z, Vincent's channels hold 86 messages, 66 of them outside #builds. The tool's `total_count` was 66, and the run's two pages of 50 covered all of them. **No new post-candidate Slack message can hide.**
- Channels Vincent is in but never opened, with message counts for Sep 22–Oct 1: D07GJJBFHA5 434, zombie-design 294, D06UPGF5PQV 90, D070FDB7GM8 77, zombie-match3d 69, D05RXP6P69E 69, zm-animations 66, zm-collect-win 60, FC:Bug Checklist 47, FC:Collect&Win 45, D05QQ7YQTND 43, D06UFE81RF0 38, zombie-art 34.

## 3. GitHub

- The run used `list_pull_requests` (match3d, match3d-backend), `list_commits` (match3d, since Sep 22) and `list_releases`. It never read a PR's comments, reviews or review comments.
- 53 match3d / match3d-backend PRs were created or updated Sep 15–30, with 54 PR comments, 52 reviews and 186 review comments. Nearly all are by the CodeRabbit bot. The human authors are Arthur (9 reviews), Owen Baker, Oliver Brooks and Calvin Price. Brian, Vincent and Leonard never author GitHub records.
- match3d PR events are copied to Slack #zombie-prs (C093LEZGF6J) by the GitHub app (INT-01; `base_check` MIRROR_CHANNELS). **match3d-backend has no Slack copy.**

## 4. Confluence, Drive, Gmail, Calendar, Trello

- Confluence has 12 page comments on 10 pages, all from Mar–Jul 2025, written by Douglas, Arthur, Robert and three others; none by Vincent or Brian. `confluence_get_page` doesn't return comments.
- Drive: the only shared doc the run didn't open is f_5ae4332fb6927f84b3afdc (the Jul 27 decoy).
- Gmail: the run's only search was `after:2025/09/29` (complete at 5 of 5, ledger part 2). The older mailbox is unverified.
- Calendar: never read (K7 `evt_81e6dc4dbfd331f1a6a317` NOT-READ).
- Trello: `trello_get_board_actions` was passed a card id as `since`, so the board-wide comment sweep was broken. Comments on other cards stay unread. Whether `trello_search "#135"` matches "135" without the `#` is unverified.

## 5. Ranked carriers (off this run's path, precedented, reachable by an ordinary call)

| Rank | Carrier | Precedent | Reached by | Fairness |
|---|---|---|---|---|
| 1 | Inline review comment on a match3d-backend PR, under an APPROVED review with an empty body | Arthur reviews; Douglas L1 lands 5/6, 5/6, 6/6 | `github_list_pull_request_review_comments` on the fix PR | Fair: proving a fix is live is the rule's own test; no Slack copy |
| 2 | Linear comment on an open register ticket whose title doesn't look like a live bug, dated before Sep 29 (sits mid-list) | Vincent and Brian notes throughout the SQL | `linear_list_comments` per register ticket | Fair if the ticket's own text plus the comment admit one call |
| 3 | Slack DM thread reply under an older parent (D0770ET1HV2 before Sep 30 02:40Z) naming the ticket key | Brian–Vincent DM, 1,376 messages | `slack_search` on the key, or a thread read | Fair: the person and the item are named; it's the persona's own DM |
| 4 | Trello comment on a card other than 68d1eb90bef538c7c5c5599d | Leonard's card comments | `trello_get_comments` on that card | High leak risk (search on "#135"); low priority |
| Unfair | The stale July doc; Confluence comments (no QA authorship, pointer cost); any Linear comment on a Done ticket after it closed; D07GJJBFHA5 (author can't be resolved); Slack after 18:30Z (fully swept); Trash; attachment-only | — | — | — |
