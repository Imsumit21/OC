# P1 re-check on SQL rev2 (sha256 e545b426aae5…), prompt unchanged

Read: the full `inputs_rev2/01_Universe_Inject.sql` changes per `sql_diff.txt`, which are:
- the notes doc (line 19)
- the draft sheet (line 26)
- the #executives note (line 52)
- the KPMG follow-up (line 86)
- Robert's Board-position reply (line 96 and its mailbox copies)
- the Matthew Collins contact UPDATE (line 115)
- ENG-2447 and ENG-2460 retitled (lines 176 and 254)
- the outline slide

Every new sentence was checked against base records through `hg.py search` only.

Proposed: **UGT 2 (FAIL)** and **Clarity 2**. F2, F3 (the KPMG figure), F4 (content), F7 and F8 are now settled. F1 and F5 are settled in part but each opens a sub-fork. F6 stays open. Two new forks come from the new text.

## F1–F9 status

| Fork | Status | Settling record / what is still open |
|---|---|---|
| F1 notice route | **SETTLED for which document** | Notes: "Notice route: the email we have. The only extra is Tor’s side letter, which Segerstrale signed too: a copy to Tor’s lawyers." This excludes the IRA/Voting Agreement copy to Orrick. It also overrides the "draft" status and the clause ending the letter on winding-up. "Tor’s lawyers" = Thompson Legal Advisory Services (side-letter draft, gdocs /docs_documents/238). **The new sentence opens F1b (below).** |
| F2 directors / preferred vote | **SETTLED** | Robert's reply-all, Feb 12 22:38 (SQL line 96, in Leonard's INBOX): "That leaves Leonard and me on the board to see the close through." Contact UPDATE for Matthew Collins: "left the board May 2025". Preferred vote is Griffin's, per the notes: "asking for their vote as preferred holders". |
| F3 KPMG item 1 | **SETTLED** | KPMG follow-up (line 86): "our prior-year file has 6,000,000 common and 3,051,879 Series Seed; if nothing has been issued since, those carry over." The #executives note (line 52, 2026-01-14 19:18:51) says "the ledger has 3,051,879 seed preferred and 305,186 for the other seed investors". Fund split 2,662,255 / 84,438 is unchanged. **This now contradicts the per-holder lines (N1 below).** |
| F4 Griffin heads-up | **SETTLED (content)**; recipients NON-FAIL | Notes: "a reply to all on the Feb 12 Board position thread, asking for their vote as preferred holders on the dissolution". Residual: the thread now has three messages. Reply-all to Robert's 22:38 message puts Robert in To with Arthur in Cc. Reply-all to PERSON_4337's original gives only PERSON_4337 and Cc PERSON_2847. PERSON_4337 and PERSON_2847 are in both, so this is Clarity 3, not a fail. |
| F5 draft recipients | **SETTLED for angels**; **F5b OPEN** | Notes: "Messages go to the address on my investor update list if they’re on it, otherwise the email we have." The list is unique: the May 18, 2024 "our first investor update" BCC (thread 1799418746420547240), and Leonard told TOR on Nov 4, 2025 "I haven’t sent any investor updates recently". It gives:<br>• ENG-2442 → PERSON_0693_EMAIL<br>• ENG-2441 → PERSON_3063_EMAIL<br>• ENG-2443 → PERSON_2260_EMAIL<br>• TOR → PERSON_5275_EMAIL<br>• ENG-2449 → PERSON_1287_EMAIL<br>• ENG-2447 (Matthew Collins) → matthew.collins@harmonygames.co, his only address<br>F5b is below. |
| F6 KPMG item 2 | **PARTLY SETTLED, still OPEN** | Settled: "a line terminated on or before the as-of date counts only what had vested by its termination date". By contrast, the Jan 30 terminations count their full grant, so the known lines total 139,993. Open: Carta's "option grant ES-9 for Husnu Matthew Collins" (digest 2023-11-17, thread 1782897835407336831) and "ES-11 for PERSON_3941_NAME [PERSON_NAME_0127]" have no amount or status on any record. ES-8 and ES-10 have no holder. Item 2's total and item 3's single figure still cannot be computed. ENG-2447 now being Matthew Collins makes ES-9 a holder line, which sharpens the gap. |
| F7 ENG-2460 told | **SETTLED** | The issue is now titled "Brian Foster", and the Feb 11 letter went "to: brian <PERSON_4243_EMAIL>" (thread 1856861400116562076). Residual NON-FAIL: the rename drops the token link to Carta's "[PERSON_NAME_2769] [PERSON_NAME_0093]" ES-15 line. The link now rests on elimination, because ENG-2454 [0612] carries the other 10,173 line and the Dec 31 letter date matches. |
| F8 count Griffin as 1 or 2 | **SETTLED** | Notes: "One row per issue on the sheet, and the counts go by rows." |
| F9 letter holder count | **Number gone; NON-FAIL** | Slide now reads "Holders, per the Nov 2024 owner list". The bullet still points the letter at the stale list, where 6 lines hold nothing per Carta. This is wording-level unless a rubric grades who the letter names. |

## New forks from the rev2 text

