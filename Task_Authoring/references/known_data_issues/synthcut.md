# SynthCut Known Inconsistencies (SC-1 – SC-73)

Compiled from 73 inconsistency cards. Each entry lists what not to grade on, why the data conflicts, and (where given) a safer alternative. Cards marked `watch` are not always a fail — check both sides before relying on them.

Sorted by number of FAILs caused (descending), as shown in the source cards.

---

### SC-4 · adjoe payments: ledger vs bank wires
**Caused 36 FAILs**
- **Don't grade:** adjoe payment amounts or dates from FINANCE_LEDGER.
- **Why:** The ledger books 10,733.60 / 20,537.92 / 14,930.02 on Apr 30 / May 31 / Jun 30, but SVB wires paid 12,005 / 18,890 / 15,306.50 on May 5 / Jul 3 / Aug 29 (the ledger comment even claims "signed cash movements").
- **Safer:** Only the 3-month total is safe (both about $46,201.50).

### SC-5 · Victor Barnes paid after he left
**Caused 26 FAILs**
- **Don't grade:** Sep 2025 payroll, headcount, burn or runway from FINANCE_LEDGER or PAYROLL_ROSTER.
- **Why:** FINANCE_LEDGER/PAYROLL_ROSTER pay Victor Barnes through Sep 2025, but Slack says he left April 16, 2025.

### SC-6 · Node CEO emails from an HG address
**Caused 21 FAILs**
- **Don't grade:** Who sent a Node Media email.
- **Why:** Node's CEO "Brian Cooper" sends from brian.foster@harmonygames.co, but that address belongs to HG engineer Brian Foster.
- **Safer:** Refer to "Node's CEO" by role.

### SC-1 · Domino Delights September 2025 installs
**Caused 19 FAILs**
- **Don't grade:** Domino Delights installs in September 2025.
- **Why:** adjoe Slack (Sep 1-8) says adjoe drove an install spike, but INSTALL_EVENTS/DAU have zero DD installs in September.
- **Safer:** Use Zombie Match 3D September installs, or DD before June.

### SC-2 · CASH_BALANCE burn column comment
**Caused 19 FAILs**
- **Don't grade:** The CASH_BALANCE.monthly_net_burn column comment.
- **Why:** The comment says the UA row omits $46,201.50 and leaves a ~$47K residual, but MONTHLY_BURN/FINANCE_LEDGER already hold the adjoe money and reconcile to within $0.49.
- **Safer:** Use the table rows, never the comment.

### SC-7 · People who left channels still listed
**Caused 18 FAILs**
- **Don't grade:** Channel membership (who is in a channel).
- **Why:** #adjoe logs Frederick leaving on 2024-10-31, but he keeps posting there through Sep 2025 and channels.json still lists him (all leavers stay listed).
- **Watch:** Not always failed — check both sides before relying on it.

### SC-8 · ZOM-475 glass crash: fixed or not
**Caused 17 FAILs**
- **Don't grade:** Whether the ZOM-475 glass crash is fixed.
- **Why:** The ZM3D GDD (Sep 30) says it was fixed by removing the glass FX, but Linear ZOM-475 is still Todo, Trello still lists it, and PR #435 re-added glass FX.

### SC-9 · Play Ventures: rejected or no reply
**Caused 17 FAILs**
- **Don't grade:** Play Ventures' status in the investor sheet or Slack.
- **Why:** The investor sheet says "Rejected" with a decline quote (Sep 15), but Leonard says on Sep 23/25 they "didn't respond."

### SC-10 · LVP meeting date: Sep 7 vs Sep 9
**Caused 16 FAILs**
- **Don't grade:** The LVP meeting date in the investor sheet.
- **Why:** The investor sheet says "Catch up on 09/07" (a Sunday), but calendar, invite and Slack say Tue Sep 9.
- **Safer:** If a date is needed, accept Sep 9.

