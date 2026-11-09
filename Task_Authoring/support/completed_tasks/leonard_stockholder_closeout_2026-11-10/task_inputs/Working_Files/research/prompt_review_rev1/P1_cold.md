# P1 (cold) · Unique Ground Truth and Clarity · Leonard stockholder close-out, rev2

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal). Persona Leonard Hayes (leonard.hayes@harmonygames.co). Blind pass: I read only the inputs named in the brief, the universe through `Task_Authoring/tools/hg.py search` / `records`, the ACL, the known-issues list and the rule files. I did not open any other report.

Scope checked: the 5 prompt sentences, plus every record the prompt brings in. That is the close-out notes doc `f_a37b403d5200d4f0a31d31` (22 rule lines), the Linear project `ec2ea957…` description, the 26 holder issues ENG-2438..2463 and their 52 comments, the #winddown list thread `e3e198cc…` with its 4 injected replies and the 3 injected #winddown posts, the 2 KPMG messages, the Sunset intake mail, Trello card 456 and its comment, the Feb 10 update outline deck, the Feb 12 Board position thread, the old outreach notes and the "Holder list (draft)" decoy.

## Findings list (deep_recheck format)

DR1 | P1 | §2 Kill the other reading / edge values (recipient) | Notes: "Messages go to the address on my investor update list if they're on it, otherwise the email we have." / "Notice route: the email we have." | contacts.json `7fe31e7e…` "Claire Morgan claire.morgan@harmonygames.co"; `51f5f16d…` "Martin Walsh martin.walsh@harmonygames.co"; `fc22d594…` "Brian Foster brian.foster@harmonygames.co" vs gmail `leonard…/1856858053929740799` (To PERSON_2360_EMAIL), `…/1856861229984402233` (To PERSON_4363_EMAIL, "Hi Martin"), `…/1856861400116562076` (To "brian <PERSON_4243_EMAIL>"), and gmail `…/1782034095239486005` "Claire Morgan: PERSON_2360_EMAIL", plus #winddown 1770838364.606739 "I'll create this for all contractors and will send them to their personal accounts" | Unique Ground Truth (also Clarity) | UGT 2 (fail-level) unless the rubric accepts either address for each person; Clarity 3

DR2 | P1 | §2 (recipients) | Notes: "Griffin's partner gets a heads-up as a reply to all on the Feb 12 Board position thread" | gmail thread `leonard.hayes@harmonygames.co/1856958794180374704`: PERSON_4337 22:05Z To Leonard Cc PERSON_2847; Leonard 22:14 PST To PERSON_4337 Cc PERSON_2847, robert, arthur; SQL-injected Robert 22:38Z To PERSON_4337 Cc leonard, PERSON_2847, arthur | Unique Ground Truth | Minor. Both outcomes pass if the rubric requires only PERSON_4337 and PERSON_2847 on that thread

DR3 | P1 | §2 (set membership) | Prompt: "an answer to KPMG's audit request"; KPMG item "4. Any financing or other significant event since that date." | #winddown 1770664094 (Feb 9 shutdown), 1770931777.561519 "wind down agreement and data agreement reviewed and signed", gmail `…/1856958794180374704` (board resignation), Carta terminations "as of Jan. 30, 2026", lapses "Last day to exercise Jan. 24, 2026 / Jan. 28, 2026" | Unique Ground Truth / Clarity (open set) | NON-FAIL if the rubric sets an acceptance floor; FAIL if a rubric row locks one list

DR4 | P1 | §2 (contents, figure) | Outline slide `el_3f1b82e16a82` "What happened / Why we are closing and when the team stopped"; notes "take my draft from #winddown and bring it up to date as a letter I can send" | Carta "has been terminated … as of Jan. 30, 2026" (Marcus, Martin, [0068], [0022]) vs the Feb 11 letters "effective January 31, 2026" vs #winddown 1770665404 "let the team know we are shutting down … no payment in February" (Feb 10) | Unique Ground Truth | BOTH_FAIR_FIGURE candidate (date only), provided the rubric accepts each value

DR5 | P1 | §2 (contents boundary) | Outline slides `el_b4a6a6d9a533` "Where things stand / Holders, per the Nov 2024 owner list / Board, process, who is running the close" and `el_9dabe7a0ac53` "Distributions, tax papers, your options" | notes "the holder sheet comes first, the notes and everything else run off it" | Clarity | Minor (the source is settled; how much detail goes in the letter is open)

