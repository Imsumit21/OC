"""Writes task_inputs/Working_Files/09_Rubric_Writing_Plan.md (prep mode) for jl-zm-difficulty-baseline.
Pasted outputs are read from files in the scratch folder given as arg 1: vis.txt (check-sql YES lines),
probe.txt (shortcut_probe output), disp.txt (SHORTCUT-OK lines). rows.json is written beside them."""
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
SC = sys.argv[1]
rd = lambda n: open(os.path.join(SC, n)).read().rstrip('\n') if os.path.exists(os.path.join(SC, n)) else ''

S_ASK = "go through his ask and everything it points to"
S_REG = "build the register the way he set it up"
S_FOLD = "put it in the zm difficulty folder"
S_SHARE = "share it with everyone on monday's tuning invite"
S_TIX = "if his rules say something needs to happen on the tickets, go ahead and do that too"
S_DM = "then reply to leonard in the dm with what he asked for"
REG = "the ZM difficulty baseline register"
rows = []


def add(**k):
    k.setdefault('prompt_title', 'no — must not hard-code')
    k.setdefault('distractor', '—')
    k.setdefault('ambig', 'no')
    k.setdefault('group', '—')
    k.setdefault('dup', 'one deliverable')
    k.setdefault('allfail', 'none · phrase broadly')
    k.setdefault('cat', 'Outcome')
    rows.append(k)


# ---------------- W1 register: artifact ----------------
add(src=f'"{S_REG}" · OE 23', what="Register artifact — one new spreadsheet holding the register", final="Google Sheet in Julia's Drive",
    vals="F10 `one sheet`; any title (brief §4b W1 title representational)", kind="lookup — the agenda says 'One sheet'", band=1, dec="—", oes=[23],
    cr="A run could build the register as a Doc table", res="the agenda F10 says 'One sheet with two tabs' (f_9ec79682ff351aa466364a); a sheet is the named artifact, any title passes")
add(src=f'"{S_REG}" · OE 9, 25', what="Register layout — two tabs, Tickets and Rules in force", final="Tab list of the register",
    vals="F10 `Tickets` `Rules in force`; clear equivalents of the two names pass", kind="lookup — the agenda names both tabs", band=1, dec="—", oes=[9, 23, 25],
    cr="Exact tab names could fail 'Rules' or 'Rules in force (Oct 1)'", res="brief §4b W1 tabs: those names or clear equivalents, two tabs; the row says so")
add(src=f'"{S_FOLD}" · OE 11, 27', what="Register location — the ZM Difficulty folder", final="Parent folder of the register file",
    vals="F13 `ZM Difficulty` `d_96489e1e00a56685625939`; created there or moved there", kind="interpretation — the folder is named in the prompt and rule 7; the file must end there", band=3, dec="—", oes=[11, 27],
    cr="A run that creates the file inside the folder never calls move", res="the row grades the end state (parent folder), not the move call (brief §4b W1 kind/location)")
add(src=f'"{S_REG}" · OE 17, 18, 22, 24', what="Register volume — exactly 24 ticket rows on the Tickets tab", final="Row set of the Tickets tab",
    vals="F20 `24`; exact; a separate note naming left-off tickets may sit beside the rows", kind="multi-source — the count follows only from the title scan, the 'tiers:' notes, the attack-power amendment, both DM thread replies, the notes doc and the PR review", band=5,
    dec="T1 T22 T28 L7", distractor="all-inclusive 34–35 row lists → exact count rejects them", oes=[17, 18, 22, 24], dup="volume row for G1",
    cr="A run listing the dropped tickets under a 'left off' heading has more than 24 lines", res="the row counts register rows; dropped tickets named in a separate note pass (brief §4b W1 row set)")
add(src=f'"{S_REG}" · OE 22, 24', what="Register volume — exactly 16 tickets with status Live", final="Status column of the Tickets tab",
    vals="F20 `16` `Live`; exact", kind="multi-source — needs every scope cut and every status call", band=5, dec="T22 L7", oes=[22, 24], dup="volume row for G1",
    cr="A run that keeps the six analytics/tutorial tickets has 22 Live", res="those six are dropped by Leonard's thread reply D05HB64NMQU/1759262838.442871; 16 is the only value under the governing reply set")
add(src=f'"{S_REG}" · OE 8, 18, 22, 24', what="Register volume — exactly 4 tickets with status Editor only", final="Status column of the Tickets tab",
    vals="F20 `4` `Editor only`; exact", kind="multi-source — Blake's mail, the closing notes and the Sep 30 21:16 reply", band=5, dec="L7 T28", oes=[8, 18, 22, 24],
    cr="ZOM-162/163/201/250 are Editor only on their merits", res="Leonard's reply D05HB64NMQU/1759267002.665190 takes them off the list; the four left are ZOM-173, 200, 277, 315")
