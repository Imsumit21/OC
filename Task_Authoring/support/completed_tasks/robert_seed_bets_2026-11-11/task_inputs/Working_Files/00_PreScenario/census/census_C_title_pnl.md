# Census C: title-by-title P&L (Feb 14, 2026 normal universe, persona Robert)

Status: COMPLETE for this pass. Facts and locators only. No task text. PDF and other binary attachments were not opened (hg.py JSON search excludes them), so anything inside them is unverified.

## 0. Method and scope notes
- All figures were read through `hg.py search get` on `snowflake.json` by pointer `/tables/<n>/rows` and summed in memory. Nothing was executed against SQL. Scope: base universe, normal, whole table unless stated.
- Table index pointers used: 0 AD_SPEND_DAILY, 3 UA_SPEND_UNIFIED_V2, 4 IAP_TRANSACTIONS, 12 REVENUE_DAILY, 13 REVENUE_DAILY_V2, 14 DAILY_METRICS_AGG, 15 MONTHLY_BURN, 16 CASH_BALANCE, 17 HEADCOUNT, 34 AD_SPEND, 35 AD_REVENUE, 36 STORE_TRANSACTIONS, 38 FINANCE_LEDGER, 39 PAYROLL_ROSTER. There are 40 tables.
- Tool note: `search get` on an out-of-range Snowflake pointer falls back to a multi-minute 2.6 GB scan, and `get-many` on Snowflake is slow. In-range single `get` takes about 0.1 s.
## 1. Snowflake finance and revenue tables

### 1a. Do finance tables carry a title column? No.
| Table (ptr) | Rows | Columns | Title column |
|---|---|---|---|
| FINANCE.EXPENSES.FINANCE_LEDGER (/tables/38) | 704, 2023-04-25 to 2026-02-13 | entry_id, date, category, counterparty, amount_usd (signed), employee_id | None |
| FINANCE.EXPENSES.MONTHLY_BURN (/tables/15) | 239, 35 months 2023-04 to 2026-02 | month, category, amount_usd, headcount_impacted | None |
| FINANCE.EXPENSES.CASH_BALANCE (/tables/16) | 34, 2023-04 to 2026-01 | month_end_date, cash_usd, monthly_net_burn, runway_months, headcount, notes | None |
| FINANCE.EXPENSES.HEADCOUNT (/tables/17) | 371 | employee_id, department, employment_type, start_month, end_month, monthly_cost_usd, roster_line_id, is_founder | None |
| FINANCE.EXPENSES.PAYROLL_ROSTER (/tables/39) | 371 | roster_line_id, employee_id, name, role, title (job title, not game), employment_type, is_founder, start_month, end_month, monthly_cost_usd | None |

Title-bearing tables are revenue and UA only: `game_id` on AD_SPEND_DAILY, AD_SPEND, REVENUE_DAILY, AD_REVENUE, IAP_TRANSACTIONS, STORE_TRANSACTIONS; `title_id` on UA_SPEND_UNIFIED_V2, REVENUE_DAILY_V2, DAILY_METRICS_AGG. Only three values exist: domino_delights, zombie_match_3d, combo_fighter. Crownfall, Trump Billionaires Club, the Telegram port and Barbie have no row in any of these tables.

### 1b. FINANCE_LEDGER by category (sum of amount_usd, whole table)
| Category | Rows | Total | Counterparties |
|---|---|---|---|
| salaries | 422 | -1,932,761.23 | named people, employee_id set |
| operations | 29 | -672,374.58 | single label "Unreconciled operating expenses", 2023-07-31 to 2025-12-31 |
| marketing_ua | 34 | -90,057.48 | adjoe -46,201.54; meta -37,054.67; applovin -6,336.25; google_uac -465.02 |
| art_outsourcing | 28 | -86,000.00 | single label "External art studio", 2023-04-30 to 2025-07-31 |
| cloud_infra | 35 | -75,705.00 | AWS |
| contractor_fees | 28 | -60,300.00 | single label "QA & localisation vendors" |
| professional_services | 36 | -54,840.00 | Legal & accounting -43,140; Sunset (wind-down) -11,700 (FIN-000702, 2026-02-12, see NB-4) |
| software_tools | 35 | -45,138.00 | single label "SaaS vendors" |
| loan_repayment | 1 | -35,500.00 | founder note |
| store_payout | 20 | +3,352.49 | Apple/Google |
| ad_revenue | 25 | +6,341.06 | AppLovin/MAX only, though AD_REVENUE lists five networks |
| financing | 11 | +3,035,500.00 | Griffin 2,700,000; angels 300,000; founder note 35,500 |
Net of all rows -7,482.74.

MONTHLY_BURN totals 3,017,176.29 and matches the ledger category for category (salaries 1,932,761.23; other 672,374.58; marketing 90,057.48; art_outsourcing 86,000; aws_hosting 75,705; contractor_fees 60,300; legal 54,840; tools_software 45,138). It is not an independent source.

Payroll from ledger by PAYROLL_ROSTER.role: executive -759,741.64 (includes Frederick -51,408.08), engineering -721,713.48, art -270,004.62, product -177,849.19, operations -3,452.30. Founders: Robert -250,000.08, Arthur -239,583.41, Leonard -218,750.07. Art-role people: Claire Morgan -106,987.08, Marcus Bennett -105,142.43, Martin Walsh -53,033.08, Artist 5 -3,038.31, Samuel Turner -1,803.72. No row allocates any person to a title.

