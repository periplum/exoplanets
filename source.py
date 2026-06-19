#!/usr/bin/env python3
"""Refresh exoplanet data from the NASA Exoplanet Archive (the proper, evolving source).

Queries the Archive's TAP service for confirmed planets with sky coordinates and a
discovery year, and prints Periplum canonical items — each placed on the celestial
basemap by RA/Dec, coloured by discovery method, dated by discovery year.

Default scope is the formative era (<= 2010), sampled for method diversity so the
map stays legible. Edit YEAR_MAX / PER to change.

    python source.py > data.json
"""

import json
import sys
import urllib.parse
import urllib.request
from collections import defaultdict

TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
YEAR_MAX = 2010
# Max planets kept per discovery method (earliest first), for a diverse, legible map.
PER = {"Radial Velocity": 14, "Transit": 14, "Imaging": 10, "Microlensing": 8,
       "Pulsar Timing": 6, "Pulsation Timing Variations": 4, "Transit Timing Variations": 4,
       "Eclipse Timing Variations": 4, "Astrometry": 4, "Orbital Brightness Modulation": 4}
COLORS = {"Radial Velocity": "#4da3ff", "Transit": "#ff7f0e", "Imaging": "#2ca02c",
          "Microlensing": "#d62728", "Pulsar Timing": "#b07fff",
          "Pulsation Timing Variations": "#f4c430", "Transit Timing Variations": "#f4c430",
          "Eclipse Timing Variations": "#e377c2", "Astrometry": "#17becf"}


def fetch():
    q = ("select pl_name,ra,dec,disc_year,discoverymethod from ps "
         "where default_flag=1 and ra is not null and disc_year is not null "
         f"and disc_year <= {YEAR_MAX} order by disc_year asc")
    url = TAP + "?" + urllib.parse.urlencode({"query": q, "format": "json"})
    with urllib.request.urlopen(url, timeout=90) as r:
        return json.load(r)


def main():
    rows = fetch()
    seen = defaultdict(int)
    picked = []
    for r in rows:
        m = r["discoverymethod"]
        if seen[m] < PER.get(m, 4):
            seen[m] += 1
            picked.append(r)
    picked.sort(key=lambda r: (r["disc_year"], r["pl_name"]))
    items = [{
        "name": r["pl_name"], "date": f"{r['disc_year']}-01-01", "status": r["discoverymethod"],
        "placements": [{"map": "sky", "ra": round(r["ra"], 4), "dec": round(r["dec"], 4),
                        "label": r["pl_name"],
                        "popup": {"Method": r["discoverymethod"], "Discovered": str(r["disc_year"])}}],
    } for r in picked]
    print(f"# {len(items)} planets, methods: {dict(seen)}", file=sys.stderr)
    json.dump({"items": items}, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
