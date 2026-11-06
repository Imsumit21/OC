"""Bring 08_OE_Check.md in line with the qualifier fixes made after the platform /oe NON-FAIL 3 (sha 3ddf0464).

Run from the workspace root after the final OE text is saved. Usage: python3 <this> <new OE sha12>
"""
import re, sys
from pathlib import Path

T = Path('Task_Authoring/task_inputs')
oe = (T / '08_Oracle_Events.md').read_text(encoding='utf-8')
p = T / 'Working_Files/08_OE_Check.md'
s = p.read_text(encoding='utf-8')
sha12 = sys.argv[1]
values = sys.argv[2] if len(sys.argv) > 2 else '798'
quotes = sys.argv[3] if len(sys.argv) > 3 else '191'

def rep(a, b, count=1):
    global s
    assert s.count(a) == count, (s.count(a), a[:90])
    s = s.replace(a, b)

rep('Checked 2026-11-05 · Events 35 · Characters 33519 (300', f'Checked 2026-11-06 · Events 35 · Characters {len(oe)} (300')
rep('(35 events, saved as the Evals `oe` input, sha256 3ddf04648bad)', f'(35 events, saved as the Evals `oe` input, sha256 {sha12})')
rep('with 764 Expected-line values ledgered, 0 absence claims, 0 unresolved (Evals/tools/hg_oe_review.py validate).',
    f'with {values} Expected-line values ledgered, 0 absence claims, 0 unresolved (Evals/tools/hg_oe_review.py validate). '
    'Platform history: Eval Portal /oe gave PASS 5 on sha 6be5f26b and NON-FAIL 3 (Accuracy 3) on sha 3ddf0464, whose only change was the heading dashes; '
    'the NON-FAIL came from a qualifier in OE 14 that both runs read, not from the dashes (plateform_report/6ae9909f7b5249d3148f3707_2_oe (1).md and (2).md). '
    'Findings 15 to 30 fix that qualifier, the three optional notes of the PASS report, and every further qualifier found by four blind hunts '
    '(GPT-6.1 Sol and Opus 5.5 redteam passes) and a narrow final check of the changed spans.')

# Inventory rows for the changed headings
rep("| OE 12  Pick out Leonard's per-ticket rulings and the art follow-ups among the comments from OE 11 |",
    "| OE 12  Pick out Leonard's per-ticket rulings and the art, UI-layout and animation follow-ups among the comments from OE 11 |")
rep("| OE 14  Pick out the latest checks on the open bugs that still fail with a blocker symptom |",
    "| OE 14  Pick out the open bugs whose latest report shows a blocker symptom, and which of them were re-checked on the candidates |")
rep("| OE 17  Pick out the comments that point to evidence elsewhere |",
    "| OE 17  Pick out the comments on the tickets whose call or build status another record settles |")
rep("| OE 18  Call the tickets filed on the candidates from their own reports. |",
    "| OE 18  Call the tickets filed on Sep 30 after the candidates were cut, which carry no QA comment, from their own reports. |")

