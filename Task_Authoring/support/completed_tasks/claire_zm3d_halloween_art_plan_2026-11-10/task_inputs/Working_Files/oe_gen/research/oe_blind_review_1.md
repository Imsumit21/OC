# Oracle Events blind review 1 (HarmonyGames task_inputsN2)

Reviewer: independent, did not write the set. Clock 2025-10-01 00:00 PT (07:00 UTC), Oct 1, 2025 (synth-cut). Persona claire_morgan (Claire Morgan, Art Lead).
Reviewed: `Task_Authoring/task_inputsN2/08_Oracle_Events.md`, 161 events (OE 1 to OE 161): 31 reads (OE 1-30, OE 37), 6 reasoning events (OE 31-36), 124 writes (OE 38-40, OE 41-52 shares, OE 53-110 comments, OE 111-158 assignments, OE 159-160 tickets, OE 161 reply).
Evidence: `Working_Files/oe_gen/sql_rows.json` (read as data), base universe through `hg.py search` and `hg.py records`, visibility through `persona_view.py` (can-see, reach, check-sql), tool contracts from `Evals/references/tools/catalog.json` and `Task_Authoring/Audit_2026-10-30_Live_Sandbox/state_full.json`, behaviour from `oe_gen/research/baseline_tool_shapes.md`. No SQL was executed. None of the excluded files was opened.

## Result in one view

| Pass | Checked | INACCURATE | MINOR | MISSING | FORMAT |
|---|---|---|---|---|---|
| A / O1 accuracy | 161 events | 0 | 7 | 0 | 0 |
| B re-derivation | 62 rows, 120 ticket/share writes | 0 mismatches | | | |
| C / O2 completeness | 13 requirements, 161 events | 0 | 0 | 0 | 0 |
| D format, non-action, absence | 161 events | 0 | 0 | 0 | 0 |

No wrong call, due date, maker, recipient, id, time or quote was found, and every stated count holds for its ID list. All seven findings are imprecise wording that does not change the path. Under `oracle_events.md` any one of them still scores Accuracy 3 (NON-FAIL) if confirmed, so they are worth fixing before `/oe`.

## Findings

Format: `DR# | pass | OE# and quoted OE text | record path, id and quoted value | Eval dimension | proposed severity`

DR1 | O1 | OE 15 "Expected: 3 messages: "October UA plan (draft)", "Unity retention restart" and "October UA plan - changes"."; OE 16 "(subject "October UA plan (draft)" from OE 15)"; same in OE 17 and OE 18 | `state_full.json` mcp_servers gmail, tool gmail_search_messages: "returns id/threadId pairs newest first."; `baseline_tool_shapes.md` section 5, B2#6 output `{"messages": [{"id": "claire.morgan@harmonygames.co/<CANf1Nxe0e348c2afd3a05d686bccff4582ec3@mail.gmail.com>", "threadId": ...` and "There is no subject, sender or snippet" | Accuracy, Eval 2 section 2.3A and 2.4: the listing call cannot show the subjects on its Expected line, and OE 16-18 pick a mail by a subject the prior step never returned. The three mails are all opened anyway, so the outcome holds | MINOR

DR2 | O1 | OE 38 "store art and icon by the Thu Oct 16 12:00 PT cut for the Oct 17 submission" | `sql_rows.json` line 199, gdocs.docs_documents f_fdd6d2d2f4a4d2f5b908fb body_text: "Google Play listing graphics are not tied to a build: upload any day and allow 1 day for review."; OE 36 itself says the Google Play set is "upload any day and allow 1 day for review" | Accuracy, O1 qualifier: "store art" covers the Google Play phone set, which the calendar takes out of the cut. OE 38 also drops the Google Play route from the plan doc's "ship route and dates" | MINOR

DR3 | O1 | OE 40 "A header and 62 rows ... each with its call, owner, due date and a short reason." | `sql_rows.json` gslides.slides_page_elements el_b04e5ccd5706: "Skip: no seasonal version this time."; gmail "October UA plan - changes" body: "so don't make Halloween versions of anything that only runs there."; line 199 calendar as in DR2. OE 31 says "Each is Skip, with no due date and no assignee" | Accuracy: followed literally, OE 40 asks for an owner and a due date on 10 Skip rows and a due date on the Google Play row, which OE 31 and OE 36 say do not have one | MINOR

