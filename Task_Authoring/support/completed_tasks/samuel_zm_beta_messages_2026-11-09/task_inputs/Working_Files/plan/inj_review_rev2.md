# /injection independent review: task_inputsK, rev2

Review version: injection-static-v2. Evidence contract: stage-evidence-v1. Reviewed 2026-11-04.
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).
Input: 01_Universe_Inject.sql, sha256 8766100f768ab9aabf51cf4bf5a5791914fed1639c92d52b538f3dd8b54476c0.
Previous: rev1, sha256 0c1cf21627d5d9fb6303127c005cbaab216522c5ba1bf25a1e04573a44d24dad.
Source: hg4-synth-sep30cut v16, archive sha256 d04f295b4c878cce145ad0d77fc5668962b1cb63412fc98f427a0026aeb0fb0c.
No SQL executed. Nothing edited except this file. Nothing saved to the Evals store.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), effort 100

Next action: Proceed to /prompt. Check there whether any prompt, OE or rubric text states the L36 audience as ask-only (see "Note for later stages").

Evidence limits: repo blobs are unreadable, so 4 parts of the L36 sentence are UNVERIFIABLE (listed below), and rev1's 27 UNVERIFIABLE client-code claims stay open. No Postgres parser was used. Live deployment is out of scope.

| Check | Result | Evidence |
|---|---|---|
| A: records, references and IDs | PASS | 3 changed statements re-checked in full. 142 unchanged data statements reused. |
| B: SQL structure and schema | PASS | Whole file re-tokenized by a new scanner. 147 statements, 0 count mismatches, 231 JSON assignments valid. |
| C: dates, relationships and consistency | PASS | The rev1 failure is closed. No new inconsistency. |

Counts: 3 changed statements, 4 changed assignments. Defects: 0 new, 1 rev1 failure closed. PENDING: 0. Lint flags: 0.

## 1. Changed statements

Compared line by line and again statement by statement with my own parser. Both files have 298 lines, LF endings and a final newline. The new file is 160 bytes longer, and every change is a pure insertion. Statement order and all column lists are identical. `cmp -l` reports 82,742 differing bytes, but that is only the offset shift after the first insertion.

| # | INSERT line | VALUES line | Table | Key | Column | Inserted text |
|---|---|---|---|---|---|---|
| 1 | L9 | L10 | gdrive.drive_files | f_de7a1ae20201816a67750d | shared_with_emails_json | `, "brian.foster@harmonygames.co"` |
| 1 | L9 | L10 | gdrive.drive_files | same | shared_roles_json | `, {"email": "brian.foster@harmonygames.co", "role": "reader"}` |
| 2 | L22 | L23 | gslides.slides_presentations | f_de7a1ae20201816a67750d | shared_with_emails_json | `, "brian.foster@harmonygames.co"` |
| 3 | L35 | L36 | slack.slack_messages | 09aae609aa744fb23288c7dcbac9926c | text | ` or they switch it on from settings` |

Check of the sums: 32 + 61 + 32 + 35 = 160 bytes, which equals the file growth.

Statements 1 and 2 were not named in the failure. They apply optional note N2 from inj_review_C2.md, so they get the same scrutiny.

## 2. Lint

`python3 Task_Authoring/tools/hg.py lint`, injection-lint-v1, on sha256 8766100f...: 147 statements, FAIL 0, CHECK 0, INFO 0, flags none. Nothing to resolve.

## 3. Checks A, B and C on each changed statement

### Check A

| Item | L9/L10 | L22/L23 | L35/L36 |
|---|---|---|---|
| New key collision | `id`: 0 hits in 53,631 /drive_files, scan complete | `presentation_id`, `drive_file_id`, `revision_id` ca404f1577: 0 hits in 132, complete | `id`: 0 hits in 610,468 records over 4,840 files, complete. `ts` 1759170096.924778: 0 hits, same coverage |
| Parent or reference | Parent d_63fffeb4fab5233ed5bb73 at /drive_files/9030, Leonard's root | drive_file_id = L9, earlier in the SQL | Parent 37c5701a... = L33, earlier in the SQL, absent from the base by the same lookup. thread_ts_legacy equals L33's ts |
| Actor and membership | All 5 sharees and the owner found in /drive_users, one row each: Leonard /7, Vincent /8, Robert /13, Samuel /19, Arthur /20, Brian /24 | Same 6 | EMPLOYEE_0025_SLACK_ID = Arthur Blake, users.json /13. Member of zombie-match3d, channels.json /108, not archived |
| Drive readability | No content_path, as in 132/132 base decks. The lint's `check_drive_readable` skips a Slides file with a slides_presentations row, and L22 is that row. Same judgment as rev1 Advisory 1 | n/a | n/a |

