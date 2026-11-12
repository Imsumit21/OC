# Coherence review brief (reviewer 1)

Bound to: 01_Universe_Inject.sql sha256 78465cd474f817d507e482d1af2bc2b7cc12ad15878d0c900ff5644f96a24898; 04_Prompt.txt sha256 33c721d609452a3672e18829856370ac2810ce87ffdcdde3e38f599a19a1d28e
Scope: full

## What you have

- The prompt below.
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

Return one JSON object in exactly this shape (empty lists are fine; keep the keys). It is saved as `Working_Files/local_reviews/coherence/findings_1.json` in the task folder:

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

## Prompt

```text
I need a hand with Frederick's playable message from yesterday. Can you do everything he's asking for in it, start to finish? The files he wants should end up in my Drive, and once they're ready the links go in the PlayableX channel like he says.
```

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
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
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
created: 2025-09-30T16:41:17Z
updated: 2025-09-30T16:41:17Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

### gcal container frederick.stone@harmonygames.co

#### evt_d622b6ab55401d23626674
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
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
created: 2025-09-30T16:41:17Z
updated: 2025-09-30T16:41:17Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

### gcal container julia.lawson@harmonygames.co

#### evt_421695d009e589ee85296c
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
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
created: 2025-09-30T16:41:17Z
updated: 2025-09-30T16:41:17Z
ical_uid: f8080166995ced4aa3e45f02c40b98b1@hg4

### gcal container robert@harmonygames.co

#### evt_1c99b11a66cfd562b13d9c
table: gcal.gcal_events | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: f8080166995ced4aa3e45f02c40b98b1@hg4
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
created: 2025-09-30T16:41:17Z
updated: 2025-09-30T16:41:17Z
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
    
    The brief. One doc PlayableX can build from: which scenario we picked and what it is for, the eight items on the board and that every other board item on the list is an extra they can swap in, the four zombies and the one animation, how a level is won and lost and how many slots the tray has, what they can use for sound and when the music may start, and the start date. How the level plays is on the design page; your deck of the reference level has what we built for them. What they told us about formats still holds, and so does their rule from last time about when the music may start.
    
    The hand-off list. One row per line of Brian's pack list, with these columns: Line, Category, Board set, State, What's owed, Who has it, Ticket. Line, Category and Ticket are as on his list. Board set is Default for the eight on the board and Extra for every other board item; leave it empty for anything that isn't a board item.
    
    State is one of three words, nothing else. Delivered: PlayableX has the current file and can use it. Ready: exported in a format they take and sitting in the outgoing folder, it opens, it is the current version and nobody is changing it. Owed: anything else. For an Owed line say what is owed, and who has it, meaning whoever has to do the next thing.
    
    Brian's note on each ticket says what he did with the line. Take it as it stands unless something later says otherwise, and go by how things stand today, not the day he wrote it: if someone who knows the file or the art has said something since, that counts. If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again, and it sits with whoever the file came from.
    
    Sound: we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we have our own version.
    
    Tickets live under Brian's pack ticket, one per line. An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. Leave the Delivered and Ready ones as they are.
    
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
    Mon 29 Sep: another batch from Claire. She still has a few to send and a few are still mine to do.
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

#### brian.foster@harmonygames.co/1844707828171705300
table: gmail.gmail_threads | statement: insert
user_email: brian.foster@harmonygames.co
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@

#### brian.foster@harmonygames.co/<calendar-c94e8bd4-a0ec-0177-cb05-b68828195e96@google.com>
table: gmail.gmail_messages | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: brian.foster@harmonygames.co/1844707828171705300
thread_id: brian.foster@harmonygames.co/1844707828171705300
user_email: brian.foster@harmonygames.co
label_ids_json: ["INBOX", "CATEGORY_PERSONAL"]
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@
date: 2025-09-30T16:41:17Z
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

#### julia.lawson@harmonygames.co/1844707828171527310
table: gmail.gmail_threads | statement: insert
user_email: julia.lawson@harmonygames.co
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@

#### julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>
table: gmail.gmail_messages | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: julia.lawson@harmonygames.co/1844707828171527310
thread_id: julia.lawson@harmonygames.co/1844707828171527310
user_email: julia.lawson@harmonygames.co
label_ids_json: ["INBOX", "CATEGORY_PERSONAL"]
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@
date: 2025-09-30T16:41:17Z
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

#### robert@harmonygames.co/1844707828171004856
table: gmail.gmail_threads | statement: insert
user_email: robert@harmonygames.co
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@

