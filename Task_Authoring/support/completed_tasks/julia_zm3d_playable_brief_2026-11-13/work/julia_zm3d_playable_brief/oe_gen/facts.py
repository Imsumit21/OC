#!/usr/bin/env python3
"""The §B fact list of the OE ledger, built from oe_gen/model.py (records only). Shared by the ledger, the drafted events
and the check, so the three never disagree. Facts are in dependency order; '{F:key}' tokens resolve to F-numbers."""
import json, re
import model as O

q = O.q
FACTS = []
def add(key, fact, service, tools, locator, origin, expected, result, visible, depends, source):
    FACTS.append(dict(key=key, fact=fact, service=service, tools=tools, locator=locator, origin=origin, expected=expected,
                      result=result, visible=visible, depends=depends, source=source))

def one(text): return re.sub(r"\s*\n\s*", " ", text).strip()
def names(ls): return ", ".join(l["name"] for l in ls)
def who_name(uid): return O.NAMES.get(uid, uid)
SEEDED_SLACK = "VERIFIED: quote cut from the SQL row text; time from its ts"
BASE_SLACK = "VERIFIED: quote cut from the base record re-read through tools/hg.py; time from its ts"

# ------------------------------------------------------------------ hub
add("ask", "Frederick's message to Julia about the playable (the ask)", f"Slack (Julia's DM with Frederick, {O.DM_FRED})",
    "slack_search_public_and_private, slack_conversations_history", O.ASK["id"],
    'prompt ("Frederick\'s playable message from yesterday"); search "playable"',
    f"Sent {O.when(O.ASK['ts'])} by {O.ASK['user']} (Frederick Stone) in DM {O.DM_FRED}; a root message, reply_count 0. Quote: '{O.ASK['text']}'",
    SEEDED_SLACK, "YES (DM party; check-sql)", "—", f"SQL L{O.ASK['line']}")

nd = O.drive(O.NOTES_ID)
add("notes", "Frederick's hand-off notes", "Docs (shared with Julia)", "gdrive_search, gdocs_get_document_text", O.NOTES_ID,
    'prompt ("Can you do everything he\'s asking for in it, start to finish?": the message it hands over says "My hand-off notes"); {F:ask}; search "hand-off notes"',
    f"Document '{O.NOTES['title']}', owner {nd['owner_email']}, created {O.when(nd['created_time'])}, modified {O.when(nd['modified_time'])}. "
    f"Text (line breaks shown as spaces): '{one(O.NOTES['body_text'])}'",
    "VERIFIED: title, owner, times and body_text cut from the SQL rows", "YES (shared reader; check-sql)", "{F:ask}",
    f"{O.sql('gdrive.drive_files', id=O.NOTES_ID)}, {O.sql('gdocs.docs_documents', document_id=O.NOTES_ID)}")

pd = O.drive(O.PACK_ID)
add("pack", "Brian's pack list: 96 lines with Kind, Category, Went out and Ticket", "Sheets (shared with Julia)",
    "gdrive_search, gsheets_get_spreadsheet, gsheets_values_get", f"{O.PACK_ID} tab Pack",
    'prompt ("Can you do everything he\'s asking for in it, start to finish?": the message it hands over says "Brian\'s pack list is where it starts"); {F:ask}; search "pack list"',
    f"Spreadsheet '{O.row('gsheets.sheets_spreadsheets', spreadsheet_id=O.PACK_ID)['title']}', owner {pd['owner_email']}, created {O.when(pd['created_time'])}, "
    f"modified {O.when(pd['modified_time'])}; one tab, 'Pack'. Header: {', '.join(O.PACK_GRID[0])}. 96 rows, 84 with Kind 'Board item' and 12 others. "
    "Rows as Line (Kind; Category; Went out) Ticket: " + "; ".join(
        f"{l['name']} ({l['kind']}; {l['category'] or 'no category'}; {l['went_out'] or 'empty'}) {l['ticket']}" for l in O.LINES),
    "VERIFIED: grid cells cut from the SQL row; 96, 84 and 12 by count of rows", "YES (shared reader; check-sql)", "{F:ask}",
    f"{O.sql('gdrive.drive_files', id=O.PACK_ID)}, {O.sql('gsheets.sheets_sheets', spreadsheet_id=O.PACK_ID)}")

