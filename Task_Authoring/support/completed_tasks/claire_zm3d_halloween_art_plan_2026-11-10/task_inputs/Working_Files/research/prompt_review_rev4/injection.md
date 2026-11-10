# /injection report: Injection data integrity (Eval 0), delta review

## 1. Scope

| Field | Value |
|---|---|
| Review version | `injection-static-v2` |
| Mode | Delta review against the previous passing SQL. Static only, SQL never executed |
| Review time | 2026-11-07T18:22Z |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut` (hg4-synth-sep30cut v16; archive sha256 `d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c`) |
| Universe manifest | `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a` |
| SQL under review | `inputs/01_Universe_Inject.sql`, 173,249 bytes, sha256 `6c143945fe3e3aae8326363b4ac7df7ac3e4349a78668bfb9d8acc1644afd033` (byte-identical to `task_stub/01_Universe_Inject.sql`) |
| Previous SQL | `prev/01_Universe_Inject.prev.sql`, 172,543 bytes, sha256 `2175e44fb540b0224d3d6e4cf92878ac24295454483d2b48ea4893ee26f6df27` (same hash as the input recorded in `prev/0_injection_prev.md`) |
| Schema snapshot | `Evals/references/schema/injection.json` sha256 `01ef5792…` (unverified snapshot; see ADV-6) |
| Lint | `hg_injection_lint.py` injection-lint-v1 |

## 2. Diff summary

| Change | Count | Detail |
|---|---|---|
| Statements changed | 1 | L2, `slack.slack_messages` INSERT `2c9fbac7d610f8a1eb138d8d875a15d2` (Marcus's parent message) |
| Statements added | 1 | L3, `slack.slack_messages` INSERT `6aecfa673deb24040a0d83058b4848d8` (Marcus's thread reply) |
| Statements removed | 0 | |
| Total | 238 → 239 | 233 → 234 INSERT, 5 UPDATE unchanged, 13 comment lines unchanged |

**Everything outside the diff is identical.** Removing prev L2 and new L2–L3 leaves two byte-identical bodies of 171,904 bytes, both sha256 `c6fa79a0123eac85…`. New L4–L321 equal prev L3–L320, so the earlier report's evidence carries over with its line numbers shifted by +1, apart from the one row in ADV-1.

**L2 field diff (exactly four of 18 columns; text, ts, id and created_at unchanged):**

| Column | Before | After |
|---|---|---|
| `thread_ts_legacy` | NULL | `'1758823964.738872'` |
| `reply_count` | 0 | 1 |
| `reply_users_count` | 0 | 1 |
| `latest_reply` | NULL | `'1758825697.426919'` |

**L3 text:** "use these from now on, they replace the april captures on ART-795, ART-805 and ART-797. the couch 16:9 on ART-823 wasnt redone, thats still the apr 7 capture"

## 3. Lint

Run on both the direct path and `hg.py lint --task-dir task_stub`, with the same result: **0 FAIL, 0 CHECK, 1 INFO**, base lookups used. The previous SQL gives the same counts.

| Flag | Severity | Resolution |
|---|---|---|
| `unparsed` L171 `gdrive.drive_files` `content_path`: 13 media files carry metadata only | INFO | Not new. Same rows as prev L170, byte-identical, already resolved in the earlier report. Eval 0 allows metadata-only media unless the task needs their content |

## 4. Operation ledger (changed statements)

| Line | Table | Op | Record | Key values | A | B | C |
|---|---|---|---|---|---|---|---|
| 2 | slack.slack_messages | INSERT (changed) | `2c9fbac7d610f8a1eb138d8d875a15d2` | C09ATAJ220H, EMPLOYEE_0002, ts 1758823964.738872, 2025-09-25T18:12:44.738872Z, thread root with 1 reply | OK | OK | OK |
| 3 | slack.slack_messages | INSERT (new) | `6aecfa673deb24040a0d83058b4848d8` | C09ATAJ220H, EMPLOYEE_0002, ts 1758825697.426919, 2025-09-25T18:41:37.426919Z, reply to L2 | OK | OK | OK |

The other 237 statements are unchanged; see the ledger in `prev/0_injection_prev.md` §7, line numbers +1.

## 5. Check results (changed statements)

| Check | Result | Evidence |
|---|---|---|
| A: Records, references and IDs | PASS | §5.1 |
| B: SQL structure and supported schema rules | PASS | §5.2 |
| C: Dates, relationships, consistency, grader-facing text | PASS | §5.3 |

### 5.1 Check A

- **ID formula:** base ids are `sha256("<channel>|<ts>")[:32]` (3,000 of 3,000 sampled base rows). Both L2 and L3 match, as do all 15 injected Slack INSERTs.
- **Collisions:** complete scan of 4,840 `messages/*/*.json` files, 610,468 records. No match for either id or either ts, and no base `thread_ts` points at either ts. Both ids and `(channel, ts)` pairs are unique across the SQL. Base ids themselves are unique (529,432 id-bearing rows, 0 duplicates).
- **Author:** `EMPLOYEE_0002_SLACK_ID` is Marcus Bennett, not deleted, a member of `C09ATAJ220H`, and 85 base posts there.
- **Channel:** `C09ATAJ220H` zm-animations, private, not archived, created 2025-08-14 (`created` 1755189890), so both posts fall after it opened.
- **Thread reference:** L3 `thread_parent_id` is L2's `id`, and L3 `thread_ts_legacy` is L2's `ts`. L2 precedes L3 in the file.
- **Ticket references:** ART-795, ART-797, ART-805 and ART-823 resolve to injected issues at L33, L38, L56 and L98, all created 2025-09-08, before the reply. Base ART stops at 792, so none collide.
- **Other references to these rows:** no other statement mentions either id or ts.

### 5.2 Check B

- **Structure:** both rows have 18 columns and 18 values. The L3 column list is byte-identical to L2's. Each statement ends correctly.
- **Required columns:** all NOT NULL columns without defaults are present (`id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json`).
- **Generated column:** `text_fts` is absent.
- **Types:** counters are unquoted integers, the booleans are `false`, and `created_at` is a valid timestamp literal. The JSON columns hold valid `'[]'` and `'{}'`.
- **Escaping:** no apostrophes in either text, so nothing needs doubling, and no non-ASCII bytes in either line.
- **Schema snapshot:** all columns MATCH `slack_messages`. No Slack table holds a channel or thread counter that would also need updating (`slack_channels` columns checked).

**Format against base conventions**

| Item | Base | L2 / L3 | Result |
|---|---|---|---|
| `ts` shape | `\d{10}\.\d{6}`, all 529,432 rows | Both match | OK |
| Parent `thread_ts` | Equals own ts, 13,678 of 13,678 parents | L2 equals own ts | OK |
| Message with no replies | `thread_ts` null | L2 correctly moved from NULL to own ts when it gained a reply | OK |
| Reply counters | `(0, 0, null)`, 80,127 of 80,127 replies | L3 `0, 0, NULL` | OK |
| Self-reply thread, one reply | `(1, 1, latest = reply ts)`, 928 of 934 | L2 `1, 1, reply ts` | OK |
| Reply `subtype`, `is_activity_message` | NULL (76,318 of 80,127), false (all) | NULL, false | OK |
| `created_at` against `ts` | Injected convention, ts to the microsecond | Both exact: `18:12:44.738872Z`, `18:41:37.426919Z` | OK |
| `thread_parent_id` | Not exported, so no base proof | Parent `id`, same as the 7 other injected replies (L5, L6, L8, L10, L12, L22, L25) | OK (see limits) |

### 5.3 Check C

**Chronology**

- Reply follows parent by 1,733 seconds. Both are before the clock.
- Both fall after the build and export events they rest on: ART-854's #1966 export at Sep 25 17:06Z and upload at 17:25Z, then parent 18:12Z, reply 18:41Z.
- Sep 25, 2025 is a Thursday. Marcus was active that day, last base post 17:44:50Z in this same channel, and the next base message there is Sep 26 10:11Z. No thread interleaves.
- Working hours: 18:00Z is a normal hour for him (1,918 of 24,072 posts in all, 17 of 1,049 in Sep 2025). Base has him posting later on other days, for example Sep 30 20:12Z.

**Each claim in the new text**

| Claim in L3 | Record | Result |
|---|---|---|
| ART-795 was an April capture | L34: "Captured from Android #456 on Apr 7" | Agrees |
| ART-805 was an April capture | L57: "Captured from Android #633 on Apr 29" | Agrees |
| ART-797 was an April capture | L39: "Captured from Android #456 on Apr 7" | Agrees |
| Ticket order and identity | Matches L2's order: couch alpha 50 (ART-795), barrel marketing2 4:5 (ART-805), balloons alpha 50 (1) (ART-797) | Agrees |
| ART-823 is the couch 16:9, Apr 7 capture, not redone | L98 title "couch alpha 50 16:9"; L99 "Captured from Android #456 on Apr 7"; one comment only, no re-capture note | Agrees |
| Builds exist on those dates | `C05433XK267`: Match3D Android #456 Success 2025-04-07T17:10Z, #633 Success 2025-04-29T15:24Z, #1896 Sep 16, #1935 Sep 22, #1966 Sep 24 | Agrees |
| April source files | Frederick posted `30 sec couch alpha 50-VEED.mp4` Apr 7 21:00Z and `30 sec balloons alpha 50-VEED (1).mp4` Apr 7 21:19Z (`C0880U9751A`), and `barrel_marketing2_4-5_blur-VEED.mp4` Apr 29 18:09Z (`C8B75A13B6E5`) | Agrees |

**Contradiction tests on the combined state**

| Test | Finding | Result |
|---|---|---|
| Ticket comments still show April captures, with no re-capture note on ART-795, 797, 805 | Those comments are dated Sep 8, and the earliest re-record build (#1896) is Sep 16. They were true when written and L3 corrects them later, which Eval 0 allows | No conflict |
| Sheet rows still show "Live since Apr 7" and "Apr 29" | "Live since" is when the ad went live, not the capture. ART-808 shows the same pattern: re-captured Sep 16, row still Jul 28 | No conflict |
| Sheet Read me says capture notes are in the ticket comments | A stale pointer superseded by a later source, which Eval 0 allows | No conflict |
| Deck rule (L207): "If a later capture has replaced it, the newest capture is the one that counts." | L3 uses the same reading. All three new builds are newer than #1452 | Agrees |
| ART-852, 853, 854 exports | Build numbers match L2 and the "same edit" wording. They are extra formats from the same re-records. "No music" matches the three masters | Agrees |
| Base: Frederick, Aug 6, "I need to rerecord all the previous videos without sound" (`C07C2866011`) | Read in full. These are his Aug 2–5 Recorder clips for Marcus's montage (`D05UDNHAPL2`, Aug 1–6), not the April UA cuts | No conflict |
| Base: Trello "Marketing Video Refresh", complete Aug 20 | Card has no description, comments, checklist or attachments, and names no cut | No conflict |
| Base: "Android Build 1966 Notes: QA Build", 2025-06-11 | A different job's bot post. The Sep 24 post reads "Match3D Android - #1966" | No conflict |
| Base: any statement that UA videos were already refreshed | None. Cut names and ticket ids searched over all Slack. Refresh terms searched over Jul 20–Oct 1 for seven relevant people. Cut names and "re-recorded" / "re-captured" searched in Gmail, Trello, Confluence, Docs, Sheets, Slides and Calendar: complete scans, no relevant hits (4 Gmail hits are newsletters). Drive: no videos with these names among 53,631 files | No conflict |
| Known issues (`synthcut.md`) | None concerns these cuts or builds. SC-70 means Slack timezones can't be used, so hours were taken from post history | No conflict |

**Grader-facing text:** none. L3 is an in-world workplace message, and lint `grader_language` and `padding_comment` are clean. No comment was added for it.

## 6. Demonstrated defects

None.

## 7. Advisories (not defects)

| ID | Observation | Why it isn't a defect | Suggested action |
|---|---|---|---|
| ADV-1 | The earlier report's row on L2 says "Coherent reading: the old cuts were not replaced". L3 now says they were | That row was a reading, not a record. Do not carry it over. The new reading: the re-records replace the captures behind ART-795, 805 and 797, and ART-852, 853 and 854 are extra formats from them | Use the new reading in later stages |
| ADV-2 | L3 is now the only record tying the re-records to those three tickets. It sits in private `C09ATAJ220H`, where Frederick (EMPLOYEE_0008) is not a member, though L2 says "for frederick" and L3 says "use these from now on". Claire (EMPLOYEE_0009) is a member | Not addressed to him by name, and L2's wording already passed. A realism point, not an incompatible fact. Agent visibility belongs to `/prompt` | Confirm at `/prompt` that the persona's route to L3 is fair |
| ADV-3 | L3 flags the couch 16:9 as not redone but says nothing about ART-806 (barrel marketing2 16:9, sibling of ART-805, L59 "Apr 29") | L3 limits the replacement to three named tickets, so ART-806 stays on Apr 29. It runs only on Android US tablet, which the Sep 30 mail drops from Halloween, so the call does not depend on it | None required. Keep OE and rubric consistent with this |
| ADV-4 | L2's `ts` ends in 2. In base, 529,409 of 529,432 id-bearing ts values end in 9 and the other 23 in 0. L3 ends in 9. 13 of the 15 injected INSERTs do not | Unlisted field, and L2's `ts` is unchanged from the passing SQL. A difference from examples is not an ID finding under Check A | None required |
| ADV-5 | #1966 is a branch build (`…/QueueManager`, started by Calvin Price), unlike #1896 and #1935 on `main`. L3 now makes it the adopted source for ART-797 | Build succeeded and is newer than #1452. L2's text is unchanged. No record says it can't be used | None required |
| ADV-6 | The schema hash here (`01ef5792…`) differs from the earlier report's (`31dcb2b4…`), which also matches neither git version of the file | The earlier report appears to have run from a different bundle (not confirmed). Current lint and §5.2 used the current file. Provenance note only | None required |
| ADV-7 | "use these" has no attachment, and no injected Drive row holds the re-recorded files | Nothing claims a location, and L2 was the same. Only matters if the task needs those files | None required |

The earlier report's ADV-1 to ADV-4 are unaffected, line numbers +1.

## 8. Limits

- `thread_parent_id` is not in the exports, so its parent-`id` form rests on the injected convention, not a base proof.
- `created_at` is also not exported. It was checked against `ts` and the injected rows.
- Statements outside the diff were not re-reviewed. They rest on the earlier report and the byte-identity proof in §2.
- Live compatibility, Agent visibility, task quality and difficulty are outside this static review.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Claude Opus 5.5 (claude-opus-5-5), effort as set for this session

Next action: Proceed to /prompt, and replace the earlier "old cuts were not replaced" reading (ADV-1)

Evidence limits: Delta scope only, with unchanged statements carried over by byte identity. `thread_parent_id` is not verifiable from base exports. Static review, so no deployment or live-schema assurance
