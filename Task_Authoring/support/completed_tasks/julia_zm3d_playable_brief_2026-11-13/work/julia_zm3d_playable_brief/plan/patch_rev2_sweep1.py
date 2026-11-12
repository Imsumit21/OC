#!/usr/bin/env python3
"""rev2 coherence sweep, round 1 (reviewer-1 and reviewer-2 on SQL 7ce1ce5a...): the data fixes and the findings-map entries,
batched in one pass so the reviewers are re-briefed once. Idempotent; prints what was applied.

Data (design_model.py):
  * Plushie Chick's note (reviewer-1 F2 / C12): the vendor's 25 Sep complaint about the second zip was the zombie package;
    the note now says so, so 'can use it' rests on the line's own record and not on silence.
  * Fonts' note (reviewer-1 F17): 'Waiting on the .ttf files from Martin', the same wording as the lines waiting on Claire,
    so the next thing is plainly Martin's.
Surface (build_surface.py):
  * B2b 'what the scenario is for' (reviewer-1 F11, reviewer-2 F3): both fair; it accepts Frederick's 12 Sep reasoning or the
    22 Sep #zombie-design agreement (test the game as it is and its audience fit, a more hardcore-friendly playable).
Findings map (build_findings_map.py): narrower keywords where a finding was claimed by the wrong entry, and new entries for
  win/loss (F26), the duck (F27), the Dominoes precedent (F28), Fonts (F29), the scenario purpose (F30), and the open set
  'what's still coming from us'."""
from pathlib import Path
HERE = Path(__file__).resolve().parent

