# S2: option and notice state, per holder (Leonard's view)

Status: COMPLETE. Facts and locators only; no prompt, Oracle Event or rubric text. Clock 2026-02-14 00:00 UTC, normal universe.
Gmail locators are `leonard@harmonygames.co_<id>` threads, shortened to the id; [n] is the message index. Slack is channel + month + idx (idx = position in that month file; ts given where it matters). FACT unless marked INFERENCE or CALC. Evaluator-only means Leonard cannot read it.

HEADLINE: the census is right on numbers and wrong on people and on who was told.
- 0 of the 8 live option-only holders has a last day in writing on any Leonard-readable record. Six have a letter that points to a Carta mail. Two have no letter at all.
- ES-14 is Vincent Parker, not a token. He resigned Nov 21 2025, asked if there was paperwork, was told no, was never told of the shutdown, and his window closes Feb 21.
- ES-18 Oliver Brooks has no letter, though Leonard told the founders "All termination letters are sent".
- Claire Morgan (ES-4) asked in writing what to do about equity. Leonard answered the other question in the same message. The equity question is open.
- The roster's "co-founder" Frederick Stone holds nothing at the clock. So do roster staff Douglas, Calvin Price and Victor Barnes. Samuel Turner never held anything.
- "Josh Dempsey" for ES-16 is an Atlas and warehouse join that Leonard's own mail contradicts. Do not use it.

## 0. Scope, reach, what was and was not read

Read in full: all six Feb 11 letters; both Oct 2025 notices and the reply thread; all 14 Carta notices; C51ECE5102ED (7 msgs); #leapblock 2026-02 (18); #company-internal from Feb 9 (idx 34-49); #prototype from Feb 11 (idx 516-726, 211 msgs); #winddown (206); #admin_foundersonly Nov 2025-Feb 2026 and the Oct 2025 thread at ts 1761701823.672399, Aug, Oct, Nov 2024 ES-2 passages; D04UC0UEN2V, D05Q3QAH2QZ, D076PSEBC4D, D05SDEQEK61, D05PX3R13QF (Nov 2025) in the relevant span; the Sunset thread 1856675475513544349 and Gemini notes f_0c37bb7235683d73569903; 1782034095239486005 (option issuance, 36 msgs), 1789011705438137160; owner list both copies; f_414596b0a9d698267dd1e1; f_5cd0524f448ee58833464a; f_6a37227593d0977fdbdd7a; PAYROLL_ROSTER (371 rows) and the employee rows of FINANCE_LEDGER.

Scan scopes. All 88,726 thread files for letter and Carta phrases, scan_complete. Leonard's mailbox for every holder address in from/to/cc/bcc (42 tokens), scan_complete; 956 messages in threads active since Jan 20 listed. Slack 2026-02 for equity, option, carta, exercis, vest, stock, shares, angel, investor, letter, terminat, shut, closing; slack 2025-2026 for exercis, carta, vested. Positive controls: "equity" hits Claire's message; "carta" hits #winddown idx 197.

