import streamlit as st
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca
import branca.colormap as cm
import matplotlib.pyplot as plt
import datetime as dt
import datetime
from dateutil.relativedelta import relativedelta
import rasterio
import rasterio.warp
import matplotlib.colors as mcolors

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

st.markdown("<h1 style='font-size: 70px; color: #FF8066;'>Windkarten</h1>", unsafe_allow_html=True)

st.header("Was zeigen diese Windkarten an und wie kann man diese Daten interpretieren?")

st.markdown("""
Die hier angezeigten Windkarten geben unterschiedliche Informationen wieder:

- Die durchschnittliche Windgeschwindigkeit
- Die Anzahl der Tage mit Windstärke über 6 Bft (Beaufort)
- Die Anzahl der Tage mit Böen über 80 km/h
- Die aktuellen Windstärken, -richtungen und -prognosen

In jeder Karte ist im rechten oberen Bereich eine Legende, welche bei der Interpretation der Daten helfen soll.
Dort sind die jeweiligen Unter- und Obergrenzen eingetragen.
<br>Sind in der Karte "Windgeschwindigkeit Monatsmittel" viele Felder der 
Heatmap gelb, bedeutet dies eine durchschnittliche Windgeschwindigkeit im Monat bei ca. 4-7 m/s für das jeweilige Gebiet.
Wichtig ist zu verstehen, dass diese Daten eine grobe Schätzung sind für ein gesamtes Gebiet. Das hat den Grund, da die Werte 
von Wetterstationen stammen (also von einem Standort) und somit nur für den jeweiligen Standort genau und präzise sind.<br>
Es gibt durchaus genauere Karten, wie beispielsweise die [<strong>GTIF</strong>-Karte (Green Transition Information Factory)
der Europäischen Raumfahrtbehörde (ESA)](https://gtif.esa.int/explore?x=1268308.6002&y=5986946.61913&z=9.04127), die du dir 
auf jeden Fall ansehen solltest. So kannst du dir selbst einen vollumfänglichen Eindruck machen! :-) <br><br>

Die letzte Karte, <strong>"Windy"</strong>, wurde 2014 von [Ivo](https://community.windy.com/topic/4/about-windy) entwickelt 
und stellt Wetterinformationen und Vorhersagen in Echtzeit bereit. Auf der Webseite von Windy sind in der kostenlosen Version
Radar-, Satelliten-, Temperatur- und Luftdruckkarten zu finden sowie andere Features.<br>
Hier in dieser Webseite ist die Windkarte von <strong>Windy</strong> eingebettet. Mithilfe der hier verfügbaren Informationen 
zu Wind sollte es einfach(er) fallen, die Daten von Windy interpretieren zu können.

""", unsafe_allow_html=True)

st.markdown("""
Die Daten der ersten drei Karten stammen aus der Datenbank des [GeoSphere DataHubs](https://data.hub.zamg.ac.at/). 
Dargestellt werden die unterschiedlichen Daten als sogenannte Heatmap.
""", unsafe_allow_html=True)

st.markdown("""_______________________________________ """)

st.header("Windgeschwindigkeit Monatsmittel")


with st.expander("HOW TO USE THE MAP:"):
    st.write(""" Mittels der Dropdown-Liste können verschiedene Monate, vom Jänner 2012 beginnend bis Jänner 2022 ausgewählt werden.""")
    st.image("https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/images/gifs/windkarte.gif")


# Color gradient for heatmap 
colors = ['#9e0142', '#cb334d', '#f57245', '#fdbf6f', '#fff2aa', '#eaf79e', '#a4daa4', '#54aead', '#4d65ad', '#5e4fa2']
color_dict = {}

for i in range(len(colors)):
    color_dict[round(i/len(colors), 1)] = colors[i]

#-------#-------#-------#-------#-------#-------#-------#

# Load the data from the CSV file into a Pandas dataframe
df = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/monatl_wdata_vv_2012_2022.csv')

# Convert the Latitude, Longitude, and vv columns to numeric values
df['Latitude'] = pd.to_numeric(df['Latitude'])
df['Longitude'] = pd.to_numeric(df['Longitude'])
df['vv'] = pd.to_numeric(df['vv'])

# Extract the month from the timestamp column and create a new column that contains the month and year in the format YYYY-MM
df['month_year'] = df['time'].apply(lambda x: x[:7])

# Group the data by the month and year and calculate the mean wind speed for each group
wind_speed_by_month = df.groupby('month_year')['vv'].mean()

# Initialize the map
m = leafmap.Map(center=[47.1133, 11.4147], zoom=7.5)