### SC-11 · Unity spend is $0 in Snowflake
**Caused 14 FAILs**
- **Don't grade:** Unity spend, CPI or total UA spend from Snowflake.
- **Why:** Every unity_ads row has spend 0 and CPI 0, but Slack shows paid Unity campaigns ($5-6 bids, $300/day caps); Confluence admits the data feed misses Unity spend.
- **Safer:** Use install counts, not spend.

### SC-12 · Meta spend missing from Snowflake
**Caused 14 FAILs**
- **Don't grade:** Meta/Facebook spend or ZM3D paid UA spend.
- **Why:** Snowflake has no Meta rows after Apr 10, 2025 and none ever for ZM3D, but Gmail Meta receipts bill ZM_UK campaigns ($900 in July) and Slack cites FB spend in September.

### SC-13 · ZM3D beta date in Trello list name
**Caused 13 FAILs**
- **Don't grade:** The ZM3D beta date from the Trello list name.
- **Why:** The list is named "BETA: Oct 10", but its last rename action (Sep 12) and every later action say "BETA: Sep 30."
- **Safer:** Settle the date in your own task data.

### SC-14 · Beta cards' two 'complete' flags disagree
**Caused 12 FAILs**
- **Don't grade:** Which Trello beta cards are 'complete' (cards 54/56/58/67).
- **Why:** The Trello card's dueComplete is false, but its badges.dueComplete is true.

### SC-15 · ZOM-521 checklist ticked, children still open
**Caused 11 FAILs**
- **Don't grade:** What is left on the ZOM-521 VFX master ticket.
- **Why:** The ZOM-521 checklist ticks all six items, but children ZOM-526 and ZOM-528 are still In Progress.
- **Safer:** Use the child ticket states.

### SC-16 · Linear tickets still open after work shipped
**Caused 11 FAILs**
- **Don't grade:** Linear status as proof of whether work shipped (ZOM-564, ZOM-513/514, ZOM-563, ART-790/792).
- **Why:** These tickets are still Todo/In Progress, but their PRs merged or the fix was confirmed in DMs/Slack.

### SC-17 · Ad-revenue payouts per network don't match
**Caused 11 FAILs**
- **Don't grade:** Ad-revenue payouts per network.
- **Why:** AD_REVENUE marks AppLovin/Meta revenue 'paid' (and the ledger books it all as 'AppLovin/MAX'), but Tipalti payout mails and the Meta statement show different amounts.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-18 · PR #477: open or closed
**Caused 10 FAILs**
- **Don't grade:** PR #477's state.
- **Why:** GitHub says #477 is open, but its CodeRabbit comment says "The pull request is closed" and cites commits not in the export.

### SC-19 · Telemetry app versions vs Slack builds
**Caused 10 FAILs**
- **Don't grade:** Matching RAW_EVENTS app versions to a store build in Slack.
- **Why:** RAW_EVENTS uses 0.1.534/0.1.601, but Slack releases are 0.3.x (and also called 1.3.x).
- **Safer:** Match by date: 0.1.601 starts Sep 30 00:47 UTC.

### SC-20 · Node Slack channel creation date
**Caused 10 FAILs**
- **Don't grade:** When the Node Slack channel started.
- **Why:** channels.json says it was created 2025-04-09, but its messages start Sep 2024.
- **Safer:** Date the relationship from messages/email.

### SC-21 · Jan 2025 Node wire missing from ledger
**Caused 9 FAILs**
- **Don't grade:** Cash or burn totals that must include the Jan 2025 Node payment.
- **Why:** SVB confirms a $16,428.57 wire to Node on Jan 2, 2025, but no FINANCE_LEDGER row can hold it and CASH_BALANCE ties to the ledger.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-22 · time_in_status_minutes runs past the clock
**Caused 8 FAILs**
- **Don't grade:** Ticket durations from Linear's time_in_status_minutes.
- **Why:** The field runs to 2026-02-13, but the clock is Oct 1, 2025.
- **Safer:** Compute from created_at/completed_at.

### SC-23 · AppLovin spend dates and countries
**Caused 8 FAILs**
- **Don't grade:** AppLovin spend, geos or campaign dates from Snowflake.
- **Why:** Snowflake books DD AppLovin spend from Apr 11, 2025, multi-country, incl. paused days, but Slack says the US-only campaign first went live Jun 23.

