# Injection Data-Integrity Review (Eval 0) — final, SQL rev7

- Stage `/injection`, review version `injection-static-v2`, evidence contract `stage-evidence-v1`.
- Mode: local static audit of a scratch copy. I did not read `Task_Authoring/task_inputs*` or `support/`, did not execute SQL, and wrote nothing under `Evals/`.
- Actual review time: 2026-11-08 (machine clock, about 04:40Z).
- Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
- Universe: `Universe_Normal` (`hg4-2026-08-31 v37`). Manifest `Evals/references/universes/normal/universe_manifest.json`, sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`.
- **Input:** `$R/inputs_rev7/01_Universe_Inject.sql`, 84,214 bytes, **sha256 `045f64bd805524ec1d0d0c4972a54ac4a682672fba2dc0c9dda0ea7971ef09d0`**. It has 138 statements: BEGIN, 125 single-row INSERTs, 11 UPDATEs, COMMIT.
  - `$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/prompt_review_rev1`.
- **Reference hashes (sha256):**
  - Schema snapshot `injection.json`: `01ef5792…6f6eb`
  - `id_contracts.json`: `fc4711ef…4682`
  - Eval 0: `86af2102…dcfd3`
  - WORKFLOW: `05a5e45e…68c69`
- **Lint:** `hg_injection_lint` (`injection-lint-v1`) run through `Task_Authoring/tools/hg.py lint`. Output `out/scratch_e0r7/lint.json`, sha256 `1c9feb80…519b`. Result: **0 FAIL / 0 CHECK / 0 INFO**.
- **Reused evidence:** facts on unchanged statements are carried from my rev1 report `$R/out/eval0.md` (sha256 `84685fa9b70903b95b5e2cf0bad60126b2b92b5f5a28cb3ccaeaecae690d378e`, SQL `6f3b1899…`). Those facts are: references, collisions, clock and threading for the 130 rev1 statements, and the owner-list figures.
  - I verified each of those statements is byte-identical in rev7, using a statement-level parse diff.
  - Everything new or changed between rev1 and rev7 was checked NEW.
  - rev3 and rev5 were reviewed along the way. Their verdicts are superseded by this report.

## What changed from rev1 to rev7 (statement-level diff)

| Kind | Statement(s) |
|---|---|
| NEW | Slack `846a70ba2460a877e1633a18857c1734` in #executives (C07C2866011), ts 1768418331.402719, Leonard, dated 2026-01-14T19:18:51Z |
| NEW | Robert's reply-all on "Re: Board position", Message-ID `<CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com>`. Inserted in three mailboxes (Leonard, Robert, Arthur), each with a thread snippet UPDATE. |
| NEW | UPDATE `contacts.contacts` `db57e559500151d6b3991b62` (Matthew Collins): job → "Investor and advisor (left the board May 2025)", updated_at → 2025-05-02T16:20:11Z |
| CHANGED | Close-out notes Doc body and style runs (body now 2,032 characters) |
| CHANGED | Draft sheet grid: added row "the list's percentages leave out the option pool, so they only add to about 94%" |
| CHANGED | Two slide text boxes |
| CHANGED | KPMG clarification body, snippet and size, plus its thread snippet UPDATE |
| CHANGED | Sunset intake mail, and Leonard's quoted reply: the formal-notice bullet removed from both |
| CHANGED | ENG-2447 title → "Husnu Matthew Collins"; ENG-2460 title → "Brian Foster" |
| CHANGED | `Email: …` description on all 26 issues |

## Check A — Records, references and IDs: PASS

- **Slack.**
  - The new message ID is unused: lookup over 687,230 messages in 5,353 files, `scan_complete: true`.
  - The new ts is unused in `C07C2866011/2026-01.json` (1,586 messages).
  - #executives is a private channel that includes Leonard.
- **Gmail.**
  - The new Message-ID is unused: complete text scan of all 88,726 thread files.
  - The three UPDATE and INSERT target threads exist:
    - `leonard.hayes@…/1856958794180374704` in `threads/leonard@harmonygames.co_1856958794180374704.json`
    - `robert@…/1856959418563541618` in `threads/00016903.json`
    - `arthur.blake@…/1856959418725253571` in `threads/blake@harmonygames.co_1856959418725253571.json`
  - Each of those threads contains the In-Reply-To parent `<CAPBs_a5B01FzMbHrb6FgGYtB1YhcNSecOo6FKJ63ki5rD0Gg6Q@mail.gmail.com>`, which is Leonard's 22:14:52Z reply. The References chain `<BYAPR02MB4358…> <CAPBs_a5B01F…>` matches the base.
- **Contacts.** The UPDATE target exists at `contacts.json` /contacts/159 (Matthew Collins, matthew.collins@harmonygames.co). Its base job is "Independent Director (investor/advisor, not an employee)".
- **Issue emails.** All 26 `Email:` values resolve to the named holder in the base:

  | Issue(s) | Address | Base evidence |
  |---|---|---|
  | ENG-2438, 2439 | PERSON_4337 | Griffin partner |
  | ENG-2440 | PERSON_3336 | `[PERSON_NAME_0089] segerstråle <PERSON_3336_EMAIL>` |
  | ENG-2442 | PERSON_0693 | `[PERSON_NAME_4468]` signature |
  | ENG-2443 | PERSON_2260 | listed with `[PERSON_NAME_52949]` |
  | ENG-2444 | patrick@ | `Patrick Lewis <patrick@harmonygames.co>` |
  | ENG-2445 | PERSON_2275 | listed with `[PERSON_NAME_27652]` |
  | ENG-2446 | PERSON_3941 | his own address |
  | ENG-2447 | matthew.collins@ | base contact |
  | ENG-2448 | PERSON_5275 | `[PERSON_NAME_0129]` in the "Second Close- Tor Capital" mails |
  | ENG-2449 | PERSON_1287 | his own address |
  | ENG-2450–2456 | per issue | match Leonard's Nov 8, 2023 option-holder list, `threads/00001948.json` |
  | ENG-2457, 2458 | PERSON_3140, PERSON_4363 | "Martin's email address is PERSON_4363_EMAIL / [PERSON_NAME_0068]'s … PERSON_3140_EMAIL" |
  | ENG-2459 | PERSON_2684 | "Full Name: [PERSON_NAME_0051] Email: PERSON_2684_EMAIL Option Grant: 3866" |
  | ENG-2460, 2461, 2462, 2463 | per issue | Leonard's Oct 18, 2024 grant list, `threads/leonard@harmonygames.co_1782034095239486005.json` (legal name, share count and email per holder) |
  | ENG-2441 | PERSON_3063 | signs "Arthur Schaeppi … Maple Grove, MN". Identity caveat O-2. |

- **Retitles are supported.**
  - ENG-2447 "Husnu Matthew Collins" is the Carta stakeholder name: certificate SSP-10 and option grant ES-9 in `threads/leonard@harmonygames.co_1777100628672295991.json` and `…_1782897835407336831.json`. The owner-list token `[PERSON_NAME_11362]` appears nowhere except the owner list.
  - ENG-2460 "Brian Foster": item 1 of the Oct 2024 grant list has legal name `[PERSON_NAME_2769] [PERSON_NAME_0093]`, 10,173 shares and PERSON_4243_EMAIL, and that address's header name is "brian".

## Check B — SQL structure and supported schema rules: PASS (provisional advisory O-1)

- An independent parser and the lint agree:
  - All column and value counts match, and no column is duplicated.
  - All `*_json` literals parse.
  - Linear `*_at` and date values use `YYYY-MM-DDTHH:MM:SSZ` and `YYYY-MM-DD`; `state_history_json '[]'` is present on every issue.
  - No generated column is set, and every NOT NULL column is given.
  - All 11 UPDATEs use single-ID predicates.
- The close-out notes style runs end at 2,032, its body length.
- **O-1, unchanged.** Four columns are absent from the unverified snapshot: `slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, and `linear_projects.links_json`. This is advisory only.

