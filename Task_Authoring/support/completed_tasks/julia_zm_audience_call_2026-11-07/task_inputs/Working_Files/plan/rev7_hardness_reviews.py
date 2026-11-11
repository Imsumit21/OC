"""Write Working_Files/hardness_reviews/{scenario,injection}.json for rev7 (Guide/Readiness_And_Evidence.md).
Evidence points at frozen rev7 copies under run_forensics/rev7/. Re-run after any manifest, surface or SQL edit.
Run from the workspace root: python -X utf8 Task_Authoring/task_inputs/Working_Files/plan/rev7_hardness_reviews.py"""
import hashlib, json, pathlib, sys

ROOT = pathlib.Path('Task_Authoring/task_inputs')
WF = ROOT / 'Working_Files'
sys.path.insert(0, 'Task_Authoring/tools')
import design_readiness as dr          # noqa: E402
import hardness_v2_check as hv         # noqa: E402
import stage_evidence as se            # noqa: E402

R7 = 'Working_Files/run_forensics/rev7/'
FILES = {'sql': R7 + '01_Universe_Inject.sql', 'truth': R7 + 'truth.json', 'check': R7 + 'solver_check.txt',
         'mb': R7 + '01a_Hardening_Report.rev6.md', 'reach': R7 + 'check_sql.txt'}


