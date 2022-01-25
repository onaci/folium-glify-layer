# folium-glify-layer [![PyPI version](https://badge.fury.io/py/folium-glify-layer.svg)](https://badge.fury.io/py/folium-glify-layer) [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://mybinder.org/v2/gh/onaci/folium-glify-layer/HEAD)

A plugin for [Folium](https://github.com/python-visualization/folium) to provide fast webgl rendering for large GeoJSON FeatureCollections (currently limited to polygons, lines and points).

For docs and examples see src, example.py, or GlifyLayer notebook.

## install

```
pip install folium-glify-layer
```

## jupyter demo

(or just follow the [binder link](https://mybinder.org/v2/gh/onaci/folium-glify-layer/HEAD))

```
conda env create -f environment.yml
conda activate folium-glify-example
jupyter lab
```

## thanks

- https://github.com/robertleeplummerjr/Leaflet.glify
- http://bl.ocks.org/Sumbera/c6fed35c377a46ff74c3
- https://github.com/mapbox/earcut
- https://github.com/gka/chroma.js