### SC-24 · Tim Steudler works for Mattel, not HG
**Caused 8 FAILs**
- **Don't grade:** Tim Steudler's employer (he has an HG email and HG accounts).
- **Why:** He writes from tim.steudler@harmonygames.co and has HG accounts, but he is Mattel's BD manager.
- **Safer:** Call him 'Mattel's contact'; don't count him as staff.

### SC-25 · PAYROLL_ROSTER vs who actually works there
**Caused 8 FAILs**
- **Don't grade:** Who is on payroll or current staff from PAYROLL_ROSTER.
- **Why:** The roster pays Felix in Sep 2025 and lists Calvin as 'General Counsel' for April only, but Slack shows Felix left Aug 2024 and Calvin is the active VFX engineer (also Samuel off-roster).
- **Watch:** Not always failed — check both sides before relying on it.

### SC-3 · Runway: investor letter vs CASH_BALANCE
**Caused 7 FAILs**
- **Don't grade:** A runway figure from the investor letter or CASH_BALANCE.
- **Why:** The Oct 1 investor letter says ~4 months, but CASH_BALANCE says 2.7 months (Sep 30).

### SC-26 · Slack links to ENG-2367/2368/2373 don't exist
**Caused 7 FAILs**
- **Don't grade:** Resolving Slack's ENG-2367/2368/2373 links.
- **Why:** Slack links ENG-2368 etc., but Linear stops at ENG-2366; those tickets are ZOM-436/521/527.
- **Safer:** Use the ZOM ids; never inject new ENG-2367+ issues.

### SC-27 · #god-bugs and #god-gameart archive state
**Caused 7 FAILs**
- **Don't grade:** Posting in #god-bugs or #god-gameart.
- **Why:** Each has an 'archived the channel' event (Jul 15), but channels.json says is_archived false.
- **Safer:** Put deciding messages elsewhere.

### SC-28 · Product OKRs page numbers vs Snowflake
**Caused 6 FAILs**
- **Don't grade:** The Confluence Product OKRs numbers.
- **Why:** It says D1 27.9% on 408 Aug UK iOS installs, a US-only launch and Facebook volume, but Snowflake has 711 installs at ~35.7% D1, a multi-country launch and no ZM3D Meta rows.

### SC-29 · MMP report times before the install
**Caused 5 FAILs**
- **Don't grade:** MMP reporting latency from INSTALL_ATTRIBUTION.
- **Why:** INSTALL_ATTRIBUTION has mmp_reported_at earlier than install_ts on 12,730 of 28,609 rows, so the MMP reports installs before they happen.

### SC-30 · Done parent tickets with open children
**Caused 4 FAILs**
- **Don't grade:** A parent ticket's status implying its children's.
- **Why:** Parents like ENG-2072 / ZOM-457 are Done, but their children are still open.
- **Safer:** Grade each child on its own state.

### SC-31 · Live-ops weekend outage dates and events
**Caused 4 FAILs**
- **Don't grade:** The live-ops weekend outage end date or affected events.
- **Why:** Confluence pages say "no recorded end", River Rush missed weekends, Streak Fever shipped April, but LIVE_EVENT_PERFORMANCE shows recovery by ~Jul 25, River Rush Mon/Wed/Fri only, Streak Fever runs from Mar 1.
- **Safer:** Measure only from the degraded rows in LIVE_EVENT_PERFORMANCE.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-32 · 'In Review' tickets with completion dates
**Caused 4 FAILs**
- **Don't grade:** 'In Review' tickets as open or done.
- **Why:** Their state is In Review, but all 12 carry completed_at.

### SC-33 · Investor sheet lists Acterra twice
**Caused 4 FAILs**
- **Don't grade:** Counts of firms in the investor sheet.
- **Why:** Acterra is listed twice (No. 71 and 86), but it is one firm (also Treo vs Treeo spelling).
- **Watch:** Not always failed — check both sides before relying on it.

