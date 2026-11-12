# LOCAL REHEARSAL — not a platform verdict

Blind pass O2 (Completeness) · stage oe (/oe) · round 4 · scope changed

You are a fresh, blind reviewer running one pass of the platform's deep recheck, rehearsed locally. This brief is your whole context: you have not seen the main review, any earlier round, any other pass's findings, the author's design, notes or check reports, and you must not look for them. You save no file, edit nothing and never execute SQL.

## What you may open (and nothing else)

- this brief;
- the inputs listed below (copies made for this round):
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round4/inputs/00_Task_Details.txt` (sha256 ed790e3e48b6)
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round4/inputs/01_Universe_Inject.sql` (sha256 7d1f2aaeb29c)
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round4/inputs/04_Prompt.txt` (sha256 33c721d60945)
  - `Task_Authoring/task_inputs/Working_Files/local_reviews/oe/round4/inputs/artifact/08_Oracle_Events.md` (sha256 6200845d5432)
- reference files the platform also gives this pass: `Evals/references/rules/deep_recheck.md`, `Evals/references/rules/common_errors.md`, `Evals/SEARCH.md`, `Evals/references/persona/`;
- the universe, only through the commands under Universe.

Never open anything else: no other file in `Task_Authoring/task_inputs/` (its Working_Files/, eval_reports/, other rounds or passes under `Working_Files/local_reviews/`), no other task folder, nothing under Task_Authoring/support/ except your own scratch files, Task_Authoring/archived_tasks/, the Evals input store (the task_inputs folder under Evals/) or any memory or notes file.

## Task details (the assignment as the platform saves it)

```text
🏢 Business Function
Product

🧑 Persona
Julia Lawson
Role: Product Manager

🎯 Competency
Marketing and GTM

🛠️ Task Skill
Authoring

📋 Task Type
long-horizon

🎚️ Difficulty Mode
hard

