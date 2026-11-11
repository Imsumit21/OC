# Prompt Brief — robert_seed_bets · prep
> Built 2026-11-08 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (rev6, sha256 ad50f039b5c2; injection stage PASS on this SQL), 03_Error_Async_Config.txt, 01_Scenario_Design.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/truth.json, plan/unresolved.md, plan/research/sc4_habits.md, plan/research/pw1_prompt_lessons.md and the platform /prompt report plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md · Persona view verified: every scoped record is readable by Robert (check-sql PASS for seeded rows, search or can-see for base rows). Exceptions: F21, F26 are readable but a natural search does not reach them, so each is marked NO and routed (§5a, §12) · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · Robert's today: Saturday Feb 14, 2026.
> 04_Prompt.txt is written (109 words, sha256 d0cb08476d23) and unchanged since the platform /prompt review of rev4 (plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md, attempt 6aeed82596dcfe103f9f74d9); plan/prompt_candidate.txt holds the same words. This brief states requirements and quotes the prompt only where a check needs its words.
> The requester skipped the error/async stage. Friction is none, and 03_Error_Async_Config.txt records that with its own gate PASS (digest b51534f72800). There are no reference files: no 02_Reference_Files_Manifest.md exists and 02_Reference_Files/ holds only the template README.

## 1 · Assignment fit