### SC-34 · Investor sheet row 82: Superplay vs Supercell
**Caused 4 FAILs**
- **Don't grade:** Investor sheet row No. 82.
- **Why:** The row is labeled 'Superplay', but its contents are Leonard's Supercell outreach.

### SC-35 · P&L workbook month headers mislabeled
**Caused 4 FAILs**
- **Don't grade:** Month columns in the P&L workbooks.
- **Why:** Salary/Costs tab headers carry wrong years (2025 columns read 2024), but the Cash P&L tab labels the same columns correctly; Gross Margin and Ending Balance formulas are also broken.
- **Safer:** Pick columns by position or the Cash P&L tab.

### SC-36 · Victor Barnes still on invites and channels
**Caused 4 FAILs**
- **Don't grade:** Invite/share lists built from channel or calendar membership.
- **Why:** Victor Barnes is still in #god-gameart, recurring invites and owns EPI-4, but he left in April 2025.

### SC-37 · Crash-by-level comment vs the rows
**Caused 4 FAILs**
- **Don't grade:** A ZM3D crash-by-level split.
- **Why:** The CLIENT_ERROR_EVENTS comment says ~82% of crashes are at levels 3-5, but the rows put ~11% there.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-38 · Season Pass ship date and analytics
**Caused 3 FAILs**
- **Don't grade:** Season Pass ship date or analytics status.
- **Why:** The spec says production Sep 22-29 and events are tagged, but PR #438 shipped in builds before that window and ZOM-552 analytics is still In Progress.
- **Safer:** Avoid ZOM-529 (it only exists in injected SQL).
- **Watch:** Not always failed — check both sides before relying on it.

### SC-39 · Singular plan: quarterly or two installments
**Caused 3 FAILs**
- **Don't grade:** The Singular payment plan from the Aug 28 exec sync.
- **Why:** The Aug 28 exec sync says 2 x $12.5K, but Singular's email, Slack and the Sep 26 $6,250 wire say quarterly.

### SC-40 · July board meeting date: 14 vs 16
**Caused 3 FAILs**
- **Don't grade:** The July 2025 board meeting date from the email body.
- **Why:** The body says 'July 14, Wednesday', but subject and calendar say Wednesday July 16.
- **Safer:** Accept July 16.

### SC-41 · ENG-2366 cited before it existed
**Caused 3 FAILs**
- **Don't grade:** When ENG-2366 was documented.
- **Why:** The Release Checklist (Jul 26 08:50Z) cites ENG-2366, but ENG-2366 was created 13 hours later.
- **Safer:** Its content is fine to use.

### SC-42 · Node kickoff date: Sept 22 vs 23
**Caused 3 FAILs**
- **Don't grade:** The Node kickoff date.
- **Why:** Node's invoice note says the kickoff was Sept 22 (a Sunday), but the calendar has it Mon Sept 23, 2024.
- **Safer:** Use the invoiced $1,428.57 as stated.

### SC-43 · Simon's Aug-Sep 2024 pay
**Caused 3 FAILs**
- **Don't grade:** What Simon was owed/paid for Aug-Sep 2024.
- **Why:** The P&L shows $0, but Slack shows 10 August hours entered in Deel; Simon has no PAYROLL_ROSTER row.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-44 · Tutorial step events listed but empty
**Caused 3 FAILs**
- **Don't grade:** A tutorial funnel from Snowflake.
- **Why:** The SESSION_LEVEL_EVENTS comment lists tutorial_step events, but there are 0 such rows.

### SC-45 · Confluence backend pages vs the code
**Caused 3 FAILs**
- **Don't grade:** Backend deploy/migration/health-check details from Confluence.
- **Why:** The pages say migrations don't run on boot, /healthz, check.yml existed in March, but the repos run migrations on boot, use /health, and check.yml came later.
- **Safer:** Read the code instead.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-46 · HEADCOUNT comment says 12, rows say 15
**Caused 3 FAILs**
- **Don't grade:** Total people at Sep 2025 from the HEADCOUNT table comment.
- **Why:** The HEADCOUNT comment says ALL PEOPLE is 12, but 15 rows are active (12 + 3 founders).

