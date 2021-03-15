"""
HTML on Popups - Simple
Note that if you want to have stylized text
(bold, different fonts, etc) in the popup window
you can use HTML.
"""

import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
elevation = list(data["Elev"])

# the text for displaying elevation
html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[13.100883217642943, 80.24192569506516], zoom_start=3, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(latitude, longitude, elevation):
    # creating an iframe for the html
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    # changing popup object to iframe
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Map.html")