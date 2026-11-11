# Census B: investor close-out / cap table (Feb 14, 2026 normal universe, persona Robert)

Status: COMPLETE. Facts and locators only. Section 0 is the working log; sections 1 to 9 below are the census.
Gmail pointers are `threads/<n>.json` in Robert's mailbox unless stated (Robert's mailbox = threads 00000674 to about 00016909).

## 0. Early findings (working notes, superseded by the sections below when they are filled)
- Cap table figures in Robert's mail: threads/00001152.json (Jul 7-10 2023, 12 msgs, counsel B. Clark): first draft wrong (founders 4,500,000), corrected msg[2]: founders 6,000,000 / Series Seed 3,051,882 / pool 1,017,294 / advisors 103,763.99 / total 10,172,940, "Price Per Share $1.0173". Leonard confirms msg[4].
- Griffin split: threads/00001194.json msg[1] (Jul 20 2023): GGP II L.P. $2,616,996.67 / 2,662,255 sh; GGP II Side Fund $83,002.56 / 84,438 sh.
- Disclosure Schedule f_d690045a2f2bf47108ae99 (Robert YES): 10,000,000 common auth, 6,000,000 issued; 3,051,882 Series Seed; pool 1,017,294.
- Due Diligence Disclosures f_6a37227593d0977fdbdd7a (Robert YES): officer loans $15,500/$13,000/$7,000 = $35,500; 4 advisors 1.7% = 103,764 sh.
- Reset Financing term sheet f_11040fe5d66821bd6951aa and framework f_f09041fe1e83ead96b3d09: Robert NO (Leonard-owned, 0 shares).
- Seed price $0.9830/share: #executives C07C2866011 2026-01 idx 708 (ts 1768415499.678309), idx 727 (ts 1768416262.426129), idx 728 (ts 1768417784.194359). Those posts give 3,051,881 seed issued, 1,121,058 reserve, FD 10,172,939, Other Seed investors 305,188.
- P&L Jan 2026 sheet f_605121f4a36752645e0ac3 (Robert YES): Funding (Preferred Shares) Jul-23 $2,700,000; Aug-23 $200,000; Sep-23 $75,000; Oct-23 $25,000 = $3,000,000.
- Tor Capital Limited $50K: threads/00001092.json msg[3].
- Griffin wires received Jul 21 2023: $2,616,996.66 and $83,002.55 (threads/00003071.json), a cent off the SOP in threads/00001194.json.
- Angel commitments (Jun 2023): #founders C04UTBZL6AX 2023-06 idx 486 (ts 1686163563.837369), #investors C04UM32UWKD 2023-06 idx 491-506, 535-537. "17 stakeholders": #admin_foundersonly C04UEQVDVB7 2023-08 idx 663 (ts 1692123029.471909). Wires: 2023-08 idx 182/358/516/641; 2023-09 idx 236/239/315; 2023-10 idx 396.

---
# CENSUS

## 1. Cap-table-grade sources (reach = Robert)

Scope: Drive 53,866 file records and gdocs 633 records searched by name; Robert's mailbox subject and body searches over threads/000[01]*.json; Sheets title and cell search. There is no Carta system of record in the universe. Carta exists only as mail notices and Slack talk.

