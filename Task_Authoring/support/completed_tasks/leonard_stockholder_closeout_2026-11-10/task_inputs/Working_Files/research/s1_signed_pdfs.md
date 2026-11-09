# S1: Signed PDFs read for contradiction checks (Leonard stockholder close-out)

Status: COMPLETE. Facts and locators only; FACT unless marked INFERENCE or CALC. Clock 2026-02-14 00:00 UTC, normal universe. Gmail ids are Leonard-mailbox threads; [n] is the message index.
Authorized exception: direct read-only reads of the signed side letter, the signed Sunset SOW (and proposals), and the seed closing binder/set. No xlsx opened.

## A. Files: exact paths, existence, opened, text or scanned

ROOT = `Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/root/attachments/leonard.hayes@harmonygames.co/`

Correction to the brief: `attachments[].rel_path` resolves under `gmail/root/`, not `gmail/`. Rel_paths starting `gmail/dwt-takeout-export-...` do not exist on disk at all.

Text layers are partly overlaid by the anonymiser; words sit out of order at the page end. All quotes were checked against page images, except the IRA, Voting, ROFR, Secretary's Certificate, packet and Disclosure Schedule, where I used the PDFKit text extract (scratchpad only).

| Document | Thread[msg] att | Path under ROOT | Bytes | Exists | Opened | Kind |
|---|---|---|---|---|---|---|
| **Side letter, Company + Segerstrale signed** | 1777587701740700050[0] | `1777587701740700050/_089f58a39c2c4b9e9d35471efcc4b60c_docusign_net_/att_0001.pdf` | 291,508 | Yes | Yes, all 4 pp | Text |
| Same, forwarded | 1777052222643175480[7] | `1777052222643175480/_CAPBs_a46H9SCR_PBn1EP4RvCL_HO3XqOma4mTNu0WdnWv17ZuA_mail_gmail_com_/att_0001.pdf` | 291,508 | Yes | No, same size; hash differs | n/a |
| Side letter, Company signed | 1777571840372992861[0] | `1777571840372992861/_85f7058cf60a47318867f0a0ffc71e0a_docusign_net_/att_0001.pdf` | 218,514 | Yes | Yes, all | Text |
| Side letter, unsigned package copy | 1777052222643175480[14] att_0005 | `1777052222643175480/_IA1PR15MB591709BB3F588A430F597EA68AF6A_IA1PR15MB5917_namprd15_prod_outlook_com_/att_0005.pdf` | 78,330 | Yes | Yes, all | Text |
| **Dissolution Services Agreement** | 1856956483320787350[1] att_0002 | `1856956483320787350/_20260212212822_7090c4d9d601368d_email_pandadoc_net_/att_0002.pdf` | 1,008,931 | Yes | Yes, all | Text; p7 absent |
| SOW quote | same att_0003 | same folder `/att_0003.pdf` | 404,109 | Yes | Yes | Text |
| NDA | same att_0001 | same folder `/att_0001.pdf` | 499,390 | Yes | Yes | Text |
| Proposal $14,650 | 1856675475513544349[8] att_0002 | `1856675475513544349/_mlimxple_b2d7a6d7-ff6b-44f3-a512-2d6c62cf1a25_we_are_superhuman_com_/att_0002.pdf` | 86,386 | Yes | Yes | Text |
| Proposal $11,100 | [8] att_0003 | same folder `/att_0003.pdf` | 86,283 | Yes | Yes | Text |
| Sunset deck, 10 slides | [8] att_0001 | same folder `/att_0001.pdf` | 1,933,528 | Yes | Yes | Text |
| Proposal $11,720 | [6] att_0002 | `1856675475513544349/_mljl9hz3_e74044fb-5410-4ac0-a126-64768e00a9fb_we_are_superhuman_com_/att_0002.pdf` | 130,311 | Yes | Yes | Text |
| Proposal $12,363 | [5] att_0001 | `1856675475513544349/_mljuvmbl_902283ac-ab5e-4ed5-93bf-f0735896563d_we_are_superhuman_com_/att_0001.pdf` | 130,351 | Yes | Yes | Text |
| **Filed charter** | 1773160052067710033[21] att_0002 | `1773160052067710033/_DS0PR15MB5923540A514A8D65683516488A08A_DS0PR15MB5923_namprd15_prod_outlook_com_/att_0002.pdf` | 3,142,208 | Yes | Yes, all 25 pp | **Scanned** |
| Secretary's Certificate | [21] att_0001 | same folder `/att_0001.pdf` | 1,319,663 | Yes | Text extract, cert + Bylaws grep | Text |
| Capitalization table | [21] att_0003 | same folder `/att_0003.pdf` | 49,754 | Yes | Yes | Text |
| Disclosure Schedule | 1773160052067710033[14] | `1773160052067710033/_IA1PR15MB59175708E692B690D1E866B18A13A_IA1PR15MB5917_namprd15_prod_outlook_com_/att_0001.pdf` | 125,036 | Yes | Yes, text extract | Text |
| **SPA with Schedule of Purchasers** | 1773127341469801602[5] att_0001 | `1773127341469801602/_IA1PR15MB591708ED4706812858EF4A9C8A0BA_IA1PR15MB5917_namprd15_prod_outlook_com_/att_0001.pdf` | 306,924 | Yes | Yes, all 47 pp | Text |
| ROFR | [5] att_0002 | same folder `/att_0002.pdf` | 237,449 | Yes | Text extract, by section | Text |
| Voting | [5] att_0003 | same folder `/att_0003.pdf` | 256,446 | Yes | Text extract, by section | Text |
| IRA | [5] att_0004 | same folder `/att_0004.pdf` | 362,315 | Yes | Text extract, by section | Text |
| Signed Company and Key Holders packet | 1771969068173893683[0] | `1771969068173893683/_355d176be0e5464296f9a9872aa4edad_docusign_net_/att_0001.pdf` | 900,149 | Yes | Yes, text extract | Text |
| Company signature pages for Tor | 1777052222643175480[8] att_0002-5 | `1777052222643175480/_CAPBs_a7W1hkd2d44ZNEUODxwQgFVHUedvzCywTXEbPxQJw03Ow_mail_gmail_com_/att_0002.pdf` to `att_0005.pdf` | 134,495; 108,055; 109,542; 105,824 | Yes | First lines only | Text |
| Closing checklist | 1771881072932881431[1] | `1771881072932881431/_BL0PR1501MB209916FF5E99B4C9CBBBA4919939A_BL0PR1501MB2099_namprd15_prod_outlook_com_/att_0001.docx` | 33,646 | Yes | Yes | Word |

