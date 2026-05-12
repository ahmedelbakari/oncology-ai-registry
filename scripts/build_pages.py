#!/usr/bin/env python3
"""Generate per-tool HTML pages from data.json into v1/tools/<id>.html.

Each entry gets a stable, citable URL like:
    https://oncologyairegistry.org/tools/paige-prostate-detect.html

Run from repo root:
    python3 scripts/build_pages.py
"""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"
OUT_DIR = ROOT / "v1" / "tools"

REG_BADGE = {
    "Breakthrough Device Designation": "bg-purple-100 text-purple-800",
    "De Novo authorized": "bg-emerald-100 text-emerald-800",
    "510(k) cleared": "bg-emerald-100 text-emerald-800",
    "PMA approved": "bg-emerald-100 text-emerald-800",
    "LDT": "bg-blue-100 text-blue-800",
    "Research Use": "bg-amber-100 text-amber-800",
}

MODALITY_LABEL = {
    "histopathology": "Histopathology",
    "radiology_mammography": "Mammography",
    "radiology_ct": "CT",
    "radiology_cxr": "Chest X-ray",
    "radiology_us": "Ultrasound",
    "radiology_mri": "MRI",
    "genomic_sequencing_with_ai": "Genomic + AI",
    "liquid_biopsy": "Liquid biopsy",
    "multiomics": "Multi-omics",
}

COMPARATOR_LABEL = {
    "pathologist_consensus": "Pathologist consensus",
    "gold_standard_test": "Gold-standard test",
    "clinical_outcomes": "Clinical outcomes",
    "clinicopathologic_factors": "Clinicopathologic factors",
    "predicate_device": "Predicate device",
    "none": "No comparator",
}

DESIGN_LABEL = {
    "prospective": "Prospective",
    "retrospective": "Retrospective",
    "rct": "Randomized controlled trial",
    "meta_analysis": "Meta-analysis",
    "bench_only": "Bench testing only",
    "unpublished": "Unpublished / company data",
}

GEOGRAPHY_LABEL = {
    "single_center_us": "Single center (US)",
    "multi_center_us": "Multi-center (US)",
    "multi_center_international": "Multi-center (international)",
}

# FDA pathway: only real submission pathways. "ldt" and "research_use" are
# statuses, not pathways, and are intentionally not included here — entries
# in those categories should have fda_pathway = null.
PATHWAY_LABEL = {
    "510k": "510(k)",
    "de_novo": "De Novo",
    "pma": "PMA",
}


def esc(s):
    if s is None:
        return ""
    return html.escape(str(s))


def or_dash(s):
    if s is None or s == "" or s == []:
        return '<span class="text-slate-400">—</span>'
    return esc(s)


def render_validation(v):
    if not v:
        return ""
    completeness = v.get("data_completeness", "stub")
    completeness_banner = ""
    if completeness in ("stub", "stub_phase1"):
        msg = (
            "Validation summary not yet populated. This entry currently lists only the regulatory pathway and headline citation; "
            "structured cohort and endpoint data are queued for v0.3."
        )
        completeness_banner = (
            f'<div class="rounded border border-amber-300 bg-amber-50 text-amber-900 text-sm px-3 py-2 mb-4">{msg}</div>'
        )
    elif completeness == "partial":
        completeness_banner = (
            '<div class="rounded border border-slate-300 bg-slate-50 text-slate-700 text-sm px-3 py-2 mb-4">'
            "Partial validation summary — some fields are still unverified. See limitations note below."
            "</div>"
        )

    cs = v.get("cohort_size") or {}
    cohort_str_parts = []
    if cs.get("n_patients") is not None:
        cohort_str_parts.append(f"{cs['n_patients']:,} patients")
    if cs.get("n_samples") is not None:
        cohort_str_parts.append(f"{cs['n_samples']:,} samples")
    cohort_str = "; ".join(cohort_str_parts) if cohort_str_parts else None
    if cohort_str and cs.get("unit_note"):
        cohort_str += f" — {cs['unit_note']}"
    elif cs.get("unit_note"):
        cohort_str = cs["unit_note"]

    ev = v.get("external_validation") or {}
    if ev.get("performed") is True:
        ext_str = f"Yes — {ev.get('cohort_description') or ''}"
        if ev.get("result"):
            ext_str += f" · {ev['result']}"
    elif ev.get("performed") is False:
        ext_str = "No"
    else:
        ext_str = None

    rows = [
        ("Study design", DESIGN_LABEL.get(v.get("study_design"), v.get("study_design"))),
        ("Cohort size", cohort_str),
        ("Number of sites", v.get("n_sites")),
        ("Site geography", GEOGRAPHY_LABEL.get(v.get("site_geography"), v.get("site_geography"))),
        ("Comparator", COMPARATOR_LABEL.get(v.get("comparator"), v.get("comparator"))),
        ("Primary endpoint", v.get("primary_endpoint")),
        ("Primary result", v.get("primary_result")),
        ("External validation", ext_str),
        ("Peer-reviewed", "Yes" if v.get("peer_reviewed") is True else ("No" if v.get("peer_reviewed") is False else None)),
        ("FDA decision summary", f'<a class="navy hover:underline" href="{esc(v["fda_summary_url"])}">View on accessdata.fda.gov</a>' if v.get("fda_summary_url") else None),
    ]

    rows_html = ""
    for label, value in rows:
        rows_html += (
            f'<tr class="border-t border-slate-200">'
            f'<td class="px-3 py-2 text-slate-500 text-xs uppercase tracking-wide w-56">{label}</td>'
            f'<td class="px-3 py-2 text-sm">{value if isinstance(value, str) and value.startswith("<") else or_dash(value)}</td>'
            f'</tr>'
        )

    pubs = v.get("key_publications") or []
    if pubs:
        items = []
        for p in pubs:
            label = " · ".join(filter(None, [p.get("journal"), str(p.get("year")) if p.get("year") else None]))
            pivotal = ' <span class="badge bg-slate-200 text-slate-700">pivotal</span>' if p.get("pivotal") else ""
            items.append(
                f'<li class="mb-2"><a class="navy hover:underline font-medium" href="{esc(p.get("url") or "#")}">{esc(p.get("title") or "(untitled)")}</a>{pivotal}<div class="text-xs text-slate-500">{esc(label)}</div></li>'
            )
        pubs_html = f'<h3 class="mt-6 mb-2 text-sm uppercase tracking-wide text-slate-500">Key publications</h3><ul class="text-sm">{"".join(items)}</ul>'
    else:
        pubs_html = ""

    if v.get("limitations_noted"):
        lim_html = f'<h3 class="mt-6 mb-2 text-sm uppercase tracking-wide text-slate-500">Limitations noted</h3><p class="text-sm text-slate-700">{esc(v["limitations_noted"])}</p>'
    else:
        lim_html = ""

    return (
        f'<section class="mt-8"><h2 class="text-xl font-bold navy">Validation summary</h2>'
        f'<div class="mt-3">{completeness_banner}'
        f'<table class="w-full"><tbody>{rows_html}</tbody></table>'
        f'{pubs_html}{lim_html}</div></section>'
    )


