#!/usr/bin/env python3
"""One-off D3 / rev2 edit of plan/assemble_dossier.py: every passage that described the rev1 records of ARTHOLD (Claire's
Turkish DM), REVISED (the pull request deciding), EXPORT (the note's own wording) and ZIP (the word 'sound') now describes
the rev2 records. Idempotent: a passage already replaced is skipped; a passage neither found nor replaced is reported."""
from pathlib import Path
P = Path(__file__).resolve().parent / "assemble_dossier.py"
s = P.read_text()
E = [
 ('"""Assemble Working_Files/01_Grounding_Dossier.md (injection rev1, design D2.2) from',
  '"""Assemble Working_Files/01_Grounding_Dossier.md (injection rev2, design D3) from'),
 ('P.append(f"""# Grounding Dossier — {M.SLUG} · rev1 (design D2.2) · facts only, no prompt, OE or criterion text\n\nWritten by `/create-injection`',
  'P.append(f"""# Grounding Dossier — {M.SLUG} · {M.REV} (design {M.DESIGN}) · facts only, no prompt, OE or criterion text\n\n'
  '**rev2 (2026-11-12).** This revision implements design D3 (`01_Scenario_Design.md` §14), after the pre-check and the six-run baseline of rev1 '
  '(`01a_Hardening_Report.md`). Four seeded records change and nothing is added: Robert\'s note to Julia `{S["a2_dm"]["id"]}` replaces Claire\'s Turkish DM as the '
  'record on the bathroom redo; Marcus\'s post `{S["a1_post"]["id"]}` loses the words of the note it corrects; Brian\'s log `{S["c4_log"]["id"]}` says \'The .wav exports.\' '
  'instead of \'The sound files.\' and records that Claire sent the three recoloured models again, so Cactus Plant, Chainsaw and Cone are Ready. Truth moves from '
  '8 / 36 / 52 to {C["Delivered"]} / {C["Ready"]} / {C["Owed"]}. The rev1 SQL is kept in `Working_Files/run_forensics/rev1/` (with the bytes the platform ran in `submitted/`) and '
  'its design artifacts in `run_forensics/rev1/artifacts/`.\n\nWritten by `/create-injection`'),
 ('"three short posts at 18:12, 21:41 and 17:31 UTC, each in a gap of his base traffic (re-check B3)"',
  '"three short posts at 18:12, 21:41 and 17:31 UTC, each in a gap of his base traffic (re-check B3); in rev2 one note in his DM with Julia at 20:38 UTC on 29 Sep, before his base messages of 20:55 and 21:21, lower case, people tagged"'),
 ('"one Turkish message in her DM with Julia, lower case, opening \'kuzum\', English nouns (uv, level, ticket); the first reviewer read it as natural"',
  '"no seeded text in rev2 (the rev1 Turkish message is removed); she is tagged in Robert\'s note and in Marcus\'s post, and named in Brian\'s notes and log"'),
 ('    ("banyo", f"base hits in the same DM in 2023 (`{M.DM_CLAIRE}`) and in mail headers", f"Claire\'s message `{sid(\'a2_dm\')}`", "reading Julia\'s DM with Claire after 24 Sep"),',
  '    ("redoing the UVs", "NEW TERM — 0 base hits", f"Robert\'s note `{sid(\'a2_dm\')}`", f"reading Julia\'s DM with Robert `{M.DM_ROBERT}` around 29 Sep; a Slack search for \'bathroom\' also returns it among 57 visible base messages (no rev1 run searched the word)"),\n'
  '    ("three recoloured models", "NEW TERM — 0 base hits", f"Brian\'s log `{S[\'c4_log\'][\'id\']}`", "a Drive or Docs search for the outgoing folder; which three is in Robert\'s base post"),\n'
  '    (".wav exports", "NEW TERM — 0 base hits", f"Brian\'s log `{S[\'c4_log\'][\'id\']}`", "the same log (rev1\'s \'The sound files.\' made a search for \'sound\' list it)"),'),
 ('f"Julia is one of the two members of `{M.DM_CLAIRE}`"', 'f"Julia is one of the two members of `{M.DM_ROBERT}`"'),
 ('f"`{M.DM_CLAIRE}`", "chain C2; trap T2 (overturning)"', 'f"`{M.DM_ROBERT}`", "chain C2; trap T2 (overturning)"'),
 ('    ("ARTHOLD", f"Brian\'s note on twelve Bathroom tickets, e.g. {tick(\'Bathtub\')}", f"`{S[\'a2_dm\'][\'id\']}` (Claire, 29 Sep 12:15 UTC)", "same", "the artist herself, later; in Julia\'s own DM, in Turkish (OFF-PATH)"),\n'
  '    ("REVISED", f"Brian\'s note on {tick(\'Cactus Plant\')}, {tick(\'Chainsaw\')}, {tick(\'Cone\')} (25 Sep, about 08:05 UTC)", f"base `{B[\'pr462\']}` (created 11:43 UTC, merged 23:15 UTC that day)", "same", "the notes send a changed file again; the pull request\'s comment names the three models (OFF-PATH)"),',
  '    ("ARTHOLD", f"Brian\'s note on twelve Bathroom tickets, e.g. {tick(\'Bathtub\')}", f"`{S[\'a2_dm\'][\'id\']}` (Robert, 29 Sep 20:38 UTC)", "same", "someone who follows the art, later, in Julia\'s DM with him; the artist is tagged, not named (OFF-PATH)"),\n'
  '    ("REVISED", f"Robert\'s base post `{B[\'robert_new_colours\']}` (29 Sep 23:44 UTC): new colour versions of the cactus, the chainsaw and the cones, after their 25 Sep files; the notes send a changed file again", f"`{S[\'c4_log\'][\'id\']}` (Brian\'s log, 30 Sep): Claire sent the three recoloured models again, they open and look right", "the post sits in #zombie-design next to Robert\'s picks; every rev1 run read it", "the latest record; it says Ready, and only Robert\'s post says which three (OFF-PATH: the entry names no line)"),'),
 ('"Robert asked for the changes the night before; the files went to Brian before Claire made them"',
  '"Robert asked for the changes the night before; the files went to Brian before Claire made them; rev2: Robert shows the new versions on 29 Sep and Brian\'s log of 30 Sep records the re-send"'),
 ('Never named in the prompt: where the notes and the pack list live; any ticket key, channel, category or item; the three state words; any count; the six deciding records or their places (Marcus\'s post, Claire\'s message, the pul',
  'Never named in the prompt: where the notes and the pack list live; any ticket key, channel, category or item; the three state words; any count; the deciding records or their places (Marcus\'s post, Robert\'s note, the pul'),
 ('"seeded", f"Claire to Julia, 29 Sep 12:15 UTC, in Turkish: redoing the UVs of the bathroom objects; Friday\'s bathroom files are the old state. Decides {cls_count(\'A2\')} lines: Owed, Claire"',
  '"seeded", f"Robert to Julia, 29 Sep 20:38 UTC, in their DM: Claire (tagged) is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version. Decides {cls_count(\'A2\')} lines: Owed, Claire (the file came from her)"'),
 ('Owed by reason: {cls_count(\'VIS\')} on their own note, {cls_count(\'A1\')} text-kind files, {cls_count(\'A2\')} bathroom, {cls_count(\'C1\')} changed models, {cls_count(\'C4\')} in the broken zip, {cls_count(\'C2\')} sound cues.',
  'Owed by reason: {cls_count(\'VIS\')} on their own note, {cls_count(\'A1\')} text-kind files, {cls_count(\'A2\')} bathroom, {cls_count(\'C4\')} in the broken zip, {cls_count(\'C2\')} sound cues; the {cls_count(\'C1\')} recoloured lines are Ready (sent again, Brian\'s log).'),
 ('- Pre-check: confirm `github_get_pull_request_comments` returns the comment `{B[\'pr462_comment\']}` (the route relied on); `github_get_pull_request_files` is not relied on.',
  '- Pre-check: note whether the run looks in Drive for the outgoing folder (the route to Brian\'s log, which decides eleven lines: the eight zipped instruments and the three recoloured items); no route through GitHub is relied on in rev2.'),
 ('    ("Disagreement 2 (ARTHOLD)", "Claire handing over files and then calling them old is unrealistic.", f"she says she will note the tickets when the rework is done (`{S[\'a2_dm\'][\'id\']}`); she tells Julia because the old versions stay in her levels", "designed, resolved"),\n'
  '    ("Disagreement 3 (REVISED)", "The 08:05 note and the 11:43 pull request are the same morning: the file could already be the new one.", f"the pull request was created at 11:43 UTC and merged 23:15 UTC (`{B[\'pr462\']}`); Claire announced the push at 14:02 UTC (`{B[\'art_claire_pr\']}`); the note is three and a half hours earlier", "designed, resolved"),',
  '    ("Disagreement 2 (ARTHOLD)", "Robert passing on Claire\'s rework, rather than Claire herself, is unnatural.", f"Robert follows the art (his colourised items and new colour versions are base) and talks with Julia daily in `{M.DM_ROBERT}`; he tells her because the old versions show in her levels (`{S[\'a2_dm\'][\'id\']}`)", "designed, resolved"),\n'
  '    ("Disagreement 3 (REVISED)", "Robert\'s new colour versions and the log\'s \'replace Thursday\'s\' could be about different files.", f"Robert\'s post names the cactus, the chainsaw and the cones (`{B[\'robert_new_colours\']}`); the Thursday files from Claire of those three are the only Thursday files with a later change; the log entry is the next day and the latest record", "designed, resolved"),'),
 ('Left for the pre-check (Platform follow-ups): the two unverified bulk routes in Linear, the pull-request comment route, and the counted calls of a real run.',
  'Left for the pre-check (Platform follow-ups): the two unverified bulk routes in Linear, the Drive route to Brian\'s log, and the counted calls of a real run.'),
 ('- Mutation: four over-application operators are WEAK (their control line is not a sampled row); each has a written disposition in `01c_Dispositions.json`.',
  '- Mutation: three over-application operators are WEAK (their control line is not a sampled row); each has a written disposition in `01c_Dispositions.json`. REVISED\'s operator (Fly Zapper called Ready) is KILLED on the sampled control C2.'),
]
done, skipped, missing = 0, 0, []
for a, b in E:
    if s.count(a) == 1:
        s = s.replace(a, b); done += 1
    elif b in s:
        skipped += 1
    else:
        missing.append(a[:90])
P.write_text(s)
print(f"applied {done}, already applied {skipped}, missing {len(missing)}: {missing}")
