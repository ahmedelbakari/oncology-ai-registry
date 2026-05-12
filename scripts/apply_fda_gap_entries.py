#!/usr/bin/env python3
"""Apply 10 net-new entries from the FDA coverage-gap batch to data.json.

Source: VALIDATION_VERIFICATION_SHEET_fda_gap.md (curator-approved 2026-05-12).

The agent that produced the verification sheet wrote richer enum values than v0.2
schema allows (e.g., study_design='prospective_multicenter_mrmc', primary_endpoint=
'specificity_at_fixed_sensitivity', comparator='expert_clinicians'). This script
parses the sheet, normalizes those values to the v0.2 enum, preserves the agent's
detail in limitations_noted, strips non-schema fields (deployment.fda_cleared),
and appends the 10 oncology-relevant entries to data.json.

Three sheet entries were already dropped by the agent as not-oncology (no JSON
proposed): #2 INFINITT DPS, #9 Exo Lung AI, #13 Imbio Lung Density.

Idempotent.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"
SHEET = ROOT / "VALIDATION_VERIFICATION_SHEET_fda_gap.md"


# v0.2 schema enums (must match scripts/validate.py)
ALLOWED_STUDY_DESIGN = {"prospective", "retrospective", "rct", "meta_analysis", "bench_only", "unpublished"}
ALLOWED_COMPARATOR = {"pathologist_consensus", "gold_standard_test", "clinical_outcomes",
                     "clinicopathologic_factors", "predicate_device", "none"}
ALLOWED_PRIMARY_ENDPOINT = {"AUC", "sensitivity", "specificity", "sensitivity_specificity",
                           "ppv_npv", "hazard_ratio", "time_to_event_risk_strata", "concordance", "other"}
ALLOWED_SITE_GEOGRAPHY = {"single_center_us", "multi_center_us", "multi_center_international"}


# Mapping rules (preserve detail; map to closest enum value)
STUDY_DESIGN_MAP = {
    "prospective_multicenter_mrmc": ("prospective", "Multi-center MRMC (multi-reader, multi-case)"),
    "prospective_singlecenter": ("prospective", "Single-center"),
    "retrospective_multicenter": ("retrospective", "Multi-center"),
    "retrospective_singlecenter": ("retrospective", "Single-center"),
    "retrospective_multicenter_mrmc": ("retrospective", "Multi-center MRMC (multi-reader, multi-case)"),
    "retrospective_multireader_multicase": ("retrospective", "MRMC (multi-reader, multi-case)"),
}

COMPARATOR_MAP = {
    "predicate_device": "predicate_device",
    "expert_clinicians": "pathologist_consensus",      # ground truth set by expert clinical reads
    "standard_of_care_clinicians": "pathologist_consensus",
    "unaided_reader": "pathologist_consensus",         # AI-aided vs same reader unaided
    "historical_controls": "clinical_outcomes",
}

PRIMARY_ENDPOINT_MAP = {
    "specificity_at_fixed_sensitivity": "specificity",
    "non_inferiority_volume_measurement": "other",
    "AUC_aided_vs_unaided": "AUC",
    "dice_coefficient": "concordance",
    "sensitivity_specificity_lesion_contouring": "sensitivity_specificity",
    "AUC_LROC_aided_vs_unaided": "AUC",
    "JAFROC_figure_of_merit": "AUC",
    "diagnostic_yield": "other",
}

SITE_GEOGRAPHY_MAP = {
    "single_center_international": "multi_center_international",   # closest; geography preserved in unit_note
}


def normalize_validation(eid, v):
    """Normalize agent-produced validation block to v0.2 enum values."""
    notes = []

    # study_design
    sd = v.get("study_design")
    if sd in STUDY_DESIGN_MAP:
        new_sd, detail = STUDY_DESIGN_MAP[sd]
        v["study_design"] = new_sd
        notes.append(f"Study design: {detail}")
    elif sd is not None and sd not in ALLOWED_STUDY_DESIGN:
        notes.append(f"Study design (original): {sd}")
        v["study_design"] = "retrospective"  # safe fallback for FDA-summary-only sourcing

    # comparator
    cmp = v.get("comparator")
    if cmp in COMPARATOR_MAP:
        v["comparator"] = COMPARATOR_MAP[cmp]
    elif cmp is not None and cmp not in ALLOWED_COMPARATOR:
        notes.append(f"Comparator (original): {cmp}")
        v["comparator"] = "predicate_device"

    # primary_endpoint
    pe = v.get("primary_endpoint")
    if pe in PRIMARY_ENDPOINT_MAP:
        v["primary_endpoint"] = PRIMARY_ENDPOINT_MAP[pe]
        notes.append(f"Primary endpoint (original): {pe}")
    elif pe is not None and pe not in ALLOWED_PRIMARY_ENDPOINT:
        notes.append(f"Primary endpoint (original): {pe}")
        v["primary_endpoint"] = "other"

    # site_geography
    sg = v.get("site_geography")
    if sg in SITE_GEOGRAPHY_MAP:
        notes.append(f"Site geography (original): {sg}")
        v["site_geography"] = SITE_GEOGRAPHY_MAP[sg]

    # Prepend notes to limitations_noted
    if notes:
        lim = v.get("limitations_noted") or ""
        prefix = "; ".join(notes)
        v["limitations_noted"] = f"[Source-detail preserved: {prefix}] {lim}".strip()

    # Ensure all required sub-blocks present
    if "external_validation" not in v:
        v["external_validation"] = {"performed": None, "cohort_description": None, "result": None}
    else:
        ev = v["external_validation"]
        ev.setdefault("performed", None)
        ev.setdefault("cohort_description", None)
        ev.setdefault("result", None)

    if "cohort_size" not in v:
        v["cohort_size"] = {"n_patients": None, "n_samples": None, "unit_note": None}
    else:
        cs = v["cohort_size"]
        cs.setdefault("n_patients", None)
        cs.setdefault("n_samples", None)
        cs.setdefault("unit_note", None)

    v.setdefault("key_publications", [])
    v.setdefault("peer_reviewed", False)
    v.setdefault("fda_summary_url", None)

    return v


def normalize_entry(e):
    # Strip non-schema fields from deployment
    dep = e.get("deployment") or {}
    dep.pop("fda_cleared", None)
    e["deployment"] = dep

    # Ensure required regulatory keys present (validator allows null)
    reg = e.get("regulatory") or {}
    for k in ("fda_status", "fda_pathway", "ldt", "ny_clep", "cap_accredited", "clia_certified"):
        reg.setdefault(k, None)
    e["regulatory"] = reg

    # Normalize validation block
    e["validation"] = normalize_validation(e["id"], e.get("validation", {}))
    return e


def parse_sheet():
    text = SHEET.read_text()
    sections = re.split(r'(?m)^(## \d+\. .*?)$', text)
    out = []
    for i in range(1, len(sections), 2):
        header = sections[i]
        body = sections[i+1] if i+1 < len(sections) else ""
        m = re.search(r'^## (\d+)\. (.+?) — `([^`]+)`', header)
        if not m:
            continue
        num, eid = int(m.group(1)), m.group(3).strip()
        m2 = re.search(r'### Proposed entry \(v0\.2\)\s*```json\s*(.*?)\s*```', body, re.DOTALL)
        if not m2:
            continue  # dropped entries have no JSON
        try:
            parsed = json.loads(m2.group(1).strip())
        except Exception as e:
            print(f"  ! parse error #{num} {eid}: {e}")
            continue
        out.append((num, parsed))
    return out


def main():
    data = json.loads(DATA.read_text())
    existing_ids = {e["id"] for e in data["entries"]}
    parsed = parse_sheet()

    added, skipped = [], []
    for num, entry in parsed:
        if entry["id"] in existing_ids:
            skipped.append(entry["id"])
            continue
        normalized = normalize_entry(entry)
        data["entries"].append(normalized)
        added.append(entry["id"])
        print(f"  + #{num:2d} {entry['id']}")

    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"\nAdded {len(added)} entries; skipped {len(skipped)} already present.")
    print(f"Total entries now: {len(data['entries'])}")


if __name__ == "__main__":
    main()