#### robert@harmonygames.co/<calendar-4263dbb8-cab6-41a8-95c1-dca6f6f7e53b@google.com>
table: gmail.gmail_messages | statement: insert | author: frederick.stone@harmonygames.co | date: 2025-09-30T16:41:17Z | thread: robert@harmonygames.co/1844707828171004856
thread_id: robert@harmonygames.co/1844707828171004856
user_email: robert@harmonygames.co
label_ids_json: ["INBOX", "CATEGORY_PERSONAL"]
snippet: ZM3D playable kickoff with PlayableX Monday Nov 3, 2025 ⋅ 9am – 9:30am Pacific Time - Los Angeles Organizer Frederick Stone frederick.stone@
date: 2025-09-30T16:41:17Z
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
    Couch | Board item | Living Room | zip 24 Sep | DES-314
    Couch and Pillow | Board item | Living Room | zip 24 Sep | DES-315
    Alarm Clock | Board item | Living Room |  | DES-316
    Record Player | Board item | Living Room |  | DES-317
    Retro TV | Board item | Living Room |  | DES-318
    Desk Lamp | Board item | Living Room |  | DES-319
    Small Lamp | Board item | Living Room |  | DES-320
    Fly Zapper | Board item | Living Room |  | DES-321
    Grenade | Board item | Survival | zip 24 Sep | DES-322
    Chainsaw | Board item | Survival |  | DES-323
    Cute Axe | Board item | Survival |  | DES-324
    Cute Hammer | Board item | Survival |  | DES-325
    Dynamite | Board item | Survival |  | DES-326
    Shuriken | Board item | Survival |  | DES-327
    Saber | Board item | Survival |  | DES-328
    Safe | Board item | Survival |  | DES-329
    Flashlight | Board item | Survival |  | DES-330
    Fire Extinguisher | Board item | Survival |  | DES-331
    Propane Tank | Board item | Survival |  | DES-332
    Plushie Bunny | Board item | Toys | zip 24 Sep | DES-333
    Plushie Chick | Board item | Toys | zip 24 Sep (second) | DES-334
    Bow | Board item | Toys |  | DES-335
    Cone | Board item | Toys |  | DES-336
    Dice | Board item | Toys |  | DES-337
    Gift Box | Board item | Toys |  | DES-338
    Plushie Dog | Board item | Toys |  | DES-339
    Plushie Whale | Board item | Toys |  | DES-340
    Whistle | Board item | Toys |  | DES-341
    Wooden Tower | Board item | Toys |  | DES-342
    Toy Car | Board item | Toys |  | DES-343
    Toy Boat | Board item | Toys |  | DES-344
    Toy Airplane | Board item | Toys |  | DES-345
    Toy Train | Board item | Toys |  | DES-346
    Beach Ball | Board item | Toys |  | DES-347
    Bathroom Scale | Board item | Bathroom |  | DES-348
    Bathtub | Board item | Bathroom |  | DES-349
    Cabinet Sink | Board item | Bathroom |  | DES-350
    Flip Flops | Board item | Bathroom |  | DES-351
    Iron | Board item | Bathroom |  | DES-352
    Ironing Board | Board item | Bathroom |  | DES-353
    Plunger | Board item | Bathroom |  | DES-354
    Slippers | Board item | Bathroom |  | DES-355
    Toilet | Board item | Bathroom |  | DES-356
    Toilet Paper | Board item | Bathroom |  | DES-357
    Wash Basin | Board item | Bathroom |  | DES-358
    Washing Machine | Board item | Bathroom |  | DES-359
    Rubber Ducky | Board item | Bathroom |  | DES-360
    Coffee Machine | Board item | Kitchen |  | DES-361
    Cooler | Board item | Kitchen |  | DES-362
    Ice Cream Machine | Board item | Kitchen |  | DES-363
    Kitchen Mixer | Board item | Kitchen |  | DES-364
    Microwave | Board item | Kitchen |  | DES-365
    Oven | Board item | Kitchen |  | DES-366
    Refrigerator | Board item | Kitchen |  | DES-367
    Stove | Board item | Kitchen |  | DES-368
    Toaster | Board item | Kitchen |  | DES-369
    Dutch Oven | Board item | Kitchen |  | DES-370
    Rolling Pin | Board item | Kitchen |  | DES-371
    Round Kettle | Board item | Kitchen |  | DES-372
    Round Pan | Board item | Kitchen |  | DES-373
    Spatula | Board item | Kitchen |  | DES-374
    Whisk | Board item | Kitchen |  | DES-375
    Ladle | Board item | Kitchen |  | DES-376
    Small Kettle | Board item | Kitchen |  | DES-377
    Tall Kettle | Board item | Kitchen |  | DES-378
    Acoustic Guitar | Board item | Music Instruments |  | DES-379
    Cello | Board item | Music Instruments |  | DES-380
    Cymbals | Board item | Music Instruments |  | DES-381
    Electric Guitar | Board item | Music Instruments |  | DES-382
    Harp | Board item | Music Instruments |  | DES-383
    Tambourine | Board item | Music Instruments |  | DES-384
    Trumpet | Board item | Music Instruments |  | DES-385
    Xylophone | Board item | Music Instruments |  | DES-386
    Music Keyboard | Board item | Music Instruments |  | DES-387
    Grand Piano | Board item | Music Instruments |  | DES-388
    Cactus Plant | Board item | Garden |  | DES-389
    Barrel | Board item | Garden |  | DES-390
    Bench | Board item | Garden |  | DES-391
    Flower Pot | Board item | Garden |  | DES-392
    Garden Shears | Board item | Garden |  | DES-393
    Watering Can | Board item | Garden |  | DES-394
    Wooden Bucket | Board item | Garden |  | DES-395
    Wheelbarrow | Board item | Garden |  | DES-396
    Wooden Crate | Board item | Garden |  | DES-397
    Cannon | Weapon |  | zip 24 Sep | DES-398
    Background | Background |  | zip 24 Sep | DES-399
    Zombie characters | Zombies |  | pack 26 Sep | DES-400
    Matching sound | Sound |  |  | DES-401
    Rocket sound | Sound |  |  | DES-402
    Explosion sound | Sound |  |  | DES-403
    Success sound | Sound |  |  | DES-404
    Failure sound | Sound |  |  | DES-405
    Background music | Sound |  |  | DES-406
    Item visuals | 2D |  |  | DES-407
    UI elements | 2D |  |  | DES-408
    Fonts | Font |  |  | DES-409

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
    Background music | new track for the ad, generated and edited here (not the in-game track) | yes | 
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

### linear container DES-314

#### a022e31f-afd4-5ab4-81a2-fd1d62c1c2cf
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:23:35Z | thread: DES-314
issue_id: DES-314
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:23:35Z
updated_at: 2025-09-25T07:23:35Z
sequence: 1

### linear container DES-315

#### c9e602eb-3bf5-533a-9571-506ee278e07b
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:24:29Z | thread: DES-315
issue_id: DES-315
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:24:29Z
updated_at: 2025-09-25T07:24:29Z
sequence: 1

### linear container DES-316

#### 513dd4bc-6bd5-5aaf-b4da-feb984524384
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:21:19Z | thread: DES-316
issue_id: DES-316
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:21:19Z
updated_at: 2025-09-25T15:21:19Z
sequence: 1

### linear container DES-317

#### 7daa1ebe-84c9-5aba-ba45-22f69fdfd01f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:22:57Z | thread: DES-317
issue_id: DES-317
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:22:57Z
updated_at: 2025-09-25T15:22:57Z
sequence: 1

### linear container DES-318

#### 395bc5d2-8e32-537e-9286-a216ddf6b5af
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:24:29Z | thread: DES-318
issue_id: DES-318
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:24:29Z
updated_at: 2025-09-25T15:24:29Z
sequence: 1

### linear container DES-319

#### 4cf25a71-ccf1-58cf-a70d-da1286b1320e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:37:26Z | thread: DES-319
issue_id: DES-319
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:37:26Z
updated_at: 2025-09-26T09:37:26Z
sequence: 1

### linear container DES-320

#### 558aa24b-3da7-5537-aaba-e8f68ffdabcf
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:39:29Z | thread: DES-320
issue_id: DES-320
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:39:29Z
updated_at: 2025-09-26T09:39:29Z
sequence: 1

### linear container DES-321

#### 33933dbf-208d-5fab-be50-5bc02a0cf709
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:31:37Z | thread: DES-321
issue_id: DES-321
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-29T12:31:37Z
updated_at: 2025-09-29T12:31:37Z
sequence: 1

### linear container DES-322

#### c2522fd7-9203-57c6-8bfc-85eee899b758
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:25:08Z | thread: DES-322
issue_id: DES-322
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:25:08Z
updated_at: 2025-09-25T07:25:08Z
sequence: 1

