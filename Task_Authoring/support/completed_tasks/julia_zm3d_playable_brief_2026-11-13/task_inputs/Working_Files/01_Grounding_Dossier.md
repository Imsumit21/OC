# Grounding Dossier — julia_zm3d_playable_brief · rev2 (design D3) · facts only, no prompt, OE or criterion text

**rev2 (2026-11-12).** This revision implements design D3 (`01_Scenario_Design.md` §14), after the pre-check and the six-run baseline of rev1 (`01a_Hardening_Report.md`). Four seeded records change and nothing is added: Robert's note to Julia `D05GU6L0XFH/1759178332.042459` replaces Claire's Turkish DM as the record on the bathroom redo; Marcus's post `C0880U9751A/1758906517.912099` loses the words of the note it corrects; Brian's log `f_faf4d7c167d14a1127dcc3` says 'The .wav exports.' instead of 'The sound files.' and records that Claire sent the three recoloured models again, so Cactus Plant, Chainsaw and Cone are Ready. Truth moves from 8 / 36 / 52 to 8 / 39 / 49. The rev1 SQL is kept in `Working_Files/run_forensics/rev1/` (with the bytes the platform ran in `submitted/`) and its design artifacts in `run_forensics/rev1/artifacts/`.

Written by `/create-injection` (Claude, authoring session). The SQL is `01_Universe_Inject.sql` (235 INSERT, 3 UPDATE, ten schemas). Linear and Slack rows come from the generator (`Working_Files/spec/spec.json`, rendered by `Task_Authoring/generators/render.py`); the other services from `Working_Files/plan/build_sql.py`. Universe: `Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)`; seed bound 2025-10-01T00:00:00Z. Every base fact below was read through `tools/hg.py` in this session or by the two reviewers' fact pack (`Working_Files/research/base_facts_D2.md`, record ids with each fact).

## 1.A Structural

| Table | Rows | Base location (pointer) | Base sample ids | Notes |
|---|---|---|---|---|
| slack.slack_messages | 6 INSERT, 1 UPDATE | `slack/messages/<channel>/<YYYY-MM>.json` (array of messages) | `C08R8CHB0QL/1758904025.123869`, `C08H78VJG80/1759226395.551469`, `C09ATAJ220H/1758905604.787929` | id = sha256(channel|ts)[:32]; ts with six decimals; created_at ISO with microseconds; the UPDATE sets the bow post's reply counters (generator convention slack.thread.counters) |
| linear.linear_issues | 97 | `linear/data.json` `/issues` (3,687 in base; 247 in the Design team) | `DES-312`, `DES-311`, `DES-307` | id = identifier = DES-n; `state_id` holds the state name (Done, In Progress, Todo); text ISO-Z stamps; `state_history_json` an empty JSON array; `time_in_status_minutes` NULL |
| linear.linear_comments | 96 | `linear/data.json` `/comments` (empty in base) | none in base; accepted injections carry them (generator convention linear.comment.shape) | uuid5 ids; `sequence` 1 per issue; `updated_at` = `created_at` |
| gdrive.drive_files | 5 | `gdrive/data.json` `/drive_files` | `d_8140f09bf9f1b94cb8ee2d`, `d_175c0d7bc72ed244b944cb`, `f_05bedd1540d3e01a90ab16` | `f_` + 22 hex; parents = the owner's root (`d_` + first 22 hex of the owner's contact id) |
| gdocs.docs_documents | 2 | `gdocs/data.json` `/docs_documents` | `f_05bedd1540d3e01a90ab16` | `body_text` non-empty; `style_runs_json` TITLE + NORMAL_TEXT; same id and sharing as the Drive row |
| gsheets.sheets_spreadsheets / sheets_sheets | 2 / 2 | `gsheets/data.json` `/sheets_spreadsheets/<n>/sheets/<m>/grid` | `f_7efae6c05be5c2414e8798` | one tab each; `grid_json` an array of rows |
| gslides.slides_presentations / pages / page_elements | 1 / 4 / 8 | `gslides/data.json` | shape taken from the accepted injection of `task_inputs-uselater` (same schema) | facts in element text, none in notes |
| gcal.gcal_events | 4 | `gcal/data.json` `/events` | `evt_257421bc09196edbf28758` | `calendar_id` = the owner's e-mail; one row per attendee calendar, shared `ical_uid` (32 hex @hg4), `self:true` on the owner's copy |
| gmail.gmail_threads / gmail_messages | 3 / 3 | `gmail/threads/<mailbox>_<thread>.json` | `claire@harmonygames.co_1831622960107831313.json` | ids `<mailbox>/<Message-ID>` and `<mailbox>/<numeric thread id>`; `internal_date` (ms) = `date` |
| trello.trello_actions; cards and boards (UPDATE) | 1 INSERT, 2 UPDATE | `trello/data.json` `/actions`, `/cards`, `/boards` | `688c4d14c312a27fa2747e5b`, `68c5a46ae3d49c189461e868` on card `688c4d14c312a27fa2747e40` | action id = 8 hex of the Unix second + 16 hex; `commentCard` data shape with `text`, `textData`, `card`, `board`, `list` |
| contacts.contacts | 1 | `contacts/contacts.json` `/contacts` | `fc22d5941b2aeb5c03ad32fa`, `175c0d7bc72ed244b944cb90` | 24 hex id; sparse row (job, email); `last_name` NOT NULL |

Column authority: `references/universe_schema_live.json` (NOT NULL columns of every table above are written; no generated column is written). Row shapes for Drive, Docs, Sheets, Slides, Calendar, Gmail, Trello and Contacts follow the accepted injection of `task_inputs-uselater/01_Universe_Inject.sql` and the base samples above; Linear and Slack shapes are the generator's, checked on the rendered bytes (`render.py`: grammar, parse-back, column types, overlay, invariants, sql_lint: 0 problems).

## 1.B Entity table

| Entity | Canonical spelling | Where it appears (ids) | Verdict |
|---|---|---|---|
| Julia Lawson (persona) | Julia Lawson · julia.lawson@harmonygames.co | Slack `EMPLOYEE_0005_SLACK_ID`; Linear `usr_8140f09bf9f1b94c` (member of team_ART, team_DES, team_ENG, team_ZOM); Drive root `d_8140f09bf9f1b94cb8ee2d`; Contacts `8140f09bf9f1b94cb8ee2dd7` | AGREE |
| Frederick Stone | Frederick Stone · frederick.stone@harmonygames.co | Slack `EMPLOYEE_0008_SLACK_ID`; Linear `usr_175c0d7bc72ed244` (team_ART and team_ENG, not team_DES: he opens no ticket in this task); Drive root `d_175c0d7bc72ed244b944cb`; DM `D05SD5QLG94` | AGREE; card SC-49 (founder status) not stated in any seeded text |
| Brian Foster | Brian Foster · brian.foster@harmonygames.co | Slack `EMPLOYEE_0026_SLACK_ID`; Linear `usr_fc22d5941b2aeb5c` (member of team_DES and team_ZOM; creator of `DES-304` to `DES-312` and of `ZOM-521`, `ZOM-566`); Drive root `d_fc22d5941b2aeb5c03ad32`; Contacts `fc22d5941b2aeb5c03ad32fa` | AGREE |
| Robert | Robert · robert@harmonygames.co | Slack `EMPLOYEE_0016_SLACK_ID`; Linear `usr_Robert` (hazard I10); Contacts `5f647df33ba6e92fbd56b05b` | AGREE; no surname in any service |
| Claire Morgan | Claire Morgan · claire.morgan@harmonygames.co | Slack `EMPLOYEE_0009_SLACK_ID`; Linear `usr_7fe31e7ec8199618`; DM with Julia `D05HMBQUC8Z`; GitHub author of `harmonygames-Games/match3d#462` | AGREE; a GitHub-only login 'Claire' also exists: Brian's notes say 'Claire', who on this game's art is Claire Morgan (fact_check warning, dispositioned in the Self-review) |
| Marcus Bennett | Marcus Bennett · marcus.bennett@harmonygames.co | Slack `EMPLOYEE_0002_SLACK_ID`; Linear `usr_c77c50cc15c5342d`; base post `C09ATAJ220H/1758905604.787929` | AGREE; two other Marcuses exist on the roster and post nowhere in this task |
| Calvin Price | Calvin Price · calvin.price@harmonygames.co | Slack `EMPLOYEE_0006_SLACK_ID`; Drive root `d_49b9dfa5208d400d9b3937`; Contacts `49b9dfa5208d400d9b3937ca`; base `C09A7PDFYCV/1755464752.078539` | AGREE |
| Leonard Hayes | Leonard Hayes · leonard.hayes@harmonygames.co | Trello `PERSON_6094_TRELLO_USER_ID` (creator of card `688c4d14c312a27fa2747e40`) | AGREE |
| Martin Walsh | Martin Walsh · martin.walsh@harmonygames.co | named once, on the Fonts ticket DES-409; Linear `usr_51f5f16d46e8cf55` | AGREE; a 'Martin Lewis' exists outside the studio and is not meant (fact_check warning, dispositioned) |
| PlayableX | PlayableX (the vendor) | Slack channel `C08H78VJG80`; staff `PERSON_6078_SLACK_ID`; masked in mail and calendar titles | DISAGREE (pre-existing, uneven masking): seeded text uses the Slack spelling; documented |
| PlayableX intake | intake@playablex.ai | Contacts `d7d31caf63ee33db2b7ed271` (seeded); no base row for the vendor (lookup, 0 hits for the address) | new role address; duplicates nobody |
| The pack ticket | DES-313 'Playable pack for PlayableX' | Linear `DES-313` and children DES-314 to DES-409 (seeded), in the Design team; base highest there is `DES-312` (7 May 2025) | AGREE; fourteen base tickets under `ZOM-97` share a title with a child (T19): the pack list's Ticket column and the team disambiguate |
| match3d#462 | Objects Revisions and Changes | GitHub `harmonygames-Games/match3d#462`, comment `harmonygames-Games/match3d#462#c_1`; Slack `C08R8CHB0QL/1758808937.107229`, `C090N54TG79/1759189466.554739` | AGREE (base, not modified) |
| The design page | ZM3D GDD | Confluence `page_zm3d_gdd` with comments `comment_zm3d_gdd_c1`, `comment_zm3d_gdd_c2` | AGREE; cards SC-8, SC-38, SC-58 concern other sentences of the page |

## 1.C Voice and realism (seeded speakers)

Seeded speakers and their `status_at_clock` (from `references/universe_kb/by_universe/synthcut/activity.json`, verified at the freeze):

