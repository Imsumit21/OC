#!/usr/bin/env python3
"""Assemble Working_Files/01_Scenario_Design.md from design_model.py, the draft manifest and the pasted tool outputs.
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
ctx = json.loads((WF / "00_Task_Context.json").read_text())
S, B = M.SEED, M.BASE
read = lambda p: Path(p).read_text().rstrip("\n")
code = lambda t: "```\n" + t + "\n```"
def tick(n): return M.BY_NAME[n]["ticket"]
def names(cls): return ", ".join(l["name"] for l in M.members(cls))
def table(head, rows):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows])
C = M.COUNTS
n_list = sum(l["on_list"] for l in M.LINES); n_all = len(M.LINES)
owed_tix = [l for l in M.LINES if l["state"] == "Owed" and l["ticket"]]
budget_total = sum(r["calls"] for r in man["call_budget"]); per_rec = sum(r["calls"] for r in man["call_budget"] if r["phase"] == "per-record")

P = []
P.append(f"""# Scenario Design — {M.SLUG} (design D1) · design only · contains no prompt, OE or criterion text

Written 2026-11-11 by `/create-scenario` (Claude, authoring session) from `00_Pre_Scenario_Analysis.md`, three read-only censuses of the synth-cut base (`Working_Files/research/census_A_design_channels.md`, `census_B_build_art_channels.md`, `census_C_other_services.md`) and the generators in `Working_Files/plan/`. Planned (seeded) records are described, never written as SQL here. Ids of the form `C…/ts`, `ART-n`, `f_…`, `evt_…`, `cmt_…` without the word base are minted for `/create-injection`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `synthcut`, label Oct 1, 2025 (synth-cut), `{ctx['universe']['clock_line']}`; seed bound `freeze_utc` {ctx['freeze_utc']} (Tue Sep 30 17:00 PT); `shutdown_rules_apply` false (the company operates normally) |
| Assignment (V3, 8 fields) | business_function Product · persona Julia Lawson · role Product Manager · competency Marketing and GTM · task_skill Authoring · task_type long-horizon · difficulty_mode hard · universe date October 1, 2025 07:00 (context_hash `{ctx['context_hash'][:12]}`, assignment_hash `{ctx['assignment_hash'][:12]}`) |
| Evals category | Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay/design requirements, art and prototype evaluation), inside Marketing and GTM: the artifact is a playable ad, a user-acquisition creative |
| Loss budget | Hard cap < 70 % (`difficulty_cap` 0.7); design target E[avg] ≤ 62 %; requester targets in the draft manifest `author_targets`: more than 130 counted calls in every run, average under 70 %, every other difficulty gate |
| Horizon | Long Horizon → `effective_profile: extreme`; `volume_exception {{call_budget_floor 220, per_record_floor 110}}` (budget {budget_total}, per-record {per_rec}; requester's words quoted in the manifest) |
| Theme screen | the storyline is ad production (objects, exports, formats, sound, a vendor hand-off). The game's name cannot be avoided; no seeded text uses infection or outbreak vocabulary, and seeded text says 'ZM3D' or 'the game'. The pre-check is read for model-fallback events (`Hardness_Mastery.md` §12: suspected, not proven) |
| Fit census | `Working_Files/00_Assignment_Fit.json`: `NO NATURAL COHORT` (WARN mode); Gmail THIN for this persona, so no anchor and no coin-flip record sits in her mailbox; route S2x: the scenario is built by injection on base containers she can read |
| Persona card | `references/persona_cards/synthcut/julia_lawson.json`: earlier tasks used ZOM tickets and the match3d repository as cohorts (claims register, difficulty baseline, beta calendar, audience call). This design's cohort is the lines of one asset pack on new ART tickets; no earlier cohort, rule vocabulary or record set is reused |
| Role remit | Julia wrote the brief for the first playable: `{B['julia_dd_brief']}` (2025-03-14, her storyboard to PlayableX) and the vendor's reply 'thank you so much for this detailed brief' (`{M.VENDOR_CH}/1742063341.276529`). For the second playable Brian asked her for the reference level on 2025-09-22 (`{B['brian_asks_level']}`). The design page names her: `confluence:{B['gdd']}` v2, 'Owner: Robert (Product). Design: Julia Lawson.' Role review: `Working_Files/00_V3_Authoring_Evidence.json` (`role_reviews.scenario`) |

Persona reach census (`persona_view.py reach julia_lawson --top 10`, verbatim):

{code(read(RES / 'reach_julia_top10.txt'))}

Identities (`entity.py resolve "Julia Lawson"`, §1c): Slack `EMPLOYEE_0005_SLACK_ID`, Linear `usr_8140f09bf9f1b94c`, GitHub `PERSON_0005_GITHUB_USERNAME`, Trello `793af7ca6940bf18eb516c75`, Contacts `8140f09bf9f1b94cb8ee2dd7`, Drive root `{B['julia_root']}` (owned). Her calendar's time zone is Europe/Istanbul (gcal `/calendars/13`); persona-written dates are still Pacific with UTC beside them when the day differs.
""")

# ------------------------------------------------------------------ 1 storyline
P.append(f"""## 1 Storyline

**The base, as read.** On 2025-08-26 Leonard opens a second playable with PlayableX, for Zombie Match 3D (`{M.VENDOR_CH}/1756223629.429589`). On 2025-09-15 Frederick picks Scenario 1 and names the open questions: which objects are on the board and which zombies are hit (`{B['fred_scenario1']}`). The vendor offers editable items 'aside from the 8-item set that you will provide' and says which file types it takes (`{B['vendor_formats']}`), then lists the assets it expects by group (`{B['vendor_asset_list']}`). Brian packages: a zip on 24 Sep (`{B['brian_zip1']}`), the plushie the vendor called 'the duck asset' the same day (`{B['vendor_duck']}`, `{B['brian_zip2']}`), a corrected zombie pack on 26 Sep after the vendor asked for a package tested 'in a blank Unity project' (`{B['vendor_blank_scene']}`, `{B['brian_pack3']}`). On 29 Sep the vendor asks for one primary animation and four zombies (`{B['vendor_zombie_ask']}`); the same evening Frederick pauses development 'for a month or so' (`{B['fred_pause']}`); on 30 Sep 09:59 UTC the vendor sets the new start for 3 November (`{B['vendor_nov3']}`). The start had already moved from 29 Sep to 6 Oct for late assets (`{B['vendor_oct6']}`). No Slack message says 'playable' after the pause post, and no record of any service is dated between the vendor's reply and the data horizon that touches it (census A §G, census B §I).

**The job (planned).** On Tue 30 Sep 18:10 UTC (11:10 PT) Frederick asks Julia in their DM (`{S['ask']['id']}`) to do for this playable what she did for the first: write what PlayableX builds from, and say where the pack stands, for the game as it is today. He names three things it starts from: Brian's pack list, Robert's picks, his own hand-off notes. The deliverables are a brief (a Google Doc) and a hand-off list (a Google Sheet) in her Drive, the ticket follow-through the notes ask for, the three counts back to him in the DM and both links in the PlayableX channel.

**Why now, against the pause.** The four latest base lines about the playable are of 29 Sep: Leonard expects a change to the core game and does not want the vendor's work wasted (`CADCE44A365D/1759171993.180879`, `CADCE44A365D/1759172018.976319`); Brian says a playable of the game in its current form would not be needed after a change (`D076PSEBC4D/1759171889.924089`) and that the vendor's optimizations of animations, panels and objects would carry over (`CADCE44A365D/1759172311.343939`). Julia is in neither conversation (`can-see` NO). The planned ask agrees with all four: it does not say the playable will ship as specified ('if the core changes we redo that part with them in November'), and what it asks for is the part that slipped the start twice and that carries over: which files PlayableX holds, which are fit to send and which are owed. Robert's base line that the playable tests 'the current form' (`{B['robert_current_form']}`) is the same scoping.

**Anchors per service.** Slack: the ask `{S['ask']['id']}` (planned); the vendor channel `{M.VENDOR_CH}` (base, 198 messages); Robert's picks `{S['picks']['id']}` and `{S['zpicks']['id']}` (planned, #zombie-design). Docs: Frederick's notes `{S['notes']['id']}` (planned); base `{B['playable_feedback_doc']}`. Sheets: Brian's pack list `{S['tracker']['id']}`, Calvin's source sheet `{S['c2_sheet']['id']}` (planned). Linear: ART-793 and children ART-794 to ART-890 (planned; base precedent ART-792, Frederick's marketing-screenshots epic). Slides: Julia's reference-level deck `{S['deck']['id']}` (planned). Calendar: the kickoff hold `{S['hold']['id']}` (planned; base precedent `evt_257421bc09196edbf28758`, the 2025-03-12 vendor meeting Frederick organised with Julia invited). Contacts: `{S['contact']['id']}` (planned). GitHub: base `{B['pr462']}`. Confluence: base `{B['gdd']}`. Trello: base card `{B['trello_kickoff']}` with a planned comment `{S['trello_note']['id']}`.

**Universe KB.** Timeline (`references/universe_kb/by_universe/synthcut/timeline.md`): the window sits after the spine beats '2025-09-15 Season Pass built for Zombie Match (match3d) - PR #438' and '2025-09-30 PR #476 Vision bot opened and merged'; neither is touched. `cohorts.json`: no fit — every KB cohort is a base Linear state or label set (`LIN-S01` … `LIN-L30`); this cohort is the lines of one pack on seeded ART tickets, defined by a seeded sheet. `trap_catalog.json` entries the traps stand on: `C01` (thread replies that correct or retract: T5), `C02` (a parent states a resolution and another record says it still fails: T1, T7), `D05` (title families with version markers: the 'old' item docs, avoided), `K02` (app-name lineage, 'Puzzles vs Zombies': not used as an alias), `N01` (ticket series collisions: ART numbers overlap ZOM and ENG numbers; every ticket is cited with its team key), `P01` (shared first names: §1c).

### Coupling seams

- The pack list `{S['tracker']['id']}` has no state column, and every line ticket (ART-794 to ART-890) is Done: a line's state needs the note on its own ticket (how and when it was exported) joined to a rule in the notes `{S['notes']['id']}`.
- 'Exported' on a ticket and 'the file is usable' are two facts. The second lives where the tool, the art or the sound is discussed (`{S['a1_post']['id']}`, `{S['a2_dm']['id']}`, `{S['c2_sheet']['id']}`), not on the ticket.
- The delivery date of a file and the date the art last changed are in different services: Slack `{B['brian_zip1']}` and GitHub `{B['pr462']}`.
- The default eight are fixed by one person's two messages in two channels: `{S['picks']['id']}` and `{S['c3_reply']['id']}`.
- The sound rule in `{S['notes']['id']}` is about ownership; the sound tickets ({tick('Match scale')} to {tick('Music')}) only state the file type.
""")

# ------------------------------------------------------------------ 1a coherence audit
audit = [
    ("vendor channel thread order", "temporal", "three start dates in one channel", f"`{B['vendor_formats']}`, `{B['vendor_oct6']}`, `{B['vendor_nov3']}`", "hazard T02 (not chronological files): none of these; card SC-13", "fold: a dated claim sequence, the last stands (T8); the beta date is never graded"),
    ("Leonard's Playable Kickoff card", "temporal", "dateLastActivity vs actions", f"`{B['trello_kickoff']}` (actions 2025-08-01, 2025-09-13)", "hazard T06", "fold: the planned comment moves the card's and the board's dateLastActivity to the comment's time"),
    ("vendor's name", "semantic", "'PlayableX' in Slack text, '[USERNAME_36301]' in mail and calendar titles", f"`{M.VENDOR_CH}/1741284538.488439`; gcal `evt_257421bc09196edbf28758`", "hazard S03: none in scope; trap catalog X04 (uneven masking)", "fold: seeded text uses the Slack spelling Julia sees; no row depends on a mail or calendar title"),
    ("roles in Slack vs roster", "semantic", "Julia called 'our lead designer' and Brian 'Product Manager' in one vendor-channel message", f"`{M.VENDOR_CH}/1741796408.361009`", "none listed", "avoid: no seeded text states either title; the assignment's role governs"),
    ("design page vs its comments", "cross-service referential", "tray 7 on the page, a 6-slot proposal in a comment", f"`{B['gdd']}` with `confluence:{B['gdd_c1']}`, `confluence:{B['gdd_c2']}`", "cards SC-8, SC-38, SC-58 (other sentences of the same page)", "fold: Robert's reply on the page keeps 7 (T9); the page's sentences on the glass crash, the Season Pass date and the monster roster are neither cited nor graded"),
    ("Slack links to Google files", "cross-service referential", "native ids never equal export ids", f"planned Slack records, e.g. the ask `{S['ask']['id']}`", "hazard R04", "excluded: no seeded Slack text carries a document link; the ask names the notes in words"),
    ("calendar invitations", "cross-service referential", "invitation mails without a calendar row", "hazard R08", "hazard R08", "fold: the hold is seeded with one row per attendee calendar and its invitation mails (INT-11)"),
    ("thread counters", "quantitative", "reply_count, reply_users_count, latest_reply of Julia's bow post", f"`{B['art_bow_root']}` (1 reply in base)", "hazards Q01, Q02, Q03", "fold: the planned reply updates the three counters as companions"),
    ("counts in the deliverables", "quantitative", "19 Delivered, 30 Ready, 54 Owed of 103 lines", f"`plan/design_model.py`; the pack list `{S['tracker']['id']}` and ART-794 to ART-890", "hazard Q01 kind (a stated count against the rows): none in base for these records", "fold: every count comes from the model; no base figure is restated"),
    ("merged pull request without review", "state/lifecycle", "match3d#462 merged with no human review", f"`{B['pr462']}`", "hazard L09", "fold: the task uses its merge time and the objects it changed, never its review state"),
    ("Linear state vs shipped work", "state/lifecycle", "tickets open after work shipped", "ZOM-564, ZOM-513, ZOM-514, ZOM-563, ART-790, ART-792", "card SC-16; hazard L06 (parent Done while child open): none in scope", "avoid: none of those tickets is cited; the pack ticket is a new Team Epic with its own children"),
    ("ids of seeded records", "identifier/format", "Slack message id, Linear keys, Drive ids, Trello action id", f"`plan/check_ids.py` output: ART-793 to ART-890, `{S['notes']['id']}`, `{S['trello_note']['id']}`", "hazards I01, I02, I10 (`usr_Robert`), I15", "fold: ids follow the base schemes; Robert's Linear id is `usr_Robert` as in base; no collision (§12)"),
    ("object names", "other", "the July export lists 151 objects; a 23 Sep commit shortened long names", f"gsheets `{B['july_export']}`; census B §A.4", "none listed", "fold: every line takes a name attested in base; no row grades a prefab or file name"),
]
P.append("## 1a Coherence audit\n\nScope = every record a correct run opens: the ask, the notes, the pack list, the pack ticket and its 97 children with their comments, the vendor channel in full, the #zombie-design playable thread and Robert's two posts, #zombie-art from 23 Sep, Julia's DM with Claire, #zombie-bugs from 25 Sep, Calvin's sheet, Julia's deck, the design page with its comments, the kickoff hold, the contact, the Playable Kickoff card, match3d#462. Hazard ids are from `references/universe_kb/by_universe/synthcut/coherence_hazards.json`. Known-data-issue cards read: `references/known_data_issues/synthcut.md` (SC-1 to SC-73); cards the scope touches are SC-13, SC-58, SC-8, SC-38 and SC-16, each with its disposition below.\n\n"
         + table(["Record", "Category", "Fields", "Pointer", "Hazard / card", "Disposition"], audit)
         + f"""

**Sibling-defect sweep.** Designed defect kinds and their base siblings: (a) a 'done' ticket whose file is unusable: base has the 25 Sep zombie package ('Only the prefabs were included', `{B['vendor_blank_scene']}`), repaired in base on 26 Sep and kept as a control (T10); (b) art changed after a hand-off: base has exactly the five lines of match3d#462 and the rocking chair rework of 29–30 Sep (`{M.ART_CH}/1759190391.487809`), which is not on the pack list; (c) a pick changed in a reply: base has Julia's own grenades-and-shuriken idea, answered 'remain as is' (T13). No other sibling was found in the windows read in full (census A: #zombie-design from 1 Sep, the vendor channel, #zm-animations, #zombie-sfx; census B: #zombie-art and #zombie-match3d September, #zombie-bugs by filter and from 27 Sep).

**Base facts the plan must not contradict** (each checked): no board object was stripped from a build and the game has no addressables for objects (`{M.BUGS_CH}/1758905363.341129`), so no line's state depends on a build; the September clone items 'don't work yet' (`C05433XK267/1758854356.576719`) and none is on the pack list; no base record states an art sign-off rule, a licence or a rule on sharing source art (census A §C, §F; census B §D, §G), so the planned notes, Claire's DM and Calvin's sheet add facts and overturn none; the vendor's price and bundle choice are open in a DM Julia cannot read (`D08JRD3TQE8/1756322075.746289`, `D08JRD3TQE8/1759115937.979409`) and no seeded text states a price or a signed order.
""")

# ------------------------------------------------------------------ 1b speakers
speak = [("Frederick Stone", "frederick.stone@harmonygames.co", f"the ask `{S['ask']['id']}`, the notes `{S['notes']['id']}`, the pack ticket ART-793, the hold `{S['hold']['id']}`, the contact"),
         ("Brian Foster", "brian.foster@harmonygames.co", f"the pack list `{S['tracker']['id']}`, the 97 child tickets and their export notes, the pack-ticket comment `{S['c4_comment']['id']}`"),
         ("Robert", "robert@harmonygames.co", f"the picks `{S['picks']['id']}`, the zombie answer `{S['zpicks']['id']}`, the reply `{S['c3_reply']['id']}`"),
         ("Claire Morgan", "claire.morgan@harmonygames.co", f"art notes on tickets; the DM `{S['a2_dm']['id']}`"),
         ("Arthur Blake", "arthur.blake@harmonygames.co", f"the #zombie-bugs post `{S['a1_post']['id']}`"),
         ("Calvin Price", "calvin.price@harmonygames.co", f"the sound source sheet `{S['c2_sheet']['id']}`; notes on the sound tickets"),
         ("Leonard Hayes", "leonard.hayes@harmonygames.co", f"the Trello comment `{S['trello_note']['id']}`"),
         ("Julia Lawson", "julia.lawson@harmonygames.co", f"her reference-level deck `{S['deck']['id']}` (23 Sep)"),
         ("Martin Walsh", "martin.walsh@harmonygames.co", "named as holder of the fonts; no seeded voice")]
P.append("## 1b Active speakers\n\nStatus from `references/universe_kb/by_universe/synthcut/activity.json` (`status_at_clock`). The PlayableX staff (`PERSON_6078_SLACK_ID`, `PERSON_3937_SLACK_ID`) are Slack-only ids with no status row and get no seeded voice: every vendor statement the design uses is a base message.\n\n"
         + table(["Person", "Email", "status_at_clock", "Seeding role"], [(n, e, "active_sep_2025_quiet_in_oct", r) for n, e, r in speak]))

# ------------------------------------------------------------------ 1c identity
resolve = read(RES / "entity_resolve.txt").split("### ")
keep = [blk for blk in resolve if blk.split("\n")[0] in ("Julia Lawson", "Frederick Stone", "Brian Foster", "Claire Morgan", "Robert", "Arthur Blake", "Leonard Hayes", "EMPLOYEE_0006_SLACK_ID")]
res_txt = "\n".join("### " + "\n".join(b.rstrip().split("\n")[:8]) for b in keep)
P.append("## 1c Identity traps\n\n`entity.py collisions` (verbatim):\n\n" + code(read(RES / "entity_collisions.txt")) +
         "\n\n`entity.py resolve` for the people the design names (first lines of each):\n\n" + code(res_txt) + f"""

Pinned entities and their lookalikes: Claire Morgan (`EMPLOYEE_0009_SLACK_ID`, Linear `usr_7fe31e7ec8199618`) against the GitHub-only 'Claire' login; Robert (Linear `usr_Robert`, hazard I10) has no surname in any service; Calvin Price has two GitHub logins and one Slack id (`EMPLOYEE_0006_SLACK_ID`); 'Blake' in base text is Arthur Blake. Victor Barnes (`EMPLOYEE_0030_SLACK_ID`), introduced to the vendor in March as the art director, left in April 2025 and has no seeded voice. No second account is created for anyone and no trap depends on a malformed id. The PlayableX intake contact is a role address, not a person, so it duplicates nobody.
""")

# ------------------------------------------------------------------ 2 cohort
cls_rows = [("Delivered", "W", "in PlayableX's hands and usable (the 24 Sep zip, the plushie zip, the 26 Sep zombie pack)"),
            ("Ready", "READY", "exported on its own in a file type they take, current, nobody changing it"),
            ("Owed, stated on the line's own ticket", "VIS", "prefab only, not exported, flat PNG, PSD only, no track chosen, no font files"),
            ("Owed, EXPORT", "A1", "exported in one go on 25 Sep: empty shells (Arthur's post)"),
            ("Owed, ARTHOLD", "A2", "set Bathroom: Claire is redoing the UVs (her DM)"),
            ("Owed, REVISED", "C1", "the art changed on 25 Sep after the file went out or was exported (base)"),
            ("Owed, PARENT", "C4", "set Music: the 26 Sep export comes in without textures (Brian's pack-ticket comment)"),
            ("Owed, AUDIO", "C2", "cut from a bought pack (Calvin's source sheet); the notes let only owned sound leave"),
            ("Owed, PICKS", "ADD", "added by Robert in a later reply; not on the list, no ticket, not exported")]
P.append(f"""## 2 Cohort spine

**Rule (closed).** A line is one row of Brian's pack list `{S['tracker']['id']}` ({n_list} rows: 78 board objects, 4 zombies, the cannon and its shot, 5 interface pieces, the board background, 6 sound cues, the fonts), plus any board object Robert has added since Brian made the list (the notes' sentence 'If Robert has added objects since Brian made the list, they go on it too'). Robert added six in one reply, so the list has {n_all} lines. The vendor's own requests add no line: its groups (`{B['vendor_asset_list']}`) are all on the pack list, the 'duck asset' is the plushie line and the 'rocket launcher' is the cannon line (T16). Size {n_all}; key = the line's name.

**Truth by class** (`plan/design_model.py`; Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}):