### linear container DES-323

#### deb96bcb-7d02-5c29-8c41-79fcbd7c1c61
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:05:17Z | thread: DES-323
issue_id: DES-323
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:05:17Z
updated_at: 2025-09-25T08:05:17Z
sequence: 1

### linear container DES-324

#### 9b58d4b0-45c2-572d-8ce5-d64f5e2834ea
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:09:04Z | thread: DES-324
issue_id: DES-324
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:09:04Z
updated_at: 2025-09-25T08:09:04Z
sequence: 1

### linear container DES-325

#### c015eaec-be3a-5c98-9ea0-aa07f9825bf9
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:11:13Z | thread: DES-325
issue_id: DES-325
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:11:13Z
updated_at: 2025-09-25T08:11:13Z
sequence: 1

### linear container DES-326

#### 158e9cc2-7625-5075-a6f9-ae787f05959f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:13:02Z | thread: DES-326
issue_id: DES-326
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:13:02Z
updated_at: 2025-09-25T08:13:02Z
sequence: 1

### linear container DES-327

#### 637efd91-10a6-5346-92d0-0816d54f4dec
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:14:52Z | thread: DES-327
issue_id: DES-327
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:14:52Z
updated_at: 2025-09-25T08:14:52Z
sequence: 1

### linear container DES-328

#### 2f4ca97c-f3d4-5bb6-ab48-3bddf1130fea
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:40:54Z | thread: DES-328
issue_id: DES-328
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:40:54Z
updated_at: 2025-09-26T09:40:54Z
sequence: 1

### linear container DES-329

#### 0a858079-e758-5bf9-a159-c65c627eb62e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:42:45Z | thread: DES-329
issue_id: DES-329
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:42:45Z
updated_at: 2025-09-26T09:42:45Z
sequence: 1

### linear container DES-330

#### b2447303-d424-5811-b7d4-72aed39b7a8b
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:06:27Z | thread: DES-330
issue_id: DES-330
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:06:27Z
updated_at: 2025-09-29T11:06:27Z
sequence: 1

### linear container DES-331

#### 80866ff3-da39-5209-aa58-5281e7bb5d2d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:33:18Z | thread: DES-331
issue_id: DES-331
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-29T12:33:18Z
updated_at: 2025-09-29T12:33:18Z
sequence: 1

### linear container DES-332

#### abd87666-157e-592c-95af-cef00f4d9474
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:35:00Z | thread: DES-332
issue_id: DES-332
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-29T12:35:00Z
updated_at: 2025-09-29T12:35:00Z
sequence: 1

### linear container DES-333

#### 10b6ac18-a627-5255-af32-8410e8ccfcf1
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:26:19Z | thread: DES-333
issue_id: DES-333
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep.
created_at: 2025-09-25T07:26:19Z
updated_at: 2025-09-25T07:26:19Z
sequence: 1

### linear container DES-334

#### f38cbc5b-4f7a-5ffd-b5c6-6f59ad44a44c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:27:06Z | thread: DES-334
issue_id: DES-334
author_id: usr_fc22d5941b2aeb5c
body: Went in the second zip on 24 Sep (the one they called the duck).
created_at: 2025-09-25T07:27:06Z
updated_at: 2025-09-25T07:27:06Z
sequence: 1

### linear container DES-335

#### e6b919e4-2499-5439-9234-0578fc2f80c6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:08:27Z | thread: DES-335
issue_id: DES-335
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:08:27Z
updated_at: 2025-09-29T11:08:27Z
sequence: 1

### linear container DES-336

#### 202ce85a-7926-5920-aa57-6cb399779639
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:05:54Z | thread: DES-336
issue_id: DES-336
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:05:54Z
updated_at: 2025-09-25T08:05:54Z
sequence: 1

### linear container DES-337

#### 414102ff-3e97-5412-821b-3a8497cb9f84
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:16:44Z | thread: DES-337
issue_id: DES-337
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:16:44Z
updated_at: 2025-09-25T08:16:44Z
sequence: 1

### linear container DES-338

#### 2df6bd67-01d4-56eb-afab-5513c5062d02
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:18:12Z | thread: DES-338
issue_id: DES-338
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:18:12Z
updated_at: 2025-09-25T08:18:12Z
sequence: 1

### linear container DES-339

#### f8aed615-9f9d-5735-9fcf-75df00ef0ca6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:44:33Z | thread: DES-339
issue_id: DES-339
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:44:33Z
updated_at: 2025-09-26T09:44:33Z
sequence: 1

### linear container DES-340

#### 410f3628-b379-5ba1-8cf6-10f6ae7881e4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:46:24Z | thread: DES-340
issue_id: DES-340
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:46:24Z
updated_at: 2025-09-26T09:46:24Z
sequence: 1

### linear container DES-341

#### a1ba138e-5b26-56c8-a400-c536e1c14e65
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:48:20Z | thread: DES-341
issue_id: DES-341
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:48:20Z
updated_at: 2025-09-26T09:48:20Z
sequence: 1

### linear container DES-342

#### 501ec8ca-11d1-58e1-ace2-389a18e8e21a
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:09:49Z | thread: DES-342
issue_id: DES-342
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:09:49Z
updated_at: 2025-09-29T11:09:49Z
sequence: 1

### linear container DES-343

#### 8c7e0da3-45ca-52ce-a259-48b8deb6adcb
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:12:00Z | thread: DES-343
issue_id: DES-343
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:12:00Z
updated_at: 2025-09-29T11:12:00Z
sequence: 1

### linear container DES-344

#### 927ea351-543a-58fb-8a7b-d99499d67a77
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:13:47Z | thread: DES-344
issue_id: DES-344
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:13:47Z
updated_at: 2025-09-29T11:13:47Z
sequence: 1

### linear container DES-345

#### b4f681db-9252-5da0-a93c-39a2d3bf58e8
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:15:13Z | thread: DES-345
issue_id: DES-345
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:15:13Z
updated_at: 2025-09-29T11:15:13Z
sequence: 1

### linear container DES-346

#### 6c4e3790-82ba-5ed4-99d8-5fc7dbdadba6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:36:28Z | thread: DES-346
issue_id: DES-346
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-29T12:36:28Z
updated_at: 2025-09-29T12:36:28Z
sequence: 1

### linear container DES-347

#### 6bbf45d2-2be3-5f72-b56a-7fdec5b13eec
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:38:37Z | thread: DES-347
issue_id: DES-347
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-29T12:38:37Z
updated_at: 2025-09-29T12:38:37Z
sequence: 1

### linear container DES-348

