# Deep Recheck P2: SQL revision 2 re-check

SQL: inputs_rev2/01_Universe_Inject.sql, sha256 e545b426aae5786bad5c826f73cfbb06e1cae530feffc3bf6f47d450f2499005. The prompt is unchanged.
I read the whole revision and diffed it against rev1, statement by statement:
- 9 changed lines: header; notes doc; draft sheet; slide; KPMG snippet; KPMG clarification; ENG-2447; ENG-2460.
- 11 added lines: the #executives note; 3 × Robert reply plus 3 thread-snippet UPDATEs; contacts UPDATE.
- Header counts "125 INSERT, 11 UPDATE" match the file.

Same rules as before: search through hg.py only, no SQL executed, blind to other passes.

## Status of earlier findings

| DR | Rev1 rank | Rev2 status | Evidence |
|---|---|---|---|
| DR1 Seed total 3,051,881 vs 3,051,879 | Fail | **Closed** | New C07C2866011 note, id 846a70ba2460a877e1633a18857c1734, ts 1768418331.402719 = 2026-01-14T19:18:51Z, by Leonard. It is top level, comes right after his 19:16–19:18:33 modelling posts, and has no id or ts collision; Leonard is an #executives member. Text: "the ledger has 3,051,879 seed preferred and 305,186 for the other seed investors, so the totals above run 2 high". The arithmetic holds: 10,172,939, 12,716,174, 11,444,556 and 305,188 are each 2 high. KPMG's new clarification says "our prior-year file has 6,000,000 common and 3,051,879 Series Seed". The ledger doc /docs_documents/40 also gives 3,051,879. The old figure is now explicitly superseded by its own author, and no live disagreement remains. |
| DR2 owner list "(Total … adds to 100%)" vs 94.125% | Fail (if touched) | **Closed (acknowledged)** | New note row in Leonard's draft sheet f_5ecaa967… (created 2026-02-10): "the list's percentages leave out the option pool, so they only add to about 94%". This is accurate: 94.125% listed, 5.874% pool omitted. The false parenthetical remains in the base email, but a record Leonard can see now explains it. Residual risk is low and applies only to a rater who scores the raw email without the note. |
| DR3 Feb 11 letters (Jan 31, 2026 / Jan 31, 2025) vs Carta Jan 30, 2026 | Non-fail | **Closed (ranked)** | The notes now say "Carta is the record, over any date in the letters." The answer can no longer use a letter date. NB-22's year slip stays in base, but it is now an explicitly subordinated record; at most one minor item for a strict rater. |
| DR4 Collins contact "Independent Director" | Non-fail | **Closed** | `UPDATE contacts … job = 'Investor and advisor (left the board May 2025)', updated_at = '2025-05-02T16:20:11Z'`. This fits the 1 May 2025 resignation (leonard@…_1830959847543474636, 23:42 +0100). Residual: the contact's base created_at is not in the export, so updated_at < created_at cannot be ruled out. Low risk; all injected contacts carry timestamps. |
| DR5 three advisor agreements hidden from Leonard | Conditional | **Open, unchanged** | f_7982b7ac6db8b5e2b7840a, f_c2c881ccc407fbdaeaa362 and f_e48755daf914ce68a899e0 are still unshared. This counts only if a rubric row grades advisor-specific vesting; PERSON_3941's shared agreement settles that all four grants are fully vested. |

## New and changed records, claim by claim (no new defect)

1. **Notes doc f_a37b… body.** style_runs end at 2202, which equals the body length.
   - "heads-up as a reply to all on the Feb 12 Board position thread, asking for their vote as preferred holders on the dissolution". Griffin holds 2,746,693 / 3,051,879 = 90.0% of the Series Seed. Leonard's Jan 14 #executives post 2524e876 says the Restated Certificate needs Preferred approval for "M&A / liquidation". Consistent.
   - "Carta is the record, over any date in the letters" — see DR3. "the counts go by rows" — no data claim.
   - "Messages go to the address on my investor update list". The list exists and Leonard can see it: the BCC of his 18 May 2024 "Exciting Updates and Milestones: [SOURCE_ORG_0001] Investor Report" (leonard@…_1799418746420547240). It includes PERSON_0693, "Patrick Lewis <patrick@harmonygames.co>", PERSON_2275, PERSON_3063, PERSON_2260, PERSON_5275, PERSON_1287, PERSON_3336 and PERSON_3935. The injected Investor contacts PERSON_0693 and PERSON_2275 are both on it.
   - "Tor's side letter, which Segerstrale signed too: a copy to Tor's lawyers" is supported by base:
     - The DocuSign notice leonard@…_1777587623652753593 (20 Sep 2023): "[PERSON_NAME_0089] Segerstråle viewed Complete with docusign: … Side Letter TLAS(final)".
     - leonard@…_1777585040212920288: PERSON_5275 asks Leonard about "[PERSON_NAME_6550]'s signature for the side letter".
     - The side-letter drafts (gdocs /238, /474) copy notices to Thompson Legal Advisory Services, P.C.
     - The draft signature blocks list only TOR's directors (PERSON_5137, PERSON_0711). That is a draft-vs-final difference, not a conflict.
