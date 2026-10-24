"""rubric-flow-v2: stricter-than-QC Non-Fail bands and row-ledger identity."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_rubric_qc import weight_tally
from hg_rubric_checks import STANDARD_AGENT
from hg_rubric_ledger import row_hash
from hg_rubric_lint import lint

KIND = {1: 'direct_lookup', 3: 'comparison', 5: 'tracing'}


def tally(n, off_one=0, off_two=0):
    rubric = [dict(title=f'The Agent does {i}.', weight=3) for i in range(n)]
    reviews = []
    for i in range(n):
        expected = 3
        if i < off_one:
            expected = 5
        elif i < off_one + off_two:
            rubric[i]['weight'] = 1
            expected = 5
        reviews.append(dict(row=i + 1, expected_weight=expected, work_kind=KIND[expected],
                            source_ids=['S1'], reason='Weight follows the QC work kind for this row.'))
    return weight_tally(reviews, rubric)


class WeightBandTests(unittest.TestCase):
    def test_clean_is_pass(self):
        self.assertEqual(tally(20)['band'], 'PASS')

    def test_one_level_up_to_ten_percent_is_non_fail(self):
        self.assertEqual(tally(20, off_one=1)['band'], 'NON-FAIL')
        self.assertEqual(tally(20, off_one=2)['band'], 'NON-FAIL')

    def test_one_level_over_ten_percent_fails(self):
        self.assertEqual(tally(20, off_one=3)['band'], 'FAIL')

    def test_any_two_level_disagreement_fails(self):
        self.assertEqual(tally(20, off_two=1)['band'], 'FAIL')


class AgentPrefixTests(unittest.TestCase):
    def test_both_standard_forms(self):
        self.assertTrue(STANDARD_AGENT.match('Agent posts the plan on ENG-2438.'))
        self.assertTrue(STANDARD_AGENT.match('The Agent posts the plan on ENG-2438.'))
        self.assertFalse(STANDARD_AGENT.match("The Agent's reply states the plan."))
        self.assertFalse(STANDARD_AGENT.match('The response states the plan.'))


class LedgerIdentityTests(unittest.TestCase):
    def test_hash_ignores_whitespace_and_annotation_layout(self):
        flat = dict(title='The Agent moves ENG-1 to Done.', weight=3, category='Outcome',
                    justification='Because.', evidence='Check state.')
        nested = dict(title='The Agent  moves ENG-1 to Done. ', weight=3,
                      annotations=dict(rubric_category='outcome', justification='Because.', evidence='Check state.'))
        self.assertEqual(row_hash(flat), row_hash(nested))

    def test_hash_changes_with_weight(self):
        a = dict(title='The Agent moves ENG-1 to Done.', weight=3, category='Outcome', justification='', evidence='')
        self.assertNotEqual(row_hash(a), row_hash({**a, 'weight': 5}))


class LintTests(unittest.TestCase):
    def row(self, **kw):
        base = dict(title='The Agent moves ENG-1 to Done.', weight=3, category='Outcome',
                    justification='Merged PR #1 closes it.', evidence='Check the state.')
        return {**base, **kw}

    def test_vague_exemplar_in_any_field(self):
        hits = lint([self.row(justification='Tickets such as ENG-2 are open.')])
        self.assertEqual([(h['check'], h['field']) for h in hits], [('vague_exemplar', 'justification')])

    def test_clean_row_has_no_hits(self):
        self.assertEqual(lint([self.row()]), [])

    def test_schema_and_markdown(self):
        hits = {h['check'] for h in lint([self.row(category='outcome', weight=2,
                                                   evidence='Mail [a](mailto:a@b.co).')])}
        self.assertEqual(hits, {'schema', 'markdown_artifact'})

if __name__ == '__main__':
    unittest.main()
