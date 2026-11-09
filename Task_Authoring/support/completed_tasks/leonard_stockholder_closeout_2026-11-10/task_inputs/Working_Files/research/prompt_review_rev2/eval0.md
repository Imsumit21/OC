# Injection Data-Integrity Review (Eval 0) — SQL rev13

| Item | Value |
|---|---|
| Stage | `/injection` |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` |
| Mode | Local static audit. No SQL executed. Nothing written under `Evals/`. |
| Review time | 2026-11-08T13:40Z |
| Universe | `Universe_Normal`. `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`. Gmail `source_manifest.json` `d4b3f8c4…454b`; Other_Services `source_manifest.json` `456c0984…f009`. |
| Schema snapshot | `Evals/references/schema/injection.json` sha256 `01ef5792…f6eb` (unverified); `id_contracts.json` `fc4711ef…4682` |
| Input | `$R/inputs/01_Universe_Inject.sql` |
| Input sha256 | **`78af8ace66a92396722fbc5b18b719dad972bd85d3271a5a80d9266fb0404538`** |
| Previous revision | `fd51afbf63aa…0dec2` (rev12), Eval 0 PASS (`$R/prev/eval0_prev.md`) |
| Statements | 147: BEGIN, 130 INSERTs, 15 UPDATEs, COMMIT. The header comment (L3) states "130 INSERT, 15 UPDATE", which matches. |
| Lint | `hg.py lint` (`hg_injection_lint` `injection-lint-v1`, universe normal, clock 2026-02-14T00:00:00Z): **0 FAIL / 0 CHECK / 0 INFO**, flags `[]` |

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/c183cff7-226e-4dae-964a-0d311047e48a/scratchpad/prompt_review_rev2`.

## Reuse and change inventory

I split both revisions into statements, respecting quotes, and compared them as text. 135 of rev12's 140 statements are byte-identical in rev13, so their checks carry over from the rev12 PASS. That covers rev12's carried checks: the Nov 2024 owner-list edits, now at L121–L122; the Griffin, Linear and Drive rows; and advisory O-1.

5 statements changed and 7 are new. Each one is re-checked below, along with every record it touches.

| # | Line | Op / table | Target | Change |
|---|---|---|---|---|
| 1 | L18–19 | INSERT `gdocs.docs_documents` | `f_a37b403d5200d4f0a31d31` "Stockholder close-out notes" | The body gains " and delivered" in "Told means … sent to them directly and delivered, from one of the three of us". The NORMAL_TEXT style run end changes from 2032 to 2046. |
| 2 | L51–52 | INSERT `slack.slack_messages` | `846a70ba2460a877e1633a18857c1734` (C07C2866011, ts 1768418331.402719) | The text is now "fyi chatgpt has the other seed investors a couple of shares off in these, go by the ledger". The message is now a thread reply: `thread_parent_id` `b658ec71…`, `thread_ts_legacy` 1768417784.194359. |
| 3 | L53 | UPDATE `slack.slack_messages` (new) | `id = 'b658ec71107dd059e03ea425728ba3b3'` | Sets `thread_ts_legacy` 1768417784.194359, `reply_count` 1, `reply_users_count` 1 and `latest_reply` 1768418331.402719. |
| 4 | L85 | UPDATE `gmail.gmail_threads` | `leonard.hayes@harmonygames.co/1857029474983245439` | The snippet changes to the new KPMG reply's opening. |
| 5 | L86–87 | INSERT `gmail.gmail_messages` | `…/<LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@…outlook.com>` | The KPMG reply drops the item-1 clarification, so "Three clarifications" becomes "Two clarifications". `size_estimate` changes from 1460 to 1326. |
| 6 | L110 | UPDATE `gmail.gmail_threads` (new) | `leonard.hayes@harmonygames.co/1856860994291529096` (base) | The snippet is set to the bounce's snippet. |
| 7 | L111–112 | INSERT `gmail.gmail_messages` (new) | `…/<698ce305.050a0220.3b7f1c.9d2e.GMR@mx.google.com>` | Adds a bounce, "Delivery Status Notification (Failure)", for PERSON_3140_EMAIL, dated 2026-02-11T20:13:57Z. |
| 8 | L113–114 | INSERT `gmail.gmail_threads` (new) | `leonard.hayes@harmonygames.co/1856121753612004097` | Adds a new thread with `history_id` NULL. |
| 9 | L115–116 | INSERT `gmail.gmail_messages` (new) | `…/<CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz@mail.gmail.com>` | Adds Calvin Price's forward of a Carta ES-3 update, dated 2026-02-03T16:20:44Z. |
| 10 | L117–118 | INSERT `gmail.gmail_threads` (new) | `leonard.hayes@harmonygames.co/1856961760270377901` | Adds a new thread with `history_id` NULL. |
| 11 | L119–120 | INSERT `gmail.gmail_messages` (new) | `…/<CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=@mail.gmail.com>` | Adds Leonard's SENT message "Harmony" to "Akin <PERSON_8862_EMAIL>", dated 2026-02-12T22:52:17Z. |
| 12 | L227–228 | INSERT `linear.linear_comments` | `comment_ece7420618510fab05ab176f95ec14b7` (ENG-2453 Claire Morgan) | The body changes from "No mail with that address before Feb" to "Last mail with that address before Feb: May 1, 2023". |

