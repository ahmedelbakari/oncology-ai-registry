# Validation Verification Sheet — FDA Gap Batch

**Purpose:** Source 13 net-new entries for the OncologyAI Registry from FDA AI/ML-enabled device list, populating v0.2 schema with primary-source-quoted validation blocks.

**Date prepared:** 2026-05-12
**Curator:** A. Elbakri (with AI-agent sourcing pass)
**Status:** Proposed entries — DO NOT merge to `data.json` without curator review.

**Scope flags identified during sourcing (read summary at end first):**
- 3 items recommended for **dropping** as not oncology-relevant (Exo Lung AI = pleural effusion ultrasound, no cancer; Imbio Lung Density = COPD/emphysema, no cancer; INFINITT DPS = pure WSI viewer, no AI cancer-detection function).
- 3 items are **prostate-imaging-workflow only** (volume/segmentation, not cancer detection): Clarius Prostate AI, JLK Medihub Prostate, Quantib Prostate. They support the prostate-cancer workflow but their indications are not cancer detection. Recommend inclusion with `data_completeness: "partial"` and clear `intended_use` text.
- 1 item (Body Vision LungVision) is a navigation-guidance device for bronchoscopic biopsy of suspected lung lesions — cancer-relevant but the 510(k) summary contains no clinical metrics; peer-reviewed prospective publication exists and is cited.

---

## 1. Imagio Breast Imaging System — `seno-imagio-breast`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA PMA SSED P200003 (Summary of Safety and Effectiveness Data) | https://www.accessdata.fda.gov/cdrh_docs/pdf20/P200003B.pdf | 2026-05-12 |
| 1 | FDA PMA listing page | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm?id=P200003 | 2026-05-12 |
| 1 | Neuschler EI et al., "A Pivotal Study of Optoacoustic Imaging to Diagnose Benign and Malignant Breast Masses: A New Evaluation Tool for Radiologists." *Radiology* 2018;287(2):398-412. | https://pubmed.ncbi.nlm.nih.gov/29178816/ | 2026-05-12 |
| 1 | Neuschler EI et al., "Optoacoustic Imaging With Decision Support for Differentiation of Benign and Malignant Breast Masses: A 15-Reader Retrospective Study." *Acad Radiol* 2022. | https://pubmed.ncbi.nlm.nih.gov/36475811/ | 2026-05-12 |

### Proposed entry (v0.2)
```json
{
  "id": "seno-imagio-breast",
  "product_name": "Imagio Breast Imaging System",
  "company": "Seno Medical Instruments, Inc.",
  "company_url": "https://senomedical.com/",
  "cancer_types": ["breast"],
  "modality": "radiology_us",
  "intended_use": "Evaluation of palpable and non-palpable breast abnormalities in adult patients referred for diagnostic imaging breast work-up. Fuses internal ultrasound (IUS) with opto-acoustic (OA) imaging; includes an AI-based decision-support classifier (SenoGram) to assist in BI-RADS assessment of BI-RADS 3-5 masses. Not a replacement for mammographic screening or definitive pathologic diagnosis.",
  "regulatory": {
    "fda_status": "PMA approved",
    "fda_pathway": "pma",
    "fda_decision_date": "2021-01-11",
    "fda_pma_number": "P200003",
    "ldt": false,
    "ny_clep": null,
    "cap_accredited": null,
    "clia_certified": null,
    "ce_marked": true
  },
  "deployment": {
    "available": true,
    "fda_cleared": true
  },
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf20/P200003B.pdf", "date_accessed": "2026-05-12"},
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm?id=P200003", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://pubmed.ncbi.nlm.nih.gov/29178816/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "prospective_multicenter_mrmc",
    "cohort_size": {
      "n_patients": 480,
      "n_samples": 480,
      "unit_note": "Reader-02 Pivotal MRMC Study read 480 masses (180 malignant + 300 benign/TPB/high-risk) drawn from the larger PIONEER ITD population of 1,739 subjects (PIONEER Safety Population N=1,972; total enrolled N=2,105). 15 independent readers, 4 blocks of 120 masses each. Each mass read twice: Read 1 (IUS+history+mammogram), Read 2 (Read 1 + OA + SenoGram)."
    },
    "n_sites": 16,
    "site_geography": "multi_center_us",
    "comparator": "predicate_device",
    "primary_endpoint": "specificity_at_fixed_sensitivity",
    "primary_result": "Primary endpoint MET. Specificity at fixed 98% sensitivity (fSp) — IUS+OA (Imagio): 47.2% (95% CI 35.9%, 58.5%); IUS alone: 38.2% (95% CI 24.9%, 51.6%); difference +9.0% (95% CI 1.0%, 17.0%), two-sided p=0.027. Secondary NLR mean 0.047 (95% CI 0.032, 0.062) for IUS+OA vs 0.053 (95% CI 0.037, 0.070) for IUS; relative NLR 0.896 (95% CI 0.693, 1.11) — NOT statistically significant, so per pre-specified sequential hierarchical testing, downstream PLR and pAUC reported as descriptive only.",
    "external_validation": {
      "performed": true,
      "cohort_description": "PIONEER was a 16-site US prospective study (7 academic + 9 private practices) enrolling from December 2012 through September 2015; subjects referred for diagnostic ultrasound work-up of suspicious findings. Reader-02 readers were independent of any prior Seno study.",
      "result": "Sites geographically distributed across the US; demographic spread by age, BI-RADS, breast density, palpability, menopausal status reported in SSED Table 3."
    },
    "peer_reviewed": true,
    "key_publications": [
      {
        "title": "A Pivotal Study of Optoacoustic Imaging to Diagnose Benign and Malignant Breast Masses: A New Evaluation Tool for Radiologists",
        "journal": "Radiology",
        "year": 2018,
        "url": "https://pubmed.ncbi.nlm.nih.gov/29178816/",
        "pivotal": true
      },
      {
        "title": "Optoacoustic Imaging With Decision Support for Differentiation of Benign and Malignant Breast Masses: A 15-Reader Retrospective Study",
        "journal": "Academic Radiology",
        "year": 2022,
        "url": "https://pubmed.ncbi.nlm.nih.gov/36475811/",
        "pivotal": false
      }
    ],
    "limitations_noted": "PMA SSED notes: (i) Reader-02 used a SUBSET (n=480) of the larger PIONEER ITD population (n=1,739) because an initial MRMC study had methodological issues and could not be submitted to FDA — Reader-02 was a re-do; (ii) prevalence of cancer in Reader-02 (~38%) was enriched/stratified, not reflective of typical clinical population; (iii) of secondary endpoints, only fSp was confirmatory — NLR, PLR, and pAUC results reported as descriptive only after NLR failed hierarchical testing; (iv) 7 SAEs in 5 subjects (none device-related); 11 procedure-related AEs in 10 subjects, all mild, including 1 second-degree burn attributed to contact dermatitis rather than laser; (v) device labeling: 'not intended to be used as a replacement for mammographic screening or for definitive pathologic diagnosis'; (vi) excluded male subjects, breast implants <12mo, mass >4cm, photosensitive disease.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf20/P200003B.pdf",
    "data_completeness": "full"
  }
}
```

### Field-by-field provenance (validation block)
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| study_design | SSED p. 11 | "single arm, sequentially read, controlled, blinded, multi-reader, multi-case (MRMC) pivotal study, referred to as Reader-02" |
| n_patients=480 | SSED p. 16 | "The number of masses was 480 masses in total, comprised of the following: • 180 malignant masses • 300 benign masses (288 benign, 12 high risk…)" |
| n_sites=16 | SSED p. 11 | "There were 16 investigational sites, 7 academic and 9 private practices. All sites were in the United States of America (USA)." |
| primary_result fSp | SSED p. 28 | "Mean (average over all readers) fSp was found to be higher with statistical significance (two-sided p=0.027) for IUS+OA (47.2%, 95% CI=[35.9%,58.5%]) compared to IUS alone (38.2%, 95% CI=[24.9%, 51.6%]), with a difference in fSp of 9.0% with 95% CI=[1.0%, 17.0%]." |
| NLR (secondary) | SSED p. 28 | "observed mean NLR was 0.047 (95% CI: 0.032, 0.062) for IUS+OA … observed mean NLR was 0.053 (95% CI: 0.037, 0.070) for IUS alone … relative NLR (the ratio in NLR for IUS+OA and IUS) was 0.896 with a 95% CI=(0.693, 1.11) which included 1 indicating that no evidence of a difference in NLR was found." |
| Re-do study limitation | SSED p. 15 | "The applicant conducted an initial MRMC reader study using the cases in the PIONEER ITD Population. Due to methodological issues, the applicant was not able to complete the submission of the final results from this study to the FDA. Subsequently, the applicant conducted the Reader-02 Pivotal Study…" |
| pma_number, date | FDA PMA listing | "PMA Number P200003"; the Approval Order is dated January 11, 2021 (per FDA PMA listing and consistent with company press release). |

