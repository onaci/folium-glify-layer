import json
import requests
import folium
from folium_glify_layer import GlifyLayer, Popup, Tooltip

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
us_states = f"{url}/us-states.json"
geo_json_data = json.loads(requests.get(us_states).text)

m = folium.Map([43, -100], zoom_start=4)

color = """\
function(index, feature){
    return {
        r: Math.random(),
        g: Math.random(),
        b: Math.random()
    }
}   
"""

popup = Popup({
    'fields': ["name"],
    'aliases': ["State"],
    'labels': True
})

tooltip = Tooltip({
    'fields': ["name"],
    'aliases': ["State"],
    'labels': True,
    'timeout_ms': 5000,
    'offset': [10, 10],
    'styles': {
        'background-color': '#CCC'
    }
})

layer = GlifyLayer({ 'shapes': geo_json_data }, color_function=color, tooltip=tooltip)
layer.add_to(m)
m