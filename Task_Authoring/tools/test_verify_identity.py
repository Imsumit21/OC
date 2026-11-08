"""Follow-up adversarial identity verification; fixtures only under support/scratch."""
import json
import hashlib
import tempfile
import unittest
from pathlib import Path

import stage_evidence as se
import trajectory_ledger as tl


SCRATCH = Path(__file__).resolve().parents[1] / 'support' / 'scratch'


class VerificationIdentity(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='verify-identity-', dir=SCRATCH)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def args(self):
        return dict(stage='scenario', revision='r1', inputs={'assignment': 'abc'}, upstream={},
                    checks=[{'id': 'check', 'outcome': 'PASS'}], availability=[],
                    reviewer='reviewer', tool_identity='v1', policy_identity='policy',
                    producer={'name': 'stage_gate', 'verdict': 'PASS', 'rerun': 'all'})

    def test_precheck_does_not_require_or_depend_on_later_oe_rubric(self):
        (self.root / '04_Prompt.txt').write_text('Prepare the requested schedule.\n')
        absent = self.root / '09_Rubrics.json'
        original = tl.binding_bundle_hash(self.root, absent, stage='precheck')
        absent.write_text('[]')
        (self.root / '08_Oracle_Events.md').write_text('Later review.\n')
        self.assertEqual(original, tl.binding_bundle_hash(self.root, absent, stage='precheck'))
        baseline = tl.binding_bundle_hash(self.root, absent)
        absent.write_text('[{"title":"Required outcome"}]')
        self.assertNotEqual(baseline, tl.binding_bundle_hash(self.root, absent))

    def test_generated_certificate_does_not_change_submitted_identity(self):
        friction = self.root / '03_Error_Async_Config.txt'
        friction.write_text('Friction: none\n')
        before = tl.binding_bundle_hash(self.root)
        friction.write_text(friction.read_text() + '\n```\nSTAGE GATE error-async: PASS\n[PASS] check: result\n```\n')
        self.assertEqual(before, tl.binding_bundle_hash(self.root))
        friction.write_text(friction.read_text() + 'Changed configured behavior.\n')
        self.assertNotEqual(before, tl.binding_bundle_hash(self.root))

    def test_attestation_preserves_producer_and_rejects_outside_output(self):
        args = self.args()
        record = se.attest(self.root, **args)
        self.assertEqual(record['producer'], args['producer'])
        self.assertEqual([], se.validate(record, task_id=se.task_identity(self.root), stage='scenario',
                                         inputs=args['inputs'], upstream={}))
        outside = Path('/private/tmp') / self.root.name
        with self.assertRaises(ValueError):
            se.attest(outside, **args)
        self.assertFalse(outside.exists())

    def test_lock_symlink_cannot_write_through(self):
        directory = self.root / se.DIRECTORY
        directory.mkdir(parents=True)
        target = self.root / 'other-lock'
        target.write_text('untouched')
        (directory / '.lock').symlink_to(target)
        with self.assertRaises(OSError):
            se.attest(self.root, **self.args())
        self.assertEqual(target.read_text(), 'untouched')

    def test_index_path_traversal_is_rejected(self):
        directory = self.root / se.DIRECTORY
        directory.mkdir(parents=True)
        (directory / 'index.json').write_text(json.dumps({'scenario': '../../outside'}))
        with self.assertRaises(ValueError):
            se.latest(self.root, 'scenario')
        with self.assertRaises(ValueError):
            se.attest(self.root, **self.args())

    def test_evaluator_difference_needs_current_substantive_evidence(self):
        proof = self.root / 'compatibility.txt'
        proof.write_text('Reviewed the releases: only presentation wording changed, no criterion or policy semantics changed.')
        review = {'local': 'release-a', 'reported': 'release-b', 'compatible': True, 'reviewer': 'reviewer',
                  'reason': 'Compared the exact release policy changes and unchanged task-specific grading.',
                  'evidence_refs': [{'path': 'compatibility.txt', 'sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
                                     'reason': 'Release comparison evidence.'}]}
        self.assertEqual('REVIEW_REQUIRED', se.evaluator_compatibility('release-a', 'release-b', review)['status'])
        self.assertEqual('REVIEWED_COMPATIBLE', se.evaluator_compatibility('release-a', 'release-b', review, task_dir=self.root)['status'])
        review['reason'] = 'reviewed'
        self.assertEqual('REVIEW_REQUIRED', se.evaluator_compatibility('release-a', 'release-b', review, task_dir=self.root)['status'])
        review['reason'] = 'Compared policy semantics and task-specific grading.'
        proof.write_text('Unreviewed policy change.')
        self.assertEqual('REVIEW_REQUIRED', se.evaluator_compatibility('release-a', 'release-b', review, task_dir=self.root)['status'])


if __name__ == '__main__':
    unittest.main()
