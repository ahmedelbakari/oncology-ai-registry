# Numerical-Accuracy Audit — 9 `full` Entries (Pre-Launch Gate)

**Date:** 2026-05-31
**Auditor method:** Each entry's `validation`/`regulatory` block in `v1/data.json` was compared field-by-field against the PRIMARY source — FDA Decision Summary / PMA SSED PDFs (downloaded directly from accessdata.fda.gov), the openFDA 510(k)/PMA database for regulatory fields, and the pivotal PubMed publications. Registry verification sheets were NOT used as ground truth.

---

## Verdict: ERRORS FOUND

**All 30+ headline validation numbers (cohort sizes, AUC, sensitivity, specificity, HR/CIs, p-values) across all 9 entries are CORRECT.** No Signatera-style headline-number error exists in any of the 9 entries.

**However, two `key_publications` metadata errors were found** (1 wrong PMID/URL pointing to an unrelated article; 1 wrong journal name). These are citation-integrity defects, not validation-number errors, but they should be fixed before a public launch since one URL resolves to the wrong paper entirely.

The two maintainer corrections called out in the task brief (ibex K241232 / 2025-01-24; icad K182373 / 2018-12-06) were **independently verified against the openFDA database and the FDA PDFs — both are CORRECT.**

---

## Summary table (headline numbers)

| Entry | Field group | data.json | Primary source | PASS/FAIL |
|---|---|---|---|---|
| pathai-aisight-dx | discordance rates, CIs, NI margin, concordance | all values | K243391 Decision Summary | PASS |
| pathai-aisight-dx | reg: K243391, 2025-06-26 | K243391 / 2025-06-26 | openFDA | PASS |
| ibex-galen-prostate | Study1/Study2 sens/spec + all CIs, site counts | all values | K241232 Decision Summary | PASS |
| ibex-galen-prostate | reg: K241232, 2025-01-24 (corrected) | K241232 / 2025-01-24 | openFDA | PASS |
| owkin-msintuit-crc | sens 0.96–0.98, spec 0.46–0.47, κ 0.82, n=600, 9 labs | all values | Nat Commun 2023 (PMC10628260) | PASS |
| veracyte-afirma-gsc | sens 91% spec 68% NPV 96% PPV 47% + CIs, n=191, 24% prev | all values | JAMA Surg 2018 abstract (PMID 29799911) | PASS |
| seno-imagio-breast | fSp 47.2/38.2, diff 9.0%, p=0.027, NLR, cohort counts | all values | P200003 SSED | PASS |
| seno-imagio-breast | reg: P200003, 2021-01-11 | P200003 / 2021-01-11 | openFDA PMA | PASS |
| avenda-prostate | sens 97.4/38.2, spec 72.1/53.4, BA, encapsulation, 10 readers, 137/50 | all values | K221624 Decision Summary | PASS |
| avenda-prostate | reg: K221624, 2022-11-22 | K221624 / 2022-11-22 | openFDA | PASS |
| quibim-qp-prostate | AUC 0.849/0.868, ΔAUC 0.019 p=0.039, standalone 0.732, n=228/247, 9 readers | all values | K242683 Decision Summary | PASS |
| quibim-qp-prostate | reg: K242683, 2025-03-18 | K242683 / 2025-03-18 | openFDA | PASS |
| coreline-aview-lung | MRMC AUC 0.73/0.92, sens 0.68/0.91, standalone 0.961/0.907/0.704, n=151/282, 11 readers | all values | K221592 Decision Summary | PASS |
| coreline-aview-lung | reg: K251203, 2025-12-03 | K251203 / 2025-12-03 | openFDA | PASS |
| icad-profound-ai-dbt | AUC 0.852/0.795 diff 0.057, sens/spec/recall + CIs, reading time 52.7%, cohorts 260/655/610 | all values | K182373 Decision Summary | PASS |
| icad-profound-ai-dbt | reg: K182373, 2018-12-06 (corrected) | K182373 / 2018-12-06 | openFDA | PASS |
| **icad-profound-ai-dbt** | **key_publications[0] URL/PMID** | **PMID 33937794** | **should be PMID 32076660** | **FAIL** |
| **seno-imagio-breast** | **key_publications[1] journal** | **"Academic Radiology"** | **"AJR Am J Roentgenol"** | **FAIL** |

