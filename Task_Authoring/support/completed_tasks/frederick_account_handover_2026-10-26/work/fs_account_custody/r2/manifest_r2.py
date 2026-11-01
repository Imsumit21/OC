"""Hardening round 2: manifest update (T16/T18 reworked, T21 added, chains, budget, writes, facts)."""
import json, sys
P = sys.argv[1]
m = json.load(open(P))
YT_T = "frederick.stone@harmonygames.co/1834647853990444617"
YT_M = "frederick.stone@harmonygames.co/<CsalywIzVSffkEGTDj2Cow@notifications.google.com>"
TT_T = "frederick.stone@harmonygames.co/1837824433193834721"
TT_M = "frederick.stone@harmonygames.co/<25b931cc-8e32-759f-91e3-4bdecbbb86d6.notice@business.tiktok.com>"
IG_T = "frederick.stone@harmonygames.co/1839715197125206004"
IG_M = "frederick.stone@harmonygames.co/<b1548908-9860-3c7e-0d23-e952f77bb721@facebookmail.com>"
CARD = "68dc406c7b0d03e53b334bab"

traps = {t['id']: t for t in m['traps']}
traps['T16'].update({
    "family": "conclusion_stop",
    "services": ["gsheets", "gmail"],
    "seeded_ids": ["f_fc27672c5bfea8b760b074", YT_T],
    "base_pointers": ["slack:C08MCEP1B9B/1732203251.229079", "slack:D05S58U4SAK/1759096868.688389"],
    "expected_wrong_reading": "stops at the export's Removed users tab (Node Media removed from Studio on 2024-12-20) and classifies YouTube SINGLE -> TRANSFER, on the checklist",
    "resolver": "Google's Brand Account notice to Fred (2025-06-11): [EMAIL_126620], the address the Removed users tab gives for Node Media LLC, is still an Owner of the Harmony Games Brand Account; Studio permissions (the export's stated scope) do not list Brand Account owners -> OUTSIDE ACCESS -> REVOKE",
    "discovery_order": "the export (read for every account) shows the Studio removal before any mail; only a YouTube, Brand Account or Node address search reaches the notice, and every run's YouTube search was dated after Aug 20",
})
traps['T18'].update({
    "family": "cross_reference_gap",
    "services": ["gsheets", "gmail"],
    "seeded_ids": ["f_215ff8da73e4173f78515c", IG_T],
    "base_pointers": [],
    "expected_wrong_reading": "reads the login row only (Fred's personal gmail, 'Login only') and classifies Instagram SINGLE with no company holder -> TRANSFER, on the checklist",
    "resolver": "Meta's notice to Fred (2025-08-06): Leonard Hayes and Frederick Stone have Full control (admin) of @harmonygames in the Domino Delights portfolio on their harmonygames.co logins, no partners -> two company holders -> COMPANY-HELD; no money moving -> card CLOSE -> socials comment -> KEEP (Arthur's 'everything else already has two of us on it' agrees)",
    "discovery_order": "the export's note says 'Login only'; the portfolio holders are only in Gmail, dated before every run's dated Instagram search",
})
t21 = {
    "id": "T21", "family": "cross_reference_gap", "services": ["gsheets", "gmail", "slack"],
    "seeded_ids": ["f_2f0abe2f1f6726fef63f80", TT_T],
    "base_pointers": ["slack:C08MCEP1B9B/1728233888.592579", "slack:C08MCEP1B9B/1728234009.536219"],
    "requirement": "R3",
    "expected_wrong_reading": "reads the TikTok export (scope: account logins) and classifies TikTok SINGLE -> TRANSFER, counts 4 TRANSFER and lists Node Media on Meta and Unity only",
    "resolver": "TikTok for Business reminder to Fred (2025-07-16): Business Center partner Node Media LLC still has Admin on @harmonygames, shared Oct 8, 2024 (Node's Oct 6, 2024 Leadsie request asked for TikTok partner access) -> OUTSIDE ACCESS -> REVOKE; not on the checklist",
    "discovery_order": "the export is read first and lists logins only; a 'Node Media' mail search reaches the reminder, the date-filtered tiktok searches do not",
}
m['traps'] = [traps.get(t['id'], t) for t in m['traps']] + [t21]

