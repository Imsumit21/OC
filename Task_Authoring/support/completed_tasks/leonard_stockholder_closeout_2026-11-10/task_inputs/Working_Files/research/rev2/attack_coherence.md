# rev2 attack: Cross-Service Coherence (cold, adversarial; P2-style deep recheck)

Scope: rev2_change_spec.md N1-N4 checked against the base (hg.py search, normal universe, clock 2026-02-14 00:00 UTC) and the overlay.
Scoring rule: any State/Lifecycle item fails; two or more low-impact items fail; one low-impact item is non-fail.

**Overlay drift during review.** The review began on 01_Universe_Inject.sql fd51afbf63aa (279 lines). At 17:40 the file
became **6ae73b6c44fb (287 lines)**, with N1 (DSN, lines 110-112), N2 (thread and message, lines 113-116) and N4 (Slack
reply plus parent UPDATE, lines 52-53; KPMG lines 85-87) drafted. N3 is not drafted (0 "Akin" hits). The findings below
cover the drafted rows as they now stand, and the spec for N3.

Status: complete

## N1 BOUNCE (Owen Baker, ES-12, ENG-2457)

### Defects
1. **Semantic, blocking until applied: the rule text still says "sent".** In 6ae73b6c44fb the notes still read "Told means a
   written message about the closing, sent to them directly ...". The bounced letter was sent, so the literal rule gives
   Told Yes, which contradicts N1's truth (Told No, "Closing and last day").
   - Fix: apply the "reached them directly" wording. The "keep 'sent'" alternative is not coherent with the truth.
2. **Format, low: "inactive" breaks the base convention for personal addresses.** In Leonard's mailbox, "550 5.2.1 ... is
   inactive" appears only for suspended harmonygames.co accounts (rachel@ 1815182275960090420; victor.barnes@
   1829704071676306712 / 1831660416587117277 / 1832293164251187803 / 1832296006757696403; thomas@ 1830949345042737324).
   The one personal-address bounce uses "is disabled. Learn more at https://support.google.com/mail/?p=DisabledUser"
   (PERSON_3158_EMAIL, 1768008486819265505 / 1768150439336785604 / 1768159419498753994).
   - Fix: use the "disabled" response line. The rest of the template already matches.

### Clean (what I checked)
- **Id and timing.** The GMR Message-ID shape matches base. 0x698ce305 = 1770840837 = 20:13:57Z, which is 9 s after the
  send (internal 1770840828000). The id has no prior use.
- **Thread placement.** Base email bounces sit in the original's thread (exports list newest first, so the bounce is at
  /messages/0; e.g. 1766170577680361145 and 1841635707568607753).
- **Labels.** All 26 base bounces in Leonard's mailbox carry INBOX(+IMPORTANT), Label_b19fb8d1b3 (= "Opened") and
  CATEGORY_UPDATES. None of Leonard's inbox mail is unread; only Spam carries "Unread".
- **Snippets.** The row snippet and the thread snippet UPDATE are both 140 characters, matching the overlay convention.
- **The other copies.** The letter was cc'd to Robert (00016874) and Arthur (arthur.blake 1856861205341126331). Each copy
  is a single message, and a bounce goes to the sender only.
- **No sign Owen got the letter.**
  - No reply in Leonard's thread.
  - Owen's work mailbox ends 2026-02-10T17:19Z (owen@ 1856759632915363101).
  - Owen's Slack posts on Feb 12 (D05S1S2AB5M, D07J501DBNE, C09UHHN6PFZ) are work talk only.
  - Feb 11 he was invited to a call ("I have some announcements to make", D05SDEQEK61 1770827705). That is not written,
    and there is no written closing notice to him in any DM or #prototype.
  - D05Q3QAH2QZ (the "shutting down harmonygames" DM) is Martin's, not Owen's.
- **The address really was dormant.** Owen gave it in Sep 2023 (Slack group DM, quoted in owen@ 1778237314398120322
  msg 3). Its last uses are Feb 2024: the lawyer thread (leonard 1789011705438137160) and the Carta acceptance digest
  (1790417238097762434). Nothing uses it in 2025-26.
- **Leonard's done line.** "All termination letters are sent" (1770841239) stays literally true.
- **Linear.** The ENG-2457 comment "No mail with that address before Feb" stays true.
- **Owen's last day.** It comes from Carta: Apr 30, 2026 (Termination details 1856960504234892536, terminated as of Jan 30).
- **KPMG.** Unchanged: Owen's termination falls after Dec 31, so his full 16,277 counts.
- **Counts.** Last day 6 → 5 and Closing and last day 2 → 3 (4 with N2) are arithmetically consistent.

## N2 EXT (Calvin Price, ES-3, ENG-2452)