# Get a list of the unique month and year values in the 'month_year' column
month_year_values = df['month_year'].unique()


def get_selected_month_year_data(selected_month_year):
    # Filter the data to only include rows with the selected month and year
    filtered_df = df[df['month_year'] == selected_month_year]
    return filtered_df


# ---- Date Picker ---- #

selected_month_year = st.selectbox("Wähle Jahr/Monat (beginnend im Jänner 2012):", month_year_values, key='windgeschwindigkeits-datepicker-key')

# Get the selected month and year data
filtered_df = get_selected_month_year_data(selected_month_year)
st.write(f"Derzeitiges Jahr/Monat: {selected_month_year}")

filtered_df = df[df['month_year'] == selected_month_year]

# ---- ********** ---- #

# Create a GeoJSON feature collection for the filtered data
geo_json_data = {
    'type': 'FeatureCollection',
    'features': [{
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['Longitude'], row['Latitude']]
        },
        'properties': {
            'vv': row['vv']
        }
    } for _, row in filtered_df.iterrows()]
}

# Create a heatmap layer from the GeoJSON data and add it to the map
HeatMap(
    filtered_df[["Latitude", "Longitude", "vv"]],
    latitude="Latitude",
    longitude="Longitude",
    value="vv",
    radius=30,
    blur= 10,
    gradient = color_dict,
).add_to(folium.FeatureGroup(name="Windgeschwindigkeit Monatsmittel")).add_to(m)


colors = ['#9e0142', '#cb334d', '#f57245', '#fdbf6f', '#fff2aa', '#eaf79e', 
              '#a4daa4', '#54aead', '#4d65ad', '#5e4fa2']
vmin = 0
vmax = 20

colormap = cm.LinearColormap(colors=colors, vmin=vmin, vmax=vmax, caption='Windgeschwindigkeit (Monatsmittel) in m/s')
m.add_child(colormap)

svg_style = '<style>svg {background-color: white;}</style>'
m.get_root().header.add_child(folium.Element(svg_style))
colormap.add_to(m)

m.to_streamlit(height=700)

st.markdown(""" 
Da moderne Windkraftanlagen fast alle nur drei Rotorblätter haben, 
benötigen sie zum Anlaufen eine Windgeschwindigkeit von mindestens vier bis fünf Meter pro Sekunde.
Dadurch wird der Raum für mögliche Standorte von Windenergieanlagen begrenzt.
Damit ein Windrad sich dreht, braucht es kontinuierlich eine bestimmte Windgeschwindigkeit von etwa 3 Metern pro Sekunde.

Bei sehr schwachem Wind (unter 2,5 m/s) produziert die Windenergieanlage keinen elektrischen Strom: 
Der Wind ist zu schwach, um die Rotorwelle anzutreiben.
Die Blätter sind in so genannter Fahnenstellung (Pitchwinkel ≈ 90°) gedreht.
Die Windenergieanlage steht still oder dreht sehr langsam, was Trudelbetrieb genannt wird.

Bei normalem Wind (2,5 m/s bis 12 m/s) dreht die Windenergieanlage und produziert Leistung, 
aber der Wind ist noch zu schwach, um die Nennleistung der Anlage zu erreichen.
Der Pitchwinkel ist 0°, die Rotorblätter stehen im optimalen Arbeitspunkt.
Von der Windleistung wird so viel wie möglich in mechanische Energie umgewandelt.
Mit zunehmender Windgeschwindigkeit erhöht sich auch gleichermaßen die Drehzahl („drehzahlvariabler Betrieb“), 
um die Schnelllaufzahl konstant und damit den Wirkungsgrad optimal zu halten.

Quellen:
- [Stadtwerke Münster - Warum sich ein Windrad nicht immer dreht](https://www.stadtwerke-muenster.de/blog/energie/warum-sich-ein-windrad-nicht-immer-dreht/)
- [WindEnergie - Funktionsweise: Leistungsbegrenzung und -regelung von Windenergieanlagen](https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/leistungsbegrenzung/)

""", unsafe_allow_html=True)

st.markdown("""_______________________________________ """)

#-------#-------#-------#-------#-------#-------#-------#

# get csv file
# filepath = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/df_zamg_21_22.csv')

st.header("Zahl der Tage mit Windstärke >= 6 Bft")

# Load the data from the CSV file into a Pandas dataframe
df = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/monatl_wdata_w6_2012_2022.csv')

# Convert the Latitude, Longitude, and vv columns to numeric values
df['Latitude'] = pd.to_numeric(df['Latitude'])
df['Longitude'] = pd.to_numeric(df['Longitude'])
df['w6'] = pd.to_numeric(df['w6'])