#### f042b03a-1af6-50d5-8ff3-545287bde448
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:08:21Z | thread: DES-348
issue_id: DES-348
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:08:21Z
updated_at: 2025-09-26T11:08:21Z
sequence: 1

### linear container DES-349

#### 8e881f9f-5d4d-554f-981c-5ac6f0f13e6c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:09:37Z | thread: DES-349
issue_id: DES-349
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:09:37Z
updated_at: 2025-09-26T11:09:37Z
sequence: 1

### linear container DES-350

#### 90e4ddbf-4fc8-5734-9240-bef69c616b89
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:10:38Z | thread: DES-350
issue_id: DES-350
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:10:38Z
updated_at: 2025-09-26T11:10:38Z
sequence: 1

### linear container DES-351

#### 06c58af5-a743-5601-b211-f2daad64e863
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:11:59Z | thread: DES-351
issue_id: DES-351
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:11:59Z
updated_at: 2025-09-26T11:11:59Z
sequence: 1

### linear container DES-352

#### a02d9030-aebe-54e2-947f-280e45439268
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:13:18Z | thread: DES-352
issue_id: DES-352
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:13:18Z
updated_at: 2025-09-26T11:13:18Z
sequence: 1

### linear container DES-353

#### 0cf2f7f2-53c5-5f19-a5a3-31e90081acfc
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:14:21Z | thread: DES-353
issue_id: DES-353
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:14:21Z
updated_at: 2025-09-26T11:14:21Z
sequence: 1

### linear container DES-354

#### 9d0c26f1-427c-5bec-92fb-f213a3263686
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:16:07Z | thread: DES-354
issue_id: DES-354
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:16:07Z
updated_at: 2025-09-26T11:16:07Z
sequence: 1

### linear container DES-355

#### ef72a5ac-66a9-50f2-ac7f-cee26aab5b04
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:16:55Z | thread: DES-355
issue_id: DES-355
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:16:55Z
updated_at: 2025-09-26T11:16:55Z
sequence: 1

### linear container DES-356

#### 7af82875-da67-5990-afed-d6750b208c1e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:18:24Z | thread: DES-356
issue_id: DES-356
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:18:24Z
updated_at: 2025-09-26T11:18:24Z
sequence: 1

### linear container DES-357

#### 568299c3-fb14-5752-a166-f4b5c8189205
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:19:28Z | thread: DES-357
issue_id: DES-357
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:19:28Z
updated_at: 2025-09-26T11:19:28Z
sequence: 1

### linear container DES-358

#### 14a4804f-c2e9-50c1-8950-b9f79dd65258
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:20:42Z | thread: DES-358
issue_id: DES-358
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:20:42Z
updated_at: 2025-09-26T11:20:42Z
sequence: 1

### linear container DES-359

#### c61b88c5-8649-5dd0-aabb-d94dee62c8ab
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T11:22:18Z | thread: DES-359
issue_id: DES-359
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T11:22:18Z
updated_at: 2025-09-26T11:22:18Z
sequence: 1

### linear container DES-360

#### 8b874340-d0a3-5476-9736-90e21eb71421
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:39:47Z | thread: DES-360
issue_id: DES-360
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-29T12:39:47Z
updated_at: 2025-09-29T12:39:47Z
sequence: 1

### linear container DES-361

#### 16b99933-0d85-5efa-bb8b-db8393d6292e
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:26:21Z | thread: DES-361
issue_id: DES-361
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:26:21Z
updated_at: 2025-09-25T15:26:21Z
sequence: 1

### linear container DES-362

#### 26028dad-f409-52fb-b4d2-bf3b697a8f43
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:27:40Z | thread: DES-362
issue_id: DES-362
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:27:40Z
updated_at: 2025-09-25T15:27:40Z
sequence: 1

### linear container DES-363

#### e080bee1-a56c-53f8-a675-ffb2ddfe6b0f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:29:42Z | thread: DES-363
issue_id: DES-363
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:29:42Z
updated_at: 2025-09-25T15:29:42Z
sequence: 1

### linear container DES-364

#### abce170c-0c57-500e-9755-dc6b5658f0ae
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:31:34Z | thread: DES-364
issue_id: DES-364
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:31:34Z
updated_at: 2025-09-25T15:31:34Z
sequence: 1

### linear container DES-365

#### 8f260004-7f8e-5a4f-ae73-250994f1fbd5
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:33:12Z | thread: DES-365
issue_id: DES-365
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:33:12Z
updated_at: 2025-09-25T15:33:12Z
sequence: 1

### linear container DES-366

#### f04cefe7-88a6-5571-a251-904748384834
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:34:55Z | thread: DES-366
issue_id: DES-366
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:34:55Z
updated_at: 2025-09-25T15:34:55Z
sequence: 1

### linear container DES-367

#### 5980046f-e4a3-56f0-8f18-f6554227011d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:36:24Z | thread: DES-367
issue_id: DES-367
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:36:24Z
updated_at: 2025-09-25T15:36:24Z
sequence: 1

### linear container DES-368

#### b8d22538-8e43-5240-8a74-40399ea9372d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:38:15Z | thread: DES-368
issue_id: DES-368
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:38:15Z
updated_at: 2025-09-25T15:38:15Z
sequence: 1

### linear container DES-369

#### c549a962-07e3-5707-948b-fafab28ea49d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T15:39:49Z | thread: DES-369
issue_id: DES-369
author_id: usr_fc22d5941b2aeb5c
body: FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T15:39:49Z
updated_at: 2025-09-25T15:39:49Z
sequence: 1

### linear container DES-370

#### 2d66b43b-70df-599c-89e0-09043ecb3bb3
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:50:02Z | thread: DES-370
issue_id: DES-370
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:50:02Z
updated_at: 2025-09-26T09:50:02Z
sequence: 1

### linear container DES-371

#### 6bae80f0-7156-5308-91d1-bc649360aeaf
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:52:06Z | thread: DES-371
issue_id: DES-371
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:52:06Z
updated_at: 2025-09-26T09:52:06Z
sequence: 1

### linear container DES-372

#### dd6b09c1-124e-5cdc-aa50-9e3bcab984d7
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:53:39Z | thread: DES-372
issue_id: DES-372
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:53:39Z
updated_at: 2025-09-26T09:53:39Z
sequence: 1

### linear container DES-373

#### d58e2ef2-eedf-51fa-8610-a5d00922dfe1
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:17:18Z | thread: DES-373
issue_id: DES-373
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:17:18Z
updated_at: 2025-09-29T11:17:18Z
sequence: 1

### linear container DES-374

#### 5e211a7f-ccb8-5bbe-81aa-dfb6a3251fc2
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:19:24Z | thread: DES-374
issue_id: DES-374
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:19:24Z
updated_at: 2025-09-29T11:19:24Z
sequence: 1

