#!/bin/zsh
# Serve logs/verify/ on 127.0.0.1:48713 (read-only HTTP), so the Code Mode `verify` calls can fetch the bundles.
# Run from the workspace root through detach.py; kill the printed PID when the verification is done.
exec python3 -B -m http.server 48713 --bind 127.0.0.1 --directory Task_Authoring/support/fix_session_2026-10-25/logs/verify
