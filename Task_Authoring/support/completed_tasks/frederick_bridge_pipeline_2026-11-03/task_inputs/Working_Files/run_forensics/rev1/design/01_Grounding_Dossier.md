# Grounding Dossier — frederick_bridge_pipeline · injection rev1 · contains no prompt, OE or criterion text

SQL: `task_inputs/01_Universe_Inject.sql` (stored byte for byte in `Working_Files/run_forensics/rev1/01_Universe_Inject.sql`),
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
CHECK-SQL as frederick_stone <frederick.stone@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_8d2c47a91e05b3f6d7c418 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_3b9e61c04d7a52e8f1a6c2 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert d_5e8a1c3f9b07d2e64a1b93 - persona owns the file
[YES LB] L13 gdrive.drive_files insert f_c61a0e93b7d24f58a2e917 - file is shared with the persona (shared_with_emails)
[YES LB] L15 gdrive.drive_files insert f_a47d0e2c95b18f63e2c0d5 - file is shared with the persona (shared_with_emails)
[YES LB] L17 gdrive.drive_files insert f_6e1d93a0c4b72f85d39a0e - file is shared with the persona (shared_with_emails)
[YES LB] L19 gdocs.docs_documents insert f_8d2c47a91e05b3f6d7c418 - file is shared with the persona (shared_with_emails)
[YES LB] L22 gdocs.docs_documents insert f_3b9e61c04d7a52e8f1a6c2 - file is shared with the persona (shared_with_emails)
[YES LB] L24 gdocs.docs_documents insert f_c61a0e93b7d24f58a2e917 - file is shared with the persona (shared_with_emails)
[YES LB] L26 gsheets.sheets_spreadsheets insert f_6e1d93a0c4b72f85d39a0e - file is shared with the persona (shared_with_emails)
[YES LB] L29 gsheets.sheets_sheets insert f_6e1d93a0c4b72f85d39a0e, f_6e1d93a0c4b72f85d39a0e#0 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gslides.slides_presentations insert f_a47d0e2c95b18f63e2c0d5 - file is shared with the persona (shared_with_emails)
[YES LB] L34 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_b4c21ca913ab - file is shared with the persona (shared_with_emails)
[YES LB] L36 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_6825f973029b, slide_b4c21ca913ab - file is shared with the persona (shared_with_emails)
[YES LB] L38 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_cffa02683868, slide_b4c21ca913ab - file is shared with the persona (shared_with_emails)
[YES LB] L40 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_256dc0474f7c - file is shared with the persona (shared_with_emails)
[YES LB] L42 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_72151261faca, slide_256dc0474f7c - file is shared with the persona (shared_with_emails)
[YES LB] L44 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_ca7b40076cd7, slide_256dc0474f7c - file is shared with the persona (shared_with_emails)
[YES LB] L46 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_fd6dbd079420 - file is shared with the persona (shared_with_emails)
[YES LB] L48 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_90fbf6fd9c1b, slide_fd6dbd079420 - file is shared with the persona (shared_with_emails)
[YES LB] L50 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_ef5243814e8f, slide_fd6dbd079420 - file is shared with the persona (shared_with_emails)
[YES LB] L52 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_bb11abfc5fad - file is shared with the persona (shared_with_emails)
[YES LB] L54 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_69587907b898, slide_bb11abfc5fad - file is shared with the persona (shared_with_emails)
[YES LB] L56 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_6ca8bffe4445, slide_bb11abfc5fad - file is shared with the persona (shared_with_emails)
[YES LB] L58 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_cb3f0884f833 - file is shared with the persona (shared_with_emails)
[YES LB] L60 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_0c72e8ba6af7, slide_cb3f0884f833 - file is shared with the persona (shared_with_emails)
[YES LB] L62 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_1e212bf4628e, slide_cb3f0884f833 - file is shared with the persona (shared_with_emails)
[YES LB] L64 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_a56932e4c738 - file is shared with the persona (shared_with_emails)
[YES LB] L66 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_5da52b8348b0, slide_a56932e4c738 - file is shared with the persona (shared_with_emails)
[YES LB] L68 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_4f7f04b6e984, slide_a56932e4c738 - file is shared with the persona (shared_with_emails)
[YES LB] L70 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_c9c7eed73bb9 - file is shared with the persona (shared_with_emails)
[YES LB] L72 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_b45885b83bf9, slide_c9c7eed73bb9 - file is shared with the persona (shared_with_emails)
[YES LB] L74 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_ed13f88ca45b, slide_c9c7eed73bb9 - file is shared with the persona (shared_with_emails)
[YES LB] L76 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_329b5dfcb888 - file is shared with the persona (shared_with_emails)
[YES LB] L78 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_09521ac10bd5, slide_329b5dfcb888 - file is shared with the persona (shared_with_emails)
[YES LB] L80 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_d65f0ea436c8, slide_329b5dfcb888 - file is shared with the persona (shared_with_emails)
[YES LB] L82 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_68eecd4f5f2a - file is shared with the persona (shared_with_emails)
[YES LB] L84 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_b87125dbf11e, slide_68eecd4f5f2a - file is shared with the persona (shared_with_emails)
[YES LB] L86 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_6548686fe965, slide_68eecd4f5f2a - file is shared with the persona (shared_with_emails)
[YES LB] L88 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_98d06d32c8d6 - file is shared with the persona (shared_with_emails)
[YES LB] L90 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_154065e277bc, slide_98d06d32c8d6 - file is shared with the persona (shared_with_emails)
[YES LB] L92 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_ee461e258b77, slide_98d06d32c8d6 - file is shared with the persona (shared_with_emails)
[YES LB] L94 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_fcf2cb38bf31 - file is shared with the persona (shared_with_emails)
[YES LB] L96 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_8ee884c1e93b, slide_fcf2cb38bf31 - file is shared with the persona (shared_with_emails)
[YES LB] L98 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_34bc96464df6, slide_fcf2cb38bf31 - file is shared with the persona (shared_with_emails)
[YES LB] L100 gslides.slides_pages insert f_a47d0e2c95b18f63e2c0d5, slide_5c7db3c42932 - file is shared with the persona (shared_with_emails)
[YES LB] L102 gslides.slides_page_elements insert f_a47d0e2c95b18f63e2c0d5, el_ef3226341cb0, slide_5c7db3c42932 - file is shared with the persona (shared_with_emails)
[YES LB] L104 slack.slack_messages insert 4921f321db5d08f936aac24a6a1d2af8, C07C2866011/1758303600.418207 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L107 slack.slack_messages insert 7fef94264090696760180223fc8265e7, C07C2866011/1759168800.117903 - persona EMPLOYEE_0008_SLACK_ID is in members of private executives
[YES LB] L109 slack.slack_messages insert 3f2d8f04b29a78808033543c740bb669, C096HFA5Z8W/1759161600.226431 - persona EMPLOYEE_0008_SLACK_ID is in members of private bridge-pitch
[YES LB] L111 slack.slack_messages insert cf10d4f7f88143dc7ab976df27513790, C096HFA5Z8W/1759184040.552871 - persona EMPLOYEE_0008_SLACK_ID is in members of private bridge-pitch
[YES] L113 slack.slack_messages update 73c2247f4a31f32d10b3068ecd1d13ac, C096HFA5Z8W/1757716998.377299 - persona EMPLOYEE_0008_SLACK_ID is in members of private bridge-pitch
[YES LB] L136 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844623441920000059 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L139 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L141 gmail.gmail_threads insert robert@harmonygames.co/1844623441920000061 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L143 gmail.gmail_messages insert robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L145 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844623441920000062 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L147 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L149 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844724419788800011 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L151 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L153 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844724419788800013 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L155 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L157 gmail.gmail_threads insert robert@harmonygames.co/1844724419788800014 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L159 gmail.gmail_messages insert robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L161 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844724419788800015 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L163 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L165 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844162278195200023 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L167 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L169 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844162278195200025 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L171 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L173 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844354293432320031 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L175 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L177 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844610859008000037 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L179 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L181 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844610859008000039 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L183 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L185 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844318935449600041 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L187 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L189 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844318935449600043 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L191 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L193 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844347876147200047 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L195 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L197 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844347876147200049 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L199 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L201 gmail.gmail_threads insert robert@harmonygames.co/1844347876147200050 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L203 gmail.gmail_messages insert robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L205 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844347876147200051 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L207 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L209 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844276782694400053 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L211 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L213 gmail.gmail_threads insert leonard.hayes@harmonygames.co/1844276782694400055 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L215 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L217 gmail.gmail_threads insert robert@harmonygames.co/1844276782694400056 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L219 gmail.gmail_messages insert robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L221 gmail.gmail_threads insert arthur.blake@harmonygames.co/1844276782694400057 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L223 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES LB] L225 gmail.gmail_threads update frederick.stone@harmonygames.co/1844276782694400053 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L226 gmail.gmail_messages insert frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>, - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L228 gmail.gmail_threads update leonard.hayes@harmonygames.co/1844276782694400055 - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L229 gmail.gmail_messages insert leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>, l - row is in mailbox leonard.hayes@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L231 gmail.gmail_threads update robert@harmonygames.co/1844276782694400056 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L232 gmail.gmail_messages insert robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>, robert@h - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L234 gmail.gmail_threads update arthur.blake@harmonygames.co/1844276782694400057 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L235 gmail.gmail_messages insert arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>, ar - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES] L237 gmail.gmail_threads insert frederick.stone@harmonygames.co/1843992534712320061 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L239 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[NO] L241 gmail.gmail_threads insert robert@harmonygames.co/1843992534712320063 - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L243 gmail.gmail_messages insert robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com>, robert@ - row is in mailbox robert@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L245 gmail.gmail_threads insert arthur.blake@harmonygames.co/1843992534712320064 - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[NO] L247 gmail.gmail_messages insert arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com>, a - row is in mailbox arthur.blake@harmonygames.co, not the persona's (frederick.stone@harmonygames.co)
[YES] L249 gmail.gmail_threads insert frederick.stone@harmonygames.co/1844724105216000067 - row user_email is the persona (frederick.stone@harmonygames.co)
[YES] L251 gmail.gmail_messages insert frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com> - row user_email is the persona (frederick.stone@harmonygames.co)
[YES LB] L253 gcal.gcal_events insert evt_2f86b0d4c9e17a35b64e0d - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L256 gcal.gcal_events insert evt_b511d4619c6f46ee63959b - persona is an attendee and holds its own copy evt_2f86b0d4c9e17a35b64e0d (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L258 gcal.gcal_events insert evt_8bd5e929463b854ec0ad13 - persona is an attendee and holds its own copy evt_2f86b0d4c9e17a35b64e0d (same ical_uid and start) on frederick.stone@harmonygames.co
[YES] L260 gcal.gcal_events insert evt_ca908a712455521f1f8b43 - persona is an attendee and holds its own copy evt_2f86b0d4c9e17a35b64e0d (same ical_uid and start) on frederick.stone@harmonygames.co
[YES LB] L262 gcal.gcal_events insert evt_9c41e7a2d05b38f6e1a7c4 - event is on the persona's own calendar frederick.stone@harmonygames.co
[YES] L264 gcal.gcal_events insert evt_75d8a0687ea57b663a40b0 - persona is an attendee and holds its own copy evt_9c41e7a2d05b38f6e1a7c4 (same ical_uid and start) on frederick.stone@harmonygames.co

summary: {'YES': 80, 'NO': 38}  unscoped rows (always visible): 17
  gcal.gcal_events: {'YES': 6}
  gdocs.docs_documents: {'YES': 3}
  gdrive.drive_files: {'YES': 6}
  gmail.gmail_messages: {'YES': 11, 'NO': 19}
  gmail.gmail_threads: {'YES': 11, 'NO': 19}
  gsheets.sheets_sheets: {'YES': 1}
  gsheets.sheets_spreadsheets: {'YES': 1}
  gslides.slides_page_elements: {'YES': 23}
  gslides.slides_pages: {'YES': 12}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 5}