DM = [
 ('NOTE_W = {"Plushie Chick": "Went in the second zip on 24 Sep (the one they called the duck).",',
  'NOTE_W = {"Plushie Chick": "Went in the second zip on 24 Sep (the one they called the duck). What they said was wrong with that zip the next day was the zombie package, not the chick.",'),
 ('"Fonts": ("Not sent. Need the .ttf files from Martin.", "the font files", "Martin Walsh"),',
  '"Fonts": ("Not sent. Waiting on the .ttf files from Martin.", "the font files", "Martin Walsh"),'),
]
SURF = [
 ('''slot("B2b", "brief: what the scenario is for", 3, INT, "Frederick's 12 Sep reasoning: filter for players who will like the game, true to the core game play",
     "write_content", ["text", "brief", "filter|retention|core game ?play|core mechanic"], "core", [], ASK_SPAN, fact_id="scenario_purpose")''',
  '''slot("B2b", "brief: what the scenario is for", 3, INT, "Frederick's 12 Sep reasoning (filter for players who will like the game, true to the core game play) or, equally, the 22 Sep #zombie-design agreement (test the game as it is and its audience fit, a more hardcore-friendly playable)",
     "write_content", ["text", "brief", "filter|retention|core game ?play|core mechanic|audience fit|hardcore|current form|as it is"], "core", [], ASK_SPAN, fact_id="scenario_purpose")'''),
]
FM = [
 ('dict(id="F05", title="The bow\'s own state", any=["arrow"],',
  'dict(id="F05", title="The bow\'s own state", any=["arrow to go with the bow", "bow\'s own state"],'),
 ('dict(id="F15", title="EXPORT: twelve files saved out of the project", any=["saved out of the project", "got out of unity", "text kind"],',
  'dict(id="F15", title="EXPORT: twelve files saved out of the project", any=["saved out of the project", "got out of unity", "text kind", "thursday unity exports", "ascii"],'),
 ('dict(id="F19", title="PICKS: the eight on the board", any=["eight items on the board", "the eight", "dynamite"],',
  'dict(id="F19", title="PICKS: the eight on the board", any=["eight items on the board", "the eight", "dynamite", "in place of the last one", "robert\'s eight", "default board items"],'),
 ('any=["which zombies", "four zombies", "zombie roster", "which zombies exist", "the 4 zombies"]',
  'any=["which zombies", "four zombies", "zombie roster", "which zombies exist", "the 4 zombies", "zombies for the playable"]'),
 ('any=["sound last time", "about sound", "when the music may start", "first click"]',
  'any=["sound last time", "about sound", "when the music may start", "first click", "music starts"]'),
 # the scenario purpose is now a both-fair fork (F30), and the tray-fill rule is part of F26 (B4b grades the loss rule)
 (''' (["which scenario we picked", "what it is for", "scenario"], f"the two base statements are compatible and the one made to the vendor is Frederick's ({B['fred_retention']}); both reviewers checked it"),\n''', ''),
 # the tray-fill dismissal is removed by hand after this patch (its claims moved to F26)
 # new forks, appended after F20 so the older entries keep their claims
 ('''      settled=settled([ZPICKS]), how="Robert's post, which now adds that all four are in the pack Marcus sent; base has them in the pack Brian asked for"),
]''',
  '''      settled=settled([ZPICKS]), how="Robert's post, which now adds that all four are in the pack Marcus sent; base has them in the pack Brian asked for"),
 dict(id="F26", title="How a level is won and lost", any=["how a level is won", "won and lost", "win condition", "fail state", "blunder = death", "full tray", "tray fills", "tray-full", "enrage"], material=True, status="settled_in_data",
      record_ids=[B["gdd"], B["brian_winfail"], f"{M.DM_ROBERT}/1759248923.659659", "C090N54TG79/1759176983.189479", "C090N54TG79/1759172801.164409"],
      reading_a=rd("the design page: a full tray is a blunder (the tray clears, the survivors enrage) and the level is lost only at zero health; won by eliminating every zombie on screen (Brian to PlayableX, 24 Sep; Robert to Julia, 30 Sep)", "lost at zero health; won by clearing the zombies"),
      reading_b=rd("Leonard's 29 Sep 'make blunder = death', the Match Factory rule on the competitive-analysis page, a boss mode's score 'before the tray fills', or an FTUE level's boss", "a full tray loses; or won by killing the boss"),
      reason="base only, and settled by base: Leonard's line is a proposal, and Robert's post in the same channel that evening says 'Blunder was fine the way it is'; the competitive-analysis page itself says Zombie Match 3D does not take Match Factory's fail rule; the boss mode and the FTUE level are modes and one level, not the core level; the design page (which the ask points to) and Brian's message to the vendor agree",
      settled=settled([B["gdd"], B["brian_winfail"]]), how="the design page's core mechanic ('not a fail state - the loss screen only appears at zero health') with Brian's 24 Sep message in the PlayableX channel ('the win condition is eliminating all the zombies on screen')"),
 dict(id="F27", title="The duck PlayableX asked for, and the zip it went in", any=["duck", "plushie"], material=True, status="settled_in_data",
      record_ids=[B["vendor_duck"], S["deck"]["id"], note("Plushie Chick"), tk("Plushie Chick"), tk("Rubber Ducky"), B["vendor_blank_scene"], B["vendor_zombie_ask"]],
      reading_a=rd("'the duck asset used in the reference' is the reference level's Plushie Chick, which went in the second zip on 24 Sep; the vendor's complaint of 25 Sep was the zombie package", "Plushie Chick: Default, Delivered; Rubber Ducky: Owed (Claire)"),
      reading_b=rd("'the duck' is the Rubber Ducky line, or the chick went in a zip the vendor called broken", "Plushie Chick Owed, or the two lines swapped"),
      reason="a Default board item's state and two of the three counts",
      settled=settled([note("Plushie Chick"), S["deck"]["id"]]), how="the Plushie Chick's note names the vendor's word for it and now says the complaint about that zip was the zombie package, not the chick; the reference deck's board has the chick and no rubber duck; the vendor's 25 Sep message names 'the zombie assets' and its 29 Sep message, after reviewing, asks only about the zombies"),
 dict(id="F28", title="What Julia did for the Dominoes playable", any=["domino"], material=False, status="settled_in_data",
      record_ids=["C08H78VJG80/1741963515.221549", B["vendor_thanks_brief"], "D05SD5QLG94/1758221343.478869", "D05SD5QLG94/1758221424.223519"],
      reading_a=rd("Julia wrote the brief the vendor built from (her 14 Mar post in the PlayableX channel, which the vendor thanks for 'this detailed brief'); Brian fished out the assets and they went over in a zip", "the brief is Julia's; where the pack stands comes from Brian's records"),
      reading_b=rd("there is no Dominoes brief of Julia's to follow", "no precedent for the brief's shape"),
      reason="base only and consistent: the precedent sits in the vendor channel, not in her Drive, and Frederick's ask names the same two parts (the brief, where the pack stands)",
      settled=settled(["C08H78VJG80/1741963515.221549", B["vendor_thanks_brief"]]), how="Julia's 14 Mar post and the vendor's thanks of 15 Mar, both in the PlayableX channel"),
 dict(id="F29", title="Fonts: who has it", any=["ttf", "fonts"], material=True, status="settled_in_data",
      record_ids=[tk("Fonts"), note("Fonts"), NOTES],
      reading_a=rd("the next thing is Martin sending the .ttf files", "Fonts: Owed, the font files, Martin"),
      reading_b=rd("Brian has to get the files and send them", "Fonts: Owed, Brian"),
      reason="the holder on one Owed row and its ticket comment",
      settled=settled([note("Fonts"), NOTES]), how="the note now reads 'Waiting on the .ttf files from Martin', the wording of the lines waiting on Claire; the notes say who has it is whoever has to do the next thing"),
 dict(id="F30", title="What the scenario is for", any=["which scenario we picked", "what it is for", "scenario"], material=True, status="both_fair",
      record_ids=[B["fred_retention"], B["fred_scenario1"], "C090N54TG79/1758569655.409719", "C090N54TG79/1758569707.508219"],
      reading_a=rd("Frederick to the vendor, 12 Sep: a playable that filters out the players who won't like the game while staying true to the core game play", "the brief gives that purpose"),
      reading_b=rd("the 22 Sep #zombie-design thread: test the game as it is and its audience fit, a more hardcore-friendly playable", "the brief gives that purpose"),
      reason="two base statements, both visible to Julia, that say the same thing in different words; which one the brief quotes changes its text",
      both_fair={"figure_a": "filter for the players who will like the game, true to the core game play (Frederick, 12 Sep)", "figure_b": "test the current game and its audience fit, more hardcore-friendly (Robert and Julia, 22 Sep)", "rubric_accepts_both": True},
      how="slot B2b accepts either wording (01_Gradable_Surface.json); the rubric stage carries the same pair"),
]'''),
 # a new open set: what PlayableX does not have yet
 (''' dict(key="few", any=["still has a few"],''',
  ''' dict(key="coming", any=["still coming from us"], where=ASK, span="so they know what's still coming from us", rule="the lines PlayableX does not have yet: every line not Delivered (the Ready ones are in our folder, not sent)", ids=READY + OWED),
 dict(key="few", any=["still has a few"],'''),
]
DISMISS_ADD = (''' (["who has it", "whoever has to do the next thing"],''',
  ''' (["zm3d sound sources sheet", "sound sources sheet"], f"checked and consistent: Calvin's sheet was started on 12 Sep after Robert's copyright question of 10 Sep ({B['robert_copyright']}) and last edited on 26 Sep, after the vendor's list of 19 Sep; cue names from that list are later edits, which the sheet's modified time shows"),
 (["who has it", "whoever has to do the next thing"],''')

def apply(name, pairs):
    p = HERE / name; s = p.read_text(); done, skipped, missing = 0, 0, []
    for a, b in pairs:
        if s.count(a) == 1:
            s = s.replace(a, b); done += 1
        elif (b and b.split("\n")[0] in s) or (not b and a not in s):
            skipped += 1
        else:
            missing.append(a[:90])
    p.write_text(s)
    print(f"{name}: applied {done}, already {skipped}, missing {missing}")
apply("design_model.py", DM)
apply("build_surface.py", SURF)
apply("build_findings_map.py", FM + [DISMISS_ADD])
