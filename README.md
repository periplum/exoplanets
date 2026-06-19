# exoplanets — the dawn of discovery, on a sky chart

[![Built with Periplum](https://img.shields.io/badge/built_with-Periplum-4da3ff)](https://periplum.js.org)

The formative era of exoplanet discovery (through 2010), each planet plotted on a
**celestial RA/Dec chart** and coloured by **detection method** — from the 1992 pulsar
planets and 1995's 51 Pegasi b to the first transits, direct images, and microlensing
finds. A different *projection*, same Periplum engine.

**[▶ Open the map](https://periplum.github.io/exoplanets/)** — press play to watch
discoveries light up across the sky in order, or drag the date slider. Real constellations
(Orion, Cygnus, Cassiopeia…) are drawn for orientation.

## Data

`data.json` comes from the **[NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)**
(the proper, evolving source) via its TAP service. [`source.py`](source.py) regenerates it:

```sh
python source.py > data.json
```

It samples for method diversity so the chart stays legible; edit `YEAR_MAX`/`PER` to widen
it. A showcase consumer of **[Periplum](https://github.com/periplum/periplum)**.