---

## Detailed verification with verbatim source quotes (headline numbers — all PASS)

### 1. pathai-aisight-dx — K243391 — PASS
Source: https://www.accessdata.fda.gov/cdrh_docs/reviews/K243391.pdf
- Leica arm: "The major discordance rate between MO and GT was 9.50% (72/758) and between MD and GT was 9.23% (70/758)… difference in major discordance rate between MO and MD was -0.26% (95% CI, -2.71, 2.52; p<0.0001)." ✔
- Hamamatsu arm: "MO and GT was 9.58% (73/762) and between MD and GT was 8.40% (64/762)… difference… was -1.18% (95% CI, -3.49, 1.16; p<0.0001)." ✔
- NI margin: "prespecified noninferiority threshold of 4%." ✔
- Concordance: Leica "96.57% (95% CI, 93.39, 98.97)"; Hamamatsu "97.90% (95% CI, 96.45, 99.21)." ✔
- 2-week washout, single site, 3 readers/arm, 258 cases/arm (n_samples 516 = 258×2). ✔
- Reg: openFDA "device_name: AISight Dx … decision_date: 2025-06-26 … K243391." ✔

### 2. ibex-galen-prostate — K241232 — PASS (incl. maintainer correction)
Source: https://www.accessdata.fda.gov/cdrh_docs/reviews/K241232.pdf
- Study 1 slide-level: "Sensitivity 81.0% (69.2%; 92.9%), Specificity 91.6% (90.9%; 92.3%)." ✔
- Study 1 case-level: "Sensitivity 80.8% (74.1%; 87.6%), Specificity 46.9% (39.5%; 54.3%)." ✔
- Study 2 combined: "Difference 3.5% (2.3%; 4.5%)"; specificity "-3.2% (-4.3%; -1.9%)"; "93.9% … 90.5% … 87.9% … 91.1%." ✔
- Intended-use (benign-by-SoC) subset: "36.3% with 95% CI: (28.0%; 45.5%) … 96.5% with 95% CI: (95.2%; 97.5%)." ✔
- Per-pathologist sensitivity improvement range 0.0%–11.6% (Table 26). ✔
- Sites: Study 1 = "two sites in the US and one OUS site" (2 US + 1 OUS, 347 cases); Study 2 (AIDER-1) = "3 US clinical pathology laboratories … and 1 OUS" (n_sites=4). ✔
  - NOTE: PDF line 360 ("4 sites - 2 US sites and 2 OUS sites") refers to the analytical *precision* study, NOT the clinical reader study cited in data.json — no conflict.
- Reg: openFDA "Galen Second Read … 2025-01-24 … K241232." ✔ (maintainer correction confirmed)

### 3. owkin-msintuit-crc — Nature Communications 2023 — PASS
Source: PMC10628260 (full text). FDA status correctly "Research Use" / CE-marked (no FDA summary).
- "MSIntuit yields a sensitivity of 0.96–0.98, a specificity of 0.47-0.46, and an excellent inter-scanner agreement (Cohen's κ: 0.82)." ✔ (data.json spec "0.46–0.47" = same range)
- "blind validation … on an independent dataset of 600 consecutive CRC patients"; "600 consecutive CRC cases diagnosed across nine different pathology labs." ✔

### 4. veracyte-afirma-gsc — JAMA Surgery 2018 (Patel) — PASS
Source: PubMed abstract PMID 29799911. LDT (no FDA review) — reg fields not FDA-verifiable, correctly marked LDT.
- "sensitivity of 91% (95% CI, 79-98) and a specificity of 68% (95% CI, 60-76). At 24% cancer prevalence, the negative predictive value was 96% (95% CI, 90-99) and the positive predictive value was 47% (95% CI, 36-58)." ✔
- "191 samples (91.0%) had adequate residual RNA." ✔ (n_samples=191 correct)
- MINOR (not a flagged headline field): abstract says "Of the 183 included patients" and "49 academic and community centers." data.json sets n_patients=191 (samples, not patients) and n_sites=null. Not an error in any populated headline metric; noted for completeness only.

