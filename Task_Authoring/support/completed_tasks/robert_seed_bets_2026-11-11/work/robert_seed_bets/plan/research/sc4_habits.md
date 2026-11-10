# SC4: measured Opus 5.5 habits on four HarmonyGames tasks

Status: complete. Every number comes from the 24 baseline exports unless labelled GUESS. Thinking blocks are empty in the exports, so reasons are inferred from calls and short status text.

## 0. Data and method

- 24 runs, all `claude-opus-5-5[1m]`: LLC = robert_llc_takeover, WD = robert_winddown_closeout, CS = frederick_card_spend_q3, BR = frederick_bridge_pipeline.
- Calls extracted with my own parser (`sc4/extract.py`, `sc4/common.py`); the counted-call logic mirrors `difficulty_stats.count_tool_calls`. It reproduces the READMEs: LLC 156/157/162/149/152/159, WD avg 129.8, BR 140/150/126/141/109/123.
- Tool results were read only by targeted extraction.

## 1. Counted calls by tool

| Task | Counted per run | Reads | Writes | Linear R / W | Biggest other |
|---|---|---|---|---|---|
| LLC | 156,157,162,149,152,159 | 69-80 | 79-83 | 40-42 / 74-76 (114-117 of ~155 are Linear, 74 %) | slack 13-20, gmail 5-9, gsheets 3-8, gdrive 3-7, snowflake 3-6 |
| WD | 137,143,116,122,139,122 | 73-98 | 42-46 | 26-31 / 37-40 (64-71, 53 %) | gmail 20-38, slack 9-17, gdrive 8-13, trello 3-5 |
| CS | 558,560,560,554,555,573 | 539-560 | 10-15 | 2 / 1 | gdrive 510-532 (92 %; `gdrive_read_file` ~330, `gdrive_read_sheet_range` ~170), gmail 12-18, gsheets 6-16, trello 5-9, slack 2-6, snowflake 2-3 |
| BR | 140,150,126,141,109,123 | 54-95 | 53-55 | 2-3 / 0 | trello 51-55 (all writes), gmail 19-47, slack 13-33, gcal 1-14, gdrive 7-12 |

- Per-record Linear work: LLC = `linear_list_comments` + `linear_create_comment` + `linear_update_issue` on each of 37 issues, 111 of ~155 counted calls in every run. WD = list + comment on 28 issues and `update_issue` on ~10 (about 66 of ~130). That is the only per-record loop those tasks had; all other services together were 45-80 calls.
- Read volume outside the per-record loop: LLC 30-38 reads, WD 45-65, BR 50-90. So 40-90 non-loop reads is the normal budget of an Opus 5.5 run.
- CS counted 550+ only because each card-feed file was a separate read (see section 7). That was mechanical, partly done by subagents.

## 2. Gmail habits

Tool behaviour that matters:
- `gmail_search_messages` hits are `{id, threadId}` only: no subject, snippet or date. A run must batch-fetch to see anything. Default page 100; `max_results` up to 500 accepted; results over the size limit spill to a file.
- `gmail_get_messages_batch`: default format returns headers + ~100-char snippet (~940 chars per message). `minimal` ~400 chars. `full` is hard-capped at 10 ids ("format='full' is limited to 10 ids per batch"), and 10 full messages can be 190k chars, which spills to a file. Spilled results were always handled by Bash + python/jq.

| Task | Searches per run | Batches | Max batch ids | Format mix | Pagination used |
|---|---|---|---|---|---|
| LLC | 2-4 | 0-2 | 12 | default, some full | never |
| WD | 11-25 (mean 15.8) | 4-7 | 42 | minimal/metadata dominant | never |
| CS | 3-9 (mean 6) | 2-5 | 12 | full for the few | never |
| BR | 5-13 (mean 7) | 1-20 | 55 | default; BR6 full in 10s | never |

- **No run in 24 used a page token.** Over-cap results (est > returned) occurred in 47 search calls; every time the run narrowed the query or moved on. Example: WD `SVB` returned 100 of 504 ids. WD1 opened 0 of the 100, WD3 5, WD6 7 (`Sunset OR SVB`). `SVB card` (44 hits, WD2, WD4, WD6) was opened 0 times.
- Runs batch-fetched a subset selected by recency, never a whole historic result set. Largest fetched: BR5 55 ids (metadata), BR4 50 ids (spilled, parsed by python), WD1 42, WD2 38.
- **One run read a whole set in full:** BR6 decoded 112 unique ids (20 batch calls, 10 ids each, after 9 failed at 12 ids) through its own `dec.py`, then read a cleaned text dump. BR2/BR3 did similar work per-thread (33 and 28 `gmail_get_thread`). All of it was one month of mail (Sep 2025), not a multi-year set.
- **Query shape.** Opening query is always the ask's author + date window (`from:leonard after:...`, `from:leonard.hayes@... newer_than:30d`). Then OR-chains of entity names, usually with a date bound. 94 of 192 searches carried a date bound in LLC/CS/BR (71 of 97) vs WD (23 of 95).
- **Vendor name:** yes, always, as OR-chains (`ElevenLabs OR Pond5 OR Layer OR Lucidchart ...`) then per-vendor retries when `from:vendor` came back empty.
- **Generic word:** yes on spend tasks. WD 24 of 95, CS 9 of 36: `receipt|invoice|subscription|cancel*|renewal`, typically with `after:`. Rarely in LLC (2 of 19), never in BR.
- **Amount:** no. Across 192 Gmail searches, zero carried a dollar amount (the one regex hit is the phrase "2025 categories"). This is the strongest single habit for the planned channels.
- **"refund" as a search word:** 3 of 192, all in CS, and only inside a cancellation OR-chain. No "return", "bounce", "failed", "reversed".
- Sweep habit: a pure date-window sweep of the mailbox (`after:2026/02/08`, `newer:2026/02/09 -from:leonard...`) ran in 6 of 12 Robert runs (LLC2, LLC3, LLC6, WD1, WD2, WD6), window 4-9 days, then a metadata skim of subjects and 3-42 opened. BR ran the same on one month, because the ask pointed there. Never longer.
- **Hit is not read.** Share of Gmail search hits ever opened: 1-10 hits 10-71 %, 11-50 hits 12-66 %, 51+ hits 12-36 % (by task, full table in section 8). Search hits are bare ids, so an unopened hit carries no information. `gmail_list_threads` returns a 100-char snippet instead; it was used in 5 of 24 runs and CS6's use was what caught three traps (section 8).

Query lists: full per-run listing with hit counts in `sc4/i2.out`.

## 3. Slack habits

**Channels read in bulk** (`slack_read_channel` or `conversations_history`, runs out of 6; "x" = pages):

| Task | Channel | Runs | Pages | Oldest message reached |
|---|---|---|---|---|
| LLC | Leonard DM (spilled, then parsed) | 6 | 1 | clock-week |
| LLC | `#winddown` | 6 | 1-3 | Feb 9-12 (4 days back) |
| LLC | `#executives` | 6 | 1, always with `oldest` between Feb 2 and Feb 8 | Feb 11 |
| LLC | Arthur DM | 2 | 1 | Jul 2025 in one run (limit 40) |
| LLC | `#prototype`-class C09UHHN6PFZ | 1 | 1 | Feb 11 |
| WD | `#winddown` | 6 | 1-3 | Feb 9 |
| WD | `#executives` | 1 | 1 | Feb 11 |
| WD | C09UHHN6PFZ | 1 | 1 | Feb 11 |
| CS | Leonard-Frederick DM D05S58U4SAK | 6 | 1 | Sep 24-28 (2-6 days back) |
| BR | `#bridge-pitch` | 6 | 1-6 | Aug 4 to Sep 3 (one month: the window Leonard set) |
| BR | `#executives` | 6 | 1-6 | Sep 14-28 |
| BR | Leonard DM | 3 | 1 | Sep 17 |

