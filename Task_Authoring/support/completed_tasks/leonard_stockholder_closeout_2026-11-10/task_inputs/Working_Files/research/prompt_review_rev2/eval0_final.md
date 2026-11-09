# Injection Data-Integrity Review (Eval 0) — final SQL 65b7c3ec814b

| Item | Value |
|---|---|
| Stage | `/injection` |
| Review version | `injection-static-v2` |
| Mode | Local static delta audit plus whole-file confirmation. No SQL executed. Nothing written under `Evals/`. |
| Universe | `Universe_Normal`; `universe_manifest.json` sha256 `5e01ac4472c8…0de450` |
| Input | `$R/inputs/01_Universe_Inject.sql` |
| Input sha256 | **`65b7c3ec814b2c2b39a06fb0431873d44678ef05daf94a786b25cf95c0ce2579`** |
| Compared against | `$R/prev/01_Universe_Inject.bd67fedbbd47.sql`, which passed Eval 0 (`$R/out/eval0_rev2b.md`) |
| Statements | 149: BEGIN, 132 INSERTs, 15 UPDATEs, COMMIT |
| Lint | `hg.py lint` on the new file (read-only; universe normal; clock 2026-02-14T00:00:00Z): **0 FAIL / 0 CHECK / 0 INFO**, flags `[]`, info `[]` |

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/c183cff7-226e-4dae-964a-0d311047e48a/scratchpad/prompt_review_rev2`.

## Whole-file confirmation

I compared the two files statement by statement. 146 of the 149 statements are byte-identical to bd67fedbbd47, which passed `eval0_rev2b.md`, so their results carry over. No statement was added or removed, and the 14 SQL comment lines are unchanged.

Every one of the 132 INSERTs has equal column and value counts, and no INSERT key is repeated. The lint is clean.

Only the three rows below changed. For each, I compared every field and found no other differences.

## Delta ledger

| Line | Table / record | Field changed | Check |
|---|---|---|---|
| L18–19 | `gdocs.docs_documents` `f_a37b403d5200d4f0a31d31` "Stockholder close-out notes" | `body_text`: inserted ". Finish my draft one in the folder rather than starting another" (64 chars) after "the notes and everything else run off it". `style_runs_json`: NORMAL_TEXT end 2082 → 2146. | Decoded body = **2,146** characters = the new style-run end; the TITLE run 0–28 is unchanged and the JSON parses. "my draft one in the folder" refers to an existing record: `f_5ecaa967db3adcfa440b09` "Holder list (draft)" (L13–14, L24, L26), whose parent is the close-out folder `d_601064334a0b493022fe83`. That folder holds exactly one sheet (L8–16). PASS |
| L115 | `gmail.gmail_messages` `…/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com>` (Calvin Price's forward) | `headers_json` Date: "Tue, 03 Feb 2026 08:20:44 -0800" → "**Tue, 03 Feb 2026 10:20:44 -0600**" | Parses to 2026-02-03T16:20:44Z, which equals `date` and `internal_date` 1770135644000. Feb 3, 2026 is a Tuesday. The -0600 offset matches Calvin's base calendar: `gcal/data.json` /calendars/3 `calvin.price@harmonygames.co` has `time_zone` "America/El_Salvador" (UTC-6, no daylight saving). Nothing else in the row changed. PASS |
| L119 | `gmail.gmail_messages` `…/<170056300100.11.4471902385519067321@notifications-worker-75f77576db-lb9sh>` (Carta digest for Nov. 20, 2023) | `label_ids_json`: `["INBOX","Label_b19fb8d1b3","CATEGORY_UPDATES"]` → `["INBOX","IMPORTANT","Label_b19fb8d1b3","CATEGORY_UPDATES"]` | The JSON parses, and the label set now equals both base digests (`leonard.hayes@harmonygames.co/1782897835407336831` and `/1790417238097762434`: INBOX, IMPORTANT, Label_b19fb8d1b3, CATEGORY_UPDATES). This resolves the label observation from `eval0_rev2b.md`. Message-ID, thread, date, snippet and size are unchanged. PASS |

## Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | No IDs changed. The doc's new sentence refers to an existing SQL sheet in the stated folder. The 146 unchanged statements, and their collision checks, carry over from `eval0_rev2b.md`. |
| B — SQL structure and supported schema rules | PASS | Lint is clean. Column and value counts are equal, the changed JSON fields parse, no generated columns are set and no keys are duplicated. The snapshot comparison and advisory O-1 are unchanged. |
| C — Dates, relationships and consistency | PASS | Body length equals the style-run end. Calvin's Date header equals `date` and `internal_date`, and the offset matches his base calendar timezone. The digest labels match the base digests. No changed text is addressed to a grader or written as padding. |

Context for /prompt (non-blocking): the new instruction "Finish my draft one in the folder rather than starting another" adds a constraint on where the solver writes. /prompt owns that decision.

No defects to repair.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt.

Evidence limits:
- **Static review only.** The SQL was not executed, and the schema snapshot is unverified. Advisory O-1 (4 columns from unchanged rows that the snapshot lacks) still applies.
- **Uniqueness scope.** Uniqueness is checked against the local base plus the SQL only.
- **Agent visibility.** Visibility for Leonard is outside this stage.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
