# 06 Spread Plan (rev5, findability changes)

Requester decision 2026-11-08: move the four blocks toward 50 % found, with a six-run average of about 45-50 %. The /create-difficulty gates: population SD 0.10-0.30; at least 2 patterns, with the largest under 45 % of failing runs (requester margin; the gate is <= 50 %); fewer than 5 full passes; corrected average under 85 % (mode medium, unchanged). Analysis and spec only: no task file was changed. Scripts are in `Working_Files/plan/spread/`.

Status labels: [V] checked in files or base exports; [S] simulated, UNCALIBRATED; [J] judgement.

## Requester decision (2026-11-08, binding)

- **Keep SQL rev5 unchanged** (sha `5b6e011195059d47…`). The rev6 findability changes are dropped: they don't raise P(all gates), and the K3 wording could read as a hint.
- **Binding for the rubric plan (`/create-rubric-writing`):** split the ticket-state work so each block fails its own row. S-ST1 becomes one Canceled-state row per block (K1, K3, K4, K5), and S-ST2 becomes "exactly the 17 counted sessions are Done". Weights stay by kind of work (1/3/5) and are never raised. Simulated effect (UNCALIBRATED): P(all gates) from about 0.51–0.54 to about 0.57–0.63, average +0.02 to +0.035.
- **Check before relying on it:** that `/rubric` and the surface grader accept several rows covering one surface slot without a duplicate-fact or bundling finding, and that no fact lands in three or more rows. If either fails, report it before drafting and don't force it.

## 0. Inputs read
- `01_Gradable_Surface.json`: 23 slots, weight 77, frozen. `01_Hardness_Manifest.json` and draft (`planned_records`, `ask_fragments`). `solver/solver.py` (`_k1_scope`, `_k5_builds`, `_DECIDING`).
- `01c_Forecast.json` and the hev_31aeef573fe8aea8 notes in `01_Grounding_Dossier.md` (flip table, the 1.00 / 0.545 / 0.442 / 0.338 / 0.234 ladder).
- `00_Route_Hunt.md` and `00_Carrier_Calibration.md`. The calibration figures are **miss** rates (record-runs missed). `01d_SQL_Review.md` M4. `00_Signature_Sim.py`. `plan/NOTES.md`. `plan/data.py` (rev5). `01_Universe_Inject.sql` (sha 5b6e0111).
- `Task_Authoring/tools/difficulty_stats.py`: `_gates` uses weighted rate = passed/total and `statistics.pstdev`. `group_patterns` uses single-linkage with symmetric difference <= 1 rubric, over failing runs only. Largest share = largest group / failing runs. V3 counts full passes against `full_pass_failure_count` 5.
- There is no pre-check or baseline yet (06/07 folders hold only READMEs), so every find rate below is judgement.

## 1. Monte Carlo model (gate-exact)
`plan/spread/spread_mc.py` [S].
- **Runs.** Six per trial. Each of R_K1, R_K3, R_K4, R_K5, R_F, R_D, R_E is missed at its miss rate. A miss fails every slot that lists it. The five slots with no mechanism (S-O1, S-O2, S-R1, S-M1, S-L1) fail independently at a 5 % slip.
- **Shared thoroughness.** A Gaussian copula inside each run, with latent correlation rho = 0 or 0.6 across all seven mechanisms. Marginal rates are kept exactly. Runs are independent of each other.
- **Gates.** Copied from `difficulty_stats.py`: weighted rate over 77, population SD with band edges inclusive, failing runs, single-linkage patterns (<= 1 slot difference), share < 45 % (and <= 50 %), full passes < 5, average < 0.85. Slots stand in for rubric rows, one row per slot.
- **Non-block miss rates** [J]. F 0.30 (Route Hunt: found about .70). D 0.10: the forward states the void and needs one calculation. E 0.25: a warehouse query plus the weighted D7. Sensitivity runs at 0.20/0.05/0.15 and 0.40/0.15/0.35.
- **Ladder** [V, from the surface]. 0 block misses 1.000, 1 miss 0.545, 2 misses 0.442, 3 misses 0.338, 4 misses 0.234, each before F/D/E/slip. Any block miss also fails the seven co-flip slots: S-H1, S-G1, S-G2 (5 each), S-DEC, S-BRIAN, S-ST1, S-ST2 (3 each), 27 weight. The flip table shows all 15 miss sets give an RPG lead.
- **Patterns.** Distinct block-miss sets always differ on at least 2 slots (Ka and Kb), so each set is its own pattern. F/D/E and slips differ by one slot and chain within a set.

