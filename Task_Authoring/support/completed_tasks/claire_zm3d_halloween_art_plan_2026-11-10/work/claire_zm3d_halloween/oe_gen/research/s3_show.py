import sys, json
sys.path.insert(0, ".")
import traj_lib as T
# usage: s3_show.py RUN SEQ[,SEQ] [maxchars]
run = sys.argv[1]; seqs = [int(x) for x in sys.argv[2].split(",")]; m = int(sys.argv[3]) if len(sys.argv) > 3 else 1500
ev, calls = T.load(run)
for s in seqs:
    c = calls[s]
    print(f"--- {run}#{s} {c['raw']} err={c['err']}")
    print("IN:", json.dumps(c["input"], ensure_ascii=False)[:m])
    print("OUT:", (c["out"] or "")[:m])
