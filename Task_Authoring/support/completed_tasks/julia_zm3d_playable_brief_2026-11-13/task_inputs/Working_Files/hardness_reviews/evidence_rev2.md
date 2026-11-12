# Scenario-stage hardness review evidence · julia_zm3d_playable_brief · rev2 (design D3)

Authoring-session review of the six selected mechanisms against the draft manifest, the gradable surface and the planned record texts. Planned records are not SQL yet: their readability and natural retrieval are deferred to `/create-injection` (`persona_view.py check-sql`, the cold-solver rehearsal). Base records were read through `tools/hg.py` and checked with `persona_view.py can-see` (Working_Files/plan/out/reach_table.md).

## Planned hub texts (Working_Files/plan/planned_texts.py)

Ask:

> Julia, PlayableX are holding Nov 3 for us and I don't want a third slip on our side. While it's parked, can you do for this one what you did for the Dominoes playable: write the brief they build from, and tell me where the item pack actually stands. Brian's pack list is where it starts. Robert's picks for the board and the zombies stand unless he's changed them since. My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files. Write it for the game as it is today; if the core changes we redo that part with them in November. Brief as a doc and the hand-off list as a sheet, both in your Drive. Then give me the count for each state here, and post both links in the PlayableX channel so they know what's still coming from us.

Notes:

> ZM3D playable: hand-off notes
>
> The brief. One doc PlayableX can build from: which scenario we picked and what it is for, the eight items on the board and that every other board item on the list is an extra they can swap in, the four zombies and the one animation, how a level is won and lost and how many slots the tray has, what they can use for sound and when the music may start, and the start date. How the level plays is on the design page; your deck of the reference level has what we built for them. What they told us about formats still holds, and so does their rule from last time about when the music may start.
>
> The hand-off list. One row per line of Brian's pack list, with these columns: Line, Category, Board set, State, What's owed, Who has it, Ticket. Line, Category and Ticket are as on his list. Board set is Default for the eight on the board and Extra for every other board item; leave it empty for anything that isn't a board item.
>
> State is one of three words, nothing else. Delivered: PlayableX has the current file and can use it. Ready: exported in a format they take and sitting in the outgoing folder, it opens, it is the current version and nobody is changing it. Owed: anything else. For an Owed line say what is owed, and who has it, meaning whoever has to do the next thing.
>
> Brian's note on each ticket says what he did with the line. Take it as it stands unless something later says otherwise, and go by how things stand today, not the day he wrote it: if someone who knows the file or the art has said something since, that counts. If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again, and it sits with whoever the file came from.
>
> Sound: we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we have our own version.
>
> Tickets live under Brian's pack ticket, one per line. An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. Leave the Delivered and Ready ones as they are.
>
> Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address, which is in Contacts.

## EXPORT

- First plausible answer: The twelve lines Brian saved out of the project on Thu 25 Sep (Alarm Clock, Record Player, Retro TV, Coffee Machine, Cooler, Ice Cream Machine, Kitchen Mixer, Microwave, Oven, Refrigerator, Stove, Toaster) read as Ready: each ticket (DES-318, DES-367 and ten more) says FBX saved out of the project, opens, looks right, in the outgoing folder.
- Deciding evidence (`C0880U9751A/1758906517.912099`): Marcus Bennett's root post in #zombie-match3d (C0880U9751A/1758906517.912099, 2025-09-26 17:08 UTC) says the models Brian got out of Unity on Thursday are the text kind (the setting was wrong that day), which open fine in Unity and Max; Claire's files are fine. The vendor takes .fbx in binary format only (C08H78VJG80/1758022459.227279, C08H78VJG80/1758283671.878269; Frederick relayed it to Julia in D05SD5QLG94/1758220925.518329). By the notes' Ready test ('exported in a format they take') the twelve are Owed: export again as binary, Brian.
- Authority and chronology: Brian's ticket notes are of 25 Sep and say the file opens, which is true in Unity. Marcus built and tested the zombie pack on 26 Sep (base) and posts a quarter of an hour after handing it over. The notes say a later word from someone who knows the file counts over the ticket. Nothing after 26 Sep says the files were exported again.
- Fair discovery path: Julia is a member of #zombie-match3d and posted there six times that week (reach table YES). The post is a top-level message. The vendor's binary-only rule is on the hub path twice and in Julia's own DM with Frederick, and the twelve tickets say 'saved out of the project' while the others say 'FBX from Claire', so asking what kind of file the project writes is the natural check. The post holds no line name, no ticket key, none of the ask's words and none of the words of the note it corrects ('saved out of', 'export').
- Outcome change: before: Refrigerator: Ready; its ticket stays In Progress · after: Refrigerator: Owed (ASCII file, export again as binary), Brian; its ticket to Todo with a comment
- Outcome pair X1 / W4: left passes, right fails when the list marks Refrigerator Owed but the run skips the ticket follow-through, so the ticket stays In Progress; right passes, left fails when the run moves the ticket to Todo in a follow-through pass and leaves the sheet row, written earlier from the ticket note, at Ready.
- Slots linked on the surface: X1, X1b, X6, X16, A1, A2, W1, W2, W4, K1
- Kind: done-claim against a later check by a colleague, joined to the vendor's format rule (v2 trap 1)

