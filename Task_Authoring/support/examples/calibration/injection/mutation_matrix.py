#!/usr/bin/env python3
"""Mutation matrix for tools/sql_lint.py + tools/base_check.py (validity side of /create-injection).

Builds one valid injection over real base anchors (clean.sql), then applies one defect per
mutation and records whether each tool version flags it at FAIL level (lint error or base_check
Check A/C finding that the clean SQL does not produce). "warn" = only a new warning.

  python3 Task_Authoring/support/examples/calibration/injection/mutation_matrix.py [--version after|before|both]

`before` runs the snapshot in before_tools/ (the tools as they were before this calibration).
Reads the base exports read-only through the tools; never executes SQL; writes only beside itself.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]          # the bundle root
TOOLS = {"after": ROOT / "tools", "before": HERE / "before_tools"}
OUT = HERE / "mutations"

CH, OLIVER_U, BRIAN_U, OUTSIDER_U = "C09R0KXFX71", "EMPLOYEE_0003_SLACK_ID", "EMPLOYEE_0026_SLACK_ID", "EMPLOYEE_0004_SLACK_ID"
OL, BR = "oliver.brooks@harmonygames.co", "brian.foster@harmonygames.co"


def ts(iso):  # '2026-01-12T15:00:00Z' -> slack ts
    return f"{dt.datetime.fromisoformat(iso.replace('Z', '+00:00')).timestamp():.0f}.000100"


def sid(ch, t):
    return hashlib.sha256(f"{ch}|{t}".encode()).hexdigest()[:32]


def trello_id(iso, tail):
    return f"{int(dt.datetime.fromisoformat(iso.replace('Z', '+00:00')).timestamp()):08x}{tail}"


P_TS, R_TS = ts("2026-01-12T15:00:00Z"), ts("2026-01-12T15:20:00Z")
CARD = trello_id("2026-01-12T16:00:00Z", "a1b2c3d4e5f6a7b8")
CHECKL = trello_id("2026-01-12T16:01:00Z", "a1b2c3d4e5f6a7b9")
ITEM1, ITEM2 = trello_id("2026-01-12T16:02:00Z", "a1b2c3d4e5f6a7c0"), trello_id("2026-01-12T16:03:00Z", "a1b2c3d4e5f6a7c1")
ACT = trello_id("2026-01-13T10:00:00Z", "a1b2c3d4e5f6a7c2")
UID = "0f1e2d3c4b5a69788796a5b4c3d2e1f0@hg4"
FILE = "f_0a1b2c3d4e5f60718293a4"
BADGES = ('{"attachments":0,"attachmentsByType":{"trello":{"board":0,"card":0}},"checkItems":2,"checkItemsChecked":1,'
          '"checkItemsEarliestDue":null,"comments":1,"description":true,"due":null,"dueComplete":false,"externalSource":null,'
          '"fogbugz":"","lastUpdatedByAi":false,"location":false,"maliciousAttachments":0,"start":null,"votes":0}')

SLACK_COLS = ("id, ts, channel_id, type, user_id, text, thread_parent_id, thread_ts_legacy, reply_count, reply_users_count, "
              "latest_reply, is_activity_message, subtype, reactions_json, files_json, attachments_json, created_at, edited_ts, "
              "edited_user, bot_id, client_msg_id, permalink, metadata_json")
GMAIL_COLS = ("id, thread_id, user_email, label_ids_json, snippet, internal_date, date, subject, from_email, from_name, "
              "to_json, cc_json, bcc_json, body_text, in_reply_to, \"references\"")
GCAL_COLS = ("event_id, calendar_id, summary, start_ts, end_ts, start_json, end_json, organizer_email, creator_email, "
             "attendees_json, status, visibility, transparency, rrule_json, sequence, created, updated, ical_uid, extras_json")


def att(owner):
    return json.dumps([{"email": OL, "organizer": False, "responseStatus": "accepted", **({"self": True} if owner == OL else {})},
                       {"email": BR, "organizer": True, "responseStatus": "accepted", **({"self": True} if owner == BR else {})}])


def gcal_row(cal, eid):
    return (f"('{eid}', '{cal}', 'Handoff sync', '2026-01-14T17:00:00Z', '2026-01-14T17:30:00Z', "
            "'{\"dateTime\":\"2026-01-14T17:00:00Z\"}', '{\"dateTime\":\"2026-01-14T17:30:00Z\"}', "
            f"'{BR}', '{BR}', '{att(cal)}', 'confirmed', 'private', 'opaque', '[]', 0, "
            f"'2026-01-12T16:05:00Z', '2026-01-12T16:05:00Z', '{UID}', '{{}}')")


CLEAN = f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages ({SLACK_COLS}) VALUES
 ('{sid(CH, P_TS)}', '{P_TS}', '{CH}', 'message', '{BRIAN_U}', 'can someone own the handoff list? <@{OLIVER_U}> see ENG-2022', NULL, NULL, 1, 1, '{R_TS}', false, NULL, '[]', '[]', '[]', '2026-01-12T15:00:00.0001Z', NULL, NULL, NULL, NULL, NULL, '{{}}'),
 ('{sid(CH, R_TS)}', '{R_TS}', '{CH}', 'message', '{OLIVER_U}', 'on it', '{sid(CH, P_TS)}', '{P_TS}', 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2026-01-12T15:20:00.0001Z', NULL, NULL, NULL, NULL, NULL, '{{}}');
INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('{OL}/1890000000000000001', '{OL}', 'Handoff list', NULL);
INSERT INTO gmail.gmail_messages ({GMAIL_COLS}) VALUES
 ('{OL}/<handoff-1@harmonygames.co>', '{OL}/1890000000000000001', '{OL}', '["INBOX"]', 'can you own it', 1768233600000, '2026-01-12T16:00:00Z', 'Handoff list', '{BR}', 'Brian Foster', '["{OL}"]', '[]', '[]', 'can you own it', NULL, NULL),
 ('{OL}/<handoff-2@harmonygames.co>', '{OL}/1890000000000000001', '{OL}', '["SENT"]', 'yes', 1768237200000, '2026-01-12T17:00:00Z', 'Re: Handoff list', '{OL}', 'Oliver Brooks', '["{BR}"]', '[]', '[]', 'yes', '<handoff-1@harmonygames.co>', '<handoff-1@harmonygames.co>');
INSERT INTO gcal.gcal_events ({GCAL_COLS}) VALUES
 {gcal_row(OL, 'evt_0a1b2c3d4e5f60718293a4')},
 {gcal_row(BR, 'evt_1a1b2c3d4e5f60718293a4')};
INSERT INTO linear.linear_issues (id, team_id, assignee_id, creator_id, state_id, identifier, number, title, description, priority, started_at, completed_at, canceled_at, labels_json, links_json, relations_json, state_history_json, is_archived, created_at, updated_at) VALUES
 ('ENG-2990', 'team_ENG', 'usr_bdf01b53c6a92c5e', 'usr_fc22d5941b2aeb5c', 'In Progress', 'ENG-2990', 2990, 'Handoff list', 'follow-up of ENG-2022', 2, '2026-01-12T18:00:00Z', NULL, NULL, '[]', '[]', '[]', '[]', false, '2026-01-12T17:30:00Z', '2026-01-13T09:00:00Z');
INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, updated_at, sequence) VALUES
 ('cmt_0a1b2c3d4e5f60718293', 'ENG-2990', 'usr_bdf01b53c6a92c5e', NULL, 'started', false, '2026-01-13T09:00:00Z', '2026-01-13T09:00:00Z', 1);
INSERT INTO github.github_pr_comments (id, pr_id, author_login, body, created_at, updated_at) VALUES
 ('harmonygames-Games/Combo-Fighters#1#c_900', 'harmonygames-Games/Combo-Fighters#1', 'EMPLOYEE_0003_GITHUB_USERNAME', 'ptal', '2026-01-20T10:00:00Z', '2026-01-20T10:00:00Z');
INSERT INTO github.github_timeline_events (id, pr_id, event, actor_login, created_at, data_json) VALUES
 ('harmonygames-Games/Combo-Fighters#1#ev_900', 'harmonygames-Games/Combo-Fighters#1', 'commented', 'EMPLOYEE_0003_GITHUB_USERNAME', '2026-01-20T10:00:00Z', '{{}}');
INSERT INTO gdrive.drive_files (id, name, mime_type, parents_json, owner_email, shared_with_emails_json, visibility, owners_json, modified_time, created_time, trashed, starred) VALUES
 ('{FILE}', 'Handoff tracker', 'application/vnd.google-apps.spreadsheet', '[]', '{OL}', '["{BR}"]', 'private', '["{OL}"]', '2026-01-12T18:00:00Z', '2026-01-12T18:00:00Z', false, false);
INSERT INTO gsheets.sheets_spreadsheets (spreadsheet_id, title, owner_email, shared_with_emails_json, visibility, drive_file_id, created_time, modified_time) VALUES
 ('{FILE}', 'Handoff tracker', '{OL}', '["{BR}"]', 'private', '{FILE}', '2026-01-12T18:00:00Z', '2026-01-12T18:00:00Z');
INSERT INTO trello.trello_cards (id, name, "idBoard", "idList", "desc", pos, closed, "dueComplete", "idMembers_json", "idLabels_json", "idShort", "dateLastActivity", badges_json) VALUES
 ('{CARD}', 'Handoff checklist', '65eb4ec525346c8070ca638f', '6709a4d20cd29d7439b98ddc', 'see ENG-2990', 900000.0, false, false, '["12c4a9dcd2d37a25a8d3b557"]', '[]', 990, '2026-01-13T10:00:00Z', '{BADGES}');
INSERT INTO trello.trello_checklists (id, name, "idCard", "idBoard", pos) VALUES ('{CHECKL}', 'Items', '{CARD}', '65eb4ec525346c8070ca638f', 16384.0);
INSERT INTO trello.trello_check_items (id, name, state, "idChecklist", pos, "idMember") VALUES
 ('{ITEM1}', 'list owners', 'complete', '{CHECKL}', 1000, '12c4a9dcd2d37a25a8d3b557'),
 ('{ITEM2}', 'confirm vendors', 'incomplete', '{CHECKL}', 2000, NULL);
INSERT INTO trello.trello_actions (id, type, date, "idMemberCreator", "idBoard", "idCard", data_json) VALUES
 ('{ACT}', 'commentCard', '2026-01-13T10:00:00Z', '12c4a9dcd2d37a25a8d3b557', '65eb4ec525346c8070ca638f', '{CARD}', '{{"text":"owners listed"}}');
INSERT INTO confluence.confluence_page_versions (id, page_id, number, title, body, author_id, message, created_at) VALUES
 ('ver_0a1b2c3d4e5f60718293a4b5c6d7e8f9', 'page_eng_home', 3, 'Engineering Home', '<p>See <ac:link><ri:page ri:content-title="Architecture Overview"/></ac:link>.</p>', 'user_EMPLOYEE_0003', 'handoff note', '2026-01-13T11:00:00Z');
UPDATE confluence.confluence_pages SET version = 3, body = '<p>See <ac:link><ri:page ri:content-title="Architecture Overview"/></ac:link>.</p>', updated_at = '2026-01-13T11:00:00Z' WHERE id = 'page_eng_home';
"""