EXC = [("ZOM-30", "F2", "T22", 2, "analytics ticket ('Need to track average blunder'); title match"), ("ZOM-49", "F2", "T22", 2, "analytics (Blunder Count by Level)"),
       ("ZOM-50", "F2", "T22", 2, "analytics (skill tier in left_level)"), ("ZOM-161", "F2", "T22", 2, "analytics (tier assignment for left level event)"),
       ("ZOM-262", "F2", "T22", 2, "tutorial (Blunder Locked User)"), ("ZOM-275", "F2", "T22", 2, "tutorial (FTUE message)"),
       ("ZOM-162", "F3", "L7", 3, "level editor tracks (Editor only on its merits)"), ("ZOM-163", "F3", "L7", 3, "level editor play button (Editor only on its merits)"),
       ("ZOM-201", "F3", "L7", 3, "stat window (Editor only on its merits)"), ("ZOM-250", "F3", "L7", 3, "attack power title via the card comment"),
       ("ZOM-258", "F7", "L6", 7, "enraged-monster icon; Leonard's notes doc"), ("ZOM-312", "F16", "L5", 19, "title match 'Difficulty Tier'; Blake's 'not tiers' review on match3d#265")]
for k, f, dec, oe, why in EXC:
    add(src=f'"{S_REG}" · OE {oe}, 22, 24', what=f"Scope boundary — {k} left off the Tickets tab", final="Row set of the Tickets tab",
        vals=f"{f} `{k}`; a separate note naming it as left off passes", kind=f"interpretation — {why}: the title or card rules put it in, a later record takes it out", band=3, dec=dec,
        distractor=f"{k} matches rule 1 → grade that it stays off", oes=[oe, 22, 24],
        cr=f"Absence-only acceptance could fail Negative Criteria", res=f"the row grades a scope boundary of a required artifact: an idle Agent with no register fails it (Robert /rubric 'disguised_negative resolved'); {k} named by {f}")
LIVE = [("ZOM-221", 3, "tag-only member ('tiers:' note), no title word", "F15", "T13"), ("ZOM-281", 5, "tag-only member assigned to someone else (cmt_df69e4a92767cbff0000)", "F15", "L3"),
        ("ZOM-246", 3, "attack-power amendment member", "F5", "T1"), ("ZOM-282", 3, "PR 401 split its values; not Replaced (rule 4)", "F17", "T9"),
        ("ZOM-45", 3, "editor label that the game also reads at runtime", "F15", "T6")]
for k, b, why, f, dec in LIVE:
    add(src=f'"{S_REG}" · OE 18, 22, 24', what=f"Status — {k} Live", final=f"{k} row of the Tickets tab", vals=f"{f} F8 `{k}` `Live`",
        kind=("multi-source" if b == 5 else "interpretation") + f" — {why}", band=b, dec=dec, group="G1", oes=[18, 22, 24],
        cr=f"{k} could read as Editor only or not a member", res=f"{why}; store builds mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> strips only editor and debug folders")
for k, why in [("ZOM-173", "set count in the level objects panel (level editor)"), ("ZOM-200", "debug menu, stripped from store builds"),
               ("ZOM-277", "average in the editor's stats panel"), ("ZOM-315", "total attack power in the editor's stats panel")]:
    add(src=f'"{S_REG}" · OE 8, 18, 22, 24', what=f"Status — {k} Editor only", final=f"{k} row of the Tickets tab", vals=f"F8 F15 `{k}` `Editor only`",
        kind=f"interpretation — {why}, read against Blake's mail", band=3, dec="T6", oes=[8, 18, 22, 24],
        cr=f"{k} is Done in Linear, so a run may call it Live", res="Blake's mail: 'A ticket whose changes are only level editor or debug tooling never reached players, Done or not'")
for k, st in [("ZOM-202", "In Progress"), ("ZOM-280", "Canceled"), ("ZOM-293", "Todo")]:
    add(src=f'"{S_REG}" · OE 17, 22, 24', what=f"Status — {k} Not shipped", final=f"{k} row of the Tickets tab", vals=f"F4 F15 `{k}` `Not shipped`",
        kind=f"lookup — Linear state {st}; rule 1 'open, cancelled and never-merged ones are in, as Not shipped'", band=1, dec="—", oes=[17, 22, 24],
        cr="A run could leave a cancelled ticket off", res="rule 1 keeps open and cancelled ones in as Not shipped (68daca5871dba40417a00383)")
