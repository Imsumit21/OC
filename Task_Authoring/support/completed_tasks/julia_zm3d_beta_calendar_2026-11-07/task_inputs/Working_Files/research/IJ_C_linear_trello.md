# IJ-C — LINEAR / TRELLO exact SQL contract (and contacts, unused)

Clock 2025-10-01 00:00 PT (07:00Z) · seed bound `2025-10-01T00:00:00Z` · synth-cut · persona Julia Lawson
(`usr_8140f09bf9f1b94c`, Trello `793af7ca6940bf18eb516c75`). Read-only research; no SQL executed.
Columns from `Task_Authoring/references/universe_schema_live.json` (144-table live export). Base rows from
`Task_Authoring/task_inputsS/Working_Files/research/raw/{linear.json,trello.json,trello_cards.json,trello_lists.json}`
and the live rowcounts (`linear_comments` = 0, `trello_actions` = 5,252, `trello_cards` = 803).

Status: COMPLETE (partial only where flagged "content-stage decision").

---

## 1. linear_comments

### 1.1 Columns — every one NOT NULL except `parent_id`, `sequence`; **no column has a default**

| # | column | type | NULL | note |
|---|---|---|---|---|
| 1 | `id` | varchar(64) | NO | format: see 1.2 |
| 2 | `issue_id` | varchar(64) | NO | = the **issue id**, i.e. the identifier string `'ZOM-429'` (base `linear_issues.id` == `identifier`; `sql_lint` enforces that identity) — **not** the Linear UUID (`linear_issues.uuid` is NULL on every base row) |
| 3 | `author_id` | varchar(64) | NO | must exist in `linear_users` (`hg_injection_lint` `ACTOR_REFS['linear.linear_comments'] = (('author_id','linear',False),)`) |
| 4 | `parent_id` | varchar(64) | YES | NULL = root comment. If set, must be an existing **comment** id on the same issue (base has no threaded Linear comments) |
| 5 | `body` | text | NO | markdown; single-quote literal, `'` → `''`; UTF-8 fine |
| 6 | `is_edited` | bool | NO | literal `false` (TRUE would need a post-hoc edit reason) |
| 7 | `created_at` | varchar(50) | NO | **exactly** `YYYY-MM-DDTHH:MM:SSZ` — 100 % of base Linear stamps are `…Z`, no fractional seconds, no offset |
| 8 | `updated_at` | varchar(50) | NO | same format; == `created_at` for a never-edited comment |
| 9 | `sequence` | int4 | YES | ordinal within the issue; use `1` for the first comment (the exemplar `task_inputsH` used `NULL` and rendered fine — both are lint-clean). Never duplicate a value within one issue |

No generated column, no `*_fts` column, no PK collision risk (0 base rows).

### 1.2 The id format — base has **0 comment rows**, so there is no base id to copy

- `linear_comments` ≈ 0 rows in **both** universes (`references/universe_rowcounts_live.json`:
  `{"table_name":"linear_comments","approx_rows":0}`; both `.../Services_Data/linear/data.json` `comments` = `[]`).
  The `08_Injection_Schema_Guideline` line "copy an existing id from data.json, under comments" is
  **unsatisfiable** for this table in either universe — record that in the dossier rather than inventing a
  "base" example.
- No pattern is enforced anywhere: the live schema is a bare `varchar(64)`; `Task_Authoring/tools/sql_lint.py`
  `ID_SHAPES` has entries for `trello.*` and (via `linear_issues` logic) `linear id = identifier`, and **no
  entry for `linear_comments`**; `hg_injection_lint` only checks the `author_id` actor reference.
- The platform's Linear ids are **human keys, not UUIDs**: `linear_issues.id` is `'ZOM-429'` (enforced by
  `sql_lint`: "base: id = identifier"), issue URLs are `https://linear.app/harmonygames-games/issue/ZOM-548/…`,
  and `linear_users` already carries symbolic ids in base (`usr_Robert`, `usr_Lucas`, `usr_Victor Barnes`).
