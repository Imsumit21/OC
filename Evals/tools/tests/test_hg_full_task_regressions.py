"""Whole exported arrays/context; test specific manually established boundaries.

These are reproducible validator/counterexample checks, not fresh model runs or
certification that all other criteria/source facts in each task are correct.
"""
import json
from decimal import Decimal
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hg_rubric_acceptance import validate_acceptance
from hg_review_evidence import EvidenceReader
from hg_review_score import calculate
from hg_rubric_loop import digest
from test_hg_review_enforcement import tally

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/rubric_golden_v6_cases.json').read_text())


class FullTaskBoundaries(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def anchored(self, task):
        data = FIXTURE['tasks'][task]
        prompt = self.root / 'Evals/task_inputs/04_Prompt.txt'
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text(data['prompt'])
        golden = self.root / 'golden.json'
        golden.write_text(json.dumps(data['golden'], ensure_ascii=False))
        return [dict(id='P1', path=str(prompt), sha256=digest(prompt.read_bytes()), quote=data['prompt'], visibility='VISIBLE', access='Supplied task prompt'),
                dict(id='G1', path=str(golden), sha256=digest(golden.read_bytes()), pointer='/alternative_approaches_notes',
                     quote=data['golden']['alternative_approaches_notes'], visibility='VISIBLE', access='Supplied golden alternative notes, checked against prompt authority')]

    def record(self, task, row_number, restriction, counterexample):
        data = FIXTURE['tasks'][task]
        return dict(sources=self.anchored(task), requirements=[dict(id='Q1', authority_chain=['P1'], outcomes=[dict(id='O1', entity='Affected record', property='Current state', output='Requested artifact')])],
                    rows=[dict(row=row_number, atomicity=dict(outcome_ids=['O1']),
                        fact_review=dict(complete=False,reason='This regression establishes a restriction boundary; unrelated source facts are not certified.',claims=[]),
                        restriction_review=dict(
                        reason='Focused restriction regression; full artifact provided as context.', restrictions=[dict(
                            field='title', quote=restriction, status='UNSUPPORTED', reason='No prompt incorporation establishes this restriction; alternatives allow the other route.',
                            counterexample=counterexample)]))],
                    overlap_review=dict(complete=True, reason='This focused check owns one outcome.'),
                    alternative_review=dict(complete=True, source_ids=['P1','G1'], branches=[], reason='Alternative is quoted in source G1 and used in the focused counterexample; separate inventory tests cover full-set matrix validation.'))

    def test_original_prefill_and_submitted_counts_stay_separate(self):
        self.assertEqual([(len(FIXTURE['tasks'][n]['prefill']),len(FIXTURE['tasks'][n]['submitted'])) for n in ('70','71','72')],[(42,42),(27,20),(25,28)])

    def test_task71_new_card_ban_blocks_and_its_removal_clears_that_defect(self):
        task=FIXTURE['tasks']['71']
        quote='without editing the original historical cards in place'
        self.assertIn('editing the existing entries directly is another', task['golden']['alternative_approaches_notes'])
        rec=self.record('71',24,quote,'Correct existing Trello entries directly.')
        pending=validate_acceptance(rec,task['prefill'],self.root,{})
        self.assertTrue(any('UNSUPPORTED restriction' in p for p in pending))
        # Scoped repaired example, not a declaration that the remaining 26 rows pass.
        rec['rows'][0]['restriction_review'].update(restrictions=[],reason='Revised predicate permits editing existing records or adding corrections.')
        pending=validate_acceptance(rec,task['prefill'],self.root,{})
        self.assertFalse(any('UNSUPPORTED restriction' in p for p in pending))
        self.assertTrue(any('incomplete' in p for p in pending))

    def test_task72_layout_restriction_rejects_prompt_valid_structure(self):
        task=FIXTURE['tasks']['72']
        self.assertIn('document structure', task['golden']['alternative_approaches_notes'])
        rec=self.record('72',1,'two distinct sections','A status table separating completed, blocked and money/approval facts.')
        self.assertTrue(validate_acceptance(rec,task['prefill'],self.root,{}))

    def test_confirmed_original_defects_use_actual_denominators(self):
        # Conservative recorded subsets, not invented complete task scores.
        for task, original_rows, submitted_rows in [('71',[3,16,17,24,25],[3,12,13,15,16]),('72',[1,21],[1,21])]:
            for field, rows in [('prefill',original_rows),('submitted',submitted_rows)]:
                rubric=FIXTURE['tasks'][task][field]
                atomic_rows = ([3,16] if field=='prefill' else [3,12]) if task=='71' else [21]
                issues=[dict(type='non_atomic',rows=atomic_rows,impact='accepts_wrong',provenance='inherited_from_golden',inherited_quote='Golden sentence bundling the results.',
                             witness='A run satisfying one bundled result and failing the other receives the same credit as a correct run.',
                             reason='Independently required results bundled in one criterion.'),
                        dict(type='unauthorized',rows=[r for r in rows if r not in atomic_rows],impact='rejects_correct',provenance='inherited_from_golden',inherited_quote='Golden elaboration of layout/sequence.',
                             witness='A prompt-valid route using another layout or editing path is rejected.',
                             reason='Extra layout, sequencing or editing-path restriction excludes a prompt-valid route.')]
                # rubric-flow-v2: §2.7A vague exemplars are enforced in every field, not only titles.
                from hg_rubric_qc import VAGUE
                vague=[n for n,c in enumerate(rubric,1) if any(VAGUE.search(str(c.get(k,(c.get('annotations') or {}).get(k,'')) or ''))
                                                              for k in ('title','justification','evidence'))]
                if vague:
                    issues.append(dict(type='vague_exemplar',rows=vague,impact='precision_only',provenance='rubric_original',
                                       omission_test='A run naming any one example passes the same as the full set.',reason='Exemplar phrase in a supporting field.'))
                r=calculate(tally(len(rubric),issues,2,gate='atomicity',rubric=rubric,
                                  unresolved=['Other task checks outside this regression scope.']),rubric)
                self.assertEqual(r['fractions']['major'],[len(rows),len(rubric)])
                self.assertEqual(r['verdict'],'FAIL')
                self.assertEqual(r['execution_status'],'PARTIAL')
                self.assertFalse(r['repair_free'])

    def test_task72_annotation_key_order_does_not_erase_justification(self):
        annotations=FIXTURE['tasks']['72']['submitted'][27]['annotations']
        self.assertTrue(annotations['justification'].strip())
        reordered=dict(reversed(list(annotations.items())))
        self.assertEqual(reordered['justification'],annotations['justification'])

    def test_task72_claimed_fix_is_absent_from_actual_submitted_answer(self):
        task=FIXTURE['tasks']['72']
        self.anchored('72')
        path=self.root/'golden.json'
        anchor=dict(path=str(path),sha256=digest(path.read_bytes()),pointer='/golden_answer',
                    quote='Robert’s current tracker supersedes the earlier $6,250/$8,250 figures.')
        EvidenceReader(self.root).quote(anchor)
        replacement="Robert's current tracker states the earlier $6,250 Singular figure is no longer current"
        with self.assertRaisesRegex(ValueError,'absent'):
            EvidenceReader(self.root).quote({**anchor,'quote':replacement})
        repaired={**task['golden'],'golden_answer':task['golden']['golden_answer'].replace(anchor['quote'],replacement+'.')}
        path.write_text(json.dumps(repaired,ensure_ascii=False))
        EvidenceReader(self.root).quote({**anchor,'sha256':digest(path.read_bytes()),'quote':replacement})

    def test_task70_arithmetic_agrees_without_mixing_currency(self):
        monthly=['57403.46','47205.06','4144.22','28799.68','27576.03','17309.90']
        payee=['133444.13','18600','18500','6250','4144.22','1500']
        self.assertEqual(sum(map(Decimal,monthly)),Decimal('182438.35'))
        self.assertEqual(sum(map(Decimal,payee)),Decimal('182438.35'))
        self.assertIn('reported separately',FIXTURE['tasks']['70']['golden']['golden_answer'])

    def test_task70_explicit_reply_and_memo_surfaces_are_preserved(self):
        task=FIXTURE['tasks']['70']
        self.assertIn('give me the headline numbers here',task['prompt'])
        self.assertIn('memo',task['prefill'][22]['title'])
        self.assertIn('final response',task['prefill'][40]['title'])
        self.assertIn('$25,031',task['prefill'][22]['title'])
        self.assertIn('$25,031',task['prefill'][40]['title'])


if __name__ == '__main__':
    unittest.main()
