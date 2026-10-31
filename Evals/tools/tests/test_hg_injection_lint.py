"""hg_injection_lint: static injection checks. Calibration snippets are real SQL from the Kelvin 50
(task ids in each test); #26's .txt row is rebuilt from its verification notes because the submitted
SQL omits that layer."""
import contextlib
import io
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_injection_lint as lint
import hg_universe
from universe_fixture import routing, select

REAL = lint.ROOT
NORMAL_OTHER = hg_universe.base_folder('normal', 'Other_Services')
PDF = b'%PDF-1.4\n1 0 obj << /Type /Catalog >> endobj\nMattel status note: fundability numbers.\n%%EOF\n'


class Fixture:
    """A tiny root: the bundle's schema and contracts plus a few base records."""

    def __init__(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        schema = root / 'Evals/references/schema'
        schema.mkdir(parents=True)
        for name in ('injection.json', 'id_contracts.json'):
            shutil.copy2(REAL / 'Evals/references/schema' / name, schema / name)
        base = root / 'base'
        services = {s: {'path': 'base/' + s} for s in ('trello', 'slack', 'gmail', 'gdrive', 'linear', 'contacts')}
        select(root).write_text(json.dumps({'services': services}))
        for s in services:
            (base / s).mkdir(parents=True)
        (base / 'trello/data.json').write_text(json.dumps({'members': [
            {'id': '904fe5def35c5dddd2037d69', 'username': 'victor.barnes', 'fullName': 'Victor Barnes'},
            {'id': '919ee44a0d5157b7839f66a8', 'username': 'owen.baker', 'fullName': 'Owen Baker'},
            {'id': '4bc5d398e54226f344ad3abc', 'username': 'claire.morgan', 'fullName': 'Claire Morgan'},
            {'id': 'PERSON_6092_TRELLO_USER_ID', 'username': 'PERSON_6092_TRELLO_USERNAME',
             'fullName': 'PERSON_6092_NAME'}], 'actions': []}))
        (base / 'slack/users.json').write_text(json.dumps([
            {'id': 'EMPLOYEE_0025_SLACK_ID', 'name': 'Arthur Blake', 'real_name': 'Arthur Blake',
             'display_name': 'Arthur Blake', 'email': 'arthur.blake@harmonygames.co'},
            {'id': 'EMPLOYEE_0030_SLACK_ID', 'name': 'Victor Barnes', 'real_name': 'Victor Barnes',
             'display_name': 'Victor Barnes', 'email': 'victor.barnes@harmonygames.co'}]))
        (base / 'gmail/users.json').write_text(json.dumps([
            {'emailAddress': 'marcus@harmonygames.co'}, {'emailAddress': 'robert@harmonygames.co'},
            {'emailAddress': 'leonard.hayes@harmonygames.co'}, {'emailAddress': 'arthur.blake@harmonygames.co'}]))
        (base / 'gdrive/data.json').write_text(json.dumps({'drive_users': [], 'drive_files': []}))
        pdf = base / 'gdrive/root/leonard.hayes@harmonygames.co/Mattel Partnership - Final Status Note (Feb 2026).pdf'
        pdf.parent.mkdir(parents=True)
        pdf.write_bytes(PDF)
        (base / 'linear/data.json').write_text(json.dumps({'users': [{'id': 'usr_eac7fcafa75e4935',
                                                                      'email': 'simon.walker@harmonygames.co'}]}))
        (base / 'contacts/contacts.json').write_text(json.dumps({'contacts': []}))
        self.root = root

    def run(self, sql, **kw):
        return lint.lint(sql, root=self.root, **kw)

    def close(self):
        self.temp.cleanup()


def flags(result, check=None, severity=None):
    return [f for f in result['flags'] if (check is None or f['check'] == check)
            and (severity is None or f['severity'] == severity)]


class LintTestCase(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture()

    def tearDown(self):
        self.fx.close()


# #1 6a7f62daa0495108140f6b43 (trimmed: card text shortened, same ids, dates and columns)
TASK1 = """BEGIN;
INSERT INTO trello.trello_cards
  (id, name, "idBoard", "idList", "desc", pos, closed, due,
   "dueComplete", "idMembers_json", "idLabels_json", "idShort",
   "shortLink", "shortUrl", url, "dateLastActivity")
VALUES
  ('69a08f48b6c1e2d3f4a5b6c7', 'Backend merge-review control gate — Owen', '640643a3fd8f3ca308d9318e', '641359135e6148b9de0e076c',
   $card$Arthur wants a historical merge-control assessment before the March live-ops work is staffed.$card$, 32768, false, '2026-02-27T18:00:00Z',
   false, '["919ee44a0d5157b7839f66a8"]', '[]', 457, 'mrgOwen1',
   'https://PERSON_6092_TRELLO_USERNAME.com/c/mrgOwen1',
   'https://PERSON_6092_TRELLO_USERNAME.com/c/mrgOwen1/457-backend-merge-review-control-gate-owen',
   '2026-02-13T18:22:01Z')
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  "dateLastActivity" = EXCLUDED."dateLastActivity";

INSERT INTO trello.trello_actions
  (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json)
VALUES
  ('69a08f46b6c1e2d3f4a5b6c6', 'createCard', '2026-02-24T16:10:00Z',
   '919ee44a0d5157b7839f66a8', '640643a3fd8f3ca308d9318e', '69a08f45b6c1e2d3f4a5b6c5',
   '{"card":{"id":"69a08f45b6c1e2d3f4a5b6c5","name":"Backend merge readiness pulse — working draft","idShort":456},"list":{"id":"641359135e6148b9de0e076c","name":"Backlog"},"board":{"id":"640643a3fd8f3ca308d9318e","name":"Harmony Games"}}')
ON CONFLICT (id) DO NOTHING;

UPDATE trello.trello_boards
SET "dateLastActivity" = GREATEST(
  COALESCE("dateLastActivity", '1970-01-01T00:00:00Z'::timestamptz),
  '2026-02-26T18:22:01Z'::timestamptz
)
WHERE id = '640643a3fd8f3ca308d9318e';
COMMIT;
"""


class FutureDateTests(LintTestCase):
    def test_task1_create_card_after_clock_fails_and_due_date_passes(self):
        result = self.fx.run(TASK1, checks=('future_date',))
        found = {(f['table'], f['column'], f['value']) for f in flags(result, 'future_date')}
        self.assertIn(('trello.trello_actions', 'date', '2026-02-24T16:10:00Z'), found)
        self.assertTrue(any(t == 'trello.trello_boards' and c == 'datelastactivity' for t, c, _ in found))
        self.assertFalse(any(c == 'due' for _, c, _ in found))
        self.assertFalse(any(t == 'trello.trello_cards' for t, _, _ in found))  # Feb 13 activity, Feb 27 due
        self.assertTrue(all(f['severity'] == 'FAIL' for f in flags(result, 'future_date')))

    def test_clock_boundary_offsets_epochs_and_plan_fields(self):
        sql = """
INSERT INTO slack.slack_messages (id, ts, channel_id, user_id, text) VALUES
  ('m1', '1771027200.000000', 'C1', 'EMPLOYEE_0025_SLACK_ID', 'at the clock'),
  ('m2', '1771027260.000100', 'C1', 'EMPLOYEE_0025_SLACK_ID', 'one minute after');
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, internal_date, date) VALUES
  ('g1', 't1', 'robert@harmonygames.co', 1771027200000, '2026-02-13T16:30:00-08:00');
INSERT INTO gcal.gcal_events (event_id, calendar_id, summary, start_ts, end_ts, created) VALUES
  ('e1', 'c1', 'Monday sync', '2026-02-16T17:00:00Z', '2026-02-16T17:30:00Z', '2026-02-12T10:00:00Z');
INSERT INTO linear.linear_issues (id, identifier, title, due_date, created_at) VALUES
  ('i1', 'ENG-1', 'Close-out', '2026-03-06', now());
"""
        result = self.fx.run(sql, checks=('future_date',))
        hits = {(f['record'], f['column']) for f in flags(result, 'future_date')}
        self.assertEqual(hits, {('m2', 'ts'), ('g1', 'date'), ('i1', 'created_at')})


# #32 6aa8272b1b7a2df0fc0fea7b
TASK32 = """INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES (
  '1872142026008101',
  'robert@harmonygames.co',
  'Need you to own the weekend product freeze register before the Monday huddle.',
  'hf_pf_reg_1'
);
INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES
  ('robert@harmonygames.co/1872142026008109', 'robert@harmonygames.co', 'ok', NULL),
  ('robert@harmonygames.co/1872142026008110', 'robert@harmonygames.co', 'ok', '98123456');
"""

# #42 6abd857f96a9f77c7e518348
TASK42 = """INSERT INTO gdrive.drive_files
  (id, name, mime_type, parents_json, owner_email, shared_with_emails_json, shared_roles_json,
   visibility_role, shared_groups_json, visibility, owners_json, modified_time, created_time, size,
   trashed, starred, content_path, web_view_link, icon_link, description, drive_id, content_text)
VALUES (
  'drv_uacreativerecap_pdf_202601', 'UA Creative Recap - Jan 2026.pdf', 'application/pdf',
  '["root/marcus.bennett@harmonygames.co"]', 'marcus.bennett@harmonygames.co',
  '["frederick.stone@harmonygames.co","claire.morgan@harmonygames.co"]', '["writer"]',
  'reader', '[]', 'private', '["marcus.bennett@harmonygames.co"]',
  '2026-01-21T16:00:00Z', '2026-01-21T16:00:00Z', 182400, false, false,
  'root/marcus.bennett@harmonygames.co/UA Creative Recap - Jan 2026.pdf', NULL, NULL,
  'Exported copy of the UA Creative Recap sheet + sign-off addendum, compiled for the leadership decision.',
  NULL, NULL
);
"""


class IdContractTests(LintTestCase):
    def test_task32_label_history_id_fails_and_digits_or_null_pass(self):
        result = self.fx.run(TASK32, checks=('id_contract',))
        bad = flags(result, 'id_contract')
        self.assertEqual([(f['value'], f['severity']) for f in bad], [('hf_pf_reg_1', 'FAIL')])
        self.assertIn('gmail_history_id', bad[0]['message'])

    def test_task42_root_prefixed_content_path_fails(self):
        result = self.fx.run(TASK42, checks=('id_contract',))
        bad = flags(result, 'id_contract')
        self.assertEqual(len(bad), 1)
        self.assertEqual(bad[0]['value'], 'root/marcus.bennett@harmonygames.co/UA Creative Recap - Jan 2026.pdf')
        self.assertIn('drive_content_path', bad[0]['message'])

    def test_content_path_must_start_with_the_owner(self):
        sql = """INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email, content_path) VALUES
          ('f1', 'a.pdf', 'application/pdf', 'robert@harmonygames.co', 'leonard.hayes@harmonygames.co/a.pdf'),
          ('f2', 'b.pdf', 'application/pdf', 'robert@harmonygames.co', 'robert@harmonygames.co/Plans/b.pdf'),
          ('f3', 'c.pdf', 'application/pdf', 'robert@harmonygames.co', '/robert@harmonygames.co/c.pdf');"""
        result = self.fx.run(sql, checks=('id_contract',))
        self.assertEqual(sorted(f['record'] for f in flags(result, 'id_contract')), ['f1', 'f3'])

    def test_contract_file_lists_the_two_agreed_fields(self):
        data = json.loads((REAL / lint.CONTRACTS).read_text())
        by_id = {c['id']: c for c in data['contracts']}
        self.assertEqual(set(by_id), {'gmail_history_id', 'drive_content_path'})
        for contract in by_id.values():
            re.compile(contract['pattern'])
            self.assertTrue(contract['base_evidence'] and contract['failure_evidence'])

    @unittest.skipUnless((REAL / NORMAL_OTHER / 'Services_Data/gdrive/data.json').is_file(),
                         'base Drive export not present')
    def test_drive_contract_holds_for_every_base_row(self):
        data = json.loads((REAL / NORMAL_OTHER / 'Services_Data/gdrive/data.json').read_text())
        contract = next(c for c in json.loads((REAL / lint.CONTRACTS).read_text())['contracts']
                        if c['id'] == 'drive_content_path')
        pattern = re.compile(contract['pattern'])
        paths = [(f['content_path'], f['owner_email']) for f in data['drive_files'] if f['content_path']]
        self.assertGreater(len(paths), 30000)
        self.assertEqual([p for p, o in paths if not pattern.fullmatch(p) or p.split('/', 1)[0] != o], [])


# #35 6abcef4dc5b130fe26c6025b
TASK35 = """INSERT INTO gdrive.drive_files
  (id, name, mime_type, parents_json, owner_email, shared_with_emails_json, visibility,
   owners_json, modified_time, created_time, trashed, starred, description)
VALUES (
  'd_mattel_status_note_inj01', 'Mattel Partnership - Final Status Note (Feb 2026).pdf', 'application/pdf',
  '["d_100f1286457509c5c59131"]', 'leonard.hayes@harmonygames.co', '[]', 'private',
  '["leonard.hayes@harmonygames.co"]', '2026-02-09T10:30:00Z', '2026-02-09T10:30:00Z', false, false,
  'One-page status note for the Feb 10 Mattel call: current fundability numbers, runway disclosure limits, and open vendor liabilities.'
);
"""
# #26 6aad7d1ec6922756b9ad396f: rebuilt from kelvin_check/VERIFIED.md (21 handoff_requirements.txt files,
# inj_dd_note_*, text/plain, every read returned 503 'content_path missing').
TASK26 = """INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email, content_path, content_text) VALUES
  ('inj_dd_note_nate_streak', 'handoff_requirements.txt', 'text/plain', 'marcus.bennett@harmonygames.co', NULL, NULL),
  ('inj_dd_note_lexi_streak', 'handoff_requirements.txt', 'text/plain', 'marcus.bennett@harmonygames.co', NULL,
   'Approved handoff take: take_03');
"""


class DriveReadableTests(LintTestCase):
    def test_task26_text_files_without_bytes_fail_even_with_content_text(self):
        result = self.fx.run(TASK26, checks=('drive_unreadable',))
        bad = {f['record']: f for f in flags(result, 'drive_unreadable', 'FAIL')}
        self.assertEqual(set(bad), {'inj_dd_note_nate_streak', 'inj_dd_note_lexi_streak'})
        self.assertIn('null content_path and empty content_text', bad['inj_dd_note_nate_streak']['message'])
        self.assertIn('content_text alone is not served', bad['inj_dd_note_lexi_streak']['message'])

    def test_task35_pdf_without_content_fails(self):
        result = self.fx.run(TASK35, checks=('drive_unreadable',))
        self.assertEqual([f['record'] for f in flags(result, 'drive_unreadable', 'FAIL')], ['d_mattel_status_note_inj01'])

    def test_pdf_with_real_bytes_passes_and_missing_bytes_fail(self):
        sql = TASK35.replace("'One-page", "'leonard.hayes@harmonygames.co/Mattel Partnership - Final Status Note "
                                          "(Feb 2026).pdf', 'One-page").replace(
            'trashed, starred, description)', 'trashed, starred, content_path, description)')
        self.assertEqual(flags(self.fx.run(sql, checks=('drive_unreadable',))), [])
        missing = sql.replace('Final Status Note (Feb 2026).pdf\', \'One', 'Final Status Note v2.pdf\', \'One')
        bad = flags(self.fx.run(missing, checks=('drive_unreadable',)), 'drive_unreadable')
        self.assertEqual(len(bad), 1)
        self.assertIn('points at no bytes', bad[0]['message'])

    def test_task42_root_path_is_also_unreadable(self):
        bad = flags(self.fx.run(TASK42, checks=('drive_unreadable',)), 'drive_unreadable')
        self.assertEqual([f['record'] for f in bad], ['drv_uacreativerecap_pdf_202601'])

    def test_google_doc_needs_a_docs_row_with_body(self):
        # The 073709 fix: same id, Google Doc mime, docs_documents row carrying the text.
        sql = """INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email) VALUES
          ('f_doc_ok', 'EXPORT_NOTES.txt', 'application/vnd.google-apps.document', 'marcus.bennett@harmonygames.co'),
          ('f_doc_empty', 'THIRD_PARTY.txt', 'application/vnd.google-apps.document', 'marcus.bennett@harmonygames.co'),
          ('f_doc_none', 'NOTES.txt', 'application/vnd.google-apps.document', 'marcus.bennett@harmonygames.co');
        INSERT INTO gdocs.docs_documents (document_id, title, body_text, drive_file_id) VALUES
          ('f_doc_ok', 'EXPORT_NOTES.txt', 'Package: InfiniteLives_Anim' || chr(10) || 'Status: done', 'f_doc_ok'),
          ('f_doc_empty', 'THIRD_PARTY.txt', '', 'f_doc_empty');"""
        bad = sorted(f['record'] for f in flags(self.fx.run(sql, checks=('drive_unreadable',)), 'drive_unreadable'))
        self.assertEqual(bad, ['f_doc_empty', 'f_doc_none'])

    def test_media_without_bytes_is_info_not_fail(self):
        sql = """INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email) VALUES
          ('f_mp4', 'ZM3D_Square_Zoomed_v1_sfx.mp4', 'video/mp4', 'marcus.bennett@harmonygames.co'),
          ('f_pkg', 'InfiniteLives_Anim.unitypackage', 'application/octet-stream', 'marcus.bennett@harmonygames.co'),
          ('f_dir', 'Exports', 'application/vnd.google-apps.folder', 'marcus.bennett@harmonygames.co');"""
        result = self.fx.run(sql, checks=('drive_unreadable',))
        self.assertEqual(flags(result), [])
        self.assertTrue(any('2 injected media/binary' in i['message'] for i in result['info']))


# #43 6a83fa91fea987ea2b173deb
TASK43 = """BEGIN;
INSERT INTO trello.trello_members (
  id, username, "fullName", initials, "avatarUrl", bio, url, "memberType", confirmed
) VALUES (
  'PERSON_6098_TRELLO_USER_ID',
  'victor_barnes',
  'Victor Barnes',
  'VB',
  NULL,
  'Game Engineer at Harmony Games · victor.barnes@harmonygames.co',
  'https://PERSON_6092_TRELLO_USERNAME.com/u/victor_barnes',
  'normal',
  TRUE
);
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", "data_json")
VALUES ('69a1c688625908c4d2da469a', 'createCard', '2026-02-13T16:30:00+00:00'::timestamptz,
  'PERSON_6098_TRELLO_USER_ID', '640643a3fd8f3ca308d9318e', '69a1c6882806636ff08de0b7', $json$
{"board": {"id": "640643a3fd8f3ca308d9318e", "name": "Harmony Games"}}
$json$);
COMMIT;
"""


class IdentityTests(LintTestCase):
    def test_task43_second_trello_account_for_victor_fails(self):
        result = self.fx.run(TASK43, checks=('identities',))
        dup = flags(result, 'duplicate_account')
        self.assertEqual(len(dup), 1)
        self.assertEqual(dup[0]['severity'], 'FAIL')
        self.assertIn('904fe5def35c5dddd2037d69 (Victor Barnes)', dup[0]['message'])
        self.assertIn('real namesake', dup[0]['message'])
        self.assertEqual(flags(result, 'unknown_actor'), [])  # the action resolves to the new SQL account

    def test_reusing_the_base_account_or_a_different_person_passes(self):
        sql = """INSERT INTO trello.trello_members (id, username, "fullName") VALUES
          ('904fe5def35c5dddd2037d69', 'victor.barnes', 'Victor Barnes')
          ON CONFLICT (id) DO NOTHING;
        INSERT INTO trello.trello_members (id, username, "fullName") VALUES ('new_member_1', 'victoria.lane', 'Victoria Lane');"""
        self.assertEqual(flags(self.fx.run(sql, checks=('identities',)), 'duplicate_account'), [])

    def test_sender_must_be_the_person_the_message_names(self):
        sql = """INSERT INTO gmail.gmail_messages (id, thread_id, user_email, from_email, from_name, date) VALUES
          ('m1', 't1', 'robert@harmonygames.co', 'arthur.blake@harmonygames.co', 'Victor Barnes', '2026-02-12T10:00:00Z'),
          ('m2', 't1', 'robert@harmonygames.co', 'arthur.blake@harmonygames.co', 'arthur blake', '2026-02-12T11:00:00Z');"""
        bad = flags(self.fx.run(sql, checks=('identities',)), 'actor_name')
        self.assertEqual([f['record'] for f in bad], ['m1'])

    def test_mailbox_that_is_not_a_base_gmail_user_is_a_check(self):
        sql = """INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES
          ('marcus.bennett@harmonygames.co/1769612800000001', 'marcus.bennett@harmonygames.co', 'recap', NULL);"""
        bad = flags(self.fx.run(sql, checks=('identities',)), 'unknown_actor')
        self.assertEqual(len(bad), 1)
        self.assertEqual(bad[0]['severity'], 'CHECK')
        self.assertIn('marcus@harmonygames.co', bad[0]['message'])
        # #42 6abd857f96a9f77c7e518348 creates the mailbox in the same SQL: no flag.
        created = """INSERT INTO gmail.gmail_users (email_address, name, messages_total, threads_total, history_id, created_at)
VALUES
  ('leonard.hayes@harmonygames.co', 'Leonard Hayes', 0, 0, NULL, NULL),
  ('marcus.bennett@harmonygames.co', 'Marcus Bennett', 1, 1, NULL, NULL)
ON CONFLICT (email_address) DO NOTHING;
""" + sql
        self.assertEqual(flags(self.fx.run(created, checks=('identities',))), [])

    @unittest.skipUnless((REAL / NORMAL_OTHER / 'Services_Data/trello/data.json').is_file(),
                         'base Trello export not present')
    def test_real_base_finds_the_victor_and_owen_duplicates(self):
        for sql, person in ((TASK43, 'Victor Barnes'), (TASK1.replace(
                "INSERT INTO trello.trello_actions", """INSERT INTO trello.trello_members
  (id, username, "fullName", initials, "avatarUrl", bio, url, "memberType", confirmed)
VALUES ('PERSON_6172_TRELLO_USER_ID', 'owen.baker', 'Owen Baker', 'OB', NULL, 'Game Engineer (Unity)',
   'https://PERSON_6092_TRELLO_USERNAME.com/u/owen.baker', 'normal', true)
ON CONFLICT (id) DO NOTHING;
INSERT INTO trello.trello_actions""", 1), 'Owen Baker')):
            dup = flags(lint.lint(sql, checks=('identities',), universe='normal'), 'duplicate_account')
            self.assertEqual(len(dup), 1, person)
            self.assertIn(person, dup[0]['message'])


# #50 6aa8272b1b7a2df0fc0fea8d
TASK50 = """INSERT INTO linear.linear_issues
 (id,team_id,assignee_id,creator_id,state_id,identifier,number,title,description,priority,estimate,
  started_at,completed_at,labels_json,links_json,relations_json,state_history_json,is_archived,created_at,updated_at)
SELECT id,'team_ZOM',NULL,'usr_eac7fcafa75e4935','Done',id,num,title,descr,3,NULL,
 NULL,'2026-02-09T19:00:00Z','[]','[]','[]','[]',false,'2026-02-09T19:00:00Z','2026-02-09T19:10:00Z'
FROM (VALUES
('ZOM-673',673,'Win & Collect 2-day distinct players','Note for the 9 Feb 2026 standard roll-up. The 2-day distinct-player totals are in the comments on this ticket. This description does not state them.'),
('ZOM-674',674,'Win & Collect 3-day distinct players','Note for the 9 Feb 2026 standard roll-up. The 3-day distinct-player totals are in the comments on this ticket. This description does not state them.')
) AS v(id,num,title,descr)
WHERE NOT EXISTS (SELECT 1 FROM linear.linear_issues z WHERE z.id=v.id);
"""
# #12 6ac674e16329279865bbecc6 (clean control): persona Slack text with lowercase "done means".
CONTROL12 = """INSERT INTO slack.slack_messages (id, ts, channel_id, user_id, text) VALUES
('a35eef4f0ed4b4d1f5e705a3f9b76826', '1771002326.447130', 'D05S1S2AB5M', 'EMPLOYEE_0025_SLACK_ID',
 'if more than one PR went in for it list all of them with the day each one merged. go by the ticket, done means fixed, anything thats not done counts as still open.');
"""


class GraderLanguageTests(LintTestCase):
    def test_task50_text_addressed_to_the_grader_is_flagged(self):
        result = self.fx.run(TASK50, checks=('grader_language',))
        hits = flags(result, 'grader_language')
        self.assertEqual(len(hits), 1)  # same sentence on both tickets: one flag, the second listed under 'also'
        self.assertEqual(hits[0]['severity'], 'CHECK')
        self.assertIn('This description does not state', hits[0]['message'])
        self.assertEqual(hits[0]['record'], 'ZOM-673')
        self.assertEqual(hits[0]['also'], {'count': 1, 'records': ['ZOM-674']})

    def test_control_persona_text_is_not_flagged(self):
        self.assertEqual(flags(self.fx.run(CONTROL12, checks=('grader_language',))), [])

    def test_state_definitions_and_solver_instructions_are_flagged(self):
        sql = """INSERT INTO linear.linear_issues (id, identifier, title, description) VALUES
          ('i1', 'ART-9922', 'Handoff check', 'Update the issue state:' || chr(10) ||
           '   - Done = the applicable current portrait export exists and matches the approved handoff take.'),
          ('i2', 'ART-9923', 'Handoff check', 'Follow that record''s cohort, decision rule, outputs, and handoff instead.');"""
        hits = {f['record']: f['message'] for f in flags(self.fx.run(sql, checks=('grader_language',)))}
        self.assertIn('state_rules', hits['i1'])
        self.assertIn('solver_address', hits['i2'])


# #3 6aad7d1ec6922756b9ad3951
TASK3 = """-- FRICTION PASS 3: targets the two weight-5 criteria and tool-call volume.
-- Additive only. Confluence still governs, so ground truth is unchanged.

-- A. Ten more tickets. Pure surface area for the tool-call gate.
INSERT INTO linear.linear_issues
  (id, title, number, team_id, priority, state_id, created_at, identifier)
VALUES
  ('ENG-2456', 'Combo chain camera shake intensity', 2456, 'team_ENG', 3,
   'state_5629b9d6559f5f8c', '2026-02-09T00:00:00Z', 'ENG-2456');
-- Migrate the exact earlier single-card Task12 injection, if present.
"""


class PaddingCommentTests(LintTestCase):
    def test_task3_gate_comments_are_flagged_and_plain_comments_are_not(self):
        result = self.fx.run(TASK3, checks=('padding_comment',))
        lines = {f['line']: f for f in flags(result, 'padding_comment')}
        self.assertEqual(sorted(lines), [1, 2, 4])
        self.assertIn('surface area', lines[4]['message'])
        self.assertIn('tool-call', lines[4]['message'])
        self.assertTrue(all(f['severity'] == 'CHECK' for f in lines.values()))

    def test_comments_inside_do_blocks_are_scanned(self):
        sql = "DO $$\nBEGIN\n  -- raises the call count for the baseline\n  PERFORM 1;\nEND\n$$;"
        self.assertEqual([f['line'] for f in flags(self.fx.run(sql, checks=('padding_comment',)))], [3])


class GeneratedColumnTests(LintTestCase):
    """2026-10-20: the platform rejected UPDATE ... SET text_fts = to_tsvector(...) ("can only be updated to
    DEFAULT"), which rolled back the inserts, and three Opus runs saw only base data."""
    INSERT = """INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES
  ('7c1e4a92d05b4f38a6e9b2c4d81f3a57', '1759290431.274819', 'C07C2866011', 'message', 'EMPLOYEE_0025_SLACK_ID',
   'before we talk to bankers', '2025-09-30 20:47:11.274819-07');
"""

    def test_update_of_text_fts_fails(self):
        sql = self.INSERT + """UPDATE slack.slack_messages SET text_fts = to_tsvector('english', text)
WHERE id = '7c1e4a92d05b4f38a6e9b2c4d81f3a57';"""
        found = flags(self.fx.run(sql, checks=('generated_column',)), 'generated_column', 'FAIL')
        self.assertEqual([(f['table'], f['op'], f['column'], f['line']) for f in found],
                         [('slack.slack_messages', 'update', 'text_fts', 4)])
        self.assertIn('can only be updated to DEFAULT', found[0]['message'])

    def test_insert_naming_a_generated_column_fails_even_with_null(self):
        sql = """INSERT INTO slack.slack_messages (id, ts, channel_id, text, text_fts) VALUES ('m1', '1.0', 'C1', 'hi', NULL);
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, body_text_fts) VALUES ('g1', 't1', 'a@b.co', to_tsvector('x'));"""
        found = flags(self.fx.run(sql, checks=('generated_column',)), 'generated_column', 'FAIL')
        self.assertEqual({(f['table'], f['column']) for f in found},
                         {('slack.slack_messages', 'text_fts'), ('gmail.gmail_messages', 'body_text_fts')})

    def test_leaving_it_out_or_default_passes(self):
        sql = self.INSERT + "UPDATE slack.slack_messages SET text_fts = DEFAULT WHERE id = 'x';"
        self.assertEqual(flags(self.fx.run(sql, checks=('generated_column',)), 'generated_column'), [])

    def test_schema_marks_exactly_the_two_search_columns(self):
        tables = lint.schema_tables(REAL)
        marked = {(k[len('#gen:'):], c) for k, v in tables.items() if k.startswith('#gen:') for c in v}
        self.assertEqual(marked, {('slack.slack_messages', 'text_fts'), ('gmail.gmail_messages', 'body_text_fts')})


class LinearTextDateTests(LintTestCase):
    """2026-10-22: Linear stores dates as text. SQL that wrote '2025-09-30 14:12:09+00' ran on the platform, then
    every agent run failed at load-universe ("cannot parse timestamp"). Base data is YYYY-MM-DDTHH:MM:SSZ / YYYY-MM-DD."""
    COLS = ("id, team_id, identifier, number, title, priority, labels_json, links_json, relations_json, is_archived, "
            "state_history_json, created_at, updated_at, due_date")

    def issue(self, created, due="'2025-10-03'", updated="'2025-09-30T14:12:09Z'"):
        return ("INSERT INTO linear.linear_issues (%s) VALUES ('ZOM-9001', 'team_ZOM', 'ZOM-9001', 9001, 't', 2, "
                "'[]', '[]', '[]', false, '[]', %s, %s, %s);" % (self.COLS, created, updated, due))

    def found(self, sql):
        return [(f['column'], f['value']) for f in
                flags(self.fx.run(sql, checks=('text_time_format',)), 'text_time_format', 'FAIL')]

    def test_base_format_passes(self):
        self.assertEqual(self.found(self.issue("'2025-09-30T14:12:09Z'")), [])
        self.assertEqual(self.found(self.issue("'2025-09-30T14:12:09Z'", due='NULL')), [])

    def test_postgres_style_and_offsets_fail(self):
        for bad in ('2025-09-30 14:12:09+00', '2025-09-30T14:12:09+00:00', '2025-09-30T14:12:09.000Z',
                    '2025-09-30 14:12:09'):
            self.assertEqual(self.found(self.issue("'%s'" % bad)), [('created_at', bad)], bad)

    def test_casts_and_wall_clock_fail(self):
        self.assertEqual([c for c, _ in self.found(self.issue("'2025-09-30T14:12:09Z'::timestamptz"))], ['created_at'])
        self.assertEqual([c for c, _ in self.found(self.issue("now()"))], ['created_at'])

    def test_date_column_takes_a_plain_date(self):
        self.assertEqual([c for c, _ in self.found(self.issue("'2025-09-30T14:12:09Z'", due="'2025-10-03T00:00:00Z'"))],
                         ['due_date'])

    def test_update_is_checked_and_other_services_are_not(self):
        sql = ("UPDATE linear.linear_comments SET updated_at = '2025-09-30 14:12:09+00' WHERE id = 'c1';\n"
               "UPDATE slack.slack_messages SET created_at = '2025-09-30 14:12:09+00' WHERE id = 'm1';")
        self.assertEqual(self.found(sql), [('updated_at', '2025-09-30 14:12:09+00')])


class MissingRequiredTests(LintTestCase):
    """2026-10-15..21: four platform errors "null value in column state_history_json of relation linear_issues
    violates not-null constraint"; the column was missing from the schema dump."""

    def found(self, sql):
        return [(f['table'], f['column']) for f in
                flags(self.fx.run(sql, checks=('missing_required',)), 'missing_required', 'FAIL')]

    def test_issue_without_state_history_fails(self):
        sql = LinearTextDateTests.issue(LinearTextDateTests(), "'2025-09-30T14:12:09Z'")
        self.assertEqual(self.found(sql), [])
        self.assertEqual(self.found(sql.replace('state_history_json, ', '').replace("false, '[]', ", 'false, ')),
                         [('linear.linear_issues', 'state_history_json')])

    def test_explicit_null_in_a_required_column_fails(self):
        sql = LinearTextDateTests.issue(LinearTextDateTests(), "'2025-09-30T14:12:09Z'").replace("false, '[]'", 'false, NULL')
        self.assertEqual(self.found(sql), [('linear.linear_issues', 'state_history_json')])

    def test_schema_requires_state_history(self):
        self.assertIn('state_history_json', lint.schema_tables(REAL)['#req:linear.linear_issues'])


class ParserTests(LintTestCase):
    def rows(self, sql):
        toks, _ = lint.tokenize(sql)
        parser = lint.Parser(lint.schema_tables(self.fx.root))
        for stmt in lint.statements(toks):
            parser.statement(stmt)
        return parser.rows

    def test_string_escapes(self):
        rows = self.rows("""INSERT INTO slack.slack_messages (id, text, subtype) VALUES
          ('a', 'nate''s streak', E'line1\\nline2 it\\'s'), ('b', $q$keeps 'quotes'; and semicolons$q$, NULL);""")
        self.assertEqual(rows[0].cols['text'].value, "nate's streak")
        self.assertEqual(rows[0].cols['subtype'].value, "line1\nline2 it's")
        self.assertEqual(rows[1].cols['text'].value, "keeps 'quotes'; and semicolons")
        self.assertEqual(rows[1].cols['subtype'].kind, 'null')

    def test_values_cte_and_update_from_values_bind_rows(self):
        rows = self.rows("""
WITH v (id, ts, created_at) AS (VALUES ('m1', '1770900000.000100', '2026-02-12T12:40:00Z'))
INSERT INTO slack.slack_messages (id, ts, channel_id, created_at)
SELECT v.id, v.ts, 'C1', v.created_at::timestamptz FROM v;
UPDATE gdrive.drive_files AS f SET modified_time = d.mt
FROM (VALUES ('f1', '2026-02-20T10:00:00Z')) AS d(id, mt) WHERE f.id = d.id;""")
        self.assertEqual(rows[0].cols['created_at'].value, '2026-02-12T12:40:00Z')
        self.assertEqual(rows[0].cols['ts'].value, '1770900000.000100')
        self.assertEqual((rows[1].op, rows[1].key, rows[1].cols['modified_time'].value),
                         ('update', 'f1', '2026-02-20T10:00:00Z'))

    def test_spreadsheet_quoted_paste_is_unwrapped(self):
        path = Path(self.fx.temp.name) / 'pasted.sql'
        path.write_text('"INSERT INTO gdrive.drive_files (id, name, mime_type, owner_email, shared_with_emails_json) '
                        'VALUES (\'f1\', \'Plan\', \'application/vnd.google-apps.folder\', \'a@b.co\', '
                        '\'[""marcus.bennett@harmonygames.co""]\');"')
        raw, text, unwrapped = lint.read_sql(path)
        self.assertTrue(unwrapped)
        row = self.rows(text)[0]
        self.assertEqual(json.loads(row.cols['shared_with_emails_json'].value), ['marcus.bennett@harmonygames.co'])

    def test_cli_prints_json_and_rejects_unknown_checks(self):
        path = Path(self.fx.temp.name) / 'task32.sql'
        path.write_text(TASK32)
        out = io.StringIO()
        with contextlib.redirect_stdout(out), patch.object(lint, 'ROOT', self.fx.root):
            code = lint.main(['--sql', str(path), '--checks', 'id_contract', '--summary', '--no-base'])
        self.assertEqual(code, 0)
        summary = json.loads(out.getvalue())
        self.assertEqual(summary['counts']['by_check'], {'id_contract': 1})
        self.assertNotIn('flags', summary)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(lint.main(['--sql', str(path), '--checks', 'nope']), 2)


if __name__ == '__main__':
    unittest.main()