### SC-47 · Weekly Quests status and incident timeline
**Caused 3 FAILs**
- **Don't grade:** Weekly Quests status or the Nov 2024 quest incident timeline.
- **Why:** The live-ops calendar still says 'Failed Nov 2024' and the postmortem dates the fix Nov 18, but the playbook says fixed, Slack shows the fix on Nov 15, and code types differ.

### SC-48 · 'Pitch Sep 25' deck date
**Caused 3 FAILs**
- **Don't grade:** The date of the 'Pitch Sep 25' deck.
- **Why:** Drive says it was created 2025-07-29, but it contains the $2.5M ask and AUG 25 metrics from late August.
- **Safer:** Date the ask from the Aug 28 sync.

### SC-49 · Founder count and Frederick's role
**Caused 2 FAILs**
- **Don't grade:** Founder counts or Frederick's founder status.
- **Why:** The persona roster lists 4 co-founders incl. Frederick, but Snowflake has 3 founders and books Frederick as non-founder 'Commercial Lead'.

### SC-50 · Bot comment authors: Organization vs Bot
**Caused 2 FAILs**
- **Don't grade:** Which GitHub account posted a bot comment.
- **Why:** Comments are by 'Organization' users, but matching timeline events are by separate 'Bot' users.
- **Safer:** Refer to 'CodeRabbit' by content.

### SC-51 · Node Google Ads link: linked or pending
**Caused 2 FAILs**
- **Don't grade:** The Node Google Ads link status.
- **Why:** An 08:04 email says the account "is now linked", but an 08:06 email says the link request is "pending".

### SC-52 · Backend PR #79 open but already merged
**Caused 2 FAILs**
- **Don't grade:** Whether game-of-dominoes-backend PR #79 shipped.
- **Why:** The PR is open and unmerged, but its head commit is already main's head.

### SC-53 · One player token used for two players
**Caused 2 FAILs**
- **Don't grade:** Player identity or counts from [IDENTIFIER_9782].
- **Why:** #live-incidents uses the token for 'another player', but it is the same token as the earlier player, so the hidden names merged two people.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-54 · Frederick paid after his last paycheck
**Caused 2 FAILs**
- **Don't grade:** Frederick's pay after May 2025 in the ledger.
- **Why:** Leonard says May 2025 is his last paycheck (then $1), but the ledger pays him $3.3-3.9K a month through Sep.

### SC-55 · Mattel RFP deadline: November 31
**Caused 2 FAILs**
- **Don't grade:** An exact deadline from the Mattel RFP.
- **Why:** The RFP says 'November 31, 2025', but that date doesn't exist.
- **Safer:** Accept 'end of November 2025'.

### SC-56 · Commit title case: GitHub vs #builds
**Caused 2 FAILs**
- **Don't grade:** Exact-case commit title matches between GitHub and #builds.
- **Why:** #builds shows titles in one case, but GitHub has different case/apostrophes (~478 lines).
- **Safer:** Match by SHA/PR number.

### SC-57 · #zm-collect-win archived but still active
**Caused 1 FAIL**
- **Don't grade:** Posting in #zm-collect-win.
- **Why:** channels.json says it is archived, but there is no archive event and people posted until Sep 30.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-58 · ZM3D monster roster and boss rules
**Caused 1 FAIL**
- **Don't grade:** The ZM3D monster roster or boss rules.
- **Why:** The Confluence GDD has the old roster (Punk, etc.) and a tray-fill boss end, but Robert's July Slack roster and the Docs boss GDD differ.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-59 · Country of early adjoe installs
**Caused 1 FAIL**
- **Don't grade:** The country of early adjoe installs (Apr 11-16).
- **Why:** Slack says they came almost all from Canada, but Snowflake codes every adjoe install US.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-60 · Josh Dempsey identity mix-up
**Caused 1 FAIL**
- **Don't grade:** 'Josh Dempsey' as a person to DM/assign.
- **Why:** Named Josh Dempsey accounts are idle, but the work sits under EMPLOYEE_0032 (and Gmail's Josh is Solsten's sales director).
- **Safer:** Use EMPLOYEE_0032.

