import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="folium-glify-layer",
    version="0.2.0",
    description="Folium plugin to provide fast webgl rendering for GeoJSON FeatureCollections.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/onaci/folium-glify-layer",
    author="Dan Wild",
    author_email="Daniel.Wild@csiro.au",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["folium_glify_layer"],
)