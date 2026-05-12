#!/usr/bin/env python3
"""Apply phase-1 validation data and curator-approved corrections.

Source: VALIDATION_VERIFICATION_SHEET_phase1.md.

This script intentionally parses the JSON-shaped validation blocks from the
verification sheet so the audit artifact remains the source of truth.
Idempotent. Run from repo root.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"
SHEET = ROOT / "VALIDATION_VERIFICATION_SHEET_phase1.md"

PHASE1_IDS = {
    "paige-her2",
    "paige-lymph-node",
    "pathai-aisight-dx",
    "ibex-galen-prostate",
    "ibex-galen-breast",
    "owkin-msintuit-crc",
    "tempus-xt",
    "tempus-xm",
    "signatera-mrd",
    "grail-galleri",
    "exact-oncotype-dx-breast",
    "veracyte-decipher-prostate",
    "veracyte-afirma-gsc",
    "icad-profound-ai-dbt",
    "hologic-genius-ai-detection",
    "aidoc-briefcase-lung-nodule",
}


def load_validation_blocks():
    text = SHEET.read_text()
    blocks = {}
    pattern = re.compile(r"^## Entry: ([^\n]+).*?```json\n(.*?)\n```", re.M | re.S)
    for entry_id, block in pattern.findall(text):
        if entry_id in PHASE1_IDS:
            blocks[entry_id] = json.loads(block)
    missing = PHASE1_IDS - set(blocks)
    if missing:
        raise SystemExit(f"Missing phase-1 validation block(s): {sorted(missing)}")
    return blocks


def apply_regulatory_corrections(entry):
    entry_id = entry["id"]
    reg = entry.setdefault("regulatory", {})

    if entry_id == "ibex-galen-prostate":
        reg.update(
            {
                "fda_status": "510(k) cleared",
                "fda_pathway": "510k",
                "fda_510k_number": "K241232",
                "fda_decision_date": "2025-02-10",
            }
        )
        reg.pop("fda_de_novo_number", None)

    elif entry_id == "paige-her2":
        reg.update({"fda_status": "Research Use", "fda_pathway": None, "ce_marked": True})

    elif entry_id == "paige-lymph-node":
        reg.update({"fda_status": "Breakthrough Device Designation", "fda_pathway": None})
        reg.setdefault("fda_decision_date", None)

    elif entry_id == "hologic-genius-ai-detection":
        reg.update(
            {
                "fda_status": "510(k) cleared",
                "fda_pathway": "510k",
                "fda_510k_number": "K201019",
                "fda_decision_date": "2020-11-09",
            }
        )

    elif entry_id == "aidoc-briefcase-lung-nodule":
        # No Aidoc-held lung-nodule 510(k) was found. Keep the registry entry
        # but remove the unsupported market-authorization implication pending
        # Riverain/Aidoc source verification.
        reg.update({"fda_status": "Research Use", "fda_pathway": None, "fda_decision_date": None})
        reg.pop("fda_510k_number", None)


def main():
    data = json.loads(DATA.read_text())
    blocks = load_validation_blocks()
    applied = []

    for entry in data["entries"]:
        entry_id = entry["id"]
        if entry_id not in blocks:
            continue
        entry["validation"] = blocks[entry_id]
        apply_regulatory_corrections(entry)
        applied.append(entry_id)

    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Applied phase-1 validation data to {len(applied)} entries:")
    for entry_id in applied:
        print(f"  - {entry_id}")


if __name__ == "__main__":
    main()
