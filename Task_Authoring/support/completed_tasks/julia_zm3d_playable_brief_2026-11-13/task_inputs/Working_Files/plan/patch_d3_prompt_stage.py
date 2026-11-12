#!/usr/bin/env python3
"""One-off D3 / rev2 edit of the prompt-stage generators (brief_search.py, assemble_brief.py, assemble_humantime.py): the
discovery facts, counter-readings and trap rows that described rev1's records now describe rev2's. The prompt itself is
unchanged. Idempotent; prints what was applied and what was neither found nor applied."""
from pathlib import Path
HERE = Path(__file__).resolve().parent
EDITS = {
 "brief_search.py": [
  (' ("F9", "Marcus on Thursday\'s exports", "slack", "saved out of unity", S["a1_post"]["id"], "seeded"),',
   ' ("F9", "Marcus on Thursday\'s exports", "slack", "unity thursday", S["a1_post"]["id"], "seeded"),'),
  (' ("F10", "Claire on the bathroom files", "slack", "banyo", S["a2_dm"]["id"], "seeded"),',
   ' ("F10", "Robert on the bathroom files", "slack", "bathroom", S["a2_dm"]["id"], "seeded"),'),
  (' ("F11", "the recolour pull request", "github", "Objects Revisions", B["pr462"], "base"),',
   ' ("F11", "Robert\'s new colour versions", "slack", "new colored version", B["robert_new_colours"], "base"),'),
 ],
 "assemble_brief.py": [
  ("(Marcus {A1}, Claire {A2}, Brian's log {LOG}, Calvin's sheet {SHEET}, the pull request",
   "(Marcus {A1}, Robert's note {A2}, Brian's log {LOG}, Calvin's sheet {SHEET}; for the three recoloured lines Robert's base post and then Brian's log, which records the re-send; the pull request"),
  ('"met first for every line; overturned for 37 lines by F9 to F13"',
   '"met first for every line; overturned for 34 lines by F9, F10, F12 and F13; three more are overturned by F11 and restored by F13"'),
  ('"the models saved out of Unity on Thursday are the text kind; the ones from Claire are fine", A1,',
   '"the models Brian got out of Unity on Thursday are the text kind; the ones from Claire are fine", A1,'),
  (' ("F10", "Claire on the bathroom files", "she is redoing the UVs of the bathroom objects; Friday\'s bathroom files are the old state", A2, "YES (DM member)", "overturns twelve of F5", "in T',
   ' ("F10", "Robert on the bathroom files", "Claire is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version", A2, "YES (DM member)", "overturns twelve of F5", "in Julia\'s DM with Robert, a person who owns neither the list nor the notes; Claire and Brian are tagged, not named", "No, never: it is a finding"),\n ("F10x", "rev1 wording (removed)", "rev1 had Claire\'s own Turkish DM here", A2, "YES (DM member)", "superseded", "in T'),
  (' ("F11", "the recolour pull request", "\'Objects Revisions and Changes\', created 25 Sep 11:43 UTC, merged 23:15 UTC; its comment names the chainsaw, cactus and cone models", B["pr462"], "YE',
   ' ("F11", "Robert\'s new colour versions", "new coloured versions of the cactus, the chainsaw and the cones, 29 Sep, after their 25 Sep files", B["robert_new_colours"], "YES (channel member)", "overturns three of F5; F13 restores them", "met with Robert\'s picks in #zombie-design", "No, never: it is a finding"),\n ("F11x", "rev1 record (not needed)", "the pull request behind the colour change", B["pr462"], "YE'),
  ('"the zip with Friday\'s music instruments will not unpack and those eight are not in the folder any other way", LOG, "YES (shared reader)", "o',
   '"the zip with Friday\'s music instruments will not unpack and those eight are not in the folder any other way; Claire sent the three recoloured models again, they open and look right", LOG, "YES (shared reader)", "o'),
  ('    ("Claire\'s message", f"{S[\'a2_dm\'][\'at\']} = {pt(S[\'a2_dm\'][\'at\'])}", f"`{A2}`", "past fact"),',
   '    ("Robert\'s note on the bathroom objects", f"{S[\'a2_dm\'][\'at\']} = {pt(S[\'a2_dm\'][\'at\'])}", f"`{A2}`", "past fact"),'),
  ("({A1}, {A2}, {B['pr462']}, {SHEET}, {REPLY}, {LOG}), each met second", "({A1}, {A2}, {B['robert_new_colours']} then {LOG}, {SHEET}, {REPLY}), each met second"),
  ("(Marcus's post, Claire's message, the pull request, Calvin'", "(Marcus's post, Robert's note, Robert's colour post with Brian's log, Calvin'"),
  ('("Fair outcomes (accepted outcomes)", "Who has the three recoloured lines could be Brian or Claire."',
   '("Fair outcomes (accepted outcomes)", "Who has the twelve bathroom lines could be Robert (he wrote the note), Brian or Claire."'),
  ("eight zipped instruments, three recoloured models, two library sounds): rejec", "eight zipped instruments, two library sounds): rejec"),
  ('"Brian as holder of the recoloured lines: rejected, the notes say a changed file sits with whoever it came from",',
   '"Robert or Brian as holder of the bathroom lines: rejected, the notes say a changed file sits with whoever it came from, and the twelve notes say FBX from Claire",\n        "the three recoloured lines Owed on Robert\'s 29 Sep post alone: rejected, Brian\'s log of 30 Sep says Claire sent them again and they open and look right",'),
 ],
 "assemble_humantime.py": [
  ('("T2 Friday\'s bathroom files look ready until the artist\'s message", "dead end"', '("T2 Friday\'s bathroom files look ready until Robert\'s note", "dead end"'),
  ('("T3 three recoloured models: the note is older than the change", "dead end", f"{over[\'C1\']} tickets, 1 pull request with its comment", "15 min on top of the PR search", 15),',
   '("T3 three recoloured models: Owed on Robert\'s post until the log says they went again", "dead end", f"{over[\'C1\']} tickets, Robert\'s post, the log entry", "15 min", 15),'),
 ],
}
for name, pairs in EDITS.items():
    p = HERE / name; s = p.read_text(); done, skipped, missing = 0, 0, []
    for a, b in pairs:
        if s.count(a) == 1:
            s = s.replace(a, b); done += 1
        elif b.split("\n")[0] in s:
            skipped += 1
        else:
            missing.append(a[:90])
    p.write_text(s)
    print(f"{name}: applied {done}, already {skipped}, missing {missing}")