add(src=f'"{S_REG}" · OE 18, 22, 24', what="Status — ZOM-254 Replaced, replaced by ZOM-282", final="ZOM-254 row of the Tickets tab",
    vals="F15 `ZOM-254` `Replaced` `ZOM-282`; ZOM-282 by key or title", kind="interpretation — ZOM-282's closing note names ZOM-254 (rule 4)", band=3, dec="T9", oes=[18, 22, 24],
    cr="Status and replaced-by are two claims", res="coupled attributes of one record (coherent_record: a row's status and the ticket that replaced it)")
add(src=f'"{S_REG}" · OE 17, 24', what="Linear state column — ZOM-202 as found (In Progress)", final="ZOM-202 row of the Tickets tab",
    vals="F15 `ZOM-202` `In Progress`", kind="lookup — one Linear field", band=1, dec="—", oes=[17, 24],
    cr="A run could write the status word in the state column", res="rule 2 lists 'Linear state (as you found it)' as its own column")
# ---------------- Rules in force ----------------
R5 = [("Starting tier timing — set when a new player's 10th game ends, wins and losses both counting", "F18 F4 `10th game`; '10 games' or '10 levels played' pass; 'level 10' or '10 levels' alone fails", 5, "multi-source — the build over ZOM-42, ZOM-199 and the deck, under rule 5 'go by the build'", "L4", [15, 26]),
      ("Starting tier threshold — average CPM above 90 goes to tier 1, 90 exactly stays on tier 0", "F9 `> 90` `tier 1`", 3, "comparison — Blake's reply over ZOM-199 and the deck", "T10", [8, 26]),
      ("Promotion — win rate 80% or more over up to the most recent 10 attempts", "F14 `80%` `10`", 3, "interpretation — ZOM-42's wording (rule 5)", "T11", [14, 26]),
      ("Promotion — tier -2 promotes after one win", "F14 `tier -2` `1 win`", 1, "lookup — one ZOM-42 sentence", "—", [14, 26]),
      ("Demotion — 4 losses in a row", "F14 `4 losses in a row`", 1, "lookup — one ZOM-42 sentence (also in the deck)", "—", [14, 26]),
      ("Demotion — win rate 50% or lower over up to the last 10 games", "F14 `50%` `10`", 3, "interpretation — only in ZOM-42; the deck omits it", "T11", [14, 16, 26]),
      ("Record reset after every promotion or demotion", "F14 `reset`", 1, "lookup — one ZOM-42 sentence", "—", [14, 26]),
      ("Level drop after a demotion — yes", "F19 `yes`; the level drops a tier", 3, "interpretation — ZOM-303's solution sentence", "—", [21, 26]),
      ("Enrage — Boxer speed 0.5, damage 0.4", "F11 `Boxer` `0.5` `0.4`", 3, "comparison — the Live tab over the deck's +25% and Brian's +50% recap", "T15", [12, 26]),
      ("Enrage — MonsterBase speed 0.8, damage 0.8", "F11 `MonsterBase` `0.8`", 3, "comparison — Live tab, not the Next pass proposal (0.3/0.8 by level band)", "T16", [12, 26]),
      ("Enrage — Plumber speed 0.3, damage 0.3", "F11 `Plumber` `0.3`", 1, "lookup — ordinary Live row", "—", [12, 26]),
      ("Enrage — no hp boost (hp 0 or switched off)", "F11 F19 `hp`; 0, off or none", 3, "comparison — Blake's note and the Live tab over the deck's +25% max HP", "T15", [12, 13, 26]),
      ("Enrage volume — 10 monster rows with speed and damage values copied from the Live tab", "F11 `10`; the Mailman, Mayor2, PartyGirl row is not counted", 3, "interpretation — copy the Live tab as it stands (rule 5)", "T16", [12, 26])]
for what, vals, b, kind, dec, oes in R5:
    add(src=f'"{S_REG}" · OE ' + ", ".join(map(str, oes)), what="Rules in force — " + what, final="Rules in force tab", vals=vals, kind=kind, band=b, dec=dec, oes=oes,
        group="G2" if what.startswith("Enrage —") and "hp" not in what else "—",
        cr="A valid run could word the rule differently", res="phrase broadly: any wording carrying the value passes (brief §4b W1 rules rows); /prompt r12 accepts '10 levels played' for the timing")