### F1b · "which Segerstrale signed too": does ENG-2440's notice route get the copy to Tor's lawyers? (OPEN; sheet cell)
- **Who Segerstråle is:** the ENG-2440 holder. Gmail (thread 1761203902899782263) shows "[PERSON_NAME_0089] segerstråle <PERSON_3336_EMAIL>". Drive/Docs hold "Harmony Games Advisor Agreement - Segerstråle", which was shared in Leonard's DM D04UC0UEN2V on 2023-08. Slack C096HFA5Z8W 2025-09 says "[PERSON_NAME_0089] Segerstråle (Glu Mobile, Supercell, Super Evil Meg…)". The 2023 investor list reads "[PERSON_NAME_0089] [PERSON_NAME_25152] … CEO of Super Evil Megacorp, Cofounder of Glu Mobile".
- **Reading A:** "signed too" just confirms the side letter was executed. Only TOR's row gets "+ copy to Tor's lawyers".
- **Reading B:** Segerstråle is a party to the side letter, so ENG-2440's row also gets "email we have + copy to Tor's lawyers".
- **Settled?** No. The only persona-visible side letter (/docs_documents/238) is addressed to "TOR Capital Limited" alone and has no signature block naming him.
- **Fix:** write "the only extra is Tor’s side letter (signed, Segerstrale witnessed it) — a copy to Tor’s lawyers on Tor’s row only", or name both rows.

### F5b · Employee option holders: "otherwise the email we have" when two exist (OPEN; To: of 3+ drafts)
- **Reading A:** the company address in Contacts:
  - Claire Morgan → "claire.morgan@harmonygames.co"
  - Martin Walsh → "martin.walsh@harmonygames.co"
  - Brian Foster → "brian.foster@harmonygames.co"
- **Reading B:** the personal address Leonard used for the Feb 11 letters, PERSON_2360_EMAIL, PERSON_4363_EMAIL and "brian <PERSON_4243_EMAIL>". #winddown Feb 11 19:32 supports it: "I’ll create this for all contractors and will send them to their personal accounts". So do the Google archiving plans.
- **Same split on the notice-route cell:** the notes use "the address on my investor update list" for messages but "the email we have" for the notice route. So for ENG-2441 the cell could be PERSON_3083_EMAIL or PERSON_3063_EMAIL. For ENG-2442 Contacts holds both patrick@harmonygames.co and the injected "PERSON_0693 … Investor".
- **Writes that differ:** To: on the ENG-2453, ENG-2458 and ENG-2460 drafts, and the notice-route cells for those rows and for ENG-2441/2442.
- **Not found:** no address for ENG-2459 [PERSON_NAME_0051], the holder who goes first, and none for ENG-2463 (ES-18, named Oliver Brooks in the Oct 2024 option-issuance thread 1782034095239486005), in Leonard's From/To/Contacts. That needs a P2 feasibility check.
- **Fix:** add "for staff, the personal email I sent their letter to" and "the notice route uses the same address as the message".

### N1 · Ledger total vs per-holder lines (OPEN; sheet total and per-row holdings; also P2 Cross-Service Coherence)
- **The conflict:**
  - The 10 non-Griffin Series Seed holders (ENG-2440 to ENG-2449) each hold a Carta SSP certificate (SSP-03 to SSP-12: digests of 2023-08-22, 09-11, 09-15, 09-26, 10-19, 2024-12-23).
  - Their Linear "Nov 2024 owner list" comments sum to 408,950 (81,383 + 5 × 25,432 + 31,536 + 86,470 + 50,865 + 31,536).
  - The new ledger note says "305,186 for the other seed investors".
- **Reading A:** sheet total = ledger, 6,000,000 + 3,051,879 shares, with rows copied from the Nov 2024 list. The rows then do not add up to the total.
- **Reading B:** total = the sum of the rows, 9,155,643. Or the solver reworks some rows: for example it treats PERSON_3941's 31,536 as the ES-11 option, and part of ENG-2447's 86,470 as ES-9.
- **Writes that differ:** the "Total shares and options outstanding" cell, "Each note says what they hold" for ENG-2446 and ENG-2447, and the ENG-2447 draft body.
- **Settled?** No record splits stock from options for ENG-2446 or ENG-2447.
- **Fix:** inject per-holder Series Seed counts that sum to 305,186 (a Carta cap-table mail), and give the ES-9 and ES-11 amounts. Otherwise drop the ledger note and use the Nov 2024 sum.

### N2 · ENG-2447 "Husnu Matthew Collins": what he holds (OPEN; part of N1/F6)
- Carta shows both "certificate SSP-10 … for Husnu Matthew Collins" (2023-09-14) and "option grant ES-9 … for Husnu Matthew Collins" (2023-11-17). There is no Carta termination for ES-9.
- **Reading A:** the note and row say 86,470 shares, from the Linear comment.
- **Reading B:** 86,470 shares plus a live ES-9 option grant, amount unknown. The sheet's "for options, what's vested" cell is then not determinable.
- **Settled?** No.
- **Fix:** as N1 (state the ES-9 amount, vested figure and status), or make ES-9 a lapsed line on record.

## Checked and fine
- "Carta is the record, over any date in the letters" settles the last days against the letter dates (Carta Jan 30 vs letters Jan 31; NB-22's "January 31, 2025").
- The draft sheet's pool note, "only add to about 94%", matches the Nov 2024 list: its percentages sum to 94.13% despite the mail's "(Total ownership percentage adds to 100%)". No sheet value is graded on percentages.
- Robert's reply and Leonard's 2026-01-14 note are dated before the clock. Leonard is a member of both, and Robert's reply sits in Leonard's INBOX.

Platform defects: none.