## Check C — Dates, relationships and consistency: FAIL

- **Clock.**
  - Every event timestamp is at or before 2026-02-13T18:21:46Z. The new entries are 2026-01-14T19:18:51Z (Slack), 2026-02-12T22:38:16Z (Gmail) and 2025-05-02T16:20:11Z (contact).
  - Only the Feb 17 calendar slot is later, and it is a plan field.
- **Encoded times agree.** The newly inserted rows check out: Slack ts = created_at (8 of 8 Slack rows). Gmail internal_date = date = Date header; ID suffix = Message-ID; In-Reply-To and References match the columns; snippet = body prefix (10 of 10 Gmail rows).
- **Robert's reply-all.**
  - It is sent at 22:38:16Z, after Leonard's 22:14:52Z reply. The quoted "2:14 PM" is correct.
  - It is the latest message in all three threads, so the three snippet UPDATEs are correct.
  - The recipients are the exact reply-all set.
  - Labels follow base patterns: Leonard's copy INBOX/IMPORTANT/Opened/PERSONAL, Robert's SENT, Arthur's INBOX/IMPORTANT/PERSONAL.
  - "That leaves Leonard and me on the board" matches the base board history:
    - Directors as of Nov 8, 2023: PERSON_4337 (Preferred), Matthew Collins (Independent), Robert (Common) and Leonard (CEO).
    - Matthew resigned "with immediate effect" on May 1, 2025 (`threads/leonard@harmonygames.co_1830959847543474636.json`).
    - The Jul 21, 2025 Carta board consent's signatories were PERSON_4337, Leonard and Robert.
    - PERSON_4337 resigned on Feb 12, 2026.
