## Finding

**FAIL: there are material counterexamples.** The supplied logs support the narrow historical-reproduction claims, but the shown code can still grade stale tracker content, suppress unreadability, select the wrong issue, and accept delivery to the wrong target.

No tools were used. The results below are **deterministic traces of the supplied code**, not claims of fresh execution. Examples use the supplied `_grade_planted` harness: successful calls, tracker issue `T-1`, and key regex `K-\d{2}`.

## Counterexamples

### 1. Replacing a tracker description leaves the old section authoritative

**Input**
```python
selectors = {
    "old": ["tracker_lists", "owner calls", "K-01"],
    "new": ["tracker_lists", "owner calls", "K-02"],
}
calls = [
    ("linear_update_issue", {
        "id": "T-1",
        "description": "### Owner calls\n- K-01",
    }),
    ("linear_update_issue", {
        "id": "T-1",
        "description": "### Owner calls\n- K-02",
    }),
]
```

**Correct result:** `{"old": False, "new": True}`. The second description replaces the first.

**Code result:** `{"old": True, "new": False}`.

**Code path:** `tracker_text()` appends both descriptions and joins them. `_section_start()` selects the first matching heading, and `_section_body()` stops at the second heading. Consequently, the grader reads the superseded section and ignores its replacement.

This produces both a false pass and a false failure using supported, readable description writes.

---

### 2. A readable earlier update suppresses UNGRADED for an unreadable later replacement

**Input**
```python
selectors = {
    "old": ["tracker_lists", "owner calls", "K-01"],
    "new": ["tracker_lists", "owner calls", "K-02"],
}
calls = [
    ("linear_update_issue", {
        "id": "T-1",
        "description": "### Owner calls\n- K-01",
    }),
    ("linear_update_issue", {
        "id": "T-1",
        "patch": [{
            "op": "replace",
            "path": "/description",
            "value": "### Owner calls\n- K-02",
        }],
    }),
]
```

The second call uses the **same unreadable patch representation planted by `_g1_unreadable_tracker()`**.

**Required result under the stated decoder policy:** both tracker-content slots are `None`, because the decoder cannot read the replacement that determines the final description.

**Code result:** `{"old": True, "new": False}`.

**Code path:**

1. `tracker_text()` retains the first description.
2. It records event `1` as unreadable because the patch has no `text` member.
3. `decode()` computes:
   ```python
   "tracker": bool(unreadable_updates) and not ztext.strip()
   ```
4. Because the *earlier* description is nonempty, the unreadability flag becomes `False`.

The decoded state therefore reports `tracker_events == [1]` while permitting definite grades from stale text.

**Result:** the unreadable-only planted case is protected, but adding an earlier readable update defeats that protection.

---

### 3. Issue selection uses substring matching, allowing another issue to supply the target’s state and content

**Input**
```python
selectors = {
    "S": ["delivery", "tracker_state", "in review"],
    "L": ["tracker_lists", "review findings", "K-01"],
}
calls = [
    ("linear_update_issue", {
        "id": "T-1",
        "state": "Open",
        "description": "No findings recorded.",
    }),
    ("linear_update_issue", {
        "id": "T-10",
        "state": "In Review",
        "description": "### Review findings\n- K-01",
    }),
]
```

**Correct result:** `{"S": False, "L": False}` for `T-1`.

**Code result:** `{"S": True, "L": True}`.

**Code path:** `tracker_updates()` tests:
```python
issue in str(c["input"].get("id") or ...)
```
`"T-1" in "T-10"` is true. Both issues’ updates are selected; `tracker_final_state()` takes `T-10`’s state, and its description supplies the section.

The same problem applies to identifiers such as `ZOM-801` and `ZOM-8010`.

There is also a broader fallback: `return named or ups` selects all updates when no identifier matches, even if the calls explicitly name unrelated issues.

---

### 4. A short prose bullet is mistaken for a bare key list

