# G2: verified per-holder facts for the seeded Linear comments (ENG-2438 to ENG-2463)

Status: COMPLETE. Facts and locators only; no prompt, Oracle Event or rubric text. Clock 2026-02-14 00:00 UTC, normal universe. All values are base records; no planned seed is counted. The verbatim owner-list lines are in plan/holder_facts.json.

## 1. Method

**Sources read.** Owner list: leonard.hayes@harmonygames.co/1816809274978043917 message 0, full body. All 14 Carta "Termination details" notices, full body. Certificates: 1774928765255297348 and 1775018766791066475. Everything went through `hg.py search` (get, get-many, search, search-many, files). No raw file was opened. Reach is `persona_view.py can-see`.

**Rule for "last contact".** Each row is the newest message before 2026-02-01 00:00 UTC that meets one of these tests:
- Mail: a founder is the sender and the holder is on to, cc or bcc; or the holder is the sender and a founder is on to, cc or bcc.
- DM or group DM: any message in a DM between Leonard and the holder; in a group DM, a message from the holder or a founder with both as members.
- Channel: a founder's message that tags the holder or answers them in a thread; a holder's message that tags a founder or answers one in a thread. A holder's post to everyone in #company-internal also counts, because that is the whole company (it decides only ENG-2453).
- Not counted: calendar invites and RSVPs, Calendly notices, Carta mail, Standard Metrics mail, Drive share notices, bounce notices, reactions, join and leave lines, founders talking about a holder, and channel talk with non-founders.

**Date rule.** UTC, which matches the clock and CS-04: Nebojsa is Oct 24 only in UTC. Three rows have a different local date; see section 4.

**Scans, all `scan_complete` true.**
- Mail headers: every address and name form for all 26 holders (165 strings) against from, to, cc and bcc, over all 17,635 files in Leonard's mailbox. Dated with a date_parsed index of all 22,648 messages.
- Mail bodies and subjects: the same strings, keeping hits after each row's date and before Feb 1. "Eren" and "Akin" were left out as substrings of common words; their address forms stayed in.
- Mail sender census: from and subject on all 4,743 messages from Jun 2025 to Feb 2026.
- Slack authors: every holder id, anonymised and raw, Jun 2025 to Jan 2026, all channels, kept to channels with Leonard as a member. Victor Jan to Sep 2025, ES-2 all of 2024-2025.
- Slack tags: founder messages tagging each holder, Oct 2025 to Jan 2026, same filter.
- Slack by name: founder messages naming a holder after the row's date, for rows dated Jan 2026; no-Slack holders' name forms (Nov 2025 to Jan 2026); references to written contact off Slack such as "whatsapp", "pinged", "texted" (Oct 2025 to Jan 2026).
- Leonard's 51 DMs: each holder DM read at the tail of its last month before February; the 22 with no holder mapping read at the tail only, and no holder appears. Group DMs joining Leonard and a holder listed for 16 holders; ES-2 is covered by the author scan.
- Holders with no Slack presence: Schaeppi, Bergmann, Enes, Patrick Lewis, Eren, Deepak, Griffin. Users `matthew` and `patrick` exist but sit in 0 channels.

**Identity checks on the record.** [PERSON_NAME_52949] is PERSON_2260 (Enes) and [PERSON_NAME_27652] is PERSON_2275 (Eren): 1770141224265557526 message 1. [PERSON_NAME_4468] signs the Jun 27, 2025 mail as Solsten co-founder and COO. ES-2 is Slack EMPLOYEE_0028: Leonard tags that id on ENG-953 (C05V5FNLB9V 2024-05 idx 1135), whose Linear assignee is [EMAIL_0072], the address of "[PERSON_NAME_0100]" on his calendar replies. [PERSON_NAME_2927] is Enes: "CEO of Libra" (C04UM32UWKD 2023-03 idx 199), and his mail comes from librasoftworks.com.

**Twice-checked.** Pass 1 was the scans above. Pass 2 re-read every locator from the record: date recomputed to UTC, founder and holder confirmed on the message, each owner-list line matched in the mail body, each figure matched in the Slack copy (C04UEQVDVB7 2024-11 idx 55), no title with Disli, Dişli or Haktan. Result on the written JSON: 26 rows, 0 mismatches. Holder membership confirmed for all 15 Slack locators where a holder is the party. can-see: 26 YES.

