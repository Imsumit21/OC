RED TEAM FALLBACK (rev2): REDTEAM_* is still unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer. In its place, on the requester's instruction of 2026-11-08 ("use many subagents in parallel"), cold Claude subagents reviewed the rev2 design: four census scouts (research/rev2/census_a_bounce.md, census_b_carta.md, census_c_alias.md, census_d_adv.md), a leak audit (leak_audit.md), a cold coherence attack barred from the census files (attack_coherence.md) and a cold UGT attack barred from them (attack_ugt.md). They are not the dual red team, and this stays in every Unresolved line.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| AC-N1a BLOCKING the told rule said "sent", and a bounced letter was sent | attack_coherence.md | Fixed: the notes say "a written message about the closing that reached them directly" |
| AC-N1b low "inactive" is the base's line for suspended work accounts | attack_coherence.md | Fixed: the 550 line now reads "is disabled. Learn more at ...", as the base's personal-address bounce (leonard.hayes@harmonygames.co/1768008486819265505) |
| AC-N2a low the Jan 23 change left no Carta admin trace | attack_coherence.md | Accepted as the single low item: a holder-side notice is how Carta tells the holder; an admin copy in Leonard's Carta stream would put the correction on the run's bulk Carta path (census_b V1, 20-25 % landing) |
| AC-N2b advisory no recorded reason for the extension | attack_coherence.md | Fixed: Calvin writes "Thanks for sorting out the extra weeks I asked for" |
| AC-N2c cosmetic thread id at .000 ms | attack_coherence.md | Fixed: thread 1856121753612004097 (.542 ms) |
| AC-N3 low a Feb 10 told-mail clashes with Leonard's Feb 10 notes and Feb 12 list | attack_coherence.md | Fixed: the mail goes Feb 12 22:52Z, after the list and before Robert's 23:41Z angel mail |
| LA-1..5 the prompt-round fixes hand over answers | leak_audit.md | Kept: BOARD, ASOF and the Griffin ask passed on the platform-era data without them; removing them reopens fail-level forks |
| CD-1 the #executives note and KPMG's item-1 sentence state the advisor split | census_d_adv.md | Fixed: numberless "go by the ledger" reply; KPMG's item-1 sentence removed |

RED TEAM UNAVAILABLE: REDTEAM_* is unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer.

RED TEAM FALLBACK: four independent cold Claude agents (general-purpose subagents, no prior context, hg.py searches, told to break the design) reviewed it in place of the dual red team, on the requester's instruction of 2026-11-07 ('go with your recommendations on all six'): a fork sweep as the /prompt evaluator, a coherence sweep as the /injection evaluator, a run simulation as an Opus 5.5 adversary, and a delta review of the rewritten rule by a reviewer barred from the earlier reports. Reports: research/sweeps/fork_sweep.md, coherence_sweep.md, run_sim.md, delta_review.md. They are not the dual red team, and this stays in every Unresolved line until something covers it.

Summary: 5 blockers and 13 majors in the first three, then 3 blockers and 3 majors in the delta, all in sentences the first fixes had just written. No base record flatly contradicts the plan, every graded number recomputed, and the censuses found no other told holder, open equity question, family contact or option line. Every finding was weighed against the base before changing the design.