**Input**
```python
text = "### Owner calls\n- K-01 blocks K-02"
selectors = {
    "one": ["tracker_count", "owner calls", 1],
    "two": ["tracker_count", "owner calls", 2],
}
```

**Correct result under `_row_keys()`’s documented rule:** `{"one": True, "two": False}`. This is a prose bullet about `K-01`, referencing `K-02`, not a bare two-key list.

**Code result:** `{"one": False, "two": True}`.

**Code path:** after removing keys and punctuation, `_row_keys()` obtains residue `"blocks"`. Its length is 6, satisfying:
```python
len(residue) <= 6 * len(keys)  # 6 <= 12
```
Both keys therefore count.

**Result:** the planted long-prose example passes, but a short relationship sentence defeats the distinction. An incorrect exact count can pass.

---

### 5. `tracker_entry` accepts another key’s value, even when the target is explicitly excluded

**Input**
```python
text = (
    "### Value notes\n"
    "- K-02: receipt a1b2c3d4e5f60718 (not K-01)."
)
selectors = {
    "E": [
        "tracker_entry", "value notes", "K-01",
        ["a1b2c3d4e5f60718"],
    ],
}
```

**Correct result:** `{"E": False}`. The entry is for `K-02` and explicitly says it is not for `K-01`.

**Code result:** `{"E": True}`.

**Code path:** `tracker_section_lines()` returns the line. The `tracker_entry` branch requires only:

- the target key somewhere on the line; and
- every value pattern somewhere on the same line.

The word-boundary search finds `K-01` inside the exclusion, and `_entry_match()` finds the exact SHA. Neither check associates the value with the entry’s actual key.

**Result:** SHA-prefix hardening does not prevent cross-key attribution.

---

### 6. Range filtering drops an explicitly listed group member when it duplicates a range endpoint

**Input**
```python
text = "Review (1): K-01; cohort K-01..K-20"
truth = {"K-01": {"groups": ["review"]}}
selectors = {
    "G": ["group_key", "K-01", "review"],
}
```

**Correct result:** `{"G": True}`. `K-01` is explicitly listed as the review member; the remaining text describes the cohort.

**Code result:** `{"G": False}`, with decoded groups `{}`.

**Code path:** `_range_only()` collects:
```text
keys = [K-01, K-01, K-20]
ends = {K-01, K-20}
```
Its `all(k in ends for k in keys)` test returns true. It loses the distinction between an explicit member occurrence and a separate occurrence used as a range endpoint, so `tracker_groups()` skips the entire line.

**Result:** the intro-range false-positive fix introduces a readable-group false negative at this boundary.

---

### 7. Slack and mail delivery checks accept target identifiers mentioned only in message bodies

**Input**
```python
selectors = {
    "E": ["delivery", "email_reply", "m1"],
    "T": ["delivery", "slack_thread", "1771012800.000101"],
}
calls = [
    ("gmail_reply_to_message", {
        "message_id": "m2",
        "body": "m1 is still pending; false.",
    }),
    ("slack_conversations_add_message", {
        "channel_id": "C1",
        "thread_ts": "1771012800.999999",
        "payload": "Reference target: 1771012800.000101",
    }),
]
```

**Correct result:** `{"E": False, "T": False}`. The actual mail target is `m2`; the actual Slack thread is different.

**Code result:** `{"E": True, "T": True}`.

**Code paths:**
```python
# email_reply
args[0] in texts["email"] and "false" in texts["email"].lower()

# slack_thread
args[0] in texts["slack"]
```

Both checks search serialized call inputs rather than binding the expected identifier to its delivery parameter. For mail, even the required `"false"` can come from body text.

**Result:** the alias fix correctly includes the Slack call, but the resulting delivery grade is wrong. This is target leakage, not a JSON-escaping issue.

---

### 8. `register_parent` checks the last shared file, not necessarily the register

Use `register=True` with the supplied planted register specification.

