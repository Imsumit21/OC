# SW2 cold coherence review of seeds_for_review.md
Clock 2026-02-14 00:00 UTC, normal universe. Base read only through hg.py. Pointers are service-relative. No Working_Files, census or truth-table files read.
Verdicts: S = SUPPORTED, U = UNSUPPORTED-BUT-CONSISTENT, C = CONTRADICTED, R = supported but risky.

## Summary
Hard numbers all tie. The Chase/Carta/$4,000 story holds. No claim fails outright on a hard fact.
Eight soft contradictions need small rewording: A5, M3, L1, L4, L5, X4, plus the artefact order (T1) and the sheet label (H2). One reference does not resolve (T2, "founders' board").

## Numbers (recomputed from Robert's 132 Processed notices, parsed in memory)
- 132 notices, 131 USD + 1 BGN, Sep 5 2023 to Feb 2 2026. Leonard's mailbox holds the same 132 (same Payment References), Arthur's a 65 subset.
- By Transaction Date, USD only: DD 984,888.21, ZM 608,820.50, CF 73,685.61, total 1,667,394.32. Sheet matches to the cent.
- Plain sum of Amount with no currency filter: ZM 610,819.50, total 1,669,393.32 (Martin 1,999.00 BGN, Oct 30 2025, threads/00015809). Sheet row says "All notices", so it differs from a literal sum by 1,999.00. See H2.
- Deck rounds correctly: 985K, 609K, 74K.
- No notice falls within 5 days of Jan 8/9 2025 (nearest Jan 2, Jan 15) or on Nov 23/24 2025 (Nov 12, Dec 1), so the cut dates carry no edge case.
- Leapblock: 29 Processed = 374,654 (2023 71,578; 2024 232,726; 2025 62,950; 2026 7,400). Sep 13 2023 33,290 exists only as Awaiting Approval (threads/00001577). With it: 2023 104,868, total 407,944, 30 wires. Post ties exactly. It is the only Awaiting Approval with an amount and no Processed notice, all mailboxes.
- 22 issues = 25 bank names less 3 merges (Deel, Singular, BANCO). Ties.
- REVENUE_DAILY lifetime total_revenue_usd: domino_delights 12,331.25, zombie_match_3d 11.99, combo_fighter 11.75.

## Atomic claims and verdicts

### A. Leonard's ask (#winddown, Feb 13 01:23:41)
| # | Claim | V | Pointer / note |
|---|---|---|---|
| A1 | Leonard, Robert, Arthur in C0ADGSZKR3R | S | channels.json members |
| A2 | Angel calls are next | S | C0ADGSZKR3R/2026-02 /197 Feb 12 22:17 "Reaching out to our angels properly"; D04UC0UEN2V/2026-02 /1 |
| A3 | Tuesday = Feb 17 2026 | S | calendar arithmetic; Feb 13 is Friday |
| A4 | "bet" as Leonard's word | S | draft mail C0ADGSZKR3R/2026-02 /7 "made multiple bets"; C07C2866011/2026-02 /75 |
| A5 | "you know who worked on what better than I do" | C (soft) | Same author, 2 hours earlier, method says "Don't try to work out who was on what". Internal tension across seeds |
| A6 | doc title, sheet title | S | internal, titles match |
| A7 | "everyone the bank shows", one issue each | S | 22 ties |
| A8 | "Blake" for Arthur | S | Leonard mail Feb 12 22:56 "my CTO Blake" (threads/00016827); C04UEQVDVB7/2025-12 "Once Blake says yes"; canvas rows "(Blake)" |
| A9 | Linear still in use | S | C0ADGSZKR3R Feb 12 22:00 "linear we keep during transition" |
| A10 | Robert owns it; reply here | U | Leonard/Arthur split Feb 12 22:34 is data vs onboarding, nothing against |

