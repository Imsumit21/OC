The supplied revision-13 comparisons report zero differences, including the solver-based reproduction. Revision-14 failed-slot sets and scores match the stated records. The falsification output reports that all eight targeted decoder reversions fail their planted tests. Those results do not cover the following blocking defects.

## Major

### 1. Declared UNGRADED slots are excluded from gate bounds and completions

**File:** `tools/surface_grader.py:595–599,714–729`  
**Hunks:** `gates()` (`@@ -332,46 +572,139 @@`), `grade_runs()` (`@@ -379,25 +712,37 @@`)

`graded` excludes every slot marked `"gradable": false` before constructing either the rubric matrix or `cells`. Consequently, these UNGRADED cells are neither bounded nor enumerated, and are absent from the gate report’s `ungraded_cells`.

This violates the decision’s treatment of **every UNGRADED cell**. For example, six runs passing all known slots but having one declared-ungradable slot each are evaluated as six definite full passes. Their actual full-pass bounds can range from zero to six.

`grade_runs()` similarly excludes these cells from its `ungraded` variable, so they do not trigger score bounds.

**Fix:** Retain all rubric slots in the gate matrix and treat every completed-run `None` as an unknown completion variable, regardless of why it is UNGRADED. Keep coverage metadata separate from gate denominators. Add a planted `gradable:false` case whose full-pass bounds disagree.

### 2. Partially unreadable tracker content still produces definite grades, including false

**File:** `tools/surface_grader.py:325–328,419,456–457,477–481`  
**Hunks:** `tracker_text()`, `decode()`, `delivery()`, and the UNGRADED guard in `grade()`

There are three uncovered paths:

- `decode()` marks the tracker unreadable only when there are unreadable updates **and no readable text whatsoever**. An earlier readable description therefore masks a later unreadable replacement.
- A patch list containing an append with `text` and a replacement using `value` is not marked unreadable, because `got` is nonempty.
- The UNGRADED guard excludes the content-dependent `tracker_preserves` delivery check. An unreadable `replace /description` patch makes `tracker_preserved()` return `False`, even when its unhandled `value` preserves the original text.

For example, a readable description followed by the same replacement-patch shape used in `_g1_unreadable_tracker()` leaves the old text available and the unreadable flag false. A selector for content introduced by the replacement then returns `False`, not UNGRADED.

**Fix:** Track unsupported content mutations individually, including partially decoded patch lists. Propagate uncertainty to all dependent selectors, including preservation, unless a later fully decoded replacement establishes the final content. Add planted mixed-readable/unreadable, partially decoded-list, and unreadable-preservation cases.

### 3. A readable earlier register masks an unreadable delivered register

**Files:**  
- `tools/trajectory_ledger.py:657–661`  
- `tools/surface_grader.py:417–418`

**Hunks:** `table()` (`@@ -614,7 +654,10 @@`), `decode()` (`@@ -162,47 +346,101 @@`)

The CSV-error path records an unreadable candidate and continues, leaving any previously decoded rows available. `decode()` then requires `not t["rows"]` before declaring the table unreadable.

Thus, a readable register followed by an unreadable register write can receive definite grades from stale rows. A concrete case is two matching register creations: the first readable, the second exceeding the CSV field limit and subsequently shared. The second candidate is unreadable, but the first supplies rows, suppressing UNGRADED.

The error candidate also omits file identity, making it harder to associate the unreadable write with the delivered register.

**Fix:** Preserve candidate identity and determine uncertainty from the selected/delivered register’s applicable writes, rather than whether any readable rows exist elsewhere. Add a planted readable-then-unreadable delivered-register case.

### 4. Tracker descriptions are concatenated instead of applying replacements

**File:** `tools/surface_grader.py:314–336`  
**Hunk:** `tracker_text()` within `@@ -131,24 +180,159 @@`

Every full `description` is appended to `texts`. A later description replacement therefore leaves obsolete content in the decoded tracker.

For two successful updates:

```text
description 1: ### Owner calls
               - K-01

description 2: ### Owner calls
               - K-02
```

the decoded tracker contains both sections. `_section_start()` selects the first heading, so `tracker_lists(..., "K-01")` passes and `tracker_lists(..., "K-02")` fails—the reverse of the final delivered description.

Reading every update requires replaying its mutation semantics, not concatenating historical snapshots.

**Fix:** Maintain an effective tracker description: full descriptions and description replacements overwrite it; append/prepend operations modify it in order. Keep history separately if preservation needs it. Plant consecutive full replacements and append-then-replace cases.

### 5. Short prose bullets are misclassified as bare key lists

**File:** `tools/surface_grader.py:232–235`  
**Hunk:** `_row_keys()` within `@@ -131,24 +180,159 @@`

The residual-length heuristic accepts arbitrary prose when:

```python
len(residue) <= 6 * len(keys)
```

For example:

```text
- K-01 depends on K-02
```

leaves `dependson`, whose length is below the two-key threshold. Both keys are counted, although the documented rule says a prose bullet counts only its first key.

This leaves decoder defect 5 incompletely fixed and introduces incorrect exact-count verdicts for short dependency notes. The planted prose example is long enough not to expose it.

**Fix:** Recognize bare key lists with an explicit key/separator/conjunction grammar, rather than a character-count allowance. Otherwise retain only the prose bullet’s first key. Add the short-prose example alongside the existing bare-list test.

### 6. SHA ambiguity checking exempts every hash extending the expected prefix

**File:** `tools/surface_grader.py:265–268`  
**Hunk:** `_entry_match()` within `@@ -131,24 +180,159 @@`

The rival exclusion removes any known hash satisfying:

```python
h.startswith(pat) or pat.startswith(h)
```

If the expected pattern is itself abbreviated, this can remove multiple distinct full hashes.

For example, with `pat = tok = "abcdef0"` and two known full hashes beginning `abcdef01…` and `abcdef02…`, both rivals are excluded because both start with `pat`. `_entry_match()` returns `True` for an ambiguous seven-character prefix.

The existing test uses distinct longer expected values, so it does not exercise this case.

**Fix:** Resolve an abbreviated expected SHA against canonical known hashes first. Do not accept an ambiguous expected prefix, and exempt only the uniquely resolved target hash from written-prefix ambiguity checking. Add a planted abbreviated selector sharing its prefix with two known full hashes.

VERDICT: FAIL