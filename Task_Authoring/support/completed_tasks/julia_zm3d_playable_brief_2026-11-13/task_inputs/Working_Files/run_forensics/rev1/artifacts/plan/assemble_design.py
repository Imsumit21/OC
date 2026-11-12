#!/usr/bin/env python3
"""Assemble Working_Files/01_Scenario_Design.md (design D2) from design_model.py, the draft manifest and the pasted tool outputs.
Design only: no prompt, Oracle Event or criterion text. Re-run after any model change, then re-run the stage gate."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_model as M
import planned_texts as TXT

HERE = Path(__file__).resolve().parent
WF = HERE.parent
OUT = HERE / "out"
RES = WF / "research"
man = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
S, B = M.SEED, M.BASE
PT = M.PACK_TICKET
read = lambda p: Path(p).read_text().rstrip("\n")
code = lambda t: "```\n" + t + "\n```"
def tick(n): return M.BY_NAME[n]["ticket"]
def names(cls): return ", ".join(l["name"] for l in M.members(cls))
def table(head, rows):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])
C = M.COUNTS
n_list, n_all, n_owed = M.N_LIST, len(M.LINES), len(M.OWED_WITH_TICKET)
n_vis = len(M.members("VIS"))
budget_total = sum(r["calls"] for r in man["call_budget"]); per_rec = sum(r["calls"] for r in man["call_budget"] if r["phase"] == "per-record")
W = sum(s["weight"] for s in surf["slots"])
brief_w = sum(s["weight"] for s in surf["slots"] if s["selector"][:2] == ["text", "brief"])
TICKS = f"{tick(M.LINES[0]['name'])} to {M.LAST_CHILD}"

P = []
P.append(f"""# Scenario Design — {M.SLUG} (design D2) · design only · contains no prompt, OE or criterion text

