# 08 OE Check: leonard_stockholder_closeout
Checked 2026-11-09 · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · Events 99 · Characters 47461 (300 to 50,000: ok) · Ledger 2026-11-09 · release task-quality-v1 · sha256 0ac36b4fd15a
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Five blind reviewers (A, B, C on the first draft; D and E on revised text) and the platform /oe report (FAIL 2 on sha 1cd0f8a2e6c0) are answered below, with what was done for each; events keep their numbers. The last pass of edits (the E findings) had no further blind review. The second platform /oe (NON-FAIL 3 on sha 0aca513e26e1) raised one MINOR, on OE 21, fixed with the report's own text.

## Inventory
| Segment (quoted start) | Role | Event |
|---|---|---|
| "Find the holder project in Linear (search the projects for "" | STEP (read) | OE 1 |
| "List the issues in the Holder records project in Linear (pro" | STEP (read) | OE 2 |
| "Read the comments on each of the 26 issues in Linear (one ca" | STEP (read) | OE 3 |
| "Find Leonard's close-out notes in Drive and read the doc (se" | STEP (read) | OE 4 |
| "List the close-out folder in Drive (the folder that holds th" | STEP (read) | OE 5 |
| "Read the draft holder sheet in Sheets ("Holder list (draft)"" | STEP (read) | OE 6 |
| "Read the update outline in Slides ("Harmony Games February 2" | STEP (read) | OE 7 |
| "Read #winddown in Slack for Leonard's investor email draft a" | STEP (read) | OE 8 |
| "Read the replies under Leonard's list in #winddown in Slack " | STEP (read) | OE 9 |
| "Read what Sunset asked for in Gmail (search "Sunset stockhol" | STEP (read) | OE 10 |
| "Read KPMG's audit request thread in Gmail (search "Audit Req" | STEP (read) | OE 11 |
| "Read Carta's termination notices in Gmail (search "has been " | STEP (read) | OE 12 |
| "Tie the ES-15 name to ENG-2460 in Gmail (search the address " | STEP (read) | OE 13 |
| "Read Calvin Price's forward in Gmail (search the mailbox for" | STEP (read) | OE 14 |
| "Search Gmail and Leonard's Slack DMs for what the founders s" | STEP (read) | OE 15 |
| "Read the thread of the letter to PERSON_3140_EMAIL in Gmail " | STEP (read) | OE 16 |
| "Find any question a holder asked about their holding that no" | STEP (read) | OE 17 |
| "Find the option grants the notices skip in Gmail (search "ES" | STEP (read) | OE 18 |
| "Find and read the Slack DM with the ENG-2440 holder (search " | STEP (read) | OE 19 |
| "Find the size of each of the four grants in Gmail (search "1" | STEP (read) | OE 20 |
| "Work out how the four grants vest. Open the board consent at" | STEP (read) | OE 21 |
| "Find the share ledger figures in Docs (search "ledger"; the " | STEP (read) | OE 22 |
| "Check whether the reset in OE 22 closed, in Gmail (search "r" | STEP (read) | OE 23 |
| "Find how Griffin's two funds split their shares in Gmail (se" | STEP (read) | OE 24 |
| "Read the Board position thread in Gmail (search "Board posit" | STEP (read) | OE 25 |
| "Find who votes on a dissolution in Docs (search "dissolve"; " | STEP (read) | OE 26 |
| "Search Gmail for what the founders sent Griffin's partner si" | STEP (read) | OE 27 |
| "Search Gmail for what the founders sent the ENG-2446 holder " | STEP (read) | OE 28 |
| "Search Leonard's sent Gmail since Feb 1 2026 for the closing" | STEP (read) | OE 29 |
| "Tie Akin to the ENG-2447 holder in Gmail (search "and Akin")" | STEP (read) | OE 30 |
| "Find who handles the family lines in Gmail (search the addre" | STEP (read) | OE 31 |
| "Read Leonard's Slack DM with TOR Capital's partner (search S" | STEP (read) | OE 32 |
| "Search Gmail and Slack for any closing message to the other " | STEP (read) | OE 33 |
| "Work out what each stock line holds (no tool; owner-list fig" | STEP (decision, no tool) | OE 34 |
| "Work out which option lines are live at the clock, Feb 14 20" | STEP (decision, no tool) | OE 35 |
| "Work out each line's label, whether it gets a note, and its " | STEP (decision, no tool) | OE 36 |
| "Work out the board, the preferred vote and who goes first (n" | STEP (decision, no tool) | OE 37 |
| "Work out KPMG's figures as of December 31, 2025 (no tool; ru" | STEP (decision, no tool) | OE 38 |
| "Write the holder sheet into "Holder list (draft)" in Sheets " | STEP (write) | OE 39 |
| "Share the holder sheet with Robert in Drive (address from OE" | STEP (write) | OE 40 |
| "Share the holder sheet with Arthur Blake in Drive (address f" | STEP (write) | OE 41 |
| "Save the note for ENG-2441 Arthur PERSON_3083_NAME as a draf" | STEP (write) | OE 42 |
| "Save the note for ENG-2442 [PERSON_NAME_4468] as a draft in " | STEP (write) | OE 43 |
| "Save the note for ENG-2443 [PERSON_NAME_52949] as a draft in" | STEP (write) | OE 44 |
| "Save the note for ENG-2448 TOR Capital Limited as a draft in" | STEP (write) | OE 45 |
| "Save the note for ENG-2449 PERSON_1287_NAME as a draft in Gm" | STEP (write) | OE 46 |
| "Save the note for ENG-2450 [PERSON_NAME_0043] as a draft in " | STEP (write) | OE 47 |
| "Save the note for ENG-2452 Calvin Price as a draft in Gmail " | STEP (write) | OE 48 |
| "Save the note for ENG-2453 Claire Morgan as a draft in Gmail" | STEP (write) | OE 49 |
| "Save the note for ENG-2456 Marcus Bennett as a draft in Gmai" | STEP (write) | OE 50 |
| "Save the note for ENG-2457 [PERSON_NAME_0068] as a draft in " | STEP (write) | OE 51 |
| "Save the note for ENG-2458 Martin [PERSON_NAME_7250] Walsh a" | STEP (write) | OE 52 |
| "Save the note for ENG-2459 [PERSON_NAME_0051] as a draft in " | STEP (write) | OE 53 |
| "Save the note for ENG-2460 Brian Foster as a draft in Gmail " | STEP (write) | OE 54 |
| "Save the note for ENG-2463 [PERSON_NAME_0022] [PERSON_NAME_2" | STEP (write) | OE 55 |
| "Write the investor letter as a new Doc in Google Docs (from " | STEP (write) | OE 56 |
| "Move the letter into the close-out folder in Drive (folder f" | STEP (write) | OE 57 |
| "Share the letter with Robert in Drive (address from OE 25; r" | STEP (write) | OE 58 |
| "Move ENG-2438 to Done in Linear (state from OE 36)" | STEP (write) | OE 59 |
| "Comment on ENG-2438 in Linear saying why it has no note of i" | STEP (write) | OE 60 |
| "Move ENG-2439 to Done in Linear (state from OE 36)" | STEP (write) | OE 61 |
| "Comment on ENG-2439 in Linear saying why it has no note of i" | STEP (write) | OE 62 |
| "Move ENG-2440 to Done in Linear (state from OE 36)" | STEP (write) | OE 63 |
| "Comment on ENG-2440 in Linear saying why it has no note of i" | STEP (write) | OE 64 |
| "Move ENG-2441 to Todo in Linear (state from OE 36)" | STEP (write) | OE 65 |
| "Move ENG-2442 to Todo in Linear (state from OE 36)" | STEP (write) | OE 66 |
| "Move ENG-2443 to Todo in Linear (state from OE 36)" | STEP (write) | OE 67 |
| "Move ENG-2444 to Done in Linear (state from OE 36)" | STEP (write) | OE 68 |
| "Comment on ENG-2444 in Linear saying why it has no note of i" | STEP (write) | OE 69 |
| "Move ENG-2445 to Done in Linear (state from OE 36)" | STEP (write) | OE 70 |
| "Comment on ENG-2445 in Linear saying why it has no note of i" | STEP (write) | OE 71 |
| "Move ENG-2446 to Done in Linear (state from OE 36)" | STEP (write) | OE 72 |
| "Comment on ENG-2446 in Linear saying why it has no note of i" | STEP (write) | OE 73 |
| "Move ENG-2447 to Done in Linear (state from OE 36)" | STEP (write) | OE 74 |
| "Comment on ENG-2447 in Linear saying why it has no note of i" | STEP (write) | OE 75 |
| "Move ENG-2448 to Todo in Linear (state from OE 36)" | STEP (write) | OE 76 |
| "Move ENG-2449 to Todo in Linear (state from OE 36)" | STEP (write) | OE 77 |
| "Move ENG-2450 to Todo in Linear (state from OE 36)" | STEP (write) | OE 78 |
| "Move ENG-2451 to Canceled in Linear (state from OE 36)" | STEP (write) | OE 79 |
| "Comment on ENG-2451 in Linear saying why it has no note of i" | STEP (write) | OE 80 |
| "Move ENG-2452 to Todo in Linear (state from OE 36)" | STEP (write) | OE 81 |
| "Move ENG-2453 to Todo in Linear (state from OE 36)" | STEP (write) | OE 82 |
| "Move ENG-2454 to Canceled in Linear (state from OE 36)" | STEP (write) | OE 83 |
| "Comment on ENG-2454 in Linear saying why it has no note of i" | STEP (write) | OE 84 |
| "Move ENG-2455 to Canceled in Linear (state from OE 36)" | STEP (write) | OE 85 |
| "Comment on ENG-2455 in Linear saying why it has no note of i" | STEP (write) | OE 86 |
| "Move ENG-2456 to Todo in Linear (state from OE 36)" | STEP (write) | OE 87 |
| "Move ENG-2457 to Todo in Linear (state from OE 36)" | STEP (write) | OE 88 |
| "Move ENG-2458 to Todo in Linear (state from OE 36)" | STEP (write) | OE 89 |
| "Move ENG-2459 to Todo in Linear (state from OE 36)" | STEP (write) | OE 90 |
| "Move ENG-2460 to Todo in Linear (state from OE 36)" | STEP (write) | OE 91 |
| "Move ENG-2461 to Canceled in Linear (state from OE 36)" | STEP (write) | OE 92 |
| "Comment on ENG-2461 in Linear saying why it has no note of i" | STEP (write) | OE 93 |
| "Move ENG-2462 to Canceled in Linear (state from OE 36)" | STEP (write) | OE 94 |
| "Comment on ENG-2462 in Linear saying why it has no note of i" | STEP (write) | OE 95 |
| "Move ENG-2463 to Todo in Linear (state from OE 36)" | STEP (write) | OE 96 |
| "Send the confirmation to KPMG in Gmail as a reply to all: a " | STEP (write) | OE 97 |
| "Send the heads-up to Griffin's partner in Gmail, as a reply " | STEP (write) | OE 98 |
| "Reply under Leonard's list in #winddown in Slack (thread of " | STEP (write) | OE 99 |

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 | OE 1 to OE 3 | covered | ledger route |
| R2 | OE 4, OE 9 | covered | ledger route |
| R3 | OE 12 to OE 37 | covered | ledger route |
| R4 | OE 5, OE 6, OE 10, OE 39 to OE 41 | covered | ledger route |
| R5 | OE 8, OE 7, OE 56 to OE 58 | covered | ledger route |
| R6 | OE 42 to OE 55 | covered | ledger route |
| R7 | OE 59 to OE 96 | covered | ledger route |
| R8 | OE 98 | covered | ledger route |
| R9 | OE 99 | covered | ledger route |
| R10 | OE 11, OE 23, OE 38, OE 97 | covered | ledger route |
| R11 | OE 97, OE 98, OE 99 | covered | ledger route |
| R12 | OE 42 to OE 55 | covered | ledger route |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |
|---|---|---|---|---|---|
| OE 1 | "Holder records" | hg.py / SQL: SQL L136, ec2ea957-fc8e-4958-b809-0fb735b1e916 | as quoted | F1 VERIFIED: every quote cut from the project row's description | match |
| OE 2 | "Email:" | hg.py / SQL: SQL L139 to L289, ENG-2438 to ENG-2463 | as quoted | F2 VERIFIED: 26 issue rows, each title and description line asserted against the SQL | match |
| OE 3 | "Last mail with that address before Feb: May 18, 2024" | hg.py / SQL: SQL L141 to L293, ENG-2438 | as quoted | F3 VERIFIED: 52 comment rows; the 26 owner-list lines quoted | match |
| OE 4 | "Stockholder close-out notes" | hg.py / SQL: SQL L17, f_a37b403d5200d4f0a31d31 | as quoted | F4 VERIFIED: every quote cut from the document body | match |
| OE 5 | "Stockholder close-out" | hg.py / SQL: SQL L6 to L15, d_601064334a0b493022fe83, f_5ecaa967db3adcfa440b09, f_75dddccabb26eeea4842c8 | as quoted | F5 VERIFIED: the three drive rows whose parent is the folder | match |
| OE 6 | "copied from the Nov 2024 list" | hg.py / SQL: SQL L25, f_5ecaa967db3adcfa440b09 | as quoted | F6 VERIFIED: grid cut from the sheet row | match |
| OE 7 | "Harmony Games February 26 Update" | hg.py / SQL: SQL L32 to L48, f_75dddccabb26eeea4842c8 | as quoted | F7 VERIFIED: text of the five slides | match |
| OE 8 | "Hi everyone," | hg.py / SQL: C0ADGSZKR3R/1770664700.848759, C0ADGSZKR3R/1770789534.434749, C0ADGSZKR3R/1770841239.761999, C0ADGSZKR3R/1770924424.711879, C0ADGSZKR3R/1770931777.561519, C0ADGSZKR3R/1770932147.282819, C0ADGSZKR3R/1770934638.035469, C0ADGSZKR3R/1770935621.095649, messages/C0ADGSZKR3R/2026-02.json /7 /57 /81 /163 /172 /174 /197 /198 | as quoted | F8 VERIFIED: every quote re-read through hg.py | match |
| OE 9 | "One thing on the angels: one note to whoever has always handled it for a family covers the rest of the family's lines, w" | hg.py / SQL: C0ADGSZKR3R/1770949310.220519, C0ADGSZKR3R/1770949322.640149, C0ADGSZKR3R/1770949351.317729, C0ADGSZKR3R/1770949437.902269, SQL L60 to L66 | as quoted | F9 VERIFIED: four seeded replies | match |
| OE 10 | "Sunset: stockholder info for intake" | hg.py / SQL: leonard.hayes@harmonygames.co/1857034369525983506, SQL L90 | as quoted | F10 VERIFIED: every quote cut from the message | match |
| OE 11 | "GRIFFIN GAMING PARTNERS 2025 Audit Request [SOURCE_ORG_0001], Inc." | hg.py / SQL: leonard.hayes@harmonygames.co/1857029474983245439, SQL L80 to L86 | as quoted | F11 VERIFIED: every quote cut from the three messages | match |
| OE 12 | "ES-1 [PERSON_NAME_0043]: granted 30,519, vested 17,802, terminated as of Dec. 31, 2025 (ef" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960433624350836, threads/leonard@harmonygames.co_1856960433624350836.json /messages/0/body | as quoted | F12 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-2 [PERSON_NAME_0100]: granted 12,208, vested 3,052, terminated as of Aug. 1, 2024 (effe" | hg.py / SQL: leonard.hayes@harmonygames.co/1808666480668498098, threads/leonard@harmonygames.co_1808666480668498098.json /messages/0/body | as quoted | F13 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-3 Calvin Price: granted 8,138, vested 4,408, terminated as of Oct. 24, 2025 (effective " | hg.py / SQL: leonard.hayes@harmonygames.co/1847333347700620793, threads/leonard@harmonygames.co_1847333347700620793.json /messages/0/body | as quoted | F14 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-4 Claire Morgan: granted 7,630, vested 4,450, terminated as of Dec. 31, 2025 (effective" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960410709778333, threads/leonard@harmonygames.co_1856960410709778333.json /messages/0/body | as quoted | F15 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-5 [PERSON_NAME_0612]: granted 10,173, vested 5,298, terminated as of Oct. 24, 2025 (eff" | hg.py / SQL: leonard.hayes@harmonygames.co/1847333395311994879, threads/leonard@harmonygames.co_1847333395311994879.json /messages/0/body | as quoted | F16 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-6 Victor [PERSON_NAME_2770] [PERSON_NAME_0086]: granted 30,519, vested 12,716, terminat" | hg.py / SQL: leonard.hayes@harmonygames.co/1830952527208439510, threads/leonard@harmonygames.co_1830952527208439510.json /messages/0/body | as quoted | F17 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-7 Marcus Bennett: granted 22,889, vested 12,875, terminated as of Jan. 30, 2026 (effect" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960351896429942, threads/leonard@harmonygames.co_1856960351896429942.json /messages/0/body | as quoted | F18 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-12 [PERSON_NAME_0068]: granted 16,277, vested 8,477, terminated as of Jan. 30, 2026 (ef" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960504234892536, threads/leonard@harmonygames.co_1856960504234892536.json /messages/0/body | as quoted | F19 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-13 Martin [PERSON_NAME_7250] Walsh: granted 3,866, vested 2,013, terminated as of Jan. " | hg.py / SQL: leonard.hayes@harmonygames.co/1856960563574318616, threads/leonard@harmonygames.co_1856960563574318616.json /messages/0/body | as quoted | F20 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-14 [PERSON_NAME_0051]: granted 3,866, vested 1,530, terminated as of Nov. 21, 2025 (eff" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960478782792748, threads/leonard@harmonygames.co_1856960478782792748.json /messages/0/body | as quoted | F21 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-15 [PERSON_NAME_2769] [PERSON_NAME_0093]: granted 10,173, vested 3,391, terminated as o" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960532806250145, threads/leonard@harmonygames.co_1856960532806250145.json /messages/0/body | as quoted | F22 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-16 [PERSON_NAME_2768] [PERSON_NAME_0011]: granted 35,605, vested 10,384, terminated as " | hg.py / SQL: leonard.hayes@harmonygames.co/1847333318158821452, threads/leonard@harmonygames.co_1847333318158821452.json /messages/0/body | as quoted | F23 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-17 [PERSON_NAME_0038]: granted 127,162, vested 34,439, terminated as of Oct. 24, 2025 (" | hg.py / SQL: leonard.hayes@harmonygames.co/1847333272519888206, threads/leonard@harmonygames.co_1847333272519888206.json /messages/0/body | as quoted | F24 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 12 | "ES-18 [PERSON_NAME_0022] [PERSON_NAME_2767] [PERSON_NAME_2763]: granted 15,259, vested 5,4" | hg.py / SQL: leonard.hayes@harmonygames.co/1856960382677662910, threads/leonard@harmonygames.co_1856960382677662910.json /messages/0/body | as quoted | F25 VERIFIED: quoted from the notice body (Granted, Vested, as of, Last day to exercise) | match |
| OE 14 | "Fwd: Your option grant at [SOURCE_ORG_0001] Games Inc. has been updated" | hg.py / SQL: leonard.hayes@harmonygames.co/1856121753612004097, SQL L115 | as quoted | F26 VERIFIED: quoted from the seeded message | match |
| OE 15 | "The company is shutting down" | hg.py / SQL: leonard.hayes@harmonygames.co/1856858053929740799, leonard.hayes@harmonygames.co/1856860994291529096, leonard.hayes@harmonygames.co/1856861229984402233, leonard.hayes@harmonygames.co/1856861323365646598, leonard.hayes@harmonygames.co/1856861400116562076, leonard.hayes@harmonygames.co/1856861462411533365, D05SDEQEK61/1770827705.815759 | as quoted | F27 VERIFIED letters; ABSENCE evidence_check: search "terminating our independent" over all 88,728 gmail thread files, scan complete, 18 matches = 6 lette | match |
| OE 16 | "Delivery Status Notification (Failure)" | hg.py / SQL: leonard.hayes@harmonygames.co/1856860994291529096, SQL L111 | as quoted | F28 VERIFIED: quoted from the seeded message; ABSENCE evidence_check: Delivery Status mails in Leonard's 17,635 thread files, scan complete, none in Feb 2 | match |
| OE 13 | "Full Legal Name: [PERSON_NAME_2769] [PERSON_NAME_0093]" | hg.py / SQL: leonard.hayes@harmonygames.co/1782034095239486005, threads/leonard@harmonygames.co_1782034095239486005.json /messages/3/body | as quoted | F29 VERIFIED: both lines quoted from the option list | match |
| OE 17 | "Bir de equity lerimiz için birşey yapmamız gerekiyor mu prosedür olarak?" | hg.py / SQL: C51ECE5102ED/1770903714.600249, C51ECE5102ED/1770906363.694689, leonard.hayes@harmonygames.co/1847333990408253969, messages/C51ECE5102ED/2026-02.json /1 /4 | as quoted | F30 VERIFIED: quoted; ABSENCE evidence_check: all 17,635 of Leonard's thread files and 161 DMs and group DMs (86,185 messages), scan complete, no date lim | match |
| OE 18 | "for Husnu" | hg.py / SQL: leonard.hayes@harmonygames.co/1782897835407336831, leonard.hayes@harmonygames.co/1783169549554193375, SQL L119 | as quoted | F31 VERIFIED: quoted from the two digests | match |
| OE 19 | "Here is the advisor contract draft" | hg.py / SQL: D04UC0UEN2V/1770664988.379119, D04UC0UEN2V/1770669799.913739, D04UC0UEN2V/1694674255.630849, D04UC0UEN2V/1706113754.132409, D04UC0UEN2V/1693245806.221449, D04UC0UEN2V/1693246524.896449 | as quoted | F32 VERIFIED: every quote re-read through hg.py; link: the other person gives the ENG-2440 address in the DM | match |
| OE 20 | "From the disclosure schedule." | hg.py / SQL: leonard.hayes@harmonygames.co/1773160163779741845, threads/leonard@harmonygames.co_1773160163779741845.json /messages/1/body | as quoted | F33 VERIFIED: rows quoted from the message body (name, role, percent and shares on separate lines) | match |
| OE 21 | "1/24th monthly/no cliff" | hg.py / SQL: leonard.hayes@harmonygames.co/1782034095239486005, message <IA1PR15MB5917E8BDC461FB37F1D957F08AAEA@IA1PR15MB5917.namprd15.prod.outlook.com>, att_0001; db57e559500151d6b3991b62 (Contacts), SQL L133 | as quoted | F34 VERIFIED: Exhibit A quoted from the attachment as gmail_get_attachment returned it (baseline run 2, consent_nov10_2023_exhibit_a.txt); all four grants | match |
| OE 22 | "Inputs from ledger (pre-recap)" | hg.py / SQL: f_11040fe5d66821bd6951aa | as quoted | F35 VERIFIED: quoted from the document body (gdocs data.json /docs_documents/40/body_text) | match |
| OE 23 | "[SOURCE_ORG_0001]: recap option, cap table reset, and next steps" | hg.py / SQL: leonard.hayes@harmonygames.co/1855133803855213163, leonard.hayes@harmonygames.co/1856688113228112603, f_11040fe5d66821bd6951aa | as quoted | F36 VERIFIED: quoted from both mails; ABSENCE evidence_check: Slack messages/*/2026-0*.json for term sheet, financing, bridge, recap, funding (scan comple | match |
| OE 24 | "2,662,255" | hg.py / SQL: leonard.hayes@harmonygames.co/1771880236343640719, threads/leonard@harmonygames.co_1771880236343640719.json /messages/0/body | as quoted | F37 VERIFIED: quoted from the message body | match |
| OE 25 | "Board position" | hg.py / SQL: leonard.hayes@harmonygames.co/1856958794180374704, SQL L96 | as quoted | F38 VERIFIED: quoted from the two base messages and the seeded reply | match |
| OE 26 | "the holders of a majority of the outstanding shares of Preferred Stock" | hg.py / SQL: f_90c029015fc474199cf736 | as quoted | F39 VERIFIED: quoted from the document body (gdocs data.json /docs_documents/360/body_text) | match |
| OE 27 | "Combo Fighter Data and [SOURCE_ORG_0001] Shut-Down" | hg.py / SQL: leonard.hayes@harmonygames.co/1856675475513544349, threads/leonard@harmonygames.co_1856675475513544349.json /messages/13/body /messages/12/body | as quoted | F40 VERIFIED: quoted from the messages | match |
| OE 28 | "PERSON_3941_NAME (PERSON_3941_EMAIL)" | hg.py / SQL: leonard.hayes@harmonygames.co/1773963101399472184, SQL L105 | as quoted | F41 VERIFIED: quoted from the seeded message; no delivery failure (ABSENCE: Delivery Status mails over all 17,635 of Leonard's thread files, none on this  | match |
| OE 29 | "Husnu Akin (PERSON_8862_EMAIL)" | hg.py / SQL: leonard.hayes@harmonygames.co/1856961760270377901, SQL L123 | as quoted | F42 VERIFIED: quoted from the seeded message | match |
| OE 30 | "best akin" | hg.py / SQL: leonard.hayes@harmonygames.co/1776432843811839680, threads/leonard@harmonygames.co_1776432843811839680.json /messages/0/body | as quoted | F43 VERIFIED: quoted; ABSENCE evidence_check: Delivery Status mails over Leonard's 17,635 thread files, none on PERSON_8862_EMAIL | match |
| OE 31 | "Patrick Lewis" | hg.py / SQL: leonard.hayes@harmonygames.co/1770141224265557526, leonard.hayes@harmonygames.co/1774211155651873582 | as quoted | F44 VERIFIED: quoted from the two threads | match |
| OE 32 | "Short story is we are running very low on cash and seed extension type of VC deals are hard to come by without strong me" | hg.py / SQL: D09R59580EM/1762285888.654689, messages/D09R59580EM/2025-11.json /1 | as quoted | F45 VERIFIED: quoted; the DM's only month file is 2025-11, three messages read | match |
| OE 33 | "None. No message in Leonard's mailbox dated in February 2026 has any of these addresses in" | hg.py / SQL: leonard.hayes@harmonygames.co/1856675475513544349, D04UC0UEN2V/1770664988.379119, C0ADGSZKR3R/1770934638.035469 | as quoted | F46 ABSENCE evidence_check: each address in to, cc and bcc over all 17,635 of Leonard's thread files, scan complete, intersected with the 470 messages dat | match |
| OE 34 | "An owner-list figure that merges one of the four grants is the shares less the grant: 81,3" | hg.py / SQL: F3, solver/truth.json, ENG-2438 | as quoted | F47 VERIFIED by recorded calculation: each line equals the owner-list figure less its grant; the 12 lines sum to 3,051,879, the ledger figure | match |
| OE 35 | "Nine of the 14 lines with a Carta notice are live: ES-1 [PERSON_NAME_0043]: 17,802 vested," | hg.py / SQL: F12, solver/truth.json, ENG-2450 | as quoted | F48 VERIFIED by recorded calculation against the clock | match |
| OE 36 | "Nothing, state Canceled, no note: ENG-2451, ENG-2454, ENG-2455, ENG-2461, ENG-2462. Alread" | hg.py / SQL: F1, solver/truth.json, ENG-2438 | as quoted | F49 VERIFIED by recorded calculation; not_a_claim on the wording | match |
| OE 37 | "Directors in office: Leonard Hayes and Robert. Preferred vote: Griffin, whose two funds ho" | hg.py / SQL: F38, solver/truth.json, ENG-2452 | as quoted | F50 VERIFIED by recorded calculation: 2,746,693 / 3,051,879 = 90.0% | match |
| OE 38 | "A line terminated on or before Dec 31, 2025 counts what had vested; a line terminated late" | hg.py / SQL: F11, solver/truth.json, ENG-2450 | as quoted | F51 VERIFIED by recorded calculation: sixteen lines sum to 243,757 | match |
| OE 39 to OE 99 | "writes: the values on these lines are those of the decision steps" | hg.py / SQL: recomputed from F-rows; solver/truth.json; ENG-2438; C0ADGSZKR3R/1770934638.035469; leonard.hayes@harmonygames.co/1857029474983245439 | as quoted | F47 to F51: VERIFIED by recorded calculation; blind reviewer recomputed | match |

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|
| 1 | RESOLVED | minor | OE 19 (at review) | ES-10 (PERSON_1287_NAME) is 6,104 | 2.4 Expected-data / 3.2 Dependency chains | The conclusion for ES-10 and ES-11 does not follow from the doc this OE reads. Only the Matthew Collins row is identifiable; the 0.5% and both 0.1% rows carry name tokens that match none of the ES-8, ES-10 or ES-11 holder names from OE 18. ES-10 and ES-11 get  | gdocs data.json /docs_documents/262/body_text: '/ [PERSON_NAME_6201] / [PERSON_NAME_4950] / 0.5% / 30,518 shares /', '/ [PERSON_NAME_0801] / [PERSON_NAME_4950] / 0.1% / 6,104 shares /', '/ [PERSON_NAME_6408] / [PERSON_NA; the Gmail table now names each advisor and grant, ledger F33 |
| 2 | RESOLVED | minor | OE 19 (at review) | the advisor total in OE 19 | 2.3 Parameter verification / 3.2 Dependency chains (locator  | The query is the target document's own phrase and is not derived from the request or any earlier event. 'Advisor' and 'advisory' appear nowhere in the request or in OE 1 to 18; the first use in the file is this OE's own heading. The search does reach the recor | grep for 'advis' over 04_Prompt.txt and lines 1 to 53 of 08_Oracle_Events.md returns nothing before OE 19. persona_view search leonard_hayes gdocs 'advisory agreements': visible hits=1 (f_6a37227593d0977fdbdd7a, 'Due Dil; the DM moved ahead of it, so the word and the total come from OE 19, ledger F32, F33 |
| 3 | RESOLVED | minor | OE 16 (at review) | the ES-12 holder has not been told | 2.4 absence claims / 3.1 discovery coverage | The conclusion rests only on the bounce and on OE 15's Gmail search. The notes define told as any written message sent directly and delivered, and OE 25 accepts a Slack DM as told, yet no step checks Slack DMs for the ES-12 holder. The same gap covers ES-3, ES | Notes (seeded docs_documents f_a37b403d5200d4f0a31d31): 'Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn't count)'. Slack files ; OE 15 now checks Leonard's Slack DMs too, ledger F27 |
| 4 | RESOLVED | minor | OE 12 (at review) | 14 threads, one per option line | 2.3 Parameter verification (locator provenance, as set in th | The quoted query is the target mails' own subject prefix. Only the word 'termination' traces to an earlier event (OE 8, 'Carta terminations are done'), and the OE does not give that link. This is the weakest finding: the count is right and the search reaches e | Gmail subjects, for example threads/leonard@harmonygames.co_1847333347700620793.json /messages/0/subject 'Termination details for Calvin Price'. A search of Leonard's mailbox for 'Termination details' hits 14 threads, su; search is now 'has been terminated', which follows #winddown 'Carta terminations are done' and returns the 14 notices, ledger F12 |
| 5 | RESOLVED | minor | OE 33 (at review) | fully vested per OE 21 | Eval 2 section 2.4 and 3.1 (fact in expected data with no re | Sunset asks for what is vested on each option line (OE 10), but no OE establishes that the four advisor grants are vested. OE 19 gives grant sizes only, and OE 32 and OE 37 list them as plain options. The total is still right, so this cannot change the outcome | gdocs data.json /docs_documents/160/body_text (f_3ee38465decc57e61df6e5, Advisor Agreement dated July 21 2023, can-see leonard_hayes YES): 'All shares shall vest on a pro rata basis monthly over a 2-year period.' The sam; new OE 21 retrieves the vesting terms, ledger F34 |
| 6 | RESOLVED | minor | OE 33 (at review) | Nine of the 14 lines with a Carta notice are live | Eval 2 section 2.4 (count qualifiers); Minor test | The step asks which option lines are live at the clock, and the count of nine covers only the lines with a Carta termination notice. ES-8, ES-9, ES-10 and ES-11 are also live, so 13 lines are live. The same Expected line adds those four in its last sentence an | 14 'Termination details' threads in Leonard's mailbox cover ES-1 to ES-7 and ES-12 to ES-18 only; none exists for ES-8 to ES-11. Live among the 14 at 2026-02-14 00:00 UTC: ES-1, 3, 4, 7, 12, 13, 14, 15, 18 (9).; reworded in OE 35, ledger F48 |
| 7 | RESOLVED | completeness | OE 95 (at review) | no new financing came in after December 31, 2025 | Eval 2 sections 3.1, 3.2 and 2.4 (absence claim; sweep 4.0 i | KPMG item 4 asks for any new financing. OE 95 states there was none and cites only OE 32 and OE 36, which hold share and option figures. No event establishes it. OE 20 surfaces a Reset Financing Term Sheet dated Jan 22 2026 and never says whether it closed; OE | Gmail threads/leonard@harmonygames.co_1855133803855213163.json /messages/2 (Fri Jan 23 2026, Leonard to Griffin's partner): 'we see only two realistic paths', reset the cap table or shut down. threads/leonard@harmonygame; new OE 23 retrieves it and OE 97 cites it, ledger F36 |
| 8 | RESOLVED | completeness | OE 33 (at review) | so all four are fully vested at Dec 31, 2025 and at the clock | Eval 2 sections 3.1, 3.2 and 2.3A (numeric derivation; sweep | Sunset asks for 'what each holds today (for options, what's vested)'. The nine employee lines use vested figures, but the four advisor grants are counted in full with no event showing they are vested. OE 18, 19 and 25 give only grant sizes. The 164,114 total o | Gmail threads/leonard@harmonygames.co_1767980387254277674.json /messages/21/body (Thu Jun 29 2023): 'both [PERSON_NAME_6550] and Akin are happy with 0.5% each vesting over 2 years with standard advisory shares.' gdocs da; new OE 21, ledger F34; advisor rows now say vested options |
| 9 | RESOLVED | minor | OE 95 (at review) | with the To and Cc addresses set explicitly | Eval 2 sections 2.1 and 3.6 (tool capability, path feasibili | The natural route for 'a reply to all' did not produce this end state at runtime. gmail_reply_to_message with reply_all true on KPMG's latest message returned To only, with no Cc, and the catalog gives that tool no cc parameter. The Expected state is still rea | 06_PreCheck_Trajectory/trajectory-run-1.json: reply on <LV3PR19MB85246D2E9B14C7A03F5E8D12BC4A7@...> with reply_all true returned headers To PERSON_3088_EMAIL and no Cc header; the run then sent again with gmail_send_mess; OE 97 now names the route and the four recipients, ledger F11 |
| 10 | RESOLVED | minor | OE 21 (at review) | so the ES-9 holder stayed in service | 2.4 expected-data sign-off / 2.3A derivation must be stated; | The conclusion is stated as settled for the ES-9 line, but a Leonard-readable record is not addressed: the ES-9 holder (Matthew Collins / Akin, listed as 'Board member', 61,038 shares in OE 20) resigned from the board with immediate effect on May 1, 2025, befo | Gmail thread leonard.hayes@harmonygames.co/1830959847543474636 'board position w/ [SOURCE_ORG_0001]', Thu 1 May 2025 from Matthew Collins: 'I would like to resign from [SOURCE_ORG_0001]' membership with immediate effect.; OE 21 now cites the Contacts row showing the ES-9 holder stayed an advisor, ledger F34 |
| 11 | RESOLVED | minor | OE 21 (at review) | 1/24th monthly/no cliff | 2.2 persona-scoped reads / 2.4 expected-data sign-off | The records OE 21 cites do not state vesting for ES-10. The cited Doc is ES-11's agreement. The Jun 29 2023 mail names only the ES-8 holder and Akin, at a then-proposed 0.5% each ('both [PERSON_NAME_6550] and Akin'). ES-10's Doc (and ES-8's and ES-9's) are not | persona_view search leonard_hayes gdocs 'Advisor Agreement': visible hits=1 (f_3ee38465decc57e61df6e5, the [PERSON_NAME_0127] agreement), hidden by ACL=4. gdocs /docs_documents/295, /490 and /570: shared_with_emails (empty). ; superseded: OE 21 now reads Exhibit A of the board consent, which states the term for all four, ledger F34 |
| 12 | RESOLVED | minor | OE 56 (at review) | preparing the required board resolutions and documentation. | 2.4 expected data / 3.1 coverage of the stale-line rule; can | The step promises every stale line is updated but names only runway, IP and part of priorities. Two stale spans of the Feb 9 draft have no mapped replacement: 'We are initiating an orderly wind-down process and preparing the required board resolutions and docu | #winddown C0ADGSZKR3R ts 1770664700.848759 has both spans. By the clock: Sunset agreement signed (ts 1770931777.561519, Gmail 'Signed copy of 'Sunset - Dissolution Services Agreement SOW''), Sunset legal still to 'prepar; OE 56 now maps that line and the vendor clause, ledger F8 |
| 13 | RESOLVED | minor | OE 56 (at review) | is a license rather than a sale | 2.4 qualifiers on an expected value; Minor test | Dates and quotes hold, but the sentence makes both agreements 'a data licensing deal'. Only the data agreement is one; the wind-down agreement answers the 'We are initiating' line, not the IP line. 'Keeps the IP' is also a little stronger than the record: the  | ts 1770924424.711879 'instead of just selling the data we’ll do data licensing agreeement'; ts 1770925714.209079 'explicit statement to the license agreement that we own all IP'; Gmail Sunset CEO Thu Feb 12 20:00 UTC 'Ad; OE 56 separates the wind-down agreement from the data license, ledger F8 |
| 14 | RESOLVED | minor | OE 56 (at review) | Domino Delights and Zombie Match are to move off Helpshift | 2.4 cohort qualifier; Minor test | The record names two games, not 'the games' (the draft lists three), and it is an intention from Feb 10, not a completed step. Combo Fighter is not in it. | C0ADGSZKR3R ts 1770789534.434749, Leonard: 'We gotta move domino delights and zombie match off Helpshift before Feb 28th.'; names the two games and states it as still to do, ledger F8 |
| 15 | RESOLVED | minor | OE 56 (at review) | with Sunset engaged for the dissolution | 3.1 a fact with no event that establishes it; 3.2 dependency | Neither cited event ties the masked counterparty to Sunset. OE 8 quotes only '[USERNAME_26907]' and OE 10 shows only Sunset's intake request. The link sits in text no event quotes. 'Running' also sits against Leonard's Feb 12 mail quoted in OE 29. | Notes (OE 4 record) 'besides the Sunset onboarding'; list post ts 1770934638.035469 third bullet 'onboarding with [USERNAME_26907] and giving them the data'; OE 25 'We signed up with [ORGANIZATION_2601] Inc. to properly ; OE 4 and OE 8 now quote the Sunset onboarding tie, ledger F4, F8 |
| 16 | RESOLVED | minor | OE 56 (at review) | says tax papers are still to come from the wind-down | 2.4 faithful description of the source; Minor test | Slide 4 reads 'Distributions, tax papers, your options'. The step drops tax papers without saying what that part contains. I found no February record giving holders any tax-paper fact, so the section has nothing to draw on and the step should say so. | gslides el_9dabe7a0ac53 'What it means for you\nDistributions, tax papers, your options'; searches of Feb 2026 Slack and Leonard's Feb Gmail for 'tax papers' returned 0.; OE 56 covers the tax papers part of the slide, ledger F7 |
| 17 | RESOLVED | minor | OE 21 (at review) | Counted from the Nov 2023 grants | 2.4 date of an expected value; 2.5; outcome unchanged so Min | The sentence is Leonard's of Wed Jun 7 2023. Jun 29 is a later reply that only quotes it. Placed after the Jun 21 Slack post, the misdating makes it look like the 0.5% note followed 'We settled at 1%' when it came two weeks before. | threads/leonard@harmonygames.co_1767980387254277674.json /messages/50, Wed 7 Jun 2023 14:41:56 -0700, Leonard's own text; /messages/21 Thu 29 Jun 2023 18:34:18 +0000 is thomas.baker quoting it. messages/C04UTBZL6AX/2023-; superseded: the Jun 7 2023 message is no longer used; OE 21 reads Exhibit A, ledger F34 |
| 18 | RESOLVED | minor | OE 21 (at review) | the 24 monthly steps end by Nov 2025 | 2.3A/2.4 claims no more than readable records show; Minor te | True for ES-10, and the disclosure is right, but ES-9 has the same gap and the step does not say so. The only readable term naming Akin is the 0.5% note from before the 1% settlement. ES-9's own agreement (61,038, 2 years) and ES-8's and ES-10's are private wi | persona_view can-see leonard_hayes: f_3ee38465decc57e61df6e5 (ES-11) YES; f_c2c881ccc407fbdaeaa362 (61,038), f_e48755daf914ce68a899e0 (30,518), f_7982b7ac6db8b5e2b7840a (PERSON_1287_NAME) NO. /docs_documents/490 'Total N; superseded: no term is assumed now, OE 21 reads Exhibit A, ledger F34 |
| 19 | RESOLVED | unresolved | OE 21 (at review) | Open the board consent attached | 2.4 evidence limit; acl.md attachment note | The access half is right under acl.md: the consent is only a Gmail attachment and no Drive or Docs copy turned up. 'Sets all four terms' I could not confirm: the helper cannot decode the PDF, and the readable thread says only that the consent covers 'contracto | threads/leonard@harmonygames.co_1782034095239486005.json /messages/29 and /33 carry att_0001.pdf; /messages/35 quoted 'share issuances to contractors and advisors' '3. Vesting Schedule'. gdrive/gdocs 'Board Consent' retu; superseded: gmail_get_attachment returns the PDF (baseline run 2 decoded it), so OE 21 reads it, ledger F34 |
| 20 | RESOLVED | minor | OE 17 (at review) | Gmail reply of Wed Oct 29 2025 | 2.3 identifier imprecision; Minor test | Reads as a note on the Linear issue. It is a Gmail reply from the ENG-2461 holder; the Linear issue carries only the two comments in OE 3. The quote, date and Leonard's Oct 30 reply are right. | threads/leonard@harmonygames.co_1847333990408253969.json /messages/1, Wed 29 Oct 2025, 'About Carta, it says I cannot exercise online in the app'; /messages/2 Oct 30 'Ok, let me know how Carta exploration goes.'; OE 17 now says Gmail, ledger F30 |
| 21 | RESOLVED | completeness | OE missing (OE 56) (at review) | each stale line of the draft brought up to date | Eval 2 3.1 (platform /oe, FAIL 2) | No step brings the letter up to date item by item: the runway, IP, obligations and distributions/options content is left out. | plateform_reports/6aed9d01a1cb8067d8ac7dee_2_oe.md Issue 1; C0ADGSZKR3R/1770932147.282819; OE 56 now names each stale draft line and what replaces it, and OE 8 retrieves the Feb 10 to Feb 12 posts; the report's 'all termination letters' is reworded because ES-14 and ES-18 had no letter (OE 15); ledger F8, F27 |
| 22 | RESOLVED | minor | OE 17 (at review) | with no date limit | Eval 2 2.3 (platform /oe) | The search for unanswered holding questions covered only Slack, the word equity and dates since Feb 1. | plateform_reports/6aed9d01a1cb8067d8ac7dee_2_oe.md Issue 2; C51ECE5102ED/1770903714.600249; OE 17 now searches Gmail and Slack across all 26 addresses with no date limit, backed by a census; ledger F30 |
| 23 | RESOLVED | minor | OE 21 (at review) | read its Exhibit A | Eval 2 2.4 (platform /oe) | The vesting term for ES-9 and ES-10 was assumed, and ES-9 was called an advisor grant though the schedule says Board member. | plateform_reports/6aed9d01a1cb8067d8ac7dee_2_oe.md Issue 3; Evals/references/persona/acl.md; OE 21 now reads the term for all four grants from Exhibit A of the board consent (second platform /oe, report fix 1); acl.md's note that Gmail attachment reads return no bytes does not match the runs, where gmail_get_attachment returned the PDF; ledger F34 |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count, ID, channel or tool | none found; 26 issues, 52 comments, 14 notices, 26 moves, 14 drafts, 12 comments recounted by a blind reviewer |
| One missing write | none; every write in ledger section C has events |
| One Expected fact with no retrieving event | none after adding OE 21 and OE 23 |
| One unledgered Expected value or unbacked absence word | none; build_events.py refuses unquoted spans and figures, and ledger section B carries the ABSENCE checks |
| One act-vs-defer conflict | none; ledger section C defer searches found ordering only |
| One non-action or final-response event | none; decision steps state a result |
| One prompt-forbidden write or one missing recovery event | none; holder notes stay drafts; Friction: none |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| OE 97 | The pre-check's reply-all on KPMG's last message came back with no copies, so the event sets the To and Cc addresses in the thread. |
| OE 33 | Leonard cannot see founder mail he was not copied on; the absence check is bound to his view (ledger risk 5). |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 2 · resolved in review 23

## Self-review

Walked Eval 1.2, 1.3, the hard gate, 2.1 to 2.7, 3.1 to 3.6 and 4.0 in order against this report. Re-verified: every Expected value was re-read through tools/hg.py or the parsed SQL (plan/oe/verify_facts.py and the per-record asserts in plan/oe/build_events.py), and the decision steps were recomputed by a blind reviewer from the rules and records without the solver. Every quoted span and figure on an Expected line is refused by the builder unless it is in a record.

| Item | Counter-reading (best case the judgement is wrong) | Evidence that resolves it | Result |
|---|---|---|---|
| R1 | Could be read as missing or wrong: OE 2 could miss issues | F2 26 issue rows, SQL L139 to L289, counted | holds |
| R2 | Could be read as missing or wrong: the older notes could be the governing ones | F4 'These replace my earlier outreach notes.'; T10 | holds |
| R3 | Could be read as missing or wrong: angels only | F1 'live or lapsed'; F3 and F12 to F25 cover all 26 | holds |
| R4 | Could be read as missing or wrong: a new file instead of the draft, or sharing with Robert only | F4 'Finish my draft one in the folder'; F9 'the sheet goes to you as well as Robert' | holds |
| R5 | Could be read as missing or wrong: sent by mail | F4 'as a letter I can send'; the request says in the folder | holds |
| R6 | Could be read as missing or wrong: 26 notes, or a note to a Covered line | F49 14 notes; F4 and F9 | holds |
| R7 | Could be read as missing or wrong: a state without a why | F1 'say why'; 12 comment events, one per no-note issue | holds |
| R8 | Could be read as missing or wrong: reply on Robert's later mail | F4 'their own Board position mail'; T13; F38 | holds |
| R9 | Could be read as missing or wrong: a new channel post | F4 'reply under my list'; thread ts in F8 | holds |
| R10 | Could be read as missing or wrong: today's options or 268,772 | F11 as of December 31, 2025; F51; T8 | holds |
| R11 | Could be read as missing or wrong: drafts instead of sends | prompt 'Send the replies yourself' | holds |
| R12 | Could be read as missing or wrong: sending the notes | prompt 'only the holder messages wait for me'; F4 'I read and send each note myself' | holds |
| Finding 1 | Best case it still stands, or was only MINOR: The conclusion for ES-10 and ES-11 does not follow from the doc this OE reads. Only the Matthew Collins row is identifiable; the 0.5% and both 0.1% ro | Re-read through hg.py in build_events.py: the Gmail table now names each advisor and grant, ledger F33 | resolved |
| Finding 2 | Best case it still stands, or was only MINOR: The query is the target document's own phrase and is not derived from the request or any earlier event. 'Advisor' and 'advisory' appear nowhere in the | Re-read through hg.py in build_events.py: the DM moved ahead of it, so the word and the total come from OE 19, ledger F32, F33 | resolved |
| Finding 3 | Best case it still stands, or was only MINOR: The conclusion rests only on the bounce and on OE 15's Gmail search. The notes define told as any written message sent directly and delivered, and OE  | Re-read through hg.py in build_events.py: OE 15 now checks Leonard's Slack DMs too, ledger F27 | resolved |
| Finding 4 | Best case it still stands, or was only MINOR: The quoted query is the target mails' own subject prefix. Only the word 'termination' traces to an earlier event (OE 8, 'Carta terminations are done') | Re-read through hg.py in build_events.py: search is now 'has been terminated', which follows #winddown 'Carta terminations are done' and returns the 14 notices, ledger F12 | resolved |
| Finding 5 | Best case it still stands, or was only MINOR: Sunset asks for what is vested on each option line (OE 10), but no OE establishes that the four advisor grants are vested. OE 19 gives grant sizes onl | Re-read through hg.py in build_events.py: new OE 21 retrieves the vesting terms, ledger F34 | resolved |
| Finding 6 | Best case it still stands, or was only MINOR: The step asks which option lines are live at the clock, and the count of nine covers only the lines with a Carta termination notice. ES-8, ES-9, ES-10 | Re-read through hg.py in build_events.py: reworded in OE 35, ledger F48 | resolved |
| Finding 7 | Best case it still stands, or was only MINOR: KPMG item 4 asks for any new financing. OE 95 states there was none and cites only OE 32 and OE 36, which hold share and option figures. No event esta | Re-read through hg.py in build_events.py: new OE 23 retrieves it and OE 97 cites it, ledger F36 | resolved |
| Finding 8 | Best case it still stands, or was only MINOR: Sunset asks for 'what each holds today (for options, what's vested)'. The nine employee lines use vested figures, but the four advisor grants are coun | Re-read through hg.py in build_events.py: new OE 21, ledger F34; advisor rows now say vested options | resolved |
| Finding 9 | Best case it still stands, or was only MINOR: The natural route for 'a reply to all' did not produce this end state at runtime. gmail_reply_to_message with reply_all true on KPMG's latest message  | Re-read through hg.py in build_events.py: OE 97 now names the route and the four recipients, ledger F11 | resolved |
| Finding 10 | Best case it still stands, or was only MINOR: The conclusion is stated as settled for the ES-9 line, but a Leonard-readable record is not addressed: the ES-9 holder (Matthew Collins / Akin, listed | Re-read through hg.py in build_events.py: OE 21 now cites the Contacts row showing the ES-9 holder stayed an advisor, ledger F34 | resolved |
| Finding 11 | Best case it still stands, or was only MINOR: The records OE 21 cites do not state vesting for ES-10. The cited Doc is ES-11's agreement. The Jun 29 2023 mail names only the ES-8 holder and Akin,  | Re-read through hg.py in build_events.py: superseded: OE 21 now reads Exhibit A of the board consent, which states the term for all four, ledger F34 | resolved |
| Finding 12 | Best case it still stands, or was only MINOR: The step promises every stale line is updated but names only runway, IP and part of priorities. Two stale spans of the Feb 9 draft have no mapped repl | Re-read through hg.py in build_events.py: OE 56 now maps that line and the vendor clause, ledger F8 | resolved |
| Finding 13 | Best case it still stands, or was only MINOR: Dates and quotes hold, but the sentence makes both agreements 'a data licensing deal'. Only the data agreement is one; the wind-down agreement answers | Re-read through hg.py in build_events.py: OE 56 separates the wind-down agreement from the data license, ledger F8 | resolved |
| Finding 14 | Best case it still stands, or was only MINOR: The record names two games, not 'the games' (the draft lists three), and it is an intention from Feb 10, not a completed step. Combo Fighter is not in | Re-read through hg.py in build_events.py: names the two games and states it as still to do, ledger F8 | resolved |
| Finding 15 | Best case it still stands, or was only MINOR: Neither cited event ties the masked counterparty to Sunset. OE 8 quotes only '[USERNAME_26907]' and OE 10 shows only Sunset's intake request. The link | Re-read through hg.py in build_events.py: OE 4 and OE 8 now quote the Sunset onboarding tie, ledger F4, F8 | resolved |
| Finding 16 | Best case it still stands, or was only MINOR: Slide 4 reads 'Distributions, tax papers, your options'. The step drops tax papers without saying what that part contains. I found no February record  | Re-read through hg.py in build_events.py: OE 56 covers the tax papers part of the slide, ledger F7 | resolved |
| Finding 17 | Best case it still stands, or was only MINOR: The sentence is Leonard's of Wed Jun 7 2023. Jun 29 is a later reply that only quotes it. Placed after the Jun 21 Slack post, the misdating makes it l | Re-read through hg.py in build_events.py: superseded: the Jun 7 2023 message is no longer used; OE 21 reads Exhibit A, ledger F34 | resolved |
| Finding 18 | Best case it still stands, or was only MINOR: True for ES-10, and the disclosure is right, but ES-9 has the same gap and the step does not say so. The only readable term naming Akin is the 0.5% no | Re-read through hg.py in build_events.py: superseded: no term is assumed now, OE 21 reads Exhibit A, ledger F34 | resolved |
| Finding 19 | Best case it still stands, or was only MINOR: The access half is right under acl.md: the consent is only a Gmail attachment and no Drive or Docs copy turned up. 'Sets all four terms' I could not c | Re-read through hg.py in build_events.py: superseded: gmail_get_attachment returns the PDF (baseline run 2 decoded it), so OE 21 reads it, ledger F34 | resolved |
| Finding 20 | Best case it still stands, or was only MINOR: Reads as a note on the Linear issue. It is a Gmail reply from the ENG-2461 holder; the Linear issue carries only the two comments in OE 3. The quote,  | Re-read through hg.py in build_events.py: OE 17 now says Gmail, ledger F30 | resolved |
| Finding 21 | Best case it still stands, or was only MINOR: No step brings the letter up to date item by item: the runway, IP, obligations and distributions/options content is left out. | Re-read through hg.py in build_events.py: OE 56 now names each stale draft line and what replaces it, and OE 8 retrieves the Feb 10 to Feb 12 posts; the report's 'all termination letters' is reworded because ES-14 and ES-18 had no letter (OE 15); ledger F8, F27 | resolved |
| Finding 22 | Best case it still stands, or was only MINOR: The search for unanswered holding questions covered only Slack, the word equity and dates since Feb 1. | Re-read through hg.py in build_events.py: OE 17 now searches Gmail and Slack across all 26 addresses with no date limit, backed by a census; ledger F30 | resolved |
| Finding 23 | Best case it still stands, or was only MINOR: The vesting term for ES-9 and ES-10 was assumed, and ES-9 was called an advisor grant though the schedule says Board member. | Re-read through hg.py in build_events.py: OE 21 now reads the term for all four grants from Exhibit A of the board consent (second platform /oe, report fix 1); acl.md's note that Gmail attachment reads return no bytes does not match the runs, where gmail_get_attachment returned the PDF; ledger F34 | resolved |

Unresolved: none. Gate note: the prompt-check chain and readiness.evidence checks fail only because the upstream gates predate the readiness framework; no content check fails.

## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Fix the events, re-run check, then run /oe.
