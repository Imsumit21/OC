"""Round 5 manifest update (pairs with harden_r5.py). Idempotent from the round-4 manifest backup.

Usage: manifest_r5.py <round-4 manifest> <out manifest>
"""
import json
import sys

M = json.load(open(sys.argv[1]))
REPLY = "julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"
FIRST = "julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>"
L1 = "33c941fae57ba8d1e23bc1dff9ce3e2c"
NEW_TID = "1844695547248825769"
RULE3 = "What is in the store builds and what counts as shipped: Blake's store builds mail and his reply to it."


def by_id(lst, i):
    return next(x for x in lst if x.get('id') == i)


R = M['requirements']
R['R2'] = R['R2'].replace("under Blake's store builds mail:",
                          "under Blake's store builds mail and his reply to it (the reply, in its own Gmail thread because he changed the subject, carries the rule):")
R['R4'] = R['R4'] if 'Blake' in R['R4'] else R['R4']
R['R7'] = (R['R7'].rstrip('.') +
           "; ZOM-199's comment says what Blake's reply says the build does: CPM > 90 (not >= 90), checked when the 10th game ends, wins and losses both counted;"
           " each of the 7 Editor only / Not shipped comments names the two builds checked, iOS 0.3.49 and Android 0.3.133 (Leonard's thread reply under the ask)")

k5 = by_id(M['ask_fragments'], 'K5')
k5.update(container=NEW_TID, delegation_quote=RULE3, requirement_ids=sorted(set(k5['requirement_ids']) | {'R2'}),
          resolver="the reply sits in its own thread (Blake changed the subject); card rules 3 and 6 name 'his reply to it'")
k14 = by_id(M['ask_fragments'], 'K14')
k14['requirement_ids'] = sorted(set(k14['requirement_ids']) | {'R7'})

t5 = by_id(M['traps'], 'T5')
t5['seeded_ids'] = [REPLY if x == FIRST else x for x in t5['seeded_ids']]
t5['resolver'] = "the notes (runtime label; editor stats panel) against the editor/debug rule in Blake's reply"
t6 = by_id(M['traps'], 'T6')
t6['resolver'] = "Blake's reply (own thread, subject 'editor stuff and ZOM-199, before Monday'): the code checks > 90 when the 10th game ends"
t6['discovery_order'] = "the first mail's thread holds only the first mail; the reply is a separate conversation that the 'store builds' search does not return"
t7 = by_id(M['traps'], 'T7')
t7['resolver'] = "Blake's reply: level editor and debug tooling are stripped before shipping"
for v in t7.get('version_records', []):
    if v.get('id') == FIRST:
        v.update(id=REPLY, at="2025-09-30T13:26:05Z")

c3 = by_id(M['chains'], 'C3')
for h in c3['hops']:
    if h['record'] == FIRST:
        h['record'] = REPLY
        h['finding'] = "Blake's reply (own thread): level editor / LevelDesigner and debug tooling stripped; editor-only tickets never reached players"

if not any(t['id'] == 'T30' for t in M['traps']):
    M['traps'] += [
        {"id": "T30", "family": "tool_surface", "services": ["gmail", "trello"], "seeded_ids": [REPLY, "68daca5871dba40417a00383"],
         "base_pointers": [], "requirement": "R2",
         "expected_wrong_reading": "reads only the 'store builds for monday' thread (one message), judges Editor only from ticket titles, marks the attack-power editor tickets ZOM-277/ZOM-315 Live, and comments nothing on ZOM-199 or only '> 90'",
         "resolver": "card rules 3 and 6 name 'his reply to it'; the reply is a separate Gmail conversation found by a sender or subject search (from:arthur.blake, ZOM-199)",
         "discovery_order": "gmail_search_messages returns ids only; 'store builds' returns the first mail's thread, which holds one message"},
        {"id": "T31", "family": "synthesis_omission", "services": ["slack", "linear"], "seeded_ids": [L1],
         "base_pointers": ["ZOM-173", "ZOM-200", "ZOM-277", "ZOM-315", "ZOM-202", "ZOM-280", "ZOM-293"], "requirement": "R7",
         "expected_wrong_reading": "writes the checklist comment ('not in the store builds') without the two build numbers",
         "resolver": "Leonard's thread reply under the ask: put the two builds in those comments (ios 0.3.49 and android 0.3.133)",
         "discovery_order": "the checklist item is read first and looks complete; the build-number line sits in the thread reply"}]

if not any(c['id'] == 'C14' for c in M['chains']):
    M['chains'].append({"id": "C14", "root_cause": "A14", "ends_in": "R2", "hops": [
        {"service": "trello", "record": "68daca5871dba40417a00383", "finding": "rule 3: Blake's store builds mail and his reply to it decide what shipped"},
        {"service": "gmail", "record": FIRST, "finding": "the first mail gives the builds only; its thread has no reply"},
        {"service": "gmail", "record": REPLY, "finding": "the reply, in its own thread, strips level editor and debug tooling; ZOM-199 is wrong on > 90 and on 10 games"},
        {"service": "linear", "record": "cmt_b0aa45d307c981ce4487", "finding": "ZOM-277 is the editor stats panel average -> Editor only"}]})

for b in M['call_budget']:
    if b.get('service') == 'gmail' and b.get('phase') == 'discovery':
        b.update(calls=4, reason="search for Blake's store builds mail and open its thread; search for his reply (own thread, new subject) and open it")

F = M['facts']
if not any(f['key'] == 'comment builds (L1 reply)' for f in F):
    F.append({"key": "comment builds (L1 reply)", "value": "0.3.133", "kind": "version", "must_appear_in": [L1]})

DD = M['design_delta']
if not any(d.get('id') == 'R5-K5' for d in DD):
    DD += [{"id": "R5-K5", "change": f"Blake's reply moves to its own thread {NEW_TID} (subject 'editor stuff and ZOM-199, before Monday'); it now carries the editor/debug stripping rule and both ZOM-199 corrections; card rule 3 names the reply",
            "reason": "hardening round 5: a second independent carrier (Gmail reply) for the failure-pattern gate"},
           {"id": "R5-K14", "change": "Leonard's thread reply under the ask adds: name the two builds in the Editor only / Not shipped comments",
            "reason": "hardening round 5: per-comment output rule (A21) on the thread carrier"}]
json.dump(M, open(sys.argv[2], 'w'), indent=2, ensure_ascii=False)
print('ok', len(M['traps']), 'traps', len(M['chains']), 'chains')
