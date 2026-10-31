"""Two universes picked by a per-task date: asked first, saved, never defaulted."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_injection_lint as lint
import hg_rubric_loop as loop
import hg_store_input as store
import hg_universe as universe
import hg_write_output as writer
from test_hg_injection_lint import Fixture, flags
from test_hg_report_contract import report
from universe_fixture import select

REAL = universe.ROOT


class DateAnswers(unittest.TestCase):
    def test_both_dates_accept_the_offered_wordings(self):
        for answer in ('2025-10-01', 'Oct 1', 'oct 1, 2025', 'October 1 2025', 'synth-cut', 'Synthcut',
                       'Oct 1, 2025 (synth-cut)'):
            self.assertEqual(universe.parse(answer), 'synthcut', answer)
        for answer in ('2026-02-14', 'Feb 14', 'feb 14, 2026', 'February 14, 2026', 'normal',
                       'Feb 14, 2026 (normal)'):
            self.assertEqual(universe.parse(answer), 'normal', answer)

    def test_anything_else_is_rejected_with_the_question(self):
        for answer in ('', 'Feb 15', '2026-02-28', 'today', 'Oct 1 or Feb 14', 'Dec 25'):
            with self.subTest(answer=answer), self.assertRaisesRegex(ValueError, 'Which date is this task on'):
                universe.parse(answer)

    def test_clocks(self):
        self.assertEqual(universe.UNIVERSES['normal']['clock'].isoformat(), '2026-02-14T00:00:00+00:00')
        # Synth-cut data ends 2025-09-30 23:59:59 PT, so its clock is the next PT midnight.
        self.assertEqual(universe.UNIVERSES['synthcut']['clock'].isoformat(), '2025-10-01T07:00:00+00:00')
        self.assertFalse(universe.UNIVERSES['synthcut']['shutdown_rules'])
        self.assertTrue(universe.UNIVERSES['normal']['shutdown_rules'])


class SavedDate(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        scope = patch.object(store, 'REPOSITORY', self.root)
        scope.start()
        self.addCleanup(scope.stop)

    def save(self, answer):
        return store.save_input('universe', content=answer.encode())

    def test_no_saved_date_stops_every_universe_read(self):
        with self.assertRaises(universe.UniverseNotSelected):
            universe.selected(self.root)
        with self.assertRaises(universe.UniverseNotSelected):
            universe.manifest_path(self.root)
        intake = store.inventory()['universe_intake']
        self.assertEqual((intake['state'], intake['ask']), ('ASK', True))
        self.assertEqual(intake['question'], universe.QUESTION)

    def test_answer_is_saved_canonically_and_reused(self):
        self.save('Oct 1, 2025 (synth-cut)')
        saved = self.root / 'Evals/task_inputs/02_Universe_Date.txt'
        self.assertEqual(saved.read_text(), '2025-10-01\n')
        self.assertEqual(universe.selected(self.root), 'synthcut')
        intake = store.inventory()['universe_intake']
        self.assertEqual((intake['state'], intake['ask'], intake['key']), ('SELECTED', False, 'synthcut'))
        self.assertEqual(intake['report_line'], 'Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)')
        self.assertEqual(universe.manifest_path(self.root),
                         self.root / 'Evals/references/universes/synthcut/universe_manifest.json')

    def test_unrecognized_answer_saves_nothing(self):
        with self.assertRaises(ValueError):
            self.save('sometime in February')
        self.assertEqual(store.inventory()['universe_intake']['state'], 'ASK')

    def test_explicit_change_replaces_the_date(self):
        self.save('normal')
        self.save('2025-10-01')
        self.assertEqual(universe.selected(self.root), 'synthcut')

    def test_edited_date_file_is_not_trusted(self):
        self.save('Feb 14')
        (self.root / 'Evals/task_inputs/02_Universe_Date.txt').write_text('2025-10-01\n')
        with self.assertRaises(universe.UniverseNotSelected):
            universe.selected(self.root)
        self.assertEqual(store.inventory()['universe_intake']['state'], 'NEEDS_ATTENTION')

    def test_file_upload_cannot_set_the_date(self):
        upload = self.root / 'date.txt'
        upload.write_text('2026-02-14\n')
        with self.assertRaises(ValueError):
            store.save_input('universe', [upload])

    def test_review_context_needs_and_binds_the_date(self):
        with self.assertRaises(universe.UniverseNotSelected):
            loop.review_context(self.root)
        self.save('Feb 14')
        feb = loop.review_context(self.root)
        self.assertIn('Evals/references/universes/normal/universe_manifest.json', feb['manifest']['references'])
        self.assertIn('universe', feb['manifest']['inputs'])
        self.save('Oct 1')
        octo = loop.review_context(self.root)
        self.assertIn('Evals/references/universes/synthcut/source_layout.json', octo['manifest']['references'])
        self.assertNotEqual(feb['sha256'], octo['sha256'])


class ReportClockLine(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        scope = patch.object(writer, 'REPOSITORY', self.root)
        scope.start()
        self.addCleanup(scope.stop)
        self.feb = report('NON-FAIL', 'PARTIAL', limits='Schema unavailable', stage='injection')

    def test_new_report_needs_the_saved_date(self):
        select(self.root, 'synthcut')
        with self.assertRaisesRegex(ValueError, 'Clock line must show the saved task date: Clock: 2025-10-01'):
            writer.save_output('injection', self.feb)
        oct_line = universe.report_line('synthcut')
        saved = writer.save_output('injection', self.feb.replace(universe.report_line('normal'), oct_line))
        self.assertEqual(saved['clock'], oct_line.removeprefix('Clock: '))

    def test_missing_clock_line_is_rejected(self):
        select(self.root, 'normal')
        with self.assertRaisesRegex(ValueError, 'task date line: Clock: 2026-02-14'):
            writer.save_output('injection', self.feb.replace(universe.report_line('normal') + '\n', ''))

    def test_no_saved_date_blocks_saving(self):
        with self.assertRaises(universe.UniverseNotSelected):
            writer.save_output('injection', self.feb)


class LintClock(unittest.TestCase):
    SQL = """
