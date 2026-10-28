#!/bin/zsh
# Round-4 evidence on the final P1 tree: the same commands as final_evidence.sh, written under logs/final4/.
# Read-only on the frozen copies; the shared-cache fingerprint is taken before and after.
D=Task_Authoring/support/fix_session_2026-10-25; L=$D/logs; O=$L/final4; FP=$D/scripts/fingerprint.py
S=Task_Authoring/support/backtests/season_pass; W=$S/rev13/working_files; F=Task_Authoring/support/fixtures/season_pass_rev13
R12=$W/injection_fix_20261024/before/01_Universe_Inject.sql; R=$S/rev14
mkdir -p $O
python3 -B $FP $L/fp_evidence4_before.tsv --only support/local_search support/hardness_ledger > /dev/null
date '+start %H:%M:%S'
echo "== G1 rev13 c10 (truth.json)"
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $F --truth $W/hardening_rev12/truth.after.json --compare $S/rev13/reference/proxy_scores.json --out $O/rev13_surface_grades.truth.json > $O/rev13_truth.txt 2>&1; echo "exit=$?"
grep "V3 (hard)\|reference comparison" $O/rev13_truth.txt | cut -c1-200
echo "== G1 rev13 c10 (solver)"
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $F --solver $S/solver/solver.py --sql $F/01_Universe_Inject.sql --compare $S/rev13/reference/proxy_scores.json --out $O/rev13_surface_grades.solver.json > $O/rev13_solver.txt 2>&1; echo "exit=$?"
grep "reference comparison" $O/rev13_solver.txt
echo "== G1 rev14 grades"
python3 -B Task_Authoring/tools/surface_grader.py --task-dir $R --surface $R/working_files/01_Gradable_Surface.json --oracle-dir $R/working_files/hardening_rev14 --sql $R/sql/01_Universe_Inject.sql --views both --run pre=$R/runs/06_PreCheck_Trajectory/trajectory-run-1.json --run r1=$R/runs/07_Baseline_Trajectories/trajectory-run-1.json --run r2=$R/runs/07_Baseline_Trajectories/trajectory-run-2.json --run r3=$R/runs/07_Baseline_Trajectories/trajectory-run-3.json --run r6=$R/runs/07_Baseline_Trajectories/trajectory-run-6.json --out $O/rev14_surface_grades.json > $O/rev14_grades.txt 2>&1; echo "exit=$?"
grep "^  \(pre\|r[0-9]\):" $O/rev14_grades.txt | cut -c1-140
echo "== V1 acceptance"
python3 -B $D/scripts/v1_acceptance.py > $O/v1_acceptance.txt 2>&1; echo "exit=$?"; tail -1 $O/v1_acceptance.txt
echo "== H1 rev13 c05"
python3 -B Task_Authoring/tools/node_verdicts.py --task-dir $F --solver $S/solver/solver.py --sql rev13=$F/01_Universe_Inject.sql --sql rev13-comment-free=$F/Working_Files/01_Universe_Inject.comment-free.sql --sql rev12=$R12 --sql rev11=$W/hardening_rev12/before/01_Universe_Inject.sql --sql rev10=$W/hardening_rev11/before/01_Universe_Inject.sql --task season_pass --reference $S/rev13/reference/attribution.json --seed-ledger Task_Authoring/support/hardness_ledger/ledger.jsonl --legacy-flags validation,receipt,review,fixture_binding,journal,acceptance,epoch_binding,history --expected-model claude-opus-4-8 --ledger-out $O/rev13_proposals.jsonl --out $O/rev13_node_verdicts.json > $O/c05.txt 2>&1; echo "exit=$? (1 = landed-key differences, by design)"
grep -A4 "reference comparison" $O/c05.txt | cut -c1-220
echo "== surface format fixtures"
python3 -B Task_Authoring/support/fixtures/surface_formats/build_fixtures.py --check > $O/build_fixtures_check.txt 2>&1; echo "exit=$?"; tail -2 $O/build_fixtures_check.txt
echo "== task 1 surface.gradeable (read-only)"
python3 -B Task_Authoring/tools/gradable_surface.py gradeable-report Task_Authoring/task_inputs/Working_Files/01_Gradable_Surface.json > $O/task1_surface_gradeable.txt 2>&1; echo "exit=$?"
tail -3 $O/task1_surface_gradeable.txt
date '+end %H:%M:%S'
python3 -B $FP $L/fp_evidence4_after.tsv --only support/local_search support/hardness_ledger > /dev/null
python3 -B $FP --diff $L/fp_evidence4_before.tsv $L/fp_evidence4_after.tsv
for r in rev13 rev14; do (cd $S/$r && shasum -a 256 -c SHA256SUMS --quiet && echo "$r SHA256SUMS ok"); done
echo DONE