- **`read_channel` never goes further back than the task's own window.** Across 24 runs the deepest channel read was 1 month (BR, because the ask named Sep 3) or, on Robert tasks, 4 days. The single older read: LLC3, Arthur's DM, 41 messages back to Jul 2025.
- Page size is 100 messages. `#winddown` and `#executives` burn a page in about 1-3 days at the clock because of wind-down traffic. Runs pass `oldest` almost every time on `#executives`.
- First read without `response_format: concise` spills on every run (WD, LLC): they then re-issue with `concise`.

**Founder channels.**
- `#admin_foundersonly` C04UEQVDVB7 and `#founders` C04UTBZL6AX: **0 of 24 runs called read_channel, read_thread or history on either.** They are `is_private: true` and do not appear in the `search_channels` keyword results runs used (`winddown`, `executives`, `bridge`). The empty-query list (LLC3, LLC5, LLC6, BR1, BR4, BR6) is alphabetical/paged and was not followed into them.
- They were only seen as search hits. 10 of the 12 Robert runs got at least one hit from them (LLC all 6 via `lifestyle` / `"Calm Play"`; WD1 `SVB card`, `receipt`; WD2 `ipostal`, `quickbooks`; WD5 `coderabbit`; WD6 `ipostal`). No run followed a founder-channel hit into the channel or the surrounding messages. No run's text mentions either channel. Slack search does not filter them out.
- Windowed context reads (`oldest` + `latest` around one point) exist but are rare: 5 of 24 runs (BR2, BR3, BR4, LLC2, LLC6), each on a public channel, each within the task's own week or month.

**Search.**
- Searches per run: LLC 2-6, WD 0-7, CS 1-4, BR 7-25.
- Undated name searches reach the whole history. Oldest message any run looked at: Apr 14 2023 (CS `fiverr`), Apr 18 2023 (WD `ipostal`), Apr 21 2023 (BR `docusign`), Apr 25 2023 (LLC `lifestyle`). So age alone does not hide a record from a **name** search; it hides it from a **channel** read.
- About 37 % of searches are undated (54 of 147). Undated ones are payee/firm/product names: `elevenlabs`, `pond5`, `ipostal`, `lucidchart`, `coderabbit`, `quickbooks`, `fiverr`, `Homa`, `Griffin`, `Harlem`. Generic words are nearly always date-bounded: `cancel* after:2026-02-08`, `counts`, `SAFE`, `pass`.
- **Keywords:** across 147 Slack searches in 24 runs, `refund` 0, `returned` 0, `credit` 0, `paid` 0, `wire` 0, `bank` 0, `invoice` 0, any dollar amount 0, `receipt` 1 (WD1). Nearest: `card` twice (LLC3, CS4), `SVB card` once, `cancel*` 5 times, `cut` and `subscriptions` once each. The money-word habit is Gmail, not Slack.
- **Literal mirroring.** Search words come from the ask and hub text: BR `signed`, `counts`, `SAFE`, `docusign`; CS `conference passes`, `Unity seats`, `opex categories`; WD `cancel*`. Generic words the hub never used are rare.
- Tool facts: results come newest first, default 20, `total_count` shown. **0 of 147 searches used a cursor.** `OR` is not supported: `Kevin OR Mike OR Demetri OR angel` returned 0 where `angel` alone returned 8 (BR2; same in WD5).
- **Thread replies are invisible to `read_channel`.** BR1, BR4 and BR5 read the `#executives` page covering Sep 30 and did not get Robert's Sciplay reply; only search or `read_thread` returned it. The same mechanism hid LLC's VO and layer.ai replies and CS's Sensor Tower reply.
- Payee names: yes, always, for the vendors listed on the hub. BR ran one search per firm in three runs (BR4, BR5, BR6); WD ran per-vendor searches in 5 of 6 runs.

Full list: `sc4/i3.out`.

## 4. Cross-checks and self-noticed anomalies

**Second-source total checks.**

| Task | Check | Runs | Asked for? |
|---|---|---|---|
| CS | Feed sums per cycle vs `FINANCE_LEDGER` lines, to the cent | 6 of 6 | Yes: "tie each month to the ledger" |
| LLC | Revenue vs hosting (the take test) | 6 of 6 | Yes: the rules doc |
| LLC | Looked at `MONTHLY_BURN` / `FINANCE_LEDGER` beyond the named table | 1 of 6 (LLC6), LLC4 errored and stopped | No, and no number came of it |
| WD | Register vs bank mail | 0 of 6 | No. WD3 saw "Payment Processed" subjects and moved on |
| BR | Group counts vs any second list | 0 of 6 | No |

- A total was reconciled against a second source only when told to: 12 of 12 asked, 0 of 18 unasked. Runs do verify their own arithmetic (CS4: "Feed parsed: 653 rows, no sheet/date mismatches"; CS1 re-sent a reply to correct two $1 subtotals).

**Anomalies in the card-spend data (CS).** The feed held 653 rows, 12 foreign-currency rows (11 EUR, 1 AUD), 12 FX fee rows, 7 refunds, two cards.

| Anomaly | Noticed | Self-noticed or rule-led? |
|---|---|---|
| Midjourney 60.00 Aug 2, -60.00 on an adjustments tab Aug 25, 60.00 Sep 2 | 6 of 6 | Rule-led (charges after a confirmed cancellation, refunds on adjustments tabs) |
| EUR / AUD rows with an FX fee row below | 6 of 6 correct (AppMagic 1,293.46, Envato 27.04) | Rule-led: the feed doc explains the fee row; `amount_usd` was already in USD, so no conversion trap was tested |
| Card 2208 closing Jul 31, charges moved to 0417 | 6 of 6 | Rule-led |
| No June ledger line; June + July in one line | 6 of 6 | Rule-led (close note 4) |
| Sep 29 rows belong to the October cycle | 6 of 6 | Rule-led |
| Murf, Buttondown, SavvyCal (Zapier) billed but absent from the Trello list | CS1, CS4 reported it | **Self-noticed.** Neither run then searched mail for those vendors; both missed the notices |
| 1Password 3 seats vs Arthur's 4 | CS2, CS3, CS6 raised it as a judgment call | Self-noticed, settled by the later note |
| Dispute cutoff, Sep 28 vs Sep 29 feed end | CS3 | Self-noticed |

- **Near-identical amounts: no test exists.** The CS feed has no same-amount pair of $50 or more within 3 days (checked over all 350 purchase and refund rows), and no run in any task remarked on a same-amount payment. "duplicate" in run text refers only to investor rows or the Intuit/QuickBooks issue. So there is no measured rate for noticing a near-duplicate payment.
- Pattern: rule-led anomalies are caught 6 of 6. Self-noticed ones are found by 2-3 of 6 and **reported, not chased**: 0 of 2 chased the off-list vendors. CS2's OR-chain included `savvycal`, `buttondown`, `webflow` and returned their thread ids, but as bare ids among 100, and it never opened them.
- Bulk data is read by script, not by eye: every CS run built a distinct-descriptor or per-vendor table in Python/pandas. What a run sees is what its parser keeps.

