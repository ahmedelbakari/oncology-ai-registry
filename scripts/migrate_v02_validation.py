#!/usr/bin/env python3
"""One-time migration: add the v0.2 validation schema to every entry.

- Bumps schema_version 0.1 -> 0.2
- For each entry, adds a `validation` object with structured fields.
- Migrates the existing `clinical_evidence` (single key publication) into
  `validation.key_publications[0]` with pivotal=true; drops `clinical_evidence`.
- Marks all 18 phase-1 entries with data_completeness="stub_phase1" so we can
  see exactly which ones need population. Everything else: "stub".
- Idempotent: re-running on already-migrated data is a no-op.

Run from repo root:
    python3 scripts/migrate_v02_validation.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"

PHASE_1_IDS = {
    "paige-prostate-detect",
    "paige-her2",
    "pathai-aisight-dx",
    "ibex-galen-prostate",
    "ibex-galen-breast",
    "owkin-msintuit-crc",
    "vesta-bcg",
    "tempus-xt",
    "tempus-xm",
    "signatera-mrd",
    "grail-galleri",
    "exact-oncotype-dx-breast",
    "veracyte-decipher-prostate",
    "veracyte-afirma-gsc",
    "artera-prostate",
    "icad-profound-ai-dbt",
    "hologic-genius-ai-detection",
    "aidoc-briefcase-lung-nodule",
}


def empty_validation():
    return {
        "study_design": None,
        "cohort_size": {
            "n_patients": None,
            "n_samples": None,
            "unit_note": None,
        },
        "n_sites": None,
        "site_geography": None,
        "comparator": None,
        "primary_endpoint": None,
        "primary_result": None,
        "external_validation": {
            "performed": None,
            "cohort_description": None,
            "result": None,
        },
        "peer_reviewed": None,
        "key_publications": [],
        "limitations_noted": None,
        "fda_summary_url": None,
        "data_completeness": "stub",
    }


def migrate_entry(e):
    if "validation" in e and "clinical_evidence" not in e:
        # already migrated
        return e
    v = empty_validation()
    ce = e.get("clinical_evidence")
    if ce and ce.get("key_publication"):
        v["key_publications"].append(
            {
                "title": ce.get("key_publication"),
                "journal": ce.get("journal"),
                "year": ce.get("year"),
                "url": ce.get("url"),
                "pivotal": True,
            }
        )
        v["peer_reviewed"] = True
    if e.get("id") in PHASE_1_IDS:
        v["data_completeness"] = "stub_phase1"
    e["validation"] = v
    e.pop("clinical_evidence", None)
    return e


def main():
    data = json.loads(DATA.read_text())
    data["schema_version"] = "0.2"
    for e in data["entries"]:
        migrate_entry(e)
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    phase1 = sum(1 for e in data["entries"] if e["validation"]["data_completeness"] == "stub_phase1")
    print(f"Migrated {len(data['entries'])} entries to schema v0.2.")
    print(f"  phase-1 stubs (full population pending): {phase1}")
    print(f"  other stubs: {len(data['entries']) - phase1}")


if __name__ == "__main__":
    main()
