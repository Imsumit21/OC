# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 30 keep the prior `0_injection.md` results (r30 §4 ledger and §6, which carry per-row provenance back through revisions 28, 25, 22, 20, 17, 14, 12, 11, 9 and earlier). See §3. |
| Actual review date | 2026-10-31 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 97,366 bytes, 393 physical lines, sha256 `7966b1496ad972ff3cb125f922660304d110b4ad9b7004e1c40ed9feed20c5b8` (input revision 42, attached as `01_Universe_Inject (22).sql`) |
| Prior SQL compared | revision 30, sha256 `dd7536cd…1c` (upload `(15)`, hash re-verified, PASS). Full `diff` below. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…`; Eval 0 `e034019b…`; known_base_issues.md `79b20289…`; schema/injection.json `31dcb2b4…` (unverified snapshot); id_contracts.json `fc4711ef…`; ENVIRONMENT.md `4ffb2b5f…`; SEARCH.md `cab83c61…`; lint `a8226e2a…`. All re-hashed and unchanged from the r30 review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `7966b149…20c5b8`: 182 statements (BEGIN, 177 INSERT, 3 UPDATE, COMMIT); 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

### Changes from revision 30 (full diff)

1. **Line 54** (Slack DM reply `33c941fa…`, Leonard, 2025-09-30T20:07:18Z): text extended with "and when you comment on the editor only and not shipped ones, put the two builds in the comment (ios 0.3.49 and android 0.3.133) so people can see what you checked against". Keys and thread fields unchanged.
2. **Lines 69 and 77** (Trello card `68daca58…` desc and its `updateCard` action `68dbe36f…` new desc): rule 3 now reads "What is in the store builds and what counts as shipped: Blake's store builds mail **and his reply to it**." No other change.
3. **Gmail "store builds for monday"** (message `<CAAMNAwY…>`, 5 mailbox copies at lines 94, 102, 110, 118, 126; thread rows 92, 100, 108, 116, 124): the editor-strip paragraph was removed from the body (it moved to the second mail); thread snippets now match this message, since it is now the only message in these threads.
4. **Gmail second mail** (message `<CA5_F2rD…>`, 5 mailbox copies at lines 134, 138, 142, 146, 150): moved out of the first thread into **5 new `gmail_threads` rows** (lines 132, 136, 140, 144, 148; ids `<mailbox>/1844695547248825769`, `…249175707`, `…249391903`, `…248700828`, `…249616481`). Subject changed from "Re: store builds for monday" to "editor stuff and ZOM-199, before Monday"; In-Reply-To/References still point at `<CAAMNAwY…>`. New body: (1) the editor/debug-strip rule (moved from mail 1), (2) "the starting tier check in the code is cpm > 90, not >= 90, and it runs when a player's 10th game ends, wins and losses both counted, not after 10 levels cleared. ZOM-199 says >= 90 after the first 10 levels, but the code never changed from the original spec, so 90 exactly stays on tier 0." size_estimate 1361 → 1544.
5. Line numbers from line 94 on differ from revision 30: the five mail-1 bodies now span 5 physical lines each (+20) and the 5 new thread rows add 10 lines, so COMMIT moves from line 363 to 393. Reused rows were matched by content, not line number.

## 2. Input and authority issues

- The attached file differed from saved revision 30, so it was saved as revision 42 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines in revision 42.
- The header comment (line 3) still says "172 INSERT (one row each), 3 UPDATE"; the file now has 177 INSERT. Comments are not data; noted in §7 as a cosmetic advisory.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for every changed/added row (§1 list). REUSED (r30 §4) for byte-identical rows, matched by content (line numbers shifted, §1 item 5). |
| Check A: references, IDs, collisions | NEW: complete Gmail scan for the 5 new thread ids; ZOM-199 / ZOM-42 base reads. REUSED complete results for unchanged keys. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse (lint) plus hand review of the changed Gmail rows. PASS (advisory G1 carried) |
| Check C: dates, relationships, consistency | NEW for every changed text against base Linear (ZOM-199, ZOM-42), the deck, the card/checklist and the DM instruction layers. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 42).

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "172 INSERT (one row each), 3 UPDATE" | lint: 177 INSERT, 3 UPDATE | NEW | Advisory C-1 (stale count; not data) |
| 5 / 393 | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint) | Structure OK |
| 8–16 | gdrive.drive_files ×5 | folder, agenda doc, notes doc, enrage sheet, tiers deck | unchanged | r30 §4 | REUSED | PASS |
| 19, 21 | gdocs.docs_documents ×2 | agenda, "notes for monday" | unchanged | r30 §4 | REUSED | PASS |
| 24–30 | gsheets spreadsheet + 3 sheets | `f_0ba93ae0…` | unchanged | r30 §4 | REUSED | PASS |
| 33–45 | gslides presentation, pages, elements | `f_048bf5e6…` (deck slide line 41: "average CPM over the first 10 levels; 90 or more starts you on tier 1") | unchanged | r30 §4 | REUSED | PASS (A2) |
| 48, 50, 52, 56, 58, 60 | slack.slack_messages ×6 | `6f773865…`, `84ff828e…`, `0282d920…`, `914b21ab…`, `5f6ed4d5…`, `6995ba10…` | unchanged | r30 §4 | REUSED | PASS |
| **54** | slack.slack_messages INSERT (**text changed**) | `33c941fae57ba8d1e23bc1dff9ce3e2c`, ts `1759262838.442871`, `D05HB64NMQU`, EMPLOYEE_0038 (Leonard), reply to `6f773865…` | 18/18 cols/values (lint parse); apostrophes doubled (`don''t`); id, ts, channel, user, thread fields, created_at `2025-09-30T20:07:18.442871Z` unchanged | r30/r28: id absent from complete Slack `messages/*.json` scan; IM with both authors as members. Builds named (iOS 0.3.49, Android 0.3.133) match Blake mail line 96 | NEW (text) / REUSED (keys) | PASS |
| 62 / 63, 65 / 66 | slack bot replies + parent UPDATEs | `5313e8da…`/`1c181040…`, `1491582c…`/`6a42cb69…` | unchanged | r30 §4 | REUSED | PASS |
| **69** | trello.trello_cards INSERT (**desc changed**) | `68daca5871dba40417a00383` | rule 3 adds "and his reply to it"; all other fields unchanged | Decoded desc (2,501 chars) is identical to line 77's `card.desc` | NEW (text) / REUSED (keys) | PASS |
| 71, 73, 75 | trello createCard ×2, DD card | unchanged | r30 §4 | REUSED | PASS (A3) |
| **77** | trello.trello_actions INSERT (**data changed**) | `68dbe36f4b2b4fffb7525fde` updateCard 2025-09-30T14:04:31Z | new desc = line 69 desc; `old.desc` "Rules go here once Blake has confirmed what's in the store builds." unchanged; JSON parses | 14:04:31Z is after both Blake mails (09:12:44Z, 13:26:05Z) | NEW | PASS |
| 79–89 | trello comment, checklist, 2 check items, attachment | unchanged | r30 §4 | REUSED | PASS (G3) |
| **92, 100, 108, 116, 124** | gmail.gmail_threads INSERT (**snippet changed**) | `julia…/1844679607844896665`, `leonard…/1844679607845770780`, `robert…/1844679607845885165`, `brian…/1844679607844988891`, `arthur…/1844679607845878519` | ids unchanged; snippet now = mail 1 snippet; history_id NULL (contract OK) | r30: ids absent from complete Gmail scan | NEW (text) / REUSED (keys) | PASS |
| **94, 102, 110, 118, 126** | gmail.gmail_messages INSERT (**body changed**) | `<mailbox>/<CAAMNAwY…>` ×5 | id, thread_id, labels (recipients INBOX/IMPORTANT/CATEGORY_PERSONAL; Arthur SENT), date 2025-09-30T09:12:44Z, internal_date 1759223564000, headers unchanged; editor paragraph removed | r30 §4 | NEW (text) / REUSED (keys) | PASS |
| **132, 136, 140, 144, 148** | gmail.gmail_threads INSERT (**new**) | `julia.lawson@…/1844695547248825769`, `leonard.hayes@…/1844695547249175707`, `robert@…/1844695547249391903`, `brian.foster@…/1844695547248700828`, `arthur.blake@…/1844695547249616481` | id prefix = user_email; history_id NULL; snippet = mail 2 snippet; each defined once in the SQL | Complete recursive fixed-string scan of all of `gmail/` (81,404 thread files + users/labels/manifest/root) for the five numeric suffixes: **0 matches** (grep exit 1) | NEW | PASS |
| **134, 138, 142, 146, 150** | gmail.gmail_messages INSERT (**changed**) | `<mailbox>/<CA5_F2rD…>` ×5 | thread_id now points at the matching new thread row (julia→…825769, leonard→…175707, robert→…391903, brian→…700828, arthur→…616481, each defined earlier in the SQL); message ids unchanged (r30 complete scan); date 2025-09-30T13:26:05Z = internal_date 1759238765000 = Date header; subject in column and header both "editor stuff and ZOM-199, before Monday"; in_reply_to/references = `<CAAMNAwY…>` (defined at lines 94–126); labels as above; headers JSON parses | ZOM-199 = Linear `/issues/3243`; ZOM-42 = `/issues/3485` | NEW | PASS (C-2, C-3 advisories) |
| 153–161 | gcal.gcal_events ×5 | unchanged (old 123–131) | r30 §4 | REUSED | PASS |
| 164 / 166 / 167 | github PR #401 comment, timeline event, PR UPDATE | unchanged (old 134/136/137) | r30 §4 | REUSED | PASS (A5) |
| 169 / 171 | github review rev_8 + review comment rc_7 on PR #265 | unchanged (old 139/141) | r30 §4 | REUSED | PASS (G1, G2) |
| 174–392 | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495 (old 144–362), incl. ZOM-199 closing note `cmt_c67b7ad4…` "closing. works on the dev build" (line 226) | unchanged | r30 §4 | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | **New keys:** the five new `gmail_threads` ids are absent from the complete base Gmail export (fixed-string scan of every file under `gmail/`, 0 matches for all five numeric suffixes) and each appears once in the SQL. **Changed references:** each `<CA5_F2rD…>` copy's `thread_id` resolves to the new thread row for the same mailbox, inserted earlier in the same transaction; `in_reply_to`/`references` resolve to `<CAAMNAwY…>` (lines 94–126). Gmail `history_id` NULL meets the listed contract. **Named base records:** ZOM-199 (`/issues/3243`, Done) and ZOM-42 (`/issues/3485`, Done) exist. Actors (Arthur Blake sender; Julia, Leonard, Robert, Brian recipients; EMPLOYEE_0038 Leonard; PERSON_6094 Trello member) are unchanged existing accounts. Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All 182 statements parse (lint: 0 `missing_required`, 0 `json_shape`, 0 `generated_column`). Changed Gmail rows keep 22 columns / 22 values; `headers_json` (with the added In-Reply-To/References entries), `label_ids_json`, `to_json` parse as JSON lists; `body_text_fts` not set. Line 77 action data parses as JSON and its desc equals line 69. **Advisory G1 carried** (off-snapshot GitHub columns on lines 169/171). |
| C: Dates, relationships and consistency | **PASS** | **Clock:** new/changed event times 2025-09-30T09:12:44Z, 13:26:05Z, 14:04:31Z, 20:07:18Z are all before 2025-10-01 07:00Z. **Order:** mail 2 (13:26) follows mail 1 (09:12) and opens "Two things I left out of the mail this morning"; the card update that adds "his reply to it" (14:04) comes after both mails; the checklist rule-6 change (16:20) precedes Leonard's 20:07 ask "when you comment on the editor only and not shipped ones", which presupposes it. **Card ↔ action:** desc identical. **Mail facts vs base:** "ZOM-199 says >= 90 after the first 10 levels" matches ZOM-199's title "first 10 level avg CPM" and description "If first 10 level CPM >= 90, then tier 1". "The code never changed from the original spec" matches ZOM-42 (created 2025-04-21, before ZOM-199 on 2025-06-01): "1st 10 level avg CPM > 90 (top 20%) moves to tier 1". The new "10th game ends, wins and losses both counted, not after 10 levels cleared" is Blake's statement about the build; no base record states a different trigger (Linear searches for "10th game", "starting tier", "initial tier", "first 10", "10 games": only ZOM-42/199/3358 hits, none contradicting; GitHub has no starting-tier code). It contradicts only the injected deck (line 41, "first 10 levels"), which the card (rule 5: "where a write-up and the build disagree, go by the build") already frames as a write-up the build overrides. **Builds:** Leonard's "ios 0.3.49 and android 0.3.133" match Blake's mail. **Exclusions:** unchanged from r30 (ZOM-258; 30/49/50/161/262/275; 162/163/201/250 with "no comments on them either"). **Grader-facing text:** none (persona voice). **Base-data conflicts:** SC-1 to SC-3 untouched; no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **C-1 (cosmetic):** header comment line 3 still says "172 INSERT"; the file has 177. Comments are not data, but updating it avoids confusion.
- **C-2, downstream for /prompt and /oe:** mail 2 is a reply by headers (In-Reply-To/References to mail 1) but sits in its own Gmail thread under a new subject with no "Re:". That matches how Gmail splits a thread when the subject changes, so it is not a data defect. But the card's "his reply to it" no longer points at a message inside the "store builds for monday" thread. An agent that opens only that thread will miss the editor-strip rule and the ZOM-199 / starting-tier correction. /prompt should confirm the second mail is discoverable (the subject names ZOM-199, and the body opens with "the mail this morning").
- **C-3, downstream for /oe and /rubric:** the starting-tier facts now have three parts, all taken from mail 2 only: threshold cpm > 90 (90 exactly stays tier 0), the check runs when the 10th game ends, and wins and losses both count. ZOM-42 also says players get "assigned after the first 6-7 levels based on CPM, to be defined later" (pre-existing base wording, not introduced by the SQL). OEs and rubric rows should tie the trigger to Blake's mail and the card's "go by the build", not to ZOM-42 or the deck. Leonard's 20:07 reply now also asks for the two build numbers in each Editor only / Not shipped comment; OEs and the rubric should reflect that if they check comment content.
- **C-4 (cosmetic):** mail 1's body (lines 94–98, all five copies) mixes real line breaks with `\n` escapes inside the `E'...'` string, so each paragraph break is four newlines (three blank lines) instead of two. That's harmless text, but writing the body on one line with `\n\n`, as mail 2 does, keeps it tidy.
- **D7 carried:** the 21:16 exclusion instruction sits under Julia's 9/29 DM thread (discoverability for /prompt).
- **G1, G2, G3, D1–D6 and A1–A5 carried** unchanged from r30/r28/r25.

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `7966b149…20c5b8`, the synth-cut manifest, the complete Gmail fixed-string scan for the five new thread ids, Linear `data.json` `/issues/3243` and `/issues/3485` plus the listed Linear/GitHub text searches (scan_complete), the r30/r28 dependencies (Slack `messages/*.json` id scan, `messages/D05HB64NMQU/*.json`, `channels.json`, `users.json`; GitHub `data.json`; Linear `data.json` `/issues`), the r25 dependencies for reused rows, and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility, Gmail runtime threading and Agent visibility are not certified. The schema snapshot is unverified (G1 carried). Rows byte-identical to revision 30 reuse the prior review's per-row checks under stage-evidence-v1.
