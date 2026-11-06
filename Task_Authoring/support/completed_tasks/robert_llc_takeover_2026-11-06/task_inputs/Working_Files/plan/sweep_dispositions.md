# Blind sweep dispositions (injection rev1)

Two fresh agents reviewed the seeded records before sealing. The fork sweep saw only Robert-visible records and no answer key. The coherence sweep checked every seeded claim against the full base through hg.py. Each finding was re-checked through hg.py before any change. The reports themselves are in the session scratchpad, not in this folder.

## Fork sweep (37 forks: 3 SETTLED, 14 WEAK, 20 OPEN or mixed)

The sweep reproduced the solver's answer independently: $3,450 a month, $1,150 each, and $902 cash for Arthur. DD comes over, ZM stays, and the campaign is a 38th row.

| # | Fork | Disposition | Record that settles it |
|---|------|-------------|------------------------|
| 1 | DD hosting: $140 vs ~$1k/$300 | designed (CORR), WEAK by intent | Arthur's DM reply D04V95AAAHW/1770952200.665739 is later and is the runner's; the costing rule names "whoever runs it". It now also says "it's still on HG's AWS bill till then". |
| 2 | What counts as DD's own hosting (prod only, prod plus dev and analytics, or January's hosting) | fixed | The ground rules now say "covers what its own hosting bills now". Arthur's notes on ENG-2442 and ENG-2444 shut dev and analytics down. |
| 3 | Which revenue table / aggregation | settled | REVENUE_DAILY and REVENUE_DAILY_V2 agree; the grain comment says to sum. A computation trap (AUTH), not a fork. |
| 4 | ZM decision; the displayed ZM figure | settled; display open but ungraded | $0.00 income; ZM is HG under any figure. Nothing grades the ZM account amount. |
| 5 | Campaign in scope | designed (FILT), WEAK by intent | Leonard's status C09UHHN6PFZ/1770938400.370665 says "it moves to the LLC from March". The hub asks for "what it costs us March through May". |
| 6 | Campaign $3,000 flat vs $100/day × days | fixed | The status now says "$100/day capped at $3,000 a month". |
| 7 | Campaign payer: LLC vs Leonard's card toward his third | fixed | "on my card till the end of Feb. it moves to the LLC from March". The ground rules add "Services we keep running just move their billing to the LLC". |
| 8 | Are founder-carried items inside "what the LLC costs" | fixed | The split mail now says "that's everything on the plan that bills monthly, including what one of us already pays for it". |
| 9 | GitHub: Founder vs HG | fixed | Arthur's mail adds "the github org itself stays HG's till the data's delivered, I'm just paying the bill". He carries the bill, so the row is Founder, and the transfer waits for the data sale (C5). |
| 10 | Metabase/dbt amounts and state | designed (COMPLETE), WEAK by intent | Arthur's later mail; the costing rule. |
| 11 | CF backend stacks: LLC vs Founder ("I keep an eye on them") | fixed | The note now says "about $62 a month on HG's AWS bill". The billing moves to the LLC. |
| 12 | DD support: done or not; LLC vs HG | designed (DONE); state fixed | The App Store notice decides "not done". The ground rules now say "A game that comes over brings what it needs to keep running, its accounts and its player support", so the item is LLC. Jenkins #218 ties the rejection to the change. |
| 13 | ZM's half of the Helpshift move | accepted, ungraded | ZM stays with HG. No slot grades ZM's support step. |
| 14 | Build machines: LLC takes them if unsold vs HG | fixed | Arthur's note on ENG-2446 (he runs Jenkins): "the build boxes are HG's, they go with the laptops in Sunset's sale. I'll move CF's jenkins job to my own machine before then". |
| 15 | Date for "when the sale closes" | accepted, ungraded | The Trello card sets the form. No slot grades a CF or DD date. Rubric: accept "when the sale closes" or a date tied to it. |
| 16 | DD owner: Arthur vs Leonard | fixed | Leonard's ENG-2439 note: "I'll handle it with Sunset". Owner Leonard (ungraded). |
| 17 | BoomBit test "still running" vs stopped Feb 13 | fixed | The DD note no longer states the test's status: "boombit's test doesn't change anything, the game is ours". |
| 18 | DD's Google Play security fix (Feb 26), not a Linear issue | accepted, out of scope | The plan covers items that bill or move. A security fix is neither, and no slot grades it. Rubric: do not penalise a mention. |
| 19 | Calm Play: HG vs the founders' vehicle | designed (EXC), WEAK by intent | C04UEQVDVB7/1701383740.580749 and C04UEQVDVB7/1703492127.063049 (subsidiary). The ground rules: "The LLC is the new one Blake and I are setting up for the three of us". Leonard's Dec 2025 idea (C07C2866011/1764796030.482829) was a suggestion that went nowhere; no Jan–Feb 2026 record mentions Calm Play. |
| 20 | Figma: draft row LLC vs note HG | designed (stale draft), WEAK | Leonard's later note on ENG-2453. |
| 21 | Format: how literally to copy the draft; where the shares go | accepted | The hub asks for the layout. The split mail: "put the three shares on the sheet per month". Rubric: any placement on the sheet. |
| 22 | AppsFlyer now vs contingent | fixed | Leonard's ENG-2451 note: "singular is getting terminated, so CF goes on appsflyer's free tier from March". |
| 23 | Singular | settled | — |
| 24 | Unity licence for the LLC | fixed | Arthur's ENG-2459 note: "CF is fine on unity personal". |
| 25 | The LLC's own Apple/Google developer accounts | fixed | The ground rules: "only what bills us every month, no one-offs or yearly fees". |
| 26 | layer.ai next step | fixed | Leonard's note: "CF's character art only lives in there, it has to be pulled out before the access ends". The date stays in C09UHHN6PFZ/1770837702.167889 (DATE). |
| 27 | Kapwing | settled | — |
| 28 | Items that stay with HG | settled | — |
| 29 | Playable vendor / Unity Ads balance | fixed | The ground rules exclude one-offs. |
| 30 | Analytics pipeline | settled | Arthur's note; CF's events go through Firebase (C07C2866011/1770298939.402129). |
| 31 | Firebase/BigQuery billing | fixed | Arthur's mail: "bigquery and firebase stay on HG's google account with GA until the data's out". |
| 32 | Auction price for the games | fixed | "no one-offs" (the ground rules). |
| 33 | AWS credits | accepted | The costing rule uses "what it bills now"; Arthur's $140 is the bill. |
| 34 | DD prod payer: LLC vs Arthur | fixed | Arthur's DM adds "it's still on HG's AWS bill till then", and the ground rules move service billing to the LLC. |
| 35 | Pay excluded | settled | — |
| 36 | Third vs cash in the reply | accepted | R2 ($902) and R3 ($1,150) grade both figures. |
| 37 | Which Wednesday call | settled | Both posts agree. |

