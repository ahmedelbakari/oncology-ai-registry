#!/usr/bin/env python3
"""Apply the pilot batch validation data to the 3 phase-1 entries.

Source: VALIDATION_VERIFICATION_SHEET_pilot.md (curator-approved 2026-05-08).
Encodes the curator's decisions:
  - Artera: include both publications, npj Digital Med 2022 pivotal; external_validation.performed = true
  - Paige Prostate Detect: n_patients = 527 (1:1 with WSIs)
  - Vesta BCG: full validation fields populated from PubMed Central full text

Idempotent. Run from repo root.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"

ARTERA = {
    "study_design": "retrospective",
    "cohort_size": {
        "n_patients": 886,
        "n_samples": None,
        "unit_note": "patients (≥1 H&E biopsy slide containing the highest Gleason grade core per patient)",
    },
    "n_sites": 3,
    "site_geography": "multi_center_us",
    "comparator": "clinical_outcomes",
    "primary_endpoint": "time_to_event_risk_strata",
    "primary_result": (
        "10-year risk of distant metastasis: ArteraAI High 28.1% (95% CI 19.4–37.5%), "
        "Intermediate 6.6% (3.6–10.8%), Low 3.3% (1.8–5.6%); overall 8.1% (6.1–10.4%). "
        "10-year risk of prostate cancer-specific mortality: High 10.2% (4.7–18.2%), "
        "Intermediate 1.1% (0.2–3.7%), Low 0.6% (0.1–2.0%); overall 2.3% (1.2–3.8%). "
        "N=886 across 3 US sites."
    ),
    "external_validation": {
        "performed": True,
        "cohort_description": (
            "Pivotal clinical validation cohort N=886 across 3 US sites, independent of the "
            "training data (NRG/RTOG phase 3 trials, N=10,009 across Canary-PASS, RTOG 0126, "
            "0415, 0521, 9202, 9408, 9413, 9902, 9910, STAMPEDE, and Contemporary Biopsy "
            "Cohort A)."
        ),
        "result": (
            "Subgroup-consistent prognostic separation across treatment groups (Active "
            "Surveillance n=314; Radiation Therapy n=203; Radical Prostatectomy n=354) and "
            "across African-American (n=72) vs. non-African-American (n=814) subgroups."
        ),
    },
    "peer_reviewed": True,
    "key_publications": [
        {
            "title": "Prostate cancer therapy personalization via multi-modal deep learning on randomized phase III clinical trials",
            "journal": "npj Digital Medicine",
            "year": 2022,
            "url": "https://pubmed.ncbi.nlm.nih.gov/35676445/",
            "pivotal": True,
        },
        {
            "title": "Artificial Intelligence Predictive Model for Hormone Therapy Use in Prostate Cancer",
            "journal": "NEJM Evidence",
            "year": 2023,
            "url": "https://evidence.nejm.org/doi/10.1056/EVIDoa2300023",
            "pivotal": False,
        },
    ],
    "limitations_noted": (
        "FDA Decision Summary notes (i) the African-American subgroup was small (N=72) and "
        "'should be taken in consideration when using the risk estimates'; (ii) erroneous "
        "results may lead to over- or under-treatment; (iii) the device 'should be used in "
        "conjunction with a complete standard of care evaluation' and is not a primary "
        "diagnosis; (iv) clinical validation was at three US sites only and is retrospective."
    ),
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf",
    "data_completeness": "full",
}

PAIGE = {
    "study_design": "retrospective",
    "cohort_size": {
        "n_patients": 527,
        "n_samples": 527,
        "unit_note": (
            "527 whole slide images (171 cancer + 356 benign), one slide per unique patient; "
            "16 pathologist readers"
        ),
    },
    "n_sites": 157,
    "site_geography": "multi_center_international",
    "comparator": "pathologist_consensus",
    "primary_endpoint": "sensitivity_specificity",
    "primary_result": (
        "Combined (16 pathologists, assisted vs unassisted): sensitivity 96.8% vs 89.5% "
        "(improvement 7.3%, 95% CI 3.9–11.4%, statistically significant); specificity "
        "89.5% vs 88.4% (difference 1.1%, 95% CI -0.7–3.4%, not statistically significant). "
        "Stand-alone algorithm localization & accuracy study (728 WSIs): sensitivity 94.5% "
        "(95% CI 91.4–96.6%), specificity 94.0% (95% CI 91.3–95.9%)."
    ),
    "external_validation": {
        "performed": True,
        "cohort_description": (
            "FDA pivotal reader study used 527 WSIs sourced from 1 internal US site (44.15%) "
            "plus 156 different external sites worldwide (55.85%); none of the WSIs "
            "overlapped with the algorithm development data. Algorithm localization/accuracy "
            "study (728 WSIs) included slides from 217 different external sites worldwide."
        ),
        "result": (
            "Sensitivity stratified by source — internal site 94.1% (88.8–97.0%), external "
            "sites 94.9% (90.5–97.3%). Specificity — internal site 96.7% (93.0–98.5%), "
            "external sites 91.9% (87.7–94.7%)."
        ),
    },
    "peer_reviewed": True,
    "key_publications": [
        {
            "title": "Clinical Validation of Artificial Intelligence-Augmented Pathology Diagnosis Demonstrates Significant Gains in Diagnostic Accuracy in Prostate Cancer Detection",
            "journal": "Archives of Pathology & Laboratory Medicine",
            "year": 2023,
            "url": "https://pubmed.ncbi.nlm.nih.gov/36538386/",
            "pivotal": True,
        },
        {
            "title": "Novel artificial intelligence system increases the detection of prostate cancer in whole slide images of core needle biopsies",
            "journal": "Modern Pathology",
            "year": 2020,
            "url": "https://pubmed.ncbi.nlm.nih.gov/32393768/",
            "pivotal": False,
        },
    ],
    "limitations_noted": (
        "FDA Decision Summary notes: (i) the clinical study was 'on a per-biopsy basis, not "
        "on a per-patient basis. … the expected benefit of the use of the Paige device on "
        "the final diagnosis in practice would likely be substantially lower than 7.3% when "
        "evaluated on a per-patient basis'; (ii) the dataset 'was enriched with 50% "
        "challenging cancer slides, which were defined as slides with minimal tumor burden "
        "(≤0.5mm)' — performance may differ on routine-difficulty cases; (iii) initial "
        "interpretation only — 'special studies were not permitted'; (iv) all slides scanned "
        "with a single Philips Ultra Fast Scanner — performance with other scanners not "
        "evaluated; (v) the device is 'an adjunctive computer-assisted methodology and its "
        "output should not be used as the primary diagnosis.'"
    ),
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf",
    "data_completeness": "full",
}

VESTA = {
    "study_design": "retrospective",
    "cohort_size": {
        "n_patients": 944,
        "n_samples": None,
        "unit_note": (
            "patients (development cohort 303 across 5 centers; validation cohort 641 across "
            "7 centers); slide count not enumerated in the publication"
        ),
    },
    "n_sites": 12,
    "site_geography": "multi_center_international",
    "comparator": "clinicopathologic_factors",
    "primary_endpoint": "hazard_ratio",
    "primary_result": (
        "International validation cohort (n=641, 7 centers): high-grade recurrence HR 2.08 "
        "(95% CI 1.80–2.40, P<.0001); progression to muscle invasion HR 3.87 (95% CI "
        "2.75–5.44, P<.001); cystectomy HR 3.35 (95% CI 2.51–4.47, P<.001); "
        "BCG-unresponsive disease HR 2.31 (95% CI 1.89–2.82, P<.0001). Median follow-up "
        "36 months."
    ),
    "external_validation": {
        "performed": True,
        "cohort_description": (
            "International external validation cohort: 641 patients across 7 centers in the "
            "United States, Australia, Belgium, Netherlands, and Chile, distinct from the "
            "303-patient 5-center development cohort."
        ),
        "result": (
            "AI assays provided predictive information beyond clinicopathologic factors; "
            "HRs reported above achieved in the external validation cohort."
        ),
    },
    "peer_reviewed": True,
    "key_publications": [
        {
            "title": "Predicting Response to Intravesical Bacillus Calmette-Guérin in High-Risk Nonmuscle-Invasive Bladder Cancer Using an Artificial Intelligence-Powered Pathology Assay: Development and Validation in an International 12-Center Cohort",
            "journal": "Journal of Urology",
            "year": 2025,
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12674634/",
            "pivotal": True,
        }
    ],
    "limitations_noted": (
        "Publication notes that optimal validation would use a prospective clinical trial to "
        "mitigate confounding and bias; BCG regimen duration was heterogeneous, with 66% "
        "receiving FDA/IBCG-defined adequate BCG; treatment heterogeneity may confound "
        "disease outcomes; not all pT1 patients underwent re-TURBT, potentially confounding "
        "oncologic outcomes in that subgroup."
    ),
    "fda_summary_url": None,
    "data_completeness": "full",
}

# Vesta entry currently has wrong DOI/URL/year for the key publication. Apply
# inline corrections to source array as well: the BusinessWire press releases
# stay; the J Urol publication URL is corrected via key_publications above.

PILOT = {
    "artera-prostate": ARTERA,
    "paige-prostate-detect": PAIGE,
    "vesta-bcg": VESTA,
}


def main():
    data = json.loads(DATA.read_text())
    applied = []
    for e in data["entries"]:
        if e["id"] in PILOT:
            e["validation"] = PILOT[e["id"]]
            applied.append(e["id"])
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Applied pilot validation data to {len(applied)} entries:")
    for x in applied:
        print(f"  - {x}")


if __name__ == "__main__":
    main()