### linear container DES-375

#### f8b3d54a-3b29-5273-9ecf-38e1feebe9e5
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:21:14Z | thread: DES-375
issue_id: DES-375
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:21:14Z
updated_at: 2025-09-29T11:21:14Z
sequence: 1

### linear container DES-376

#### 600e8939-4e8b-5660-9638-c4328b605ff4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:22:37Z | thread: DES-376
issue_id: DES-376
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:22:37Z
updated_at: 2025-09-29T11:22:37Z
sequence: 1

### linear container DES-377

#### f638e4f9-db25-5147-a967-772c4263d4b6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:42:07Z | thread: DES-377
issue_id: DES-377
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-29T12:42:07Z
updated_at: 2025-09-29T12:42:07Z
sequence: 1

### linear container DES-378

#### 1fdef95d-609d-5eba-afb3-1bdc07494156
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:43:17Z | thread: DES-378
issue_id: DES-378
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-29T12:43:17Z
updated_at: 2025-09-29T12:43:17Z
sequence: 1

### linear container DES-379

#### 0d2b852c-979f-5ed8-a046-899a3e81e476
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:04:08Z | thread: DES-379
issue_id: DES-379
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:04:08Z
updated_at: 2025-09-26T13:04:08Z
sequence: 1

### linear container DES-380

#### fc981716-2526-53b9-ad72-1e753cf07fa6
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:06:04Z | thread: DES-380
issue_id: DES-380
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:06:04Z
updated_at: 2025-09-26T13:06:04Z
sequence: 1

### linear container DES-381

#### 2e1503f8-fe6d-5d46-9be3-4f2e70d58bf8
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:07:26Z | thread: DES-381
issue_id: DES-381
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:07:26Z
updated_at: 2025-09-26T13:07:26Z
sequence: 1

### linear container DES-382

#### cbb94883-96c9-5d48-a262-4b3f61968c86
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:08:20Z | thread: DES-382
issue_id: DES-382
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:08:20Z
updated_at: 2025-09-26T13:08:20Z
sequence: 1

### linear container DES-383

#### 17174e8a-464a-5509-a94d-1aae20ffe4b5
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:09:43Z | thread: DES-383
issue_id: DES-383
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:09:43Z
updated_at: 2025-09-26T13:09:43Z
sequence: 1

### linear container DES-384

#### 74e79473-1e5a-55af-9962-cd4ed0303cdd
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:11:33Z | thread: DES-384
issue_id: DES-384
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:11:33Z
updated_at: 2025-09-26T13:11:33Z
sequence: 1

### linear container DES-385

#### 4554db44-2454-5e50-a63e-2e825f187546
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:13:02Z | thread: DES-385
issue_id: DES-385
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:13:02Z
updated_at: 2025-09-26T13:13:02Z
sequence: 1

### linear container DES-386

#### 11a633e9-dfe3-5d3e-93ca-b7831510b562
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T13:14:23Z | thread: DES-386
issue_id: DES-386
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.
created_at: 2025-09-26T13:14:23Z
updated_at: 2025-09-26T13:14:23Z
sequence: 1

### linear container DES-387

#### fc775035-8381-5e0d-9591-626ed573c5b4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:24:21Z | thread: DES-387
issue_id: DES-387
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:24:21Z
updated_at: 2025-09-29T11:24:21Z
sequence: 1

### linear container DES-388

#### 6f786f20-f3fd-59e1-8d4c-4c7dda754a35
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:45:34Z | thread: DES-388
issue_id: DES-388
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-29T12:45:34Z
updated_at: 2025-09-29T12:45:34Z
sequence: 1

### linear container DES-389

#### 6fcca602-b45d-5d9e-a519-d6a67875a6e9
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T08:06:42Z | thread: DES-389
issue_id: DES-389
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.
created_at: 2025-09-25T08:06:42Z
updated_at: 2025-09-25T08:06:42Z
sequence: 1

### linear container DES-390

#### c5008259-08bf-590d-bfaf-5afc88e9c965
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:55:27Z | thread: DES-390
issue_id: DES-390
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:55:27Z
updated_at: 2025-09-26T09:55:27Z
sequence: 1

### linear container DES-391

#### a1ee4ac0-3701-524c-aaa1-656761e111d3
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:57:10Z | thread: DES-391
issue_id: DES-391
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:57:10Z
updated_at: 2025-09-26T09:57:10Z
sequence: 1

### linear container DES-392

#### 420807e5-7eae-5adb-b8f0-99897c93e8fb
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T09:59:26Z | thread: DES-392
issue_id: DES-392
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-26T09:59:26Z
updated_at: 2025-09-26T09:59:26Z
sequence: 1

### linear container DES-393

#### ec5c139f-0fa3-5508-997b-325c926ed298
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:26:46Z | thread: DES-393
issue_id: DES-393
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:26:46Z
updated_at: 2025-09-29T11:26:46Z
sequence: 1

### linear container DES-394

#### 801740a2-691c-5f53-9bba-90c5a6c3405a
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:28:25Z | thread: DES-394
issue_id: DES-394
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:28:25Z
updated_at: 2025-09-29T11:28:25Z
sequence: 1

### linear container DES-395

#### 48c53d03-5e9c-50eb-ad08-85698a838e8c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T11:30:19Z | thread: DES-395
issue_id: DES-395
author_id: usr_fc22d5941b2aeb5c
body: FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder.
created_at: 2025-09-29T11:30:19Z
updated_at: 2025-09-29T11:30:19Z
sequence: 1

### linear container DES-396

#### 08f6b5e9-0d0c-585f-965c-cbe0856d60d1
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:46:59Z | thread: DES-396
issue_id: DES-396
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Waiting on the FBX from Claire.
created_at: 2025-09-29T12:46:59Z
updated_at: 2025-09-29T12:46:59Z
sequence: 1

### linear container DES-397

#### 9e9cd387-beb3-5370-a54f-564699b560d4
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:48:46Z | thread: DES-397
issue_id: DES-397
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. Mine to do, didn't get to it on Friday.
created_at: 2025-09-29T12:48:46Z
updated_at: 2025-09-29T12:48:46Z
sequence: 1

### linear container DES-398

#### b9331366-208f-54f7-b66f-29595e56b81f
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:28:15Z | thread: DES-398
issue_id: DES-398
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep, with its projectile. It is what they call the rocket launcher.
created_at: 2025-09-25T07:28:15Z
updated_at: 2025-09-25T07:28:15Z
sequence: 1

### linear container DES-399

