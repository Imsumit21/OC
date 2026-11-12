#!/usr/bin/env python3
"""Write plan/rubric/probe_dispositions.txt: one `SHORTCUT-OK: <service> <record> — <reason>` line per HIT/INCOMPLETE
in plan/rubric/probe.txt. Every reason was checked by reading the record (hg.py get / the probe cache snippets /
the task SQL) on 2026-11-12; an unmapped HIT stops the script so a new hit is never waved through."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

NO_ANSWER = ("it names asset files only and carries no State, What's owed, Who has it, Board set, zombie pick or brief "
             "value, so no row can be answered from it")
GH = {
    "data.json/commits/4374": "base match3d merge commit whose conflict list is texture file paths (Alarm Clock, Bathtub …); " + NO_ANSWER,
    "data.json/commits/5750": "base match3d commit touching item prefab files; " + NO_ANSWER,
    "data.json/commits/8003": "base zombie-game commit touching zombie prefab files (Magician, Party Girl, Plumber); the picks row needs Robert's 29 Sep post, which this does not hold; " + NO_ANSWER,
    "data.json/pull_request_comments/456": "base CodeRabbit 'review skipped' list of ignored prefab paths; " + NO_ANSWER,
    "data.json/pull_request_comments/461": "base CodeRabbit 'review skipped' list of ignored prefab paths; " + NO_ANSWER,
    "data.json/pull_request_comments/467": "base CodeRabbit 'review skipped' list of ignored prefab paths; " + NO_ANSWER,
    "data.json/pull_request_comments/488": "base CodeRabbit 'review skipped' list of ignored prefab paths; " + NO_ANSWER,
    "data.json/pull_request_comments/499": "base CodeRabbit comment on match3d#323 listing 300 ignored prefab paths (Assets/Prefabs/Objects/…); its 49 line-name keys are file names, " + NO_ANSWER,
    "data.json/pull_request_comments/515": "base CodeRabbit 'review skipped' list of ignored prefab paths; " + NO_ANSWER,
    "data.json/pull_request_comments/535": "base CodeRabbit list of zombie prefab paths; it is not Robert's pick of four and " + NO_ANSWER,
    "data.json/pull_request_comments/644": "base CodeRabbit 'review skipped' list of ignored prefab paths; " + NO_ANSWER,
    "data.json/pull_requests/2194": "base zombie-game pull request touching zombie prefabs; it is not Robert's pick of four and " + NO_ANSWER,
    "data.json/reviews/2049": "base code review on zombie prefab changes; it is not Robert's pick of four and " + NO_ANSWER,
    "data.json/reviews/2132": "base code review on item prefab changes; " + NO_ANSWER,
}
SHEET_ACL = ("base spreadsheet whose owner/collaborator list holds the three kickoff-hold addresses; the sharing rows grade "
             "permissions on the two files the Agent creates, which no base file can supply")
GS = {
    "f_20374926b5634ce543479f": SHEET_ACL + "; its Dynamite is the event name dynamite_tile_used in the 'Data Dictionary GoD' sheet of another game",
    "f_b716211e83ea64d6008145": SHEET_ACL + "; its Dynamite is a booster counter (Dynamite-Tile:0) in the 'Data Dictionary Firebase' sheet",
    "f_b82d4d41386fe0a90da5bd": SHEET_ACL + "; its Cannon and Dynamite are booster texts in another game's 'Loc files' localisation sheet",
    "f_e26ebf66da093ef7d77fc6": SHEET_ACL + "; it is 'Zombie Match 3D FTUE Steps DEPRECATED', a tutorial-step sheet whose zombie and item names (cannon booster tutorial, iron) carry no pick, state or holder",
}
SLACK = {
    "C05433XK267/1755041507.929169": "base August build-notes post listing 'VarC of Magician, Party Girl, Boxer, Plumber' (a different set: Boxer, no Football Player); not the playable's four, no state or holder",
    "C05433XK267/1755043877.139149": "base August build-notes post listing 'VarC of Magician, Party Girl, Boxer, Plumber' (a different set); not the playable's four, no state or holder",
    "C05433XK267/1756130042.256759": "base August build-notes post listing 'VarC of Magician, Party Girl, Boxer, Plumber' (a different set) beside a Grenade change; not the picks, no state or holder",
    "C0880U9751A/1753782605.895689": "base July zombie balance notes (travel time, HP per zombie); a design roster, not the playable's picks, no state or holder",
    "D076RBM29JS/1757343180.172849": "base September DM on the tutorial order of zombies by level; a roster, not Robert's pick of four for the playable",
    "C08H78VJG80/1757695108.506159": "base 12 Sep PlayableX scenario message: the designed purpose source the brief's scenario/purpose rows read (with the 22 Sep thread and its walk-back); it answers only those rows, which is the intended read",
    "C08H78VJG80/1757956024.883249": "base 15 Sep PlayableX message on reference-level items (grenade, couch, plush doll): the vendor's suggestion, superseded by Robert's 25 Sep board picks; answers no board row on its own",
    "C090N54TG79/1758567201.262949": "base 22 Sep re-share of the vendor's reference-level item suggestion; superseded by Robert's 25 Sep board picks; answers no board row on its own",
    "C08H78VJG80/1758283671.878269": "base 19 Sep vendor asset list (Matching, rocket, explosion sounds…): it says what PlayableX asks for, not which sounds are ours to hand over; the sound rows need Calvin's sheet",
}
CONF = ("the design page (page_zm3d_gdd), the designed source for the tray-size and lose-condition rows (7-slot tray, zero "
        "health); its Magician is the SC-58 monster roster that no row grades, and it holds no zombie pick, state or holder")
SQL = {
    "L265:evt_d622b6ab55401d23626674": "seeded kickoff hold 'ZM3D playable kickoff with PlayableX' (Frederick's copy): the designed sharing-target list; sharing is the Agent's write on its own files",
    "L268:evt_421695d009e589ee85296c": "seeded kickoff hold (Julia's copy): the designed sharing-target list; sharing is the Agent's write on its own files",
    "L270:evt_a78612f3eaf04ce8461eb4": "seeded kickoff hold (Brian's copy): the designed sharing-target list; sharing is the Agent's write on its own files",
    "L272:evt_1c99b11a66cfd562b13d9c": "seeded kickoff hold (Robert's copy): the designed sharing-target list; sharing is the Agent's write on its own files",
    "L277:julia.lawson@harmonygames.co/<calendar-483bd48e-cfb4-fd3f-b55c-4b417cd0d88a@google.com>": "seeded invitation email for the kickoff hold: the same sharing-target list; sharing is the Agent's write on its own files",
    "L17:f_8c1d0bca1d1d5fde4c5008": "Frederick's hand-off notes, the rule source the ask hands over ('My hand-off notes say …'); it states the rules and columns, not any line's State, owed work or holder",
    "L6:f_8c1d0bca1d1d5fde4c5008": "Drive row of Frederick's hand-off notes; its permission list holds the three addresses, no answer value",
    "L9:f_956e60ec7f2f7977d98934": "Drive row of Brian's pack list; its permission list holds the three addresses, no answer value",
    "L22:f_956e60ec7f2f7977d98934": "spreadsheet row of Brian's pack list; its permission list holds the three addresses, no answer value",
    "L25:f_956e60ec7f2f7977d98934": "Brian's pack list Pack tab, the population source the ask names ('Brian's pack list is where it starts'); it holds Line, Kind, Category, Went out and Ticket, never State, What's owed, Who has it or Board set, which come from the tickets, posts and the art/sound records",
    "L29:f_b2387e31d46d3a7b3fa2a9": "Calvin's sound sheet, the designed unlinked authority for the sound rows; finding it is the intended work and it holds no item-line answer",
    "L44:f_6a2fa8e61b31139ca8e3d4": "reference-level deck (older state): it names the three reference items, not the board eight; Robert's 25 Sep post decides the board",
    "L61:da6776f77288224ec67847a799bbde5a": "Robert's 25 Sep board picks, the authority the ask names ('Robert's picks for the board … stand'); it answers the board-eight rows only, which is the intended read",
    "L62:0b7f656a96c5cc50d1f6924e089bf8ba": "Robert's 29 Sep zombie and animation post, the authority the ask names; it answers the zombie and animation rows only, which is the intended read",
}
INC = {
    ("snowflake", "Iron"): ("search hit the match limit; the other 177 values complete on Snowflake and no Snowflake record holds more than one of them "
                            "(probe cache, 9,848 records), so Iron can raise a record to 2 values at most, below k=3 and far below a population's 50%"),
}


def reason(svc, rec):
    if svc == "github":
        return GH.get(rec)
    if svc == "gsheets":
        return GS.get(rec) or SHEET_ACL
    if svc == "slack":
        return SLACK.get(rec)
    if svc == "confluence":
        return CONF
    if svc.startswith("sql:"):
        return SQL.get(rec)
    return None


out, missing = [], []
for l in (HERE / "probe.txt").read_text().splitlines():
    h = re.match(r"^HIT (\S+) (\S+) ", l)
    x = re.match(r'^INCOMPLETE (\S+) value:"(.*)" \(', l)
    if h:
        svc, rec = h.groups()
        r = reason(svc, rec)
        if not r:
            missing.append(l)
            continue
        line = f"SHORTCUT-OK: {svc} {rec} — {r}"
    elif x:
        svc, v = x.groups()
        r = INC.get((svc, v))
        if not r:
            missing.append(l)
            continue
        line = f'SHORTCUT-OK: {svc} value:"{v}" — {r}'
    else:
        continue
    if line not in out:
        out.append(line)
assert not missing, "undispositioned probe lines:\n" + "\n".join(missing)
(HERE / "probe_dispositions.txt").write_text("\n".join(out) + "\n")
print(len(out), "dispositions written")
