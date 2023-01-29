import streamlit as st
import leafmap.foliumap as leafmap
import folium
#import psycopg2
from config import read_config
import geopandas as gpd
import requests

# Connect to the database
#host = read_config('postgresql', 'host')
#database = read_config('postgresql', 'database')
#user = read_config('postgresql', 'user')
#password = read_config('postgresql', 'password')

#conn = psycopg2.connect(host=host, database=database, user=user, password=password)
#cur = conn.cursor()

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    GitHub repository: [Annina Delacour](https://github.com/AnninaDelacour/bachelor)
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Annina Ecker: [Mastodon](https://mastodon.world/@aeae) | [LinkedIn](https://www.linkedin.com/in/)
    """
)

st.title("Zonenkarte Tirol")
st.markdown(
    """
    Die <strong>Zonenkarte Tirol</strong> soll als Übersichtshilfe dienen, um einen Eindruck zu erhalten, 
    welche unterschiedlichen Zonen, Schutzgebiete etc., existieren. Diese sind von großer Bedeutung und sind eine Orientierungshilfe,
    um so direkt zu erkennen, wo potentielle Standortmöglichkeiten zur Errichtung von Kraftwerken für die Abschöpfung von Windenergie sind.
    <br>
    Zum Beispiel:<br>
    Überall dort, wo Schigebiete existieren, ist Infrastruktur prinzipiell vorhanden. Je nach Größe des Schigebiets wurden 
    auch somit bereits Schwertransportgüter auf Berge gebracht, womit es grundsätzlich möglich ist, auch Windräder hinauf zu transportieren.
    <br>
    Viele Schigebiete grenzen direkt an Naturschutzgebiete oder befinden sich inmitten dieser. Auch diesen Fakt gilt es genauer 
    zu prüfen und hinterfragen; besonders, wenn es um ein zukünftig gesundes und nachhaltiges Miteinander für Mensch und Tier geht.
    <br>

    Die hier verwendeten Daten wurden von https://data-tiris.opendata.arcgis.com/ erhoben.

    """, unsafe_allow_html=True)

with st.expander("HOW TO USE THE MAP:"):
    st.write(""" Mithilfe des Karten-Layermenüs (Karte: rechts oben) können unterschiedliche Layer ein- und ausgeschaltet 
    werden.""")
    st.image("https://github.com/AnninaDelacour/bachelor/blob/main/zonenkarte.gif?raw=true")

m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5, layer="Swiss Federal Geoportal Map")
m.add_basemap('Stamen.Toner')


#-------#-------#-------#-------#-------#-------#

# THIS SECTION IS COMMENTED OUT BECAUSE THERE WAS NO FREE HOSTING OF THE POSTGRESQL DB
# CODE IS LEFT HERE FOR A BETTER UNDERSTANDING IN HOW THE IMPLEMENTATION WOULD LOOK LIKE WITH A CONNECTION TO A DB

# Select the GeoJSON data from the table
#sql1 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM schigebiete"
#cur.execute(sql1)

# Retrieve all the GeoJSON data as a list of tuples
#geojson_list = cur.fetchall()

# Initialize a folium.FeatureGroup object to hold the GeoJSON features
#schigebiete_layer = folium.FeatureGroup(name='Schigebiete')

# Iterate over the list of tuples and extract the GeoJSON string from each tuple
#for geojson in geojson_list:
#    geojson_str = geojson[0]
    
    # Pass the GeoJSON string to the folium.GeoJson function and add the resulting layer to the FeatureGroup object
    # schigebiete_layer.add_child(
        # folium.GeoJson(
#             geojson_str,
#             show = True,
#             name='Schigebiete',
#             style_function=lambda feature: {
#                 'aliases': 'Schigebiete',
#                 'fillColor': '#10e0ff',
#                 'fillOpacity': 0.8,
#                 'color': '#00a0d1',
#                 'weight': 1,
#                 'dashArray': '1, 1'
#             }
#         )
#     )

# Add the FeatureGroup object to the map
# schigebiete_layer.add_to(m)


#-------#-------#-------#-------#-------#-------#


#geojson
schigebiet = 'https://bachelor.blob.core.windows.net/newcontainer/URP_Schigebietsgrenzen.geojson'
wald_wild_schutzzonen = 'https://bachelor.blob.core.windows.net/newcontainer/Wald_und_Wildschutzzonen.geojson'
natura_2000_ffh = 'https://bachelor.blob.core.windows.net/newcontainer/Natura_2000_FFH_Richtlinie.geojson'
natura_2000_vogelschutz = 'https://bachelor.blob.core.windows.net/newcontainer/Natura_2000_Vogelschutzrichtlinie.geojson'
schutzgebiete_umwelt = 'https://bachelor.blob.core.windows.net/newcontainer/Schutzgebiete_Umwelt.geojson'
ramsar = 'https://bachelor.blob.core.windows.net/newcontainer/Ramsar_Gebiete.geojson'
wildruheflaechen = 'https://bachelor.blob.core.windows.net/newcontainer/Wildruheflaechen_Tirol.geojson'


# Use the requests library to fetch the data from the URL
schigebiet_resp = requests.get(schigebiet)
wald_wild_resp = requests.get(wald_wild_schutzzonen)
natura2000_resp = requests.get(natura_2000_ffh)
natura_vogel_resp = requests.get(natura_2000_vogelschutz)
schutzgebiete_resp = requests.get(schutzgebiete_umwelt)
wildruhe_resp = requests.get(wildruheflaechen)
ramsar_resp = requests.get(ramsar)


# Check if the request was successful
if schigebiet_resp.status_code == 200:
    # Get the data from the response
    schi_data = schigebiet_resp.json()

    folium.GeoJson(
    schi_data,
    name='Schigebiete',
    style_function=lambda feature: {
        'aliases': 'Schigebiete',
        'fillColor': '#10e0ff',
        'fillOpacity': 0.8,
        'color': '#00a0d1',
        'weight': 1,
        'dashArray': '1, 1'
    }
).add_to(m)

else:
    print("Request failed with status code:", schigebiet_resp.status_code)

    #-------#-------#-------#-------#-------#-------#

if wald_wild_resp.status_code == 200:
    wald_wild_data = wald_wild_resp.json()

    folium.GeoJson(
    wald_wild_data,
    name='Wald- und Wildschutzzonen',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Wald- & Wild-Schutzzonen',
        'fillColor': '#01d669',
        'fillOpacity': 0.8,
        'color': 'black',
        'weight': 1,
        'dashArray': '1, 1'
    }
).add_to(m)
else:
    print("Request failed with status code:", wald_wild_resp.status_code)

#-------#-------#-------#-------#-------#-------#


if natura_vogel_resp.status_code == 200:
    natura_vogel_data = natura_vogel_resp.json()

    folium.GeoJson(
    natura_vogel_data,
    name='Natura 2000 Vogelschutzrichtlinie',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Natura 2000 Vogelschutzrichtlinie',
        'fillColor': '#ffce00',
        'fillOpacity': 0.8,
        'color': '#ffb700',
        'weight': 0.8,
        'dashArray': '1, 1'
    }
).add_to(m)

else:
    print("Request failed with status code:", natura_vogel_resp.status_code)


#-------#-------#-------#-------#-------#-------#

if natura2000_resp.status_code == 200:
    natura2000_data = natura2000_resp.json()

    folium.GeoJson(
    natura2000_data,
    name='Natura 2000 FFH Richtlinie',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Natura 2000 FFH Richtlinie',
        'fillColor': '#e2348b',
        'fillOpacity': 0.5,
        'color': 'black',
        'weight': 1,
        #dashArray': '5, 5'
    }
).add_to(m)

else:
    print("Request failed with status code:", natura2000_resp.status_code)

#-------#-------#-------#-------#-------#-------#

if schutzgebiete_resp.status_code == 200:
    schutzgebiete_data = schutzgebiete_resp.json()

    folium.GeoJson(
    schutzgebiete_data,
    name='Schutzgebiete Umwelt',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Schutzgebiete Umwelt',
        'fillColor': '#a9e04a',
        'fillOpacity': 0.7,
        'color': 'black',
        'weight': 0.3,
        'dashArray': '2, 2'
    }
).add_to(m)

else:
    print("Request failed with status code:", schutzgebiete_resp.status_code)

#-------#-------#-------#-------#-------#-------#

if ramsar_resp.status_code == 200:
    ramsar_data = ramsar_resp.json()

    folium.GeoJson(
    ramsar_data,
    name='Ramsar (Feuchtgebiete)',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Ramsar (Feuchtgebiete)',
        'fillColor': '#2735ba',
        'fillOpacity': 0.7,
        'color': '#0d41e1',
        'weight': 0.8,
        'dashArray': '1, 1'
    }
).add_to(m)

else:
    print("Request failed with status code:", ramsar_resp.status_code)

#-------#-------#-------#-------#-------#-------#


if wildruhe_resp.status_code == 200:
    wildruhe_data = wildruhe_resp.json()

    folium.GeoJson(
    wildruhe_data,
    name='Wildruheflächen',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Wildruhefläclhen',
        'fillColor': '#ff304f',
        'fillOpacity': 0.6,
        'color': '#000000',
        'weight': 0.9,
                }
).add_to(m)

else:
    print("Request failed with status code:", wildruhe_resp.status_code)

#-------#-------#-------#-------#-------#-------#

# Creating Legend for Map

legend_dict = {
    "Schigebiete": "10e0ff",
    "Wald- und Wildschutzzonen": "01d669",
    "Natura 2000 FFH Richtlinien": "e2348b",
    "Schutzgebiete Umwelt": "a9e04a",
    "Natura 2000 Vogelschutzrichtlinie": "ffce00",
    "Ramsar (Feuchtgebiete)": "2735ba",
    "Wildruheflächen": "ff304f"
}

style = {
    'position': 'fixed',
    'z-index': '9999',
    'border': '2px solid grey',
    'background-color': 'rgba(255, 255, 255, 0.8)',
    'border-radius': '10px',
    'padding': '5px',
    'font-size': '14px',
    'bottom': '20px',
    'right': '5px',
}

m.add_legend(
    title="Übersicht Zonen",
    legend_dict=legend_dict,
    draggable=False,
    style=style
)

m.to_streamlit(height=800)

# cur.close()
# conn.close()