### 1a. Robert CAN read (native text)
| id | title | owner | date | holds | state |
|---|---|---|---|---|---|
| f_d690045a2f2bf47108ae99 | Harmony Games Inc Disclosure Schedule | Arthur, shared to Clark, Robert, Leonard | 2023-07-10 | 10,000,000 common authorised, 6,000,000 issued; 3,051,882 Series Seed designated; 1,017,294 pool | Draft. Option/RSPA counts are literal blanks "[_______]". No holder table. |
| f_f2054f1311fb4146353037 | Outline of Disclosure Schedule | Arthur | 2023-07-07 | NVCA rep skeleton | Draft |
| f_6a37227593d0977fdbdd7a | Due Diligence Disclosures | Leonard, 5 shares | 2023-07-10 | Officer loans $15,500 / $13,000 / $7,000 = $35,500; advisor table 0.5% 30,518, 1% 61,038, 0.1% 6,104, 0.1% 6,104 = 1.7% 103,764; Claire Morgan verbal 0.038% | Complete; names partly tokenised |
| f_5e80ba8a32129193f119bc | Term Sheet Analysis | Resource 7240..., shared to Leonard, Arthur, Robert, PERSON_3336, Clark | 2023-06-06 | Griffin Jun 6 2023 term sheet with Leonard's notes: $3M, $10M post, dividend 8% non-cum, 1x, protective provisions, board, drag-along | Term sheet, NOT the filed charter |
| f_ce0c4b43b26e5a3505249f | Board Consent Option Grants Q4 2024 | Resource 7240..., shared to Leonard, Arthur, Robert, founders list | 2024-10-17 | Exhibit A: Oliver Brooks 15,259; [ORGANIZATION_3503] 35,605; [PERSON_NAME_43101] 10,173; [PERSON_NAME_0172] 127,162; strike $0.14 | Complete; 3 of 4 names tokenised |
| f_5cd0524f448ee58833464a | Board Consent Option Grants Template (Q2 24 grants) | Resource 7240..., shared | 2024-05-14 | [PERSON_NAME_9415] 16,277; Martin [PERSON_NAME_9416] and [PERSON_NAME_9942] share counts REDACTED as [CREDIT_CARD_NUMBER_0548]; strike $0.16 | Numbers partly destroyed |
| f_b5cac6b6428ae5268e9d46 | Board Consent Salary Freeze | Resource 7240..., shared | 2025-05-01 | Board action | not read for holders |
| f_83e4b5195ae4c432699ad2, f_a5f0b190669221bea0520b | Founders Stock Purchase Agreement (template pair) | Robert | 2023-04-11 | Form | Robert's Legal Docs folder |
| f_98139fe59fc8ac379ffacf, f_60037f20b11c95306dbcec | Organizational Consent | Robert | 2023-04-11 | Formation consent | |
| f_2187a0763c4f33752d4d53, f_66095cf21d30150c080754 | Certificate of Incorporation (pre-seed) | Robert | 2023-04-11 | Original charter, NOT the restated one | superseded |
| f_605952e48eb7ad3efa8f38 / f_f48ce41e7f638848670166 / f_1b59f8add3874350651f77 | Promissory notes (Arthur $7,000; Robert $7,000; Leonard) | Robert / Resource | 2023-04-25 | Founder loans | |
| f_af481d73feee6fd3bc4d8e, f_2aa111aa51f3cf15d0425d, f_d2f01836491ac7e2e4b22f, f_5d08b987dd42240501fd50, f_093699b840b863c38ef12d, f_a17bda426285acec3020e2 | Consulting agreements / offer letter with option clause | Resource 7240 / Leonard, shared | 2023-2025 | Marcus 22,889; Martin 3,866; Victor 30,519; [0043] 30,519; [0092] 10,173; [0038] VP Marketing & BD 127,162 | Offer amounts, not grants |
| f_3ee38465decc57e61df6e5 | Advisor Agreement [PERSON_NAME_0127] | Resource 7240, shared | 2023-09-08 | 6,104 shares, as of Jul 21 2023 | The only advisor agreement Robert can read |
| f_605121f4a36752645e0ac3 (and other P&L tabs) | P&L and forecast Jan 2026, tab HG P&L, row 18 | Resource 7240, shared | | Funding (Preferred Shares): Jul-23 2,700,000; Aug-23 200,000; Sep-23 75,000; Oct-23 25,000 | NB-2/NB-3 sheet family; funding row only |
| f_00c30de5acd0cf7656c140 etc. | Offer Parameters sheets (Martin f_3f7505f95c01726fc1793c, Marcus f_5c11246c68bd54413f70b2, [0120] f_12726d993580473e498729, douglas f_977e1c8d1daf3ea744c041, f_cd3829766ba935bc451650) | Resource 7240, shared | 2023-2024 | Equity % offer calculators | Offer menus, not grants |

### 1b. Robert's Gmail (threads/<n>.json) that carry cap-table facts
00001152 Cap Table (Jul 7-10 2023); 00001194 Revised SPA and Certificate (SOP numbers for Griffin); 00001114 Series Seed (17 msgs, 20 attachments, diligence on single-trigger, Continuous Service); 00001195 Closing Checklist; 00001200 signature packet; 00001285 2nd close; 00001092 Tor $50K; 00001356, 00001446, 00001622, 00001632, 00001660 Tor second close; 00001538 and 00001805 PERSON_1287 angel/advisor; 00001412 Carta onboarding (21 msgs: price $0.0001, $200 per founder, SSP-08/09/10 certificate ids); 00001417 409A inputs; 00001413 equity contracts; 00001542 Sep 8 2023 board approvals ($0.16 409A, side letter, loan repayment); 00001822 angel close and "Employee Stock" tab; 00001895 closing set to investors; 00001948 option issuance, directors and team list; 00001961/00001963 Option Grants Nov 2023; 00004760 and 00008065 option consents; 00003071 KPMG audit confirmation (wires, Carta xlsx attachment); 00011034 "Cap table hasn't changed in 2024"; 00016526 recap ask; 00016827 shutdown notice; 00016903 Griffin director resignation.

