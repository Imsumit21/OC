"""Exercise the real writer, release binding and UGT comparison together."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

import test_hg_prompt_rubric_reliability as reliability
from test_hg_prompt_ugt import same_result_review, both_fair_review, PROMPT_50, NOTE_50, TOTALS_50, ZOM_673

inputs = reliability.inputs
writer = reliability.writer
checks = reliability.prompt_checks
release = reliability.release


class UGTSaving(unittest.TestCase):
    setUp = reliability.PromptAndRelease.setUp
    rendered = reliability.PromptAndRelease.rendered

    def record(self):
        self.prompt = 'Publish the signed date. Follow the calendar. ISO or long-form date text is acceptable.'
        inputs.save_input('prompt', content=self.prompt.encode())
        raw = b'{"signed_date":"2026-01-01"}'
        (self.root / 'calendar.json').write_bytes(raw)
        self.source.update(sha256=hashlib.sha256(raw).hexdigest(), quote=raw.decode())
        record = reliability.PromptAndRelease.record(self)
        record.update(premises=[], verdict='PASS', verdict_score=5, verdict_reason='The signed date is fixed.')
        record['clauses'][0].update(role='REQUEST', premise_ids=[], reason='Requested note; no factual premise asserted.')
        for reading in record['unique_ground_truth']['readings']:
            reading['support'].append(dict(source_id='S', quote='2026-01-01'))
        return record

    def failure_record(self):
        record = self.record()
        self.prompt = 'Choose one call: drop or port with changes. Write that call to decision.md.'
        inputs.save_input('prompt', content=self.prompt.encode())
        record.update(checks.start(self.root))
        record['sources'][1].update(quote=self.prompt, sha256=hashlib.sha256(self.prompt.encode()).hexdigest())
        record['clauses'][0].update(end=len(self.prompt), quote=self.prompt)
        review = same_result_review('P', self.prompt)
        evidence = [dict(source_id='P', quote=self.prompt)]
        review.update(verdict='FAIL', score=2, reason='The two calls require different decision contents.',
                      alternative_selection_reason='Compare both named calls, not an unrelated alternative.')
        for reading, call in zip(review['readings'], ('drop', 'port with changes')):
            reading.update(interpretation=call, material_result=dict(
                decision=call, writes='Create decision.md', destinations='decision.md', contents='Decision: ' + call))
        comparison = review['comparisons'][0]
        comparison.update(resolution='UNRESOLVED_MATERIAL_DIFFERENCE', reason='Neither listed call is selected by a rule.')
        for field in ('decision', 'contents'):
            comparison['field_comparison'][field].update(relation='DIFFERENT', reason='The chosen product decision differs.')
        comparison['challenge'].update(resolution_relevance='The option list establishes the competing calls but does not resolve the choice.',
                                       delegation_reason='Asking for one call does not explicitly accept either result.')
        review['option_inventory'].update(reason='Both named calls were tested.', options=[
            dict(id='O1', option='drop', source_id='P', quote='drop', reading_ids=['R1'],
                 disposition='RETAINED', reason='No source excludes dropping.'),
            dict(id='O2', option='port with changes', source_id='P', quote='port with changes', reading_ids=['R2'],
                 disposition='RETAINED', reason='No source excludes a changed port.')])
        review['challenge_review'].update(strongest_alternative_reason='The other named product call survives and changes the required contents.',
                                          evidence=evidence)
        record.update(unique_ground_truth=review, verdict='FAIL', verdict_score=2,
                      verdict_reason='Two materially different calls survive.')
        return record

    def both_fair_record(self):
        """#50-style both-fair rate fork bound to real record text (local override 2026-10-17)."""
        record = self.record()
        self.prompt = PROMPT_50
        inputs.save_input('prompt', content=self.prompt.encode())
        record.update(checks.start(self.root))
        record['sources'][1].update(quote=self.prompt, sha256=hashlib.sha256(self.prompt.encode()).hexdigest())
        record['clauses'][0].update(end=len(self.prompt), quote=self.prompt)
        for sid, name, text in (('NOTE', 'analytics.txt', NOTE_50), ('TOTALS', 'perf.json', TOTALS_50),
                                ('ZOM673', 'zom673.txt', ZOM_673)):
            (self.root / name).write_text(text)
            record['sources'].append(dict(id=sid, path=name, sha256=hashlib.sha256(text.encode()).hexdigest(), quote=text,
                                          visibility='VISIBLE', access='Persona-visible record copied from task #50.'))
        record.update(unique_ground_truth=both_fair_review(), verdict_reason='One reported rate has two fair values.')
        return record

    def save_record(self, record):
        return writer.save_output('prompt-checks', json.dumps(record))

    def test_missing_comparison_is_rejected_for_overall_pass_and_fail(self):
        for overall in ('PASS', 'FAIL'):
            record = self.record()
            record.pop('unique_ground_truth')
            if overall == 'FAIL':
                record.update(verdict='FAIL', verdict_score=2,
                              other_failures=[dict(dimension='Feasibility', reason='Synthetic supported defect', source_ids=['P'])])
            with self.subTest(overall=overall), self.assertRaisesRegex(ValueError, 'dimension-specific'):
                self.save_record(record)

    def test_legacy_record_cannot_be_relabelled_current(self):
        record = self.record()
        record['format_version'] = 1
        with self.assertRaisesRegex(ValueError, 'unsupported record format'):
            self.save_record(record)

    def test_ugt_pass_requires_table_even_when_overall_fails(self):
        record = self.record()
        record.update(verdict='FAIL', verdict_score=2,
                      other_failures=[dict(dimension='Feasibility', reason='Synthetic supported defect', source_ids=['P'])])
        receipt = self.save_record(record)
        report = self.rendered(receipt)
        writer.save_output('prompt', report)
        without_table = report.replace(receipt['ugt_report_section'], '')
        with self.assertRaisesRegex(ValueError, 'exact rendered comparison'):
            writer.save_output('prompt', without_table)
        self.assertEqual((self.root / writer.OUTPUTS['prompt']).read_text(), report)

    def test_ugt_failure_alone_controls_overall_verdict(self):
        record = self.failure_record()
        receipt = self.save_record(record)
        self.assertEqual(receipt['verdict'], 'FAIL')
        writer.save_output('prompt', self.rendered(receipt))
        record.update(verdict='PASS', verdict_score=5)
        with self.assertRaisesRegex(ValueError, 'requires FAIL'):
            self.save_record(record)

    def test_overall_score_cannot_exceed_ugt_failure(self):
        record = self.failure_record()
        record['unique_ground_truth']['score'] = 1
        with self.assertRaisesRegex(ValueError, 'cannot exceed'):
            self.save_record(record)
        record['verdict_score'] = 1
        self.assertEqual(self.save_record(record)['verdict_score'], 1)

    def test_ugt_cannot_bypass_comparison_through_other_failures(self):
        for alias in ('Unique Ground Truth', 'unique_ground_truth', 'UGT', '2.1', 'Phase 2.1', 'Section 2.1'):
            record = self.record()
            record.update(verdict='FAIL', verdict_score=2,
                          other_failures=[dict(dimension=alias, reason='An unstructured ambiguity claim.', source_ids=['P'])])
            with self.subTest(alias=alias), self.assertRaisesRegex(ValueError, 'not other_failures'):
                self.save_record(record)

    def test_partial_unscored_ugt_is_preserved(self):
        record = self.record()
        record.update(verdict='NON-FAIL', verdict_score=None, execution_status='PARTIAL',
                      unique_ground_truth=dict(complete=False, verdict='UNVERIFIED', score=None,
                                               reason='Required source has not been retrieved.', evidence_limits=['Signed decision missing.']))
        receipt = self.save_record(record)
        self.assertTrue(receipt['unresolved'])
        writer.save_output('prompt', self.rendered(receipt))
        record.update(verdict='PASS', verdict_score=5, execution_status='COMPLETE')
        with self.assertRaisesRegex(ValueError, 'cannot establish COMPLETE'):
            self.save_record(record)

    def test_no_score_partial_report_can_still_save_without_record(self):
        report = ('Unique Ground Truth: UNVERIFIED (unscored)\n\n'
                  '### FINAL VERDICT: NON-FAIL\nExecution status: PARTIAL\nClock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)\nEvaluator model: Opus 5.5\n'
                  'Next action: Read signed decision\nEvidence limits: Signed decision missing\n')
        self.assertIsNone(writer.save_output('prompt', report)['verdict_score'])

    def test_partial_aggregate_cannot_smuggle_a_definitive_ugt_without_record(self):
        final = ('### FINAL VERDICT: NON-FAIL\nExecution status: PARTIAL\nClock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)\nEvaluator model: Opus 5.5\n'
                 'Next action: Complete feasibility\nEvidence limits: Feasibility checks pending\n')
        for declaration in ('Unique Ground Truth: PASS 5', 'UGT: PASS', 'UGT: FAIL',
                            '| Prompt | Unique Ground Truth | 5/5 | Clear |',
                            '### UGT\nScore: 5\nVerdict: PASS', 'UGT: NON-FAIL 3'):
            with self.subTest(declaration=declaration), self.assertRaisesRegex(ValueError, 'Save prompt-checks'):
                writer.save_output('prompt', declaration + '\n\n' + final)

    def test_partial_aggregate_can_include_a_bound_ugt_pass(self):
        record = self.record()
        record.update(other_checks_complete=False, verdict='NON-FAIL', verdict_score=None, execution_status='PARTIAL')
        receipt = self.save_record(record)
        self.assertEqual(writer.save_output('prompt', self.rendered(receipt))['unique_ground_truth']['score'], 5)

    def test_mismatched_summary_cannot_override_bound_fail(self):
        receipt = self.save_record(self.failure_record())
        for summary in ('Unique Ground Truth: PASS 5', '| Prompt | Unique Ground Truth | 5 | Clear |',
                        '### UGT\nVerdict: PASS\nScore: 5'):
            with self.subTest(summary=summary), self.assertRaisesRegex(ValueError, 'contradictory UGT'):
                writer.save_output('prompt', self.rendered(receipt) + '\n' + summary)

    def test_report_cannot_hide_or_duplicate_comparison(self):
        receipt = self.save_record(self.record())
        report = self.rendered(receipt)
        block = receipt['ugt_report_section']
        for hidden in ('<!--\n' + block + '-->\n', '```\n' + block + '```\n',
                       '<div hidden>\n' + block + '</div>\n', block + '\n' + block):
            with self.subTest(wrapper=hidden[:20]), self.assertRaisesRegex(ValueError, 'exact rendered comparison'):
                writer.save_output('prompt', report.replace(block, hidden))

    def test_record_comparison_tampering_invalidates_report(self):
        record = self.record()
        receipt = self.save_record(record)
        record['unique_ground_truth']['comparisons'][0]['reason'] += ' Rechecked.'
        self.save_record(record)
        with self.assertRaisesRegex(ValueError, 'prompt_record_sha256'):
            writer.save_output('prompt', self.rendered(receipt))

    def test_current_inventory_rejects_report_without_bound_table(self):
        receipt = self.save_record(self.record())
        result = writer.save_output('prompt', self.rendered(receipt))
        path = Path(result['absolute_path'])
        self.assertEqual(release.classify_report(path, 'prompt')['classification'], 'CURRENT_RELEASE')
        path.write_text(path.read_text().replace(receipt['ugt_report_section'], ''))
        self.assertNotEqual(release.classify_report(path, 'prompt')['classification'], 'CURRENT_RELEASE')

    def test_both_fair_figure_saves_renders_and_classifies_current(self):
        receipt = self.save_record(self.both_fair_record())
        self.assertEqual((receipt['verdict'], receipt['unique_ground_truth']['score']), ('PASS', 5))
        self.assertIn('Rubric must accept: 32.8% or 28.5%', receipt['ugt_report_section'])
        self.assertEqual(receipt['both_fair_figures'], [dict(label='2-day Win & Collect completion rate', kind='RATE',
                                                             accept=['32.8%', '28.5%'])])
        result = writer.save_output('prompt', self.rendered(receipt))
        self.assertEqual(release.classify_report(Path(result['absolute_path']), 'prompt')['classification'],
                         'CURRENT_RELEASE')

    def test_other_resolutions_list_no_both_fair_figure(self):
        self.assertEqual(self.save_record(self.record())['both_fair_figures'], [])
        self.assertEqual(self.save_record(self.failure_record())['both_fair_figures'], [])

    def test_mislabelled_both_fair_figure_cannot_be_saved(self):
        record = self.both_fair_record()
        record['unique_ground_truth']['comparisons'][0]['figure']['checks']['newer_source']['settles'] = True
        with self.assertRaisesRegex(ValueError, 'newer source check settles'):
            self.save_record(record)

    def test_fresh_process_renders_the_exact_validated_section(self):
        receipt = self.save_record(self.record())
        # The CLI uses its package task root, so call the public renderer through
        # the same validator with the synthetic root in a fresh process.
        code = ('import pathlib,sys; import hg_prompt_checks as c; '
                'r=pathlib.Path(sys.argv[1]); '
                'print(c.validate_record(r,(r/c.RECORD).read_text())["ugt_report_section"],end="")')
        result = subprocess.run([sys.executable, '-B', '-c', code, str(self.root)],
                                cwd=Path(checks.__file__).parent, text=True, capture_output=True, check=True)
        self.assertEqual(result.stdout, receipt['ugt_report_section'])


if __name__ == '__main__':
    unittest.main()