| Finding | Source file | Disposition with evidence |
|---|---|---|
| FS-01 BLOCKER four holders get two classes | fork_sweep.md | Fixed. H1: one row and one note per person, handled on their stock; §2, two-reading row. Avoids naming advisors, per LEAK-1 |
| FS-02 BLOCKER 'personal' has no sender | fork_sweep.md | Fixed. H1: from any of the three of us; two-reading row |
| FS-03 BLOCKER no class-to-state map | fork_sweep.md | Fixed. States in the project description, ENG-2438 |
| FS-04 BLOCKER no record says who goes first | fork_sweep.md | Fixed. H1: whoever's last day comes first |
| CS-01 BLOCKER project cites later records | coherence_sweep.md | Fixed. project updated_at follows the Sunset mail; created_at stays, §11 |
| FS-05 family sentence covers Enes | fork_sweep.md | Fixed. 'the rest of the family's lines, which need no note of their own' |
| FS-06 backdated dates | fork_sweep.md | Fixed. KPMG: regardless of when recorded; rows must not penalise a run that flags it |
| FS-07 graded totals have no ask | fork_sweep.md | Fixed. KPMG asks each option line and the total; Sunset asks the totals and counts |
| FS-08 newest board record omitted | fork_sweep.md | Fixed. two-reading row cites C04UEQVDVB7/1752517647.842649 |
| FS-09 comment count | fork_sweep.md | Fixed. 12, §2, §7, §9 |
| FS-10 resolvers not visible | fork_sweep.md | Fixed. seed says formal notices come later; research file no longer a resolver |
| FS-11 to FS-16, FS-18 | fork_sweep.md | Fixed in the two-reading and self-review rows, C07C2866011/1770837454.464209 added to T4 |
| FS-17, CS-06 Robert reads as planted | both | Fixed. Moved to Nebojsa, his ex-coworker; reply on their own thread leonard.hayes@harmonygames.co/1773963101399472184 with a reason in its first line |
| CS-02 'counts only' against FY24 | coherence_sweep.md | Fixed. body cites the Standard Metrics submission leonard.hayes@harmonygames.co/1856787396431935562 |
| CS-03 bare figures in comments | coherence_sweep.md | Fixed. quoted and dated, §11 rule |
| CS-04 last-contact values | coherence_sweep.md | Fixed. values from §1a; stamped before Robert's reply |
| CS-05 Tuesday against Feb 15 | coherence_sweep.md | Fixed. one line in H1 tying it to C0ADGSZKR3R/1770933601.686309 |
| CS-07 T3 resolver false | coherence_sweep.md | Fixed. T3 rewritten; deck attributes its figure |
| CS-08 Arthur has no Trello actions | coherence_sweep.md | Fixed. Leonard writes the card and comment; list id corrected to 640643a3fd8f3ca308d93195 |
| CS-09 to CS-22 | coherence_sweep.md | Fixed in §1a corrections, §11 and the Must-not list. CS-18: T9's Drive timestamp stays manifest-only, no row uses it |
| LEAK-1 rule doc as a trap index | run_sim.md | Fixed. neutral sentences; family moved to a DM; no sentence names a case |
| LEAK-2 'every angel investor' | run_sim.md | Fixed. K3 removed; H1 quotes no base sentence |
| LEAK-3 T7 caught by the plan's calls | run_sim.md | Fixed in part. reply sits on a 2023 thread dated Feb 12; address searches cut from 26 to 12. A run that searches his address still finds it, which is fair |
| LEAK-4 'board position' returns both | run_sim.md | Accepted. Base records; BOARD is not counted as a hard trap |
| LEAK-5 titles show the surname | run_sim.md | Fixed. owner-list forms; no Eren contact row |
| LEAK-6 ASK rows pass on a date note | run_sim.md | Fixed. Q1 needs an answer to the question; Q2 is now a date sample |
| LEAK-7 last contact leaks told state | run_sim.md | Fixed. none on ENG-2440, ENG-2446, ENG-2459 |
| LEAK-8 to LEAK-11 | run_sim.md | Fixed. 'any special terms'; Arthur row added; figures required. LEAK-9 accepted, T22 not counted |
| OH-1, OH-2 ASOF rows | run_sim.md | Fixed. selector accepts ES-16 or 35,605; KPMG asks each option line |
| OH-3 ASCII spelling | run_sim.md | Fixed. title uses Segerstråle, the base spelling |
| OH-4 weight on drafts | run_sim.md | Open. Pre-check proves it first; fallback is sends. In Unresolved |
| OH-5, OH-6 | run_sim.md | Fixed. B1 accepts either order; board row cites the call |
| Row tagging: 27 weight never flipped | run_sim.md | Fixed. K2, K3, A3, S1, S2 and the Tor rows untagged; lookups cut to weight 1 |
| Forecast: baseline 76 to 82 % | run_sim.md | Accepted. §6 now states 78 % central and that under 70 % is not supported |
| Delta F1, F2 BLOCKER state sentence decides 18 of 26 | delta_review.md | Fixed word for word: Canceled where the line holds nothing; otherwise Todo where its own note is waiting, Done where it isn't; ENG-2444 |
| Delta F3 BLOCKER 'addressed to them' lets `<!here>` in | delta_review.md | Fixed. 'sent to them directly'; ENG-2463 |
| Delta F4 Robert's line promised a note | delta_review.md | Fixed. line removed; promises nothing further; ENG-2446 |
| Delta F5, F15 KPMG wording | delta_review.md | Fixed. 'each effective date as Carta shows it'; closes ES-1, ES-4, ES-15 and Collins; leonard.hayes@harmonygames.co/1830959847543474636 |
| Delta F6 dangling pointer to the family rule | delta_review.md | Fixed. At injection the line moved to a reply under the Feb 12 list, which H1 names twice and every run must write under |
| Delta F7 to F14, F16 | delta_review.md | Fixed. §4 amendment names the family sentence; 'at most one note'; Robert copy row robert@harmonygames.co/1773963101279916523; a dated last contact on all 26 removes the gap (ENG-2440); 'their total'; ES-4 only |
| Delta: reason comments had no carrier | delta_review.md | Fixed. the state sentence now requires them; ENG-2452 |