# ---------------- W2 shares ----------------
for who, mail, role, f, b, dec, oe, why in [("Robert", "robert@harmonygames.co", "editor", "F12 F4", 1, "—", 28, "rule 7 'Robert can edit'"),
                                             ("Brian", "brian.foster@harmonygames.co", "commenter", "F12 F3", 3, "L7", 29, "the Sep 30 21:16 reply takes back the checklist's 'Brian gets edit'"),
                                             ("Leonard", "leonard.hayes@harmonygames.co", "commenter", "F12 F4", 1, "—", 30, "rule 7 'everyone else comments'"),
                                             ("Arthur", "arthur.blake@harmonygames.co", "viewer", "F12 F7", 3, "L6", 31, "the notes doc: 'view access is enough for him'")]:
    add(src=f'"{S_SHARE}" · OE 10, {oe}', what=f"Share — {who} ({mail}) as {role}", final="Register file permissions", vals=f"{f} `{mail}` `{role}`",
        kind=("lookup" if b == 1 else "interpretation") + f" — {why}", band=b, dec=dec, oes=[10, oe],
        cr=f"{who}'s existing folder access could stand in for a share", res=("Leonard owns the folder, so his folder access also satisfies his row (brief §4b W2)" if who == "Leonard" else f"{why}"))
# ---------------- W3 comments ----------------
add(src=f'"{S_TIX}" · OE 8, 32', what="Comment — ZOM-199: the build checks CPM > 90, not >= 90", final="New comment on ZOM-199", vals="F9 `ZOM-199` `> 90`; any wording carrying > 90 vs >= 90",
    kind="comparison — Blake's reply against the ticket text", band=3, dec="T10", oes=[8, 32], cr="A run could comment on ZOM-42 instead", res="Blake's reply names ZOM-199; rule 6 comments on the ticket whose text is wrong")
add(src=f'"{S_TIX}" · OE 18, 33', what="Comment — ZOM-254 names ZOM-282 as what replaced it", final="New comment on ZOM-254", vals="F15 `ZOM-254` `ZOM-282`",
    kind="interpretation — rule 6 Replaced comment from ZOM-282's note", band=3, dec="T9", oes=[18, 33], cr="A run could comment on ZOM-282 instead", res="rule 6: 'Replaced tickets get a comment naming what replaced them' — the comment goes on ZOM-254")
for k, oe in [("ZOM-173", 34), ("ZOM-200", 35), ("ZOM-277", 36), ("ZOM-202", 38), ("ZOM-280", 39)]:
    add(src=f'"{S_TIX}" · OE 6, {oe}', what=f"Comment — {k}: the change isn't in the store builds", final=f"New comment on {k}", vals=f"F6 `{k}`; any wording that the change is not in the store builds",
        kind="interpretation — the checklist's rule 6 change applied to a register status", band=3, dec="L2", group="G3", oes=[6, oe],
        cr="The checklist could be read as a to-do for Leonard", res="the checklist item says 'the Editor only and Not shipped tickets get a comment too' (68dc033bf7d24e86b8a9cc67); /prompt r12 settled the reading")
add(src=f'"{S_TIX}" · OE 3, 6, 32–40', what="Comment volume — new comments on exactly 9 ZOM tickets", final="Linear comments created by the run",
    vals="F22 F3 `9`; exact", kind="multi-source — rule 6 plus the checklist minus the four tickets Leonard's Sep 30 reply drops", band=5, dec="L7 L5", oes=[3, 6] + list(range(32, 41)), dup="volume row for G3",
    cr="Leonard's 'no comments on them either' could be missed only by an ambiguous reading", res="the reply D05HB64NMQU/1759267002.665190 says it plainly; 9 = ZOM-199, 254 and the 7 Editor only / Not shipped")
# ---------------- W4 DM ----------------
DMP = "in the DM reply to Leonard"
add(src=f'"{S_DM}" · OE 1, 41', what="DM reply — sent to Leonard in the DM", final="Message from Julia in D05HB64NMQU", vals="F1 `D05HB64NMQU`; a thread reply or a top-level DM message",
    kind="lookup — the ask says 'reply here'", band=1, dec="—", oes=[1, 41], cr="A run could post in #zombie-design (Vincent's request)", res="the ask says 'reply here' (D05HB64NMQU/1759261706.530914); /prompt r12: thread or top level both pass")
for what, vals, b, kind, dec in [("total — 24 tickets made the list", "F23 F1 `24`", 5, "multi-source — the register count after both thread replies", "T22 L7"),
                                 ("Live count — 16", "F23 `16` `Live`", 5, "multi-source — the register count after both thread replies", "T22 L7"),
                                 ("Editor only count — 4", "F23 `4` `Editor only`", 3, "interpretation — count after the Sep 30 21:16 reply", "L7"),
                                 ("Not shipped count — 3", "F23 `3` `Not shipped`", 1, "lookup — three open or cancelled tickets", "—"),
                                 ("Replaced count — 1", "F23 `1` `Replaced`", 1, "lookup — one Replaced row", "—")]:
    add(src=f'"{S_DM}" · OE 1, 22, 41', what=f"DM reply — {what}", final="DM reply text", vals=vals, kind=kind, band=b, dec=dec, oes=[1, 22, 41], dup="second deliverable (register count rows P4–P6)",
        cr="The register row counts and the DM counts grade the same fact", res="gate 6: the ask requires the counts in the reply; the register is a second prompt-required deliverable")
