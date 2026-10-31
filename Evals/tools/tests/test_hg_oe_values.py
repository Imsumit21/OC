"""Expected-value ledger regressions (Eval 2 §2.4, port of golden G3).

Every value on an OE Expected line is quoted from a record or marked not_a_claim,
and an absence claim needs a scope-bound search. Fixtures are minimal excerpts of
real task data from Kelvin's 50-task review (2026-10-17): #7 (6aa8272b...fea90)
and #47 (6abcef4d...6025c). The OE review never reads the rubric.
"""
import json
import unittest

import test_hg_oe_review as fixture
import hg_oe_review as oe
import hg_store_input as inputs

PROMPT_7 = (b"leonard's archiving everyone's google accounts on february 15 and he wants the zombie match analytics "
            b"written down properly before it all disappears. can you work out what's actually live versus what was "
            b"only ever planned, leave the record and the loose tickets in linear so someone could pick it up cold, "
            b"and send leonard the summary when you're done?")
# #7: the event that fires on a quest claim (AnalyticsManager.cs:849-856 in harmonygames-Games/match3d).
LIVE_7 = '''        private void OnQuestCompletion(OnQuestCompleted questCompleted)
        {
            const string QuestCompletionEvent = "quest_completed";
            LogEvent(QuestCompletionEvent, new List<EventParameter>
            {
                new EventParameter("quest_id", questCompleted.QuestModel.Id),
                new EventParameter("reward_content", LiveOpsRewards.ArrayToAnalyticsString(questCompleted.QuestModel.QuestReward.ToArray()))
            });
        }
'''
STEP_7 = ('OE 1  Work out what the quest event is called when it actually fires. Read '
          'Assets/Scripts/Utils/AnalyticsManager.cs in GitHub (harmonygames-Games/match3d) and follow the '
          'QuestCompleted case to the method it calls.\n')
# #7's key (criterion-10) said the specified `quest_completion` ships under that name.
EXPECTED_7 = 'Expected: claiming a quest logs `{}` with quest_id and reward_content.\n'
# #47 OE 15, verbatim apart from the shortened action sentence.
OE_47 = ('OE 15  For every flagged pull request, call github_get_pull_request_commits (re-checked for a later fixing '
         'commit) before marking it "open" on the register. The agent finds that none of the 33 flagged pull requests '
         'shows a later commit or merged follow-up PR that addresses the specific finding named in its Critical '
         'comment, every one is still correctly disclosed as open, not remediated.\n')
ABSENCE_47 = ('none of the 33 flagged pull requests shows a later commit or merged follow-up PR that addresses the '
              'specific finding named in its Critical comment')
# Base GitHub data: CodeRabbit's own note on GameOfDominoes #1912 rc_1 and the fixing commit.
COMMENT_47 = {'id': 'harmonygames-Games/GameOfDominoes#1912#rc_1', 'pr_id': 'harmonygames-Games/GameOfDominoes#1912',
              'body': '_⚠️ Potential issue_ | _\U0001f534 Critical_\n\n<!-- This is an auto-generated comment by '
                      'CodeRabbit -->\n\n✅ Addressed in commit 77cf03f', 'created_at': '2025-11-22T02:03:23Z'}
COMMIT_47 = {'sha': '77cf03fefbd63a9c9838ab4c799d106a6c8b97ac', 'repo_id': 'harmonygames-Games/GameOfDominoes',
             'message': 'Wait on all assets to download.', 'authored_date': '2025-11-22T02:19:11Z'}
REGISTER_47 = {'policy': 'Each row is marked Open until a source-grounded commit shows the finding remediated.'}