## 5. Warehouse habits

| Task | Was the warehouse named? | Runs that queried | Tools | Queries |
|---|---|---|---|---|
| LLC | Yes: the ground-rules doc names `ANALYTICS.MONETIZATION.REVENUE_DAILY` | 6 of 6 | `list_tables` 1, `describe_table` 1-2, `execute_query` 2-4 | One aggregate: revenue by game for January. First query guessed a column and errored in 6 of 6, then `describe_table`, then the right query |
| CS | Yes: close note rule 2 names `FINANCE.EXPENSES.FINANCE_LEDGER` | 6 of 6 | `list_tables` 0-1, `describe_table` 0-1, `execute_query` 1-2 | One `COUNTERPARTY ILIKE '%unreconciled%'` filter; 3 runs errored on a guessed column first |
| WD | No | 0 of 6 queried (WD2 listed databases and tables, ran nothing) | - | - |
| BR | No | 0 of 6 | - | Confluence: one search in one run, 0 hits |

- When a hub document names a table, every run queries it, once, for exactly the number asked. When nothing names it, no run opens it.
- Unprompted use: LLC6 went beyond the named table to `FINANCE.EXPENSES.MONTHLY_BURN` and `FINANCE_LEDGER` for Dec 2025 on; LLC4 tried MONTHLY_BURN and errored and dropped it. 2 of 12 named-table runs looked sideways.
- Volume: 2-6 calls per run.

## 6. Sheets habits

- **P&L / costs tab.** WD: 6 of 6 read Jan 2026 P&L `f_605121f4a36752645e0ac3`, tab `HG Costs` (`gsheets_values_get` or `gdrive_read_sheet_range` sheetIndex 2), because Leonard's ask named it. Each listed the tabs, then read that one tab: exactly 2 calls per run on that workbook. `HG P&L` and the Salary tab were never opened. LLC: 0 of 6 read the P&L (their costs came from issue comments and mail). BR: 0 of 6. CS: 6 of 6 read the close workbook `QuickBooks close 2025` tabs `Monthly close`, `Bank rules`, `Card close notes`, all named in the ask chain.
- Runs list the tabs first (`gdrive_list_sheets` or `gsheets_get_spreadsheet`), then read only tabs with an obvious job. CS is the positive case: `adjustments` tabs on 7 of 496 sheets were found by 6 of 6 because the feed doc said they exist; CS6 also used `modifiedTime` differing from `createdTime` to pick which sheets to open twice.
- Read-back after writing: LLC 5 of 6, WD 3 of 6, CS 3 of 6, BR 1 of 6 re-read the sheet they wrote, usually only the total or tail rows.
- The draft/template sheet is opened with `valueRenderOption: FORMULA` in LLC (6 of 6): runs copy layout faithfully.

## 7. Subagents

| Task | Runs that spawned | Agents | Brief | Coverage effect |
|---|---|---|---|---|
| LLC | 0 of 6 | 0 | - | - |
| WD | 0 of 6 | 0 | - | - |
| CS | 5 of 6 (CS2 did not) | 34, 5, 8, 8, 17 | "Mechanical download task": read every file in a list, copy raw to `/app/...` as xlsx or CSV, "Do not transcribe or summarize", report a count | Finished the 496-sheet read. CS2 read all 496 itself, so subagents changed cost, not coverage. All six ended with the same 653 rows |
| BR | 1 of 6 (BR1) | 2 | "Summarize investor email threads A/B": read listed threads, report party, every message, quote accept/decline sentences verbatim | 13 calls on 7 threads. BR1 still missed Paul and Sciplay (both in Slack, outside the brief) |

- Subagents are used for **enumerated, already-listed work**, never for open search. No brief says "look for anything unusual", and no subagent was given Slack.
- Requested `sonnet` / `haiku` overrides (CS1, CS4, CS5) did not take: every subagent call reports `claude-opus-5-5`.
- Consequence: subagent output is raw files parsed by the main run, so nothing is noticed in transit. A subagent scope is the list it is handed; a record outside the list stays unread.

## 8. Per-trap catch rates

| Task | Trap | Deciding record sits in | Caught | How catching runs got it |
|---|---|---|---|---|
| LLC | VO line | Leonard's reply in a `#prototype` thread, no issue | 1/6 | LLC3: Slack `card after:2026-02-01`, then `from:<Leonard> after:2026-02-11`, then `read_thread` |
| LLC | layer.ai by Mar 3 | Leonard's reply, same channel | 1/6 | LLC3, same sweep |
| LLC | ENG-2462 reopened | Apple App Review mail in Robert's box, Feb 13 | 3/6 | LLC2, 3, 6: the three runs that swept the mailbox by date. The other three did not sweep |
| LLC | DD take test | Arthur's DM + warehouse | 5/6 | `read_thread` on the DM the Linear/DM trail pointed to. LLC5 skipped it |
| LLC | CF stacks $62 | Jenkins mail | 5/6 | Gmail `AWS` / `metabase` searches |
| WD | Unity closed | Arthur's top-level `#executives` note, Feb 13 21:18 UTC | 1/6 | WD5: Slack `after:2026-02-08 unity` and a page of `#executives` |
| WD | Cursor closed | Arthur's `#prototype` reply | 4/6 | Slack `cancel*` date-bounded (WD1, 3, 5), `cursor` (WD2) |
| WD | CodeRabbit closed | GitHub bot comment on PR 38 | 0/6 | One `github_search_code` call in 6 runs |
| WD | Slack plan clash | `#winddown` decision vs Sunset checklist | 3/6 | All 6 read both sides. **The only judgment miss found:** WD1 and WD5 wrote "something to check, not a clash" |
| BR | Paul out | Leonard's DM, Sep 30 | 3/6 | BR3, 4, 6: exactly the runs that read the DM |
| BR | Sciplay | Robert's thread reply in `#executives` | 3/6 | BR2 `pass`, BR5 `sciplay`, BR6 search + spill parse. Channel readers missed it |
| BR | Build access | Arthur's `#zombie-match3d` post | 3/6 | BR1, 3 `tester`; BR6 `internal test`. Then `read_thread`. No run read that channel |
| BR | Homa, Brightwater | Calendar only | 6/6 | All listed events for the window |
| CS | Griffin's answers | Leonard's DM, Sep 30 | 6/6 | All read the clock-week DM |
| CS | Adjustments tabs | 7 of 496 sheets, second tab | 6/6 | Feed doc says they exist |
| CS | Sensor Tower keep | `#executives` thread reply | 4/6 | `read_thread` from the card's pointer to the Sep 23 thread |
| CS | LinkedIn cancelled | Vendor mail to Frederick | 5/6 | Gmail cancel words + vendor |
| CS | Edgegap confirmed | Vendor mail, cc Frederick | 5/6 | Same |
| CS | SavvyCal, Buttondown | Leonard's forwards, not on the board | 1/6 | CS6: `gmail_list_threads` on a date+term query, read snippets, `get_thread` on each |
| CS | WeWork | Leonard's forward | 1/6 | CS6, same |
| CS | Webflow, Murf | Forward; vendor mail | 0/6 | Webflow hit once as a bare id (CS2), unopened |

