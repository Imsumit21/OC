# Injection Data-Integrity Review (Eval 0) — SQL rev12

| Item | Value |
|---|---|
| Stage | `/injection` |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` |
| Mode | Local static audit. No SQL executed. Nothing written under `Evals/`. |
| Universe | `Universe_Normal`. Manifest sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`. |
| Input | `$R/inputs_rev12/01_Universe_Inject.sql` |
| Input sha256 | **`fd51afbf63aa2d05631c5f21a61d2966003389c093ce46b6c530511a1d30dec2`** |
| Statements | 140: BEGIN, 125 INSERTs, 13 UPDATEs, COMMIT |
| Lint | 0 FAIL / 0 CHECK / 0 INFO |

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/prompt_review_rev1`.

## Reuse

All 138 statements of rev11 are present unchanged in rev12, checked by statement-level parse comparison. Their checks carry over from `$R/out/eval0_rev11.md` (PASS, sha256 `40ce7bef…1cc1`).

The only additions are 2 UPDATEs, at L109 and L110.

## New statements

| Line | Target | Check |
|---|---|---|
| L109 | UPDATE `gmail.gmail_messages` SET `body_text` WHERE `id = 'arthur.blake@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>'` | The target exists, once, in `threads/blake@harmonygames.co_1816806726955267951.json` (thread `arthur.blake@harmonygames.co/1816806726955267951`). After decoding the E-literal, the new body equals the base body with only `'\n         (Total ownership percentage adds to 100%).'` removed. That is one occurrence and 52 characters (7,936 → 7,884). Nothing else differs. PASS |
| L110 | UPDATE `gmail.gmail_messages` SET `body_text` WHERE `id = 'leonard.hayes@harmonygames.co/<CAPBs_a6zM=or+nDw0YSrZ3Rmkvzr0fnVHNBaaRqx6vN6Uxrs_Q@mail.gmail.com>'` | The target exists, once, in `threads/leonard@harmonygames.co_1816809274978043917.json` (msg 0). Same exact result: 7,926 → 7,874, with only that sentence removed. PASS |

### Why the removed sentence is wrong

The base claim is that ownership "adds to 100%", but the 27 listed percentages sum to 94.13%. Removing it is consistent with the injected sheet note "only add to about 94%".

### Side effects

- **Snippets are unaffected.** The edit is near the end of the body, while snippets come from the opening ("Hi [PERSON_NAME_0613], Thank you…").
- **`body_text` is not a generated column.** The generated `body_text_fts` column is not set.

## Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | Both UPDATE targets exist in their base threads, with exact single-ID predicates. |
| B — SQL structure and supported schema rules | PASS | Lint and the independent parse are clean. Advisory O-1 remains: 4 columns are absent from the unverified snapshot (`slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, `linear_projects.links_json`). |
| C — Dates, relationships and consistency | PASS | The edits remove a claim that the base's own figures contradict. No dates or relationships change. |

## Pre-existing context (non-blocking, for /prompt)

The same owner list survives in base Slack with the sentence intact: `slack/messages/C04UEQVDVB7/2024-11.json` /55, Leonard, ts 1732646280.941869, still contains "(Total ownership percentage adds to 100%)".

This is pre-existing base content and was not introduced by the SQL. A reader of the Slack copy would still see the 100% claim.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt.

Evidence limits:
- Static review only; the schema snapshot is unverified and 4 of the columns used are not in it.
- The Slack copy of the owner list still carries the 100% sentence. This is base context, not a defect introduced by the SQL.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
