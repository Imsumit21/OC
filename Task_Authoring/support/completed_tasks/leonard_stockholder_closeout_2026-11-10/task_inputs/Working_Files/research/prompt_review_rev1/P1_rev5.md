# P1 re-check on SQL rev5 (sha256 ee52cd4c2582…), prompt unchanged

Diff vs rev3, confirmed by a full-file diff with 4 changed lines:
- notes doc line 12 (Griffin heads-up)
- notes doc line 23 (notice route)
- the notes doc style-run end offset
- the ENG-2448 description

Nothing else changed.

## Griffin heads-up recipients: SETTLED
- **Notes:** "Griffin’s partner gets a heads-up as a reply to all on their own Board position mail from Feb 12, asking for their vote as preferred holders on the dissolution."
- **"Their own Board position mail from Feb 12"** can only be PERSON_4337's "Board position" message (Message-ID `<BYAPR02MB435880CCF501BE0AE906AFFDC460A@BYAPR02MB4358.namprd02.prod.outlook.com>`, 2026-02-12 22:05:07 UTC, from PERSON_4337 to Leonard, Cc PERSON_2847). The other two replies in that thread are Leonard's own (22:14) and Robert's (22:38).
- **Result:** reply-all from Leonard on that message goes To PERSON_4337, Cc PERSON_2847. This removes the rev2 Robert/Arthur cc difference and closes the Clarity residual.

## Notice-route sentence: no fail-level fork; one wording residual
- **Notes:** "Notice route: the legal-notice address on their issue where it gives one, otherwise their email. The only extra is for Tor and Segerstrale, who are both on Tor’s side letter: a copy to Tor’s lawyers."
- **ENG-2448** now reads "Email: PERSON_5275_EMAIL\nLegal notices: [EMAIL_15398]". "[EMAIL_15398]" is grounded: the side-letter draft (gdocs /docs_documents/238) addresses TOR at "Attn: [EMAIL_15398]". It is the only issue with a "Legal notices:" line (grep count 1).
- **Resulting notice-route cells:**
  - TOR: [EMAIL_15398] plus a copy to Tor's lawyers (Thompson Legal Advisory Services).
  - Segerstråle (ENG-2440): PERSON_3336_EMAIL plus a copy to Tor's lawyers.
  - Every other row: its issue "Email:" address.
- **Messages are not affected:** "Messages go to the email on each holder’s issue" still points the TOR draft at the "Email:" line (PERSON_5275_EMAIL), not the legal-notice line. That bullet is labelled and separate, so there is no fork.
- **Residual (Clarity 4 if kept, not a UGT fail):** rev3 said "the email on their issue". rev5's fallback "otherwise their email" drops "on their issue". A literal reader could take the notice cell for holders with a second known address from that other address, for example:
  - ENG-2441: PERSON_3083_EMAIL vs the issue's PERSON_3063_EMAIL
  - ENG-2442: patrick@harmonygames.co vs PERSON_0693_EMAIL
  - ENG-2453: claire.morgan@harmonygames.co vs PERSON_2360_EMAIL
  - ENG-2440: PERSON_3335_EMAIL vs PERSON_3336_EMAIL
- **Why it is not a UGT fail:** the same clause anchors on "on their issue", and the Messages bullet makes the issue's "Email:" line the holder's email. No record names a different notice email for those holders.
- **One-phrase fix:** "otherwise the email on their issue".

## Scores (P1 scope, rev5)
- Unique Ground Truth: **5**. F1–F9, F1b, F5b, N1, N2 and F6 are all settled by quoted records, as in P1_rev2.md and P1_rev3.md, and the Griffin recipients are now settled too.
- Clarity: **4**. The only residual is "otherwise their email". With the fix it would be 5.

Platform defects: none.