**Positive controls.**
- The author scan found Tor Nov 4 (D09R59580EM idx 2) and Nebojsa Oct 24 (C7442B7CD94B idx 141) by id alone, with no pointer to either, reproducing both CS-04 corrections.
- The header scan returned the six Feb 11 letters and Phil's Feb 9 mail, so it reaches past the cut-off.
- Zero-hit control: [PERSON_NAME_27652] has 0 header hits, and the body scan finds it in 1816809274978043917 message 0.

**A slip caught.** `--key user` also matches `/N/replies/N/user`, `/N/files/N/user` and `/N/edited/user`. The first pass credited Leonard's Jan 31 messages to Owen and Martin, and three Robert and Brian posts to Vincent. Fixed by keeping `/N/user` only, then re-run. A thread reply sits in the month file of the reply: Martin's reply to #prototype 2026-01 idx 6167 is 2026-02 idx 41, dated Feb 2, so it is out of scope.

## 2. Table

| Issue | Carta id | title_form | Owner list | Last contact (UTC) | Channel | Locator | Reach |
|---|---|---|---|---|---|---|---|
| ENG-2438 | SSP-01 | GRIFFIN GAMING PARTNERS II, L.P. | 2,746,693 | 2026-01-25 | mail | leonard.hayes@harmonygames.co/1855133803855213163 | YES |
| ENG-2439 | SSP-02 | GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. | 2,746,693 | 2026-01-25 | mail | leonard.hayes@harmonygames.co/1855133803855213163 | YES |
| ENG-2440 | SSP-03 | [PERSON_NAME_0089] [PERSON_NAME_25152] | 81,383 | 2026-01-30 | DM | D04UC0UEN2V/1769801610.399419 | YES |
| ENG-2441 | SSP-04 | Arthur PERSON_3083_NAME | 25,432 | 2025-11-06 | mail, Leonard on bcc | leonard.hayes@harmonygames.co/1847629332615617366 | YES |
| ENG-2442 | SSP-05 | [PERSON_NAME_4468] | 25,432 | 2025-06-27 | mail | leonard.hayes@harmonygames.co/1836075678772806708 | YES |
| ENG-2443 | SSP-06/08 | [PERSON_NAME_52949] | 25,432 | 2025-12-16 | mail, Leonard on cc | leonard.hayes@harmonygames.co/1850625296912603629 | YES |
| ENG-2444 | SSP-06/08 | Patrick Lewis | 25,432 | 2024-05-18 | mail, bcc | leonard.hayes@harmonygames.co/1799418746420547240 | YES |
| ENG-2445 | SSP-07 | [PERSON_NAME_27652] | 25,432 | 2024-05-18 | mail, bcc | leonard.hayes@harmonygames.co/1799418746420547240 | YES |
| ENG-2446 | SSP-09 | PERSON_3941_NAME [PERSON_NAME_0127] | 31,536 | 2025-10-24 | group DM | C7442B7CD94B/1761284126.873379 | YES |
| ENG-2447 | SSP-10 | [PERSON_NAME_11362] | 86,470 | 2026-01-05 | WhatsApp, per Leonard's note in #executives | C07C2866011/1767653456.884179 | YES |
| ENG-2448 | SSP-11 | TOR Capital Limited | 50,865 | 2025-11-04 | DM | D09R59580EM/1762291459.981899 | YES |
| ENG-2449 | SSP-12 | PERSON_1287_NAME | 31,536 | 2024-05-18 | mail, bcc | leonard.hayes@harmonygames.co/1799418746420547240 | YES |
| ENG-2450 | ES-1 | [PERSON_NAME_0043] | 30,519 | 2026-01-27 | group channel, #prototype | C09UHHN6PFZ/1769538701.270539 | YES |
| ENG-2451 | ES-2 | [PERSON_NAME_0100] | null (not on the list) | 2024-06-16 | group channel, #engineering-bots | C050WGU41HR/1718567051.806159 | YES |
| ENG-2452 | ES-3 | Calvin Price | 8,138 | 2025-10-16 | DM | D050GG6KZT9/1760635871.092849 | YES |
| ENG-2453 | ES-4 | Claire Morgan | 7,630 | 2026-01-07 | group channel, #company-internal | C05KNDCHAAG/1767803163.285499 | YES |
| ENG-2454 | ES-5 | [PERSON_NAME_0612] | 10,173 | 2025-10-22 | group channel, #zombie-bugs | C08R27X0EAH/1761099441.660419 | YES |
| ENG-2455 | ES-6 | Victor [PERSON_NAME_2770] [PERSON_NAME_0086] | 30,519 | 2025-04-14 | group channel, #zombie-match3d | C0880U9751A/1744648055.209429 | YES |
| ENG-2456 | ES-7 | Marcus Bennett | 22,889 | 2026-01-26 | group channel, #combofighter-vfx | C0AA36TV9QA/1769460413.888309 | YES |
| ENG-2457 | ES-12 | [PERSON_NAME_0068] | 16,277 | 2026-01-31 | group channel, #prototype | C09UHHN6PFZ/1769895868.279769 | YES |
| ENG-2458 | ES-13 | Martin [PERSON_NAME_7250] Walsh | 3,866 | 2026-01-30 | group channel, #prototype | C09UHHN6PFZ/1769791141.517879 | YES |
| ENG-2459 | ES-14 | [PERSON_NAME_0051] | 3,866 | 2025-11-23 | group channel, #dd-road-to-sub-250mb | C09Q4S613CN/1763890610.357549 | YES |
| ENG-2460 | ES-15 | [PERSON_NAME_2769] [PERSON_NAME_0093] | 10,173 | 2026-01-26 | DM | D076PSEBC4D/1769453985.097849 | YES |
| ENG-2461 | ES-16 | [PERSON_NAME_2768] [PERSON_NAME_0011] | 35,605 | 2025-10-30 | mail | leonard.hayes@harmonygames.co/1847333990408253969 | YES |
| ENG-2462 | ES-17 | [PERSON_NAME_0038] | 127,162 | 2025-10-29 | mail | leonard.hayes@harmonygames.co/1847335165884050330 | YES |
| ENG-2463 | ES-18 | [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763] | 15,259 | 2026-01-31 | group channel, #prototype | C09UHHN6PFZ/1769876261.393479 | YES |