## Lint flags and resolutions

The lint raised no FAIL, CHECK or INFO flags, so there was nothing to resolve. A clean lint is not enough for a PASS, so checks A–C below were still run in full.

## Check A — Records, references and IDs: PASS

**Collision checks on new keys**
- I searched all 88,728 Gmail files for the new keys. The scan was complete with no errors, and nothing matched:
  - the thread IDs `1856121753612004097` and `1856961760270377901`;
  - the Message-IDs `CAJr7mPx2QwF8nVb4LtK9sYd3HcE6uZaR1oGiN5tMeBq0WsXkQz`, `CAPBs_aLeDrdRoqOb0LrQ1AfGvbpmR-YdoG8A6PGmPay5Sc-ng=` and `698ce305.050a0220.3b7f1c.9d2e.GMR`.
- Within the SQL, no primary key (`id`, `document_id`, `contact_id`, `event_id`, or `(presentation_id, object_id)`) is repeated across the 130 INSERTs, and no Slack `(channel, ts)` pair is repeated.
- Both new thread IDs decode (id >> 20, in ms) to their first message's own instant: 2026-02-03 16:20:44.5Z and 2026-02-12 22:52:17.3Z. That matches the base Gmail convention, although it is not a listed contract.
- The bounce Message-ID prefix `0x698ce305` = 1770840837, which equals its `internal_date` of 1770840837000.

**Slack reply and parent**
- A `lookup` over `messages/*/*.json` (5,353 files, 687,230 records, scan complete) gave these results:
  - `846a70ba…` is absent from the base.
  - The parent `b658ec71…` exists exactly once, at `slack/messages/C07C2866011/2026-01.json` /728. It was posted by `EMPLOYEE_0038_SLACK_ID` (Leonard Hayes, `users.json` /23), with ts 1768417784.194359, `thread_ts` null, `reply_count` 0 and `latest_reply` null.
- ts `1768418331.402719` is absent from C07C2866011.

**UPDATE targets**
- L53 targets the Slack parent above, which exists.
- L110 targets `gmail/threads/leonard@harmonygames.co_1856860994291529096.json`, which exists and holds a single message, msg 0:
  - Message-ID `<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>`, from Leonard to PERSON_3140_EMAIL, cc robert and arthur.blake;
  - dated "Wed, 11 Feb 2026 12:13:48 -0800", which is 20:13:48Z.
- The bounce's In-Reply-To/References point to that message ID, and X-Failed-Recipients is PERSON_3140_EMAIL.
- L85 targets the thread inserted at L78–79 in the SQL.

