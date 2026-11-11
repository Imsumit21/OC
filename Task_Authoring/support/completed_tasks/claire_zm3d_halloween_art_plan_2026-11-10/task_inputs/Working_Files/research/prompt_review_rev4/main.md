# Eval 1 main review: Phase 2 (UGT, Clarity) and Phase 3 (Data Existence, Coherence)

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Universe_SynthCut. Persona: Claire Morgan, Art Lead.
Inputs: 04_Prompt.txt, 01_Universe_Inject.sql (all 252 statements parsed, none executed), 00_Task_Assigned_Inputs.md, 02_Universe_Date.txt.
Scope: Phases 2.1, 2.6, 3.1, 3.2 only. Other dimensions, Phase 5 passes and the saved-report writer were not run. Known-issue list: Task_Authoring/references/known_data_issues/synthcut.md.

## Scores

| Dimension | Score | Basis |
|---|---|---|
| Unique Ground Truth | 5 | 9 forks tested, every Reading B killed by a quoted prompt sentence or Claire-visible record; totals below come out as one answer. |
| Clarity & Specificity | 5 | Write actions are the same under every reasonable reading; no delegation ambiguity. |
| Data Existence | 5 | Every record the answer needs exists, is Claire-visible and has a cataloged read path. |
| Cross-Service Coherence | 2 (FAIL) | Four injected claims contradict base (C1 to C4 below). Non-Fail needs a single inconsistency, so this fails by count, not impact: none changes the Claire-visible answer. |

Ruthless standard (WORKFLOW.md, ruthless-grading-v1): the bar is evidence, not intent. A demonstrated inconsistency is scored where the rule puts it, even if no agent would trip on it (Eval 1 §3.2: this dimension "fails on the presence of an inconsistency itself"). It must not be inflated either: the UGT and Clarity scores stay at 5 because the hidden-side contradictions cannot move an answer built from Claire-visible records.

## Totals (58 ads: 56 on the Unity tab + ART-826 + ART-831)

| Call | Count | Tickets |
|---|---|---|
| Halloween version | 12 | ART-795, 797, 805, 808, 816, 817, 818, 819, 851, 852, 853, 854 |
| Skip | 10 | ART-806, 811, 813, 820, 821, 822, 824, 842, 844, 849 |
| Refresh first | 36 | all other live tickets |
| Reuse | 0 | none |

Date split (48 ads with a due date): Fri Oct 10 = 30, Wed Oct 15 = 18.
Maker split: Marcus 42 (26 on Oct 10, 16 on Oct 15), Julia 6 (ART-825, 827, 829, 830 on Oct 10; ART-826, 828 on Oct 15).
Oct 15 set: ART-805, 812, 816, 817, 818, 823, 826, 828, 832, 834, 843, 845, 847, 848, 850, 851, 853, 854.

Store: iPhone 6.5" set and Google Play phone set = Reuse, no ticket. App icon and iPad 12.9" set = new art, one ART ticket each, Martin, due Thu Oct 16 12:00 PT.
Shares: Leonard, Frederick, Martin, Marcus, Robert, Arthur (the six other attendees), commenter. Julia is not on the review and gets no share.
Out of scope: Archive tab ART-836 to ART-839, the KayKit props offer.

## Rule sources

| Topic | Source | Quote |
|---|---|---|
| Ask | #zombie_marketing, Leonard, Sep 30 22:05 UTC (df862615) | "go through everything that's live today and work out what gets a halloween version, what needs work first, what we already have, and who makes what by when" |
| Live set | same | "the live creatives sheet is what's running" |
| Makers | same | "Martin has the icon and the stills, Marcus has video and end cards" |
| Labels | Robert's deck, slide 4 | "Halloween version: dress it from the current art. Refresh first: re-capture, re-render or re-cut before any seasonal pass. Reuse: it already has a seasonal version, use that one. Skip: no seasonal version this time." |
| Build rule | deck, slide 2 | "Anything captured or rendered from a build older than Android #1452 / iOS 1232 ... is redone on the current build first. If a later capture has replaced it, the newest capture is the one that counts." |
| Music rule | deck, slide 2 | "A video whose master has the music baked in is re-cut first from a master without music (re-export one from the project if there is none)" |
| Plan | Frederick mail, Sep 30 23:10 UTC | "don't make Halloween versions of anything that only runs there"; "every Halloween ad needs to be with me by Wed Oct 15, not the 17th" |
| Android date | #zombie-match3d thread reply, Sep 30 23:42 UTC (ca1f761b) | "any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th." |
| Store dates | Arthur's calendar | "new iOS screenshots go up with the Oct 17 submission and are due by the same Oct 16 12:00 PT cut"; "Oct 17 submission: the last build that can carry Halloween changes"; "Nov 6 submission: post-Halloween clean-up (icon and screenshots back to normal)" |
| Tickets | #zombie-art, Leonard, Sep 30 15:47 UTC (b041f2ed) | "whatever is already exported is done so no tickets needed for those, tickets are just for store art that still has to be made" |