## ARTHOLD

- First plausible answer: The twelve exported Bathroom lines (Bathroom Scale, Bathtub, Cabinet Sink, Flip Flops, Iron, Ironing Board, Plunger, Slippers, Toilet, Toilet Paper, Wash Basin, Washing Machine) read as Ready: each ticket says FBX from Claire, Fri 26 Sep, opens, looks right.
- Deciding evidence (`D05GU6L0XFH/1759178332.042459`): Robert's note to Julia in their DM (D05GU6L0XFH/1759178332.042459, 2025-09-29 20:38 UTC) says Claire (tagged) is redoing the UVs on the bathroom objects from scratch and that the bathroom files she gave Brian (tagged) on Friday are the old version. The notes' Ready test ('the current version and nobody is changing it') makes the twelve Owed; a changed file 'sits with whoever the file came from': Claire.
- Authority and chronology: Brian's notes are of 26 Sep; Robert, who follows the art (his colourised items in #zombie-art, his new colour versions in #zombie-design), writes three days later. No later record says the UVs are finished.
- Fair discovery path: The DM is Julia's own conversation with Robert (reach table YES), where they talk about the game every day. It is a top-level message between his other messages of 29 Sep. It names the game's category, which is a column of the pack list, and no line; Claire and Brian are tagged, not named.
- Outcome change: before: Bathtub: Ready; who has it: nobody · after: Bathtub: Owed (art being redone), Claire; its ticket to Todo with a comment
- Outcome pair X2 / X11: left passes, right fails when the list marks Bathtub Owed and leaves 'who has it' empty or names Robert or Brian; right passes, left fails when the run notes the redo against the bathroom lines while the State cells, filled earlier from the ticket notes, stay Ready.
- Slots linked on the surface: X2, X2b, X7, X11, X11b, A1, A2, W1, W2, K2
- Kind: a later statement by someone who knows the art, in another person's DM with the persona (v2 trap 2)

## REVISED

- First plausible answer: Cactus Plant, Chainsaw and Cone read as Owed once Robert's post is read: their tickets say FBX from Claire, 25 Sep; Robert shows new colour versions of the cactus, the chainsaw and the cones on 29 Sep (C090N54TG79/1759189466.554739), and the notes say a file whose art changed 'goes again'.
- Deciding evidence (`f_faf4d7c167d14a1127dcc3`): Brian Foster's own log of the outgoing folder (f_faf4d7c167d14a1127dcc3, last edited 2025-09-30 09:12 UTC) says Claire sent the three recoloured models again, that he opened them, that they look right and that they replace Thursday's; which three is in Robert's post (cactus, chainsaw, cones). The file went again, is in the folder, opens and is current: by the notes' Ready test the three are Ready.
- Authority and chronology: Ticket notes 25 Sep; base pull request match3d#462 merged 25 Sep 23:15 UTC; Robert's post 29 Sep 23:44 UTC; Brian's log entry Tue 30 Sep (last edit 09:12 UTC). The latest record governs; nothing after it changes the three.
- Fair discovery path: The log is shared with Julia (planned sharing; proven on the SQL at injection). The notes make 'sitting in the outgoing folder' part of Ready and every exported ticket note ends with that folder, so looking for the folder in Drive is the natural check; a search for it returns the log, which carries no word of the ask and no line name except the three items.
- Outcome change: before: Cactus Plant: Owed (the file again), Claire; its ticket to Todo with a comment · after: Cactus Plant: Ready; its ticket left as it is
- Outcome pair X3 / X3b: left passes, right fails when the list marks Cactus Plant Ready while a ticket comment still asks for the file again; right passes, left fails when the list keeps Cactus Plant Owed from Robert's post while the brief says the eight are in hand.
- Slots linked on the surface: X3, X3b, X8, A1, A2, W1, W2
- Kind: a completion note elsewhere that undoes a correction met first (v2 move A25)