""" + table(["State", "Lines", "Why", "Members"], [(st, len(M.members(c)), why, names(c)) for st, c, why in cls_rows]) + f"""

**Surfaces and shortcut audit** (manifest `cohort.evidence_surfaces`):

""" + table(["Surface", "Records", "Calls each", "Bulk call that does not cover it", "Why it cannot be skipped", "Serves"],
            [(f"{s['service']} `{s['tool']}`", s["records"], s["per_record_calls"], s["why_no_bulk"], s["short_circuit"], f"{s['requirement']}: {s['decides']}") for s in man["cohort"]["evidence_surfaces"]]) + f"""

**Predicate.** Delivered: PlayableX has the file and can use it. Ready: exported in a format they take, it opens, it is the current version and nobody is changing it. Owed: anything else, with what is owed and who has it. The three words and their tests are in the notes; the facts are on the tickets and in the records of §5. **House rule that overrides the natural reading:** a Done ticket that says 'exported' is not Ready when the file is an empty shell, the art is being redone, the art changed afterwards, or the sound is not ours. **Dual regime by date:** a file that went out on 24 Sep or was exported on the morning of 25 Sep predates the art change merged at 23:15 UTC that day (`{B['pr462']}`). **Boundary records:** six lines outside the list (Robert's reply); the plushie delivered in a second zip the same day (`{B['brian_zip2']}`); the zombie pack sent twice (T10); the nine lines that are Owed on their own ticket's note (Buttons went out in the zip as a flat PNG and is still Owed).

**Necessity of the per-line read.** {len(M.members('VIS')) + 12 + 12 + 8 + 2 + 5} of the {n_list} listed lines are Owed and nothing upstream says which: the pack list has no state column. Every line ticket is Done (Brian closed each as he dealt with it, 23 to 26 Sep), so workflow state marks nothing either; the notes tell the reader that 'Brian's note on each says what he did with it'. Every ticket carries that note; art notes by Claire sit on 31 tickets across five sets, so a note by itself marks nothing. Notes state raw facts (how, when, what file type), never the state. Padding check: every line is an asset the vendor asked for by group or Robert put on the board or among the extras; none exists to raise a count, and each line's state is a cell of the hand-off list.

**Ids.** Tickets ART-794 to ART-890 follow the list order (`plan/design_model.py`); ART-793 is the pack ticket. Base highest ART number is ART-792 (census C §1). Collision check: §12.
""")

# ------------------------------------------------------------------ 3 authorities
P.append("## 3 Hidden authorities\n\n" + table(["Id", "Name (what it governs)", "Home", "Record", "Governs", "Decoy and its scope", "Findability"],
    [(a["id"], a["name"], a["home_service"], ", ".join(f"`{x}`" for x in a["seeded_ids"]), ", ".join(a["governs"]),
      f"{a['decoy_service']}: " + ", ".join(f"`{x}`" for x in a["decoy_base_pointers"] + a["decoy_seeded_ids"]) + f" — {a['decoy_scope']['dimension']}: {a['decoy_scope']['decoy']}",
      f"a search for '{a['findable_query']}' returns it; the ask names it in words") for a in man["authorities"]]) + f"""

`governs` lists do not overlap (H1: R2, R3, R6; H2: R1; H3: R7). H1 has a same-service decoy with an adjacent scope: Leonard's 'Playable Feedback' (`{B['playable_feedback_doc']}`, the first playable, P0/P1/P2 feedback on dominoes). Each authority is named by what it governs or who issued it ('my hand-off notes', 'Brian's pack list', 'the kickoff hold'); no decoy carries a self-advertising cue. Findability of planned records is proven on the SQL at `/create-injection` (`persona_view.py check-sql`); the base decoys are YES in the reach table (§10).
""")

# ------------------------------------------------------------------ 4 lattice
P.append("## 4 Delegation lattice\n\n" + table(["Anchor", "Anchor name (noun phrase, ≤ 6 words)", "Record"],
    [(a["id"], a["prompt_reference"], f"`{a['locator']}`") for a in man["anchors"]]) + f"""

