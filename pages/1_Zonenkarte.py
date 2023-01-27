import streamlit as st
import leafmap.foliumap as leafmap
import folium
import psycopg2
from config import read_config

# Connect to the database
host = read_config('postgresql', 'host')
database = read_config('postgresql', 'database')
user = read_config('postgresql', 'user')
password = read_config('postgresql', 'password')

conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cur = conn.cursor()

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    GitHub repository: <https://github.com/AnninaDelacour/bachelor>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Annina Ecker:
    [GitHub](https://github.com/AnninaDelacour) | [LinkedIn](https://www.linkedin.com/in/annina-ecker/)
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
    st.image("/Users/annina/Downloads/zonenkarte.gif")

m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5, layer="Swiss Federal Geoportal Map")
m.add_basemap('Stamen.Toner')

# Select the GeoJSON data from the table
sql1 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM schigebiete"
cur.execute(sql1)

# Retrieve all the GeoJSON data as a list of tuples
geojson_list = cur.fetchall()

# Initialize a folium.FeatureGroup object to hold the GeoJSON features
schigebiete_layer = folium.FeatureGroup(name='Schigebiete')

# Iterate over the list of tuples and extract the GeoJSON string from each tuple
for geojson in geojson_list:
    geojson_str = geojson[0]
    
    # Pass the GeoJSON string to the folium.GeoJson function and add the resulting layer to the FeatureGroup object
    schigebiete_layer.add_child(
        folium.GeoJson(
            geojson_str,
            show = True,
            name='Schigebiete',
            style_function=lambda feature: {
                'aliases': 'Schigebiete',
                'fillColor': '#10e0ff',
                'fillOpacity': 0.8,
                'color': '#00a0d1',
                'weight': 1,
                'dashArray': '1, 1'
            }
        )
    )

# Add the FeatureGroup object to the map
schigebiete_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

sql2 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM wald_wildzonen"
cur.execute(sql2)

geojson_list = cur.fetchall()

wild_wald_layer = folium.FeatureGroup(name='Wald- und Wildschutzzonen', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    wild_wald_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Wald- und Wildschutzzonen',
            style_function=lambda feature: {
                'aliases': 'Wald- & Wild-Schutzzonen',
                'fillColor': '#01d669',
                'fillOpacity': 0.8,
                'color': 'black',
                'weight': 1,
                'dashArray': '1, 1'
                }
            )
        )
wild_wald_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

sql3 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM natura_2000_ffh"
cur.execute(sql3)

geojson_list = cur.fetchall()

natura_ffh_layer = folium.FeatureGroup(name='Natura 2000 FFH Richtlinie', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    natura_ffh_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Natura 2000 FFH Richtlinie',
            style_function=lambda feature: {
                'aliases': 'Natura 2000 FFH Richtlinie',
                'fillColor': '#ff7d00',
                'fillOpacity': 0.5,
                'color': 'black',
                'weight': 1,
                #'dashArray': '5, 5'
                }
            )
        )
natura_ffh_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

sql4 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM naturdenkmaeler"
cur.execute(sql4)

geojson_list = cur.fetchall()

naturdenk_layer = folium.FeatureGroup(name='Naturdenkmäler', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    naturdenk_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Naturdenkmäler',
            style_function=lambda feature: {
                'aliases': 'Naturdenkmäler',
                'fillColor': '#00ffd0',
                'fillOpacity': 0.8,
                'color': 'black',
                'weight': 0.5,
                'dashArray': '1, 1'
                }
            )
        )
naturdenk_layer.add_to(m)


#-------#-------#-------#-------#-------#-------#

sql5 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM umwelt_schutzgebiete"
cur.execute(sql5)

geojson_list = cur.fetchall()

schutz_umwelt_layer = folium.FeatureGroup(name='Schutzgebiete Umwelt', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    schutz_umwelt_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Schutzgebiete Umwelt',
            style_function=lambda feature: {
                'aliases': 'Schutzgebiete Umwelt',
                'fillColor': '#821cff',
                'fillOpacity': 0.5,
                'color': 'black',
                'weight': .1,
                'dashArray': '2, 2'
                }
            )
        )
schutz_umwelt_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

sql6 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM natura_2000_vogelschutz"
cur.execute(sql6)

geojson_list = cur.fetchall()

vogelschutz_layer = folium.FeatureGroup(name='Natura 2000 Vogelschutzrichtlinie', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    vogelschutz_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Natura 2000 Vogelschutzrichtlinie',
            style_function=lambda feature: {
                'aliases': 'Natura 2000 Vogelschutzrichtlinie',
                'fillColor': '#ffce00',
                'fillOpacity': 0.4,
                'color': '#ffb700',
                'weight': 0.8,
                'dashArray': '1, 1'
                }
            )
        )
vogelschutz_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

sql7 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM ramsar_gebiete"
cur.execute(sql7)

geojson_list = cur.fetchall()

ramsar_layer = folium.FeatureGroup(name='Ramsar (Feuchtgebiete)', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    ramsar_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Ramsar (Feuchtgebiete)',
            style_function=lambda feature: {
                'aliases': 'Ramsar (Feuchtgebiete)',
                'fillColor': '#0d41e1',
                'fillOpacity': 0.7,
                'color': '#00aaff',
                'weight': 0.8,
                'dashArray': '1, 1'
                }
            )
        )
ramsar_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

sql7 = "SELECT ST_AsGeoJSON(wkb_geometry) FROM wildruheflaechen"
cur.execute(sql7)

geojson_list = cur.fetchall()

wildruhefl_layer = folium.FeatureGroup(name='Wildruheflächen', show=False)

for geojson in geojson_list:
    geojson_str = geojson[0]
    
    wildruhefl_layer.add_child(
        folium.GeoJson(
            geojson_str,
            name='Wildruheflächen',
            style_function=lambda feature: {
                'aliases': 'Wildruhefläclhen',
                'fillColor': '#ff304f',
                'fillOpacity': 0.4,
                'color': '#ff304f',
                'weight': 0.9,
                #'dashArray': '1, 1'
                }
            )
        )
wildruhefl_layer.add_to(m)

#-------#-------#-------#-------#-------#-------#

# Creating Legend for Map

legend_dict = {
    "Schigebiete": "10e0ff",
    "Wald- und Wildschutzzonen": "01d669",
    "Natura 2000 FFH Richtlinien": "ff7d00",
    "Naturdenkmäler": "00ffd0",
    "Schutzgebiete Umwelt": "ffce00",
    "Natura 2000 Vogelschutzrichtlinie": "ffb700",
    "Ramsar (Feuchtgebiete)": "00aaff",
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

cur.close()
conn.close()