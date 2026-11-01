# /injection — Injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows that are byte-identical to revision 4, taken from the prior `0_injection.md` (sha256 `4aacfaf45b194eef03bbdc0d86ea8b38880ec2b96186db1c633ee561f475abf3`, §4 ledger and §6). See §3. |
| Actual review date | 2026-10-30 |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16. `Evals/references/universes/synthcut/universe_manifest.json` sha256 `da2f4cf0dcf710257ec9016ee48d02fc1ba40ef08c6bee273842ee14a04aac1a`, the same as in the prior review |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 85,712 bytes, sha256 `2fde6b111cd425fdeeab53b0a941f973b2b10b0f512ab88d3ae3451c2fd8deba` (input revision 6, attached to this /injection message as `01_Universe_Inject (3).sql`) |
| Prior SQL compared | revision 4, sha256 `37a8c7ab…5080`. Diff hunks: line 3 (header count 157 → 158 INSERT), line 56 (Trello card desc: rules 1, 4 and 6 rewritten), lines 63–64 (new `updateCard` action), line 254 (ZOM-315 comment body). Every other row is byte-identical; rows after line 62 are shifted by +2 lines. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md sha256 `ee4cd8e1…cd5d`; Eval 0 `e034019b…3eff`; scoring.json `c14873e6…e5bc`; schema injection.json `31dcb2b4…5151` (unverified snapshot); known_base_issues.md `79b20289…7a7b`. All unchanged from the prior review. |
| Lint | `hg_injection_lint.py` injection-lint-v1: 161 statements (BEGIN, 158 INSERT, 1 UPDATE, COMMIT), 0 unparsed. 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above take the place of the injection entry of `input_manifest.json`. This portal allows writes under `reports/` only through the report writer.

## 2. Input and authority issues