Mail locators are thread ids. The message inside each thread: 1855133803855213163 [0]; 1847629332615617366 [0]; 1836075678772806708 [0]; 1850625296912603629 [1]; 1799418746420547240 [2]; 1847333990408253969 [0]; 1847335165884050330 [0].

## 3. Values changed from the leads, and why

### Last contact
| Issue | Lead | Now | Why |
|---|---|---|---|
| ENG-2438, 2439 Griffin | s2: Feb 12 (after the cut-off); s2 and census cite the recap as Jan 23 | 2026-01-25 | Jan 23 opens the thread. Phil replies Jan 25 00:06 UTC and Leonard answers 00:22 UTC |
| ENG-2440 Segerstrale | s2: DM Feb 12; mail Jan 8 | 2026-01-30 | Last DM before February, idx 64 |
| ENG-2447 Collins | s2: Oct 28, 2025 | 2026-01-05 | Leonard: "chatting with Matthew on whatsapp", #executives 2026-01 idx 224. Oct 28 would be false against that. See section 4 |
| ENG-2448 TOR | s2: May 19, 2024; CS-04: Nov 4, 2025 | 2025-11-04, same date as CS-04 | Locator moved to Tor's reply (21:24 UTC), the last message; design §1a cites Leonard's at 19:51 |
| ENG-2446 Nebojsa | s2: Sep 15, 2025; CS-04: Oct 24, 2025 | 2025-10-24, same as CS-04 | His reply to Robert, idx 141 |
| ENG-2450 ES-1 | s2: Feb 12 | 2026-01-27 | Robert tags her in #prototype; her last DM exchange with Leonard is Jan 15 |
| ENG-2451 ES-2 | s2: Oct-Nov 2024, Arthur, no locator | 2024-06-16 | Last message on file, a thread between him and Robert. See section 4 |
| ENG-2453 ES-4 | s2: Feb 12 | 2026-01-07 | Her post to everyone in #company-internal |
| ENG-2454 ES-5 | s2: DM Sep 8; #admin thread Oct 29 | 2025-10-22 | Robert tags him in #zombie-bugs. The #admin thread is founders only, so it is not contact |
| ENG-2455 ES-6 | s2: DM Feb 13, 2025 | 2025-04-14 | Exchange with Arthur in #zombie-match3d, two days before Carta's date |
| ENG-2456 ES-7 | s2: Feb 11 | 2026-01-26 | Thread with Robert, #combofighter-vfx |
| ENG-2457 ES-12 | s2: Feb 12 | 2026-01-31 | Leonard tags him, #prototype idx 6507 |
| ENG-2458 ES-13 | s2: Feb 12 | 2026-01-30 | He tags Robert, #prototype idx 5937 |
| ENG-2459 ES-14 | s2: Nov 20, 2025 | 2025-11-23 | He answers Robert's question in a thread, after his last working day; s2 notes the post but not that it answers a founder |
| ENG-2460 ES-15 | s2: Feb 12 | 2026-01-26 | Last DM before February, idx 44 |
| ENG-2462 ES-17 | s2: Feb 4 (redacted) | 2025-10-29 | Feb 2 and Feb 4 are after the cut-off. 1849220777700700390 (Nov 19, cc him) is a stranger's job mail, not contact |
| ENG-2463 ES-18 | s2: Feb 11 | 2026-01-31 | Leonard tags him, he answers, #prototype idx 6162, 6164 |

