"""Round 2 rubric: applies the /rubric r1 Fix List (Audit-Report/3_rubric_FAIL_r1.md) to the r1 draft.

Writes task_inputs/09_Rubrics.json (68 criteria) and Working_Files/09_Rubrics.draft_with_plan_ids.json
(same rows plus plan_row, r1 row and the counter-reading used by build_rubcheck_r2.py).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
R1 = json.load(open(os.path.join(HERE, 'rubric_r1_base.json')))

CARD = "Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383"
ASKR = "Leonard's reply under the ask, D05HB64NMQU/1759262838.442871"
SEPR = "Leonard's reply under Julia's Sep 29 question, D05HB64NMQU/1759267002.665190"
NOTES = "Leonard's 'notes for monday' doc f_f494073fc667097c3c2c6b"
PR265 = "Blake's review comment harmonygames-Games/match3d#265#rc_7"
MAIL = "Blake's 'store builds for monday' mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>"
ASK = "Leonard's ask in the DM, D05HB64NMQU/1759261706.530914"
LIN = "team ZOM issues created up to Aug 31 and their closing notes"
LIVE = "Live tab of the 'ZM monster enrage' sheet f_0ba93ae0238d9ed4178212"
Z42 = "ZOM-42 description"
CODE = "match3d Assets/Scripts/DynamicDifficulty/TierManager.cs (totalGames == 10, cpm > 90.0f) and Player/WinHistory.cs"
BREPLY = "Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"
CHECK = "the card's 'Before Monday' checklist 68dc033bf7d24e86b8a9cc67"
INVITE = "the tuning invite evt_91674a9c23d012a9ac34da"
FOLDER = "the ZM Difficulty folder d_96489e1e00a56685625939"
AGENDA = "agenda doc 'ZM difficulty tuning - Oct 6' f_9ec79682ff351aa466364a"
N282 = "ZOM-282's closing note cmt_912bdd42ad5c8d51521f"
VINCENT = "Vincent's #zombie-design message C090N54TG79/1759248760.118527"
DOMINO = "Domino Delights card 683dbef4e319167a802bd888"
REG = f"{CARD}, rules 1-7; {ASKR}; {SEPR}; {NOTES}; {PR265}; {MAIL}"
T = "on the Tickets tab of the ZM difficulty baseline register"
RT = "on the Rules in force tab of the ZM difficulty baseline register"
TIER_OK = ("passes: wording that counts 10 games, attempts or plays, or a count of levels that says losses or replays count, with or without a CPM average over the first 10 levels beside it; fails: a count of levels with nothing saying losses or replays count ('after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'), 'after level 10', 'once level 10 is cleared', or only a CPM average over the first 10 levels with no timing")

OUT = []


def row(r1, title, w, just, ev, cr, cat='Outcome'):
    OUT.append(dict(title=title, category=cat, weight=w, justification=just, evidence=ev,
                    plan_row=(f"P{r1}" if r1 else "new"), r1=(f"R{r1}" if r1 else "added"), cr=cr))


def keep(r1, w=None, title=None, just=None, ev=None, cr=''):
    o = R1[r1 - 1]
    row(r1, title or o['title'], w or o['weight'], just or o['justification'], ev or o['evidence'], cr)


# --- register artifact
keep(1, just=f"Lookup — the agenda says 'One sheet with two tabs' ({AGENDA.split()[-1]}); a sheet is the named artifact, so any title passes.",
     cr="a run that adds the tabs to an existing sheet — the agenda asks for a new sheet")
row(2, "The Agent gives the ZM difficulty baseline register a tab named Tickets (a tab name containing the word Tickets passes)", 1,
    "Lookup — the agenda names the Tickets tab.", f"Sources: {AGENDA}. Accept: a tab whose name contains Tickets.",
    "a tab named 'Ticket list' — contains Tickets, passes")
row(2, "The Agent gives the ZM difficulty baseline register a tab named Rules in force (a tab name containing the word Rules passes)", 1,
    "Lookup — the agenda names the Rules in force tab.", f"Sources: {AGENDA}. Accept: a tab whose name contains Rules.",
    "a tab named 'Rules' — contains Rules, passes")
row(3, "The Agent places the ZM difficulty baseline register in the ZM Difficulty folder in Google Drive (created there or moved there)", 1,
    "Lookup — the prompt and card rule 7 name the folder; the row grades the file's parent folder.",
    f"Sources: {FOLDER}; {CARD}, rule 7. Accept: parent folder d_96489e1e00a56685625939, whether created there or moved there.",
    "created in My Drive and moved later — passes on the end state")
row(4, f"The Agent fills the Tickets tab of the ZM difficulty baseline register with exactly 24 ticket rows with a status of Live, Editor only, Replaced or Not shipped (left-off tickets listed without one of these statuses are not counted)", 5,
    "Multi-source — the count follows only from the title scan, the 'tiers:' notes, the attack-power amendment, both DM thread replies, the notes doc and the PR 265 review.",
    f"Sources: {REG}. Accept: exactly 24 rows carrying Live, Editor only, Replaced or Not shipped; rows for left-off tickets without one of these statuses are not counted.",
    "a run keeping 34 or 35 rows with statuses fails; a left-off list with no statuses does not count against it")
row(5, f"The Agent records exactly 16 tickets with the status Live {T}", 5,
    f"Multi-source — needs every scope cut and every status call; Leonard's reply D05HB64NMQU/1759262838.442871 drops the six analytics and tutorial tickets, which leaves 16 Live.",
    f"Sources: {REG}. Accept: exactly 16 rows with status Live.", "22 Live (no thread replies read) fails")
row(6, f"The Agent records exactly 4 tickets with the status Editor only {T}", 5,
    f"Multi-source — Blake's mail, the closing notes and the Sep 30 21:16 reply; Leonard's reply D05HB64NMQU/1759267002.665190 takes four tickets off the list, leaving ZOM-173, 200, 277 and 315 as Editor only.",
    f"Sources: {REG}. Accept: exactly 4 rows with status Editor only.", "8 or 9 Editor only rows fail")

# --- Live samples (5) + statuses
LIVEJ = f"store builds mail {MAIL.split()[-1]} strips only editor and debug folders."
keep(19, just=f"Interpretation — tag-only member ('tiers:' closing note) with no title keyword; the {LIVEJ}",
     cr="a run that leaves tag-only tickets out — fails, as rule 1 counts the 'tiers:' notes")
row(None, f"The Agent records the status Live for ZOM-42 {T}", 1,
    f"Lookup — card rule 4 says 'ZOM-42 is the system itself: it stays Live' ({CARD.split()[-1]}).",
    f"Sources: {CARD}, rule 4. Accept: 'ZOM-42' Live.", "ZOM-42 marked Replaced by a later tier ticket — fails rule 4")
keep(21, just=f"Interpretation — member through the attack-power amendment on the card; the {LIVEJ}", cr="")
keep(22, just=f"Interpretation — PR 401 split its values, which does not make it Replaced (rule 4); the {LIVEJ}", cr="")
keep(23, just=f"Interpretation — an editor label that the game also reads at runtime; the {LIVEJ}", cr="")
for r in (24, 25, 26, 27):
    keep(r, cr="")
for r in (28, 29, 30):
    keep(r, cr="")
row(31, f"The Agent records ZOM-254 as Replaced, with ZOM-282 (Optimize enrage mechanic for speed and attack damage only) as the ticket that replaced it, {T} (naming ZOM-282 by key or by that title passes)", 3,
    f"Interpretation — {N282} says it replaces ZOM-254 (rule 4). Status and replacing ticket are coupled attributes of one row.",
    f"Sources: {LIN}; {N282}. Accept: 'ZOM-254' Replaced, replaced by 'ZOM-282' or 'Optimize enrage mechanic for speed and attack damage only'.",
    "ZOM-254 marked Live — fails")
keep(32, cr="")
row(None, f"The Agent records ZOM-254's title, Blunder Mechanic 2.0 enrages zombies instead of HP penalty, {T} (any letter case)", 1,
    "Lookup — rule 2 lists a title column; one Linear field.",
    f"Sources: {LIN}; {CARD}, rule 2. Accept: 'Blunder Mechanic 2.0 enrages zombies instead of HP penalty' in any letter case.",
    "a shortened title — fails; the row names the full title")
row(None, f"The Agent records ZOM-280's Linear state as Canceled {T} (Cancelled also passes)", 1,
    "Lookup — rule 2 'Linear state (as you found it)'; one Linear field, the non-Done edge of the column.",
    f"Sources: {LIN}; {CARD}, rule 2. Accept: 'ZOM-280' Canceled or Cancelled.", "'Not shipped' written in the state column — fails")

# --- Rules in force
row(33, f"The Agent states {RT} that a new player's starting tier is set once they have played 10 games ({TIER_OK})", 5,
    "Multi-source — the build over ZOM-42, ZOM-199 and the deck, under rule 5 'go by the build'.",
    f"Sources: {CODE}; {CARD}, rule 5. Accept: {TIER_OK}.",
    "'after the first 10 levels played' — passes; 'once they finish level 10' — fails")
row(34, f"The Agent states {RT} that a new player starts on tier 1 only when their average CPM is above 90 (any wording that the threshold is strictly above 90 passes, with or without saying the build does not use >= 90; giving the threshold as '90 or more' or '>= 90' fails)", 3,
    "Comparison — Blake's reply and the build over ZOM-199 and the deck.",
    f"Sources: {BREPLY}; {CODE}. Accept: any wording that the threshold is strictly above 90, with or without saying the build does not use >= 90; giving the threshold as '90 or more' or '>= 90' fails.",
    "'90 or more' (ZOM-199) — fails")
WIN = "any wording of a window of the last 10 {u}, with or without 'up to', passes"
row(35, f"The Agent states {RT} that a player is promoted at a win rate of 80% or more over their last 10 attempts ({WIN.format(u='attempts or games')})", 1,
    "Lookup — one ZOM-42 sentence, which words the window both ways.",
    f"Sources: {Z42}. Accept: 80% or more; {WIN.format(u='attempts or games')}.", "'last 10 levels won' — fails, wrong window")
keep(36, just="Lookup — one ZOM-42 sentence.", cr="")
keep(37, just="Lookup — one ZOM-42 sentence, also in the deck.", cr="")
row(38, f"The Agent states {RT} that a player is demoted at a win rate of 50% or lower over their last 10 games ({WIN.format(u='games or attempts')})", 1,
    "Lookup — one ZOM-42 sentence; the deck omits it.",
    f"Sources: {Z42}. Accept: 50% or lower; {WIN.format(u='games or attempts')}.", "a run naming only the 4-loss demotion — fails")
keep(39, just="Lookup — one ZOM-42 sentence.", cr="")
row(40, f"The Agent states {RT} that after a demotion the level the player is on also drops in difficulty (that level dropping with no amount stated, or by one tier, passes; any other stated amount fails)", 1,
    "Lookup — rule 5 asks whether the level drops; ZOM-303's solution sentence answers it.",
    f"Sources: ZOM-303 description; {CARD}, rule 5. Accept: the level drops, with no amount or by one tier; any other stated amount fails.",
    "'yes, the level drops' with no amount — passes")
row(41, f"The Agent records {RT} Boxer's enrage values as speed 0.5 and damage 0.4", 1,
    "Lookup — one Live-tab row copied as it stands.", f"Sources: {LIVE}. Accept: Boxer speed 0.5, damage 0.4.", "the deck's +25% — fails")
row(42, f"The Agent records {RT} MonsterBase's enrage values as speed 0.8 and damage 0.8", 1,
    "Lookup — one Live-tab row, not the Next pass proposal.", f"Sources: {LIVE}. Accept: MonsterBase speed 0.8, damage 0.8.",
    "Next pass 0.3/0.8 — fails")
keep(43, just="Lookup — one Live-tab row copied as it stands.", ev=f"Sources: {LIVE}. Accept: Plumber speed 0.3, damage 0.3.", cr="")
row(44, f"The Agent states {RT} that enrage's hp boost is 0 or switched off", 1,
    "Lookup — the Live tab's hp column and ZOM-282's closing note.",
    f"Sources: {LIVE}; {N282}. Accept: hp boost 0, off or none.", "the deck's +25% max HP — fails")
row(45, f"The Agent lists enrage speed and damage values for exactly 10 monster entries {RT} (a monster whose variants are split over several rows counts once; Mailman, Mayor2 and PartyGirl are not counted)", 1,
    "Lookup — rule 5 copies the Live tab as it stands; it already holds exactly 10 valued entries with the variants merged.",
    f"Sources: {LIVE}. Accept: exactly 10 monster entries with speed and damage values; variant rows of one monster count once; Mailman, Mayor2 and PartyGirl are not counted.",
    "Magician split into three variant rows — counts once, passes")
row(None, f"The Agent lists Mailman, Mayor2 and PartyGirl {RT} with their enrage speed and damage marked as not copied yet (any wording that their values have not been copied yet passes; one combined row or one row per monster passes)", 1,
    "Lookup — rule 5: 'a monster it hasn't copied yet goes on the tab as not copied yet'; one Live-tab row.",
    f"Sources: {LIVE}; {CARD}, rule 5. Accept: Mailman, Mayor2 and PartyGirl listed with values marked not copied yet, in one row or three.",
    "the three monsters left off the tab — fails")

# --- shares
keep(46, cr="")
keep(47, cr="")
row(48, "The Agent shares the ZM difficulty baseline register with Leonard Hayes (leonard.hayes@harmonygames.co) with commenter access (his access as owner of the ZM Difficulty folder also passes)", 1,
    "Lookup — rule 7 'everyone else comments'; Leonard owns the folder.",
    f"Sources: {INVITE}; {CARD}, rule 7; {FOLDER}. Accept: leonard.hayes@harmonygames.co commenter, or his access as owner of the ZM Difficulty folder.",
    "Leonard as editor — fails")
keep(49, cr="")
row(None, "The Agent shares the ZM difficulty baseline register with exactly three people other than Leonard Hayes (Julia Lawson, the owner, is not counted)", 1,
    "Lookup — the tuning invite lists the three others; the count guards against extra people.",
    f"Sources: {INVITE}; {DOMINO}. Accept: exactly 3 people other than Leonard Hayes and Julia Lawson.",
    "Vincent added from the Domino Delights card — fails")

# --- Linear comments
row(50, "The Agent adds a new comment on Linear issue ZOM-199 saying the build's starting-tier check is an average CPM strictly above 90 (> 90), with or without mentioning >= 90", 3,
    "Comparison — Blake's reply against the ticket text; rule 6 comments on the ticket whose text is wrong.",
    f"Sources: {BREPLY}; {CARD}, rule 6. Accept: 'ZOM-199' comment saying the check is strictly above 90 (> 90), with or without >= 90.",
    "a comment saying '>= 90' is right — fails")
keep(51, ev=f"Sources: {N282}; {CARD}, rule 6. Accept: 'ZOM-254' comment naming 'ZOM-282'.", cr="")
CL = ("Interpretation — the checklist's rule 6 change applied to a register status: 'the Editor only and Not shipped tickets get a "
      "comment too' (68dc033bf7d24e86b8a9cc67).")
for r in (52, 53, 54, 55, 56):
    keep(r, just=CL, cr="")
for k in ("ZOM-315", "ZOM-293"):
    row(None, f"The Agent adds a new comment on Linear issue {k} saying its change is missing from the store builds (any wording that the store builds lack the change passes)", 3,
        CL, f"Sources: {CHECK}; {MAIL}. Accept: '{k}' comment saying the change is not in the store builds, any wording.",
        "no comment on the ticket — fails")
keep(57, just="Multi-source — rule 6 plus the checklist, minus the four tickets Leonard's reply D05HB64NMQU/1759267002.665190 drops: ZOM-199, ZOM-254 and the seven Editor only and Not shipped tickets.",
     ev=f"Sources: {CARD}, rule 6; {CHECK}; {SEPR}. Accept: exactly 9 ZOM tickets with a new comment.", cr="")

# --- DM reply
DMJ = "the ask requires the counts in the reply; the register is a second required deliverable."
row(59, "The Agent states in its DM reply to Leonard that 24 tickets made the list", 5,
    f"Multi-source — the register count after both thread replies; {DMJ}", f"Sources: {REG}; {ASK}. Accept: 24 tickets.", "35 — fails")
row(60, "The Agent states in its DM reply to Leonard that 16 tickets are Live", 5,
    f"Multi-source — the Live count after both thread replies; {DMJ}", f"Sources: {REG}. Accept: 16 Live.", "22 Live — fails")
row(61, "The Agent states in its DM reply to Leonard that 4 tickets are Editor only", 5,
    f"Multi-source — the Editor only count after the Sep 30 21:16 reply and the PR 265 review; {DMJ}",
    f"Sources: {REG}. Accept: 4 Editor only.", "9 Editor only — fails")
row(62, "The Agent states in its DM reply to Leonard that 3 tickets are Not shipped", 3,
    f"Interpretation — three open or cancelled tickets under rule 1; {DMJ}",
    f"Sources: {CARD}, rule 1; {LIN}. Accept: 3 Not shipped.", "")
row(63, "The Agent states in its DM reply to Leonard that 1 ticket is Replaced", 3,
    f"Interpretation — one Replaced row under rule 4; {DMJ}", f"Sources: {CARD}, rule 4; {N282}. Accept: 1 Replaced.", "")
for r, k in ((64, 'ZOM-202'), (65, 'ZOM-280'), (66, 'ZOM-293')):
    row(r, f"The Agent names {k} in its DM reply to Leonard as a Not shipped ticket", 1,
        "Lookup — Leonard's thread reply asks for 'the keys of the not shipped ones'; an open or cancelled Linear state.",
        f"Sources: {ASKR}; {LIN}. Accept: '{k}' Not shipped.", "")
for r, k in ((67, 'ZOM-173'), (68, 'ZOM-200'), (69, 'ZOM-277'), (70, 'ZOM-315')):
    row(r, f"The Agent names {k} in its DM reply to Leonard as an Editor only ticket", 3,
        f"Interpretation — Leonard's thread reply asks for 'the editor only ones'; the store builds mail {MAIL.split()[-1]} decides the status.",
        f"Sources: {ASKR}; {MAIL}. Accept: '{k}' Editor only.", "")
keep(72, ev=f"Sources: {NOTES}; {N282}. Accept: 'ZOM-254' replaced by 'ZOM-282'.", cr="")
row(73, f"The Agent tells Leonard in its DM reply that a new player's starting tier is set once they have played 10 games ({TIER_OK})", 5,
    "Multi-source — the build over ZOM-42, ZOM-199 and the deck (rule 5); Leonard's ask names the question.",
    f"Sources: {CODE}; {ASK}. Accept: {TIER_OK}.",
    "'10 games played, not 10 levels beaten' — passes; 'after level 10' — fails")
row(None, "The Agent posts Slack messages in exactly one Slack channel or DM (several threads or top-level messages in the same DM count as one)", 1,
    "Lookup — the ask says 'reply here'; the count guards against Vincent's request.",
    f"Sources: {ASK}; {VINCENT}. Accept: Slack messages in exactly one channel or DM.", "a copy posted in #zombie-design — fails")
row(None, "The Agent sends its DM reply to Leonard after the last step that creates or moves the ZM difficulty baseline register (only the order of these steps is graded)", 1,
    "Lookup — the ask: 'reply here when it's in the folder'; only the order is graded.",
    f"Sources: {ASK}. Accept: the DM reply is sent after the register's final create or move step.",
    "a reply sent before the move — fails", cat='Process')

import re
for c in OUT:
    for k in ('title', 'justification', 'evidence'):
        v = re.sub(r'^(Lookup|Interpretation|Multi-source|Comparison) \u2014 ', r'\1: ', c[k])
        c[k] = v.replace(' \u2014 ', '; ').replace('\u2014', ', ').replace('\u2013', '-')
        assert '\u2014' not in c[k] and '\u2013' not in c[k]
assert len(OUT) == 68, len(OUT)
json.dump([{k: c[k] for k in ('title', 'category', 'weight', 'justification', 'evidence')} for c in OUT],
          open(os.path.join(TI, '09_Rubrics.json'), 'w'), indent=2, ensure_ascii=False)
json.dump(OUT, open(os.path.join(TI, 'Working_Files', '09_Rubrics.draft_with_plan_ids.json'), 'w'), indent=2, ensure_ascii=False)
print('wrote', len(OUT), 'weight', sum(c['weight'] for c in OUT))
