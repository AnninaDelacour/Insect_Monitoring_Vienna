import streamlit as st
import leafmap.foliumap as leafmap
import folium
#import psycopg2
from config import read_config
import geopandas as gpd
import requests
from folium.features import CustomIcon


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
    Annina Ecker: [Mastodon](https://mastodon.world/@aeae) | [LinkedIn](https://www.linkedin.com/in/annina-ecker/)
    """
)

st.markdown("<h1 style='font-size: 70px; color: #FF8066;'>Zonenkarte Tirol</h1>", unsafe_allow_html=True)
st.markdown(
    """
    Die <strong>Zonenkarte</strong> soll dabei helfen, zu sehen, welche unterschiedlichen Gebiete in Tirol existieren, die für
    die Errichtung von Windkraftanlagen infrage kommen würden. Und genauso, welche Standorte sich wahrscheinlich weniger gut eignen. <br>
    Die Kartenlegende in der rechten unteren Hälfte der Karte gibt dir einen Überblick über die unterschiedlichen "Layer",
    die du an- und ausschalten kannst.<br>

    """, unsafe_allow_html=True)

with st.expander("HOW TO USE THE MAP:"):
    st.image("https://bachelor.blob.core.windows.net/newcontainer/zonenkartengif_neu.gif")


st.markdown("""_______________________________________ """)


m = leafmap.Map(center=[47.1133, 11.4147], zoom=8)
m.add_basemap('CartoDB.Positron')


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
power_grid = 'https://bachelor.blob.core.windows.net/newcontainer/bb_tirol_power_line.geojson'
power_plants = 'https://bachelor.blob.core.windows.net/newcontainer/power_plant.geojson'


# Use the requests library to fetch the data from the URL
schigebiet_resp = requests.get(schigebiet)
wald_wild_resp = requests.get(wald_wild_schutzzonen)
natura2000_resp = requests.get(natura_2000_ffh)
natura_vogel_resp = requests.get(natura_2000_vogelschutz)
schutzgebiete_resp = requests.get(schutzgebiete_umwelt)
wildruhe_resp = requests.get(wildruheflaechen)
ramsar_resp = requests.get(ramsar)
power_grid_resp = requests.get(power_grid)
power_plants_resp = requests.get(power_plants)

#-------#-------#-------#-------#-------#-------#

if power_grid_resp.status_code == 200:
    # Get the data from the response
    power_grid_data = power_grid_resp.json()

    folium.GeoJson(
    power_grid_data,
    name='Power Grid (Stromnetz)',
    style_function=lambda feature: {
        'aliases': 'Power Grid',
        'fillColor': '#C000F9',
        'fillOpacity': 0.8,
        'color': '#C000F9',
        'weight': 2,
        #'dashArray': '1, 1'
    }
).add_to(m)

else:
    print("Request failed with status code:", power_grid_resp.status_code)

#-------#-------#-------#-------#-------#-------#

df = gpd.read_file("https://bachelor.blob.core.windows.net/newcontainer/tirol_power_plants.geojson")

df["lon"] = df["geometry"].centroid.x
df["lat"] = df["geometry"].centroid.y

data = df.rename(columns={"geometry": "geometry", "lon": "longitude", "lat": "latitude"})

# create a new feature group for the markers
fg = folium.FeatureGroup(name="Kraftwerke")

# add the markers to the feature group
for _, row in data.iterrows():
    # create a custom icon with FontAwesome
    icon = folium.Icon(icon="bolt", prefix="fa",  color="red")
    # add the marker with the custom icon to the feature group
    folium.Marker([row['latitude'], row['longitude']],
        icon=icon,
        tooltip=row['name'],
        show=False).add_to(fg)

# add the feature group to the map
fg.add_to(m)

#-------#-------#-------#-------#-------#-------#


def add_geojson_layer(request, name, fill_color, fill_opacity, stroke_color):
    if request.status_code == 200:
        data = request.json()

        folium.GeoJson(
            data,
            name=name,
            show=False,
            style_function=lambda _: {
                'aliases': name,
                'fillColor': fill_color,
                'fillOpacity': fill_opacity,
                'color': stroke_color,
                'weight': 1,
                'dashArray': '1, 1'
            }
        ).add_to(m)
    else:
        print("Request failed with status code:", request.status_code)

add_geojson_layer(schigebiet_resp, 'Schigebiete', '#10e0ff', 0.8, '#00a0d1')
add_geojson_layer(wald_wild_resp, 'Wald- und Wildschutzzonen', '#01d669', 0.8, 'black')
add_geojson_layer(natura_vogel_resp, 'Natura 2000 Vogelschutzrichtlinie', '#FFEB2F', 0.8, '#ffb700')
add_geojson_layer(natura2000_resp, 'Natura 2000 FFH Richtlinie', '#e2348b', 0.5, 'black')
add_geojson_layer(schutzgebiete_resp, 'Umweltschutzgebiete', '#FF9300', 0.7, 'black')
add_geojson_layer(ramsar_resp, 'Ramsar (Feuchtgebiete)', '#2735ba', 0.7, '#0d41e1')
add_geojson_layer(wildruhe_resp, 'Wildruheflächen', '#ff304f', 0.6, '#000000')

#-------#-------#-------#-------#-------#-------#

# Creating Legend for Map

legend_dict = {
    "Power Grid (Stromnetz)" : "C000F9",
    "Schigebiete": "10e0ff",
    "Wald- und Wildschutzzonen": "01d669",
    "Natura 2000 FFH Richtlinien": "e2348b",
    "Umweltschutzgebiete": "FF9300",
    "Natura 2000 Vogelschutzrichtlinie": "FFEB2F",
    "Ramsar (Feuchtgebiete)": "2735ba",
    "Wildruheflächen": "ff304f",
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

st.markdown("""_______________________________________ """)

st.markdown("""
    Du fragst dich vielleicht: <strong>Wofür ist das gut?</strong><br>
    Betrachten wir folgendes Beispiel:<br>
    Du möchtest dir ansehen, wo in Tirol Schigebiete existieren, und dann herausfinden, ob in der Nähe davon
    Naturschutzgebiete sind. Beides kannst du im Layermenü am oberen rechten Rand der Karte auswählen 
    und siehst auf einen Blick, wie oftmals nahe beieinander diese Gebiete liegen. <br>
    In manchen Fällen ist es eventuell kein Zufall,
    dass ein Schigebiet von einem Naturschutzgebiet umringt ist, oder sich inmitten davon befindet.<br>""", unsafe_allow_html=True)

st.markdown("ABER - Hier hört unsere Beobachtung nicht auf!")

st.markdown("""
    Schigebiete bringen nämlich so einiges Wichtiges mit sich, wenn es um den Ausbau erneuerbarer Energien geht.<br>
    Überall dort, wo Schigebiete existieren, ist Infrastruktur vorhanden. Je nach Größe des Schigebiets wurden 
    bereits Schwertransportgüter auf Berge gebracht, womit es grundsätzlich möglich ist, 
    auch Windräder hinauf zu transportieren.
    Unsere Nachbarin, die [Schweiz](https://www.energie-experten.ch/de/wissen/detail/windenergie-in-der-schweiz-ausbau-flaute-bald-vorbei.html), 
    hat bereits gezeigt, dass es möglich ist.
    <br>
    Außerdem ist das Stromnetz in Tirol gut ausgebaut (auf der Karte als violette Linie dargestellt) 
    und führt auch hoch hinauf ins Gebirge (z.B. wegen Speicherseen). Auch das ist ein Zeichen dafür,
    dass [Schwertransporter](https://www.bautrans.cc/aktuell/news-detail/alpine-schwertransporte-fuer-speicherkraftwerk) 
    grundsätzlich die Möglichkeit haben, [Teile für Windkraftanlagen](https://www.youtube.com/watch?v=_y6VgqvnDEc) und dergleichen 
    in höher gelegene Gebiete zu transportieren.<br>
    """, unsafe_allow_html=True)

st.warning("""
Zitat:
    "[...] Dass es nicht am Geld mangelt, sondern an Prioritäten, kritisiert Biologe Essl , 
    selbst Mitglied des Biodiversitätsrats, anhand des Beispiels Niederösterreich: 
    "Das Naturschutzbudget betrug im Vorjahr 15 Millionen Euro. 
    Für den Neubau von Straßen wurden 450 Millionen Euro ausgegeben. 
    Das ist ein Verhältnis von eins zu 30." Würde man die Bevölkerung fragen, wie viel Geld für den Naturschutz 
    ausgegeben werden soll, wäre das Verhältnis sicherlich ein anderes, ist Essl überzeugt. 
    Dazu komme, dass der Straßenbau ein wesentlicher Treiber für den Verlust von Boden und die 
    Zerschneidung und Zerstörung von Naturlebensräumen sei."
    """)
st.markdown("""
        <span style='font-size:8px'>Das Zitat (und Zitat-im-Zitat) wurde entnommen aus 
        dem [Standard-Artikel vom 07. Dezember 2022.](https://www.derstandard.at/story/2000141566369/biologe-fuer-strassenbau-wird-30-mal-mehr-geld-ausgegeben-als)</span>
        """, unsafe_allow_html=True)

st.markdown(
    """
    Wir können also bereits mehrere Rückschlüsse ziehen und haben ein klareres Bild der Situation in Tirol.
    """, unsafe_allow_html=True)


st.markdown("""_______________________________________ """)

st.markdown(
    """
    Die hier verwendeten Daten wurden von [Tiris - Open Government Data](https://data-tiris.opendata.arcgis.com/) erhoben. <br>
    Die Daten zum Stromnetz sowie der Kraftwerke wurden von [OpenStreetMap](https://www.openstreetmap.org/#map=8/47.714/13.349) entommen. <br>
    Der in der Karte verwendete Kraftwerk-Icon stammt von: [Fontawesome](https://fontawesome.com/icons/)<br>
    Das verwendete Video stammt vom Youtube-Kanal: [urweidercom](https://www.youtube.com/@urweidercom)
    """, unsafe_allow_html=True)

# cur.close()
# conn.close()


#--------------------------------------#