pt = O.ISSUES[O.PACK_TICKET]["row"]
add("ticket", "Brian's pack ticket and its 96 children", "Linear (unscoped)", "linear_get_issue, linear_list_issues", "DES-314 (its parent)",
    'prompt ("Can you do everything he\'s asking for in it, start to finish?": the notes the message hands over say "Tickets live under Brian\'s pack ticket, one per line"); {F:pack} (the Ticket column); {F:notes}',
    f"DES-314 'Couch' has parent {O.PACK_TICKET} '{pt['title']}', team Design, creator and assignee Brian Foster ({O.BRIAN_USR}), state {pt['state_id']}, "
    f"created {O.when(pt['created_at'])}. Description: '{pt['description']}' Children: 96, DES-314 to DES-409, all created by Brian Foster. "
    f"State Done on 8: {', '.join(l['ticket'] + ' ' + l['name'] for l in O.DONE)}. State In Progress on the other 88.",
    "VERIFIED: fields cut from the SQL rows; 96, 8 and 88 by count of rows", "YES (Linear unscoped)", "{F:pack}, {F:notes}",
    f"SQL L{O.ISSUES[O.PACK_TICKET]['line']} to SQL L{O.ISSUES['DES-409']['line']}")

# ------------------------------------------------------------------ Robert's picks
add("picks", "Robert's eight for the board (25 Sep)", f"Slack (#zombie-design, {O.DESIGN_CH})", "slack_search_public_and_private, slack_conversations_history",
    O.PICKS["id"], '{F:ask} ("Robert\'s picks for the board"); search "playable board"',
    f"Posted {O.when(O.PICKS['ts'])} by {O.PICKS['user']} (Robert), a root post. Quote: '{O.PICKS['text']}'",
    SEEDED_SLACK, "YES (channel member; check-sql)", "{F:ask}", f"SQL L{O.PICKS['line']}")

bow = O.base("art_bow_root"); bowc = O.base("art_bow_claire")
upd = next(r for r in O.ROWS if r["op"] == "update" and r["table"] == "slack.slack_messages")
add("bowroot", "Julia's post about the bow, the parent of Robert's reply", f"Slack (#zombie-art, {O.ART_CH})", "slack_conversations_history, slack_read_thread",
    bow["id"], 'search "arrow to go with the bow"',
    f"Posted {O.when(bow['ts'])} by {bow['user']} (Julia Lawson). Quote: '{bow['text']}'. Thread at the clock: reply_count {upd['set']['reply_count']}, "
    f"latest_reply {upd['set']['latest_reply']}. First reply {bowc['id']}, {O.when(bowc['ts'])}, by {bowc['user']} (Claire Morgan): '{bowc['text']}'",
    "VERIFIED: text cut from the base record (tools/hg.py); reply_count and latest_reply from the overlay UPDATE", "YES (channel member; can-see, check-sql)", "—",
    f"{bow['src']}; {bowc['src']}; SQL L{upd['line']}")

add("c3", "Robert's reply: the bow takes the place of the last item on his list", f"Slack (#zombie-art, {O.ART_CH})", "slack_read_thread, slack_search_public_and_private",
    O.C3["id"], '{F:bowroot} (latest_reply); {F:ask} ("unless he\'s changed them since"); search "in place of the last one"',
    f"Posted {O.when(O.C3['ts'])} by {O.C3['user']} (Robert) as a reply in the thread under {bow['id']}. Quote: '{O.C3['text']}'",
    SEEDED_SLACK, "YES (channel member; check-sql)", "{F:bowroot}, {F:ask}", f"SQL L{O.C3['line']}")

add("zpicks", "Robert's four zombies and the one animation (29 Sep)", f"Slack (#zombie-design, {O.DESIGN_CH})", "slack_search_public_and_private, slack_conversations_history",
    O.ZPICKS["id"], '{F:ask} ("Robert\'s picks for the board and the zombies"); search "4 zombies"',
    f"Posted {O.when(O.ZPICKS['ts'])} by {O.ZPICKS['user']} (Robert), a root post. Quote: '{O.ZPICKS['text']}'",
    SEEDED_SLACK, "YES (channel member; check-sql)", "{F:ask}", f"SQL L{O.ZPICKS['line']}")