for k, st in [("ZOM-202", "Not shipped"), ("ZOM-280", "Not shipped"), ("ZOM-293", "Not shipped"), ("ZOM-173", "Editor only"), ("ZOM-200", "Editor only"), ("ZOM-277", "Editor only"), ("ZOM-315", "Editor only")]:
    add(src=f'"{S_DM}" · OE 2, 41', what=f"DM reply — {k} named as {st}", final="DM reply text", vals=f"F2 F23 `{k}` `{st}`; key in any format",
        kind="interpretation — Leonard's thread reply asks for the keys", band=3, dec="T22", oes=[2, 41], dup="second deliverable (register status rows)",
        cr="A run listing keys without status labels", res="the reply asks for 'the keys of the not shipped ones and the editor only ones'; the row needs the key under its status")
add(src=f'"{S_DM}" · OE 3, 41', what="DM reply — exactly 4 tickets named as Editor only", final="DM reply text", vals="F3 F23 `4` `Editor only`; exact count of keys listed as Editor only",
    kind="multi-source — the Editor only keys after the Sep 30 21:16 reply and the PR 265 review", band=5, dec="L7 L5", oes=[3, 19, 41], dup="volume row for the Editor only keys",
    cr="A run listing ZOM-162/163/201/250 as Editor only passes the four key rows", res="the volume row rejects the 8- or 9-key list; Leonard took those four off (D05HB64NMQU/1759267002.665190)")
add(src=f'"{S_DM}" · OE 7, 41', what="DM reply — ZOM-254 was replaced by ZOM-282", final="DM reply text", vals="F7 F23 `ZOM-254` `ZOM-282`",
    kind="interpretation — the notes doc asks for it; ZOM-282's note decides it", band=3, dec="L6", oes=[7, 18, 41], dup="second deliverable (register replaced-by row)",
    cr="Naming #401 as a replacement", res="rule 4: PRs that split numbers don't replace (harmonygames-Games/match3d#401#c_2)")
add(src=f'"{S_DM}" · OE 1, 15, 41', what="DM reply — a new player gets the starting tier when the 10th game ends, wins and losses both counting", final="DM reply text",
    vals="F18 F1 `10 games`; '10 games' or '10 levels played' pass; 'level 10' or 'after 10 levels' alone fails", kind="multi-source — the build over ZOM-42, ZOM-199 and the deck (rule 5)", band=5, dec="L4", oes=[1, 15, 41],
    dup="second deliverable (rules tab timing row)", cr="'10 levels played' could read as level 10", res="/prompt r12 rubric note: accept '10 games' or '10 levels played'; reject 'level 10'")

import re as _re
GENERIC = {"live", "editor only", "not shipped", "replaced", "in progress", "editor", "commenter", "viewer", "yes", "reset", "tickets",
           "rules in force", "tier 1", "tier -2", "0.5", "0.4", "0.3", "0.8", "50%", "80%", "10 games", "10th game", "> 90", "hp", "one sheet",
           "zm difficulty", "4 losses in a row", "1 win", "boxer", "monsterbase", "plumber", "robert@harmonygames.co", "arthur.blake@harmonygames.co",
           "leonard.hayes@harmonygames.co", "brian.foster@harmonygames.co", "24", "16", "4", "9", "3", "1", "10", "d05hb64nmqu"}
for r in rows:
    v = _re.sub(r"`([^`]+)`", lambda m: m.group(1) if m.group(1).casefold() in GENERIC else m.group(0), r["vals"])
    if not _re.search(r"`[^`]+`", v):
        tag = r["what"].split(" — ", 1)[-1]
        v = f"`{tag}` " + v
    r["vals"] = v
for i, r in enumerate(rows, 1):
    r['P'] = f"P{i}"
P = {r['what']: r['P'] for r in rows}
pid = lambda pre: [r['P'] for r in rows if r['what'].startswith(pre)]
cell = lambda s: str(s).replace('|', '/').replace('\n', ' ')
L = []
w = L.append
w("# 09 Rubric Writing Plan — Julia ZM difficulty baseline register (jl-zm-difficulty-baseline)")
w("Generated 2026-10-31 · Clock 2025-10-01T00:00:00Z (task universe_date) · Persona Julia Lawson julia.lawson@harmonygames.co · Tier Long-Horizon · "
  "Human time 16.75 h · OE status: /oe PASS 2026-10-31 (Audit-Report/2_oe_PASS_r2.md, Score 5, 41 events)")
