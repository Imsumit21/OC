#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md (prep) from the model, the final manifest, the SQL and the pasted
search and entity outputs (plan/brief_search.py). Facts, locators and requirements only; the prompt text is written in
draft mode. Also writes the prompt-writing outcome review into 00_V3_Authoring_Evidence.json. Re-run, then the gate."""
import datetime as D, hashlib, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
OUT = HERE / "out"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TASK.parent / "tools"))
import design_model as M
import planned_texts as TXT

man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
srch = json.loads((OUT / "brief_search.json").read_text())
S, B, PT = M.SEED, M.BASE, M.PACK_TICKET
C = M.COUNTS
JULIA, FRED, BRIAN, ROBERT = "julia.lawson@harmonygames.co", "frederick.stone@harmonygames.co", "brian.foster@harmonygames.co", "robert@harmonygames.co"
INTAKE = TXT.CONTACT["email"]
ROOT = B["julia_root"]
def tk(n): return M.BY_NAME[n]["ticket"]
def table(head, rws): return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rws])
def code(t): return "```\n" + t.rstrip("\n") + "\n```"
def tool_blocks(text):
    """One fence per command: the command as a plain line, then the tool's output starting with its own header line."""
    out, cur, cmd = [], [], None
    def flush():
        body = [l for l in cur if l.strip()]
        if cmd is not None and body: out.append("`" + cmd + "`\n\n" + code("\n".join(body)))
    for line in text.splitlines():
        if line.startswith("$ "):
            flush(); cmd, cur = line[2:], []
        else: cur.append(line)
    flush()
    return "\n\n".join(out)
def pt(iso):
    """UTC stamp -> 'Tue Sep 30, 11:21 AM PT' (PDT, UTC-7, in the task's window)."""
    d = D.datetime.fromisoformat(iso.replace("Z", "+00:00")) - D.timedelta(hours=7)
    return d.strftime("%a %b %-d, %-I:%M %p PT")
sql_sha = hashlib.sha256((TASK / "01_Universe_Inject.sql").read_bytes()).hexdigest()
ASK, NOTES, LIST, DECK, HOLD, CONTACT, TRELLO = (S[k]["id"] for k in ("ask", "notes", "tracker", "deck", "hold", "contact", "trello_note"))
PICKS, ZPICKS, REPLY, A1, A2, LOG, SHEET = (S[k]["id"] for k in ("picks", "zpicks", "c3_reply", "a1_post", "a2_dm", "c4_log", "c2_sheet"))
FIRST, LAST = tk(M.LINES[0]["name"]), M.LAST_CHILD
owed = [l for l in M.LINES if l["state"] == "Owed"]
holders = {}
for l in owed: holders[l["who"]] = holders.get(l["who"], 0) + 1
calls = sum(x["calls"] for x in man["call_budget"])
per_record = sum(x["calls"] for x in man["call_budget"] if x["phase"] == "per-record")
CLOCK = ctx["universe"]["clock_line"].replace("Clock: ", "")

