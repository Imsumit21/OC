import json
import subprocess
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_reference as ref


class ReferenceViews(unittest.TestCase):
    def test_nested_sections_keep_code_fence_verdict_example(self):
        source = '# A\n## B\ntext\n```md\n## fake\n```\n### C\nchild\n## D\nend\n'
        view = ref.sections(source)
        self.assertNotIn('fake', view)
        self.assertIn('### C\nchild', view['B'][2])
        self.assertIn('## fake', view['B'][2])
        self.assertNotIn('## D', view['B'][2])

    def test_all_guides_preserve_selected_rules_and_canonical_scoring(self):
        workflow = (ref.ROOT / 'Evals/WORKFLOW.md').read_text()
        sections = ref.sections(workflow)
        for stage in ref.hg_context.GROUPS:
            guide = ref.guide(stage)
            for name in ref.COMMON + ([] if stage == 'injection' else ref.TASK):
                self.assertIn(sections[name][2], guide)
            scoring = json.loads(guide.rsplit('```json\n', 1)[1].split('\n```')[0])
            self.assertEqual(scoring['scoring_groups'], ref.hg_context.context(stage)['scoring_groups'])

    def test_schema_preserves_every_property_and_handles_unknown_tables(self):
        all_entries = json.loads((ref.ROOT / 'Evals/references/schema/injection.json').read_text())
        view = ref.schema(['linear_issues', 'slack_messages', 'missing_table'])
        expected = [e for e in all_entries if e.get('table_name', e.get('name', e.get('table')))
                    in ('linear_issues', 'slack_messages')]
        self.assertEqual(view['tables'], expected)
        self.assertEqual(view['missing_tables'], ['missing_table'])
        qualified = ref.schema(['slack.slack_messages'])
        self.assertEqual(len(qualified['tables']), 1)
        self.assertEqual(qualified['missing_tables'], [])

    def test_routes_reference_the_verified_linear_and_slack_shapes(self):
        routes = ref.routes(['slack', 'linear'])['services']
        self.assertIn('/issues', routes['linear']['locations'][0]['array_pointers'])
        self.assertTrue(any(row['file'] == 'users.json' and row['array_pointers'] == ['']
                            for row in routes['slack']['locations']))
        with self.assertRaises(ValueError):
            ref.routes(['nonexistent'])

    def test_combined_guide_keeps_every_independent_view(self):
        for stage in ref.hg_context.GROUPS:
            proc = subprocess.run([sys.executable, str(Path(ref.__file__)), 'guide', stage,
                '--services', 'linear', 'slack', '--tables', 'linear_issues', 'missing_table'],
                capture_output=True, text=True, check=True)
            self.assertTrue(proc.stdout.startswith(ref.guide(stage)))
            payloads = [json.loads(part.split('\n```')[0]) for part in proc.stdout.split('```json\n')[1:]]
            self.assertEqual(payloads[-2], ref.routes(['linear', 'slack']))
            self.assertEqual(payloads[-1], ref.schema(['linear_issues', 'missing_table']))

    def test_invalid_combined_route_returns_error_without_partial_guide(self):
        proc = subprocess.run([sys.executable, str(Path(ref.__file__)), 'guide', 'prompt',
            '--services', 'invalid'], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(proc.stdout, '')
        self.assertIn('Unknown service', proc.stderr)


if __name__ == '__main__':
    unittest.main()