w("Canonical outcome: brief §4b (one acceptance class per deliverable; re-synced to hardening round 4 on 2026-10-31) — W1 one sheet in the ZM Difficulty "
  "folder, tabs Tickets and Rules in force, 24 rows (16 Live, 4 Editor only, 3 Not shipped, ZOM-254 Replaced by ZOM-282); W2 Robert writer, Brian and "
  "Leonard commenter, Arthur reader; W3 9 comments (ZOM-199, ZOM-254, ZOM-173/200/277/315, ZOM-202/280/293); W4 a DM reply with 24 and the "
  "per-status counts, the 7 keys, 254 → 282 and the starting-tier timing.\n")
w("Row shape follows the accepted Robert and Douglas rubrics: volume rows for counts, one row per named exclusion (scope boundary of the "
  "register, failed by an idle Agent), ≤ 5 samples per repetitive group, one row per told fact. Weights follow 01a §2 round 4 with the "
  "playbook's ban on bundled exact-set rows applied (the 'exactly the 16 / the 4' sets became count rows plus samples).\n")
w("## A · Coverage matrix")
w("| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs + backticked literals; exact / tolerance) |")
w("|---|---|---|---|---|---|")
for r in rows:
    w(f"| {r['P']} | {cell(r['src'])} | {cell(r['what'])} | {cell(r['final'])} | {r['cat']} | {cell(r['vals'])} |")
