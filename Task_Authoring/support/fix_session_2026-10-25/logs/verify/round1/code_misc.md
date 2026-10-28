## Major

1. **Explicit unknown model labels can be discarded, producing valid provenance.**  
   **File:** `tools/difficulty_stats.py:212–215`  
   **Hunk:** `@@ -162,12 +162,97 @@` — `message_models`

   Both collectors require the model value to be truthy. Consequently, a valid Opus 5.5 init followed by an assistant message containing `"model": ""` produces `valid == "VALID"` and `v3_valid is True`: the empty label never reaches `check_models`. This contradicts the added classifier test, which explicitly classifies `""` as unknown, and the decision that an unrecognised label must never yield valid provenance.

   **Fix:** Distinguish an absent model field from an explicitly supplied empty/null label. Collect explicitly supplied labels even when falsey, and classify them as UNKNOWN. Add a provenance-level test with a valid init plus an explicitly empty assistant model, rather than testing `classify_model("")` alone.

2. **Golden checking can pass despite an absent deciding base record.**  
   **File:** `tools/oracle_kit.py:431–440,445–452`  
   **Hunk:** `@@ -265,22 +430,30 @@` — `check_golden`

   There are two paths around the documented absent-record failure:
   - If any evidence ID exists in the SQL index, `found` is nonempty and no base evidence IDs are queried.
   - For multiple routed base IDs, absence fails only when **none** of their results is a dictionary. If one record exists and another is absent, the existing record can supply the value and the check passes.

   For example, evidence containing `team_ZOM` and `team_NOPE_0000` passes when the value appears in `team_ZOM`, despite the second routed record being absent. The current absent-record test uses only one ID and cannot expose this.

   **Fix:** Partition and account for every evidence ID independently. Query routed base IDs even alongside SQL evidence, and fail on each definitively absent deciding record. Add cases for mixed SQL/base evidence and for two routed base records with one absent.

3. **Failed or incomplete routed golden reads still produce a passing blocking check.**  
   **File:** `tools/oracle_kit.py:386–396,446–453`  
   **Hunks:** `@@ -245,7 +367,36 @@` and `@@ -265,22 +430,30 @@`

   An `hg.py records` error or incomplete scan is added only to `unverified`; the final status depends exclusively on `not wrong`. Thus, all routed base reads can fail and `contract.golden` still reports PASS. Additionally, a nonzero subprocess exit is not rejected when stdout happens to contain parseable JSON.

   This permits the blocking golden check to succeed without performing the required routed-record verification. The allowance for **unrouted** records to remain unverified should not turn failed routed checks green.

   **Fix:** Check the subprocess return code and response structure. Make errors or incomplete results for required routed records blocking—FAIL, or an UNKNOWN outcome that blocks release. Add planted read-error, nonzero-exit, and incomplete-scan tests.

## Minor

4. **Model comparison performs normalization beyond the permitted bracketed suffix removal.**  
   **File:** `tools/difficulty_stats.py:173,179`  
   **Hunk:** `@@ -162,12 +162,97 @@` — `model_id` / `classify_model`

   Both functions call `.strip()`. Therefore, `" claude-opus-5-5 "` is accepted as the expected model, and padded synthetic labels are excluded from checking. That is not exact comparison after stripping **only** a bracketed suffix.

   **Fix:** Preserve whitespace and other characters; remove only the permitted terminal bracketed suffix. Add leading/trailing-whitespace cases through both `check_models` and provenance collection.

5. **The E2E test does not establish that only pending-review proposals were refused.**  
   **File:** `support/fixtures/season_pass_rev14/e2e_rev14.py:211–222`  
   **Hunk:** `@@ -0,0 +1,264 @@` — verdict append assertions

   The asserted refusal result is only the command’s aggregate exit code. With pending proposals present, additional erroneous refusals still satisfy `rc == 1`. The subsequent comparison checks only which families changed, not which records were accepted or how much their priors changed. Losing valid proposals can therefore escape detection if other proposals still touch the same families.

   **Fix:** Assert the exact accepted/idempotent and rejected proposal identities and rejection reasons. Confirm every permitted proposal exists in the resulting ledger and that the rejected set is exactly the pending-review set. Plant an additional erroneous rejection to demonstrate failure.

6. **The F1 assertion does not prove that the current control/channel hand-off contributed to the forecast.**  
   **File:** `support/fixtures/season_pass_rev14/e2e_rev14.py:239–246`  
   **Hunk:** `@@ -0,0 +1,264 @@` — channel-rate assertions

   `ids` includes every control/channel record in the seeded ledger. Checking that forecast record IDs are a subset of that set proves only that they exist somewhere in the ledger. It does not establish the claimed use of the records appended by this replay, nor verify the rate’s eligible model/family sources. A stale-only forecast can satisfy this assertion when matching seeded records are available.

   **Fix:** Track the replay’s accepted side-record identities and verify their expected eligible contributions to each rate, while allowing other eligible records for cross-task pooling. Check the resulting Beta parameters against those contributions. Add a stale-only or wrong-family rate control that must fail.

VERDICT: FAIL