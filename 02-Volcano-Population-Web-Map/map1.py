""" 
BASE MAP
"""

import folium
import pandas

# To read the contents of the volcanoes.txt file
data = pandas.read_csv("volcanoes.txt")

# Extracting the columns into separate lists
latitude = list(data["Latitude"])
longitude = list(data["Longitude"])

# NOTE that the type of data in this list is float !
# That is why we are changing it to 
# string in the popup parameter within the for loop
elevation = list(data["Elev"])


"""
You can get them from Google Maps by right clicking
the location
Lat range: -90 to +90
Lat range: -180 to +180
"""
# Creating a Map object and setting the opening coords
# These geographical coords (lat, long) are for Chennai
map = folium.Map(location=[13.100883217642943, 80.24192569506516], zoom_start=3, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(latitude, longitude, elevation):
    # Adds the red marker with the given message on the map
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map.html")