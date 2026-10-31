"""Prompt rules agreed 2026-10-17 (Kelvin's 50-task flags) and their calibration cases.

These guard the case file's integrity and that the prompt eval files still carry
the agreed rules. They do not replay a model judgment; staged typos, trap hints,
hidden destinations and audit-form wording stay reviewer judgments.
"""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
EVALS = ROOT / 'Evals'
RULES = EVALS / 'references/rules'
RANKS = {1: '6a7f62daa0495108140f6b43', 11: '6abc06a64719e24dcc073708', 31: '6aaae61198c351537cbb2a2b',
         42: '6abd857f96a9f77c7e518348', 43: '6a83fa91fea987ea2b173deb', 44: '6ac674e16329279865bbecbf',
         47: '6abcef4dc5b130fe26c6025c', 49: '6abc06a64719e24dcc073719', 50: '6aa8272b1b7a2df0fc0fea8d'}
MISSPELLED_11 = ('breakdiwn', 'wirk', 'actualy', 'testd', 'chanel', 'everthing', 'whatevr', 'supposad',
                 ' nd ', 'calndars', 'telll')


def read(path):
    return path.read_text(encoding='utf-8')


class CalibrationCaseFile(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(read(RULES / 'prompt_qc_cases.json'))
        self.cases = {c['id']: c for c in self.data['calibration_cases']}

    def test_historical_cases_and_counts_are_unchanged(self):
        cases = self.data['cases']
        self.assertEqual(self.data['counts'], dict(
            cards=len(cases), tasks=len({c['task_id'] for c in cases}),
            criterion_flags=sum(len(c['flags']) for c in cases),
            fail_flags=sum(f['verdict'] == 'FAIL' for c in cases for f in c['flags'])))
        self.assertEqual(self.data['counts'], dict(cards=25, tasks=24, criterion_flags=29, fail_flags=10))
        names = [s['filename'] for s in self.data['sources']]
        self.assertEqual(names[:2], ['qc-audit-rubric-and-prompt-failures.csv', 'qc-audit-rubric-and-prompt-failures.html'])

    def test_new_sources_are_hash_bound(self):
        added = [s for s in self.data['sources'] if 'Kelvin Task Quality Flags 2026-10-17' in s['filename']]
        self.assertEqual(len(added), 2)
        for source in self.data['sources']:
            with self.subTest(source=source['filename']):
                self.assertRegex(source['sha256'], r'^[0-9a-f]{64}$')

    def test_calibration_counts_and_shape(self):
        cases = self.data['calibration_cases']
        self.assertEqual(len(self.cases), len(cases), 'case ids must be unique')
        counts = {'cases': len(cases), 'tasks': len({c['task_id'] for c in cases if c['kind'] == 'TASK'}),
                  'fail': sum(c['expected'] == 'FAIL' for c in cases),
                  'pass': sum(c['expected'] == 'PASS' for c in cases)}
        self.assertEqual(self.data['calibration_counts'], counts)
        for case in cases:
            with self.subTest(case=case['id']):
                self.assertIn(case['kind'], {'TASK', 'CONTROL'})
                self.assertIn(case['expected'], {'PASS', 'FAIL'})
                for key in ('rule', 'dimension', 'reason', 'eval_reference'):
                    self.assertTrue(case[key].strip())
                if case['kind'] == 'TASK':
                    self.assertEqual(RANKS[case['kelvin_rank']], case['task_id'])
                    self.assertEqual(hashlib.sha256(case['prompt'].encode()).hexdigest(), case['prompt_sha256'])
                    self.assertTrue(case['quotes'])
                    for quote in case['quotes']:
                        self.assertIn(quote, case['prompt'])
                else:
                    self.assertEqual(case['expected'], 'PASS')
                    self.assertTrue(case['text'].strip())

    def test_each_agreed_rule_has_fail_cases_and_a_control(self):
        expected = {'staged_errors': (['K11-staged-errors'], ['K11-control-spelled-correctly']),
                    'trap_hint_or_riddle': (['K31-trap-hint'], ['control-symptom']),
                    'hidden_destination': (['K42-hidden-destination', 'K47-hidden-destination',
                                            'K44-hidden-destination'], ['control-named-destination']),
                    'audit_form': (['K1-audit-form', 'K43-audit-form'], ['control-plain-request']),
                    'if_chain': (['K44-if-chain'], []),
                    'false_state_premise': (['K43-departed-person-premise'], [])}
        for rule, (fails, passes) in expected.items():
            with self.subTest(rule=rule):
                got = [c for c in self.data['calibration_cases'] if c['rule'] == rule]
                self.assertEqual(sorted(c['id'] for c in got if c['expected'] == 'FAIL'), sorted(fails))
                self.assertEqual(sorted(c['id'] for c in got if c['expected'] == 'PASS'), sorted(passes))

    def test_spelled_correctly_control_differs_only_by_the_misspellings(self):
        original = self.cases['K11-staged-errors']['prompt']
        control = self.cases['K11-control-spelled-correctly']['text']
        self.assertEqual(sum(original.count(w) for w in MISSPELLED_11), 11)
        self.assertFalse([w for w in MISSPELLED_11 if w in control])
        fixed = original
        for wrong, right in zip(MISSPELLED_11, ('breakdown', 'work', 'actually', 'tested', 'channel', 'everything',
                                                 'whatever', 'supposed', ' and ', 'calendars', 'tell')):
            fixed = fixed.replace(wrong, right)
        self.assertEqual(fixed, control)

    def test_ugt_cases_name_the_resolution(self):
        both = self.cases['K50-both-fair-figure']
        self.assertEqual((both['expected_resolution'], both['rubric_must_accept']), ('BOTH_FAIR_FIGURE', ['32.8%', '28.5%']))
        self.assertEqual(self.cases['K49-newer-source']['expected_resolution'], 'EXCLUDED')


class PromptEvalCarriesAgreedRules(unittest.TestCase):
    def setUp(self):
        self.eval1 = read(EVALS / '1_Prompt_Eval.md')
        self.scoring = read(RULES / 'scoring.json')
        self.common = read(RULES / 'common_errors.md')
        self.recheck = read(RULES / 'deep_recheck.md')
        self.skill = read(ROOT / 'claude/skills/prompt/SKILL.md')

    def test_a_staged_typos_fail_and_clean_typing_is_not_a_flag(self):
        for text in (self.eval1, self.scoring):
            self.assertIsNone(re.search(r'capitali[sz]', text, re.I))
        self.assertIn('| Staged errors: misspellings, made-up emoji or broken punctuation a person typing '
                      'normally would not leave | Yes/No |', self.eval1)
        self.assertIn('A prompt is a plain natural request: readable, not polished into a document, not roughed up on purpose.', self.eval1)
        self.assertNotIn('Real people type fast and unproofread', self.eval1)
        self.assertIn('Judge against the role only; the persona\'s own Slack or mail style is not a standard.', self.eval1)
        self.assertNotIn("persona's own messages in the Slack and Gmail exports", self.eval1)
        self.assertIn("cosmetic typos that don't affect meaning are fine. Staged typos fail Contrived (1.2).", self.eval1)
        self.assertIn('| Typing (2026-10-17) |', self.eval1)
        self.assertNotIn('read it as the persona would type it', self.recheck)

    def test_b_trap_hints_and_riddles_fail(self):
        self.assertIn('| Hidden root causes the prompt does not hint at |', self.eval1)
        self.assertIn('| Implicit requirements carried by records, not by prompt wording |', self.eval1)
        self.assertIn('| Trap hint or riddle: wording that points at the trap without naming it | Yes/No |', self.eval1)
        self.assertIn('| Riddles (2026-10-17) |', self.eval1)
        self.assertNotIn('If my date or channel is off, use the message that is actually there.', self.common)
        p4 = self.recheck.split('### P4')[1].split('## Oracle event passes')[0]
        self.assertIn('a hint or riddle aimed at the trap', p4)

    def test_c_both_fair_figure_is_a_narrow_local_override(self):
        self.assertIn('**PASS (5): both-fair figure (local override 2026-10-17).**', self.eval1)
        self.assertIn('Every other fork follows the FAIL and PASS rules above unchanged.', self.eval1)
        self.assertIn('The only exception is a\nboth-fair figure (below).', self.eval1)
        self.assertIn('| UGT both-fair figure (2026-10-17) |', self.eval1)
        self.assertIn('unless only one reported figure\ndiffers and both values are on records (Eval 1, both-fair figure).', self.common)
        self.assertIn('BOTH_FAIR_FIGURE', self.recheck)
        # The FAIL rule and the no-NON-FAIL statement are unchanged.
        self.assertIn('A leading or more-likely interpretation alone does not resolve it (06/09);', self.eval1)
        self.assertIn('- This sub-dimension has no scored NON-FAIL band.', self.eval1)

    def test_d_hidden_destinations_fail(self):
        self.assertNotIn('(dates, names, priorities, destinations) are planted', self.eval1)
        self.assertIn('Where the output goes is named when the persona would know it.', self.eval1)
        self.assertIn("| Hidden destination the persona would know ('wherever that's been asked for', 'the same place "
                      "the rest of these calls have been going') | Yes/No |", self.eval1)

    def test_audit_forms_and_if_chains_fail_without_a_word_list(self):
        self.assertIn('| Reads like an audit or compliance form, not a person asking for help | Yes/No |', self.eval1)
        self.assertIn('| Long chains of if / but-not / then-also clauses dictating what the Agent does per case | Yes/No |', self.eval1)
        self.assertIn('There is no word list\nand no count', self.eval1)
        self.assertNotIn('If a leftover review already has an owner, comment on it and leave it open.', self.common)

    def test_premise_check_covers_shutdown_and_departed_people(self):
        self.assertIn('company and people state: work that assumes HarmonyGames still runs normally after the '
                      'February 11, 2026 shutdown announcement', self.eval1)
        self.assertIn('not the storyline YAML', self.eval1)

    def test_e_today_is_february_14(self):
        sentence = ("'today' means Saturday, February 14, 2026, the date of\nthe fixed clock")
        self.assertIn(sentence, self.eval1)
        self.assertIn('today is Saturday, February 14, 2026', self.recheck)
        self.assertIn('today is Saturday, February 14, 2026 and yesterday\n  is February 13', self.skill)

    def test_housekeeping_common_errors_matches_eval_3_bands(self):
        self.assertIsNone(re.search(r'no\s+non-fail\s+band', self.common, re.I))
        self.assertIn('Eval 3 Local Overrides', self.common)
        self.assertNotIn('GOOD: “The Agent leaves ENG-123 open.”', self.common)
        self.assertNotIn('what the agent does or leaves in place', self.common)
        negative = next(s for g in json.loads(self.scoring) for s in g.get('Sub-Dimensions', [])
                        if s['Sub- Dimension'] == 'Negative Criteria')
        self.assertNotIn('preserved state', negative['Notes for Auditors'])
        self.assertIn('a condition on a write the Agent must make (an exact count or scope)', negative['Notes for Auditors'])

    def test_anonymized_tokens_are_a_platform_note(self):
        self.assertIn('Anonymized tokens such as `[PERSON_NAME_0854]` are the source string.', self.recheck)


if __name__ == '__main__':
    unittest.main()