**Absent from the export:** the Closing Binder zip, the Oct 30 and Oct 31 2023 closing sets, Tor's signature counterparts (Egnyte link only), the Pro Rata and Management Rights letter bodies, SOW page 7.

**Noted, not opened (xlsx and other).** On-disk status from a path check only:

| File | Thread[msg] | Size | On disk |
|---|---|---|---|
| Carta cap table xlsx, KPMG FY23 reply | 1788910618703813283[0] att_0001 | 37,450 | No |
| Carta cap table xlsx, KPMG FY24 reply | 1817557789846606177[2] att_0001 | 43,650 | No |
| xlsx, Tor second close | 1773160052067710033[3] att_0001 | 13,238 | No |
| xlsx "Cap Table", Jul 2023 | 1770717887098657139[7], [5] | 15,349; 38,433 | Yes |
| Side letter draft docx (draft, outside the exception) | 1775602109531090463[2], [0] att_0001 | 29,560 | Yes |
| Data agreement docx, Sunset | 1856675475513544349[4], [5], [6] | about 50 KB each | Yes |
| "Small Investor Informations" docx | 1770577968081445872[2] | 79,921 | Yes |
| KPMG bank-statement PDFs, Griffin confirmation | 1788910618703813283[0], [1] | various | Some |

## B. Signed side letter

**Status: FACT unless marked.** Read from the PDF text layer and the page images. ATT = `Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/root/attachments/leonard.hayes@harmonygames.co/`.

**Which copy.** Three PDFs of the same text, all read in full:

| Copy | Thread / message | Signed by |
|---|---|---|
| Pre-signing copy in the fund-admin package, Sep 15 2023 | 1777052222643175480[14] att_0005 (78,330 B) | Nobody |
| "Side Letter TLAS(final).pdf", DocuSign, Sep 20 08:43 PT | 1777571840372992861[0] (218,514 B) = 1777052222643175480[8] att_0001 | Company only |
| "Side Letter TLAS(final) (1)", DocuSign, Sep 20 12:55 PT | **1777587701740700050[0]** (291,508 B) = 1777052222643175480[7] | **Company and Segerstrale** |

The word-for-word body is the same across the three. The last one is the operative copy in the files.

**Tor's signature is NOT on any PDF in the files.** All four Tor signature lines are blank on all three copies. Tor's signatures came by a link, "held in trust pending closing": `https://tlas.egnyte.com/fl/pIPk8OqqV5` (1777052222643175480[6], Sep 20 2023). No fully combined copy is in the export. So "signed" means Company plus Segerstrale on the record; Tor's counterpart is asserted by its counsel's mail, not seen.

**Parties.** HARMONY GAMES, Inc., a Delaware corporation; TOR Capital Limited (Don Street, JE2 4TR; signs through Rouge 2004 Limited and Vert 2004 Limited as directors); and [PERSON_NAME_6201], with a personal address block ([ADDRESS_4201], [LOCATION_1305] CB2 8EW, [LOCATION_0415]). INFERENCE: [PERSON_NAME_6201] is Segerstrale. Census C2 has this token for him, the DocuSign signature image reads as his name, and Leonard BCC'd PERSON_3336 on the signed copy (1777052222643175480[7]). He signs in his own name, with no entity ("Kris didn't use any entity", 1774541878774535160).

**Date.** "September 1, 2023". DocuSign completion Sep 20 2023.

**Effective date.** No fixed date. "The terms of this letter agreement shall become effective upon each Investor having made an investment in the Company pursuant to the Financing Documents." Tor's wire had a value date of Sep 21 2023 and had not arrived on Sep 22 (1777052222643175480[1], [2], [3]).

**Company signatory.** [PERSON_NAME_0357], title "CEO" (typed in the signature block). The DocuSign signature IMAGES on these PDFs are not anonymised and show a real name, not "Leonard Hayes". Do not quote or re-render them in any seed.

### Operative text, verbatim
Tokens are as they appear in the PDF. Bracketed elisions are mine.

> "This letter agreement is to confirm in writing an agreement made by HARMONY GAMES, Inc., a Delaware corporation (the "Company"), with each of the investors set out above (each an "Investor" and collectively the "Investors"), in connection with the Investors' conditional agreement to invest in the Company on or about the date hereof (the "Investment"), based on the Series Seed Preferred Stock Purchase Agreement, Investor's Rights Agreement (the "IRA"), Right of First Refusal and Co-Sale Agreement and Voting Agreement each by and among the Company, the Investors and the other parties thereto (such agreements, individually and collectively, and each as may be amended and restated from time to time, the "Financing Documents"). Capitalized terms not otherwise defined herein shall have the meaning set forth in the Financing Documents."

> "The terms of this letter agreement are, notwithstanding the terms of any Financing Documents or the Company's certificate of incorporation or bylaws (together, the "Constitutional Documents") or any definitive agreement entered into in connection with the Financing Documents in the Equity Financing (collectively, including the Financing Documents and the Constitutional Documents, for the avoidance of doubt, each as may be amended and restated from time to time, the "Company Documents") in furtherance and not in limitation of any similar rights or provisions of the Investor set out therein. In the event of a conflict between the terms of this letter agreement, on the one hand, and the terms of any Company Document, on the other hand, the terms of this letter agreement are intended to and shall control. The terms of this letter agreement shall become effective upon each Investor having made an investment in the Company pursuant to the Financing Documents."

> "1. Cap Table. Upon request by an Investor, the Company will promptly deliver to the requesting Investor a summary fully diluted capitalization table, with sufficient detail to enable such Investor to calculate its ownership interest in the Company on a fully diluted basis."

> "2. Notices. The Company agrees that, for purposes of sending any notices to an Investor, it shall send such notices by personal delivery, email or pre-paid reputable overnight courier to the address set forth above for the applicable Investor or at such other email or physical address or addresses as shall be specified by the applicable Investor in writing), with a copy (which shall not constitute notice) to Thompson Legal Advisory Services, P.C., Attn: [PERSON_NAME_8652], 229 [LOCATION_25304], Suite 18G, San Francisco, CA [ZIP_CODE_0001], U.S.A.; Fax: [PHONE_9954]; Email: [EMAIL_145502]. Any notice sent to an Investor via mail/post will not apply for purposes of effective delivery or receipt of such notice. Any notices sent via pre-paid reputable overnight courier, shall be deemed delivered two (2) Business Days following the sending of such notice. "Business Days" shall mean a regular business day in the jurisdiction of both the sender and the recipient of any notice."