add("eight", "The eight on the board at the clock", "Derived (recorded calculation)", "none (a reading of two messages)", "—", "{F:picks}, {F:c3}",
    f"{', '.join(O.EIGHT)}. Robert's list of 25 Sep in his order is {', '.join(O.EIGHT_25SEP)}; the last one on it is {O.SWAPPED_OUT}; his reply of 26 Sep sits under the bow "
    f"post and puts 'it' in the 8 'in place of the last one on my list'. {O.SWAPPED_OUT} stays on the pack list as an extra.",
    "VERIFIED by recorded calculation: the last item of the quoted list replaced by Bow; equal to solver/truth.json (8 lines with Board set Default)",
    "n/a (derived)", "{F:picks}, {F:bowroot}, {F:c3}", f"SQL L{O.PICKS['line']}, SQL L{O.C3['line']}; oe_gen/model.py EIGHT; solver/truth.json")

# ------------------------------------------------------------------ rules and deciding records
vf = O.base("vendor_formats")
add("formats", "PlayableX's format rule and the 8-item set", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_conversations_history, slack_read_thread",
    vf["id"], '{F:notes} ("What they told us about formats still holds"); search "Binary format"',
    f"Posted {O.when(vf['ts'])} by {vf['user']} as a reply in the thread under Frederick's message {O.base('fred_retention')['id']}. Quotes: "
    f"'{q(vf['text'], 'aside from the 8-item set that you will provide for the board, you can also test any additional items you’d like to try in the game')}'; "
    f"'{q(vf['text'], '*3D assets*: .fbx, .glb, or .blend (when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII)')}'; "
    f"'{q(vf['text'], '*2D assets*: .png')}'; '{q(vf['text'], '*Font*: .ttf or .woff2')}'; '{q(vf['text'], '*Sound*: .mp3 or .wav')}'. "
    f"The same message opens '{q(vf['text'], 'We are planning to start this project on *September 29*')}', a start date two later messages replace.",
    BASE_SLACK, "YES (channel member; can-see)", "{F:notes}", vf["src"])

add("a1", "Marcus on the models got out of Unity on Thursday", f"Slack (#zombie-match3d, {O.MATCH3D_CH})", "slack_conversations_history, slack_search_public_and_private",
    O.A1["id"], '{F:notes} ("if someone who knows the file or the art has said something since, that counts"); search "text kind"',
    f"Posted {O.when(O.A1['ts'])} by {O.A1['user']} (Marcus Bennett), a root post. Quote: '{O.A1['text']}' "
    "(EMPLOYEE_0026_SLACK_ID is Brian Foster, EMPLOYEE_0009_SLACK_ID is Claire Morgan)",
    SEEDED_SLACK, "YES (channel member; check-sql)", "{F:notes}", f"SQL L{O.A1['line']}")

add("a2", "Robert on the bathroom files", f"Slack (Julia's DM with Robert, {O.DM_ROBERT})", "slack_conversations_history, slack_search_public_and_private",
    O.A2["id"], '{F:notes} ("if someone who knows the file or the art has said something since, that counts"); search "redoing the UVs"',
    f"Sent {O.when(O.A2['ts'])} by {O.A2['user']} (Robert). Quote: '{O.A2['text']}' (EMPLOYEE_0009_SLACK_ID is Claire Morgan, EMPLOYEE_0026_SLACK_ID is Brian Foster)",
    SEEDED_SLACK, "YES (DM party; check-sql)", "{F:notes}", f"SQL L{O.A2['line']}")

rc = O.base("robert_new_colours")
add("c1", "Robert's new colour versions of three items", f"Slack (#zombie-design, {O.DESIGN_CH})", "slack_conversations_history, slack_search_public_and_private",
    rc["id"], '{F:notes} ("new colour versions"); search "new colored version"',
    f"Posted {O.when(rc['ts'])} by {rc['user']} (Robert), a root post with one video file. Quote: '{rc['text']}'",
    BASE_SLACK, "YES (channel member; can-see)", "{F:notes}", rc["src"])

