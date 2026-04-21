#!/usr/bin/env python3
"""Validate data.json schema for the OncologyAI Registry.

Runs in CI and pre-push. Returns non-zero on any schema violation.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "v1" / "data.json"

REQUIRED_ENTRY_FIELDS = {"id", "product_name", "company", "cancer_types", "modality", "intended_use", "regulatory", "sources"}
ALLOWED_FDA_STATUS = {
    "Breakthrough Device Designation",
    "De Novo authorized",
    "510(k) cleared",
    "PMA approved",
    "LDT",
    "Research Use",
}
ALLOWED_MODALITIES = {
    "histopathology",
    "radiology_mammography",
    "radiology_ct",
    "radiology_mri",
    "radiology_cxr",
    "genomic_sequencing_with_ai",
    "liquid_biopsy",
    "multiomics",
}


def validate(data):
    errors = []
    seen_ids = set()
    entries = data.get("entries", [])
    if not entries:
        errors.append("No entries in data.json")
        return errors

    for i, e in enumerate(entries):
        ctx = f"entry[{i}] id={e.get('id', '<missing>')}"
        missing = REQUIRED_ENTRY_FIELDS - set(e.keys())
        if missing:
            errors.append(f"{ctx}: missing required fields {sorted(missing)}")
        if e.get("id") in seen_ids:
            errors.append(f"{ctx}: duplicate id")
        seen_ids.add(e.get("id"))

        if e.get("modality") and e["modality"] not in ALLOWED_MODALITIES:
            errors.append(f"{ctx}: unknown modality '{e['modality']}'")

        reg = e.get("regulatory") or {}
        fda = reg.get("fda_status")
        if fda and fda not in ALLOWED_FDA_STATUS:
            errors.append(f"{ctx}: fda_status '{fda}' not in allowed set")

        sources = e.get("sources") or []
        if not sources:
            errors.append(f"{ctx}: must have at least one source")
        for s in sources:
            if "url" not in s or "date_accessed" not in s:
                errors.append(f"{ctx}: source missing url or date_accessed")

    return errors


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    with open(DATA_FILE) as f:
        data = json.load(f)

    errors = validate(data)
    if errors:
        print(f"❌ Validation failed with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"✅ {len(data['entries'])} entries valid.")


if __name__ == "__main__":
    main()
