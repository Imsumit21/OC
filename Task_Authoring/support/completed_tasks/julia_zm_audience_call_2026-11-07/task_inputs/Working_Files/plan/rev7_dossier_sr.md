### rev7 clause sweep (blocking, learnings §61)

Every rule sentence the answer applies, each condition, every value the 82 seeded sessions carry (read from the SQL by `solver.load_state`; ages 26–44, nothing on the 25 or 45 edge).

| Rule sentence (record) | Condition | Values seen | Settling record or "inert" |
|---|---|---|---|
| "25–45 casual and/or RPG gamer friends (not kids)" (note `C090N54TG79/1758517286.431379`) | age 25–45 | 26–44 (min 26 ×1, max 44 ×7) | age band settled by `12b40a5b7cc18f7c9fe2d0a9e0e929b4` ("25–45 years old"); no value on an edge |
| same | "friends" | relation: friend 37, family 15, neighbor 12, classmate 9, Kadıköy ekibi 9 | `ba19de7863a540175f2aeadc12916fa6`: "family, neighbours and old classmates count the same"; Kadıköy ekibi settled by `246d6f4a90620e5dafbb06068f450e46` |
| same | "casual and/or RPG gamer" | audience labels: casual 41, RPG 41 | deck `f_a087f049d271e9aa9f567f`: the observer's label stands |
| same | "not kids" | ages ≥ 26 | inert: no minor anywhere |
| "No coaching, just observe" (note) | coaching | 13 sessions of Claire's Sep 26 gathering; every form says no coaching; Owen's late reply says "no coaching" | Claire's Sep 29 mail `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` |
| "game-industry people don't count … sessions already run too" (`e72083b249987542a134098010edd305`) | works in games | jobs in Contacts: 2 games jobs (QA tester, console games publisher; Live ops producer, mobile games studio), 71 non-games jobs (teacher, nurse, radio producer, marketing specialist at a retail bank, …), Brian's 9 with no job | the two games jobs by `038b5eb5a30326895cb54756`, `0810fb8287e489c125fe2cd9`; Brian's group by his DM; "Radio producer", "Journalist", "Marketing …" are not games work: inert (no one reading "works in games" excludes them, and none is in a games company) |
| Gate Doc "Samsung is the one device group … SM-S, SM-A and SM-F" (`f_748d26e760e54651eaa0d8`) | Samsung device | Galaxy S24/S23/S23 FE/S22/A54/A35/A15, SM-A546E, SM-S921B, SM-A346E, SM-S911B, SM-A155F, SM-A256E (13); Pixel, Redmi, OnePlus, iPhone (69) | "Other phones need nothing" in the same Doc |
| Gate Doc "counts once we have a clean pass covering that device … covers all the Samsung sessions" | a pass exists | Vision Bot run #15 (editor), QA matrix row SM-A546E (real device) | matrix `f_cadae9f611d82d56ac02c3` + post `3dd0b6d6c52c21cd5bbfcd6d6f5345cd`; Vision Bot limited by `harmonygames-Games/match3d#476#rc_27` |
| Gate Doc "A pass is a clean test run of the build players get" | build players get | matrix build 0.3.127 (127) on Android, 0.3.40 (40) on iOS | K5 reply `d7122186e361aa99778c65cb1502759d`: 0.3.127 (127) and 0.3.38 / 0.3.40 went through the store |
| Gate Doc "Sessions on dev builds do not count … never went through a store" | build | 0.3.127 (127) 30, 0.3.40 (40) 30, 0.3.38 (38) 9, 0.3.127 (1943) 13 | `d7122186e361aa99778c65cb1502759d` names 1943 as non-store and the other three as store |
| Robert "dropped for a technical reason, device or build … re-run note" (`167dc58affb9902420038f71d0f5af28`) | technical reason | not-counted reasons: build 13, coached 13, game industry 11; device 0 (the Samsung sessions count) | the same DM: "Dropped for anything else, no re-run" |
| Deck lead test (tie band 0.25, per-audience minimum) (`f_a087f049d271e9aa9f567f`) | gap vs 0.25; minimum per side | truth gap 0.3333 (27 v 18); single misses −0.151 … +0.189 | edge margin 0.083 on the truth, ≥ 0.06 on every single miss (`run_forensics/rev7/solver_check.txt`) |
| Log note "Close-out … counted goes to Done, not counted goes to Canceled" (`f_c691d577b8f837eb4f9eaa`) | state per verdict | 45 counted, 37 not counted | inert beyond the verdicts |
| Log note "Any form that comes in after this batch gets a ticket and a log row" | after the batch | Owen's Sep 30 20:40Z reply (2 sessions); every other form is before the batch | the reply's timestamp vs the last batch ticket (`ZOM-647` updated 20:25:34Z) |
| Leonard "a void rating comes out of both the sum and the count" (`7b38bd6429ce0f189456ac72af02f210`) | void | player 8 void in the forward | the forward `julia.lawson@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>` |
| Robert "install-weighted D7 … mature cohorts … both platforms pooled" + Vincent "cohort weeks starting on or after 2025-07-24" | mature; cut-off | 51 ZM rows; 47 with D14; 16 on or after 2025-07-24 (week 2025-07-21 spans the transfer and is out by "starting on or after") | `2ca968ace3e14d1a34c535f8a5c0cd6e`, `f_4e21b203a62910bdae0353` |