### Discrepancies/notes
- The PMA approval letter (P200003A.pdf) was not directly retrieved with metadata; the 2021-01-11 decision date is verified against the GlobeNewswire/Seno press release dated 2021-01-19 and the FDA listing.
- The Neuschler 2018 *Radiology* paper covered 2,105 subjects and 7 readers (the PIONEER pivotal MRMC analysis) — this was the **first** MRMC that had methodological issues. The 2022 *Academic Radiology* paper (PMID 36475811) is the 15-reader Reader-02 analysis that matches the PMA SSED.

---

## 2. INFINITT DPS — `infinitt-dps` ⚠️ RECOMMEND DROP

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K243449 | https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243449.pdf | 2026-05-12 |

### Indication for use (verbatim, K243449 p.3)
> "INFINITT DPS is a software device intended for viewing and management of whole slide digital images derived from scanned surgical pathology slides… intended to aid trained pathologists to review and interpret these digital images for the purpose of pathology primary diagnosis."

### Why DROP recommendation
INFINITT DPS is a **whole-slide-image viewer / image management system** (product code QKQ, "Whole Slide Imaging System"). The K243449 Decision Summary contains NO AI/CAD cancer-detection function. The "Performance Testing" section (p. 5) describes only:
- Pixel-wise Color Comparison Test (CIEDE2000 ΔE₀₀ values averaged 0.00 across 30 H&E slides)
- Measurement Accuracy Test (±2% or ±5 μm for length; ±5% for area)
- Turnaround Time Test (load <5s, interaction <1s)

There is no AI algorithm, no cancer detection, no diagnostic accuracy claim, no clinical study. This is infrastructure software, not an oncology AI product. It appears on FDA AI/ML lists because the WSI product code (QKQ) is sometimes catalogued under that umbrella, but the device itself has no AI/ML feature for cancer.

### Proposed action: **EXCLUDE from registry** — flag for the curator to drop. If kept, stub-only with `data_completeness: "stub"` and `cancer_types: ["pan_cancer"]` strictly because pathology supports cancer diagnosis (not because the software has any cancer-specific function).

---

## 3. Clarius Prostate AI — `clarius-prostate-ai`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K243853 | https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243853.pdf | 2026-05-12 |

### Indication (verbatim, K243853 p.3)
> "Clarius Prostate AI is intended for semi-automatic measurements of prostate volume on ultrasound data acquired by the Clarius Ultrasound Scanner (i.e., curvilinear and endo-cavitary scanners). The user shall be a healthcare professional trained and qualified in ultrasound… Clarius Prostate AI is intended for use in adult male patients only."

### Cancer-relevance caveat
This is a **prostate-volume-measurement** AI tool, NOT a cancer-detection tool. It supports the prostate cancer workflow (PSA density calculation, biopsy planning, MR-fusion biopsy targeting all rely on prostate volume) but does not detect lesions or cancer. The 510(k) Decision Summary makes NO cancer-detection claim.

