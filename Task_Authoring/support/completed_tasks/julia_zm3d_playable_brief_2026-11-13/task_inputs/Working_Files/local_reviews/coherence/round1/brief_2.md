# Coherence review brief (reviewer 2)

Bound to: 01_Universe_Inject.sql sha256 90a13ce4ba8961467f681de0637ecebfeee81a93bfdf7c77a53355daa625f78e; 04_Prompt.txt not written yet
Scope: full

## What you have

- The prompt below is not written yet; the ask is described instead.
- The universe: the base data, read through the search helpers (`python3.12 -B Task_Authoring/tools/hg.py search ... --task-dir Task_Authoring/task_inputs` picks this task's universe; `Task_Authoring/tools/persona_view.py`), and the injected records listed below. Injected records are laid over the base and are not in the base search, so read them here.
- The persona: Julia Lawson (Product Manager, julia.lawson@harmonygames.co). Only a record this persona can open settles anything.
- The universe date: Oct 1, 2025 (synth-cut), clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC). Nothing after the clock exists.

You are not given the task design, an expected answer or grading rows, and you must not look for them: do not open the task's Working_Files folder, its Oracle Events, its rubric or its reference notes. Work from the prompt and the records only, as a careful stranger would.

## What to report

1. Every material reading. A fork is two fair readings of the prompt, or of a record the prompt points to, that lead to different outcomes: a different decision, write, destination, recipient or content. Report it unless you can quote a record the persona can open that rules one reading out. "Less likely" does not rule a reading out. A claim by the item's own owner about their own work does not settle it. When no record speaks to an item at all, that is still a fork. When the two readings differ only in one reported figure (an amount, a count, a rate or a date), set figure_only to true.
2. Every contradiction. Two records that disagree about the same thing: an amount, a date, a status, an owner, a name or identity, a count, a lifecycle state (a closed ticket with later activity, a ticked checklist whose item is still open) or the order of events (a reply before its parent, a record that cites something created later). Report it whoever introduced it: injected against injected, injected against base, or base against base where the task has to read those base records.
3. Every population. For each phrase that defines a set (every, all, each, any, whoever, what still has to, remaining, outstanding, the rest, "if a ..."), in the prompt or in a record that carries the ask: write the membership rule as you read it, list every member you find in the universe, and list the edge members, where the rule does not say in or out.

Read the base around each injected record: its thread, its parent, the records it names, and other records about the same person, ticket, vendor or date. List what you could not read under not_checked.

## Output

Return one JSON object in exactly this shape (empty lists are fine; keep the keys). It is saved as `Working_Files/local_reviews/coherence/findings_2.json` in the task folder:

```json
{
  "reviewer": "<your reviewer id>",
  "forks": [
    {"id": "F1",
     "span": "<the words of the prompt, or of a record, that can be read two ways>",
     "record_ids": ["<records involved>"],
     "reading_a": {"reading": "<first fair reading>", "outcome": "<what gets decided, written, sent or reported>"},
     "reading_b": {"reading": "<second fair reading>", "outcome": "<what gets decided, written, sent or reported>"},
     "material": true,
     "figure_only": false,
     "reason": "<why the outcomes differ, or why they do not>",
     "settling_record": "<id of a record the persona can open that rules one reading out, or null>"}
  ],
  "contradictions": [
    {"id": "C1",
     "record_ids": ["<record>", "<record it disagrees with>"],
     "about": "<the person, ticket, vendor, file or event>",
     "field": "amount | date | status | owner | identity | count | lifecycle | chronology | other",
     "value_a": "<what the first record says>",
     "value_b": "<what the second record says>",
     "introduced_by": "injected | base | both",
     "matters_because": "<what a reader would get wrong>"}
  ],
  "open_sets": [
    {"id": "S1",
     "span": "<the words that define a population>",
     "where": "prompt | <record id>",
     "rule": "<who or what is in, as you read it>",
     "members": ["<every member you found>"],
     "edge_members": [{"id": "<record>", "why": "<why the rule does not say in or out>"}]}
  ],
  "not_checked": ["<anything you could not read or did not get to>"]
}
```

## The ask (no prompt is written yet)

The prompt will point the persona at:
- Frederick's playable message: 7e84f1cf59f8e95fef961268fbf37cc1
- the PlayableX channel: C08H78VJG80
- my Drive: d_8140f09bf9f1b94cb8ee2d

Records that carry parts of the ask (injected ones are in the listing below; read the others in the base):
- f_8c1d0bca1d1d5fde4c5008
- f_956e60ec7f2f7977d98934
- C090N54TG79/1758823946.262829
- ZOM-567
- C08H78VJG80/1758022459.227279 (base)
- C08H78VJG80/1758283671.878269 (base)
- page_zm3d_gdd (base)
- confluence:page_zm3d_gdd (base)
- evt_421695d009e589ee85296c
- d7d31caf63ee33db2b7ed271
- f_6a2fa8e61b31139ca8e3d4
- C090N54TG79/1759167068.371289
- C08H78VJG80/1759140968.965099 (base)
- C08R8CHB0QL/1758922879.243189
- C08R8CHB0QL/1758904025.123869
- C08H78VJG80/1744637266.363689 (base)
- C08H78VJG80/1759226395.551469 (base)
- C08H78VJG80/1757956024.883249 (base)
- C08H78VJG80/1757695108.506159 (base)
- D05SD5QLG94/1759256494.852159

# Injected records (238 records in 10 services: contacts, gcal, gdocs, gdrive, gmail, gsheets, gslides, linear, slack, trello)

## contacts

### contacts container contacts

#### d7d31caf63ee33db2b7ed271
table: contacts.contacts | statement: insert
first_name: PlayableX
last_name: Intake
gender: Unknown
status: Unknown
job: Project intake (playable ads)
email: intake@playablex.ai

## gcal

### gcal container brian.foster@harmonygames.co

#### evt_a78612f3eaf04ce8461eb4
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
calendar_id: brian.foster@harmonygames.co
summary: ZM3D playable kickoff with PlayableX
start_ts: 2025-11-03T17:00:00Z
end_ts: 2025-11-03T17:30:00Z
start_json: {"dateTime": "2025-11-03T17:00:00Z"}
end_json: {"dateTime": "2025-11-03T17:30:00Z"}
organizer_email: frederick.stone@harmonygames.co
creator_email: frederick.stone@harmonygames.co
attendees_json: [{"email": "brian.foster@harmonygames.co", "organizer": false, "responseStatus": "needsAction", "self": true}, {"email": "frederick.stone@harmonygames.co", "organizer": true, "responseStatus": "accepted"}, {"email": "julia.lawson@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}, {"email": "robert@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}]
status: confirmed
transparency: opaque
sequence: 0
created: 2025-09-30T17:05:43Z
updated: 2025-09-30T17:05:43Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

### gcal container frederick.stone@harmonygames.co