- **Therefore keep the design's ids verbatim**: `cmt_zom429_1`, `cmt_zom78_1`, … (≤ 64 chars, unique).
  Precedent that already shipped: `task_inputsH/01_Universe_Inject.sql` seeded `cmt_zom567_1`, `cmt_zom513_1`,
  `cmt_zom514_1`, and its dossier records the Opus pre-check confirming `linear_list_comments` **returns**
  `cmt_zom514_1` on ZOM-514. Do **not** mint a 36-char UUID: it would be the only UUID-shaped Linear id in the
  universe and it would break the `cmt_zom*` pointers in `01_Hardness_Manifest.draft.json` (lines 352, 565–573,
  711, 947, 969) and `01_Scenario_Design.md` §8, §14, §15.
- 15 ids total: the 14 live-ops issues + `cmt_zom78_1`. All are free (no rows to collide with).

### 1.3 The 14 live-ops issues — verbatim current state (drives the `updated_at` bump)

| issue | state_id | started_at | created_at | current updated_at | seeded comment id |
|---|---|---|---|---|---|
| ZOM-344 | Todo | NULL | 2025-07-03T12:28:16Z | 2025-07-03T12:28:16Z | `cmt_zom344_1` |
| ZOM-429 | Backlog | NULL | 2025-07-22T15:14:49Z | 2025-09-22T14:51:23Z | `cmt_zom429_1` |
| ZOM-432 | Todo | NULL | 2025-07-23T09:48:01Z | 2025-07-23T09:48:01Z | `cmt_zom432_1` |
| ZOM-465 | In Progress | 2025-09-23T14:16:25Z | 2025-08-11T14:48:37Z | 2025-09-23T14:16:25Z | `cmt_zom465_1` |
| ZOM-471 | Todo | NULL | 2025-08-13T18:01:16Z | 2025-08-13T18:01:16Z | `cmt_zom471_1` |
| ZOM-504 | Backlog | NULL | 2025-08-25T12:54:47Z | 2025-09-15T15:10:41Z | `cmt_zom504_1` |
| ZOM-517 | Backlog | NULL | 2025-09-03T22:22:22Z | 2025-09-03T22:22:22Z | `cmt_zom517_1` |
| ZOM-526 | In Progress | 2025-09-17T15:52:10Z | 2025-09-02T19:48:54Z | 2025-09-17T15:52:10Z | `cmt_zom526_1` |
| ZOM-534 | In Progress | 2025-09-15T15:10:32Z | 2025-09-08T00:34:41Z | 2025-09-15T15:10:32Z | `cmt_zom534_1` |
| ZOM-549 | In Validation | 2025-09-22T13:40:39Z | 2025-09-17T02:31:59Z | 2025-09-22T13:40:39Z | `cmt_zom549_1` |
| ZOM-552 | In Progress | 2025-09-18T18:50:36Z | 2025-09-17T19:54:58Z | 2025-09-18T18:50:36Z | `cmt_zom552_1` |
| ZOM-556 | Todo | NULL | 2025-09-22T14:44:06Z | 2025-09-22T14:44:06Z | `cmt_zom556_1` |
| ZOM-565 | Todo | NULL | 2025-09-25T13:46:04Z | 2025-09-25T13:46:04Z | `cmt_zom565_1` |
| ZOM-566 | Todo | NULL | 2025-09-30T16:26:02Z | 2025-09-30T16:26:02Z | `cmt_zom566_1` |
| ZOM-78 | Backlog | NULL | 2025-04-26T09:21:59Z | 2025-04-26T09:21:59Z | `cmt_zom78_1` |

All 14 are `is_archived = false`, `canceled_at/completed_at/archived_at = NULL`. Only ZOM-429 (Backlog,
`time_in_status_minutes` 207643), ZOM-504 and ZOM-517 sit in Backlog; the state is deliberately **not** changed
by the note (stale state is the trap).

### 1.4 Lifecycle rules the seeded rows must satisfy (`sql_lint.linear_lifecycle`, 3,165 base exceptions of ~3.6 k)

- `Done` ⇔ `completed_at` set; `Canceled|Duplicate` ⇔ `canceled_at` set and **no** `completed_at`;
  `Todo|Backlog|Triage` ⇒ **no** `started_at` / `completed_at` / `canceled_at` at all;
  `completed_at` is only legal on `Done` / `In Review`.
