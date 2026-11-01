"""Final manifest = draft + ids the SQL settled (Gmail message ids for chronology) + facts + integration exceptions."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WF = ROOT / 'task_inputs/Working_Files'
M = json.load(open(HERE / 'minted_ids.json'))
S = json.load(open(HERE / 'sql_ids.json'))
d = json.loads((WF / '01_Hardness_Manifest.draft.json').read_text())

DG = 'douglas@harmonygames.co'
sql = (ROOT / 'task_inputs/01_Universe_Inject.sql').read_text()


def msg_id(key):
    """Douglas's copy of a seeded mail: '<mailbox>/<Message-ID>' (the row that carries the date)."""
    thread = S['gmail_threads'][key][DG]
    import re
    m = re.search(r"VALUES \('(" + re.escape(DG) + r"/<[^']+>)', '" + re.escape(thread) + "'", sql)
    return m.group(1)


LEO_MSG = msg_id('G_LEO')
# hardening r1: Arthur's amendment is a reply inside Leonard's thread; the draft already addresses it by its message row
AMEND_MSG = f"{DG}/{M['G_AMEND']['message_id']}"
assert f"VALUES ('{AMEND_MSG}', '{S['gmail_threads']['G_LEO'][DG]}'" in sql and LEO_MSG != AMEND_MSG

note = {k: v['id'] for k, v in M['LIN_NOTES'].items()}
LOG = M['SHEET_DEPLOYLOG']['id']
d['facts'] = [
    {"key": "ZOM-336", "value": "match3d-backend#40", "kind": "id", "home_ids": [note['ZOM-336']], "must_appear_in": [note['ZOM-336']]},
    {"key": "ZOM-392", "value": "match3d-backend#41", "kind": "id", "home_ids": [note['ZOM-392']], "must_appear_in": [note['ZOM-392']]},
    {"key": "ZOM-518", "value": "match3d-backend#43", "kind": "id", "home_ids": [note['ZOM-518']], "must_appear_in": [note['ZOM-518']]},
    {"key": "ZOM-435", "value": "match3d-backend#51", "kind": "id", "home_ids": [note['ZOM-435']], "must_appear_in": [note['ZOM-435']]},
    {"key": "ZOM-557", "value": "match3d-backend#54", "kind": "id", "home_ids": [note['ZOM-557']], "must_appear_in": [note['ZOM-557']]},
    {"key": "ZOM-499", "value": "match3d-backend#44", "kind": "id", "home_ids": [note['ZOM-499']], "must_appear_in": [note['ZOM-499']]},
    {"key": "ZOM-444", "value": "match3d-backend#47", "kind": "id", "home_ids": [note['ZOM-444']], "must_appear_in": [note['ZOM-444']]},
    {"key": "ZOM-487", "value": "match3d-backend#48", "kind": "id", "home_ids": [note['ZOM-487']], "must_appear_in": [note['ZOM-487']]},
]
d['integration_exceptions'] = [
    {"record_id": M['GCAL_FREEZE']['ical_uid'],
     "reason": "no_notify: Arthur's freeze hold on the beta crew's calendars; he announced it in #zombie-match3d instead, so "
               "the pulled-in time lives only on the calendar (design T2)"}]
for f in d['ask_fragments']:
    if f['id'] == 'K12':
        f['delegated_by_record'] = LEO_MSG
        f['seeded_ids'] = f['seeded_ids'] + [LEO_MSG]
for a in d['anchors']:
    if a['id'] == 'A2':
        a['locator'] = LEO_MSG
d['design_delta'] = [
    {"id": "K12", "change": f"delegated_by_record {DG}/{M['G_LEO']['gmail_id']} (thread) -> {LEO_MSG} (message)",
     "reason": "the delegating words are in the message row's body; the thread row carries only a snippet"},
    {"id": "A2", "change": f"locator {DG}/{M['G_LEO']['gmail_id']} (thread) -> {LEO_MSG} (message)", "reason": "same as K12"},
    {"id": "K4", "change": f"container: Arthur's own thread {DG}/{M['G_AMEND']['gmail_id']} -> Leonard's go/no-go thread "
                          f"{S['gmail_threads']['G_LEO'][DG]}; locator {AMEND_MSG} (reply-all, In-Reply-To Leonard's message)",
     "reason": "hardening r1 (01a_Hardening_Report.md): the six baseline runs never searched mail beyond Leonard; the "
               "amendment now sits inside the thread the prompt names, so it is found by reading that thread in full"},
    {"id": "K14", "change": f"new fragment: Arthur's reply {M['CC_ART']['id']} on the ZM beta page (ZOM-487 import)",
     "reason": "hardening r1: second independent decisive fact, on a different row, behind the page's comment thread"},
    {"id": "K15", "change": f"new fragment: Arthur's inline review comment {M['RC_ART46']['id']} on #46 (ZOM-537 import); "
                           "hardening r2 moved it here from r1's Slack thread reply on the ask",
     "reason": "hardening r2 (01a_Hardening_Report.md §15): all six r1 baseline runs opened the ask's thread (reply_count 1 "
               "on the first message read); inline review comments were read in 1 of 6 runs for #46"},
    {"id": "K16", "change": f"new fragment: second point of Arthur's reply-all {AMEND_MSG} (analytics events table import is part "
                           "of ZOM-444's and ZOM-436's server change, loadout table import of ZOM-531's; both dev only)",
     "reason": "hardening r3 (01a_Hardening_Report.md): the r2 baseline's per-run SD was ~0.02-0.05 under an atomic per-ticket "
               "rubric; the thread read (10 of 20 runs across three baselines) is the one habit near 50%, so it now decides "
               "three ticket rows as well as the 547/553 exclusion"},
    {"id": "K17", "change": f"new fragment: the reviewer's inline review comment {M['RC_C38']['id']} on #38 (ZOM-459 import)",
     "reason": "hardening r3: inline comments on #37-#42 were read in 4 of 13 r1/r2 runs, independent of the thread read"},
    {"id": "K18", "change": f"new fragment: Douglas's inline review comment {M['RC_DG39']['id']} on #39 (ZOM-509 import)",
     "reason": "hardening r3: same habit as K17, a second row on it"},
]
(WF / '01_Hardness_Manifest.json').write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
print('ok', len(d['facts']), 'facts', AMEND_MSG, LEO_MSG)