### M. Method doc
| # | Claim | V | Pointer / note |
|---|---|---|---|
| M1 | replaces the quick plan on "our board" | S after T1 | needs Trello earlier than doc; see T2 |
| M2 | "ground source of truth", banks | S | C04UEQVDVB7/2025-08 Aug 6 02:01 |
| M3 | Processed notices are "the only place with a line per payment" | C (soft) | The design's own Sep 13 wire shows on an Awaiting Approval notice (00001577); QBO exists (threads/00016879 Feb 11 "balances currently reflected in QBO"). FINANCE_LEDGER is monthly by category, so it does not contradict |
| M4 | first SVB wires Sep 2023, last run Feb 2 | S | Sep 5 2023; Feb 2 2026 Deel, Leapblock, Eveline |
| M5 | Chase payments out of scope | S | Carta on 3203 |
| M6 | "left and stayed out", own accounts not spend | S | Wire returns: Apr 2024 C04UEQVDVB7 Apr 12 "bank returned our money"; May 7 2024 $125 Wire Returned |
| M7 | other payment route counts only with a receipt | S | Payoneer receipt leonard@..1798426229536387534 $126.25 |
| M8 | Build/Marketing/Company definitions | U | rule, nothing against. Ledger, Deel unaffected |
| M9 | Our own pay and Gusto excluded | S | C04UEQVDVB7/2025-06 "$1 pay for Blake..." ; Sep 2023 expenses in gusto |
| M10 | Jan 9 2025 ZM start | S | timeline row 2025-01-10; C0880U9751A first activity Jan 9 |
| M11 | Nov 24 2025 CF start | S | #prototype opens Nov 24; kickoff Nov 12 is earlier but this is a rule |
| M12 | Non-dollar stays out | S | one BGN notice |
| M13 | daily revenue table | S | ANALYTICS.MONETIZATION.REVENUE_DAILY, game_id per row. See risk NB-26 |
| M14 | close issue once line is right | U | Linear states support it |