w("")
w("## A2 · Grading risks and weight")
w("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk (per deliverable) / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |")
w("|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    w(f"| {r['P']} | {cell(r['prompt_title'])} | {cell(r['distractor'])} | {cell(r['ambig'])} | {cell(r['kind'])} | {r['band']} | {cell(r['dec'])} | {cell(r['group'])} | {cell(r['dup'])} | {cell(r['allfail'])} |")
w("")
w("## B · OE trace")
w("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |\n|---|---|---|---|")
for oe in range(1, 42):
    ps = [r['P'] for r in rows if oe in r['oes']]
    kind = "write" if oe >= 23 else ("discovery (calculation)" if oe == 22 else "discovery")
    own = ("yes — a write target gets its own result row" if oe >= 23 else "no — proved by the register cells and counts it produces" if oe == 22
           else "no — discovery; proved by the content row(s) that carry its result")
    show = ", ".join(ps) if len(ps) <= 12 else ", ".join(ps[:10]) + f" … ({len(ps)} rows)"
    if not ps and oe in (37, 40):
        show, own = f"{P['Comment volume — new comments on exactly 9 ZOM tickets']} (volume)", "no — sampled member of G3; the volume row covers it"
    if not ps and oe in (9, 13, 16, 20, 21):
        show = show or "—"
    w(f"| OE {oe} | {kind} | {show or '—'} | {own} |")
w("")
w("## C · Process candidates — three-condition test")
w("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |\n|---|---|---|---|---|---|---|")
w(f'| C1 | "{S_DM}" (reply after the register is in the folder) | the end state shows both, not their order | yes | yes | fails — the order of independent writes is a trace; the reply\'s counts already depend on the finished register | not Process; the DM count rows carry the dependency |')
w(f'| C2 | "{S_ASK}" (read both thread replies) | reading is a trace | yes | no — the exclusion rows and the count rows prove it | fails — a read is an execution trace | not Process; tighten the scope-boundary rows with F2 and F3 |')
w("")
w("## D · Spot-check groups")
w("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |\n|---|---|---|---|---|---|")
LV = ["ZOM-23", "ZOM-42", "ZOM-45", "ZOM-199", "ZOM-221", "ZOM-246", "ZOM-263", "ZOM-274", "ZOM-281", "ZOM-282", "ZOM-288", "ZOM-295", "ZOM-300", "ZOM-303", "ZOM-305", "ZOM-378"]
w(f"| G1 Live rows | F15 F20, 16: " + " ".join(f"`{k}`" for k in LV) + f" | {', '.join(pid('Status — ZOM-2') [:0] + [P[f'Status — {k} Live'] for k,_,_,_,_ in LIVE])} — ZOM-221 and ZOM-281 (tag-only; 281 assigned to someone else), ZOM-246 (attack-power amendment), ZOM-282 (PR 401 split is not a replacement), ZOM-45 (editor label read at runtime) | {P['Register volume — exactly 16 tickets with status Live']} | none — bundle (Rubric Writing §7; Eval 2.2) | no — repetitive status cells; the four non-Live groups are graded on every member |")
EN = ["Bikekid", "Boxer", "Cheerleader", "Chef", "FootballPlayer", "Karen", "Magician", "Mayor1", "Plumber", "MonsterBase"]
w(f"| G2 Enrage rows | F11, 10 monsters: " + " ".join(f"`{k}`" for k in EN) + f" | {', '.join(pid('Rules in force — Enrage — Boxer') + pid('Rules in force — Enrage — MonsterBase') + pid('Rules in force — Enrage — Plumber'))} — Boxer (speed ≠ damage), MonsterBase (base prefab, 0.8 also in Next pass), Plumber (ordinary) | {P['Rules in force — Enrage volume — 10 monster rows with speed and damage values copied from the Live tab']} | none — bundle (Rubric Writing §7; Eval 2.2) | no — repetitive copied cells |")
w(f"| G3 Checklist comments | F6 F20, 7: `ZOM-173` `ZOM-200` `ZOM-277` `ZOM-315` `ZOM-202` `ZOM-280` `ZOM-293` | {', '.join(pid('Comment — ZOM-173') + pid('Comment — ZOM-200') + pid('Comment — ZOM-277') + pid('Comment — ZOM-202') + pid('Comment — ZOM-280'))} — three Editor only (incl. ZOM-200, debug menu) and two Not shipped (ZOM-280 is Canceled) | {P['Comment volume — new comments on exactly 9 ZOM tickets']} | none — bundle (Rubric Writing §7; Eval 2.2) | no — one identical message per ticket; ZOM-199 and ZOM-254 (different content) are graded directly |")
w("")
bands = Counter(r['band'] for r in rows)
tot = sum(r['band'] for r in rows)
w("## E · Summary")
w(f"Rows {len(rows)} · Outcome {len(rows)} · Process candidates 2 (C1, C2 — both fail condition 3, none kept) — ≥ 1 Outcome ☑ (no Process ratio) · "
  "builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (G1 → Live count, G2 → enrage volume, G3 → comment volume) · "
  "predicted all-fail rows = 0 ☑ (harness tolerance 0; /rubric fails at ≥ 2; every value is persona-reachable — Visibility proof)")
w("Failure diversity: largest unit of discovery — see the gate line in Self-review (≤ 50% ☒ — the rules card 68daca5871dba40417a00383 sits upstream of "
  "every status, rules-tab, comment and DM-count row because every rule comes from it; it is named by Leonard's ask, the task's hub, not a hidden "
  "discovery; the same structural finding the accepted Robert and Douglas tasks carried) · chains landing on distinct rows ☑ (L1 thread reply → six "
  "scope rows and the Not shipped keys; L7 Sep 29 thread → four scope rows, Brian's share, the comment volume, the Editor only count and key volume; "
  "L5 PR 265 → ZOM-312 scope; L6 notes doc → ZOM-258 scope, Arthur's share, 254 → 282 in the DM; L4 build → starting-tier rows)")
w(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total weight {tot})")
w(f"Set size: {len(rows)} rows for 16.75 h (reference: 31 criteria for a ~10-hour task). Twelve named exclusions and seven told keys each get their own row (core asks); "
  "three repetitive groups are sampled.")
w("Coverage: requirements 8/8 (ledger R1–R8) · OEs 41/41 · writes 9/9 write kinds (sheet, two tabs, folder, 4 shares, 9 comments, DM) · told facts 5/5 "
  "(counts, keys, 254 → 282, starting tier, folder) · friction 0/0 (Friction: none)")
w("Four prohibitions: ☑ unstated expectations (no row for formatting, titles, the checklist ticks, a rage-by-level tab or thread-vs-top-level placement) "
  "☑ conclusions on ambiguous evidence (none on the critical path; enrage values for Mailman, Mayor2, PartyGirl never graded) ☑ grading the distractor "
  "(traps graded by their handling: scope rows, counts, Live for ZOM-282) ☑ hard-coded titles/phrasings (sheet title and comment wording delegated)")
w("Blocking: none for validity — no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share is a structural finding (rules card).\n")
w("Projection (replay of these rows on the six baselines on dd7536cdea3f, scratchpad rub/sim2.py): per-rollout 65 / 58 / 58 / 66 / 100 / 66%, "
  "average ≈ 69%, SD ≈ 0.14, pass@1 1/6. Failure patterns: {run-2, run-3} and {run-1, run-4, run-6}; run-1 differs from runs 4 and 6 on one row "
  "(ZOM-312 kept), so single-linkage puts three of five failing runs in one pattern (60% > 50%). No valid affirmative row separates them: run-1's "
  "only other difference is a comment on ZOM-312, and an absence-only 'no comment on ZOM-312' row fails Negative Criteria. Recorded as an open risk.\n")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)\n")