**Brian's identity.** brian.foster@harmonygames.co is one person across services: drive_users /24 (user_fc22d5941b2a), Slack /14 (EMPLOYEE_0026_SLACK_ID, Brian Foster, not deleted), Linear /users/40 (usr_fc22d5941b2aeb5c), roster (Game Engineer), contacts (id prefix fc22d5941b2a). Drive, Slack and Linear each have exactly one Brian, so there is no second account and no namesake. He owns or shares 228 base Drive files. Card SC-6 mentions this address, but only for Node Media email senders, and it confirms the address belongs to the HG engineer. The share is unaffected.

### Check B

- **Whole file, new scanner:** 147 statements (BEGIN, 137 INSERT, 8 UPDATE, COMMIT), empty tail, 0 column/value mismatches, 0 duplicate columns. 1,961 INSERT plus 17 UPDATE assignments = 1,978, matching rev1.
- **JSON:** 223 INSERT and 4 UPDATE values parse under a parser that rejects duplicate keys, and 4 are NULL, so 231 in total, matching rev1.
- **Column and value counts on the changed rows:** L9 13/13, L22 9/9, L35 18/18.
- **Quoting:** quote counts are even on L10 (22), L23 (18) and L36 (28). L36 keeps `doesn''t` doubled, and the new clause has no apostrophe. No backslashes or non-ASCII on these lines.
- **Schema:** all 4 edited columns are `text` with no max_length in both injection.json and the live reference. `slack_messages.text` is NOT NULL and supplied. `text_fts` is not written.

### Check C

**Sibling arrays.** `shared_with_emails_json` on L10 equals L23 in content and order, and the emails in `shared_roles_json` equal both. 5 entries, 5 unique, all `reader`, owner not listed. All 132 base decks also agree between Drive and Slides, so this matches the base pattern. Title, owner, visibility, created and modified are equal on L10 and L23. The other deck rows (L24 to L28) carry no share list.

**Chronology.** No timestamp changed. Deck 2025-09-19T18:30:26Z, then Brian cites it 2025-09-26T18:02:19Z, so he had access when he cited it. L36 is 2025-09-29T18:21:36.924778Z, after parent L33 at 17:40:08, and before the clock.

**Brian's deck citation (L32).** "the readiness deck says 6 anyway" matches L29 "6 Ready on the PN sheet". The sheet has 6 Ready rows of 14 (gsheets /sheets_spreadsheets/220/sheets/1).

**Other copies.** "only schedules" occurs once in the SQL, on L36. No record quotes the old wording. A scan for deck mentions found only the deck rows and L32. Grader-language scan of the new text: clean.

## 4. The named failure: verdict CLOSED

Rule: Check C, incompatible facts introduced by the SQL.
Revised L36: "that popup doesn't switch anything on btw. NotificationManager only schedules once our own ask has run or they switch it on from settings, on both platforms".

The sentence states a necessary condition ("only ... once"). It is false only if scheduling can start outside those two arms, so I traced every route.

### Every route that turns scheduling on