def render_regulatory(reg):
    if not reg:
        return ""
    fda = reg.get("fda_status")
    badge_cls = REG_BADGE.get(fda, "bg-slate-100 text-slate-700")
    pathway_raw = reg.get("fda_pathway")
    pathway_display = PATHWAY_LABEL.get(pathway_raw) if pathway_raw else None

    # Only show the pathway row for real FDA submission pathways.
    rows = [
        ("Regulatory status", f'<span class="badge {badge_cls}">{esc(fda) or "—"}</span>'),
        ("FDA submission pathway", pathway_display),
        ("FDA decision date", reg.get("fda_decision_date")),
        ("FDA 510(k) number", reg.get("fda_510k_number")),
        ("LDT", "Yes" if reg.get("ldt") else None),
        ("NY CLEP", reg.get("ny_clep")),
        ("CAP-accredited lab", "Yes" if reg.get("cap_accredited") else None),
        ("CLIA-certified lab", "Yes" if reg.get("clia_certified") else None),
        ("CE marked", "Yes" if reg.get("ce_marked") else None),
    ]
    rows_html = ""
    for label, value in rows:
        if value is None:
            continue
        rows_html += (
            f'<tr class="border-t border-slate-200">'
            f'<td class="px-3 py-2 text-slate-500 text-xs uppercase tracking-wide w-56">{label}</td>'
            f'<td class="px-3 py-2 text-sm">{value if isinstance(value, str) and value.startswith("<") else or_dash(value)}</td>'
            f'</tr>'
        )

    # Explanatory note for non-FDA categories.
    note_html = ""
    if fda == "LDT" and not pathway_display:
        note_html = (
            '<p class="mt-3 text-xs text-slate-600 italic">'
            "Laboratory-developed test (LDT) offered under CLIA. Not reviewed or cleared by the FDA. "
            "Validation is the responsibility of the offering CLIA-certified laboratory."
            "</p>"
        )
    elif fda == "Research Use" and not pathway_display:
        note_html = (
            '<p class="mt-3 text-xs text-slate-600 italic">'
            "Research Use Only (RUO) — not for use in clinical diagnostic procedures."
            "</p>"
        )
    elif fda == "Breakthrough Device Designation":
        note_html = (
            '<p class="mt-3 text-xs text-slate-600 italic">'
            "Breakthrough Device Designation is an FDA program that grants priority review and interactive feedback. "
            "It is not the same as FDA clearance or approval; the device may still be in pre-market development."
            "</p>"
        )

    return (
        f'<section class="mt-8"><h2 class="text-xl font-bold navy">Regulatory</h2>'
        f'<table class="w-full mt-3"><tbody>{rows_html}</tbody></table>'
        f'{note_html}</section>'
    )