> "3. The Right of First Offer set forth in Section 4 of the IRA shall apply to the Investors; notwithstanding the definition of Major Investor. The Investors shall also be excluded from the definition of "Competitor" as defined in Section 1.5 of the IRA."

> "4. The Company agrees that the provisions set forth in Section 5.9 (Right to Conduct Activities) of the IRA shall apply mutatis mutandis to each Investor and its Affiliates."

> "5. Miscellaneous. (a) Termination. This letter agreement shall terminate and be of no further force or effect upon the earliest to occur of with regard to each Investor, as the case may be, (i) the Investor and its Affiliates collectively no longer holding any securities of the Company or any successor to the Company, (ii) a Deemed Liquidation Event / Liquidity Event, (iii) the liquidation, dissolution, or winding-up of the Company, or (iv) mutual express agreement in writing of each of the parties hereto."

> "(b) Relation to Other Agreements. This letter agreement and the other documents referred to herein constitute the entire agreement among the parties hereto with respect to the subject matter hereof and supersede all prior oral or written agreements, if any, between the parties hereto with respect to such subject matter. [...]"

> "(c) Governing Law. [...] shall be governed by and construed in accordance with the internal laws of the State of Delaware. The substantially prevailing party in any action to enforce this letter agreement or a Company Document will be entitled to recover its (including its legal counsel's) fees and costs (including any interest) in connection with such action."

> "(d) Changes. No variation, amendment, alteration, modification of, or addition to this letter agreement will be valid or binding unless expressed in writing and signed by all parties hereto."

(e) Other (severability, counterparts, headings) and (f) Binding Obligation are boilerplate, unchanged from the draft.

| Topic | Answer from the signed text |
|---|---|
| Cap table on request | Yes, clause 1. Either Investor may ask. Goes to the **requesting** Investor. "Summary fully diluted", with enough detail to calculate its own ownership |
| Notices | Clause 2. Personal delivery, email, or pre-paid reputable overnight courier, to the address above or as later specified in writing |
| Copy to counsel | Yes, TLAS, "which shall not constitute notice". **It applies to notices to "an Investor", so Segerstrale's notices carry a TLAS copy too.** TLAS is Tor's counsel |
| Post/mail | "will not apply for purposes of effective delivery or receipt". Applies to both Investors |
| Courier timing | Deemed delivered two Business Days after sending; Business Day must be one in both jurisdictions |
| Termination | Clause 5(a), per Investor, earliest of four events. (iii) is "the liquidation, dissolution, or winding-up of the Company", so the letter stays live until that happens, then falls away |
| Pro rata | **Clause 3 is IN the signed text.** Section 4 Right of First Offer applies to both Investors "notwithstanding the definition of Major Investor". See below |
| Segerstrale | Party in his own name, an "Investor" for every clause, and a signatory. Every right in clauses 1 to 4 is his |
| Override | "shall control" over any Company Document, which includes the charter and bylaws by definition |

### The clause-3 finding
The mail chain says pro rata was to come OUT:
- Leonard, Sep 4: "we'll take out the pro rata language from the side letter" if the push fails (1775636449493308689[19]).
- Leonard, Sep 8: "let's move forward with the side letter including [PERSON_NAME_6550] but excluding pro-rata rights if possible" (1775636449493308689[17]).
- Tor, Sep 9: "Sounds good, let's go ahead as you propose" ([16]).
- Clark, Sep 14: "Only revision - ... it become effective on funding" (1775602109531090463[2]).

The signed text still carries clause 3. FACT: all three PDFs have it. INFERENCE: the Sep 14 file added effectiveness and the removal was never made; I did not open that docx because it is a draft outside the exception, so the mechanism is unproven. Section D checks what Section 4 of the IRA says.

### Differences from the Drive drafts
**The two Drive drafts are the same document.** f_6201c7027d02997bfb2c84 and f_bc574824d936285e308cff differ only in anonymisation tokens: state name vs [LOCATION_0256], "CA" vs [LOCATION_0004], "HARMONY GAMES" vs [ORGANIZATION_NAME_0351], and a signatory name vs [PERSON_NAME_6199]. Oddity: (1)'s Drive metadata says created 2023-06-29, modified 2023-07-25, before the Aug 28 draft it is a copy of. Do not date anything off it.

Signed copy against both drafts:

| # | Item | Drive draft | Signed |
|---|---|---|---|
| 1 | Date | "August __, 2023" | "September 1, 2023" |
| 2 | Addressees | TOR Capital Limited only | Adds [PERSON_NAME_6201] with address and "Email:" line |
| 3 | Defined party | "the investor set out above (the "Investor")" | "each of the investors set out above (each an "Investor" and collectively the "Investors")" |
| 4 | Recital | "the Investor's conditional agreement" | "the Investors' conditional agreement", plus new defined term (the "Investment") |
| 5 | Financing Documents parties | "the Company, the Investor and the other parties" | "the Company, the Investors and the other parties" |
| 6 | Effectiveness | No such sentence | New: "shall become effective upon each Investor having made an investment" |
| 7 | Cap Table | "deliver to the Investor"; "to enable Investor" | "deliver to the requesting Investor"; "to enable such Investor" |
| 8 | Notices | "notices to Investor"; "for Investor"; "by the Investor"; "sent to the Investor via mail/post" | "to an Investor"; "for the applicable Investor"; "by the applicable Investor"; "sent to an Investor via mail/post" |
| 9 | **Clause 3** | **Absent** | **New: Section 4 Right of First Offer applies to the Investors despite the Major Investor definition; Investors excluded from "Competitor" (IRA 1.5)** |
| 10 | Section 5.9 | Clause 3, "to Investor and its Affiliates" | Clause 4, "to each Investor and its Affiliates" |
| 11 | Miscellaneous | Clause 4 | Clause 5 |
| 12 | Termination lead-in | "earliest to occur of (i)" | "earliest to occur of with regard to each Investor, as the case may be, (i)" |
| 13 | Termination (iv) | "of the parties hereto" | "of each of the parties hereto" |
| 14 | Signature page | Company and Tor only, all blank | Adds a [PERSON_NAME_6201] block; Company and Segerstrale DocuSigned; Name and Title "CEO" filled; Tor blank; Rouge 2004 Limited is legible where one draft shows [USERNAME_15748] |

Unchanged in substance: the override paragraph, TLAS copy, mail/post rule, two Business Days, section 5.9, termination events (i) to (iii), Delaware law, fee shifting, amendments.

**Census D5 wording fix.** The Drive copy's notice rule survives into the signed text, so a run reading only the Drive draft gets Tor's route right. What the draft gets wrong is who is covered (Segerstrale), the right of first offer, and the date.

