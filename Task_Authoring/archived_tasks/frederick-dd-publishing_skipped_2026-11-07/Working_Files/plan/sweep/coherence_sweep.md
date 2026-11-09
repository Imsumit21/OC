# Coherence sweep: seeded records against the base

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Seeded text read: `Working_Files/plan/sweep/seeded_records.md` only. Base read through `hg.py search` and `persona_view.py` only.
Record ids: Slack `channel:ts`, Gmail thread file, Drive/Docs file id, gcal event id.

Counts: 1 BLOCKER, 6 FIX, 14 NOTE.

## BLOCKER

### B1. Outreach sheet says nothing was sent to Appodeal
- Seeded: `f_fd467bd2ae0c6d4f3bd2bc` row `Appodeal | their partnerships team | Apr 17, 2025 | came to us | nothing, they wrote first`.
- Base, all in Frederick's own mail and DM:
  - `threads/frederick@harmonygames.co_1829689338387596598.json`, 2025-04-17T22:08:32Z, subject "We received your application - Next steps": "We're thrilled that you've taken the step to apply for Appodeal publishing Program."
  - `slack D05S58U4SAK:1745277199.604849`, 2025-04-21T23:13:19Z, Frederick: "I'm filling out Appodeal's intake form. They ask for DAU and ARPDAU."
  - `threads/frederick@harmonygames.co_1830012626042968381.json`, nine-message thread "Appodeal publishing Program". Frederick wrote 2025-04-29T17:16:13Z and 2025-05-14T16:29:35Z ("Can I ask if it's possible to structure a publishing deal for specific geos?"). Appodeal wrote last, 2025-05-21T05:33:45Z ("Just checking in to see if you've had a chance to consider our proposal").
- Why it fails: a solver has to open this thread to place Appodeal, and the thread shows an application, a form and two replies beside a cell that says "nothing".
- Smallest fix: change the cell to `Intake form (DAU, ARPDAU)`. Keep `came to us`. The status is unaffected: no terms, last message theirs, so Waiting on us still holds.

## FIX

### F1. "still Live" appears four days before Live exists
- Seeded: Slack reply 2025-09-25T16:20Z (`C096HFA5Z8W`, id 1e1e72f7): "Anyone who got it and is still Live hears the organic figure from us".
- Seeded order: the status word is defined in the ground rules, 2025-09-29T16:00Z. At 16:20Z on Sep 25 only one May one-pager recipient had sent terms (Harbor Lane, 16:00Z); Wavecrest, Moonrail and Tallwater come later.
- Smallest fix: lower-case it or say "is still talking to us". Keeping the capital needs a re-date to after Sep 29 16:00Z, which then clashes with the doc's "Anything I've already said".

### F2. May mails say US only after the global release
- Seeded: six mails dated May 7 to 9 (Sofia, Anika, Rhys, Nadia, Orchard Lane, Summit): "is live on iOS and Android in the US, and we're exploring publishing partners for new markets".
- Base:
  - `slack C05KNDCHAAG:1746387035.926539`, 2025-05-04T19:30:35Z: "our global release build is out ... we'll release the build in all countries by EOD today/early tomorrow".
  - `slack C05KNDCHAAG:1746557417.594259`, 2025-05-06T18:50:17Z: "Domino Delights is now live in 16 languages and will be available to players around the world in the next 24 hours".
  - `slack C07C2866011:1746560478.552859`, 2025-05-06T19:41:18Z: "we are live in Turkey on both ios and android".
- The wording itself is base (template in Biz Dev Notes, see clean list), so May 5 and the two May 6 17:xxZ mails are fine.
- Smallest fix: move the six sends to May 5 or 6 before 18:50Z (replies are May 12 to 15, so order survives), or change those six to "live on iOS and Android, with UA in the US so far".