verdict: PASS (0 load-bearing rows not visible)
```

Scoped load-bearing records (all Frederick's copies or files shared with him):
- frederick.stone@harmonygames.co/1844724419788800011 — hub thread in his mailbox (INBOX) LB
- frederick.stone@harmonygames.co/1844162278195200023 — Anton's mail, cc Frederick LB
- frederick.stone@harmonygames.co/1844354293432320031 — DocuSign Completed (Anton), to Frederick LB
- frederick.stone@harmonygames.co/1844610859008000037 — Leonard's nudge to Paul, cc Frederick LB
- frederick.stone@harmonygames.co/1844318935449600041 — Edith Vane's pass, cc Frederick LB
- frederick.stone@harmonygames.co/1844347876147200047 — Leonard's Dentsu mail, cc Frederick LB
- frederick.stone@harmonygames.co/1844276782694400053 — Brightwater follow-up and Ilse's reply, cc Frederick LB
- f_3b9e61c04d7a52e8f1a6c2 — template shared with Frederick (reader) LB
- d_5e8a1c3f9b07d2e64a1b93 — Board folder owned by Frederick LB
- evt_2f86b0d4c9e17a35b64e0d — Brightwater call on Frederick's calendar LB
- C096HFA5Z8W — #bridge-pitch, Frederick a member LB
- C07C2866011 — #executives, Frederick a member LB
- Unscoped (visible to all): ZOM-567, 68c64270d660c977c4696986, e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8.

## 1.F Collision

- Minted ids checked: Slack ts C07C2866011/1758303600.418207, C07C2866011/1759168800.117903, C096HFA5Z8W/1759161600.226431, C096HFA5Z8W/1759184040.552871 absent from the month files; ZOM-567 absent (max ZOM 566); f_/d_/evt_/24-hex ids (f_3b9e61c04d7a52e8f1a6c2, f_8d2c47a91e05b3f6d7c418, f_c61a0e93b7d24f58a2e917, d_5e8a1c3f9b07d2e64a1b93, f_a47d0e2c95b18f63e2c0d5, f_6e1d93a0c4b72f85d39a0e, evt_2f86b0d4c9e17a35b64e0d, evt_9c41e7a2d05b38f6e1a7c4, e3a91c07d5b48f26a0c7e314, b72f0d6e19c3a84e5d21f9a0, 5d0e8b31f7a29c64e1b0d3a8) absent from gdrive/gdocs/gsheets/gslides/gcal/contacts data (Python containment scan with control f_48247af79428823c3cac92 found); base_check Check A (identifier uniqueness over the full collections) PASS.
- Header tokens: PERSON_9901–9904_EMAIL unused anywhere (0 of 386,054 files); existing tokens reused only for their own people (PERSON_5282 Hiro Investment Director, PERSON_3242 Karthic of T-Accelerate per frederick.stone@harmonygames.co/1843625920612854647, Dentsu PERSON_2581/5584/5221, SVC_1302 DocuSign).
- Body tokens: none minted ([IDENTIFIER_99011] in the DocuSign link is a new link placeholder in the base's style; no identity).

## Record ledger

| # | Table | Id | Manifest element | Carrier | Discovery role |
|---|---|---|---|---|---|
| 1 | gdrive.drive_files | f_8d2c47a91e05b3f6d7c418 | H1/T9/K13/K11/R5/T4 files | ● | authority · decoy · write target |
| 2 | gdrive.drive_files | f_3b9e61c04d7a52e8f1a6c2 | H1/T9/K13/K11/R5/T4 files | ● | authority · decoy · write target |
| 3 | gdrive.drive_files | d_5e8a1c3f9b07d2e64a1b93 | H1/T9/K13/K11/R5/T4 files | ● | authority · decoy · write target |
| 4 | gdrive.drive_files | f_c61a0e93b7d24f58a2e917 | H1/T9/K13/K11/R5/T4 files | ● | authority · decoy · write target |
| 5 | gdrive.drive_files | f_a47d0e2c95b18f63e2c0d5 | H1/T9/K13/K11/R5/T4 files | ● | authority · decoy · write target |
| 6 | gdrive.drive_files | f_6e1d93a0c4b72f85d39a0e | H1/T9/K13/K11/R5/T4 files | ● | authority · decoy · write target |
| 7 | gdocs.docs_documents | f_8d2c47a91e05b3f6d7c418 | H1 template, July decoy (T9), README (K13) | ● | authority · decoy |
| 8 | gdocs.docs_documents | f_3b9e61c04d7a52e8f1a6c2 | H1 template, July decoy (T9), README (K13) | ● | authority · decoy |
| 9 | gdocs.docs_documents | f_c61a0e93b7d24f58a2e917 | H1 template, July decoy (T9), README (K13) | ● | authority · decoy |
| 10 | gslides.slides_presentations | f_a47d0e2c95b18f63e2c0d5 | K11 draft deck | ● | connecting |
| 11 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_b4c21ca913ab | K11 draft deck slide (notes ○) | ○ | connecting |
| 12 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_256dc0474f7c | K11 draft deck slide (notes ○) | ○ | connecting |
| 13 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_fd6dbd079420 | K11 draft deck slide (notes ○) | ○ | connecting |
| 14 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_bb11abfc5fad | K11 draft deck slide (notes ○) | ○ | connecting |
| 15 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_cb3f0884f833 | K11 draft deck slide (notes ○) | ○ | connecting |
| 16 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_a56932e4c738 | K11 draft deck slide (notes ○) | ○ | connecting |
| 17 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_c9c7eed73bb9 | K11 draft deck slide (notes ○) | ○ | connecting |
| 18 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_329b5dfcb888 | K11 draft deck slide (notes ○) | ○ | connecting |
| 19 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_68eecd4f5f2a | K11 draft deck slide (notes ○) | ○ | connecting |
| 20 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_98d06d32c8d6 | K11 draft deck slide (notes ○) | ○ | connecting |
| 21 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_fcf2cb38bf31 | K11 draft deck slide (notes ○) | ○ | connecting |
| 22 | gslides.slides_pages | f_a47d0e2c95b18f63e2c0d5#slide_5c7db3c42932 | K11 draft deck slide (notes ○) | ○ | connecting |
| 23 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_6825f973029b | K11 draft deck text | ● | connecting |
| 24 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_cffa02683868 | K11 draft deck text | ● | connecting |
| 25 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_72151261faca | K11 draft deck text | ● | connecting |
| 26 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_ca7b40076cd7 | K11 draft deck text | ● | connecting |
| 27 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_90fbf6fd9c1b | K11 draft deck text | ● | connecting |
| 28 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_ef5243814e8f | K11 draft deck text | ● | connecting |
| 29 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_69587907b898 | K11 draft deck text | ● | connecting |
| 30 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_6ca8bffe4445 | K11 draft deck text | ● | connecting |
| 31 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_0c72e8ba6af7 | K11 draft deck text | ● | connecting |
| 32 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_1e212bf4628e | K11 draft deck text | ● | connecting |
| 33 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_5da52b8348b0 | K11 draft deck text | ● | connecting |
| 34 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_4f7f04b6e984 | K11 draft deck text | ● | connecting |
| 35 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_b45885b83bf9 | K11 draft deck text | ● | connecting |
| 36 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_ed13f88ca45b | K11 draft deck text | ● | connecting |
| 37 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_09521ac10bd5 | K11 draft deck text | ● | connecting |
| 38 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_d65f0ea436c8 | K11 draft deck text | ● | connecting |
| 39 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_b87125dbf11e | K11 draft deck text | ● | connecting |
| 40 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_6548686fe965 | K11 draft deck text | ● | connecting |
| 41 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_154065e277bc | K11 draft deck text | ● | connecting |
| 42 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_ee461e258b77 | K11 draft deck text | ● | connecting |
| 43 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_8ee884c1e93b | K11 draft deck text | ● | connecting |
| 44 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_34bc96464df6 | K11 draft deck text | ● | connecting |
| 45 | gslides.slides_page_elements | f_a47d0e2c95b18f63e2c0d5#el_ef3226341cb0 | K11 draft deck text | ● | connecting |
| 46 | gsheets.sheets_spreadsheets | f_6e1d93a0c4b72f85d39a0e | T1/T4 stale angels sheet | ● | claim met first |
| 47 | gsheets.sheets_sheets | f_6e1d93a0c4b72f85d39a0e#0 | T1/T4 stale angels sheet tab | ● | claim met first |
| 48 | slack.slack_messages | C07C2866011/1758303600.418207 | T1/T4 post, D2 aside, K8 root, T3 reply | ● | claim met first · overturning |
| 49 | slack.slack_messages | C07C2866011/1759168800.117903 | T1/T4 post, D2 aside, K8 root, T3 reply | ● | claim met first · overturning |
| 50 | slack.slack_messages | C096HFA5Z8W/1759161600.226431 | T1/T4 post, D2 aside, K8 root, T3 reply | ● | claim met first · overturning |
| 51 | slack.slack_messages | C096HFA5Z8W/1759184040.552871 | T1/T4 post, D2 aside, K8 root, T3 reply | ● | claim met first · overturning |
| 52 | trello.trello_actions | 68c64270d660c977c4696986 | H2 rule comment / K10 deck card actions | ● | authority · connecting |
| 53 | trello.trello_actions | 68d8193c164e823ac3ae735d | H2 rule comment / K10 deck card actions | ● | authority · connecting |
| 54 | trello.trello_actions | 68d81ae0459a87b4efb4b1e3 | H2 rule comment / K10 deck card actions | ● | authority · connecting |
| 55 | trello.trello_actions | 68d81f30a6c94e2b7d05e1f4 | H2 rule comment / K10 deck card actions | ● | authority · connecting |
| 56 | trello.trello_cards | 68d8193cf451863621c88a2a | K10 Board Deck - Oct 14 card | ● | connecting |
| 57 | trello.trello_checklists | 68d81ae0bac8fd292e6606f8 | K10 deck sections checklist | ● | connecting |
| 58 | trello.trello_check_items | 68d81ae032fe8d64dbd262c7 | K10 deck sections items | ● | connecting |
| 59 | trello.trello_check_items | 68d81ae087c12c3d08c79ff8 | K10 deck sections items | ● | connecting |
| 60 | trello.trello_check_items | 68d81ae05ac90637e942026c | K10 deck sections items | ● | connecting |
| 61 | trello.trello_check_items | 68d81ae07d46d8fe71f4ba98 | K10 deck sections items | ● | connecting |
| 62 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844623441920000059 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 63 | gmail.gmail_threads | robert@harmonygames.co/1844623441920000061 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 64 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844623441920000062 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 65 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844724419788800011 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 66 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844724419788800013 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 67 | gmail.gmail_threads | robert@harmonygames.co/1844724419788800014 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 68 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844724419788800015 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 69 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844162278195200023 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 70 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844162278195200025 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 71 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844354293432320031 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 72 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844610859008000037 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 73 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844610859008000039 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 74 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844318935449600041 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 75 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844318935449600043 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 76 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844347876147200047 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 77 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844347876147200049 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 78 | gmail.gmail_threads | robert@harmonygames.co/1844347876147200050 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 79 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844347876147200051 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 80 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844276782694400053 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 81 | gmail.gmail_threads | leonard.hayes@harmonygames.co/1844276782694400055 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 82 | gmail.gmail_threads | robert@harmonygames.co/1844276782694400056 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 83 | gmail.gmail_threads | arthur.blake@harmonygames.co/1844276782694400057 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 84 | gmail.gmail_threads | frederick.stone@harmonygames.co/1843992534712320061 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 85 | gmail.gmail_threads | robert@harmonygames.co/1843992534712320063 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 86 | gmail.gmail_threads | arthur.blake@harmonygames.co/1843992534712320064 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 87 | gmail.gmail_threads | frederick.stone@harmonygames.co/1844724105216000067 | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 88 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 89 | gmail.gmail_messages | robert@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 90 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAdKLID2b1N4D6wzcwD-rpm-ZCAR-AB8XlFkArQG@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 91 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 92 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 93 | gmail.gmail_messages | robert@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 94 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAxDeR9CSc9iEY-zACLQaU5Hff5KY0zkGE4PQ9iK@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 95 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 96 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 97 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 98 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 99 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 100 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 101 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 102 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 103 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 104 | gmail.gmail_messages | robert@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 105 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 106 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 107 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 108 | gmail.gmail_messages | robert@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 109 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 110 | gmail.gmail_messages | frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 111 | gmail.gmail_messages | leonard.hayes@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 112 | gmail.gmail_messages | robert@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 113 | gmail.gmail_messages | arthur.blake@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 114 | gmail.gmail_messages | frederick.stone@harmonygames.co/<calendar-2b67d1aa-cbdd-d816-22c3-d5ace6cf900b@google.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 115 | gmail.gmail_messages | robert@harmonygames.co/<calendar-c82c189b-c33c-a6e0-5e43-def7d943af26@google.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 116 | gmail.gmail_messages | arthur.blake@harmonygames.co/<calendar-44faeeb8-a4b0-dae2-c4eb-4d2fda67b29b@google.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 117 | gmail.gmail_messages | frederick.stone@harmonygames.co/<calendar-297f69c9-ad63-fafd-14c3-70dbf78756f3@google.com> | A1 hub, T1/T4/T5/T2/T6 mails, D5, INT-11 invitations | ● | first link · evidence |
| 118 | gcal.gcal_events | evt_2f86b0d4c9e17a35b64e0d | T6 Brightwater call, K12 review event | ● (time/attendees) | evidence · deadline |
| 119 | gcal.gcal_events | evt_b511d4619c6f46ee63959b | T6 Brightwater call, K12 review event | ● (time/attendees) | evidence · deadline |
| 120 | gcal.gcal_events | evt_8bd5e929463b854ec0ad13 | T6 Brightwater call, K12 review event | ● (time/attendees) | evidence · deadline |
| 121 | gcal.gcal_events | evt_ca908a712455521f1f8b43 | T6 Brightwater call, K12 review event | ● (time/attendees) | evidence · deadline |
| 122 | gcal.gcal_events | evt_9c41e7a2d05b38f6e1a7c4 | T6 Brightwater call, K12 review event | ● (time/attendees) | evidence · deadline |
| 123 | gcal.gcal_events | evt_75d8a0687ea57b663a40b0 | T6 Brightwater call, K12 review event | ● (time/attendees) | evidence · deadline |
| 124 | linear.linear_issues | ZOM-567 | T2 ZOM-567 | ● | overturning |
| 125 | linear.linear_comments | lc_94eb35d962cfbdd31e1bd496 (ZOM-567) | T2 ZOM-567 comments | ● | overturning |
| 126 | linear.linear_comments | lc_b549f3057640a5eb08f7581e (ZOM-567) | T2 ZOM-567 comments | ● | overturning |
| 127 | contacts.contacts | e3a91c07d5b48f26a0c7e314 | T5/T6/T11 partner mappings | ○ (job) | connecting |
| 128 | contacts.contacts | b72f0d6e19c3a84e5d21f9a0 | T5/T6/T11 partner mappings | ○ (job) | connecting |
| 129 | contacts.contacts | 5d0e8b31f7a29c64e1b0d3a8 | T5/T6/T11 partner mappings | ○ (job) | connecting |

## Findability and discovery-order proofs

- Hub (A1) frederick.stone@harmonygames.co/1844724419788800011 — query "board pre-read" / "fundraising section" via gmail search; first link (prompt names it).
- Template H1 f_3b9e61c04d7a52e8f1a6c2 — query "board pre-read template" via gdocs/drive search; competing hit the July decoy f_8d2c47a91e05b3f6d7c418 (same words; dated by its body "for the Jul 16 board").
- Card rule H2 68c64270d660c977c4696986 on 68c5a49e8491a9d7faf869d0 — query "Existing Investor Update" via trello search returns the card; the rule is in comments (trello_get_comments); decoy 663ea0fc3f231e879cefd5e8 "Investor Update".
- CORR C096HFA5Z8W/1759184040.552871 — claim met first: the SciPlay thread frederick.stone@harmonygames.co/1842285743246816270 ("We'll continue to play and let you know"); overturned by Robert's reply under C096HFA5Z8W/1757716998.377299; met first because a firm-name mail search hits the thread; channel history omits replies.
- DONE1 C07C2866011/1758303600.418207 met first (channel history), Leonard's sheet f_6e1d93a0c4b72f85d39a0e repeats it; overturned by the absence of a DocuSign Completed notice for Paul beside Anton's (frederick.stone@harmonygames.co/1844354293432320031) and Leonard's nudge frederick.stone@harmonygames.co/1844610859008000037.
- INPUT: $40K in C07C2866011/1758303600.418207 and f_6e1d93a0c4b72f85d39a0e; overturned by frederick.stone@harmonygames.co/1844162278195200023 ($25K).
- DONE2: frederick.stone@harmonygames.co/1844347876147200047 ("Invites … are out to all three") met with the firm; overturned by ZOM-567 comment lc_b549f3057640a5eb08f7581e (Play track not added).
- ALIAS: list row "no response as of 09/11" (f_48247af79428823c3cac92) met first; overturned by frederick.stone@harmonygames.co/1844318935449600041 mapped through e3a91c07d5b48f26a0c7e314 and the cc of PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096).
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
| gcal | INT-11 | invitation mails | seeded: Brightwater call (Frederick, Robert, Arthur) and the Oct 6 review (Frederick) |
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
- referential: R08 (invitation mails vs calendar) — every seeded event has its invitation copies (evt_2f86b0d4c9e17a35b64e0d, evt_9c41e7a2d05b38f6e1a7c4).
- quantitative: Q01/Q03 — the seeded reply's root 73c2247f4a31f32d10b3068ecd1d13ac gets reply_count 1, reply_users_count 1, latest_reply 1759184040.552871 (companion UPDATE).
- state/lifecycle: L08 — ZOM-567 (Arthur, active_sep_2025_quiet_in_oct) is a Sep 30 ticket with a dated plan ("Will chase Thursday"); no acknowledgement required (new record, not a hazard example).
- identifier/format: I03 — seeded files use the roster address frederick.stone@harmonygames.co (not the frederick@ alias); I14 — the list f_48247af79428823c3cac92 is Resource-owned, read only.

## Intended disagreements

| Claim met first | Overturning record | Why realistic | Resolution |
|---|---|---|---|
| Paul Heydon "is in for $50K" (C07C2866011/1758303600.418207, f_6e1d93a0c4b72f85d39a0e) | no DocuSign Completed notice for Paul; nudge frederick.stone@harmonygames.co/1844610859008000037 (Sep 29) | founders post verbal yeses before docs; the template defines committed as signed | soft-circled $50,000 |
| Anton Bernstein $40K (same post, sheet) | frederick.stone@harmonygames.co/1844162278195200023 (Sep 24, $25K) and Completed notice frederick.stone@harmonygames.co/1844354293432320031 | angels trim checks | committed $25,000 |
| Dentsu "invites … out to all three" (frederick.stone@harmonygames.co/1844347876147200047, Sep 26) | ZOM-567 comment lc_b549f3057640a5eb08f7581e (Sep 30): Play track not added | Play internal tracks need the console owner (base C096HFA5Z8W/1758677722.184129) | iOS only |
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
FACT CHECK: PASS — 87 text-bearing rows, 3 declared facts, 5 declared superseded records
Errors: none
  note: line 104 4921f321db5d08f936aac24a6a1d2af8: superseded version, expected to differ — fact 'Anton Bernstein' is declared 25000 (amount); this row says '$50K' next to 'Anton Bernstein': "angel update: Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE. sending the docs through docusign next week. not a round "
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
| frederick.stone@harmonygames.co/1844318935449600041 | seeded | Edith Vane 2025-09-26T09:40Z: pass on the bridge (no firm name), cc PERSON_5282 | cc | overturning evidence (alias) |
| frederick.stone@harmonygames.co/1844347876147200047 | seeded | Leonard → Dentsu 2025-09-26T17:20Z: invites out to all three | cc | claim met first |
| frederick.stone@harmonygames.co/1844276782694400053 | seeded | Brightwater follow-up 2025-09-25T22:30Z + Ilse's reply 2025-09-26T15:05Z signed "Principal, Brightwater Games Fund" | cc | evidence (off-list firm) |
| evt_2f86b0d4c9e17a35b64e0d | seeded | "Ilse Marrow and Leonard Hayes" 2025-09-25T16:00–16:45Z | Frederick's calendar | evidence |
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

## Platform follow-ups

- ○ carriers to confirm in the Opus pre-check: Contacts `job` through contacts_search_contacts (e3a91c07d5b48f26a0c7e314); gslides notes on slide 9 (f_a47d0e2c95b18f63e2c0d5; the columns are also in the slide text and the hub).
- Trello comment rendering through trello_get_comments (68c64270d660c977c4696986) and Linear comments through linear_list_comments (ZOM-567; ● per Ask_Carriers §6b).
- Preflight digest: `01c_Preflight_Report.json` binds the SQL, solver, surface, manifest and dispositions by sha256; the optional manifest `preflight {report, digest}` field is not written, because the report hashes the whole manifest file and the field would stale it (recorded here instead).

## Self-review

Tool outputs (final run, verbatim):

```
schemas touched (10): contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 6, 'gdocs': 3, 'gsheets': 2, 'gslides': 36, 'slack': 5, 'trello': 11, 'gmail': 60, 'gcal': 6, 'linear': 3, 'contacts': 3}  total rows: 135  ops: {'insert': 129, 'update': 6}
errors: 0  warnings: 9
  warn  line 114: trello.trello_actions.date = 2025-09-14T04:20:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 118: trello.trello_cards.due = 2025-10-14T16:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 120: trello.trello_actions.date = 2025-09-27T17:05:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 132: trello.trello_actions.date = 2025-09-27T17:12:00Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 134: trello.trello_actions.date = 2025-09-27T17:30:24Z falls on a weekend (UTC) — business messages should be on weekdays
  warn  line 262: gcal.gcal_events.start_ts = 2025-10-06T16:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 262: gcal.gcal_events.end_ts = 2025-10-06T16:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 264: gcal.gcal_events.start_ts = 2025-10-06T16:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 264: gcal.gcal_events.end_ts = 2025-10-06T16:45:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```

Warning dispositions: weekend warn (Trello actions on Sat Sep 14 04:20Z = Fri Sep 13 9:20pm PT, and Sat Sep 27 17:05–17:30Z) — disposition: Leonard posts on weekends in the base (#bridge-pitch Sep 6–7 and Sep 28: C096HFA5Z8W/1757282790.636379); after the clock warn (trello due 2025-10-14, gcal Oct 6 review) — disposition: deadline and not-yet-happened event, plan fields only.

```
BASE CHECK (/injection A + C, static): PASS  — 129 inserts, 6 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
  note: trello.trello_check_items: no base-reference rules (checked by sql_lint only)
  note: trello.trello_checklists: no base-reference rules (checked by sql_lint only)