## C. Sunset SOW

**Status: FACT unless marked.** The anonymiser overlaid pieces of these pages, so quotes below are read from the page images. Token forms are kept.

**Plain answer on the fee: it is $12,363, not $11,700.** Schedule A: "Project Fee: $12,363". The one-page quote in the same signed set: "Your all-in quote $12,363 / One-time, flat fee / Bundle Discount (20%)", dated February 12, 2026.

### The signed set
Mail: pandadoc to Leonard, Feb 12 2026 21:28 UTC, "Signed copy of "Sunset - Dissolution Services Agreement SOW"", 1856956483320787350[1]. Leonard forwarded it to Robert and Arthur at [0]. Three PDFs:

| File | What it is |
|---|---|
| att_0001 | Mutual Non-Disclosure Agreement, 3 pp, Sunsets HQ Corp. and Harmony Games, Inc., 02/12/2026, New York law, both signed as CEO |
| att_0002 | Company Dissolution Services Agreement, ref 4908-6586-8865v.8, PandaDoc ref TPBRA-JHHBG-3DU9N-YAH2S. 23 pages present of 24 numbered: "Page 7 of 24" is absent. Black boxes cover part of 15.7 and the start of a force majeure clause (Accountant agreement) |
| att_0003 | One-page all-in quote. This is the scope list: Schedule A says "SOW titled below" and the list itself sits in this quote |

### Parties
- Sunsets HQ Corp. ("Sunset") and Harmony Games, Inc. (the "Company"). Sunset signs by [PERSON_NAME_27772], CEO (PERSON_0767 in mail). The Company signs by [PERSON_NAME_0357], CEO.
- Effective Date: "the date of the last signature". All dates read 02 / 12 / 2026.
- Appendix 1: Sutter Law, P.C. "Attorney-Client Fee Agreement", signed by [PERSON_NAME_52850], President. Client is the Company.
- Appendix 2: Stable Rock Services LLC "Accountant engagement Agreement", signed by [PERSON_NAME_35351], Co-Founder & Principal.

### Scope and what is included (quote, verbatim headings)
Unlimited Legal Support; Unlimited Tax Advisory; Dedicated Project Manager ("One point of contact to coordinate your entire shutdown — timelines, filings, deliverables."); Custom Shutdown Plan; **Investor + Stockholder Support ("Guidance for communicating with your board, investors, and/or employees.")**; Support in Perpetuity; **Board + Stockholder Consents ("We draft, review, and send all required approvals")**; Delaware Certificate of Dissolution ("Prepared and filed on your behalf"); Delaware Franchise Taxes ("Calculated and filed on your behalf"); Expedited Filing Fees; IRS + EIN Shutdown Filings ("We notify the IRS and cancel your EIN"); **1 Year of Federal and State income Tax Returns ("2026 return prepared and filed on your behalf")**; State Withdrawal Filings in 3 states ("File all necessary withdrawal documents in North Carolina, Oregon, and California"); Asset/IP liquidation ("Help assigning, auctioning, or disposing of your assets/IP").

### Excluded
Schedule A: "Items that do not expressly appear on the above list are not covered by the Project Fee and are out-of-scope. By way of example and not limitation, the SOW excludes services concerning dispute resolution, arbitration, court proceedings, proceedings before regulators, auction services, or debt collection services."
- Base inconsistency: the quote says "auctioning", the SOW excludes "auction services". Do not lean on either.
- 4.7: no bankruptcy services. If liabilities exceed assets and creditors will not resolve the overage, Sunset may terminate and refund 80% of Project Fees paid, less amounts due to the Accountant.
- 4.6: Sunset "will not itself provide tax or legal advice". 4.2: Legal Services "shall be rendered by Legal Counsel not" Sunset.
- Sutter's flat fee covers review only, "committing up to three hours": Board Resolutions, Shareholder Resolutions, Dissolution Plan "(as well as asset distribution to shareholders)", Dissolution Managers Agreement, Delaware taxes filings, Cert of Dissolution with Delaware, "investment documents and waterfalls". "Final State and Federal tax returns are not included; however we can help your CPA with these filings." Flat fee $1,125.00, paid by Sunset; overages run at listed hourly rates and are also paid by Sunset under the DSA.

### Deliverables, investor notices, tax, consents, timing
| Topic | What the signed set says |
|---|---|
| Investor notices | No clause says Sunset sends notices to investors. Sunset gives "Guidance for communicating". The outreach stays with the Company |
| Stockholder consents | Sunset drafts, reviews and sends Board and Stockholder approvals. Sutter reviews resolutions. Deck (1856675475513544349[8] att_0001 p4): "Consents: Drafting and executing Board and Stockholder approvals." |
| Waterfall | Deck p4: "Shareholders: Calculating the waterfall and distributing any remaining capital." Sutter reviews "investment documents and waterfalls" |
| Tax | Stable Rock via the Platform. 2026 federal and state return, franchise tax, IRS/EIN, three state withdrawals. No line for holder tax documents or K-1s |
| Timing | No dates in the SOW. Term runs "until the completion of the SOW". Deck: "Speed: Weeks". Mail 1856675475513544349[1]: intake takes "~30-60 minutes"; "Once submitted, the legal team will review all the docs, prepare your Plan of Dissolution, and you'll set up a kickoff call with legal + your dedicated customer success manager." |
| Payment | 7.3: initial invoice due on execution, invoices within 15 days, 1.5% a month late, "All invoices must be paid prior to the filing of the final dissolution documents", "The Project Fee is non-refundable." Payment-due mail 1856956473569789052. Paid state stays NB-4 |
| Notices under the DSA | 15.6: by post (effective 4 days after mailing) or email (on receipt), to each Party's contact person on the SOW |

### What the Company must supply
- Section 2: "The Company has provided (under the Parties' Mutual Non-Disclosure Agreement) or the Company will provide, on the Effective Date, the information specified in the SOW. The Company will promptly update this information as additional information becomes available or upon Sunset's reasonable request. The Company will provide such information in the form Sunset specifies or, at Sunset's request, provide Sunset with requisite access privileges to networks, subscription services, and other resources relevant to the dissolution (collectively "Company Information"). Unless otherwise specified in the SOW, the Company shall include in Company Information all necessary details concerning the Company's assets and liabilities."
- Section 5: "The Company will be responsible for the tasks identified or implicit in the SOW and Accountant engagement Letter, and as reasonably assigned by Sunset or Accountant ("Company Tasks"). The Company will perform Company Tasks in a timely manner and with requisite due diligence."
- Section 9: the Company warrants that "you have sufficient authority to direct and cause the dissolution of the Company" and that Company Information is "truthful, accurate, and complete."

