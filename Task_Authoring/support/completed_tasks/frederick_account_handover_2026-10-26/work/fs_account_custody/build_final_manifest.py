"""Final manifest = draft + ids the SQL settled + facts + design_delta (injection rev 1)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WF = ROOT / 'task_inputs/Working_Files'
M = json.load(open(HERE / 'minted_ids.json'))
S = json.load(open(HERE / 'sql_ids.json'))

txt = (WF / '01_Hardness_Manifest.draft.json').read_text()
old_decoy = M['S_DECOY90']
REPL = [(M['FOLDER_SWEEP']['id'], S['folder_sweep']), (M['FOLDER_OPS']['id'], S['folder_ops']),
        (old_decoy['id'], S['decoy90']['id']), (old_decoy['ts'], S['decoy90']['ts']), (old_decoy['at'], S['decoy90']['at']),
        ('2025-09-15T19:02:33Z', S['decoy90']['at']), ('Sep 15', 'Sep 24'), ('15 per-platform', '16 per-platform'),
        ('holds 15 exports', 'holds 16 exports'), ('12 accounts remain', '13 accounts remain'),
        ("handover rules are on the ops board", "handover rules are on the Harmony Games board")]
for a, b in REPL:
    txt = txt.replace(a, b)
d = json.loads(txt)

SW = {k[3:]: v['id'] for k, v in M.items() if k.startswith('SW_')}
G = S['gmail_threads']['frederick.stone@harmonygames.co']
GMSG = 'frederick.stone@harmonygames.co/' + S['msgid']
d['facts'] = [
    {"key": "Harmony Games, Inc.", "value": "569-350-5790", "kind": "id",
     "must_appear_in": [SW['gads_569'], GMSG]},
    {"key": "Calm Play one", "value": "449-481-1590", "kind": "id", "aliases": ["Calm Play LLC"],
     "must_appear_in": [GMSG]},
    {"key": "Publisher ID", "value": "pub-3556282811018998", "kind": "id", "home_ids": [SW['admob']],
     "must_appear_in": [SW['admob']]},
    {"key": "Unlinked", "value": "2024-12-20", "kind": "date", "aliases": ["Removed"],
     "must_appear_in": [SW['gads_569'], SW['gads_449'], SW['youtube']]},
]
d['design_delta'] = [
    {"id": "K6", "change": f"sweep folder id {M['FOLDER_SWEEP']['id']} -> {S['folder_sweep']}",
     "reason": "Drive folders are d_ + 22 hex in the base (Ask_Carriers 2.4); same hex kept"},
    {"id": "K7", "change": f"Company Ops folder id {M['FOLDER_OPS']['id']} -> {S['folder_ops']}",
     "reason": "Drive folders are d_ + 22 hex in the base"},
    {"id": "T3", "change": f"90-day remark moved from C07C2866011/{old_decoy['ts']} (Sep 15) to C07C2866011/{S['decoy90']['ts']} (Sep 24)",
     "reason": "on Sep 15 nobody had raised cuts yet; on Sep 24 Leonard had just said 'we have 2 months left before letting everyone go' (C07C2866011/1758739409.488879), so the remark fits there and still predates the cash notes doc"},
    {"id": "H2", "change": "decoy_seeded_ids follows the moved remark", "reason": "same as T3"},
    {"id": "K4", "change": "subject 'Account handover rules - marketing, UA & socials' (no 'Re:')",
     "reason": "the card is not an email; a 'Re:' with no parent message would break Gmail reply integrity"},
    {"id": "C1", "change": "Node Media manager ID on the Google Ads 569/449 Linked managers tabs 812-604-3397 -> 645-364-1205",
     "reason": "/injection rev-1 C-1: base Gmail links both accounts to manager 645-364-1205 (HarmonyGames_Gmail threads/00007026.json, 00007027.json)"},
    {"id": "C2", "change": "Google Ads 449-481-1590 Access tab: Robert (Admin, 2024-01-10), Leonard (Admin, 2024-01-20), Arthur (Admin, 2024-01-20), Frederick (Admin, 2024-09-05); class SINGLE -> COMPANY-HELD, action stays CLOSE (no money moving)",
     "reason": "/injection rev-1 C-2: base Gmail adds Leonard and Arthur as Administrative on 2024-01-20 (threads/00002732.json, 00002735.json) and Fred on 2024-09-05 (00006561.json, 00006608.json); Robert's box has the account since 2024-01-10 (00002504.json); 2025 notices still reach all four and no removal exists"},
    {"id": "C3", "change": "Google Ads 569-350-5790 Access tab: Frederick Added 2024-10-07, Leonard 2024-09-20",
     "reason": "/injection rev-1 C-3: Fred was invited by Leonard 2024-09-22 and added as Administrative 2024-10-07 (leonard@harmonygames.co_1812273271350908422.json)"},
    {"id": "T1", "change": "Leonard's admin claim is now true on all three platforms; the trap is his 'so those are covered': Meta is REVOKE (Node partner) and the Calm Play Google Ads is CLOSE",
     "reason": "follows C2 and rev-2 C-2; f_63b42f52fa11d7df238a4e and f_f7e7c5bf089029cee91175 dropped from the trap's seeded_ids"},
    {"id": "R2-C1", "change": "AdMob export: publisher ID pub-7795231806614420 -> pub-3556282811018998 (title, grid, fact)",
     "reason": "/injection rev-2 C-1: base names Leonard's new AdMob account pub-3556282811018998 (C73E02AA3A22/1745467232.203529; leonard@harmonygames.co_1830467552498804662.json)"},
    {"id": "R2-C2", "change": "Meta export is the Domino Delights ad account 907669287942378: Fred Admin 2024-10-06 (created it), Robert Admin 2024-10-06, Leonard Admin via the business portfolio 2024-01-22, Arthur Admin 2025-04-29; Partners tab unchanged (Node Media partner admin) -> still OUTSIDE ACCESS -> REVOKE",
     "reason": "/injection rev-2 C-2: Fred created the ad account 2024-10-06 (C08MCEP1B9B/1728233888.592579); Robert added (HarmonyGames_Gmail threads/00007738.json); Leonard invited to the portfolio 2024-01-22 (leonard@harmonygames.co_1788818142336108597.json) and invited Fred into it; Fred invited Arthur to manage the ad account 2025-04-29 (C07C2866011/1745941986.729119)"},
    {"id": "R2-C3", "change": "YouTube Fred Owner 2024-11-21, Leonard Manager 2025-04-27; Play Console and App Store Connect rebuilt from the base acceptance / welcome mails; March sheet YouTube row 'Fred' only, AdMob login Fred",
     "reason": "/injection rev-2 C-3 and A-3: channel created for Node 2024-11-21 (C08MCEP1B9B/1732203251.229079); manager invite D05S58U4SAK/1745795372.283269; frederick.stone@ exists from 2024-06-25"},
    {"id": "R2-C4", "change": "Singular users: Leonard 2024-01-01, Robert 2024-01-01, Douglas 2024-02-19, Fred 2024-09-04, Simon Walker 2024-10-22", "reason": "/injection rev-2 C-4 base invites"},
    {"id": "R3-B", "change": "Meta Partners tab drops the Business ID column; Node fact removed; AppLovin adds EMPLOYEE_0032 (2024-10-24), Arthur (2025-05-06), Brian Foster (2025-05-08) as User; adjoe Leonard added 2025-04-28; TikTok second account 'Deactivated 2025-09-29 (deletion pending)'; Singular lists Node Media removed 2024-12-20; March sheet adjoe 'Fred', AppLovin login Fred",
     "reason": "independent pre-review: 2150873365841209 has 0 base hits; D07FYRRD0JJ/1729790608.878139; D04UGG61DUM/1746568639.203489; brian@harmonygames.co_1831584819763467477.json; C07UCC631A6/1745858198.308669; SVC_0009 still receives TikTok mail after the clock; C08MCEP1B9B/1728279841.550309 (Node has Singular access)"},
    {"id": "R3-C1", "change": "App Store Connect Harmony Games, Inc. team drops Vincent Parker and Brian Foster; Meta Leonard date marked '(portfolio)'",
     "reason": "/injection rev-3 C-1: their 2025-07 joins are on the Calm Play LLC Apple team (vincent@harmonygames.co_1837750651533817330.json; brian@harmonygames.co_1837749595759137426.json)"},
    {"id": "P1-CS", "change": "cash notes 'Money still moving' section adds a warehouse note: spend tables have no Meta spend after April and no Unity cost; the finance ledger lumps the ad-network payouts under AppLovin/MAX and runs a month behind (e.g. FIN-000597 2025-08-31 954.80 = July admob+applovin+meta_audience); use receipts / campaign state for spend and the ad revenue numbers by network for revenue. Hub says 'on the Harmony Games board' instead of 'on the ops board'",
     "reason": "/prompt FAIL (Cross-Service Coherence 2, CS-1/CS-2): snowflake.json /tables/34 and /tables/0 have no meta rows May-Sep 2025 and unity_ads spend 0.0; /tables/38 has no 2025-09 marketing_ua entry and FIN-000616 (2025-09-30, AppLovin/MAX, 348.87) is the August admob+applovin+meta_audience total from /tables/35; advisory: no board is named 'ops'"},
    {"id": "R2-A1", "change": "LinkedIn page admins add Robert and Arthur (Super admin 2023-04-18)", "reason": "C04UEQVDVB7/1681871195.627119"},
    {"id": "R2-U", "change": "Unity export is the Harmony Games Inc org 20067043314233 (Arthur, Robert, Leonard Owner; Fred Manager; filtered to Owners and Managers, seat-only users not shown); Invites tab removed; class SINGLE -> COMPANY-HELD, action TRANSFER -> KEEP; totals REVOKE 1 / TRANSFER 4 / KEEP 6 / CLOSE 2",
     "reason": "/injection rev-2 A-2: the September money (Leonard's prepayment receipts to 'Harmony Games Inc', Sep 28 campaign link C07C2866011/1759078905.131549) is in org 20067043314233; Robert invited Fred into the other org (C07C2866011/1728453730.535849), so Fred cannot be its sole owner; Arthur receives the org's Unity Pro renewals (blake@harmonygames.co_1843681663885543164.json)"},
    {"id": "B1", "change": "trello_cards INSERTs no longer set start / idAttachmentCover", "reason": "/injection rev-1 Check B advisory: columns absent from the schema snapshot; both were NULL"},
]
U, X_, META = 'f_1191b7f8c96419e1f4dc88', 'f_99d66f33c54338e70f5ed2', 'f_f7e7c5bf089029cee91175'
T = {t['id']: t for t in d['traps']}
T['T1']['seeded_ids'] = ['d18954e94e8b9caa935704bd676ccffe', META, 'f_63b42f52fa11d7df238a4e', U]
T['T1']['expected_wrong_reading'] = "takes 'admin on meta, google ads and unity already so those are covered' as meaning those accounts are settled (KEEP)"
T['T1']['resolver'] = "his admin is real, but the card decides the action: Meta still has Node Media as partner admin -> REVOKE; the Calm Play Google Ads has no money moving -> CLOSE; only Unity and the Harmony Games, Inc. Google Ads (Arthur's email) are KEEP"
T['T6']['seeded_ids'] = [i for i in T['T6']['seeded_ids'] if i != U]
T['T6']['expected_wrong_reading'] = "counts managers, shared logins or a personal address as company holders (YouTube, TikTok, Instagram look COMPANY-HELD)"
T['T9']['expected_wrong_reading'] = "reads only the People block of the Meta export and classifies Meta COMPANY-HELD -> KEEP"
T['T14']['seeded_ids'] = [i for i in T['T14']['seeded_ids'] if i != U]
T['T14']['resolver'] = "the exports under card rules 2-4: X and Instagram are SINGLE as well; Meta has an outside partner"
for c in d['chains']:
    if c['id'] == 'C1':
        c['hops'][1] = {"service": "gsheets", "record": X_, "finding": "X: Fred is the only Owner, no delegates"}
        c['hops'][2]['finding'] = "fewer than two company holders -> SINGLE; socials never CLOSE (comment) -> TRANSFER"
for b in d.get('budget', d.get('call_budget', [])):
    if b.get('calls') == 18 and 'Unity Invites' in b.get('reason', ''):
        b['calls'] = 17
        b['reason'] = "one export per in-scope account (13) plus the second tab of four exports: Meta Partners, Google Ads 569 and 449 Linked managers, YouTube Removed users (each needed to rule outside access or a holder in or out)"
for t in d['traps']:
    if t['id'] == 'T3':
        for v in t['version_records']:
            if v['service'] == 'slack':
                v['id'] = S['decoy90']['id']
for t in d['traps']:
    for v in t.get('version_records', []):
        if v['service'] == 'gmail' and v.get('id') == 'frederick.stone@harmonygames.co/' + M['G_AMEND']['gmail_id']:
            v['id'] = GMSG
(WF / '01_Hardness_Manifest.json').write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n')
print('ok', len(d['facts']), 'facts')