### F3. "DD publishing: founders" includes Frederick
- Seeded: four events `evt_881d3e07c598b2205a7ff3`, `evt_8512c7a6aa483d8aeb6a7d`, `evt_b0d8daa048f918be523cb0`, `evt_cb02d2cef6eb1d6bd4cd0b` and four invite mails.
- Base: `evt_12a95022752d8c588866b1` "founders Biweekly Sync" has attendees arthur.blake, leonard.hayes, robert only. `evt_189fe218303982c1d78e99` "Executives Biweekly Sync" is the one with Frederick. The channel is #executives. Card SC-49 says not to rest anything on Frederick's founder status.
- Smallest fix: rename to `DD publishing: execs` in the events and invite subjects and bodies. "The four of us" in the mail and doc is already right.

### F4. British spelling and idiom from US writers
- Seeded: ESG Law mail subject "Licence paper timing", body "turn a licence". Trello comment by Frederick: "Lena rang."
- Base: ESG Law signature `threads/leonard@harmonygames.co_1841635707568607753.json`, 2025-08-27T21:49:52Z: "5115 Excelsior Blvd. #729 | Minneapolis, MN 55416". Frederick is in Seattle (`slack C07C2866011:1746119691.531529`, 2025-05-01T17:14:51Z).
- Smallest fix: "License paper timing", "turn a license", "Lena called."

### F5. Word-for-word replies from different companies
- Seeded: "Thanks for the note. I've shared our term sheet for Domino Delights with you in Drive." eight times; "Thanks for thinking of us, but we'll pass on Domino Delights. It isn't a fit for our slate this year." six times; "Thanks. Nothing for us right now, but we plan next year's slate in the autumn, so ping me then." four times: eighteen messages from fourteen writers at separate firms.
- Base: real inbound publisher mail varies widely (Appodeal, Rayking above).
- Smallest fix: vary a few words per writer. Keep "term sheet", "in Drive" and "pass" so the facts stay findable.

### F6. Sheet footnote says unlisted names were not approached
- Seeded: "Names on my Publishing Partners doc that aren't listed here haven't been approached yet."
- Base: Publishing Partners (`f_10dfa1b4236a7c35dcb632`, 2025-09-24T17:08:16Z) lists Tilting Point first. `threads/frederick@harmonygames.co_1842443183462721250.json`, 2025-09-05T16:45:42Z, subject "'UA Funding request": "Thank you for submitting your application ... Tilting Point".
- The ground rules cover the form, so this only needs wording.
- Smallest fix: "haven't been approached about DD yet."

## NOTE

