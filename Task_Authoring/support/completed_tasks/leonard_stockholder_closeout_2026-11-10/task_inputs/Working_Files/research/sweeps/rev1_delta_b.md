# Rev1 delta B: cold check of seeded records (clock 2026-02-14 00:00 UTC, normal universe)

Inputs read: `research/sweeps/seed_snapshot.md`, `plan/holder_facts.json`. Base reads only through `tools/hg.py search` (read-only). No SQL was run, and I wrote nothing except this file.

## Findings

### MAJOR 1: two "last written contact" comments are false as Leonard wrote them
Base record: Slack `CE22D7884D8F/2026-01.json` [0] and [1], `mpdm-robert--arthur.blake--leonard.hayes--martin.walsh--owen.baker--marcus.bennett--oliver.brooks-1`. Leonard wrote both messages himself, which puts them in his view.
- [0] `1769826382.170389` (2026-01-31 02:26:22 UTC, Jan 30 18:26 PT): "Hey guys. We just ran payroll for January. We were able to send full amount due to 4 of you ..."
- [1] `1769826544.570159`: "We do have a verbal high level alignment with [PERSON_NAME_2000] ..."

These messages are written contact sent directly to Marcus Bennett (EMPLOYEE_0002), Martin Walsh (EMPLOYEE_0033), Owen Baker (EMPLOYEE_0021) and Oliver Brooks (EMPLOYEE_0003). They do not mention the closing ("in trouble for February"), so no Told outcome changes. Two comments are wrong because of them:
- **ENG-2456** "Last written contact I have before Feb: Jan 26, 2026, #combofighter-vfx". This is false. Marcus's contacts after Jan 26:
  - Marcus also posted in #prototype on Jan 30 at 07:08 UTC, inside Oliver's channel thread `1769719702.315389`, where Robert had also replied. The post is `C09UHHN6PFZ/1769756901.779809`, "I like the port!".
  - Leonard's group DM followed on Jan 31 UTC.