def render_deployment(dep):
    if not dep:
        return ""
    rows = [
        ("Available", "Yes" if dep.get("available") else "No"),
        ("US cancer centers (est.)", dep.get("us_cancer_centers_estimated")),
        ("Patients (est.)", dep.get("patients_estimated")),
        ("Partners", ", ".join(dep.get("partners") or []) or None),
    ]
    rows_html = ""
    for label, value in rows:
        if value is None:
            continue
        rows_html += (
            f'<tr class="border-t border-slate-200">'
            f'<td class="px-3 py-2 text-slate-500 text-xs uppercase tracking-wide w-56">{label}</td>'
            f'<td class="px-3 py-2 text-sm">{or_dash(value)}</td>'
            f'</tr>'
        )
    return (
        f'<section class="mt-8"><h2 class="text-xl font-bold navy">Deployment</h2>'
        f'<table class="w-full mt-3"><tbody>{rows_html}</tbody></table></section>'
    )


def render_sources(sources):
    if not sources:
        return ""
    items = []
    for s in sources:
        meta = " · ".join(filter(None, [s.get("type"), s.get("date_accessed")]))
        items.append(
            f'<li class="mb-1"><a class="navy hover:underline" href="{esc(s.get("url"))}">{esc(s.get("url"))}</a>'
            f'<span class="text-xs text-slate-500"> · {esc(meta)}</span></li>'
        )
    return (
        f'<section class="mt-8"><h2 class="text-xl font-bold navy">Sources</h2>'
        f'<ul class="text-sm mt-3">{"".join(items)}</ul></section>'
    )


def render_page(e, last_updated):
    title = f"{e['product_name']} — OncologyAI Registry"
    cancers = ", ".join(c.replace("_", " ") for c in (e.get("cancer_types") or []))
    modality = MODALITY_LABEL.get(e.get("modality"), e.get("modality") or "")
    citation = (
        f'Elbakri A. OncologyAI Registry: {esc(e["product_name"])}. '
        f'Available at: https://oncologyairegistry.org/tools/{esc(e["id"])}.html. '
        f'Accessed [date].'
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(e.get('intended_use') or '')}">
  <link rel="canonical" href="https://oncologyairegistry.org/tools/{esc(e['id'])}.html">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', system-ui, sans-serif; }}
    .navy {{ color: #1F3A5F; }}
    .navy-bg {{ background-color: #1F3A5F; }}
    .badge {{ display: inline-block; padding: 0.15em 0.55em; border-radius: 0.35em; font-size: 0.72em; font-weight: 600; }}
  </style>
</head>
<body class="bg-white text-slate-900">

<header class="border-b">
  <div class="max-w-4xl mx-auto px-4 py-5 flex items-center justify-between">
    <div>
      <a href="../index.html" class="text-2xl font-bold navy">OncologyAI Registry</a>
      <div class="text-xs text-slate-500">Public, curated registry of AI diagnostics in oncology</div>
    </div>
    <nav class="text-sm text-slate-600 space-x-4">
      <a href="../index.html" class="hover:underline">Registry</a>
      <a href="../methodology.html" class="hover:underline">Methodology</a>
      <a href="../about.html" class="hover:underline">About</a>
    </nav>
  </div>
</header>

<main class="max-w-4xl mx-auto px-4 py-10">
  <div class="text-xs text-slate-500"><a href="../index.html" class="hover:underline">← Back to registry</a></div>
  <h1 class="text-3xl font-bold navy mt-2">{esc(e['product_name'])}</h1>
  <div class="mt-1 text-slate-600">
    <a href="{esc(e.get('company_url') or '#')}" class="hover:underline">{esc(e.get('company') or '')}</a>
  </div>
  <div class="mt-3 flex flex-wrap gap-2 text-xs">
    <span class="badge bg-slate-100 text-slate-700">{esc(modality)}</span>
    <span class="badge bg-slate-100 text-slate-700">{esc(cancers)}</span>
  </div>
  <p class="mt-4 text-slate-700">{esc(e.get('intended_use') or '')}</p>

  {render_regulatory(e.get('regulatory'))}
  {render_validation(e.get('validation'))}
  {render_deployment(e.get('deployment'))}
  {render_sources(e.get('sources'))}

  <section class="mt-10 border-t pt-6 text-sm text-slate-600">
    <div class="font-semibold text-slate-700 mb-1">How to cite this entry</div>
    <code class="block bg-slate-50 p-3 rounded text-xs">{citation}</code>
  </section>
</main>

<footer class="mt-12 border-t bg-slate-50">
  <div class="max-w-4xl mx-auto px-4 py-8 text-xs text-slate-500 flex flex-wrap justify-between gap-2">
    <div>OncologyAI Registry · last updated {esc(last_updated)} · CC BY 4.0</div>
    <div>Curator: Ahmed Elbakri</div>
  </div>
</footer>

</body>
</html>
"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(DATA.read_text())
    last_updated = data.get("last_updated", "")
    written = 0
    for e in data["entries"]:
        page_path = OUT_DIR / f"{e['id']}.html"
        page_path.write_text(render_page(e, last_updated))
        written += 1
    print(f"✅ Wrote {written} per-tool pages to {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
