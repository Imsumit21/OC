# /injection: injection data-integrity review

## 1. Scope

| Field | Value |
|---|---|
| Review | `/injection`, chat review of attempt 6adfee3ef9092601a61245bb, audit mode |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1`. reused_evidence: rows byte-identical to revision 45 keep the prior `0_injection.md` results (r45 §4 ledger and §6, which carry per-row provenance back through revisions 42, 30, 28, 25, 22, 20, 17, 14, 12, 11, 9 and earlier). See §3. |
| Actual review date | 2026-10-31 (UTC) |
| Clock | Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) |
| Universe | `Universe_SynthCut`, hg4-synth-sep30cut v16, unchanged |
| Input | `Evals/task_inputs/01_Universe_Inject.sql`, 102,725 bytes, 406 physical lines, sha256 `b64bc2f2c6dc834cb1c326903d30c21d625709e97285da4e4e71d48f911eec23` (input revision 48, attached as `01_Universe_Inject (24).sql`) |
| Prior SQL compared | revision 45, sha256 `f6afeda7…62f8` (upload `(23)`, PASS). Full `diff` below. |
| Assignment (context only) | Julia Lawson, Product Manager; Product; Engineering Ops; Retrieval; long-horizon |
| References | WORKFLOW.md `ee4cd8e1…`; Eval 0 `e034019b…`; known_base_issues.md `79b20289…`; schema/injection.json `31dcb2b4…` (unverified snapshot); id_contracts.json `fc4711ef…`; ENVIRONMENT.md `4ffb2b5f…`; SEARCH.md `cab83c61…`; lint `a8226e2a…`. All re-hashed this run and unchanged from the r45 review. |
| Lint | `hg_injection_lint.py` (injection-lint-v1) on sha256 `b64bc2f2…ec23`: BEGIN, 183 INSERT, 4 UPDATE, COMMIT; 0 FAIL / 0 CHECK / 0 INFO |

Manifest note: the review version, evidence contract, input hash and source provenance above stand in for the injection entry of `input_manifest.json` (`review_version: injection-static-v2`). This portal allows writes under `reports/` only through the report writer.

### Changes from revision 45 (full diff: 4 hunks)

1. **Line 3** (header comment): "179 INSERT …, 3 UPDATE" → "183 INSERT …, 4 UPDATE". Matches the file (lint: 183 INSERT, 4 UPDATE).
2. **Line 50** (Robert's group-DM reply `abe096ff…`): text now reads "the day it got marked done, **pacific time** (leave it blank if it never got done)". No other field changed.
3. **Lines 71–75 (new):** in `C093LEZGF6J` (GitHub notifications for match3d), two GitHub-bot (`SLACK_BOT_0004`) thread replies under PR #271's "Pull request opened" parent `2e34453f…`:
   - `f590e554c3b5e1d6b01cc9d1395388eb`, ts `1751591124.205377` (2025-07-04T01:05:24Z): "Review approved by arthur.blake on owen.baker's pull request", title link `#pullrequestreview-2984501722`.
   - `e7977b0f608c8af00f33c4744ab7ea1f`, ts `1751591125.638214` (01:05:25Z): "Comment on #271" by arthur.blake, link `#discussion_r2184401907`, text "not tiers: this is a bug fix, enrage was always meant to clear on refill health and push back. no tier version or enrage number changes here. leave it out when we list tier work".
   - `UPDATE slack.slack_messages SET reply_count = 6 WHERE id = '2e34453f…'`.
4. **Lines 181–184 (new):** `github.github_reviews` `harmonygames-Games/match3d#271#rev_2` (EMPLOYEE_0025, APPROVED, empty body, 2025-07-04T01:05:22Z, commit `2f1c9a22…`, seq 2) and `github.github_review_comments` `…#271#rc_1` (same author and text as the Slack comment; `Assets/Scripts/Monster/MonsterSpawner.cs`, line 528, review id `…#rev_2`).
5. Lines 51–70 are unchanged; lines after 70 shift +5 and lines after 180 shift +9 from revision 45 (COMMIT 397 → 406). Reused rows were matched by content.

## 2. Input and authority issues

