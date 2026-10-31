"""Shared paths and helpers for the per-universe universe_kb build (stdlib only, read-only on sources).

One build serves one universe, selected by the activated task context (``universe`` and
``source``). Every data path, the prepared Snowflake index and the storyline metadata come
from that universe; outputs go only to ``source.kb_output_path`` and never to the legacy KB
root at ``references/universe_kb/``.
"""
import json, os, re, datetime, hashlib, sys
from pathlib import Path

BUNDLE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ROOT = os.path.dirname(BUNDLE)  # the workspace root (holds the eval bundle)
sys.path.insert(0, BUNDLE + "/tools")
from task_context import load_context, ContextError

BUILD_ID = "per-universe-v1"

try:
    CONTEXT = load_context(os.environ.get("TASK_AUTHORING_TASK_DIR", BUNDLE + "/task_inputs"), require_source=True)
    SOURCE = CONTEXT["source"]
    UNIVERSE = CONTEXT.get("universe") or {}
    with open(SOURCE["manifest"]) as source_file:
        SOURCE_MANIFEST = json.load(source_file)
    BUILD_PATHS = SOURCE_MANIFEST.get("kb_build_paths") or {}
except (ContextError, OSError, ValueError, KeyError, TypeError) as error:
    raise SystemExit("KB SOURCE BLOCKED: " + str(error))

UNIVERSE_KEY = UNIVERSE.get("key") or SOURCE.get("universe")


def universe_install_hint(universe=None, key=None):
    """Name the universe data folder that has to be installed before a build can run."""
    universe, key = universe or UNIVERSE, key or UNIVERSE_KEY
    folder, prefix = universe.get("folder"), universe.get("prefix")
    if folder and prefix:
        return "install %s/%s_HarmonyGames_* per Evals/UNIVERSE_MAP.md" % (folder, prefix)
    return "install the %s universe data per Evals/UNIVERSE_MAP.md" % key


if not UNIVERSE_KEY:
    raise SystemExit("KB SOURCE BLOCKED: the task context has no universe; run task_context.load_context first")
if SOURCE.get("status") != "ready":
    raise SystemExit("KB SOURCE BLOCKED: %s source is %s (%s); %s"
                     % (UNIVERSE_KEY, SOURCE.get("status") or "missing",
                        SOURCE.get("reason") or "no validated export", universe_install_hint()))

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


def other_services_root(paths):
    """The universe's *_Other_Services folder, derived from its configured service paths."""
    return Path(paths.get("contacts") or paths["slack"]).parent.parent


def universe_snowflake_index(workspace, key):
    """The selected universe's prepared Snowflake index (never a shared/legacy index folder)."""
    return Path(workspace) / "Evals" / "references" / "universes" / key / "search_indexes" / "snowflake-snowflake.json"


SNOW_IDX = source_path(BUILD_PATHS.get("snowflake_index") or universe_snowflake_index(ROOT, UNIVERSE_KEY))
META = source_path(BUILD_PATHS.get("metadata_path") or (other_services_root(PATHS) / "metadata"))
CACHE = BUNDLE + "/support/local_search/cache/kb_cache/" + UNIVERSE_KEY + "/" + SOURCE["fingerprint"][:20]
if not SOURCE.get("kb_output_path"):
    raise SystemExit("KB SOURCE BLOCKED: universe %s has no source.kb_output_path; a per-universe build writes "
                     "only to references/universe_kb/by_universe/%s" % (UNIVERSE_KEY, UNIVERSE_KEY))
OUT = SOURCE["kb_output_path"]
CLOCK_ISO = UNIVERSE.get("clock_utc") or SOURCE.get("data_clock") or CONTEXT["freeze_utc"]
SEED_BOUND_ISO = CONTEXT["freeze_utc"]
CLOCK = datetime.datetime.fromisoformat(CLOCK_ISO.replace("Z", "+00:00"))
CLOCK_TS = CLOCK.timestamp()
LEGACY_KB = os.path.join(BUNDLE, "references", "universe_kb")

if Path(LEGACY_KB).resolve().is_relative_to(Path(OUT).resolve()):
    raise SystemExit("KB SOURCE BLOCKED: refusing to write the %s build into the legacy KB root; "
                     "source.kb_output_path must be references/universe_kb/by_universe/%s"
                     % (UNIVERSE_KEY, UNIVERSE_KEY))