DR4 | O1 | OE 32 "12 working ads whose newest capture is at or after Android #1452 with a master without music" | `sql_rows.json` linear.linear_comments cmt on ART-833: "Rendered from Android #1529 footage (Aug 4). Master: SFX only, no music. Unity: iOS UK phone, Android US phone."; same "#1529" and "SFX only, no music" on ART-834, ART-835, ART-848 | Accuracy, O1 "count lists yourself" and qualifier: the filter as written returns 16, not 12. The ID list is right because OE 26 and OE 33 take those four out; the sentence needs that third condition | MINOR

DR5 | O1 | OE 6 'the doc titled "ZM3D release calendar"' | `sql_rows.json` line 199, gdocs.docs_documents f_fdd6d2d2f4a4d2f5b908fb title: "ZM3D release calendar — Q4"; drive_files line 197 name the same | Accuracy, Eval 2 section 2.4 (names character for character): the title is cut short. It still resolves to one record (gdrive_search "release calendar", 7/7 runs) | MINOR

DR6 | O1 | OE 26 'comment on card "Marketing Video Refresh"' | Trello `data.json` /cards/750 id 68768a1501ae552dbee94b8a name: "Marketing Video Refresh (Marcus/[PERSON_NAME_0036])"; injected action 68d6cff0c6568da5d9c8e81f data.card.name the same | Accuracy, Eval 2 section 2.4: partial name on an Expected line. Harmless, the card is unique | MINOR

DR7 | O1 | OE 25 "Marcus's post is the #zombie-art hit of the same search" | The search just before it is OE 24, a Drive search ("search "ZM3D Halloween 2025""). The Slack search is OE 23 ("search "cheer fastcouch""). `sql_rows.json` line 10, slack message 4c2fdbe41fae4579a928389af8bd163d text: "quick test on cheer fastcouch, 9:16 and 16:9, pumpkins and fog over the cut. files are in ua masters" | Accuracy, dependency wording: read straight through, "the same search" points at the wrong event. Naming OE 23 fixes it | MINOR

## Pass A / O1: event sign-off

Every quoted string in OE 1-40 was machine-compared with `sql_rows.json`. All matched character for character except five that belong to base records or are search strings, and those were opened by hand (OE 15 and OE 27 query strings; OE 27 Frederick and Marcus quotes; OE 30 Martin quote). All 65 comment quotes in OE 10-14 equal a whole comment body. PT times were computed from UTC ts values with a -7h offset, weekdays from the calendar.