- `created_at ≤ started_at ≤ completed_at ≤ updated_at` (and `created_at ≤ canceled_at ≤ updated_at`).
- **A comment never changes `state_id` here.** In particular do **not** "fix" ZOM-565 to Done because its note
  says it shipped, and do not add `completed_at` to it: the Todo + shipped-note pair *is* the designed
  state/lifecycle hazard (L03).
- `updated_at` bump: real Linear touches the parent issue's `updated_at` when a comment lands, so bump it to the
  comment's own instant. This is lint-clean and makes the note findable through `orderBy updatedAt` without
  leaking the fact. The exemplar bumped `updated_at` only when it also changed `state_id`; both forms pass, but
  **bump**, because every other ZOM issue's `updated_at` equals its `created_at`, and a comment dated after a
  months-old `updated_at` would be a visible inconsistency to a careful reader.
- Constraint on the chosen instant `T` (content stage): `T ≥ issue.started_at ?? issue.created_at`,
  `T ≥ issue.updated_at` **only if** you keep the bump monotonic in spirit — strictly required:
  `T ≤ 2025-10-01T00:00:00Z`; `T` must be ≥ the base event the note reacts to (ZOM-429's note reacts to the
  Sep 22 leaderboard thread, so `T` = 2025-09-23 per the design); avoid Sat/Sun UTC (`sql_lint` warns
  "business message on a weekend"). New `updated_at = T`.

### 1.5 Copy-ready statements

```sql
-- one row per issue; 15 rows. is_edited false, sequence 1, parent_id NULL, updated_at = created_at.
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence)
VALUES ('cmt_zom429_1', 'ZOM-429', 'usr_cd7849ec043ab3da', NULL,
        '<note body: owner decision, one paragraph, no placeholder tokens>', false,
        '2025-09-23T16:12:00Z', '2025-09-23T16:12:00Z', 1);
-- … 14 more, one per issue in 1.3, then:
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence)
VALUES ('cmt_zom78_1', 'ZOM-78', 'usr_175c0d7bc72ed244', NULL,
        '<reuse-and-link note>', false,
        '2025-09-30T<hh>:<mm>:<ss>Z', '2025-09-30T<hh>:<mm>:<ss>Z', 1);

-- one per issue, same instant as that issue's comment:
UPDATE linear.linear_issues SET updated_at = '2025-09-23T16:12:00Z' WHERE id = 'ZOM-429';
```

`16:12:00Z` is a placeholder **inside the design's 2025-09-23 date** (Tue, 09:12 PT) — the content stage fixes
the exact minute from `by_universe/synthcut/conventions.json` hours for Douglas. `linear_create_comment` /
`linear_list_comments(issueId)` both key on the identifier string.

---

## 2. linear_users — real author ids (41 base rows; never INSERT one)

`linear_users` is fully populated in the universe (41 rows, all `is_active = true`). No seed needs a new user;
`author_id` just has to be one of these. NOT NULL columns if a user ever had to be added: `id, email, name,
is_active, is_admin, is_guest, created_at, updated_at`.