FIND = [
 ('15', 'OE 14', 'Re-checked on the candidates and still failing', 'Eval 2.3 qualifiers (platform /oe on sha 3ddf0464)',
  'The header "the latest checks on the open bugs that still fail" grouped ZOM-559 (latest report on #133) and ZOM-293 (a July comment, no build) with candidate re-checks; the event now splits re-checked from not re-checked, names the build of each re-check, states the fixed rule as applied to two open tickets, and gives ZOM-293\'s description',
  'F18; cmt_zom559_1 (SQL L45), cmt_zom293_1 (SQL L87), SQL L60-L70; linear /issues ZOM-293'),
 ('16', 'OE 5', 'also counts as fixed if its fix is actually in the candidate builds (or live on prod), noted as not re-checked.', 'Platform PASS report, optional note 1',
  'The fixed rule skipped Leonard\'s Done-not-re-checked sentence; it is now quoted so the ZOM-569 reasoning in OE 25 is self-contained', 'F6; SQL L229'),
 ('17', 'OE 12', 'though ZOM-536 and ZOM-555 carry the Bug label and all three are Done', 'Platform PASS report, optional note 2; Eval 2.3 qualifiers',
  'The Bug label was stated for all three tickets, but ZOM-498 is labelled Improvement; the heading also called all three "art follow-ups"', 'F16; linear /issues ZOM-536, ZOM-555, ZOM-498; SQL L82-L84'),
 ('18', 'OE 16', 'although all three are still open in Linear (ZOM-429 and ZOM-517 Backlog, ZOM-564 Todo)', 'Platform PASS report, optional note 3',
  'Only two of the three were said to be open; ZOM-564 is Todo', 'F20; linear /issues ZOM-429, ZOM-517, ZOM-564'),
 ('19', 'OE 25', 'more than eight days before both Started lines', 'Eval 2.3 qualifiers',
  '"a week before" understated the gap (8 d 3-4 h); the close-time fallback is now quoted with its condition, the #1974 change is placed before both Started lines, #1759\'s time is labelled as its Changes post, and the #135 change "fix trampoline and glue count being set to 0 on game start" is shown not to be a re-check of ZOM-293',
  'F31, F32; SQL L257; C05433XK267/2025-09.json /902, /1124, /1131'),
 ('20', 'OE 33', 'the result of its latest check where there is one', 'Eval 2.3 qualifiers',
  '"each row has the result of its latest check" overstated: ZOM-559, ZOM-293 and ZOM-569 were not re-tested on #135 / #50 and NO CALL rows need no check', 'F38; SQL L31, L45, L87'),
 ('21', 'OE 27', 'the columns are "Area", "Fresh install - iOS #50 (iPhone 13)"', 'Eval 2.3 (lists exact)',
  'The column list left out "Area"', 'F34; SQL L261'),
 ('22', 'OE 7', 'open bugs not re-tested', 'Eval 2.3 qualifiers',
  'The n/a paraphrase dropped "open" from the not-re-tested branch, which would also take in Done bugs', 'F9; SQL L257'),
 ('23', 'OE 8', 'So ZOM-435 still fails on Android #135 (player stuck): a BLOCKER.', 'Eval 2.3 qualifiers',
  '"a BLOCKER on the candidates" claimed both builds; Leonard re-tested Android #135 only', 'F11; Trello 68dc63484a5b2d0a869e758f (SQL L278)'),
 ('24', 'OE 9', 'cut at 2025-09-22 12:30:43 UTC (Android #127) and 12:32:20 UTC (iOS #40)', 'Eval 2.3 qualifiers',
  'One cut time was given for both builds; iOS #40 started 97 seconds later', 'F12; C05433XK267/2025-09.json /692, /693'),
 ('25', 'OE 17', 'the comments on the tickets whose call or build status another record settles', 'Eval 2.3 qualifiers (group label)',
  '"comments that point to evidence elsewhere" included ZOM-562 and ZOM-473, whose comments name no other record; the closing sentence now says which record settles each', 'F21; SQL L66, L74'),
 ('26', 'OE 18', 'filed on Sep 30 after the candidates were cut', 'Eval 2.3 qualifiers (date window)',
  '"filed on the candidates ... Sep 29-30" was wider than the group (all ten were created 2025-09-30 20:40-22:50 UTC) and ZOM-575 names no build', 'F22; SQL L18-L27'),
 ('27', 'OE 20', 'in the boss arena the nuke went to a dead zombie', 'Eval 2.3 (translation of a quoted record)',
  'Two glosses said more or less than the quoted Turkish: the ZOM-535 gloss used words outside the quoted span (the quote now covers them) and the ZOM-473 gloss is now closer to "hala geçilebiliyor" / "x2 olmadan geldi"; the closing labels follow the records', 'F24, F25; SQL L120, L123-L125'),
 ('28', 'OE 29', 'the bottom boosts not visible', 'Eval 2.3 (lists exact)',
  'ZOM-424\'s symptom list dropped one of four symptoms and narrowed "the items I had" to equipped items', 'F36; linear /issues/3490'),
 ('29', 'OE 31', 'install TestFlight 50 over it, launch. Only one new ticket', 'Eval 2.6 / O1 (required write content)',
  'The new ticket\'s required content included a sentence citing the runbook row and the gate, which no record asks for', 'F33, F40; SQL L263-L274; page_qa_runbook'),
 ('30', 'OE 35', 'giving the QA call: NO-GO for Android Submission #135 and iOS Submission #50, because of the 19 blockers', 'Eval 2.6 / O1 (required write content)',
  'The reply\'s expected content read as requiring a register mention and the blocker count; the prompt asks for the QA call in the thread', 'F39, F41; SQL L32, L118'),
]
rows = ''.join(f'| {n} | RESOLVED (rewritten) | Accuracy | {ev} | {q} | {rule} | {what} | {evid} |\n' for n, ev, q, rule, what, evid in FIND)
assert s.count('\n\n## Pre-verdict sweep') == 1
i = s.index('\n\n## Pre-verdict sweep')
s = s[:i] + '\n' + rows.rstrip('\n') + s[i:]