- **Contact UPDATE.** "left the board May 2025" with an edit on 2025-05-02 follows the May 1 resignation, so it is supported.
- **#executives note.** It sits 18 seconds after Leonard's 19:18:33Z post.
  - "Totals above run 2 high": the 19:09:44Z pro forma uses 3,051,881 Seed and 305,188 for the other seed investors. 3,051,879 matches the Aug 2023 disclosure schedule (`threads/leonard@harmonygames.co_1773160052067710033.json`). 2,746,693 + 305,186 = 3,051,879.
- **KPMG follow-up.** "6,000,000 common" is 3 × 2,000,000, and "3,051,879 Series Seed" matches the base. Item 4 asks about financing and the wind-down; nothing in the base contradicts it. One prose issue: O-3.
- **Sunset mail.** The formal-notice bullet is removed in both the original and Leonard's quoted copy, so the two stay consistent.
- **Notes Doc.** "reply to all on their own Board position mail from Feb 12" points at PERSON_4337's 22:05:07Z mail, which is in Leonard's mailbox. "Messages go to the email on each holder's issue" resolves for all 26 issues.
- **Sheet note.** The owner list's percentages sum to 94.13%, so "about 94%" is correct.
- **Last written contact before Feb** (the comments are unchanged since rev1; the new emails make identities checkable).

  18 of 26 issues match, on the same reading as rev1: the last written exchange visible to Leonard, Pacific or UTC date.

  | Issue | Claimed date | Base evidence |
  |---|---|---|
  | ENG-2438, 2439 | Jan 24 | |
  | ENG-2440 | Jan 30 | Slack DM D04UC0UEN2V, PERSON_3335 ↔ Leonard |
  | ENG-2442 | Jun 27, 2025 | |
  | ENG-2443 | Dec 16, 2025 | `…_1850625296912603629.json` |
  | ENG-2444, 2445, 2449 | May 18, 2024 | |
  | ENG-2446 | Oct 23 | |
  | ENG-2448 | Nov 4, 2025 | Slack DM D09R59580EM, PERSON_5275_SLACK_ID ↔ Leonard |
  | ENG-2452 | Oct 23 | |
  | ENG-2453 | Jan 7 | |
  | ENG-2455 | Apr 14 | |
  | ENG-2456 | Jan 30 UTC | |
  | ENG-2458 | Jan 30 | |
  | ENG-2460 | Jan 26 | Leonard–Brian DM D076PSEBC4D; all later Brian posts are in DMs without Leonard |
  | ENG-2461 | Oct 30 | Leonard's reply 13:47 PT on "Notice of Termination of Consulting Agreement" |
  | ENG-2462 | Oct 29 | Termination notice; next mail is Feb 2 |

  One issue is contradicted: **ENG-2447** (F-1 below).

  Seven are not individually reconciled: ENG-2441, 2450, 2451, 2454, 2457, 2459 and 2463. None has a Gmail founder contact later than its claim, and no adjacent-token Slack account exists for the externals. Slack identities for the contractors are unresolved. This is a source limit.