| person | linear_users.id | role in this task |
|---|---|---|
| **Douglas** | `usr_cd7849ec043ab3da` | ZOM-429 owner note (§3 of the design: "the ZOM-429 owner note"); also assignee of ZOM-78 / ZOM-429 / ZOM-534 |
| **Frederick Stone** | `usr_175c0d7bc72ed244` | `cmt_zom78_1` (he asks for the calendar link in the ask DM); his `updated_at` is `2025-10-01T06:59:59Z` (clock − 1 s) |
| Vincent Parker | `usr_65c76e0b87aa7e9b` | QA/prod reporter; creator of ZOM-429, ZOM-432, ZOM-504, ZOM-517, ZOM-549, ZOM-552, ZOM-556 |
| Calvin Price | `usr_49b9dfa5208d400d` | assignee of ZOM-432 / ZOM-556 / ZOM-565 |
| Marcus Bennett | `usr_c77c50cc15c5342d` | assignee of ZOM-344 / ZOM-465 (VFX), creator of ZOM-565 |
| Samuel Turner | `usr_caafeec2804b3a67` | assignee of ZOM-471 |
| Oliver Brooks | `usr_bdf01b53c6a92c5e` | assignee of ZOM-552 |
| Owen Baker | `usr_4e13bd40cc73d0fc` | assignee of ZOM-566 |
| Brian Foster | `usr_fc22d5941b2aeb5c` | not needed on Linear (he owns the Trello comment + the Gmail handoff) |
| Julia Lawson | `usr_8140f09bf9f1b94c` | creator of ZOM-78; the persona — do **not** author a note she "reads" unless the scenario says she wrote it |
| Arthur Blake | `usr_cc3e90160f490686` | GitHub-only (inline review notes), not Linear |
| Robert | `usr_Robert` | symbolic id, valid (ART/VFX threads) |
| Leonard Hayes | `usr_63fffeb4fab5233e` | the player report quoted in ZOM-534 |
| Martin Walsh | `usr_51f5f16d46e8cf55` | base #zombie-art, unchanged |

**Trap:** `usr_EMPLOYEE_0032` is a real `linear_users` row (assignee of ZOM-504/517/549) and would **pass** the
actor check, but it renders as `EMPLOYEE_0032_NAME`. Never use a placeholder account as a note author.

Author assignment is a content-stage call; the only two the design pins are ZOM-429 (Douglas) and ZOM-78
(Frederick, "Frederick asks for the link there"). Every other note should be authored by the issue's spec-owner
in the table above, not by a random name.

---

## 3. Fact-leak guard — the comment must be the only carrier of the per-record finding

`linear_list_issues` returns `title` **and** `description` in bulk (`Ask_Carriers` §6b: items carry
`description` with `descriptionTruncated`/`descriptionLength`, and **never** comments). `linear_get_issue` also
returns the description. So any finding written into the description or title is a bulk-readable fact_leak;
`linear_list_comments` is the per-issue surface. Checked against the real rows:

**ZOM-429** — `title`: *"Leaderboard next session doesn't start without killing the app"*.
`description` (339 chars, abridged): *"When the weekly leaderboard is ended, it doesn't start the new one or let
me claim my rewards. … It can only proceed to next leaderboard if the app is killed and when I can claim my
rewards if any. … This wouldn't be the biggest issue considering it happens only once a week."*
→ the player's own words already mention "the app is killed", i.e. the *reporter's* workaround is in the
description. That is **not** a leak of the deciding fact, and must not be extended: the description says nothing
about owner, priority, urgency, or the re-test. **Do not edit this description.** The note carries the owner
decision ("restart gets players in; not urgent") and the decisive supersession (Vincent's 2025-09-30 prod
re-test) stays in Slack `C0880U9751A/1759265412.481907`. If the note merely restated the description's
"kill the app" it would add nothing — write the *decision*, not the symptom.

**ZOM-565** — `title`: *"Endless Horde Start Screen Vfx"*. `description` (1,542 chars): Marcus's VFX spec —
prefab `EndlessScreenBar`, dotween autoplay only when the Claim button is available, "I've let everthing on my
branch Marcus/EndlessMode_Vfx", "the glow behind its on all and the bar its the old bar, not mine". Term scan:
contains `claim`, `work` (as "start working"), and **no** `ship|shipped|merge|merged|main|done|release`.
→ the "this shipped" finding exists **only** in the seeded comment. Confirmed clean.

**ZOM-556** — `title`: *"When the daily gift is skipped, it doesn't reset to 0."*; `description` (132 chars):
*"If I didn't log in for a day, the bottom part should reset to day 1. However, it doesn't reset right now."*
→ contains none of `ship|merge|done|claim|restart|work`; the "claiming works / not reproducible" finding is
comment-only. Confirmed clean.

**ZOM-78** — `title`: *"Event Calendar For Zombie Match 3D"*; `description`: **NULL** (and stays NULL or at most
a neutral line). → the only carrier of "this is the calendar ticket, reuse it, here is the link" is
`cmt_zom78_1`. Do not create a second calendar ticket and do not put "reuse this one" into the title.