#### e0bf84cd-6269-541d-9a1d-95cde07ef6d2
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:28:51Z | thread: DES-399
issue_id: DES-399
author_id: usr_fc22d5941b2aeb5c
body: In the first zip, 24 Sep. The background of the reference level.
created_at: 2025-09-25T07:28:51Z
updated_at: 2025-09-25T07:28:51Z
sequence: 1

### linear container DES-400

#### 8e46f0c1-1d5f-5a81-94d9-bf044167be06
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T10:21:17Z | thread: DES-400
issue_id: DES-400
author_id: usr_fc22d5941b2aeb5c
body: Unity pack from Marcus, sent Fri 26 Sep. They have been through it and will re-rig the characters from it. They want us to pick one animation and four of the zombies, that one is for Robert.
created_at: 2025-09-29T10:21:17Z
updated_at: 2025-09-29T10:21:17Z
sequence: 1

### linear container DES-401

#### 507e797c-becd-5c82-af5e-a0d2afc68b47
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:11:37Z | thread: DES-401
issue_id: DES-401
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:11:37Z
updated_at: 2025-09-26T14:11:37Z
sequence: 1

### linear container DES-402

#### df8f83f4-dc50-5c79-8fff-cdb205166aa9
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:12:21Z | thread: DES-402
issue_id: DES-402
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:12:21Z
updated_at: 2025-09-26T14:12:21Z
sequence: 1

### linear container DES-403

#### 4f248b0b-3991-59aa-b439-0e4d8742c70d
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:13:59Z | thread: DES-403
issue_id: DES-403
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:13:59Z
updated_at: 2025-09-26T14:13:59Z
sequence: 1

### linear container DES-404

#### 4386339b-9cda-5d85-9470-7895c1c10a1c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:15:03Z | thread: DES-404
issue_id: DES-404
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:15:03Z
updated_at: 2025-09-26T14:15:03Z
sequence: 1

### linear container DES-405

#### 1af79ca9-52b2-50cc-9c85-f699e4ee3e54
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-26T14:16:15Z | thread: DES-405
issue_id: DES-405
author_id: usr_fc22d5941b2aeb5c
body: Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.
created_at: 2025-09-26T14:16:15Z
updated_at: 2025-09-26T14:16:15Z
sequence: 1

### linear container DES-406

#### 9ff62cdd-c2fe-500b-8832-539a7e4e04a7
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:50:36Z | thread: DES-406
issue_id: DES-406
author_id: usr_fc22d5941b2aeb5c
body: Not exported. Calvin is still cutting the ad track down to a loop.
created_at: 2025-09-29T12:50:36Z
updated_at: 2025-09-29T12:50:36Z
sequence: 1

### linear container DES-407

#### c02ca57d-f926-54d1-ba56-b4154f35728a
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:52:29Z | thread: DES-407
issue_id: DES-407
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. The item icons are in Figma, mine to pull as PNG.
created_at: 2025-09-29T12:52:29Z
updated_at: 2025-09-29T12:52:29Z
sequence: 1

### linear container DES-408

#### e3e92efb-563b-5f29-8bbf-b14b95ce291c
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:54:13Z | thread: DES-408
issue_id: DES-408
author_id: usr_fc22d5941b2aeb5c
body: Not exported yet. In Figma, mine to pull as PNG.
created_at: 2025-09-29T12:54:13Z
updated_at: 2025-09-29T12:54:13Z
sequence: 1

### linear container DES-409

#### 31b53426-4274-593c-b1cf-ef944ed22968
table: linear.linear_comments | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-29T12:55:40Z | thread: DES-409
issue_id: DES-409
author_id: usr_fc22d5941b2aeb5c
body: Not sent. Need the .ttf files from Martin.
created_at: 2025-09-29T12:55:40Z
updated_at: 2025-09-29T12:55:40Z
sequence: 1

### linear container team_DES

#### DES-313
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:05:12Z
team_id: team_DES
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 313
title: Playable pack for PlayableX
description: Frederick wants every line of the playable pack tracked after the start slipped. One sub-ticket per line of the pack list, kept in Design so it stays off the ZM3D board. I leave a note on each one saying what I did with it. A line's ticket closes when PlayableX have the file.
priority: 0
started_at: 2025-09-25T07:21:48Z
created_at: 2025-09-25T07:05:12Z
updated_at: 2025-09-25T07:21:48Z

#### DES-314
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:05Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 314
title: Couch
priority: 0
started_at: 2025-09-25T07:21:52Z
completed_at: 2025-09-25T07:24:16Z
created_at: 2025-09-25T07:06:05Z
updated_at: 2025-09-25T07:24:16Z

#### DES-315
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:15Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 315
title: Couch and Pillow
priority: 0
started_at: 2025-09-25T07:21:52Z
completed_at: 2025-09-25T07:25:19Z
created_at: 2025-09-25T07:06:15Z
updated_at: 2025-09-25T07:25:19Z

#### DES-316
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:23Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 316
title: Alarm Clock
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:23Z
updated_at: 2025-09-25T15:21:19Z

#### DES-317
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:31Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 317
title: Record Player
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:31Z
updated_at: 2025-09-25T15:22:57Z

#### DES-318
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:37Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 318
title: Retro TV
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:37Z
updated_at: 2025-09-25T15:24:29Z

#### DES-319
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:43Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 319
title: Desk Lamp
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:43Z
updated_at: 2025-09-26T09:37:26Z

#### DES-320
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:06:52Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 320
title: Small Lamp
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:06:52Z
updated_at: 2025-09-26T09:39:29Z

#### DES-321
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:01Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 321
title: Fly Zapper
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:01Z
updated_at: 2025-09-29T12:31:37Z

#### DES-322
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:10Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 322
title: Grenade
priority: 0
started_at: 2025-09-25T07:21:52Z
completed_at: 2025-09-25T07:26:02Z
created_at: 2025-09-25T07:07:10Z
updated_at: 2025-09-25T07:26:02Z

#### DES-323
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:19Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 323
title: Chainsaw
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:19Z
updated_at: 2025-09-25T08:05:17Z

#### DES-324
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:26Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 324
title: Cute Axe
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:26Z
updated_at: 2025-09-25T08:09:04Z

#### DES-325
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:34Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 325
title: Cute Hammer
priority: 0
started_at: 2025-09-25T07:21:52Z
created_at: 2025-09-25T07:07:34Z
updated_at: 2025-09-25T08:11:13Z

#### DES-326
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:39Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 326
title: Dynamite
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:07:39Z
updated_at: 2025-09-25T08:13:02Z

#### DES-327
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:51Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 327
title: Shuriken
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:07:51Z
updated_at: 2025-09-25T08:14:52Z

