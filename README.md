<table align="center">
<tr><td align="center" width="640">

## ▶&nbsp; [Open the interactive map](https://periplum.github.io/exoplanets/)

✨ &nbsp;The dawn of exoplanet discovery, on a celestial chart

</td></tr>
</table>

# exoplanets

[![Built with Periplum](https://img.shields.io/badge/built_with-Periplum-4da3ff)](https://periplum.js.org)

Exoplanets discovered through 2010, plotted on a celestial RA/Dec chart and coloured by
detection method (pulsar timing, radial velocity, transit, imaging, microlensing). Real
constellations are drawn for orientation. Press play to watch discoveries light up by year.

## Data & updates

[`source.py`](source.py) regenerates `data.json` from the **NASA Exoplanet Archive** TAP
service — deterministic, no manual curation (Python standard library only):

```sh
python source.py > data.json     # edit YEAR_MAX / PER to widen coverage
```

### GitHub Actions

[`.github/workflows/refresh-data.yml`](.github/workflows/refresh-data.yml) runs it
**quarterly** (and on manual *Run workflow*) and uploads the refreshed `data.json` as a
build **artifact**. The periplum org blocks Actions from pushing or opening PRs, so
download the artifact and commit it.

---

Built with [Periplum](https://periplum.js.org) · [periplum.js.org](https://periplum.js.org)
