#!/usr/bin/env python3
"""Planned wording of the seeded records for design D2 (scenario stage). Design content, not a prompt: the final text is
written at /create-injection in each author's own register (dossier 1.C). The manifest's delegation quotes are exact
substrings of ASK and NOTES; the gate checks them."""

# Frederick's DM to Julia, Tue 30 Sep 18:21 UTC (their DM is English; his last base message there is 18 Sep).
ASK = ("Julia, PlayableX are holding Nov 3 for us and I don't want a third slip on our side. While it's parked, can you do "
       "for this one what you did for the Dominoes playable: write the brief they build from, and tell me where the item "
       "pack actually stands. Brian's pack list is where it starts. Robert's picks for the board and the zombies stand "
       "unless he's changed them since. My hand-off notes say what goes in the brief, what counts as ready, what to do "
       "with the tickets and who gets the files. Write it for the game as it is today; if the core changes we redo that part with them in "
       "November. Brief as a doc and the hand-off list as a sheet, both in your Drive. Then give me the count for each state here, "
       "and post both links in the PlayableX channel so they know what's still coming from us.")

# Frederick's Google Doc, created and last edited Tue 30 Sep (16:25 to 16:58 UTC, before his 17:30 call), shared with Julia, Brian and Robert.
NOTES = ("ZM3D playable: hand-off notes\n\n"
         "The brief. One doc PlayableX can build from: which scenario we picked and what it is for, the eight items on the "
         "board and that every other board item on the list is an extra they can swap in, the four zombies and the one animation, "
         "how a level is won and lost and how many slots the tray has, what they can use for sound and when the music may start, and the start date. How "
         "the level plays is on the design page; your deck of the reference level has what we built for them. What they "
         "told us about formats still holds, and so does their rule from last time about when the music may start.\n\n"
         "The hand-off list. One row per line of Brian's pack list, with these columns: Line, Category, Board set, State, "
         "What's owed, Who has it, Ticket. Line, Category and Ticket are as on his list. Board set is Default for the eight on the board and Extra for every other board "
         "item; leave it empty for anything that isn't a board item.\n\n"
         "State is one of three words, nothing else. Delivered: PlayableX has the current file and can use it. Ready: "
         "exported in a format they take and sitting in the outgoing folder, it opens, it is the current version and nobody is changing it. Owed: anything "
         "else. For an Owed line say what is owed, and who has it, meaning whoever has to do the next thing.\n\n"
         "Brian's note on each ticket says what he did with the line. Take it as it stands unless something later says "
         "otherwise, and go by how things stand today, not the day he wrote it: if someone who knows the file or the art "
         "has said something since, that counts. If the art changed after a file went out or was exported (a fix, a "
         "retexture, new colour versions), it goes again, and it sits with whoever the file came from.\n\n"
         "Sound: we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we "
         "have our own version.\n\n"
         "Tickets live under Brian's pack ticket, one per line. An Owed line's ticket goes to Todo with a comment saying "
         "what is owed and who has it. Leave the Delivered and "
         "Ready ones as they are.\n\n"
         "Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address, which "
         "is in Contacts.\n")

# Brian's pack ticket DES-313, created Thu 25 Sep 07:05 UTC (description).
PACK_TICKET_TITLE = "Playable pack for PlayableX"
PACK_TICKET_DESC = ("Frederick wants every line of the playable pack tracked after the start slipped. One sub-ticket per line of "
                    "the pack list, kept in Design so it stays off the ZM3D board. I leave a note on each one saying what I did "
                    "with it. A line's ticket closes when PlayableX have the file.")

# Robert, #zombie-design, Thu 25 Sep 18:12 UTC (root post): the vendor's "8-item set".
PICKS = ("For the playable board, the 8: Grenade, Couch and Plushie Chick from the reference level, plus Shuriken, Cute Axe, "
         "Gift Box, Cactus Plant and Dynamite. Everything else <@EMPLOYEE_0026_SLACK_ID> sends them is extras they can swap in.")

# Robert, #zombie-design, Mon 29 Sep 17:31 UTC (root post): the answer to the vendor's question of that morning.
ZPICKS = ("<@EMPLOYEE_0026_SLACK_ID> for PlayableX's question, in case we carry on with them: one animation, walk. The 4 zombies: Party Girl, "
          "Plumber, Magician, Football Player. All four are in the pack Marcus sent.")