| OE | Record opened | Result |
|---|---|---|
| 1 | slack C06DJBJL798 ts 1759269913.882683 (line 19); 22:05:13Z = Tue Sep 30 3:05 PM PT; private, Claire a member; route is slack_search_channels with channel_types, then slack_read_channel, parent is top level | Verified |
| 2 | gcal evt_d947bf7cd910549b674b1f (line 309); 16:00Z = Thu Oct 2 9:00 AM PT; 7 attendees, 6 besides Claire; description quote exact | Verified |
| 3 | drive/sheets f_02b1968f5e882366fbb883 (lines 190-196); owner frederick.stone; 4 tabs; Read me quotes exact; 4 Store rows | Verified |
| 4 | Unity grid: 56 rows, all 56 name and ticket pairs equal; listed in ticket order, not sheet order, no effect | Verified |
| 5 | Archive grid: 4 rows, names and tickets equal | Verified |
| 6 | gdocs f_fdd6d2d2f4a4d2f5b908fb; owner arthur.blake; all quotes exact; Oct 16 Thu, Oct 17 Fri, Oct 22 Wed | Title: DR5. Icon line: AR5 |
| 7 | gslides f_5ebf55ad29e815d46243c8; owner robert; 8 elements; all quotes exact | Verified |
| 8 | linear rows ART-793 to ART-854: 62; 58 Done, 4 Canceled; "Paused on Sep 15" on 836-838, "Paused on Sep 19" on 839; 826 and 831 not on the sheet; 56 + 4 + 2 = 62; filter proven by B2#88, hasNextPage false | Verified |
| 9 | trello action 68dc65a0f2d7fb28743f5860; 23:20Z = Tue Sep 30 4:20 PM PT; idMemberCreator 4b4a68fc0fec0b254e4f9d8e = Frederick Stone (/members/12); board ZM ROADMAP; quotes exact | Verified |
| 10-14 | linear_comments for 58 tickets; 65 quotes equal whole bodies; unquoted second comments are the "Still running ... (checked Sep 9)" notes on 10 tickets, none changes a campaign | Verified |
| 15 | 3 mails in Claire's mailbox from frederick.stone (B1#18 3 of 3); lines 226, 251, 271 | Count verified. Subjects: DR1 |
| 16 | mail Date header Fri, 12 Sep 2025 10:40:00 -0700; quotes exact | Verified |
| 17 | mail Date header Tue, 30 Sep 2025 16:10:00 -0700; quotes exact | Verified |
| 18 | mail Date header Mon, 29 Sep 2025 16:48:00 -0700; quote exact | Verified |
| 19 | slack C0880U9751A ts 1759275738.984915 (line 30); 4:42 PM PT; reply under 1759211437.306779, parent id cd68a603aef386cb7ad0f7cf9a363f04 matches line 32; private, Claire a member; words AND as substrings, search returns reply rows, newest first, so it is the top hit | Verified |
| 20 | slack C05KNDCHAAG ts 1759243286.478812 and 1759275107.322377; 7:41 AM and 4:31 PM PT; private, Claire a member; both match "ad statics" | Verified |
| 21 | slack users.json /3: EMPLOYEE_0005_SLACK_ID = Julia Lawson, julia.lawson@harmonygames.co; slack_read_user_profile takes user_id | Verified |
| 22 | slack C09ATAJ220H ts 1758823964.738872; Thu Sep 25 11:12 AM PT; private, Claire a member; base hits for "couch alpha 50" are file names only, so the message search lands on this post | Verified |
| 23 | slack D05V2N6PZNU ts 1759166437.080255; Mon Sep 29 10:20 AM PT; is_im true, 5 member ids listed but only Claire and Marcus post (Sep 2025: 23 and 22 messages) | Verified |
| 24 | drive d_272d849cde40c35980a433, d_74a7c95c28097dd9777e01, d_6c2e4339e5d58108799ac8; files f_dc5cf9e4250d433c1511ec, f_bcd34f98925e3f20d846ce owned by marcus.bennett; all shared with Claire | Verified |
| 25 | slack C08R8CHB0QL ts 1759167065.499092, 1759248337.170599, 1759249269.380507; 10:31 AM, 9:05 AM, 9:21 AM PT; thread read returns both replies (B4#96) | Values verified. Route wording: DR7 |
| 26 | trello action 68d6cff0c6568da5d9c8e81f; 17:40Z = Fri Sep 26 10:40 AM PT; actions arm matches comment text, all three words present; base has no other "end card" comment | Values verified. Card name: DR6 |
| 27 | slack C06DJBJL798 /2025-08 ts 1755114007.441789 (12:40 PM PT, reply_count 15, file marcus.bennett_9-16_blur-VEED.mp4) and 1755118817.302199 (files as quoted); in: and on: are valid modifiers; 17 messages that UTC day, inside the default 20 | Verified. "keeps its music": see AR2 |
| 28 | slack C08R8CHB0QL ts 1759245641.309714, 1759247246.453725; 8:20 AM, 8:47 AM PT | Verified |
| 29 | drive_files lines 177-187: 5 iPhone65 + 6 GooglePlay_phone PNG = 11, parent d_74a7c95c28097dd9777e01; base Drive holds no Halloween iPad file (hg search "halloween", "ipad") | Verified |
| 30 | slack C08R8CHB0QL ts 1758121809.236839 (8:10 AM PT, base record id 9025d428af1f551a20e303c3acbc545b matches line 29 parent) and 1758127951.679146 (9:52 AM PT); inside the first 7 hits for "app icon", newest first; message also carries image 11.png, not a claim | Verified |
| 31 | see table below: 10 of 10 | Verified |
| 32 | 12 of 12 IDs | IDs verified. Filter wording: DR4 |
| 33 | 36 of 36 IDs, sub-count 31 + 1 + 4 | Verified |
| 34 | 30 + 18 = 48 of 48 | Verified |
| 35 | 6 + 42 = 48; ART-832 description "Made by Martin Walsh" | Verified |
| 36 | four store calls, see table | Verified |
| 37 | linear /users/33, /users/18, /users/9, /users/28, /teams/0: ids and emails as quoted | Verified |
| 38 | gdocs_create_document; content checks against OE 31-36 | Route verified. Scope: DR2 |
| 39 | gsheets_create_spreadsheet returns spreadsheetUrl | Verified |
| 40 | 4 + 56 + 2 = 62; 14 + 36 + 2 + 10 = 62 | Counts verified. "each with": DR3 |
| 41-52 | gdrive_share_file, role commenter; 6 addresses equal the 6 attendees on each of 2 files; roster addresses exact | Verified |
| 53-110 | linear_create_comment; 58 tickets once each; call, due, dependency tags and heading names all checked by script | Verified, 0 differences |
| 111-158 | linear_update_issue; 48 tickets once each; 42 Marcus, 6 Julia; Skip tickets excluded | Verified, 0 differences |
| 159-160 | linear_create_issue; team ART; assignee martin.walsh; due 2025-10-16 is the Thu Oct 16 cut | Verified |
| 161 | slack_send_message with thread_ts; doc link from gdrive_share_file `file.webViewLink`, tracker link from `spreadsheetUrl`; Claire a channel member | Verified |

Visibility: `persona_view.py check-sql` gives YES for every Claire-side row (gcal 7, gdocs 1, gdrive 19, gmail 4 + 4, gsheets 5, gslides 13, slack 16). The 24 NO rows are other people's mailbox copies, which no event reads. Linear and Trello are unscoped. Base records used (Aug 13 thread, Martin's Sep 17 post) sit in channels where Claire is a member. Every named tool is in `catalog.json`.

