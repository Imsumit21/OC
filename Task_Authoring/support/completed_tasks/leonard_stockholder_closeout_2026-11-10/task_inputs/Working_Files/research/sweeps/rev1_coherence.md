# Rev1 cold coherence review of the seeded records

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Slack export ends Feb 13 10:03 UTC.

Result: 2 BLOCKER, 3 MAJOR, 9 MINOR. As seeded, this fails §3.2. Each BLOCKER or MAJOR is a demonstrated inconsistency in data the task touches. The MINORs can't be left either, because two low-impact items also fail.

Ranks:
- BLOCKER: a base record contradicts the seeded sentence outright, and a strict reviewer would fail on it alone.
- MAJOR: demonstrated, but narrower or easier to argue.
- MINOR: format, voice or a soft tension.

File paths below are service-relative. "#winddown" is `messages/C0ADGSZKR3R/2026-02.json`. SQL line numbers refer to `01_Universe_Inject.sql`.

## BLOCKER

### B1. "The team is already gone" (Robert's mail, both copies, SQL lines 86 and 89)

Seeded: "We ran out of runway and the team is already gone."

Sent 2026-02-12 23:41:12Z. The team is still working that day, and Robert is working with them:

| Time (Feb 12, UTC) | Record | Text |
|---|---|---|
| 05:01 | slack `messages/D07H86MV4DN/2026-02.json` /342 (Robert to Oliver Brooks) | "We are gonna sync on Friday and talk about it right?" |
| 14:27 | slack `messages/C51ECE5102ED/2026-02.json` /6 (Leonard) | "Cuma günü all hands var buyurun takımla vedalaşmak isterseniz." That is an all hands on Friday, come say goodbye to the team. Friday is Feb 13, the day after Robert's mail. |
| 19:06 | slack `messages/C09UHHN6PFZ/2026-02.json` /725 (Robert, #prototype) | "new build out for variant B" |
| 22:21 | slack `messages/D05S1S2AB5M/2026-02.json` /22 (Owen Baker) | "pushed to develop main update and new pop up for no ads" |
| 22:30 | slack `messages/D07J501DBNE/2026-02.json` /31 (Owen Baker) | "I'll make these changes on the pr", 71 minutes before the mail |

The paper record gives only partial cover. The Feb 11 letters (`threads/leonard@harmonygames.co_1856860994291529096.json` /messages/0) and Carta's Feb 12 notices (`..._1856960351896429942.json` /messages/0, "as of Jan. 30, 2026") back-date the terminations. Neither says the people have stopped. This is §3.2's own example: "a person active in one service and departed in another". All of this evidence is in #prototype and DMs, the area NB-1 calls safe.

Fix, in both bodies: "We ran out of runway and we've had to let the team go." The Feb 11 letters support this, and Robert is cc'd on them. The snippets stop before this sentence, so they don't change.

### B2. "I can't add to that one" (close-out notes, SQL line 19)

Seeded: "everything goes in the close-out folder, not the Wind Down one. I can't add to that one"

Leonard almost certainly made that folder, and wrote in it two days before these notes. The export names no creator, so the evidence is the timing and Leonard's own posts:
- gdrive `data.json` /drive_files/20868: folder created 2026-02-09T21:50:11Z. #winddown /22: Leonard posts "wind down folder:" with the link at 21:50:21Z, ten seconds later.
- gdrive /drive_files/26277: `Employee Termination Letters.docx` created in that folder 2026-02-11T19:29:13Z. #winddown /65, 19:23:23Z: "gonna write official termination letters now". #winddown /68, 19:32:17Z: Leonard posts the same doc (`1X21lYOsQLGBW-ghqxZbjw37zS4s5t9qQL04lLPRVkTk`, matching that row's `web_view_link`). #winddown /69: "I'll create this for all contractors".
- No record says Leonard lost access. The folder's empty `shared_with_emails` goes with its shared-drive owner (`Resource: 7240535625619857401`). Its three children are shared with Leonard, Arthur and Robert.

Fix: drop the sentence, or use a reason the base supports: "everything goes in the close-out folder, not the Wind Down one, that one is the vendor and termination papers". The first clause already carries the instruction.

## MAJOR

### M1. "The angels are what's open" (close-out notes, SQL line 19)

Seeded: "where I left things today in #winddown: the angels are what's open from my list"

#winddown /197 lists three items: Carta terminations, angels, and "onboarding with [USERNAME_26907] and giving them the data". /198 closes only Carta. /200 splits the onboarding as still to do ("I'll take care of the other onboarding stuff"). PERSON_0767's mail of Feb 12 22:22Z (`..._1856675475513544349.json` /messages/1) says the intake is just starting, and the seeded Sunset mail of Feb 13 18:06Z still treats it as open. So two items were open at 01:05Z, and the seed contradicts itself as well as the base.

Fix: "the angels are what's open from my list, besides the Sunset onboarding".

### M2. "Numbers on there" comes before "there" exists (#winddown seed, SQL line 56)

Seeded, at 2026-02-12T23:15:58Z: "Numbers on there are just what I pasted in, the sheet is the real thing"

The project is created at 23:24:00Z and the first issue at 23:25:00Z (SQL lines 98 and 100). The line is in the past tense about content that is nine minutes in the future. The line one above it, "Putting the holders in linear", is fine.

Fix: "Numbers on there will just be what I paste in, the sheet is the real thing". This keeps the ts and id. The Linear comments still to come must be dated after their issues.

### M3. "Founders aside" against an issue for a roster co-founder (project description, SQL line 98)

Seeded: "one issue per holder on Carta, live or lapsed, founders aside"

`Evals/references/persona/roster.json` and `Task_Authoring/references/persona_roster_v2.json` give Frederick Stone the role "Co-founder", and ENG-2462 is Frederick Stone. Contacts /contacts/138 says Commercial Lead, so the base is split. This sentence defines the cohort, so it should not depend on which source the reader opens.

Fix: "the three of us aside". That matches the seeded Slack line and #winddown /94.

## MINOR

### m1. Google archive date (close-out notes, SQL line 19)

Seeded: "We keep google until the data is extracted, so my drafts are safe until I've gone through them."

The clause is accurate (#winddown /190, bullet 4). Bullet 3 of the same message says Leonard will "archieve account on google after Feb 15", which is before the Tuesday Feb 17 due date. A reader who opens /190 sees the tension, and the seed resolves it only by leaving it out.

Fix: "I said I'd archive google after the 15th but that waits, we keep it until the data is extracted, so my drafts are safe until I've gone through them."

### m2. Sunset signature (SQL line 83)

Seeded: "Best,\r\nPERSON_2888_NAME"

Every hand-written PERSON_2888 mail in Leonard's mailbox carries the full block: `..._1856675475513544349.json` /messages/8 and /10 and `..._1856872398290956689.json` /messages/2. The seed's Message-ID also claims Superhuman.

Fix: add "Head of Partnerships", "M: [PHONE_15402]", "W: www.sunsethq.com ( http://www.sunsethq.com/ )" and "Sent via Superhuman ( https://sprh.mn/?vip=PERSON_2888_EMAIL )".

### m3. Sunset uses Leonard's private phrase (SQL line 83)

Seeded: "A count of holders by what is owed to them"

This repeats "gets what they are owed" from a doc shared with nobody. To a legal team, "owed" means money, and Sunset has never seen those labels.

Fix: "A count of holders by what each still needs to hear from you".

### m4. KPMG voice and signature (SQL line 76)

Seeded: "Hi Leonard,\r\n\r\nHope you are doing well." and "Thank you,"

Base first requests open "Hello," and close "Thank you in advance," (`..._1817557789846606177.json` /messages/6, `..._1788910618703813283.json` /messages/1). The base signature also has the PERSON_3088_EMAIL line and "kpmg.com/us", and the disclaimer runs longer between rows of asterisks. Item 2's last sentence reads like a rule, not an audit request.

Fix: use the base opener, closing, signature and disclaimer. Keep "as Carta shows it" (see NB-22).

### m5. Robert's headers and greeting (SQL lines 84 to 89)

- To is `PERSON_3941_NAME [PERSON_NAME_0127] <PERSON_3941_EMAIL>`. The header Robert replied to says `PERSON_3941_NAME <PERSON_3941_EMAIL>` (`threads/leonard@harmonygames.co_1773963101399472184.json` /messages/0 `to`). The two-token form appears only in body text.
- `References` holds only the parent. Base replies carry the chain: `<1002618385.1717453.1691782739607@jlppacebcwls01.onefiserv.net> <CAE426NoTs38nTRaaAq=2u4nYuWZwpwtjTiJ6KAL+WBERzGLm6Q@mail.gmail.com>`, then the parent.
- There is no quoted tail. The same applies to Leonard's KPMG reply; base replies quote the parent.
- "Hey PERSON_3941_NAME," has zero base hits as a greeting, on a complete Gmail scan of "Hi" and "Hey" with that token. Base greets this person as [PERSON_NAME_0112]: `..._1773231301906977143.json` /messages/0 "Hi [PERSON_NAME_0112],", and the quoted "Hey [PERSON_NAME_0112]," in `..._1767975483498350973.json`.

Fix: correct the To, extend References, add the quoted tail, and use [PERSON_NAME_0112] in the bodies and snippets.

### m6. Contacts token form (SQL line 95)

Seeded: first_name `PERSON_0693_NAME`.

Base token contacts use the bare form: `PERSON_3941` (/contacts/84), `PERSON_1287` (/contacts/25).

Fix: `PERSON_0693`.

### m7. Deck title (SQL lines 16, 29, 33)

Seeded: "Harmony Games Feb 26 Update"

In base titles, a short month plus a number is a day: "Harmony Games Mar 27 Update", created 2024-03-27 (gdrive /drive_files/25263). A full month plus a number is month and year: "March 25 Investor Update" (/31145), "August 25 Update" (/39324). "Feb 26" therefore reads as Feb 26, twelve days after the clock, on a deck created Feb 10. The deck's own "Jan 22 term sheet" uses the day form (gdocs /docs_documents/40, created 2026-01-22).

Fix: "Harmony Games February 26 Update" in all three rows.

### m8. Trello board activity date (SQL lines 67 to 71)

The board's `dateLastActivity` stays 2025-11-12T17:25:43Z (trello `data.json`, boards), which is the base's latest card update. The seeded card is active on 2026-02-13.

Fix: one UPDATE on `trello.trello_boards` to 2026-02-13T18:14:00Z.

### m9. Machine-looking timestamps

Whole-minute times appear on all Drive and Docs rows, the gcal event, the project, the contact and the Trello comment. All 26 issues sit on an exact 20-second step from 23:25:00Z. Base bursts are irregular, for example ENG-2430 to ENG-2435 at 16:27:41, :51, 16:28:11, :15, :21, :25.

Fix: add seconds and jitter. Keep every value in the same order.

## Known-issue cards touched

| Card | What it means here |
|---|---|
| NB-1 | Seeded Slack authors are only Leonard and Arthur, in #winddown and their DM. No seed argues Slack access. "the three of us can all see it" is about Linear. |
| NB-6 | Last seeded Slack is Feb 13 02:23:57Z. Five records sit after the export end (KPMG, Leonard's reply, Sunset, the Trello comment, the project update, 16:48Z to 18:20Z), all in other services. None implies a Slack message. |
| NB-15 | KPMG's "service" is neutral. Keep B1's fix free of "employee" or "contractor". |
| NB-22 | KPMG's Dec 31, 2025 date makes the Owen Baker letter's "January 31, 2025" matter. "as Carta shows it" sends the reader to the Carta notice instead. Keep that phrase. |
| NB-24 | Base Linear has no comments, so everything M2 leans on is injected. |
| NB-29 | The slide "Why we are closing and when the team stopped" carries no date. Keep it that way in the letter. |
| NB-31 | "my DM with Arthur" is D04UGG61DUM, which lists five members. No seed draws a conclusion from that. |
| NB-32 | ENG-2454 Douglas. KPMG's "on or before that date" holds on both sides of the card. Never grade the end date. |

Pattern check from the memory file: no closed-record activity and no status that contradicts a record's own content. Robert's reply sits in the right thread in both mailboxes. The only threading gap is m5.

## Limits

- PDFs were not opened, and Linear comments were not reviewed because they don't exist yet.
- Voice sampling for Robert used the 677 Robert-authored messages in Leonard's mailbox.
- While checking NB-22 and NB-32 I grepped the earlier sweep files, and I grepped them again for Frederick Stone, so M3 was not reached blind. A sweep had raised that point as CS-21. Every finding here rests on the base and roster records cited.