Written 2026-11-11 by `/create-scenario` (Claude, authoring session). D2 replaces D1 after two cold reviews (section 13). It is built on the reviewers' base fact pack (`Working_Files/research/base_facts_D2.md`, `research/object_categories.csv`), on base records re-read in this session through `tools/hg.py`, and on the generators in `Working_Files/plan/`. Planned (seeded) records are described, never written as SQL here. Ids of the form `C…/ts`, `ZOM-n`, `f_…`, `evt_…` without the word base are minted for `/create-injection`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `{ctx['universe']['clock_line']}`; seed bound `freeze_utc` {ctx['freeze_utc']} (Tue Sep 30 17:00 PT); `shutdown_rules_apply` false (the company operates normally) |
| Assignment (V3, 8 fields) | business_function Product · persona Julia Lawson · role Product Manager · competency Marketing and GTM · task_skill Authoring · task_type long-horizon · difficulty_mode hard · universe date October 1, 2025 07:00 (context_hash `{ctx['context_hash'][:12]}`, assignment_hash `{ctx['assignment_hash'][:12]}`) |
| Evals category | Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay and design requirements, art and prototype evaluation), inside Marketing and GTM: the artifact is the brief for a playable ad, a user-acquisition creative, and its hand-off list |
| Loss budget | Hard cap < 70 % (`difficulty_cap` 0.7); design target E[avg] ≤ 62 %; requester targets in the draft manifest `author_targets`: more than 130 counted calls in every run, average under 70 %, every other difficulty gate |
| Horizon | Long Horizon → `effective_profile: extreme`; `volume_exception {{call_budget_floor 220, per_record_floor 110}}` (budget {budget_total}, per-record {per_rec}; requester's words quoted in the manifest) |
| Theme screen | the storyline is ad production (items, exports, formats, sound, a vendor hand-off). The game's name cannot be avoided; no seeded text uses infection or outbreak vocabulary, and seeded text says 'ZM3D', 'the playable' or 'the game'. The pre-check is read for model-fallback events (`Hardness_Mastery.md` §12: suspected, not proven) |
| Fit census | `Working_Files/00_Assignment_Fit.json`: `NO NATURAL COHORT` (WARN mode); Gmail THIN for this persona, so no anchor and no coin-flip record sits in her mailbox; route S2x: the scenario is built by injection on base containers she can read |
| Persona card | `references/persona_cards/synthcut/julia_lawson.json`: earlier tasks used ZOM tickets and the match3d repository as cohorts (claims register, difficulty baseline, beta calendar, audience call). This design's cohort is the lines of one item pack on new Design-team tickets under one new parent; no earlier cohort, rule vocabulary or record set is reused |
| Role remit | Julia wrote the brief for the first playable: `{B['julia_dd_brief']}` (2025-03-14) and the vendor's reply 'thank you so much for this detailed brief' (`{B['vendor_thanks_brief']}`). For the second playable Frederick came to her first with the vendor's asset formats (`{B['fred_asks_julia']}`, 18 Sep), Brian asked her for the reference level (`{B['brian_asks_level']}`, 22 Sep) and she built it (`{B['julia_level']}`, 23 Sep). The design page names her: `confluence:{B['gdd']}` v2, 'Owner: Robert (Product). Design: Julia Lawson.' Role review: `Working_Files/00_V3_Authoring_Evidence.json` (`role_reviews.scenario`) |

Persona reach census (`persona_view.py reach julia_lawson --top 10`, verbatim):

{code(read(RES / 'reach_julia_top10.txt'))}

Identities (`entity.py resolve "Julia Lawson"`, §1c): Slack `EMPLOYEE_0005_SLACK_ID`, Linear `usr_8140f09bf9f1b94c` (member of `team_ART`, `team_DES`, `team_ENG` and `team_ZOM`, `/team_memberships`), GitHub `PERSON_0005_GITHUB_USERNAME`, Trello `793af7ca6940bf18eb516c75`, Contacts `8140f09bf9f1b94cb8ee2dd7`, Drive root `{B['julia_root']}` (owned). Her calendar's time zone is Europe/Istanbul; persona-written dates are still Pacific with UTC beside them when the day differs.
""")

# ------------------------------------------------------------------ 1 storyline
P.append(f"""## 1 Storyline

**The base, as read.** On 28 Aug the vendor lists four scenarios for a second playable, for Zombie Match 3D (`{B['vendor_scenarios']}`), and recommends Scenario 1, the core game in its simplest form (`{B['vendor_simple']}`). On 12 Sep Frederick says what Scenario 1 is for: filtering out players who will not like the game while staying true to the core game play (`{B['fred_retention']}`). On 15 Sep he chooses it and names the open questions: which items are on the board and which zombies; grenade, couch and plush doll 'would be a good start' (`{B['fred_scenario1']}`). On 16 Sep the vendor plans to start on 29 Sep, offers editable items 'aside from the 8-item set that you will provide for the board' and says which file types it takes, .fbx in binary format only (`{B['vendor_formats']}`); on 19 Sep it lists the assets it expects by group (`{B['vendor_asset_list']}`). Frederick relays the formats to Julia on 18 Sep and she points him to Brian (`{B['fred_asks_julia']}`, `{B['julia_names_brian']}`). On 23 Sep Brian tells Julia that Robert is fine with Frederick's items, and she builds the grenade, couch, plushie reference level (`{B['brian_robert_ok']}`, `{B['julia_level']}`). On 24 Sep the start moves to 6 Oct for late assets (`{B['vendor_oct6']}`); Brian sends the first zip, the level video with the win and fail conditions, and says more items and zombie types come later (`{B['brian_zip1']}`, `{B['brian_winfail']}`, `{B['brian_later']}`); the vendor misses only 'the duck asset' and wants the zombies as a Unity package (`{B['vendor_duck']}`); Brian sends the plushie the same day (`{B['brian_zip2']}`). On 25 Sep the vendor reports the zombie package holds prefabs only (`{B['vendor_blank_scene']}`); on 26 Sep Marcus builds a pack he tests in an empty project (`{B['anim_pack']}`) and Brian sends it (`{B['brian_pack3']}`). On 29 Sep the vendor asks for one primary animation and four zombies (`{B['vendor_zombie_ask']}`); that evening Frederick pauses development 'for a month or so' (`{B['fred_pause']}`); on 30 Sep the vendor sets the new start for 3 November (`{B['vendor_nov3']}`). Nothing in base after the pause concerns the playable (fact pack §2, §3).

**The job (planned).** On Tue 30 Sep 18:21 UTC (11:21 PT), after the investor call that fills his 17:30 to 18:09 that day, Frederick asks Julia in their DM (`{S['ask']['id']}`) to do for this playable what she did for the first: write the brief PlayableX builds from, and say where the item pack stands, for the game as it is today. He names three things it starts from: Brian's pack list, Robert's picks, his own hand-off notes. The deliverables are a brief (a Google Doc) and a hand-off list (a Google Sheet) in her Drive, the ticket follow-through the notes ask for, the three counts back to him in the DM and both links in the PlayableX channel.

**What the plan adds between the first zip and the pause.** Base leaves this stretch open: the vendor wants an 8-item set and extra items, and Brian has said they come later. In the plan Brian opens a pack ticket in the Design team on 25 Sep (his own last tickets there, `DES-307` and its children of 7 May, are a parent with bare-titled sub-tickets) with one sub-ticket per line of a pack list ({n_list} lines), and works through it until 29 Sep, leaving a note on each ticket. Robert names the eight on 25 Sep and changes one in a reply on 26 Sep. Five other records say something the tickets do not (section 5).

**Why now, against the pause.** The base lines of 29 Sep are about vendor development on a game that may change: Leonard asks whether to pause 'if they haven't started yet' (`{B['leonard_pause_q']}`) and Brian answers that he sent the assets and they have not started (`{B['brian_sent']}`). The planned ask agrees with them: it does not say the playable ships as specified ('if the core changes we redo that part with them in November'), and what it asks for is the part that slipped the start twice: which files PlayableX holds, which are fit to send and which are owed. Leonard's group DM with Brian and `#executives` are not readable by Julia and are not cited.

**Anchors per service.** Slack: the ask `{S['ask']['id']}` (planned); the PlayableX channel `{M.VENDOR_CH}` (base); Robert's posts `{S['picks']['id']}` and `{S['zpicks']['id']}` (planned, #zombie-design). Docs: Frederick's notes `{S['notes']['id']}` (planned); base `{B['playable_feedback_doc']}`. Sheets: Brian's pack list `{S['tracker']['id']}`, Calvin's sources sheet `{S['c2_sheet']['id']}` (planned). Linear: {PT} and its children {TICKS} (planned; base precedent `{B['zom97']}`, 'REVISION FOR ITEMS', 51 children titled with object names). Slides: Julia's deck of the reference level `{S['deck']['id']}` (planned). Calendar: the kickoff hold `{S['hold']['id']}` (planned; base precedent `evt_257421bc09196edbf28758`, the 2025-03-12 vendor meeting Frederick organised with Julia invited). Contacts: `{S['contact']['id']}` (planned). GitHub: base `{B['pr462']}`. Confluence: base `{B['gdd']}`. Trello: base card `{B['trello_kickoff']}` with a planned comment `{S['trello_note']['id']}`.

**Universe KB.** Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the spine beats '2025-09-15 Season Pass built for Zombie Match (match3d) - PR #438' and '2025-09-30 PR #476 Vision bot opened and merged'; neither is touched. `cohorts.json`: no fit — every KB cohort is a base Linear state or label set (`LIN-S01` … `LIN-L30`); this cohort is the lines of one pack on seeded ZOM tickets, defined by a seeded sheet. `trap_catalog.json` entries the traps stand on: `C01` (thread replies that correct: T5), `C02` (a parent states a resolution and another record says it still fails: T1, T7), `D05` (title families with version markers: avoided), `K02` (app-name lineage: not used as an alias), `N01` (ticket series collisions: ZOM numbers overlap ART and ENG numbers; every ticket is cited with its team key), `P01` (shared first names: §1c).

### Coupling seams

- The pack list `{S['tracker']['id']}` has no state column, and every undelivered line ticket ({TICKS}) is In Progress: a line's state needs Brian's note on its own ticket joined to a rule in the notes `{S['notes']['id']}`.
- 'Exported and opens' on a ticket and 'usable by PlayableX' are two facts. The second lives where the file, the art or the sound is discussed (`{S['a1_post']['id']}`, `{S['a2_dm']['id']}`, `{S['c2_sheet']['id']}`), not on the ticket.
- The time a file was handed over and the time the art last changed are in different services: the ticket note on {tick('Cactus Plant')} and GitHub `{B['pr462']}`.
- The eight on the board are fixed by one person's two messages in two channels: `{S['picks']['id']}` and `{S['c3_reply']['id']}`.
- The sound rule in `{S['notes']['id']}` is about what is ours to pass on; the sound tickets ({tick('Matching sound')} to {tick('Background music')}) only state the file type.
""")

# ------------------------------------------------------------------ 1a coherence audit
audit = [
    ("PlayableX channel thread order", "temporal", "three start dates in one channel", f"`{B['vendor_formats']}`, `{B['vendor_oct6']}`, `{B['vendor_nov3']}`", "hazard T02 (files not in chronological order): none of these; card SC-13 (ZM3D beta date)", "fold: a dated claim sequence, the last stands (T8); the beta date is never cited or graded"),
    ("Leonard's Playable Kickoff card", "temporal", "dateLastActivity against its actions", f"`{B['trello_kickoff']}` (created 2025-08-01, moved 2025-09-13, no comment)", "hazard T06", "fold: the planned comment moves the card's and the board's dateLastActivity and the badge's comment count"),
    ("the vendor's name", "semantic", "'PlayableX' in Slack text, a masked token in mail and calendar titles", f"`{B['vendor_formats']}`; gcal `evt_257421bc09196edbf28758`", "hazard S03: none in scope; trap catalog X04 (uneven masking)", "fold: seeded text uses the Slack spelling Julia sees; no row depends on a mail or calendar title"),
    ("masked names in Slack text", "semantic", "one token stands for both Julia and Claire", f"`{B['fred_asks_julia']}`; fact pack §0", "none listed", "avoid: no seeded text uses a masking token; people are named or mentioned by Slack id"),
    ("design page against its comments", "cross-service referential", "tray 7 on the page, a 6-slot proposal in a comment", f"`{B['gdd']}` with `confluence:{B['gdd_c1']}`, `confluence:{B['gdd_c2']}`", "cards SC-8, SC-38, SC-58 (other sentences of the same page)", "fold: Robert's reply on the page keeps 7 (T9); the page's sentences on the glass crash, the Season Pass date and the monster roster are neither cited nor graded"),
    ("Slack links to Google files", "cross-service referential", "native ids never equal export ids", f"planned Slack records, e.g. the ask `{S['ask']['id']}`", "hazard R04", "excluded: no seeded Slack text carries a document link; the ask names the notes in words"),
    ("calendar invitations and share lists", "cross-service referential", "invitation mails without a calendar row; a departed person on base invites", f"the planned hold `{S['hold']['id']}`", "hazard R08; card SC-36", "fold: the hold is seeded, single, with four attendees who are all active at the clock, one row per attendee calendar and one invitation mail each (INT-11); no base invite or channel roster is used for the share list"),
    ("channel membership", "cross-service referential", "leavers stay listed", f"`{M.MATCH3D_CH}`, `{M.VENDOR_CH}`", "card SC-7", "not graded: membership is used only to show Julia can read a container (persona_view can-see), never as an answer"),
    ("thread counters", "quantitative", "reply_count, reply_users_count, latest_reply of Julia's bow post", f"`{B['art_bow_root']}` (1 reply in base: `{B['art_bow_claire']}`)", "hazards Q01, Q02, Q03", "fold: the planned reply updates the three counters as companions"),
    ("counts in the deliverables", "quantitative", f"{C['Delivered']} Delivered, {C['Ready']} Ready, {C['Owed']} Owed of {n_all} lines", f"`plan/design_model.py`; the pack list `{S['tracker']['id']}` and {TICKS}", "hazard Q01 kind (a stated count against the rows): none in base for these records", "fold: every count comes from the model; no base figure is restated"),
    ("merged pull request without review", "state/lifecycle", "match3d#462 merged with no human review", f"`{B['pr462']}`", "hazard L09; card SC-50 (bot comment authorship)", "fold: the task uses its times and the models its comment names, never its review state or which account commented"),
    ("Linear state against shipped work", "state/lifecycle", "tickets open after the work shipped", "`ZOM-513`, `ZOM-514`, `ZOM-564`, `ZOM-563`, `ART-790`, `ART-792`", "card SC-16; card SC-22 (time_in_status_minutes); hazard L06: none in scope", "avoid: Maracas (ZOM-513) and Helmet (ZOM-514) are not on the list, nor any object with an open ticket under ZOM-97 (Gas Can, Indoor Plant, Curling Iron, Bagel, the plates); new tickets carry no time_in_status value"),
    ("ids of seeded records", "identifier/format", "Slack message id, Linear keys and comment ids (97 keys after `DES-312` of 7 May 2025, the Design team's last base ticket, so numbers and dates run in order), Drive ids, Trello action id", f"`plan/check_ids.py` output: {PT} to {M.LAST_CHILD}, `{S['notes']['id']}`, `{S['trello_note']['id']}`", "hazards I01, I02, I10 (`usr_Robert`), I15", "fold: ids follow the base schemes and the generators' conventions; Robert's Linear id is `usr_Robert` as in base; no collision (§12)"),
    ("object names and categories", "other", "the July export's names differ from the game's; four masked zombie names", f"`research/object_categories.csv` (the repository tree); `{B['anim_zombies']}`", "none listed", "fold: every board item takes the tree's name and category; the zombies are one line; Robert's planned answer uses the four unmasked names"),
    ("people and roles", "other", "Frederick's founder status; time zones", f"`{B['fred_asks_julia']}`", "cards SC-49, SC-70", "not stated and not graded: no seeded text gives anyone a title or a time zone; seeded times are within each author's September posting hours (fact pack §5)"),
]
P.append("## 1a Coherence audit\n\nScope = every record a correct run opens: the ask, the notes, the pack list, the pack ticket and its " + str(n_list) + " children with their notes, the PlayableX channel in full, Robert's two posts in #zombie-design, #zombie-art from 24 Sep, Julia's DMs with Claire and with Brian, #zombie-match3d and #zm-animations for the week, Calvin's sheet, Julia's deck, the design page with its comments, the kickoff hold, the contact, the Playable Kickoff card, match3d#462 and #460. Hazard ids are from `references/universe_kb/by_universe/synthcut/coherence_hazards.json`. Known-data-issue cards read: `references/known_data_issues/synthcut.md` (SC-1 to SC-73); the cards the scope touches are SC-13, SC-58, SC-8, SC-38, SC-16, SC-22, SC-36, SC-7, SC-50, SC-49 and SC-70, each with its disposition below.\n\n"
         + table(["Record", "Category", "Fields", "Pointer", "Hazard / card", "Disposition"], audit)
         + f"""

**Sibling-defect sweep.** Designed defect kinds and their base siblings: (a) an export that is 'done' and unusable: base has the 24 Sep zombie package ('Only the prefabs were included', `{B['vendor_blank_scene']}`), repaired on 26 Sep and kept as a control (T10); (b) art changed after a hand-over: base has match3d#462 (Cactus Plant, Chainsaw, Cone on the list; Kettlebell, Dart Board and Candy off it) and the rocking chair rework of 29 to 30 Sep (`{M.ART_CH}/1759190391.487809`), not a game object yet; (c) a pick changed in a reply: base has Julia's own grenades-and-shuriken idea, answered 'remain as is' (T13); (d) a rights question on sound: base has two system sounds to be swapped (`{B['robert_copyright']}`), which are on Calvin's sheet and not on the pack list. Windows read in full: the PlayableX channel from 28 Aug, #zombie-design and #zombie-art from 22 Sep, #zm-animations 24 to 30 Sep, Julia's DMs with Frederick, Claire and Brian for September (fact pack §2, §3, §6).

**Base facts the plan must not contradict** (each checked against the fact pack and the records cited): the first zip held the reference level's six item variants, the zombies, the background and the cannon (`D07G5QWN3TM/1758712833.442809`, `{B['brian_zip1']}`); Claire holds the FBX files and sends them, and colours are assigned in Unity (`D076Y0SDV18/1758713188.374029`), which is why twelve planned lines came out of Unity's exporter; the vendor does not use Unity for playables (`{B['vendor_zombie_ask']}`) and takes .fbx only in binary; no export tool exists in base and none is planned; object work is ticketed in ZOM (`{B['zom97']}`), where Brian created 13 issues in September; Dart Board and Candy have models and no object data, so they are not lines; match3d#460 (merged 21:51 UTC on 24 Sep) adds new objects and touches the two shared texture atlases without naming a line; Robert asked for the thicker health bar before the zip (`{M.MATCH3D_CH}/1758691270.557429`) and no UI piece is planned as sent; the combo scale was pitched by Calvin from a sample Robert gave (`{B['sfx_scale']}`), which Calvin's planned sheet repeats; the vendor's price and bundle choice are open in a DM Julia cannot read and no seeded text states a price. One base record holds a credential (`D05UDNCCFEW/1757008285.488349`); it is neither cited as evidence nor copied.
""")

# ------------------------------------------------------------------ 1b speakers
speak = [("Frederick Stone", "frederick.stone@harmonygames.co", f"the ask `{S['ask']['id']}`, the notes `{S['notes']['id']}`, the hold `{S['hold']['id']}`, the contact"),
         ("Brian Foster", "brian.foster@harmonygames.co", f"the pack list `{S['tracker']['id']}`, the pack ticket {PT} and its {n_list} children with a note on each, his log of the outgoing folder `{S['c4_log']['id']}`"),
         ("Robert", "robert@harmonygames.co", f"the eight `{S['picks']['id']}`, the zombie answer `{S['zpicks']['id']}`, the reply `{S['c3_reply']['id']}`"),
         ("Claire Morgan", "claire.morgan@harmonygames.co", f"the message to Julia `{S['a2_dm']['id']}` (Turkish)"),
         ("Marcus Bennett", "marcus.bennett@harmonygames.co", f"the #zombie-match3d post `{S['a1_post']['id']}`"),
         ("Calvin Price", "calvin.price@harmonygames.co", f"the sound sources sheet `{S['c2_sheet']['id']}`"),
         ("Leonard Hayes", "leonard.hayes@harmonygames.co", f"the Trello comment `{S['trello_note']['id']}`"),
         ("Julia Lawson", "julia.lawson@harmonygames.co", f"her deck of the reference level `{S['deck']['id']}` (23 Sep)"),
         ("Martin Walsh", "martin.walsh@harmonygames.co", "named on the Fonts ticket as holder of the font files; no seeded voice")]
P.append("## 1b Active speakers\n\nStatus from `references/universe_kb/by_universe/synthcut/activity.json` (`status_at_clock`); seeded times sit inside each person's September posting hours (fact pack §5). The PlayableX staff (`PERSON_6078_SLACK_ID`, `PERSON_3937_SLACK_ID`) are Slack-only ids with no status row and get no seeded voice: every vendor statement the design uses is a base message.\n\n"
         + table(["Person", "Email", "status_at_clock", "Seeding role"], [(n, e, "active_sep_2025_quiet_in_oct", r) for n, e, r in speak]))

# ------------------------------------------------------------------ 1c identity
resolve = read(RES / "entity_resolve.txt").split("### ")
keep = [blk for blk in resolve if blk.split("\n")[0] in ("Julia Lawson", "Frederick Stone", "Brian Foster", "Claire Morgan", "Robert", "Marcus Bennett", "Leonard Hayes", "EMPLOYEE_0006_SLACK_ID")]
res_txt = "\n".join("### " + "\n".join(b.rstrip().split("\n")[:8]) for b in keep)
P.append("## 1c Identity traps\n\n`entity.py collisions` (verbatim):\n\n" + code(read(RES / "entity_collisions.txt")) +
         "\n\n`entity.py resolve` for the people the design names (first lines of each):\n\n" + code(res_txt) + f"""

Pinned entities and their lookalikes: Claire Morgan (`EMPLOYEE_0009_SLACK_ID`, Linear `usr_7fe31e7ec8199618`) against the GitHub-only 'Claire' login; Robert (Linear `usr_Robert`, hazard I10) has no surname in any service; Calvin Price has two GitHub logins and one Slack id (`EMPLOYEE_0006_SLACK_ID`); Marcus Bennett is `EMPLOYEE_0002_SLACK_ID` (Linear `usr_c77c50cc15c5342d`), not the two other Marcuses of the roster; `EMPLOYEE_0032_SLACK_ID`, the engineer Brian asked about assets on 24 Sep, is unidentified in every service and gets no seeded voice. Victor Barnes left in April 2025 and has no seeded voice. No second account is created for anyone and no trap depends on a malformed id. The PlayableX intake contact is a role address, not a person, so it duplicates nobody.
""")

# ------------------------------------------------------------------ 2 cohort
cls_rows = [("Delivered", "W", "in PlayableX's hands and usable: the two zips of 24 Sep and the 26 Sep pack (base)"),
            ("Ready", "READY", "FBX from Claire (or .wav from the project), opens or plays, current, nobody changing it"),
            ("Owed, stated on the line's own ticket", "VIS", "not exported or not sent, in Brian's words, with who has it"),
            ("Owed, EXPORT", "A1", "FBX saved out of the Unity project on 25 Sep: the text kind, which the vendor does not take (Marcus's post)"),
            ("Owed, ARTHOLD", "A2", "category Bathroom: Claire is redoing the UVs; Friday's files are the old state (her message to Julia)"),
            ("Owed, REVISED", "C1", "the model changed on 25 Sep after the file was handed over (base)"),
            ("Owed, ZIP", "C4", "in Friday's zip of instruments, which will not unpack (Brian's own log of the outgoing folder)"),
            ("Owed, AUDIO", "C2", "from a library seat or a bought pack (Calvin's sheet); the notes hand over only what is ours"),
            ]
cat_rows = []
for cat in list(M.BOARD) + ["(not a board item)"]:
    ls = [l for l in M.LINES if l["on_list"] and (l["category"] == cat if cat in M.BOARD else l["kind"] != "Board item")]
    by = {}
    for l in ls: by[l["cls"]] = by.get(l["cls"], 0) + 1
    cat_rows.append((cat, len(ls), ", ".join(f"{k} {v}" for k, v in by.items())))
P.append(f"""## 2 Cohort spine

**Rule (closed).** A line is one row of Brian's pack list `{S['tracker']['id']}` ({n_list} rows: 84 board items in seven of the game's categories, the cannon, the background, the zombie characters, six sound cues, the item visuals, the UI elements, the fonts). The list has {n_all} lines; key = the line's name, spelled as the pack list spells it. Nothing adds a line: the ask has no clause about the vendor's requests, the vendor's 'duck asset' is the Plushie Chick line and its 'rocket launcher' the Cannon line (T16), and the choice of animation and zombies goes in the brief.

