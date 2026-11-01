"""Draft mode: writes task_inputs/09_Rubrics.json (builder shape) from the plan rows (rows.json in the scratch folder, arg 1).
Also writes Working_Files/09_Rubrics.draft_with_plan_ids.json (same criteria plus the plan row id)."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
rows = json.load(open(os.path.join(sys.argv[1], 'rows.json')))
REG = "the ZM difficulty baseline register"
TAB = f"on the Tickets tab of {REG}"
RIF = f"on the Rules in force tab of {REG}"
DM = "in its DM reply to Leonard"
EMAIL = {"Robert": ("Robert", "robert@harmonygames.co"), "Brian": ("Brian Foster", "brian.foster@harmonygames.co"),
         "Leonard": ("Leonard Hayes", "leonard.hayes@harmonygames.co"), "Arthur": ("Arthur Blake", "arthur.blake@harmonygames.co")}
RULES = {
 "Starting tier timing": f"states {RIF} that a new player's starting tier is set when their 10th game ends, with wins and losses both counting ('10 games', '10 attempts' or '10 levels played' pass; 'level 10' or 'after 10 levels' alone fails)",
 "Starting tier threshold": f"states {RIF} that an average CPM above 90 sets the starting tier to tier 1 and that exactly 90 stays on tier 0",
 "Promotion — win rate": f"states {RIF} that a player is promoted at a win rate of 80% or more over up to the most recent 10 attempts",
 "Promotion — tier -2": f"states {RIF} that a player on tier -2 is promoted after one win",
 "Demotion — 4 losses": f"states {RIF} that 4 losses in a row demote a player",
 "Demotion — win rate": f"states {RIF} that a player is demoted at a win rate of 50% or lower over up to the last 10 games",
 "Record reset": f"states {RIF} that the win record resets after every promotion or demotion",
 "Level drop": f"states {RIF} that after a demotion the level the player is on also drops one tier",
 "Enrage — Boxer": f"records {RIF} Boxer's enrage values as speed 0.5 and damage 0.4",
 "Enrage — MonsterBase": f"records {RIF} MonsterBase's enrage values as speed 0.8 and damage 0.8",
 "Enrage — Plumber": f"records {RIF} Plumber's enrage values as speed 0.3 and damage 0.3",
 "Enrage — no hp": f"states {RIF} that enrage's hp boost is 0 or switched off",
 "Enrage volume": f"lists {RIF} enrage speed and damage values for exactly 10 monster rows copied from the Live tab of the ZM monster enrage sheet (the Mailman, Mayor2, PartyGirl row marked not copied yet sits outside the 10)",
}


def title(r):
    w = r['what']
    m = re.match(r"Scope boundary — (ZOM-\d+)", w)
    if m:
        return f"The Agent leaves {m.group(1)} off the Tickets tab of {REG} (naming it in a separate note of left-off tickets passes)"
    m = re.match(r"Status — (ZOM-\d+) (Live|Editor only|Not shipped)$", w)
    if m:
        return f"The Agent records the status {m.group(2)} for {m.group(1)} {TAB}"
    if w.startswith("Status — ZOM-254"):
        return f"The Agent records ZOM-254 as Replaced, replaced by ZOM-282 (key or title), {TAB}"
    if w.startswith("Linear state column"):
        return f"The Agent records ZOM-202's Linear state as In Progress {TAB}"
    if w.startswith("Register artifact"):
        return f"The Agent creates {REG} as one new spreadsheet (any title)"
    if w.startswith("Register layout"):
        return f"The Agent gives {REG} two tabs, Tickets and Rules in force (clear equivalents of those two names pass)"
    if w.startswith("Register location"):
        return f"The Agent places {REG} in the ZM Difficulty folder in Google Drive (created there or moved there)"
    if "exactly 24 ticket rows" in w:
        return f"The Agent fills the Tickets tab of {REG} with exactly 24 ticket rows (a separate note naming left-off tickets may sit beside them)"
    if "exactly 16 tickets" in w:
        return f"The Agent records exactly 16 tickets with the status Live {TAB}"
    if "exactly 4 tickets with status" in w:
        return f"The Agent records exactly 4 tickets with the status Editor only {TAB}"
    if w.startswith("Rules in force — "):
        for k, v in RULES.items():
            if w.startswith("Rules in force — " + k) or (k == "Enrage — no hp" and "no hp" in w) or (k == "Enrage volume" and "Enrage volume" in w) \
               or (k == "Demotion — 4 losses" and "4 losses" in w) or (k == "Promotion — win rate" and "80%" in w) or (k == "Promotion — tier -2" and "tier -2" in w) \
               or (k == "Demotion — win rate" and "50%" in w) or (k == "Record reset" and "Record reset" in w) or (k == "Level drop" and "Level drop" in w):
                return "The Agent " + v
        raise SystemExit("no rules title: " + w)
    m = re.match(r"Share — (\w+) \(([^)]+)\) as (\w+)", w)
    if m:
        name, mail = EMAIL[m.group(1)]
        role = {"editor": "editor (writer) access", "commenter": "commenter access (editor access fails)", "viewer": "viewer (reader) access"}[m.group(3)]
        extra = "; his access as owner of the ZM Difficulty folder also passes" if m.group(1) == "Leonard" else ""
        if extra:
            role = role.replace(" (editor access fails)", "") + f" ({extra[2:]})"
        return f"The Agent shares {REG} with {name} ({mail}) with {role}"
    if w.startswith("Comment — ZOM-199"):
        return "The Agent adds a new comment on Linear issue ZOM-199 saying the build's starting-tier check is CPM > 90 rather than >= 90 (so exactly 90 stays on tier 0)"
    if w.startswith("Comment — ZOM-254"):
        return "The Agent adds a new comment on Linear issue ZOM-254 naming ZOM-282 as the ticket that replaced it"
    m = re.match(r"Comment — (ZOM-\d+): the change", w)
    if m:
        return f"The Agent adds a new comment on Linear issue {m.group(1)} saying its change is missing from the store builds (any wording that the store builds lack the change passes)"
    if w.startswith("Comment volume"):
        return "The Agent adds a new comment to exactly 9 ZOM tickets in Linear"
    if w.startswith("DM reply — sent"):
        return "The Agent replies to Leonard in his direct message conversation with Julia (a thread reply or a new message in that DM both pass)"
    m = re.match(r"DM reply — total", w)
    if m:
        return f"The Agent states {DM} that 24 tickets made the list"
    m = re.match(r"DM reply — (Live|Editor only|Not shipped|Replaced) count — (\d+)", w)
    if m:
        return f"The Agent states {DM} that {m.group(2)} {'ticket is' if m.group(2) == '1' else 'tickets are'} {m.group(1)}"
    m = re.match(r"DM reply — (ZOM-\d+) named as (.+)$", w)
    if m:
        return f"The Agent names {m.group(1)} {DM} as an {m.group(2)} ticket" if m.group(2).startswith("E") else f"The Agent names {m.group(1)} {DM} as a {m.group(2)} ticket"
    if "exactly 4 tickets named as Editor only" in w:
        return f"The Agent names exactly 4 tickets {DM} as Editor only"
    if w.startswith("DM reply — ZOM-254"):
        return f"The Agent tells Leonard in its DM reply that ZOM-254 was replaced by ZOM-282"
    if w.startswith("DM reply — a new player"):
        return (f"The Agent tells Leonard in its DM reply that a new player gets the starting tier when their 10th game ends, with wins and losses both "
                "counting ('10 games', '10 attempts' or '10 levels played' pass; 'level 10' or 'after 10 levels' alone fails)")
    raise SystemExit("no title: " + w)


PTR = {"F1": "Leonard's ask in the DM, D05HB64NMQU/1759261706.530914", "F2": "Leonard's reply under the ask, D05HB64NMQU/1759262838.442871",
       "F3": "Leonard's reply under Julia's Sep 29 question, D05HB64NMQU/1759267002.665190", "F4": "Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383, rules 1-7",
       "F5": "Leonard's card comment 68dbfa4362a051efb5e0ae45", "F6": "the card's 'Before Monday' checklist 68dc033bf7d24e86b8a9cc67",
       "F7": "Leonard's 'notes for monday' doc f_f494073fc667097c3c2c6b", "F8": "Blake's 'store builds for monday' mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>",
       "F9": "Blake's reply julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>", "F10": "agenda doc 'ZM difficulty tuning - Oct 6' f_9ec79682ff351aa466364a",
       "F11": "Live tab of the 'ZM monster enrage' sheet f_0ba93ae0238d9ed4178212", "F12": "the tuning invite evt_91674a9c23d012a9ac34da",
       "F13": "the ZM Difficulty folder d_96489e1e00a56685625939", "F14": "ZOM-42 description", "F15": "team ZOM issues created up to Aug 31 and their closing notes",
       "F16": "Blake's review comment harmonygames-Games/match3d#265#rc_7", "F17": "harmonygames-Games/match3d#401#c_2",
       "F18": "match3d Assets/Scripts/DynamicDifficulty/TierManager.cs (totalGames == 10, cpm > 90.0f) and Player/WinHistory.cs",
       "F19": "ZOM-303 description; Blake's #zombie-design note C090N54TG79/1756912929.304417",
       "F20": "the register worked out from the card rules, both DM thread replies, the notes doc and the PR 265 review",
       "F22": "card rule 6 plus the checklist, minus the four tickets in D05HB64NMQU/1759267002.665190",
       "F23": "the counts and keys of the 24-row register"}


def clean(x):
    x = re.sub(r"\s*\((?:Robert|Douglas) /rubric[^)]*\)", "", x)
    x = re.sub(r"\bgate 6: ", "", x).replace("/prompt r12 rubric note: ", "the prompt review accepts this: ").replace("/prompt r12", "the prompt review")
    x = re.sub(r"\bbrief §4b[^;).]*", "the task's canonical outcome", x)
    x = re.sub(r"\(?\bF\d+\b\)?", "", x)
    x = re.sub(r";?\s*[A-Z]{3}-\d+ named by\s*\.", ".", x)
    x = x.replace("the prompt review accepts this: accept ", "the prompt review accepts ")
    parts = []
    for sent in re.split(r"(?<=\.)\s+", x):
        if sent.strip().lower() not in [q.strip().lower() for q in parts]:
            parts.append(sent)
    x = " ".join(parts)
    x = re.sub(r"\s{2,}", " ", x).replace(". the prompt review", ". The prompt review").replace(" ;", ";").replace(" .", ".").replace("..", ".").replace('|', '/')
    return x.strip()


BAD = re.compile(r"\b(such as|e\.g\.|for example|does not|do not|must not|never|without|avoid|primary|main|mainly|overall)\b", re.I)
out, out2 = [], []
for r in rows:
    t = title(r)
    assert not BAD.search(t), t
    if r['res'] in r['kind']:
        r = dict(r, res='the record named in the evidence decides the role')
    just = clean(f"{r['kind'][0].upper() + r['kind'][1:]}. {r['res'][0].upper() + r['res'][1:]}.".replace(". the prompt", ". The prompt"))
    ev = clean("Sources: " + "; ".join(dict.fromkeys(PTR[f] for f in re.findall(r"\bF\d+\b", r['vals'] + ' ' + r['res']) if f in PTR))
               + ". Accept: " + re.sub(r"\bF\d+\b\s*", "", r['vals'].replace("`" + r['what'].split(" — ", 1)[-1] + "` ", "")).replace('`', "'").strip() + ".")
    for x in (just, ev):
        assert not re.search(r"\b(such as|e\.g\.|for example)\b", x, re.I), x
    c = {"title": t, "category": "Outcome", "weight": r['band'], "justification": just, "evidence": ev}
    out.append(c)
    out2.append(dict(c, plan_row=r['P']))
assert len({c['title'] for c in out}) == len(out), "duplicate titles"
json.dump(out, open(os.path.join(TI, '09_Rubrics.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(out2, open(os.path.join(TI, 'Working_Files', '09_Rubrics.draft_with_plan_ids.json'), 'w'), indent=1, ensure_ascii=False)
print(len(out), 'criteria; weight', sum(c['weight'] for c in out))