### Fee ladder
| Date | Locator | Quote | Note |
|---|---|---|---|
| Feb 11 | 1856675475513544349[8] att_0002 | $14,650 | With tax work, 2 states |
| Feb 11 | [8] att_0003 | $11,100 | No tax work, 2 states |
| Feb 12, 15:12 UTC | [6] att_0002 | $11,720 | Bundle Discount (20%), with tax, 2 states. CALC: 14,650 x 0.8 = 11,720 exactly |
| Feb 12, 15:43 UTC | #winddown C0ADGSZKR3R idx 151 | "$11700" | Leonard, rounded (INFERENCE) |
| Feb 12, 19:27 UTC | #winddown idx 165 | "slightly higher" | "they also forgot to add California to the bundle" |
| Feb 12, 19:34 UTC | [5] att_0001 | $12,363 | Bundle Discount (20%), with tax, 3 states |
| Feb 12, 21:28 UTC | signed set | **$12,363** | Project Fee |

So $11,700 is a stale, rounded figure from a superseded quote. It still appears in Slack, in FINANCE_LEDGER FIN-000702 (census C3) and on card NB-4.

### What a seeded Sunset mail must not contradict
1. **Who speaks.** Legal conclusions come from Sutter Law, not Sunset (4.2, 4.6). A Sunset or customer-success voice can ask for information "in the form Sunset specifies". It cannot rule on who is a holder of record as legal advice.
2. **Direction of the list.** Sunset does not know the holders. Under Section 2 the Company supplies them. A seed must be a request or a spec for Company Information, not a list Sunset produced. "Sunset's stockholder notice list" is only safe as a form to fill in.
3. **Sequence.** Welcome and intake invite came Feb 12 22:21 UTC. Legal review, the Plan of Dissolution and the kickoff come after the intake is submitted. No base record shows it submitted. So a seed before the clock cannot cite a finished Plan of Dissolution, a held kickoff, or a Sutter review.
4. **Consents.** Sunset drafts and sends them. A seed cannot make Leonard author or send the formal stockholder consent.
5. **Fee.** $12,363, flat, one-time, non-refundable, if it is mentioned at all. Do not write $11,700, and do not say it is paid.
6. **Entity names.** Sunsets HQ Corp.; Sutter Law, P.C.; Stable Rock Services LLC. Agreement title Company Dissolution Services Agreement. Contact roles in mail: CEO PERSON_0767, Head of Partnerships PERSON_2888, CTO PERSON_3131, an unnamed customer success manager.
7. **Scope.** Three states are NC, Oregon, California. Tax is the 2026 return. No promise of holder tax documents, no dispute, auction or debt-collection work, no bankruptcy.
8. **Solvency.** Sunset's fit is "Solvent; orderly close" (deck p9). Its own template V2 says "the company is insolvent" (1856872398290956689[2]). 4.7 lets it walk if liabilities exceed assets and creditors will not settle. Stay off the word.

## D. Closing binder

**Bottom line.** The bound "Closing Binder" is NOT in the export. The closing set survives in pieces, and those pieces give the filed charter, the final text of all four agreements, and the Schedule of Purchasers. Every requested number is now known.

### What exists
| Document | Status | Locator | Executed? |
|---|---|---|---|
| Amended and Restated Certificate of Incorporation | **Filed.** Delaware file 7412761, SR 20233050795, filed 07/21/2023 10:24 AM, certified copy, 25 pp. Scanned images: only the cover has a text layer. Read from the images | 1773160052067710033[21] att_0002 = 1772042876506898182[1] = 1772039667008952550[21] att_0001 | **Yes** |
| Series Seed SPA with Exhibit A | Final text "made as of July 21, 2023". Sent Aug 2 2023 as "pdf copies of financing documents", 47 pp, signature blocks unsigned, "Second Closing: August __, 2023" | 1773127341469801602[5] att_0001 | Text final; this copy unsigned |
| IRA | "made as of July 21, 2023", 43 pp | [5] att_0004 | Text final; this copy unsigned |
| Voting Agreement | "as of July 21, 2023", 32 pp | [5] att_0003 | Text final; this copy unsigned |
| ROFR and Co-Sale | "as of July 21, 2023", 29 pp | [5] att_0002 | Text final; this copy unsigned |
| Company and Key Holders signature packet | Signature pages only, 13 pp, DocuSign: SPA, Voting, ROFR, IRA, Indemnification, Management Rights, Pro Rata Rights, Compliance Certificate, Secretary's Certificate, stockholder consent page dated 7/20/2023 | 1771969068173893683[0] | Yes, founders and Company |
| Company signature pages for Tor's closing | SPA, Voting, ROFR, IRA, one page each | 1777052222643175480[8] att_0002 to 0005 | Company side |
| Secretary's Certificate with original COI, Bylaws, consents | 23 pp | 1773160052067710033[21] att_0001 | Yes |
| Disclosure Schedule | Dated as of July 21, 2023, 11 pp | 1773160052067710033[14] att_0001 | Final form |
| Capitalization table | 1 p, Section 2.2(c) | 1773160052067710033[21] att_0003 | n/a |
| Closing checklist | 22 rows, status columns blank | 1771881072932881431[1] att_0001 (docx) | n/a |

**Not in the export.** Oct 30 2023 "Attached please find a complete set of closing documents" (1780025394687338162[5]), the Oct 31 mailing (1781310711617833275[6]), "see [..] Closing Binder" (1772969392648081004[1], 1773214172892638586[6]) and the "Closing Binder.zip" named to KPMG (1788910618703813283[0]) all have zero attachment records for those files. A scan of all 88,726 thread records finds no zip by type or extension. So no fully countersigned IRA, Voting or ROFR exists here, and no dated final Schedule of Purchasers. The Pro Rata Rights Letter and Management Rights Letter bodies are absent too; only their signature pages exist.

### Quotes
**Major Investor threshold** (IRA 1.17): "any Investor that, individually or together with such Investor's Affiliates, holds at least 1,500,000 shares of Registrable Securities".

**Protective-provision floor** (filed charter, Art. Fourth B 3.3): "At any time when at least 1,500,000 shares of Preferred Stock (subject to appropriate adjustment in the event of any stock dividend, stock split, combination, or other similar recapitalization with respect to the Preferred Stock) are outstanding, the Corporation shall not, either directly or indirectly by amendment, merger, consolidation, recapitalization, reclassification, or otherwise, do any of the following without (in addition to any other vote required by law or this Amended and Restated Certificate of Incorporation) the written consent or affirmative vote of the Requisite Holders given in writing or by vote at a meeting, consenting or voting (as the case may be) separately as a class on an as-converted to Common Stock basis:" and 3.3.5: "liquidate, dissolve or wind-up the business and affairs of the Corporation, effect any merger or consolidation or any other Deemed Liquidation Event, or consent to any of the foregoing;".

