# Minted ids, collision checks and verified base quotes

Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)
Status: COMPLETE — machine-readable copy in ids_and_quotes.json; per-service request files in tmp_ids/.

- Minting: sha256(seed) prefixes; Trello action ids lead with the unix-seconds hex; Slack message id = sha256(channel|ts)[:32]; Gmail thread ids ≈ unix_ms << 20 (shape-checked against Vincent's threads).
- Collisions: every minted id absent; each lookup has a positive control (gdrive, gsheets, gdocs, gcal event_id + ical_uid, trello, contacts, slack ×3). Gmail: the original key lookup's control was invalid (ids carry angle brackets), so absence was re-proven by literal search over Vincent's thread files with a found control (tmp_ids/gmail_check.txt).
- Maxima: ZOM-566, ART-792, DES-312, match3d #477, match3d-backend #35.
- Verified Confluence quotes (exact substrings of the stored body): see ids_and_quotes.json `verified_base_quotes`.
- #builds posts used by the design: see ids_and_quotes.json `builds_posts`.