#### DES-328
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:07:56Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 328
title: Saber
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:07:56Z
updated_at: 2025-09-26T09:40:54Z

#### DES-329
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:07Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 329
title: Safe
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:07Z
updated_at: 2025-09-26T09:42:45Z

#### DES-330
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:14Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 330
title: Flashlight
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:14Z
updated_at: 2025-09-29T11:06:27Z

#### DES-331
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:23Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 331
title: Fire Extinguisher
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:23Z
updated_at: 2025-09-29T12:33:18Z

#### DES-332
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:31Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 332
title: Propane Tank
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:31Z
updated_at: 2025-09-29T12:35:00Z

#### DES-333
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:36Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 333
title: Plushie Bunny
priority: 0
started_at: 2025-09-25T07:21:55Z
completed_at: 2025-09-25T07:27:19Z
created_at: 2025-09-25T07:08:36Z
updated_at: 2025-09-25T07:27:19Z

#### DES-334
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:46Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 334
title: Plushie Chick
priority: 0
started_at: 2025-09-25T07:21:55Z
completed_at: 2025-09-25T07:28:05Z
created_at: 2025-09-25T07:08:46Z
updated_at: 2025-09-25T07:28:05Z

#### DES-335
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:08:54Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 335
title: Bow
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:08:54Z
updated_at: 2025-09-29T11:08:27Z

#### DES-336
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:01Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 336
title: Cone
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:09:01Z
updated_at: 2025-09-25T08:05:54Z

#### DES-337
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:07Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 337
title: Dice
priority: 0
started_at: 2025-09-25T07:21:55Z
created_at: 2025-09-25T07:09:07Z
updated_at: 2025-09-25T08:16:44Z

#### DES-338
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:17Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 338
title: Gift Box
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:17Z
updated_at: 2025-09-25T08:18:12Z

#### DES-339
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:27Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 339
title: Plushie Dog
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:27Z
updated_at: 2025-09-26T09:44:33Z

#### DES-340
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:33Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 340
title: Plushie Whale
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:33Z
updated_at: 2025-09-26T09:46:24Z

#### DES-341
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:41Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 341
title: Whistle
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:41Z
updated_at: 2025-09-26T09:48:20Z

#### DES-342
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:51Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 342
title: Wooden Tower
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:51Z
updated_at: 2025-09-29T11:09:49Z

#### DES-343
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:09:58Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 343
title: Toy Car
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:09:58Z
updated_at: 2025-09-29T11:12:00Z

#### DES-344
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:07Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 344
title: Toy Boat
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:07Z
updated_at: 2025-09-29T11:13:47Z

#### DES-345
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:13Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 345
title: Toy Airplane
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:13Z
updated_at: 2025-09-29T11:15:13Z

#### DES-346
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:23Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 346
title: Toy Train
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:23Z
updated_at: 2025-09-29T12:36:28Z

#### DES-347
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:28Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 347
title: Beach Ball
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:28Z
updated_at: 2025-09-29T12:38:37Z

#### DES-348
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:38Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 348
title: Bathroom Scale
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:38Z
updated_at: 2025-09-26T11:08:21Z

#### DES-349
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:47Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 349
title: Bathtub
priority: 0
started_at: 2025-09-25T07:21:58Z
created_at: 2025-09-25T07:10:47Z
updated_at: 2025-09-26T11:09:37Z

#### DES-350
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:10:55Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 350
title: Cabinet Sink
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:10:55Z
updated_at: 2025-09-26T11:10:38Z

#### DES-351
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:02Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 351
title: Flip Flops
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:02Z
updated_at: 2025-09-26T11:11:59Z

#### DES-352
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:11Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 352
title: Iron
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:11Z
updated_at: 2025-09-26T11:13:18Z

#### DES-353
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:16Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 353
title: Ironing Board
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:16Z
updated_at: 2025-09-26T11:14:21Z

#### DES-354
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:23Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 354
title: Plunger
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:23Z
updated_at: 2025-09-26T11:16:07Z

#### DES-355
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:31Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 355
title: Slippers
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:31Z
updated_at: 2025-09-26T11:16:55Z

#### DES-356
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:41Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 356
title: Toilet
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:41Z
updated_at: 2025-09-26T11:18:24Z

#### DES-357
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:51Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 357
title: Toilet Paper
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:51Z
updated_at: 2025-09-26T11:19:28Z

#### DES-358
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:11:58Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 358
title: Wash Basin
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:11:58Z
updated_at: 2025-09-26T11:20:42Z

#### DES-359
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:05Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 359
title: Washing Machine
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:12:05Z
updated_at: 2025-09-26T11:22:18Z

#### DES-360
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:11Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 360
title: Rubber Ducky
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:12:11Z
updated_at: 2025-09-29T12:39:47Z

#### DES-361
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:22Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 361
title: Coffee Machine
priority: 0
started_at: 2025-09-25T07:22:01Z
created_at: 2025-09-25T07:12:22Z
updated_at: 2025-09-25T15:26:21Z

#### DES-362
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:30Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 362
title: Cooler
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:30Z
updated_at: 2025-09-25T15:27:40Z

#### DES-363
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:37Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 363
title: Ice Cream Machine
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:37Z
updated_at: 2025-09-25T15:29:42Z

#### DES-364
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:46Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 364
title: Kitchen Mixer
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:46Z
updated_at: 2025-09-25T15:31:34Z

#### DES-365
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:12:55Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 365
title: Microwave
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:12:55Z
updated_at: 2025-09-25T15:33:12Z

#### DES-366
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:03Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 366
title: Oven
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:03Z
updated_at: 2025-09-25T15:34:55Z

#### DES-367
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:11Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 367
title: Refrigerator
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:11Z
updated_at: 2025-09-25T15:36:24Z

#### DES-368
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:17Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 368
title: Stove
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:17Z
updated_at: 2025-09-25T15:38:15Z

#### DES-369
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:24Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 369
title: Toaster
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:24Z
updated_at: 2025-09-25T15:39:49Z

#### DES-370
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:32Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 370
title: Dutch Oven
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:32Z
updated_at: 2025-09-26T09:50:02Z

#### DES-371
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:43Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 371
title: Rolling Pin
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:43Z
updated_at: 2025-09-26T09:52:06Z

#### DES-372
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:47Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 372
title: Round Kettle
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:47Z
updated_at: 2025-09-26T09:53:39Z

#### DES-373
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:13:57Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 373
title: Round Pan
priority: 0
started_at: 2025-09-25T07:22:04Z
created_at: 2025-09-25T07:13:57Z
updated_at: 2025-09-29T11:17:18Z

#### DES-374
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:04Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 374
title: Spatula
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:04Z
updated_at: 2025-09-29T11:19:24Z

