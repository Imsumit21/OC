## PROMPT EVALUATION REPORT

### Task: Robert builds Leonard's one-page "what each bet cost to build and brought in" sheet from the SVB notices and the Payee history project, shares it, closes out the Linear issues and replies in #winddown
### Assigned Persona: Robert - Co-Founder & Creative Director (robert@harmonygames.co)
### Assigned Business Function: Executive
### Assigned Competency: Finance
### Assigned Task Skill: Analysis and synthesis
### Assigned Horizon: long-horizon (Long Horizon, 100–500+ calls; not estimated at /prompt)

## Scope

| Field | Value |
|---|---|
| Review | `/prompt`, chat attachment review, attempt 6aeed82596dcfe103f9f74d9 |
| Review time | 2026-11-08 (UTC) |
| Universe | `Universe_Normal` (Feb 14, 2026 normal); manifest `Evals/references/universes/normal/universe_manifest.json` sha256 `5e01ac4472c8c181d46aaaad5c83e7d319d3e35e5c297396260df295f22de450` |
| Clock | 2026-02-14 00:00 UTC (today = Saturday Feb 14, 2026) |
| Prompt | `Evals/task_inputs/04_Prompt.txt` sha256 `d0cb08476d234f3246dea8cd6595cea03f16ec4c5ea9d57a99fa12074fd25631` (uploaded `04_Prompt.txt`, input-store revision 4) |
| Assignment | `Evals/task_inputs/00_Task_Assigned_Inputs.md` sha256 `02927c30549fd390296830b7630319757e7c33dfb70e40e92a097a75e082a6d5` (platform record) |
| Injection SQL | `Evals/task_inputs/01_Universe_Inject.sql` sha256 `872bbb30771099c1d72d7121c9a9d195f056839043854ef63dd74223eb0279fd` |
| Error/async config, dynamic context, reference files | none supplied; none needed by the prompt |
| Eval | `Evals/1_Prompt_Eval.md` sha256 `9b3f723eecb485ed21e7cfd05cd01f140adca0e43b46f84eddbe10b2ecceb3d7` |

## Input / authority issues

None. All five assignment fields are in the platform record: Persona Robert, Business Function Executive, Competency Finance, Task Skill Analysis and synthesis, Task Type long-horizon. The SQL is saved, and /injection reviewed this exact hash.

## Checklist

- [x] Intake: prompt saved, all five assignment fields read from the platform record (NEW)
- [x] STEP 0.5 Injection gate: CURRENT, /injection PASS reused for the static checks (REUSED, report `0_injection.md`, same SQL hash)
- [x] STEP 0.6 Dataset similarity: run on this prompt (NEW)
- [x] Phase 0.1 Docs: QC rating form V12 (CSV) and the PDFs extracted with `pdftotext` (Prompt Writing, Overall Task Flow, Universe and Tools, Persona ACL, Common Errors, Example Task, Unique Ground Truth). The QC spec XLSX was not extracted (no reader available); its rules are carried by the rating form, `scoring.json` and the Eval's local overrides (NEW)
- [x] Phase 0.2 Universe exploration: Leonard's doc, sheet, deck, Trello card, Slack posts, Linear project (22 issues, 59 comments), all 132 unique SVB Payment Processed notices in Robert's mailbox, the 170 Awaiting Approval/Scheduled notices, Western Union and Payoneer mail, the Node Media invoice thread, #company-internal / #telegram-dd / #art_outsourcing, Snowflake REVENUE_DAILY and IAP_TRANSACTIONS (NEW)
- [x] Phases 1.1–1.5, 2.1–2.9, 3.1–3.2, 4.1–4.2 (NEW)
- [x] Phase 5 deep recheck P1–P4 (NEW)

### Injection Gate
- State: CURRENT
- Reviewed SQL sha256: `872bbb30771099c1d72d7121c9a9d195f056839043854ef63dd74223eb0279fd`. Eval 0 verdict: PASS (`injection-static-v2`, COMPLETE, 2026-11-08T05:02:44Z)
- Eval 0 findings on records this prompt depends on: none. The Eval 0 advisories (the "warehouse's daily revenue table" needs a /prompt check, NB-23 Singular, NB-24) are handled below. The revenue advisory became the Cross-Service Coherence finding (I3).

### Dataset Similarity
- Library: refreshed 2026-11-07T19:36Z (9.5 h old), 482 tasks. Gate: PASS. Nearest tier: distinct.
- Nearest neighbours, all distinct (below 0.70): an Arthur Blake BoomBit/domino-test task (0.676); Robert's "wind-down cash plan and settlement offers" (0.652); Frederick's October cash plan (0.649). None shares this scenario (per-bet build cost and revenue from SVB notices for the angel note).

## Requirement ledger

