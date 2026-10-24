"""UGT contract regression tests, not tests of a model's semantic judgment."""
from copy import deepcopy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_prompt_ugt import validate_review, render_review, validate_report, has_scored_ugt
from hg_review_evidence import EvidenceReader, sources


def same_result_review(source_id='P', quote='Publish the signed date.'):
    """Simple structural fixture; callers supply a real bound prompt passage."""
    evidence = [dict(source_id=source_id, quote=quote)]
    result = dict(decision='Publish the signed date', writes='Create one note',
                  destinations='The requested note', contents='Date: 2026-01-01')
    return dict(complete=True, verdict='PASS', score=5, reason='Both readings require the same signed date.',
                evidence_limits=[], alternative_search_complete=True,
                alternative_selection_reason='Test whether an alternate display changes the required date.',
                readings=[dict(id='R1', interpretation='ISO date display', support=deepcopy(evidence),
                               material_result=deepcopy(result)),
                          dict(id='R2', interpretation='Long-form date display', support=deepcopy(evidence),
                               material_result={**result, 'contents': 'Date: January 1, 2026'})],
                comparisons=[dict(alternative_id='R2', resolution='SAME_MATERIAL_RESULT',
                                  reason='The calendar date and required note are unchanged.',
                                  evidence=deepcopy(evidence),
                                  field_comparison={f: dict(relation='SAME', reason=(
                                      'ISO and long-form text express the same calendar date.' if f == 'contents'
                                      else 'Both readings have the same required ' + f + '.')) for f in result},
                                  challenge=dict(resolution_relevance='The signed date requirement governs both date displays.',
                                                 delegation_basis='NOT_CLAIMED',
                                                 delegation_reason='No differing material outcome is authorized or claimed.',
                                                 evidence=deepcopy(evidence)))],
                option_inventory=dict(complete=True, reason='This request contains no enumerated material options.',
                                      evidence=deepcopy(evidence), options=[]),
                challenge_review=dict(strongest_alternative_id='R2',
                                      strongest_alternative_reason='Alternate display is the strongest supported competing interpretation; it preserves the calendar date.',
                                      evidence=deepcopy(evidence)))


class UGTTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.prompt = 'Publish the signed date. Follow the signed decision. Either display is acceptable if the date is unchanged.'
        self.context = dict(inputs={'prompt': dict(files=[dict(path='Evals/task_inputs/04_Prompt.txt')])})
        self.known = {}
        self.add_source('P', 'Evals/task_inputs/04_Prompt.txt', self.prompt)
        self.add_source('S', 'source.txt', 'Signed decision: publish January 1, 2026; do not publish January 2, 2026.',
                        incorporated_by='P', incorporation_reason='The prompt explicitly says to follow the signed decision.')
        self.review = same_result_review('P', self.prompt)

    def add_source(self, sid, path, quote, **extra):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(quote)
        source = dict(id=sid, path=path, quote=quote, sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                      visibility='VISIBLE', access='Public task source visible to the acting persona.', **extra)
        self.known.update(sources(EvidenceReader(self.root), [source]))

    def validate(self, review=None):
        return validate_review(self.review if review is None else review, self.known, self.root, self.context)

    def excluded(self):
        review = deepcopy(self.review)
        review['readings'][1]['material_result']['contents'] = 'Date: January 2, 2026'
        comparison = review['comparisons'][0]
        comparison.update(resolution='EXCLUDED', authority_chain=['P', 'S'],
                          reason='The incorporated signed decision forbids the alternate date.',
                          evidence=[dict(source_id='S', quote='do not publish January 2, 2026')])
        comparison['field_comparison']['contents'].update(relation='DIFFERENT', reason='The dates are one day apart.')
        comparison['challenge']['resolution_relevance'] = 'The signed decision explicitly excludes the alternate calendar date.'
        return review

    def delegated(self, kind='EXPLICIT_DELEGATION'):
        review = deepcopy(self.review)
        comparison = review['comparisons'][0]
        comparison.update(resolution='AUTHORIZED_VARIATION', authority_chain=['P'], authority_kind=kind,
                          acceptance_boundary='Publish the signed calendar date with either display.',
                          acceptance_checks={'R1': 'ISO text gives the signed date.', 'R2': 'Long-form text gives the signed date.'})
        comparison['challenge'].update(delegation_basis='EXPLICIT_AUTHORITY',
                                       delegation_reason='The prompt explicitly permits either display subject to the unchanged-date boundary.')
        return review

    def unresolved(self):
        review = deepcopy(self.review)
        review.update(verdict='FAIL', score=2, reason='Two supported contents remain materially different.')
        review['readings'][1]['material_result']['contents'] = 'Date: January 2, 2026'
        comparison = review['comparisons'][0]
        comparison.update(resolution='UNRESOLVED_MATERIAL_DIFFERENCE', reason='Both dates remain plausible without a resolving authority.')
        comparison['field_comparison']['contents'].update(relation='DIFFERENT', reason='The concrete note contains a different date.')
        return review

    def test_equivalent_prose_can_pass_without_literal_equality(self):
        self.assertNotEqual(self.review['readings'][0]['material_result'], self.review['readings'][1]['material_result'])
        self.assertEqual(self.validate()['verdict'], 'PASS')

    def test_supported_excluded_delegated_and_open_ended_controls(self):
        for review in [self.excluded(), self.delegated(), self.delegated('OBJECTIVE_ACCEPTANCE_BOUNDARY')]:
            with self.subTest(resolution=review['comparisons'][0]['resolution']):
                self.assertEqual(self.validate(review)['score'], 5)

    def test_supported_unresolved_difference_fails(self):
        self.assertEqual(self.validate(self.unresolved())['score'], 2)
        review = self.unresolved()
        review['score'] = 1
        self.assertEqual(self.validate(review)['score'], 1)

    def test_comparison_required_before_pass_and_fail(self):
        for review in (deepcopy(self.review), self.unresolved()):
            for key in ('readings', 'comparisons', 'alternative_selection_reason', 'challenge_review', 'option_inventory'):
                bad = deepcopy(review)
                bad.pop(key)
                with self.subTest(verdict=review['verdict'], key=key), self.assertRaises(ValueError):
                    self.validate(bad)

    def test_every_alternative_is_compared(self):
        for mode in ('missing', 'duplicate', 'unknown'):
            bad = deepcopy(self.review)
            if mode == 'missing':
                bad['readings'].append({**deepcopy(bad['readings'][1]), 'id': 'R3'})
            elif mode == 'duplicate':
                bad['comparisons'].append(deepcopy(bad['comparisons'][0]))
            else:
                bad['comparisons'][0]['alternative_id'] = 'unknown'
            with self.subTest(mode=mode), self.assertRaises(ValueError):
                self.validate(bad)

    def test_same_destination_does_not_resolve_different_contents(self):
        bad = self.unresolved()
        bad.update(verdict='PASS', score=5)
        with self.assertRaises(ValueError):
            self.validate(bad)
        bad['comparisons'][0]['resolution'] = 'SAME_MATERIAL_RESULT'
        with self.assertRaisesRegex(ValueError, 'same destination'):
            self.validate(bad)

    def test_fail_requires_actual_recorded_material_difference(self):
        bad = deepcopy(self.review)
        bad.update(verdict='FAIL', score=2)
        with self.assertRaises(ValueError):
            self.validate(bad)
        bad = self.unresolved()
        bad['readings'][1]['material_result']['contents'] = bad['readings'][0]['material_result']['contents']
        with self.assertRaisesRegex(ValueError, 'different concrete contents'):
            self.validate(bad)
        bad['comparisons'][0]['resolution'] = 'UNRESOLVED_MATERIAL_DIFFERENCE'
        with self.assertRaises(ValueError):
            self.validate(bad)

    def test_no_unsupported_band_boolean_score_or_incomplete_score(self):
        for verdict, score in [('NON-FAIL', 3), ('NON-FAIL', 4), ('PASS', 4), ('FAIL', 5), ('FAIL', True), ('PASS', 5.0), ('UNVERIFIED', None)]:
            bad = deepcopy(self.review)
            bad.update(verdict=verdict, score=score)
            with self.subTest(verdict=verdict, score=score), self.assertRaises(ValueError):
                self.validate(bad)

    def test_partial_review_is_preserved_without_inventing_score(self):
        partial = dict(complete=False, verdict='UNVERIFIED', score=None,
                       reason='Signed appendix is unavailable.', evidence_limits=['Need the signed appendix to resolve two dates.'])
        checked = self.validate(partial)
        self.assertEqual(checked['pending'], partial['evidence_limits'])
        self.assertIsNone(checked['score'])
        block = render_review(checked, self.known)
        validate_report(checked, self.known, block)
        self.assertFalse(has_scored_ugt(block))
        for extra in ({'score': 3}, {'evidence_limits': []}, {'verdict': 'PASS'}):
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                self.validate({**partial, **extra})

    def test_sources_must_be_known_bound_visible_and_primary(self):
        for alteration in ('unknown', 'invented quote', 'inaccessible', 'metadata', 'audit', 'model'):
            bad = deepcopy(self.review)
            known = deepcopy(self.known)
            if alteration == 'unknown':
                bad['readings'][1]['support'][0]['source_id'] = 'unknown'
            elif alteration == 'invented quote':
                bad['readings'][1]['support'][0]['quote'] = 'Unwritten authority.'
            elif alteration == 'inaccessible':
                known['P']['visibility'] = 'INACCESSIBLE'
            else:
                known['P']['source_role'] = {'metadata': 'AUTHORING_METADATA', 'audit': 'AUDIT_REPORT', 'model': 'MODEL_OUTPUT'}[alteration]
            with self.subTest(alteration=alteration), self.assertRaises(ValueError):
                validate_review(bad, known, self.root, self.context)

    def test_authority_must_start_at_actual_prompt_and_quote_resolver(self):
        for chain in ([], ['S'], ['unknown'], ['P', 'S']):
            bad = self.excluded()
            bad['comparisons'][0]['authority_chain'] = chain
            if chain == ['P', 'S']:
                bad['comparisons'][0]['evidence'] = [dict(source_id='P', quote=self.prompt)]
            with self.subTest(chain=chain), self.assertRaises(ValueError):
                self.validate(bad)
        known = deepcopy(self.known)
        known['S'].pop('incorporated_by')
        with self.assertRaises(ValueError):
            validate_review(self.excluded(), known, self.root, self.context)

    def test_optional_authority_chain_is_checked_when_supplied(self):
        for value in (None, [None], ['unknown']):
            bad = deepcopy(self.review)
            bad['comparisons'][0]['authority_chain'] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.validate(bad)

    def test_excluded_option_must_match_concrete_compared_reading(self):
        review = self.excluded()
        review['option_inventory']['options'] = [dict(id='O2', option='January 2', source_id='S', quote='January 2, 2026',
                                                     reading_ids=['R2'], disposition='EXCLUDED', reason='Signed decision excludes this date.')]
        self.validate(review)
        for change in ({'reading_ids': []}, {'reading_ids': ['unknown']}, {'disposition': 'RETAINED'}, {'reading_ids': ['R1']}):
            bad = deepcopy(review)
            bad['option_inventory']['options'][0].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.validate(bad)

    def test_option_inventory_and_challenges_cannot_be_skipped(self):
        for change in ('inventory incomplete', 'no prompt evidence', 'no relevance', 'no strongest reason', 'false delegation', 'no boundary'):
            bad = self.delegated()
            if change == 'inventory incomplete':
                bad['option_inventory']['complete'] = False
            elif change == 'no prompt evidence':
                bad['option_inventory']['evidence'] = [dict(source_id='S', quote=self.known['S']['quote'])]
            elif change == 'no relevance':
                bad['comparisons'][0]['challenge'].pop('resolution_relevance')
            elif change == 'no strongest reason':
                bad['challenge_review'].pop('strongest_alternative_reason')
            elif change == 'false delegation':
                bad['comparisons'][0]['challenge']['delegation_basis'] = 'NOT_CLAIMED'
            else:
                bad['comparisons'][0].pop('acceptance_boundary')
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.validate(bad)

    def test_exact_report_block_must_be_present_once_and_visible(self):
        checked = self.validate()
        block = render_review(checked, self.known)
        validate_report(checked, self.known, '# Report\n\n' + block)
        validate_report(checked, self.known, 'Reference: <https://example.test/source>\n\n' + block)
        hidden = ['', block + block, block.replace('calendar date', 'other date'),
                  '```markdown\n' + block + '```\n', '<!--\n' + block + '-->',
                  '<pre>\n' + block + '</pre>', '<details>\n' + block + '</details>',
                  '<div hidden>\n' + block + '</div>', '<span style="display:none">\n' + block + '</span>']
        hidden += ['<' + tag + '="\n' + block + '">' for tag in ('img alt', 'meta content', 'br data-example', 'hr title')]
        for report in hidden:
            with self.subTest(report=report[:40]), self.assertRaises(ValueError):
                validate_report(checked, self.known, report)

    def test_report_summary_must_agree(self):
        checked = self.validate()
        block = render_review(checked, self.known)
        valid = ['Unique Ground Truth: PASS 5\n', '| Prompt | Unique Ground Truth | 5/5 | Same required date |\n',
                 '**UGT:** PASS (5)\n', '### UGT\nScore: 5\n', 'UGT PASS 5\n', 'UGT: Score5\n',
                 '| Unique Ground Truth | PASS | 5 | Resolved |\n',
                 '| Unique Ground Truth | 5 | Historical report was FAIL 2. |\n']
        for summary in valid:
            with self.subTest(summary=summary):
                validate_report(checked, self.known, block + '\n' + summary)
                self.assertTrue(has_scored_ugt(summary))
        invalid = ['Unique Ground Truth: FAIL 2\n', '| Prompt | Unique Ground Truth | 2/5 | Ambiguous |\n',
                   '**UGT:** NON-FAIL (3)\n', '### UGT\nScore: 2\n', 'UGT: UNVERIFIED\n']
        for summary in invalid:
            with self.subTest(summary=summary), self.assertRaises(ValueError):
                validate_report(checked, self.known, block + '\n' + summary)

    def test_detector_ignores_examples_comments_and_narrative_citations(self):
        for text in ['```\nUGT: PASS 5\n```', '<!-- UGT: PASS 5 -->',
                     'The historical report said Unique Ground Truth: PASS 5.', 'UGT: UNVERIFIED unscored']:
            with self.subTest(text=text):
                self.assertFalse(has_scored_ugt(text))

    def test_omitting_numeric_score_cannot_bypass_definitive_ugt_claim(self):
        for text in ['UGT: PASS', 'Unique Ground Truth: FAIL', 'UGT: NON-FAIL', '| Unique Ground Truth | PASS |']:
            with self.subTest(text=text):
                self.assertTrue(has_scored_ugt(text))

    def test_rendering_escapes_review_controlled_markup(self):
        review = deepcopy(self.review)
        review['reason'] = '<!-- hide -->\n```\n# Heading | [label](link)'
        checked = self.validate(review)
        block = render_review(checked, self.known)
        self.assertIn('&lt;!-- hide --&gt;', block)
        self.assertNotIn('<!-- hide -->', block)
        validate_report(checked, self.known, block)


if __name__ == '__main__':
    unittest.main()
