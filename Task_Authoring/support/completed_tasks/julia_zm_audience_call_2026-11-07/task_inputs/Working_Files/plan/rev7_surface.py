"""rev7 gradable surface (S6b): 82-session truth, two-sided K3, R_G, R_T, retention cut-off. Fact slots only.
Run from the workspace root: python -X utf8 Task_Authoring/task_inputs/Working_Files/plan/rev7_surface.py"""
import json, pathlib

WF = pathlib.Path('Task_Authoring/task_inputs/Working_Files')
P = WF / '01_Gradable_Surface.json'
sur = json.loads(P.read_text(encoding='utf-8'))
truth = json.loads((WF / 'solver' / 'truth.json').read_text(encoding='utf-8'))
keys = [k for k in truth if k not in ('panel', 'retention')]
assert len(keys) == 82

MS = ["R_K1", "R_K3", "R_K4", "R_K5", "R_G", "R_T"]
R5 = "the session's own records say it counts; the verdict needs a record in another service joined to it"


def slot(id, title, weight, wk, why, cls, sel, role, mech, fact, **kw):
    d = dict(id=id, title=title, weight=weight, work_kind=wk, work_reason=why, **{"class": cls}, selector=sel,
             role=role, mechanisms=mech, fact_id=fact)
    d.update(kw)
    return d