**Truth by class** (`plan/design_model.py`; Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}; without the five hidden records: {M.NAIVE['Delivered']} / {M.NAIVE['Ready']} / {M.NAIVE['Owed']} of {n_list}):

""" + table(["State", "Lines", "Why", "Members"], [(st, len(M.members(c)), why, names(c)) for st, c, why in cls_rows]) + f"""

**Every category is mixed** (class counts per category on the pack list; W delivered, READY, VIS owed on its own note, A1 / A2 / C1 / C2 / C4 the hidden classes):

""" + table(["Category", "Lines", "Classes"], cat_rows) + f"""

**Surfaces and shortcut audit** (manifest `cohort.evidence_surfaces`):

""" + table(["Surface", "Records", "Calls each", "Bulk call that does not cover it", "Why it cannot be skipped", "Serves"],
            [(f"{s['service']} `{s['tool']}`", s["records"], s["per_record_calls"], s["why_no_bulk"], s["short_circuit"], f"{s['requirement']}: {s['decides']}") for s in man["cohort"]["evidence_surfaces"]]) + f"""

**Predicate.** The notes define the three states: Delivered, PlayableX has the current file and can use it; Ready, exported in a format they take, it opens, it is the current version and nobody is changing it; Owed, anything else, with what is owed and who has it (whoever has to do the next thing). Brian's note stands unless something later says otherwise. **House rule that overrides the natural reading:** a ticket that says 'exported, opens' is not Ready when the file is in a format the vendor refuses, the art is being redone, the art changed afterwards, the zip it sits in will not unpack, or the sound is not ours to pass on. (The board set is a separate column: PICKS changes which two lines are Default and Extra, not a state.) **Dual regime by date:** a note stamped 08:05 UTC on 25 Sep predates the model change created at 11:43 UTC and merged at 23:15 UTC that day (`{B['pr462']}`). **Boundary records:** the Plushie Chick delivered in a second zip the same day (`{B['brian_zip2']}`); the zombie pack sent twice (T10); Kettlebell, Dart Board and Candy, touched by the same pull request and not lines (T18).

