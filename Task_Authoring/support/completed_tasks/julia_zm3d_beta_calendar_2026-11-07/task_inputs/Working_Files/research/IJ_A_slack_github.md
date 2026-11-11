# IJ-A — Slack + GitHub injection shapes (synth-cut)

Build persisted this from the IJ-A worker's final report (worker ran out of steps before writing). Verbatim base
sample rows are re-pulled by build when drafting the SQL (sources noted). All ids verified against the live schema
and base.

## 1 · slack_messages (24 cols)

- **NOT NULL:** `id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json,
  files_json, attachments_json, created_at, metadata_json`.
- **Nullable:** `user_id, thread_parent_id, thread_ts_legacy, latest_reply, subtype, edited_ts, edited_user, bot_id,
  client_msg_id, permalink`. **`text_fts` is GENERATED ALWAYS — never write it.**
- **id derivation:** `sha256('<channel_id>|<ts>').hexdigest()[:32]` (reproduced on 5 base rows, e.g.
  `C08R8CHB0QL|1757614800.772141` → `65ba253c289c2cee538d9b94b5406655`). Computed seeded ids:
  - `D05SD5QLG94/1759263600.418207` → **`8b090dec472117f4598b9ad84318272e`** (Frederick ask DM root)
  - `C08R8CHB0QL/1758213600.552913` → **`2e75e232f5e6206273411a8305ac5d01`** (Robert approval reply, #zombie-art thread)
  - `D05GU6L0XFH/1759270200.638114` → **`58d06bd55ea4129eaadb726291967d5a`** (Robert withdrawal reply, his DM)
  - `C0880U9751A/1759265412.481907` → **`fa3eee2c614b0741aeb240275f86abf7`** (Vincent re-test ROOT, #zombie-match3d)
- **Thread encoding (base convention):** a root has `thread_ts == ts` in the export; in the DB `thread_parent_id` =
  the parent **message id** (32-hex), `thread_ts_legacy` = the parent **ts**. Children carry
  `thread_parent_id`/`thread_ts_legacy` and `reply_count 0`. On a seeded reply, UPDATE the parent's `reply_count`,
  `reply_users_count`, `latest_reply`. (Our ROOT in #zombie-match3d has no parent; our two thread replies —
  #zombie-art approval under base root `C08R8CHB0QL/1758121809.236839`, and the DM withdrawal under base parent
  `D05GU6L0XFH/1759248350.473459` — need their parents' counters bumped.)
- Membership (not needed here — Julia already a member of every channel used): `members_json` + `num_members` together.
- Base sample rows to mirror (re-pull when drafting): root `C0880U9751A/1757020057.613329` + reply
  `1757020105.526219`.

## 2 · INT-01 companion mirror (#zombie-prs C093LEZGF6J; Julia NOT a member → non-load-bearing by ACL)

Seed one bot message per seeded match3d PR comment/review (playbook S4 Mirror rule), in `C093LEZGF6J`, at the same
time, each **≤ 2025-09-30T22:33:40Z** (INT-01 match3d window close). Shape (base example `C093LEZGF6J/1759180981.072539`):
- bot `SLACK_BOT_0004_SLACK_ID`, `text ""`, `subtype bot_message`.
- `attachments_json[0]`: `color 24292f`; `fallback "[harmonygames-Games/match3d] Comment on #N"`; `pretext
  "<https://github.com/harmonygames-Games/match3d/pull/N#discussion_r<id>|Comment> on pull request by
  <https://github.com/<login>|<login>>"` (conversation comments use `#issuecomment-<id>`); `title`, `footer`,
  `footer_icon`, `id 1`, `mrkdwn_in ["text"]`, `text` = the comment body verbatim; outer `ts` = integer epoch.
- Round-2 §16: seed the faithful mirror (integration parity). Non-load-bearing because Julia is not in `#zombie-prs`.

## 3 · github tables

- `github_pull_requests` (30 cols), `github_reviews` (8 cols, **NOT NULL `seq` int**), `github_review_comments`
  (17 cols, **NOT NULL `seq`**), `github_pr_comments` (6), `github_timeline_events` (6), `github_users`.
- Suffix scheme per PR: review `#rev_N`, inline review comment `#rc_N`, conversation comment `#c_N`, timeline `#ev_N`.
  Every seeded PR comment needs a matching `commented` timeline event `#ev_N`; bump the PR `updated_at`.
- Seeded rows (re-pull match3d#470/#370/#438/#454/#471 base rows to mirror columns):
  - inline review_comment fields: `diff_hunk, path, position, author_login, author_name, body, created_at, seq`.
  - review fields: `state, body, submitted_at, author_login, author_name, seq`.
  - conversation pr_comment: `author_login, author_name, body, created_at`.
  - timeline `commented` event: `event, author_login, created_at, seq`.

## 4 · Collision checks (all free; via hg.py search lookup)

| PR | base max suffixes | planned seeds (FREE) |
|---|---|---|
| #470 | rev 1-9, rc 1-9, c 1, ev 1-8 | `#rc_10` (Arthur inline, under empty APPROVED `#rev_9`), `#ev_9` |
| #370 | no reviews/rc, c 1, ev 1-4 | `#rev_1`, `#rc_1` (Arthur post-merge: vial sprites, Claire), `#ev_5` |
| #438 | rev 1-3, rc 1-73, c 1, ev 1-8 | `#rev_4`, `#rc_74` (Arthur post-merge: premium strip → Nov range, Oliver), `#ev_9` |
| #454 | rev 1, c 1, no rc, ev 1-5 | `#c_4` (Marcus conversation: C&W icon animation), `#ev_6` |
| #471 | c 1-2, rev 1-2, rc 1-2, ev 1-7 | `#c_18` (Samuel: daily-gift frame shipped), `#ev_8` |

All planned Slack `(channel, ts)` confirmed absent from base. (`#c_2`/`#c_3` on some PRs collide with
`pull_request_commits` ids — a different table; our suffixes sidestep them.)

## 5 · Identities (GitHub login → rendered name)

| Person | Slack | GitHub login | note |
|---|---|---|---|
| Frederick Stone | EMPLOYEE_0008_SLACK_ID | PERSON_2314_GITHUB_USERNAME | renders **"Ryan"** — never cross-attribute |
| Robert | EMPLOYEE_0016_SLACK_ID | EMPLOYEE_0016_GITHUB_USERNAME | |
| Vincent Parker | EMPLOYEE_0012_SLACK_ID | EMPLOYEE_0012_GITHUB_USERNAME | |
| Arthur Blake | EMPLOYEE_0025_SLACK_ID | EMPLOYEE_0025_GITHUB_USERNAME | #470 inline, #370/#438 post-merge |
| Marcus Bennett | — | **PERSON_0396_GITHUB_USERNAME** | NOT PERSON_0394 (= Martin Lewis); #454 note |
| Samuel Turner | — | **EMPLOYEE_0004_GITHUB_USERNAME** | #471 note |
| Owen Baker | EMPLOYEE_0021_SLACK_ID | PERSON_5877_GITHUB_USERNAME | |
| Julia Lawson | EMPLOYEE_0005_SLACK_ID | PERSON_0005_GITHUB_USERNAME | NOT a member of #zombie-prs (12 members) |
