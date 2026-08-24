#!/usr/bin/env python3
"""Deterministic Stage 8 source reconstruction from the protected Session 3 seed."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path


UPGRADE_DIR = Path(__file__).resolve().parent.parent
WORKSPACE_DIR = UPGRADE_DIR.parent.parent
BASELINE_MASTER = (
    WORKSPACE_DIR
    / "versions"
    / "v7.4.0-baseline"
    / "canonical"
    / "master"
    / "PITBULL_Master_Stage7_4_EdgeBoard_Final_Session3.pine"
)
MODULE_DIR = UPGRADE_DIR / "src" / "modules"
WORKING_MASTER = UPGRADE_DIR / "src" / "master" / "PITBULL_Master_Working.pine"
MODULE_MANIFEST = UPGRADE_DIR / "BASELINE_MODULE_MANIFEST.json"
BUILD_MANIFEST = UPGRADE_DIR / "BUILD_MANIFEST.json"
SEED_MANIFEST = UPGRADE_DIR / "SEED_MANIFEST.sha256"
LIBRARY_DIR = UPGRADE_DIR / "src" / "libraries"

EXPECTED_MASTER_BYTES = 213_473
EXPECTED_MASTER_LINES = 5_243
EXPECTED_MASTER_SHA256 = "58ebabed2cc5b065a4b8b8bcb88eee3d7d81de5248f8bdb334c8683b97d77094"
EXPECTED_SEED_MANIFEST_SHA256 = "487bf16e0805775573e0b36b0c96834ab33672d6cb07b150a1a9f32cff070a6c"

# Offsets are zero-based, half-open byte ranges in the protected Session 3 file.
MODULES = (
    ("00_HEADER_PANEL.pine.part", 1, 199, 0, 10_745, "26802074e76d8248e69d5de63e887a51ab91399e663dfbc4f1a76ac9b69932c3"),
    ("01_FOUNDATION_POOL.pine.part", 200, 820, 10_745, 34_782, "444b9b1a1611c5064cd1b90cf5ab505cee93148e5e2dbb09cc3f2ec8d6502646"),
    ("02_ENGINES_ARTIFACT_POOL.pine.part", 821, 1_259, 34_782, 51_768, "8da60eab06a1244893a00545a0d57968d5d7d2f0e39619f3cf9c0b05c4d9be19"),
    ("03_EXECUTION_POSITION_SERVICE.pine.part", 1_260, 1_665, 51_768, 61_862, "298fe4dfa1e59604bc80094df6dcfc58a25bc20af406f01cb5aa352934cbf762"),
    ("04A_RENDER_REGISTRY.pine.part", 1_666, 2_162, 61_862, 80_353, "0f9230cf7db1dc871e27466d7ab308ed420c58f1aa8f06527611fef9ab28e160"),
    ("04B_FVG_TRANSPORT.pine.part", 2_163, 2_392, 80_353, 91_454, "7db45c3d519a1b842265b983dd82a152b6703aa47ccf24342f7dbd76ebf39089"),
    ("04C_REMOTE_PRIMITIVES.pine.part", 2_393, 2_564, 91_454, 96_865, "99f34159de0ed40e536ab46b6625e924dc3c98c0b0883d63ba75b0172d7f7409"),
    ("05A_WEDGE_CEMENT_FIB.pine.part", 2_565, 2_900, 96_865, 110_703, "549939ad8c67d51b10be0da2d0411cb0064f05771a793b3041f5318c616ed05a"),
    ("05B_FORK_WAVE_TIME.pine.part", 2_901, 3_430, 110_703, 135_111, "9130905831f294e07e8a784362d54a4e96b5bfbc4ff59ab9360448a3daa51425"),
    ("05C_SIGNAL_WAVE_RECOVERY.pine.part", 3_431, 3_773, 135_111, 151_585, "7b551b0480a779f7c716ba3199773f845e69520a10a6a13996d73603f5dfcf64"),
    ("05D_FIELD_ORBIT_ANGLE.pine.part", 3_774, 4_116, 151_585, 167_996, "74980de1fa7e1fb4a8a6a3b1f7880596ae4f1c8f53381169974ae3520d6eb01f"),
... (truncated for brevity)