#!/usr/bin/env python3
"""Add 3 net-new Ataraxis Breast entries to data.json.

Source: VALIDATION_VERIFICATION_SHEET_ataraxis.md (curator-approved 2026-05-12).
Curator decisions applied:
  - RISK: downgraded to data_completeness="partial", peer_reviewed=false
    (clinical headline numbers are in preprint + ASCO abstract, not yet a
    peer-reviewed clinical paper; analytical-validation paper is peer-reviewed)
  - RISK: limitations note expanded to reflect preprint/abstract status
  - CTX: added as stub (no peer-reviewed pivotal exists yet)
  - NEO: added as stub (no peer-reviewed pivotal exists yet)
  - NY CLEP and CAP accreditation set to null for all three (not publicly asserted)

Idempotent — re-running on data with these entries already present is a no-op.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"


RISK = {
    "id": "ataraxis-breast-risk",
    "product_name": "Ataraxis Breast RISK",
    "company": "Ataraxis AI",
    "company_url": "https://www.ataraxis.ai/",
    "cancer_types": ["breast"],
    "modality": "histopathology",
    "intended_use": (
        "AI-based prognostic test that integrates clinical data with morphological "
        "features extracted from H&E-stained primary tumor slides to predict risk of "
        "recurrence or death in women with early-stage (stage I–III) invasive breast "
        "cancer; validated across all major molecular subtypes including HR+/HER2-, "
        "HER2+, and triple-negative breast cancer."
    ),
    "regulatory": {
        "fda_status": "LDT",
        "fda_pathway": None,
        "ldt": True,
        "ny_clep": None,
        "cap_accredited": None,
        "clia_certified": True,
        "ce_marked": None,
    },
    "deployment": {
        "available": True,
        "us_cancer_centers_estimated": None,
        "patients_estimated": None,
        "partners": [
            "NYU Langone Health",
            "Karmanos Cancer Institute",
            "Gundersen Health System",
            "Catholic University of Korea",
            "UChicago Medicine",
            "University Hospital Basel",
            "Unicancer",
            "MEDSIR",
        ],
    },
    "sources": [
        {"type": "publication", "url": "https://www.mdpi.com/2075-4418/16/7/1023", "date_accessed": "2026-05-12"},
        {"type": "publication", "url": "https://arxiv.org/html/2410.21256", "date_accessed": "2026-05-12"},
        {"type": "publication", "url": "https://ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.549", "date_accessed": "2026-05-12"},
        {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-overview", "date_accessed": "2026-05-12"},
        {"type": "press", "url": "https://www.businesswire.com/news/home/20260105730450/en/", "date_accessed": "2026-05-12"},
        {"type": "press", "url": "https://www.businesswire.com/news/home/20251002282761/en/", "date_accessed": "2026-05-12"},
    ],
    "validation": {
        "study_design": "retrospective",
        "cohort_size": {
            "n_patients": 3502,
            "n_samples": 3632,
            "unit_note": (
                "External evaluation cohort: 3,502 patients (3,632 slides) across 5 cohorts spanning "
                "7 countries (USA, South Korea, Lithuania, Malaysia, Switzerland, Wales, UK). "
                "Development cohort (separately): 4,659 patients across 10 cohorts. "
                "Analytical validation paper (Diagnostics 2026) used 160 cases for the full AV battery."
            ),
        },
        "n_sites": 5,
        "site_geography": "multi_center_international",
        "comparator": "gold_standard_test",
        "primary_endpoint": "concordance",
        "primary_result": (
            "External evaluation (n=3,502 across 5 cohorts, 7 countries): DFI C-index 0.71 "
            "(95% CI 0.68–0.75), HR 3.63 (3.02–4.37, p<0.001) per 0.2-unit increase. "
            "Subtype-specific: HR+/HER2- (n=1,858) C-index 0.67 (0.61–0.74), HR 3.67 (2.79–4.84); "
            "TNBC (n=230) C-index 0.71 (0.62–0.81), HR 3.81 (2.35–6.17); HER2+ (n=343) "
            "C-index 0.67 (0.55–0.80), HR 2.22 (0.99–5.01). "
            "Head-to-head vs Oncotype DX (n=858): ATX C-index 0.67 (0.61–0.74) vs Oncotype 0.61 "
            "(0.49–0.73); ATX adds independent prognostic information in multivariate analysis "
            "(adjusted HR 3.11 [1.91–5.09], p<0.001). "
            "Analytical validation (Diagnostics 2026): all pre-defined acceptance criteria met for "
            "intra-/inter-operator repeatability, limit of blank, limit of detection, and "
            "inter-laboratory reproducibility in a CLIA setting."
        ),
        "external_validation": {
            "performed": True,
            "cohort_description": (
                "External evaluation cohort of 3,502 patients across 5 cohorts spanning 7 countries "
                "(USA, South Korea, Lithuania, Malaysia, Switzerland, Wales/UK), institutionally "
                "distinct from the 4,659-patient 10-cohort development set. Includes Karmanos Cancer "
                "Institute, University Hospital Basel, UChicago Medicine, plus public datasets "
                "(TCGA-BRCA, METABRIC, BASIS, Providence)."
            ),
            "result": (
                "DFI C-index 0.71 (0.68–0.75), HR 3.63 (3.02–4.37, p<0.001); ATX added independent "
                "prognostic information beyond Oncotype DX and clinicopathologic variables "
                "(adjusted HR 3.11 [1.91–5.09], p<0.001)."
            ),
        },
        "peer_reviewed": False,
        "key_publications": [
            {
                "title": "Analytical Validation of Multimodal AI Test Predicting Breast Cancer Recurrence Risk (Ataraxis Breast RISK)",
                "journal": "Diagnostics",
                "year": 2026,
                "url": "https://www.mdpi.com/2075-4418/16/7/1023",
                "pivotal": True,
            },
            {
                "title": "Multi-modal AI for comprehensive breast cancer prognostication",
                "journal": "arXiv (preprint)",
                "year": 2024,
                "url": "https://arxiv.org/html/2410.21256",
                "pivotal": False,
            },
            {
                "title": "Clinical validation of a multi-modal Ataraxis AI platform for recurrence prediction in early-stage breast cancer across multiple patient cohorts",
                "journal": "Journal of Clinical Oncology (ASCO 2025 abstract 549)",
                "year": 2025,
                "url": "https://ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.549",
                "pivotal": False,
            },
        ],
        "limitations_noted": (
            "Analytical validation (Diagnostics 2026) is peer-reviewed; the clinical headline numbers "
            "(C-index, HRs, Oncotype DX head-to-head) currently live in an arXiv preprint (Witowski "
            "et al., 2024) and an ASCO 2025 congress abstract — neither has yet completed peer review. "
            "Per the preprint: study uses observational, retrospective data and 'did not evaluate the "
            "test's predictive capabilities (i.e., its ability to determine whether a patient is "
            "likely to benefit from a specific treatment)'; approximately 93% of cases were "
            "represented by a single slide; HER2+ subtype HR confidence interval includes 1.0 (p=0.05); "
            "intermediate-risk thresholding has not yet been validated prospectively. Prospective "
            "RCT-based validation pipeline (Unicancer, MEDSIR) is announced but not yet reported."
        ),
        "fda_summary_url": None,
        "data_completeness": "partial",
    },
}


CTX = {
    "id": "ataraxis-breast-ctx",
    "product_name": "Ataraxis Breast CTX",
    "company": "Ataraxis AI",
    "company_url": "https://www.ataraxis.ai/",
    "cancer_types": ["breast"],
    "modality": "histopathology",
    "intended_use": (
        "Predictive AI test that quantifies individualized adjuvant chemotherapy benefit in patients "
        "with early-stage HR+/HER2- breast cancer by simulating outcomes under endocrine therapy "
        "alone versus endocrine plus chemotherapy from H&E pathology slides combined with clinical data."
    ),
    "regulatory": {
        "fda_status": "LDT",
        "fda_pathway": None,
        "ldt": True,
        "ny_clep": None,
        "cap_accredited": None,
        "clia_certified": True,
        "ce_marked": None,
    },
    "deployment": {
        "available": True,
        "us_cancer_centers_estimated": None,
        "patients_estimated": None,
        "partners": [],
    },
    "sources": [
        {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-ctx", "date_accessed": "2026-05-12"},
        {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-overview", "date_accessed": "2026-05-12"},
        {"type": "press", "url": "https://www.businesswire.com/news/home/20260330075280/en/", "date_accessed": "2026-05-12"},
        {"type": "press", "url": "https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-individualized-chemotherapy-benefit-breast-cancer/", "date_accessed": "2026-05-12"},
    ],
    "validation": {
        "study_design": "retrospective",
        "cohort_size": {
            "n_patients": None,
            "n_samples": None,
            "unit_note": (
                "Company-stated development cohort >10,000 breast cancer patients worldwide; "
                "validation effect sizes and 95% CIs not yet published in a peer-reviewed venue. "
                "Product page references subgroup sizes (n=191 and n=1,339) without naming "
                "underlying cohorts."
            ),
        },
        "n_sites": None,
        "site_geography": "multi_center_international",
        "comparator": "clinical_outcomes",
        "primary_endpoint": "other",
        "primary_result": None,
        "external_validation": {
            "performed": None,
            "cohort_description": (
                "Company asserts independent validation across observational real-world studies and "
                "randomized controlled trials; no peer-reviewed external validation report identified."
            ),
            "result": None,
        },
        "peer_reviewed": False,
        "key_publications": [],
        "limitations_noted": (
            "No peer-reviewed pivotal publication for Ataraxis Breast CTX identified as of 2026-05-12. "
            "Effect-size and cohort statements come from the company's product page and launch press "
            "release (Tier-3 / Tier-4 sources). The 'Ataraxis Tau' causal-inference layer asserted to "
            "handle treatment-selection confounding in retrospective data has not been independently "
            "audited in a peer-reviewed venue specific to CTX."
        ),
        "fda_summary_url": None,
        "data_completeness": "stub",
    },
}


NEO = {
    "id": "ataraxis-breast-neo",
    "product_name": "Ataraxis Breast NEO",
    "company": "Ataraxis AI",
    "company_url": "https://www.ataraxis.ai/",
    "cancer_types": ["breast"],
    "modality": "histopathology",
    "intended_use": (
        "Predictive AI test that estimates the likelihood of pathologic complete response (pCR) "
        "following neoadjuvant therapy in patients with early-stage (stage I–III) invasive breast "
        "cancer across all major subtypes (HR+/HER2-, HER2+, TNBC), ordered from the core needle "
        "biopsy H&E slide at initial diagnosis before treatment decisions are made."
    ),
    "regulatory": {
        "fda_status": "LDT",
        "fda_pathway": None,
        "ldt": True,
        "ny_clep": None,
        "cap_accredited": None,
        "clia_certified": True,
        "ce_marked": None,
    },
    "deployment": {
        "available": True,
        "us_cancer_centers_estimated": None,
        "patients_estimated": None,
        "partners": ["UChicago Medicine"],
    },
    "sources": [
        {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-neo", "date_accessed": "2026-05-12"},
        {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-overview", "date_accessed": "2026-05-12"},
        {"type": "press", "url": "https://www.businesswire.com/news/home/20260409921421/en/", "date_accessed": "2026-05-12"},
        {"type": "press", "url": "https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-neoadjuvant-response-early-breast-cancer/", "date_accessed": "2026-05-12"},
    ],
    "validation": {
        "study_design": "retrospective",
        "cohort_size": {
            "n_patients": None,
            "n_samples": None,
            "unit_note": (
                "Company-stated: ~1,000 training and ~1,500 evaluation, ~2,500 patients from US and "
                "abroad total. Subtype-specific breakdown on product page: HR+/HER2- n=296; HER2+ "
                "n=916; TNBC n=254. SABCS 2025 abstract (Howard et al., UChicago) reports external "
                "validation in n=563. No peer-reviewed pivotal publication identified as of 2026-05-12."
            ),
        },
        "n_sites": None,
        "site_geography": "multi_center_international",
        "comparator": "clinical_outcomes",
        "primary_endpoint": "AUC",
        "primary_result": (
            "Tier-3 only (company product page + SABCS 2025 abstract; no peer-reviewed publication): "
            "subtype-specific AUCs — HR+/HER2- (n=296) AUC 0.85 (95% CI 0.76–0.96); HER2+ (n=916) "
            "AUC 0.66 (0.60–0.73); TNBC (n=254) AUC 0.77 (0.68–0.86). SABCS 2025 external-validation "
            "AUC 0.72 (0.65–0.80) in n=563."
        ),
        "external_validation": {
            "performed": True,
            "cohort_description": (
                "Company-stated external validation of '563 patients from four independent, "
                "international datasets'; SABCS 2025 abstract (Howard et al., PS3-04-04) describes "
                "'AI Predicts Response to Neoadjuvant Therapy in Breast Cancer Across Diverse Cohorts.'"
            ),
            "result": (
                "AUC 0.72 (95% CI 0.65–0.80) for prediction of pathologic complete response "
                "(per SABCS 2025 abstract, mirror coverage)."
            ),
        },
        "peer_reviewed": False,
        "key_publications": [],
        "limitations_noted": (
            "No peer-reviewed pivotal publication for Ataraxis Breast NEO identified as of 2026-05-12. "
            "SABCS 2025 abstract by Howard et al. (UChicago, PS3-04-04) is the most rigorous public "
            "evidence but is an abstract, not a full paper. Subtype AUCs vary widely (HER2+ AUC 0.66 "
            "vs HR+/HER2- AUC 0.85), suggesting heterogeneous performance across subtypes; clinical "
            "utility of using a single test cutoff across subtypes is unestablished."
        ),
        "fda_summary_url": None,
        "data_completeness": "stub",
    },
}


NEW_ENTRIES = [RISK, CTX, NEO]


def main():
    data = json.loads(DATA.read_text())
    existing_ids = {e["id"] for e in data["entries"]}
    added = []
    for entry in NEW_ENTRIES:
        if entry["id"] in existing_ids:
            print(f"  - skip {entry['id']} (already present)")
            continue
        data["entries"].append(entry)
        added.append(entry["id"])
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {len(added)} new Ataraxis entries:")
    for x in added:
        print(f"  + {x}")
    print(f"Total entries now: {len(data['entries'])}")


if __name__ == "__main__":
    main()