DR6 | P1 | §2 (sheet cells) | Sunset intake gmail `…/1857034369525983506`: "Total shares and options outstanding", "Directors in office, and who holds the preferred vote", "How each holder gets formal notice" | gdocs Restated Certificate "Requisite Holders" (majority of Preferred); Robert 22:38Z "That leaves Leonard and me on the board" | Clarity | Minor; several fair outcomes

DR7 | P1 | §2 (identity) | Linear ENG-2460 "Brian Foster", comment "Nov 2024 owner list: 10,173" | Carta "Termination details for [PERSON_NAME_2769] [PERSON_NAME_0093] … ES-15 … Granted 10,173 Vested 3,391 … Last day to exercise March 31, 2026"; letter To "brian <PERSON_4243_EMAIL>" "Hi [PERSON_NAME_0092]"; Carta digest Oct 22, 2024 "signed option grant ES-15 … for Omer [PERSON_NAME_0092] [PERSON_NAME_0008]" | Unique Ground Truth | Settled by the record chain (see F7). Recorded as a token risk: the rubric must accept the token name

## Detailed forks

### F1. Which address is "the email we have" (holder drafts and the notice-route cells) · OPEN

- **Span.** Notes: "Messages go to the address on my investor update list if they're on it, otherwise the email we have." and "Notice route: the email we have."
- **Reading A.** "The email we have" means the Contacts record. The SQL added Investor contacts on Feb 12 for PERSON_0693 and PERSON_2275, which suggests Leonard keeps them there. On that reading Claire Morgan's draft goes to claire.morgan@harmonygames.co, Martin Walsh's to martin.walsh@harmonygames.co, and Brian Foster's (ES-15) to brian.foster@harmonygames.co, and the notice-route cells carry the same addresses. Records: contacts.json `7fe31e7e…`, `51f5f16d…`, `fc22d594…`. The company accounts are still live: the notes say "we keep it until the data is extracted".
- **Reading B.** "The email we have" means the personal address the company actually uses for these people. The Feb 11 closing letters went to PERSON_2360_EMAIL (Claire), PERSON_4363_EMAIL (Martin) and PERSON_4243_EMAIL ("brian"). The Carta option-issuance address list in gmail `…/1782034095239486005` reads "Claire Morgan: PERSON_2360_EMAIL", and #winddown 1770838364.606739 says "I'll create this for all contractors and will send them to their personal accounts".
- **What changes.** The To address on 3 or more holder drafts, and the notice-route cell on those rows. [PERSON_NAME_0022] and [PERSON_NAME_0051] may be affected too (I did not map their addresses). The same split can also apply to holders on the investor-update list. Example: Arthur Schaeppi is PERSON_3063 on the May 18, 2024 BCC list but PERSON_3083 in Contacts, so his notice-route cell could differ from his message address.
- **Settled?** No. No persona-visible record says where "the email we have" lives. "B is less likely" does not settle it. The same person is reached either way, so Clarity is 3, but the write (the To field) differs, so UGT stays open.
- **Smallest fix.** Have the notes name the store, for example "otherwise the email in my Contacts", and keep the Feb 11 letter addresses out of play. Or make the rubric accept either address of the same person on each draft and notice cell.

### F2. Griffin heads-up: reply-all to which message · OPEN (minor, fair-outcome)

- **Span.** "Griffin's partner gets a heads-up as a reply to all on the Feb 12 Board position thread, asking for their vote as preferred holders on the dissolution."
- **Reading A.** Reply-all to the latest message, Robert's injected 22:38Z message. That gives To: robert, PERSON_4337; Cc: PERSON_2847, arthur.
- **Reading B.** Reply-all to Griffin's partner's own message (PERSON_4337, 22:05Z). That gives To: PERSON_4337; Cc: PERSON_2847. Robert and Arthur are left off.
- **What changes.** Whether Robert and Arthur are on the sent message.
- **Settled?** No record picks the message. Both readings reach Griffin's partner on the right thread.
- **Fix.** The rubric checks only that the reply is on thread 1856958794180374704 and reaches PERSON_4337 and PERSON_2847, and accepts any extra cc. Or change the notes to "reply to all on Robert's last message in the Feb 12 Board position thread".
- **Settled sub-points.** "Griffin's partner" is PERSON_4337 ("Senior Partner & Co-Founder", gmail `…/1856958794180374704` msg 1). The heads-up is sent, not drafted. That follows from "Send the replies yourself" and "That one can go out once the sheet is done", and the notes reserve "note" for drafts ("I read and send each note myself").