Confirmed unchanged: ENG-2441 (Nov 6), 2442 (Jun 27), 2443 (Dec 16), 2444, 2445 and 2449 (May 18, 2024), 2452 (Oct 16), 2461 (Oct 30).

### Title forms against the table in 01_Scenario_Design.md §2
| Issue | Design | title_form | Source |
|---|---|---|---|
| ENG-2438 | Griffin Gaming Partners II, L.P. | GRIFFIN GAMING PARTNERS II, L.P. | Carta 1774928765255297348; the list has one merged line, so it cannot name a fund |
| ENG-2439 | Griffin Gaming Partners II Side Fund, L.P. | GRIFFIN GAMING PARTNERS II SIDE FUND, L.P. | same |
| ENG-2440 | Segerstråle | [PERSON_NAME_0089] [PERSON_NAME_25152] | list |
| ENG-2441 | Schaeppi | Arthur PERSON_3083_NAME | list |
| ENG-2442 | Bergmann | [PERSON_NAME_4468] | list |
| ENG-2446 | Nebojsa | PERSON_3941_NAME [PERSON_NAME_0127] | list |
| ENG-2447 | Matthew Collins | [PERSON_NAME_11362] | list |
| ENG-2449 | Deepak | PERSON_1287_NAME | list |
| ENG-2450 | Julia Lawson | [PERSON_NAME_0043] | Carta |
| ENG-2454 | Douglas | [PERSON_NAME_0612] | Carta |
| ENG-2455 | Victor Barnes | Victor [PERSON_NAME_2770] [PERSON_NAME_0086] | Carta |
| ENG-2457 | Owen Baker | [PERSON_NAME_0068] | Carta |
| ENG-2458 | Martin Walsh | Martin [PERSON_NAME_7250] Walsh | Carta; the list has Martin Georgiev Walsh |
| ENG-2459 | Vincent Parker | [PERSON_NAME_0051] | Carta |
| ENG-2460 | Brian Foster | [PERSON_NAME_2769] [PERSON_NAME_0093] | Carta |
| ENG-2462 | Frederick Stone | [PERSON_NAME_0038] | Carta |
| ENG-2463 | Oliver Brooks | [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763] | Carta; the list has [PERSON_NAME_0022] [PERSON_NAME_32704] |

Unchanged: ENG-2443, 2444, 2445, 2448, 2451, 2452, 2453, 2456, 2461. Family forms must come from the mail copy of the list: the Slack copy reads "Patrick Haktan Dişli" and Carta reads "Eren Dişli".

## 4. Could not settle, and where the wording matters

