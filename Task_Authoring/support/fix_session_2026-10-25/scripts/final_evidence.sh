#!/bin/zsh
# Re-run the P1 acceptance commands on the final code (read-only on the frozen copies; outputs in the session logs),
# with shared-cache fingerprints around them (run from the workspace root, through detach.py).
D=Task_Authoring/support/fix_session_2026-10-25; L=$D/logs; FP=$D/scripts/fingerprint.py
S=Task_Authoring/support/backtests/season_pass; W=$S/rev13/working_files; F=Task_Authoring/support/fixtures/season_pass_rev13
R12=$W/injection_fix_20261024/before/01_Universe_Inject.sql; R=$S/rev14
python3 -B $FP $L/fp_evidence_before.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
echo "== G1 rev13 c10 (truth.json)"
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $F --truth $W/hardening_rev12/truth.after.json --compare $S/rev13/reference/proxy_scores.json --out $L/g1/rev13_surface_grades.final.json > $L/g1/rev13_c10_final.txt 2>&1; echo "exit=$?"
grep "V3 (hard)\|reference comparison" $L/g1/rev13_c10_final.txt | cut -c1-200
echo "== G1 rev13 c10 (solver)"
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $F --solver $S/solver/solver.py --sql $F/01_Universe_Inject.sql --compare $S/rev13/reference/proxy_scores.json --out $L/g1/rev13_surface_grades.solver.final.json > $L/g1/rev13_c10_solver_final.txt 2>&1; echo "exit=$?"
grep "reference comparison" $L/g1/rev13_c10_solver_final.txt
echo "== G1 rev14 grades"
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $R --surface $R/working_files/01_Gradable_Surface.json --oracle-dir $R/working_files/hardening_rev14 --sql $R/sql/01_Universe_Inject.sql --views both --run pre=$R/runs/06_PreCheck_Trajectory/trajectory-run-1.json --run r1=$R/runs/07_Baseline_Trajectories/trajectory-run-1.json --run r2=$R/runs/07_Baseline_Trajectories/trajectory-run-2.json --run r3=$R/runs/07_Baseline_Trajectories/trajectory-run-3.json --run r6=$R/runs/07_Baseline_Trajectories/trajectory-run-6.json --out $L/g1/rev14_surface_grades.final.json > $L/g1/rev14_grades_final.txt 2>&1; echo "exit=$?"
grep "^  \(pre\|r[0-9]\):" $L/g1/rev14_grades_final.txt | cut -c1-140
echo "== V1 acceptance"
python3 -B $D/scripts/v1_acceptance.py > $L/v1_acceptance_final.txt 2>&1; echo "exit=$?"; tail -1 $L/v1_acceptance_final.txt
echo "== H1 rev13 c05"
python3 -B Task_Authoring/tools/node_verdicts.py --task-dir $F --solver $S/solver/solver.py --sql rev13=$F/01_Universe_Inject.sql --sql rev13-comment-free=$F/Working_Files/01_Universe_Inject.comment-free.sql --sql rev12=$R12 --sql rev11=$W/hardening_rev12/before/01_Universe_Inject.sql --sql rev10=$W/hardening_rev11/before/01_Universe_Inject.sql --task season_pass --reference $S/rev13/reference/attribution.json --seed-ledger Task_Authoring/support/hardness_ledger/ledger.jsonl --legacy-flags validation,receipt,review,fixture_binding,journal,acceptance,epoch_binding,history --expected-model claude-opus-4-8 --ledger-out $L/h1/rev13_proposals.final.jsonl --out $L/h1/rev13_node_verdicts.final.json > $L/h1/c05_h1_final.txt 2>&1; echo "exit=$? (1 = landed-key differences, by design)"
grep -A3 "reference comparison" $L/h1/c05_h1_final.txt | cut -c1-200
date '+end %H:%M:%S'
python3 -B $FP $L/fp_evidence_after.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_evidence_before.tsv $L/fp_evidence_after.tsv
for r in rev13 rev14; do (cd $S/$r && shasum -a 256 -c SHA256SUMS --quiet && echo "$r SHA256SUMS ok"); done
echo DONE
