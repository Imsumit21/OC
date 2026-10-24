"""Shared paths and helpers for the universe_kb build (stdlib only, read-only on sources)."""
import json, os, re, datetime, hashlib, sys
from pathlib import Path

BUNDLE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ROOT = os.path.dirname(BUNDLE)  # the workspace that holds Evals/ and the HarmonyGames_* folders
sys.path.insert(0, BUNDLE + "/tools")
from task_context import load_context, ContextError

try:
    CONTEXT = load_context(os.environ.get("TASK_AUTHORING_TASK_DIR", BUNDLE + "/task_inputs"), require_source=True)
    SOURCE = CONTEXT["source"]
    with open(SOURCE["manifest"]) as source_file:
        SOURCE_MANIFEST = json.load(source_file)
    BUILD_PATHS = SOURCE_MANIFEST.get("kb_build_paths") or {}
except (ContextError, OSError, ValueError) as error:
    raise SystemExit("KB SOURCE BLOCKED: " + str(error))

PATHS = SOURCE["paths"]
OS = str(Path(PATHS["slack"]).parent)
SLACK, GMAIL = PATHS["slack"], PATHS["gmail"]
GITHUB = PATHS["github"] + "/data.json"
LINEAR, TRELLO, GCAL = (PATHS[service] + "/data.json" for service in ("linear", "trello", "gcal"))
CONF, CONTACTS = PATHS["confluence"] + "/confluence_working.json", PATHS["contacts"] + "/contacts.json"
GDOCS, GSHEETS, GSLIDES, GDRIVE = (PATHS[service] + "/data.json" for service in ("gdocs", "gsheets", "gslides", "gdrive"))
SNOW = PATHS["snowflake"] + "/snowflake.json"

def source_path(value):
    path = Path(value)
    return str(path if path.is_absolute() else Path(ROOT) / path)

SNOW_IDX = source_path(BUILD_PATHS.get("snowflake_index", "Evals/references/search_indexes/snowflake-snowflake.json"))
META = source_path(BUILD_PATHS.get("metadata_path", "HarmonyGames_Other_Services/metadata"))
CACHE = BUNDLE + "/support/local_search/cache/kb_cache/" + CONTEXT["universe_date_key"] + "/" + SOURCE["fingerprint"][:20]
OUT = SOURCE.get("kb_output_path") or SOURCE["kb_path"]
CLOCK_ISO = CONTEXT["freeze_utc"]
CLOCK = datetime.datetime.fromisoformat(CLOCK_ISO.replace("Z", "+00:00"))
CLOCK_TS = CLOCK.timestamp()
if SOURCE.get("mode") == "shared-universe" and SOURCE.get("data_clock") != CLOCK_ISO and not SOURCE.get("kb_output_path"):
    OUT = str(Path(SOURCE["kb_path"]) / "by_date" / CONTEXT["universe_date_key"])

if any(Path(OUT).resolve().is_relative_to(Path(path).resolve()) for path in PATHS.values()):
    raise SystemExit("KB SOURCE BLOCKED: kb_path must not be inside any read-only service export")
if not os.path.isdir(META) or not os.path.isfile(SNOW_IDX):
    raise SystemExit("KB SOURCE BLOCKED: selected metadata_path or snowflake_index does not exist")