P = [f"""# Prompt Brief — {M.SLUG} · prep
> Built 2026-11-12 from 00_Assigments.md, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (sha256 {sql_sha[:12]}, {M.REV}), 01_Scenario_Design.md, 01_Hardness_Manifest.json, 03_Error_Async_Config.txt (Friction: none). No reference files. Persona view verified: all
> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.
> **Clock:** {CLOCK}. Julia's today is Wed Oct 1, 2025. The latest seeded event is Leonard's Trello comment {TRELLO} (2025-09-30T20:05:47Z, {pt('2025-09-30T20:05:47Z')}). Seed bound {ctx['freeze_utc']}.

## 1 · Assignment fit

Raw assignment: Business Function Product · Persona Julia Lawson, Role: Product Manager · Competency Marketing and GTM · Task Skill Authoring · Task Type long-horizon · Difficulty Mode hard · Universe Date Oct 1, 2025.

""" + table(["Axis", "Assigned value", "What it requires here (cited)"], [
    ("Business function", "Product → Product & Design (`Evals/references/rules/task_categories.md`: product decisions, gameplay and design requirements, art and prototype evaluation)", f"a product call on what the vendor builds from: which eight items sit on the board, which zombies and animation, how a level is won and lost, the tray, what sound may be used; and a product owner's statement of which asset lines are delivered, ready or owed (the rules are Frederick's, in {NOTES})"),
    ("Persona / role", f"Julia Lawson, {JULIA}, Product Manager (roster `julia_lawson`, department Product)", f"Voice: an ordinary colleague request, clean spelling. Remit: she wrote the storyboard and brief for the first playable in the vendor channel on 14 Mar 2025 ({B['julia_dd_brief']}); for this one Brian asked her for the reference level ({B['brian_asks_level']}) and she built it ({B['julia_level']}); the design page names her as the game's designer ({B['gdd']}). Read scope: her DMs with Frederick {M.DM_FRED}, Claire {M.DM_CLAIRE} and Brian {M.DM_BRIAN}; the PlayableX channel {M.VENDOR_CH}, #zombie-design {M.DESIGN_CH}, #zombie-art {M.ART_CH}, #zombie-match3d {M.MATCH3D_CH}, #zm-animations {M.ANIM_CH}; Linear, GitHub, Trello, Contacts and Confluence are unscoped"),
    ("Competency", "Marketing and GTM (taxonomy screen 7: demand and retention, GTM, communications; typical personas include PM; outputs: decks, memos, spreadsheets, emails)", f"a playable ad is a user-acquisition creative; the brief tells the vendor what to build so the ad filters for players who will like the game ({B['fred_retention']}), and the hand-off list is the go-to-market hand-over of its assets. Both outputs are of the listed kinds (a memo-style doc and a spreadsheet)"),
    ("Task skill", "Authoring (taxonomy: produce a deliverable: an email or message, document, slide deck, spreadsheet, or report)", f"two authored artifacts carry the work: the brief (a Google Doc) and the hand-off list (a Google Sheet of {M.N_LIST} rows). Stacked: Retrieval (one note per ticket, the six later statements), Analysis and Synthesis (the three state tests), Actions (ticket moves and comments, shares, two messages)"),
    ("Task type / tier", "long-horizon → Long Horizon 100–500+; requester bar: more than 130 counted calls in every run, corrected average under 70 %", f"11 services carry weight (slack, linear, gsheets, gdocs, gdrive, gslides, gcal, contacts, github, confluence, trello; gmail holds the invitation only). Volumes: {M.N_LIST} pack lines, each with its own ticket and one note ({FIRST} to {LAST}); {len(owed)} ticket moves and {len(owed)} comments; manifest call budget {calls} ({per_record} per-record), `HARDNESS GATE (extreme): PASS` in the dossier with the requester-confirmed volume exception (floor 220)"),
    ("Difficulty mode / date", "hard (cap 70 %); Oct 1, 2025", f"nothing on or after Wed Oct 1 00:00 PT may be described as done; the kickoff on 3 Nov ({HOLD}) is a plan"),
]) + f"""

Remit argument. Frederick runs the vendor relationship (he chose Scenario 1 in {B['fred_scenario1']} and asked for the pause in {B['fred_pause']}) and asks Julia in their own DM ({ASK}) to do for this playable what she did for the first. Nothing asks her to export or fix an asset; the ticket follow-through is moving and commenting tickets in the Design team, of which she is a member (`/team_memberships`).

## 2 · Situation

""" + table(["Symptom (what is visibly wrong)", "Seen by", "Where it shows (locator)", "Relevant records the persona cannot see"], [
    (f"The second playable's start has moved to 3 November and is parked; the vendor has no brief to build from and nobody has said which of the pack's lines PlayableX actually hold", "Julia, as the person Frederick asked", f"Frederick's DM to her {ASK} ({pt(S['ask']['at'])}); the vendor's new start date {B['vendor_nov3']}", f"a group chat of 23 Sep whose roster does not list her (`C2637A3385F7/1758656830.965739`: one remark by Frederick on what a full tray should do in the playable). Nothing graded depends on it"),
    ("Brian's tickets say what he did with each line on the day he did it; nobody has gone back over them", "Julia, reading the pack ticket", f"{PT} and its children {FIRST} to {LAST}; Brian's pack list {LIST}", f"Brian's DMs with the artists (`D076Y0SDV18`, `D07G5QWN3TM`): hand-overs of files; not needed, every line's note is on its ticket"),
]) + f"""

## 3 · Investigation → action

Questions the work has to resolve (no answers here):

1. Which lines make up the pack, and which ticket belongs to each?
2. What did Brian do with each line, and is that still how it stands today?
3. Has anyone who knows a file or the art said something about it since Brian's note?
4. Which formats does PlayableX take, and does every exported file meet them?
5. Which sounds are ours to hand over?
6. Which eight items did Robert pick for the board, and has he changed any since? Which zombies and which animation?
7. What does the brief have to tell the vendor about the scenario, the level's rules, the tray, the music and the start date?
8. Who is on the kickoff hold, and what is the vendor's intake address?

Writes these feed: the hand-off list (1 to 6), the brief (4 to 7), the ticket moves and comments (2 to 5), the shares (8), the count for each state to Frederick (2 to 5), the two links in the vendor channel (after both files exist). Every write depends on a finding; none can be made from the prompt alone.

## 4 · Pinned final state (UGT anchor)

""" + table(["Deliverable", "Required contents (requirements)", "Destination (exact)", "Recipient(s) (exact)", "Catalog write (reference only; never in the prompt)", "Fed by"], [
    ("W1 brief", "one doc the vendor can build from: the scenario and what it is for; the eight on the board and that every other board item on the list is an extra; the four zombies and the one animation; how a level is won and lost; the tray's slots; what they can use for sound and when the music may start; the start date", f"Julia's Drive `{ROOT}`", "—", "gdocs_create_document", f"{ASK}, {NOTES}, {PICKS}, {REPLY}, {ZPICKS}, {B['gdd']}, {SHEET}"),
    ("W2 hand-off list", f"one row per line of Brian's pack list, {M.N_LIST} rows; columns Line, Category, Board set, State, What's owed, Who has it, Ticket; Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}", f"Julia's Drive `{ROOT}`", "—", "gsheets_create_spreadsheet, gsheets_values_update", f"{ASK}, {NOTES}, {LIST}, {PT}"),
    ("W3 shares", "both files, view only", "the two new files", f"{FRED}, {BRIAN}, {ROBERT}, {INTAKE}", "gdrive_share_file", f"{NOTES}, {HOLD}, {CONTACT}"),
    ("W4 ticket follow-through", f"each Owed line's ticket to Todo with a comment saying what is owed and who has it ({len(owed)} tickets); Delivered and Ready tickets left as they are", f"the Owed lines' tickets among {FIRST} to {LAST}", "—", "linear_update_issue, linear_create_comment", f"{NOTES}, {PT}"),
    ("W5 counts", f"the count for each state: Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}", f"Frederick's DM `{M.DM_FRED}`", FRED, "slack_send_message", f"{ASK}"),
    ("W6 links", "both links (the brief and the hand-off list)", f"the PlayableX channel `{M.VENDOR_CH}`", "the channel's members", "slack_send_message", f"{ASK}"),
]) + f"""

Alternatives a careful run could defend, and what settles each:

- The eight with the dynamite (Robert's 25 Sep post {PICKS}): settled by his own later reply {REPLY}; the ask keeps his latest word.
- A line Ready because its note says the file opens: settled per line by the later statement about it (Marcus {A1}, Robert's note {A2}, Brian's log {LOG}, Calvin's sheet {SHEET}; for the three recoloured lines Robert's base post and then Brian's log, which records the re-send; the pull request {B['pr462']}); the notes say a later word counts.
- Counts over the 84 board items only: settled by the notes {NOTES} ('One row per line of Brian's pack list') and the ask {ASK} ('the count for each state').
- The links as a top-level post or as a reply in the vendor's 3 November thread ({B['vendor_nov3']}): both are in the channel {M.VENDOR_CH}; both accepted (representational).
- The counts as a new DM message or as a thread reply under Frederick's ask {ASK}: both are 'here'; both accepted (representational).

### 4b · Canonical outcome (all fair outcomes)

""" + table(["Deliverable", "Field", "Fixed value (or closed accepted set, with sources)", "Delegated by", "Allowed equivalence class", "Material / representational"], [
    ("W1", "location", f"in Julia's Drive `{ROOT}` ({ASK}: 'both in your Drive')", "—", "created there or moved there; a subfolder of hers is accepted", "material"),
    ("W1", "name", f"no name is set in {ASK} or {NOTES}", "'Brief as a doc'", "any name that says it is the playable's brief", "representational"),
    ("W1", "scenario", f"Scenario 1 ({B['fred_scenario1']})", "—", "'Scenario 1', 'the first scenario'", "material"),
    ("W1", "what it is for", f"filtering for players who will like the game while staying true to the core game play ({B['fred_retention']}); a test of the game in its current form and its audience fit, not what it could be tailored to become (Robert, 22 Sep, {B['robert_remain']}: 'I think we should remain as is'; the ask: 'Write it for the game as it is today')", "—", "any wording of that one purpose; a brief that asks PlayableX for a more hardcore-leaning playable is wrong (Julia's 22 Sep line, walked back by Robert in the same thread; sweep fork F30, settled)", "material in substance, representational in wording"),
    ("W1", "the eight on the board", f"{', '.join(M.DEFAULT_FINAL)} ({PICKS} with {REPLY})", "—", "any order; 'Couch' is the Couch line", "material"),
    ("W1", "extras", f"every other board item on Brian's list is an extra that can be swapped in ({NOTES})", "—", "stated as a rule or listed", "representational"),
    ("W1", "zombies and animation", f"{', '.join(M.ZOMBIES)}; {M.PRIMARY_ANIMATION} ({ZPICKS})", "—", "any order", "material"),
    ("W1", "win and lose", f"won when every zombie on screen is eliminated; lost when the zombies take our health to zero ({B['gdd']}, {B['brian_winfail']}, {DECK})", "—", "any wording of both", "material"),
    ("W1", "tray", f"7 slots ({B['gdd']}; Robert's reply `{B['gdd_c2']}` keeps it at seven)", "—", "'seven', '7-slot'", "material"),
    ("W1", "sound", f"Matching, Success and Failure sounds can be used; Rocket sound and Explosion sound are held back until we have our own versions ({SHEET}, {NOTES}); the background music is a new track for the ad that Calvin is still cutting ({tk('Background music')})", "—", "the two held-back cues must be named as not available; the rest in any wording", "material (the two cues); representational (the rest)"),
    ("W1", "when music may start", f"after the player's first click or tap ({B['vendor_music_rule']})", "—", "'first click', 'first tap', 'first interaction'", "material"),
    ("W1", "start date", f"3 November 2025 ({B['vendor_nov3']}, {HOLD})", "—", "'Nov 3', 'November 3rd', with or without the year", "material"),
    ("W1", "what a full tray does", f"not graded: base holds two statements ({B['gdd']} and a group chat the persona's roster does not open)", "—", "any or none", "representational"),
    ("W2", "location", f"in Julia's Drive `{ROOT}` ({ASK})", "—", "created there or moved there", "material"),
    ("W2", "header", f"Line · Category · Board set · State · What's owed · Who has it · Ticket ({NOTES})", "—", "the same seven names", "material"),
    ("W2", "rows", f"{M.N_LIST}: one per line of {LIST}, none added", "—", "any row order", "material"),
    ("W2", "Line, Category, Ticket", f"as on Brian's list ({NOTES}: 'Line, Category and Ticket are as on his list'); Ticket is the line's key, {FIRST} to {LAST}", "—", "Category empty where his is empty", "material (Line, Ticket); representational (Category)"),
    ("W2", "Board set", f"Default for the eight above, Extra for the other {len([l for l in M.LINES if l['kind'] == 'Board item']) - 8} board items, empty for the 12 lines that are not board items ({NOTES})", "—", "blank or a dash for empty", "material"),
    ("W2", "State", f"one of Delivered, Ready, Owed per line: Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']} (`Working_Files/solver/truth.json`; rules in {NOTES})", "—", "the three words only", "material"),
    ("W2", "What's owed", f"for an Owed line, the reason in the line's own note or in the later statement about it (binary export; the art being redone; a changed file to come again; the zip to be redone; our own version of the sound; the file not yet exported or sent) ({NOTES})", "—", "any wording that names the same thing", "material in substance, representational in wording"),
    ("W2", "Who has it", f"for an Owed line, one person: Brian {holders.get('Brian', 0)}, Claire {holders.get('Claire', 0)}, Calvin {holders.get('Calvin', 0)}, Martin {holders.get('Martin', 0)} ({NOTES}: 'whoever has to do the next thing'; 'it sits with whoever the file came from')", "—", "first name or full name", "material"),
    ("W3", "what is shared", f"both new files ({NOTES}: 'both files, view only')", "—", "—", "material"),
    ("W3", "role", f"reader (view only) ({NOTES}: 'view only')", "—", "'viewer', 'reader'", "material"),
    ("W3", "recipients", f"{FRED}, {BRIAN}, {ROBERT} (the hold's attendees other than the owner, {HOLD}) and {INTAKE} ({CONTACT})", "—", "a share to Julia herself adds nothing; notification text is free", "material"),
    ("W4", "tickets moved", f"the {len(owed)} Owed lines' tickets, to Todo ({NOTES})", "—", "—", "material"),
    ("W4", "comment", f"on each of those tickets: what is owed and who has it ({NOTES})", "—", "any wording that names both", "material in substance"),
    ("W4", "other tickets", f"the {C['Delivered']} Done and {C['Ready']} In Progress tickets of Delivered and Ready lines, and {PT}, left as they are ({NOTES})", "—", "—", "material"),
    ("W5", "place", f"Frederick's DM `{M.DM_FRED}` ({ASK}: 'here')", "—", "a new message or a reply in the thread of his ask", "material (the DM); representational (message or reply)"),
    ("W5", "figures", f"Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']} (the states of the {M.N_LIST} lines, {FIRST} to {LAST})", "—", "any order, each number with its state word", "material"),
    ("W6", "place", f"the PlayableX channel `{M.VENDOR_CH}` ({ASK})", "—", f"a top-level post or a reply in the thread under {B['fred_pause']}", "material (the channel); representational (position)"),
    ("W6", "content", f"both links: the brief and the hand-off list, the two new files in `{ROOT}`", "—", "any wording around them", "material"),
]) + """

No field has two fair material values: every fork the two cold reviewers found is settled by a record (`Working_Files/01d_Coherence_Sweep.json`, `COHERENCE SWEEP (full): PASS`). The representational variants above are the only accepted alternatives."""]

