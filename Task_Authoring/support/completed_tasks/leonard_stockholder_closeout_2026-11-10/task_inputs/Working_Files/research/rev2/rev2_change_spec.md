# rev2 change spec (draft for attack review; nothing installed yet)

Base for rev2: `task_inputs/01_Universe_Inject.sql` sha fd51afbf63aa (local rev1). Prompt `04_Prompt.txt` unchanged.
Evidence: `research/rev2/census_a_bounce.md`, `census_b_carta.md`, `census_c_alias.md`, `census_d_adv.md`,
`leak_audit.md`, `surface_handdiff.md`, `generator_map.md`.

Why: the platform pre-check (Opus 5.5, 209 counted calls) met every rule except ADV (hand grade 79.5%). The notes doc
and Linear project spell out each rule and every deciding record sits on the obvious path. rev2 adds decisions whose
deciding record is out of the way (Hardness v2 Part 8), adds no holders, rows or volume, and keeps the prompt.

## N1. BOUNCE — a done source with a missing piece (v2 trap 1, A24)
- Holder: Owen Baker, ES-12, ENG-2457 (told by his Feb 11 letter only; Julia/Claire/Brian/Martin were also told in DMs).
- Done source: Leonard in #winddown, Feb 11 "All termination letters are sent" (C0ADGSZKR3R/1770841239.761999), and the
  letter itself `leonard.hayes@harmonygames.co/<CAPBs_a5HKTOGV3nwn6iyxz8GhwLGRaF_Gs-uii3x7tVQ9eTfQQ@mail.gmail.com>`
  (thread 1856860994291529096, 2026-02-11T20:13:48Z to PERSON_3140_EMAIL).
- New record: Gmail DSN in that same thread (base convention: every base bounce sits in the original's thread), from
  PERSON_3555 (mailer-daemon), "Delivery Status Notification (Failure)", 9 s after the send, "550 5.2.1 The email account
  that you tried to reach is inactive", exact row in census_a §6; thread snippet UPDATE.
- Rule wording: the notes doc today says "Told means a written message about the closing, sent to them directly, from one
  of the three of us; for a fund, its partner." Proposed: "Told means a written message about the closing that reached
  them directly, from one of the three of us; for a fund, its partner." (alternative: keep "sent" unchanged). Reviewers:
  say which wording leaves no fork, and whether "reached" points at the trap.
- Truth: ENG-2457 Told No, Owed "Closing and last day" (Full note), State Todo; its draft must give the closing as news.
  Counts: Last day 6 → 5, Closing and last day 2 → 3 (with N2 below: 4). The draft address stays the issue email
  (the notes: "Messages go to the email on each holder's issue"); Owen's To is not graded.

## N2. EXT — a correction somewhere else (v2 trap 2, superseding)
- Line: Calvin Price, ES-3, ENG-2452. Granted 8,138, vested 4,408, termination effective Oct 24, 2025, last day Jan 24,
  2026 in Carta's termination notice (thread 1847333347700620793, 2025-10-29). Today truth: lapsed, Nothing, Canceled.
- New record: a new Gmail thread in Leonard's mailbox (id about 1856121753043675905), 2026-02-03T16:20:44Z, from Calvin's
  issue address [EMAIL_0801], To Leonard, subject "Fwd: Your option grant at [SOURCE_ORG_0001] Games Inc. has been
  updated". Body: one line from Calvin ("Forwarding this so you have it. Thanks for the extra four weeks.") then the
  forwarded Carta holder notice dated Jan 23, 2026: ES-3, Granted 8,138, Vested 4,408, Termination date Oct. 24, 2025,
  Last day to exercise Feb 20, 2026 (previously Jan 24, 2026). No question, no word about the closing.
- Rule: "Carta is the record, over any date in the letters. If a line's last day has passed, it holds nothing." Carta's
  later notice (Jan 23) gives Feb 20, which has not passed.
- Truth: ENG-2452 live: Options now 4,408, Last day 2026-02-20, Told No, Owed "Closing and last day", State Todo, one new
  draft. Options now 159,706 → 164,114. Notes 14 → 15. Who goes first: Calvin (Feb 20) before Vincent (Feb 21), so the
  #winddown reply and the sheet order change. KPMG unchanged (4,408 at Dec 31 either way).

## N3. ALIAS — the deciding fact behind an alias (v2 trap 6) — CONDITIONAL on this attack
- Holder: Husnu Matthew Collins, SSP-10 / ES-9, ENG-2447 (stock 25,432 + advisor line 61,038).
- New records: one Gmail thread + message, 2026-02-10 about 18:40Z, from Leonard to `Akin <PERSON_NNNN_EMAIL>` (a new
  personal-address token, collision-checked), no cc, subject neutral ("Harmony"), body in Leonard's voice telling him in
  writing that the company is closing; no holdings, no question, no "Matthew"/"Collins". Optional Contacts row
  first_name "Akin", job "Investor", that email.
- The link Akin = Collins exists only in old base mail (Collins signs "best / akin", thread 1847258343060233599 "Re: Akin <>
  Joe Intro"; DocuSign "Akin Babayigit viewed … Board Consent" against consents sent to Matthew Collins,
  1799069283659406996; board mail "Hi PERSON_4337_NAME and Akin").
- Truth: ENG-2447 Told Yes, Owed Already told, State Done, no note (sheet row keeps 25,432 + 61,038). Notes 15 → 14.
- Wrong-way source: ENG-2447's comment "Last mail with that address before Feb: Oct 28, 2025" (still true).

## N4. ADV un-pointed (the advisor table and the ledger decide; no record states the split)
- Delete Leonard's Jan 14 #executives top-level note (C07C2866011/1768418331.402719: "fyi the seed figures in these are 2
  off, the ledger has 3,051,879 seed preferred and 305,186 for the other seed investors, so the totals above run 2 high.
  the owner list counts the advisor options in with the stock"). Replace with a numberless thread reply under the ChatGPT
  post C07C2866011/1768416262.426129 (parent counters updated): "fyi chatgpt has the seed count a couple of shares off in
  these, go by the ledger".
- KPMG follow-up: delete "For item 1, our prior-year file has 6,000,000 common and 3,051,879 Series Seed; if nothing has
  been issued since, those carry over." and change "Three clarifications" to "Two clarifications". Items 2 and 4 stay.
- Deciding records (base): the advisor table (gdocs "Due Diligence Disclosures" f_6a37227593d0977fdbdd7a; Gmail copy
  "RE: Follow up items" …1773160163779741845: 61,038 / 30,518 / 6,104 / 6,104 = 103,764) and the ledger (term sheet gdocs
  f_11040fe5d66821bd6951aa "Inputs from ledger": 3,051,879 Series Seed, 6,000,000 common, 268,772 options). Ties:
  3,155,643 − 103,764 = 3,051,879; 408,950 − 103,764 = 305,186.
- A2 (9,295,636) is the same under both readings: tag it ASOF only.

## Kept (leak audit: none of these made the run easy)
KPMG's vested-only sentence; Robert's board reply-all; the notes' Griffin heads-up line; the Email line on every issue;
Collins's contact job line. (Leak audit: BOARD, ASOF and the Griffin ask passed on the platform-era data without them.)

## Independence
N1 (Owen, a Feb 11 letter thread), N2 (Calvin, a holder's forward in its own thread), N3 (Collins, a founder mail to an
alias), N4 (stock/option split from a doc table and the ledger) use different holders, records and services paths.