### Defects
1. **Cross-service, low: the Jan 23 change left no Carta admin or board trace.**
   - Every base Carta termination produced an admin "Termination details for X" mail to Leonard: Oct 29 ×4 (including
     Calvin, 1847333347700620793) and Feb 12 ×8.
   - Option actions go through Carta board consents mailed to the board (00001961/00001963 in Nov 2023,
     00006398/00006425 in Aug 2024, 00014657/00014725 in Jul 2025). None exists in 2026.
   - In Oct 2025 Leonard asked his co-founders about the Carta terminations ("are you OK with the Carta termination?",
     #executives 1761702481.870449). No Jan 2026 Slack mentions the extension.
   - Support for the change: there is a Carta login alert at Jan 22 23:26Z (1855061354643750087).
   - Fix: either accept the absence (the holder-only notice is plausible), or add Leonard's admin copy "Termination
     details for Calvin Price" on Jan 23 with Last day Feb. 20, 2026. The second option adds a findable carrier.

### Advisory (not counted)
- **Motive.** In Oct 2025 Leonard said "my plan is to terminate all 5 on Carta so they have 90 days to decide ... I don't
  think we should keep them on the tabs" (C07C2866011 1761702408.948829–1761702450.021159). Nothing records Calvin asking
  for an extension.
  - Optional fix: "Thanks for sorting out the extra weeks I asked for."
- **Cosmetic.** The Date header uses "+0000" for a Gmail web send; base Gmail senders carry their local offset. The thread
  id 1856121753043675905 decodes to exactly .000 ms; base and rev1 inbound threads carry sub-second ms (.542, .469, .100,
  .900).

### Clean
- **Id and dates.** Thread id >> 20 = 1770135644000 = 2026-02-03T16:20:44Z. Jan 23 2026 is a Friday and Feb 3 is a
  Tuesday.
- **Sender.** An [EMAIL_nnnn] token as sender is a base convention (Arthur [EMAIL_0049], blake@ 1817982915629049978).
  [EMAIL_0801] is the address Leonard gave Carta in 2023 (leonard 1782034095239486005).
- **Forwarded notice.** SVC_0077 sender, ES-3, 8,138 granted / 4,408 vested, grant date Nov 10 2023 and termination
  Oct 24 2025 all match the Oct 29 notice. "Your option grant" has no base hit; it is a new holder-side subject.
- **Linear.** The ENG-2452 comment "No mail with that address before Feb" stays true (Feb 3 is in Feb).
- **Nothing says ES-3 lapsed.** Checked Slack 2025-11 to 2026-02 (no Calvin activity or mention), Linear, gdocs, gsheets
  (P&L salary zero after Oct), gcal and contacts.
- **Quantities.**
  - The Jan 22 term sheet's 268,772 options (gdocs f_11040fe5d66821bd6951aa, created 23:43Z) reconcile exactly with ES-3 at
    4,408: 165,008 employee + 103,764 advisor.
  - rev1's 159,706 = 55,942 + 103,764, so 164,114 = 159,706 + 4,408 is correct.
  - KPMG A2 9,295,636 = 9,051,879 + 243,757 is unchanged.
  - Order: Calvin (Feb 20) goes before ES-14 (Feb 21, 1856960478782792748).

## N3 ALIAS (Akin = Matthew Collins, ENG-2447), spec only

### Defects
1. **Temporal/semantic, low: Feb 10 18:40Z clashes with Leonard's same-day behavior.**
   - At 16:39Z Leonard deferred telling even the team ("I'll skip that until tomorrow since Blake is not in the
     meeting", #executives 1770741594.530789).
   - At 17:41Z his outreach notes say "Griffin first, then everyone else ... one email to everyone, same note".
   - On Feb 12 at 22:17Z his #winddown list still has "Reaching out to our angels properly and let them know about the
     situation" (1770934638.035469).
   - It also touches NB-29: under the Feb 10 reading of the decision date, 10:40 PST may precede finalization.
   - Fix: move the mail to Feb 12, about 22:20–23:20Z, after the list. This mirrors Robert's rev1 angel mail at 23:41Z.

### Clean
- **The alias link exists in base.** matthew.collins@ signs "best / akin" (1847258343060233599, 2025-10-28) and the 2023
  intros use "Akin, thank you for the introduction" (00000965, 00000966).
- **No other address for Akin.** Every base Akin mail uses matthew.collins@harmonygames.co, and Contacts has only that
  address. So no existing token is being overwritten.
- **Linear.** The ENG-2447 comment "Oct 28, 2025" stays true.
- **Calendar.** gcal has no Feb 10 events, so nothing conflicts.

## N4 ADV un-pointed

### Clean
- **Slack reply.** Under the ChatGPT post 1768416262.426129 (id 6a3713ea95d4fe3d4150a032195560f8, which had no replies),
  the reply has ts 1768418331.402719, matching created_at 2026-01-14T19:18:51Z. The parent UPDATE (thread_ts_legacy,
  reply_count 1, reply_users_count 1, latest_reply) matches the rev1 convention.
- **"These" is accurate.** The parent says 3,051,881 and the pro forma post 1768417784 says 305,188, so both are 2 off.
- **KPMG reply.** Body, row snippet and thread snippet are all rewritten ("Two clarifications ... For item 2"). The size
  falls 1460 → 1326 (−134), matching the deleted text.
- **Arithmetic.** 103,764 = 61,038 + 30,518 + 6,104 + 6,104, and the advisor lines tie to owner-list rows: 86,470 =
  25,432 + 61,038; 81,383 = 50,865 + 30,518; 31,536 = 25,432 + 6,104 (×2).
  - 3,155,643 − 103,764 = 3,051,879.
  - 408,950 − 103,764 = 305,186.
  - A2 comes out the same under both readings.

## Known data issues touched
- **NB-22.** Owen's bounced letter is the "January 31, 2025" letter (Robert's copy 00016874). Do not grade Owen's
  termination date; his last day comes from Carta (Apr 30, 2026).
- **NB-29.** Touched by N3's Feb 10 date; moving the mail to Feb 12 avoids it.
- **NB-24.** The overlay's Linear comments ("Last mail with that address ...") stay true under all four changes.
- **NB-1, NB-15.** Not affected: no channel posts are added after Feb 11, and the contractor wording is not graded.

## Verdict per change
- **N1:** non-fail (one low item), provided the "reached" wording is applied. If "sent" is kept, the change fails as a
  rule/truth contradiction.
- **N2:** non-fail (one low item).
- **N3:** non-fail (one low item); move it to Feb 12.
- **N4:** clean.
- **State/Lifecycle:** none found. Nobody acts after closing or leaving: Calvin's forward is from his personal address
  months after termination, Owen's account is only bounced, and Akin is an ex-director writing as an investor.