**Actors and identities**
- **Calvin Price.** `[EMAIL_0801]` is Calvin Price per the base list "Calvin Price: [EMAIL_0801]" (`gmail/threads/leonard@harmonygames.co_1782034095239486005.json` /messages/4/body and other copies). The same address is the email on ENG-2452 at L220.
- **Carta sender.** The forwarded sender `SVC_0077_NAME <SVC_0077_EMAIL>` and the footer tokens `SVC_5909_EMAIL` and `SVC_4490_EMAIL` match the base Carta template (`leonard@harmonygames.co_1847333347700620793.json` /messages/0).
- **Bounce sender.** `PERSON_3555_NAME <PERSON_3555_EMAIL>` is the base mailer-daemon. Base bounces in `gmail/threads/00001116.json` /messages/1, `00003106.json` and `00007891.json` use the same sender, subject and body layout, including the DisabledUser 550 5.2.1 variant. The label set `INBOX, IMPORTANT, Label_b19fb8d1b3, CATEGORY_UPDATES` matches 00001116.
- **PERSON_3140_EMAIL** is [PERSON_NAME_0068] per `leonard@harmonygames.co_1789011705438137160.json` /messages/1/body. That matches ENG-2457 at L250.
- **Akin's address.** `PERSON_8862_EMAIL` appears in no base record. Complete scans of Gmail, Contacts, Slack, Linear, GDrive and GCal returned 0 matches.
  - The name "Akin" resolves to an existing base investor and board member. Examples: `slack/messages/C050WGU41HR/2023-08.json` /240 "Meeting with our investor/board … Akin", and `C04UTBZL6AX/2023-06.json` /1550 "so Akin, 1%".
  - This is a recipient address, not a second service account. The base already has more than one address per person; for example Claire Morgan has claire@harmonygames.co and PERSON_2360_EMAIL. No duplicate-account rule is broken.
- **Linear author.** The ENG-2453 comment author `usr_63fffeb4fab5233e` is unchanged.

**ID contracts**
- New `gmail_threads.history_id` is NULL, which is allowed.
- The new messages leave `history_id` unset. The column is nullable.
- No Drive files are new or changed in this revision.

## Check B — SQL structure and supported schema rules: PASS

- **Column and value counts.** Every INSERT parses with equal column and value counts. All 147 statements were checked, including the 12 changed or new ones.
- **UPDATE structure.** The UPDATEs at L53, L85 and L110 have single-ID predicates and no duplicate assignments.
- **JSON.** All JSON-typed literals in the changed and new rows parse:
  - Gmail: `label_ids_json`, `to_json`, `cc_json`, `bcc_json`, `reply_to_json`, `headers_json`, `attachments_meta_json`;
  - Slack: `reactions_json`, `files_json`, `attachments_json`, `metadata_json`;
  - the doc's `style_runs_json`.
- **Generated columns.** No statement sets `body_text_fts` or `text_fts`.
- **Required columns.** The new Slack row gives every column marked NOT NULL in the snapshot. The new Gmail rows give `id`, `thread_id` and `user_email`.
- **Linear dates.** The changed comment keeps its `YYYY-MM-DDTHH:MM:SSZ` values.
- **Snapshot comparison (provisional).** Every column used by the changed and new statements is in the snapshot for `gmail_messages`, `gmail_threads`, `slack_messages`, `linear_comments` and `docs_documents`: MATCH.
- **Advisory O-1.** From unchanged rows: 4 columns are not in the unverified snapshot. They are `slides_pages.notes`, `slides_page_elements.table_json`, `slides_page_elements.ordinal` and `linear_projects.links_json`. This is advisory only.
- **Ordering.** Each new thread is inserted before its message (L113→L115, L117→L119). The Slack reply's parent is a base record.

## Check C — Dates, relationships and consistency: PASS

**Clock.** Every new event timestamp is at or before 2026-02-14 00:00 UTC:
- 2026-01-14T19:18:51Z;
- 2026-02-03T16:20:44Z;
- 2026-02-11T20:13:57Z;
- 2026-02-12T22:52:17Z;
- 2026-02-13T17:37:15Z.