Base vs seed points the sweep raised:
- BoomBit status: fixed (#17).
- The "Blake and I" vs thirds side note on the LLC: fixed ("for the three of us").
- PR #1917 "merged=null": a dump artefact. The SQL row has `merged` = true and merged_at = closed_at = 21:10Z. The base `arthur.blake/boombitWithEcon` branch is DD's iOS-submission branch (C05433XK267 2026-01 /1236–/1238). DD Android moved to `Blake/boombitFixAddressables` on Feb 11 (C05433XK267 2026-02 /200–/210), which has no GitHub branch row, so the PR targets the iOS branch. No branch is graded (NB-13).

## Coherence sweep (5 major, 8 minor, 0 blocker)

| # | Finding | Disposition | Evidence and change |
|---|---------|-------------|---------------------|
| 1 | Arthur's $48 GitHub figure vs the Feb 3 receipt ($52 Team Plan + $38 Copilot); "from this cycle" vs bills already paid | fixed | Verified: threads/blake@harmonygames.co_1856132203079406675.json (Team Plan $52.00, Copilot $38.00, total $90.00). The mail now reads "github is back to the $48 team plan now that I dropped the extra seat and copilot is off" and "from the next bill". The Jan 3 receipt shows $48 before the seat was added. $248 is unchanged. |
| 2 | Leonard's status: "only … still on" ignores the Unity playable campaign; "VO" is event optimization, not video; $100/day is the budget while Meta bills a few dollars; "on my card" | fixed | Verified the Unity playable campaign: C09UHHN6PFZ/1770845845.148039 and C09UHHN6PFZ/1770846133.630899, still pending on Feb 13 (C07C2866011/1770952950.369459). VO = value/event optimization (C09UHHN6PFZ/1770404397.819789; C07C2866011/1770438169.228649). The status now names only the Meta campaigns, says the Unity test uses up the $100 left there, and says Meta barely bills the VO one while it learns but that it runs at $100/day capped at $3,000 a month from March. "On my card till the end of Feb" matches Leonard's card paying HG tools ("I canceled other subscriptions under mine", C0ADGSZKR3R/1770933601.686309). From March the line is the LLC's, so the split rule's "already pays personally" does not apply in the window. "VO" is used everywhere, including the cohort key "Combo Fighter VO campaign". |
| 3 | The deck predates the campaign and uses "video"; "no new playables" vs Robert's playable push | fixed | The deck is now dated 2026-02-08T03:00Z, after the creation (Feb 6) and Leonard's "keep both campaigns live" (Feb 7). It reads "Run the VO campaign at $100/day (~$3k a month) through May" and "No playables beyond the one in production until D1 is over 35%". |
| 4 | The ground rules cite the card, and the card cites the project, each before it exists | fixed | Project 23:24Z, issues 23:25–23:37Z, card 23:42Z (its id is minted from that time), ground rules 23:46Z, all Feb 12. |
| 5a | The Fargate line is not ZM-only | fixed | Arthur's ENG-2443 note: "ZM's account still runs phoenix, its nakama and the aurora cluster at full size, well over $1k a month". It no longer cites the guide's line. |
| 5b/c | The CF client calls ZM's Phoenix API (page_aws_infra sibling /pages/8); CF has a Nakama stack (D04UY3DQJE5 2026-01) | fixed | Verified both. Arthur's ENG-2445 note: "Combo Fighter's own account (auth, nakama and backend stacks) runs about $62 a month on HG's AWS bill. CF stopped calling ZM's phoenix api, it doesn't need ZM's account". |
| 6 | Slack "going to the free plan" vs three paid members | fixed | C0ADGSZKR3R/1770842395.641349 ("per paid account we can do 5 people") and C0ADGSZKR3R/1770842402.772039. The note now says "down to the three of us as paid members, everyone else is a single channel guest". |
| 7 | The $140 reply sits under an unrelated root | designed (CORR placement) | It is intentional (A14 thread hiding) and the root counters are updated. Disposition recorded. |
| 8 | The App Review mail is only in Robert's box | fixed | Copies were added to Arthur's and Leonard's mailboxes with the same Message-ID (companions). |
| 9 | Arthur's invitation is in PST | fixed | It is now in EST with his display name, like blake@harmonygames.co_1856867715191204796.json. Robert's copy is in PST with his name token, like robert threads/00016854.json. |
| 10 | PR refs `arthur.blake/…`; merge sha missing from commits | fixed | The PR refs are now `Blake/supportEmail` → `Blake/boombitWithEcon`, as in base PRs (/pull_requests/1040). The branches-table row stays `arthur.blake/supportEmail` (NB-13 split). A merge commit row was added in the base merge shape (commits/4580). The branch head is not advanced (R05: base heads are pre-rewrite SHAs). |
| 11 | The notes doc comes 13 minutes after "not worth keeping the lights up" | fixed | The notes doc is now 2026-02-09T23:55Z, after Arthur's ~$1k (23:49Z) and before "easy to get to 300" (00:10Z) and Leonard's lights line (01:16Z). |
| 12 | "needs a payer" after Leonard's 👍 to Arthur's move | fixed | The ENG-2447 note now reads "about $300 a month with dbt, that's what we've been paying". |
| 13 | The hub opens "ok," with nothing to answer | fixed | The hub now opens "if you really want to keep combo fighter going". |

Snowflake note confirmed: REVENUE_DAILY and REVENUE_DAILY_V2 give January DD $183.11, ZM $0.00 and CF $7.36.

## Coherence re-check on rev2 (same reviewer; 9 of 10 fix groups hold; 1 new major, 4 minor, 1 nit)

| # | Finding | Disposition | Evidence and change |
|---|---------|-------------|---------------------|
| R1 | ZM "well over $1k a month" cannot fit HG's whole AWS line | fixed | Verified: snowflake FINANCE.EXPENSES.MONTHLY_BURN aws_hosting is $1,485 for 2026-01 and $1,485 for 2026-02, which already covers DD prod (~$1k), analytics (~$300) and CF ($62). ENG-2443 now reads "ZM's account still runs phoenix, its nakama and the aurora cluster, nobody trimmed it. it bills every month on HG's AWS bill", with no figure. ZM still fails the take test because any bill exceeds its $0.00 January income. The solver uses "bill > 0". |
| R2 | Arthur's and Leonard's App Review copies greet Robert's token and carry Robert's labels | fixed | They now greet "Hello Arthur," and "Hello Leonard," with each box's base labels (blake@harmonygames.co_1838693712455374094.json; leonard@harmonygames.co_1838693748302395744.json). |
| R3 | "that's what we've been paying" turns ~$300 into a billed figure (receipts $226–$248) | fixed | ENG-2447 now reads "about $300 a month with dbt, more or less", Leonard's own words from C0ADGSZKR3R/1770933903.645709. It stays a superseded estimate (T4). |
| R4 | "CF's character art only lives in there" overstates it | fixed | The note now says "CF's character source art only lives in there". |
| R5 | "build boxes are HG's" vs Jenkins at Arthur's place | fixed | The note now says "the build boxes at my place are HG's" (C07C2866011/1770839126.382429; Jenkins at blake.tplinkdns.com). |
| R6 | The project's start_date was Feb 13 but it was created Feb 12 23:24Z | fixed | start_date is now 2026-02-12. |

These supersede the earlier wording quoted in rows 5a, 12, 14 and 26 above.

## Second blind fork sweep on rev2 (fresh agent, no answer key; 50 forks rated)

It reproduced the plan and totals again: $3,450 a month, $1,150 a third, $902 cash from Arthur, DD in and ZM out. Changes made from it:

| # | Fork | Disposition | Change |
|---|------|-------------|--------|
| 42 | The App Review rejection could concern an earlier build: it named no build and spoke of "a support screen" | fixed | The item now reads "The support option in the app only opens an email draft, and on a device without a mail account set up it does nothing … Please add a support URL or another way to contact you in the app". Only the #218 support-email build (Jenkins C05433XK267, 'Replace Helpshift with support email') has an email-draft support option. |
| 3 | DD's Jenkins jobs also run on the build boxes going into the sale | fixed | ENG-2446 (Arthur): "I'll move our jenkins jobs to my own machine before then". |
| 21 | GitHub Done vs Canceled (the org stays HG's, Arthur pays) | fixed | Arthur's mail: "I'm just paying the bill, so count it as mine like the other two". |
| 2 | Firebase/BigQuery after the data is out (the P&L shows ~$26) | fixed | Arthur's mail: "bigquery and firebase stay on HG's google account with GA until the data's out, then CF's are on the free tier, its volume is tiny". |
| 1 | Is the Meta campaign on the plan? | designed (FILT), now explicit inside the hidden record | Leonard's status adds "so count it in what the LLC costs". The record is still a thread reply outside every list. |
| — | Confluence says CF doesn't use Nakama; ENG-2445 named a nakama stack | fixed | ENG-2445: "its auth and backend stacks". |
| 4, 5, 6, 24, 25, 27–29, 34, 36, 39, 43, 45 | ZM's Helpshift move, DD's support mailbox, where listings land, share vs cash wording, rounding, owners, the sale-close date, the Jenkins date, the Calm Play and layer.ai Linear states | accepted (ungraded) | No surface slot grades an owner, a sale or Jenkins date, a listing destination, a Linear state for these items, or the ZM step. #43 treats Calm Play as not HG's, which is the EXC trap landing (C04UEQVDVB7/1701383740.580749). For the rubric: accept either side of each. |
| 42 (note) | PR "merged=None" | not a defect | The SQL row has `merged` = true. The local parser renders SQL booleans as None, and the platform /injection review read it as merged. |

## Third blind fork sweep on rev3 (fresh agent, no answer key; Linear writes first)

The platform /prompt review of rev2 failed UGT on three Linear writes (run_forensics/rev2/1_prompt_FAIL_r2.md), so this sweep rated each issue's state, each Todo assignee and each new issue before the sheet values. It reproduced the solver: DD in ($183.11 January income in snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY against $140), ZM out ($0.00), $3,450 a month, $1,150 each, Arthur $902 cash, Todo ENG-2438/2439/2441/2445/2451/2462 plus a new VO campaign issue assigned to Leonard, Done ENG-2447/2448/2449, the rest Canceled. The three rev2 platform forks (F1 new VO issue, F2 ENG-2451 assignee, F3 ENG-2452 state) came back settled.

| # | Sweep's OPEN fork | Disposition | Record that settles it |
|---|---|---|---|
| 1 | ENG-2446 build machines: Canceled, or the LLC takes them if Sunset can't sell them | fixed | Arthur's note now ends 'I'll move our jenkins jobs to my own machine before then, so the LLC doesn't need them'; the ground rules put equipment through Sunset's sale (f_1e468a9d69ea0f0a2001f5). |
| 2 | ENG-2472 Calm Play: no Robert-visible owner record | settled (missed by the sweep) | #admin_foundersonly C04UEQVDVB7/1701383740.580749 ('an LLC that's fully owned by Harmony Games', Robert is a member) and the Dec 2023 'make calm play full subsidiary of Harmony Games'; the platform's own sweep cited both. |
| 3 | ENG-2439 DD assignee: Leonard or Arthur (who builds DD) | settled | Leonard's note 'I'll handle it with Sunset'; the card says sale items move when the sale closes (698e6548aa9516b76c4ab475). The platform's sweep settled it the same way. |
| 4 | CF player support: the ground rules say a game brings 'its player support', and there is no CF support issue | fixed | Leonard's Helpshift note (ENG-2461) now adds 'CF was never on it, its support is the contact on its store listing and that moves with the game'. Base check: no Helpshift, Zendesk or 'contact us' for CF in #prototype (hg.py search-many, scan complete). |
| 5 | ENG-2462 due date: before Feb 28 or Mar 1 | settled | Helpshift note 'DD and ZM have to be off it before Feb 28th' and the card's own-deadline rule; any Feb 15–28 date accepted (brief §4b). |
| 6 | ENG-2454 layer.ai: who pulls the art and by when | settled / representational | Base #prototype C09UHHN6PFZ/1770837702.167889 gives access until March 3 (missed by the sweep); the row is Canceled, so no assignee; the sheet's owner on non-LLC rows is representational (brief §4b). |
| 7 | Next step / owner / by on Canceled and Done rows | representational | Brief §4b: any or blank on non-LLC rows; no Linear assignee is written for Canceled or Done. |
| 8 | Share role | representational | The hub says only 'share it with Blake and me'. |
| 9 | A calendar date for CF/DD instead of 'when the sale closes' | settled | The card: 'Anything that comes through Sunset's sale moves when the sale closes.' |

WEAK items (Arthur's $140 under the Feb 2 root, the campaign reply, the Metabase + dbt row split, third vs cash) are designed or already accepted; the platform scored them settled.

## Fourth blind fork sweep on rev4 (fresh agent, no answer key; Linear writes first)

The sweep reproduced the solver independently:
- DD in ($183.11 January income in snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY against $140) and ZM out ($0.00);
- CF's stacks at $62 (Arthur's Jenkins email robert@harmonygames.co/1856982378087295205 over his $95 note on ENG-2445);
- ENG-2462 Todo/Arthur (the App Store notice after Arthur's "done");
- Metabase, dbt and GitHub Done ("even if HG still owns it");
- a new VO campaign issue, Todo/Leonard;
- $3,450 a month, $1,150 each, and Arthur $902 cash.

| # | Sweep's fork | Disposition | Record that settles it |
|---|---|---|---|
| 1 | ENG-2454 layer.ai: Canceled, or Todo with Robert by Mar 3 (OPEN) | fixed | Leonard's reply C09UHHN6PFZ/1770923700.470906 now ends "it goes with CF, the account itself just lapses": the account stays with HG (Canceled), and the art pull is a sheet step owned by Robert by Mar 3 (the project description assigns only Todo issues). |
| 2 | VO campaign: its own row and issue, or folded into CF's cost (WEAK) | fixed | Leonard's status C09UHHN6PFZ/1770938400.370665 now ends "so count it as its own line in what we pay each month"; the project description covers "anything the LLC might ... pay for", and the prompt asks the project to match the sheet. |
| 3 | ENG-2462 By: Feb 28, Mar 1 or Feb 27 (WEAK) | accepted (rubric) | Leonard's Helpshift line C0ADGSZKR3R/1770789534.434749 ("before Feb 28th") plus the card's own-deadline rule; the rubric accepts any date from Feb 15 to Feb 28 (rev3 brief §4b, unchanged). |
| 4 | ENG-2472 Calm Play: Leonard's "could just be our LLC" note was later than the ground rules (WEAK) | fixed | The note is now dated Feb 12 23:41Z, before the ground rules f_1e468a9d69ea0f0a2001f5 (23:46Z), which then name "the new one Blake and I are setting up for the three of us". |
| 5 | ENG-2439 DD assignee: Leonard or Arthur (WEAK) | settled (unchanged from rev3) | Leonard's note "I'll handle it with Sunset" and the card's "Anything that comes through Sunset's sale moves when the sale closes" (698e6548aa9516b76c4ab475); the rev3 platform /prompt sweep settled it the same way. |
| C3 | PR #1917 `merged=None` | false positive | The SQL inserts `merged = true` (01_Universe_Inject.sql line 127); the sweep's dump script did not render the boolean. |
| C2 | Arthur's Feb 11 "transfer to my LLC" vs the later records | settled | C05KNDCHAAG/1770842137.835489 (Feb 11) is the dated claim (T17, L13); the Feb 12 checklist and Arthur's Feb 13 mail govern. |

## Fifth blind fork sweep on rev4 (focused re-sweep of the rev4 forks, fresh agent, no answer key; 2026-11-06)

Scope: the six items rev4's wording touched (ENG-2454 layer.ai, the CF VO campaign, ENG-2462, ENG-2445, ENG-2449, ENG-2446 and Arthur's 'jenkins' email). The sweep matched the solver on every value except one open state.

| # | Sweep's fork | Disposition | Record that settles it (or the route) |
|---|---|---|---|
| 1 | ENG-2454 layer.ai: Todo/Robert (the LLC takes CF's art and the export is still to do) or Canceled (the account lapses; #winddown lists layer as decided; 'cancelled it on the 11th') (OPEN) | **routed to /create-injection** | The rev4 reply C09UHHN6PFZ/1770923700.470906 ('it goes with CF, the account itself just lapses') does not say whether anything on the issue is the LLC's. Proposed wording: '... can you pull it out yourself before then? the art goes with CF, there's nothing on the layer account for the LLC to take, it just lapses' (Canceled under the project description; the step, Robert and Mar 3 stay on the sheet, on the layer.ai or the CF row). |
| 2 | VO campaign: its own row and issue (WEAK) | settled | 'count it as its own line' plus the prompt's 'the project should match the sheet'; cost 'capped at $3,000 a month' beats $100 × 31; payer 'moves to our new company's card from March'. |
| 3 | ENG-2462 By: Feb 27 or Feb 28 (WEAK) | accepted (rubric) | 'off it before Feb 28th' (C0ADGSZKR3R/1770789534.434749); brief §4b accepts any Feb 15–28 date. State Todo: the App Review notice beats Arthur's 'done'. |
| 4 | ENG-2445: $95 or $62 (WEAK) | settled | the 'jenkins' email (04:20Z) 'bills $62 a month now' beats the 00:58Z note under 'Cost every item at what it bills now'; Todo, Mar 1. |
| 5 | ENG-2449 GitHub: Done or Todo/LLC (Leonard's 'then the repos transfer') (WEAK) | settled | the Done test comes first: 'if one of us pays it himself through May (even if HG still owns it)'; Arthur's 'count it as mine like the other two'. |
| 6 | Jenkins as a new line or issue (SETTLED) | settled | the jobs run on Arthur's own machine with no bill; the ground rules count only monthly bills; 'the build boxes are HG's'. |
| C | Seed vs base: Arthur's Feb 11 'transfer to my LLC' (superseded by the Feb 12 checklist), the Feb 7 'keep both campaigns live' (updated by the install-campaign pause), PR #1917 head_ref vs branch (platform rev3 DR6: base pattern, NB-13), Arthur's $140 reply under an unrelated Feb 2 root (the CORR trap, kept) | no change | none blocks. |

### Re-check of the fix (fresh agent, no answer key, rev4 SQL f1a290ced176)

| Field | Verdict | Disposition |
|---|---|---|
| ENG-2454 state | SETTLED: Canceled | 'to Canceled if it stays with HG' plus the reply's 'nothing on the layer account for our new company to take, it just lapses'; Todo needs 'if the LLC takes it'. The reply has no 'LLC' keyword. |
| Decision, Monthly cost, Next step, Owner | SETTLED: HG, 0, Robert pulls CF's concept art out, Robert | as solver/truth.json |
| Paid by | WEAK (wording) | 'HG', 'none' or blank are accepted (representational). |
| By | WEAK | Mar 3 / 'before Mar 3' / Mar 2 accepted (brief §4b already accepts by/before Mar 3 and Mar 1–3). |
| Row for the export step | OPEN (placement only) | accepted for the rubric: the step may sit on the layer.ai row or the Combo Fighter row (same step, owner and date on the same sheet; the surface's C4 pattern already reads either row). To be written into brief §4b at /create-prompt-writing. |