```

```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 28 load-bearing seeded ids for frederick_stone (7 in unscoped services = visible, 21 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (3 declared facts), 0 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 129 INSERTed rows (UPDATE companions not counted; 135 rows in all); need ≥ 120
  [ok] services_carrying_weight: 10 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 47 seeded ids cited; missing from SQL: none
  [ok] anchors: 1 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 14 fragments; need ≥ 12
  [ok] ask_fragment_services: 8 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 10 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 7 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 79; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 3 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 327; need ≥ 300
  [ok] call_budget: unconditional (verified) floor 502 of 502 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 500 (Long Horizon; plan ~600 for headroom)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 30% (≤ 50%)
  [ok] traps: 18 traps across 7 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 6 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (3 with versions in ≥ 2 services, 1 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 4 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 7 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 9 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 5 chains with 5 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 7 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 2 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 2 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 15 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 4 writes over 4 services; each must depend on findings
```

hg.py lint (eval hg_injection_lint, base data used): counts {"FAIL": 0, "CHECK": 0, "INFO": 0, "by_check": {}} sql /home/sumit/Desktop/OC/Task_Authoring/task_inputs/01_Universe_Inject.sql sha256 0b6812c56fe6876a — no FAIL or CHECK flag to disposition.

Preflight: `PREFLIGHT: PASS` (solver contract PASS, surface PASS, all 30 mutation results dispositioned in 01c_Dispositions.json, geometry U = 0.8841 > 0.15, L_max 0.5072 OK); mutation (verbatim tail):

```
  intervention:rule:FOLLOW           load-bearing    
  intervention:degrade:done1_over    no-injected-records
  intervention:degrade:input_over    no-injected-records
  intervention:degrade:done2_over    no-injected-records
  intervention:degrade:corr_over     no-injected-records
  intervention:degrade:alias_over    no-injected-records
  intervention:degrade:filt_over     no-injected-records
  intervention:degrade:follow_over   no-injected-records
  intervention:degrade:filt_miss     no-injected-records
  geometry: U = 0.8841 (61/69) · L_max = 0.5072 over ['rule:DONE1', 'rule:INPUT', 'rule:DONE2', 'rule:CORR', 'rule:ALIAS', 'rule:FILT']
    V3 cap 0.85: U PASS (needs > 0.15) · L_max OK
```

Forecast (UNCALIBRATED, pre-registered hev_4c8f05e25916f114): V3 E[avg] 0.715–0.737, P(all four difficulty gates) 0.078–0.351; channel rates for CH-FILT-HOMA 0.35 and CH-FILT-BRIGHT 0.50 are disclosed author overrides (no ledger records); text-graded slots (RP2, RP3, KW1, KW2) are not simulated, so losses are understated.

Checks A–C walk (Evals/0_Injection_Quality_Eval.md): inventory 129 INSERT + 6 UPDATE (sql_lint); Check A references, uniqueness over full collections, ownership/membership (Frederick in C096HFA5Z8W and C07C2866011; owner of d_5e8a1c3f9b07d2e64a1b93), id contracts — PASS (base_check, eval lint); Check B structure, literal JSON, generated/NOT NULL columns — PASS (sql_lint 0 errors, eval lint FAIL 0); Check C dates, parent/reply, counts — PASS (base_check), every seed before 2025-10-01T00:00Z; no PENDING item.

Touched-data census: listed above under "Touched-data census and coherence hazards".

| # | Category | Counter-reading (strongest case it fails) | Evidence | Verdict |
|---|---|---|---|---|
| 1 | temporal | Robert's reply says "this morning" but is posted 3:14pm PT | C096HFA5Z8W/1759184040.552871 | consistent: a morning call noted in the afternoon |
| 2 | semantic | "Sciplay" vs "SciPlay" reads as two firms | f_48247af79428823c3cac92, frederick.stone@harmonygames.co/1842285743246816270 | case variant of one name; register key follows the list |
| 3 | cross-service referential | Edith's pass names no firm, so it cannot be placed | e3a91c07d5b48f26a0c7e314, cc PERSON_5282 (frederick.stone@harmonygames.co/1842278425320449096) | resolvable through two persona-visible records |
| 4 | quantitative | Leonard's sheet still says Anton 40000, contradicting Anton's mail | f_6e1d93a0c4b72f85d39a0e (Sep 20) vs frederick.stone@harmonygames.co/1844162278195200023 (Sep 24) | dated stale tracker, later mail overturns (intended) |
| 5 | state/lifecycle | Leonard says Dentsu has invites; ZOM-567 says Play not added | frederick.stone@harmonygames.co/1844347876147200047, lc_b549f3057640a5eb08f7581e | dated human claim overturned by the later ticket comment |
| 6 | identifier/format | DocuSign link placeholder [IDENTIFIER_99011] is a new token | frederick.stone@harmonygames.co/1844354293432320031 | base links use [IDENTIFIER_n] placeholders (leonard@harmonygames.co_1774464522151433079.json); no identity meaning |
| 7 | other | the Paul nudge makes DONE1 trivially visible | frederick.stone@harmonygames.co/1844610859008000037 | a fair resolver is required (UGT); the post and sheet remain the first convincing sources |
| 8 | intended disagreement (Paul) | an unintended inconsistency between post and signing state | C07C2866011/1758303600.418207 | dated verbal claim vs later signing records; template defines committed |
| 9 | intended disagreement (Anton) | two amounts for one person in two services | frederick.stone@harmonygames.co/1844162278195200023 | later message from the investor himself |
| 10 | intended disagreement (Dentsu) | the mail and ticket are both system-like | ZOM-567 | both are human texts with dates (Leonard Sep 26, Arthur Sep 30) |
| 11 | intended disagreement (SciPlay) | Robert's note could be hearsay | C096HFA5Z8W/1759184040.552871 | the template makes written phone notes count |
| 12 | intended disagreement (Hiro) | list column vs mail | f_48247af79428823c3cac92 | the column states its own date (as of 09/11) |
| 13 | intended disagreement (templates) | two live templates with different rules | f_8d2c47a91e05b3f6d7c418 vs f_3b9e61c04d7a52e8f1a6c2 | different boards (Jul 16 vs Oct 14), the hub names the Oct 14 one |
| 14 | people status | Arthur quiet in Oct yet owns an open ticket | arthur.blake@harmonygames.co, ZOM-567 | ticket and comment dated Sep 30, before the clock |

Re-verified from source this session through tools/hg.py and the exports: list rows (f_48247af79428823c3cac92), SciPlay messages (gmail:threads/frederick@harmonygames.co_1842285743246816270.json /messages/1), T-Accelerate recap (/messages/0 of 1842283406259093714), Calendly note "here from T-Accelerate" (frederick.stone@harmonygames.co/1843625920612854647), Hiro Investment Director signature (leonard@harmonygames.co_1842278433020808799.json), ZOM-566 creation time, DocuSign notice shapes.

Unresolved: no independent (dual red-team) review — REDTEAM_* unset; forecast channel rates are author overrides (UNCALIBRATED); ○ carriers (Contacts job, slide notes) await confirmation in the Opus pre-check.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#0b6812c56fe6 · 01_Hardness_Manifest.json#93167bfbe4e8 · 01_Grounding_Dossier.md#7955cb8cabd3 · solver/solver.py#b3baca60e7a3 · 01c_Dispositions.json#189e9a7d4b76 · 01c_Preflight_Report.json#252c99bdbd61 · 00_Assigments.md#8ae66b700bc2 · 01_Scenario_Design.md#1e7246adb475 · 01_Hardness_Manifest.draft.json#2040a6821d42 · 01_Gradable_Surface.json#c052ab4dedcb · __context__#f1f763cb8cb4 · __assignment__#827e8afa884d · __policy__#dc4ab5df3cdd · __gate_policy__#f0c73a621309 · __review__#724c5240bc3b · blocking 0 · warnings 0 · checks 39
[PASS] assignment.v3_context: Frederick Stone / Co-founder; medium cap <85%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#1e7246adb475, 01_Hardness_Manifest.draft.json#2040a6821d42, 01_Gradable_Surface.json#c052ab4dedcb, 00_Assigments.md#8ae66b700bc2, __context__#f1f763cb8cb4, __assignment__#827e8afa884d, __policy__#dc4ab5df3cdd, __gate_policy__#f0c73a621309, __review__#103fcbd1ee53)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 11/12 items carry a source pointer (min 90%); unsourced e.g. L35: 'Frederick\'s GitHub login "Ryan" (S04) | not used | avoid'
[PASS] evidence.keyword: 10/10 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 13/13 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 129/129 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 21/21 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 9, rows 135
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 0b6812c56fe6 matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (weekend×4, clock×5)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 47 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 30 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.884 (61/69) vs 1 - cap 0.15 (V3 medium): PASS (bound PASS); re-run U 0.884 PASS (bound PASS)
[PASS] geometry.margin: L_max 0.5072463768115942 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (15 flag(s))
[PASS] forecast.preregistered: forecast hev_4c8f05e25916f114 pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 27 scoped load-bearing ids YES for frederick_stone
[PASS] structure.facts_declared: manifest declares 3 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 8 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 3 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (7 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 2 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 14 evidenced counter-readings (of 14 found; need ≥ 13) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] handoff.pasted: pasted into the Self-review by --paste
```
