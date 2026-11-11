"""Scenario-stage amendment of 2026-11-08 (coordinator instruction): reclass 8 slots, refresh stale design text. Run once."""
import json
import pathlib
import re

WF = pathlib.Path(__file__).resolve().parent.parent
sp = WF / "01_Gradable_Surface.json"
s = sp.read_text(encoding="utf8")
IDS = ["S-K1b", "S-K3b", "S-K4b", "S-K5b", "S-H1", "S-G2", "S-D1", "S-E1"]
for sid in IDS:
    pat = re.compile(r'("id": "' + sid + r'",.*?"class": ")(direct|aggregate)(")', re.S)
    s, n = pat.subn(r"\1write_content\3", s, count=1)
    assert n == 1, sid
a = '"_note": "Rev 5.1 draft surface. Fact slots only. Slot titles state facts; no criterion text."'
b = ('"_note": "Rev 5.1 draft surface. Fact slots only. Slot titles state facts; no criterion text. Amended 2026-11-08: '
     'S-K1b, S-K3b, S-K4b, S-K5b, S-H1, S-G2, S-D1, S-E1 reclassed to write_content, because each value is text in a written '
     'deliverable (register reason column or memo) that no solver row holds; weights and selectors unchanged."')
assert a in s
s = s.replace(a, b)
sp.write_text(s, encoding="utf8", newline="\n")
json.loads(s)

dp = WF / "01_Scenario_Design.md"
d = dp.read_text(encoding="utf8")
R = [
    ("| Seeded pointer from note thread to Doc |", "| Seeded pointer from a channel post to Doc |"),
    ("All five roots checked clean", "All four touched roots checked clean"),
    ("The note thread names the Doc by title", "A top-level post after the note names the Doc by title"),
    ('"the rules we set under my note"', '"the rules I posted in the channel after my note"'),
    ('"the rules we set under my note still stand"', '"the rules I posted in the channel after my note still stand"'),
    ('"read the panel the way I set out when you asked who those players were"', '"read the panel the way I set out when Robert asked who those players were"'),
    ('"retention the way Robert set it under Vincent\'s post"', '"retention the way Robert set it in the channel after Vincent\'s post"'),
    ("Julia's question and Leonard's answer under the note (", "Julia's question and Leonard's answer, posted in the channel after the note ("),
    ("narrows who counts, later and in the same thread", "narrows who counts, later and in the same channel"),
    ("Robert's reply under Vincent's retention post sets", "Robert's channel post after Vincent's retention post sets"),
    ("by replies under `C090N54TG79/1759165414.829399`", "by a read of the channel after `C090N54TG79/1759165414.829399`"),
    ("it stays in the reply under Vincent's post", "it stays in the channel post after Vincent's post"),
    ("the ask, its channel pages back to the note, the note thread", "the ask, its channel pages back to the note, the rule posts after it"),
    ("| Note thread replies | ts", "| Rule posts after the note (top-level) | ts"),
    ("Root `C090N54TG79/1758517286.431379`: reply_count 4, reply_users_count 2, latest_reply `1758733233.117446`, thread_ts set",
     "Top-level in `C090N54TG79`; the note `C090N54TG79/1758517286.431379` keeps reply_count 0, because it has no base thread"),
    ("| `harmonygames-Games/match3d#476#rc_28`, `#rev_4` |", "| `harmonygames-Games/match3d#476#rc_28` (no review row; `#rev_4` removed) |"),
    ("Under the note: it would bury the ask in the rule thread.", "After the rule posts as a reply: it would bury the ask among them."),
    ("Slack replies under the note make it the hub, so rules enter through the note by name.",
     "Top-level posts after the note carry the rules, and each says what it refers to, so the rules enter through the note by name."),
    ('| "25–45" is an age band | Slack replies under `C090N54TG79/1758517286.431379`: Julia\'s question, Leonard\'s answer |',
     '| "25–45" is an age band | Slack top-level posts after `C090N54TG79/1758517286.431379`: Julia\'s question, Leonard\'s answer |'),
    ("Root gets `thread_ts`, reply_count 4 after R3, users 2", "The note keeps reply_count 0; the posts quote it"),
    ("(`2c84150a541063a6138e2f5a0cff9f33`) | Slack reply under the note |", "(`2c84150a541063a6138e2f5a0cff9f33`) | Slack top-level post after the note |"),
    ("game-industry people don't count | Slack reply under the note |", "game-industry people don't count | Slack top-level post after the note |"),
    ("| Slack reply under `C090N54TG79/1759165414.829399` | Sep 29 17:30Z | Robert | Vincent's retention post; root rc 0 → 1 |",
     "| Slack top-level post after `C090N54TG79/1759165414.829399` | Sep 29 17:30Z | Robert | Refers to Vincent's retention post; that post keeps rc 0 |"),
    ("Five roots get counter updates: `C090N54TG79/1758517286.431379`, `C090N54TG79/1758581651.167799`, `C090N54TG79/1758691397.679889`, `C090N54TG79/1759165414.829399`, `D05GU6L0XFH/1758901945.292269`",
     "Four roots get counter updates: `C090N54TG79/1758581651.167799`, `C090N54TG79/1758691397.679889`, `D05GU6L0XFH/1758901945.292269`, `C093LEZGF6J/1759258475.735779`"),
    ("`rev_3`, and `rev_4` for CodeRabbit, go in `integration_exceptions` citing #470 rev_3", "`rev_3` goes in `integration_exceptions` citing #470 rev_3; CodeRabbit's `rev_4` is not seeded"),
    ('The ask\'s "the rules we set under my note still stand" repeats', 'The ask\'s "the rules I posted in the channel after my note still stand" repeats'),
    ("Slack channel, `rc 0`", "Slack channel, `rc 0`"),
]
for a, b in R:
    if a not in d:
        print("MISSING", a[:70])
    d = d.replace(a, b)
