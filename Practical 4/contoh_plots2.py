import numpy as np
import pandas as pd

# --------------------------------------------------------------
# Contoh 5-2
# --------------------------------------------------------------
import folium
import webbrowser

# Siapkan sebuah object yang bertipe Map
# Cari latitude and longitude sebuah lokasi menggunakan https://www.latlong.net/
# dan gunakan untuk menampilkan area tersebut 
m = folium.Map(location=[-7.250445, 112.768845], zoom_start=12)  # Surabaya
m = folium.Map(location=[40, -95], zoom_start=4)                 # Amerika Serikat

# Siapkan data di tiap area yang akan diterjemahkan menjadi warna tertentu untuk area tsb.
state_data = pd.read_csv("US_Unemployment_Oct2012.csv")

folium.Choropleth(
    name="contoh_dari_choropleth",

    # Silakan baca format dari isi file geolocation di https://en.wikipedia.org/wiki/GeoJSON
    geo_data="us-states.json",  key_on="feature.id",

    data=state_data, columns=["State", "Unemployment"],

    fill_color="YlGn", fill_opacity=0.7, line_opacity=.1,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.Marker(
    location=[40.417286, -82.907120],
    tooltip="Click meeee!",
    popup="This is OHIO",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.LayerControl().add_to(m)

m.save("map.html")
webbrowser.open("map.html")