# Robert, #zombie-art, Fri 26 Sep 21:41 UTC: reply under Julia's base post "Can we have arrow to go with the bow?".
C3_REPLY = ("Fun one. Let's have it in the 8 in place of the last one on my list, we've got enough things that go boom. As it is "
            "now, the arrow can be its own item later.")

# Marcus, #zombie-match3d, Fri 26 Sep 17:08 UTC (root post), a quarter of an hour after he handed over the zombie pack.
A1_POST = ("<@EMPLOYEE_0026_SLACK_ID> fyi the models you saved out of unity on thursday are the text kind, thats what the exporter "
           "does if you dont change it. they open fine in unity and in max so you wouldnt notice. the ones from "
           "<@EMPLOYEE_0009_SLACK_ID> are ok")

# Claire to Julia, their DM, Mon 29 Sep 12:15 UTC. Turkish, in her register (lower case, "kuzum", English nouns); no person is named.
A2_DM = ("kuzum bu arada banyo objelerinin uv'lerini baştan açıyorum, levellerde bi süre eski halleri görünür haberin olsun. "
         "cuma verdiğim banyo dosyaları da eski hali, bitince ticketlara yazarım")
A2_DM_GLOSS = ("by the way I am redoing the UVs of the bathroom objects from scratch, the old versions will show in the levels for a "
               "while, just so you know. the bathroom files I gave on Friday are the old state too, I will write on the tickets when it is done")

# Brian's own Google Doc, created Thu 25 Sep, last edited Tue 30 Sep 09:12 UTC (the morning after the pause was decided).
C4_LOG_TITLE = "Outgoing folder - what's in it"
C4_LOG = (C4_LOG_TITLE + "\n"
          "So I don't lose track of what I've put in there.\n"
          "Thu 25 Sep: the models saved out of the project, and the first files from Claire.\n"
          "Fri 26 Sep: more files from Claire. The music instruments went in as one zip. The sound files.\n"
          "Mon 29 Sep: another batch from Claire. She still has a few to send and a few are still mine to do.\n"
          "Tue 30 Sep: the zip with Friday's music instruments got cut off on upload, it won't unpack on my side, and those eight "
          "aren't in the folder any other way. I still have Claire's files, I'll put them back when we pick this up again.")

# Calvin's sheet "ZM3D sound sources" (created Fri 12 Sep after the copyright question, last edited Fri 26 Sep 20:10 UTC).
C2_SHEET_TITLE = "ZM3D sound sources"
C2_SHEET_GRID = [
    ["Cue", "Where it came from", "OK outside the game", "Replacement"],
    ["Matching sound", "made here", "yes", ""],
    ["Combo meter scale (endless mode)", "made here: pitched in Reaper from the sample Robert gave me", "yes", ""],
    ["Rocket sound", "Soundly library (Robert's seat)", "no", "not made yet, Calvin"],
    ["Explosion sound", "Universal Sound FX pack (Unity Asset Store, Robert's)", "no", "not made yet, Calvin"],
    ["Success sound", "made here", "yes", ""],
    ["Failure sound", "made here", "yes", ""],
    ["Background music", "new track for the ad, generated and edited here (not the in-game track)", "yes", ""],
    ["Laptop error, shutdown", "Windows system sounds", "no", "Robert is swapping them"],
]

# Julia's deck "ZM3D playable - reference level" (Tue 23 Sep 19:55 UTC), the level she built that afternoon.
DECK_SLIDES = [
    ("ZM3D playable - reference level", "Built 23 Sep on the playable levels branch. Brian recorded it for PlayableX."),
    ("Board", "Grenade (red, green), Couch, Couch and Pillow, Plushie Bunny, Plushie Chick."),
    ("Zombies", "A mix, nothing fixed yet."),
    ("Win and lose", "Win: every zombie on screen is eliminated. Lose: the zombies reach us and our HP runs out."),
]

# Frederick's calendar hold (created Tue 30 Sep 16:41 UTC, before the notes' last edit at 16:58).
HOLD_SUMMARY = "ZM3D playable kickoff with PlayableX"

# Contacts row (Frederick, 19 Sep).
CONTACT = {"first_name": "PlayableX", "last_name": "Intake", "job": "Project intake (playable ads)", "email": "intake@playablex.ai"}

# Leonard, comment on his Playable Kickoff card, Tue 30 Sep 20:05 UTC.
TRELLO_NOTE = "Parked until Nov 3, the new start PlayableX gave us after we asked for the pause. Julia is pulling the brief and the pack status together for Frederick in the meantime."