- N1. Sunset message. `slack C1C2137664A3:1751910057.219479`, 2025-07-07T17:40:57Z, Frederick to AppLovin: "we've decided to Sunset the game". It means stop UA: later base posts have DD live and seeking a publisher (2025-08-26T15:53:49Z, 2025-09-03, 2025-09-10). It is the only base line that reads as DD being shut. No change.
- N2. Oct 1 post. `slack C07C2866011:1759290145.061509`, 2025-10-01T03:42:25Z: "close an engine licensing deal with NCsoft and/or get some co-dev going" and `1759290197.446099`: "if nothing pans out in the next 7-10 days it is likely time to talk to the bankers". Five hours after the seeded mail, publishers go unmentioned. Silence, not a clash. No change.
- N3. Same-day tension. `slack D04UC0UEN2V:1758819286.279859`, 2025-09-25T16:54:46Z: "I'm chasing publishers ... not sure how fast we can get something done" lands while seeded term sheets arrive (15:00Z to 17:00Z). Fits; no change.
- N4. Rayking "First contact Sep 4". Earlier Rayking mail hit the jobs@ group: 2025-05-28, 07-11, 07-30, 08-11 (`threads/00000230`, `00000233`, `00000236`, `00000237`). Sep 4 is when it reached Frederick, so the cell reads fine as his view. The mail never names DD, but Leonard's forward does: "Should we explore for DD?" (`threads/frederick@harmonygames.co_1842348778705877030.json`, 2025-09-04T15:44:55Z).
- N5. Tamatem. Not on the sheet, yet `threads/frederick@harmonygames.co_1841836604752785737.json`, 2025-08-30T00:04:24Z, is a Tamatem Helpshift survey on "How do I submit my game for publishing?". "A name someone passed along doesn't count" keeps it out. No change, but expect a sharp reader to ask.
- N6. "(Zombie Match)" on the co-dev doc. Base co-dev is not tied to ZM: "co-dev pilot on a Mattel IP" (`slack D05S58U4SAK`, 2025-08), "hybrid-casual RPG direction" (Leonard mail 2025-09-26), and "games you are considering going after our current games" (`slack D04UP2L3E3S:1759282380.829039`, 2025-10-01T01:33:00Z). Nothing contradicts it outright. "Co-dev talks only, not DD" would be safer.
- N7. Tilting Point form "was for Zombie Match": the base never says which game. Uncontradicted.
- N8. Thread fit. The Sep 25 numbers reply sits under "talked to Matthew ... almost impossible to raise"; the Sep 30 SVB reply sits under "time to get a banker involved", which means an investment banker. Both are loose but passable. Only Robert's says "Off topic".
- N9. The short form "Fred" is not used in base: 2025 Slack case-sensitive hits are all "Frederick" or URL fragments, and Gmail has 0 for "Fred," and "Hi Fred". Leonard uses @mentions. Harmless, and the seeds use it consistently.
- N10. Leonard's voice. Base Slack is short lower-case bursts; the Sep 25 reply is one formal paragraph. His mail to Frederick is terse ("Should we explore for DD?"), the Sep 30 mail is long. Splitting the Slack reply into two or three lines would read closer.
- N11. Internal timing. The doc (Sep 29 16:00Z) predates both events the mail gives as the reason to "get serious" (Sep 29 21:50Z, Sep 30 01:37Z). "Written for Monday's talk" is dated on a Monday; "next Monday's" is clearer. Oakline's "within 3 days of this sheet" from Sep 25 is Sep 28, but the wire is Sep 29.
- N12. Sheet metadata. `f_fd467bd2ae0c6d4f3bd2bc` is stamped 2025-09-24T19:30Z but lists the tranche 3 mails sent 20:05Z to 20:55Z. Tranche 2 mails open "following up from Harmony Games" to people first contacted that day. "Reaching out" fits better.
- N13. Trello habits. Frederick (`4b4a68fc0fec0b254e4f9d8e`) has no base card or action. UA/BD was idle since 2025-03-18 and BD Follow Up cards are bare names untouched since 2024-10-04 (Netflix, Mattel). The "F/up with" pattern is base (`F/up with Martin`, card index 30). Tallwater call 18:30Z overlaps a Leonard and Frederick TikTok DM ending 18:37:02Z (`D05S58U4SAK:1759171022.538959`).
- N14. Linear. The base `/comments` array is empty, so `lc_674982ffdca63f854ec6f591` is the only Linear comment in the universe. Nothing to contradict it and no style to match.

## Time checks asked for

