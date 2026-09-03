#!/usr/bin/env python3
"""Advance the persistent PITBULL build serial after a successful build."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SERIAL_FILE = ROOT / "BUILD_SERIAL.json"
HISTORY_FILE = ROOT / "BUILD_HISTORY.jsonl"
HEADER_FILE = ROOT / "src" / "modules" / "00_HEADER_PANEL.pine.part"
VERSION = "8.0.0-development"


def main() -> None:
    serial = 0
    if SERIAL_FILE.is_file():
        try:
            serial = int(json.loads(SERIAL_FILE.read_text(encoding="utf-8")).get("serial", 0))
        except (ValueError, TypeError, json.JSONDecodeError):
            raise SystemExit(f"invalid build serial: {SERIAL_FILE}")
    serial += 1
    stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    record = {"serial": serial, "version": VERSION, "built_at_utc": stamp}
    SERIAL_FILE.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    header = HEADER_FILE.read_text(encoding="utf-8")
    lines = header.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if 'title="PITBULL ' in line:
            prefix = line.split('title="', 1)[0]
            suffix = line.split('",', 1)[1]
            lines[index] = f'{prefix}title="PITBULL v.HA.01 | Build {serial} | v{VERSION}",{suffix}'
            break
    else:
        raise SystemExit(f"strategy title marker not found: {HEADER_FILE}")
    HEADER_FILE.write_text("".join(lines), encoding="utf-8")
    with HISTORY_FILE.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, separators=(",", ":")) + "\n")
    print(f"BUILD SERIAL: {serial} • v{VERSION} • {stamp}")


if __name__ == "__main__":
    main()