COUNTER = [
 ('15', 'Counter-reading: "latest check" can cover ZOM-559\'s #133 report and ZOM-293\'s July comment, since each is the newest record on its ticket', 'The platform /oe (sha 3ddf0464) confirmed the header as a wrong qualifier because it said "still fail" on the candidates; cmt_zom559_1 names #133 (SQL L45) and cmt_zom293_1 names no build (SQL L87)'),
 ('16', 'Counter-reading: the extra sentence decides no row, so quoting it is noise', 'It explains why ZOM-569 (Done, not re-checked) is not FIXED: its fix is not in the candidate builds (OE 25, C05433XK267/2025-09.json /1129); SQL L229'),
 ('17', 'Counter-reading: "Bug label" was a paraphrase of Leonard\'s rule, not a claim about each ticket', 'The parenthetical sat on the three keys; linear /issues shows ZOM-498 labelled Improvement'),
 ('18', 'Counter-reading: naming two open tickets did not say ZOM-564 was closed', 'Listing only two as "still open" invites that reading; linear /issues ZOM-564 state Todo'),
 ('19', 'Counter-reading: "a week" is a round figure', 'The gap is 8 d 3 h 32 m to 8 d 4 h 50 m (linear completed_at vs ts 1759257812.041449); "more than eight days" is exact'),
 ('20', 'Counter-reading: an empty QA result is obviously fine for NO CALL rows', 'The sentence said "each row"; ZOM-569\'s only comment is a developer\'s branch note (SQL L31), which a run could copy as a check'),
 ('21', 'Counter-reading: "Area" is the row label, not a result column', 'SQL L261 grid_json header row lists six columns, "Area" first'),
 ('22', 'Counter-reading: the How we gate cell is the source either way, so the paraphrase does no harm', 'Without "open" the n/a branch overlaps the Done-bug branches of the same cell (SQL L257)'),
 ('23', 'Counter-reading: one failing candidate makes ZOM-435 a candidate blocker', 'The call is unchanged; the wording now names the build the re-test used (SQL L278 "android #135")'),
 ('24', 'Counter-reading: the earlier start is the cut that matters for the Done cutoff', 'Both times are now stated; the first Done move after either is 13:53:29Z, so the population is unchanged (linear /issues/3502)'),
 ('25', 'Counter-reading: every listed ticket needs another record, so the old label fit', 'The old label described the comments; ZOM-562\'s and ZOM-473\'s comments name no record (SQL L66, L74); the new label describes the tickets'),
 ('26', 'Counter-reading: ZOM-575 is in scope as a ticket filed during the gate whatever build it names', 'It stays in scope and NO CALL; the change only makes the header and date window match SQL L18-L27'),
 ('27', 'Counter-reading: glosses are aids, not Expected values', 'A gloss on a quoted record is read as a claim about it; the new quote (SQL L125) holds every word the gloss uses'),
 ('28', 'Counter-reading: three symptoms are enough to show ZOM-424 is a different bug', 'True, but a list presented as the record\'s list must be complete; linear /issues/3490 has four'),
 ('29', 'Counter-reading: citing the gate in the ticket is good practice', 'It may be written, but stating it as expected content makes it required; the runbook asks for device, OS version, source build and repro (page_qa_runbook)'),
 ('30', 'Counter-reading: a NO-GO without its reasons is a weak sign-off', 'The blockers stay as the stated basis of the call; the prompt and SQL L32 require the call as a thread reply'),
]
crow = ''.join(f'| Finding {n} resolved | {c} | {r} |\n' for n, c, r in COUNTER)
a = s.index('| Finding 14 resolved |')
b = s.index('\n', a) + 1
s = s[:b] + crow + s[b:]

rep('Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 4 · resolved 14',
    'Blocking 0 (incomplete 0 · inaccurate 0 · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor 0 · unresolved 0 · advisory 4 · resolved 30')
rep('oe_lint.py found 182 quoted spans verbatim in records', f'oe_lint.py found {int(quotes) - 2} of {quotes} quoted spans verbatim in records')
rep('returned PASS 5 / COMPLETE, 764 values, 0 unledgered.', f'returned PASS 5 / COMPLETE, {values} values, 0 unledgered.')
rep('4. Fixes: every rewritten span in Findings 1–14 was re-checked against its record in this run (oe_lint.py, O1).',
    '4. Fixes: every rewritten span in Findings 1–30 was re-checked against its record in this run (oe_lint.py, O1, the four qualifier hunts and the narrow final check of the changed spans).')
p.write_text(s, encoding='utf-8')
print('check updated', len(oe))
