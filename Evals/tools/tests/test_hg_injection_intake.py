import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_store_input as store


class InjectionIntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.patch = patch.object(store, 'REPOSITORY', self.root)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def state(self):
        return store.inventory()['injection_intake']

    def test_omission_stays_unanswered_and_inventory_is_read_only(self):
        self.assertEqual(self.state()['state'], 'ASK')
        self.assertTrue(self.state()['ask'])
        self.assertFalse((self.root / store.INDEX).exists())
        store.save_input('prompt', content=b'exact prompt')
        self.assertEqual(self.state()['state'], 'ASK')

    def test_explicit_none_persists_then_sql_replaces_it(self):
        store.clear_input('injection', confirmed_unused=True)
        self.assertEqual(self.state()['state'], 'NOT_USED')
        self.assertFalse(self.state()['ask'])
        again = store.clear_input('injection', confirmed_unused=True)
        self.assertFalse(again['changed'])
        store.save_input('prompt', content=b'new prompt')
        self.assertEqual(self.state()['state'], 'NOT_USED')
        store.save_input('injection', content=b'SELECT 1;')
        self.assertEqual(self.state()['state'], 'SUPPLIED')
        self.assertNotIn('usage', store.read_index()['inputs']['injection'])

    def test_none_clears_sql_and_source_but_preserves_other_inputs_reports(self):
        attachment = self.root / 'upload.sql'
        attachment.write_bytes(b'-- original SQL source')
        store.save_input('source:injection', sources=[attachment])
        store.save_input('injection', content=b'-- extracted SQL')
        store.save_input('prompt', content=b'keep prompt')
        report = self.root / store.INPUTS / 'reports/1_prompt.md'
        report.parent.mkdir(parents=True)
        report.write_bytes(b'keep historical report')
        store.clear_input('injection', confirmed_unused=True)
        self.assertEqual(self.state()['state'], 'NOT_USED')
        self.assertFalse((self.root / store.INPUTS / store.SLOTS['injection']).exists())
        self.assertFalse((self.root / store.INPUTS / 'attachments/source/injection/upload.sql').exists())
        self.assertEqual((self.root / store.INPUTS / store.SLOTS['prompt']).read_bytes(), b'keep prompt')
        self.assertEqual(report.read_bytes(), b'keep historical report')

    def test_plain_or_legacy_clear_is_not_a_no_injection_answer(self):
        store.clear_input('injection')
        self.assertEqual(self.state()['state'], 'ASK')
        store.clear_input('injection', confirmed_unused=True)
        result = store.clear_input('injection')
        self.assertTrue(result['changed'])
        self.assertEqual(self.state()['state'], 'ASK')

    def test_empty_changed_and_missing_sql_cannot_turn_into_none(self):
        store.save_input('injection', content=b'')
        self.assertEqual(self.state()['state'], 'NEEDS_ATTENTION')
        store.save_input('injection', content=b'SELECT 1;')
        path = self.root / store.INPUTS / store.SLOTS['injection']
        path.write_bytes(b'changed')
        self.assertEqual(self.state()['state'], 'NEEDS_ATTENTION')
        path.unlink()
        self.assertEqual(self.state()['state'], 'NEEDS_ATTENTION')

    def test_legacy_sql_and_replacement_source_are_recognized(self):
        path = self.root / store.INPUTS / store.SLOTS['injection']
        path.parent.mkdir(parents=True)
        path.write_bytes(b'SELECT 1;')
        self.assertEqual(self.state()['state'], 'LEGACY_SUPPLIED')
        store.clear_input('injection', confirmed_unused=True)
        source = self.root / 'new.sql'
        source.write_bytes(b'SELECT 2;')
        store.save_input('source:injection', sources=[source])
        self.assertEqual(self.state()['state'], 'SOURCE_SUPPLIED')

    def test_answer_survives_separate_cli_processes(self):
        tool = self.root / 'Evals/tools/hg_store_input.py'
        tool.parent.mkdir(parents=True)
        shutil.copy2(Path(store.__file__), tool)
        shutil.copy2(Path(store.__file__).with_name('hg_universe.py'), tool.with_name('hg_universe.py'))
        def cli(*args):
            result = subprocess.run([sys.executable, str(tool), *args],
                                    capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        self.assertEqual(cli('list')['injection_intake']['state'], 'ASK')
        cli('no-injection')
        self.assertEqual(cli('list')['injection_intake']['state'], 'NOT_USED')
        self.assertFalse((self.root / store.INPUTS / 'reports').exists())


if __name__ == '__main__':
    unittest.main()
