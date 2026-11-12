#!/usr/bin/env python3
"""Assemble Working_Files/01_Grounding_Dossier.md (injection rev2, design D3) from the model, the final manifest, the SQL and
the pasted tool outputs. Facts only: no prompt, Oracle Event or criterion text. Re-run after any SQL change, then the gate."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TI = WF.parent
OUT = HERE / "out"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TI.parent / "tools"))
import design_model as M
import planned_texts as TXT
from base_check import parse_sql

man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
truth = json.loads((WF / "solver" / "truth.json").read_text())
ids = json.loads((OUT / "sql_ids.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
S, B, PT = M.SEED, M.BASE, M.PACK_TICKET
SQL = (TI / "01_Universe_Inject.sql").read_text()
rows = [x for x in parse_sql(SQL)]
by_table = {}
for x in rows: by_table.setdefault(x["table"] + (" (UPDATE)" if x["op"] == "update" else ""), []).append(x)
read = lambda p: Path(p).read_text().rstrip("\n")
code = lambda t: "```\n" + t + "\n```"
def tick(n): return M.BY_NAME[n]["ticket"]
def table(head, rws):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rws])
def sid(k): return M.slack_id(*S[k]["id"].split("/"))
C = M.COUNTS
n_list = M.N_LIST
TICKS = f"{tick(M.LINES[0]['name'])} to {M.LAST_CHILD}"
JULIA = "julia.lawson@harmonygames.co"
lint = json.loads((OUT / "hg_lint.json").read_text())

sweep = json.loads((WF / "01d_Coherence_Sweep.json").read_text()) if (WF / "01d_Coherence_Sweep.json").exists() else {}
def _short(s, n=150): s = " ".join(str(s).split()); return s if len(s) <= n else s[:n - 1] + "…"
SWEEP_TABLE = table(["Id", "What forked or conflicted", "Material", "Status", "Settled by"],
    [(f.get("id"), _short(f.get("title") or f.get("span")), "yes" if f.get("material") else "no", f.get("status"),
      _short(f.get("how") or ", ".join("`" + i + "`" for i in (f.get("settled") or {}).get("record_ids", [])) or f.get("reason"), 600)) for f in sweep.get("forks", [])] +
    [(d.get("id"), _short(d.get("defect")), "-", d.get("status"), _short(d.get("how") or d.get("reason") or ", ".join("`" + i + "`" for i in (d.get("fix") or {}).get("record_ids", [])), 600)) for d in sweep.get("siblings", [])]) if sweep else "pending"
def _fc(path):
    t = read(path)
    m = re.search(r"'id': '(hev_[0-9a-f]+)'", t)
    e = sorted(float(x) for x in re.findall(r"E\[avg\] ([0-9.]+)", t))
    p = re.search(r"P\(all four difficulty gates\) ([0-9.]+-[0-9.]+)", t)
    return (m.group(1) if m else "?"), (f"E[average] {e[0]:.3f} to {e[-1]:.3f}, P(all four difficulty gates) {p.group(1)}" if e and p else "see the output")
FC_DESIGN_ID, FC_DESIGN = _fc(OUT / "forecast.txt")
FC_INJ_ID, _ = _fc(OUT / "forecast_injection.txt")
_rows = {l.split()[0] + (" " + l.split()[1] if l.split()[0] in ("low", "high") else ""): l.split() for l in read(OUT / "policy_scores.txt").splitlines() if l.strip().startswith(("low find", "midpoint", "high find"))}
FC_BUDGET = "; ".join(f"{k}: E[average] {v[-8]} %, P(average under 70 %) {v[-6]}, P(spread in band) {v[-4]}, P(all gates) {v[-2]}" for k, v in _rows.items())
def _sweep_summary():
    if not sweep: return "the sweep record is pending."
    forks = sweep.get("forks", [])
    by = {}
    for f in forks: by[f.get("status")] = by.get(f.get("status"), 0) + 1
    mat_open = sum(1 for f in forks if f.get("material") and f.get("status") not in ("settled_in_data", "both_fair"))
    return (f"{len(forks)} forks taken up ({', '.join(f'{v} {k}' for k, v in sorted(by.items()))}), {len(sweep.get('open_sets', []))} open sets with a rule and a census, "
            f"{len(sweep.get('dismissed', []))} findings dismissed with a reason; material forks left open: {mat_open}.")
SWEEP_SUMMARY = _sweep_summary()
P = []
P.append(f"""# Grounding Dossier — {M.SLUG} · {M.REV} (design {M.DESIGN}) · facts only, no prompt, OE or criterion text

**rev2 (2026-11-12).** This revision implements design D3 (`01_Scenario_Design.md` §14), after the pre-check and the six-run baseline of rev1 (`01a_Hardening_Report.md`). Four seeded records change and nothing is added: Robert's note to Julia `{S["a2_dm"]["id"]}` replaces Claire's Turkish DM as the record on the bathroom redo; Marcus's post `{S["a1_post"]["id"]}` loses the words of the note it corrects; Brian's log `{S["c4_log"]["id"]}` says 'The .wav exports.' instead of 'The sound files.' and records that Claire sent the three recoloured models again, so Cactus Plant, Chainsaw and Cone are Ready. Truth moves from 8 / 36 / 52 to {C["Delivered"]} / {C["Ready"]} / {C["Owed"]}. The rev1 SQL is kept in `Working_Files/run_forensics/rev1/` (with the bytes the platform ran in `submitted/`) and its design artifacts in `run_forensics/rev1/artifacts/`.

Written by `/create-injection` (Claude, authoring session). The SQL is `01_Universe_Inject.sql` ({sum(1 for x in rows if x['op'] == 'insert')} INSERT, {sum(1 for x in rows if x['op'] == 'update')} UPDATE, ten schemas). Linear and Slack rows come from the generator (`Working_Files/spec/spec.json`, rendered by `Task_Authoring/generators/render.py`); the other services from `Working_Files/plan/build_sql.py`. Universe: `{ctx['universe']['clock_line']}`; seed bound {ctx['freeze_utc']}. Every base fact below was read through `tools/hg.py` in this session or by the two reviewers' fact pack (`Working_Files/research/base_facts_D2.md`, record ids with each fact).

## 1.A Structural

""" + table(["Table", "Rows", "Base location (pointer)", "Base sample ids", "Notes"], [
    ("slack.slack_messages", f"{len(by_table.get('slack.slack_messages', []))} INSERT, 1 UPDATE", "`slack/messages/<channel>/<YYYY-MM>.json` (array of messages)", f"`{B['art_bow_root']}`, `{B['vendor_nov3']}`, `{B['anim_pack']}`", "id = sha256(channel|ts)[:32]; ts with six decimals; created_at ISO with microseconds; the UPDATE sets the bow post's reply counters (generator convention slack.thread.counters)"),
    ("linear.linear_issues", len(by_table.get("linear.linear_issues", [])), "`linear/data.json` `/issues` (3,687 in base; 247 in the Design team)", "`DES-312`, `DES-311`, `DES-307`", "id = identifier = DES-n; `state_id` holds the state name (Done, In Progress, Todo); text ISO-Z stamps; `state_history_json` an empty JSON array; `time_in_status_minutes` NULL"),
    ("linear.linear_comments", len(by_table.get("linear.linear_comments", [])), "`linear/data.json` `/comments` (empty in base)", "none in base; accepted injections carry them (generator convention linear.comment.shape)", "uuid5 ids; `sequence` 1 per issue; `updated_at` = `created_at`"),
    ("gdrive.drive_files", len(by_table.get("gdrive.drive_files", [])), "`gdrive/data.json` `/drive_files`", f"`{B['julia_root']}`, `d_175c0d7bc72ed244b944cb`, `{B['playable_feedback_doc']}`", "`f_` + 22 hex; parents = the owner's root (`d_` + first 22 hex of the owner's contact id)"),
    ("gdocs.docs_documents", len(by_table.get("gdocs.docs_documents", [])), "`gdocs/data.json` `/docs_documents`", f"`{B['playable_feedback_doc']}`", "`body_text` non-empty; `style_runs_json` TITLE + NORMAL_TEXT; same id and sharing as the Drive row"),
    ("gsheets.sheets_spreadsheets / sheets_sheets", f"{len(by_table.get('gsheets.sheets_spreadsheets', []))} / {len(by_table.get('gsheets.sheets_sheets', []))}", "`gsheets/data.json` `/sheets_spreadsheets/<n>/sheets/<m>/grid`", "`f_7efae6c05be5c2414e8798`", "one tab each; `grid_json` an array of rows"),
    ("gslides.slides_presentations / pages / page_elements", f"{len(by_table.get('gslides.slides_presentations', []))} / {len(by_table.get('gslides.slides_pages', []))} / {len(by_table.get('gslides.slides_page_elements', []))}", "`gslides/data.json`", "shape taken from the accepted injection of `task_inputs-uselater` (same schema)", "facts in element text, none in notes"),
    ("gcal.gcal_events", len(by_table.get("gcal.gcal_events", [])), "`gcal/data.json` `/events`", "`evt_257421bc09196edbf28758`", "`calendar_id` = the owner's e-mail; one row per attendee calendar, shared `ical_uid` (32 hex @hg4), `self:true` on the owner's copy"),
    ("gmail.gmail_threads / gmail_messages", f"{len(by_table.get('gmail.gmail_threads', []))} / {len(by_table.get('gmail.gmail_messages', []))}", "`gmail/threads/<mailbox>_<thread>.json`", "`claire@harmonygames.co_1831622960107831313.json`", "ids `<mailbox>/<Message-ID>` and `<mailbox>/<numeric thread id>`; `internal_date` (ms) = `date`"),
    ("trello.trello_actions; cards and boards (UPDATE)", f"{len(by_table.get('trello.trello_actions', []))} INSERT, 2 UPDATE", "`trello/data.json` `/actions`, `/cards`, `/boards`", f"`688c4d14c312a27fa2747e5b`, `68c5a46ae3d49c189461e868` on card `{B['trello_kickoff']}`", "action id = 8 hex of the Unix second + 16 hex; `commentCard` data shape with `text`, `textData`, `card`, `board`, `list`"),
    ("contacts.contacts", len(by_table.get("contacts.contacts", [])), "`contacts/contacts.json` `/contacts`", "`fc22d5941b2aeb5c03ad32fa`, `175c0d7bc72ed244b944cb90`", "24 hex id; sparse row (job, email); `last_name` NOT NULL"),
]) + f"""