**Seen means used.** I traced 16 of the traps above record by record. Every run that had the record's text in a result passed that trap (35 run-trap cases, 0 exceptions). Every failure was a run that never had the text. Bare-id hits left unopened (7 cases: CS2 four, CS4 three) all failed. The single judgment miss is the WD clash, where a classification word decided it. So a miss on these tasks is a retrieval miss.

**Habits that split runs near 50 %:** date sweep of the mailbox (LLC 3/6, Robert overall 6/12); reading the clock-week DM (BR 3/6); a date-bounded generic Slack word (WD 4/6, BR 3/6); `read_thread` from a pointer (CS 4/6).
**Places that gave 0-1 of 6:** a surface no hub names (GitHub 0/6), mail with no name in the run's list (CS 0-1/6), a reply off the swept channels (LLC 1/6), a top-level note in an unread channel on an unsearched word (WD Unity 1/6).

Gmail hit open rates, opened / hits: BR 71 % / 66 % / 36 %, CS 49 % / 14 % / 12 %, LLC 10 % / 12 % / 15 %, WD 41 % / 25 % / 15 %, for 1-10, 11-50 and 51+ hits.

## 9. Channel miss estimates (RET, OFF, ORPH, CORR, ALIAS, OVR, CURR)

P(miss) means a run ends without the deciding fact applied. Basis: **M** measured analog, **G** guess. Every number is an estimate from four tasks, none of which had a multi-year bank spine, so all carry a G component. Assumes the method record as described in the plan's section 4 ("stayed out", off-bank contractors, the "tied to one game" exception).

| Channel | Plan | Estimate | Range | Mostly |
|---|---|---|---|---|
| RET | 0.45 | **0.85** | 0.75-0.92 | M on routes, G on the method's effect |
| OFF | 0.50 | **0.60** | 0.45-0.75 | M analogs, G on wording |
| ORPH | 0.40 | **0.50** | 0.35-0.65 | M |
| CORR | 0.45 | **0.60** | 0.45-0.80 | M, depends on seed date |
| ALIAS | 0.40 | **0.60** weight-averaged (MotMot 0.75, Node 0.55, Creative X 0.50) | 0.45-0.80 | Mostly G: no task had an opaque payee |
| OVR | 0.45 | **0.50** | 0.35-0.65 | M + G |
| CURR | 0.25 | **0.45** row level (currency alone 0.30, laptop label 0.55) | 0.25-0.60 | G for currency |

Mean 0.59 against the plan's 0.41.

**RET: 0.85.** The note is in a channel 0 of 24 runs opened, 22 months back when the deepest channel read was 1 month, and it names neither payee, so name searches (the only undated habit) miss it.
- Route a, channel read: 0 of 24. Estimate 0.01-0.02.
- Route b, Slack word `returned` / `wrong account`: 0 of 147 today. The "stayed out" clause might prompt it (G 0.15-0.30), and the mirroring habit says literal words beat paraphrases. Then the hit must land in a newest-first page of 20-50 with 0 of 147 paging (G 0.3-0.5). Net 0.05-0.15. The hit rank of `returned` is checkable and should be, since census D scanned that term.
- Route c, amount: 0 of 339 searches, and the note carries no amount anyway.
- Route d, Recipient Modified mail (`00004120`) from a `BANCO` mail search, then inference: about 0.04 (G).
- Lowers it: any record reachable by `BANCO`, `MotMot`, or a date sweep near the clock; a method sentence using the word "returned". Raises it: nothing needed. Nearest analogs: CS Webflow and Murf 0/6, WD CodeRabbit 0/6.

**OFF: 0.60.** Analogs: mail outside the run's list CS 0-1/6; mail in a date sweep LLC 3/6; a named feed row sending the run to mail, Fiverr 6/6 (2 hits, opened by all). OFF sits between: the method clause gives a reason to look, the run must pick the right word. A `Lucas` Gmail search should match the receipts' "Lucas's digital wallet" text and return a small hit set, which runs open at 41-71 % on WD/BR. It needs the name `Lucas`, since the notices show a token; check the issue spells it. Slack `Lucas` shows "payment to Lucas OK to go?" but "via company card" sits in the next messages and carries no name, and windowed reads are 5 of 24.
- Lowers it: the method naming Western Union or the card (to about 0.2, G); any hub naming `HG Costs`, because 6 of 6 read a named tab and its row is $13,975 against $6,450 (to about 0.35, G). Raises it: "paid another way" with nothing else (0.75, G).

**ORPH: 0.50.** Slack name search is undated, newest first, so a Feb 13 post with the word Leapblock tops any `leapblock` hit list, and seen means used. The limit is whether the run searches that payee at all. WD runs name-searched Slack for 0-6 of 28 vendors: 18 of 168 vendor-run pairs, 11 % overall, 33-50 % for vendors with an open question (`coderabbit`, `elevenlabs` 3/6; `ipostal`, `layer`, `pond5`, `trello` 2/6). The bet calendar assigns Leapblock by date, so nothing opens a question unless the run also reads Awaiting notices. Its size and its own channel lift the rate above 11 %. Date-bounded sweeps by person (`from:<Leonard>`) would not catch a post from the payee.
- Lowers it: any pointer to `#leapblock` from the payee issue or method; the word "statement" in the method. Raises it: posting it as a thread reply (invisible to `read_channel`); a post that does not spell Leapblock.