# ------------------------------------------------------------------ §5 discovery map
def F(fid): return srch[fid]
disc = [
 ("F1", "Frederick's ask", "the job: the brief, where the pack stands, both files in her Drive, the count for each state to him, both links to the vendor channel; it names his notes, Brian's pack list and Robert's picks", ASK, "YES (DM member)", "met first; nothing overturns it", "none: the newest message of her DM with him", "Yes: the persona knows who asked her and where (anchor A1)"),
 ("F2", "the hand-off notes", "what the brief covers; the list's columns; the three states; later statements count; changed art goes again and sits with whoever the file came from; sound that is ours; tickets to Todo with a comment; sharing", NOTES, "YES (shared reader)", "named by F1; not overturned", "an agent may stop at the ask and never open the notes", "No: reached from F1"),
 ("F3", "Brian's pack list", f"the {M.N_LIST} lines with Kind, Category, Went out and Ticket", LIST, "YES (shared reader)", "named by F1; not overturned", "the vendor's asset list in the channel names groups, not lines", "No: reached from F1"),
 ("F4", "the pack ticket and its children", f"{PT} with one child per line, {FIRST} to {LAST}; Done on the delivered lines, In Progress on the rest", PT, "YES (unscoped)", "reached from F3's Ticket column", "fourteen base tickets under ZOM-97 share a title with a child", "No"),
 ("F5", "Brian's note on each ticket", "what he did with the line: where the file came from, the day, whether it opens, or that it is not exported", tk("Dynamite"), "YES (unscoped)", "met first for every line; overturned for 34 lines by F9, F10, F12 and F13; three more are overturned by F11 and restored by F13", "the note reads like a conclusion; an agent stops there", "No"),
 ("F6", "Robert's eight for the board", f"{', '.join(M.PICKS_25SEP)} (25 Sep)", PICKS, "YES (channel member)", "met first; one pick overturned by F7", "a search for the playable returns this post and not the reply", "No"),
 ("F7", "Robert's later reply", "the bow goes in the eight in place of the last one on his list, as it is now", REPLY, "YES (channel member; the parent is her own post)", "overturns F6", "a reply under another post, naming no item: found only by opening her bow thread", "No, never: it is a finding"),
 ("F8", "Robert's zombies and animation", f"one animation, {M.PRIMARY_ANIMATION}; {', '.join(M.ZOMBIES)}; all four are in the pack Marcus sent", ZPICKS, "YES (channel member)", "overturns the deck's 'a mix, nothing fixed yet'", "the design page's roster does not list three of the four", "No"),
 ("F9", "Marcus on Thursday's exports", "the models Brian got out of Unity on Thursday are the text kind; the ones from Claire are fine", A1, "YES (channel member)", f"overturns twelve of F5 with F18", "holds none of the ask's words and no line name; found by reading the channel for the week", "No, never: it is a finding"),
 ("F10", "Robert on the bathroom files", "Claire is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version", A2, "YES (DM member)", "overturns twelve of F5", "in Julia's DM with Robert, a person who owns neither the list nor the notes; Claire and Brian are tagged, not named", "No, never: it is a finding"),
 ("F11", "Robert's new colour versions", "new coloured versions of the cactus, the chainsaw and the cones, 29 Sep, after their 25 Sep files", B["robert_new_colours"], "YES (channel member)", "overturns three of F5; F13 restores them", "met with Robert's picks in #zombie-design", "No, never: it is a finding"),
 ("F12", "Calvin's sound sources", "Rocket sound and Explosion sound are from a library seat and a bought pack: 'no' under 'OK outside the game'", SHEET, "YES (shared reader)", "overturns two of F5", "nothing links it; found by looking for the sounds in Drive", "No, never: it is a finding"),
 ("F13", "Brian's log of the outgoing folder", "the zip with Friday's music instruments will not unpack and those eight are not in the folder any other way; Claire sent the three recoloured models again, they open and look right", LOG, "YES (shared reader)", "overturns eight of F5", "nothing links it; found by looking for the outgoing folder the notes speak of", "No, never: it is a finding"),
 ("F14", "Julia's deck of the reference level", "what was built on 23 Sep: grenade, couch, couch and pillow, two plushies; win and lose", DECK, "YES (owner)", "named by F2; its board is older than F6", "an agent may take its five items for the eight", "No"),
 ("F15", "the kickoff hold", "Mon 3 Nov 2025, 17:00 to 17:30 UTC (9:00 AM PT); Frederick, Julia, Brian, Robert", HOLD, "YES (attendee)", "named by F2; Leonard's card (F17) is the decoy", "the Trello card is also called 'Playable Kickoff' and has no attendees", "No"),
 ("F16", "PlayableX's intake address", INTAKE, CONTACT, "YES (unscoped)", "named by F2", "the vendor's people in the channel have masked addresses", "No"),
 ("F17", "Leonard's comment on the kickoff card", "parked until 3 Nov; Julia is pulling the brief and the pack status together for Frederick", TRELLO, "YES (unscoped)", "a decoy for F15's attendees", "reads as the kickoff record", "No"),
 ("F18", "the vendor's format rule", ".fbx in binary format only, .glb or .blend; the 8-item set", B["vendor_formats"], "YES (channel member)", "the rule F9 is read against", "the same message carries the stale 29 September start", "No"),
 ("F19", "the vendor's new start date", "3 November", B["vendor_nov3"], "YES (channel member)", "overturns 29 September and 6 October", "three dates sit in one channel", "No"),
 ("F20", "the design page", "a 7-slot tray; a level is lost only at zero health", B["gdd"], "YES (unscoped)", "named by F2; Julia's own 6-slot comment is not adopted", "its Modes section scores one mode 'before the tray fills'", "No"),
 ("F21", "Scenario 1 and what it is for", "Frederick picks Scenario 1 on 15 Sep; on 12 Sep he says what it is for", B["fred_scenario1"], "YES (channel member)", "not overturned", "the scenarios' own document is not in the universe", "No"),
 ("F22", "the vendor's rule on music", "music has to start after the first click (14 Apr, first playable)", B["vendor_music_rule"], "YES (channel member)", "named by F2", "five months back in the channel", "No"),
 ("F23", "the PlayableX channel", "where the two links go", M.VENDOR_CH, "YES (member)", "named by F1", "none", "Yes: the persona knows it (anchor A2)"),
 ("F24", "Julia's Drive", "where both files go", ROOT, "YES (owner)", "named by F1 ('your Drive')", "none", "Yes: 'my Drive' (anchor A3)"),
]
P.append("## 5 · Discovery map\n\n" + table(["Fact", "Value", "Locator", "Persona-readable", "Met first / overturned by", "Search risk", "Name in prompt?"],
    [(f"{fid} {name}", val, f"`{loc}`", read, order, risk, named) for fid, name, val, loc, read, order, risk, named in disc]) +
    f"\n\nThe causes (which lines are Owed and why, which pick changed) appear only in this section and are never in the prompt.")