**Requisite Holders** (2.3.1): "the holders of a majority of the outstanding shares of Preferred Stock, voting together as a single class on an as-converted to Common Stock basis (the "Requisite Holders")".

**Dissolution notice** (4.10(c) and closing line): "of the voluntary or involuntary dissolution, liquidation or winding-up of the Corporation, then, and in each such case, the Corporation will send or cause to be sent to the holders of the Preferred Stock a notice specifying, as the case may be, [...] (ii) the effective date on which such reorganization, reclassification, consolidation, merger, transfer, dissolution, liquidation or winding-up is proposed to take place [...] Such notice shall be sent at least ten (10) days prior to the record date or effective date for the event specified in such notice."

**Notice form** (Fourth B 9): "shall be mailed, postage prepaid, to the post office address last shown on the records of the Corporation, or given by electronic communication in compliance with the provisions of the General Corporation Law, and shall be deemed sent upon such mailing or electronic transmission."

**Liquidation preference** (2.1): "an amount per share equal to the greater of (i) one times the applicable Original Issue Price, plus any dividends declared but unpaid thereon, or (ii) such amount per share as would have been payable had all shares of such series of Preferred Stock been converted into Common Stock pursuant to Section 4 immediately prior to such liquidation, dissolution, winding up or Deemed Liquidation Event". Shortfall: "shall share ratably in any distribution of the assets available for distribution in proportion to the respective amounts which would otherwise be payable". Original Issue Price: "$0.9830 per share".

**Also new.**
- Authorized (Fourth): "10,700,000 shares of Common Stock" and "3,051,881 shares of Preferred Stock"; "3,051,881 shares [...] hereby designated "Series Seed Preferred Stock"". SPA 2.2(a) says the same.
- Section 3.2: "For so long as at least [1,125,000] shares of Preferred Stock remain outstanding", holders of Preferred elect 1 director and Common elect 2. The square brackets are in the filed text.
- **Section 8 Waiver:** any rights of the Preferred (as a class) "may be waived (either prospectively or retrospectively) on behalf of all holders of Preferred Stock by the affirmative written consent or vote of the Requisite Holders". So Griffin can waive class rights for the angels, the 4.10 notice arguably included (INFERENCE).
- Dividends: 8%, non-cumulative, only if declared.
- Bylaws 1.7: on less than unanimous written consent "the Company shall provide prompt written notice of such action to all stockholders who did not consent".
- Stock plan (SPA 2.2(b)): 1,121,058 reserved, 103,764 committed to advisors, 1,017,294 available. Advisors (Disclosure 2.11): [6201] 30,518; Matthew Collins 61,038; [0801] 6,104; [6408] 6,104; total 103,764.
- Notes (SPA Exhibit H; Disclosure): $35,500; Leonard $15,500, Robert $13,000, Arthur $7,000.
- IRA 6.5: notice copies go to Rimon Law when to the Company, to Orrick, Herrington & Sutcliffe when "given to Stockholders". 6.5(b) and SPA 6.6(b): consent to electronic stockholder notice under DGCL 232. Signed side letter overrides for its two Investors.
- Voting 1.2 seats: (a) Griffin II designee, initially [0509]; (b) Key Holders' designee, Robert; (c) "the Company's Chief Executive Officer", Leonard; (d) a mutually acceptable independent. SPA 4.5 lists the four: Matthew Collins, [0509], Leonard Hayes, Robert. INFERENCE: Matthew held seat (d).

### Schedule of Purchasers (SPA Exhibit A)
Initial Closing: July 21, 2023. Second Closing: "August __, 2023" (blank in this Aug 2 copy).

| Purchaser as listed | Purchase price | Shares | Against the brief |
|---|---|---|---|
| Griffin Gaming Partners II, L.P. | $2,616,996.67 | 2,662,255 | Same |
| Griffin Gaming Partners II Side Fund, L.P. | $83,002.56 | 84,438 | Same |
| [PERSON_NAME_6407] (Segerstrale) | $50,000.30 | 50,865 | Same |
| TOR Capital Limited [[PERSON_NAME_50056]] | $50,000.30 | 50,865 | Same |
| [PERSON_NAME_10656] (Schaeppi, INFERENCE from address and token) | $24,999.66 | 25,432 | Same |
| [PERSON_NAME_4468] (Bergmann) | $24,999.66 | 25,432 | Same |
| [PERSON_NAME_52949] (Sadik Enes Disli) | $24,999.66 | 25,432 | Same |
| [PERSON_NAME_27652] (Eren Disli) | $24,999.66 | 25,432 | Same |
| Patrick Lewis | $24,999.66 | 25,432 | Same |
| **Golden Square I, LP** [Matthew Collins] | $24,999.66 | 25,432 | **Shares same. Holder is an LP, not the person** |
| **Investment and Production LLC** [[PERSON_NAME_0801]] | $24,999.66 | 25,432 | **Shares same. Holder is an LLC, not the person** |
| **Ike Loa LLC** ([ORGANIZATION_NAME_3202]) [[PERSON_NAME_6408]] | $24,999.66 | 25,432 | **Shares same. Holder is an LLC, not the person** |

CALC: 2,662,255 + 84,438 + 2 x 50,865 + 8 x 25,432 = **3,051,879**. No share figure differs. Purchase prices sum to $2,999,997.11.

IRA Schedule A and ROFR Schedule A carry the same entity names, so the three entities are not a slip in one document.

### Which drafts this confirms or contradicts
| Draft | Result |
|---|---|
| Charter draft f_90c029015fc474199cf736 | **Confirmed.** 2.1, Requisite Holders, 3.3.5, the 10-day notice, the notice form, 8% dividend and the 1 + 2 director split match word for word. Blanks in the draft are filled in the filed text: authorized counts, $0.9830, 1,500,000 floor, [1,125,000] |
| IRA draft f_d373f14848cf5977b5fe99 | **Confirmed.** All 287 tested sentences match. Only the date and the Major Investor blank differ |
| Voting draft f_5354a786653610abfbb5fc | **Confirmed**, 139 sentences. 1.2(a) "[______] shares" became "at least fifty percent (50%) of the shares of the Preferred Stock such Investor is purchasing"; Robert named. Drag-along unchanged |
| ROFR draft f_1873ca10847a3d3a1b398c | Substantively confirmed. 8 boilerplate sentences did not match in the text layer (notice copy, governing law, titles, counterparts, aggregation, specific performance). Overlay noise or a real change: not resolved. None touches a right used here |
| SPA draft f_966445655f653d26dc8537 | Filled: price, reserve, exhibits. Numbering moved: additional sales are 1.3, not 1.2 |
| Drive drafts saying 3,051,882 (gdocs/214, 492, 529) | **Contradicted** as to designation: filed charter and SPA say 3,051,881 |
| Side letter drafts | See B |

