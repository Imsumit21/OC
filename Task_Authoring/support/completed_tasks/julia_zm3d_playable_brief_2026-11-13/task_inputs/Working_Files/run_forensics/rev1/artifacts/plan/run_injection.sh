#!/bin/zsh
# Rebuild the injection artifacts in dependency order and capture every tool output the dossier pastes.
# Usage (from anywhere):  zsh Task_Authoring/task_inputs/Working_Files/plan/run_injection.sh [build] [forecast]
#   build     re-render the spec and rebuild 01_Universe_Inject.sql first (only when texts or the model changed)
#   forecast  re-run and pre-register the injection forecast (appends to the ledger: only for a new SQL)
# Nothing is executed against a database. The stage gate is run separately.
set -u
ROOT=/Users/sumitkumar/Source/Outlier/OC
cd $ROOT
export TASK_AUTHORING_TASK_DIR=$ROOT/Task_Authoring/task_inputs
T=Task_Authoring/task_inputs
W=$T/Working_Files
P=$W/plan
O=$P/out
TOOLS=Task_Authoring/tools
SQL=$T/01_Universe_Inject.sql
MAN=$W/01_Hardness_Manifest.json
mkdir -p $O
BUILD=0; FORECAST=0
for a in "$@"; do [[ $a == build ]] && BUILD=1; [[ $a == forecast ]] && FORECAST=1; done

if [[ $BUILD == 1 ]]; then
  python3 -B $P/build_spec.py || { echo "build_spec failed"; exit 1; }
  python3 -B Task_Authoring/generators/render.py render --task-dir $T > $O/render.txt 2>&1; echo "render rc=$? $(grep -m1 -iE 'verdict|PASS|FAIL' $O/render.txt | cut -c1-120)"
  python3 -B $P/build_sql.py || { echo "build_sql failed"; exit 1; }
fi
echo "sql sha256 $(shasum -a 256 $SQL | cut -c1-64)"

# truth, final manifest, surface
python3 -B $TOOLS/oracle_kit.py truth --solver $W/solver/solver.py --sql $SQL --out $W/solver/truth.json 2>&1 | tail -1 | cut -c1-110
python3 -B $P/build_final_manifest.py > $O/_build_final_manifest.log 2>&1 || { echo "build_final_manifest failed"; cat $O/_build_final_manifest.log; exit 1; }
( python3 -B $TOOLS/gradable_surface.py validate --task-dir $T; python3 -B $TOOLS/gradable_surface.py gradeable-report --task-dir $T ) > $O/gradable_surface.txt 2>&1
head -1 $O/gradable_surface.txt | cut -c1-110
# the skeleton is bound to the final manifest's bytes; the budget takes its rows from the skeleton
python3 -B $TOOLS/rubric_skeleton.py build --write --task-dir $T > $O/_skeleton_build.log 2>&1
python3 -B $P/build_budget.py skeleton > $O/_build_budget.log 2>&1 || { echo "build_budget skeleton failed"; cat $O/_build_budget.log; exit 1; }
python3 -B $TOOLS/rubric_skeleton.py build --write --task-dir $T >> $O/_skeleton_build.log 2>&1

# load-bearing ids (seeded evidence, the base records the rules rest on, the scoped containers)
python3 -B - <<'EOF'
import sys
sys.path.insert(0, 'Task_Authoring/task_inputs/Working_Files/plan')
import design_model as M
ids = [v["id"] for k, v in M.SEED.items() if k not in ("ticket_parent", "contact", "trello_note")]
ids += [M.BASE[k] for k in ("vendor_formats", "vendor_asset_list", "vendor_nov3", "vendor_zombie_ask", "brian_zip1", "brian_zip2", "brian_pack3",
                            "brian_winfail", "fred_scenario1", "fred_retention", "vendor_music_rule", "art_bow_root", "art_cactus", "art_cone",
                            "art_claire_pr", "robert_new_colours", "anim_pack", "fred_asks_julia", "julia_level")]
ids += [M.DM_FRED, M.DM_CLAIRE, M.MATCH3D_CH, M.VENDOR_CH, M.BASE["julia_root"], M.BASE["playable_feedback_doc"]]
open('Task_Authoring/task_inputs/Working_Files/01c_load_bearing_ids.txt', 'w').write("\n".join(ids) + "\n")
print("load-bearing ids:", len(ids))
EOF