### 1c. Exists but Robert CANNOT read (persona_view NO, or not in his mailbox)
- Reset term sheet f_11040fe5d66821bd6951aa and framework f_f09041fe1e83ead96b3d09: NO.
- Series Seed SPA, all copies: Leonard f_966445655f653d26dc8537 NO; Arthur f_6ca56d6a31b11edde441ce NO. Text is a form with blank Schedule of Purchasers anyway ("purchase price of $[] per share", Exhibit A empty).
- IRA, ROFR/Co-Sale, Voting Agreement: all Leonard or Arthur copies, 0 shares, NO by the same rule (spot-checked SPA; shared lists are empty on every copy).
- Tor side letter f_6201c7027d02997bfb2c84: NO. Founder amendment f_9e3086d26af0da29977c38: NO.
- GGP Due Diligence folder d_7438da82fd2614f44840a8 and its Capital Stock subfolder d_6f5a2b20d5d82d7431e76e: Leonard, 0 shares. A two-level walk shows 3 PDFs shared to Robert (External FAQ f_05eb8d514e89127c3463b0, Pitch Deck f_d031ee8492450cdd6c13ae, Hayes_semc agreement f_2dd8a90d09d991c86cb752), none of them equity documents. Deeper levels not walked.
- Advisor agreements for Matthew Collins f_c2c881ccc407fbdaeaa362, Segerstrale f_e48755daf914ce68a899e0, PERSON_1287 f_7982b7ac6db8b5e2b7840a: NO.
- Consulting agreements with option clause, Robert NO: Calvin 8,138; Claire 7,630 (v2) and 3,866 (v1); Oliver 15,259; [0051] 3,866; [0068] 16,277; [0100] 12,208; [0612] 10,173; [2768]/[0011] 35,605.
- "Harmony Games Cap Table" Sheet (link 1qzUDjigj0LmzinXX8t0uqZDxAz4a346Dw7uL45ovVW8; share notice threads/00001360.json Aug 10 2023; #admin_foundersonly 2023-08 idx 504 "Our final cap table"): NOT IN THE UNIVERSE under that title. Sheets title search "cap", "ledger" finds no such sheet, Drive name search "cap table" 0 hits. Dead link.
- Carta exports: Drive sidecars f_7cc13cef3dbeda4e0d8f1d and f_8fbcee9068d3dcbc3e66cf are metadata JSON of 1.5KB / 0.9KB, no ledger.
- Harmony Games Shares sheet f_e758b2128e21984a0ad09a: Leonard, 0 shares, founder vesting grid only.
- Bridge Round sheet f_efaec72066ee44e5888bd7: shared list 0 (Resource 7240).
- Equity Value Calculators folder d_08e92865de334c505d0fe0: 0 child records.

## 2. Holder cohort Robert can build

Base data only. "Conf" = independent records Robert can read that confirm the figure. Share figures marked calc are $ / $0.9830, not read from any record.

### Series Seed Preferred
| Holder (token/name) | $ | Shares | Locator | Conf |
|---|---|---|---|---|
| Griffin Gaming Partners II, L.P. | $2,616,996.67 SOP; $2,616,996.66 wire | 2,662,255 | threads/00001194.json msg[1]; threads/00003071.json; #executives 2026-01 idx 727 | 3 |
| Griffin Gaming Partners II Side Fund, L.P. | $83,002.56 SOP; $83,002.55 wire | 84,438 | same | 3 |
| TOR Capital Limited (Jersey), via [PERSON_NAME_0128]/PERSON_5275 | $50,000 | 50,864 calc | threads/00001092.json msg[3]; #admin_foundersonly 2023-09 idx 315; FINANCE_LEDGER FIN-000060 | 3 |
| Matthew Collins | $25,000 | 25,432 calc | #founders 2023-06 idx 1971; #admin 2023-09 idx 236 | 2 |
| Deepak = [PERSON_NAME_2950] = PERSON_1287 | $25,000 | 25,432 calc | #investors 2023-06 idx 491, 493; #admin 2023-10 idx 282, 396; threads/00001805.json | 2-3 |
| Nebojsa = [PERSON_NAME_0112] / [0127] | $25,000 | 25,432 calc | #founders 2023-06 idx 473, 486 | 1-2 (commitment only; no wire tied to him) |
| Solsten CEO [PERSON_NAME_11409] | $25,000 | calc | #founders 2023-06 idx 472, 486; 2023-08 idx 196, 206 | 1-2 |
| Solsten COO [PERSON_NAME_11408] | $25,000 | calc | same | 1-2 |
| Segerstrale = [PERSON_NAME_6550]/[0090]/[0089] | $100,000 committed, "giving up $25K" so $75,000 INFERRED | calc | #founders 2023-06 idx 486; #investors 2023-06 idx 535 | 1 for $75K |
| Enes = [PERSON_NAME_2927]/[66357] (CEO Libra Softworks) and brothers [PERSON_NAME_26149] | $100,000 committed, "reduce down to $75K"; balance implies about $50,000 family total | UNKNOWN split | #investors 2023-06 idx 503; #admin 2023-08 idx 490, 928, 1002 | 0 for the final figure |

Tie-out: angels sum to $300,000 only if Enes family = $50K and Segerstrale = $75K, which is my inference. The record says other Seed holders total 305,188 shares (#executives 2026-01 idx 728), and 305,188 x $0.9830 = about $300,000.
Holder-line count: 11 or 12 preferred lines. Certificate ids reach SSP-10 on Sep 13 2023 with Tor and Deepak still to come (threads/00001412.json msg[16]), which points to 12 if numbering began at SSP-01 with no cancellations. That fits Griffin 2, Patrick, Segerstrale, [0112], [5466], Enes and 2 brothers, then Matthew, Tor, Deepak. No record lists them. "17 stakeholders" on Aug 15 2023 (#admin 2023-08 idx 663) is not itemised.

### Common
Leonard, Robert, Arthur: 2,000,000 each, $0.0001, $200 cash, issued 04/18/2023 (threads/00001412.json msg[1], msg[7]; threads/00001152.json msg[1]; #executives 2026-01 idx 728). Only Leonard's lines are stated outright; the other two follow from "2M shares each".
Founder notes: $35,500 lent (DD doc; ledger FIN-000004, 000010, 000016 = 21,000 + 2,500 + 12,000), repayment consent Sep 2023 (threads/00001541.json, 00001581.json) and a ledger loan_repayment row, so no founder debt claim is apparent. Repayment row amount not read.

### Advisors (all four are also angels)
Due Diligence Disclosures f_6a37227593d0977fdbdd7a: Segerstrale 0.5% 30,518; Matthew Collins 1% 61,038; [0801] 0.1% 6,104; [6408] 0.1% 6,104; total 103,764. Signed: #admin 2023-09 idx 272, 284; Deepak Oct 17 2023 (#admin 2023-10 idx 282). Robert reads one agreement only, f_3ee38465decc57e61df6e5.

### Options (offer or grant figures; exercised status unknown)
| Holder | Shares | Robert-readable source |
|---|---|---|
| [0172]/[0038] VP Marketing & BD ("Dear Ryan") | 127,162 | f_ce0c4b43b26e5a3505249f; f_a17bda426285acec3020e2 |
| [ORGANIZATION_3503]/[2768]/[0121] Lead Engineer | 35,605 | f_ce0c4b43b26e5a3505249f |
| [0043] | 30,519 | f_5d08b987dd42240501fd50 |
| Victor | 30,519 | f_d2f01836491ac7e2e4b22f |
| Marcus Bennett | 22,889 | f_af481d73feee6fd3bc4d8e |
| [9415]/[0068] | 16,277 | f_5cd0524f448ee58833464a |
| Oliver Brooks | 15,259 | f_ce0c4b43b26e5a3505249f |
| [43101]/[0092]/[0093] PM | 10,173 | f_ce0c4b43b26e5a3505249f; f_093699b840b863c38ef12d |
| Martin Walsh | 3,866 | f_2aa111aa51f3cf15d0425d |
| [0100] | 12,208 | Robert NO (f_b9c1a318597221548a671c) |
| [0612] | 10,173 | Robert NO |
| Calvin Price | 8,138 | Robert NO |
| Claire Morgan | 7,630 v2, 3,866 v1 | Robert NO; he sees only "0.038%" in the DD doc, which is the superseded number |
| [0051]/[9942] | 3,866 | Robert NO; the consent cell is redacted |

Named option holders: 14; Robert has a count for 9. Sum of the 14 = 334,284 (Nov 2023 list 122,076; Q2 24 24,009; Q4 24 188,199). Term sheet says options outstanding 268,772 (Robert NO). The gap of 65,512 is unexplained and likely lapsed grants of departed staff, but no record says which. Possible extras with offer sheets only: Douglas, [0120], [0067] (likely = [0051]); Trello card 688 "[PERSON_NAME_0116] Carta" Apr 2025.

### Size verdict
Scope: unique holders in base data. 3 founders + 11-12 preferred + 14 option-only = 28-29, and the 4 advisors overlap angels. Up to about 31 with the offer-sheet names. A cohort of 40+ is NOT honest without injection. Holders with a provable figure from Robert's reach: about 12 with a real name (3 founders, 2 Griffin, Tor, Matthew, Deepak, Victor, Marcus, Martin, Oliver), about 17 counting the 5 token-only option holders.

## 3. Alias structure

| Real | Forms in records | Resolved by (Robert-visible unless noted) |
|---|---|---|
| Griffin (firm) | [PERSON_NAME_2000], [ORGANIZATION_NAME_0151], [ORG_NAME_0153], [ORGANIZATION_0351], [PERSON_NAME_0203], GGP, GRIFFIN GAMING PARTNERS | threads/00001194.json msg[1] vs msg[2]; #founders 2023-06 idx 486 "GGP"; Slack keeps plain "Griffin" in places |
| Griffin funds | "II, L.P." and "II Side Fund, L.P." are two legal holders | threads/00001194.json; threads/00003071.json |
| Griffin partner, board director | PERSON_4337, [PERSON_NAME_1999], [PERSON_NAME_0509], [PERSON_NAME_1655] | #winddown idx 5 "email to [1999]" has the same text as threads/00016827.json to PERSON_4337; [0509] is "Preferred Director" and SOP "Attn:" (inference) |
| Griffin staff | PERSON_2717 (cc on board mail), PERSON_2847 VP Finance | threads/00004760.json; threads/00004046.json msg[1] quote |
| Matthew Collins | Akin, Akin Babayigit, [USERNAME_0910] | threads/00001152.json msg[4] vs msg[6]; threads/00001542.json msg[1]; f_5e80ba8a32129193f119bc; /contacts/159 |
| Segerstrale | [6550], [0090], [0089], [6201], [6407], PERSON_3336 mail, PERSON_3335 Slack | #bridge-pitch 2025-09 idx 77 ts 1757285477.378439; #founders 2023-06 idx 486; the mail link is a "-k" sign-off, threads/00004819.json msg[1] (inference) |
| Tor | person [0128]/[0129]/PERSON_5275; vehicle TOR Capital Limited; directors Rouge 2004 Limited, Vert 2004 Limited; signatories PERSON_5137, PERSON_0711; counsel PERSON_5593 (TLAS) | threads/00001092.json msg[3]; threads/00001542.json |
| Deepak | [2950], [0801], [56893]?, PERSON_1287 | #admin 2023-10 idx 282, 396; #investors 2023-06 idx 491-506; [56893] link is inference |
| Nebojsa | [0127], [0112], [6408] | #founders 2023-06 idx 486; doc title vs body of f_3ee38465decc57e61df6e5 |
| Enes family | [2927], [66357], [26149] | #founders 2023-06 idx 486; #investors idx 492-503 |
| Solsten pair | [11409], [11408], [5466], Patrick/[7500], Bastion | #founders 2023-06 idx 472, 486; 2023-08 idx 196. Which name is which is NOT resolved |
| Founders | Leonard [0357]; Robert [0174]/[0054]/[0055]/[0085]; Arthur [0152]/Blake | Consent signature blocks; promissory notes; threads/00001948.json |
| Outside counsel posing as staff | Benjamin Clark = "Dror", Rimon partner; michelle.carter = Rimon paralegal; thomas.baker = "Michael", Orrick for Griffin | Signatures in threads/00001114.json. All three carry @harmonygames.co addresses |
| founders@ group | SVC_0325_EMAIL | Google Group footer in threads/00001412.json |

Token collisions: [0054] covers two founders in threads/00001092.json msg[1]; [5466] and [2927] appear in Feb 2026 #executives (idx 214, 268) in contexts that do not fit the 2023 angels. Contacts: 170 records, only Matthew Collins is a holder outside staff (/contacts/159). The Atlas pointer /contacts/160 is Brian Foster, so it is a bad lead. Holder mail addresses seen: PERSON_4337, PERSON_5275, PERSON_1287, PERSON_3336, Matthew. None found for Enes family, Solsten pair or Nebojsa (not an exhaustive search).

## 4. Who has been told (clock Feb 14; Slack ends Feb 13 10:03 UTC)

| Party | Told | Record | Robert sees |
|---|---|---|---|
| Griffin partner PERSON_4337 | Feb 9 19:12 UTC mail; call Feb 11; resigned Feb 12 | threads/00016827.json msg[0]; #executives 2026-02 idx 387-398; threads/00016903.json | YES |
| Griffin VP Finance PERSON_2847 | cc Feb 12 | threads/00016903.json | YES |
| Segerstrale | Feb 9 | #winddown idx 9, 12, 25 YES; DM D04UC0UEN2V idx 0-13 Robert NO | Partly |
| Griffin via Standard Metrics | Submission confirmed Feb 11 00:40 UTC | threads/leonard@harmonygames.co_1856787396431935562.json | NO |
| Sherwood | Feb 9 | threads/00016832.json | YES |
| Sunset | Feb 11 | threads/00016827.json msg[1] on; threads/00016883.json | YES |
| ESG Law | Feb 11 | threads/00015129.json msg[15] | YES |
| Remaining team, contractors | Feb 11; termination letters; Carta terminations Feb 12 | #winddown idx 65-82, 198; mpdm C51ECE5102ED idx 0 Robert NO | Partly (NB-1) |

Not told per any record: Tor, Deepak, Nebojsa, Solsten pair, Enes family, Matthew Collins. Evidence: #winddown idx 197 (Feb 12 22:17 UTC) lists "Reaching out to our angels properly" as still to do; Task List f_31115ddb6ed866f2b10d60 row "Send email to investors | False" (modified Feb 10); no Feb mail to or from PERSON_5275, PERSON_1287, PERSON_3336 or Matthew in Robert's mailbox, and none after Jan 7 2026 in Leonard's by to/from token search. Feb 2026 Slack search for Matthew, [0112], [2950], [0128], Patrick, Deepak: 0 hits; scan complete. This is absence evidence only. Phone or text would leave no record, and Leonard does text Griffin (#executives idx 370). Former staff with options: no record either way. Company counsel Rimon: not checked.

## 5. Preferred terms, board, Reset Financing

Robert can read the June 2023 term sheet, not the filed charter. Source f_5e80ba8a32129193f119bc, which is pre-closing:
- Item 2 "Investment Amount: $3,000,000"; item 3 $10,000,000 post with an unallocated pool of at least 10%.
- Item 5 dividends 8%, non-cumulative, when declared. Item 6 "Redemption: None".
- Item 7 liquidation: "an amount per share equal to the Purchase Price, plus any declared but unpaid dividends". The same clause then repeats a second distribution to "Series Seed Stock" before common, so it reads like a garbled sentence. Do not grade participation from it.
- Item 9 protective provisions: consent of a majority of Series Seed needed for, among others, "(vi) the liquidation or dissolution of the Company". Griffin holds 2,746,693 of about 3,051,881, or 90.0%, so Griffin alone carries that vote.
- Board in the term sheet: CEO, one company seat, one Griffin nominee, one outside director; Griffin observer. Drag-along.
Other reachable summaries: #executives 2026-01 idx 708 (ChatGPT reading of the seed docs: broad-based weighted average, Preferred class approval for liquidation, Griffin Pro Rata Rights Letter to 33% FD). Tor: Major Investor status refused (threads/00001446.json); asks for cap table on request and no-post notices with a cc to TLAS (threads/00001356.json); the signed side letter is unreadable. Angels' pro rata: decided, content not stated (#admin 2023-09 idx 157, 165).
Stockholder approval: Leonard lists "Any stockholder approvals or creditor notice steps" as an open question (threads/00016827.json msg[0]). No answer in the record. Plan of Dissolution is to come from Sunset; paperwork due in "30-45 days" (threads/00016903.json).

Board at the clock: Leonard and Robert. Basis: Griffin director resigned Feb 12 (threads/00016903.json); Gemini notes Feb 11 say the board is Leonard's side plus Griffin (threads/00016883.json). Directors list Nov 2023: PERSON_4337, Matthew, Robert, plus Leonard (threads/00001948.json msg[0]). Robert is the Common Director (f_5cd0524f448ee58833464a; Carta notice threads/00001958.json). Matthew: on the Aug 2024 consent, absent from the Jul 21 2025 consent recipients (threads/00014725.json); last board invite Jul 16 2025 (evt_a23fe8e9d123086ed31344); "our advisor at the time" Oct 2025 (DM D05GU6L0XFH 2025-10 idx 327, Robert reach unchecked). No resignation record found. Frederick attended Oct 2025 and Jan 2026 as a guest, not a director.

Reset term sheet f_11040fe5d66821bd6951aa: Robert NO. Framework f_f09041fe1e83ead96b3d09: Robert NO. Threads/00016526.json carries one PDF attachment "short memo" to Robert in Jan 2026; its text is not searchable here and may or may not be the framework. Term sheet money terms, quoted:
- "Pre-Money Valuation: $2,250,000 (fully diluted, including the post-money 10% option pool, and after the Recapitalization)"
- "Financing Amount: up to $250,000 total, includes $50,000 founders"; "Post-Money (at $250,000): $2,500,000"
- "founders (lead): $50,000 total ($16,666.67 each, or reallocated among founders)"; "All other investors: $200,000 total"
- "1 share of new Common for each 40 shares of existing Series Seed Preferred (40:1 washout)"; 10-for-1 split after
- Series R: "Liquidation preference: 1x non-participating"; "Price per share: $2,250,000 / 68,358,240 = $0.0329148322"
- Exhibit A "Founder common: 6,000,000", "Series Seed Preferred (all non-founder investors): 3,051,879", "Options outstanding: 268,772", Griffin 2,746,693.
Framework repeats $2.25M pre, up to $250K incl. $50K founders, $2.5M post, 80/10/10 with 2% founders and 8% others. It never closed; the Feb 9 outreach says "preferred stock from a seed round (no SAFEs)" (threads/00016832.json msg[0]).

## 6. Griffin quarterly metrics requests

All in Leonard's mailbox, sender SVC_0254 (Standard Metrics). Robert CANNOT read any (mailbox rule; no Robert copy in threads/000[01]*). 33 such mails by my count, Nov 15 2023 to Feb 11 2026.
- Jan 27 2026 00:58 UTC: threads/leonard@harmonygames.co_1855429523880965666.json
- Feb 3 2026 15:00 UTC reminder: threads/leonard@harmonygames.co_1856116678494354384.json
- Feb 11 2026 00:40 UTC thank-you: threads/leonard@harmonygames.co_1856787396431935562.json
Fields requested: UNKNOWN. These records have an empty body and no attachments; only subject and headers survive. The only field hint is "Investor report ... 20/20" in threads/00004046.json (Mar 2024), which Robert can read. Trello card 770 "Griffin Standard metrics submission" (Done Aug 7 2025) is unscoped.

## 7. Coherence hazards; keep these out of graded answers

1. Series Seed count: 3,051,882 (threads/00001152.json, f_d690045a2f2bf47108ae99) vs 3,051,881 (#executives idx 727) vs 3,051,879 (term sheet). Any exact total needs all three accepted.
2. Price: "$1.0173" in threads/00001152.json msg[2] is wrong; "$1.3107" in msg[0] is the wrong draft; true $0.9830.
3. Founders "4,500,000" in msg[0] is a retracted error. Outline schedule f_f2054f1311fb4146353037 has stale 2,250,000 and 750,000.
4. Reserve: 1,017,294 vs 1,121,058 (pool plus advisors); FD 10,172,940 vs 10,172,939.
5. Griffin dollars: SOP vs wires differ by a cent each; ledger books one $2,700,000 row while mail shows two wires. Term sheet says $3,000,000 from Griffin.
6. Wire dates and months: ledger Aug 7, 9, 11, 14, Sep 21, Oct 5, Oct 19 (Sep 50,000; Oct 50,000 incl. odd 25,600 and 24,400) vs P&L Sep 75,000, Oct 25,000 vs Slack Matthew Sep 13, Enes Aug 18, Tor not arrived Sep 23, Deepak Oct 17. Do not grade wire date. "Closed Jul-Aug 2023" in the brief is also incomplete: first close Jul 21, last money Oct 17, set sent Oct 31.
7. Ledger counterparty is only "Seed round - angel"; the "8 entries" comment is not 8 holders.
8. Option totals do not reconcile: 334,284 vs 268,772; Leonard's "retain 5.8%" (threads/00008065.json) does not match pool arithmetic.
9. Consents say "incentive stock option" in text, NSO in Exhibit A. Strike $0.14 vs $0.16.
10. Q2 24 consent values are destroyed by [CREDIT_CARD_NUMBER_0548].
11. Claire 3,866 vs 7,630.
12. Mail says Series Seed doc and Cap Table sheet were shared to Robert (threads/00001159.json, 00001360.json), but no such share is in the Drive export.
13. Carta "terminations are done" (idx 198) concerns holders; Carta the subscription stays until 8/15 (idx 182, 187). Do not merge them.
14. Slack finance posts idx 708-732 are pasted ChatGPT output, not records.
15. NB-1 #winddown after Feb 11; NB-2/3/4 cash and Feb payments, so no residual-to-investors figure; NB-6; NB-12 tokens; NB-15 contractor or employee; NB-20; NB-29 Feb 9 vs 10; NB-31 DM member lists.
16. Do not grade: exercised shares, vested amounts at termination, final angel $ for Segerstrale and Enes family, Matthew's exit date, any distribution per holder.

## 8. Natural per-record volume

Honest reads per holder, base data: Griffin funds 4-6; each angel 3-5 (commitment post, signing post, wire post, mail or advisor doc); founders 2; option holders 2-3 where a doc exists. Roughly 28 holders x 3 = 80-110 reads, plus 10-15 for terms and status. But keyword search collapses this: 5-6 Slack month reads cover all angels, so a strong solver could do it in 40-50. One write per holder adds about 28. A 130-call run needs per-holder writes, not per-holder reads.

## 9. Robert's own investor and cap table work

- 2023-04-24 Pitch Deck Talking Points, owner Robert: f_b784592c60aabc1e1bb7d0.
- 2023-06-07 #founders idx 478 on the advisor grant vs the 30% allocation.
- 2023-06-08 #investors idx 488-496, 509-510: Robert tallies angels ("Akin 25K + ... = $300K"), pastes a prospect's chat, proposes cuts. Strongest record.
- 2023-07-06 #founders idx 69 "Remainder angels at 3%, they put in 300K".
- 2023-07-20 #founders idx 914 "Signed"; threads/00001200.json signature packet.
- 2023-08-11 #admin idx 574. 2023-09-27 #founders idx 1343 on sharing the cap table. 2023-10-02 #founders idx 10 "looking for that cap table again".
- 2023-11-09/10 Carta board director add and first consent: threads/00001958.json, 00001961.json; threads/00001948.json msg[2] "Finished!".
- 2024-08-28, 2025-07-14 409A consents: threads/00006398.json, 00014657.json.
- 2025-09 #bridge-pitch: 112 Robert posts of 420 (21 in Jul, 4 in Aug, 0 in Oct); idx 39 "Let's sync tomorrow and rehearse?". Many are chatter.
- 2026-01-14 #executives idx 697-700, 741; 2026-01-22 idx 1205 on Griffin and angels. 2026-02-03 idx 26 team-message draft naming angels.
- 2026-02-11 Robert is cc on the counsel, Sunset and Griffin threads. He is on all Feb investor mail, but sends none of it.
I ran no dedicated search for Robert editing investor updates or deck text, so absence is not established there. In the records read, Leonard runs Carta, the metrics and all holder mail.

## Coverage limits
Gmail attachments were not opened (hg.py excludes blobs): the SPA and certificate in 00001194, closing checklist 00001195, Carta xlsx in 00003071, memo in 00016526. Whether a solver can read them is unverified, and they could change Section 1 and 5 (00003071 xlsx may be a true holder list). Game Investor List 25 f_48247af79428823c3cac92 is Robert YES but was not opened; it is a pipeline list. Robert's mailbox subject and body searches all reported scan_complete under their limits. Evals/ reads: SEARCH.md only.