w("```\n" + (rd('vis.txt') or "(pending)") + "\n```\n")
w("Unscoped facts need no proof: Linear (F14, F15, F19 ZOM-303), Trello (F4–F6), GitHub (F16–F18) — `Evals/references/persona/acl.md`.\n")
w("## F · Shortcut probe")
w("```\n" + (rd('probe.txt') or "(pending)") + "\n```")
d = rd('disp.txt')
if d:
    w(d)
w("")
w("## Self-review\n")
w("Re-read as /rubric: `Evals/3_Rubrics_Eval.md` 1.4 and 3.1, the hg-strict-overrides-v1 table, `rubric_sampling.md` and `coherent_record.md`, walked against §A in order.\n")
w("Re-verified values this run (not from the ledger): the 24 rows, statuses and counts from support/task_work/jl_difficulty/truth.json recomputed against "
  "`linear/data.json` (31 title matches, ZOM-203/276 Duplicate) and the SQL comment rows; thread replies D05HB64NMQU/1759262838.442871 and "
  "D05HB64NMQU/1759267002.665190, the checklist 68dc033bf7d24e86b8a9cc67, the notes doc f_f494073fc667097c3c2c6b, the review harmonygames-Games/match3d#265#rc_7, "
  "the store builds mail and reply, and the Live tab f_0ba93ae0238d9ed4178212 (Boxer 0.5/0.4, MonsterBase 0.8/0.8, Plumber 0.3/0.3) by grep on "
  "01_Universe_Inject.sql; ZOM-42 and ZOM-303 through `tools/hg.py` (linear data.json); TierManager.cs line 31 and WinHistory.cs line 166 in the match3d export.\n")
w("| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |\n|---|---|---|---|---|")
for r in rows:
    w(f"| {r['P']} {cell(r['what'][:70])} | PASS | {cell(r['cr'])} | {cell(r['res'])} | none |")
GEN = [("Coverage (Eval 1.4, 3.1)", "PASS", "Counter: a run that never shares or never replies still passes many rows", "each write kind has its own rows: sheet, tabs, folder, 4 shares, comments, DM (F12, F22, F23)"),
       ("Negative criteria", "PASS (risk noted)", "Counter: the twelve scope rows read as absence checks", "each is a scope boundary of the required Tickets tab; an idle Agent with no register fails it (Robert /rubric: disguised_negative resolved when an idle Agent fails); ZOM-30 … ZOM-312 named by F2, F3, F7, F16"),
       ("Predicted all-fail re-check", "PASS — 0 rows", "Counter: 5 of 6 baselines missed both thread replies, so the L1/L7 rows look all-fail",
        "run-5 passed every one (base4 replay); both replies are check-sql YES for julia_lawson (D05HB64NMQU/1759262838.442871, D05HB64NMQU/1759267002.665190); none of the four bases applies"),
       ("Weights by work kind", "PASS", "Counter: scope rows at 3 are single lookups once the reply is read", "each needs the title scan (or the amendment) to put the ticket in and a later record to take it out — interpretation across two sources (QC Spec V2 weights)"),
       ("Failure patterns (baseline replay)", "RISK", "Counter: runs 1, 4 and 6 fail the same rows but one",
        "run-1 also kept ZOM-312 (harmonygames-Games/match3d#265#rc_7) and commented on it; no affirmative row can split them further — reported to the human"),
       ("Shortcut probe and diversity", "see §F / Summary", "Counter: the rules card lists every rule, so one read answers most rows",
        "the card gives rules, not values: the members, statuses and counts need the 498-ticket scan, the notes, the mail, both threads, the notes doc and the PR review (F2, F3, F7, F15, F16)"),
       ("Re-verified", "PASS", "Counter: ledger values could predate the §4b re-sync", "re-read this run (paragraph above); §4b now matches truth.json /counts")]
for c, v, cr, res in GEN:
    w(f"| {c} | {v} | {cr} | {res} | {'diversity.authority_share' if 'diversity' in c else 'failure-pattern risk' if 'patterns' in c else 'none'} |")
w("")
w("Unresolved: (1) diversity.authority_share — the rules card decides most of the weight by construction (every rule lives on it); a design finding for the "
  "human to accept, as on the Robert and Douglas tasks. (2) failure-pattern risk on the replayed baselines (60% vs 50%); the real gate runs on the verifier's results.")
dst = os.path.join(TI, 'Working_Files', '09_Rubric_Writing_Plan.md')
open(dst, 'w').write("\n".join(L) + "\n")
json.dump(rows, open(os.path.join(SC, 'rows.json'), 'w'), indent=0)
print(len(rows), 'rows; weight', tot, dict(bands))