### SC-61 · ENG-2255 owner: Brian or Samuel
**Caused 1 FAIL**
- **Don't grade:** Who owns Linear ENG-2255.
- **Why:** Linear says Brian, but Brian says he assigned it to Samuel, and the unfurl shows Samuel.

### SC-62 · Reward import: hourly or every 5 minutes
**Caused 1 FAIL**
- **Don't grade:** The reward-import cadence.
- **Why:** The live-ops calendar says hourly in prod, but the CDK stack and Douglas's Sep 8 DM say every 5 minutes.

### SC-63 · Griffin pro-rata range math
**Caused 1 FAIL**
- **Don't grade:** A Griffin pro-rata dollar figure from the Aug 28 sync.
- **Why:** The Aug 28 sync says ~$545K-$1.2M, but that range fits a $2M raise, not the $2.5M ask in the same note.

### SC-64 · Node Media's two addresses
**Caused 1 FAIL**
- **Don't grade:** Node Media's address on its invoices.
- **Why:** Invoice 1158 says La Jolla, CA, but invoice 1168 says Miami, FL.

### SC-65 · ZM average playtime: 18 vs 37 min
**Caused 1 FAIL**
- **Don't grade:** ZM average playtime.
- **Why:** Leonard says ~18 min (30 with Variant C), but PLAYER_DAILY_PROGRESS means are 37-40 min (only the median is ~17).
- **Safer:** Define the measure and accept either.

### SC-66 · Closed analytics AWS account still active
**Caused 1 FAIL**
- **Don't grade:** Whether the analytics AWS account is live.
- **Why:** AWS mails say it was permanently closed (Aug 21), but Lambda notices keep arriving and Confluence/config still treat it as live.

### SC-67 · Build #1621 post lists #1620
**Caused no FAILs yet**
- **Don't grade:** Which build contained PR #439, from the #builds post.
- **Why:** The #builds post is headed #1621, but its change list says #1620.

### SC-68 · Boss Arena on prod before its code
**Caused no FAILs yet**
- **Don't grade:** When Boss Arena reached prod.
- **Why:** Douglas's Aug 25 self-DM runs BossArena on prod, but the first BossArena commit is Sep 1.

### SC-69 · April 2025 BigQuery cost: 123.47 vs 126
**Caused no FAILs yet**
- **Don't grade:** The exact April 2025 BigQuery cost.
- **Why:** The receipt says $123.47, but the July P&L says 126.
- **Safer:** Use the receipt.
- **Watch:** Not always failed — check both sides before relying on it.

### SC-70 · Slack timezones all Los Angeles
**Caused no FAILs yet**
- **Don't grade:** A person's timezone from Slack.
- **Why:** Slack lists everyone as America/Los_Angeles, but calendars show real zones (Istanbul, El Salvador, UTC+3...).
- **Safer:** Use the calendar zone, non-decisively.

### SC-71 · ZOM-471 priority: high vs Medium
**Caused no FAILs yet**
- **Don't grade:** ZOM-471's priority from the Linear-bot post.
- **Why:** The Linear-bot post says 'high priority', but Linear says Medium (never updated).
- **Watch:** Not always failed — check both sides before relying on it.

### SC-72 · Python 3.9 end-of-life date in the future
**Caused no FAILs yet**
- **Don't grade:** The Python 3.9 EOL as already passed.
- **Why:** AWS notices say EOL was 'reached on October 30, 2025', but that is after the Oct 1 clock.
- **Safer:** Use the Lambda deprecation dates.

### SC-73 · Monthly burn in pitch text
**Caused no FAILs yet**
- **Don't grade:** A monthly burn figure from pitch text.
- **Why:** Leonard's pitches say ~$100K/month, but he also says $55K and CASH_BALANCE says ~$58K.
