# P2 (cold): rev11 confirmation

- SQL: `inputs_rev11/01_Universe_Inject.sql`, sha256 `40ce7beff0d924d0…` (matches the stated hash).
- I read the diff against rev7. Only three things change: the KPMG clarification body and its thread snippet, and the 26 Linear first comments.
- Universe: normal, Feb 14, 2026 (Clock: 2026-02-14 00:00 UTC).

## Spot-check: comment date = latest pre-Feb mail with the issue's `Email:` address in Leonard's mailbox

I keyed each check on the from/to/cc/bcc headers, using complete scans of `threads/leonard@harmonygames.co_*`.

| Issue | Address | rev11 comment | Latest pre-Feb message found | Match |
|---|---|---|---|---|
| ENG-2440 | PERSON_3336_EMAIL | Jan 8, 2026 | Leonard reply, bcc PERSON_3336, 2026-01-08 08:38 PT (`…_1853682990477206418`) | ✓ |
| ENG-2442 | PERSON_0693_EMAIL | May 30, 2025 | patrick@ mail cc PERSON_0693, Fri 30 May 2025 03:59 -0700 (`…_1833542911997635888`); no later mail | ✓ |
| ENG-2444 | patrick@harmonygames.co | Jun 27, 2025 | "Ask for support", Fri 27 Jun 2025 02:56:56 -0700 (`…_1836075678772806708`) | ✓ |
| ENG-2446 | PERSON_3941_EMAIL | Sep 15, 2025 | "Fwd: Follow-up on intros", 2025-09-15 19:27 UTC (`…_1843007315645862923`) | ✓ |
| ENG-2447 | matthew.collins@harmonygames.co | Oct 28, 2025 | "Matthew Collins <> PERSON_3083_NAME", 2025-10-28 13:24 PT (`…_1847258343060233599`) | ✓ |
| ENG-2448 | PERSON_5275_EMAIL | May 19, 2024 | TOR reply, Sun 19 May 2024 15:17:49 +0200 (`…_1799418746420547240`); 142 header hits, none later | ✓ |
| ENG-2441 (extra) | PERSON_3063_EMAIL | May 18, 2024 | Investor-report BCC, Sat 18 May 2024 12:29:07 -0700 | ✓ |
| ENG-2455 (extra) | victor.barnes@ | Jul 11, 2025 | 2025-07-11 19:06:10 UTC (`…_1837378590377771160`) | ✓ |
| ENG-2456 (extra) | marcus.bennett@ | Dec 29, 2025 | 2025-12-29 18:30:11 UTC (`…_1852868408136317821`) | ✓ |
| ENG-2460 (extra) | PERSON_4243_EMAIL | Aug 15, 2024 | Thu 15 Aug 2024 21:40:02 +0300 (`…_1807411291844719379`) | ✓ |
| ENG-2463 (extra) | PERSON_1174_EMAIL | Aug 8, 2024 | Thu 8 Aug 2024 12:11:25 -0300 (`…_1805529066540243862`) | ✓ |

Results:
- All 11 dates match, and no injected comment now contradicts Gmail.
- **F1 is resolved.** The comments no longer assert who owns patrick@. The base email collision remains ([PERSON_NAME_4468] signing from Patrick Lewis's address). It is a platform anonymization artifact and is not scored.
- **N3 is resolved.**
- **KPMG:** the follow-up now says "Three clarifications" and lists exactly three (items 1, 2 and 4). The count and the snippet match. Item 4 now asks "whether the company is winding down", so it no longer depends on a decision date (the NB-29 watch item is closed).

## Remaining items

| # | Status | Item |
|---|---|---|
| F2 | **FAIL (sole blocker; borderline)** | Base Nov 26, 2024 owner list (`leonard.hayes@harmonygames.co/1816809274978043917` /messages/0; same in `arthur.blake@…/1816806726955267951` /messages/0) says "(Total ownership percentage adds to 100%)". Its 27 listed percentages sum to 94.129%. The task leans on this record: every Linear comment and the outline cite it, and the Jan 14 #executives message corrects it. The draft-sheet note ("only add to about 94%") puts the disagreement in two records; it does not remove it. §3.2 says a Quantitative inconsistency (line items that do not sum to the stated total) always fails, whether or not anyone would miss it. **Smallest fix:** UPDATE `gmail.gmail_messages.body_text` on both copies to delete that one sentence; the sheet note then stays true. If the main session treats the parenthetical as a person's misstatement rather than data, this item is rejected. |
| N1 | Non-fail (minor, counted) | NB-22. The PERSON_3140 letter says "effective January 31, 2025"; Carta says Jan 30, 2026. The answer follows Carta under the notes' rule, so no order, window or count changes. |
| N2 | Note (not counted) | The letters' Jan 31, 2026 and Carta's Jan 30, 2026 are different fields (contract end vs equity termination). The notes' "Carta is the record" settles it. |
| N4 | Evidence limit | Three advisor agreements carrying vesting terms are not shared with Leonard. Their status is inferable from the shared PERSON_3941 template. |

## Final Cross-Service Coherence verdict: FAIL

- **Why:** F2 alone. It falls in an always-fail Quantitative category.
- **If F2 is fixed, or rejected by the main session:** only N1 is left, a single minor item, and the verdict becomes NON-FAIL.
- **The other dimensions are unchanged:** Feasibility, Persona access, Data exists and Tool use and cross-service all pass.