### Proposed entry (v0.2)
```json
{
  "id": "clarius-prostate-ai",
  "product_name": "Clarius Prostate AI",
  "company": "Clarius Mobile Health Corp.",
  "company_url": "https://clarius.com/",
  "cancer_types": ["prostate"],
  "modality": "radiology_us",
  "intended_use": "Semi-automatic AI-based measurement of prostate volume on ultrasound (curvilinear and endo-cavitary probes) for adult male patients. Supports prostate cancer workflow (PSA density, biopsy planning) but is NOT a lesion-detection or cancer-detection tool.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2025-04-16",
    "fda_510k_number": "K243853",
    "ldt": false,
    "ce_marked": null
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243853.pdf", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_multicenter",
    "cohort_size": {
      "n_patients": 139,
      "n_samples": 139,
      "unit_note": "139 male subjects in the clinical verification (test) study. Test dataset entirely independent of training/tuning/internal-testing datasets per FDA summary."
    },
    "n_sites": null,
    "site_geography": "multi_center_international",
    "comparator": "expert_clinicians",
    "primary_endpoint": "non_inferiority_volume_measurement",
    "primary_result": "Non-inferiority of Clarius Prostate AI prostate-volume measurement to mean of human expert reviewers met (p-value 1.146e-5, equivalence margin 22%). Mean difference of absolute percent differences (Clarius vs expert mean) 0.1192 (95% CI 0.0738, 0.1646). View prediction accuracy 95%. ICC: endo-cavitary probes (EC7 HD3) 0.87; curvilinear probes (C3 HD3) 0.67.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Ultrasound images randomly obtained from anonymized multi-center database from the United States, Canada, Peru, United Kingdom, Germany, Argentina, Jamaica, Barbados, Greece, Bulgaria, and Italy. Institutions used in training/tuning/internal testing were EXCLUDED from this study.",
      "result": "Majority of patients from US-based institutions; multiple ethnicities and ages represented per FDA summary."
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "(i) Device is for prostate VOLUME measurement only — does not detect cancer or lesions; (ii) lower ICC for curvilinear probes (0.67) vs endo-cavitary (0.87) per FDA summary 'highlighting expected variations in performance'; (iii) exact site count not disclosed; (iv) no peer-reviewed pivotal publication identified.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243853.pdf",
    "data_completeness": "partial"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| n_patients=139 | K243853 p. 9 | "Images of the prostate gland were collected and the total sample size included in the study was 139 subjects, with the majority representing patients from the United States." |
| primary_result | K243853 p. 9 | "The automated prostate volume measurement was found to be non-inferior to human experts with statistically significant results (p-value of 1.146e-5). The mean difference between percent differences of the expert mean, and the Clarius Prostate AI mean was 0.1192 (95% CI 0.0738, 0.1646)." |
| ICC | K243853 p. 9 | "The ICC scores for different probe models (i.e., C3 HD3, EC7 HD3) were 0.87 for endo-cavitary probes and 0.67 for curvilinear probes, highlighting expected variations in performance." |
| site_geography | K243853 p. 9 | "Ultrasound images were randomly obtained from an anonymized multi-center database of images from the United States, Canada, Peru, United Kingdom, Germany, Argentina, Jamaica, Barbados, Greece, Bulgaria, and Italy…" |

### Discrepancies/notes
- The K243853 Decision Summary does not enumerate the exact number of sites.
- No PubMed-indexed peer-reviewed pivotal publication identified for the AI algorithm.

---

## 4. QP-Prostate CAD — `quibim-qp-prostate`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K242683 | https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242683.pdf | 2026-05-12 |
| 4 | Company press release re: lesion-detection clearance (Mar 2025) | https://quibim.com/newsroom/news-and-press-releases/quibims-qp-prostate-cad-including-lesion-detection-and-diagnosis-capability-cleared-by-fda/ | 2026-05-12 |

### Proposed entry (v0.2)
```json
{
  "id": "quibim-qp-prostate",
  "product_name": "QP-Prostate CAD",
  "company": "Quibim S.L.",
  "company_url": "https://quibim.com/",
  "cancer_types": ["prostate"],
  "modality": "radiology_mri",
  "intended_use": "Radiological CADe/CADx software that automatically detects and identifies suspected lesions for clinically significant prostate cancer (csPCa; Gleason ≥7) on bi-parametric prostate MRI (T2w + DWI). Outputs include 3D prostate gland segmentation and DICOM overlay markings of suspected lesions in two suspicion levels (moderate/high). For physicians qualified to read and interpret prostate MRI per ACR PI-RADS recommendations. Patients above 40 years.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2025-03-18",
    "fda_510k_number": "K242683",
    "ldt": false,
    "ce_marked": true
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242683.pdf", "date_accessed": "2026-05-12"},
    {"type": "company", "url": "https://quibim.com/qp-prostate/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_multicenter",
    "cohort_size": {
      "n_patients": 228,
      "n_samples": 247,
      "unit_note": "Pivotal dataset: 228 cases collected retrospectively from multiple US centers, completely independent from training data. Standalone lesion-level analysis included N=247 lesion observations (positives + negatives from targeted biopsies plus negative cases without biopsy). MRMC: same 228 cases × 9 readers, fully crossed factorial design."
    },
    "n_sites": null,
    "site_geography": "multi_center_us",
    "comparator": "predicate_device",
    "primary_endpoint": "AUC_aided_vs_unaided",
    "primary_result": "MRMC primary endpoint: AUCunaided 0.849 (95% CI 0.814, 0.884); AUCaided 0.868 (95% CI 0.834, 0.902); ΔAUC +0.019 (95% CI 0.001, 0.038), p=0.039 — statistically significant. Standalone (lesion level): AUC-ROC 0.732 (95% CI 0.668, 0.791); sensitivity at high-suspicion marker 0.677 (95% CI 0.593, 0.761) with FPR/case 0.417; sensitivity at high+moderate markers 0.795 (95% CI 0.722, 0.861) with FPR/case 0.855.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Pivotal dataset (n=228) acquired in US at multiple centers, independent from training institutions. Demographics: age range 43–81, mean 64.7; 85.1% White, 8.3% African American, 1.3% Asian, 1.8% Other, 3.5% declined/unavailable; 3.1% Hispanic; 86.0% on 3T scanners (14.0% 1.5T); Siemens 62.3%, Philips 20.2%, GE 17.5%.",
      "result": "Subgroup analyses showed consistent performance across age (≤65, >65), BMI (<25, ≥25), race/ethnicity, and scanner vendor; minor performance deviation on 1.5T attributed to inherently lower image quality vs 3T (3T preferable when available)."
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "(i) Pivotal dataset enriched 50:50 positive:negative — not population prevalence; (ii) standalone AUC 0.732 is modest; high-+moderate-marker operating point has high FPR/case 0.855; (iii) 1.5T subgroup underperformed vs 3T; (iv) no peer-reviewed pivotal publication identified — only FDA Decision Summary and Quibim press releases.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242683.pdf",
    "data_completeness": "full"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| n_patients=228 | K242683 p. ~7 | "The pivotal dataset included 228 cases collected retrospectively from multiple centers across the US." |
| Standalone AUC | K242683 Table 2 | "AUC-ROC … 0.732 (95% CI: 0.668-0.791); Sensitivity (high suspicion marker) 0.677 (95% CI: 0.593-0.761); False Positive Rate per Case (high suspicion marker, any biopsy source) 0.417 (95% CI: 0.313-0.522)" |
| MRMC result | K242683 Table 3 | "AUCunaided 0.849 (95% CI: 0.814-0.884); AUCaided 0.868 (95% CI: 0.834-0.902); ΔAUC 0.019 (95% CI: 0.001-0.038); p-value: 0.039" |
| Comparator (predicate) | K242683 | Predicate device: "ProstatID™ (K212783)" |

### Discrepancies/notes
- No PubMed pivotal publication found for QP-Prostate CAD — only press releases and the FDA Summary.

---

## 5. Medihub Prostate — `jlk-medihub-prostate`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K233196 | https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233196.pdf | 2026-05-12 |

### Cancer-relevance caveat
JLK's marketing materials position Medihub Prostate as a prostate-cancer diagnostic AI. The cleared K233196 indication, however, is **prostate gland segmentation and volume calculation only** — the AI does not segment lesions. The Decision Summary states verbatim (p. 4): "The AI functionality is limited to assessing the total prostate volume, without segmenting lesions." This is a workflow-support tool for the prostate cancer setting, not a cancer detection tool.

### Proposed entry (v0.2)
```json
{
  "id": "jlk-medihub-prostate",
  "product_name": "Medihub Prostate",
  "company": "JLK Inc.",
  "company_url": "https://jlkgroup.com/en/",
  "cancer_types": ["prostate"],
  "modality": "radiology_mri",
  "intended_use": "Image processing software for outlining, processing, viewing, and editing of prostate MR images. AI semi-automatically outlines the prostate gland based on MRI by contour for total-volume calculation; AI functionality is limited to total prostate volume — it does not segment lesions. Edited PI-RADS report and semi-annotated prostate region are presented to user. Intended for trained radiologists and urologists. Validated for Siemens 3T Vida and Skyra MRI, slice thickness ≥3mm, patients aged 55+.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2024-06-21",
    "fda_510k_number": "K233196",
    "ldt": false,
    "ce_marked": null
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233196.pdf", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_singlecenter",
    "cohort_size": {
      "n_patients": 114,
      "n_samples": 114,
      "unit_note": "Clinical Testing (Stand-alone Performance): 114 T2 MR images from University of Missouri Hospital (single US site). Ground truth from consensus of three expert radiologists with majority-rule resolution. Reader performance subset (Phase II) used three expert radiologists."
    },
    "n_sites": 1,
    "site_geography": "single_center_us",
    "comparator": "expert_clinicians",
    "primary_endpoint": "dice_coefficient",
    "primary_result": "Standalone segmentation: mean Dice coefficient 0.928 (95% CI 0.925, 0.931); Hausdorff distance 2.171 (95% CI 1.097, 3.245), exceeding pre-specified pass criterion of mean Dice >0.894. Reader study: Dice-coefficient improvements when radiologists used Medihub Prostate were +0.156, +0.011, +0.008 for the three readers (all improved). No cancer-detection sensitivity/specificity reported (algorithm does not detect lesions).",
    "external_validation": {
      "performed": false,
      "cohort_description": "Algorithm development used Korea, US (University of Missouri Health Care), and ProstateX (open dataset). Stand-alone performance Phase I evaluation used 114 cases from University of Missouri (the same source as part of training); per FDA Decision Summary the 'Study Population Dataset is the same as algorithm development dataset' split 9:1 into Train/Validate + Test. This is internal test set splitting rather than truly external validation.",
      "result": null
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "(i) AI is for prostate-gland volume/segmentation only — does NOT detect or segment lesions; (ii) test set comes from same institutional source as training data ('Study Population Dataset is the same as algorithm development dataset'), so this is internal validation, not true external; (iii) only validated for Siemens 3T Vida and Skyra; (iv) only tested in patients aged 55+ (114/114 male); (v) no peer-reviewed pivotal publication identified; (vi) only 7 African American and 1 Asian subject in test set — very limited racial diversity.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233196.pdf",
    "data_completeness": "partial"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| AI scope | K233196 p. 4 | "The AI functionality is limited to assessing the total prostate volume, without segmenting lesions." |
| n_patients=114 | K233196 p. 5–6 | "Based on a total of 114 T2 MR images (University of Missouri Hospital) the final validity evaluation was performed on prostate region segmentation ground truth produced by three expert radiologists." |
| Dice result | K233196 p. 6 | "The clinical testing results demonstrated that the overall Dice coefficient and Hausdorff distance were 0.928 and 2.171, respectively, with the 95% confidence intervals for these measurements being [0.925, 0.931] for the Dice coefficient and [1.097, 3.245] for the Hausdorff distance." |
| Reader improvement | K233196 p. 7 | "The improvements in the Dice coefficient for prostate outlining performance for the three radiologists when using the prostate region segmentation algorithm of MEDIHUB-PROSTATE were 0.156, 0.011, and 0.008, respectively." |

### Discrepancies/notes
- JLK press materials describe Medihub Prostate as a "prostate cancer diagnostic AI" but the cleared FDA indication is segmentation/volume, not cancer detection.
- True external validation absent.

---

## 6. Quantib Prostate — `quantib-prostate`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K230772 (Special 510(k), v3.0) | https://www.accessdata.fda.gov/cdrh_docs/pdf23/K230772.pdf | 2026-05-12 |
| 1 | Peer-reviewed: Chiacchio et al., "The added value of artificial intelligence using Quantib Prostate for the detection of prostate cancer at multiparametric magnetic resonance imaging." *La Radiologia Medica* 2025. | https://pubmed.ncbi.nlm.nih.gov/40332649/ | 2026-05-12 |
| 1 | Peer-reviewed: Faiella et al., "Quantib Prostate Compared to an Expert Radiologist for the Diagnosis of Prostate Cancer on mpMRI: A Single-Center Preliminary Study." *Diagnostics* 2022. | https://pmc.ncbi.nlm.nih.gov/articles/PMC9415513/ | 2026-05-12 |

### Cancer-relevance caveat
The cleared K230772 indication is image post-processing, viewing, segmentation, and PI-RADS structured workflow support. The AI function in v3.0 is **prostate (sub-region) segmentation + image registration**. The FDA performance section discloses only bench tests (Dice / mean surface distance) plus a qualitative Likert-scale radiologist scoring for the new subregion-segmentation feature — no cancer-detection sensitivity/specificity. Peer-reviewed papers have evaluated Quantib Prostate's added value for csPCa detection by reader assistance, with mixed results.

### Proposed entry (v0.2)
```json
{
  "id": "quantib-prostate",
  "product_name": "Quantib Prostate",
  "company": "Quantib BV",
  "company_url": "https://www.quantib.com/",
  "cancer_types": ["prostate"],
  "modality": "radiology_mri",
  "intended_use": "Image post-processing software for processing, visualization, and editing of prostate MRI images. Supports registered multi-parametric MRI viewing, semi-automatic AI-based segmentation of anatomical structures (prostate gland and sub-regions), volume computations, manual editing tools, and PI-RADS structured workflow. Diagnosis should not be made solely based on Quantib Prostate analysis.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k_special",
    "fda_decision_date": "2023-04-17",
    "fda_510k_number": "K230772",
    "ldt": false,
    "ce_marked": true
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf23/K230772.pdf", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://pubmed.ncbi.nlm.nih.gov/40332649/", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9415513/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_singlecenter",
    "cohort_size": {
      "n_patients": null,
      "n_samples": null,
      "unit_note": "FDA Special 510(k) bench testing only — sample size for the subregion-segmentation Dice/MSD comparison not disclosed in the public Decision Summary. Predicate clinical performance (Quantib Prostate v2.0, K221106) was leveraged. Peer-reviewed Chiacchio 2025 in La Radiologia Medica and Faiella 2022 in Diagnostics provide independent real-world csPCa detection cohorts (curator should populate full cohort sizes from those full texts)."
    },
    "n_sites": null,
    "site_geography": null,
    "comparator": "predicate_device",
    "primary_endpoint": "dice_coefficient",
    "primary_result": "FDA K230772 bench testing: automatic segmentations compared to ground truth via Dice overlap and Mean Surface Distance; results stated 'as safe and effective as the predicate device'. Quantitative Dice/MSD values not disclosed in the public Decision Summary text. Qualitative reader Likert scoring concluded sub-region segmentations and ROI initial localizations 'are judged at least as accurate as the predicate device'.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Independent external evaluations exist in peer-reviewed literature. Per Chiacchio 2025 (La Radiologia Medica), Quantib did not enhance csPCa detection in experienced readers but did improve performance for inexperienced readers; Faiella 2022 reported inter-reader agreement (weighted κ ≈ 0.45–0.46) and shorter reporting time with Quantib.",
      "result": "Mixed real-world evidence: benefit appears concentrated in less-experienced readers."
    },
    "peer_reviewed": true,
    "key_publications": [
      {
        "title": "The added value of artificial intelligence using Quantib Prostate for the detection of prostate cancer at multiparametric magnetic resonance imaging",
        "journal": "La Radiologia Medica",
        "year": 2025,
        "url": "https://pubmed.ncbi.nlm.nih.gov/40332649/",
        "pivotal": false
      },
      {
        "title": "Quantib Prostate Compared to an Expert Radiologist for the Diagnosis of Prostate Cancer on mpMRI: A Single-Center Preliminary Study",
        "journal": "Diagnostics",
        "year": 2022,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9415513/",
        "pivotal": false
      }
    ],
    "limitations_noted": "(i) K230772 is a Special 510(k) — relies heavily on predicate K221106 for clinical performance; current Decision Summary discloses bench only; (ii) no MRMC reader study or AUC/sensitivity/specificity metrics in K230772 public summary; (iii) peer-reviewed evidence mixed — benefit may be limited to less-experienced readers; (iv) curator should review prior predicate K221106 / K202501 for full historical clinical metrics.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf23/K230772.pdf",
    "data_completeness": "partial"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| Indication | K230772 p. 3 | "Quantib Prostate is image post-processing software that provides the user with processing, visualization, and editing of prostate MRI images. … The software can be used for semi-automatic segmentation of anatomical structures and provides volume computations…" |
| Bench-only PD | K230772 §7.2 | "Bench testing of the software was done to show that the system is suitable for its intended use and to evaluate the stand-alone performance of the sub-region segmentation algorithm. This was done by comparing the automatic segmentations to their ground truth and calculating the Dice overlap and Mean Surface Distance." |
| Likert clinical | K230772 §7.2 | "Radiologists were asked to score the sub-region segmentations and ROI initial localizations using a 5-point Likert scale. It is concluded that sub-regions and ROI localizations are judged at least as accurate as the predicate device was." |

### Discrepancies/notes
- Special 510(k) defers extensively to predicate K221106; for fully populated v0.2 metrics, the curator should pull the predicate's Decision Summary (K221106) and earlier K202501.

---

## 7. Avenda Health AI Prostate Cancer Planning Software — `avenda-prostate-cancer-planning`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K221624 | https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221624.pdf | 2026-05-12 |
| 1 | Priester A et al., "Artificial Intelligence Improves the Ability of Physicians to Identify Prostate Cancer Extent." *Journal of Urology* 2024;212(1):104-114. PMID 38860576. | https://pubmed.ncbi.nlm.nih.gov/38860576/ | 2026-05-12 |
| 1 | Priester A et al., "Prediction and Mapping of Intraprostatic Tumor Extent with Artificial Intelligence." *Eur Urol Open Sci* 2023. PMID 37545845. | https://pubmed.ncbi.nlm.nih.gov/37545845/ | 2026-05-12 |

### Proposed entry (v0.2)
```json
{
  "id": "avenda-prostate-cancer-planning",
  "product_name": "Avenda Health AI Prostate Cancer Planning Software",
  "company": "Avenda Health, Inc.",
  "company_url": "https://avendahealth.com/",
  "cancer_types": ["prostate"],
  "modality": "radiology_mri",
  "intended_use": "AI-based decision-support adjunct to MRI + biopsy review for the prostate oncological workflow. Lesion characterization functions intended for use on patients with pathology-confirmed Gleason Grade Group (GGG) ≥ 2 lesion and biopsy coordinates uploaded — used to evaluate the extent of known disease. The device generates a 3D voxel-level cancer probability map and an Encapsulation Confidence Score for clinician-selected boundaries. Supports treatment-planning (biopsy, focal soft-tissue ablation). Also functions as a medical image viewer (3D-visualization, comparison) for prostate MRI. Marketed commercially as Unfold AI.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2022-11-22",
    "fda_510k_number": "K221624",
    "ldt": false,
    "ce_marked": null
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221624.pdf", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://pubmed.ncbi.nlm.nih.gov/38860576/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_multicenter_mrmc",
    "cohort_size": {
      "n_patients": 50,
      "n_samples": 50,
      "unit_note": "FDA MRMC reader study used a whole-mount prostatectomy database of GGG 2-3 patients (representative of intended-use population). Each whole-mount sample included 3D surfaces and pathology labels registered to preoperative T2-weighted MRI. 10 practicing urologists or radiologists from different institutions (range 2–23 years of experience). Each reader reviewed each case. Standalone segmentation test set: 137 patients (prostate segmentation); 50 patients (whole-mount pathology lesion-contouring accuracy)."
    },
    "n_sites": 5,
    "site_geography": "multi_center_us",
    "comparator": "standard_of_care_clinicians",
    "primary_endpoint": "sensitivity_specificity_lesion_contouring",
    "primary_result": "Reader study (lesion contours vs whole-mount pathology ground truth): Sensitivity mean 97.4% (with device) vs 38.2% (SOC), p<0.0001; Specificity mean 72.1% (with device) vs 53.4% (hemi-gland contours), p<0.0001; Balanced accuracy 84.7% (device) vs 67.2% (SOC) vs 75.9% (hemi-gland), p<0.0001; Complete csPCa encapsulation rate 72.8% (device) vs 1.6% (SOC), p<0.0001; clinical-quality rating: 99% device vs 60% hemi-gland (p<0.0001).",
    "external_validation": {
      "performed": true,
      "cohort_description": "Reader-study cases were independent of training set per FDA summary. The peer-reviewed J Urol 2024 paper (Priester et al.) used a 50-case prostatectomy whole-mount cohort retrospectively eligible for focal therapy; 7 urologists + 3 radiologists from 5 institutions, experience 2–23 years.",
      "result": "Concordant with FDA summary results: AI assistance improved encapsulation accuracy ~45× vs SOC."
    },
    "peer_reviewed": true,
    "key_publications": [
      {
        "title": "Artificial Intelligence Improves the Ability of Physicians to Identify Prostate Cancer Extent",
        "journal": "Journal of Urology",
        "year": 2024,
        "url": "https://pubmed.ncbi.nlm.nih.gov/38860576/",
        "pivotal": true
      },
      {
        "title": "Prediction and Mapping of Intraprostatic Tumor Extent with Artificial Intelligence",
        "journal": "European Urology Open Science",
        "year": 2023,
        "url": "https://pubmed.ncbi.nlm.nih.gov/37545845/",
        "pivotal": false
      }
    ],
    "limitations_noted": "(i) Indication is restricted to patients with pathology-confirmed GGG ≥ 2 lesion AND biopsy-coordinate upload — NOT a screening or unaided detection tool; (ii) test cohort 50 patients is small; (iii) predicate is QuantX (DEN170022) but Avenda is the first FDA device specifically for prostate cancer extent mapping; (iv) ground truth is whole-mount prostatectomy — generalizability to patients NOT going to prostatectomy not established; (v) reader pool included urologists in addition to radiologists, broader than typical radiology MRMC.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221624.pdf",
    "data_completeness": "full"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| Indication | K221624 p. 3 | "The Avenda Health AI Prostate Cancer Planning Software's lesion characterization functions are intended for use on patients with a pathology-confirmed Gleason Grade Group (GGG) ≥ 2 lesion and for whom corresponding biopsy coordinate information have been uploaded." |
| 10 readers, 5 institutions | K221624 p. 6 + Priester 2024 | "Ten practicing urologists or radiologists from different institutions with a range of experience levels (2 to 23 years…)"; Priester 2024 specifies 7 urologists + 3 radiologists from 5 institutions. |
| Standalone test sets | K221624 p. 6 | "the prostate segmentation algorithm has been determined to accurately segment the prostate organ in T2-weighted MRI in a standalone test set of 137 patients. Furthermore, the lesion contouring algorithm has been validated for accuracy in contouring GGG ≥2 lesions in the intended use population within a representative, independent whole mount pathology dataset of N=50 patients." |
| Reader study results | K221624 p. 6–7 | "lesion contours produced using the Proposed Device had superior sensitivity (mean 97.4% vs 38.2%, p < 0.0001) compared to SOC contours and superior specificity compared to hemi-gland contours (mean 72.1% vs 53.4%, p < 0.0001). … balanced accuracy (mean 84.7% vs 67.2% & 75.9% respectively, p < 0.0001) and 'clinical quality' (in 99% and 60% of cases respectively, p < 0.0001). On average, the readers achieved a complete csPCa encapsulation rate of 72.8% with the Proposed Device, and only 1.6% with SOC methods (p < 0.0001)." |

---

## 8. AVIEW Lung Nodule CAD — `coreline-aview-lung-nodule`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K251203 (most recent, software v2.0; minor change) | https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251203.pdf | 2026-05-12 |
| 1 | FDA 510(k) Decision Summary K221592 (predicate, original clinical validation) | https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221592.pdf | 2026-05-12 |

### Note on the 510(k) update
K251203 (December 2025) is a UI/icon/operating-environment update with no algorithm change. The substantive clinical and standalone validation data live in K221592 (the predicate), which the current 510(k) explicitly defers to. The proposed entry uses the latest decision date (2025-12-03, K251203) for regulatory metadata but cites K221592 metrics for validation.

### Proposed entry (v0.2)
```json
{
  "id": "coreline-aview-lung-nodule",
  "product_name": "AVIEW Lung Nodule CAD",
  "company": "Coreline Soft Co., Ltd.",
  "company_url": "https://www.corelinesoft.com/en/",
  "cancer_types": ["lung"],
  "modality": "radiology_ct",
  "intended_use": "Computer-Aided Detection (CAD) software designed to assist radiologists in the detection of pulmonary nodules (diameter 3–20 mm) during the review of CT examinations of the chest for asymptomatic populations. Adjunctive second-reader after the radiologist's initial read. Validated using non-contrast chest CT.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2025-12-03",
    "fda_510k_number": "K251203",
    "ldt": false,
    "ce_marked": true
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251203.pdf", "date_accessed": "2026-05-12"},
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221592.pdf", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_multicenter_mrmc",
    "cohort_size": {
      "n_patients": 151,
      "n_samples": 282,
      "unit_note": "MRMC reader study (K221592): 151 chest CTs (103 negative controls + 48 cases with one or more lung nodules); 11 board-certified radiologists, blinded, 4-week washout between unaided and AI-aided reads. Standalone study: 282 chest CTs (140 with nodule data + 142 without) from three geographically distinct US clinical sites; gender split 132M/150F. K251203 (2025) is a UI-only minor change with no new clinical study."
    },
    "n_sites": 3,
    "site_geography": "multi_center_us",
    "comparator": "unaided_reader",
    "primary_endpoint": "AUC_aided_vs_unaided",
    "primary_result": "MRMC: AUC 0.73 (unaided, 95% CI 0.66–0.79) vs 0.92 (aided, 95% CI 0.89–0.95), Δ=0.19; Sensitivity 0.68 (unaided, 95% CI 0.62–0.73) vs 0.91 (aided, 95% CI 0.89–0.94), Δ=0.23; FP/scan 0.48 (unaided, 95% CI 0.28–0.69) vs 0.28 (aided, 95% CI 0.15–0.42), Δ improvement 0.24. Standalone: AUC 0.961 (95% CI 0.939–0.983); Sensitivity 0.907 (95% CI 0.846–0.95); Specificity 0.704 (95% CI 0.622–0.778); Sensitivity at FP/scan<2: 0.889 (95% CI 0.849–0.93) at FP/scan=0.504.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Standalone test set sourced from three geographically distinct US clinical sites; anonymized medical data purchased separately from any training or internal validation data per K221592 Decision Summary. Both screening and incidental populations included.",
      "result": "Subgroup analyses performed for challenging/confounding cases per K221592; consistent performance."
    },
    "peer_reviewed": true,
    "key_publications": [
      {
        "title": "Outstanding negative prediction performance of solid pulmonary nodule volume AI for ultra-LDCT baseline lung cancer screening risk stratification",
        "journal": "Lung Cancer",
        "year": 2022,
        "url": "https://pubmed.ncbi.nlm.nih.gov/35123156/",
        "pivotal": false
      }
    ],
    "limitations_noted": "(i) Nodule diameter range 3–20 mm — does not cover sub-3mm or >20mm nodules; (ii) validated using non-contrast CT only; (iii) MRMC cohort enriched (48 positives / 103 negatives) is not population-prevalence representative; (iv) K251203 is a UI-only change — no new clinical data submitted; (v) Lung Cancer 2022 paper is an independent real-world Moscow Lung Cancer Screening evaluation, not the pivotal trial.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221592.pdf",
    "data_completeness": "full"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| MRMC design | K221592 §8.1 | "A HIPAA-compliant multi-case, multi-reader, retrospective study design… a dataset of 151 Chest CTs with 103 negative controls and 48 cases with one or more lung nodules… eleven board-certified radiologists interpreted the same cases unassisted, followed by AI assistance after randomization and a 4-week washout period." |
| MRMC results | K221592 §8.1 table | "AUC 0.73 (0.66–0.79) Unaided / 0.92 (0.89–0.95) Aided; Sensitivity 0.68 (0.62–0.73) Unaided / 0.91 (0.89–0.94) Aided; FP/scan 0.48 (0.28–0.69) Unaided / 0.28 (0.15–0.42) Aided" |
| Standalone | K221592 §8.2.2 | "Dataset are collected from three geographically distinct US clinical sites. The total number of data is 282 (140 cases with nodule data and 142 cases without nodule data). … Overall AUC (with CI): 0.961(0.939-0.983); Overall Sensitivity (with CI): 0.907(0.846-0.95); Overall Specificity (with CI): 0.704(0.622-0.778)" |

---

## 9. Lung AI (LAI001) — `exo-lung-ai` ⚠️ RECOMMEND DROP

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K243239 | https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243239.pdf | 2026-05-12 |

### Indication (verbatim, K243239 p. 3)
> "Lung AI software device is a Computer-Aided Detection (CADe) tool designed to assist in the detection of **consolidation/atelectasis and pleural effusion** during the review of **lung ultrasound** scans. … Lung AI is intended to be used on images collected from the PLAPS point, in accordance with the **BLUE protocol** … intended users are healthcare professionals who … perform lung ultrasounds as part of their current practice in a point-of-care environment — namely Emergency Medicine. … Lung AI is not intended for clinical diagnosis and does not replace the healthcare provider's judgment or other diagnostic tests in the standard care for lung ultrasound findings. All cases where a Chest CT scan and/or Chest X-ray is part of the standard of care should undergo these imaging procedures, irrespective of the device output."

### Why DROP recommendation
Exo Lung AI is a **point-of-care lung ultrasound** device that detects **consolidation/atelectasis and pleural effusion** in **emergency medicine** contexts. It does NOT detect cancer, lung nodules, or any cancer-related target. Grep of the entire 22,810-character extracted text for "cancer", "tumor", "nodule", "oncolog", or "malignan" returns zero hits.

This product is on the FDA AI/ML list because lung ultrasound is broadly catalogued under thoracic imaging — but it has zero oncology relevance.

### Proposed action: **EXCLUDE from registry**. Flag for the curator to drop from the FDA-gap candidate list.

---

## 10. V5med Lung AI — `v5med-lung-ai`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K242919 | https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242919.pdf | 2026-05-12 |

### Proposed entry (v0.2)
```json
{
  "id": "v5med-lung-ai",
  "product_name": "V5med Lung AI",
  "company": "V5med Inc.",
  "company_url": null,
  "cancer_types": ["lung"],
  "modality": "radiology_ct",
  "intended_use": "Computer-Aided Detection (CAD) software designed to assist radiologists in detecting pulmonary nodules (diameter 4–30 mm) during chest CT examinations. Concurrent-read mode (AI analysis results displayed alongside the original CT images during both the initial review and any subsequent reads). Does not replace radiologist judgment.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2025-03-27",
    "fda_510k_number": "K242919",
    "ldt": false,
    "ce_marked": null
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242919.pdf", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_multireader_multicase",
    "cohort_size": {
      "n_patients": 340,
      "n_samples": 340,
      "unit_note": "Pivotal reader study (retrospective fully crossed MRMC): 16 board-certified radiologists × 340 chest CT scans (mix of screening and non-screening). All screening cases drawn from NLST CT arm. Age range 55–77 (mean 62). 41.1% male / 58.9% female. Race: 92.8% White, 4.4% Black, 2.2% Asian, 0.3% Pacific Islander, 0.3% Indian."
    },
    "n_sites": null,
    "site_geography": "multi_center_us",
    "comparator": "unaided_reader",
    "primary_endpoint": "AUC_LROC_aided_vs_unaided",
    "primary_result": "MRMC pivotal study: AUC unaided 0.734, aided 0.830; Δ (Aided − Unaided) = +0.0959 (95% CI 0.0586, 0.1332). Reading time: 113.0 s unaided vs 115.9 s aided; difference reported as -17.1 (95% CI -26.7, -9.0), i.e., a ~13% reduction (NB: the SSED table appears to show aided slightly longer than unaided, but the calculated difference is reported as a 17.1 s reduction — see Discrepancies). All endpoints met acceptance criteria. Standalone testing showed 'similar nodule detection sensitivity compared to those of the predicate device' (AVIEW K221592) — exact metrics not disclosed.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Screening cases sourced from the National Lung Screening Trial (NLST) CT arm. Population demographics with broad age (55–77) and racial diversity reported.",
      "result": "Statistically significant AUC improvement (+0.0959) and statistically significant decrease in reading time."
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "(i) Standalone metrics not disclosed in K242919 public summary — only relative-to-predicate language; (ii) Site count not disclosed; (iii) reading-time numbers in the FDA table appear inconsistent with the stated difference — possible typographic error in the SSED (unaided reported as 113.0s, aided as 115.9s, but the reported 'difference' is -17.1s); (iv) no peer-reviewed pivotal publication identified; (v) racial diversity skewed (92.8% White) reflecting NLST source population.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242919.pdf",
    "data_completeness": "partial"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| Cohort | K242919 p. 6 | "A total of sixteen board-certified radiologists and a dataset of 340 chest CT scans were involved in the reader study including both screening and non-screening populations. All screening cases were acquired from NLST CT arm." |
| Primary result | K242919 p. 7 | "Readers benefited from using V5med Lung AI, demonstrating a significant increase in the AUC (Aided-Unaided: 0.0959, 95%CI: (0.0586, 0.1332)) and a significant decrease in reading time from 133.0 seconds unaided to 115.9 seconds, yielding a time difference (Aided- Unaided: -17.1, 95% CI: (-26.7, -9.0)), a 13% improvement." |
| Standalone | K242919 p. 6 | "Standalone performance testing, which included chest CT scans from lung cancer screening population and non-screening population, was conducted to validate detection accuracy of V5med Lung AI. Results showed that V5med Lung AI had similar nodule detection sensitivity compared to those of the predicate device." |

### Discrepancies/notes
- The K242919 text reports "reading time from 133.0 seconds unaided to 115.9 seconds" but the table immediately below states "Unaided 113.0, Aided 115.9". This is an internal inconsistency in the FDA Summary — curator should flag.

---

## 11. Auto Lung Nodule Detection — `samsung-auto-lung-nodule`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K201560 | https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201560.pdf | 2026-05-12 |
| 4 | Samsung/NeuroLogica press release (Oct 2021) | https://www.itnonline.com/content/samsung-receives-fda-clearance-ai-algorithms-detect-lung-nodules-chest-x-rays | 2026-05-12 |

### IMPORTANT modality correction
The candidate-list table proposes `modality: radiology_ct`, but K201560 is for **chest X-ray** (PA radiographs), NOT CT. The cleared indication explicitly states: "PA chest radiographs of adults" and the device is integrated into Samsung Digital X-ray Imaging systems. Use `modality: radiology_xray`.

### Proposed entry (v0.2)
```json
{
  "id": "samsung-auto-lung-nodule",
  "product_name": "Auto Lung Nodule Detection",
  "company": "Samsung Electronics Co., Ltd.",
  "company_url": "https://www.samsunghealthcare.com/",
  "cancer_types": ["lung"],
  "modality": "radiology_xray",
  "intended_use": "Computer-aided detection (CADe) software to identify and mark regions in relation to suspected pulmonary nodules 10–30 mm in size on posterior-anterior (PA) chest radiographs of adults. Designed as a second reader, integrated into S-Station operation software on Samsung Digital X-ray Imaging systems. Not intended for patients with lung lesions other than abnormal nodules.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2021-08-31",
    "fda_510k_number": "K201560",
    "ldt": false,
    "ce_marked": null
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201560.pdf", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective_multireader_multicase",
    "cohort_size": {
      "n_patients": null,
      "n_samples": null,
      "unit_note": "K201560 Decision Summary describes design (multi-reader retrospective study using normal + diseased chest radiographs, sensitivity/FPPI/JAFROC FOM endpoints) but DOES NOT disclose quantitative N, sensitivity, specificity, or AUC. Press release indicates approval was 'based on a sensitivity of 80% or more' and study was conducted across Freiburg University Hospital, Massachusetts General Hospital, Samsung Medical Center, and Severance Hospital with 600 lung-cancer chest radiographs + 200 normals."
    },
    "n_sites": 4,
    "site_geography": "multi_center_international",
    "comparator": "unaided_reader",
    "primary_endpoint": "JAFROC_figure_of_merit",
    "primary_result": "K201560 Decision Summary: 'all readers' nodule detection performances using the proposed device have increased with statistical significance.' Specific quantitative metrics NOT disclosed in the FDA Decision Summary. Press materials cite ≥80% sensitivity acceptance criterion.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Per Samsung/NeuroLogica press materials: '600 chest radiographs with lung cancer and 200 normal chest radiographs' from Freiburg University Hospital (Germany), Massachusetts General Hospital (US), Samsung Medical Center (Korea), and Severance Hospital (Korea) — multi-national external evaluation.",
      "result": "Sensitivity stated by Samsung press as ≥80% (acceptance criterion); specific multi-center breakdown not in FDA summary."
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "(i) Modality is chest X-RAY (PA radiograph), NOT CT — important distinction from CT-based lung nodule CADs; (ii) limited to nodules 10–30 mm; (iii) FDA Decision Summary does not disclose quantitative validation metrics — only narrative claim of statistical significance; (iv) press-release-sourced metrics are Tier 4 and should not be treated as primary numbers; (v) no peer-reviewed pivotal publication identified; (vi) device tightly coupled to Samsung Digital X-ray Imaging systems / S-Station — not modality-agnostic.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201560.pdf",
    "data_completeness": "partial"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| Indication (PA X-ray) | K201560 p. 3 | "The Auto Lung Nodule Detection is computer-aided detection software to identify and mark regions in relation to suspected pulmonary nodules from 10 to 30 mm in size. It is designed to aid the physician to review the PA chest radiographs of adults as a second reader…" |
| Study design | K201560 §11.B | "Nodule detection performances before and after ALND were measured via sensitivity, false positives per image (FPPI), and jackknife alternative free response receiver operating characteristic (JAFROC) figure of merit (FOM). The results have demonstrated that all readers' nodule detection performances using the proposed device have increased with statistical significance." |
| Multi-site (Tier 4) | Samsung press / ITN article | "Investigators at Freiburg University Hospital, Freiburg, Germany; Massachusetts General Hospital, Boston, Massachusetts; Samsung Medical Center, Seoul, South Korea; and Severance Hospital, Seoul, South Korea — retrospectively identified 600 chest radiographs with lung cancer and 200 normal chest radiographs." |

### Discrepancies/notes
- Modality must be corrected from candidate list's `radiology_ct` → `radiology_xray`.
- Quantitative metrics not in primary FDA source — `data_completeness: "partial"`.

---

## 12. Lung Vision System — `body-vision-lung`

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K183593 (Adobe PDF Portfolio; embedded summary extracted) | https://www.accessdata.fda.gov/cdrh_docs/pdf18/K183593.pdf | 2026-05-12 |
| 1 | Pertzov B et al., "The LungVision navigational platform for peripheral lung nodule biopsy and the added value of cryobiopsy." *Thoracic Cancer* 2021 Jul;12(13):2007-2015. PMID 34096182. | https://pubmed.ncbi.nlm.nih.gov/34096182/ | 2026-05-12 |
| 1 | Pritchett MA et al., "Prospective Analysis of a Novel Endobronchial Augmented Fluoroscopic Navigation System for Diagnosis of Peripheral Pulmonary Lesions." *J Bronchology Interv Pulmonol* 2021. PMID 32732491. | https://pubmed.ncbi.nlm.nih.gov/32732491/ | 2026-05-12 |

### Proposed entry (v0.2)
```json
{
  "id": "body-vision-lung",
  "product_name": "LungVision System",
  "company": "Body Vision Medical Ltd.",
  "company_url": "https://www.bodyvisionmedical.com/",
  "cancer_types": ["lung"],
  "modality": "radiology_ct",
  "intended_use": "Image navigation and guidance system that enables segmentation of previously acquired 3D CT datasets and overlay/registration of these 3D segmented data sets with fluoroscopic live X-ray images of the same anatomy in order to support catheter/device navigation during pulmonary procedures (i.e., bronchoscopic biopsy of peripheral pulmonary lesions suspicious for cancer). Uses AI-driven augmented fluoroscopy and image fusion.",
  "regulatory": {
    "fda_status": "510(k) cleared",
    "fda_pathway": "510k",
    "fda_decision_date": "2019-04-18",
    "fda_510k_number": "K183593",
    "ldt": false,
    "ce_marked": null
  },
  "deployment": {"available": true, "fda_cleared": true},
  "sources": [
    {"type": "fda_db", "url": "https://www.accessdata.fda.gov/cdrh_docs/pdf18/K183593.pdf", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://pubmed.ncbi.nlm.nih.gov/34096182/", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://pubmed.ncbi.nlm.nih.gov/32732491/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "prospective_singlecenter",
    "cohort_size": {
      "n_patients": 63,
      "n_samples": 63,
      "unit_note": "Pertzov 2021 prospective single-center (Rabin Medical Center, Israel; January 2016 – August 2020): 63 procedures performed with LungVision navigation for peripheral pulmonary nodule biopsy; median lesion size 25.0 mm. Pritchett 2021 multicenter prospective study of augmented-fluoroscopic navigation reported a separate cohort (index-procedure yield 78.4%, 12-month diagnostic accuracy 88.2%)."
    },
    "n_sites": 1,
    "site_geography": "single_center_international",
    "comparator": "historical_controls",
    "primary_endpoint": "diagnostic_yield",
    "primary_result": "Pertzov 2021: overall diagnostic yield 81.8%; for lesions <20 mm, 72.2%. In 9 cases, transbronchial cryobiopsy yielded malignant tissue not found in other sampling tools. Complications: 1 pneumothorax requiring chest tube; no other major complications. Pritchett 2021: index-procedure diagnostic yield 78.4%; 12-month follow-up diagnostic accuracy 88.2%.",
    "external_validation": {
      "performed": false,
      "cohort_description": "Pertzov 2021 is single-center (Rabin, Israel). Pritchett 2021 is a separate multicenter prospective cohort but not formally external to the device manufacturer.",
      "result": null
    },
    "peer_reviewed": true,
    "key_publications": [
      {
        "title": "The LungVision navigational platform for peripheral lung nodule biopsy and the added value of cryobiopsy",
        "journal": "Thoracic Cancer",
        "year": 2021,
        "url": "https://pubmed.ncbi.nlm.nih.gov/34096182/",
        "pivotal": true
      },
      {
        "title": "Prospective Analysis of a Novel Endobronchial Augmented Fluoroscopic Navigation System for Diagnosis of Peripheral Pulmonary Lesions",
        "journal": "Journal of Bronchology & Interventional Pulmonology",
        "year": 2021,
        "url": "https://pubmed.ncbi.nlm.nih.gov/32732491/",
        "pivotal": true
      }
    ],
    "limitations_noted": "(i) FDA Decision Summary K183593 contains only bench/engineering tests (ANSI/AAMI 60601-1, pig-lung deformable-tissue testing) — no clinical metrics; clinical evidence comes from peer-reviewed publications, not the FDA summary; (ii) Pertzov cohort is single-center and small (n=63); (iii) diagnostic yield is an interventional pulmonology outcome, not a typical 'AI sensitivity/specificity' — comparator class is different from screening/detection AIs; (iv) device is procedural-guidance — does not detect cancer, but guides biopsy of presumed-cancer lesions.",
    "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf18/K183593.pdf",
    "data_completeness": "partial"
  }
}
```

### Field-by-field provenance
| Field | Source | Verbatim quote |
|-------|--------|----------------|
| Indication | K183593 510k Summary p. 2 | "The LungVision System is intended to enable users to segment previously acquired 3D CT datasets and overlay and register these 3D segmented data sets with fluoroscopic live X-ray images of the same anatomy in order to support catheter/device navigation during pulmonary procedures." |
| Pertzov cohort | Thoracic Cancer 2021 (PMID 34096182) abstract | "Sixty-three procedures were performed with a median lesion size of 25.0 mm. The diagnostic yield overall was 81.8% and for lesions smaller than 20 mm was 72.2%. In nine cases the transbronchial cryobiopsy showed tissue with malignant cells that were not found in any other biopsy material taken with other sampling tools." |
| Pritchett 2021 | J Bronchology Interv Pulmonol 2021 (PMID 32732491) | Diagnostic yield at index procedure 78.4%; 12-month diagnostic accuracy 88.2%. |
| K183593 PD scope | K183593 §Nonclinical / Bench | "We have performed bench tests and found that the LungVision met all requirements… Testing has also been performed with pig lungs to test accuracy in deformable tissue." |

### Discrepancies/notes
- K183593 is delivered as an Adobe PDF Portfolio (3 embedded files: 510(k) Summary, IFU, SE Letter). pdftotext-of-portfolio returns the "open in Acrobat" placeholder; the actual summary was extracted via PyMuPDF embfile extraction.

---

## 13. Lung Density Analysis — `imbio-lung-density` ⚠️ RECOMMEND DROP

### Sources consulted
| Tier | Source | URL | Accessed |
|------|--------|-----|----------|
| 1 | FDA 510(k) Decision Summary K141069 (extraction problematic — see notes) | https://www.accessdata.fda.gov/cdrh_docs/pdf14/K141069.pdf | 2026-05-12 |
| 3 | Imbio product page (Lung Density Analysis) | https://www.imbio.com/products/lung-density-analysis-inspiration/ | 2026-05-12 |

### Indication (verbatim, K141069)
> "The Imbio CT Lung Density Analysis Software provides reproducible CT values for pulmonary tissue, which is essential for providing quantitative support for diagnosis and follow up examinations. The Imbio CT Lung Density Analysis Software can be used to support the physician in the diagnosis and documentation of pulmonary tissue images (e.g., abnormalities) from CT thoracic datasets. Three-D segmentation and isolation of sub-compartments, volumetric analysis, density evaluations and reporting tools are provided."

### Why DROP recommendation
Imbio's Lung Density Analysis software is intended for **quantification of low-attenuation lung tissue (emphysema)** and pulmonary tissue density — primarily for **COPD, asthma, bronchiolitis obliterans syndrome**, and incidental-finding quantification on lung cancer screening LDCT. Per Imbio's product page: "LDAi provides fully-automated detection, visualization and quantification of areas of low attenuation (LAA) which can be indicative of emphysema and is validated for use with low-dose CT scans as a component of lung cancer screening programs." The indication and primary clinical application are **not cancer detection**. Mentions of "cancer", "nodule", "tumor", or "malignan" do not appear in the K141069 Decision Summary text. The product is on FDA radiologic-software lists but does not detect or diagnose cancer.

There is a tangential link (emphysema quantification is sometimes reported in lung cancer screening LDCT alongside Lung-RADS), but the device itself does not address oncology endpoints.

### Proposed action: **EXCLUDE from registry**. Flag for the curator. If retained for screening-workflow completeness, mark `data_completeness: "stub"` and note that the device is COPD/emphysema-focused.

### Note on extraction
The K141069 PDF used heavily-substituted font glyphs in its 510(k) summary section that pdftotext could not decode (text shows non-ASCII placeholders). Indication text was recoverable from the clean Form 3881 indication page. Quantitative validation metrics (if any) could not be extracted from the substituted-font portion; a curator with Acrobat OCR access can verify.

---

# SUMMARY

## Data-completeness counts (proposed entries)
| Completeness | Count | Items |
|--------------|-------|-------|
| `full` | 4 | seno-imagio-breast (1), quibim-qp-prostate (4), avenda-prostate-cancer-planning (7), coreline-aview-lung-nodule (8) |
| `partial` | 6 | clarius-prostate-ai (3), jlk-medihub-prostate (5), quantib-prostate (6), v5med-lung-ai (10), samsung-auto-lung-nodule (11), body-vision-lung (12) |
| `stub` | 0 | — |
| RECOMMEND DROP | 3 | infinitt-dps (2), exo-lung-ai (9), imbio-lung-density (13) |

If the 3 "DROP" items are retained anyway, they should each be `data_completeness: "stub"` with explicit `intended_use` text disclosing they are not cancer-detection devices.

## Items the curator should review first (priority order)
1. **Imagio (PMA P200003)** — full PMA SSED data populated, but the SSED notes only the *primary* endpoint passed; secondary endpoints (NLR, PLR, pAUC) failed hierarchical testing. The curator should ensure the `limitations_noted` text reflects this nuance. Also verify the 2018 Neuschler *Radiology* paper PubMed ID (29178816) — I used the well-known canonical reference but cite-check.
2. **Avenda (K221624)** — full data, but the 510(k) indication is restricted to patients with confirmed GGG ≥ 2 lesion AND uploaded biopsy coordinates. This is NOT a screening or unaided detection tool. Curator should ensure `intended_use` accurately reflects the restriction.
3. **The 3 DROP candidates (#2 INFINITT, #9 Exo, #13 Imbio)** — confirm exclusion. If their inclusion was politically required by the project plan, mark them as stubs with clear "not a cancer-detection device" language. Most useful action: drop and document in `NEEDS_VERIFICATION.md` why they were excluded.
4. **Samsung Auto Lung Nodule (K201560)** — table guess was `radiology_ct` but **actual modality is chest X-ray (PA radiograph)**. Curator MUST correct modality before merging.
5. **Quantib Prostate (K230772)** — Special 510(k) with only bench data in the public summary; for full historical metrics, curator should also pull predicate K221106 / K202501 Decision Summaries.
6. **V5med (K242919)** — internal inconsistency in reading-time numbers (text says "133.0 → 115.9 s" but the table says "113.0 → 115.9 s"). Curator should flag this typographic ambiguity in the FDA Summary.

## FDA-listed products that are not oncology-relevant (recommended drops)
- **INFINITT DPS (K243449)** — pure whole-slide-image viewer / management system; no AI cancer-detection function.
- **Exo Lung AI / LAI001 (K243239)** — point-of-care lung ultrasound for **consolidation/atelectasis and pleural effusion** in emergency medicine; no cancer, no nodule, no oncology endpoint.
- **Imbio CT Lung Density Analysis (K141069)** — pulmonary tissue density quantification for **emphysema / COPD / ILD**; not a cancer-detection device. Tangential lung-cancer-screening-LDCT use as an incidental-finding quantifier does not make it an oncology AI product.

## Modality corrections vs candidate-list table
| # | Candidate-list guess | Actual (per FDA summary) | Action |
|---|----------------------|--------------------------|--------|
| 9 | `radiology_us or radiology_ct (verify)` for Exo Lung AI | `radiology_us` — but drop entirely (no cancer indication) | Drop |
| 11 | `radiology_ct` for Samsung Auto Lung Nodule | `radiology_xray` (PA chest radiograph) | Correct modality |
| Others | as guessed | confirmed | OK |

## Net-new entries actually recommended for inclusion (10 of 13)
1. `seno-imagio-breast` (full)
2. `clarius-prostate-ai` (partial — volume measurement only)
3. `quibim-qp-prostate` (full)
4. `jlk-medihub-prostate` (partial — segmentation only)
5. `quantib-prostate` (partial — workflow/segmentation; mixed peer-reviewed evidence)
6. `avenda-prostate-cancer-planning` (full — strongest evidence package)
7. `coreline-aview-lung-nodule` (full)
8. `v5med-lung-ai` (partial — standalone metrics not in summary)
9. `samsung-auto-lung-nodule` (partial — quantitative metrics not in summary; **modality = X-ray**)
10. `body-vision-lung` (partial — procedural guidance; clinical evidence is via PubMed not FDA summary)

Net-new entries recommended for drop (3 of 13): `infinitt-dps`, `exo-lung-ai`, `imbio-lung-density`.

---

**END OF SHEET**
