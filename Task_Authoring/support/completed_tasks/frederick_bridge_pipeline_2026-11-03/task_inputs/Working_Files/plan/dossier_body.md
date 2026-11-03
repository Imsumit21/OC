# Grounding Dossier — frederick_bridge_pipeline · injection rev12 (Q4 update send list) · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev12/01_Universe_Inject.sql`; rev12 moves Leonard's "Paul's out" into his 1:1 DM with Frederick, removes the T-Accelerate mail replies and makes Arthur's correction a #zombie-match3d root post naming four firms in talks after the rev11 baseline (section "Rev11 baseline and the rev12 change"); rev11 had Paul back out in a thread reply under Leonard's angel post and splits the Play correction by firm, with Arthur's answer to Karthic in the T-Accelerate mail thread, after the rev10 baseline (section "Rev10 baseline and the rev11 change"); rev10 moved Arthur's Play correction into a thread reply under Leonard's 0.3.49 iOS release post and adds Paul's "signed it" reply after the rev9 /hardness (section "Platform /hardness of rev9 and the rev10 change"); rev9 added Leonard's Sep 29 card comment, his open To Do card for NCsoft's partner and the Oct 8 Makers Fund call after the rev8 baseline (section "Rev8 baseline and the rev9 change"); earlier: rev6 (sha256 848189443008) passed the platform /injection and scored every /prompt content dimension 5 but failed the new dataset-duplicate gate, see "Platform /prompt review of rev6 and the rev7 job change"; rev5 (sha256 3ba2b413458f) passed the platform /injection and /prompt reviews and then failed the platform Opus pre-check /hardness (score 1, too easy), see "Platform Opus pre-check of rev5 and the rev6 changes"; rev1 (sha256 0b6812c56fe6), rev2 (sha256 b2bfda86002c), rev3 (sha256 952e12a9ad7a) and rev4 (sha256 2e2428bc5e49) each passed the platform /injection review and are kept in `run_forensics/rev1/`–`rev4/` with their reports and design files; rev3 and rev4 then failed the platform /prompt review, see "Platform /prompt review of rev3 and the rev4 changes" and "Platform /prompt review of rev4 and the rev5 changes"),
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
| Robert | robert@harmonygames.co | slack EMPLOYEE_0016_SLACK_ID (C07C2866011/1759248360.377105), gmail frederick.stone@harmonygames.co/1844623441920000059 | AGREE |
| Arthur Blake | arthur.blake@harmonygames.co | linear usr_cc3e90160f490686 (ZOM-567), slack EMPLOYEE_0025_SLACK_ID (C07C2866011/1759168800.117903, C0880U9751A/1759274400.518306) | AGREE |
| Sciplay / SciPlay | list row 81 "Sciplay" (f_48247af79428823c3cac92); mail "SciPlay" (frederick.stone@harmonygames.co/1842285743246816270); Robert's reply "Sciplay" (C07C2866011/1759248360.377105) | AGREE (case only) |
| Hiro Capital | list row 47 (f_48247af79428823c3cac92); Investment Director PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096); Edith Vane PERSON_9903 (e3a91c07d5b48f26a0c7e314) | DISAGREE (designed alias: pass mail names no firm; Contacts maps) |
| T-Accelerate / PXLite | list "T-accelerate" (f_48247af79428823c3cac92); Bubbles notes "PXLite" (frederick.stone@harmonygames.co/1843978997950200606); Calendly note "here from T-Accelerate" (frederick.stone@harmonygames.co/1843625920612854647); Contacts 5d0e8b31f7a29c64e1b0d3a8 | DISAGREE (designed alias, one firm) |
| Brightwater Games Fund / Ilse Marrow | PERSON_9904 (b72f0d6e19c3a84e5d21f9a0, evt_2f86b0d4c9e17a35b64e0d, frederick.stone@harmonygames.co/1844276782694400053) | AGREE (new entity; census below) |
| Paul Heydon, Anton Bernstein | list rows 5 and 4 (f_48247af79428823c3cac92); PERSON_9902, PERSON_9901; Leonard's DM names "Anton" (D05S58U4SAK/1758731100.281734) | AGREE (angels on the list; no other base footprint) |
| T-Accelerate / Karthic (rev6 build access) | ZOM-567 comment lc_94eb35d962cfbdd31e1bd496 "T-Accelerate (Karthic)"; rev12: Arthur's #zombie-match3d post C0880U9751A/1759274400.518306 names Karthic; Contacts 5d0e8b31f7a29c64e1b0d3a8 | AGREE |
| Dentsu team | PERSON_2581, PERSON_5584, PERSON_5221 (frederick.stone@harmonygames.co/1843473831194478743) | AGREE |
| DocuSign | SVC_1302 (base leonard@harmonygames.co_1774464522151433079.json "Completed: Complete with docusign: …") | AGREE (same sender and subject shape) |
| Frederick's GitHub login "Ryan" (S04) | not used | avoid |

## 1.C Voice and realism