| Seeded claim | Earliest base support | Seeded time | Result |
|---|---|---|---|
| "a16z didn't happen" | `C07C2866011:1759196253.935149` / `1759196260.965849`, 2025-09-30T01:37:33Z: "That means that we didn't get in" | Sep 30 23:10Z | Clean; letter lands later, 2025-10-01T03:23:07Z, "expected rejection" |
| "the Turkish fund is a no" | `C07C2866011:1759179977.219349`, 2025-09-29T21:06:17Z "waiting for the Turkish VC"; `1759182620.491829`, 21:50:20Z: "so this is gonna be a no" | Sep 30 23:10Z | Clean |
| "DD publishing idea from the sync" | Exec sync doc `f_26e1f9a86761e35049192a`, Aug 28; Slack `C07C2866011:1756140953.197759`, 2025-08-25T16:55:53Z | Sep 30 | Clean |
| "position from the August sync" | Same: "I want to retain code, IP and non-mobile distribution rights but anything else is up for grabs" | Sep 29 | Clean; fits Northglow and Pinegrove |
| "my Sep 24 note", $0.50 D30 ARPI | `D05S58U4SAK:1758736747.409459`, 2025-09-24T17:59:07Z: "pure organics, $0.50 D30 ARPI" | Sep 24 20:05Z on | Clean; `1758736770.826819` gives the installs x $0.50 logic |
| New tranche on Sep 24 | `D05S58U4SAK:1758736827.548589`, 18:00:27Z: "I'll reach out to a new tranche of potential pubs today" | 20:05Z on | Clean |
| "That guy from Sep 24" | `D05S58U4SAK:1758736842.534589` / `1758736846.185239`, 18:00:42Z: "There was a dude from [USERNAME_34104] looking for games", "I'll reach out to him" | Sep 30 | Clean |
| May one-pager numbers | `C07C2866011:1746064698.469589`, 2025-05-01T01:58:18Z: first ~3K installs, D1 50%+, D7 20%+, ARPDAU ~$0.13, incentivized channels | May 5 | Clean, exact |
| Homa | Leonard mail 2025-09-17T22:34:08Z before the Sep 18 8am call Slack calls Homa (`threads/leonard@harmonygames.co_1843149115540588888.json`): "We are also considering publishing opportunities", then DD stats; `C096HFA5Z8W:1758210489.170809`, 2025-09-18T15:48:09Z: "focus Homa on the co-dev investment path" | Sep 29 | Clean; "even where DD came up" is true |
| NCsoft | `C07C2866011:1747282330.535609`, 2025-05-15T04:12:10Z; `D04UC0UEN2V`, Sep: liveops engine deep dive | Sep 29 | Clean |
| Tilting Point form | Gmail 2025-09-05T16:45:42Z (F6) | Sep 29 | Clean |
| Rayking | `threads/00000240.json`, 2025-09-04T08:54:09Z "manager of marketing"; `D05S58U4SAK:1757009185.631739`, 18:06:25Z: "I'll reach out to someone over There on linkedin" | Sep 5 16:40Z | Clean; fits the gap in that DM (no base post until Sep 6 04:23Z) |
| SVB account, "with Leonard this morning" | Invite "SVB/Harmony Games Inc catch up call" 2025-09-02. `D04UGG61DUM:1759246370.423429`, 2025-09-30T15:32:50Z, Leonard: "one pending approval on SVB"; `1759247343.811309`, 15:49:03Z, Arthur: "Submitted for approval on SVB" | Sep 30 17:05Z | Clean; the base has them on SVB that same morning |
| Calm Play | Real sister LLC, used for ZM (`C04UEQVDVB7/2025-05`, `C07C2866011/2025-07`). DD bundle is `com.harmonygames.dominodelights`, so a DD payer naming it is a mistake, which is the story | Sep 30 | Clean |
| ENG-2362 | `/issues/2305`, title "Implement Deep Link + Campaign Tracking via Singular", assignee Arthur (`usr_cc3e90160f490686`), Todo, created 2025-06-03 | Sep 26 | Clean; right author, right topic, no prior comments |
| Monday Oct 6 10am PT | See clean list | Sep 30 | Clean |

## Revenue

`ANALYTICS.MONETIZATION.REVENUE_DAILY` holds DD rows for all three months, 2 rows a day (ios, android), under `total_revenue_usd`. No zero-revenue DD rows in September.

| Month | iOS | Android | Total |
|---|---|---|---|
| 2025-07 | 1,709.85 | 368.48 | 2,078.33 |
| 2025-08 | 509.36 | 212.19 | 721.55 |
| 2025-09 | 278.28 | 102.83 | 381.11 |

Sum 3,180.99, average 1,060.33, x 12 = 12,723.96. Cross-check: Leonard's "about $150-$200/week" at `D04UGG61DUM:1756074938.954919`, 2025-08-24T22:35:38Z, is in line with August.
Cards: none names this table, the $0.50 figure, or the Sep 24 DM. Q09 says REVENUE_DAILY and _V2 agree. SC-1 is DD September installs, SC-17 is AD_REVENUE payouts; neither touches `total_revenue_usd`. SC-39 and SC-63 touch other lines of the Aug 28 sync, not the DD line.

