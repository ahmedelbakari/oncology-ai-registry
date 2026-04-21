#!/usr/bin/env python3
"""Compile v1/entries/*.yaml into v1/data.json.

Lets contributors add entries as individual YAML files rather than hand-editing
the monolithic JSON. The YAML files are source-of-truth; data.json is derived.
Requires: pyyaml (pip install pyyaml).
"""

import json
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "v1" / "entries"
DATA_FILE = ROOT / "v1" / "data.json"


def main():
    yaml_files = sorted(ENTRIES_DIR.glob("*.yaml"))
    yaml_files = [p for p in yaml_files if not p.name.startswith("_")]
    if not yaml_files:
        print("No entries/*.yaml files found. Nothing to build.")
        return

    entries = []
    for p in yaml_files:
        with open(p) as f:
            e = yaml.safe_load(f)
        entries.append(e)

    payload = {
        "schema_version": "0.1",
        "last_updated": date.today().isoformat(),
        "curator": "Ahmed Elbakri",
        "license": "CC BY 4.0",
        "entries": entries,
    }

    with open(DATA_FILE, "w") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"✅ Wrote {DATA_FILE} with {len(entries)} entries.")


if __name__ == "__main__":
    main()