### 1c. Lifetime revenue by title and source (REVENUE_DAILY, /tables/12, 2,284 rows, 2023-11-01 to 2026-02-09)
| Title | IAP | Ads | Total | First non-zero year |
|---|---|---|---|---|
| domino_delights | 4,824.24 | 7,507.01 | 12,331.25 | 2024 (323.06); 2025 11,762.52; 2026 245.67 |
| zombie_match_3d | 1.99 | 10.00 | 11.99 | 2025 only |
| combo_fighter | 0.00 | 11.75 | 11.75 | 2026 only |
| All | 4,826.23 | 7,528.76 | 12,354.99 | |

Cross-checks: REVENUE_DAILY_V2 (/tables/13) is identical row count and totals; its source_table is REVENUE_DAILY, so it is a copy. IAP_TRANSACTIONS sum 4,824.24 + 1.99 ties exactly (977 rows). STORE_TRANSACTIONS is gross: 993 rows, 16 DD refunds worth 125.84. AD_REVENUE (/tables/35, 77,373 rows, 2024-01-01 to 2026-02-09) gives DD 7,507.43 (0.42 above REVENUE_DAILY), ZM3D 10.00, CF 11.75; paid 6,363.18, accrued_unpaid 1,166.00 (sum 7,529.18). DAILY_METRICS_AGG (/tables/14, 1,682 rows) has no ZM3D rows at all, so it understates by 11.99.

IAP SKUs (IAP_TRANSACTIONS): dd_coins_large 146 / 1,458.54; dd_coins_medium 269 / 1,342.31; dd_coins_mega 29 / 579.71; dd_coins_small 375 / 746.25; dd_remove_ads 57 / 398.43; dd_starter_pack 100 / 299.00; ZM3D bundle.tier2.abandoned_backpack 1 / 1.99.

### 1d. Lifetime UA by title (AD_SPEND_DAILY /tables/0, 2,590 rows, 2024-09-01 to 2026-02-09)
| Title | Spend | Installs | Channels |
|---|---|---|---|
| domino_delights | 83,359.74 | 11,328 | adjoe 46,201.54 / 8,730; meta 30,607.15 / 790; applovin 6,086.03 / 573; google_uac 465.02 / 256; unity_ads 0.00 / 979 |
| zombie_match_3d | 2,187.41 | 3,657 | meta 1,937.19 / 50; applovin 250.22 / 126; unity_ads 0.00 / 3,481 |
| combo_fighter | 4,510.33 | 615 | meta only; Dec 710.04, Jan 2,843.84, Feb 956.45 |
| All | 90,057.48 | 15,600 | |

AD_SPEND (/tables/34) and UA_SPEND_UNIFIED_V2 (/tables/3) have the same 2,590 rows and the same totals by title and network. The ledger's marketing_ua equals the same 90,057.48, month by month, and by counterparty (meta 37,054.67 = 30,607.15 + 1,937.19 + 4,510.33). So Snowflake UA by title is internally consistent, and the only per-title cost that is. The February row is NB-4 territory.

Title return on UA alone: DD 12,331.25 on 83,359.74; ZM3D 11.99 on 2,187.41; CF 11.75 on 4,510.33.

### 1e. Where two tables disagree
- Revenue vs cash in: REVENUE_DAILY 12,354.99 against ledger inflows 9,693.55 (store_payout 3,352.49 + ad_revenue 6,341.06). IAP 4,826.23 at 70% would be 3,378.36, 25.87 above store_payout. Paid ad revenue 6,363.18 is 22.12 above ledger ad_revenue. No table states the store fee rate.
- Ledger art_outsourcing 86,000 against the P&L sheet's outsourcing lines: see section 2 and 5.
- Ledger UA 90,057.48 against the P&L sheet UA row: see section 3.
## 2. Art/creative spend

### 2a. Ledger view (no vendors, no titles)
- `art_outsourcing`: 28 rows, -86,000.00, one counterparty label "External art studio", 2023-04-30 to 2025-07-31, smooth 2,240 to 3,680 a month. Equal to MONTHLY_BURN art_outsourcing.
- `contractor_fees`: 28 rows, -60,300.00, label "QA & localisation vendors".
- `operations`: 29 rows, -672,374.58, label "Unreconciled operating expenses". Real vendor names (Leapblock, Eveline Art, Creative X, Deel) appear nowhere in FINANCE_LEDGER.
- Art-role payroll in the ledger is under `salaries`, by person (section 1b). Marcus Bennett -105,142.43 and Claire Morgan -106,987.08 are the largest.

### 2b. Bank view: SVB "Payment Processed" notices in Robert's own mailbox (the strongest record set found)
Scope: Gmail subject contains "SVB Payment", full scan complete, 765 subject hits in 539 thread files. Mailbox split: Robert 241 thread files, Leonard 184, Arthur 114. Message counts for "Payment Processed": Robert 132, Leonard 132, Arthur 65. Other statuses in Robert's box: Awaiting Approval 130, Scheduled 40, Recipient Created 22, reminders 24, Recipient Modified 2. Each Processed body carries recipient, account suffix, amount, transaction date, payment reference. Sum of Robert's 132: 1,669,393.32, first 2023-09-05, last 2026-02-02.