**Necessity of the per-line read.** {n_vis + len(M.members('A1')) + len(M.members('A2')) + len(M.members('C1')) + len(M.members('C2')) + len(M.members('C4'))} of the {n_list} listed lines are Owed and nothing upstream says which: the pack list has no state column, every undelivered ticket is In Progress, ticket titles and descriptions carry the line's name only, and no category is of one class. The {n_vis} lines that are Owed on their own note sit in ten groups, so a run that samples a few tickets per category gets the three totals and its sampled states wrong. Notes state raw facts (where the file came from, when, whether it opens), never the state. Purpose of the volume, per group: 84 board items because the vendor asked for an 8-item set plus extra items it can make editable and Brian promised more items later; six sound cues, the item visuals, the UI elements and the fonts because the vendor's 19 Sep list names them; the cannon, the background and the zombies because they went. No line exists to raise a count, and each line's state is a cell of the hand-off list. Base holds no Linear comment at all, so every comment a run reads here is one of this task's notes; that is named for the injection dossier.

**Ids.** {PT} is the pack ticket; children {TICKS} follow the list order (`plan/design_model.py`). Base highest Design number is `DES-312` (`conventions.json` linear.max_number; every minted key looked up in `plan/check_ids.py`, scan complete). Collision check: §12.
""")

# ------------------------------------------------------------------ 3 authorities
P.append("## 3 Hidden authorities\n\n" + table(["Id", "Name (what it governs)", "Home", "Record", "Governs", "Decoy and its scope", "Findability"],
    [(a["id"], a["name"], a["home_service"], ", ".join(f"`{x}`" for x in a["seeded_ids"]), ", ".join(a["governs"]),
      f"{a['decoy_service']}: " + ", ".join(f"`{x}`" for x in a["decoy_base_pointers"] + a["decoy_seeded_ids"]) + f" — {a['decoy_scope']['dimension']}: {a['decoy_scope']['decoy']}",
      f"a search for '{a['findable_query']}' returns it; the ask names it in words") for a in man["authorities"]]) + f"""

`governs` lists do not overlap (H1: R2, R3, R5, R6; H2: R1; H3: R7). H1 has a same-service decoy with an adjacent scope: Leonard's 'Playable Feedback' (`{B['playable_feedback_doc']}`, the first playable). Each authority is named by what it governs or who issued it ('my hand-off notes', 'Brian's pack list', 'the kickoff hold'); no decoy carries a self-advertising cue. Findability of planned records is proven on the SQL at `/create-injection` (`persona_view.py check-sql`); the base decoys are YES in the reach table (§10).
""")

# ------------------------------------------------------------------ 4 lattice
P.append("## 4 Delegation lattice\n\n" + table(["Anchor", "Anchor name (noun phrase, ≤ 6 words)", "Record"],
    [(a["id"], a["prompt_reference"], f"`{a['locator']}`") for a in man["anchors"]]) + f"""

**Hub.** Frederick's DM `{S['ask']['id']}` (planned wording in `plan/planned_texts.py`). It delegates by role: 'Brian's pack list', 'Robert's picks', 'My hand-off notes'. It names no location, no id and none of the records in §5 that decide a row. The notes `{S['notes']['id']}` say what the brief covers, name the list's columns and the three state words, give the rule for later statements and changed art, the sound rule, the ticket follow-through and the sharing; they point at the pack ticket, the design page, the deck, the kickoff hold and Contacts by name, and at nothing that decides a hidden row.

**Incorporation table** (every `delegation_quote` is an exact substring of the delegating record's planned or base text; the gate reads them):

""" + table(["Fragment", "Service · container", "Kind", "Chain", "Delegated by", "Words (verbatim)", "Requirements", "Names"],
    [(f["id"], f"{f['service']} · `{f['container']}`", f["kind"], " → ".join(f["incorporated_via"] + [f["id"]]), f"`{f['delegated_by_record']}`",
      "'" + f["delegation_quote"] + "'", ", ".join(f["requirement_ids"]), ", ".join(n["id"] for n in f.get("names_authorities", [])) or "—") for f in man["ask_fragments"]]) + f"""

{len(man['ask_fragments'])} fragments over 8 services. **Amendment:** K11, Robert's 26 Sep reply, in another channel and a day after K3; it changes one item (the dynamite) and the ask keeps his latest word ('unless he's changed them since'); nothing later re-asserts the dynamite. **Non-authoritative instruction distractors:** Julia's own grenades-and-shuriken idea (T13), Frederick's three-item 'good start' and the reference level (T14), the March FBX rule from the first playable (T12), Leonard's card (T11).
""")

# ------------------------------------------------------------------ 5 chains, traps, portfolio, liveness
P.append("## 5 Chains and trap register\n\n**Chains** (six, six distinct root causes):\n\n" + table(["Chain", "Root cause", "Hops (service: record — finding)", "Ends in"],
    [(c["id"], c["root_cause"], "<br>".join(f"{h['service']}: `{h['record']}` — {h['finding']}" for h in c["hops"]), c["ends_in"]) for c in man["chains"]]) +
    "\n\n**Trap register:**\n\n" + table(["Trap", "Family", "Services", "Records", "Req.", "Expected wrong reading", "Resolver", "Discovery order"],
    [(t["id"], t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else ""), ", ".join(t["services"]),
      ", ".join(f"`{x}`" for x in ((["confluence:" + B["gdd"]] if t["id"] == "T9" else []) + t["seeded_ids"] + t["base_pointers"])[:4]), t["requirement"], t["expected_wrong_reading"], t["resolver"], t.get("discovery_order", "—")) for t in man["traps"]]) + f"""

Supersession chronology (oldest first, timestamps from the records): T2 Brian's note on {tick('Bathtub')} 2025-09-26T11:20Z → `{S['a2_dm']['id']}` {S['a2_dm']['at']}; T3 Brian's note on {tick('Cactus Plant')} 2025-09-25T08:05Z → `{B['pr462']}` created 2025-09-25T11:43Z, merged 23:15Z; T5 `{S['picks']['id']}` {S['picks']['at']} → `{S['c3_reply']['id']}` {S['c3_reply']['at']}; T8 `{B['vendor_formats']}` 2025-09-16 → `{B['vendor_oct6']}` 2025-09-24 → `{B['vendor_nov3']}` 2025-09-30 (three versions); T15 `{S['deck']['id']}` {S['deck']['at']} → `{S['picks']['id']}`. Every seeded timestamp is before the seed bound; the only later value is the plan field of the hold (start 2025-11-03T17:00Z).

**Hardness v2 trap selection.** Two separate cross-source decisions carry the difficulty, each naming the convincing wrong source and the record that beats it: (1) trap 1, proving done across services — EXPORT: the ticket note on {tick('Refrigerator')} (Brian, 25 Sep: .fbx, opens, in the outgoing folder) against Marcus's 26 Sep post in #zombie-match3d `{S['a1_post']['id']}` (he tested the zombie pack that day; later; another service), joined to the vendor's binary-only rule `{B['vendor_formats']}`; (2) trap 2, a correction somewhere else — ARTHOLD: Brian's note on {tick('Bathtub')} (Friday's file looks right) against Claire's 29 Sep message to Julia `{S['a2_dm']['id']}` (she made the file; later; another service and language). Four more are used: trap 4 dates (REVISED, base `{B['pr462']}`), trap 5 a rule in the data (AUDIO, `{S['c2_sheet']['id']}`), trap 2 again (PICKS: a later reply `{S['c3_reply']['id']}` that names no item), a second document by the list's owner (ZIP, `{S['c4_log']['id']}`), trap 9 work already done (T10: the zombie pack `{B['brian_pack3']}`). No correction sits in the superseded record's container, in an anchor's container or on a delegation path (`hardness_v2_check` SAME_PLACE below). Volume and arithmetic carry no difficulty.

### Mechanism portfolio (S5a)

Candidates considered (grounded in the fact pack and the census files) and the selection:

""" + table(["#", "Candidate", "Coupling", "Verdict", "Reason (record)"], [
    (1, "EXPORT: FBX files saved out of the Unity project are the text kind", "ticket 'FBX, opens, looks right' → format the vendor refuses → Owed", "selected", f"the vendor's rule is base (`{B['vendor_formats']}`, `{B['vendor_asset_list']}`) and reached Julia herself (`{B['fred_asks_julia']}`); colours are assigned in Unity in base, which is why Brian would export from the project"),
    (2, "ARTHOLD: the artist is redoing one category's UVs", "ticket note → DM → Owed (art)", "selected", f"Claire makes every board item and keeps Julia posted on sets for her levels (`{M.DM_CLAIRE}/1758555266.534569`); she is not in the PlayableX channel"),
    (3, "REVISED: the model changed later the day its file was handed over", "note time → pull request → Owed", "selected", f"all base: `{B['art_cactus']}`, `{B['art_cone']}`, `{B['art_claire_pr']}`, `{B['pr462']}`, `{B['robert_new_colours']}`"),
    (4, "AUDIO: only sound that is ours is handed over", "file type passes → sources sheet → Owed", "selected", f"base: Robert sources sound from a Soundly seat and bought packs (`C07JYF2CFFU/1737054449.137119`) and two sounds were already a copyright problem (`{B['robert_copyright']}`)"),
    (5, "PICKS: Robert changes one pick in a reply elsewhere, naming no item", "the eight → reply → board set and the brief", "selected", f"parent `{B['art_bow_root']}` is Julia's own base post about the bow; the reply says 'it' and 'the last one on my list', so no item name makes it a search hit (path exposure, §12)"),
    (6, "ZIP: one zip that will not unpack, noted in the packer's own log of the outgoing folder", "tickets say in the folder and fine → the log → Owed", "selected", f"a comment on the pack ticket {PT} would sit on a named record (path exposure flagged it); the log `{S['c4_log']['id']}` is a second document by the list's owner that nothing links"),
    (15, "six items Robert adds to the list in his reply (D2 before the path-exposure run)", "reply → six new lines and tickets", "rejected", f"a reply that names items is the newest Slack hit for each name (`path_exposure.py`: EXPOSED on `{S['c3_reply']['id']}`), so it would be found by every keyword sweep"),
    (7, "an 'object browser' whose batch export writes empty shells (D1)", "ticket 'exported' → tool bug → Owed", "rejected", f"no such tool exists in base and Arthur has no such post (reviewer 1, finding 4; `{M.MATCH3D_CH}/1738678859.796159` is the kind of post base does have)"),
    (8, "Unity packages with prefabs only, as with the zombies", "ticket 'exported' → hollow package → Owed", "rejected", f"a Unity package is not a format the vendor takes for 3D (`{B['vendor_formats']}`), so the lines would be Owed on the hub's own text with nothing to find"),
    (9, "item effects as shipped (a design line per item)", "ticket text → pull request review", "rejected", f"effects are spread over dozens of base messages in #zombie-design `{M.DESIGN_CH}`; any seeded effect risks a base contradiction"),
    (10, "which zombies have full animation sets", "enemy set → animations channel", "rejected", f"five of the nine zombie names are masked in base (`{B['anim_zombies']}`) and card SC-58 covers the roster on `{B['gdd']}`"),
    (11, "UI pieces changed after the first zip", "sent UI → later pull request", "rejected", f"base does not say UI went in the zip, and `{B['pr460']}` and the later UI pull requests do not name pieces: a fork"),
    (12, "a due date on a calendar hold against 'a week before'", "rule arithmetic → hold", "rejected", f"two fair dates with no resolving record; the hold `{S['hold']['id']}` is kept only for its attendees"),
    (13, "open art tickets as 'somebody is changing it' (Maracas, Helmet, Indoor Plant)", "ticket state elsewhere → Owed", "rejected", "card SC-16: `ZOM-513` and `ZOM-514` are open after the work shipped; those objects are kept off the list instead"),
    (14, "a brief that is valid under each pivot option", "pivot options → brief", "rejected", f"the options are undecided in base (`{B['leonard_pause_q']}`): no truth value"),
]) + "\n\n**Selected rules** (one per solver rule; draft manifest `mechanism_portfolio`). Ledger priors for `claude-opus-5-5`, UNCALIBRATED (`hardness_ledger.py priors`; `plan/out/ledger_priors.txt`):\n\n" +
    table(["Rule", "Mechanism", "Prior family · prior · record ids", "Natural reading", "Decides", "Control · over-application", "Stays hard after complete retrieval", "Natural call that returns the decider", "Slots only it flips"], [
    ("EXPORT", "A24", "done_gap · Beta(1.0, 2.86) mean 0.26 · `hev_7af7471ca0d3855f`, `hev_bdb9590893044914`, `hev_e30a8c13fa044076`", "the twelve are Ready", "State, What's owed, Who has it", "Rolling Pin (a kitchen line from Claire) · export_over", "reading 'the text kind' as ASCII against the vendor's binary-only rule, and joining 'saved out of unity on thursday' to the twelve notes that say 'saved out of the project, Thu 25 Sep' in two categories", f"`slack_read_channel` on #zombie-match3d for the week → `{S['a1_post']['id']}`", "X1, X1b, X6, X16, W4, K1"),
    ("ARTHOLD", "A11", "superseding · Beta(2.57, 1.29) mean 0.67 · `hev_d4e1db2db22b1a55`, `hev_a9c69a91cf1cefd0`, `hev_01debb8fc63f4c1e`", "the twelve are Ready", "State, What's owed, Who has it", "Desk Lamp (a Friday file from Claire outside Bathroom) · art_over", "mapping 'banyo objeleri' to the list's category, the iron and the washing machine included", f"reading Julia's DM with Claire after 24 Sep → `{S['a2_dm']['id']}`", "X2, X2b, X7, X11, X11b, K2"),
    ("REVISED", "A1", "stale_summary · Beta(1.0, 2.85) mean 0.26 · `hev_5ad302a3d2e2ed5b`, `hev_6aa0e2dc797c1a41`, `hev_8c277ed5dc029ed7`", "the three are Ready", "State, What's owed", "Cute Axe (same morning's files, not in the pull request) · revised_over", "comparing the note's time with the pull request's, and leaving Kettlebell, Dart Board and Candy out", f"`github_list_pull_requests` then the comment of `{B['pr462']}`; or #zombie-art", "X3, X3b, X8, K3"),
    ("AUDIO", "A13", "authority · Beta(1.0, 2.86) mean 0.26 · `hev_c4bbc05b4e9b08ea`, `hev_923eb1fef7d8dc20`, `hev_0eec4f03fda7d5a4`", "all five exported cues are Ready", "State, What's owed, Who has it", "Success sound (made here) · audio_over", "applying the rule to a source column and carrying it into the brief", f"a Drive search for the sound sheet, then its rows → `{S['c2_sheet']['id']}`", "X5, X5b, X10, X12, K5, B6"),
    ("PICKS", "A14", "superseding · same prior and records as ARTHOLD", "dynamite in the eight", "Board set", "Grenade (unchanged pick) · picks_over", "resolving 'it' through the thread parent and 'the last one on my list' through the order of his 25 Sep post", f"`slack_read_thread` on Julia's bow post `{B['art_bow_root']}` → `{S['c3_reply']['id']}`", "X13, X14, B1"),
    ("ZIP", "A25", "completion_elsewhere · no ledger record for this family: UNPARAMETERIZED (prior Beta(1,1))", "the eight are Ready", "State, What's owed, Who has it", "Music Keyboard (an instrument outside Friday's zip) · zip_over", "joining 'Friday's music instruments' to the eight notes that say zipped", f"a Drive search for the outgoing folder, then the document → `{S['c4_log']['id']}`", "X4, X4b, X9, X17, K4"),
]) + f"""

A5b checks per rule: **incorporated** — each state follows from the notes (K1) applied to records Julia can read; **survives complete retrieval** — each needs a join after the record is found (note or category → lines); **tool-surface proof** — every decider is a top-level message, a ticket comment, a sheet or a base pull request comment that the named call returns (no DM thread reply, no attachment body); **graded weight** — each flips at least two weight-5 slots. No liveness flag is resolved by removing an incorporation link.

### Liveness flags (S5b)

`trap_liveness.py --design` (advisory, UNCALIBRATED; verbatim):

""" + code(read(OUT / "trap_liveness.txt")) + "\n\nDispositions:\n\n" + table(["Traps", "Flag", "Disposition"], [
    ("T1", "breadcrumb", f"the vendor's binary-only rule is on the hub path (`{B['vendor_formats']}`) and the notes say a later word from someone who knows the file counts: both are the fairness path, kept. Neither names #zombie-match3d or Marcus, and the post `{S['a1_post']['id']}` shares no word with the ask."),
    ("T2, T7", "breadcrumb", f"the notes `{S['notes']['id']}` give the rule (later statements count; nobody changing it) and no place. Kept."),
    ("T4", "breadcrumb", f"the notes carry the sound rule, as they must for incorporation; they do not name Calvin's sheet `{S['c2_sheet']['id']}`, its title or its owner. Kept."),
    ("T5, T6, T15", "breadcrumb", f"the ask `{S['ask']['id']}` says 'unless he's changed them since' and the notes add Robert's later items: they authorise a later change and give no place, date or word of it. The reply is under a post about an arrow in another channel. Kept; the wording sweep on the SQL checks that the reply shares no rare word with the ask."),
    ("T3, T8", "breadcrumb", f"the changed-art rule is in the notes; the dates are base (`{B['pr462']}`, `{M.VENDOR_CH}`). T8 is a realism trap with no budget weight."),
    ("T9 to T19 (distractors and aliases)", "breadcrumb", f"on the read path by design (`{M.VENDOR_CH}`, `{M.DESIGN_CH}`, `{B['gdd']}`); none carries budget weight."),
]) + "\n\nA trap the tool flags and the table does not name is covered by the last row.\n\n`hardness_v2_check.py --design` (verbatim):\n\n" + code(read(OUT / "hardness_v2_check.txt")) + """