Column authority: `references/universe_schema_live.json` (NOT NULL columns of every table above are written; no generated column is written). Row shapes for Drive, Docs, Sheets, Slides, Calendar, Gmail, Trello and Contacts follow the accepted injection of `task_inputs-uselater/01_Universe_Inject.sql` and the base samples above; Linear and Slack shapes are the generator's, checked on the rendered bytes (`render.py`: grammar, parse-back, column types, overlay, invariants, sql_lint: 0 problems).

## 1.B Entity table

""" + table(["Entity", "Canonical spelling", "Where it appears (ids)", "Verdict"], [
    ("Julia Lawson (persona)", "Julia Lawson · julia.lawson@harmonygames.co", f"Slack `EMPLOYEE_0005_SLACK_ID`; Linear `usr_8140f09bf9f1b94c` (member of team_ART, team_DES, team_ENG, team_ZOM); Drive root `{B['julia_root']}`; Contacts `8140f09bf9f1b94cb8ee2dd7`", "AGREE"),
    ("Frederick Stone", "Frederick Stone · frederick.stone@harmonygames.co", f"Slack `EMPLOYEE_0008_SLACK_ID`; Linear `usr_175c0d7bc72ed244` (team_ART and team_ENG, not team_DES: he opens no ticket in this task); Drive root `d_175c0d7bc72ed244b944cb`; DM `{M.DM_FRED}`", "AGREE; card SC-49 (founder status) not stated in any seeded text"),
    ("Brian Foster", "Brian Foster · brian.foster@harmonygames.co", f"Slack `EMPLOYEE_0026_SLACK_ID`; Linear `usr_fc22d5941b2aeb5c` (member of team_DES and team_ZOM; creator of `DES-304` to `DES-312` and of `ZOM-521`, `ZOM-566`); Drive root `d_fc22d5941b2aeb5c03ad32`; Contacts `fc22d5941b2aeb5c03ad32fa`", "AGREE"),
    ("Robert", "Robert · robert@harmonygames.co", f"Slack `EMPLOYEE_0016_SLACK_ID`; Linear `usr_Robert` (hazard I10); Contacts `5f647df33ba6e92fbd56b05b`", "AGREE; no surname in any service"),
    ("Claire Morgan", "Claire Morgan · claire.morgan@harmonygames.co", f"Slack `EMPLOYEE_0009_SLACK_ID`; Linear `usr_7fe31e7ec8199618`; DM with Julia `{M.DM_CLAIRE}`; GitHub author of `{B['pr462']}`", "AGREE; a GitHub-only login 'Claire' also exists: Brian's notes say 'Claire', who on this game's art is Claire Morgan (fact_check warning, dispositioned in the Self-review)"),
    ("Marcus Bennett", "Marcus Bennett · marcus.bennett@harmonygames.co", f"Slack `EMPLOYEE_0002_SLACK_ID`; Linear `usr_c77c50cc15c5342d`; base post `{B['anim_pack']}`", "AGREE; two other Marcuses exist on the roster and post nowhere in this task"),
    ("Calvin Price", "Calvin Price · calvin.price@harmonygames.co", f"Slack `EMPLOYEE_0006_SLACK_ID`; Drive root `d_49b9dfa5208d400d9b3937`; Contacts `49b9dfa5208d400d9b3937ca`; base `{B['sfx_scale']}`", "AGREE"),
    ("Leonard Hayes", "Leonard Hayes · leonard.hayes@harmonygames.co", f"Trello `PERSON_6094_TRELLO_USER_ID` (creator of card `{B['trello_kickoff']}`)", "AGREE"),
    ("Martin Walsh", "Martin Walsh · martin.walsh@harmonygames.co", f"named once, on the Fonts ticket {tick('Fonts')}; Linear `usr_51f5f16d46e8cf55`", "AGREE; a 'Martin Lewis' exists outside the studio and is not meant (fact_check warning, dispositioned)"),
    ("PlayableX", "PlayableX (the vendor)", f"Slack channel `{M.VENDOR_CH}`; staff `PERSON_6078_SLACK_ID`; masked in mail and calendar titles", "DISAGREE (pre-existing, uneven masking): seeded text uses the Slack spelling; documented"),
    ("PlayableX intake", f"{TXT.CONTACT['email']}", f"Contacts `{S['contact']['id']}` (seeded); no base row for the vendor (lookup, 0 hits for the address)", "new role address; duplicates nobody"),
    ("The pack ticket", f"{PT} 'Playable pack for PlayableX'", f"Linear `{PT}` and children {TICKS} (seeded), in the Design team; base highest there is `DES-312` (7 May 2025)", "AGREE; fourteen base tickets under `ZOM-97` share a title with a child (T19): the pack list's Ticket column and the team disambiguate"),
    ("match3d#462", "Objects Revisions and Changes", f"GitHub `{B['pr462']}`, comment `{B['pr462_comment']}`; Slack `{B['art_claire_pr']}`, `{B['robert_new_colours']}`", "AGREE (base, not modified)"),
    ("The design page", "ZM3D GDD", f"Confluence `{B['gdd']}` with comments `{B['gdd_c1']}`, `{B['gdd_c2']}`", "AGREE; cards SC-8, SC-38, SC-58 concern other sentences of the page"),
]))

# ------------------------------------------------------------------ 1.C voice
ACT = "active_sep_2025_quiet_in_oct"
P.append(f"""## 1.C Voice and realism (seeded speakers)

Seeded speakers and their `status_at_clock` (from `references/universe_kb/by_universe/synthcut/activity.json`, verified at the freeze):

- Frederick Stone <frederick.stone@harmonygames.co> (`EMPLOYEE_0008_SLACK_ID`): activity.json status {ACT}. Seeded: the ask (Slack), the notes (Docs), the hold (Calendar) and its invitation mails, the contact.
- Brian Foster <brian.foster@harmonygames.co> (`EMPLOYEE_0026_SLACK_ID`): activity.json status {ACT}. Seeded: the pack ticket, its children and the note on each (Linear), the pack list (Sheets), his log (Docs).
- Robert <robert@harmonygames.co> (`EMPLOYEE_0016_SLACK_ID`): activity.json status {ACT}. Seeded: three Slack messages.
- Claire Morgan <claire.morgan@harmonygames.co> (`EMPLOYEE_0009_SLACK_ID`): activity.json status {ACT}. Seeded: one DM to Julia.
- Marcus Bennett <marcus.bennett@harmonygames.co> (`EMPLOYEE_0002_SLACK_ID`): activity.json status {ACT}. Seeded: one post in #zombie-match3d.
- Calvin Price <calvin.price@harmonygames.co> (`EMPLOYEE_0006_SLACK_ID`): activity.json status {ACT}. Seeded: the sound sources sheet.
- Leonard Hayes <leonard.hayes@harmonygames.co>: activity.json status {ACT}. Seeded: one Trello comment.
- Julia Lawson <julia.lawson@harmonygames.co> (`EMPLOYEE_0005_SLACK_ID`): activity.json status {ACT}. Seeded: her deck (Slides), 23 Sep.