**Hub.** Frederick's DM `{S['ask']['id']}` (planned wording in `plan/planned_texts.py`). It delegates by role: 'Brian's pack list', 'Robert's picks', 'My hand-off notes', 'the channel'. It names no location, no id and none of the records in §5 that decide a row. The notes define the three states, the current-version test, the sound test, the board, the ticket follow-through and the sharing, as plain definitions; they point at the pack ticket, the design page, the deck, the kickoff hold and Contacts by name, and at nothing that decides a hidden row.

**Incorporation table** (every `delegation_quote` is an exact substring of the delegating record's planned or base text; the gate reads them):

""" + table(["Fragment", "Service · container", "Kind", "Chain", "Delegated by", "Words (verbatim)", "Requirements", "Names"],
    [(f["id"], f"{f['service']} · `{f['container']}`", f["kind"], " → ".join(f["incorporated_via"] + [f["id"]]), f"`{f['delegated_by_record']}`",
      "'" + f["delegation_quote"] + "'", ", ".join(f["requirement_ids"]), ", ".join(n["id"] for n in f.get("names_authorities", [])) or "—") for f in man["ask_fragments"]]) + f"""

{len(man['ask_fragments'])} fragments over 8 services and 14 containers. **Amendment:** K11, Robert's 26 Sep reply, in another channel and three days after K3; it changes one clause (the iron) and the ask keeps his latest word ('unless he's changed them since'); nothing later re-asserts the iron. **Non-authoritative instruction distractors:** Julia's own grenades-and-shuriken idea (T13), Frederick's three-object 'good start' (T18), the March FBX rule from the first playable (T12), Leonard's card (T11).
""")

# ------------------------------------------------------------------ 5 chains, traps, portfolio, liveness
P.append("## 5 Chains and trap register\n\n**Chains** (six, six distinct root causes):\n\n" + table(["Chain", "Root cause", "Hops (service: record — finding)", "Ends in"],
    [(c["id"], c["root_cause"], "<br>".join(f"{h['service']}: `{h['record']}` — {h['finding']}" for h in c["hops"]), c["ends_in"]) for c in man["chains"]]) +
    "\n\n**Trap register:**\n\n" + table(["Trap", "Family", "Services", "Records", "Req.", "Expected wrong reading", "Resolver", "Discovery order"],
    [(t["id"], t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else ""), ", ".join(t["services"]),
      ", ".join(f"`{x}`" for x in ((["confluence:" + B["gdd"]] if t["id"] == "T9" else []) + t["seeded_ids"] + t["base_pointers"])[:4]), t["requirement"], t["expected_wrong_reading"], t["resolver"], t.get("discovery_order", "—")) for t in man["traps"]]) + f"""