ld = O.drive(O.LOG_ID)
add("c4", "Brian's log of the outgoing folder: the re-sent recoloured models and the instruments zip", "Docs (shared with Julia)", "gdrive_search, gdocs_get_document_text", O.LOG_ID,
    '{F:notes} ("sitting in the outgoing folder"); search "outgoing folder"',
    f"Document '{O.LOG['title']}', owner {ld['owner_email']}, created {O.when(ld['created_time'])}, modified {O.when(ld['modified_time'])}. "
    f"Text (line breaks shown as spaces): '{one(O.LOG['body_text'])}'",
    "VERIFIED: title, owner, times and body_text cut from the SQL rows", "YES (shared reader; check-sql)", "{F:notes}",
    f"{O.sql('gdrive.drive_files', id=O.LOG_ID)}, {O.sql('gdocs.docs_documents', document_id=O.LOG_ID)}")

sd = O.drive(O.SOUND_ID)
add("c2", "Calvin's sound sources sheet", "Sheets (shared with Julia)", "gdrive_search, gsheets_get_spreadsheet, gsheets_values_get", f"{O.SOUND_ID} tab Sources",
    '{F:notes} ("Anything from a library or a bought pack stays here"); search "sound sources"',
    f"Spreadsheet '{O.row('gsheets.sheets_spreadsheets', spreadsheet_id=O.SOUND_ID)['title']}', owner {sd['owner_email']}, created {O.when(sd['created_time'])}, "
    f"modified {O.when(sd['modified_time'])}; one tab, 'Sources'. Header: {', '.join(O.SOUND_GRID[0])}. Rows: "
    + "; ".join("'" + "' / '".join(c if c else "(empty)" for c in r) + "'" for r in O.SOUND_GRID[1:]),
    "VERIFIED: grid cells cut from the SQL row", "YES (shared reader; check-sql)", "{F:notes}",
    f"{O.sql('gdrive.drive_files', id=O.SOUND_ID)}, {O.sql('gsheets.sheets_sheets', spreadsheet_id=O.SOUND_ID)}")

dd = O.drive(O.DECK_ID)
add("deck", "Julia's deck of the reference level", "Slides (Julia owns it)", "gdrive_search, gslides_get_presentation_text", O.DECK_ID,
    '{F:notes} ("your deck of the reference level"); search "reference level"',
    f"Presentation '{dd['name']}', owner {dd['owner_email']}, modified {O.when(dd['modified_time'])}. Slides: "
    + "; ".join(f"'{t}': '{b}'" for t, b, _, _ in O.DECK_SLIDES),
    "VERIFIED: slide texts cut from the SQL rows", "YES (owner; check-sql)", "{F:notes}",
    f"{O.sql('gdrive.drive_files', id=O.DECK_ID)}, " + ", ".join(f"SQL L{b}" for _, _, _, b in O.DECK_SLIDES))

add("gdd", "The design page: tray slots and when a level is lost", "Confluence (unscoped)", "confluence_search, confluence_get_page, confluence_list_comments", O.GDD["id"],
    '{F:notes} ("How the level plays is on the design page"); search "7-slot tray"',
    f"Page '{O.GDD['title']}', version {O.GDD['version']}, updated {O.when(O.GDD['updated_at'])}. Quotes: '{q(O.GDD_TEXT, 'the player drags items into a 7-slot tray')}'; "
    f"'{q(O.GDD_TEXT, 'It is a tempo penalty, not a fail state - the loss screen only appears at zero health.')}' "
    f"Comments: {O.GDD_C1['id']} by Julia Lawson, created {O.when(O.GDD_C1['created_at'])}: '{q(O.GDD_C1['body'], 'I pulled the 7-slot tray down to 6 in a soft-test branch')}'; "
    f"{O.GDD_C2['id']} by Robert, created {O.when(O.GDD_C2['created_at'])}: '{q(O.GDD_C2['body'], 'keep the GDD at 7 for now')}'. "
    "The page's monster roster and its boss mode are a known base issue (SC-58) and stay off every Expected line.",
    "VERIFIED: quotes cut from the base records (tools/hg.py), tags removed", "YES (Confluence unscoped)", "{F:notes}",
    f"confluence/{O.GDD['_src']}; confluence/{O.GDD_C1['_src']}; confluence/{O.GDD_C2['_src']}")