2. **#executives note:** see DR1. The voice matches Leonard's lower-case style.
3. **KPMG clarification** (same id, thread, time 17:37:15Z and threading as rev1). The body now covers item 1 (3,051,879 carried over) and item 2 ("a line terminated on or before the as-of date counts only what had vested by its termination date"). Both agree with the ledger and with Carta's "Vested" figures. The thread snippet equals the new body start. size_estimate rises from 1206 to 1379, consistent with the longer body.
4. **Robert's reply-all on "Board position"**, Message-ID <CAGkro_Tn7wQ2xLp9VbR4mYc8KsHd3EjUf6ZaNi1oGqX5tBe0Rw@mail.gmail.com>, 2026-02-12T22:38:16Z.
   - Copies exist in all three mailboxes on threads that exist in base: leonard.hayes/1856958794180374704, robert/1856959418563541618 (base 00016903.json, which holds only Leonard's 22:14:52Z reply) and arthur.blake/1856959418725253571.
   - Threading: In-Reply-To is Leonard's <CAPBs_a5B01Fz…>, and References = original + reply. The quote header "Thu, Feb 12, 2026 at 2:14 PM leonard hayes" matches 22:14:52Z.
   - Labels per mailbox: Leonard INBOX/IMPORTANT/Opened/PERSONAL; Robert SENT; Arthur INBOX/IMPORTANT/PERSONAL, which correctly omits Leonard's user label. All three thread snippets are updated.
   - Voice: Robert's CAGkro_ id prefix and "Thanks / [PERSON_NAME_0054]" sign-off match his base mail.
   - Timing: it falls after Leonard's reply and before Robert's 23:41Z Funds Transfer note.
   - Content: "That leaves Leonard and me on the board" matches the board composition. In 2023 it was Leonard (CEO), Robert (common), PERSON_4337 (preferred) and Collins (independent); Collins resigned May 2025 and PERSON_4337 resigned Feb 12, 2026.
   - Cosmetic only: the quoted text stops after Leonard's first paragraph.
5. **ENG-2447 → "Husnu Matthew Collins".** This is the Carta name: digests leonard@…_1777100628672295991 (SSP-10) and …_1782897835407336831 (ES-9).
   - "Nov 2024 owner list: 86,470" = 25,432 Seed + 61,038 board-member options (10 Aug 2023 schedule, leonard@…_1773160163779741845).
   - "Jan 5, 2026" is now supported: on Jan 5, 2026, 22:50Z, Leonard wrote in #executives "chatting with Matthew on whatsapp".
6. **ENG-2460 → "Brian Foster".** The Carta name is "[PERSON_NAME_2769] [PERSON_NAME_0093]". They are linked through PERSON_4243:
   - Display name "brian" on the 2024 hiring and offer mails and the Feb 11, 2026 letter (leonard@…_1807411291844719379, …_1856861400116562076).
   - The Oct 2024 option mail lists PERSON_4243 for [2769][0093], 10,173 shares, vesting from 8/19/24.
   - Brian Foster (contact /160 "Game Engineer", Slack EMPLOYEE_0026) first appears in June 2024, matching PERSON_4243's June 2024 contract thread.
   - The rename keeps the same person, and 10,173 is distinguished from [PERSON_NAME_0612]'s 10,173 by ENG-2454. This is a naming overlap, not a misdescription.
7. **Draft sheet and slide.** The sheet's note row is covered under DR2. The slide now reads "Holders, per the Nov 2024 owner list" and has no count to check.

## Unchanged observations

- TOR's "Last written contact … Nov 4, 2025" (ENG-2448) is still unsupported but not contradicted. TOR's contact PERSON_5275 last appears in Leonard's mail on 18 May 2024, as an investor-update BCC.
- PERSON_3941's "Oct 23, 2025" is also still unsupported but not contradicted.
- PLATFORM anonymized-token notes from rev1 stand.

## Proposed P2 scores on rev2

| Dimension | Proposed |
|---|---|
| Cross-Service Coherence | PASS (DR1–DR4 closed; no new inconsistency). If a strict rater counts the acknowledged base remnants (DR2's raw email, NB-22), at most NON-FAIL. |
| Feasibility | PASS |
| Persona ACL Reachability | PASS (DR5 is conditional on rubric content) |
| Data Exists | PASS (the investor update list, the Segerstrale signature evidence and Griffin's preferred majority all exist and are visible to Leonard) |
| Tool Use & Cross-service | PASS |