### 5. seno-imagio-breast — P200003 SSED — PASS
Source: https://www.accessdata.fda.gov/cdrh_docs/pdf20/P200003B.pdf
- "fSp was found to be higher with statistical significance (two-sided p=0.027) for IUS+OA (47.2%, 95% CI=[35.9%,58.5%]) compared to IUS alone (38.2%, 95% CI=[24.9%, 51.6%]), with a difference in fSp of 9.0% with 95% CI=[1.0%, 17.0%]." ✔
- "NLR was 0.047 (95% CI: 0.032, 0.062) for IUS+OA … 0.053 (95% CI: 0.037, 0.070) for IUS alone … relative NLR … was 0.896 with a 95% CI= (0.693, 1.11) which included 1." ✔ (hierarchical testing stopped — PLR/pAUC descriptive only ✔)
- "480 masses in total … 180 malignant masses … 300 benign masses (288 benign, 12 high risk)." ✔
- "PIONEER ITD Population included 1739 subjects"; "Safety Population … 1972 subjects"; "subjects who consented (n=2105)." ✔
- Reg: openFDA original P200003 decision 2021-01-11. ✔

### 6. avenda-prostate-cancer-planning — K221624 — PASS
Source: https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221624.pdf
- "superior sensitivity (mean 97.4% vs 38.2%, p<0.0001) … superior specificity … (mean 72.1% vs 53.4%, p<0.0001) … balanced accuracy (mean 84.7% vs 67.2% & 75.9% respectively, p<0.0001) and 'clinical quality' (in 99% and 60% of cases respectively, p<0.0001) … complete csPCa encapsulation rate of 72.8% with the Proposed Device, and only 1.6% with SOC methods (p<0.0001)." ✔
- "standalone test set of 137 … whole mount pathology dataset of N=50 patients." ✔
- "Ten practicing urologists or radiologists from different institutions … (2 to 23 years … experience)." ✔ (the "7 urologists + 3 radiologists / 5 institutions" detail comes from the J Urol 2024 paper; n_sites=5 derived from there)
- Reg: openFDA "Avenda Health AI Prostate Cancer Planning Software … 2022-11-22 … K221624." ✔

### 7. quibim-qp-prostate — K242683 — PASS
Source: https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242683.pdf
- "AUCunaided 0.849 (95% CI: 0.814-0.884); AUCaided 0.868 (95% CI: 0.834-0.902); DAUC … 0.019 (95% CI: 0.001-0.038) … p-value: 0.039." ✔
- Standalone: "AUC-ROC 0.732 (95% CI: 0.668-0.791)"; high-suspicion sens "0.677 (0.593-0.761)" FPR/case 0.417; high+moderate sens "0.795 (0.722-0.861)" FPR/case 0.855. ✔
- "228 cases … N=247 … each case (N=228) … each of the 9 readers." ✔; demographics (85.1% White, 8.3% AA, 86.0% 3T, Siemens 62.3% …) all match. ✔
- Reg: openFDA "QP-Prostate® CAD … 2025-03-18 … K242683." ✔

### 8. coreline-aview-lung-nodule — validation from K221592; reg = K251203 — PASS
Source: https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221592.pdf
- MRMC: "AUC 0.73 (0.66–0.79) … 0.92 (0.89–0.95) … 0.19; Sensitivity 0.68 (0.62–0.73) … 0.91 (0.89–0.94) … 0.23; FP/scan 0.48 (0.28–0.69) … 0.28 (0.15–0.42)." ✔
- Standalone: "Overall AUC 0.961(0.939-0.983); Sensitivity 0.907(0.846-0.95); Specificity 0.704(0.622-0.778); sensitivity at FP/scan<2: 0.889(0.849-0.93) at FP/scan=0.504." ✔
- "151 Chest CTs with 103 negative controls and 48 cases"; "eleven board-certified radiologists … 4-week washout"; standalone "282 (140 … 142 …)"; "132 males and 150 females." ✔
- Reg: openFDA confirms BOTH K221592 (2023-02-24, original pivotal clearance) and K251203 (2025-12-03, the UI-only minor change). data.json correctly lists K251203/2025-12-03 as current reg and documents that the validation data is from K221592. ✔