## Decision sweep

Scope:
- 56 Unity rows plus two off-sheet ads. ART-826: Frederick on the Halloween push card, Sep 30 23:20 UTC, "It never made it onto the live creatives sheet, so count it in for Halloween." ART-831: ticket comment, Sep 29, "Still running on Unity: Android US phone (checked Sep 29). Not on the live creatives sheet yet."
- The 62 injected tickets split exactly: 56 on the sheet, 2 off-sheet live, 4 Archive (Canceled). No ticket title or format differs from its sheet row, and no ticket lists two different placement sets.
- "Every ad we're running" stops at Unity. Frederick, #zombie-match3d Sep 30 16:04 UTC: "We are only running the retention campaigns." Leonard also turned off the FB campaign on Sep 26, but that is in a DM Claire cannot read, so it is corroboration only.

Skip (10): placement is Android US tablet only. ART-811 and ART-813 become tablet-only through Frederick's Sep 29 mail: "I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time ... Both stay on Android US tablet." That is newer than ART-811's "(checked Sep 9)" comment.

Halloween version (12):
- Later capture replaces an old one: ART-795 (#1935), 797 (#1966), 805 (#1896), per Marcus in #zm-animations Sep 25 "they replace the april captures on ART-795, ART-805 and ART-797". ART-808 and 816 (#1896, ticket comments Sep 16). ART-851, 852 (#1896), 853 (#1935), 854 (#1966).
- Current and SFX-only: ART-817, 818, 819 (#1630).

Refresh first (36):
- Older than #1452 by number or date: ART-793, 794, 796, 798 to 804, 807, 810, 812, 814, 815, 823, 825 to 830, 832, 840, 841, 843, 845, 846, 847, 850, and ART-831 (#1450, Jul 29, two builds short of the cut).
- Music baked on a current build: ART-809. The ticket points to the Aug 13 thread, where Frederick says "the background music is baked in".
- Trello comment, Sep 26: "end card 001 still has the old zombies on the packs ... Same on the 16:9, 1:1 and 4:5 cut from it ... they need a re-render before anyone builds on them." ART-833, 834, 835, 848.
- Build-less dates checked against #builds: Android #1427 ran Jul 28 17:13 UTC, #1452 ran Jul 29 20:18 UTC, so a Jul 28 capture (ART-840) is older.

Due dates: any Halloween or Refresh ad on Android US phone = Oct 10; otherwise Oct 15. iOS UK tablet + Android US tablet ads are Oct 15, because the tablet campaign is out of the flight.

Makers: videos and end cards = Marcus, including the ones "Made by Frederick", "Made by Leonard" and ART-832 "Made by Martin Walsh". Statics = Julia.

Store: Drive folder ZM3D Halloween 2025 / Store holds 5 iPhone65 files and 6 GooglePlay_phone files, no iPad file and no icon.

## UGT two-reading table

| # | Fork | Reading A | Reading B | Ruled out by |
|---|---|---|---|---|
| 1 | Statics maker | Julia, 6 ads | Martin, per "Martin has the icon and the stills", working before he leaves | #company-internal, Martin Sep 30 14:41 UTC: "I'll be on vacation Oct 6-15. <@Julia> takes the ad statics while I'm out, store art stays with me." Leonard 23:31 UTC, newer than his own 22:05 message: "julia on the ad statics works for me". All six due dates sit inside Oct 6-15. |
| 2 | ART-809 | Refresh first (re-cut) | Halloween version, because Marcus exported a no-music master that evening | Slide 2 says the ad "is re-cut first from a master without music", so a no-music master existing is the input to the Refresh, not its completion. No record shows the live 9:16 was re-cut (compare ART-808's explicit re-capture comment). |
| 3 | Cheer fastcouch 9:16 and 16:9 | Halloween version from the Sep 16 capture | Reuse Marcus's Sep 29 test, or Refresh first | Robert Sep 30: "We can't ship these, they need doing again from the Sep 16 one". Slide 2: "the newest capture is the one that counts", and #1896 is past the cut, so nothing needs refreshing. |
| 4 | Dual iOS UK + Android US phone ads | Oct 10 | Oct 15, or split by platform | "any new ad going on Android US phone has to be with me by Fri Oct 10" |
| 5 | Squirrelfail and mrfluffernot landscape | Skip | Halloween version from the ticket's iOS UK tablet placement | Frederick's Sep 29 mail, newer than the ticket. |
| 6 | App icon | New art, ticket, Oct 16 12:00 PT | Reuse the Sep 17 concept, or swap around the 24th | Robert Sep 17: "Nice for an event, but not for the app icon". Arthur: "the last build that can carry Halloween changes" and "icon and screenshots back to normal" on the Nov 6 submission, so the icon rides a submission. A Google Play listing swap on the 24th would not change the ticket date, since iOS needs the same art by the cut. |
| 7 | iPad 12.9" set | Ticket, Martin, Oct 16 12:00 PT | Done, per Martin's "halloween store screens are exported" | Store folder has no iPad file. Leonard: "whatever is already exported is done". |
| 8 | Store art date against Martin's leave | Oct 16 12:00 PT | Fri Oct 3, before he leaves | Arthur states the date: "due by the same Oct 16 12:00 PT cut". Martin keeps the work: "store art stays with me". Reading B is a planning buffer with no record; a good plan flags it, but it is not the due date. |
| 9 | Share list | Six attendees | Add Julia, or use the folder's five people | Prompt: "shared with everyone on the review". Event attendee list includes Arthur, excludes Julia. |

Verdict: PASS (5). No BOTH_FAIR_FIGURE needed. Edge values tested: Oct 15 inclusive of Martin's leave (ART-826, 828 stay Julia); #1450 against #1452; Jul 28 against Jul 29; before and after each later correction.

## Clarity

Write actions under every reasonable reading: 1 doc and 1 sheet in Claire's Drive, 12 share grants, 58 ticket comments, 48 assignments, 2 new ART tickets, 1 thread reply. "The ones that need new work" could at a stretch mean Refresh-first only, but Leonard's text ties it to "so Frederick can queue the uploads", and a Halloween version is also made new, so all 48 are assigned. "I'm walking everyone through it" is Claire's own act and is not delegated. Score 5.

## Data Existence

| Need | Record | Claire visible |
|---|---|---|
| Leonard's message | Slack C06DJBJL798 (member) | Yes |
| Sheet, calendar, deck | Drive-family, Claire in shared_with | Yes |
| Halloween folder | d_272d849cde40c35980a433, Claire writer | Yes |
| UA mails | Claire's mailbox copy | Yes |
| Oct 10 reply, Martin's leave, re-records, Robert's replies | #zombie-match3d, #company-internal, #zm-animations, #zombie-art (all member) | Yes |
| Capture and placement notes, ticket writes | Linear (unscoped), Julia, Martin, Marcus all on team_ART | Yes |
| Trello comments | Unscoped | Yes |
| Review attendees | Claire's event copy | Yes |
| Build dates | #builds C05433XK267 (member) | Yes |

No Claire channel_leave in these channels. Every injected Slack author is a member of the channel. persona_view check-sql: Claire's copies all YES; the 24 NO rows are other people's mailbox copies. Catalog covers every read and write, including gdrive_share_file, linear_create_comment, linear_update_issue, linear_create_issue and slack_send_message with thread_ts. Evidence limit: return shapes are not in the catalog, so whether create calls return a link is not established. Score 5.

## Cross-Service Coherence findings

All four are injected claims read against base. None changes an answer built from Claire-visible records, so UGT stays at 5. Fail by count: the form allows Non-Fail only for a single low-impact inconsistency (Eval 1 §3.2).

**C1. ART-841 and ART-850 capture note contradicts what boris alin2 is (Cross-service Referential). Could flip two calls.**
- Injected: ART-841 cmt_art841_1 "Captured from Android #1427 on Jul 28. Master: SFX only, no music." ART-850 cmt_art850_1 says the same. Deck slide 2 puts anything before #1452 ahead of "the zombie swap", so these read as old zombies and take Refresh first.
- Base, Slack DM D05S58U4SAK (Frederick and Leonard, not Claire), 2025-09-11: Leonard 19:39 "you have the old zombies", 19:40 "I think he created many scenes with the new zombies"; Frederick 19:47 "I want to run [PERSON_NAME_52459] --> old zombies vs [PERSON_NAME_52459] --> Marcus"; Frederick 21:33 "[PERSON_NAME_52459] --> Marcus" with file boris_alin2_9-16_blur-VEED.mp4. An alin2_9-16_blur-VEED cut already existed on Aug 17 (same DM, 22:36).
- Effect: if the DM is right, the footage is Marcus's new-zombie cut, past the zombie swap, and the two ads are not Refresh first on build. Claire cannot open the DM, so the ticket decides for her and totals stand at 36/12.
- Missing: a capture note on ART-841 and ART-850 that matches Marcus's footage. Changing it re-derives both calls, so totals can move by up to 2.

**C2. "Android US" campaigns have no base support (Cross-service Referential).**
- Injected: sheet Read me "Android US phone, Android US tablet"; Frederick's mails; ticket placements; the Oct 10 reply.
- Base, #executives (not Claire): Frederick 2025-07-11 22:11 "Currently, we can only run retention campaigns in Netherlands"; 2025-07-25 19:45 "So we should just get installs from Netherlands and Sweden"; 19:51 "if we do run US, every install we get will get us 1 install closer to being able to turn on US retention campaigns". Leonard 2025-09-28 17:00 posts a dashboard link filtered country=Netherlands&country=Sweden, then 17:01 "country filter no source filter previous 24 hours on Android says 24 first time app opens - out of those 24 15 shows up as Unity".
- Snowflake INSTALL_EVENTS (Claire can read; install counts are safe under SC-11), six sampled dates in September, Android unity_ads rows: GB 49, US 8, SE 5, DK 2, NL 1. Attributed campaign unity_ads_GB_zombie_match_3d dominates.
- Against: Confluence Product OKRs says "US-only from April 2025", already flagged by SC-28. Base disagrees with itself, and no record shows a US Android retention campaign.
- Effect: none on calls or dates, since the injected label is used uniformly.
- Missing: a base-consistent campaign name, or an injected record saying the Android retention campaign moved to the US.

**C3. "#1630" capture note is later than the footage it describes (Temporal, minor).**
- Injected: ART-809 "Captured from Android #1630 on Aug 13"; ART-817, 818, 819 the same.
- Base: #zombie_marketing Marcus 2025-08-13 18:42 UTC "Investor Facing Video. Final version"; #builds Match3D Android #1630 started 19:00 UTC. D05UDNHAPL2 Frederick 17:18 "I'm gonna try to slice up your video for investors". Frederick's cut, posted 19:40, is a slice of a video finished before that build existed.
- Effect: none, since any August build is past #1452. Date-slip rule scores it as minor.

**C4. "Store sets have no ART ticket" against ART-790 and ART-792 (Semantic, minor).**
- Injected: sheet Read me "Store sets have no ART ticket."
- Base: ART-790 "Updated ZM Marketing Screenshots" and ART-792 "ZM3D - Marketing Screenshots round 3", both Martin. #zombie_marketing 2025-08-28 Martin "New concept for marketing screens", Leonard "Will roll it out at the next release".
- SC-16 covers these tickets' status, not this claim. Effect: none, because Leonard's rule sets what gets a ticket.

**Unresolved, not scored.** Ten tickets say "Still running on Unity ... (checked Sep 9)" and 22 rows say "Live since Sep 9". Slack suggests UA was off: Robert 2025-08-22 "Yeah we can pause"; Leonard #zombie-match3d 2025-09-11 03:31 "when it's approved we'll start buying users at small scale" (Claire-visible); #executives 2025-09-12 "we are ready to turn on campaigns"; #random 2025-09-27 "Unity Android campaign is live already" (Claire-visible). Snowflake disagrees: unity_ads installs on Sep 5, 9 and 10 run 17, 18 and 21 a day before jumping to 76 on Sep 13. Base conflicts with itself here, so this is not a demonstrated injection defect. Moving the checks to the restart, as ART-831 already does with "checked Sep 29", would remove the question.

**Checked and cleared.** Sheet against all 58 tickets (titles, formats, placements). Ticket lifecycle: no comment after completed_at or updated_at; Canceled tickets match Archive dates. Slack reply counters and author membership. Build numbers and dates against #builds (#440 through #1966, iOS #1232). Weekdays of all quoted dates. Trello authors. Trello card and board activity dates. Vacation and leave: no base record for Marcus or Julia in October. App Store sets "Live since Sep 17" against #zombie-match3d 2025-09-17 15:48 "it's under review": same-day approval is possible, so not demonstrated. SQL apostrophes parse clean and all column counts match.


## Closest UGT calls

1. ART-809 (fork 2). Closed by slide 2 wording plus the absence of any re-cut record. The risk is a solver reading the thread's last messages as the fix.
2. Store art date against Martin's leave (fork 8). Closed because Arthur's doc states the date, but the noon cut on his first day back is a real planning risk the plan should flag.

## Method notes

- Rule deviation: the brief limits base search to hg.py, with raw exports for whole channels. I used hg.py for Slack term searches, Confluence and Snowflake, but also read raw JSON directly for Linear, Trello, GDrive and GCal lookups and scanned Slack messages across channels with my own scripts. Findings cite the records, which can be re-read through hg.py.
- Snowflake figures are a sample: all 225 INSTALL_EVENTS rows on Sep 5, 9, 10, 13, 28 and 29, read through hg.py. All are zombie_match_3d. Not a full-month count.
- Not opened: Evals/task_inputs, review_r4/prev, Task_Authoring reports or plans, the learnings file. SQL was parsed, never executed.
- Injection gate not run (the brief excludes the saved-input store).
- out/ also holds files from other reviewers (for example injection.md, p1.md). I did not open them, so this review stays blind.
