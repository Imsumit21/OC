# Grounding Dossier — frederick_bridge_pipeline · injection rev3 · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev3/01_Universe_Inject.sql`; rev1 (sha256 0b6812c56fe6) and rev2 (sha256 b2bfda86002c) each passed the platform /injection review and are kept in `run_forensics/rev1/` and `run_forensics/rev2/` with their reports and design files),
built by `Working_Files/plan/build_sql.py`; final manifest by `plan/build_final_manifest.py`; solver
`Working_Files/solver/solver.py` (truth `solver/truth.json`). Universe synth-cut (hg4-synth-sep30cut v16), seed bound
2025-10-01T00:00:00Z, eval clock 2025-10-01T07:00:00Z. Every probability is UNCALIBRATED.

## 1.A Structural

| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |
|---|---|---|---|
| gmail.gmail_threads / gmail_messages | id, thread_id, user_email | gmail/threads/frederick@harmonygames.co_1843625920612854647.json (message id frederick.stone@harmonygames.co/<calendar-f18abc9b-afab-4f82-a3ad-8bc700a558b1@google.com>) | thread id = mailbox/(ms << 20 + k); message id = mailbox/RFC Message-ID; labels INBOX/SENT; history_id NULL (id_contracts gmail_history_id) |
| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack/messages/C096HFA5Z8W/2025-09.json (73c2247f4a31f32d10b3068ecd1d13ac) | id = sha256(channel|ts)[:32]; reply: thread_parent_id = parent id, thread_ts_legacy = parent ts (as the platform-passed Julia SQL) |
| gdrive.drive_files / gdocs.docs_documents / gsheets / gslides | id, name, mime_type; document_id, title; spreadsheet_id, title; presentation_id, object_id | gdrive/data.json d_175c0d7bc72ed244b944cb; gsheets/data.json f_48247af79428823c3cac92 | f_/d_ + 22 hex; identical sharing on the Drive and native rows; docs body_text non-empty |
| gcal.gcal_events | event_id, calendar_id | gcal/data.json evt_89381fe5a15b802c5652a9 | one row per attendee calendar, self:true on the owner's copy, ical_uid 32 hex @hg4 |
| linear.linear_issues / linear_comments | id, title, priority, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at; comment id, issue_id, author_id, body, is_edited | linear/data.json ZOM-566 (created 2025-09-30T16:26:02Z) | ZOM-567 next number; ISO-Z; state Todo, no lifecycle stamps; state_history_json an empty JSON list |
| trello.trello_actions / cards / checklists / check_items | id, type, date; id, name, idBoard, idList | trello/data.json 68c5a49e8491a9d7faf869d0 | ids: first 8 hex = Unix seconds of the action; commentCard data_json full base shape; badges_json full shape |
| contacts.contacts | contact_id, first_name, last_name | contacts/contacts.json db57e559500151d6b3991b62 | 24 hex ids; sparse like the base (job, email) |

## 1.B Entity

| Entity | Spelling used | Where it appears (cited) | Agreement |
|---|---|---|---|
| Frederick Stone | frederick.stone@harmonygames.co | slack EMPLOYEE_0008_SLACK_ID, gmail mailbox frederick.stone@harmonygames.co/1844724419788800011, gdrive d_175c0d7bc72ed244b944cb | AGREE |
| Leonard Hayes | leonard.hayes@harmonygames.co | slack EMPLOYEE_0038_SLACK_ID (C07C2866011/1758303600.418207), trello PERSON_6094_TRELLO_USER_ID (68c64270d660c977c4696986), gdrive owner f_3b9e61c04d7a52e8f1a6c2 | AGREE |
| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID (C096HFA5Z8W/1759184040.552871), gmail frederick.stone@harmonygames.co/1844623441920000059 | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co | linear usr_cc3e90160f490686 (ZOM-567), slack EMPLOYEE_0025_SLACK_ID (C07C2866011/1759168800.117903) | AGREE |
| Sciplay / SciPlay | list row 81 "Sciplay" (f_48247af79428823c3cac92); mail "SciPlay" (frederick.stone@harmonygames.co/1842285743246816270); Robert's reply "Sciplay" (C096HFA5Z8W/1759184040.552871) | AGREE (case only) |
| Hiro Capital | list row 47 (f_48247af79428823c3cac92); Investment Director PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096); Edith Vane PERSON_9903 (e3a91c07d5b48f26a0c7e314) | DISAGREE (designed alias: pass mail names no firm; Contacts maps) |
| T-Accelerate / PXLite | list "T-accelerate" (f_48247af79428823c3cac92); Bubbles notes "PXLite" (frederick.stone@harmonygames.co/1843978997950200606); Calendly note "here from T-Accelerate" (frederick.stone@harmonygames.co/1843625920612854647); Contacts 5d0e8b31f7a29c64e1b0d3a8 | DISAGREE (designed alias, one firm) |
| Brightwater Games Fund / Ilse Marrow | PERSON_9904 (b72f0d6e19c3a84e5d21f9a0, evt_2f86b0d4c9e17a35b64e0d, frederick.stone@harmonygames.co/1844276782694400053) | AGREE (new entity; census below) |
| Paul Heydon, Anton Bernstein | list rows 5 and 4 (f_48247af79428823c3cac92); PERSON_9902, PERSON_9901 | AGREE (angels on the list; no other base footprint) |
| Dentsu team | PERSON_2581, PERSON_5584, PERSON_5221 (frederick.stone@harmonygames.co/1843473831194478743) | AGREE |
| DocuSign | SVC_1302 (base leonard@harmonygames.co_1774464522151433079.json "Completed: Complete with docusign: …") | AGREE (same sender and subject shape) |
| Frederick's GitHub login "Ryan" (S04) | not used | avoid |