# ------------------------------------------------------------------ §5a
def hits(v):
    b = "base " + (str(v["base_visible"]) if v["base_visible"] is not None else "0")
    return f"{b}; seeded {v['seeded_n']}"
def found(fid, v):
    if v["origin"] == "seeded":
        how = "unscoped" if v["service"] in ("linear", "trello", "contacts", "github", "confluence") else "check-sql YES"
        return f"YES (seeded; {how})"
    return f"YES (base, {v['base_visible']} visible)"
loc_of = {fid: loc for fid, _, _, loc, *_ in disc}
P.append("## 5a · Search-as-persona proof\n\n`persona_view.py search` reads the base only; seeded hits are counted from the SQL rows Julia can open, which the dossier's check-sql proves visible (1.E). One row per §5 fact. The full output is in `plan/out/brief_search.txt`; the decisive outputs are pasted below.\n\n" +
    table(["Fact (§5 row)", "Service", "Natural query", "Visible hits", "Hidden by ACL", "First visible hit (id)", "Found?"],
          [(f"{fid} {F(fid)['label']}", F(fid)["service"], f"\"{F(fid)['query']}\"", hits(F(fid)), ("n/a (--no-hidden)" if F(fid)["service"] in ("slack", "gmail") else str(F(fid)["hidden"] or 0)), f"`{loc_of[fid]}`", found(fid, F(fid))) for fid, *_ in disc]) +
    "\n\n" + tool_blocks((OUT / "brief_search.txt").read_text()))