INSERT INTO slack.slack_messages (id, ts, channel_id, user_id, text) VALUES
  ('pt_evening', '2025-10-01T06:30:00Z', 'C1', 'EMPLOYEE_0025_SLACK_ID', 'Sep 30 11:30 PM PT'),
  ('oct_morning', '2025-10-01T08:00:00Z', 'C1', 'EMPLOYEE_0025_SLACK_ID', 'Oct 1 1:00 AM PT'),
  ('feb_after', '2026-02-14T00:01:00Z', 'C1', 'EMPLOYEE_0025_SLACK_ID', 'after the Feb clock');
"""

    def setUp(self):
        self.fx = Fixture()
        self.addCleanup(self.fx.temp.cleanup)

    def hits(self, key):
        result = self.fx.run(self.SQL, checks=('future_date',), universe=key)
        self.assertEqual(result['universe'], key)
        return {f['record'] for f in flags(result, 'future_date')}, result['clock']

    def test_each_universe_uses_its_own_clock(self):
        self.assertEqual(self.hits('synthcut'), ({'oct_morning', 'feb_after'}, '2025-10-01T07:00:00Z'))
        self.assertEqual(self.hits('normal'), ({'feb_after'}, '2026-02-14T00:00:00Z'))

    def test_saved_date_is_the_default_for_the_lint(self):
        select(self.fx.root, 'synthcut')
        result = self.fx.run(self.SQL, checks=('future_date',))
        self.assertEqual(result['universe'], 'synthcut')
        self.assertIn('2025-10-01 00:00 PT', flags(result, 'future_date')[0]['message'])


class Documentation(unittest.TestCase):
    def test_every_skill_asks_the_same_question_first(self):
        for skill in ('prompt', 'oe', 'rubric', 'injection', 'hardness'):
            text = (REAL / 'claude/skills' / skill / 'SKILL.md').read_text()
            with self.subTest(skill=skill):
                self.assertIn('**Task date first.**', text)
                self.assertIn(universe.QUESTION, text)
                self.assertLess(text.index('**Task date first.**'), text.index('Evals/INPUTS.md'))
        self.assertIn(universe.QUESTION, (REAL / 'Evals/INPUTS.md').read_text())
        self.assertIn(universe.QUESTION.split(':')[0], (REAL / 'claude/CLAUDE.md').read_text())

    def test_environment_documents_both_clocks_and_the_cut(self):
        text = (REAL / 'Evals/ENVIRONMENT.md').read_text()
        for entry in universe.UNIVERSES.values():
            self.assertIn(entry['folder'], text)
        self.assertIn('Clock **2025-10-01 00:00 PT (2025-10-01 07:00 UTC)**', text)
        self.assertIn('Clock **2026-02-14 00:00 UTC**', text)
        self.assertIn('Victor Barnes left in April 2025', text)
        self.assertIn('"today" is Wednesday, October 1, 2025', text)

    def test_shutdown_premise_is_scoped_to_feb_14(self):
        recheck = (REAL / 'Evals/references/rules/deep_recheck.md').read_text()
        self.assertIn('On a Feb 14 task, a premise that the company still runs', recheck)
        self.assertIn('business as usual is not', recheck)
        eval1 = (REAL / 'Evals/1_Prompt_Eval.md').read_text()
        self.assertIn('The shutdown part applies to Feb 14 tasks only.', eval1)


@unittest.skipUnless(all((REAL / e['folder']).is_dir() for e in universe.UNIVERSES.values()),
                     'universe folders not present')
class RealUniverses(unittest.TestCase):
    def test_every_routed_service_exists_with_its_manifest(self):
        for key, entry in universe.UNIVERSES.items():
            manifest = json.loads(universe.manifest_path(REAL, key).read_text())
            self.assertEqual(manifest['universe'], key)
            self.assertEqual(len(manifest['services']), 13)
            for service, info in manifest['services'].items():
                with self.subTest(universe=key, service=service):
                    self.assertTrue(info['path'].startswith(entry['folder'] + '/'))
                    source = json.loads((REAL / info['path'] / 'source_manifest.json').read_text())
                    self.assertEqual(source['file_count'], info['file_count'])

    def test_prepared_indexes_are_pinned_to_their_own_universe(self):
        for key in universe.UNIVERSES:
            manifest = json.loads(universe.manifest_path(REAL, key).read_text())
            for kind in ('search_indexes', 'id_indexes'):
                package = json.loads((universe.references(REAL, key) / kind / 'manifest.json').read_text())
                for entry in package['indexes']:
                    with self.subTest(universe=key, kind=kind, service=entry['service']):
                        folder = REAL / manifest['services'][entry['service']]['path']
                        files = json.loads((folder / 'source_manifest.json').read_text())['files']
                        self.assertEqual(next(f['sha256'] for f in files if f['path'] == entry['file']),
                                         entry['source_sha256'])

    def test_synth_cut_lacks_the_later_storylines(self):
        later = ('combo-fighter', 'zombie-match-lite', 'telegram-dd', 'ui-sprite-optimization',
                 'barbie-idle-life-sim', 'web-distribution-partnership')
        for key, expected in (('normal', True), ('synthcut', False)):
            folder = REAL / universe.base_folder(key, 'Other_Services') / 'metadata'
            names = [p.name for p in folder.iterdir()]
            for part in later:
                with self.subTest(universe=key, storyline=part):
                    self.assertEqual(any(part in n for n in names), expected)


if __name__ == '__main__':
    unittest.main()
