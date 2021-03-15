"""
Layer Control Panel
"""

import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
elevation = list(data["Elev"])
vname = list(data["Volcano Name"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def color_producer(elev):

    if elev < 1000:
        return 'violet'
    elif 1000<= elev < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[13.100883217642943, 80.24192569506516], zoom_start=3, tiles="Stamen Terrain")

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function= lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 10000000
else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, name in zip(latitude, longitude, elevation, vname):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='black', fill=True, fill_opacity=0.9))

# This order of calling functions is very important
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")