Dispositions: no FLAG and no UNRESOLVED. SAME_PLACE is re-run on the SQL. INPUT_CHECK reports no weight-5 total: the three counts are weight 3 (calculation) and five rules move two of them, so neither is plain arithmetic on clean inputs. RULE_IN_PROMPT runs when the prompt exists.
""")

# ------------------------------------------------------------------ 6 failure diversity
P.append("## 6 Failure-diversity plan\n\nEach unit is one deciding record behind its own retrieval habit, so a run's misses are a subset of six independent records. The comment, move, create and share writes are declared templates, so the rubric skeleton is the surface plus four volume rows (56 rows, weight 196): the budget is computed on the sampled shape a rubric can defend, not on one row per comment. Budget table (`difficulty_budget.py table`):\n\n"
         + read(OUT / "difficulty_budget_table.md") + "\n\n`difficulty_budget.py check` (verbatim):\n\n" + code(read(OUT / "difficulty_budget_check.txt")) +
         "\n\n`rubric_skeleton.py check` (verbatim):\n\n" + code(read(OUT / "rubric_skeleton_check.txt")) +
         "\n\nWhole policies and single misses on the skeleton, and the six-run simulation (`plan/policy_scores.py`, UNCALIBRATED; verbatim):\n\n" + code(read(OUT / "policy_scores.txt")) + f"""