📅 Universe Date
October 1, 2025 07:00
```

Clock: 2025-10-01 00:00 PT (synth-cut universe, task date Oct 1, 2025).
Persona key for persona_view.py: `julia_lawson`.

## Injection

Injection SQL: the `01_Universe_Inject.sql` copy under the inputs above (sha256 7d1f2aaeb29c).

Friction (error and wait configuration): none.

## Universe

Run these from the workspace root (the folder that holds Evals/ and Task_Authoring/). They read the task's universe
as the platform tools would; they never write into Evals/:

    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search inventory
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search search <service> "<terms>" --limit 20
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search search-many --request <queries.json> --compact
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search get <service> --file <file> --pointer <pointer>
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search get-many --request <reads.json> --compact
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search lookup <service> --ids-file <ids.json> --file '<glob>'
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs records --request <checks.json>
    python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs reference routes <service>
    python3 Task_Authoring/tools/persona_view.py --task-dir Task_Authoring/task_inputs can-see julia_lawson <service> <id>
    python3 Task_Authoring/tools/persona_view.py --task-dir Task_Authoring/task_inputs search julia_lawson <service> "<query>"

Where a text below says `python3 Evals/tools/hg_search.py <args>` (or hg_records.py, hg_reference.py), run
`python3 Task_Authoring/tools/hg.py --task-dir Task_Authoring/task_inputs search <args>` (or `records`, `reference`) instead; never run
a helper under Evals/tools/ directly. persona_view.py applies this persona's read access (Evals/references/persona/
acl.md) to Gmail, Slack, Calendar and the Drive family. Put any request file you write under
Task_Authoring/support/scratch/ and delete it when you are done.
Base search does not show injected rows: the injection rows are in the SQL copy under Inputs. Read it as text, a proposed overlay on base; never execute it.

## The artifact under review: 08_Oracle_Events.md (sha256 6200845d5432d5e5dcce5d475acb7af380b15295126626f286dc487b1f623887)

### OE 1

````text
OE 1  Find Frederick's message of yesterday in Slack: search for "playable" on Sep 30 2025 and read Julia's direct messages with Frederick Stone
Expected: Frederick Stone, Tue Sep 30 2025 11:21 AM PT, DM D05SD5QLG94, ts 1759256494.852159: "Julia, PlayableX are holding Nov 3 for us and I don't want a third slip on our side. While it's parked, can you do for this one what you did for the Dominoes playable: write the brief they build from, and tell me where the item pack actually stands. Brian's pack list is where it starts. Robert's picks for the board and the zombies stand unless he's changed them since. My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files. Write it for the game as it is today; if the core changes we redo that part with them in November. Brief as a doc and the hand-off list as a sheet, both in your Drive. Then give me the count for each state here, and post both links in the PlayableX channel so they know what's still coming from us."
````

### OE 2

````text
OE 2  Find Frederick's hand-off notes in Google Drive (search "hand-off notes") and read the document in Google Docs (OE 1)
Expected: Document "ZM3D playable: hand-off notes", owner frederick.stone@harmonygames.co, file f_8c1d0bca1d1d5fde4c5008. "The brief. One doc PlayableX can build from: which scenario we picked and what it is for, the eight items on the board and that every other board item on the list is an extra they can swap in, the four zombies and the one animation, how a level is won and lost and how many slots the tray has, what they can use for sound and when the music may start, and the start date. How the level plays is on the design page; your deck of the reference level has what we built for them. What they told us about formats still holds, and so does their rule from last time about when the music may start." "The hand-off list. One row per line of Brian's pack list, with these columns: Line, Category, Board set, State, What's owed, Who has it, Ticket. Line, Category and Ticket are as on his list. Board set is Default for the eight on the board and Extra for every other board item; leave it empty for anything that isn't a board item." "State is one of three words, nothing else. Delivered: PlayableX has the current file and can use it. Ready: exported in a format they take and sitting in the outgoing folder, it opens, it is the current version and nobody is changing it. Owed: anything else. For an Owed line say what is owed, and who has it, meaning whoever has to do the next thing." "Brian's note on each ticket says what he did with the line. Take it as it stands unless something later says otherwise, and go by how things stand today, not the day he wrote it: if someone who knows the file or the art has said something since, that counts. If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again, and it sits with whoever the file came from." "Sound: we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we have our own version." "Tickets live under Brian's pack ticket, one per line. An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. Leave the Delivered and Ready ones as they are." "Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address, which is in Contacts."
````

### OE 3

````text
OE 3  Find Brian's pack list in Google Drive (search "pack list") and read every row of its Pack tab in Google Sheets (OE 1)
Expected: Spreadsheet "ZM3D playable - pack list", owner brian.foster@harmonygames.co, file f_956e60ec7f2f7977d98934, tab "Pack", columns Line, Kind, Category, Went out, Ticket. 96 rows. Kind "Board item" on 84 rows, by Category, each line with its Ticket. Living Room: Couch DES-314, Couch and Pillow DES-315, Alarm Clock DES-316, Record Player DES-317, Retro TV DES-318, Desk Lamp DES-319, Small Lamp DES-320, Fly Zapper DES-321. Survival: Grenade DES-322, Chainsaw DES-323, Cute Axe DES-324, Cute Hammer DES-325, Dynamite DES-326, Shuriken DES-327, Saber DES-328, Safe DES-329, Flashlight DES-330, Fire Extinguisher DES-331, Propane Tank DES-332. Toys: Plushie Bunny DES-333, Plushie Chick DES-334, Bow DES-335, Cone DES-336, Dice DES-337, Gift Box DES-338, Plushie Dog DES-339, Plushie Whale DES-340, Whistle DES-341, Wooden Tower DES-342, Toy Car DES-343, Toy Boat DES-344, Toy Airplane DES-345, Toy Train DES-346, Beach Ball DES-347. Bathroom: Bathroom Scale DES-348, Bathtub DES-349, Cabinet Sink DES-350, Flip Flops DES-351, Iron DES-352, Ironing Board DES-353, Plunger DES-354, Slippers DES-355, Toilet DES-356, Toilet Paper DES-357, Wash Basin DES-358, Washing Machine DES-359, Rubber Ducky DES-360. Kitchen: Coffee Machine DES-361, Cooler DES-362, Ice Cream Machine DES-363, Kitchen Mixer DES-364, Microwave DES-365, Oven DES-366, Refrigerator DES-367, Stove DES-368, Toaster DES-369, Dutch Oven DES-370, Rolling Pin DES-371, Round Kettle DES-372, Round Pan DES-373, Spatula DES-374, Whisk DES-375, Ladle DES-376, Small Kettle DES-377, Tall Kettle DES-378. Music Instruments: Acoustic Guitar DES-379, Cello DES-380, Cymbals DES-381, Electric Guitar DES-382, Harp DES-383, Tambourine DES-384, Trumpet DES-385, Xylophone DES-386, Music Keyboard DES-387, Grand Piano DES-388. Garden: Cactus Plant DES-389, Barrel DES-390, Bench DES-391, Flower Pot DES-392, Garden Shears DES-393, Watering Can DES-394, Wooden Bucket DES-395, Wheelbarrow DES-396, Wooden Crate DES-397. The other 12 rows have no Category: Kind "Weapon": Cannon DES-398; Kind "Background": Background DES-399; Kind "Zombies": Zombie characters DES-400; Kind "Sound": Matching sound DES-401, Rocket sound DES-402, Explosion sound DES-403, Success sound DES-404, Failure sound DES-405, Background music DES-406; Kind "2D": Item visuals DES-407, UI elements DES-408; Kind "Font": Fonts DES-409. Went out is filled on 8 rows: "zip 24 Sep" on Couch, Couch and Pillow, Grenade, Plushie Bunny, Cannon, Background; "zip 24 Sep (second)" on Plushie Chick; "pack 26 Sep" on Zombie characters.
````

### OE 4

````text
OE 4  Open DES-314, the first ticket on the list, in Linear, go to its parent and list the parent's sub-tickets (OE 3)
Expected: Parent DES-313 "Playable pack for PlayableX", team Design, created by Brian Foster (brian.foster@harmonygames.co in Linear), state In Progress: "One sub-ticket per line of the pack list, kept in Design so it stays off the ZM3D board. I leave a note on each one saying what I did with it. A line's ticket closes when PlayableX have the file." 96 sub-tickets, DES-314 to DES-409, each titled with its line. State Done on 8: Couch DES-314, Couch and Pillow DES-315, Grenade DES-322, Plushie Bunny DES-333, Plushie Chick DES-334, Cannon DES-398, Background DES-399, Zombie characters DES-400. State In Progress on the other 88.
````

### OE 5

````text
OE 5  Read Brian's note, the one comment, on each of the 96 sub-tickets in Linear (list the comments of DES-314 to DES-409) (OE 4)
Expected: One comment by Brian Foster (brian.foster@harmonygames.co) on every ticket. "In the first zip, 24 Sep." on 4: Couch, Couch and Pillow, Grenade, Plushie Bunny. "FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder." on 12: Alarm Clock, Record Player, Retro TV, Coffee Machine, Cooler, Ice Cream Machine, Kitchen Mixer, Microwave, Oven, Refrigerator, Stove, Toaster. "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder." on 25: Desk Lamp, Small Lamp, Saber, Safe, Plushie Dog, Plushie Whale, Whistle, Bathroom Scale, Bathtub, Cabinet Sink, Flip Flops, Iron, Ironing Board, Plunger, Slippers, Toilet, Toilet Paper, Wash Basin, Washing Machine, Dutch Oven, Rolling Pin, Round Kettle, Barrel, Bench, Flower Pot. "Not exported yet. Waiting on the FBX from Claire." on 6: Fly Zapper, Fire Extinguisher, Beach Ball, Rubber Ducky, Grand Piano, Wheelbarrow. "FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder." on 3: Chainsaw, Cone, Cactus Plant. "FBX from Claire, Thu 25 Sep. Opens, looks right. In the outgoing folder." on 6: Cute Axe, Cute Hammer, Dynamite, Shuriken, Dice, Gift Box. "FBX from Claire, Mon 29 Sep. Opens, looks right. In the outgoing folder." on 14: Flashlight, Bow, Wooden Tower, Toy Car, Toy Boat, Toy Airplane, Round Pan, Spatula, Whisk, Ladle, Music Keyboard, Garden Shears, Watering Can, Wooden Bucket. "Not exported yet. Mine to do, didn't get to it on Friday." on 5: Propane Tank, Toy Train, Small Kettle, Tall Kettle, Wooden Crate. Plushie Chick: "Went in the second zip on 24 Sep (the one they called the duck). Their message today about that zip is the zombie package, not the chick." "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder." on 8: Acoustic Guitar, Cello, Cymbals, Electric Guitar, Harp, Tambourine, Trumpet, Xylophone. Cannon: "In the first zip, 24 Sep, with its projectile. It is what they call the rocket launcher." Background: "In the first zip, 24 Sep. The background of the reference level." Zombie characters: "Unity pack from Marcus, sent Fri 26 Sep. They have been through it and will re-rig the characters from it. They want us to pick one animation and four of the zombies, that one is for Robert." "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder." on 5: Matching sound, Rocket sound, Explosion sound, Success sound, Failure sound. Background music: "Not exported. Calvin is still cutting the ad track down to a loop." Item visuals: "Not exported yet. The item icons are in Figma, mine to pull as PNG." UI elements: "Not exported yet. In Figma, mine to pull as PNG." Fonts: "Not sent. Waiting on the .ttf files from Martin." By the notes' Owed rule (OE 2), these lines are Owed on their own note: Fly Zapper, Fire Extinguisher, Beach Ball, Rubber Ducky, Grand Piano, Wheelbarrow: the FBX from Claire, with Claire. Propane Tank, Toy Train, Small Kettle, Tall Kettle, Wooden Crate: the export, with Brian. Background music: the loop cut from the ad track, with Calvin. Item visuals, UI elements: the PNG export from Figma, with Brian. Fonts: the .ttf files, with Martin.
````

### OE 6

````text
OE 6  Find the PlayableX channel in Slack (channel search "playablex", private channels included; it is C08H78VJG80), read its history for September 2025 and the thread under Frederick's Sep 12 message (OE 2)
Expected: Channel C08H78VJG80. Frederick Stone, Fri Sep 12 2025 9:38 AM PT, ts 1757695108.506159: "I think Scenario 1 is a good bet for filtering out the players that won't like our game, while remaining true to our core game play." Frederick Stone, Mon Sep 15 2025 10:07 AM PT, ts 1757956024.883249: "lets go with Scenario 1." PERSON_6078_SLACK_ID of PlayableX, Tue Sep 16 2025 4:34 AM PT, ts 1758022459.227279: "aside from the 8-item set that you will provide for the board, you can also test any additional items you’d like to try in the game"; "*3D assets*: .fbx, .glb, or .blend (when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII)"; "*Sound*: .mp3 or .wav"
````

### OE 7

````text
OE 7  Read the thread under Frederick's Sep 18 message in the PlayableX channel in Slack, where Brian sent the assets (thread ts 1758227288.370029) (OE 5)
Expected: Brian Foster, Wed Sep 24 2025 5:39 AM PT, ts 1758717576.077489: "You can access the game assets here." with the file Playable-assets-harmonygames-games.zip. Brian Foster, Wed Sep 24 2025 5:40 AM PT, ts 1758717625.209649: "The fail condition in the game is when zombies reach us and deplete our HP, while the win condition is eliminating all the zombies on screen". PERSON_6078_SLACK_ID of PlayableX, Wed Sep 24 2025 7:18 AM PT, ts 1758723504.085039: "At this stage, the only missing piece seems to be the duck asset used in the reference." Brian Foster, Wed Sep 24 2025 8:58 AM PT, ts 1758729487.922339: "Sure, I’m sending the files." with the file Plushie-and-zombies.zip. PERSON_6078_SLACK_ID of PlayableX, Thu Sep 25 2025 6:50 AM PT, ts 1758808234.045839: "We’ve checked the zombie assets, but it looks like the package wasn’t exported correctly." Brian Foster, Fri Sep 26 2025 10:00 AM PT, ts 1758906043.375719: "Sorry, it took a little while, I had to get help from our animator" with the file zombies_Characters_UnityPack.zip. PERSON_6078_SLACK_ID of PlayableX, Mon Sep 29 2025 3:16 AM PT, ts 1759140968.965099: "We have reviewed the assets."; "Select the primary animation you want us to use (attack, idle, die, or walk), and"; "Specify the 4 zombie characters to which this animation should be applied." With the Done tickets and their notes (OE 4, OE 5) and the notes' Delivered rule (OE 2), these 8 lines are Delivered: Couch, Couch and Pillow, Grenade, Plushie Bunny, Plushie Chick, Cannon, Background, Zombie characters.
````

### OE 8

````text
OE 8  Read the thread under Frederick's Sep 29 message in the PlayableX channel in Slack (thread ts 1759174925.309129) for the start date (OE 1)
Expected: Frederick Stone, Mon Sep 29 2025 12:42 PM PT, ts 1759174925.309129: "I think we should pause development of the playable for a month or so". PERSON_6078_SLACK_ID of PlayableX, Tue Sep 30 2025 2:59 AM PT, ts 1759226395.551469: "We’re planning the new start date for the game on November 3rd."
````

### OE 9

````text
OE 9  Search Slack for "music" in the PlayableX channel to find their rule from the first playable about when the music may start (OE 2)
Expected: PERSON_6073_SLACK_ID of PlayableX, Mon Apr 14 2025 6:27 AM PT, ts 1744637266.363689, in C08H78VJG80: "music has to start after first click as a rule"
````

### OE 10

````text
OE 10  Read #zombie-design in Slack from Sep 22 2025 on (channel history, and the thread under Brian's Sep 22 post about the playable scenario) for what the playable is for, Robert's picks and what he posted after them (OE 1)
Expected: Robert, Mon Sep 22 2025 12:34 PM PT, ts 1758569655.409719: "the idea is to test the current form and audience fit"; Julia Lawson, Mon Sep 22 2025 12:35 PM PT, ts 1758569707.508219: "do a more hardcore friendly playable and see how they do with the funnel"; Julia Lawson, Mon Sep 22 2025 12:37 PM PT, ts 1758569824.148029: "Do you want to try a cute level with lots of grenades and shruiken then?"; Robert, Mon Sep 22 2025 12:37 PM PT, ts 1758569872.578829: "Doesn't really matter"; Robert, Mon Sep 22 2025 12:38 PM PT, ts 1758569885.985319: "I think we should remain as is". So the playable tests the game in its current form and its audience fit; the hardcore-friendly line is walked back (with the ask's "Write it for the game as it is today", OE 1). Robert, Thu Sep 25 2025 11:12 AM PT, ts 1758823946.262829: "For the playable board, the 8: Grenade, Couch and Plushie Chick from the reference level, plus Shuriken, Cute Axe, Gift Box, Cactus Plant and Dynamite." "Everything else" Brian Foster (tagged) "sends them is extras they can swap in." Robert, Mon Sep 29 2025 10:31 AM PT, ts 1759167068.371289: "one animation, walk. The 4 zombies: Party Girl, Plumber, Magician, Football Player. All four are in the pack Marcus sent." Robert, Mon Sep 29 2025 4:44 PM PT, ts 1759189466.554739: "Got new colored version of cactus, chainsaw and cones that can probably come in handy:" — later than the Thu Sep 25 notes on Chainsaw, Cone, Cactus Plant (OE 5).
````

### OE 11

````text
OE 11  Check whether Robert changed a pick since Sep 25: search Slack for his messages from that day on and read the thread under Julia's bow post in #zombie-art (OE 1, OE 10)
Expected: Julia Lawson, Fri Sep 26 2025 9:27 AM PT, ts 1758904025.123869: "Can we have arrow to go with the bow?" Claire Morgan, Fri Sep 26 2025 9:28 AM PT, ts 1758904103.894649: "Of course". Robert, Fri Sep 26 2025 2:41 PM PT, ts 1758922879.243189: "Fun one. Let's have it in the 8 in place of the last one on my list, we've got enough things that go boom. As it is now, the arrow can be its own item later." His Sep 25 list ends with Dynamite, so the eight on the board are Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant, Bow; Dynamite stays on the pack list as an extra.
````

### OE 12

````text
OE 12  Read #zombie-match3d in Slack from Sep 25 2025 on (channel history) for anything said about Brian's exports after his notes (OE 2, OE 5)
Expected: Marcus Bennett, Fri Sep 26 2025 10:08 AM PT, ts 1758906517.912099, tagging Brian Foster: "fyi the models you got out of unity on thursday are the text kind, the setting was wrong that day so youll need to redo them. they open fine in unity and in max so you wouldnt notice." "the ones from" Claire Morgan (tagged) "are ok". With PlayableX's Binary-only rule (OE 6), the 12 lines whose note says "FBX saved out of the project, Thu 25 Sep" (OE 5) are Owed: a binary FBX export, with Brian: Alarm Clock, Record Player, Retro TV, Coffee Machine, Cooler, Ice Cream Machine, Kitchen Mixer, Microwave, Oven, Refrigerator, Stove, Toaster.
````

### OE 13

````text
OE 13  Read Julia's direct messages with Robert in Slack from Sep 25 2025 on (conversation history) (OE 2, OE 5)
Expected: Robert, Mon Sep 29 2025 1:38 PM PT, DM D05GU6L0XFH, ts 1759178332.042459, tagging Claire Morgan: "is redoing the UVs on the bathroom objects from scratch, so the old ones will show in the levels for a bit." "the bathroom files she gave" Brian Foster (tagged) "on Friday are the old version too". So the 12 Bathroom lines whose note says "FBX from Claire, Fri 26 Sep" (OE 5) are Owed: the file again once the UVs are redone, with Claire: Bathroom Scale, Bathtub, Cabinet Sink, Flip Flops, Iron, Ironing Board, Plunger, Slippers, Toilet, Toilet Paper, Wash Basin, Washing Machine.
````

### OE 14

````text
OE 14  Find Brian's log of the outgoing folder in Google Drive (search "outgoing folder") and read it in Google Docs (OE 2, OE 5)
Expected: Document "Outgoing folder - what's in it", owner brian.foster@harmonygames.co, file f_faf4d7c167d14a1127dcc3. "Fri 26 Sep: more files from Claire. The music instruments went in as one zip. The .wav exports." "Tue 30 Sep: Claire sent the three recoloured models again. Opened them, they look right, and they replace Thursday's." "The zip with Friday's music instruments got cut off on upload, it won't unpack on my side, and those eight aren't in the folder any other way. I still have Claire's files, I'll put them back when we pick this up again." So Chainsaw, Cone, Cactus Plant, the three with new colour versions (OE 10), are current and in the folder again: Ready. The 8 instrument lines whose note says "Zipped with the other instruments" (OE 5) are Owed: the file put back in the outgoing folder, with Brian: Acoustic Guitar, Cello, Cymbals, Electric Guitar, Harp, Tambourine, Trumpet, Xylophone.
````

### OE 15

````text
OE 15  Find Calvin's sound sources sheet in Google Drive (search "sound") and read its Sources tab in Google Sheets (OE 2)
Expected: Spreadsheet "ZM3D sound sources", owner calvin.price@harmonygames.co, file f_b2387e31d46d3a7b3fa2a9, tab "Sources", columns Cue, Where it came from, OK outside the game, Replacement. Matching sound, Success sound and Failure sound: "made here", "yes". Rocket sound: "Soundly library (Robert's seat)", "no", "not made yet, Calvin". Explosion sound: "Universal Sound FX pack (Unity Asset Store, Robert's)", "no", "not made yet, Calvin". Background music: "new track for the ad, generated and edited here (not the in-game track)", "yes". By the notes' sound rule (OE 2), Rocket sound, Explosion sound, exported on Fri 26 Sep (OE 5), are Owed: our own version of the sound, with Calvin.
````

### OE 16

````text
OE 16  Read Julia's deck of the reference level in Google Slides (search Google Drive for "reference level") (OE 2)
Expected: Presentation "ZM3D playable - reference level", owner julia.lawson@harmonygames.co, file f_6a2fa8e61b31139ca8e3d4. Slide "Board": "Grenade (red, green), Couch, Couch and Pillow, Plushie Bunny, Plushie Chick." Slide "Zombies": "A mix, nothing fixed yet." Slide "Win and lose": "Win: every zombie on screen is eliminated. Lose: the zombies reach us and our HP runs out."
````

### OE 17

````text
OE 17  Open the design page in Confluence (search "7-slot tray" or the title) and read its core mechanic and its comments (OE 2)
Expected: Page "Zombie Match 3D — Game Design Document", page_zm3d_gdd: "the player drags items into a 7-slot tray"; "It is a tempo penalty, not a fail state - the loss screen only appears at zero health." Comments: Julia Lawson: "I pulled the 7-slot tray down to 6 in a soft-test branch"; Robert: "keep the GDD at 7 for now".
````

### OE 18

````text
OE 18  Find the kickoff hold on Julia's calendar in Google Calendar (search "kickoff", November 2025) (OE 2)
Expected: Event "ZM3D playable kickoff with PlayableX", evt_421695d009e589ee85296c, starts Mon Nov 3 2025 9:00 AM PT, organizer frederick.stone@harmonygames.co. Attendees: brian.foster@harmonygames.co, frederick.stone@harmonygames.co, julia.lawson@harmonygames.co, robert@harmonygames.co.
````

### OE 19

````text
OE 19  Look up PlayableX's intake address in Contacts (search "PlayableX") (OE 2)
Expected: Contact "PlayableX Intake", "Project intake (playable ads)", intake@playablex.ai.
````

### OE 20

````text
OE 20  Create the brief as a Google Doc in Julia's Drive (Google Docs, a new document with its text) (OE 1, OE 2)
Expected: A new document owned by Julia, in her Drive, that PlayableX can build from. It says: the scenario is Scenario 1, picked to filter out the players that won't like our game while remaining true to our core game play (OE 6), and there to test the game in its current form and its audience fit, not what the game could be tailored to become (OE 10); the eight on the board are Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant, Bow, and every other board item on Brian's list is an extra they can swap in (OE 11); the four zombies are Party Girl, Plumber, Magician and Football Player and the one animation is walk (OE 10); a level is won when every zombie on screen is eliminated and lost when the zombies reach us and our HP runs out (OE 7, OE 16, OE 17); the tray has 7 slots (OE 17); for sound they can use Matching sound, Success sound and Failure sound, Rocket sound and Explosion sound stay with us until we have our own versions, and the background music is a new track for the ad that Calvin is still cutting (OE 15, OE 5); the music may start after the first click (OE 9); the start date is November 3 (OE 8).
````

### OE 21

````text
OE 21  Create the hand-off list as a Google Sheet in Julia's Drive (Google Sheets, a new spreadsheet) (OE 1)
Expected: A new spreadsheet owned by Julia, in her Drive.
````

### OE 22

````text
OE 22  Write the header and the 96 rows into the hand-off list (Google Sheets, update values on the spreadsheet of OE 21)
Expected: Header: Line, Category, Board set, State, What's owed, Who has it, Ticket. One row per line of Brian's pack list, 96 rows, with Line, Category and Ticket as on his list (OE 3). Board set is Default on the eight of OE 11, Extra on the other 76 board items and empty on the 12 lines that are not board items. State is Delivered on the 8 lines of OE 7; Owed on the 49 lines of OE 5, OE 12, OE 13, OE 14, OE 15, each with what is owed and who has it as stated there; and Ready on the other 39, whose note says the file is exported, opens or plays and is in the outgoing folder (OE 5, with Chainsaw, Cone, Cactus Plant current again by OE 14): Desk Lamp, Small Lamp, Chainsaw, Cute Axe, Cute Hammer, Dynamite, Shuriken, Saber, Safe, Flashlight, Bow, Cone, Dice, Gift Box, Plushie Dog, Plushie Whale, Whistle, Wooden Tower, Toy Car, Toy Boat, Toy Airplane, Dutch Oven, Rolling Pin, Round Kettle, Round Pan, Spatula, Whisk, Ladle, Music Keyboard, Cactus Plant, Barrel, Bench, Flower Pot, Garden Shears, Watering Can, Wooden Bucket, Matching sound, Success sound, Failure sound.
````

### OE 23

````text
OE 23  Share the brief (OE 20) with brian.foster@harmonygames.co as a viewer in Google Drive (OE 2, OE 18)
Expected: brian.foster@harmonygames.co has reader access to the brief.
````

### OE 24

````text
OE 24  Share the brief (OE 20) with frederick.stone@harmonygames.co as a viewer in Google Drive (OE 2, OE 18)
Expected: frederick.stone@harmonygames.co has reader access to the brief.
````

### OE 25

````text
OE 25  Share the brief (OE 20) with robert@harmonygames.co as a viewer in Google Drive (OE 2, OE 18)
Expected: robert@harmonygames.co has reader access to the brief.
````

### OE 26

````text
OE 26  Share the brief (OE 20) with intake@playablex.ai as a viewer in Google Drive (OE 2, OE 19)
Expected: intake@playablex.ai has reader access to the brief.
````

### OE 27

````text
OE 27  Share the hand-off list (OE 21) with brian.foster@harmonygames.co as a viewer in Google Drive (OE 2, OE 18)
Expected: brian.foster@harmonygames.co has reader access to the hand-off list.
````

### OE 28

````text
OE 28  Share the hand-off list (OE 21) with frederick.stone@harmonygames.co as a viewer in Google Drive (OE 2, OE 18)
Expected: frederick.stone@harmonygames.co has reader access to the hand-off list.
````

### OE 29

````text
OE 29  Share the hand-off list (OE 21) with robert@harmonygames.co as a viewer in Google Drive (OE 2, OE 18)
Expected: robert@harmonygames.co has reader access to the hand-off list.
````

### OE 30

````text
OE 30  Share the hand-off list (OE 21) with intake@playablex.ai as a viewer in Google Drive (OE 2, OE 19)
Expected: intake@playablex.ai has reader access to the hand-off list.
````

### OE 31

````text
OE 31  Move DES-316 (Alarm Clock) to Todo in Linear (OE 2, OE 12)
Expected: DES-316 is in state Todo.
````

### OE 32

````text
OE 32  Comment on DES-316 (Alarm Clock) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-316: a binary FBX export is owed; Brian has it.
````

### OE 33

````text
OE 33  Move DES-317 (Record Player) to Todo in Linear (OE 2, OE 12)
Expected: DES-317 is in state Todo.
````

### OE 34

````text
OE 34  Comment on DES-317 (Record Player) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-317: a binary FBX export is owed; Brian has it.
````

### OE 35

````text
OE 35  Move DES-318 (Retro TV) to Todo in Linear (OE 2, OE 12)
Expected: DES-318 is in state Todo.
````

### OE 36

````text
OE 36  Comment on DES-318 (Retro TV) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-318: a binary FBX export is owed; Brian has it.
````

### OE 37

````text
OE 37  Move DES-321 (Fly Zapper) to Todo in Linear (OE 2, OE 5)
Expected: DES-321 is in state Todo.
````

### OE 38

````text
OE 38  Comment on DES-321 (Fly Zapper) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-321: the FBX from Claire is owed; Claire has it.
````

### OE 39

````text
OE 39  Move DES-331 (Fire Extinguisher) to Todo in Linear (OE 2, OE 5)
Expected: DES-331 is in state Todo.
````

### OE 40

````text
OE 40  Comment on DES-331 (Fire Extinguisher) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-331: the FBX from Claire is owed; Claire has it.
````

### OE 41

````text
OE 41  Move DES-332 (Propane Tank) to Todo in Linear (OE 2, OE 5)
Expected: DES-332 is in state Todo.
````

### OE 42

````text
OE 42  Comment on DES-332 (Propane Tank) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-332: the export is owed; Brian has it.
````

### OE 43

````text
OE 43  Move DES-346 (Toy Train) to Todo in Linear (OE 2, OE 5)
Expected: DES-346 is in state Todo.
````

### OE 44

````text
OE 44  Comment on DES-346 (Toy Train) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-346: the export is owed; Brian has it.
````

### OE 45

````text
OE 45  Move DES-347 (Beach Ball) to Todo in Linear (OE 2, OE 5)
Expected: DES-347 is in state Todo.
````

### OE 46

````text
OE 46  Comment on DES-347 (Beach Ball) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-347: the FBX from Claire is owed; Claire has it.
````

### OE 47

````text
OE 47  Move DES-348 (Bathroom Scale) to Todo in Linear (OE 2, OE 13)
Expected: DES-348 is in state Todo.
````

### OE 48

````text
OE 48  Comment on DES-348 (Bathroom Scale) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-348: the file is owed again once the UVs are redone; Claire has it.
````

### OE 49

````text
OE 49  Move DES-349 (Bathtub) to Todo in Linear (OE 2, OE 13)
Expected: DES-349 is in state Todo.
````

### OE 50

````text
OE 50  Comment on DES-349 (Bathtub) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-349: the file is owed again once the UVs are redone; Claire has it.
````

### OE 51

````text
OE 51  Move DES-350 (Cabinet Sink) to Todo in Linear (OE 2, OE 13)
Expected: DES-350 is in state Todo.
````

### OE 52

````text
OE 52  Comment on DES-350 (Cabinet Sink) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-350: the file is owed again once the UVs are redone; Claire has it.
````

### OE 53

````text
OE 53  Move DES-351 (Flip Flops) to Todo in Linear (OE 2, OE 13)
Expected: DES-351 is in state Todo.
````

### OE 54

````text
OE 54  Comment on DES-351 (Flip Flops) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-351: the file is owed again once the UVs are redone; Claire has it.
````

### OE 55

````text
OE 55  Move DES-352 (Iron) to Todo in Linear (OE 2, OE 13)
Expected: DES-352 is in state Todo.
````

### OE 56

````text
OE 56  Comment on DES-352 (Iron) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-352: the file is owed again once the UVs are redone; Claire has it.
````

### OE 57

````text
OE 57  Move DES-353 (Ironing Board) to Todo in Linear (OE 2, OE 13)
Expected: DES-353 is in state Todo.
````

### OE 58

````text
OE 58  Comment on DES-353 (Ironing Board) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-353: the file is owed again once the UVs are redone; Claire has it.
````

### OE 59

````text
OE 59  Move DES-354 (Plunger) to Todo in Linear (OE 2, OE 13)
Expected: DES-354 is in state Todo.
````

### OE 60

````text
OE 60  Comment on DES-354 (Plunger) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-354: the file is owed again once the UVs are redone; Claire has it.
````

### OE 61

````text
OE 61  Move DES-355 (Slippers) to Todo in Linear (OE 2, OE 13)
Expected: DES-355 is in state Todo.
````

### OE 62

````text
OE 62  Comment on DES-355 (Slippers) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-355: the file is owed again once the UVs are redone; Claire has it.
````

### OE 63

````text
OE 63  Move DES-356 (Toilet) to Todo in Linear (OE 2, OE 13)
Expected: DES-356 is in state Todo.
````

### OE 64

````text
OE 64  Comment on DES-356 (Toilet) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-356: the file is owed again once the UVs are redone; Claire has it.
````

### OE 65

````text
OE 65  Move DES-357 (Toilet Paper) to Todo in Linear (OE 2, OE 13)
Expected: DES-357 is in state Todo.
````

### OE 66

````text
OE 66  Comment on DES-357 (Toilet Paper) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-357: the file is owed again once the UVs are redone; Claire has it.
````

### OE 67

````text
OE 67  Move DES-358 (Wash Basin) to Todo in Linear (OE 2, OE 13)
Expected: DES-358 is in state Todo.
````

### OE 68

````text
OE 68  Comment on DES-358 (Wash Basin) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-358: the file is owed again once the UVs are redone; Claire has it.
````

### OE 69

````text
OE 69  Move DES-359 (Washing Machine) to Todo in Linear (OE 2, OE 13)
Expected: DES-359 is in state Todo.
````

### OE 70

````text
OE 70  Comment on DES-359 (Washing Machine) in Linear what is owed and who has it (OE 2, OE 13)
Expected: A comment by Julia on DES-359: the file is owed again once the UVs are redone; Claire has it.
````

### OE 71

````text
OE 71  Move DES-360 (Rubber Ducky) to Todo in Linear (OE 2, OE 5)
Expected: DES-360 is in state Todo.
````

### OE 72

````text
OE 72  Comment on DES-360 (Rubber Ducky) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-360: the FBX from Claire is owed; Claire has it.
````

### OE 73

````text
OE 73  Move DES-361 (Coffee Machine) to Todo in Linear (OE 2, OE 12)
Expected: DES-361 is in state Todo.
````

### OE 74

````text
OE 74  Comment on DES-361 (Coffee Machine) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-361: a binary FBX export is owed; Brian has it.
````

### OE 75

````text
OE 75  Move DES-362 (Cooler) to Todo in Linear (OE 2, OE 12)
Expected: DES-362 is in state Todo.
````

### OE 76

````text
OE 76  Comment on DES-362 (Cooler) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-362: a binary FBX export is owed; Brian has it.
````

### OE 77

````text
OE 77  Move DES-363 (Ice Cream Machine) to Todo in Linear (OE 2, OE 12)
Expected: DES-363 is in state Todo.
````

### OE 78

````text
OE 78  Comment on DES-363 (Ice Cream Machine) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-363: a binary FBX export is owed; Brian has it.
````

### OE 79

````text
OE 79  Move DES-364 (Kitchen Mixer) to Todo in Linear (OE 2, OE 12)
Expected: DES-364 is in state Todo.
````

### OE 80

````text
OE 80  Comment on DES-364 (Kitchen Mixer) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-364: a binary FBX export is owed; Brian has it.
````

### OE 81

````text
OE 81  Move DES-365 (Microwave) to Todo in Linear (OE 2, OE 12)
Expected: DES-365 is in state Todo.
````

### OE 82

````text
OE 82  Comment on DES-365 (Microwave) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-365: a binary FBX export is owed; Brian has it.
````

### OE 83

````text
OE 83  Move DES-366 (Oven) to Todo in Linear (OE 2, OE 12)
Expected: DES-366 is in state Todo.
````

### OE 84

````text
OE 84  Comment on DES-366 (Oven) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-366: a binary FBX export is owed; Brian has it.
````

### OE 85

````text
OE 85  Move DES-367 (Refrigerator) to Todo in Linear (OE 2, OE 12)
Expected: DES-367 is in state Todo.
````

### OE 86

````text
OE 86  Comment on DES-367 (Refrigerator) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-367: a binary FBX export is owed; Brian has it.
````

### OE 87

````text
OE 87  Move DES-368 (Stove) to Todo in Linear (OE 2, OE 12)
Expected: DES-368 is in state Todo.
````

### OE 88

````text
OE 88  Comment on DES-368 (Stove) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-368: a binary FBX export is owed; Brian has it.
````

### OE 89

````text
OE 89  Move DES-369 (Toaster) to Todo in Linear (OE 2, OE 12)
Expected: DES-369 is in state Todo.
````

### OE 90

````text
OE 90  Comment on DES-369 (Toaster) in Linear what is owed and who has it (OE 2, OE 12)
Expected: A comment by Julia on DES-369: a binary FBX export is owed; Brian has it.
````

### OE 91

````text
OE 91  Move DES-377 (Small Kettle) to Todo in Linear (OE 2, OE 5)
Expected: DES-377 is in state Todo.
````

### OE 92

````text
OE 92  Comment on DES-377 (Small Kettle) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-377: the export is owed; Brian has it.
````

### OE 93

````text
OE 93  Move DES-378 (Tall Kettle) to Todo in Linear (OE 2, OE 5)
Expected: DES-378 is in state Todo.
````

### OE 94

````text
OE 94  Comment on DES-378 (Tall Kettle) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-378: the export is owed; Brian has it.
````

### OE 95

````text
OE 95  Move DES-379 (Acoustic Guitar) to Todo in Linear (OE 2, OE 14)
Expected: DES-379 is in state Todo.
````

### OE 96

````text
OE 96  Comment on DES-379 (Acoustic Guitar) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-379: the file is owed back in the outgoing folder; Brian has it.
````

### OE 97

````text
OE 97  Move DES-380 (Cello) to Todo in Linear (OE 2, OE 14)
Expected: DES-380 is in state Todo.
````

### OE 98

````text
OE 98  Comment on DES-380 (Cello) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-380: the file is owed back in the outgoing folder; Brian has it.
````

### OE 99

````text
OE 99  Move DES-381 (Cymbals) to Todo in Linear (OE 2, OE 14)
Expected: DES-381 is in state Todo.
````

### OE 100

````text
OE 100  Comment on DES-381 (Cymbals) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-381: the file is owed back in the outgoing folder; Brian has it.
````

### OE 101

````text
OE 101  Move DES-382 (Electric Guitar) to Todo in Linear (OE 2, OE 14)
Expected: DES-382 is in state Todo.
````

### OE 102

````text
OE 102  Comment on DES-382 (Electric Guitar) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-382: the file is owed back in the outgoing folder; Brian has it.
````

### OE 103

````text
OE 103  Move DES-383 (Harp) to Todo in Linear (OE 2, OE 14)
Expected: DES-383 is in state Todo.
````

### OE 104

````text
OE 104  Comment on DES-383 (Harp) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-383: the file is owed back in the outgoing folder; Brian has it.
````

### OE 105

````text
OE 105  Move DES-384 (Tambourine) to Todo in Linear (OE 2, OE 14)
Expected: DES-384 is in state Todo.
````

### OE 106

````text
OE 106  Comment on DES-384 (Tambourine) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-384: the file is owed back in the outgoing folder; Brian has it.
````

### OE 107

````text
OE 107  Move DES-385 (Trumpet) to Todo in Linear (OE 2, OE 14)
Expected: DES-385 is in state Todo.
````

### OE 108

````text
OE 108  Comment on DES-385 (Trumpet) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-385: the file is owed back in the outgoing folder; Brian has it.
````

### OE 109

````text
OE 109  Move DES-386 (Xylophone) to Todo in Linear (OE 2, OE 14)
Expected: DES-386 is in state Todo.
````

### OE 110

````text
OE 110  Comment on DES-386 (Xylophone) in Linear what is owed and who has it (OE 2, OE 14)
Expected: A comment by Julia on DES-386: the file is owed back in the outgoing folder; Brian has it.
````

### OE 111

````text
OE 111  Move DES-388 (Grand Piano) to Todo in Linear (OE 2, OE 5)
Expected: DES-388 is in state Todo.
````

### OE 112

````text
OE 112  Comment on DES-388 (Grand Piano) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-388: the FBX from Claire is owed; Claire has it.
````

### OE 113

````text
OE 113  Move DES-396 (Wheelbarrow) to Todo in Linear (OE 2, OE 5)
Expected: DES-396 is in state Todo.
````

### OE 114

````text
OE 114  Comment on DES-396 (Wheelbarrow) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-396: the FBX from Claire is owed; Claire has it.
````

### OE 115

````text
OE 115  Move DES-397 (Wooden Crate) to Todo in Linear (OE 2, OE 5)
Expected: DES-397 is in state Todo.
````

### OE 116

````text
OE 116  Comment on DES-397 (Wooden Crate) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-397: the export is owed; Brian has it.
````

### OE 117

````text
OE 117  Move DES-402 (Rocket sound) to Todo in Linear (OE 2, OE 15)
Expected: DES-402 is in state Todo.
````

### OE 118

````text
OE 118  Comment on DES-402 (Rocket sound) in Linear what is owed and who has it (OE 2, OE 15)
Expected: A comment by Julia on DES-402: our own version of the sound is owed; Calvin has it.
````

### OE 119

````text
OE 119  Move DES-403 (Explosion sound) to Todo in Linear (OE 2, OE 15)
Expected: DES-403 is in state Todo.
````

### OE 120

````text
OE 120  Comment on DES-403 (Explosion sound) in Linear what is owed and who has it (OE 2, OE 15)
Expected: A comment by Julia on DES-403: our own version of the sound is owed; Calvin has it.
````

### OE 121

````text
OE 121  Move DES-406 (Background music) to Todo in Linear (OE 2, OE 5)
Expected: DES-406 is in state Todo.
````

### OE 122

````text
OE 122  Comment on DES-406 (Background music) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-406: the loop cut from the ad track is owed; Calvin has it.
````

### OE 123

````text
OE 123  Move DES-407 (Item visuals) to Todo in Linear (OE 2, OE 5)
Expected: DES-407 is in state Todo.
````

### OE 124

````text
OE 124  Comment on DES-407 (Item visuals) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-407: the PNG export from Figma is owed; Brian has it.
````

### OE 125

````text
OE 125  Move DES-408 (UI elements) to Todo in Linear (OE 2, OE 5)
Expected: DES-408 is in state Todo.
````

### OE 126

````text
OE 126  Comment on DES-408 (UI elements) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-408: the PNG export from Figma is owed; Brian has it.
````

### OE 127

````text
OE 127  Move DES-409 (Fonts) to Todo in Linear (OE 2, OE 5)
Expected: DES-409 is in state Todo.
````

### OE 128

````text
OE 128  Comment on DES-409 (Fonts) in Linear what is owed and who has it (OE 2, OE 5)
Expected: A comment by Julia on DES-409: the .ttf files are owed; Martin has them.
````

### OE 129

````text
OE 129  Give Frederick the count for each state in Slack, in the direct messages where he asked (OE 1, OE 22)
Expected: A message from Julia in DM D05SD5QLG94: Delivered 8, Ready 39, Owed 49.
````

### OE 130

````text
OE 130  Post both links in the PlayableX channel in Slack once both files are written (OE 1, OE 6, OE 20, OE 21, OE 22)
Expected: A message from Julia in C08H78VJG80 with the link of the brief (OE 20) and the link of the hand-off list (OE 21).
````


In scope this round: OE 10, OE 11, OE 14, OE 20, OE 23, OE 24, OE 25, OE 26, OE 130. The others are unchanged since an earlier round. Check the in-scope items; report a finding on another item only when it also involves an in-scope item (a pair, a group, or coverage of the whole set).

## Platform pass text (verbatim from the local Evals/ copy)

### Evals/references/rules/deep_recheck.md:61-67 (sha256 218dca42c269)

**Pass inputs.** Each pass gets the saved task inputs (`Evals/task_inputs/`
except `reports/`), the universe exports through `Evals/tools/hg_search.py` and
`Evals/SEARCH.md`, `Evals/references/persona/`, `common_errors.md`, and this
file. It is told its pass ID. Pass O3 is also not given `08_Oracle_Events.md` or any OE text. It does not open `Evals/task_inputs/reports/`
(including `drafts/`) or any earlier report, chat summary or record. It never
executes SQL. It is not given the main session's findings, scores or verdict,
or another pass's findings.

### Evals/references/rules/deep_recheck.md:69-88 (sha256 d79ba0d0bd9c)

**Known platform defects.** These are not contributor defects. A pass that
finds one reports it with the tag `PLATFORM:<id>`. The main session records it
in the report and never scores it against the task:

- `FD-2880`: the GitHub export's `commits` lists are a subset. A commit that
  is in git history or `commit_map` but missing from `commits` is an export
  gap, not a coherence or accuracy defect.
- `FD-3785`: the synthetic Snowflake rollups (DAILY_ACTIVE_USERS retention
  columns, USER_COHORT_RETENTION immature cells) disagree with their own
  definitions, and `analytics.game_events` is not in the injection database.
  A finding that rests only on these cells is platform. A prompt that makes
  the answer depend on them still fails UGT, because the agent cannot get one
  answer; the fix is to steer the prompt to a source that is consistent.
- Slack paste artifacts in saved SQL or text: markdown auto-link wrappers,
  doubled `""` from a CSV paste, missing `$$` and stripped `*`. Report the
  file as unreadable as sent; do not score the task content on them.
- Anonymized tokens such as `[PERSON_NAME_0854]` are the source string. A row
  or answer that uses the token as shown is correct; the real name is correct
  only when a persona-visible record maps the token to it. Do not score a
  token-for-name difference as a factual or accuracy defect.

### Evals/references/rules/deep_recheck.md:90-96 (sha256 4a6e18950546)

**Pass work.** A pass checks only its own topic, on every sentence, event or
row, not a sample. It returns findings in this format and nothing else:

`DR# | pass | checklist section | quoted prompt sentence, OE text (OE#) or rubric row (R#) | record path, id and quoted value | Eval dimension or issue type | proposed score or severity`