# Extract the month from the timestamp column and create a new column that contains the month and year in the format YYYY-MM
df['month_year'] = df['time'].apply(lambda x: x[:7])

# Group the data by the month and year and calculate the mean wind speed for each group
wind_speed_by_month = df.groupby('month_year')['w6'].mean()

# Initialize the map
m = leafmap.Map(center=[47.1133, 11.4147], zoom=7.5)

# Get a list of the unique month and year values in the 'month_year' column
month_year_values = df['month_year'].unique()


def get_selected_month_year_data(selected_month_year):
    # Filter the data to only include rows with the selected month and year
    filtered_df = df[df['month_year'] == selected_month_year]
    return filtered_df


# ---- Date Picker ---- #

selected_month_year = st.selectbox("Wähle Jahr/Monat (beginnend im Jänner 2012):", month_year_values, 
key='windboeen-datepicker-key')

# Get the selected month and year data
filtered_df = get_selected_month_year_data(selected_month_year)
st.write(f"Derzeitiges Jahr/Monat: {selected_month_year}")

filtered_df = df[df['month_year'] == selected_month_year]

# ---- ********** ---- #

# Create a GeoJSON feature collection for the filtered data
geo_json_data = {
    'type': 'FeatureCollection',
    'features': [{
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['Longitude'], row['Latitude']]
        },
        'properties': {
            'w6': row['w6']
        }
    } for _, row in filtered_df.iterrows()]
}

# Create a heatmap layer from the GeoJSON data and add it to the map

HeatMap(
    filtered_df[["Latitude", "Longitude", "w6"]],
    latitude="Latitude",
    longitude="Longitude",
    value="w6",
    radius=30,
    blur=10,
    gradient= color_dict,
).add_to(folium.FeatureGroup(name="Windgeschwindigkeit Monatsmittel")).add_to(m)


colors = ['#9e0142', '#cb334d', '#f57245', '#fdbf6f', '#fff2aa', '#eaf79e', 
              '#a4daa4', '#54aead', '#4d65ad', '#5e4fa2']
vmin = 0.0
vmax = 30.0

colormap = cm.LinearColormap(colors=colors, vmin=vmin, vmax=vmax, caption='Anzahl der Tage mit Windstärke >= 6 Bft')
m.add_child(colormap)

svg_style = '<style>svg {background-color: white;}</style>'
m.get_root().header.add_child(folium.Element(svg_style))
colormap.add_to(m)

m.to_streamlit(height=700)