if any(Path(OUT).resolve().is_relative_to(Path(path).resolve()) for path in PATHS.values()):
    raise SystemExit("KB SOURCE BLOCKED: kb_output_path must not be inside any read-only service export")
# Checked as written and as resolved, so a link named by_universe/<key> cannot lead into another folder.
if any(path.name != UNIVERSE_KEY or path.parent.name != "by_universe" for path in (Path(OUT), Path(OUT).resolve())):
    raise SystemExit("KB SOURCE BLOCKED: kb_output_path %s is not a by_universe/%s folder; a build writes only its own "
                     "universe's references/universe_kb/by_universe/%s" % (OUT, UNIVERSE_KEY, UNIVERSE_KEY))
if not os.path.isdir(META) or not os.path.isfile(SNOW_IDX):
    raise SystemExit("KB SOURCE BLOCKED: %s metadata or Snowflake index missing (%s, %s); %s"
                     % (UNIVERSE_KEY, META, SNOW_IDX, universe_install_hint()))
os.makedirs(CACHE, exist_ok=True)
os.makedirs(OUT, exist_ok=True)


def shutdown_rules_apply():
    """True only for a universe whose February-2026 shutdown rules apply (the normal universe)."""
    return bool(UNIVERSE.get("shutdown_rules_apply"))


def hand_written_allowed():
    """True only on the normal universe: hand-written KB knowledge (Scenario_Atlas rows, hand-picked example ids,
    static narrative titles) was written from its Feb 14, 2026 data. On another universe an id can exist while its
    content or version differs, so none of it is carried over."""
    return UNIVERSE_KEY == "normal"


def hand_written(refs):
    """Example ids hand-picked in this builder from the Feb 14 data: kept only where hand_written_allowed()."""
    return list(refs) if hand_written_allowed() else []


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
    """Read a JSON artifact of this build. Never falls back to another universe's KB."""
    with open(p) as f:
        return json.load(f)


def build_stamp():
    """The fields a KB file is bound by (task_context._kb_binding compares the same ones)."""
    return {"universe": UNIVERSE_KEY, "clock": CLOCK_ISO, "seed_bound": SEED_BOUND_ISO,
            "source_fingerprint": SOURCE["fingerprint"], "build": BUILD_ID}


def jload_kb(name):
    """Read a KB file this build depends on (entities.json from entity.py, or an earlier step's output) and refuse one
    stamped for another universe, clock, seed bound, source or build instead of carrying it into new outputs."""
    data = jload(os.path.join(OUT, name))
    meta = (data.get("_meta") if isinstance(data, dict) else None) or {}
    stale = sorted(k for k, v in build_stamp().items() if meta.get(k) != v)
    if stale:
        raise SystemExit("KB SOURCE BLOCKED: %s in %s does not carry this build's %s; rebuild it in this task context "
                         "(entity.py build, then run_all.py)" % (name, OUT, ", ".join(stale)))
    return data


def jload_cache(name):
    """Read a kb_cache intermediate and refuse it unless its sidecar (written by jdump) carries this build's stamp,
    so a partial rebuild never mixes caches of another universe, source or builder version into new outputs."""
    path = os.path.join(CACHE, name)
    try:
        meta = jload(path + ".meta.json").get("_meta") or {}
    except (OSError, ValueError, AttributeError):
        meta = {}
    stale = sorted(k for k, v in build_stamp().items() if meta.get(k) != v)
    if stale:
        raise SystemExit("KB SOURCE BLOCKED: kb_cache/%s does not carry this build's %s; run run_all.py without a "
                         "step list to rebuild the caches" % (name, ", ".join(stale)))
    return jload(path)


def jdump(obj, p, indent=None):
    p = str(p)
    manifest = SOURCE["manifest"]
    workspace = os.path.dirname(BUNDLE)
    if os.path.isabs(manifest) and os.path.commonpath([workspace, manifest]) == workspace:
        manifest = os.path.relpath(manifest, workspace)       # no machine-specific path in a committed KB file
    # No context hash: it covers machine paths and the KB status.
    metadata = {**build_stamp(), "source_manifest": manifest}
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
    """A record dated before the universe data horizon (the KB clock)."""
    when = iso_to_dt(value)
    return when is not None and when < CLOCK


def within_horizon(value):
    """Evidence at or before the selected universe's data horizon can support a listed fact."""
    when = iso_to_dt(value)
    return when is not None and when <= CLOCK


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