## AUDIO

- First plausible answer: All five exported sound cues read as Ready: each sound ticket says exported .wav from the project, plays.
- Deciding evidence (`f_b2387e31d46d3a7b3fa2a9`): Calvin Price's sound sources sheet (f_b2387e31d46d3a7b3fa2a9) lists the rocket sound as from a library seat and the explosion sound as from a bought pack, both 'no' under 'OK outside the game', with 'not made yet, Calvin' under 'Replacement'. The notes: 'we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we have our own version'. The two are Owed: our own version, Calvin. The brief's sound section holds them back.
- Authority and chronology: The rule is Frederick's (the notes); the source column is Calvin's, who made or collected the cues. The tickets state the file type only, so nothing contradicts the sheet. Base agrees on the general picture: Robert uses a Soundly subscription and bought packs, and two sounds were already to be swapped for copyright.
- Fair discovery path: The sheet is shared with Julia (planned sharing; proven on the SQL at injection). A Drive search for sound, or a look at Calvin's files, returns it; its rows are grid cells, which gsheets_values_get returns.
- Outcome change: before: Rocket sound: Ready; the brief lists it among the cues PlayableX can use · after: Rocket sound: Owed (not ours to pass on), Calvin; the brief's sound section names it as held back
- Outcome pair X5 / B6: left passes, right fails when the list marks Rocket sound Owed and the brief's sound section is written from the ticket list without the two cues held back; right passes, left fails when the brief holds the two cues back after the sheet is read while the list row written earlier keeps Ready.
- Slots linked on the surface: X5, X5b, X10, X12, A1, A2, W1, W2, K5, B6
- Kind: a rule in the data applied to a second carrier (v2 trap 5)

## PICKS

- First plausible answer: The eight are Robert's 25 Sep post (C090N54TG79/1758823946.262829), with the dynamite as the last of them.
- Deciding evidence (`C08R8CHB0QL/1758922879.243189`): Robert's reply under Julia's bow post in #zombie-art (C08R8CHB0QL/1758922879.243189, 2025-09-26 21:41 UTC, parent C08R8CHB0QL/1758904025.123869) puts it, the bow of the parent post, in the eight in place of the last item on his list, as it is now. The last item of his 25 Sep list is the dynamite. The ask keeps his latest word ('unless he's changed them since').
- Authority and chronology: Same person, a day later. No later record re-lists the eight; Julia's deck (23 Sep) is the reference level, older than both.
- Fair discovery path: The parent is Julia's own post in a channel she is a member of (reach table YES for the root). slack_read_thread on it returns the reply. The reply names no item, so a keyword search on an item name does not return it; the bow comes from the parent and the dynamite from the order of Robert's own list.
- Outcome change: before: Bow: Extra; Dynamite: Default; the brief lists the dynamite among the eight · after: Bow: Default; Dynamite: Extra; the brief lists the bow among the eight
- Outcome pair X13 / B1: left passes, right fails when the list has Bow as Default while the brief, written from the 25 Sep post, still lists the dynamite; right passes, left fails when the brief lists the bow among the eight while the list's Board set column was filled from the 25 Sep post.
- Slots linked on the surface: X13, X14, B1
- Kind: a later reply under an unrelated parent (v2 trap 2)

## ZIP