A finding without a quote is dropped. A pass with no findings returns `none`
and the number of sentences, events or rows it checked.

### Evals/references/rules/deep_recheck.md:287-289 (sha256 4a49e5d188fa)

Each OE pass reads the prompt to know what the path must do. It follows Eval 2
route independence (§3.1): a step that reaches a requirement by another valid
route covers it.

### Evals/references/rules/deep_recheck.md:312-320 (sha256 7f67c1cbec08)

### O2 · Completeness

Split the prompt sentence by sentence into every requirement: each fact the
answer needs, each write with its target and audience, each dependency, and any
recovery or wait for an injected error. Each needs an event that covers it. A
fact in any `Expected:` line with no event that obtains it is a missing step. An
event too vague to follow ("identify the relevant current and stale records")
names no record, date or value, and is missing that step. A non-action or
final-response event is NON-FAIL 3, not a missing step.

## Local differences from the platform

- The platform text asks for pipe-delimited lines (or `none` with a count). Return the same content as the JSON object under Required output instead.
- Where it names the saved task inputs, read the copies listed above; where it names the Evals search helpers, use the commands under Universe.
- Known platform defects: severity "PLATFORM", issue_type "PLATFORM:<id>"; they are not scored.

## Platform rules not in the local Evals/ copy

The platform has applied these rules in its own reports; the local pass text above does not have them. Apply them as well. `verbatim` means the excerpt quotes the platform's own rule; `reconstructed` means the rule is inferred from how the platform applied it, so use judgement. The excerpts come from other tasks' reports: they show how a rule is applied and say nothing about this task.

