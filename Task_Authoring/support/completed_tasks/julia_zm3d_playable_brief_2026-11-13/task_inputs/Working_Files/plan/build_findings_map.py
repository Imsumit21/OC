#!/usr/bin/env python3
"""Write plan/sweep_findings_map.json: every finding of the two reviewers' current files taken up by a fork, an open set
or a dismissal with its reason (coherence_sweep.py `sweep.findings`). The judgements are written here once, as entries
with the words that identify the finding; a finding no entry claims is printed and the script exits 1, so nothing is
taken up silently. Run after the reviewers wrote findings_<n>.json for the current SQL, then build_settlements.py and
build_sweep.py."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
sys.path.insert(0, str(HERE))
import design_model as M
S, B = M.SEED, M.BASE
REV = M.REV
def tk(n): return M.BY_NAME[n]["ticket"]
def note(n): return M.comment_id("note_" + n)
def tks(cls): return [l["ticket"] for l in M.members(cls)]
NOTES, LOG, SHEET, LIST = S["notes"]["id"], S["c4_log"]["id"], S["c2_sheet"]["id"] + "/0", S["tracker"]["id"]
ASK, PICKS, ZPICKS, REPLY, A1, A2 = (S[k]["id"] for k in ("ask", "picks", "zpicks", "c3_reply", "a1_post", "a2_dm"))
HOLD, TRELLO, PT = S["hold"]["id"], S["trello_note"]["id"], M.PACK_TICKET
LISTED = [l for l in M.LINES if l["on_list"]]
ALL = [l["ticket"] for l in LISTED]
BOARD = [l for l in LISTED if l["kind"] == "Board item"]
EXTRA = [l["ticket"] for l in BOARD if l["name"] not in M.DEFAULT_FINAL]
DEFAULT = [tk(n) for n in M.DEFAULT_FINAL]
OWED = [l["ticket"] for l in LISTED if l["state"] == "Owed"]
READY = [l["ticket"] for l in LISTED if l["state"] == "Ready"]
DELIVERED = [l["ticket"] for l in LISTED if l["state"] == "Delivered"]
WAIT_CLAIRE = [l["ticket"] for l in M.members("VIS") if "Waiting on the FBX from Claire" in l["note"]]
MINE = [l["ticket"] for l in M.members("VIS") if "ine to" in l["note"]]
C = M.COUNTS

def rd(reading, outcome): return {"reading": reading, "outcome": outcome}
def settled(ids): return {"record_ids": ids, "sql_revision": REV}

# ---------------------------------------------------------------- forks (any: words that identify the finding; all lower case)
FORKS = [
 # readings of the prompt itself (listed first so their words win over the record forks below)
 dict(id="F21", title="Which message is Frederick's playable message", any=["which message", "invitation", "pause post", "frederick's playable message"], material=False, status="settled_in_data",
      record_ids=[ASK, HOLD],
      reading_a=rd("his DM to Julia of 30 Sep, the only message of his that carries asks", "the job is the DM"),
      reading_b=rd("his kickoff invitation of the same day, or his 29 Sep post asking the vendor for the pause, which also mention the playable", "nothing to do, or a reply to an invitation"),
      reason="the prompt names the message by a noun phrase; two other records of his mention the playable",
      settled=settled([ASK]), how="only the DM asks for anything, and the prompt's third sentence (files in her Drive, links in the PlayableX channel) matches it word for word"),
 dict(id="F23", title="Sharing: is it part of what he asks", any=["sharing", "view-only share", "view only", "who gets the files"], material=False, status="settled_in_data",
      record_ids=[ASK, NOTES],
      reading_a=rd("the share is in scope: the notes say who gets both files", "both files shared view only with the hold's attendees and the vendor's intake address"),
      reading_b=rd("the message names the notes for three things and sharing is not one of them, so the share is not asked", "no share; the vendor cannot open the links"),
      reason="in the fourth round both reviewers noted that the share was reached only through the notes' last paragraph",
      settled=settled([ASK]), how="the message now says the notes cover 'what goes in the brief, what counts as ready, what to do with the tickets and who gets the files'"),
 dict(id="F24", title="Who acts: Julia or the assistant", any=["i need a hand", "who acts", "who does what", "acting as julia", "nothing for her to send", "assistant does"], material=False, status="settled_in_data",
      record_ids=[ASK],
      reading_a=rd("the assistant does all of it as Julia, including the DM reply and the channel post", "all six outputs are the assistant's"),
      reading_b=rd("the assistant prepares the files and Julia sends the messages", "no messages sent"),
      reason="the prompt has no 'I'll' statement; listed by the reviewers for completeness",
      settled=settled([ASK]), how="'do everything he's asking for in it, start to finish' leaves nothing for her; the message's requests include the reply and the post"),
 dict(id="F22", title="What 'everything he's asking for in it' takes in", any=["everything he's asking for", "full output list", "third sentence", "six outputs"], material=False, status="settled_in_data",
      record_ids=[ASK, NOTES],
      reading_a=rd("everything the message asks, including what it hands to the notes: the brief, the list, the ticket follow-through, the sharing, the count for each state, the two links", "six outputs"),
      reading_b=rd("only what the prompt's third sentence repeats: the files and the links", "two files and one post; no tickets, no counts, no share"),
      reason="the third sentence repeats two destinations and is silent on the rest",
      settled=settled([ASK, NOTES]), how="the message itself asks for the counts 'here' and makes the notes part of the job; the prompt says 'everything ... start to finish'"),
 dict(id="F25", title="Where inside her Drive the files go", any=["inside her drive", "sub-folder", "subfolder", "zombie art", "place inside", "should end up in my drive"], material=False, status="both_fair",
      record_ids=[ASK],
      reading_a=rd("the root of her Drive", "both files in the root"), reading_b=rd("a folder of hers", "both files in her one subfolder"),
      reason="the message says 'both in your Drive' and names no folder; either is in her Drive",
      both_fair={"figure_a": "her Drive root", "figure_b": "a folder she owns under it", "rubric_accepts_both": True},
      how="the rubric accepts any location owned by her (brief §4b: location)"),
 dict(id="F01", title="Background music: what is owed and who has it", any=["background music"], material=True, status="settled_in_data",
      record_ids=[tk("Background music"), note("Background music"), SHEET, NOTES],
      reading_a=rd("the line waits on a decision by the requester (the first wording of Brian's note), or its music is the in-game track, which base chat says was a found file", "Owed; who has it is Frederick, or what is owed is our own version of the music; the brief's sound paragraph differs"),
      reading_b=rd("the playable gets a new track made for the ad, which is ours; Calvin has not finished cutting it", "Owed: the loop for the ad, Calvin; the brief offers the track once it is cut"),
      reason="first open: the note waited on the requester himself, and the sheet's row could be read as the in-game track. Both changed 'what is owed', 'who has it', the ticket comment and the brief's sound paragraph",
      settled=settled([note("Background music"), SHEET]),
      how=f"Brian's note on {tk('Background music')} now says Calvin is still cutting the ad track down to a loop, and Calvin's sheet names the row as the pack list does and says it is a new track made for the ad, not the in-game track"),
 dict(id="F02", title="The three recoloured lines: state and who has them", any=["chainsaw", "recolour", "colour version", "color version"], material=True, status="settled_in_data",
      record_ids=[tk("Chainsaw"), tk("Cone"), tk("Cactus Plant"), NOTES],
      reading_a=rd("Brian's notes of 25 Sep 08:05 UTC stand: the files open and are in the outgoing folder; or the files are Owed and Brian re-exports them", "Ready; or Owed with Brian"),
      reading_b=rd("the art changed after the files were handed over (match3d#462, created 11:43 UTC that day), so the files go again, from Claire, who supplied them", "Owed: the current file, Claire"),
      reason="designed supersession (REVISED). The state was never in doubt for a reader who finds the pull request; the holder was open in the first round because no record said who re-exports a changed file",
      settled=settled([NOTES, note("Chainsaw"), note("Cone"), note("Cactus Plant")]),
      how="the notes now say a changed file goes again 'and it sits with whoever the file came from'; the three ticket notes say 'FBX from Claire'"),
 dict(id="F03", title="Which statement about sound the brief carries", any=["sound last time", "about sound", "when the music may start", "first click", "music starts"], material=True, status="settled_in_data",
      record_ids=[NOTES],
      reading_a=rd("'what they told us about sound last time' is the 14 Apr rule that music starts after the first click", "one sound rule in the brief"),
      reading_b=rd("it is also, or instead, the 4 Apr answer that an ad-appropriate track would be better", "a second statement in the brief, and a push on whose track is used"),
      reason="two statements by the vendor about sound sat in the first playable's history and the notes did not say which",
      settled=settled([NOTES]), how="the notes now name it: 'their rule from last time about when the music may start'"),
 dict(id="F04", title="A line without a ticket; the weapon's projectile", any=["without a ticket", "projectile"], material=True, status="settled_in_data",
      record_ids=[NOTES, tk("Cannon"), LIST],
      reading_a=rd("the rule applies to nothing: every line of the pack list has a ticket", "no ticket is opened; 96 rows"),
      reading_b=rd("the rule is there because something lacks a ticket: the vendor's list names a projectile, and Robert parks an arrow", "a 97th row and a new ticket; the Owed count moves"),
      reason="a rule sentence with an empty population invites an invented write, and no record said the projectile was covered",
      settled=settled([NOTES, note("Cannon")]), how=f"the sentence is removed from the notes, and Brian's note on {tk('Cannon')} says the cannon went in the first zip with its projectile and is what the vendor calls the rocket launcher"),
 dict(id="F05", title="The bow's own state", any=["arrow to go with the bow", "bow's own state"], material=True, status="settled_in_data",
      record_ids=[tk("Bow"), note("Bow"), REPLY],
      reading_a=rd("Robert's reply keeps the bow as it is and makes the arrow its own item; nobody is changing the bow", f"Bow: Default, Ready; {C['Delivered']} / {C['Ready']} / {C['Owed']}"),
      reading_b=rd("Claire agreed to add an arrow after the bow's file was exported, so the file may be changing", f"Bow: Default, Owed (Claire); {C['Delivered']} / {C['Ready'] - 1} / {C['Owed'] + 1}"),
      reason="the bow is one of the eight on the board and its state moves two of the three counts",
      settled=settled([note("Bow"), REPLY]), how=f"the bow's file is now of Mon 29 Sep ({tk('Bow')}, note stamped after Friday's thread), so no change follows the export; Robert's reply in the thread says to take it as it is"),
 dict(id="F06", title="'The last files from Claire' against six lines still waiting on her", any=["last files", "still has a few", "waiting on the fbx"], material=True, status="settled_in_data",
      record_ids=[S["c4_log"]["id"]] + WAIT_CLAIRE,
      reading_a=rd("'last' is the latest batch; the six lines noted as waiting on Claire are still with her", "the six: Owed, Claire"),
      reading_b=rd("'last' is the final batch; the six notes are stale and the files sit with Brian, or are in the folder", "the six: Owed with Brian, or Ready (42 / 46)"),
      reason="Brian's log is later than the six notes and is the kind of later word the notes tell the reader to honour",
      settled=settled([S["c4_log"]["id"]] + [note(l["name"]) for l in M.members("VIS") if "Waiting on the FBX from Claire" in l["note"]]),
      how="the log's Monday line now reads 'another batch from Claire. She still has a few to send and a few are still mine to do', and the notes on the lines not yet exported are stamped Mon 29 Sep after that day's batch"),
 dict(id="F07", title="Zombie characters: Delivered or Owed", any=["zombie characters", "re-rig"], material=False, status="settled_in_data",
      record_ids=[tk("Zombie characters"), note("Zombie characters"), ZPICKS],
      reading_a=rd("the vendor holds a working pack, has reviewed it and will re-rig from it; what is open is a choice, which Robert has made", "Delivered; the ticket stays Done"),
      reading_b=rd("they cannot use the pack until told the four zombies and the animation", "Owed; 7 / 36 / 53"),
      reason="both reviewers read it as Delivered on the vendor's own 29 Sep message; the first wording of the note ('a question for Robert, not about the files') sat badly with Brian's base remark of the same morning",
      settled=settled([note("Zombie characters"), ZPICKS]), how="the note now reports the vendor's message as it is (they will re-rig from the pack and want one animation and four zombies picked), and Robert's post says all four are in the pack Marcus sent"),
 dict(id="F08", title="What the counts count", any=["three counts", "count for each state"], material=True, status="settled_in_data",
      record_ids=[ASK, NOTES, PT],
      reading_a=rd("one count per state word over every row of the hand-off list", f"{C['Delivered']} / {C['Ready']} / {C['Owed']}"),
      reading_b=rd("one count per Board set value, or 'item pack' read as the board items only", "8 / 76 / 12, or " + " / ".join(str(sum(1 for l in BOARD if l["state"] == st)) for st in ("Delivered", "Ready", "Owed"))),
      reason="the three figures in the DM to Frederick",
      settled=settled([ASK, NOTES, PT]), how="the ask says 'give me the count for each state' right after 'where the item pack actually stands. Brian's pack list is where it starts'; the notes give a State to every row, one row per line of the pack list (sounds, 2D, font, cannon, background and zombies included); Brian's pack ticket tracks 'every line of the playable pack'"),
 dict(id="F09", title="Category on the hand-off list", any=["category"], material=False, status="settled_in_data",
      record_ids=[NOTES, LIST],
      reading_a=rd("Category is copied from the pack list (empty for the twelve lines that are not board items)", "Brian's column, as it is"),
      reading_b=rd("Category is the Kind for those twelve, or the value in another base source for about ten board items", "other values in that column"),
      reason="no check reads the column for those lines; the base files a few objects under other categories in a workbook the persona cannot open and in the prefab folders",
      settled=settled([NOTES]), how="the notes now say 'Line, Category and Ticket are as on his list'"),
 dict(id="F10", title="Where in the PlayableX channel the links go", any=["post both links", "both links in the playablex channel", "thread position", "top-level", "top level"], material=False, status="both_fair",
      record_ids=[ASK],
      reading_a=rd("a new top-level message in the channel", "a top-level post with the two links"),
      reading_b=rd("a reply in the thread where the vendor gave 3 November", "a thread reply with the two links"),
      reason="both are 'in the PlayableX channel'; no record prefers one, and it matters only to a check that reads the thread position",
      both_fair={"figure_a": "top-level post in C08H78VJG80", "figure_b": "reply under C08H78VJG80/1759174925.309129", "rubric_accepts_both": True},
      how="the rubric accepts the two links in the channel in either position (dossier, platform follow-ups)"),
 dict(id="F11", title="The kickoff hold cited by notes saved before it existed", any=["kickoff hold"], material=False, status="settled_in_data",
      record_ids=[NOTES, HOLD],
      reading_a=rd("the hold the notes name is the one on Julia's calendar for 3 Nov", "the hold's four attendees"),
      reading_b=rd("the notes were last saved before that hold was created, so they mean an older hold", "a search for another event"),
      reason="a timestamp inconsistency with no second event to find; it changes nothing but reads as planted",
      settled=settled([HOLD]), how="the hold and its invitations are now created 30 Sep 16:41 UTC, before the notes' last edit at 16:58 (plan/out/citation_chronology.txt)"),
 dict(id="F12", title="Leonard's Trello comment on who is doing the work", any=["trello"], material=False, status="settled_in_data",
      record_ids=[TRELLO, ASK],
      reading_a=rd("Julia writes the brief and reports on the pack, as the ask says", "Julia's work"),
      reading_b=rd("Frederick is doing both himself, and the vendor moved the start on its own", "a reader of the card expects nothing from Julia"),
      reason="low: the comment disagreed with the ask and with the channel on who asked for the pause",
      settled=settled([TRELLO]), how="the comment now says the start is the one PlayableX gave after we asked for the pause, and that Julia is pulling the brief and the pack status together for Frederick"),
 dict(id="F13", title="Ticket numbers against the team's base tickets", any=["ticket order", "issue numbers", "order of linear tickets", "back-dated", "out of sequence", "new home"], material=False, status="settled_in_data",
      record_ids=[PT, ALL[0], ALL[-1]],
      reading_a=rd("the pack tickets were opened on 25 Sep, as their dates say", "Brian's notes of 25 to 29 Sep predate the later statements"),
      reading_b=rd("numbers follow creation order, so tickets numbered after a ticket of 30 Sep were opened after it", "every note would postdate the statements that overturn it"),
      reason="in ZOM the 97 keys sat above ZOM-566, created five days later; both reviewers named it the most visible tell",
      settled=settled([PT]), how=f"the pack ticket and its children are now Design-team tickets, {PT} to {M.LAST_CHILD}: the team's last base ticket is DES-312 of 7 May 2025, so numbers and dates run in order; the pack ticket's description says why it is kept there ('kept in Design so it stays off the ZM3D board'), which is the one record that explains the first Design-team activity since May and a parent with 96 children; Brian's last base tickets there are the same parent-and-children shape"),
 dict(id="F14", title="Two different notes in the same second", any=["same second"], material=False, status="settled_in_data",
      record_ids=[note("Cannon"), note("Background")],
      reading_a=rd("two notes typed one after the other", "nothing"), reading_b=rd("two different hand-written notes cannot share a second: the notes were generated", "a reader distrusts the notes"),
      reason="cosmetic; it appeared when the two notes got their own wording",
      settled=settled([note("Cannon"), note("Background")]), how="the notes on the delivered lines are now about a minute apart; plan/build_spec.py refuses two notes in one second and two differently worded notes less than 20 s apart"),
 # designed supersessions: the reviewers list them as contradictions that resolve
 dict(id="F15", title="EXPORT: twelve files saved out of the project", any=["saved out of the project", "got out of unity", "text kind", "thursday unity exports", "ascii"], material=True, status="settled_in_data",
      record_ids=tks("A1") + [A1],
      reading_a=rd("Brian's notes stand: FBX, opens, looks right, in the outgoing folder; or the fix is to get the twelve from Claire", "Ready; or Owed with Claire"),
      reading_b=rd("Marcus's later post: the models Brian got out of Unity on Thursday are the text kind (the setting was wrong that day) and Brian will need to redo them; the vendor takes binary FBX only", "Owed: export again as binary, Brian"),
      reason="designed (anchor A1): the note passes every Ready test on its face", settled=settled([A1]), how="Marcus's post in #zombie-match3d, dated after the twelve notes and addressed to Brian ('youll need to redo them'), with the vendor's base format rule"),
 dict(id="F16", title="ARTHOLD: twelve bathroom files", any=["bathroom", "uvs", "redoing the uv"], material=True, status="settled_in_data",
      record_ids=tks("A2") + [A2],
      reading_a=rd("Brian's notes of Fri 26 Sep stand", "Ready"), reading_b=rd("Robert's later note: Claire is redoing the UVs on the bathroom objects and the files she gave Brian on Friday are the old version", "Owed, Claire (the file came from her)"),
      reason="designed (anchor A2)", settled=settled([A2]), how="Robert's note to Julia of 29 Sep, in their DM; the notes leave a changed file with whoever it came from"),
 dict(id="F17", title="ZIP: eight instruments in Friday's zip", any=["instrument", "zipped", "those eight"], material=True, status="settled_in_data",
      record_ids=tks("C4") + [S["c4_log"]["id"]],
      reading_a=rd("Brian's notes stand: zipped, in the outgoing folder", "Ready"), reading_b=rd("his own log of 30 Sep: the zip will not unpack and the eight are not in the folder any other way", "Owed: put the files back, Brian"),
      reason="designed (coin-flip C4)", settled=settled([S["c4_log"]["id"]]), how="Brian's log of the outgoing folder"),
 dict(id="F18", title="AUDIO: two cues from a library and a bought pack", any=["rocket sound", "explosion sound", "library or a bought pack"], material=True, status="settled_in_data",
      record_ids=tks("C2") + [SHEET, NOTES],
      reading_a=rd("Brian's notes stand: exported .wav, plays", "Ready"), reading_b=rd("the notes hand over only sound that is ours; Calvin's sheet marks both 'no'", "Owed: our own version, Calvin"),
      reason="designed (coin-flip C2)", settled=settled([SHEET, NOTES]), how="Calvin's sound sources sheet with the notes' rule on sound"),
 dict(id="F19", title="PICKS: the eight on the board", any=["eight items on the board", "the eight", "dynamite", "in place of the last one", "robert's eight", "default board items"], material=True, status="settled_in_data",
      record_ids=[PICKS, REPLY, S["deck"]["id"], tk("Bow"), tk("Dynamite")],
      reading_a=rd("Robert's post of 25 Sep: the eight end with the dynamite; or the deck's five", "Dynamite: Default; Bow: Extra"),
      reading_b=rd("his reply of 26 Sep puts the bow in place of the last one on his list; the deck is what was built on 23 Sep", "Bow: Default; Dynamite: Extra"),
      reason="designed (coin-flip C3)", settled=settled([REPLY, PICKS]), how="Robert's reply under Julia's bow post, read with his 25 Sep post"),
 dict(id="F20", title="Which zombies and which animation", any=["which zombies", "four zombies", "zombie roster", "which zombies exist", "the 4 zombies", "zombies for the playable"], material=False, status="settled_in_data",
      record_ids=[ZPICKS, S["deck"]["id"]],
      reading_a=rd("'a mix, nothing fixed yet' (the deck, 23 Sep), or the design page's roster", "no fixed four, or other names"),
      reading_b=rd("Robert's answer of 29 Sep: walk; Party Girl, Plumber, Magician, Football Player", "the four and the one animation in the brief"),
      reason="resolves by date and by the ask ('Robert's picks ... stand'); the design page's roster does not list three of the four (card SC-58: not cited, not graded)",
      settled=settled([ZPICKS]), how="Robert's post, which now adds that all four are in the pack Marcus sent; base has them in the pack Brian asked for"),
 dict(id="F26", title="How a level is won and lost", any=["how a level is won", "won and lost", "win condition", "fail state", "blunder = death", "full tray", "tray fills", "tray-full", "enrage"], material=True, status="settled_in_data",
      record_ids=[NOTES, B["gdd"], B["brian_winfail"], f"{M.DM_ROBERT}/1759248923.659659", "C090N54TG79/1759176983.189479", "C090N54TG79/1759172801.164409"],
      reading_a=rd("the design page: a full tray is a blunder (the tray clears, the survivors enrage) and the level is lost only at zero health; won by eliminating every zombie on screen (Brian to PlayableX, 24 Sep; Robert to Julia, 30 Sep)", "lost at zero health; won by clearing the zombies"),
      reading_b=rd("Leonard's 29 Sep 'make blunder = death', the Match Factory rule on the competitive-analysis page, a boss mode's score 'before the tray fills', or an FTUE level's boss", "a full tray loses; or won by killing the boss"),
      reason="base only, and settled by base: Leonard's line is a proposal, and Robert's post in the same channel that evening says 'Blunder was fine the way it is'; the competitive-analysis page itself says Zombie Match 3D does not take Match Factory's fail rule; the boss mode and the FTUE level are modes and one level, not the core level; the design page (which the ask points to) and Brian's message to the vendor agree",
      settled=settled([NOTES]), how="the hand-off notes say 'How the level plays is on the design page', and the design page's core mechanic ('not a fail state - the loss screen only appears at zero health') with Brian's 24 Sep message in the PlayableX channel ('the win condition is eliminating all the zombies on screen')"),
 dict(id="F27", title="The duck PlayableX asked for, and the zip it went in", any=["duck", "plushie"], material=True, status="settled_in_data",
      record_ids=[B["vendor_duck"], S["deck"]["id"], note("Plushie Chick"), tk("Plushie Chick"), tk("Rubber Ducky"), B["vendor_blank_scene"], B["vendor_zombie_ask"]],
      reading_a=rd("'the duck asset used in the reference' is the reference level's Plushie Chick, which went in the second zip on 24 Sep; the vendor's complaint of 25 Sep was the zombie package", "Plushie Chick: Default, Delivered; Rubber Ducky: Owed (Claire)"),
      reading_b=rd("'the duck' is the Rubber Ducky line, or the chick went in a zip the vendor called broken", "Plushie Chick Owed, or the two lines swapped"),
      reason="a Default board item's state and two of the three counts. Reviewer-1 holds that Brian's note is the owner's own reading; so is every Delivered line's note (the first zip's Couch, Grenade, Cannon and the rest carry no vendor confirmation either), and the notes are the record the hand-off rests on. The vendor's own 25 Sep message names 'the zombie assets', and its 29 Sep message, after reviewing, raises only the characters",
      settled=settled([note("Plushie Chick"), S["deck"]["id"]]), how="the Plushie Chick's note, written at 14:06 UTC on 25 Sep after the vendor's 13:50 UTC message, names the vendor's word for it and says that message is about the zombie package, not the chick; the reference deck's board has the chick and no rubber duck; the vendor's 25 Sep message names 'the zombie assets' and its 29 Sep message, after reviewing, asks only about the zombies"),
 dict(id="F28", title="What Julia did for the Dominoes playable", any=["domino"], material=False, status="settled_in_data",
      record_ids=[ASK, "C08H78VJG80/1741963515.221549", B["vendor_thanks_brief"], "D05SD5QLG94/1758221343.478869", "D05SD5QLG94/1758221424.223519"],
      reading_a=rd("Julia wrote the brief the vendor built from (her 14 Mar post in the PlayableX channel, which the vendor thanks for 'this detailed brief'); Brian fished out the assets and they went over in a zip", "the brief is Julia's; where the pack stands comes from Brian's records"),
      reading_b=rd("there is no Dominoes brief of Julia's to follow", "no precedent for the brief's shape"),
      reason="base only and consistent: the precedent sits in the vendor channel, not in her Drive, and Frederick's ask names the same two parts (the brief, where the pack stands)",
      settled=settled([ASK]), how="Frederick's ask itself says what she did for the Dominoes playable ('write the brief they build from'); that brief is her 14 Mar post in the PlayableX channel, which the vendor thanked on 15 Mar"),
 dict(id="F29", title="Fonts: who has it", any=["ttf", "fonts"], material=True, status="settled_in_data",
      record_ids=[tk("Fonts"), note("Fonts"), NOTES],
      reading_a=rd("the next thing is Martin sending the .ttf files", "Fonts: Owed, the font files, Martin"),
      reading_b=rd("Brian has to get the files and send them", "Fonts: Owed, Brian"),
      reason="the holder on one Owed row and its ticket comment",
      settled=settled([note("Fonts"), NOTES]), how="the note now reads 'Waiting on the .ttf files from Martin', the wording of the lines waiting on Claire; the notes say who has it is whoever has to do the next thing"),
 dict(id="F30", title="What the scenario is for", any=["which scenario we picked", "what it is for", "scenario"], material=True, status="settled_in_data",
      record_ids=[ASK, B["fred_retention"], B["fred_scenario1"], "C090N54TG79/1758569655.409719", "C090N54TG79/1758569707.508219", B["julia_shuriken_idea"], "C090N54TG79/1758569872.578829", B["robert_remain"]],
      reading_a=rd("Frederick to the vendor, 12 Sep: a playable that filters out the players who won't like the game while staying true to the core game play; Robert, 22 Sep: test the current form and audience fit, not what the game could be tailored to become", "the brief gives that purpose"),
      reading_b=rd("Julia's 22 Sep line in the same thread: a more hardcore friendly playable", "the brief asks PlayableX for a more hardcore-leaning playable"),
      reason="the purpose sentence PlayableX builds from",
      settled=settled([ASK]), how="Robert answers in the same thread three minutes later ('Doesn't really matter', 'I think we should remain as is'), and Frederick's ask says 'Write it for the game as it is today'; the platform's /oe round 1 read it the same way (reading b refuted). Rev2 had marked this fork both fair, which was wrong"),
]

# ---------------------------------------------------------------- dismissals (base-only or checked-and-consistent findings)
DISMISS = [
 (["how many slots the tray has", "tray size", "6 in a soft-test", "7-slot", "slots"], f"settled by a base record the persona can open: Robert's reply on the design page keeps it at seven ({B['gdd_c2']}); both reviewers checked it"),
 (["start date"], f"base only and resolved by date: the vendor's latest message gives 3 November ({B['vendor_nov3']}), and the hold is on that day"),
 (["role"], "base only and low: it affects voice, not an outcome; the ask's reference to the first playable matches base"),
 (["i sent them the assets", "how much of the pack"], f"base only: Brian's remark of 29 Sep is about the three uploads in the vendor channel; the pack ticket's rule (a ticket closes when the vendor has the file), the eight Done tickets and the pack list's 'Went out' column say which lines went"),
 (["zm3d sound sources sheet", "sound sources sheet"], f"checked and consistent: Calvin's sheet was started on 12 Sep after Robert's copyright question of 10 Sep ({B['robert_copyright']}) and last edited on 26 Sep, after the vendor's list of 19 Sep; cue names from that list are later edits, which the sheet's modified time shows"),
 (["who has it", "whoever has to do the next thing"], "checked and consistent: each Owed line names one holder (the deciding record or the line's own note); listed for completeness by the reviewer"),
]

# ---------------------------------------------------------------- open sets beyond the quantifier spans (span must be in the record's text)
OPEN_SETS = [
 dict(key="themessage", any=["frederick's playable message"], where="prompt", span="Frederick's playable message", rule="the one message from Frederick to Julia that asks for anything about the playable: his DM of 30 Sep 2025", ids=[ASK]),
 dict(key="everything", any=["everything he's asking for", "start to finish"], where="prompt", span="everything he's asking for in it", rule="every instruction of Frederick's message and of the notes it names: the brief, the hand-off list, the ticket follow-through, the sharing, the count for each state, the two links. Not asked: replying to the invitation, answering the vendor's question in the channel, chasing the holders, the Trello card, new or reassigned tickets", ids=[ASK, NOTES]),
 dict(key="rows", any=["one row per line"], where=NOTES, span="One row per line of Brian's pack list", rule="a data row of the pack list's tab = a child ticket of the pack ticket: 96 lines", ids=ALL),
 dict(key="default", any=["default for the eight", "the eight items on the board"], where=NOTES, span="Board set is Default for the eight on the board", rule="Robert's eight of 25 Sep with his 26 Sep reply applied: " + ", ".join(M.DEFAULT_FINAL), ids=DEFAULT),
 dict(key="extra", any=["every other board item", "everything else"], where=NOTES, span="Extra for every other board item", rule="a row whose Kind is Board item and which is not one of the eight: 76 lines", ids=EXTRA),
 dict(key="nonboard", any=["isn't a board item", "is not a board item"], where=NOTES, span="leave it empty for anything that isn't a board item", rule="a row whose Kind is not Board item: 12 lines", ids=[l["ticket"] for l in LISTED if l["kind"] != "Board item"]),
 dict(key="delivered", any=["delivered: playablex has the current file"], where=NOTES, span="Delivered: PlayableX has the current file and can use it.", rule="the lines Brian notes as sent on 24 or 26 Sep with no change since; their tickets are Done", ids=DELIVERED),
 dict(key="ready", any=["ready: exported in a format"], where=NOTES, span="Ready: exported in a format they take and sitting in the outgoing folder, it opens, it is the current version and nobody is changing it.", rule="the lines whose note says the file opens or plays and is in the outgoing folder, with nothing later against format, presence, currency or source", ids=READY),
 dict(key="owed", any=["owed: anything else"], where=NOTES, span="Owed: anything else.", rule="every line that is neither Delivered nor Ready (solver/truth.json)", ids=OWED),
 dict(key="todo", any=["goes to todo"], where=NOTES, span="An Owed line's ticket goes to Todo with a comment saying what is owed and who has it.", rule="the tickets of the Owed lines; all are In Progress in the SQL", ids=OWED),
 dict(key="leave", any=["leave the delivered and ready"], where=NOTES, span="Leave the Delivered and Ready ones as they are.", rule="the Done tickets of the Delivered lines and the In Progress tickets of the Ready lines: no change, no comment", ids=DELIVERED + READY),
 dict(key="changed", any=["if the art changed"], where=NOTES, span="If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again", rule="a line whose art changed after the date of Brian's note: the three recoloured lines (Robert's 29 Sep post), which went again on 30 Sep (Brian's log) and are Ready; the twelve bathroom lines are being changed now and fail 'nobody is changing it' instead", ids=tks("C1")),
 dict(key="library", any=["library or a bought pack"], where=NOTES, span="Anything from a library or a bought pack stays here until we have our own version.", rule="a sound line of the pack list whose row in Calvin's sheet says 'no' under 'OK outside the game': Rocket sound, Explosion sound", ids=tks("C2")),
 dict(key="hold", any=["everyone on the kickoff hold", "sharing: both files"], where=NOTES, span="Everyone on the kickoff hold", rule="the attendees of the 3 Nov hold: Frederick Stone, Julia Lawson, Brian Foster, Robert (one event copy per calendar)", ids="HOLD"),
 dict(key="since", any=["said something since"], where=NOTES, span="if someone who knows the file or the art has said something since, that counts", rule="a dated statement after Brian's note on a line, by the person who made, exported or holds the file or the art", ids=[A1, A2, S["c4_log"]["id"], REPLY], base_ids=[B["pr462"], B["robert_new_colours"]]),
 dict(key="musicrule", any=["rule from last time", "sound last time"], where=NOTES, span="their rule from last time about when the music may start", rule="the vendor's one statement on when music may start, from the first playable", ids=[], base_ids=[B["vendor_music_rule"]]),
 dict(key="picks", any=["robert's picks"], where=ASK, span="Robert's picks for the board and the zombies stand unless he's changed them since", rule="Robert's own statements on the playable's board and zombies, latest first", ids=[PICKS, REPLY, ZPICKS]),
 dict(key="eightzip", any=["those eight"], where=S["c4_log"]["id"], span="those eight", rule="the instrument lines whose note says 'Zipped with the other instruments'", ids=tks("C4")),
 dict(key="thursday", any=["got out of unity on thursday", "saved out of unity on thursday"], where=A1, span="the models you got out of unity on thursday", rule="the lines whose note says 'FBX saved out of the project, Thu 25 Sep'", ids=tks("A1")),
 dict(key="banyo", any=["banyo objeleri", "the bathroom objects"], where=A2, span="the UVs on the bathroom objects", rule="the lines in Category Bathroom whose file came from Claire on Fri 26 Sep (the Rubber Ducky was never exported and is Owed on its own note)", ids=tks("A2")),
 dict(key="clairetickets", any=["ticketlara", "files she gave"], where=A2, span="the bathroom files she gave", rule="the bathroom files Claire gave Brian on Fri 26 Sep: the twelve Bathroom lines whose note says 'FBX from Claire, Fri 26 Sep' (the Rubber Ducky was never exported and is Owed on its own note)", ids=tks("A2")),
 dict(key="coming", any=["still coming from us"], where=ASK, span="so they know what's still coming from us", rule="the lines PlayableX does not have yet: every line not Delivered (the Ready ones are in our folder, not sent)", ids=READY + OWED),
 dict(key="few", any=["still has a few"], where=S["c4_log"]["id"], span="She still has a few to send and a few are still mine to do.", rule="the lines whose note says 'Waiting on the FBX from Claire' and those whose note says the export is Brian's to do", ids=WAIT_CLAIRE + MINE),
 dict(key="fourz", any=["all four are in the pack", "the 4 zombies"], where=ZPICKS, span="The 4 zombies: Party Girl, Plumber, Magician, Football Player.", rule="four of the nine zombies in the pack Brian asked Marcus for", ids=[], base_ids=[B["anim_zombies"]]),
]
NOT_POP = [
 (["should end up in my drive", "go in the playablex channel"], "prompt", "my Drive", "the two destinations the prompt names (her Drive and the PlayableX channel); places, not sets of records"),
 (["files he wants", "the files"], "prompt", "The files he wants", "the two files the task creates; nothing in the universe to enumerate"),
 (["the links"], "prompt", "the links", "the links to those two files; nothing in the universe to enumerate"),
 (["count for each state", "three counts"], ASK, "the count for each state", "three numbers computed from the hand-off list, one per state word; not a set of records"),
 (["both files", "both links"], NOTES, "both files", "the two files the task creates (the brief and the hand-off list); nothing in the universe to enumerate"),
]

# ---------------------------------------------------------------- take up every finding
def text_of(f):
    return " ".join(json.dumps(f.get(k), ensure_ascii=False) for k in ("span", "about", "rule", "where", "record_ids")).lower()
REVIEW = WF / "local_reviews" / "coherence"
forks = {f["id"]: dict(f, sources=[]) for f in FORKS}
osets = {o["key"]: dict(o, sources=[]) for o in OPEN_SETS}
npop = [dict(any=a, where=w, span=s, why=y, sources=[]) for a, w, s, y in NOT_POP]
dismissed, unmatched = [], []
for rid in ("1", "2"):
    data = json.loads((REVIEW / f"findings_{rid}.json").read_text())
    for kind in ("forks", "contradictions", "open_sets"):
        for f in data.get(kind, []):
            src, t = f"{rid}:{f['id']}", text_of(f)
            if kind == "open_sets":
                hit = next((o for o in osets.values() if any(w in t for w in o["any"])), None)
                if hit: hit["sources"].append(src); continue
                hit = next((o for o in npop if any(w in t for w in o["any"])), None)
                if hit: hit["sources"].append(src); continue
            hit = next((x for x in forks.values() if any(w in t for w in x["any"])), None)
            if hit: hit["sources"].append(src); continue
            d = next((why for words, why in DISMISS if any(w in t for w in words)), None)
            if d: dismissed.append({"source": src, "reason": d}); continue
            unmatched.append((src, kind, t[:160]))
if "--show" in sys.argv:
    for x in forks.values(): print("FORK", x["id"], x["title"][:50], "<-", x["sources"])
    for o in osets.values(): print("SET ", o["key"], "<-", o["sources"])
    for o in npop: print("NPOP", o["span"], "<-", o["sources"])
    for d in dismissed: print("DISM", d["source"], "|", d["reason"][:70])
if unmatched:
    print("NOT TAKEN UP:"); [print("  ", u) for u in unmatched]; sys.exit(1)

hold_ids = sorted(json.loads((HERE / "out" / "sql_ids.json").read_text())["events"].values())
out_forks = []
for f in forks.values():
    e = {k: v for k, v in f.items() if k not in ("any",)}
    out_forks.append(e)
out_sets = []
for o in osets.values():
    ids = hold_ids if o["ids"] == "HOLD" else list(dict.fromkeys(o["ids"]))
    base_ids = o.get("base_ids", [])
    out_sets.append({"span": o["span"], "where": o["where"], "sources": o["sources"], "rule": o["rule"], "census": {"count": len(ids) + len(base_ids), "ids": ids, "base_ids": base_ids}})
for o in npop:
    out_sets.append({"span": o["span"], "where": o["where"], "sources": o["sources"], "not_a_population": o["why"]})
(HERE / "sweep_findings_map.json").write_text(json.dumps({"forks": out_forks, "open_sets_reviewed": out_sets, "dismissed": dismissed}, indent=1, ensure_ascii=False) + "\n")
print("findings map:", len(out_forks), "forks,", sum(1 for f in out_forks if f["sources"]), "with a current finding;", len(out_sets), "reviewed open sets;", len(dismissed), "dismissed")