st.markdown("""
Die Beaufortskala (Bft) ist eine Skala zur Einteilung der Windstärke in 13 Stärkenbereiche von 0 (Windstille) bis 12 (Orkan), die nicht auf exakten Messungen, sondern den beobachteten Auswirkungen des Windes basiert. 
Sie ist benannt nach Sir Francis Beaufort und ein weit verbreitetes System zur Beschreibung der Windstärke.

Beaufort-Skala nach phänomenologischen Kriterien: 
- <span style="color: #0089FF">0 Bft: 0 bis 1 kn</span> | <span style="color: #FF2372">0 bis 0.2 m/s</span> | <span style="color: #00B141">0 bis 1 km/h</span> | Windstille, Flaute
- <span style="color: #0089FF">1 Bft: 1 bis 4 kn</span> | <span style="color: #FF2372">0.3 bis 1.5 m/s</span> | <span style="color: #00B141">1 bis 5 km/h</span> | leiser Zug
- <span style="color: #0089FF">2 Bft: 4 bis 6 kn</span> | <span style="color: #FF2372">1.6 bis 3.3 m/s</span> | <span style="color: #00B141">6 bis 11 km/h</span> | leichte Brise
- <span style="color: #0089FF">3 Bft: 7 bis 10 kn</span> | <span style="color: #FF2372">3.4 bis 5.4 m/s</span> | <span style="color: #00B141">12 bis 19 km/h</span> | schwache Brise
- <span style="color: #0089FF">4 Bft: 11 bis 15 kn</span> | <span style="color: #FF2372">5.5 bis 7.9 m/s</span> | <span style="color: #00B141">20 bis 28 km/h</span> | mäßige Brise
- <span style="color: #0089FF">5 Bft: 16 bis 21 kn</span> | <span style="color: #FF2372">8.0 bis 10.7 m/s</span> | <span style="color: #00B141">29 bis 38 km/h</span> | frische Brise, frischer Wind
- <span style="color: #0089FF">6 Bft: 22 bis 27 kn</span> | <span style="color: #FF2372">10.8 b is 13.8 m/s</span> | <span style="color: #00B141">39 bis 49 km/h</span> | starker Wind
- <span style="color: #0089FF">7 Bft: 28 bis 33 kn</span> | <span style="color: #FF2372">13.9 bis 17.1 m/s</span> | <span style="color: #00B141">50 bis 61 km/h</span> | steifer Wind
- <span style="color: #0089FF">8 Bft: 34 bis 40 kn</span> | <span style="color: #FF2372">17.2 bis 20.7 m/s</span> | <span style="color: #00B141">62 bis 74 km/h</span> | stürmischer Wind
- <span style="color: #0089FF">9 Bft: 41 bis 47 kn</span> | <span style="color: #FF2372">20.8 bis 24.4 m/s</span> | <span style="color: #00B141">75 bis 88 km/h</span> | Sturm
- <span style="color: #0089FF">10 Bft: 48 bis 55 kn</span> | <span style="color: #FF2372">24.5 bis 28.4 m/s</span> | <span style="color: #00B141">89 bis 102 km/h</span> | schwerer Sturm
- <span style="color: #0089FF">11 Bft: 56 bis 63 kn</span> | <span style="color: #FF2372">28.5 bis 32.6 m/s</span> | <span style="color: #00B141">103 bis 117 km/h</span> | Orkanartiger Sturm
- <span style="color: #0089FF">12 Bft: >64 kn</span> | <span style="color: #FF2372">> 32.7 m/s</span> | <span style="color: #00B141">> 118 km/h</span> | Orkan

Üblicherweise wird ab einer Windgeschwindigkeit von rund neun bis zwölf m/s die aus der Auftriebskraft resultierende Rotorleistung durch aerodynamische Maßnahmen begrenzt, 
um die vorgegebene Nennleistung nicht zu übersteigen, da es sonst zu Überlastungen und Materialschäden kommen könnte.

Bei Starkwind (12 m/s bis 25 m/s) ist die angebotene Windleistung zu groß und die Anlage muss 
in ihrer Leistungsabgabe begrenzt werden. Die Anlage wird dann „gepitcht“.
Der Pitchwinkel nimmt mit der Windgeschwindigkeit zu (von 0° bis circa 30 °) und die Auftriebskraft wird so beeinflusst, 
dass die Leistungsabgabe der Windenergieanlage konstant bei Nennleistung bleibt.

Quellen: 
- siehe Quelle oben "WindEnergie - Leistungsbegrenzung", und: [WindEnergie - Energieumwandlung](https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/energiewandlung/)
- [Wikipedia - Beaufortskala](https://de.wikipedia.org/wiki/Beaufortskala)

""", unsafe_allow_html=True)
#-------#-------#-------#-------#-------#-------#-------#


st.markdown("""_______________________________________ """)

# get csv file
# filepath = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/df_zamg_21_22.csv')

st.header("Zahl der Tage mit Böen >= 80 km/h")

# Load the data from the CSV file into a Pandas dataframe
df = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/monatl_wdata_v80_2012_2022.csv')

# Convert the Latitude, Longitude, and vv columns to numeric values
df['Latitude'] = pd.to_numeric(df['Latitude'])
df['Longitude'] = pd.to_numeric(df['Longitude'])
df['v80'] = pd.to_numeric(df['v80'])

# Extract the month from the timestamp column and create a new column that contains the month and year in the format YYYY-MM
df['month_year'] = df['time'].apply(lambda x: x[:7])

# Group the data by the month and year and calculate the mean wind speed for each group
wind_speed_by_month = df.groupby('month_year')['v80'].mean()

# Initialize the map
m = leafmap.Map(center=[47.1133, 11.4147], zoom=8)

# Get a list of the unique month and year values in the 'month_year' column
month_year_values = df['month_year'].unique()


def get_selected_month_year_data(selected_month_year):
    # Filter the data to only include rows with the selected month and year
    filtered_df = df[df['month_year'] == selected_month_year]
    return filtered_df


# ---- Date Picker ---- #

selected_month_year = st.selectbox("Wähle Jahr/Monat (beginnend im Jänner 2012):", month_year_values, 
key='windstaerke-datepicker-key')

# Get the selected month and year data
filtered_df = get_selected_month_year_data(selected_month_year)
st.write(f"Derzeitiges Jahr/Monat: {selected_month_year}")

filtered_df = df[df['month_year'] == selected_month_year]

# ---- ********** ---- #

# Create a GeoJSON feature collection for the filtered data
geo_json_data = {
    'type': 'FeatureCollection',
    'features': [{
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['Longitude'], row['Latitude']]
        },
        'properties': {
            'v80': row['v80']
        }
    } for _, row in filtered_df.iterrows()]
}