## E. Reach at run time; facts only in a PDF

**Can Leonard's agent read these files? No.** It can see that they exist and nothing more.
- Reach of the threads: YES by `persona_view can-see` for 1777587701740700050, 1856956483320787350, 1773160052067710033, 1773127341469801602.
- Reach of the content: NO. `Evals/references/persona/acl.md` line 38 gives Gmail "attachment names and metadata"; lines 52-56 record that Gmail attachment reads return no bytes (`no_attachment_root_configured`). `Task_Authoring/references/Ask_Carriers.md` line 122 says the same, and says Linear and Drive-family attachments do ship content.
- So a fact held only in these PDFs cannot decide an answer. It can only limit what a seed may say.

Census scope for "PDF-only": literal searches over Leonard's mail (all `leonard@` threads), gdocs and Slack, scan_complete true. Positive controls: "Major Investor" hits mail, Slack and six Drive drafts; "Ike Loa" hits mail and Slack. "12,363" also returns 0 in snowflake, gsheets, gslides, linear, trello and confluence; the "12363" hits there are id fragments. Tokenisation can hide a name from a literal search, so a zero on a name is weaker than a zero on a number.

| Fact | Only in a PDF? | Readable alternative | Needs a seeded carrier if graded? |
|---|---|---|---|
| Major Investor threshold 1,500,000 | **Yes** | Drive drafts are blank | **Yes** |
| Protective-provision floor 1,500,000 | **Yes** | Draft blank | **Yes**, or leave the floor unstated |
| Preferred Director floor [1,125,000] | **Yes** | Draft blank | Keep off the path |
| Signed side letter clause 3 (right of first offer, Competitor carve-out) | **Yes** | Mail says the opposite (pro rata excluded) | **Yes** |
| Side letter date, effectiveness sentence | **Yes** for the text | Mail: "become effective on funding" (1775602109531090463[2]) | Date yes; effectiveness no |
| Segerstrale is a party and signed | No | 1775602109531090463[4], 1777052222643175480[7] | No |
| TLAS copy and no-mail rule covers Segerstrale too | **Yes** as text | Reader can infer from "includes [..] as a party" plus Drive draft; the draft's wording says only "Investor" | **Yes**, if graded as a fact about him |
| No-mail rule and TLAS copy for Tor | No | Drive draft; 1773160052067710033[1] "no notices by mail (email is fine)... Cc to TLAS" | No |
| Cap table on request | No | Drive draft | No. Note "requesting Investor" is PDF-only |
| Termination on dissolution | No | Drive draft | No |
| Requisite Holders, 3.3.5 consent, 10-day notice, notice form, liquidation preference | No | Charter draft, word for word | No, but a reader only sees "draft" on it. A method record should say the filed text matches |
| Waiver by Requisite Holders (Fourth B 8) | No | Charter draft, same wording | No |
| Bylaws 1.7, prompt notice to non-consenting stockholders | **Yes** | gdocs 0 hits | **Yes**, if used |
| Designated 3,051,881 | Partly | #executives 2026-01 idx 727, 728 give 3,051,881 as issued, in a model reading | Do not grade |
| Holder shares per line | No | Owner list plus subtraction, C2 ties | No |
| Griffin two fund lines and prices | No | C2 sources | No |
| Golden Square I, LP as Collins's line | **Yes** | 0 hits in mail, Slack, gdocs | **Yes**, or key by SSP id and never grade it |
| Investment and Production LLC as Deepak's line | **Yes** | 0 hits | Same |
| Ike Loa LLC as Nebojsa's line | No | 1770577968081445872[1]; Slack D050GJD3X34 2023-06 idx 74 (Leonard YES, group DM) | Same rule anyway |
| Per-holder purchase price $24,999.66, $50,000.30 | **Yes** | Rounded dollars elsewhere | Do not grade |
| Sunset fee $12,363 | **Yes** | Slack "$11700", "slightly higher", "~$15K" | Keep out of scope |
| Sunsets HQ Corp., Sutter Law, Stable Rock | **Yes** | 0 hits | **Yes**, if a seed names them. A seed would be the first readable mention |
| SOW scope: consents, investor guidance, tax, 3 states | **Yes** | Mail gives only "contract and invoice", "Plan of Dissolution", "One with tax work"; California in #winddown idx 165 | **Yes**, if a rule depends on it |
| Company Information duty (Section 2) | **Yes** | Mail: "onboarding intake" | A seed can restate it as a request |
| Advisor table 103,764 | No | f_6a37227593d0977fdbdd7a | No |
| Notes $35,500 repaid | No | FIN rows | No |

**The carrier rule for design.** Any seed restating a fact marked Yes above must use the exact value given here. Seed them as text in Drive, Linear or a mail body, never as a Gmail attachment.

## F. Contradictions with 00_Pre_Scenario_Analysis.md and census_C2_holders.md

Ordered by damage. "Pre" is the analysis, "C2" the census.