## Checked and clean

- Roles: Frederick "I lead marketing" and "Our first title" come straight from the template in Biz Dev Notes (`f_0d17fc08eddaf231cf7f28`, 4/28/25).
- Leonard, Robert, Arthur ids: Slack EMPLOYEE_0038, 0016, 0025, Frederick 0008; Trello and Linear ids resolve to the right people.
- ESG Law: Leonard's new lawyer from Aug 26, engagement signed 2025-08-27, PERSON_2694 is PARTNER; token and role match.
- Authors: each seeded speaker plausibly says their line; Arthur owns ENG-2362, and Arthur and Leonard both work SVB.
- Slack threads: all three roots exist, ids match, replies follow the last base reply, and UPDATE counters are right (5/2, 9/1, 3/3, latest_reply equals the seeded ts).
- Channels: #bridge-pitch, #executives, #analytics and the Frederick and Leonard DM all include the people posting; Frederick can see all (persona_view).
- Oct 6: no base row that day. Monday pattern on Sep 29 is POD 16:00Z and Eng planning 16:30Z to 17:00Z (`evt_1d9a1b8875405e3d140087`, `evt_0897e1e52ec0ba414a069b`), so 17:00Z starts clear. Exec Sync rrule lands 20:00Z the same day. Leonard is back Friday (`C05KNDCHAAG:1759279503.256079`).
- Other seeded calls: Sep 25 18:00Z, Sep 26 19:00Z, Sep 29 18:30Z clash with no instance row or live Thursday, Friday or Monday series on Frederick's or Leonard's calendar. Weekdays and PDT to UTC conversions all correct.
- Dates: no seeded record is after 2025-10-01T00:00Z except the Oct 6 event itself, created Sep 30.
- Working hours: every seeded Slack, mail and Trello time is inside the sender's core window. May 7 mails stay clear of Frederick's "out of pocket" afternoon.
- Drive: `d_175c0d7bc72ed244b944cb` and `d_63fffeb4fab5233ed5bb73` are Frederick's and Leonard's root folders; base keeps files there.
- Publishing Partners doc exists and predates the sheet that cites it. No base file or card is called DD publishing.
- Trello: UA/BD board, BD Follow Up list and card id timestamps all match; dateLastActivity equals the last seeded comment.
- Gmail labels: INBOX plus CATEGORY_PERSONAL matches base; PERSON_2694 tokens match base style; Meet link format matches.
- Contacts: Anika Rao and Lena Fischer collide with nothing; job field is the right slot.
- Publishers that came to the four about DD since Apr 1: only Appodeal and Rayking found across about 50 Gmail queries and all Slack. Other hits are lead-gen vendors or newsletters.
- No base statement says the company has no publisher contact; Sep 3 mail says "Domino Delights is pursuing a publisher".
- Invented names: zero hits in Gmail (81,404 files), Slack (4,840 files), Docs, Drive, Sheets, Slides, Trello, Linear, Calendar, Contacts, Confluence for all publisher, person and domain strings, except unrelated newsletter text: "Kestrel" (Remedy project, Kestrel Capital), "Pinegrove" (Pinegrove Capital Partners), "bellwether" (common noun).
- Oct 1 00:00Z to 07:00Z: nine Slack files hold Oct posts; seven read in full, the two bot channels keyword-searched. Only N2 is near the storyline. "sent you guys a meeting invite" (00:02:11Z) is the Dentsu invite created 00:02:03Z, not a rival to the seeded one.

## Not covered

- GitHub not searched for invented names.
- Snowflake name scan did not finish: stopped after about 12 minutes on the 2.2 GB export, so invented names are unchecked there. REVENUE_DAILY itself was read row by row for Jun to Sep 2025.
- Thread-id date encoding and message-id hashes were not checked; a reviewer would not see them and the lint covers ids.