The only later date is "Last day to exercise Feb. 20, 2026", which is a plan date and allowed. Header dates match the `date` and `internal_date` fields, and the weekdays are correct:
- "Wed, 11 Feb 2026 12:13:57 -0800 (PST)" = 20:13:57Z;
- "Tue, 03 Feb 2026";
- "Thu, 12 Feb 2026";
- the forwarded "Fri, Jan 23, 2026".

**Doc (1).** The decoded body is 2,046 characters, matching the new style-run end of 2046 (title run 0–28). The diff against rev12 is the single insertion " and delivered". No other SQL text defines "told" differently. The older "Holder outreach notes" (L21) is explicitly superseded by "These replace my earlier outreach notes."

**Slack reply (2, 3)**
- **Ordering.** The reply ts (19:18:51Z) is after the parent ts (19:09:44Z). `created_at` matches the ts.
- **Thread fields.** The parent's new thread fields follow the same pattern as the rev12 thread at L60–L68, which already passed: `thread_ts_legacy` = own ts, `reply_count` 1, `reply_users_count` 1 (Leonard only), `latest_reply` = the reply ts.
- **The claim matches base data.** The parent's ChatGPT table uses "3,051,881 Seed" and "Other Seed investors 305,188". The base ledger figure is 3,051,879 (`gdocs/data.json` /docs_documents/40, "Inputs from ledger … Series Seed Preferred: 3,051,879"; also `leonard@harmonygames.co_1773160052067710033.json` /messages/10, "3,051,882 vs 3,051,879"). Griffin holds 2,746,693, so the other investors hold 305,186: two shares off. The text "a couple of shares off … go by the ledger" is therefore accurate.
- **Removed clause.** The dropped clause, "owner list counts the advisor options…", is referenced by nothing else in the SQL.

**KPMG reply (4, 5)**
- **Body and size.** Only the item-1 sentence and "Three" → "Two" changed. The body shrinks by 134 characters, which equals the `size_estimate` drop of 1460 → 1326.
- **Item numbering.** The remaining items, 2 and 4, exist in the original request at L81 (items 1–4).
- **Snippets.** The thread snippet (L85) equals the message snippet, and the message is the thread's latest (16:48:33Z request → 17:12:40Z Leonard → 17:37:15Z KPMG).
- **Removed figures.** "6,000,000 common" and "3,051,879" no longer appear anywhere in the SQL, so there is nothing left dangling.

**Bounce (6, 7)**
- **Timing.** It arrives 9 s after the base letter (20:13:48Z → 20:13:57Z). It is the thread's latest message, and the thread snippet equals its snippet.
- **No conflicting delivery evidence.** In the complete Gmail scan, PERSON_3140_EMAIL never appears as a sender. Its only header-level occurrences are this letter and the cc copies of it (`gmail/threads/00016874.json`, Robert's copy; `blake@harmonygames.co_1856861205341126331.json`, Arthur Blake's copy), so nothing shows the account receiving mail.
- **ENG-2457.** This agrees with the unchanged ENG-2457 comment, "No mail with that address before Feb".
- **Doc rule.** The doc's new "and delivered" rule is what makes this bounce matter.

**Calvin forward (8, 9)**
- **Matches the base Carta notice.** The base Carta notice `leonard@harmonygames.co_1847333347700620793.json` /messages/0 ("Termination details for Calvin Price", 2025-10-29) states ES-3, Granted 8,138, Vested 4,408, Grant date Nov. 10, 2023, terminated Oct. 24, 2025, Last day to exercise Jan. 24, 2026. The forward repeats every one of those figures and adds "Feb. 20, 2026 (previously Jan. 24, 2026)".
- **A dated, valid supersession.** The update is dated Jan 23, before the old deadline, and the forward is dated Feb 3.
- **No conflicting record.** No other base ES-3 record exists. A complete scan for "ID ES-" found 14 Carta notices, and only one is ES-3.
- **Linear rows.** It agrees with ENG-2452's "Nov 2024 owner list: 8,138" (L224) and "No mail with that address before Feb" (L222, since Feb 3 falls in Feb).

