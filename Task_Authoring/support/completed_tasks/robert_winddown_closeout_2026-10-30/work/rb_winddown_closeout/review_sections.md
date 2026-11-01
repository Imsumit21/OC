## 12 Self-test results

`python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design` (verbatim):

```
@@HARDNESS@@
```

**Lazy-solver pass** (one broad search per service, first hits only, no thread or reply opened, stops at the first
conclusion, every bulk shortcut used):
- Slack: reads the anchor and the #winddown history page → keep list, action items, 'covers everything', LLC moves,
  'cancelled' claims. Gets Deel/Intuit Keep, Metabase Move, most Cancel actions right. Misses the Gusto reply
  (thread, `@@GUSTO@@`) → Gusto wrong in action, status, deadline and the after-plan total.
- Linear: `linear_list_issues` on the project → 48 titles, assignees, description. Never lists comments → wrong owner for
  Docusign (ENG-2469), wrong in/out for OpenAI/Typecast/Adobe/JetBrains/Solsten (ENG-2441, ENG-2442, ENG-2450, ENG-2447,
  ENG-2453), wrong status for Unity/Layer/Singular, and Metabase/GitHub/dbt card state unknown.
- Gmail: one search 'checklist' → Sherwood's (Feb 11) and Sunset's (Feb 12) first messages. Reads the first hit only →
  either Sherwood (cancel everything) or Sunset v1 (Metabase held, Trello/dbt/BigQuery cancelled). Never opens the
  thread's second message. No per-vendor receipt search → no next-charge dates: every Cancel deadline guessed.
- Trello / Calendar / Confluence / GitHub / Snowflake: a lazy run opens none of them → no Feb 19 card deadline, no Mar 12
  hold date, Helpshift export unknown, CodeRabbit Requested, Meta Ads/AppLovin missing.
- Sheets: reads the costs tab → Dec-25 costs right for the tab rows only if it reads column AF (the header dates are a year off — the trap row in §10); one Sound row; iPostal kept at 34.79.
- **Leaks found and fixed in this design:** (1) the review event was first minted after the checklist that calls it
  booked — moved to Feb 12 22:40Z (§10 Explicit rules); (2) the project description first carried 'vendor has confirmed'
  in its Done rule, which would have put the A15 house rule in the most-read record — removed, Done now says 'once the
  account is closed' and rule 5 defines closed; (3) the SVB card text first asked to 'put the new card next to it in the
  register', a manufactured column — removed; (4) the blanked '[PERSON_NAME_20852]' and '[USERNAME_30019]' vendors in
  #winddown left a second reading of membership — Leonard's base subscriptions table (C0ADGSZKR3R/1770933450.410449) names Kapwing (ENG-2478) and Arthur's ENG-2457 comment states dbt's KubLLC move (an invented Notion/Sentry mapping was removed at the /injection review, F2). Review fixes (§13) removed the remaining cues ('nothing back yet', billing days in comments, exact costs in Arthur's sheet). What the lazy run still scores: Keep/Move actions, the tab costs if it picks column AF, the exclusions it can
  read from the tab (Veed, Kling, Hailuo zeros), the share and the reply's existence — about 30–40% of the weight.

**Literal-value sweep** (each decisive value searched across the seeded wording in `planned_text.json` and the base):
'Feb 19' / 'Feb 20' appear only in the SVB card (`@@SVB@@`); no seeded record carries a card number; 'March 12' / '2026-03-12' only in the event start (no mail subject, no_notify);
'Trello is part of the bundle' / 'keep BigQuery and dbt' only in the correction (`@@SUNSET2@@`); 'on the 3rd' (Gusto)
only in the thread reply; meta/applovin amounts only in Snowflake (FIN-000688/FIN-000689/FIN-000699/FIN-000700); the
Sound line split only in the costs tab and the Pond5/ElevenLabs mails; 'canceled on Feb 12' only on Combo-Fighters#38 (matching CodeRabbit's base notice to Arthur). No
base record carries these values (`hg.py search` 'Feb 19', 'data delivery', 'KubLLC card', 'Shutdown – accounts': only
the base C0ADGSZKR3R/1770937232.664809 for KubLLC).

