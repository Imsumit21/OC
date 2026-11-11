# /injection report: Injection data integrity (Eval 0)

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` (new and changed statements NEW; byte-identical statements REUSED from the revision-3 review, see §8) |
| Mode | Chat review, attempt 6aeed825ea17fab7311d0896, static audit (SQL never executed) |
| Review time | 2026-11-07 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16; archive sha256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c`) |
| Universe manifest | `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| Input | `Evals/task_inputs/01_Universe_Inject.sql` (uploaded as `01_Universe_Inject (6).sql`), 173,249 bytes, sha256 `6c143945fe3e3aae8326363b4ac7df7ac3e4349a78668bfb9d8acc1644afd033`, input revision 6 |
| Previous version | revision 3, sha256 `2175e44f…6df27` (PASS). Diff: SQL line 2 changed (thread counters on Marcus's Sep 25 zm-animations post) and a new line 3 (his thread reply); every other statement is byte-identical, shifted down one line |
| Lint | `hg_injection_lint.py` injection-lint-v1 |
| Schema snapshot | `Evals/references/schema/injection.json` sha256 `31dcb2b43feca8e5c7cb67f37973f819c9b9774f12f8b15cb7da89ecd74c5151` (unverified snapshot) |
| Shared guide | WORKFLOW.md sha256 `ee4cd8e1cc291c3b733bfd53907f073f3c8dcbfbbec4723b978a1e4a504fcd5d`; scoring.json sha256 `c14873e614cdcda5190db761e6fd0922111991308dace2e1ccd3de8ad789e5bc` |
| Assignment (context only) | Claire Morgan, Art Lead; Design / Marketing and GTM / Authoring; long-horizon; easy |

## 2. Input and authority issues

- None blocking. The SQL was saved and read in full before any base search: 239 statements (234 INSERT rows, 5 UPDATEs) plus 13 `--` comments.
- The SQL comments state what each record is for (for example "Robert's Sep 17 thread reply…", "base ART-792's status-duration counter… cleared like ART-774 / ART-790"). None mention tool-call counts, pass rate or gates, and none address a grader.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; record hash, base manifest, review version | NEW, done (manifest and schema snapshot hashes unchanged from revision 3) |
| Run lint; resolve every flag | NEW, done on revision 6 (239 statements; 0 FAIL, 0 CHECK, 1 INFO resolved) |
| Inventory every statement and record | NEW, done (239/239, ledger in §7) |
| Check A: references, collisions, ID contracts, readable Drive files, one account per person | PASS: rows 2–3 NEW; other rows REUSED (byte-identical statements, unchanged manifest) |
| Check B: SQL structure and schema rules | PASS: full-file lint NEW; rows 2–3 NEW; others REUSED (snapshot advisories ADV-3) |
| Check C: dates, relationships, consistency, grader-facing text | PASS: rows 2–3 NEW, including a re-check of every injected record that names ART-795/797/805/823 or the three re-recorded creatives; others REUSED (advisories ADV-1, ADV-2, ADV-4) |

## 4. Lint flags and resolutions

| Flag | Severity | Resolution |
|---|---|---|
| `unparsed` L171 `gdrive.drive_files` `content_path`: 13 media files (11 PNG store screenshots `f_a72a7fd18327ed34fa2ac6` … `f_fcfdf5502a68b1797fa0db`, 2 MP4 cuts `f_dc5cf9e4250d433c1511ec`, `f_bcd34f98925e3f20d846ce`) carry metadata only | INFO | Allowed. Eval 0 Check A says media files carry metadata only, as in the base, and fail only when the task needs their content. These files' role (they exist, they're named, they sit in the Halloween folders) comes from their metadata. What is *in* the Marcus cuts (July capture, old background) is stated in Slack text (L5, L10), not left to the video bytes. |

No FAIL or CHECK flags (`future_date`, `id_contract`, `drive_unreadable`, `identities`, `grader_language`, `padding_comment`, `generated_column`, `text_time_format`, `missing_required`, `json_shape` all clean).

## 5. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | All actors, parents and targets resolve; no key collides in the complete local base; ID contracts held; native Docs/Sheets/Slides have readable content rows; no second account for anyone. Details §5.1. |
| B — SQL structure and supported schema rules | PASS | All 234 INSERT rows have matching column/value counts; every NOT NULL column without a default is supplied non-NULL; all `*_json` values parse, with the snapshot's array/object shape; no generated column (`text_fts`, `body_text_fts`) is written; Linear dates use `YYYY-MM-DDTHH:MM:SSZ`; `state_history_json='[]'` on every new issue. Advisory ADV-3: 10 column names not in the unverified snapshot, all set to NULL. |
| C — Dates, relationships and consistency | PASS | Every event timestamp ≤ 2025-10-01T07:00Z; Slack `ts` = `created_at` on all 15 messages; Gmail `internal_date` = `date` = header `Date`; replies follow parents; thread counters match; every cross-record fact checked against base agrees (builds, dates, people, threads). No grader-facing text. Advisories ADV-1, ADV-2, ADV-4 are not demonstrated defects. Details §5.3. |

### 5.1 Check A detail

**Actors and identities**
- Slack users `EMPLOYEE_0002/0005/0008/0009/0016/0033/0038_SLACK_ID` = Marcus Bennett, Julia Lawson, Frederick Stone, Claire Morgan, Robert, Martin Walsh, Leonard Hayes (`slack/users.json`, none deleted). Each poster is a member of the channel they post in: `C08R8CHB0QL` zombie-art (23), `C09ATAJ220H` zm-animations (Marcus a member), `C05KNDCHAAG` company-internal, `C06DJBJL798` zombie_marketing, `C0880U9751A` zombie-match3d. `D05V2N6PZNU` is the base Claire–Marcus DM (members include 0002/0009; base posters 0002: 3,184, 0009: 2,902).
- Linear `usr_175c0d7bc72ed244` = frederick.stone@, `usr_c77c50cc15c5342d` = marcus.bennett@ (`linear/data.json /users`); both are in `team_ART` (`tmem_team_ART_…`). `team_ART` exists.
- Drive/Docs/Sheets/Slides owners and shares (leonard.hayes, martin.walsh, marcus.bennett, frederick.stone, arthur.blake, robert, claire.morgan) are all in `gdrive /drive_users`. Gmail mailboxes for all five recipients exist in `gmail/users.json`. All 7 calendar IDs exist in `gcal /calendars`.
- Trello `PERSON_6094_TRELLO_USER_ID` = Leonard Hayes and `4b4a68fc0fec0b254e4f9d8e` = Frederick Stone (`trello /members`).
- New contact `PERSON_6311` / `PERSON_6311_EMAIL` ("Founder, KayKit") follows the base anonymised-contact shape (compare base `PERSON_0242`, empty last_name). `PERSON_6311` appears nowhere in the base: complete searches of contacts (170 records), Gmail, Slack, Trello, Linear, GCal and GDrive found 0 matches. So it is not a second account for an existing person.

**Parents and targets**
- Drive parents `d_63fffeb4fab5233ed5bb73`, `d_175c0d7bc72ed244b944cb`, `d_cc3e90160f490686039986`, `d_9f7ba94f7526d54d8482ba` are the root folders of Leonard, Frederick, Arthur and Robert, each matching the owner of the injected file. The Store/UA masters subfolders are injected first (L168–170) and used afterwards.
- Slack UPDATE L23 target `9025d428af1f551a20e303c3acbc545b` (Martin, Sep 17 15:10Z, "*Halloween theme* for an app icon or an event", reply_count 0) exists. The reply L22 is Robert, who is @-mentioned in it.
- Slack UPDATE L26 target `cd68a603aef386cb7ad0f7cf9a363f04` (Robert, Sep 30 05:50Z, Unity bot/fake installs, @Frederick) exists with reply_count 4, reply_users_count 2 (0008, 0016) and latest_reply `1759248267.162909`. Frederick's L25 reply makes 5; reply users stay 2 (he has already replied); latest_reply moves to L25's ts.
- New thread (rows 2–3): L3 is Marcus's reply (`EMPLOYEE_0002_SLACK_ID`) to his own L2 post in `C09ATAJ220H` (he is a channel member). `thread_parent_id` = L2's id and `thread_ts_legacy` = L2's ts `1758823964.738872`; L2 now carries `thread_ts_legacy` = its own ts, `reply_count` 1, `reply_users_count` 1 (one reply author) and `latest_reply` = L3's ts `1758825697.426919`. This matches the base export's thread shape (base `C09ATAJ220H/2025-09.json`: parent `d2b9bdc2…` has `thread_ts` = own ts, reply `60166a0e…` has `thread_ts` = parent ts, `reply_users_count` counts reply authors) and the script's own L22/L23 pair. The reply names `ART-795`, `ART-805`, `ART-797` and `ART-823`, all injected earlier (L33, L56, L38, L98).
- Linear UPDATE L166 target `ART-792` exists (Team Epic, created 2025-08-26T18:57:06Z, `time_in_status_minutes` 246277, which runs to Feb 2026, past the clock: SC-22). Setting it to NULL matches base ART-774/ART-790 (both NULL).
- Trello: board `6851a6569f3bf818760632ab` "ZM ROADMAP", list `6851a677e090018224fb8c7f` "Oct 21" and list `6876878e769a212c7eb16c36` "Jul 24" exist. Card `68768a1501ae552dbee94b8a` (#45 Marketing Video Refresh) exists, with base badges comments 0, description false, dueComplete true and dateLastActivity 2025-08-20T16:38:52Z; the UPDATE keeps every badge field and sets comments 1 (one injected comment) and a later activity time. The board's base dateLastActivity is 2025-09-30T17:09:07Z; the UPDATE moves it to the later 23:20Z.
- Linear comments all point to issues injected earlier in the script (ART-793…854).

**Collision coverage (complete scans, scope = local base + this SQL)**

| Keys | Scope | Result |
|---|---|---|
| 15 Slack message ids | 14 unchanged ids: revision-3 complete scan of `messages/*.json` (4,840 files, 610,468 records, scan_complete; REUSED, unchanged manifest). New id `6aecfa673deb24040a0d83058b4848d8` and ts `1758825697.426919`: NEW complete raw substring scan of all 4,840 `messages/*.json` files (grep, control id `d2b9bdc2…` found as expected; the helper `lookup` aborted with "Source, manifest or helper changed during operation", complete=false, so it is not relied on) plus a direct read of `C09ATAJ220H/2025-09.json` (203 records) | 0 matches; new id appears once in the SQL; ts `1758825697.426919` and `1758823964.738872` absent from the channel's Sep file |
| 62 Linear ids/identifiers ART-793…ART-854 | `linear/data.json /issues`: 3,687 issues (ART max 792) | 0 matches |
| 75 Linear comment ids `cmt_art…` | base `/comments` is empty (0); unique within the SQL | 0 matches |
| 19 Drive ids | `gdrive/data.json /drive_files`: 53,631 | 0 matches |
| Spreadsheet / document / presentation ids (and `drive_file_id`) | gsheets 356, gdocs 595, gslides 132 records | 0 matches |
| 4 slide page + 8 element object ids | all 4,540 base slide object ids | 0 matches |
| 16 Gmail message ids | `threads/*.json /messages`: 81,404 files, 95,164 messages, scan_complete | 0 matches |
| 16 Gmail thread ids (full id and numeric THRID) | all 81,404 thread files (top-level `id`) | 0 matches |
| 7 GCal event ids + ical_uid `83766dff…@hg4` | `gcal /events`: 10,395 | 0 matches (one ical_uid shared across attendee copies, as in 802 base meetings) |
| Trello card id, idShort 80, 3 action ids | 803 cards (board max idShort 79), 5,252 actions | 0 matches; ids' embedded timestamps match their dates |
| Contact id `6b350edd259a8b4499a9e625` | 170 contacts | 0 matches |

**ID contracts and readability**
- Gmail `history_id` is NULL on all 32 Gmail rows (contract: NULL or decimal string). Drive `content_path` is NULL on every row (folders, native Google files, media), so the path-format contract doesn't apply.
- The native files are readable: the Doc `f_fdd6d2d2f4a4d2f5b908fb` has a `docs_documents` row with non-empty `body_text`; the Sheet `f_02b1968f5e882366fbb883` has 4 tabs with `grid_json`; the Slides deck `f_5ebf55ad29e815d46243c8` has 4 pages and 8 text elements. Media files: see the lint resolution.

### 5.2 Check B detail

- Structure: the statements parse cleanly (quotes balanced, `''` escapes). All INSERTs are single-row with no ON CONFLICT clause. The 5 UPDATEs each target one primary key.
- NOT NULL (snapshot): no omission and no NULL in a NOT NULL/no-default column across all 17 affected tables (`linear_issues.title/priority/labels_json/links_json/relations_json/is_archived/created_at/updated_at/state_history_json`, `linear_comments.body/is_edited/…`, `slack_messages.reactions_json/files_json/attachments_json/metadata_json/…`, etc.).
- JSON: every `*_json` value is valid JSON with the snapshot shape (`metadata_json='{}'`, Slack arrays `[]`, `start_json/end_json` objects, `attendees_json` array, Trello `data_json`/`badges_json` objects, `grid_json` array of arrays).
- Linear text dates: every value matches `YYYY-MM-DDTHH:MM:SSZ` (lint `text_time_format` clean).
- Provisional snapshot comparison: MATCH for every listed column except the NOT COVERED columns in ADV-3.

### 5.3 Check C detail

**Chronology**
- No event timestamp (created/updated/sent/posted/commented/modified/dateLastActivity/action date) is later than 2025-10-01T07:00Z. The latest is Slack L25 at 2025-09-30T23:42:18Z. The only later values are plan fields: the GCal review on Thu 2025-10-02 16:00–16:30Z (created 2025-09-30T22:10Z) and in-text deadlines.
- Every Slack `ts` equals its `created_at` to the microsecond (new L3: `1758825697.426919` = 2025-09-25T18:41:37.426919Z, 28 min 53 s after its parent L2 at 18:12:44.738872Z). Gmail `internal_date` = `date` = RFC 2822 `Date` header (-0700) on all 16 messages; each id is `<mailbox>/<Message-ID>`; X-GM-THRID matches `thread_id`.
- Linear: created ≤ started ≤ completed = updated on every Done issue. All 75 comments fall between their issue's `created_at` and `updated_at`.
- Event ordering: the Slides deck (09-25 16:10Z) comes before Robert's Slack pointer (16:30Z); Marcus's MP4s (09-29 17:05Z) before his DM reply (17:20Z) and zombie-art post (17:31Z); Martin's PNGs (09-30 15:12Z) before his post (15:20Z); the Trello card (22:00Z) and GCal event (22:10Z) follow Leonard's 22:05Z ask in time; Frederick's changes mail (23:10Z) comes before his Slack Android correction (23:42Z), which says "not the 15th".
- Weekday names all match the 2025 calendar (Fri Sep 12, Mon Sep 29, Thu Oct 2, Fri Oct 10, Sun Oct 12, Wed Oct 15, Thu Oct 16, Fri Oct 17, Sat Oct 18, Wed Oct 22, Fri Oct 31).

**Facts checked against base records**

| Injected claim | Base evidence | Result |
|---|---|---|
| Slides: older than "Android #1452 / iOS 1232 (the zombie swap with the new background, Jul 29)" | `slack/messages/C05433XK267/2025-07.json` /1672 Android #1452 ZombieSwap Success 2025-07-29T20:24Z; /1673 iOS #1232 ZombieSwap 20:24Z; `C0880U9751A/2025-07.json` /903 "iOS build 1232 … zombie swap completed with new background" | Agrees |
| Capture builds/dates: #440 Apr 5, #456/#457 Apr 7, #475 Apr 8, #633 Apr 29, #771 May 28, #852 Jun 5, #1427 Jul 28, #1450 Jul 29, #1529 Aug 4, #1630 Aug 13, #1896 Sep 16, #1935 (exported Sep 23), #1966 (exported Sep 25) | Match3D Android build posts in `C05433XK267`: 2025-04-05, 04-07, 04-07, 04-08, 04-29, 05-28, 06-05, 07-28, 07-29 ("New Background…"), 08-04, 08-13, 09-16, 09-22, 09-24 | Agrees (each export follows its build) |
| "Captured Dec 5, 2024 from the prototype, before the first Match3D build" | First Match3D Android/iOS builds (#1): 2025-01-12 | Agrees |
| ART-809 "Master notes are in Frederick's Aug 13 thread in #zombie_marketing" | `C06DJBJL798/2025-08.json`: Frederick 2025-08-13T19:40Z, 15 replies, "the background music is baked in" | Agrees |
| Trello Sep 26: end card 001 has the old zombie packs, because "Martin's new packs came after Marcus rendered it" (ART-833 from #1529, Aug 4) | #1529 build 2025-08-04T00:39Z; Martin "I did new packs to replace the old ones" `C08R8CHB0QL/2025-08.json` /64 at 2025-08-04T14:04Z | Agrees |
| Gmail Sep 29 23:48Z: "The iOS retention campaigns went back on today" | `C07C2866011` 2025-09-29 22:28Z Leonard asks Frederick to turn iOS Unity retention back on; 22:48Z budget raised from the $1 pause | Agrees |
| Slack L25 builds on Robert's Unity-fraud thread ("Android") | Base thread replies: Frederick 09-30 13:58Z, Robert "Android" 15:21Z, … | Agrees |
| Martin's vacation Oct 6–15 (L7) | Base Martin vacation was Sep 8–12; nothing in base covers October | No conflict |
| Release calendar (Oct 16 cut / Oct 17 submit / Oct 22 live / Nov 6) | No base statement of Q4 submission dates found (Sep Slack searches "Oct 16/17/22", "October 17", "Nov 6": 0) | No conflict |
| Trello: Julia's 4:5 static still runs on iOS UK and "never made it onto the live creatives sheet" | ART-826 julia 4:5 (Unity: iOS UK phone) is missing from both the Unity and Archive tabs | Consistent (deliberate) |
| Slack L2 "re-recorded … couch alpha 50 on #1935, barrel marketing2 4:5 on #1896, balloons alpha 50 (1) on #1966" + new L3 "they replace the april captures on ART-795, ART-805 and ART-797. the couch 16:9 on ART-823 wasnt redone, thats still the apr 7 capture" | ART-795 couch alpha 50 9:16 "Captured from Android #456 on Apr 7" (L34); ART-805 barrel marketing2 4:5 "#633 on Apr 29" (L57); ART-797 balloons alpha 50 (1) 9:16 "#456 on Apr 7" (L39); ART-823 couch alpha 50 16:9 "#456 on Apr 7" (L99). The new exports ART-853 (4:5, #1935, Sep 23), ART-852 (1:1, #1896, Sep 17), ART-854 (16:9, #1966, Sep 25 17:06Z) all predate L2/L3, and builds #1896/#1935/#1966 predate them | Agrees: all three named tickets are April captures, in L2's order; ART-823 is the Apr 7 couch alpha 50 16:9. No injected record dated after L3 (Trello Sep 26/30, Gmail Sep 29/30, Slack Sep 29/30) says these cuts are still the April captures. The sheet's "Live since Apr 7/Apr 29" and the tickets' original capture comments are older, stale context that L3 supersedes; no ticket comment records the replacement (a deliberate correction elsewhere, not a contradiction) |

**Supersession chains (deliberate, coherent)**
- Re-recorded UA cuts: ART-795/805/797 April captures (Linear Sep 8, sheet) → Marcus Sep 25 18:41Z (L3): replaced by the #1935/#1896/#1966 re-recordings; ART-823 explicitly still the Apr 7 capture.
- Halloween ad deadline: Gmail Sep 12 "by Fri Oct 17" → Gmail Sep 30 "by Wed Oct 15" → Slack Sep 30 23:42Z "Android US phone … by Fri Oct 10".
- Campaigns: Sep 12 four campaigns → Sep 29 squirrelfail/mrfluffernot landscape off iOS UK tablet → Sep 30 Android US tablet ends Oct 12.
- Cheer fastcouch: Marcus's Halloween test from the July capture (L4/L10) → Robert: redo from the Sep 16 one (L5) → Marcus agrees (L6), matching the ART-808/816 Sep 16 re-capture comments.

**Grader-facing text:** none. All injected text is in-world (workplace messages, ticket notes, deck copy). No text addresses a solver or grader or describes the test.

## 6. Findings

No demonstrated defects. The advisories below don't change the verdict.

| ID | Record | Observation | Why it isn't a defect | Optional fix |
|---|---|---|---|---|
| ADV-1 | L127–L130 `ART-836…ART-839` (`state_id='Canceled'`) | `canceled_at` is NULL; in base, all 372 Canceled issues have `canceled_at` set (and all 3,058 Done issues have `completed_at`) | Missing timestamp, not a contradictory fact. The pause dates are carried by `updated_at` (Sep 15/19) and the sheet's Archive tab | Set `canceled_at` to each row's `updated_at` (`2025-09-15T17:00:00Z` ×3, `2025-09-19T17:00:00Z`) |
| ADV-2 | Linear "Still running on Unity: iOS UK … (checked Sep 9)" comments (e.g. L29, L36, L43, L71) and sheet "Live since Sep 9" rows | Base private #executives (`C07C2866011`) has Leonard on 2025-09-12 15:05–15:16Z: "we are ready to turn on campaigns … I turned on UK Retention IOS", which suggests iOS UK may have been off on Sep 9. Sep 16: "Both Unity campaigns (phone and tablet)"; Sep 19 mpdm: "Unity retention campaigns IOS UK … the only campaign we are running" | Not a demonstrated contradiction. No base record says when the campaigns went off. Base shows Unity campaigns active in Jun, Jul 30 and Aug 22, and Android Unity traffic on Sep 28. The tension sits only in channels Claire is not in (executives, mpdm), so it isn't on her view of the data | If the task grades Sep 9 serving status, date those checks after Sep 12, or drop "(checked Sep 9)" |
| ADV-3 | INSERT column lists | Columns not in the unverified snapshot (NOT COVERED): `linear_issues.uuid`, `linear_comments.sequence`, `drive_files.drive_id`, `docs_documents.text_style_runs_json`, `slides_pages.notes`, `slides_page_elements.table_json`/`ordinal`, `gcal_events.extras_json`, `trello_cards.start`/`idAttachmentCover`; all set to NULL | Eval 0: a snapshot mismatch alone is advisory. Live compatibility is outside static scope | None required. If a load reports an unknown column, drop these NULL columns from the column lists |
| ADV-4 | L314 Trello comment ("still our best CPI there") | A qualitative CPI claim; Snowflake records Unity CPI as 0 (known data issue SC-11) | No number is asserted, so nothing conflicts. Whether the task depends on Unity CPI belongs to /prompt (base-data-v1) | Keep rubric/OEs off Unity CPI figures from Snowflake |

## 7. Operation ledger (all 239 statements in SQL order)

Base sources: `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/{slack,linear,gdrive,gsheets,gdocs,gslides,gcal,trello,contacts}` and `Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/gmail`. "OK" means the row passed A (refs/collisions), B (structure/schema) and C (dates/consistency) as detailed in §5.

| # | SQL line | Table | Op | Record / target | Detail | Result |
|---|---|---|---|---|---|---|
| 1 | 1 | slack.slack_messages | INSERT | `7bc65781afc70022ccfe703ce0a4688c` | C08R8CHB0QL EMPLOYEE_0016 2025-09-25T16:30 | OK |
| 2 | 2 | slack.slack_messages | INSERT | `2c9fbac7d610f8a1eb138d8d875a15d2` | C09ATAJ220H EMPLOYEE_0002 2025-09-25T18:12; now thread parent (thread_ts_legacy own ts, reply_count 1, reply_users_count 1, latest_reply 1758825697.426919) | OK (NEW) |
| 3 | 3 | slack.slack_messages | INSERT | `6aecfa673deb24040a0d83058b4848d8` | C09ATAJ220H EMPLOYEE_0002 2025-09-25T18:41, reply to row 2 | OK (NEW) |
| 4 | 4 | slack.slack_messages | INSERT | `4c2fdbe41fae4579a928389af8bd163d` | C08R8CHB0QL EMPLOYEE_0002 2025-09-29T17:31 | OK |
| 5 | 5 | slack.slack_messages | INSERT | `258fa1a8b911063c05b51e843cb33975` | C08R8CHB0QL EMPLOYEE_0016 2025-09-30T16:05 | OK |
| 6 | 6 | slack.slack_messages | INSERT | `aba47cfddc303d4db7d51b00b6354e8e` | C08R8CHB0QL EMPLOYEE_0002 2025-09-30T16:21 | OK |
| 7 | 7 | slack.slack_messages | INSERT | `c50f7403ef0b0cdda1d261760cebd86f` | C05KNDCHAAG EMPLOYEE_0033 2025-09-30T14:41 | OK |
| 8 | 8 | slack.slack_messages | INSERT | `a3734776dfe0410d8a5dacaa8987e7bc` | C05KNDCHAAG EMPLOYEE_0038 2025-09-30T23:31 | OK |
| 9 | 9 | slack.slack_messages | INSERT | `c737e6b93220471d68d2286a35c6868a` | D05V2N6PZNU EMPLOYEE_0009 2025-09-26T07:40 | OK |
| 10 | 10 | slack.slack_messages | INSERT | `ca1f5be7ac733cc1ab5a47a7db37c89b` | D05V2N6PZNU EMPLOYEE_0002 2025-09-29T17:20 | OK |
| 11 | 11 | slack.slack_messages | INSERT | `55737ddb68db0ef92a114cc676bbef18` | C08R8CHB0QL EMPLOYEE_0033 2025-09-30T15:20 | OK |
| 12 | 12 | slack.slack_messages | INSERT | `b041f2ed8617697746dec5437e9b5e20` | C08R8CHB0QL EMPLOYEE_0038 2025-09-30T15:47 | OK |
| 13 | 13 | slack.slack_messages | INSERT | `df8626158cd6733c068ca36341eeee35` | C06DJBJL798 EMPLOYEE_0038 2025-09-30T22:05 | OK |
| 14 | 22 | slack.slack_messages | INSERT | `8ce7e9eec2958c799a1aa11e4249cddd` | C08R8CHB0QL EMPLOYEE_0016 2025-09-17T16:52 | OK |
| 15 | 23 | slack.slack_messages | UPDATE | `id = '9025d428af1f551a20e303c3acbc545b'` | thread_ts_legacy = '1758121809.236839', reply_count = 1, reply_users_count = 1, latest_reply = '1758127951.679 | OK |
| 16 | 25 | slack.slack_messages | INSERT | `ca1f761be9c227f410d508ba8a9d324a` | C0880U9751A EMPLOYEE_0008 2025-09-30T23:42 | OK |
| 17 | 26 | slack.slack_messages | UPDATE | `id = 'cd68a603aef386cb7ad0f7cf9a363f04'` | reply_count = 5, latest_reply = '1759275738.984915' | OK |
| 18 | 28 | linear.linear_issues | INSERT | `ART-793` | couch boss 30 (9:16 video); Done | OK |
| 19 | 29 | linear.linear_comments | INSERT | `cmt_art793_1` | ART-793 by usr_175c0d7bc72ed244 2025-09-08T16:01 | OK |
| 20 | 30 | linear.linear_comments | INSERT | `cmt_art793_2` | ART-793 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 21 | 31 | linear.linear_issues | INSERT | `ART-794` | couch alpha 30 (9:16 video); Done | OK |
| 22 | 32 | linear.linear_comments | INSERT | `cmt_art794_1` | ART-794 by usr_175c0d7bc72ed244 2025-09-08T16:02 | OK |
| 23 | 33 | linear.linear_issues | INSERT | `ART-795` | couch alpha 50 (9:16 video); Done | OK |
| 24 | 34 | linear.linear_comments | INSERT | `cmt_art795_1` | ART-795 by usr_175c0d7bc72ed244 2025-09-08T16:03 | OK |
| 25 | 35 | linear.linear_issues | INSERT | `ART-796` | balloons alpha 50 (9:16 video); Done | OK |
| 26 | 36 | linear.linear_comments | INSERT | `cmt_art796_1` | ART-796 by usr_175c0d7bc72ed244 2025-09-08T16:04 | OK |
| 27 | 37 | linear.linear_comments | INSERT | `cmt_art796_2` | ART-796 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 28 | 38 | linear.linear_issues | INSERT | `ART-797` | balloons alpha 50 (1) (9:16 video); Done | OK |
| 29 | 39 | linear.linear_comments | INSERT | `cmt_art797_1` | ART-797 by usr_175c0d7bc72ed244 2025-09-08T16:05 | OK |
| 30 | 40 | linear.linear_issues | INSERT | `ART-798` | barrel alpha 30 (9:16 video); Done | OK |
| 31 | 41 | linear.linear_comments | INSERT | `cmt_art798_1` | ART-798 by usr_175c0d7bc72ed244 2025-09-08T16:06 | OK |
| 32 | 42 | linear.linear_issues | INSERT | `ART-799` | couch marketing2 30s (9:16 video); Done | OK |
| 33 | 43 | linear.linear_comments | INSERT | `cmt_art799_1` | ART-799 by usr_175c0d7bc72ed244 2025-09-08T16:07 | OK |
| 34 | 44 | linear.linear_comments | INSERT | `cmt_art799_2` | ART-799 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 35 | 45 | linear.linear_issues | INSERT | `ART-800` | couch marketing2 endcard (9:16 video); Done | OK |
| 36 | 46 | linear.linear_comments | INSERT | `cmt_art800_1` | ART-800 by usr_175c0d7bc72ed244 2025-09-08T16:08 | OK |
| 37 | 47 | linear.linear_issues | INSERT | `ART-801` | barrel alpha 30 endcard (9:16 video); Done | OK |
| 38 | 48 | linear.linear_comments | INSERT | `cmt_art801_1` | ART-801 by usr_175c0d7bc72ed244 2025-09-08T16:09 | OK |
| 39 | 49 | linear.linear_issues | INSERT | `ART-802` | couch alpha 30 endcard (9:16 video); Done | OK |
| 40 | 50 | linear.linear_comments | INSERT | `cmt_art802_1` | ART-802 by usr_175c0d7bc72ed244 2025-09-08T16:10 | OK |
| 41 | 51 | linear.linear_comments | INSERT | `cmt_art802_2` | ART-802 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 42 | 52 | linear.linear_issues | INSERT | `ART-803` | balloons alpha 50 endcard (9:16 video); Done | OK |
| 43 | 53 | linear.linear_comments | INSERT | `cmt_art803_1` | ART-803 by usr_175c0d7bc72ed244 2025-09-08T16:11 | OK |
| 44 | 54 | linear.linear_issues | INSERT | `ART-804` | balloons marketing2 endcard (9:16 video); Done | OK |
| 45 | 55 | linear.linear_comments | INSERT | `cmt_art804_1` | ART-804 by usr_175c0d7bc72ed244 2025-09-08T16:12 | OK |
| 46 | 56 | linear.linear_issues | INSERT | `ART-805` | barrel marketing2 4:5 (4:5 video); Done | OK |
| 47 | 57 | linear.linear_comments | INSERT | `cmt_art805_1` | ART-805 by usr_175c0d7bc72ed244 2025-09-08T16:13 | OK |
| 48 | 58 | linear.linear_issues | INSERT | `ART-806` | barrel marketing2 16:9 (16:9 video); Done | OK |
| 49 | 59 | linear.linear_comments | INSERT | `cmt_art806_1` | ART-806 by usr_175c0d7bc72ed244 2025-09-08T16:14 | OK |
| 50 | 60 | linear.linear_issues | INSERT | `ART-807` | cheer 30p 9:16 (9:16 video); Done | OK |
| 51 | 61 | linear.linear_comments | INSERT | `cmt_art807_1` | ART-807 by usr_175c0d7bc72ed244 2025-09-08T16:15 | OK |
| 52 | 62 | linear.linear_comments | INSERT | `cmt_art807_2` | ART-807 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 53 | 63 | linear.linear_issues | INSERT | `ART-808` | cheer fastcouch 9:16 (9:16 video); Done | OK |
| 54 | 64 | linear.linear_comments | INSERT | `cmt_art808_1` | ART-808 by usr_175c0d7bc72ed244 2025-09-08T16:16 | OK |
| 55 | 65 | linear.linear_comments | INSERT | `cmt_art808_2` | ART-808 by usr_c77c50cc15c5342d 2025-09-16T16:40 | OK |
| 56 | 66 | linear.linear_issues | INSERT | `ART-809` | marcus.bennett 9:16 (9:16 video); Done | OK |
| 57 | 67 | linear.linear_comments | INSERT | `cmt_art809_1` | ART-809 by usr_175c0d7bc72ed244 2025-09-08T16:17 | OK |
| 58 | 68 | linear.linear_issues | INSERT | `ART-810` | squirrelfail portrait (9:16 video); Done | OK |
| 59 | 69 | linear.linear_comments | INSERT | `cmt_art810_1` | ART-810 by usr_175c0d7bc72ed244 2025-09-08T16:18 | OK |
| 60 | 70 | linear.linear_issues | INSERT | `ART-811` | squirrelfail landscape (16:9 video); Done | OK |
| 61 | 71 | linear.linear_comments | INSERT | `cmt_art811_1` | ART-811 by usr_175c0d7bc72ed244 2025-09-08T16:19 | OK |
| 62 | 72 | linear.linear_comments | INSERT | `cmt_art811_2` | ART-811 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 63 | 73 | linear.linear_issues | INSERT | `ART-812` | mrfluffernot portrait (9:16 video); Done | OK |
| 64 | 74 | linear.linear_comments | INSERT | `cmt_art812_1` | ART-812 by usr_175c0d7bc72ed244 2025-09-08T16:20 | OK |
| 65 | 75 | linear.linear_comments | INSERT | `cmt_art812_2` | ART-812 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 66 | 76 | linear.linear_issues | INSERT | `ART-813` | mrfluffernot landscape (16:9 video); Done | OK |
| 67 | 77 | linear.linear_comments | INSERT | `cmt_art813_1` | ART-813 by usr_175c0d7bc72ed244 2025-09-08T16:21 | OK |
| 68 | 78 | linear.linear_issues | INSERT | `ART-814` | cinematicTutorial Ad 1 (9:16 video); Done | OK |
| 69 | 79 | linear.linear_comments | INSERT | `cmt_art814_1` | ART-814 by usr_175c0d7bc72ed244 2025-09-08T16:22 | OK |
| 70 | 80 | linear.linear_issues | INSERT | `ART-815` | tutorialCinematic portrait (9:16 video); Done | OK |
| 71 | 81 | linear.linear_comments | INSERT | `cmt_art815_1` | ART-815 by usr_175c0d7bc72ed244 2025-09-08T16:23 | OK |
| 72 | 82 | linear.linear_issues | INSERT | `ART-816` | cheer fastcouch 16:9 (16:9 video); Done | OK |
| 73 | 83 | linear.linear_comments | INSERT | `cmt_art816_1` | ART-816 by usr_175c0d7bc72ed244 2025-09-08T16:24 | OK |
| 74 | 84 | linear.linear_comments | INSERT | `cmt_art816_2` | ART-816 by usr_c77c50cc15c5342d 2025-09-16T17:10 | OK |
| 75 | 85 | linear.linear_issues | INSERT | `ART-817` | marcus.bennett 16:9 (16:9 video); Done | OK |
| 76 | 86 | linear.linear_comments | INSERT | `cmt_art817_1` | ART-817 by usr_175c0d7bc72ed244 2025-09-08T16:25 | OK |
| 77 | 87 | linear.linear_comments | INSERT | `cmt_art817_2` | ART-817 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 78 | 88 | linear.linear_issues | INSERT | `ART-818` | marcus.bennett 4:5 (4:5 video); Done | OK |
| 79 | 89 | linear.linear_comments | INSERT | `cmt_art818_1` | ART-818 by usr_175c0d7bc72ed244 2025-09-08T16:26 | OK |
| 80 | 90 | linear.linear_issues | INSERT | `ART-819` | marcus.bennett 1:1 (1:1 video); Done | OK |
| 81 | 91 | linear.linear_comments | INSERT | `cmt_art819_1` | ART-819 by usr_175c0d7bc72ed244 2025-09-08T16:27 | OK |
| 82 | 92 | linear.linear_issues | INSERT | `ART-820` | cheer 30p 16:9 (16:9 video); Done | OK |
| 83 | 93 | linear.linear_comments | INSERT | `cmt_art820_1` | ART-820 by usr_175c0d7bc72ed244 2025-09-08T16:28 | OK |
| 84 | 94 | linear.linear_issues | INSERT | `ART-821` | couch alpha 30 16:9 (16:9 video); Done | OK |
| 85 | 95 | linear.linear_comments | INSERT | `cmt_art821_1` | ART-821 by usr_175c0d7bc72ed244 2025-09-08T16:29 | OK |
| 86 | 96 | linear.linear_issues | INSERT | `ART-822` | balloons alpha 50 16:9 (16:9 video); Done | OK |
| 87 | 97 | linear.linear_comments | INSERT | `cmt_art822_1` | ART-822 by usr_175c0d7bc72ed244 2025-09-08T16:30 | OK |
| 88 | 98 | linear.linear_issues | INSERT | `ART-823` | couch alpha 50 16:9 (16:9 video); Done | OK |
| 89 | 99 | linear.linear_comments | INSERT | `cmt_art823_1` | ART-823 by usr_175c0d7bc72ed244 2025-09-08T16:31 | OK |
| 90 | 100 | linear.linear_issues | INSERT | `ART-824` | barrel alpha 30 endcard 16:9 (16:9 video); Done | OK |
| 91 | 101 | linear.linear_comments | INSERT | `cmt_art824_1` | ART-824 by usr_175c0d7bc72ed244 2025-09-08T16:32 | OK |
| 92 | 102 | linear.linear_issues | INSERT | `ART-825` | julia 1:1 (1:1 static); Done | OK |
| 93 | 103 | linear.linear_comments | INSERT | `cmt_art825_1` | ART-825 by usr_175c0d7bc72ed244 2025-09-08T16:33 | OK |
| 94 | 104 | linear.linear_comments | INSERT | `cmt_art825_2` | ART-825 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 95 | 105 | linear.linear_issues | INSERT | `ART-826` | julia 4:5 (4:5 static); Done | OK |
| 96 | 106 | linear.linear_comments | INSERT | `cmt_art826_1` | ART-826 by usr_175c0d7bc72ed244 2025-09-08T16:34 | OK |
| 97 | 107 | linear.linear_issues | INSERT | `ART-827` | julia 9:16 (9:16 static); Done | OK |
| 98 | 108 | linear.linear_comments | INSERT | `cmt_art827_1` | ART-827 by usr_175c0d7bc72ed244 2025-09-08T16:35 | OK |
| 99 | 109 | linear.linear_issues | INSERT | `ART-828` | julia 16:9 (16:9 static); Done | OK |
| 100 | 110 | linear.linear_comments | INSERT | `cmt_art828_1` | ART-828 by usr_175c0d7bc72ed244 2025-09-08T16:36 | OK |
| 101 | 111 | linear.linear_issues | INSERT | `ART-829` | julia 1:1 android 1080 (1:1 static); Done | OK |
| 102 | 112 | linear.linear_comments | INSERT | `cmt_art829_1` | ART-829 by usr_175c0d7bc72ed244 2025-09-08T16:37 | OK |
| 103 | 113 | linear.linear_issues | INSERT | `ART-830` | julia 4:5 android 1080x1350 (4:5 static); Done | OK |
| 104 | 114 | linear.linear_comments | INSERT | `cmt_art830_1` | ART-830 by usr_175c0d7bc72ed244 2025-09-08T16:38 | OK |
| 105 | 115 | linear.linear_issues | INSERT | `ART-831` | marcus portrait UA end card (9:16 end card); Done | OK |
| 106 | 116 | linear.linear_comments | INSERT | `cmt_art831_1` | ART-831 by usr_175c0d7bc72ed244 2025-09-08T16:39 | OK |
| 107 | 117 | linear.linear_comments | INSERT | `cmt_art831_2` | ART-831 by usr_175c0d7bc72ed244 2025-09-29T17:40 | OK |
| 108 | 118 | linear.linear_issues | INSERT | `ART-832` | end card template 16:9 (16:9 end card); Done | OK |
| 109 | 119 | linear.linear_comments | INSERT | `cmt_art832_1` | ART-832 by usr_175c0d7bc72ed244 2025-09-08T16:40 | OK |
| 110 | 120 | linear.linear_issues | INSERT | `ART-833` | end card 001 (9:16 end card); Done | OK |
| 111 | 121 | linear.linear_comments | INSERT | `cmt_art833_1` | ART-833 by usr_175c0d7bc72ed244 2025-09-08T16:41 | OK |
| 112 | 122 | linear.linear_comments | INSERT | `cmt_art833_2` | ART-833 by usr_175c0d7bc72ed244 2025-09-09T17:30 | OK |
| 113 | 123 | linear.linear_issues | INSERT | `ART-834` | end card 16:9 from 001 (16:9 end card); Done | OK |
| 114 | 124 | linear.linear_comments | INSERT | `cmt_art834_1` | ART-834 by usr_175c0d7bc72ed244 2025-09-08T16:42 | OK |
| 115 | 125 | linear.linear_issues | INSERT | `ART-835` | end card 1:1 from 001 (1:1 end card); Done | OK |
| 116 | 126 | linear.linear_comments | INSERT | `cmt_art835_1` | ART-835 by usr_175c0d7bc72ed244 2025-09-08T16:43 | OK |
| 117 | 127 | linear.linear_issues | INSERT | `ART-836` | GreenCouch 001 (9:16 video); Canceled | OK, advisory ADV-1 |
| 118 | 128 | linear.linear_issues | INSERT | `ART-837` | Professional Mode 9x16 test (9:16 video); Canceled | OK, advisory ADV-1 |
| 119 | 129 | linear.linear_issues | INSERT | `ART-838` | sophie ocean portrait (9:16 video); Canceled | OK, advisory ADV-1 |
| 120 | 130 | linear.linear_issues | INSERT | `ART-839` | squirrelfail portrait text (9:16 video); Canceled | OK, advisory ADV-1 |
| 121 | 131 | linear.linear_issues | INSERT | `ART-840` | boris fastcouch 9:16 (9:16 video); Done | OK |
| 122 | 132 | linear.linear_comments | INSERT | `cmt_art840_1` | ART-840 by usr_175c0d7bc72ed244 2025-09-12T16:21 | OK |
| 123 | 133 | linear.linear_issues | INSERT | `ART-841` | boris alin2 9:16 (9:16 video); Done | OK |
| 124 | 134 | linear.linear_comments | INSERT | `cmt_art841_1` | ART-841 by usr_175c0d7bc72ed244 2025-09-12T16:22 | OK |
| 125 | 135 | linear.linear_issues | INSERT | `ART-842` | boris fastcouch 16:9 (16:9 video); Done | OK |
| 126 | 136 | linear.linear_comments | INSERT | `cmt_art842_1` | ART-842 by usr_175c0d7bc72ed244 2025-09-12T16:23 | OK |
| 127 | 137 | linear.linear_issues | INSERT | `ART-843` | couch boss 30 16:9 (16:9 video); Done | OK |
| 128 | 138 | linear.linear_comments | INSERT | `cmt_art843_1` | ART-843 by usr_175c0d7bc72ed244 2025-09-15T16:01 | OK |
| 129 | 139 | linear.linear_issues | INSERT | `ART-844` | couch marketing2 30s 16:9 (16:9 video); Done | OK |
| 130 | 140 | linear.linear_comments | INSERT | `cmt_art844_1` | ART-844 by usr_175c0d7bc72ed244 2025-09-15T16:02 | OK |
| 131 | 141 | linear.linear_issues | INSERT | `ART-845` | cinematicTutorial Ad 1 16:9 (16:9 video); Done | OK |
| 132 | 142 | linear.linear_comments | INSERT | `cmt_art845_1` | ART-845 by usr_175c0d7bc72ed244 2025-09-15T16:03 | OK |
| 133 | 143 | linear.linear_issues | INSERT | `ART-846` | tutorialCinematic 1:1 (1:1 video); Done | OK |
| 134 | 144 | linear.linear_comments | INSERT | `cmt_art846_1` | ART-846 by usr_175c0d7bc72ed244 2025-09-15T16:04 | OK |
| 135 | 145 | linear.linear_issues | INSERT | `ART-847` | cheer 30p 4:5 (4:5 video); Done | OK |
| 136 | 146 | linear.linear_comments | INSERT | `cmt_art847_1` | ART-847 by usr_175c0d7bc72ed244 2025-09-15T16:05 | OK |
| 137 | 147 | linear.linear_issues | INSERT | `ART-848` | end card 4:5 from 001 (4:5 end card); Done | OK |
| 138 | 148 | linear.linear_comments | INSERT | `cmt_art848_1` | ART-848 by usr_175c0d7bc72ed244 2025-09-15T16:06 | OK |
| 139 | 149 | linear.linear_issues | INSERT | `ART-849` | julia 1:1 android tablet (1:1 static); Done | OK |
| 140 | 150 | linear.linear_comments | INSERT | `cmt_art849_1` | ART-849 by usr_175c0d7bc72ed244 2025-09-15T16:07 | OK |
| 141 | 151 | linear.linear_issues | INSERT | `ART-850` | boris alin2 16:9 (16:9 video); Done | OK |
| 142 | 152 | linear.linear_comments | INSERT | `cmt_art850_1` | ART-850 by usr_175c0d7bc72ed244 2025-09-15T16:08 | OK |
| 143 | 153 | linear.linear_issues | INSERT | `ART-851` | cheer fastcouch 4:5 (4:5 video); Done | OK |
| 144 | 154 | linear.linear_comments | INSERT | `cmt_art851_1` | ART-851 by usr_c77c50cc15c5342d 2025-09-17T17:36 | OK |
| 145 | 155 | linear.linear_comments | INSERT | `cmt_art851_2` | ART-851 by usr_175c0d7bc72ed244 2025-09-17T17:55 | OK |
| 146 | 156 | linear.linear_issues | INSERT | `ART-852` | barrel marketing2 1:1 (1:1 video); Done | OK |
| 147 | 157 | linear.linear_comments | INSERT | `cmt_art852_1` | ART-852 by usr_c77c50cc15c5342d 2025-09-17T17:46 | OK |
| 148 | 158 | linear.linear_comments | INSERT | `cmt_art852_2` | ART-852 by usr_175c0d7bc72ed244 2025-09-17T18:05 | OK |
| 149 | 159 | linear.linear_issues | INSERT | `ART-853` | couch alpha 50 4:5 (4:5 video); Done | OK |
| 150 | 160 | linear.linear_comments | INSERT | `cmt_art853_1` | ART-853 by usr_c77c50cc15c5342d 2025-09-23T16:16 | OK |
| 151 | 161 | linear.linear_comments | INSERT | `cmt_art853_2` | ART-853 by usr_175c0d7bc72ed244 2025-09-23T16:35 | OK |
| 152 | 162 | linear.linear_issues | INSERT | `ART-854` | balloons alpha 50 (1) 16:9 (16:9 video); Done | OK |
| 153 | 163 | linear.linear_comments | INSERT | `cmt_art854_1` | ART-854 by usr_c77c50cc15c5342d 2025-09-25T17:06 | OK |
| 154 | 164 | linear.linear_comments | INSERT | `cmt_art854_2` | ART-854 by usr_175c0d7bc72ed244 2025-09-25T17:25 | OK |
| 155 | 166 | linear.linear_issues | UPDATE | `id = 'ART-792'` | time_in_status_minutes = NULL | OK |
| 156 | 168 | gdrive.drive_files | INSERT | `d_272d849cde40c35980a433` | ZM3D Halloween 2025 (vnd.google-apps.folder) owner leonard.hayes | OK |
| 157 | 169 | gdrive.drive_files | INSERT | `d_74a7c95c28097dd9777e01` | Store (vnd.google-apps.folder) owner leonard.hayes | OK |
| 158 | 170 | gdrive.drive_files | INSERT | `d_6c2e4339e5d58108799ac8` | UA masters (vnd.google-apps.folder) owner leonard.hayes | OK |
| 159 | 171 | gdrive.drive_files | INSERT | `f_a72a7fd18327ed34fa2ac6` | ZM3D_Halloween_iPhone65_01_1242x2688.png (png) owner martin.walsh | OK |
| 160 | 172 | gdrive.drive_files | INSERT | `f_facf46180c5ba68c35925d` | ZM3D_Halloween_iPhone65_02_1242x2688.png (png) owner martin.walsh | OK |
| 161 | 173 | gdrive.drive_files | INSERT | `f_60aee1e96a59111c246a73` | ZM3D_Halloween_iPhone65_03_1242x2688.png (png) owner martin.walsh | OK |
| 162 | 174 | gdrive.drive_files | INSERT | `f_8a09205b3ab1ae2b7061b3` | ZM3D_Halloween_iPhone65_04_1242x2688.png (png) owner martin.walsh | OK |
| 163 | 175 | gdrive.drive_files | INSERT | `f_353fa24f04ab2c658d09bb` | ZM3D_Halloween_iPhone65_05_1242x2688.png (png) owner martin.walsh | OK |
| 164 | 176 | gdrive.drive_files | INSERT | `f_dc52b1cdde87ff49f36bc1` | ZM3D_Halloween_GooglePlay_phone_01_1080x1920.png (png) owner martin.walsh | OK |
| 165 | 177 | gdrive.drive_files | INSERT | `f_e84ff3bed0d6eb20aa6ae5` | ZM3D_Halloween_GooglePlay_phone_02_1080x1920.png (png) owner martin.walsh | OK |
| 166 | 178 | gdrive.drive_files | INSERT | `f_846e988c8642078ec32fd8` | ZM3D_Halloween_GooglePlay_phone_03_1080x1920.png (png) owner martin.walsh | OK |
| 167 | 179 | gdrive.drive_files | INSERT | `f_ca2f05278861dc6e12ecfd` | ZM3D_Halloween_GooglePlay_phone_04_1080x1920.png (png) owner martin.walsh | OK |
| 168 | 180 | gdrive.drive_files | INSERT | `f_a1582de8fc89f7ab4d42e8` | ZM3D_Halloween_GooglePlay_phone_05_1080x1920.png (png) owner martin.walsh | OK |
| 169 | 181 | gdrive.drive_files | INSERT | `f_fcfdf5502a68b1797fa0db` | ZM3D_Halloween_GooglePlay_phone_06_1080x1920.png (png) owner martin.walsh | OK |
| 170 | 182 | gdrive.drive_files | INSERT | `f_dc5cf9e4250d433c1511ec` | cheer_fastcouch_halloween_9x16.mp4 (mp4) owner marcus.bennett | OK |
| 171 | 183 | gdrive.drive_files | INSERT | `f_bcd34f98925e3f20d846ce` | cheer_fastcouch_halloween_16x9.mp4 (mp4) owner marcus.bennett | OK |
| 172 | 185 | gdrive.drive_files | INSERT | `f_02b1968f5e882366fbb883` | ZM3D live creatives (vnd.google-apps.spreadsheet) owner frederick.stone | OK |
| 173 | 186 | gsheets.sheets_spreadsheets | INSERT | `f_02b1968f5e882366fbb883` | ZM3D live creatives | OK |
| 174 | 187 | gsheets.sheets_sheets | INSERT | `sheet_id 0` | tab "Read me" of f_02b1968f5e882366fbb883 | OK |
| 175 | 188 | gsheets.sheets_sheets | INSERT | `sheet_id 1` | tab "Store" of f_02b1968f5e882366fbb883 | OK |
| 176 | 189 | gsheets.sheets_sheets | INSERT | `sheet_id 2` | tab "Unity" of f_02b1968f5e882366fbb883 | OK |
| 177 | 190 | gsheets.sheets_sheets | INSERT | `sheet_id 3` | tab "Archive" of f_02b1968f5e882366fbb883 | OK |
| 178 | 192 | gdrive.drive_files | INSERT | `f_fdd6d2d2f4a4d2f5b908fb` | ZM3D release calendar — Q4 (vnd.google-apps.document) owner arthur.blake | OK |
| 179 | 193 | gdocs.docs_documents | INSERT | `f_fdd6d2d2f4a4d2f5b908fb` | ZM3D release calendar — Q4 | OK |
| 180 | 200 | gdrive.drive_files | INSERT | `f_5ebf55ad29e815d46243c8` | Seasonal art direction — Q4 2025 (vnd.google-apps.presentation) owner robert | OK |
| 181 | 201 | gslides.slides_presentations | INSERT | `f_5ebf55ad29e815d46243c8` | Seasonal art direction — Q4 2025 | OK |
| 182 | 202 | gslides.slides_pages | INSERT | `slide_3094f53a92b2` | page 0 | OK |
| 183 | 203 | gslides.slides_page_elements | INSERT | `el_46b532d7f66d` | on slide_3094f53a92b2 | OK |
| 184 | 204 | gslides.slides_page_elements | INSERT | `el_9006e13d1b71` | on slide_3094f53a92b2 | OK |
| 185 | 205 | gslides.slides_pages | INSERT | `slide_2f543a88ea15` | page 1 | OK |
| 186 | 206 | gslides.slides_page_elements | INSERT | `el_bc403344b919` | on slide_2f543a88ea15 | OK |
| 187 | 207 | gslides.slides_page_elements | INSERT | `el_1f12d04ad444` | on slide_2f543a88ea15 | OK |
| 188 | 209 | gslides.slides_pages | INSERT | `slide_0655492faa5a` | page 2 | OK |
| 189 | 210 | gslides.slides_page_elements | INSERT | `el_61ecca3f712d` | on slide_0655492faa5a | OK |
| 190 | 211 | gslides.slides_page_elements | INSERT | `el_5925f7c037fa` | on slide_0655492faa5a | OK |
| 191 | 212 | gslides.slides_pages | INSERT | `slide_2b60b5e53f2c` | page 3 | OK |
| 192 | 213 | gslides.slides_page_elements | INSERT | `el_43a43bd396b4` | on slide_2b60b5e53f2c | OK |
| 193 | 214 | gslides.slides_page_elements | INSERT | `el_b04e5ccd5706` | on slide_2b60b5e53f2c | OK |
| 194 | 219 | gmail.gmail_threads | INSERT | `claire.morgan@harmonygames.co/1843080777036925215` | mailbox claire.morgan | OK |
| 195 | 220 | gmail.gmail_messages | INSERT | `claire.morgan/<CANf1Nx8adc8e5aab6a…` | "October UA plan (draft)" 2025-09-12T17:40 | OK |
| 196 | 224 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1843080777478741540` | mailbox frederick.stone | OK |
| 197 | 225 | gmail.gmail_messages | INSERT | `frederick.stone/<CANf1Nx8adc8e5aab6a…` | "October UA plan (draft)" 2025-09-12T17:40 | OK |
| 198 | 229 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1843080777552218739` | mailbox leonard.hayes | OK |
| 199 | 230 | gmail.gmail_messages | INSERT | `leonard.hayes/<CANf1Nx8adc8e5aab6a…` | "October UA plan (draft)" 2025-09-12T17:40 | OK |
| 200 | 234 | gmail.gmail_threads | INSERT | `marcus.bennett@harmonygames.co/1843080777405480450` | mailbox marcus.bennett | OK |
| 201 | 235 | gmail.gmail_messages | INSERT | `marcus.bennett/<CANf1Nx8adc8e5aab6a…` | "October UA plan (draft)" 2025-09-12T17:40 | OK |
| 202 | 239 | gmail.gmail_threads | INSERT | `martin.walsh@harmonygames.co/1843080777143145137` | mailbox martin.walsh | OK |
| 203 | 240 | gmail.gmail_messages | INSERT | `martin.walsh/<CANf1Nx8adc8e5aab6a…` | "October UA plan (draft)" 2025-09-12T17:40 | OK |
| 204 | 244 | gmail.gmail_threads | INSERT | `claire.morgan@harmonygames.co/1844644077950167516` | mailbox claire.morgan | OK |
| 205 | 245 | gmail.gmail_messages | INSERT | `claire.morgan/<CANf1Nx47805f8aa3d3…` | "Unity retention restart" 2025-09-29T23:48 | OK |
| 206 | 248 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844644078464897252` | mailbox frederick.stone | OK |
| 207 | 249 | gmail.gmail_messages | INSERT | `frederick.stone/<CANf1Nx47805f8aa3d3…` | "Unity retention restart" 2025-09-29T23:48 | OK |
| 208 | 252 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844644078011653282` | mailbox leonard.hayes | OK |
| 209 | 253 | gmail.gmail_messages | INSERT | `leonard.hayes/<CANf1Nx47805f8aa3d3…` | "Unity retention restart" 2025-09-29T23:48 | OK |
| 210 | 256 | gmail.gmail_threads | INSERT | `marcus.bennett@harmonygames.co/1844644078077504433` | mailbox marcus.bennett | OK |
| 211 | 257 | gmail.gmail_messages | INSERT | `marcus.bennett/<CANf1Nx47805f8aa3d3…` | "Unity retention restart" 2025-09-29T23:48 | OK |
| 212 | 260 | gmail.gmail_threads | INSERT | `martin.walsh@harmonygames.co/1844644078449983920` | mailbox martin.walsh | OK |
| 213 | 261 | gmail.gmail_messages | INSERT | `martin.walsh/<CANf1Nx47805f8aa3d3…` | "Unity retention restart" 2025-09-29T23:48 | OK |
| 214 | 264 | gmail.gmail_threads | INSERT | `claire.morgan@harmonygames.co/1844732284519287777` | mailbox claire.morgan | OK |
| 215 | 265 | gmail.gmail_messages | INSERT | `claire.morgan/<CANf1Nxe0e348c2afd3…` | "October UA plan - changes" 2025-09-30T23:10 | OK |
| 216 | 271 | gmail.gmail_threads | INSERT | `frederick.stone@harmonygames.co/1844732284882540716` | mailbox frederick.stone | OK |
| 217 | 272 | gmail.gmail_messages | INSERT | `frederick.stone/<CANf1Nxe0e348c2afd3…` | "October UA plan - changes" 2025-09-30T23:10 | OK |
| 218 | 278 | gmail.gmail_threads | INSERT | `leonard.hayes@harmonygames.co/1844732285026565607` | mailbox leonard.hayes | OK |
| 219 | 279 | gmail.gmail_messages | INSERT | `leonard.hayes/<CANf1Nxe0e348c2afd3…` | "October UA plan - changes" 2025-09-30T23:10 | OK |
| 220 | 285 | gmail.gmail_threads | INSERT | `marcus.bennett@harmonygames.co/1844732284828828071` | mailbox marcus.bennett | OK |
| 221 | 286 | gmail.gmail_messages | INSERT | `marcus.bennett/<CANf1Nxe0e348c2afd3…` | "October UA plan - changes" 2025-09-30T23:10 | OK |
| 222 | 292 | gmail.gmail_threads | INSERT | `martin.walsh@harmonygames.co/1844732284741054074` | mailbox martin.walsh | OK |
| 223 | 293 | gmail.gmail_messages | INSERT | `martin.walsh/<CANf1Nxe0e348c2afd3…` | "October UA plan - changes" 2025-09-30T23:10 | OK |
| 224 | 299 | gmail.gmail_threads | INSERT | `claire.morgan@harmonygames.co/1844154099753384967` | mailbox claire.morgan | OK |
| 225 | 300 | gmail.gmail_messages | INSERT | `claire.morgan/<CAJec750be2c45f33a4…` | "Halloween props for Zombie Match 3D" 2025-09-24T14:00 | OK |
| 226 | 304 | gcal.gcal_events | INSERT | `evt_d947bf7cd910549b674b1f` | calendar claire.morgan | OK |
| 227 | 305 | gcal.gcal_events | INSERT | `evt_239a96845c8465f6c4099b` | calendar leonard.hayes | OK |
| 228 | 306 | gcal.gcal_events | INSERT | `evt_7ca595cfa2e8a51769ef28` | calendar frederick.stone | OK |
| 229 | 307 | gcal.gcal_events | INSERT | `evt_1f74e7a2684103c4644a3d` | calendar martin.walsh | OK |
| 230 | 308 | gcal.gcal_events | INSERT | `evt_78fd240a7e0229f18fe246` | calendar marcus.bennett | OK |
| 231 | 309 | gcal.gcal_events | INSERT | `evt_8678e073bb601ead3e686b` | calendar robert | OK |
| 232 | 310 | gcal.gcal_events | INSERT | `evt_26c86d9ea1b590bf86fe70` | calendar arthur.blake | OK |
| 233 | 312 | trello.trello_cards | INSERT | `68dc52e015f87c50c441d1a9` | #80 Halloween push - store + ads (Claire/Martin/Marcus) | OK |
| 234 | 313 | trello.trello_actions | INSERT | `68dc52e00c3711a8c59f3b0c` | createCard on 68dc52e015f87c50c441d1a9 2025-09-30T22:00 | OK |
| 235 | 314 | trello.trello_actions | INSERT | `68dc65a0f2d7fb28743f5860` | commentCard on 68dc52e015f87c50c441d1a9 2025-09-30T23:20 | OK |
| 236 | 316 | trello.trello_actions | INSERT | `68d6cff0c6568da5d9c8e81f` | commentCard on 68768a1501ae552dbee94b8a 2025-09-26T17:40 | OK |
| 237 | 317 | trello.trello_cards | UPDATE | `id = '68768a1501ae552dbee94b8a'` | "dateLastActivity" = '2025-09-26T17:40:00Z', badges_json = {comments:1,...} | OK |
| 238 | 318 | trello.trello_boards | UPDATE | `id = '6851a6569f3bf818760632ab'` | "dateLastActivity" = '2025-09-30T23:20:00Z' | OK |
| 239 | 320 | contacts.contacts | INSERT | `6b350edd259a8b4499a9e625` | PERSON_6311_EMAIL, Founder, KayKit | OK |

## 8. Stage dependencies for reuse (stage-evidence-v1)

- This review is bound to SQL sha256 `6c143945…fd033` (revision 6), universe manifest `da2f4cf0…aac1a`, schema snapshot `31dcb2b4…5151`, clock 2025-10-01T07:00Z. Any SQL change invalidates it.
- NEW checks: full-file lint (239 statements); rows 2–3 (A, B, C); collision check of the new Slack id; re-check of every injected record that names ART-795/797/805/823, the three re-recorded creatives or builds #1935/#1966 (the only records the new reply could contradict); updated thread counters.
- reused_evidence: per-row A/B/C results for the 237 byte-identical statements from the revision-3 review (SQL sha256 `2175e44f…6df27`, same report format and `injection-static-v2`). Dependencies verified unchanged: statement text (diff shows only line 2 changed and line 3 added), universe manifest sha256 `da2f4cf0…aac1a`, schema snapshot sha256 `31dcb2b4…5151`, clock, lint version. Collection-wide absence results reused only for ids that are unchanged; the one new id was scanned NEW.
- What /prompt can reuse: collision coverage (§5.1 table), reference resolution, chronology and the base-fact table (§5.3). /prompt still owns discoverability, Claire's visibility of each record (including zm-animations, where the new reply sits), feasibility and base-data dependence (ADV-2, ADV-4).

## 9. Evidence limits (outside static scope)

- The SQL was not executed. Live database compatibility, including the ADV-3 columns, and load-universe behaviour are not certified.
- The schema snapshot is unverified. Uniqueness is certified against the local base plus this SQL, not the live database.
- Task difficulty, discoverability and persona visibility are not assessed here; they belong to /prompt and /hardness.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort 15

Next action: Send /prompt, /hardness, /oe and /rubric again (they all read the injection SQL), in that order.

Evidence limits: Static review only; SQL not executed; live schema compatibility (ADV-3 columns) and Agent visibility not certified.

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
