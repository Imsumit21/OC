# R-C — Carriers, ids, identities, integrations (synth-cut, clock 2025-10-01 00:00 PT)

The build session wrote this from the R-C worker's final report: the worker ran out of steps after gathering the facts
and before writing them. Locators unchanged. §7 lookups the worker did not run are re-run by the build session (marked
BUILD).

## 1 · Carriers, companions, integrations

- **Slack** message `id` = `sha256(channel_id + "|" + ts)[:32]` (confirmed on C0880U9751A, C08R8CHB0QL, D05GU6L0XFH,
  D05SD5QLG94, parents and replies). `thread_ts` exported; no `thread_parent_id`. Parent counters on a new reply:
  `reply_count`, `reply_users_count`, `latest_reply` (example C093LEZGF6J ts 1759180973.545069: rc 16, lru 1, lr
  1759247478.371389). `text_fts` is generated — never INSERT it.
- **Gmail**: thread id `julia.lawson@harmonygames.co/<19-digit>`; message id `julia.lawson@harmonygames.co/<RFC Message-ID>`;
  `internal_date_ms` = `date`; labelIds INBOX / IMPORTANT / Label_b19fb8d1b3 / CATEGORY_PERSONAL; `X-GM-THRID` carries the
  19-digit thread. Julia: 253 threads / 304 messages, last 2025-09-17; thread files also use the alias `jlawson@`.
- **GCal**: `evt_` + 22 hex; `ical_uid` hex + `@hg4`; one row per attendee calendar with `self:true` on the owner copy.
  Julia's calendar `julia.lawson@harmonygames.co`, time zone **Europe/Istanbul**.
- **Drive** `d_`/`f_` + 22 hex; Docs/Sheets/Slides id = `drive_files.id`; `owners_json=[owner]`; `content_path` =
  `<owner_email>/<path>`; a Google Doc needs a non-empty `docs_documents.body_text`.
- **Trello**: 24-hex ObjectId (first 8 hex = timestamp); comment action `data_json` = board/card/list/text;
  `badges.comments` must equal the card's commentCard count; bump `dateLastActivity`.
- **Linear**: `ZOM-<n>`, `id = identifier`; the comments table has **0 base rows**; timestamps exactly
  `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json` NOT NULL on issues.
- **GitHub**: a conversation comment `#c_N` needs a `#ev_N` `commented` timeline event (884/884 in base); bump the PR
  `updated_at`. **Caution:** on match3d#470 the `#c_N` suffix collides with `pull_request_commits` ids `#c_0…#c_5`
  (382 of 630 PRs overlap) — use `#c_6` or record the overlap.
- **Integrations**: INT-01 GitHub → `#zombie-prs` C093LEZGF6J for match3d (window ends 2025-09-30T22:33:40Z); INT-11 GCal →
  invitation mails; INT-12 GitHub → Gmail svc_0248; INT-13 Drive → Slack DMs; INT-04 Linear → Slack ("commented on"
  notification only); **INT-21: no Trello ↔ Slack integration**. Linear comments have no mirror of their own text.

## 2 · Identities (all `active_sep_2025_quiet_in_oct`)

| Person | Slack | GitHub | Linear | Trello | Contacts |
|---|---|---|---|---|---|
| Frederick Stone | EMPLOYEE_0008_SLACK_ID | PERSON_2314_GITHUB_USERNAME (shown "Ryan") | usr_175c0d7bc72ed244 | 4b4a68fc0fec0b254e4f9d8e | 175c0d7bc72ed244b944cb90 |
| Robert | EMPLOYEE_0016_SLACK_ID | EMPLOYEE_0016_GITHUB_USERNAME | usr_Robert | 3d06b73654d0c8940792514c | 5f647df33ba6e92fbd56b05b |
| Brian Foster | EMPLOYEE_0026_SLACK_ID | PERSON_0180_GITHUB_USERNAME | usr_fc22d5941b2aeb5c | d1cd0fef645a6c978ae1f068 | fc22d5941b2aeb5c03ad32fa |
| Owen Baker | EMPLOYEE_0021_SLACK_ID | PERSON_5877_GITHUB_USERNAME | usr_4e13bd40cc73d0fc | 919ee44a0d5157b7839f66a8 | 4e13bd40cc73d0fc76f87c7d |
| Douglas | EMPLOYEE_0031_SLACK_ID | PERSON_5760_GITHUB_USERNAME | usr_cd7849ec043ab3da | 1c0688ee1d9093f5b978c1db | cd7849ec043ab3da107f8c03 |
| Vincent Parker | EMPLOYEE_0012_SLACK_ID | EMPLOYEE_0012_GITHUB_USERNAME | usr_65c76e0b87aa7e9b | 864e381ee6c844b2a3a7eaf8 | 65c76e0b87aa7e9b84d1df22 |
| Oliver Brooks | EMPLOYEE_0003_SLACK_ID | EMPLOYEE_0003_GITHUB_USERNAME | usr_bdf01b53c6a92c5e | 12c4a9dcd2d37a25a8d3b557 | bdf01b53c6a92c5e167c658c |
| Leonard Hayes | EMPLOYEE_0038_SLACK_ID | none | usr_63fffeb4fab5233e | PERSON_6094_TRELLO_USER_ID | 63fffeb4fab5233ed5bb73bf |
| Martin Walsh | EMPLOYEE_0033_SLACK_ID | none | usr_51f5f16d46e8cf55 | ba9cc333cefad99228d6757d | 51f5f16d46e8cf55f5ee337b |
| Arthur Blake | EMPLOYEE_0025_SLACK_ID | EMPLOYEE_0025_GITHUB_USERNAME | usr_cc3e90160f490686 | 2162c1ba310341bf318f48b7 | cc3e90160f49068603998654 |
| Julia Lawson | EMPLOYEE_0005_SLACK_ID | PERSON_0005_GITHUB_USERNAME | usr_8140f09bf9f1b94c | 793af7ca6940bf18eb516c75 | 8140f09bf9f1b94cb8ee2dd7 |