| Ask | Grounded sources | Discovery path | Exact catalog capability | Persona visibility | Expected output |
|---|---|---|---|---|---|
| Find Leonard's Thursday request in #winddown | SQL slack_messages `fa707da5…`, `f5b759f3…` in C0ADGSZKR3R | Slack channel history / search | `slack_*` read operations | Robert is a #winddown member (`slack/channels.json` /154) | The request, the doc name, the sheet layout, the deck, the Linear project |
| Count per Leonard's doc "Angel note: how to count the money" | SQL gdocs `f_6feda53b…` | Drive search by title | `gdrive_search`, `gdrive_read_file` | Shared writer with robert@ | The counting rules, bucket rules, bet windows, currency rule, revenue source, Linear instructions |
| Line per payee from SVB Payment Processed notices | 132 unique notices in robert@ mailbox (25 payee/account pairs, 22 issues) | Gmail search | `gmail_search_messages`, `gmail_get_message(s_batch)` | Robert's own mailbox | One line per payee with bet columns by Transaction Date |
| Apply the adjustments | Leapblock close-out (SQL `6312d121…`, #leapblock); Blake's "Chase records" (robert@ INBOX); Lucas Western Union receipts (robert@, 5 transfers, 7,525); Oleg's wire came back (ENG-2459); MotMot's Apr 2 2024 ***8605 4,032 wire returned (#admin_foundersonly, Robert a member); Node Media invoice thread (robert@) | Slack, Gmail, Linear | Slack/Gmail/Linear reads | Robert in #leapblock (/51); mail in his mailbox; Linear unscoped | Leapblock 407,944; JPMorgan 0; Lucas +7,525; Oleg 0; MotMot −4,032; Node = Marketing |
| Bucket each payee | Linear comments ENG-2438..2459; #art_outsourcing (Ozhan); #company-internal (Lauren) | Linear, Slack | `linear_get_issue`, `linear_list_issues`, Slack reads | Linear unscoped; Robert in both channels | Build / Marketing / Company per payee (**Lauren Brooks unsettled, see UGT**) |
| What each game brought in | Snowflake `ANALYTICS.MONETIZATION.REVENUE_DAILY` | Warehouse query | `snowflake_execute_query` | Snowflake unscoped | Lifetime total per game (**Combo Fighter conflicts with NB-26, see I3**) |
| Build the sheet in Robert's Drive with Leonard's layout | Sheet "Angel note working" header row | n/a (new output) | `gsheets_create_spreadsheet`, `gsheets_values_update` | Write (not ACL-governed) | New sheet in Robert's Drive |
| Share with Leonard and Blake | Leonard: "share it with Blake and me" | n/a | `gdrive_share_file` | Write | Shares to leonard.hayes@ and arthur.blake@ |
| Work through the Payee history project | Doc: "move each payee's issue to Done once its line is right. If your figure isn't what the notices add up to, say why on the issue first." | Linear project | `linear_create_comment`, `linear_update_issue` (team_ENG has a Done state) | Linear unscoped; writes allowed | Comments on the issues whose figure differs, then all 22 to Done |
| Reply in #winddown | Leonard: "tell me here what each bet cost and brought in and what changes on the deck" | n/a | `slack_send_message` | Robert is a member | Build cost and revenue per bet, deck changes, sheet link |

## Phase 1: Prompt Structure & Persona

**Persona:** PASS (5)
- Robert is a co-founder, and Leonard asks him because "you know what each of these people did better than I do". He is in #winddown, #leapblock, #art_outsourcing and #telegram-dd, he owns the mailbox with the SVB notices and the Western Union receipts, and he is shared on the doc, sheet and deck. The voice is a short co-founder hand-off.

**Assigned Competency (Finance):** PASS (5). Cost per bet from bank records plus lifetime revenue for an investor note is finance work.

**Assigned Task Skill (Analysis and synthesis):** PASS (5). It combines 132 notices, four kinds of correction record, a bucket per payee and warehouse revenue into one table and a summary.

**Business Function (Executive):** PASS (5). It maps to Founders / Exec / Strategy: a founder deliverable for the angel calls.

**Complexity Dimensions:** Ambiguity Y · Dynamic Change Y · Multi-Source Y. PASS.
- Ambiguity: the rules sit in Leonard's doc, not the prompt. Dynamic Change: the Leapblock close-out beats the notices, Blake's email reclassifies the $4,000, Oleg's and MotMot's wires came back, and the doc replaces the Trello "quick plan". Multi-Source: Gmail, Slack, Linear, Drive and Snowflake, with the deck and sheet figures as decoys.
- Data seeding: PASS. The prompt is 6 sentences, and every operating detail is in seeded records.

**Naturalness:** PASS. It is first person and plain, with no document formatting, polished connectives, enumerated specs or staged errors. Long-horizon guidance applied: the work is one distinct check per payee (22) over a source-defined cohort (132 notices), with no padding.

**Anti-Patterns:**

| Pattern | Status |
|---|---|
| Command List | PASS ("When you're done" is one ordering phrase, not a step list) |
| Bolt-On | PASS (every sentence feeds the one deliverable) |
| Pre-Solving | PASS (no adjustment, payee or figure is named) |
| Tool Mention | PASS ("in Linear", "in my Drive" are service names) |

**Prompt diversity:** a sheet, two shares, about 26 Linear writes and a Slack reply, built item by item. This goes well beyond "investigate and post one Slack message".

## Phase 2: Depth Assessment

**Unique Ground Truth:** FAIL (2)

### Unique Ground Truth comparison

Unique Ground Truth: FAIL 2

Basis: One payee's bucket has two supported answers that change Leonard's build-cost figures: Lauren Brooks (ENG-2455) can be Marketing or Build, and no persona-visible record decides it.

Alternative selection: Every one of the 22 payees was swept against Leonard's bucket, currency, date and adjustment rules. 21 are settled by a record. Brooks is the only payee whose role (Telegram distribution lead) the bucket wording does not reach. Readings B and C test her other buckets.

| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |
|---|---|---|---|---|---|---|
| A | Lauren Brooks (payee \[PERSON\_NAME\_7249\] Brooks, 3 x $500 SVB wires) led Telegram distribution for Domino Delights, which is work to get players, so her line is Marketing: listed under ZM ($500, Oct 30 2025) and Combo Fighter ($1,000) but kept out of build cost. | Brooks line bucket = Marketing; ZM and Combo Fighter build cost exclude her $1,500. | Create one spreadsheet in Robert's Drive with Leonard's layout; share it with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co; comment on each Payee history issue whose figure differs from its notices, then move all 22 issues to Done; post one reply to Leonard in \#winddown with the build cost and revenue per bet, the deck changes and the sheet link. | Robert's Drive (new sheet, shared with Leonard and Blake); Linear Payee history issues ENG-2438..ENG-2459; \#winddown. | Sheet: Brooks row Bucket Marketing. ZM build cost and Combo Fighter build cost (sheet and \#winddown reply) leave out $500 and $1,000. | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)"; CI (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05KNDCHAAG/2025-10.json): "She will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights." |
| B | Lauren Brooks is a contractor on the team (contact title Telegram Contractor, a monthly contract, standups), so her line is Build: ZM build cost +$500 and Combo Fighter build cost +$1,000. | Brooks line bucket = Build; ZM and Combo Fighter build cost include her $1,500. | Create one spreadsheet in Robert's Drive with Leonard's layout; share it with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co; comment on each Payee history issue whose figure differs from its notices, then move all 22 issues to Done; post one reply to Leonard in \#winddown with the build cost and revenue per bet, the deck changes and the sheet link. | Robert's Drive (new sheet, shared with Leonard and Blake); Linear Payee history issues ENG-2438..ENG-2459; \#winddown. | Sheet: Brooks row Bucket Build. ZM build cost is $500 higher and Combo Fighter build cost $1,000 higher than under A, in the sheet and the \#winddown reply. | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games."; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "'Lauren', 'Brooks', false, 'Unknown', 'Unknown', 'Telegram Contractor'"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "the contract I sent out in Oct, $500 a month" |
| C | Lauren Brooks's work was not for one of the three games, so her line goes in the Company column. | Brooks line bucket = Company; her $1,500 goes in the Company column. | Create one spreadsheet in Robert's Drive with Leonard's layout; share it with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co; comment on each Payee history issue whose figure differs from its notices, then move all 22 issues to Done; post one reply to Leonard in \#winddown with the build cost and revenue per bet, the deck changes and the sheet link. | Robert's Drive (new sheet, shared with Leonard and Blake); Linear Payee history issues ENG-2438..ENG-2459; \#winddown. | Sheet: Brooks row in the Company column; build totals as under A. | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |

Explicit option inventory: The prompt has no option list. Leonard's doc, which the prompt incorporates, offers three buckets (Build, Marketing, Company), and all three were tested for the one unsettled payee.
Inventory evidence: P (Evals/task\_inputs/04\_Prompt.txt): "He laid out how he wants it counted and how it should look."

| Option | Disposition | Tested readings | Reason and evidence |
|---|---|---|---|
| Build | RETAINED | B | Brooks was a monthly contractor on the team; nothing rules Build out. Evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games." |
| Marketing | RETAINED | A | Her role was Telegram distribution; nothing rules Marketing out. Evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)" |
| Company | EXCLUDED | C | Her work was a Domino Delights experiment, one of the three games. Evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |

