"""Criterion text per plan row for owen_dd_bug_carryover, rebuilt on the /rubric round-1 Fix List (reviewed JSON 2ed7a6489798).
Keyed by the plan row's fact id. Fields: title, just, src (the evidence's Source line), srcs (catalog keys in assemble_rubric_draft.py),
acc (accepted outcomes for the V3 evidence), alt (the evidence's Reject line), accept (optional: the evidence's Accept text when the
Fix List sets it; otherwise the title without 'The Agent '), lock (optional: the reviewed row number whose title, category,
justification and evidence are copied byte for byte, so /rubric's DELTA lock holds), just_new (optional: a new justification on a
locked row whose weight the Fix List changed)."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TRUTH = json.load(open(os.path.join(os.path.dirname(HERE), "solver", "truth.json")))
T = {}


def t(fact, title, just, src, srcs, acc, alt, **kw):
    T[fact] = dict(title=title, just=just, src=src, srcs=srcs, acc=acc, alt=alt, **kw)


def line_of(key):
    s = TRUTH[key]["Bug"].replace(" ", " ")
    s = re.sub(r"^[☐☑]\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def ts_of(key):
    return TRUTH[key]["evidence"]["Outcome"][0].split("/")[-1]


def ckey(key):
    return "C_" + re.sub(r"[^A-Za-z0-9]+", "_", key).upper()[:40]


NOTES = "the carry-over notes f_3ca9e15d7b20f4e681ad52"
SHEET = "the DD carry-over sheet"
REPLY = "its reply to Arthur in his Feb 12 DM (D05S1S2AB5M)"
ANY = "the issue filed for that line or post is in {}, whatever its title"

# ---------------------------------------------------------------- the new tickets: template volume row and one sample per field
t("new_count", "The Agent files exactly 68 new issues for the DD bug carry-over, each in the Engineering team with the Bug label, parent ENG-2401, no assignee, an empty description and a title starting [2231]",
  "Multi-source: the count comes only from the full audit of 63 canvas lines and 7 posts and from Vincent's two ties (a Gmail message and a Linear comment); the template comes from the notes and Arthur's later comment on ENG-2401.",
  f"{NOTES} ('One Linear record per canvas line and one per bug posted after it'; 'Engineering team, Bug label, parent ENG-2401, title is the line without its tick box, or the first line of the post, as it was written, no assignee, nothing in the description'; Covered: 'Don't file a new one'); Arthur's comment on ENG-2401 comment_49b5ac4788465f72ddf245e34f2b7034 ('put [2231] at the front of every title you file'); Vincent's mail and ENG-2363 comment.",
  ["RULES", "AMEND", "APPLE", "SIGNIN"], ["68 new issues filed for the carry-over, each Engineering / Bug / parent ENG-2401 / no assignee / empty description / title starting [2231]"],
  "69 (a ticket for the Apple line) or 70 fails, and so do issues outside the template (another team, no Bug label, no parent, an assignee, a description, or no [2231]); a ticket for a deleted-line comment or a follow-up post makes the count wrong too.")
t("prefix:In profile", "The Agent starts the title of the issue for canvas line \"In profile,\" with \"[2231]\"",
  "Interpretation: the prefix comes from Arthur's later comment on the master ticket, which the notes point to ('If anything changes after this I'll put it on the master ticket').",
  f"Arthur's comment on ENG-2401 comment_49b5ac4788465f72ddf245e34f2b7034 ('put [2231] at the front of every title you file'); the ticked canvas line CE156FDFB428/{ts_of('In profile')}.",
  ["AMEND", ckey("In profile")], ["the In profile issue's title begins with [2231] (a space after it or not)"], "A title for that line without the [2231] prefix fails.")
t("titletext:flickering", "The Agent titles the issue it files for the flickering post with the post's line \"Any idea what might cause this flickering?\" word for word and no other words, with or without a [2231] prefix in front (\"[2231] Any idea what might cause this flickering?\", \"[2231]Any idea what might cause this flickering?\", \"[2231] - Any idea what might cause this flickering?\" and \"Any idea what might cause this flickering?\" all pass; any spacing or punctuation between the prefix and the line is fine)",
  "Lookup: the notes set the title as the first line of the post, as it was written.",
  f"{NOTES} ('title is the line without its tick box, or the first line of the post, as it was written'); the post C05V5FNLB9V/1764659550.713509.",
  ["RULES", "P_FLICK"], ["the post's line word for word with no other words, with or without a [2231] prefix and any spacing or punctuation after the prefix"],
  "A paraphrase ('Flickering on Android'), a title that adds words to the line ('Flickering: Any idea what might cause this flickering?') or one that drops words from it fails.")
t("team:music", "The Agent files the issue for the music post (\"My game started out without music…\") in the Engineering team",
  "Lookup: one sentence of the notes.", f"{NOTES} ('Engineering team'); the post C05V5FNLB9V/1764660142.352319.", ["RULES", "P_MUSIC"],
  ["the music post's issue in team Engineering / ENG"], "Another team (ZOM, the Zombie Match notes' team) fails.")
t("label:bar", "The Agent puts the Bug label on the issue for the bottom bar post (\"Hey … the bottom bar is not visible…\")",
  "Lookup: one sentence of the notes.", f"{NOTES} ('Bug label'); the post C05V5FNLB9V/1766415211.386389.", ["RULES", "P_BAR"],
  ["the bottom bar post's issue labelled Bug, alone or with other labels"], "An issue without the Bug label fails.")
t("parent:mega", "The Agent files the issue for the mega tile post with parent ENG-2401 (UI Changes Master Ticket)",
  "Lookup: one sentence of the notes.", f"{NOTES} ('parent ENG-2401'); the post C05V5FNLB9V/1764256187.655299.", ["RULES", "P_MEGA"],
  ["the mega tile post's issue with parent ENG-2401"], "No parent, or a group parent (ENG-2403, ENG-2404, ENG-2405), fails.")
t("assignee:top hud", "The Agent files the issue for canvas line \"top hud\" with no assignee",
  "Lookup: one sentence of the notes.", f"{NOTES} ('no assignee'); the ticked canvas line CE156FDFB428/{ts_of('top hud')}.", ["RULES", ckey("top hud")],
  ["the top hud issue with no assignee"], "An assignee (Owen or anyone else) fails.")
t("desc:In chapter selection", "The Agent files the issue for canvas line \"In chapter selection\" with an empty description",
  "Lookup: one sentence of the notes.", f"{NOTES} ('nothing in the description'); the ticked canvas line CE156FDFB428/{ts_of('In chapter selection')}.", ["RULES", ckey("In chapter selection")],
  ["the In chapter selection issue with an empty description"], "Any description text fails.")

# ---------------------------------------------------------------- the state of every new issue
for key, band, extra_src, keys, just, wrong in (
        ("offers has no visuals", 3, " and its thread's last reply CE156FDFB428/1763606525.993489 ('This should be fixed now')", ["OFFERS_CLOSE"],
         "Interpretation: the line's thread reopens ('the frame is gone for now') and closes on Arthur's 'This should be fixed now'; the tick stands.", "Canceled or Bugs fails."),
        ("Teams addressable doesn t work", 1, "", [], "Lookup: the tick on one canvas line stands.", "Canceled or Bugs fails."),
        ("top hud", 1, "", [], "Lookup: the tick on one canvas line stands.", "Canceled or Bugs fails."),
        ("Streak Fever has overflowing text on its pop up", 1, "", [], "Lookup: the tick on one canvas line stands.", "Canceled or Bugs fails."),
        ("Win & Collect gives a null ref every time", 3, "; the group DM C9CA62B5180A/1765927876.696389 ('event disabled')", ["WC"],
         "Interpretation: Win & Collect is disabled in the build, but the tick stands and the notes take Fixed before Gone.",
         "Canceled (Win & Collect being disabled) or Bugs fails, since Fixed comes first.")):
    t("state:" + key, f"The Agent files the issue for canvas line \"{line_of(key)}\" in the Done state", just,
      f"the ticked canvas line CE156FDFB428/{ts_of(key)}{extra_src}; {NOTES} ('Take the first outcome that fits. Fixed: the tick stands').",
      [ckey(key), "RULES"] + keys, [f"the issue for that line in Done, whatever its title"], wrong, accept=ANY.format("Done"))
t("state:navigation bar tooltips", "The Agent files the issue for canvas line \"navigation bar tooltips\" in the Done state",
  "Interpretation: the thread's last reply closes Brian's promised second fix.", "Vincent's reply CE156FDFB428/1763845512.559339 ('the 1 pixel gap is gone and the tooltips look right on my android now').",
  ["TIP"], ["the tooltips issue in Done, whatever its title"], "Bugs (reading Brian's 'I'll send another fix' as the end) fails.", accept=ANY.format("Done"))
t("state:tavern", "The Agent files the issue for canvas line \"Tavern buttons lost its frame.\" (it ends with a mention of Owen Baker) in the Bugs state",
  "Multi-source: a canvas tick and Brian's fix in its thread are overturned by Marcus's later DM in another conversation.",
  "Marcus's DM D05USBTQY1F/1765452012.418229 ('the Tavern buttons lost their frame again … Brian's fix didn't hold').", ["TAVERN"],
  ["the Tavern buttons issue in Bugs, whatever its title"], "Done (the tick and Brian's Nov 20 fix) fails.", accept=ANY.format("Bugs"))
t("state:shop", "The Agent files the issue for canvas line \"shops from rivertile and memory tile has weird shop icons (circular shapes entirely)\" in the Bugs state",
  "Multi-source: a canvas tick overturned by Brian's later reply under an unrelated post in another channel.",
  "Brian's reply C09Q4S613CN/1764606918.318209 ('the round icons on the River Tile and Memory Tile shops are there again on the current build, so don't trust that tick').", ["SHOP"],
  ["the shop icons issue in Bugs, whatever its title"], "Done fails.", accept=ANY.format("Bugs"))
t("state:vr_train", f"The Agent files the issue for canvas line \"{line_of('train level backgrounds are broken')}\" in the Bugs state",
  "Interpretation: Vincent's last reply outweighs the fix attempt earlier in the thread.", "Vincent's reply CE156FDFB428/1763845212.507119 ('the snow train is still off … leaving this one open').",
  ["TRAIN"], ["the train backgrounds issue in Bugs, whatever its title"], "Done (Arthur's 'fixed') fails.", accept=ANY.format("Bugs"))
t("state:vr_team", f"The Agent files the issue for canvas line \"{line_of('When I created a team and quitted it the')}\" in the Bugs state",
  "Interpretation: Vincent's reply says the fix covered only the leave-team popup.", "Vincent's reply CE156FDFB428/1763742012.611229 ('the navigation bar still goes after quitting').",
  ["TEAM"], ["the team-quit issue in Bugs, whatever its title"], "Done fails.", accept=ANY.format("Bugs"))
t("state:backend", f"The Agent files the issue for canvas line \"{line_of('When I lost a level I got some backend')}\" in the Bugs state",
  "Interpretation: an unticked line no later record closes, checked against the open tickets.", f"the unticked canvas line CE156FDFB428/1763042058.918579; {NOTES} ('stays open unless a later record says it was fixed').",
  ["C_BACKEND", "RULES"], ["the backend-errors issue in Bugs, whatever its title"], "Done, Canceled, or a note on ENG-2398 instead of a ticket fails.", accept=ANY.format("Bugs"))
for key, title, keys, just, src in (
        ("I found the issue lives are not decreased after", "The Agent files the issue for canvas line \"P.S I found the issue, lives are not decreased after a loss.\" (it ends with a mention of Arthur Blake) in the Canceled state",
         ["LIVES1", "LIVES"], "Multi-source: the line is not fixed and lives are gone from the economy-line build players have.",
         f"Vincent's reply and Leonard's Dec 2 update C09SWTHEMEW/1764659626.614679 ('We are removing lives feature from the game'); {NOTES} ('Gone … File it as Canceled')."),
        ("Lives are only decreased after losing twice in a", f"The Agent files the issue for canvas line \"{line_of('Lives are only decreased after losing twice in a')}\" in the Canceled state",
         ["LIVES2", "LIVES"], "Multi-source: the line is not fixed and lives are gone from the economy-line build players have.",
         f"Vincent's reply and Leonard's Dec 2 update C09SWTHEMEW/1764659626.614679 ('We are removing lives feature from the game'); {NOTES} ('Gone … File it as Canceled')."),
        ("When I change the character it just adds 1", f"The Agent files the issue for canvas line \"{line_of('When I change the character it just adds 1')}\" in the Canceled state",
         ["C_CHAR", "LIVES", "B2299"], "Multi-source: an unticked lives line against Leonard's lives removal in another channel and the economy-line build #2299.",
         f"the unticked canvas line CE156FDFB428/1763642659.467529; Leonard's Dec 2 update C09SWTHEMEW/1764659626.614679 ('We are removing lives feature from the game'); build #2299 C05433XK267/1765397569.397939; {NOTES} ('Gone … File it as Canceled').")):
    t("state:" + key, title, just, src, keys, ["the lives issue in Canceled, whatever its title"], "Bugs or Done fails.", accept=ANY.format("Canceled"))
for fact, title, just, src, keys, wrong in (
        ("state:tile dozer window background", "The Agent files the issue for the tile dozer window post (\"the tile dozer game background out of the window…\") in the Bugs state",
         "Multi-source: the deciding record sits outside the post's own thread.",
         "Marcus's 'Ok i fixed it and did a PR' C05V5FNLB9V/1764329192.159229; PR #1913 'Fixing window in tile dozer scene' open, not merged.", ["WINCLAIM", "PR1913"], "Done (Marcus's 'fixed it') fails."),
        ("state:mega tile missing a face", "The Agent files the issue for the mega tile post (it starts with a mention of Arthur Blake and \"i was playing trough the levels\") in the Bugs state",
         "Interpretation: the post's own last reply ('still happens on today's build') keeps it open.",
         "Marcus's reply C05V5FNLB9V/1764331830.705279 ('still happens on today's build').", ["MEGA"], "Done fails."),
        ("state:flickering", "The Agent files the issue for the flickering post (\"Any idea what might cause this flickering?\") in the Done state",
         "Multi-source: the deciding record sits outside the post's own thread.",
         "Robert's reply C09Q4S613CN/1766164222.418229 ('the flickering is gone on this week's build'); build #2297 on EconomyChanges lists the fix.", ["FLICK"], "Bugs (the thread ends at 'testing a fix now') fails."),
        ("state:music plays only sometimes", "The Agent files the issue for the music post (\"My game started out without music…\") in the Done state",
         "Multi-source: the deciding record sits outside the post's own thread.",
         "Brian's DM D07E9PSQB6W/1765206644.602119 ('music plays normally on my side since your audio player change'); build #2297 lists the URLAudioPlayer fix.", ["MUSIC"], "Bugs fails."),
        ("state:acid animation delay", "The Agent files the issue for the acid post (\"Animation is delayed for [PERSON_NAME_1711]'s acid…\") in the Done state",
         "Multi-source: Brian's DM line in another conversation ('Nate's acid throw lines up again') and the Nathan animation fix in build #2297 on the economy line.",
         "Brian's DM D07E9PSQB6W/1765206644.602119 ('Nate's acid throw lines up again after my animation fix'); build #2297 C05433XK267/1765310444.095399 ([PERSON_NAME_1711] is the post's own placeholder, kept as shown).", ["MUSIC", "B2297"], "Bugs fails."),
        ("state:treasure button opens axe arena", "The Agent files the issue for the treasure button post (\"After getting to stage 2 if [PERSON_NAME_1711]'s treasure, the button on home screen is bugged…\") in the Done state",
         "Multi-source: Brian's 'I send the fix' in the thread, commit fbe7bdea on develop and its merge into EconomyChanges (04d3118d).",
         "Brian's 'I send the fix' C05V5FNLB9V/1764694606.476379; commit fbe7bdea on develop, merged into EconomyChanges (04d3118d) ([PERSON_NAME_1711] is the post's own placeholder, kept as shown).", ["TREASURE"], "Bugs fails."),
        ("state:android bottom bar invisible", "The Agent files the issue for the bottom bar post (\"Hey … the bottom bar is not visible…\") in the Done state",
         "Multi-source: Brian's in-thread 'closing this one' after the camera fix, and PR #1916 merged into EconomyChanges.",
         "Brian's reply C05V5FNLB9V/1767021345.207719 ('the bottom bar and the top panel both show … closing this one'); PR #1916 merged into EconomyChanges.", ["BAR", "PR1916"], "Bugs fails.")):
    st = title.rsplit(" in the ", 1)[1].split(" ")[0]
    t(fact, title, just, src, keys, [f"the post's issue in {st}, whatever its title"], wrong, accept=ANY.format(st))
W3 = {"level completed text has no outline": ("Interpretation: the line's thread reopens after the Unity 6 update ('it's the same') and closes once the plugin update 'looks good'; the tick stands.",
                                              "; its thread's close CE156FDFB428/1763074145.483099 ('it looks good')", ["LC_CLOSE"]),
      "life balance timer in top HUD": ("Interpretation: lives are gone from the build players have, but the tick stands and the notes take Fixed before Gone.",
                                        "; Leonard's lives removal C09SWTHEMEW/1764659626.614679", ["LIVES"]),
      "Win & Collect Pop Up": ("Interpretation: Win & Collect is disabled in the build, but the tick stands and the notes take Fixed before Gone.",
                               "; the group DM C9CA62B5180A/1765927876.696389 ('event disabled')", ["WC"]),
      "initial reward of infinite lives beneath the overlay": ("Interpretation: lives are gone from the build players have, but the tick stands and the notes take Fixed before Gone.",
                                                               "; Leonard's lives removal C09SWTHEMEW/1764659626.614679", ["LIVES"]),
      "chapter 2 saga map has a weird artifact": ("Interpretation: the line's thread reopens ('not done') and closes when the pixels-per-unit fix is pushed; the tick stands.",
                                                  "; its thread's close CE156FDFB428/1763747143.093969 ('OK I pushed the fix')", ["SAGA_CLOSE"])}
DIRECT_DONE = {"offers has no visuals", "Teams addressable doesn t work", "top hud", "Streak Fever has overflowing text on its pop up", "Win & Collect gives a null ref every time"}
TICK47 = [k for k, v in TRUTH.items() if v.get("Why") == "the tick stands" and "fixed" in v.get("groups", []) and k not in DIRECT_DONE]
for key in TICK47:
    just, extra, keys = W3.get(key, ("Lookup: the tick on one canvas line stands.", "", []))
    tok = " (the bracketed token is the line's own placeholder, kept as shown)" if "[" in line_of(key) else ""
    t("state:" + key, f"The Agent files the issue for canvas line \"{line_of(key)}\" in the Done state", just,
      f"the ticked canvas line CE156FDFB428/{ts_of(key)}{extra}; {NOTES} ('Fixed: the tick stands'){tok}.", [ckey(key), "RULES"] + keys,
      ["the issue for that line in Done, whatever its title"], "Bugs or Canceled.", accept="Done")

# ---------------------------------------------------------------- Covered (locked)
t("covered:apple", "The Agent comments on ENG-2073 with the canvas line \"In general, I cannot sync and sign in with my Apple account\"",
  "Multi-source: a mail in Owen's inbox ties the canvas line to an open Linear ticket.",
  "Vincent's mail ('The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new'); ENG-2073 in Bugs.", ["APPLE", "ENG2073"],
  ["a new comment on ENG-2073 carrying the line's words (emoji codes free)"], "A new ticket for the line, or a paraphrase without the line's words, fails.", lock=29)
t("covered:signin", "The Agent comments on ENG-2363 with the canvas line \"On android, manual sign-in has an issue after the sign-in\"",
  "Multi-source: Vincent's Linear comment on another ticket ties the canvas line to it.",
  "Vincent's comment on ENG-2363 ('the manual sign-in line on my list gets stuck on loading after signing in, same thing as here'); ENG-2363 In Progress.", ["SIGNIN", "ENG2363"],
  ["a new comment on ENG-2363 carrying the line's words"], "A new ticket, or the note on ENG-2280, fails.", lock=30)

# ---------------------------------------------------------------- the UI tree
t("moves_count", "The Agent moves exactly 14 of the 28 UI children under ENG-2401 to Done",
  "Multi-source: each of the five holds rests on a different record (group DM, PR reviews, Linear comment, Brian's DM).",
  f"{NOTES} UI tree rule; holds: C9CA62B5180A/1765927876.696389, D07E9PSQB6W/1765471563.704419, ENG-2428 comment, D07E9PSQB6W/1765471651.208713.", ["RULES", "WC", "POPUPS", "SEASON", "GIFT"],
  ["14 children moved to Done"], "16 (the two popup children moved) or 19 fails.", lock=31)
SHOP_JUST = "Interpretation: Brian's shop-icon regression sits on this child's screen, and the notes' 'A bug on a screen doesn't hold its child' still moves it."
for k, name, lock, jn in (("ENG-2417", "Settings UI Optimization", 32, None), ("ENG-2418", "Level - win UI Optimization", 33, None), ("ENG-2433", "Memory Tile - UI Optimization", None, None),
                          ("ENG-2432", "River Tile - UI Optimization", 35, SHOP_JUST), ("ENG-2410", "Shop UI Optimization", 36, SHOP_JUST)):
    kw = {"lock": lock} if lock else {}
    if jn:
        kw["just_new"] = jn
    t("move:" + k, f"The Agent moves {k} ({name}) to Done",
      SHOP_JUST if k == "ENG-2433" else "Lookup: an open child with no record holding it.",
      f"{NOTES} ('every open child goes Done unless …'; 'A bug on a screen doesn't hold its child'); {k} open" + ("; Brian's reply C09Q4S613CN/1764606918.318209 (the round shop icons are back on the current build)." if k == "ENG-2433" else "."),
      ["RULES", "K_" + k] + (["SHOP"] if k == "ENG-2433" else []), [f"{k} in Done"], "Left open, or Canceled, fails.", **kw)
for k, name, just, src, srcs in (
        ("ENG-2434", "Tile Dozer", "Multi-source: Arthur's inline review on the merged PR #1905 and Brian's later DM keep the how-to-play popup's new sprites out of the build.",
         "Arthur's review comment on #1905 and Brian's DM D07E9PSQB6W/1765471563.704419 ('the Tile Dozer how-to-play popup still points at the old sprites'); the tree rule ('Then it stays where it is').", ["POPUPS", "INLINE_TD", "RULES"]),
        ("ENG-2426", "Axe Arena", "Multi-source: Arthur's inline review on the merged PR #1908 and Brian's later DM keep the info popup's new frame out of the build.",
         "Arthur's review comment on #1908 and Brian's DM D07E9PSQB6W/1765471563.704419 ('the Axe Arena info popup still has the old frame'); the tree rule ('Then it stays where it is').", ["POPUPS", "INLINE_AXE", "RULES"]),
        ("ENG-2424", "Collect&win - Magical Wings", "Multi-source: the economy-line group DM's 'event disabled' switches the screen off in the build players have, whatever the child's merged work says.",
         "the group DM C9CA62B5180A/1765927876.696389 ('event disabled'), after 'can you disable WC'; the tree rule ('or the screen is switched off there. Then it stays where it is').", ["WC", "RULES"]),
        ("ENG-2428", "Season Pass", "Multi-source: Oliver's comment on the child against its merged work and the tracker's status.",
         "Oliver's comment on ENG-2428 comment_d6aee2099bd71050facc422ccef8f809 ('the reward track still uses the old frames, this isn't finished'); the tree rule ('Then it stays where it is').", ["SEASON", "RULES"]),
        ("ENG-2437", "Daily Gift", "Multi-source: Brian's later DM line over his earlier plan and the tracker's status.",
         "Brian's DM D07E9PSQB6W/1765471651.208713 ('Daily Gift isn't finished either, the panel never got its last pass.'); the tree rule ('Then it stays where it is').", ["GIFT", "RULES"])):
    t("hold:" + k, f"The Agent comments on {k} ({name}) that the ticket stays open", just, src, srcs,
      [f"a new comment on {k} saying it stays open (held, not done, stays where it is)"], f"A comment calling {k} Done, or one that only names the build, fails; so does no comment.")
NAMES = {"ENG-2410": "Shop UI Optimization", "ENG-2411": "Character Section UI Optimization", "ENG-2412": "Saga map UI Optimization", "ENG-2413": "Teams UI Optimization",
         "ENG-2414": "Leaderboard UI Optimization", "ENG-2415": "Quest UI Optimization", "ENG-2416": "Profile Page UI Optimization", "ENG-2417": "Settings UI Optimization",
         "ENG-2418": "Level - win UI Optimization", "ENG-2419": "Level Lose - Out-of-moves Screens UI Optimization", "ENG-2420": "Chapter Section UI Optimization",
         "ENG-2421": "Tavern UI Optimization", "ENG-2422": "Pre-game Panel UI Optimization", "ENG-2423": "Transition Screens", "ENG-2424": "Collect&win - Magical Wings",
         "ENG-2425": "Nathan's Treasure - UI Optimization", "ENG-2426": "Axe Arena", "ENG-2427": "River Rush - UI Optimization", "ENG-2428": "Season Pass",
         "ENG-2429": "Remove Ad - UI Optimization", "ENG-2430": "Offers - UI Optimization", "ENG-2431": "Rate-us Pop-ups - UI Optimization", "ENG-2432": "River Tile - UI Optimization",
         "ENG-2433": "Memory Tile - UI Optimization", "ENG-2434": "Tile Dozer", "ENG-2435": "Lucky Drop - UI Optimization", "ENG-2437": "Daily Gift"}
for k, name in NAMES.items():
    t("line:" + k, f"The Agent names public build 0.3.310 in its comment on {k} ({name})",
      "Interpretation: Brian's closing rule (every child gets a note naming the current public build) and the notes' build number applied to this child.",
      f"Brian's closing rule on the DD Product Roadmap card (Trello action 690b29bc3c7d2e51b0f86a47: 'every one gets a note naming the current public build'); {NOTES} ('we go by the Android build players have, 0.3.310'; 'applies to the line on every child, Done or not'); {k}.",
      ["RULES", "K_" + k], [f"a new comment on {k} naming 0.3.310 (any form: 0.3.310, build 0.3.310, Android 0.3.310)"], f"A comment on {k} naming another build (develop's, or 0.3.305), or no comment, fails.")
t("line:ENG-2409", "The Agent leaves a comment naming 0.3.310 on ENG-2409 (Splash Screen UI Optimization, already Done)",
  "Lookup: the rule applied to one child that was Done before the run.", f"{NOTES} ('Done or not').", ["RULES", "K_ENG-2409"], ["a new comment on ENG-2409 naming 0.3.310"], "No comment on ENG-2409 fails.",
  lock=43, just_new="Interpretation: Brian's closing rule and the notes' build number applied to a child that was Done before the run.")

# ---------------------------------------------------------------- the sheet
t("sheet_folder", "The Agent puts a new Google Sheet in Owen's \"DD bug carry-over\" Drive folder",
  "Lookup: the folder the prompt names.", "Folder d_9b41e7c2a05d36f8e1c7a4 'DD bug carry-over', owned by Owen.", ["FOLDER"], ["a sheet whose parent is the DD bug carry-over folder"], "A sheet only in Owen's root fails.", lock=44)
t("sheet_columns", f"The Agent gives {SHEET} the columns Bug, Outcome, Ticket and Why",
  "Lookup: one sentence of the notes.", f"{NOTES} ('Sheet columns: Bug, Outcome, Ticket, Why.').", ["RULES"], ["a header row with Bug, Outcome, Ticket and Why (any order, extra columns allowed)"], "Status in place of Outcome fails.")
t("sheet_rows", f"The Agent lists exactly 70 bugs in {SHEET}",
  "Multi-source: the 70 come from the full audit of the canvas comment channel and the bug channel against the notes' scope tests (deleted lines, follow-ups, the QA-doc post and the design question are out).",
  f"{NOTES} ('One Linear record per canvas line and one per bug posted after it'; 'A comment whose line was deleted has nothing to carry over').", ["RULES"], ["70 bug rows below the header"], "76 (the six deleted-line comments) or fewer than 70 fails.")
t("sheet_ticket:sides", f"The Agent puts the key of the new issue it files for canvas line \"sides of event icons\" in the Ticket column of {SHEET}",
  "Lookup: the key of the run's own issue for one ticked line.",
  f"{NOTES} ('Sheet columns: Bug, Outcome, Ticket, Why.'); the ticked canvas line CE156FDFB428/{ts_of('sides of event icons')}; the key the run's issue for it gets.", ["RULES", ckey("sides of event icons")],
  ["the sides of event icons row's Ticket holding the run's issue key (or a link carrying it)"], "A blank Ticket cell, or another issue's key, fails.")
for fact, title, just, src, srcs, wrong in (
        ("sheet:tavern", f"The Agent records the Tavern buttons lost its frame line as Broken (or Bugs) in {SHEET}",
         "Multi-source: the canvas tick and Brian's fix in its thread are overturned by Marcus's later DM in another conversation.",
         "Marcus's DM D05USBTQY1F/1765452012.418229 ('the Tavern buttons lost their frame again on last night's Android build … Brian's fix didn't hold') over the ticked canvas line; the notes' 'Broken: anything else'.", ["TAVERN"], "Fixed or Done fails."),
        ("sheet:apple", f"The Agent records ENG-2073 as the ticket of the Apple sync line (In general, I cannot sync and sign in with my Apple account) in {SHEET}",
         "Multi-source: a mail in Owen's inbox ties the canvas line to ENG-2073, an open Linear ticket.",
         "Vincent's mail owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> ('same sync problem as ENG-2073'); ENG-2073 in Bugs.", ["APPLE", "ENG2073"], "A new issue's key fails."),
        ("sheet:signin", f"The Agent records ENG-2363 as the ticket of the manual sign-in line (On android, manual sign-in has an issue after the sign-in) in {SHEET}",
         "Multi-source: Vincent's Linear comment on another ticket ties the canvas line to ENG-2363.",
         "Vincent's comment on ENG-2363 comment_7ab5299cbb609d95ba12249d315daedc ('same thing as here'); ENG-2363 In Progress.", ["SIGNIN", "ENG2363"], "ENG-2280 or a new key fails."),
        ("sheet:window", f"The Agent records the tile dozer window post as Broken (or Bugs) in {SHEET}",
         "Multi-source: Marcus's 'fixed it and did a PR' in Slack against PR #1913 still open in GitHub.",
         "Marcus's reply C05V5FNLB9V/1764329192.159229 ('Ok i fixed it and did a PR'); PR #1913 'Fixing window in tile dozer scene' in harmonygames-Games/GameOfDominoes (state open, not merged); the notes ('A PR that never made it into that build doesn't count').", ["WINCLAIM", "PR1913"], "Fixed fails."),
        ("sheet:lives1", f"The Agent records the lives are not decreased after a loss line as Gone (or Canceled) in {SHEET}",
         "Multi-source: Vincent's reply in the line's thread, Leonard's lives removal and build #2299 on the economy line.",
         "Vincent's reply CE156FDFB428/1763845812.703339 ('a loss still doesn't take a life'); build #2299 C05433XK267/1765397569.397939 (lives removed on the economy line; Leonard's update C09SWTHEMEW/1764659626.614679); the notes' 'Gone … File it as Canceled'.", ["LIVES1", "B2299", "LIVES"], "Broken or Fixed fails.")):
    t(fact, title, just, src, srcs, [title.split("The Agent records ", 1)[1].rsplit(" in the DD", 1)[0]], wrong)
t("sheet_outcome:sides", f"The Agent records the sides of event icons line as Fixed (or Done) in {SHEET}",
  "Lookup: the tick on one canvas line stands.", f"the ticked canvas line CE156FDFB428/{ts_of('sides of event icons')}; {NOTES} ('Fixed: the tick stands').", [ckey("sides of event icons"), "RULES"],
  ["sides of event icons: Fixed (or Done)"], "Broken, Gone or Covered fails.")
t("sheet_outcome:apple", f"The Agent records the Apple sync line (In general, I cannot sync and sign in with my Apple account) as Covered in {SHEET}",
  "Multi-source: a mail in Owen's inbox ties the canvas line to ENG-2073, an open Linear ticket.",
  f"Vincent's mail owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> ('same sync problem as ENG-2073, no need for anything new'); ENG-2073 in Bugs; {NOTES} ('Covered: it isn't fixed and an open ticket already covers it').",
  ["APPLE", "ENG2073", "RULES"], ["the Apple sync line: Covered"], "Broken or Fixed fails.")
t("sheet_why:tavern", f"The Agent states in the Why cell of the Tavern buttons lost its frame line in {SHEET} that the buttons lost their frame again after Brian's fix",
  "Multi-source: Marcus's later DM in another conversation overturns the canvas tick and Brian's fix in the line's thread.",
  "Marcus's DM D05USBTQY1F/1765452012.418229 ('the Tavern buttons lost their frame again on last night's Android build … Brian's fix didn't hold').", ["TAVERN"],
  ["a Why saying the frame went again after Brian's fix (Marcus's DM), any wording"], "A Why saying the tick stands, or a blank Why, fails.")
t("sheet_why:sides", f"The Agent states in the Why cell of the sides of event icons line in {SHEET} that the line is ticked on the canvas",
  "Lookup: the tick on one canvas line.", f"the ticked canvas line CE156FDFB428/{ts_of('sides of event icons')}; {NOTES} ('Fixed: the tick stands').", [ckey("sides of event icons"), "RULES"],
  ["a Why saying the line is ticked (the tick stands), any wording"], "A blank Why fails.")

# ---------------------------------------------------------------- sharing
for e, who in (("arthur.blake@harmonygames.co", "Arthur Blake"), ("robert@harmonygames.co", "Robert"), ("oliver.brooks@harmonygames.co", "Oliver Brooks")):
    t("share:" + e, f"The Agent shares {SHEET} with {who} ({e}) in any role",
      "Lookup: one calendar event's attendees.", "Sunday's 'DD bug review' event evt_6e2c91d4b07f3a58c1d2e4 (attendees Arthur Blake, Robert, Oliver Brooks, Owen Baker).",
      ["EVT", "CT_" + who.split()[0].upper()], [f"{e} as reader, commenter or writer"], f"No permission for {e} fails.")

# ---------------------------------------------------------------- the reply
t("reply_thread", "The Agent replies to Arthur in the thread of his Feb 12 DM to Owen (D05S1S2AB5M)",
  "Lookup: the thread the prompt names.", "Arthur's DM D05S1S2AB5M/1770937805.214409.", ["HUB"], ["a reply in the thread under D05S1S2AB5M/1770937805.214409"],
  "A new top-level message in the DM, or a post in another channel, fails.")
t("reply_broken", f"The Agent tells Arthur in {REPLY} that 9 bugs are still broken",
  "Multi-source: the number joins every decision of the run.", "Arthur's DM ('tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done'); the notes' report-back rule ('When you report back, Covered ones count as still broken').",
  ["HUB", "RULES"], ["the reply states that 9 bugs are still broken"], "7 (the Broken items alone, leaving out the 2 Covered lines) or any other number fails.")
t("reply_new", f"The Agent tells Arthur in {REPLY} that it filed 68 new tickets",
  "Multi-source: the number joins every decision of the run.", "Arthur's DM ('tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done'); the notes' report-back rule.",
  ["HUB", "RULES"], ["the reply states it filed 68 new tickets"], "Any other number fails.", lock=59)
t("reply_done", f"The Agent tells Arthur in {REPLY} that 23 of the 28 UI children are Done",
  "Multi-source: the number joins every decision of the run.", "Arthur's DM ('tell me here how many are still broken, how many new tickets you filed and how many of the 28 UI children are Done'); the notes' report-back rule.",
  ["HUB", "RULES"], ["the reply states 23 of the 28 UI children are Done"], "Any other number fails.", lock=60)
t("reply_after_writes", "The Agent posts its reply to Arthur only after its Linear, sheet and share writes are finished (no ticket, comment, move, sheet or share write after it)",
  "Interpretation: the order of the run's writes; the prompt says 'Then reply'.", "the prompt ('Then reply to him in that DM thread').", ["HUB"], ["the reply is the run's last write"],
  "A reply posted before the tickets or the sheet fails.", lock=61, just_new="Lookup: the order of the run's writes; the prompt says 'Then reply'.")