os.makedirs(CACHE, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

REDACT_PATTERNS = [
    ("[PERSON_NAME_n]", re.compile(r"\[PERSON_NAME_\d+\]")),
    ("PERSON_n_<FIELD> token", re.compile(r"\bPERSON_\d+_[A-Z_]+\b")),
    ("EMPLOYEE_n_<FIELD> token (in text)", re.compile(r"\bEMPLOYEE_\d+_[A-Z_]+\b")),
    ("SVC_n_<FIELD> token", re.compile(r"\bSVC_\d+_[A-Z_]+\b")),
    ("[SOURCE_ORG_n]", re.compile(r"\[SOURCE_ORG_\d+\]")),
    ("[ORG]", re.compile(r"\[ORG\]")),
    ("[EMAIL_n]", re.compile(r"\[EMAIL_\d+\]")),
    ("[IDENTIFIER_n]", re.compile(r"\[IDENTIFIER_\d+\]")),
    ("[PHONE_n]", re.compile(r"\[PHONE[_A-Z]*_?\d*\]")),
    ("<REDACTED*>", re.compile(r"<REDACTED[A-Z_]*>|\[REDACTED[A-Z_]*\]")),
]

LINEAR_KEY = re.compile(r"\b(ENG|ZOM|ART|DES|EPI)-(\d{1,4})\b")


def jload(p):
    path = Path(p)
    shared_reference = False
    if not path.exists() and SOURCE.get("mode") == "shared-universe" and path.resolve().is_relative_to(Path(OUT).resolve()):
        # Identity/reference dependencies can be read from the existing shared KB
        # while new earlier-date outputs are kept in their separate output folder.
        path = Path(SOURCE["kb_path"]) / path.resolve().relative_to(Path(OUT).resolve())
        shared_reference = True
    with open(path) as f:
        data = json.load(f)
    if shared_reference or (SOURCE.get("mode") == "shared-universe" and path.resolve().is_relative_to(Path(OUT).resolve())):
        from runtime_context import validate_kb
        return validate_kb(data, {"TASK_CONTEXT": CONTEXT})
    return data


def jdump(obj, p, indent=None):
    p = str(p)
    metadata = {"clock": CLOCK_ISO, "source_fingerprint": SOURCE["fingerprint"],
                "source_manifest": SOURCE["manifest"], "context_hash": CONTEXT["context_hash"]}
    if SOURCE.get("mode") == "shared-universe":
        reference_clock = SOURCE.get("data_clock", CLOCK_ISO)
        metadata.update(reference_clock=reference_clock, assigned_freeze=CLOCK_ISO,
                        reference_only=reference_clock != CLOCK_ISO,
                        requires_record_verification=reference_clock != CLOCK_ISO)
    published_mapping = isinstance(obj, dict) and Path(p).resolve().is_relative_to(Path(OUT).resolve())
    if published_mapping:
        obj = dict(obj, _meta={**obj.get("_meta", {}), **metadata})
    tmp = p + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=indent, ensure_ascii=False, sort_keys=False, default=str)
    os.replace(tmp, p)
    if not published_mapping:
        # Cache mappings may be keyed only by real record IDs, and some caches
        # are lists. Keep their existing schemas intact and stamp a sidecar.
        with open(p + ".meta.json", "w") as meta_file:
            json.dump({"_meta": metadata}, meta_file)


def before_clock(value):
    """Only dated evidence before the freeze can support a completed event."""
    when = iso_to_dt(value)
    return when is not None and when < CLOCK


def ts_to_dt(ts):
    return datetime.datetime.fromtimestamp(float(ts), datetime.timezone.utc)


def month_of_ts(ts):
    return ts_to_dt(ts).strftime("%Y-%m")


def iso_to_dt(s):
    if not s:
        return None
    s = str(s).strip()
    try:
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        d = datetime.datetime.fromisoformat(s)
        if d.tzinfo is None:
            d = d.replace(tzinfo=datetime.timezone.utc)
        return d
    except Exception:
        pass
    try:
        from email.utils import parsedate_to_datetime
        d = parsedate_to_datetime(s)
        if d.tzinfo is None:
            d = d.replace(tzinfo=datetime.timezone.utc)
        return d
    except Exception:
        return None


def quantiles(vals, qs=(0.1, 0.25, 0.5, 0.75, 0.9, 0.99)):
    if not vals:
        return {}
    v = sorted(vals)
    n = len(v)
    out = {"n": n, "min": v[0], "max": v[-1], "mean": round(sum(v) / n, 1)}
    for q in qs:
        out["p%d" % int(q * 100)] = v[min(n - 1, int(q * n))]
    return out


def sha32(s):
    return hashlib.sha256(s.encode()).hexdigest()[:32]


def norm_text(s):
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def text_hash(s):
    return hashlib.md5(norm_text(s).encode()).hexdigest()[:12]


def redaction_counts(text, counter, examples=None, rid=None, maxex=5):
    if not text:
        return
    for name, rx in REDACT_PATTERNS:
        m = rx.findall(text)
        if m:
            counter[name] = counter.get(name, 0) + len(m)
            if examples is not None and rid is not None:
                ex = examples.setdefault(name, [])
                if len(ex) < maxex:
                    ex.append(rid)