bw = O.base("brian_winfail")
add("winfail", "Brian's statement of the win and fail conditions to PlayableX", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_read_thread",
    bw["id"], 'search "fail condition"',
    f"Posted {O.when(bw['ts'])} by {bw['user']} (Brian Foster) in the thread under {O.VENDOR_CH}/{bw['thread_ts']}. Quote: '{bw['text']}'",
    BASE_SLACK, "YES (channel member; can-see)", "—", bw["src"])

fs = O.base("fred_scenario1"); fr = O.base("fred_retention"); p22r = O.base("purpose_robert_22sep"); p22j = O.base("purpose_julia_22sep")
p22q = O.base("julia_shuriken_idea"); p22m = O.base("purpose_robert_matter"); p22s = O.base("robert_remain")
add("purpose", "What Scenario 1 is for", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_conversations_history, slack_read_thread", fr["id"],
    '{F:notes} ("which scenario we picked and what it is for"); search "Scenario 1 is a good bet"',
    f"Posted {O.when(fr['ts'])} by {fr['user']} (Frederick Stone), a root post with {fr['reply_count']} replies. Quote: "
    f"'{q(fr['text'], 'I think Scenario 1 is a good bet for filtering out the players that won' + chr(39) + 't like our game, while remaining true to our core game play.')}' "
    f"The team's thread of {O.day_pt(p22r['ts'])} in #zombie-design ({O.DESIGN_CH}), in order: {p22r['id']} by {p22r['user']} (Robert): '{p22r['text']}'; "
    f"{p22j['id']} by {p22j['user']} (Julia Lawson): '{p22j['text']}'; {p22q['id']} by {p22q['user']} (Julia Lawson): '{p22q['text']}'; "
    f"{p22m['id']} by {p22m['user']} (Robert): '{p22m['text']}'; {p22s['id']} by {p22s['user']} (Robert): '{p22s['text']}'. With the ask's 'Write it for the game as it is today' ({{F:ask}}), "
    "the purpose is one: filter for the players who will like the game, true to the core game play, testing the game in its current form and its audience fit; the hardcore-friendly line is walked back.",
    BASE_SLACK, "YES (channel member; can-see)", "{F:notes}, {F:ask}", f"{fr['src']}; {p22r['src']}; {p22j['src']}; {p22q['src']}; {p22m['src']}; {p22s['src']}")
add("scenario", "The scenario picked: Scenario 1", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_read_thread", fs["id"],
    '{F:purpose} (its thread); search "lets go with Scenario 1"',
    f"Posted {O.when(fs['ts'])} by {fs['user']} (Frederick Stone) as a reply in the thread under {fr['id']}. Quote: '{q(fs['text'], 'lets go with Scenario 1.')}' "
    f"The same message suggests items and zombies before Robert picked them: '{q(fs['text'], 'I think grenade (powerful), couch (splash damage), plush doll (weak but potentially funny), would be a good start.')}'",
    BASE_SLACK, "YES (channel member; can-see)", "{F:purpose}", fs["src"])

fp = O.base("fred_pause"); vn = O.base("vendor_nov3")
add("pause", "Frederick's request to pause the playable", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_conversations_history", fp["id"],
    'search "pause development of the playable"',
    f"Posted {O.when(fp['ts'])} by {fp['user']} (Frederick Stone), a root post with {fp['reply_count']} reply. Quote: '{fp['text']}'",
    BASE_SLACK, "YES (channel member; can-see)", "—", fp["src"])
add("nov3", "The new start date: 3 November", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_read_thread", vn["id"],
    '{F:ask} ("PlayableX are holding Nov 3 for us"); {F:pause} (its thread); search "November 3rd"',
    f"Posted {O.when(vn['ts'])} by {vn['user']} as the reply in the thread under {fp['id']}. Quote: '{vn['text']}' (a start date, not yet reached at the clock)",
    BASE_SLACK, "YES (channel member; can-see)", "{F:ask}, {F:pause}", vn["src"])

vm = O.base("vendor_music_rule")
add("music", "PlayableX's rule on when the music may start", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_search_public_and_private, slack_conversations_history", vm["id"],
    '{F:notes} ("their rule from last time about when the music may start"); search "music has to start"',
    f"Posted {O.when(vm['ts'])} by {vm['user']}, a root post from the first playable. Quote: '{q(vm['text'], 'music has to start after first click as a rule')}'",
    BASE_SLACK, "YES (channel member; can-see)", "{F:notes}", vm["src"])

