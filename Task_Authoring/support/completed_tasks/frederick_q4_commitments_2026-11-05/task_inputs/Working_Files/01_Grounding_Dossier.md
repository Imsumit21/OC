# Grounding Dossier — frederick_q4_commitments · injection rev4 · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev4/01_Universe_Inject.sql`; rev1, rev2 and rev3, each passed by the platform /injection review, are kept with their reviews and truth in `run_forensics/rev1/`–`rev3/`, and rev3's Opus pre-check and /hardness review in `run_forensics/rev3/`), built by `Working_Files/plan/build_sql.py` from the certified design-2 (`01_Scenario_Design.md` 2c09f947100b, draft manifest 84fea705bc87, surface abd340b2b96e); final manifest by `plan/build_final_manifest.py`; solver `Working_Files/solver/solver.py` (truth `solver/truth.json`); this file by `plan/assemble_dossier.py`. Universe synth-cut, seed bound 2025-10-01T00:00:00Z (Tue Sep 30 17:00 PT), eval clock 2025-10-01T07:00:00Z; Frederick's today is Wed Oct 1, 2025. 258 INSERT + 36 UPDATE statements over 10 schemas. Every probability here is UNCALIBRATED.

## 1.A Structural

| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |
|---|---|---|---|
| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email, label_ids_json, internal_date, date | gmail/threads/frederick@harmonygames.co_1840501641217286806.json (message thread_id frederick.stone@harmonygames.co/1840501641217286806) | thread id = mailbox/((ms << 20) + 20 bits); message id = mailbox/ + the RFC Message-ID in angle brackets; one copy per sender/recipient mailbox with SENT or INBOX labels; In-Reply-To / References on replies; thread snippet = newest message (UPDATE) |
| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack/messages/C07C2866011/2025-09.json (root c41d37178fca394c135408d2b38e0879 = C07C2866011/1758513190.847889) | id = sha256(channel|ts)[:32]; a reply carries thread_ts + parent id, and its root's reply_count / reply_users_count / latest_reply are updated (Q01) |
| gdrive.drive_files / gdocs.docs_documents / gsheets / gslides | id, name, mime_type; document_id, title; spreadsheet_id, title; presentation_id, object_id | gdrive/data.json d_175c0d7bc72ed244b944cb (Frederick's root) | f_/d_ + 22 hex; identical sharing on the Drive row and the native row; docs body_text with style_runs headings |
| gcal.gcal_events | event_id, calendar_id | gcal/data.json (10,395 events checked, plan/id_checks_sql.out.json) | one row per attendee calendar, self:true on the owner's copy; evt_ + 22 hex; ical_uid 32 hex @hg4; future plan fields only for the Jan 5, 2026 review |
| linear.linear_issues / linear_comments | id, title, priority, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at; comment id, issue_id, author_id, body, is_edited | linear/data.json (3,687 issues; ZOM-566 is the newest) | id = identifier = ZOM-567; cmt_ + 20 hex; Todo, no lifecycle stamps |
| trello.trello_cards / actions / checklists / check_items | id, name, idBoard, idList; id, type, date; id, name, idCard, idBoard; id, name, idChecklist | trello/data.json board 640643a3fd8f3ca308d9318e (founders' 'Harmony Games' board), card 688c4fa78031638f0804a994 | ids: first 8 hex = Unix seconds of the action (I16); full badges_json shape; createCard + addChecklistToCard actions |
| contacts.contacts | contact_id, first_name, last_name | contacts/contacts.json (170 contacts) | 24 hex ids; sparse like the base (job, email) |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Frederick Stone | frederick.stone@harmonygames.co (roster; base files use the frederick@ alias, I03) | slack EMPLOYEE_0008_SLACK_ID in C07C2866011; mailbox frederick.stone@harmonygames.co/1844732913254784171; Drive root d_175c0d7bc72ed244b944cb | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID (7e88911312fa9a969f0659a105af59a3, D05S58U4SAK/1759174260.052645); hub sender frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>; owner of f_b98287f6f80fe431a71209 | AGREE |
| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID (80ced6c98e9bd0aa1ccb462488f1746d, fc2f69c06b333f6c54dfd63d455c3958); organizer of evt_564a16d0f5f6598d0360d5 | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co | linear usr_cc3e90160f490686 (ZOM-567, cmt_c9a6660d81e067ad1de7); Trello creator of 689b662c60cbe40b9f4a97ae | AGREE |
| ESG Law | partner PERSON_2694 (base engagement frederick.stone@harmonygames.co/1841636073974841484); intake PERSON_2599_EMAIL | seeded note frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>; contact 9b0185e445572aeee9f27d35; checklist f_3b06917a41dd59308d890b | AGREE |
| Nintendo (developer portal) | Nintendo | base frederick.stone@harmonygames.co/1842358947604469113 (Global ToS & NDA Acceptance Required), frederick.stone@harmonygames.co/1842359398719557772 (Registration Completed), C07C2866011/1757011358.730529; seeded ZOM-567 | AGREE ('Global ToS & NDA' in the portal mail, 'Global ToS and NDA' in Arthur's comment) |
| Balancy | Balancy | base frederick.stone@harmonygames.co/1840501641217286806 (PERSON_0527, Leonard's Sep 11 answer) | AGREE |
| Playtestcloud | Playtestcloud | base root C07C2866011/1758513190.847889 (Leonard, Sep 21 PT / Sep 22 03:53 UTC) | AGREE (the Framewell waiver is a reply under it: 9fb2d23420c7e01ca163571f4129c912) |
| Clipforge / UGC Studio / workspace HG-2291 / Paylane | Clipforge (company), UGC Studio (product), HG-2291 (workspace), Paylane (its processor) | welcome frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com> ('workspace is set up (HG-2291)'); paper f_8d0e0e3ae076b2f745e7e2; kickoff evt_0a5e42c3aac62434ba2cfc; notice frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> (no 'Clipforge' string) | DISAGREE (designed alias, one company; joined by HG-2291) |
| Lanternfly Publishing | 'Lanternfly Publishing' (signature, deck); 'Lanternfly' short form | frederick.stone@harmonygames.co/1842800807116855774, deck f_5dbbaf5b251d5261427eb1, DM thread reply D05S58U4SAK/1759174260.052645 under Leonard's Sep 17 root D05S58U4SAK/1758151772.570449 (rev4: names Wen and 'their Southeast Asia deal', not the company) | AGREE (Wen Halvorsen signs the company's thread) |
| Framewell | Framewell · Maren Holt (PERSON_9701_EMAIL) | frederick.stone@harmonygames.co/1843618067251203081, f_fba21c2d5d4bbb02983961 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Pingwise | Pingwise · Dana Whitfield (PERSON_9703_EMAIL) | frederick.stone@harmonygames.co/1844157874176168845, f_6c212cbfb31c3ded44ef8a | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Pixel Harbor Events | Pixel Harbor Events · Teodor Lind (PERSON_9705_EMAIL) | frederick.stone@harmonygames.co/1835288808653226583, f_614f88a28a2f0cf1b88408 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Brightlane Studio | Brightlane Studio · Ines Varga (PERSON_9706_EMAIL) | frederick.stone@harmonygames.co/1841809902797646290, f_9d4639f91c93478d888f4b | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Soundvault | Soundvault · Rafael Moreno (PERSON_9707_EMAIL) | frederick.stone@harmonygames.co/1842719647334876669, f_2686da1086bfcc2fba3f57 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Reviewly | Reviewly · Hana Kobayashi (PERSON_9708_EMAIL) | frederick.stone@harmonygames.co/1843712439092112354, f_4bdfb8e0c47288087c7bba | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Streamcast Talent | Streamcast Talent · Kofi Mensah (PERSON_9709_EMAIL) | frederick.stone@harmonygames.co/1842998987980893279, f_5b961c9c6887d31dcd2ee2 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Lingora | Lingora · Elena Petrova (PERSON_9710_EMAIL) | frederick.stone@harmonygames.co/1842168515789422611, f_34ba4ac9a0f0fa4fd34e9e | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Panelpulse | Panelpulse · Arjun Shah (PERSON_9711_EMAIL) | frederick.stone@harmonygames.co/1842353484595925809, f_41a9ea5036a231989745b2 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Ascendo | Ascendo · Lucia Ferrer (PERSON_9712_EMAIL) | frederick.stone@harmonygames.co/1841081352192260725, f_a9593b0bf23b760e2972c7 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Wishwave | Wishwave · Sven Aalto (PERSON_9713_EMAIL) | frederick.stone@harmonygames.co/1843538794906427760, f_54c2b4e172bb73a4a19845 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Vaultline | Vaultline · Mila Novak (PERSON_9714_EMAIL) | frederick.stone@harmonygames.co/1843980455117084538, f_2715771ae5f0358ad39aa9 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Certwell | Certwell · Jonas Weber (PERSON_9715_EMAIL) | frederick.stone@harmonygames.co/1844067277209770126, f_cfb172dea30b9f6ac8a340 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Kinetic Arcade | Kinetic Arcade · Noor Haddad (PERSON_9716_EMAIL) | frederick.stone@harmonygames.co/1842895178957083445, f_6252955f500f81e3aacbef | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Lumencloud | Lumencloud · Aiden Clarke (PERSON_9717_EMAIL) | frederick.stone@harmonygames.co/1842991438234544282, f_a227b14f03e12005fe8324 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Bundlehouse | Bundlehouse · Freya Olsen (PERSON_9718_EMAIL) | frederick.stone@harmonygames.co/1843442535629243130, f_9d1e0270574584de0eb92c | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Orbit Store | Orbit Store · Mateo Rossi (PERSON_9719_EMAIL) | frederick.stone@harmonygames.co/1843708664218314020, f_2ae7e3ee3220b628391234 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Markward | Markward · Leah Brennan (PERSON_9720_EMAIL) | frederick.stone@harmonygames.co/1842802694553769659, f_71a95593c736b3baf45f91 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Playfuse | Playfuse · Iris Navarro (PERSON_9721_EMAIL) | frederick.stone@harmonygames.co/1844256020889910750, f_9a7fc4a3e45e4394227fa5 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Hootline | Hootline · Gemma Doyle (PERSON_9722_EMAIL) | frederick.stone@harmonygames.co/1839631800730308867 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Glyphworks | Glyphworks · Tomas Novotny (PERSON_9723_EMAIL) | frederick.stone@harmonygames.co/1843350051225919345, f_f6701704e5659b05d9530f | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Cloudlark | Cloudlark · Yara Nasser (PERSON_9724_EMAIL) | frederick.stone@harmonygames.co/1843078260327282996, f_eb94c65ce9f273c6b5a579 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Echohall | Echohall · Bruno Costa (PERSON_9725_EMAIL) | frederick.stone@harmonygames.co/1841538111898044975, f_68e288146ba0eee9fc17fa | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Pressbeam | Pressbeam · Ava Lindqvist (PERSON_9726_EMAIL) | frederick.stone@harmonygames.co/1842983888486665921, f_a9bb79c86b8b7b92083785 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Retainly | Retainly · Omar Farouk (PERSON_9727_EMAIL) | frederick.stone@harmonygames.co/1843346276352069546, f_be21bac5d50e291ebfbe2b | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Quillcraft | Quillcraft · Nadia Petrov (PERSON_9728_EMAIL) | frederick.stone@harmonygames.co/1842262887629456494, f_af809bf6325b452edc8476 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Tilecast | Tilecast · Kenji Mori (PERSON_9729_EMAIL) | frederick.stone@harmonygames.co/1843708664217753499, f_6d13a63be892a29f796b78 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Benchmarkly | Benchmarkly · Clara Weiss (PERSON_9730_EMAIL) | frederick.stone@harmonygames.co/1843984229991264696, f_e916ab7563891481ab3b16 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Loopnote | Loopnote · Pavel Sokol (PERSON_9731_EMAIL) | frederick.stone@harmonygames.co/1842712097587609477, f_6963d4d30aceef4f88966a | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Driftwood Audio | Driftwood Audio · Sofia Marin (PERSON_9732_EMAIL) | frederick.stone@harmonygames.co/1844165423924029064, f_17878d7b82fafcee79bfe7 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Motive Forge | Motive Forge · Hugo Lambert (PERSON_9733_EMAIL) | frederick.stone@harmonygames.co/1843346276352084348, f_e81c6ef89513cac632700a | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Spotlight Fest | Spotlight Fest · Rina Takeda (PERSON_9734_EMAIL) | frederick.stone@harmonygames.co/1842712097588195482, f_9d9cf4e53b1c8607f9c869 | AGREE (new entity; 0 base hits in plan/name_census.json) |
| Rayking Game | Rayking Game | frederick.stone@harmonygames.co/1842348778705877030 | AGREE (boundary (T18)) |
| Playable Factory | Playable Factory | frederick.stone@harmonygames.co/1843000993076735547 | AGREE (boundary (T11)) |
| Gamesforum SF | Gamesforum SF | frederick.stone@harmonygames.co/1842890197572292911 | AGREE (boundary) |
| InterCo Digital | InterCo Digital | frederick.stone@harmonygames.co/1841620870486605150 | AGREE (boundary) |
| Google partner check-in | Google partner check-in | frederick.stone@harmonygames.co/1817715521687421486 | AGREE (boundary (T12)) |
| Singular | Singular | frederick.stone@harmonygames.co/1837914783244638008 | AGREE (boundary (SC-39)) |
| NCsoft | NCsoft | frederick.stone@harmonygames.co/1842898562278009736 | AGREE (boundary (T15)) |
| Dentsu | Dentsu | frederick.stone@harmonygames.co/1843473831194478743 | AGREE (boundary) |
| Mattel | Mattel | C07C2866011/1756832039.396149 | AGREE (boundary (SC-24, SC-55)) |
| Nova Rewards | Nova Rewards | frederick.stone@harmonygames.co/1842255337882328812 | AGREE (boundary (T16)) |

Frederick's GitHub display name 'Ryan' (S04) is avoided: no GitHub record is touched. No roster person is renamed or re-titled.

## 1.C Voice and realism

Seeded speakers, each with its activity.json (synth-cut KB) status at the clock:
- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds dated Jul 22 and Sep 22–30 2025 (C07C2866011/1753207800.603298, C07C2866011/1759166100.370044, C07C2866011/1758920520.674991, D05S58U4SAK/1759174260.052645, hub frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>, docs f_b98287f6f80fe431a71209, f_846ddc38b2aab3d2ed3fcb, f_05f0a451b29b19a1c0b90f).
- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 17 and Sep 25 2025 (C07C2866011/1758134460.899858, C07C2866011/1758819840.884370) and the Sep 17 call he organizes (evt_564a16d0f5f6598d0360d5).
- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Aug 12 (keep-running card 689b662c60cbe40b9f4a97ae) and Sep 23–25 2025 (ZOM-567, cmt_c9a6660d81e067ad1de7), plus Motive Forge's decline in frederick.stone@harmonygames.co/1843346276352084348.
- Frederick Stone (frederick.stone@harmonygames.co, EMPLOYEE_0008_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; his seeded replies (e.g. Lanternfly Sep 10 in frederick.stone@harmonygames.co/1842800807116855774) and the July tracker f_9d6edd4922d8130ccd272e predate the seed bound; quiet only after it.
- External senders PERSON_9701_EMAIL–PERSON_9735_EMAIL (one per counterparty, plain names in the signature), PERSON_2694_EMAIL (ESG partner, base), PERSON_0527_EMAIL (Balancy, base only) and SVC_9701_EMAIL (Paylane notices) are not personas (no activity.json entry).

Lengths, hours and titles from conventions.json (synth-cut KB): slack.length_chars_by_channel_type private p50 51 / p90 155 / p99 617 — the seeded #executives lines run 85–200 characters (the amendment is the longest at ~200, below p99) and the DM line ~150 (im); slack.per_person_hours_and_style — Leonard's core UTC window 15–02 (07–18 PT), Robert's 16–04, Arthur's 15–01: every seeded post falls inside its author's window (Leonard 17:15Z, 18:10Z, 19:31Z, 21:02Z; Robert 17:04Z, 18:41Z; Arthur 16:05Z, 18:20Z); gmail.internal_subject_len_chars p50 42 — the hub subject 'Vendor and partner stuff while I'm in LA' is 41; gcal.duration_min p50 30 — the Spotlight call is 30 minutes, the January review 45; linear.title_prefixes_by_team: most ZOM titles carry no prefix — 'Switch: order dev kits' follows the base's plain imperative titles.

Voice from real messages: Leonard writes lower-case, run-on Slack lines ('we need to talk to more VCs', C096HFA5Z8W/1758564801.307569) and full-sentence mail signed 'Leonard'; Robert's Slack is short and blunt; Arthur's Linear text is matter-of-fact. The seeded lines keep those registers (S_AMEND, S_WAIVER, S_DM in plan/build_sql.py).

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "Nintendo" | base frederick.stone@harmonygames.co/1842358947604469113, frederick.stone@harmonygames.co/1842359398719557772, C07C2866011/1757011358.730529; seeded ZOM-567 | the comment cmt_c9a6660d81e067ad1de7 says 'the portal' and 'Global ToS and NDA' |
| "Balancy" | base frederick.stone@harmonygames.co/1840501641217286806 | Leonard's in-thread answer |
| "Playtestcloud" | base C07C2866011/1758513190.847889 | the root the Framewell reply sits under |
| "ESG" | base frederick.stone@harmonygames.co/1841636073974841484 (engagement, Aug 27); seeded frederick.stone@harmonygames.co/1844177063117059830, f_3b06917a41dd59308d890b | ESG Law intake contact 9b0185e445572aeee9f27d35 |
| "Rayking" | base frederick.stone@harmonygames.co/1842348778705877030 | Frederick's Sep 4 'reply' is addressed to Leonard |
| "runway guardrails" | NEW TERM — introduced in f_b98287f6f80fe431a71209 | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "keep-running" | NEW TERM — introduced in 689b662c60cbe40b9f4a97ae | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "night pager" | NEW TERM — introduced in 689b66a450734c26dcdf6291 | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "HG-2291" | NEW TERM — introduced in f_8d0e0e3ae076b2f745e7e2, frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com>, evt_0a5e42c3aac62434ba2cfc, frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "Paylane / billing@paylane.io" | NEW TERM — introduced in frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "Q4 commitments" | NEW TERM — introduced in d_80a8c04753ba82ba4ba6a5, f_846ddc38b2aab3d2ed3fcb, f_05f0a451b29b19a1c0b90f, evt_fd469c29811879519c2c96 | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "intake checklist" | NEW TERM — introduced in f_3b06917a41dd59308d890b | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "UA spend buckets" | NEW TERM — introduced in f_7bacf15c4e8eea1a52dcd4 | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "Vendor & partner tracker" | NEW TERM — introduced in f_9d6edd4922d8130ccd272e | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "Vendor & partner paperwork" | NEW TERM — introduced in d_ffa3e6e473da7e6523614f | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "Spotlight Fest" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842712097588195482, evt_564a16d0f5f6598d0360d5, C07C2866011/1758134460.899858 | reached via the hub frederick.stone@harmonygames.co/1844732913254784171 or its delegations |
| "Framewell" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843618067251203081 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Pingwise" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844157874176168845 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Pixel Harbor Events" | NEW TERM — introduced in frederick.stone@harmonygames.co/1835288808653226583 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Brightlane Studio" | NEW TERM — introduced in frederick.stone@harmonygames.co/1841809902797646290 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Soundvault" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842719647334876669 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Reviewly" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843712439092112354 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Streamcast Talent" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842998987980893279 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Lingora" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842168515789422611 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Panelpulse" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842353484595925809 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Ascendo" | NEW TERM — introduced in frederick.stone@harmonygames.co/1841081352192260725 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Wishwave" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843538794906427760 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Vaultline" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843980455117084538 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Certwell" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844067277209770126 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Kinetic Arcade" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842895178957083445 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Lumencloud" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842991438234544282 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Bundlehouse" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843442535629243130 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Orbit Store" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843708664218314020 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Markward" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842802694553769659 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Playfuse" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844256020889910750 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Hootline" | NEW TERM — introduced in frederick.stone@harmonygames.co/1839631800730308867 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Glyphworks" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843350051225919345 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Cloudlark" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843078260327282996 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Echohall" | NEW TERM — introduced in frederick.stone@harmonygames.co/1841538111898044975 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Pressbeam" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842983888486665921 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Retainly" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843346276352069546 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Quillcraft" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842262887629456494 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Tilecast" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843708664217753499 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Benchmarkly" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843984229991264696 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Loopnote" | NEW TERM — introduced in frederick.stone@harmonygames.co/1842712097587609477 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Driftwood Audio" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844165423924029064 | 0 base hits over 10 services (plan/name_census.json, complete scans) |
| "Motive Forge" | NEW TERM — introduced in frederick.stone@harmonygames.co/1843346276352084348 | 0 base hits over 10 services (plan/name_census.json, complete scans) |

Name census with a positive control: plan/name_census.json counts every seeded company name over gmail, slack, gdocs, gdrive, contacts, trello, gsheets, gslides, linear and gcal (scan_complete true, 0 hits each); the base names above are the positive controls (each returns its cited record).

## 1.E Persona reach

Load-bearing ids (seeded and base) written to `Working_Files/plan/lb_ids.txt` (167 ids); output verbatim:

```
CHECK-SQL as frederick_stone <frederick.stone@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_b98287f6f80fe431a71209 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_7bacf15c4e8eea1a52dcd4 - persona owns the file
[YES LB] L11 gdrive.drive_files insert f_3b06917a41dd59308d890b - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdrive.drive_files insert d_80a8c04753ba82ba4ba6a5 - persona owns the file
[YES LB] L15 gdrive.drive_files insert f_846ddc38b2aab3d2ed3fcb - file is shared with the persona (shared_with_emails)
[YES LB] L17 gdrive.drive_files insert f_05f0a451b29b19a1c0b90f - file is shared with the persona (shared_with_emails)
[YES LB] L19 gdrive.drive_files insert f_9d6edd4922d8130ccd272e - persona owns the file
[YES LB] L21 gdrive.drive_files insert d_ffa3e6e473da7e6523614f - persona owns the file
[YES LB] L23 gdrive.drive_files insert f_fba21c2d5d4bbb02983961 - persona owns the file
[YES LB] L25 gdrive.drive_files insert f_6c212cbfb31c3ded44ef8a - persona owns the file
[YES LB] L27 gdrive.drive_files insert f_8d0e0e3ae076b2f745e7e2 - persona owns the file
[YES LB] L29 gdrive.drive_files insert f_614f88a28a2f0cf1b88408 - persona owns the file
[YES LB] L31 gdrive.drive_files insert f_5dbbaf5b251d5261427eb1 - persona owns the file
[YES LB] L33 gdrive.drive_files insert f_9d4639f91c93478d888f4b - persona owns the file
[YES LB] L35 gdrive.drive_files insert f_2686da1086bfcc2fba3f57 - persona owns the file
[YES LB] L37 gdrive.drive_files insert f_4bdfb8e0c47288087c7bba - persona owns the file
[YES LB] L39 gdrive.drive_files insert f_5b961c9c6887d31dcd2ee2 - persona owns the file
[YES LB] L41 gdrive.drive_files insert f_34ba4ac9a0f0fa4fd34e9e - persona owns the file
[YES LB] L43 gdrive.drive_files insert f_41a9ea5036a231989745b2 - persona owns the file
[YES LB] L45 gdrive.drive_files insert f_a9593b0bf23b760e2972c7 - persona owns the file
[YES LB] L47 gdrive.drive_files insert f_54c2b4e172bb73a4a19845 - persona owns the file
[YES LB] L49 gdrive.drive_files insert f_2715771ae5f0358ad39aa9 - persona owns the file
[YES LB] L51 gdrive.drive_files insert f_cfb172dea30b9f6ac8a340 - persona owns the file
[YES LB] L53 gdrive.drive_files insert f_6252955f500f81e3aacbef - persona owns the file
[YES LB] L55 gdrive.drive_files insert f_a227b14f03e12005fe8324 - persona owns the file
[YES LB] L57 gdrive.drive_files insert f_9d1e0270574584de0eb92c - persona owns the file
[YES LB] L59 gdrive.drive_files insert f_2ae7e3ee3220b628391234 - persona owns the file
[YES LB] L61 gdrive.drive_files insert f_71a95593c736b3baf45f91 - persona owns the file
[YES LB] L63 gdrive.drive_files insert f_9a7fc4a3e45e4394227fa5 - persona owns the file
[YES LB] L65 gdrive.drive_files insert f_f6701704e5659b05d9530f - persona owns the file
[YES LB] L67 gdrive.drive_files insert f_eb94c65ce9f273c6b5a579 - persona owns the file
[YES LB] L69 gdrive.drive_files insert f_68e288146ba0eee9fc17fa - persona owns the file
[YES LB] L71 gdrive.drive_files insert f_a9bb79c86b8b7b92083785 - persona owns the file
[YES LB] L73 gdrive.drive_files insert f_be21bac5d50e291ebfbe2b - persona owns the file
[YES LB] L75 gdrive.drive_files insert f_af809bf6325b452edc8476 - persona owns the file
[YES LB] L77 gdrive.drive_files insert f_6d13a63be892a29f796b78 - persona owns the file
[YES LB] L79 gdrive.drive_files insert f_e916ab7563891481ab3b16 - persona owns the file
[YES LB] L81 gdrive.drive_files insert f_6963d4d30aceef4f88966a - persona owns the file
[YES LB] L83 gdrive.drive_files insert f_17878d7b82fafcee79bfe7 - persona owns the file
[YES LB] L85 gdrive.drive_files insert f_e81c6ef89513cac632700a - persona owns the file
[YES LB] L87 gdrive.drive_files insert f_9d9cf4e53b1c8607f9c869 - persona owns the file
[YES LB] L89 gdocs.docs_documents insert f_b98287f6f80fe431a71209 - file is shared with the persona (shared_with_emails)
[YES LB] L92 gdocs.docs_documents insert f_7bacf15c4e8eea1a52dcd4 - persona owns the file
[YES LB] L94 gdocs.docs_documents insert f_3b06917a41dd59308d890b - file is shared with the persona (shared_with_emails)
[YES LB] L96 gdocs.docs_documents insert f_846ddc38b2aab3d2ed3fcb - file is shared with the persona (shared_with_emails)
[YES LB] L98 gdocs.docs_documents insert f_fba21c2d5d4bbb02983961 - persona owns the file
[YES LB] L100 gdocs.docs_documents insert f_6c212cbfb31c3ded44ef8a - persona owns the file
[YES LB] L102 gdocs.docs_documents insert f_8d0e0e3ae076b2f745e7e2 - persona owns the file
[YES LB] L104 gdocs.docs_documents insert f_614f88a28a2f0cf1b88408 - persona owns the file
[YES LB] L106 gdocs.docs_documents insert f_9d4639f91c93478d888f4b - persona owns the file
[YES LB] L108 gdocs.docs_documents insert f_2686da1086bfcc2fba3f57 - persona owns the file
[YES LB] L110 gdocs.docs_documents insert f_4bdfb8e0c47288087c7bba - persona owns the file
[YES LB] L112 gdocs.docs_documents insert f_5b961c9c6887d31dcd2ee2 - persona owns the file
[YES LB] L114 gdocs.docs_documents insert f_34ba4ac9a0f0fa4fd34e9e - persona owns the file
[YES LB] L116 gdocs.docs_documents insert f_41a9ea5036a231989745b2 - persona owns the file
[YES LB] L118 gdocs.docs_documents insert f_a9593b0bf23b760e2972c7 - persona owns the file
[YES LB] L120 gdocs.docs_documents insert f_54c2b4e172bb73a4a19845 - persona owns the file
[YES LB] L122 gdocs.docs_documents insert f_2715771ae5f0358ad39aa9 - persona owns the file
[YES LB] L124 gdocs.docs_documents insert f_cfb172dea30b9f6ac8a340 - persona owns the file
[YES LB] L126 gdocs.docs_documents insert f_6252955f500f81e3aacbef - persona owns the file
[YES LB] L128 gdocs.docs_documents insert f_a227b14f03e12005fe8324 - persona owns the file
[YES LB] L130 gdocs.docs_documents insert f_2ae7e3ee3220b628391234 - persona owns the file
[YES LB] L132 gdocs.docs_documents insert f_71a95593c736b3baf45f91 - persona owns the file
[YES LB] L134 gdocs.docs_documents insert f_9a7fc4a3e45e4394227fa5 - persona owns the file
[YES LB] L136 gdocs.docs_documents insert f_f6701704e5659b05d9530f - persona owns the file
[YES LB] L138 gdocs.docs_documents insert f_eb94c65ce9f273c6b5a579 - persona owns the file
[YES LB] L140 gdocs.docs_documents insert f_68e288146ba0eee9fc17fa - persona owns the file
[YES LB] L142 gdocs.docs_documents insert f_a9bb79c86b8b7b92083785 - persona owns the file
[YES LB] L144 gdocs.docs_documents insert f_be21bac5d50e291ebfbe2b - persona owns the file
[YES LB] L146 gdocs.docs_documents insert f_af809bf6325b452edc8476 - persona owns the file
[YES LB] L148 gdocs.docs_documents insert f_6d13a63be892a29f796b78 - persona owns the file
[YES LB] L150 gdocs.docs_documents insert f_e916ab7563891481ab3b16 - persona owns the file
[YES LB] L152 gdocs.docs_documents insert f_6963d4d30aceef4f88966a - persona owns the file
[YES LB] L154 gdocs.docs_documents insert f_17878d7b82fafcee79bfe7 - persona owns the file
[YES LB] L156 gdocs.docs_documents insert f_e81c6ef89513cac632700a - persona owns the file
[YES LB] L158 gdocs.docs_documents insert f_9d9cf4e53b1c8607f9c869 - persona owns the file
[YES LB] L160 gsheets.sheets_spreadsheets insert f_05f0a451b29b19a1c0b90f - file is shared with the persona (shared_with_emails)
[YES LB] L163 gsheets.sheets_sheets insert f_05f0a451b29b19a1c0b90f, f_05f0a451b29b19a1c0b90f#0 - file is shared with the persona (shared_with_emails)
[YES LB] L165 gsheets.sheets_spreadsheets insert f_9d6edd4922d8130ccd272e - persona owns the file
[YES LB] L167 gsheets.sheets_sheets insert f_9d6edd4922d8130ccd272e, f_9d6edd4922d8130ccd272e#0 - persona owns the file
[YES LB] L169 gslides.slides_presentations insert f_5dbbaf5b251d5261427eb1 - persona owns the file
[YES LB] L172 gslides.slides_pages insert f_5dbbaf5b251d5261427eb1, slide_bd9e4b92fdc9 - persona owns the file
[YES LB] L174 gslides.slides_page_elements insert f_5dbbaf5b251d5261427eb1, el_8834f6ce6725, slide_bd9e4b92fdc9 - persona owns the file
[YES LB] L176 gslides.slides_page_elements insert f_5dbbaf5b251d5261427eb1, el_fb76c317bfff, slide_bd9e4b92fdc9 - persona owns the file
[YES LB] L178 gslides.slides_pages insert f_5dbbaf5b251d5261427eb1, slide_e799ff88ca1a - persona owns the file
[YES LB] L180 gslides.slides_page_elements insert f_5dbbaf5b251d5261427eb1, el_877e3d66198b, slide_e799ff88ca1a - persona owns the file
[YES LB] L182 gslides.slides_page_elements insert f_5dbbaf5b251d5261427eb1, el_ef57d97ed3b0, slide_e799ff88ca1a - persona owns the file
[YES LB] L184 gslides.slides_pages insert f_5dbbaf5b251d5261427eb1, slide_07d1f58819b2 - persona owns the file
[YES LB] L186 gslides.slides_page_elements insert f_5dbbaf5b251d5261427eb1, el_15f716be26f7, slide_07d1f58819b2 - persona owns the file
[YES LB] L188 gslides.slides_page_elements insert f_5dbbaf5b251d5261427eb1, el_9b987d530635, slide_07d1f58819b2 - persona owns the file
[YES LB] L190 gslides.slides_presentations insert f_9d1e0270574584de0eb92c - persona owns the file
[YES LB] L192 gslides.slides_pages insert f_9d1e0270574584de0eb92c, slide_3818928cc5b4 - persona owns the file
[YES LB] L194 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_0fc3f5f3ace9, slide_3818928cc5b4 - persona owns the file
[YES LB] L196 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_a0dbd46db1a6, slide_3818928cc5b4 - persona owns the file
[YES LB] L198 gslides.slides_pages insert f_9d1e0270574584de0eb92c, slide_111fef17ef5d - persona owns the file
[YES LB] L200 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_53e619c8898a, slide_111fef17ef5d - persona owns the file
[YES LB] L202 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_322d7da20cb6, slide_111fef17ef5d - persona owns the file
[YES LB] L204 gslides.slides_pages insert f_9d1e0270574584de0eb92c, slide_52be557fc2cd - persona owns the file
[YES LB] L206 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_d7939404bc4a, slide_52be557fc2cd - persona owns the file
[YES LB] L208 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_6a07a17c39ac, slide_52be557fc2cd - persona owns the file
[YES LB] L210 gslides.slides_pages insert f_9d1e0270574584de0eb92c, slide_2961165dab03 - persona owns the file
[YES LB] L212 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_34a6e6e73388, slide_2961165dab03 - persona owns the file
[YES LB] L214 gslides.slides_page_elements insert f_9d1e0270574584de0eb92c, el_1bf4ee220b8b, slide_2961165dab03 - persona owns the file
[YES LB] L216 slack.slack_messages insert 0573efd133cabdb1acde61e68571aa82, C07C2866011/1753207800.603298 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L219 slack.slack_messages insert 80ced6c98e9bd0aa1ccb462488f1746d, C07C2866011/1758819840.884370 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L221 slack.slack_messages insert fc2f69c06b333f6c54dfd63d455c3958, C07C2866011/1758134460.899858 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L223 slack.slack_messages insert 7e88911312fa9a969f0659a105af59a3, C07C2866011/1759166100.370044 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L225 slack.slack_messages insert 9fb2d23420c7e01ca163571f4129c912, C07C2866011/1758920520.674991 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L227 slack.slack_messages update c41d37178fca394c135408d2b38e0879, C07C2866011/1758513190.847889 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L228 slack.slack_messages insert 418a0a6d6c29b7b67ce0ffb270c78c1e, D05S58U4SAK/1759174260.052645 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES] L230 slack.slack_messages update c148cae9de21cd26027d8bbc89bb127c, D05S58U4SAK/1758151772.570449 - persona EMPLOYEE_0008_SLACK_ID is in members of im D05S58U4SAK
[YES LB] L248 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844732913254784171 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L251 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L253 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844732913254960629 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L255 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L257 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844177063117059830 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L259 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L261 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844177063117003267 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L263 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L265 gmail.gmail_threads insert robert@harmonygames.co/1844177063117516849 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L267 gmail.gmail_messages insert robert@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L269 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844177063117181908 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L271 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L273 gmail.gmail_threads update frederick.stone@harmonygames.co/1844177063117059830 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L274 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L276 gmail.gmail_threads update leonard.hayes@harmonygames.co/1844177063117003267 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L277 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L279 gmail.gmail_threads update robert@harmonygames.co/1844177063117516849 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L280 gmail.gmail_messages insert robert@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L282 gmail.gmail_threads update arthur.blake@harmonygames.co/1844177063117181908 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L283 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L285 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843067564852153540 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L287 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>, fre - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L289 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843618067251203081 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L291 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAGJkuaxoKn_J2zxTzhLswrYwOGA_wA5IXe9v747@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L293 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844157874176168845 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L295 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAZgisbRwHgHd3Hk_E9LYMNIOFiMZminBj4K2tWc@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L297 gmail.gmail_threads insert frederick.stone@harmonygames.co/1837102635418059486 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L299 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L301 gmail.gmail_threads update frederick.stone@harmonygames.co/1837102635418059486 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L302 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAFEbdSLTqGx4K9ylCWMjfozRDorLWGyAc5mo6e7@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L304 gmail.gmail_threads insert frederick.stone@harmonygames.co/1835288808653226583 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L306 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L308 gmail.gmail_threads update frederick.stone@harmonygames.co/1835288808653226583 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L309 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CALCA8gxcwd0yOaLVGO1KlKBHNjV4IHaI4Lm7Shq@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L311 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842800807116855774 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L313 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAUTttDNR2kwXReKZgzK8GvbJXxwUnrHN42rwhn1@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L315 gmail.gmail_threads update frederick.stone@harmonygames.co/1842800807116855774 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L316 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAY11pXWEb2u5uCxBJhKpklYcHpViFPzYgETaeTx@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L318 gmail.gmail_threads update frederick.stone@harmonygames.co/1842800807116855774 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L319 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CArrsRpTwnF5vDz3j8sB1bdi-2N8lorF7bNSSbk-@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L321 gmail.gmail_threads insert frederick.stone@harmonygames.co/1841809902797646290 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L323 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA0uGW7WigxQ0mENWo-aIuiEpfLWJbrhuxMJjS0A@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L325 gmail.gmail_threads update frederick.stone@harmonygames.co/1841809902797646290 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L326 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA-xgF65XCwo6QXURZM_eCJcAClcs_LfeftzR27P@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L328 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842719647334876669 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L330 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdDglIne-JLPfhnQyZF8qjaAlhus3WbzeVF5FoW@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L332 gmail.gmail_threads update frederick.stone@harmonygames.co/1842719647334876669 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L333 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAeW3ux2LavW4Rp-PXhOt5Xhvgtjzfq1XU3eJO_C@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L335 gmail.gmail_threads update frederick.stone@harmonygames.co/1842719647334876669 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L336 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAa-jv7GWQa7i06XwUWtNIJ_DInBkE5Qi4Y8PmMT@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L338 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843712439092112354 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L340 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAN4G0SGg1BdZ4ApKmfoiXizgNPn1Wz1lObQmvmL@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L342 gmail.gmail_threads update frederick.stone@harmonygames.co/1843712439092112354 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L343 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAEcTJxNSlNWdzmdlv0uAxA5LWo-4JRqmN_lbkGs@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L345 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842998987980893279 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L347 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAKGQuOVQjttk8qpLC2bhGl1ZJ4oRI7nPbIzP6mR@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L349 gmail.gmail_threads update frederick.stone@harmonygames.co/1842998987980893279 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L350 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAIauDHOvbuHs1D8VFmRdi2YfR01quJPqo1ZiQZJ@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L352 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842168515789422611 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L354 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAIMbUgCSlodxbiO4p94ujFhTeSTtN2swRzPIQL0@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L356 gmail.gmail_threads update frederick.stone@harmonygames.co/1842168515789422611 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L357 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdgQm_LmTWyiKsAANkrEQIXisEv_9hNMklsIUx_@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L359 gmail.gmail_threads update frederick.stone@harmonygames.co/1842168515789422611 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L360 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAb3f_RRKlDbfktS3_Cu7qnXPyTybHnS1K2Eq3b7@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L362 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842353484595925809 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L364 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA1qNRLdbV7Qkr9KCNYq0gKKHAL3Hn7aap534PvX@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L366 gmail.gmail_threads update frederick.stone@harmonygames.co/1842353484595925809 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L367 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAM5dEEI7CWxEdApgrQnK2XC211TZL1KF-WNUpsB@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L369 gmail.gmail_threads insert frederick.stone@harmonygames.co/1841081352192260725 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L371 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAyf6nlOFNNbNBnx3fo0wtMQ8n9aXQTM_GxC86hB@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L373 gmail.gmail_threads update frederick.stone@harmonygames.co/1841081352192260725 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L374 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA0BbU6OEljE3nhaS2pWMojXL9GJ_kYqFO8JTtP2@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L376 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843538794906427760 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L378 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAXYl4kZwjniI2DACcpaEMWNhajoK6HBVw4uaXGD@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L380 gmail.gmail_threads update frederick.stone@harmonygames.co/1843538794906427760 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L381 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAHavdKpt7nR3fxojrxKL1PYVBWt8ridR2XEm01t@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L383 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843980455117084538 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L385 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CASRfZCkXuHwLJPLUeim95W1qFlzEaz37BReSyJz@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L387 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844067277209770126 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L389 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CApaJB4i_PhvJp_95Q3bE-l9yDV4x096tsJobB11@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L391 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842895178957083445 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L393 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA3aUrexaU1ytNuMja5-4b03__ehILzpWLqaO5Yx@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L395 gmail.gmail_threads update frederick.stone@harmonygames.co/1842895178957083445 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L396 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAwVKKP1C-1rXHFCWIgbB9PjITqgDI3ziZAK9984@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L398 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842991438234544282 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L400 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAMStwDpDMa-TpyL6LYTnlEtJ1wHg3ijdeUe3kRU@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L402 gmail.gmail_threads update frederick.stone@harmonygames.co/1842991438234544282 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L403 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA2AOLHmh-RU9NexSr5s80P3mUbj-J4_hr59arcw@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L405 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843442535629243130 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L407 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAO2B00xDzwszNF3Ilw5PbJg0oZh1fnZ-QLkS2Jt@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L409 gmail.gmail_threads update frederick.stone@harmonygames.co/1843442535629243130 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L410 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAlSBl5tSj6BhvNqcMHhDChnKE3Fcp7fgMJdKNtH@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L412 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843708664218314020 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L414 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdma6oOdAQE9dig43QVuUgNp0etrBmzar36esvm@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L416 gmail.gmail_threads update frederick.stone@harmonygames.co/1843708664218314020 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L417 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAo7WkZSvPT7fVQd40F1HezmilqIw9AoAb6_uTM2@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L419 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842802694553769659 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L421 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAkJn3vHo1ZSVJM1fxECsBF9x2KnMEi9FvdW5zAr@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L423 gmail.gmail_threads update frederick.stone@harmonygames.co/1842802694553769659 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L424 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAjzt3v0v5AIRijm5FdJu1yYv5Q-LMNqpRFDYAqb@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L426 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844256020889910750 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L428 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAWCBU--R8_Q4xxjtvPvDrzjjgqqRxz_flrPVZo6@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L430 gmail.gmail_threads insert frederick.stone@harmonygames.co/1839631800730308867 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L432 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAat3tn3W0qDDTcWKmBYwD1Jnj1j_YU1h2NqzJZj@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L434 gmail.gmail_threads update frederick.stone@harmonygames.co/1839631800730308867 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L435 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L437 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843350051225919345 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L439 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAK5OtyGBKIjnQ7R24aq6RTWoGDUT4Dvg3I21YVO@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L441 gmail.gmail_threads update frederick.stone@harmonygames.co/1843350051225919345 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L442 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAWFrjpQqU9OPoIfzxLgVsbT6sBJa8bgCCjzFYiF@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L444 gmail.gmail_threads update frederick.stone@harmonygames.co/1843350051225919345 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L445 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CApanLB9xL5jrjcNSzDTWYvE6RiWdfZchZxr4q3K@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L447 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843078260327282996 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L449 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAXUVl-vI7c6T4f22vI41yY2P83JxLRUdeHW1-hC@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L451 gmail.gmail_threads insert frederick.stone@harmonygames.co/1841538111898044975 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L453 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAF3j_dVe4Smvh19S7lyCBLjtao8Qe8vwV9yybpg@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L455 gmail.gmail_threads update frederick.stone@harmonygames.co/1841538111898044975 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L456 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAHV7my-sLo9CEzISCj6j5YvPRBW1ReAHi-SrN7V@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L458 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842983888486665921 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L460 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAGdptfs7cIHOLvLgF6LBpN_8DHhsOmA8Oqoddfh@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L462 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843346276352069546 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L464 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAOHCdeuLRHpqtIPQZRUGefwtjIwm5BrmgGS_Loo@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L466 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842262887629456494 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L468 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAi_XBSxfgfRVpvhsqJCtZzn_v40OoXxKbCxhQb8@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L470 gmail.gmail_threads update frederick.stone@harmonygames.co/1842262887629456494 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L471 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CALcXsJB9Dsqckdbzui4zsoYGv8YD3gxSJbpOQzA@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L473 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843708664217753499 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L475 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdfSBCTPq8pDFK70IArhUSHj5PEV3Tnz19vDg7Y@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L477 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843984229991264696 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L479 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAHSfM6DagNeY2EUvRjCOyAb1FwmdFsO1FgnXFpY@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L481 gmail.gmail_threads update frederick.stone@harmonygames.co/1843984229991264696 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L482 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAFrM1JgqylGFM5MjwuqQMZPLsTjafUxYfbcriCb@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L484 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842712097587609477 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L486 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAXtogZgoD89z43tdTH1zDpTmUGOoXKTd_jeRYV5@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L488 gmail.gmail_threads update frederick.stone@harmonygames.co/1842712097587609477 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L489 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAff-LH5Vcdc03I5o2aYmpkuR0BE-z_AH8pa3w_W@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L491 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844165423924029064 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L493 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA6I5lYTxcuD1NKwoqPt6_lMK3iSCs805OP2H7LL@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L495 gmail.gmail_threads update frederick.stone@harmonygames.co/1844165423924029064 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L496 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA-DqRg1TZ4TPniI7P8AW7DvtD6lNosGZdpC1x6_@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L498 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843346276352084348 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L500 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAroxkgBywTvnZooHWA1QvDuZcDMuI8XdpMtLkts@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L502 gmail.gmail_threads insert arthur.blake@harmonygames.co/1843346276352842555 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L504 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAroxkgBywTvnZooHWA1QvDuZcDMuI8XdpMtLkts@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L506 gmail.gmail_threads update frederick.stone@harmonygames.co/1843346276352084348 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L507 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CALRuD4F9RvCLHQDHmtUqgPhhu2lRtd9SiD5vfMt@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L509 gmail.gmail_threads update arthur.blake@harmonygames.co/1843346276352842555 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L510 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CALRuD4F9RvCLHQDHmtUqgPhhu2lRtd9SiD5vfMt@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L512 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842712097588195482 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L514 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAjj6h7BzqoAZSS2-4M7N9e7ZLBDyeyZXl0BwgcI@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L516 gmail.gmail_threads insert frederick.stone@harmonygames.co/1842255337882328812 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L518 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAFbpDWclpri3pr8w9gLzu4buYYHdy_xmueMuggv@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L520 gmail.gmail_threads update frederick.stone@harmonygames.co/1842255337882328812 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L521 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA32kc92PkZh7ZypeSz7afbb9TxyW_GZmCBXxoch@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L523 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844622183629433486 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L525 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-7ab9aa8e-d441-a5e5-d4a5-953239767264@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L527 gmail.gmail_threads insert robert@harmonygames.co/1844622183628992238 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L529 gmail.gmail_messages insert robert@harmonygames.co/<calendar-a902eeee-7fb9-b775-7653-360e98115ee6@google.com>, robert@ - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L531 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844622183629272206 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L533 gmail.gmail_messages insert arthur.blake@harmonygames.co/<calendar-d127348e-9054-26a4-f7c1-21f3338d10c6@google.com>, a - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L535 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843074485453681260 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L537 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-36ed726c-941d-8aa3-2a87-2dccaaba569c@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L539 gcal.gcal_events insert evt_fd469c29811879519c2c96 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L542 gcal.gcal_events insert evt_2ad963d94b80e64c3a3c12 - persona is an attendee and holds its own copy evt_fd469c29811879519c2c96 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L544 gcal.gcal_events insert evt_c8f5a9295ed40f33d90fab - persona is an attendee and holds its own copy evt_fd469c29811879519c2c96 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L546 gcal.gcal_events insert evt_bde03e4af2d3b5039711c0 - persona is an attendee and holds its own copy evt_fd469c29811879519c2c96 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES LB] L548 gcal.gcal_events insert evt_0a5e42c3aac62434ba2cfc - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES LB] L550 gcal.gcal_events insert evt_564a16d0f5f6598d0360d5 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L552 gcal.gcal_events insert evt_0c2bdb97953bcb213e1d36 - persona is an attendee and holds its own copy evt_564a16d0f5f6598d0360d5 (same ical_uid and start) on frederick.stone@harmonygames.co
[YES LB] base slack C07C2866011/1757011358.730529 - base record: message inherits channel: persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] base gmail frederick.stone@harmonygames.co/1817715521687421486 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1840501641217286806 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1841636073974841484 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1842348778705877030 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1842358947604469113 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1842359398719557772 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co
[YES LB] base gmail frederick.stone@harmonygames.co/1843000993076735547 - base record: thread is in the persona's own mailbox frederick.stone@harmonygames.co

summary: {'YES': 258, 'NO': 22}  unscoped rows (always visible): 14
  gcal.gcal_events: {'YES': 7}
  gdocs.docs_documents: {'YES': 35}
  gdrive.drive_files: {'YES': 41}
  gmail.gmail_messages: {'YES': 70, 'NO': 11}
  gmail.gmail_threads: {'YES': 70, 'NO': 11}
  gsheets.sheets_sheets: {'YES': 2}
  gsheets.sheets_spreadsheets: {'YES': 2}
  gslides.slides_page_elements: {'YES': 14}
  gslides.slides_pages: {'YES': 7}
  gslides.slides_presentations: {'YES': 2}
  slack.slack_messages: {'YES': 8}
verdict: PASS (0 load-bearing rows not visible)
```

- C07C2866011 — #executives, Frederick a member (EMPLOYEE_0008_SLACK_ID in members_json) LB; seeded posts 0573efd133cabdb1acde61e68571aa82, 80ced6c98e9bd0aa1ccb462488f1746d, fc2f69c06b333f6c54dfd63d455c3958, 7e88911312fa9a969f0659a105af59a3, reply 9fb2d23420c7e01ca163571f4129c912.
- D05S58U4SAK — Frederick's DM with Leonard (im member) LB; seeded thread reply 418a0a6d6c29b7b67ce0ffb270c78c1e (D05S58U4SAK/1759174260.052645) under the base root c148cae9de21cd26027d8bbc89bb127c (D05S58U4SAK/1758151772.570449), whose counters the SQL updates.
- Frederick's mailbox: the hub frederick.stone@harmonygames.co/1844732913254784171, ESG's thread frederick.stone@harmonygames.co/1844177063117059830, the notice frederick.stone@harmonygames.co/1843067564852153540 and every member thread (Facts for the human) are INBOX/SENT copies in frederick.stone@harmonygames.co LB.
- Drive: d_80a8c04753ba82ba4ba6a5 and f_7bacf15c4e8eea1a52dcd4 are Frederick-owned; f_b98287f6f80fe431a71209, f_846ddc38b2aab3d2ed3fcb, f_05f0a451b29b19a1c0b90f and f_3b06917a41dd59308d890b are shared with him (shared_with_emails); the counterparties' papers are Frederick-owned copies he filed in d_ffa3e6e473da7e6523614f LB.
- Calendar: evt_fd469c29811879519c2c96 (January review), evt_564a16d0f5f6598d0360d5 (Spotlight call) and evt_0a5e42c3aac62434ba2cfc (kickoff) are Frederick's own copies (self:true) LB.
- Unscoped (visible to all): ZOM-567, cmt_c9a6660d81e067ad1de7, 689b662c60cbe40b9f4a97ae, 689b66a450734c26dcdf6291, 9b0185e445572aeee9f27d35.
- No designed denial: denied_probes is empty; other people's mailbox and calendar copies are companions, never evidence (the review is cited only by Frederick's copy evt_fd469c29811879519c2c96).

## 1.F Collision

Every id the SQL mints was looked up over its full base collection (`tools/hg.py records --request plan/id_checks_sql.json`, `hg.py search lookup`):
- drive: 53631 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- gcal: 10395 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- trello_cards: 803 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- trello_actions: 5252 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- trello_checklists: 54 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- contacts: 170 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- linear_issues: 3687 base records checked, scan_complete True, 0 matches (plan/id_checks_sql.out.json).
- slack: the 7 seeded message ids over messages/*/*.json — 4,840 of 4,840 files, scan_complete true, 0 hits (plan/slack_lookup.out.json); the new Spotlight note fc2f69c06b333f6c54dfd63d455c3958 (C07C2866011/1758134460.899858) also 0 hits in the 16 #executives month files.
- gmail: thread ids (mailbox/((ms << 20) + bits)) and RFC Message-IDs are minted per seeded time; base_check Check A (full-collection uniqueness through its base caches) PASS, see Self-review.
- Header tokens: PERSON_9701–9735_EMAIL and SVC_9701_EMAIL are new identities (census in plan/token_census.txt); PERSON_2694 (ESG partner), PERSON_2599 (ESG intake) and PERSON_0527 (Balancy) are reused only for their own people.
- Body tokens: none minted.

## Record ledger

One row per SQL statement (inserts and the companion updates), in SQL order.

| # | SQL line | Table | Id | Manifest element | Carrier | Reach | Discovery role |
|---|---|---|---|---|---|---|---|
| 1 | L6 | gdrive.drive_files | f_b98287f6f80fe431a71209 | H1 / K2 / K3 / K4 / T8 / T9 | ● | Drive owner or share | claim met first |
| 2 | L9 | gdrive.drive_files | f_7bacf15c4e8eea1a52dcd4 | H1 decoy | ● | Drive owner or share | decoy |
| 3 | L11 | gdrive.drive_files | f_3b06917a41dd59308d890b | K12 | ● | Drive owner or share | connecting |
| 4 | L13 | gdrive.drive_files | d_80a8c04753ba82ba4ba6a5 | A2 | ● | Drive owner or share | write target |
| 5 | L15 | gdrive.drive_files | f_846ddc38b2aab3d2ed3fcb | K8 | ● | Drive owner or share | authority (log format) · write target folder |
| 6 | L17 | gdrive.drive_files | f_05f0a451b29b19a1c0b90f | K9 | ● | Drive owner or share | write target |
| 7 | L19 | gdrive.drive_files | f_9d6edd4922d8130ccd272e | T14 | ● | Drive owner or share | connecting |
| 8 | L21 | gdrive.drive_files | d_ffa3e6e473da7e6523614f | companion | ● | Drive owner or share | connecting |
| 9 | L23 | gdrive.drive_files | f_fba21c2d5d4bbb02983961 | cohort paper: Framewell | ● | Drive owner or share | connecting (per-company evidence) |
| 10 | L25 | gdrive.drive_files | f_6c212cbfb31c3ded44ef8a | cohort paper: Pingwise | ● | Drive owner or share | connecting (per-company evidence) |
| 11 | L27 | gdrive.drive_files | f_8d0e0e3ae076b2f745e7e2 | T5 / cohort paper: Clipforge | ● | Drive owner or share | claim met first |
| 12 | L29 | gdrive.drive_files | f_614f88a28a2f0cf1b88408 | cohort paper: Pixel Harbor Events | ● | Drive owner or share | connecting (per-company evidence) |
| 13 | L31 | gdrive.drive_files | f_5dbbaf5b251d5261427eb1 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 14 | L33 | gdrive.drive_files | f_9d4639f91c93478d888f4b | cohort paper: Brightlane Studio | ● | Drive owner or share | connecting (per-company evidence) |
| 15 | L35 | gdrive.drive_files | f_2686da1086bfcc2fba3f57 | cohort paper: Soundvault | ● | Drive owner or share | connecting (per-company evidence) |
| 16 | L37 | gdrive.drive_files | f_4bdfb8e0c47288087c7bba | cohort paper: Reviewly | ● | Drive owner or share | connecting (per-company evidence) |
| 17 | L39 | gdrive.drive_files | f_5b961c9c6887d31dcd2ee2 | cohort paper: Streamcast Talent | ● | Drive owner or share | connecting (per-company evidence) |
| 18 | L41 | gdrive.drive_files | f_34ba4ac9a0f0fa4fd34e9e | cohort paper: Lingora | ● | Drive owner or share | connecting (per-company evidence) |
| 19 | L43 | gdrive.drive_files | f_41a9ea5036a231989745b2 | cohort paper: Panelpulse | ● | Drive owner or share | connecting (per-company evidence) |
| 20 | L45 | gdrive.drive_files | f_a9593b0bf23b760e2972c7 | cohort paper: Ascendo | ● | Drive owner or share | connecting (per-company evidence) |
| 21 | L47 | gdrive.drive_files | f_54c2b4e172bb73a4a19845 | cohort paper: Wishwave | ● | Drive owner or share | connecting (per-company evidence) |
| 22 | L49 | gdrive.drive_files | f_2715771ae5f0358ad39aa9 | cohort paper: Vaultline | ● | Drive owner or share | connecting (per-company evidence) |
| 23 | L51 | gdrive.drive_files | f_cfb172dea30b9f6ac8a340 | cohort paper: Certwell | ● | Drive owner or share | connecting (per-company evidence) |
| 24 | L53 | gdrive.drive_files | f_6252955f500f81e3aacbef | cohort paper: Kinetic Arcade | ● | Drive owner or share | connecting (per-company evidence) |
| 25 | L55 | gdrive.drive_files | f_a227b14f03e12005fe8324 | cohort paper: Lumencloud | ● | Drive owner or share | connecting (per-company evidence) |
| 26 | L57 | gdrive.drive_files | f_9d1e0270574584de0eb92c | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 27 | L59 | gdrive.drive_files | f_2ae7e3ee3220b628391234 | cohort paper: Orbit Store | ● | Drive owner or share | connecting (per-company evidence) |
| 28 | L61 | gdrive.drive_files | f_71a95593c736b3baf45f91 | cohort paper: Markward | ● | Drive owner or share | connecting (per-company evidence) |
| 29 | L63 | gdrive.drive_files | f_9a7fc4a3e45e4394227fa5 | cohort paper: Playfuse | ● | Drive owner or share | connecting (per-company evidence) |
| 30 | L65 | gdrive.drive_files | f_f6701704e5659b05d9530f | cohort paper: Glyphworks | ● | Drive owner or share | connecting (per-company evidence) |
| 31 | L67 | gdrive.drive_files | f_eb94c65ce9f273c6b5a579 | cohort paper: Cloudlark | ● | Drive owner or share | connecting (per-company evidence) |
| 32 | L69 | gdrive.drive_files | f_68e288146ba0eee9fc17fa | cohort paper: Echohall | ● | Drive owner or share | connecting (per-company evidence) |
| 33 | L71 | gdrive.drive_files | f_a9bb79c86b8b7b92083785 | cohort paper: Pressbeam | ● | Drive owner or share | connecting (per-company evidence) |
| 34 | L73 | gdrive.drive_files | f_be21bac5d50e291ebfbe2b | T17 / cohort paper: Retainly | ● | Drive owner or share | connecting (per-company evidence) |
| 35 | L75 | gdrive.drive_files | f_af809bf6325b452edc8476 | cohort paper: Quillcraft | ● | Drive owner or share | connecting (per-company evidence) |
| 36 | L77 | gdrive.drive_files | f_6d13a63be892a29f796b78 | cohort paper: Tilecast | ● | Drive owner or share | connecting (per-company evidence) |
| 37 | L79 | gdrive.drive_files | f_e916ab7563891481ab3b16 | cohort paper: Benchmarkly | ● | Drive owner or share | connecting (per-company evidence) |
| 38 | L81 | gdrive.drive_files | f_6963d4d30aceef4f88966a | cohort paper: Loopnote | ● | Drive owner or share | connecting (per-company evidence) |
| 39 | L83 | gdrive.drive_files | f_17878d7b82fafcee79bfe7 | cohort paper: Driftwood Audio | ● | Drive owner or share | connecting (per-company evidence) |
| 40 | L85 | gdrive.drive_files | f_e81c6ef89513cac632700a | cohort paper: Motive Forge | ● | Drive owner or share | connecting (per-company evidence) |
| 41 | L87 | gdrive.drive_files | f_9d9cf4e53b1c8607f9c869 | cohort paper: Spotlight Fest | ● | Drive owner or share | connecting (per-company evidence) |
| 42 | L89 | gdocs.docs_documents | f_b98287f6f80fe431a71209 | H1 / K2 / K3 / K4 / T8 / T9 | ● | Drive owner or share | claim met first |
| 43 | L92 | gdocs.docs_documents | f_7bacf15c4e8eea1a52dcd4 | H1 decoy | ● | Drive owner or share | decoy |
| 44 | L94 | gdocs.docs_documents | f_3b06917a41dd59308d890b | K12 | ● | Drive owner or share | connecting |
| 45 | L96 | gdocs.docs_documents | f_846ddc38b2aab3d2ed3fcb | K8 | ● | Drive owner or share | authority (log format) · write target folder |
| 46 | L98 | gdocs.docs_documents | f_fba21c2d5d4bbb02983961 | cohort paper: Framewell | ● | Drive owner or share | connecting (per-company evidence) |
| 47 | L100 | gdocs.docs_documents | f_6c212cbfb31c3ded44ef8a | cohort paper: Pingwise | ● | Drive owner or share | connecting (per-company evidence) |
| 48 | L102 | gdocs.docs_documents | f_8d0e0e3ae076b2f745e7e2 | T5 / cohort paper: Clipforge | ● | Drive owner or share | claim met first |
| 49 | L104 | gdocs.docs_documents | f_614f88a28a2f0cf1b88408 | cohort paper: Pixel Harbor Events | ● | Drive owner or share | connecting (per-company evidence) |
| 50 | L106 | gdocs.docs_documents | f_9d4639f91c93478d888f4b | cohort paper: Brightlane Studio | ● | Drive owner or share | connecting (per-company evidence) |
| 51 | L108 | gdocs.docs_documents | f_2686da1086bfcc2fba3f57 | cohort paper: Soundvault | ● | Drive owner or share | connecting (per-company evidence) |
| 52 | L110 | gdocs.docs_documents | f_4bdfb8e0c47288087c7bba | cohort paper: Reviewly | ● | Drive owner or share | connecting (per-company evidence) |
| 53 | L112 | gdocs.docs_documents | f_5b961c9c6887d31dcd2ee2 | cohort paper: Streamcast Talent | ● | Drive owner or share | connecting (per-company evidence) |
| 54 | L114 | gdocs.docs_documents | f_34ba4ac9a0f0fa4fd34e9e | cohort paper: Lingora | ● | Drive owner or share | connecting (per-company evidence) |
| 55 | L116 | gdocs.docs_documents | f_41a9ea5036a231989745b2 | cohort paper: Panelpulse | ● | Drive owner or share | connecting (per-company evidence) |
| 56 | L118 | gdocs.docs_documents | f_a9593b0bf23b760e2972c7 | cohort paper: Ascendo | ● | Drive owner or share | connecting (per-company evidence) |
| 57 | L120 | gdocs.docs_documents | f_54c2b4e172bb73a4a19845 | cohort paper: Wishwave | ● | Drive owner or share | connecting (per-company evidence) |
| 58 | L122 | gdocs.docs_documents | f_2715771ae5f0358ad39aa9 | cohort paper: Vaultline | ● | Drive owner or share | connecting (per-company evidence) |
| 59 | L124 | gdocs.docs_documents | f_cfb172dea30b9f6ac8a340 | cohort paper: Certwell | ● | Drive owner or share | connecting (per-company evidence) |
| 60 | L126 | gdocs.docs_documents | f_6252955f500f81e3aacbef | cohort paper: Kinetic Arcade | ● | Drive owner or share | connecting (per-company evidence) |
| 61 | L128 | gdocs.docs_documents | f_a227b14f03e12005fe8324 | cohort paper: Lumencloud | ● | Drive owner or share | connecting (per-company evidence) |
| 62 | L130 | gdocs.docs_documents | f_2ae7e3ee3220b628391234 | cohort paper: Orbit Store | ● | Drive owner or share | connecting (per-company evidence) |
| 63 | L132 | gdocs.docs_documents | f_71a95593c736b3baf45f91 | cohort paper: Markward | ● | Drive owner or share | connecting (per-company evidence) |
| 64 | L134 | gdocs.docs_documents | f_9a7fc4a3e45e4394227fa5 | cohort paper: Playfuse | ● | Drive owner or share | connecting (per-company evidence) |
| 65 | L136 | gdocs.docs_documents | f_f6701704e5659b05d9530f | cohort paper: Glyphworks | ● | Drive owner or share | connecting (per-company evidence) |
| 66 | L138 | gdocs.docs_documents | f_eb94c65ce9f273c6b5a579 | cohort paper: Cloudlark | ● | Drive owner or share | connecting (per-company evidence) |
| 67 | L140 | gdocs.docs_documents | f_68e288146ba0eee9fc17fa | cohort paper: Echohall | ● | Drive owner or share | connecting (per-company evidence) |
| 68 | L142 | gdocs.docs_documents | f_a9bb79c86b8b7b92083785 | cohort paper: Pressbeam | ● | Drive owner or share | connecting (per-company evidence) |
| 69 | L144 | gdocs.docs_documents | f_be21bac5d50e291ebfbe2b | T17 / cohort paper: Retainly | ● | Drive owner or share | connecting (per-company evidence) |
| 70 | L146 | gdocs.docs_documents | f_af809bf6325b452edc8476 | cohort paper: Quillcraft | ● | Drive owner or share | connecting (per-company evidence) |
| 71 | L148 | gdocs.docs_documents | f_6d13a63be892a29f796b78 | cohort paper: Tilecast | ● | Drive owner or share | connecting (per-company evidence) |
| 72 | L150 | gdocs.docs_documents | f_e916ab7563891481ab3b16 | cohort paper: Benchmarkly | ● | Drive owner or share | connecting (per-company evidence) |
| 73 | L152 | gdocs.docs_documents | f_6963d4d30aceef4f88966a | cohort paper: Loopnote | ● | Drive owner or share | connecting (per-company evidence) |
| 74 | L154 | gdocs.docs_documents | f_17878d7b82fafcee79bfe7 | cohort paper: Driftwood Audio | ● | Drive owner or share | connecting (per-company evidence) |
| 75 | L156 | gdocs.docs_documents | f_e81c6ef89513cac632700a | cohort paper: Motive Forge | ● | Drive owner or share | connecting (per-company evidence) |
| 76 | L158 | gdocs.docs_documents | f_9d9cf4e53b1c8607f9c869 | cohort paper: Spotlight Fest | ● | Drive owner or share | connecting (per-company evidence) |
| 77 | L160 | gsheets.sheets_spreadsheets | f_05f0a451b29b19a1c0b90f | K9 | ● | Drive owner or share | write target |
| 78 | L163 | gsheets.sheets_sheets | f_05f0a451b29b19a1c0b90f#Log | K9 | ● | Drive owner or share | write target |
| 79 | L165 | gsheets.sheets_spreadsheets | f_9d6edd4922d8130ccd272e | T14 | ● | Drive owner or share | connecting |
| 80 | L167 | gsheets.sheets_sheets | f_9d6edd4922d8130ccd272e#Tracker | T14 | ● | Drive owner or share | connecting |
| 81 | L169 | gslides.slides_presentations | f_5dbbaf5b251d5261427eb1 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 82 | L172 | gslides.slides_pages | f_5dbbaf5b251d5261427eb1#slide_bd9e4b92fdc9 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 83 | L174 | gslides.slides_page_elements | f_5dbbaf5b251d5261427eb1#el_8834f6ce6725 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 84 | L176 | gslides.slides_page_elements | f_5dbbaf5b251d5261427eb1#el_fb76c317bfff | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 85 | L178 | gslides.slides_pages | f_5dbbaf5b251d5261427eb1#slide_e799ff88ca1a | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 86 | L180 | gslides.slides_page_elements | f_5dbbaf5b251d5261427eb1#el_877e3d66198b | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 87 | L182 | gslides.slides_page_elements | f_5dbbaf5b251d5261427eb1#el_ef57d97ed3b0 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 88 | L184 | gslides.slides_pages | f_5dbbaf5b251d5261427eb1#slide_07d1f58819b2 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 89 | L186 | gslides.slides_page_elements | f_5dbbaf5b251d5261427eb1#el_15f716be26f7 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 90 | L188 | gslides.slides_page_elements | f_5dbbaf5b251d5261427eb1#el_9b987d530635 | cohort paper: Lanternfly Publishing | ● | Drive owner or share | connecting (per-company evidence) |
| 91 | L190 | gslides.slides_presentations | f_9d1e0270574584de0eb92c | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 92 | L192 | gslides.slides_pages | f_9d1e0270574584de0eb92c#slide_3818928cc5b4 | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 93 | L194 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_0fc3f5f3ace9 | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 94 | L196 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_a0dbd46db1a6 | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 95 | L198 | gslides.slides_pages | f_9d1e0270574584de0eb92c#slide_111fef17ef5d | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 96 | L200 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_53e619c8898a | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 97 | L202 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_322d7da20cb6 | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 98 | L204 | gslides.slides_pages | f_9d1e0270574584de0eb92c#slide_52be557fc2cd | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 99 | L206 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_d7939404bc4a | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 100 | L208 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_6a07a17c39ac | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 101 | L210 | gslides.slides_pages | f_9d1e0270574584de0eb92c#slide_2961165dab03 | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 102 | L212 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_34a6e6e73388 | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 103 | L214 | gslides.slides_page_elements | f_9d1e0270574584de0eb92c#el_1bf4ee220b8b | cohort paper: Bundlehouse | ● | Drive owner or share | connecting (per-company evidence) |
| 104 | L216 | slack.slack_messages | 0573efd133cabdb1acde61e68571aa82 | H2 decoy / T7 | ● | #executives member | claim met first |
| 105 | L219 | slack.slack_messages | 80ced6c98e9bd0aa1ccb462488f1746d | T10 | ● | #executives member | connecting |
| 106 | L221 | slack.slack_messages | fc2f69c06b333f6c54dfd63d455c3958 | T19 | ● | #executives member | connecting |
| 107 | L223 | slack.slack_messages | 7e88911312fa9a969f0659a105af59a3 | K10 / T9 | ● | #executives member | overturning |
| 108 | L225 | slack.slack_messages | 9fb2d23420c7e01ca163571f4129c912 | T2 | ● | #executives member | overturning |
| 109 | L227 | slack.slack_messages (UPDATE) | c41d37178fca394c135408d2b38e0879 | companion | ● | #executives member | companion (counters / snippet) |
| 110 | L228 | slack.slack_messages | 418a0a6d6c29b7b67ce0ffb270c78c1e | T3 | ● | DM member | connecting |
| 111 | L230 | slack.slack_messages (UPDATE) | c148cae9de21cd26027d8bbc89bb127c | companion | ● | #executives member | companion (counters / snippet) |
| 112 | L231 | trello.trello_cards | 689b662c60cbe40b9f4a97ae | H3 / K6 / T4 | ● | unscoped service | authority |
| 113 | L234 | trello.trello_actions | 689b662ce06ba74821d997f4 | companion | ● | unscoped service | connecting |
| 114 | L236 | trello.trello_checklists | 689b66a4b56c4354aa1efab8 | companion | ● | unscoped service | connecting |
| 115 | L238 | trello.trello_check_items | 689b66a46f62e8218a32924c | companion | ● | unscoped service | connecting |
| 116 | L240 | trello.trello_check_items | 689b66a49d4295a2b3145041 | companion | ● | unscoped service | connecting |
| 117 | L242 | trello.trello_check_items | 689b66a450734c26dcdf6291 | companion | ● | unscoped service | connecting |
| 118 | L244 | trello.trello_check_items | 689b66a4c5bb6c266c1cedba | companion | ● | unscoped service | connecting |
| 119 | L246 | trello.trello_actions | 689b66a48cfc5e5bd6608131 | companion | ● | unscoped service | connecting |
| 120 | L248 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844732913254784171 | K1 / K13 / K14 | ● | Frederick's mailbox | connecting |
| 121 | L251 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com> | A1 / K1 / K13 / K14 | ● | Frederick's mailbox | first link |
| 122 | L253 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844732913254960629 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 123 | L255 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 124 | L257 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844177063117059830 | H2 / K5 / T7 | ● | Frederick's mailbox | authority |
| 125 | L259 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> | H2 / K5 / T7 | ● | Frederick's mailbox | claim met first |
| 126 | L261 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844177063117003267 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 127 | L263 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 128 | L265 | gmail.gmail_threads | robert@harmonygames.co/1844177063117516849 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 129 | L267 | gmail.gmail_messages | robert@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 130 | L269 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844177063117181908 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 131 | L271 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 132 | L273 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1844177063117059830 | H2 / K5 / T7 | ● | Frederick's mailbox | companion (counters / snippet) |
| 133 | L274 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> | H2 / K5 / T7 | ● | Frederick's mailbox | overturning |
| 134 | L276 | gmail.gmail_threads (UPDATE) | leonard.hayes@harmonygames.co/1844177063117003267 | companion | ● | other mailbox | companion (counters / snippet) |
| 135 | L277 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 136 | L279 | gmail.gmail_threads (UPDATE) | robert@harmonygames.co/1844177063117516849 | companion | ● | other mailbox | companion (counters / snippet) |
| 137 | L280 | gmail.gmail_messages | robert@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 138 | L282 | gmail.gmail_threads (UPDATE) | arthur.blake@harmonygames.co/1844177063117181908 | companion | ● | other mailbox | companion (counters / snippet) |
| 139 | L283 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 140 | L285 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843067564852153540 | T5 / cohort: Clipforge (Paylane notice) | ● | Frederick's mailbox | connecting (per-company evidence) |
| 141 | L287 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> | T5 / cohort: Clipforge (Paylane notice) | ● | Frederick's mailbox | overturning |
| 142 | L289 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843618067251203081 | T2 / cohort: Framewell | ● | Frederick's mailbox | connecting (per-company evidence) |
| 143 | L291 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAGJkuaxoKn_J2zxTzhLswrYwOGA_wA5IXe9v747@mail.gmail.com> | T2 / cohort: Framewell | ● | Frederick's mailbox | claim met first |
| 144 | L293 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844157874176168845 | T4 / cohort: Pingwise | ● | Frederick's mailbox | connecting (per-company evidence) |
| 145 | L295 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAZgisbRwHgHd3Hk_E9LYMNIOFiMZminBj4K2tWc@mail.gmail.com> | T4 / cohort: Pingwise | ● | Frederick's mailbox | connecting (per-company evidence) |
| 146 | L297 | gmail.gmail_threads | frederick.stone@harmonygames.co/1837102635418059486 | cohort: Clipforge | ● | Frederick's mailbox | connecting (per-company evidence) |
| 147 | L299 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com> | cohort: Clipforge | ● | Frederick's mailbox | connecting (per-company evidence) |
| 148 | L301 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1837102635418059486 | cohort: Clipforge | ● | Frederick's mailbox | companion (counters / snippet) |
| 149 | L302 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAFEbdSLTqGx4K9ylCWMjfozRDorLWGyAc5mo6e7@mail.gmail.com> | cohort: Clipforge | ● | Frederick's mailbox | connecting (per-company evidence) |
| 150 | L304 | gmail.gmail_threads | frederick.stone@harmonygames.co/1835288808653226583 | T6 / cohort: Pixel Harbor Events | ● | Frederick's mailbox | connecting (per-company evidence) |
| 151 | L306 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com> | T6 / cohort: Pixel Harbor Events | ● | Frederick's mailbox | connecting (per-company evidence) |
| 152 | L308 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1835288808653226583 | T6 / cohort: Pixel Harbor Events | ● | Frederick's mailbox | companion (counters / snippet) |
| 153 | L309 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CALCA8gxcwd0yOaLVGO1KlKBHNjV4IHaI4Lm7Shq@mail.gmail.com> | T6 / cohort: Pixel Harbor Events | ● | Frederick's mailbox | connecting (per-company evidence) |
| 154 | L311 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842800807116855774 | T3 / cohort: Lanternfly Publishing | ● | Frederick's mailbox | connecting (per-company evidence) |
| 155 | L313 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAUTttDNR2kwXReKZgzK8GvbJXxwUnrHN42rwhn1@mail.gmail.com> | T3 / cohort: Lanternfly Publishing | ● | Frederick's mailbox | connecting (per-company evidence) |
| 156 | L315 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842800807116855774 | T3 / cohort: Lanternfly Publishing | ● | Frederick's mailbox | companion (counters / snippet) |
| 157 | L316 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAY11pXWEb2u5uCxBJhKpklYcHpViFPzYgETaeTx@mail.gmail.com> | T3 / cohort: Lanternfly Publishing | ● | Frederick's mailbox | connecting (per-company evidence) |
| 158 | L318 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842800807116855774 | T3 / cohort: Lanternfly Publishing | ● | Frederick's mailbox | companion (counters / snippet) |
| 159 | L319 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CArrsRpTwnF5vDz3j8sB1bdi-2N8lorF7bNSSbk-@mail.gmail.com> | T3 / cohort: Lanternfly Publishing | ● | Frederick's mailbox | connecting (per-company evidence) |
| 160 | L321 | gmail.gmail_threads | frederick.stone@harmonygames.co/1841809902797646290 | cohort: Brightlane Studio | ● | Frederick's mailbox | connecting (per-company evidence) |
| 161 | L323 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA0uGW7WigxQ0mENWo-aIuiEpfLWJbrhuxMJjS0A@mail.gmail.com> | cohort: Brightlane Studio | ● | Frederick's mailbox | connecting (per-company evidence) |
| 162 | L325 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1841809902797646290 | cohort: Brightlane Studio | ● | Frederick's mailbox | companion (counters / snippet) |
| 163 | L326 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA-xgF65XCwo6QXURZM_eCJcAClcs_LfeftzR27P@mail.gmail.com> | cohort: Brightlane Studio | ● | Frederick's mailbox | connecting (per-company evidence) |
| 164 | L328 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842719647334876669 | cohort: Soundvault | ● | Frederick's mailbox | connecting (per-company evidence) |
| 165 | L330 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdDglIne-JLPfhnQyZF8qjaAlhus3WbzeVF5FoW@mail.gmail.com> | cohort: Soundvault | ● | Frederick's mailbox | connecting (per-company evidence) |
| 166 | L332 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842719647334876669 | cohort: Soundvault | ● | Frederick's mailbox | companion (counters / snippet) |
| 167 | L333 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAeW3ux2LavW4Rp-PXhOt5Xhvgtjzfq1XU3eJO_C@mail.gmail.com> | cohort: Soundvault | ● | Frederick's mailbox | connecting (per-company evidence) |
| 168 | L335 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842719647334876669 | cohort: Soundvault | ● | Frederick's mailbox | companion (counters / snippet) |
| 169 | L336 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAa-jv7GWQa7i06XwUWtNIJ_DInBkE5Qi4Y8PmMT@mail.gmail.com> | cohort: Soundvault | ● | Frederick's mailbox | connecting (per-company evidence) |
| 170 | L338 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843712439092112354 | cohort: Reviewly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 171 | L340 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAN4G0SGg1BdZ4ApKmfoiXizgNPn1Wz1lObQmvmL@mail.gmail.com> | cohort: Reviewly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 172 | L342 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843712439092112354 | cohort: Reviewly | ● | Frederick's mailbox | companion (counters / snippet) |
| 173 | L343 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAEcTJxNSlNWdzmdlv0uAxA5LWo-4JRqmN_lbkGs@mail.gmail.com> | cohort: Reviewly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 174 | L345 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842998987980893279 | cohort: Streamcast Talent | ● | Frederick's mailbox | connecting (per-company evidence) |
| 175 | L347 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAKGQuOVQjttk8qpLC2bhGl1ZJ4oRI7nPbIzP6mR@mail.gmail.com> | cohort: Streamcast Talent | ● | Frederick's mailbox | connecting (per-company evidence) |
| 176 | L349 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842998987980893279 | cohort: Streamcast Talent | ● | Frederick's mailbox | companion (counters / snippet) |
| 177 | L350 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAIauDHOvbuHs1D8VFmRdi2YfR01quJPqo1ZiQZJ@mail.gmail.com> | cohort: Streamcast Talent | ● | Frederick's mailbox | connecting (per-company evidence) |
| 178 | L352 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842168515789422611 | cohort: Lingora | ● | Frederick's mailbox | connecting (per-company evidence) |
| 179 | L354 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAIMbUgCSlodxbiO4p94ujFhTeSTtN2swRzPIQL0@mail.gmail.com> | cohort: Lingora | ● | Frederick's mailbox | connecting (per-company evidence) |
| 180 | L356 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842168515789422611 | cohort: Lingora | ● | Frederick's mailbox | companion (counters / snippet) |
| 181 | L357 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdgQm_LmTWyiKsAANkrEQIXisEv_9hNMklsIUx_@mail.gmail.com> | cohort: Lingora | ● | Frederick's mailbox | connecting (per-company evidence) |
| 182 | L359 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842168515789422611 | cohort: Lingora | ● | Frederick's mailbox | companion (counters / snippet) |
| 183 | L360 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAb3f_RRKlDbfktS3_Cu7qnXPyTybHnS1K2Eq3b7@mail.gmail.com> | cohort: Lingora | ● | Frederick's mailbox | connecting (per-company evidence) |
| 184 | L362 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842353484595925809 | cohort: Panelpulse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 185 | L364 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA1qNRLdbV7Qkr9KCNYq0gKKHAL3Hn7aap534PvX@mail.gmail.com> | cohort: Panelpulse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 186 | L366 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842353484595925809 | cohort: Panelpulse | ● | Frederick's mailbox | companion (counters / snippet) |
| 187 | L367 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAM5dEEI7CWxEdApgrQnK2XC211TZL1KF-WNUpsB@mail.gmail.com> | cohort: Panelpulse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 188 | L369 | gmail.gmail_threads | frederick.stone@harmonygames.co/1841081352192260725 | cohort: Ascendo | ● | Frederick's mailbox | connecting (per-company evidence) |
| 189 | L371 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAyf6nlOFNNbNBnx3fo0wtMQ8n9aXQTM_GxC86hB@mail.gmail.com> | cohort: Ascendo | ● | Frederick's mailbox | connecting (per-company evidence) |
| 190 | L373 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1841081352192260725 | cohort: Ascendo | ● | Frederick's mailbox | companion (counters / snippet) |
| 191 | L374 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA0BbU6OEljE3nhaS2pWMojXL9GJ_kYqFO8JTtP2@mail.gmail.com> | cohort: Ascendo | ● | Frederick's mailbox | connecting (per-company evidence) |
| 192 | L376 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843538794906427760 | cohort: Wishwave | ● | Frederick's mailbox | connecting (per-company evidence) |
| 193 | L378 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAXYl4kZwjniI2DACcpaEMWNhajoK6HBVw4uaXGD@mail.gmail.com> | cohort: Wishwave | ● | Frederick's mailbox | connecting (per-company evidence) |
| 194 | L380 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843538794906427760 | cohort: Wishwave | ● | Frederick's mailbox | companion (counters / snippet) |
| 195 | L381 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAHavdKpt7nR3fxojrxKL1PYVBWt8ridR2XEm01t@mail.gmail.com> | cohort: Wishwave | ● | Frederick's mailbox | connecting (per-company evidence) |
| 196 | L383 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843980455117084538 | cohort: Vaultline | ● | Frederick's mailbox | connecting (per-company evidence) |
| 197 | L385 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CASRfZCkXuHwLJPLUeim95W1qFlzEaz37BReSyJz@mail.gmail.com> | cohort: Vaultline | ● | Frederick's mailbox | connecting (per-company evidence) |
| 198 | L387 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844067277209770126 | cohort: Certwell | ● | Frederick's mailbox | connecting (per-company evidence) |
| 199 | L389 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CApaJB4i_PhvJp_95Q3bE-l9yDV4x096tsJobB11@mail.gmail.com> | cohort: Certwell | ● | Frederick's mailbox | connecting (per-company evidence) |
| 200 | L391 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842895178957083445 | cohort: Kinetic Arcade | ● | Frederick's mailbox | connecting (per-company evidence) |
| 201 | L393 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA3aUrexaU1ytNuMja5-4b03__ehILzpWLqaO5Yx@mail.gmail.com> | cohort: Kinetic Arcade | ● | Frederick's mailbox | connecting (per-company evidence) |
| 202 | L395 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842895178957083445 | cohort: Kinetic Arcade | ● | Frederick's mailbox | companion (counters / snippet) |
| 203 | L396 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAwVKKP1C-1rXHFCWIgbB9PjITqgDI3ziZAK9984@mail.gmail.com> | cohort: Kinetic Arcade | ● | Frederick's mailbox | connecting (per-company evidence) |
| 204 | L398 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842991438234544282 | cohort: Lumencloud | ● | Frederick's mailbox | connecting (per-company evidence) |
| 205 | L400 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAMStwDpDMa-TpyL6LYTnlEtJ1wHg3ijdeUe3kRU@mail.gmail.com> | cohort: Lumencloud | ● | Frederick's mailbox | connecting (per-company evidence) |
| 206 | L402 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842991438234544282 | cohort: Lumencloud | ● | Frederick's mailbox | companion (counters / snippet) |
| 207 | L403 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA2AOLHmh-RU9NexSr5s80P3mUbj-J4_hr59arcw@mail.gmail.com> | cohort: Lumencloud | ● | Frederick's mailbox | connecting (per-company evidence) |
| 208 | L405 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843442535629243130 | cohort: Bundlehouse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 209 | L407 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAO2B00xDzwszNF3Ilw5PbJg0oZh1fnZ-QLkS2Jt@mail.gmail.com> | cohort: Bundlehouse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 210 | L409 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843442535629243130 | cohort: Bundlehouse | ● | Frederick's mailbox | companion (counters / snippet) |
| 211 | L410 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAlSBl5tSj6BhvNqcMHhDChnKE3Fcp7fgMJdKNtH@mail.gmail.com> | cohort: Bundlehouse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 212 | L412 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843708664218314020 | cohort: Orbit Store | ● | Frederick's mailbox | connecting (per-company evidence) |
| 213 | L414 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdma6oOdAQE9dig43QVuUgNp0etrBmzar36esvm@mail.gmail.com> | cohort: Orbit Store | ● | Frederick's mailbox | connecting (per-company evidence) |
| 214 | L416 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843708664218314020 | cohort: Orbit Store | ● | Frederick's mailbox | companion (counters / snippet) |
| 215 | L417 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAo7WkZSvPT7fVQd40F1HezmilqIw9AoAb6_uTM2@mail.gmail.com> | cohort: Orbit Store | ● | Frederick's mailbox | connecting (per-company evidence) |
| 216 | L419 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842802694553769659 | cohort: Markward | ● | Frederick's mailbox | connecting (per-company evidence) |
| 217 | L421 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAkJn3vHo1ZSVJM1fxECsBF9x2KnMEi9FvdW5zAr@mail.gmail.com> | cohort: Markward | ● | Frederick's mailbox | connecting (per-company evidence) |
| 218 | L423 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842802694553769659 | cohort: Markward | ● | Frederick's mailbox | companion (counters / snippet) |
| 219 | L424 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAjzt3v0v5AIRijm5FdJu1yYv5Q-LMNqpRFDYAqb@mail.gmail.com> | cohort: Markward | ● | Frederick's mailbox | connecting (per-company evidence) |
| 220 | L426 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844256020889910750 | cohort: Playfuse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 221 | L428 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAWCBU--R8_Q4xxjtvPvDrzjjgqqRxz_flrPVZo6@mail.gmail.com> | cohort: Playfuse | ● | Frederick's mailbox | connecting (per-company evidence) |
| 222 | L430 | gmail.gmail_threads | frederick.stone@harmonygames.co/1839631800730308867 | T20 / cohort: Hootline | ● | Frederick's mailbox | connecting (per-company evidence) |
| 223 | L432 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAat3tn3W0qDDTcWKmBYwD1Jnj1j_YU1h2NqzJZj@mail.gmail.com> | T20 / cohort: Hootline | ● | Frederick's mailbox | connecting (per-company evidence) |
| 224 | L434 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1839631800730308867 | T20 / cohort: Hootline | ● | Frederick's mailbox | companion (counters / snippet) |
| 225 | L435 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com> | T20 / cohort: Hootline | ● | Frederick's mailbox | connecting (per-company evidence) |
| 226 | L437 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843350051225919345 | cohort: Glyphworks | ● | Frederick's mailbox | connecting (per-company evidence) |
| 227 | L439 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAK5OtyGBKIjnQ7R24aq6RTWoGDUT4Dvg3I21YVO@mail.gmail.com> | cohort: Glyphworks | ● | Frederick's mailbox | connecting (per-company evidence) |
| 228 | L441 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843350051225919345 | cohort: Glyphworks | ● | Frederick's mailbox | companion (counters / snippet) |
| 229 | L442 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAWFrjpQqU9OPoIfzxLgVsbT6sBJa8bgCCjzFYiF@mail.gmail.com> | cohort: Glyphworks | ● | Frederick's mailbox | connecting (per-company evidence) |
| 230 | L444 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843350051225919345 | cohort: Glyphworks | ● | Frederick's mailbox | companion (counters / snippet) |
| 231 | L445 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CApanLB9xL5jrjcNSzDTWYvE6RiWdfZchZxr4q3K@mail.gmail.com> | cohort: Glyphworks | ● | Frederick's mailbox | connecting (per-company evidence) |
| 232 | L447 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843078260327282996 | cohort: Cloudlark | ● | Frederick's mailbox | connecting (per-company evidence) |
| 233 | L449 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAXUVl-vI7c6T4f22vI41yY2P83JxLRUdeHW1-hC@mail.gmail.com> | cohort: Cloudlark | ● | Frederick's mailbox | connecting (per-company evidence) |
| 234 | L451 | gmail.gmail_threads | frederick.stone@harmonygames.co/1841538111898044975 | cohort: Echohall | ● | Frederick's mailbox | connecting (per-company evidence) |
| 235 | L453 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAF3j_dVe4Smvh19S7lyCBLjtao8Qe8vwV9yybpg@mail.gmail.com> | cohort: Echohall | ● | Frederick's mailbox | connecting (per-company evidence) |
| 236 | L455 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1841538111898044975 | cohort: Echohall | ● | Frederick's mailbox | companion (counters / snippet) |
| 237 | L456 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAHV7my-sLo9CEzISCj6j5YvPRBW1ReAHi-SrN7V@mail.gmail.com> | cohort: Echohall | ● | Frederick's mailbox | connecting (per-company evidence) |
| 238 | L458 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842983888486665921 | cohort: Pressbeam | ● | Frederick's mailbox | connecting (per-company evidence) |
| 239 | L460 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAGdptfs7cIHOLvLgF6LBpN_8DHhsOmA8Oqoddfh@mail.gmail.com> | cohort: Pressbeam | ● | Frederick's mailbox | connecting (per-company evidence) |
| 240 | L462 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843346276352069546 | cohort: Retainly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 241 | L464 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAOHCdeuLRHpqtIPQZRUGefwtjIwm5BrmgGS_Loo@mail.gmail.com> | cohort: Retainly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 242 | L466 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842262887629456494 | cohort: Quillcraft | ● | Frederick's mailbox | connecting (per-company evidence) |
| 243 | L468 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAi_XBSxfgfRVpvhsqJCtZzn_v40OoXxKbCxhQb8@mail.gmail.com> | cohort: Quillcraft | ● | Frederick's mailbox | connecting (per-company evidence) |
| 244 | L470 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842262887629456494 | cohort: Quillcraft | ● | Frederick's mailbox | companion (counters / snippet) |
| 245 | L471 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CALcXsJB9Dsqckdbzui4zsoYGv8YD3gxSJbpOQzA@mail.gmail.com> | cohort: Quillcraft | ● | Frederick's mailbox | connecting (per-company evidence) |
| 246 | L473 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843708664217753499 | cohort: Tilecast | ● | Frederick's mailbox | connecting (per-company evidence) |
| 247 | L475 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdfSBCTPq8pDFK70IArhUSHj5PEV3Tnz19vDg7Y@mail.gmail.com> | cohort: Tilecast | ● | Frederick's mailbox | connecting (per-company evidence) |
| 248 | L477 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843984229991264696 | cohort: Benchmarkly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 249 | L479 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAHSfM6DagNeY2EUvRjCOyAb1FwmdFsO1FgnXFpY@mail.gmail.com> | cohort: Benchmarkly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 250 | L481 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843984229991264696 | cohort: Benchmarkly | ● | Frederick's mailbox | companion (counters / snippet) |
| 251 | L482 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAFrM1JgqylGFM5MjwuqQMZPLsTjafUxYfbcriCb@mail.gmail.com> | cohort: Benchmarkly | ● | Frederick's mailbox | connecting (per-company evidence) |
| 252 | L484 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842712097587609477 | cohort: Loopnote | ● | Frederick's mailbox | connecting (per-company evidence) |
| 253 | L486 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAXtogZgoD89z43tdTH1zDpTmUGOoXKTd_jeRYV5@mail.gmail.com> | cohort: Loopnote | ● | Frederick's mailbox | connecting (per-company evidence) |
| 254 | L488 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842712097587609477 | cohort: Loopnote | ● | Frederick's mailbox | companion (counters / snippet) |
| 255 | L489 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAff-LH5Vcdc03I5o2aYmpkuR0BE-z_AH8pa3w_W@mail.gmail.com> | cohort: Loopnote | ● | Frederick's mailbox | connecting (per-company evidence) |
| 256 | L491 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844165423924029064 | cohort: Driftwood Audio | ● | Frederick's mailbox | connecting (per-company evidence) |
| 257 | L493 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA6I5lYTxcuD1NKwoqPt6_lMK3iSCs805OP2H7LL@mail.gmail.com> | cohort: Driftwood Audio | ● | Frederick's mailbox | connecting (per-company evidence) |
| 258 | L495 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1844165423924029064 | cohort: Driftwood Audio | ● | Frederick's mailbox | companion (counters / snippet) |
| 259 | L496 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA-DqRg1TZ4TPniI7P8AW7DvtD6lNosGZdpC1x6_@mail.gmail.com> | cohort: Driftwood Audio | ● | Frederick's mailbox | connecting (per-company evidence) |
| 260 | L498 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843346276352084348 | cohort: Motive Forge | ● | Frederick's mailbox | connecting (per-company evidence) |
| 261 | L500 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAroxkgBywTvnZooHWA1QvDuZcDMuI8XdpMtLkts@mail.gmail.com> | cohort: Motive Forge | ● | Frederick's mailbox | connecting (per-company evidence) |
| 262 | L502 | gmail.gmail_threads | arthur.blake@harmonygames.co/1843346276352842555 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 263 | L504 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAroxkgBywTvnZooHWA1QvDuZcDMuI8XdpMtLkts@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 264 | L506 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1843346276352084348 | cohort: Motive Forge | ● | Frederick's mailbox | companion (counters / snippet) |
| 265 | L507 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CALRuD4F9RvCLHQDHmtUqgPhhu2lRtd9SiD5vfMt@mail.gmail.com> | cohort: Motive Forge | ● | Frederick's mailbox | connecting (per-company evidence) |
| 266 | L509 | gmail.gmail_threads (UPDATE) | arthur.blake@harmonygames.co/1843346276352842555 | companion | ● | other mailbox | companion (counters / snippet) |
| 267 | L510 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CALRuD4F9RvCLHQDHmtUqgPhhu2lRtd9SiD5vfMt@mail.gmail.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 268 | L512 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842712097588195482 | T19 / cohort: Spotlight Fest | ● | Frederick's mailbox | connecting (per-company evidence) |
| 269 | L514 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAjj6h7BzqoAZSS2-4M7N9e7ZLBDyeyZXl0BwgcI@mail.gmail.com> | T19 / cohort: Spotlight Fest | ● | Frederick's mailbox | connecting (per-company evidence) |
| 270 | L516 | gmail.gmail_threads | frederick.stone@harmonygames.co/1842255337882328812 | T16 / cohort: Nova Rewards | ● | Frederick's mailbox | connecting (per-company evidence) |
| 271 | L518 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAFbpDWclpri3pr8w9gLzu4buYYHdy_xmueMuggv@mail.gmail.com> | T16 / cohort: Nova Rewards | ● | Frederick's mailbox | connecting (per-company evidence) |
| 272 | L520 | gmail.gmail_threads (UPDATE) | frederick.stone@harmonygames.co/1842255337882328812 | T16 / cohort: Nova Rewards | ● | Frederick's mailbox | companion (counters / snippet) |
| 273 | L521 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA32kc92PkZh7ZypeSz7afbb9TxyW_GZmCBXxoch@mail.gmail.com> | T16 / cohort: Nova Rewards | ● | Frederick's mailbox | connecting (per-company evidence) |
| 274 | L523 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844622183629433486 | companion | ● | Frederick's mailbox | connecting |
| 275 | L525 | gmail.gmail_messages | frederick.stone@harmonygames.co/<calendar-7ab9aa8e-d441-a5e5-d4a5-953239767264@google.com> | companion | ● | Frederick's mailbox | companion (INT-11 invitation) |
| 276 | L527 | gmail.gmail_threads | robert@harmonygames.co/1844622183628992238 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 277 | L529 | gmail.gmail_messages | robert@harmonygames.co/<calendar-a902eeee-7fb9-b775-7653-360e98115ee6@google.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 278 | L531 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844622183629272206 | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 279 | L533 | gmail.gmail_messages | arthur.blake@harmonygames.co/<calendar-d127348e-9054-26a4-f7c1-21f3338d10c6@google.com> | companion | ● | other mailbox | companion copy (another attendee's mailbox or calendar) |
| 280 | L535 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843074485453681260 | companion | ● | Frederick's mailbox | connecting |
| 281 | L537 | gmail.gmail_messages | frederick.stone@harmonygames.co/<calendar-36ed726c-941d-8aa3-2a87-2dccaaba569c@google.com> | companion | ● | Frederick's mailbox | companion (INT-11 invitation) |
| 282 | L539 | gcal.gcal_events | evt_fd469c29811879519c2c96 | K7 / T8 | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | overturning |
| 283 | L542 | gcal.gcal_events | evt_2ad963d94b80e64c3a3c12 | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 284 | L544 | gcal.gcal_events | evt_c8f5a9295ed40f33d90fab | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 285 | L546 | gcal.gcal_events | evt_bde03e4af2d3b5039711c0 | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 286 | L548 | gcal.gcal_events | evt_0a5e42c3aac62434ba2cfc | T5 | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | connecting |
| 287 | L550 | gcal.gcal_events | evt_564a16d0f5f6598d0360d5 | companion | ● (summary, attendees, time; description ○) | Frederick's calendar (self) | connecting |
| 288 | L552 | gcal.gcal_events | evt_0c2bdb97953bcb213e1d36 | companion | ● (summary, attendees, time; description ○) | other calendar | companion copy (another attendee's mailbox or calendar) |
| 289 | L554 | linear.linear_issues | ZOM-567 | T1 | ● | unscoped service | connecting |
| 290 | L557 | linear.linear_comments | cmt_c9a6660d81e067ad1de7 | T1 | ● (§6b) | unscoped service | connecting |
| 291 | L559 | contacts.contacts | 9b0185e445572aeee9f27d35 | K11 | ● (email, job) | unscoped service | connecting |
| 292 | L562 | contacts.contacts | a6ebc7683d450b0017b8acf3 | companion | ● (email, job) | unscoped service | connecting |
| 293 | L564 | contacts.contacts | 35a52a2e3c634972639806b5 | companion | ● (email, job) | unscoped service | connecting |
| 294 | L566 | contacts.contacts | 8a7605bdc08105137d87f5a7 | companion | ● (email, job) | unscoped service | connecting |

## Findability and discovery-order proofs

- Hub (A1) frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com> in frederick.stone@harmonygames.co/1844732913254784171: Leonard → Frederick, Sep 30 23:20Z; the prompt names it ('Leonard's vendor and partner email'); a gmail search for 'vendor' or 'partner' returns it first (newest). First link.
- Guardrails doc H1 f_b98287f6f80fe431a71209: the hub names 'the runway guardrails doc'; a Drive/Docs search for 'runway guardrails' returns it; competing hit the UA buckets doc f_7bacf15c4e8eea1a52dcd4 (Frederick's own, Sep 16, about UA spend: decoy_scope team) and Frederick's Sep 15 framing C07C2866011/1757961037.465799.
- ESG note H2 frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> + Leonard's ack frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> (thread frederick.stone@harmonygames.co/1844177063117059830): the hub names 'ESG's note about signing'; a gmail search for 'ESG' or 'signing' returns the thread; the competing first hit is Leonard's July Slack note 0573efd133cabdb1acde61e68571aa82 (C07C2866011/1753207800.603298), which a Slack search for 'accept the terms' or 'sign' returns.
- Keep-running card H3 689b662c60cbe40b9f4a97ae (checklist 689b66a4b56c4354aa1efab8): the guardrails name 'Arthur's keep-running list on our board'; trello search 'keep-running' returns the card; the decoy is the base card 688c4fa78031638f0804a994 'cancel browsestack if not used'.
- T1 DONE: claim met first — the base portal mail frederick.stone@harmonygames.co/1842359398719557772 (Registration Completed, Sep 4) and Frederick's #executives post C07C2866011/1757011358.730529, returned by any 'Nintendo' search; overturned by Arthur's ZOM-567 comment cmt_c9a6660d81e067ad1de7 (Sep 25), reached by linear search 'Nintendo' (the issue description names the portal) and linear_list_comments; decisive because only the comment says the org account stays limited until an officer accepts the Global ToS and NDA (lapses Oct 15).
- T2 CORR: claim met first — the order form f_fba21c2d5d4bbb02983961 and quote thread frederick.stone@harmonygames.co/1843618067251203081 (Pro from Nov 1); overturned by Leonard's reply 9fb2d23420c7e01ca163571f4129c912 (Sep 26) under his Sep 21 PT Playtestcloud root C07C2866011/1758513190.847889; met first because the mail search hits the quote and channel history lists roots only; rev4: the reply names Maren (who signs the quote thread) and 'the Pro plan', not Framewell, so it is found by a Slack search for 'Maren' or 'Pro plan' or by opening the root's replies.
- T3 COMPL: claim met first — Wen's unanswered Sep 22 'Any news on the proposal?' in frederick.stone@harmonygames.co/1842800807116855774; overturned by Leonard's DM D05S58U4SAK/1759174260.052645 (Sep 29: called them back Saturday); found by a Slack search for 'Lanternfly' or by reading the DM.
- T4 EXC: the notice frederick.stone@harmonygames.co/1844157874176168845 says Team $29/month from Nov 1 (cash in window); the guardrails' Keep clause points at the card; the checklist item 689b66a450734c26dcdf6291 names the function ('the night pager for backend outages') and Pingwise's own paper f_6c212cbfb31c3ded44ef8a names 'on-call alerting ... phone and SMS paging' — the join is by function, not by name.
- T5 DATE: claim met first — the pilot agreement f_8d0e0e3ae076b2f745e7e2 and the July tracker f_9d6edd4922d8130ccd272e (free through Jan 15); overturned by the Paylane notice frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> (Sep 12; workspace HG-2291, pilot ends Oct 15, cancel in writing to billing@paylane.io); a 'Clipforge' search does not return it (no company name); joined through HG-2291 in the welcome mail frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com> and the Jul 14 kickoff evt_0a5e42c3aac62434ba2cfc.
- T6 FILT: Pixel Harbor's quote thread frederick.stone@harmonygames.co/1835288808653226583 is dated Jun 18 (outside a September search window); the hub's scope has no date limit; the paper f_614f88a28a2f0cf1b88408 still asks a $2,400 deposit by Oct 10; found by a 'quote' / 'booth' / 'deposit' search without a date filter or by the July tracker f_9d6edd4922d8130ccd272e.
- T7 SIGN: the July note 0573efd133cabdb1acde61e68571aa82 is met first by a Slack search; ESG's note and Leonard's Sep 25 ack ('This replaces what I said in July') overturn it; Markward's click-through f_71a95593c736b3baf45f91 therefore goes to an officer (card).
- T8 review date: the guardrails say 'the January commitments review I'll put on our calendars' (Sep 26); the date is the review event evt_fd469c29811879519c2c96 (Mon Jan 5, 2026 17:00Z, created Sep 29) with its invitation frederick.stone@harmonygames.co/1844622183629433486.
- T9 AMEND: the guardrails' travel clause (only when we book them ourselves) is met first; the hub's 'one change I posted in #executives on Monday' points at 7e88911312fa9a969f0659a105af59a3 (C07C2866011/1759166100.370044, Mon Sep 29); Wishwave's paper f_54c2b4e172bb73a4a19845 has partner-booked travel.
- Robert's cancel-all post 80ced6c98e9bd0aa1ccb462488f1746d (T10) is a non-authoritative instruction; Robert's Spotlight note fc2f69c06b333f6c54dfd63d455c3958 (C07C2866011/1758134460.899858; rev4: 'the call about the Dec 5 indie showcase … I let Rina know') is found by a Slack search for 'showcase' or 'Rina', or by reading #executives for Sep 17. Hootline (rev4, T20) is found by an undated mail search ('promo', 'scheduler', 'Hootline') or a mailbox listing from early August: thread frederick.stone@harmonygames.co/1839631800730308867 has messages on Aug 5 and Aug 12 only and no filed paper.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | check-sql PASS (1.E) | every deciding fact persona-readable: ZOM-567 comment cmt_c9a6660d81e067ad1de7, reply 9fb2d23420c7e01ca163571f4129c912, DM D05S58U4SAK/1759174260.052645, checklist item 689b66a450734c26dcdf6291, notice frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>, June quote frederick.stone@harmonygames.co/1835288808653226583 |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: the hub (Tue Sep 30) says 'the one change I posted in #executives on Monday' = 7e88911312fa9a969f0659a105af59a3 (Mon Sep 29); Leonard's DM (Mon Sep 29) says 'on Saturday' = Sep 27; the README (Sep 30 22:40Z) and template (22:45Z) predate the hub (23:20Z); the review event was created Sep 29 for Mon Jan 5, 2026 |
| Cross-service Referential | base_check Check A PASS | one name and amount per company across thread, paper and Slack (Framewell $149/month in f_fba21c2d5d4bbb02983961 and frederick.stone@harmonygames.co/<CAGJkuaxoKn_J2zxTzhLswrYwOGA_wA5IXe9v747@mail.gmail.com>; Pixel Harbor $2,400 by Oct 10 in f_614f88a28a2f0cf1b88408 and frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com>) |
| Quantitative | reply counters updated on the Playtestcloud root c41d37178fca394c135408d2b38e0879 (reply_count 1, latest_reply 1758920520.674991); Trello badges match the checklist (4 items, 0 checked) | no figure is quoted against a base row; no totals are seeded |
| State / Lifecycle | ZOM-567 Todo without stamps | the keep-running card 689b662c60cbe40b9f4a97ae sits in Doing (not Done, so L12 does not apply); Nova's offer is withdrawn in its own thread frederick.stone@harmonygames.co/1842255337882328812 |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); roster addresses in every seeded row (I03) |
| Semantic / Category | — | titles match content (f_b98287f6f80fe431a71209, f_846ddc38b2aab3d2ed3fcb, 689b662c60cbe40b9f4a97ae, evt_fd469c29811879519c2c96) |
| Other | — | voice per 1.C; no record states a decision, a total or the log |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails | seeded: the January review (Frederick frederick.stone@harmonygames.co/1844622183629433486, Robert, Arthur; Leonard organizes) and the Spotlight call (Frederick frederick.stone@harmonygames.co/1843074485453681260; Robert organizes); declared exception for the Jul 14 kickoff 24cbd5ab34e4c9c132384aae9cf0a03c@hg4 (integration_exceptions: no_notify — Frederick organizes, the only other attendee is external) |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / mail digest | none: ZOM-567 has no PR; Arthur creates, assigns and comments on his own issue (no notification to Frederick) |
| gdrive | INT-13 | Drive Slack app share DM | none: the shared docs (f_b98287f6f80fe431a71209, f_846ddc38b2aab3d2ed3fcb, f_3b06917a41dd59308d890b) follow the base pattern of Leonard's shares to Frederick, which carry no Drive-app DM (e.g. f_17e6175e84e745f92b3415) |
| slack | INT-22 | Slack e-mail notifications | none: Frederick's base mailbox holds 2 '[Slack] … sent you a message' threads in 4,656 (complete scan; frederick@harmonygames.co_1814459351624238255.json, frederick@harmonygames.co_1814909772684074125.json, both 2024) and none for D05S58U4SAK; the seeded posts carry no @mention |
| trello | INT-21 | no Trello→Slack integration | none (the keep-running card 689b662c60cbe40b9f4a97ae posts nowhere) |
| gmail, gdocs, gsheets, gslides, contacts | not integration sources | — | none |

## Touched-data census and coherence hazards

Touched data: the hub frederick.stone@harmonygames.co/1844732913254784171 and its copies; the guardrails doc f_b98287f6f80fe431a71209 and the UA decoy f_7bacf15c4e8eea1a52dcd4; ESG's thread frederick.stone@harmonygames.co/1844177063117059830, checklist f_3b06917a41dd59308d890b and intake contact 9b0185e445572aeee9f27d35; the Q4 folder d_80a8c04753ba82ba4ba6a5 with README f_846ddc38b2aab3d2ed3fcb and template f_05f0a451b29b19a1c0b90f; the July tracker f_9d6edd4922d8130ccd272e; the founders' board 640643a3fd8f3ca308d9318e (keep-running card 689b662c60cbe40b9f4a97ae, base card 688c4fa78031638f0804a994); #executives C07C2866011 (Jul 22, Sep 4, Sep 15–29: base C07C2866011/1757011358.730529, C07C2866011/1757961037.465799, root C07C2866011/1758513190.847889 whose counters the SQL updates, C07C2866011/1756832039.396149); the DM D05S58U4SAK (Sep, including the base root D05S58U4SAK/1758151772.570449 whose counters the SQL updates); ZOM-567; the Paylane notice frederick.stone@harmonygames.co/1843067564852153540; the three calendar events; every member thread and paper (Facts for the human); and the base threads a correct run opens: frederick.stone@harmonygames.co/1842358947604469113, frederick.stone@harmonygames.co/1842359398719557772, frederick.stone@harmonygames.co/1840501641217286806, frederick.stone@harmonygames.co/1842348778705877030, frederick.stone@harmonygames.co/1843000993076735547, frederick.stone@harmonygames.co/1842890197572292911, frederick.stone@harmonygames.co/1841620870486605150, frederick.stone@harmonygames.co/1817715521687421486, frederick.stone@harmonygames.co/1837914783244638008, frederick.stone@harmonygames.co/1842898562278009736, frederick.stone@harmonygames.co/1843473831194478743, frederick.stone@harmonygames.co/1841636073974841484.

Hazards from coherence_hazards.json:
- temporal: T02 — every seeded thread is in chronological order (base_check Check C; e.g. frederick.stone@harmonygames.co/1842800807116855774: Sep 9, Sep 10, Sep 22); T03 none in scope (every seeded date parses; RFC-2822 dates as in the base).
- semantic: S04 (Frederick's GitHub 'Ryan') avoided — no GitHub record touched; S01–S03 none in scope — no Linear key is cited outside Linear and no label is written; the seeded contacts are counterparties with the company as job (9b0185e445572aeee9f27d35, a6ebc7683d450b0017b8acf3).
- referential: R08 (invitation mails vs calendar) — every seeded meeting has its invitation copies (evt_fd469c29811879519c2c96, evt_564a16d0f5f6598d0360d5) except the declared no_notify kickoff 24cbd5ab34e4c9c132384aae9cf0a03c@hg4; R01 none in scope — ZOM-567 is cited only in Linear.
- quantitative: Q01/Q02/Q03 — the seeded reply under C07C2866011/1758513190.847889 updates the root's reply_count 1, reply_users_count 1 and latest_reply 1758920520.674991 (companion UPDATE; hazard_acknowledgements Q01 dated_claim, the reply is an attributed dated claim); rev4: the seeded DM reply under D05S58U4SAK/1758151772.570449 (base c148cae9de21cd26027d8bbc89bb127c) updates that root's reply_count 1, reply_users_count 1 and latest_reply 1759174260.052645 (second Q01 acknowledgement); Q04 none in scope — every seeded Slack row carries reply_count / reply_users_count fields like the base.
- state/lifecycle: L08 — ZOM-567 is assigned to Arthur (active at the clock per activity.json) and stays Todo because the officer step is pending (cmt_c9a6660d81e067ad1de7); L12 none in scope — the keep-running card is in Doing.
- identifier/format: I03 — seeded rows use the roster address frederick.stone@harmonygames.co (base thread files use the frederick@ alias); I16 — Trello ids encode their action time (689b662c60cbe40b9f4a97ae = 2025-08-12T16:05Z).

Known data issues (references/known_data_issues/synthcut.md, read for every touched record; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):
- SC-39 (Singular payment plan): Singular is off the log by the hub's exclusion; its renewal thread frederick.stone@harmonygames.co/1837914783244638008 is never read for a value.
- SC-49 (founder count, Frederick's role): no founder count or status is graded; the role review rests on activity (C07C2866011/1757011358.730529, frederick.stone@harmonygames.co/1840501641217286806).
- SC-7 (channel membership): membership is used only for reach (C07C2866011, D05S58U4SAK), never graded.
- SC-24 / SC-55 (Mattel contact, RFP deadline): Mattel is a boundary ('Leonard keeps it', C07C2866011/1756832039.396149); no Mattel person or date is graded.
- SC-54 (Frederick's pay): FINANCE tables untouched.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Nintendo 'Registration Completed' (frederick.stone@harmonygames.co/1842359398719557772, Sep 4) and Frederick's 'I registered an account' (C07C2866011/1757011358.730529) | Arthur's comment cmt_c9a6660d81e067ad1de7 on ZOM-567 (Sep 25): the org account stays limited until an officer accepts the Global ToS and NDA; lapses Oct 15 | portals finish sign-up before the legal step; the base Sep 4 mail frederick.stone@harmonygames.co/1842358947604469113 already asked for ToS & NDA acceptance | Sign, card, next date Oct 15 |
| Framewell order form, Pro billed from Nov 1 (f_fba21c2d5d4bbb02983961) | Leonard's reply 9fb2d23420c7e01ca163571f4129c912 (Sep 26): no charge until Feb 1 | vendors extend free periods by phone; founders mention it in passing | Park, revisit Jan 5 |
| Wen's unanswered 'Any news?' (Sep 22, frederick.stone@harmonygames.co/1842800807116855774) | Leonard's DM D05S58U4SAK/1759174260.052645 (Sep 29): he called them back on Saturday | a CEO answers a publisher by phone | Answered by Leonard, revisit Jan 5, no new reply |
| Pilot free through Jan 15 (agreement f_8d0e0e3ae076b2f745e7e2; July tracker f_9d6edd4922d8130ccd272e) | Paylane notice frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> (Sep 12): cap reached, pilot ends Oct 15, $1,800/month from Oct 16 | pilots end early on a usage cap; processors notify by workspace id | End, cancel in writing by Oct 15 |
| Leonard's July note: Frederick may accept small terms himself (0573efd133cabdb1acde61e68571aa82) | ESG's note frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> and Leonard's ack frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> ('This replaces what I said in July') | counsel tightens signing while raising | officer signs; card |
| Guardrails: travel and event costs count only when we book them (f_b98287f6f80fe431a71209, Sep 26) | Leonard's Sep 29 change 7e88911312fa9a969f0659a105af59a3: they count even when a partner books them | founders amend rules in Slack | Wishwave End |
| Robert: cancel every marketing tool (80ced6c98e9bd0aa1ccb462488f1746d, Sep 25) | the guardrails doc (Sep 26, Leonard) decides per company | a co-founder vents before the CEO writes the rule | the guardrails apply; Robert's post decides nothing |
| Frederick's July 31 tracker as the population (f_9d6edd4922d8130ccd272e) | the hub's scope over the mail since June (frederick.stone@harmonygames.co/1844732913254784171) | a stale personal tracker | the scope rule decides; the tracker is a lead |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's vendor and partner email; Leonard's email from yesterday | frederick.stone@harmonygames.co/1844732913254784171 |
| A2 | my Q4 commitments folder; the Q4 commitments folder | d_80a8c04753ba82ba4ba6a5 |

Never name in the prompt: the guardrails doc's rules or location, ESG's note or its intake address, the keep-running card or its items, ZOM-567 or any Linear comment, Leonard's DM, Leonard's reply under the Playtestcloud post, the Sep 29 change, the Paylane notice or HG-2291, the January review event, Robert's Spotlight note, the July tracker, any company name, decision, date, amount or count. Deadlines: Frederick's today is Wed Oct 1, 2025; Leonard asks for written answers 'this week'. Deliverable kinds: one log sheet in the Q4 commitments folder, written answers and cancellations by mail, revisit reminders on the calendar, founders' board cards for signatures, ESG intake emails, Contacts entries, one reply on the hub thread.

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| Nintendo officer step | Global ToS and NDA | status | cmt_c9a6660d81e067ad1de7 |
| ZOM-567 lapse date | Oct 15 | date | cmt_c9a6660d81e067ad1de7 |
| Framewell waiver | no charge until Feb 1 | status | 9fb2d23420c7e01ca163571f4129c912 |
| Lanternfly call-back | Southeast Asia has to wait until after the raise | status | 418a0a6d6c29b7b67ce0ffb270c78c1e |
| keep-running night pager | night pager for backend outages | status | 689b66a450734c26dcdf6291 |
| Clipforge workspace | HG-2291 | id | f_8d0e0e3ae076b2f745e7e2, frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>, frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com> |
| Paylane cancellation address | billing@paylane.io | id | frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> |
| Pixel Harbor deposit | $2,400 | amount | f_614f88a28a2f0cf1b88408, frederick.stone@harmonygames.co/<CAC1R0eFyTK7ezriX3kHgoWqGCC1DkbKElci5sJ8@mail.gmail.com> |
| partner-booked travel | even when a partner books them | status | 7e88911312fa9a969f0659a105af59a3 |
| July signing note superseded | This replaces what I said in July | status | frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, leonard.hayes@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, robert@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, arthur.blake@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> |
| ESG officer rule | Only an officer, you or Arthur, accepts terms | status | frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, leonard.hayes@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, robert@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com>, arthur.blake@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> |
| keep-running card | Keep-running list (don't cut) | status | 689b662c60cbe40b9f4a97ae |
| Spotlight answer | sitting this one out this year | status | fc2f69c06b333f6c54dfd63d455c3958 |
| Hootline ask | would you like to keep the scheduler after that | status | frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com> |
| log sheet name | Q4 commitments log | status | f_846ddc38b2aab3d2ed3fcb |

Clause facts use the `status` kind: the `name` kind's near-spelling scan flags the sub-windows of a correct multi-word mention (fact_check, verified on this SQL), so phrases are held to an exact match instead.

```
FACT CHECK: PASS — 198 text-bearing rows, 15 declared facts, 7 declared superseded records
Errors: none
Warnings (9):
  line 138: gdocs.docs_documents f_eb94c65ce9f273c6b5a579: [value_drift] 'credit' carries 2 different amounts across rows: '$25,000,' (line 128, row f_a227b14f03e12005fe8324); '$10,000' (line 138, row f_eb94c65ce9f273c6b5a579) — supersession (declare it in traps[].version_records / facts) or drift?
  line 112: gdocs.docs_documents f_5b961c9c6887d31dcd2ee2: [value_drift] 'deposit' carries 2 different amounts across rows: '$2,400' (line 104, row f_614f88a28a2f0cf1b88408); '$4,000' (line 112, row f_5b961c9c6887d31dcd2ee2) — supersession (declare it in traps[].version_records / facts) or drift?
  line 118: gdocs.docs_documents f_a9593b0bf23b760e2972c7: [value_drift] 'fee' carries 3 different amounts across rows: '$750' (line 158, row f_9d9cf4e53b1c8607f9c869, +1); '$3,500' (line 106, row f_9d4639f91c93478d888f4b); '$900' (line 118, row f_a9593b0bf23b760e2972c7) — supersession (declare it in traps[].version_records / facts) or drift?
  line 110: gdocs.docs_documents f_4bdfb8e0c47288087c7bba: [value_drift] 'growth' carries 2 different amounts across rows: '$99' (line 144, row f_be21bac5d50e291ebfbe2b, +1); '$79' (line 110, row f_4bdfb8e0c47288087c7bba) — supersession (declare it in traps[].version_records / facts) or drift?
  line 156: gdocs.docs_documents f_e81c6ef89513cac632700a: [value_drift] 'price' carries 10 different amounts across rows: '$1,200,' (line 116, row f_41a9ea5036a231989745b2, +1); '$149' (line 98, row f_fba21c2d5d4bbb02983961); '$29' (line 100, row f_6c212cbfb31c3ded44ef8a); '$4,800' (line 104, row f_614f88a28a2f0cf1b88408) — supersession (declare it in traps[].version_records / facts) or drift?
  line 407: gmail.gmail_messages frederick.stone@harmonygames.co/<CAO2B00xDzwszNF3Ilw5PbJg0oZh1fnZ-QLkS2Jt@mail.gmail.com>: [value_drift] 'close' carries 2 different dates across rows: 'Oct 31' (line 347, row frederick.stone@harmonygames.co/<CAKGQuOVQjttk8qpLC2bhGl1ZJ4oRI7nPbIzP6mR@mail.gmail.com>, +1); 'Nov 1' (line 407, row frederick.stone@harmonygames.co/<CAO2B00xDzwszNF3Ilw5PbJg0oZh1fnZ-QLkS2Jt@mail.gmail.com>) — supersession (declare it in traps[].version_records / facts) or drift?
  line 104: gdocs.docs_documents f_614f88a28a2f0cf1b88408: [value_drift] 'due' carries 2 different dates across rows: 'Oct 10, 2025' (line 104, row f_614f88a28a2f0cf1b88408, +1); 'Oct 20' (line 104, row f_614f88a28a2f0cf1b88408) — supersession (declare it in traps[].version_records / facts) or drift?
  line 435: gmail.gmail_messages frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com>: [value_drift] 'ends' carries 2 different dates across rows: 'Oct 31' (line 295, row frederick.stone@harmonygames.co/<CAZgisbRwHgHd3Hk_E9LYMNIOFiMZminBj4K2tWc@mail.gmail.com>, +1); 'Jan 31' (line 435, row frederick.stone@harmonygames.co/<CAhKYUa4HtPNJGhGU5qifbVfYwMCjxb0DSaMXtME@mail.gmail.com>) — supersession (declare it in traps[].version_records / facts) or drift?
  line 287: gmail.gmail_messages frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>: [value_drift] 'starts' carries 3 different dates across rows: 'Oct 15, 2025' (line 287, row frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>, +1); 'Nov 1, 2025' (line 98, row f_fba21c2d5d4bbb02983961); 'Oct 16' (line 287, row frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io>) — supersession (declare it in traps[].version_records / facts) or drift?
```

Solver totals (`solver/truth.json`, sha256 273cbd92ab32c38e): 46 companies looked at; 36 on the log (Answered 4, End 10, Keep 3, Sign 7, Park 12); written answers 31, January revisits 14, signature cards 7, ESG intake emails 3, new contacts 32; 10 off the log (boundary records).

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| frederick.stone@harmonygames.co/<CAlIXcq3nWlSRBAZONcbY9d2v0ggkPYER8WfaoZa@mail.gmail.com> | seeded | Leonard → Frederick, cc Robert, Arthur, 2025-09-30T23:20Z, subject 'Vendor and partner stuff while I'm in LA': scope rule, guardrails, the Monday change, ESG's note, answers this week, Contacts, log in the Q4 folder per the README, reply with what we keep and what waits on a signature (thread frederick.stone@harmonygames.co/1844732913254784171) | Frederick's INBOX | authority (hub, anchor A1) |
| f_b98287f6f80fe431a71209 | seeded | Leonard, Sep 26 16:00Z, 'Runway guardrails - Q4 commitments': already answered → cash test Oct 1–Dec 31 (trials that convert count; travel only when we book) → Keep (Arthur's keep-running list) → Sign (ESG's note) → Park (January review); portals and no-reply notices need no answer | shared with Frederick | authority H1 |
| f_7bacf15c4e8eea1a52dcd4 | seeded | Frederick, Sep 16, 'UA spend buckets (Q4)': UA ad spend only | Frederick owns | decoy (H1, team scope) |
| frederick.stone@harmonygames.co/<CAyKP29rjypyVF_dZsTX0hDpFvI5fgxGX5-KMwIz@mail.gmail.com> | seeded | ESG partner → Leonard, cc founders, 2025-09-24T20:05Z: only Leonard or Arthur accept terms; auto-renewal, exclusivity, IP licence or term > 12 months to ESG intake first, one email each; mutual NDAs on ESG's template need no review (thread frederick.stone@harmonygames.co/1844177063117059830) | Frederick's INBOX | authority H2 |
| frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> | seeded | Leonard, 2025-09-25T16:30Z: 'This replaces what I said in July'; cards on the founders' board To Do list with the company name; intake checklist shared | Frederick's INBOX | overturning (T7) |
| f_3b06917a41dd59308d890b | seeded | ESG Law intake checklist (company, term/renewal, exclusivity/IP, cost, date needed, signer) | shared with Frederick | authority (ESG email content) |
| 9b0185e445572aeee9f27d35 | seeded | Contacts: ESG Law intake, PERSON_2599_EMAIL | unscoped | write target address |
| f_846ddc38b2aab3d2ed3fcb | seeded | Leonard, Sep 30 22:40Z: one row per company, sheet 'Q4 commitments log', columns, Next date definitions, Contacts rule | shared with Frederick | authority (log format) |
| f_05f0a451b29b19a1c0b90f | seeded | header row Company · Contact · What's waiting · Decision · Answered by · What we told them · Next date | shared with Frederick | write target (copy) |
| d_80a8c04753ba82ba4ba6a5 | seeded | Frederick's 'Q4 commitments' folder (Sep 29) | Frederick owns | write target (anchor A2) |
| f_9d6edd4922d8130ccd272e | seeded | Frederick's Jul 31 'Vendor & partner tracker' (Clipforge free through Jan 15; Pixel Harbor deposit Oct 10) | Frederick owns | stale summary (T14) · claim met first (T5) |
| 689b662c60cbe40b9f4a97ae | seeded | Arthur, Aug 12, 'Keep-running list (don't cut)', Doing list, founders' board | unscoped | authority H3 |
| 689b66a450734c26dcdf6291 | seeded | check item 'the night pager for backend outages (whatever wakes me up at 3am)' | unscoped | overturning (T4) |
| 0573efd133cabdb1acde61e68571aa82 | seeded | Leonard, 2025-07-22T18:10Z (C07C2866011/1753207800.603298): Frederick may accept terms under $500/year himself | #executives member | claim met first (T7) |
| 80ced6c98e9bd0aa1ccb462488f1746d | seeded | Robert, 2025-09-25T17:04Z (C07C2866011/1758819840.884370): cancel every marketing tool | #executives member | distractor (T10) |
| fc2f69c06b333f6c54dfd63d455c3958 | seeded | Robert, 2025-09-17T18:41Z (C07C2866011/1758134460.899858): 'had the call about the Dec 5 indie showcase. we're sitting this one out this year, I let Rina know' (Rina Takeda invited us to the Spotlight Fest indie showcase on Dec 5) | #executives member | evidence (Spotlight Fest answered by Robert; T19) |
| 7e88911312fa9a969f0659a105af59a3 | seeded | Leonard, Mon 2025-09-29T17:15Z (C07C2866011/1759166100.370044): travel and event costs count as cash even when a partner books them | #executives member | overturning (T9) |
| C07C2866011/1758513190.847889 | base | Leonard, Sep 21 PT (Sep 22 03:53 UTC): Playtestcloud results (root; reply counters updated by the SQL) | #executives member | container of the T2 reply |
| 9fb2d23420c7e01ca163571f4129c912 | seeded | Leonard, 2025-09-26T21:02Z (C07C2866011/1758920520.674991), reply under the Playtestcloud root: 'Maren called me back about the Pro plan … no charge until Feb 1' (Maren Holt sends Framewell's Pro order form) | #executives member | overturning (T2) |
| 418a0a6d6c29b7b67ce0ffb270c78c1e | seeded | Leonard → Frederick, 2025-09-29T19:31Z (D05S58U4SAK/1759174260.052645), reply in the DM thread under his Sep 17 'we have no localization though': rang Wen back on Saturday about their Southeast Asia deal; Southeast Asia has to wait until after the raise; pick it up again in January | DM member | overturning (T3) |
| ZOM-567 | seeded | Arthur, Sep 23: 'Switch: order dev kits' (Frederick registered on the portal Sep 4) | unscoped | connecting (T1) |
| cmt_c9a6660d81e067ad1de7 | seeded | Arthur, 2025-09-25T18:20Z: org account limited until an officer accepts the Global ToS and NDA; lapses Oct 15 | unscoped | overturning (T1) |
| frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> | seeded | Paylane (SVC_9701_EMAIL) → Frederick, 2025-09-12T14:10Z: workspace HG-2291 (UGC Studio) pilot cap reached, pilot ends Oct 15, $1,800/month from Oct 16 unless cancelled in writing to billing@paylane.io by Oct 15 (thread frederick.stone@harmonygames.co/1843067564852153540) | Frederick's INBOX | overturning (T5) |
| evt_0a5e42c3aac62434ba2cfc | seeded | Jul 14 16:00Z 'UGC Studio kickoff (workspace HG-2291)', Frederick organizer, Priya Raman attendee | Frederick's calendar | connecting (T5 join) |
| evt_fd469c29811879519c2c96 | seeded | Mon 2026-01-05 17:00–17:45Z 'Q4 commitments review', Leonard organizer, founders invited (created Sep 29) | Frederick's calendar | authority (revisit date, T8) |
| frederick.stone@harmonygames.co/1844622183629433486 | seeded | INT-11 invitation for the January review | Frederick's INBOX | companion |
| evt_564a16d0f5f6598d0360d5 | seeded | Wed 2025-09-17 18:00–18:30Z 'Spotlight Fest showcase call', Robert organizer, Frederick attendee; description 'Showcase slot call with Rina.' (rev4: no answer in the description) | Frederick's calendar | evidence (the call happened; the answer is in Robert's note) |
| frederick.stone@harmonygames.co/1843074485453681260 | seeded | INT-11 invitation for the Spotlight call | Frederick's INBOX | companion |
| d_ffa3e6e473da7e6523614f | seeded | Frederick's 'Vendor & partner paperwork' folder: his filed copies of each counterparty's paper, each created 10–15 minutes after the mail that sent it | Frederick owns | container |
| frederick.stone@harmonygames.co/1842358947604469113 | base | Sep 4: Nintendo Developer Portal 'Global ToS & NDA Acceptance Required' | Frederick's INBOX | evidence (T1) |
| frederick.stone@harmonygames.co/1842359398719557772 | base | Sep 4: 'Registration Completed' | Frederick's INBOX | claim met first (T1) |
| C07C2866011/1757011358.730529 | base | Frederick, Sep 4: 'I registered an account for harmonygames.' | #executives member | claim met first (T1) |
| frederick.stone@harmonygames.co/1840501641217286806 | base | Leonard → Balancy (PERSON_0527), Sep 11: priorities shifted, we'll circle back | Frederick's mailbox | evidence (Balancy answered by Leonard, later) |
| frederick.stone@harmonygames.co/1842348778705877030 | base | Sep 4 forward: Frederick's 'reply' is addressed to Leonard (nothing reached Rayking) | Frederick's mailbox | boundary (T18) |
| frederick.stone@harmonygames.co/1843000993076735547 | base | cold pitch with an unanswered follow-up | Frederick's mailbox | boundary (T11) |
| frederick.stone@harmonygames.co/1817715521687421486 | base | Google partner check-in (ad network) | Frederick's mailbox | boundary (T12) |
| frederick.stone@harmonygames.co/1842898562278009736 | base | NCsoft meeting report (strategic talks) | Frederick's mailbox | boundary (T15) |
| frederick.stone@harmonygames.co/1842255337882328812 | seeded | Nova Rewards offer, withdrawn on Sep 23 | Frederick's INBOX | boundary (T16) |
| frederick.stone@harmonygames.co/1843618067251203081 | seeded | Framewell thread with Maren Holt (PERSON_9701_EMAIL): creative asset subscription; order form: Pro plan billed from Nov 1 at $149/month; Leonard's Sep 26 thread reply under the Playtestcloud post (rev4: names Maren and the Pro plan, not Framewell): no charge until Feb 1 -> nothing before January → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_fba21c2d5d4bbb02983961 | seeded | Framewell paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842800807116855774 | seeded | Lanternfly Publishing thread with Wen Halvorsen (PERSON_9702_EMAIL): Southeast Asia publishing proposal; Frederick replied Sep 10 ('thanks, we'll take a look'); Lanternfly's Sep 22 'any news?' sits unanswered in the thread; Leonard's Sep 29 reply in the DM thread under his Sep 17 'we have no localization though' (rev4: names Wen and the Southeast Asia deal, not Lanternfly): he rang Wen back on Saturday, Southeast Asia waits until after the raise, talk again in January → Answered, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_5dbbaf5b251d5261427eb1 | seeded | Lanternfly Publishing paper (gslides): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1844157874176168845 | seeded | Pingwise thread with Dana Whitfield (PERSON_9703_EMAIL): uptime monitoring and on-call paging; free tier ends Oct 31, Team $29/month from Nov 1 (cash in window); Arthur's keep-running list names 'the night pager for backend outages' -> Pingwise's on-call paging -> Keep → Keep, next date 2025-11-01 | Frederick's mailbox | evidence (cohort) |
| f_6c212cbfb31c3ded44ef8a | seeded | Pingwise paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1837102635418059486 | seeded | Clipforge thread with Priya Raman (PERSON_9704_EMAIL): UGC video ad pilot; pilot agreement (Jul 14): free through Jan 15, 2026; processor notice (Sep 12) for workspace HG-2291 'UGC Studio': pilot cap reached, pilot ends Oct 15, $1,800/month from Oct 16 unless cancelled in writing to the address in the notice -> End, cancel by Oct 15 → End, next date 2025-10-15 | Frederick's mailbox | evidence (cohort) |
| f_8d0e0e3ae076b2f745e7e2 | seeded | Clipforge paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1835288808653226583 | seeded | Pixel Harbor Events thread with Teodor Lind (PERSON_9705_EMAIL): booth at the Oct 24 indie showcase; June 18 quote (outside the September window): booth hold needs a $2,400 deposit by Oct 10 -> cash in window -> End → End, next date 2025-10-10 | Frederick's mailbox | evidence (cohort) |
| f_614f88a28a2f0cf1b88408 | seeded | Pixel Harbor Events paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1841809902797646290 | seeded | Brightlane Studio thread with Ines Varga (PERSON_9706_EMAIL): creative agency retainer; paper: $3,500/month from Oct 1 → End, next date 2025-10-01 | Frederick's mailbox | evidence (cohort) |
| f_9d4639f91c93478d888f4b | seeded | Brightlane Studio paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842719647334876669 | seeded | Soundvault thread with Rafael Moreno (PERSON_9707_EMAIL): music licence (annual); paper: $1,188 prepaid on signature; quote valid to Oct 15 → End, next date 2025-10-15 | Frederick's mailbox | evidence (cohort) |
| f_2686da1086bfcc2fba3f57 | seeded | Soundvault paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843712439092112354 | seeded | Reviewly thread with Hana Kobayashi (PERSON_9708_EMAIL): store-review management trial; paper: trial converts Oct 20 at $79/month → End, next date 2025-10-19 | Frederick's mailbox | evidence (cohort) |
| f_4bdfb8e0c47288087c7bba | seeded | Reviewly paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842998987980893279 | seeded | Streamcast Talent thread with Kofi Mensah (PERSON_9709_EMAIL): influencer campaign; paper: 50% deposit on booking for a November campaign → End, next date 2025-10-31 | Frederick's mailbox | evidence (cohort) |
| f_5b961c9c6887d31dcd2ee2 | seeded | Streamcast Talent paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842168515789422611 | seeded | Lingora thread with Elena Petrova (PERSON_9710_EMAIL): store-listing localization sprint; paper: $2,640 invoiced on delivery; quote valid until Oct 3 → End, next date 2025-10-03 | Frederick's mailbox | evidence (cohort) |
| f_34ba4ac9a0f0fa4fd34e9e | seeded | Lingora paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842353484595925809 | seeded | Panelpulse thread with Arjun Shah (PERSON_9711_EMAIL): player research panel; paper: $1,200 prepaid for an Oct 14 panel; confirm by Oct 6 → End, next date 2025-10-06 | Frederick's mailbox | evidence (cohort) |
| f_41a9ea5036a231989745b2 | seeded | Panelpulse paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1841081352192260725 | seeded | Ascendo thread with Lucia Ferrer (PERSON_9712_EMAIL): ASO agency retainer; paper: $900/month from Oct 1 → End, next date 2025-10-01 | Frederick's mailbox | evidence (cohort) |
| f_a9593b0bf23b760e2972c7 | seeded | Ascendo paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843538794906427760 | seeded | Wishwave thread with Sven Aalto (PERSON_9713_EMAIL): pre-registration push at a partner showcase; paper: partner-booked travel for two (counts under the Sep 29 amendment); confirm by Oct 17 → End, next date 2025-10-17 | Frederick's mailbox | evidence (cohort) |
| f_54c2b4e172bb73a4a19845 | seeded | Wishwave paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843980455117084538 | seeded | Vaultline thread with Mila Novak (PERSON_9714_EMAIL): nightly database backups; renews Oct 12 at $19/month; on Arthur's keep-running list by name → Keep, next date 2025-10-12 | Frederick's mailbox | evidence (cohort) |
| f_2715771ae5f0358ad39aa9 | seeded | Vaultline paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1844067277209770126 | seeded | Certwell thread with Jonas Weber (PERSON_9715_EMAIL): SSL certificate for the API domain; renews Oct 20 at $89/year; on Arthur's keep-running list by name → Keep, next date 2025-10-20 | Frederick's mailbox | evidence (cohort) |
| f_cfb172dea30b9f6ac8a340 | seeded | Certwell paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842895178957083445 | seeded | Kinetic Arcade thread with Noor Haddad (PERSON_9716_EMAIL): publishing LOI (12-month exclusivity); free in window; exclusivity -> ESG first; officer signs → Sign, next date 2025-10-20 | Frederick's mailbox | evidence (cohort) |
| f_6252955f500f81e3aacbef | seeded | Kinetic Arcade paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842991438234544282 | seeded | Lumencloud thread with Aiden Clarke (PERSON_9717_EMAIL): cloud credits programme (36-month term); free; 36-month term -> ESG first → Sign, next date 2025-10-31 | Frederick's mailbox | evidence (cohort) |
| f_a227b14f03e12005fe8324 | seeded | Lumencloud paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843442535629243130 | seeded | Bundlehouse thread with Freya Olsen (PERSON_9718_EMAIL): co-marketing bundle (licenses our game IP); free; licence of our IP -> ESG first → Sign, next date 2025-11-01 | Frederick's mailbox | evidence (cohort) |
| f_9d1e0270574584de0eb92c | seeded | Bundlehouse paper (gslides): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843708664218314020 | seeded | Orbit Store thread with Mateo Rossi (PERSON_9719_EMAIL): store featuring agreement; free; needs an officer's acceptance → Sign, next date 2025-10-24 | Frederick's mailbox | evidence (cohort) |
| f_2ae7e3ee3220b628391234 | seeded | Orbit Store paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842802694553769659 | seeded | Markward thread with Leah Brennan (PERSON_9720_EMAIL): brand-monitoring free tier (click-through terms); free; click-through terms = an officer accepts (ESG overrides Leonard's July note) → Sign, next date - | Frederick's mailbox | evidence (cohort) |
| f_71a95593c736b3baf45f91 | seeded | Markward paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1844256020889910750 | seeded | Playfuse thread with Iris Navarro (PERSON_9721_EMAIL): bundle partnership NDA (ESG mutual template); mutual NDA on ESG's template: an officer signs, no counsel review → Sign, next date 2025-10-08 | Frederick's mailbox | evidence (cohort) |
| f_9a7fc4a3e45e4394227fa5 | seeded | Playfuse paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1839631800730308867 | seeded | Hootline thread with Gemma Doyle (PERSON_9722_EMAIL): social scheduler; Frederick signed up Aug 5 (promo keeps the scheduler free until Jan 31, then $39/month); Gemma's Aug 12 question whether to keep it after Jan 31 is unanswered; no filed paper and nothing after Aug 12 -> in scope by the hub's undated rule, Park → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| frederick.stone@harmonygames.co/1843350051225919345 | seeded | Glyphworks thread with Tomas Novotny (PERSON_9723_EMAIL): font licence quote; paper: quote valid to Jan 31, nothing owed until ordered → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_f6701704e5659b05d9530f | seeded | Glyphworks paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843078260327282996 | seeded | Cloudlark thread with Yara Nasser (PERSON_9724_EMAIL): startup credits offer; paper: credits, no term, start any time → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_eb94c65ce9f273c6b5a579 | seeded | Cloudlark paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1841538111898044975 | seeded | Echohall thread with Bruno Costa (PERSON_9725_EMAIL): community platform upgrade proposal; paper: free plan continues → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_68e288146ba0eee9fc17fa | seeded | Echohall paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842983888486665921 | seeded | Pressbeam thread with Ava Lindqvist (PERSON_9726_EMAIL): PR distribution package for 2026; paper: booked later; no travel → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_a9bb79c86b8b7b92083785 | seeded | Pressbeam paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843346276352069546 | seeded | Retainly thread with Omar Farouk (PERSON_9727_EMAIL): analytics trial; paper: trial converts Jan 12, 2026 (outside the window) → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_be21bac5d50e291ebfbe2b | seeded | Retainly paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842262887629456494 | seeded | Quillcraft thread with Nadia Petrov (PERSON_9728_EMAIL): AI copywriting tool beta; paper: free beta through January → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_af809bf6325b452edc8476 | seeded | Quillcraft paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843708664217753499 | seeded | Tilecast thread with Kenji Mori (PERSON_9729_EMAIL): website playable-preview widget; paper: free pilot slot in February → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_6d13a63be892a29f796b78 | seeded | Tilecast paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843984229991264696 | seeded | Benchmarkly thread with Clara Weiss (PERSON_9730_EMAIL): benchmark report subscription; paper: free sample now, paid from February → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_e916ab7563891481ab3b16 | seeded | Benchmarkly paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842712097587609477 | seeded | Loopnote thread with Pavel Sokol (PERSON_9731_EMAIL): meeting-notes tool trial; paper: trial free until Feb 1 → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_6963d4d30aceef4f88966a | seeded | Loopnote paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1844165423924029064 | seeded | Driftwood Audio thread with Sofia Marin (PERSON_9732_EMAIL): voice-over studio quote; paper: quote valid until Feb 28 → Park, next date 2026-01-05 | Frederick's mailbox | evidence (cohort) |
| f_17878d7b82fafcee79bfe7 | seeded | Driftwood Audio paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1843346276352084348 | seeded | Motive Forge thread with Hugo Lambert (PERSON_9733_EMAIL): outsourced art quote; Arthur declined in-thread on Sep 19 (cc Frederick) → Answered, next date - | Frederick's mailbox | evidence (cohort) |
| f_e81c6ef89513cac632700a | seeded | Motive Forge paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |
| frederick.stone@harmonygames.co/1842712097588195482 | seeded | Spotlight Fest thread with Rina Takeda (PERSON_9734_EMAIL): showcase slot invitation; Robert's Sep 17 #executives note (rev4: names the Dec 5 indie showcase and Rina, not Spotlight Fest; the call's calendar description no longer carries the answer): sitting this one out, he let Rina know → Answered, next date - | Frederick's mailbox | evidence (cohort) |
| f_9d9cf4e53b1c8607f9c869 | seeded | Spotlight Fest paper (gdocs): Frederick's filed copy of the paper the counterparty sent | Frederick owns | evidence (cohort paper) |

## Platform /injection review of rev1 and the rev2 changes

Attempt 6ae9909f707bc2aa0a7ed6e9 (`injection-static-v2`, stored in `run_forensics/rev1/platform_injection_review.md`) reviewed rev1 (sha256 9066997d79a3): FINAL VERDICT: PASS — Checks A, B and C PASS, lint 0 FAIL / 0 CHECK / 0 INFO, no demonstrated defects. Advisories and their disposition:
- B-adv (gslides.slides_pages.notes, slides_page_elements.table_json and ordinal, linear.linear_comments.sequence not in the unverified snapshot): kept — the same four columns loaded in two submitted tasks whose baselines scored on seeded data (support/completed_tasks/frederick_card_spend_q3_6ad83eebbd6456fd065bbd20, julia_zm_difficulty_baseline_2026-11-01); every other column matches the snapshot.
- C-adv 1 (the guardrails doc f_b98287f6f80fe431a71209, Sep 26, cited the January review 'on our calendars' while evt_fd469c29811879519c2c96 was created Sep 29): FIXED in rev2 — the doc now says the review 'comes back at the January commitments review I'll put on our calendars', so it announces the review Leonard schedules three days later; K7's delegation quote follows (design_delta).
- C-adv 2 (ZOM-567 created Sep 23 numbers after base issues created Sep 24–30; card idShort 456 created Aug 12 before base 452–455): kept — the issue must predate Arthur's Sep 25 comment, the base itself holds 6 ZOM inversions and neither field has an id contract; no record states an order.
- C-adv 3 (vendor mails say 'attached' with empty attachments_meta_json): kept — the base does the same (ESG's engagement thread frederick.stone@harmonygames.co/1841636073974841484: 'I've attached the complete set' with no attachment on any of its 3 messages); attachment bytes never reach the agent in HarmonyGames runs (Ask_Carriers §2.2), the Gmail attachment encoding is unverified (Ask_Carriers §7), and each paper is Frederick's filed copy in d_ffa3e6e473da7e6523614f, created 10–15 minutes after its mail. Rewording to 'shared' was rejected: the vendors cannot share files Frederick owns.
- C-adv 4 (Markward f_71a95593c736b3baf45f91 and Playfuse f_9a7fc4a3e45e4394227fa5 TITLE style runs shorter than the first line): FIXED in rev2 — every doc's TITLE run now covers its whole first line.
Rev2 changes exactly three rows (the guardrails doc and the two papers); no trap, fact, answer or truth value changes (truth.json identical; `oracle_kit` regression against rev1 PASS).

### Platform /injection review of rev2

Attempt 6ae9909f707bc2aa0a7ed6e9, rev 4 on the platform (sha256 795bd191872d…b4713f, stored in `run_forensics/rev2/platform_injection_review.md`): FINAL VERDICT: PASS — the 3 changed rows checked fresh, Drive and Docs collisions re-run, the other 292 rows reused from the rev1 review under stage-evidence-v1; C-adv 1 and C-adv 4 confirmed resolved ('I'll put on our calendars' in f_b98287f6f80fe431a71209; TITLE runs 0–43 and 0–56); B-adv, C-adv 2 and C-adv 3 remain advisories with the dispositions above. Next: /prompt, then /hardness, /oe and /rubric on this exact SQL.

Platform load (changelog `public._changelog`, stored in `run_forensics/rev2/platform_changelog.json`): 295 operations in one transaction at 2026-11-03T19:55:26Z, per-table INSERT/UPDATE counts equal to the SQL (260 + 35) and every statement matched to its entry; the guardrails doc f_b98287f6f80fe431a71209 loaded with the rev2 wording; the four B-adv columns are present in the loaded rows (slides_pages.notes 7 rows, slides_page_elements.table_json and ordinal 14 rows, linear_comments.sequence on cmt_c9a6660d81e067ad1de7), so the snapshot advisory is settled by the live load.

### Rev3: fork sweep at the prompt-brief stage

Before the prompt brief, an independent agent read only Frederick-visible records (no solver, manifest or surface) and listed every value two careful readers could set differently (`Working_Files/plan/blind_fork_sweep.md`). Each unsettled fork was settled in a record, keeping the solver's truth (the Lanternfly told text is read from the DM, so `oracle_kit` regression against rev2 holds):
- Scope: the hub now names PlayableX and Craftsman+ (UA-side vendors Frederick can see: base Slack C08H78VJG80, thread frederick.stone@harmonygames.co/1823332883409810377) with the ad networks and Singular on the UA budget call.
- Cash test vs Park for pay-when-you-order offers: the guardrails f_b98287f6f80fe431a71209 now say an offer we would have to take up and pay for before January counts as cash, and Park covers offers we could still take up after that.
- Framewell (CORR): Leonard's reply 9fb2d23420c7e01ca163571f4129c912 adds 'with nothing to sign before then' (no Sign reading).
- Nintendo (DONE): Arthur's comment cmt_c9a6660d81e067ad1de7 reconciles the base 'NDA Effective: 09/04/2025' (frederick.stone@harmonygames.co/1842359398719557772: Frederick is only the administrator; the agreement approver must be an officer), says the click-through has no fee, exclusivity or IP licence and can be ended by either side (no ESG trigger), gives 'accepted by Oct 15', and defers the kits until after the raise (no cash reading).
- Lanternfly (COMPL): Leonard's DM D05S58U4SAK/1759174260.052645 now says Southeast Asia has to wait until after the raise (the base shows other publishing outreach and Kinetic Arcade's LOI stays a Sign row).
- Plain noes, no 'later' reading: Robert's note fc2f69c06b333f6c54dfd63d455c3958 drops 'maybe next year'; Arthur's Motive Forge reply in frederick.stone@harmonygames.co/1843346276352084348 drops 'this quarter … for now'.
- Dates: Brightlane and Ascendo follow-ups ask to confirm by Oct 1; Reviewly's terms f_4bdfb8e0c47288087c7bba say 'cancelled by Oct 19'; Playfuse's NDA f_9a7fc4a3e45e4394227fa5 says 'by Oct 8, 2025 (before our call that day)'.
- ESG and signing: Markward's terms f_71a95593c736b3baf45f91 have no rolling term; Bundlehouse's deck f_9d1e0270574584de0eb92c and follow-up make joining a signed participation agreement; Playfuse's NDA is on ESG Law's mutual NDA template (the base 2023 HG template predates ESG).
- Waiting to hear from us: Retainly, Benchmarkly and Driftwood Audio now ask a question; Markward's Leah asks whether to hold the setup.
- Coherence: the UA buckets doc f_7bacf15c4e8eea1a52dcd4 no longer says the real UA bucket is paused (base Unity bids moved on Sep 29–30); Brightlane's retainer no longer includes playable work; Nova's withdrawal drops 'back and forth'.
- Second sweep on the first rev3 build (`plan/blind_fork_sweep_rev3.md`: its independent log matched the solver row for row, 36 rows): the guardrails' Sign step now says what to tell them ('with Leonard or Arthur to sign, and with our lawyers first when ESG has to see it'); Lumencloud's and Orbit Store's mails state the application and the call; Hootline's follow-up drops the annual-plan upsell; Certwell's notice says nothing new to sign; the Paylane notice says replies to the email aren't monitored (the billing address is); Priya's Sep 22 mail no longer reports videos after the cap; Tilecast's widget is an interactive demo widget (no 'playable' wording beside the UA doc).

### Platform reviews of rev3 and the rev3 Opus pre-check

- /injection on rev3 (platform rev 5, sha256 2176eb708f74, `run_forensics/rev3/platform_injection_review.md`): FINAL VERDICT: PASS; new minor advisory C-adv 3 (Lumencloud 'Thanks for applying' vs 'Apply by Oct 31') dispositioned as outcome-invariant (`run_forensics/rev3/platform_injection_dispositions.md`).
- /prompt on rev3 (`run_forensics/rev3/platform_prompt_review.md`): PASS, Score 5 on every dimension; STEP 0.6 nearest neighbour 0.658 (distinct).
- Opus 5.5 pre-check on rev3 (265 calls, `run_forensics/rev3/precheck/`) and /hardness (`run_forensics/rev3/platform_hardness_review.md`): FAIL, Score 2, HOLD (narrow miss: only Nintendo missed). The run searched Slack for every company name and for 'told'/'vendor', read the Leonard DM's newest roots and built its cohort from the Aug 15+ inbox, the paperwork folder and the July tracker (`01a_Hardening_Report.md` §5).

### Rev4: after the rev3 Opus pre-check (design-2)

Each change moves where an existing record sits or how it is worded; no record is added for volume, no truth value changes (truth.json identical in every field to rev3; `oracle_kit` regression against rev3 PASS):
- CORR (T2): Leonard's reply 9fb2d23420c7e01ca163571f4129c912 names Maren and the Pro plan instead of Framewell and drops 'while we're on vendors' (the pre-check found it by 'Framewell' and 'vendor after:').
- COMPL (T3): Leonard's Lanternfly answer 418a0a6d6c29b7b67ce0ffb270c78c1e is now a reply in the DM thread under his Sep 17 root 'we have no localization though' (D05S58U4SAK/1758151772.570449, counters updated), names Wen and 'their Southeast Asia deal' and says he let them know Southeast Asia has to wait until after the raise, and drops 'Lanternfly' and 'told' (it was the DM's newest root, found three ways).
- NOTE (T19, new rule): Robert's note fc2f69c06b333f6c54dfd63d455c3958 names the Dec 5 indie showcase and Rina instead of 'spotlight fest' and drops 'told'; the call's description (evt_564a16d0f5f6598d0360d5) is now 'Showcase slot call with Rina.', so the note is the only carrier of the answer.
- WIN (T20, new rule): Hootline's ask moves from Sep 24 to Aug 12 and its filed paper (f_f7902fdbb11a8bbd623959) is dropped; the terms ($39/month after Jan 31 unless cancelled) move into the Aug 5 mail (frederick.stone@harmonygames.co/1839631800730308867).
- Solver: rules NOTE and WIN with their controls (Motive Forge, Wishwave; Quillcraft, Gamesforum SF) and over-application operators; SIGN's control moves from Hootline to Echohall. Gradable surface design-2 (scenario-owned): X20 replaces X7 in the decision group, X18/X19/X21 added, Answered by and Next date compare by word (issue_key), told patterns accept 'no', 'won't', 'said no', 'passed on'.
- Blind fork sweep on the first rev4 build (`plan/blind_fork_sweep_rev4.md`, a fresh agent reading only Frederick-visible records): its independent log matched the solver row for row (36 rows; Answered 4, End 10, Keep 3, Sign 7, Park 12) and tied every alias to one company (Maren → Framewell, Wen → Lanternfly, the Dec 5 indie showcase and Rina → Spotlight Fest; Hootline in scope). Its three material open forks were settled in records, keeping the truth: the Lanternfly reply now says Leonard let them know (Answered, no Park email); Priya's Sep 22 mail asks to be told too if we are not carrying on (a written answer to Priya beside the Paylane cancellation); the README's Contacts line excludes portals and no-reply senders (no Nintendo contact). Two tightenings ride along: Arthur's ZOM-567 comment adds 'no fixed term' (no ESG trigger for Nintendo), and Lumencloud's agreement says 'Sign by Oct 31, 2025 (cohort closes)' (the rev3 platform C-adv 3). Its two cosmetic forks (timed vs all-day reminders; signer 'Leonard or Arthur') are accepted both ways in the brief.
Rev4 needs the platform /injection review, then /prompt with the same prompt, before the next pre-check.

## Platform follow-ups

- ○ carrier: none load-bearing — rev4 removed the answer from the Spotlight call's description (evt_564a16d0f5f6598d0360d5); Robert's #executives note C07C2866011/1758134460.899858 is the ● carrier.
- Linear comment cmt_c9a6660d81e067ad1de7 is ● (Ask_Carriers §6b, linear_list_comments); confirm it renders in the pre-check like any comment.
- Forecast blind spot: in exact mode the forecast never fails write-content slots (cards, sends, events, replies, the told column, the report lists), so its E[avg] 0.738 is optimistic; the design-mode view (declared mechanisms) gives 0.655. The rev3 pre-check scored about 95 %, far above both rev3 forecasts; rev4's rates are re-estimated from that run (UNCALIBRATED).
- No independent red team ran (REDTEAM_* unset; fallback recorded in the scenario design §13).

## Self-review

### Tool outputs (final SQL, verbatim)

`tools/sql_lint.py`:
```
schemas touched (10): contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 41, 'gdocs': 35, 'gsheets': 4, 'gslides': 23, 'slack': 8, 'trello': 8, 'gmail': 162, 'gcal': 7, 'linear': 2, 'contacts': 4}  total rows: 294  ops: {'insert': 258, 'update': 36}
errors: 0  warnings: 8
  warn  line 539: gcal.gcal_events.start_ts = 2026-01-05T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 539: gcal.gcal_events.end_ts = 2026-01-05T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 542: gcal.gcal_events.start_ts = 2026-01-05T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 542: gcal.gcal_events.end_ts = 2026-01-05T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 544: gcal.gcal_events.start_ts = 2026-01-05T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 544: gcal.gcal_events.end_ts = 2026-01-05T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 546: gcal.gcal_events.start_ts = 2026-01-05T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 546: gcal.gcal_events.end_ts = 2026-01-05T17:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```

sql_lint warning disposition (8 warnings, one class — on/after the clock): the four copies of the Jan 5, 2026 'Q4 commitments review' carry future start/end plan fields only; it is a not-yet-happened event created Sep 29 (before the seed bound), allowed as a deadline/plan field (Ask_Carriers clock rule); no event is treated as completed.

`tools/base_check.py`:
```
BASE CHECK (/injection A + C, static): PASS  — 258 inserts, 36 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
  note: integration exception declared for 24cbd5ab34e4c9c132384aae9cf0a03c@hg4: no_notify: Frederick organized the Jul 14 UGC Studio kickoff himself; the only other attendee is Cli
  note: trello.trello_check_items: no base-reference rules (checked by sql_lint only)
  note: trello.trello_checklists: no base-reference rules (checked by sql_lint only)
```

base_check (run with the final manifest): 0 warnings; the INT-11 exception for the Jul 14 kickoff 24cbd5ab34e4c9c132384aae9cf0a03c@hg4 is a declared note (no_notify: Frederick organizes; the only other attendee is external).

`tools/base_claims.py`:
```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```

`tools/hardness_gate.py` (final manifest + SQL):
```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 37 load-bearing seeded ids for frederick_stone (4 in unscoped services = visible, 33 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (15 declared facts), 9 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 258 INSERTed rows (UPDATE companions not counted; 294 rows in all); need ≥ 120
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 60 seeded ids cited; missing from SQL: none
  [ok] anchors: 2 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 14 fragments; need ≥ 12
  [ok] ask_fragment_services: 7 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 10 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 46; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 4 surfaces over 4 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 99; need ≥ 90
  [ok] call_budget: unconditional (verified) floor 236 of 236 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 200 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 37% (≤ 50%)
  [ok] traps: 20 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 5 supersessions (5 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 5 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 8 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 8 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 8 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 10 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 18 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 10 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 6 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 200 and per-record floor 90 replace 500 and 300; every other extreme target applies — reason: the cohort is 46 real companies (36 in scope); mail and calendar are bulk-readab; requester confirmation: task author in chat on 2026-11-03 set the horizon target at 'over 130 tool calls
```

`tools/hg.py lint` (the eval's hg_injection_lint, base data, sha256 69603ab4b6a4): counts {'FAIL': 0, 'CHECK': 0, 'INFO': 0, 'by_check': {}}. LINT: no CHECK flag to disposition; no INFO.

### Preflight (S4b–S5e)

```
SOLVER CONTRACT: PASS · solver.py sha 070ede94989a · sql 69603ab4b6a4 · 10 rules
  [PASS] contract.interface: 10 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (46 keys, sha ff17decb0624), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: previous truth truth.json: solver at revision ? reproduces it in fields and groups (evidence differs); current rules (None) on the previous SQL: 0 field difference(s)
  [PASS] contract.rules_nodes: 10 rules vs 10 portfolio entries: one-to-one
  [PASS] contract.slots: 14 direct/aggregate slots read a solver value; 20 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: DONE: 3 control(s); done_over moves ['Retainly']; CORR: 2 control(s); corr_over moves ['Brightlane Studio']; COMPL: 3 control(s); compl_over moves ['Glyphworks']; EXC: 3 control(s); exc_over moves ['Reviewly']; DATE: 2 control(s); date_over moves ['Retainly']; FILT: 3 control(s); filt_over moves ['Playable Factory']; SIGN: 2 control(s); sign_over moves ['Echohall']; AMEND: 1 control(s); amend_over moves ['Pressbeam']; NOTE: 2 control(s); note_over moves ['Wishwave']; WIN: 2 control(s); win_over moves ['Gamesforum SF']; channel CH-DONE (scale): ch_miss moves 1 of 1 member(s); channel CH-CORR (scale): ch_miss moves 1 of 1 member(s); channel CH-COMPL (scale): ch_miss moves 1 of 1 member(s); channel CH-EXC (scale): ch_miss moves 1 of 1 member(s); channel CH-DATE (scale): ch_miss moves 1 of 1 member(s); channel CH-FILT (scale): ch_miss moves 1 of 1 member(s); channel CH-NOTE (scale): ch_miss moves 1 of 1 member(s); channel CH-WIN (scale): ch_miss moves 1 of 1 member(s); channel CH-SLIP (scale): fails surface slots ['C1', 'C2', 'C5', 'C6', 'C7', 'C9']
  [PASS] contract.golden: 9 golden values checked against their deciding records (9 sampled keys x 6 fields): 9 identifier values found, 0 short tokens found, 0 presence-type (1 through tools/hg.py records); 45 unverified e.g. ['Nintendo/Contact: no evidence ids', "Nintendo/What's waiting: no evidence ids"]
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest 070ede94989a vs file 070ede94989a
```

```
MUTATION · rev4 · sql 69603ab4b6a4 · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 45 of 45 configurations checked
  rule:DONE                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X1', 'X17']
  rule:CORR                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X3', 'X14']
  rule:COMPL                         KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X5', 'X6']
  rule:EXC                           KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X16']
  rule:DATE                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X9', 'X10']
  rule:FILT                          KILLED     flipped   5 flips direct slot(s) of weight >= 3: ['X12']
  rule:SIGN                          SURVIVED   flipped   0 changes outputs that no slot reads
  rule:AMEND                         SURVIVED   flipped   0 changes outputs that no slot reads
  rule:NOTE                          KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X20', 'C3']
  rule:WIN                           SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:done_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:corr_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:compl_over                 SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:exc_over                   SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:date_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:filt_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:sign_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:note_over                  SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:win_over                   SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:amend_over                 SURVIVED   flipped   0 changes outputs that no slot reads
  degrade:ch_miss                    KILLED     flipped  60 flips direct slot(s) of weight >= 3: ['X1', 'X3', 'X5', 'X6', 'X20', '
  shards (consecutive slices of 14 records, 4 batches): 10 mutants {'KILLED': 7, 'SURVIVED': 3}
  intervention:rule:DONE             load-bearing    
  intervention:rule:CORR             load-bearing    
  intervention:rule:COMPL            load-bearing    
  intervention:rule:EXC              load-bearing    
  intervention:rule:DATE             load-bearing    
  intervention:rule:FILT             load-bearing    
  intervention:rule:SIGN             load-bearing    
  intervention:rule:AMEND            load-bearing    
  intervention:rule:NOTE             load-bearing    
  intervention:rule:WIN              load-bearing    
  intervention:degrade:done_over     no-injected-records
  intervention:degrade:corr_over     no-injected-records
  intervention:degrade:compl_over    no-injected-records
  intervention:degrade:exc_over      no-injected-records
  intervention:degrade:date_over     no-injected-records
  intervention:degrade:filt_over     no-injected-records
  intervention:degrade:sign_over     no-injected-records
  intervention:degrade:note_over     no-injected-records
  intervention:degrade:win_over      no-injected-records
  intervention:degrade:amend_over    no-injected-records
  intervention:degrade:ch_miss       no-injected-records
  geometry: U = 0.8116 (112/138) · L_max = UNSUPPORTED
    V3 cap 0.90: U PASS (needs > 0.10) · L_max UNSUPPORTED
  dispositions: 42/42 recorded; missing: none
```

Mutation dispositions (`01c_Dispositions.json`, 42 of 42): DONE, CORR, COMPL, EXC, DATE, FILT, NOTE and ch_miss are live (KILLED); SIGN, AMEND and WIN are live (they flip only write-content or delivery slots — C10, P2, C11; X18, X21, V1 — which the direct-slot diagnosis does not read and geometry counts); the ten over-application operators are weak-accepted (they move only unslotted control rows — control trials, never landings); the eleven degrade interventions are redundant (no deciding record of their own); the ten rule interventions are live (load-bearing, no escape).
Geometry: U = 0.812 (112/138) > 1 − 0.90 (Easy cap) — PASS; L_max UNSUPPORTED (ten rules exceed the exact-combination limit; advisory). Liveness: 23 flags (breadcrumb, order, one rule placement; T20 adds breadcrumb and order), each weak-accepted with its reason in `01c_Dispositions.json` (the hub's delegations are the fairness links; no flag names a deciding record).

`tools/preflight_report.py --forecast 01c_Forecast.json`: PREFLIGHT: PASS — blocking solver_contract, surface_validation, mutation_dispositions and geometry_upper_bound all True; advisory geometry margin OK (V3), geometry bound PASS (V3), liveness dispositions missing: none, forecast recorded; report and .md bound by sha256 to the SQL, solver, surface, manifest and dispositions.

Forecast (UNCALIBRATED, pre-registered `hev_4c1e7e8286625c7c`, exact solver outcomes, disclosed mechanism rates re-estimated from the rev3 pre-check and bridge analogs; SIGN and AMEND at 0.05 left out of the exact combinations): E[avg] 0.738 [0.692, 0.783]; P(all four V3 gates) 0.061–0.511 across dependence scenarios. Its exact mode never fails a write-content slot, so every landed mechanism loses only its direct slots there. The design-mode view (the scenario's pre-registered `hev_da8a164703569b79`) counts the declared write-content consequences: E[avg] 0.655 [0.591, 0.719], P(all) 0.28–0.56. Replaying the rev3 pre-check's own behaviour on the design-2 surface scores 48.6 % (`plan/policy_scores_output.txt`). Both are model outputs, not measurements; the requester's targets (> 130 calls per run, average < 80 %) are checked on the Opus pre-check (rev3: 265 calls).

### Changes made at this stage (and why)

- Gradable surface: the five 'What we told them' slots (X13, X15, C5, C6, C11) use `reason_matches`, which `oracle_kit.py` cannot read as a solver value; they were reclassed `write_content` (graded from the written log, unchanged weights/keys/mechanisms) and X15's pattern now keys on the DM-only words, in a scenario-stage amendment re-certified by `stage_gate.py scenario` (design bb54cb161530, surface 3f1a7f7485cc; 01_Scenario_Design.md §12).
- SQL: Lanternfly's signature and deck now carry 'Lanternfly Publishing' (the log key; no record named it in full); Robert's Sep 17 note fc2f69c06b333f6c54dfd63d455c3958 carries Spotlight's answer in a ● carrier (the calendar description is ○).
- Rev2 (after the platform /injection PASS on rev1): the guardrails doc announces the January review it cites (C-adv 1) and every doc's TITLE run covers its first line (C-adv 4); see 'Platform /injection review of rev1 and the rev2 changes'.
- Rev4 (after the rev3 Opus pre-check, `01a_Hardening_Report.md`): the Framewell, Lanternfly and Spotlight corrections are de-named and the Lanternfly answer moves into a DM thread; Hootline moves outside the inbox-window/folder/tracker filter; rules NOTE and WIN are added; see 'Rev4: after the rev3 Opus pre-check'.
- Manifest: design_delta lists the id normalisation (Slack 32-hex ids, Gmail message rows), the T5/T7/T17 placeholders, the anchor's message row and the four control members added for the over-application operators; no preflight {report, digest} is written into the manifest because `preflight_report.py` binds the manifest by sha256 (either direction makes one stale).

### /injection Checks A–C walk

- Inventory: 258 INSERT, 36 UPDATE, 0 DELETE, no upserts; tables {'contacts.contacts': 4, 'gcal.gcal_events': 7, 'gdocs.docs_documents': 35, 'gdrive.drive_files': 41, 'gmail.gmail_messages': 81, 'gmail.gmail_threads': 81, 'gsheets.sheets_sheets': 2, 'gsheets.sheets_spreadsheets': 2, 'gslides.slides_page_elements': 14, 'gslides.slides_pages': 7, 'gslides.slides_presentations': 2, 'linear.linear_comments': 1, 'linear.linear_issues': 1, 'slack.slack_messages': 8, 'trello.trello_actions': 2, 'trello.trello_cards': 1, 'trello.trello_check_items': 4, 'trello.trello_checklists': 1}. PASS.
- Check A (references and IDs): every channel, user, issue, thread, calendar, board, list and folder resolves (base_check Check A PASS); in_reply_to and references point at seeded messages; uniqueness scoped to the full collections (1.F, complete scans, 0 hits); ownership, membership and shares give Frederick reach (check-sql PASS, 1.E). PASS.
- Check B (structure): sql_lint 0 errors; every *_json column is literal JSON; NOT NULL columns supplied; generated *_fts columns never written; camelCase Trello columns quoted. PASS.
- Check C (dates, parents, statuses, counts): all seeded timestamps ≤ 2025-10-01T00:00Z except the Jan 5 review's plan fields; replies after their parents (the Framewell reply 4 days after its root; the Lanternfly DM reply 12 days after its Sep 17 root); both roots' counters updated; ZOM-567 Todo without stamps; Trello badges match 4 items / 0 checked; the Sep 29 change and the Sep 25 ack each postdate what they supersede. PASS.

### Touched-data census

See 'Touched-data census and coherence hazards' above: six hazard categories covered (T02, S04, R08, Q01–Q03, L08/L12, I03/I16) and SC-7, SC-24, SC-39, SC-49, SC-54, SC-55 dispositioned.

### Counter-readings

| Category | Counter-reading (strongest argument it FAILS) | Evidence that resolves it | Verdict |
|---|---|---|---|
| Temporal | the DM reply says 'on Saturday' but is dated Monday: the call date is ambiguous | D05S58U4SAK/1759174260.052645 is Mon Sep 29 19:31Z; Saturday = Sep 27, before it; the answer is dated by the reply, not graded by day | holds |
| Temporal | the guardrails doc (Sep 26) cites a January review that is only put on the calendars on Sep 29 (a record citing something created after it; platform C-adv 1) | rev2: f_b98287f6f80fe431a71209 now says 'the January commitments review I'll put on our calendars'; evt_fd469c29811879519c2c96 is created Sep 29 by Leonard, as announced | holds (fixed in rev2) |
| Temporal | the review event's start (Jan 5, 2026) is after the clock, so it 'already happened' in no record | evt_fd469c29811879519c2c96 is a plan field created Sep 29 (sql_lint clock warnings dispositioned); nothing claims it happened | holds |
| Temporal | the hub's 'the one change I posted in #executives on Monday' could mean a Sep 22 post | 7e88911312fa9a969f0659a105af59a3 is Mon Sep 29 17:15Z; the only Leonard post about the guardrails; the hub is Tue Sep 30 | holds |
| Semantic / Category | the keep-running card is in Doing, so it reads as a task in progress rather than a standing list | 689b662c60cbe40b9f4a97ae desc 'Stuff the live game needs to keep running. Ask me before cancelling any of it.'; the guardrails name it a list | holds |
| Semantic / Category | 'Lanternfly' and 'Lanternfly Publishing' could be two companies | one sender PERSON_9702_EMAIL signs 'Lanternfly Publishing' in frederick.stone@harmonygames.co/1842800807116855774; the deck f_5dbbaf5b251d5261427eb1 uses the full name | holds |
| Cross-service Referential | the Paylane notice never says Clipforge, so a reader may treat it as an unknown vendor | HG-2291 appears in the welcome mail frederick.stone@harmonygames.co/<CAyIhcf4XSg_rUt0eT-St8La39wsNDnRzBlIxJMi@mail.gmail.com>, the pilot paper f_8d0e0e3ae076b2f745e7e2 and the kickoff evt_0a5e42c3aac62434ba2cfc (fact 'Clipforge workspace', fact_check PASS) | holds (designed join, T5) |
| Cross-service Referential | Arthur's comment says 'the portal' without naming Nintendo | ZOM-567's description names the Nintendo developer portal and Frederick's Sep 4 registration (C07C2866011/1757011358.730529) | holds |
| Quantitative | Pixel Harbor's deposit ($2,400) and price ($4,800) could be read as two amounts for one thing | f_614f88a28a2f0cf1b88408: price $4,800, deposit $2,400 by Oct 10, balance by Oct 20 (fact 'Pixel Harbor deposit' home rows only) | holds |
| Quantitative | the Playtestcloud root's reply counters disagree with the export after the seeded reply (Q01) | c41d37178fca394c135408d2b38e0879 UPDATE: reply_count 1, reply_users_count 1, latest_reply 1758920520.674991 (hazard_acknowledgements Q01) | holds |
| State / Lifecycle | Nintendo's 'Registration Completed' and Arthur's 'limited account' contradict each other (two live statuses) | intended: the Sep 4 completion is of sign-up, the Sep 25 comment adds the pending officer step, and the base Sep 4 mail frederick.stone@harmonygames.co/1842358947604469113 already asked for ToS & NDA acceptance | holds (designed, T1) |
| State / Lifecycle | Framewell's order form (paid from Nov 1) and Leonard's waiver are two live answers | the waiver 9fb2d23420c7e01ca163571f4129c912 is a dated human claim (Sep 26) after the form (Sep 18); best unintended reading: a stale form nobody updated; resolved because Leonard reports the vendor's phone call and nothing later restores Nov 1 | holds (designed, T2) |
| State / Lifecycle | Lanternfly's open 'Any news?' contradicts 'already answered' | Leonard's DM D05S58U4SAK/1759174260.052645 (Sep 29) postdates the Sep 22 follow-up; the guardrails' first step says not to write again | holds (designed, T3) |
| State / Lifecycle | the pilot agreement (free to Jan 15) and the notice (ends Oct 15) are both current | the notice frederick.stone@harmonygames.co/<CAYV6MxN9j-x1B7nyXxQQO_hYhY5AoRuc5G7XzgR@paylane.io> (Sep 12) cites the agreement's usage cap; the July tracker f_9d6edd4922d8130ccd272e predates it; best unintended reading: a phishing-like notice — resolved by the HG-2291 workspace id and the processor named in the agreement | holds (designed, T5) |
| State / Lifecycle | the July Slack note and ESG's rule disagree on who may accept terms | Leonard's ack frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com> says 'This replaces what I said in July' (Sep 25) | holds (designed, T7) |
| State / Lifecycle | the guardrails' travel clause and the Sep 29 change are two live rules | 7e88911312fa9a969f0659a105af59a3 names 'one change to the runway guardrails doc'; the hub points at it | holds (designed, T9) |
| State / Lifecycle | Robert's 'cancel every marketing tool' could be read as a founder decision that overrides the doc | 80ced6c98e9bd0aa1ccb462488f1746d (Sep 25) precedes Leonard's doc (Sep 26) and the hub delegates to the doc, not to Robert | holds (designed, T10) |
| State / Lifecycle | the July tracker lists ended or stale entries as current | f_9d6edd4922d8130ccd272e is dated Jul 31 ('Status (Jul 31)'); the hub's scope over the mail decides | holds (designed, T14) |
| Identifier / Format | a seeded mail uses frederick.stone@ while base files use frederick@ (I03), so the mailbox may look split | all seeded rows use the roster address, the same user_email as the base messages (thread_id frederick.stone@harmonygames.co/1840501641217286806) | holds |
| Other | the designed disagreements read as silent system fields rather than dated human claims | each overturning record is an authored message with a date and a reason (cmt_c9a6660d81e067ad1de7, 9fb2d23420c7e01ca163571f4129c912, D05S58U4SAK/1759174260.052645, frederick.stone@harmonygames.co/<CAyZDYLgzExhQkAm-LGcRvcnmhRj4gYsOAVITlO5@mail.gmail.com>, 7e88911312fa9a969f0659a105af59a3) | holds |
| Other | Robert's Spotlight answer could be unreachable if the note's alias does not resolve | Robert's #executives note fc2f69c06b333f6c54dfd63d455c3958 names the Dec 5 indie showcase and Rina; Rina Takeda's invitation frederick.stone@harmonygames.co/1842712097588195482 is for the Spotlight Fest indie showcase on Dec 5 and the Sep 17 call (evt_564a16d0f5f6598d0360d5, Robert organizer) ties the date | holds |
| Semantic | the de-named Framewell reply ('Maren … the Pro plan') could be read as another vendor's plan | Maren Holt is the sender of Framewell's Pro order form (frederick.stone@harmonygames.co/1843618067251203081); no other seeded or base record names a Maren (hg.py search slack/gmail/contacts 'Maren': only 'gsmarena' substrings) | holds |
| Semantic | the Lanternfly DM reply ('Wen … their Southeast Asia deal') could be about another publisher | Wen Halvorsen signs Lanternfly Publishing's Southeast Asia proposal thread (frederick.stone@harmonygames.co/1842800807116855774); 'Halvorsen' and 'SEA deal' have no other hits; Kinetic Arcade's LOI is Japan/Korea | holds |
| State / Lifecycle | Hootline with nothing after Aug 12 and no paper could be read as a dead sign-up, not a waiting item | Gemma's Aug 12 question is unanswered and the promo ends Jan 31 (thread frederick.stone@harmonygames.co/1839631800730308867); the hub's scope has no date limit and counts a sign-up | holds (designed, T20) |

People status: everyone a rule depends on is active at the clock (Leonard, Robert, Arthur per activity.json; ESG Law is external); no Snowflake roster or Confluence headcount line is touched.

Unresolved: no independent red-team review (fallback recorded); the six channels' landing rates are analogs from the completed Frederick tasks (UNCALIBRATED); calendar-description rendering unverified (supporting only); the forecast's exact mode cannot see write-content consequences.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#69603ab4b6a4 · 01_Hardness_Manifest.json#08ebd53b714c · 01_Grounding_Dossier.md#3c7feab09262 · solver/solver.py#070ede94989a · 01c_Dispositions.json#7fb4ea56cf3c · 01c_Preflight_Report.json#f412d847464a · 00_Assigments.md#5418f950517f · 01_Scenario_Design.md#2c09f947100b · 01_Hardness_Manifest.draft.json#84fea705bc87 · 01_Gradable_Surface.json#abd340b2b96e · __context__#db8af19cc1c3 · __assignment__#b196657eace0 · __policy__#dc4ab5df3cdd · __gate_policy__#115714063000 · __review__#d1d08c1c8c7d · blocking 0 · warnings 1 · checks 40
[PASS] assignment.v3_context: Frederick Stone / Co-founder; easy cap <90%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#2c09f947100b, 01_Hardness_Manifest.draft.json#84fea705bc87, 01_Gradable_Surface.json#abd340b2b96e, 00_Assigments.md#5418f950517f, __context__#db8af19cc1c3, __assignment__#b196657eace0, __policy__#dc4ab5df3cdd, __gate_policy__#115714063000, __review__#f8ef1e723697)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 52/52 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 47/47 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 7/7 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 294/294 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 105/105 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 8, rows 294
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 69603ab4b6a4 matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×8)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 57 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 42 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.812 (112/138) vs 1 - cap 0.10 (V3 easy): PASS (bound PASS); re-run U 0.812 PASS (bound PASS)
[WARN] geometry.margin: L_max None vs (1 - cap) + 0.10: UNSUPPORTED (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (23 flag(s))
[PASS] forecast.preregistered: forecast hev_4c1e7e8286625c7c pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 106 scoped load-bearing ids YES for frederick_stone
[PASS] structure.facts_declared: manifest declares 15 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 15 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 4 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 4 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 25 evidenced counter-readings (of 25 found; need ≥ 15) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

