"""Test helper: give a temporary workspace a saved task date (see hg_universe.py)."""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hg_universe

DATE_FILE = 'Evals/task_inputs/02_Universe_Date.txt'


def routing(root, key='normal'):
    """Routing manifest path of one universe in a temporary workspace (folder created)."""
    path = hg_universe.manifest_path(Path(root), key)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def select(root, key='normal'):
    """Save the task date as hg_store_input.py universe would; return the routing manifest path."""
    root = Path(root)
    raw = (hg_universe.UNIVERSES[key]['date'] + '\n').encode()
    path = root / DATE_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    index_path = root / hg_universe.INDEX
    index = (json.loads(index_path.read_text()) if index_path.exists()
             else {'format_version': 1, 'revision': 0, 'inputs': {}})
    index['revision'] += 1
    index['inputs']['universe'] = {'state': 'saved', 'revision': index['revision'], 'files': [
        {'filename': path.name, 'path': DATE_FILE, 'bytes': len(raw),
         'sha256': hashlib.sha256(raw).hexdigest()}]}
    index_path.write_text(json.dumps(index, indent=2) + '\n')
    return routing(root, key)