#### DES-375
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:14Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 375
title: Whisk
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:14Z
updated_at: 2025-09-29T11:21:14Z

#### DES-376
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:21Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 376
title: Ladle
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:21Z
updated_at: 2025-09-29T11:22:37Z

#### DES-377
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:29Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 377
title: Small Kettle
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:29Z
updated_at: 2025-09-29T12:42:07Z

#### DES-378
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:39Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 378
title: Tall Kettle
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:39Z
updated_at: 2025-09-29T12:43:17Z

#### DES-379
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:47Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 379
title: Acoustic Guitar
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:47Z
updated_at: 2025-09-26T13:04:08Z

#### DES-380
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:14:53Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 380
title: Cello
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:14:53Z
updated_at: 2025-09-26T13:06:04Z

#### DES-381
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:00Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 381
title: Cymbals
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:00Z
updated_at: 2025-09-26T13:07:26Z

#### DES-382
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:11Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 382
title: Electric Guitar
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:11Z
updated_at: 2025-09-26T13:08:20Z

#### DES-383
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:17Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 383
title: Harp
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:17Z
updated_at: 2025-09-26T13:09:43Z

#### DES-384
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:24Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 384
title: Tambourine
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:24Z
updated_at: 2025-09-26T13:11:33Z

#### DES-385
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:33Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 385
title: Trumpet
priority: 0
started_at: 2025-09-25T07:22:07Z
created_at: 2025-09-25T07:15:33Z
updated_at: 2025-09-26T13:13:02Z

#### DES-386
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:41Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 386
title: Xylophone
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:15:41Z
updated_at: 2025-09-26T13:14:23Z

#### DES-387
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:48Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 387
title: Music Keyboard
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:15:48Z
updated_at: 2025-09-29T11:24:21Z

#### DES-388
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:15:56Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 388
title: Grand Piano
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:15:56Z
updated_at: 2025-09-29T12:45:34Z

#### DES-389
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:05Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 389
title: Cactus Plant
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:05Z
updated_at: 2025-09-25T08:06:42Z

#### DES-390
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:13Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 390
title: Barrel
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:13Z
updated_at: 2025-09-26T09:55:27Z

#### DES-391
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:21Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 391
title: Bench
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:21Z
updated_at: 2025-09-26T09:57:10Z

#### DES-392
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:29Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 392
title: Flower Pot
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:29Z
updated_at: 2025-09-26T09:59:26Z

#### DES-393
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:38Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 393
title: Garden Shears
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:38Z
updated_at: 2025-09-29T11:26:46Z

#### DES-394
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:44Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 394
title: Watering Can
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:44Z
updated_at: 2025-09-29T11:28:25Z

#### DES-395
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:16:54Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 395
title: Wooden Bucket
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:16:54Z
updated_at: 2025-09-29T11:30:19Z

#### DES-396
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:02Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 396
title: Wheelbarrow
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:17:02Z
updated_at: 2025-09-29T12:46:59Z

#### DES-397
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:11Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 397
title: Wooden Crate
priority: 0
started_at: 2025-09-25T07:22:10Z
created_at: 2025-09-25T07:17:11Z
updated_at: 2025-09-29T12:48:46Z

#### DES-398
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:17Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 398
title: Cannon
priority: 0
started_at: 2025-09-25T07:22:13Z
completed_at: 2025-09-25T07:29:07Z
created_at: 2025-09-25T07:17:17Z
updated_at: 2025-09-25T07:29:07Z

#### DES-399
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:23Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 399
title: Background
priority: 0
started_at: 2025-09-25T07:22:13Z
completed_at: 2025-09-25T07:29:59Z
created_at: 2025-09-25T07:17:23Z
updated_at: 2025-09-25T07:29:59Z

#### DES-400
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:34Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: Done
number: 400
title: Zombie characters
priority: 0
started_at: 2025-09-25T07:22:13Z
completed_at: 2025-09-29T10:22:00Z
created_at: 2025-09-25T07:17:34Z
updated_at: 2025-09-29T10:22:00Z

#### DES-401
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:41Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 401
title: Matching sound
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:17:41Z
updated_at: 2025-09-26T14:11:37Z

#### DES-402
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:50Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 402
title: Rocket sound
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:17:50Z
updated_at: 2025-09-26T14:12:21Z

#### DES-403
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:17:59Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 403
title: Explosion sound
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:17:59Z
updated_at: 2025-09-26T14:13:59Z

#### DES-404
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:05Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 404
title: Success sound
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:05Z
updated_at: 2025-09-26T14:15:03Z

#### DES-405
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:15Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 405
title: Failure sound
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:15Z
updated_at: 2025-09-26T14:16:15Z

#### DES-406
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:23Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 406
title: Background music
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:23Z
updated_at: 2025-09-29T12:50:36Z

#### DES-407
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:29Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 407
title: Item visuals
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:29Z
updated_at: 2025-09-29T12:52:29Z

#### DES-408
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:36Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 408
title: UI elements
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:36Z
updated_at: 2025-09-29T12:54:13Z

#### DES-409
table: linear.linear_issues | statement: insert | author: usr_fc22d5941b2aeb5c | date: 2025-09-25T07:18:47Z
team_id: team_DES
parent_id: DES-313
assignee_id: usr_fc22d5941b2aeb5c
creator_id: usr_fc22d5941b2aeb5c
state_id: In Progress
number: 409
title: Fonts
priority: 0
started_at: 2025-09-25T07:22:13Z
created_at: 2025-09-25T07:18:47Z
updated_at: 2025-09-29T12:55:40Z

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
text: <@EMPLOYEE_0026_SLACK_ID> for PlayableX's question, in case we carry on with them: one animation, walk. The 4 zombies: Party Girl, Plumber, Magician, Football Player. All four are in the pack Marcus sent.
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
text: Julia, PlayableX are holding Nov 3 for us and I don't want a third slip on our side. While it's parked, can you do for this one what you did for the Dominoes playable: write the brief they build from, and tell me where the item pack actually stands. Brian's pack list is where it starts. Robert's picks for the board and the zombies stand unless he's changed them since. My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files. Write it for the game as it is today; if the core changes we redo that part with them in November. Brief as a doc and the hand-off list as a sheet, both in your Drive. Then give me the count for each state here, and post both links in the PlayableX channel so they know what's still coming from us.
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
    Parked until Nov 3, the new start PlayableX gave us after we asked for the pause. Julia is pulling the brief and the pack status together for Frederick in the meantime.
    card: name=Playable Kickoff, idShort=447
    list: name=To Do

### trello container trello_boards

#### 640643a3fd8f3ca308d9318e
table: trello.trello_boards | statement: update (changes a record that is in the base) | date: 2025-09-30T20:05:47Z
dateLastActivity: 2025-09-30T20:05:47Z
