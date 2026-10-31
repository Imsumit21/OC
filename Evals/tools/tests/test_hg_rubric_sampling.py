"""Sampling contract tests; no arbitrary rubric grading or model accuracy claims."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as inputs
import hg_write_output as writer
from hg_review_score import calculate, validate_score
from hg_rubric_checks import validate_checks
from hg_rubric_loop import digest, review_context, REFERENCES
from hg_rubric_sampling import validate_sampling
from rubric_checks_fixture import checks_fixture, idle_case
from test_hg_review_enforcement import tally
from test_hg_rubric_loop import candidate, score_record, audit_report


class SamplingChecks(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.addCleanup(patch.stopall)
        patch.object(inputs, 'REPOSITORY', self.root).start()
        inputs.save_input('universe', content=b'2026-02-14\n')  # task date (hg_universe.py)
        patch.object(writer, 'REPOSITORY', self.root).start()
        self.prompt = ('Report download sizes for all builds in the approved register, '
                       'including the unusual deployment, and send the report to the release channel.')
        inputs.save_input('prompt', content=self.prompt.encode())
        inputs.save_input('task-details', content=b'Synthetic sampling contract fixture')
        inputs.clear_input('injection', confirmed_unused=True)
        self.rubric = [json.loads(candidate(t))[0] for t in (
            'The Agent includes exactly the approved build-name multiset in the release report.',
            'The Agent reports 214 MB for Build Alpha in the release report.',
            'The Agent reports 214 MB for Build Edge in the release report.',
            'The Agent sends the release report to the release channel.')]
        self.checks = checks_fixture(self.rubric, self.prompt)
        for i, (req, row) in enumerate(zip(self.checks['requirements'], self.checks['rows'])):
            prop = ('cohort identity', 'download size', 'download size', 'delivery')[i]
            req.update(property=prop, output='Release report')
            row['assertion_inventory']['assertions'][0]['property'] = prop
        for req in self.checks['requirements'][1:3]:
            req.update(coverage_basis='SPOT_CHECK', sampling_group='sizes', sampling_eligible=True)
        self.group = dict(id='sizes', scope='All approved builds in the register.',
            property='download size', output='Release report', source_ids=['SCOPE'], eligibility='ELIGIBLE',
            repetition_reason='Each register member has the same requested download-size field.',
            comparable_importance_reason='Each routine size serves the same release reporting decision.',
            selection_reason='Alpha represents the ordinary builds; Edge represents the unusual deployment.',
            control_outcome_ids=['Q1-O1'], protected_outcome_ids=['Q4-O1'],
            protected_review_reason='Sending the report is a separately required action.',
            samples=[dict(outcome_id='Q2-O1', case_kind='ORDINARY', reason='Ordinary deployment.'),
                     dict(outcome_id='Q3-O1', case_kind='EDGE', reason='Unusual deployment.')],
            edge_cases_complete=True, edge_review_reason='The register identifies one unusual deployment.',
            edge_cases=[dict(id='unusual', description='Different deployment packaging.',
                             outcome_ids=['Q3-O1'], reason='The selected edge tests this case.')],
            limitations='Unsampled sizes may still be wrong; cohort membership does not prove every size.')
        self.checks['sampling_groups'] = [self.group]
        self.scope(48)

    def scope(self, count):
        raw = json.dumps(dict(builds=['Build Alpha', 'Build Edge'] +
                              [f'Build Routine {i}' for i in range(count-2)],
                              field='download size', edge='Build Edge')).encode()
        (self.root / 'scope.json').write_bytes(raw)
        source = dict(id='SCOPE', path='scope.json', sha256=digest(raw), quote=raw.decode(),
                      visibility='VISIBLE', access='Immutable synthetic register.', reachability='PROMPT_LINKED')
        self.checks['sources'] = [s for s in self.checks['sources'] if s['id'] != 'SCOPE'] + [source]

    def check(self, issues=None):
        return validate_checks(self.checks, self.rubric, issues or [], root=self.root,
                               context=review_context(self.root)['manifest'])

    def test_valid_sampling_does_not_manufacture_unsampled_cell_omissions(self):
        result = self.check()
        self.assertEqual(result['unresolved'], [])
        self.assertEqual((result['required_outcomes'], result['covered_outcomes']), (4, 4))
        self.assertEqual(result['sampling']['sampled_outcomes'], 2)
        scored = calculate(tally(4, [], 5), self.rubric, result)
        self.assertEqual(scored['verdict'], 'PASS')
        self.assertEqual(scored['fractions']['major'], [0, 4])

    def test_no_fixed_row_threshold_or_sample_ratio(self):
        for count in (3, 39, 40, 116, 1000):
            with self.subTest(records=count):
                self.scope(count)
                self.assertEqual(self.check()['unresolved'], [])

    def test_direct_reviews_remain_compatible(self):
        self.checks = checks_fixture(self.rubric, self.prompt)
        self.assertEqual(self.check()['sampling']['groups'], [])

    def test_no_criterion_cap_on_a_supplied_exhaustive_rubric(self):
        self.rubric = [json.loads(candidate())[0] for _ in range(116)]
        self.checks = checks_fixture(self.rubric, self.prompt)
        # The existing fixture gives each criterion a different entity/outcome;
        # this checks count handling, not the semantics of arbitrary titles.
        self.assertEqual(self.check()['required_outcomes'], 116)

    def test_sample_without_group_is_invalid_metadata_not_a_qc_verdict(self):
        del self.checks['sampling_groups']
        with self.assertRaisesRegex(ValueError, 'needs its sampling group'):
            self.check()

    def test_all_group_rationales_are_required(self):
        for key in ('scope', 'repetition_reason', 'comparable_importance_reason',
                    'selection_reason', 'protected_review_reason', 'edge_review_reason', 'limitations'):
            with self.subTest(key=key):
                old = self.group.pop(key)
                with self.assertRaisesRegex(ValueError, 'needs an explanation'):
                    self.check()
                self.group[key] = old

    def test_unknown_source_and_outcome_ids_rejected(self):
        for key, value in (('source_ids', ['missing']), ('control_outcome_ids', ['missing']),
                           ('protected_outcome_ids', ['missing'])):
            with self.subTest(key=key):
                old = self.group[key]
                self.group[key] = value
                with self.assertRaisesRegex(ValueError, 'known'):
                    self.check()
                self.group[key] = old

    def test_tampered_scope_bytes_rejected(self):
        (self.root / 'scope.json').write_text('different register')
        with self.assertRaisesRegex(ValueError, '(?i)sha|hash|changed'):
            self.check()

    def test_unresolved_scope_prevents_complete_pass(self):
        self.checks['sources'][-1]['visibility'] = 'UNRESOLVED'
        result = self.check()
        self.assertTrue(any('sampling scope' in s for s in result['unresolved']))
        scored = calculate(tally(4, [], 5), self.rubric, result)
        self.assertEqual(scored['execution_status'], 'PARTIAL')
        self.assertNotEqual(scored['verdict'], 'PASS')

    def test_unresolved_eligibility_or_edge_inventory_remains_partial(self):
        for key, value in (('eligibility', 'UNRESOLVED'), ('edge_cases_complete', False)):
            with self.subTest(key=key):
                old = self.group[key]
                self.group[key] = value
                self.assertTrue(self.check()['unresolved'])
                self.group[key] = old

    def test_no_edges_allowed_when_explained_and_all_samples_ordinary(self):
        self.group.update(edge_cases=[], edge_review_reason='No differing cases within this eligible family.')
        self.group['samples'][1]['case_kind'] = 'ORDINARY'
        self.assertEqual(self.check()['unresolved'], [])

    def test_known_edge_cannot_be_replaced_with_only_ordinary_first_rows(self):
        self.group['samples'][1]['case_kind'] = 'ORDINARY'
        with self.assertRaisesRegex(ValueError, 'each relevant edge'):
            self.check()

    def test_every_edge_sample_needs_explanation(self):
        self.group['edge_cases'] = []
        with self.assertRaisesRegex(ValueError, 'edge sample needs'):
            self.check()

    def test_ordinary_case_is_required(self):
        self.group['samples'][0]['case_kind'] = 'EDGE'
        with self.assertRaisesRegex(ValueError, 'ordinary representative'):
            self.check()

    def test_core_outcome_cannot_be_added_as_a_sample(self):
        self.group['samples'].append(dict(outcome_id='Q4-O1', case_kind='EDGE', reason='Attempt to sample delivery.'))
        with self.assertRaisesRegex(ValueError, 'SPOT_CHECK outcome IDs'):
            self.check()

    def test_declared_ineligible_requirement_cannot_be_a_sample(self):
        self.checks['requirements'][1]['sampling_eligible'] = False
        with self.assertRaisesRegex(ValueError, 'core/distinct or ineligible'):
            self.check()

    def test_protected_core_or_control_cannot_also_be_marked_sample(self):
        for key in ('control_outcome_ids', 'protected_outcome_ids'):
            with self.subTest(key=key):
                self.group[key].append('Q2-O1')
                with self.assertRaisesRegex(ValueError, 'require direct coverage'):
                    self.check()
                self.group[key].pop()

    def test_core_edge_can_be_protected_directly(self):
        req = self.checks['requirements'][2]
        for key in ('coverage_basis', 'sampling_group', 'sampling_eligible'):
            req.pop(key)
        self.group['samples'].pop()
        self.group['protected_outcome_ids'].append('Q3-O1')
        self.group['protected_review_reason'] += ' The unusual case is consequential and protected directly.'
        self.assertEqual(self.check()['unresolved'], [])

    def test_missing_core_outcome_still_requires_normal_major_finding(self):
        title = 'The Agent names the release report.'
        self.rubric[3]['title'] = title
        self.checks['rows'][3]['title'] = title
        self.checks['rows'][3]['assertion_inventory']['assertions'][0]['quote'] = title
        self.checks['rows'][3]['do_nothing_case'] = idle_case(title)
        req = self.checks['requirements'][3]
        req['coverage'] = 'MENTION_ONLY'
        for name in ('omission_test', 'wrong_result_test'):
            req[name].update(result='ACCEPT', caught_by=[], example='Name the report but never send it.',
                             reason='Naming a report does not establish delivery.')
        issue = dict(type='missing_coverage', rows=[], outcome_id=req['id'], criticality='critical',
                     impact='accepts_wrong', provenance='rubric_original',
                     reason='Requested delivery is not graded.', witness='Name the report but never send it.')
        with self.assertRaisesRegex(ValueError, 'missing_coverage issues must'):
            self.check()
        checked = self.check([issue])
        record = tally(4, [issue], 2)
        record['coverage'] = dict(required_outcomes=4, covered_outcomes=3)
        result = calculate(record, self.rubric, checked)
        self.assertEqual(result['fractions']['major'], [1, 4])
        self.assertEqual(result['verdict'], 'FAIL')

    def test_supplied_criteria_cannot_be_skipped(self):
        self.checks['rows'].pop()
        with self.assertRaisesRegex(ValueError, 'every criterion'):
            self.check()

    def test_sample_property_output_and_group_must_match(self):
        for key, value in (('property', 'merge date'), ('output', 'Another report'), ('sampling_group', 'another')):
            with self.subTest(key=key):
                req = self.checks['requirements'][1]
                old = req[key]
                req[key] = value
                with self.assertRaisesRegex(ValueError, 'group binding|same property'):
                    self.check()
                req[key] = old

    def test_controls_required_and_duplicate_samples_rejected(self):
        old = self.group['control_outcome_ids']
        self.group['control_outcome_ids'] = []
        with self.assertRaisesRegex(ValueError, 'known outcome IDs'):
            self.check()
        self.group['control_outcome_ids'] = old
        self.group['samples'].append(copy.deepcopy(self.group['samples'][0]))
        with self.assertRaisesRegex(ValueError, 'unique SPOT_CHECK'):
            self.check()

    def test_separate_requested_outputs_are_not_duplicate_grading(self):
        self.checks = checks_fixture(self.rubric[:2], self.prompt)
        self.rubric = self.rubric[:2]
        a, b = self.checks['requirements']
        b.update(entity=a['entity'], property=a['property'], output='Separately requested memo')
        self.assertFalse(any('duplicate' in s for s in self.check()['unresolved']))

    def test_sampling_is_bound_into_public_report_without_rewriting_input(self):
        raw = json.dumps(self.rubric).encode()
        inputs.save_input('rubric', content=raw)
        record = score_record(self.root)
        record['checks'] = self.checks
        receipt = writer.save_output('rubric-score', json.dumps(record))
        writer.save_output('rubric', audit_report(receipt))
        self.assertEqual((self.root / 'Evals/task_inputs/09_Rubrics.json').read_bytes(), raw)
        self.assertFalse((self.root / 'Evals/task_inputs/5_Rubric.json').exists())
        self.assertEqual(receipt['verdict'], 'PASS')
        self.checks['sampling_groups'][0]['samples'].pop()
        record['checks'] = self.checks
        with self.assertRaises(ValueError):
            validate_score(self.root, json.dumps(record))

    def test_sampling_helper_and_rule_are_context_dependencies(self):
        for name in ('Evals/tools/hg_rubric_sampling.py', 'Evals/references/rules/rubric_sampling.md'):
            self.assertIn(name, REFERENCES)
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('before')
            before = review_context(self.root)['sha256']
            path.write_text('after')
            self.assertNotEqual(review_context(self.root)['sha256'], before)


class ActualLargeRubricBoundaries(unittest.TestCase):
    """Real 2a3f prompt/title regressions, not a factual re-audit of its 116 rows."""
    def setUp(self):
        self.fixture = json.loads((Path(__file__).parent / 'fixtures/rubric_sampling_2a3f.json').read_text())

    def test_exact_116_authored_rows_remain_the_denominator(self):
        self.assertEqual(self.fixture['rubric_sha256'], 'e2a69d47166c42a49cd74d52b5091aaf5b9de6a4df5ed31d7749b051702324c4')
        self.assertEqual(digest(self.fixture['prompt'].encode()), self.fixture['prompt_sha256'])
        self.assertEqual(self.fixture['authored_count'], 116)
        self.assertEqual(len(self.fixture['titles']), 116)
        rubric = [json.loads(candidate(t))[0] for t in self.fixture['titles']]
        # A known hypothetical row defect is tallied against the full supplied array.
        issue = dict(type='incorrect', rows=[15], impact='rejects_correct', provenance='rubric_original',
                     reason='Hypothetical scoring-boundary check only.', witness='Hypothetical wrong accepted date.')
        result = calculate(tally(116, [issue], 2, rubric=rubric), rubric)
        self.assertEqual(result['fractions']['major'], [1, 116])
        self.assertEqual(result['verdict'], 'FAIL')

    def test_prompt_protects_core_platform_findings_diagnoses_and_actions(self):
        prompt = self.fixture['prompt']
        for quote in ('Do it per platform', 'For each gap I want the likely cause',
                      'needs correcting', 'post it where this got raised'):
            self.assertIn(quote, prompt)
        self.assertIn('2026-01-16', self.fixture['titles'][14])
        self.assertIn('2026-02-13', self.fixture['titles'][15])
        self.assertTrue(all('2026-02-13' in self.fixture['titles'][i-1] for i in (1, 2, 3, 4)))
        self.assertIn('client build', self.fixture['titles'][91])
        self.assertIn('ENG-2441', self.fixture['titles'][106])
        self.assertIn('ENG-2455', self.fixture['titles'][115])

    def test_real_core_rows_cannot_be_sampled_away_by_routine_group(self):
        # Manually established prompt/title boundary: routine arrivals are eligible
        # candidates, but a stopped platform and its comparison are core findings.
        requirements = {
            'ordinary': dict(coverage_basis='SPOT_CHECK', sampling_group='arrivals', sampling_eligible=True,
                             property='last-arrival date', output='Published audit'),
            'scope': dict(output='Published audit'),
            'R15': dict(output='Published audit'), 'R16': dict(output='Published audit')}
        group = dict(id='arrivals', scope='Routine comparable arrivals across the source-defined taxonomy.',
            property='last-arrival date', output='Published audit', source_ids=['prompt'], eligibility='ELIGIBLE',
            repetition_reason='The repeated routine date predicate appears at R1-R4.',
            comparable_importance_reason='Only routine healthy entries are eligible; R15/R16 are protected.',
            selection_reason='Illustrative ordinary case with the platform contrast protected directly.',
            protected_review_reason='The prompt explicitly asks for platform-specific stops.',
            edge_review_reason='Domino purchase has a different iOS/Android state.',
            limitations='No factual completeness or full rubric verdict is claimed by this focused test.',
            control_outcome_ids=['scope'], protected_outcome_ids=['R15', 'R16'],
            samples=[dict(outcome_id='ordinary', case_kind='ORDINARY', reason='Routine arrival case.')],
            edge_cases_complete=True, edge_cases=[dict(id='purchase-stop', description='iOS stop / Android healthy.',
                outcome_ids=['R15', 'R16'], reason='Both sides are needed for the explicitly requested contrast.')])
        known = {'prompt': dict(visibility='VISIBLE')}
        self.assertEqual(validate_sampling(dict(sampling_groups=[group]), requirements, known)['unresolved'], [])
        requirements['R15'].update(coverage_basis='SPOT_CHECK', sampling_group='arrivals', sampling_eligible=True)
        with self.assertRaisesRegex(ValueError, 'require direct coverage'):
            validate_sampling(dict(sampling_groups=[group]), requirements, known)


if __name__ == '__main__':
    unittest.main()
