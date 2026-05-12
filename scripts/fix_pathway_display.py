#!/usr/bin/env python3
"""One-time fix: null out fda_pathway when it just restates a non-FDA status.

LDTs and Research-Use products do not have an FDA submission pathway.
Listing fda_pathway='ldt' or 'research_use' is noise — those are statuses,
not pathways. After this fix, fda_pathway is only populated for entries
that actually went through an FDA pathway (510(k), De Novo, PMA, Breakthrough).

Idempotent.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "v1" / "data.json"

NON_FDA_PATHWAY_VALUES = {"ldt", "research_use"}


def main():
    data = json.loads(DATA.read_text())
    fixed = 0
    for e in data["entries"]:
        r = e.get("regulatory") or {}
        if r.get("fda_pathway") in NON_FDA_PATHWAY_VALUES:
            r["fda_pathway"] = None
            fixed += 1
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Cleared fda_pathway on {fixed} entries (was 'ldt' or 'research_use').")


if __name__ == "__main__":
    main()