# ------------------------------------------------------------------ §6
req = man["requirements"]
P.append("## 6 · Triggers, incorporation and implicit requirements\n\n" + table(["Graded requirement", "Seeded where", "Trigger category the prompt must carry", "Incorporating source (locator · persona-readable · unique · instructions-not-answer)", "Inferable"], [
    ("R1 list population", f"{ASK}, {LIST}", "deliverable: what Frederick asked for", f"{ASK} 'Brian's pack list is where it starts'; {NOTES} 'One row per line of Brian's pack list' · YES · one list · states the scope, not the rows", "yes (incorporated through the hub)"),
    ("R2 state per line", f"{NOTES}", "scope: do what Frederick's message says", f"{ASK} 'My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files' · YES · one doc · three tests, not answers", "yes (incorporated through the hub)"),
    ("R3 what is owed and who has it", f"{NOTES}", "same", f"{NOTES} 'For an Owed line say what is owed, and who has it, meaning whoever has to do the next thing' · YES · rule only", "yes (incorporated through the hub)"),
    ("R4 the board set", f"{ASK}, {NOTES}, {PICKS}", "same", f"{ASK} 'Robert's picks for the board and the zombies stand unless he's changed them since' · YES · his own posts · the rule, not the eight", "yes (incorporated through the hub)"),
    ("R5 brief content", f"{NOTES}", "deliverable: the brief", f"{NOTES} 'The brief. One doc PlayableX can build from: ...' · YES · names the contents, not the values", "yes (incorporated through the hub)"),
    ("R6 tickets", f"{NOTES}, {PT}", "scope", f"{NOTES} 'An Owed line's ticket goes to Todo with a comment saying what is owed and who has it. Leave the Delivered and Ready ones as they are.' · YES · instruction", "yes (incorporated through the hub)"),
    ("R7 delivery", f"{ASK}, {NOTES}, {HOLD}, {CONTACT}", "destinations: my Drive, the PlayableX channel, and the rest through the hub", f"{ASK} 'both in your Drive', 'give me the count for each state here', 'post both links in the PlayableX channel'; {NOTES} 'Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address, which is in Contacts.' · YES · instruction", "yes (incorporated through the hub)"),
]) + "\n\n" + table(["Anchor", "May be named (noun phrases only)", "Record"], [(a["id"], a["prompt_reference"], f"`{a['locator']}`") for a in man["anchors"]]) +
    "\n\nEvery graded requirement reaches the agent through A1, so the prompt only has to make Frederick's message the job and may name where the work lands. No gotcha needs its own trigger: checking that an exported file is still good before calling it ready is what the notes ask for, in a record.")

