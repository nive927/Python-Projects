"""
HTML on Popups - Advanced
You can even put links in the popup window.
For example, the code below will produce
a popup window with the name of the volcano
as a link which does a Google search
for that particular volcano when clicked.
"""

import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
elevation = list(data["Elev"])
vname = list(data["Volcano Name"])

# the text for displaying elevation
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[13.100883217642943, 80.24192569506516], zoom_start=3, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(latitude, longitude, elevation, vname):
    # creating an iframe for the html
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    # changing popup object to iframe
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Map.html")