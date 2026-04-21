# Entries needing Ahmed's verification before press push

This file tracks entries where the curator (Claude) populated the core product
identity (name, company, cancer type, modality, general intended use) from
well-documented public sources, but left specific regulatory dates, pathway
decisions, or pivotal-publication references as `null` pending verification.

Before the July 2026 press push (tracker task 1.6), Ahmed should walk through
this list and for each entry either:
1. Fill in the verified values by consulting FDA 510(k)/De Novo/PMA database or the
   company's published evidence, or
2. If a claim cannot be verified, delete the entry or open a GitHub issue.

---

## Batch 02 additions (2026-04-20) — 43 entries

All batch-02 entries currently have at least one source URL, but most have:
- `fda_decision_date: null`
- `clinical_evidence.key_publication: null`
- No specific performance metrics

**Histopathology (12 entries):**
- paige-breast — verify 510(k) number and decision date
- pathai-aisight-dx — verify FDA clearance scope vs. research-use components
- deepbio-deepdx-prostate — confirm De Novo decision date
- contextvision-inify-prostate — confirm US regulatory status
- aiforia-clinical-prostate — verify specific 510(k) clearance
- aiforia-her2 — confirm LDT vs. cleared status
- roche-upath-her2-breast — find 510(k) number
- mindpeak-pdl1 — confirm current US regulatory status
- owkin-rlapsrisk-bc — confirm US availability
- stratipath-breast — confirm US availability
- visiopharm-her2-connect — confirm US pathway
- ibex-galen-gastric-colon — confirm US regulatory status (ID collides with existing ibex-galen-gastric — rename or merge)

**Radiology lung/CT (7 entries):**
- optellum-virtual-nodule-clinic — De Novo date confirmed as 2021-10, verify specific DEN#
- vuno-med-lungct-ai — verify 510(k) number
- infervision-inferread-lung-ct — verify 510(k) number
- siemens-ai-rad-chest-ct-oncology — verify specific product SKU under clearance
- ge-lung-vcar — verify Lung VCAR 510(k) is the right product family
- aidoc-briefcase-lung-nodule — verify 510(k) number
- oxipit-chesteye — confirm US status

**GI endoscopy (4 entries):**
- medtronic-gi-genius — De Novo 2021-04 confirmed; verify DEN200055 number
- iterative-skout — 510(k) cleared 2022 confirmed; verify K number
- magentiq-colo — verify FDA status
- fujifilm-cad-eye — verify current US 510(k)

**Mammography (2 entries):**
- densitas-intellimammo — verify 510(k) number
- deephealth-saige-dx — verify 510(k) number

**MRI/PET (1 entry):**
- subtle-medical-subtlepet — 2018-09 clearance confirmed; verify K number

**Genomics/molecular (9 entries):**
- myriad-mychoice-cdx — verify PMA number
- myriad-prolaris — LDT, no FDA review (confirmed)
- agendia-mammaprint — 2007-02 clearance confirmed; verify K number
- exact-oncotype-dx-breast — LDT, confirmed
- veracyte-prosigna — verify 510(k) number
- veracyte-envisia — LDT confirmed
- tempus-xf — LDT confirmed
- tempus-xm — LDT confirmed
- natera-altera — LDT confirmed

**CRC / MCED screening (4 entries):**
- exact-cologuard-plus — 2024-10 PMA confirmed; verify number
- guardant-shield — 2024-07 PMA confirmed; verify number
- freenome-crc-blood-test — verify current De Novo / PMA status (PREEMPT-CRC submitted)
- delfi-firstlook-lung — LDT confirmed

**Cervical (2 entries):**
- hologic-genius-cervical — verify 510(k) number and date
- bd-focalpoint-gs — verify PMA number

**Dermatology (2 entries):**
- castle-decisiondx-melanoma — LDT confirmed
- castle-decisiondx-sqcc — LDT confirmed

---

## Process going forward

- When adding large batches, create a similar `NEEDS_VERIFICATION` entry.
- Before press (task 1.6), Ahmed's time is better spent verifying batch-02 than sourcing
  new entries, because the registry's credibility depends on data quality not volume.
- Any batch-02 entry that cannot be verified from the FDA public database or the
  company's IFU/product insert should be downgraded or deleted before launch.