**ZOM-432 / ZOM-471 / ZOM-534 / ZOM-344 / ZOM-465 / ZOM-504 / ZOM-517 / ZOM-526 / ZOM-549 / ZOM-552 / ZOM-566**
— their descriptions are the original reports (player text, VFX specs, analytics field lists); none states a
delivery status, an owner decision or a hold. No edit needed; no edit allowed.

Rules to record for `/create-injection`: (a) never UPDATE `description` or `title` of these 15 issues;
(b) never put a status/owner/hold sentence in `linear_issues.*`; (c) the description edit form
(`UPDATE linear.linear_issues SET description = …, updated_at = …`) is for *other* tasks only;
(d) `linear_show_data` is still `[U]` — the pre-check must confirm it does not return `linear_comments`
(the `task_inputsH` dossier lists exactly that check for `linear_list_comments`).

---

## 4. trello actions + cards + badges

### 4.1 `trello.trello_actions` — 7 columns, all plain `varchar` except `date timestamptz`

`id`! , `type`! , `date`! (timestamptz), `"idMemberCreator"`, `"idBoard"`, `"idCard"`, `data_json` (text).
No `memberCreator` column exists — the audit field is the **`idMemberCreator` column**; the nested
`memberCreator` object does not appear in this platform's snapshot (base rows carry only the id column plus the
board/card/list snapshot in `data_json`). `id` is 24-hex with the first 8 hex = the record's Unix seconds
(`sql_lint` errors if it is after the clock, before 2011, or more than 86 400 s from `date`).

### 4.2 The seeded action

| field | value |
|---|---|
| `id` | `68dac8204f1e9a3b7c2d5e61` — first 8 hex `68dac820` = 1 759 168 544 = **2025-09-29T17:55:44Z**, exactly the `date` |
| `type` | `commentCard` |
| `date` | `2025-09-29T17:55:44Z` |
| `idMemberCreator` | `d1cd0fef645a6c978ae1f068` (Trello member `brian.foster`, fullName "Brian Foster", initials BF, `https://trello.com/brian.foster`) |
| `idBoard` | `6851a6569f3bf818760632ab` (ZM ROADMAP) |
| `idCard` | `6851a724601a61857a1b202f` |
| `data_json` | see 4.5 |

`memberCreator` = the same member (`d1cd0fef645a6c978ae1f068`) if a shape ever needs the object; the column set
in the live schema has no such column, so nothing to insert.

### 4.3 The card — verbatim base row (as stored; `idMembers`/`idLabels`/`badges` are the text columns)

```json
{"id":"6851a724601a61857a1b202f","name":"[Feature] Quests and Milestones and Achievements - [PERSON_NAME_0022]","idBoard":"6851a6569f3bf818760632ab","idList":"6851a6608b76856437112e45","desc":"Live ops feature","pos":140737488333824.0,"closed":false,"due":null,"dueComplete":true,"idMembers_json":"[]","idLabels_json":"[]","idShort":4,"shortLink":null,"shortUrl":null,"url":"https://PERSON_6092_TRELLO_USERNAME.com/c/bEsvQPP4/4-feature-quests-and-milestones-and-achievements-oliver.brooks","dateLastActivity":"2025-06-30T16:56:34Z","cover_json":null,"badges_json":"{...see 4.4...}","start":null,"idAttachmentCover":null}
```
Export-level detail: `closed` is `false` in the export (`closed: false`), `badges`/`idMembers`/`idLabels`/`cover`
are nested objects in `data.json` and become `badges_json` / `idMembers_json` / `idLabels_json` / `cover_json`
text on INSERT; `shortLink` and `shortUrl` are **NULL on all 803 base cards** (the 8-char code survives only in
`url` and in the action snapshots), so never INSERT or UPDATE `shortLink`.
List: `6851a6608b76856437112e45` = **"Jun 30th"** (`pos` 16384.0, board ZM ROADMAP).
Board: ZM ROADMAP `shortLink` `HSqnngwQ`, `dateLastActivity` **2025-09-30T17:09:07Z**.

### 4.4 `badges_json` — full base shape, never `'{}'` (16 keys, base order)