# (defect class, name, old, new) — each old string must occur in CLEAN
MUTATIONS = [
    ("broken reference", "Linear comment on a nonexistent issue", "'cmt_0a1b2c3d4e5f60718293', 'ENG-2990'", "'cmt_0a1b2c3d4e5f60718293', 'ENG-999999'"),
    ("broken reference", "Slack <@mention> of a nonexistent user", f"<@{OLIVER_U}>", "<@UNOBODY000>"),
    ("broken reference", "Text cites a nonexistent Linear ticket", "follow-up of ENG-2022", "follow-up of ENG-2989"),
    ("broken reference", "Slack text links a PR missing from GitHub", "'on it'", "'on it https://github.com/harmonygames-Games/Combo-Fighters/pull/99999'"),
    ("broken reference", "Gmail in_reply_to resolves to nothing", "'<handoff-1@harmonygames.co>', '<handoff-1@", "'<nope@harmonygames.co>', '<handoff-1@"),
    ("broken reference", "Confluence link to a missing page title", 'ri:content-title="Architecture Overview"/></ac:link>.</p>\', \'user_', 'ri:content-title="Arch Overview v9"/></ac:link>.</p>\', \'user_'),
    ("broken reference", "Trello checklist on a missing card", f"'Items', '{CARD}'", "'Items', '0000000000000000000000ff'"),
    ("ID-contract break", "Slack id is not sha256(channel|ts)", sid(CH, R_TS), "0123456789abcdef0123456789abcdef"),
    ("ID-contract break", "Gmail message id not <mailbox>/<Message-ID>", f"('{OL}/<handoff-2@harmonygames.co>'", f"('{OL}/handoff-2'"),
    ("ID-contract break", "Drive id not f_ + 22 hex", f"('{FILE}', 'Handoff tracker', 'application", f"('{FILE}9', 'Handoff tracker', 'application"),
    ("ID-contract break", "GitHub comment id outside <pr>#c_<n>", "Combo-Fighters#1#c_900'", "Combo-Fighters#1#c_extra'"),
    ("ID-contract break", "GCal ical_uid not 32hex@hg4", UID, UID[1:]),
    ("ID-contract break", "Trello id not minted from its time", f"('{ACT}'", "('9a1b2c3d4e5f6a7b8c9d0e1f'"),
    ("ID-contract break", "Linear id differs from identifier", "('ENG-2990', 'team_ENG'", "('iss_handoff', 'team_ENG'"),
    ("chronology inversion", "Slack reply before its parent", f"'{R_TS}', '{CH}', 'message', '{OLIVER_U}'", f"'{ts('2026-01-12T14:00:00Z')}', '{CH}', 'message', '{OLIVER_U}'"),
    ("chronology inversion", "Gmail reply dated before the message it answers", "1768237200000, '2026-01-12T17:00:00Z'", "1768230000000, '2026-01-12T15:00:00Z'"),
    ("chronology inversion", "GCal event ends before it starts", "'2026-01-14T17:00:00Z', '2026-01-14T17:30:00Z', '{\"dateTime\":\"2026-01-14T17:00:00Z\"}', '{\"dateTime\":\"2026-01-14T17:30:00Z\"}', 'brian.foster@harmonygames.co', 'brian.foster@harmonygames.co', '[{\"email\": \"oliver.brooks@harmonygames.co\", \"organizer\": false, \"responseStatus\": \"accepted\", \"self\"",
     "'2026-01-14T17:00:00Z', '2026-01-14T16:30:00Z', '{\"dateTime\":\"2026-01-14T17:00:00Z\"}', '{\"dateTime\":\"2026-01-14T16:30:00Z\"}', 'brian.foster@harmonygames.co', 'brian.foster@harmonygames.co', '[{\"email\": \"oliver.brooks@harmonygames.co\", \"organizer\": false, \"responseStatus\": \"accepted\", \"self\""),
    ("chronology inversion", "Linear comment before its issue exists", "'started', false, '2026-01-13T09:00:00Z'", "'started', false, '2026-01-10T09:00:00Z'"),
    ("chronology inversion", "Slack message before the channel existed", None,
     lambda q: q.replace(sid(CH, P_TS), sid(CH, ts("2025-01-12T15:00:00Z"))).replace(P_TS, ts("2025-01-12T15:00:00Z"))
                .replace("'2026-01-12T15:00:00.0001Z'", "'2025-01-12T15:00:00.0001Z'")),
    ("status/activity mismatch", "Linear Done without completed_at", "'In Progress', 'ENG-2990'", "'Done', 'ENG-2990'"),
    ("status/activity mismatch", "Linear comment newer than issue updated_at", "false, '2026-01-12T17:30:00Z', '2026-01-13T09:00:00Z'", "false, '2026-01-12T17:30:00Z', '2026-01-12T19:00:00Z'"),
    ("status/activity mismatch", "PR comment newer than PR updated_at", "'ptal', '2026-01-20T10:00:00Z'", "'ptal', '2026-02-01T10:00:00Z'"),
    ("status/activity mismatch", "Trello badges disagree with checklist/comments", '"checkItems":2,"checkItemsChecked":1', '"checkItems":0,"checkItemsChecked":0'),
    ("status/activity mismatch", "Slack parent reply_count disagrees with replies", "ENG-2022', NULL, NULL, 1, 1", "ENG-2022', NULL, NULL, 3, 1"),
    ("status/activity mismatch", "Confluence version gap / page.version stale", "'page_eng_home', 3, 'Engineering Home'", "'page_eng_home', 4, 'Engineering Home'"),
    ("status/activity mismatch", "PR comment without its 'commented' timeline event", "'commented', 'EMPLOYEE_0003_GITHUB_USERNAME'", "'labeled', 'EMPLOYEE_0003_GITHUB_USERNAME'"),
    ("malformed JSON in a JSON column", "attendees_json not valid JSON", '"responseStatus": "accepted", "self": true}', '"responseStatus": "accepted", "self": true'),
    ("malformed JSON in a JSON column", "badges_json not valid JSON", '"votes":0}', '"votes":0'),
    ("non-member poster", "Slack poster not in channel members", f"'message', '{OLIVER_U}', 'on it'", f"'message', '{OUTSIDER_U}', 'on it'"),
    ("mailbox mismatch", "Copy in a mailbox that is neither sender nor recipient", "'Brian Foster', '[\"oliver.brooks@harmonygames.co\"]'", "'Brian Foster', '[\"arthur.blake@harmonygames.co\"]'"),
    ("mailbox mismatch", "Own sent copy not labelled SENT", "'[\"SENT\"]'", "'[\"INBOX\"]'"),
    ("attendee-copy gap", "Organizer's calendar has no copy", f",\n {gcal_row(BR, 'evt_1a1b2c3d4e5f60718293a4')}", ""),
    ("attendee-copy gap", "Drive share to an unknown person", f"'{OL}', '[\"{BR}\"]', 'private', '[\"{OL}\"]'", f"'{OL}', '[\"nobody.here@harmonygames.co\"]', 'private', '[\"{OL}\"]'"),
    ("attendee-copy gap", "Sheets row sharing differs from its Drive row", f"'Handoff tracker', '{OL}', '[\"{BR}\"]', 'private', '{FILE}'", f"'Handoff tracker', '{OL}', '[]', 'private', '{FILE}'"),
    ("duplicate keys", "Same Slack row inserted twice", f"'{{}}');\nINSERT INTO gmail.gmail_threads", f"'{{}}'),\n ('{sid(CH, R_TS)}', '{R_TS}', '{CH}', 'message', '{OLIVER_U}', 'on it', '{sid(CH, P_TS)}', '{P_TS}', 0, 0, NULL, false, NULL, '[]', '[]', '[]', '2026-01-12T15:20:00.0001Z', NULL, NULL, NULL, NULL, NULL, '{{}}');\nINSERT INTO gmail.gmail_threads"),
    ("duplicate keys", "New Linear issue collides with the base", "('ENG-2990', 'team_ENG', 'usr_bdf01b53c6a92c5e', 'usr_fc22d5941b2aeb5c', 'In Progress', 'ENG-2990', 2990", "('ENG-2022', 'team_ENG', 'usr_bdf01b53c6a92c5e', 'usr_fc22d5941b2aeb5c', 'In Progress', 'ENG-2022', 2022"),
    ("duplicate keys", "Trello idShort already used on the board", "'[]', 990,", "'[]', 80,"),
    ("generated-column write", "INSERT writes slack text_fts", None,
     lambda q: q.replace("permalink, metadata_json)", "permalink, metadata_json, text_fts)")
                .replace("NULL, NULL, NULL, NULL, NULL, '{}')", "NULL, NULL, NULL, NULL, NULL, '{}', 'x')")),
    ("missing NOT NULL", "INSERT omits Linear is_archived", None,
     lambda q: q.replace("state_history_json, is_archived, created_at", "state_history_json, created_at")
                .replace("'[]', '[]', '[]', '[]', false, '2026-01-12T17:30:00Z'", "'[]', '[]', '[]', '[]', '2026-01-12T17:30:00Z'")),
]


