# /prompt working draft (Phases 1-4, Phase 5 pending)

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
Universe: `Evals/references/universes/normal/universe_manifest.json` (sha256 5e01ac4472c8c181...)
Inputs: prompt `inputs/04_Prompt.txt` sha256 d0cb08476d234f32...; SQL `inputs/01_Universe_Inject.sql` sha256 40f90385e31e099d... (124 INSERT, 2 UPDATE); SQL rev7 differs from rev6 by one added Slack row and two reworded Linear comments.
Evaluator: Opus 5.5 (claude-opus-5-5), blind Phases 1-4. No write outside `out/`.

## Assignment (intake clear)

Persona Robert, robert@harmonygames.co, Co-founder & Creative Director (roster); business function Executive; competency Finance; task skill Analysis and synthesis; horizon Long Horizon (`inputs/00_Task_Assigned_Inputs.md`).

### Injection Gate (STEP 0.5)
State: PENDING. A separate Eval 0 reviewer is running on sha 40f90385...; this draft does not reuse any Eval 0 result. Lint (`hg.py lint`): 0 FAIL / 0 CHECK / 0 INFO. If Eval 0 fails on a record the answer depends on, that goes to Cross-Service Coherence (3.2).

## What the prompt requires (independently derived)

Incorporation chain: prompt "He laid out how he wants it counted and how it should look" and "Work through the Payee history project in Linear the way he wants" point at Leonard's Slack (#winddown C0ADGSZKR3R, fa707da5..., f5b759f3...) which names the doc "Angel note: how to count the money" (f_6feda53b...) and "the layout of my Angel note working sheet" (f_3304033...). Both are shared with robert@ in SQL.

Required writes (all from the prompt plus the doc):
1. New Google Sheet in Robert's Drive, layout of `Angel note working` (Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note), 22 payee lines, shared with Leonard and Arthur Blake.
2. All 22 Linear issues ENG-2438..ENG-2459 moved to Done.
3. A comment on each issue whose figure differs from the notices, before the Done move: 5 issues (ENG-2439, ENG-2442, ENG-2447, ENG-2450, ENG-2459).
4. One Slack reply in #winddown: cost to build per bet, brought in per bet (no Combo Fighter revenue), what changes on the deck, the sheet link. No deck write (Leonard: "I'll update it myself").

### Ground-truth ledger (computed, base notices + SQL overlay)

Source: 329 `SVB Payment Notification: Payment Processed` emails across 3 mailboxes = 132 unique payments (Robert holds all 132; `Payment Reference` dedupe). USD by bet: DD 984,888.21 / ZM 608,820.50 / CF 73,685.61 (matches Leonard's quick numbers in `Angel note working` and the deck's $985K/$609K/$74K). Plus 1 BGN payment.

Adjustments, each with its authority:

| Payee (issue) | Notices | Line | Why (record, Robert-visible) |
|---|---:|---:|---|
| Leapblock LTD (ENG-2439) | 374,654.00 | **407,944.00** | Doc: "If someone we paid closes out their file with us and tells us what they received, that beats the notices for them." Leapblock's accountant closure in #leapblock (SQL 6312d121, EMPLOYEE_0024): "2023 (from 13 Sep, the first one 33,290) 104,868; 2024 232,726; 2025 62,950; 2026 7,400. Total 407,944 over 30 wires". Notices are 29 wires: 2023 71,578 / 2024 232,726 / 2025 62,950 / 2026 7,400. Only the 13 Sep 2023 $33,290 is missing (Payment Awaiting Approval email in Robert's mail, threads/00001577 "Amount: 33,290.00 USD Transaction Date: Sep 13 2023"). DD +33,290 |
| BANCO DE AMERICA / MotMot (ENG-2442) | 41,088.00 | **37,056.00** | Doc: "Take a notice as paid unless one of us has said the money came back." Leonard #admin_foundersonly (SQL a1488189): "that Apr 2024 wire to the account ending 8605 came back to us. Blake had the wrong number, he re-sent it to 3341". Base corroboration C04UEQVDVB7 2024-04: "money returned to us because Blake put the wrong account number". Re-send to 3341 on 2024-04-05 $4,032 stays |
| JPMorgan ***3203 (ENG-2450) | 4,000.00 | **0** no bucket | Arthur's email (Gmail, SQL, robert copy): "the $4,000 to JPMorgan ***3203 on the SVB notices in Aug 2024 was me. That was our own Chase account ... So it never left the company." Doc: "Money we moved between our own accounts isn't spending, no bucket for that. Every payee keeps its line, even at zero." |
| Private Entrepreneur / Oleg (ENG-2459) | 125.00 | **0** Marketing | Leonard's comment on ENG-2459: "that wire came back the same day, I'd already re-sent it through payoneer". Doc: re-send "goes in only if a receipt for it reached your mail". Robert's mail holds only `Dixelar sent you a payment request` (threads/00004614, 00007150, "Dixelar is requesting a payment of 125.00 USD", "Pay Now"). No receipt. Actual receipts ("Thanks for your payment to Dixelar", 126.25 USD) are in Leonard's mailbox only |
| Lucas (ENG-2447) | 6,450.00 | **13,975.00** | Doc: "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee." Five Western Union transfers in Robert's mail, each with "Lucas received the money you sent" and Transfer amount: 1,075 (2024-06-03, 00005198), 1,075 (06-17, 00005351), 1,075 (06-29, 00005490), 2,150 (07-23, 00005963), 2,150 (08-23, 00006330) = 7,525. Fee 0.00 / 0.99 excluded (Billing Summary in 00005184 etc.) |