Compared alternative: B
Resolution: UNRESOLVED_MATERIAL_DIFFERENCE. Leonard's bucket rules name Deel staff, studios and freelancers who made the games (Build) and ad networks, agencies, ad creative, playables and trailers (Marketing). A contractor who led Telegram distribution fits neither list by name. The Linear comments on her issue speak only to the contract and the payment route, and no record the persona can open puts her (or distribution / platform work) in a bucket. The two readings change the Brooks bucket and two of the three build-cost figures Leonard asked for.
Resolution evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games."; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)"; CI (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05KNDCHAAG/2025-10.json): "She will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights."; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "the contract I sent out in Oct, $500 a month"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "direct wire from me, not through Deel"

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | A puts Brooks in Marketing, B in Build. |
| writes | SAME | Both create, share, comment, move to Done and reply the same way. |
| destinations | SAME | Same sheet, issues and channel. |
| contents | DIFFERENT | ZM build cost differs by $500 and Combo Fighter build cost by $1,000, in the sheet and the reply; the Brooks Bucket cell differs. |

Resolution relevance challenge: The Build sentence covers people who made the games and the Marketing sentence covers things made or bought to get installs; the \#company-internal post says she leads distribution strategy, which a careful reader can place in either. Her Linear comments (contract, direct wire) say nothing about the bucket.
Delegation challenge: NOT_CLAIMED. No record lets the Agent pick either bucket; both values change graded build totals, so this is not a both-fair figure (it changes a classification and two figures).
Challenge evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games."; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)"; CI (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05KNDCHAAG/2025-10.json): "She will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights."

Compared alternative: C
Resolution: EXCLUDED. Leonard's Company bucket is for anything that was not for one of the three games, and the \#company-internal post says her Telegram work started as an experiment on Domino Delights, one of the three games.
Resolution evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn"; CI (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05KNDCHAAG/2025-10.json): "She will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights."

