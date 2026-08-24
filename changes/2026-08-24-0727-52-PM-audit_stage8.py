#!/usr/bin/env python3
"""Deterministic static audit for the PITBULL Stage 8 source set."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


UPGRADE = Path(__file__).resolve().parent.parent
WORKSPACE = UPGRADE.parent.parent
MASTER = UPGRADE / "src/master/PITBULL_Master_Working.pine"
LIBRARIES = UPGRADE / "src/libraries"
MODULES = UPGRADE / "src/modules"
BUILD_MANIFEST = UPGRADE / "BUILD_MANIFEST.json"
BASELINE_MANIFEST = UPGRADE / "BASELINE_MODULE_MANIFEST.json"
SOURCE_LOCK = UPGRADE / "SOURCE_LOCK.json"
BASELINE_SOURCE_LOCK = WORKSPACE / "versions/v7.4.0-baseline/SOURCE_LOCK.json"
PROTECTED_MASTER = (
    WORKSPACE
    / "versions/v7.4.0-baseline/canonical/master"
    / "PITBULL_Master_Stage7_4_EdgeBoard_Final_Session3.pine"
)
OUTPUT_JSON = UPGRADE / "tests/static/STATIC_AUDIT.json"
OUTPUT_MD = UPGRADE / "tests/static/STATIC_AUDIT.md"

PLOT_FUNCTIONS = (
    "plot",
    "plotshape",
    "plotchar",
    "plotarrow",
    "plotbar",
    "plotcandle",
    "alertcondition",
    "bgcolor",
    "barcolor",
    "fill",
)
ORDER_FUNCTIONS = (
    "strategy.entry",
    "strategy.exit",
    "strategy.order",
... (truncated for brevity)