```json
{"attachments":0,"attachmentsByType":{"trello":{"board":0,"card":0}},"checkItems":2,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":1,"description":true,"due":null,"dueComplete":true,"externalSource":null,"fogbugz":"","lastUpdatedByAi":false,"location":false,"maliciousAttachments":0,"start":null,"votes":0}
```
After Brian's comment: **`comments` 1 → 2**; `checkItems` stays `2`, `checkItemsChecked` stays `0` — the card has
one base checklist `6855f2e861b7b62fa876ab04` "Estimate" (created by action `6855f2e861b7b62fa876ab13`
2025-06-20) with items `…ab05` "Provide engineering estimate" and `…ab06` "Set Priority", both `incomplete`;
`description` stays `true`
(the `desc` "Live ops feature" is non-empty) — the `description` bool must keep matching the real `desc`;
`dueComplete` stays `true` (card `dueComplete` is `true` while `due` is `null` — copy it, do not "fix" it).

### 4.5 Verbatim base `commentCard` on the same card (the row to mirror)

```json
{"id":"68598651c63b35d952130929","type":"commentCard","date":"2025-06-23T16:52:33Z","idMemberCreator":"PERSON_6095_TRELLO_USER_ID","idBoard":"6851a6569f3bf818760632ab","idCard":"6851a724601a61857a1b202f","data":{"board":{"id":"6851a6569f3bf818760632ab","name":"ZM ROADMAP","shortLink":"HSqnngwQ"},"card":{"id":"6851a724601a61857a1b202f","idShort":4,"name":"[Feature] Quests and Milestones and Achievements","shortLink":"bEsvQPP4"},"idCard":"6851a724601a61857a1b202f","list":{"id":"6851a6608b76856437112e45","name":"Jun 30th"},"text":"If everything goes well 2-3 days.\n\nSo likely 4-5 days.","textData":{"emoji":{}}}}
```
`data_json` = exactly that object as a JSON **string** (keys `board{id,name,shortLink}`, `card{id,idShort,name,shortLink}`,
`idCard`, `list{id,name}`, `text`, `textData{emoji:{}}`). The `_id` variants appear only on the 2014 Welcome-Board
template rows. The base snapshot's `card.name` predates the rename (it lacks the `- [PERSON_NAME_0022]` suffix);
the *current* card name carries it. **Mirror the current name** (what `trello_get_card` returns) — the only
authored copy in `data_json` is `text`; do not put a `[PERSON_NAME_*]` token into `text`. (Fallback, also
lint-clean: use the rename-era name as the base action did — record whichever is chosen.)

### 4.6 Copy-ready statements

```sql
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json)
VALUES ('68dac8204f1e9a3b7c2d5e61', 'commentCard', '2025-09-29T17:55:44Z', 'd1cd0fef645a6c978ae1f068',
        '6851a6569f3bf818760632ab', '6851a724601a61857a1b202f',
        '{"board":{"id":"6851a6569f3bf818760632ab","name":"ZM ROADMAP","shortLink":"HSqnngwQ"},"card":{"id":"6851a724601a61857a1b202f","idShort":4,"name":"<current card name>","shortLink":"bEsvQPP4"},"idCard":"6851a724601a61857a1b202f","list":{"id":"6851a6608b76856437112e45","name":"Jun 30th"},"text":"<the comment>","textData":{"emoji":{}}}');

UPDATE trello.trello_cards
   SET badges_json = '{"attachments":0,"attachmentsByType":{"trello":{"board":0,"card":0}},"checkItems":2,"checkItemsChecked":0,"checkItemsEarliestDue":null,"comments":2,"description":true,"due":null,"dueComplete":true,"externalSource":null,"fogbugz":"","lastUpdatedByAi":false,"location":false,"maliciousAttachments":0,"start":null,"votes":0}',
       "dateLastActivity" = '2025-09-29T17:55:44Z'
 WHERE id = '6851a724601a61857a1b202f';
```

No `trello.trello_boards` UPDATE: the board's `dateLastActivity` is `2025-09-30T17:09:07Z`, **later** than the
seeded action, so bumping it would move it backwards (a chronologies error a reader can see). No checklist /
check-item write. No `trello_lists` write (the list is not renamed; the card does not move).