**Reading.** At the budget's find-rate ranges E[average] is 36 to 55 % and P(all gates) 0.45 to 0.62: the average target (≤ 62 %) holds everywhere, and the all-gates target (≥ 0.5) holds at the middle and high find rates and misses at the low end (0.45). The printed spread chance is the binding figure and the tool warns below 0.70: with a third of the weight on two records that few runs find, runs differ mainly through the four coin-flip records. Two sensitivity runs sit outside the budget's ranges. If the two anchor records are found as often as a coin flip (the second reviewer's reading of D1), the average rises to about 56 %, still under the cap in 99 % of trials, and the spread chance improves. If every record is found two times in three, the average is about 67 % and the cap holds in only 70 % of trials: the design depends on runs missing about half of six records, and the pre-check is where that is measured. No single miss clears the cap by itself (see the table); a run that finds all four coin-flip records and misses both anchors scores about two thirds. A spread miss on a baseline that passes every other gate is reported to the owner (owner decision of 2026-11-10).

**Which runs miss what.** A1 is found by runs that read the game's dev channel for the week or ask what kind of file a save out of the project gives; A2 by runs that read Julia's DM with Claire after 24 Sep (it is in Turkish and holds no English task word). C1 is found by runs that check what changed after the notes (a pull request list or #zombie-art). C2 by runs that look for where the sounds came from. C3 by runs that open Julia's bow thread (the reply names no item). C4 by runs that look for the outgoing folder and open Brian's log of it. The six habits are different calls in four services, so two runs rarely share a signature. No single record decides more than {max(sum(r['weight'] for r in u['rows']) for u in json.loads((WF / '01_Difficulty_Budget.json').read_text())['units'] if u['role'] != 'realism')} of 196 weight.

**Lessons applied** (`00_Pre_Scenario_Analysis.md` §9b; Frederick's rev10 forensics, `task_inputs-uselater/Working_Files/01a_Hardening_Report.md` §8): in twelve runs a broad Slack search on the task's key noun returned every correction that held it. Here no deciding record contains 'playable', 'PlayableX', 'pack', 'brief', 'hand-off', 'asset', 'FBX' or 'vendor'; the SQL wording sweep at `/create-injection` enforces it. Inline review comments are not used. Every miss moves the counts in one direction (Owed up, Ready down), so misses cannot cancel in the reply.
""")

# ------------------------------------------------------------------ 7 deliverables
P.append("## 7 Deliverables and dependent writes\n\n" + table(["Write", "Tool", "Count", "Depends on", "Requirements"],
    [(w["service"], f"`{w['tool']}`", w["count"], ", ".join(w["depends_on"]), ", ".join(w["requirements"])) for w in man["writes"]]) + f"""

- **Hand-off list** (Google Sheet in Julia's Drive `{B['julia_root']}`): one row per line of Brian's list ({n_all}); the notes name the columns: Line, Category, Board set, State, What's owed, Who has it, Ticket. The truth of 'Who has it' is the person's first name (`plan/design_model.py` field `who`), compared as a whole word, so 'Brian' and 'Brian Foster' both pass. Totals {C['Delivered']} / {C['Ready']} / {C['Owed']}. Board set is Default for the eight ({', '.join(M.DEFAULT_FINAL)}), Extra for every other board item, empty otherwise.
- **Brief** (Google Doc in her Drive), covering what the notes list: Scenario 1 and what it is for (filtering for players who will like the game, true to the core game play); the eight on the board and the extras they can swap in; the four zombies ({', '.join(M.ZOMBIES)}) and the one animation ({M.PRIMARY_ANIMATION}); a level is won when every zombie is eliminated and lost when they take the player's health to zero; a 7-slot tray; sound: the cues that are ours, the rocket and explosion cues held back until we have our own, and when the music may start (after the first click, the vendor's rule of 14 Apr); start 3 November. Free-text parts are bounded: any wording that states these facts is accepted.
- **Tickets:** the {n_owed} Owed lines that have a ticket go to Todo (each starts In Progress) with a comment saying what is owed and who has it; no ticket is created. The {C['Delivered'] + C['Ready']} Delivered and Ready tickets are left as they are. The surface grades one named ticket's final state, comment and ticket text by content, and the counts on the list; the exclusion and the per-ticket targets are rubric rows the grader cannot decode (selector guide §2, §3), named here for the rubric stage.
- **Shares:** both files, view only, to the three other attendees of the kickoff hold and to PlayableX's intake address (eight share calls).
- **Messages:** the three counts to Frederick in `{M.DM_FRED}`; both links in `{M.VENDOR_CH}`.

Every write's content depends on findings (`depends_on`); none is a bolt-on. Each is asked for by the ask or the notes (a trigger Julia owns), and each target is hers to write: she owns both new files, is a member of both Slack conversations (`can-see` YES), and is a member of `team_DES` in Linear (`/team_memberships`).
""")

# ------------------------------------------------------------------ 8 service role map
order = ["slack", "linear", "gsheets", "gdocs", "gdrive", "gslides", "gcal", "contacts", "github", "confluence", "trello", "gmail"]
carrier = {"slack": "● message text, thread replies, DMs", "linear": "● title, state, parent; comments ● per §6b", "gsheets": "● grid", "gdocs": "● body_text",
           "gdrive": "● name, parents, sharing", "gslides": "● element text", "gcal": "● summary, start, attendees", "contacts": "● email, job",
           "github": "● PR title, dates, comment (base)", "confluence": "● page body, comments (base)", "trello": "● card, commentCard action", "gmail": "● invitation mails (companions)"}
P.append("## 8 Service role map\n\n" + table(["Service", "Role", "Load-bearing fact or write", "Carrier"],
    [(s, man["services"][s]["role"], man["services"][s]["weight_reason"], carrier[s]) for s in order] +
    [("snowflake", "not used", "none: nothing in the pack is measured in the warehouse, and Snowflake cannot be injected", "—")]))

# ------------------------------------------------------------------ 9 call budget
P.append("## 9 Call budget\n\n" + table(["Phase", "Service", "Calls", "Reason"], [(r["phase"], r["service"], r["calls"], r["reason"]) for r in man["call_budget"]]) + f"""

Total {budget_total} unconditional calls over 11 services; per-record {per_rec} in these rows (the gate output in §12 adds the pull-request surface's two calls). No row is conditional on an unverified tool behaviour; one unverified tool is on the pre-check list by name: `linear_show_data` (Ask_Carriers marks it a possible bulk read), with the `query` parameter of `linear_list_issues`. **Golden-run rule:** a correct run needs the volume: {n_list} comment reads fill the state column, {n_owed} moves and {n_owed} comments are the follow-through. **Every-run floor:** a run that finds no hidden record still reads the {n_list} tickets' notes, because nothing else says which lines are exported, and moves and comments the {n_vis} lines that are Owed on their own note: about 40 discovery and rule calls + {n_list} reads + {2 * n_vis} ticket writes + 13 for the two files, the shares and the messages ≈ {40 + n_list + 2 * n_vis + 13} counted calls, over the requester's 130. A run that samples tickets instead of reading them loses the totals and falls under the floor; if the pre-check comes in under 150 calls the design is revised before any baseline.
""")

# ------------------------------------------------------------------ 10 QC rails
two = [
    ("How many lines", f"{n_all}: the rows of Brian's list", "more, with the vendor's asks or the reference level's variants added", "the notes: one row per line of Brian's pack list; the ask has no clause about the vendor's requests", f"`{S['notes']['id']}`, `{S['tracker']['id']}`"),
    ("Twelve lines saved out of the project", "Owed, export again as binary (Brian)", "Ready: FBX, opens, looks right, in the outgoing folder; or Owed on suspicion, without the post", "Marcus: those files are the text kind; the vendor takes binary only; the notes: a format they take, and a later word from someone who knows the file counts. Without the post the note passes every Ready test on its face and 'take it as it stands' applies, so suspicion alone is not a fair Owed", f"`{S['a1_post']['id']}`, `{B['vendor_formats']}`"),
    ("Twelve exported bathroom lines", "Owed, the art (Claire)", "Ready: Friday's files open and look right", "Claire made them and says later that she is redoing the UVs and Friday's files are the old state", f"`{S['a2_dm']['id']}`"),
    ("Cactus Plant, Chainsaw, Cone", "Owed, the current file", "Ready: the file opens; colour versions are additions", "the notes name the case ('a fix, a retexture, new colour versions') and the pull request changed the three model files after the note's time", f"`{S['notes']['id']}`, `{B['pr462']}`, `{B['robert_new_colours']}`"),
    ("Kettlebell, Dart Board, Candy; the shared atlases", "not lines; nothing to do", "lines to add or delivered files to send again", "they are not on Brian's list and Robert did not add them; #460 adds objects and names no line's art", f"`{B['pr462']}`, `{B['pr460']}`"),
    ("Eight instruments in Friday's zip", "Owed, put the files back (Brian)", "Ready: each file opens and looks right, and Brian still has it", "the notes: Ready is 'sitting in the outgoing folder, it opens'; Brian's log: that zip will not unpack and the eight are not in the folder any other way", f"`{S['c4_log']['id']}`"),
    ("Rocket sound and Explosion sound", "Owed, our own version (Calvin)", "Ready: .wav is a type the vendor takes and it plays", "the notes hand over only what is ours; Calvin's sheet marks both 'no' and names him for our own version", f"`{S['c2_sheet']['id']}`"),
    ("The eight on the board", "with the bow, without the dynamite", "with the dynamite (25 Sep); or the reference level's three; or the bow in place of some other item", "Robert's own later reply: 'it' is the bow of the post he answers, 'the last one on my list' is the dynamite, the last item of his 25 Sep post; the ask keeps his latest word", f"`{S['c3_reply']['id']}`, `{S['picks']['id']}`"),
    ("The bow's own state", "Ready", "Owed: Claire agreed to add an arrow", "Robert's reply: the bow as it is now, the arrow as its own item later; and the bow's file is of Mon 29 Sep, after Friday's thread", f"`{S['c3_reply']['id']}`, `{B['art_bow_claire']}`, {tick('Bow')}"),
    ("The zombie characters", "Delivered", "Owed: the vendor said the package was not exported correctly; or the project's shaders changed", "base: Marcus's tested pack went on 26 Sep and the vendor reviewed it on 29 Sep and asked for a choice, not files; the pack's files did not change", f"`{B['brian_pack3']}`, `{B['vendor_zombie_ask']}`"),
    ("What the first zip held", "the reference level's items, the cannon, the background, the zombies", "everything on the vendor's list, since 'the only missing piece' was the duck", "the pack ticket says what the first zip was and the sound, 2D and font tickets say in words that they did not go; the vendor's sentence is about the reference", f"{PT}, `{B['vendor_duck']}`"),
    ("The cannon and the zombies after match3d#469", "Delivered", "to send again: #469 (30 Sep) touches the import settings of the cannon's and the monsters' source files", "its own comment: default importer fields added, no existing field changed; the delivered files are not art that changed", f"`{B['brian_pack3']}`, `harmonygames-Games/match3d#469`"),
    ("Music Keyboard, Grenade and the open rendering ticket", "Ready and Delivered as their notes say", "somebody is changing them: ZOM-449 (Backlog since July) names them among items with artifacts on low-end devices", "that ticket is about rendering on low-end Android, assigned to engineering, untouched since July; nobody is changing the models", f"`ZOM-449`, {tick('Music Keyboard')}"),
    ("Tray size", "seven slots", "six (Julia's July proposal)", "base: Robert's reply keeps the page at seven", f"`{B['gdd']}`, `confluence:{B['gdd_c2']}`"),
    ("Start date", "3 November", "6 October", "base: the vendor's latest message", f"`{B['vendor_nov3']}`"),
    ("Who the files are shared with", "both files, view only: the three other attendees of the hold and the intake address", "the brief only; or Leonard (his card is the 'kickoff')", "the notes: 'Sharing: both files, view only', the kickoff hold and Contacts", f"`{S['hold']['id']}`, `{S['contact']['id']}`"),
    ("Where the counts go", "Frederick's DM, as a message or a thread reply under his ask", "the PlayableX channel", "the ask: 'give me the count for each state here'; both forms in the DM are accepted", f"`{S['ask']['id']}`"),
    ("Ticket follow-through on an Owed line", "Todo plus a comment, also for the lines Owed on their own note", "a description edit, or a new ticket; or nothing for a line whose note already says not exported", "the notes: every Owed line's ticket goes to Todo with a comment saying what is owed and who has it; every line of the list has a ticket, so none is opened", f"`{S['notes']['id']}`"),
    ("Who has a REVISED line", "Claire: the file came from her", "Brian (he packs)", "the notes: a changed file goes again and sits with whoever the file came from; the three notes say 'FBX from Claire'. The surface grades 'who has it' only where the deciding record names the person", f"`{S['notes']['id']}`, {tick('Cactus Plant')}"),
]
P.append("## 10 QC rails\n\n### Two-reading table\n\n" + table(["Decision point", "Best reading", "Strongest alternative", "Resolved by", "Evidence"], two) +
    "\n\nNo figure forks: no BOTH_FAIR_FIGURE is declared. Dates: every graded date has the same Pacific and UTC day (3 November 17:00 UTC is 09:00 PT).\n\n### Reach table (load-bearing records)\n\nBase records (`persona_view.py can-see julia_lawson …`, run by `plan/reach_table.py`):\n\n" + read(OUT / "reach_table.md") + f"""

Planned records are checked at the injection gate (`persona_view.py check-sql`). Their planned access: the ask and Claire's message are in Julia's own DMs; Robert's posts and reply and Marcus's post are in channels she is a member of; the notes, the pack list and Calvin's sheet are shared with her and the deck is hers; the hold has her as an attendee; Linear, Trello and Contacts are unscoped. Records she cannot read are never load-bearing: Brian's DMs with Claire and with the engineer are cited in §1a and §13 as whole-base consistency checks only, and the Slack mirror of the pull request comment in #zombie-prs is not relied on.

### Feasibility, precedence, naturalness, grading devices

- **Feasibility.** Tools in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdocs_create_document`, `gdrive_share_file`, `linear_update_issue`, `linear_create_comment`, `linear_create_issue`, `slack_send_message`. One sheet with one tab. The outside recipient has an authorised path: the notes name the intake address in Contacts and the sharing level (view only).
- **Explicit rules.** Multi-version evidence: Brian's note stands unless something later says otherwise, and a later word from someone who knows the file or the art counts (notes); Robert's latest word on the picks (ask). What 'now' means: how things stand today (notes), the game as it is today (ask). Each write's end state is in the notes. Every cross-reference postdates its target (Robert's reply after Julia's post; Brian's comment after his zip; Marcus's post after Thursday's save; Claire's message after Friday's files; Brian's comment after the pause it mentions).
- **Precedence.** Load-bearing facts sit only in ● carriers (Ask_Carriers §5 as amended by §6b): Slack text, Linear comments, Sheets grids, Docs body, Slides element text, calendar summary and attendees, Contacts email, base PR comment text. Nothing load-bearing is in a calendar description, slide notes, a Drive `content_text` or a Slack file.
- **Prompt naturalness.** The human's trigger needs: Frederick's message as the starting point, that the job is all of it, that both files go in her Drive, the PlayableX channel. It must not carry: the three state words, any rule, any category or item name, any count, any ticket key, the places of §5, or where the notes and the list live. The surface's spans are the three anchor names only.
- **Grading devices.** Exact key set of the list ({n_all}); three totals; at most five samples per group (state, a second line of each hidden set, two controls, what is owed, who has it, board set, ticket comments) with a volume row; one tracked ticket. Brief rows are {brief_w} of {W} surface weight. No graded count, format or limit that the ask or the notes do not state.

### Coherence rail

Every §1a row is dispositioned. Designed disagreements are dated human claims with a named later record: Brian's notes (25 and 26 Sep) against Marcus's post (26 Sep), Claire's message (29 Sep) and his own comment (30 Sep); Robert's eight (25 Sep) against his reply (26 Sep). No two system fields disagree: undelivered tickets are In Progress until the run moves the Owed ones, which is the task, and a ticket's state never contradicts its own note. Companions planned with each record are in §11. No seeded text names a git branch, a build number or a release; the one base artifact the plan relies on is match3d#462 (title, created and merged times, the models its comment names), cited as base states it. Ids follow the base schemes (§2, §11).
""")

# ------------------------------------------------------------------ 11 record plan
rec = [(k, v["svc"], f"`{v['id']}`", v["at"], v["by"], v["what"]) for k, v in S.items()]
rec.insert(6, ("tickets", "linear", f"`{tick(M.LINES[0]['name'])}` … `{M.LAST_CHILD}`", "2025-09-25 07:06 to 07:20 (created); notes 2025-09-25 to 2025-09-29", "Brian Foster (creator, assignee, one note each)", f"one ticket per listed line, title = the line's name, parent {PT}, team DES; state Done for the eight delivered lines, In Progress for the rest; one comment by Brian on each saying what he did with the line"))
P.append("## 11 Record plan for /create-injection\n\n" + table(["Key", "Service", "Id", "At (UTC)", "By", "What"], rec) + f"""

Planned wording: `plan/planned_texts.py` (the ask, the notes, the pack ticket's description, Robert's three messages, Marcus's post, Claire's message with an English gloss, Brian's log of the outgoing folder, Calvin's grid, the deck's slides, the hold, the contact, Leonard's comment). Brian's note per class (`plan/design_model.py` NOTE, VIS_NOTE): Delivered — 'In the first zip, 24 Sep.'; Ready — 'FBX from Claire', the day, 'Opens, looks right. In the outgoing folder.'; EXPORT — 'FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.' (no tool is named on a ticket); Bathroom — the Ready wording, Fri 26 Sep; instruments — the Ready wording plus 'Zipped with the other instruments'; REVISED — 'FBX from Claire, Thu 25 Sep, first thing', stamped 08:05 UTC; sound — 'Exported .wav from the project, Fri 26 Sep. Plays.'; Owed on its own note — 'Not exported yet' or 'Not sent', with who has it. Haystack: routine traffic around each deciding record is base (#zombie-match3d 64 messages in the week, Julia's DM with Claire 55 in September, #zombie-art, {PT}'s neighbours); `path_exposure.py` at injection decides whether more is needed. Seeded Slack text names nobody by plain first name: base text carries a mention or a masking token where a person is meant, so a plain 'Brian' or 'Claire' would be a unique search key (re-check, row F3); mentions are used instead and names are added to the SQL wording sweep. Size about 330 rows over ten schemas (slack, linear, gsheets, gdocs, gdrive, gslides, gcal, gmail, trello, contacts); Snowflake, Confluence and GitHub are not injected.

### Integrations and companions

""" + table(["Service", "INT id", "Companion", "Decision"], [
    ("slack", "INT-13 (Drive app DMs), INT-04 (Linear app posts)", "share and ticket notifications", f"none seeded: the Linear app's team-channel posts are for ZOM and ENG tickets (INT-04), and Design-team tickets created outside Slack carry no bot post, and the shares are covered by mail (INT-11 below); the thread counters of Julia's bow post `{B['art_bow_root']}` are updated with the reply"),
    ("linear", "INT-04, INT-05", "Slack posts, e-mail digests", "none: digests are not per ticket; `updated_at` follows the newest note (generator convention)"),
    ("gcal", "INT-11", "invitation mails", "seeded: one event row per attendee calendar (same `ical_uid`) and one invitation mail per attendee mailbox"),
    ("gmail", "INT-11, INT-22", "the invitation mails themselves", "seeded as companions only; no deciding fact in mail (Gmail is THIN for the persona)"),
    ("gdrive, gdocs, gsheets, gslides", "INT-13", "Drive rows mirror Docs, Sheets and Slides ids and sharing", "seeded: one `drive_files` row per file with identical sharing; Julia owns the deck"),
    ("trello", "INT-21", "none exists", "trello: none — the card's and the board's dateLastActivity move with the comment and the card's badge counts one comment"),
    ("contacts", "—", "none", "contacts: none — a single row in the base shape (15 fields)"),
    ("github", "INT-01, INT-03", "Slack mirror, linear[bot]", "github: none — nothing is seeded in GitHub; match3d#462's comment already has its base mirror in #zombie-prs"),
]))

# ------------------------------------------------------------------ 12 self-test
review = [
    ("temporal", "The ask is dated after the pause and asks for prep the pause was meant to stop.", f"the base lines of 29 Sep are about vendor development on a game that may change (`{B['leonard_pause_q']}`, `{B['fred_pause']}`); the ask scopes to the game as it is today and to what PlayableX hold and are owed (`{S['ask']['id']}`)", "holds"),
    ("semantic", "'Owed' could mean owed by the vendor, or money; 'who has it' could mean who holds the file.", f"the notes define the three states and 'who has it, meaning whoever has to do the next thing' (`{S['notes']['id']}`); learnings §80: each label defined in a record", "holds"),
    ("cross-service referential", "The pack list and the tickets can disagree on a line's name or ticket.", f"both are generated from one model (`plan/design_model.py`: the pack list `{S['tracker']['id']}`, tickets {TICKS}); the injection gate's `fact_check` holds them to it", "holds, enforced at injection"),
    ("quantitative", f"{C['Delivered']} / {C['Ready']} / {C['Owed']} could fork on a line whose note is unclear.", f"every listed line's note says where the file came from and that it opens, or that it is not exported (`plan/design_model.py` NOTE, VIS_NOTE); the two-reading table covers the bow, the zombies and the first zip (`{B['vendor_duck']}`)", "holds"),
    ("state/lifecycle", "In Progress tickets whose files are 'in the outgoing folder' could be read as a State/Lifecycle inconsistency.", f"the pack ticket {PT} says a line's ticket closes when PlayableX have the file, so In Progress is right for every undelivered line, exported or not; card SC-16's tickets are not touched", "holds"),
    ("identifier/format", f"{PT} to {M.LAST_CHILD} could collide or break the series.", "base highest in the Design team is `DES-312` (7 May 2025) and the range is free (`plan/check_ids.py`: 0 hits, scan complete), so the keys follow in number and in date", "holds"),
    ("other", f"A reviewer reads the cohort as padding: {n_all} lines for one ad.", f"the vendor asked for an 8-item set plus extra items it makes editable (`{B['vendor_formats']}`), its list names sound, 2D and fonts (`{B['vendor_asset_list']}`), and Brian promised more items later (`{B['brian_later']}`); every line is a cell of the list the ask requests", "holds"),
] + [("decision: " + r[0], f"the alternative: {r[2]}", f"{r[3]} ({r[4]})", "best reading stands") for r in two]
P.append("## 12 Self-test results\n\n`hardness_gate.py … --design` (verbatim):\n\n" + code(read(OUT / "hardness_gate_design.txt")) +
    "\n\n`gradable_surface.py validate` and `gradeable-report` (verbatim):\n\n" + code(read(OUT / "gradable_surface.txt")) +
    "\n\nId collision check (`plan/check_ids.py`, `hg.py search lookup`; verbatim):\n\n" + code(read(OUT / "check_ids.txt")) + f"""

**Lazy-solver pass.** An agent that makes one broad search per service, reads first hits, opens no thread, stops at the first conclusion and uses every bulk call: it finds the ask, the notes, the pack list and the PlayableX channel's last page; lists the {n_list} children with their states in two calls; reads no comments. It scores the delivery rows and the brief rows that come from the hub (scenario, start date), about 8 % of the surface weight; it cannot fill the state column, because no bulk call returns a ticket's notes. Leaks looked for and closed: the pack list has no state or note column; ticket state marks only the eight delivered lines, which the list's 'Went out' column already shows; ticket titles and descriptions carry the line's name only; no label marks a class; no category is of one class; the notes name no deciding record. Still open by design and named for the pre-check: `linear_show_data`.

**Literal-value sweep and wording sweep** (base, `plan/literal_sweep.py` through `tools/hg.py search-many` over eleven services; the SQL repeats both):

{code(read(OUT / 'literal_sweep.txt'))}

Reading of the sweep: a planned phrase with no base hit cannot contradict base; a hit is listed above with its record and is unrelated to this pack unless stated in §1a. None of the six deciding records is planned with a word of the rule it triggers ('format', 'binary', 'current version', 'changing', 'ours', 'picks') or with one of the swept nouns of §6.

**'The rest stands' check.** Robert's reply changes one item; no later planned record re-lists the eight. The deck (23 Sep) is the reference level and is not edited after his posts.

**S9b prior forecast** (advisory, UNCALIBRATED, pre-registered before any platform run: `hardness_forecast.py forecast --design … --preregister`; ledger id `hev_1072a8a9540b0640`; output verbatim except that the ledger line's empty 'rejected' list is left out):

{code(read(OUT / 'forecast.txt').replace(", 'rejected': []", ''))}

The priors are per-family miss rates for `claude-opus-5-5` (superseding 0.67, done_gap, stale_summary and authority 0.26, tool_surface without a record 0.50). On them the expected average is 61 to 62 % and the chance of passing all four gates 0.445 to 0.483, below the budget simulation of §6 (0.50 to 0.65), which uses carrier find rates. Both are uncalibrated; the pre-check is the first measurement.

### Self-review

Gate output re-read after the last change: `HARDNESS GATE (extreme (design)): PASS` (pasted above with its ok lines and the volume-exception note). Re-read as the eval: `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and `Evals/0_Injection_Quality_Eval.md` Check C, walked against §1a, §7 and §10. Load-bearing base values were re-read through `tools/hg.py` in this session: the PlayableX channel from 15 Sep, Julia's DM with Brian of 23 Sep, Brian's two DMs of 24 Sep, the pull requests #459 to #471 (titles, times), the open ZOM tickets that name objects, the ZOM number range and team memberships; the rest is the reviewers' fact pack with record ids.

""" + table(["Item", "Counter-reading (the best case that it fails)", "Resolution (evidence)", "Verdict"], review) + f"""

Required items addressed: the two v2 decisions and their sources (§5); corrections off the first-read path (§5, v2 check); reach (§10); feasibility (§10, §7); volume and the every-run floor (§9); budget and spread (§6); known-data-issue cards (§1a); padding (§2); both cold reviews (§13).

Unresolved: none that blocks the design. Carried to `/create-injection` as checks, not open questions: the SQL wording sweep; the haystack decision; the cold-solver rehearsal; `persona_view.py check-sql` on every planned record; the final Turkish wording of Claire's message against her base register. UNVERIFIED-OK items that no row depends on: the binary contents of the three base zips, the five masked zombie names, and whether `github_get_pull_request_files` returns files at run time (the comment route is the one relied on).
""")

# ------------------------------------------------------------------ 13 red team
P.append(read(OUT / "redteam_section.md"))
out = WF / "01_Scenario_Design.md"
out.write_text("\n\n".join(P) + "\n")
print("wrote", out, len("\n\n".join(P)), "chars")