### Wrong, and would cause a failed seed
1. **"Pro rata dropped" is false for the signed text.** C2 D5, C2 F.5 ("must [...] omit pro rata") and the C2 rights table ("none of the angels have pro-rata rights") all point one way. Signed clause 3 keeps the Section 4 right of first offer for Tor and Segerstrale, "notwithstanding the definition of Major Investor". The Sep 8-9 mail says it would come out; the signed PDF says it did not. A seed that omits or denies it contradicts the signed PDF. The eight $25K angel lines do lack it. It is moot in a dissolution, because no new securities are coming. Leave it off the graded path, and do not write "no angel has pro rata".
2. **The planned Major Investor seed is wrong.** Pre section 4 and C2 F.5 say seed a threshold "above 50,865 and at or below 84,438". The real figure is **1,500,000**. Seeding anything else contradicts the IRA. C2's reason also fails: at 1,500,000 the Side Fund qualifies only by aggregation with Griffin II, and every angel is far below.
3. **Pre section 4 "notice route: Tor [...]; others electronic" is too narrow.** Segerstrale is under the same clause: personal delivery, email or courier only, no post, TLAS copy. C2 says the side letter "Touches Tor only"; that is wrong. Pre section 5 SIDE gets this right, so the two sections disagree.
4. **Holder identity on three lines.** C2 rows 12, 13, 15 list persons. The Schedule of Purchasers, IRA Schedule A and ROFR Schedule A list Golden Square I, LP, Investment and Production LLC and Ike Loa LLC. Pre's fork names only Nebojsa; it now covers **three** lines. Against that, Carta says SSP-10 is "for Husnu Matthew Collins" (1777100628672295991). So the forms and Carta disagree on at least SSP-10, and the final binder that could settle it is not in the export. C2's "Name: FULL" for line 13 is overconfident. Key by SSP id and never grade the holder's legal name on these lines. Share counts are unaffected.
5. **Method record voice (Pre section 4 item 1).** "A seeded notice list from Sunset's legal or customer-success side" that "sets who counts as a record holder" runs into SOW 4.2 and 4.6: Sunset gives no legal advice and Legal Counsel is Sutter Law. Sunset also cannot own the list; Section 2 makes the Company supply it. The seed has to be a Company Information request in a stated form. Sutter has no readable footprint, and any Sutter voice before intake and kickoff breaks the sequence.
6. **Consent ask (Pre section 9, deliverables).** The SOW says Sunset will "draft, review, and send all required approvals". Leonard's write can only be a heads-up to Griffin, not the consent. As worded, "the consent ask" is safe only if it stops short of the instrument.

### Wrong or stale, lower damage
7. **C2 unreconciled gap 1 is wrong.** "3,051,882 designated vs 3,051,879 issued". The filed charter and SPA designate **3,051,881**. 3,051,882 lives in the cap table, Disclosure Schedule and Drive drafts. There are three numbers; do not grade authorized or designated shares. Pre's tie-outs are untouched: 3,051,879 is the issued sum.
8. **C2 "Tor refused Major Investor status" reads backwards.** Tor asked for it (1773160052067710033, Aug 9 2023, item 1). What I read of 1774250421965722936 does not show a refusal by Tor. The signed result: no Major Investor status, so no 3.1 information rights, but the 4.1 right of first offer and the Competitor carve-out. Fix the wording before it enters a rule.
9. **Pre's "every clause is a June 2023 draft" risk is overstated.** The filed charter and final-form IRA and Voting match the drafts on every clause used here. The risk is now smaller and narrower: only filled blanks and the side letter differ. The agent still cannot verify that, so a method record should say it. R4 and R6 hold on executed text, with R4 widened per item 3.
10. **C2 "$3,000,000" tie.** Angels are $24,999.66 and $50,000.30 on the Schedule, not $25,000 and $50,000. Schedule total $2,999,997.11, not $2,999,999.23. Wires were round (C2 sources). Keep dollars per line off the graded path, as Pre already does for wire dates.
11. **C2 section 3 "Closing set attached".** The Oct 31 2023 mail says so, but the record has no attachment. It is a claim in the body. The two "BCC" facts stand.
12. **Pre section 0 role note.** Every signed instrument gives Leonard as CEO: charter, SPA, side letter, SOW. Voting 1.2(c) names the CEO seat. The note stands; the evidence is simply stronger than "Contacts says CEO".

### New forks neither document has
13. **Is a personal note a "notice"?** Side letter clause 2 governs "any notices to an Investor". If the note to Tor or Segerstrale is a courtesy, the TLAS copy may not apply. If it is the charter 4.10 notice, it does. The CAP and SIDE rows need a closed rule.
14. **A Slack DM is not a clause 2 channel.** Segerstrale is TOLD by DM, but that is not notice under clause 2. Told state and notice state are different columns.
15. **Waiver.** Fourth B 8 lets Requisite Holders waive class rights for all holders. A rule that says every SSP line must get 10 days' notice is open to "Griffin can waive it". State it or drop the deadline.
16. **Griffin's consent is not the whole vote.** 3.3 is "in addition to any other vote required by law". CALC: Griffin 90.0% of preferred; Griffin II alone 87.2%; founders 66.3% of issued stock. INFERENCE: a general stockholder vote is separate, and the founders carry it. R6 should say only that the preferred class vote needs Griffin.
17. **Charter notice reaches Preferred only; Bylaws 1.7 reaches all non-consenting stockholders.** That includes no option holders. It helps a closed rule, but the Bylaws text is PDF-only.
18. **Deemed Liquidation Event.** C2 D10 is right for a pure dissolution. A sale of substantially all assets is a Deemed Liquidation Event (2.3.1(b)) unless Requisite Holders elect otherwise. Data or IP sales edge toward that. This is LLC take-over territory, so stay away.

### Confirmed, no change
Griffin 2,662,255 and 84,438; Tor and Segerstrale 50,865; eight lines at 25,432; 3,051,879; 103,764 advisors and the four-way split; 1,121,058 = 1,017,294 + 103,764; 10,172,940; $0.9830; notes $35,500 by founder; non-participating preference (C2 D8 settled); drag-along limited to a Sale of the Company; information rights end on a Deemed Liquidation Event, not a dissolution; Observer at 50% of purchased shares; Orrick copy; Sep 20 signing with Segerstrale.

## Not read / not done

- **Scope call for the caller to confirm.** I treated these as part of the "closing set": the Aug 2 financing documents, the Secretary's Certificate, the capitalization table, the Disclosure Schedule, the signature packet and the closing checklist. Each is a line on the closing checklist or a named lead. The unsigned side-letter copy was treated as part of the side letter. The Sunset deck came with the proposals in the same message.
- I did not open any xlsx, the side letter draft docx, the data agreements, the KPMG PDFs, or the Robert copies. The two Robert ids were leads only.
- I did not read the IRA, Voting and ROFR page by page. I extracted their text into the scratchpad and read the clauses used here, plus a sentence-level match against the drafts. That match tests chunks of each sentence, so a small mid-sentence edit could pass.
- The filed charter's clause match to the draft covers the listed clauses and the waiver sentence only, not all 25 pages.
- Tor's executed counterparts, any final dated Schedule of Purchasers, and the Griffin Pro Rata letter text are not in the export.
- I read only the opening messages of 1774250421965722936, so item F8 is limited to those.
- Extracted text is in `/private/tmp/claude-501/-Users-sumit-Source-OC/46989a83-cbdb-4145-86b5-605b4a19b678/scratchpad/s1/txt/`. Nothing was written inside `Universe_*`.
- PDF page images and some text still show real, un-anonymised names on signature pages. This file does not repeat them. Seeds must not either.
