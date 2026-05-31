# Review Request — v0.2.2 cleanup batch (pre-commit)

**To:** Independent reviewer
**From:** Registry maintainer
**Date:** 2026-05-31
**Status:** All changes below are APPLIED to the working tree but NOT committed. Do not let me commit until you've signed off.

## Context

The prior pre-launch review (`PRE_LAUNCH_REVIEW.md`, verdict GO WITH FIXES) flagged ~11 issues against the committed site (commit `adebce0` / v0.2.1, 116 entries). Separately, a downstream reader flagged 6 more items. This batch applies fixes for both. **None of this work has been reviewed yet.** Your job: verify it's correct before it goes live.

Repo: `/Users/ahmed-elbakri/Downloads/_Immigration/Ahmed_EB-2_NIW/REFILE_2026/05_side_projects/registry/`
Diff to review: `git diff` against commit `adebce0` (the working tree). 122 files changed (most are regenerated `v1/tools/*.html` from a template/date change — focus on `v1/data.json`, `scripts/build_pages.py`, the 3 HTML taglines, and `README.md`).

## What changed and what to verify

### A. Newly populated entries (HIGHEST RISK — verify against primary sources)

1. **`vesta-risk-stratify`** — went from stub to `data_completeness: "full"`.
   - Source: European Urology 2025, PMID **40514253**, PMC12718547.
   - Claims to verify: 269 patients; 13 sites (12 US + 1 Chile); HG-RFS HR **2.23 (95% CI 1.45–3.44, p<0.001)**; MIBC-PFS CHAI AI component HR **4.55 (1.39–14.92, p=0.012)**; AUA HR 1.93, EAU HR 1.47.
   - **Critical judgment call to confirm:** `external_validation.performed` is set to **false** (single analysis cohort, no separate external cohort). The prior data wrongly carried the BCGPredict paper's "international validation" framing. Confirm false is right.
   - key_publications URL was a Business Wire press release — replaced with the PubMed URL. Confirm the new URL resolves and matches the title.
   - Enum normalization applied: comparator `clinicopathologic_factors` (paper compares vs EAU/AUA guideline risk groups); primary_endpoint `hazard_ratio`; site_geography `multi_center_international`. Confirm these are the best fits in the v0.2 controlled vocabulary (see `scripts/validate.py` for allowed values). Precise original labels preserved in `limitations_noted`.

2. **`vitara-pancreas-chemopredict`** — stub to `data_completeness: "partial"`.
   - Source: JCO 2026, PMID **41671529** (full text paywalled — populated from PubMed abstract only).
   - Claims to verify: 477 patients (178 dev + 299 validation from COMPASS + PanCAN Know Your Tumor); F-pref n=173, G-pref n=126; TNTD/OS numbers and interaction P-values (P<.001 TNTD, P=.005 OS).
   - `n_sites` left null and marked partial because the full text is paywalled — confirm that's honest, not lazy.
   - key_publications URL was Business Wire — replaced with PubMed. Verify.

### B. Numerical correction (reviewer's critical #1)

3. **`signatera-mrd`** — `cohort_size.unit_note` changed "795 longitudinal plasma samples" → "**829**". Verify 829 is what Reinert 2019 JAMA Oncology (PMID 31070691) actually states. (The reviewer quoted "Plasma samples (n = 829)".)

### C. Regulatory contradiction fix (reader's item 5)

4. **`aiforia-her2`, `mindpeak-pdl1`, `visiopharm-her2-connect`** — `ldt: true → false`, kept `fda_status: "Research Use"` + `ce_marked: true`. Rationale: all three are CE-IVD in EU but Research Use Only in the US (no CLIA LDT offering). Verbatim disclaimers are in `VALIDATION_VERIFICATION_SHEET_cleanup.md` Task 3. **Verify the RUO-in-US claim for each is correct** — this is a regulatory status change, so it must be right. Also `deployment.primary_markets` dropped "US" for aiforia-her2 and mindpeak-pdl1.

### D. Peer-review flag flip (reader's item 3 — curator-approved)

5. **`ataraxis-breast-risk`** — `peer_reviewed: false → true`, with a note in `limitations_noted` stating the analytical validation (Diagnostics 2026, MDPI) is peer-reviewed but the headline clinical numbers are still preprint + ASCO abstract. **Verify this is not overclaiming** — is it defensible to mark peer_reviewed:true when the clinical numbers aren't yet peer-reviewed, given the note? Flag if you disagree.

### E. Text/labeling fixes

6. **`artera-prostate`** `intended_use` — appended note explaining LDT→De Novo transition (DEN240068, 2025-07-31). Verify accurate.
7. **`paige-her2`** `intended_use` — changed from "AI assistant for HER2 IHC interpretation" to "AI inference of HER2 status from H&E-stained breast cancer slides (no IHC required)." Verify this matches the tool's actual mechanism (it infers from H&E, not IHC).
8. **`exact-oncotype-dx-breast`** source URL — replaced a 404 with `https://www.exactsciences.com/cancer-testing/oncotype-dx-breast-recurrence-score-invasive-ductal`. Confirm it resolves.

### F. Presentation fixes (reviewer #2, #11)

9. **`scripts/build_pages.py`** — added `PRIMARY_ENDPOINT_LABEL` dict so detail pages render human labels (e.g. "Time-to-event by risk category") instead of raw enum strings (`time_to_event_risk_strata`). Verify on a rebuilt page (e.g. `v1/tools/artera-prostate.html`). Also renamed table label "Number of sites" → "Number of validation sites".

### G. Scope + metadata (reviewer #4, #5, #6; curator-approved)

10. **Tagline broadened** "diagnostic" → "diagnostic, predictive, and prognostic" in `index.html` (title, meta, subtitle, h1), `methodology.html` (Purpose), `about.html` (Why this exists), `README.md`. Verify consistent and no remaining "diagnostic"-only scope claims that contradict content.
11. **`README.md`** — full rewrite from stale v0.1/12-entries to v0.2/116-entries. Verify entry count, version, citation block, and links are correct.
12. **Dates** — `data.json.last_updated` 2026-04-22 → 2026-05-31; methodology.html "May 7" → "May 31". Verify no other stale dates remain.

## Known pending (NOT in this diff yet — flag if you think they block)

A parallel verification job is still finishing. It will add 2–3 more facts before commit: a replacement URL for `ibex-galen-prostate` (current source 404s), the `fda_510k_number` + decision date for `icad-profound-ai-dbt`, and any numerical errors found in 9 other `full` entries that weren't deep-checked in the first review. Those will get folded in and should get a quick sanity check too. Note in your report whether you consider the commit blocked until they land.

## What to produce

Write your assessment to `/Users/ahmed-elbakri/Downloads/_Immigration/Ahmed_EB-2_NIW/REFILE_2026/05_side_projects/registry/REVIEW_v022_RESULT.md`:

- **Verdict:** APPROVE TO COMMIT / APPROVE WITH FIXES / DO NOT COMMIT
- Per-item PASS/FAIL for items 1–12 above, with the primary source you checked and any discrepancy found
- Any new issue you find that I didn't list
- Be skeptical and specific. Verify numbers against PubMed/FDA, not against my verification sheets (those could carry my errors forward). For paywalled sources, verify what the abstract supports and flag what you couldn't check.

Time-box ~30–40 min. Sample the highest-risk items (A, B, C, D) thoroughly; spot-check the rest.