tb = O.base("brian_zip1"); z2 = O.base("brian_zip2"); z3 = O.base("brian_pack3"); vd = O.base("vendor_duck"); vz = O.base("vendor_zombie_ask"); vb = O.base("vendor_blank_scene")
VB_SENT = vb["text"][vb["text"].index("We"):vb["text"].index("correctly.") + len("correctly.")]
add("sent", "What Brian sent PlayableX and what they said about it", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_read_thread",
    f"{O.VENDOR_CH}/{tb['thread_ts']}", 'search "package up assets"',
    f"Thread under Frederick's message of {O.day_pt(tb['thread_ts'])}. Brian Foster, {O.when(tb['ts'])}: '{q(tb['text'], 'You can access the game assets here.')}' with file {tb['files'][0]}. "
    f"{vd['user']}, {O.when(vd['ts'])}: '{q(vd['text'], 'At this stage, the only missing piece seems to be the duck asset used in the reference.')}' "
    f"Brian Foster, {O.when(z2['ts'])}: '{z2['text']}' with file {z2['files'][0]}. {vb['user']}, {O.when(vb['ts'])}: '{q(vb['text'], VB_SENT)}' "
    f"Brian Foster, {O.when(z3['ts'])}: file {z3['files'][0]}. "
    f"{vz['user']}, {O.when(vz['ts'])}: '{q(vz['text'], 'We have reviewed the assets.')}' and '{q(vz['text'], 'Select the primary animation you want us to use (attack, idle, die, or walk), and')}' "
    f"'{q(vz['text'], 'Specify the 4 zombie characters to which this animation should be applied.')}' File names are metadata; no step reads a file's content.",
    BASE_SLACK, "YES (channel member; can-see)", "—", f"{tb['src']}; {vd['src']}; {z2['src']}; {vb['src']}; {z3['src']}; {vz['src']}")

att = json.loads(O.HOLD["attendees_json"])
add("hold", "The kickoff hold and who is on it", "Calendar (Julia's own)", "gcal_search_events, gcal_list_events, gcal_get_event", O.HOLD_ID,
    '{F:notes} ("Everyone on the kickoff hold"); search "playable kickoff"',
    f"Event '{O.HOLD['summary']}', starts {O.when(O.HOLD['start_ts'])}, ends {O.when(O.HOLD['end_ts'])}, organizer {O.HOLD['organizer_email']}, "
    f"created {O.when(O.HOLD['created'])}, sequence {O.HOLD['sequence']}. Attendees: {', '.join(a['email'] for a in att)}. "
    f"Other than Julia: {', '.join(a['email'] for a in att if a['email'] != O.JULIA)}.",
    "VERIFIED: fields cut from the SQL row; the start is a semantic future date", "YES (own calendar; check-sql)", "{F:notes}",
    O.sql("gcal.gcal_events", event_id=O.HOLD_ID))

add("contact", "PlayableX's intake address", "Contacts (unscoped)", "contacts_search_contacts", "the contact named PlayableX Intake",
    '{F:notes} ("PlayableX through their intake address, which is in Contacts")',
    f"Contact '{O.CONTACT['first_name']} {O.CONTACT['last_name']}', job '{O.CONTACT['job']}', email {O.CONTACT['email']}",
    "VERIFIED: fields cut from the SQL row", "YES (Contacts unscoped)", "{F:notes}", O.sql("contacts.contacts", contact_id=O.CONTACT["contact_id"]))

add("todo", "The Design team's Todo status", "Linear (unscoped)", "linear_list_issue_statuses, linear_list_issues", "team Design, key DES",
    '{F:ticket} (the tickets\' team)', "The Design team has a status named Todo: base ticket DES-304 'Questions and Analyzes' is in it. The seeded tickets carry Done and In Progress.",
    "VERIFIED: state_id 'Todo' on DES-304 re-read through tools/hg.py", "YES (Linear unscoped)", "{F:ticket}", "linear/data.json/issues/769")