- First plausible answer: The eight instruments in Friday's zip (Acoustic Guitar, Cello, Cymbals, Electric Guitar, Harp, Tambourine, Trumpet, Xylophone) read as Ready: each ticket says FBX from Claire, Fri 26 Sep, opens, looks right, zipped with the other instruments, in the outgoing folder.
- Deciding evidence (`f_faf4d7c167d14a1127dcc3`): Brian Foster's own log of the outgoing folder (f_faf4d7c167d14a1127dcc3, a Google Doc, last edited 2025-09-30 09:12 UTC) says the zip with Friday's music instruments got cut off on upload and will not unpack, that the eight are not in the folder any other way, and that he will put Claire's files back. By the notes' Ready test ('sitting in the outgoing folder, it opens') the eight are Owed: put the files back, Brian.
- Authority and chronology: Brian's own later statement about his own zip; the ticket notes are of 26 Sep, the log line of 30 Sep. Nothing later says it was redone.
- Fair discovery path: The log is shared with Julia (planned sharing; proven on the SQL). The notes make 'sitting in the outgoing folder' part of Ready and every ticket note ends with that folder, so looking for the folder in Drive is the natural check; a search for it returns the log. Its title and text hold none of the ask's nouns and no instrument's name; D3 also takes the word 'sound' out of it, so the search made for the sound cues no longer lists it.
- Outcome change: before: Cello: Ready; its ticket stays In Progress · after: Cello: Owed (its zip will not unpack), Brian; its ticket to Todo with a comment
- Outcome pair X4 / K4: left passes, right fails when the list marks Cello Owed and no ticket comment says the zip has to be redone; right passes, left fails when a ticket comment says the zip has to be redone while the list row keeps Ready.
- Slots linked on the surface: X4, X4b, X9, X17, A1, A2, W1, W2, K4
- Kind: a second record by the list's owner that contradicts his ticket notes (completion elsewhere)

## Independence

Five deciding records in five containers: #zombie-match3d (EXPORT), Julia's DM with Robert (ARTHOLD), Calvin's sheet (AUDIO), the thread under Julia's bow post (PICKS), and Brian's log of the outgoing folder, which decides two rules (ZIP: eight lines Owed; REVISED: three lines Ready). None quotes or links another, and the lines they decide are disjoint (12, 12, 2, the board set of two lines, 8 and 3). ZIP and REVISED are one carrier: a run that opens the log settles both, one that does not misses both; every other rule stays solvable without it.

## Natural retrieval on base (REVISED's first-read record)

```
$ persona_view.py search julia_lawson slack "colorized" --limit 12
SEARCH slack 'colorized' as julia_lawson  scope: Slack message text, attachment text/pretext/title/fallback, attached file titles (all shards)
visible hits=8 (showing 8)  hidden by ACL=0 in 0 containers  UNVERIFIED=0 in 0 containers
  {"id": "C0880U9751A/1737088923.253069", "channel": "zombie-match3d", "kind": "private", "date": "2025-01-17", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "Weapon colorized sample"}
  {"id": "C0880U9751A/1741936391.969339", "channel": "zombie-match3d", "kind": "private", "date": "2025-03-14", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "brown pieces itself, but the rings around the barrel can be colorized. We should also start checking the various themes we have,
  {"id": "C0880U9751A/1743787068.653039", "channel": "zombie-match3d", "kind": "private", "date": "2025-04-04", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "That can be colorized"}
  {"id": "C0880U9751A/1743832915.722879", "channel": "zombie-match3d", "kind": "private", "date": "2025-04-05", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "I think we desperately need a new fridge. One that can be colorized, and maybe a bit more rectangular. The current one is too muc
  {"id": "C0880U9751A/1744040685.996969", "channel": "zombie-match3d", "kind": "private", "date": "2025-04-07", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "ver works for us to get thicker set of utensils that can be colorized. Right now they are a bit too skinny"}
  {"id": "C08R8CHB0QL/1758298618.492459", "channel": "zombie-art", "kind": "public", "date": "2025-09-19", "user": "EMPLOYEE_0016_SLACK_ID", "reply": true, "snippet": "Trying to think if the handsaw, if colorized, will be distinct enough one vs. another"}
  {"id": "C08R8CHB0QL/1758752145.583769", "channel": "zombie-art", "kind": "public", "date": "2025-09-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "LOYEE_0009_SLACK_ID> Hey here is a quick win, can we make a colorized version of the cactus plant? Let's just have different pot colo
  {"id": "C08R8CHB0QL/1758754866.994649", "channel": "zombie-art", "kind": "public", "date": "2025-09-24", "user": "EMPLOYEE_0016_SLACK_ID", "reply": false, "snippet": "Let's also get a colorized versions of the cone:"}

$ hg.py search search github "Objects Revisions" --limit 5 --compact
scan_complete False matches 5
  Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /commits/335/message | 
  Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /commits/4442/message | 
  Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /commits/7625/message | 
  Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /pull_requests/2366/title | 
  Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/github/data.json /pull_requests/2392/title |
```
