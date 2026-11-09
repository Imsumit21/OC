## Self-review

Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R13), every write family (sheet, note, comments, moves, new tickets, checklist, emails, DM), the three told counts, every exclusion (the decoys and second tickets, as exact counts on the required writes; Leonard, as the count of people emailed) and the ordering ask ('When it's all finished') has a row on the correct artifact. No row grades the final response; the DM is the deliverable the prompt names. The /oe report's 'No Process row is needed' speaks to reads; the prompt's ordering ask still needs its one row, which no Outcome can show.

Re-verified: every source value in 00_V3_Authoring_Evidence.json was read in this run by plan/rubric/build_rubric.py: seeded rows by parsing 01_Universe_Inject.sql (never executed), base records through hg.py get-many (GitHub review comment 599, Trello cards 705 and 802, Confluence page 27, Contacts, Snowflake table 10 rows 236 and 237). Every quote in a row's evidence is asserted against its record at build time. Counts were recomputed from solver/truth.json (36 rows, 32 existing tickets, 24 Backlog, 6 Canceled, 5 new tickets, 2 Go items, 8 people, Go 2, Hold 28, Drop 6). Limits of the V3 sidecar, not of the rows: the gate's lookup for unscoped services reads base data only, so seeded Linear tickets (DES-313 to DES-345) are named in each row's evidence text and the sidecar cites the rule doc, the DM or a base ZOM ticket; the Snowflake rows have no timezone-aware field, so the sidecar cites the DM, and the build asserts the four values on rows 236 and 237.

Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (Gmail, Slack, Calendar and Drive records pasted YES under Visibility proof; Linear, Trello, GitHub, Confluence, Snowflake and Contacts unscoped), each write exists in the catalog (ledger §C), no row needs a rate-1.0 retry and no evidence sits outside Samuel's view. Count on the four bases: 0. The local grade below shows 30 rows (140 weight) failing all six baselines: all rest on the four comment asks, each reachable through OE 9 to OE 13 (updatedAt, then each ticket's comments). They are discovery failures, not impossible targets, and /create-allfail must prove that route (ledger §F 1 and §F 3).

Local baseline grade (plan/rubric/grade_baselines.py over the six rev6 trajectories; a local estimate of the verifier, not its result):

```text
rows 153 weight 583
scores [74.3, 74.3, 58.0, 65.7, 76.0, 74.3] mean 70.4 popSD 0.065 pass rows [121, 121, 102, 111, 123, 121]
precheck 64.8
patterns 4 largest 0.5
varying rows 27
```

Shortcut and diversity: the §F probe hits are dispositioned below the paste. The largest units of discovery are the rule doc (F2) and the parent DES-314 (F4), upstream of every call by construction — see Unresolved.

Surface dispositions: ten slots are dispositioned. X2b, X6b, X8b and X21b are reasons on ticket comments: the DM asks to 'Leave the call as a comment', and the reason is already graded in the sheet and the note. X11, X12, X11b and X12b are sheet Call cells whose call is graded on the ticket and in the email; their rows are graded by What's missing. X18 and X19 are per-ticket moves the round-1 Fix List cut to keep the Backlog samples at five.

Brief §4b: two acceptances are narrowed. §4b lets Todo pass on the four Done Holds; the rows require Backlog, because OE 98 to OE 101 say so, /oe passed that reading, and a row accepting Todo would pass a wrong state (overly_broad). §4b and ledger §F 6 let the call sit in a new ticket's description; the rows require a comment, because the DM says 'Leave the call as a comment on each ticket' and OE 50, 52, 54 and 56 are comments. No run is affected: all seven moved those tickets to Backlog when they held them, and none reached the new tickets.

Platform /rubric round 2 (2026-11-06, FAIL 1, reviewed sha d1cbadf710e9, coverage 153/153): every checked fix is copied word for word, by assertion. R21 is the author's rewrite the report asks for: the cell must identify Lapsed 7 days, the bare name passes, the client's and Leonard's names and any other wording that identifies it pass, and a cell naming only the Weekly Leaderboard batch fails, because that batch also fires on day 14 and is a Hold. The code call site was re-read in the PR #248 hunk and in run-5's file read. R121 is left locked, though its name list lacks the client's 'Lapsed last session reminder' (the report's note for QM): editing it would unlock a row that passed.