| Recipient (acct suffix) | Payments | Total | Range | What it is |
|---|---|---|---|---|
| Deel, Inc. (8380) | 24 | 714,059.38 | 2023-09 to 2026-02 | Contractor payroll run |
| [ORG_NAME_0057], Inc. (8380) | 11 | 301,287.81 | 2023-09 to 2025-09 | Same account suffix as Deel, so the same payee behind a token (NB-12 pattern). Combined 1,015,347.19, 35 payments |
| Leapblock LTD (1359) | 29 | 374,654.00 | 2023-10-02 to 2026-02-02 | External studio under MSA; saga map crew plus named people |
| Eveline Art S.R.L. (8501) | 28 | 93,171.50 | 2023-10-27 to 2026-02-02 | Marcus Bennett's company (see below) |
| Adjoe GMBH (5000) | 3 | 46,201.50 | 2025-05-05 to 2025-08-29 | UA, DD; warehouse 46,201.54 |
| BANCO DE AMERICA (3341 x10, 8605 x1) | 11 | 41,088.00 | 2024-04 to 2025-02 | A contractor's Costa Rica bank, invoice thread robert/1795166906688019939 |
| Singular (4015; shown as [SOURCE_ORG_0351] Labs Inc 25,000 and Singular Labs Inc 6,250) | 2 | 31,250.00 | 2024-09-25, 2025-09-26 | MMP |
| PERSON_4419_NAME LLC (0115) | 1 | 16,428.57 | 2025-01-02 | Unidentified |
| TYZ Law Group | 1 | 7,500.00 | 2024-02-06 | Legal |
| [PERSON_NAME_7200] (7393) | 4 | 7,175.00 | 2023-11 to 2025-03 | Unidentified |
| [PERSON_NAME_36400] (6577) | 3 | 6,450.00 | 2024-09 to 2024-11 | Unidentified |
| AppLovin Corporation | 2 | 6,085.56 | 2025-08-29, 2025-11-12 | UA; warehouse DD 6,086.03 |
| Graham Porter | 1 | 5,000.00 | 2025-05-29 | Unidentified |
| JPMorgan token | 1 | 4,000.00 | 2024-08-19 | Unidentified |
| CREATIVE X TEKNOLOJi (5660) | 1 | 3,750.00 | 2025-05-16 | PlayableX, first DD playable |
| M token (4020) | 1 | 3,200.00 | 2023-10-27 | Unidentified |
| Nathan Price token (0148) | 1 | 2,368.00 | 2024-08-03 | Contractor, Robert ended the contract 2024-07-25 |
| Martin Walsh (3801) | 1 | 1,999.00 | 2025-10-30 | Contractor |
| Brooks token (5384) | 3 | 1,500.00 | 2025-10 to 2026-01 | Contractor |
| PERSON_6074_NAME token (3307) | 1 | 1,000.00 | 2025-03-21 | Ozhan, 2D zombie animation for ZM3D (see 2d) |
| Small | 3 | 1,225.00 | | 600, 500, 125 |

Locators: bodies are in `threads/<8 digits>.json` of Robert's mailbox, for example Leapblock first payment `threads/00001695.json`, Creative X `threads/00013667.json`, Eveline first `threads/00001860.json`, Adjoe `threads/00013448.json`, `00014467.json`, `00015146.json`, Ozhan `threads/00012291.json`. One thread file can stack several same-subject messages (00015146 has six payments), so 132 payments sit in fewer files.

Caution on deduping across mailboxes: Leonard's and Arthur's copies render the date and sometimes the reference differently, and a naive union gives a false 188. Use Robert's 132 alone. Only the count equality with Leonard's box (132 and 132) was checked, not a payment-by-payment match.

Eveline Art identity: `D05UDNCCYKC/2023-10 /118` says the consulting agreement is with "Marcus ... Bennett doing business as Eveline Art S.R.L." That DM is NOT readable by Robert (can-see NO). A Robert-readable tie is still needed; the P&L salary tab lists Marcus Bennett at 3,700 a month against Eveline 3,720, which is a lead, not proof.