Date check: nothing expected as done falls after the clock. Act-vs-defer (2.6): no defer found. Scope: Slack text across all channels for Sep 2025 on "hold off", "ART-8" and "ART-79" (0 hits for the first three; "as-is" has 3 hits, none in the channels this task uses), and for Aug-Sep 2025 on "halloween" and "seasonal" (7 and 4 base hits: Martin's concept post and unrelated items), plus every injected Slack row and Claire's four injected mails. Base Linear, Trello and Confluence have no "halloween" hit.

Considered and not raised:
- OE 16-18: Gmail bodies come back base64 in `payload.body.data`. The text is still exposed and all seven runs recovered it, so this is tool shape, not a wrong step.
- OE 8 `ART-826 "julia 4:5"`: the ticket title adds "(4:5 static)", but the quote is the creative name and makes no title claim.
- OE 4 says "each with its creative, format and ART ticket" and lists no separate format. Nothing stated is wrong.
- OE 37 is not strictly needed, since assignee takes an email. It is harmless and flags marcus.lee.
- Injection note, not an OE defect: ART-809 and ART-817 to ART-819 say "Captured from Android #1630 on Aug 13", while Marcus posted the investor video at 11:42 AM PT and #builds shows #1630 starting at 12:00 PM PT. No call changes, since either way the source is after #1452.

## Pass B: re-derived calls

Method: from the 75 ticket comments, Frederick's two mails and his Slack reply, Marcus's Sep 25 post, Robert's deck and thread reply, Frederick's two Trello comments, the Aug 13 thread and the Drive listing. Rule order: Android US tablet only = Skip; old zombies note, source before #1452, or baked music = Refresh first; otherwise Halloween version. Due: Fri Oct 10 if the ad is on Android US phone, otherwise Wed Oct 15. Maker: Julia for working statics, Marcus for video and end cards, Martin for store art.

Totals: Halloween version 14 (12 ads + 2 store), Refresh first 36, Reuse 2, Skip 10. Due Oct 10: 30, Oct 15: 18. Makers: Marcus 42, Julia 6, Martin 4 store.
Comparison: OE 31, 32, 33, 34, 35, 36 and all of OE 53-110, 111-158, 159-160 and 41-52 match. Mismatches: 0.

| # | Surface | Campaigns in play | Deciding record | Call | Due | Maker | OE comment / assign | Match |
|---|---|---|---|---|---|---|---|---|
| 1 | app icon | App Store, Google Play | Robert rejected the Sep 17 concept for the icon | Halloween version | Thu Oct 16 12:00 PT | Martin Walsh | OE 159 ticket | Yes |
| 2 | iPad 12.9" set | App Store | On the Store tab, no file in the Store folder | Halloween version | Thu Oct 16 12:00 PT | Martin Walsh | OE 160 ticket | Yes |
| 3 | iPhone 6.5" set | App Store | 5 exported PNGs, Leonard: no ticket | Reuse | Thu Oct 16 12:00 PT, Oct 17 submission | Martin Walsh | none | Yes |
| 4 | Google Play phone set | Google Play | 6 exported PNGs, Leonard: no ticket | Reuse | Any day, allow 1 day review | Martin Walsh | none | Yes |
| 5 | ART-793 couch boss 30 | iOS UK phone, Android US phone | #440, older than #1452 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 53 / OE 111 | Yes |
| 6 | ART-794 couch alpha 30 | iOS UK phone, Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 54 / OE 112 | Yes |
| 7 | ART-795 couch alpha 50 | iOS UK phone, Android US phone | Marcus re-record #1935 (Sep 25 post) beats Apr 7 note | Halloween version | Fri Oct 10 | Marcus Bennett | OE 55 / OE 113 | Yes |
| 8 | ART-796 balloons alpha 50 | iOS UK phone, Android US phone | #456, older than #1452, music baked | Refresh first | Fri Oct 10 | Marcus Bennett | OE 56 / OE 114 | Yes |
| 9 | ART-797 balloons alpha 50 (1) | iOS UK phone, Android US phone | Marcus re-record #1966 beats Apr 7 note | Halloween version | Fri Oct 10 | Marcus Bennett | OE 57 / OE 115 | Yes |
| 10 | ART-798 barrel alpha 30 | iOS UK phone, Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 58 / OE 116 | Yes |
| 11 | ART-799 couch marketing2 30s | iOS UK phone, Android US phone | #457, older than #1452, music baked | Refresh first | Fri Oct 10 | Marcus Bennett | OE 59 / OE 117 | Yes |
| 12 | ART-800 couch marketing2 endcard | iOS UK phone, Android US phone | #475, older than #1452 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 60 / OE 118 | Yes |
| 13 | ART-801 barrel alpha 30 endcard | iOS UK phone, Android US phone | #475, older than #1452 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 61 / OE 119 | Yes |
| 14 | ART-802 couch alpha 30 endcard | iOS UK phone, Android US phone | #475, older than #1452, music baked | Refresh first | Fri Oct 10 | Marcus Bennett | OE 62 / OE 120 | Yes |
| 15 | ART-803 balloons alpha 50 endcard | iOS UK phone, Android US phone | #475, older than #1452 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 63 / OE 121 | Yes |
| 16 | ART-804 balloons marketing2 endcard | iOS UK phone, Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 64 / OE 122 | Yes |
| 17 | ART-805 barrel marketing2 4:5 | iOS UK phone | Marcus re-record #1896 beats Apr 29 note | Halloween version | Wed Oct 15 | Marcus Bennett | OE 65 / OE 123 | Yes |
| 18 | ART-806 barrel marketing2 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 66 / none | Yes |
| 19 | ART-807 cheer 30p 9:16 | iOS UK phone, Android US phone | #771, older than #1452, music baked | Refresh first | Fri Oct 10 | Marcus Bennett | OE 67 / OE 124 | Yes |
| 20 | ART-808 cheer fastcouch 9:16 | iOS UK phone, Android US phone | Re-captured Sep 16 on #1896; Robert turned down the July-capture test | Halloween version | Fri Oct 10 | Marcus Bennett | OE 68 / OE 125 | Yes |
| 21 | ART-809 marcus.bennett 9:16 | iOS UK phone, Android US phone | #1630 but music baked (Frederick, Aug 13 thread) | Refresh first | Fri Oct 10 | Marcus Bennett | OE 69 / OE 126 | Yes |
| 22 | ART-810 squirrelfail portrait | Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 70 / OE 127 | Yes |
| 23 | ART-811 squirrelfail landscape | Android US tablet | Off iOS UK tablet (Frederick mail Sep 29); Android US tablet only | Skip | none | none | OE 71 / none | Yes |
| 24 | ART-812 mrfluffernot portrait | iOS UK phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Wed Oct 15 | Marcus Bennett | OE 72 / OE 128 | Yes |
| 25 | ART-813 mrfluffernot landscape | Android US tablet | Off iOS UK tablet (Frederick mail Sep 29); Android US tablet only | Skip | none | none | OE 73 / none | Yes |
| 26 | ART-814 cinematicTutorial Ad 1 | iOS UK phone, Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 74 / OE 129 | Yes |
| 27 | ART-815 tutorialCinematic portrait | iOS UK phone, Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 75 / OE 130 | Yes |
| 28 | ART-816 cheer fastcouch 16:9 | iOS UK tablet, Android US tablet | Exported Sep 16 from #1896; Robert turned down the July-capture test | Halloween version | Wed Oct 15 | Marcus Bennett | OE 76 / OE 131 | Yes |
| 29 | ART-817 marcus.bennett 16:9 | iOS UK tablet, Android US tablet | #1630, no music | Halloween version | Wed Oct 15 | Marcus Bennett | OE 77 / OE 132 | Yes |
| 30 | ART-818 marcus.bennett 4:5 | iOS UK phone | #1630, no music | Halloween version | Wed Oct 15 | Marcus Bennett | OE 78 / OE 133 | Yes |
| 31 | ART-819 marcus.bennett 1:1 | iOS UK phone, Android US phone | #1630, no music | Halloween version | Fri Oct 10 | Marcus Bennett | OE 79 / OE 134 | Yes |
| 32 | ART-820 cheer 30p 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 80 / none | Yes |
| 33 | ART-821 couch alpha 30 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 81 / none | Yes |
| 34 | ART-822 balloons alpha 50 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 82 / none | Yes |
| 35 | ART-823 couch alpha 50 16:9 | iOS UK tablet, Android US tablet | Own capture #456; Marcus note names "couch alpha 50" only | Refresh first | Wed Oct 15 | Marcus Bennett | OE 83 / OE 135 | Yes |
| 36 | ART-824 barrel alpha 30 endcard 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 84 / none | Yes |
| 37 | ART-825 julia 1:1 | iOS UK phone, Android US phone | #852, older than #1452 | Refresh first | Fri Oct 10 | Julia Lawson | OE 85 / OE 136 | Yes |
| 38 | ART-826 julia 4:5 | iOS UK phone | #852 (Jun 5); off the sheet, counted in by Frederick Trello Sep 30 | Refresh first | Wed Oct 15 | Julia Lawson | OE 86 / OE 137 | Yes |
| 39 | ART-827 julia 9:16 | iOS UK phone, Android US phone | #852, older than #1452 | Refresh first | Fri Oct 10 | Julia Lawson | OE 87 / OE 138 | Yes |
| 40 | ART-828 julia 16:9 | iOS UK tablet, Android US tablet | #852, older than #1452 | Refresh first | Wed Oct 15 | Julia Lawson | OE 88 / OE 139 | Yes |
| 41 | ART-829 julia 1:1 android 1080 | Android US phone | #852, older than #1452 | Refresh first | Fri Oct 10 | Julia Lawson | OE 89 / OE 140 | Yes |
| 42 | ART-830 julia 4:5 android 1080x1350 | Android US phone | #852, older than #1452 | Refresh first | Fri Oct 10 | Julia Lawson | OE 90 / OE 141 | Yes |
| 43 | ART-831 marcus portrait UA end card | Android US phone | #1450, older than #1452 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 91 / OE 142 | Yes |
| 44 | ART-832 end card template 16:9 | iOS UK tablet, Android US tablet | #456, older than #1452 | Refresh first | Wed Oct 15 | Marcus Bennett | OE 92 / OE 143 | Yes |
| 45 | ART-833 end card 001 | iOS UK phone, Android US phone | #1529 but old zombies on packs (Frederick, Trello Sep 26) | Refresh first | Fri Oct 10 | Marcus Bennett | OE 93 / OE 144 | Yes |
| 46 | ART-834 end card 16:9 from 001 | iOS UK tablet, Android US tablet | Cut from end card 001, old zombies (Trello Sep 26) | Refresh first | Wed Oct 15 | Marcus Bennett | OE 94 / OE 145 | Yes |
| 47 | ART-835 end card 1:1 from 001 | iOS UK phone, Android US phone | Cut from end card 001, old zombies (Trello Sep 26) | Refresh first | Fri Oct 10 | Marcus Bennett | OE 95 / OE 146 | Yes |
| 48 | ART-840 boris fastcouch 9:16 | iOS UK phone, Android US phone | Captured Jul 28, before Jul 29; Sep 11 opening is an edit | Refresh first | Fri Oct 10 | Marcus Bennett | OE 96 / OE 147 | Yes |
| 49 | ART-841 boris alin2 9:16 | iOS UK phone, Android US phone | #1427, older than #1452 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 97 / OE 148 | Yes |
| 50 | ART-842 boris fastcouch 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 98 / none | Yes |
| 51 | ART-843 couch boss 30 16:9 | iOS UK tablet, Android US tablet | #440, older than #1452 | Refresh first | Wed Oct 15 | Marcus Bennett | OE 99 / OE 149 | Yes |
| 52 | ART-844 couch marketing2 30s 16:9 | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 100 / none | Yes |
| 53 | ART-845 cinematicTutorial Ad 1 16:9 | iOS UK tablet | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Wed Oct 15 | Marcus Bennett | OE 101 / OE 150 | Yes |
| 54 | ART-846 tutorialCinematic 1:1 | Android US phone | Dec 2024 prototype or dated Apr capture, pre-Jul 29 | Refresh first | Fri Oct 10 | Marcus Bennett | OE 102 / OE 151 | Yes |
| 55 | ART-847 cheer 30p 4:5 | iOS UK phone | #771, older than #1452, music baked | Refresh first | Wed Oct 15 | Marcus Bennett | OE 103 / OE 152 | Yes |
| 56 | ART-848 end card 4:5 from 001 | iOS UK phone | Cut from end card 001, old zombies (Trello Sep 26) | Refresh first | Wed Oct 15 | Marcus Bennett | OE 104 / OE 153 | Yes |
| 57 | ART-849 julia 1:1 android tablet | Android US tablet | Android US tablet only; campaign ends Oct 12 | Skip | none | none | OE 105 / none | Yes |
| 58 | ART-850 boris alin2 16:9 | iOS UK tablet, Android US tablet | #1427, older than #1452 | Refresh first | Wed Oct 15 | Marcus Bennett | OE 106 / OE 154 | Yes |
| 59 | ART-851 cheer fastcouch 4:5 | iOS UK phone | #1896, no music | Halloween version | Wed Oct 15 | Marcus Bennett | OE 107 / OE 155 | Yes |
| 60 | ART-852 barrel marketing2 1:1 | Android US phone | #1896, no music | Halloween version | Fri Oct 10 | Marcus Bennett | OE 108 / OE 156 | Yes |
| 61 | ART-853 couch alpha 50 4:5 | iOS UK phone | #1935, no music | Halloween version | Wed Oct 15 | Marcus Bennett | OE 109 / OE 157 | Yes |
| 62 | ART-854 balloons alpha 50 (1) 16:9 | iOS UK tablet, Android US tablet | #1966, no music | Halloween version | Wed Oct 15 | Marcus Bennett | OE 110 / OE 158 | Yes |

Arguable calls (none is proposed as a defect; each gives the record that makes it arguable):

- AR1, ART-823 couch alpha 50 16:9. Marcus: "couch alpha 50 on android #1935"; ART-853: "Exported Sep 23 from Android #1935, same edit." A wide reading of "the newest capture is the one that counts" could carry #1935 to the 16:9. I keep Refresh first: the only comment on ART-823 is "Captured from Android #456 on Apr 7", the name Marcus uses matches ART-795 exactly, and no 16:9 exists from #1935. Either way the 16:9 needs a new cut.
- AR2, ART-809 marcus.bennett 9:16. "The live 9:16 cut keeps its music" is an inference, not a quote: the thread ends with no-music variants delivered, and no Claire-visible record shows a re-cut going live. The call survives both ways, because the deck says "re-cut first from a master without music (re-export one from the project if there is none)". The later `marcus_9-16_blur-VEED (1).mp4` (Aug 17) sits in a DM Claire cannot read.
- AR3, ART-831 portrait end card. Base #builds shows #1450 is where the background landed: "New Background and light/reflection rebake". The deck's line is still "older than Android #1452" and #1452 is the ZombieSwap build, so Refresh first stands.
- AR4, the 24 ads on both iOS UK phone and Android US phone. Frederick: "any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th." A split date is conceivable, but one file per ticket means the earlier date binds. Oct 10 stands.
- AR5, icon. OE 6 and OE 38 say the icon rides the Oct 17 build, "not a swap around the 24th". The calendar names the icon only on its Nov 6 line: "post-Halloween clean-up (icon and screenshots back to normal)". That covers the App Store. The sheet lists the icon on "App Store, Google Play", and "Google Play listing graphics are not tied to a build", so the Play half is not settled by a record. The due date does not change.
- AR6, icon and iPad set due date. Martin: "I'll be on vacation Oct 6-15 ... store art stays with me." The Oct 16 noon cut is his first morning back, so the real work window is Oct 1-3 or that morning. OE 35 flags the vacation for statics only; OE 36, 38, 159 and 160 do not raise it. No record sets an earlier date, so Oct 16 is correct, but a reviewer may ask why the plan is silent.
- AR7, Google Play set by-when. The prompt asks "who makes what by when". The record gives only "upload any day and allow 1 day for review", so OE 36 gives no date. Reasonable for a Reuse, but it is the one non-Skip row with no date.
- AR8, ART-832 maker. Description says "Made by Martin Walsh"; Leonard says "Marcus has video and end cards". Title is "(16:9 end card)". Marcus stands, as OE 35 says.

## Pass C / O2: completeness

none. 13 requirements checked:

| Requirement (prompt or Leonard) | Events |
|---|---|
| Read Leonard's message | OE 1 |
| Thursday's review and who is on it | OE 2 |
| Everything live: store surfaces | OE 3, 29, 30, 36 |
| Every ad running, including off-sheet | OE 4, 5, 8, 9 |
| Release calendar dates, icon question | OE 6 |
| Robert's direction | OE 7 |
| Frederick's UA plan and later changes | OE 15-19 |
| Calls and what we already have | OE 10-14, 22-33, 36 |
| Who makes what by when | OE 20, 21, 34-36 |
| Plan doc and tracker in Claire's Drive, shared to comment | OE 38-52 |
| Comment each ad's call and due date | OE 53-110 |
| Assign the ones needing new work | OE 37, 111-158 |
| New store tickets, reply in thread with both links | OE 159-161 |

Dependency walk: each value on an Expected line has an earlier producer (ART-826 from OE 8, Sep 16 capture from OE 11, ART-833 name from OE 4, addresses from OE 2, Julia from OE 21, doc link from OE 41, tracker link from OE 39). No value is used before an event produces it, apart from the subject selection in DR1. `03_Error_Async_Config.txt` says "Friction:          none", so no recovery events are needed. The user's own act (walking people through the plan) is correctly left out.

## Pass D: format, non-action, absence

Format under Eval 2 section 2.7: none, 161 checked. All numbered 1-161 with no gaps, all have `Expected:`, no arrow chains, no JSON, every heading names a service or source, and no event mixes a lookup with a write.
Borderline, not raised: OE 10-14 bundle 58 same-kind reads in five events and OE 37 bundles four lookups. Section 2.7 defines several actions as one OE that "both looks something up and sends or updates something", and the guideline's own example chains two reads, so these pass. OE 4, 10, 11, 13 and 14 run 1,470 to 1,986 characters against the guideline's "a few lines", which is a readability note only.
Non-action or final-response events: none, 161 checked. OE 31-36 are reasoning steps with stated results. OE 5 "left out of the plan" and OE 40 "stay out" sit inside real steps.
Absence words on Expected lines, each backed:
- OE 29 "with no file here": Store folder listing, plus base Drive scan for "halloween" and "ipad".
- OE 36 "the exported sets get none": Leonard, "no tickets needed for those".
- OE 9 "never made it", OE 13 "Not on the live creatives sheet yet", OE 3 "have no ART ticket": the records' own words.
- OE 31 "no due date and no assignee": a decision from the deck's Skip line, not a claim about existing data.
- OE 33 "keeps its April capture" and OE 22 "keep their own captures": ticket comments, and the only Slack text hit for the name is Marcus's post.
- OE 27 "keeps its music": see AR2.
