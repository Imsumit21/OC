# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 42 keep the prior `0_injection.md` results (r42 §4 ledger and §6, which carry per-row provenance back through revisions 30, 28, 25, 22, 20, 17, 14, 12, 11, 9 and earlier). See §3. |
| Actual review date | 2026-10-31 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 98,831 bytes, 397 physical lines, sha256 `f6afeda7b08647d790a5d96b5bd7ccb2cb6291d83fadf4bd9f2ae2a79f5362f8` (input revision 45, attached as `01_Universe_Inject (23).sql`) |
| Prior SQL compared | revision 42, sha256 `7966b149…20c5b8` (upload `(22)`, PASS). Full `diff` below. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…`; Eval 0 `e034019b…`; known_base_issues.md `79b20289…`; schema/injection.json `31dcb2b4…` (unverified snapshot); id_contracts.json `fc4711ef…`; ENVIRONMENT.md `4ffb2b5f…`; SEARCH.md `cab83c61…`; lint `a8226e2a…`. All re-hashed this run and unchanged from the r42 review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `f6afeda7…62f8`: 184 statements (BEGIN, 179 INSERT, 3 UPDATE, COMMIT); 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

### Changes from revision 42 (full diff: 4 hunks)

1. **Line 3** (header comment): "172 INSERT" → "179 INSERT". Now matches the file (resolves advisory C-1).
2. **Lines 47–50 (new):** two `slack.slack_messages` INSERTs in the group DM `CAFC495E4006`:
   - `cec246a6e43158f200fe144f0dd7039c`, ts `1759226461.318204`, Leonard Hayes (EMPLOYEE_0038), 2025-09-30T10:01:01Z: "robert anything you want on julia's difficulty list for monday? she's putting it together from the card". Thread parent: reply_count 1, reply_users_count 1, latest_reply `1759229513.774912`.
   - `abe096ff0b5d7216efbc889e91d6d13a`, ts `1759229513.774912`, Robert (EMPLOYEE_0016), 2025-09-30T10:51:53Z, reply to `cec246a6…`: "yeah three things after status please. who it's assigned to in linear, the day it got marked done (leave it blank if it never got done), and its linear priority. i want to sort by them in the session".
3. **Line 73** (Trello card `68daca58…` desc) and **line 81** (its `updateCard` action `68dbe36f…` new desc): rule 2 now ends "Layout as in the session agenda, **plus the three things Robert asked for when I asked him in our group chat**." No other change.
4. Every line from 48 on shifts by +4 from revision 42 (COMMIT 393 → 397). Reused rows were matched by content.

## 2. Input and authority issues

- The attached file differed from saved revision 42, so it was saved as revision 45 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines in revision 45.
- Search-helper note: `hg_records.py` (for `channels.json`) and `hg_search.py lookup` (for `messages/*.json`) returned "source changed during read" errors although `channels.json` hashed twice to its manifest value `3cca0f7e…`. The channel record the helper returned was used after that hash check; the message-ID collision check was redone as a complete fixed-string `grep -rlF` over the whole Slack export (4,840 message files plus root files). Coverage below is from that scan.

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 2 added Slack rows and 2 changed Trello rows. REUSED (r42 §4) for byte-identical rows, matched by content (+4 line shift). |
| Check A: references, IDs, collisions | NEW: channel/user/Trello-member resolution; complete Slack scan for the 2 new ids and ts values; in-SQL uniqueness. REUSED complete results for unchanged keys. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse (lint) plus hand review of the new Slack rows against the `slack_messages` snapshot; card ↔ action desc equality. PASS (advisory G1 carried) |
| Check C: dates, relationships, consistency | NEW for the new messages and card text against the card's create/update actions, the agenda doc, and the Linear fields Robert names. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 45). Revision-42 line in brackets where shifted.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "179 INSERT (one row each), 3 UPDATE" | lint: 179 INSERT, 3 UPDATE | NEW | OK (C-1 resolved) |
| 5 / 397 [393] | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint) | Structure OK |
| 8–16 | gdrive.drive_files ×5 | folder, agenda doc, notes doc, enrage sheet, tiers deck | unchanged | r42 §4 | REUSED | PASS |
| 19, 21 | gdocs.docs_documents ×2 | agenda, "notes for monday" | unchanged | r42 §4 | REUSED | PASS |
| 24–30 | gsheets spreadsheet + 3 sheets | `f_0ba93ae0…` | unchanged | r42 §4 | REUSED | PASS |
| 33–45 | gslides presentation, pages, elements | `f_048bf5e6…` | unchanged | r42 §4 | REUSED | PASS (A2) |
| **48** | slack.slack_messages INSERT (**new**) | `cec246a6e43158f200fe144f0dd7039c`, ts `1759226461.318204`, channel `CAFC495E4006`, EMPLOYEE_0038 | 18 cols / 18 values; thread parent (thread fields NULL, reply_count 1, reply_users_count 1, latest_reply = line 50 ts); created_at `2025-09-30T10:01:01.318204Z` = ts; JSON lists `[]`, metadata `{}`; `text_fts` not set | `channels.json` `/307`: `CAFC495E4006` = `mpdm-robert--leonard.hayes--julia.lawson-1`, is_mpim, members EMPLOYEE_0005 (Julia), 0016 (Robert), 0038 (Leonard), PERSON_6089. `users.json` `/23` EMPLOYEE_0038 = Leonard Hayes. Id and ts: 0 matches in a complete `grep -rlF` of the Slack export; each appears only at lines 48/50 in the SQL (id ×2: own row + line 50's parent ref) | NEW | PASS |
| **50** | slack.slack_messages INSERT (**new**) | `abe096ff0b5d7216efbc889e91d6d13a`, ts `1759229513.774912`, `CAFC495E4006`, EMPLOYEE_0016 | 18/18; thread_parent_id = `cec246a6…`, thread_ts_legacy = parent ts (both defined at line 48, earlier in the transaction); reply_count 0; created_at `2025-09-30T10:51:53.774912Z` = ts; apostrophes doubled | `users.json` `/9` EMPLOYEE_0016 = Robert (robert@harmonygames.co), a channel member. Id/ts absent from the complete Slack scan; id appears once in the SQL | NEW | PASS |
| 52, 54, 56, 58, 60, 62, 64 [48–60] | slack.slack_messages ×7 | `6f773865…`, `84ff828e…`, `0282d920…`, `33c941fa…`, `914b21ab…`, `5f6ed4d5…`, `6995ba10…` | unchanged | r42 §4 | REUSED | PASS |
| 66 / 67, 69 / 70 [62–66] | slack bot replies + parent UPDATEs | `5313e8da…`/`1c181040…`, `1491582c…`/`6a42cb69…` | unchanged | r42 §4 | REUSED | PASS |
| **73** [69] | trello.trello_cards INSERT (**desc changed**) | `68daca5871dba40417a00383` | rule 2 adds "plus the three things Robert asked for when I asked him in our group chat"; all other fields unchanged | Decoded desc (2,576 chars) is identical to line 81's `card.desc` | NEW (text) / REUSED (keys) | PASS |
| 75, 77, 79 [71–75] | trello createCard ×2, DD card | createCard `68daca58…45e48874…` 2025-09-29T18:05:12Z by PERSON_6094 | unchanged | r42 §4 | REUSED | PASS (A3) |
| **81** [77] | trello.trello_actions INSERT (**data changed**) | `68dbe36f4b2b4fffb7525fde` updateCard 2025-09-30T14:04:31Z, PERSON_6094 | new desc = line 73 desc; `old.desc` unchanged; JSON parses | `trello/data.json` `/members/2`: PERSON_6094 = Leonard Hayes, so "I asked him in our group chat" = Leonard's line 48 message (10:01Z), which precedes this update | NEW | PASS |
| 83–93 [79–89] | trello comment, checklist, 2 check items, attachment | unchanged | r42 §4 | REUSED | PASS (G3) |
| 96, 104, 112, 120, 128 [92–124] | gmail.gmail_threads ×5 (mail 1) | unchanged | r42 §4 | REUSED | PASS |
| 98, 106, 114, 122, 130 [94–126] | gmail.gmail_messages ×5 (mail 1 `<CAAMNAwY…>`) | unchanged | r42 §4 | REUSED | PASS |
| 136, 140, 144, 148, 152 [132–148] | gmail.gmail_threads ×5 (mail 2) | unchanged | r42 §4 (complete Gmail scan) | REUSED | PASS |
| 138, 142, 146, 150, 154 [134–150] | gmail.gmail_messages ×5 (mail 2 `<CA5_F2rD…>`) | unchanged | r42 §4 | REUSED | PASS (C-2, C-3) |
| 157–165 [153–161] | gcal.gcal_events ×5 | unchanged | r42 §4 | REUSED | PASS |
| 168 / 170 / 171 [164–167] | github PR #401 comment, timeline event, PR UPDATE | unchanged | r42 §4 | REUSED | PASS (A5) |
| 173 / 175 [169/171] | github review rev_8 + review comment rc_7 on PR #265 | unchanged | r42 §4 | REUSED | PASS (G1, G2) |
| 178–396 [174–392] | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495 | unchanged | r42 §4 | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | **New keys:** message ids `cec246a6…` and `abe096ff…` and ts `1759226461.318204` / `1759229513.774912` have 0 matches in a complete fixed-string scan of the whole Slack export (`grep -rlF`, exit 1; 4,840 `messages/*/*.json` files plus root files). Each is defined once in the SQL. **References:** channel `CAFC495E4006` exists (mpim of Julia, Robert, Leonard, PERSON_6089); both authors are members and existing accounts (EMPLOYEE_0038 Leonard Hayes, EMPLOYEE_0016 Robert; no second accounts). The reply's thread_parent_id/thread_ts_legacy resolve to line 48. The card update's actor PERSON_6094 is Leonard Hayes (Trello `/members/2`). Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All 184 statements parse (lint: 0 `missing_required`, 0 `json_shape`, 0 `generated_column`). New Slack rows: 18 columns / 18 values; all NOT NULL snapshot columns supplied (id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions/files/attachments `[]`, created_at, metadata_json `{}`); `text_fts` omitted. Line 81 action data parses as JSON and its desc equals line 73 (verified by decoding both). **Advisory G1 carried** (off-snapshot GitHub columns on lines 173/175). |
| C: Dates, relationships and consistency | **PASS** | **Clock:** new times 2025-09-30T10:01:01Z and 10:51:53Z are before 2025-10-01 07:00Z. **Order:** the card exists from 2025-09-29T18:05:12Z (createCard; old desc already "Julia owns this one"), so Leonard's 10:01Z "she's putting it together from the card" has its referent. Robert's reply follows the parent by 51 minutes. The card update that cites "the three things Robert asked for when I asked him in our group chat" (14:04:31Z) comes after both messages, and its author (Leonard) is the one who asked in the group DM. **Fit with other records:** the agenda (line 19) asks for "one sheet with two tabs, Tickets and Rules in force"; card rule 2 lists the columns, and Robert's "three things after status" adds to them without contradicting any of them. **Facts vs base:** the fields Robert names exist on every candidate ZOM issue in Linear `data.json` (`assignee_id`, `completed_at`, `priority`): all 38 ZOM keys in the task's record set have an assignee and a nonzero priority. Done issues have `completed_at`; the In Progress (202), Todo (293), Duplicate (203, 276) and Canceled (280) ones have none, so "leave it blank if it never got done" is answerable. **Grader-facing text:** none (persona voice). **Base-data conflicts:** SC-1 to SC-3 untouched; no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **C-5, new, downstream for /oe and /rubric (the day it was marked done):** Robert's "the day it got marked done" is persona-written, so it means a PT day. Three possible register tickets were completed after 00:00 UTC, so their PT day is one day before their UTC date: **ZOM-200** `2025-06-13T01:17:38Z` (June 12 PT), **ZOM-274** `2025-06-21T01:17:25Z` (June 20 PT), **ZOM-282** `2025-06-21T01:17:19Z` (June 20 PT). ZOM-50, 163, 262 and 275 are in the same position but are excluded by Leonard's lists. OEs and rubric rows that check the done date should use the PT date or accept both dates for these three.
- **C-6, new, downstream for /prompt (where Robert's columns live):** the three extra columns are stated only in the group DM `CAFC495E4006`; the card just points to "our group chat". Julia is a member, so she can read it, but the agent has to find that thread. /prompt should confirm it is discoverable. Also, Leonard's "notes for monday" doc opens with "julia, three things for the register:" (a different three things: ZOM-258, Arthur's access, which ticket replaced which). That's not a data conflict, but OEs and the rubric should keep the two lists apart.
- **C-7 (cosmetic):** the two new messages are at 03:01 and 03:51 PT. Unusual hours are not a defect (Eval 0). If they are moved, both must stay before the 14:04:31Z card update that cites them (for example 13:00Z and 13:45Z, about 6:00 and 6:45 AM PT).
- **C-2, C-3, C-4, D7 carried** from r42 (mail 2 in its own thread; starting-tier facts from mail 2 only; mail 1 newline spacing; 21:16 exclusion under Julia's 9/29 DM thread).
- **G1, G2, G3, D1–D6 and A1–A5 carried** unchanged from r42/r30/r28/r25.
- **C-1 resolved** (header count now correct).

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `f6afeda7…62f8`, the synth-cut manifest, Slack `channels.json` (sha256 `3cca0f7e…`, `/307`), `users.json` (`/9`, `/23`), the complete fixed-string scan of the Slack export for the two new ids and ts values, Trello `data.json` `/members/2`, Linear `data.json` `/issues` (ZOM assignee/priority/completed_at/state fields), the r42 dependencies (complete Gmail scan for the five mail-2 thread ids; Linear `/issues/3243`, `/issues/3485` and the listed Linear/GitHub text searches), the r30/r28/r25 dependencies for reused rows, and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility, Slack/Gmail runtime threading and Agent visibility are not certified. The schema snapshot is unverified (G1 carried). Rows byte-identical to revision 42 reuse the prior review's per-row checks under stage-evidence-v1. The Slack id collision check used a complete fixed-string scan because the indexed helpers reported transient source-change errors.