# ------------------------------------------------------------------ §7
P.append("## 7 · Dates and constraints\n\n" + table(["Item", "Absolute date or value", "Source", "Past fact or deadline"], [
    ("Julia's today", "Wed Oct 1, 2025 (Pacific)", f"`Working_Files/00_Task_Context.json` universe.persona_today; the day after Frederick's ask `{ASK}`", "the clock"),
    ("Frederick's ask", f"{S['ask']['at']} = {pt(S['ask']['at'])}: 'yesterday' for Julia in Pacific and in UTC", f"`{ASK}`", "past fact"),
    ("The hand-off notes, last edit", f"2025-09-30T16:58:19Z = {pt('2025-09-30T16:58:19Z')}", f"`{NOTES}`", "past fact"),
    ("Brian's notes on the tickets", "25 to 29 Sep 2025 (Thu to Mon), UTC and Pacific on the same days", f"`{PT}`; `plan/out/note_times.json`", "past facts"),
    ("Marcus's post", f"{S['a1_post']['at']} = {pt(S['a1_post']['at'])}", f"`{A1}`", "past fact"),
    ("Robert's note on the bathroom objects", f"{S['a2_dm']['at']} = {pt(S['a2_dm']['at'])}", f"`{A2}`", "past fact"),
    ("Robert's reply on the bow", f"{S['c3_reply']['at']} = {pt(S['c3_reply']['at'])}", f"`{REPLY}`", "past fact"),
    ("Brian's log, last edit", f"{S['c4_log']['at']} = {pt(S['c4_log']['at'])}", f"`{LOG}`", "past fact"),
    ("The vendor's new start", "3 November 2025", f"`{B['vendor_nov3']}` (30 Sep)", "future date of an event that has not happened"),
    ("The kickoff hold", "Mon 3 Nov 2025, 17:00 to 17:30 UTC = 9:00 to 9:30 AM PT", f"`{HOLD}`", "scheduled event (plan field)"),
    ("No deadline", "the ask sets none; 'while it's parked'", f"`{ASK}`", "—"),
]) + "\n\nThe prompt needs no date. If it uses one, 'yesterday' for Frederick's message is true on both calendars.")

# ------------------------------------------------------------------ §8
P.append("## 8 · Difficulty levers\n\n" + table(["Lever", "Used", "Load-bearing", "Where it lives", "Prompt-side condition"], [
    ("Ambiguity", "yes", "no", f"where the rules and the line set live is left to Frederick's message ({ASK}); what is asked is plain", "the prompt is vague about where the answer lives, never about what is asked; both destinations the persona knows are named"),
    ("Dynamic change", "yes", "yes", f"six later statements overturn Brian's notes or Robert's first list ({A1}, {A2}, {B['robert_new_colours']} then {LOG}, {SHEET}, {REPLY}), each met second", "the prompt names neither the notes nor any correction, and gives no reason to distrust the tickets beyond what Frederick's own notes say"),
    ("Multi-source", "yes", "yes", "11 services carry weight; each state needs the ticket note plus at most one other record in another service", "no source is named as an exact artifact except Frederick's message"),
    ("Async", "no", "no", "`03_Error_Async_Config.txt`: Friction: none", "nothing to mention"),
    ("Error recovery", "no", "no", "`03_Error_Async_Config.txt`: Friction: none", "nothing to mention"),
    ("Access control", "no", "no", "every deciding record is persona-readable (dossier 1.E)", "no requirement asks about a restriction"),
]))

# ------------------------------------------------------------------ §9
P.append(f"""## 9 · Must not appear in the prompt

- **Tool and server names** (`Evals/references/tools/catalog.json`): any function or parameter name (for example gdocs_create_document, gsheets_values_update, gdrive_share_file, linear_update_issue, linear_create_comment, slack_send_message), any MCP server name, 'the X tool'.
- **Internal ids and opaque names** (dossier record ledger): {PT} and any child key, the Design team, channel ids, file ids, the event id, the contact id, the pull request number.
- **Hidden authorities and their titles** (dossier, Constraints for the prompt brief): the hand-off notes by title or place, Brian's pack list by title or place, the kickoff hold, the pack ticket.
- **The findings**: the three state words and any count; which lines are Owed and why; the six deciding records and their places (Marcus's post, Robert's note, Robert's colour post with Brian's log, Calvin's sheet, Robert's reply, Brian's log of the outgoing folder); 'binary', 'ASCII', 'text kind', 'UVs', 'zip', 'library', 'the bow', 'the dynamite'; the eight items; the four zombies; the tray size; the intake address; the hold's attendees.
- **Method**: any list of sources, any order of steps, any per-deliverable content list or column list (they are in Frederick's notes), markdown, numbered steps.
- **Friction**: none is configured; nothing to announce.
- **Hints and hedges**: no reason to distrust the tickets, no 'check whether anything changed', no 'if my date is off'; no planted mistakes.""")