- `decision-forks-2.8` (reconstructed; local rule: absent): "Decision forks (2.8): `hg_decision_forks.py` found no hedge wording; no OE leaves a boundary item unsettled (the returned ***8605 wire, Oleg's returned wire, the Leapblock wire with no Processed notice and the JPMorgan own-account transfer are each settled by a dated record that names them)."
- `hg_decision_forks.py` (reconstructed; local rule: absent): "- Decision forks (2.8): `hg_decision_forks.py` finds no hedge wording."
- `tool_outputs.md@oe` (verbatim; local rule: absent): "| OE 30, 32, 33 | all | VERIFIED | Cataloged create / share tools; a created spreadsheet has a link (tool_outputs.md `gdrive.web_view_link`) |"

## Required output

Return one JSON object and nothing else. It carries the same content as the line format named in the platform text above, one finding per line you would have written:

```json
{
 "pass": "O2",
 "artifact_sha256": "6200845d5432d5e5dcce5d475acb7af380b15295126626f286dc487b1f623887",
 "checked": "<how many items you checked>",
 "findings": [
  {
   "event": "<id>",
   "issue_type": "<type>",
   "severity": "<severity>",
   "quote": "<exact words copied from the cited item>",
   "evidence": "<record path, id and quoted value, or the quoted rule>",
   "fix": "<plain fix>"
  }
 ],
 "verdict": "PASS | NON-FAIL | FAIL"
}
```

