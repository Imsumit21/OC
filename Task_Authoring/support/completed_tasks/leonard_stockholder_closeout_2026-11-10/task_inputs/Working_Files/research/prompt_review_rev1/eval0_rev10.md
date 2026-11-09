# Injection Data-Integrity Review (Eval 0) — SQL rev10

| Item | Value |
|---|---|
| Stage | `/injection` |
| Review version | `injection-static-v2` |
| Evidence contract | `stage-evidence-v1` |
| Mode | Local static audit. No SQL executed. Nothing written under `Evals/`. |
| Review time | 2026-11-08 (machine clock) |
| Clock | 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) |
| Universe | `Universe_Normal`. Manifest sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450`. |
| Input | `$R/inputs_rev10/01_Universe_Inject.sql`, 84,227 bytes |
| Input sha256 | **`7d73038e5e44313c79afc8a18aff8f5c07ab7a13adfd1066cae5250c05621cd2`** |
| Statements | 138: BEGIN, 125 INSERTs, 11 UPDATEs, COMMIT |
| Lint | `injection-lint-v1`: 0 FAIL / 0 CHECK / 0 INFO. Output `out/scratch_e0r10/lint.json`, sha256 `17d52710…`. |

`$R` = `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/prompt_review_rev1`.

## Reuse

Every check on the unchanged statements is carried from `$R/out/eval0_final.md` (rev7, sha256 `045f64bd…09d0`). That report holds the full ledger, the Checks A–C evidence and the holder identity and contact tables.

Reuse is valid because my own parse diff shows 135 of the 138 statements are byte-identical to rev7. The source manifest, clock and rules are also unchanged.

## Changed statements vs rev7 (3 statements)

| Line | Statement | Change | Check |
|---|---|---|---|
| L177 | `linear.linear_comments` `comment_2f94df42f7cb90e3d04bea2945c2c1a8` (ENG-2447) | Body is now "Last written contact I have before Feb: Oct 28, 2025" | See F-1 below. Timestamps unchanged (2026-02-12T23:36:26Z). |
| L84 | UPDATE `gmail.gmail_threads` `leonard.hayes@harmonygames.co/1857029474983245439` | Snippet now begins "Thank you Leonard. Three clarifications…" | Equals the new snippet on the latest message. PASS |
| L85 | INSERT `gmail.gmail_messages` `<LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@…>` (KPMG follow-up) | "Three clarifications". Item 4 reads "we need any new financing and whether the company is winding down." size_estimate 1460. | Count now matches the three items (1, 2, 4), closing O-3. Snippet = body prefix. internal_date, date and headers unchanged and consistent. "whether the company is winding down" asks rather than asserts, so nothing in the base contradicts it. PASS |

### F-1 status: closed

The base's last written exchange with Matthew Collins is Oct 28, 2025. Leonard sent an intro at 12:24 PT and Matthew replied at 12:28 PT, in `threads/leonard@harmonygames.co_1847258343060233599.json`.

The search scope that established this was complete:

- **Gmail:** all mail to or from his address, and all header occurrences of his name.
- **Slack:** his account UEC7997064E has no posts or mentions in 2025–26.
- **Calendar:** his last event is in July 2025.

The new comment value matches that date. ENG-2447's title and email are unchanged and remain supported by the base Carta records and the base contact.

## Checks

| Check | Result | Evidence |
|---|---|---|
| A — Records, references and IDs | PASS | No ID or target changed from rev7. The comment's ID, issue reference and author are unchanged. |
| B — SQL structure and supported schema rules | PASS | Independent parse and lint agree. Counts, JSON and Linear formats are all valid. The notes doc runs end at 2,032, its body length. Advisory O-1 remains: four columns are absent from the unverified snapshot (`slides_pages.notes`, `slides_page_elements.table_json` and `.ordinal`, `linear_projects.links_json`). |
| C — Dates, relationships and consistency | PASS | Every event timestamp is at or before 2026-02-13T18:21:46Z; only the Feb 17 calendar plan fields are later. Encoded times are consistent on all 10 Gmail and 8 Slack inserts. 19 of 26 "last written contact" notes are now verified against the base, none contradicted. The other 7 are source-limited by anonymization (ENG-2441, 2450, 2451, 2454, 2457, 2459, 2463), with no contradicting record found. |

## Remaining advisories (non-blocking)

- **O-1:** the schema snapshot columns noted under Check B.
- **O-2:** ENG-2441's email PERSON_3063 signs as "Arthur Schaeppi", but the title token PERSON_3083_NAME also belongs to the Solsten CEO's address. The author should confirm which address and date belong to this holder.
- **O-4:** base anonymization conflations matter for /prompt:
  - `patrick@harmonygames.co` is shared by Patrick Lewis and the Solsten COO.
  - PERSON_3941 is Frederick Stone.
  - PERSON_3335 (Slack) and PERSON_3336 (email) are both Segerstråle.

### FINAL VERDICT: PASS

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Proceed to /prompt. Optionally address O-1 and O-2 first.

Evidence limits:
- Static review only; no execution or live-database check. The schema snapshot is unverified, and 4 of the columns used are not in it.
- 7 persona contact notes could not be matched to a holder identity because of base anonymization. No contradiction was found for any of them.

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