class ExpectedValueTests(unittest.TestCase):
    setUp = fixture.OEReviewTests.setUp
    source = fixture.OEReviewTests.source

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content if isinstance(content, str) else json.dumps(content, ensure_ascii=False))
        return path

    def build(self, oe_text, sources, entries, tool, params, prompt=PROMPT_7):
        inputs.save_input('prompt', content=prompt)
        inputs.save_input('oe', content=oe_text.encode())
        ids = [s['id'] for s in sources]
        checks = {k: dict(result='VERIFIED', reason='Checked against the cited records.', source_ids=ids) for k in oe.FIELDS}
        checks['dependencies'] = dict(result='NOT_APPLICABLE', reason='First discovery step.')
        return {**oe.start(self.root), 'inventory_complete': True, 'inventory_reason': 'One-step fixture.',
                'sources': [self.source('P', self.root / 'Evals/task_inputs/04_Prompt.txt')] + sources,
                'segments': [dict(start=0, end=len(oe_text), quote=oe_text, role='STEP', step_ids=['OE1'], reason='Supplied step.')],
                'steps': [dict(id='OE1', checks=checks, rubric_verification=dict(category='OUTCOME', reason='Graded on the record the agent leaves.'))],
                'coverage': [dict(id='R1', requirement='Establish what is live.', authority_chain=['P'], step_ids=['OE1'],
                                  result='COVERED', reason='The prompt asks what is actually live.')],
                'format_review': dict(checked=True, reason='Numbered, one action, service named, Expected line present.', findings=[]),
                'expected_values': entries,
                'path_review': dict(complete=True, reason='Maps the one supplied step.', nodes=[dict(
                    id='read', step_ids=['OE1'], oe_quote=oe_text.split('.')[0], mapping_reason='Descriptive read mapped to the catalog tool.',
                    mode='TOOL', depends_on=[], tool=tool, service='github', parameter_style='DESCRIPTIVE', parameters=params, outputs={})],
                    feasibility={f: dict(result='SUPPORTED', reason='Fixture records are readable.', source_ids=ids)
                                 for f in ('data_access', 'tool_capability', 'preconditions', 'completion')},
                    runtime=dict(status='NOT_NEEDED', reason='Static evidence suffices.'), upstream_blockers=[])}

    def validate(self, record):
        return oe.validate_record(self.root, json.dumps(record))

    # --- #7: wrong event key --------------------------------------------------------------
    def record_7(self, key='quest_completion', key_entry=None):
        live = self.source('LIVE', self.write('match3d/AnalyticsManager.cs', LIVE_7))
        entries = [key_entry or dict(step_id='OE1', oe_quote='`' + key + '`', result='INACCURATE', source_ids=['LIVE'],
                                     source_value='quest_completed', reason='The QuestCompleted handler logs quest_completed.'),
                   dict(step_id='OE1', oe_quote='quest_id and reward_content', result='VERIFIED', source_ids=['LIVE'],
                        reason='Both parameters are on the live call.')]
        return self.build(STEP_7 + EXPECTED_7.format(key), [live], entries, 'github_get_file_contents',
                          {'owner': 'harmonygames-Games', 'repo': 'match3d', 'path': 'Assets/Scripts/Utils/AnalyticsManager.cs'})

    def test_7_wrong_event_key_is_wrong_expected_data(self):
        result = self.validate(self.record_7())
        self.assertEqual((result['verdict'], result['completeness_score'], result['accuracy_score']), ('FAIL', 5, 2))
        self.assertEqual(result['path_feasibility'], 'BROKEN')
        finding = [i for i in result['inaccurate'] if i.startswith('WRONG_EXPECTED_DATA')]
        self.assertEqual(len(finding), 1)
        self.assertIn('`quest_completion`', finding[0]); self.assertIn('quest_completed', finding[0])

    def test_7_wrong_key_cannot_be_recorded_verified(self):
        entry = dict(step_id='OE1', oe_quote='`quest_completion`', result='VERIFIED', source_ids=['LIVE'], reason='Looks right.')
        with self.assertRaisesRegex(ValueError, 'quest_completion.*character for character'):
            self.validate(self.record_7(key_entry=entry))

    def test_7_correct_key_quoted_from_the_record_passes(self):
        entry = dict(step_id='OE1', oe_quote='`quest_completed`', result='VERIFIED', source_ids=['LIVE'], reason='Live call site.')
        result = self.validate(self.record_7('quest_completed', entry))
        self.assertEqual((result['verdict'], result['verdict_score']), ('PASS', 5))
        self.assertEqual(result['expected_values'], dict(values=3, absence_claims=0, unledgered=[]))

    def test_unledgered_value_leaves_review_unscored(self):
        record = self.record_7(); record['expected_values'] = record['expected_values'][1:]
        result = self.validate(record)
        self.assertEqual((result['verdict'], result['verdict_score'], result['execution_status']), ('NON-FAIL', None, 'PARTIAL'))
        self.assertEqual(result['expected_values']['unledgered'], ['`quest_completion`'])
        self.assertTrue(any(u.startswith('unledgered expected value: `quest_completion`') for u in result['unresolved']))

    def test_not_a_claim_needs_a_reason_and_no_result(self):
        entry = dict(step_id='OE1', oe_quote='`quest_completion`', not_a_claim=True, reason='Names the spec, not a finding.')
        self.assertEqual(self.validate(self.record_7(key_entry=entry))['verdict'], 'PASS')
        for bad in (dict(entry, result='VERIFIED'), dict(entry, not_a_claim=False), dict(entry, reason='')):
            with self.assertRaises(ValueError): self.validate(self.record_7(key_entry=bad))

    def test_inaccurate_value_needs_the_differing_record_value(self):
        for value in ('quest_finished', 'quest_completion', ''):
            entry = dict(step_id='OE1', oe_quote='`quest_completion`', result='INACCURATE', source_ids=['LIVE'],
                         source_value=value, reason='Wrong key.')
            with self.assertRaisesRegex(ValueError, 'source_value'): self.validate(self.record_7(key_entry=entry))

    def test_entry_must_quote_the_supplied_oe(self):
        entry = dict(step_id='OE1', oe_quote='`quest_complete`', not_a_claim=True, reason='Not in the OE.')
        with self.assertRaisesRegex(ValueError, 'exact quote'): self.validate(self.record_7(key_entry=entry))
        entry = dict(entry, oe_quote='`quest_completion`', step_id='OE9')
        with self.assertRaisesRegex(ValueError, 'known step_id'): self.validate(self.record_7(key_entry=entry))

    def test_harmless_value_slip_is_minor(self):
        entry = dict(step_id='OE1', oe_quote='`quest_completion`', result='MINOR', source_ids=['LIVE'],
                     source_value='quest_completed', reason='Fixture: treated as a harmless spelling of the same key.')
        result = self.validate(self.record_7(key_entry=entry))
        self.assertEqual((result['verdict'], result['accuracy_score']), ('NON-FAIL', 3)); self.assertFalse(result['inaccurate'])

    def test_rendered_figures_need_the_record_or_a_calculation(self):
        # #7's injected #analytics message (excerpt of the saved injection SQL).
        inputs.save_input('injection', content=(
            "INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at)\nVALUES\n"
            "  ('c4bfc0e62fe9427fd8bd1124f389d97b',\n   '1770930847.412000',\n   'C069FF9Q57S',\n   'message',\n"
            "   'EMPLOYEE_0025_SLACK_ID',\n   'im pulling the metabase boards down next week. as far as im concerned the zm3d "
            "instrumentation list is closed out',\n   '2026-02-12 21:14:07.412+00');\n").encode())
        sql = self.root / 'Evals/task_inputs/01_Universe_Inject.sql'
        text = ('OE 1  Read the #analytics channel in Slack for Blake\'s latest word on the list.\n'
                'Expected: EMPLOYEE_0025_SLACK_ID posts in C069FF9Q57S on 2026-02-12 at 1:14 PM PT (ts 1770930847.412000) '
                'that the zm3d instrumentation list is closed out.\n')
        def record(calculation=None):
            entry = dict(step_id='OE1', oe_quote=text.split('Expected: ')[1].strip(), result='VERIFIED', source_ids=['SQL'],
                         reason='The injected message.')
            if calculation: entry['calculation'] = calculation
            return self.build(text, [self.source('SQL', sql)], [entry], 'github_get_file_contents',
                              {'owner': 'harmonygames-Games', 'repo': 'match3d'})
        with self.assertRaisesRegex(ValueError, '1:14.*calculation'): self.validate(record())
        result = self.validate(record('created_at 2026-02-12 21:14:07 UTC is 1:14 PM PST.'))
        self.assertEqual(result['verdict'], 'PASS')

    # --- #47: absence claim refuted by fix commits --------------------------------------------
    def record_47(self, entry, extra=()):
        sources = [self.source('CR', self.write('github/comment_1912.json', COMMENT_47)),
                   self.source('FIX', self.write('github/commit_77cf03f.json', COMMIT_47))] + list(extra)
        prompt = (b"Can you get eyes on the actual draft, fix whatever in it doesn't hold up, and get it sent today? "
                  b"and finish off the reconcilliation sheet I started instead of leaving it half full.")
        return self.build(OE_47, sources, [entry], 'github_get_pull_request_commits',
                          {'owner': 'harmonygames-Games', 'repo': 'GameOfDominoes', 'pullNumber': 1912}, prompt)

    def absence_entry(self, **changes):
        return dict(dict(step_id='OE1', oe_quote=ABSENCE_47, result='INACCURATE', source_ids=['CR', 'FIX'],
                         counterexample=dict(source_id='CR', quote='✅ Addressed in commit 77cf03f'),
                         calculation='33 = flagged pull requests counted in the OE 14 sweep.',
                         reason='CodeRabbit marks the Critical comment addressed by 77cf03f, a later commit on the PR.'), **changes)

    def absence_check(self, incomplete=False):
        surfaces = [dict(kind=k, status='NOT_APPLICABLE', source_ids=[], reason='Not where PR fixes live.')
                    for k in ('JSON', 'ATTACHMENTS', 'REPOSITORY_FILES', 'TABLE_METADATA', 'INJECTION')]
        surfaces.append(dict(kind='REPOSITORY_REFS', status='INCOMPLETE' if incomplete else 'COMPLETE', source_ids=['FIX'],
                             reason='Commits and review comments of the 33 flagged pull requests.'))
        return dict(method='ABSENCE', scope='Commits and CodeRabbit comments on the 33 flagged pull requests, through 2026-02-14.',
                    reason='A fix is a later commit or an Addressed-in-commit note.', errors=[], surfaces=surfaces,
                    positive_control=dict(source_id='FIX', quote='Wait on all assets to download.'))

    def test_47_refuted_absence_claim_is_wrong_expected_data(self):
        result = self.validate(self.record_47(self.absence_entry()))
        self.assertEqual((result['verdict'], result['accuracy_score'], result['path_feasibility']), ('FAIL', 2, 'BROKEN'))
        self.assertTrue(any(i.startswith('WRONG_EXPECTED_DATA') and 'refuted' in i for i in result['inaccurate']))
        self.assertEqual(result['expected_values'], dict(values=1, absence_claims=1, unledgered=[]))

    def test_47_absence_claim_needs_a_scope_bound_search(self):
        verified = dict(result='VERIFIED', counterexample=None)
        register = self.source('REG', self.write('register_policy.json', REGISTER_47))
        for changes, extra in ((verified, ()),
                               (dict(verified, source_ids=['REG'], evidence_check=dict(method='DIRECT', reason='The register says Open.',
                                     source_id='REG', positive_evidence='marked Open')), (register,))):
            entry = self.absence_entry(**changes); entry.pop('counterexample')
            with self.assertRaisesRegex(ValueError, 'scope-bound evidence_check'):
                self.validate(self.record_47(entry, extra))

    def test_47_verified_absence_cannot_carry_a_counterexample(self):
        entry = self.absence_entry(result='VERIFIED', evidence_check=self.absence_check())
        with self.assertRaisesRegex(ValueError, 'counterexample'): self.validate(self.record_47(entry))

    def test_counterexample_must_quote_a_cited_source(self):
        for counter in (dict(source_id='CR', quote='Addressed in commit 61f574d'), dict(source_id='P', quote='draft')):
            with self.assertRaisesRegex(ValueError, 'counterexample'):
                self.validate(self.record_47(self.absence_entry(counterexample=counter)))

    def test_incomplete_absence_search_is_unresolved_not_verified(self):
        entry = self.absence_entry(result='VERIFIED', evidence_check=self.absence_check(incomplete=True)); entry.pop('counterexample')
        result = self.validate(self.record_47(entry))
        self.assertEqual((result['verdict'], result['verdict_score']), ('NON-FAIL', None))
        self.assertTrue(any('REPOSITORY_REFS: incomplete coverage' in u for u in result['unresolved']))

    def test_complete_scope_bound_search_is_accepted(self):
        # Mechanics only: the helper checks the search record, the reviewer judges whether a record refutes it.
        entry = self.absence_entry(result='VERIFIED', evidence_check=self.absence_check()); entry.pop('counterexample')
        self.assertEqual(self.validate(self.record_47(entry))['verdict'], 'PASS')

    def test_unledgered_absence_wording_is_unresolved(self):
        entry = dict(step_id='OE1', oe_quote='33', result='VERIFIED', source_ids=['CR'], calculation='Counted from the sweep.',
                     reason='Count of flagged PRs.')
        result = self.validate(self.record_47(entry))
        self.assertIsNone(result['verdict_score'])
        self.assertTrue(any(u.startswith('unledgered absence claim: none') for u in result['unresolved']))

    def test_negation_quoted_from_a_record_needs_no_search(self):
        gdd = self.source('GDD', self.write('gdocs/combo_fighter_gdd.txt', '6. Audio\nMusic: None\nSFX: Standard fighting sounds.\n'
                                            '7. Monetization\nAds: None in MVP\n8. Ugly Game Mockups\n'))
        text = ('OE 2  Find the Combo Fighter GDD in Google Drive as Martin.\n'
                'Expected: It also still says "Ads: None in MVP", so it is not a source for shipped features.\n')
        entry = dict(step_id='OE1', oe_quote='"Ads: None in MVP"', result='VERIFIED', source_ids=['GDD'], reason='Quoted from the GDD.')
        result = self.validate(self.build(text, [gdd], [entry], 'github_get_file_contents', {'owner': 'x', 'repo': 'y'}))
        self.assertEqual((result['verdict'], result['expected_values']['absence_claims']), ('PASS', 1))

    # --- Expected lines and rubric blindness ---------------------------------------------------
    def test_expected_lines_with_and_without_label(self):
        text = ('OE 2  Search Arthur\'s Gmail for "boombit" (thread 1856918250324385305).\n'
                'Expected:\n   PERSON_0633 on Feb 13 at 17:04Z moves the call to 15:00 CET (OE 16).\n'
                '   Trap: the 0.3.269 build is not the retest build.\n\n'
                'OE 3  Read ZOM-387 in Linear. The agent finds ticket ZOM-387, created by usr_63fffeb4fab5233e; nobody closed it.\n'
                'OE 4  Post in #winddown.\n')
        values, absences = oe.expected_items(text)
        self.assertEqual([v[3] for v in values], ['PERSON_0633', '13', '17:04', '15:00', '0.3.269', 'ZOM-387', 'usr_63fffeb4fab5233e'])
        self.assertEqual([a[3] for a in absences], ['nobody'])

    def test_calibration_cases_match_the_fixtures(self):
        cases = json.loads((fixture.PACKAGE / 'Evals/references/rules/oracle_events_qc_cases.json').read_text())
        texts = {c['kelvin_number']: c['expected_text'] for c in cases['calibration_cases']}
        self.assertIn(texts[7], EXPECTED_7.format('quest_completion'))
        self.assertIn(texts[47], OE_47)
        self.assertEqual(len(cases['cases']), cases['counts']['criterion_flags'])  # historical block unchanged

    def test_rubric_is_neither_an_input_nor_evidence_for_the_oe_review(self):
        record = self.record_7('quest_completed', dict(step_id='OE1', oe_quote='`quest_completed`', result='VERIFIED',
                                                         source_ids=['LIVE'], reason='Live call site.'))
        before = oe.context(self.root)['sha256']
        inputs.save_input('rubric', content=b'[{"id": "criterion-10", "title": "ships under the same name, `quest_completed`"}]')
        self.assertEqual(oe.context(self.root)['sha256'], before)
        self.assertEqual(self.validate(record)['verdict'], 'PASS')
        rubric = self.source('RUB', self.root / 'Evals/task_inputs/09_Rubrics.json')
        record['sources'].append(rubric); record['expected_values'][0]['source_ids'] = ['RUB']
        self.assertIsNone(self.validate(record)['verdict_score'])


if __name__ == '__main__':
    unittest.main()
