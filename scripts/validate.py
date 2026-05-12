#!/usr/bin/env python3
"""Validate data.json schema for the OncologyAI Registry.

Runs in CI and pre-push. Returns non-zero on any schema violation.
Schema v0.2 adds a `validation` object per entry.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "v1" / "data.json"

REQUIRED_ENTRY_FIELDS = {
    "id",
    "product_name",
    "company",
    "cancer_types",
    "modality",
    "intended_use",
    "regulatory",
    "sources",
    "validation",
}
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
    "radiology_us",
    "genomic_sequencing_with_ai",
    "liquid_biopsy",
    "multiomics",
}
ALLOWED_STUDY_DESIGN = {
    None,
    "prospective",
    "retrospective",
    "rct",
    "meta_analysis",
    "bench_only",
    "unpublished",
}
ALLOWED_SITE_GEOGRAPHY = {
    None,
    "single_center_us",
    "multi_center_us",
    "multi_center_international",
}
ALLOWED_COMPARATOR = {
    None,
    "pathologist_consensus",
    "gold_standard_test",
    "clinical_outcomes",
    "clinicopathologic_factors",
    "predicate_device",
    "none",
}
ALLOWED_PRIMARY_ENDPOINT = {
    None,
    "AUC",
    "sensitivity",
    "specificity",
    "sensitivity_specificity",
    "ppv_npv",
    "hazard_ratio",
    "time_to_event_risk_strata",
    "concordance",
    "other",
}
ALLOWED_DATA_COMPLETENESS = {"full", "partial", "stub", "stub_phase1"}

REQUIRED_VALIDATION_FIELDS = {
    "study_design",
    "cohort_size",
    "n_sites",
    "site_geography",
    "comparator",
    "primary_endpoint",
    "primary_result",
    "external_validation",
    "peer_reviewed",
    "key_publications",
    "limitations_noted",
    "fda_summary_url",
    "data_completeness",
}


def validate_validation_block(ctx, v, errors):
    if not isinstance(v, dict):
        errors.append(f"{ctx}: validation must be an object")
        return
    missing = REQUIRED_VALIDATION_FIELDS - set(v.keys())
    if missing:
        errors.append(f"{ctx}: validation missing fields {sorted(missing)}")
    if v.get("study_design") not in ALLOWED_STUDY_DESIGN:
        errors.append(f"{ctx}: validation.study_design '{v.get('study_design')}' not allowed")
    if v.get("site_geography") not in ALLOWED_SITE_GEOGRAPHY:
        errors.append(f"{ctx}: validation.site_geography '{v.get('site_geography')}' not allowed")
    if v.get("comparator") not in ALLOWED_COMPARATOR:
        errors.append(f"{ctx}: validation.comparator '{v.get('comparator')}' not allowed")
    if v.get("primary_endpoint") not in ALLOWED_PRIMARY_ENDPOINT:
        errors.append(f"{ctx}: validation.primary_endpoint '{v.get('primary_endpoint')}' not allowed")
    if v.get("data_completeness") not in ALLOWED_DATA_COMPLETENESS:
        errors.append(
            f"{ctx}: validation.data_completeness '{v.get('data_completeness')}' not in {sorted(ALLOWED_DATA_COMPLETENESS)}"
        )

    cs = v.get("cohort_size")
    if not isinstance(cs, dict) or {"n_patients", "n_samples", "unit_note"} - set(cs.keys()):
        errors.append(f"{ctx}: validation.cohort_size must include n_patients, n_samples, unit_note")

    ev = v.get("external_validation")
    if not isinstance(ev, dict) or {"performed", "cohort_description", "result"} - set(ev.keys()):
        errors.append(f"{ctx}: validation.external_validation must include performed, cohort_description, result")

    pubs = v.get("key_publications")
    if not isinstance(pubs, list):
        errors.append(f"{ctx}: validation.key_publications must be a list")
    else:
        for j, p in enumerate(pubs):
            if not isinstance(p, dict) or "url" not in p:
                errors.append(f"{ctx}: validation.key_publications[{j}] missing url")


def validate(data):
    errors = []
    seen_ids = set()
    entries = data.get("entries", [])
    if not entries:
        errors.append("No entries in data.json")
        return errors

    if data.get("schema_version") != "0.2":
        errors.append(f"schema_version must be '0.2', got '{data.get('schema_version')}'")

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

        if "validation" in e:
            validate_validation_block(ctx, e["validation"], errors)

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
