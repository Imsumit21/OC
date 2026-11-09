# Deep Recheck P2: SQL revision 3 delta

SQL: inputs_rev3/01_Universe_Inject.sql, sha256 aeff93679c8788d45947bbeb03675e411c66feeacaf7620fce6e5fe720a61a4e.
Diff against rev2: 28 changed lines (notes doc; #executives note; the 26 ENG issues, where only the description changed). The header counts (125 INSERT, 11 UPDATE) still hold.
Each issue's created_at and updated_at are unchanged. The notes body is 2168 characters, matching its NORMAL_TEXT style-run end of 2168.

## The 26 issue emails

Every address below appears in mail Leonard can read: his own mailbox, as sender, recipient or cc.

| Issue | Holder | Email on issue | Visible source that ties the address to the person | Conflict? |
|---|---|---|---|---|
| ENG-2438/2439 | Griffin II / Side Fund | PERSON_4337_EMAIL | IRA Schedule A, both funds (gdocs /525, owned by Leonard); Board position thread; Robert's Feb 12 reply | No |
| ENG-2440 | [PERSON_NAME_0089] [PERSON_NAME_25152] (Segerstråle) | PERSON_3336_EMAIL | "From: [PERSON_NAME_0089] segerstråle <PERSON_3336_EMAIL>" (leonard@…_1761203902899782263); 18 May 2024 investor-update BCC | No. He also uses PERSON_3335 (Slack D04UC0UEN2V; May 2023 intro), which is a second address, not a contradiction |
| ENG-2441 | Arthur Schaeppi | PERSON_3063_EMAIL | Jun 29 2023 investor info "Arthur PERSON_3083_NAME … PERSON_3063_EMAIL" (…_1770053656612413311); BCC | No. PERSON_3083 is his Solsten work address |
| ENG-2442 | [PERSON_NAME_4468] | PERSON_0693_EMAIL | Signature "[PERSON_NAME_4468] … via email: PERSON_0693_EMAIL" (…_1773213846196143460); BCC; injected contact | No |
| ENG-2443 | [PERSON_NAME_52949] | PERSON_2260_EMAIL | PERSON_2260's Jun 30 2023 list "[PERSON_NAME_52949] … PERSON_2260_EMAIL 25.000 usd" (…_1770141224265557526); BCC | No |
| ENG-2444 | Patrick Lewis | patrick@harmonygames.co | The same Jun 30 2023 list "Patrick Lewis … patrick@harmonygames.co 25.000 usd"; BCC "Patrick Lewis <patrick@harmonygames.co>" | **Yes, platform token collision (see PLATFORM below)** |
| ENG-2445 | [PERSON_NAME_27652] | PERSON_2275_EMAIL | The same list "[PERSON_NAME_27652] … PERSON_2275_EMAIL"; BCC; injected contact | No |
| ENG-2446 | PERSON_3941 | PERSON_3941_EMAIL | Funds Transfer thread; advisor-agreement share; contact | No |
| ENG-2447 | Husnu Matthew Collins | matthew.collins@harmonygames.co | Nov 8 2023 list "Matthew Collins: matthew.collins@harmonygames.co" (…_1782034095239486005 [34]); his May 1 2025 resignation is sent from it | No |
| ENG-2448 | TOR Capital Limited | PERSON_5275_EMAIL | TOR's contact [PERSON_NAME_0128] (…_1768520517901907516); BCC | Correct as TOR's messaging address. **TOR's notice address differs (DR6)** |
| ENG-2449 | PERSON_1287 | PERSON_1287_EMAIL | Contact /25; BCC | No |
| ENG-2450 | [PERSON_NAME_0043] | PERSON_2361_EMAIL | [34] list; Feb 11 letter | No |
| ENG-2451 | [PERSON_NAME_0100] | PERSON_3641_EMAIL | [34] list | No |
| ENG-2452 | Calvin Price | [EMAIL_0801] | [34] list | No (calvin.price@ is his work address) |
| ENG-2453 | Claire Morgan | PERSON_2360_EMAIL | [34] list; Feb 11 letter | No |
| ENG-2454 | [PERSON_NAME_0612] | PERSON_4194_EMAIL | [34] list | No |
| ENG-2455 | Victor | victor.barnes@harmonygames.co | [34] list | No |
| ENG-2456 | Marcus Bennett | marcus.bennett@harmonygames.co | [34] list; Feb 11 letter | No |
| ENG-2457 | [PERSON_NAME_0068] | PERSON_3140_EMAIL | "[PERSON_NAME_0068]'s email address is: PERSON_3140_EMAIL" (…_1789011705438137160 [15]); Feb 11 letter | No |
| ENG-2458 | Martin Walsh | PERSON_4363_EMAIL | "Martin's email address is: PERSON_4363_EMAIL" (same [15]); Feb 11 letter | No |
| ENG-2459 | [PERSON_NAME_0051] | PERSON_2684_EMAIL | "[PERSON_NAME_0051] <PERSON_2684_EMAIL>" (…_1794611880070985008) | No |
| ENG-2460 | Brian Foster | PERSON_4243_EMAIL | Oct 18 2024 list "[PERSON_NAME_2769] [PERSON_NAME_0093] … PERSON_4243_EMAIL" ([3]); "brian <PERSON_4243_EMAIL>" on the offer letter and the Feb 11 letter | No |
| ENG-2461 | [PERSON_NAME_2768] [PERSON_NAME_0011] | cameron@harmonygames.co | [3] list; Oct 2025 notice | No |
| ENG-2462 | [PERSON_NAME_0038] | PERSON_2314_EMAIL | [3] list; Oct 2025 notice | No |
| ENG-2463 | [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763] | PERSON_1174_EMAIL | [3] list | No |

For the eight holders on the 18 May 2024 investor-update BCC, the issue email equals the BCC address in every case.

## Findings

**DR6 | P2 | §3.2 Cross-record / Semantic | FAIL (new)**
- Prompt sentence: "my close-out notes doc has how each holder gets handled". This feeds Sunset's sheet ask, "How each holder gets formal notice, including any special terms".
- Injected side:
  - Notes: "Notice route: the email on their issue. The only extra is for Tor and Segerstrale, who are both on Tor's side letter: a copy to Tor's lawyers."
  - ENG-2448: "Email: PERSON_5275_EMAIL".
  - Together these make TOR's formal notice address PERSON_5275 plus a copy to the lawyers.
- Base side:
  - TOR's own written designation (leonard.hayes@harmonygames.co/<CAMx_T-qLCuT+xT8prz_+yQyvLXa4MDkOGau7FH=8pc63aHtV=Q@mail.gmail.com>, 14 Jun 2023): "For legal notices: [EMAIL_15398]".
  - The TOR side letter (gdocs /238 and /474, owned by Leonard): notices go "to the address set forth above for Investor", and that address block reads "Attn: [EMAIL_15398]".
- The notes therefore name a different notice destination for TOR than TOR's own designation and its contract. The answer reports this destination, so the item does not qualify as low-impact. It is also a UGT fork for P1. Rev1's wording ("unless a document says otherwise") let the document win; rev3 removed that.
- Smallest fix:
  - Make the ENG-2448 description "Email: PERSON_5275_EMAIL" followed by a new line "Legal notices: [EMAIL_15398]".
  - Change the notes sentence to: "Notice route: the notice address on their issue if it has one, otherwise the email on it. The only extra is for Tor and Segerstrale, who are both on Tor's side letter: a copy to Tor's lawyers."

**PLATFORM (anonymized tokens), not scored: patrick@harmonygames.co belongs to two people**
- It is Patrick Lewis's address on ENG-2444, in PERSON_2260's 30 Jun 2023 list and in the 18 May 2024 BCC.
- It is also the sender address of Solsten's "patrick" (Co-founder//COO, the [PERSON_NAME_4468] / PERSON_0693 investor, Luxembourg address) in …_1770053656612413311 (29 Jun 2023) and …_1836075678772806708 (27 Jun 2025, the "Press Play" book).
- Base holds no other address for Patrick Lewis. His line is covered by the family note to PERSON_2260 and gets no note of its own, so the only exposure is his notice-route cell.
- Optional fix: none in data. A rubric should accept patrick@harmonygames.co.

## The two changed sentences

1. **"Messages go to the email on each holder's issue."** Fine. All 26 addresses resolve to the right person on Leonard-visible records, and the ones on the investor-update list match it.
2. **"Notice route: the email on their issue. The only extra is for Tor and Segerstrale, who are both on Tor's side letter: a copy to Tor's lawyers."**
   - "both on Tor's side letter" is supported:
     - The DocuSign notice "[PERSON_NAME_0089] Segerstråle viewed Complete with docusign: … Side Letter TLAS(final)" (…_1777587623652753593).
     - PERSON_5275 asking about "[PERSON_NAME_6550]'s signature for the side letter" (…_1777585040212920288).
   - "a copy to Tor's lawyers" matches the side letter's "with a copy … to Thompson Legal Advisory Services, P.C."
   - The notice address for TOR conflicts with base (DR6).

## The Slack note's new clause

"the owner list counts the advisor options in with the stock" is correct:
- PERSON_3941: 31,536 = 25,432 + 6,104
- PERSON_1287: 31,536 = 25,432 + 6,104
- Collins: 86,470 = 25,432 + 61,038
- Segerstråle: 81,383 = 50,865 + 30,518

The option figures come from the 10 Aug 2023 advisor schedule (…_1773160163779741845). Posting it on Jan 14, 2026, after the Nov 2024 list, is consistent with the timeline.

## Status

| DR | Status |
|---|---|
| DR1–DR4 | Closed (unchanged since rev2) |
| DR5 | Conditional (unchanged) |
| DR6 | **New FAIL: TOR's notice address** |

Proposed scores: Cross-Service Coherence FAIL (DR6); Feasibility, Persona ACL, Data Exists and Tool Use PASS.