- The attached file differed from saved revision 45, so it was saved as revision 48 of the injection input before review.
- The SQL is substantive and parses in full. It makes no Confluence or Snowflake writes.
- Line numbers are physical (`\n`) lines in revision 48.
- Base reads this run: GitHub `data.json` (33.6 MB, loaded directly; PR #271 and all its reviews, review comments, PR comments, timeline events and commits; complete id scans of `/reviews` and `/review_comments`; whole-file fixed-string counts), Slack `messages/C093LEZGF6J/2025-07.json` (parent and all replies), a complete fixed-string `grep -rlF` over the whole Slack export (4,845 JSON files) for the new ids, ts values and URL numbers, and Linear `data.json` `/issues` (ZOM-295).

## 3. Checklist

| Item | Status |
|---|---|
| Save/reload SQL; hash, base manifest, review version | NEW, done |
| Run lint; resolve every flag | NEW: 0 flags. Checks A–C still run below. |
| Inventory every statement and target | NEW for the 2 Slack rows, 1 Slack UPDATE, 2 GitHub rows and the changed line 50/line 3. REUSED (r45 §4) for byte-identical rows, matched by content. |
| Check A: references, IDs, collisions | NEW: parent message, PR, author, commit resolution; complete Slack and GitHub collision scans; in-SQL uniqueness. REUSED complete results for unchanged keys. PASS |
| Check B: SQL structure, supported schema rules | NEW whole-file parse (lint), JSON parse of both new attachments, column review against the snapshot. PASS (advisory G1 extended to lines 182/184) |
| Check C: dates, relationships, consistency | NEW for the review/comment against PR #271 history, the Slack thread counts, ZOM-295, the card's scope rule and Robert's changed text. PASS |
| Coverage, findings, limits, one verdict | NEW, below |

Reuse basis (stage-evidence-v1): reused rows are byte-identical. The base manifest, WORKFLOW, Eval 0, known_base_issues, schema snapshot, id contracts and fixed clock are unchanged.

## 4. Operation ledger

Lines refer to `01_Universe_Inject.sql` (revision 48). Revision-45 line in brackets where shifted.

| Line(s) | Table / op | Record(s) | Key values checked | Base evidence | Verif. | Result |
|---|---|---|---|---|---|---|
| 3 | comment | header | "183 INSERT (one row each), 4 UPDATE" | lint: 183 INSERT, 4 UPDATE | NEW | OK |
| 5 / 406 [397] | BEGIN / COMMIT | one transaction | all statements commit or roll back together | — | NEW (lint) | Structure OK |
| 8–45 | gdrive ×5, gdocs ×2, gsheets 1+3, gslides 1+3+3 | unchanged | unchanged | r45 §4 | REUSED | PASS (A2) |
| 48 | slack.slack_messages | `cec246a6…` (Leonard, group DM) | unchanged | r45 §4 | REUSED | PASS |
| **50** | slack.slack_messages INSERT (**text changed**) | `abe096ff0b5d7216efbc889e91d6d13a` | only `text` changed: adds ", pacific time"; apostrophe still doubled; all keys unchanged | r45 §4 keys (complete Slack scan) | NEW (text) / REUSED (keys) | PASS |
| 52–70 | slack ×7, bot replies + 2 parent UPDATEs | unchanged | unchanged | r45 §4 | REUSED | PASS |
| **72** | slack.slack_messages INSERT (**new**) | `f590e554c3b5e1d6b01cc9d1395388eb`, ts `1751591124.205377`, `C093LEZGF6J`, SLACK_BOT_0004 | 18 cols / 18 values; thread_parent_id `2e34453f…`, thread_ts_legacy `1751588271.756019` = parent ts; created_at `2025-07-04T01:05:24.205377Z` = ts; attachment JSON parses; attachment ts 1751591122 = rev_2 submitted_at; `text_fts` not set | Parent `2e34453f…` in `messages/C093LEZGF6J/2025-07.json` is the bot's "Pull request opened by owen.baker" for #271 (ts `1751588271.756019`). Format (color `36a64f`, fallback/pretext "Review approved by … on owen.baker's pull request", title "Review on #271 …", title_link `#pullrequestreview-…`) matches base approvals, e.g. `4ad5e8ab…` for #258. Id, ts and `2984501722`: 0 matches in the complete Slack scan and in GitHub `data.json`; each once in the SQL | NEW | PASS |
| **74** | slack.slack_messages INSERT (**new**) | `e7977b0f608c8af00f33c4744ab7ea1f`, ts `1751591125.638214` | 18/18; same thread fields; created_at = ts; attachment JSON parses; pretext/fallback "Comment on #271" format matches base inline-comment notices (e.g. `81563893…` `#discussion_r…`) | Id, ts and `2184401907`: 0 matches in the complete Slack scan and GitHub `data.json`; once in the SQL | NEW | PASS |
| **75** | slack.slack_messages UPDATE (**new**) | parent `2e34453f…` reply_count 4 → 6 | Base parent: reply_count 4, reply_users_count 1, latest_reply `1751635772.012369`. Base replies: `2f43ee6c…`, `5074910c…`, `18f605df…`, `cbf291bd…`, all SLACK_BOT_0004. Adding two bot replies gives 6, reply_users stays 1, and latest_reply stays (new ts precede `1751635772…`); so leaving those fields alone is correct | NEW | PASS |
| 78–98 [73–93] | trello card, createCard ×2, DD card, updateCard, comment, checklist, check items, attachment | unchanged | unchanged | r45 §4 | REUSED | PASS (A3, G3) |
| 101–159 [96–154] | gmail.gmail_threads ×10, gmail.gmail_messages ×10 | unchanged | unchanged | r45 §4 | REUSED | PASS (C-2, C-3) |
| 162–170 [157–165] | gcal.gcal_events ×5 | unchanged | unchanged | r45 §4 | REUSED | PASS |
| 173 / 175 / 176 [168–171] | github PR #401 comment, timeline event, PR UPDATE | unchanged | unchanged | r45 §4 | REUSED | PASS (A5) |
| 178 / 180 [173/175] | github review rev_8 + review comment rc_7 on PR #265 | unchanged | unchanged | r45 §4 | REUSED | PASS (G1, G2) |
| **182** | github.github_reviews INSERT (**new**) | `harmonygames-Games/match3d#271#rev_2` | pr_id resolves to PR #271 (merged, created 2025-07-04T00:17:49Z, merged 13:29:30Z); author EMPLOYEE_0025 = Arthur Blake (`/users`, arthur.blake@harmonygames.co), a requested reviewer (timeline `#271#ev_4`, 00:36:36Z); commit `2f1c9a22…` = PR head_sha and `#271#c_1` in pull_request_commits; base #271 has only `rev_1` (CodeRabbit), so `rev_2` / seq 2 continue the sequence. Id: 0 matches across all 2,230 `/reviews` and 1,387 `/review_comments` ids | NEW | PASS (G1) |
| **184** | github.github_review_comments INSERT (**new**) | `harmonygames-Games/match3d#271#rc_1` | Base #271 has no review comments, so `rc_1` is free (0 matches in complete id scan); pull_request_review_id = line 182 id (defined earlier in the transaction); path `Assets/Scripts/Monster/MonsterSpawner.cs` is a PR #271 file (CodeRabbit walkthrough `#271#c_2`); hunk `@@ -523,4 +524,9 @@` puts `+ public void ResetEnrageCounter()` at new line 528, which matches `line` 528 and CodeRabbit's `528-531` nitpick in `rev_1`; created_at = review submitted_at; E'' string parses (lint) | NEW | PASS (G1) |
| 187–405 [178–396] | linear.linear_comments ×110 | `cmt_*` on ZOM-23 … ZOM-495 | unchanged | r45 §4 | REUSED | PASS (A1, A4) |

## 5. Lint flags and resolutions

| Flag | Resolution |
|---|---|
| (none) | 0 FAIL / 0 CHECK / 0 INFO. Checks A–C still run below. |

## 6. Checks A–C

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A: Records, references and IDs | **PASS** | **New keys:** Slack ids `f590e554…`, `e7977b0f…` and ts `1751591124.205377` / `1751591125.638214` have 0 matches in a complete fixed-string scan of the whole Slack export (`grep -rlF`, exit 1, 4,845 JSON files). GitHub ids `#271#rev_2` and `#271#rc_1` have 0 matches across every id in `/reviews` and `/review_comments`. The URL numbers `2984501722` and `2184401907` appear nowhere in Slack or GitHub. Each new key is defined once in the SQL. **References:** parent `2e34453f…` exists in `C093LEZGF6J` and is #271's opened notice; PR #271, head commit `2f1c9a22…`, file path and author EMPLOYEE_0025 (Arthur Blake, an existing account, rendered `arthur.blake` as in 5,787 base Slack links) all resolve. No second accounts. Unchanged keys keep their earlier complete collision results. |
| B: SQL structure and supported schema rules | **PASS** | All statements parse (lint: 0 `missing_required`, 0 `json_shape`, 0 `generated_column`). New Slack rows: 18 columns / 18 values; NOT NULL snapshot columns supplied; `reactions_json`/`files_json` `[]`, `attachments_json` a JSON array that parses, `metadata_json` `{}`; `text_fts` omitted. The UPDATE touches only `reply_count`. **Advisory G1 extended:** line 182 adds `seq` and line 184 adds `seq`, `pull_request_review_id`, `side`, `subject_type`, which are not in the snapshot's `github_reviews` / `github_review_comments` definitions. This is the same column set as the accepted #265 rows (lines 178/180). The snapshot is unverified, so per Eval 0 / schema README it's advisory, not a defect. |
| C: Dates, relationships and consistency | **PASS** | **Clock:** 2025-07-04T01:05:22–25Z, well before 2025-10-01 07:00Z. **Order:** PR opened 00:17:49Z → CodeRabbit review (Slack 00:21:51Z) → Arthur's review requested 00:36:36Z → **Arthur's approval and comment 01:05:22Z** → merge 13:29:30Z → Linear closing note `cmt_9bd1d317…` "merged with match3d#271" 16:25:40Z → ZOM-295 completed 16:40:40Z. PR `updated_at` 13:29:30Z is already later than the review, so it needs no update. The Slack notices are 2–3 s after the GitHub event, like base notices (e.g. `4ad5e8ab…`: event 1751358683, message 1751358686). **Content:** ZOM-295 ("Refill health and push monster back should reset ALL enrage status.", created 2025-06-23, Done) has "enrage" in its title, so card rule 1 would include it on the title match. Blake's "not tiers" review on its PR removes it, which is how rule 1 says to treat such a ticket. The closing note does not start with "tiers:", so nothing contradicts that. "This is a bug fix … no enrage number changes" fits the PR body (fixes a slow, low-damage enraged spawn; adds a reset method) and ZOM-295's description. Nothing in the injected enrage sheet or deck cites #271/ZOM-295. The wording follows the #265 comment (line 180) that passed review. **Line 50:** ", pacific time" keeps Robert's ask at three items, so the card's "the three things Robert asked for" still matches. It makes the PT reading of the done date explicit (see C-5). **Grader-facing text:** none; the new text is in persona voice. **Base-data conflicts:** SC-1 to SC-3 untouched; no Snowflake or Confluence writes. |

## 7. Findings

No demonstrated defects and no unresolved required checks.

**Advisories (not failures):**
- **G2-a, new (no timeline event for rev_2):** like rev_8 on #265, the new approval has no matching `reviewed` row in `github_timeline_events`. Base has 53 PRs with fewer `reviewed` events than reviews (and #271's own `ev_3` has an empty actor and null time), so this is within base patterns. Optional: add a `reviewed` timeline event `harmonygames-Games/match3d#271#ev_9` for EMPLOYEE_0025 at 2025-07-04T01:05:22Z with `{"commit_id": "2f1c9a2251dd59ea40b7a64f09231de80ff466ed"}`.
- **C-5, updated, downstream for /oe and /rubric:** Robert now says "the day it got marked done, pacific time", so OEs and rubric rows must use the PT day. That matters for **ZOM-200** (`2025-06-13T01:17:38Z` → June 12 PT), **ZOM-274** (`2025-06-21T01:17:25Z` → June 20 PT) and **ZOM-282** (`2025-06-21T01:17:19Z` → June 20 PT). Rows that only accept the UTC date for these would now be wrong.
- **C-8, new, downstream for /prompt, /oe and /rubric:** ZOM-295 is now a second "not tiers" decoy, a title match removed by Blake's review. Its evidence lives in the PR #271 review comment and the matching Slack notice in `C093LEZGF6J`. The OEs and rubric should keep ZOM-295 off the register and cite this review as the reason.
- **C-6, C-7, C-2, C-3, C-4, D7 carried** from r45/r42.
- **G1 (extended to lines 182/184), G2, G3, D1–D6 and A1–A5 carried** unchanged.

## 8. Next action and downstream

Proceed to `/prompt`. Because the SQL changed, every earlier pass that read it is outdated. Rerun `/prompt`, `/hardness`, `/oe` and `/rubric` in that order.

Stage dependencies for reuse: this result depends on SQL sha256 `b64bc2f2…ec23`, the synth-cut manifest, GitHub `data.json` (`/pull_requests` #271, `/reviews`, `/review_comments` complete id scans, `/timeline_events`, `/pull_request_commits`, `/pull_request_comments` for #271, `/users` EMPLOYEE_0025), Slack `messages/C093LEZGF6J/2025-07.json` (parent `2e34453f…` and its four replies), the complete fixed-string scan of the Slack export for the new ids, ts values and URL numbers, Linear `data.json` `/issues` (ZOM-295), the r45 dependencies for reused rows, and the reference hashes in §1.

### FINAL VERDICT: PASS

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt, then /hardness, /oe and /rubric, since the SQL changed.

Evidence limits: Static review only. No SQL was executed, and live database compatibility, Slack/GitHub runtime threading and Agent visibility are not certified. The schema snapshot is unverified (G1 carried and extended). Rows byte-identical to revision 45 reuse the prior review's per-row checks under stage-evidence-v1.