Lines (USD, DD / ZM / CF, bucket):

| Issue | Payee | Bucket | DD | ZM | CF | Company | Key evidence |
|---|---|---|---:|---:|---:|---:|---|
| ENG-2438 | Deel, Inc. ***8380 | Build | 530,736.14 | 434,185.44 | 50,425.61 | | Doc "Everything on Deel counts as team" |
| ENG-2439 | Leapblock LTD | Build | 337,594.00 | 59,250.00 | 11,100.00 | | statement + notices |
| ENG-2440 | Eveline Art S.R.L. | Build | 45,941.50 | 36,070.00 | 11,160.00 | | "Marcus's art" |
| ENG-2441 | Adjoe GMBH | Marketing | | 46,201.50 | | | "incent UA" |
| ENG-2442 | BANCO / MotMot | Build | 28,128.00 | 8,928.00 | | | engineer on our team; 8605 out |
| ENG-2443 | Singular Labs | Company | | | | 31,250.00 | "attribution tool, not one game" |
| ENG-2444 | PERSON_4419 LLC (Node Media) | Marketing | 16,428.57 | | | | Robert's mail: Google Ads manager link (00007026), "Fwd: PERSON_4419_NAME Invoices for Sept, Oct, and Nov" with "ad spend" and "creative concepts" (00008689) |
| ENG-2445 | TYZ Law Group | Company | | | | 7,500.00 | "lawyers" |
| ENG-2446 | [PERSON_7200] trademark filings | Company | | | | 7,175.00 | "trademark filings" |
| ENG-2447 | Lucas | Build | 13,975.00 | | | | "mini games dev"; #founders 2024-06-14 "build it as a mini game as well in our game" |
| ENG-2448 | AppLovin | Marketing | | 6,085.56 | | | "past due UA bills" |
| ENG-2449 | Graham Porter | Build | | 5,000.00 | | | "art director for a month" |
| ENG-2450 | JPMorgan ***3203 | none | 0 | | | | own account |
| ENG-2451 | CREATIVE X TEKNOLOJi | Marketing | | 3,750.00 | | | "playable ad for our UA" |
| ENG-2452 | M [PERSON_0056] JP | Company | | | | 3,200.00 | "the website" |
| ENG-2453 | Nathan Price | Build | 2,368.00 | | | | "animation job, coins and chests" |
| ENG-2454 | Martin Walsh ***3801 | Company | | | | BGN 1,999.00 | "paid him direct for his laptop" (equipment, not added to USD) |
| ENG-2455 | [PERSON_7249] Brooks (Lauren) | Marketing | | 500.00 | 1,000.00 | | "she's marketing, not build" |
| ENG-2456 | Ozhan | Build | | 1,000.00 | | | "2D animation"; #art_outsourcing C08FG9924R2 in-game zombies |
| ENG-2457 | [PERSON_9100] | Build | 600.00 | | | | "UX job on the dominoes game" |
| ENG-2458 | [PERSON_0054] [PERSON_0131] | Company | | | | 500.00 | "4X proposal, not one of the three games" |
| ENG-2459 | Oleg | Marketing | 0 | | | | wire back; no receipt in Robert's mail |