**CORR: 0.60.** Its issue already gives an answer, so no question prompts a search. That is the shape of Frederick Q4 (0/6 per the plan's lesson) and BR Sciplay (3/6). Routes: date sweep of mail (6 of 12 Robert runs), then subject skim; or `JPMorgan` / `Chase` per-payee search (small hit set). If the mail is dated in the last 9 days of the clock, about 0.50. If older, sweeps miss it and it depends on a name search, about 0.80.
- Lowers it: a late date and a subject carrying Chase, JPMorgan or Carta. Raises it: an older date or a subject like "fyi".

**ALIAS: 0.60.** Amount search is 0 of 339, so "by amount" is not a route on measured habit. The plan's route is the least supported of the seven. Caveat: no earlier payee was opaque, so a run holding only `BANCO DE AMERICA` may behave differently (G: 0.15-0.30 tries an amount).
- MotMot 0.75: `BANCO` matches nothing useful in Slack and Arthur's note is in the founder channel. `4032` would hit it.
- Node 0.55: the notice's token may match the mail, because the subject of `00008689` carries `PERSON_4419_NAME`. Token search exists (BR2 tried one). $16,428.57 is not spelled in that mail, so a run must add up the months.
- Creative X 0.50 (G): `#playablex` exists and a name search might reach it.
- Lowers it: the Salary tab's "MotMot + Blake LLC" row or the `UA Assets` row, if a hub names them. Raises it: nothing needed.

**OVR: 0.50.** The rule itself is safe: rule-led items are 6/6 once read. The miss is reaching the fact. `#telegram-dd` carries the answer in its name, and a `telegram` or `Brooks` search reaches `#executives` and the agreement file. The exception gives a reason to test each payee, but runs test what looks open: 11 % per vendor in WD, 33-50 % with an open question. If the issue says "Telegram contractor", the miss falls to about 0.35 (G). If it shows only the notice's name, about 0.65 (G).

**CURR: 0.45 at row level.** The currency is in the notice, but runs parse by script. My own parse returned a null on that row, which is the likely first sign: a USD regex fails and a run checking row counts sees it (CS runs checked counts). A loose number regex would pass 1,999 as USD. No task tested this: CS amounts were already USD. Currency alone 0.30 (G). The laptop label needs `Martin` in Slack, a clean spelled name reaching `#admin_foundersonly` by search, 0.55. The USD value needs settling first, as the plan notes.

**What the retrieval finding changes.** The plan says CORR, ALIAS and OVR survive complete retrieval because a rule applies after the record is found. Measured, that step never failed (35 of 35). Only a soft classification word did (WD clash, 3/6). So all seven channels should be treated as retrieval traps. A run that finds them all gets them all.

## 10. Bank notice full read; two $4,032 payments

**What a read costs.** The snippet stops before the payee and amount: "SVB Payment Notification: Payment Processed Hello [PERSON_NAME_0054],The following payment has been " (WD3, the only run that saw one). So default, `metadata` and `minimal` show nothing usable; a run needs bodies. `format: full` is capped at **10 ids per batch**, so 132 notices are at least 14 batch calls, not the 2 in the plan's section 7 (which assumes 100 ids). At `sizeEstimate` 7,540 bytes, ten notices are about 75k characters. Results spill above roughly 50k (52,676 spilled, 49,952 did not), so each batch spills and needs a base64 decode in Bash.

**Share reading all 132: about 0.85 (range 0.65-0.95), by script.** This assumes the method names the notices as source of record.
- For: CS 6 of 6 read all 496 sheets once the ask named the folder, paging Drive in all 6. BR6 decoded 112 messages in full with its own `dec.py`. BR4 parsed a spilled batch of 50. Every run handled spills.
- Against: no Gmail set over 60 has ever been read in full. WD left 500+ SVB hits unread, though nothing asked for them. 0 of 24 used a Gmail page token and the default page is 100 of 132, though 25 calls in 15 runs set `max_results` of 100 or more and 6 of 6 paged Drive.
- If the method does not name the notices as the source, this falls below 0.2, per WD.
- Reading by eye: about 0. A run sees its parser's table.

**Two $4,032 payments.** Facts: Apr 2 to `BANCO DE AMERICA ***8605`, Apr 5 to `***3341`. Five $4,032 notices exist in all, so the amount itself looks routine. There is no measured basis: no task planted a near-duplicate.
- Sees both rows in its table: about 0.75 (0.85 full read x 0.9 parser keeps the suffix; G for the second factor). Runs must collapse 25 spellings to 22 payees, so the two suffixes get looked at.
- Remarks on the pair in a comment or reply: about 0.30 (G). The analog is CS's off-list vendors, 2 of 6.
- Chases it to the Apr 2024 note: about 0.10 (G). The same analog chased 0 of 2.
- Nets it out with no record: about 0.03 (G).
- Likeliest outcome: both suffixes merged under one payee and summed to $41,088.

## 11. Per-run rubric facts for the SD gate

Scores reproduce from each verifier file with `09_Rubrics.json` weights. BR's `In talks 7` row is not its own trap: it fails whenever Paul or Sciplay does, so it is left out here. All six BR runs placed Homa and Brightwater.

| Task | Trap channels | Failed per run (1-6) | Mean | SD of count | Weighted score % | Avg | Pop SD | Full passes |
|---|---|---|---|---|---|---|---|---|
| LLC | 5 (VO, layer.ai, ENG-2462, DD, stacks) | 3, 2, 0, 3, 5, 2 | 2.50 | 1.50 | 82.3, 85.7, 100, 82.3, 64.9, 86.6 | 83.6 | 0.103 | 1 |
| WD | 4 (Unity, Cursor, CodeRabbit, clash) | 3, 3, 2, 3, 2, 3 | 2.67 | 0.47 | 85.6, 85.0, 86.6, 81.6, 92.4, 83.2 | 85.7 | 0.034 | 0 |
| CS | 7 (Sensor, LinkedIn, Edgegap, 2 forwards, WeWork, Webflow, Murf) | 5, 4, 4, 4, 6, 3 | 4.33 | 0.94 | 75.3, 79.0, 79.0, 79.0, 69.5, 87.7 | 78.3 | 0.054 | 0 |
| BR | 3 (Paul, Sciplay, build access) | 2, 2, 1, 2, 2, 0 | 1.50 | 0.76 | 73.2, 73.2, 79.2, 67.3, 73.2, 100 | 77.7 | 0.106 | 1 |

| Task | Rows | Rows passing all 6 | Their weight | Rows failing all 6 | Discriminating rows | SD without best run | SD without worst run |
|---|---|---|---|---|---|---|---|
| LLC | 130 | 97 | 64.9 % | 0 | 33 | 0.079 | 0.065 |
| WD | 136 | 111 | 77.4 % | 5 | 20 | 0.018 | 0.031 |
| CS | 63 | 44 | 65.0 % | 4 | 15 | 0.037 | 0.041 |
| BR | 40 | 27 | 61.3 % | 0 | 13 | 0.038 | 0.104 |

- **Both tasks that cleared SD 0.1 had a 100 % run,** and neither clears it without that run. WD and CS had no full pass, and both had traps missed 6/6.
- A 0/6 trap adds nothing to SD. In CS two of seven channels were 6/6 and two were 5/6 with the same catcher; in WD one of four was 6/6.
- Trap-count dispersion against independence: LLC 1.50 vs 0.90 (over), BR 0.76 vs 0.87, WD 0.47 vs 0.78 (under), CS 0.94 vs 0.88. One task of four shows a thoroughness latent. rho 0.35 is on the high side.

**The plan's model with these miss rates** (`policy_model.py` imported read-only, 6,000 sims; inputs are estimates, and this model has overstated SD before: LLC proxy 0.17, real 0.103):

| Rubric shape | rho | E[avg] | Mean six-run SD | P(SD in band and avg < 90 %) |
|---|---|---|---|---|
| Weight 108 | 0.35 | 56 % | 0.149 | 0.85 |
| Weight 108 | 0.10 | 56 % | 0.113 | 0.60 |
| One row per close (+16) | 0.35 | 62 % | 0.130 | 0.76 |
| One row per close (+16) | 0.10 | 62 % | 0.098 | 0.44 |
| Row per close and comment (+38) | 0.35 | 68 % | 0.110 | 0.60 |
| Row per close and comment (+38) | 0.10 | 67 % | 0.083 | 0.26 |

- The average gate looks safe: the risk has moved to the SD and all-fail side.
- P(a channel misses in all six, independent): RET 0.38; OFF, CORR, ALIAS 0.05; ORPH, OVR 0.02; CURR 0.01.
- P(one run catches everything) is well under the plan's 0.02. So the 100 % run that carried LLC and BR should not be expected.
- Shared habits make channels land together: RET, MotMot and the laptop label need founder-channel reach; OFF and CORR need the mail sweep or a name search. Two habits, so fewer independent patterns than seven channels suggest.

## Appendix A. Gmail query strings (unique, with runs)


**LLC** (16 unique)

- `from:leonard.hayes@harmonygames.co newer_than:30d` runs [1, 4, 5, 6]
- `LLC OR split OR "Combo Fighter" OR Sunset newer_than:14d` runs [1]
- `AWS OR "amazon web services" OR billing newer_than:30d` runs [1]
- `boombit newer_than:120d` runs [1]
- `from:leonard.hayes@harmonygames.co` runs [2]
- `(metabase OR dbt OR github OR KubLLC) newer_than:30d` runs [2]
- `after:2026/02/09 -from:github.com -from:notifications` runs [2]
- `from:leonard.hayes@harmonygames.co newer:2026/02/09` runs [3]
- `"Calm Play" OR metabase OR github OR dbt newer:2026/01/15` runs [3]
- `newer:2026/02/09 -from:leonard.hayes@harmonygames.co` runs [3]
- `LLC OR split OR "combo fighter" newer_than:14d` runs [4]
- `AWS newer_than:30d` runs [4]
- `metabase OR dbt OR github OR KubLLC newer_than:60d` runs [5]
- `github (receipt OR invoice OR billing OR plan)` runs [6]
- `after:2026/02/10 -from:github.com` runs [6]
- `Sunset (sale OR auction OR close)` runs [6]

**WD** (84 unique)

- `Sunset` runs [1, 2, 3, 4, 5]
- `SVB` runs [1, 3]
- `after:2026/02/08` runs [1, 2]
- `SVB card after:2026/02/01` runs [1]
- `Pond5 OR ElevenLabs OR "Eleven Labs"` runs [1]
- `layer.ai OR "Layer AI" OR from:layer.ai` runs [1]
- `(receipt OR invoice OR payment) (Layer OR iPostal OR Trello OR Figma OR Lucidchart OR "Google Ads" OR Pond5 OR ElevenLabs OR Intuit OR QuickBooks OR CodeRabbit) after:202` runs [1]
- `from:ipostal` runs [1]
- `from:figma` runs [1]
- `from:lucid` runs [1]
- `from:elevenlabs` runs [1]
- `from:pond5` runs [1]
- `from:trello OR from:atlassian` runs [1]
- `"Eleven Labs"` runs [1]
- `subject:(iPostal OR "iPostal1")` runs [1]
- `subject:Figma (receipt OR invoice OR renewal OR payment)` runs [1]
- `Lucidchart OR "Lucid Software"` runs [1]
- `subject:Trello (receipt OR invoice OR Standard OR Premium OR billing)` runs [1]
- `"Google Ads" (receipt OR invoice OR payment)` runs [1]
- `CodeRabbit` runs [1]
- `iPostal1 after:2025/06/01` runs [1]
- `(Intuit OR QuickBooks) after:2025/10/01` runs [1]
- `(Layer OR "layer.ai") (receipt OR subscription OR invoice OR cancel)` runs [1]
- `Unity after:2026/02/09` runs [1]
- `(Helpshift OR Zapier OR Kapwing OR Cursor OR Docusign OR 1Password OR Carta) after:2026/02/09` runs [1]
- `SVB card` runs [2, 4, 6]
- `Pond5` runs [2]
- `elevenlabs OR "eleven labs"` runs [2]
- `elevenlabs (receipt OR invoice OR subscription OR payment OR cancel)` runs [2]
- `figma (receipt OR invoice)` runs [2]
- `trello (receipt OR invoice OR atlassian)` runs [2]
- `ipostal` runs [2]
- `layer` runs [2]
- `coderabbit` runs [2]
- `lucid OR lucidchart` runs [2]
- `quickbooks OR intuit` runs [2, 5, 6]
- `Layer (cancel OR cancelled OR canceled OR subscription)` runs [2]
- `from:trello OR subject:trello after:2024/10/01` runs [2]
- `trello (premium OR standard OR billing OR "free plan" OR downgrade)` runs [2]
- `"mail storage" OR "virtual mailbox" OR "ipostal1"` runs [2]
- `subject:(quickbooks OR intuit) (invoice OR receipt OR payment OR billing OR subscription)` runs [2]
- `quickbooks` runs [2]
- `pond5 OR elevenlabs OR soundly` runs [3]
- `layer OR lucidchart OR ipostal OR calendly` runs [3]
- `cursor OR coderabbit OR 1password OR intuit OR quickbooks` runs [3]
- `unity OR singular OR trello after:2026/02/01` runs [3]
- `subject:(receipt OR invoice OR cancelled OR canceled OR cancellation OR subscription OR renewal OR payment OR billing) after:2025/09/01` runs [3]
- `pond5` runs [3, 5, 6]
- `elevenlabs (receipt OR invoice OR subscription OR cancel OR plan)` runs [3]
- `after:2026/02/09 (layer OR cursor OR coderabbit OR unity OR singular OR zapier OR kapwing OR helpshift OR 1password OR docusign)` runs [3]
- `from:intuit OR subject:quickbooks` runs [3]
- `SVB after:2026/02/01` runs [4]
- `(pond5 OR elevenlabs OR soundly) newer_than:2y` runs [4]
- `from:elevenlabs.io` runs [4]
- `from:pond5.com` runs [4]
- `from:soundly.com OR subject:soundly` runs [4]
- `subject:(pond5 OR elevenlabs OR "eleven labs") ` runs [4]
- `(receipt OR invoice OR subscription OR cancelled OR canceled) after:2025/11/01 -from:me` runs [4]
- `subject:(layer OR trello OR ipostal OR lucid OR lucidchart OR figma OR kapwing OR zapier) after:2025/01/01` runs [4]
- `subject:(unity OR helpshift OR coderabbit OR cursor OR 1password OR docusign OR "google ads" OR singular) after:2026/01/15` runs [4]
- `ipostal OR "ipostal1" OR "mail center"` runs [4]
- `after:2026/02/09 (unity OR helpshift OR coderabbit OR cursor OR kapwing OR zapier OR 1password OR docusign OR gusto OR layer OR singular)` runs [4]
- `from:ipostal1.com OR from:ipostal.com OR subject:ipostal` runs [4]
- `after:2026/01/01 (receipt OR invoice OR cancel OR cancelled OR canceled OR subscription OR renewal)` runs [5]
- `ElevenLabs OR Pond5 OR Layer OR Lucidchart OR iPostal OR Trello OR CodeRabbit OR Cursor OR Unity OR Figma OR Intuit OR QuickBooks` runs [5]
- `elevenlabs` runs [5, 6]
- `subject:layer OR from:layer` runs [5]
- `lucidchart OR lucid` runs [5]
- `ipostal OR "mail storage"` runs [5]
- `after:2026/02/09 (unity OR singular OR coderabbit OR cursor OR trello OR figma OR docusign OR 1password OR zapier OR kapwing)` runs [5]
- `(ipostal OR bizxpress) (invoice OR receipt OR charged OR payment OR renew)` runs [5]
- `bizxpress -"Order Confirmation" -"Mailbox Storage"` runs [5]
- `(eleven labs OR elevenlabs OR "eleven labs") (receipt OR invoice OR subscription OR starter OR creator OR paid OR cancel)` runs [5]
- `after:2026/02/10 (unity OR coderabbit OR cursor OR layer OR "1password" OR intuit OR gusto)` runs [5]
- `(trello OR atlassian) (receipt OR invoice OR premium OR standard OR downgrade OR "free")` runs [5]
- `figma (receipt OR invoice OR renewal OR "professional")` runs [5]
- `(1password OR docusign OR zapier OR kapwing OR gusto OR deel OR slack OR "google workspace") (receipt OR invoice OR cancel)` runs [5]
- `Sunset OR SVB` runs [6]
- `after:2026/02/05` runs [6]
- `Lucidchart OR Lucid OR Layer OR iPostal OR Pond5 OR ElevenLabs OR Calendly OR Trello receipt OR Figma invoice` runs [6]
- `(trello OR atlassian OR ipostal OR intuit OR quickbooks OR lucid OR layer OR figma) newer_than:1y` runs [6]
- `(receipt OR invoice OR subscription OR cancelled OR canceled OR renew) newer_than:8m -from:substack` runs [6]
- `subject:(receipt OR invoice OR subscription OR cancelled OR renewal) after:2025/08/01` runs [6]
- `"Eleven Labs" OR "ElevenLabs Starter" OR "elevenlabs creator" OR from:elevenlabs.io receipt` runs [6]

**CS** (33 unique)

- `from:leonard after:2025/09/28 before:2025/10/01` runs [1, 3]
- `conference passes OR Unity OR "opex categories" OR "card feed" OR "card close"` runs [1]
- `AppMagic OR "Sensor Tower" OR LinkedIn OR Canva OR Edgegap OR Zoom OR cancellation OR subscription` runs [1]
- `(linkedin OR "sales navigator" OR canva OR envato OR 1password OR unity OR notion OR zoom OR chatgpt OR openai) newer_than:2y -from:leonard.hayes@harmonygames.co` runs [1]
- `subject:(cancelled OR canceled OR cancellation OR "plan change" OR "price" OR "subscription" OR "plan has been") after:2025/01/01` runs [1]
- `from:(.mail) after:2025/01/01` runs [1]
- `griffin after:2025/08/01` runs [1]
- `fiverr after:2025/06/01` runs [1]
- `from:leonard after:2025/09/28 before:2025/09/30` runs [2, 4, 5, 6]
- `conference passes OR Unity seats OR "opex categories"` runs [2, 5]
- `Griffin after:2025/08/01` runs [2]
- `Unity OR conference OR "Standard Metrics" after:2025/08/10` runs [2]
- `cancel OR cancellation OR downgrade OR subscription OR "plan change" after:2025/01/01` runs [2]
- `"engine licences" OR "conference passes" OR "Unity seats" OR "opex categories" OR "2025 categories"` runs [2]
- `fiverr` runs [2]
- `(zapier OR wework OR webflow OR savvycal OR buttondown OR docusign OR midjourney OR loom OR zoom OR 1password OR unity OR envato OR notion OR openai OR chatgpt OR edgegap` runs [2]
- `(confirmed OR receipt OR renewal OR "your plan" OR seats) after:2025/06/01 -from:leonard.hayes@harmonygames.co` runs [2]
- `Griffin OR "Standard Metrics" OR "card feed" OR "Unity seats" OR "conference passes"` runs [3]
- `sensor tower OR appmagic OR linkedin OR canva OR zoom OR edgegap OR envato OR docusign OR midjourney OR loom OR notion OR chatgpt OR openai OR supernormal OR 1password OR` runs [3]
- `(subscription OR cancel OR cancelled OR cancellation OR downgrade OR receipt OR invoice OR renewal) after:2025/06/01` runs [3]
- `"conference passes" OR "engine licences" OR "engine licenses" OR "opex categories"` runs [3]
- `after:2025/08/01 (Griffin OR Unity OR "conference passes" OR "card spend" OR "Standard Metrics" OR categories)` runs [4]
- `after:2025/09/29` runs [4]
- `{"Sensor Tower" AppMagic LinkedIn Edgegap Canva Zoom Midjourney Loom Notion Backtrace Supernormal 1Password Unity cancel cancellation downgrade subscription} after:2025/0` runs [4]
- `from:(edgegap.mail OR appmagic.mail OR sensortower.mail OR linkedin.mail OR murf.mail OR canva OR zoom OR midjourney OR loom OR notion OR 1password OR unity3d OR backtrac` runs [4]
- `subject:(subscription OR plan OR refund OR receipt OR cancelled OR canceled OR renewal OR price OR seats OR invoice) after:2025/01/01` runs [4]
- `Sensor Tower OR AppMagic OR LinkedIn OR Edgegap OR Zoom OR Griffin OR Canva OR Envato` runs [5]
- `(cancel OR cancelled OR cancellation OR downgrade OR subscription OR plan OR refund) after:2025/01/01` runs [5]
- `LinkedIn OR "Sales Navigator" OR Unity OR "conference pass" OR Standard Metrics` runs [5]
- `"engine licences" OR "engine licenses" OR "conference passes" OR "Q3 submission" OR "Unity seats"` runs [5]
- `after:2025/08/01 (Griffin OR Unity OR "conference passes" OR "card spend" OR "Standard Metrics")` runs [6]
- `after:2025/01/01 (cancel OR cancelled OR cancellation OR downgrade OR downgraded OR refund OR "subscription" OR "membership")` runs [6]
- `fiverr OR playtestcloud OR "best buy" OR "apple store"` runs [6]

**BR** (37 unique)

- `from:leonard after:2025/09/29 before:2025/10/02` runs [1, 3]
- `from:leonard investor update bridge` runs [1, 3, 5]
- `docusign after:2025/09/01` runs [1, 2, 4, 5, 6]
- `(Paul OR Heydon OR Anton OR Kevin OR Fischer OR Demetri) after:2025/09/01` runs [1]
- `after:2025/09/02 -from:calendar-notification` runs [1]
- `after:2025/08/25 -category:promotions -from:tiktok.com -from:apple.com -from:facebookmail.com` runs [1]
- `Edith OR Vane` runs [1]
- `(Demetri OR Fischer OR "Kevin Lin" OR Bernstein OR Heydon) after:2025/08/30` runs [1]
- `from:leonard after:2025/09/29` runs [2, 4, 5, 6]
- `(Anton OR Bernstein OR Heydon OR "Kevin Lin" OR Fischer OR Detsaridis OR Demetri) after:2025/08/25` runs [2]
- `after:2025/09/02 before:2025/10/02 -category:promotions` runs [2, 4]
- `"PERSON_2534_EMAIL" OR Laton` runs [2]
- `after:2025/09/01 before:2025/10/02 (invitation OR invite)` runs [3]
- `after:2025/09/01 before:2025/10/02` runs [3]
- `after:2025/09/01 before:2025/10/02 -from:calendar-notification@google.com` runs [3]
- `docusign` runs [3]
- `(Kevin OR Mike OR Demetri OR Anton OR Paul OR SAFE OR angel) after:2025/09/01` runs [3]
- `Edith OR Karthic OR Rutik` runs [3]
- `(ncsoft OR homa OR bitkraft OR transcend OR acterra OR "core finance" OR "Initial Capital" OR treo OR "mini fund") after:2025/09/01` runs [3]
- `(completed OR SAFE OR envelope) after:2025/09/01` runs [4]
- `Rohan` runs [4]
- `after:2025/09/02 (Transcend OR Acterra OR Bitkraft OR "Initial Capital" OR BBQ OR Superplay OR Sony OR Revo OR e2vc OR Treo OR Triptyq OR Turkven OR Harlem OR "General Ca` runs [4]
- `after:2025/09/02 (Kevin OR Fischer OR Demetri OR Detsaridis OR Anton OR Bernstein OR Heydon)` runs [4]
- `after:2025/09/02 Acterra` runs [4]
- `after:2025/09/02 (Transcend OR "General Catalyst" OR Galaxy OR Index OR Superplay)` runs [4]
- `after:2025/09/02 "Index"` runs [4]
- `after:2025/09/02 "Galaxy"` runs [4]
- `after:2025/09/02 "General Catalyst"` runs [4]
- `(Kevin Lin OR Fischer OR Detsaridis OR Bernstein OR Heydon) after:2025/09/01` runs [5]
- `(angel OR SAFE OR Kevin OR Mike OR Demetri OR Anton OR Paul) after:2025/09/02 before:2025/10/02` runs [5]
- `after:2025/09/02 before:2025/10/02 -from:calendar-notification@google.com` runs [5]
- `Edith` runs [5]
- `(SciPlay OR a16z OR Homa OR NCsoft OR Rohan) after:2025/09/18` runs [5]
- `bridge investor update` runs [6]
- `(Anton OR Paul OR Heydon OR Bernstein OR SAFE OR Kevin OR Fischer OR Demetri) after:2025/09/01` runs [6]
- `after:2025/08/25 before:2025/10/08` runs [6]
- `after:2025/08/25 before:2025/10/08 (from:harmonygames.co OR to:harmonygames.co) -category:promotions` runs [6]

## Appendix B. Slack search strings (unique, with runs)


**LLC** (20 unique)

- `Sunset  filter_date_after=2026-02-01` runs [1]
- `lifestyle` runs [1, 2, 3, 4, 5, 6]
- `AWS  filter_date_after=2026-01-20` runs [1]
- `boombit  filter_date_after=2025-10-01` runs [1]
- `LLC  after=1770500000` runs [2]
- `from:<@EMPLOYEE_0025_SLACK_ID> month  after=1769900000` runs [2]
- `aws  after=1769000000` runs [2]
- `metabase  after=1769500000` runs [2]
- `github  after=1769500000` runs [2]
- `from:<@EMPLOYEE_0025_SLACK_ID> after:2026-02-08` runs [3]
- `"Calm Play"` runs [3]
- `card after:2026-02-01` runs [3]
- `from:<@EMPLOYEE_0038_SLACK_ID> after:2026-02-11` runs [3]
- `Calm Play` runs [4]
- `aws after:2026-01-25` runs [4]
- `after:2026-02-11` runs [4, 6]
- `KubLLC` runs [5]
- `LLC` runs [6]
- `metabase after:2026-02-08` runs [6]
- `from:<@EMPLOYEE_0025_SLACK_ID> after:2026-02-11` runs [6]

**WD** (22 unique)

- `SVB card` runs [1]
- `cancel* after:2026-02-08` runs [1]
- `layer` runs [1]
- `receipt` runs [1]
- `elevenlabs` runs [2, 3, 6]
- `coderabbit  filter_date_after=2026-01-15` runs [2]
- `cursor  filter_date_after=2026-01-15` runs [2]
- `ipostal` runs [2, 6]
- `cancel*  filter_date_after=2026-02-08` runs [2]
- `quickbooks` runs [2]
- `pond5` runs [3, 6]
- `after:2026-02-08 cancel` runs [3, 5]
- `coderabbit after:2026-02-01` runs [3]
- `after:2026-02-08 subscription` runs [5]
- `coderabbit` runs [5]
- `after:2026-02-08 unity` runs [5]
- `after:2026-02-08 trello` runs [5]
- `after:2026-02-11 (singular OR layer OR figma OR slack OR intuit OR zapier OR kapwing OR helpshift OR docusign OR deel OR github OR metabase OR dbt OR ` runs [5]
- `lucidchart` runs [6]
- `layer after:2026-01-01` runs [6]
- `trello after:2026-01-15` runs [6]
- `eleven after:2025-10-01` runs [6]

**CS** (13 unique)

- `Griffin  after=1754006400` runs [1]
- `from:<@EMPLOYEE_0038_SLACK_ID> on:2025-09-23` runs [1]
- `fiverr` runs [1, 6]
- `Griffin categories` runs [2, 6]
- `Fiverr` runs [2]
- `in:#executives subscriptions` runs [2]
- `screenshots freelancer after:2025-06-01` runs [2]
- `in:#executives cut` runs [3]
- `Griffin` runs [3, 4]
- `card  after=1758000000` runs [4]
- `Unity seats` runs [5]
- `in:#executives after:2025-09-20` runs [6]
- `filter_date_on=2025-09-23 filter_in_channel=C07C2866011` runs [6]

**BR** (65 unique)

- `signed in:#executives` runs [1, 2, 4]
- `SAFE  after=1756684800` runs [1, 3, 4]
- `docusign  after=1756684800` runs [1, 4]
- `counts  after=1756684800` runs [1, 4]
- `testflight  after=1756684800` runs [1]
- `tester  after=1756684800` runs [1, 3]
- `Kevin  after=1756800000` runs [1, 4]
- `angel  after=1756800000` runs [1, 4]
- `SAFE  after=1756252800` runs [2]
- `docusign  after=1756252800` runs [2]
- `counts as signed` runs [2]
- `Kevin OR Mike OR Demetri OR angel  after=1756252800` runs [2]
- `angel  after=1756252800` runs [2]
- `Demetri` runs [2, 4, 6]
- `Fischer` runs [2, 6]
- `"Kevin Lin"` runs [2]
- `pass  after=1756800000` runs [2]
- `TestFlight  after=1756800000` runs [2]
- `in:#executives signed` runs [3, 5]
- `angel  after=1756684800` runs [3]
- `docusign` runs [3]
- `NCsoft  after=1757980000` runs [3]
- `Homa` runs [3]
- `Rohan` runs [4]
- `Mike  after=1756800000` runs [4]
- `Paul  after=1756800000` runs [4]
- `testflight  after=1756800000` runs [4]
- `Transcend  after=1756800000` runs [4]
- `Acterra  after=1756800000` runs [4]
- `Superplay  after=1756800000` runs [4]
- `Homa  after=1756800000` runs [4]
- `GFR  after=1756800000` runs [4]
- `SAFE  after=1756700000` runs [5]
- `in:#executives counts  after=1756700000` runs [5]
- `docusign  after=1756700000` runs [5]
- `Anton  after=1756700000` runs [5]
- `angel  after=1756700000` runs [5]
- `Homa  after=1756700000` runs [5]
- `testflight  after=1756700000` runs [5]
- `Edith` runs [5]
- `sciplay  after=1758150000` runs [5]
- `passing  after=1756800000` runs [5]
- `signed  filter_in_channel=#executives` runs [6]
- `SAFE  filter_date_after=2025-09-01` runs [6]
- `docusign  filter_date_after=2025-09-01` runs [6]
- `counts  filter_date_after=2025-09-01` runs [6]
- `Transcend  filter_date_after=2025-09-01` runs [6]
- `Acterra  filter_date_after=2025-09-01` runs [6]
- `Kevin  filter_date_after=2025-09-01` runs [6]
- `angel  filter_date_after=2025-09-01` runs [6]
- `testflight  filter_date_after=2025-09-01` runs [6]
- `internal test  filter_date_after=2025-09-01` runs [6]
- `VC  filter_date_after=2025-09-02 filter_in_channel=#executives` runs [6]
- `pass  filter_date_after=2025-09-02` runs [6]
- `homa  filter_date_after=2025-09-14` runs [6]
- `Karthic  filter_date_after=2025-09-14` runs [6]
- `ncsoft  filter_date_after=2025-09-20` runs [6]
- `Brightwater` runs [6]
- `GFR  filter_date_after=2025-09-20` runs [6]
- `Triptyq` runs [6]
- `Harlem` runs [6]
- `Turkven` runs [6]
- `Makers  filter_date_after=2025-09-09` runs [6]
- `Raine  filter_date_after=2025-09-09` runs [6]
- `bitkraft  filter_date_after=2025-09-23` runs [6]
