#!/usr/bin/env python3
"""Create and verify a complete, deterministic PITBULL project inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "PROJECT_MANIFEST.json"
EXCLUDED_PARTS = {".git", ".venv", "__pycache__"}
EXCLUDED_NAMES = {".DS_Store", OUTPUT.name, "BUILD_SERIAL.json", "BUILD_HISTORY.jsonl"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def included_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if path.name in EXCLUDED_NAMES or any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def record(path: Path) -> dict[str, object]:
    relative = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    category = relative.split("/", 1)[0]
    item: dict[str, object] = {
        "file": relative,
        "category": category,
        "bytes": len(raw),
        "lines": raw.count(b"\n") if not b"\x00" in raw else None,
        "sha256": digest(path),
    }
    if relative.startswith("src/modules/"):
        item["origin_module"] = relative
    elif relative == "src/master/PITBULL_Master_Working.pine":
        item["origin_modules"] = [
            path.relative_to(ROOT).parent.parent.as_posix() + "/modules/" + module.name
            for module in sorted((ROOT / "src/modules").glob("*.pine.part"))
... (truncated for brevity)