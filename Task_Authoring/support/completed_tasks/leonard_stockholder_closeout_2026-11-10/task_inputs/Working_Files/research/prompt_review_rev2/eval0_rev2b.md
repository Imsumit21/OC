# Injection Data-Integrity Review (Eval 0) — re-check of SQL bd67fedbbd47

| Item | Value |
|---|---|
| Stage | `/injection` |
| Review version | `injection-static-v2` |
| Mode | Local static audit. No SQL executed. Nothing written under `Evals/`. |
| Universe | `Universe_Normal`. `universe_manifest.json` sha256 `5e01ac4472c8…0de450`. |
| Input | `$R/inputs/01_Universe_Inject.sql` |
| Input sha256 | **`bd67fedbbd47675056920d80253746a092795fa0f0358258fa3a65abccc32bb1`** |
| Compared against | `$R/prev/01_Universe_Inject.78af8ace66a9.sql`, which passed Eval 0 (`$R/out/eval0.md`) |
| Statements | 149: BEGIN, 132 INSERTs, 15 UPDATEs, COMMIT |
| Lint | `hg.py lint` on the new file (read-only): **0 FAIL / 0 CHECK / 0 INFO**, flags `[]`, info `[]` |

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/c183cff7-226e-4dae-964a-0d311047e48a/scratchpad/prompt_review_rev2`.

## Change inventory

I compared the two files statement by statement. 137 of the 147 statements in 78af8ace66a9 are byte-identical here, and their results carry over from `eval0.md`. 10 statements changed, 2 are new, and none were removed. I compared every changed row field by field.

| Line | Op / table | Record | Change |
|---|---|---|---|
| L18–19 | INSERT `gdocs.docs_documents` | `f_a37b403d5200d4f0a31d31` | The body gains " (a post in a channel doesn't count)" inside the "Told means …" rule. The NORMAL_TEXT style-run end changes from 2046 to 2082. |
| L83 | INSERT `gmail.gmail_messages` | `leonard…/<CAPBs_a7Tq2L…>` | Date header changes from "Fri, 13 Feb 2026 17:12:40 +0000" to "09:12:40 -0800". Nothing else changes. |
| L93 | INSERT `gmail.gmail_messages` | `leonard…/<CAPBs_a5Wn3R…>` | Date header changes from 18:19:02 +0000 to 10:19:02 -0800. |
| L96, L99, L102 | INSERT `gmail.gmail_messages` | `<CAGkro_Tn7wQ…>` copies in the Leonard, Robert and Arthur Blake mailboxes | Date header changes from 22:38:16 +0000 to "Thu, 12 Feb 2026 14:38:16 -0800". |
| L105, L108 | INSERT `gmail.gmail_messages` | `<CAGkro_PbX4m…>` copies in the Leonard and Robert mailboxes | Date header changes from 23:41:12 +0000 to 15:41:12 -0800. |
| L115 | INSERT `gmail.gmail_messages` | `<CAJr7mPx2Q…>`, Calvin Price's forward | Date header changes from 16:20:44 +0000 to "Tue, 03 Feb 2026 08:20:44 -0800". |
| L117 | INSERT `gmail.gmail_threads` (new) | `leonard.hayes@harmonygames.co/1783169549554193375` | New thread with `history_id` NULL. |
| L119 | INSERT `gmail.gmail_messages` (new) | `leonard…/<170056300100.11.4471902385519067321@notifications-worker-75f77576db-lb9sh>` | New Carta digest, "Carta activity for Nov. 20, 2023", dated 2023-11-21T10:36:41Z. It reports that ES-8 and ES-10 were accepted. |
| L123 | INSERT `gmail.gmail_messages` | `<CAPBs_aLeDrd…>`, the Akin note | `to_json` and the To header change from "Akin <PERSON_8862_EMAIL>" to "Husnu Akin <PERSON_8862_EMAIL>". The Date header changes from 22:52:17 +0000 to "Thu, 12 Feb 2026 14:52:17 -0800". The body, snippet and size are unchanged. |

## Check A — Records, references and IDs: PASS

**Collisions.** A complete scan of base Gmail found none of the following:
- the thread ID `1783169549554193375`;
- the Message-ID `170056300100.11.4471902385519067321`, or its 12-digit prefix on its own;
- the Carta option IDs `18258527` and `18258529`.

The option IDs are also absent from Slack, GDrive, GSheets and GDocs (all complete scans). Within the SQL, no INSERT key is repeated.

**Thread ID against time.** `1783169549554193375 >> 20` decodes to 2023-11-21 10:36:41.207Z, the digest's own send time. That is the base convention; for example, base `1782897835407336831` decodes to the Nov 18, 2023 digest.

**Message-ID shape** compared with the base digests:

| Message | Message-ID | Matches its Date header |
|---|---|---|
| Base `leonard.hayes@harmonygames.co/1782897835407336831` | `<170030387383.11.5512588904826114323@notifications-worker-75f77576db-lb9sh>` | 1700303873.83 = Sat, 18 Nov 2023 10:37:53 |
| Base `/1790417238097762434` | `<170747493524.10.8857752395685666242@notifications-worker-f45bb5d74-55mtm>` | 1707474935.24 = Fri, 09 Feb 2024 10:35:35 |
| New L119 | `<170056300100.11.4471902385519067321@notifications-worker-75f77576db-lb9sh>` | 1700563001.00 = 2023-11-21T10:36:41Z = `internal_date` 1700563001000 |

The new ID has the same structure: epoch in centiseconds, a 2-digit field, a 19-digit field, and the same worker host as the Nov 2023 base digest.

**Sender and template.** The sender is `SVC_0077_NAME <SVC_0077_EMAIL>`, and the subject pattern is "Carta activity for <Mon. D, YYYY>". The body template matches both base digests:
- "Here's what's happening in your accounts", then "<name> accepted option grant ES-n <…open=…>";
- the Carta footer tokens `SVC_5909_EMAIL` and `SVC_4490_EMAIL`.

The option-ID mapping in the Nov 17 base digest is ES-n → 18258519+n (ES-1→…520, ES-3→…522, ES-7→…526, ES-9→…528, ES-11→…530). The new ES-8 (→…527) and ES-10 (→…529) fit that sequence.

**Holders.** Both resolve to existing base people who also have SQL holder issues:
- **ES-8** goes to `[PERSON_NAME_0089] [PERSON_NAME_25152]` (ENG-2440). The base shows them as an advisor: "Advisor Agreement" DocuSign (`leonard@…_1777096000955189741`), and the disclosure-schedule question about their role (`leonard@…_1769323197485172949` /messages/10).
- **ES-10** goes to `PERSON_1287_NAME` (ENG-2449). The base shows them as an advisor: "Apologies for shipping the advisory contract late. We have been waiting for our 409 approval and Carta setup" (`gmail/threads/00001538.json`).
- **No conflicting assignment.** No base record assigns ES-8 or ES-10 to anyone. The case-sensitive scans in Gmail, Slack, GDrive, GSheets and GDocs returned only Linear "DES-8"/"DES-10" text and Slack file IDs.

**Akin display name.** "Husnu Akin" is a display name on an existing recipient address, not a new account. It is consistent with the base digest `leonard@…_1782897835407336831` ("ES-9 … for Husnu Matthew Collins") and with the Slack mentions of Akin as investor and board member. "Husnu Akin" itself appears nowhere in base Gmail.

**Changed Date headers.** Only the header value changed in each. The rows still have the same IDs, threads and in-thread positions as in the version that passed.

## Check B — SQL structure and supported schema rules: PASS

- **Lint.** Clean.
- **Column and value counts.** Equal for all 132 INSERTs.
- **JSON.** Every JSON field in the changed and new rows parses: `label_ids_json`, `to_json`, `cc_json`, `bcc_json`, `reply_to_json`, `headers_json`, `attachments_meta_json` and `style_runs_json`.
- **Generated columns.** No `body_text_fts` or `text_fts` is set.
- **Required columns.** The new rows give `id`, `thread_id` and `user_email`.
- **Ordering.** The thread at L117 is inserted before its message at L119.
- **Snapshot.** Every column used is in the snapshot for `gmail_threads`, `gmail_messages` and `docs_documents`. Advisory O-1, from unchanged rows, is unchanged.

## Check C — Dates, relationships and consistency: PASS

**All 14 Gmail rows.** Each Date header parses to exactly the row's `date` and `internal_date` (checked by script). The offsets map correctly, for example "Thu, 12 Feb 2026 14:52:17 -0800" = 22:52:17Z. The weekdays are right (Fri 13 Feb 2026, Thu 12 Feb, Tue 03 Feb, Tue 21 Nov 2023). The quoted line "On Fri, Feb 13, 2026 at 8:48 AM" in L83 still matches the request sent at 16:48:33Z. The base's own sent mail uses -0800 headers (for example the 2026-02-11 letter "12:13:48 -0800").

**Clock.** The new digest (2023-11-21) is historical, which is allowed. No event timestamp is later than 2026-02-14 00:00 UTC.

**Digest chronology.** The Nov 17, 2023 base digest has Arthur Blake signing grants; the new digest has acceptances on Nov 20, sent the next morning at about 10:36Z, the same slot as the base digests (10:37Z and 10:35Z). Both grants were accepted after the November 2023 grant round, consistent with the Nov. 10, 2023 grant date in the base ES-3 notice. No SQL row conflicts: `ES-8` and `ES-10` appear only at L120.

**Snippet, size and labels**
- The thread snippet equals the message snippet, and both equal the start of the whitespace-collapsed body.
- `size_estimate` 2544 is at least the body's 1,656 bytes.
- Labels are `INBOX, Label_b19fb8d1b3, CATEGORY_UPDATES`. Both base digests also carry `IMPORTANT`. Leaving it out is a per-message importance flag, not a supported rule, so this is an observation only.

**Doc.** The decoded body is 2,082 characters, equal to the new style-run end; the title run is 0–28. The diff is a single insertion of 36 characters. No other SQL text defines "told".

**Akin note.** The body, snippet and size (1177) are unchanged. The added 6-character display name and the offset change do not need a size change, since `size_estimate` is approximate.

**Grader-facing or padding text.** None. No new comments were added, and the comment on L3 still matches the counts.

## Context for /prompt (non-blocking)

- **Doc rule.** The new parenthetical "(a post in a channel doesn't count)" changes who counts as already told. Deciding which holders it affects belongs to /prompt.
- **Akin identity.** "Husnu Akin" now gives a mailbox link, through the name "Husnu", to the base digest's "Husnu Matthew Collins" (ES-9, `leonard@…_1782897835407336831`). /prompt should confirm that this settles the Akin → ENG-2447 identity raised in `eval0.md`.

## Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | The new thread and message IDs and the option IDs are absent from complete base scans, with no SQL-internal duplicates. The thread ID decodes to the send time, and the Message-ID matches the base worker shape. The holders are existing base advisors. |
| B — SQL structure and supported schema rules | PASS | Lint and the independent parse are clean. Snapshot MATCH. |
| C — Dates, relationships and consistency | PASS | All 14 Date headers equal their `date` and `internal_date`. The digest chronology and the doc length are consistent, and nothing conflicts with an ES-8 or ES-10 record. |

No defects to repair.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt.

Evidence limits:
- **Static review only.** The SQL was not executed, and the schema snapshot is unverified. Advisory O-1 (4 columns from unchanged rows) still applies.
- **Uniqueness scope.** Uniqueness is checked against the local base plus the SQL only.
- **Labels.** Leaving `IMPORTANT` off the digest is noted, not a defect.
- **Agent visibility.** Visibility for Leonard is outside this stage.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
