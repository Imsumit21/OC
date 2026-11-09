# P2 (cold): Services, data and access

Pass P2 of the deep recheck (`Evals/references/rules/deep_recheck.md`), with Eval 1 §3.2 Cross-Service Coherence and §2.2 Feasibility. I ran it blind and on my own. The universe is normal, Feb 14, 2026 (Clock: 2026-02-14 00:00 UTC), persona Leonard Hayes `<leonard.hayes@harmonygames.co>`.

**Scope checked:**
- All 5 prompt sentences.
- All 136 SQL statements (125 INSERT, 11 UPDATE). I checked each one claim by claim against the base.
- The base records the task leans on:
  - the Nov 2024 owner list
  - 14 Carta "Termination details" notices
  - 6 Feb 11 letters
  - the advisor tables
  - the reset term sheet
  - the Series Seed SOP mail
  - the Board-position, Sunset and KPMG threads
  - #winddown Feb 2026 and #executives Jan/Feb 2026
  - Task List.xlsx, the Wind Down folder and the Option Issuances thread
  - holder mail in all mailboxes, and holder Slack DMs where they exist
- SQL quotes balance and every apostrophe is doubled.
- No ID collides with the base: Drive, Linear ENG-2438..2463, Trello idShort 456, Gmail thread and Message-IDs, and Slack ids.
- All Message-ID threading resolves to base messages.

## Verdict (Cross-Service Coherence): FAIL

| | Dimension | Result |
|---|---|---|
| Fail | Cross-Service Coherence | **F1** confirmed-level. **F2** borderline, but it falls in an always-fail category. Separately, N1–N3 are three low-impact items, and two or more low-impact items fail on their own. |
| Non-fail | Feasibility | PASS. Every write is cataloged and every needed record exists. |
| Non-fail | Persona access | PASS, with one evidence limit (N4). |
| Non-fail | Data exists | PASS (the N4 caveat applies). |
| Non-fail | Tool use and cross-service | PASS. Gmail, Linear, Slack and the Drive family each change a graded fact. |

---

## FAIL-ranked findings

### F1: one email address belongs to two holders; the injected Linear comments make it a contradiction (Cross-service Referential / Identifier)

**Injected side:**
- SQL lines 157–162, `linear.linear_issues` **ENG-2444**: `'Patrick Lewis'`, `'Email: patrick@harmonygames.co'`.
  - Comment `comment_ddac696381e399e80cb72b2eed4ba3d2`: `'Last written contact I have before Feb: May 18, 2024'`.
- SQL lines 145–150, **ENG-2442**: `'[PERSON_NAME_4468]'`, `'Email: PERSON_0693_EMAIL'`.
  - Comment `comment_3553af035a9738781951b795e0e0cedc`: `'Last written contact I have before Feb: Jun 27, 2025'`.

