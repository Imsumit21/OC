# P1 re-check on SQL rev7 (sha256 045f64bd8055…), prompt unchanged

What I compared: a full-file diff against rev5, with comments ignored.

What changed:
- The notes doc drops the "Notice route" bullet.
- The Sunset intake mail drops "How each holder gets formal notice, including any special terms", and so does its quoted copy in Leonard's reply.
- ENG-2448's description is back to "Email: PERSON_5275_EMAIL".
- The outline slide's first section reads "What happened\nWhy we are closing".
- The KPMG follow-up adds "For item 4, we need any new financing and the decision to wind down."

Nothing else changed.

## Status
- **Notice route:** out of scope. Neither the notes doc nor the Sunset list asks for it any more, so my rev5 Clarity residual about the "otherwise their email" fallback no longer applies.
- **KPMG item 4: SETTLED as a closed set.** The follow-up says "For item 4, we need any new financing and the decision to wind down." That gives two entries:
  - New financing since Dec 31, 2025: none. The Jan 2026 SAFE and bridge talks never closed, and Leonard's Feb 9 mail to Sherwood says "We have preferred stock from a seed round (no SAFEs)". The $22,500 data licence with Sunset is a sale, not a financing.
  - The decision to wind down.
- **Decision date: BOTH_FAIR_FIGURE candidate, not a UGT fail.** The reply makes the same write either way, but the date of the decision has two values on persona-visible records:
  - **Feb 9, 2026.** Leonard's mail to PERSON_4337 on Feb 9 says "we’ve decided to shut the company down". #executives on 2026-02-09 21:33 says "at least we finalized the decision to shut down".
  - **Feb 10, 2026.** #leapblock on 2026-02-11 20:54 says "We didn’t finalize this decision until yesterday."
  - This is known data issue NB-29.
  - The rubric should accept Feb 9 or Feb 10, or not grade the date.
- **Letter slide:** "Why we are closing" removes the "when the team stopped" date.
- **Earlier forks:** everything settled through rev5 still holds. That covers F1–F9, F5b, F6, N1, N2 and the Griffin recipients. None of the rev7 changes touch those records.

## Non-UGT note for P3/P4
- The KPMG follow-up still opens "Two clarifications on our side" but now lists three items (1, 2 and 4). The count is a slip inside the record. No graded value depends on it. Fix: change it to "A few clarifications" or "Three clarifications".

## Scores (P1 scope, rev7)
- Unique Ground Truth: **5**, with one BOTH_FAIR_FIGURE: the decision date, Feb 9 or Feb 10.
- Clarity: **5**.

Platform defects: none. NB-29 is noted above as a known data issue.