Supersession chronology (oldest first, timestamps from the records): T2 `{M.comment_id('claire_ok_bathtub')}` (Claire's note on {tick('Bathtub')}) 2025-09-24T09:20Z → `{S['a2_dm']['id']}` 2025-09-26T08:10Z; T3 `{B['brian_zip1']}` 2025-09-24T12:39Z → `{B['pr462']}` created 2025-09-25T11:43Z, merged 23:15Z; T5 `{S['picks']['id']}` 2025-09-23T17:00Z → `{S['c3_reply']['id']}` 2025-09-26T17:05Z; T8 `{B['vendor_formats']}` 2025-09-16 → `{B['vendor_oct6']}` 2025-09-24 → `{B['vendor_nov3']}` 2025-09-30 (three versions); T15 `{S['deck']['id']}` 2025-09-23T19:50Z → `{S['c3_reply']['id']}`. Every seeded timestamp is before the seed bound; the only later value is the plan field of the hold (start 2025-11-03T17:00Z).

**Hardness v2 trap selection.** Two separate cross-source decisions carry the difficulty, each naming the convincing wrong source and the record that beats it: (1) trap 1, proving done across services — EXPORT: the ticket (Brian, 25 Sep, Done, 'exported, in the outgoing folder') against Arthur's 27 Sep post in #zombie-bugs (he wrote the export button; later; another service); (2) trap 2, a correction somewhere else — ARTHOLD: Claire's own 24 Sep ticket note against her 26 Sep DM (same person, later, another service). Four more are used: trap 4 dates (REVISED, base), trap 5 a rule in the data (AUDIO), traps 2 and 7 (PICKS: a later reply and six lines outside the list), trap 9 work already done (T10: the zombie pack; graded as an exact count of tickets moved, never a 'leaves alone' row). No correction sits in the superseded record's container, in an anchor's container or on a delegation path (`hardness_v2_check` SAME_PLACE clean below). Volume and arithmetic carry no difficulty.

### Mechanism portfolio (S5a)

Candidates considered (grounded in the census files) and the selection:

""" + table(["#", "Candidate", "Coupling", "Verdict", "Reason (record)"], [
    (1, "EXPORT: a multi-select export writes empty shells", "ticket 'exported' → file unusable → Owed + re-export", "selected", f"base precedent of a bad package: `{B['vendor_blank_scene']}`; survives complete retrieval as a join (ticket note 'all twelve in one go' × the post)"),
    (2, "ARTHOLD: the artist withdraws her own 'fine to go'", "ticket note → DM → Owed (art)", "selected", f"Claire makes every board object (census B §D: match3d#412 … #462) and is not in the vendor channel (`{M.VENDOR_CH}` members)"),
    (3, "REVISED: art changed the day after the zip", "delivery date → pull request → Owed", "selected", f"all base: `{B['art_cactus']}`, `{B['art_candy']}`, `{B['art_cone']}`, `{B['art_dart']}`, `{B['art_claire_pr']}`, `{B['pr462']}`, `{B['robert_new_colours']}`"),
    (4, "AUDIO: only owned sound leaves", "file type passes → source sheet → Owed", "selected", "base is silent on sound ownership (census A §E); the cue names come from base (`C09A7PDFYCV/1755541416.578719`)"),
    (5, "PICKS: Robert changes a pick and adds lines in a reply elsewhere", "picks → reply → board and list", "selected", f"parent `{B['art_bow_root']}` is Julia's own base post about the bow"),
    (6, "PARENT: the export failure of a set noted on the pack ticket", "children Done → parent comment → Owed", "selected", f"`linear_get_issue` returns no comments (Ask_Carriers §6b); planned on ART-793, base precedent {B['art792']}"),
    (7, "objects stripped from the beta build", "tracker 'in build' → build content", "rejected", f"base contradicts it: no addressables for objects (`{M.BUGS_CH}/1758905363.341129`)"),
    (8, "item effects as shipped (a design line per object)", "ticket text → pull request review", "rejected", f"effects are spread over dozens of base messages in #zombie-design `{M.DESIGN_CH}` and data files (census A §A2); any seeded effect risks a base contradiction; an inline review also needs a real diff hunk (learnings: Calvin)"),
    (9, "which enemies have full animation sets", "enemy set → animations channel", "rejected", f"card SC-58: the monster roster on `{B['gdd']}` is a known conflict; the four zombies are fixed by one seeded answer `{S['zpicks']['id']}` and one light row"),
    (10, "a due date on a calendar hold against 'a week before'", "rule arithmetic → hold", "rejected", f"two fair dates with no resolving record: a UGT fork; the hold `{S['hold']['id']}` is kept only for its attendees"),
    (11, "vendor labels as an alias for lines", "acceptance note → label map", "rejected", f"the note would sit in the hub channel `{M.VENDOR_CH}` that every run reads to the end; the map would be the whole trap"),
    (12, "interface art changed by match3d#471", "sent UI → later pull request", "rejected", "'UI polishes' does not say which pieces: a fork"),
    (13, "a brief that is valid under each pivot option", "pivot options → brief", "rejected", f"the options are undecided in base (`{B['leonard_priorities']}`): no truth value"),
    (14, "lines defined by level number ('by level 40')", "level export → list", "rejected", f"level content at the clock is in repository files the tools do not read; the July export `{B['july_export']}` is stale and its readability for Julia is not proven"),
]) + "\n\n**Selected rules** (one per solver rule; draft manifest `mechanism_portfolio`). Ledger priors for `claude-opus-5-5`, UNCALIBRATED (`hardness_ledger.py priors`; `plan/out/ledger_priors.txt`):\n\n" +
    table(["Rule", "Mechanism", "Prior family · prior · record ids", "Natural reading", "Decides", "Control · over-application", "Stays hard after complete retrieval", "Natural call that returns the decider", "Slots it flips"], [
    ("EXPORT", "A24", "done_gap · Beta(1.0, 2.86) mean 0.26 · `hev_7af7471ca0d3855f`, `hev_bdb9590893044914`, `hev_e30a8c13fa044076`", "the twelve are Ready", "State, What's owed, Who has it", "Rolling Pin (exported on its own) · export_over", "joining 'all twelve in one go' on the ticket to a post that names no object", f"`slack_read_channel` or a search of #zombie-bugs → `{S['a1_post']['id']}`", "X1, X6, X16, W4, A1, A2, W1, W2"),
    ("ARTHOLD", "A11", "superseding · Beta(2.57, 1.29) mean 0.67 · `hev_d4e1db2db22b1a55`, `hev_a9c69a91cf1cefd0`, `hev_01debb8fc63f4c1e`", "the twelve are Ready", "State, What's owed, Who has it", "Armchair (Claire's note stands) · art_over", "mapping 'the bathroom ones' to the list's set", f"reading Julia's DM with Claire → `{S['a2_dm']['id']}`", "X2, X7, X11, W5, A1, A2, W1, W2"),
    ("REVISED", "A1", "stale_summary · Beta(1.0, 2.85) mean 0.26 · `hev_5ad302a3d2e2ed5b`, `hev_6aa0e2dc797c1a41`, `hev_8c277ed5dc029ed7`", "three Delivered, two Ready", "State, What's owed", "Grenade (in the same zip, unchanged) · revised_over", "comparing each line's send or export time with 25 Sep 23:15 UTC", f"`github_list_pull_requests` then the file list of `{B['pr462']}`; or #zombie-art", "X3, X8, W6, A1, A2, A3, W1, W2, W3"),
    ("AUDIO", "A13", "authority · Beta(1.0, 2.86) mean 0.26 · `hev_c4bbc05b4e9b08ea`, `hev_923eb1fef7d8dc20`, `hev_0eec4f03fda7d5a4`", "all five exported cues are Ready", "State, What's owed, Who has it", "Win stinger (made here) · audio_over", "applying an ownership rule to a source column", f"a Drive search for the sound sheet, then its rows → `{S['c2_sheet']['id']}`", "X5, X10, X12, W8, B6, A1, A2, W1, W2"),
    ("PICKS", "A14", "superseding · same prior and records as ARTHOLD", "iron in the eight; 97 lines", "Board set, Line", "Grenade (unchanged pick) · picks_over", "the latest word wins; six lines need tickets", f"`slack_read_thread` on Julia's bow post `{B['art_bow_root']}`, or a search for the iron → `{S['c3_reply']['id']}`", "X13, X14, X15, V1, B1, W10, W11, A1, W1"),
    ("PARENT", "A3", "tool_surface · Beta(1,1), no ledger record: UNPARAMETERIZED", "the eight are Ready", "State, What's owed, Who has it", "Record Player (exported on its own, 25 Sep) · parent_over", "mapping 'the music set from Friday's export' to eight lines", f"`linear_list_comments` on ART-793 → `{S['c4_comment']['id']}`", "X4, X9, W7, A1, A2, W1, W2"),
]) + f"""

A5b checks per rule: **incorporated** — each state follows from the notes (K1) applied to records Julia can read; **survives complete retrieval** — each needs a join after the record is found (set or export method → lines); **tool-surface proof** — every decider is a top-level message, a ticket comment, a sheet or a base pull request that the named call returns (no DM thread reply, no attachment body, no result that depends on a search missing); **graded weight** — each flips at least one weight-5 slot. No liveness flag is resolved by removing an incorporation link.

### Liveness flags (S5b)

`trap_liveness.py --design` (advisory, UNCALIBRATED; `plan/out/trap_liveness.txt`) raises one kind of flag, `breadcrumb`, on eleven traps. Dispositions:

""" + table(["Trap", "Flag", "Disposition"], [
    ("T4", "breadcrumb", f"the notes `{S['notes']['id']}` carry the sound rule, as they must for incorporation; they do not name Calvin's sheet `{S['c2_sheet']['id']}`, its title or its owner. Kept."),
    ("T5, T6, T15", "breadcrumb", f"the ask `{S['ask']['id']}` says 'unless he's changed them since': it authorises a later change and gives no place, date or word of it. The reply is under a post about an arrow in another channel. Kept; the wording sweep on the SQL checks that the reply shares no rare word with the ask."),
    ("T8", "breadcrumb", f"all three dates are in the channel the ask names (`{M.VENDOR_CH}`); this is a realism trap with no budget weight."),
    ("T12, T13, T16, T17, T18, T19", "breadcrumb", f"distractors on the read path by design (`{M.VENDOR_CH}`, `{M.DESIGN_CH}`); none carries budget weight."),
]) + "\n\n`hardness_v2_check.py --design` (verbatim):\n\n" + code(read(OUT / "hardness_v2_check.txt")) + """

Dispositions: no FLAG and no UNRESOLVED. SAME_PLACE is clean over five version chains; it is re-run on the SQL. INPUT_CHECK reports no weight-5 total: the three counts are weight 3 (calculation) and each is moved by at least one rule, so none is plain arithmetic on clean inputs. RULE_IN_PROMPT runs when the prompt exists.
""")

# ------------------------------------------------------------------ 6 failure diversity
P.append("## 6 Failure-diversity plan\n\nEach unit is one deciding record behind its own retrieval habit, so a run's misses are a subset of six independent records. Budget table (`difficulty_budget.py table`, weights from the rubric skeleton `01_Rubric_Skeleton.json`, the rows the portal's rules force):\n\n"
         + read(OUT / "difficulty_budget_table.md") + "\n\n`difficulty_budget.py check` (verbatim):\n\n" + code(read(OUT / "difficulty_budget_check.txt")) +
         "\n\n`rubric_skeleton.py check` (verbatim):\n\n" + code(read(OUT / "rubric_skeleton_check.txt")) +
         "\n\nWhole policies and single misses on the skeleton, and the six-run simulation (`plan/policy_scores.py`, UNCALIBRATED; verbatim):\n\n" + code(read(OUT / "policy_scores.txt")) + f"""

**Reading.** E[average] is 30–50 % and P(all gates) 0.55–0.73 at the budget's find-rate ranges; both targets (≤ 62 %, ≥ 0.5) hold at every setting. The printed spread chance is 0.549 / 0.689 / 0.730 (low / middle / high find rates): the spread gate is the binding one and the tool warns below 0.70. Reaching 0.8 would need about 60 % of the weight on coin-flip records on top of the anchors' 32 %; this design carries 45.1 %. A spread miss on a baseline that passes every other gate is reported to the owner (owner decision of 2026-11-10). No single miss clears the cap: a run that misses one record scores 79–87 %; the average holds only when runs miss several. The ledger-prior forecast (§12) gives a second, less favourable view.

**Which runs miss what.** A1 and A2 are found by few runs: neither record holds a word of the ask, an object name or a ticket key, and neither container is named by anything the run reads. C1 is found by runs that check what changed after the zip (a pull request list or #zombie-art after 24 Sep). C2 by runs that look for where the sound came from. C3 by runs that open Julia's bow thread or search for the iron. C4 by runs that read the pack ticket's own comments. The six habits are different calls in five services, so two runs rarely share a signature. No single discovery decides more than 16.6 % of the weight.

**Lessons applied** (`00_Pre_Scenario_Analysis.md` §9b; Frederick's rev10 forensics, `task_inputs-uselater/Working_Files/01a_Hardening_Report.md` §8): in twelve runs a broad Slack search on the task's key noun returned every correction that held it. Here no deciding record contains 'playable', 'PlayableX', 'pack', 'brief', 'hand-off', 'asset', 'FBX' or 'vendor'; the SQL wording sweep at `/create-injection` enforces it. Inline review comments are not used (found by all or none). Every miss moves a count in one direction (Owed up, Ready or Delivered down), so misses cannot cancel in the reply.
""")

# ------------------------------------------------------------------ 7 deliverables
P.append("## 7 Deliverables and dependent writes\n\n" + table(["Write", "Tool", "Count", "Depends on", "Requirements"],
    [(w["service"], f"`{w['tool']}`", w["count"], ", ".join(w["depends_on"]), ", ".join(w["requirements"])) for w in man["writes"]]) + f"""

- **Hand-off list** (Google Sheet in Julia's Drive root `{B['julia_root']}`): one row per line ({n_all}); columns line, kind, board set (Default / Extra / blank), state, what is owed, who has it, ticket. Totals {C['Delivered']} / {C['Ready']} / {C['Owed']}.
- **Brief** (Google Doc in her Drive): Scenario 1; the default eight (Grenade, Couch, Plushie Chick, Bow, Shuriken, Cute Axe, Cactus Plant, Gift Box) and the extras; four zombies (Chef, Bike Kid, Boxer, Mayor) and walk as the primary animation; a 7-slot tray, the level is lost when the zombies take the player's health to zero and won when all are cleared; the file types the vendor takes; sound: only owned cues, music starts after the first click; start 3 November. Free-text parts are bounded: any wording that states these facts is accepted.
- **Tickets:** the {len(owed_tix)} Owed lines that have a ticket go back to Todo (every line ticket starts Done) with a comment saying what is owed and who has it; the six added lines get a new ticket under ART-793 (reuse-versus-create: no line that has a ticket gets a second one). The 49 Delivered and Ready tickets are not touched: graded as the exact count of tickets moved (48), never as a 'leaves alone' row.
- **Shares:** both files, view only, to the three other attendees of the kickoff hold and to PlayableX's intake address (eight share calls).
- **Messages:** the three counts to Frederick in `{M.DM_FRED}`; both links in `{M.VENDOR_CH}`.

Every write's content depends on findings (`depends_on`); none is a bolt-on. Each is asked for by the ask or the notes (trigger Julia owns), each target is hers to write: she owns both new files, is a member of both Slack conversations (`can-see` YES), and Linear writes are unscoped for an ART team member (`/team_memberships`: Julia is in ART).
""")

# ------------------------------------------------------------------ 8 service role map
order = ["slack", "linear", "gsheets", "gdocs", "gdrive", "gslides", "gcal", "contacts", "github", "confluence", "trello", "gmail"]
carrier = {"slack": "● message text, thread replies, DMs", "linear": "● description, state, parent; comments ● per §6b", "gsheets": "● grid", "gdocs": "● body_text",
           "gdrive": "● name, parents, sharing", "gslides": "● element text", "gcal": "● summary, start, attendees", "contacts": "● email, job",
           "github": "● PR title, dates, files (base)", "confluence": "● page body, comments (base)", "trello": "● card, commentCard action", "gmail": "● invitation mails (companions)"}
P.append("## 8 Service role map\n\n" + table(["Service", "Role", "Load-bearing fact or write", "Carrier"],
    [(s, man["services"][s]["role"], man["services"][s]["weight_reason"], carrier[s]) for s in order] +
    [("snowflake", "not used", "none: nothing in the pack is measured in the warehouse, and Snowflake cannot be injected", "—")]))

# ------------------------------------------------------------------ 9 call budget
P.append("## 9 Call budget\n\n" + table(["Phase", "Service", "Calls", "Reason"], [(r["phase"], r["service"], r["calls"], r["reason"]) for r in man["call_budget"]]) + f"""

Total {budget_total} unconditional calls over 11 services; per-record {per_rec}; the largest share outside the per-record phase is 30 % (gate output, §12). No row is conditional on an unverified tool behaviour. **Golden-run rule:** a correct run needs the volume: {n_list} comment reads fill the state column, {len(owed_tix)} comments and 40 state writes are the follow-through, six tickets are new. **Every-run floor:** a run that finds no hidden record still reads the {n_list} tickets' comments, because ticket state and the pack list say nothing about a line's state, and moves and comments the nine lines that are Owed on their own note: about 40 discovery and rule calls + {n_list} reads + 18 ticket writes + 16 for the two files, the shares and the messages ≈ 171 counted calls, over the requester's 130. If the pre-check comes in under 150 the design is revised before any baseline.
""")

# ------------------------------------------------------------------ 10 QC rails
two = [
    ("How many lines", "103: Brian's 97 plus Robert's six", "97: the pack list as it stands", "the notes: 'If Robert has added objects since Brian made the list, they go on it too'; Robert's reply names six and says they go over", f"`{S['notes']['id']}`, `{S['c3_reply']['id']}`"),
    ("Twelve lines exported in one go", "Owed, re-export (Brian)", "Ready: tickets Done, files in the outgoing folder", "Arthur wrote the export button and says every file from a multi-select run is an empty shell; the notes require that a Ready file opens", f"`{S['a1_post']['id']}`"),
    ("Twelve bathroom lines", "Owed, art (Claire)", "Ready: Claire's own 24 Sep note says fine to go", "the same person, later: she is redoing the UVs and what Brian pulled is the old unwrap; the notes require that nobody is changing it", f"`{S['a2_dm']['id']}`"),
    ("Five lines changed on 25 Sep", "Owed, send the current version", "Delivered or Ready: new colour versions are additions, the file sent is unchanged", "the notes name the case: 'a fix, a retexture, new colour versions', 'so they always hold what the game has'", f"`{S['notes']['id']}`, `{B['pr462']}`, `{B['robert_new_colours']}`"),
    ("Eight music lines", "Owed, another export pass (Brian)", "Ready: tickets Done, .glb is a type the vendor takes", "Brian's own later comment: the set comes in grey and needs another pass before it goes", f"`{S['c4_comment']['id']}` on ART-793"),
    ("Match scale and Explosion", "Owed, a cue we own (Calvin)", "Ready: .wav is a type the vendor takes", "the notes: only what we own outright leaves; Calvin's sheet marks both as cut from a bought pack", f"`{S['c2_sheet']['id']}`"),
    ("The default eight", "with the bow, without the iron", "with the iron (Robert's 23 Sep picks, Julia's deck)", "Robert's own later reply; the ask keeps his latest word", f"`{S['c3_reply']['id']}`"),
    ("The four zombie lines", "Delivered", "Owed: the vendor said the package was not exported correctly", "base: the full pack went on 26 Sep and the vendor reviewed it on 29 Sep", f"`{B['brian_pack3']}`, `{B['vendor_zombie_ask']}`"),
    ("Tray size", "seven slots", "six (Julia's July proposal)", "base: Robert's reply keeps the page at seven", f"`{B['gdd']}`, `confluence:{B['gdd_c2']}`"),
    ("Start date", "3 November", "6 October", "base: the vendor's latest message", f"`{B['vendor_nov3']}`"),
    ("Who the files are shared with", "both files, view only: the three other attendees of the hold and the intake address", "the brief only; or Leonard (his card is the 'kickoff')", "the notes: 'Sharing: both files, view only', the kickoff hold and Contacts", f"`{S['hold']['id']}`, `{S['contact']['id']}`"),
    ("Where the counts go", "Frederick's DM, as a message or a thread reply under his ask", "the vendor channel", "the ask: 'give me the three counts here'; both forms in the DM are accepted", f"`{S['ask']['id']}`"),
    ("Ticket follow-through on an Owed line", "Todo plus a comment", "a description edit, or a new ticket", "the notes: 'goes back to Todo with a comment'; a new ticket only for a line without one", f"`{S['notes']['id']}`"),
    ("Buttons", "Owed (parts not separated), ticket back to Todo", "Delivered: sent on the 24th", "its own ticket note; the vendor takes 2D as PNG with parts separated", f"`{tick('Buttons')}`, `{B['vendor_asset_list']}`"),
    ("The plushie line", "Delivered, one line", "a missing 'duck' line", "base: the vendor's duck is the plushie sent the same day", f"`{B['vendor_duck']}`, `{B['brian_zip2']}`"),
]
P.append("## 10 QC rails\n\n### Two-reading table\n\n" + table(["Decision point", "Best reading", "Strongest alternative", "Resolved by", "Evidence"], two) +
    "\n\nNo figure forks: no BOTH_FAIR_FIGURE is declared. Dates: every graded date has the same Pacific and UTC day (3 November 17:00 UTC is 09:00 PT).\n\n### Reach table (load-bearing records)\n\nBase records (`persona_view.py can-see julia_lawson …`, run by `plan/reach_table.py`):\n\n" + read(OUT / "reach_table.md") + f"""

Planned records are checked at the injection gate (`persona_view.py check-sql`). Their planned access: the ask and Claire's message are in Julia's own DMs; the picks, the reply and Arthur's post are in channels she is a member of; the notes, the pack list, Calvin's sheet are shared with her and the deck is hers; the hold has her as an attendee; Linear, Trello and Contacts are unscoped. Records she cannot read are never load-bearing: `#executives`, the Leonard–Frederick–Brian group DM and the vendor's DM with Leonard are cited in §1 and §1a as whole-base consistency checks only, and the July export sheets (UNVERIFIED) are cited only as the source of object names.

### Feasibility, precedence, naturalness, grading devices

- **Feasibility.** Tools in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`, `gdocs_create_document`, `gdocs_batch_update`, `gdrive_share_file`, `linear_update_issue`, `linear_create_comment`, `linear_create_issue`, `slack_send_message`. One sheet with one tab; no multi-tab creation is needed. The outside recipient has an authorised path: the notes name the intake address in Contacts and the sharing level (view only).
- **Explicit rules.** Multi-version evidence: the later record by the same or the owning person stands (ask, notes). What 'now' means: the game as it is today (ask). Each write's end state is in the notes. Every cross-reference postdates its target (Robert's reply after Julia's post; Brian's comment after his export; Arthur's post after the export).
- **Precedence.** Load-bearing facts sit only in ● carriers (Ask_Carriers §5 as amended by §6b): Slack text, Linear comments, Sheets grids, Docs body, Slides element text, calendar summary and attendees, Contacts email, base PR fields. Nothing load-bearing is in a calendar description, slide notes, a Drive `content_text` or a Slack file.
- **Prompt naturalness.** The human's trigger needs: Frederick's message as the starting point, that the job is all of it, the two deliverables and that they go in her Drive, the PlayableX channel. It must not carry: the three state words, any rule, any set or object name, any count, any ticket key, the channels of §5, or where the notes and the list live.
- **Grading devices.** Exact key set of the list ({n_all}); three totals; at most five samples per group (state, what is owed, who has it, board set, Todo moves) with a volume row; one row per comment target and per new ticket; the exclusion as an exact count (48 tickets moved to Todo). No graded count, format or limit that the ask or the notes do not state.

### Coherence rail

Every §1a row is dispositioned. Designed disagreements are dated human claims with a named later record: Brian's ticket notes (25–26 Sep) against Arthur's post (27 Sep) and his own comment (29 Sep); Claire's note (24 Sep) against her DM (26 Sep); Robert's picks (23 Sep) against his reply (26 Sep). No two system fields disagree: tickets stay Done until the run moves them, which is the task. Companions planned with each record are in §11. No seeded text names a git branch, a build number or a release; the one base artifact the plan relies on is match3d#462 (title, created and merged times, changed objects), cited as base states it. Ids follow the base schemes (§2, §11).
""")

# ------------------------------------------------------------------ 11 record plan
rec = [(k, v["svc"], f"`{v['id']}`", v["at"], v["by"], v["what"]) for k, v in S.items()]
rec.insert(6, ("tickets", "linear", "`ART-794` … `ART-890`", "2025-09-23 to 2025-09-26", "Brian Foster (creator); notes by Brian, Claire, Calvin", "one ticket per listed line, title = the line's name, parent ART-793, state Done (all 97, closed by Brian as he dealt with each); one note by Brian on each saying what he did, art notes on 31, raw facts only"))
P.append("## 11 Record plan for /create-injection\n\n" + table(["Key", "Service", "Id", "At (UTC)", "By", "What"], rec) + f"""

Planned wording of the ask and the notes: `plan/planned_texts.py`. Per-line ticket notes by class (`plan/design_model.py`): Delivered — 'In the zip that went over on the 24th'; Ready — 'Exported on its own', with the date and file type; EXPORT — 'Exported, all twelve in one go, 25 Sep'; Bathroom — Claire's 'fine to go' (24 Sep) then Brian's export note (25 Sep); Music — 'Exported as .glb, Fri 26 Sep'; sound — 'Exported .wav'; visible Owed — what is missing. Haystack: routine traffic around each deciding record is base (#zombie-bugs 3,830 messages, Julia's DM with Claire 2,687, #zombie-art 2,650); `path_exposure.py` at injection decides whether more is needed. Size about 330 rows over ten schemas (slack, linear, gsheets, gdocs, gdrive, gslides, gcal, gmail, trello, contacts); Snowflake and Confluence are not injected.

### Integrations and companions

""" + table(["Service", "INT id", "Companion", "Decision"], [
    ("slack", "INT-13 (Drive app DMs), INT-04 (Linear app posts)", "share and ticket notifications", "none seeded: base has no Linear-app post for ART tickets (ART-790, ART-792 have none) and the shares are covered by mail (INT-11 pattern below); thread counters of Julia's bow post are updated"),
    ("linear", "INT-04, INT-05", "Slack posts, e-mail digests", "none: ART tickets created outside Slack have no bot post in base; digests are not per ticket"),
    ("gcal", "INT-11", "invitation mails", "seeded: one event row per attendee calendar (same `ical_uid`) and one invitation mail per attendee mailbox"),
    ("gmail", "INT-11, INT-22", "the invitation mails themselves", "seeded as companions only; no deciding fact in mail (Gmail is THIN for the persona)"),
    ("gdrive, gdocs, gsheets, gslides", "INT-13", "Drive rows mirror Docs, Sheets and Slides ids and sharing", "seeded: one `drive_files` row per file with identical sharing; Julia owns the deck"),
    ("trello", "INT-21", "none exists", "trello: none — the card's and the board's dateLastActivity move with the comment"),
    ("contacts", "—", "none", "contacts: none — a single row in the base shape (15 fields)"),
    ("github", "INT-01, INT-03", "Slack mirror, linear[bot]", "github: none — nothing is seeded in GitHub; match3d#462 is base and has no comments to mirror"),
]))

# ------------------------------------------------------------------ 12 self-test
review = [
    ("temporal", "The ask is dated after the pause and asks for prep the pause was meant to stop.", f"the four 29 Sep base lines (§1) object to vendor development on a game that may change, not to knowing what the vendor holds; the ask scopes to 'the game as it is today' and says the part is redone if the core changes (`{S['ask']['id']}`; `CADCE44A365D/1759172311.343939`)", "holds"),
    ("semantic", "'Owed' could mean owed by the vendor, or money.", f"the notes define the three states in one paragraph and nothing else uses the words (`{S['notes']['id']}`); learnings §80: each label defined in a record", "holds"),
    ("cross-service referential", "The pack list and the tickets can disagree on a line's name or ticket.", f"both are generated from one model (`plan/design_model.py`: the pack list `{S['tracker']['id']}`, tickets ART-794 to ART-890); the injection gate's `fact_check` holds them to it", "holds, enforced at injection"),
    ("quantitative", "19 / 30 / 54 could fork on Buttons or the plushie.", f"Buttons is Owed on its own ticket (`{tick('Buttons')}`); the plushie is one Delivered line (`{B['brian_zip2']}`); both are in the two-reading table", "holds"),
    ("state/lifecycle", "Done tickets for files that are unusable are a State/Lifecycle inconsistency in the seeded data.", f"each is a dated human claim (Brian's note) overturned by a named later record (`{S['a1_post']['id']}`, `{S['c4_comment']['id']}`); the task is to move them; card SC-16's tickets are not touched", "holds as a designed claim"),
    ("identifier/format", "ART-793 to ART-890 could collide or break the series.", "base highest is ART-792 with gaps before it (census C §1); `plan/check_ids.py`: 0 hits, scan complete", "holds"),
    ("other", "A reviewer reads the cohort as padding: 103 lines for one ad.", f"the vendor asked for each group (`{B['vendor_asset_list']}`), offers extra editable items (`{B['vendor_formats']}`) and Brian planned to 'upload all the objects' (`{M.DESIGN_CH}/1758569323.919359`); every line is a cell of the list the ask requests", "holds"),
] + [("decision: " + r[0], f"the alternative: {r[2]}", f"{r[3]} ({r[4]})", "best reading stands") for r in two]
P.append("## 12 Self-test results\n\n`hardness_gate.py … --design` (verbatim):\n\n" + code(read(OUT / "hardness_gate_design.txt")) +
    "\n\n`gradable_surface.py validate` and `gradeable-report` (verbatim):\n\n" + code(read(OUT / "gradable_surface.txt")) +
    "\n\nId collision check (`plan/check_ids.py`, `hg.py search lookup`; verbatim):\n\n" + code(read(OUT / "check_ids.txt")) + f"""

**Lazy-solver pass.** An agent that makes one broad search per service, reads first hits, opens no thread, stops at the first conclusion and uses every bulk call: it finds the ask, the notes, the pack list and the vendor channel's last page; lists the 97 children with descriptions in two calls; reads no comments. It scores the delivery rows and the brief rows that come from the hub (scenario, start date), about 9 % of the skeleton weight; it cannot fill the state column, because no bulk call returns a ticket's notes. Leaks looked for and closed: the pack list has no state or note column; every line ticket has the same workflow state (Done), so state is no proxy for Ready or Owed (an earlier draft left the nine self-stated Owed tickets in Todo: closed); ticket descriptions carry the line's name and kind only; no ticket title or label marks a class; the notes name no deciding record.

**Literal-value sweep and wording sweep** (base, `plan/literal_sweep.py` through `tools/hg.py search-many` over eleven services, output in `plan/out/literal_sweep.txt`; the SQL repeats both): 'empty shell', 'old unwrap', 'comes in grey', 'instead of the iron', 'object browser', 'hand-off notes', 'own outright', 'outgoing folder', 'redoing the UVs', 'sound source' and 'intake@' have no base hit. 'bought pack' has one, a 2024 DM about in-app purchase packs (`D07GJJBFHA5/1727689171.546549`); 'multi-select' has a July 2025 #zombie-art reply about a player-facing selection screen (`C08R8CHB0QL/1753362278.857159`), a 2023 stand-up transcript in Docs and four vendor newsletters in Gmail; 'pack list' has two 2024 hits about puzzle packs (`D0770ET1HV2/1720174256.332539`, a bot post in `C050WGU41HR`) and one pull-request body. None concerns asset export, sound sources or this pack, so the planned facts contradict nothing. None of the six deciding records is planned with a word of the rule it triggers ('opens', 'current version', 'changing', 'own outright', 'picks').

**'The rest stands' check.** Robert's reply changes one object; no later planned record re-lists the eight. The deck (23 Sep) is the older version and is not edited after the reply.

**S9b prior forecast** (advisory, UNCALIBRATED, pre-registered): see the forecast block pasted below by `plan/run_gate.sh`.

{read(OUT / 'forecast.txt')}

### Self-review

Gate output re-read after the last change: `HARDNESS GATE (extreme (design)): PASS` (pasted above, with its 37 ok lines and the volume-exception note). Re-read as the eval: `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and `Evals/0_Injection_Quality_Eval.md` Check C, walked against §1a, §7 and §10. Load-bearing base values were re-read through `tools/hg.py` in this session (the vendor channel in full, the six #zombie-art messages, match3d#462's title and times through census C §3, the design page and its two comments, the Trello card and its three actions, Julia's DM and channel memberships).

""" + table(["Item", "Counter-reading (the best case that it fails)", "Resolution (evidence)", "Verdict"], review) + f"""

Required items addressed: the two v2 decisions and their sources (§5); corrections off the first-read path (§5, v2 check); reach (§10); feasibility (§10, §7); volume and the every-run floor (§9); budget and spread (§6); known-data-issue cards (§1a); padding (§2).

Unresolved: none that blocks the design. Carried to `/create-injection` as checks, not open questions: the SQL wording sweep; `path_exposure.py` on the six deciding records; the cold-solver rehearsal; `persona_view.py check-sql` on every planned record.
""")

# ------------------------------------------------------------------ 13 red team
P.append(read(OUT / "redteam_section.md"))
out = WF / "01_Scenario_Design.md"
out.write_text("\n\n".join(P) + "\n")
print("wrote", out, len("\n\n".join(P)), "chars")