### 9. icad-profound-ai-dbt — K182373 — PASS on numbers (incl. maintainer correction)
Source: https://www.accessdata.fda.gov/cdrh_docs/pdf18/K182373.pdf
- "AUC with CAD, 0.852, versus without CAD, 0.795 … difference in AUC was 0.057 (95% CI: 0.028, 0.087; non-inferiority p<0.01…)." ✔
- Case-level sens "increased by 0.080 (95% CI: 0.026, 0.134) … 0.770 without CAD and 0.850 with CAD." ✔
- Lesion-level sens "increased by 0.084 (95% CI: 0.029, 0.139) … from 0.769 … to 0.853." ✔
- Specificity "0.627 without CAD and 0.696 with CAD … increase of 0.069 (95% CI: 0.030, 0.108)." ✔
- Recall in non-cancers "0.380 without CAD and 0.309 with CAD … reduction of 0.072 (95% CI: 0.031, 0.112)." ✔
- Reading time "improved 52.7% with CAD (95% CI: 41.8%, 61.5%; p<0.01)." ✔
- Cohorts: "260 … 65 cancer cases with 66 malignant lesions … 24 tomosynthesis radiologist readers"; standalone "655 Hologic … 235 cancer … 242 malignant lesions"; "610 GE DBT cases … 204 cancer … 221 malignant lesions." ✔
- Reg: openFDA "PowerLook Tomo Detection V2 Software … Icad, Inc. … 2018-12-06 … K182373." ✔ (maintainer correction confirmed)

---

## FAILURES — exact corrections required

### FAIL #1 — icad-profound-ai-dbt: key_publications URL points to the WRONG paper
- **Field path:** `entries[icad-profound-ai-dbt].validation.key_publications[0].url`
- **data.json value:** `https://pubmed.ncbi.nlm.nih.gov/33937794/`
- **Problem:** PMID **33937794** is an unrelated editorial titled *"Will Artificial Intelligence Replace Radiologists?"* (Radiology: Artificial Intelligence, 2019). It is NOT the Conant et al. pivotal ProFound AI DBT study whose title is stored in data.json.
- **Correct value:** PMID **32076660** → `https://pubmed.ncbi.nlm.nih.gov/32076660/`
- **Verbatim source (esummary PMID 32076660):** "Radiology. Artificial intelligence | 2019 Jul 31 | Improving Accuracy and Efficiency with Concurrent Use of Artificial Intelligence for Digital Breast Tomosynthesis."
- The stored title, journal ("Radiology: Artificial Intelligence"), and year (2019) are correct — only the URL/PMID is wrong.

### FAIL #2 — seno-imagio-breast: key_publications wrong journal name
- **Field path:** `entries[seno-imagio-breast].validation.key_publications[1].journal`
- **data.json value:** `"Academic Radiology"`
- **Correct value:** `"AJR. American Journal of Roentgenology"` (commonly "AJR Am J Roentgenol")
- **Verbatim source (esummary PMID 36475811):** "AJR. American journal of roentgenology | 2023 May | Optoacoustic Imaging With Decision Support for Differentiation of Benign and Malignant Breast Masses…"
- The URL (PMID 36475811), title, and pivotal:false flag are correct; data.json's year (2022) vs PubMed (2023 May, with a 2022 epub) is a minor epub-vs-issue difference, not flagged as an error. Only the journal name is wrong.

---

## Notes / could-not-fully-verify

- **veracyte-afirma-gsc** is an LDT with no FDA Decision Summary; performance was verified against the JAMA Surgery 2018 abstract (the pivotal primary source), which carries all headline numbers. Full-text body figures were not separately retrieved (paywalled), but every headline metric in data.json appears verbatim in the abstract, so all flagged fields are verified.
- **owkin-msintuit-crc**: data.json itself flags that exact standalone 95% CIs are "not captured in summary text"; the abstract-level ranges and κ all match. The narrowed CIs in the full text (e.g., sens 0.98 [0.95–1.0], spec 0.47 [0.43–0.51]) are consistent and not contradicted.
- No other entry had inaccessible primary sources — all 7 FDA PDFs downloaded and parsed cleanly, and openFDA confirmed all 8 regulatory K/PMA records.