# section 7 slot table: class column
for sid in IDS:
    d, n = re.subn(r"(\| " + sid + r" \| \d \| )(direct|aggregate)( \|)", r"\1write_content\3", d)
    assert n == 1, sid
d = d.replace("**Gradable surface.** `01_Gradable_Surface.json`: 23 slots, weight 77, mechanism share 88.3 % (reported, not gated).",
              "**Gradable surface.** `01_Gradable_Surface.json`: 23 slots, weight 77, mechanism share 88.3 % (reported, not gated), classes as amended 2026-11-08 (section 12).")
note = """### Amendment 2026-11-08 (injection found these; scenario stage re-gated)

**Surface.** `oracle_kit` `contract.slots` failed: `gradable_surface.solver_value` reads no solver value for `reason_matches` or `text` selectors, so a slot of class direct or aggregate with those selectors can never pass. Eight slots move to `write_content`. No weight, selector or row count changes. Each value really sits in a written deliverable:

| Slot | Was | Where the value is written | Solver holds it? |
|---|---|---|---|
| S-K1b | direct | `reason` column of the register in `f_43bc35baf77fd59f4e57b8`, row `ZOM-613` | a label only; the graded words are the run's |
| S-K3b | direct | `reason` column, row `ZOM-594` | same |
| S-K4b | direct | `reason` column, row `ZOM-573` | same |
| S-K5b | direct | `reason` column, row `ZOM-585` | same |
| S-H1 | aggregate | memo text in `d_8140f09bf9f1b94cb8ee2d` | yes, through `aggregates(rows)`, not a row |
| S-G2 | aggregate | memo text | yes, through `aggregates(rows)`, not a row |
| S-D1 | aggregate | memo text | the context row `panel` |
| S-E1 | aggregate | memo text | the context row `retention` |

Effect on the checks. `hardness_v2_check` INPUT_CHECK lists class `aggregate` only, so S-H1 and S-G2 leave its list: it now reads 1 weight-5 total (S-G1), not 3. They are still real totals that the four block rules move, by `mechanisms` on each slot; INPUT_CHECK simply stops looking at them. DECISION_FLIP reads `mechanisms` and weights, so it is unchanged.

**Records as built.** The five rule records (`C090N54TG79/1758553214.330914`, `C090N54TG79/1758554405.774120`, `C090N54TG79/1758728411.540327`, `C090N54TG79/1758733233.117446`, `C090N54TG79/1759167008.881274`) are top-level, because the note and Vincent's post have no base thread. The ask's quotes changed with them. `#rev_4` is removed: `stage_gate` re-runs `base_check` without a manifest, where it failed INT-01. `harmonygames-Games/match3d#476#rc_28` keeps `in_reply_to_id` on `#rc_27` and stands without a review row. Leonard's copy of the forward is `leonard.hayes@harmonygames.co/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>`, the same Message-ID as Julia's copy; the draft manifest's `planned_records.panel_forward.leonard_copy` is superseded by it. 17 sender mail copies and Claire's calendar copy are added. The F root UPDATE is keyed on channel and ts. The draft manifest keeps its old quotes as a design record; `01_Hardness_Manifest.json` `design_delta` carries each change.

"""
mark = "### Self-review\n"
i = d.index(mark, d.index("## 12 Self-test results"))
d = d[:i] + note + d[i:]
dp.write_text(d, encoding="utf8", newline="\n")
print("amended")