### rev7 time order (learnings §60)

`python3 Task_Authoring/tools/time_order_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql`: Part 1 (automatic forward references) PASS; Part 2, 33 descriptive pointers, worked through: "the card"/"the board"/"the deck" in notes Docs are the game's cards and deck, not records; the log note's "the workbook" (`f_43bc35baf77fd59f4e57b8` created 16:21:47Z) and "this batch" precede it (16:24Z); the card's "her log note" (card 16:52:31Z) follows the note; the ask's "the roadmap card" (21:10Z) follows the card; Vincent's "sheet in thread" (15:12:37Z) is his own reply 86 s later, the base pattern for a post and its thread; the rule posts' "the feedback note" (Sep 22) precede them.

### rev7 counter-readings

| Category | Counter-reading (strongest case it fails) | Evidence | Verdict |
|---|---|---|---|
| People status | an observer who left would void a batch | Victor Barnes replaced by Douglas (`d_cd7849ec043ab3da107f8c`; activity.json quiet_since_2025-12, active at the clock); Frederick Stone quiet_since_2025-10, active at the clock | holds |
| Temporal | Julia's contacts for the late and second-wave players were created Sep 22, before those sessions ran | `038b5eb5a30326895cb54756` created 2025-09-22T16:05:31Z, after Julia's #zombie-match3d call-out asked hosts for their players up front; the gift-code list is built ahead of play | holds, disclosed |
| Cross-service referential | the matrix names SM-A546E, ZOM-588's phone, so it reads as a pass for one phone only | gate Doc "Once there is a pass, it covers all the Samsung sessions in the read" (`f_748d26e760e54651eaa0d8`) | holds |
| Quantitative | 10.47 % could be 10.44 % if week 2025-07-21 is kept | `f_4e21b203a62910bdae0353` says "starting on or after 2025-07-24"; the S-E1 pattern accepts 10.47 and 10.5 only | holds |
| State / Lifecycle | the retention correction first sat on closed ZOM-227 (a comment after Done) | dropped; the KPI tab note carries it; base_check Check C PASS | fixed |
| Identifier / Format | Leonard's relation rule broke the Slack id contract | re-derived to `ba19de7863a540175f2aeadc12916fa6`; base_check Check A PASS | fixed |
| Other | heuristic name warnings on players (Thomas Reid, Matthew Doyle, Peter Langley, Rachel Dunn, George Ellis, Nathan Cole) | fact_check matches first names to roster people; the players are friends of observers with different surnames, named in "Player:" lines only | accepted warning |
| Done gap | Vincent owns both the Done ZOM-567 line and the matrix, so his own records disagree | `cmt_38b3cc50dceda37f40f5` now speaks only to the editor repro and Vision Bot; the matrix is a separate device run | holds |

LINT unknown_column L856: github.github_review_comments seq on harmonygames-Games/match3d#476#rc_27, kept by instruction (base github review rows carry seq and it is NOT NULL in the 2026-10-04 live export; rev6 kept it the same way); evidence harmonygames-Games/match3d#476#rev_2
sql_lint warning L892 (UPDATE keyed on channel_id and ts): the F root `D05GU6L0XFH/1758901945.292269` is a raw export row with no id field (rev4 note), so the predicate cannot be keyed on id
fact_check warnings (10): heuristic first-name and roster matches, dispositioned in the counter-readings above; Claire, Marcus and Martin bare names are rev6 text, unchanged

Unresolved (rev7): the 400+ call ask is met by necessary work only at about 360 (358 planned unconditional; rev6 measured 4.4 calls per session × 82 ≈ 360 + writes), so 400+ needs a run that also reads the routine context; no independent review of the rev7 SQL; Contacts creation date for late players is a disclosed choice.