### 4.7 INT-21 — confirmed NONE

`references/universe_kb/by_universe/synthcut/integrations.json`: **INT-21 Trello → Slack does not exist**; there
is no companion row for this comment (design §16: "trello → Slack: INT-21 — NO integration exists; no companion
for the quests-card comment"). Do not seed a Slack mirror of Brian's Trello text anywhere. Contrast INT-04
(Linear → Slack) which produces a generic "commented on" DM notice with **no** comment text — an optional
companion for `cmt_zom*`, never evidence; and INT-03 (linear[bot] PR comment) is a different direction and not
triggered by a comment insert.

---

## 5. Collision + reach

**Action id.** `68dac8204f1e9a3b7c2d5e61` is free: the trello export contains **no** occurrence of the prefix
`68dac820` (0 hits across 5,252 actions / 803 cards / 54 checklists / 161 check items), and the full literal
appears nowhere in `Universe_SynthCut/.../Services_Data/trello/`. It is well-formed for `sql_lint`
(24 lowercase hex; first 8 hex = 2025-09-29T17:55:44Z = its own `date`; not after the clock; > 2011).
R-C §7 records the collision sweep for the Linear keys (`ZOM` max 566 → `ZOM-567` free, base comments empty,
max issue `created_at` 2025-09-30T16:26:02Z); this re-cite adds the Trello half that §7 left as "BUILD re-run".

**Linear comment ids.** 15 ids, all free — the table has 0 rows in both universes, so `cmt_zom{344,429,432,465,
471,504,517,526,534,549,552,556,565,566,78}_1` cannot collide with anything. They also cannot collide with
`linear_issues.id` (identifier form `ZOM-<n>`) or `linear_attachments.id` (24-hex, 1,955 rows, keyed to the
issue through `issue_identifier`).

**Card/board/list ids** already exist and are only UPDATEd, never duplicated. Both people exist in
`trello_members` — Julia `793af7ca6940bf18eb516c75` (username `julia.lawson`, initials JL) and Brian
`d1cd0fef645a6c978ae1f068` (username `brian.foster`, initials BF), 42 members total — so no member row is added.
The board row carries **no** `memberIds_json` in the export (NULL) and the card's `"idMembers_json"` is `[]`:
leave both alone (adding Brian/Julia to the card would change `idMembers_json` and is not needed for reach).

**Reach — both services are UNSCOPED.** `Evals/references/persona/acl.md` (QC Rating Form V12; design §0 line 21:
"UNSCOPED (always visible): contacts, github, trello, linear, snowflake, confluence") — Linear and Trello are
**never** filtered for Julia: any issue/card/comment she can name, she can read, with no membership or sharing
step, and only Gmail/Slack/GCal/Drive/Docs/Sheets/Slides are scoped. Consequences for the design:
`linear_list_comments(issueId='ZOM-429')` and `trello_get_comments(cardId='6851a724601a61857a1b202f')` always
return the seeded rows; findability, not permission, is the only gate. Two caveats to record:
(i) `trello_get_card_actions(cardId, filter='commentCard')` **and** `trello_get_board_actions(boardId,
filter='commentCard')` also return the seeded action — the Trello comment is *not* a per-record-only surface (one
board-level call reaches it), which is why the design treats it as a trap (T12), not a cohort surface;
(ii) `linear_show_data` `[U]` could be a bulk shortcut to issues — the pre-check must confirm it does not render
comment bodies (otherwise the 14-note cohort surface collapses to 1 call).

**Contacts — NOT USED.** The design seeds nothing in `contacts` (no row, no criterion, no authority). If a later
revision needs one: `contacts.contacts` NOT NULL = `contact_id, first_name, last_name` (rest nullable, incl.
`description`, which has 0 base rows = no rendering precedent); `contacts.contact_groups` NOT NULL = `group_id,
name`; `contacts.contact_group_members` NOT NULL = `membership_id, group_id, contact_id`. Julia's contact id is
`8140f09bf9f1b94cb8ee2dd7`.
