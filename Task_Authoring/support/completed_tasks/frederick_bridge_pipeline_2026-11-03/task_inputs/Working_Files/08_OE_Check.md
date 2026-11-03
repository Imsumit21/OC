# 08 OE Check — frederick_bridge_pipeline (Q4 investor update send list, injection rev12)
Checked 2026-11-03 (round 3, after /oe round 2 NON-FAIL 3) · Events 86 · Characters 31388 (300–50,000: ok) · Ledger 2026-11-03 (08_OE_Writing_Ledger.md, stage gate oe-writing PASS) · release task-quality-v1
Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
/oe prediction (a prediction only; /oe gives the verdict): PASS 5
Completeness 5 · Accuracy 5 · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE

Inputs: /oe round 2 report (NON-FAIL 3; Completeness 5, Accuracy 3; one MINOR issue in OE 7; it confirms all five round-1 issues fixed; reviewed OE sha256 22fc978ed33b) and the /oe round 1 report (five MINOR issues, reviewed sha256 a52557b95996), 08_Oracle_Events.md (86 events, read in full), 08_OE_Writing_Ledger.md (52 facts), 04_Prompt.txt (sha256 b5ea6f0ff28c), 01_Universe_Inject.sql (sha256 69db98aed17f), 03_Error_Async_Config.txt (Friction: none), the /prompt report (PASS 5) and brief §4b for accepted variants. Every quoted span in the events was compared character for character with the specific record its own event cites (scratchpad percite.py: each event mapped to its records, a quote must sit inside one line of that record). All match except three deliberate cross-references (OE 8 quotes OE 7's "reached out to bitkraft", OE 19 quotes OE 7's "co-dev investment path", OE 17's "Edith Vane" is the search term) and the 18 new card titles, which are records the run creates. Round 1 only checked that each quote existed somewhere in the records, which is how the OE 8 thread misattributions slipped through; this round closes that gap.

## Inventory
| Segment (quoted start) | Role | Event |
|---|---|---|
| "OE 1  Find Leonard's Sep 30 email in Frederick's Gmail" | STEP (discovery) | 1 |
| "OE 2  Read the Q4 send-list doc in Drive/Docs" to "OE 5  Read the 2025 game investor list" | STEP (rules and population reads) | 2–5 |
| "OE 6  List Frederick's calendar events from Sep 3 to Sep 30 2025" | STEP (population read) | 6 |
| "OE 7  Read #bridge-pitch in Slack" to "OE 27  Find Arthur's later word on Android access" | STEP (reads, one source each) | 7–27 |
| "OE 28  Settle each recipient's group and details" | STEP (analysis) | 28 |
| "OE 29  Find Frederick's Q4 2025 investor update folder" | STEP (read) | 29 |
| "OE 30  Create the send list in Sheets" to "OE 32  Write the send list rows" | STEP (writes, one each) | 30–32 |
| "OE 33  Read the Existing Investor Update card" to "OE 35  List Frederick's calendar events from Oct 1 2025 on" | STEP (reads) | 33–35 |
| "OE 36  Work out the follow-up cards" | STEP (analysis) | 36 |
| "OE 37  Create the Keep warm checklist" to "OE 65  Add Harlem Capital to the Awaiting reply checklist" | STEP (writes: 4 checklists, 25 items) | 37–65 |
| "OE 66  Create the GFR Fund follow-up card" to "OE 83  Create the Harlem Capital follow-up card" | STEP (writes: 18 cards) | 66–83 |
| "OE 84  Comment on the existing NCsoft card" | STEP (write) | 84 |
| "OE 85  Count the firms and angels in each group" | STEP (analysis) | 85 |
| "OE 86  Reply on Leonard's thread in Gmail" | STEP (write) | 86 |

No CONTEXT, RESPONSE_DESCRIPTION or NON_ACTION segments. Every event has a number, a service, its parameters and an `Expected:` line; no arrow chains, no JSON, and no event mixes a read with a write.

## Coverage
| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |
|---|---|---|---|
| R1 find Leonard's Sep 30 email (F1) | OE 1 | Covered | Ledger route: Gmail search on the subject |
| R2 the incorporated rules (F2, F3, F7) | OE 2, OE 3, OE 4 | Covered | Ledger route |
| R3 the population, list plus off-list callers, and who stays off (F6, F15, F20, F21, F35–F40) | OE 5, OE 6, OE 7, OE 8, OE 9, OE 28 | Covered (population derived before the filter; the 48 off names backed by OE 8's mailbox check and OE 7's channel read) | Ledger route |
| R4 group per recipient (F16–F34, F40) | OE 6–OE 25, OE 28 | Covered | Ledger route; Homa via OE 6, OE 7, OE 19 |
| R5 Anton's amount, Paul off (F8–F14) | OE 10, OE 11, OE 12 | Covered | Ledger route |
| R6 build access (F41–F44) | OE 26, OE 27, OE 28 | Covered | Ledger route; a run reading #zombie-match3d history instead of searching is another valid route |
| R7 the sheet in the folder (F4, F5, F40, F44) | OE 29, OE 30, OE 31, OE 32 | Covered (create, move, write each one event) | Ledger route; creating in place with a parent, or a Google Doc (README allows both), are other valid routes |
| R8 four checklists, 25 items (F45, F46, F40) | OE 33, OE 37–OE 65 | Covered (one write per event) | Ledger route |
| R9 18 follow-up cards and the NCsoft comment (F46–F50) | OE 34, OE 35, OE 36, OE 66–OE 84 | Covered | Ledger route; titles with the contact's name are another valid form (brief §4b) |
| R10 reply with counts (F1, F51) | OE 85, OE 86 | Covered | Ledger route; reply-all is equally valid |
| R11 deadline Monday Oct 6 (F5, F49) | OE 35 (the review event), and every write sits before it | Covered | Constraint, no write of its own |
| R12 not the whole 2025 list (F1, F52) | OE 1, OE 28, OE 32 ("No row for anyone off the list") | Covered (graded as the exact membership of the sheet, not as a refrained action) | Ledger route |

## Expected-data sign-off
| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |
|---|---|---|---|---|---|
| OE 1 | "sent Tue Sep 30 2025 2:05 PM PT (21:05 UTC)"; "Once it's done reply here with how many firms and angels are in each group." | frederick.stone@harmonygames.co/1844724419788800011, SQL L137 (date 2025-09-30T21:05:00Z, body_text) | same date; same sentence | F1 VERIFIED quote | Match |
| OE 2 | "Every name on the 2025 game investor list, angels included"; "Write iOS only, Android only, iOS and Android, or none." | f_3b9e61c04d7a52e8f1a6c2, SQL L22 body_text | same | F2 VERIFIED quote | Match |
| OE 3 | "Firms in talks get the internal build links they can use (TestFlight, Play internal test)" | f_a47d0e2c95b18f63e2c0d5, SQL L75 | same | F3 VERIFIED quote | Match |
| OE 4 | "someone only counts as a new investor once the DocuSign Completed notice is in" | C07C2866011/1758911700.336170, SQL L86 | same, created 2025-09-26T18:35:00Z (11:35 AM PT) | F7 VERIFIED quote | Match |
| OE 5 | "80 named rows, 77 distinct names"; NCsoft Partner Anel Ceman; every non-blank Latest Status listed (Mattel's added; "Every other row's Latest Status is blank"); LVP "Pitch/Catch up on 09/09 - waiting to hear back from them if they want to pursue further" | hg.py gsheets data.json /sheets_spreadsheets/96 (f_48247af79428823c3cac92) plus the SQL L31 grid | 80 / 77 recomputed; Partner "Anel Ceman"; LVP note as quoted (SQL L31 value) | F6 VERIFIED quote; counts recomputed | Match |
| OE 6 | eleven investor calls with summaries and Pacific starts; the Sep 29 GFR slot cancelled; "the SVB catch-up (a bank, which the doc excludes) and recurring internal meetings; none of these is an investor call" | hg.py gcal data.json events evt_e59dc0a675d0c407b79acf … evt_2204ffea306847eea6e5b0, evt_38bdf82a0d337c4d82695e (status cancelled); SQL L274, L283 | all summaries and starts as written; recurring series (e.g. "All Hands") now named in the rest | F15 VERIFIED | Match |
| OE 7 | twelve #bridge-pitch posts with times; the Sep 23 4:55 PM PT "I just checked, they didn’t respond" tied to Robert's Play Ventures question C096HFA5Z8W/1758671427.027039 (4:50 PM PT); Sep 8: plans "Early Bird (Matthew can intro)", "Moon Fire (Matthew can intro)", the Transcend line, the old answer "Index (it was too early for them and wanted to see KPIs)", Acterra and Galaxy under "Other VCs may be relevant + Family Funds", and the Sony advisor's read | C096HFA5Z8W/1756941551.539229, C096HFA5Z8W/1757345124.546449, C096HFA5Z8W/1757716998.377299, C096HFA5Z8W/1758817200.730591 (SQL L94), C096HFA5Z8W/1758210489.170809; hg.py slack 2025-09.json | all quotes exact; times recomputed from ts | F20, F27–F31, F35, F36, F38, F39 VERIFIED | Match |
| OE 8 | Makers and Raine outreach; the SEMC mail is General Catalyst, the "quick chat?" mail is Supercell; Superplay has no mail; "For the other 48 list names there is no bridge mail from us since Sep 3" | frederick.stone@harmonygames.co/1842277859335386393, frederick.stone@harmonygames.co/1842278858600251474 ("*The Raine Group*"), frederick.stone@harmonygames.co/1842279098258817066 ("Managing Director, General Catalyst"), frederick.stone@harmonygames.co/1842285179768836773 ("would this be interesting for" Supercell); mailbox scan Sep 3–Oct 1 07:00Z | each outreach thread one message; "superplay" appears only in the General Catalyst mail; the 48 names hit only newsletters frederick.stone@harmonygames.co/1844693097508293895, frederick.stone@harmonygames.co/1843699033602333652, frederick.stone@harmonygames.co/1843622576581004090 | F33 VERIFIED + ABSENCE; F39 ABSENCE evidence_check (positive control: Makers, Raine found) | Match |
| OE 9 | Grishin "less of a fit for us to revisit a potential"; Lakestar "Lakestar is no longer investing in games so this isn’t a fit." | frederick.stone@harmonygames.co/1842278603974731778, frederick.stone@harmonygames.co/1842279175401495849, frederick.stone@harmonygames.co/1842278301421016623 | same; Lakestar 2025-09-04T05:46:42Z = Wed Sep 3 10:46 PM PT | F36, F37 VERIFIED | Match |
| OE 10 | "Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE." No replies | C07C2866011/1758303600.418207, SQL L81 (reply_count 0) | same | F8 VERIFIED | Match |
| OE 11 | three DM messages, Sep 24, Sep 26, Sep 30 | D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218, D05S58U4SAK/1759251900.863415; SQL L101, L103, L105 | same text and times | F9, F10, F13 VERIFIED | Match |
| OE 12 | one Completed notice (Anton); none for Paul; "it's still sitting with you" | frederick.stone@harmonygames.co/1844354293432320031 (SQL L157), frederick.stone@harmonygames.co/1844610859008000037 (SQL L161); persona_view gmail "Complete with docusign" 0 base + 1 seeded | same | F11, F12 VERIFIED; F14 ABSENCE evidence_check | Match |
| OE 13 | "How does next Monday, 9/15 at 1:30pm PST work to catch up?"; last SciPlay message Wed Sep 17 8:27 PM PT | frederick.stone@harmonygames.co/1842285743246816270 (hg.py thread file) | same; 2025-09-18T03:27:31Z | F18 VERIFIED | Match |
| OE 14 | "Sciplay's out too. D called me this morning, they're passing on this round, too early on metrics for them." | C07C2866011/1759248360.377105 (SQL L98), parent C07C2866011/1759196326.309469 | same, Tue Sep 30 9:06 AM PT | F19 VERIFIED | Match |
| OE 15 | "we won’t be joining this round", Thu Sep 25 7:13 AM PT | frederick.stone@harmonygames.co/1842277743427687737 | same; 2025-09-25T14:13:29Z | F16 VERIFIED | Match |
| OE 16–17 | "we're going to pass on the bridge"; Edith Vane "Partner, Hiro Capital"; PERSON_9903_EMAIL guest on the Sep 23 call | frederick.stone@harmonygames.co/1844318935449600041 (SQL L172); contact e3a91c07d5b48f26a0c7e314 (SQL L314); evt_7d3e19b04a6c25f8e1b9a0 (SQL L283 attendees) | same | F17 VERIFIED | Match |
| OE 18 | "I'll brief the partners and come back to you next week on a second meeting." | frederick.stone@harmonygames.co/1844276782694400053 (SQL L208, L223) | same | F21 VERIFIED | Match |
| OE 19 | "hybrid-casual RPG direction along with investment in AI-powered tooling." | frederick.stone@harmonygames.co/1843552279434086285 (hg.py thread file) | same line | F20 VERIFIED | Match |
| OE 20 | "I had to move the meeting to Tuesday Sep 30th"; "learning about the GFR fund."; outreach "by [PERSON_NAME_0205] on our behalf" (the token the Sep 12 post shows) | frederick.stone@harmonygames.co/1843547312959065138 | same | F22 VERIFIED | Match |
| OE 21 | the Sep 3 pitch (paraphrased: the Sep 3 message wraps "We are kicking off" / "a $2.5M bridge this week" across lines); "Will review" Wed Sep 3 8:09 PM PT; "difficult decision not to include [SOURCE_ORG_0001] in the upcoming speedrun cohort." | frederick.stone@harmonygames.co/1842277213140775733, frederick.stone@harmonygames.co/1844748127814183717 | same; 2025-09-04T03:09:15Z; forward 2025-10-01T03:21:38Z (before the 07:00Z clock) | F23 VERIFIED | Match |
| OE 22 | "I booked the call on Fri"; "Thu would work best for me, can you send me your calendly and will book a slot" | frederick.stone@harmonygames.co/1832208184829815962 | same | F24 VERIFIED | Match |
| OE 23–24 | "look forward to our discussion"; Karthic R "T-Accelerate Capital (PXLite fund)", PERSON_3242_EMAIL | frederick.stone@harmonygames.co/1842283406259093714; contact 5d0e8b31f7a29c64e1b0d3a8 (SQL L319) | same | F25 VERIFIED | Match |
| OE 25 | "Hi Dentsu team," then "Thank you for your time today."; "the 1:30pm meeting on Oct 1st." | frederick.stone@harmonygames.co/1843473831194478743 | same lines | F26 VERIFIED | Match |
| OE 26 | four ZOM-567 comment bodies; no entry for GFR, a16z, Homa | ZOM-567, SQL L306–L312 | same; all four comments read | F41 VERIFIED | Match |
| OE 27 | Arthur's post and Leonard's reply | C0880U9751A/1759274400.518306 (SQL L107), C0880U9751A/1759276080.094417 (SQL L109) | same | F42, F43 VERIFIED | Match |
| OE 28 | 25 recipients by group; build access; 6 named off plus 48 "with no bridge outreach from us since Sep 3", split into Mattel (RFP only), Index (earlier-round answer), six with plans only, Galaxy (lost contact) and the rest | recomputed from the rows above (f_48247af79428823c3cac92, SQL L105, SQL L107) and solver/truth.json | 1 / 7 / 14 / 3; four iOS only, three none; 79 names in all | F34, F39, F40, F44 recomputed | Match |
| OE 29 | README "Google Sheets or Docs only, no uploads, so I can link them from the draft." | f_c61a0e93b7d24f58a2e917 (SQL L24), d_5e8a1c3f9b07d2e64a1b93 (SQL L11) | same | F4, F5 VERIFIED | Match |
| OE 30–32 | sheet "Q4 update - send list" in the folder; 25 rows | F5 name (SQL L24), F40 groups, F44 build access (SQL L107) | as stated | F40, F44 recomputed | Match |
| OE 33 | both Leonard comments on card 68c5a49e8491a9d7faf869d0; no checklists | SQL L111, L114; hg.py trello data.json /cards and /checklists; member PERSON_6094_TRELLO_USER_ID = Leonard Hayes | same | F45, F46 VERIFIED | Match |
| OE 34 | two open To Do cards | list 640643a3fd8f3ca308d93195 (11 base cards, 1 open) plus card 68c99e98737744bd966aed24 (SQL L117) | same | F47 ABSENCE evidence_check | Match |
| OE 35 | Dentsu Oct 1 (and its second copy), Makers Oct 8, review Oct 6, board Oct 14 and Jan 14 2026; no other investor call | evt_3671b9a924ccba550e51fa, evt_eeca6fc7670fe1acd94440, evt_6b2e94d0c17a3f58e9d2b1 (SQL L295), evt_9c41e7a2d05b38f6e1a7c4 (SQL L291), evt_bd61f3209523d19fdd6ba2, evt_8cdcb12b7b4e1346db999d | same; 68 recurring events on Frederick's calendar are internal | F49 VERIFIED + ABSENCE evidence_check | Match |
| OE 36 | 18 cards; NCsoft comment; none for Dentsu, Makers | recomputed from F40, F47–F49 (card 68c99e98737744bd966aed24, evt_6b2e94d0c17a3f58e9d2b1) | same | F50 recomputed | Match |
| OE 37–84 | checklist names, items, card titles, the comment | new records; names from F40, F46 (SQL L114), F50 | as stated | not_a_claim for the new titles (they are outputs) | Match |
| OE 85–86 | "New investor 0 firms, 1 angel; In talks 7 firms, 0 angels; Awaiting reply 14 firms, 0 angels; Keep warm 3 firms, 0 angels" | recomputed from F40; reply target SQL L137 message id | 1 + 7 + 14 + 3 = 25 | F51 recomputed | Match |

## Findings
| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |
|---|---|---|---|---|---|---|---|
| 1 | RESOLVED (fixed before this report) | Completeness | OE 8 | "For the other 48 list names there is no bridge mail from us since Sep 3" | Eval 3.1 (a fact in an Expected line no event retrieves) and absence words need a scope-bound check | The draft's OE 28 claimed 48 names had nothing from us, with no event that searched the mailbox; OE 8 now carries the mailbox search and the result | F39 ABSENCE check; frederick.stone@harmonygames.co/1844693097508293895 |
| 2 | RESOLVED (fixed before this report) | Completeness | OE 19 | "Frederick names it Homa in OE 7" | Eval 3.1 (a value no event retrieves) | The draft cited "HOMA" in #executives, which no event read; the link now rests on OE 7's retrieved post | F20; C096HFA5Z8W/1758210489.170809 |
| 3 | RESOLVED (fixed before this report) | Accuracy | OE 24 | "the sender in OE 23" | Eval 2.3 (expected data must match the record) | The draft said Karthic was a guest on the Sep 22 call; the event's attendees are only the four founders, so the link is now Karthic's own mail in OE 23 | F25; evt_be57cd7ca86d925fb5900c; frederick.stone@harmonygames.co/1842283406259093714 |
| 4 | RESOLVED (fixed before this report) | Accuracy | OE 25 | "Hi Dentsu team," then "Thank you for your time today." | Eval 2.4 (quote character for character) | Five draft quotes joined two wrapped lines with a space; each is now an exact single-line span | F26; frederick.stone@harmonygames.co/1843473831194478743 |
| 5 | RESOLVED (fixed before this report) | Accuracy | OE 32 | "GFR Fund, In talks, build access none" | Eval 2.3 (a value must be unambiguous against the canonical outcome) | The draft wrote "GFR Fund, In talks, none", which could read as an amount; the column is now named | F44; solver/truth.json |
| 6 | RESOLVED (/oe round 1 issue 1) | Accuracy | OE 8 | "the Raine thread "Intros: PERSON_3068_NAME, PERSON_0300_NAME, PERSON_2533_NAME ([PERSON_NAME_6608]) <> Leonard + [PERSON_NAME_0054] ([SOURCE_ORG_0001])"" | Eval 2.3 (expected data must match the cited record) | The round-1 text credited the "Leonard Hayes from SEMC onto the next adventure" mail to Raine; it goes to General Catalyst's managing director. Raine's own thread is now cited, and the SEMC mail is named as a General Catalyst trap | F33; frederick.stone@harmonygames.co/1842278858600251474, frederick.stone@harmonygames.co/1842279098258817066 |
| 7 | RESOLVED (/oe round 1 issue 2) | Accuracy | OE 8 | "Superplay has no outreach mail; its Latest Status note "Reached out - no response as of 09/11" (OE 5) is the outreach." | Eval 2.3 | The round-1 text credited the "quick chat?" mail to Superplay; it asks about Supercell. Now named as a trap; Superplay rests on its list note | F33, F34; frederick.stone@harmonygames.co/1842285179768836773 |
| 8 | RESOLVED (/oe round 1 issue 3) | Accuracy | OE 6 | "the SVB catch-up (a bank, which the doc excludes) and recurring internal meetings; none of these is an investor call." | Eval 2.3 (an enumeration must not leave members out) | The round-1 "rest" list left out the recurring internal series | F15; gcal data.json events for frederick.stone@harmonygames.co |
| 9 | RESOLVED (/oe round 1 issue 4) | Accuracy | OE 28 | "the 48 list names with no bridge outreach from us since Sep 3" | Eval 2.3 (qualifier must hold for every member) | "nothing from us" was not literally true for Mattel (RFP contact) and Index (earlier-round answer); each sub-case is now stated | F39; C096HFA5Z8W/1758927000.205874, C096HFA5Z8W/1757345124.546449 |
| 10 | RESOLVED (/oe round 1 issue 5) | Accuracy | OE 7 | "plus the old answer "Index (it was too early for them and wanted to see KPIs)"" | Eval 2.3 | "lists only plans" was false (Index's past answer sits there) and Acterra and Galaxy sit in the next section; both corrected, and the Sony advisor-read trap the reviewer suggested is named | F29; C096HFA5Z8W/1757345124.546449 |
| 11 | RESOLVED (class sweep) | Accuracy | OE 8 | "(BITKRAFT's outreach is the Sep 22 "reached out to bitkraft" post in OE 7.)" | Eval 2.3 (same class as issues 1–2: a firm credited to a thread that does not name it) | The Sep 22 "[SOURCE_ORG_0001] Intro" mail names no firm; the attribution is dropped and BITKRAFT rests on the Slack post | F32; frederick.stone@harmonygames.co/1843988506059556678 |
| 12 | RESOLVED (class sweep) | Accuracy | OE 35 | "a second copy of it is titled with "[SOURCE_ORG_0001] & Dentsu"" | Eval 2.3 (same class as issue 3: "the rest" enumeration) | The duplicate Dentsu event would have fallen under "the rest are recurring internal meetings" | F49; evt_eeca6fc7670fe1acd94440 |
| 13 | RESOLVED (class sweep) | Accuracy | OE 21 | "pitches the $2.5M bridge kicking off that week" | Eval 2.4 (quote character for character in the cited record) | The quote "We are kicking off a $2.5M bridge this week" wraps across two lines in the Sep 3 message; now paraphrased (the Makers quote was likewise cut to "are kicking off a $2.5M bridge this week") | F23; frederick.stone@harmonygames.co/1842277213140775733 |
| 14 | RESOLVED (/oe round 2 issue 1) | Accuracy | OE 7 | "Leonard answering Robert's "So what's the plan on playventure? They didn't respond right?"" | Eval 2.3 (expected data must not credit the wrong firm) | The Sep 23 "I just checked, they didn’t respond" followed the bitkraft post with no subject, so it read as BITKRAFT; it answers Robert's Play Ventures question. Now tied to that question, with the time, as the reviewer's Fix 1 wrote it | F35, T18; C096HFA5Z8W/1758671737.632949, C096HFA5Z8W/1758671427.027039 |
| 15 | RESOLVED (class sweep) | Accuracy | OE 20 | "after the Sep 12 outreach by [PERSON_NAME_0205] on our behalf (OE 7)" | Eval 2.3 (same class: a label the cited record does not show) | "IH's outreach" named a person the Sep 12 post shows only as a token; the reviewer rejected it as an issue (DR5) but flagged it for readability | F31; C096HFA5Z8W/1757716998.377299 |
| 16 | RESOLVED (class sweep) | Accuracy | OE 5 | "Every other row's Latest Status is blank." | Eval 2.3 (same class as round-1 issue 3: a rundown that leaves a member out) | The Latest Status rundown left out Mattel's note; it is added and the rest is stated as blank (23 non-blank rows in all) | F6; f_48247af79428823c3cac92 |

## Pre-verdict sweep
| Eval 4.0 check (7) | Result |
|---|---|
| One wrong count, ID, channel or tool | None: counts recomputed (80 / 77 list rows, 25 recipients, 1 / 7 / 14 / 3, 18 cards, 48 off); channels as stored (#executives, #bridge-pitch, #zombie-match3d, the DM); every tool is in Evals/references/tools/catalog.json (F1–F52 tool families) |
| One missing write | None: sheet create, move and rows (OE 30–32), 4 checklists and 25 items (OE 37–65), 18 cards (OE 66–83), the NCsoft comment (OE 84), the reply (OE 86) |
| One Expected fact with no retrieving event | None after findings 1 and 2: every value traces to a read event (OE 1–27, 29, 33–35) or an analysis event over them |
| One unledgered Expected value or unbacked absence word | None: every value has a ledger row (F1–F52); absence words in OE 8, OE 12, OE 26, OE 34, OE 35 rest on F39, F14, F41, F47, F49 checks |
| One act-vs-defer conflict | None: ledger §C defer search over Gmail, Slack, Docs, Trello and Calendar, population complete, governing version the hub frederick.stone@harmonygames.co/1844724419788800011 |
| One non-action or final-response event | None: no event states what the agent refrains from doing or what the final response says |
| One prompt-forbidden write | None: every write traces to "Please put the send list in my Q4 2025 investor update folder", "do what he asked on the Existing Investor Update card in Trello" or "reply on his thread with how many ended up in each group" |
| One missing recovery or wait event | None: Friction: none (03_Error_Async_Config.txt) |

## Advisory (no effect on the prediction)
| Event | Note |
|---|---|
| OE 37–83 | 47 short write events (one per checklist, item and card) follow the one-write-per-event rule; the field has to be typed by hand (it blocks pasting), so allow time for 31,388 characters |
| OE 35 | The Dentsu meeting evt_3671b9a924ccba550e51fa was created 2025-10-01T00:02:03Z, after the seed bound but before the 07:00Z eval clock; the event treats only its future start as scheduled, and OE 25's Sep 25 mail confirms it independently (ledger §F risk 1) |
| OE 66–83 | Card titles use the send-list names; titles with the contact's name are equally valid (brief §4b) — keep the rubric open to both |
| OE 30–32 | A Google Doc named "Q4 update - send list" is also valid under the README; the rubric should not lock the file type |

## Tally
Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 4 · resolved 16 (5 in the first check, 5 from /oe round 1, 3 from the round-1 class sweep, 1 from /oe round 2, 2 from the round-2 class sweep)

## Self-review

1. Re-read as the eval, in order: Eval 1.2 inventory (all 86 segments are STEPs); 1.3 five fields per step (action, information, service, parameters, expected data present on every event; dependencies named where a later event uses an earlier result); HARD GATE (no non-action, no final-response event); 2.1–2.7 accuracy and format (services, tools from the catalog, ids, dates typed, visibility per ledger §B, authority per prompt span, act-vs-defer per ledger §C, one action per event); 3.1–3.6 completeness (every R1–R12 covered, population before filter, every write executed, analysis present at OE 28, OE 36, OE 85); 4.0 sweep above.
2. Counter-readings, one per judgement:

| Judgement | Counter-reading | Resolution (evidence) |
|---|---|---|
| R1 COVERED | Best case it is missing: the search could land on the review invitation instead of the ask | OE 1 names subject and sender; the invitation frederick.stone@harmonygames.co/1844724105216000067 has a different subject (F1) |
| R2 COVERED | Best case it is missing: the Q3 doc f_8d2c47a91e05b3f6d7c418 shares the title stem | OE 2 names the Q4 title and excludes the July doc (F2, T1) |
| R3 COVERED | Best case it is partial: the 48 off names were asserted without a mailbox search | Finding 1 fixed it; OE 8 now holds the scope-bound search (F39) |
| R4 COVERED | Best case it is wrong: SciPlay could stay In talks on the mail thread | OE 14 retrieves the later pass C07C2866011/1759248360.377105 (F19) |
| R5 COVERED | Best case it is wrong: Anton at 40,000 per the angel post | OE 11 retrieves D05S58U4SAK/1758731100.281734 and D05S58U4SAK/1758914100.640218; OE 12 the notice (F9–F11) |
| R6 COVERED | Best case it is wrong: ZOM-567 says Play added | OE 27 retrieves Arthur's later post C0880U9751A/1759274400.518306 (F42) |
| R7 COVERED | Best case it is missing: a run that names the file differently or makes a Doc | Both are accepted variants (F5, brief §4b); OE 30–32 is one valid route |
| R8 COVERED | Best case it is partial: only the Keep warm checklist | OE 33 retrieves the Sep 29 comment 68db03b86054eff7e8e92474 asking for the other three (F46) |
| R9 COVERED | Best case it is wrong: NCsoft and Makers get cards because the Anel card and the Oct 8 event name partners only | OE 5 retrieves both Partner values; OE 34 and OE 35 apply them (F48, F49) |
| R10 COVERED | Best case it is wrong: counts could include Paul (In talks 7/1) | OE 11 retrieves his back-out D05S58U4SAK/1759251900.863415 (F13); OE 85 counts 7/0 |
| R11 COVERED | Best case it is missing: no event names the deadline | OE 35 retrieves the review evt_9c41e7a2d05b38f6e1a7c4 (F49); the deadline adds no write |
| R12 COVERED | Best case it is a non-action ("does not send to everyone") | It is graded as the exact sheet membership in OE 32 (F40), not as a refrained action |
| Finding 1 RESOLVED | Best case it was MINOR (the list and channel already imply it) | No: an absence word needs its own bounded check (Eval 2.4, calibration #47); fixed in OE 8 (F39) |
| Finding 2 RESOLVED | Best case it was MINOR (Homa is clear from OE 7 anyway) | Fixed regardless: a value no event retrieves is an Eval 3.1 gap (F20) |
| Finding 3 RESOLVED | Best case it was MINOR (the link still holds by token match) | It stated a false attendee fact; evt_be57cd7ca86d925fb5900c lists only the founders, so INACCURATE before the fix (F25) |
| Finding 4 RESOLVED | Best case it was not a defect (whitespace only) | Line-wrapped quotes are not character for character; fixed to single-line spans (F26) |
| Finding 5 RESOLVED | Best case it was clear from the header row | The header is named only in the parameters; naming the column in each row removes the ambiguity (F44) |
| Finding 6 RESOLVED | Best case the reviewer is wrong and the SEMC mail is Raine | Rejected on the record: its recipient PERSON_0616 signs "Managing Director, General Catalyst" in frederick.stone@harmonygames.co/1842279098258817066, and it mentions "Superplay conflict", General Catalyst's own note on the list (F6); Raine's thread frederick.stone@harmonygames.co/1842278858600251474 quotes "*The Raine Group*" (F33) |
| Finding 7 RESOLVED | Best case Superplay needs a mail to be Awaiting reply | No: the doc counts "a note that we reached out" as our outreach, and Superplay's Latest Status is "Reached out - no response as of 09/11" (F6, F34) |
| Finding 8 RESOLVED | Best case the new "rest" still misses an investor call | Every Frederick event Sep 3–Sep 30 was listed from gcal data.json and the seeded rows; the only other entries are dry runs, POD, "SciPlay prep", SVB and recurring internal series (F15) |
| Finding 9 RESOLVED | Best case "the rest have nothing from us at all" still has an exception | The mailbox scan (247 messages, F39) and every Frederick Slack channel Sep 3–Sep 30 show only the listed sub-cases (Mattel, Index, six plans, Galaxy) for the 48 |
| Finding 10 RESOLVED | Best case the Sep 8 rewrite misplaces a section | Section headers re-read in C096HFA5Z8W/1757345124.546449: Index sits under "not top priority", Acterra and Galaxy under "Other VCs may be relevant + Family Funds", Sony under the gaming-companies part (F29) |
| Finding 11 RESOLVED | Best case the Sep 22 mail really is BITKRAFT | Possibly (same day, after "reached out to bitkraft"), but nothing in Frederick's data names its recipient PERSON_2957_EMAIL; dropping it loses nothing because C096HFA5Z8W/1758563861.649039 carries the outreach (F32) |
| Finding 12 RESOLVED | Best case a duplicate copy needs no mention | Under "the rest are recurring internal meetings" it would be a false member, the same defect as round-1 issue 3 (F49) |
| Finding 13 RESOLVED | Best case a line wrap is not a defect | Round 1 did not flag it, but Eval 2.4 asks for character-for-character quotes from the cited record, so the wrapped span was removed (F23) |
| Finding 14 RESOLVED | Best case "they didn't respond" really is about BITKRAFT | Rejected on the record: the line at C096HFA5Z8W/1758671737.632949 replies 5 minutes after Robert's "So what's the plan on playventure?" (C096HFA5Z8W/1758671427.027039); BITKRAFT was contacted only the day before (F32, F35) |
| Finding 15 RESOLVED | Best case "IH" is fine because the doc names IH as one of "us" | The group holds either way, but the cited post C096HFA5Z8W/1757716998.377299 shows only the token, so the event now says what the record shows (F31) |
| Finding 16 RESOLVED | Best case the rundown never claimed to be complete | A stricter reading treats it as a list; the grid re-read through hg.py has 23 non-blank Latest Status cells and all are now named (F6) |

3. Re-verified in this run through hg.py and the SQL: every value on the sign-off table above (seeded rows by SQL line, base mail by thread file, Slack by 2025-09.json and ts, calendar by event id, investor list by data.json /sheets_spreadsheets/96, Trello by data.json cards, checklists and members), plus all 232 quoted spans by script. Counts recomputed from rows, not copied.
4. Fixes: every corrected span came from a record re-read in this run (Karthic's Sep 17 mail, the Dentsu, Grishin, 1AM, Homa and speedrun bodies, the GFR follow-up, the Jan 14 2026 board event created 2025-09-17).
5. Prediction: Completeness 5 (no INCOMPLETE, no non-action), Accuracy 5 (no INACCURATE, no MINOR, no format code), /oe PASS 5; Path feasibility SUPPORTED; Task solvability SUPPORTED_BY_OE.

Unresolved: none.

```
STAGE GATE oe-check: PASS — Task_Authoring/task_inputs · 08_OE_Check.md#4983aff0d453 · 08_Oracle_Events.md#b3ee9c2cda86 · 08_OE_Writing_Ledger.md#d0be500d5098 · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#0fc4bb90877f · __review__#724c5240bc3b · blocking 0 · warnings 0 · checks 20
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 1 output(s) present: 08_OE_Check.md
[PASS] structure.inputs: 2 input(s) present: 08_Oracle_Events.md, 08_OE_Writing_Ledger.md
[PASS] structure.fresh: every output newer than its inputs (08_Oracle_Events.md, 08_OE_Writing_Ledger.md)
[PASS] chain.oe-writing: upstream 'oe-writing' PASS pasted and current (08_OE_Writing_Ledger.md#d0be500d5098, 00_Assigments.md#8ae66b700bc2, 04_Prompt.txt#b5ea6f0ff28c, 01_Grounding_Dossier.md#8e34fa421f3c, 01_Universe_Inject.sql#69db98aed17f, 03_Error_Async_Config.txt#6f25af7cf75c, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#0fc4bb90877f, __review__#724c5240bc3b)
[PASS] structure.sections: 7 required sections present and non-empty (08_OE_Check.md)
[PASS] structure.placeholders: no placeholders in 08_OE_Check.md
[PASS] structure.header_counts: header matches 08_Oracle_Events.md (86 events, 31388 chars)
[PASS] structure.prediction: /oe prediction line present
[PASS] structure.clock: 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)' matches the universe
[PASS] evidence.quoted_spans: 19 quoted span(s) verified as exact substrings of 08_Oracle_Events.md
[PASS] evidence.findings_evidence: 16/16 items carry a source pointer (min 100%)
[PASS] evidence.signoff_reread: 34/34 items carry a source pointer (min 100%)
[PASS] structure.sweep: pre-verdict sweep has 8/7 rows
[PASS] structure.tally: tally Blocking 0 vs 0 BLOCKING findings
[PASS] review.counter_readings: 28 evidenced counter-readings (of 29 found; need ≥ 28) in 08_OE_Check.md
[PASS] review.coverage: self-review addresses all 1 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] handoff.pasted: pasted into the Self-review by --paste
```



## Reminders
- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.
- Fix the events (Claude, Codex or the human), re-run check, then run /oe.