# Create a heatmap layer from the GeoJSON data and add it to the map

HeatMap(
    filtered_df[["Latitude", "Longitude", "v80"]],
    latitude="Latitude",
    longitude="Longitude",
    value="v80",
    radius=30,
    blur=10,
    gradient= color_dict,
).add_to(folium.FeatureGroup(name="Anzahl Tage mit Windböen >= 80 km/h")).add_to(m)

colors = ['#9e0142', '#cb334d', '#f57245', '#fdbf6f', '#fff2aa', '#eaf79e', 
              '#a4daa4', '#54aead', '#4d65ad', '#5e4fa2']
vmin = 0.0
vmax = 25.0

colormap = cm.LinearColormap(colors=colors, vmin=vmin, vmax=vmax, caption='Anzahl der Tage mit Windböen >= 80 km/h')
m.add_child(colormap)

svg_style = '<style>svg {background-color: white;}</style>'
m.get_root().header.add_child(folium.Element(svg_style))
colormap.add_to(m)

m.to_streamlit(height=700)

st.markdown(""" 
Bei Sturm (ab 25 m/s) ist der Wind so stark, dass die Windenergieanlage abgeschaltet werden muss, 
um eventuelle Schäden zu vermeiden. Der Pitchwinkel ist nahezu 90°; die Blätter sind in Fahnenstellung.

Quelle: [WindEnergie - Widerstands- und Auftriebsläufer ](https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/widerstandlaeufer-auftriebslaeufer/)
""", unsafe_allow_html=True)

st.markdown("""_______________________________________ """)

st.header("Windy - Wind- und Wettervorhersagen in Echtzeit")

st.markdown(""" 
Bei [Windy](https://www.windy.com/?48.171,16.321,5) handelt es sich um eine Wettervorhersage-Plattform, welche Daten wie Temperatur, Windgeschwindigkeit und Niederschlag
visualisiert und animiert. Auf der Webseite kann man noch weitere (kostenlose) Funktionen und Einstellungsmöglichkeiten finden.

Anhand dieser Karte ist sehr gut zu erkennen, wie komplex Wind sich verhält.
Wind wird durch viele Variablen beeinflusst, einschließlich der Temperaturunterschiede in der Atmosphäre, 
der unterschiedlichen Luftdichte in verschiedenen Höhen, der Geographie der Landschaft, der Feuchtigkeit der Luft, 
der Rotation der Erde und vieler anderer Faktoren.
""", unsafe_allow_html=True)

st.markdown(""" 
Die hier eingebetteten Visualisierung der Karte zeigt folgende Daten:

- <strong><span style="color: #FB4724">HOURS</span></strong> <br>
Alle drei Stunden wird die Karte aktualisiert. Beginnend um 1 Uhr morgens, 
kommt das nächste Update somit um 4 Uhr morgens etc. <br>

- <strong><span style="color: #FB4724">TEMPERATURE</span></strong> <br>
Die Temperatur in Grad Celsius <br>

- <strong><span style="color: #FB4724">RAIN</span></strong> <br>
Die Menge an Niederschlag (Regen), gemessen in Millimeter <br>

- <strong><span style="color: #FB4724">WIND</span></strong> 
<br> Die Windstärke in Kilometer pro Stunde <br>

- <strong><span style="color: #FB4724">WIND GUSTS</span></strong> 
<br> Die Windböen in Kilometer pro Stunde <br>

- <strong><span style="color: #FB4724">WIND DIR(ECTION)</span></strong> 
<br> Die jeweilige Windrichtung <br>

Außerdem ist am unteren Rand der Karte eine Legende abgebildet, die farblich erste Hinweise über die Windgeschwindigkeit in 
km/h liefert.
Mithilfe der im rechten oberen Rand befindlichen Zoom-Navigation kann man genauer Orte und Gebiete, durch Herauszoomen aber auch 
die globalen Windströme insgesamt betrachten.
""", unsafe_allow_html=True)

# Set the coordinates and zoom level for the Windy map
lat, lon = 47.1133, 11.4147
zoom = 8.5

# Build the URL for the Windy map with the specified location and zoom
url = f"https://embed.windy.com/?lat={lat}&lon={lon}&zoom={zoom}&level=surface&overlay=wind&menu=&message=&marker=&calendar=&pressure=&type=map&location=coordinates&detail=&detailLat={lat}&detailLon={lon}&metricWind=km%2Fh&metricTemp=%C2%B0C&radarRange=-1"

# Embed the Windy map in Streamlit using an iframe
st.write(f'<iframe src="{url}" width="100%" height="800"></iframe>', unsafe_allow_html=True)