- The attached file differed from saved revision 4, so it was saved as revision 6 of the injection input before review.
- The SQL is substantive and parses in full. No Confluence or Snowflake writes.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C done. |
| Inventory every statement and target | NEW for the 3 changed/added rows. REUSED (prior report §4) for byte-identical rows, with line numbers updated. Full ledger in §4. |
| Check A: references, IDs, collisions | NEW for changed/new rows plus a fresh intra-SQL key check. REUSED for unchanged rows. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse; new action's JSON checked against base shape. PASS (advisories carried) |
| Check C: dates, relationships, consistency | NEW for changed rows and their links. **FAIL** (F1) |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): the reused rows are byte-identical in SQL; base manifest, WORKFLOW, Eval 0, scoring and schema hashes and the fixed clock are unchanged. The new rows add one new key (`68dbab2f4b2b4fffb7525fde`), which collides with nothing in the base or the SQL. The changed card text and Linear comment were re-checked against every record they mention, rather than reused.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 6). Base paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/` unless noted.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 5 / 333 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW | Structure OK |
| 8 | gdrive.drive_files INSERT | folder `d_96489e1e00a56685625939` "ZM Difficulty" | parent Leonard's root; Julia writer; created 2025-06-13 | prior §4 line 8 (53,631 drive rows, full load) | REUSED | PASS |
| 10 | gdrive.drive_files INSERT | doc `f_9ec79682ff351aa466364a` | created 09-29, modified 09-30 | prior §4 line 10 | REUSED | PASS |
| 12 | gdrive.drive_files INSERT | sheet `f_0ba93ae0238d9ed4178212` | owner Julia; created 08-26 | prior §4 line 12 | REUSED | PASS |
| 14 | gdrive.drive_files INSERT | slides `f_048bf5e69f8e7f1a659a5c` | owner robert@, created 2025-06-16 | prior §4 line 14 | REUSED | PASS |
| 17 | gdocs.docs_documents INSERT | `f_9ec79682…` | non-empty body_text | prior §4 line 17 | REUSED | PASS |
| 20–26 | gsheets spreadsheet + 3 tabs | `f_0ba93ae0…` | tab grids valid JSON | prior §4 lines 20–26 | REUSED | PASS |
| 29–41 | gslides presentation, 3 pages, 3 elements | `f_048bf5e6…`, `slide_*`, `el_*` | IDs absent from 132 / 2,309 / 2,231 base rows | prior §4 lines 29–41 | REUSED | PASS (advisory A2) |
| 44–50 | slack.slack_messages INSERT ×4 | Leonard DM 09-30 19:48Z; Brian 09-29; Vincent 09-30; Arthur 09-03 | IDs absent (610,468 messages); authors are channel members | prior §4 lines 44–50 | REUSED | PASS |
| 52–53 | slack INSERT reply + UPDATE parent | `5313e8da…` / parent `1c181040…` | reply_count 2→3 | prior §4 lines 52–53 | REUSED | PASS |
| 56 | trello.trello_cards INSERT (**changed**) | `68daca5871dba40417a00383` "Difficulty baseline (Julia)", idShort 80 | New desc: rule 1 "created up to Aug 31 (so everything since we started ZM)"; rule 4 adds the numbers-change carve-out; rule 6 "where Blake's store builds mail **or his reply to it** says a ticket's text is wrong…". dateLastActivity 2025-09-30T15:41:55Z | id/shortLink absence REUSED (prior §4 line 56). Desc equals the `card.desc` of the line-64 action exactly (parsed and compared). | NEW | PASS on A/B; text feeds F1 |
| 58 | trello.trello_actions INSERT | `68daca5845e48874fb98e25a` createCard 2025-09-29T18:05:12Z | ID prefix 0x68daca58 = same second | prior §4 line 58 | REUSED | PASS |
| 60 / 62 | DD card #211 + createCard | `683dbef4…` | 2025-06-02 | prior §4 lines 60, 62 | REUSED | PASS (advisory A3) |
| 64 | trello.trello_actions INSERT (**new**) | `68dbab2f4b2b4fffb7525fde` updateCard **2025-09-30T10:04:31Z**, creator `PERSON_6094_TRELLO_USER_ID` (Leonard Hayes), card 80 | ID prefix 0x68dbab2f = 2025-09-30T10:04:31Z, which matches `date`. data_json keys board/card{desc,id,idShort,name,shortLink}/list/old{desc}, the shape of 267 of the 281 base desc-update actions. old.desc = "…Rules go here once Blake has confirmed what's in the store builds." | id absent: lookup over all 5,252 base actions, scan_complete | NEW | A/B PASS; **C FAIL (F1)** |
| 66 | trello.trello_actions INSERT | `68dbfa4362a051efb5e0ae45` commentCard 2025-09-30T15:41:55Z | after the update; equals card dateLastActivity | prior §4 line 64; id re-checked absent (5,252 actions) | REUSED / NEW id | PASS |
| 69–87 | gmail threads ×5 + messages ×5 | "store builds for monday", Arthur Blake → Julia, Leonard, Robert, Brian; **2025-09-30T09:12:44Z** | body: build versions; editor/debug code stripped from store builds | prior §4 lines 67–85 | REUSED | PASS |
| 88–97 | gmail messages ×5 | "Re: store builds for monday", Arthur Blake, **2025-09-30T13:26:05Z**: "One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90. ZOM-199 says >= …" | In-Reply-To first message | prior §4 lines 86–95 | REUSED | PASS (timestamp used in F1) |
| 99–108 | gcal.gcal_events ×5 | "ZM difficulty tuning" 2025-10-06 (plan field) | created 09-29 | prior §4 lines 97–106 | REUSED | PASS |
| 111 / 113 | github PR comment + timeline event | `match3d#401#c_2` / `#ev_7` | 2025-08-25, after merge | prior §4 lines 109, 111 | REUSED | PASS |
| 254 | linear.linear_comments INSERT (**changed**) | `cmt_98027df98af6fb30b763` on ZOM-315, author `usr_cc3e90160f490686`, 2025-07-02T11:07:32Z: "closing. this is the total attack power in the editor's stats panel, items without cardData now count with their base damage. nothing changes in the game itself" | ZOM-315 (linear/data.json `/issues/3371`): title "Use base damage of item if total attack power excludes items without cardData", assignee `usr_cc3e90160f490686`, Done, started 06-29, completed 07-02T11:16:32Z, so the comment comes 9 min before completion. GitHub (`SynthCut_HarmonyGames_GitHub/.../github/data.json` `/pull_requests/2138`): match3d#257 "Adding 'diff' display for level editor.", head `Blake/levelDiff`, merged 2025-06-30T21:36:10Z. Its review comment `/review_comments/624` is on `Assets/Scripts/LevelEditor/UI/StatsPanel.cs` and uses the total-attack calculation. The comment's "editor's stats panel… nothing changes in the game itself" agrees. Base Linear has 0 comments, so the id cannot collide. | NEW | PASS |
| 115–331 (others) | linear.linear_comments INSERT ×108 | `cmt_*` on ZOM-23 … ZOM-495 | formats, NOT NULL, authors, chronology | prior §4 lines 113–330 | REUSED | PASS (advisories A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run; the lint does not compare dates between records, and that is where F1 is. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | New action `68dbab2f4b2b4fffb7525fde` is absent from all 5,252 base Trello actions (scan_complete) and appears once in the SQL. Its board, card and list resolve to line 56 and the base board. Its creator is Leonard Hayes, one account. The ZOM-315 comment's issue and author exist; the author is the issue's assignee. Intra-SQL: the only repeated first values are the Drive file ids reused across drive/docs/sheets/slides tables, as intended. Unchanged rows reuse prior results. |
| B: SQL structure and supported schema rules | **PASS** | 161 statements parse. The new `data_json` is valid JSON with the base desc-update shape; `date` is a valid timestamptz literal; columns match the snapshot for trello_actions. Provisional advisories A1/A2 carried unchanged. |
| C: Dates, relationships and consistency | **FAIL** | F1: the updateCard action dated 2025-09-30T10:04:31Z writes a desc whose rule 6 refers to Blake's reply to the store builds mail. That reply was sent at 2025-09-30T13:26:05Z, 3 h 21 min later. Everything else checked is consistent: the update comes after Blake's first mail (09:12:44Z), so "once Blake has confirmed" → rules is in the right order; the update comes before the 15:41:55Z commentCard and dateLastActivity. The ZOM-315 comment agrees with ZOM-315 and match3d#257. Rule 1's "everything since we started ZM" agrees with Leonard's DM ("every difficulty ticket since we started zm"). The rule 4 carve-out agrees with Arthur's Sep 3 Slack ("split since match3d#401"). No event timestamp is after the clock. No grader-facing text in the changed rows. |

## 7. Findings

**F1 — Card update quotes a reply that doesn't exist yet (Check C, FAIL)**
- Rule: Check C, supported chronology. A record presented as already written can't refer to a record created after it.
- Record: line 64, `trello.trello_actions` `68dbab2f4b2b4fffb7525fde`, `updateCard`, `date` 2025-09-30T10:04:31Z (the ID's timestamp prefix encodes the same second). Its `card.desc`, which is also the line-56 card desc, rule 6: "where Blake's store builds mail **or his reply to it** says a ticket's text is wrong, comment on that ticket with what the build does".
- Conflicting evidence: the only reply is Arthur Blake's "Re: store builds for monday" (lines 88–97), Date header `Tue, 30 Sep 2025 13:26:05 +0000`. The first mail (09:12:44Z) doesn't announce a follow-up ("Hi all, For Monday … Blake"), and the reply begins "One more, for the rules tab", so it was unprompted. At 10:04 Leonard had no way to refer to "his reply to it" as a definite thing. No other Blake reply to that mail exists in the SQL.
- Effect: the edit that introduces rule 6 is dated before the reply it relies on. Trello's activity log shows the change at 10:04, so an Agent or reviewer reading the history sees impossible ordering.
- Smallest fix: move the update to after 13:26:05Z and before the 15:41:55Z comment, and change the ID's timestamp prefix with it. For example, `id` `68dbe36f4b2b4fffb7525fde` with `date` `'2025-09-30T14:04:31Z'` (0x68dbe36f = 14:04:31Z; this id is free across all 5,252 base actions and the SQL). Nothing else needs to change: the card's dateLastActivity (15:41:55Z) and the comment stay after it. The other option is to drop "or his reply to it" from rule 6 in both line 56 and line 64. That changes what the task authorizes, though, because the ZOM-199 ">= 90" correction is only in the reply.

**Advisories (not failures), carried unchanged from the prior review:**
- A1. `linear.linear_comments.sequence` (109 rows) is not in the unverified snapshot; base Linear has no comments. If the live table lacks it, the whole transaction rolls back. Dropping it is safest.
- A2. `gslides.slides_pages.notes` (all NULL) and `gslides.slides_page_elements.table_json` (all NULL) / `ordinal` (all 0) are absent from both the snapshot and the base export. You lose nothing by dropping them.
- A3. DD decoy card #211 sits in the June 2024 "Rebirth (June)" list. That's odd, but it doesn't contradict anything.
- A4. Minor carried items (comments after `updated_at` on some Todo issues, "wip on a branch" with no branch, gdocs revision_id style, sheet History entry). None is a defect.
- Base-data check: none of the listed synth-cut conflicts (SC-1 to SC-3) touch this SQL.

Prior issues: the prior revision had no updateCard, so a card created 09-29 carried text naming the 09-30 mail. The new action fixes that ordering for the first mail, but its 10:04 date is still too early for the reply (F1).

## 8. Next action and downstream

Re-date the line-64 updateCard (id and date) to after 13:26:05Z, e.g. 14:04:31Z, then rerun `/injection`. Once the SQL changes, any `/prompt`, `/hardness`, `/oe` or `/rubric` result that read an earlier SQL is outdated and must be rerun in order.

### FINAL VERDICT: FAIL

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Change the updateCard action (line 64) to `id` `68dbe36f4b2b4fffb7525fde`, `date` `'2025-09-30T14:04:31Z'` (any time between 13:26:05Z and 15:41:55Z with a matching ID prefix works), then rerun /injection.

Evidence limits: Static review only. No SQL was executed, and live database compatibility is not certified. The schema snapshot is unverified (advisories A1, A2). Rows byte-identical to revision 4 reuse the prior review's per-row checks under stage-evidence-v1, including its Gmail collision coverage over 81,404 thread files and its Slack coverage over 610,468 messages.