Scheduling is gated by one flag: `if (!NotificationsEnabled /*|| PlayerData.Profile == null*/) return;` (#248 rc_16). The flag is declared `public bool NotificationsEnabled { get; private set; } = false;`, so only NotificationManager can set it. It is set true in `EnableNotifications()` and reloaded in `Awake`.

| # | Route | Source | Arm | Result |
|---|---|---|---|---|
| 1 | Android ask, permission already held: `if (Permission.HasUserAuthorizedPermission(permission)) { EnableNotifications(); ...` | #248 rc_16 | Ask routine | Covered |
| 2 | Android ask, grant callback | #248 rc_16 | Ask | Covered |
| 3 | iOS ask: `HandleAuthorizationGranted(true)` calls `EnableNotifications()` | #248 rc_10 | Ask | Covered |
| 4 | Toggle, permission pref granted: `NotificationManager.Instance.EnableNotifications();` | #263 rc_4 | Settings | Covered. This is the route that failed rev1 |
| 5 | Toggle, first time: "Key does not exist ... NotificationToggleButton->>NotificationManager: Init()" | #292 walkthrough, /pull_request_comments/464, reviewed through head commit 3f814c4851 ("Enable to request notification permission pop up manually") | Settings | Covered. Not cited in rev1 |
| 6 | Toggle after denial: popup, then "NotificationManager->>SystemUI: Open system notification settings" | #263 walkthrough, /pull_request_comments/425 | Settings | Covered. Changes the OS state only; `OnApplicationFocus` writes just the pref string |
| 7 | `Awake`: `NotificationsEnabled = PlayerPrefs.GetInt(NotificationsEnabledKey, 0) == 1;` | #248 rc_16 | Neither directly | Covered. The key is only written by `EnableNotifications()`, so this restores an earlier routes 1 to 5 result |
| 8 | Launch: `Start() { Init(); }` in the June hunks | #248 rc_16 | Would be a third route | Closed. #251: "Removed the `Start()` method that previously called `Init()`" |
| 9 | `OnApplicationFocus(false)` calling `ScheduleDominoNotifications()` | #248 rc_16 | n/a | Guarded by the flag, cannot enable |

The one live entry to `Init()` outside the toggle is `NotificationPermissionRequester.Start()`. #327 gates it: "Tutorial not done ... Return early", and "ZombieConstants.FirstTutorialFinished (value 20)" (/reviews/2007). It also says init happens "consistently across all platforms". This supports L34 "our own ask after level 20" and "on both platforms" in L36.

**Result: the sentence is true against all visible code.** No visible route falls outside the two arms.

### Attacks that did not land

- **"that popup doesn't switch anything on".** Still true. On focus, the code only does `PlayerPrefs.SetString(NotificationsPermission, PermissionGranted)`, and the flag is untouched. Arthur's base post agrees that Unity triggers the launch prompt (EXEC /952).
- **"has run" on iOS when the second prompt is not shown.** EXEC /952: "if you accepted the first prompt, it won't show you the one after level 20". The sentence says the ask has *run*, not that it was shown, so it holds. "Has been shown" would have been wrong.
- **"on both platforms".** The toggle hunk has no `#if` block, and L180 reports arrival on both.
- **"from settings" read as the phone's Settings app.** Changing the OS setting alone does not set the flag (route 6). But L36 states a necessary condition, not a sufficient one, so this reading does not make it false. L15, L20 and L180 all mean the in-game route.
- **Base contradiction.** Complete searches found none: Slack 2025-06 to 2025-09 (626 files, 6 queries), Linear, Confluence, the PN sheet and Docs. ZOM-314 is Done, #263 merged 2025-07-02, and D076V3N8YUD 2025-07 /4 describes the new settings menu with the toggle. The only toggle removal, /pull_requests/527, is GameOfDominoes#1473 from 2024-11-21, a different game and earlier than match3d's toggle.

### Compatibility with every injected record on the subject

| Record | Text | Result |
|---|---|---|
| L15 rule doc | "A player only counts once our own permission ask has happened, the settings toggle doesn't count." | Compatible. The rule says who counts, and L36 says what schedules. The exclusion only makes sense if the toggle is a real route, so rev2 fits better than rev1 |
| L34 Robert | "leaving our own ask after level 20 ... The Unity popup at launch on iOS stays as it is." | Compatible. Same ask, same popup |
| L180 Vincent, DES-318 | "arrives on both when notifications are switched on from settings" | Compatible, and this resolves rev1's conflict. A below-20 player can now be scheduled |
| L168, L172, L176, L184, L190 Vincent | Arrival reports | Compatible. They do not say how notifications were enabled |
| L59, L63 QA note | "Seen only counts on a store build..." | Compatible. It sets no rule on how notifications are enabled |
| L20 pass log | "notifications switched on from settings" | Compatible. Same words as L36 |
| L178 Leonard | "new players below level 20" | Compatible. With K248 (value 20), L36 now explains how the test could pass |
| L65, L81 | PR #248 review text and hunk | No claim on enabling. June state, earlier than L36 |

### UNVERIFIABLE (needs a repo blob, not marked wrong)

1. Any caller of the public `EnableNotifications()` outside the visible hunks. **This is the only part that could falsify the sentence.** Nothing suggests one exists.
2. Whether the toggle's granted branch (route 4) survived #292, which changed `OnNotificationButtonClicked`. The sentence holds either way, because route 5 still exists.
3. The body of `NotificationManager.RequestNotificationPermission`. The #263 walkthrough says it opens system settings. It is a settings route either way.
4. What the current iOS level-20 check does when permission is already held. The sentence holds either way.

### Correction to the rev1 reasoning (not a defect)

Rev1 cited #263 rc_4 as the current toggle. That code is from Jul 1 and #292 changed it on Jul 10, so "with no ask" may no longer describe the first-time tap, which runs `Init()`. The fix is still right, because it does not depend on that branch. rev1's C2 row A18 also said "current client is a blob"; the #251, #292 and #327 walkthroughs give later-state evidence it did not use. They are CodeRabbit summaries, not code, so I treat them as secondary.

### New inaccuracy from the edit

None demonstrated. The rev1 sentence was false in the literal sense, and the rev2 sentence is true. Rev2's "or" arms overlap slightly (route 5 runs the same `Init()`), but a true disjunction with overlapping arms is not an error.

## 5. Reopened and reused checks

**Dependencies validated for all REUSED rows.**
- Base: all 16 single-file `shape_source_sha256` values MATCH, including gdrive, gslides, gdocs, gsheets, linear, trello, gcal, github, Slack users and channels, Gmail users and labels, contacts and confluence.
- Slack 4,844/4,844 and Gmail 83,727/83,727 files MATCH by sha256 against their source_manifest.json.
- All 13 services match the universe manifest on file count and bytes. The only files newer than the export are 16 source_manifest.json files dated 2026-10-20, before rev1.
- Snowflake and the bulk gdrive, github and linear files were validated by count and bytes only.
- References: Eval 0 86af2102, injection.json 01ef5792, id_contracts.json fc4711ef, hg_injection_lint.py fec37bce, universe_manifest.json da2f4cf0. Last commit 0d1ba3a (2026-10-31), before rev1, working tree clean.
- SQL overlay: 142 of 145 data statements are byte-identical, and all 8 UPDATEs are among them. Clock unchanged.

**Source reports (sha256).** A = inj_review_A.md 47f4d0ff. B = inj_review_B.md 2e70ff35. C1 = inj_review_C1.md f9216ec4. C2 = inj_review_C2.md d5549411. Report = 0_injection_report.md 338be371. Rev1 failed only on L36, so rows that do not depend on L36 may be reused.

| Check | Status | Source | Reason |
|---|---|---|---|
| Diff and statement inventory | NEW | this review | Done from the files |
| Lint | NEW | this review | Hash changed |
| A: key collisions and parents for L9, L22, L35 | NEW | this review | Changed statements |
| A: Drive shares, "7 emails" now 8 | NEW | A coverage row "Drive users" | Brian is a new reference |
| A: one account per person, Brian | NEW | this review | New reference on the Drive rows |
| A: Drive readability of L9 | NEW | A Advisory 1 | Changed statement. Re-verified 132/132 and the lint path |
| A: collisions for all other keys | REUSED | A coverage table | No key column changed, base hashes match |
| A: ledger rows for 142 unchanged statements | REUSED | A per-statement ledger | Byte-identical, base unchanged |
| A: L11 Sheet readability | REUSED | A Advisory 1 | L11 unchanged, not related to the edit |
| B: statements, quoting, counts, JSON | NEW | this review | Cheap to rerun whole file. Results equal B's totals |
| B: types and schema for 4 edited columns | NEW | this review | Changed values |
| B: generated columns | NEW | lint plus this review | L35 is in scope |
| B: Linear dates, UPDATE targets, order, JSON shapes | REUSED | B rules 5, 7, 8 and shape table | Statements and order unchanged |
| B: columns exist | REUSED | B per-table summary | Column lists proven identical |
| C: deck siblings L9 and L22 | NEW | C1 section 3 row, C1 ledger | The shares changed, so the rev1 "shares equal" result had to be redone |
| C: chronology of L9, L22, L35 | NEW | C1 ledger | Re-read. Stamps unchanged |
| C: Vincent's passes against the sheet | NEW | C1 section 3 | Same subject as the edit |
| C: A6, A13, A14 to A19, C1 | NEW | C2 tables | Depend on L36 or the deck share, or evidence the same subject |
| C: N1, N2 | NEW | C2 notes | Directly addressed by the revision |
| C: injected-to-injected, push permission and deck subjects | NEW | C2 section | Depends on the changed text |
| C: grader language on new text | NEW | this review | New text |
| C: rest of chronology, parents, counters, lifecycle, UPDATE before/after | REUSED | C1 sections 1, 3 to 6 | No timestamp, parent or counter changed. Text-only edit to L36, shares-only to L10 and L23 |
| C: C2 A1 to A5, A7 to A12, A20 to A96 | REUSED | C2 Table A | Grep of C2: only A18, A19, N1 cite L36, and only N2 cites L10. All four are reopened above |
| C: C2 Table B (B1 to B24), Table C except C1 | REUSED | C2 | Unchanged records. Their UNVERIFIABLE and UNSUPPORTED labels carry over, nothing is cleared |
| C: known-issue cards | REUSED | C2 section | Changed statements add no fact on those cards. SC-6 checked here for Brian's address |

## 6. rev1 advisories

| Advisory | Status |
|---|---|
| C2 N1 (L36 "only") | **Resolved.** C2 A19 no longer needs a scope caveat |
| C2 N2 (Brian not on the deck) | **Resolved.** Added on L10, L23, and consistent |
| A Advisory 1 (Drive rule wording, L9 and L11) | Unchanged. Re-judged for L9 with the same result. L11's residual Sheet risk stands |
| A Advisory 2 = C1 A1 = B O4 (L64 reply columns) | Unchanged |
| B A1 (7 columns not in the snapshot) | Unchanged. No edited column is among them |
| B O1 (shared_roles_json shape) | Unchanged in shape. L10 now holds 5 entries |
| B O2, O3 | Unchanged |
| C1 A2 to A6 | Unchanged |
| C2 N3, N4, N5 | Unchanged. N4 still matters to /prompt if the task touches PUSH_NOTIFICATION_STATS |

## 7. New defects

None.

## 8. Note for later stages (outside /injection)

Rev2 changes a fact the solver can read: players who switched notifications on from settings are now scheduled too. The L44 ask "who actually hears from us once they stop playing" may now have a second group, while L15's exclusion applies only to the rule test. I could not check this, because the prompt, OE, rubric and design files are off limits for this review. Whoever runs /prompt should check that any stated audience still matches.

## 9. Limits

- Repo blobs were not read. The 4 UNVERIFIABLE parts above and rev1's 27 remain open.
- CodeRabbit walkthroughs are auto-generated and describe PR heads, the latest from July 2025. No match3d commit after 2025-07-21 mentions notifications or permissions (complete search), but a commit could change the code without saying so.
- Two scanners agree on structure (B's and mine). No real Postgres parser was used.
- `universe_schema_live.json` was used for comparison only. injection.json is an unverified snapshot.
- Snowflake and the bulk gdrive, github and linear files were validated by count and bytes, not by hash.
- Reused rows rest on rev1's ledgers. I did not re-derive them.
- The harness saved one large output of my own command under /home/sumit/.claude/projects/.../tool-results/. I did not open it and re-read that data from my scratchpad. The auto-loaded project memory index was in my context from the start, and no finding relies on it.