# the rule each mutation targets (substring of the expected finding)
EXPECT = {
    1: "issue ENG-999999 does not exist", 2: "not a Slack user", 3: "dangling reference", 4: "which does not exist in GitHub", 5: "does not resolve to a message", 6: "does not resolve to any page title", 7: "does not exist", 8: "Slack id contract", 9: "RFC Message-ID", 10: "breaks the service ID format", 11: "GitHub id scheme", 12: "32-hex@hg4", 13: "Trello ids start with", 14: "differs from identifier", 15: "is not after its parent", 16: "dated before the message it answers", 17: "ends before it starts", 18: "predates its issue", 19: "predates channel", 20: "without completed_at", 21: "is newer than issue", 22: "is newer than PR", 23: "disagree with its SQL comments/check items", 24: "thread counters", 25: "do not continue the base history", 26: "'commented' timeline event", 27: "malformed JSON", 28: "malformed JSON", 29: "not a channel member", 30: "neither the sender", 31: "not labelled SENT", 32: "has no copy of the event", 33: "not a known HarmonyGames identity", 34: "owner/sharing differ", 35: "inserted twice", 36: "collides with the base", 37: "already used on board", 38: "generated column", 39: "omits NOT NULL",
}


def run(version: str, sql_path: Path) -> dict:
    tools = TOOLS[version]
    code = f"""
import json, sys
sys.path.insert(0, {str(tools)!r})
import sql_lint, base_check
from pathlib import Path
real = Path({str(ROOT / 'tools')!r}).resolve().parent.parent
base_check.OTHER = real / 'HarmonyGames_Other_Services' / 'Services_Data'
base_check.GITHUB = real / 'HarmonyGames_GitHub' / 'Services_Data' / 'github' / 'data.json'
base_check.GMAIL = real / 'HarmonyGames_Gmail' / 'Services_Data' / 'gmail'
base_check.CACHE = real / {ROOT.name!r} / 'support' / 'local_search' / 'cache'
sql = Path({str(sql_path)!r}).read_text()
lint = sql_lint.lint(sql, sql_lint.load_schema(Path({str(ROOT / 'references' / 'universe_schema_live.json')!r})))
try:
    bc = base_check.check(sql)
except Exception as e:
    bc = {{'check_A': [{{'msg': 'CRASH ' + repr(e)}}], 'check_C': [], 'warnings': []}}
print(json.dumps({{'fail': sorted({{'L:' + e['msg'] for e in lint['errors']}} | {{'B:' + f['msg'] for f in bc['check_A'] + bc['check_C']}}),
                  'warn': sorted({{'L:' + w['msg'] for w in lint['warnings']}} | {{'B:' + w['msg'] for w in bc.get('warnings', [])}})}}))
"""
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=str(ROOT.parent))
    if out.returncode:
        raise SystemExit(out.stderr)
    return json.loads(out.stdout.strip().splitlines()[-1])


