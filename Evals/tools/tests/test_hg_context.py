import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

TOOLS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('stage_context', TOOLS / 'hg_context.py')
context = importlib.util.module_from_spec(spec)
spec.loader.exec_module(context)


class StageContextTests(unittest.TestCase):
    def test_stage_views_preserve_canonical_scoring_groups(self):
        path = context.ROOT / 'Evals/references/rules/scoring.json'
        raw = path.read_bytes()
        full = json.loads(raw)
        for stage, names in context.GROUPS.items():
            with self.subTest(stage=stage):
                view = context.context(stage)
                expected = [group for group in full if group['Dimension'] in names]
                self.assertEqual(view['scoring_groups'], expected)
                self.assertEqual(view['source_sha256'], hashlib.sha256(raw).hexdigest())
                self.assertTrue(all(Path(p).is_file() for p in view['helpers'].values()))

    def test_hardness_view_does_not_import_trajectory_QC_gates(self):
        view = context.context('hardness')
        self.assertNotIn('Trajectory (Agent Run)', [g['Dimension'] for g in view['scoring_groups']])