- `artifact_sha256`: exactly `6200845d5432d5e5dcce5d475acb7af380b15295126626f286dc487b1f623887` (the bytes listed under the artifact).
- `event`: event ids "OE 1".."OE 130" as listed; use "span" with a prompt sentence id S1..S3 for a requirement that has no event.
- `quote`: the exact words of the cited item (a sentence, event or row). A finding without a quote is dropped.
- `issue_type`: one of: accuracy, after_clock, completeness, deferred_write, dependency_cycle, final_response_event, forbidden_write, format, invented_trap, missing_dependency, missing_recovery, missing_step, missing_write, non_action_event, persona_inaccessible, unobservable_precision, vague_step, wrong_expected_data, wrong_identifier, wrong_parameter, wrong_qualifier, wrong_service, wrong_tool.
- `severity`: "Major" for a fail-level finding (score 1-2, or 2 on /oe), "Minor" for a non-fail one (3-4, or 3 on /oe); "UNSURE" for a suspicion you cannot support with a record; "PLATFORM" for a known platform defect (issue_type "PLATFORM:<id>").
- `evidence`: the record path, id and quoted value behind the finding.
- `fix`: a plain description of the fix (it may be empty for an inventory line).
- `checked`: the number of sentences, events or rows you checked; required when `findings` is empty.
- `verdict`: PASS when you have no finding, FAIL when any finding is fail-level, else NON-FAIL.