for c in m['chains']:
    if c['id'] == 'C4' and c['root_cause'] == 'A3':
        c.update({"root_cause": "A10", "hops": [
            {"service": "gsheets", "record": "f_fc27672c5bfea8b760b074", "finding": "Scope: Studio channel permissions; Removed users: Node Media LLC [EMAIL_126620] removed 2024-12-20 (apparent conclusion)"},
            {"service": "gmail", "record": YT_T, "finding": "Brand Account notice: [EMAIL_126620] still Owner"},
            {"service": "trello", "record": CARD, "finding": "rule 4 -> OUTSIDE ACCESS -> REVOKE; not on the rule-7 checklist"}]})
m['chains'] += [
    {"id": "C7", "root_cause": "A18", "ends_in": "R6", "hops": [
        {"service": "slack", "record": "C08MCEP1B9B/1728234009.536219", "finding": "Node's Leadsie link asks for partner access to Facebook, Google and TikTok (Oct 6, 2024)"},
        {"service": "gmail", "record": TT_T, "finding": "TikTok Business Center: Node Media LLC still Admin on @harmonygames"},
        {"service": "trello", "record": CARD, "finding": "rule 4 -> OUTSIDE ACCESS -> REVOKE; TRANSFER count drops to 1"}]},
    {"id": "C8", "root_cause": "A13", "ends_in": "R8", "hops": [
        {"service": "gsheets", "record": "f_215ff8da73e4173f78515c", "finding": "login is Fred's personal gmail, 'Login only'"},
        {"service": "gmail", "record": IG_T, "finding": "Leonard and Fred have Full control (admin) in the Domino Delights portfolio"},
        {"service": "trello", "record": CARD, "finding": "rules 3-5 + socials comment -> COMPANY-HELD -> KEEP, not on the checklist"}]},
]

for b in m['call_budget']:
    if b['phase'] == 'per-record' and b['service'] == 'gsheets':
        b.update(calls=19, reason="one export per in-scope account (13), the old AdMob export (boundary), and the second tabs of five exports: Meta Partners, Google Ads 569 and 449 Linked managers, YouTube Removed users, Unity Ads advertiser")
    if b['phase'] == 'per-record' and b['service'] == 'gmail':
        b.update(calls=10, reason="September money evidence for the paid accounts (Meta receipts, AppLovin payouts, both Google Ads IDs, Adjoe, Unity, AdMob) and who else holds the three socials the exports cover only partly: YouTube Brand Account owners, TikTok Business Center partners (Node Media), Instagram portfolio admins")
    if b['phase'] == 'writes' and b['service'] == 'trello':
        b.update(calls=2, reason="create the checklist on the handles card; one item for the only social transfer (X)")
for w in m['writes']:
    if w['service'] == 'trello':
        w['count'] = 2
        w['depends_on'] = sorted(set(w['depends_on']) | {"T16", "T18", "T21"})
    if w['service'] == 'slack':
        w['depends_on'] = sorted(set(w['depends_on']) | {"T16", "T21"})
    if w['service'] == 'gsheets':
        w['depends_on'] = sorted(set(w['depends_on']) | {"T16", "T18", "T21"})

m['facts'] += [
    {"key": "Brand Account owner address", "value": "[EMAIL_126620]", "kind": "id", "home_ids": ["f_fc27672c5bfea8b760b074"], "must_appear_in": [YT_M, "f_fc27672c5bfea8b760b074"]},
    {"key": "TikTok partner", "value": "Node Media LLC", "kind": "name", "must_appear_in": [TT_M]},
]
m['design_delta'] += [
    {"id": "T16", "change": "YouTube export: Brand Account tab removed; Node Media's Owner role now only in Google's Brand Account notice to Fred (Gmail, 2025-06-11)", "reason": "hardening r2: 6/6 baseline runs listed every tab (run-6 #48 read the Brand Account tab), so the trap was on the first-read surface"},
    {"id": "T18", "change": "Instagram export: portfolio tab removed, note back to 'Login only'; the two portfolio admins now only in Meta's notice to Fred (Gmail, 2025-08-06)", "reason": "hardening r2: 6/6 runs read the tab (run-6 #29)"},
    {"id": "T21", "change": "TikTok export: Scope row 'Account logins'; TikTok for Business reminder (Gmail, 2025-07-16): Node Media LLC still Admin through Business Center", "reason": "hardening r2: no run searched for Node Media or for access notices; grounded on Node's Leadsie request C08MCEP1B9B/1728234009.536219"},
]
json.dump(m, open(P, 'w'), indent=2, ensure_ascii=False)
open(P, 'a').write('\n')
print('traps', len(m['traps']), 'chains', len(m['chains']))