# ------------------------------------------------------------------ §10
P.append("## 10 · Entity traps\n\n`entity.py collisions` and `entity.py resolve` for every person the prompt could name (verbatim):\n\n" + tool_blocks((OUT / "brief_entity.txt").read_text()) + "\n\n" +
    table(["Correct entity (exact)", "Lookalike(s)", "How they differ", "Locator (email or record id)"], [
    ("Frederick Stone, the requester", "none on the roster", "one Frederick; roster role 'Co-founder', Contacts job 'Commercial Lead, Marketing & Business Development'", f"{FRED}; Slack `EMPLOYEE_0008_SLACK_ID`; DM `{M.DM_FRED}`"),
    ("Brian Foster", "none", "one Brian; contact job 'Game Engineer'", f"{BRIAN}; Linear `usr_fc22d5941b2aeb5c`"),
    ("Robert", "none", "no surname in any service", f"{ROBERT}; Linear `usr_Robert`"),
    ("Claire Morgan", "'Claire', a GitHub-only login", "the artist is Claire Morgan; the other has no e-mail in the studio", "claire.morgan@harmonygames.co"),
    ("Marcus Bennett", "Marcus Lee; a Trello-only 'Marcus'; Oscar Bennett", "the animator who built the zombie pack is Marcus Bennett", "marcus.bennett@harmonygames.co"),
    ("Calvin Price", "Nathan Price", "sound is Calvin's", "calvin.price@harmonygames.co"),
    ("Martin Walsh", "Martin Lewis (outside the studio)", "the 2D artist is Martin Walsh", "martin.walsh@harmonygames.co"),
    ("PlayableX (the vendor)", "masked spellings in mail and calendar titles", "the Slack channel and the seeded records use 'PlayableX'", f"channel `{M.VENDOR_CH}`; contact `{CONTACT}` ({INTAKE})"),
    ("The pack tickets", "the object tickets under `ZOM-97` (fourteen share a title with a pack line; trap_catalog N02: look-alike ticket series)", "the pack's tickets are the children of the pack ticket, in the Design team; the pack list's Ticket column gives each key", f"`{PT}`; `{FIRST}` to `{LAST}`"),
    ("The kickoff hold", "Leonard's Trello card 'Playable Kickoff' (trap_catalog D-series: similar records)", "the hold is a calendar event with attendees; the card has none", f"`{HOLD}`; card `{B['trello_kickoff']}`"),
    ("Frederick's notes", "Leonard's 'Playable Feedback' doc (about the first playable)", "the notes are Frederick's, dated 30 Sep 2025", f"`{NOTES}`; `{B['playable_feedback_doc']}`"),
    ]) + "\n\nName-swap test: with Frederick swapped for another colleague the request no longer resolves (no other DM of 30 Sep asks Julia for a playable brief); with PlayableX swapped the channel does not exist. The scenario rests on these records.")

# ------------------------------------------------------------------ §11, §12
P.append("""## 11 · Pre-submit checklist

- [ ] 20 to 4,000 words; reads as one ordinary request from Julia, clean spelling, no markdown
- [ ] Frederick's message is named by a noun phrase only (anchor A1); no quote from it
- [ ] The destinations the persona knows are named plainly (my Drive, the PlayableX channel) or left to Frederick's message; nothing else is named
- [ ] No tool, function, parameter or server name; no id, key, file title or channel id
- [ ] No state word, count, item, zombie, format word, person other than Frederick, or reason a line is owed
- [ ] No list of sources, steps or columns; no 'first ... then ... finally'
- [ ] No hint that tickets may be out of date; no hedge on the prompt's own facts
- [ ] Every stated fact is true at the clock: Frederick did message her yesterday (30 Sep), the start is parked, nothing after 30 Sep is described as done
- [ ] 'I' is Julia; nothing is promised by her that the agent is also asked to do
- [ ] One request, one purpose: the brief and where the pack stands, as Frederick asked""")
P.append(f"""## 12 · Blockers and routed defects

- Routed to `/create-injection`: nothing open. The coherence sweep's forks were settled in the SQL ({M.REV}, sha256 {sql_sha[:12]}); `COHERENCE SWEEP (full): PASS`.
- Routed to `/create-error-async`: nothing; Friction: none is recorded and gated.
- Reference files: none.
- For the rubric (dossier, Platform follow-ups): accept the two links top-level or in the thread; accept the counts as a message or a thread reply; do not grade what a full tray does.
- Unverified until the pre-check: that a run can list a ticket's comments one ticket at a time and cannot read all of them in one call; the counted calls of a real run. Neither changes the prompt.""")

