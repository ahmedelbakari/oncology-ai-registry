#!/usr/bin/env python3
"""v0.2.2 pre-launch cleanup — apply curator-approved fixes to data.json.

Sources:
  - PRE_LAUNCH_REVIEW.md (adversarial reviewer, 2026-05-12)
  - VALIDATION_VERIFICATION_SHEET_cleanup.md (cleanup agent, 2026-05-31)
  - Paper H reader's 6-item list (curator-forwarded)

Curator decisions (2026-05-31):
  - Broaden scope tagline (handled in HTML/README, not here)
  - Flip ataraxis-breast-risk peer_reviewed -> true with analytical-only note
  - Apply all cleanup-sheet fixes

Agent-proposed non-schema enum values are normalized to the v0.2 controlled
vocabulary; the precise original label is preserved in limitations_noted.

NOTE: Ibex URL, iCAD 510(k) number, and any numerical-audit corrections from the
parallel verification job are applied SEPARATELY (not in this script).

Idempotent. Run from repo root.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"

TODAY = "2026-05-31"


def main():
    data = json.loads(DATA.read_text())
    g = {e["id"]: e for e in data["entries"]}
    changes = []

    # --- 0. Bump last_updated -------------------------------------------------
    data["last_updated"] = TODAY
    changes.append("last_updated -> 2026-05-31")

    # --- 1. Signatera sample count 795 -> 829 (reviewer critical #1) ----------
    sig = g["signatera-mrd"]["validation"]["cohort_size"]
    if "795" in (sig.get("unit_note") or ""):
        sig["unit_note"] = sig["unit_note"].replace(
            "795 longitudinal plasma samples", "829 longitudinal plasma samples"
        )
        changes.append("signatera-mrd: plasma samples 795 -> 829 (Reinert 2019 abstract)")

    # --- 2. vesta-risk-stratify: populate validation from Euro Urology 2025 ---
    g["vesta-risk-stratify"]["validation"] = {
        "study_design": "retrospective",
        "cohort_size": {
            "n_patients": 269,
            "n_samples": None,
            "unit_note": (
                "269 patients with BCG-naive high-grade Ta NMIBC treated with adjuvant "
                "intravesical BCG after TURBT (2004-2024); none from the biomarker "
                "development set. Distinct from the cohort in Valar's BCGPredict paper."
            ),
        },
        "n_sites": 13,
        "site_geography": "multi_center_international",
        "comparator": "clinicopathologic_factors",
        "primary_endpoint": "hazard_ratio",
        "primary_result": (
            "Primary endpoint high-grade recurrence-free survival (HG-RFS): CHAI biomarker "
            "HR 2.23 (95% CI 1.45-3.44; p<0.001), outperforming EAU and AUA/SUO guideline "
            "risk-stratification schemes. On multivariable adjustment, AUA risk (HR 1.93, "
            "95% CI 1.07-3.48; p=0.029) and EAU risk (HR 1.47, 95% CI 0.96-2.23; p=0.074) "
            "were not independently significant. Secondary endpoint MIBC progression-free "
            "survival: CHAI AI component HR 4.55 (95% CI 1.39-14.92; p=0.012)."
        ),
        "external_validation": {
            "performed": False,
            "cohort_description": (
                "Single multicenter analysis cohort of 269 patients, none in the biomarker "
                "development set; no separate independent external-validation cohort in this "
                "publication."
            ),
            "result": (
                "CHAI biomarker outperformed EAU and AUA/SUO guideline risk schemes for both "
                "HG-RFS and MIBC-PFS within this cohort."
            ),
        },
        "peer_reviewed": True,
        "key_publications": [
            {
                "title": (
                    "Computational Histology Artificial Intelligence (CHAI) Enhances Risk "
                    "Stratification of High-grade Ta Non-muscle-invasive Bladder Cancer in a "
                    "Multicenter Cohort: Comparison to Current European Association of Urology "
                    "and American Urological Association Stratification Schemes"
                ),
                "journal": "European Urology",
                "year": 2025,
                "url": "https://pubmed.ncbi.nlm.nih.gov/40514253/",
                "pivotal": True,
            }
        ],
        "limitations_noted": (
            "[Source-detail: comparator = EAU/AUA guideline risk groups; primary endpoint = "
            "high-grade recurrence-free survival; geography = 12 US sites + 1 Chilean site.] "
            "Authors note the study is limited by its retrospective nature and potential for "
            "bias or variation in clinical factors across participating sites."
        ),
        "fda_summary_url": None,
        "data_completeness": "full",
    }
    # keep press release only in sources (deployment context); ensure it's there
    changes.append("vesta-risk-stratify: validation populated from Euro Urology 2025 (PMID 40514253); external_validation.performed=false; key_pub URL fixed")

    # --- 3. vitara-pancreas-chemopredict: populate from JCO 2026 (partial) ----
    g["vitara-pancreas-chemopredict"]["validation"] = {
        "study_design": "retrospective",
        "cohort_size": {
            "n_patients": 477,
            "n_samples": None,
            "unit_note": (
                "Advanced PDAC patients: 178 in the multi-institutional development cohort + "
                "299 in the independent validation cohort (F-pref n=173, G-pref n=126) drawn "
                "from the prospective COMPASS and PanCAN Know Your Tumor studies."
            ),
        },
        "n_sites": None,
        "site_geography": "multi_center_international",
        "comparator": "clinical_outcomes",
        "primary_endpoint": "other",
        "primary_result": (
            "Independent validation cohort (n=299): F-pref group (n=173) F-chemo vs G-chemo "
            "TNTD 8.6 vs 7.5 mo (P=.035), OS 14.4 vs 11.7 mo (P=.003); G-pref group (n=126) "
            "G-chemo vs F-chemo TNTD 9.6 vs 7.2 mo (P=.038), OS 14.3 vs 12.4 mo (P=.5, NS). "
            "Propensity-score-weighted biomarker-treatment interaction P<.001 (TNTD); P=.005 (OS)."
        ),
        "external_validation": {
            "performed": True,
            "cohort_description": (
                "Independent validation cohort of 299 patients from the prospective COMPASS "
                "and PanCAN Know Your Tumor studies, separate from the 178-patient development "
                "cohort. Biomarker and threshold locked before validation."
            ),
            "result": (
                "Biomarker-treatment interaction significant for both TNTD (P<.001) and OS "
                "(P=.005) on propensity-score-weighted analysis."
            ),
        },
        "peer_reviewed": True,
        "key_publications": [
            {
                "title": (
                    "Development and Validation of a Computational Histology Artificial "
                    "Intelligence-Powered Predictive Biomarker for Selection of Chemotherapy "
                    "in Advanced Pancreatic Cancer"
                ),
                "journal": "Journal of Clinical Oncology",
                "year": 2026,
                "url": "https://pubmed.ncbi.nlm.nih.gov/41671529/",
                "pivotal": True,
            }
        ],
        "limitations_noted": (
            "[Source-detail: primary endpoints = time to next treatment/death (TNTD) and "
            "overall survival; comparator = alternative first-line chemotherapy regimen "
            "(fluoropyrimidine- vs gemcitabine-based).] JCO full text paywalled; n_sites and "
            "the formal limitations section not accessible. Validation cohort assembled from "
            "two distinct prospective studies (COMPASS, Know Your Tumor), not a single "
            "randomized prospective trial."
        ),
        "fda_summary_url": None,
        "data_completeness": "partial",
    }
    changes.append("vitara-pancreas-chemopredict: validation populated from JCO 2026 (PMID 41671529); partial (paywall); key_pub URL fixed")

    # --- 4. RUO/LDT contradiction fix (3 entries): ldt true -> false ----------
    for eid in ("aiforia-her2", "mindpeak-pdl1", "visiopharm-her2-connect"):
        reg = g[eid]["regulatory"]
        if reg.get("ldt") is True:
            reg["ldt"] = False
            changes.append(f"{eid}: ldt true -> false (CE-IVD in EU, RUO in US, no CLIA LDT)")
    # trim primary_markets to drop US for the two that list it
    for eid in ("aiforia-her2", "mindpeak-pdl1"):
        dep = g[eid].get("deployment", {})
        pm = dep.get("primary_markets")
        if isinstance(pm, list) and "US" in pm:
            dep["primary_markets"] = [m for m in pm if m != "US"]
            changes.append(f"{eid}: primary_markets drop US (RUO-only in US)")

    # --- 5. ataraxis-breast-risk: flip peer_reviewed -> true with note --------
    arv = g["ataraxis-breast-risk"]["validation"]
    if arv.get("peer_reviewed") is not True:
        arv["peer_reviewed"] = True
        note = (
            "Peer-review status: analytical validation IS peer-reviewed (Diagnostics 2026, "
            "MDPI); the headline clinical-validation numbers (C-index, HRs, Oncotype DX "
            "head-to-head) currently live in an arXiv preprint + ASCO 2025 congress abstract, "
            "neither of which has completed peer review. "
        )
        lim = arv.get("limitations_noted") or ""
        if "Peer-review status" not in lim:
            arv["limitations_noted"] = note + lim
        changes.append("ataraxis-breast-risk: peer_reviewed false -> true (analytical-only note added)")

    # --- 6. artera-prostate: explain LDT + De Novo dual status ----------------
    art = g["artera-prostate"]
    note = " Originally offered as a laboratory-developed test; FDA De Novo authorized 2025-07-31 (DEN240068)."
    if "De Novo authorized 2025-07-31" not in art["intended_use"]:
        art["intended_use"] = art["intended_use"].rstrip() + note
        changes.append("artera-prostate: intended_use notes LDT->De Novo transition")

    # --- 7. paige-her2: intended_use H&E inference, not IHC interpretation ----
    ph = g["paige-her2"]
    if "IHC interpretation" in ph["intended_use"]:
        ph["intended_use"] = (
            "AI inference of HER2 status from H&E-stained breast cancer slides (no IHC required)."
        )
        changes.append("paige-her2: intended_use corrected (H&E inference, not IHC interpretation)")

    # --- 8. exact-oncotype-dx-breast: fix broken source URL -------------------
    onc = g["exact-oncotype-dx-breast"]
    for s in onc.get("sources", []):
        if s.get("url") == "https://www.exactsciences.com/products/oncotype-dx":
            s["url"] = "https://www.exactsciences.com/cancer-testing/oncotype-dx-breast-recurrence-score-invasive-ductal"
            changes.append("exact-oncotype-dx-breast: source URL fixed (was 404)")

    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Applied {len(changes)} changes:")
    for c in changes:
        print(f"  - {c}")


if __name__ == "__main__":
    main()
