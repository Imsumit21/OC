#!/usr/bin/env python3
"""Run the generators test suite: python3 -B Task_Authoring/generators/tests/run_tests.py [-k PATTERN] [-v]"""
import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.pycache_prefix = "/dev/null/generators-no-bytecode"     # context.NO_BYTECODE: no __pycache__ is read or written
HERE = os.path.dirname(os.path.abspath(__file__))
TA = os.path.dirname(os.path.dirname(HERE))          # Task_Authoring/
sys.path.insert(0, TA)

if __name__ == "__main__":
    argv = [sys.argv[0], "discover", "-s", HERE, "-t", TA, "-p", "test_*.py"] + sys.argv[1:]
    unittest.main(module=None, argv=argv)