Bet boundaries were checked at the edges: no payment on Jan 8/9 2025 (closest Jan 2 and Jan 15) or Nov 23/24 2025 (Nov 12 and Dec 1).

**Cost to build:** DD **959,342.64**, ZM **544,433.44**, CF **72,685.61**. (Marketing DD 16,428.57 / ZM 56,537.06 / CF 1,000; Company 49,625 + BGN 1,999.) Sum check: USD notices 1,667,394.32 + 40,815 adds - 8,157 zeros = 1,700,052.32 = Build 1,576,461.69 + Marketing 73,965.63 + Company 49,625.00 (recomputed).

**Brought in:** REVENUE_DAILY `total_revenue_usd`, 2023-11-01..2026-02-09, summed by `game_id` (grain note in the column comment followed): DD **12,331.25**, ZM **11.99**, CF left off (11.75 recorded; doc "Leave Combo Fighter's revenue off for now, on the page, on the deck and when you tell me"). REVENUE_DAILY_V2 gives the same per-title totals.

**Deck changes for the reply:** slide 3 "$985K/$609K/$74K" -> $959K/$544K/$73K; slide 4 "to fill in" -> DD $12.3K, ZM $12, CF left off.

## Phase 1

| Item | Score | Note |
|---|---|---|
| Persona (1.1) | 5 | Co-founder; Leonard tagged him: "you know what each of these people did better than I do, can you own it?" |
| Competency (1.5) | 5 | Finance: cost-by-bet, revenue reconcile against the bank |
| Task skill (1.5) | 5 | Analysis and synthesis across bank notices, closure statement, WU receipts, warehouse |
| Complexity (1.5) | 5 | Ambiguity Y (rules, buckets in the environment); Dynamic change Y (Leapblock statement, Arthur's email, returned wires beat the first figures); Multi-source Y (Gmail, Slack, GDocs, Linear, Snowflake) |
| Data seeding | 5 | 4 short sentences; operating detail lives in the doc, Slack and Linear |
| Naturalness / AI-text | 5 | "Can you do it for me?" - plain delegation, no enumerated specs, no staged errors |
| Command list / bolt-on / pre-solving / tool mention | PASS | No sequence words beyond "When you're done"; Linear sentence ties to the same doc (not a bolt-on); no figure or cause stated; "Drive", "Linear", "#winddown" are natural service references |
| Diversity | fine | Sheet creation plus share, 22-issue state pass with conditional comments, Slack reply |

## Phase 2.1 Unique Ground Truth

Two-reading tests, one per fork; A = best-supported, B = strongest alternative. Every B is killed by a quoted prompt sentence or Robert-visible record.

| # | Fork | Reading A | Reading B | Settled by (quote) |
|---|---|---|---|---|
| F1 | Leapblock line | 407,944 (statement) | 374,654 (notices, "go by the bank") | Doc: "that beats the notices for them" |
| F2 | $33,290 bet | DD (Sep 2023) | none | statement "from 13 Sep"; Doc "Go by the Transaction Date" |
| F3 | Banco 8605 $4,032 | Out | Stays | Leonard SQL a1488189; Doc "unless one of us has said the money came back" |
| F4 | JPM $4,000 | 0, no bucket, line kept | Company/DD | Arthur's email; Doc "no bucket for that. Every payee keeps its line, even at zero" |
| F5 | Oleg line | 0 | $125 (or $250 with Sep trailer) from the Dixelar mail | Doc "only if a receipt for it reached your mail"; the mail says "requesting a payment ... Pay Now". Request is not a receipt |
| F6 | "your mail" | Robert's | Leonard's or any founder's | Slack to Robert "can you own it"; doc's receipt sentence; Robert's mailbox is what the agent can open |
| F7 | Lucas WU | +7,525 at amount sent | fee-inclusive 7,528.96 | Doc "at the amount sent, not the fee"; receipts Billing Summary |
| F8 | WU "paid out of Chase"? | Counted | Excluded via "Anything paid out of Chase isn't in here" | WU receipts: "Paid with Credit/Debit card MASTERCARD ending in 4655". That card is SVB's: Security Alert from SVC_0227_EMAIL (same sender as "SVB Account Application" threads/00001355) "your ... MasterCard account ending in 4655" (threads/00002502, 00002865), and Robert 2024-06-03 #founders "hey our SVB cards is a credit card, not debit card right?" + reply "yeah, it's credit". Not Chase |
| F9 | Lucas bucket | Build | Company ("wasn't for one of the three games") | ENG-2447 "mini games dev"; #founders 2024-06-14 "build it as a mini game as well in our game"; Doc: "freelancers who made the games" |
| F10 | Node Media bucket | Marketing | Company | Doc "agencies"; Robert's mail 00008689 "ad spend exceeds $100,000", Google Ads manager link 00007026 |
| F11 | Combo Fighter revenue | Omitted (sheet, deck, reply) | Reported since the prompt says "each bet" | Doc: "Leave Combo Fighter's revenue off for now, on the page, on the deck and when you tell me" |
| F12 | Which revenue table | REVENUE_DAILY | REVENUE_DAILY_V2 | Same result per title (12,331.25 / 11.99 / 11.75); immaterial |
| F13 | Singular bucket | Company | Marketing | ENG-2443 "attribution tool, not one game"; Doc "Company is legal, tools" |
| F14 | Payments in the Company column or bet columns | Company (Singular etc.) out of bets | By-date in bet columns | Doc: "that goes in the Company column" |
| F15 | Martin laptop | Company, BGN 1,999 | ZM build / converted | Comment "for his laptop"; Doc equipment + "stays in its own currency" |
| F16 | Reply destination | #winddown | DM/thread elsewhere | Prompt "reply to him in #winddown"; Slack "tell me here" |
| F17 | Deck write | None | Edit deck | Slack "I'll update it myself"; prompt "what changes on the draft deck" |
| F18 | Issue comments | 5 issues | All 22 or none | Doc "If your figure isn't what the notices add up to, say why on the issue first"; figures equal the notices on the other 17 |

Census of open-ended rules (all complete over the Robert-visible universe):

- "says the money came back": Slack search ("came back", returned, bounced, refund, reversed, recall, wrong account) over all channels: only the Apr 2024 8605 note (base + SQL) and ENG-2459 (Oleg). Gmail Robert: no "wire returned" mail. The bank's `Wire Returned` notice for Oleg ($125) sits only in Leonard's mailbox; ENG-2459 is the visible statement of the same fact.
- "closes out their file and tells us what they received": SQL Leapblock message only. Slack 2026-*, Gmail Robert ("for your records", "close out", "final statement", "closed the file") returned no other payee statement.
- "paid some other way / receipt reached your mail": Robert's mail census across Western Union, Payoneer, Wise, PayPal, Zelle, Revolut, Venmo, receipts: 5 WU transfers to Lucas (2 mails each: ready for pickup + received) and 2 Payoneer requests. No other contractor receipt. "ready for pickup" and "received" are the same five MTCNs, so count is five.
- Non-USD: 1 notice set (Martin BGN 1,999, ***3801).
- Payee completeness: 23 notice accounts map to the 22 issues (Banco has two accounts on ENG-2442); every issue maps to a notice account.
- Notices vs Awaiting/Scheduled: every Awaiting/Scheduled payment has a matching Processed notice (same account and amount, within 16 days) except the Leapblock $33,290, the one the statement supplies.
- Bet boundary edges: no payment within 5 days of either cutoff.

UGT verdict: **PASS (5)** on the record above. Every fork resolved by a quoted prompt sentence or a Robert-visible record; no both-fair figure needed.

## Phase 2.2 Feasibility

Tools (catalog.json): `gmail_*` search/read; `slack_*` read/send_message; `gdocs_*`/`gdrive_*`/`gsheets_*` read; `gsheets_create_spreadsheet`, `gdrive_share_file`; `linear_update_issue`, `linear_create_comment`; `snowflake_execute_query`. No unsupported output format.

Data reachable as Robert (ACL): 132 SVB notices delivered to robert@ (all recipients lists include him); WU mail, Payoneer requests, Arthur's email, Node Media forwards in his mailbox; #winddown, #admin_foundersonly, #leapblock, #founders, #art_outsourcing, #video_editing_oleg member (persona_view YES); Drive doc/sheet/deck shared with robert@ in SQL; Linear, Snowflake unscoped. Numeric observability: amounts and Transaction Dates are plain text in notice bodies; WU "Transfer amount" and Billing Summary plain text; Snowflake `total_revenue_usd` at source precision (rendering not observed, evidence limit). Dimensional breakdown: game_id/title_id present; bet by Transaction Date present.

**Feasibility 5; Persona ACL 5.**

## Phase 2.3 Truthfulness

| Claim | Check | Result |
|---|---|---|
| #winddown | Channel C0ADGSZKR3R name "winddown" | Yes |
| "On Thursday" | fa707da5 at 2026-02-13T01:23:41Z = Thursday 2026-02-12 17:23 Pacific (Robert's and Leonard's Slack timezone America/Los_Angeles). deep_recheck: one instant whose Pacific and UTC day differ, either accepted | Pass |
| "his angel calls on Tuesday" | Leonard: "before I start the angel calls on tuesday"; GCal evt 2026-02-17T17:00Z Tue | Yes |
| "one straight page ... what each bet cost us to build and what it brought in" | fa707da5 near-verbatim | Yes |
| "He laid out how he wants it counted and how it should look" | Doc + "use the layout of my Angel note working sheet" | Yes |
| "Payee history project in Linear" | SQL linear_projects name "Payee history", team_ENG | Yes |
| Blake | arthur.blake@harmonygames.co, called Blake throughout Slack (e.g. C04UEQVDVB7 2024-04) | Yes |
| draft deck | "Note to angels (draft)" | Yes |
| Shutdown premise | Task is wind-down work after Feb 11; consistent | Yes |

No tight-identifier error. **Truthfulness 5.**

## Phase 2.4-2.9

- Cross-service (2.4): Gmail (notices, WU, Arthur) changes figures; Linear (buckets, ENG-2459 return) changes lines; Slack (Leapblock statement, 8605) changes figures; GDocs rules decide everything; Snowflake supplies revenue. Writes in GSheets/GDrive, Linear, Slack. 5.
- Investigation + action (2.5): 5.
- Clarity (2.6): one write set under every reading tested; no "I'll X" delegation; 5.
- Contrived (2.7): no exact timestamps, opaque IDs, register triggers, trap hints, hidden destinations, if-chains. 5.
- Date alignment (2.8): 5.
- Originality (2.9): N/A, no samples supplied.

## Phase 3

Data exists: all entities retrievable (Slack, Gmail, GDocs/Sheets/Slides, Linear, Snowflake tools). 5.

Cross-Service Coherence (task-touched data): checked chronology (Linear 23:13-00:58Z before Slack 01:23Z; doc modified 00:41Z before "the doc I just wrote"); Leapblock statement sums (104,868+232,726+62,950+7,400 = 407,944; 29 notices + 33,290 = 30 wires); quick numbers on the sheet and deck match notices-by-date exactly; authors are channel members (Leonard in C0ADGSZKR3R/C04UEQVDVB7, EMPLOYEE_0024 in C05URGU759U); Leapblock message 08:37Z is before the Slack cut (NB-6 10:03Z); Lauren contact email matches Slack users (lauren@harmonygames.co); Node Media invoices sum to 16,428.57; Oleg's wire return is corroborated by the bank's own notice in Leonard's mail; 8605 return corroborated by base Slack; Arthur's email and Leonard's reply are coherent with ENG-2450.
Inconsistencies found: **none** on the records this answer depends on. Score **5**, subject to Eval 0 (STEP 0.5 pending).

## Phase 4 Scoring (Phases 1-4)

| Dimension | Score |
|---|---|
| Unique Ground Truth | 5 |
| Feasibility | 5 |
| Persona ACL Reachability | 5 |
| Explicit Tool Mention | 5 |
| Clarity & Specificity | 5 |
| Contrived / Unnatural | 5 |
| Alignment with Today's Date | 5 |
| Originality | N/A |
| Truthfulness | 5 |
| Tool Use & Cross-service | 5 |
| Investigation + Action | 5 |
| Coherence (Bolt-on) | 5 |
| Persona | 5 |
| Business Function | 5 |
| Assigned Competency | 5 |
| Assigned Task Skill | 5 |
| Complexity & Data Seeding | 5 |
| Data Exists | 5 |
| Cross-Service Coherence | 5 (pending Eval 0) |

Draft verdict (Phases 1-4): **no fail-level finding; PASS pending STEP 0.5 and Phase 5.**

## Findings

None at fail level. Forks F5, F8 and F9 are the ones most likely to be raised at Phase 5; each is settled by the quoted records above.

Evidence limits: Snowflake tool rendering precision not observed (Evals catalog carries no return schema; raw values only). Eval 0 and Phase 5 not run here.
