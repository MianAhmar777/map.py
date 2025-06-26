# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 23:28:36 2025

@author: Ahmar
"""

import folium
from geopy.geocoders import Nominatim

# Create a geolocator object
geolocator = Nominatim(user_agent="my_geocoder_app")

# Get user input for an address
address = input("Enter an address to map: ")

# Get location details
location = geolocator.geocode(address)

# Check if location is found
if location:
    lat, lon = location.latitude, location.longitude
else:
    print("Address not found. Defaulting to White House.")
    lat, lon = 38.8977, -77.0365  # Default to White House, Washington DC

# Create a map centered at the location
m = folium.Map(location=[lat, lon], zoom_start=15)

# Add a marker for the location
folium.Marker(
    location=[lat, lon],
    popup=f"{address}",
    icon=folium.Icon(color="blue")
).add_to(m)

# Save the map as an HTML file
map_file = "my_location.html"
m.save(map_file)

# Open the map in a web browser
import webbrowser
webbrowser.open(map_file)

print(f"Map generated! Open {map_file} in your browser.")