# ------------------------------------------------------------------ the 96 lines
DECIDER = {"W": ["sent"], "A1": ["a1", "formats"], "A2": ["a2"], "C1": ["c1", "c4"], "C4": ["c4"], "C2": ["c2", "notes"], "VIS": [], "READY": []}
for l in O.LINES:
    dep = ["pack", "ticket"] + DECIDER[l["cls"]]
    verdict = f"State {l['state']}" + (f"; what is owed: {l['owed']}; who has it: {l['who']}" if l["state"] == "Owed" else "") + \
              f"; Board set {l['board'] or 'empty'}."
    add("line:" + l["name"], f"{l['ticket']} {l['name']}: Brian's note and the line's state", "Linear (unscoped)", "linear_get_issue, linear_list_comments",
        l["ticket"], "{F:pack}",
        f"Title '{l['name']}', ticket state {l['ticket_state']}, parent {O.PACK_TICKET}. One comment, by Brian Foster, created {O.when(l['note_at'])}: '{l['note']}' {verdict}",
        "VERIFIED: title, state and comment cut from the SQL rows; the line's state recomputed by oe_gen/model.py from the note and the deciding record, equal to solver/truth.json",
        "YES (Linear unscoped)", ", ".join("{F:%s}" % d for d in dep), f"SQL L{l['ticket_line']}, SQL L{l['note_line']}")

# ------------------------------------------------------------------ results
add("absence", f"Nothing later about the {len(O.ABSENCE_TARGETS)} Delivered and Ready lines no later record touches", f"Slack (every container Julia can open) and the overlay; controls {rc['id']}, {O.A2['id']}",
    "slack_search_public_and_private, slack_conversations_history", "—", "{F:pack}",
    "ABSENCE_PLACEHOLDER", "ABSENCE evidence_check: oe_gen/out/absence_check.json", "YES (channel member, DM party; can-see, check-sql)", "{F:pack}", f"oe_gen/out/absence_check.json; controls {rc['id']}, {bow['id']}")

LINES_SRC = f"SQL L{O.LINES[0]['ticket_line']} to SQL L{O.LINES[-1]['note_line']} (the 96 tickets and notes); oe_gen/model.py; solver/truth.json"
def group_list(ls): return ", ".join(f"{l['name']} {l['ticket']}" for l in ls)
add("delivered", "Delivered lines", "Derived (recorded calculation)", "none", "—", "{F:notes} (the Delivered rule)",
    f"8: {group_list(O.by_state('Delivered'))}. Each ticket is Done and its note says the file went to PlayableX; PlayableX reviewed the assets.",
    "VERIFIED by recorded calculation over the 96 line facts; 8 equals solver/truth.json", "n/a (derived)", "{F:notes}, {F:ticket}, {F:sent}", LINES_SRC)
add("ready", "Ready lines", "Derived (recorded calculation)", "none", "—", "{F:notes} (the Ready rule)",
    f"{O.COUNTS['Ready']}: {group_list(O.by_state('Ready'))}. Of these, {group_list(O.members('C1'))} have new colour versions (Robert, 29 Sep) and were sent again on Tue Sep 30 "
    "(Brian's log: 'they replace Thursday's'), so they are current and in the folder.",
    f"VERIFIED by recorded calculation over the 96 line facts; {O.COUNTS['Ready']} equals solver/truth.json", "n/a (derived)",
    "{F:notes}, {F:absence}, {F:c1}, {F:c4}", LINES_SRC)
owed_txt = []
for key, head, ls in O.OWED_GROUPS:
    if key == "VIS":
        by = {}
        for l in ls: by.setdefault((l["owed"], l["who"]), []).append(l)
        for (owed, who), g in by.items(): owed_txt.append(f"{len(g)} owed {owed}, with {who}: {group_list(g)}")
    else:
        owed_txt.append(f"{len(ls)} ({head}) owed {ls[0]['owed']}, with {ls[0]['who']}: {group_list(ls)}")
add("owed", "Owed lines, what is owed and who has it", "Derived (recorded calculation)", "none", "—", "{F:notes} (the Owed rule and the later-word rule)",
    f"{O.COUNTS['Owed']}: " + ". ".join(owed_txt) + f". By person: Brian {O.WHO_COUNTS['Brian']}, Claire {O.WHO_COUNTS['Claire']}, Calvin {O.WHO_COUNTS['Calvin']}, Martin {O.WHO_COUNTS['Martin']}.",
    f"VERIFIED by recorded calculation over the 96 line facts; {O.COUNTS['Owed']} and the four holder counts equal solver/truth.json", "n/a (derived)",
    "{F:notes}, {F:a1}, {F:formats}, {F:a2}, {F:c4}, {F:c2}", LINES_SRC)