| Material field | Relation | Explanation |
|---|---|---|
| decision | DIFFERENT | C puts Brooks in Company. |
| writes | SAME | Same writes. |
| destinations | SAME | Same destinations. |
| contents | DIFFERENT | Company column instead of a bet column. |

Authority chain: P → SQL

Resolution relevance challenge: The Company sentence excludes work for one of the three games, and the post ties her role to Domino Delights.
Delegation challenge: NOT_CLAIMED. Excluded by the cited rule and post; no delegation claimed.
Challenge evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn"; CI (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05KNDCHAAG/2025-10.json): "She will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights."

Decision sweep: Leonard's doc assigns every payee a bucket, a bet by date and an amount, and the prompt asks for the Payee history issues to be worked through one by one.
Decision rule: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games."; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn"

| Item | Outcome | Basis | Settled by / gap |
|---|---|---|---|
| ENG-2438 Deel (both SVB spellings, account 8380) | Build, split by notice date | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Everything on Deel counts as team"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "SVB shows it under two spellings, same account" |
| ENG-2439 Leapblock LTD, including the 13 Sep 2023 33,290 wire that has only an SVB awaiting approval notice | Build, 407,944 by close-out, the 33,290 in Domino Delights | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Total 407,944 over 30 wires."; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "that beats the notices for them"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "external art studio". Edge check NOT\_AN\_EDGE: Leapblock's own close-out lists the 13 Sep 33,290 wire as one it received, so it is a plain member of the payments to Leapblock, and Leonard's doc says a close-out beats the notices for that payee. SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "the first one 33,290" |
| ENG-2440 Eveline Art S.R.L. (Marcus) | Build | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "he wanted off Deel so direct bank wire"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games." |
| ENG-2441 Adjoe GMBH | Marketing (ad network), under its bet by date, out of build cost | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "incent UA on iOS in the US"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)" |
| ENG-2442 BANCO DE AMERICA (MotMot, accounts 3341 and 8605), including the Apr 2 2024 \*\*\*8605 4,032 wire that came back | Build; the 4,032 \*\*\*8605 wire is out (money came back), so the line is below the notices and needs a why comment | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "one of their engineers on our team"; AFO (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C04UEQVDVB7/2024-04.json): "this is money returned to us because Blake put the wrong account number"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Take a notice as paid unless one of us has said the money came back." |
| ENG-2443 Singular Labs Inc (both spellings, account 4015) | Company column | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "attribution tool, not one game"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |
| ENG-2444 PERSON\_4419\_NAME LLC (Node Media) | Marketing (agency), Domino Delights by date, out of build cost | RECORD | NODE (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00008689.json): "nodemedia.co"; NODE2 (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00008689.json): "creative concepts, which are included in the Nov $5k"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)" |
| ENG-2445 TYZ Law Group | Company column (legal) | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "lawyers, the patent scare"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |
| ENG-2446 \[PERSON\_NAME\_7200\] trademark filings | Company column (legal) | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "the trademark filings"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |
| ENG-2447 \[PERSON\_NAME\_36400\] (Lucas), SVB wires plus five Western Union transfers in Robert's mail | Build, SVB 6,450 plus Western Union 7,525 at amount sent, all Domino Delights | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "mini games dev"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee."; WU (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00005198.json): "Lucas received the money you sent" |
| ENG-2448 AppLovin Corporation | Marketing (UA bills), out of build cost | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "past due UA bills"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)" |
| ENG-2449 Graham Porter | Build (art direction) | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "art direction and a look at our AI art pipeline"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games." |
| ENG-2450 JPMorgan \*\*\*3203 $4,000 own-account transfer | Zero line, no bucket | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "That was our own Chase account"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Money we moved between our own accounts"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Every payee keeps its line, even at zero." |
| ENG-2451 CREATIVE X TEKNOLOJi (PlayableX) | Marketing (playable), out of build cost | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "playable ad for our UA"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers)" |
| ENG-2452 M \[PERSON\_NAME\_0056\] (JP) | Company column (website) | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "the website"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |
| ENG-2453 Nathan Price | Build | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "short animation job, coins and chests"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games." |
| ENG-2454 Martin Walsh 1,999 BGN | Build, ZM, kept in BGN beside the line | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "paid him direct for this one, not through Leapblock"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Anything not paid in dollars stays in its own currency next to the line." |
| ENG-2455 \[PERSON\_NAME\_7249\] Brooks (Lauren Brooks) | Build or Marketing; no record decides | SILENCE | No record; tested as A vs B |
| ENG-2456 PERSON\_6074\_NAME (Ozhan) | Build (in-game 2D zombie animation) | RECORD | ART (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C08FG9924R2/2025-02.json): "we found someone from Turkey to help us with the 2D animation"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games." |
| ENG-2457 \[PERSON\_NAME\_9100\] UX job | Build, Domino Delights | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "second half of the UX job on the dominoes game"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Build is the team on Deel plus the studios and freelancers who made the games." |
| ENG-2458 \[PERSON\_NAME\_0054\] \[PERSON\_NAME\_0131\] 4X proposal | Company column | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "$500 for help on the 4X proposal, not one of the three games"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Company is legal, tools, the website, equipment and anything else that wasn" |
| ENG-2459 Private Entrepreneur (Oleg) 125 USD wire that came back the same day | Zero line; the Payoneer re-send has no receipt in Robert's mail, only a payment request | RECORD | SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "that wire came back the same day"; SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "Take a notice as paid unless one of us has said the money came back."; DIX (Universe\_Normal/Normal\_HarmonyGames\_Gmail/Services\_Data/gmail/threads/00004614.json): "Dixelar is requesting a payment of" |