**Akin note (10, 11)**
- "we let the team know yesterday" matches the base termination notices sent on Feb 11, 2026 (`gmail/threads/00016873.json` and `leonard@harmonygames.co_1856858053929740799.json`, "Notice of Involuntary Termination", 2026-02-11 12:10:30 -0800).
- "on the board and since" agrees with the SQL contact update at L129, "left the board May 2025", for Matthew Collins.
- It is sent after Leonard's #winddown list (`slack/messages/C0ADGSZKR3R/2026-02.json` /197, ts 1770934638 = 22:17:18Z), so the ordering is coherent.

**ENG-2453 comment (12)**
- In Leonard's mailbox, PERSON_2360_EMAIL appears in these headers:
  - `leonard@harmonygames.co_1760997136114607232.json`, 2023-03-21 (Reply-To);
  - `leonard@harmonygames.co_1764717974138707720.json`, **Mon, 01 May 2023 18:36:47 +0000** (Reply-To "claire <PERSON_2360_EMAIL>");
  - `leonard@harmonygames.co_1856858053929740799.json`, 2026-02-11 (To).
- The last of those before February is May 1, 2023, so the new comment is accurate. The scan was complete: 69 matches against a limit of 80.

**Grader-facing or padding text.** None. All of the new text is ordinary in-world mail, Slack and Linear content, and the SQL comments only add the updated statement count on L3.

## Context for /prompt (non-blocking; not introduced defects)

1. **Akin and the holder issue.**
   - The Feb 12 note goes to `PERSON_8862_EMAIL`, an address found in no base record and on no Linear holder issue.
   - Linking "Akin" to the holder issue ENG-2447 "Husnu Matthew Collins" (matthew.collins@harmonygames.co) depends on context: the base Slack mentions of investor/board member Akin, and the SQL contact update "left the board May 2025".
   - /prompt should confirm that a Leonard-reachable record settles this identity for the "Already told" decision.
2. **What "mail with that address" means.** The Linear comments on ENG-2452, ENG-2453 and ENG-2457 hold only if the phrase means the address appears in a header (sender or recipient).
   - The base thread "Re: [SOURCE_ORG_0001]- Option Issuances" (`leonard@harmonygames.co_1782034095239486005.json` /messages/4–34, dated 2023-11 to 2024-10) lists `[EMAIL_0801]` and `PERSON_2360_EMAIL` in its body text.
   - `leonard@harmonygames.co_1789011705438137160.json` names PERSON_3140_EMAIL in its body.
   - If body mentions counted, these comments would read differently.
3. **Owner-list sentence in Slack.** As in rev12, the Slack copy of the owner list (`slack/messages/C04UEQVDVB7/2024-11.json` /55) still says "(Total ownership percentage adds to 100%)". This is base content.

## Checks

| Check | Result | Evidence / unresolved required check |
|---|---|---|
| A — Records, references and IDs | PASS | New thread and message IDs are absent from the complete Gmail scan (88,728 files). The Slack reply ID is absent and its parent is present once (687,230 records). The UPDATE targets exist. Actors resolve to base identities. No SQL-internal key duplicates. |
| B — SQL structure and supported schema rules | PASS | Lint is clean. The independent parse is clean (column/value counts, JSON, no generated columns, NOT NULLs given). Snapshot MATCH for every changed or new column; advisory O-1 unchanged. |
| C — Dates, relationships and consistency | PASS | All timestamps are at or before the clock. Header dates, internal dates and snippets agree, and replies follow their parents. Each changed claim matches a base record: the Carta ES-3 notice, the ledger figure 3,051,879, the May 1, 2023 header, the Feb 11 letter and the KPMG item list. |

No defects to repair.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt.

Evidence limits:
- **Static review only.** The SQL was not executed, and the schema snapshot is unverified. Four columns from unchanged rows are not in it (advisory O-1).
- **Uniqueness scope.** Uniqueness is checked against the local base plus the SQL, not the live database.
- **Agent visibility.** Visibility for Leonard is outside this stage. The open points on the Akin identity and the meaning of "mail with that address" are passed to /prompt above.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