| Axis | Assigned value | What it requires here (cited) |
|---|---|---|
| Business function | Executive | Maps to Founders / Exec / Strategy in `Evals/references/rules/task_categories.md` (strategic decisions, pitches, executive coordination). The work is a founder's account to investors, and that file says a finance task must fit a real person's responsibilities and creates no CFO persona. Reconciliation alone reads as Finance / Legal / HR / Ops, so the investor framing ('angel calls', 'bet', the draft deck) has to stay in the prompt (pw1_prompt_lessons.md row 3). |
| Persona | Robert · robert@harmonygames.co · Co-founder & Creative Director (roster.json persona_key robert, listed there as Co-Founder & Creative Director, department Executive) | Voice: short, plain, first person to his assistant. Remit: Leonard hands it to him by name, 'you know what each of these people did better than I do, can you own it?' (C0ADGSZKR3R/1770945821.640039), and Robert handled contractor payments with his co-founders (C04UEQVDVB7/1732216147.969439). Read scope: his own mailbox and calendar; Drive files he owns or that are shared with him; member of C0ADGSZKR3R (#winddown), C04UEQVDVB7 (#admin_foundersonly), C05URGU759U (#leapblock) and C06MXPL9536; Linear, Trello, Contacts and Snowflake unscoped. |
| Competency | Finance | Taxonomy screen 9: focus budget, forecast, cap table, fundraising; expected outputs models, spreadsheets, decks. Here: an account of how the seed money was spent for the angel calls (evt_f21476dc404329f67fd60d), delivered as a spreadsheet with deck corrections. |
| Task skill | Analysis and synthesis | Taxonomy: combine information from multiple sources and compute, model, reconcile or diagnose to reach findings. Exercised by reconciling the bank notices against the method (f_6feda53b2382c63bf47b25), the payee notes (ENG-2438 to ENG-2459) and the warehouse, then writing the sheet. Stacked: Actions (22 issue closes, the reply). |
| Task type | long-horizon (Long Horizon; difficulty mode easy, V3 cap below 90%) | Measured this run: Gmail 88 threads holding 132 Processed payments; Linear 22 issues and 60 notes, 22 closes and 5 reason comments; Snowflake 2,284 revenue rows; Slack, Docs, Sheets, Slides, Drive, Contacts, Trello and Calendar carry the rest. call_budget 127 (01_Hardness_Manifest.json, requester-confirmed volume and cohort exceptions, floors 120 and 22). HARDNESS GATE (extreme): PASS in the dossier. |

## 2 · Situation

| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |
|---|---|---|---|
| Leonard wants one straight page on what each bet cost to build and what it brought in before his angel calls, and asks Robert to own it. | Robert (mentioned by name) | C0ADGSZKR3R/1770945821.640039, C0ADGSZKR3R/1770945859.212469 | — |
| The only figures so far are Leonard's own quick numbers, and the deck's brought-in slide still says to fill it in. | Robert (shared with him) | f_3304033843904a426f3c00, f_a4b3c4287a4314d8e532e1 | — |
| 22 payee issues sit in Backlog with bank spellings as titles and short notes of what the founders remember. | Robert (Linear, unscoped) | linear:project/0742c172-85de-47ed-a111-316e5c8cb187, ENG-2438 to ENG-2459 | leonard.hayes@harmonygames.co/1798427314394417287, Leonard's mailbox only (can-see NO, pasted in §5a); not needed, §5 F36 and F37 carry what Robert can read |

## 3 · Investigation → action

Questions to resolve (no answers here):
- Who is each payee, where the bank shows a token or another name?
- Which payments count under the method for each payee, and does anything outside the notices belong in?
- Which bucket does each payee fall in?
- Which bet does each counted payment belong to?
- What did each bet cost to build, and what did each bring in?
- Where does a figure differ from what the notices add up to, and why?
- What changes on the draft deck?

Writes those answers feed: the sheet (one row per payee, the bet totals), a reason on each issue whose figure differs, each issue moved to Done, and the reply to Leonard. Every write depends on the investigation.

## 4 · Pinned final state (UGT anchor)

| Deliverable | Required contents | Destination | Recipients | Catalog write | Fed by |
|---|---|---|---|---|---|
| The sheet | one row per payee in the layout of f_3304033843904a426f3c00 (Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note), each bet's build cost and what each bet brought in, with Combo Fighter's left off as the method says | Robert's Drive; his root is d_9f7ba94f7526d54d8482ba | shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co | gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file | every §3 question |
| Payee issues | all 22 moved to Done once the row is right; a reason comment first wherever the figure differs from the notices' sum | linear:project/0742c172-85de-47ed-a111-316e5c8cb187, ENG-2438 to ENG-2459 | read by leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co | linear_create_comment, linear_update_issue | bucket, count and figure questions |
| Reply to Leonard | what each bet cost and brought in (Combo Fighter's left off), what changes on the deck, and the link to the sheet | #winddown C0ADGSZKR3R: a thread under C0ADGSZKR3R/1770945821.640039 or C0ADGSZKR3R/1770945859.212469, or top-level | leonard.hayes@harmonygames.co | slack_send_message | the totals and the sheet |

Alternatives a careful run could defend, each accepted or settled in §4b: a thread under either of Leonard's two posts or a new post in #winddown (C0ADGSZKR3R/1770945859.212469 says 'tell me here'); editing the deck as well as reporting on it, though he says he will update it himself (f_a4b3c4287a4314d8e532e1); a one-page doc beside the sheet (C0ADGSZKR3R/1770945821.640039); where the brought-in figures sit on the sheet, since the layout has no column for them (f_3304033843904a426f3c00); and whether Marketing and Company dollars also fill the bet columns (f_6feda53b2382c63bf47b25).

### 4b · Canonical outcome (all fair outcomes)

| Deliverable | Field | Fixed value (or closed accepted set, with sources) | Delegated by (quoted span, or —) | Allowed equivalence class | Material / representational | Source |
|---|---|---|---|---|---|---|
| Sheet | owner and place | owned by Robert, in his Drive | 'keep yours in your drive' | his root d_9f7ba94f7526d54d8482ba or any folder he owns; not a folder of Leonard's | material (owner) / representational (folder) | C0ADGSZKR3R/1770945859.212469 |
| Sheet | title | — | 'keep yours in your drive' | any title | representational | C0ADGSZKR3R/1770945859.212469 |
| Sheet | columns | Payee · Name on the bank · Bucket · Domino Delights · ZM · Combo Fighter · Company · Note | 'use the layout of my Angel note working sheet' | same columns; extra columns and a totals row free | material (columns) / representational (order) | f_3304033843904a426f3c00 |
| Sheet | rows | 22, one per payee, with the zero rows kept | — | matched on the account ending (NB-12), never on a token name; Payee label free, bank spelling or the name the notes give | material | f_6feda53b2382c63bf47b25, ENG-2438 |
| Sheet | Build rows | ENG-2438 ***8380 Domino Delights 530,736.14, ZM 434,185.44, Combo Fighter 50,425.61; ENG-2439 ***1359 Domino Delights 337,594.00, ZM 59,250.00, Combo Fighter 11,100.00; ENG-2440 ***8501 Domino Delights 45,941.50, ZM 36,070.00, Combo Fighter 11,160.00; ENG-2442 ***3341, 8605 Domino Delights 28,128.00, ZM 8,928.00; ENG-2447 ***6577 Domino Delights 13,975.00; ENG-2449 ***1794 ZM 5,000.00; ENG-2453 ***0148 Domino Delights 2,368.00; ENG-2456 ***3307 ZM 1,000.00; ENG-2457 ***1876 Domino Delights 600.00 | — | to the cent or the whole dollar | material | ENG-2438, f_6feda53b2382c63bf47b25 |
| Sheet | Marketing rows | ENG-2441 ***5000 ZM 46,201.50; ENG-2444 ***0115 Domino Delights 16,428.57; ENG-2448 ***2532 ZM 6,085.56; ENG-2451 ***5660 ZM 3,750.00; ENG-2455 ***5384 ZM 500.00, Combo Fighter 1,000.00 | — | dollars in the bet columns, or in the row with the bet named; kept out of every build total. Marketing total 73,965.63 if shown | material (bucket) / representational (cell) | ENG-2441, f_6feda53b2382c63bf47b25 |
| Sheet | ENG-2459 row | ENG-2459 ***9368 at zero in every money cell, Bucket Marketing | 'Every payee keeps its line, even at zero' | zero or blank cells | material | ENG-2459, f_6feda53b2382c63bf47b25 |
| Sheet | Company rows | ENG-2443 ***4015 Company 31,250.00; ENG-2445 ***7534 Company 7,500.00; ENG-2446 ***7393 Company 7,175.00; ENG-2452 ***4020 Company 3,200.00; ENG-2458 ***3139 Company 500.00 | 'that goes in the Company column' | dollars in the Company column, with or without the same amount in a bet column; Company total 49,625.00 | material (Company figure) / representational (bet cells) | ENG-2443, f_6feda53b2382c63bf47b25 |
| Sheet | Non-dollar row | ENG-2454 ***3801 1,999.00 BGN, on the Company line, never in a dollar total | 'stays in its own currency next to the line' | in the Company cell or that row's Note; '1,999 BGN' or 'BGN 1,999' | material (currency, bucket) / representational (cell) | ENG-2454, f_6feda53b2382c63bf47b25 |
| Sheet | ENG-2450 row | ENG-2450 ***3203 at zero in every money cell | 'Every payee keeps its line, even at zero' | any bucket label that marks it as no cost: 'Not a cost', 'None', blank or similar; zero or blank cells | material (zero) / representational (label) | ENG-2450, f_6feda53b2382c63bf47b25 |
| Sheet | bet totals | build cost Domino Delights 959,342.64 · ZM 544,433.44 · Combo Fighter 72,685.61 | — | a totals row or anywhere on the sheet; the sum of a whole bet column need not equal it, because Marketing or Company cells may sit there | material | f_6feda53b2382c63bf47b25 |
| Sheet | brought in | Domino Delights 12,331.25 · ZM 11.99, as recorded, table totals only. Combo Fighter's is left off: 'Leave Combo Fighter’s revenue off for now, on the page' | 'Leave Combo Fighter’s revenue off for now' | anywhere on the sheet, in any row or tab, because the layout has no column for it. Combo Fighter's cell blank, marked held or 'to come'; a Combo Fighter figure is outside acceptance but nothing grades it (NB-26) | material (figures) / representational (place) | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY, f_6feda53b2382c63bf47b25 |
| Sheet | Note column | a reason on the five rows whose figure differs | — | wording free; the same reason may sit on the issue only | representational | ENG-2439, ENG-2442, ENG-2447, ENG-2450, ENG-2459 |
| Sheet | sharing | leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co | 'share it with Blake and me' | editor, viewer or commenter | material (people) / representational (role) | C0ADGSZKR3R/1770945859.212469 |
| Issues | state | Done on all 22, ENG-2438 to ENG-2459 | — | assignee free | material | f_6feda53b2382c63bf47b25 |
| Issues | reason comment | before Done on ENG-2439, ENG-2442, ENG-2447, ENG-2450 and ENG-2459, the five whose figure differs from the notices' sum | — | wording free; an extra comment on any other issue, such as ENG-2454, is not penalised | material (the five) / representational (wording) | f_6feda53b2382c63bf47b25 |
| Reply | destination | #winddown C0ADGSZKR3R | — | a thread under C0ADGSZKR3R/1770945821.640039, a thread under C0ADGSZKR3R/1770945859.212469, or a top-level post | material (channel) / representational (placement) | C0ADGSZKR3R/1770945859.212469 |
| Reply | what each bet cost | 959,342.64 · 544,433.44 · 72,685.61 | — | exact, whole dollars, or rounded ($959K, $544K, $73K; $0.96M, $0.54M; $72.7K) | material (figure) / representational (rounding) | f_6feda53b2382c63bf47b25 |
| Reply | what each brought in | Domino Delights 12,331.25 · ZM 11.99; Combo Fighter's left off ('and when you tell me') | 'Leave Combo Fighter’s revenue off for now' | exact, or rounded ($12.3K, $12); Combo Fighter's omitted, marked held or 'to come'; a Combo Fighter figure is outside acceptance but nothing grades it | material (figure) / representational (rounding) | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY, f_6feda53b2382c63bf47b25 |
| Reply | what changes on the deck | the three cost figures ($985K, $609K, $74K) move to the new ones, and the brought-in slide gets Domino Delights and ZM, with Combo Fighter left off | 'what changes on the deck' | any wording; Marketing and Company totals optional | material | f_a4b3c4287a4314d8e532e1 |
| Reply | link | a link to the sheet | — | a Drive or Sheets URL | material | C0ADGSZKR3R/1770945859.212469 |
| Deck | edit | left unchanged: 'I’ll update it myself' | 'what changes on the deck, I’ll update it myself' | an edit to the deck is not penalised | representational | f_a4b3c4287a4314d8e532e1, C0ADGSZKR3R/1770945859.212469 |
| Trello card | state | left untouched: no write is asked of it | — | — | representational | 698e55f9af74d68d679de7b3 |

## 5 · Discovery map

Root causes and findings appear here and nowhere earlier, and never in the prompt. Rows marked 'settled at the platform /prompt' cite the deep-recheck forks of plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md (attempt 6aeed82596dcfe103f9f74d9, rev4 SQL 872bbb307710), which found each settled by a record Robert can see; rev6 changes none of those records.

| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |
|---|---|---|---|---|---|---|
| F1 Leonard's ask, first post | wants one page on what each bet cost and brought in; names the doc | C0ADGSZKR3R/1770945821.640039 | YES (#winddown; check-sql) | met first (anchor AN1) | — | Yes (AN1) |
| F2 Leonard's ask, second post | the project, the layout, his Drive, who to share with, where to report, and that he will update the deck himself | C0ADGSZKR3R/1770945859.212469 | YES (#winddown; check-sql) | met second; a run that reads only the first post misses the deliverables | the words 'more below' are the only pointer to it | Yes (AN1) |
| F3 the method | every counting rule, including 'that beats the notices for them', 'move each payee's issue to Done' and 'say why on the issue first' | f_6feda53b2382c63bf47b25 | YES (shared; check-sql) | named by F1; replaces F9 | — | No (F1 names it) |
| F4 the working sheet | the layout; its row is a quick pass, 984,888.21 / 608,820.50 / 73,685.61, every notice by date | f_3304033843904a426f3c00 | YES (shared; check-sql) | overturned by F3 for the figures, kept for the layout | figures copied as truth | No |
| F5 the draft deck | $985K, $609K, $74K; brought-in slide empty | f_a4b3c4287a4314d8e532e1 | YES (shared; check-sql) | overturned by the sheet's results | — | No |
| F6 the project | 'One issue per payee on the SVB notices' | linear:project/0742c172-85de-47ed-a111-316e5c8cb187 ENG-2438 | YES (unscoped) | named by F2 | — | Yes (AN2) |
| F7 the 22 issues | bank spellings and account endings; state Backlog | ENG-2438 to ENG-2459 | YES (unscoped) | — | 12 titles carry tokens (NB-12) | No |
| F8 the 60 notes | what the founders remember, including ENG-2443 'attribution tool, not one game' (with F3's 'tools' it closes Singular as Company) and ENG-2457 'second half of the UX job on the dominoes game'; the notes on ENG-2454 and ENG-2455 are F31 and F39 | ENG-2443, ENG-2457 and every issue's comments | YES (unscoped) | read per issue | comments are not searchable, one read per issue | No |
| F9 the quick plan card | 'add up the notices by date and round them' | 698e55f9af74d68d679de7b3 | YES (unscoped) | overturned by F3 ('replaces the quick plan') and the card's comment | first hit on the board | No |
| F10 the angel calls | Tue Feb 17, 2026, 9:00 to 10:30 PT (17:00 to 18:30Z) | evt_f21476dc404329f67fd60d | YES (own calendar; check-sql) | — | — | No (the prompt may say Tuesday) |
| F11 the notices | 132 Processed payments in 88 threads, 131 USD and 1 BGN, Sep 5, 2023 to Feb 2, 2026 (re-derived this run, VERIFY lines in §5a) | robert@harmonygames.co/1776227799449805411 | YES (his mailbox) | named by F3 | several payments per thread; bodies need a full read | No |
| F12 the ***8605 notice | $4,032.00 Processed Apr 2, 2024. Root cause, never in the prompt: this wire went to a bad account number and came back | robert@harmonygames.co/1795282860741136988 | YES (his mailbox) | met first / overturned by F13 and F14; settled at the platform /prompt, fork F2 | the bank says Processed | No |
| F13 the Apr 5, 2024 exchange | 'This wire didn’t go through', 'I think I messed up the bank account number', 'Fixed up and resubmitted the payment' | C04UEQVDVB7/1712331142.975829 C04UEQVDVB7/1712331372.614469 C04UEQVDVB7/1712331718.859679 | YES (#admin_foundersonly member) | overturns F12; settled at the platform /prompt, fork F2 | no run has read a founder channel; 0 of 24 followed a hit into its neighbours (sc4 §3) | No |
| F14 the Apr 12, 2024 note | 'bank returned our money': MotMot nets $37,056.00, not $41,088.00 | C04UEQVDVB7/1712901800.684259 C04UEQVDVB7/1712901837.860709 | YES (#admin_foundersonly member) | overturns F12; settled at the platform /prompt, fork F2 | 'returned' was searched 0 of 147 times (sc4 §3) | No |
| F15 the Recipient Modified mail | account ***3341 set Apr 5, 2024, 15:40Z, after the ***8605 wire and before the resend at 16:02Z | robert@harmonygames.co/1795509850966005840 | YES (his mailbox) | sits between F12 and the resend | — | No |
| F16 the off-bank route | Robert paid the mini games dev by company card before the bank had him | C04UEQVDVB7/1719603220.131689 C04UEQVDVB7/1719603590.685019 C04UEQVDVB7/1719603595.852129 | YES (#admin_foundersonly member) | overturns the ENG-2447 note ('the bank has him from Sep 2024' read as the whole story) | the 'Lucas' hit needs a read around it | No |
| F17 the first receipt | Western Union, Jun 3, 2024, $1,075.00 | robert@harmonygames.co/1800873055214061794 | YES (his mailbox) | admitted by F3's receipt sentence; settled at the platform /prompt, fork F6 | 68 hits; only 2 of 5 receipts inside the limit | No |
| F18 all five receipts | $7,525.00 sent to [PERSON_NAME_36400], the token on ENG-2447: Lucas totals $13,975.00. Thread 1802092844284446043 also holds a Fwd of its own receipt, same tracking number, so a per-message sum gives $8,600.00, wrongly | robert@harmonygames.co/1800873055214061794 robert@harmonygames.co/1802092844284446043 robert@harmonygames.co/1803223458475671884 robert@harmonygames.co/1805405368810910191 robert@harmonygames.co/1808201559428745555 | YES (his mailbox) | overturns the $6,450.00 notice sum; settled at the platform /prompt, fork F6 | the forwarded copy double counts | No |
| F19 Leapblock's statement | 30 wires, $407,944; the first one 33,290. F3: closing a file and saying what they received 'beats the notices' | C05URGU759U/1770971846.479179 | YES (#leapblock member; check-sql) | overturns the notices' $374,654.00; settled at the platform /prompt, fork F3 | a Feb 13 post in a channel runs read only by name | No |
| F20 the Awaiting notice | $33,290.00, Sep 13, 2023, no Processed notice follows | robert@harmonygames.co/1776934359028762037 | YES (his mailbox) | a Processed-only read never sees it; settled at the platform /prompt, fork F3 | — | No |
| F21 Arthur's 'Done!' | the approval run on Sep 13, 2023; corroborates F19 and F20, which settle the figure without it | C04UEQVDVB7/1694616691.082479 C04UEQVDVB7/1694616951.239909 | YES (#admin_foundersonly member) | — | the post names no payee and no amount | No |
| F22 Arthur's Chase mail | the $4,000 went to the company's own Chase account, so it never left the company | robert@harmonygames.co/<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com> | YES (his INBOX; check-sql) | overturns F24 and the ENG-2450 note; settled at the platform /prompt, fork F4 | subject is about Chase, not the payee | No |
| F23 Leonard's reply | 'ah that’s the one I couldn’t place, thanks' | robert@harmonygames.co/<CAPBs_a5xhlLhxf4uFEerJEygHD5CJ2ob3qegV9nV-erG4foiIU@mail.gmail.com> | YES (his INBOX; check-sql) | confirms F22 | — | No |
| F24 the JPMorgan notice | $4,000.00, Aug 19, 2024, ***3203 | robert@harmonygames.co/1807851044809802572 | YES (his mailbox) | met first / overturned by F22; settled at the platform /prompt, fork F4 | — | No |
| F25 Chase is the company's | 'Chase account closed. Cashiers check deposited into SVB.' Oct 31, 2025: Chase was a company account, still open in Aug 2024 | C04UEQVDVB7/1761954952.006759 | YES (#admin_foundersonly member) | supports F22 | — | No |
| F26 the post naming Node Media | 'closing our account with Node Media LLC', Jan 2, 2025 | C04UEQVDVB7/1735854841.070019 | YES (#admin_foundersonly member) | gives the display name only; F27 settles the bucket | the note's wording differs from the post's | No |
| F27 the agency's invoice mail | invoices for services with an ad-spend clause: Marketing, not Build | robert@harmonygames.co/1815095592611804295 | YES (his mailbox) | overturns a by-date Build reading of PERSON_4419_NAME LLC; settled at the platform /prompt, fork F7 | the name is a token in mail | No |
| F28 the contact row | Lauren Brooks, Telegram Contractor | 564155d70112411151e512a6 | YES (unscoped) | spells the name the notices token out | — | No |
| F29 her contract | Exhibit A opens 'plan, launch, and scale Telegram distribution': with F39 and F38 it closes ENG-2455 as Marketing, not Build | f_20a0df3860bb5731d22f07 | YES (shared) | overturns a by-date Build reading of ENG-2455 | the note says only 'the contract' | No |
| F30 the BGN notice | 1,999.00 BGN, Oct 30, 2025 | robert@harmonygames.co/1847427662807006290 | YES (his mailbox) | a USD-only parser drops or adds it | 'BGN' alone is past the limit | No |
| F31 Martin's note on ENG-2454 | 'paid him direct for his laptop, not through Leapblock': equipment, so Company. #admin_foundersonly agrees: 'did you handle Martin’s laptop?', then 'we are doing that as direct wire' | ENG-2454 (comment_e89f05a3984064bdb00bc2b1fe6ffee2) C04UEQVDVB7/1761844454.096829 C04UEQVDVB7/1761844624.408899 | YES (unscoped; the exchange: #admin_foundersonly member) | overturns a Build reading of the payment, which the platform report made on the older note (its F10 row) | a note read per issue | No |
| F32 lifetime revenue | Domino Delights 12,331.25 · ZM 11.99, 2,284 rows; REVENUE_DAILY_V2 equal (summed this run). F3 holds Combo Fighter's figure off the page, the deck and the reply, so it is no value here (NB-26; platform I3) | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY | YES (unscoped) | named by role in F3 | a run may report Combo Fighter's anyway | No |
| F33 the P&L | monthly lines, no per-payee figures; a decoy, not called wrong by F3 | f_605121f4a36752645e0ac3 | YES (shared) | F3 sends the count to the notices instead | NB-2: no P&L cost is graded | No |
| F34 the balance posts | 'discrepancy between the cash in bank' and 'matching what banks say' concern balances, not payees | C04UEQVDVB7/1754445622.992119 C04UEQVDVB7/1754445718.724799 | YES (#admin_foundersonly member) | distractor | — | No |
| F35 the Leapblock MSA | the saga map work: Build | f_322bbfdb37d253aa8624b9 | YES (shared) | supports the ENG-2439 notes | — | No |
| F36 Leonard's third note on ENG-2459 | 'that wire came back the same day, I’d already re-sent it through payoneer': F3's test takes the $125.00 notice out, and the Payoneer route then needs a receipt in Robert's mail (F37) | ENG-2459 (comment_3906b5b40dfcdabdc83381f0060bac82) | YES (unscoped) | overturns the $125.00 notice. C06MXPL9536/1715113013.494939 and C06MXPL9536/1715064961.427529 agree but are not needed; settled at the platform /prompt, fork F5 | a note read per issue; the run must then look for a receipt | No |
| F37 no receipt for the re-send | Robert's mail holds only two 'Dixelar sent you a payment request' mails, May 5 and Sep 25, 2024. A request is not a receipt, so the line is zero with a reason and Marketing stays its bucket. The Payoneer receipts are in Leonard's mailbox only, and Robert's mail has no Upwork receipt either (census and positive control, VERIFY lines in §5a) | robert@harmonygames.co/1798239548116390324 robert@harmonygames.co/1811158112675912556 | YES (his mailbox) | closes F36's route under F3's receipt sentence; settled at the platform /prompt, fork F5 | a request can be misread as a receipt; the absence is shown only by searching | No |
| F38 her role post | 'She will lead our Telegram distribution strategy', Oct 10, 2025 | C05KNDCHAAG/1760125440.959149 | YES (#company-internal member) | with F39 and F29 closes ENG-2455 as Marketing | — | No |
| F39 Leonard's third note on ENG-2455 | 'her contract had her running our paid UA on telegram, so she’s marketing, not build' | ENG-2455 (comment_990674712ad0127e26f780eadb5418ea) | YES (unscoped) | settles the bucket the platform found open (UGT 2, Clarity 1; plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md I1, attempt 6aeed82596dcfe103f9f74d9); F29 and F38 agree | a note read per issue | No |

## 5a · Search-as-persona proof

Every query uses only what an agent knows at that step: the prompt, an issue title or note, or a record already found. A verbatim quote from a target does not count as a natural query. Seeded records never appear in `persona_view.py search`, which reads base data only: those rows are counted from the SQL overlay and proven by `check-sql`, and each says so. Limits of the proof: the tool matches a contiguous phrase, so a multi-word query can return 0 where a live search might not ('Martin laptop' 0, 'Martin’s laptop' 1), and it lists oldest first where live Slack lists newest first (sc4 §3), so limit 10 is not the live ranking.

| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |
|---|---|---|---|---|---|---|
| F1 | slack | angel calls (from the prompt's own words) | 0 base + 1 seeded | 0 | C0ADGSZKR3R/1770945821.640039 | YES (seeded: base search cannot show it; check-sql YES) |
| F2 | slack | Payee history (named in the prompt) | 0 base + 1 seeded | 0 | C0ADGSZKR3R/1770945859.212469 | YES (seeded: base search cannot show it; check-sql YES) |
| F3 | gdocs | how to count the money (title quoted by F1) | 0 base + 1 seeded | 0 | f_6feda53b2382c63bf47b25 | YES (seeded: base search cannot show it; check-sql YES) |
| F4 | gsheets | Angel note working (title quoted by F2) | 0 base + 1 seeded | 0 | f_3304033843904a426f3c00 | YES (seeded: base search cannot show it; check-sql YES) |
| F5 | gslides | angels (F2 says the draft deck; one word of its subject) | 4 base + 1 seeded | 0 | f_a4b3c4287a4314d8e532e1 | YES (seeded: base search cannot show it; check-sql YES) |
| F6 | linear | Payee history (named in the prompt) | 0 base + 1 seeded | 0 | 0742c172-85de-47ed-a111-316e5c8cb187 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F7 | linear | SVB notices (the project description's words) | 0 base + 23 seeded | 0 | ENG-2438 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F8 | linear | Singular Labs (an issue title; its notes are read per issue, comments are not searched) | 0 base + 1 seeded | 0 | ENG-2443 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F9 | trello | Angel note (F3 says the plan is on the board) | 0 base + 1 seeded | 0 | 698e55f9af74d68d679de7b3 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F10 | gcal | Angel calls (F1's words) | 0 base + 1 seeded | 0 | evt_f21476dc404329f67fd60d | YES (seeded: base search cannot show it; check-sql YES) |
| F11 | gmail | Payment Processed (named by F3) | 88 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1776227799449805411 | YES (base hit) |
| F12 | gmail | BANCO DE AMERICA (the title of ENG-2442) | 29 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1795282860741136988 | YES (base hit) |
| F13 | slack | MotMot (the payee in the ENG-2442 note; the hit sits inside the exchange) | 34 base + 0 seeded | 27 | C04UEQVDVB7/1712331372.614469 | YES (base hit; the hit sits in the exchange; the two target posts are its neighbours, reached by reading around it) |
| F14 | slack | wrong account (two account endings on ENG-2442 prompt the words) | 3 base + 0 seeded | 5 | C04UEQVDVB7/1712901800.684259 | YES (base hit) |
| F15 | gmail | BANCO DE AMERICA (same search as F12) | 29 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1795509850966005840 | YES (base hit) |
| F16 | slack | Lucas (the name in the ENG-2447 note; the hit sits inside the exchange) | 184 base + 0 seeded | 43 | C04UEQVDVB7/1719603220.131689 | YES (base hit; the hit sits in the exchange; the target post follows it the same day, reached by reading around it) |
| F17 | gmail | Western Union (the service named in Slack; 2 of 5 receipts inside the limit) | 68 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1800873055214061794 | YES (base hit) |
| F18 | gmail | ready for pickup (the subject line F17 shows; lists all 5) | 5 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1808201559428745555 | YES (base hit) |
| F19 | slack | Leapblock (the title of ENG-2439) | 175 base + 1 seeded | 43 | C05URGU759U/1770971846.479179 | YES (seeded: base search cannot show it; check-sql YES) |
| F20 | gmail | Leapblock LTD (the title of ENG-2439) | 74 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1776934359028762037 | YES (base hit) |
| F21 | slack | Leapblock payment (the payee plus the plain word) | 3 base + 0 seeded | 1 | C04UEQVDVB7/1718839744.677849 | NO — routed to /create-injection (§12): no natural query reaches it; F19 and F20 settle the figure without it |
| F22 | gmail | JPMorgan (the title of ENG-2450) | 18 base + 2 seeded | n/a (--no-hidden) | robert@harmonygames.co/<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com> | YES (seeded: base search cannot show it; check-sql YES) |
| F23 | gmail | JPMorgan (same search; it quotes F22) | 18 base + 2 seeded | n/a (--no-hidden) | robert@harmonygames.co/<CAPBs_a5xhlLhxf4uFEerJEygHD5CJ2ob3qegV9nV-erG4foiIU@mail.gmail.com> | YES (seeded: base search cannot show it; check-sql YES) |
| F24 | gmail | JPMorgan (the title of ENG-2450) | 18 base + 2 seeded | n/a (--no-hidden) | robert@harmonygames.co/1807851044809802572 | YES (base hit) |
| F25 | slack | Chase account (F22's own words) | 7 base + 0 seeded | 0 | C04UEQVDVB7/1761954952.006759 | YES (base hit) |
| F26 | slack | closed the account (the ENG-2444 note's own words) | 0 base + 0 seeded | 0 | — | NO — routed to /create-injection (§12): the note's own words return nothing and the name can't be formed cold; F27 settles the bucket |
| F27 | gmail | PERSON_4419_NAME (the title of ENG-2444) | 6 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1815095592611804295 | YES (base hit) |
| F28 | contacts | Brooks (the title of ENG-2455) | 2 base + 1 seeded | 0 | 564155d70112411151e512a6 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F29 | gdocs | Lauren Brooks (the name F28 gives) | 1 base + 0 seeded | 0 | f_20a0df3860bb5731d22f07 | YES (base hit) |
| F30 | gmail | ***3801 (the account ending on ENG-2454) | 3 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1847427662807006290 | YES (base hit) |
| F31 | linear | Walsh (the title of ENG-2454; its notes are read per issue) | 10 base + 1 seeded | 0 | ENG-2454 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F32 | snowflake | REVENUE_DAILY (F3 names the table by role) | 10 base + 0 seeded | 0 | ANALYTICS.MONETIZATION.REVENUE_DAILY | YES (base hit) |
| F33 | gsheets | P&L (plain word) | 8 base + 0 seeded | 12 | f_605121f4a36752645e0ac3 | YES (base hit) |
| F34 | slack | cash in bank (plain words; the next post is the other half) | 1 base + 0 seeded | 0 | C04UEQVDVB7/1754445622.992119 | YES (base hit) |
| F35 | gdocs | Saga Map (the ENG-2439 note's words) | 10 base + 0 seeded | 34 | f_322bbfdb37d253aa8624b9 | YES (base hit) |
| F36 | linear | Private Entrepreneur (the title of ENG-2459; its notes are read per issue) | 0 base + 1 seeded | 0 | ENG-2459 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |
| F37 | gmail | Payoneer (the F36 note's own word) | 2 base + 0 seeded | n/a (--no-hidden) | robert@harmonygames.co/1798239548116390324 | YES (base hit) |
| F38 | slack | Telegram distribution (the words of F29's Exhibit A) | 1 base + 0 seeded | 0 | C05KNDCHAAG/1760125440.959149 | YES (base hit) |
| F39 | linear | Brooks (the title of ENG-2455; its notes are read per issue) | 3 base + 1 seeded | 0 | ENG-2455 | YES (seeded: base search cannot show it; unscoped, in the SQL overlay) |

Outputs verbatim, then the check-sql rows for these facts, the can-see lines and this run's VERIFY lines:
```
SEARCH slack 'angel calls' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH slack 'Payee history' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gdocs 'how to count the money' as robert  scope: GDocs title + body_text
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gsheets 'Angel note working' as robert  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gslides 'angels' as robert  scope: GSlides title + page element text
visible hits=4 (showing 4)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_65ada5e24989d256cabdfa", "name": "Harmony Games BoD Jan 14 2026", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "ent  Bridge round offered to all existing investors and new angels Investors who participate main
  {"id": "f_6f5a82695950374e9d58f3", "name": "Harmony Games Pitch Dec 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "cap table with [PERSON_NAME_2000], founders  ●  , and a few angels.  [PERSON_NAME_2000] committed to
  {"id": "f_9312d5e8a2d0205f7b4a24", "name": "Harmony Games Pitch Oct 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "cap table with [PERSON_NAME_2000], founders  ●  , and a few angels.  [PERSON_NAME_2000] committed to
  {"id": "f_b4f48a356b22b09812ad2b", "name": "Harmony Games Pitch Nov 25", "mime": "application/vnd.google-apps.presentation", "why": "file is shared with the persona (shared_with_emails)", "snippet": "cap table with [PERSON_NAME_2000], founders  ●  , and a few angels.  [PERSON_NAME_2000] committed to

SEARCH linear 'Payee history' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH linear 'SVB notices' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH linear 'Singular Labs' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH trello 'Angel note' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gcal 'Angel calls' as robert  scope: GCal event summary (base events carry no description/location)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
note: counted per meeting instance (ical_uid + start), visible if any copy is visible

SEARCH gmail 'Payment Processed' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=88 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1776227799449805411", "last": "2023-09-05T19:40:31Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1778183297904473683", "last": "2023-09-27T09:42:16Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1778675214290918178", "last": "2023-10-02T20:01:07Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1779362835587714091", "last": "2023-10-10T10:10:33Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1780927524744938453", "last": "2023-10-27T20:00:59Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1781216944848716116", "last": "2023-10-30T21:20:50Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1781374231721722365", "last": "2023-11-01T16:22:21Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1781472945910297699", "last": "2023-11-02T17:09:52Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1784016683763338498", "last": "2023-11-30T21:40:28Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
  {"id": "robert@harmonygames.co/1784385347612012667", "last": "2023-12-04T20:41:14Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "SVB Payment Notification: Payment Processed"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'BANCO DE AMERICA' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=29 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1795166906688019939", "last": "2024-04-01T20:49:16Z", "subject": "Invoice: Contractor [PERSON_NAME_1900] March 2024", "snippet": "n banks: [BANK_ACCOUNT_NUMBER_0094]  Beneficiary Bank Name: BANCO DE AMERICA CENTRAL,S.A.  Beneficiary Bank Address: 55 Av. Entre Calle Roo
  {"id": "robert@harmonygames.co/1795182296548841984", "last": "2024-04-02T00:53:49Z", "subject": "SVB Payment Notification: Recipient Created", "snippet": "can now initiate payments to this recipient.Recipient Name: BANCO DE AMERICA ***8605Created by: Arthur [PERSON_NAME_17939] view the Recipient det
  {"id": "robert@harmonygames.co/1795182318659688694", "last": "2024-04-02T00:54:28Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***8605Amount: 4,032.00 USDTransaction Date: Apr 02 2024Tran
  {"id": "robert@harmonygames.co/1795182749681334173", "last": "2024-04-02T01:01:19Z", "subject": "SVB Payment Notification: Payment Scheduled", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***8605Amount: 4,032.00 USDTransaction Date: Apr 02 2024Transaction 
  {"id": "robert@harmonygames.co/1795282860741136988", "last": "2024-04-03T03:32:33Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***8605Amount: 4,032.00 USDTransaction Date: Apr 02 2024Transaction 
  {"id": "robert@harmonygames.co/1795509850966005840", "last": "2024-04-05T15:40:27Z", "subject": "SVB Payment Notification: Recipient Modified", "snippet": "can now initiate payments to this recipient.Recipient Name: BANCO DE AMERICA  ***3341Created by: Arthur [PERSON_NAME_91976] by: Arthur [PERSON_N
  {"id": "robert@harmonygames.co/1795510012758086524", "last": "2024-04-05T15:43:01Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: Apr 05 2024Tran
  {"id": "robert@harmonygames.co/1795511257876658998", "last": "2024-04-05T16:02:49Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: Apr 05 2024Transaction 
  {"id": "robert@harmonygames.co/1797806674476915535", "last": "2024-05-01T02:54:50Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: May 01 2024Tran
  {"id": "robert@harmonygames.co/1797816647013177532", "last": "2024-05-01T03:02:44Z", "subject": "SVB Payment Notification: Payment Scheduled", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: May 01 2024Transaction 
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'MotMot' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=34 (showing 10)  hidden by ACL=27 in 14 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1712331372.614469", "channel": "admin_foundersonly", "kind": "private", "date": "2024-04-05", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "thats the motmot one?"}
  {"id": "C04UEQVDVB7/1718575865.167309", "channel": "admin_foundersonly", "kind": "private", "date": "2024-06-16", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": " set up a reminder “pay motmot for May” in this channel at 9AM tomorrow, Eastern Daylight Time."}
  {"id": "C04UEQVDVB7/1718629238.456309", "channel": "admin_foundersonly", "kind": "private", "date": "2024-06-17", "user": "PERSON_6089_SLACK_ID", "reply": false, "snippet": "reminder: pay motmot for May."}
  {"id": "C04UEQVDVB7/1730393083.619159", "channel": "admin_foundersonly", "kind": "private", "date": "2024-10-31", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "xtra days [PERSON_NAME_0550] spent this month then I can do MotMot."}
  {"id": "C04UEQVDVB7/1733160392.546119", "channel": "admin_foundersonly", "kind": "private", "date": "2024-12-02", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "Ok approved.  Can one of you approve the MotMot and Deel payments now"}
  {"id": "C04UEQVDVB7/1735240619.835039", "channel": "admin_foundersonly", "kind": "private", "date": "2024-12-26", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "I think we wait on MotMot payment until we know the number of hours for [PERSON_NAME_0550]. He's putting "}
  {"id": "C04UEQVDVB7/1735240662.204909", "channel": "admin_foundersonly", "kind": "private", "date": "2024-12-26", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "yeah, we can do motmot and leapblock when they arrive"}
  {"id": "C04UEQVDVB7/1736978214.260099", "channel": "admin_foundersonly", "kind": "private", "date": "2025-01-15", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "Just put the MotMot payment into SVB. Needs approval. [PERSON_NAME_24716] worked 4 extra days OT fo"}
  {"id": "C04UTBZL6AX/1705615960.209809", "channel": "founders", "kind": "private", "date": "2024-01-18", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Also love their name. Motmot "}
  {"id": "C04UTBZL6AX/1705618964.457719", "channel": "founders", "kind": "private", "date": "2024-01-18", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I got an invite from Motmot studios? But I don't have iOS device readily available =\\"}

SEARCH slack 'wrong account' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=5 in 3 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1712901800.684259", "channel": "admin_foundersonly", "kind": "private", "date": "2024-04-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "this is money returned to us because Blake put the wrong account number to pay up [PERSON_NAME_24716] and bank returned our 
  {"id": "C050WGU41HR/1738791645.030739", "channel": "engineering-bots", "kind": "private", "date": "2025-02-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I bought it under the wrong account though. You need to rebuy it under your account "}
  {"id": "C05H8KVNU67/1713979784.963319", "channel": "game-design", "kind": "private", "date": "2024-04-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "created meeting with wrong account"}

SEARCH gmail 'BANCO DE AMERICA' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=29 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1795166906688019939", "last": "2024-04-01T20:49:16Z", "subject": "Invoice: Contractor [PERSON_NAME_1900] March 2024", "snippet": "n banks: [BANK_ACCOUNT_NUMBER_0094]  Beneficiary Bank Name: BANCO DE AMERICA CENTRAL,S.A.  Beneficiary Bank Address: 55 Av. Entre Calle Roo
  {"id": "robert@harmonygames.co/1795182296548841984", "last": "2024-04-02T00:53:49Z", "subject": "SVB Payment Notification: Recipient Created", "snippet": "can now initiate payments to this recipient.Recipient Name: BANCO DE AMERICA ***8605Created by: Arthur [PERSON_NAME_17939] view the Recipient det
  {"id": "robert@harmonygames.co/1795182318659688694", "last": "2024-04-02T00:54:28Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***8605Amount: 4,032.00 USDTransaction Date: Apr 02 2024Tran
  {"id": "robert@harmonygames.co/1795182749681334173", "last": "2024-04-02T01:01:19Z", "subject": "SVB Payment Notification: Payment Scheduled", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***8605Amount: 4,032.00 USDTransaction Date: Apr 02 2024Transaction 
  {"id": "robert@harmonygames.co/1795282860741136988", "last": "2024-04-03T03:32:33Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***8605Amount: 4,032.00 USDTransaction Date: Apr 02 2024Transaction 
  {"id": "robert@harmonygames.co/1795509850966005840", "last": "2024-04-05T15:40:27Z", "subject": "SVB Payment Notification: Recipient Modified", "snippet": "can now initiate payments to this recipient.Recipient Name: BANCO DE AMERICA  ***3341Created by: Arthur [PERSON_NAME_91976] by: Arthur [PERSON_N
  {"id": "robert@harmonygames.co/1795510012758086524", "last": "2024-04-05T15:43:01Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: Apr 05 2024Tran
  {"id": "robert@harmonygames.co/1795511257876658998", "last": "2024-04-05T16:02:49Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: Apr 05 2024Transaction 
  {"id": "robert@harmonygames.co/1797806674476915535", "last": "2024-05-01T02:54:50Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: May 01 2024Tran
  {"id": "robert@harmonygames.co/1797816647013177532", "last": "2024-05-01T03:02:44Z", "subject": "SVB Payment Notification: Payment Scheduled", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: BANCO DE AMERICA ***3341Amount: 4,032.00 USDTransaction Date: May 01 2024Transaction 
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Lucas' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=184 (showing 10)  hidden by ACL=43 in 25 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1717088846.984229", "channel": "admin_foundersonly", "kind": "private", "date": "2024-05-30", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "and Lucas but not sure if Lucas is gonna be Deel or something else - <@EMPLOYEE_0016_SLAC"}
  {"id": "C04UEQVDVB7/1719603220.131689", "channel": "admin_foundersonly", "kind": "private", "date": "2024-06-28", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "2nd half of June's payment to Lucas OK to go?"}
  {"id": "C04UEQVDVB7/1721776655.058739", "channel": "admin_foundersonly", "kind": "private", "date": "2024-07-23", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I paid Lucas for July, FYI, the invoice he sent us"}
  {"id": "C04UEQVDVB7/1727147072.731139", "channel": "admin_foundersonly", "kind": "private", "date": "2024-09-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Hey, I could use some help setup IBAN for Lucas, he has to show some \"real\" income via bank transfer"}
  {"id": "C04UEQVDVB7/1728515757.225709", "channel": "admin_foundersonly", "kind": "private", "date": "2024-10-09", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ERSON_NAME_61253], [PERSON_NAME_0063], [PERSON_NAME_24716], Lucas + [PERSON_NAME_0034] (aka [USERNAME_18514])"}
  {"id": "C04UEQVDVB7/1728515975.249119", "channel": "admin_foundersonly", "kind": "private", "date": "2024-10-09", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "I told Lucas to play our game thoroughly so he can take existing code and hack together some"}
  {"id": "C04UEQVDVB7/1728842414.383799", "channel": "admin_foundersonly", "kind": "private", "date": "2024-10-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "and both Lucas and [PERSON_NAME_0063] I extended until Dec"}
  {"id": "C04UEQVDVB7/1728842466.629699", "channel": "admin_foundersonly", "kind": "private", "date": "2024-10-13", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "we’ll probably re-evaluate how things are going with Lucas and [PERSON_NAME_0063] over the next few months"}
  {"id": "C04UEQVDVB7/1729641090.599789", "channel": "admin_foundersonly", "kind": "private", "date": "2024-10-22", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "hey I initiated a payment for Lucas so he can pay his taxes on the 25th, it will need an approval when you get a ch"}
  {"id": "C04UEQVDVB7/1732216147.969439", "channel": "admin_foundersonly", "kind": "private", "date": "2024-11-21", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Please approve Lucas's payment when any of you get a chance in SVB"}

SEARCH gmail 'Western Union' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=68 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1800862632807829954", "last": "2024-06-03T17:40:37Z", "subject": "Money Services: Please complete your registration.", "snippet": " PLEASE  CONTACT US.  This is a customer service email from Western Union. Please dont reply to this email, but instead contact us securel
  {"id": "robert@harmonygames.co/1800862666016310104", "last": "2024-06-03T17:41:09Z", "subject": "Western Union: Thanks for registering with [ORG_NAME_0267]", "snippet": "Western Union: Thanks for registering with [ORG_NAME_0267]"}
  {"id": "robert@harmonygames.co/1800863023092539271", "last": "2024-06-03T17:47:58Z", "subject": "Western Union: Your profile has been updated", "snippet": "Western Union: Your profile has been updated"}
  {"id": "robert@harmonygames.co/1800863377084981753", "last": "2024-06-03T17:52:29Z", "subject": "[PERSON_NAME_0054], We’re reviewing your money transfer", "snippet": "Western Union    We’ll contact you if we need more information &zwnj; &zwnj; &zwnj; &zwnj; &z"}
  {"id": "robert@harmonygames.co/1800866258379753665", "last": "2024-06-03T18:38:16Z", "subject": "[PERSON_NAME_0054], we need more information to complete your transfer", "snippet": "Western Union      Please contact us within 12 hours   &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zw"}
  {"id": "robert@harmonygames.co/1800868316185080331", "last": "2024-06-03T19:10:59Z", "subject": "[PERSON_NAME_0054], looks like you didn't finish your transfer", "snippet": "Western Union &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &z"}
  {"id": "robert@harmonygames.co/1800873055214061794", "last": "2024-06-03T20:26:18Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "Western Union    Please find your transaction details inside &zwnj; &zwnj; &zwnj; &zwnj; &zwn"}
  {"id": "robert@harmonygames.co/1800906573953663690", "last": "2024-06-04T05:19:05Z", "subject": "[PERSON_NAME_0054], your money transfer's been received", "snippet": "                      This is a customer service email from Western Union.     [ORG_NAME_0267] Financial Services, Inc PO Box 6036 En
  {"id": "robert@harmonygames.co/1801865781398666352", "last": "2024-06-14T19:25:16Z", "subject": "[PERSON_NAME_0054], send [PERSON_NAME_26022] money so he can spend Father's Day his way", "snippet": "Western Union &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &z"}
  {"id": "robert@harmonygames.co/1802092844284446043", "last": "2024-06-17T07:36:18Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "Western Union    Please find your transaction details inside &zwnj; &zwnj; &zwnj; &zwnj; &zwn"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'ready for pickup' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=5 (showing 5)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1800873055214061794", "last": "2024-06-03T20:26:18Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "[PERSON_NAME_0054], your money transfer is ready for pickup"}
  {"id": "robert@harmonygames.co/1802092844284446043", "last": "2024-06-17T07:36:18Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "[PERSON_NAME_0054], your money transfer is ready for pickup"}
  {"id": "robert@harmonygames.co/1803223458475671884", "last": "2024-06-29T19:04:57Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "[PERSON_NAME_0054], your money transfer is ready for pickup"}
  {"id": "robert@harmonygames.co/1805405368810910191", "last": "2024-07-23T21:05:27Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "[PERSON_NAME_0054], your money transfer is ready for pickup"}
  {"id": "robert@harmonygames.co/1808201559428745555", "last": "2024-08-23T17:49:45Z", "subject": "[PERSON_NAME_0054], your money transfer is ready for pickup", "snippet": "[PERSON_NAME_0054], your money transfer is ready for pickup"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Leapblock' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=175 (showing 10)  hidden by ACL=43 in 16 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1691348161.902379", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "MASTER SERVICE AGREEMENT LEAPBLOCK.docx"}
  {"id": "C04UEQVDVB7/1691736503.333139", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-11", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Victor’s contract for leapblock is out for signature"}
  {"id": "C04UEQVDVB7/1693596970.119839", "channel": "admin_foundersonly", "kind": "private", "date": "2023-09-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "he wants to get paid via LeapBlock"}
  {"id": "C04UEQVDVB7/1693844392.858779", "channel": "admin_foundersonly", "kind": "private", "date": "2023-09-04", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ested him to send his personal ones and we can take care of leapblock later if it’s not ready"}
  {"id": "C04UEQVDVB7/1694123922.586709", "channel": "admin_foundersonly", "kind": "private", "date": "2023-09-07", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "a new contract for Martin, the UI Artist that’s running via leapblock and voided his existing contract. The contract needs t
  {"id": "C04UEQVDVB7/1694542569.878419", "channel": "admin_foundersonly", "kind": "private", "date": "2023-09-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I need help with leapblock wire transfer first"}
  {"id": "C04UEQVDVB7/1696031212.675419", "channel": "admin_foundersonly", "kind": "private", "date": "2023-09-29", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I got leapblock’s invoices for September: $15K for Saga map + $3260 for Martin (including a cou"}
  {"id": "C04UEQVDVB7/1696465283.996359", "channel": "admin_foundersonly", "kind": "private", "date": "2023-10-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ome if we can do some co-dev project with let’s say netflix/leapblock/hg"}
  {"id": "C04UEQVDVB7/1696465505.146419", "channel": "admin_foundersonly", "kind": "private", "date": "2023-10-05", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "M dollars - that should leave us with $125K/month to pay up leapblock and ourselves. [ORG_NAME_1552] pays up their own folks
  {"id": "C04UEQVDVB7/1698421493.218169", "channel": "admin_foundersonly", "kind": "private", "date": "2023-10-27", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": " create a contract for the animator • We need invoices from leapblock folks"}

SEARCH gmail 'Leapblock LTD' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=74 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1776934065865609837", "last": "2023-09-13T14:46:16Z", "subject": "SVB Payment Notification: Recipient Created", "snippet": "can now initiate payments to this recipient.Recipient Name: Leapblock LTD ***1359Created by: Leonard [USERNAME_8451] view the Recipient details, 
  {"id": "robert@harmonygames.co/1776934359028762037", "last": "2023-09-13T14:50:58Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 33,290.00 USDTransaction Date: Sep 13 2023Transa
  {"id": "robert@harmonygames.co/1778417830931312360", "last": "2023-09-29T23:50:04Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 22,260.00 USDTransaction Date: Oct 02 2023Transa
  {"id": "robert@harmonygames.co/1778673046872307222", "last": "2023-10-02T19:23:25Z", "subject": "SVB Payment reminder: Payments Awaiting Approval", "snippet": "ment MethodPayment Cut-off time Analysis Checking  ***0100  Leapblock LTD  ***1359  22,260.00 USD  Oct 02 2023  Leonard Hayes  Wire Transfer
  {"id": "robert@harmonygames.co/1778675214290918178", "last": "2023-10-02T20:01:07Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 22,260.00 USDTransaction Date: Oct 02 2023Transaction ID
  {"id": "robert@harmonygames.co/1781426224426097097", "last": "2023-11-02T04:47:14Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "oval.From: Harmony Games Inc.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 25,000.00 USDTransaction Date: Nov 02 2023Transa
  {"id": "robert@harmonygames.co/1781472945910297699", "last": "2023-11-02T17:09:52Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 25,000.00 USDTransaction Date: Nov 02 2023Transaction ID
  {"id": "robert@harmonygames.co/1784014596972608016", "last": "2023-11-30T19:16:47Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 24,318.00 USDTransaction Date: Nov 30 2023Transa
  {"id": "robert@harmonygames.co/1784016683763338498", "last": "2023-11-30T21:40:28Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 24,318.00 USDTransaction Date: Nov 30 2023Transaction ID
  {"id": "robert@harmonygames.co/1788379827654071548", "last": "2024-01-17T22:51:47Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: Leapblock LTD ***1359Amount: 21,018.00 USDTransaction Date: Jan 17 2024Transa
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Leapblock payment' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=3 (showing 3)  hidden by ACL=1 in 1 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1718839744.677849", "channel": "admin_foundersonly", "kind": "private", "date": "2024-06-19", "user": "EMPLOYEE_0025_SLACK_ID", "reply": false, "snippet": "<@EMPLOYEE_0038_SLACK_ID> [USERNAME_1052] and leapblock payments submitted"}
  {"id": "C04UTBZL6AX/1706811955.873289", "channel": "founders", "kind": "private", "date": "2024-02-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ok, on leapblock payment I’ll wait for you to finalize the correction of the animator’s time btw"}
  {"id": "D04UP2L3E3S/1738876895.221479", "channel": "D04UP2L3E3S", "kind": "im", "date": "2025-02-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Martin may be tricky because we are handling him via leapblock payments"}

SEARCH gmail 'JPMorgan' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=18 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1766186833505963865", "last": "2023-05-17T23:43:40Z", "subject": "Review your credit balance change", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1773986854471813951", "last": "2023-08-12T02:01:39Z", "subject": "Great job! You've paid off an account", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1785389929361055139", "last": "2023-12-15T22:48:39Z", "subject": "Check out your credit limit change", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1807850432367440782", "last": "2024-08-19T20:48:43Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: JPMorgan [PERSON_NAME_4503] ***3203Amount: 4,000.00 USDTransaction Date: Aug 
  {"id": "robert@harmonygames.co/1807851044809802572", "last": "2024-08-19T20:58:27Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: JPMorgan [PERSON_NAME_4503] ***3203Amount: 4,000.00 USDTransaction Date: Aug 19 2024T
  {"id": "robert@harmonygames.co/1811027924934171801", "last": "2024-09-23T22:33:35Z", "subject": "Important: Data breach alert", "snippet": "                                                      ©2024 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1817515193234348261", "last": "2024-12-04T13:05:58Z", "subject": "⚙️  China's semiconductor ban", "snippet": "001/job/210559411?utm_medium=jobboard&utm_source=linkedin): JPMorgan Chase, New York, NY  View image: (https://media.beehiiv.com/cdn-cgi/image/fit=s"}
  {"id": "robert@harmonygames.co/1818055705923708476", "last": "2024-12-10T12:17:10Z", "subject": "Cybersecurity VC funding returns to growth", "snippet": "O in Tokyo. The company is set to list on Dec. 18.GIC hired JPMorgan Chase as advisor for a potential sale of its 50% stake in Greenko Energy, an 
  {"id": "robert@harmonygames.co/1820776693169333299", "last": "2025-01-09T13:06:06Z", "subject": "⚙️  The trillion dollar gamble", "snippet": "ildouts across the consumer and enterprise landscape.”    **JPMorgan **[**wrote**](https://am.jpmorgan.com/gb/en/asset-management/institutional/insi"}
  {"id": "robert@harmonygames.co/1828561646752419641", "last": "2025-04-05T11:24:36Z", "subject": "Tariff fallout: Near- and long-term", "snippet": "     Our new research explores how financial giants such as JPMorgan Chase and Goldman Sachs are ramping up their presence in the ecosystem, targeti"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'JPMorgan' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=18 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1766186833505963865", "last": "2023-05-17T23:43:40Z", "subject": "Review your credit balance change", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1773986854471813951", "last": "2023-08-12T02:01:39Z", "subject": "Great job! You've paid off an account", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1785389929361055139", "last": "2023-12-15T22:48:39Z", "subject": "Check out your credit limit change", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1807850432367440782", "last": "2024-08-19T20:48:43Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: JPMorgan [PERSON_NAME_4503] ***3203Amount: 4,000.00 USDTransaction Date: Aug 
  {"id": "robert@harmonygames.co/1807851044809802572", "last": "2024-08-19T20:58:27Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: JPMorgan [PERSON_NAME_4503] ***3203Amount: 4,000.00 USDTransaction Date: Aug 19 2024T
  {"id": "robert@harmonygames.co/1811027924934171801", "last": "2024-09-23T22:33:35Z", "subject": "Important: Data breach alert", "snippet": "                                                      ©2024 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1817515193234348261", "last": "2024-12-04T13:05:58Z", "subject": "⚙️  China's semiconductor ban", "snippet": "001/job/210559411?utm_medium=jobboard&utm_source=linkedin): JPMorgan Chase, New York, NY  View image: (https://media.beehiiv.com/cdn-cgi/image/fit=s"}
  {"id": "robert@harmonygames.co/1818055705923708476", "last": "2024-12-10T12:17:10Z", "subject": "Cybersecurity VC funding returns to growth", "snippet": "O in Tokyo. The company is set to list on Dec. 18.GIC hired JPMorgan Chase as advisor for a potential sale of its 50% stake in Greenko Energy, an 
  {"id": "robert@harmonygames.co/1820776693169333299", "last": "2025-01-09T13:06:06Z", "subject": "⚙️  The trillion dollar gamble", "snippet": "ildouts across the consumer and enterprise landscape.”    **JPMorgan **[**wrote**](https://am.jpmorgan.com/gb/en/asset-management/institutional/insi"}
  {"id": "robert@harmonygames.co/1828561646752419641", "last": "2025-04-05T11:24:36Z", "subject": "Tariff fallout: Near- and long-term", "snippet": "     Our new research explores how financial giants such as JPMorgan Chase and Goldman Sachs are ramping up their presence in the ecosystem, targeti"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH gmail 'JPMorgan' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=18 (showing 10)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1766186833505963865", "last": "2023-05-17T23:43:40Z", "subject": "Review your credit balance change", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1773986854471813951", "last": "2023-08-12T02:01:39Z", "subject": "Great job! You've paid off an account", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1785389929361055139", "last": "2023-12-15T22:48:39Z", "subject": "Check out your credit limit change", "snippet": " Center to learn how to protect your information.    © 2023 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1807850432367440782", "last": "2024-08-19T20:48:43Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: JPMorgan [PERSON_NAME_4503] ***3203Amount: 4,000.00 USDTransaction Date: Aug 
  {"id": "robert@harmonygames.co/1807851044809802572", "last": "2024-08-19T20:58:27Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: JPMorgan [PERSON_NAME_4503] ***3203Amount: 4,000.00 USDTransaction Date: Aug 19 2024T
  {"id": "robert@harmonygames.co/1811027924934171801", "last": "2024-09-23T22:33:35Z", "subject": "Important: Data breach alert", "snippet": "                                                      ©2024 JPMorgan Chase & Co."}
  {"id": "robert@harmonygames.co/1817515193234348261", "last": "2024-12-04T13:05:58Z", "subject": "⚙️  China's semiconductor ban", "snippet": "001/job/210559411?utm_medium=jobboard&utm_source=linkedin): JPMorgan Chase, New York, NY  View image: (https://media.beehiiv.com/cdn-cgi/image/fit=s"}
  {"id": "robert@harmonygames.co/1818055705923708476", "last": "2024-12-10T12:17:10Z", "subject": "Cybersecurity VC funding returns to growth", "snippet": "O in Tokyo. The company is set to list on Dec. 18.GIC hired JPMorgan Chase as advisor for a potential sale of its 50% stake in Greenko Energy, an 
  {"id": "robert@harmonygames.co/1820776693169333299", "last": "2025-01-09T13:06:06Z", "subject": "⚙️  The trillion dollar gamble", "snippet": "ildouts across the consumer and enterprise landscape.”    **JPMorgan **[**wrote**](https://am.jpmorgan.com/gb/en/asset-management/institutional/insi"}
  {"id": "robert@harmonygames.co/1828561646752419641", "last": "2025-04-05T11:24:36Z", "subject": "Tariff fallout: Near- and long-term", "snippet": "     Our new research explores how financial giants such as JPMorgan Chase and Goldman Sachs are ramping up their presence in the ecosystem, targeti"}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Chase account' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=7 (showing 7)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1692055047.802419", "channel": "admin_foundersonly", "kind": "private", "date": "2023-08-14", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "We’ll still receive $175K from angels to our Chase account, brining total close to $250K FDIC insured limit"}
  {"id": "C04UEQVDVB7/1754444435.379339", "channel": "admin_foundersonly", "kind": "private", "date": "2025-08-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "money ICS cash account = $188K Checking account SVB = $250K Chase account = $3K total should be $436K or so -&gt; There is a
  {"id": "C04UEQVDVB7/1761954952.006759", "channel": "admin_foundersonly", "kind": "private", "date": "2025-10-31", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Chase account closed. Cashiers check deposited into SVB. Remind me the download all statement"}
  {"id": "C04UEQVDVB7/1761958213.753549", "channel": "admin_foundersonly", "kind": "private", "date": "2025-11-01", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "Chase Account Closure Harmony Games All Statements attached for reference"}
  {"id": "C04UTBZL6AX/1689789839.031959", "channel": "founders", "kind": "private", "date": "2023-07-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I guess just go the Chase account and get the info from There?"}
  {"id": "C04UTBZL6AX/1689792396.124199", "channel": "founders", "kind": "private", "date": "2023-07-19", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "ing international): CHASUS33 Harmony Games Address for this Chase account: [ADDRESS_0902] MATTHEWS NC 28104-7890"}
  {"id": "C0ADGSZKR3R/1770932925.126829", "channel": "winddown", "kind": "private", "date": "2026-02-12", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "remove the bank account from Carta but they are tied to our Chase account which is closed so good luck to them taking the money from u

SEARCH slack 'closed the account' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'PERSON_4419_NAME' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=6 (showing 6)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1810637269242475896", "last": "2024-09-19T15:04:19Z", "subject": "Your account (449-481-1590) is now linked to a manager account (PERSON_4419_NAME)", "snippet": " account (449-481-1590) is now linked to a manager account (PERSON_4419_NAME)"}
  {"id": "robert@harmonygames.co/1810637392442456501", "last": "2024-09-19T15:06:17Z", "subject": "You have a pending request to link your account to a Manager account (PERSON_4419_NAME)", "snippet": " pending request to link your account to a Manager account (PERSON_4419_NAME)"}
  {"id": "robert@harmonygames.co/1815095592611804295", "last": "2024-11-07T21:08:14Z", "subject": "Fwd: PERSON_4419_NAME Invoices for Sept, Oct, and Nov", "snippet": "Fwd: PERSON_4419_NAME Invoices for Sept, Oct, and Nov"}
  {"id": "robert@harmonygames.co/1820175611244310641", "last": "2025-01-02T21:52:10Z", "subject": "SVB Payment Notification: Recipient Created", "snippet": "can now initiate payments to this recipient.Recipient Name: PERSON_4419_NAME LLC ***0115Created by: Leonard [USERNAME_8451] view the Recipient de
  {"id": "robert@harmonygames.co/1820175712774488305", "last": "2025-01-02T21:53:42Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: PERSON_4419_NAME LLC ***0115Amount: 16,428.57 USDTransaction Date: Jan 02 202
  {"id": "robert@harmonygames.co/1820177564355637667", "last": "2025-01-02T22:23:12Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "rom: Harmony Games GAMES INC.: Analysis Checking ***0100To: PERSON_4419_NAME LLC ***0115Amount: 16,428.57 USDTransaction Date: Jan 02 2025Transac
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH contacts 'Brooks' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=2 (showing 2)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/contacts/contacts.json", "service_file": "contacts.json", "pointer": "/contacts/157/last_name", "parent_pointer": "/contacts/157", "encoding": "json", "text": "Brooks", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/contacts/contacts.json", "service_file": "contacts.json", "pointer": "/contacts/157/email", "parent_pointer": "/contacts/157", "encoding": "json", "text": "oliver.brooks@harmonygames.co", "truncated": false}

SEARCH gdocs 'Lauren Brooks' as robert  scope: GDocs title + body_text
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_20a0df3860bb5731d22f07", "name": "Consulting Agreement Lauren Brooks.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Consulting Agreement Lauren Brooks"}

SEARCH gmail '***3801' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=3 (showing 3)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1847427662807006290", "last": "2025-10-30T18:02:10Z", "subject": "SVB Payment Notification: Payment Processed", "snippet": "nalysis Checking ***0100To: Martin [PERSON_NAME_7250] Walsh ***3801Amount: 1,999.00 BGNTransaction Date: Oct 30 2025Transaction ID: [IDENTIFIER_1
  {"id": "robert@harmonygames.co/1847428048462968163", "last": "2025-10-30T17:27:52Z", "subject": "SVB Payment Notification: Recipient Created", "snippet": "s recipient.Recipient Name: Martin [PERSON_NAME_7250] Walsh ***3801Created by: Arthur [PERSON_NAME_17939] view the Recipient details, please log 
  {"id": "robert@harmonygames.co/1847428090813337287", "last": "2025-10-30T23:06:19Z", "subject": "SVB Payment Notification: Payment Awaiting Approval", "snippet": "nalysis Checking ***0100To: Martin [PERSON_NAME_7250] Walsh ***3801Amount: 1,999.00 BGNTransaction Date: Oct 30 2025Transaction ID: [IDEN
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH linear 'Walsh' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=10 (showing 10)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/users/9/email", "parent_pointer": "/users/9", "encoding": "json", "text": "martin.walsh@harmonygames.co", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/users/9/name", "parent_pointer": "/users/9", "encoding": "json", "text": "martin.walsh@harmonygames.co", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/users/9/display_name", "parent_pointer": "/users/9", "encoding": "json", "text": "martin.walsh@harmonygames.co", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/176/description", "parent_pointer": "/issues/176", "encoding": "json", "text": "visibility to what is clickable on the mini game hub.\n\nThe current yellow a
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/448/description", "parent_pointer": "/issues/448", "encoding": "json", "text": "'@[PERSON_NAME_0054] said:\n\n> @Martin.Walsh we need new art for these skill
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/548/description", "parent_pointer": "/issues/548", "encoding": "json", "text": "'@Leonard said:\n\n> @Martin.Walsh this is the ask for “achievements” on the 
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/559/description", "parent_pointer": "/issues/559", "encoding": "json", "text": "'@Leonard said:\n\n> @Martin.Walsh we also need another “unlock screen” for b
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/560/description", "parent_pointer": "/issues/560", "encoding": "json", "text": "'@[PERSON_NAME_0054] said:\n\n> @Martin.Walsh can we get this unlock mini gam
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1173/description", "parent_pointer": "/issues/1173", "encoding": "json", "text": "ce to ensure proper adjustments are made. For reposition suggestions and th
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/issues/1211/description", "parent_pointer": "/issues/1211", "encoding": "json", "text": "'@Martin.Walsh said:\n\n> **Splash Screen** - New Logo + Loading bar @[PERS

SEARCH snowflake 'REVENUE_DAILY' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=10 (showing 10)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/12/name", "parent_pointer": "/tables/12", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/12/id", "parent_pointer": "/tables/12", "encoding": "json", "text": "ANALYTICS.MONETIZATION.REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/name", "parent_pointer": "/tables/13", "encoding": "json", "text": "REVENUE_DAILY_V2", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/id", "parent_pointer": "/tables/13", "encoding": "json", "text": "ANALYTICS.MONETIZATION.REVENUE_DAILY_V2", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/0/source_table", "parent_pointer": "/tables/13/rows/0", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/1/source_table", "parent_pointer": "/tables/13/rows/1", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/2/source_table", "parent_pointer": "/tables/13/rows/2", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/3/source_table", "parent_pointer": "/tables/13/rows/3", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/4/source_table", "parent_pointer": "/tables/13/rows/4", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/snowflake/snowflake.json", "service_file": "snowflake.json", "pointer": "/tables/13/rows/5/source_table", "parent_pointer": "/tables/13/rows/5", "encoding": "json", "text": "REVENUE_DAILY", "truncated": false}

SEARCH gsheets 'P&L' as robert  scope: GSheets spreadsheet title, tab titles, cell strings (streamed)
visible hits=8 (showing 8)  hidden by ACL=12 in 12 containers  UNVERIFIED=0 in 0 containers
  {"id": "f_28ecc492b19f3696a19a97", "name": "Harmony Games P&L and forecast - Oct 2025.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_29467f8365d566d7bb2e76", "name": "Harmony Games P&L and forecast - Apr 2024.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_2cb4e217609f00a8ecf416", "name": "Harmony Games P&L and forecast - Oct 2024.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_44ea2c36d71239ae75cc84", "name": "Harmony Games P&L and forecast - Apr 2025.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_605121f4a36752645e0ac3", "name": "Harmony Games P&L and forecast - Jan 2026.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_68c2418dd4ab47afe9254a", "name": "4X GAME BUDGET.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_779b6777b8ffc4acecc2d1", "name": "Harmony Games P&L and forecast - Jan 2024.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}
  {"id": "f_90976e6b4466acbfaf5a74", "name": "Harmony Games P&L and forecast - Oct 2023.xlsx", "mime": "application/vnd.google-apps.spreadsheet", "why": "file is shared with the persona (shared_with_emails)", "snippet": "Cash P&L"}

SEARCH slack 'cash in bank' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C04UEQVDVB7/1754445622.992119", "channel": "admin_foundersonly", "kind": "private", "date": "2025-08-06", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "I identified a discrepancy between the cash in bank balance in QuickBooks and the actual bank balances per the statements. T

SEARCH gdocs 'Saga Map' as robert  scope: GDocs title + body_text
visible hits=10 (showing 10)  hidden by ACL=34 in 34 containers  UNVERIFIED=4 in 4 containers
  {"id": "f_322bbfdb37d253aa8624b9", "name": "MASTER SERVICE AGREEMENT LEAPBLOCK.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "uch budget and whose formal title is “Game of Dominoes - 3D Saga Map” (the “Project”). The 
  {"id": "f_4425abc665c6aba6256234", "name": "QA Checklist For Every Release.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "Test: At end of level 2, tap anywhere to be brought back to Saga map Immediately exit the game via the home button. Uninstall 
  {"id": "f_64e832f6ab61eb09e6ccd0", "name": "Board Meeting Jul_OCT 17 2024.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "ue to be careful with our budget and with completion of the saga maps, we reduced our art contra
  {"id": "f_6ef44568fe44d2dc76dd63", "name": "[LiveOps] Team Co-Op Event.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": " each level ranging from 1 to 3. When players return to the saga map/home after a level completion,
  {"id": "f_766b2d58c50ca246703f16", "name": "Bad looking Textures.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "rs look good but buttons/ribbons/arrows need better texture Saga map: Mushroom houses, logs, flowers, hou
  {"id": "f_89fadbc54660c9881d8cf9", "name": "Zombie Match 3D Testing and GDD.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "rmined. Question: What is our level progression like? Is it saga map style? Repeatable levels? Or single finish per level? Or
  {"id": "f_97bbbdbf4a6078fa98e7a0", "name": "[LiveOps] Streak Fever.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": "pop up as soon as the 4-15 is completed and returned to the saga map. loaded.  The pop up may have eith
  {"id": "f_c57724584820a26f3bbe54", "name": "DD Global Launch Readiness.docx", "mime": "application/vnd.google-apps.document", "why": "file is shared with the persona (shared_with_emails)", "snippet": ") P0 - 2312 - sophie's favor reset after killing the app in saga map (blake) P0s last minute for bl
  {"id": "f_c82c8f52efe79e566b6d25", "name": "Tentative Engineering + Linear (2023-08-03 11_06 G.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "backend boost system Puzzle, level editor in the backend of saga map, main gameplay, mini game. Number one
  {"id": "f_f593467ab59941eb012a7d", "name": "07.01.2024 Rebirth - Release Candidate Checklist a.docx", "mime": "application/vnd.google-apps.document", "why": "persona owns the file", "snippet": "e sound component from Unity (Marcus’s request) (blake) The Saga map is actively using resources when the

SEARCH linear 'Private Entrepreneur' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=0 (showing 0)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers

SEARCH gmail 'Payoneer' as robert  scope: Gmail subject, body, from, to, cc, attachment filenames (thread files)
visible hits=2 (showing 2)  hidden by ACL=None in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "robert@harmonygames.co/1798239548116390324", "last": "2024-05-05T18:47:47Z", "subject": "Dixelar sent you a payment request", "snippet": "                                                            payoneer balance                                                                        "}
  {"id": "robert@harmonygames.co/1811158112675912556", "last": "2024-09-25T09:02:50Z", "subject": "Dixelar sent you a payment request", "snippet": "                                                            payoneer balance                                                                        "}
note: --no-hidden: containers outside the persona's view were not scanned

SEARCH slack 'Telegram distribution' as robert  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=1 (showing 1)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C05KNDCHAAG/1760125440.959149", "channel": "company-internal", "kind": "private", "date": "2025-10-10", "user": "EMPLOYEE_0038_SLACK_ID", "reply": false, "snippet": "EMPLOYEE_0035_SLACK_ID>* to harmonygames. She will lead our Telegram distribution strategy, starting with a focused experiment

SEARCH linear 'Brooks' as robert  scope: hg.py search (unscoped: no ACL filter)
visible hits=3 (showing 3)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/users/29/email", "parent_pointer": "/users/29", "encoding": "json", "text": "oliver.brooks@harmonygames.co", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/users/29/name", "parent_pointer": "/users/29", "encoding": "json", "text": "oliver.brooks@harmonygames.co", "truncated": false}
  {"file": "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/linear/data.json", "service_file": "data.json", "pointer": "/users/29/display_name", "parent_pointer": "/users/29", "encoding": "json", "text": "oliver.brooks@harmonygames.co", "truncated": false}

CHECK-SQL as robert <robert@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_6feda53b2382c63bf47b25 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_3304033843904a426f3c00 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_a4b3c4287a4314d8e532e1 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdocs.docs_documents insert f_6feda53b2382c63bf47b25 - file is shared with the persona (shared_with_emails)
[YES LB] L16 gsheets.sheets_spreadsheets insert f_3304033843904a426f3c00 - file is shared with the persona (shared_with_emails)
[YES LB] L19 gsheets.sheets_sheets insert f_3304033843904a426f3c00, f_3304033843904a426f3c00#0 - file is shared with the persona (shared_with_emails)
[YES LB] L21 gslides.slides_presentations insert f_a4b3c4287a4314d8e532e1 - file is shared with the persona (shared_with_emails)
[YES LB] L24 gslides.slides_pages insert f_a4b3c4287a4314d8e532e1, slide_876d3aebf1e5 - file is shared with the persona (shared_with_emails)
[YES LB] L26 gslides.slides_page_elements insert f_a4b3c4287a4314d8e532e1, el_6b8f1c138f0c, slide_876d3aebf1e5 - file is shared with the persona (shared_with_emails)
[YES LB] L28 gslides.slides_pages insert f_a4b3c4287a4314d8e532e1, slide_541fd17875ce - file is shared with the persona (shared_with_emails)
[YES LB] L30 gslides.slides_page_elements insert f_a4b3c4287a4314d8e532e1, el_15b213cdfaa1, slide_541fd17875ce - file is shared with the persona (shared_with_emails)
[YES LB] L32 gslides.slides_pages insert f_a4b3c4287a4314d8e532e1, slide_09f12ee6f24d - file is shared with the persona (shared_with_emails)
[YES LB] L34 gslides.slides_page_elements insert f_a4b3c4287a4314d8e532e1, el_0e414d770865, slide_09f12ee6f24d - file is shared with the persona (shared_with_emails)
[YES LB] L36 gslides.slides_pages insert f_a4b3c4287a4314d8e532e1, slide_9bd7d5368d2a - file is shared with the persona (shared_with_emails)
[YES LB] L38 gslides.slides_page_elements insert f_a4b3c4287a4314d8e532e1, el_30f4d02c73c5, slide_9bd7d5368d2a - file is shared with the persona (shared_with_emails)
[YES LB] L40 gslides.slides_pages insert f_a4b3c4287a4314d8e532e1, slide_8f7eb76d1929 - file is shared with the persona (shared_with_emails)
[YES LB] L42 gslides.slides_page_elements insert f_a4b3c4287a4314d8e532e1, el_2f133c6a4173, slide_8f7eb76d1929 - file is shared with the persona (shared_with_emails)
[YES LB] L44 slack.slack_messages insert fa707da5679e86fd88f6638bd1828bfe, C0ADGSZKR3R/1770945821.640039 - persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] L47 slack.slack_messages insert f5b759f3d1c117ac1596b1bdf0abdb93, C0ADGSZKR3R/1770945859.212469 - persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
[YES LB] L49 slack.slack_messages insert 6312d121675119df7a441f9ca5c6b4cb, C05URGU759U/1770971846.479179 - persona EMPLOYEE_0016_SLACK_ID is in members of private leapblock
[YES] L86 gcal.gcal_events insert evt_cdc76b69e93767407fb591 - persona is an attendee and holds its own copy evt_f21476dc404329f67fd60d (same ical_uid and start) on robert@harmonygames.co
[YES LB] L89 gcal.gcal_events insert evt_f21476dc404329f67fd60d - event is on the persona's own calendar robert@harmonygames.co
[YES] L91 gcal.gcal_events insert evt_351ff9bbba676066532e05 - persona is an attendee and holds its own copy evt_f21476dc404329f67fd60d (same ical_uid and start) on robert@harmonygames.co
[YES LB] base slack C04UEQVDVB7/1694616951.239909 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C04UEQVDVB7/1712331372.614469 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C04UEQVDVB7/1712901800.684259 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C04UEQVDVB7/1735854841.070019 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C04UEQVDVB7/1754445622.992119 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
[YES LB] base slack C05KNDCHAAG/1760125440.959149 - base record: message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private company-internal
[YES LB] base gdrive f_20a0df3860bb5731d22f07 - base record: file is shared with the persona (shared_with_emails)
[YES LB] base gdrive f_322bbfdb37d253aa8624b9 - base record: file is shared with the persona (shared_with_emails)
[YES LB] base gdrive f_605121f4a36752645e0ac3 - base record: file is shared with the persona (shared_with_emails)
[YES LB] base gmail robert@harmonygames.co/1776227799449805411 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1776934359028762037 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1795282860741136988 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1795509850966005840 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1800873055214061794 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1807851044809802572 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1808201559428745555 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1815095592611804295 - base record: thread is in the persona's own mailbox robert@harmonygames.co
[YES LB] base gmail robert@harmonygames.co/1847427662807006290 - base record: thread is in the persona's own mailbox robert@harmonygames.co
verdict: PASS (0 load-bearing rows not visible)

robert gmail leonard.hayes@harmonygames.co/1798427314394417287: NO
  reason:   thread is in mailbox leonard.hayes@harmonygames.co, not the persona's mailbox robert@harmonygames.co
  evidence: thread=leonard.hayes@harmonygames.co/1798427314394417287, mailbox=leonard.hayes@harmonygames.co, messages_in_thread=1, last=2024-05-07T20:32:17Z, file=threads/leonard@harmonygames.co_1798427314394417287.json, persona_mailbox=robert@harmonygames.co
robert gdrive d_9f7ba94f7526d54d8482ba: YES
  reason:   persona owns the file
  evidence: file=d_9f7ba94f7526d54d8482ba, name=robert@harmonygames.co, mime=application/vnd.google-apps.folder, owner=robert@harmonygames.co, shared_with=0, visibility=private
robert slack C0ADGSZKR3R/1770934638.035469: YES
  reason:   message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private winddown
  evidence: channel=C0ADGSZKR3R, name=winddown, kind=private, members=7, persona_slack_id=EMPLOYEE_0016_SLACK_ID, message=[ts 1770934638.035469 2026-02-12 user EMPLOYEE_0038_SLACK_ID]
robert slack C06MXPL9536/1715113013.494939: YES
  reason:   message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private video_editing_oleg
  evidence: channel=C06MXPL9536, name=video_editing_oleg, kind=private, members=12, persona_slack_id=EMPLOYEE_0016_SLACK_ID, message=[ts 1715113013.494939 2024-05-07 user EMPLOYEE_0038_SLACK_ID]
robert slack C04UEQVDVB7/1761844454.096829: YES
  reason:   message inherits channel: persona EMPLOYEE_0016_SLACK_ID is in members of private admin_foundersonly
  evidence: channel=C04UEQVDVB7, name=admin_foundersonly, kind=private, members=7, persona_slack_id=EMPLOYEE_0016_SLACK_ID, message=[ts 1761844454.096829 2025-10-30 user EMPLOYEE_0038_SLACK_ID]

VERIFY notices: 88 of 88 Robert threads read through hg.py; 132 Processed payments; currencies {'USD': 131, 'BGN': 1}
VERIFY by-date USD sum Domino Delights: 984,888.21
VERIFY by-date USD sum ZM: 608,820.50
VERIFY by-date USD sum Combo Fighter: 73,685.61
VERIFY ending 0115: 16,428.57 over 1 notices
VERIFY ending 0148: 2,368.00 over 1 notices
VERIFY ending 1359: 374,654.00 over 29 notices
VERIFY ending 1794: 5,000.00 over 1 notices
VERIFY ending 1876: 600.00 over 1 notices
VERIFY ending 2532: 6,085.56 over 2 notices
VERIFY ending 3139: 500.00 over 1 notices
VERIFY ending 3203: 4,000.00 over 1 notices
VERIFY ending 3307: 1,000.00 over 1 notices
VERIFY ending 3341: 37,056.00 over 10 notices
VERIFY ending 3801 BGN: 1,999.00 over 1 notices
VERIFY ending 4015: 31,250.00 over 2 notices
VERIFY ending 4020: 3,200.00 over 1 notices
VERIFY ending 5000: 46,201.50 over 3 notices
VERIFY ending 5384: 1,500.00 over 3 notices
VERIFY ending 5660: 3,750.00 over 1 notices
VERIFY ending 6577: 6,450.00 over 3 notices
VERIFY ending 7393: 7,175.00 over 4 notices
VERIFY ending 7534: 7,500.00 over 1 notices
VERIFY ending 8380: 1,015,347.19 over 35 notices
VERIFY ending 8501: 93,171.50 over 28 notices
VERIFY ending 8605: 4,032.00 over 1 notices
VERIFY ending 9368: 125.00 over 1 notices
VERIFY Leapblock ***1359 by year: 2023 71,578.00, 2024 232,726.00, 2025 62,950.00, 2026 7,400.00
VERIFY Western Union: 5 transfers by tracking number, 1 forwarded copy, each naming [PERSON_NAME_36400]; sent ['1075.00', '1075.00', '1075.00', '2150.00', '2150.00']; total 7,525.00
VERIFY census as Robert, 'Dixelar': 2 threads; subjects ['Dixelar sent you a payment request']
VERIFY census as Robert, 'Payoneer': 2 threads; subjects ['Dixelar sent you a payment request']
VERIFY census as Robert, 'Thanks for your payment': 0 threads; subjects []
VERIFY census as Robert, 'Your Payment Was Approved': 0 threads; subjects []
VERIFY census as Robert, 'Upwork': 4 threads; subjects ['Document shared with you: "[T] Wanted!"', 'Issue #262: Adapting to the Gig Economy', 'Re: Harmony Games intro to [T] @ [T]', 'StartUp founders: Entropy Wins.']
VERIFY census as Robert, 'PayPal': 9 threads; subjects ["Buckling AI's seatbelts", 'Can VC win over private wealth?', 'How a Free Browser Extension Scaled to a $4B', 'Mobile Gaming Ad Quality Report: Challenges ']
VERIFY census as Robert, 'Remitly': 0 threads; subjects []
VERIFY census as Robert, 'MoneyGram': 0 threads; subjects []
VERIFY census as Robert, 'Zelle': 1 threads; subjects ["Fintech's consumer protection quandry"]
VERIFY census as Robert, 'Venmo': 0 threads; subjects []
VERIFY census as Robert, 'Fiverr': 2 threads; subjects ['Issue #262: Adapting to the Gig Economy', 'RE: Starting as a Freelancer!']
VERIFY census as Robert, 'payment receipt': 4 threads; subjects ['Fwd: [T] Payment Receipt', 'Q3 Dividend Distribution Confirmation 013494', 'Re: Payment Receipt 0283884784584_9494849', 'Receipt from Unity Ads']
VERIFY census control, all mailboxes, 'Thanks for your payment': 6 hits, 6 in Leonard's mailbox files, scan_complete True
```

## 6 · Triggers, incorporation and implicit requirements

| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · persona-readable · unique · instructions-not-answer) | Inferable |
|---|---|---|---|---|
| count by the method | f_6feda53b2382c63bf47b25 | scope: Leonard's ask, and that he laid out how to count it | C0ADGSZKR3R/1770945821.640039 names the doc by title · YES · one doc with that title · rules, no figures | yes, once the ask is followed |
| sheet layout | f_3304033843904a426f3c00 | a pointer that he set how it should look; no layout clause | C0ADGSZKR3R/1770945859.212469 'use the layout of my Angel note working sheet' · YES · one working sheet · layout only; its figures are the quick pass | yes, once the ask is followed |
| sheet in his Drive, shared | C0ADGSZKR3R/1770945859.212469 | destination and recipients | C0ADGSZKR3R/1770945859.212469 · YES · named by the prompt too · instruction | yes |
| issues to Done, reason first | f_6feda53b2382c63bf47b25 | deliverable: work through the project the way he wants | f_6feda53b2382c63bf47b25 last paragraph · YES · unique · instruction | gotcha with a record trigger |
| the five figures that differ | F12 to F24, F36, F37 | none in the prompt | f_6feda53b2382c63bf47b25 'A notice is where you start, not the last word' and 'that beats the notices for them' · YES · unique · states the tests, not the payees | gotcha with a record trigger |
| buckets and the bet calendar | f_6feda53b2382c63bf47b25 | none in the prompt | f_6feda53b2382c63bf47b25 · YES · unique · rules only | gotcha with a record trigger |
| brought-in figures | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY | deliverable: what each bet brought in, on the page; the method holds Combo Fighter's | f_6feda53b2382c63bf47b25 names the table by role · YES · V2 sums equal · no sums given | gotcha with a record trigger |
| reply with figures, deck changes, link | C0ADGSZKR3R/1770945859.212469 | destination and content | C0ADGSZKR3R/1770945859.212469 'tell me here' · YES · one channel · instruction; the link comes from the prompt | yes |

Prompt text: 04_Prompt.txt, 109 words, sha256 d0cb08476d23, the text the platform reviewed. It says 'how it should look' and 'Build that page as a sheet' in place of a layout clause, 'reply to him in #winddown', and 'the draft deck'.

Anchor-name table (noun phrases of at most 6 words; `;` separates synonyms):

| Anchor | May be named |
|---|---|
| AN1 | Leonard's ask in #winddown |
| AN2 | the Payee history project |

## 7 · Dates and constraints

| Item | Absolute date or value | Source | Past fact or deadline |
|---|---|---|---|
| Robert's today | Saturday Feb 14, 2026 (clock 2026-02-14T00:00Z = Fri Feb 13, 4:00 PM PT) | 00_Task_Context.json universe.persona_today; latest ask post C0ADGSZKR3R/1770945859.212469 | — |
| Leonard's ask | Thu Feb 12, 2026, 5:23 and 5:24 PM PT (Fri Feb 13, 01:23 and 01:24Z). 'Thursday' is the Pacific day | C0ADGSZKR3R/1770945821.640039, C0ADGSZKR3R/1770945859.212469 | past fact |
| the method | written Thu Feb 12, 3:52 PM PT (23:52Z), edited 4:41 PM PT (Feb 13, 00:41Z) | f_6feda53b2382c63bf47b25 | past fact |
| the working sheet and deck | Thu Feb 12, 2:44 and 2:52 PM PT (22:44 and 22:52Z) | f_3304033843904a426f3c00, f_a4b3c4287a4314d8e532e1 | past fact |
| Leapblock's statement | Fri Feb 13, 12:37 AM PT (08:37Z), before the Slack export end (NB-6) | C05URGU759U/1770971846.479179 | past fact |
| Arthur's mail and Leonard's reply | Fri Feb 13, 8:26 and 9:08 AM PT (16:26 and 17:08Z) | robert@harmonygames.co/<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com> robert@harmonygames.co/<CAPBs_a5xhlLhxf4uFEerJEygHD5CJ2ob3qegV9nV-erG4foiIU@mail.gmail.com> | past fact |
| the notices' window | Sep 5, 2023 to Feb 2, 2026 | robert@harmonygames.co/1776227799449805411 | past fact |
| the bet calendar | Domino Delights to Jan 8, 2025; ZM Jan 9 to Nov 23, 2025; Combo Fighter from Nov 24, 2025. No payment falls near a boundary | f_6feda53b2382c63bf47b25 | rule |
| the angel calls | Tue Feb 17, 2026, 9:00 to 10:30 AM PT (17:00 to 18:30Z) | evt_f21476dc404329f67fd60d | deadline (future event) |
| shutdown premise | Feb 14 is after the wind-down began: no business as usual, and the deck itself says orderly wind-down | f_a4b3c4287a4314d8e532e1 | past fact |
| Leonard's notes on ENG-2455 and ENG-2459 | Thu Feb 12, 4:45 and 4:58 PM PT (Feb 13, 00:45 and 00:58Z) | ENG-2455, ENG-2459 | past fact |
| known issues touched | NB-1 and NB-6 (only founders and Leapblock's contact post late, all before 10:03Z Feb 13); NB-2 (no P&L cost graded); NB-12 (key on account endings); NB-24 (no base Linear comments, all 60 notes are seeded); NB-26 (the method holds Combo Fighter's revenue, so no Combo Fighter figure is graded) | f_605121f4a36752645e0ac3, ENG-2438, C05URGU759U/1770971846.479179 | constraint |

## 8 · Difficulty levers

| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |
|---|---|---|---|---|
| Ambiguity | yes | yes | who each payee is and which payments count sit across notes, mail, Slack and a contract (F12 to F31) | the prompt names the two anchors only, never where an answer lives |
| Dynamic change | yes | yes | the notices and quick numbers come first; F13, F14, F19 and F22 overturn them | the prompt names neither the first summary nor the correction |
| Multi-source | yes | yes | Gmail, Linear, Slack, Docs, Sheets, Slides, Snowflake, Contacts, Trello, Calendar, Drive | no source named as an exact artifact beyond the anchors |
| Async | no | no | friction none (03_Error_Async_Config.txt) | — |
| Error recovery | no | no | friction none | — |
| Access control | no | no | every graded record is Robert-visible (check-sql PASS); records outside his reach are off the graded path (F37) | no ask to read someone else's scoped data |

## 9 · Must not appear in the prompt

- **Tool and server names (catalog.json):** slack_send_message, slack_read_channel, slack_read_thread, slack_search_public_and_private, linear_list_issues, linear_list_comments, linear_create_comment, linear_update_issue, gsheets_create_spreadsheet, gsheets_values_update, gsheets_values_get, gdrive_share_file, gdrive_search, gdocs_get_document_text, gslides_get_presentation_text, gmail_search_messages, gmail_get_messages_batch, gmail_get_thread, snowflake_execute_query, snowflake_describe_table, trello_search, trello_get_card, contacts_search_contacts, gcal_list_events; any MCP server name; 'the X tool'.
- **The dossier's never-name list:** the method's rules, the bet dates, the buckets, any payee, any figure, the notices, #leapblock, #admin_foundersonly, the Chase mail, the contract, Western Union, the warehouse table.
- **Opaque ids and filenames:** f_6feda53b2382c63bf47b25, f_3304033843904a426f3c00, f_a4b3c4287a4314d8e532e1, 698e55f9af74d68d679de7b3, the project id, ENG-2438 to ENG-2459, C0ADGSZKR3R/1770945821.640039, C0ADGSZKR3R/1770945859.212469, C05URGU759U/1770971846.479179, REVENUE_DAILY.
- **Findings and root causes (§5):** that any wire came back or was re-sent; card, Payoneer or other off-bank payments; the wire with no Processed notice; the company's own account; Combo Fighter's revenue or that it is held; who any token is; every total, per-payee figure, count of differing issues or deck replacement.
- **Hidden authorities:** the method's contents, the Trello card, the P&L, Arthur's mail, the #leapblock post.
- **Format and choreography:** markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …', and 'payee by payee', which reads as enumeration (pw1_prompt_lessons.md span 11).
- **Copied wording:** 'Can you take care of what he asked for?', word for word the LLC prompt (pw1_prompt_lessons.md span 4).
- **Friction and files:** none configured; no reference files or /app/artifact paths.

## 10 · Entity traps

`entity.py collisions` and `entity.py resolve` for every name below, verbatim:
```
SHARED_FIRST_NAMES (4)
  claire: ['Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]', 'Claire <github:PERSON_2360_GITHUB_USERNAME>']
  marcus: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Marcus Lee <marcus.lee@harmonygames.co>', 'Marcus <github:PERSON_0396_GITHUB_USERNAME>', 'Marcus <trello:c48a210d5c5a4b59231c6873>']
  martin: ['Martin Lewis <PERSON_0394_EMAIL>', 'Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]']
  thomas: ['Thomas Baker <thomas.baker@harmonygames.co>', 'Thomas <thomas@harmonygames.co> [persona thomas]']

SHARED_LAST_NAMES (5)
  baker: ['Owen Baker <owen.baker@harmonygames.co> [persona owen_baker]', 'Thomas Baker <thomas.baker@harmonygames.co>']
  bennett: ['Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]', 'Oscar Bennett <oscar.bennett@harmonygames.co>']
  brooks: ['Lauren Brooks <lauren@harmonygames.co>', 'Oliver Brooks <oliver.brooks@harmonygames.co> [persona oliver_brooks]']
  lawson: ['Julia Lawson <julia.lawson@harmonygames.co> [persona julia_lawson]', 'Peter Lawson <peter.lawson@harmonygames.co>']
  price: ['Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]', 'Nathan Price <nathan@harmonygames.co>']

LOOKALIKE_HANDLES_AND_ALIASES (15)
  - Gmail thread files of arthur.blake@harmonygames.co are named 'blake@harmonygames.co_*'
  - Gmail thread files of brian.foster@harmonygames.co are named 'brian@harmonygames.co_*'
  - Gmail thread files of calvin.price@harmonygames.co are named 'calvin@harmonygames.co_*'
  - Gmail thread files of claire.morgan@harmonygames.co are named 'claire@harmonygames.co_*'
  - Gmail thread files of frederick.stone@harmonygames.co are named 'frederick@harmonygames.co_*'
  - Gmail thread files of julia.lawson@harmonygames.co are named 'jlawson@harmonygames.co_*'
  - Gmail thread files of leonard.hayes@harmonygames.co are named 'leonard@harmonygames.co_*'
  - Gmail thread files of oliver.brooks@harmonygames.co are named 'oliver@harmonygames.co_*'
  - Gmail thread files of owen.baker@harmonygames.co are named 'owen@harmonygames.co_*'
  - Gmail thread files of samuel.turner@harmonygames.co are named 'samuel@harmonygames.co_*'
  - Gmail thread files of simon.walker@harmonygames.co are named 'simon@harmonygames.co_*'
  - Gmail thread files of vincent.parker@harmonygames.co are named 'vincent@harmonygames.co_*'
  - Gmail thread files of felix.young@harmonygames.co are named 'felixyoung@harmonygames.co_*'
  - Gmail thread files of oscar.bennett@harmonygames.co are named 'oscar@harmonygames.co_*'
  - Slack handle 'thomas' (U05F0A0D12F) belongs to Thomas Baker <thomas.baker@harmonygames.co> but equals the mailbox local part of Thomas <thomas@harmonygames.co> [persona thomas]

LOOKALIKE_EMAIL_LOCAL_PARTS (2)
  - 'thomas@' vs 'thomas.baker@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['Thomas Baker <thomas.baker@harmonygames.co>']
  - 'thomas@' vs 'thomaslee@': ['Thomas <thomas@harmonygames.co> [persona thomas]'] / ['? <thomaslee@harmonygames.co>']

TOKENS_MAPPING_TO_SEVERAL_ENTITIES (9)
  EMPLOYEE_0024: {'entities': ['scott <employee_0024@harmonygames.co>', '? <slack:EMPLOYEE_0024_SLACK_ID>', '? <trello:3d36d70154e6a715614e0d75>'], 'records': ['gcal.calendar_id=employee_0024@harmonygames.co', 'gcal.owner_email=employee_0024@harmonygames.co', 'linear.id=usr_EMPLOYEE_0024', 'linear.email=employee_0024@harmonygames.co', 'contacts.email=employee_0024@harmonygames.co', 'email.email=employee_0024@harmonygames.co', 'slack.id=EMPLOYEE_0024_SLACK_ID', 'trello.username=employee_0024']}
  EMPLOYEE_0032: {'entities': ['? <EMPLOYEE_0032_EMAIL>', 'Josh Dempsey <josh.dempsey@harmonygames.co>', '? <github:EMPLOYEE_0032_GITHUB_USERNAME>', '? <slack:EMPLOYEE_0032_SLACK_ID>'], 'records': ['confluence.id=user_EMPLOYEE_0032', 'gmail.mailbox=EMPLOYEE_0032_EMAIL', 'gdrive.email=EMPLOYEE_0032_EMAIL', 'linear.id=usr_EMPLOYEE_0032', 'linear.email=EMPLOYEE_0032_EMAIL', 'contacts.email=EMPLOYEE_0032_EMAIL', 'email.email=EMPLOYEE_0032_EMAIL', 'github.login=EMPLOYEE_0032_GITHUB_USERNAME', 'slack.id=EMPLOYEE_0032_SLACK_ID']}
  PERSON_2218: {'entities': ['? <PERSON_2218_EMAIL>', '? <github:PERSON_2218_GITHUB_USERNAME>'], 'records': ['linear.id=usr_PERSON_2218', 'linear.email=PERSON_2218_EMAIL', 'contacts.email=PERSON_2218_EMAIL', 'email.email=PERSON_2218_EMAIL', 'github.login=PERSON_2218_GITHUB_USERNAME']}
  PERSON_2360: {'entities': ['? <PERSON_2360_EMAIL>', 'Claire <github:PERSON_2360_GITHUB_USERNAME>'], 'records': ['github.login=PERSON_2360_GITHUB_USERNAME', 'email.email=PERSON_2360_EMAIL']}
  PERSON_3233: {'entities': ['? <PERSON_3233_EMAIL>', '? <github:PERSON_3233_GITHUB_USERNAME>', '? <slack:PERSON_3233_SLACK_ID>'], 'records': ['linear.id=usr_PERSON_3233', 'linear.email=PERSON_3233_EMAIL', 'contacts.email=PERSON_3233_EMAIL', 'email.email=PERSON_3233_EMAIL', 'github.login=PERSON_3233_GITHUB_USERNAME', 'slack.id=PERSON_3233_SLACK_ID']}
  PERSON_3335: {'entities': ['? <PERSON_3335_EMAIL>', '? <slack:PERSON_3335_SLACK_ID>'], 'records': ['contacts.email=PERSON_3335_EMAIL', 'email.email=PERSON_3335_EMAIL', 'slack.id=PERSON_3335_SLACK_ID']}
  PERSON_3935: {'entities': ['? <PERSON_3935_EMAIL>', '? <slack:PERSON_3935_SLACK_ID>'], 'records': ['email.email=PERSON_3935_EMAIL', 'slack.id=PERSON_3935_SLACK_ID']}
  PERSON_5275: {'entities': ['? <PERSON_5275_EMAIL>', '? <slack:PERSON_5275_SLACK_ID>'], 'records': ['contacts.email=PERSON_5275_EMAIL', 'email.email=PERSON_5275_EMAIL', 'slack.id=PERSON_5275_SLACK_ID']}
  PERSON_5360: {'entities': ['? <PERSON_5360_EMAIL>', '? <slack:PERSON_5360_SLACK_ID>'], 'records': ['email.email=PERSON_5360_EMAIL', 'slack.id=PERSON_5360_SLACK_ID']}

SEVERAL_IDS_IN_ONE_SERVICE (1)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: 2 github identities ['PERSON_0003_GITHUB_USERNAME', 'PERSON_2137_GITHUB_USERNAME'] (joins: ['exact_email', 'exact_name'])

PERSONA_ROLE_VS_CONTACTS_JOB (5)
  - Calvin Price <calvin.price@harmonygames.co> [persona calvin_price]: roster role 'Game Engineer (Unity VFX)' vs Contacts job 'Game Engineer (Unity/VFX)'
  - Frederick Stone <frederick.stone@harmonygames.co> [persona frederick_stone]: roster role 'Co-founder' vs Contacts job 'Commercial Lead, Marketing & Business Development'
  - Leonard Hayes <leonard.hayes@harmonygames.co> [persona leonard_hayes]: roster role 'Co-founder & Creative Director' vs Contacts job 'Co-founder & CEO'
  - Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]: roster role 'Artist' vs Contacts job 'Artist (VFX & Animation)'
  - Robert <robert@harmonygames.co> [persona robert]: roster role 'Co-Founder & Creative Director' vs Contacts job 'Co-founder & Chief Product Officer'

SHARED_CONTACT_JOB_TITLES (5)
  Game Designer: ['Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]', 'Samuel Turner <samuel.turner@harmonygames.co> [persona samuel_turner]']
  Game Developer: ['Thomas <thomas@harmonygames.co> [persona thomas]', 'Lucas <lucas@harmonygames.co>']
  Game Engineer: ['Brian Foster <brian.foster@harmonygames.co> [persona brian_foster]', 'Victor Barnes <victor.barnes@harmonygames.co> [persona victor_barnes]']
  General Counsel: ['Michelle Carter <michelle.carter@harmonygames.co>', 'Thomas Baker <thomas.baker@harmonygames.co>']
  User Acquisition Manager: ['George Miller <george.miller@harmonygames.co>', 'Megan Wilson <megan.wilson@harmonygames.co>', 'Victoria Lane <victoria.lane@harmonygames.co>']

UNRESOLVED (12)
  [ambiguous_name] github: mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  [ambiguous_name] github: mononym 'Claire' is an exact name of [] and the first name of ['email:claire.morgan@harmonygames.co'] -> candidates ['email:claire.morgan@harmonygames.co']
  [ambiguous_name] trello: mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co'] -> candidates ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co', 'github:PERSON_0396_GITHUB_USERNAME']
  [token_link] EMPLOYEE_0024: same token number across services but no shared exact email/name: not joined -> candidates ['email:employee_0024@harmonygames.co', 'slack:EMPLOYEE_0024_SLACK_ID', 'trello:3d36d70154e6a715614e0d75']
  [token_link] EMPLOYEE_0032: same token number across services but no shared exact email/name: not joined -> candidates ['email:EMPLOYEE_0032_EMAIL', 'email:josh.dempsey@harmonygames.co', 'github:EMPLOYEE_0032_GITHUB_USERNAME', 'slack:EMPLOYEE_0032_SLACK_ID']
  [token_link] PERSON_2218: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2218_EMAIL', 'github:PERSON_2218_GITHUB_USERNAME']
  [token_link] PERSON_2360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_2360_EMAIL', 'github:PERSON_2360_GITHUB_USERNAME']
  [token_link] PERSON_3233: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3233_EMAIL', 'github:PERSON_3233_GITHUB_USERNAME', 'slack:PERSON_3233_SLACK_ID']
  [token_link] PERSON_3335: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3335_EMAIL', 'slack:PERSON_3335_SLACK_ID']
  [token_link] PERSON_3935: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_3935_EMAIL', 'slack:PERSON_3935_SLACK_ID']
  [token_link] PERSON_5275: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5275_EMAIL', 'slack:PERSON_5275_SLACK_ID']
  [token_link] PERSON_5360: same token number across services but no shared exact email/name: not joined -> candidates ['email:PERSON_5360_EMAIL', 'slack:PERSON_5360_SLACK_ID']

INTEGRITY FLAGS (2)
  {'type': 'id_with_space', 'service': 'linear', 'id': 'usr_Victor Barnes'}
  {'type': 'name_mismatch_on_email_join', 'service': 'github', 'id': 'PERSON_2314_GITHUB_USERNAME', 'detail': "GitHub PERSON_2314_GITHUB_USERNAME joined by email but shows name 'Ryan' (entity is Frederick Stone)"}

ENTITY email:robert@harmonygames.co  name=Robert  kind=person  emails=['robert@harmonygames.co']
  persona: robert - Co-Founder & Creative Director / Executive
  slack      id=EMPLOYEE_0016_SLACK_ID, name=Robert, real_name=Robert, email=robert@harmonygames.co, is_bot=False, deleted=False, messages=129939, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=robert@harmonygames.co, threads=16233, messages=19169, first=2023-03-15, last=2026-02-13   [join: exact_email]
  gcal       calendar_id=robert@harmonygames.co, owner_email=robert@harmonygames.co, summary=Robert — primary, events=1229, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_9f7ba94f7526, email=robert@harmonygames.co, display_name=Robert, root_folders=['d_9f7ba94f7526d54d8482ba'], owned_items=223, last_modified=2026-02-12, files_shared_with=464   [join: exact_email]
  linear     id=usr_Robert, email=robert@harmonygames.co, name=Robert, is_active=True, last_activity=2025-10-27   [join: exact_email]
  github     login=EMPLOYEE_0016_GITHUB_USERNAME, name=Robert, email=robert@harmonygames.co, type=User, last_activity=2026-01-16   [join: exact_email]
  trello     id=3d06b73654d0c8940792514c, username=robert, fullName=Robert   [join: exact_name]
  confluence id=user_EMPLOYEE_0016, account_id=acct_EMPLOYEE_0016, email=robert@harmonygames.co, display_name=Robert, is_active=True, last_activity=2026-02-12   [join: exact_email]
  contacts   contact_id=5f647df33ba6e92fbd56b05b, name=Robert, email=robert@harmonygames.co, job=Co-founder & Chief Product Officer, is_user=True   [join: exact_email]
  last activity: {'slack': '2026-02-13', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-02-12', 'linear': '2025-10-27', 'github': '2026-01-16', 'confluence': '2026-02-12'}

no exact match for 'Leonard'
  candidate: email:leonard.hayes@harmonygames.co  Leonard Hayes  ['leonard.hayes@harmonygames.co']

ENTITY email:leonard.hayes@harmonygames.co  name=Leonard Hayes  kind=person  emails=['leonard.hayes@harmonygames.co']
  persona: leonard_hayes - Co-founder & Creative Director / Executive
  slack      id=EMPLOYEE_0038_SLACK_ID, name=Leonard Hayes, real_name=Leonard Hayes, email=leonard.hayes@harmonygames.co, is_bot=False, deleted=False, messages=143292, first_post=2023-03-15, last_post=2026-02-13   [join: exact_email]
  gmail      mailbox=leonard.hayes@harmonygames.co, threads=17635, messages=22648, first=2023-03-15, last=2026-02-13, thread_filename_alias=['leonard@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=leonard.hayes@harmonygames.co, owner_email=leonard.hayes@harmonygames.co, summary=Leonard Hayes — primary, events=1512, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_63fffeb4fab5, email=leonard.hayes@harmonygames.co, display_name=leonard.hayes@harmonygames.co, root_folders=['d_63fffeb4fab5233ed5bb73'], owned_items=817, last_modified=2026-02-11, files_shared_with=413   [join: exact_email]
  linear     id=usr_63fffeb4fab5233e, email=leonard.hayes@harmonygames.co, name=leonard.hayes@harmonygames.co, is_active=True, last_activity=2026-01-28   [join: exact_email]
  trello     id=PERSON_6094_TRELLO_USER_ID, username=leonard.hayes, fullName=Leonard Hayes, last_activity=2025-11-13   [join: exact_name]
  confluence id=user_EMPLOYEE_0038, account_id=acct_EMPLOYEE_0038, email=leonard.hayes@harmonygames.co, display_name=Leonard Hayes, is_active=True, last_activity=2026-02-09   [join: exact_email]
  contacts   contact_id=63fffeb4fab5233ed5bb73bf, name=Leonard Hayes, email=leonard.hayes@harmonygames.co, job=Co-founder & CEO, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2026-02-13', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-02-11', 'linear': '2026-01-28', 'trello': '2025-11-13', 'confluence': '2026-02-09'}

no exact match for 'Arthur'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']

no exact match for 'Blake'
  candidate: email:arthur.blake@harmonygames.co  Arthur Blake  ['arthur.blake@harmonygames.co']

ENTITY email:arthur.blake@harmonygames.co  name=Arthur Blake  kind=person  emails=['arthur.blake@harmonygames.co']
  persona: arthur_blake - Co-founder & CTO / Executive
  slack      id=EMPLOYEE_0025_SLACK_ID, name=Arthur Blake, real_name=Arthur Blake, email=arthur.blake@harmonygames.co, is_bot=False, deleted=False, messages=38591, first_post=2023-03-20, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=arthur.blake@harmonygames.co, threads=4721, messages=6876, first=2023-03-23, last=2026-02-13, thread_filename_alias=['blake@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=arthur.blake@harmonygames.co, owner_email=arthur.blake@harmonygames.co, summary=Arthur Blake — primary, events=824, last_event_before_clock=2026-02-12   [join: exact_email]
  gdrive     id=user_cc3e90160f49, email=arthur.blake@harmonygames.co, display_name=arthur.blake@harmonygames.co, root_folders=['d_cc3e90160f490686039986'], owned_items=269, last_modified=2026-01-15, files_shared_with=456   [join: exact_email]
  linear     id=usr_cc3e90160f490686, email=arthur.blake@harmonygames.co, name=arthur.blake@harmonygames.co, is_active=True, last_activity=2026-01-28   [join: exact_email]
  github     login=EMPLOYEE_0025_GITHUB_USERNAME, name=Arthur Blake, email=arthur.blake@harmonygames.co, type=User, last_activity=2026-02-13   [join: exact_email]
  trello     id=2162c1ba310341bf318f48b7, username=arthur.blake, fullName=Arthur Blake   [join: exact_name]
  confluence id=user_EMPLOYEE_0025, account_id=acct_EMPLOYEE_0025, email=arthur.blake@harmonygames.co, display_name=Arthur Blake, is_active=True, last_activity=2026-02-11   [join: exact_email]
  contacts   contact_id=cc3e90160f49068603998654, name=Arthur Blake, email=arthur.blake@harmonygames.co, job=Co-founder & CTO, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-13', 'gcal': '2026-02-12', 'gdrive': '2026-01-15', 'linear': '2026-01-28', 'github': '2026-02-13', 'confluence': '2026-02-11'}

ENTITY email:lucas@harmonygames.co  name=Lucas  kind=person  emails=['lucas@harmonygames.co']
  slack      id=U7CADAB457A, name=lucas, real_name=Lucas, email=lucas@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=lucas@harmonygames.co, owner_email=lucas@harmonygames.co, summary=Lucas — primary, events=1, last_event_before_clock=2024-09-28   [join: exact_email]
  gdrive     share_recipient=lucas@harmonygames.co, files_shared_with=3   [join: exact_email]
  linear     id=usr_Lucas, email=lucas@harmonygames.co, name=Lucas, is_active=True, last_activity=2024-10-16   [join: exact_email]
  github     login=PERSON_0484_GITHUB_USERNAME, name=Lucas, email=lucas@harmonygames.co, type=User, last_activity=2024-12-18   [join: exact_email]
  trello     id=93b95cf4d887f3d0956df501, username=lucas, fullName=Lucas   [join: exact_name]
  confluence id=user_STAFF_14, account_id=acct_STAFF_14, email=lucas@harmonygames.co, display_name=Lucas, is_active=True   [join: exact_email]
  contacts   contact_id=655f2fd84c2100fcc45498a1, name=Lucas, email=lucas@harmonygames.co, job=Game Developer, is_user=False   [join: exact_email]
  absent from: gmail
  last activity: {'gcal': '2024-09-28', 'linear': '2024-10-16', 'github': '2024-12-18'}

no exact match for 'Martin'
  candidate: email:martin.walsh@harmonygames.co  Martin Walsh  ['martin.walsh@harmonygames.co']
  candidate: email:PERSON_0394_EMAIL  Martin Lewis  ['PERSON_0394_EMAIL']

ENTITY email:martin.walsh@harmonygames.co  name=Martin Walsh  kind=person  emails=['martin.walsh@harmonygames.co']
  persona: martin_walsh - Game Designer / Design
  slack      id=EMPLOYEE_0033_SLACK_ID, name=Martin Walsh, real_name=Martin Walsh, email=martin.walsh@harmonygames.co, is_bot=False, deleted=False, messages=9492, first_post=2023-08-28, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=martin.walsh@harmonygames.co, threads=4543, messages=4868, first=2023-08-27, last=2026-02-13, thread_filename_alias=['martin.walsh@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=martin.walsh@harmonygames.co, owner_email=martin.walsh@harmonygames.co, summary=Martin Walsh — primary, events=631, last_event_before_clock=2026-01-14   [join: exact_email]
  gdrive     id=user_51f5f16d46e8, email=martin.walsh@harmonygames.co, display_name=martin.walsh@harmonygames.co, root_folders=['d_51f5f16d46e8cf55f5ee33'], owned_items=30, last_modified=2024-02-16, files_shared_with=144   [join: exact_email]
  linear     id=usr_51f5f16d46e8cf55, email=martin.walsh@harmonygames.co, name=martin.walsh@harmonygames.co, is_active=True, last_activity=2026-01-10   [join: exact_email]
  trello     id=ba9cc333cefad99228d6757d, username=martin.walsh, fullName=Martin Walsh   [join: exact_name]
  confluence id=user_EMPLOYEE_0033, account_id=acct_EMPLOYEE_0033, email=martin.walsh@harmonygames.co, display_name=Martin Walsh, is_active=True   [join: exact_email]
  contacts   contact_id=51f5f16d46e8cf55f5ee337b, name=Martin Walsh, email=martin.walsh@harmonygames.co, job=Game Designer, is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-13', 'gcal': '2026-01-14', 'gdrive': '2024-02-16', 'linear': '2026-01-10'}

ENTITY trello:c48a210d5c5a4b59231c6873  name=Marcus  kind=person  emails=[]
  trello     id=c48a210d5c5a4b59231c6873, username=marcus, fullName=Marcus   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, github, confluence, contacts
  last activity: -
ENTITY github:PERSON_0396_GITHUB_USERNAME  name=Marcus  kind=unidentified  emails=[]
  github     login=PERSON_0396_GITHUB_USERNAME, name=Marcus, type=User, last_activity=2026-02-10   [join: own_record (ambiguous name)]
  absent from: slack, gmail, gcal, gdrive, linear, trello, confluence, contacts
  last activity: {'github': '2026-02-10'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

no exact match for 'Victor'
  candidate: email:victor.barnes@harmonygames.co  Victor Barnes  ['victor.barnes@harmonygames.co']
  candidate: email:victoria.lane@harmonygames.co  Victoria Lane  ['victoria.lane@harmonygames.co']

ENTITY email:lauren@harmonygames.co  name=Lauren Brooks  kind=person  emails=['lauren@harmonygames.co']
  slack      id=EMPLOYEE_0035_SLACK_ID, name=Lauren Brooks, real_name=Lauren Brooks, email=lauren@harmonygames.co, is_bot=False, deleted=False, messages=71, first_post=2025-10-10, last_post=2026-01-06   [join: exact_email]
  gmail      mailbox=lauren@harmonygames.co, threads=28, messages=29, first=2025-10-10, last=2026-01-06, thread_filename_alias=['lauren@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=lauren@harmonygames.co, owner_email=lauren@harmonygames.co, summary=lauren@harmonygames.co — primary, events=14, last_event_before_clock=2025-12-26   [join: exact_email]
  gdrive     id=user_b614e9f9cb3f, email=lauren@harmonygames.co, display_name=lauren@harmonygames.co, root_folders=['d_b614e9f9cb3f0f5a53dfd1'], owned_items=6, last_modified=2025-10-13, files_shared_with=105   [join: exact_email]
  confluence id=user_STAFF_1, account_id=acct_STAFF_1, email=lauren@harmonygames.co, display_name=Lauren Brooks, is_active=True   [join: exact_email]
  absent from: linear, github, trello, contacts
  last activity: {'slack': '2026-01-06', 'gmail': '2026-01-06', 'gcal': '2025-12-26', 'gdrive': '2025-10-13'}

no exact match for 'Brooks'
  candidate: email:oliver.brooks@harmonygames.co  Oliver Brooks  ['oliver.brooks@harmonygames.co']
  candidate: email:lauren@harmonygames.co  Lauren Brooks  ['lauren@harmonygames.co']

ENTITY email:nathan@harmonygames.co  name=Nathan Price  kind=person  emails=['nathan@harmonygames.co']
  github     login=PERSON_5170_GITHUB_USERNAME, name=Nathan Price, email=nathan@harmonygames.co, type=User, last_activity=2024-07-19   [join: exact_email]
  contacts   contact_id=6fac1701283890f8af5da90d, name=Nathan Price, email=nathan@harmonygames.co, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, gdrive, linear, trello, confluence
  last activity: {'github': '2024-07-19'}

no exact match for 'Graham Porter'

no exact match for 'Oleg'

ENTITY email:ozhan@harmonygames.co  name=Ozhan  kind=person  emails=['ozhan@harmonygames.co']
  slack      id=U1F37AF74B0, name=ozhan, real_name=Ozhan, email=ozhan@harmonygames.co, is_bot=False, deleted=False, messages=0   [join: exact_email]
  gcal       calendar_id=ozhan@harmonygames.co, owner_email=ozhan@harmonygames.co, summary=Ozhan — primary, events=0   [join: exact_email]
  linear     id=usr_1f37af74b0393f3c, email=ozhan@harmonygames.co, name=ozhan@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=3fcb45782f26eb87f3f489f5, username=ozhan, fullName=Ozhan   [join: exact_name]
  confluence id=user_STAFF_7, account_id=acct_STAFF_7, email=ozhan@harmonygames.co, display_name=Ozhan, is_active=True   [join: exact_email]
  contacts   contact_id=cnt_1f37af74b039, name=Ozhan, email=ozhan@harmonygames.co, job=Freelance Character Animator, is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: -

no exact match for 'Frederick'
  candidate: email:frederick.stone@harmonygames.co  Frederick Stone  ['frederick.stone@harmonygames.co']

ENTITY email:samuel.turner@harmonygames.co  name=Samuel Turner  kind=person  emails=['samuel.turner@harmonygames.co']
  persona: samuel_turner - Game Designer / Design
  slack      id=EMPLOYEE_0004_SLACK_ID, name=Samuel Turner, real_name=Samuel Turner, email=samuel.turner@harmonygames.co, is_bot=False, deleted=False, messages=4661, first_post=2024-02-20, last_post=2025-10-24   [join: exact_email]
  gmail      mailbox=samuel.turner@harmonygames.co, threads=3928, messages=4603, first=2024-02-20, last=2025-10-24, thread_filename_alias=['samuel@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=samuel.turner@harmonygames.co, owner_email=samuel.turner@harmonygames.co, summary=Samuel Turner — primary, events=355, last_event_before_clock=2025-10-24   [join: exact_email]
  gdrive     id=user_caafeec2804b, email=samuel.turner@harmonygames.co, display_name=samuel.turner@harmonygames.co, root_folders=['d_caafeec2804b3a67ce46aa'], owned_items=24, last_modified=2025-07-04, files_shared_with=110   [join: exact_email]
  linear     id=usr_caafeec2804b3a67, email=samuel.turner@harmonygames.co, name=samuel.turner@harmonygames.co, is_active=True, last_activity=2025-10-23   [join: exact_email]
  github     login=EMPLOYEE_0004_GITHUB_USERNAME, name=Samuel Turner, email=samuel.turner@harmonygames.co, type=User, last_activity=2025-10-24   [join: exact_email]
  trello     id=4ac40f0fbbad94d9e0e2df2a, username=samuel.turner, fullName=Samuel Turner   [join: exact_name]
  confluence id=user_STAFF_18, account_id=acct_STAFF_18, email=samuel.turner@harmonygames.co, display_name=Samuel Turner, is_active=True   [join: exact_email]
  contacts   contact_id=caafeec2804b3a67ce46aabb, name=Samuel Turner, email=samuel.turner@harmonygames.co, job=Game Designer, is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-24', 'gmail': '2025-10-24', 'gcal': '2025-10-24', 'gdrive': '2025-07-04', 'linear': '2025-10-23', 'github': '2025-10-24'}

no exact match for 'Brian'
  candidate: email:brian.foster@harmonygames.co  Brian Foster  ['brian.foster@harmonygames.co']

ENTITY email:oliver.brooks@harmonygames.co  name=Oliver Brooks  kind=person  emails=['oliver.brooks@harmonygames.co']
  persona: oliver_brooks - Senior Game Engineer / Engineering
  slack      id=EMPLOYEE_0003_SLACK_ID, name=Oliver Brooks, real_name=Oliver Brooks, email=oliver.brooks@harmonygames.co, is_bot=False, deleted=False, messages=23993, first_post=2024-08-12, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=oliver.brooks@harmonygames.co, threads=1687, messages=2445, first=2024-08-08, last=2026-02-12, thread_filename_alias=['oliver@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=oliver.brooks@harmonygames.co, owner_email=oliver.brooks@harmonygames.co, summary=Oliver Brooks — primary, events=315, last_event_before_clock=2026-01-01   [join: exact_email]
  gdrive     id=user_bdf01b53c6a9, email=oliver.brooks@harmonygames.co, display_name=oliver.brooks@harmonygames.co, root_folders=['d_bdf01b53c6a92c5e167c65'], owned_items=8, last_modified=2025-09-01, files_shared_with=112   [join: exact_email]
  linear     id=usr_bdf01b53c6a92c5e, email=oliver.brooks@harmonygames.co, name=oliver.brooks@harmonygames.co, is_active=True, last_activity=2025-11-20   [join: exact_email]
  github     login=EMPLOYEE_0003_GITHUB_USERNAME, name=Oliver Brooks, email=oliver.brooks@harmonygames.co, type=User, last_activity=2026-02-13   [join: exact_email]
  trello     id=12c4a9dcd2d37a25a8d3b557, username=oliver.brooks, fullName=Oliver Brooks   [join: exact_name]
  confluence id=user_EMPLOYEE_0003, account_id=acct_EMPLOYEE_0003, email=oliver.brooks@harmonygames.co, display_name=Oliver Brooks, is_active=True, last_activity=2025-10-01   [join: exact_email]
  contacts   contact_id=bdf01b53c6a92c5e167c658c, name=Oliver Brooks, email=oliver.brooks@harmonygames.co, job=Senior Game Engineer, is_user=False   [join: exact_email]
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-12', 'gcal': '2026-01-01', 'gdrive': '2025-09-01', 'linear': '2025-11-20', 'github': '2026-02-13', 'confluence': '2025-10-01'}

ENTITY email:calvin.price@harmonygames.co  name=Calvin Price  kind=person  emails=['calvin.price@harmonygames.co']
  persona: calvin_price - Game Engineer (Unity VFX) / Engineering
  slack      id=EMPLOYEE_0006_SLACK_ID, name=Calvin Price, real_name=Calvin Price, email=calvin.price@harmonygames.co, is_bot=False, deleted=False, messages=12359, first_post=2023-03-29, last_post=2025-10-24   [join: exact_email]
  gmail      mailbox=calvin.price@harmonygames.co, threads=8213, messages=9971, first=2023-03-29, last=2025-11-13, thread_filename_alias=['calvin@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=calvin.price@harmonygames.co, owner_email=calvin.price@harmonygames.co, summary=Calvin Price — primary, events=455, last_event_before_clock=2025-10-24   [join: exact_email]
  gdrive     id=user_49b9dfa5208d, email=calvin.price@harmonygames.co, display_name=calvin.price@harmonygames.co, root_folders=['d_49b9dfa5208d400d9b3937'], owned_items=1918, last_modified=2025-02-14, files_shared_with=132   [join: exact_email]
  linear     id=usr_49b9dfa5208d400d, email=calvin.price@harmonygames.co, name=calvin.price@harmonygames.co, is_active=True, last_activity=2026-01-01   [join: exact_email]
  github     login=PERSON_0003_GITHUB_USERNAME, name=Calvin Price, email=calvin.price@harmonygames.co, type=User, last_activity=2025-10-22   [join: exact_email]
  github     login=PERSON_2137_GITHUB_USERNAME, name=Calvin Price, type=User, last_activity=2025-10-09   [join: exact_name]
  trello     id=ca5bb4c09fbf2a437f04531e, username=calvin.price, fullName=Calvin Price   [join: exact_name]
  confluence id=user_STAFF_19, account_id=acct_STAFF_19, email=calvin.price@harmonygames.co, display_name=Calvin Price, is_active=True   [join: exact_email]
  contacts   contact_id=49b9dfa5208d400d9b3937ca, name=Calvin Price, email=calvin.price@harmonygames.co, job=Game Engineer (Unity/VFX), is_user=False   [join: exact_email]
  last activity: {'slack': '2025-10-24', 'gmail': '2025-11-13', 'gcal': '2025-10-24', 'gdrive': '2025-02-14', 'linear': '2026-01-01', 'github': '2025-10-22'}

ENTITY email:PERSON_0394_EMAIL  name=Martin Lewis  kind=person  emails=['PERSON_0394_EMAIL']
  gdrive     share_recipient=PERSON_0394_EMAIL, files_shared_with=1   [join: exact_email]
  contacts   contact_id=42869c73053b8c1b750ca3b6, name=Martin Lewis, email=PERSON_0394_EMAIL, is_user=False   [join: exact_email]
  absent from: slack, gmail, gcal, linear, github, trello, confluence
  last activity: -

ENTITY email:marcus.bennett@harmonygames.co  name=Marcus Bennett  kind=person  emails=['marcus.bennett@harmonygames.co']
  persona: marcus_bennett - Artist / Design
  slack      id=EMPLOYEE_0002_SLACK_ID, name=Marcus Bennett, real_name=Marcus Bennett, email=marcus.bennett@harmonygames.co, is_bot=False, deleted=False, messages=29373, first_post=2023-09-28, last_post=2026-02-12   [join: exact_email]
  gmail      mailbox=marcus.bennett@harmonygames.co, threads=4329, messages=4355, first=2023-09-28, last=2026-02-11, thread_filename_alias=['marcus.bennett@harmonygames.co']   [join: exact_email]
  gcal       calendar_id=marcus.bennett@harmonygames.co, owner_email=marcus.bennett@harmonygames.co, summary=Marcus Bennett — primary, events=663, last_event_before_clock=2026-02-03   [join: exact_email]
  gdrive     id=user_c77c50cc15c5, email=marcus.bennett@harmonygames.co, display_name=marcus.bennett@harmonygames.co, root_folders=['d_c77c50cc15c5342d638ebb'], owned_items=47335, last_modified=2025-09-10, files_shared_with=137   [join: exact_email]
  linear     id=usr_c77c50cc15c5342d, email=marcus.bennett@harmonygames.co, name=marcus.bennett@harmonygames.co, is_active=True, last_activity=2025-12-03   [join: exact_email]
  trello     id=7a20445f698bc5871ffd17f5, username=marcus.bennett, fullName=Marcus Bennett   [join: exact_name]
  confluence id=user_EMPLOYEE_0002, account_id=acct_EMPLOYEE_0002, email=marcus.bennett@harmonygames.co, display_name=Marcus Bennett, is_active=True   [join: exact_email]
  contacts   contact_id=c77c50cc15c5342d638ebb21, name=Marcus Bennett, email=marcus.bennett@harmonygames.co, job=Artist (VFX & Animation), is_user=False   [join: exact_email]
  absent from: github
  last activity: {'slack': '2026-02-12', 'gmail': '2026-02-11', 'gcal': '2026-02-03', 'gdrive': '2025-09-10', 'linear': '2025-12-03'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

ENTITY email:marcus.lee@harmonygames.co  name=Marcus Lee  kind=person  emails=['marcus.lee@harmonygames.co']
  slack      id=PERSON_2705_SLACK_ID, name=Marcus Lee, real_name=Marcus Lee, email=marcus.lee@harmonygames.co, is_bot=False, deleted=False, messages=199, first_post=2023-12-19, last_post=2025-12-18   [join: exact_email]
  gcal       calendar_id=marcus.lee@harmonygames.co, owner_email=marcus.lee@harmonygames.co, summary=Marcus Lee — primary, events=3, last_event_before_clock=2024-09-26   [join: exact_email]
  linear     id=usr_b501f018a4c5319f, email=marcus.lee@harmonygames.co, name=marcus.lee@harmonygames.co, is_active=True   [join: exact_email]
  trello     id=54b24ad13c96c74bd0376532, username=marcus.lee, fullName=Marcus Lee   [join: exact_name]
  confluence id=user_STAFF_5, account_id=acct_STAFF_5, email=marcus.lee@harmonygames.co, display_name=Marcus Lee, is_active=False   [join: exact_email]
  contacts   contact_id=c7b13b5c524387cbef98ab8d, name=Marcus Lee, email=marcus.lee@harmonygames.co, job=AppLovin Business Development (UA partner, not an employee), is_user=False   [join: exact_email]
  absent from: gmail, gdrive, github
  last activity: {'slack': '2025-12-18', 'gcal': '2024-09-26'}
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of [] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']
  UNRESOLVED (ambiguous_name): mononym 'Marcus' is an exact name of ['github:PERSON_0396_GITHUB_USERNAME'] and the first name of ['email:marcus.bennett@harmonygames.co', 'email:marcus.lee@harmonygames.co']

no exact match for 'Deel'

no exact match for 'Singular'

no exact match for 'Dixelar'
```
| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |
|---|---|---|---|
| Leonard Hayes | no exact match on 'Leonard' alone; one candidate | co-founder, sender of the ask | leonard.hayes@harmonygames.co |
| Arthur Blake ('Blake') | no exact match on 'Blake' alone; one candidate. Mail files use blake@harmonygames.co | one person; share to the arthur.blake address | arthur.blake@harmonygames.co |
| Robert | — | the persona; Slack EMPLOYEE_0016_SLACK_ID | robert@harmonygames.co |
| Martin Walsh (ENG-2454) | Martin Lewis (PERSON_0394_EMAIL); Martin on the Leapblock notes is the same Walsh | the note says 'same Martin as on Leapblock' | martin.walsh@harmonygames.co, ENG-2454 |
| Marcus (Eveline Art) | Marcus Bennett, Marcus Lee, the Trello and GitHub Marcus | ENG-2440's note, 'Marcus’s company'; bare name, resolved only by the issue | ENG-2440 |
| Lauren Brooks | Oliver Brooks | the contact row 564155d70112411151e512a6 is Lauren | lauren@harmonygames.co |
| Nathan Price | Calvin Price | ENG-2453 is Nathan | nathan@harmonygames.co |
| Lucas | — | ENG-2447's token [PERSON_NAME_36400] is on all five receipts | lucas@harmonygames.co |
| Graham Porter | no entity record (resolve: no exact match) | appears by name on the notice and issue only | ENG-2449 |
| Oleg | no entity record (resolve: no exact match) | appears in the ENG-2459 note | ENG-2459 |
| Dixelar | no entity record (resolve: no exact match) | the name on the payment requests in Robert's mail, which the notes call Oleg | ENG-2459 |
| Deel, Inc. ***8380 | [ORG_NAME_0057], Inc. ***8380 | two spellings, one account (NB-12) | ENG-2438 |
| Singular Labs Inc ***4015 | [SOURCE_ORG_0351] Labs Inc ***4015 | two spellings, one account (NB-12) | ENG-2443 |
| the Payee history project | base projects on team_ENG | the only project of that name | ENG-2438 |
| Angel note: how to count the money | Angel note working; Angel note money page | the doc is the method; the others are the layout and the replaced plan | f_6feda53b2382c63bf47b25 |

## 11 · Pre-submit checklist

- [ ] Reads like Robert: first person, plain, no spec-sheet layout
- [ ] Names only the two anchors (§6); nothing from §9
- [ ] Names no tool, server or parameter
- [ ] States no root cause
- [ ] Every sentence is needed; deleting one changes something
- [ ] Every date sits before the clock or is a real future date; Thursday and Tuesday checked against §7
- [ ] Carries the three deliverables and their destinations: the sheet in his Drive, shared with Leonard and Blake; the project worked through; the reply in #winddown with the link
- [ ] No hint, riddle, hedge, if-chain or audit wording
- [ ] Keeps 'angel calls' and 'bet', which hold the investor framing; no 'payee by payee'; not the LLC prompt's sentence
- [ ] Asks for investigation and action across at least two services
- [ ] Every fair reading in §4b is still fair against the final text
- [ ] 20 to 4,000 words
- [ ] Run `/create-prompt-writing check` before `/prompt`

## 12 · Blockers and routed defects

No blocker in this brief. Error/async: the requester skipped the stage; friction is none and 03_Error_Async_Config.txt records that (digest b51534f72800). Reference files: none exist.

Routed to /create-injection for the requester's decision. My read is that neither needs a change, because no graded figure rests on them:

- F21 Arthur's 'Done!' corroborates only: F3's closing-file sentence with F19 and F20 settles Leapblock.
- F26 the post naming Node Media gives a display name: F27 settles the bucket, and §4b leaves the Payee label free. The surface's X6 keys its row on the name 'Node Media', so the rubric must key on ***0115 instead.

The platform /prompt review of rev4 (plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md, attempt 6aeed82596dcfe103f9f74d9) failed at 2 on two record gaps. Rev6 closes both, verified on disk this run: Leonard's third note on ENG-2455 settles Lauren Brooks's bucket (F39; its I1 and I2), and the method now holds Combo Fighter's revenue off the page, the deck and the reply (F3, F32; its I3, NB-26). The prompt is unchanged. ENG-2459 stays zero, Marketing, reason first (F36, F37; its fork F5).

Two facts pass only through a read around the hit, which runs rarely do (sc4 §3): F13 and F16. They stay YES because a natural query lands inside the right exchange. Martin's bucket no longer needs one: the ENG-2454 note now names the laptop (F31).

For /create-rubric-writing: 01_Gradable_Surface.json is narrower than §4b or misses a graded fact in these slots, which the rubric must widen or add to rather than copy:

- D4 reads a thread on 1770945821.640039 only; §4b accepts either post or top-level.
- D1 reads the parent d_9f7ba94f7526d54d8482ba only; §4b accepts any folder Robert owns.
- X9 reads the Company cell; §4b also accepts the row's Note.
- The ledger's name_regex needs a word like angel, seed, bet, money or payee in the title; §4b accepts any title.
- X6 and the other field slots key on truth names; NB-12 says key on account endings.
- C1 to C4 cover four reason comments; no slot covers ENG-2459, the fifth.
- R2 matches only the word 'deck'; plan a real row for the three cost figures and the brought-in line, with Combo Fighter left off (pw1_prompt_lessons.md).
- V3 is gone (29 slots, weight 91), so no slot grades Combo Fighter's revenue, which matches the method's hold; no rubric row may grade a Combo Fighter figure.

Unverified: the Leapblock invoice PDFs (f_06f42106818045db3b7d0d and siblings) can't be read through hg.py, so nothing here confirms they total the Sep 2023 wire; the Chase top-up reason in F22 is seeded and no base record states it; live search ranking and matching differ from persona_view (§5a), so findability is proven for this tool only; the off-bank census covers the routes in the VERIFY lines, and hits were judged by subject except the four 'Payment Receipt' threads, which were read (a registered-agent receipt, an ad prepayment and two inbound deposit notices, none a contractor payment).

Folded in: plan/research/pw1_prompt_lessons.md, which reviewed an earlier 115-word candidate; the platform /prompt report plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md; and the cold reviews listed in §13.

## 13 · Self-review

Walked Evals/1_Prompt_Eval.md Phases 1 to 3 against this brief. 04_Prompt.txt exists and is the text the platform reviewed; check mode re-runs every C-check on it. The rows below cover every area the brief can settle.

| Area | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Fair readings (C6) | Leapblock stays at $374,654: 'what the banks say is our ground source of truth', and a payee's statement is not a bank. | f_6feda53b2382c63bf47b25 says 'If someone we paid closes out their file with us and tells us what they received, that beats the notices for them', and C05URGU759U/1770971846.479179 is that closing post. It ties to the notices in every year once F20's wire is added (VERIFY lines, §5a). A newer source settles it: case K49-newer-source. | settled |
| Fair readings (C6) | ENG-2459 stays at $125: the notice says Processed, and Robert's mail holds Dixelar's requests for that amount, so a receipt reached him. | Leonard's note on ENG-2459 says the wire came back, which meets f_6feda53b2382c63bf47b25 'unless one of us has said the money came back'. robert@harmonygames.co/1798239548116390324 and robert@harmonygames.co/1811158112675912556 are payment requests. 'Thanks for your payment' returns 0 as Robert and sits only in Leonard's mailbox (positive control, VERIFY lines), and the method counts what 'reached your mail'. Zero, Marketing, reason first. | settled |
| Fair readings (C6) | Lucas should carry the fees, $7,528.96 on 'money that left', or $8,600 if every receipt mail is summed. | f_6feda53b2382c63bf47b25 says 'at the amount sent, not the fee'. VERIFY shows 5 tracking numbers and 1 forwarded copy in robert@harmonygames.co/1802092844284446043, so $7,525.00. | settled |
| Fair readings (C6) | Lauren Brooks is Build by date, as a monthly contractor on the team, or Company: the platform found no record deciding it. | That was rev4 (plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md I1, attempt 6aeed82596dcfe103f9f74d9). Rev6 adds Leonard's note on ENG-2455, 'her contract had her running our paid UA on telegram, so she’s marketing, not build' (F39), which agrees with f_20a0df3860bb5731d22f07 Exhibit A and C05KNDCHAAG/1760125440.959149. A record by the payee's own approver now names the bucket. | settled |
| Fair readings (C6) | Martin's 1,999 BGN is Build, ZM by date, as the platform read it. | ENG-2454's note now reads 'paid him direct for his laptop, not through Leapblock' (F31), C04UEQVDVB7/1761844454.096829 asks about the laptop, and f_6feda53b2382c63bf47b25 puts equipment in Company. | settled |
| Fair readings (C6) | The reply must give Combo Fighter's revenue, because the prompt asks what each bet brought in. | f_6feda53b2382c63bf47b25 says 'Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me'. The prompt hands the counting to Leonard ('how he wants it counted'), and an incorporated source governs the decisions it covers (playbook fair-reading step 2). §4b accepts the figure left blank, held or 'to come'; it closes the platform's I3 (NB-26). | settled |
| Fair readings (C6) | The traps the platform called settled could still fork on rev6. | plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md forks F2 to F7 settle MotMot, Leapblock, JPMorgan, Oleg, the Western Union receipts and Node Media on records Robert can see. Rev6 changes none of those records apart from Oleg's note wording, which still says the wire came back (F36). | settled |
| Fair readings (C6) | Singular is Marketing, since attribution serves ads, or splits across the games. | ENG-2443's note says 'attribution tool, not one game', and f_6feda53b2382c63bf47b25 puts 'tools' and anything not for one game in Company. | settled |
| Fair readings (C6) | The reply belongs only under the post that says 'tell me here'. | C0ADGSZKR3R/1770945859.212469 says it, but the draft wording says 'in #winddown', and Eval 1 §2.1 fails only materially incompatible outcomes. All three placements reach Leonard with the same content, so §4b accepts them. Surface D4 is flagged in §12. | accepted outcomes |
| Fair readings (C6) | Brought-in figures can sit in the reply alone, since the layout has no column for them. | C0ADGSZKR3R/1770945821.640039 defines the page as cost and brought in, and the draft wording says 'Build that page as a sheet', so they belong on the sheet. f_3304033843904a426f3c00 has no column, so §4b takes any row or tab. | settled |
| Fair readings (C6) | The run should edit the deck, since it is told what changes. | C0ADGSZKR3R/1770945859.212469 ends 'I’ll update it myself', so the deck is his edit. §4b keeps an edit unpenalised because f_a4b3c4287a4314d8e532e1 is shared with Robert. | accepted outcomes |
| Assignment fit (C4) | Reconciling payees is bookkeeping, so Business Function scores 3 as it did on the winddown task. | The platform scored Business Function 5 on this exact prompt (plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md, Phase 1: 'a founder deliverable for the angel calls'). It keeps 'angel calls', 'bet' and the draft deck, which pw1_prompt_lessons.md row 3 named as the guard. | settled on the platform |
| Clarity (C7) | 'work through the project the way he wants' is a vague verb with no stated write. | f_6feda53b2382c63bf47b25 states the writes, and Eval 1 §2.6 treats a vague verb as Minor when records hold the rule. Two competing named writes are absent. | Minor at most |
| Clarity (C7) | 'one straight page' could mean a document, not the sheet. | The draft wording says 'Build that page as a sheet', and C0ADGSZKR3R/1770945859.212469 sets the layout. A doc beside it changes no graded write. | settled |
| Incorporation (C8) | 'He laid out how he wants it counted' could lead to the Trello plan instead of the doc. | C0ADGSZKR3R/1770945821.640039 names the doc by title, F3's search has one hit, and f_6feda53b2382c63bf47b25 says it replaces the plan on 698e55f9af74d68d679de7b3. | unique |
| Incorporation (C8) | The method might hand over the answer. | f_6feda53b2382c63bf47b25 states tests and dates and no payee or total. The closing-file sentence names no payee. fact_check --no-leak passed in the dossier (01_Grounding_Dossier.md). | instructions only |
| Truthfulness (C17) | 'On Thursday' is false: the ts falls on Friday in UTC. | C0ADGSZKR3R/1770945821.640039 is 2026-02-13T01:23:41Z, which is Thu Feb 12, 5:23 PM PT; persona dates are Pacific (§7). | true |
| Truthfulness (C17) | 'Blake' could be someone else, and 'angel calls on Tuesday' could be loose. | entity.py resolve 'Blake' gives one candidate, arthur.blake@harmonygames.co (§10). evt_f21476dc404329f67fd60d is Tue Feb 17, 2026. | true |
| Feasibility / ACL (C18–C19) | Robert may not read a deciding record, or the Done state may not exist. | check-sql verdict PASS with 0 load-bearing rows hidden (§5a), and Done is a state on team_ENG issues (hg.py search linear, 1,944 base issues). All six writes are in catalog.json. | feasible |
| Feasibility / ACL (C18–C19) | Exact revenue may not survive the tool path. | snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY sums to the cent through hg.py; V2 agrees. Combo Fighter's is held by the method and graded nowhere (NB-26). | feasible |
| Feasibility / ACL (C18–C19) | The prompt asks what each bet brought in while the method withholds one, which is conflicting instructions. | The prompt incorporates the method ('He laid out how he wants it counted'), and f_6feda53b2382c63bf47b25 narrows Leonard's own ask; a reply that says Combo Fighter's figure is held answers each bet. No write becomes impossible. Check mode should re-test this on the final text. | feasible; watch at check |
| Contrived register (C15–C16) | 'how it should look' hides a layout the persona knows, which is the hidden-destination pattern. | The destination is named ('in my Drive'), and the clause only points at C0ADGSZKR3R/1770945859.212469: pw1_prompt_lessons.md §1b shows 'His email lays out what he's after.' rejected as a defect, and control-named-destination passes, unlike K42-hidden-destination. | ordinary |
| Contrived register (C15–C16) | Three deliverables in order could read as a command list. | Deliverables and who to tell are not sequenced method steps (Eval 1 §1.3.1): control-plain-request, unlike K1-audit-form. | ordinary |

Fair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above. Facts were re-read in this run, not carried from notes: 132 notices, 23 account endings, Leapblock by year, 5 receipts, the off-bank census, both revenue tables, and every §5a query. The root cause appears only in §5; assemble_brief.py stops if a cause word reaches §1 to §4.

Independent reviews. The platform /prompt review of rev4 (plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md, attempt 6aeed82596dcfe103f9f74d9, SQL 872bbb307710) is on disk and was read in this run: it failed at 2 on Lauren Brooks's bucket (UGT 2, Clarity 1) and Combo Fighter's revenue (Cross-Service Coherence 1), scored every other dimension 5, and settled the Leapblock close-out, JPMorgan, the Western Union receipts, Oleg, MotMot and Node Media. The others were reported to me by the coordinator in this session; none is saved as a file and I have not seen their text, so these are the coordinator's summaries, not findings I checked: a rev1 blind sweep (36 forks, 18 open); a rev2 sweep in which a keyless reviewer reproduced the three build totals, Company 49,625.00 plus BGN 1,999 and that revision's revenue figures, with prompt findings none; a cold Eval 1 review (NON-FAIL on Clarity and Coherence, both reported fixed on the record in rev3); a fourth cold reviewer on the rev3 wording, whose two small findings went into rev4; and a cold reviewer on rev5 who found the reply gap and the Martin reading, both reported fixed in rev6. I verified the Martin fix (F31). For the reply gap I can only say the rev6 change that touches the reply is the method's 'and when you tell me' clause on Combo Fighter; Leonard's two posts are unchanged since rev3. No cold review has covered rev6 itself.

Unresolved: F21 and F26 are routed for the requester's decision (§12); the surface slots listed in §12 need widening at the rubric stage; the items marked Unverified in §12 stand; no cold review has covered rev6; the prompt/method split on Combo Fighter's revenue should be re-tested in check mode; check mode re-tests every point on 04_Prompt.txt.

```
STAGE GATE prompt-writing: PASS — Task_Authoring/task_inputsS2 · 04_Prompt_Writing_Brief.md#90722254898a · 00_Assigments.md#1555ee0dca48 · 01_Grounding_Dossier.md#d9c0dda36e9c · 01_Universe_Inject.sql#ad50f039b5c2 · 03_Error_Async_Config.txt#b51534f72800 · __context__#4ae6fe0e2394 · __assignment__#a525bbe797a2 · __policy__#dc4ab5df3cdd · __gate_policy__#f8638415ca2c · __review__#82014072ec39 · blocking 0 · warnings 0 · checks 24
[PASS] assignment.v3_context: Robert / Co-founder & Creative Director; easy cap <90%; freeze 2026-02-14T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe normal; KB bound; clock Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)
[PASS] structure.outputs: 1 output(s) present: 04_Prompt_Writing_Brief.md
[PASS] structure.inputs: 3 input(s) present: 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql, 03_Error_Async_Config.txt)
[PASS] chain.injection: upstream 'injection' PASS pasted and current (01_Universe_Inject.sql#ad50f039b5c2, 01_Hardness_Manifest.json#7f5ee8286c9a, 01_Grounding_Dossier.md#d9c0dda36e9c, solver/solver.py#4c9f139f4940, 01c_Dispositions.json#b1277995c8e8, 01c_Preflight_Report.json#ce8d48bc8fb8, 00_Assigments.md#1555ee0dca48, 01_Scenario_Design.md#4cb14f49ed40, 01_Hardness_Manifest.draft.json#5fcaf8d794b0, 01_Gradable_Surface.json#69b55f424206, __context__#4ae6fe0e2394, __assignment__#a525bbe797a2, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#49e9a0e1b1f7)
[PASS] chain.error-async: upstream 'error-async' PASS pasted and current (03_Error_Async_Config.txt#b51534f72800, 00_Assigments.md#1555ee0dca48, 01_Grounding_Dossier.md#d9c0dda36e9c, 01_Universe_Inject.sql#ad50f039b5c2, __context__#4ae6fe0e2394, __assignment__#a525bbe797a2, __policy__#dc4ab5df3cdd, __gate_policy__#f8638415ca2c, __review__#49e9a0e1b1f7)
[PASS] structure.sections: 14 required sections present and non-empty (04_Prompt_Writing_Brief.md)
[PASS] structure.placeholders: no placeholders in 04_Prompt_Writing_Brief.md
[PASS] evidence.situation: 3/3 items carry a source pointer (min 100%)
[PASS] evidence.final_state: 26/26 items carry a source pointer (min 100%)
[PASS] evidence.discovery_map: 39/39 items carry a source pointer (min 100%)
[PASS] evidence.dates: 12/12 items carry a source pointer (min 100%)
[PASS] evidence.entity_traps: 15/15 items carry a source pointer (min 100%)
[PASS] tool.search_as_persona: 39 facts proven findable by persona_view search as robert
[PASS] reach.brief: 46 scoped load-bearing ids YES for robert
[PASS] tool.entity: entity.py collisions/resolve output pasted in the identity-trap section
[PASS] structure.accepted_outcomes: V3 accepts multiple fair outcomes; see v3.fair_outcomes_review
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 23 evidenced counter-readings (of 23 found; need ≥ 6) in 04_Prompt_Writing_Brief.md
[PASS] review.coverage: self-review addresses all 6 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.fair_outcomes_review: current accepted outcomes and considered alternatives recorded; multiple fair outcomes are allowed
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