- **ENG-2458** "Last written contact I have before Feb: Jan 30, 2026, #prototype". The #prototype post is Jan 30 16:39 UTC (`1769791141.517879`), but the group DM came later (Jan 31 02:26 UTC). Under the UTC dates the file uses elsewhere (see MINOR 1), both the date and the channel are wrong. Under Pacific dates the date holds, but the channel is still wrong.
- ENG-2457 (Owen, #prototype Jan 31 21:44 UTC) and ENG-2463 (Oliver, #prototype Jan 31 16:17 UTC) come after the group DM, so both still hold.
- **Smallest fix:**
  - ENG-2456: change the comment text to `Last written contact I have before Feb: Jan 31, 2026, group DM`.
  - ENG-2458: change it to `Last written contact I have before Feb: Jan 31, 2026, group DM`.
  - Update holder_facts locators to `CE22D7884D8F/1769826382.170389`.

### MINOR 1: date convention is UTC, not Leonard's local date
- ENG-2438 and ENG-2439 say "Jan 25, 2026, mail". The message is in `leonard@harmonygames.co_1855133803855213163.json` [0], dated `Sat, 24 Jan 2026 16:22:26 -0800`, which is Jan 25 00:22 UTC.
- ENG-2446 says "Oct 24, 2025, group DM". The message is at 05:35 UTC, which is Oct 23 22:35 PT.

Leonard reads Gmail and Slack in Pacific time, so a reader comparing the header sees Jan 24. This is harmless for outcomes. Fix, if wanted: either leave as is (and keep UTC for the MAJOR 1 fix), or switch all comments to PT dates: ENG-2438 and ENG-2439 become Jan 24, ENG-2446 becomes Oct 23, ENG-2456 and ENG-2458 become Jan 30 group DM. ENG-2454's Robert locator becomes Oct 21 PT, but Douglas's own #zombie-match-lite post on Oct 22 10:59 PT keeps "Oct 22".

### MINOR 2: ENG-2452 (Calvin Price) "Oct 16, 2025, DM" is defensible but inconsistent with the other comments
Calvin posted later in channels Leonard belongs to:
- #zombie-match-lite `C09MN425A77/1761166673.267619` (Oct 22)
- #zombie-bugs `C08R27X0EAH/1761236027.208299` (Oct 23, "I sent a fix for that")

Neither exchange involves one of the three founders. Other comments, however, count a holder's own channel post (ENG-2458, ENG-2463). No outcome turns on this. Optional fix: "Oct 23, 2025, #zombie-bugs".

### MINOR 3: ENG-2451 stands out
- Its owner-list comment, "Not on the Nov 2024 owner list", is the only one that breaks the pattern. Together with the oldest date (Jun 16, 2024), it hints that this is a lapsed line. The fact is true and natural, so keep it unless the lapse is meant to be found only through Carta.
- Arthur's "I reached out to him and he didn't respond" (`C04UEQVDVB7` 2024-11 [21]) gives no written record Leonard has, so the comment is not false.

### MINOR 4: Drive files are older than their parent folder
`Holder list (draft)` (created 2026-02-10T18:12:26Z) and the deck (created 2026-02-10T18:33:52Z) have parent `d_601064334a0b493022fe83`, but that folder was created 2026-02-12T23:20:37Z. A Drive move explains this, and the notes say "everything goes in the close-out folder". Smallest fix: set each file's modified time to at least Feb 12 23:20, or leave as is.

### MINOR 5: the deck title can be read as a date
"Harmony Games February 26 Update" can read as "the Feb 26 update", one day before the KPMG 2/27 deadline, not as "Feb '26". Optional: "Harmony Games February 2026 Update".

## Passed
1. **Spot checks against the locator plus a later-contact scan of channels and mail Leonard can see.** Each of these is true as written:
   - ENG-2438 and ENG-2439: Griffin partner. There is a later Jan 25 00:40 calendar accept, still the same date. The next mail is Feb 9.
   - ENG-2440: DM `D04UC0UEN2V`. Jan 30 is the last exchange before Feb. Feb 9 is the first message about the closing, which is after the cutoff.
   - ENG-2441: Nov 6 2025, the holder writing with Leonard on bcc.
   - ENG-2446: mpim `C7442B7CD94B`. The holder has no Slack or mail after Oct 24. The Sep 15 mail is earlier.
   - ENG-2447: Matthew Collins (`UEC7997064E`) has no Slack or Dec–Feb mail. Jan 5 WhatsApp per `C07C2866011/1767653456.884179`.
   - ENG-2450 (ES-1, EMPLOYEE_0005): Jan 27. Later DMs are not in Leonard's view.
   - ENG-2451: Robert's reply in #engineering-bots. The Jun 18 Arthur DM `D050QE35K9U` is not in Leonard's view.
   - ENG-2453: Claire, Jan 7.
   - ENG-2454: Douglas (EMPLOYEE_0031), Oct 22.
   - ENG-2455: Victor, Apr 14 2025.
   - ENG-2457: Owen, Jan 31.
   - ENG-2460: EMPLOYEE_0026, DM Jan 26.
   - ENG-2463: Oliver, Jan 31.
   - Across the 26 comments, nothing marks who has been told: every date is before Feb, and the closing messages are in Feb. Lapsed lines are not marked, apart from the ENG-2451 hint in MINOR 3.
   - The channel labels match their records, except ENG-2456 and ENG-2458 (MAJOR 1).
2. **Titles.** Checked against base forms:
   - ENG-2463 matches the Carta "Full Legal Name" of Oliver Brooks (`leonard@harmonygames.co_1782034095239486005.json`) and the Feb 12 termination mail `1856960382677662910`.
   - ENG-2458 matches the bank recipient form.
   - ENG-2446 matches the 2023 mail header form.
   - ENG-2447 [11362] matches the owner list.
   - No token belongs to another holder. ENG-2441 "Arthur PERSON_3083_NAME" is the owner-list form. Its "Arthur" could be mistaken for Arthur Blake, but this is base wording and was already logged.
3. **Seeded records.**
   - The #winddown origin lines follow the base:
     - [188] "linear we keep during transition" leads to "We keep it during the transition anyway".
     - [190] "archieve account on google after Feb 15" and "keep ... google ... until the data is extracted" lead to the notes' "I said I'd archive google after the 15th but that waits".
     - [197] lists "Carta terminations; Reaching out to our angels; onboarding with [USERNAME_26907]", and [198] says the Carta terminations are done. Together they lead to "the angels are what's open from my list, besides the Sunset onboarding".
     - [7] and [8] are the draft letter and "reach out to investors one by one".
   - "They stay in Backlog until the sheet is done" matches the 26 Backlog states and the project description.
   - The Board position thread exists on Feb 12 (`1856958794180374704`).
   - The sheet figures match the owner-list lines. "27 holders" matches the 27-line owner list.
   - The Trello description and its comment (18:14:27, after the Sunset mail at 18:06:21) are consistent.
   - The Contacts rows use the base shape (`first_name` = PERSON_n, empty `last_name`), and neither duplicates a base contact.
   - The Robert-to-holder mail is attached to base thread `1773963101399472184` (Aug 11 2023, Leonard cc). Its quoted line and weekday match. [PERSON_NAME_0054] is Robert's base name token.
   - All three voices fit: Leonard's notes, Slack and Linear; the auditors; and Sunset. None of the seeded text gives away a label or count.
4. **Timestamps.**
   - The Slack rows run from 2026-02-12 23:15:20 to 2026-02-13 02:23:57, all before Feb 13 10:03 UTC.
   - Every Linear comment comes 6 to 31 minutes after its issue, and the last one is Feb 13 00:03.
   - The project was created 23:24:12, after the Slack "Putting the holders in linear" message (23:15:20). Its description cites the notes (01:05), KPMG (16:48) and Sunset (18:06), all of which fall before its updated_at of 2026-02-13T18:21:46Z.
   - The notes (Feb 13 01:05) follow the Board thread (Feb 12 22:05) and replace the Feb 10 outreach notes. The 02:21 to 02:22 Slack supersessions follow the notes.
   - The mail quote headers convert correctly to PT (8:48 AM, 10:06 AM, Fri Feb 13).
   - "Tuesday" matches the Feb 17 calendar event.
   - Nothing refers to a record later than itself.

Not checked: the greeting token [PERSON_NAME_0112] in Robert's mail; whether Robert's mailbox thread id `robert@harmonygames.co/1773963101279916523` matches his base copy of the Aug 2023 thread (his base files are numbered, so the id was not found by name); and comments ENG-2442, 2443, 2444, 2445, 2448, 2449, 2459, 2461, 2462 beyond reading their locators in holder_facts.