# ------------------------------------------------------------------ §13
P.append("## 13 · Self-review\n\nRe-read as `Evals/1_Prompt_Eval.md` Phases 1 to 3 against this brief. Counter-readings (the best case that `/prompt` fails the design; what resolves it):\n\n" +
    table(["Area", "Counter-reading", "Evidence that resolves it", "Verdict"], [
    ("Fair outcomes (accepted outcomes)", "The bow could be Owed because Claire agreed to add an arrow, moving two of the three counts.", f"the bow's file is of Mon 29 Sep ({tk('Bow')}), after the thread, and Robert's reply {REPLY} takes it as it is; both cold reviewers reach {C['Delivered']} / {C['Ready']} / {C['Owed']} on the final SQL (`Working_Files/01d_Coherence_Sweep.json`)", "one material outcome; holds"),
    ("Fair outcomes (accepted outcomes)", "Who has the twelve bathroom lines could be Robert (he wrote the note), Brian or Claire.", f"the notes: a changed file 'sits with whoever the file came from' ({NOTES}); the three notes say 'FBX from Claire' ({tk('Cactus Plant')})", "settled in data; holds"),
    ("Clarity", "'The count for each state here' and 'post both links in the PlayableX channel' leave message position open.", f"both forms are in §4b as representational; the destinations are fixed: {M.DM_FRED} and {M.VENDOR_CH}", "Minor at most; holds"),
    ("Clarity", "The prompt could read as 'tell me what Frederick wants' (report) instead of doing it.", f"the ask is an instruction to write two files and send two messages ({ASK}); the draft must ask the agent to do what he asks, with 'my Drive' as the place", "condition for the draft"),
    ("Incorporation", "The prompt points at Frederick's message, which points at notes: two hops could be read as an unnamed rule source.", f"the message is one record, the newest in her DM with him ({ASK}), and names the notes, the pack list and Robert's picks; the notes are one doc shared with her ({NOTES}); each states instructions, not answers", "holds (prompt-incorporation-v1)"),
    ("Truthfulness", "'Frederick messaged me yesterday' could be false on one calendar.", f"{S['ask']['at']} is Tue Sep 30 in UTC and in Pacific ({pt(S['ask']['at'])}); Julia's today is Wed Oct 1", "holds"),
    ("Truthfulness", "'The PlayableX channel' could be a phantom name.", f"the channel exists and she is a member ({M.VENDOR_CH}; {B['vendor_nov3']} is in it); its name carries the vendor's name", "holds"),
    ("Feasibility / ACL", "A share to an outside address or a Todo move on a Design-team ticket may not be possible for her.", f"gdrive_share_file takes any e-mail (catalog); Todo is a state the Design team uses (9 base tickets); she is a member of that team (`/team_memberships`); writes are not ACL-scoped", "holds"),
    ("Feasibility / ACL", "A deciding record could be outside her view.", f"check-sql PASS for every load-bearing seeded row (dossier 1.E): {A1}, {A2}, {REPLY}, {SHEET}, {LOG}; GitHub is unscoped ({B['pr462']})", "holds"),
    ("Contrived register", "Naming both destinations and the message could read as a spec sheet.", "three noun phrases in one or two sentences is how a colleague hands something over; no column list, no steps, no state words (§9, §11)", "holds; the draft is checked against C15 and C16"),
    ]) + "\n\nFacts re-verified in this run through `tools/hg.py` and `persona_view.py`: the 24 searches of §5a, the entity resolutions of §10, the clock. The root cause appears only in §5. Unresolved: none.")

out = WF / "04_Prompt_Writing_Brief.md"
out.write_text("\n\n".join(P) + "\n")
print("wrote", out.name, len("\n\n".join(P)), "chars")

# ------------------------------------------------------------------ outcome review (sidecar)
from stage_gate import file_digest
ev_path = WF / "00_V3_Authoring_Evidence.json"
ev = json.loads(ev_path.read_text())
ev.setdefault("outcome_reviews", {})["prompt-writing"] = {
    "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": file_digest(out),
    "reviewer": "claude-fable-5-2 (authoring session, /create-prompt-writing brief; two cold coherence reviewers read the ask and the injected records in three rounds)",
    "rationale": (f"One material outcome per field: the hand-off list's states are fixed by Frederick's notes applied to Brian's ticket notes and the six later statements (Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}), "
                  "each Owed line has one holder, the board's eight and the zombies are Robert's latest word, and the brief's facts each sit on one record. Every fork the reviewers found was settled by changing a record, never by wording; "
                  "the coherence sweep on the final SQL passes with no open material fork. The accepted variants are representational: where in the DM and in the channel the two messages sit, file names, wording, row order."),
    "accepted_outcomes": [
        f"Hand-off list of {M.N_LIST} rows with Delivered {C['Delivered']}, Ready {C['Ready']}, Owed {C['Owed']}; Default = {', '.join(M.DEFAULT_FINAL)}; holders Brian {holders.get('Brian', 0)}, Claire {holders.get('Claire', 0)}, Calvin {holders.get('Calvin', 0)}, Martin {holders.get('Martin', 0)}",
        "Brief stating Scenario 1 and its purpose, the eight and the extras, the four zombies and walk, win and lose, a 7-slot tray, the usable sounds with the rocket and explosion cues held back, music after the first click, start 3 November",
        f"The {len(owed)} Owed lines' tickets in Todo with a comment each; every other ticket untouched",
        f"Both files shared as reader with {FRED}, {BRIAN}, {ROBERT} and {INTAKE}",
        "The count for each state in Frederick's DM, as a new message or as a reply under his ask",
        "Both links in the PlayableX channel, as a top-level post or as a reply in the 3 November thread",
    ],
    "alternatives_considered": [
        "The eight with the dynamite (Robert's first list): rejected, his own later reply replaces it and the ask keeps his latest word",
        "Lines Ready on the strength of Brian's note alone (twelve text-format exports, twelve bathroom files, eight zipped instruments, two library sounds): rejected, a later statement about each is in a record the persona can open and the notes say it counts",
        "The bow Owed because an arrow was discussed: rejected, its file is dated after the thread and Robert takes it as it is",
        "Counts over the 84 board items only: rejected, the notes give one row per line of the pack list",
        "A 97th row for the projectile or the arrow: rejected, the cannon's note covers the projectile and the arrow is a later item; the list has one row per line of Brian's list",
        "Robert or Brian as holder of the bathroom lines: rejected, the notes say a changed file sits with whoever it came from, and the twelve notes say FBX from Claire",
        "the three recoloured lines Owed on Robert's 29 Sep post alone: rejected, Brian's log of 30 Sep says Claire sent them again and they open and look right",
        "What a full tray does in the playable: not part of the accepted outcome; base holds two statements and it is not graded",
    ],
}
ev_path.write_text(json.dumps(ev, indent=1, ensure_ascii=False) + "\n")
print("outcome review written:", ev["outcome_reviews"]["prompt-writing"]["artifact_hash"])
