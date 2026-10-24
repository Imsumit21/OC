"""Opus-first intake supports Haiku fallback without conflating model evidence."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]


class OpusInputTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / 'Evals/tools').mkdir(parents=True)
        (self.root / 'claude').mkdir()
        for name in ('hg_store_input.py', 'hg_preflight.py'):
            shutil.copy2(TOOLS / name, self.root / 'Evals/tools' / name)

    def tearDown(self):
        self.temp.cleanup()

    def cli(self, tool, *args, content=None, expected=0):
        result = subprocess.run([sys.executable, str(self.root / 'Evals/tools' / tool), *args],
                                input=content, capture_output=True, cwd=self.temp.name)
        self.assertEqual(result.returncode, expected, result.stderr.decode())
        return json.loads(result.stdout)

    def test_new_opus_replaces_only_opus_across_processes(self):
        legacy = b'[{"model":"claude-haiku-4-5","run":"legacy"}]'
        first = b'[{"model":"claude-opus-4-8","run":"first"}]'
        latest = b'[{"model":"claude-opus-4-8","run":"latest"}]'
        for key, content in [('haiku', legacy), ('prompt', b'exact prompt'), ('injection', b'SELECT 1;'),
                             ('opus', first), ('opus', latest)]:
            self.cli('hg_store_input.py', 'save', key, content=content)
        inventory = self.cli('hg_store_input.py', 'list')
        self.assertEqual(set(inventory['inputs']), {'haiku', 'opus', 'prompt', 'injection'})
        self.assertEqual(inventory['hardness_intake']['key'], 'opus')
        self.assertFalse(inventory['hardness_intake']['fallback'])
        base = self.root / 'Evals/task_inputs'
        self.assertEqual((base / 'opus/trajectory.json').read_bytes(), latest)
        self.assertEqual((base / 'haiku/trajectory.json').read_bytes(), legacy)
        self.assertEqual((base / '04_Prompt.txt').read_bytes(), b'exact prompt')
        self.assertEqual((base / '01_Universe_Inject.sql').read_bytes(), b'SELECT 1;')
        self.assertFalse((base / 'reports').exists())

    def test_preflight_falls_back_then_prefers_backfilled_opus(self):
        self.cli('hg_store_input.py', 'save', 'prompt', content=b'exact prompt')
        self.cli('hg_store_input.py', 'save', 'haiku', content=b'[{"model":"claude-haiku-4-5"}]')
        task = str(self.root / 'Evals/task_inputs')
        fallback = self.cli('hg_preflight.py', task, '--stage', 'hardness', '--format', 'json')
        self.assertEqual(fallback['screening_trajectory']['status'], 'PRESENT')
        self.assertEqual(fallback['screening_trajectory']['selection'], 'HAIKU_FALLBACK')
        self.assertEqual(Path(fallback['screening_trajectory']['path']), Path(task) / 'haiku/trajectory.json')
        self.assertEqual(self.cli('hg_store_input.py', 'list')['hardness_intake']['key'], 'haiku')
        self.cli('hg_store_input.py', 'save', 'opus', content=b'[{"model":"claude-opus-4-8"}]')
        ready = self.cli('hg_preflight.py', task, '--stage', 'hardness', '--format', 'json')
        self.assertEqual(ready['structural_input_issues'], [])
        self.assertEqual(ready['screening_trajectory']['selection'], 'OPUS_PRIMARY')
        self.assertEqual(ready['screening_trajectory']['model_and_completion'], 'NOT_INTERPRETED')
        self.assertEqual(ready['batches'], {})
        self.assertEqual({a['path'] for a in ready['artifacts'] if a['required_for_selected_stage']}, {'04_Prompt.txt'})
        # A mapped single run can live elsewhere; no golden, verifier, template,
        # Docs or base-universe folder is required by structural intake.
        explicit = self.root / 'selected.json'
        explicit.write_text('[{"model":"claude-haiku-4-5","run":"selected"}]')
        mapped = self.cli('hg_preflight.py', task, '--stage', 'hardness', '--trajectory', str(explicit), '--format', 'json')
        self.assertEqual(Path(mapped['screening_trajectory']['path']), explicit)
        self.assertEqual(mapped['screening_trajectory']['selection'], 'EXPLICIT')

    def test_invalid_run_is_preserved_but_preflight_cannot_claim_ready(self):
        self.cli('hg_store_input.py', 'save', 'prompt', content=b'exact prompt')
        self.cli('hg_store_input.py', 'save', 'haiku', content=b'[{"model":"claude-haiku-4-5"}]')
        for content, status in [(b'{broken', 'INVALID_CONTENT'), (b'[]', 'EMPTY_JSON'), (b'7', 'INVALID_SHAPE')]:
            with self.subTest(status=status):
                self.cli('hg_store_input.py', 'save', 'opus', content=content)
                task = self.root / 'Evals/task_inputs'
                self.assertEqual((task / 'opus/trajectory.json').read_bytes(), content)
                report = self.cli('hg_preflight.py', str(task), '--stage', 'hardness', '--format', 'json', expected=1)
                self.assertEqual(report['screening_trajectory']['status'], status)
                self.assertEqual(report['screening_trajectory']['selection'], 'OPUS_PRIMARY')

    def test_unindexed_old_task_falls_back_without_writing_or_relabeling(self):
        task = self.root / 'Evals/task_inputs'
        path = task / 'haiku/trajectory.json'
        path.parent.mkdir(parents=True)
        original = b'[{"model":"claude-haiku-4-5","run":"old-task"}]'
        path.write_bytes(original)
        before = self.cli('hg_store_input.py', 'list')
        self.assertEqual(before['hardness_intake']['state'], 'UNINDEXED_CANDIDATE')
        self.assertEqual(before['hardness_intake']['key'], 'haiku')
        self.assertTrue(before['hardness_intake']['fallback'])
        self.assertFalse((task / 'inputs.json').exists())
        self.assertEqual(path.read_bytes(), original)
        self.assertFalse((task / 'opus').exists())

    def test_damaged_preferred_saved_run_is_not_silently_skipped(self):
        self.cli('hg_store_input.py', 'save', 'haiku', content=b'[{"model":"claude-haiku-4-5"}]')
        self.cli('hg_store_input.py', 'save', 'opus', content=b'[{"model":"claude-opus-4-8"}]')
        path = self.root / 'Evals/task_inputs/opus/trajectory.json'
        path.write_bytes(b'changed')
        damaged = self.cli('hg_store_input.py', 'list')['hardness_intake']
        self.assertEqual((damaged['state'], damaged['key']), ('NEEDS_ATTENTION', 'opus'))
        path.unlink()
        missing = self.cli('hg_store_input.py', 'list')['hardness_intake']
        self.assertEqual((missing['state'], missing['key']), ('NEEDS_ATTENTION', 'opus'))
        checked = self.cli('hg_preflight.py', str(self.root / 'Evals/task_inputs'), '--stage', 'hardness', '--format', 'json', expected=1)
        self.assertEqual(checked['screening_trajectory']['status'], 'INPUT_INTEGRITY_ISSUE')
        self.assertEqual(checked['screening_trajectory']['selection'], 'OPUS_PRIMARY')
        self.cli('hg_store_input.py', 'clear', 'opus')
        fallback = self.cli('hg_store_input.py', 'list')['hardness_intake']
        self.assertEqual((fallback['state'], fallback['key']), ('CANDIDATE', 'haiku'))

    def test_cleared_run_is_not_revived_and_absent_inputs_ask_for_either_model(self):
        empty = self.cli('hg_store_input.py', 'list')['hardness_intake']
        self.assertEqual(empty['state'], 'ASK')
        self.cli('hg_store_input.py', 'save', 'haiku', content=b'[{}]')
        self.cli('hg_store_input.py', 'clear', 'haiku')
        path = self.root / 'Evals/task_inputs/haiku/trajectory.json'
        path.write_bytes(b'[{"model":"claude-haiku-4-5"}]')
        cleared = self.cli('hg_store_input.py', 'list')['hardness_intake']
        self.assertEqual(cleared['state'], 'ASK')
        self.assertIsNone(cleared['key'])
        checked = self.cli('hg_preflight.py', str(self.root / 'Evals/task_inputs'), '--stage', 'hardness', '--format', 'json', expected=1)
        self.assertEqual(checked['screening_trajectory']['status'], 'MISSING')

    def test_unmapped_opus_source_precedes_haiku(self):
        self.cli('hg_store_input.py', 'save', 'haiku', content=b'[{}]')
        source = self.root / 'source.json'
        source.write_text('[{"model":"claude-opus-4-8"}]')
        self.cli('hg_store_input.py', 'save', 'source:opus', '--source', str(source))
        intake = self.cli('hg_store_input.py', 'list')['hardness_intake']
        self.assertEqual((intake['state'], intake['key']), ('SOURCE_SUPPLIED', 'opus'))
        checked = self.cli('hg_preflight.py', str(self.root / 'Evals/task_inputs'), '--stage', 'hardness', '--format', 'json', expected=1)
        self.assertEqual(checked['screening_trajectory']['status'], 'UNMAPPED_SOURCE')


    def test_external_old_task_uses_file_fallback_and_respects_explicit_selection(self):
        task = self.root / 'older-task'
        (task / 'haiku').mkdir(parents=True)
        (task / '04_Prompt.txt').write_text('exact task')
        (task / 'haiku/trajectory.json').write_text('[{"model":"claude-haiku-4-5"}]')
        fallback = self.cli('hg_preflight.py', str(task), '--stage', 'hardness', '--format', 'json')
        self.assertEqual(fallback['screening_trajectory']['selection'], 'HAIKU_FALLBACK')
        (task / 'opus').mkdir()
        (task / 'opus/trajectory.json').write_text('')
        invalid = self.cli('hg_preflight.py', str(task), '--stage', 'hardness', '--format', 'json', expected=1)
        self.assertEqual(invalid['screening_trajectory']['selection'], 'OPUS_PRIMARY')
        self.assertEqual(invalid['screening_trajectory']['status'], 'EMPTY')
        explicit = self.cli('hg_preflight.py', str(task), '--stage', 'hardness', '--trajectory', str(task / 'haiku/trajectory.json'), '--format', 'json')
        self.assertEqual(explicit['screening_trajectory']['selection'], 'EXPLICIT')
        absent = self.cli('hg_preflight.py', str(task), '--stage', 'hardness', '--trajectory', str(task / 'missing.json'), '--format', 'json', expected=1)
        self.assertEqual(absent['screening_trajectory']['status'], 'MISSING')
        self.assertEqual(absent['screening_trajectory']['selection'], 'EXPLICIT')



if __name__ == '__main__':
    unittest.main()