Strongest-alternative challenge (B): Build is the reading a careful agent reaches from the contact title and the monthly contract; Marketing is the one it reaches from the distribution-strategy post. Neither is a strawman, and the totals differ.
Challenge evidence: SQL (Evals/task\_inputs/01\_Universe\_Inject.sql): "'Lauren', 'Brooks', false, 'Unknown', 'Unknown', 'Telegram Contractor'"; CI (Universe\_Normal/Normal\_HarmonyGames\_Other\_Services/Services\_Data/slack/messages/C05KNDCHAAG/2025-10.json): "She will lead our Telegram distribution strategy, starting with a focused experiment on Domino Delights."

Validation scope: source binding and comparison completeness are checked mechanically; alternative strength, evidence relevance and authorization remain substantive review judgments.

**Feasibility:** PASS (5)

| Ask | Required capability | Tool(s) | Feasible? |
|---|---|---|---|
| Read Slack request, Leapblock close-out, team channels | Channel history/search | `slack_*` reads | Yes (Robert is a member of every channel used) |
| Read doc, sheet, deck | Drive reads | `gdrive_search`, `gdrive_read_file`, `gdrive_read_sheet_range`, `gslides_get_presentation_text` | Yes (shared with Robert) |
| Read SVB notices, Western Union receipts, Chase email, Node invoices | Gmail search/read | `gmail_search_messages`, `gmail_get_message`, `gmail_get_messages_batch` | Yes (Robert's mailbox) |
| Read and update Payee history issues | Linear read, comment, state change | `linear_list_issues`, `linear_get_issue`, `linear_create_comment`, `linear_update_issue` | Yes (Done exists on team_ENG: 1,944 base issues) |
| Lifetime revenue per game | Warehouse query | `snowflake_execute_query` | Yes (REVENUE_DAILY has game_id and total_revenue_usd at 2 decimals) |
| Create and share the sheet | Sheet create/write, Drive share | `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdrive_share_file` | Yes |
| Reply in #winddown | Post | `slack_send_message` | Yes |

- Dimensional feasibility: per-bet split by the notice `Transaction Date` (in every notice body), per-payee by `To:` name and account, per-game revenue by `game_id`. All present.
- Numeric observability: notice amounts are written to the cent in the email bodies; REVENUE_DAILY is NUMBER(38,2). The return format of the catalog tools is not documented (catalog limit, recorded as an evidence limit, not a defect).
- Persona-scoped reads (Lens 1 and Lens 2): every scoped record the answer needs is in Robert's mailbox, in a channel he is a member of, or in a Drive file shared with him. Leonard's own Payoneer receipts ("Thanks for your payment to Dixelar", leonard.hayes@ only) are not needed: the doc counts only receipts in "your mail". No ask directs Robert to someone else's scoped data.

**Truthfulness:** PASS (5). All 6 premises were checked in the bound record:
- "On Thursday": Leonard's post is 2026-02-13T01:23:41Z, which is Thu Feb 12, 17:23 PT. Robert's calendar invite for the angel calls is in PST.
- "#winddown": C0ADGSZKR3R.
- "one straight page": Leonard's words.
- "angel calls on Tuesday": the event is Tue Feb 17, 9:00 PT.
- "laid out how he wants it counted and how it should look": the doc, plus "use the layout of my Angel note working sheet".
- "Blake": Arthur Blake, the only Blake.
- "Payee history project": exists.
- "the draft deck": "Note to angels (draft)".

None contradicted; no shutdown or departed-person premise.

**Tool Use & Cross-service:** PASS (5). Each service changes a graded fact:
- Gmail: the notice lines (MotMot's returned wire is in #admin_foundersonly, Slack), Lucas +7,525 from Western Union receipts, JPMorgan to 0 from Blake's email, the Node bucket.
- Slack: Leapblock +33,290 from the close-out, and the request itself.
- Linear: buckets per payee, Oleg to 0, the Done/comment writes.
- Snowflake: revenue.
- Drive: the rules, the layout, the deck figures that change.

**Investigation + Action:** PASS (5). The writes are a sheet, shares, Linear comments and state changes, and a Slack reply. All of them depend on the investigation.

**Clarity & Specificity:** FAIL (1). This is Action Decision Ambiguity on the Lauren Brooks bucket (same fork as UGT): the sheet's Bucket cell and the ZM and Combo Fighter build totals in the sheet and the reply differ by reading. The rest is clear. A thread reply and a top-level #winddown reply reach the same recipient in the same channel. Share role (writer or reader) is a non-action detail; Leonard shared his own files as writer.

**Contrived / Unnatural:** PASS (5). Nothing in it is spec-sheet register, a trap hint, a hidden destination, an opaque ID, an exact timestamp or an if-chain. The destinations are all named.

**Alignment with Today's Date:** PASS (5). "Thursday" (Feb 12 PT) and "Tuesday" (Feb 17) resolve against the clock and the records. Every record the task relies on predates 2026-02-14 00:00 UTC; the Leapblock post (Feb 13 08:37 UTC) is before the Slack export's 10:03 UTC end (NB-6).

**Originality / Sample Similarity:** N/A: no comparison samples supplied (library similarity is reported above).

**Coherence (Bolt-on):** PASS (5).

## Phase 3: Universe Feasibility

**Data Existence:** 22/22 payees, 132/132 notices, the doc/sheet/deck, every correction record and the revenue table all exist and can be reached with cataloged tools. PASS (5).

**Cross-Service Coherence:** FAIL (1)
- Inconsistency in task-touched data (Cross-service Referential, base Snowflake, counts under base-data-v1 because the prompt asks what each bet brought in): Combo Fighter's lifetime revenue. `ANALYTICS.MONETIZATION.REVENUE_DAILY` gives Combo Fighter $11.75, all ad revenue, with `iap_revenue_usd` 0 and `paying_users` 0 on every row through 2026-02-09. `IAP_TRANSACTIONS` has no Combo Fighter purchase ("absence here means no sales"). But Robert's own DM (D07H86MV4DN, ts 1770782454) says "I mean I was sort of shocked that 2 people bought rotation pack..". Leonard also wrote in C07C2866011 on Feb 6 "I can see my purchase" after the v1.0.91 IAP build. This is known issue NB-26 (avoid). Leonard's "as recorded" line does not remove the dependency. Evidence limit: the warehouse ends on Feb 9, so purchases made on Feb 10 alone would not contradict it. The records give no purchase dates.
- Known base-data issues (not scored): NB-23 Singular invoice totals and NB-24 base Linear comments. The task builds Singular only on its two SVB wires and grades only injected comments; keep the rubric and OEs off both.
- Injection SQL considered: Yes.
- Static integrity evidence: REUSED from `0_injection.md` (checks A–C PASS on this SQL hash): IDs, collisions, author membership, doubled apostrophes, chronology, notice reconciliation.
- Prompt-specific sources, access and configuration: supported. Every needed record is visible to Robert. No error/async configuration.

| Prompt ask / source | Static evidence NEW or REUSED | Prompt-specific discovery/access/configuration evidence | Task coherence |
|---|---|---|---|
| #winddown request, doc, sheet, deck, Trello card | REUSED 0_injection A–C | Robert member/shared writer | PASS |
| Leapblock close-out vs notices (407,944 vs 374,654) | REUSED C3 | Robert in #leapblock; 33,290 Awaiting-Approval-only wire is the only unmatched SVB notice (170 parsed) | PASS |
| Chase records / JPMorgan $4,000 | REUSED C3 | robert@ INBOX copy | PASS |
| Linear Payee history (22 issues, 59 comments) | REUSED A–C | Linear unscoped | PASS |
| Lucas Western Union receipts | NEW | 5 receipts in robert@ (1,075 ×3, 2,150 ×2) | PASS |
| Combo Fighter revenue (REVENUE_DAILY) | NEW | Snowflake unscoped; conflicts with Robert's DM | **FAIL (NB-26)** |

## Phase 4: Final Evaluation

**Scoring Table:**

| Dimension | Sub-Dimension | Score (1-5) | Justification |
|---|---|---|---|
| Prompt | Unique Ground Truth | 2 | Lauren Brooks's bucket (Build vs Marketing) is unsettled and changes ZM and Combo Fighter build cost |
| Prompt | Feasibility | 5 | Every ask has a cataloged path and data |
| Prompt | Persona ACL Reachability | 5 | Every scoped read is Robert's own mail, his channels or files shared with him |
| Prompt | Explicit Tool Mention | 5 | None |
| Prompt | Clarity & Specificity | 1 | Action Decision Ambiguity on the same Brooks fork |
| Prompt | Contrived / Unnatural | 5 | Natural co-founder request |
| Prompt | Alignment with Today's Date | 5 | Thursday and Tuesday resolve |
| Prompt | Originality / Sample Similarity | N/A | No samples supplied |
| Prompt | Truthfulness | 5 | 6/6 premises verified |
| Prompt | Tool Use & Cross-service | 5 | Gmail, Slack, Linear, Snowflake, Drive each change a graded fact |
| Prompt | Investigation + Action | 5 | Sheet, shares, Linear, Slack |
| Prompt | Coherence (Bolt-on) | 5 | No bolt-on |
| Prompt | Persona | 5 | Fits Robert |
| Prompt | Business Function | 5 | Founders / Exec / Strategy |
| Prompt | Assigned Competency | 5 | Finance |
| Prompt | Assigned Task Skill | 5 | Analysis and synthesis |
| Prompt | Complexity Dimensions & Data Seeding | 5 | All three dimensions; short trigger prompt |
| Universe | Data Exists | 5 | All records exist and can be reached |
| Universe | Cross-Service Coherence | 1 | NB-26: Combo Fighter revenue vs Robert's "2 people bought rotation pack" |

### Issues Found:

| # | Issue | Severity | Dimension |
|---|---|---|---|
| I1 | ENG-2455 [PERSON_NAME_7249] Brooks (Lauren Brooks, 3 × $500, Oct 30 2025 → ZM, later two → Combo Fighter). Leonard's buckets are Build (Deel staff, studios and freelancers who made the games) and Marketing (anything made or bought to get installs). Lauren "will lead our Telegram distribution strategy" (#company-internal, Oct 10 2025); her contact says "Telegram Contractor", and her Linear comments only cover the contract and the wire. No record puts her in a bucket, and the choice moves ZM build cost by $500 and Combo Fighter build cost by $1,000 | Major | UGT |
| I2 | The same fork changes what the Agent writes in the sheet and the reply | Major | Clarity |
| I3 | Combo Fighter "brought in" depends on base Snowflake data that Robert's own DM contradicts (NB-26) | Major | Cross-Service Coherence |

### Recommended Improvements:

1. I1: settle Lauren Brooks's bucket in the data. Add one dated record Robert can see, before Feb 13 01:23 UTC, that says which bucket her Telegram distribution work goes in. Leonard's own comment on ENG-2455 or a line in his doc naming distribution or platform work would do it. Then re-run /prompt. Saying "accept either" in the OE or rubric does not fix it (ugt-fork-v1).
2. I3: take Combo Fighter's revenue out of what is graded, or base "brought in" on something that does not conflict. Snowflake can't be changed by injection, and an "as recorded" line doesn't remove the conflict. Options:
   - narrow Leonard's revenue ask to Domino Delights and ZM;
   - have him say the Combo Fighter number stays off the page until the store report lands.
   Then keep the rubric and OEs off the Combo Fighter revenue figure.
3. Everything else held up. The Leapblock close-out, the JPMorgan transfer, the Western Union receipts, Oleg's wire, MotMot's returned $4,032 wire and Node Media each have a deciding record, and these are good traps. Keep them.


## Deep Recheck

Passes: P1, P2, P3, P4, Opus 5.5 (claude-opus-5-5), session effort, each blind to the main review.

| Pass | Checked | Findings | Confirmed |
|---|---|---|---|
| P1 | 6 sentences, 22 payees, date windows, revenue source, edge values | 1 (plus 21 fork lines) | 1 |
| P2 | 6 sentences, about 40 record groups | 7 | 4 (3 not scored, 1 platform) |
| P3 | 6 sentences, 17 claims, 126 SQL statements | 0 | 0 |
| P4 | 6 sentences | 0 | 0 |

| DR# | Pass | Quote | Record | Section | Dimension / issue | Status | Reason |
|---|---|---|---|---|---|---|---|
| DR1 | P1 | "Work through the Payee history project in Linear the way he wants." | ENG-2455 "the contract I sent out in Oct, $500 a month"; contact "Telegram Contractor"; #company-internal "She will lead our Telegram distribution strategy"; doc Build/Marketing sentences | §2 bucket | Unique Ground Truth | CONFIRMED | Same fork as the main review (I1). No prompt sentence or Robert-visible record puts her in a bucket; Combo Fighter build is 72,685.61 or 73,685.61 and ZM 544,433.44 or 544,933.44 |
| DR2 | P2 | "He laid out how he wants it counted and how it should look." | Payoneer "Thanks for your payment to Dixelar" receipts only in leonard.hayes@ (`leonard@harmonygames.co_1798426229536387534.json`, `…1812016089445671988.json`) | §3 hidden record | Persona access | REJECTED | The doc counts an other-route payment only if "a receipt for it reached your mail". Robert's mail has only the payment requests (`00004614.json`, `00007150.json`), so the expected answer leaves them out and no graded record is hidden. P1 F5 reaches the same result |
| DR3 | P2 | "…what each bet cost to build and brought in…" | REVENUE_DAILY combo_fighter iap 0, total 11.75; Robert's DM "2 people bought rotation pack" (NB-26) | base-data-v1 | Cross-Service Coherence | CONFIRMED | P2 rated it not scored. The main review scores it because the reply must report Combo Fighter's revenue, which is one side of the conflict (I3). A doc line saying "as recorded" does not remove the dependency |
| DR4 | P2 | "…what each bet cost to build and brought in…" | DAILY_METRICS_AGG has no zombie_match_3d rows; REVENUE_DAILY has ZM 11.99 | base-data-v1 | Cross-Service Coherence | CONFIRMED | Not scored. The doc names "the warehouse's daily revenue table", which is REVENUE_DAILY; the mart is "derived from the DAU and revenue tables" (P1 F18 settled). Keep the rubric off the mart |
| DR5 | P2 | "Work through the Payee history project in Linear the way he wants." | FINANCE_LEDGER adjoe vs SVB wires | base-data-v1 | Cross-Service Coherence | CONFIRMED | Not scored: the doc says "Go by the bank", and the ledger is not read |
| DR6 | P2 | "Work through the Payee history project in Linear the way he wants." | NB-23 Singular invoice INVSINC22671 | base-data-v1 | Cross-Service Coherence | CONFIRMED | Not scored: only the two SVB wires are used |
| DR7 | P2 | "Work through the Payee history project in Linear the way he wants." | Notice payee tokens match the issue titles and account endings | PLATFORM | anonymized-token | CONFIRMED | Platform note, not scored |

Main-session correction from P1 F2: MotMot's Apr 2, 2024 ***8605 $4,032 wire came back. #admin_foundersonly (Robert is a member): "this is money returned to us because Blake put the wrong account number". The doc's "came back" rule settles it, so it is a settled trap, not a defect. The sweep item in the record was corrected.

Effect on verdict: unchanged. UGT 2, Clarity 1 and Cross-Service Coherence 1 stand; all other dimensions 5.

- F1: ENG-2455 Lauren Brooks bucket | A: Marketing (Telegram distribution = getting installs), $1,500 out of build cost | B: Build (monthly contractor on the team), ZM +$500 and Combo Fighter +$1,000 | Missing: a dated record Robert can see (Leonard's comment on ENG-2455 or a doc line) that says which bucket distribution or platform contractors go in
- F2: ENG-2442 MotMot ***8605 $4,032 | A: out, with a why comment | B: in as a notice | Settled by: #admin_foundersonly "this is money returned to us because Blake put the wrong account number" + doc "Take a notice as paid unless one of us has said the money came back."
- F3: ENG-2439 Leapblock 13 Sep 2023 $33,290 (Awaiting Approval only) | A: in, total 407,944 | B: notices only, 374,654 | Settled by: #leapblock "Total 407,944 over 30 wires." + doc "that beats the notices for them"
- F4: ENG-2450 JPMorgan $4,000 | A: zero line, no bucket | B: counted | Settled by: "That was our own Chase account" + "Money we moved between our own accounts"
- F5: ENG-2459 Oleg $125 + Payoneer re-send | A: zero | B: Payoneer amount counted | Settled by: "that wire came back the same day" + doc receipt-in-your-mail rule; Robert's mail has only payment requests
- F6: ENG-2447 Lucas Western Union transfers | A: +7,525 at amount sent | B: notices only | Settled by: doc "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee." + five receipts "Lucas received the money you sent"
- F7: ENG-2444 PERSON_4419_NAME LLC | A: Marketing, Domino Delights | B: Build/Company or spread over 2024 | Settled by: Node Media invoice thread (nodemedia.co, ad spend, creative concepts) + doc "the whole payment to one bet"
- F8: ENG-2443 Singular | A: Company | B: Marketing | Settled by: "attribution tool, not one game" + "Company is legal, tools, …"
- F9: ENG-2449 Graham Porter | A: Build | B: Company | Settled by: "art direction and a look at our AI art pipeline"
- F10: ENG-2454 Martin Walsh 1,999 BGN | A: kept in BGN | B: converted | Settled by: "Anything not paid in dollars stays in its own currency next to the line."
- F11: ENG-2438 Deel | A: all Build | B: split | Settled by: "Everything on Deel counts as team"
- F12: ENG-2440 Eveline bank-fee add-on | A: notice amounts | B: fee stripped | Settled by: doc "What counts is money that left the company and stayed out"; the not-the-fee rule covers only other-route payments
- F13: Adjoe, AppLovin, CREATIVE X | A: Marketing | B: Build | Settled by: the doc's Marketing list + each issue's comment
- F14: TYZ, trademark filings, JP website, 4X proposal | A: Company | B: Build | Settled by: the doc's Company sentence + each issue's comment
- F15: Nathan Price, UX job, Ozhan | A: Build, bet by date | B: bet by game worked on | Settled by: "Don't try to work out who was on what"
- F16: bet-window and run edges | A/B inclusive or exclusive | Settled by: no notice falls on an edge day
- F17: card spend not on a notice | A: out | B: in | Settled by: "Go by the bank" and the other-route receipt rule (contractors only)
- F18: revenue table | A: REVENUE_DAILY | B: DAILY_METRICS_AGG | Settled by: "the warehouse's daily revenue table, as recorded"
- F19: revenue scope | A: lifetime total | B: IAP only or windowed | Settled by: "lifetime revenue … as recorded" + table comment "Includes both IAP and ad revenue"
- F20: Trello quick plan | A: the doc | B: quick plan | Settled by: "It replaces the quick plan I left on our board."
- F21: share role and reply form | not a fork in the decision, writes or contents; both forms meet "share it with him and Blake" and "reply to him in #winddown"

Platform defects: PLATFORM:anonymized-token (DR7), not scored.

### FINAL VERDICT: FAIL

Score: 2

Execution status: COMPLETE

Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)

Evaluator model: Opus 5.5 (claude-opus-5-5), session effort

Next action: Settle Lauren Brooks's bucket (ENG-2455) in the injection data, and take Combo Fighter's revenue out of the graded answer or narrow the revenue ask (NB-26). Then send /injection, /prompt and /hardness again.

Evidence limits: The catalog lists no return formats, so how tools render the notice amounts and revenue values is not shown (raw values were verified). The QC spec XLSX could not be read (no reader); the rating form and PDFs were read. No purchase dates for the Combo Fighter rotation-pack sales, so a sale made on Feb 10 alone would not contradict the warehouse (which ends Feb 9).

Reviewed prompt SHA-256: d0cb08476d234f3246dea8cd6595cea03f16ec4c5ea9d57a99fa12074fd25631

Review context SHA-256: fb12d380941d1f0acf5adf92e46815b3536e3ee22e686aee0362cda0e25bf4c1

Prompt record SHA-256: 8d101da3dcfc266d7681f860b464af472281105b6881987a42077a2c747c088a

Eval version: task-quality-v1

Eval release SHA-256: adefd7cbd5ec880e02058bd4a90c9e5719d2a9a8a3635ba97d4a865fccb1bce8

**Lowest Dimension:** Clarity & Specificity and Cross-Service Coherence (1); Unique Ground Truth (2). The Lauren Brooks bucket fork and the Combo Fighter revenue conflict.

**Summary:** A natural, well-seeded long-horizon prompt. Its traps (Leapblock close-out, the JPMorgan own-account transfer, the Western Union receipts, the two wires that came back, Node Media) are each settled by a record Robert can see. It fails because one payee, Lauren Brooks, has no record deciding Build vs Marketing, which changes two of the three build-cost figures, and because Combo Fighter's "brought in" rests on warehouse data that Robert's own DM contradicts (NB-26).