## 1.C Voice and realism

Seeded speakers, each with its activity.json (synthcut KB) status at the clock:
- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds dated Sep 14–30 2025 (C07C2866011/1758303600.418207, frederick.stone@harmonygames.co/1844724419788800011).
- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 29 (C096HFA5Z8W/1759161600.226431, frederick.stone@harmonygames.co/1844623441920000059).
- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 29–30 (C07C2866011/1759168800.117903, ZOM-567).
- External senders PERSON_9901_EMAIL (Anton Bernstein), PERSON_9902_EMAIL (Paul Heydon, recipient only), PERSON_9903_EMAIL (Edith Vane), PERSON_9904_EMAIL (Ilse Marrow) and SVC_1302_EMAIL (DocuSign) are not personas (no activity.json entry).

Voice from real messages: Leonard in Slack is lower-case, run-on, 40–200 chars ("I reached out to all VCs except General Catalyst", C096HFA5Z8W/1756935295.190929; "we need to talk to more VCs :disappointed:", C096HFA5Z8W/1758564801.307569); in mail he writes full sentences with "Best regards, Leonard" (frederick.stone@harmonygames.co/1842283406259093714). Robert is short and casual ("Didn't really practice, added new items and made levels instead =/", C096HFA5Z8W/1757400808.661529). Arthur is terse ("I think 2", C096HFA5Z8W/1758207375.664029). Lengths and hours from conventions.json (`slack.length_chars_by_channel_type` private 40–120 p50; `slack.per_person_hours_and_style` Leonard 15–04 UTC; `gmail.internal_subject_len_chars`; `linear.title_prefixes_by_team` ZOM untitled-prefix; `gcal.duration_min` 45). Seeded hours: Slack 17:40Z, 16:00Z, 18:00Z, 22:14Z; Trello 04:20Z and 17:05–17:30Z; mail 09:40Z (UK partner) to 22:30Z.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "Sciplay" | slack C096HFA5Z8W/1757716998.377299 (root), gsheets f_48247af79428823c3cac92 row 81, seeded reply C096HFA5Z8W/1759184040.552871 | the reply is under a multi-firm root |
| "Hiro" | gmail frederick.stone@harmonygames.co/1842278425320449096 (Sep 3), gsheets f_48247af79428823c3cac92 row 47, contacts e3a91c07d5b48f26a0c7e314 | the pass mail frederick.stone@harmonygames.co/1844318935449600041 does not contain it |
| "Brightwater" | NEW TERM — introduced in b72f0d6e19c3a84e5d21f9a0 and frederick.stone@harmonygames.co/1844276782694400053 (Ilse's reply), reached via evt_2f86b0d4c9e17a35b64e0d |
| "Ilse Marrow" | NEW TERM — introduced in evt_2f86b0d4c9e17a35b64e0d (title), frederick.stone@harmonygames.co/1844276782694400053, b72f0d6e19c3a84e5d21f9a0 |
| "Edith Vane" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844318935449600041 (signature), e3a91c07d5b48f26a0c7e314 |
| "Paul Heydon" / "Anton Bernstein" | gsheets f_48247af79428823c3cac92 (list only, 0 Gmail hits in the census); seeded C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e | |
| "board pre-read" | NEW TERM — introduced in f_3b9e61c04d7a52e8f1a6c2 and f_8d2c47a91e05b3f6d7c418, reached via the hub frederick.stone@harmonygames.co/1844724419788800011 |
| "Keep warm" | NEW TERM — introduced in 68c64270d660c977c4696986 (card 68c5a49e8491a9d7faf869d0) |
| "Play internal" | slack C096HFA5Z8W/1758677722.184129 (Arthur: add by email), linear ZOM-567 comment lc_b549f3057640a5eb08f7581e | |
| "Completed: Complete with docusign" | 84 base notices from SVC_1302 (leonard@harmonygames.co_1774464522151433079.json); seeded frederick.stone@harmonygames.co/1844354293432320031 | |

Census with positive control (learnings §35): a full `grep -r -F` over `Universe_SynthCut/SynthCut_HarmonyGames_Gmail` found "Grishin Robotics" (control) in 00001934.json and 0 files for Paul Heydon, Anton Bernstein; "Kestrel" in 3 files (rejected); PERSON_9xxx tokens: 0 uses in 386,054 files (scratch scan). Gmail by name (`grep -r -l -F` over the whole Gmail export): Edith Vane, Ilse Marrow, Brightwater 0 files, control "Grishin Robotics" found (00001934.json). Non-Gmail services: Edith Vane, Ilse Marrow, Brightwater 0 hits (gsheets/gdrive/gdocs/gslides/gcal/trello/linear/contacts/slack/confluence data scanned in Python; control "Grishin Robotics" found in gsheets/gdrive/gdocs/gslides data.json).

## 1.E Persona reach

Load-bearing ids written to `Working_Files/plan/lb_ids.txt`; output verbatim:

```
{{CHECKSQL}}
```

Scoped load-bearing records (all Frederick's copies or files shared with him):
- frederick.stone@harmonygames.co/1844724419788800011 — hub thread in his mailbox (INBOX) LB
- frederick.stone@harmonygames.co/1844162278195200023 — Anton's mail, cc Frederick LB
- frederick.stone@harmonygames.co/1844354293432320031 — DocuSign Completed (Anton), to Frederick LB
- frederick.stone@harmonygames.co/1844610859008000037 — Leonard's nudge to Paul, cc Frederick LB
- frederick.stone@harmonygames.co/1844318935449600041 — Edith Vane's pass, cc Frederick LB
- evt_7d3e19b04a6c25f8e1b9a0 — Hiro pitch call (Tue Sep 23) on Frederick's calendar LB
- frederick.stone@harmonygames.co/1844294398771200045 — Ryo-san's tester addresses and Leonard's "invites are out" reply, cc Frederick LB
- frederick.stone@harmonygames.co/1844276782694400053 — Brightwater follow-up and Ilse's reply, cc Frederick LB
- f_3b9e61c04d7a52e8f1a6c2 — template shared with Frederick (reader) LB
- d_5e8a1c3f9b07d2e64a1b93 — Board folder owned by Frederick LB
- evt_2f86b0d4c9e17a35b64e0d — Brightwater call on Frederick's calendar LB
- C096HFA5Z8W — #bridge-pitch, Frederick a member LB
- C07C2866011 — #executives, Frederick a member LB
- Unscoped (visible to all): ZOM-567, 68c64270d660c977c4696986, e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8.

## 1.F Collision

- Minted ids checked: Slack ts C07C2866011/1758303600.418207, C07C2866011/1759168800.117903, C096HFA5Z8W/1759161600.226431, C096HFA5Z8W/1759184040.552871 absent from the month files; ZOM-567 absent (max ZOM 566); f_/d_/evt_/24-hex ids (f_3b9e61c04d7a52e8f1a6c2, f_8d2c47a91e05b3f6d7c418, f_c61a0e93b7d24f58a2e917, d_5e8a1c3f9b07d2e64a1b93, f_a47d0e2c95b18f63e2c0d5, f_6e1d93a0c4b72f85d39a0e, evt_2f86b0d4c9e17a35b64e0d, evt_9c41e7a2d05b38f6e1a7c4, evt_7d3e19b04a6c25f8e1b9a0, e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8) absent from gdrive/gdocs/gsheets/gslides/gcal/contacts data (Python containment scan with control f_48247af79428823c3cac92 found); base_check Check A (identifier uniqueness over the full collections) PASS.
- Header tokens: PERSON_9901–9904_EMAIL unused anywhere (0 of 386,054 files); existing tokens reused only for their own people (PERSON_5282 Hiro Investment Director, PERSON_3242 Karthic of T-Accelerate per frederick.stone@harmonygames.co/1843625920612854647, Dentsu PERSON_2581/5584/5221, SVC_1302 DocuSign).
- Body tokens: none minted ([IDENTIFIER_99011] in the DocuSign link is a new link placeholder in the base's style; no identity).

## Record ledger

| # | Table | Id | Manifest element | Carrier | Discovery role |
|---|---|---|---|---|---|
{{LEDGER}}

## Findability and discovery-order proofs

- Hub (A1) frederick.stone@harmonygames.co/1844724419788800011 — query "board pre-read" / "fundraising section" via gmail search; first link (prompt names it).
- Template H1 f_3b9e61c04d7a52e8f1a6c2 — query "board pre-read template" via gdocs/drive search; competing hit the July decoy f_8d2c47a91e05b3f6d7c418 (same words; dated by its body "for the Jul 16 board").
- Card rule H2 68c64270d660c977c4696986 on 68c5a49e8491a9d7faf869d0 — query "Existing Investor Update" via trello search returns the card; the rule is in comments (trello_get_comments); decoy 663ea0fc3f231e879cefd5e8 "Investor Update".
- CORR C096HFA5Z8W/1759184040.552871 — claim met first: the SciPlay thread frederick.stone@harmonygames.co/1842285743246816270 ("We'll continue to play and let you know"); overturned by Robert's reply under C096HFA5Z8W/1757716998.377299; met first because a firm-name mail search hits the thread; channel history omits replies.
- DONE1 C07C2866011/1758303600.418207 met first (channel history), Leonard's sheet f_6e1d93a0c4b72f85d39a0e repeats it; overturned by the absence of a DocuSign Completed notice for Paul beside Anton's (frederick.stone@harmonygames.co/1844354293432320031) and Leonard's nudge frederick.stone@harmonygames.co/1844610859008000037.
- INPUT: $40K in C07C2866011/1758303600.418207 and f_6e1d93a0c4b72f85d39a0e; overturned by frederick.stone@harmonygames.co/1844162278195200023 ($25K).
- DONE2: frederick.stone@harmonygames.co/1844294398771200045 ("Invites … are out to all three") met with the firm; overturned by ZOM-567 comment lc_b549f3057640a5eb08f7581e (Play track not added).
- ALIAS: list row "no response as of 09/11" (f_48247af79428823c3cac92) met first; overturned by frederick.stone@harmonygames.co/1844318935449600041 ("Thanks again for the session on Tuesday") mapped through e3a91c07d5b48f26a0c7e314, the cc of PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096) and the Tue Sep 23 call evt_7d3e19b04a6c25f8e1b9a0 (PERSON_5487, the To of the Sep 3 Hiro thread, and Edith as guests). The call also makes Hiro a pass after a pitch call, which the keep-warm rule 68c64270d660c977c4696986 needs.
- FILT: list read first; Homa via evt_89381fe5a15b802c5652a9 + "HOMA" in frederick.stone@harmonygames.co/1843169166284025277; Brightwater via evt_2f86b0d4c9e17a35b64e0d + b72f0d6e19c3a84e5d21f9a0.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | — | every deciding fact persona-readable (1.E, check-sql PASS) |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: Anton "the 40 we talked about" after the Sep 19 post (C07C2866011/1758303600.418207); Robert's reply "this morning" at 22:14Z = 3:14pm PT Sep 29; ZOM-567 created after ZOM-566 |
| Cross-service Referential | base_check Check A PASS | same amounts per service ($50K Paul in C07C2866011/1758303600.418207 and f_6e1d93a0c4b72f85d39a0e) |
| Quantitative | reply counters updated (73c2247f4a31f32d10b3068ecd1d13ac) | no figure quoted against a base row |
| State / Lifecycle | Linear Todo without stamps (ZOM-567) | Leonard's "invites are out" vs ZOM-567 is a dated human claim overturned later (intended) |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A) |
| Semantic / Category | — | titles match content (f_3b9e61c04d7a52e8f1a6c2, 68d8193cf451863621c88a2a) |
| Other | — | voice per 1.C; no record states a conclusion or total |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails | seeded: Brightwater call and Hiro call (Frederick, Robert, Arthur each) and the Oct 6 review (Frederick) |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / mail digest | none: ZOM-567 has no PR; Arthur assigns himself (no notification to Frederick) |
| gdrive | INT-13 | Drive Slack app share DM | none: shares predate Slack DM pattern for these docs (base shares in Frederick's view carry no DM for Leonard's docs, e.g. f_17e6175e84e745f92b3415) |
| slack | INT-22 | Slack email notifications | none: no @mention of Frederick in the seeded posts |
| trello | INT-21 | no Trello→Slack integration | none |
| gmail, gdocs, gsheets, gslides, contacts | not integration sources | — | none |

## Touched-data census and coherence hazards

Touched data: the hub and its copies; the template and July decoy; the Board folder and README; the deck; the angels sheet; #bridge-pitch Sep (C096HFA5Z8W, root C096HFA5Z8W/1757716998.377299 whose counters the SQL updates) and #executives Sep (C07C2866011); every cc'd investor thread (frederick.stone@harmonygames.co/1842285743246816270, frederick.stone@harmonygames.co/1842277743427687737, frederick.stone@harmonygames.co/1842278425320449096, frederick.stone@harmonygames.co/1842283406259093714, frederick.stone@harmonygames.co/1843473831194478743, frederick.stone@harmonygames.co/1832208184829815962, frederick.stone@harmonygames.co/1843547312959065138); calendar Sep 3–30 (evt_89381fe5a15b802c5652a9); the list f_48247af79428823c3cac92; cards 68c5a49e8491a9d7faf869d0 and 68d8193cf451863621c88a2a; ZOM-567; three contacts.

Hazards from coherence_hazards.json:
- temporal: T03 none in scope — the Speedrun forward frederick.stone@harmonygames.co/1844748127814183717 (Oct 1 03:21Z) is after the seed bound; a16z is never graded (both statuses accepted).
- semantic: S04 (Frederick's GitHub "Ryan") avoided; no GitHub record touched (github none in scope).
- referential: R08 (invitation mails vs calendar) — every seeded event has its invitation copies (evt_2f86b0d4c9e17a35b64e0d, evt_7d3e19b04a6c25f8e1b9a0, evt_9c41e7a2d05b38f6e1a7c4).
- quantitative: Q01/Q03 — the seeded reply's root 73c2247f4a31f32d10b3068ecd1d13ac gets reply_count 1, reply_users_count 1, latest_reply 1759184040.552871 (companion UPDATE).
- state/lifecycle: L08 — ZOM-567 (Arthur, active_sep_2025_quiet_in_oct) is a Sep 30 ticket with a dated plan ("Will chase Thursday"); no acknowledgement required (new record, not a hazard example).
- identifier/format: I03 — seeded files use the roster address frederick.stone@harmonygames.co (not the frederick@ alias); I14 — the list f_48247af79428823c3cac92 is Resource-owned, read only.

Known data issues (references/known_data_issues/synthcut.md, read at design per learnings §44, checked against the touched list f_48247af79428823c3cac92 and threads; no load-bearing fact, trap or graded slot rests on a card's "Don't grade" value):
- SC-33 (watch, investor sheet lists Acterra twice): touched by V1 (register size). Relied-on side: the incorporated template rule f_3b9e61c04d7a52e8f1a6c2 ("one row per name on the 2025 game investor list, angels included … a repeated name is still one row"), which counts Acterra (rows 71/86), Progression Fund (22/23) and BITKRAFT Ventures (32/33) once each in f_48247af79428823c3cac92; "Treo/Treeo" is a Slack spelling (C096HFA5Z8W/1756941551.539229), not a list duplicate. No raw sheet count is graded.
- SC-34 (row 82 labeled Superplay, contents Supercell): row 82's status is never sampled; it is one register row under either name (f_48247af79428823c3cac92).
- SC-9 (Play Ventures rejected vs no reply): never graded; both statuses accepted (C096HFA5Z8W/1757955553.793529, C096HFA5Z8W/1758671737.632949).
- SC-10 (LVP meeting date Sep 7 vs Sep 9): no date graded; LVP's status comes from its own thread frederick.stone@harmonygames.co/1842277743427687737; the call is evt_e59dc0a675d0c407b79acf (Sep 9).
- SC-40 (July board date 14 vs 16): the seeded July template says "for the Jul 16 board" (f_8d2c47a91e05b3f6d7c418), the card's safer value; not graded.
- SC-49 (founder count, Frederick's role): no founder count or founder status is graded; the role review rests on activity (evt_bd61f3209523d19fdd6ba2, C096HFA5Z8W).
- SC-3 / SC-73 (runway, monthly burn): no cash, runway or burn figure is read or graded (snowflake.FINANCE untouched).
- SC-7 (channel membership): membership is used only for reach (C096HFA5Z8W, C07C2866011), never graded.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Paul Heydon "is in for $50K" (C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e) | no DocuSign Completed notice for Paul; nudge frederick.stone@harmonygames.co/1844610859008000037 (Sep 29) | founders post verbal yeses before docs; the template defines committed as signed | soft-circled $50,000 |
| Anton Bernstein $40K (same post, sheet) | frederick.stone@harmonygames.co/1844162278195200023 (Sep 24, $25K) and Completed notice frederick.stone@harmonygames.co/1844354293432320031 | angels trim checks | committed $25,000 |
| Dentsu "invites … out to all three" (frederick.stone@harmonygames.co/1844294398771200045, Leonard's Sep 26 17:20Z reply to Ryo-san's 03:10Z addresses mail) | ZOM-567 comment lc_b549f3057640a5eb08f7581e (Sep 30): Play track not added | Play internal tracks need the console owner (base C096HFA5Z8W/1758677722.184129) | iOS only |
| SciPlay "we'll continue to play" (frederick.stone@harmonygames.co/1842285743246816270, Sep 18) | Robert's reply C096HFA5Z8W/1759184040.552871 (Sep 29) | investors pass by phone | Passed |
| Hiro "no response as of 09/11" (f_48247af79428823c3cac92) | frederick.stone@harmonygames.co/1844318935449600041 (Sep 26) + e3a91c07d5b48f26a0c7e314 | the list's Latest Status column stops at 09/11 | Passed |
| July template committed = verbal yes (f_8d2c47a91e05b3f6d7c418) | Oct 14 template (f_3b9e61c04d7a52e8f1a6c2) | per-board templates | signed SAFE only |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's board pre-read email; the fundraising section ask | frederick.stone@harmonygames.co/1844724419788800011 |

Never name in the prompt: the template's location or definitions, the Existing Investor Update card's rule, Robert's thread, ZOM-567, the DocuSign notices, Contacts, Brightwater, Homa, PXLite, any amount, status, count or firm. Destinations the prompt may name: the Board - Oct 14 2025 folder (d_5e8a1c3f9b07d2e64a1b93), a reply on Leonard's email (frederick.stone@harmonygames.co/1844724419788800011). Deadline: before Monday's review (evt_9c41e7a2d05b38f6e1a7c4, Oct 6). Deliverable kinds: one Google Sheet, an email reply, Trello checklist items (by the card's rule, not by the prompt).

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| Paul Heydon | 50000 | amount | 4921f321db5d08f936aac24a6a1d2af8 (C07C2866011/1758303600.418207), f_6e1d93a0c4b72f85d39a0e |
| Anton Bernstein | 25000 | amount | frederick.stone@harmonygames.co/1844162278195200023 (both copies); superseded versions 4921f321db5d08f936aac24a6a1d2af8, f_6e1d93a0c4b72f85d39a0e |
| keep-warm rule | Keep warm | name | 68c64270d660c977c4696986 |

```
{{FACTCHECK}}
```

Solver totals (`solver/truth.json`, sha256 cda8fce125b347aa): register 79 firms; committed total 25,000 (Anton Bernstein); soft-circled total 50,000 (Paul Heydon); keep-warm members London Venture Partners, Sciplay, Hiro Capital (a16z accepted either way); Dentsu Ventures build access iOS only; T-accelerate iOS and Android.

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| frederick.stone@harmonygames.co/1844724419788800011 | seeded | Leonard → Frederick, cc Robert, Arthur, 2025-09-30T21:05Z: the ask | Frederick's INBOX | authority (hub, anchor) |
| f_3b9e61c04d7a52e8f1a6c2 | seeded | template: buckets, as-of end of Sep 30 PT, committed = DocuSign Completed, soft = latest written amount, build access per tester list | shared reader | authority H1 |
| f_8d2c47a91e05b3f6d7c418 | seeded | July template: committed = verbal yes | shared reader | decoy (superseded) |
| d_5e8a1c3f9b07d2e64a1b93 | seeded | Board - Oct 14 2025 folder, owner Frederick; README f_c61a0e93b7d24f58a2e917 names files "Fundraising - Oct 14 board" | owner | write target |
| frederick.stone@harmonygames.co/1844162278195200023 | seeded | Anton 2025-09-24T16:10Z: $25K, not 40 | cc | overturning evidence |
| frederick.stone@harmonygames.co/1844354293432320031 | seeded | DocuSign Completed: SAFE - Anton Bernstein, 2025-09-26T19:02Z | to Frederick | evidence |
| frederick.stone@harmonygames.co/1844610859008000037 | seeded | Leonard → Paul 2025-09-29T15:00Z: SAFE still with you | cc | overturning evidence |
| frederick.stone@harmonygames.co/1844318935449600041 | seeded | Edith Vane 2025-09-26T09:40Z: thanks for Tuesday's session, pass on the bridge (no firm name), cc PERSON_5282 | cc | overturning evidence (alias) |
| evt_7d3e19b04a6c25f8e1b9a0 | seeded | "PERSON_5487_NAME and Leonard Hayes" 2025-09-23T16:00–16:45Z (guests: founders, PERSON_5487, Edith Vane); invitations 2025-09-19T18:30Z | Frederick's calendar + INBOX | evidence (Hiro pitched on a call) |
| frederick.stone@harmonygames.co/1844294398771200045 | seeded | Ryo-san (PERSON_5221) 2025-09-26T03:10Z: three tester addresses; Leonard's reply 17:20Z: invites out to all three | cc | claim met first |
| frederick.stone@harmonygames.co/1844276782694400053 | seeded | Brightwater follow-up 2025-09-25T22:30Z (deck to follow separately) + Ilse's reply 2025-09-26T15:05Z signed "Principal, Brightwater Games Fund" | cc | evidence (off-list firm) |
| evt_2f86b0d4c9e17a35b64e0d | seeded | "Ilse Marrow and Leonard Hayes" 2025-09-25T15:30–16:15Z | Frederick's calendar | evidence |
| evt_9c41e7a2d05b38f6e1a7c4 | seeded | Board pre-read review, Oct 6 16:00Z | Frederick's calendar | deadline |
| C096HFA5Z8W/1759184040.552871 | seeded | Robert 2025-09-29T22:14Z under C096HFA5Z8W/1757716998.377299: Sciplay out | member | overturning evidence |
| C07C2866011/1758303600.418207 | seeded | Leonard 2025-09-19T17:40Z: Paul $50K, Anton $40K "in" | member | claim met first |
| C07C2866011/1759168800.117903 | seeded | Arthur: just list who Leonard emailed | member | distractor |
| f_6e1d93a0c4b72f85d39a0e | seeded | Bridge angels sheet (stale, Sep 20) | shared reader | claim met first |
| frederick.stone@harmonygames.co/1844623441920000059 | seeded | Robert: email the board directly (withdrawn by the hub) | to Frederick | distractor |
| frederick.stone@harmonygames.co/1842285743246816270 | base | SciPlay thread, last investor word Sep 18 | cc | claim met first |
| frederick.stone@harmonygames.co/1842277743427687737 | base | LVP pass Sep 25 (call Sep 9, evt_e59dc0a675d0c407b79acf) | cc | evidence (keep-warm) |
| frederick.stone@harmonygames.co/1843169166284025277 | base | Homa invitation ("HOMA") for evt_89381fe5a15b802c5652a9 | cc | evidence (off-list firm) |
| f_48247af79428823c3cac92 | base | 2025 game investor list, 80 rows / 77 firms, Latest Status as of 09/11 | shared | population |

## Platform /injection review of rev1 and the rev2 changes

The platform review of rev1 (`Task_Authoring/task_inputs/Platform_Report/injection_report1`, copied to `run_forensics/rev1/design/platform_injection_report_PASS.md`; SQL sha256 0b6812c56fe6876a, 129 INSERT + 6 UPDATE) returned FINAL VERDICT: PASS with four advisories. Dispositions:

| Advisory | Finding | Disposition | Evidence |
|---|---|---|---|
| 1 | slides_pages.notes, slides_page_elements.table_json / ordinal and linear_comments.sequence are not in the eval's 58-table schema snapshot | kept: the platform's own schema export (references/universe_schema_live.json, exported from the platform DB 2026-10-04) lists all four columns; the completed Julia task's SQL wrote the same columns and its six baselines ran on the loaded injection | universe_schema_live.json (gslides.slides_pages notes; gslides.slides_page_elements table_json, ordinal; linear.linear_comments sequence); support/completed_tasks/julia_zm_difficulty_baseline_2026-11-01 |
| 2 | Edith Vane thanks Leonard for a "session", but no Hiro call is recorded this round; the keep-warm rule (passes after a call or meeting) makes Hiro's membership depend on it | fixed in rev2: the Sep 3 Hiro thread frederick.stone@harmonygames.co/1842278425320449096 is a re-intro email, not a call; rev2 seeds the call evt_7d3e19b04a6c25f8e1b9a0 (Tue 2025-09-23 16:00–16:45Z, created 2025-09-19T18:30Z after the list's "as of 09/11" note) on four calendars with invitation mails, and Edith's mail now reads "Thanks again for the session on Tuesday. We discussed it as a team yesterday" | evt_7d3e19b04a6c25f8e1b9a0, frederick.stone@harmonygames.co/1844318935449600041 |
| 3 | Leonard's Brightwater mail claims attachments with no attachment metadata | fixed in rev2: "I'll send the deck and the puzzle engine doc over in a separate email" | frederick.stone@harmonygames.co/1844276782694400053 |
| 4 | Leonard's "thank you for sending your emails" and Arthur's "came in Fri" refer to an unrecorded Dentsu message | fixed in rev2: Ryo-san's Fri 2025-09-26 03:10Z mail with the three addresses starts the thread; Leonard's "invites are out" mail is its reply | frederick.stone@harmonygames.co/1844294398771200045; ZOM-567 comment lc_b549f3057640a5eb08f7581e |

Rev2 also tightens the template's population rule for known data issue SC-33 ("one row per name on the 2025 game investor list, angels included … a repeated name is still one row", f_3b9e61c04d7a52e8f1a6c2). Rev2 changes no rule, slot or truth value (truth.json sha256 cda8fce125b347aa in both revisions; oracle_kit regression against rev1: 0 field differences). An intermediate rev2 (sha256 d158f2e7ab51, before the template change) was never reviewed and is kept unedited in run_forensics/rev2a_superseded/. Rev2 needs /injection again before /prompt (the rev1 report is bound to sha256 0b6812c56fe6).

### Platform /injection review of rev2 and the rev3 changes

The review of rev2 (`Platform_Report/injection_report2`, copied to `run_forensics/rev2/design/platform_injection_report_PASS.md`; sha256 b2bfda86002c, 143 INSERT + 10 UPDATE) returned FINAL VERDICT: PASS, recorded rev1's three fixed advisories as resolved, and raised five advisories:

| Advisory | Finding | Disposition | Evidence |
|---|---|---|---|
| 1 | the same four columns outside the snapshot; the Trello comment relies on slide-9 speaker notes | columns kept (as rev1 advisory 1; also written by the completed Frederick card-spend and Douglas SQL); rev3 moves the column list into slide 9's visible text, leaves every speaker note NULL and rewords the comment to "Slide 9 of the draft deck lists the table's columns" | f_a47d0e2c95b18f63e2c0d5, 68d81f30a6c94e2b7d05e1f4 |
| 2 | Arthur's "came in Fri" vs Ryo-san's mail at Thu 20:10 PT | fixed in rev3: "came in Thursday night" | ZOM-567 comment lc_b549f3057640a5eb08f7581e |
| 3 | Leonard double-booked 16:30–16:45Z on Sep 25 | fixed in rev3: the Brightwater call is 15:30–16:15Z (8:30–9:15 PT), clear of evt_c6d85261f1e1dc58ddf1ad | evt_2f86b0d4c9e17a35b64e0d |
| 4 | the board's dateLastActivity was not bumped | fixed in rev3: UPDATE to 2025-09-27T17:30:24Z | trello board 640643a3fd8f3ca308d9318e |
| 5 | T-Accelerate Play track "added Sep 23" vs the link shared Sep 22 | kept: link shared Sep 22, tester added Sep 23 (the reviewer agrees it is consistent) | frederick.stone@harmonygames.co/1842283406259093714 |

Rev3 changes no rule, slot or truth value; it needs /injection again before /prompt.

### Platform /injection review of rev3 (current)

The review of rev3 (`Platform_Report/injection_report3`, copied to `run_forensics/rev3/design/platform_injection_report_PASS.md`; sha256 952e12a9ad7a6b88, 143 INSERT + 11 UPDATE) returned FINAL VERDICT: PASS / COMPLETE and recorded rev2's advisories 2–4 as resolved and advisory 1 as narrowed. Remaining advisories and dispositions:

| Advisory | Finding | Disposition | Evidence |
|---|---|---|---|
| 1 | slides_pages.notes (all NULL), slides_page_elements.table_json (all NULL) / ordinal and linear_comments.sequence are outside the eval's schema snapshot; no task content depends on them | kept: the platform's schema export (universe_schema_live.json, 2026-10-04) lists all four, and the completed Julia, Frederick card-spend and Douglas injections wrote the same columns and loaded (their baselines read the injected rows); dropping them would only add another /injection cycle | f_a47d0e2c95b18f63e2c0d5, ZOM-567 |
| 2 | T-Accelerate Play track added Sep 23 vs the link shared Sep 22 | kept: consistent (link shared Sep 22, tester added Sep 23), as the reviewer states | frederick.stone@harmonygames.co/1842283406259093714 |

Rev3 is the SQL for /prompt, /hardness, /oe and /rubric; its static checks may be reused while sha256 952e12a9ad7a6b887a783b1aa8f8d028fd7807a460d3b5b0c39d0cf5d79985a2 holds. Investor-list visibility (left to /prompt by the reviewer): f_48247af79428823c3cac92 is shared with frederick.stone@harmonygames.co (persona_view can-see YES, section 1.E).

## Platform follow-ups

- ○ carriers to confirm in the Opus pre-check: Contacts `job` through contacts_search_contacts (e3a91c07d5b48f26a0c7e314); no speaker notes are relied on: slide 9's columns are visible element text (f_a47d0e2c95b18f63e2c0d5).
- Trello comment rendering through trello_get_comments (68c64270d660c977c4696986) and Linear comments through linear_list_comments (ZOM-567; ● per Ask_Carriers §6b).
- Preflight digest: `01c_Preflight_Report.json` binds the SQL, solver, surface, manifest and dispositions by sha256; the optional manifest `preflight {report, digest}` field is not written, because the report hashes the whole manifest file and the field would stale it (recorded here instead).

## Self-review

Tool outputs (final run, verbatim):

```
{{SQLLINT}}
```

Warning dispositions: weekend warn (Trello actions on Sat Sep 14 04:20Z = Fri Sep 13 9:20pm PT, and Sat Sep 27 17:05–17:30Z) — disposition: Leonard posts on weekends in the base (#bridge-pitch Sep 6–7 and Sep 28: C096HFA5Z8W/1757282790.636379); after the clock warn (trello due 2025-10-14, gcal Oct 6 review) — disposition: deadline and not-yet-happened event, plan fields only.

```
{{BASECHECK}}
```

```
{{BASECLAIMS}}
```

```
{{HGATE}}
```

{{HGLINT}} — no FAIL or CHECK flag to disposition.

Preflight: `PREFLIGHT: PASS` (solver contract PASS, surface PASS, all 30 mutation results dispositioned in 01c_Dispositions.json, geometry U = 0.8841 > 0.15, L_max 0.5072 OK); mutation (verbatim tail):

```
{{MUTATION}}
```

Forecast (UNCALIBRATED, pre-registered for rev3 as hev_5d9bd3b90d474f0e; earlier records: rev1 hev_4c8f05e25916f114, rev2a hev_e6d9d0fba5e9c65a, rev2 hev_a994b86c419749c5): V3 E[avg] 0.715–0.737, P(all four difficulty gates) 0.078–0.351; channel rates for CH-FILT-HOMA 0.35 and CH-FILT-BRIGHT 0.50 are disclosed author overrides (no ledger records); text-graded slots (RP2, RP3, KW1, KW2) are not simulated, so losses are understated.

Checks A–C walk (Evals/0_Injection_Quality_Eval.md): inventory 143 INSERT + 11 UPDATE (sql_lint); Check A references, uniqueness over full collections, ownership/membership (Frederick in C096HFA5Z8W and C07C2866011; owner of d_5e8a1c3f9b07d2e64a1b93), id contracts — PASS (base_check, eval lint); Check B structure, literal JSON, generated/NOT NULL columns — PASS (sql_lint 0 errors, eval lint FAIL 0); Check C dates, parent/reply, counts — PASS (base_check), every seed before 2025-10-01T00:00Z; no PENDING item.

Touched-data census: listed above under "Touched-data census and coherence hazards".

| # | Category | Counter-reading (strongest case it fails) | Evidence | Verdict |
|---|---|---|---|---|
| 1 | temporal | Robert's reply says "this morning" but is posted 3:14pm PT | C096HFA5Z8W/1759184040.552871 | consistent: a morning call noted in the afternoon |
| 2 | semantic | "Sciplay" vs "SciPlay" reads as two firms | f_48247af79428823c3cac92, frederick.stone@harmonygames.co/1842285743246816270 | case variant of one name; register key follows the list |
| 3 | cross-service referential | Edith's pass names no firm, so it cannot be placed | e3a91c07d5b48f26a0c7e314, cc PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096) | resolvable through two persona-visible records |
| 4 | quantitative | Leonard's sheet still says Anton 40000, contradicting Anton's mail | f_6e1d93a0c4b72f85d39a0e (Sep 20) vs frederick.stone@harmonygames.co/1844162278195200023 (Sep 24) | dated stale tracker, later mail overturns (intended) |
| 5 | state/lifecycle | Leonard says Dentsu has invites; ZOM-567 says Play not added | frederick.stone@harmonygames.co/1844294398771200045, lc_b549f3057640a5eb08f7581e | dated human claim overturned by the later ticket comment |
| 6 | identifier/format | DocuSign link placeholder [IDENTIFIER_99011] is a new token | frederick.stone@harmonygames.co/1844354293432320031 | base links use [IDENTIFIER_n] placeholders (leonard@harmonygames.co_1774464522151433079.json); no identity meaning |
| 7 | other | the Paul nudge makes DONE1 trivially visible | frederick.stone@harmonygames.co/1844610859008000037 | a fair resolver is required (UGT); the post and sheet remain the first convincing sources |
| 8 | intended disagreement (Paul) | an unintended inconsistency between post and signing state | C07C2866011/1758303600.418207 | dated verbal claim vs later signing records; template defines committed |
| 9 | intended disagreement (Anton) | two amounts for one person in two services | frederick.stone@harmonygames.co/1844162278195200023 | later message from the investor himself |
| 10 | intended disagreement (Dentsu) | the mail and ticket are both system-like | ZOM-567 | both are human texts with dates (Leonard Sep 26, Arthur Sep 30) |
| 11 | intended disagreement (SciPlay) | Robert's note could be hearsay | C096HFA5Z8W/1759184040.552871 | the template makes written phone notes count |
| 12 | intended disagreement (Hiro) | list column vs mail | f_48247af79428823c3cac92 | the column states its own date (as of 09/11) |
| 13 | intended disagreement (templates) | two live templates with different rules | f_8d2c47a91e05b3f6d7c418 vs f_3b9e61c04d7a52e8f1a6c2 | different boards (Jul 16 vs Oct 14), the hub names the Oct 14 one |
| 14 | people status | Arthur quiet in Oct yet owns an open ticket | arthur.blake@harmonygames.co, ZOM-567 | ticket and comment dated Sep 30, before the clock |
| 15 | cross-service referential (rev2) | the seeded Hiro call contradicts the list's "no response as of 09/11" or Leonard's Sep 8 tracker | f_48247af79428823c3cac92 (modified 2025-09-15T19:27:01Z), C096HFA5Z8W/1757345124.546449, evt_7d3e19b04a6c25f8e1b9a0 (created 2025-09-19T18:30Z) | the call is booked after both dated notes; no base calendar row holds any Hiro person, so nothing is contradicted |
| 16 | temporal (rev3) | Ryo-san's mail is dated Friday in Japan but Thursday evening in LA, and Arthur's note must match | frederick.stone@harmonygames.co/1844294398771200045 (2025-09-26T03:10Z = Fri 12:10 JST, Thu 20:10 PT) | rev3: Arthur writes "came in Thursday night" (PT); Leonard's reply is Fri Sep 26 PT |

Re-verified from source this session through tools/hg.py and the exports: list rows (f_48247af79428823c3cac92), SciPlay messages (gmail:threads/frederick@harmonygames.co_1842285743246816270.json /messages/1), T-Accelerate recap (/messages/0 of 1842283406259093714), Calendly note "here from T-Accelerate" (frederick.stone@harmonygames.co/1843625920612854647), Hiro Investment Director signature (leonard@harmonygames.co_1842278433020808799.json), ZOM-566 creation time, DocuSign notice shapes.

Unresolved: no independent (dual red-team) review — REDTEAM_* unset; forecast channel rates are author overrides (UNCALIBRATED); ○ carriers (Contacts job, slide notes) await confirmation in the Opus pre-check.