1. **ENG-2447 Collins: the Jan 5 message itself is not on file.** The record is Leonard's own note, so the value rests on his statement. "Matthew" as Collins is INFERENCE: no other Matthew is in contacts, and D04UC0UEN2V 2026-01 idx 18 and #executives idx 357 fit him. #executives 2025-12 idx 679 also says "pinged Matthew" (Dec 18). If you want only messages on file, the fallback is 2025-10-28, mail, leonard.hayes@harmonygames.co/1847258343060233599, and it would then be contradicted by idx 224.
2. **ENG-2443 Enes: written and spoken dates differ.** The last written message is Dec 16, 2025, but #executives records talks on Jan 8 (idx 356) and Jan 15 (idx 756). The comment must say written, or it reads false. Jan 6 idx 259 "I set up time to talk" implies a message that is not on file.
3. **ENG-2438, 2439 Griffin: same point.** A call followed on Jan 26 (#executives idx 1401). Griffin's Standard Metrics request of Jan 27 (1855429523880965666) is automated and not counted.
4. **ENG-2451 ES-2.** Arthur says "I reached out to him and he didn't respond" (C04UEQVDVB7 2024-11 idx 21) after Leonard's Oct 22, 2024 ask. No such message exists in any readable record. Evaluator check: Arthur's DM with him ends Jun 2024, and Arthur's mailbox has no non-calendar mail to either of his addresses. June 16, 2024 is true only as "last message on file".
5. **Judgement calls on what counts as "between".** ENG-2453 Claire: Jan 7 is a post to everyone that no founder answered; the last direct exchanges are Dec 23, 2025 with Robert (#prototype 2025-12 idx 1951, 1969) and Dec 15 with Leonard (D04V187QSTY idx 7). ENG-2456 Marcus: he posted in #prototype on Jan 28 and Jan 30, but to Martin and in Oliver's thread, so Jan 26 stands. ENG-2452 Calvin: he posted on Oct 22-23, but to Julia, Oliver and Vincent, so Oct 16 stands.
6. **Later founder traffic outside Leonard's reach (evaluator-only, not used).** Calvin: DMs with Arthur and Robert to Oct 21. Douglas: DM with Arthur to Oct 23. Brian: DMs with Robert and Arthur to Jan 29. Each row is true for Leonard's records, not for all three founders' records. A comment worded as Leonard's own view is safe; "company's last contact" is not. Robert's numbered threads and Arthur's blake@ threads show no later non-calendar mail with any angel or Griffin.
7. **ENG-2444 Patrick Lewis.** The bcc reads "Patrick Lewis <patrick@harmonygames.co>", and that address also carries Bergmann's mail, so delivery to the brother cannot be proved. The header names him, so the row stands. Every `patrick` mail after it is signed by Bergmann.
8. **ENG-2438, 2439 figure.** 2,746,693 is the merged line. On a single fund's issue it must be labelled as the combined line, or it reads false: the Side Fund holds 84,438.
9. **ENG-2441 token.** PERSON_3083_NAME also renders Arthur Blake's first name (1816809274978043917 message 1). The title reads like a second Arthur; the list has a separate Arthur Blake line.
10. **Local dates differ on three rows.** ENG-2438 and 2439: Leonard's header reads Sat, 24 Jan 2026 16:22 -0800, Phil's reads Sun, 25 Jan 2026 00:06 +0000. ENG-2446: Oct 23 in PT. ENG-2454: Oct 21 in PT.
11. **Dates after a Carta end date.** ES-1, ES-4, ES-12, ES-14, ES-15 and ES-18 have last-contact dates after their Carta "as of" dates. That is true to the base (they kept working), and a reviewer may ask. ENG-2455 Victor booked a Calendly slot on Apr 22, 2025 for Apr 25 (1830089811325376557): no text, not counted.
12. **SSP-06/08** stays unresolved between ENG-2443 and ENG-2444.

## 5. Not read
Attachments, PDFs and Slack images. WhatsApp, text and phone leave no record beyond the notes cited. Thread 1856226460086133468 is redacted but after the cut-off. Linear has 0 comments in the base. Trello comments end Jun 23, 2025; I did not map every commenter, and none is a message in the sense used here. GitHub, Google Doc comments and GCal were not scanned for messages.