### 2c. Sheet view: HG Costs tab, Jan 2026 P&L (`f_605121f4a36752645e0ac3`, /sheets_spreadsheets/141/sheets/2, Robert shared)
Totals below are all non-empty cells. Columns run Jul-23 to Dec-26, see the header trap in section 5.
| Row | Total | Months | Title link |
|---|---|---|---|
| Saga Map Outsourcing | 194,950 | Jul-23 to Nov-24 | Saga map is a DD feature (#god-saga-map) |
| 3D Animator | 26,518 | Oct-23 to Jul-25 | Not stated |
| Mini Game Unity Developer PERSON_R001 | 13,975 | May to Nov 24 | DD mini games, lead |
| Mini Game Unity Developer PERSON_3060 | 11,361.10 | to Mar-25 | DD mini games, lead |
| Temp Game Unity Developer PERSON_3233 | 23,336.20 | Jul to Nov 24 | Not stated |
| Unity Assets (Zombie Match) | 946.80 | Jan to Oct 25 | Named ZM in the row label: the only per-title row in the tab |
| Sound (Pond5, Soundly, Elevenlabs) | 595.50 | from Jul-24 | Not stated |
| Typecast.ai (Voice) | 495 | May-24 to Jul-25 | Not stated |
| Veed 528, Kling 99, Hailuo.ai 120 | | | Video tools |
| Silje Molna | 1,500 | Oct to Dec 25 | Telegram port lead (BoD Oct 14 2025 p9) |
| UA Assets | 20,633.45 | Jan-24 to Apr-25 | Not stated |
| Figma 4,779; Adobe 350; Solsten 30,000 (Jan-24) | | | |

### 2d. Vendor records with per-record lookups
| Vendor | Amount | Title | Attribution record | Robert can read? |
|---|---|---|---|---|
| Creative X / PlayableX | 3,750 | DD first playable | `C08H78VJG80/2025-03 /10` "first playable, we'll focus on Domino Delights"; `C07C2866011/2026-02 /24` and ts 1770082607.231919 "we did it for $3750" | Yes (#playablex, #executives) |
| Ozhan, 2D animator | 1,000 | ZM3D | #executives ts 1740691596.526029 "$1K for a week"; #art_outsourcing `C08FG9924R2/2025-02` (zombie walk, idle, attack clips; poster PERSON_6074_SLACK_ID); SVB `threads/00012291.json` payee PERSON_6074_NAME, same token number | Yes |
| Telegram contractor (Consulting Agreement Lauren Brooks `f_20a0df3860bb5731d22f07`) | 3 x 500 | Telegram port | Exhibit B: minimum $500 up to $20,000 a month, profit share on Telegram only, from Oct 10 2025; SVB 2025-10-30, 2025-12-01, 2026-01-06; HG Costs "Silje Molna" 500 x 3. The sheet name and contract name differ, so the match rests on amount, dates and scope | Yes |
| Leapblock saga map crew | $15K a month in 2023-24 | DD | `C04UEQVDVB7/2023-09 /554`, `2023-11 /35` "$25K ($15K for saga map + $4K for Victor + $3K for Martin + $3K for animator)", `2024-01 /109` | Yes (admin_foundersonly) |
| Leapblock November 2024 tail | "$1750 to November" | DD | `C04UEQVDVB7/2024-10 /124` | Yes |
| Typecast | cancelled | None | `C04UEQVDVB7/2025-07 /16` "canceling since we are not adding any voiceovers" | Yes |
| Unity Assets (Zombie Match) | 946.80 | ZM3D | HG Costs row 15 | Yes |

Unity Asset Store orders, Robert's mailbox, 12 order confirmations (Arthur 5, Leonard 1 more). Bodies name packs but no price; the price is in a PDF attachment, not read. Their months match the HG Costs row "Unity Assets (Zombie Match)" exactly: Jan-25 164.89 (4 orders), Feb-25 377.97 (2), Mar-25 264.95 (4), May-25 39.99 (1), Oct-25 99.00 (1), sum 946.80.
| Thread | Date | Packs |
|---|---|---|
| 00010438 | 2025-01-08 | Low Poly FPS Weapons Pack, vol.2 |
| 00010455 | 2025-01-09 | Hypercasual Kids Cartoon Weapon Pack, Hypercasual Action Props Pack vols 1-4 |
| 00010474 | 2025-01-10 | 3D Food Pack, Interior Low Poly Asset Pack |
| 00010748 | 2025-01-20 | KayKit bundle (Furniture, Prototype, City Builder, Space Base, Skeletons, Dungeon, Adventurers, Halloween) |
| 00011032 | 2025-02-03 | Zombie Undead Ultimate MegaPack |
| 00011412 | 2025-02-14 | 3D Object Pack, Low Poly Cartoon Item Pack 2, BIG PACK Cozy Cartoon Profession Rooms, Furniture Cute |
| 00011793 / 00011794 / 00011795 | 2025-03-05 | BIG PACK Cozy Cartoon Rooms 2; Stylized Explosion Pack 1; Stylized Impacts +100 VFX |
| 00012170 | 2025-03-18 | BIG PACK Cozy Cartoon Rooms Interiors |
| 00013529 | 2025-05-09 | Toon Camp Pack |
| 00015627 | 2025-10-13 | Game UI & Puzzle Sound Effects Pack |

Trap inside that row: the Oct-25 pack sits only in the Combo-Fighters repo (3,770 of 3,770 matching paths), so the 99.00 labelled Zombie Match in the sheet is Combo Fighter by the repo. KayKit and Hypercasual paths appear under match3d (first 400 of 4,543 and 1,539 shown, not a full count). No path matched the names Zombie Undead, Stylized Impacts, Toon Camp or Cozy Cartoon, so those folders are renamed or absent.

Unity Ads: 7 "Receipt from Unity Ads" in Robert's mailbox, $1,000 each (`threads/00002874`, `00003209`, `00003348`, `00003439`, `00003851`, `00007783`, `00014282`), 21 more in Leonard's box only. No title on them, and NB-19 applies to the warehouse side.

| Lead, not proven | | | HG Costs 3D Animator Jun-25 600 and Jul-25 4,800 sit next to Robert's 2025-06-24 "finding Marcus some contractor to help him animate/rig the monsters" (ZM3D). Payee not identified | |

Honest per-record attribution count: about 7 vendor lines plus the 12 orders have an amount or pack and a title from Robert-readable records. Everything else in 2c lacks a title in the record. Leapblock's PDF invoices (for example `C04UEQVDVB7/2024-05 /54`, files "0000000074 29.04.2024 EN.pdf") are Slack attachments and were not read.
## 3. Board decks and P&L sheets Robert can read

### 3a. P&L versions (Sheets; owner Resource: 7240535625619857401, private)
Shared with Robert: Oct 2023 `f_90976e6b4466acbfaf5a74`, Jan 2024 `f_779b6777b8ffc4acecc2d1`, Apr 2024 `f_29467f8365d566d7bb2e76`, Oct 2024 `f_2cb4e217609f00a8ecf416`, Apr 2025 `f_44ea2c36d71239ae75cc84`, Oct 2025 `f_28ecc492b19f3696a19a97`, Jan 2026 `f_605121f4a36752645e0ac3`, and 4X GAME BUDGET `f_68c2418dd4ab47afe9254a`. Confirmed by can-see for Jan 2026 and 4X.
Not readable: June 2025 `f_846ac36bcfd5d2fb5be232`, July 2025 `f_a5e9fc9c8a3188faf66784`, Sep 30 2025 `f_dd0ba4f44cacbb5941d82e`, Game of Dominoes Internal Financial Model v2.2 `f_438130df7c32bce9388d58` (all can-see NO). Also not shared by the list: July 2024 `f_98ec332dff628ee0c55eb4`, April 2024 `f_a945855a550793e43d7b8d`, Internal Copy `f_8e071fd6b2f51c4149d761`, Jan 2024(1) `f_96380180e62e7121b22013`, "without or reduction" `f_47ee780ad5758983d1db6f`.

No P&L tab splits by title. The only title words are the comment "Small Budget for ZM test, else marketing freeze" (Oct 2025, /sheets_spreadsheets/62/sheets/0/grid/9/40), "Small Budget for CF test" (Jan 2026), "Soft launch on Oct 3rd, initial marketing budget $35K/month" (Oct 2024, /72/sheets/0/grid/1/25) and the HG Costs row "Unity Assets (Zombie Match)".

### 3b. Jan 2026 sheet against other sources (positional months, to Dec-25)
| Line | P&L sheet | Warehouse or ledger | Bank notices |
|---|---|---|---|
| Revenue | 9,859.36 "Mobile revenue (cash in)" | REVENUE_DAILY 12,097.57; ledger inflows 9,369.49 | None |
| Revenue Oct-25 | 2,021.42 | 307.88; ledger 278.01 | |
| Revenue May-25 | 1,036.08 | 3,295.46; ledger 747.79 | |
| UA | 126,134.96 (18,259.33 before Sep-24) | 86,237.56 (spend starts 2024-09-01) | Adjoe 46,201.50, AppLovin 6,085.56 |
| UA Sep-24 to Dec-25 only | 107,875.63 | 86,237.56 | |
| Salary and benefits | 2,086,509.80 | ledger 1,922,865.35 | Deel account 1,015,347.19 plus others (bank totals run to 2026-02-02) |
| Art outsourcing | Saga Map 194,950 + 3D Animator 26,518 | art_outsourcing 86,000 | Leapblock 374,654; Eveline 93,171.50 |
| Jan-26 people | 17,000 | ledger 9,895.88 | 2026-02-02: Deel 9,889.90 + Eveline 3,720 + Leapblock 3,700 = 17,309.90 |
The last row suggests the ledger's January salaries equal the Deel leg only. That is an inference. NB-2 still bars grading those sheet lines.

### 3c. Decks and docs (all Robert-shared; Slides pointers)
| Record | Figures quoted | Title-level? | Cards |
|---|---|---|---|
| BoD Jan 14 2026 `f_65ada5e24989d256cabdfa` /slides_presentations/57 | p2 ~$25K bank, burn $25K/month, Boombit and CrazyGames signed for DD; p6 CF ~500 installs, D1 30%, CPI ~$3.90; p10 $500K bridge = founders $210K + 4 core $150K + $140K marketing; p13 salary burn $17K | CF KPIs only | NB-3, NB-20 (the deck reads $140K on p10, not the $150K or $170K on the card, so a third figure) |
| BoD Oct 14 2025 `f_d03044b385b94f24b21ff4` /132 | p2 ~$157K bank, burn ~$25K; p7 DD installs by source; p8 ARPDAU $0.10; p9 Telegram "No fixed fee or salary"; p11 ZM ~300 installs, CPI ~$4.5 | KPIs, no spend | NB-17, NB-18 |
| Internal BoD Jul 16 2025 `f_0421912301531f11c54686` /2 | p8 DD incent: installs 18.5K, ad spend $51K, IAP $3.5K, ad rev $5.3K, total $8.8K, ROAS 17%; p20 4X partnership did not materialise; p21 $1.5M dev + $0.5M UA | DD UA test only | NB-18 |
| Board Meeting Jul 25 doc `f_af99b76ff4da59a710edba` /docs_documents/439 | ~$365K bank, $50K UA spend, $30K incentive option | DD | |
| Internal BoD Jan 15 2025 `f_6c5e1d9d447327083a0638` /62 | p8 CPI $6.70 and $6.85 by audience | DD | |
| Crownfall External `f_06634353252b13af2bdedd` /4 p25 | Budget proposal: Phase 1 ~$2.15M, post launch ~$1.95M, FTE ~$3.65M. A proposal, never spent | Crownfall, plan only | |
| FAQ `f_07954a17e579a6d662c2fa` /5 p31 | Heading "Game of Dominoes P&L" only, body is not text. Note p13 uses DD for the competitor Domino Dreams | None | |
No deck or sheet Robert can read states lifetime spend by title.
## 4. IP and asset side

### 4a. What is known about the auction
- The word "auction" appears once in Slack for Feb 2026: #executives ts 1770850800.723979 `/411`. Gmail in Robert's box has no relevant hit (all 23 hits read, all noise such as ad auctions and newsletters).
- Same day, ts 1770839126.382429 and 1770839149.629569: "they will liquidify all the assets including laptops build machines etc as well as IP"; "if we want the IP we can buy with our own money from liquidation". "They" means Sunset or Sherwood, per the investor's advice at ts 1770839105.706739.
- Nobody has published a date, reserve, asset list or bidder. Leonard's 2026-02-09 draft, #winddown `/7`, says "evaluate what to do with the remaining IP and codebase (archive, sale, or other disposition)" and "We will share a more detailed wind-down plan and timeline shortly". A 2025-12-05 line, ts 1764907635.338249: "if [investor] doesn't mind us taking over the IP for free".
- Superseding event: 2026-02-12. Sunset offered $22,500 cash for data with a data purchase agreement (`threads/00016827.json` msg 6). Leonard objected that the assignment was broad (#winddown ts 1770923360.551399, 1770924424.711879). It became a data licence: msg 7, then msg 8 "Added in Section 1.5 re: IP ownership" and "7.9 ... this license would still survive upon a transfer of the assets". Signed by msg 11. The agreement text is an attachment, not read.
- Fee: $11,700 (#winddown ts 1770911000.728559), after a 20% bundle discount (msg 6), against $13,000-$15,000 in notes `threads/00016883.json` and ~$15K at ts 1770850852.708789. "Quote is gonna go slightly higher" for California, ts 1770924465.624129. NB-4 applies to whether it was paid. Sherwood thread: robert/1856689465442954434.

### 4b. Assets per title (GitHub is visible to all personas)
| Title | Repos | Third-party packs in Assets/ (file-path evidence) | Encumbrances |
|---|---|---|---|
| Domino Delights (GoD) | GameOfDominoes, game-of-dominoes-backend | D.A. Assets, NiceVibrations, 4300UIButtonsPack, I2, Le Tai's Asset, OToon URP Toon Shading, Simple Scroll-Snap, SuperCombiner, Layer Lab, BIG_Environment_Pack_LP, AmplifyColor, Helpshift. Fonts include sui generis, LuckiestGuy, Lato, Noto | CrazyGames licence signed 2025-12-05 (`threads/00016114.json`; #admin_foundersonly `2025-12 /9`, `/10`; web only per the summary in the thread); Boombit test agreement (#publishing-ext `C09SWTHEMEW` ts 1763483180.065909 onward, Jan deck p2) |
| Zombie Match 3D | match3d, match3d-backend, match3d-backend-auth, match3d-quests, ZM-Liveops-Docs | Feel, SpecialSkillsEffectsPack, EffectCore, D.A. Assets, ColliderCreatorPro, QuickOutline, KayKit, Hypercasual packs. Fonts include NEXON Football Gothic, Lato | None found |
| Combo Fighter | Combo-Fighters | Game UI & Puzzle Sound Effects Pack, Art/Music BattleMusic wavs, stock-numbered sound file heal-sound-2-409138.mp3, ChangaOne font | None found |
| Shared | auth-game-backend, game-analytics-pipeline, liveops, liveops-dashboard-buddy, harmony-gpt, website, rpg-prototype, MinigamePrototypes | | |
match3d listing is truncated at 60,000 of 118,592 paths, so its pack list is partial. Licence files exist in-repo for some packs, for example NiceVibrations/3RD-PARTY-LICENSES.md, Feel/license.txt. No record states whether Asset Store seats transfer. Seats are on an organisation per the order mails.

Other titles: Crownfall is decks and a budget only. Trump Billionaires Club is not an HG title; #executives shows it as a separate "Blake LLC" matter (ts 1744319690.043349) plus a news link (ts 1765384805.140929). No revenue or spend rows. Telegram port is the DD WebGL work plus the Brooks contract. Barbie is a pitch: `threads` robert/1842359641903957253, 1850507819115092292, 1851346358384492307.

### 4c. Brand
- "Harmony Games" and "Domino Delights" US applications via a Turkish firm, `threads/00014372.json`. Toon Boom co-existence terms in #admin_foundersonly `2025-08` ts 1755063509.040609: no use of "Harmony Games" standing alone, deemed abandoned after 3+ years unused, binds successors and licensees. Whether it was signed was not established.

### 4d. Contractor IP chain
- Leapblock MSA `f_322bbfdb37d253aa8624b9` /docs_documents/123, Robert shared: effective Aug 7 2023, project "Game of Dominoes - 3D Saga Map", US$15,000 a month, present assignment plus works made for hire. Termination notice `threads/00004488.json` (2024-04-25) names different contracts: "Forest Zone Creation" from April 7 2023 and "Animations" from Sep 25 2023, both ending May 31 2024, then on-demand individuals.
- 37 docs titled Consulting Agreement in Docs; all contain assign or work-for-hire language by regex; 20 are shared with Robert; 2 are templates and 1 is a placeholder (XXXXX), and several are versions of one person (Claire Morgan 5, Calvin Price 3). Claire Morgan's five are NOT Robert-shared. Distinct people were not counted because tokens hide names. These are drafts in Docs; a signature needs a DocuSign mail or signed PDF, for example `f_073197a3c33ab963975eb1` Consulting Agreement Marcus signed.pdf. Robert has 25 "Completed:" mail hits.
- Confidentiality, IP and Non-Solicitation form: `f_0f8dbf075d5d5c55bf10fd` (Robert owns). Advisors: robert/1768085436824934351 "two advisors who will not be signing IP assignments".
- Marcus: `f_af481d73feee6fd3bc4d8e`, Robert shared, doing business as a token, Sr. VFX Artist, $3,000 a month from Oct 12 2023.
- Creative X: Leonard's objection to "All IP related to the playable ads remains solely with Creative X" is in `D08JRD3TQE8/2025-05 /21`, which Robert cannot read (can-see NO). Final contract terms not established. Robert-readable #playablex was not read for this.
## 5. Coherence hazards
Keep these out of any graded answer unless the row says otherwise.
1. HG Costs headers are not real dates. Day-of-month is the year, and the year field drifts: `2023-01-24` means Jan-24, `2024-12-25` means Dec-25, `2025-10-26` means Oct-26. Read by position from Jul-23 (col 2) to Dec-26 (col 43). Jan-26 onward is forecast. Proof: HG P&L shows 5,000 Jan-26, 6,250 Feb-26 and Jun-26, matching HG Costs cells `2025-01-26`, `2025-02-26`, `2025-06-26`. The Atlas section 5 line "Monthly values (Sep-Dec 2025)" is therefore a year out: those cells are Sep-Dec 2026 forecast. Unity licence in Dec-25 is column `2024-12-25` at 2,172; the 1,200 cells are Oct to Dec 2026 forecast. That also sits closer to Leonard's "~2.348*9 months" than the Atlas reading does.
2. Ledger art_outsourcing 86,000 is a smooth label, not an invoice history. It disagrees with HG Costs and with the bank. Do not present it as "what art cost" without saying so. `operations` 672,374.58 is an explicit plug.
3. Ledger counterparties never name Leapblock, Eveline or Creative X. A by-vendor answer can only come from SVB mail.
4. [ORG_NAME_0057], Inc. equals Deel by account suffix 8380 only. Same for Singular under [SOURCE_ORG_0351] (4015). NB-12 pattern.
5. SVB Leapblock 33,290 on 2023-09-13 (`threads/00001577.json`) reached Awaiting Approval and has no Processed notice in Robert's box. Leonard: "I need help with leapblock wire transfer first" (2023-09-12). Lifetime Leapblock is 374,654 or 407,944 depending on this. The other 18 unmatched Awaiting rows are token swaps. A $125 wire of 2024-05-07 was returned (Leonard's box only), yet Robert's box shows it Processed.
6. Creative X: bank 3,750 on 2025-05-16; HG Costs UA Assets Apr-25 is 3,500. Slack "$3,000 per playable" is the rival offer and "$4,000" the ask. No payment to Creative X after May 2025, so "playable spend" in Feb 2026 has no invoice.
7. Warehouse Unity Ads rows: $0 spend with 4,460 installs (ZM3D 3,481, DD 979). ZM3D's UA and CPI are understated. NB-19.
8. Warehouse spend starts 2024-09-01, so pre-Sep-24 UA (18,259.33 on the sheet) has no warehouse row.
9. CF CPI: deck ~$3.90, Leonard ~$5, Robert $6, warehouse Dec $5.26 / Jan $7.02 / Feb $12.75. Do not grade a single CF CPI.
10. CF IAP: warehouse 0.00, Robert "2 people bought rotation pack". NB-26. CF title return can only be stated as warehouse-recorded.
11. Revenue basis: gross 12,354.99, ledger cash 9,693.55, P&L 9,859.36 to Dec-25. Any graded revenue must name REVENUE_DAILY. DAILY_METRICS_AGG omits ZM3D.
12. AD_REVENUE DD 7,507.43 against REVENUE_DAILY 7,507.01.
13. February 2026 rows are accrued. NB-4. The ledger runs to 2026-02-13, warehouse to 2026-02-09.
14. Cash at Dec 31 and Jan 31. NB-3. Burn comment. NB-10. Sheet costs. NB-2.
15. Employee or contractor. NB-15. Job titles also differ: roster has Robert as Chief Product Officer, decks CXO, Leonard in Slack "chief product officer"; Marcus is "Artist" on the roster and Sr. VFX Artist in his contract and the deck; Victor Barnes is Art on the P&L salary tab, engineering on the roster; Martin Walsh is "Game Designer" on the roster, "UI Artist ... via leapblock" in Slack.
16. Combo Fighter on Google Play, level funnel. NB-9, NB-7. DD installs for Jan-Feb 2026 and Sep 2025. NB-17, NB-18. Oct-Dec DAU drop. NB-33. Board marketing figure. NB-20.
17. Name collisions: DD can mean Domino Dreams in the FAQ; GoD and Game of Dominoes are Domino Delights; Puzzles vs Zombies is ZM3D until July 2025 (Confluence pages/7), and NB-25.
18. Shutdown date. NB-29. Slack after Feb 13 10:03. NB-6. #winddown Slack access after Feb 11 for non-founders. NB-1. Robert's own reach is fine: all finance channels are YES.
19. A 2026-01 revenue split DD 183.11, CF 7.36, ZM3D 0.00 was already used as a trap in robert_llc_takeover. Reusing January-versus-hosting would overlap. Lifetime figures are new.
20. Silje Molna (sheet) and Lauren Brooks (contract, bank) are different strings. Oct deck says "No fixed fee or salary"; the contract says minimum $500.
## 6. Natural per-record volume
| Cohort | Source-defined? | Count, scope | Per-record surface | Bulk shortcut |
|---|---|---|---|---|
| SVB "Payment Processed" | Yes, bank notices | 132 payments in 80 thread files, Robert's mailbox | Recipient, suffix, amount, date in body; subject identical on all | No table carries them. A payee-name search narrows the list, but amounts need thread reads. This is the only 40+ cohort that passes |
| Art subset of that | Yes | Leapblock 29 + Eveline 28 + Creative X 1 + Ozhan 1 + Telegram 3 = 62 payments | As above | Same |
| SVB "Awaiting Approval" | Yes | 130 messages; 111 pair with Processed, 18 token swaps, 1 true orphan | Status comparison | No |
| Consulting Agreement docs | Yes | 37 in Docs, 20 Robert-shared | Exhibit B pay and IP clause; signature proof elsewhere | Search returns titles only |
| Asset Store orders | Yes | 12 Robert, 18 across three boxes | Pack names, repo path check | No, but small |
| Monthly Leapblock breakdowns in Slack | Partly | Only a few months spelled out in text (2023-09, 2023-11, 2024-01); the rest are PDF attachments | | |
| AD_SPEND_DAILY 2,590, IAP 977, STORE 993, AD_REVENUE 77,373 | Yes | | | One Snowflake read each. Bulk, so no per-record work |

Limit on the SVB cohort: the payee is per-record, the title is not. Deel's 35 payments (1,015,347.19, the largest share) are payroll lumps with no title or person on them. Only Leapblock before June 2024 has a title by contract.
## 7. Robert personally making budget or money decisions
Slack, Robert's own messages, channels admin_foundersonly, executives, founders, winddown, art_outsourcing, prototype, playablex, combofighter-vfx. Counts (all / matching a money regex): admin_foundersonly 2,785 / 265; executives 8,046 / 231; founders 16,579 / 770; prototype 5,372 / 88; art_outsourcing 65 / 3; winddown 19 / 0. Most hits are personal or market chatter. Read before quoting. The strongest:
- #executives 2026-02-05 ts 1770264360.331789, `C07C2866011/2026-02 /219`: "Save money for playable spend", answering Leonard's 2026-02-04 question ts 1770236308.958639 on doubling Meta spend (Arthur proposed one day at ts 1770239191.950109). Leonard replies "hahaha ok" ts 1770270579.935499.
- #executives 2025-02-27 ts 1740691596.526029 `/1286`: "So we hired a art contract ... $1K for a week. Slightly over priced"; `/1287`: "Reasonable price would be closer to $750".
- #art_outsourcing 2025-02-27 ts 1740687004.695729 to 1740687076.849859: Robert brings in Ozhan for ZM3D 2D animation and scopes it to about a week.
- #executives 2025-04-25 ts 1745613793.935509 `/1546`: quoted line on budget holding back ZM UI/UX, "another $5K-$10K 3D art objects"; `/1548` "More like $20K+".
- #executives 2025-06-24 ts 1750802263.452099 `/552`: "I'm finding Marcus some contractor to help him animate/rig the monsters".
- admin_foundersonly 2024-06-17 ts 1718609550.085859 "$1075 it is"; 2024-07-23 ts 1721776655.058739 "I paid Lucas for July"; 2024-07-25 ts 1721871255.143949 "I ended Nathan's contract"; ts 1721871680.548609 "~$2K a month, what can you possibly get?".
- admin_foundersonly 2023-11-01 ts 1698823242.646219 "Nah, it's fine. It's $250 man"; 2025-05-06 ts 1746550083.541619 on paying by exchange rate hurting "P&L planning".
- #executives 2026-02-03 ts 1770094038.279489: Robert's own breakeven arithmetic on CPI and ARPDAU; ts 1770093770.065709 "our marketing sucks if we're doing $6 CPI?".
- #executives 2026-02-03 ts 1770084297.911029: "I just need to see if Combo Fighters can get to a point where it's self sustaining".
- Bank role: in Robert's 132 Processed notices the "by" fields show his token [PERSON_NAME_0054] (the greeting in his own mailbox) as creator on 2 and as approver on 16. Leonard created 83, Arthur 46. Token mapping is inferred.
- Unity Asset Store: 12 order confirmations 2025-01-08 to 2025-10-13 addressed by his token (section 2), and Marcus at #art_outsourcing ts 1740859873.551479 says Robert has the full paid version of a VFX pack. Robert archived that channel, ts 1748446155.320549.
