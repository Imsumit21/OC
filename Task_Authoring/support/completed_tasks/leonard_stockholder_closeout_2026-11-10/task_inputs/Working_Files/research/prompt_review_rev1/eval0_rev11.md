# Injection Data-Integrity Review (Eval 0) — SQL rev11

| Item | Value |
|---|---|
| Stage | `/injection` |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` |
| Mode | Local static audit. No SQL executed. Nothing written under `Evals/`. |
| Universe | `Universe_Normal`. Manifest sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`. |
| Input | `$R/inputs_rev11/01_Universe_Inject.sql` |
| Input sha256 | **`40ce7beff0d924d0f70b436a271b50c1534635e9fe558667cd3b1a2f6b631cc1`** |
| Statements | 138: BEGIN, 125 INSERTs, 11 UPDATEs, COMMIT |
| Lint | 0 FAIL / 0 CHECK / 0 INFO. Output `out/scratch_e0r11/lint.json`, sha256 `e510c6fa…`. |

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/prompt_review_rev1`.

## Reuse

Everything outside the changed comments is carried from `$R/out/eval0_rev10.md` (rev10 PASS, sha256 `7d73038e…1cd2`), and through it from `eval0_final.md` (rev7).

My own statement-level parse diff shows 112 of the 138 statements are byte-identical to rev10. The same check confirms what changed: only the `body` of the 26 "last contact" comments. Their IDs, issue references, author and timestamps are unchanged.

## Changed statements: 26 `linear.linear_comments` bodies

Each body now reads "Last mail with that address before Feb: <date>", or "No mail with that address before Feb". It refers to the `Email:` address on its own issue.

I checked the claims against Leonard's mailbox (`user_email` = leonard.hayes@harmonygames.co). A message counted if the address appeared in from/to/cc/bcc and it was dated before 2026-02-01 PT. Each address was drawn from a complete Gmail scan, recorded in my rev1–rev7 header indexes.

**22 of 26 checked. All 22 match.**

| Issue | Address | Claim | Base (Leonard's mailbox) |
|---|---|---|---|
| ENG-2438 / 2439 | PERSON_4337 | Jan 24, 2026 | Jan 24, 2026 PT (177 msgs) |
| ENG-2440 | PERSON_3336 | Jan 8, 2026 | Jan 8, 2026 |
| ENG-2441 | PERSON_3063 | May 18, 2024 | May 18, 2024 |
| ENG-2442 | PERSON_0693 | May 30, 2025 | May 30, 2025 |
| ENG-2443 | PERSON_2260 | Dec 16, 2025 | Dec 16, 2025 |
| ENG-2445 | PERSON_2275 | May 18, 2024 | May 18, 2024 |
| ENG-2446 | PERSON_3941 | Sep 15, 2025 | Sep 15, 2025 |
| ENG-2447 | matthew.collins@ | Oct 28, 2025 | Oct 28, 2025 |
| ENG-2448 | PERSON_5275 | May 19, 2024 | May 19, 2024 |
| ENG-2449 | PERSON_1287 | May 18, 2024 | May 18, 2024 |
| ENG-2450 | PERSON_2361 | Jul 16, 2023 | Jul 16, 2023 |
| ENG-2451 | PERSON_3641 | none | none |
| ENG-2452 | [EMAIL_0801] | none | none |
| ENG-2453 | PERSON_2360 | none | none |
| ENG-2454 | PERSON_4194 | Sep 1, 2023 | Sep 1, 2023 |
| ENG-2457 | PERSON_3140 | none | none |
| ENG-2458 | PERSON_4363 | Aug 27, 2023 | Aug 27, 2023 |
| ENG-2459 | PERSON_2684 | Mar 26, 2024 | Mar 26, 2024 |
| ENG-2460 | PERSON_4243 | Aug 15, 2024 | Aug 15, 2024 |
| ENG-2461 | cameron@ | Oct 30, 2025 | Oct 30, 2025 |
| ENG-2462 | PERSON_2314 | Oct 29, 2025 | Oct 29, 2025 |
| ENG-2463 | PERSON_1174 | Aug 8, 2024 | Aug 8, 2024 |

**Not independently checked (3 issues):**

- ENG-2444 `patrick@`, claim Jun 27, 2025: consistent with the rev1 finding of the Jun 27, 2025 "Ask for support" mail to Leonard, but my index for that address was not complete-scope.
- ENG-2455 `victor.barnes@` and ENG-2456 `marcus.bennett@`: not indexed.

Because the notes are now scoped to the literal address and mailbox, the earlier reading questions no longer arise. That covers the Slack-versus-mail question, the `patrick@` conflation and the ENG-2441 identity caveat.

## Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | Unchanged from rev10. The comment IDs and references are unchanged. |
| B — SQL structure and supported schema rules | PASS | Independent parse and lint are clean. Advisory O-1 remains: 4 columns are absent from the unverified snapshot (`slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, `linear_projects.links_json`). |
| C — Dates, relationships and consistency | PASS | All spot-checked dates match the base. Every event timestamp is at or before 2026-02-13T18:21:46Z; only the Feb 17 calendar plan fields are later. |

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt.

Evidence limits:
- Static review only; the schema snapshot is unverified and 4 of the columns used are not in it.
- The comment dates were spot-checked as requested: 22 of 26 match. ENG-2444, 2455 and 2456 were not independently re-verified.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
