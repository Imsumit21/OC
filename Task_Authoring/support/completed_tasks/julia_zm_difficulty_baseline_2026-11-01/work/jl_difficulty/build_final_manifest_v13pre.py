"""Final manifest = draft + ids the SQL settled (Gmail message rows) + facts + integration exceptions + design_delta."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WF = ROOT / 'task_inputs/Working_Files'
M = json.load(open(HERE / 'minted_ids.json'))
S = json.load(open(HERE / 'sql_ids.json'))
draft_text = (WF / '01_Hardness_Manifest.draft.json').read_text()
sql = (ROOT / 'task_inputs/01_Universe_Inject.sql').read_text()

JL = 'julia.lawson@harmonygames.co'
G1_OLD = f"{JL}/{M['G_BUILD']['gmail_id']}"
G2_OLD = f"{JL}/{M['G_BUILD_RE']['gmail_id']}"
G1_MSG = f"{JL}/{M['G_BUILD']['message_id']}"
G2_MSG = f"{JL}/{M['G_BUILD_RE']['message_id']}"
assert f"VALUES ('{G1_MSG}'" in sql and f"VALUES ('{G2_MSG}'" in sql
# the thread row keeps G1_OLD; the draft's seeded/version references move to the message rows that carry text and date
text = draft_text.replace(G2_OLD, G2_MSG).replace(G1_OLD, G1_MSG)
d = json.loads(text)

note = {k: v['id'] for k, v in M['LIN_NOTES'].items()}
d['facts'] = [
    {"key": "iOS 0.3.49", "value": "0.3.49", "kind": "version", "must_appear_in": [G1_MSG]},
    {"key": "Android 0.3.133", "value": "0.3.133", "kind": "version", "must_appear_in": [G1_MSG]},
    {"key": "ZOM-173", "value": "match3d#243", "kind": "id", "home_ids": [note['ZOM-173'], note['ZOM-307']], "must_appear_in": [note['ZOM-173']]},
    {"key": "ZOM-312", "value": "match3d#265", "kind": "id", "home_ids": [note['ZOM-312']], "must_appear_in": [note['ZOM-312']]},
    {"key": "ZOM-292", "value": "match3d#267", "kind": "id", "home_ids": [note['ZOM-292']], "must_appear_in": [note['ZOM-292']]},
    {"key": "ZOM-387", "value": "match3d#319", "kind": "id", "home_ids": [note['ZOM-387']], "must_appear_in": [note['ZOM-387']]},
    {"key": "ZOM-352", "value": "match3d#282", "kind": "id", "home_ids": [note['ZOM-352']], "must_appear_in": [note['ZOM-352']]},
]
d['integration_exceptions'] = [
    {"record_id": M['GCAL_TUNING']['ical_uid'],
     "reason": "no_notify: Leonard put the Oct 6 tuning session straight on the four calendars and announced it on the card "
               "(rule 7 names the invite); the attendee list lives only on the calendar (design C4/T13)"}]
d['design_delta'] = [
    {"id": "K4", "change": f"seeded_ids {G1_OLD} (thread) -> {G1_MSG} (first message row)",
     "reason": "the store builds text and its date live on the message row; the thread row carries only a snippet"},
    {"id": "K5", "change": f"seeded_ids {G2_OLD} -> {G2_MSG} (reply row, thread {G1_OLD})",
     "reason": "the reply has no thread of its own; it is a message row inside the first message's thread"},
    {"id": "H2", "change": "seeded_ids moved to the two message rows (as K4/K5)", "reason": "same as K4/K5"},
    {"id": "PRC_244", "change": "the minted key PRC_244 now holds Blake's comment on match3d#401 (#401#c_2), not a #244 comment",
     "reason": "design v4: no #244 seed (the level drop is live in the code); the key name was kept to keep builder ids stable"},
]
(WF / '01_Hardness_Manifest.json').write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
print('ok', len(d['facts']), 'facts')
