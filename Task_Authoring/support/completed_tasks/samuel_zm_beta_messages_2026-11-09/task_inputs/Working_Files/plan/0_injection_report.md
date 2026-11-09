# /injection report: task_inputsK, rev1

Review version: injection-static-v2. Reviewed 2026-11-04. Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut).
Input: 01_Universe_Inject.sql, sha256 0c1cf21627d5d9fb6303127c005cbaab216522c5ba1bf25a1e04573a44d24dad. Source: hg4-synth-sep30cut v16.
Not saved to the Evals store or Evals/task_inputs/reports/, per the standing instruction for this task. No SQL executed.

### FINAL VERDICT: FAIL

Execution status: COMPLETE

Evaluator model: Opus 5.5 (claude-opus-5-5), reasoning effort 100, with four independent reviewers

Next action: change one clause in SQL line 36, re-run the local checks, store rev2, then re-run /injection.

Evidence limits: repo blobs are not readable through hg.py, so 27 client-code claims are UNVERIFIABLE; no real Postgres parser was available; live deployment is out of scope.

| Check | Result | Evidence |
|---|---|---|
| A: records, references and IDs | PASS | inj_review_A.md: 147 statements, 0 defects, 0 PENDING |
| B: SQL structure and schema | PASS | inj_review_B.md: 1,978 assignments, 0 defects; 7 columns not in the unverified snapshot, advisory |
| C: dates, relationships and consistency | FAIL | inj_review_C1.md PASS on chronology; inj_review_C2.md 150 claims, 0 marked contradicted; lead overrides N1 |

## Failure
Rule: Check C, incompatible facts introduced by the SQL. Line 36, slack reply: "NotificationManager only schedules once our own ask has run, on both platforms". Base harmonygames-Games/match3d#263#rc_4 (NotificationToggleButton.cs): the toggle calls NotificationManager.Instance.EnableNotifications() when permission is already granted, with no ask. Injected line 180 (Vincent on DES-318): "arrives on both when notifications are switched on from settings", for a message that only fires below level 20, before the ask.
Fix: "...only schedules once our own ask has run or they switch it on from settings, on both platforms".

## Reviewer files
plan/inj_review_A.md, plan/inj_review_B.md, plan/inj_review_C1.md, plan/inj_review_C2.md