Platform /rubric round 1 (2026-11-06, FAIL 1, reviewed sha 3911b7d5f4de, coverage 154/156): every Fix List item is applied word for word, checked by an assertion that each title sits in the report and that each row lands at its 'cand.' number. 113 of the 149 rows are byte-identical to the reviewed JSON, so DELTA keeps them locked. Local edits made after that build (sha 6dc1d728a183, from two blind reviews) were set aside, so no row changes that the report did not name; they are stored in run_forensics/rev6/rubric_r1/. The five 'not scored, worth doing' items are applied to supporting fields only.

Counter-readings, one per section A row:

| P | Counter-reading (a valid answer that could fail · a wrong answer that could pass) and resolution (evidence) |
|---|---|
| P1 | Counter-reading — (a) a sheet created in the root and moved in passes, the title says so · (b) a sheet left outside d_caafeec2804b3a67ce46aa fails on its final parent |
| P2 | Counter-reading — (a) another letter case or column order passes · (b) a dropped What's missing fails against D06L58XCVKK/1759264851.763895 |
| P3 | Counter-reading — (a) a row named by the sheet's or the ticket's name counts once · (b) 32 rows (no comment asks) fail, and a 37th for a red dot fails; the rule doc f_dc45e0e5a8b8635c1b82b2 defines a message as what reaches a closed phone |
| P4 | Counter-reading — (a) either name passes, in any wording · (b) a blank Message cell fails; PN sheet f_a325dd4af80afc5994d5dc row 4 and DES-316 |
| P5 | Counter-reading — (a) none: test 6 fails once Vincent's tick is off, and the row's name 'Full Ammo' is the same message · (b) Go from the Sep 24 pass fails against C0880U9751A/1759245146.720608 |
| P6 | Counter-reading — (a) none: Vincent scratched iOS, so test 6 fails · (b) Go from the checks sheet's Sep 24 pass fails against D06UFE81RF0/1759174846.723833 |
| P7 | Counter-reading — (a) none: test 5 fails on Arthur's comment · (b) Go from Ready, Done and Vincent's pass fails against harmonygames-Games/match3d#248#rc_18 |
| P8 | Counter-reading — (a) none: 'It fails only if none of them count', and none do · (b) Go from the settings-toggle pass fails against C0880U9751A/1759167608.326578 |
| P9 | Counter-reading — (a) none: all six tests pass · (b) Hold because Full Ammo went missing on 0.3.49 fails: Vincent says 'the lapsed ones are still coming through' (C0880U9751A/1759245146.720608) |
| P10 | Counter-reading — (a) none: a line change is a String change, not a Hold · (b) Hold for the new line fails against rule doc f_dc45e0e5a8b8635c1b82b2 |
| P11 | Counter-reading — (a) the row may use the sheet's or the ticket's name, so it is found by its Ticket cell · (b) Any other call on that row fails. Record: 6851a7a6c31a93809acded72 |
| P12 | Counter-reading — (a) the row may use the sheet's or the ticket's name, so it is found by its Ticket cell · (b) Any other call on that row fails. Record: 68c45bba5d2c25a3a5c26a8c |
| P13 | Counter-reading — (a) the row may use the sheet's or the ticket's name, so it is found by its Ticket cell · (b) Any other call on that row fails. Record: page_liveops_calendar |
| P14 | Counter-reading — (a) none: the weekly batch covers day 14, so the rule makes it a Drop · (b) Hold as new work fails against the cancellation mail and DES-344 (rule doc f_dc45e0e5a8b8635c1b82b2) |
| P15 | Counter-reading — (a) the row may use the sheet's or the ticket's name, so it is found by its Ticket cell · (b) Any other call on that row fails. Record: DES-322 |
| P16 | Counter-reading — (a) the row may use the sheet's or the ticket's name, so it is found by its Ticket cell · (b) Any other call on that row fails. Record: DES-321 |
| P17 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A blank cell, or any other test, fails. Record: C0880U9751A/1759245146.720608 |
| P18 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A blank cell, or any other test, fails. Record: D06UFE81RF0/1759174846.723833 |
| P19 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A blank cell, or 'passes all six', fails. Record: f_dc45e0e5a8b8635c1b82b2 |
| P20 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A blank cell, or test 6, fails. Record: C0880U9751A/1759167608.326578 |
| P21 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A cell that names no covering message fails. Record: f_a325dd4af80afc5994d5dc |
| P22 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A sheet with no row for this ask fails; so does a row naming another test. Record: ZOM-542 |
| P23 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A sheet with no row for this ask fails; so does a row naming another test. Record: ZOM-556 |
| P24 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A sheet with no row for this ask fails; so does a row naming another test. Record: ZOM-563 |
| P25 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A sheet with no row for this ask fails; so does a row naming another test. Record: ZOM-483 |
| P26 | Counter-reading — (a) any wording naming that gap passes, with or without the test number · (b) A blank cell, or test 3, fails. Record: DES-335 |
| P27 | Counter-reading — (a) a plain rewording passes (brief §4b) · (b) A different group fails; a plain rewording passes. Record: DES-330 |
| P28 | Counter-reading — (a) a plain rewording passes (brief §4b) · (b) A different group fails; a plain rewording passes. Record: DES-335 |
| P29 | Counter-reading — (a) a plain rewording passes (brief §4b) · (b) A different group fails; a plain rewording passes. Record: DES-318 |
| P30 | Counter-reading — (a) a plain rewording passes (brief §4b) · (b) A different group fails; a plain rewording passes. Record: DES-313 |
| P31 | Counter-reading — (a) a plain rewording passes (brief §4b) · (b) A different group fails; a plain rewording passes. Record: ZOM-563 |
| P32 | Counter-reading — (a) 'DES-313 Ping when a Collect & Win window opens' passes · (b) a new key fails: DES-313 exists (Confluence page_liveops_calendar) |
| P33 | Counter-reading — (a) a key with a title passes · (b) Another key fails. Record: DES-317 |
| P34 | Counter-reading — (a) the new key alone or with a title passes · (b) ZOM-563 in the cell fails: the comment's ticket is not the message's ticket (OE 58) |
| P35 | Counter-reading — (a) with or without an emoji passes · (b) 'Your Squad Needs You Back' fails: evt_f2c03e69f50acf62c9d1c3 says it replaces the art-thread line |
| P36 | Counter-reading — (a) with or without its emoji passes (rule doc: emoji don't count) · (b) another line fails against f_a325dd4af80afc5994d5dc row 4 |
| P37 | Counter-reading — (a) 'Yes - DES-346', or the key alone, passes: the DM names the column but sets no Yes/No form · (b) No fails: the client ships a different line (harmonygames-Games/match3d#248) |
| P38 | Counter-reading — (a) 'None - client already ships this line' passes, as in run-4 · (b) Yes fails: emoji don't count (f_dc45e0e5a8b8635c1b82b2) |
| P39 | Counter-reading — (a) n/a or a dash on the other rows passes, and the row reads the sheet's own Go rows, so a wrong Go is judged on its own call row · (b) a headline on a Hold row fails against rule doc f_dc45e0e5a8b8635c1b82b2 ('only for Go rows') |
| P40 | Counter-reading — (a) n/a or a dash on the other rows passes · (b) 'No' down all 36 rows fails against rule doc f_dc45e0e5a8b8635c1b82b2 ('only for Go rows') |
| P41 | Counter-reading — (a) any row order passes · (b) run-3's four Go fail; the rule doc f_dc45e0e5a8b8635c1b82b2 sets a Go at all six tests |
| P42 | Counter-reading — (a) a note moved in passes · (b) a note left elsewhere fails on d_caafeec2804b3a67ce46aa |
| P43 | Counter-reading — (a) any layout passes; all seven runs wrote 364 to 711 words · (b) a multi-page note fails; the prompt says 'the one-page note' (D06L58XCVKK/1759264851.763895 repeats it) |
| P44 | Counter-reading — (a) a title or lead-in first passes, as in run-5 · (b) Holds before the lapsed reminders fail against D06L58XCVKK/1759264851.763895 ('start with D1 and D7', 'then the lapsed reminders') |
| P45 | Counter-reading — (a) rounded to one decimal, with or without %, passes (brief §4b) · (b) The other platform's figure, a pooled figure or another cohort week fails. Record: wh_USER_COHORT_RETENTION rows 236 and 237 |
| P46 | Counter-reading — (a) rounded to one decimal, with or without %, passes (brief §4b) · (b) The other platform's figure, a pooled figure or another cohort week fails. Record: wh_USER_COHORT_RETENTION rows 236 and 237 |
| P47 | Counter-reading — (a) rounded to one decimal, with or without %, passes (brief §4b) · (b) The other platform's figure, a pooled figure or another cohort week fails. Record: wh_USER_COHORT_RETENTION rows 236 and 237 |
| P48 | Counter-reading — (a) rounded to one decimal, with or without %, passes (brief §4b) · (b) The other platform's figure, a pooled figure or another cohort week fails. Record: wh_USER_COHORT_RETENTION rows 236 and 237 |
| P49 | Counter-reading — (a) 'Day 1, then days 7, 14, 21 and 28' in any layout passes, and the race and leaderboard may sit beside them · (b) stopping at day 7 fails against harmonygames-Games/match3d#248 |
| P50 | Counter-reading — (a) any of the listed names passes, in any layout · (b) Leaving it out, or calling it ready, fails. Record: C0880U9751A/1759245146.720608 |
| P51 | Counter-reading — (a) any wording naming the gap passes, with or without the test number · (b) Leaving it out, or calling it ready, fails. Record: C0880U9751A/1759245146.720608 |
| P52 | Counter-reading — (a) any of the listed names passes, in any layout · (b) Leaving it out, or calling it ready, fails. Record: D06UFE81RF0/1759174846.723833 |
| P53 | Counter-reading — (a) any wording naming the gap passes, with or without the test number · (b) Leaving it out, or calling it ready, fails. Record: D06UFE81RF0/1759174846.723833 |
| P54 | Counter-reading — (a) any of the listed names passes, in any layout · (b) Leaving it out, or calling it ready, fails. Record: DES-320 |
| P55 | Counter-reading — (a) any wording naming the gap passes, with or without the test number · (b) Leaving it out, or calling it ready, fails. Record: f_dc45e0e5a8b8635c1b82b2 |
| P56 | Counter-reading — (a) any of the listed names passes, in any layout · (b) Leaving it out, or calling it ready, fails. Record: C0880U9751A/1759167608.326578 |
| P57 | Counter-reading — (a) any wording naming the gap passes, with or without the test number · (b) Leaving it out, or calling it ready, fails. Record: C0880U9751A/1759167608.326578 |
| P58 | Counter-reading — (a) the four named in any order pass, a caveat beside them is harmless · (b) three, with Plague Race passed as Go, fail; solver/truth.json holds four |
| P59 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-313 |
| P60 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: C0880U9751A/1759245146.720608 |
| P61 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: f_8eb8c04713ff6a6ef4a265 |
| P62 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: f_8eb8c04713ff6a6ef4a265 |
| P63 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: C0880U9751A/1759167608.326578 |
| P64 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: D06UFE81RF0/1759174846.723833 |
| P65 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-320 |
| P66 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-321 |
| P67 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-322 |
| P68 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-323 |
| P69 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: 68c45bba5d2c25a3a5c26a8c |
| P70 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: page_liveops_calendar |
| P71 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: page_liveops_calendar |
| P72 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: 6851a7a6c31a93809acded72 |
| P73 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-328 |
| P74 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-329 |
| P75 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-330 |
| P76 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-331 |
| P77 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-332 |
| P78 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-333 |
| P79 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-334 |
| P80 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-335 |
| P81 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-336 |
| P82 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-337 |
| P83 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-338 |
| P84 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-339 |
| P85 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-340 |
| P86 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-341 |
| P87 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-342 |
| P88 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-343 |
| P89 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: f_dc45e0e5a8b8635c1b82b2 |
| P90 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A comment giving another call fails; so does no comment. Record: DES-345 |
| P91 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A new ticket with no comment, or no ticket, fails. Record: ZOM-542 |
| P92 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A new ticket with no comment, or no ticket, fails. Record: ZOM-556 |
| P93 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A new ticket with no comment, or no ticket, fails. Record: ZOM-563 |
| P94 | Counter-reading — (a) any wording carrying the call passes, a reason beside it is free · (b) A new ticket with no comment, or no ticket, fails. Record: ZOM-483 |
| P95 | Counter-reading — (a) a comment pointing to a new ticket is no call comment · (b) a call left on ZOM-542 instead of the new ticket fails (brief §4 risk 'base tickets holding the asks') |
| P96 | Counter-reading — (a) a move in any order among the writes passes · (b) Todo (the rule doc's default, which the roadmap card overrides) fails. Record: 68d1eb90bef538c7c5c5599d |
| P97 | Counter-reading — (a) a move in any order among the writes passes · (b) Todo (the rule doc's default, which the roadmap card overrides) fails. Record: 68d1eb90bef538c7c5c5599d |
| P98 | Counter-reading — (a) a move in any order among the writes passes · (b) Todo (the rule doc's default, which the roadmap card overrides) fails. Record: 68d1eb90bef538c7c5c5599d |
| P99 | Counter-reading — (a) a move in any order among the writes passes · (b) Todo (the rule doc's default, which the roadmap card overrides) fails. Record: D06UFE81RF0/1759174846.723833 |
| P100 | Counter-reading — (a) a move in any order among the writes passes · (b) Todo (the rule doc's default, which the roadmap card overrides) fails. Record: 68d1eb90bef538c7c5c5599d |
| P101 | Counter-reading — (a) a move in any order among the writes passes · (b) Any other state fails. Record: f_dc45e0e5a8b8635c1b82b2 |
| P102 | Counter-reading — (a) a move in any order among the writes passes · (b) Todo (the rule doc's default, which the roadmap card overrides) fails. Record: 68d1eb90bef538c7c5c5599d |
| P103 | Counter-reading — (a) a move in any order among the writes passes · (b) Any other state fails. Record: 68c45bba5d2c25a3a5c26a8c |
| P104 | Counter-reading — (a) a move in any order among the writes passes · (b) Any other state fails. Record: DES-345 |
| P105 | Counter-reading — (a) moves in any order pass, and its new tickets don't count · (b) the 18 unsampled Holds left in Todo, or a Go ticket put in Backlog, break the 24; card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.') |
| P106 | Counter-reading — (a) moves in any order pass · (b) a Hold canceled, or Lapsed 14 days left in place, breaks the 6; rule doc f_dc45e0e5a8b8635c1b82b2 ('Drop tickets go to Canceled') |
| P107 | Counter-reading — (a) unassigning in the same update or a later one passes, and its new tickets don't count · (b) a state-only move leaves Samuel assigned and fails, and a Todo run that unassigns nothing can't pass; card 68d1eb90bef538c7c5c5599d ('unassigned') |
| P108 | Counter-reading — (a) unassigning in the same update as the move or a later one passes · (b) DES-313 left with Calvin Price fails. Record: 68d1eb90bef538c7c5c5599d |
| P109 | Counter-reading — (a) unassigning in the same update as the move or a later one passes · (b) DES-315 left with Samuel Turner fails. Record: 68d1eb90bef538c7c5c5599d |
| P110 | Counter-reading — (a) unassigning in the same update as the move or a later one passes · (b) DES-329 left with Samuel Turner fails. Record: 68d1eb90bef538c7c5c5599d |
| P111 | Counter-reading — (a) any title, state or assignee passes (brief §4b) · (b) 'Your Squad Needs You Back' fails against evt_f2c03e69f50acf62c9d1c3 |
| P112 | Counter-reading — (a) any title in Design or Zombie Match 3D passes (brief §4b) · (b) No ticket, or a ticket for another message, fails. Record: ZOM-542 |
| P113 | Counter-reading — (a) any title in Design or Zombie Match 3D passes (brief §4b) · (b) No ticket, or a ticket for another message, fails. Record: ZOM-556 |
| P114 | Counter-reading — (a) any title in Design or Zombie Match 3D passes (brief §4b) · (b) No ticket, or a ticket for another message, fails. Record: ZOM-563 |
| P115 | Counter-reading — (a) any title in Design or Zombie Match 3D passes (brief §4b) · (b) No ticket, or a ticket for another message, fails. Record: ZOM-483 |
| P116 | Counter-reading — (a) the four asks and one string ticket in any team pass · (b) a second Win & Collect ticket makes six, against D06L58XCVKK/1759264851.763895 ('don't make a second one') |
| P117 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket in Todo fails. Record: 68d1eb90bef538c7c5c5599d |
| P118 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket given an assignee fails. Record: 68d1eb90bef538c7c5c5599d |
| P119 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket in Todo fails. Record: 68d1eb90bef538c7c5c5599d |
| P120 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket given an assignee fails. Record: 68d1eb90bef538c7c5c5599d |
| P121 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket in Todo fails. Record: 68d1eb90bef538c7c5c5599d |
| P122 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket given an assignee fails. Record: 68d1eb90bef538c7c5c5599d |
| P123 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket in Todo fails. Record: 68d1eb90bef538c7c5c5599d |
| P124 | Counter-reading — (a) set at creation or by a later update passes · (b) That ticket given an assignee fails. Record: 68d1eb90bef538c7c5c5599d |
| P125 | Counter-reading — (a) any checklist name, and an item that adds the headline, passes · (b) An item on another card fails. Record: 6851a769c65dc0017a227bb7 |
| P126 | Counter-reading — (a) any checklist name, and an item that adds the headline, passes · (b) An item on another card fails. Record: 6851a769c65dc0017a227bb7 |
| P127 | Counter-reading — (a) any checklist name passes · (b) run-3's four items fail: a Hold is on the list; card 6851a769c65dc0017a227bb7 |
| P128 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-328 |
| P129 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-329 |
| P130 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-333 |
| P131 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-345 |
| P132 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: ZOM-542 |
| P133 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-330 |
| P134 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-331 |
| P135 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-344 |
| P136 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-332 |
| P137 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-334 |
| P138 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-335 |
| P139 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-341 |
| P140 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: ZOM-556 |
| P141 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-336 |
| P142 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-337 |
| P143 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-340 |
| P144 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-338 |
| P145 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: ZOM-483 |
| P146 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-313 |
| P147 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: DES-339 |
| P148 | Counter-reading — (a) the ticket key or the name passes, in any wording, in one mail or two · (b) A draft, or an email giving another call, fails. Record: ZOM-563 |
| P149 | Counter-reading — (a) a second mail to one person counts once · (b) nine with Leonard fails, and seven with Douglas missing fails; D06L58XCVKK/1759264851.763895 ('apart from me') |
| P150 | Counter-reading — (a) any order and wording with the number passes · (b) Another count fails; so does a message in a channel. Record: D06L58XCVKK/1759264851.763895 |
| P151 | Counter-reading — (a) any order and wording with the number passes · (b) Another count fails; so does a message in a channel. Record: D06L58XCVKK/1759264851.763895 |
| P152 | Counter-reading — (a) any order and wording with the number passes · (b) Another count fails; so does a message in a channel. Record: D06L58XCVKK/1759264851.763895 |
| P153 | Counter-reading — (a) a read after the post is harmless; only the listed writes count · (b) a late email fails; the prompt says 'When it's all finished' (D06L58XCVKK/1759264851.763895) |

Unresolved: (1) diversity.authority_share, the one structural gate check: the parent DES-314 (95%) and the rule doc f_dc45e0e5a8b8635c1b82b2 (90%) sit upstream of most of the weight. Leonard's DM names both as the rule and the ticket list, and no honest rubric can grade a call without them. A design finding for the human to accept, as on the archived bridge and Q4 tasks. (2) The local grade estimates mean 70.4 and population SD 0.065 on the rev6 baselines (retained band 0.10–0.30): the SD check is expected to fail on this batch; the requester has not ruled on it. Trimming or re-weighting rows to reach the band is forbidden. (3) If the comment-ask rows were ruled invalid, the average would rise above the 85% cap, so /create-allfail must prove the updatedAt route. (4) The Fix List adds a sheet Call row for DES-344 beside its comment and email rows, so that call sits on three artifacts. The platform asked for it; the email row's fact is declared told:Lapsed 14 days, so v3.fact_duplication passes on the declared ids only. (5) Ledger §F 2 says relations are seeded on the ZOM side only. That is out of date: the SQL inserts relations_json on DES-315, DES-330 and DES-338 as well (SQL L111, L141, L157), a second route to the asks. No OE or row relies on it and no run saw a non-empty relatedTo, so the ledger is left as sealed, and /create-allfail can cite the route once it is proven.