Reach (persona_view, this session). YES: C51ECE5102ED, D05PX3R13QF, D05S58U4SAK, D05Q3QAH2QZ, D076PSEBC4D, D05SDEQEK61, C05KNDCHAAG, C09UHHN6PFZ, C05URGU759U, C04UEQVDVB7, C0ADGSZKR3R, D04UC0UEN2V, D050GG6KZT9, D05Q1UD6Y77, D057F5F95JQ, D07GU8WCEM6, D05UDNCCYKC, D07FYRRD0JJ; f_414596b0a9d698267dd1e1, f_623913a57e4fef9ac0dc4b, f_a17bda426285acec3020e2, f_367435eacc9712f20f38c7, f_5cd0524f448ee58833464a, f_af481d73feee6fd3bc4d8e, f_0c37bb7235683d73569903, f_4480979d3d09c0c50a5ac8, f_bdb1b56a5ed7480ea88eda, f_ce0c4b43b26e5a3505249f. NO: D05QQ7YQTND (Vincent's farewell), D05UDNCCFEW (Robert-Marcus). Evaluator-only is marked wherever used.

Method slips to note. (1) Outside the "search only through the tools" rule: `users.json`, `channels.json` and, once, every channel's 2026-02.json (to count activity) were opened with plain Python, read-only. Every message quoted here was re-read through `hg.py get-many`. (2) Turkish messages are my translation: treat the quoted Turkish as the fact and the gloss as INFERENCE.

NOT read: all attachments, PDFs, images (the "Harmony Games Stock Plan" is never in text anywhere I searched, so the 90-day term is known only from Leonard's letters and Carta's dates). Redacted: 1856226460086133468 (five messages, `<REDACTED_FLAGGED_CONTENT>`), #winddown idx 68. Calls and meetings leave no record: the Feb 11 prototype meeting where Leonard said he would "address all questions" (D05Q3QAH2QZ idx 2), the Feb 13 all hands (C51ECE5102ED idx 6). Slack ends Feb 13 10:03 UTC (NB-6). Phone and WhatsApp absence proves nothing: #winddown idx 12 is an image "From [6550]", and #executives Oct 2025 idx 2225 shows WhatsApp in use.

## 1. Source reads
### 1.1 Feb 11 termination letters (read in full)

All six: Leonard to the holder, cc Robert and Arthur, sent Feb 11 2026 12:10-12:18 PT (20:10-20:18 UTC). Copies: Robert 00016873-00016878, Arthur blake@ 1856860997442534285, 1856861205341126331, 1856861313211714543, 1856861391192946544, 1856861457103259746, 1856861508021962058. Full-phrase search "terminating our independent" over all 88,726 thread files, scan_complete: 18 hits = 6 letters x 3 mailboxes. There is no seventh letter.

Recipient-to-holder key (FACT, Leonard's own lists, 1782034095239486005[34] and [3], 1789011705438137160[15]; Leonard-readable):

| Thread | To | Salutation | Holder | ES | Effective date in letter |
|---|---|---|---|---|---|
| 1856858053929740799 | PERSON_2360_EMAIL | [0040] | Claire Morgan | ES-4 | Dec 31 2025 (subject "Notice of Involuntary Termination", the only one with that subject) |
| 1856860994291529096 | PERSON_3140_EMAIL | [0067] | [0068] = Owen Baker | ES-12 | "January 31, 2025" (NB-22 typo; never grade) |
| 1856861229984402233 | PERSON_4363_EMAIL | Martin | Martin Walsh | ES-13 | Jan 31 2026 |
| 1856861323365646598 | marcus.bennett@harmonygames.co | Marcus | Marcus Bennett | ES-7 | Jan 31 2026. Sent to his WORK address, the only letter that was, though #winddown idx 69 said "their personal accounts", and accounts archive by Feb 15 |
| 1856861400116562076 | brian PERSON_4243_EMAIL | [0092] | Brian Foster, [2769] [0093] | ES-15 | Dec 31 2025 |
| 1856861462411533365 | PERSON_2361_EMAIL | [0040] | [0043] = Julia Lawson | ES-1 | Dec 31 2025 |

The Equity paragraph is identical in all six (the only change is that three say "[ORG_NAME_0253]" where three say "Carta", same word under the token):

> "Equity (if applicable) If you have any equity, options, or other grants, you should receive a separate email from Carta by February 15, 2026. Any exercise rights will be governed by the applicable equity plan and your grant agreement, including any post-termination exercise window. Given the company shutdown, exercising is not recommended because the shares are expected to have no value."

- States a last day to exercise: NO, in all six. It gives no date, no window length and no vested count.
- Says shutdown: YES, in all six: "The company is shutting down; consequently, we no longer have work or a role for you." and "Given the company shutdown".
- Also in all six: return and delete by Feb 15 2026; written confirmation of deletion requested; contact PERSON_5885_EMAIL or LinkedIn after accounts go.
- Letters promise the Carta mail by Feb 15. That promise is the open item.

NOT among the six: ES-18 Oliver Brooks and ES-14 Vincent Parker, though both were terminated in Carta on Feb 12. See B and C.

### 1.2 Oct 2025 leaver notices (read in full)

| Thread | To | Holder | What it says on equity | Says shutdown? |
|---|---|---|---|---|
| 1847335165884050330 Oct 29 2025, "Notice of Involuntary Termination", cc founders; Robert 00015796, Arthur 1847335762986172865 | ryan PERSON_2314_EMAIL, "[0036]" | ES-17 | "You may choose to exercise vested options within 90 days of October 24, 2025 ... Based on a fair market value of 0.14 dollars per share, exercising 34,409 vested shares would cost about 4,817 dollars. ... Carta will show the exact numbers. Your current 90-day window ends January 22, 2026." | No: "changing direction and will not self-publish" |
| 1847333990408253969 [2] Oct 29 2025, "Notice of Termination of Consulting Agreement", cc founders; Robert 00015795, Arthur 1847334900885972692 | cameron@harmonygames.co, "[0120]" | ES-16 | "You should have received a separate email from Carta on Oct 29, 2025 ... you may exercise any vested equity within the applicable post-termination exercise window of 90 days." No date | No: breach, competitor services for Superbanana since June 2025 |

Holder reply: 1847333990408253969 [1] Oct 29: "About Carta, it says I cannot exercise online in the app, tried following few links in the dashboard with no result. Will try to investigate more how it works." Leonard [0] Oct 30: "Ok, let me know how Carta exploration goes. I haven't done it myself but if you want to move forward we can surely figure it out." Nothing later: ES-16 tried to exercise, could not, and lapsed Jan 24 2026 with no record it was resolved.

Letter against Carta for ES-17 differ in two cells: letter 34,409 vested and Jan 22 2026; Carta 34,439 and Jan 28 2026 (1847333272519888206). CALC: 34,409 x $0.14 = $4,817.26, so the letter's dollar figure follows the letter's count. Carta's last day, Jan 28, is 96 days after Oct 24; the other three same-date leavers show Jan 24 (92 days). Letter's "90-day" Jan 22 is the true 90 days. Both dates are before the clock, so ES-17 is lapsed on either reading.

Calvin (ES-3), Douglas (ES-5): no letter found. Search "changing direction" returns 3 files, all the ES-17 letter; "post-termination exercise" returns only the ES-16 thread and the six. #admin 2025-10 idx 502-507 confirms only two were sent ("termination email to [0120]", "termination notice to [0036]").

Founder working for the October set, #admin_foundersonly thread ts 1761701823.672399 (Leonard-readable): idx 482-485 Douglas "* 0.16 = $847 he can buy his current shares"; idx 487-489 [0120] "10,384 *0.14 = $1453"; idx 490-492 [0029] "* 0.16 = $705"; idx 493 "it look like we never offered shares to Samuel"; idx 494-496 [0036] "* 0.14 = $4817.36"; idx 497 "if they all buy that's $7K lol". CALC: 5,298 x 0.16 = 847.68 (ES-5); 4,408 x 0.16 = 705.28 (ES-3). So Douglas = ES-5 and [0029] = ES-3 on the numbers.

### 1.3 Carta "Termination details" (all 14 read in full)

All 14: From SVC_0077, To leonard.hayes@harmonygames.co ONLY, cc and bcc empty, one message per thread, Leonard's mailbox only (subject search over all mailboxes: 14 hits, all leonard@). Every notice: "Acceptance status Accepted", Exercised 0.

| ES | Holder as named in the notice | Granted | Vested | Grant date | Effective ("as of") | Last day | Entered (mail UTC) | Lag | Thread |
|---|---|---|---|---|---|---|---|---|---|
| 2 | [0100] | 12,208 | 3,052 | Nov 10 2023 | Aug 1 2024 | Nov 1 2024 | Aug 28 2024 | 27 d | 1808666480668498098 |
| 6 | Victor [2770] [0086] | 30,519 | 12,716 | Nov 10 2023 | Apr 16 2025 | Jul 16 2025 | May 1 2025 | 15 d | 1830952527208439510 |
| 17 | [0038] | 127,162 | 34,439 | Oct 22 2024 | Oct 24 2025 | Jan 28 2026 | Oct 29 2025 16:11 | 5 d | 1847333272519888206 |
| 16 | [2768] [0011] / EMPLOYEE_0032 | 35,605 | 10,384 | Oct 22 2024 | Oct 24 2025 | Jan 24 2026 | Oct 29 2025 16:12 | 5 d | 1847333318158821452 |
| 3 | Calvin Price | 8,138 | 4,408 | Nov 10 2023 | Oct 24 2025 | Jan 24 2026 | Oct 29 2025 16:12 | 5 d | 1847333347700620793 |
| 5 | [0612] | 10,173 | 5,298 | Nov 10 2023 | Oct 24 2025 | Jan 24 2026 | Oct 29 2025 16:13 | 5 d | 1847333395311994879 |
| 7 | Marcus Bennett | 22,889 | 12,875 | Nov 10 2023 | Jan 30 2026 | Apr 30 2026 | Feb 12 2026 22:29 | 13 d | 1856960351896429942 |
| 18 | [0022] [2767] [2763] | 15,259 | 5,404 | Oct 22 2024 | Jan 30 2026 | Apr 30 2026 | Feb 12 22:30 | 13 d | 1856960382677662910 |
| 4 | Claire Morgan | 7,630 | 4,450 | Nov 10 2023 | Dec 31 2025 | Mar 31 2026 | Feb 12 22:30 | 43 d | 1856960410709778333 |
| 1 | [0043] | 30,519 | 17,802 | Nov 10 2023 | Dec 31 2025 | Mar 31 2026 | Feb 12 22:31 | 43 d | 1856960433624350836 |
| 14 | [0051] | 3,866 | 1,530 | May 15 2024 | Nov 21 2025 | Feb 21 2026 | Feb 12 22:31 | 83 d | 1856960478782792748 |
| 12 | [0068] | 16,277 | 8,477 | Jan 29 2024 | Jan 30 2026 | Apr 30 2026 | Feb 12 22:32 | 13 d | 1856960504234892536 |
| 15 | [2769] [0093] | 10,173 | 3,391 | Oct 22 2024 | Dec 31 2025 | Mar 31 2026 | Feb 12 22:32 | 43 d | 1856960532806250145 |
| 13 | Martin [7250] Walsh | 3,866 | 2,013 | Jan 29 2024 | Jan 30 2026 | Apr 30 2026 | Feb 12 22:33 | 13 d | 1856960563574318616 |

CALC: vested total of the 8 Feb 12 entries = 55,942, the census figure. Census section 2 table re-checked cell by cell against these reads: no cell differs.

Do the notices go to the holder as well? The record does not show it. What the base holds:
- FACT: each notice is addressed to Leonard alone. The body describes the holder in the third person, so it is the administrator's copy.
- FACT, Leonard's belief about a holder copy: #admin_foundersonly 2024-08 idx 181 "we should let him know this letter is coming to his ways from Carta and he needs to decide"; idx 185-186 (ts 1724878799.746229) "he is gonna receive multiple reminders from Carta regarding exercise deadline". 2025-10 idx 505 "all Carta emails are out". Letter 1847333990408253969[2] "You should have received a separate email from Carta on Oct 29, 2025".
- FACT: ES-16 saw Carta's dashboard (1847333990408253969[1]). He does not mention a mail or a date.
- Evaluator-only: no holder mailbox on the export holds a termination mail from SVC_0077. Search over all mailboxes: 90 SVC_0077 messages: 75 Leonard, 10 Robert, 3 Vincent, 2 Martin; the Vincent and Martin ones are 2024 "verify your backup email". Marcus's Carta address is his work mailbox and it holds no Carta mail at all, not even the 2023 grant, so this absence proves nothing.
- Carta addresses, from Leonard's own lists: personal for ES-1 PERSON_2361, ES-2 PERSON_3641, ES-3 [EMAIL_0801], ES-4 PERSON_2360, ES-5 PERSON_4194, ES-12 PERSON_3140, ES-13 PERSON_4363, ES-14 PERSON_2684, ES-15 PERSON_4243, ES-17 PERSON_2314, ES-18 PERSON_1174 (1782034095239486005[34],[3]; 1789011705438137160[10],[15]). Work for ES-6 victor.barnes@, ES-7 marcus.bennett@, ES-16 cameron@.

Verdict: UNPROVEN that any holder received a Carta last-day message. Carta also does not make exercise self-serve: #admin 2024-10 idx 196 "I think I need to hit 'exercise options' here"; idx 197-198 "3052 * 0.16 = $488.32 ... He can maybe do a wire to Harmony Games"; ES-16 "I cannot exercise online in the app".

Window arithmetic (CALC). Every notice but one is effective date plus three calendar months. ES-17 is the outlier (see 1.2). Leonard says "90 days" in writing (1847333990408253969[2]; #executives 2025-10 idx 2209 "terminate all 5 on Carta so they have 90 days to decide"). The two differ for ES-14: Nov 21 + 90 days = Feb 19, Carta says Feb 21. They agree for Dec 31 and Jan 30. The window runs from the effective date, not the entry date, so late entry burns it: ES-14 lost 83 of about 92 days before anyone could see a date.

### 1.4 Group chats after Feb 11

| Channel | Who is addressed | What was said on closing | On equity, exercise, last day |
|---|---|---|---|
| C51ECE5102ED, group DM Leonard, Julia, Claire, Brian | ES-1, ES-4, ES-15 | idx 0, Feb 11 19:20 UTC, ts 1770837657.515519, Leonard: "Harmony Games'i officially kapatiyoruz" (we are officially closing), they missed the team announcement because they do not come to meetings; a termination letter will come to their personal account; "Termination tarih olarak verbally kullandigimiz end of December 25 kullanacagiz, legally protect olmak icin" (we will use end of December 25, the date used verbally, to be legally protected) | idx 1, Feb 12 13:41, ts 1770903714.600249, Claire: "Bir de equity lerimiz için birşey yapmamız gerekiyor mu prosedür olarak?" (do we need to do anything for our equity as a procedure?). idx 4-6 Leonard answers the deletion question only ("öyle yazıldı"), says take your files, invites them to Friday's all hands. **The equity question has no answer.** idx 2 Julia "Mailler ulaştı abi" (the mails arrived). idx 3 Brian, no equity word |
| #company-internal C05KNDCHAAG | listed members, `<!here>` | idx 40, Feb 11 19:59 UTC, ts 1770839984.194409: "per our conversation we'll be shutting down the company. I'll archive everyone's Google Account's by Feb 15". idx 41-44 Oliver replies about git. idx 45-46 Leonard, Arthur | Nothing. idx 39 Thomas leaves, idx 47-49 Marcus, Oliver, Owen leave at 20:40-20:41 |
| #prototype C09UHHN6PFZ | Owen, Oliver, Martin, Marcus as guests | No closing statement. idx 604-606, Feb 11 20:42: "I made ... single channel guests ... need to keep all comms here for the next week or 2", "I don't want [USERNAME_48456] to figure out our situation yet". idx 603 Claire leaves at 20:35. Work continues to the end of the export | Nothing in all 211 messages |
| #leapblock C05URGU759U | EMPLOYEE_0024, Martin's employer | idx 0 "we are shutting down Harmony Games", idx 5 "Martin was already aware", idx 6-7 no money. #winddown idx 155-159 Leapblock paid Martin Feb 1-12 and let him go | Nothing |
| D05Q3QAH2QZ Leonard-Martin | ES-13 | idx 2, Feb 11 15:46: "we will be shutting down ... won't be able to pay anyone in February ... send Everyone official termination letters as early as today. I will address all questions today at the prototype meeting" | Nothing |
| D05SDEQEK61 Leonard-Owen | ES-12 | idx 1 "I have some announcements to make" (no content) | Nothing |
| D076PSEBC4D Leonard-Brian | ES-15 | idx 6-12 Feb 12: will you continue; Robert wants to go on, we will try to take the IP | Nothing. idx 9 devices |
| D04UC0UEN2V Leonard-Segerstrale | SSP-03 | idx 0, Feb 9 19:23 "shut down the company"; idx 1 the promise; idx 16 Sunset chosen | Nothing on his grant |
| #winddown (founders only) | | idx 65 "gonna write official termination letters now"; idx 69 "for all contractors and will send them to their personal accounts"; idx 70 "I'll also cancel their Carta stuff today"; idx 81 ts 1770841239.761999 "All termination letters are sent"; idx 197 list; idx 198 ts 1770935621.095649 "Carta terminations are done" | Six letters against eight Carta entries. The founders' record reads as closed; it is not |

Sunset's stated part (f_0c37bb7235683d73569903, Feb 11 Gemini notes, Leonard-private): "board and stockholder consents"; "if not, they will provide investor notices and necessary tax write-off documentation"; "a dedicated client success manager". Nothing on option holders. 1856675475513544349[1], Feb 12 22:22 UTC: intake, then "the legal team will review all the docs, prepare your Plan of Dissolution".

### 1.5 Angel lines: last contact, Feb 2026 contact, country

Feb 2026 contact, all services. Slack 2026-02: only Segerstrale (D04UC0UEN2V, 29 msgs). Mail: only Griffin (Phil, PERSON_2847). GCal Jan-Feb events read for holder addresses: none (8047 "Kris <> Leonard" Jan 7 only). Contacts have no country for any holder. Evaluator check: Robert's mailbox 0001[5-9]* and Arthur's blake 185* show no holder traffic since Jan 15 (67 threads matched, none dated in the window). So no founder wrote to an angel either.

Traps found while reading:
- 1855403930517654215 (Feb 3 2026) subject "PERSON_3083_NAME from Brace YMCA": not Schaeppi. That token also renders Arthur Blake's own first name (1816809274978043917[1] signature). INFERENCE: this is Arthur's contact. A name search for that token gives a false Feb 2026 hit.
- patrick@harmonygames.co after 2024 is Solsten's Bergmann, not the Disli brother: 1833542911997635888 "Dear friends and partners of Solsten", 1836075678772806708 "my first book". Contacts /contacts/144 calls patrick@ a BD/Partnerships Manager.
- [6423] (SEMC general manager, #winddown idx 28) is not a holder. No hidden told-state there.

## A. Holder table (26 rows)

What is still owed to each holder is the Rule A column and the overlays in the D matrix. Live or lapsed from Carta notices and certificate digests. "Told" means a written record that reached the holder before the clock. "Told window" means a record giving the calendar last day. Mark: F = FACT, I = INFERENCE on the marked cell. All locators Leonard-readable unless marked (E).

### 12 SSP lines

| Id | Name forms | Instrument | State | Told of shutdown | Told of window | By | Last contact | Country / tz | Mark |
|---|---|---|---|---|---|---|---|---|---|
| SSP-01 | GRIFFIN GAMING PARTNERS II, L.P.; Phil, [1999], PERSON_4337 | Series Seed 2,662,255 | Live | YES: 1856675475513544349[13] Feb 9 | n/a | Leonard | 1856958794180374704[0] Feb 12 22:14 UTC | San Francisco/Santa Monica: 1856675475513544349[12] signature | F |
| SSP-02 | GRIFFIN ... Side Fund, L.P.; same GP; PERSON_2847 finance | Series Seed 84,438 | Live | YES, same mail; one signer for both funds (1774928765255297348) | n/a | Leonard | same | same | I that one mail covers both funds |
| SSP-03 | Segerstrale: [0089] [25152], [0090], [6550], [6407], [6201], Kris, Christian, PERSON_3336, PERSON_3335 | Series Seed 50,865 + ES-8 or 10, 30,518 | Live; grant has no notice | YES: D04UC0UEN2V idx 0 Feb 9. No letter, no investor mail | NO, none exists | Leonard, Slack DM | D04UC0UEN2V idx 28 Feb 12 20:27 UTC; mail 1853682990477206418[9] Jan 8 | Cambridge CB2 8EW, UK: 1770577968081445872[0] (Jul 2023) | F |
| SSP-04 | Schaeppi, Joe, Arthur [41260], [1909], [11409], [5466], PERSON_3083, PERSON_3063 | Series Seed 25,432 | Live | NO, no record | n/a | nobody | 1847629332615617366[0] Nov 6 2025 (BCC); direct 1846001072143051006[0] Oct 31 2025 | CEST: 1847629332615617366[0] | F |
| SSP-05 | Bergmann, Bastian, [4468], [11408], "patrick", PERSON_0693 | Series Seed 25,432 | Live | NO | n/a | nobody | 1836075678772806708 Jun 27 2025, from patrick@ (I); no Leonard reply found; his address last 1833542911997635888 May 30 2025 | Niederanven, Luxembourg: 1770053656612413311[13] (Jun 2023) | F; I on sender |
| SSP-06 or 08 | Sadik Enes Disli, [52949], [2927], [66357], PERSON_2260 | Series Seed 25,432 | Live | NO | n/a | nobody | 1850625296912603629[1] Dec 16 2025 (cc Leonard); Leonard to him [6] Dec 4 | Istanbul: 1770141224265557526[1]; 1847547415984757793[0] | F; which cert is I |
| SSP-06 or 08 | Patrick Haktan Disli, Patrick Lewis, patrick@ collision | Series Seed 25,432 | Live | NO | n/a | nobody | 1799418746420547240[2] May 18 2024, BCC | Istanbul: 1770141224265557526[1] | F; which cert is I |
| SSP-07 | Eren Disli, [27652], [79918] [3237], [10246], PERSON_2275 | Series Seed 25,432 | Live | NO | n/a | nobody | 1799418746420547240[2] May 18 2024 BCC; no mail from him | Istanbul: 1770141224265557526[1] | F |
| SSP-09 | Nebojsa [0127], [0112], [0113], [10455], PERSON_3941, PERSON_3935; IKE LOA LLC | Series Seed 25,432 + ES-11 6,104 | Live; grant no notice | NO | NO, none exists | nobody | 1843007315645862923[0] Sep 15 2025 (Leonard's pitch deck); from him Apr 2024 | Not found | F |
| SSP-10 | Husnu Matthew Collins, Akin, [11362], matthew.collins@ | Series Seed 25,432 + ES-9 61,038 | Live; grant no notice; left board May 1 2025 | NO | NO, none exists | nobody | 1847258343060233599[0] Oct 28 2025 (BCC) | London: same record | F |
| SSP-11 | TOR Capital Limited; [0128], [0129], PERSON_5275; PERSON_5137, PERSON_0711; TLAS PERSON_5593 | Series Seed 50,865 | Live | NO | n/a | nobody | 1799418746420547240[0] May 19 2024; TLAS 1838482551095945310[0] Jul 26 2025, unrelated | St Helier, Jersey: 1768520517901907516[6] | F |
| SSP-12 | Deepak, [2950], [0801], PERSON_1287 | Series Seed 25,432 + ES-8 or 10, 6,104 | Live; grant no notice | NO | NO, none exists | nobody | 1799418746420547240[2] May 18 2024 BCC; from him Jun 2023 | CDT: 1761665866565990705[0] (Mar 2023). Texas only in the no-persona agreement (E) | F |

### 14 ES lines

| Id | Name forms | Vested / last day | State | Told of shutdown | Told of window | By | Last contact | Country / tz | Mark |
|---|---|---|---|---|---|---|---|---|---|
| ES-1 | Julia Lawson, [0043], [0754], [0040], PERSON_2361 | 17,802 / Mar 31 2026 | LIVE | YES: 1856861462411533365; C51ECE5102ED idx 0; receipt idx 2 | NO: letter says Carta mail by Feb 15 | Leonard | C51ECE5102ED idx 6 Feb 12 14:27 UTC | Turkey: mail +03:00 1771428305047591949[1]; Turkish chat | F; country I |
| ES-2 | [0100], [0099]; name unresolved; PERSON_3641, [EMAIL_0072] | 3,052 / Nov 1 2024 | LAPSED ("forfeited", #admin 2024-11 idx 13) | NO | YES in effect: #admin 2024-08 idx 179-186; Arthur reached out, no reply (2024-11 idx 21) | Leonard, Arthur, Carta | Oct-Nov 2024, Arthur; no locator for the message itself | La Libertad, [LOCATION_1357]: gdocs/468 (E, no-persona) | F |
| ES-3 | Calvin Price, [0029] on numbers | 4,408 / Jan 24 2026 | LAPSED | NO | UNPROVEN: "all Carta emails are out" only | Carta, if at all | D050GG6KZT9 Oct 16 2025 | Not found Leonard-readable | F; [0029] I |
| ES-4 | Claire Morgan, [0040], PERSON_2360 | 4,450 / Mar 31 2026 | LIVE | YES: 1856858053929740799; C51ECE5102ED idx 0 | NO. **Asked, unanswered: idx 1** | Leonard | C51ECE5102ED idx 6 | Turkey: Turkish chat; Ankara (E, gdocs/192) | F; country I |
| ES-5 | Douglas, [0612], PERSON_4194 | 5,298 / Jan 24 2026 | LAPSED; NB-32 touches this | NO | UNPROVEN | Carta, if at all | D05Q1UD6Y77 Sep 8 2025; #admin thread Oct 29 | Not found | F |
| ES-6 | Victor Barnes, Victor [2770] [0086], [5749] | 12,716 / Jul 16 2025 | LAPSED | NO | UNPROVEN | Carta, if at all | D057F5F95JQ Feb 13 2025 | Address tokens only (gdocs/522) | F |
| ES-7 | Marcus Bennett | 12,875 / Apr 30 2026 | LIVE | YES: 1856861323365646598 (work address); #company-internal idx 40 | NO | Leonard | 1856861323365646598 Feb 11 20:16 UTC; #prototype idx 604 | Romania: Com. Cioroiași, 207196, f_af481d73feee6fd3bc4d8e | F; country I |
| ES-12 | Owen Baker, [0068], [0067], [0105], [9415], PERSON_3140 | 8,477 / Apr 30 2026 | LIVE | YES: 1856860994291529096 (date typo NB-22); #company-internal idx 40 | NO | Leonard | #prototype idx 715 Feb 12 18:00 UTC | Residencial Alturas de Holanda, [LOCATION_1357]: gdocs/477 f_bdb1b56a5ed7480ea88eda | F; country unresolved |
| ES-13 | Martin Walsh, Martin Georgiev Walsh, [7250], [9416], PERSON_4363 | 2,013 / Apr 30 2026 | LIVE | YES: 1856861229984402233; D05Q3QAH2QZ idx 2 | NO | Leonard | D05Q3QAH2QZ idx 7 Feb 12 19:05 UTC | Bulgaria: "10 Ivan Rilski Str.", f_2aa111aa51f3cf15d0425d | F; country I |
| ES-14 | Vincent Parker, [0051], [0050], [9942], PERSON_2684, vincent.parker@ | 1,530 / Feb 21 2026 | LIVE, 7 days | **NO** | **NO** | nobody | 1849344928983425627 Nov 20 21:05 UTC; D05PX3R13QF idx 54 Nov 20 21:00 UTC | Beşiktaş, Istanbul: gdocs/317 (E); Abbasağa address also gdocs/176 f_4480979d3d09c0c50a5ac8; Turkey #admin 2025-11 idx 35 | F |
| ES-15 | Brian Foster, [2769] [0093], [0092], [43101], PERSON_4243 | 3,391 / Mar 31 2026 | LIVE | YES: 1856861400116562076; C51ECE5102ED idx 0 | NO | Leonard | D076PSEBC4D idx 12 Feb 12 16:23 UTC | Maltepe, Istanbul: f_093699b840b863c38ef12d | F |
| ES-16 | [2768] [0011], EMPLOYEE_0032, [0121], [0120], cameron@. NOT "Josh Dempsey" (see C) | 10,384 / Jan 24 2026 | LAPSED | NO: letter gives breach, not closing | Partly: "window of 90 days", no date, 1847333990408253969[2] | Leonard | 1847333990408253969[0] Oct 30 2025 | Poland: f_367435eacc9712f20f38c7 | F |
| ES-17 | Frederick Stone, [0038], [0036], [0172], "Ryan", PERSON_2314 | 34,439 / Jan 28 2026 (letter 34,409, Jan 22) | LAPSED either way | NO: "changing direction". Feb 2 mail "Hope you and the team are doing well!" shows he did not know then | **YES, the only holder with a date in writing**: 1847335165884050330 | Leonard | 1856226460086133468[3] Feb 4 2026 (redacted); inbound 1856036107053480877 Feb 2 | Washington State: 1816809274978043917[0] + start Sep 4 2024 | F; WA link I |
| ES-18 | Oliver Brooks, [0022] [2767] [2763], [32704], [36999], PERSON_1174 | 5,404 / Apr 30 2026 | LIVE | YES by group post only: #company-internal idx 40, he replied idx 41. **No letter** | NO, and no pointer to Carta | Leonard, to the channel | #prototype idx 673 Feb 11 21:24 UTC; #company-internal idx 45 | Not found | F |

Totals (CALC): live option-only 8, vested 55,942; lapsed 6. Told of shutdown 10 of 26: SSP-01, 02, 03 and seven live ES lines. Not told 16: nine SSP lines, ES-14, six lapsed ES lines. Told a last day in writing 1 of 14 (ES-17, lapsed); 0 of the 8 live.

## B. The crossing: live option holders not told their last day

**Answer: all eight.** No Leonard-readable record gives any of them a date. Six have a letter that promises a Carta mail "by February 15, 2026". Two have nothing. Carta's date sits only in Leonard's inbox.

| Order | Id | Holder | Last day | Days from clock | Letter | Vested | CALC cost at strike | What crossing the sources adds |
|---|---|---|---|---|---|---|---|---|
| 1 | ES-14 | Vincent Parker | Sat Feb 21 2026 | 7 | NONE | 1,530 | $244.80 at $0.16 | Not told of shutdown either. See below |
| 2 | ES-1 | Julia Lawson | Mar 31 | 45 | Yes | 17,802 | $2,848.32 at $0.16 | Largest live line. Letter date Dec 31 was chosen "to be legally protected" (C51ECE5102ED idx 0) |
| 2 | ES-4 | Claire Morgan | Mar 31 | 45 | Yes | 4,450 | $712.00 at $0.16 | Open written equity question, idx 1 |
| 2 | ES-15 | Brian Foster | Mar 31 | 45 | Yes | 3,391 | $474.74 at $0.14 | |
| 3 | ES-7 | Marcus Bennett | Apr 30 | 75 | Yes, to work address | 12,875 | $2,060.00 at $0.16 | Letter and Carta both on marcus.bennett@, which Leonard archives "by Feb 15" (#company-internal idx 40). No personal address found in Leonard's mail |
| 3 | ES-12 | Owen Baker | Apr 30 | 75 | Yes, year wrong (NB-22) | 8,477 | $1,356.32 at $0.16 | Never grade the letter's date |
| 3 | ES-13 | Martin Walsh | Apr 30 | 75 | Yes | 2,013 | $322.08 at $0.16 | Employer of record is Leapblock; Leapblock let him go Feb 12 (#winddown idx 156) |
| 3 | ES-18 | Oliver Brooks | Apr 30 | 75 | NONE | 5,404 | $756.56 at $0.14 | Terminated in Carta as of Jan 30 yet still building on Feb 12 (#prototype idx 707-722) |

Strikes: $0.16 on f_5cd0524f448ee58833464a (template consent naming Owen, Martin, ES-14; unsigned form) and #admin 2025-10 idx 484; $0.14 on f_ce0c4b43b26e5a3505249f (ES-15..18). ES-1, 4, 7 at $0.16 is INFERENCE from idx 484 on the same Nov 2023 series. Letters give Jan 31 where Carta gives Jan 30: a holder counting 90 days from the letter reaches May 1, Carta says Apr 30.

The four advisor grants (ES-8 to 11, 103,764) sit outside this table: no notice, no last day, nobody told. "Live" for them only means no termination is recorded. Collins left the board May 1 2025 and the advisor terms ran two years to about Jul 2025 (CALC); if service ended, the ES-14 pattern (a window running with no Carta entry) could apply. The agreements are no-persona, so this cannot be decided from Leonard's reach. Keep it off the graded path or settle it with a record.

**Is one holder urgent? Yes, ES-14, on seven independent facts.**
1. Last day Feb 21, seven days from the clock, a Saturday. FACT, 1856960478782792748.
2. He resigned; he was not laid off. Mail 1849344928983425627 and D05PX3R13QF idx 50: "My last working day will be November 21, 2025. I confirm that I am choosing to voluntarily leave the company."
3. He asked. D05PX3R13QF idx 43 (ts 1763665854.644329) "herhangi bir paperwork var mı acaba"; idx 45 Leonard "yok şenlik bişi" (no, nothing formal); idx 46-47 asks only for a short voluntary-exit email as a paper trail. Equity is not mentioned.
4. Carta entry Feb 12 22:31 UTC is 83 days after the effective date. He had 9 days left when the entry was made.
5. He is outside every Feb 11 channel of record: no letter (scan of all mailboxes), not in the group DM, last Slack post Nov 23 2025 (C09Q4S613CN idx 234), none Dec-Feb. His name on the #company-internal member list proves nothing (NB-1, NB-31 logic).
6. Exercise is not self-serve. It needs Leonard to act in Carta and a wire (#admin 2024-10 idx 195-198). Chase is closed (#winddown idx 183).
7. There is a founder precedent for exactly this: at "8 days left" for ES-2 Leonard told Arthur "can you reach out to him and ask if he wants to move forward or not?" (#admin 2024-10 idx 193-195, ts 1729626587.176319). Then "I think he missed his window. I reached out to him and he didn't respond" (2024-11 idx 21).

Plain caution: nobody loses money by missing it. $0.16 strike against a $0.10 409A, and the letters say the shares are "expected to have no value". The urgency is duty and trust, not value, so no record should claim a loss. A 90-day reading gives Feb 19, not Feb 21; use Carta's date only.

Evaluator-only support: vincent@ mailbox runs to Feb 13 2026 (27 messages in 2026), none from the company about closing or Carta. Farewell D05QQ7YQTND idx 56 is not Leonard-readable.

## C. Holders whose real state differs from the owner list or the Feb 12 list

The owner list calls 13 option holders "Owners" with "shares". The Feb 12 list says angels are open and Carta is a task, then "Carta terminations are done". Against the base:

| Id | List suggests | Real state | Why it matters |
|---|---|---|---|
| ES-17 Frederick Stone | Largest non-Griffin, non-founder line, 127,162, 1.263%. Roster role "Co-founder" | Nothing at the clock. 34,439 vested, lapsed Jan 28 (letter: Jan 22). Payroll is_founder False, "Commercial Lead"; Contacts /contacts/138 same; on no certificate. Invited to the Jan 14 2026 board meeting (GCal 6127) but is no director | A "co-founder" who is not one, holds no stock and no live option, and has not been told. He last wrote Feb 2 |
| ES-5 Douglas | 10,173 | Nothing. Lapsed Jan 24. Ledger pays him to Dec 31 (FIN-000683): NB-32. If service really ran to Dec 31 the window would be Mar 31 | Carta must decide, stated in the rule; never grade his end date |
| ES-3 Calvin Price | 8,138 | Nothing. Lapsed Jan 24. Payroll has one row, Apr 2025, "General Counsel" | Roster persona, nothing at the clock |
| ES-6 Victor Barnes | 30,519 | Nothing. Lapsed Jul 16 2025. Payroll runs to Oct 2025, against Carta's Apr 16 | Roster persona. Warehouse disagrees with Carta; no Slack from him in late 2025 supports Carta |
| ES-16 | 35,605 | Nothing. Lapsed Jan 24. Tried to exercise, failed, thread open | Leonard: "we can surely figure it out". Nothing followed |
| Samuel Turner | Roster Game Designer, not on list | "it look like we never offered shares to Samuel" (#admin 2025-10 idx 493). Holds nothing, never did | Correct to leave out; a solver may add him from the roster |
| ES-14 Vincent Parker | "[0051] 3,866", name a token; Feb 12 "done" | 1,530 live, 7 days, untold. Roster "Game Systems Engineer"; his own letter says Game Designer (f_623913a57e4fef9ac0dc4b). Ledger pays him to Dec 31 (FIN-000681) against Nov 21 resignation | The "done" item hides the one live emergency. Census had him TOKEN |
| ES-18 Oliver Brooks | "All termination letters are sent" | No letter. Only 6 letters exist | Founders' statement is off by one, and also off by ES-14 if "all" meant all Carta entries |
| ES-12 Owen Baker | Census PART by inference | FULL: f_414596b0a9d698267dd1e1 "Owen Baker – 0.162%" = 16,277 | Second Leonard-owned owner list, Nov 4 2024, tokens differ from LIST. It also spells "Arthur Schaeppi" and "Patrick Lewis" |
| 8 live lines | Grant size | Vested only: 55,942 of 110,479 granted (CALC) | Every live line's number moves |
| SSP-03, 09, 10, 12 | 81,383, 31,536, 86,470, 31,536 | Stock 50,865 / 25,432 x3 plus advisor grants | Census ADV channel stands |

Census corrections: ES-5 is Douglas, ES-1 Julia Lawson, ES-14 Vincent Parker, ES-15 Brian Foster, ES-12 Owen Baker, all provable. Census name status moves from 18 FULL, 6 PART, 5 TOKEN to 24 FULL, 4 PART, 1 TOKEN of 29 (CALC: ES-1, 5, 12, 14, 15, 17 move to FULL; PART stays Bergmann, Nebojsa, Deepak, ES-16; TOKEN is ES-2). Census line "No record tells [0051], Calvin, [0612], Victor, [0100]" stands, and gains ES-16 and ES-17, which got notices that do not say shutdown. The census's six Feb 11 letters are right; it did not map them. They are ES-1, 4, 7, 12, 13, 15.

### Token-to-name mapping

**ES-17 ([0038]) = Frederick Stone: PROVABLE from Leonard-readable records. Not Atlas-only.**
1. Carta "[0038]" ES-17 127,162: 1847333272519888206.
2. Leonard's list: "[0038] ... 127,162 ... PERSON_2314_EMAIL ... 9/4/24": 1782034095239486005[3].
3. Letter to "ryan <PERSON_2314_EMAIL>", "[0036]": 1847335165884050330.
4. "[0038] <frederick.stone@harmonygames.co>" in mail headers: 1766143815460517446, 1772415006259670038.
5. Offer letter "[0038] Offer Letter" f_a17bda426285acec3020e2, Leonard-owned, shared with frederick.stone@, VP Marketing & BD, start Sep 4 2024, "Dear Ryan".
6. D05S58U4SAK: Slack user Frederick Stone, Leonard posts "[0036] <> Leonard" idx 17. Contacts /contacts/138.
Second owner list token [0172] (f_414596b0a9d698267dd1e1), same in f_ce0c4b43b26e5a3505249f.

**ES-14 ([0051]) = Vincent Parker: PROVABLE, and stronger.** 1849344928983425627: From vincent <vincent.parker@harmonygames.co>, Subject "Resignation - [0051]". D05PX3R13QF idx 50: Slack user Vincent Parker signs [0051]. 1775854887109011340: "[0051] has accepted", from vincent.parker@. f_623913a57e4fef9ac0dc4b "[0050] Employment Verification Letter" shared with vincent.parker@. 1789011705438137160[10]: "Full Name: [0051] Email: PERSON_2684_EMAIL Option Grant: 3866".

**ES-16: the person is provable, "Josh Dempsey" is not.** Chain: Carta "[2768] [0011]", body "EMPLOYEE_0032 [0011]" (1847333318158821452); 1782034095239486005[3] "[0121] Full Legal Name: [2768] [0011] ... 35,605 ... cameron@harmonygames.co ... 8/19/24"; letter to cameron@, "[0120]"; f_414596b0a9d698267dd1e1 "EMPLOYEE_0032 – 0.354%"; f_367435eacc9712f20f38c7 "EMPLOYEE_0032 from Poland", Unity engineer. That is one person, keyed by tokens and cameron@.
"Josh Dempsey" reaches him only through employee_id EMPLOYEE_0032 in PAYROLL_ROSTER and FINANCE_LEDGER (unscoped, so readable, plus the Atlas). Leonard's mail contradicts it:
- Josh Dempsey is josh.dempsey@harmonygames.co on the June 2023 Solsten MNDA thread (1763470202195355185) and Solsten meeting accepts, 14 months before ES-16 joined. Contacts /contacts/59 "Business Development Manager", a separate row from /contacts/0 EMPLOYEE_0032.
- Ledger starts Mar 31 2024 (FIN-000183), role "product". ES-16's agreement and vesting start Aug 2024, Unity engineer.
INFERENCE: the warehouse label is a bad join. Grade ES-16 by id only; never put "Josh Dempsey" in a title or a note.

## D. Closed-rule candidates, applied to all 26

Shared terms, each decidable from named records:
- **Lapsed**: option-only line whose Carta "Last day to exercise" is on or before Feb 14 2026. Carta's date governs over letters, payroll and ledger.
- **Told**: a written record of the closing reached the holder before the clock. Reach means addressed to the holder, or a thread the holder replied in. A channel member list is not reach.
- **Dated**: a written record to the holder gives the calendar last day.

**Rule A, the two-bit crossing (recommended).**
A1 Lapsed line: no note.
A2 Stock line, not told: first personal note.
A3 Stock line, told: no first note.
A4 Live option-only line, told, not dated: short note giving Carta's last day.
A5 Live option-only line, not told: one note covering the closing and the last day, sent first.
Counts: A1 6, A2 9, A3 3, A4 7, A5 1 = 26.

**Rule A-prime.** Same, but reach means addressed to the holder personally, so a group post does not count. ES-18 moves to A5. Counts: A1 6, A2 9, A3 3, A4 6, A5 2 = 26.

**Rule C, deadline only.** Every live option-only line gets a dated note, ordered by last day. Counts: 8 notes (1 + 3 + 4 by date), 18 none. Closed and trivial; drops the angels.

**Rule D, promise only.** Everyone not told gets told, live or not. Counts: 16 notes, 10 none. Sends notes to six people holding nothing and never sends the date to seven who need it.

**Overlays, each a separate closed sentence.**
- O1 Open written question from a holder gets an answer: ES-4 (equity, idx 1), ES-16 (exercise, 1847333990408253969[1]). Count 2.
- O2 Letter owed: Carta terminated, no letter on file: ES-14, ES-18. Count 2.
- O3 Route: no note to an address archived by Feb 15: ES-7 (only known address is work), ES-14 (use PERSON_2684, not vincent.parker@). Count 2.
- O4 Advisor grant line in the note, only if a record settles grant status: SSP-03, 09, 10, 12. Count 4.

| Id | Rule A | A-prime | C | D | Overlays |
|---|---|---|---|---|---|
| SSP-01 | A3 none | A3 | none | none | |
| SSP-02 | A3 none | A3 | none | none | |
| SSP-03 | A3 none | A3 | none | none | O4 |
| SSP-04 | A2 first | A2 | none | note | |
| SSP-05 | A2 first | A2 | none | note | |
| SSP-06/08 Enes | A2 first | A2 | none | note | |
| SSP-06/08 Patrick | A2 first | A2 | none | note | |
| SSP-07 | A2 first | A2 | none | note | |
| SSP-09 | A2 first | A2 | none | note | O4 |
| SSP-10 | A2 first | A2 | none | note | O4 |
| SSP-11 | A2 first | A2 | none | note | |
| SSP-12 | A2 first | A2 | none | note | O4 |
| ES-1 | A4 short | A4 | Mar 31 | none | |
| ES-2 | A1 none | A1 | none | note | |
| ES-3 | A1 none | A1 | none | note | |
| ES-4 | A4 short | A4 | Mar 31 | none | O1 |
| ES-5 | A1 none | A1 | none | note | |
| ES-6 | A1 none | A1 | none | note | |
| ES-7 | A4 short | A4 | Apr 30 | none | O3 |
| ES-12 | A4 short | A4 | Apr 30 | none | |
| ES-13 | A4 short | A4 | Apr 30 | none | |
| ES-14 | A5 full | A5 | Feb 21 | note | O2, O3 |
| ES-15 | A4 short | A4 | Mar 31 | none | |
| ES-16 | A1 none | A1 | none | note | O1 |
| ES-17 | A1 none | A1 | none | note | |
| ES-18 | A4 short | **A5 full** | Apr 30 | none | O2 |

**Every holder where two sentences of a rule disagree.**

| Id | Sentence X says | Sentence Y says | What settles it |
|---|---|---|---|
| SSP-03 Segerstrale | A3: told by DM Feb 9, no note | Leonard's promise "every angel investor" (idx 1) and Feb 12 list "our angels"; he got no investor mail and his grant is unaddressed | Needs a stated line: a personal DM counts as the outreach, or it does not |
| SSP-02 Side Fund | A3: told via Phil | "Told" is per line, and no mail names the fund | One sentence: a fund is told through its GP |
| SSP-06/08, SSP-07 Disli | A2: a first note per line, three notes | Enes supplied all three addresses and speaks for them (1770141224265557526; 1774211155651873582); Eren has no mail at all | The FAM rule; needs a stated record, as the analysis says |
| SSP-05 and SSP-06/08 Patrick | A2 note goes to the holder | patrick@ reaches Bergmann after 2024 by the mail on file | Never grade an address |
| SSP-09 Nebojsa | A2 note to the person | Possible holder of record IKE LOA LLC (1770577968081445872[1]) | Off the graded path |
| SSP-03, 09, 10, 12 | "Live" stock line, note about stock | Grant live only because no notice exists; service may have ended (B) | O4 needs a record; otherwise silent on grants |
| ES-18 Oliver | A4: told, he replied at idx 41 | O2 and A-prime: no letter, so not told personally | Reply test, stated. A cold reader will see he knows; A-prime reads false |
| ES-14 Vincent | A5: not told | A listed member of #company-internal at the `<!here>`, so a loose "told" gives A4 | "A channel member list is not reach", stated |
| ES-5 Douglas | A1: Carta Jan 24 | Ledger pays to Dec 31 (FIN-000683); NB-32. On Dec 31 he would be live to Mar 31 | "Carta's date governs". Never grade his end date |
| ES-6 Victor | A1: Carta Jul 16 2025 | Payroll end Oct 2025 | Same sentence |
| ES-16 | A1: no note | O1: open exercise thread, Leonard's "we can surely figure it out" | Say whether O1 reaches lapsed lines |
| ES-17 Frederick | A1: no note | Promise and courtesy: he wrote Feb 2, Leonard replied Feb 4 (redacted), and he is the one person with a date that disagrees with Carta | A1 stands; the redaction is an evidence limit |
| ES-12 Owen | A4: told | Letter's date is wrong (NB-22) | Told is about the closing, not the date |

Decidability. A1 to A5 are decidable for all 26 from 14 notices, 6 letters, 2 Oct notices, C51ECE5102ED, #company-internal idx 40-44, D04UC0UEN2V and 1856675475513544349. No sentence needs a PDF. Against the two wrong sources: the owner list misstates 17 of its 24 non-founder lines (5 lapsed, 8 vested-only, 4 merged, CALC); "Carta terminations are done" misstates all 8 live lines.

## E. Voices

Who can carry a settling record without being the owner of the list. Date any seed after what it relies on.

| Voice | Natural for | Base anchor | Limits |
|---|---|---|---|
| Sunset legal or client success manager | The method record: what counts as told, Carta's date governs, what option holders get | 1856675475513544349[1]: legal team prepares the Plan, "dedicated customer success manager"; Gemini notes: "investor notices", "board and stockholder consents" | Unnamed in the base: census any new person. After Feb 12 22:22 UTC. Must match the signed SOW (PDF, UNREAD). Notes say Sunset gives investor notices, so the seed must leave Leonard's personal outreach to him |
| PERSON_0767 Sunset founder/CEO; PERSON_2888 Head of Partnerships ("Jackie Alfenas" in the Gemini notes); PERSON_3131 CTO | Same, if a named sender is wanted | Same thread; 1856872398290956689 | PERSON_3131 is data only. Sunset "cannot support negotiating" creditors; do not stretch it |
| Arthur Blake | Fact of contact: he handled ES-2's reach-out; Carta co-admin; repo seats for "whoever still works on it" (#company-internal idx 46) | #admin 2024-11 idx 21; #winddown | A founder, so not non-owner in the strict sense. Fine for ES-18's status. Post in #winddown before Feb 13 10:03 UTC |
| Robert | Same; he is already asking staff about plans (D05UDNCCFEW, E) | #prototype, #winddown | Founder |
| Phil, PERSON_4337 | Griffin's position as investor | 1856958794180374704[1] | Not as a director after Feb 12 22:05 UTC |
| PERSON_2847 Griffin finance | KPMG, FY numbers | cc on 1856958794180374704; 1817557789846606177 | Not on holder notes |
| KPMG PERSON_3088, PERSON_4416 | As-of confirmation | 1817557789846606177 | Not told state |
| Segerstrale | Angel view: what an angel expects; he said do it correctly (D04UC0UEN2V idx 8) | Live DM to Feb 12 | Must not say any other holder knows. Before Feb 13 10:03 UTC |
| TLAS PERSON_5593 | Tor's cap table or notice route | 1838482551095945310 | Last contact Jul 2025; she declined engagement; speaks for Tor only |
| Leapblock EMPLOYEE_0024 / [0083] | Martin's status only | #leapblock | Martin's letter already exists |
| Carta SVC_0077 | Automated reminder to the administrator | 75 notices in Leonard's box | Automated, never a settling rule. Do not seed an export |
| Claire, Julia, Brian in C51ECE5102ED | A follow-up on equity | Group DM still live on Feb 12 | Pointing record: it lowers difficulty. Base idx 1 already carries the fact |
| Vincent from PERSON_2684 | A question of his own | 1789011705438137160[10] | Would change his told state and may contradict "not told": avoid |

Must not speak:

| Who | Bar | Source |
|---|---|---|
| Julia, Marcus, Owen, Oliver, Martin, Claire, Brian | In any channel they left after Feb 11 20:40 UTC. Safe: #prototype for Owen, Oliver, Martin, Marcus; DMs; C51ECE5102ED for Claire, Julia, Brian. Claire left #prototype at 20:35 (idx 603) | NB-1 |
| Thomas | Left #company-internal Feb 11 19:58 (idx 39) | NB-1 logic |
| Anyone in Slack | After Feb 13 10:03 UTC | NB-6 |
| Frederick Stone | No company channel or address: Google archived Nov 13 2025 (#admin 2025-11 idx 52). Not as founder, director or staff. Personal mail only | Left Oct 24 |
| ES-16, Calvin, Douglas, Victor, ES-2 | Left; no internal voice. Douglas also NB-32 | Carta dates |
| Vincent Parker | Left Nov 21; last Slack post Nov 23 2025. Must stay untold | D05PX3R13QF |
| Matthew Collins | Not as director or for the board. Resigned May 1 2025 | 1830959847543474636[3] |
| Benjamin Clark, michelle | Not as current counsel: Leonard told TLAS "Our current counsel ... has stepped away from private practice in March" (1838482551095945310[4]) | INFERENCE that this is Clark |
| Any seed | Must not say Leonard already told an angel, or that ES-14 or ES-18 got a letter or a date; #winddown idx 197 and the mailbox scan contradict it | Base |