def ref(*keys):
    out = []
    for k in keys:
        p = ROOT / FILES[k]
        out.append({'path': FILES[k], 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    return out


def proof(reason, keys, **extra):
    return {'reason': reason, 'evidence': ref(*keys), **extra}


M = {
 'R_K1': dict(init="the 13 sessions of the Sep 26 gathering count: form, ticket and Log all say no coaching",
              dec='julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>',
              decwhy="Claire's Sep 29 mail to Julia says what she did before the group played",
              chron="the form (Sep 26) is older than Claire's mail (Sep 29); tickets are a Sep 30 transcription of the form",
              path="Julia's mailbox: a listing or a search on Claire returns the mail on page 1",
              before='counted', after='notcounted', slots=['S-K1a', 'S-K1b'], ret_q="gmail_search_messages from:claire.morgan",
              ret_ids=['julia.lawson@harmonygames.co/<CAefcc9dd45170efad4834318d398795bc1db8@mail.gmail.com>',
                       'julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>']),
 'R_K3': dict(init="the 13 Samsung sessions are dropped: ZOM-567's Vision Bot pass is editor-only, so no device pass exists",
              dec='3dd0b6d6c52c21cd5bbfcd6d6f5345cd',
              decwhy="Vincent's Sep 29 #zombie-bugs QA matrix post and its sheet: real device yes, SM-A546E, 0.3.127 (127), PASS",
              chron="matrix Sep 29 15:12Z; Vincent's ZOM-567 comment Sep 30 16:50Z and Arthur's rc_27 Sep 30 20:10Z are later but speak only to Vision Bot",
              path="gate Doc 'A pass is a clean test run of the build players get' -> #zombie-bugs (Julia is a member) -> the sheet link in the thread reply",
              before='notcounted', after='counted', slots=['S-K3a', 'S-K3b'], ret_q="slack_conversations_history C08R27X0EAH",
              ret_ids=['3dd0b6d6c52c21cd5bbfcd6d6f5345cd', '3d8e451a198d5d59b39e60064b590305']),
 'R_K4': dict(init="Brian's 9 sessions count: the notes Docs' RPG label is clean and his contacts have no job",
              dec='246d6f4a90620e5dafbb06068f450e46',
              decwhy="Brian's Turkish DM line to Julia says the Kadıköy group all works in mobile games companies",
              chron="Brian's Docs Sep 23 09:05Z; his DM line Sep 23 20:23Z; Leonard's industry rule Sep 24 17:00Z covers sessions already run",
              path="Julia's DM with Brian, page 1 of D076RBM29JS",
              before='counted', after='notcounted', slots=['S-K4a', 'S-K4b'], ret_q="slack_conversations_history D076RBM29JS",
              ret_ids=['246d6f4a90620e5dafbb06068f450e46']),
 'R_K5': dict(init="the 13 sessions on 0.3.127 (1943) count: the build id reads like any other",
              dec='d7122186e361aa99778c65cb1502759d',
              decwhy="Leonard's Sep 25 reply says Android 1943 never went through a store",
              chron="reply Sep 25 17:05Z, before every ticket; the gate Doc's builds clause applies whatever day a session ran",
              path="replies under C090N54TG79/1758581651.167799 in the request's channel",
              before='counted', after='notcounted', slots=['S-K5a', 'S-K5b'], ret_q="slack_conversations_replies C090N54TG79/1758581651.167799",
              ret_ids=['d7122186e361aa99778c65cb1502759d']),
 'R_G': dict(init="only Brian's batch is game industry; ZOM-598 and ZOM-622 count",
             dec='038b5eb5a30326895cb54756',
             decwhy="Julia's contacts give the players' jobs: QA tester at a console games publisher; live ops producer at a mobile games studio",
             chron="contacts added Sep 22 for gift codes; Leonard's industry rule Sep 24 covers sessions already run",
             path="log note 'Players are in my contacts' -> contacts_search_contacts on the notes Doc's Player name",
             before='counted', after='notcounted', slots=['S-Ga', 'S-Gb'], ret_q="contacts_search_contacts 'Alper Koçak' / 'Arda Keskin'",
             ret_ids=['038b5eb5a30326895cb54756', '0810fb8287e489c125fe2cd9']),
 'R_T': dict(init="the read is the 80 ticketed sessions; nothing else exists",
             dec='julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>',
             decwhy="Owen's Sep 30 20:40Z reply in his form thread reports two Sep 28 sessions inline",
             chron="the batch of tickets ends Sep 30 20:2xZ; the reply comes later; the log note says a later form gets a ticket and a log row",
             path="Julia's inbox, newest first, or a thread read of Owen's form mail",
             before='absent', after='counted with a new ticket', slots=['S-Ta', 'S-Tb'], ret_q="gmail_search_messages from:owen.baker",
             ret_ids=['julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>']),
 'R_F': dict(init="no re-run note, or a note on every not-counted ticket",
             dec='167dc58affb9902420038f71d0f5af28',
             decwhy="Robert's DM: technical drops (device or build) get a re-run note, other drops just close",
             chron="Sep 26, before the batch; no later record changes it",
             path="Julia's DM with Robert", before='no notes', after='13 notes on the build-1943 drops', slots=['S-F1'],
             ret_q="slack_conversations_replies D05GU6L0XFH/1758901945.292269", ret_ids=['167dc58affb9902420038f71d0f5af28']),
 'R_D': dict(init="panel mean of all 10 ratings, 3.1", dec='7b38bd6429ce0f189456ac72af02f210',
             decwhy="Leonard: a void rating comes out of both the sum and the count",
             chron="Sep 24 reply; the forward states the one void", path="the panel thread in #zombie-design",
             before='3.1', after='3.33 over 9', slots=['S-D1'], ret_q="slack_conversations_replies C090N54TG79/1758691397.679889",
             ret_ids=['7b38bd6429ce0f189456ac72af02f210']),
 'R_E': dict(init="install-weighted D7 over all 47 mature cohorts, 9.09 %", dec='f_4e21b203a62910bdae0353',
             decwhy="Vincent's Sep 30 note on his KPI tab: use only cohort weeks starting on or after 2025-07-24",
             chron="Robert's method Sep 29 17:30Z; Vincent's scope note Sep 30 10:22Z, later, keeps the method",
             path="the KPI snapshot Vincent shared with Julia, the retention source the team quotes",
             before='9.09', after='10.47', slots=['S-E1'], ret_q="gsheets_get_values f_4e21b203a62910bdae0353 KPI",
             ret_ids=['f_4e21b203a62910bdae0353']),
}
SELECTED = ['R_K3', 'R_G', 'R_T', 'R_K4']
PAIR_TEXT = {
 'R_K3': ("ZOM-588 counted, ZOM-641 dropped by a reader who stops at the first wave", "ZOM-641 counted, ZOM-588 dropped by a reader who matches the sheet model only"),
 'R_G': ("ZOM-622 dropped from its live-ops job, ZOM-598 kept by a reader who discounts console QA", "ZOM-598 dropped, ZOM-622 kept by a reader who discounts live ops"),
 'R_T': ("Ayşe Polat's ticket made, Daniel Hughes's skipped as a 1.5-star abandon", "Daniel Hughes's ticket made, Ayşe Polat's missed by a reader who takes one line"),
 'R_K4': ("ZOM-568 not counted from the DM, reason missing the industry", "reason names the industry while ZOM-568 is still counted"),
}


def review(stage, manifest, surface, sql_text):
    cfg = json.loads((WF / '00_Readiness_Config.json').read_text(encoding='utf-8'))
    ctx = json.loads((WF / '00_Task_Context.json').read_text(encoding='utf-8'))
    rows = {}
    for mid, m in M.items():
        r = {
            'initial_plausible_answer': proof(m['init'], ['mb', 'sql']),
            'deciding_evidence': proof(m['decwhy'], ['sql'], record_id=m['dec']),
            'authority_chronology': proof(m['chron'], ['sql']),
            'fair_discovery_path': proof(m['path'], ['sql', 'reach']),
            'changed_outcome': proof("solver ablation of this rule on the rev7 SQL moves the outcome; see solver_check.txt (b)",
                                     ['truth', 'check'], before=m['before'], after=m['after']),
            'independent_operation': proof("each selected rule has its own deciding record in its own service; a miss of this "
                                           "one leaves the others' verdicts unchanged (solver_check.txt single-rule ablations)",
                                           ['check'], others_solvable_if_missed=[x for x in SELECTED if x != mid]),
            'outcome_slots': m['slots'],
            'channel_kind': 'judgment',
        }
        if stage == 'scenario':
            r['access'] = {'status': 'deferred', 'required_at': 'injection'}
            r['natural_retrieval'] = {'status': 'deferred', 'required_at': 'injection'}
        else:
            r['access'] = proof("persona_view check-sql: every load-bearing id YES for julia_lawson; Contacts, Linear "
                                "and the KPI sheet are unscoped or shared with Julia", ['reach', 'sql'], status='verified')
            r['natural_retrieval'] = proof("the natural call returns the deciding record; it is read in a result the "
                                           "main thread sees, not through a spill", ['reach', 'sql'], query=m['ret_q'],
                                           returned_ids=m['ret_ids'],
                                           assessment="retrieval does not settle it: the record must still be joined to "
                                                      "the sessions and read against the rule (section 5, four A5b checks)")
        if mid in SELECTED:
            lp, rp = PAIR_TEXT[mid]
            r['outcome_pair'] = proof("two existing slots on different facts, each passable without the other",
                                      ['truth', 'check'], slots=m['slots'][:2], left_pass_right_fail=lp,
                                      right_pass_left_fail=rp)
        rows[mid] = r
    adv = hv.run(manifest, sql_text, '', surface)
    disp = {}
    for f in adv['flags'] + adv['unresolved']:
        key = f['check'] + ':' + str(f.get('node') or '-')
        disp[key] = proof("dispositioned in 01_Scenario_Design.md section 5 (liveness and v2 tables): a context rule "
                          "flips a weight-3 slot by the kind of work; weights are not raised (09 gate 8)",
                          ['mb', 'check'], status='accepted')
    return {'schema_version': 1, 'stage': stage, 'task_id': se.task_identity(ROOT), 'revision': cfg['revision'],
            'reviewer': 'Claude Opus 5.5 authoring subagent (rev7 S0r/injection); not an independent or human review',
            'difficulty_mode': ctx['difficulty_mode'], 'diversity_channels': SELECTED, 'mechanisms': rows,
            'dispositions': disp,
            'input_hashes': dr.input_hashes(stage, manifest, surface, sql_text=sql_text),
            'forecast': 'see 01_Scenario_Design.md section 12 (UNCALIBRATED)'}


def main():
    sql_text = (ROOT / '01_Universe_Inject.sql').read_text(encoding='utf-8')
    surface = json.loads((WF / '01_Gradable_Surface.json').read_text(encoding='utf-8'))
    ctx = json.loads((WF / '00_Task_Context.json').read_text(encoding='utf-8'))
    (WF / 'hardness_reviews').mkdir(exist_ok=True)
    for stage, name in (('scenario', '01_Hardness_Manifest.draft.json'), ('injection', '01_Hardness_Manifest.json')):
        man = json.loads((WF / name).read_text(encoding='utf-8'))
        rv = review(stage, man, surface, sql_text)
        (WF / 'hardness_reviews' / (stage + '.json')).write_text(json.dumps(rv, ensure_ascii=False, indent=1) + '\n',
                                                                 encoding='utf-8')
        res = dr.evaluate(stage, man, surface, rv, sql_text=sql_text, task_dir=ROOT, task_id=se.task_identity(ROOT),
                          revision=rv['revision'], difficulty_mode=ctx['difficulty_mode'])
        print(stage, res['verdict'], res['blockers'][:8], 'deferred', len(res['deferred']))


if __name__ == '__main__':
    main()