**Base side (all in Leonard's mailbox):**

`patrick@harmonygames.co` is Patrick Lewis's address in the seed-round records:
- `threads/leonard@harmonygames.co_1770141224265557526.json` /messages/0 (Jun 30, 2023): "Patrick Lewis … Üsküdar İstanbul > patrick@harmonygames.co > 25.000 usd".
- `threads/leonard@harmonygames.co_1799418746420547240.json` /messages/2, Sat 18 May 2024 12:29:07 -0700. The investor report is BCC'd to "Patrick Lewis <patrick@harmonygames.co>" and to "PERSON_0693_NAME <PERSON_0693_EMAIL>".

The same address writes to Leonard after May 18, 2024, signed as [PERSON_NAME_4468]:
- `threads/leonard@harmonygames.co_1836075678772806708.json` /messages/0, Fri 27 Jun 2025 02:56:56 -0700. From `patrick <patrick@harmonygames.co>` to Leonard, "Ask for support", signed "*[PERSON_NAME_4468]* Co-founder // COO patrick@harmonygames.co".
- `…_1833542911997635888.json` (May 30, 2025): from patrick@, cc PERSON_0693_EMAIL, bcc Leonard, signed "*[PERSON_NAME_4468]*".
- `…_1806215566714640829.json` (Aug 1, 2024) and `…_1802832312010970202.json` (Jun 28, 2024): further patrick@ mail with Leonard.

[PERSON_NAME_4468] is also tied to PERSON_0693_EMAIL:
- `…_1773213846196143460.json` (Aug 2023): "*[PERSON_NAME_4468]* … via email: PERSON_0693_EMAIL".

**The contradiction:**
- ENG-2444 says the last written contact with patrick@harmonygames.co was May 18, 2024. Gmail shows four later written messages from that address, the latest on Jun 27, 2025.
- ENG-2442's "Jun 27, 2025" can only come from that same patrick@ email. No record reaches PERSON_0693_EMAIL on that date.
- So the injected records treat patrick@ as [PERSON_NAME_4468]'s address and also as Patrick Lewis's address.
- The root cause is a collision in the base anonymization, but the injected comments surface it as a direct Linear-vs-Gmail conflict.

**Knock-on:** the notes say "Messages go to the email on each holder's issue" and "At most one note per person". Under those rules, a Patrick Lewis note would go to an address the 2024–25 mail shows as [PERSON_NAME_4468]'s. [PERSON_NAME_4468] also has his own issue and address. This is also a UGT risk for P1.

**Smallest fix:**
- Preferred: drop the two "Last written contact" comments on ENG-2442 and ENG-2444. They are decoys, and no rule reads them.
- Alternative: key both comments by the issue address.
  - ENG-2444 → "Jun 27, 2025": the latest patrick@harmonygames.co mail, Fri 27 Jun 2025 02:56:56 -0700.
  - ENG-2442 → "May 18, 2024": the latest mail reaching PERSON_0693_EMAIL from one of the three, Sat 18 May 2024 12:29:07 -0700.
  - This alternative still leaves the base signature token mismatch, which is a platform token issue.

### F2 (borderline): the base owner list states a total its lines don't reach (Quantitative; §3.2 says this category always fails)

**Base side:**
- `threads/leonard@harmonygames.co_1816809274978043917.json` /messages/0 (Tue 26 Nov 2024 10:47:40 -0800). The same text is in `threads/blake@harmonygames.co_1816806726955267951.json` /messages/0.
- It lists 27 owner lines with "% diluted ownership" and says "(Total ownership percentage adds to 100%)".
- The listed percentages sum to **94.129%**. The shares sum to 9,477,719, against an implied denominator of about 10,069,261.

**Injected side, which makes the disagreement explicit:**
- `gsheets.sheets_sheets` `f_5ecaa967db3adcfa440b09`, grid last row: "the list's percentages leave out the option pool, so they only add to about 94%".

**Why it is task-touched:**
- All 26 Linear comments cite "Nov 2024 owner list: …".
- Slide `el_b4a6a6d9a533` says "Holders, per the Nov 2024 owner list".
- Slack `846a70ba2460a877e1633a18857c1734` says "the owner list counts the advisor options in with the stock".

**Why it is only borderline:**
- It is a person's wrong parenthetical in an email, not a table aggregate.
- The share line items reconcile with Carta and the term sheet: 6,000,000 + 3,051,879 + 425,840 options, including 103,764 advisor options.
- The main session may reject it as speech rather than data.

**Smallest fix:** UPDATE `gmail.gmail_messages` body (and snippet, if it carries the text) on both copies to delete the sentence "(Total ownership percentage adds to 100%)". There is no other change that leaves the decoy intact.

---

## Non-fail findings (low-impact)

Three of these are scored inconsistencies: N1, N2 and N3. Under the strict rule, two or more such items fail even without F1 and F2.

**N1: date slip in a letter (NB-22).**
- `threads/leonard@harmonygames.co_1856860994291529096.json` /messages/0 (Wed 11 Feb 2026 12:13:48 -0800, to PERSON_3140_EMAIL) says "effective January 31, 2025".
- Carta `…_1856960504234892536.json` says [PERSON_NAME_0068] was "terminated … as of Jan. 30, 2026" (ES-12, last day to exercise April 30, 2026).
- Linear ENG-2457 uses the same PERSON_3140_EMAIL.
- The letter is still read as "told" evidence. The notes ("Carta is the record, over any date in the letters") stop the wrong year from reaching the answer.
- Per date-slip severity, it changes no order, window or count, so it is minor.
- Fix: none needed beyond the existing Carta rule. Optionally UPDATE the letter's year to 2026.

**N2: letters and Carta disagree by one day (Cross-service).**
- The letters to Marcus (`…_1856861323365646598.json`) and Martin (`…_1856861229984402233.json`) say "effective January 31, 2026".
- Carta says "as of Jan. 30, 2026" (`…_1856960351896429942.json`, `…_1856960563574318616.json`).
- The Carta rule neutralizes it. A contract end date versus the last service day is plausible.
- Fix: none required. Optionally make the two dates agree.

**N3: four injected "last written contact" dates match no record in any service.** Each claims a later contact than any mail or Slack record shows; none is contradicted outright.
- ENG-2440 `comment_2111c140a4689c9cea5bf649e0035f4f` says "Jan 30, 2026". The latest PERSON_3336_EMAIL mail is Jan 7–8, 2026 (`…_1853682990477206418.json`).
- ENG-2446 `comment_828018862b6830931b07005fb37392cd` says "Oct 23, 2025". The latest PERSON_3941_EMAIL mail is Sep 15, 2025 (`…_1843007315645862923.json`).
- ENG-2447 `comment_2f94df42f7cb90e3d04bea2945c2c1a8` says "Jan 5, 2026". The latest Matthew Collins mail is Oct 28, 2025 (`…_1847258343060233599.json`), and Slack user UEC7997064E has no messages.
- ENG-2448 `comment_3d28d40e61eb9113c2705fc13e05fd11` says "Nov 4, 2025". The latest PERSON_5275_EMAIL mail is Sun 19 May 2024 (`…_1799418746420547240.json` /messages/0).
- None of these people has Slack messages or 2025–26 mail in Robert's or Arthur's mailboxes.
- Fix: set each to the record date above, or drop it.

**N4: persona access and evidence limit (not counted as an inconsistency).**
- The vesting terms for the Matthew Collins (61,038), Segerstråle/[PERSON_NAME_0089] (30,518) and PERSON_1287 (6,104) advisor grants sit only in Resource-owned docs with `shared_with []`: `f_c2c881ccc407fbdaeaa362`, `f_e48755daf914ce68a899e0`, `f_7982b7ac6db8b5e2b7840a`.
- Only PERSON_3941's agreement (`f_3ee38465decc57e61df6e5`, "vest … monthly over a 2-year period", Jul 21, 2023) is shared with Leonard.
- The holder sheet's "for options, what's vested" for those three rests on assuming the shared "Founder Advisor Standard Template".
- Fix: share one more agreement with Leonard, or state the advisors' full vesting in a record Leonard can see.

## Watch items (not scored)

**Platform token collisions.** The platform note says to treat tokens as the source string:
- "Hi [PERSON_NAME_0040]" opens two different letters (PERSON_2361, PERSON_2360).
- PERSON_3083_NAME is both Arthur Blake's signature (Nov 2024) and the holder "Arthur PERSON_3083_NAME".
- [PERSON_NAME_0038] is both the display name of frederick.stone@ and the 127,162 option holder.
- The 30,518 advisor appears as [PERSON_NAME_6201], [PERSON_NAME_0090] and [PERSON_NAME_6407]. Leonard-visible DocuSign mail resolves it: "[PERSON_NAME_0089] [PERSON_NAME_25152] viewed … Advisor Agreement - Segerstråle.pdf" (`…_1777096000955189741.json`).

**Other watch items:**
- NB-29 decision date. #winddown and #executives agree on Feb 9 ("at least we finalized the decision to shut down", Feb 9 21:33). The Feb 10 reading is only in #leapblock, which the task does not name. It matters only if the KPMG item-4 answer gets a date.
- On Oct 29, 2025, #executives says "my plan is to terminate all 5 on Carta", but Carta sent four notices that day. The fifth may be [PERSON_NAME_0051], terminated Nov 21, 2025 and recorded only Feb 12.

## Checks that passed (summary)

**Seed and option figures:**
- Seed figures agree:
  - injected #executives "3,051,879 … 305,186" (Jan 14, 2026 19:18:51)
  - the term sheet ledger (gdocs #40: "Series Seed Preferred … 3,051,879", Griffin 2,746,693)
  - the SOP mail (`…_1771880236343640719.json`: 2,662,255 + 84,438)
  - KPMG's "3,051,879 Series Seed"
- Term-sheet "Options outstanding: 268,772" reconciles exactly with Carta as recorded on Jan 23: advisors 103,764 + Oct-terminated vested 54,529 + full grants of the 8 later lines 110,479.

**Carta:**
- All 14 notices are Leonard-only and agree with the Option Issuances thread and all 26 Linear owner-list comments.
- [PERSON_NAME_0100] ES-2 lapsed Nov 1, 2024, which explains "Not on the Nov 2024 owner list".

**People, directors and mailboxes:**
- Matthew Collins resigned from the board May 1, 2025 (`…_1830959847543474636.json`), consistent with the contact UPDATE "left the board May 2025". The directors list (Nov 2023) is consistent with Robert's "That leaves Leonard and me".
- Robert's two injected mails both cc Leonard. No Robert- or Arthur-only 2026 holder mail exists, so nothing a holder was told is hidden from Leonard.

**Slack:**
- All Slack authors are channel members: Leonard and Arthur in C0ADGSZKR3R, Leonard in C07C2866011.
- The thread counters are right (reply_count 4, reply_users_count 2, latest_reply = Arthur's ts).
- All posts are before the NB-6 cutoff.

**Timestamps and threads:**
- Timestamps, internal_date, quoted "On … wrote:" headers, Trello IDs (Feb 12 22:54:08 and Feb 13 18:14:27) and Gmail thread-id epochs are consistent.
- The final snippet of each thread is its latest message.

**Visibility:** everything Leonard must read is owned by him, shared with him, a Slack channel he belongs to, his own mailbox or calendar, or in an unscoped service (Linear, Trello, Contacts).

**Writes:** all cataloged:
- `gsheets_create_spreadsheet`, `gdocs_create_document`, `gdrive_move_file`, `gdrive_share_file`
- `gmail_create_draft`, `gmail_reply_to_message` (reply_all)
- `slack_send_message` (thread_ts)
- `linear_update_issue`, `linear_create_comment`. The states Todo, Done and Canceled exist in the base.

## DR lines

```
DR1 | P2 | §3.2 cross-service referential / identifier | "the messages to holders as drafts in my Gmail, the Linear issues" | linear ENG-2444 'Email: patrick@harmonygames.co' + comment_ddac696381e399e80cb72b2eed4ba3d2 'Last written contact I have before Feb: May 18, 2024'; ENG-2442 comment_3553af035a9738781951b795e0e0cedc 'Jun 27, 2025' vs gmail threads/leonard@harmonygames.co_1836075678772806708.json /messages/0 'Fri, 27 Jun 2025 … from patrick <patrick@harmonygames.co> … *[PERSON_NAME_4468]* Co-founder // COO' | Cross-Service Coherence | FAIL (2)
DR2 | P2 | §3.2 quantitative | "my close-out notes doc has how each holder gets handled" (owner list is the notes' decoy source) | gmail threads/leonard@harmonygames.co_1816809274978043917.json /messages/0 '(Total ownership percentage adds to 100%)' (27 listed % sum 94.129) vs gsheets f_5ecaa967db3adcfa440b09 'they only add to about 94%' | Cross-Service Coherence | FAIL (2), borderline
DR3 | P2 | §3.2 temporal (NB-22) | "the way those lay it out" | gmail …_1856860994291529096.json 'effective January 31, 2025' vs Carta …_1856960504234892536.json 'as of Jan. 30, 2026' | Cross-Service Coherence | NON-FAIL (minor)
DR4 | P2 | §3.2 cross-service | "the way those lay it out" | letters …_1856861323365646598.json / …_1856861229984402233.json 'effective January 31, 2026' vs Carta …_1856960351896429942.json / …_1856960563574318616.json 'as of Jan. 30, 2026' | Cross-Service Coherence | NON-FAIL (minor)
DR5 | P2 | §3.2 referential (unresolved) | "the Linear issues" | ENG-2440 'Jan 30, 2026', ENG-2446 'Oct 23, 2025', ENG-2447 'Jan 5, 2026', ENG-2448 'Nov 4, 2025' vs latest records Jan 8 2026 / Sep 15 2025 / Oct 28 2025 / May 19 2024 | Cross-Service Coherence | NON-FAIL (minor)
DR6 | P2 | §2.2E persona read / data exists | "That's the holder sheet …" (Sunset: "for options, what's vested") | advisor agreements f_c2c881ccc407fbdaeaa362, f_e48755daf914ce68a899e0, f_7982b7ac6db8b5e2b7840a shared_with [] (only f_3ee38465decc57e61df6e5 shared with Leonard) | Feasibility | NON-FAIL (evidence limit)
```

Checked: 5 prompt sentences, 136 SQL statements, about 60 base records.