## Full operation ledger
| # | Line | Op | Table | Record or target |
|---|---|---|---|---|
| 1 | L6 | INSERT | gdrive.drive_files | f_dc45e0e5a8b8635c1b82b2 |
| 2 | L9 | INSERT | gdrive.drive_files | f_de7a1ae20201816a67750d |
| 3 | L11 | INSERT | gdrive.drive_files | f_8eb8c04713ff6a6ef4a265 |
| 4 | L13 | INSERT | gdocs.docs_documents | f_dc45e0e5a8b8635c1b82b2 |
| 5 | L16 | INSERT | gsheets.sheets_spreadsheets | f_8eb8c04713ff6a6ef4a265 |
| 6 | L19 | INSERT | gsheets.sheets_sheets | f_8eb8c04713ff6a6ef4a265#Beta |
| 7 | L21 | INSERT | gslides.slides_presentations | f_de7a1ae20201816a67750d |
| 8 | L24 | INSERT | gslides.slides_pages | f_de7a1ae20201816a67750d#slide_7cbfbffe1b54 |
| 9 | L26 | INSERT | gslides.slides_page_elements | f_de7a1ae20201816a67750d#el_b78f5cefad1f |
| 10 | L28 | INSERT | gslides.slides_page_elements | f_de7a1ae20201816a67750d#el_9ecdf1278098 |
| 11 | L30 | INSERT | slack.slack_messages | 394f73aa43aa303a755bc81b2cf43840 |
| 12 | L33 | INSERT | slack.slack_messages | 37c5701a1780374401d295e86884f276 |
| 13 | L35 | INSERT | slack.slack_messages | 09aae609aa744fb23288c7dcbac9926c |
| 14 | L37 | INSERT | slack.slack_messages | d2b16907dc8c10fe5052805751097b58 |
| 15 | L39 | UPDATE | slack.slack_messages | a3e78e820b9f880ef4e3d941562110df |
| 16 | L40 | INSERT | slack.slack_messages | 4a5ee02518ff2fbeacaef2fc6d5a9ef9 |
| 17 | L42 | UPDATE | slack.slack_messages | c42902df5f54c75c1a6e3529cd25121c |
| 18 | L43 | INSERT | slack.slack_messages | 6fd96f3c3977cee8345e685d31cbc177 |
| 19 | L45 | INSERT | trello.trello_actions | 68d41578905712b474fbc0ca |
| 20 | L48 | UPDATE | trello.trello_cards | 6851a769c65dc0017a227bb7 |
| 21 | L49 | INSERT | trello.trello_actions | 68d415a716abcb84070a8e2a |
| 22 | L51 | UPDATE | trello.trello_cards | 6851a769c65dc0017a227bb7 |
| 23 | L52 | INSERT | trello.trello_actions | 68dae8c7d95e24b55b69bf80 |
| 24 | L54 | UPDATE | trello.trello_cards | 68d1eb90bef538c7c5c5599d |
| 25 | L55 | INSERT | gmail.gmail_threads | samuel.turner@harmonygames.co/1843335316636662321 |
| 26 | L58 | INSERT | gmail.gmail_messages | samuel.turner@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> |
| 27 | L60 | INSERT | gmail.gmail_threads | vincent.parker@harmonygames.co/1843335316636098078 |
| 28 | L62 | INSERT | gmail.gmail_messages | vincent.parker@harmonygames.co/<CAYr96MXDLI990PHRTvHgBNzJ5rcdWTpWyXj8JCA@mail.gmail.com> |
| 29 | L64 | INSERT | gmail.gmail_messages | samuel.turner@harmonygames.co/<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com> |
| 30 | L66 | INSERT | gmail.gmail_threads | samuel.turner@harmonygames.co/1844079259288333361 |
| 31 | L68 | INSERT | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-811bec31-daa2-c3e0-fc2e-c5ac9baf27a2@google.com> |
| 32 | L70 | INSERT | gmail.gmail_threads | samuel.turner@harmonygames.co/1844248505745845006 |
| 33 | L72 | INSERT | gmail.gmail_messages | samuel.turner@harmonygames.co/<calendar-c3b6ab0e-584f-11f3-3a4e-21f2067d4780@google.com> |
| 34 | L74 | INSERT | gcal.gcal_events | evt_b56d5b19baa0a573da4553 |
| 35 | L77 | INSERT | gcal.gcal_events | evt_8cad40bb558f994b74576a |
| 36 | L79 | INSERT | github.github_review_comments | harmonygames-Games/match3d#248#rc_18 |
| 37 | L82 | INSERT | github.github_reviews | harmonygames-Games/match3d#248#rev_7 |
| 38 | L84 | INSERT | linear.linear_team_memberships | tmem_team_DES_usr_49b9dfa5208d400d |
| 39 | L87 | INSERT | linear.linear_team_memberships | tmem_team_DES_usr_caafeec2804b3a67 |
| 40 | L89 | INSERT | linear.linear_team_memberships | tmem_team_DES_usr_51f5f16d46e8cf55 |
| 41 | L91 | INSERT | linear.linear_team_memberships | tmem_team_DES_usr_bdf01b53c6a92c5e |
| 42 | L93 | INSERT | linear.linear_issues | DES-313 |
| 43 | L95 | INSERT | linear.linear_issues | DES-314 |
| 44 | L97 | INSERT | linear.linear_issues | DES-315 |
| 45 | L99 | INSERT | linear.linear_issues | DES-316 |
| 46 | L101 | INSERT | linear.linear_issues | DES-317 |
| 47 | L103 | INSERT | linear.linear_issues | DES-318 |
| 48 | L105 | INSERT | linear.linear_issues | DES-319 |
| 49 | L107 | INSERT | linear.linear_issues | DES-320 |
| 50 | L109 | INSERT | linear.linear_issues | DES-321 |
| 51 | L111 | INSERT | linear.linear_issues | DES-322 |
| 52 | L113 | INSERT | linear.linear_issues | DES-323 |
| 53 | L115 | INSERT | linear.linear_issues | DES-324 |
| 54 | L117 | INSERT | linear.linear_issues | DES-325 |
| 55 | L119 | INSERT | linear.linear_issues | DES-326 |
| 56 | L121 | INSERT | linear.linear_issues | DES-327 |
| 57 | L123 | INSERT | linear.linear_issues | DES-328 |
| 58 | L125 | INSERT | linear.linear_issues | DES-329 |
| 59 | L127 | INSERT | linear.linear_issues | DES-330 |
| 60 | L129 | INSERT | linear.linear_issues | DES-331 |
| 61 | L131 | INSERT | linear.linear_issues | DES-332 |
| 62 | L133 | INSERT | linear.linear_issues | DES-333 |
| 63 | L135 | INSERT | linear.linear_issues | DES-334 |
| 64 | L137 | INSERT | linear.linear_issues | DES-335 |
| 65 | L139 | INSERT | linear.linear_issues | DES-336 |
| 66 | L141 | INSERT | linear.linear_issues | DES-337 |
| 67 | L143 | INSERT | linear.linear_issues | DES-338 |
| 68 | L145 | INSERT | linear.linear_issues | DES-339 |
| 69 | L147 | INSERT | linear.linear_issues | DES-340 |
| 70 | L149 | INSERT | linear.linear_issues | DES-341 |
| 71 | L151 | INSERT | linear.linear_issues | DES-342 |
| 72 | L153 | INSERT | linear.linear_issues | DES-343 |
| 73 | L155 | INSERT | linear.linear_issues | DES-344 |
| 74 | L157 | INSERT | linear.linear_issues | DES-345 |
| 75 | L159 | INSERT | linear.linear_issues | DES-346 |
| 76 | L161 | INSERT | linear.linear_comments | cmt_7c6c022293a0505fbf85 |
| 77 | L163 | INSERT | linear.linear_comments | cmt_cb634ee40df2ae6c6022 |
| 78 | L165 | INSERT | linear.linear_comments | cmt_2395189dfd5e7d5c1e88 |
| 79 | L167 | INSERT | linear.linear_comments | cmt_51e018b23e18c2f680cd |
| 80 | L169 | INSERT | linear.linear_comments | cmt_d6bf99cc8b3e926c2569 |
| 81 | L171 | INSERT | linear.linear_comments | cmt_5ab75e0ee96e70745960 |
| 82 | L173 | INSERT | linear.linear_comments | cmt_f64ebdf08bef6b136513 |
| 83 | L175 | INSERT | linear.linear_comments | cmt_e4bb9fe925b86f52cf55 |
| 84 | L177 | INSERT | linear.linear_comments | cmt_886fb8b04e3b6ba66b57 |
| 85 | L179 | INSERT | linear.linear_comments | cmt_f4960d3c073493b6bfc6 |
| 86 | L181 | INSERT | linear.linear_comments | cmt_10ae5518084785a96cfc |
| 87 | L183 | INSERT | linear.linear_comments | cmt_fd950c410ed25c447c02 |
| 88 | L185 | INSERT | linear.linear_comments | cmt_9338bb2c286a6c207792 |
| 89 | L187 | INSERT | linear.linear_comments | cmt_f1b42e3a7c9cfa136439 |
| 90 | L189 | INSERT | linear.linear_comments | cmt_f76672cf21387ec1eeab |
| 91 | L191 | INSERT | linear.linear_comments | cmt_4aa525e0162ec9ef15f6 |
| 92 | L193 | INSERT | linear.linear_comments | cmt_7b184259cfbb33052325 |
| 93 | L195 | INSERT | linear.linear_comments | cmt_8531c2616065b39e5c26 |
| 94 | L197 | INSERT | linear.linear_comments | cmt_5acbc1a3f111af34e7ac |
| 95 | L199 | INSERT | linear.linear_comments | cmt_3dabe2da836af3cc9ba8 |
| 96 | L201 | INSERT | linear.linear_comments | cmt_181bcd11a979359893fb |
| 97 | L203 | INSERT | linear.linear_comments | cmt_144462e04c0e02c19d02 |
| 98 | L205 | INSERT | linear.linear_comments | cmt_8c9ab0f70f9ab1dc5d5f |
| 99 | L207 | INSERT | linear.linear_comments | cmt_4478b09dc764fe7e1cd1 |
| 100 | L209 | INSERT | linear.linear_comments | cmt_64fc795e9c80b7c68a7e |
| 101 | L211 | INSERT | linear.linear_comments | cmt_84609a55e9bb01533c18 |
| 102 | L213 | INSERT | linear.linear_comments | cmt_5d85e7a910a89f7e0eeb |
| 103 | L215 | INSERT | linear.linear_comments | cmt_5a45fa6ed829ce69c092 |
| 104 | L217 | INSERT | linear.linear_comments | cmt_842c9cb4757414e145d3 |
| 105 | L219 | INSERT | linear.linear_comments | cmt_55c7d795dc967c39c6a5 |
| 106 | L221 | INSERT | linear.linear_comments | cmt_c6f09d1660c6a174811f |
| 107 | L223 | INSERT | linear.linear_comments | cmt_6e27d2eb839bbc66a95a |
| 108 | L225 | INSERT | linear.linear_comments | cmt_9d5748e1540a9588ceb9 |
| 109 | L227 | INSERT | linear.linear_comments | cmt_c6a61568172ef0ebb990 |
| 110 | L229 | INSERT | linear.linear_comments | cmt_e4ac33987005778b372e |
| 111 | L231 | INSERT | linear.linear_comments | cmt_d9f2d461e083b4a65263 |
| 112 | L233 | INSERT | linear.linear_comments | cmt_e1c7ebcf5aa9ee4b4a8c |
| 113 | L235 | INSERT | linear.linear_comments | cmt_e911c52cf054cb3ed19b |
| 114 | L237 | INSERT | linear.linear_comments | cmt_44a1117f30fbb476c28c |
| 115 | L239 | INSERT | linear.linear_comments | cmt_2456f47526183e4e1161 |
| 116 | L241 | INSERT | linear.linear_comments | cmt_ff7c43f0633261872ec7 |
| 117 | L243 | INSERT | linear.linear_comments | cmt_abb99f26dc3013206909 |
| 118 | L245 | INSERT | linear.linear_comments | cmt_521d7e03d14d535f1d5b |
| 119 | L247 | INSERT | linear.linear_comments | cmt_83e42df52254cf27fe4d |
| 120 | L249 | INSERT | linear.linear_comments | cmt_fda157bae8336585356a |
| 121 | L251 | INSERT | linear.linear_comments | cmt_546a8f6d521e2d00dc28 |
| 122 | L253 | INSERT | linear.linear_comments | cmt_b55d6a0b35ae5242ffd4 |
| 123 | L255 | INSERT | linear.linear_comments | cmt_cd8081a714a205760ce7 |
| 124 | L257 | INSERT | linear.linear_comments | cmt_4feec391e19bb4a4a16a |
| 125 | L259 | INSERT | linear.linear_comments | cmt_b770ad38987fc947c65f |
| 126 | L261 | INSERT | linear.linear_comments | cmt_32da06fe646ada57c7fa |
| 127 | L263 | INSERT | linear.linear_comments | cmt_e0e37d68814e1eae6002 |
| 128 | L265 | INSERT | linear.linear_comments | cmt_aa68a0b0ee32e8e24c58 |
| 129 | L267 | INSERT | linear.linear_comments | cmt_a6c862db8697a973afc7 |
| 130 | L269 | INSERT | linear.linear_comments | cmt_31db977b4adf091259da |
| 131 | L271 | INSERT | linear.linear_comments | cmt_904474dee7687823b700 |
| 132 | L273 | INSERT | linear.linear_comments | cmt_96b8c0e10b3d2b20a982 |
| 133 | L275 | INSERT | linear.linear_comments | cmt_1443f47829522f8bb44e |
| 134 | L277 | INSERT | linear.linear_comments | cmt_af799d5941e425ad3e53 |
| 135 | L279 | INSERT | linear.linear_comments | cmt_fe5087128f529fdbb69f |
| 136 | L281 | INSERT | linear.linear_comments | cmt_58672546fb6435495753 |
| 137 | L283 | INSERT | linear.linear_comments | cmt_fd99936084694fa6d973 |
| 138 | L285 | INSERT | linear.linear_comments | cmt_8c95a627941e0b32e091 |
| 139 | L287 | INSERT | linear.linear_comments | cmt_13477aa8d1468ae11c9d |
| 140 | L289 | INSERT | linear.linear_comments | cmt_bd206b061637646ac5cb |
| 141 | L291 | INSERT | linear.linear_comments | cmt_f1b8a109dfa70cdc4565 |
| 142 | L293 | INSERT | linear.linear_comments | cmt_2b519285937e7fa79453 |
| 143 | L295 | UPDATE | linear.linear_issues | ZOM-542 |
| 144 | L296 | UPDATE | linear.linear_issues | ZOM-556 |
| 145 | L297 | UPDATE | linear.linear_teams | team_DES |
