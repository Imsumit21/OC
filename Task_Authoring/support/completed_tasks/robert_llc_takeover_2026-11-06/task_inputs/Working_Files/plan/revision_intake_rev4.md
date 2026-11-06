Verdicts consumed: `run_forensics/rev3/precheck.node_verdicts.json`, from `/create-hardening` MODE B (pre-check), revision 3 (`Working_Files/01a_Hardening_Report.md`, gate PASS).

The export is `06_PreCheck_Trajectory/trajectory.json`: one platform Opus 5.5 run, sha256 53c30765e132, 168 counted calls. It is BOUND to rev3 on discriminating content (12 rev3-only needles seen; rev1 and rev2 SQL were passed and excluded). It certifies nothing about rev4.

The tool proposed BYPASSED for every rule. The cause is a decoder keying defect: the run's sheet keys carry an ` (ENG-n)` suffix. The verdicts below are the hardening report's hand dispositions; each is also in the ledger as `hev_…`.

| Node | Runs | Proposed (tool) | Disposed (01a) | Disposition | Evidence |
|---|---|---|---|---|---|
| CORR | precheck | BYPASSED | LEAKED | keep: stable backbone; hardening it would put more failures on the DD cascade (the platform's failure-pattern warning) | precheck event 211: a `from:Arthur after:2026-02-08` search returned the $140 reply first; ledger hev_3a71c99557336ba6 |
| AUTH | precheck | BYPASSED | LEAKED | keep: same reason; the ground rules naming the table is a UGT link | precheck event 180: one January query, DD 183.11 / ZM 0.00; ledger hev_2da16037a402bf13 |
| FILT | precheck | BYPASSED | LEAKED | rebuild: the campaign status drops the project word; facts unchanged | precheck event 44: the Slack search "LLC" returned the VO reply second; ledger hev_b76760802056e969 |
| COMPLETE | precheck | BYPASSED | LEAKED | keep: the lead is base data (C0ADGSZKR3R/1770937232.664809) and cannot be reworded | precheck event 256: the $248 thread read after a mail search by tool names (precheck event 247); ledger hev_d2253957e65e0329 |
| DONE | precheck | BYPASSED | LANDED | rebuild: the project's Done rule makes the miss flip ENG-2462 to Done; the notice and its bland snippet unchanged | precheck event 269: the notice fetched as `format: minimal`, body never read; false "already live" at precheck event 316, 342, 405 and 492; ledger hev_f9b2298b6c9739d4 |
| EXC | precheck | BYPASSED | FALSE | purge: the trap leaves the design; Calm Play stays as a control row decided by the ground rules' vehicle sentence, kept for UGT | precheck event 425 cites "the new one" from the ground rules (read at precheck event 22); ledger hev_9cefe52f59fd5be5 |
| DATE | precheck | BYPASSED | LANDED (minor) | rebuild: the export caveat leaves the issue note; the art and its owner move into a reply under the base access-date post | precheck event 316: the layer.ai row has no owner or date; "March 3" never seen in any result; ledger hev_3d96146a0a8b19a5 |

**CONFOUNDED candidates.** `node_verdicts` flagged none (no `flags` on any rule). Two items are confirmed CONFOUNDED (fairness) and rejected as hardness evidence:
- Surface slots R1 ("$3,202 March cash need") and R5 (the tradeoff). The rev3 prompt never asks for either, so a run could not fairly be failed on them; the rev3 run's reply at precheck event 492 gave the thirds and the cash, which is what was asked. Both are retired from the rev4 surface; L2 is dropped with EXC.
- The tool's BYPASSED proposals. They are a decoder keying defect, rejected on review of precheck event 316. That event holds all 38 rows, under keys like "Combo Fighter (ENG-2438)".

**New mechanism (not a verdict):**

| Node | Runs | Proposed (tool) | Disposed (01a) | Disposition | Evidence |
|---|---|---|---|---|---|
| STACKS | precheck | none (new in rev4) | none | rebuild (added): a later owner email corrects CF's stacks figure on ENG-2445, which every run reads; answer unchanged at $62 | precheck event 106 read ENG-2445's comment (then $62) and the run kept it; RB5 of 01a §10 |

**Routing.**

| Item | Route | Evidence |
|---|---|---|
| Universe changes (FILT, DONE, DATE, STACKS wording and records) | S5a onward here, then `/create-injection` as rev4, then `/injection` + `/prompt` after both blind sweeps | precheck event 44, precheck event 269, precheck event 316 and precheck event 106 |
| Surface defects (R1, R5 unincorporated; Decision labels; per-row patterns) | fixed here: `01_Gradable_Surface.json` revision design-2 (rev4) | precheck event 316 (labels "One of us", "Not used"; C4 matched "Feb 25" on the next row) |
| Prompt | no defect: unchanged, sha256 ccd229a59a17; RULE_IN_PROMPT CLEAN | precheck event 3 matched the prompt by content |
| OE and rubric (later stages) | accept "One of us" / "Not used"; no $3,202 or tradeoff row; grade the ENG-2462 state, the DD support step and the layer.ai export date | precheck event 342 and precheck event 336 (what the rev3 run wrote) |
