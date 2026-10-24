"""Paired source/binding regressions; these do not certify arbitrary model judgments."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as inputs
import hg_write_output as writer
import hg_eval_release as release
import hg_prompt_checks as prompt_checks
from hg_review_evidence import EvidenceReader
from hg_rubric_fact_binding import checked_facts
from hg_rubric_loop import digest
from hg_source_checks import SURFACES
from test_hg_rubric_loop import candidate, score_record, audit_report
from test_hg_prompt_ugt import same_result_review


class SourceBoundaries(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.known = {}
        self.context = dict(inputs={})
        self.source('S', 'source.json', {'value': 6209.70, 'records': [], 'control': 'known-present', 'unit': 'USD'})

    def source(self, sid, name, value):
        raw = json.dumps(value).encode()
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        self.known[sid] = dict(id=sid, path=name, sha256=digest(raw), quote=raw.decode(),
                              visibility='VISIBLE', access='Explicit synthetic source fixture.')
        return self.known[sid]

    def check(self, quote='6,209.70', kind='NUMBER', **extra):
        claim = dict(id='F', quote=quote, kind=kind, source_ids=['S'], reason='Compare against the scoped source.')
        if kind in {'NUMBER', 'RANGE'}:
            claim['calculation'] = dict(op='direct', operands=[dict(source_id='S', pointer='/value')])
        else:
            claim['status'] = 'VERIFIED'
        claim.update(extra)
        return checked_facts(dict(complete=True, reason='Focused fact inventory.', claims=[claim]),
                             dict(title='The Agent reports ' + quote + '.'), EvidenceReader(self.root),
                             self.known, self.root, self.context)

    def absence(self):
        return dict(method='ABSENCE', scope='All records in the authoritative synthetic register.',
                    reason='Check the complete applicable collection.', errors=[],
                    positive_control=dict(source_id='S', quote='known-present'),
                    surfaces=[dict(kind=k, status='COMPLETE' if k == 'JSON' else 'NOT_APPLICABLE',
                        source_ids=['S'] if k == 'JSON' else [],
                        reason='The fixture defines a standalone JSON register without this other surface.') for k in sorted(SURFACES)])

    def test_primary_correct_and_incorrect_numbers(self):
        self.assertEqual(self.check()['unresolved'], [])
        self.assertTrue(self.check('6,140')['mismatches'])

    def test_metadata_cannot_prove_match_or_mismatch(self):
        for name in ('07_Dynamic_Context.md', '12_Difficulty_Stats.txt', '08_Golden_Answer.md',
                     'Evals/task_inputs/reports/old_audit.md'):
            self.source('S', name, {'value': 6209.70})
            for value in ('6,209.70', '6,140'):
                result = self.check(value)
                self.assertFalse(result['mismatches'])
                self.assertFalse(result['computed'])
                self.assertTrue(result['unresolved'])

    def test_renamed_metadata_and_explicit_source_role_are_blocked(self):
        self.context['inputs']['source:dynamic-context'] = dict(files=[dict(path='source.json')])
        self.assertTrue(self.check()['unresolved'])
        self.context = dict(inputs={})
        self.known['S']['source_role'] = 'AUTHORING_METADATA'
        self.assertTrue(self.check()['unresolved'])

    def test_prompt_rubric_qc_examples_cannot_prove_task_facts(self):
        # Historical facts must not become PASS or Incorrect even if a caller
        # mislabels the packaged corpus or review guide as primary evidence.
        for name in ('prompt_qc_cases.json', 'prompt_qc_examples.md',
                     'rubric_qc_cases.json', 'rubric_qc_examples.md'):
            with self.subTest(name=name):
                source = self.source('S', 'Evals/references/rules/' + name,
                                     {'value': 6209.70})
                source['source_role'] = 'UNIVERSE_DATA'
                for quote in ('6,209.70', '6,140'):
                    result = self.check(quote)
                    self.assertFalse(result['mismatches'])
                    self.assertFalse(result['computed'])
                    self.assertTrue(result['unresolved'])

    def test_source_unit_mismatch_remains_a_real_defect(self):
        result = self.check('6,209.70 EUR', calculation=dict(op='direct',
            operands=[dict(source_id='S', pointer='/value')], source_unit=dict(source_id='S', pointer='/unit')))
        self.assertTrue(result['mismatches'])

    def test_wrong_and_correct_closed_bands(self):
        self.assertTrue(self.check('approximately 6,140 (band 6,100–6,200)', 'RANGE')['mismatches'])
        good = self.check('approximately 6,210 (band 6,200–6,220)', 'RANGE')
        self.assertEqual(good['mismatches'], [])
        self.assertEqual(good['unresolved'], [])

    def test_range_boundary_and_currency(self):
        for value, accepted in ((6100, True), (6200, True), (6200.01, False), (6099.99, False)):
            self.source('S', 'source.json', {'value': value})
            result = self.check('6,100–6,200', 'RANGE')
            self.assertEqual(not result['mismatches'], accepted)
        self.source('S', 'source.json', {'value': 6209.70, 'unit': 'USD'})
        claim = dict(id='F', quote='6,200–6,220', kind='RANGE', source_ids=['S'], reason='USD interval.',
                     calculation=dict(op='direct', operands=[dict(source_id='S', pointer='/value')],
                                      source_unit=dict(source_id='S', pointer='/unit')))
        result = checked_facts(dict(complete=True, reason='Interval only.', claims=[claim]),
            dict(title='The Agent reports 6,200–6,220 USD.'), EvidenceReader(self.root), self.known, self.root, {})
        self.assertEqual(result['unresolved'] + result['mismatches'], [])

    def test_range_does_not_invent_tolerance_or_round_into_band(self):
        for quote in ('approximately 6,140', '6,200–6,100', '6,100–6,200)'):
            with self.assertRaises(ValueError):
                self.check(quote, 'RANGE')
        with self.assertRaisesRegex(ValueError, 'unrounded'):
            self.check('6,100–6,200', 'RANGE', calculation=dict(op='direct',
                operands=[dict(source_id='S', pointer='/value')], rounding=dict(places=0, mode='HALF_UP')))

    def test_absence_without_scope_evidence_is_unresolved(self):
        result = self.check('no matching records', 'SEMANTIC')
        self.assertTrue(result['unresolved'])
        self.assertFalse(result['mismatches'])

    def test_scoped_absence_with_positive_control_passes(self):
        result = self.check('no matching records', 'SEMANTIC', evidence_check=self.absence())
        self.assertEqual(result['unresolved'] + result['mismatches'], [])

    def test_incomplete_attachment_search_cannot_prove_absence(self):
        check = self.absence()
        next(s for s in check['surfaces'] if s['kind'] == 'ATTACHMENTS')['status'] = 'INCOMPLETE'
        self.assertTrue(self.check('no matching records', 'SEMANTIC', evidence_check=check)['unresolved'])

    def test_json_receipt_cannot_prove_missing_repository_refs(self):
        self.source('SCAN', 'scan.json', dict(scan_complete=True, errors=[], matches=[],
            scope='JSON scalar values; excludes root/ blobs and non-JSON attachments'))
        check = self.absence()
        next(s for s in check['surfaces'] if s['kind'] == 'REPOSITORY_REFS').update(status='COMPLETE', source_ids=['SCAN'])
        self.assertTrue(self.check('no release tags', 'SEMANTIC', evidence_check=check)['unresolved'])

    def test_failed_command_or_search_receipt_cannot_look_complete(self):
        for receipt in (dict(exit_code=2), dict(scan_complete=False), dict(errors=['regex failed']), dict(truncated=True)):
            self.source('SCAN', 'scan.json', receipt)
            check = self.absence()
            next(s for s in check['surfaces'] if s['kind'] == 'JSON')['source_ids'] = ['SCAN']
            self.assertTrue(self.check('no matching records', 'SEMANTIC', evidence_check=check)['unresolved'])

    def test_empty_git_tag_listing_is_not_exported_ref_proof(self):
        self.source('GIT', 'git.json', dict(command='git tag -l', stdout='', exit_code=0))
        check = self.absence()
        next(s for s in check['surfaces'] if s['kind'] == 'REPOSITORY_REFS').update(status='COMPLETE', source_ids=['GIT'])
        self.assertTrue(self.check('no release tags', 'SEMANTIC', evidence_check=check)['unresolved'])

    def test_empty_count_cannot_independently_prove_incorrect(self):
        calc = dict(op='count', operands=[dict(source_id='S', pointer='/records')], allow_empty=True, empty_reason='Empty selected collection.')
        result = self.check('3', calculation=calc)
        self.assertFalse(result['mismatches'])
        self.assertTrue(result['unresolved'])
        proven = self.check('3', calculation=calc, evidence_check=self.absence())
        self.assertTrue(proven['mismatches'])

    def test_formatting_zero_count_does_not_bypass_absence_guard(self):
        calc = dict(op='count', operands=[dict(source_id='S', pointer='/records')], allow_empty=True,
                    empty_reason='Empty collection.', rounding=dict(places=2, mode='HALF_UP'))
        result = self.check('3.00', calculation=calc)
        self.assertTrue(result['unresolved'])
        self.assertFalse(result['mismatches'])

    def test_positive_counterexample_does_not_require_global_absence_scan(self):
        result = self.check('no matching records', 'SEMANTIC', status='CONTRADICTED')
        self.assertTrue(result['mismatches'])
        self.assertFalse(result['unresolved'])

    def test_direct_evidence_for_descriptive_negative_needs_exact_quote(self):
        self.source('S', 'source.json', {'description': 'The authoritative register explicitly states no matching records.'})
        direct = dict(method='DIRECT', reason='An explicit source describes this property.', source_id='S', positive_evidence='explicitly states no matching records')
        self.assertFalse(self.check('no matching records', 'SEMANTIC', evidence_check=direct)['unresolved'])
        direct['positive_evidence'] = 'not in source'
        with self.assertRaisesRegex(ValueError, 'quote is absent'):
            self.check('no matching records', 'SEMANTIC', evidence_check=direct)

    def test_absence_inventory_and_control_cannot_be_omitted(self):
        check = self.absence()
        check['surfaces'].pop()
        with self.assertRaisesRegex(ValueError, 'account for'):
            self.check('no matching records', 'SEMANTIC', evidence_check=check)
        check = self.absence()
        check['positive_control']['quote'] = 'missing control'
        with self.assertRaisesRegex(ValueError, 'control quote is absent'):
            self.check('no matching records', 'SEMANTIC', evidence_check=check)


class PromptAndRelease(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.addCleanup(patch.stopall)
        patch.object(writer, 'REPOSITORY', self.root).start()
        patch.object(inputs, 'REPOSITORY', self.root).start()
        self.prompt = 'The launch shipped 2025-02-01.'
        inputs.save_input('prompt', content=self.prompt.encode())
        inputs.save_input('task-details', content=b'Synthetic task: assigned identity and fields are test data.')
        inputs.clear_input('injection', confirmed_unused=True)
        raw = b'{"shipped_at":"2025-04-01"}'
        (self.root / 'calendar.json').write_bytes(raw)
        self.source = dict(id='S', path='calendar.json', sha256=digest(raw), quote=raw.decode(),
                           visibility='VISIBLE', access='Synthetic authoritative calendar.')

    def record(self):
        prompt_source = dict(id='P', path=str(prompt_checks.PROMPT), sha256=digest(self.prompt.encode()),
                             quote=self.prompt, visibility='VISIBLE', access='The exact synthetic request.')
        return dict(**prompt_checks.start(self.root), sources=[self.source, prompt_source],
            unique_ground_truth=same_result_review('P', self.prompt),
            inventory_complete=True, inventory_reason='One asserted launch date.', other_checks_complete=True,
            clauses=[dict(start=0, end=len(self.prompt), quote=self.prompt, role='PREMISE', premise_ids=['P1'], reason='The date is asserted as fact.')],
            premises=[dict(id='P1', quote=self.prompt, start=0, kind='STATE', reason='Asserted completed launch.',
                fact_review=dict(complete=True, reason='Compare the date with the source calendar.', claims=[dict(
                    id='D', quote='2025-02-01', kind='DATE', source_ids=['S'], reason='Calendar gives the actual launch date.',
                    selection=dict(source_id='S', pointer='/shipped_at'))]))],
            other_failures=[], verdict='FAIL', verdict_score=2, execution_status='COMPLETE',
            verdict_reason='The asserted launch date is contradicted by the source.')

    def rendered(self, receipt):
        return (f"### FINAL VERDICT: {receipt['verdict']}\nScore: {receipt['verdict_score'] if receipt['verdict_score'] is not None else 'null'}\n"
                f"Execution status: {receipt['execution_status']}\nEvaluator model: Opus 5.5 (claude-opus-5-5), xhigh effort\n"
                "Next action: Review findings\n"
                f"Evidence limits: {'; '.join(receipt['unresolved']) or 'None'}\n"
                f"Reviewed prompt SHA-256: {receipt['reviewed_prompt_sha256']}\nReview context SHA-256: {receipt['review_context_sha256']}\n"
                f"Prompt record SHA-256: {receipt['prompt_record_sha256']}\nEval version: {receipt['eval_release']['version']}\n"
                f"Eval release SHA-256: {receipt['eval_release']['manifest_sha256']}\n\n"
                + receipt['ugt_report_section'])

    def test_false_premise_fails_and_supported_premise_passes(self):
        rec = self.record()
        bad = writer.save_output('prompt-checks', json.dumps(rec))
        self.assertEqual(bad['contradicted_premises'], ['P1'])
        self.prompt = 'The launch shipped 2025-04-01.'
        inputs.save_input('prompt', content=self.prompt.encode())
        rec = self.record()
        rec['premises'][0]['fact_review']['claims'][0]['quote'] = '2025-04-01'
        rec.update(verdict='PASS', verdict_score=5)
        good = writer.save_output('prompt-checks', json.dumps(rec))
        writer.save_output('prompt', self.rendered(good))
        self.assertEqual(good['contradicted_premises'], [])

    def test_false_premise_cannot_be_cleared_by_pass_label(self):
        rec = self.record()
        rec.update(verdict='PASS', verdict_score=5)
        with self.assertRaisesRegex(ValueError, 'requires FAIL'):
            writer.save_output('prompt-checks', json.dumps(rec))

    def test_metadata_cannot_produce_a_prompt_failure(self):
        rec = self.record()
        rec['sources'][0]['source_role'] = 'AUTHORING_METADATA'
        rec['execution_status'] = 'PARTIAL'
        with self.assertRaisesRegex(ValueError, 'demonstrated defect'):
            writer.save_output('prompt-checks', json.dumps(rec))
        rec.update(verdict='NON-FAIL', verdict_score=None)
        receipt = writer.save_output('prompt-checks', json.dumps(rec))
        self.assertTrue(receipt['unresolved'])
        self.assertFalse(receipt['contradicted_premises'])

    def test_prompt_cannot_certify_its_own_premise(self):
        rec = self.record()
        rec['sources'][0] = dict(id='S', path=str(prompt_checks.PROMPT), sha256=digest(self.prompt.encode()),
            quote=self.prompt, visibility='VISIBLE', access='The prompt itself.')
        claim = rec['premises'][0]['fact_review']['claims'][0]
        claim.pop('selection')
        claim.update(kind='SEMANTIC', status='VERIFIED', quote=self.prompt)
        rec.update(verdict='NON-FAIL', verdict_score=None, execution_status='PARTIAL')
        self.assertTrue(writer.save_output('prompt-checks', json.dumps(rec))['unresolved'])

    def test_new_output_and_explicit_hypothesis_are_not_phantoms(self):
        for text, role in (('Create a new audit issue.', 'REQUEST'), ('Check whether the launch shipped in February.', 'HYPOTHESIS')):
            self.prompt = text
            inputs.save_input('prompt', content=text.encode())
            rec = self.record()
            rec['premises'] = []
            rec['clauses'][0].update(role=role, premise_ids=[], reason='No asserted existing fact in this fixture.')
            rec.update(verdict='PASS', verdict_score=5)
            self.assertEqual(writer.save_output('prompt-checks', json.dumps(rec))['verdict'], 'PASS')

    def test_clause_gaps_and_unchecked_premises_rejected(self):
        rec = self.record()
        rec['clauses'][0]['end'] -= 1
        with self.assertRaisesRegex(ValueError, 'clause quote'):
            writer.save_output('prompt-checks', json.dumps(rec))
        rec = self.record()
        rec['clauses'][0]['premise_ids'] = []
        with self.assertRaisesRegex(ValueError, 'needs a premise'):
            writer.save_output('prompt-checks', json.dumps(rec))

    def test_scored_prompt_report_requires_record_and_exact_hashes(self):
        with self.assertRaisesRegex(ValueError, 'Save prompt-checks'):
            writer.save_output('prompt', '### FINAL VERDICT: PASS\nScore: 5\nExecution status: COMPLETE\nEvaluator model: Opus 5.5\nNext action: Done\nEvidence limits: None\n')
        receipt = writer.save_output('prompt-checks', json.dumps(self.record()))
        report = self.rendered(receipt)
        writer.save_output('prompt', report)
        with self.assertRaisesRegex(ValueError, 'contradicts'):
            writer.save_output('prompt', report.replace('Score: 2', 'Score: 1'))
        inputs.save_input('prompt', content=b'Another prompt.')
        with self.assertRaisesRegex(ValueError, 'changed'):
            writer.save_output('prompt', report)

    def test_source_change_invalidates_report(self):
        receipt = writer.save_output('prompt-checks', json.dumps(self.record()))
        (self.root / 'calendar.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'changed evidence'):
            writer.save_output('prompt', self.rendered(receipt))

    def test_old_and_current_records_are_counted_separately(self):
        receipt = writer.save_output('prompt-checks', json.dumps(self.record()))
        saved = writer.save_output('prompt', self.rendered(receipt))
        old = self.root / 'old.md'
        old.write_text('### FINAL VERDICT: PASS\nScore: 5\nExecution status: COMPLETE\nNext action: Done\nEvidence limits: None\n')
        result = release.summarize([saved['absolute_path'], old], 'prompt')
        self.assertEqual(result['groups']['CURRENT_RELEASE']['total'], 1)
        self.assertEqual(result['groups']['HISTORICAL_OR_UNBOUND']['total'], 1)
        (self.root / prompt_checks.RECORD).write_text('{}')
        self.assertEqual(release.classify_report(Path(saved['absolute_path']), 'prompt')['classification'], 'INVALID_BINDING')

    def test_missing_or_modified_installed_package_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Missing'):
            release.snapshot('prompt', self.root)
        manifest = json.loads((release.ROOT / release.MANIFEST).read_text())
        for name in [str(release.MANIFEST), *manifest['files']]:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(release.ROOT / name, path)
        self.assertEqual(release.snapshot('prompt', self.root)['version'], release.RELEASE)
        target = self.root / 'Evals/tools/hg_source_checks.py'
        target.write_text(target.read_text() + '\n# changed\n')
        with self.assertRaisesRegex(ValueError, 'changed or incomplete'):
            release.snapshot('prompt', self.root)

    def test_old_release_tag_cannot_authorize_new_record(self):
        rec = self.record()
        rec['eval_release']['version'] = 'rubric-revision-v8'
        with self.assertRaisesRegex(ValueError, 'current eval_release'):
            writer.save_output('prompt-checks', json.dumps(rec))

    def test_range_rubric_saves_without_rewriting_input(self):
        raw = candidate('The Agent reports 200–220 MB.')
        inputs.save_input('rubric', content=raw.encode())
        rec = score_record(self.root)
        rec['checks']['rows'][0]['fact_review']['claims'] = [dict(id='R', quote='200–220', kind='RANGE',
            source_ids=['F_SOURCE'], reason='Source-supported allowed interval.', calculation=dict(op='direct',
            operands=[dict(source_id='F_SOURCE', pointer='/size_mb')], source_unit=dict(source_id='F_SOURCE', pointer='/unit')))]
        receipt = writer.save_output('rubric-score', json.dumps(rec))
        writer.save_output('rubric', audit_report(receipt))
        self.assertEqual((self.root / 'Evals/task_inputs/09_Rubrics.json').read_text(), raw)


class ConfirmedRecipientCase(unittest.TestCase):
    def test_397a_authorized_recipient_and_invented_recipient(self):
        path = Path(__file__).parent / 'fixtures/reliability_397a.json'
        case = json.loads(path.read_text())
        self.assertEqual(digest(case['prompt'].encode()), case['prompt_sha256'])
        self.assertIn('follow his lead', case['prompt'])
        self.assertIn('Slack the numbers to Michelle Carter', case['delivery_quote'])
        self.assertIn('Arthur Blake', case['criterion_4'])
        source = dict(id='DM', path=str(path), sha256=digest(path.read_bytes()), pointer='/delivery_quote',
                      quote=case['delivery_quote'], visibility='VISIBLE',
                      access='Source-confirmed static SQL excerpt; original hash and line retained in this fixture.')
        for recipient, status in (('Arthur Blake', 'CONTRADICTED'), ('Michelle Carter', 'VERIFIED')):
            # Focused, manually established recipient boundary. The raw stored
            # rubric's formatting and other task facts are outside this test.
            review = dict(complete=True, reason='Only the delivery recipient is tested.', claims=[dict(
                id='recipient', quote=recipient, kind='SEMANTIC', status=status, source_ids=['DM'],
                reason='The prompt delegates to the DM; the DM explicitly names Michelle as recipient.')])
            result = checked_facts(review, dict(title='The Agent reports the figures to ' + recipient + '.'),
                                   EvidenceReader(path.parent), {'DM': source}, path.parent, {})
            self.assertEqual(bool(result['mismatches']), status == 'CONTRADICTED')
            self.assertFalse(result['unresolved'])


if __name__ == '__main__':
    unittest.main()