**Wording sweep.** Rule 5's decisive words ('confirmed', 'Closed', 'Requested') appear in no seeded comment or receipt;
cancellation mails say 'has been cancelled/canceled' (vendor voice), founders say 'cancelled' (our voice) — the rule, not a
keyword, separates them. Sunset's list never says 'Hold'; the SVB card never names an account; no comment says 'Keep'.

**"The rest stands" check.** After K9 (Gusto) no record re-asserts 'keep gusto'; after K4 (Metabase out) no record
re-asserts Metabase on the list (searched 'gusto', 'metabase' over `planned_text.json`; base mentions are older:
C0ADGSZKR3R/1770933601.686309, /1770937232.664809).

### Self-review

Walked against `Evals/1_Prompt_Eval.md` §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence)
and `Evals/0_Injection_Quality_Eval.md` Check C, in that order. Every base value below was re-read through `tools/hg.py` /
the export (`persona_view` for reach); planned values come from `planned_text.json` and `truth.json` (emitted, not typed).

| # | Item | Counter-reading (strongest case it FAILS) | Resolution with evidence |
|---|---|---|---|
| 1 | temporal | A seeded record refers to something that did not exist yet (the checklist calls the review call 'booked') | fixed: event created 2026-02-12T22:40:15Z (`minted_ids.json` E_REVIEW) before the checklist 23:58:21Z, after the SOW signing C0ADGSZKR3R/1770931777.561519 |
| 2 | semantic | 'Closed' could mean 'we cancelled it' (Arthur's 'coderabbit is cancelled', C0ADGSZKR3R/1770936655.574079) | rule 5 in `planned_text.json` DOC_CONV defines Closed as vendor-confirmed and lists the carriers; the counter reading is the designed A15 trap T13 |
| 3 | cross-service referential | the redacted vendor names in #winddown (C0ADGSZKR3R/1770839715.391309, /1770937232.664809) point at accounts no issue covers | Leonard's table C0ADGSZKR3R/1770933450.410449 names Kapwing (ENG-2478); dbt's move is in Arthur's ENG-2457 comment; the costs tab's '[PERSON_NAME_0499]' is Singular (trap_catalog X03) |
| 4 | quantitative | Helpshift's monthly cost could be read as $1,500 / $300 (C0ADGSZKR3R/1770673467.186629, hazard Q07) | rule 8 reads column AF (150, f_605121f4a36752645e0ac3 row 10); balances are owed amounts, not a month |
| 5 | quantitative | AWS cost: the tab says 0, Confluence page_aws_infra ~$1,550, Arthur ~$1k | rule 8 fallback (revised at /prompt): tab 0 → the owner's figure in ENG-2455 (1,485; Arthur: the P&L line was never kept up), matching FIN-000687 |
| 6 | state/lifecycle | Trello's paid plan ended Nov 21 (robert@harmonygames.co/1849420841999587093), so rule 2 drops it | rule 2's exception ('anything on Sunset's list goes on the register whatever else applies') + the correction naming Trello |
| 7 | state/lifecycle | Singular could be Closed: Leonard terminated it on Feb 12 (robert@harmonygames.co/1853470745017478863) | the same message asks Singular to 'confirm in writing'; no reply exists before the clock → Requested |
| 8 | identifier/format | the conventions doc's owner 'Resource: 7240535625619857401' is not an email (hazard I14) | it is the owner of every Wind Down sibling (f_31115ddb6ed866f2b10d60); Robert reads it through its share list |
| 9 | other | 'Sunset' is redacted in Slack ([USERNAME_26907], C0ADGSZKR3R/1770931777.561519), so Sherwood could be the provider | the signed SOW mail robert@harmonygames.co/1856956532017091340 names Sunset; Sherwood's mail says 'If you decide to engage us' |
| 10 | two-reading: Trello | best argument it is out: cancelled before Feb 9 | resolved in §10 row 1 (correction `@@SUNSET2@@`, rule 2 exception) |
| 11 | two-reading: Metabase | best argument it is a Hold: the first checklist names it | §10 row 2: correction removes it; ENG-2456 comment confirms the KubLLC card |
| 12 | two-reading: GitHub | best argument it is a Move (Arthur's LLC message C0ADGSZKR3R/1770937232.664809) | rule 4 'Sunset's list wins over everything above' → Hold, Mar 12 |
| 13 | two-reading: Gusto | best argument it stays Keep (C0ADGSZKR3R/1770933601.686309) | the later reply `@@GUSTO@@` in that thread, incorporated by A1's 'the replies under it' |
| 14 | two-reading: CodeRabbit | best argument it is Requested: no mail from CodeRabbit | rule 5 accepts 'an in-app or bot notice'; harmonygames-Games/Combo-Fighters#38#c_1 is the vendor's own |
| 15 | two-reading: Singular deadline | best argument for Mar 14: the extension to Mar 15 | Mar 15 is the overdue balance's due date (robert@harmonygames.co/1853470745017478863); invoices Sep 1, Dec 1 (robert@harmonygames.co/1850283027022457279) → Mar 1 → Feb 28 |
| 16 | two-reading: Helpshift deadline | best argument for Feb 27: export pending | comment_support_after_helpshift_c1 on page_support_after_helpshift logs the export and the switch-over Feb 13 |
| 17 | two-reading: Figma deadline | best argument for Feb 19: the SVB card is on file | `@@FIGMA@@` next charge 2026-09-11, after the Mar 12 review → rule 6 'won't charge it again before Sunset's review call' |
| 17a | two-reading: costs-tab column | best argument for column AR: its header reads 2025-12-26 | rule 8 names column AF by position; HG P&L's Dec-25 (header 2025-12-25) is column AF; subtotals tie (UA 610) |
| 18 | two-reading: Meta Ads cost | best argument for 956.45 (last ledger line, FIN-000700) or trailing 30 days (page_ua_vendor_closeout) | rule 8 'last full month in the ledger (January)' → FIN-000689 2,843.84; the UA page is scoped to the Growth/UA tracker |
| 19 | two-reading: Docusign owner | best argument for Leonard (assignee of ENG-2469) | rule 7 + Leonard's handover comment on ENG-2469 |
| 20 | two-reading: clashes | best argument the GitHub/Metabase card moves or Gusto also clash | card moves close nothing; the three that Sunset forbids are C0ADGSZKR3R/1770840054.486779 (free plan), /1770842405.931359 (guest seats), /1770933903.645709 (archive); extras accepted |
| 21 | two-reading: Confluence | best argument it is out: never billed, not in the project | Sunset's list names it (`@@SUNSET1@@`), rule 2 exception, rule 8 'never charged us are 0', rule 7 owner Robert |
| 22 | feasibility | Robert cannot write into the Wind Down folder (d_e5caf6a8c630421942ee59, persona_view NO) | A1 asks for a shared sheet, not a folder; Robert owns what he creates and shares it (gdrive_share_file) |
| 23 | difficulty | the levers might all reward one 'deep reader' trait (Douglas round 2, SD collapse) | §6: nine levers in seven services with different habits (thread reply, mail thread, Trello, Calendar, Snowflake, PR bot comment, page comments); rubric must be replayed with `difficulty_stats.py` |

Expected baseline metrics (to be measured, never assumed): errored runs 0 of 6 expected (no forced errors; Friction: none);
pass@1 0 of 6 expected (no run expected to find all nine levers); average ~62–70% before the rubric is modelled; SD
0.1–0.3 if levers stay independent; ≥ 2 failure patterns with the largest ≤ 50%; horizon basis = rollout mean, budget
@@BUDGET@@ → expected counted calls ~185–260 (Douglas ratio), every run above the author's 150 floor if each issue is settled.

Gate output pasted above (HARDNESS GATE (long (design)): PASS). Re-verified base values: P&L Dec-25 column AF
(f_605121f4a36752645e0ac3 HG Costs rows 2–73, re-read after review A #1), ledger FIN-000686…FIN-000704, #winddown timestamps (C0ADGSZKR3R/2026-02.json),
Robert's mail 00016283/00016086/00016395/00016044/00016902 (thread ids in §1), persona_view can-see (§10 Reach table).

Unresolved: (1) Linear comment rendering of injected comments is verified (Ask_Carriers §6b) but `linear_list_comments` per
issue vs a hypothetical bulk path must be confirmed in the Opus pre-check; (2) whether runs open the review event (Calendar
5/131) — the mail names the call, so the fact is reachable, but the find rate is unmeasured; (3) the rubric's atomic
weighting decides the average — projection deferred to `/create-rubric-writing`.

@@REDTEAM@@