slots = [
    slot("S-K1a", "the 13 sessions of the one gathering at Claire's are not counted", 5, "multi_source_reconciliation", R5,
         "direct", ["field", "ZOM-607", "verdict"], "exception", ["R_K1"], "verdict:K1", singled_out_by="F-COACH"),
    slot("S-K1b", "the not-counted reason for the 13 sessions of the one gathering at Claire's names the deciding fact", 3,
         "interpretation", "the reason has to be read from the deciding record, not from a neighbouring rule", "write_content",
         ["reason_matches", "ZOM-613", "coach|walk|brief|explain|show|told|guid"], "core", ["R_K1"], "reason:K1"),
    slot("S-K3a", "the Samsung session on an SM-A546E counts", 5, "multi_source_reconciliation",
         "the gate, the Done ticket and Arthur's PR note all point to exclusion; the on-device pass sits in another channel and a sheet that names the phone by model number",
         "direct", ["field", "ZOM-588", "verdict"], "exception", ["R_K3"], "verdict:K3:588", singled_out_by="H-GATE"),
    slot("S-K3b", "the Samsung session on a Galaxy phone in the second wave counts", 5, "multi_source_reconciliation",
         "the same pass has to be carried to every Samsung session, including the later ones, by the gate's coverage line",
         "direct", ["field", "ZOM-641", "verdict"], "exception", ["R_K3"], "verdict:K3:641", singled_out_by="H-GATE"),
    slot("S-K4a", "the 9 sessions of Brian's batch are not counted", 5, "multi_source_reconciliation", R5,
         "direct", ["field", "ZOM-568", "verdict"], "exception", ["R_K4"], "verdict:K4", singled_out_by="F-INDUSTRY"),
    slot("S-K4b", "the not-counted reason for the 9 sessions of Brian's batch names the deciding fact", 3, "interpretation",
         "the reason has to be read from the deciding record, not from a neighbouring rule", "write_content",
         ["reason_matches", "ZOM-573", "game industry|game-industry|work in games|works in games|industry"], "core",
         ["R_K4"], "reason:K4"),
    slot("S-K5a", "the 13 sessions on build 1943 are not counted", 5, "multi_source_reconciliation", R5,
         "direct", ["field", "ZOM-579", "verdict"], "exception", ["R_K5"], "verdict:K5", singled_out_by="H-GATE"),
    slot("S-K5b", "the not-counted reason for the 13 sessions on build 1943 names the deciding fact", 3, "interpretation",
         "the reason has to be read from the deciding record, not from a neighbouring rule", "write_content",
         ["reason_matches", "ZOM-585", "1943|dev build|non-store|not a store|never went through"], "core", ["R_K5"],
         "reason:K5"),
    slot("S-Ga", "the session of the player who is a live ops producer at a mobile games studio is not counted", 5,
         "multi_source_reconciliation", "nothing in the session's records names the job; it is joined from Julia's contacts",
         "direct", ["field", "ZOM-622", "verdict"], "exception", ["R_G"], "verdict:G:622", singled_out_by="F-PLAYERS"),
    slot("S-Gb", "the session of the player who is a QA tester at a console games publisher is not counted", 5,
         "multi_source_reconciliation", "nothing in the session's records names the job; it is joined from Julia's contacts",
         "direct", ["field", "ZOM-598", "verdict"], "exception", ["R_G"], "verdict:G:598", singled_out_by="F-PLAYERS"),
    slot("S-Ta", "Owen's late casual session (Ayşe Polat, Sun Sep 28) gets a ticket", 5, "tracing",
         "the session exists only inline in a late reply under an older form mail; no ticket, Log row or Doc carries it",
         "write_content", ["text", "new_tickets", "Ay[sş]e Polat"], "exception", ["R_T"], "late:T1", singled_out_by="F-LATE"),
    slot("S-Tb", "Owen's late RPG session (Daniel Hughes, Sun Sep 28) gets a ticket", 5, "tracing",
         "the session exists only inline in a late reply under an older form mail; no ticket, Log row or Doc carries it",
         "write_content", ["text", "new_tickets", "Daniel Hughes"], "exception", ["R_T"], "late:T2", singled_out_by="F-LATE"),
    slot("S-H1", "casual leads over counted sessions", 5, "deeper_reasoning",
         "the single audience call rests on every session verdict and the lead test", "write_content",
         ["text", "memo", "casual.{0,80}(?:lead|ahead|higher)|(?:lead|ahead|higher).{0,80}casual"], "core", MS, "audience_lead"),
    slot("S-G1", "45 sessions are counted", 5, "multi_source_reconciliation",
         "the total depends on six independent decisions across services", "aggregate", ["total", "counted"], "volume",
         MS, "counted_total", volume_for=["register:verdict"]),
    slot("S-G2", "casual mean 3.83 over 27 and RPG mean 3.50 over 18 counted sessions", 5, "multi_source_reconciliation",
         "the means exist only after the reconciled session set is fixed", "write_content",
         ["text", "memo", "3\\.83.*3\\.50?\\b|3\\.50?\\b.*3\\.83"], "core", MS, "means"),
    slot("S-DEC", "the reply to Leonard says hold", 3, "interpretation", "applies the stated mapping to the audience call",
         "write_content", ["delivery", "slack_channel_post", "C090N54TG79", "hold"], "core", MS, "decision_reply"),
    slot("S-BRIAN", "the message to Brian in #zombie-design says hold", 3, "interpretation",
         "carries the decision to the person whose work it stops", "write_content",
         ["text", "slack", "(?:brian|EMPLOYEE_0026).{0,240}(?:hold|stop|pause)|(?:hold|stop|pause).{0,240}(?:brian|EMPLOYEE_0026)"],
         "core", MS, "decision_brian"),
    slot("S-ST1", "37 tickets move to Canceled", 3, "limited_reconciliation",
         "state writes follow the verdicts and the log note's mapping", "write_content",
         ["text", "tickets", "(?:cancell?ed\\s+(?:done\\s+)*){36}cancell?ed"], "core", ["R_K1", "R_K3", "R_K4", "R_K5", "R_G"],
         "state_canceled"),
    slot("S-ST2", "43 existing tickets move to Done", 3, "limited_reconciliation",
         "state writes follow the verdicts and the log note's mapping", "write_content",
         ["text", "tickets", "(?:done\\s+(?:cancell?ed\\s+)*){42}done"], "core", ["R_K1", "R_K3", "R_K4", "R_K5", "R_G"],
         "state_done"),
    slot("S-F1", "technical drops carry a re-run note", 3, "interpretation",
         "applies Robert's handling to the sessions it covers", "write_content",
         ["text", "rerun_notes", "re-?run|run (?:it|them|this|these|that) again"], "core", ["R_F"], "rerun"),
    slot("S-D1", "panel context: 3.33 over 9 players after the void", 3, "calculation",
         "one void applied under Leonard's panel reply", "write_content",
         ["text", "memo", "3\\.33?.*\\b9\\b|\\b9\\b.*3\\.33?"], "core", ["R_D"], "panel"),
    slot("S-E1", "retention context: install-weighted D7 of 10.47 % over the mature cohorts from 2025-07-24", 3,
         "calculation", "weighted mean over the rule's cohorts after Vincent's later cut-off", "write_content",
         ["text", "memo", "\\b10\\.(?:47|5)\\b"], "core", ["R_E"], "retention"),
    slot("S-O1", "an ordinary Pixel session stays counted", 3, "comparison",
         "control: Android, and the gate names only Samsung", "direct", ["field", "ZOM-643", "verdict"], "sample", [],
         "verdict:ZOM-643", group="register:verdict"),
    slot("S-O2", "another session of the same day stays counted", 3, "comparison",
         "control: same date as the gathering, another observer", "direct", ["field", "ZOM-605", "verdict"], "sample", [],
         "verdict:ZOM-605", group="register:verdict"),
    slot("S-M1", "the memo exists", 1, "lookup", "delivery only", "delivery", ["text", "memo", "audience"], "core", [],
         "memo_exists"),
    slot("S-L1", "the reply sits in Leonard's thread", 1, "lookup", "delivery only", "delivery",
         ["delivery", "slack_thread", "1759266627.418203"], "core", [], "reply_thread"),
]