Collisions involving them (`entity.py collisions`): `martin` (Martin Walsh / Martin Lewis), `baker` (Owen / Thomas
Baker), `brooks` (Oliver / Lauren Brooks), `lawson` (Julia / Peter Lawson) and the `jlawson@` alias files. Emails are
`<first>[.<last>]@harmonygames.co`.

## 3 · GCal

Events start as late as 2026-01-14, but `created`/`updated` are never after 2025-10-01T00:02:44Z; 24 future-start rows
exist (e.g. `evt_fd2fd7c06e83d9862197d7`, start 2026-01-14, created 2025-09-17). Precedent: a plan event after the seed
bound has start/end after the clock and created/updated before it. Clean multi-copy example: "Engineering Focused
Weekly Planning" uid `b3af6175e2173521cafdd9b32bb3abde@hg4` (12 attendees, 12 copies, `self` moving, identical
created/updated, `sequence` 0–11); Julia's copy `evt_b76bc8baaef3e4a38bbb03`.

## 4 · Gmail

Inbound example `jlawson@harmonygames.co_1773610146653213588.json` ("Canceled event with note", from Leonard, cc empty,
Message-ID `<calendar-47c09d94-…@google.com>`); GitHub PR mail example `_1839183246678864981` (to SVC_3649, cc Julia +
SVC_0613, `in_reply_to` `<…/pull/349@github.com>`).

## 5 · Trello

ZM ROADMAP `6851a6569f3bf818760632ab`; outside list `6851a674975da1fe76e70d93` ("BETA: Oct 10" in earlier reads; the
worker reports a "BETA: Sep 30" name — BUILD re-checks before citing): Jun 30th (14 cards), July 18 (9), July 30 (5),
Oct 21 (8), Jun 18th (5), Jul 24 (7), Backlog (12). **Axe Arena card `6851a7a6c31a93809acded72`** (idShort 9, list Oct
21). Only 12 ZM commentCards in base, all by `PERSON_6095_TRELLO_USER_ID`; example action `685982a91718c11e81a0f1bd`.

## 6 · GitHub match3d#470

"Collect And Win minor bugs fixes", merged 2025-09-30T15:51:15Z. Conversation comments: `#c_1` (CodeRabbit) only;
reviews `#rev_1…#rev_9`; review comments `#rc_1…#rc_9`; timeline `#ev_1…#ev_8` (`#ev_1` commented, `#ev_7` merged,
`#ev_8` closed). #zombie-prs mirror shape: `<https://…/pull/470#issuecomment-<id>|Comment> on pull request by
<https://github.com/owen.baker|owen.baker>`, fallback `[harmonygames-Games/match3d] Comment on #470`, threaded under the
PR's parent post (C093LEZGF6J), bot `SLACK_BOT_0004_SLACK_ID`. Julia is not a member of #zombie-prs (12 members):
`can-see` UNVERIFIED — the mirror is a companion, never evidence.

## 7 · Collision checks

Linear ZOM max = 566 → **ZOM-567** is the next free identifier; base `comments` empty, max issue `created_at`
2025-09-30T16:26:02Z. Drive/Docs/Slides/Sheets title lookups and `#470#c_N`: BUILD re-run (below, when done).