python3 -B $TOOLS/sql_lint.py $SQL > $O/sql_lint.txt 2>&1;                          echo "sql_lint rc=$? $(grep -E 'errors' $O/sql_lint.txt | head -1 | cut -c1-100)"
python3 -B $TOOLS/base_check.py $SQL > $O/base_check.txt 2>&1;                      echo "base_check rc=$? $(head -1 $O/base_check.txt | cut -c1-100)"
python3 -B $TOOLS/base_claims.py $SQL --task-dir $T > $O/base_claims.txt 2>&1;      echo "base_claims rc=$? $(head -1 $O/base_claims.txt | cut -c1-100)"
python3 -B $TOOLS/hg.py lint > $O/hg_lint.json 2>$O/hg_lint.err;                    echo "hg lint rc=$? $(python3 -c "import json;d=json.load(open('$O/hg_lint.json'));print(d.get('counts'), d.get('sha256','')[:12])")"
python3 -B $TOOLS/persona_view.py check-sql julia_lawson $SQL --load-bearing $W/01c_load_bearing_ids.txt > $O/check_sql.txt 2>&1; echo "check-sql rc=$? $(tail -1 $O/check_sql.txt | cut -c1-100)"
python3 -B $TOOLS/fact_check.py $SQL --manifest $MAN --no-leak > $O/fact_check.txt 2>&1; echo "fact_check rc=$? $(head -1 $O/fact_check.txt | cut -c1-100)"
python3 -B $TOOLS/hardness_gate.py $MAN $SQL > $O/hardness_gate_final.txt 2>&1;     echo "hardness_gate rc=$? $(grep -E 'HARDNESS GATE' $O/hardness_gate_final.txt | tail -1 | cut -c1-100)"
python3 -B $TOOLS/oracle_kit.py check --task-dir $T > $O/oracle_check.txt 2>&1;     echo "oracle rc=$? $(grep -E 'CONTRACT' $O/oracle_check.txt | head -1 | cut -c1-100)"

python3 -B $P/build_dispositions.py > /dev/null
python3 -B $TOOLS/difficulty_mutation.py mutate --task-dir $T > $O/mutation.txt 2>&1;      echo "mutation rc=$?"
python3 -B $TOOLS/difficulty_mutation.py geometry --task-dir $T > $O/geometry.txt 2>&1;    echo "geometry rc=$? $(grep -iE 'U |L_max' $O/geometry.txt | head -2 | tr '\n' ' ' | cut -c1-160)"
python3 -B $TOOLS/trap_liveness.py --task-dir $T > $O/trap_liveness_sql.txt 2>&1;          echo "liveness rc=$?"
if [[ $FORECAST == 1 ]]; then
  python3 -B $TOOLS/hardness_forecast.py forecast --task-dir $T --model claude-opus-5-5 --no-channels --preregister --out $W/01c_Forecast.json > $O/forecast_injection.txt 2>&1
  echo "forecast rc=$? $(grep -E 'ledger' $O/forecast_injection.txt | head -1 | cut -c1-140)"
fi
python3 -B $TOOLS/preflight_report.py --task-dir $T --forecast $W/01c_Forecast.json > $O/preflight.txt 2>&1; echo "preflight rc=$? $(grep -E 'PREFLIGHT' $O/preflight.txt | tail -1 | cut -c1-100)"
python3 -B $TOOLS/path_exposure.py check --task-dir $T --write > $O/path_exposure.txt 2>&1;  echo "path rc=$? $(grep -E 'PATH EXPOSURE' $O/path_exposure.txt | head -1 | cut -c1-100)"
python3 -B $TOOLS/difficulty_budget.py check --task-dir $T > $O/difficulty_budget_check.txt 2>&1; echo "budget rc=$? $(head -1 $O/difficulty_budget_check.txt | cut -c1-100)"
python3 -B $TOOLS/rubric_skeleton.py check --task-dir $T > $O/rubric_skeleton_check.txt 2>&1;     echo "skeleton rc=$? $(head -1 $O/rubric_skeleton_check.txt | cut -c1-100)"
python3 -B $P/check_ids.py > $O/check_ids.txt 2>&1;                                 echo "check_ids rc=$? $(tail -1 $O/check_ids.txt | cut -c1-100)"
python3 -B $P/citation_chronology.py > /dev/null;                                  echo "citation chronology rc=$? $(tail -1 $O/citation_chronology.txt | cut -c1-100)"
python3 -B $TOOLS/coherence_sweep.py candidates --task-dir $T > $O/sweep_candidates.txt 2>&1; echo "sweep candidates rc=$?"
if [[ -f $W/01d_Coherence_Sweep.json ]]; then
  python3 -B $TOOLS/coherence_sweep.py check --task-dir $T > $O/sweep_check.txt 2>&1; echo "sweep check rc=$? $(head -1 $O/sweep_check.txt | cut -c1-100)"
fi