sur['_note'] = ("rev7 surface (S0r delta over rev 5.1). Fact slots only; titles state facts, no criterion text. Two "
                "weight-5 atomic rows per new or rebuilt trap where the surface supports it (K3 two-sided, R_G, R_T); "
                "S-R1 dropped because the two late sessions get ticket keys the design cannot know in advance.")
sur['revision'] = 'rev7-design'
sur['truth_keys'] = keys
reg = sur['deliverables']['register']
reg['key_regex'] = 'ZOM-(?:5(?:6[89]|[7-9]\\d)|6[0-4]\\d|65\\d)|T[12]'
sur['deliverables']['new_tickets'] = {'kind': 'json_text', 'tool': 'linear_create_issue'}
SPANS = {"S-K1a": "fill in the register tab in my audience sessions workbook",
         "S-K1b": "fill in the register tab in my audience sessions workbook",
         "S-K3a": "fill in the register tab in my audience sessions workbook",
         "S-K3b": "fill in the register tab in my audience sessions workbook",
         "S-K4a": "fill in the register tab in my audience sessions workbook",
         "S-K4b": "fill in the register tab in my audience sessions workbook",
         "S-K5a": "fill in the register tab in my audience sessions workbook",
         "S-K5b": "fill in the register tab in my audience sessions workbook",
         "S-Ga": "fill in the register tab in my audience sessions workbook",
         "S-Gb": "fill in the register tab in my audience sessions workbook",
         "S-Ta": "close out the session tickets", "S-Tb": "close out the session tickets"}
prompt = pathlib.Path('Task_Authoring/task_inputs/04_Prompt.txt').read_text(encoding='utf-8')
for sl in slots:
    if sl['id'] in SPANS:
        assert SPANS[sl['id']] in prompt, sl['id']
        sl['incorporating_span'] = SPANS[sl['id']]
sur['slots'] = slots
P.write_text(json.dumps(sur, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('slots', len(slots), 'weight', sum(s['weight'] for s in slots))