def main(argv):
    versions = ["before", "after"] if "both" in argv or len(argv) == 0 else [a.split("=")[-1] for a in argv if a.startswith("--version")] or ["after"]
    if "--version" in argv:
        versions = [argv[argv.index("--version") + 1]] if argv[argv.index("--version") + 1] != "both" else ["before", "after"]
    OUT.mkdir(exist_ok=True)
    (OUT / "clean.sql").write_text(CLEAN)
    clean = {v: run(v, OUT / "clean.sql") for v in versions}
    rows = []
    for i, (cls, name, old, new) in enumerate(MUTATIONS, 1):
        p = OUT / f"m{i:02d}.sql"
        if old is None:
            p.write_text(new(CLEAN))
        else:
            assert old in CLEAN, f"mutation {i} anchor missing: {old[:60]}"
            p.write_text(CLEAN.replace(old, new, 1))
        res = {}
        for v in versions:
            r = run(v, p)
            new_fail = [m for m in r["fail"] if m not in clean[v]["fail"]]
            new_warn = [m for m in r["warn"] if m not in clean[v]["warn"]]
            hit = [m for m in new_fail if EXPECT[i] in m]
            res[v] = ("Y" if hit else "Y*" if new_fail else "warn" if new_warn else "N",
                      (hit or new_fail or new_warn or [""])[0][:150])
        rows.append((i, cls, name, res))
    lines = ["# Mutation matrix — sql_lint + base_check", "",
             "Clean fixture: " + "; ".join(f"{v}: {len(clean[v]['fail'])} fail-level findings, {len(clean[v]['warn'])} warnings" for v in versions), ""]
    for v in versions:
        for m in clean[v]["fail"]:
            lines.append(f"- clean/{v} FAIL: {m}")
    lines += ["", "Y = the targeted rule fired at FAIL level · Y* = caught at FAIL level only by another rule · warn = warning only · N = missed", "",
              "| # | Defect class | Mutation | " + " | ".join(f"{v}" for v in versions) + " | First new finding (latest version) |",
              "|---|---|---|" + "---|" * len(versions) + "---|"]
    for i, cls, name, res in rows:
        lines.append(f"| {i} | {cls} | {name} | " + " | ".join(res[v][0] for v in versions) + f" | {res[versions[-1]][1].replace('|', '/')} |")
    for v in versions:
        lines.append(f"\n{v}: targeted rule fired {sum(r[3][v][0] == 'Y' for r in rows)}/{len(rows)}; "
                     f"caught only by a side-effect rule {sum(r[3][v][0] == 'Y*' for r in rows)}; "
                     f"any FAIL-level catch {sum(r[3][v][0] in ('Y', 'Y*') for r in rows)}/{len(rows)}, "
                     f"{sum(r[3][v][0] == 'warn' for r in rows)} warning-only, {sum(r[3][v][0] == 'N' for r in rows)} missed")
    text = "\n".join(lines)
    (HERE / "mutation_matrix.md").write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main(sys.argv[1:])