### F3. KPMG item 4: which "significant events since that date" · OPEN (open set)

- **Reading A.** List the Feb 9 decision to dissolve, the Feb 12 Sunset wind-down engagement and $22,500 data licence ("wind down agreement and data agreement reviewed and signed", #winddown 1770931777.561519), and no new financing.
- **Reading B.** Add or leave out the Feb 12 board resignation (gmail `…/1856958794180374704`), the Jan 30, 2026 terminations of the whole team (Carta), the Jan 24/28 option lapses, and the failed Jan 2026 bridge talks.
- **What changes.** The contents of the sent KPMG reply.
- **Settled?** No record defines "significant". There is no closed list to grade against.
- **Fix.** Either the rubric sets a floor (the dissolution decision plus no new financing) and accepts extra items, or a record such as a Leonard Slack line names the events to report.
- **Settled sub-points.** Recipients: reply-all on `…/1857029474983245439` = PERSON_3088 + Cc PERSON_4416, PERSON_2322, PERSON_2847. KPMG says "return directly to us via email by replying to all Recipients herein", and the Linear project says "Send KPMG's confirmation as a reply to all once the sheet is done".

### F4. Letter "when the team stopped" date · both-fair candidate

- **The values.** Jan 30, 2026 (Carta, last terminations "as of Jan. 30, 2026"), Jan 31, 2026 (Feb 11 letters "effective January 31, 2026") and Feb 10/11, 2026 (the team was told; #winddown 1770665404).
- **Partly settled.** "Carta is the record, over any date in the letters" ranks Carta over the letters, so Jan 30 beats Jan 31. It does not separate the date work stopped from the date the team was told.
- **Same for both.** Writes, destination and recipients do not change; only one date in the letter does.
- **Fix.** The rubric accepts Jan 30, 2026, or the date the team was told (Feb 10/11). Or the outline says "when the team's contracts ended".

### F5. Letter holder section and outline wording · Clarity minor

- **Source is settled.** The outline's "Holders, per the Nov 2024 owner list" is overridden by "the holder sheet comes first, the notes and everything else run off it" and "Carta is the record". The notes, dated Feb 13, also replace the Feb 10 outreach notes ("These replace my earlier outreach notes").
- **Still open.** What the letter's holder section must contain: per-holder figures, class totals, or the holder count. The same goes for distributions and tax papers. The letter goes to everyone, so per-holder figures may be unwanted.
- **Fix.** The rubric checks the outline's sections and the Carta-based totals only.

### F6. Sheet cells with several fair outcomes · Clarity minor

- "Total shares and options outstanding" can be one figure or two. Today's values: shares 9,051,879 (6,000,000 common + 3,051,879 Series Seed); options 159,706 vested on live lines (advisors 103,764 + 55,942). Combined total 9,211,585.
- "Who holds the preferred vote" can be "Griffin II + Side Fund (2,746,693 of 3,051,879)" or "Series Seed holders, controlled by Griffin".
- The notice-route cell on "Nothing" rows can be the email or n/a.
- Holder sheet file: updating the existing "Holder list (draft)" (`f_5ecaa967…`, already in the close-out folder) or creating a new sheet there both end with a sheet in the close-out folder.
- **Fix.** The rubric is written to accept each of these.

### F7. Brian Foster vs Carta ES-15 · settled by a record chain (token risk)

- **Reading B.** ENG-2460 "Brian Foster" has no Carta line under that name, so it gets "Nothing"/Canceled. ES-15 ([PERSON_NAME_2769] [PERSON_NAME_0093]) would then need a new row or issue.
- **What kills B.** The chain of records:
  - The Feb 11 letter goes To "brian <PERSON_4243_EMAIL>" with "Hi [PERSON_NAME_0092]", effective Dec 31, 2025.
  - The Carta digest of Oct 22, 2024 has "ES-15 … for Omer [PERSON_NAME_0092] [PERSON_NAME_0008]".
  - The Carta termination of ES-15 is "as of Dec. 31, 2025", 10,173 granted.
  - A calendar acceptance from brian <PERSON_4243_EMAIL> reads "[PERSON_NAME_0093] has accepted … [PERSON_NAME_0092] and Leonard Hayes".
  - The Linear comment reads "Nov 2024 owner list: 10,173".
  - The Linear project says "one issue per holder on Carta".
- **Fix.** The rubric names both the token and "Brian Foster".

### Checked and settled (not findings)

- **Told.** "Told means a written message about the closing, sent to them directly …":
  - The Feb 11 letters say "The company is shutting down", so they count. Those letters go to Claire (PERSON_2360, mapped by gmail `…/1782034095239486005`), [0043] (PERSON_2361), [0068] (PERSON_3140, "Hi [PERSON_NAME_0067]"), Martin, Marcus and Brian/Ömer.
  - Griffin was told by Feb 9, gmail `…/1856675475513544349` msg 13 To PERSON_4337: "we've decided to shut the company down". The Linear comment "Last written contact … before Feb: Jan 24, 2026" is scoped "before Feb", so it does not conflict.
  - PERSON_3941 was told by Robert's SQL-injected message of Feb 12, 23:41Z: "we're closing the company".
- **Families.** "One note to whoever has always handled it for a family …":
  - The family is [PERSON_NAME_52949] (PERSON_2260) with Patrick Lewis and [PERSON_NAME_27652]. Gmail `…/1770141224265557526` lists all three at "25.000 usd", and `…/1774211155651873582` reads "me and my brothers … single account".
  - Labels: Patrick and [27652] get Covered, and [52949] gets Closing with a note giving all three holdings.
- **Carta vs other dates.** Carta wins over the letter dates. That includes NB-22, the [0067] letter dated "January 31, 2025".
- **Lapsed lines.** These hold Nothing: [0038] (Jan 28, 2026), [2768], Calvin and [0612] (Jan 24, 2026), Victor (Jul 16, 2025) and [0100] (Nov 1, 2024).
- **Who goes first.** [PERSON_NAME_0051]: last day Feb 21, 2026, not told. They are the only holder with a February last day.
- **KPMG item 1.**
  - Common: 6,000,000.
  - Series Seed: 3,051,879, of which Griffin II holds 2,662,255 and the Side Fund 84,438. The split is in #executives 1768416262; the total is set by KPMG's own "3,051,879 Series Seed" and the SQL #executives correction "3,051,879 seed preferred … 305,186".
  - "Each fund" means the audited Griffin funds ("audit of GRIFFIN GAMING PARTNERS … the fund's investment").
- **KPMG item 2 (as of Dec 31, 2025).**
  - "On or before" puts the Dec 31 terminations (Claire, [0043], Ömer) at vested only.
  - Lines ending Jan 30, 2026 count in full. That follows from KPMG's "a line terminated on or before the as-of date counts only what had vested" and "using each effective date as Carta shows it, regardless of when recorded".
  - Oct-24 lines count at vested (outstanding until Jan 2026).
  - Advisor lines count in full: 61,038 + 30,518 + 6,104 + 6,104 = 103,764 (gdocs `/docs_documents/262`).
  - Total: 243,757. Item 3: 9,295,636.
- **Directors in office.** Leonard and Robert (Robert 22:38Z: "That leaves Leonard and me on the board"). The SQL contact update says Matthew Collins "left the board May 2025".
- **Sharing.** The sheet goes to Robert and Arthur. The letter goes to Robert only ("<@Arthur> the sheet goes to you as well as Robert, the rest of my notes stands").
- **Folder.** The close-out folder `d_601064334a0b493022fe83`, not Wind Down ("everything goes in the close-out folder, not the Wind Down one").
- **Linear.** States: Canceled / Todo / Done, with a "why" comment on every issue without its own note. "Note" means a Leonard draft. Not sent to Sunset ("I'll pass it to Sunset myself").
- **Sent vs drafted.**
  - Sent: the KPMG reply, the Griffin heads-up and the #winddown thread reply.
  - Drafted: the holder notes.
  - Neither: the letter is a doc, not sent.
- **Segerstråle notice route.** It gets the copy to Tor's lawyers too. The notes say "which Segerstrale signed too"; DocuSign "[PERSON_NAME_0089] Segerstråle viewed … Side Letter TLAS(final) (1).pdf"; and TLAS wrote "The letter also includes [PERSON_NAME_0090] as a party".
- **TOR message address.** PERSON_5275 is on the May 18, 2024 investor-update BCC. TOR is "[PERSON_NAME_0128]'s personal investment fund" and the side-letter request came "from [PERSON_NAME_0129] (Tor Capital)", which the TLAS cc shows as PERSON_5275. That is resolvable but hard.
- **Investor update list.** It is unique: the only investor-update email is gmail `…/1799418746420547240` (May 18, 2024). Its BCC list: PERSON_0693, Patrick Lewis, PERSON_2275, PERSON_3063, PERSON_2260, PERSON_5275, PERSON_1287, PERSON_3336 (Segerstråle, signs "[PERSON_NAME_0089]" / "-k") and PERSON_3935.

### Evidence limits (not scored)

- **Unanswered questions.** I did not finish the census of "Anything they asked about their holding that we never answered". The searches covered Leonard's mailbox for each holder token and address in 2025–26 and found no open question from a note-getting holder. The one holding-related request found ("[PERSON_NAME_2768] [PERSON_NAME_0011] requests access to your cap table", Carta, Oct 29, 2025) belongs to a holder who now holds nothing and gets no note.
- **Unmapped addresses.** I did not map the addresses for [0022], [0051] and Matthew Collins (matthew.collins@harmonygames.co in Contacts; PERSON_3935 on the list is not him, since gmail `…/1843007315645862923` sends him a separate forward).
- **Advisor vesting.** Vested amounts for the advisor lines (Matthew, Segerstråle, PERSON_3941, PERSON_1287) are not in any visible Carta record. They follow from the advisor agreements: "vest on a pro rata basis monthly over a 2-ye[ar]" from Jul 21, 2023, so fully vested by Jul 2025. Matthew "left the board May 2025" but stays "Investor and advisor" with no Carta termination, so I treat his line as live and fully vested. This belongs to P2 (data exists).

## Census table (26 holder issues)

Today = Feb 14, 2026. "Told" = a closing message seen in Leonard's mailbox. Holdings come from Carta, the Nov 2024 list split and the advisor agreements. Address forks refer to F1.

| Issue | Holder | Holds today | Last day | Told (record) | Label | Linear | Note to | Fork |
|---|---|---|---|---|---|---|---|---|
| ENG-2438 | Griffin II | 2,662,255 Seed | — | Feb 9 to PERSON_4337 | Already told | Done + why | — (heads-up sent) | F2 |
| ENG-2439 | Griffin Side Fund | 84,438 Seed | — | Feb 9 | Already told | Done + why | — | F2 |
| ENG-2440 | Segerstråle | 50,865 Seed + 30,518 opt (vested) | — | no | Closing | Todo | PERSON_3336 (list) | notice: +TLAS copy |
| ENG-2441 | Arthur Schaeppi | 25,432 Seed | — | no | Closing | Todo | PERSON_3063 (list) | F1 (notice cell PERSON_3083?) |
| ENG-2442 | [4468] | 25,432 Seed | — | no | Closing | Todo | PERSON_0693 (list) | — |
| ENG-2443 | [52949] (family handler) | 25,432 Seed | — | no | Closing | Todo | PERSON_2260 (list) | — |
| ENG-2444 | Patrick Lewis | 25,432 Seed | — | no | Covered | Done + why | (in [52949] note) | — |
| ENG-2445 | [27652] | 25,432 Seed | — | no | Covered | Done + why | (in [52949] note) | — |
| ENG-2446 | PERSON_3941 [0127] | 25,432 Seed + 6,104 opt | — | Robert Feb 12 | Already told | Done + why | — | — |
| ENG-2447 | Husnu Matthew Collins | 25,432 Seed + 61,038 opt | — | no | Closing | Todo | matthew.collins@ (Contacts) | F1 / limit |
| ENG-2448 | TOR Capital | 50,865 Seed | — | no | Closing | Todo | PERSON_5275 (list) | notice: +TLAS copy |
| ENG-2449 | PERSON_1287 | 25,432 Seed + 6,104 opt | — | no | Closing | Todo | PERSON_1287 (list) | — |
| ENG-2450 | [0043] | 17,802 opt | Mar 31, 2026 | Feb 11 letter | Last day | Todo | PERSON_2361 | — |
| ENG-2451 | [0100] | 0 (lapsed Nov 1, 2024) | passed | — | Nothing | Canceled + why | — | — |
| ENG-2452 | Calvin Price | 0 (lapsed Jan 24, 2026) | passed | — | Nothing | Canceled + why | — | — |
| ENG-2453 | Claire Morgan | 4,450 opt | Mar 31, 2026 | Feb 11 letter (PERSON_2360) | Last day | Todo | company vs PERSON_2360 | **F1** |
| ENG-2454 | [0612] | 0 (lapsed Jan 24, 2026) | passed | — | Nothing | Canceled + why | — | — |
| ENG-2455 | Victor | 0 (lapsed Jul 16, 2025) | passed | — | Nothing | Canceled + why | — | — |
| ENG-2456 | Marcus Bennett | 12,875 opt | Apr 30, 2026 | Feb 11 letter | Last day | Todo | marcus.bennett@ | — |
| ENG-2457 | [0068] | 8,477 opt | Apr 30, 2026 | Feb 11 letter (PERSON_3140) | Last day | Todo | PERSON_3140 / ? | F1 (unmapped) |
| ENG-2458 | Martin Walsh | 2,013 opt | Apr 30, 2026 | Feb 11 letter (PERSON_4363) | Last day | Todo | company vs PERSON_4363 | **F1** |
| ENG-2459 | [0051] | 1,530 opt | Feb 21, 2026 (first) | no | Closing and last day | Todo | ? | F1 (unmapped) |
| ENG-2460 | Brian Foster = ES-15 | 3,391 opt | Mar 31, 2026 | Feb 11 letter (PERSON_4243) | Last day | Todo | company vs PERSON_4243 | **F1**, F7 |
| ENG-2461 | [2768] | 0 (lapsed Jan 24, 2026) | passed | — | Nothing | Canceled + why | — | — |
| ENG-2462 | [0038] | 0 (lapsed Jan 28, 2026) | passed | — | Nothing | Canceled + why | — | — |
| ENG-2463 | [0022] | 5,404 opt | Apr 30, 2026 | no | Closing and last day | Todo | ? | F1 (unmapped) |

Row counts by label: Nothing 6, Already told 3, Closing 7, Covered 2, Last day 6, Closing and last day 2. Total 26 rows and 15 drafts.

## Census of mail and Slack the decisions turn on

| Decision | Records read |
|---|---|
| Told | Feb 9 Leonard→PERSON_4337 (`…/1856675475513544349` m13); Feb 11 Sunset intro (PERSON_4337 bcc); 6 Feb 11 letters (`…1856858053…`, `…1856860994…`, `…1856861229…`, `…1856861323…`, `…1856861400…`, `…1856861462…`); Oct 29, 2025 letters to cameron / ryan (do not mention the closing); Robert→PERSON_3941 Feb 12 (SQL) |
| Last day / holds | 14 Carta "Termination details" emails (Aug 2024 – Feb 12, 2026); Carta activity digests Aug 2023 – Dec 2024 (ES/SSP ids); advisor agreements gdocs 160/295/490/570; disclosure gdocs 262 |
| Family | gmail `…/1770141224265557526`, `…/1774211155651873582`; #winddown SQL replies 1770949310 / 1770949322 |
| Addresses | contacts.json (170 + 2 SQL); May 18, 2024 investor update BCC; Nov 2023 Carta address list `…/1782034095239486005`; Feb 11 letter recipients |
| Griffin heads-up | thread `…/1856958794180374704` (3 base messages + 3 SQL copies) |
| KPMG | thread `…/1857029474983245439` (3 SQL messages); #executives 1768416262 (fund split), SQL #executives 1768418331 (3,051,879 / 305,186) |
| #winddown reply | parent `e3e198cc…` "next things for me are … Reaching out to our angels properly"; SQL replies 1770949310 / 1770949322 / 1770949351 / 1770949437 |
| Order / timing | Trello 456 desc "holder sheet, then the notes, then the letter" + comment "Sunset wants the same sheet"; #winddown SQL 1770938158 "They stay in Backlog until the sheet is done" |

Open forks this round: F1 (UGT fail-level unless the rubric accepts both addresses of the same person), F2 (minor; fair if the rubric keeps the Griffin recipients loose), F3 (open set; needs a rubric floor), F4 (both-fair date), F5 and F6 (Clarity minor). F7 is settled by the record chain.