**Input**
```python
selectors = {
    "P": ["delivery", "register_parent", "folder-good"],
}
calls = [
    ("gdrive_create_file", {
        "name": "register.csv",
        "content": "key,class\nK-01,HOLD\n",
        "parentId": "folder-wrong",
    }, {"id": "f1"}),

    ("gdrive_create_file", {
        "name": "notes.txt",
        "content": "Unrelated notes",
        "parentId": "folder-good",
    }, {"id": "f2"}),

    ("gdrive_share_file", {"fileId": "f1", "role": "reader"}),
    ("gdrive_share_file", {"fileId": "f2", "role": "reader"}),
]
```

**Correct result:** `{"P": False}`. The register is `f1`, in `folder-wrong`.

**Code result:** `{"P": True}`.

**Code path:** `decode()` sets `reg` to the `fileId` of each share call in turn, leaving `d["link"] == "f2"`. `register_parent` then calls `_register_parent(..., "f2")`, which correctly finds the unrelated notes file in `folder-good`.

The faulty assumption is upstream: **“last shared file” is treated as “shared register.”** The same misidentification can also make a `link` selector accept a link to the wrong deliverable.

## Gate checks

### What the supplied evidence does support

For `None` cells that actually reach `gates()`:

- The code constructs explicit all-failed and all-passed fills instead of applying `bool(None)`.
- Average and full-pass verdicts require agreement between those bounds.
- SD and failure patterns enumerate every completion through 12 unknown cells.
- Above 12, those nonmonotone gates return `INCOMPLETE`.
- The planted six-unknown matrix asserts 64 completions, average bounds of 40–60%, and SD `INCOMPLETE`. The supplied control/falsification output supports that planted test’s sensitivity.

I found no material counterexample to that completion loop itself from the shown code. The underlying `difficulty_stats` implementation is not supplied, so its thresholds cannot independently be rederived here.

### End-to-end uncertainty handling still fails

Counterexample 2 prevents the unknowns from reaching that loop.

Take the supplied `_g1_ungraded_gates()` matrix and source each run’s weight-3 `B` slot from counterexample 2’s stale-content check:

- Required decoding: `B=None`; the supplied test establishes that SD must be `INCOMPLETE` across 64 completions.
- Actual decoding: `B=True`; all six unknowns disappear.
- `gates()` takes its no-unknown branch, lists no UNGRADED cells, and returns a definite SD verdict for six identical 60% scores instead of the required uncertainty verdict.

Thus correct enumeration does not rescue the decoder’s suppression of unreadability.

## Do the raw outputs support the stated historical claims?

| Claim | Assessment from supplied artifacts |
|---|---|
| Revision 13 reproduces with zero differences | **Supported at the supplied-log level.** `rev13_c10_final.txt` explicitly reports `reference comparison (proxy_scores.json): 0 difference(s)`. |
| Revision-14 failed-slot sets match the grades of record | **Supported.** All five printed sets match the README, including expanding r2’s `S38–S46`. The printed scores also match. |
| Each undone fix fails its planted case | **Supported at the supplied-log level.** The control reports 11 planted cases plus 12 format fixtures passing; all eight decoder undos and the three unreadable/gate undos show their designated assertion failing. |

The revision-14 comparison is exact:

| Run | Score | Failed slots |
|---|---:|---|
| pre | 90.2% | S04, S05, S07, S08, S40 |
| r1 | 92.2% | S43, S46, S47, S52 |
| r2 | 76.1% | S04, S05, S07, S08, S38–S46 |
| r3 | 91.8% | S01, S47, S49, S52, S54 |
| r6 | 99.6% | S01 |

The fixture rebuild reports zero differences, and the E2E log repeats these reference sets. Those are useful compatibility checks. The revision-14 V3 refusal with four non-precheck rollouts is also appropriate, not a gate defect.

However, these results establish reproduction of the frozen cases—not soundness on the additional inputs above. In particular, unreadable-only and single-description fixtures do not exercise mixed readable/unreadable histories or replacement semantics.

**The FAIL is based on concrete wrong slot results and an end-to-end uncertainty failure, not on disputing the logged backtest matches.**

VERDICT: FAIL