- Frederick Stone <frederick.stone@harmonygames.co> (`EMPLOYEE_0008_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: the ask (Slack), the notes (Docs), the hold (Calendar) and its invitation mails, the contact.
- Brian Foster <brian.foster@harmonygames.co> (`EMPLOYEE_0026_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: the pack ticket, its children and the note on each (Linear), the pack list (Sheets), his log (Docs).
- Robert <robert@harmonygames.co> (`EMPLOYEE_0016_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: three Slack messages.
- Claire Morgan <claire.morgan@harmonygames.co> (`EMPLOYEE_0009_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: one DM to Julia.
- Marcus Bennett <marcus.bennett@harmonygames.co> (`EMPLOYEE_0002_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: one post in #zombie-match3d.
- Calvin Price <calvin.price@harmonygames.co> (`EMPLOYEE_0006_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: the sound sources sheet.
- Leonard Hayes <leonard.hayes@harmonygames.co>: activity.json status active_sep_2025_quiet_in_oct. Seeded: one Trello comment.
- Julia Lawson <julia.lawson@harmonygames.co> (`EMPLOYEE_0005_SLACK_ID`): activity.json status active_sep_2025_quiet_in_oct. Seeded: her deck (Slides), 23 Sep.

Voice, from base quotes (verbatim, with the export's own capitals):

| Author | Base quotes (ids) | Length, style, hours (UTC) | Seeded text follows it by |
|---|---|---|---|
| Frederick | 'Do you think it's fair to ask him to mock up screenshots he thinks could outperform our current set?' (`D05SD5QLG94/1756232330.990849`); 'lets go with Scenario 1. From a design standpoint, I think the main elements to figure out are 1) what items are on the board, and 2) what zombies are being smashed.' (`C08H78VJG80/1757956024.883249`); 'we are considering a pretty substantial pivot in core game play for Zombie Match.' (`C08H78VJG80/1759174925.309129`) | full sentences, American English, opens with the name; posts 13 to 23 UTC; his last base DM to Julia is 18 Sep | the ask is one paragraph of full sentences, sent 18:21 UTC after the call that fills 17:30 to 18:09 on his calendar (`evt_2204ffea306847eea6e5b0`); the notes and the hold are stamped before it |
| Brian | 'Since our zombies are made with 2D Unity animations, I’ve included the PSD files along with the animation and prefab files.' (`C08H78VJG80/1758717576.077489`); 'Sorry, it took a little while, I had to get help from our animator' (`C08H78VJG80/1758906043.375719`); 'Makes sense, I sent them the assets, but as far as I know, they haven’t started yet' (`C090N54TG79/1759141833.339099`) | short plain English in channels; active 06 to 21 UTC; Turkish in DMs | ticket notes of one to three short sentences; the log and the pack ticket's description in the same plain register; no note is in a DM |
| Robert | 'Let's also get a colorized versions of the cone:' (`C08R8CHB0QL/1758754866.994649`); 'Got new colored version of cactus, chainsaw and cones that can probably come in handy:' (`C090N54TG79/1759189466.554739`); 'I think we should remain as is' (`C090N54TG79/1758569885.985319`) | one or two casual sentences, sentence case; posts 14 to 07 UTC, none 09 to 12 | three short posts at 18:12, 21:41 and 17:31 UTC, each in a gap of his base traffic (re-check B3); in rev2 one note in his DM with Julia at 20:38 UTC on 29 Sep, before his base messages of 20:55 and 21:21, lower case, people tagged |
| Claire | 'Daha texture'lar final değil ama senin seti hazırlıyorum' (`D05HMBQUC8Z/1758555266.534569`); 'Kuzum yaparım tabi, pazartesi onu eklerim' (`D05HMBQUC8Z/1758300559.154229`); 'aa o da güzel fikirmiş bak aşlskdaşlkds' (`D05HMBQUC8Z/1758732588.831919`) | Turkish with English nouns, lower case, 'kuzum'; 06 to 18 UTC; English in channels | no seeded text in rev2 (the rev1 Turkish message is removed); she is tagged in Robert's note and in Marcus's post, and named in Brian's notes and log |
| Marcus | 'yah alright i can export them zombies!' (`C09ATAJ220H/1758883570.104439`); 'i've included packages, an instalation text with what you need to do. and a video on how to play the animations. I've tested it in an empty project myself' (`C09ATAJ220H/1758905604.787929`); 'the fbx export seetings need to be set on meters.' (`C0880U9751A/1738678859.796159`) | lower case, loose spelling, no apostrophes; 97 % of posts 08 to 17 UTC | one lower-case post without apostrophes at 17:08 UTC, fifteen minutes after his pack post of 16:53 |
| Leonard | 'For the playable - should we pause the effort if they haven’t started yet?' (`C090N54TG79/1759114097.776589`); 'I’m worried that we pivot the core game and then playable dev money will be wasted.' (`C090N54TG79/1759114127.213749`) | short, direct; 14 to 07 UTC | a three-sentence Trello comment at 20:05 UTC |
| Calvin | 'I used the sample you gave me and increased and lower the pitch, would you need more or 10 are okay?' (`C09A7PDFYCV/1755464752.078539`); 'can you help me vote which soundtrack you think fits better for endless mode?' and, on its next line, 'I'm open for any suggestions, it's AI generated' (`C05KNDCHAAG/1755195783.942099`) | plain, practical; 13 to 01 UTC | sheet cells of a few words each |

Conventions used (`references/universe_kb/by_universe/synthcut/conventions.json`): `slack.per_person_hours_and_style` and `slack.length_chars_by_channel_type` for message length and hours; `linear.title_prefixes_by_team` (Design-team titles carry no prefix in 238 of 247 cases, and Brian's own `DES-311` and `DES-312` are titled 'Chapter 14' and 'Chapter 15' under a parent: the children are titled with the line's name, as the object tickets under `ZOM-97` are); `linear.priority_by_team` (priority 0, as on Brian's own Design tickets `DES-304` to `DES-312`); `gcal.duration_min` (30 minutes) and `gcal.summary_patterns_top`; `gmail.subject_patterns_top` ('Invitation: … @ …'). Ticket notes carry jittered seconds; no seeded time falls on a round minute by rule.


## 1.D Keyword

Base sweep of the seeded wording (`plan/literal_sweep.py`, eleven services, `tools/hg.py search-many`; output kept in `Working_Files/plan/out/literal_sweep.txt`). A term with no base hit is new and is reached through an anchor; a term with base hits lists one.

| Term | Base | Seeded in | Reached via |
|---|---|---|---|
| hand-off notes | NEW TERM — 0 base hits | the ask `7e84f1cf59f8e95fef961268fbf37cc1`, the notes `f_8c1d0bca1d1d5fde4c5008` | anchor A1 (the ask names them); a Docs or Drive search for the words |
| pack list | 2 unrelated Slack hits of 2024 (e.g. `D0770ET1HV2/1720174256.332539`, about a puzzle pack list) and one pull-request body | the ask, the sheet `f_956e60ec7f2f7977d98934` titled 'ZM3D playable - pack list' | anchor A1; a Drive search for 'pack list' |
| playable pack | NEW TERM — 0 base hits | the pack ticket DES-313 | the pack list's Ticket column; the notes ('Brian's pack ticket') |
| 8-item | 1 base hit, the vendor's own message `C08H78VJG80/1758022459.227279` | Robert's post `da6776f77288224ec67847a799bbde5a` ('the 8') | a search for the playable in #zombie-design |
| the text kind | 1 unrelated base hit in a DM of May 2025 (`D07G5QWT20K`) | Marcus's post `a5ee6e90923eeab380e6730f674240d2` | reading #zombie-match3d `C0880U9751A` for the week |
| redoing the UVs | NEW TERM — 0 base hits | Robert's note `8a1b1c6d448eecb7ccc81f796c95d5ce` | reading Julia's DM with Robert `D05GU6L0XFH` around 29 Sep; a Slack search for 'bathroom' also returns it among 57 visible base messages (no rev1 run searched the word) |
| three recoloured models | NEW TERM — 0 base hits | Brian's log `f_faf4d7c167d14a1127dcc3` | a Drive or Docs search for the outgoing folder; which three is in Robert's base post |
| .wav exports | NEW TERM — 0 base hits | Brian's log `f_faf4d7c167d14a1127dcc3` | the same log (rev1's 'The sound files.' made a search for 'sound' list it) |
| in place of the last one on my list | NEW TERM — 0 base hits | Robert's reply `1d55b38831d7517fe403e4f2a906a897` | `slack_read_thread` on Julia's bow post `C08R8CHB0QL/1758904025.123869` |
| won't unpack | NEW TERM — 0 base hits | Brian's log `f_faf4d7c167d14a1127dcc3` | a Drive or Docs search for the outgoing folder |
| outgoing folder | NEW TERM — 0 base hits | every exported line's note (DES-314 to DES-409), the notes, Brian's log | the ticket notes; the notes' Ready test |
| sound sources | NEW TERM — 0 base hits | Calvin's sheet `f_b2387e31d46d3a7b3fa2a9` | a Drive or Sheets search for sound |
| intake@ | NEW TERM — 0 base hits | the contact `d7d31caf63ee33db2b7ed271` | the notes name Contacts |
| kickoff | base card `688c4d14c312a27fa2747e40` 'Playable Kickoff' | the hold `evt_421695d009e589ee85296c`, Leonard's comment `68dc381b75aff34acf5a5424` | the notes name the kickoff hold; a calendar search for the playable or for 3 Nov |

## 1.E Persona reach

`persona_view.py check-sql julia_lawson 01_Universe_Inject.sql --load-bearing Working_Files/01c_load_bearing_ids.txt` (verbatim):

```
CHECK-SQL as julia_lawson <julia.lawson@harmonygames.co>
[YES LB] L6 gdrive.drive_files insert f_8c1d0bca1d1d5fde4c5008 - file is shared with the persona (shared_with_emails)
[YES LB] L9 gdrive.drive_files insert f_956e60ec7f2f7977d98934 - file is shared with the persona (shared_with_emails)
[YES LB] L11 gdrive.drive_files insert f_b2387e31d46d3a7b3fa2a9 - file is shared with the persona (shared_with_emails)
[YES LB] L13 gdrive.drive_files insert f_6a2fa8e61b31139ca8e3d4 - persona owns the file
[YES LB] L15 gdrive.drive_files insert f_faf4d7c167d14a1127dcc3 - file is shared with the persona (shared_with_emails)
[YES LB] L17 gdocs.docs_documents insert f_8c1d0bca1d1d5fde4c5008 - file is shared with the persona (shared_with_emails)
[YES LB] L20 gdocs.docs_documents insert f_faf4d7c167d14a1127dcc3 - file is shared with the persona (shared_with_emails)
[YES LB] L22 gsheets.sheets_spreadsheets insert f_956e60ec7f2f7977d98934 - file is shared with the persona (shared_with_emails)
[YES LB] L25 gsheets.sheets_sheets insert f_956e60ec7f2f7977d98934, f_956e60ec7f2f7977d98934#0 - file is shared with the persona (shared_with_emails)
[YES LB] L27 gsheets.sheets_spreadsheets insert f_b2387e31d46d3a7b3fa2a9 - file is shared with the persona (shared_with_emails)
[YES LB] L29 gsheets.sheets_sheets insert f_b2387e31d46d3a7b3fa2a9, f_b2387e31d46d3a7b3fa2a9#0 - file is shared with the persona (shared_with_emails)
[YES LB] L31 gslides.slides_presentations insert f_6a2fa8e61b31139ca8e3d4 - persona owns the file
[YES LB] L34 gslides.slides_pages insert f_6a2fa8e61b31139ca8e3d4, slide_f9b479c24b7b - persona owns the file
[YES LB] L36 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_c5c63f51d806, slide_f9b479c24b7b - persona owns the file
[YES LB] L38 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_829ffaef8aab, slide_f9b479c24b7b - persona owns the file
[YES LB] L40 gslides.slides_pages insert f_6a2fa8e61b31139ca8e3d4, slide_0e3a07bbbcdd - persona owns the file
[YES LB] L42 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_40c443410200, slide_0e3a07bbbcdd - persona owns the file
[YES LB] L44 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_bccaace88002, slide_0e3a07bbbcdd - persona owns the file
[YES LB] L46 gslides.slides_pages insert f_6a2fa8e61b31139ca8e3d4, slide_70fbd773b799 - persona owns the file
[YES LB] L48 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_d80b1de7a1b7, slide_70fbd773b799 - persona owns the file
[YES LB] L50 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_23bcd0034408, slide_70fbd773b799 - persona owns the file
[YES LB] L52 gslides.slides_pages insert f_6a2fa8e61b31139ca8e3d4, slide_97402415f9e1 - persona owns the file
[YES LB] L54 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_3ab2af2a0848, slide_97402415f9e1 - persona owns the file
[YES LB] L56 gslides.slides_page_elements insert f_6a2fa8e61b31139ca8e3d4, el_9ea4f88ee342, slide_97402415f9e1 - persona owns the file
[YES LB] L58 slack.slack_messages insert a5ee6e90923eeab380e6730f674240d2, C0880U9751A/1758906517.912099 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-match3d
[YES LB] L60 slack.slack_messages insert 1d55b38831d7517fe403e4f2a906a897, C08R8CHB0QL/1758922879.243189 - persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art
[YES LB] L61 slack.slack_messages insert da6776f77288224ec67847a799bbde5a, C090N54TG79/1758823946.262829 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L62 slack.slack_messages insert 0b7f656a96c5cc50d1f6924e089bf8ba, C090N54TG79/1759167068.371289 - persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] L63 slack.slack_messages insert 8a1b1c6d448eecb7ccc81f796c95d5ce, D05GU6L0XFH/1759178332.042459 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05GU6L0XFH
[YES LB] L64 slack.slack_messages insert 7e84f1cf59f8e95fef961268fbf37cc1, D05SD5QLG94/1759256494.852159 - persona EMPLOYEE_0005_SLACK_ID is in members of im D05SD5QLG94
[YES LB] L65 slack.slack_messages update 088b096edb82a130771a5da3344bcef1, C08R8CHB0QL/1758904025.123869 - persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art
[YES] L265 gcal.gcal_events insert evt_d622b6ab55401d23626674 - persona is an attendee and holds its own copy evt_421695d009e589ee85296c (same ical_uid and start) on julia.lawson@harmonygames.co
[YES LB] L268 gcal.gcal_events insert evt_421695d009e589ee85296c - event is on the persona's own calendar julia.lawson@harmonygames.co
[YES] L270 gcal.gcal_events insert evt_a78612f3eaf04ce8461eb4 - persona is an attendee and holds its own copy evt_421695d009e589ee85296c (same ical_uid and start) on julia.lawson@harmonygames.co
[YES] L272 gcal.gcal_events insert evt_1c99b11a66cfd562b13d9c - persona is an attendee and holds its own copy evt_421695d009e589ee85296c (same ical_uid and start) on julia.lawson@harmonygames.co
[YES] L274 gmail.gmail_threads insert julia.lawson@harmonygames.co/1844707828171527310 - row user_email is the persona (julia.lawson@harmonygames.co)
[YES] L277 gmail.gmail_messages insert julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>, j - row user_email is the persona (julia.lawson@harmonygames.co)
[NO] L279 gmail.gmail_threads insert brian.foster@harmonygames.co/1844707828171705300 - row is in mailbox brian.foster@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L281 gmail.gmail_messages insert brian.foster@harmonygames.co/<calendar-c94e8bd4-a0ec-0177-cb05-b68828195e96@google.com>, b - row is in mailbox brian.foster@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L283 gmail.gmail_threads insert robert@harmonygames.co/1844707828171004856 - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[NO] L285 gmail.gmail_messages insert robert@harmonygames.co/<calendar-4263dbb8-cab6-41a8-95c1-dca6f6f7e53b@google.com>, robert@ - row is in mailbox robert@harmonygames.co, not the persona's (julia.lawson@harmonygames.co)
[YES LB] base slack C0880U9751A - base record: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-match3d
[YES LB] base slack C08H78VJG80 - base record: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1744637266.363689 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1757695108.506159 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1757956024.883249 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1758022459.227279 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1758283671.878269 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1758717576.077489 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1758717625.209649 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1758729487.922339 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1758906043.375719 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1759140968.965099 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08H78VJG80/1759226395.551469 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private [SOURCE_ORG_0001]-playablex
[YES LB] base slack C08R8CHB0QL/1758752145.583769 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art
[YES LB] base slack C08R8CHB0QL/1758754866.994649 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art
[YES LB] base slack C08R8CHB0QL/1758808937.107229 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of public zombie-art
[YES LB] base slack C090N54TG79/1759189466.554739 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zombie-design
[YES LB] base slack C09ATAJ220H/1758905604.787929 - base record: thread reply inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of private zm-animations
[YES LB] base slack D05GU6L0XFH - base record: persona EMPLOYEE_0005_SLACK_ID is in members of im D05GU6L0XFH
[YES LB] base slack D05SD5QLG94 - base record: persona EMPLOYEE_0005_SLACK_ID is in members of im D05SD5QLG94
[YES LB] base slack D05SD5QLG94/1758220925.518329 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of im D05SD5QLG94
[YES LB] base slack D076RBM29JS/1758638743.317009 - base record: message inherits channel: persona EMPLOYEE_0005_SLACK_ID is in members of im D076RBM29JS
[YES LB] base gdrive d_8140f09bf9f1b94cb8ee2d - base record: persona owns the file
[YES LB] base gdrive f_05bedd1540d3e01a90ab16 - base record: file is shared with the persona (shared_with_emails)

summary: {'YES': 37, 'NO': 4}  unscoped rows (always visible): 197
  gcal.gcal_events: {'YES': 4}
  gdocs.docs_documents: {'YES': 2}
  gdrive.drive_files: {'YES': 5}
  gmail.gmail_messages: {'YES': 1, 'NO': 2}
  gmail.gmail_threads: {'YES': 1, 'NO': 2}
  gsheets.sheets_sheets: {'YES': 2}
  gsheets.sheets_spreadsheets: {'YES': 2}
  gslides.slides_page_elements: {'YES': 8}
  gslides.slides_pages: {'YES': 4}
  gslides.slides_presentations: {'YES': 1}
  slack.slack_messages: {'YES': 7}
verdict: PASS (0 load-bearing rows not visible)
```

Reach path per scoped load-bearing record:

| Record | Service class | Visibility path |
|---|---|---|
| `D05SD5QLG94/1759256494.852159` LB | Slack DM | Julia is one of the two members of `D05SD5QLG94` |
| `D05GU6L0XFH/1759178332.042459` LB | Slack DM | Julia is one of the two members of `D05GU6L0XFH` |
| `C090N54TG79/1758823946.262829` LB, `C090N54TG79/1759167068.371289` LB | Slack public channel | member of #zombie-design `C090N54TG79` |
| `C08R8CHB0QL/1758922879.243189` LB | Slack public channel, thread reply | member of #zombie-art `C08R8CHB0QL`; the parent `C08R8CHB0QL/1758904025.123869` is her own post |
| `C0880U9751A/1758906517.912099` LB | Slack private channel | member of #zombie-match3d `C0880U9751A` (can-see YES; six posts of hers that week) |
| `f_8c1d0bca1d1d5fde4c5008` LB, `f_956e60ec7f2f7977d98934` LB, `f_b2387e31d46d3a7b3fa2a9` LB, `f_faf4d7c167d14a1127dcc3` LB | Drive files | shared with julia.lawson@harmonygames.co as reader (`shared_with_emails_json`) |
| `f_6a2fa8e61b31139ca8e3d4` LB | Drive file | owned by Julia |
| `evt_421695d009e589ee85296c` LB | Calendar | the copy on Julia's calendar, `self:true` |
| `julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>` | Gmail | her own mailbox copy, INBOX (a companion, not load-bearing) |
| `C08H78VJG80` LB (base hub channel) | Slack private channel | member (can-see YES) |

Unscoped services (always visible to the persona): Linear (DES-313 and its children), Trello (`68dc381b75aff34acf5a5424`), Contacts (`d7d31caf63ee33db2b7ed271`), GitHub (`harmonygames-Games/match3d#462`), Confluence (`page_zm3d_gdd`). The four NO rows of the check are the invitation copies in Brian's and Robert's mailboxes: companions of the hold, not evidence. No designed denial and no UNVERIFIED record is load-bearing.

## 1.F Collision

Identity tokens: no new person is created; the one new contact is a role address with no Slack, Linear or Gmail identity, and no masking token is used in any seeded text. Minted ids against the full collections (`plan/check_ids.py`, `tools/hg.py search lookup`, verbatim):

```
linear issues    ids  97 hits 0 scan_complete=True 
linear comments  ids  96 hits 0 scan_complete=True 
drive files      ids   5 hits 0 scan_complete=True 
gcal events      ids   1 hits 0 scan_complete=True 
trello actions   ids   1 hits 0 scan_complete=True 
contacts         ids   1 hits 0 scan_complete=True 
slack message ids ids   6 hits 0 scan_complete=True 
minted slack: {'D05SD5QLG94/1759256494.852159': '7e84f1cf59f8e95fef961268fbf37cc1', 'C090N54TG79/1758823946.262829': 'da6776f77288224ec67847a799bbde5a', 'C090N54TG79/1759167068.371289': '0b7f656a96c5cc50d1f6924e089bf8ba', 'C0880U9751A/1758906517.912099': 'a5ee6e90923eeab380e6730f674240d2', 'D05GU6L0XFH/1759178332.042459': '8a1b1c6d448eecb7ccc81f796c95d5ce', 'C08R8CHB0QL/1758922879.243189': '1d55b38831d7517fe403e4f2a906a897'}
```

Slack `(channel, ts)` pairs are unique in their channel-month files (generator invariant S3 and the lookup above). Linear: the Design team's highest base number is `DES-312` (created 2025-05-07T19:31:13Z, `conventions.json` linear.max_number); `DES-313` to `DES-409` are free and follow it in number and in date. The invitation mails' Message-IDs and thread ids are minted from the hold's key and each mailbox and collide with nothing (`base_check` Check A: PASS).

## Record ledger

| # | Service | Table(s) | Id | Container | Manifest element | Carrier | Reach path | Discovery role |
|---|---|---|---|---|---|---|---|---|
| 1 | slack | slack_messages | `D05SD5QLG94/1759256494.852159` | `D05SD5QLG94` | anchor A1; fragments K13, K16 | ● text | DM member | first link (hub) |
| 2 | gdocs + gdrive | docs_documents, drive_files | `f_8c1d0bca1d1d5fde4c5008` | Frederick's Drive root `d_175c0d7bc72ed244b944cb` | authority H1; fragment K1 | ● body_text | shared reader | connecting (the rules) |
| 3 | gsheets + gdrive | sheets_spreadsheets, sheets_sheets, drive_files | `f_956e60ec7f2f7977d98934` | Brian's Drive root `d_fc22d5941b2aeb5c03ad32` | authority H2; fragment K2; cohort definition | ● grid | shared reader | connecting (the line set) |
| 4 | linear | linear_issues | `DES-313` | team DES (Design) | fragment K4 (destination) | ● title, description | unscoped | connecting; write target's parent |
| 5 | linear | linear_issues | `DES-314` … `DES-409` (96) | children of DES-313 | cohort (one per line) | ● title, state | unscoped | evidence carrier; write targets |
| 6 | linear | linear_comments | 96 notes, one per child (e.g. `5980046f-e4a3-56f0-8f18-f6554227011d` on DES-367) | the child tickets | cohort evidence surface 1; traps T1, T2, T3, T7 | ● comment body (Ask_Carriers §6b) | unscoped | evidence; claims met first |
| 7 | slack | slack_messages | `C090N54TG79/1758823946.262829` | #zombie-design `C090N54TG79` | fragment K3; trap T5 (older version) | ● text | channel member | connecting; claim met first |
| 8 | slack | slack_messages | `C090N54TG79/1759167068.371289` | #zombie-design `C090N54TG79` | fragment K10 | ● text | channel member | connecting |
| 9 | slack | slack_messages (+ UPDATE of the parent's counters) | `C08R8CHB0QL/1758922879.243189` | thread under `C08R8CHB0QL/1758904025.123869` in #zombie-art | fragment K11; chain C4; trap T5 (overturning) | ● thread reply text | channel member | overturning |
| 10 | slack | slack_messages | `C0880U9751A/1758906517.912099` | #zombie-match3d `C0880U9751A` | chain C1; trap T1 (overturning) | ● text | channel member | overturning |
| 11 | slack | slack_messages | `D05GU6L0XFH/1759178332.042459` | `D05GU6L0XFH` | chain C2; trap T2 (overturning) | ● text | DM member | overturning |
| 12 | gsheets + gdrive | sheets_spreadsheets, sheets_sheets, drive_files | `f_b2387e31d46d3a7b3fa2a9` | Calvin's Drive root `d_49b9dfa5208d400d9b3937` | chain C5; trap T4 (overturning) | ● grid | shared reader | overturning |
| 13 | gdocs + gdrive | docs_documents, drive_files | `f_faf4d7c167d14a1127dcc3` | Brian's Drive root `d_fc22d5941b2aeb5c03ad32` | chain C6; trap T7 (overturning) | ● body_text | shared reader | overturning |
| 14 | gslides + gdrive | slides_presentations, slides_pages, slides_page_elements, drive_files | `f_6a2fa8e61b31139ca8e3d4` | Julia's Drive root `d_8140f09bf9f1b94cb8ee2d` | fragment K9; traps T14, T15 (older state of the board) | ● element text | owner | claim met first |
| 15 | gcal | gcal_events | `evt_421695d009e589ee85296c` and three more copies (`evt_d622b6ab55401d23626674`, `evt_a78612f3eaf04ce8461eb4`, `evt_1c99b11a66cfd562b13d9c`) | the four attendees' calendars | authority H3; fragment K7 | ● summary, start, attendees | attendee | connecting (recipients) |
| 16 | gmail | gmail_threads, gmail_messages | `julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>` and the copies in Brian's and Robert's mailboxes | three mailboxes | companion of the hold (INT-11) | ● subject, body | own mailbox (Julia's copy) | companion |
| 17 | contacts | contacts | `d7d31caf63ee33db2b7ed271` | Contacts | fragment K8 | ● email | unscoped | connecting (recipient) |
| 18 | trello | trello_actions (+ UPDATE of card badges and dateLastActivity, board dateLastActivity) | `68dc381b75aff34acf5a5424` | card `688c4d14c312a27fa2747e40` | authority H3's decoy; trap T11 | ● comment text | unscoped | decoy |

Every injected row maps to one of the eighteen entries above (`plan/out/sql_ids.json` lists the rows per table); no row exists only to raise a count. The six Slack rows and the 193 Linear rows are generated from `Working_Files/spec/spec.json`.

## Findability, discovery order, hidden-authority proofs

```
Record:               slack.slack_messages · D05SD5QLG94/1759256494.852159
Agent's likely query: the DM with Frederick, newest first (slack_read_channel or conversations_history)
Term present:         the message is the newest of the DM (last base message 18 Sep)
Competing base hits:  0 newer; 36 base messages in the DM since July
Chain position:       first link
```

```
Record:               gdocs.docs_documents · f_8c1d0bca1d1d5fde4c5008
Agent's likely query: "hand-off notes" via gdocs_search_documents or gdrive_search
Term present:         title 'ZM3D playable: hand-off notes'
Competing base hits:  0 (NEW TERM); the decoy 'Playable Feedback' answers a search for 'playable'
Chain position:       connecting; authority H1
```

```
Record:               gsheets.sheets_spreadsheets · f_956e60ec7f2f7977d98934
Agent's likely query: "pack list" via gdrive_search or gsheets_search_spreadsheets
Term present:         title 'ZM3D playable - pack list'
Competing base hits:  0 sheets with that title
Chain position:       connecting; authority H2
```

```
Record:               linear.linear_issues · DES-313
Agent's likely query: the Ticket column of the pack list; linear_get_issue, then linear_list_issues(parentId)
Term present:         every child key is in the pack list's rows
Competing base hits:  the 51 object tickets under ZOM-97 share titles, not keys
Chain position:       connecting
```

```
Record:               linear.linear_comments · one per child (DES-314 to DES-409)
Agent's likely query: linear_list_comments(issueId) per ticket
Term present:         the notes say 'Brian's note on each ticket says what he did with the line'
Competing base hits:  base holds no Linear comment at all
Chain position:       evidence (per line)
```

```
Record:               slack.slack_messages · C090N54TG79/1758823946.262829 and C090N54TG79/1759167068.371289
Agent's likely query: "playable" or "PlayableX" in #zombie-design
Term present:         both posts carry the word
Competing base hits:  the 22 Sep playable thread and Leonard's 29 Sep posts in the same channel
Chain position:       connecting
```

```
Record:               gcal.gcal_events · evt_421695d009e589ee85296c
Agent's likely query: "kickoff" via a calendar search, or events on 3 Nov
Term present:         summary 'ZM3D playable kickoff with PlayableX'
Competing base hits:  more than forty base events have 'Kickoff' in the title (art and feature kickoffs); none is on 3 Nov 2025 and none names the playable or the vendor ('2025-11-03', 'PlayableX', 'playable': 0 hits in the calendar export); the Trello card 'Playable Kickoff' answers the same word in Trello
Chain position:       connecting; authority H3
```

```
Record:               contacts.contacts · d7d31caf63ee33db2b7ed271
Agent's likely query: "PlayableX" via a contacts search
Term present:         first name 'PlayableX', job 'Project intake (playable ads)'
Competing base hits:  no other PlayableX contact
Chain position:       connecting
```

**Dynamic-change seeds** (claim met first · overturned by · why met first · why decisive):

| Seed | Claim met first | Overturned by | Why the claim is met first | Why the later record decides |
|---|---|---|---|---|
| EXPORT | Brian's note on twelve tickets, e.g. DES-367: FBX saved out of the project, opens, looks right | `C0880U9751A/1758906517.912099` (Marcus, 26 Sep 17:08 UTC) | the note is on the line's own ticket, which every run reads | the vendor takes binary FBX only (base) and the notes let a later word from someone who knows the file count; the post holds no word of the ask and no line name (path exposure: OFF-PATH) |
| ARTHOLD | Brian's note on twelve Bathroom tickets, e.g. DES-349 | `D05GU6L0XFH/1759178332.042459` (Robert, 29 Sep 20:38 UTC) | same | someone who follows the art, later, in Julia's DM with him; the artist is tagged, not named (OFF-PATH) |
| REVISED | Robert's base post `C090N54TG79/1759189466.554739` (29 Sep 23:44 UTC): new colour versions of the cactus, the chainsaw and the cones, after their 25 Sep files; the notes send a changed file again | `f_faf4d7c167d14a1127dcc3` (Brian's log, 30 Sep): Claire sent the three recoloured models again, they open and look right | the post sits in #zombie-design next to Robert's picks; every rev1 run read it | the latest record; it says Ready, and only Robert's post says which three (OFF-PATH: the entry names no line) |
| ZIP | Brian's note on eight instrument tickets, e.g. DES-380: zipped, in the outgoing folder | `f_faf4d7c167d14a1127dcc3` (Brian's log, 30 Sep 09:12 UTC) | same | his own later statement; the notes make 'sitting in the outgoing folder, it opens' part of Ready (OFF-PATH) |
| AUDIO | Brian's note on DES-402 and DES-403: exported .wav, plays | `f_b2387e31d46d3a7b3fa2a9` (Calvin's sheet) | same | the notes hand over only sound that is ours; the sheet marks both 'no' (OFF-PATH) |
| PICKS | `C090N54TG79/1758823946.262829` (Robert's eight, 25 Sep) | `C08R8CHB0QL/1758922879.243189` (his reply, 26 Sep 21:41 UTC) | a search for the playable in #zombie-design returns the 25 Sep post | same person, later; the ask keeps his latest word (OFF-PATH: the reply names no item) |

**Hidden authorities.** H1: a search for 'hand-off notes' returns `f_8c1d0bca1d1d5fde4c5008`; the decoy is Leonard's 'Playable Feedback' (`f_05bedd1540d3e01a90ab16`), about the first playable. H2: a search for 'pack list' returns `f_956e60ec7f2f7977d98934`; the decoy is the vendor's asset list `C08H78VJG80/1758283671.878269`, which names groups, not lines. H3: a calendar search for 'kickoff' returns `evt_421695d009e589ee85296c` among older events with that word in the title, and it is the only one that names the playable or falls on 3 Nov; the decoy is the Trello card `688c4d14c312a27fa2747e40` with Leonard's comment `68dc381b75aff34acf5a5424`, which has no attendees.

`path_exposure.py check --write` (verbatim):

```
PATH EXPOSURE (prompt stage, 6 unit(s)): PASS
[PASS] exposure.bound: 5 file(s) hashed: 01_Universe_Inject.sql, 04_Prompt.txt, Working_Files/01_Difficulty_Budget.json, Working_Files/01_Gradable_Surface.json, Working_Files/01_Hardness_Manifest.json
[PASS] exposure.sources: keywords and named containers come from 04_Prompt.txt, the anchors' prompt_reference names and the cohort entity names; 97 name keyword(s), 52 path record(s), 1 fragment(s) or authority(ies) held back as a decider's own fairness entry
[PASS] exposure.base: base data read as julia_lawson; data clock 2025-10-01T07:00:00Z
[PASS] exposure.units: all 5 anchor/variance unit(s) are OFF-PATH
[PASS] exposure.unit.A1: OFF-PATH (anchor; doc_body f_faf4d7c167d14a1127dcc3): no condition applies (notes: 'music' (one word of 'Background music' (a cohort entity name)) is in the record; not counted because the search could not be run)
[PASS] exposure.unit.A2: OFF-PATH (anchor; slack_root D05GU6L0XFH/1759178332.042459): no condition applies (notes: 'Bathroom' (one word of 'Bathroom Scale' (a cohort entity name)) is in the record but is a common word here (58 results): not counted)
[PASS] exposure.unit.C1: OFF-PATH (variance; slack_root C0880U9751A/1758906517.912099): no condition applies
[PASS] exposure.unit.C2: OFF-PATH (variance; file f_b2387e31d46d3a7b3fa2a9): no condition applies (notes: 'sound' (one word of 'Explosion sound' (a cohort entity name)) is in the record; not counted because the search could not be run)
[PASS] exposure.unit.C3: OFF-PATH (variance; slack_reply C08R8CHB0QL/1758922879.243189): no condition applies (notes: 'Item' (one word of 'Item visuals' (a cohort entity name)) is in the record but is a common word here (3646 results): not counted | allowed fairness pointer: K11 from 7e84f1cf59f8e95fef961268fbf37cc1 says "unless he's changed them since" and names no container)
[SKIP] exposure.unit.R1: realism unit: not checked
[PASS] exposure.rules: rules applied: window = 7 days before the earliest dated anchor, anchor A1 (2025-09-30); searched senders = none; the full rule text is under `rules` in --json and in the tool's RULES
```

## Self-validation table

| QC category | Tool-enforced (result) | Manual (evidence) |
|---|---|---|
| Missing Universe Data | — | every needed fact is in a record Julia can open (1.E) and a cataloged tool returns it: `slack_read_channel`, `slack_read_thread`, `linear_list_comments`, `gsheets_values_get`, `gdocs_get_document_text`, `github_get_pull_request_comments`, `gcal` and `contacts` reads; no tool is killed (Friction: none) |
| Temporal Field | sql_lint 0 errors; base_check Check C PASS; generator invariants L1 to L12, S1 to S11 PASS | dates in text agree with the fields: 'Thu 25 Sep', 'Fri 26 Sep', 'Mon 29 Sep' in notes stamped on those days (`plan/out/note_times.json`); the zombie ticket's note (29 Sep 10:21 UTC) follows the vendor's review message `C08H78VJG80/1759140968.965099`; Brian's log line of 30 Sep follows the pause `C08H78VJG80/1759174925.309129`; no record cites a later one |
| Cross-service Referential | base_check Check A PASS (channels, users, issues, calendars, cards, parents resolve) | the pack list's Ticket column equals the child keys (DES-314 to DES-409); the hold's attendees equal the invitation's guests; Docs, Sheets and Slides sharing equals the Drive rows |
| Quantitative / Reconciliation | Slack reply counters updated by the generator; Trello badge counts 1 comment | the pack list has 96 rows and DES-313 has 96 children; truth counts 8 / 39 / 49 come from `solver/truth.json` |
| State / Lifecycle | Linear stamps follow the state (Done ⇔ completed_at; In Progress ⇔ started_at); no comment after a ticket closed | Done only on the eight delivered lines, as DES-313's description says ('A line's ticket closes when PlayableX have the file'); the zombie ticket closes at 10:22 UTC on 29 Sep, after its note |
| Identifier / Format | sql_lint, hg.py lint id_contract, generator id invariants: 0 problems | e-mails and ids copied from base (1.B); one naming scheme per service |
| Semantic / Category | — | the pack list's Category is the game's data folder (`Assets/Data/Objects/<Category>` in `harmonygames-Games/match3d`, `research/object_categories.csv`) for all 84 board items; the base master item list and the prefab folders file about ten of them elsewhere, so the notes say to copy Brian's column; the sheet titles say what they hold |
| Other | hg.py lint grader_language and padding_comment: 0 flags | no record states a conclusion: notes give where the file came from and whether it opens, never the state; nothing addresses a solver |