Voice, from base quotes (verbatim, with the export's own capitals):

""" + table(["Author", "Base quotes (ids)", "Length, style, hours (UTC)", "Seeded text follows it by"], [
    ("Frederick", f"'Do you think it's fair to ask him to mock up screenshots he thinks could outperform our current set?' (`{M.DM_FRED}/1756232330.990849`); 'lets go with Scenario 1. From a design standpoint, I think the main elements to figure out are 1) what items are on the board, and 2) what zombies are being smashed.' (`{B['fred_scenario1']}`); 'we are considering a pretty substantial pivot in core game play for Zombie Match.' (`{B['fred_pause']}`)", "full sentences, American English, opens with the name; posts 13 to 23 UTC; his last base DM to Julia is 18 Sep", "the ask is one paragraph of full sentences, sent 18:21 UTC after the call that fills 17:30 to 18:09 on his calendar (`evt_2204ffea306847eea6e5b0`); the notes and the hold are stamped before it"),
    ("Brian", f"'Since our zombies are made with 2D Unity animations, I’ve included the PSD files along with the animation and prefab files.' (`{B['brian_zip1']}`); 'Sorry, it took a little while, I had to get help from our animator' (`{B['brian_pack3']}`); 'Makes sense, I sent them the assets, but as far as I know, they haven’t started yet' (`{B['brian_sent']}`)", "short plain English in channels; active 06 to 21 UTC; Turkish in DMs", "ticket notes of one to three short sentences; the log and the pack ticket's description in the same plain register; no note is in a DM"),
    ("Robert", f"'Let's also get a colorized versions of the cone:' (`{B['art_cone']}`); 'Got new colored version of cactus, chainsaw and cones that can probably come in handy:' (`{B['robert_new_colours']}`); 'I think we should remain as is' (`{B['robert_remain']}`)", "one or two casual sentences, sentence case; posts 14 to 07 UTC, none 09 to 12", "three short posts at 18:12, 21:41 and 17:31 UTC, each in a gap of his base traffic (re-check B3); in rev2 one note in his DM with Julia at 20:38 UTC on 29 Sep, before his base messages of 20:55 and 21:21, lower case, people tagged"),
    ("Claire", f"'Daha texture'lar final değil ama senin seti hazırlıyorum' (`{M.DM_CLAIRE}/1758555266.534569`); 'Kuzum yaparım tabi, pazartesi onu eklerim' (`{M.DM_CLAIRE}/1758300559.154229`); 'aa o da güzel fikirmiş bak aşlskdaşlkds' (`{M.DM_CLAIRE}/1758732588.831919`)", "Turkish with English nouns, lower case, 'kuzum'; 06 to 18 UTC; English in channels", "no seeded text in rev2 (the rev1 Turkish message is removed); she is tagged in Robert's note and in Marcus's post, and named in Brian's notes and log"),
    ("Marcus", f"'yah alright i can export them zombies!' (`{M.ANIM_CH}/1758883570.104439`); 'i've included packages, an instalation text with what you need to do. and a video on how to play the animations. I've tested it in an empty project myself' (`{B['anim_pack']}`); 'the fbx export seetings need to be set on meters.' (`{B['marcus_fbx_settings']}`)", "lower case, loose spelling, no apostrophes; 97 % of posts 08 to 17 UTC", "one lower-case post without apostrophes at 17:08 UTC, fifteen minutes after his pack post of 16:53"),
    ("Leonard", f"'For the playable - should we pause the effort if they haven’t started yet?' (`{B['leonard_pause_q']}`); 'I’m worried that we pivot the core game and then playable dev money will be wasted.' (`{M.DESIGN_CH}/1759114127.213749`)", "short, direct; 14 to 07 UTC", "a three-sentence Trello comment at 20:05 UTC"),
    ("Calvin", f"'I used the sample you gave me and increased and lower the pitch, would you need more or 10 are okay?' (`{B['sfx_scale']}`); 'can you help me vote which soundtrack you think fits better for endless mode?' and, on its next line, 'I'm open for any suggestions, it's AI generated' (`C05KNDCHAAG/1755195783.942099`)", "plain, practical; 13 to 01 UTC", "sheet cells of a few words each"),
]) + f"""

Conventions used (`references/universe_kb/by_universe/synthcut/conventions.json`): `slack.per_person_hours_and_style` and `slack.length_chars_by_channel_type` for message length and hours; `linear.title_prefixes_by_team` (Design-team titles carry no prefix in 238 of 247 cases, and Brian's own `DES-311` and `DES-312` are titled 'Chapter 14' and 'Chapter 15' under a parent: the children are titled with the line's name, as the object tickets under `{B['zom97']}` are); `linear.priority_by_team` (priority 0, as on Brian's own Design tickets `DES-304` to `DES-312`); `gcal.duration_min` (30 minutes) and `gcal.summary_patterns_top`; `gmail.subject_patterns_top` ('Invitation: … @ …'). Ticket notes carry jittered seconds; no seeded time falls on a round minute by rule.
""")

# ------------------------------------------------------------------ 1.D keyword
P.append("## 1.D Keyword\n\nBase sweep of the seeded wording (`plan/literal_sweep.py`, eleven services, `tools/hg.py search-many`; output kept in `Working_Files/plan/out/literal_sweep.txt`). A term with no base hit is new and is reached through an anchor; a term with base hits lists one.\n\n" + table(["Term", "Base", "Seeded in", "Reached via"], [
    ("hand-off notes", "NEW TERM — 0 base hits", f"the ask `{sid('ask')}`, the notes `{S['notes']['id']}`", "anchor A1 (the ask names them); a Docs or Drive search for the words"),
    ("pack list", f"2 unrelated Slack hits of 2024 (e.g. `D0770ET1HV2/1720174256.332539`, about a puzzle pack list) and one pull-request body", f"the ask, the sheet `{S['tracker']['id']}` titled 'ZM3D playable - pack list'", "anchor A1; a Drive search for 'pack list'"),
    ("playable pack", "NEW TERM — 0 base hits", f"the pack ticket {PT}", "the pack list's Ticket column; the notes ('Brian's pack ticket')"),
    ("8-item", f"1 base hit, the vendor's own message `{B['vendor_formats']}`", f"Robert's post `{sid('picks')}` ('the 8')", "a search for the playable in #zombie-design"),
    ("the text kind", f"1 unrelated base hit in a DM of May 2025 (`D07G5QWT20K`)", f"Marcus's post `{sid('a1_post')}`", "reading #zombie-match3d `C0880U9751A` for the week"),
    ("redoing the UVs", "NEW TERM — 0 base hits", f"Robert's note `{sid('a2_dm')}`", f"reading Julia's DM with Robert `{M.DM_ROBERT}` around 29 Sep; a Slack search for 'bathroom' also returns it among 57 visible base messages (no rev1 run searched the word)"),
    ("three recoloured models", "NEW TERM — 0 base hits", f"Brian's log `{S['c4_log']['id']}`", "a Drive or Docs search for the outgoing folder; which three is in Robert's base post"),
    (".wav exports", "NEW TERM — 0 base hits", f"Brian's log `{S['c4_log']['id']}`", "the same log (rev1's 'The sound files.' made a search for 'sound' list it)"),
    ("in place of the last one on my list", "NEW TERM — 0 base hits", f"Robert's reply `{sid('c3_reply')}`", f"`slack_read_thread` on Julia's bow post `{B['art_bow_root']}`"),
    ("won't unpack", "NEW TERM — 0 base hits", f"Brian's log `{S['c4_log']['id']}`", "a Drive or Docs search for the outgoing folder"),
    ("outgoing folder", "NEW TERM — 0 base hits", f"every exported line's note ({TICKS}), the notes, Brian's log", "the ticket notes; the notes' Ready test"),
    ("sound sources", "NEW TERM — 0 base hits", f"Calvin's sheet `{S['c2_sheet']['id']}`", "a Drive or Sheets search for sound"),
    ("intake@", "NEW TERM — 0 base hits", f"the contact `{S['contact']['id']}`", "the notes name Contacts"),
    ("kickoff", f"base card `{B['trello_kickoff']}` 'Playable Kickoff'", f"the hold `{S['hold']['id']}`, Leonard's comment `{S['trello_note']['id']}`", "the notes name the kickoff hold; a calendar search for the playable or for 3 Nov"),
]))

# ------------------------------------------------------------------ 1.E persona reach
P.append("## 1.E Persona reach\n\n`persona_view.py check-sql julia_lawson 01_Universe_Inject.sql --load-bearing Working_Files/01c_load_bearing_ids.txt` (verbatim):\n\n" + code(read(OUT / "check_sql.txt")) + "\n\nReach path per scoped load-bearing record:\n\n" + table(["Record", "Service class", "Visibility path"], [
    (f"`{S['ask']['id']}` LB", "Slack DM", f"Julia is one of the two members of `{M.DM_FRED}`"),
    (f"`{S['a2_dm']['id']}` LB", "Slack DM", f"Julia is one of the two members of `{M.DM_ROBERT}`"),
    (f"`{S['picks']['id']}` LB, `{S['zpicks']['id']}` LB", "Slack public channel", f"member of #zombie-design `{M.DESIGN_CH}`"),
    (f"`{S['c3_reply']['id']}` LB", "Slack public channel, thread reply", f"member of #zombie-art `{M.ART_CH}`; the parent `{B['art_bow_root']}` is her own post"),
    (f"`{S['a1_post']['id']}` LB", "Slack private channel", f"member of #zombie-match3d `{M.MATCH3D_CH}` (can-see YES; six posts of hers that week)"),
    (f"`{S['notes']['id']}` LB, `{S['tracker']['id']}` LB, `{S['c2_sheet']['id']}` LB, `{S['c4_log']['id']}` LB", "Drive files", "shared with julia.lawson@harmonygames.co as reader (`shared_with_emails_json`)"),
    (f"`{S['deck']['id']}` LB", "Drive file", "owned by Julia"),
    (f"`{S['hold']['id']}` LB", "Calendar", "the copy on Julia's calendar, `self:true`"),
    (f"`{ids['invites'][JULIA]['message']}`", "Gmail", "her own mailbox copy, INBOX (a companion, not load-bearing)"),
    (f"`{M.VENDOR_CH}` LB (base hub channel)", "Slack private channel", "member (can-see YES)"),
]) + f"\n\nUnscoped services (always visible to the persona): Linear ({PT} and its children), Trello (`{S['trello_note']['id']}`), Contacts (`{S['contact']['id']}`), GitHub (`{B['pr462']}`), Confluence (`{B['gdd']}`). The four NO rows of the check are the invitation copies in Brian's and Robert's mailboxes: companions of the hold, not evidence. No designed denial and no UNVERIFIED record is load-bearing.")

# ------------------------------------------------------------------ 1.F collision
P.append("## 1.F Collision\n\nIdentity tokens: no new person is created; the one new contact is a role address with no Slack, Linear or Gmail identity, and no masking token is used in any seeded text. Minted ids against the full collections (`plan/check_ids.py`, `tools/hg.py search lookup`, verbatim):\n\n" + code(read(OUT / "check_ids.txt")) + f"\n\nSlack `(channel, ts)` pairs are unique in their channel-month files (generator invariant S3 and the lookup above). Linear: the Design team's highest base number is `DES-312` (created 2025-05-07T19:31:13Z, `conventions.json` linear.max_number); `{PT}` to `{M.LAST_CHILD}` are free and follow it in number and in date. The invitation mails' Message-IDs and thread ids are minted from the hold's key and each mailbox and collide with nothing (`base_check` Check A: PASS).")

# ------------------------------------------------------------------ record ledger
led = [
    (1, "slack", "slack_messages", f"`{S['ask']['id']}`", f"`{M.DM_FRED}`", "anchor A1; fragments K13, K16", "● text", "DM member", "first link (hub)"),
    (2, "gdocs + gdrive", "docs_documents, drive_files", f"`{S['notes']['id']}`", "Frederick's Drive root `d_175c0d7bc72ed244b944cb`", "authority H1; fragment K1", "● body_text", "shared reader", "connecting (the rules)"),
    (3, "gsheets + gdrive", "sheets_spreadsheets, sheets_sheets, drive_files", f"`{S['tracker']['id']}`", "Brian's Drive root `d_fc22d5941b2aeb5c03ad32`", "authority H2; fragment K2; cohort definition", "● grid", "shared reader", "connecting (the line set)"),
    (4, "linear", "linear_issues", f"`{PT}`", "team DES (Design)", "fragment K4 (destination)", "● title, description", "unscoped", "connecting; write target's parent"),
    (5, "linear", "linear_issues", f"`{tick(M.LINES[0]['name'])}` … `{M.LAST_CHILD}` ({n_list})", f"children of {PT}", "cohort (one per line)", "● title, state", "unscoped", "evidence carrier; write targets"),
    (6, "linear", "linear_comments", f"{n_list} notes, one per child (e.g. `{M.comment_id('note_Refrigerator')}` on {tick('Refrigerator')})", "the child tickets", "cohort evidence surface 1; traps T1, T2, T3, T7", "● comment body (Ask_Carriers §6b)", "unscoped", "evidence; claims met first"),
    (7, "slack", "slack_messages", f"`{S['picks']['id']}`", f"#zombie-design `{M.DESIGN_CH}`", "fragment K3; trap T5 (older version)", "● text", "channel member", "connecting; claim met first"),
    (8, "slack", "slack_messages", f"`{S['zpicks']['id']}`", f"#zombie-design `{M.DESIGN_CH}`", "fragment K10", "● text", "channel member", "connecting"),
    (9, "slack", "slack_messages (+ UPDATE of the parent's counters)", f"`{S['c3_reply']['id']}`", f"thread under `{B['art_bow_root']}` in #zombie-art", "fragment K11; chain C4; trap T5 (overturning)", "● thread reply text", "channel member", "overturning"),
    (10, "slack", "slack_messages", f"`{S['a1_post']['id']}`", f"#zombie-match3d `{M.MATCH3D_CH}`", "chain C1; trap T1 (overturning)", "● text", "channel member", "overturning"),
    (11, "slack", "slack_messages", f"`{S['a2_dm']['id']}`", f"`{M.DM_ROBERT}`", "chain C2; trap T2 (overturning)", "● text", "DM member", "overturning"),
    (12, "gsheets + gdrive", "sheets_spreadsheets, sheets_sheets, drive_files", f"`{S['c2_sheet']['id']}`", "Calvin's Drive root `d_49b9dfa5208d400d9b3937`", "chain C5; trap T4 (overturning)", "● grid", "shared reader", "overturning"),
    (13, "gdocs + gdrive", "docs_documents, drive_files", f"`{S['c4_log']['id']}`", "Brian's Drive root `d_fc22d5941b2aeb5c03ad32`", "chain C6; trap T7 (overturning)", "● body_text", "shared reader", "overturning"),
    (14, "gslides + gdrive", "slides_presentations, slides_pages, slides_page_elements, drive_files", f"`{S['deck']['id']}`", f"Julia's Drive root `{B['julia_root']}`", "fragment K9; traps T14, T15 (older state of the board)", "● element text", "owner", "claim met first"),
    (15, "gcal", "gcal_events", f"`{S['hold']['id']}` and three more copies ({', '.join('`' + v + '`' for k, v in ids['events'].items() if k != JULIA)})", "the four attendees' calendars", "authority H3; fragment K7", "● summary, start, attendees", "attendee", "connecting (recipients)"),
    (16, "gmail", "gmail_threads, gmail_messages", f"`{ids['invites'][JULIA]['message']}` and the copies in Brian's and Robert's mailboxes", "three mailboxes", "companion of the hold (INT-11)", "● subject, body", "own mailbox (Julia's copy)", "companion"),
    (17, "contacts", "contacts", f"`{S['contact']['id']}`", "Contacts", "fragment K8", "● email", "unscoped", "connecting (recipient)"),
    (18, "trello", "trello_actions (+ UPDATE of card badges and dateLastActivity, board dateLastActivity)", f"`{S['trello_note']['id']}`", f"card `{B['trello_kickoff']}`", "authority H3's decoy; trap T11", "● comment text", "unscoped", "decoy"),
]
P.append("## Record ledger\n\n" + table(["#", "Service", "Table(s)", "Id", "Container", "Manifest element", "Carrier", "Reach path", "Discovery role"], led) +
         f"\n\nEvery injected row maps to one of the eighteen entries above (`plan/out/sql_ids.json` lists the rows per table); no row exists only to raise a count. The six Slack rows and the {2 * n_list + 1} Linear rows are generated from `Working_Files/spec/spec.json`.")

# ------------------------------------------------------------------ findability
def proof(rec, query, term, competing, pos):
    return f"```\nRecord:               {rec}\nAgent's likely query: {query}\nTerm present:         {term}\nCompeting base hits:  {competing}\nChain position:       {pos}\n```"
P.append("## Findability, discovery order, hidden-authority proofs\n\n" + "\n\n".join([
    proof(f"slack.slack_messages · {S['ask']['id']}", "the DM with Frederick, newest first (slack_read_channel or conversations_history)", "the message is the newest of the DM (last base message 18 Sep)", "0 newer; 36 base messages in the DM since July", "first link"),
    proof(f"gdocs.docs_documents · {S['notes']['id']}", '"hand-off notes" via gdocs_search_documents or gdrive_search', "title 'ZM3D playable: hand-off notes'", "0 (NEW TERM); the decoy 'Playable Feedback' answers a search for 'playable'", "connecting; authority H1"),
    proof(f"gsheets.sheets_spreadsheets · {S['tracker']['id']}", '"pack list" via gdrive_search or gsheets_search_spreadsheets', "title 'ZM3D playable - pack list'", "0 sheets with that title", "connecting; authority H2"),
    proof(f"linear.linear_issues · {PT}", "the Ticket column of the pack list; linear_get_issue, then linear_list_issues(parentId)", "every child key is in the pack list's rows", "the 51 object tickets under ZOM-97 share titles, not keys", "connecting"),
    proof(f"linear.linear_comments · one per child ({TICKS})", "linear_list_comments(issueId) per ticket", "the notes say 'Brian's note on each ticket says what he did with the line'", "base holds no Linear comment at all", "evidence (per line)"),
    proof(f"slack.slack_messages · {S['picks']['id']} and {S['zpicks']['id']}", '"playable" or "PlayableX" in #zombie-design', "both posts carry the word", "the 22 Sep playable thread and Leonard's 29 Sep posts in the same channel", "connecting"),
    proof(f"gcal.gcal_events · {S['hold']['id']}", '"kickoff" via a calendar search, or events on 3 Nov', "summary 'ZM3D playable kickoff with PlayableX'", "more than forty base events have 'Kickoff' in the title (art and feature kickoffs); none is on 3 Nov 2025 and none names the playable or the vendor ('2025-11-03', 'PlayableX', 'playable': 0 hits in the calendar export); the Trello card 'Playable Kickoff' answers the same word in Trello", "connecting; authority H3"),
    proof(f"contacts.contacts · {S['contact']['id']}", '"PlayableX" via a contacts search', "first name 'PlayableX', job 'Project intake (playable ads)'", "no other PlayableX contact", "connecting"),
]) + f"""

**Dynamic-change seeds** (claim met first · overturned by · why met first · why decisive):

""" + table(["Seed", "Claim met first", "Overturned by", "Why the claim is met first", "Why the later record decides"], [
    ("EXPORT", f"Brian's note on twelve tickets, e.g. {tick('Refrigerator')}: FBX saved out of the project, opens, looks right", f"`{S['a1_post']['id']}` (Marcus, 26 Sep 17:08 UTC)", "the note is on the line's own ticket, which every run reads", "the vendor takes binary FBX only (base) and the notes let a later word from someone who knows the file count; the post holds no word of the ask and no line name (path exposure: OFF-PATH)"),
    ("ARTHOLD", f"Brian's note on twelve Bathroom tickets, e.g. {tick('Bathtub')}", f"`{S['a2_dm']['id']}` (Robert, 29 Sep 20:38 UTC)", "same", "someone who follows the art, later, in Julia's DM with him; the artist is tagged, not named (OFF-PATH)"),
    ("REVISED", f"Robert's base post `{B['robert_new_colours']}` (29 Sep 23:44 UTC): new colour versions of the cactus, the chainsaw and the cones, after their 25 Sep files; the notes send a changed file again", f"`{S['c4_log']['id']}` (Brian's log, 30 Sep): Claire sent the three recoloured models again, they open and look right", "the post sits in #zombie-design next to Robert's picks; every rev1 run read it", "the latest record; it says Ready, and only Robert's post says which three (OFF-PATH: the entry names no line)"),
    ("ZIP", f"Brian's note on eight instrument tickets, e.g. {tick('Cello')}: zipped, in the outgoing folder", f"`{S['c4_log']['id']}` (Brian's log, 30 Sep 09:12 UTC)", "same", "his own later statement; the notes make 'sitting in the outgoing folder, it opens' part of Ready (OFF-PATH)"),
    ("AUDIO", f"Brian's note on {tick('Rocket sound')} and {tick('Explosion sound')}: exported .wav, plays", f"`{S['c2_sheet']['id']}` (Calvin's sheet)", "same", "the notes hand over only sound that is ours; the sheet marks both 'no' (OFF-PATH)"),
    ("PICKS", f"`{S['picks']['id']}` (Robert's eight, 25 Sep)", f"`{S['c3_reply']['id']}` (his reply, 26 Sep 21:41 UTC)", "a search for the playable in #zombie-design returns the 25 Sep post", "same person, later; the ask keeps his latest word (OFF-PATH: the reply names no item)"),
]) + f"""

**Hidden authorities.** H1: a search for 'hand-off notes' returns `{S['notes']['id']}`; the decoy is Leonard's 'Playable Feedback' (`{B['playable_feedback_doc']}`), about the first playable. H2: a search for 'pack list' returns `{S['tracker']['id']}`; the decoy is the vendor's asset list `{B['vendor_asset_list']}`, which names groups, not lines. H3: a calendar search for 'kickoff' returns `{S['hold']['id']}` among older events with that word in the title, and it is the only one that names the playable or falls on 3 Nov; the decoy is the Trello card `{B['trello_kickoff']}` with Leonard's comment `{S['trello_note']['id']}`, which has no attendees.

`path_exposure.py check --write` (verbatim):

""" + code(read(OUT / "path_exposure.txt")))

# ------------------------------------------------------------------ self-validation
P.append("## Self-validation table\n\n" + table(["QC category", "Tool-enforced (result)", "Manual (evidence)"], [
    ("Missing Universe Data", "—", f"every needed fact is in a record Julia can open (1.E) and a cataloged tool returns it: `slack_read_channel`, `slack_read_thread`, `linear_list_comments`, `gsheets_values_get`, `gdocs_get_document_text`, `github_get_pull_request_comments`, `gcal` and `contacts` reads; no tool is killed (Friction: none)"),
    ("Temporal Field", "sql_lint 0 errors; base_check Check C PASS; generator invariants L1 to L12, S1 to S11 PASS", f"dates in text agree with the fields: 'Thu 25 Sep', 'Fri 26 Sep', 'Mon 29 Sep' in notes stamped on those days (`plan/out/note_times.json`); the zombie ticket's note (29 Sep 10:21 UTC) follows the vendor's review message `{B['vendor_zombie_ask']}`; Brian's log line of 30 Sep follows the pause `{B['fred_pause']}`; no record cites a later one"),
    ("Cross-service Referential", "base_check Check A PASS (channels, users, issues, calendars, cards, parents resolve)", f"the pack list's Ticket column equals the child keys ({TICKS}); the hold's attendees equal the invitation's guests; Docs, Sheets and Slides sharing equals the Drive rows"),
    ("Quantitative / Reconciliation", "Slack reply counters updated by the generator; Trello badge counts 1 comment", f"the pack list has {n_list} rows and {PT} has {n_list} children; truth counts {C['Delivered']} / {C['Ready']} / {C['Owed']} come from `solver/truth.json`"),
    ("State / Lifecycle", "Linear stamps follow the state (Done ⇔ completed_at; In Progress ⇔ started_at); no comment after a ticket closed", f"Done only on the eight delivered lines, as {PT}'s description says ('A line's ticket closes when PlayableX have the file'); the zombie ticket closes at 10:22 UTC on 29 Sep, after its note"),
    ("Identifier / Format", "sql_lint, hg.py lint id_contract, generator id invariants: 0 problems", "e-mails and ids copied from base (1.B); one naming scheme per service"),
    ("Semantic / Category", "—", f"the pack list's Category is the game's data folder (`Assets/Data/Objects/<Category>` in `harmonygames-Games/match3d`, `research/object_categories.csv`) for all 84 board items; the base master item list and the prefab folders file about ten of them elsewhere, so the notes say to copy Brian's column; the sheet titles say what they hold"),
    ("Other", "hg.py lint grader_language and padding_comment: 0 flags", "no record states a conclusion: notes give where the file came from and whether it opens, never the state; nothing addresses a solver"),
]))

# ------------------------------------------------------------------ integrations
P.append("## Integrations and companions\n\n" + table(["Service", "INT id", "Companion", "Decision (record)"], [
    ("slack", "INT-13, INT-04, INT-22", "Drive-app DMs, Linear-app posts, notification mails", f"none seeded (manifest `integration_exceptions`); the bow post's thread counters are updated with the reply `{S['c3_reply']['id']}`"),
    ("linear", "INT-04, INT-05", "Slack posts, e-mail digests", f"none: {PT} and its children were made outside Slack; digests are aggregate"),
    ("gcal", "INT-11", "invitation mails", f"seeded: four event rows with one `ical_uid` (`{S['hold']['id']}` on Julia's calendar) and one invitation mail per guest mailbox"),
    ("gmail", "INT-11", "the invitation mails", f"seeded as companions only (`{ids['invites'][JULIA]['message']}`)"),
    ("gdrive, gdocs, gsheets, gslides", "INT-13", "Drive rows mirror Docs, Sheets and Slides ids and sharing", f"seeded: one `drive_files` row per file (`{S['notes']['id']}`, `{S['tracker']['id']}`, `{S['c2_sheet']['id']}`, `{S['deck']['id']}`, `{S['c4_log']['id']}`)"),
    ("trello", "INT-21", "none exists", f"trello: none — card `{B['trello_kickoff']}` and its board get the comment's time as dateLastActivity; the badge counts one comment"),
    ("contacts", "—", "none", f"contacts: none — one sparse row `{S['contact']['id']}`"),
]))

# ------------------------------------------------------------------ touched-data census
P.append(f"""## Touched-data census and coherence hazards

Records a correct run opens, beyond the seeded ones: the PlayableX channel `{M.VENDOR_CH}` in full; #zombie-design `{M.DESIGN_CH}` from 22 Sep; #zombie-art `{M.ART_CH}` from 24 Sep with Julia's bow thread `{B['art_bow_root']}`; #zombie-match3d `{M.MATCH3D_CH}` and #zm-animations `{M.ANIM_CH}` for the week; Julia's DMs `{M.DM_FRED}`, `{M.DM_CLAIRE}`, `{M.DM_BRIAN}`; `{B['pr462']}` with its comment; the design page `{B['gdd']}` and its two comments; card `{B['trello_kickoff']}`; `{B['playable_feedback_doc']}`. Hazard ids are from `references/universe_kb/by_universe/synthcut/coherence_hazards.json`; cards from `references/known_data_issues/synthcut.md`.

""" + table(["Category", "Hazard / card", "Where it meets the task (id)", "Disposition"], [
    ("temporal", "hazard T02; card SC-13", f"three start dates in `{M.VENDOR_CH}`", "dated claim sequence, the last stands; the beta date is never cited"),
    ("temporal", "hazard T06", f"card `{B['trello_kickoff']}`", "the SQL moves the card's and the board's dateLastActivity to the comment's time"),
    ("semantic", "hazard S03: none in scope; card SC-58", f"`{B['gdd']}`", "the roster sentence of the page is neither cited nor graded; no label is seeded"),
    ("referential", "hazards R04, R08; cards SC-36, SC-7", f"the hold `{S['hold']['id']}`; channel rosters", "no Slack text carries a document link; the hold is seeded with a copy on every attendee's calendar and its mails; no base invite or roster feeds an answer"),
    ("quantitative", "hazards Q01, Q02, Q03", f"`{B['art_bow_root']}`", "reply_count, reply_users_count and latest_reply are updated with the seeded reply"),
    ("state / lifecycle", "hazards L06: none in scope, L09; cards SC-16, SC-22, SC-15", f"`{B['pr462']}`; open ZOM tickets naming objects (`ZOM-449`, `ZOM-513`, `ZOM-514`)", "the pull request's review state is not used; the objects of SC-16's tickets are not on the list; `ZOM-521` is not cited by any seeded record; new tickets carry no time_in_status value"),
    ("identifier / format", "hazards I01, I02, I10, I15; card SC-50", f"seeded Slack ids; `usr_Robert`; the bot comment `{B['pr462_comment']}`", "ids follow the base schemes; the comment is used for the models it names, never for which account wrote it"),
]) + "\n\nNo State/Lifecycle or Referential hazard record is modified by the SQL, so `hazard_acknowledgements` is empty. The two reviewers' re-check of the planned records against the base found no remaining contradiction (`Working_Files/research/recheck_D2_base.md`: five majors, all fixed before this SQL).")

# ------------------------------------------------------------------ intended disagreements
P.append("## Intended disagreements\n\n" + table(["#", "Claim (dated, by)", "Later record (dated, by)", "Why it is realistic", "What resolves it"], [
    (1, f"twelve notes, 25 Sep, Brian: FBX saved out of the project, opens, looks right ({tick('Refrigerator')})", f"`{S['a1_post']['id']}`, 26 Sep, Marcus: those files are the text kind", "Brian checked in Unity, where the files open; Marcus had just rebuilt the zombie pack after the vendor's complaint", "the vendor takes binary only (`" + B["vendor_formats"] + "`); the notes: a later word from someone who knows the file counts"),
    (2, f"twelve notes, 26 Sep, Brian: FBX from Claire, looks right ({tick('Bathtub')})", f"`{S['a2_dm']['id']}`, 29 Sep, Claire: redoing the bathroom UVs; Friday's files are the old state", "the artist decided on a rework after handing the files over and told the level designer first", "the notes: current version, nobody changing it"),
    (3, f"three notes, 25 Sep 08:05 UTC, Brian ({tick('Cactus Plant')})", f"base `{B['pr462']}`, merged 25 Sep 23:15 UTC", "Robert asked for the changes the night before; the files went to Brian before Claire made them; rev2: Robert shows the new versions on 29 Sep and Brian's log of 30 Sep records the re-send", "the notes: a changed file goes again"),
    (4, f"eight notes, 26 Sep, Brian: zipped with the other instruments, in the outgoing folder ({tick('Cello')})", f"`{S['c4_log']['id']}`, 30 Sep, Brian: that zip will not unpack", "an upload cut off; he noticed after the pause and noted it for himself", "the notes: sitting in the outgoing folder, it opens"),
    (5, f"two notes, 26 Sep, Brian: exported .wav, plays ({tick('Rocket sound')})", f"`{S['c2_sheet']['id']}`, Calvin: from a library seat and a bought pack", "the packer checked the file type, not the source", "the notes: only sound that is ours is handed over"),
    (6, f"`{S['picks']['id']}`, 25 Sep, Robert: the eight, the dynamite last", f"`{S['c3_reply']['id']}`, 26 Sep, Robert: it goes in place of the last one", "a pick changed in passing, in a thread about the item", "the ask: his picks stand unless he has changed them since"),
    (7, f"`{S['deck']['id']}`, 23 Sep, Julia: the reference level has three item types", f"`{S['picks']['id']}`, 25 Sep, Robert: eight for the board", "the reference level was built before the vendor's 8-item set was answered (base `" + B["julia_level"] + "`)", "the notes: the eight on the board; the deck is what was built for them"),
]))

# ------------------------------------------------------------------ constraints for the prompt brief
P.append("## Constraints for the prompt brief\n\n" + table(["Anchor", "May be named (noun phrases only)", "Record"],
    [(a["id"], a["prompt_reference"], f"`{a['locator']}`") for a in man["anchors"]]) + """

Never named in the prompt: where the notes and the pack list live; any ticket key, channel, category or item; the three state words; any count; the deciding records or their places (Marcus's post, Robert's note, the pull request, Calvin's sheet, Robert's reply, Brian's log). Deadlines: none stated to the agent beyond the ask. Deliverable kinds: one Google Doc and one Google Sheet in Julia's Drive; ticket updates and comments; one DM reply; one channel post.""")

# ------------------------------------------------------------------ fact sheet
P.append("## Fact sheet\n\n" + table(["Key", "Value", "Kind", "Home rows / must appear in"],
    [(f["key"], f["value"], f["kind"], ", ".join(f"`{x}`" for x in (f.get("home_ids") or f.get("must_appear_in") or [])[:3]) + (" …" if len(f.get("home_ids") or f.get("must_appear_in") or []) > 3 else "")) for f in man["facts"]]) +
    "\n\n`fact_check.py … --no-leak` (verbatim):\n\n" + code(read(OUT / "fact_check.txt")))

# ------------------------------------------------------------------ facts for the human
def cls_count(c): return len(M.members(c))
fh = [
    (f"`{sid('ask')}` ({S['ask']['id']})", "seeded", "Frederick's ask to Julia, Tue 30 Sep 2025 18:21 UTC: the brief and where the item pack stands; Brian's pack list, Robert's picks, his hand-off notes; both files in her Drive; the count for each state 'here'; both links in the PlayableX channel", "DM member", "anchor (hub)", "no"),
    (f"`{S['notes']['id']}`", "seeded", "Frederick's hand-off notes (30 Sep 16:58 UTC): what the brief covers; the list's columns (Line, Category, Board set, State, What's owed, Who has it, Ticket); Delivered, Ready, Owed; later statements count; changed art goes again; sound that is ours; tickets to Todo with a comment; sharing", "shared reader", "authority", "no"),
    (f"`{S['tracker']['id']}`", "seeded", f"Brian's pack list: {n_list} rows (Line, Kind, Category, Went out, Ticket), last edited 26 Sep 17:25 UTC", "shared reader", "authority (line set)", "no"),
    (f"`{PT}` and `{tick(M.LINES[0]['name'])}` … `{M.LAST_CHILD}`", "seeded", f"the pack ticket and one child per line; Done on the {cls_count('W')} delivered lines, In Progress on the other {n_list - cls_count('W')}; one note by Brian on each child", "unscoped", "evidence; write targets", "no"),
    (f"`{sid('picks')}`", "seeded", f"Robert, 25 Sep 18:12 UTC: the eight ({', '.join(M.PICKS_25SEP)})", "channel member", "claim met first", "no"),
    (f"`{sid('c3_reply')}` under `{B['art_bow_root']}`", "seeded", f"Robert, 26 Sep 21:41 UTC: the bow in the eight in place of the last item of his list, as it is now. The eight become {', '.join(M.DEFAULT_FINAL)}", "channel member", "overturning evidence", "no"),
    (f"`{sid('zpicks')}`", "seeded", f"Robert, 29 Sep 17:31 UTC: one animation, {M.PRIMARY_ANIMATION}; the four zombies {', '.join(M.ZOMBIES)}", "channel member", "evidence", "no"),
    (f"`{sid('a1_post')}`", "seeded", f"Marcus, 26 Sep 17:08 UTC, #zombie-match3d: the models saved out of Unity on Thursday are the text kind; Claire's are fine. Decides {cls_count('A1')} lines: Owed, export again as binary, Brian", "channel member", "overturning evidence", "no"),
    (f"`{sid('a2_dm')}`", "seeded", f"Robert to Julia, 29 Sep 20:38 UTC, in their DM: Claire (tagged) is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version. Decides {cls_count('A2')} lines: Owed, Claire (the file came from her)", "DM member", "overturning evidence", "no"),
    (f"`{B['pr462']}` and `{B['pr462_comment']}`", "base", "'Objects Revisions and Changes', created 2025-09-25T11:43:06Z, merged 23:15:41Z; the comment names the chainsaw, cactus and cone models (and Candy, Dart Board, Kettlebell, which are not lines). Decides 3 lines: Owed", "unscoped", "overturning evidence", "yes, if GitHub is regenerated"),
    (f"`{S['c2_sheet']['id']}`", "seeded", f"Calvin's sound sources: Rocket sound (Soundly library seat) and Explosion sound (bought pack) are 'no' under 'OK outside the game', 'not made yet, Calvin' under 'Replacement'. Decides {cls_count('C2')} lines: Owed, Calvin", "shared reader", "overturning evidence", "no"),
    (f"`{S['c4_log']['id']}`", "seeded", f"Brian's log of the outgoing folder, 30 Sep 09:12 UTC: the zip with Friday's music instruments will not unpack and the eight are not in the folder any other way. Decides {cls_count('C4')} lines: Owed, Brian", "shared reader", "overturning evidence", "no"),
    (f"`{S['deck']['id']}`", "seeded", "Julia's deck of the reference level (23 Sep): grenade, couch, couch and pillow, the two plushies; win and lose as told to the vendor", "owner", "claim met first (older state)", "no"),
    (f"`{S['hold']['id']}`", "seeded", "kickoff hold, Mon 3 Nov 2025 17:00 to 17:30 UTC (09:00 PST); attendees Frederick, Julia, Brian, Robert", "attendee", "authority (recipients)", "no"),
    (f"`{S['contact']['id']}`", "seeded", f"PlayableX intake: {TXT.CONTACT['email']}", "unscoped", "evidence (recipient)", "no"),
    (f"`{S['trello_note']['id']}` on `{B['trello_kickoff']}`", "seeded", "Leonard, 30 Sep 20:05 UTC: parked until 3 Nov, the start PlayableX gave after we asked for the pause; Julia is pulling the brief and the pack status together for Frederick", "unscoped", "decoy", "no"),
    (f"`{B['vendor_formats']}`, `{B['vendor_asset_list']}`", "base", "the vendor takes .fbx in binary format only, .glb or .blend; the 8-item set; editable extra items", "channel member", "evidence (format rule)", "no"),
    (f"`{B['vendor_nov3']}`", "base", "new start 3 November", "channel member", "evidence", "no"),
    (f"`{B['gdd']}`", "base", "7-slot tray; a level is lost only at zero health", "unscoped", "evidence", "yes, Confluence is regenerated"),
    (f"`{B['fred_retention']}`, `{B['fred_scenario1']}`", "base", "Scenario 1: filters for players who will like the game, true to the core game play; chosen 15 Sep", "channel member", "evidence", "no"),
    (f"`{B['vendor_music_rule']}`", "base", "music starts after the first click (14 Apr, first playable)", "channel member", "evidence", "no"),
]
P.append("## Facts for the human\n\nTotals from `solver/truth.json`: " + f"{C['Delivered']} Delivered, {C['Ready']} Ready, {C['Owed']} Owed of {len(M.LINES)} lines; {len(M.OWED_WITH_TICKET)} Owed lines have a ticket (to Todo with a comment); without the six deciding records a reader gets {M.NAIVE['Delivered']} / {M.NAIVE['Ready']} / {M.NAIVE['Owed']}. Owed by reason: {cls_count('VIS')} on their own note, {cls_count('A1')} text-kind files, {cls_count('A2')} bathroom, {cls_count('C4')} in the broken zip, {cls_count('C2')} sound cues; the {cls_count('C1')} recoloured lines are Ready (sent again, Brian's log).\n\n" +
         table(["Locator", "Base / seeded", "Fact (values, actors, UTC)", "Reach path", "Role", "Re-verify?"], fh))

# ------------------------------------------------------------------ platform follow-ups
P.append(f"""## Platform follow-ups

- Pre-check: confirm that `linear_list_comments` returns Brian's notes and that `linear_show_data` and the `query` parameter of `linear_list_issues` do not return comment bodies in bulk (both are unverified in `Ask_Carriers.md`); confirm the counted calls of the run are above 150.
- Pre-check: note whether the run looks in Drive for the outgoing folder (the route to Brian's log, which decides eleven lines: the eight zipped instruments and the three recoloured items); no route through GitHub is relied on in rev2.
- Confluence (`{B['gdd']}`) is being regenerated: re-verify the 7-slot tray and the zero-health sentence before the rubric is written.
- Rubric: accept the two links in the PlayableX channel as a top-level post or as a reply in the pause thread (both are 'in the channel'); accept the counts in Frederick's DM as a message or a thread reply.
- Rubric: do not grade what a full tray does in the playable. Base holds two statements (the design page `page_zm3d_gdd`; Frederick's 23 Sep remark `C2637A3385F7/1758656830.965739` in a group chat whose roster does not list Julia), and the page's Modes section scores one mode 'before the tray fills'. Tray size (7) and the loss rule (zero health) are stated consistently and are the graded facts.
- Pre-check: note whether the run can open the group chat `C2637A3385F7`; nothing graded depends on it.
- No ○ carrier is load-bearing: nothing sits in a calendar description, slide notes, a Drive `content_text` or a Slack file.
- The injection-stage forecast is computed on the 24 solver-readable slots only (list cells and totals); the 29 slots graded from written text are outside the solver. It is recorded as such (Self-review).""")

# ------------------------------------------------------------------ self-review
LINTC = lint["counts"]
P.append("## Self-review\n\n**Tool outputs, verbatim.**\n\n`sql_lint.py`:\n\n" + code(read(OUT / "sql_lint.txt")) +
    "\n\n`base_check.py`:\n\n" + code(read(OUT / "base_check.txt")) + "\n\n`base_claims.py`:\n\n" + code(read(OUT / "base_claims.txt")) +
    "\n\n`hardness_gate.py` on the final manifest and the SQL:\n\n" + code(read(OUT / "hardness_gate_final.txt")) +
    "\n\n`oracle_kit.py check`:\n\n" + code(read(OUT / "oracle_check.txt")) +
    "\n\n`plan/citation_chronology.py` (times read from the SQL; every record against the record it names or answers):\n\n" + code(read(OUT / "citation_chronology.txt")) +
    "\n\n`difficulty_mutation.py mutate` (rules, degrades, geometry):\n\n" + code("\n".join(l for l in read(OUT / "mutation.txt").splitlines() if not l.strip().startswith("shards")) ) +
    "\n\n`preflight_report.py` (the empty list of missing liveness dispositions is printed here as `none`):\n\n" + code(read(OUT / "preflight.txt").replace("'liveness_dispositions_missing': []", "'liveness_dispositions_missing': none")) + f"""

**Warning dispositions.**
- sql_lint warning, clock class (8 lines, the hold's `start_ts` and `end_ts` after the clock): disposition — allowed, a not-yet-happened event: the kickoff on 3 Nov 2025 is the vendor's own new start date (`{B['vendor_nov3']}`); the event's `created` and `updated` are 30 Sep 16:41 UTC, before the seed bound and before the last edit of the notes that name it (16:58 UTC).
- fact_check warnings (ambiguous first names 'Claire', 'Marcus', 'Martin' in Brian's ticket notes): disposition — kept as a colleague writes them; on this game they are Claire Morgan, Marcus Bennett and Martin Walsh (1.B), no graded value depends on a full name, and 'Who has it' is compared on the first name.
- `hg.py lint` (the eval's `hg_injection_lint.py`, with base data): FAIL {LINTC['FAIL']}, CHECK {LINTC['CHECK']}, INFO {LINTC['INFO']} on sha256 `{lint['sha256'][:12]}`; no LINT line needs a disposition.
- Mutation: three over-application operators are WEAK (their control line is not a sampled row); each has a written disposition in `01c_Dispositions.json`. REVISED's operator (Fly Zapper called Ready) is KILLED on the sampled control C2. Geometry: U and L_max as printed above.

**Forecasts (advisory, UNCALIBRATED, pre-registered).** Four figures, which measure different things; none is a measurement. (1) Design stage, `{FC_DESIGN_ID}`, on declared attributions for every slot and the ledger's family priors (which now include the seven rev1 runs): {FC_DESIGN}. Its completion_elsewhere prior still holds the rev1 runs that found Brian's log through the search for 'sound', which rev2 removes, so it is pessimistic for this revision. (2) Injection stage, this SQL (`{FC_INJ_ID}`, block below): the tool evaluates only the slots the solver can compute (list cells and totals); the slots graded from written text (reasons, ticket comments, the brief, the reply, the shares) count as always passing, so its averages are upper bounds and its P(all gates) near zero says only that list cells alone would not bring the average under 70 %. A first injection forecast of this revision (`hev_b59c9f65ca1510cb`) ran on the SQL before the log stopped naming the chainsaw and the cone (path exposure) and is superseded by the one below. (3) The difficulty budget on the rubric skeleton, with find rates measured in the rev1 runs (`plan/out/policy_scores.txt`): {FC_BUDGET}. (4) The MODE B simulation of rev1 habits (`hardening_gen/simulate.py`): E[average] 0.47 to 0.61 for these four changes. The next pre-check is the first measurement of rev2.

""" + code("\n".join(l for l in read(OUT / "forecast_injection.txt").replace(", 'rejected': []", "").splitlines() if "shard" not in l and "batches" not in l and "slip " not in l)) + f"""

**Checks A to C walk** (`Evals/0_Injection_Quality_Eval.md`).
- Inventory: {sum(1 for x in rows if x['op'] == 'insert')} INSERT and {sum(1 for x in rows if x['op'] == 'update')} UPDATE, no DELETE, no upsert; statements grouped by service inside one BEGIN/COMMIT. PASS.
- Check A (references, uniqueness, identities, id contracts): every channel, user, team, parent ticket, calendar, card, board and mailbox exists in base (`base_check` Check A PASS); every minted id is absent from the full collections (1.F); one account per person per service; Drive files have a Docs, Sheets or Slides row with content. PASS.
- Check B (structure, literal JSON, generated and NOT NULL columns): literal values only; every `*_json` value is valid JSON; `text_fts` and `body_text_fts` are never written; Linear text dates are `YYYY-MM-DDTHH:MM:SSZ` (`hg.py lint` text_time_format: 0). PASS.
- Check C (dates, parent and reply, statuses, counts, claimed updates): every created, sent or updated value is before {ctx['freeze_utc']}; the reply is after its base parent `{B['art_bow_root']}`; comments follow their tickets and precede the close of the eight Done tickets; the hold's start is a plan field. PASS.
- Grader-facing or padding text: none (lint 0); every record has a task purpose (record ledger).

**Touched-data census:** the section above; each hazard category and card has its disposition.

**Counter-readings** (category · the best case that it fails · evidence that resolves it · verdict):

""" + table(["Category", "Counter-reading", "Resolution (evidence)", "Verdict"], [
    ("Temporal", "Brian's notes of 26 Sep say 'FBX from Claire' on days base shows no file transfer in their DM.", f"base neither shows nor contradicts hand-overs after 24 Sep (re-check: `D076Y0SDV18` ends 24 Sep 12:29 UTC); Claire offered to send whatever is asked (`D076Y0SDV18/1758712890.403889`)", "holds"),
    ("Temporal", "The zombie ticket's note mentions the vendor's review, which is of 29 Sep, on a ticket created 25 Sep.", f"the note is stamped 29 Sep 10:21 UTC, after `{B['vendor_zombie_ask']}` (10:16 UTC), and the ticket closes a minute later", "holds"),
    ("Semantic / Category", "'Category' on the list could be read as Brian's own grouping.", "all 84 board items carry the category of the game's data folders (`research/object_categories.csv`); Bathroom, Kitchen and Garden agree in every base source (both reviewers checked), so 'banyo objeleri' maps to the thirteen Bathroom rows, and the notes say Category is copied from Brian's list", "holds"),
    ("Cross-service Referential", "The pack list and the tickets could disagree on a line.", f"both come from one model; `sql_ids.json` and the solver's `listed` read the grid back; {n_list} rows, {n_list} children", "holds"),
    ("Quantitative", f"{C['Delivered']} / {C['Ready']} / {C['Owed']} could move on a line whose note is unclear.", "every note states source and that the file opens, or that it is not exported (`plan/design_model.py` NOTE, VIS_NOTE); two cold reviews of the wording found one fork (the instruments), closed in the notes and the log", "holds"),
    ("State / Lifecycle", "In Progress tickets with files in the outgoing folder look unfinished or inconsistent.", f"{PT}'s description: a line's ticket closes when PlayableX have the file; only the eight delivered lines are Done", "holds"),
    ("Identifier / Format", "97 new keys could sit out of order against the team's base tickets (in ZOM they sat above `ZOM-566`, created five days later; both reviewers flagged it).", "moved to the Design team: its last base ticket is `DES-312` (2025-05-07T19:31:13Z), so `DES-313` to `DES-409`, created 25 Sep, follow in number and in date; Brian's own last tickets there are a parent with bare-titled children (`DES-307`)", "fixed in data"),
    ("People status", "Someone the rules depend on is not active at the clock.", f"all eight seeded speakers are {ACT} in activity.json (1.C); no rule depends on anyone having left", "holds"),
    ("Other", "The designed disagreements read as two silent system fields.", "each is a dated note by a named person against a later dated statement by a named person (Intended disagreements 1 to 7)", "holds"),
    ("Disagreement 1 (EXPORT)", "Brian's 'opens, looks right' and Marcus's 'text kind' are a plain contradiction in seeded data.", f"both are true: the files open in Unity and in Max (the post says so) and are ASCII; the vendor's rule `{B['vendor_formats']}` makes the second matter", "designed, resolved"),
    ("Disagreement 2 (ARTHOLD)", "Robert passing on Claire's rework, rather than Claire herself, is unnatural.", f"Robert follows the art (his colourised items and new colour versions are base) and talks with Julia daily in `{M.DM_ROBERT}`; he tells her because the old versions show in her levels (`{S['a2_dm']['id']}`)", "designed, resolved"),
    ("Disagreement 3 (REVISED)", "Robert's new colour versions and the log's 'replace Thursday's' could be about different files.", f"Robert's post names the cactus, the chainsaw and the cones (`{B['robert_new_colours']}`); the Thursday files from Claire of those three are the only Thursday files with a later change; the log entry is the next day and the latest record", "designed, resolved"),
    ("Disagreement 4 (ZIP)", "Brian's log contradicts his own ticket notes without him fixing the tickets.", f"the log line is of 30 Sep, the morning after the pause (`{B['fred_pause']}`); he writes that he will put the files back when the work resumes", "designed, resolved"),
    ("Disagreement 5 (AUDIO)", "A sound that 'plays' and is 'not ours' is an unintended inconsistency.", f"file type and source are different facts; base already has two sounds to be swapped for rights (`{B['robert_copyright']}`)", "designed, resolved"),
    ("Disagreement 6 (PICKS)", "'The last one on my list' could point at another list.", f"Robert has one list of picks, his post `{S['picks']['id']}` of the day before in the channel where the playable is discussed; its last item is the dynamite, and 'things that go boom' fits it", "designed, resolved"),
    ("Disagreement 7 (deck)", "The deck's three item types contradict the eight.", f"the deck is dated 23 Sep and titled as the reference level; base says that level was grenade, couch, plushie (`{B['julia_level']}`); the eight answer the vendor's 8-item set two days later", "designed, resolved"),
]) + f"""

**Coherence sweep** (`coherence_sweep.py`; record `Working_Files/01d_Coherence_Sweep.json`; two cold reviewers who saw only the ask and the injected records):

""" + code(read(OUT / "sweep_check.txt") if (OUT / "sweep_check.txt").exists() else "pending") + "\n\nrev2 round (this SQL): two new cold reviewers, who saw only the ask and the rev2 records, reviewed the SQL bound above; " + SWEEP_SUMMARY + " Rounds 1 to 5 reviewed rev1 (their briefs and findings are kept in `Working_Files/local_reviews/coherence/round1/` to `round5/`): both rev1 reviewers reached Delivered 8, Ready 36, Owed 52 and every material fork was settled in data before rev1 was submitted. What is left is base-only and is not graded: the design page's roster and its two statements on a full tray, and a remark in a group chat the persona's roster does not open (Platform follow-ups).\n\nForks, and what settled each (from the record):\n\n" + SWEEP_TABLE + f"""

**Re-verified facts.** Read again from their source with `tools/hg.py` in this session: the vendor channel from 15 Sep (formats, dates, the zombie question), Julia's DM with Brian of 23 Sep, Brian's two DMs of 24 Sep, the pull requests #459 to #471 (titles and times), Linear numbering per team and team memberships, the Trello card with its actions, the calendar precedent, the Contacts and Drive root shapes.

Unresolved: none that blocks the injection. Left for the pre-check (Platform follow-ups): the two unverified bulk routes in Linear, the Drive route to Brian's log, and the counted calls of a real run. UNVERIFIED-OK, with no row depending on them: the binary contents of the three base zips and the five masked zombie names.
""")
out = WF / "01_Grounding_Dossier.md"
out.write_text("\n\n".join(P) + "\n")
print("wrote", out.name, len("\n\n".join(P)), "chars")