## 2. Current per-block find odds (rev5 as built)
| Block | Point | Range | Evidence |
|---|---|---|---|
| K1 Claire mail | .55 | .45-.65 | [V] Julia's mailbox has no base mail after Sep 17, so 18 seeded mails sit on one page. [V] The subject is `a small thing from Friday` and the snippet ends "...on my mind about Fri". Ticket titles and the calendar event name Claire and Friday; `from:claire` returns the form and K1. Scenario and design review say about .50. The unpointed-mail miss of 57 % comes from mailboxes of 100-500 mails, so here it is lower [J] |
| K3 rc_27 inline on #476 | .45 | .35-.60 | Inline review comments are missed 21/30 overall but 3/12 on Julia tasks. Design review says .50-.60, signature-sim reviewer .38. The gate Doc points only at "his Vision Bot PR". The comments read spills (about 285K chars). The ZOM-567 decoy is strong |
| K4 Brian's Turkish DM | .50 | .40-.60 | Route Hunt .45 surfaced. [V] "Kadıköy ekibi" is the only non-English Relation in 60 Docs, and Julia's question in the DM repeats it verbatim, so one search returns both lines. DM page 1 |
| K5 Leonard's reply on 1943 | .70 | .60-.80 | [V] `0.3.127 (1943)` is the only id whose code is not the version patch (22 × `(127)`, 19 × `(40)`, 9 × `(38)`). [V] Base Slack **text** holds "1943" in only 3 messages, so a "1943" search puts K5 at rank 1. [V] The root `C090N54TG79/1758581651.167799` is Julia's "kick of joy" thread on players' stars (rc 15). Runs reading audience context open it. #builds is a second path. Slack thread-reply carriers were missed 4/18, about 78 % found. Review M4 and the signature sim say .75 |

The current profile (.55, .45, .50, .70) simulates as follows [S, 30 000 trials]. E[avg] is 0.462 at rho 0 and 0.523 at rho 0.6, mid 0.493. P(all gates, < 45 %) is 0.51 at rho 0 and 0.54 at rho 0.6. K5 sits outside the requested 0.35-0.65 band.

## 3. Profile search
Grid: each block at 0.35-0.65 in steps of 0.05, 210 multisets (blocks are symmetric on this surface), 4 000 trials each, rho 0 and 0.6. Output: `plan/spread/grid.json`, `grid.txt`.

| Result [S] | Value |
|---|---|
| P(all, < 45 %) over the band | 0.35-0.56 at rho 0; 0.46-0.56 at rho 0.6 |
| P(all) for profiles with mid E[avg] 0.45-0.50 (93 profiles) | about 0.50-0.55 at both rho |
| Binding gate | SD. Rho 0: about 47-50 % of trials are **under** 0.10 (median SD 0.100-0.115). Rho 0.6: 34-38 % are **over** 0.30 (median 0.28) |
| P(largest pattern < 45 %) | 0.94-0.96 at rho 0; 0.86-0.87 at rho 0.6. It holds with K3 at 0.30 (0.94 / 0.85) |
| P(< 5 full passes) | >= 0.999 everywhere; expected full passes 0.15-0.40 at rho 0, 1.0-1.6 at rho 0.6 |
| P(avg < 0.85) | 1.00; the p90 average never passes 0.78 |

Reading [J]. Inside the band the profile barely matters: P(all) tracks E[avg] and rho, not which block is easy. Findability changes can centre the blocks and set the average. They cannot lift P(all) much above 0.55, because the 27-weight co-flip packs every run with a miss onto rungs 0.10 apart. With independent runs SD then clears 0.10 only when some run misses nothing. With correlated runs it overshoots 0.30 when one run finds everything.

**27-weight co-flip through the rubric** (surface unchanged) [S]:
| Rubric variant at profile (.50, .50, .50, .60) | E[avg] rho 0 / 0.6 | P(SD) | P(all, < 45 %) |
|---|---|---|---|
| One row per slot (as the surface is) | 0.447 / 0.510 | 0.51 / 0.59 | 0.50 / 0.53 |
| S-ST1 written as four per-block Canceled rows | 0.465 / 0.520 | 0.58 / 0.61 | 0.57 / 0.56 |
| S-ST1 and S-ST2 per block (6 of the 27 weight block-local) | 0.482 / 0.531 | 0.65 / 0.63 | 0.63 / 0.57 |
| The same, with blocks at (.45, .45, .45, .55) | 0.451 / 0.495 | 0.63 / 0.66 | 0.61 / 0.60 |