### L. Linear notes
| # | Claim | V | Pointer / note |
|---|---|---|---|
| L0 | Project 'Payee history' Feb 12 23:12 | U | Only 2 projects in Linear (GoD - Beta, Zombie Match 3D); no name clash; no finance team, so it must sit under an existing team. Last issue created 2025-11-07; users active |
| L1 | Deel "everyone on contract ... one run a month" | C (soft) | Same project lists direct contractors; Oct 27 2023 "Marcus wanted to skip Deel"; Sep 26 2023 "not paying [Victor] and the team via Deel". 35 wires, 5 top-ups (1,873.25; 320; 254; 649; 1,505), no wire dated Apr 2024, Nov 2024, Apr 2025, Nov 2025 |
| L2 | Deel two spellings, same account | S | notices ***8380, 24 + 11 |
| L3 | Arthur: invoice month end, wire lands next month | S | #leapblock prompts; the 5 wires dated at month end all deliver next month |
| L4 | Leapblock "saga map crew first, then Martin and Victor" | C (soft) | C04UEQVDVB7/2023-09 /554 first monthly invoice: "$15K for Saga map + $3260 for Martin + $4K for [Victor]". They ran together; crew ended Jun 2024 (#leapblock Jun 14), Victor Apr 16 2025 |
| L5 | Eveline "Marcus's company" S; "fixed monthly" | C (soft) | D05UDNCCYKC/2023-10 /118 d/b/a. Amounts move 2,400, 3,000, 3,160, 3,020, 3,350, 3,330.50, 3,700, 3,720, and go down twice |
| L6 | Adjoe, incent, three wires | S | "incent" Leonard C07C2866011/2025-04 /1085; May 5, Jul 3, Aug 29 |
| L7 | MotMot by the day, bank's name | S | C04UEQVDVB7/2025-01 Jan 15 "4 extra days ... $4032"; D08SDCVRJ9W San Salvador |
| L8 | "I always just approved what Blake put in" | S | all 11 wires by Arthur, approved Leonard |
| L9 | Singular attribution tool | S | |
| L10 | Node, one payment closing account Jan 2025 | S | C04UEQVDVB7/2025-01 Jan 2 "closing our account with Node Media LLC"; 1,428.57 + 3 x 5,000 |
| L11 | TYZ, patent scare | S | C04UTBZL6AX/2024-01; thread 00002505 |
| L12 | ***7393 trademark filings | S | 4 of 4 tied to trademark posts |
| L13 | Lucas, mini games, bank from Sep 2024 | S | $2150 a month Jun 2024; C04UEQVDVB7/2024-09 /63 IBAN; 3 wires |
| L14 | AppLovin past due | S | C04UEQVDVB7/2025-11 Nov 11 "about to hit 90 days past due" |
| L15 | Graham art director for a month | S | C0880U9751A May 1 2025 "with us during May ... art direction"; D08QN2UDJCB May 22 "until the 31st" |
| L16 | JPMorgan: Leonard approved Aug 2024 | S | threads/00006272 approver Leonard; C04UEQVDVB7 Aug 19 20:49/20:56 |
| L17 | "can't remember what it was" | R | Title says JPMorgan, he closed Chase himself Oct 31 2025 and posted the zip. Not falsifiable, but "what it was" reads oddly |
| L18 | Creative X first playable | U | C04UEQVDVB7 May 15 "playable invoice"; "first" has no direct support, nothing against |
| L19 | M ***4020 the website | S | C04UEQVDVB7/2023-10 Oct 20 "invoice from JP for the website" |
| L20 | Nathan coins and chests | S | C04UEQVDVB7 Jul 25 2024 |
| L21 | Martin paid direct | S | C04UEQVDVB7 Oct 30 2025 Arthur "Martin's is ready for approval"; notice by Arthur, Leonard |
| L22 | Brooks contract Oct, $500 a month | S | docusign Oct 10 2025; Exhibit B minimum $500; 3 wires |
| L23 | Ozhan 2D animation, about a week | S/R | Robert Feb 27 2025 "about 1 week"; actual run to Mar 12. Arthur is in #art_outsourcing. Memory, keep |
| L24 | UX second half | S | C04UEQVDVB7/2023-05 "$600 after the project, $600 more if we get funded"; Oct 31 2023; agreement title ui/ux designer |
| L25 | $500 4X proposal help | S | D04TJREVBMM/2025-05 "4X Crypto Game Proposal" |
| L26 | Video editor, ad videos | S | Payoneer "Video 1 of 4"; #video_editing_oleg shared with Dixelar |

### P. Leapblock post (#leapblock, Feb 13 08:37:26)
| # | Claim | V | Pointer / note |
|---|---|---|---|
| P1 | Author in channel, not an NB-1 leaver | S | EMPLOYEE_0024 (contacts: scott, Art Studio Principal) posted Feb 12 18:50 |
| P2 | "as we said yesterday" | S | call Feb 12 18:50; winddown 18:57 |
| P3 | accountant | S | Feb 11 20:47 "our accountant" |
| P4 | Sep 13 first wire 33,290 | S | 00001577; Sep 11 2023 "4 different invoices from the past"; Sep 12 wire help; Sep 13 invoices approved. Contract Apr 2023 predates it but the wire settled the back invoices |
| P5 | year totals, 407,944, 30 wires | S | ties |
| P6 | Nothing else open | S | Feb 12 18:57 "don't worry"; the ~$600 is Leonard's optional gesture |
| P7 | timing | S | before Slack end 10:03; 10:37 Sofia, Friday |

### X. Arthur's mail (Feb 13 16:26:44)
| # | Claim | V | Pointer / note |
|---|---|---|---|
| X1 | $4,000, Aug 2024, ***3203, "was me" | S | threads/00006270 recipient created by Arthur; 00006271; 00006272 |
| X2 | 3203 is the company's Chase | S | Carta mail Jul 16 2024: renewal Aug 15 2024, "Bank account ending in 3203" (leonard@..1804729872424032900); Jul/Aug 2025 same; Feb 12 21:48 "tied to our Chase account" |
| X3 | Carta renewal came out of Chase, money put back after | S/U | Aug 15 renewal precedes Aug 19 wire; canvas row "Carta (renewal 8/15 and tied to Chase account". The reason itself is stated nowhere; nothing against. No Carta amount in the base. Aug 7 EDD $4,122.74 is unrelated (paid via SVB details) |
| X4 | "that's our own Chase account" | C (soft) | Closed: C04UEQVDVB7 Oct 31 2025 "Chase account closed"; Feb 12 "which is closed" |
| X5 | "pulling the Chase statements" | R | Leonard already posted Chase_HarmonyGames_Alllstatements_2023-2025.zip, C04UEQVDVB7 Nov 1 2025; Arthur is a member. Reads like a live login to a closed account |
| X6 | for Sunset's file | S | Feb 12 22:34 Arthur takes data stuff |

### H/D. Sheet and deck
| # | Claim | V | Pointer / note |
|---|---|---|---|
| H1 | Figures | S | ties (USD) |
| H2 | Row label "All notices, by date" | C (soft) | ZM excludes the BGN notice; quantitative class always fails, so label it |
| H3 | Timestamps | see T1 | |
| D1 | Deck rounding | S | |
| D2 | Three games | S | draft mail "We built and tested three games" |

### T. Trello, calendar, contact
| # | Claim | V | Pointer / note |
|---|---|---|---|
| T1 | Order: deck 19:21, sheet 19:48, Trello 20:14 | C (soft) | Deck quotes numbers rounded from a sheet dated 27 min later; the plan to use the P&L is dated after both and is not how those numbers were made. 19:21 is inside the Sunset CEO call (19:09 "gonna hop on a call", 19:26 "talked to"). Leonard names angels as next only at 22:17, and says "I looked at the P&L" at 22:06 |
| T2 | "founders' board" | C (ref) | 5 boards, none so named. Harmony Games board (640643a3...) is the fit: all its 2024-25 actions are Leonard's |
| T3 | Leonard writes a card Feb 12 | S/R | 228 actions in 2025, last Nov 12; Trello live Feb 12 00:52 "Trello is done" is the Sunset connector, not a cancellation. T06: set card and board dateLastActivity |
| T4 | Calendar hold | U | No wind-down conflict. Google archive is "unused accounts". Stale open rrules (e.g. Design Meeting Weekly Tue 18:00) overlap harmlessly |
| T5 | Lauren contact | S | Exhibit A Telegram distribution; C05KNDCHAAG Oct 2025 intro. No existing contact row; not on PAYROLL_ROSTER, so NB-15 not touched |

## Known issue cards touched
- NB-2: Trello plan points to the P&L sheet, no value stated. OK as a superseded decoy; never grade a P&L figure.
- NB-12: 7 titles are tokens and tokens differ by mailbox ([PERSON_NAME_7200] vs [ORG_NAME_3801] on ***7393). Key every row on account last 4.
- NB-23: use notices (25,000; 6,250), not the invoice.
- NB-24: seeds add the first Linear comments in the export; fine, must be real comment rows.
- NB-26: CF 11.75 is a warehouse total; "as recorded" covers it. Do not phrase any row as "CF sold".
- NB-1, NB-6: both Slack seeds are inside the limits.
- Pre-existing, not caused by seeds: C04UTBZL6AX/2024-08 /73 "Reports into: Lauren Brooks", 14 months before her contract. Leave it out of any check.
- Reachability, not coherence: Wire Returned notices and the Payoneer receipt are in Leonard's mailbox only; Robert sees Apr 2024 return via Slack, nothing for the May 7 $125.

## Conventions
- Slack mention form is right. Leonard mostly types curly apostrophes; curly also avoids SQL doubling. Nit.
- Ask is 717 chars, above private p99 (617) and long for Leonard, who usually splits a thought over several short posts (see Feb 12 #winddown). Not a data defect; splitting into 2-3 consecutive posts would fit his habit better.
- Leapblock contact opens "Hey guys" and never "Leonard, Robert,". Nit.
- Arthur rarely mails; his replies are capitalised ("Done."). Capitalise the first word. Short subject is fine.
- Mail needs copies in Arthur, Leonard, Robert mailboxes; ISO date in numbered files, RFC-2822 in alias files; \r\n.
- Trello: ObjectId prefix from the action time, idMemberCreator PERSON_6094_TRELLO_USER_ID, list Backlog (To Do and Doing hold only closed cards).
- Sheet and deck need Robert in sharing, plus matching Drive rows. Seeds state sharing only for the doc.
- Calendar: copies on both attendee calendars, evt_/ical_uid/hangout_link formats.
- Contact job: base style is 'Marketing Site Contractor', 'Data Analyst (Contractor)'. 'Telegram Contractor' fits better.
- Linear: Arthur's comments must fall between 23:12 and 01:23.

## Rewordings and break attempts
1. A5: "you know what each of these people did better than I do". Break: bucket work needs that, game split does not; no clash.
2. M3: "the one place I know with a line per payment". Break: belief, survives the Sep 13 wire; pairs with "not the last word".
3. L1: "the team's monthly runs go through here". Break: top-ups and gap months no longer conflict; "team" matches the method.
4. L4: "the saga map crew early on, Martin and Victor through them". Break: no order claimed; crew did end first; Victor leaving is not denied.
5. L5: "Marcus's company, monthly". Break: Nov 2023 wire landed Dec 4, still monthly in memory.
6. L17: "...can't remember what it was for". Break: concedes he can read the payee; Arthur's mail still adds the reason.
7. X4/X5: "going through the Chase statements for Sunset's file ... that was our own Chase account". Break: zip covers 2023-2025; tense fits closure.
8. H2: label "All USD notices, by date". Break: ties to the cent; does not name Martin.
9. T1: Trello 22:36, sheet 22:44, deck 22:52, all Feb 12. Break: Slack 22:34 and 23:04, mail 22:56; follows 22:06 P&L and 22:17 angels; precedes Linear 23:12. Tight for 132 notices but a quick pass; if that looks thin, keep the sheet earlier and only move the deck and card.
10. T2: drop "founders'"; Harmony Games board, Backlog; keep "our board" in the doc.