## Integrations and companions

| Service | INT id | Companion | Decision (record) |
|---|---|---|---|
| slack | INT-13, INT-04, INT-22 | Drive-app DMs, Linear-app posts, notification mails | none seeded (manifest `integration_exceptions`); the bow post's thread counters are updated with the reply `C08R8CHB0QL/1758922879.243189` |
| linear | INT-04, INT-05 | Slack posts, e-mail digests | none: DES-313 and its children were made outside Slack; digests are aggregate |
| gcal | INT-11 | invitation mails | seeded: four event rows with one `ical_uid` (`evt_421695d009e589ee85296c` on Julia's calendar) and one invitation mail per guest mailbox |
| gmail | INT-11 | the invitation mails | seeded as companions only (`julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>`) |
| gdrive, gdocs, gsheets, gslides | INT-13 | Drive rows mirror Docs, Sheets and Slides ids and sharing | seeded: one `drive_files` row per file (`f_8c1d0bca1d1d5fde4c5008`, `f_956e60ec7f2f7977d98934`, `f_b2387e31d46d3a7b3fa2a9`, `f_6a2fa8e61b31139ca8e3d4`, `f_faf4d7c167d14a1127dcc3`) |
| trello | INT-21 | none exists | trello: none — card `688c4d14c312a27fa2747e40` and its board get the comment's time as dateLastActivity; the badge counts one comment |
| contacts | — | none | contacts: none — one sparse row `d7d31caf63ee33db2b7ed271` |

## Touched-data census and coherence hazards

Records a correct run opens, beyond the seeded ones: the PlayableX channel `C08H78VJG80` in full; #zombie-design `C090N54TG79` from 22 Sep; #zombie-art `C08R8CHB0QL` from 24 Sep with Julia's bow thread `C08R8CHB0QL/1758904025.123869`; #zombie-match3d `C0880U9751A` and #zm-animations `C09ATAJ220H` for the week; Julia's DMs `D05SD5QLG94`, `D05HMBQUC8Z`, `D076RBM29JS`; `harmonygames-Games/match3d#462` with its comment; the design page `page_zm3d_gdd` and its two comments; card `688c4d14c312a27fa2747e40`; `f_05bedd1540d3e01a90ab16`. Hazard ids are from `references/universe_kb/by_universe/synthcut/coherence_hazards.json`; cards from `references/known_data_issues/synthcut.md`.

| Category | Hazard / card | Where it meets the task (id) | Disposition |
|---|---|---|---|
| temporal | hazard T02; card SC-13 | three start dates in `C08H78VJG80` | dated claim sequence, the last stands; the beta date is never cited |
| temporal | hazard T06 | card `688c4d14c312a27fa2747e40` | the SQL moves the card's and the board's dateLastActivity to the comment's time |
| semantic | hazard S03: none in scope; card SC-58 | `page_zm3d_gdd` | the roster sentence of the page is neither cited nor graded; no label is seeded |
| referential | hazards R04, R08; cards SC-36, SC-7 | the hold `evt_421695d009e589ee85296c`; channel rosters | no Slack text carries a document link; the hold is seeded with a copy on every attendee's calendar and its mails; no base invite or roster feeds an answer |
| quantitative | hazards Q01, Q02, Q03 | `C08R8CHB0QL/1758904025.123869` | reply_count, reply_users_count and latest_reply are updated with the seeded reply |
| state / lifecycle | hazards L06: none in scope, L09; cards SC-16, SC-22, SC-15 | `harmonygames-Games/match3d#462`; open ZOM tickets naming objects (`ZOM-449`, `ZOM-513`, `ZOM-514`) | the pull request's review state is not used; the objects of SC-16's tickets are not on the list; `ZOM-521` is not cited by any seeded record; new tickets carry no time_in_status value |
| identifier / format | hazards I01, I02, I10, I15; card SC-50 | seeded Slack ids; `usr_Robert`; the bot comment `harmonygames-Games/match3d#462#c_1` | ids follow the base schemes; the comment is used for the models it names, never for which account wrote it |

No State/Lifecycle or Referential hazard record is modified by the SQL, so `hazard_acknowledgements` is empty. The two reviewers' re-check of the planned records against the base found no remaining contradiction (`Working_Files/research/recheck_D2_base.md`: five majors, all fixed before this SQL).

## Intended disagreements

| # | Claim (dated, by) | Later record (dated, by) | Why it is realistic | What resolves it |
|---|---|---|---|---|
| 1 | twelve notes, 25 Sep, Brian: FBX saved out of the project, opens, looks right (DES-367) | `C0880U9751A/1758906517.912099`, 26 Sep, Marcus: those files are the text kind | Brian checked in Unity, where the files open; Marcus had just rebuilt the zombie pack after the vendor's complaint | the vendor takes binary only (`C08H78VJG80/1758022459.227279`); the notes: a later word from someone who knows the file counts |
| 2 | twelve notes, 26 Sep, Brian: FBX from Claire, looks right (DES-349) | `D05GU6L0XFH/1759178332.042459`, 29 Sep, Claire: redoing the bathroom UVs; Friday's files are the old state | the artist decided on a rework after handing the files over and told the level designer first | the notes: current version, nobody changing it |
| 3 | three notes, 25 Sep 08:05 UTC, Brian (DES-389) | base `harmonygames-Games/match3d#462`, merged 25 Sep 23:15 UTC | Robert asked for the changes the night before; the files went to Brian before Claire made them; rev2: Robert shows the new versions on 29 Sep and Brian's log of 30 Sep records the re-send | the notes: a changed file goes again |
| 4 | eight notes, 26 Sep, Brian: zipped with the other instruments, in the outgoing folder (DES-380) | `f_faf4d7c167d14a1127dcc3`, 30 Sep, Brian: that zip will not unpack | an upload cut off; he noticed after the pause and noted it for himself | the notes: sitting in the outgoing folder, it opens |
| 5 | two notes, 26 Sep, Brian: exported .wav, plays (DES-402) | `f_b2387e31d46d3a7b3fa2a9`, Calvin: from a library seat and a bought pack | the packer checked the file type, not the source | the notes: only sound that is ours is handed over |
| 6 | `C090N54TG79/1758823946.262829`, 25 Sep, Robert: the eight, the dynamite last | `C08R8CHB0QL/1758922879.243189`, 26 Sep, Robert: it goes in place of the last one | a pick changed in passing, in a thread about the item | the ask: his picks stand unless he has changed them since |
| 7 | `f_6a2fa8e61b31139ca8e3d4`, 23 Sep, Julia: the reference level has three item types | `C090N54TG79/1758823946.262829`, 25 Sep, Robert: eight for the board | the reference level was built before the vendor's 8-item set was answered (base `D076RBM29JS/1758638743.317009`) | the notes: the eight on the board; the deck is what was built for them |

## Constraints for the prompt brief

| Anchor | May be named (noun phrases only) | Record |
|---|---|---|
| A1 | Frederick's playable message | `7e84f1cf59f8e95fef961268fbf37cc1` |
| A2 | the PlayableX channel | `C08H78VJG80` |
| A3 | my Drive | `d_8140f09bf9f1b94cb8ee2d` |

Never named in the prompt: where the notes and the pack list live; any ticket key, channel, category or item; the three state words; any count; the deciding records or their places (Marcus's post, Robert's note, the pull request, Calvin's sheet, Robert's reply, Brian's log). Deadlines: none stated to the agent beyond the ask. Deliverable kinds: one Google Doc and one Google Sheet in Julia's Drive; ticket updates and comments; one DM reply; one channel post.

## Fact sheet

| Key | Value | Kind | Home rows / must appear in |
|---|---|---|---|
| files saved out of Unity are the text kind | the text kind | status | `a5ee6e90923eeab380e6730f674240d2` |
| bathroom UVs being redone | is redoing the UVs on the bathroom objects from scratch | status | `8a1b1c6d448eecb7ccc81f796c95d5ce` |
| Friday's bathroom files are the old version | the bathroom files she gave <@EMPLOYEE_0026_SLACK_ID> on Friday are the old version too | status | `8a1b1c6d448eecb7ccc81f796c95d5ce` |
| bow replaces the last pick | in place of the last one on my list | status | `1d55b38831d7517fe403e4f2a906a897` |
| instruments' zip will not unpack | won't unpack | status | `f_faf4d7c167d14a1127dcc3` |
| three recoloured items sent again | Claire sent the three recoloured models again | status | `f_faf4d7c167d14a1127dcc3` |
| re-sent items open and look right | Opened them, they look right, and they replace Thursday's | status | `f_faf4d7c167d14a1127dcc3` |
| rocket sound source | Soundly library (Robert's seat) | status | `f_b2387e31d46d3a7b3fa2a9` |
| explosion sound source | Universal Sound FX pack (Unity Asset Store, Robert's) | status | `f_b2387e31d46d3a7b3fa2a9` |
| the eight of 25 Sep | Shuriken, Cute Axe, Gift Box, Cactus Plant and Dynamite | status | `da6776f77288224ec67847a799bbde5a` |
| the four zombies | Party Girl, Plumber, Magician, Football Player | status | `0b7f656a96c5cc50d1f6924e089bf8ba` |
| saved out of the project (twelve notes) | FBX saved out of the project, Thu 25 Sep | status | `513dd4bc-6bd5-5aaf-b4da-feb984524384`, `7daa1ebe-84c9-5aba-ba45-22f69fdfd01f`, `395bc5d2-8e32-537e-9286-a216ddf6b5af` … |
| zipped with the other instruments (eight notes) | Zipped with the other instruments | status | `0d2b852c-979f-5ed8-a046-899a3e81e476`, `fc981716-2526-53b9-ad72-1e753cf07fa6`, `2e1503f8-fe6d-5d46-9be3-4f2e70d58bf8` … |
| handed over first thing on 25 Sep (three notes) | FBX from Claire, Thu 25 Sep, first thing | status | `deb96bcb-7d02-5c29-8c41-79fcbd7c1c61`, `202ce85a-7926-5920-aa57-6cb399779639`, `6fcca602-b45d-5d9e-a519-d6a67875a6e9` |
| PlayableX intake address | intake@playablex.ai | status | `d7d31caf63ee33db2b7ed271` |
| kickoff hold | ZM3D playable kickoff with PlayableX | status | `evt_1c99b11a66cfd562b13d9c`, `evt_421695d009e589ee85296c`, `evt_a78612f3eaf04ce8461eb4` … |
| pack ticket rule | A line's ticket closes when PlayableX have the file | status | `DES-313` |

`fact_check.py … --no-leak` (verbatim):

```
FACT CHECK: PASS — 227 text-bearing rows, 17 declared facts, 7 declared superseded records
Errors: none
Warnings (3):
  line 20: gdocs.docs_documents f_faf4d7c167d14a1127dcc3: [ambiguous_name] bare first name 'Claire' matches several roster entities (Claire Morgan <claire.morgan@harmonygames.co> [persona claire_morgan]; Claire <github:PERSON_2360_GITHUB_USERNAME>) — use the full name or a <@mention>; 65 row(s) (e.g. lines 20, 20, 20, 20)
  line 62: slack.slack_messages 0b7f656a96c5cc50d1f6924e089bf8ba: [ambiguous_name] bare first name 'Marcus' matches several roster entities (Marcus Bennett <marcus.bennett@harmonygames.co> [persona marcus_bennett]; Marcus Lee <marcus.lee@harmonygames.co>; Marcus <trello:c48a210d5c5a4b59231c6873>) — use the full name or a <@mention>; 2 row(s) (e.g. lines 62, 250)
  line 259: linear.linear_comments 31b53426-4274-593c-b1cf-ef944ed22968: [ambiguous_name] bare first name 'Martin' matches several roster entities (Martin Lewis <PERSON_0394_EMAIL>; Martin Walsh <martin.walsh@harmonygames.co> [persona martin_walsh]) — use the full name or a <@mention>; 1 row(s) (e.g. lines 259)
```

## Facts for the human

Totals from `solver/truth.json`: 8 Delivered, 39 Ready, 49 Owed of 96 lines; 49 Owed lines have a ticket (to Todo with a comment); without the six deciding records a reader gets 8 / 73 / 15. Owed by reason: 15 on their own note, 12 text-kind files, 12 bathroom, 8 in the broken zip, 2 sound cues; the 3 recoloured lines are Ready (sent again, Brian's log).

| Locator | Base / seeded | Fact (values, actors, UTC) | Reach path | Role | Re-verify? |
|---|---|---|---|---|---|
| `7e84f1cf59f8e95fef961268fbf37cc1` (D05SD5QLG94/1759256494.852159) | seeded | Frederick's ask to Julia, Tue 30 Sep 2025 18:21 UTC: the brief and where the item pack stands; Brian's pack list, Robert's picks, his hand-off notes; both files in her Drive; the count for each state 'here'; both links in the PlayableX channel | DM member | anchor (hub) | no |
| `f_8c1d0bca1d1d5fde4c5008` | seeded | Frederick's hand-off notes (30 Sep 16:58 UTC): what the brief covers; the list's columns (Line, Category, Board set, State, What's owed, Who has it, Ticket); Delivered, Ready, Owed; later statements count; changed art goes again; sound that is ours; tickets to Todo with a comment; sharing | shared reader | authority | no |
| `f_956e60ec7f2f7977d98934` | seeded | Brian's pack list: 96 rows (Line, Kind, Category, Went out, Ticket), last edited 26 Sep 17:25 UTC | shared reader | authority (line set) | no |
| `DES-313` and `DES-314` … `DES-409` | seeded | the pack ticket and one child per line; Done on the 8 delivered lines, In Progress on the other 88; one note by Brian on each child | unscoped | evidence; write targets | no |
| `da6776f77288224ec67847a799bbde5a` | seeded | Robert, 25 Sep 18:12 UTC: the eight (Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant, Dynamite) | channel member | claim met first | no |
| `1d55b38831d7517fe403e4f2a906a897` under `C08R8CHB0QL/1758904025.123869` | seeded | Robert, 26 Sep 21:41 UTC: the bow in the eight in place of the last item of his list, as it is now. The eight become Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Bow, Cactus Plant | channel member | overturning evidence | no |
| `0b7f656a96c5cc50d1f6924e089bf8ba` | seeded | Robert, 29 Sep 17:31 UTC: one animation, walk; the four zombies Party Girl, Plumber, Magician, Football Player | channel member | evidence | no |
| `a5ee6e90923eeab380e6730f674240d2` | seeded | Marcus, 26 Sep 17:08 UTC, #zombie-match3d: the models saved out of Unity on Thursday are the text kind; Claire's are fine. Decides 12 lines: Owed, export again as binary, Brian | channel member | overturning evidence | no |
| `8a1b1c6d448eecb7ccc81f796c95d5ce` | seeded | Robert to Julia, 29 Sep 20:38 UTC, in their DM: Claire (tagged) is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version. Decides 12 lines: Owed, Claire (the file came from her) | DM member | overturning evidence | no |
| `harmonygames-Games/match3d#462` and `harmonygames-Games/match3d#462#c_1` | base | 'Objects Revisions and Changes', created 2025-09-25T11:43:06Z, merged 23:15:41Z; the comment names the chainsaw, cactus and cone models (and Candy, Dart Board, Kettlebell, which are not lines). Decides 3 lines: Owed | unscoped | overturning evidence | yes, if GitHub is regenerated |
| `f_b2387e31d46d3a7b3fa2a9` | seeded | Calvin's sound sources: Rocket sound (Soundly library seat) and Explosion sound (bought pack) are 'no' under 'OK outside the game', 'not made yet, Calvin' under 'Replacement'. Decides 2 lines: Owed, Calvin | shared reader | overturning evidence | no |
| `f_faf4d7c167d14a1127dcc3` | seeded | Brian's log of the outgoing folder, 30 Sep 09:12 UTC: the zip with Friday's music instruments will not unpack and the eight are not in the folder any other way. Decides 8 lines: Owed, Brian | shared reader | overturning evidence | no |
| `f_6a2fa8e61b31139ca8e3d4` | seeded | Julia's deck of the reference level (23 Sep): grenade, couch, couch and pillow, the two plushies; win and lose as told to the vendor | owner | claim met first (older state) | no |
| `evt_421695d009e589ee85296c` | seeded | kickoff hold, Mon 3 Nov 2025 17:00 to 17:30 UTC (09:00 PST); attendees Frederick, Julia, Brian, Robert | attendee | authority (recipients) | no |
| `d7d31caf63ee33db2b7ed271` | seeded | PlayableX intake: intake@playablex.ai | unscoped | evidence (recipient) | no |
| `68dc381b75aff34acf5a5424` on `688c4d14c312a27fa2747e40` | seeded | Leonard, 30 Sep 20:05 UTC: parked until 3 Nov, the start PlayableX gave after we asked for the pause; Julia is pulling the brief and the pack status together for Frederick | unscoped | decoy | no |
| `C08H78VJG80/1758022459.227279`, `C08H78VJG80/1758283671.878269` | base | the vendor takes .fbx in binary format only, .glb or .blend; the 8-item set; editable extra items | channel member | evidence (format rule) | no |
| `C08H78VJG80/1759226395.551469` | base | new start 3 November | channel member | evidence | no |
| `page_zm3d_gdd` | base | 7-slot tray; a level is lost only at zero health | unscoped | evidence | yes, Confluence is regenerated |
| `C08H78VJG80/1757695108.506159`, `C08H78VJG80/1757956024.883249` | base | Scenario 1: filters for players who will like the game, true to the core game play; chosen 15 Sep | channel member | evidence | no |
| `C08H78VJG80/1744637266.363689` | base | music starts after the first click (14 Apr, first playable) | channel member | evidence | no |

## Platform follow-ups

- Pre-check: confirm that `linear_list_comments` returns Brian's notes and that `linear_show_data` and the `query` parameter of `linear_list_issues` do not return comment bodies in bulk (both are unverified in `Ask_Carriers.md`); confirm the counted calls of the run are above 150.
- Pre-check: note whether the run looks in Drive for the outgoing folder (the route to Brian's log, which decides eleven lines: the eight zipped instruments and the three recoloured items); no route through GitHub is relied on in rev2.
- Confluence (`page_zm3d_gdd`) is being regenerated: re-verify the 7-slot tray and the zero-health sentence before the rubric is written.
- Rubric: accept the two links in the PlayableX channel as a top-level post or as a reply in the pause thread (both are 'in the channel'); accept the counts in Frederick's DM as a message or a thread reply.
- Rubric: do not grade what a full tray does in the playable. Base holds two statements (the design page `page_zm3d_gdd`; Frederick's 23 Sep remark `C2637A3385F7/1758656830.965739` in a group chat whose roster does not list Julia), and the page's Modes section scores one mode 'before the tray fills'. Tray size (7) and the loss rule (zero health) are stated consistently and are the graded facts.
- Pre-check: note whether the run can open the group chat `C2637A3385F7`; nothing graded depends on it.
- No ○ carrier is load-bearing: nothing sits in a calendar description, slide notes, a Drive `content_text` or a Slack file.
- The injection-stage forecast is computed on the 24 solver-readable slots only (list cells and totals); the 29 slots graded from written text are outside the solver. It is recorded as such (Self-review).

## Self-review

**Tool outputs, verbatim.**

`sql_lint.py`:

```
schemas touched (10): contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello
rows by schema: {'gdrive': 5, 'gdocs': 2, 'gsheets': 4, 'gslides': 13, 'slack': 7, 'linear': 193, 'trello': 3, 'gcal': 4, 'gmail': 6, 'contacts': 1}  total rows: 238  ops: {'insert': 235, 'update': 3}
errors: 0  warnings: 8
  warn  line 265: gcal.gcal_events.start_ts = 2025-11-03T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 265: gcal.gcal_events.end_ts = 2025-11-03T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 268: gcal.gcal_events.start_ts = 2025-11-03T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 268: gcal.gcal_events.end_ts = 2025-11-03T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 270: gcal.gcal_events.start_ts = 2025-11-03T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 270: gcal.gcal_events.end_ts = 2025-11-03T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 272: gcal.gcal_events.start_ts = 2025-11-03T17:00:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
  warn  line 272: gcal.gcal_events.end_ts = 2025-11-03T17:30:00Z is on/after the clock — allowed only as a deadline or a not-yet-happened event
```

`base_check.py`:

```
BASE CHECK (/injection A + C, static): PASS  — 235 inserts, 3 updates
KB: bound (2025-10-01) — KB bound to the selected universe
Check A — records, references, IDs: PASS
Check C — dates and relationships: PASS
  note: gsheets.sheets_sheets: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_page_elements: no base-reference rules (checked by sql_lint only)
  note: gslides.slides_pages: no base-reference rules (checked by sql_lint only)
```

`base_claims.py`:

```
BASE CLAIMS (injected text vs base git + #builds): PASS · 0 branch mentions · 0 fail · 0 warn · 0 date-only
branch windows:
```

`hardness_gate.py` on the final manifest and the SQL:

```
HARDNESS GATE (extreme): PASS
  [ok] assignment_context: manifest bound to current V3 assignment, freeze and policy
  [ok] effective_profile: effective_profile 'extreme' for 'Long Horizon' → thresholds 'extreme'
  [ok] sql_lint_clean: 0 lint error(s) — run tools/sql_lint.py
  [ok] base_consistency: /injection-style checks vs the base universe: A 0 finding(s), C 0 finding(s), 0 warning(s) — run tools/base_check.py --manifest
  [ok] persona_reach: 113 load-bearing seeded ids for julia_lawson (101 in unscoped services = visible, 12 judged by persona_view check-sql); not provably visible: none
  [ok] fact_consistency: fact_check: 0 error(s) (17 declared facts), 3 drift warning(s); first: none — run tools/fact_check.py --manifest --no-leak
  [ok] hazard_scope: 0 pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a verified resolution: none
  [ok] services_injected: 10 schemas injected (contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello); need ≥ 10
  [ok] rows: 235 INSERTed rows (UPDATE companions not counted; 238 rows in all); need ≥ 120
  [ok] services_carrying_weight: 12 services with a weight_reason; need ≥ 10
  [ok] no_orphan_injection: schemas injected but absent from the design: none
  [ok] seeded_ids_exist_in_sql: 45 seeded ids cited; missing from SQL: none
  [ok] anchors: 3 anchors (1–3, each with a plain-language prompt_reference)
  [ok] ask_fragments: 15 fragments; need ≥ 12
  [ok] ask_fragment_services: 8 services carry asks; need ≥ 7
  [ok] ask_fragment_containers: 14 distinct containers; need ≥ 10
  [ok] incorporation_chains: every fragment must chain back to a prompt anchor through explicit delegations whose words (delegation_quote) are in the delegating record; broken: none
  [ok] requirement_coverage: 7 declared requirements; each must be named (requirement_ids) by an incorporated fragment or an anchor — orphan requirements (graded with no source the prompt reaches): none
  [ok] authority_incorporation: every authority must be named by a fragment's own record (names_authorities [{id, quote}]) or be the record an incorporated fragment delegates to; orphan authorities: none
  [ok] cohort_size: cohort 96; need ≥ 40 (source-defined: True)
  [ok] evidence_surfaces: 3 surfaces over 2 services; each needs why_no_bulk and (extreme) a short_circuit analysis — why a correct run cannot skip it once other surfaces decide the record (missing: none)
  [ok] surface_requirements: every cohort surface must serve a declared, incorporated requirement and the output column or decision it states (`requirement`, `decides`) — no manufactured columns; bad: none
  [ok] per_record_calls: Σ per-record calls × records each surface applies to = 195; need ≥ 110
  [ok] call_budget: unconditional (verified) floor 252 of 252 planned calls (0 conditional on unverified tool behaviour count 0); need floor ≥ 220 (requester-confirmed volume_exception)
  [ok] call_budget_spread: 10 services in budget; largest share outside the per-record phase 34% (≤ 50%)
  [ok] traps: 19 traps across 10 families; need ≥ 12 / ≥ 7; unknown family: none
  [ok] trap_independence: traps hit 7 distinct requirements; need ≥ 6 (failure-pattern diversity)
  [ok] trap_completeness: each trap needs records, a resolver and the expected wrong reading; incomplete: none
  [ok] supersession: 4 supersessions (2 with versions in ≥ 2 services, 2 with ≥ 3 versions); each needs version_records [{service, id|base_pointer, seeded, at (ISO, oldest first)}] ≥ 2 — missing/unordered: none
  [ok] supersession_chronology: 5 trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the base record) must be strictly increasing in the listed order (oldest first); bad: none
  [ok] distractors: 6 distractors of 6 types; need ≥ 6 / ≥ 4
  [ok] discovery_order_proofs: 11 traps carry a discovery-order proof; need ≥ 4
  [ok] independent_chains: 6 chains with 6 distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism count once); need ≥ 3, each ≥ 3 hops over ≥ 2 services ending in a graded fact; thin: none; root_cause not a mechanism id: none
  [ok] mechanism_portfolio: 6 portfolio entries, each a mechanism-enum id with trap/chain nodes, a requirement, a natural-reading fallback and a prior family with its reason
  [ok] artifact_fields: declared ['gradable_surface', 'solver']: paths relative, digests sha256
  [ok] hidden_authorities: 3 authorities (need ≥ 2), each homed in ['gcal', 'gdocs', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello'] with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), a findable_query, records, and NON-overlapping 'governs'; bad: none; overlap: False; same-service decoys 1 (need ≥ 1: a targeted search must also meet a decoy)
  [ok] decoy_scope: each authority's decoy must apply to a different scope (decoy_scope {dimension: game|issuer|lot|team, decoy, task}) or be an older entry of a trap's version_records — an identical-scope contradiction fails Cross-Service Coherence and Unique Ground Truth; bad: none
  [ok] rarely_opened_evidence: 6 traps carry decisive evidence in rarely-opened services ['gcal', 'gmail', 'gsheets', 'gslides', 'snowflake', 'trello']; need ≥ 3
  [ok] requirements: 7 requirements declared; referenced but undeclared: none; declared with no trap/chain/authority/write mapping: none
  [ok] writes: 6 writes over 5 services; each must depend on findings
  [note] volume_exception: call-budget floor 220 and per-record floor 110 replace 500 and 300; every other extreme target applies — reason: the cohort is the 96 lines of one playable pack; honest necessary calls are abou; requester confirmation: task author in chat on 2026-11-11: '220 calls are good with required failure'; a
```

`oracle_kit.py check`:

```
SOLVER CONTRACT: PASS · solver.py sha 3fb11113479e · sql 7d1f2aaeb29c · 6 rules
  [PASS] contract.interface: 6 rules, each with mechanism, requirement and natural_reading; optional: ['touched', 'deciding', 'DEGRADES']
  [PASS] contract.deterministic: two fresh solves (forward and reverse key order) give identical output (96 keys, sha f3ff5af5b0ca), and so do fresh processes with PYTHONHASHSEED 1 and 2
  [PASS] contract.regression: no previous revision supplied (first revision)
  [PASS] contract.rules_nodes: 6 rules vs 6 portfolio entries: one-to-one
  [PASS] contract.slots: 25 direct/aggregate slots read a solver value; 27 write-content/delivery slots are graded from the writes, not the solver
  [PASS] contract.controls: EXPORT: 1 control(s); export_over moves ['Rolling Pin']; ARTHOLD: 1 control(s); art_over moves ['Desk Lamp']; REVISED: 1 control(s); revised_over moves ['Fly Zapper']; AUDIO: 1 control(s); audio_over moves ['Success sound']; PICKS: 1 control(s); picks_over moves ['Grenade']; ZIP: 1 control(s); zip_over moves ['Music Keyboard']; channel CH-EXPORT (scale): ch_miss moves 12 of 12 member(s); channel CH-ARTHOLD (scale): ch_miss moves 12 of 12 member(s); channel CH-REVISED (scale): ch_miss moves 3 of 3 member(s); channel CH-AUDIO (scale): ch_miss moves 2 of 2 member(s); channel CH-PICKS (scale): ch_miss moves 2 of 2 member(s); channel CH-ZIP (scale): ch_miss moves 8 of 8 member(s)
  [PASS] contract.golden: 12 golden values checked against their deciding records (12 sampled keys x 6 fields): 9 identifier values found, 3 short tokens found, 0 presence-type; 60 unverified e.g. ['Refrigerator/Category: no evidence ids', 'Refrigerator/Board set: no evidence ids']
  [PASS] contract.digest: manifest solver Working_Files/solver/solver.py digest 3fb11113479e vs file 3fb11113479e
```

`plan/citation_chronology.py` (times read from the SQL; every record against the record it names or answers):

```
Citation chronology (UTC): each record against the record it names or answers

[ok] the ask (sent) 30 Sep 18:21:34  >=  the notes (last edit) 30 Sep 16:58:19  (the ask names 'my hand-off notes')
[ok] the ask (sent) 30 Sep 18:21:34  >=  the pack list (last edit) 26 Sep 17:25:08  (the ask names Brian's pack list)
[ok] the ask (sent) 30 Sep 18:21:34  >=  base: vendor's new start date 30 Sep 09:59:55  (the ask names Nov 3)
[ok] the ask (sent) 30 Sep 18:21:34  >=  Robert's zombie answer (posted) 29 Sep 17:31:08  (the ask names Robert's picks for the zombies)
[ok] the notes (last edit) 30 Sep 16:58:19  >=  the kickoff hold (created) 30 Sep 16:41:17  (the notes name the kickoff hold)
[ok] the notes (last edit) 30 Sep 16:58:19  >=  the deck (last edit) 23 Sep 19:55:47  (the notes name Julia's deck)
[ok] the notes (last edit) 30 Sep 16:58:19  >=  the pack ticket (created) 25 Sep 07:05:12  (the notes name Brian's pack ticket)
[ok] the kickoff hold (created) 30 Sep 16:41:17  >=  base: vendor's new start date 30 Sep 09:59:55  (the hold is on the vendor's date)
[ok] the pack ticket (created) 25 Sep 07:05:12  >=  the pack list (created) 25 Sep 06:48:27  (the ticket's description names the pack list)
[ok] the pack list (last edit) 26 Sep 17:25:08  >=  the pack ticket (created) 25 Sep 07:05:12  (the list's Ticket column holds the children's keys)
[ok] Robert's reply on the bow (posted) 26 Sep 21:41:19  >=  Robert's eight (posted) 25 Sep 18:12:26  ('the last one on my list')
[ok] Robert's reply on the bow (posted) 26 Sep 21:41:19  >=  base: Claire's answer in the bow thread 26 Sep 16:28:23  (reply in the thread)
[ok] note: Bow 29 Sep 11:08:27  >=  Robert's reply on the bow (posted) 26 Sep 21:41:19  (the bow's file is exported after the arrow thread)
[ok] Robert's zombie answer (posted) 29 Sep 17:31:08  >=  base: vendor's question on the zombies 29 Sep 10:16:08  ('for PlayableX's question')
[ok] note: Zombie characters 29 Sep 10:21:17  >=  base: vendor's question on the zombies 29 Sep 10:16:08  (the note reports their question)
[ok] note: Zombie characters 29 Sep 10:21:17  >=  base: Brian sends the pack to the vendor 26 Sep 17:00:43  (the note says the pack was sent)
[ok] Marcus's post 26 Sep 17:08:37  >=  notes on the twelve Thursday exports (latest) 25 Sep 15:39:49  (a later word on Thursday's exports)
[ok] Marcus's post 26 Sep 17:08:37  >=  base: Marcus hands over the zombie pack 26 Sep 16:53:24  (posted after his own pack)
[ok] Robert's note on the bathroom objects 29 Sep 20:38:52  >=  notes on the twelve bathroom files (latest) 26 Sep 11:22:18  (a later word on Friday's bathroom files)
[ok] base: match3d#462 created 25 Sep 11:43:06  >=  notes on the three recoloured lines (latest) 25 Sep 08:06:42  (the art changed after the files were handed over)
[ok] base: Robert's new colour versions 29 Sep 23:44:26  >=  notes on the three recoloured lines (latest) 25 Sep 08:06:42  (new colour versions after the files were handed over)
[ok] Brian's log (last edit) 30 Sep 09:12:26  >=  base: Robert's new colour versions 29 Sep 23:44:26  ('Claire sent the three recoloured models again')
[ok] Brian's log (last edit) 30 Sep 09:12:26  >=  notes on the eight zipped instruments (latest) 26 Sep 13:14:23  (a later word on Friday's zip)
[ok] Brian's log (last edit) 30 Sep 09:12:26  >=  base: Frederick asks for the pause 29 Sep 19:42:05  ('when we pick this up again')
[ok] Brian's log (last edit) 30 Sep 09:12:26  >=  notes on lines not exported (earliest) 29 Sep 12:31:37  ('a few are still mine to do')
[ok] notes on lines not exported (earliest) 29 Sep 12:31:37  >=  notes on Monday's files (latest) 29 Sep 11:30:19  (written after Monday's batch)
[ok] Leonard's Trello comment 30 Sep 20:05:47  >=  the ask (sent) 30 Sep 18:21:34  ('Julia is pulling the brief ... together for Frederick')
[ok] Leonard's Trello comment 30 Sep 20:05:47  >=  base: vendor's new start date 30 Sep 09:59:55  ('the new start PlayableX gave us')

CITATION CHRONOLOGY: PASS · 28 pairs · 0 out of order
```

`difficulty_mutation.py mutate` (rules, degrades, geometry):

```
MUTATION · rev2 · sql 7d1f2aaeb29c · deterministic design diagnostics from the solver; on the Season Pass backtests these are development fixtures, not validation
  key-locality: PASS on 37 of 37 configurations checked
  rule:EXPORT                        KILLED     flipped  21 flips direct slot(s) of weight >= 3: ['X1', 'X1b', 'X16']
  rule:ARTHOLD                       KILLED     flipped  26 flips direct slot(s) of weight >= 3: ['X2', 'X2b', 'X11', 'X11b']
  rule:REVISED                       KILLED     flipped  21 flips direct slot(s) of weight >= 3: ['X3', 'X3b', 'X8']
  rule:AUDIO                         KILLED     flipped  21 flips direct slot(s) of weight >= 3: ['X5', 'X5b', 'X12']
  rule:PICKS                         KILLED     flipped  10 flips direct slot(s) of weight >= 3: ['X13', 'X14']
  rule:ZIP                           KILLED     flipped  21 flips direct slot(s) of weight >= 3: ['X4', 'X4b', 'X17']
  degrade:export_over                KILLED     flipped   9 flips direct slot(s) of weight >= 3: ['C1']
  degrade:art_over                   WEAK       flipped   6 flips only aggregate or weight-1 slots: ['A1', 'A2']
  degrade:revised_over               KILLED     flipped   9 flips direct slot(s) of weight >= 3: ['C2']
  degrade:audio_over                 WEAK       flipped   6 flips only aggregate or weight-1 slots: ['A1', 'A2']
  degrade:picks_over                 KILLED     flipped   3 flips direct slot(s) of weight >= 3: ['C4']
  degrade:zip_over                   WEAK       flipped   6 flips only aggregate or weight-1 slots: ['A1', 'A2']
  degrade:ch_miss                    KILLED     flipped  96 flips direct slot(s) of weight >= 3: ['X1', 'X2', 'X3', 'X4', 'X5', 'X
  intervention:rule:EXPORT           load-bearing    
  intervention:rule:ARTHOLD          load-bearing    
  intervention:rule:REVISED          load-bearing    
  intervention:rule:AUDIO            load-bearing    
  intervention:rule:PICKS            load-bearing    
  intervention:rule:ZIP              load-bearing    
  intervention:degrade:export_over   no-injected-records
  intervention:degrade:art_over      no-injected-records
  intervention:degrade:revised_over  no-injected-records
  intervention:degrade:audio_over    no-injected-records
  intervention:degrade:picks_over    no-injected-records
  intervention:degrade:zip_over      no-injected-records
  intervention:degrade:ch_miss       no-injected-records
  geometry: U = 0.7969 (153/192) · L_max = 0.5000 over ['rule:EXPORT', 'rule:ARTHOLD', 'rule:REVISED', 'rule:AUDIO', 'rule:PICKS', 'rule:ZIP']
    V3 cap 0.70: U PASS (needs > 0.30) · L_max OK
  dispositions: 0/26 recorded; missing ['rule:EXPORT', 'rule:ARTHOLD', 'rule:REVISED', 'rule:AUDIO', 'rule:PICKS', 'rule:ZIP', 'degrade:export_over', 'degrade:art_over'] ...
```

`preflight_report.py` (the empty list of missing liveness dispositions is printed here as `none`):

```
PREFLIGHT: PASS · blocking {'solver_contract': True, 'surface_validation': True, 'mutation_dispositions': True, 'geometry_upper_bound': True} · advisory {'geometry_margin': {'V3': 'OK'}, 'geometry_bound_verdict': {'V3': 'PASS'}, 'liveness_dispositions_missing': none, 'forecast': 'recorded'}
wrote Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.json and Task_Authoring/task_inputs/Working_Files/01c_Preflight_Report.md
```

**Warning dispositions.**
- sql_lint warning, clock class (8 lines, the hold's `start_ts` and `end_ts` after the clock): disposition — allowed, a not-yet-happened event: the kickoff on 3 Nov 2025 is the vendor's own new start date (`C08H78VJG80/1759226395.551469`); the event's `created` and `updated` are 30 Sep 16:41 UTC, before the seed bound and before the last edit of the notes that name it (16:58 UTC).
- fact_check warnings (ambiguous first names 'Claire', 'Marcus', 'Martin' in Brian's ticket notes): disposition — kept as a colleague writes them; on this game they are Claire Morgan, Marcus Bennett and Martin Walsh (1.B), no graded value depends on a full name, and 'Who has it' is compared on the first name.
- `hg.py lint` (the eval's `hg_injection_lint.py`, with base data): FAIL 0, CHECK 0, INFO 0 on sha256 `7d1f2aaeb29c`; no LINT line needs a disposition.
- Mutation: three over-application operators are WEAK (their control line is not a sampled row); each has a written disposition in `01c_Dispositions.json`. REVISED's operator (Fly Zapper called Ready) is KILLED on the sampled control C2. Geometry: U and L_max as printed above.

**Forecasts (advisory, UNCALIBRATED, pre-registered).** Four figures, which measure different things; none is a measurement. (1) Design stage, `hev_930ca8da536b9595`, on declared attributions for every slot and the ledger's family priors (which now include the seven rev1 runs): E[average] 0.657 to 0.670, P(all four difficulty gates) 0.360-0.450. Its completion_elsewhere prior still holds the rev1 runs that found Brian's log through the search for 'sound', which rev2 removes, so it is pessimistic for this revision. (2) Injection stage, this SQL (`hev_e258af3aaa3d48aa`, block below): the tool evaluates only the slots the solver can compute (list cells and totals); the slots graded from written text (reasons, ticket comments, the brief, the reply, the shares) count as always passing, so its averages are upper bounds and its P(all gates) near zero says only that list cells alone would not bring the average under 70 %. A first injection forecast of this revision (`hev_b59c9f65ca1510cb`) ran on the SQL before the log stopped naming the chainsaw and the cone (path exposure) and is superseded by the one below. (3) The difficulty budget on the rubric skeleton, with find rates measured in the rev1 runs (`plan/out/policy_scores.txt`): low find: E[average] 40.1 %, P(average under 70 %) 1.000, P(spread in band) 0.564, P(all gates) 0.553; midpoint: E[average] 51.5 %, P(average under 70 %) 0.998, P(spread in band) 0.721, P(all gates) 0.711; high find: E[average] 63.2 %, P(average under 70 %) 0.853, P(spread in band) 0.776, P(all gates) 0.633. (4) The MODE B simulation of rev1 habits (`hardening_gen/simulate.py`): E[average] 0.47 to 0.61 for these four changes. The next pre-check is the first measurement of rev2.

```
HARDNESS FORECAST · UNCALIBRATED · advisory · model claude-opus-5-5 · rev2 · model outputs, not measurements; the Season Pass backtests are development fixtures, not validation
  rule:EXPORT                                  family done_gap                                 Beta(1.75, 3.8571) mean 0.31 n_eff 3.6071 records 20
  rule:ARTHOLD                                 family superseding                              Beta(3.8214, 1.7857) mean 0.68 n_eff 3.6071 records 39
  rule:REVISED                                 family completion_elsewhere                     Beta(1.6429, 3.9643) mean 0.29 n_eff 3.6071 records 20
  rule:AUDIO                                   family authority                                Beta(1.25, 4.3571) mean 0.22 n_eff 3.6071 records 20
  rule:PICKS                                   family superseding                              Beta(3.8214, 1.7857) mean 0.68 n_eff 3.6071 records 39
  rule:ZIP                                     family completion_elsewhere                     Beta(1.6429, 3.9643) mean 0.29 n_eff 3.6071 records 20
  independent whole    V3 E[avg] 0.777 [0.713, 0.844] P(all) 0.008
  source      whole    V3 E[avg] 0.778 [0.708, 0.848] P(all) 0.017
  correlated  whole    V3 E[avg] 0.783 [0.683, 0.884] P(all) 0.085
  V3: P(all four difficulty gates) 0.000-0.085 across scenarios; value of information (first scenario): ['rule:REVISED', 'rule:AUDIO', 'rule:ZIP']
  slots most at risk (independent whole; P(fail) / P(fails all six) - all-fail justification workload, never a block): A1 0.92/0.63, A2 0.92/0.63, X2 0.68/0.21, X2b 0.68/0.21, X11 0.68/0.21, X11b 0.68/0.21, X13 0.68/0.20, X14 0.68/0.20
  ledger: forecast record {'id': 'hev_e258af3aaa3d48aa', 'added': True, 'present': False}
wrote Task_Authoring/task_inputs/Working_Files/01c_Forecast.json
```

**Checks A to C walk** (`Evals/0_Injection_Quality_Eval.md`).
- Inventory: 235 INSERT and 3 UPDATE, no DELETE, no upsert; statements grouped by service inside one BEGIN/COMMIT. PASS.
- Check A (references, uniqueness, identities, id contracts): every channel, user, team, parent ticket, calendar, card, board and mailbox exists in base (`base_check` Check A PASS); every minted id is absent from the full collections (1.F); one account per person per service; Drive files have a Docs, Sheets or Slides row with content. PASS.
- Check B (structure, literal JSON, generated and NOT NULL columns): literal values only; every `*_json` value is valid JSON; `text_fts` and `body_text_fts` are never written; Linear text dates are `YYYY-MM-DDTHH:MM:SSZ` (`hg.py lint` text_time_format: 0). PASS.
- Check C (dates, parent and reply, statuses, counts, claimed updates): every created, sent or updated value is before 2025-10-01T00:00:00Z; the reply is after its base parent `C08R8CHB0QL/1758904025.123869`; comments follow their tickets and precede the close of the eight Done tickets; the hold's start is a plan field. PASS.
- Grader-facing or padding text: none (lint 0); every record has a task purpose (record ledger).

**Touched-data census:** the section above; each hazard category and card has its disposition.

**Counter-readings** (category · the best case that it fails · evidence that resolves it · verdict):

| Category | Counter-reading | Resolution (evidence) | Verdict |
|---|---|---|---|
| Temporal | Brian's notes of 26 Sep say 'FBX from Claire' on days base shows no file transfer in their DM. | base neither shows nor contradicts hand-overs after 24 Sep (re-check: `D076Y0SDV18` ends 24 Sep 12:29 UTC); Claire offered to send whatever is asked (`D076Y0SDV18/1758712890.403889`) | holds |
| Temporal | The zombie ticket's note mentions the vendor's review, which is of 29 Sep, on a ticket created 25 Sep. | the note is stamped 29 Sep 10:21 UTC, after `C08H78VJG80/1759140968.965099` (10:16 UTC), and the ticket closes a minute later | holds |
| Semantic / Category | 'Category' on the list could be read as Brian's own grouping. | all 84 board items carry the category of the game's data folders (`research/object_categories.csv`); Bathroom, Kitchen and Garden agree in every base source (both reviewers checked), so 'banyo objeleri' maps to the thirteen Bathroom rows, and the notes say Category is copied from Brian's list | holds |
| Cross-service Referential | The pack list and the tickets could disagree on a line. | both come from one model; `sql_ids.json` and the solver's `listed` read the grid back; 96 rows, 96 children | holds |
| Quantitative | 8 / 39 / 49 could move on a line whose note is unclear. | every note states source and that the file opens, or that it is not exported (`plan/design_model.py` NOTE, VIS_NOTE); two cold reviews of the wording found one fork (the instruments), closed in the notes and the log | holds |
| State / Lifecycle | In Progress tickets with files in the outgoing folder look unfinished or inconsistent. | DES-313's description: a line's ticket closes when PlayableX have the file; only the eight delivered lines are Done | holds |
| Identifier / Format | 97 new keys could sit out of order against the team's base tickets (in ZOM they sat above `ZOM-566`, created five days later; both reviewers flagged it). | moved to the Design team: its last base ticket is `DES-312` (2025-05-07T19:31:13Z), so `DES-313` to `DES-409`, created 25 Sep, follow in number and in date; Brian's own last tickets there are a parent with bare-titled children (`DES-307`) | fixed in data |
| People status | Someone the rules depend on is not active at the clock. | all eight seeded speakers are active_sep_2025_quiet_in_oct in activity.json (1.C); no rule depends on anyone having left | holds |
| Other | The designed disagreements read as two silent system fields. | each is a dated note by a named person against a later dated statement by a named person (Intended disagreements 1 to 7) | holds |
| Disagreement 1 (EXPORT) | Brian's 'opens, looks right' and Marcus's 'text kind' are a plain contradiction in seeded data. | both are true: the files open in Unity and in Max (the post says so) and are ASCII; the vendor's rule `C08H78VJG80/1758022459.227279` makes the second matter | designed, resolved |
| Disagreement 2 (ARTHOLD) | Robert passing on Claire's rework, rather than Claire herself, is unnatural. | Robert follows the art (his colourised items and new colour versions are base) and talks with Julia daily in `D05GU6L0XFH`; he tells her because the old versions show in her levels (`D05GU6L0XFH/1759178332.042459`) | designed, resolved |
| Disagreement 3 (REVISED) | Robert's new colour versions and the log's 'replace Thursday's' could be about different files. | Robert's post names the cactus, the chainsaw and the cones (`C090N54TG79/1759189466.554739`); the Thursday files from Claire of those three are the only Thursday files with a later change; the log entry is the next day and the latest record | designed, resolved |
| Disagreement 4 (ZIP) | Brian's log contradicts his own ticket notes without him fixing the tickets. | the log line is of 30 Sep, the morning after the pause (`C08H78VJG80/1759174925.309129`); he writes that he will put the files back when the work resumes | designed, resolved |
| Disagreement 5 (AUDIO) | A sound that 'plays' and is 'not ours' is an unintended inconsistency. | file type and source are different facts; base already has two sounds to be swapped for rights (`D05GU6L0XFH/1757519060.984519`) | designed, resolved |
| Disagreement 6 (PICKS) | 'The last one on my list' could point at another list. | Robert has one list of picks, his post `C090N54TG79/1758823946.262829` of the day before in the channel where the playable is discussed; its last item is the dynamite, and 'things that go boom' fits it | designed, resolved |
| Disagreement 7 (deck) | The deck's three item types contradict the eight. | the deck is dated 23 Sep and titled as the reference level; base says that level was grenade, couch, plushie (`D076RBM29JS/1758638743.317009`); the eight answer the vendor's 8-item set two days later | designed, resolved |

**Coherence sweep** (`coherence_sweep.py`; record `Working_Files/01d_Coherence_Sweep.json`; two cold reviewers who saw only the ask and the injected records):

```
COHERENCE SWEEP (full): PASS
[PASS] sweep.bound: bound to 01_Universe_Inject.sql 7d1f2aaeb29c and 04_Prompt.txt 33c721d60945
[PASS] sweep.reviewers: 2 reviewers, each with a model, a brief hash that matches its kept brief, and a findings file
[PASS] sweep.findings: all 78 reviewer finding(s) are taken up or dismissed
[PASS] sweep.forks: 30 fork(s): 28 settled_in_data, 2 both_fair; no material fork is open
[PASS] sweep.prompt_sentences: no fork was settled by adding a prompt sentence
[PASS] sweep.open_sets: 1 quantifier span(s) in the prompt, each with a rule and a census; 43 open set(s) recorded
[PASS] sweep.siblings: 0 defect(s), each closed and with its sibling list
[PASS] sweep.base: 17 seeded fact(s) checked against the base, every conflicting hit dispositioned
[PASS] sweep.known_issues: 3 known-issue card(s) touched, each with a disposition
[PASS] sweep.conflicts: 0 value conflict candidate(s), each with a disposition
```

rev2 round (this SQL): two new cold reviewers, who saw only the ask and the rev2 records, reviewed the SQL bound above; 30 forks taken up (2 both_fair, 28 settled_in_data), 43 open sets with a rule and a census, 7 findings dismissed with a reason; material forks left open: 0. Rounds 1 to 5 reviewed rev1 (their briefs and findings are kept in `Working_Files/local_reviews/coherence/round1/` to `round5/`): both rev1 reviewers reached Delivered 8, Ready 36, Owed 52 and every material fork was settled in data before rev1 was submitted. What is left is base-only and is not graded: the design page's roster and its two statements on a full tray, and a remark in a group chat the persona's roster does not open (Platform follow-ups).

Forks, and what settled each (from the record):

| Id | What forked or conflicted | Material | Status | Settled by |
|---|---|---|---|---|
| F21 | Which message is Frederick's playable message | no | settled_in_data | only the DM asks for anything, and the prompt's third sentence (files in her Drive, links in the PlayableX channel) matches it word for word |
| F23 | Sharing: is it part of what he asks | no | settled_in_data | the message now says the notes cover 'what goes in the brief, what counts as ready, what to do with the tickets and who gets the files' |
| F24 | Who acts: Julia or the assistant | no | settled_in_data | 'do everything he's asking for in it, start to finish' leaves nothing for her; the message's requests include the reply and the post |
| F22 | What 'everything he's asking for in it' takes in | no | settled_in_data | the message itself asks for the counts 'here' and makes the notes part of the job; the prompt says 'everything ... start to finish' |
| F25 | Where inside her Drive the files go | no | both_fair | the rubric accepts any location owned by her (brief §4b: location) |
| F01 | Background music: what is owed and who has it | yes | settled_in_data | Brian's note on DES-406 now says Calvin is still cutting the ad track down to a loop, and Calvin's sheet names the row as the pack list does and says it is a new track made for the ad, not the in-game track |
| F02 | The three recoloured lines: state and who has them | yes | settled_in_data | the notes now say a changed file goes again 'and it sits with whoever the file came from'; the three ticket notes say 'FBX from Claire' |
| F03 | Which statement about sound the brief carries | yes | settled_in_data | the notes now name it: 'their rule from last time about when the music may start' |
| F04 | A line without a ticket; the weapon's projectile | yes | settled_in_data | the sentence is removed from the notes, and Brian's note on DES-398 says the cannon went in the first zip with its projectile and is what the vendor calls the rocket launcher |
| F05 | The bow's own state | yes | settled_in_data | the bow's file is now of Mon 29 Sep (DES-335, note stamped after Friday's thread), so no change follows the export; Robert's reply in the thread says to take it as it is |
| F06 | 'The last files from Claire' against six lines still waiting on her | yes | settled_in_data | the log's Monday line now reads 'another batch from Claire. She still has a few to send and a few are still mine to do', and the notes on the lines not yet exported are stamped Mon 29 Sep after that day's batch |
| F07 | Zombie characters: Delivered or Owed | no | settled_in_data | the note now reports the vendor's message as it is (they will re-rig from the pack and want one animation and four zombies picked), and Robert's post says all four are in the pack Marcus sent |
| F08 | What the counts count | yes | settled_in_data | the ask says 'give me the count for each state' right after 'where the item pack actually stands. Brian's pack list is where it starts'; the notes give a State to every row, one row per line of the pack list (sounds, 2D, font, cannon, background and zombies included); Brian's pack ticket tracks 'every line of the playable pack' |
| F09 | Category on the hand-off list | no | settled_in_data | the notes now say 'Line, Category and Ticket are as on his list' |
| F10 | Where in the PlayableX channel the links go | no | both_fair | the rubric accepts the two links in the channel in either position (dossier, platform follow-ups) |
| F11 | The kickoff hold cited by notes saved before it existed | no | settled_in_data | the hold and its invitations are now created 30 Sep 16:41 UTC, before the notes' last edit at 16:58 (plan/out/citation_chronology.txt) |
| F12 | Leonard's Trello comment on who is doing the work | no | settled_in_data | the comment now says the start is the one PlayableX gave after we asked for the pause, and that Julia is pulling the brief and the pack status together for Frederick |
| F13 | Ticket numbers against the team's base tickets | no | settled_in_data | the pack ticket and its children are now Design-team tickets, DES-313 to DES-409: the team's last base ticket is DES-312 of 7 May 2025, so numbers and dates run in order; the pack ticket's description says why it is kept there ('kept in Design so it stays off the ZM3D board'), which is the one record that explains the first Design-team activity since May and a parent with 96 children; Brian's last base tickets there are the same parent-and-children shape |
| F14 | Two different notes in the same second | no | settled_in_data | the notes on the delivered lines are now about a minute apart; plan/build_spec.py refuses two notes in one second and two differently worded notes less than 20 s apart |
| F15 | EXPORT: twelve files saved out of the project | yes | settled_in_data | Marcus's post in #zombie-match3d, dated after the twelve notes and addressed to Brian ('youll need to redo them'), with the vendor's base format rule |
| F16 | ARTHOLD: twelve bathroom files | yes | settled_in_data | Robert's note to Julia of 29 Sep, in their DM; the notes leave a changed file with whoever it came from |
| F17 | ZIP: eight instruments in Friday's zip | yes | settled_in_data | Brian's log of the outgoing folder |
| F18 | AUDIO: two cues from a library and a bought pack | yes | settled_in_data | Calvin's sound sources sheet with the notes' rule on sound |
| F19 | PICKS: the eight on the board | yes | settled_in_data | Robert's reply under Julia's bow post, read with his 25 Sep post |
| F20 | Which zombies and which animation | no | settled_in_data | Robert's post, which now adds that all four are in the pack Marcus sent; base has them in the pack Brian asked for |
| F26 | How a level is won and lost | yes | settled_in_data | the hand-off notes say 'How the level plays is on the design page', and the design page's core mechanic ('not a fail state - the loss screen only appears at zero health') with Brian's 24 Sep message in the PlayableX channel ('the win condition is eliminating all the zombies on screen') |
| F27 | The duck PlayableX asked for, and the zip it went in | yes | settled_in_data | the Plushie Chick's note, written at 14:06 UTC on 25 Sep after the vendor's 13:50 UTC message, names the vendor's word for it and says that message is about the zombie package, not the chick; the reference deck's board has the chick and no rubber duck; the vendor's 25 Sep message names 'the zombie assets' and its 29 Sep message, after reviewing, asks only about the zombies |
| F28 | What Julia did for the Dominoes playable | no | settled_in_data | Frederick's ask itself says what she did for the Dominoes playable ('write the brief they build from'); that brief is her 14 Mar post in the PlayableX channel, which the vendor thanked on 15 Mar |
| F29 | Fonts: who has it | yes | settled_in_data | the note now reads 'Waiting on the .ttf files from Martin', the wording of the lines waiting on Claire; the notes say who has it is whoever has to do the next thing |
| F30 | What the scenario is for | yes | settled_in_data | Robert answers in the same thread three minutes later ('Doesn't really matter', 'I think we should remain as is'), and Frederick's ask says 'Write it for the game as it is today'; the platform's /oe round 1 read it the same way (reading b refuted). Rev2 had marked this fork both fair, which was wrong |

**Re-verified facts.** Read again from their source with `tools/hg.py` in this session: the vendor channel from 15 Sep (formats, dates, the zombie question), Julia's DM with Brian of 23 Sep, Brian's two DMs of 24 Sep, the pull requests #459 to #471 (titles and times), Linear numbering per team and team memberships, the Trello card with its actions, the calendar precedent, the Contacts and Drive root shapes.

Unresolved: none that blocks the injection. Left for the pre-check (Platform follow-ups): the two unverified bulk routes in Linear, the Drive route to Brian's log, and the counted calls of a real run. UNVERIFIED-OK, with no row depending on them: the binary contents of the three base zips and the five masked zombie names.

```
STAGE GATE injection: PASS — Task_Authoring/task_inputs · 01_Universe_Inject.sql#7d1f2aaeb29c · 01_Hardness_Manifest.json#4a6b7a0f7097 · 01_Grounding_Dossier.md#796862c5b768 · solver/solver.py#3fb11113479e · 01c_Dispositions.json#d5e961bdb57b · 01c_Preflight_Report.json#7c44e825726b · 00_Assigments.md#82494197a841 · 01_Scenario_Design.md#75b70f53c84a · 01_Hardness_Manifest.draft.json#eeb7fafe905a · 01_Gradable_Surface.json#bfc0af31ecfd · __context__#3246c54345b9 · __assignment__#70579cebc8fc · __policy__#dc4ab5df3cdd · __gate_policy__#1f62b72f1b1d · __review__#b62863bc4291 · blocking 0 · warnings 2 · checks 47
[PASS] assignment.v3_context: Julia Lawson / Product Manager; hard cap <70%; freeze 2025-10-01T00:00:00Z; selected universe available; record dates and freeze-state evidence checked separately
[PASS] assignment.source_mode: source mode 'universe' for universe synthcut; KB bound; clock Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
[PASS] structure.outputs: 6 output(s) present: 01_Universe_Inject.sql, 01_Hardness_Manifest.json, 01_Grounding_Dossier.md, solver/solver.py, 01c_Dispositions.json, 01c_Preflight_Report.json
[PASS] structure.inputs: 4 input(s) present: 00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json
[PASS] structure.fresh: every output newer than its inputs (00_Assigments.md, 01_Scenario_Design.md, 01_Hardness_Manifest.draft.json, 01_Gradable_Surface.json)
[PASS] chain.scenario: upstream 'scenario' PASS pasted and current (01_Scenario_Design.md#75b70f53c84a, 01_Hardness_Manifest.draft.json#eeb7fafe905a, 01_Gradable_Surface.json#bfc0af31ecfd, 00_Assigments.md#82494197a841, __context__#3246c54345b9, __assignment__#70579cebc8fc, __policy__#dc4ab5df3cdd, __gate_policy__#cc8d944b3feb, __review__#6ba4eb7ccff8)
[PASS] structure.sections: 17 required sections present and non-empty (01_Grounding_Dossier.md)
[PASS] structure.placeholders: no placeholders in 01_Grounding_Dossier.md
[PASS] evidence.entity: 14/14 items carry a source pointer (min 90%)
[PASS] evidence.keyword: 14/14 items carry a source pointer (min 100%)
[PASS] evidence.persona_reach: 10/10 items carry a source pointer (min 100%)
[PASS] evidence.record_ledger: 18/18 items carry a source pointer (min 100%)
[PASS] evidence.facts_for_human: 21/21 items carry a source pointer (min 100%)
[PASS] tool.sql_lint: sql_lint re-run matches the paste: errors 0, warnings 8, rows 238
[PASS] tool.injection_lint: hg.py lint: 0 FAIL, 0 CHECK dispositioned, 0 INFO; sha256 7d1f2aaeb29c matches 01_Universe_Inject.sql
[PASS] review.warning_dispositions: every sql_lint warning class dispositioned (clock×8)
[PASS] tool.base_check: base_check pasted PASS; re-run PASS
[PASS] tool.base_claims: base_claims pasted PASS; re-run PASS
[PASS] tool.hardness_gate: hardness_gate (SQL) pasted PASS; re-run PASS
[PASS] structure.design_delta: final manifest keeps all 53 draft ids
[PASS] structure.preflight: 01c_Preflight_Report.json bound by sha256 to the current SQL, solver, surface, manifest and dispositions
[PASS] solver.contract: solver contract re-run PASS
[PASS] mutation.dispositions: 26 mutation and intervention results each carry a written disposition (01c_Dispositions.json)
[PASS] geometry.upper_bound: U 0.797 (153/192) vs 1 - cap 0.30 (V3 hard): PASS (bound PASS); re-run U 0.797 PASS (bound PASS)
[PASS] geometry.margin: L_max 0.5 vs (1 - cap) + 0.10: OK (advisory: the margin is a judgment, not a proof)
[PASS] liveness.dispositions: every liveness flag dispositioned (11 flag(s))
[PASS] forecast.preregistered: forecast hev_e258af3aaa3d48aa pre-registered in the ledger (UNCALIBRATED)
[PASS] tool.check_sql_pasted: persona_view check-sql --load-bearing output pasted with verdict PASS
[PASS] reach.injection: 26 scoped load-bearing ids YES for julia_lawson
[PASS] structure.facts_declared: manifest declares 17 load-bearing fact(s) in `facts`
[PASS] tool.fact_check: fact_check --no-leak pasted PASS; re-run PASS
[PASS] kb.coherence_hazards: coherence audit cites 14 valid hazard ids covering all 6 hazard categories
[PASS] kb.activity: 5 seeded speakers each cited with activity.json status; conventions.json cited
[PASS] kb.integrations: companions listed per integrations.json (6 INT ids, services ['contacts', 'gcal', 'gdocs', 'gdrive', 'gmail', 'gsheets', 'gslides', 'linear', 'slack', 'trello'])
[PASS] boundary.anchor_naming: 6 anchor-naming entries, each a noun phrase of ≤ 6 words
[PASS] review.counter_readings: 14 evidenced counter-readings (of 16 found; need ≥ 14) in 01_Grounding_Dossier.md
[PASS] review.coverage: self-review addresses all 9 required items
[PASS] review.unresolved: unresolved items listed (or 'none')
[PASS] v3.manifest_context: 01_Hardness_Manifest.json is bound to the current assignment, policy, source context and freeze
[PASS] readiness.context: explicit task/revision and current upstream evidence verified
[PASS] readiness.hardness_review: current evidenced review; deferred: []
[WARN] task.folder: the task folder is the bare default `task_inputs`: give each task its own folder (`Task_Authoring/task_inputs<Label>`) and pass it to every command, so two tasks never share one [first-pass check in warn mode: reported, not blocking]
[WARN] budget.injection: FAIL: budget.anchors: find rate above 0.20: A1 (up to 0.40), A2 (up to 0.45) (a record found that often is a variance unit).; budget.variance: 0 independent coin-flip habit(s) with a find-rate range inside 0.35-0.65, needs 4 (3 variance units over 3 habits; outside the range: C1 (0.; budget.average: P(six-run average strictly under 70.0%) is 1.000 with every unit at its low find rate and 0.764 at its high find rate (needs 0.90 at both).  (+3 more) — python3 Task_Authoring/tools/difficulty_budget.py check --task-dir <task_dir> [first-pass check in warn mode: reported, not blocking]
[PASS] exposure.units: path exposure PASS: every anchor and coin-flip unit's deciding record is off the paths the model sweeps, on the current SQL and budget
[PASS] sweep.forks: fork sweep PASS on the current SQL: no open material fork, every open set has a rule and a census
[PASS] skeleton.present: rubric skeleton PASS: on the expanded row set the anchors still carry the mode's loss and the coin-flip share holds
[PASS] handoff.pasted: pasted into the Self-review by --paste
```