So yes, spreading through the rubric helps, by about +0.07 to +0.13 P(all) at rho 0 and +0.03 to +0.04 at rho 0.6. It works because a single miss then costs less than the next miss, which widens the rungs. It also raises E[avg] by about 0.02-0.035. **Recommendation for the rubric plan** (no slot change):
- Grade S-ST1 ("43 tickets move to Canceled") as one row per block's tickets: K1 13, K3 11, K4 9, K5 10, which together are the 43.
- Grade S-ST2 as "exactly the 17 counted tickets are Done".
- Keep S-H1, S-G1, S-G2, S-DEC and S-BRIAN as single rows: they co-flip by nature.
- Check before relying on it: (a) /rubric and `hg.py rubric-lint` must accept several rows bound to one slot, and the surface grader binding must allow it; (b) weights must stay 1/3/5 (four rows of 1 make 4 against the slot's 3); (c) the "overly granular" and duplicate-row checks.
- If adopted, stay at the chosen find profile. The average then reads 0.47-0.53. If the requester wants it back under 0.50, the next lever is K1 or K4 at 0.45.

## 4. Chosen profile
**K1 .50, K3 .50, K4 .50, K5 .60** (targets) [S, 30 000 trials, frozen surface, one row per slot]:

| Measure | rho 0 | rho 0.6 |
|---|---|---|
| E[avg] (10-90 %) | 0.447 (0.37-0.54) | 0.510 (0.35-0.68) |
| P(SD in 0.10-0.30) | 0.51 (low 0.47, high 0.01) | 0.59 (low 0.03, high 0.38) |
| P(largest pattern < 45 %) | 0.96 | 0.87 |
| P(< 5 full passes) | 1.000 | 0.999 |
| P(avg < 0.85) | 1.00 | 1.00 |
| P(all gates, < 45 %) / (<= 50 %) | 0.50 / 0.51 | 0.53 / 0.57 |
| Expected patterns / full passes | 5.4 / 0.17 | 4.4 / 1.10 |

- The mid E[avg] is 0.479, inside 45-50 %.
- With block rates jittered ±0.10 per batch, P(all) is 0.49 / 0.55.
- With other miss rates F/D/E at 0.20/0.05/0.15, E is 0.457 / 0.520; at 0.40/0.15/0.35, E is 0.438 / 0.500.
- Why this one: every block sits in the band and near 0.50. K5 is kept at 0.60, not 0.50, because 0.60 is as far as fair changes reach (section 5). P(all) is level with the best band profiles (0.50-0.55), with the average in the target.
- Compared with the current build, P(all) is unchanged within noise (0.51 / 0.54). The gain is the band, not the gate odds. The gate odds need the rubric step in section 3.

## 5. Per-block changes
All edits go in `plan/data.py` (and, for K5, `plan/data.py`'s root wiring plus the draft manifest's `planned_records`). Then rebuild with `plan/build.py`, `audience_check.py`, `sweep.py` and `parent_check.py`, and re-run the injection chain (`chain_rev5.sh` pattern) as rev6. `plan/spread/text_check.py` checks the new texts: RESULT PASS on the avoid lists, the cross-record words, the no-tester rule and the solver parse phrases.

### K1: neutral subject, fact pushed out of the snippet (.55 to about .50, -0.05; range -0.02 to -0.10 [J])
Records: `julia.lawson@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` (thread `julia.lawson@harmonygames.co/1844592159752803121`, SQL lines 422-424). Claire's sent copy `claire.morgan@harmonygames.co/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>` (thread `…/1844592159753417634`, lines 426-428). Same Message-ID and time 2025-09-29T10:02:47Z.

- Subject: old `a small thing from Friday`, new `quick catch-up`. Change it in `planned_records.k1_mail.subject` (draft manifest), which `emitters.py:222` reads.
- `data.K1_BODY`, opening only:
  - old: "How is the level work going? I keep missing you on Slack, last week was all items for me.\n\nSomething has been on my mind about Friday at my place."
  - new: "Hope the level work is going well. I keep missing you on Slack, last week was all items for me and this week is starting the same way, so mail it is.\n\nOne thing has been on my mind about Friday at my place."
  - The rest of the body is unchanged.
- Generator effects [V, text_check]:
  - snippet old "…Something has been on my mind about Fri", new "Hey Julia, Hope the level work is going well. I keep missing you on Slack, last week was all items for me and this week is starting the same" (no "Fri");
  - size_estimate 557 to 617, recomputed by `mail_copy`;
  - "Friday" moves from character 137 to 197.
- Why [J]:
  - A listing of Julia's 18 recent mails shows the subject and snippet. The old pair says "a small thing" and "about Fri", which invites an opening by any run that is triaging the form mails.
  - The new pair reads as a social note. Runs that open every recent mail, search `from:claire`, or follow ticket titles and the calendar event to Claire still read it. Those are the careful routes and are unchanged.
  - Snippet triage is maybe a fifth of the K1 finds, so about -0.05.
- Fairness kept:
  - Host is the sender and "at my place"; the day "Friday" stays in the body. The fact is not in the subject or the first lines, as Route Hunt asked.
  - The solver phrases "before anyone touched their phone" and "friday at my place" are kept.
  - The K1 avoid list passes.
  - Also update: `gen_dossier.py` lines 163 and 260 (subject text), `ground_probe.py` probe phrase (line 47) and the dossier term table.

### K3: plainer location for the pass caveat (.45 to about .50, +0.05; range +0.02 to +0.10 [J])
Record: gate Doc `f_748d26e760e54651eaa0d8` (`data.GATE_DOC`, "Passes" paragraph).
- old: "What a pass does and doesn't cover gets discussed on his Vision Bot PR."
- new: "What a pass does and doesn't cover gets discussed in the review comments on his Vision Bot PR."
- This is a delegation quote, so it also changes in three places:
  - `data.QUOTE_CHANGES`: the F-LIMIT value becomes the new sentence without the full stop;
  - the final manifest `ask_fragments` F-LIMIT `delegation_quote` (01_Hardness_Manifest.json line 263);
  - a design_delta row.
- Why [J]:
  - Runs that reach #476 but read only conversation comments and reviews miss rc_27. Those calls return the CodeRabbit summary and empty reviews.
  - "review comments" is GitHub's own name for inline comments, so it steers the endpoint choice without stating the answer. This is the "his review notes" shape that gave 3/12 misses on Julia tasks, against 18/18 where the rule did not imply review text.
  - It does not touch the spill or the ZOM-567 decoy, which keep K3 hard.
- Fairness:
  - It answers 01d M4: a plain location, no branch riddle, and it does not say what the comment says.
  - The gate avoid list passes; it does not contain "sit in review".
  - The store clause the solver needs is kept.

### K4: no change (estimate .50 is on target)
Records stay: `D076RBM29JS/1758658884.207315` (row `5e2947d9447f26c28b465f4fd64254d3`, Julia's question) and `D076RBM29JS/1758659012.418207` (row `246d6f4a90620e5dafbb06068f450e46`, Brian's line), Sep 23 20:21-20:23Z.
- **If a pre-check shows K4 is easy** (run found it with a "Kadıköy" search): drop the verbatim nickname from Julia's question. Old "paylaştığın notlara bakıyorum, Kadıköy ekibi kim ya? nereden tanıyorsun onları"; new "paylaştığın notlara bakıyorum, notlardaki ekip kim ya? nereden tanıyorsun onları". One search then returns one line instead of two, about -0.03 [J]. The m7 prompt for Brian's line stays.
- **If K4 is hard:** no fair raise is worth making. The Doc nickname is already the pointer.
- **Do not move the DM position.** Sep 23 is K4's one-record day, the line is page 1 either way, and moving it to Sep 29 changes nothing for search.

### K5: move the reply off the audience thread (.70 to about .62, -0.08; range -0.03 to -0.12 [J])
Record `d7122186e361aa99778c65cb1502759d`, `C090N54TG79/1758819934.612483`, Leonard, Sep 25 17:05:34Z. The ts, row id and day are all unchanged.
- Root:
  - old: `C090N54TG79/1758581651.167799` (row `e6a91393854458ad70331ef478952136`, Julia, "kick of joy", on players' stars). Drop its ROOT_UPDATES entry so it returns to base: rc 15, users 2, latest_reply 1758582083.678989.
  - new: `C090N54TG79/1758564414.759259` (row `609d88bff39b50ce83116b5aae507171`, Vincent, "And also the muting problem when the game is in background. I couldn't repro it as well", Sep 22 18:06Z; base rc 4, users 2, latest 1758564855.603169 [V]). The update becomes rc 5, users 3 (Leonard is new), latest_reply 1758819934.612483.
  - The row has an id, so `slack_parent` emits the sha id, not the RAW_ROOTS subquery.
  - Also change in the draft manifest: `planned_records.K5_reply.root`, `reply_count` 5, `reply_users_count` 3. Change the gen_dossier K5 root strings (lines 164, 262, 326).
- `data.K5_TEXT`:
  - old "on watching people play it: careful with android 1943, the one that's been passed around. it never went through a store, so anyone on it isn't seeing what a player gets"
  - new "for repros like this one, and for anyone watching people play it: careful with android 1943, the one that's been passed around. it never went through a store, so anyone on it isn't seeing what a player gets"
  - "repros" ties it to the new root. It keeps "android 1943" and "never went through a store" for `_k5_builds`, so the truth is unchanged.
- Why [J]:
  - K5 has three routes: a "1943" search (about .45), opening the threads around Julia's own "players' stars" root (about .30), and the #builds job post (about .15).
  - The second route is the one an audience-read run walks by default: Julia's own root, about players' star ratings.
  - Under a muting-bug repro thread (rc 4) that route falls to about .12. The search route and the #builds path are untouched, so the result is about 1-(.55)(.88)(.85) = .59-.62.
- Not changed, on purpose:
  - The id shape `0.3.127 (1943)` stays. It is the fairness join, and the alternatives break base:
    - a store-shaped `0.3.128 (128)` collides with base `Match3D Android Submission - #128` [V];
    - any other number loses the #builds post `C05433XK267/1758575557.575349`;
    - adding build ids to 50 other Docs is a large coherence change for about -0.05.
  - The reply text keeps 1943: removing it would remove the link.
- Coherence:
  - Late replies are rare in this channel but have precedent: 26 of 1442 replies are more than 48 h after their root, Leonard among them [V]. The current placement is already 66 h after its root, so this is no worse.
  - The text names no tester.
  - It is disjoint from F ("device", "build", "technical", "re-run" absent) and from K4.

### Net
Targets: K1 .50, K3 .50, K4 .50, K5 .62. The simulated profile used .60; the difference is inside noise.

## 6. Coherence checks
| Check | Result |
|---|---|
| Truth / audience table | No verdict, rating, device, build or session changes, so `audience_check.py` should reproduce 17 counted, casual 9 at 3.833, RPG 8 at 3.375, and 15 of 15 miss combinations past 0.25 (smallest 0.270, K5) [V: inputs unchanged; re-run required]. The solver phrases are kept (text_check PASS) |
| One record per day | K4 Sep 23, K5 Sep 25 (same ts), F Sep 26 unchanged. `filter_date_on` Sep 22 shows the new root, not the reply. K1 is Gmail, not bound |
| Disjoint vocabulary | `sweep.py` lists for K1, K5 and GATE pass on the new text, as do the cross-record words K5 vs F and K4, and K1 vs F and K5 (text_check). Re-run the collision test on the rebuilt SQL |
| No tester names in deciding records | PASS (text_check) |
| Base coherence | Base roots are updated only through counters. The old root returns to base values. `parent_check.py` must show `K5_reply` pointing at `609d88bf…`. `base_check` needs no new exception |
| Persona reach | Julia is a member of `C090N54TG79`, and the mail and Doc are unchanged in visibility. Re-run `check-sql --load-bearing` |
| Prompt | Unchanged, so there is no hint in the prompt. The prompt does not cite the ask quote that changed, and the ask itself does not carry F-LIMIT |
| Regenerate | Manifest (F-LIMIT quote, K5_reply root, k1_mail subject), dossier tables, forecast note, stored rev6 diff against rev5 |

## 7. What stays uncertain
- Every find rate is judgement. There is no pre-check, and K3, K4 and K5 are untested carriers on this task. The effect sizes in section 5 are ±0.05-wide guesses.
- Correlation between runs decides which way SD fails: too low when runs are independent, too high when they share thoroughness. Neither is measured. With findability alone, P(all) sits near 0.50-0.55 whatever the profile.
- The rubric step in section 3 is the only lever that clearly raises P(all). It depends on /rubric and the surface grader accepting several rows for one slot.
- K3 has a confound and a review risk. The #476 comments spill (about 285K chars) may decide K3 instead of the pointer, which would be CONFOUNDED. "In the review comments" may be read at /prompt 2.7 as a trap hint, though it names a location only.
- K1: Opus may simply open all 18 recent mails, in which case the subject change does nothing (-0 to -0.02).
- K5: Slack search may index thread replies under parents differently. Attachment indexing and non-member reads are still [U] (Route Hunt).
- Patterns are modelled with one row per slot. Real rubric rows that split or merge slots change the symmetric differences, so re-run `spread_mc.py` on the drafted rubric.
- Next step: one Opus pre-check on rev6, read block by block, then refresh these rates before the baseline.