Seeded speakers, each with its activity.json (synthcut KB) status at the clock:
- Leonard Hayes (leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds dated Sep 14–30 2025 (C07C2866011/1758303600.418207, frederick.stone@harmonygames.co/1844724419788800011).
- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 29–30 (frederick.stone@harmonygames.co/1844623441920000059; rev6 thread reply C07C2866011/1759248360.377105, Sep 30 16:06Z, beside his own base #executives posts that day).
- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_sep_2025_quiet_in_oct; seeds Sep 29–30 (C07C2866011/1759168800.117903, ZOM-567; rev6 #zombie-match3d post C0880U9751A/1759274400.518306, where he posts builds: "for android test latest on the Harmony Games build site", C0880U9751A Sep 16).
- Leonard's rev6 DM lines (D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218) follow his DM voice with Frederick (short lower-case lines, D05S58U4SAK Sep 2025), and his #zombie-match3d reply (C0880U9751A/1759276080.094417) his channel voice.
- External senders PERSON_9901_EMAIL (Anton Bernstein), PERSON_9902_EMAIL (Paul Heydon; rev11: his back-out mail goes to Leonard only), PERSON_9903_EMAIL (Edith Vane), PERSON_9904_EMAIL (Ilse Marrow) and SVC_1302_EMAIL (DocuSign) are not personas (no activity.json entry).

Voice from real messages: Leonard in Slack is lower-case, run-on, 40–200 chars ("I reached out to all VCs except General Catalyst", C096HFA5Z8W/1756935295.190929; "we need to talk to more VCs :disappointed:", C096HFA5Z8W/1758564801.307569); in mail he writes full sentences with "Best regards, Leonard" (frederick.stone@harmonygames.co/1842283406259093714). Robert is short and casual ("Didn't really practice, added new items and made levels instead =/", C096HFA5Z8W/1757400808.661529). Arthur is terse ("I think 2", C096HFA5Z8W/1758207375.664029). Lengths and hours from conventions.json (`slack.length_chars_by_channel_type` private 40–120 p50; `slack.per_person_hours_and_style` Leonard 15–04 UTC; `gmail.internal_subject_len_chars`; `linear.title_prefixes_by_team` ZOM untitled-prefix; `gcal.duration_min` 45). Seeded hours: Slack 17:40Z, 18:00Z, 16:06Z, 16:25Z, 19:15Z, 23:20Z, 23:48Z; Trello 04:20Z and 17:05–17:30Z; mail 09:40Z (UK partner) to 22:30Z.

## 1.D Keyword

| Term | Hits / pointer | Note |
|---|---|---|
| "Sciplay" | slack C096HFA5Z8W/1757716998.377299 (root), gsheets f_48247af79428823c3cac92 row 81, rev6 seeded reply C07C2866011/1759248360.377105 | the reply is under Leonard's speedrun root C07C2866011/1759196326.309469, not under a SciPlay root |
| "Hiro" | gmail frederick.stone@harmonygames.co/1842278425320449096 (Sep 3), gsheets f_48247af79428823c3cac92 row 47, contacts e3a91c07d5b48f26a0c7e314 | the pass mail frederick.stone@harmonygames.co/1844318935449600041 does not contain it |
| "Brightwater" | NEW TERM — introduced in b72f0d6e19c3a84e5d21f9a0 and frederick.stone@harmonygames.co/1844276782694400053 (Ilse's reply), reached via evt_2f86b0d4c9e17a35b64e0d |
| "Ilse Marrow" | NEW TERM — introduced in evt_2f86b0d4c9e17a35b64e0d (title), frederick.stone@harmonygames.co/1844276782694400053, b72f0d6e19c3a84e5d21f9a0 |
| "Edith Vane" | NEW TERM — introduced in frederick.stone@harmonygames.co/1844318935449600041 (signature), e3a91c07d5b48f26a0c7e314 |
| "Paul Heydon" / "Anton Bernstein" | gsheets f_48247af79428823c3cac92 (list only, 0 Gmail hits in the census); seeded C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e | |
| "Anton" (rev6) | seeded D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218, C07C2866011/1758303600.418207 | a Slack search for "Anton" returns the DM lines and the post |
| "send list" | NEW TERM — introduced in f_3b9e61c04d7a52e8f1a6c2 (Q4) and f_8d2c47a91e05b3f6d7c418 (Q3 decoy), reached via the hub frederick.stone@harmonygames.co/1844724419788800011 |
| "Keep warm" | NEW TERM — introduced in 68c64270d660c977c4696986 (card 68c5a49e8491a9d7faf869d0) |
| "Play internal" | slack C096HFA5Z8W/1758677722.184129 (Arthur: add by email), C07C2866011/1758558621.032499 (Arthur: Play internal test link), linear ZOM-567 comment lc_b549f3057640a5eb08f7581e | |
| "investor tester list" | NEW TERM — introduced in lc_b549f3057640a5eb08f7581e (ZOM-567, rev6); rev12: Arthur's root post C0880U9751A/1759274400.518306 uses the same words ("the investor tester list I made in the Play console") |
| "Completed: Complete with docusign" | 84 base notices from SVC_1302 (leonard@harmonygames.co_1774464522151433079.json); seeded frederick.stone@harmonygames.co/1844354293432320031 | |

Census with positive control (learnings §35): a full `grep -r -F` over `Universe_SynthCut/SynthCut_HarmonyGames_Gmail` found "Grishin Robotics" (control) in 00001934.json and 0 files for Paul Heydon, Anton Bernstein; "Kestrel" in 3 files (rejected); PERSON_9xxx tokens: 0 uses in 386,054 files (scratch scan). Gmail by name (`grep -r -l -F` over the whole Gmail export): Edith Vane, Ilse Marrow, Brightwater 0 files, control "Grishin Robotics" found (00001934.json). Non-Gmail services: Edith Vane, Ilse Marrow, Brightwater 0 hits (gsheets/gdrive/gdocs/gslides/gcal/trello/linear/contacts/slack/confluence data scanned in Python; control "Grishin Robotics" found in gsheets/gdrive/gdocs/gslides data.json).

## 1.E Persona reach

Load-bearing ids written to `Working_Files/plan/lb_ids.txt`; output verbatim:

```
{{CHECKSQL}}
```

Scoped load-bearing records (all Frederick's copies or files shared with him):
- frederick.stone@harmonygames.co/1844724419788800011 — hub thread in his mailbox (INBOX) LB
- frederick.stone@harmonygames.co/1844354293432320031 — DocuSign Completed (Anton), to Frederick LB
- frederick.stone@harmonygames.co/1844610859008000037 — Leonard's nudge to Paul, cc Frederick LB; rev11: Paul's reply in this thread goes to Leonard only, so Frederick's copy ends with the nudge
- D05S58U4SAK/1759251900.863415 — rev12: Leonard in his 1:1 DM with Frederick: "Paul's out, he wrote me this morning that he can't put money in this year after all" LB (Frederick is a member of the DM)
- lc_4369758f577612cdb63b3457 and lc_5e2ff140afff06e3a78e2fe1 — rev12: ZOM-567 comments logging NCsoft (Sep 22) and Brightwater (Sep 26) on TestFlight and the Play internal track (Linear is unscoped)
- frederick.stone@harmonygames.co/1844318935449600041 — Edith Vane's pass, cc Frederick LB
- evt_7d3e19b04a6c25f8e1b9a0 — Hiro pitch call (Tue Sep 23) on Frederick's calendar LB
- frederick.stone@harmonygames.co/1844294398771200045 — Ryo-san's tester addresses and Leonard's "invites are out" reply, cc Frederick LB
- frederick.stone@harmonygames.co/1844276782694400053 — Brightwater follow-up and Ilse's reply, cc Frederick LB
- f_3b9e61c04d7a52e8f1a6c2 — template shared with Frederick (reader) LB
- d_5e8a1c3f9b07d2e64a1b93 — Board folder owned by Frederick LB
- evt_2f86b0d4c9e17a35b64e0d — Brightwater call on Frederick's calendar LB
- C096HFA5Z8W — #bridge-pitch, Frederick a member LB
- C07C2866011 — #executives, Frederick a member LB; rev6 reply C07C2866011/1759248360.377105 under C07C2866011/1759196326.309469
- D05S58U4SAK — Frederick's DM with Leonard (im member) LB; rev6 lines D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218
- C0880U9751A — #zombie-match3d, Frederick a member LB; rev6 post C0880U9751A/1759274400.518306 and reply C0880U9751A/1759276080.094417
- Unscoped (visible to all): ZOM-567, 68c64270d660c977c4696986, e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8.

## 1.F Collision

- Minted ids checked: Slack ts C07C2866011/1758303600.418207, C07C2866011/1759168800.117903 and the rev6 ts C07C2866011/1759248360.377105, D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218, C0880U9751A/1759274400.518306, C0880U9751A/1759276080.094417 absent from the month files (`hg.py search search slack <ts>`: 0 hits each; 1759248300 was rejected for a same-second message in D07GJJBFHA5); ZOM-567 absent (max ZOM 566); f_/d_/evt_/24-hex ids (f_3b9e61c04d7a52e8f1a6c2, f_8d2c47a91e05b3f6d7c418, f_c61a0e93b7d24f58a2e917, d_5e8a1c3f9b07d2e64a1b93, f_a47d0e2c95b18f63e2c0d5, f_6e1d93a0c4b72f85d39a0e, evt_2f86b0d4c9e17a35b64e0d, evt_9c41e7a2d05b38f6e1a7c4, evt_7d3e19b04a6c25f8e1b9a0, e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8) absent from gdrive/gdocs/gsheets/gslides/gcal/contacts data (Python containment scan with control f_48247af79428823c3cac92 found); base_check Check A (identifier uniqueness over the full collections) PASS.
- Header tokens: PERSON_9901–9904_EMAIL unused anywhere (0 of 386,054 files); existing tokens reused only for their own people (PERSON_5282 Hiro Investment Director, PERSON_3242 Karthic of T-Accelerate per frederick.stone@harmonygames.co/1843625920612854647, Dentsu PERSON_2581/5584/5221, SVC_1302 DocuSign).
- Body tokens: none minted ([IDENTIFIER_99011] in the DocuSign link is a new link placeholder in the base's style; no identity).

## Record ledger

| # | Table | Id | Manifest element | Carrier | Discovery role |
|---|---|---|---|---|---|
{{LEDGER}}

## Findability and discovery-order proofs

- Hub (A1) frederick.stone@harmonygames.co/1844724419788800011 — query "send list" / "Q4 investor update" via gmail search; first link (prompt names it).
- Send-list doc H1 f_3b9e61c04d7a52e8f1a6c2 — query "send list" via gdocs/drive search; competing hit the Q3 (July) decoy f_8d2c47a91e05b3f6d7c418 (same words; dated by its body "for the July update"). Leonard's signed note (K17) C07C2866011/1758911700.336170 is named by the doc and found by a Slack search for "DocuSign" or "new investor".
- Card rule H2 68c64270d660c977c4696986 on 68c5a49e8491a9d7faf869d0 — query "Existing Investor Update" via trello search returns the card; the rule is in comments (trello_get_comments); decoy 663ea0fc3f231e879cefd5e8 "Investor Update".
- CORR C07C2866011/1759248360.377105 (rev6) — claim met first: the SciPlay thread frederick.stone@harmonygames.co/1842285743246816270 ("We'll continue to play and let you know"); overturned by Robert's reply under Leonard's speedrun post C07C2866011/1759196326.309469; met first because a firm-name mail search hits the thread; channel history omits replies; found by a Slack search for "Sciplay" or by opening the replied thread.
- DONE1 (rev12) C07C2866011/1758303600.418207 met first (returned by the SAFE and DocuSign searches; no replies), Leonard's sheet f_6e1d93a0c4b72f85d39a0e repeats it and the Sep 29 nudge frederick.stone@harmonygames.co/1844610859008000037 shows only an unsigned SAFE; overturned by Leonard's Sep 30 message in his 1:1 DM with Frederick, D05S58U4SAK/1759251900.863415 ("Paul's out"); found by reading the DM (newest message on Sep 30) or a Slack search for "Paul"; not by "SAFE", "docusign", "signed", "counts" or "angel".
- INPUT (rev6): $40K in C07C2866011/1758303600.418207 and f_6e1d93a0c4b72f85d39a0e; overturned by Leonard's DM D05S58U4SAK/1758731100.281734 (Anton down to 25, SAFE re-sent at 25) and D05S58U4SAK/1758914100.640218 (signed the 25 one); found by a Slack search for "Anton" or by reading the DM.
- DONE2 (rev12): ZOM-567 (both tracks logged for T-Accelerate lc_94eb35d962cfbdd31e1bd496, NCsoft lc_4369758f577612cdb63b3457, Brightwater lc_5e2ff140afff06e3a78e2fe1 and Dentsu lc_b549f3057640a5eb08f7581e) and frederick.stone@harmonygames.co/1844294398771200045 ("Invites … are out to all three") met first; overturned for all four by Arthur's Sep 30 root post C0880U9751A/1759274400.518306 in #zombie-match3d (the investor tester list in the Play console never got attached to the internal track, so nobody on it has android yet: Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater; iOS fine for all of them) with Leonard's answer C0880U9751A/1759276080.094417; Arthur attaches the list with his Oct 1 push; found by a Slack search for "tester", "android", "Play" or a firm name (Dentsu, Karthic, NCsoft, Brightwater); not by "testflight" or "ZOM-567".
- ALIAS: list row "no response as of 09/11" (f_48247af79428823c3cac92) met first; overturned by frederick.stone@harmonygames.co/1844318935449600041 ("Thanks again for the session on Tuesday") mapped through e3a91c07d5b48f26a0c7e314, the cc of PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096) and the Tue Sep 23 call evt_7d3e19b04a6c25f8e1b9a0 (PERSON_5487, the To of the Sep 3 Hiro thread, and Edith as guests). The call also makes Hiro a pass after a pitch call, which the keep-warm rule 68c64270d660c977c4696986 needs.
- FILT: list read first; Homa via evt_89381fe5a15b802c5652a9 + "HOMA" in frederick.stone@harmonygames.co/1843169166284025277; Brightwater via evt_2f86b0d4c9e17a35b64e0d + b72f0d6e19c3a84e5d21f9a0.
- Q4 send rule (rev9) 68db03b86054eff7e8e92474 on 68c5a49e8491a9d7faf869d0: trello_get_comments on the card returns it beside the Sep 13 Keep warm rule; persona_view trello "F/up" finds it (brief §5a F42).
- DUP (rev9): the To Do list holds Leonard's open card 68c99e98737744bd966aed24 "F/up with Anel after the engine deep dive" (trello "F/up with Anel", F43); a board search for "NCsoft" returns nothing; the 2025 list f_48247af79428823c3cac92 maps Anel Ceman to NCsoft (persona_view gsheets "Anel": the list is a visible hit with snippet "Anel Ceman", F44).
- BOOKED (rev9): Fred's calendar after Sep 30 holds the base Dentsu meeting evt_3671b9a924ccba550e51fa (Wed Oct 1; gcal "Dentsu" 2 visible hits, F46) and the seeded "Michael Cheung and Leonard Hayes" call evt_6b2e94d0c17a3f58e9d2b1 (Wed Oct 8; gcal "Michael Cheung", F45), tied to Makers Fund only by the 2025 list's Partner column (gsheets "Michael Cheung", F47); every rev8 baseline run listed only Sep 3 - Oct 1.

## Self-validation

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | — | every deciding fact persona-readable (1.E, check-sql PASS) |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS | text dates agree: Leonard's "not the 40" (D05S58U4SAK/1758731100.281734, Sep 24) after the Sep 19 post (C07C2866011/1758303600.418207) and before the Sep 26 Completed notice; Robert's reply "this morning" at 16:06Z = 9:06am PT Sep 30; Arthur's post (23:20Z) after the ZOM-567 comments (18:40Z) and before the seed bound; Arthur's "tomorrow's build" = Oct 1, after the as-of (his base Oct 1 01:50Z build-size note follows); ZOM-567 created after ZOM-566 |
| Cross-service Referential | base_check Check A PASS | same amounts per service ($50K Paul in C07C2866011/1758303600.418207 and f_6e1d93a0c4b72f85d39a0e) |
| Quantitative | reply counters updated (rev6: 99aa913348bb05e6eda8daa06d37fc2a; the seeded root 3cddf83c394676d8b72c0c20ed58f520 carries reply_count 1) | no figure quoted against a base row |
| State / Lifecycle | Linear Todo without stamps (ZOM-567) | ZOM-567 "added" vs Arthur's later post is a dated human claim overturned later (intended); the ticket stays Todo while the Play list is not attached |
| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A) |
| Semantic / Category | — | titles match content (f_3b9e61c04d7a52e8f1a6c2, f_a47d0e2c95b18f63e2c0d5, d_5e8a1c3f9b07d2e64a1b93) |
| Other | — | voice per 1.C; no record states a conclusion or total |

## Integrations and companions

| Service | INT id | Companion | Decision |
|---|---|---|---|
| gcal | INT-11 | invitation mails | seeded: Brightwater call and Hiro call (Frederick, Robert, Arthur each) and the Oct 6 review (Frederick) |
| linear | INT-03, INT-04, INT-05 | linear[bot] PR comment / Slack DM / mail digest | none: ZOM-567 has no PR; Arthur assigns himself (no notification to Frederick) |
| gdrive | INT-13 | Drive Slack app share DM | none: shares predate Slack DM pattern for these docs (base shares in Frederick's view carry no DM for Leonard's docs, e.g. f_17e6175e84e745f92b3415) |
| slack | INT-22 | Slack email notifications | none: no @mention in the seeded posts (rev6 posts name Leonard and Karthic in plain text) |
| trello | INT-21 | no Trello→Slack integration | none |
| gmail, gdocs, gsheets, gslides, contacts | not integration sources | — | none |

## Touched-data census and coherence hazards

Touched data: the hub and its copies; the Q4 send-list doc and the Q3 decoy; the Q4 2025 investor update folder and README; the draft Q4 update deck; the angels sheet; #bridge-pitch Sep (C096HFA5Z8W) and #executives Sep (C07C2866011, rev6 root C07C2866011/1759196326.309469 whose counters the SQL updates); Frederick's DM with Leonard (D05S58U4SAK, Sep); #zombie-match3d Sep 30 (C0880U9751A); every cc'd investor thread (frederick.stone@harmonygames.co/1842285743246816270, frederick.stone@harmonygames.co/1842277743427687737, frederick.stone@harmonygames.co/1842278425320449096, frederick.stone@harmonygames.co/1842283406259093714, frederick.stone@harmonygames.co/1843473831194478743, frederick.stone@harmonygames.co/1832208184829815962, frederick.stone@harmonygames.co/1843547312959065138); calendar Sep 3–30 (evt_89381fe5a15b802c5652a9); the list f_48247af79428823c3cac92; cards 68c5a49e8491a9d7faf869d0 and 68d8193cf451863621c88a2a; ZOM-567; three contacts.

Hazards from coherence_hazards.json:
- temporal: T03 none in scope — the Speedrun forward frederick.stone@harmonygames.co/1844748127814183717 (Oct 1 03:21Z) is after the seed bound; a16z is never graded and the rev4 template settles it (an accelerator decision is not a bridge answer; In talks) (both statuses accepted).
- semantic: S04 (Frederick's GitHub "Ryan") avoided; no GitHub record touched (github none in scope).
- referential: R08 (invitation mails vs calendar) — every seeded event has its invitation copies (evt_2f86b0d4c9e17a35b64e0d, evt_7d3e19b04a6c25f8e1b9a0, evt_9c41e7a2d05b38f6e1a7c4).
- quantitative: Q01/Q03 — rev6: the seeded reply's root 99aa913348bb05e6eda8daa06d37fc2a (C07C2866011/1759196326.309469) gets reply_count 1, reply_users_count 1, latest_reply 1759248360.377105 (companion UPDATE); the rev5 update on 73c2247f4a31f32d10b3068ecd1d13ac is gone with its reply.
- state/lifecycle: L08 — ZOM-567 (Arthur, active_sep_2025_quiet_in_oct) is a Sep 30 ticket; Arthur's same-day post C0880U9751A/1759274400.518306 explains why it stays open (the Play list still needs attaching); no acknowledgement required (new record, not a hazard example).
- identifier/format: I03 — seeded files use the roster address frederick.stone@harmonygames.co (not the frederick@ alias); I14 — the list f_48247af79428823c3cac92 is Resource-owned, read only.

Known data issues (references/known_data_issues/synthcut.md, read at design per learnings §44, checked against the touched list f_48247af79428823c3cac92 and threads; no load-bearing fact, trap or graded slot rests on a card's "Don't grade" value):
- SC-33 (watch, investor sheet lists Acterra twice): touched by V1 (register size). Relied-on side: the incorporated template rule f_3b9e61c04d7a52e8f1a6c2 ("one row per name on the 2025 game investor list, angels included … a repeated name is still one row"), which counts Acterra (rows 71/86), Progression Fund (22/23) and BITKRAFT Ventures (32/33) once each in f_48247af79428823c3cac92; "Treo/Treeo" is a Slack spelling (C096HFA5Z8W/1756941551.539229), not a list duplicate. No raw sheet count is graded.
- SC-34 (row 82 labeled Superplay, contents Supercell): row 82's status is never sampled; it is one register row under either name (f_48247af79428823c3cac92).
- SC-9 (Play Ventures rejected vs no reply): never graded; rev4 settles it with Leonard's Sep 25 correction C096HFA5Z8W/1758817200.730591 (the Sep 15 no C096HFA5Z8W/1757955553.793529 was their reply to Griffin, which is why he wrote "they didn't respond" on Sep 23, C096HFA5Z8W/1758671737.632949): Passed.
- SC-10 (LVP meeting date Sep 7 vs Sep 9): no date graded; LVP's status comes from its own thread frederick.stone@harmonygames.co/1842277743427687737; the call is evt_e59dc0a675d0c407b79acf (Sep 9).
- SC-40 (July board date 14 vs 16): the seeded July template says "for the Jul 16 board" (f_8d2c47a91e05b3f6d7c418), the card's safer value; not graded.
- SC-49 (founder count, Frederick's role): no founder count or founder status is graded; the role review rests on activity (evt_bd61f3209523d19fdd6ba2, C096HFA5Z8W).
- SC-3 / SC-73 (runway, monthly burn): no cash, runway or burn figure is read or graded (snowflake.FINANCE untouched).
- SC-7 (channel membership): membership is used only for reach (C096HFA5Z8W, C07C2866011), never graded.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Paul Heydon "is in for $50K" (C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e) | rev12: Leonard's Sep 30 message in his 1:1 DM with Frederick D05S58U4SAK/1759251900.863415: Paul's out; nudge frederick.stone@harmonygames.co/1844610859008000037 (Sep 29) | founders post verbal yeses before docs; an angel can back out before signing; Leonard tells his co-founder directly | rev12: off the send list (a no for this round, no call) |
| Anton Bernstein $40K (same post, sheet) | rev6: Leonard's DM D05S58U4SAK/1758731100.281734 (Sep 24: down to 25, SAFE re-sent at 25), D05S58U4SAK/1758914100.640218 (Sep 26: signed the 25 one) and the Completed notice frederick.stone@harmonygames.co/1844354293432320031 | angels trim checks; founders pass such news in DMs | rev7: New investor, $25,000 |
| T-Accelerate, NCsoft, Brightwater and Dentsu on both tracks (ZOM-567 lc_94eb35d962cfbdd31e1bd496, lc_4369758f577612cdb63b3457, lc_5e2ff140afff06e3a78e2fe1, lc_b549f3057640a5eb08f7581e; Leonard's "invites … out to all three" frederick.stone@harmonygames.co/1844294398771200045) | rev12: Arthur's root post C0880U9751A/1759274400.518306 (Sep 30): the investor tester list was never attached to the internal track, nobody on it has android yet, iOS fine; Arthur attaches it with the Oct 1 build; Leonard C0880U9751A/1759276080.094417: ping me when it's live | Play internal testing needs the tester email list attached to the track (base C096HFA5Z8W/1758677722.184129, Arthur: "I have to add them by email for google play to work") | all four iOS only |
| SciPlay "we'll continue to play" (frederick.stone@harmonygames.co/1842285743246816270, Sep 18) | rev6: Robert's reply C07C2866011/1759248360.377105 (Sep 30) under Leonard's speedrun post | investors pass by phone; a rejection thread collects them | Passed |
| Hiro "no response as of 09/11" (f_48247af79428823c3cac92) | frederick.stone@harmonygames.co/1844318935449600041 (Sep 26) + e3a91c07d5b48f26a0c7e314 | the list's Latest Status column stops at 09/11 | Passed |
| July template committed = verbal yes (f_8d2c47a91e05b3f6d7c418) | Oct 14 template (f_3b9e61c04d7a52e8f1a6c2) | per-board templates | signed SAFE only |
| Play Ventures "is no" (C096HFA5Z8W/1757955553.793529) then "they didn't respond" (C096HFA5Z8W/1758671737.632949) | Leonard's Sep 25 correction (C096HFA5Z8W/1758817200.730591): the no was their reply to Griffin | a no often reaches the lead investor first | Passed (rev4) |
| "Iamgaming (sent … less likely)" (C096HFA5Z8W/1757345124.546449) and the 1AM Gaming no (frederick.stone@harmonygames.co/1842278301421016623) vs the list's "March Gaming Fund" | Leonard's Sep 8 post (C096HFA5Z8W/1757365500.384216): 1AM Gaming is the March Gaming Fund row | firms rename | March Gaming Fund Passed (rev4) |
| Mattel listed under "Reached out to" (C096HFA5Z8W/1756941551.539229) | Leonard's Sep 26 post (C096HFA5Z8W/1758927000.205874): RFP/partnership only, not pitched the bridge | partnership talks run beside fundraising | Not contacted this round (rev4) |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Leonard's Q4 update email; the send list ask | frederick.stone@harmonygames.co/1844724419788800011 |

Never name in the prompt: the send-list doc's location or rules, the Existing Investor Update card's rule, Robert's thread reply, Leonard's DM, Arthur's #zombie-match3d post, ZOM-567, the DocuSign notices, Contacts, Brightwater, Homa, PXLite, any amount, status, count or firm. Destinations the prompt may name: the Q4 2025 investor update folder (d_5e8a1c3f9b07d2e64a1b93), the Existing Investor Update card, a reply on Leonard's email (frederick.stone@harmonygames.co/1844724419788800011). Deadline: before Monday's review (evt_9c41e7a2d05b38f6e1a7c4, Oct 6). Deliverable kinds: one Google Sheet, an email reply, Trello checklist items (by the card's rule, not by the prompt).

## Fact sheet

| Key | Value | Kind | Home / must appear in |
|---|---|---|---|
| Paul | out | name | c5657466a4af062ceef9f7c3285aeb74 (D05S58U4SAK/1759251900.863415) |
| Arthur's Play correction | Play console | name | 3cddf83c394676d8b72c0c20ed58f520 (C0880U9751A/1759274400.518306) |
| Anton Bernstein | 25 (thousand, as Leonard writes it) | amount | 99b22482ddd77dd01b451afb39014839 (D05S58U4SAK/1758731100.281734), f7261dd1b05eb2da3b81fe7d8cde2854 (D05S58U4SAK/1758914100.640218); superseded versions 4921f321db5d08f936aac24a6a1d2af8, f_6e1d93a0c4b72f85d39a0e |
| keep-warm rule | Keep warm | name | 68c64270d660c977c4696986 |

```
{{FACTCHECK}}
```

Solver totals (`solver/truth.json`, rev12): 79 names looked at; 25 on the send list (New investor 1: Anton Bernstein 25,000; In talks 7: GFR Fund none, Andreessen Horowitz none, Homa none, NCsoft iOS only, Brightwater Games Fund iOS only, Dentsu Ventures iOS only, T-accelerate iOS only; Awaiting reply 14; Keep warm 3: London Venture Partners, Hiro Capital, Sciplay); 54 off (5 email-only passes, Paul Heydon, 48 not contacted); Trello: 4 checklists with 25 items, 18 follow-up cards (everyone In talks or Awaiting reply except NCsoft, Dentsu Ventures and Makers Fund), 1 comment on 68c99e98737744bd966aed24 for NCsoft; no firm keeps an alternative reading.

## Facts for the human

| Locator | Base/seeded | Fact | Reach | Role |
|---|---|---|---|---|
| frederick.stone@harmonygames.co/1844724419788800011 | seeded | Leonard → Frederick, cc Robert, Arthur, 2025-09-30T21:05Z: the ask | Frederick's INBOX | authority (hub, anchor) |
| f_3b9e61c04d7a52e8f1a6c2 | seeded | Q4 investor update send-list doc (rev7): look at every 2025-list name plus off-list firms pitched on a call since Sep 3; groups as of end of Sep 30 PT: New investor (signed SAFE, per Leonard's #executives note; amount), In talks (call this round, no pass; unsigned angels with their amount; build access for firms), Awaiting reply, Keep warm (passed after a pitch call); everyone else off; Passed = they've told us no for this round (a no sent to Griffin counts); accelerator decisions are not bridge answers; build access = whether they can get the current internal build (Arthur tracks the adds) | shared reader | authority H1 |
| f_8d2c47a91e05b3f6d7c418 | seeded | Q3 (July) send list: new investor = anyone who said yes with an amount | shared reader | decoy (superseded) |
| d_5e8a1c3f9b07d2e64a1b93 | seeded | Q4 2025 investor update folder, owner Frederick; README f_c61a0e93b7d24f58a2e917 names the file "Q4 update - send list" | owner | write target |
| C07C2866011/1758911700.336170 | seeded (rev7) | Leonard 2025-09-26T18:35Z in #executives: someone only counts as a new investor once the DocuSign Completed notice is in | member | rule (K17) |
| f_a47d0e2c95b18f63e2c0d5 | seeded (rev7 content) | draft Q4 update deck: the bridge slide says what each group gets; firms in talks get the build links they can use | shared reader | connecting (K11) |
| D05S58U4SAK/1758731100.281734 | seeded (rev6) | Leonard → Frederick DM 2025-09-24T16:25Z: Anton can only do 25, not the 40; voiding his DocuSign and sending a new SAFE at 25 | DM member | overturning evidence (INPUT) |
| D05S58U4SAK/1758914100.640218 | seeded (rev6) | Leonard → Frederick DM 2025-09-26T19:15Z: Anton signed the 25 one | DM member | settling (signed amount) |
| frederick.stone@harmonygames.co/1844354293432320031 | seeded | DocuSign Completed: SAFE - Anton Bernstein, 2025-09-26T19:02Z | to Frederick | evidence |
| frederick.stone@harmonygames.co/1844610859008000037 | seeded | Leonard → Paul 2025-09-29T15:00Z: SAFE still with you | cc | context (Paul unsigned on Sep 29) |
| D05S58U4SAK/1759251900.863415 | seeded (rev12) | Leonard 2025-09-30T17:05Z (10:05am PT), in his 1:1 DM with Frederick: "Paul's out, he wrote me this morning that he can't put money in this year after all" | member | overturning evidence (DONE1) |
| leonard.hayes@harmonygames.co/<CAH2UMEfxg69PBVI7YxuPTO9uXYBOEfsCOfTEzpB@mail.gmail.com> | seeded (rev11) | Paul → Leonard only, 2025-09-30T14:55Z, in Leonard's copy of the nudge thread: has to back out, can't put money in this year | not visible (Leonard's mailbox) | source of Leonard's relay; not needed by Frederick · DENIAL-INTENDED: Paul wrote Leonard only, and Frederick learns it from Leonard's #executives reply · alternate_evidence_ids: the rev11 reply under the angel post (moved to D05S58U4SAK/1759251900.863415 in rev12) |
| lc_4369758f577612cdb63b3457 | seeded (rev12) | ZOM-567 comment 2025-09-30T17:45Z: NCsoft (2 accounts from Anel's team, after the Sep 19 call): TestFlight and Play internal track both added Sep 22 | unscoped | claim met first (done source) |
| lc_5e2ff140afff06e3a78e2fe1 | seeded (rev12) | ZOM-567 comment 2025-09-30T18:05Z: Brightwater (Ilse Marrow): TestFlight and Play internal track both added Sep 26 | unscoped | claim met first (done source) |
| frederick.stone@harmonygames.co/1844318935449600041 | seeded | Edith Vane 2025-09-26T09:40Z: thanks for Tuesday's session, pass on the bridge (no firm name), cc PERSON_5282 | cc | overturning evidence (alias) |
| evt_7d3e19b04a6c25f8e1b9a0 | seeded | "PERSON_5487_NAME and Leonard Hayes" 2025-09-23T16:00–16:45Z (guests: founders, PERSON_5487, Edith Vane); invitations 2025-09-19T18:30Z | Frederick's calendar + INBOX | evidence (Hiro pitched on a call) |
| frederick.stone@harmonygames.co/1844294398771200045 | seeded | Ryo-san (PERSON_5221) 2025-09-26T03:10Z: three tester addresses; Leonard's reply 17:20Z: invites out to all three | cc | claim met first |
| frederick.stone@harmonygames.co/1844276782694400053 | seeded | Brightwater follow-up 2025-09-25T22:30Z (deck to follow separately) + Ilse's reply 2025-09-26T15:05Z signed "Principal, Brightwater Games Fund" | cc | evidence (off-list firm) |
| evt_2f86b0d4c9e17a35b64e0d | seeded | "Ilse Marrow and Leonard Hayes" 2025-09-25T15:30–16:15Z | Frederick's calendar | evidence |
| evt_9c41e7a2d05b38f6e1a7c4 | seeded | Q4 update send list review, Oct 6 21:00Z (2:00pm PT, clear of the recurring POD and planning meetings) | Frederick's calendar | deadline |
| C07C2866011/1759248360.377105 | seeded (rev6) | Robert 2025-09-30T16:06Z, reply under Leonard's speedrun post C07C2866011/1759196326.309469: Sciplay's out too, D called him that morning, passing on this round | member | overturning evidence (CORR) |
| C0880U9751A/1759274400.518306 | seeded (rev6; root post again in rev12) | Arthur 2025-09-30T23:20Z (4:20pm PT), root post in #zombie-match3d (one reply): found a problem with investor android access: the investor tester list he made in the Play console never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says; iOS fine for all of them; he'll attach it with tomorrow's push | member | overturning evidence (DONE2) |
| C0880U9751A/1759276080.094417 | seeded (rev6) | Leonard 2025-09-30T23:48Z, reply under Arthur's post: ok thx, ping me when it's live so I can tell Karthic, Ryo-san and the others (rev12) | member | settling (Android not live by end of Sep 30) |
| ZOM-567 | seeded | Arthur's investor tester log (created 2025-09-30T17:10Z): T-Accelerate TestFlight and Play both added Sep 22 (lc_94eb35d962cfbdd31e1bd496); NCsoft both added Sep 22 (lc_4369758f577612cdb63b3457, rev12); Brightwater both added Sep 26 (lc_5e2ff140afff06e3a78e2fe1, rev12); Dentsu TestFlight and Play added Sep 26 (lc_b549f3057640a5eb08f7581e) | unscoped | claim met first (done source) |
| C07C2866011/1758303600.418207 | seeded | Leonard 2025-09-19T17:40Z: Paul $50K, Anton $40K "in" | member | claim met first |
| C07C2866011/1759168800.117903 | seeded | Arthur: just list who Leonard emailed | member | distractor |
| C096HFA5Z8W/1756942260.617302 | seeded | Leonard 2025-09-03T23:31Z: Treo VC pinged him on LinkedIn that morning; deck and blurb sent | member | settling (Treo contact date) |
| C096HFA5Z8W/1757365500.384216 | seeded | Leonard 2025-09-08T21:05Z: 1AM Gaming is the March Gaming Fund row, they passed | member | settling (F9) |
| C096HFA5Z8W/1757442000.492583 | seeded | Leonard 2025-09-09T18:20Z: pinged Initial Capital on LinkedIn about the bridge; they won't lead but might write a small check | member | settling (rev4 report fork F1) |
| a4c2e9f07b31d85e6c0f1b29 | seeded | Contact Ryo Ishikawa, Dentsu Ventures (games and AI investments), PERSON_5221_EMAIL | unscoped | connecting (Dentsu team = Dentsu Ventures row) |
| C096HFA5Z8W/1758817200.730591 | seeded | Leonard 2025-09-25T16:20Z: Play's Sep 15 no was their reply to Griffin; still their no | member | settling (F2, coherence) |
| C096HFA5Z8W/1758927000.205874 | seeded | Leonard 2025-09-26T22:50Z: since the kickoff Mattel has only been an RFP conversation, not pitched the bridge | member | settling (coherence) |
| f_6e1d93a0c4b72f85d39a0e | seeded | Bridge angels sheet (stale, Sep 20) | shared reader | claim met first |
| frederick.stone@harmonygames.co/1844623441920000059 | seeded | Robert: email the board directly (withdrawn by the hub) | to Frederick | distractor |
| frederick.stone@harmonygames.co/1842285743246816270 | base | SciPlay thread, last investor word Sep 18 | cc | claim met first |
| frederick.stone@harmonygames.co/1842277743427687737 | base | LVP pass Sep 25 (call Sep 9, evt_e59dc0a675d0c407b79acf) | cc | evidence (keep-warm) |
| frederick.stone@harmonygames.co/1843169166284025277 | base | Homa invitation ("HOMA") for evt_89381fe5a15b802c5652a9 | cc | evidence (off-list firm) |
| f_48247af79428823c3cac92 | base | 2025 game investor list, 80 rows / 77 firms, Latest Status as of 09/11; NCsoft partner Anel Ceman | shared | population; maps the Anel card (rev9) |
| 68db03b86054eff7e8e92474 | seeded (rev9) | Leonard 2025-09-29T22:10Z, comment on the Existing Investor Update card: besides Keep warm, a checklist per other group, one item per firm or angel; an "F/up with" card in To Do for everyone In talks or Awaiting reply; comment on an existing To Do card instead; none for anyone with a call or meeting on Fred's calendar after Sep 30 | unscoped | rule (H2, K18) |
| 68c99e98737744bd966aed24 | seeded (rev9) | Leonard's open To Do card "F/up with Anel after the engine deep dive" (idShort 456, created 2025-09-16T17:30Z, createCard 68c99e98647b81be91f207f2) | unscoped | existing card for NCsoft (DUP) |
| evt_6b2e94d0c17a3f58e9d2b1 | seeded (rev9) | "Michael Cheung and Leonard Hayes", 2025-10-08T16:00–16:45Z (Wed 9:00am PT), booked 2025-09-29T17:40Z; copies for Leonard, Robert, Arthur; invitation frederick.stone@harmonygames.co/1844620925337600069; Michael Cheung = Makers Fund partner (f_48247af79428823c3cac92) | Frederick's calendar + INBOX | booked call, no card for Makers (BOOKED) |
| evt_3671b9a924ccba550e51fa | base | Harmony Games & Dentsu, 2025-10-01T20:30Z (Wed 1:30pm PT), created 2025-10-01T00:02Z (Sep 30 5:02pm PT); second copy evt_eeca6fc7670fe1acd94440 | Frederick's calendar | booked meeting, no card (BOOKED) |

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

### Platform /injection review of rev3

The review of rev3 (`Platform_Report/injection_report3`, copied to `run_forensics/rev3/design/platform_injection_report_PASS.md`; sha256 952e12a9ad7a6b88, 143 INSERT + 11 UPDATE) returned FINAL VERDICT: PASS / COMPLETE and recorded rev2's advisories 2–4 as resolved and advisory 1 as narrowed. Remaining advisories and dispositions:

| Advisory | Finding | Disposition | Evidence |
|---|---|---|---|
| 1 | slides_pages.notes (all NULL), slides_page_elements.table_json (all NULL) / ordinal and linear_comments.sequence are outside the eval's schema snapshot; no task content depends on them | kept: the platform's schema export (universe_schema_live.json, 2026-10-04) lists all four, and the completed Julia, Frederick card-spend and Douglas injections wrote the same columns and loaded (their baselines read the injected rows); dropping them would only add another /injection cycle | f_a47d0e2c95b18f63e2c0d5, ZOM-567 |
| 2 | T-Accelerate Play track added Sep 23 vs the link shared Sep 22 | kept: consistent (link shared Sep 22, tester added Sep 23), as the reviewer states | frederick.stone@harmonygames.co/1842283406259093714 |

Rev3 was the SQL for the first /prompt review (FAIL, below); rev4 replaces it. Investor-list visibility (left to /prompt by the reviewer): f_48247af79428823c3cac92 is shared with frederick.stone@harmonygames.co (persona_view can-see YES, section 1.E).

### Platform /prompt review of rev3 and the rev4 changes

The platform `/prompt` review of rev3 (`Platform_Report/peompt_report1`, copied to `run_forensics/rev3/design/platform_prompt_report_FAIL.md`; prompt sha256 cecfad824fd8, SQL 952e12a9ad7a) scored the prompt 5 on every prompt dimension and FAIL 2 overall: Unique Ground Truth 2 (forks F1–F9) and Cross-Service Coherence 2 (Play Ventures contradiction; Mattel's Leonard-only exchange). The prompt is unchanged; every fork is settled in the records:

| Platform finding | Rev4 change | Record |
|---|---|---|
| F1 Homa in scope | template: a firm pitched the bridge counts even when co-dev or publishing was also on the table (Leonard's Sep 17 mail pitched extension funding) | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1843552279434086285 |
| F2 Play Ventures; coherence | Leonard's Sep 25 correction; template counts a no sent to Griffin | C096HFA5Z8W/1758817200.730591 |
| F3 connector outreach | template: outreach by anyone introducing us counts as ours | f_3b9e61c04d7a52e8f1a6c2 |
| F4 a16z | template: an accelerator decision is not a bridge answer; the interview is a call | f_3b9e61c04d7a52e8f1a6c2, evt_e802a3583ee79ff6087f76 |
| F5 Paul soft-circled | template: a yes one of us wrote down counts | f_3b9e61c04d7a52e8f1a6c2 |
| F6 angels' bucket | template: angels who said yes are In talks, Build access blank | f_3b9e61c04d7a52e8f1a6c2 |
| F7/F8 last two-way contact | column dropped (template, slide 9, gradable surface) | f_3b9e61c04d7a52e8f1a6c2, f_a47d0e2c95b18f63e2c0d5 |
| F9 1AM Gaming | Leonard's Sep 8 post ties it to March Gaming Fund | C096HFA5Z8W/1757365500.384216 |
| Mattel hidden exchange (coherence) | Leonard's Sep 26 post; template: only bridge outreach counts | C096HFA5Z8W/1758927000.205874 |
| unflagged solver two-reading rows (BITKRAFT, Superplay, Treo VC, Transcend Fund, Acterra, Index Ventures) | template: only this round counts; Awaiting reply holds even if they wrote back; an advisor's read is not a firm's answer | f_3b9e61c04d7a52e8f1a6c2 |
| keep-warm scope (earlier-round calls) | comment: "pitched them on a call or meeting this round" | 68c64270d660c977c4696986 |
| Leonard-only calendar calls (minor; the Sep 29 "Turkish VC" call) | template: a call counts only when it's on Fred's calendar, also for In talks | f_3b9e61c04d7a52e8f1a6c2 |
| author blind sweep of rev4: the reply's firm count (79 / 77 / 74) | Board Deck comment: "how many firms are on it (every row, angels included)"; slide 9: "Firms on Fred's sheet" | 68d81f30a6c94e2b7d05e1f4, f_a47d0e2c95b18f63e2c0d5 |
| author blind sweep: row 69 [PERSON_NAME_5402] ("They don't do bridge") and Initial Capital ("would potentially write a small check") | template: Latest Status notes count as written; a note that they passed or don't do bridges is their no | f_3b9e61c04d7a52e8f1a6c2, f_48247af79428823c3cac92 |
| author blind sweep: Treo VC contact date (Sep 2 warm-up vs kickoff) | Leonard's Sep 3 post; template: the kickoff day counts | C096HFA5Z8W/1756942260.617302 |
| author blind sweep: the Sep 5 SVB catch-up, Homa's co-dev framing, Brightwater's pitch | template excludes banks and counts an investment alongside a co-dev deal; Brightwater's follow-up names the bridge round | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1844276782694400053 |
| author blind sweep: Dentsu build-access format; Anton's committed amount | template: write iOS only / Android only / iOS and Android / none; the latest amount the investor gave applies to both money columns | f_3b9e61c04d7a52e8f1a6c2 |

Rev4 (sha256 2e2428bc5e49, 147 INSERT + 11 UPDATE) adds four #bridge-pitch posts and rewrites five seeded texts (template, keep-warm comment, Board Deck comment, slide 9, Brightwater follow-up); no id, timestamp or other row changes. An author-run blind fork sweep (a fresh agent with only Frederick-visible records and the template) classified all 79 rows independently; after the rev4 fixes its table matches solver/truth.json row for row (Passed 8, In talks 9, Awaiting reply 14, Not contacted 48; keep warm LVP, Sciplay, Hiro Capital; reply 79 / $25,000 / $50,000), with only weak residuals (Initial Capital's note, Dentsu = Dentsu Ventures, the SVB event title). The solver now gives one status per firm (`accepted_status` empty for all 79 keys) and reproduces rev3's truth on the rev3 SQL (contract.regression PASS). It needs `/injection` again, then `/prompt`.

### Platform /prompt review of rev4 and the rev5 changes

The platform `/injection` review of rev4 (`Platform_Report/injection_report4`, SQL 2e2428bc5e49) returned PASS / COMPLETE. The `/prompt` review of rev4 (`Platform_Report/prompt_report2`, prompt sha256 cecfad824fd8) settled every rev3 fork and scored the prompt 5 on every prompt dimension; it failed on two items only:

| Platform finding | Severity | Rev5 change | Record |
|---|---|---|---|
| F1 Initial Capital: the list's 09/11 note ("They won't lead - would potentially write a small check") implies contact, but no Frederick-visible record showed our outreach | Major, UGT 2 | Leonard's Sep 9 post: he pinged Initial Capital on LinkedIn about the bridge and they wrote back that they won't lead but might write a small check (no amount, so not soft-circled): Awaiting reply | C096HFA5Z8W/1757442000.492583 |
| DR2 tester records: ZOM-567 said T-Accelerate's Play add was Sep 23 and Arthur lacked Play console rights, while base #executives (Sep 22 16:30Z) shows Arthur sending both invites | Minor, Cross-Service Coherence 3 | T-Accelerate comment: both tracks added Sep 22 (Karthic), unsupported install claim dropped; Dentsu comment: TestFlight added Sep 26, Play not added because their work addresses aren't Google accounts (Arthur's base Sep 23 "add them by email for google play to work"); description reworded as a dated log | lc_94eb35d962cfbdd31e1bd496, lc_b549f3057640a5eb08f7581e, ZOM-567 |
| author coherence sweep: the base Sep 30 a16z speedrun feedback also discusses the bridge | (pre-empted) | template: the program's decision and its feedback aren't their answer on the bridge; that has to come on the bridge thread or in #bridge-pitch (their bridge thread has only "Will review") | f_3b9e61c04d7a52e8f1a6c2, frederick.stone@harmonygames.co/1842277213140775733 |
| author coherence sweep: Dentsu team not tied to the list row; Brightwater promised a deck email that never came; deck agenda order differed from the slides | (pre-empted) | contact Ryo Ishikawa, Dentsu Ventures (PERSON_5221_EMAIL); follow-up no longer promises the email; agenda reordered | a4c2e9f07b31d85e6c0f1b29, frederick.stone@harmonygames.co/1844276782694400053, f_a47d0e2c95b18f63e2c0d5 |
| /injection rev4 advisory 1: the Mattel post overstated the history (Aug 26 email offered a small strategic investment) | advisory | post now reads "since the kickoff that's only been an RFP conversation, we haven't pitched them the bridge" | C096HFA5Z8W/1758927000.205874 |

Graded values are unchanged (Initial Capital was already Awaiting reply under the template rule; T-accelerate iOS and Android; Dentsu iOS only). Rev5 is sha256 3ba2b413458f, 149 INSERT + 11 UPDATE; it needs `/injection`, then `/prompt`.

### Platform Opus pre-check of rev5 and the rev6 changes

Rev5 passed the platform `/injection` (`Platform_Report/injection_report5`) and `/prompt` (`Platform_Report/prompt_report3`, every dimension 5). The platform Opus 5.5 pre-check run (`06_PreCheck_Trajectory/trajectory.json`, 107 tool calls) then solved every requirement, and `/hardness` returned FAIL, score 1, Too easy (`Platform_Report/hardness_report1`). Forensics are in `Working_Files/01a_Hardening_Report.md` (all seven rules LEAKED), and the decisions are in design section 15. Rev6 changes:

| Rev5 record or wording (how the run found it) | Rev6 change | Record |
|---|---|---|
| Anton's "SAFE amount" mail frederick.stone@harmonygames.co/1844162278195200023 (the run's Sep mailbox listing returned it, run call 40) | removed from Frederick's mailbox (Anton's mail now reaches Leonard only, as Leonard's copy); Leonard's DM to Frederick carries the change (Sep 24) and the signed amount (Sep 26) | D05S58U4SAK/1758731100.281734, D05S58U4SAK/1758914100.640218 |
| Robert's #bridge-pitch root C096HFA5Z8W/1759161600.226431 and reply C096HFA5Z8W/1759184040.552871 (the template named #bridge-pitch; the run's threads-only search returned the reply, run call 34) | removed (and the counter update on C096HFA5Z8W/1757716998.377299); Robert's reply under Leonard's speedrun post in #executives | C07C2866011/1759248360.377105 (root C07C2866011/1759196326.309469, counters updated) |
| ZOM-567 Dentsu caveat "Play internal track not added yet" (the done source carried its own gap, run call 94) | the Dentsu comment logs the Play add like T-Accelerate's; Arthur's later post says the investor tester list was never attached to the Play internal track, although ZOM-567 shows them as added; Arthur attaches it with the Oct 1 build | lc_b549f3057640a5eb08f7581e, C0880U9751A/1759274400.518306, C0880U9751A/1759276080.094417 |
| template resolver sentences (read at run call 11): the #bridge-pitch phone rule, "in writing", "check contacts and the earlier threads", "use the latest amount the investor gave us" | removed; Passed = "they've told us no for this round"; build access = "whether they can get the current internal build" | f_3b9e61c04d7a52e8f1a6c2 |

Seeded-vs-base coherence sweep of rev6 (an independent reviewer read every mailbox and channel; report in the author's scratchpad) and the fixes made:

| Finding | Base evidence | Rev6 fix | Record |
|---|---|---|---|
| Arthur said his Play console role could not change track testers | Arthur invites a colleague into Play Console on Sep 30 15:09Z (CD843DBC4C3E/1759244974.454399) and added Play internal testers himself in July (D06477JGUKT/1753708724.412369) | Arthur attaches the list "when I push tomorrow's build" (Oct 1, after the as-of); the post names ZOM-567 as showing them added; Leonard asks to be told when it's live | C0880U9751A/1759274400.518306, C0880U9751A/1759276080.094417 |
| "found why Karthic can't get the android build" had no record of Karthic reporting it | Karthic's thread ends with Leonard's Sep 22 recap (frederick.stone@harmonygames.co/1842283406259093714) | rev11 recorded Karthic's report in his thread; rev12 removes it again, and Arthur's root post no longer says why he looked ("found a problem with investor android access") | C0880U9751A/1759274400.518306 |
| Treo "pinged me on LinkedIn this morning" on Sep 3, but the inbound was logged on Sep 2 | D04UC0UEN2V/1756878703.235739 and C096HFA5Z8W/1756941551.539229 ("Treeo VC (inbound b2b AI, Leonard responded on linkedin)") | "pinged me again on LinkedIn this morning"; the deck still went out on Sep 3 | C096HFA5Z8W/1756942260.617302 |
| the Play Ventures correction ignored Robert's "discussing" relay | C096HFA5Z8W/1758760214.401689, C096HFA5Z8W/1758764726.605039 | adds "the \"discussing\" Robert heard via Applovin doesn't change that" | C096HFA5Z8W/1758817200.730591 |
| the template said only the Latest Status notes are from this round, but the list's comment column also has this-round notes | f_48247af79428823c3cac92 comments (Play, Mattel, Treo, T-accelerate, Sony) | "On the list, go only by the Latest Status notes (as of 09/11)" | f_3b9e61c04d7a52e8f1a6c2 |
| Arthur's invitation copies said PDT; his calendar is Eastern | his 20 base invitations say EDT, "Eastern Time - New York" | Arthur's copies of the Hiro and Brightwater invitations now say 12pm / 11:30am EDT, "Eastern Time - New York" | invitation mails in arthur.blake@harmonygames.co |
| the new Trello card's number 466 skipped ahead of the board's highest base card 455 | trello data.json, board 640643a3fd8f3ca308d9318e | idShort 456 | 68d8193cf451863621c88a2a |

The blind fork sweep of rev6 (Frederick-visible records and the template only, no author answers) classified all 79 rows and matched the solver row for row. It found one fork new to rev6: build access read from the ZOM-567 log versus Arthur's post. That fork is settled by naming ZOM-567 in Arthur's post. Its other forks (NCsoft, Homa, the keep-warm "email-only no's" wording, a16z, Index Ventures, the Turkish VC, Treo, General Catalyst, reply-all) are the rev4/rev5 settlements that passed the platform `/prompt` on rev5 unchanged.

### Platform /prompt review of rev6 and the rev7 job change

Rev6 passed the platform `/injection` (`Platform_Report/injection_report6`, SQL 848189443008). The platform `/prompt` (`Platform_Report/prompt_report4`) scored all 20 content dimensions 5, including Unique Ground Truth (30 forks, none open) and Cross-Service Coherence. It failed only on the new STEP 0.6 dataset-duplicate gate: meaning similarity 0.804 to another contributor's Frederick task on the Oct 14 board pre-read handoff. The fix had to be a different job. Rev7 keeps every trap record and changes the job to the bridge part of the Q4 investor update send list:
- the hub asks for the send list and a reply with how many firms and angels are in each group;
- the template becomes the send-list doc and the July template becomes the Q3 send-list decoy;
- the folder becomes "Q4 2025 investor update" with its README;
- the deck becomes the draft Q4 update;
- the Board Deck card is removed;
- Leonard's #executives note on what counts as signed is added (C07C2866011/1758911700.336170);
- Robert's mail and Arthur's aside now aim at the send list.

The prompt is new (sha256 b5ea6f0ff28c). Design section 17 lists every change. Values (rev12): 25 on the list (see Solver totals).

### Platform /prompt review of rev7 and the rev8 change

Rev7 passed the platform `/injection` (`Platform_Report/injection_report7`, SQL efe3cab14874). Its `/prompt` (`Platform_Report/prompt_report5`, prompt b5ea6f0ff28c) returned NON-FAIL, score 3. Dataset similarity passed at 0.762, under the 0.80 line, and every prompt dimension scored 5, including Unique Ground Truth (33 forks, none open). The one score below 5 was Cross-Service Coherence at 3. The base 2025 investor list (f_48247af79428823c3cac92, row No. 8, Latest Status) dates LVP's catch-up "09/07", a Sunday, while the calendar (evt_e59dc0a675d0c407b79acf), #bridge-pitch on Sep 8 ("meeting on Sep 9th") and Fred's Sep 12 mail all say Tue Sep 9 (known data issue SC-10). Rev8 follows the review's own minimum fix: one `UPDATE gsheets.sheets_sheets ... WHERE spreadsheet_id = 'f_48247af79428823c3cac92' AND sheet_id = 0` rewrites the base grid with only that cell changed to "09/09". Decoding the statement against the base grid shows 89 rows of the same shape and exactly one differing cell (row 8, column 13). The list keeps its base modified_time. This follows the precedent of the completed robert_winddown_closeout task, which shipped a full-grid sheets_sheets UPDATE and passed the platform `/injection`. Nothing graded changes, and neither do the prompt nor any other record.

Kept for the rev4 fork settlements (section 14 of the design): the speedrun rule and its tail, "as one of us wrote it down", the Griffin/advisor rule, the population and exclusion rules, and the Latest Status rule. Graded values: unchanged except T-accelerate build access (iOS and Android → iOS only). Rev6 was sha256 848189443008, 150 INSERT + 11 UPDATE (rev7 is 4895577edea8, 130 INSERT + 11 UPDATE). The prompt is unchanged (sha256 cecfad824fd8). Rev6 needs `/injection`, then `/prompt`, then a new Opus pre-check and `/hardness`.

### Rev8 baseline and the rev9 change

The six Opus 5.5 baseline runs of rev8 (SQL 4895577edea8, prompt b5ea6f0ff28c; `run_forensics/rev8/baseline/`) averaged 72.7 counted MCP calls (82, 60, 70, 72, 69, 83), under Long Horizon's 100. Runs 3 and 5 graded about 100%, and the horizon rule takes a 100% rollout's count when one exists. The estimated average pass was about 82%. Opus reads in bulk and writes the sheet in one call, so the one lever that is not padding is per-entry writes the job really needs.

Rev9 keeps the prompt and every graded sheet and reply value. Three things change:
- Hub sentence: "Then do what I put on the Existing Investor Update card in Trello."
- Leonard's Sep 29 card comment 68db03b86054eff7e8e92474 adds a checklist per other group (rev11: 25 items over four checklists) and an "F/up with" card in To Do for everyone In talks or Awaiting reply.
- Two outcomes are settled by new records:
  - NCsoft gets a comment on Leonard's open card 68c99e98737744bd966aed24 (DUP).
  - Dentsu (base Oct 1 meeting) and Makers Fund (seeded Oct 8 call evt_6b2e94d0c17a3f58e9d2b1) get no card (BOOKED).

A correct run makes 48 single-object Trello writes in rev11 (4 checklists, 25 items, 18 cards, 1 comment); the catalog has no batch write for check items or cards. Design section 18 has the counter-readings.

### Platform /hardness of rev9 and the rev10 change

/injection and /prompt passed on rev9 (a34c7de3). The Opus 5.5 pre-check made 135 tool calls, so the Trello writes did their job for the horizon. It met every requirement, and /hardness scored 1 (Too easy, FAIL; `run_forensics/rev9/platform/1a_hardness.md`). The run found the SciPlay reply by reading the #executives thread, found Arthur's correction because a Slack search for "tester" returned the root post, and read Paul's gap off Leonard's "still sitting with you" nudge.

Rev10 keeps the prompt, the truth (f3dd0b9de6e2d3f8) and every graded value. Two records change, following the reviewer's suggestions 1 and 2:
- Arthur's correction C0880U9751A/1759274400.518306 and Leonard's answer C0880U9751A/1759276080.094417 are now replies in the thread under Leonard's base post C0880U9751A/1759182908.627389 ("I just released 0.3.49 on IOS"; reply_count 2, reply_users_count 2, latest_reply 1759276080.094417). Arthur's text names Karthic, the 3 Dentsu folks, the Play console group, the internal track and the Linear log. It no longer says tester, TestFlight or ZOM-567.
- Paul's reply frederick.stone@harmonygames.co/<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com> (Sep 30 8:40am PT, to Leonard, cc Frederick; Leonard's copy too) in the nudge thread: "Done, signed it last night". No DocuSign Completed notice for Paul exists in any mailbox, so Leonard's #executives note C07C2866011/1758911700.336170 still makes Paul In talks at $50,000. Coherence: a SAFE completes only when Harmony countersigns, and Leonard is flying to LA on Oct 1; a signer's "signed it" coming before the Completed notice is ordinary.

SQL: 145 INSERT, 15 UPDATE (the release-post root counters and the two thread snippets are the new updates). Design section 19 has the run table and the counter-readings.

### Rev10 baseline and the rev11 change

/injection and /prompt passed on rev10 (c999829d), and /hardness scored NON-FAIL 3, PROCEED: the pre-check missed both build-access cells. The six baseline runs (`run_forensics/rev10/baseline/baseline_review.md`) averaged 133 counted calls (lowest 114) with 0 of 6 full passes, but runs 1, 3, 5 and 6 failed exactly the same values (SciPlay plus both build-access cells), so one failure signature covers 4 of 6 failing runs, and the spread of scores is about 0.04. Build access was missed 7 of 7 times, SciPlay 5 of 7, Paul's rev10 done claim 0 of 7.

Rev11 keeps the prompt and every value except Paul's:
- Paul backs out. His rev10 "signed it" reply is removed. He writes Leonard only (reply on the nudge thread without Frederick, Sep 30 7:55am PT), and Leonard relays it under his own Sep 19 angel post: the rev11 reply under the angel post (moved to D05S58U4SAK/1759251900.863415 in rev12), "Paul's out, he wrote me this morning that he can't put money in this year after all" (root reply_count 1, latest_reply 1759251900.863415). Under the send-list doc a no for this round with no call stays off, so Paul has no row, checklist item or card, and the reply's In talks count is 7 firms, 0 angels.
- T-Accelerate's correction moves into Karthic's own thread (frederick.stone@harmonygames.co/1842283406259093714, all four mailbox copies): Karthic reports at 10:20Z that the Android link doesn't work, and Arthur, cc'd on the thread since Sep 3, answers at 20:05Z (1:05pm PT) that the Play tester list the investor accounts are on was never attached to the internal test track, so nobody on it has the Android build yet; iOS is all set. Arthur's later #zombie-match3d reply now covers the 3 Dentsu folks ("either"), and Leonard's answer names Ryo-san only. Both cells stay iOS only.
- Coherence: Arthur's ZOM-567 comments (10:25 and 11:40am PT) log the adds; Karthic's report came in at 3:20am PT; Arthur's answer (1:05pm) and his Dentsu heads-up (4:20pm) follow the log. Paul's Sep 29 nudge said the SAFE was still with him; his Sep 30 mail withdraws before signing. Leonard's hub mail (2:05pm PT) comes after both.

SQL: 153 INSERT, 18 UPDATE. Truth (rev11): 25 on the list (1 / 7 / 14 / 3), 18 follow-up cards, the NCsoft comment, none for Dentsu or Makers. Design section 20 has the run table, the expected effect and the counter-readings.

### Rev11 baseline and the rev12 change

/injection PASS, /prompt PASS 5 and /hardness NON-FAIL 3 (PROCEED) on rev11 (75b6cb2a). The six baseline runs (`run_forensics/rev11/baseline/baseline_review.md`) caught Paul's back-out and both build-access cells in every run, because every run reached the angel post through its own SAFE or DocuSign search and opened its thread, and read the T-Accelerate mail thread in full. Five of six failed only SciPlay, so the failure-pattern and spread gates would fail.

Rev12 keeps the prompt, the groups, the counts and the Trello writes:
- Leonard's "Paul's out" moves from the reply under his angel post (removed; the post has no replies again) to his 1:1 DM with Frederick, D05S58U4SAK/1759251900.863415, same time and words. Measured over 15 Opus runs, 6 read that DM (newest message first) and 4 opened the SciPlay thread, with little overlap.
- Karthic's report and Arthur's answer in the T-Accelerate thread are removed, as is the rev11 placement under the 0.3.49 release post (its counters are base again). Arthur's correction C0880U9751A/1759274400.518306 is a #zombie-match3d root post again, saying "investor tester list" (the README's "tester adds") and naming Karthic, the 3 Dentsu folks, Anel's two at NCsoft and Ilse from Brightwater. It avoids "testflight" (searched by 13 of 15 runs) and the ticket id; "tester" was searched by 5 of 15.
- ZOM-567 gains two comments: NCsoft (lc_4369758f577612cdb63b3457, both tracks added Sep 22, after its Sep 19 call) and Brightwater (lc_5e2ff140afff06e3a78e2fe1, both added Sep 26, the day after its Sep 25 call). Truth: NCsoft and Brightwater Build access iOS only (was none); the other two cells unchanged.
- Coherence: the ZOM-567 comments are logged at 10:45 and 11:05am PT, before Arthur's 4:20pm post; Brightwater's add follows Ilse's Sep 26 reply; NCsoft's follows the Sep 19 call that Leonard's "F/up with Anel after the engine deep dive" card tracks.

SQL: 147 INSERT, 13 UPDATE. Truth (rev12): 25 on the list (1 / 7 / 14 / 3), four In talks firms iOS only (T-Accelerate, Dentsu, NCsoft, Brightwater), 18 follow-up cards, the NCsoft comment, none for Dentsu or Makers. Design section 21 has the exposure table, the expected effect and the counter-readings.

## Platform follow-ups

- ○ carriers to confirm in the Opus pre-check: Contacts `job` through contacts_search_contacts (e3a91c07d5b48f26a0c7e314); no speaker notes are relied on: slide 9's columns are visible element text (f_a47d0e2c95b18f63e2c0d5).
- Trello comment rendering through trello_get_comments (68c64270d660c977c4696986 and, rev9, 68db03b86054eff7e8e92474) and Linear comments through linear_list_comments (ZOM-567; ● per Ask_Carriers §6b).
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

Preflight: `PREFLIGHT: PASS` (solver contract PASS; contract.regression not run for rev7 because the deliverable changed from the 79-row register to the send list, so no earlier truth applies; surface PASS, all 30 mutation results dispositioned in 01c_Dispositions.json, geometry U = 0.8889 > 0.15, L_max 0.5556 OK); mutation (verbatim tail):

```
{{MUTATION}}
```

Forecast (UNCALIBRATED, pre-registered for rev6 as hev_9c763b7f8d97bf4a (earlier rev6 drafts: hev_eb2ec6fb4c97683f, hev_40590c7d7c45c5c4); earlier records: rev5 hev_e8e5aad467bf08f7, rev5 posterior after the pre-check hev_7b7855d894bf400b, rev6 design hev_77b5a028a20fb6ac, rev1 hev_4c8f05e25916f114, rev2a hev_e6d9d0fba5e9c65a, rev2 hev_a994b86c419749c5, rev3 hev_5d9bd3b90d474f0e, rev4 hev_48c507386b768324): V3 P(all four difficulty gates) 0.018-0.260; every rule's prior is Beta(1,2) from its one rev5 LEAKED record, which measured rev5's placements, not rev6's; text-graded slots (RP2, RP3, KW1, KW2) are not simulated, so losses are understated.

Checks A–C walk (Evals/0_Injection_Quality_Eval.md): inventory 130 INSERT + 11 UPDATE (sql_lint); Check A references, uniqueness over full collections, ownership/membership (Frederick in C096HFA5Z8W and C07C2866011; owner of d_5e8a1c3f9b07d2e64a1b93), id contracts — PASS (base_check, eval lint); Check B structure, literal JSON, generated/NOT NULL columns — PASS (sql_lint 0 errors, eval lint FAIL 0); Check C dates, parent/reply, counts — PASS (base_check), every seed before 2025-10-01T00:00Z; no PENDING item.

Touched-data census: listed above under "Touched-data census and coherence hazards".

| # | Category | Counter-reading (strongest case it fails) | Evidence | Verdict |
|---|---|---|---|---|
| 1 | temporal | Robert's reply says "this morning"; is it after the seed bound or before its root? | C07C2866011/1759248360.377105 (2025-09-30T16:06Z = 9:06am PT), root C07C2866011/1759196326.309469 (Sep 30 01:38Z) | after its root and before 2025-10-01T00:00Z; sql_lint 0 errors |
| 2 | semantic | "Sciplay" vs "SciPlay" reads as two firms | f_48247af79428823c3cac92, frederick.stone@harmonygames.co/1842285743246816270 | case variant of one name; register key follows the list |
| 3 | cross-service referential | Edith's pass names no firm, so it cannot be placed | e3a91c07d5b48f26a0c7e314, cc PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096) | resolvable through two persona-visible records |
| 4 | quantitative | Leonard's sheet still says Anton 40000, contradicting his own DM | f_6e1d93a0c4b72f85d39a0e (Sep 20) vs D05S58U4SAK/1758731100.281734 (Sep 24) | dated stale tracker, later DM overturns (intended); the sheet's last edit is Sep 20 |
| 5 | state/lifecycle | ZOM-567 says the Play adds landed; Arthur's post says nobody has Android | lc_94eb35d962cfbdd31e1bd496, lc_b549f3057640a5eb08f7581e vs C0880U9751A/1759274400.518306 | the adds were made to a list; the post (later the same day) explains the list was not attached; both by Arthur (intended) |
| 6 | identifier/format | DocuSign link placeholder [IDENTIFIER_99011] is a new token | frederick.stone@harmonygames.co/1844354293432320031 | base links use [IDENTIFIER_n] placeholders (leonard@harmonygames.co_1774464522151433079.json); no identity meaning |
| 7 | other | the Paul nudge makes DONE1 trivially visible | frederick.stone@harmonygames.co/1844610859008000037 | rev10: Paul's own Sep 30 reply in that thread says he signed, so the thread no longer shows the gap; the resolver is the missing Completed notice under Leonard's note C07C2866011/1758911700.336170 (UGT kept) |
| 8 | intended disagreement (Paul) | an unintended inconsistency between post and signing state | C07C2866011/1758303600.418207 | dated verbal claim vs later signing records; template defines committed |
| 9 | intended disagreement (Anton) | two amounts for one person in two services | D05S58U4SAK/1758731100.281734 | later message from Leonard, who sent both SAFEs; the second DM D05S58U4SAK/1758914100.640218 settles which one was signed |
| 10 | intended disagreement (Dentsu, T-Accelerate) | the base Sep 22 Play link (C07C2866011/1758558621.032499) means T-Accelerate has Android | C096HFA5Z8W/1758677722.184129, C0880U9751A/1759274400.518306 | the base itself says the link is not enough ("add them by email"); Arthur's post says the email list never reached the track |
| 11 | intended disagreement (SciPlay) | Robert's note could be hearsay, or a phone no might not count | C07C2866011/1759248360.377105, f_3b9e61c04d7a52e8f1a6c2 | Robert took the call himself; the rev6 Passed rule has no channel or writing condition |
| 12 | intended disagreement (Hiro) | list column vs mail | f_48247af79428823c3cac92 | the column states its own date (as of 09/11) |
| 13 | intended disagreement (templates) | two live templates with different rules | f_8d2c47a91e05b3f6d7c418 vs f_3b9e61c04d7a52e8f1a6c2 | different boards (Jul 16 vs Oct 14), the hub names the Oct 14 one |
| 14 | people status | Arthur quiet in Oct yet owns an open ticket | arthur.blake@harmonygames.co, ZOM-567 | ticket and comment dated Sep 30, before the clock |
| 15 | cross-service referential (rev2) | the seeded Hiro call contradicts the list's "no response as of 09/11" or Leonard's Sep 8 tracker | f_48247af79428823c3cac92 (modified 2025-09-15T19:27:01Z), C096HFA5Z8W/1757345124.546449, evt_7d3e19b04a6c25f8e1b9a0 (created 2025-09-19T18:30Z) | the call is booked after both dated notes; no base calendar row holds any Hiro person, so nothing is contradicted |
| 16 | temporal (rev3) | Ryo-san's mail is dated Friday in Japan but Thursday evening in LA, and Arthur's note must match | frederick.stone@harmonygames.co/1844294398771200045 (2025-09-26T03:10Z = Fri 12:10 JST, Thu 20:10 PT) | rev3: Arthur writes "came in Thursday night" (PT); Leonard's reply is Fri Sep 26 PT |
| 17 | temporal (rev4) | Leonard's 1AM post comes before the email it describes | C096HFA5Z8W/1757365500.384216 (Sep 8 21:05Z) vs frederick.stone@harmonygames.co/1842278301421016623 (forwarded 20:53Z) | consistent: posted 12 minutes after his forward to the founders |
| 18 | state/lifecycle (rev4) | Leonard's Play correction contradicts his own Sep 23 and Sep 24 posts | C096HFA5Z8W/1758817200.730591 vs C096HFA5Z8W/1758671737.632949, C096HFA5Z8W/1758764645.225239 | the correction is later (Sep 25) and explains them: the Sep 15 no reached Griffin (base forward leonard@harmonygames.co_1843348868615219366, Sep 15) |
| 19 | cross-service referential (rev4) | Leonard's Mattel note refers to a decline Frederick cannot see | C096HFA5Z8W/1758927000.205874 (Sep 26 22:50Z) vs the Leonard-only reply of Sep 26 22:28Z (leonard@harmonygames.co_1842359642190933488) | the note is posted after the decline and states its content, so Frederick's view now agrees with the full data |
| 20 | semantic (rev4) | the new template rules hand over statuses | f_3b9e61c04d7a52e8f1a6c2 | they define buckets and sources, not any firm's status (the only firm named is a16z, as the speedrun example); FACT CHECK --no-leak PASS |
| 21 | temporal (rev4) | Leonard's Treo post sits beside his Sep 3 reach-out list and could be read as Sep 2 warm-up work | C096HFA5Z8W/1756942260.617302 (Sep 3 23:31Z = 4:31pm PT) vs C096HFA5Z8W/1756941551.539229 | "this morning" is Sep 3 PT, the kickoff day the template counts |
| 22 | quantitative (rev4) | the reply's firm count could leave angels out | 68d81f30a6c94e2b7d05e1f4 | the Board Deck comment now says "every row, angels included"; the template already counts angels as rows |
| 23 | state/lifecycle (rev5) | the ZOM-567 comments contradict Arthur's Sep 22 #executives invites | lc_94eb35d962cfbdd31e1bd496, lc_b549f3057640a5eb08f7581e vs C07C2866011/1758558604.159869 ("Invites sent") | rev5: T-Accelerate's two adds are dated Sep 22; Dentsu's Play add waits on Google account addresses, matching Arthur's Sep 23 "add them by email for google play to work" |
| 24 | cross-service referential (rev5) | Leonard's Initial Capital post has no mail behind it | C096HFA5Z8W/1757442000.492583 | the post says the exchange was on LinkedIn, like the base Treo and BITKRAFT LinkedIn contacts; no mail is expected |
| 25 | cross-service referential (rev6) | Anton "emailed" Leonard, but no such mail is in Frederick's view | D05S58U4SAK/1758731100.281734 | the mail went to Leonard only (Frederick is not on it), as the DM says; the Completed notice frederick.stone@harmonygames.co/1844354293432320031 reached Frederick as a DocuSign cc |
| 26 | temporal (rev6) | Arthur could have attached the Play list on Sep 30 evening, making Android live by end of day | C0880U9751A/1759276080.094417 | Arthur's post says he attaches it "when I push tomorrow's build" (Oct 1); no later record shows it done before the clock |
| 30 | semantic (rev7) | the send list could be read as the whole 2025 list (Robert's idea) | frederick.stone@harmonygames.co/1844623441920000059, frederick.stone@harmonygames.co/1844724419788800011 | the hub withdraws it ("Let's not, only the people the doc says"); the doc lists the groups and says everyone else stays off |
| 31 | quantitative (rev7) | the reply's group counts could count Anton under In talks (an angel who said yes) | C07C2866011/1758911700.336170, frederick.stone@harmonygames.co/1844354293432320031 | the doc puts signed SAFE holders under New investor and only unsigned angels under In talks; Anton's Completed notice is in: New investor 1, In talks 8 |
| 28 | cross-service referential (rev6 sweep) | Arthur's request to Leonard implied Arthur lacked Play console rights, but the base shows him inviting people to Play Console that morning | CD843DBC4C3E/1759244974.454399, C0880U9751A/1759274400.518306 | rewritten: Arthur attaches it himself with tomorrow's build; no permission claim |
| 29 | temporal (rev6 sweep) | Treo's first LinkedIn ping was Sep 2, not Sep 3 | D04UC0UEN2V/1756878703.235739, C096HFA5Z8W/1756942260.617302 | "pinged me again"; the Sep 3 deck send keeps Treo contacted this round (template: the kickoff day counts) |
| 27 | semantic (rev6) | Robert's reply under a speedrun post could read as about a16z | C07C2866011/1759248360.377105 | it names Sciplay and "D" (SciPlay's contact sign-off in frederick.stone@harmonygames.co/1842285743246816270) |
| 32 | temporal (rev9) | the Anel card's idShort 456 is out of order with the board | 68c99e98737744bd966aed24 (created 2025-09-16T17:30Z) vs 68c5a49e8491a9d7faf869d0 (idShort 455, created 2025-09-13T17:06Z) | 456 follows the board's highest base card, made three days earlier |
| 33 | cross-service referential (rev9) | the Oct 8 call names a person no other record ties to a firm | evt_6b2e94d0c17a3f58e9d2b1, f_48247af79428823c3cac92 | the 2025 list's Makers Fund row has Partner Michael Cheung; the name occurs nowhere else in the universe |
| 34 | state/lifecycle (rev9) | a booked Oct 8 call means Makers is In talks, not Awaiting reply | evt_6b2e94d0c17a3f58e9d2b1, f_3b9e61c04d7a52e8f1a6c2 | the doc's In talks needs a call that happened by end of Sep 30; Makers stays Awaiting reply ("even if they've written back") |
| 35 | semantic (rev9) | Homa's open Doing card "[USERNAME_34488] send material [PERSON_NAME_0854]" counts as an existing card | 68db03b86054eff7e8e92474 | the rule names cards "in To Do"; Homa gets a new card |
| 36 | semantic (rev10) | Paul's "Done, signed it last night" makes him a New investor | frederick.stone@harmonygames.co/<CAA_lm07dfuR9zTKG5Xh1lma8QW1_dNi4pJJcvpJ@mail.gmail.com>, C07C2866011/1758911700.336170 | Leonard's note: only the DocuSign Completed notice counts, "them telling us they're in doesn't count"; no Completed notice for Paul exists |
| 37 | state/lifecycle (rev10) | Paul signed, so DocuSign should have sent a Completed notice | frederick.stone@harmonygames.co/1844354293432320031 | a SAFE completes only after Harmony countersigns (Anton's Completed came Sep 26, two days after Leonard resent his SAFE); Leonard is packing for LA on Sep 30 |
| 38 | temporal (rev10) | Arthur's Sep 30 reply sits under a Sep 29 post, so it predates the problem | C0880U9751A/1759182908.627389, C0880U9751A/1759274400.518306 | replies carry their own time (Sep 30 4:20pm PT), after the ZOM-567 comments (10:25 and 11:40am PT) |
| 39 | voice (rev10) | Arthur's reply is about the iOS release, not investor access | C0880U9751A/1759274400.518306 | it opens "heads up on the investor builds" and names the 3 Dentsu folks (rev11); Leonard answers about telling Ryo-san |
| 40 | semantic (rev11) | Leonard's note says his posts don't count, so "Paul's out" doesn't either | C07C2866011/1758911700.336170, the rev11 reply under the angel post (moved to D05S58U4SAK/1759251900.863415 in rev12) | the note governs what counts as signed (a yes); a no is governed by the send-list doc ("Passed means they've told us no for this round"; "us" includes Leonard, and Paul wrote to Leonard) |
| 41 | intended disagreement (rev11) | the Bridge angels sheet still says Paul is in | f_6e1d93a0c4b72f85d39a0e | the sheet was last edited Sep 20; Leonard's Sep 30 reply is later and names Paul |
| 42 | cross-service referential (rev11) | Leonard's "he wrote me this morning" needs a mail | leonard.hayes@harmonygames.co/<CAH2UMEfxg69PBVI7YxuPTO9uXYBOEfsCOfTEzpB@mail.gmail.com> | Paul's reply to Leonard only, Sep 30 7:55am PT, in Leonard's copy of the nudge thread |
| 43 | quantitative (rev11) | Arthur's mail may cover Karthic only, so Dentsu could still have Android | Arthur's rev11 answer to Karthic (removed in rev12), C0880U9751A/1759274400.518306 | the mail says nobody on the investor list has Android; the Slack reply names the 3 Dentsu folks; iOS only either way |
| 44 | temporal (rev11, history) | Karthic's report predates the ZOM-567 log, so the log could reflect a fix | lc_94eb35d962cfbdd31e1bd496, Arthur's rev11 answer to Karthic (removed in rev12) | the log records adds, not the attach; Arthur's answer after the log says the list was never attached |
| 45 | semantic (rev12) | a 1:1 DM is not the investor telling us no | D05S58U4SAK/1759251900.863415, leonard.hayes@harmonygames.co/<CAH2UMEfxg69PBVI7YxuPTO9uXYBOEfsCOfTEzpB@mail.gmail.com> | Paul wrote Leonard ("us"); Leonard relays it to his co-founder; the doc's Passed rule applies |
| 46 | intended disagreement (rev12) | ZOM-567 logs both tracks for NCsoft and Brightwater | lc_4369758f577612cdb63b3457, lc_5e2ff140afff06e3a78e2fe1, C0880U9751A/1759274400.518306 | the log records adds; Arthur's later post says the Play list was never attached, naming both |
| 47 | cross-service referential (rev12) | Arthur names "Anel's two at NCsoft" but no mail shows NCsoft asking for the build | lc_4369758f577612cdb63b3457 | the ticket is the record of the add ("2 accounts from Anel's team, after the Sep 19 call") |
| 48 | temporal (rev12) | Brightwater's add (Sep 26) comes before Ilse's second meeting | lc_5e2ff140afff06e3a78e2fe1, frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com> | Leonard offered the build after the Sep 25 call; the second meeting is about the partners, not access |
| 49 | voice (rev12) | Arthur's root post is addressed to Leonard in a game channel | C0880U9751A/1759274400.518306 | Arthur posts build matters there; Frederick is a member; the README says Arthur tracks the tester adds |

Re-verified from source this session through tools/hg.py and the exports: rev6 Slack roots and channels (C07C2866011/1759196326.309469 id 99aa913348bb05e6eda8daa06d37fc2a; D05S58U4SAK Sep 2025 messages; C0880U9751A Sep 2025 build messages; persona_view can-see YES for all three); list rows (f_48247af79428823c3cac92), SciPlay messages (gmail:threads/frederick@harmonygames.co_1842285743246816270.json /messages/1), T-Accelerate recap (/messages/0 of 1842283406259093714), Calendly note "here from T-Accelerate" (frederick.stone@harmonygames.co/1843625920612854647), Hiro Investment Director signature (leonard@harmonygames.co_1842278433020808799.json), ZOM-566 creation time, DocuSign notice shapes.

Unresolved: no independent (dual red-team) review — REDTEAM_* unset (the two blind sweeps run before /prompt); forecasts are UNCALIBRATED and their priors are the seven rev5 LEAKED records; whether a fresh Opus run searches Slack per firm is unknown until the rev6 pre-check.
