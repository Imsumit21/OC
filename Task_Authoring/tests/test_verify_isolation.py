"""Independent adversarial checks of production CLI task boundaries."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProductionTaskIsolation(unittest.TestCase):
    def setUp(self):
        scratch = ROOT / 'support/scratch'
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='verify-isolation-', dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.a, self.b = [Path(self.temp.name) / name for name in ('taskA', 'taskB')]
        for task in (self.a, self.b):
            task.mkdir()
            (task / '00_Assigments.md').write_text('spec_version: V3\n')
            (task / 'run.json').write_text(json.dumps([
                {'type': 'system', 'subtype': 'init', 'model': 'claude-opus-5-5', 'session_id': task.name},
                {'type': 'result', 'subtype': 'success', 'session_id': task.name}]))

    def command(self, run, out):
        return subprocess.run([sys.executable, '-B', str(ROOT / 'tools/trajectory_ledger.py'),
            '--task-dir', str(self.a), '--run', 'run-1=' + str(run),
            '--expected-model', 'claude-opus-5-5', '--out-dir', str(out), '--json'],
            capture_output=True, text=True)

    def test_foreign_run_cannot_be_read_under_selected_task(self):
        result = self.command(self.b / 'run.json', self.a / 'out')
        self.assertNotEqual(result.returncode, 0, 'foreign trajectory was accepted under task A')
        self.assertFalse((self.a / 'out/summary.json').exists())

    def test_selected_task_cannot_publish_into_other_task(self):
        result = self.command(self.a / 'run.json', self.b / 'out')
        self.assertNotEqual(result.returncode, 0, 'task A published into task B')
        self.assertFalse((self.b / 'out/summary.json').exists())

    def test_symlinked_foreign_run_is_rejected(self):
        alias = self.a / 'foreign.json'
        alias.symlink_to(self.b / 'run.json')
        result = self.command(alias, self.a / 'out')
        self.assertNotEqual(result.returncode, 0, 'symlink hid foreign task identity')
        self.assertFalse((self.a / 'out/summary.json').exists())

    def test_selected_same_task_flow_still_works(self):
        result = self.command(self.a / 'run.json', self.a / 'out')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.a / 'out/summary.json').is_file())

    def test_default_discovery_cannot_follow_foreign_export_symlink(self):
        folder = self.a / '06_PreCheck_Trajectory'
        folder.mkdir()
        (folder / 'trajectory.json').symlink_to(self.b / 'run.json')
        result = subprocess.run([sys.executable, '-B', str(ROOT / 'tools/trajectory_ledger.py'),
            '--task-dir', str(self.a), '--expected-model', 'claude-opus-5-5',
            '--out-dir', str(self.a / 'out')], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue('Selected task disagrees' in result.stderr or 'Mixed task artifacts' in result.stderr)
        self.assertFalse((self.a / 'out/summary.json').exists())

    def test_all_task_aware_forensic_clis_reject_foreign_paths_first(self):
        cases = [
            ('surface_grader.py', ['--surface', str(self.b / 'surface.json')]),
            ('preflight_report.py', ['--solver', str(self.b / 'solver.py')]),
            ('node_verdicts.py', ['--sql', 'revision=' + str(self.b / 'inject.sql')]),
            ('oracle_kit.py', ['check', '--solver', str(self.b / 'solver.py')]),
            ('gradable_surface.py', ['validate', str(self.b / 'surface.json')]),
            ('trap_liveness.py', ['--manifest', str(self.b / 'manifest.json'), '--design']),
            ('difficulty_mutation.py', ['geometry', '--surface', str(self.b / 'surface.json')]),
            ('hardness_forecast.py', ['forecast', '--model', 'fixture', '--surface', str(self.b / 'surface.json')]),
        ]
        for tool, args in cases:
            with self.subTest(tool=tool):
                result = subprocess.run([sys.executable, '-B', str(ROOT / 'tools' / tool),
                    *args, '--task-dir', str(self.a)], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Selected task disagrees', result.stderr,
                              f'{tool} did not reject at the task boundary: {result.stderr}')


if __name__ == '__main__':
    unittest.main()