add("counts", "The count for each state", "Derived (recorded calculation)", "none", "—", '{F:ask} ("the count for each state")',
    f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}; 96 lines in all.",
    f"VERIFIED by recorded calculation: {O.COUNTS['Delivered']} + {O.COUNTS['Ready']} + {O.COUNTS['Owed']} = 96, recomputed from the rows", "n/a (derived)", "{F:delivered}, {F:ready}, {F:owed}", LINES_SRC)
add("boardset", "Board set for each line", "Derived (recorded calculation)", "none", "—", "{F:notes} (the Board set rule)",
    f"Default on 8: {', '.join(O.EIGHT)}. Extra on the other 76 board items. Empty on the 12 lines that are not board items: {names(O.NOT_BOARD)}.",
    "VERIFIED by recorded calculation: Kind 'Board item' on 84 rows, 8 of them in the eight", "n/a (derived)", "{F:notes}, {F:pack}, {F:eight}", f"{O.sql('gsheets.sheets_sheets', spreadsheet_id=O.PACK_ID)}; oe_gen/model.py; solver/truth.json")
add("recipients", "Who gets the files", "Derived (recorded calculation)", "none", "—", '{F:notes} ("Sharing: both files, view only")',
    f"{', '.join(a['email'] for a in att if a['email'] != O.JULIA)} and {O.CONTACT['email']}, each as a reader; Julia owns both files.",
    "VERIFIED: addresses cut from the event and the contact rows", "n/a (derived)", "{F:notes}, {F:hold}, {F:contact}", f"{O.sql('gcal.gcal_events', event_id=O.HOLD_ID)}, {O.sql('contacts.contacts', contact_id=O.CONTACT['contact_id'])}")

# ------------------------------------------------------------------ destinations
add("drive", "Julia's Drive, where both files go", "Drive (Julia's own)", "gdocs_create_document, gsheets_create_spreadsheet", "Julia's own Drive",
    'prompt ("my Drive"); {F:ask} ("both in your Drive")',
    f"Julia's root folder {O.ROOT_FOLDER['id']} is named '{O.ROOT_FOLDER['name']}' and owned by {O.ROOT_FOLDER['owner_email']}. A document or spreadsheet Julia creates is hers and sits in her Drive.",
    "VERIFIED: folder fields re-read through tools/hg.py", "YES (owner; can-see)", "{F:ask}", f"gdrive/{O.ROOT_FOLDER['_src']}")
add("channel", "The PlayableX channel, where the links go", f"Slack (the PlayableX channel, {O.VENDOR_CH})", "slack_search_channels, slack_send_message", O.VENDOR_CH,
    'prompt ("the PlayableX channel"); {F:ask} ("post both links in the PlayableX channel"); search "PlayableX"',
    f"Channel {O.VENDOR_CH}, private, the one channel shared with PlayableX; Julia is a member and has posted there (her brief for the first playable, {O.base('julia_dd_brief')['id']}, "
    f"{O.day_pt(O.base('julia_dd_brief')['ts'])}).",
    "VERIFIED: channel and membership from persona_view can-see; her post re-read through tools/hg.py", "YES (channel member; can-see)", "{F:ask}", O.base("julia_dd_brief")["src"])

N = {f["key"]: f"F{i + 1}" for i, f in enumerate(FACTS)}
def res(s): return re.sub(r"\{F:([^}]+)\}", lambda m: N[m.group(1)], s)
for f in FACTS:
    f["F"] = N[f["key"]]
    for k in ("origin", "depends", "expected", "fact"): f[k] = res(f[k])
def F(key): return N[key]
def FL(name): return N["line:" + name]

if __name__ == "__main__":
    print(len(FACTS), "facts;", sum(len(f["expected"]) for f in FACTS), "chars of expected data")
    for f in FACTS[:30]: print(f["F"], f["key"], "|", f["locator"][:44], "|", f["origin"][:70])
