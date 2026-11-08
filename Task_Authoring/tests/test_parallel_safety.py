"""Isolated task selection and real concurrent ledger transactions."""
import json
import multiprocessing
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
import task_context as tc
import runtime_context as runtime
from hardness_ledger import Ledger


def record(task, verdict='LANDED'):
    return dict(kind='verdict', task=task, revision='r1', source='platform-baseline',
                model='claude-opus-4-8', harness={'name': 'fixture', 'version': '1'},
                epistemic='observed', run='one', node='A', family='A15', verdict=verdict)


def append_worker(path, task, verdict, barrier, result):
    ledger = Ledger(path)  # deliberately capture stale state before anyone commits
    barrier.wait(timeout=20)
    result.put(ledger.append([record(task, verdict)]))


class ParallelSafety(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='isolation-', dir=TOOLS.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.tasks = []
        for index in range(4):
            task = self.root / ('task_inputs' + str(index))
            task.mkdir()
            (task / '00_Assigments.md').write_text('spec_version: V3\n')
            (task / 'prompt.txt').write_text(str(index))
            self.tasks.append(task)

    def test_ambiguous_default_and_valid_explicit_single_flow(self):
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(tc, 'BUNDLE', self.root):
            with self.assertRaises(tc.ContextError):
                tc.select_task()
            self.assertEqual(tc.select_task(self.tasks[1]), self.tasks[1])
            self.assertEqual(tc.select_task(artifact_paths=[self.tasks[2] / 'prompt.txt']), self.tasks[2])
            with mock.patch.object(tc, 'BUNDLE', self.tasks[0].parent / 'single'):
                tc.BUNDLE.mkdir()
                single = tc.BUNDLE / 'task_inputs'
                single.mkdir()
                (single / '00_Assigments.md').write_text('spec_version: V3\n')
                self.assertEqual(tc.select_task(), single)

    def test_mixed_paths_including_future_outputs_and_symlinks(self):
        a, b = self.tasks[:2]
        for path in (b / 'prompt.txt', b / 'Working_Files' / 'future.json'):
            with self.assertRaises(tc.ContextError):
                tc.validate_task_paths(a, [path])
        alias = a / 'alias.txt'
        alias.symlink_to(b / 'prompt.txt')
        with self.assertRaises(tc.ContextError):
            tc.validate_task_paths(a, [alias])
        with self.assertRaises(tc.ContextError):
            tc.select_task(a, artifact_paths=[a / 'prompt.txt', b / 'prompt.txt'])

    def test_cli_rejects_foreign_artifact_before_activation(self):
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(sys, 'argv', [
            'base_check.py', '--task-dir', str(self.tasks[0]), str(self.tasks[1] / 'prompt.txt')]), \
                mock.patch.object(runtime, 'activate') as activation:
            with self.assertRaises(tc.ContextError):
                runtime.cli_entry({})
            activation.assert_not_called()

    def run_concurrent(self, entries):
        path = self.root / 'ledger.jsonl'
        ctx = multiprocessing.get_context('spawn')
        barrier, result = ctx.Barrier(4), ctx.Queue()
        processes = [ctx.Process(target=append_worker, args=(path, task, verdict, barrier, result))
                     for task, verdict in entries]
        for process in processes:
            process.start()
        reports = [result.get(timeout=30) for _ in processes]
        for process in processes:
            process.join(30)
            self.assertEqual(process.exitcode, 0)
        return Ledger(path), reports

    def test_four_distinct_appends_and_task_local_outputs_survive(self):
        ledger, reports = self.run_concurrent([(str(t), 'LANDED') for t in self.tasks])
        self.assertEqual(len(ledger.records), 4)
        self.assertEqual({r['task'] for r in ledger.records}, set(map(str, self.tasks)))
        self.assertTrue(all(len(r['added']) == 1 and not r['rejected'] for r in reports))
        for index, task in enumerate(self.tasks):
            self.assertEqual((task / 'prompt.txt').read_text(), str(index))

    def test_concurrent_duplicate_identity_is_idempotent(self):
        ledger, reports = self.run_concurrent([('task-A', 'LANDED')] * 4)
        self.assertEqual(len(ledger.records), 1)
        self.assertEqual(sum(len(r['added']) for r in reports), 1)
        self.assertEqual(sum(len(r['present']) for r in reports), 3)

    def test_concurrent_conflicting_identity_rejects(self):
        ledger, reports = self.run_concurrent([('task-A', v) for v in ['LANDED', 'LEAKED'] * 2])
        self.assertEqual(len(ledger.records), 1)
        self.assertEqual(sum(len(r['added']) for r in reports), 1)
        self.assertEqual(sum(len(r['rejected']) for r in reports), 2)

    def test_entity_build_publishes_without_shared_temporary(self):
        import entity
        target = self.root / 'entities.json'
        old_shared_temp = target.with_suffix('.tmp')
        old_shared_temp.write_text('must remain untouched')
        with mock.patch.object(entity, 'build', return_value={'fixture': 'new'}):
            self.assertEqual(entity.build_to(target), {'fixture': 'new'})
        self.assertEqual(json.loads(target.read_text()), {'fixture': 'new'})
        self.assertEqual(old_shared_temp.read_text(), 'must remain untouched')

    def test_stale_instance_reload_and_supersession(self):
        path = self.root / 'ledger.jsonl'
        stale, first = Ledger(path), Ledger(path)
        rid = first.append([record('A')])['added'][0]
        self.assertEqual(stale.append([record('A')])['present'], [rid])
        changed = dict(record('A', 'LEAKED'), supersedes=rid)
        self.assertEqual(len(stale.append([changed])['added']), 1)
        self.assertEqual(Ledger(path).current()[0]['verdict'], 'LEAKED')
        self.assertEqual(len(Ledger(path).records), 2)


if __name__ == '__main__':
    unittest.main()