- **Grader-facing or padding text.** None found.

## Findings

**F-1 (FAIL, Check C: an incompatible fact in the combined state)**

- **Where.** `linear.linear_comments` `comment_2f94df42f7cb90e3d04bea2945c2c1a8` (L178), on ENG-2447. Rev3+ made ENG-2447 "Husnu Matthew Collins" with `Email: matthew.collins@harmonygames.co`. The comment body is "Last written contact I have before Feb: Jan 5, 2026".
- **Evidence.**
  - The base's last written exchange with him is **Oct 28, 2025**: Leonard's intro at 12:24 PT and Matthew's reply at 12:28 PT, "Matthew Collins <> PERSON_3083_NAME" (`threads/leonard@harmonygames.co_1847258343060233599.json`).
  - Gmail: a complete scan of his address (1,061 hits in 134 files) and a complete scan of "Matthew Collins" in from/to/cc/bcc (only that address appears) find nothing later.
  - Slack: his only account, UEC7997064E, has 0 posts and 0 mentions in 2025–26. Leonard's January DMs do not include him. The only external posters on Jan 5 are BoomBit accounts in C09SWTHEMEW.
  - Calendar: his last event is Jul 16, 2025.
- **Why it fails.** Under every reading that fits the other 18 issues, this date would be Oct 28, 2025. The note asserts a contact the base does not contain.
- **Smallest repair.** Change the body to "Last written contact I have before Feb: Oct 28, 2025". If `[PERSON_NAME_11362]` is not Matthew Collins, revert ENG-2447's title and email instead. Then rerun /injection.

**Advisories (non-blocking)**

- **O-1.** The snapshot column advisory in Check B.
- **O-2.** ENG-2441's email PERSON_3063 signs as "Arthur Schaeppi". But the title token PERSON_3083_NAME also belongs to the Solsten CEO's address PERSON_3083_EMAIL. The Nov 6, 2025 date is not found for PERSON_3063, whose last contact is May 18, 2024. The author should confirm which address and date belong to this holder.
- **O-3.** The KPMG follow-up says "Two clarifications" but now gives three (items 1, 2 and 4). Suggested fix: "A few clarifications".
- **O-4.** Anonymization conflations for /prompt:
  - `patrick@harmonygames.co` is shared by Patrick Lewis and the Solsten COO.
  - PERSON_3941 is Frederick Stone.
  - PERSON_3335 (Slack) and PERSON_3336 (email) are both Segerstråle.

## Limits

- Static review only. No live-database or schema certification.
- Seven contact notes are not individually reconciled, as listed in Check C.
- Carta holder completeness and Agent visibility belong to /prompt.

### FINAL VERDICT: FAIL

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Fix F-1, either by setting ENG-2447's contact comment to Oct 28, 2025 or by reverting the retitle. Optionally address O-2 and O-3. Then rerun /injection on the new SQL hash.

Evidence limits: Unverified schema snapshot (4 columns). Seven of the 26 persona contact notes are unreconciled because of base anonymization. No execution or live check.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