#### evt_d622b6ab55401d23626674
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
calendar_id: frederick.stone@harmonygames.co
summary: ZM3D playable kickoff with PlayableX
start_ts: 2025-11-03T17:00:00Z
end_ts: 2025-11-03T17:30:00Z
start_json: {"dateTime": "2025-11-03T17:00:00Z"}
end_json: {"dateTime": "2025-11-03T17:30:00Z"}
organizer_email: frederick.stone@harmonygames.co
creator_email: frederick.stone@harmonygames.co
attendees_json: [{"email": "brian.foster@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}, {"email": "frederick.stone@harmonygames.co", "organizer": true, "responseStatus": "accepted", "self": true}, {"email": "julia.lawson@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}, {"email": "robert@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}]
status: confirmed
transparency: opaque
sequence: 0
created: 2025-09-30T17:05:43Z
updated: 2025-09-30T17:05:43Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

### gcal container julia.lawson@harmonygames.co

#### evt_421695d009e589ee85296c
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
calendar_id: julia.lawson@harmonygames.co
summary: ZM3D playable kickoff with PlayableX
start_ts: 2025-11-03T17:00:00Z
end_ts: 2025-11-03T17:30:00Z
start_json: {"dateTime": "2025-11-03T17:00:00Z"}
end_json: {"dateTime": "2025-11-03T17:30:00Z"}
organizer_email: frederick.stone@harmonygames.co
creator_email: frederick.stone@harmonygames.co
attendees_json: [{"email": "brian.foster@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}, {"email": "frederick.stone@harmonygames.co", "organizer": true, "responseStatus": "accepted"}, {"email": "julia.lawson@harmonygames.co", "organizer": false, "responseStatus": "needsAction", "self": true}, {"email": "robert@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}]
status: confirmed
transparency: opaque
sequence: 0
created: 2025-09-30T17:05:43Z
updated: 2025-09-30T17:05:43Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

### gcal container robert@harmonygames.co

#### evt_1c99b11a66cfd562b13d9c
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
calendar_id: robert@harmonygames.co
summary: ZM3D playable kickoff with PlayableX
start_ts: 2025-11-03T17:00:00Z
end_ts: 2025-11-03T17:30:00Z
start_json: {"dateTime": "2025-11-03T17:00:00Z"}
end_json: {"dateTime": "2025-11-03T17:30:00Z"}
organizer_email: frederick.stone@harmonygames.co
creator_email: frederick.stone@harmonygames.co
attendees_json: [{"email": "brian.foster@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}, {"email": "frederick.stone@harmonygames.co", "organizer": true, "responseStatus": "accepted"}, {"email": "julia.lawson@harmonygames.co", "organizer": false, "responseStatus": "needsAction"}, {"email": "robert@harmonygames.co", "organizer": false, "responseStatus": "needsAction", "self": true}]
status: confirmed
transparency: opaque
sequence: 0
created: 2025-09-30T17:05:43Z
updated: 2025-09-30T17:05:43Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

## gdocs

### gdocs container f_8c1d0bca1d1d5fde4c5008

#### f_8c1d0bca1d1d5fde4c5008
table: gdocs.docs_documents | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:25:41Z
title: ZM3D playable: hand-off notes
owner_email: frederick.stone@harmonygames.co
shared_with_emails_json: ["julia.lawson@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co"]
visibility: private
body_text:
    ZM3D playable: hand-off notes
    
    The brief. One doc PlayableX can build from: which scenario we picked and what it is for, the eight items on the board and that everything else on the list is an extra they can swap in, the four zombies and the one animation, how a level is won and lost and how many slots the tray has, what they can use for sound and when the music may start, and the start date. How the level plays is on the design page; your deck of the reference level has what we built for them. What they told us about formats still holds, and so does what they told us about sound last time.
    
    The hand-off list. One row per line of Brian's pack list, with these columns: Line, Category, Board set, State, What's owed, Who has it, Ticket. Board set is Default for the eight on the board and Extra for every other board item; leave it empty for anything that isn't a board item.
    
    State is one of three words, nothing else. Delivered: PlayableX has the current file and can use it. Ready: exported in a format they take and sitting in the outgoing folder, it opens, it is the current version and nobody is changing it. Owed: anything else. For an Owed line say what is owed, and who has it, meaning whoever has to do the next thing.
    
    Brian's note on each ticket says what he did with the line. Take it as it stands unless something later says otherwise, and go by how things stand today, not the day he wrote it: if someone who knows the file or the art has said something since, that counts. If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again.
    
    Sound: we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we have our own version.
    
    Tickets live under Brian's pack ticket, one per line. An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. A line without a ticket gets one under the pack ticket. Leave the Delivered and Ready ones as they are.
    
    Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address, which is in Contacts.
created_time: 2025-09-30T16:25:41Z
modified_time: 2025-09-30T16:58:19Z

### gdocs container f_faf4d7c167d14a1127dcc3

#### f_faf4d7c167d14a1127dcc3
table: gdocs.docs_documents | statement: insert | author: brian.foster@harmonygames.co | date: 2025-09-25T15:58:14Z
title: Outgoing folder - what's in it
owner_email: brian.foster@harmonygames.co
shared_with_emails_json: ["frederick.stone@harmonygames.co", "julia.lawson@harmonygames.co"]
visibility: private
body_text:
    Outgoing folder - what's in it
    So I don't lose track of what I've put in there.
    Thu 25 Sep: the models saved out of the project, and the first files from Claire.
    Fri 26 Sep: more files from Claire. The music instruments went in as one zip. The sound files.
    Mon 29 Sep: the last files from Claire.
    Tue 30 Sep: the zip with Friday's music instruments got cut off on upload, it won't unpack on my side, and those eight aren't in the folder any other way. I still have Claire's files, I'll put them back when we pick this up again.
created_time: 2025-09-25T15:58:14Z
modified_time: 2025-09-30T09:12:26Z

## gdrive

### gdrive container d_175c0d7bc72ed244b944cb

#### f_8c1d0bca1d1d5fde4c5008
table: gdrive.drive_files | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:25:41Z
name: ZM3D playable: hand-off notes
mime_type: application/vnd.google-apps.document
parents_json: ["d_175c0d7bc72ed244b944cb"]
owner_email: frederick.stone@harmonygames.co
shared_with_emails_json: ["julia.lawson@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co"]
shared_roles_json: [{"email": "julia.lawson@harmonygames.co", "role": "reader"}, {"email": "brian.foster@harmonygames.co", "role": "reader"}, {"email": "robert@harmonygames.co", "role": "reader"}]
visibility: private
owners_json: ["frederick.stone@harmonygames.co"]
modified_time: 2025-09-30T16:58:19Z
created_time: 2025-09-30T16:25:41Z

### gdrive container d_49b9dfa5208d400d9b3937

#### f_b2387e31d46d3a7b3fa2a9
table: gdrive.drive_files | statement: insert | author: calvin.price@harmonygames.co | date: 2025-09-12T15:42:11Z
name: ZM3D sound sources
mime_type: application/vnd.google-apps.spreadsheet
parents_json: ["d_49b9dfa5208d400d9b3937"]
owner_email: calvin.price@harmonygames.co
shared_with_emails_json: ["robert@harmonygames.co", "julia.lawson@harmonygames.co", "brian.foster@harmonygames.co"]
shared_roles_json: [{"email": "robert@harmonygames.co", "role": "writer"}, {"email": "julia.lawson@harmonygames.co", "role": "reader"}, {"email": "brian.foster@harmonygames.co", "role": "reader"}]
visibility: private
owners_json: ["calvin.price@harmonygames.co"]
modified_time: 2025-09-26T20:10:36Z
created_time: 2025-09-12T15:42:11Z

### gdrive container d_8140f09bf9f1b94cb8ee2d

#### f_6a2fa8e61b31139ca8e3d4
table: gdrive.drive_files | statement: insert | author: julia.lawson@harmonygames.co | date: 2025-09-23T19:31:22Z
name: ZM3D playable - reference level
mime_type: application/vnd.google-apps.presentation
parents_json: ["d_8140f09bf9f1b94cb8ee2d"]
owner_email: julia.lawson@harmonygames.co
shared_with_emails_json: ["brian.foster@harmonygames.co"]
shared_roles_json: [{"email": "brian.foster@harmonygames.co", "role": "reader"}]
visibility: private
owners_json: ["julia.lawson@harmonygames.co"]
modified_time: 2025-09-23T19:55:47Z
created_time: 2025-09-23T19:31:22Z

### gdrive container d_fc22d5941b2aeb5c03ad32

#### f_956e60ec7f2f7977d98934
table: gdrive.drive_files | statement: insert | author: brian.foster@harmonygames.co | date: 2025-09-25T06:48:27Z
name: ZM3D playable - pack list
mime_type: application/vnd.google-apps.spreadsheet
parents_json: ["d_fc22d5941b2aeb5c03ad32"]
owner_email: brian.foster@harmonygames.co
shared_with_emails_json: ["frederick.stone@harmonygames.co", "julia.lawson@harmonygames.co", "robert@harmonygames.co"]
shared_roles_json: [{"email": "frederick.stone@harmonygames.co", "role": "reader"}, {"email": "julia.lawson@harmonygames.co", "role": "reader"}, {"email": "robert@harmonygames.co", "role": "reader"}]
visibility: private
owners_json: ["brian.foster@harmonygames.co"]
modified_time: 2025-09-26T17:25:08Z
created_time: 2025-09-25T06:48:27Z

#### f_faf4d7c167d14a1127dcc3
table: gdrive.drive_files | statement: insert | author: brian.foster@harmonygames.co | date: 2025-09-25T15:58:14Z
name: Outgoing folder - what's in it
mime_type: application/vnd.google-apps.document
parents_json: ["d_fc22d5941b2aeb5c03ad32"]
owner_email: brian.foster@harmonygames.co
shared_with_emails_json: ["frederick.stone@harmonygames.co", "julia.lawson@harmonygames.co"]
shared_roles_json: [{"email": "frederick.stone@harmonygames.co", "role": "reader"}, {"email": "julia.lawson@harmonygames.co", "role": "reader"}]
visibility: private
owners_json: ["brian.foster@harmonygames.co"]
modified_time: 2025-09-30T09:12:26Z
created_time: 2025-09-25T15:58:14Z

## gmail

### gmail container brian.foster@harmonygames.co

#### brian.foster@harmonygames.co/1844709365384121300
table: gmail.gmail_threads | statement: insert
user_email: brian.foster@harmonygames.co
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@

#### brian.foster@harmonygames.co/<calendar-c94e8bd4-a0ec-0177-cb05-b68828195e96@google.com>
table: gmail.gmail_messages | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: brian.foster@harmonygames.co/1844709365384121300
thread_id: brian.foster@harmonygames.co/1844709365384121300
user_email: brian.foster@harmonygames.co
label_ids_json: ["INBOX", "CATEGORY_PERSONAL"]
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@
date: 2025-09-30T17:05:43Z
subject: Invitation: ZM3D playable kickoff with PlayableX @ Mon Nov 3, 2025 9am - 9:30am (PST) (brian.foster@harmonygames.co)
from_email: frederick.stone@harmonygames.co
from_name: frederick stone
to_json: ["julia.lawson@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co"]
reply_to_json: ["frederick stone <frederick.stone@harmonygames.co>"]
body_text:
    ZM3D playable kickoff with PlayableX
    Monday Nov 3, 2025 ⋅ 9am – 9:30am
    Pacific Time - Los Angeles
    
    Organizer
    Frederick Stone
    frederick.stone@harmonygames.co
    
    Guests
    Frederick Stone - organizer
    julia.lawson@harmonygames.co
    brian.foster@harmonygames.co
    robert@harmonygames.co

### gmail container julia.lawson@harmonygames.co

#### julia.lawson@harmonygames.co/1844709365383943310
table: gmail.gmail_threads | statement: insert
user_email: julia.lawson@harmonygames.co
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@

#### julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>
table: gmail.gmail_messages | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: julia.lawson@harmonygames.co/1844709365383943310
thread_id: julia.lawson@harmonygames.co/1844709365383943310
user_email: julia.lawson@harmonygames.co
label_ids_json: ["INBOX", "CATEGORY_PERSONAL"]
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@
date: 2025-09-30T17:05:43Z
subject: Invitation: ZM3D playable kickoff with PlayableX @ Mon Nov 3, 2025 9am - 9:30am (PST) (julia.lawson@harmonygames.co)
from_email: frederick.stone@harmonygames.co
from_name: frederick stone
to_json: ["julia.lawson@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co"]
reply_to_json: ["frederick stone <frederick.stone@harmonygames.co>"]
body_text:
    ZM3D playable kickoff with PlayableX
    Monday Nov 3, 2025 ⋅ 9am – 9:30am
    Pacific Time - Los Angeles
    
    Organizer
    Frederick Stone
    frederick.stone@harmonygames.co
    
    Guests
    Frederick Stone - organizer
    julia.lawson@harmonygames.co
    brian.foster@harmonygames.co
    robert@harmonygames.co

### gmail container robert@harmonygames.co

#### robert@harmonygames.co/1844709365383420856
table: gmail.gmail_threads | statement: insert
user_email: robert@harmonygames.co
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@

#### robert@harmonygames.co/<calendar-4263dbb8-cab6-41a8-95c1-dca6f6f7e53b@google.com>
table: gmail.gmail_messages | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T17:05:43Z | thread: robert@harmonygames.co/1844709365383420856
thread_id: robert@harmonygames.co/1844709365383420856
user_email: robert@harmonygames.co
label_ids_json: ["INBOX", "CATEGORY_PERSONAL"]
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@
date: 2025-09-30T17:05:43Z
subject: Invitation: ZM3D playable kickoff with PlayableX @ Mon Nov 3, 2025 9am - 9:30am (PST) (robert@harmonygames.co)
from_email: frederick.stone@harmonygames.co
from_name: frederick stone
to_json: ["julia.lawson@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co"]
reply_to_json: ["frederick stone <frederick.stone@harmonygames.co>"]
body_text:
    ZM3D playable kickoff with PlayableX
    Monday Nov 3, 2025 ⋅ 9am – 9:30am
    Pacific Time - Los Angeles
    
    Organizer
    Frederick Stone
    frederick.stone@harmonygames.co
    
    Guests
    Frederick Stone - organizer
    julia.lawson@harmonygames.co
    brian.foster@harmonygames.co
    robert@harmonygames.co

## gsheets

### gsheets container f_956e60ec7f2f7977d98934

#### f_956e60ec7f2f7977d98934/0
table: gsheets.sheets_sheets | statement: insert | thread: f_956e60ec7f2f7977d98934
spreadsheet_id: f_956e60ec7f2f7977d98934
sheet_id: 0
title: Pack
index: 0
row_count: 1000
column_count: 26
grid_json:
    Line | Kind | Category | Went out | Ticket
    Couch | Board item | Living Room | zip 24 Sep | ZOM-568
    Couch and Pillow | Board item | Living Room | zip 24 Sep | ZOM-569
    Alarm Clock | Board item | Living Room |  | ZOM-570
    Record Player | Board item | Living Room |  | ZOM-571
    Retro TV | Board item | Living Room |  | ZOM-572
    Desk Lamp | Board item | Living Room |  | ZOM-573
    Small Lamp | Board item | Living Room |  | ZOM-574
    Fly Zapper | Board item | Living Room |  | ZOM-575
    Grenade | Board item | Survival | zip 24 Sep | ZOM-576
    Chainsaw | Board item | Survival |  | ZOM-577
    Cute Axe | Board item | Survival |  | ZOM-578
    Cute Hammer | Board item | Survival |  | ZOM-579
    Dynamite | Board item | Survival |  | ZOM-580
    Shuriken | Board item | Survival |  | ZOM-581
    Saber | Board item | Survival |  | ZOM-582
    Safe | Board item | Survival |  | ZOM-583
    Flashlight | Board item | Survival |  | ZOM-584
    Fire Extinguisher | Board item | Survival |  | ZOM-585
    Propane Tank | Board item | Survival |  | ZOM-586
    Plushie Bunny | Board item | Toys | zip 24 Sep | ZOM-587
    Plushie Chick | Board item | Toys | zip 24 Sep (second) | ZOM-588
    Bow | Board item | Toys |  | ZOM-589
    Cone | Board item | Toys |  | ZOM-590
    Dice | Board item | Toys |  | ZOM-591
    Gift Box | Board item | Toys |  | ZOM-592
    Plushie Dog | Board item | Toys |  | ZOM-593
    Plushie Whale | Board item | Toys |  | ZOM-594
    Whistle | Board item | Toys |  | ZOM-595
    Wooden Tower | Board item | Toys |  | ZOM-596
    Toy Car | Board item | Toys |  | ZOM-597
    Toy Boat | Board item | Toys |  | ZOM-598
    Toy Airplane | Board item | Toys |  | ZOM-599
    Toy Train | Board item | Toys |  | ZOM-600
    Beach Ball | Board item | Toys |  | ZOM-601
    Bathroom Scale | Board item | Bathroom |  | ZOM-602
    Bathtub | Board item | Bathroom |  | ZOM-603
    Cabinet Sink | Board item | Bathroom |  | ZOM-604
    Flip Flops | Board item | Bathroom |  | ZOM-605
    Iron | Board item | Bathroom |  | ZOM-606
    Ironing Board | Board item | Bathroom |  | ZOM-607
    Plunger | Board item | Bathroom |  | ZOM-608
    Slippers | Board item | Bathroom |  | ZOM-609
    Toilet | Board item | Bathroom |  | ZOM-610
    Toilet Paper | Board item | Bathroom |  | ZOM-611
    Wash Basin | Board item | Bathroom |  | ZOM-612
    Washing Machine | Board item | Bathroom |  | ZOM-613
    Rubber Ducky | Board item | Bathroom |  | ZOM-614
    Coffee Machine | Board item | Kitchen |  | ZOM-615
    Cooler | Board item | Kitchen |  | ZOM-616
    Ice Cream Machine | Board item | Kitchen |  | ZOM-617
    Kitchen Mixer | Board item | Kitchen |  | ZOM-618
    Microwave | Board item | Kitchen |  | ZOM-619
    Oven | Board item | Kitchen |  | ZOM-620
    Refrigerator | Board item | Kitchen |  | ZOM-621
    Stove | Board item | Kitchen |  | ZOM-622
    Toaster | Board item | Kitchen |  | ZOM-623
    Dutch Oven | Board item | Kitchen |  | ZOM-624
    Rolling Pin | Board item | Kitchen |  | ZOM-625
    Round Kettle | Board item | Kitchen |  | ZOM-626
    Round Pan | Board item | Kitchen |  | ZOM-627
    Spatula | Board item | Kitchen |  | ZOM-628
    Whisk | Board item | Kitchen |  | ZOM-629
    Ladle | Board item | Kitchen |  | ZOM-630
    Small Kettle | Board item | Kitchen |  | ZOM-631
    Tall Kettle | Board item | Kitchen |  | ZOM-632
    Acoustic Guitar | Board item | Music Instruments |  | ZOM-633
    Cello | Board item | Music Instruments |  | ZOM-634
    Cymbals | Board item | Music Instruments |  | ZOM-635
    Electric Guitar | Board item | Music Instruments |  | ZOM-636
    Harp | Board item | Music Instruments |  | ZOM-637
    Tambourine | Board item | Music Instruments |  | ZOM-638
    Trumpet | Board item | Music Instruments |  | ZOM-639
    Xylophone | Board item | Music Instruments |  | ZOM-640
    Music Keyboard | Board item | Music Instruments |  | ZOM-641
    Grand Piano | Board item | Music Instruments |  | ZOM-642
    Cactus Plant | Board item | Garden |  | ZOM-643
    Barrel | Board item | Garden |  | ZOM-644
    Bench | Board item | Garden |  | ZOM-645
    Flower Pot | Board item | Garden |  | ZOM-646
    Garden Shears | Board item | Garden |  | ZOM-647
    Watering Can | Board item | Garden |  | ZOM-648
    Wooden Bucket | Board item | Garden |  | ZOM-649
    Wheelbarrow | Board item | Garden |  | ZOM-650
    Wooden Crate | Board item | Garden |  | ZOM-651
    Cannon | Weapon |  | zip 24 Sep | ZOM-652
    Background | Background |  | zip 24 Sep | ZOM-653
    Zombie characters | Zombies |  | pack 26 Sep | ZOM-654
    Matching sound | Sound |  |  | ZOM-655
    Rocket sound | Sound |  |  | ZOM-656
    Explosion sound | Sound |  |  | ZOM-657
    Success sound | Sound |  |  | ZOM-658
    Failure sound | Sound |  |  | ZOM-659
    Background music | Sound |  |  | ZOM-660
    Item visuals | 2D |  |  | ZOM-661
    UI elements | 2D |  |  | ZOM-662
    Fonts | Font |  |  | ZOM-663

#### f_956e60ec7f2f7977d98934
table: gsheets.sheets_spreadsheets | statement: insert | author: brian.foster@harmonygames.co | date: 2025-09-25T06:48:27Z
title: ZM3D playable - pack list
owner_email: brian.foster@harmonygames.co
shared_with_emails_json: ["frederick.stone@harmonygames.co", "julia.lawson@harmonygames.co", "robert@harmonygames.co"]
visibility: private
created_time: 2025-09-25T06:48:27Z
modified_time: 2025-09-26T17:25:08Z

### gsheets container f_b2387e31d46d3a7b3fa2a9

#### f_b2387e31d46d3a7b3fa2a9/0
table: gsheets.sheets_sheets | statement: insert | thread: f_b2387e31d46d3a7b3fa2a9
spreadsheet_id: f_b2387e31d46d3a7b3fa2a9
sheet_id: 0
title: Sources
index: 0
row_count: 1000
column_count: 26
grid_json:
    Cue | Where it came from | OK outside the game | Replacement
    Matching sound | made here | yes | 
    Combo meter scale (endless mode) | made here: pitched in Reaper from the sample Robert gave me | yes | 
    Rocket sound | Soundly library (Robert's seat) | no | not made yet, Calvin
    Explosion sound | Universal Sound FX pack (Unity Asset Store, Robert's) | no | not made yet, Calvin
    Success sound | made here | yes | 
    Failure sound | made here | yes | 
    Soundtrack | generated, edited here | yes | 
    Laptop error, shutdown | Windows system sounds | no | Robert is swapping them

#### f_b2387e31d46d3a7b3fa2a9
table: gsheets.sheets_spreadsheets | statement: insert | author: calvin.price@harmonygames.co | date: 2025-09-12T15:42:11Z
title: ZM3D sound sources
owner_email: calvin.price@harmonygames.co
shared_with_emails_json: ["robert@harmonygames.co", "julia.lawson@harmonygames.co", "brian.foster@harmonygames.co"]
visibility: private
created_time: 2025-09-12T15:42:11Z
modified_time: 2025-09-26T20:10:36Z

## gslides

### gslides container f_6a2fa8e61b31139ca8e3d4

#### f_6a2fa8e61b31139ca8e3d4/slide_0e3a07bbbcdd
table: gslides.slides_pages | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
object_id: slide_0e3a07bbbcdd
index: 1
layout: TITLE_AND_BODY

#### f_6a2fa8e61b31139ca8e3d4/slide_0e3a07bbbcdd/el_40c443410200
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_0e3a07bbbcdd
object_id: el_40c443410200
kind: SHAPE
text: Board

#### f_6a2fa8e61b31139ca8e3d4/slide_0e3a07bbbcdd/el_bccaace88002
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_0e3a07bbbcdd
object_id: el_bccaace88002
kind: SHAPE
text: Grenade (red, green), Couch, Couch and Pillow, Plushie Bunny, Plushie Chick.

#### f_6a2fa8e61b31139ca8e3d4/slide_70fbd773b799
table: gslides.slides_pages | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
object_id: slide_70fbd773b799
index: 2
layout: TITLE_AND_BODY

#### f_6a2fa8e61b31139ca8e3d4/slide_70fbd773b799/el_23bcd0034408
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_70fbd773b799
object_id: el_23bcd0034408
kind: SHAPE
text: A mix, nothing fixed yet.

#### f_6a2fa8e61b31139ca8e3d4/slide_70fbd773b799/el_d80b1de7a1b7
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_70fbd773b799
object_id: el_d80b1de7a1b7
kind: SHAPE
text: Zombies

#### f_6a2fa8e61b31139ca8e3d4/slide_97402415f9e1
table: gslides.slides_pages | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
object_id: slide_97402415f9e1
index: 3
layout: TITLE_AND_BODY

#### f_6a2fa8e61b31139ca8e3d4/slide_97402415f9e1/el_3ab2af2a0848
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_97402415f9e1
object_id: el_3ab2af2a0848
kind: SHAPE
text: Win and lose

#### f_6a2fa8e61b31139ca8e3d4/slide_97402415f9e1/el_9ea4f88ee342
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_97402415f9e1
object_id: el_9ea4f88ee342
kind: SHAPE
text: Win: every zombie on screen is eliminated. Lose: the zombies reach us and our HP runs out.

#### f_6a2fa8e61b31139ca8e3d4/slide_f9b479c24b7b
table: gslides.slides_pages | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
object_id: slide_f9b479c24b7b
index: 0
layout: TITLE_AND_BODY

#### f_6a2fa8e61b31139ca8e3d4/slide_f9b479c24b7b/el_829ffaef8aab
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_f9b479c24b7b
object_id: el_829ffaef8aab
kind: SHAPE
text: Built 23 Sep on the playable levels branch. Brian recorded it for PlayableX.

#### f_6a2fa8e61b31139ca8e3d4/slide_f9b479c24b7b/el_c5c63f51d806
table: gslides.slides_page_elements | statement: insert | thread: f_6a2fa8e61b31139ca8e3d4
presentation_id: f_6a2fa8e61b31139ca8e3d4
page_object_id: slide_f9b479c24b7b
object_id: el_c5c63f51d806
kind: SHAPE
text: ZM3D playable - reference level

#### f_6a2fa8e61b31139ca8e3d4
table: gslides.slides_presentations | statement: insert | author: julia.lawson@harmonygames.co | date: 2025-09-23T19:31:22Z
title: ZM3D playable - reference level
owner_email: julia.lawson@harmonygames.co
shared_with_emails_json: ["brian.foster@harmonygames.co"]
visibility: private
created_time: 2025-09-23T19:31:22Z
modified_time: 2025-09-23T19:55:47Z

## linear

### linear container ZOM-568

#### a022e31f-afd4-5ab4-81a2-fd1d62c1c2cf
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:23:35Z | thread: ZOM-568
issue_id: ZOM-568
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:23:35Z
updated_at: 2025-09-25T07:23:35Z
sequence: 1

### linear container ZOM-569

#### c9e602eb-3bf5-533a-9571-506ee278e07b
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:23:53Z | thread: ZOM-569
issue_id: ZOM-569
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:23:53Z
updated_at: 2025-09-25T07:23:53Z
sequence: 1

### linear container ZOM-570

#### 513dd4bc-6bd5-5aaf-b4da-feb984524384
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:21:19Z | thread: ZOM-570
issue_id: ZOM-570
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:21:19Z
updated_at: 2025-09-25T15:21:19Z
sequence: 1

### linear container ZOM-571

#### 7daa1ebe-84c9-5aba-ba45-22f69fdfd01f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:22:57Z | thread: ZOM-571
issue_id: ZOM-571
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:22:57Z
updated_at: 2025-09-25T15:22:57Z
sequence: 1

### linear container ZOM-572

#### 395bc5d2-8e32-537e-9286-a216ddf6b5af
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:24:29Z | thread: ZOM-572
issue_id: ZOM-572
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:24:29Z
updated_at: 2025-09-25T15:24:29Z
sequence: 1

### linear container ZOM-573

#### 4cf25a71-ccf1-58cf-a70d-da1286b1320e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:37:26Z | thread: ZOM-573
issue_id: ZOM-573
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:37:26Z
updated_at: 2025-09-26T09:37:26Z
sequence: 1

### linear container ZOM-574

#### 558aa24b-3da7-5537-aaba-e8f68ffdabcf
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:39:29Z | thread: ZOM-574
issue_id: ZOM-574
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:39:29Z
updated_at: 2025-09-26T09:39:29Z
sequence: 1

### linear container ZOM-575

#### 33933dbf-208d-5fab-be50-5bc02a0cf709
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:14:37Z | thread: ZOM-575
issue_id: ZOM-575
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-26T16:14:37Z
updated_at: 2025-09-26T16:14:37Z
sequence: 1

### linear container ZOM-576

#### c2522fd7-9203-57c6-8bfc-85eee899b758
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:23:56Z | thread: ZOM-576
issue_id: ZOM-576
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:23:56Z
updated_at: 2025-09-25T07:23:56Z
sequence: 1

### linear container ZOM-577

#### deb96bcb-7d02-5c29-8c41-79fcbd7c1c61
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:05:17Z | thread: ZOM-577
issue_id: ZOM-577
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:05:17Z
updated_at: 2025-09-25T08:05:17Z
sequence: 1

### linear container ZOM-578

#### 9b58d4b0-45c2-572d-8ce5-d64f5e2834ea
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:09:04Z | thread: ZOM-578
issue_id: ZOM-578
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:09:04Z
updated_at: 2025-09-25T08:09:04Z
sequence: 1

### linear container ZOM-579

#### c015eaec-be3a-5c98-9ea0-aa07f9825bf9
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:11:13Z | thread: ZOM-579
issue_id: ZOM-579
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:11:13Z
updated_at: 2025-09-25T08:11:13Z
sequence: 1

### linear container ZOM-580

#### 158e9cc2-7625-5075-a6f9-ae787f05959f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:13:02Z | thread: ZOM-580
issue_id: ZOM-580
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:13:02Z
updated_at: 2025-09-25T08:13:02Z
sequence: 1

### linear container ZOM-581

#### 637efd91-10a6-5346-92d0-0816d54f4dec
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:14:52Z | thread: ZOM-581
issue_id: ZOM-581
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:14:52Z
updated_at: 2025-09-25T08:14:52Z
sequence: 1

### linear container ZOM-582

#### 2f4ca97c-f3d4-5bb6-ab48-3bddf1130fea
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:40:54Z | thread: ZOM-582
issue_id: ZOM-582
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:40:54Z
updated_at: 2025-09-26T09:40:54Z
sequence: 1

### linear container ZOM-583

#### 0a858079-e758-5bf9-a159-c65c627eb62e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:42:45Z | thread: ZOM-583
issue_id: ZOM-583
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:42:45Z
updated_at: 2025-09-26T09:42:45Z
sequence: 1

### linear container ZOM-584

#### b2447303-d424-5811-b7d4-72aed39b7a8b
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:06:27Z | thread: ZOM-584
issue_id: ZOM-584
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:06:27Z
updated_at: 2025-09-29T11:06:27Z
sequence: 1

### linear container ZOM-585

#### 80866ff3-da39-5209-aa58-5281e7bb5d2d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:16:18Z | thread: ZOM-585
issue_id: ZOM-585
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-26T16:16:18Z
updated_at: 2025-09-26T16:16:18Z
sequence: 1

### linear container ZOM-586

#### abd87666-157e-592c-95af-cef00f4d9474
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:18:00Z | thread: ZOM-586
issue_id: ZOM-586
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-26T16:18:00Z
updated_at: 2025-09-26T16:18:00Z
sequence: 1

### linear container ZOM-587

#### 10b6ac18-a627-5255-af32-8410e8ccfcf1
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:24:31Z | thread: ZOM-587
issue_id: ZOM-587
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:24:31Z
updated_at: 2025-09-25T07:24:31Z
sequence: 1

### linear container ZOM-588

#### f38cbc5b-4f7a-5ffd-b5c6-6f59ad44a44c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:24:42Z | thread: ZOM-588
issue_id: ZOM-588
author_id: usr_fc22d5941b2aeb5c
body: Went in the second zip on 24 Sep (the one they called the duck).
created_at: 2025-09-25T07:24:42Z
updated_at: 2025-09-25T07:24:42Z
sequence: 1

### linear container ZOM-589

#### e6b919e4-2499-5439-9234-0578fc2f80c6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:44:57Z | thread: ZOM-589
issue_id: ZOM-589
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:44:57Z
updated_at: 2025-09-26T09:44:57Z
sequence: 1

### linear container ZOM-590

#### 202ce85a-7926-5920-aa57-6cb399779639
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:05:54Z | thread: ZOM-590
issue_id: ZOM-590
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:05:54Z
updated_at: 2025-09-25T08:05:54Z
sequence: 1

### linear container ZOM-591

#### 414102ff-3e97-5412-821b-3a8497cb9f84
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:16:44Z | thread: ZOM-591
issue_id: ZOM-591
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:16:44Z
updated_at: 2025-09-25T08:16:44Z
sequence: 1

### linear container ZOM-592

#### 2df6bd67-01d4-56eb-afab-5513c5062d02
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:18:12Z | thread: ZOM-592
issue_id: ZOM-592
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:18:12Z
updated_at: 2025-09-25T08:18:12Z
sequence: 1

### linear container ZOM-593

#### f8aed615-9f9d-5735-9fcf-75df00ef0ca6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:46:23Z | thread: ZOM-593
issue_id: ZOM-593
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:46:23Z
updated_at: 2025-09-26T09:46:23Z
sequence: 1

### linear container ZOM-594

#### 410f3628-b379-5ba1-8cf6-10f6ae7881e4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:48:14Z | thread: ZOM-594
issue_id: ZOM-594
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:48:14Z
updated_at: 2025-09-26T09:48:14Z
sequence: 1

### linear container ZOM-595

#### a1ba138e-5b26-56c8-a400-c536e1c14e65
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:50:10Z | thread: ZOM-595
issue_id: ZOM-595
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:50:10Z
updated_at: 2025-09-26T09:50:10Z
sequence: 1

### linear container ZOM-596

#### 501ec8ca-11d1-58e1-ace2-389a18e8e21a
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:07:59Z | thread: ZOM-596
issue_id: ZOM-596
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:07:59Z
updated_at: 2025-09-29T11:07:59Z
sequence: 1

### linear container ZOM-597

#### 8c7e0da3-45ca-52ce-a259-48b8deb6adcb
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:10:10Z | thread: ZOM-597
issue_id: ZOM-597
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:10:10Z
updated_at: 2025-09-29T11:10:10Z
sequence: 1

### linear container ZOM-598

#### 927ea351-543a-58fb-8a7b-d99499d67a77
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:11:57Z | thread: ZOM-598
issue_id: ZOM-598
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:11:57Z
updated_at: 2025-09-29T11:11:57Z
sequence: 1

### linear container ZOM-599

#### b4f681db-9252-5da0-a93c-39a2d3bf58e8
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:13:23Z | thread: ZOM-599
issue_id: ZOM-599
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:13:23Z
updated_at: 2025-09-29T11:13:23Z
sequence: 1

### linear container ZOM-600

#### 6c4e3790-82ba-5ed4-99d8-5fc7dbdadba6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:19:28Z | thread: ZOM-600
issue_id: ZOM-600
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-26T16:19:28Z
updated_at: 2025-09-26T16:19:28Z
sequence: 1

### linear container ZOM-601

#### 6bbf45d2-2be3-5f72-b56a-7fdec5b13eec
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:21:37Z | thread: ZOM-601
issue_id: ZOM-601
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-26T16:21:37Z
updated_at: 2025-09-26T16:21:37Z
sequence: 1

### linear container ZOM-602

#### f042b03a-1af6-50d5-8ff3-545287bde448
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:08:21Z | thread: ZOM-602
issue_id: ZOM-602
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:08:21Z
updated_at: 2025-09-26T11:08:21Z
sequence: 1

### linear container ZOM-603

#### 8e881f9f-5d4d-554f-981c-5ac6f0f13e6c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:09:37Z | thread: ZOM-603
issue_id: ZOM-603
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:09:37Z
updated_at: 2025-09-26T11:09:37Z
sequence: 1

### linear container ZOM-604

#### 90e4ddbf-4fc8-5734-9240-bef69c616b89
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:10:38Z | thread: ZOM-604
issue_id: ZOM-604
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:10:38Z
updated_at: 2025-09-26T11:10:38Z
sequence: 1

### linear container ZOM-605

#### 06c58af5-a743-5601-b211-f2daad64e863
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:11:59Z | thread: ZOM-605
issue_id: ZOM-605
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:11:59Z
updated_at: 2025-09-26T11:11:59Z
sequence: 1

### linear container ZOM-606

#### a02d9030-aebe-54e2-947f-280e45439268
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:13:18Z | thread: ZOM-606
issue_id: ZOM-606
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:13:18Z
updated_at: 2025-09-26T11:13:18Z
sequence: 1

### linear container ZOM-607

#### 0cf2f7f2-53c5-5f19-a5a3-31e90081acfc
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:14:21Z | thread: ZOM-607
issue_id: ZOM-607
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:14:21Z
updated_at: 2025-09-26T11:14:21Z
sequence: 1

### linear container ZOM-608

#### 9d0c26f1-427c-5bec-92fb-f213a3263686
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:16:07Z | thread: ZOM-608
issue_id: ZOM-608
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:16:07Z
updated_at: 2025-09-26T11:16:07Z
sequence: 1

### linear container ZOM-609

#### ef72a5ac-66a9-50f2-ac7f-cee26aab5b04
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:16:55Z | thread: ZOM-609
issue_id: ZOM-609
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:16:55Z
updated_at: 2025-09-26T11:16:55Z
sequence: 1

### linear container ZOM-610

#### 7af82875-da67-5990-afed-d6750b208c1e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:18:24Z | thread: ZOM-610
issue_id: ZOM-610
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:18:24Z
updated_at: 2025-09-26T11:18:24Z
sequence: 1

### linear container ZOM-611

#### 568299c3-fb14-5752-a166-f4b5c8189205
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:19:28Z | thread: ZOM-611
issue_id: ZOM-611
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:19:28Z
updated_at: 2025-09-26T11:19:28Z
sequence: 1

### linear container ZOM-612

#### 14a4804f-c2e9-50c1-8950-b9f79dd65258
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:20:42Z | thread: ZOM-612
issue_id: ZOM-612
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:20:42Z
updated_at: 2025-09-26T11:20:42Z
sequence: 1

### linear container ZOM-613

#### c61b88c5-8649-5dd0-aabb-d94dee62c8ab
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:22:18Z | thread: ZOM-613
issue_id: ZOM-613
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:22:18Z
updated_at: 2025-09-26T11:22:18Z
sequence: 1

### linear container ZOM-614

#### 8b874340-d0a3-5476-9736-90e21eb71421
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:22:47Z | thread: ZOM-614
issue_id: ZOM-614
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-26T16:22:47Z
updated_at: 2025-09-26T16:22:47Z
sequence: 1

### linear container ZOM-615

#### 16b99933-0d85-5efa-bb8b-db8393d6292e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:26:21Z | thread: ZOM-615
issue_id: ZOM-615
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:26:21Z
updated_at: 2025-09-25T15:26:21Z
sequence: 1

### linear container ZOM-616

#### 26028dad-f409-52fb-b4d2-bf3b697a8f43
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:27:40Z | thread: ZOM-616
issue_id: ZOM-616
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:27:40Z
updated_at: 2025-09-25T15:27:40Z
sequence: 1

### linear container ZOM-617

#### e080bee1-a56c-53f8-a675-ffb2ddfe6b0f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:29:42Z | thread: ZOM-617
issue_id: ZOM-617
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:29:42Z
updated_at: 2025-09-25T15:29:42Z
sequence: 1

### linear container ZOM-618

#### abce170c-0c57-500e-9755-dc6b5658f0ae
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:31:34Z | thread: ZOM-618
issue_id: ZOM-618
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:31:34Z
updated_at: 2025-09-25T15:31:34Z
sequence: 1

### linear container ZOM-619

#### 8f260004-7f8e-5a4f-ae73-250994f1fbd5
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:33:12Z | thread: ZOM-619
issue_id: ZOM-619
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:33:12Z
updated_at: 2025-09-25T15:33:12Z
sequence: 1

### linear container ZOM-620

#### f04cefe7-88a6-5571-a251-904748384834
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:34:55Z | thread: ZOM-620
issue_id: ZOM-620
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:34:55Z
updated_at: 2025-09-25T15:34:55Z
sequence: 1

### linear container ZOM-621

#### 5980046f-e4a3-56f0-8f18-f6554227011d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:36:24Z | thread: ZOM-621
issue_id: ZOM-621
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:36:24Z
updated_at: 2025-09-25T15:36:24Z
sequence: 1

### linear container ZOM-622

#### b8d22538-8e43-5240-8a74-40399ea9372d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:38:15Z | thread: ZOM-622
issue_id: ZOM-622
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:38:15Z
updated_at: 2025-09-25T15:38:15Z
sequence: 1

### linear container ZOM-623

#### c549a962-07e3-5707-948b-fafab28ea49d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:39:49Z | thread: ZOM-623
issue_id: ZOM-623
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:39:49Z
updated_at: 2025-09-25T15:39:49Z
sequence: 1

### linear container ZOM-624

#### 2d66b43b-70df-599c-89e0-09043ecb3bb3
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:51:52Z | thread: ZOM-624
issue_id: ZOM-624
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:51:52Z
updated_at: 2025-09-26T09:51:52Z
sequence: 1

### linear container ZOM-625

#### 6bae80f0-7156-5308-91d1-bc649360aeaf
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:53:56Z | thread: ZOM-625
issue_id: ZOM-625
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:53:56Z
updated_at: 2025-09-26T09:53:56Z
sequence: 1

### linear container ZOM-626

#### dd6b09c1-124e-5cdc-aa50-9e3bcab984d7
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:55:29Z | thread: ZOM-626
issue_id: ZOM-626
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:55:29Z
updated_at: 2025-09-26T09:55:29Z
sequence: 1

### linear container ZOM-627

#### d58e2ef2-eedf-51fa-8610-a5d00922dfe1
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:15:28Z | thread: ZOM-627
issue_id: ZOM-627
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:15:28Z
updated_at: 2025-09-29T11:15:28Z
sequence: 1

### linear container ZOM-628

#### 5e211a7f-ccb8-5bbe-81aa-dfb6a3251fc2
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:17:34Z | thread: ZOM-628
issue_id: ZOM-628
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:17:34Z
updated_at: 2025-09-29T11:17:34Z
sequence: 1

### linear container ZOM-629

#### f8b3d54a-3b29-5273-9ecf-38e1feebe9e5
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:19:24Z | thread: ZOM-629
issue_id: ZOM-629
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:19:24Z
updated_at: 2025-09-29T11:19:24Z
sequence: 1

### linear container ZOM-630

#### 600e8939-4e8b-5660-9638-c4328b605ff4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:20:47Z | thread: ZOM-630
issue_id: ZOM-630
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:20:47Z
updated_at: 2025-09-29T11:20:47Z
sequence: 1

### linear container ZOM-631

#### f638e4f9-db25-5147-a967-772c4263d4b6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:25:07Z | thread: ZOM-631
issue_id: ZOM-631
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-26T16:25:07Z
updated_at: 2025-09-26T16:25:07Z
sequence: 1

### linear container ZOM-632

#### 1fdef95d-609d-5eba-afb3-1bdc07494156
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:26:17Z | thread: ZOM-632
issue_id: ZOM-632
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-26T16:26:17Z
updated_at: 2025-09-26T16:26:17Z
sequence: 1

### linear container ZOM-633

#### 0d2b852c-979f-5ed8-a046-899a3e81e476
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:04:08Z | thread: ZOM-633
issue_id: ZOM-633
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:04:08Z
updated_at: 2025-09-26T13:04:08Z
sequence: 1

### linear container ZOM-634

#### fc981716-2526-53b9-ad72-1e753cf07fa6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:06:04Z | thread: ZOM-634
issue_id: ZOM-634
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:06:04Z
updated_at: 2025-09-26T13:06:04Z
sequence: 1

### linear container ZOM-635

#### 2e1503f8-fe6d-5d46-9be3-4f2e70d58bf8
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:07:26Z | thread: ZOM-635
issue_id: ZOM-635
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:07:26Z
updated_at: 2025-09-26T13:07:26Z
sequence: 1

### linear container ZOM-636

#### cbb94883-96c9-5d48-a262-4b3f61968c86
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:08:20Z | thread: ZOM-636
issue_id: ZOM-636
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:08:20Z
updated_at: 2025-09-26T13:08:20Z
sequence: 1

### linear container ZOM-637

#### 17174e8a-464a-5509-a94d-1aae20ffe4b5
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:09:43Z | thread: ZOM-637
issue_id: ZOM-637
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:09:43Z
updated_at: 2025-09-26T13:09:43Z
sequence: 1

### linear container ZOM-638

#### 74e79473-1e5a-55af-9962-cd4ed0303cdd
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:11:33Z | thread: ZOM-638
issue_id: ZOM-638
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:11:33Z
updated_at: 2025-09-26T13:11:33Z
sequence: 1

### linear container ZOM-639

#### 4554db44-2454-5e50-a63e-2e825f187546
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:13:02Z | thread: ZOM-639
issue_id: ZOM-639
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:13:02Z
updated_at: 2025-09-26T13:13:02Z
sequence: 1

### linear container ZOM-640

#### 11a633e9-dfe3-5d3e-93ca-b7831510b562
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:14:23Z | thread: ZOM-640
issue_id: ZOM-640
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:14:23Z
updated_at: 2025-09-26T13:14:23Z
sequence: 1

### linear container ZOM-641

#### fc775035-8381-5e0d-9591-626ed573c5b4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:22:31Z | thread: ZOM-641
issue_id: ZOM-641
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:22:31Z
updated_at: 2025-09-29T11:22:31Z
sequence: 1

### linear container ZOM-642

#### 6f786f20-f3fd-59e1-8d4c-4c7dda754a35
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:28:34Z | thread: ZOM-642
issue_id: ZOM-642
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-26T16:28:34Z
updated_at: 2025-09-26T16:28:34Z
sequence: 1

### linear container ZOM-643

#### 6fcca602-b45d-5d9e-a519-d6a67875a6e9
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:06:42Z | thread: ZOM-643
issue_id: ZOM-643
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:06:42Z
updated_at: 2025-09-25T08:06:42Z
sequence: 1

### linear container ZOM-644

#### c5008259-08bf-590d-bfaf-5afc88e9c965
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:57:17Z | thread: ZOM-644
issue_id: ZOM-644
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:57:17Z
updated_at: 2025-09-26T09:57:17Z
sequence: 1

### linear container ZOM-645

#### a1ee4ac0-3701-524c-aaa1-656761e111d3
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:59:00Z | thread: ZOM-645
issue_id: ZOM-645
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:59:00Z
updated_at: 2025-09-26T09:59:00Z
sequence: 1

### linear container ZOM-646

#### 420807e5-7eae-5adb-b8f0-99897c93e8fb
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T10:01:16Z | thread: ZOM-646
issue_id: ZOM-646
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T10:01:16Z
updated_at: 2025-09-26T10:01:16Z
sequence: 1

### linear container ZOM-647

#### ec5c139f-0fa3-5508-997b-325c926ed298
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:24:56Z | thread: ZOM-647
issue_id: ZOM-647
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:24:56Z
updated_at: 2025-09-29T11:24:56Z
sequence: 1

### linear container ZOM-648

#### 801740a2-691c-5f53-9bba-90c5a6c3405a
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:26:35Z | thread: ZOM-648
issue_id: ZOM-648
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:26:35Z
updated_at: 2025-09-29T11:26:35Z
sequence: 1

### linear container ZOM-649

#### 48c53d03-5e9c-50eb-ad08-85698a838e8c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:28:29Z | thread: ZOM-649
issue_id: ZOM-649
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:28:29Z
updated_at: 2025-09-29T11:28:29Z
sequence: 1

### linear container ZOM-650

#### 08f6b5e9-0d0c-585f-965c-cbe0856d60d1
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:29:59Z | thread: ZOM-650
issue_id: ZOM-650
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-26T16:29:59Z
updated_at: 2025-09-26T16:29:59Z
sequence: 1

### linear container ZOM-651

#### 9e9cd387-beb3-5370-a54f-564699b560d4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:31:46Z | thread: ZOM-651
issue_id: ZOM-651
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-26T16:31:46Z
updated_at: 2025-09-26T16:31:46Z
sequence: 1

### linear container ZOM-652

#### b9331366-208f-54f7-b66f-29595e56b81f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:25:15Z | thread: ZOM-652
issue_id: ZOM-652
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:25:15Z
updated_at: 2025-09-25T07:25:15Z
sequence: 1

### linear container ZOM-653

#### e0bf84cd-6269-541d-9a1d-95cde07ef6d2
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:25:15Z | thread: ZOM-653
issue_id: ZOM-653
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:25:15Z
updated_at: 2025-09-25T07:25:15Z
sequence: 1

### linear container ZOM-654

#### 8e46f0c1-1d5f-5a81-94d9-bf044167be06
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T10:21:17Z | thread: ZOM-654
issue_id: ZOM-654
author_id: usr_fc22d5941b2aeb5c
body: Unity pack from Marcus, sent Fri 26 Sep. They went through it and came back with a question for Robert, not about the files.
created_at: 2025-09-29T10:21:17Z
updated_at: 2025-09-29T10:21:17Z
sequence: 1

### linear container ZOM-655

#### 507e797c-becd-5c82-af5e-a0d2afc68b47
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:11:37Z | thread: ZOM-655
issue_id: ZOM-655
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:11:37Z
updated_at: 2025-09-26T14:11:37Z
sequence: 1

### linear container ZOM-656

#### df8f83f4-dc50-5c79-8fff-cdb205166aa9
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:12:21Z | thread: ZOM-656
issue_id: ZOM-656
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:12:21Z
updated_at: 2025-09-26T14:12:21Z
sequence: 1

### linear container ZOM-657

#### 4f248b0b-3991-59aa-b439-0e4d8742c70d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:13:59Z | thread: ZOM-657
issue_id: ZOM-657
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:13:59Z
updated_at: 2025-09-26T14:13:59Z
sequence: 1

### linear container ZOM-658

#### 4386339b-9cda-5d85-9470-7895c1c10a1c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:15:03Z | thread: ZOM-658
issue_id: ZOM-658
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:15:03Z
updated_at: 2025-09-26T14:15:03Z
sequence: 1

### linear container ZOM-659

#### 1af79ca9-52b2-50cc-9c85-f699e4ee3e54
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:16:15Z | thread: ZOM-659
issue_id: ZOM-659
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:16:15Z
updated_at: 2025-09-26T14:16:15Z
sequence: 1

### linear container ZOM-660

#### 9ff62cdd-c2fe-500b-8832-539a7e4e04a7
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:33:36Z | thread: ZOM-660
issue_id: ZOM-660
author_id: usr_fc22d5941b2aeb5c
body: Not exported. Frederick still has to say whether the ad uses our soundtrack or theirs.
created_at: 2025-09-26T16:33:36Z
updated_at: 2025-09-26T16:33:36Z
sequence: 1

### linear container ZOM-661

#### c02ca57d-f926-54d1-ba56-b4154f35728a
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:35:29Z | thread: ZOM-661
issue_id: ZOM-661
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. The item icons are in Figma, mine to pull as PNG.
created_at: 2025-09-26T16:35:29Z
updated_at: 2025-09-26T16:35:29Z
sequence: 1

### linear container ZOM-662

#### e3e92efb-563b-5f29-8bbf-b14b95ce291c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:37:13Z | thread: ZOM-662
issue_id: ZOM-662
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. In Figma, mine to pull as PNG.
created_at: 2025-09-26T16:37:13Z
updated_at: 2025-09-26T16:37:13Z
sequence: 1

### linear container ZOM-663

#### 31b53426-4274-593c-b1cf-ef944ed22968
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T16:38:40Z | thread: ZOM-663
issue_id: ZOM-663
author_id: usr_fc22d5941b2aeb5c
body: Not sent. Need the .ttf files from Martin.
created_at: 2025-09-26T16:38:40Z
updated_at: 2025-09-26T16:38:40Z
sequence: 1

### linear container team_ZOM

#### ZOM-567
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:05:12Z
team_id: team_ZOM
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 567
title: Playable pack for PlayableX
description: Frederick wants every line of the playable pack tracked after the start slipped. One sub-ticket per line of the pack list. I leave a note on each one saying what I did with it. A line's ticket closes when PlayableX have the file.
priority: 2
started_at: 2025-09-25T07:21:48Z
created_at: 2025-09-25T07:05:12Z
updated_at: 2025-09-25T07:21:48Z

#### ZOM-568
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:05Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 568
title: Couch
priority: 2
started_at: 2025-09-25T07:21:52Z
completed_at: 2025-09-25T07:24:16Z
created_at: 2025-09-25T07:06:05Z
updated_at: 2025-09-25T07:24:16Z

#### ZOM-569
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:15Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 569
title: Couch and Pillow
priority: 2
started_at: 2025-09-25T07:21:52Z
completed_at: 2025-09-25T07:24:43Z
created_at: 2025-09-25T07:06:15Z
updated_at: 2025-09-25T07:24:43Z

#### ZOM-570
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:23Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 570
title: Alarm Clock
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:23Z
updated_at: 2025-09-25T15:21:19Z

#### ZOM-571
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:31Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 571
title: Record Player
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:31Z
updated_at: 2025-09-25T15:22:57Z

#### ZOM-572
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:37Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 572
title: Retro TV
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:37Z
updated_at: 2025-09-25T15:24:29Z

#### ZOM-573
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:43Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 573
title: Desk Lamp
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:43Z
updated_at: 2025-09-26T09:37:26Z

#### ZOM-574
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:52Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 574
title: Small Lamp
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:52Z
updated_at: 2025-09-26T09:39:29Z

#### ZOM-575
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:01Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 575
title: Fly Zapper
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:01Z
updated_at: 2025-09-26T16:14:37Z

#### ZOM-576
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:10Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 576
title: Grenade
priority: 2
started_at: 2025-09-25T07:21:52Z
completed_at: 2025-09-25T07:24:50Z
created_at: 2025-09-25T07:07:10Z
updated_at: 2025-09-25T07:24:50Z

#### ZOM-577
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:19Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 577
title: Chainsaw
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:19Z
updated_at: 2025-09-25T08:05:17Z

#### ZOM-578
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:26Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 578
title: Cute Axe
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:26Z
updated_at: 2025-09-25T08:09:04Z

#### ZOM-579
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:34Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 579
title: Cute Hammer
priority: 2
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:34Z
updated_at: 2025-09-25T08:11:13Z

#### ZOM-580
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:39Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 580
title: Dynamite
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:07:39Z
updated_at: 2025-09-25T08:13:02Z

#### ZOM-581
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:51Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 581
title: Shuriken
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:07:51Z
updated_at: 2025-09-25T08:14:52Z

#### ZOM-582
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:56Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 582
title: Saber
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:07:56Z
updated_at: 2025-09-26T09:40:54Z

#### ZOM-583
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:07Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 583
title: Safe
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:07Z
updated_at: 2025-09-26T09:42:45Z

#### ZOM-584
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:14Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 584
title: Flashlight
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:14Z
updated_at: 2025-09-29T11:06:27Z

#### ZOM-585
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:23Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 585
title: Fire Extinguisher
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:23Z
updated_at: 2025-09-26T16:16:18Z

#### ZOM-586
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:31Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 586
title: Propane Tank
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:31Z
updated_at: 2025-09-26T16:18:00Z

#### ZOM-587
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:36Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 587
title: Plushie Bunny
priority: 2
started_at: 2025-09-25T07:21:55Z
completed_at: 2025-09-25T07:25:31Z
created_at: 2025-09-25T07:08:36Z
updated_at: 2025-09-25T07:25:31Z

#### ZOM-588
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:46Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 588
title: Plushie Chick
priority: 2
started_at: 2025-09-25T07:21:55Z
completed_at: 2025-09-25T07:25:41Z
created_at: 2025-09-25T07:08:46Z
updated_at: 2025-09-25T07:25:41Z

#### ZOM-589
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:54Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 589
title: Bow
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:54Z
updated_at: 2025-09-26T09:44:57Z

#### ZOM-590
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:01Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 590
title: Cone
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:09:01Z
updated_at: 2025-09-25T08:05:54Z

#### ZOM-591
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:07Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 591
title: Dice
priority: 2
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:09:07Z
updated_at: 2025-09-25T08:16:44Z

#### ZOM-592
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:17Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 592
title: Gift Box
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:17Z
updated_at: 2025-09-25T08:18:12Z

#### ZOM-593
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:27Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 593
title: Plushie Dog
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:27Z
updated_at: 2025-09-26T09:46:23Z

#### ZOM-594
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:33Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 594
title: Plushie Whale
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:33Z
updated_at: 2025-09-26T09:48:14Z

#### ZOM-595
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:41Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 595
title: Whistle
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:41Z
updated_at: 2025-09-26T09:50:10Z

#### ZOM-596
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:51Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 596
title: Wooden Tower
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:51Z
updated_at: 2025-09-29T11:07:59Z

#### ZOM-597
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:58Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 597
title: Toy Car
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:58Z
updated_at: 2025-09-29T11:10:10Z

#### ZOM-598
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:07Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 598
title: Toy Boat
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:07Z
updated_at: 2025-09-29T11:11:57Z

#### ZOM-599
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:13Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 599
title: Toy Airplane
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:13Z
updated_at: 2025-09-29T11:13:23Z

#### ZOM-600
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:23Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 600
title: Toy Train
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:23Z
updated_at: 2025-09-26T16:19:28Z

#### ZOM-601
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:28Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 601
title: Beach Ball
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:28Z
updated_at: 2025-09-26T16:21:37Z

#### ZOM-602
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:38Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 602
title: Bathroom Scale
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:38Z
updated_at: 2025-09-26T11:08:21Z

#### ZOM-603
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:47Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 603
title: Bathtub
priority: 2
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:47Z
updated_at: 2025-09-26T11:09:37Z

#### ZOM-604
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:55Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 604
title: Cabinet Sink
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:10:55Z
updated_at: 2025-09-26T11:10:38Z

#### ZOM-605
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:02Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 605
title: Flip Flops
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:02Z
updated_at: 2025-09-26T11:11:59Z

#### ZOM-606
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:11Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 606
title: Iron
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:11Z
updated_at: 2025-09-26T11:13:18Z

#### ZOM-607
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:16Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 607
title: Ironing Board
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:16Z
updated_at: 2025-09-26T11:14:21Z

#### ZOM-608
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:23Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 608
title: Plunger
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:23Z
updated_at: 2025-09-26T11:16:07Z

#### ZOM-609
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:31Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 609
title: Slippers
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:31Z
updated_at: 2025-09-26T11:16:55Z

#### ZOM-610
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:41Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 610
title: Toilet
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:41Z
updated_at: 2025-09-26T11:18:24Z

#### ZOM-611
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:51Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 611
title: Toilet Paper
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:51Z
updated_at: 2025-09-26T11:19:28Z

#### ZOM-612
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:58Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 612
title: Wash Basin
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:58Z
updated_at: 2025-09-26T11:20:42Z

#### ZOM-613
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:05Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 613
title: Washing Machine
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:12:05Z
updated_at: 2025-09-26T11:22:18Z

#### ZOM-614
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:11Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 614
title: Rubber Ducky
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:12:11Z
updated_at: 2025-09-26T16:22:47Z

#### ZOM-615
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:22Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 615
title: Coffee Machine
priority: 2
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:12:22Z
updated_at: 2025-09-25T15:26:21Z

#### ZOM-616
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:30Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 616
title: Cooler
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:30Z
updated_at: 2025-09-25T15:27:40Z

#### ZOM-617
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:37Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 617
title: Ice Cream Machine
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:37Z
updated_at: 2025-09-25T15:29:42Z

#### ZOM-618
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:46Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 618
title: Kitchen Mixer
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:46Z
updated_at: 2025-09-25T15:31:34Z

#### ZOM-619
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:55Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 619
title: Microwave
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:55Z
updated_at: 2025-09-25T15:33:12Z

#### ZOM-620
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:03Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 620
title: Oven
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:03Z
updated_at: 2025-09-25T15:34:55Z

#### ZOM-621
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:11Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 621
title: Refrigerator
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:11Z
updated_at: 2025-09-25T15:36:24Z

#### ZOM-622
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:17Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 622
title: Stove
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:17Z
updated_at: 2025-09-25T15:38:15Z

#### ZOM-623
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:24Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 623
title: Toaster
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:24Z
updated_at: 2025-09-25T15:39:49Z

#### ZOM-624
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:32Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 624
title: Dutch Oven
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:32Z
updated_at: 2025-09-26T09:51:52Z

#### ZOM-625
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:43Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 625
title: Rolling Pin
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:43Z
updated_at: 2025-09-26T09:53:56Z

#### ZOM-626
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:47Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 626
title: Round Kettle
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:47Z
updated_at: 2025-09-26T09:55:29Z

#### ZOM-627
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:57Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 627
title: Round Pan
priority: 2
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:57Z
updated_at: 2025-09-29T11:15:28Z

#### ZOM-628
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:04Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 628
title: Spatula
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:04Z
updated_at: 2025-09-29T11:17:34Z

#### ZOM-629
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:14Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 629
title: Whisk
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:14Z
updated_at: 2025-09-29T11:19:24Z

#### ZOM-630
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:21Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 630
title: Ladle
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:21Z
updated_at: 2025-09-29T11:20:47Z

#### ZOM-631
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:29Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 631
title: Small Kettle
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:29Z
updated_at: 2025-09-26T16:25:07Z

#### ZOM-632
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:39Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 632
title: Tall Kettle
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:39Z
updated_at: 2025-09-26T16:26:17Z

#### ZOM-633
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:47Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 633
title: Acoustic Guitar
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:47Z
updated_at: 2025-09-26T13:04:08Z

#### ZOM-634
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:53Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 634
title: Cello
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:53Z
updated_at: 2025-09-26T13:06:04Z

#### ZOM-635
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:00Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 635
title: Cymbals
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:00Z
updated_at: 2025-09-26T13:07:26Z

#### ZOM-636
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:11Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 636
title: Electric Guitar
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:11Z
updated_at: 2025-09-26T13:08:20Z

#### ZOM-637
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:17Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 637
title: Harp
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:17Z
updated_at: 2025-09-26T13:09:43Z

#### ZOM-638
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:24Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 638
title: Tambourine
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:24Z
updated_at: 2025-09-26T13:11:33Z

#### ZOM-639
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:33Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 639
title: Trumpet
priority: 2
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:33Z
updated_at: 2025-09-26T13:13:02Z

#### ZOM-640
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:41Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 640
title: Xylophone
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:15:41Z
updated_at: 2025-09-26T13:14:23Z

#### ZOM-641
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:48Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 641
title: Music Keyboard
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:15:48Z
updated_at: 2025-09-29T11:22:31Z

#### ZOM-642
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:56Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 642
title: Grand Piano
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:15:56Z
updated_at: 2025-09-26T16:28:34Z

#### ZOM-643
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:05Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 643
title: Cactus Plant
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:05Z
updated_at: 2025-09-25T08:06:42Z

#### ZOM-644
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:13Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 644
title: Barrel
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:13Z
updated_at: 2025-09-26T09:57:17Z

#### ZOM-645
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:21Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 645
title: Bench
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:21Z
updated_at: 2025-09-26T09:59:00Z

#### ZOM-646
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:29Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 646
title: Flower Pot
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:29Z
updated_at: 2025-09-26T10:01:16Z

#### ZOM-647
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:38Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 647
title: Garden Shears
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:38Z
updated_at: 2025-09-29T11:24:56Z

#### ZOM-648
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:44Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 648
title: Watering Can
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:44Z
updated_at: 2025-09-29T11:26:35Z

#### ZOM-649
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:54Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 649
title: Wooden Bucket
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:54Z
updated_at: 2025-09-29T11:28:29Z

#### ZOM-650
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:02Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 650
title: Wheelbarrow
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:17:02Z
updated_at: 2025-09-26T16:29:59Z

#### ZOM-651
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:11Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 651
title: Wooden Crate
priority: 2
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:17:11Z
updated_at: 2025-09-26T16:31:46Z

#### ZOM-652
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:17Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 652
title: Cannon
priority: 2
started_at: 2025-09-25T07:22:13Z
completed_at: 2025-09-25T07:26:07Z
created_at: 2025-09-25T07:17:17Z
updated_at: 2025-09-25T07:26:07Z

#### ZOM-653
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:23Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 653
title: Background
priority: 2
started_at: 2025-09-25T07:22:13Z
completed_at: 2025-09-25T07:26:23Z
created_at: 2025-09-25T07:17:23Z
updated_at: 2025-09-25T07:26:23Z

#### ZOM-654
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:34Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 654
title: Zombie characters
priority: 2
started_at: 2025-09-25T07:22:13Z
completed_at: 2025-09-29T10:22:00Z
created_at: 2025-09-25T07:17:34Z
updated_at: 2025-09-29T10:22:00Z

#### ZOM-655
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:41Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 655
title: Matching sound
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:17:41Z
updated_at: 2025-09-26T14:11:37Z

#### ZOM-656
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:50Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 656
title: Rocket sound
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:17:50Z
updated_at: 2025-09-26T14:12:21Z

#### ZOM-657
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:59Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 657
title: Explosion sound
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:17:59Z
updated_at: 2025-09-26T14:13:59Z

#### ZOM-658
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:05Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 658
title: Success sound
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:05Z
updated_at: 2025-09-26T14:15:03Z

#### ZOM-659
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:15Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 659
title: Failure sound
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:15Z
updated_at: 2025-09-26T14:16:15Z

#### ZOM-660
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:23Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 660
title: Background music
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:23Z
updated_at: 2025-09-26T16:33:36Z

#### ZOM-661
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:29Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 661
title: Item visuals
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:29Z
updated_at: 2025-09-26T16:35:29Z

#### ZOM-662
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:36Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 662
title: UI elements
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:36Z
updated_at: 2025-09-26T16:37:13Z

#### ZOM-663
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:47Z
team_id: team_ZOM
parent_id: ZOM-567
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 663
title: Fonts
priority: 2
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:47Z
updated_at: 2025-09-26T16:38:40Z

## slack

### slack container C0880U9751A

#### C0880U9751A/1758906517.912099
table: slack.slack_messages | statement: insert | row id: a5ee6e90923eeab380e6730f674240d2 | author: EMPLOYEE_0002_SLACK_ID | date: 2025-09-26T17:08:37Z
ts: 1758906517.912099
channel_id: C0880U9751A
type: message
user_id: EMPLOYEE_0002_SLACK_ID
text: <@EMPLOYEE_0026_SLACK_ID> fyi the models you saved out of unity on thursday are the text kind, thats what the exporter does if you dont change it. they open fine in unity and in max so you wouldnt notice. the ones from <@EMPLOYEE_0009_SLACK_ID> are ok
reply_count: 0
reply_users_count: 0
created_at: 2025-09-26T17:08:37.912099Z

### slack container C08R8CHB0QL

#### C08R8CHB0QL/1758904025.123869
table: slack.slack_messages | statement: update (changes a record that is in the base) | row id: 088b096edb82a130771a5da3344bcef1
thread_ts_legacy: 1758904025.123869
reply_count: 2
reply_users_count: 2
latest_reply: 1758922879.243189

#### C08R8CHB0QL/1758922879.243189
table: slack.slack_messages | statement: insert | row id: 1d55b38831d7517fe403e4f2a906a897 | author: EMPLOYEE_0016_SLACK_ID | date: 2025-09-26T21:41:19Z | thread: C08R8CHB0QL/1758904025.123869
ts: 1758922879.243189
channel_id: C08R8CHB0QL
type: message
user_id: EMPLOYEE_0016_SLACK_ID
text: Fun one. Let's have it in the 8 in place of the last one on my list, we've got enough things that go boom. As it is now, the arrow can be its own item later.
thread_parent_id: 088b096edb82a130771a5da3344bcef1
thread_ts_legacy: 1758904025.123869
reply_count: 0
reply_users_count: 0
created_at: 2025-09-26T21:41:19.243189Z

### slack container C090N54TG79

#### C090N54TG79/1758823946.262829
table: slack.slack_messages | statement: insert | row id: da6776f77288224ec67847a799bbde5a | author: EMPLOYEE_0016_SLACK_ID | date: 2025-09-25T18:12:26Z
ts: 1758823946.262829
channel_id: C090N54TG79
type: message
user_id: EMPLOYEE_0016_SLACK_ID
text: For the playable board, the 8: Grenade, Couch and Plushie Chick from the reference level, plus Shuriken, Cute Axe, Gift Box, Cactus Plant and Dynamite. Everything else <@EMPLOYEE_0026_SLACK_ID> sends them is extras they can swap in.
reply_count: 0
reply_users_count: 0
created_at: 2025-09-25T18:12:26.262829Z

#### C090N54TG79/1759167068.371289
table: slack.slack_messages | statement: insert | row id: 0b7f656a96c5cc50d1f6924e089bf8ba | author: EMPLOYEE_0016_SLACK_ID | date: 2025-09-29T17:31:08Z
ts: 1759167068.371289
channel_id: C090N54TG79
type: message
user_id: EMPLOYEE_0016_SLACK_ID
text: <@EMPLOYEE_0026_SLACK_ID> for PlayableX's question, in case we carry on with them: one animation, walk. The 4 zombies: Party Girl, Plumber, Magician, Football Player.
reply_count: 0
reply_users_count: 0
created_at: 2025-09-29T17:31:08.371289Z

### slack container D05HMBQUC8Z

#### D05HMBQUC8Z/1759148152.833779
table: slack.slack_messages | statement: insert | row id: 6642a2d59e2a85bf5b2c15c41ba73761 | author: EMPLOYEE_0009_SLACK_ID | date: 2025-09-29T12:15:52Z
ts: 1759148152.833779
channel_id: D05HMBQUC8Z
type: message
user_id: EMPLOYEE_0009_SLACK_ID
text: kuzum bu arada banyo objelerinin uv'lerini baştan açıyorum, levellerde bi süre eski halleri görünür haberin olsun. cuma verdiğim banyo dosyaları da eski hali, bitince ticketlara yazarım
reply_count: 0
reply_users_count: 0
created_at: 2025-09-29T12:15:52.833779Z

### slack container D05SD5QLG94

#### D05SD5QLG94/1759256494.852159
table: slack.slack_messages | statement: insert | row id: 7e84f1cf59f8e95fef961268fbf37cc1 | author: EMPLOYEE_0008_SLACK_ID | date: 2025-09-30T18:21:34Z
ts: 1759256494.852159
channel_id: D05SD5QLG94
type: message
user_id: EMPLOYEE_0008_SLACK_ID
text: Julia, PlayableX are holding Nov 3 for us and I don't want a third slip on our side. While it's parked, can you do for this one what you did for the Dominoes playable: write the brief they build from, and tell me where the item pack actually stands. Brian's pack list is where it starts. Robert's picks for the board and the zombies stand unless he's changed them since. My hand-off notes say what goes in the brief, what counts as ready and what to do with the tickets. Write it for the game as it is today; if the core changes we redo that part with them in November. Brief as a doc and the hand-off list as a sheet, both in your Drive. Then give me the three counts here, and post both links in the PlayableX channel so they know what's still coming from us.
reply_count: 0
reply_users_count: 0
created_at: 2025-09-30T18:21:34.852159Z

## trello

### trello container (container not named in the SQL)

#### 688c4d14c312a27fa2747e40
table: trello.trello_cards | statement: update (changes a record that is in the base) | date: 2025-09-30T20:05:47Z
badges_json: {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0, "checkItemsEarliestDue": null, "comments": 1, "description": false, "due": null, "dueComplete": false, "externalSource": null, "fogbugz": "", "lastUpdatedByAi": false, "location": false, "maliciousAttachments": 0, "start": null, "votes": 0}
dateLastActivity: 2025-09-30T20:05:47Z

### trello container 688c4d14c312a27fa2747e40

#### 68dc381b75aff34acf5a5424
table: trello.trello_actions | statement: insert | author: PERSON_6094_TRELLO_USER_ID | date: 2025-09-30T20:05:47Z | thread: 688c4d14c312a27fa2747e40
type: commentCard
date: 2025-09-30T20:05:47Z
idMemberCreator: PERSON_6094_TRELLO_USER_ID
idBoard: 640643a3fd8f3ca308d9318e
idCard: 688c4d14c312a27fa2747e40
data_json:
    Parked. PlayableX moved the start to Nov 3. Frederick is getting the brief and the item pack squared away in the meantime.
    card: name=Playable Kickoff, idShort=447
    list: name=To Do

### trello container trello_boards

#### 640643a3fd8f3ca308d9318e
table: trello.trello_boards | statement: update (changes a record that is in the base) | date: 2025-09-30T20:05:47Z
dateLastActivity: 2025-09-30T20:05:47Z
