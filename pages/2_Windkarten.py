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
from dateutil.relativedelta import relativedelta

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

st.title("Windkarten")

# get csv file
# filepath = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/df_zamg_21_22.csv')

st.header("Windgeschwindigkeit Monatsmittel")

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
m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5)

# Get a list of the unique month and year values in the 'month_year' column
month_year_values = df['month_year'].unique()

@st.cache
def get_selected_month_year_data(selected_month_year):
    # Get the selected month and year from the list of unique values
    selected_month_year_value = month_year_values[int(selected_month_year)]

    # Filter the data to only include rows with the selected month and year
    filtered_df = df[df['month_year'] == selected_month_year_value]
    
    return selected_month_year_value, filtered_df


# Use the st.slider function to create a slider for selecting the month and year
selected_month_year = st.slider("Wähle Jahr/Monat (beginnend im Jänner 2012):", 
0, len(month_year_values) - 1, 0, 1, key='windgeschwindigkeits-slider-key')

# Get the selected month and year data
selected_month_year_value, filtered_df = get_selected_month_year_data(selected_month_year)
st.write(f"Derzeitiges Jahr/Monat: {selected_month_year_value}")

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
    gradient= {
        0.0: '#f7fcfd',
        0.10: '#fff7fb',
        0.20: '#e0ecf4',
        0.30: '#bfd3e6',
        0.40: '#9ebcda',
        0.50: '#8c96c6',
        0.60: '#8c6bb1',
        0.70: '#88419d',
        0.80: '#810f7c',
        0.90: '#4d004b',
        1.0: '#49006a'
    },
).add_to(folium.FeatureGroup(name="Windgeschwindigkeit Monatsmittel")).add_to(m)

colors = ['#f7fcfd', '#fff7fb', '#e0ecf4', '#bfd3e6', '#9ebcda', '#8c96c6', '#8c6bb1', '#88419d', '#810f7c', '#4d004b', '#49006a']
vmin = 0
vmax = 12.4

colormap = cm.LinearColormap(colors=colors, vmin=vmin, vmax=vmax, caption='Windgeschwindigkeit (Monatsmittel) in m/s')
m.add_child(colormap)

svg_style = '<style>svg {background-color: white;}</style>'
m.get_root().header.add_child(folium.Element(svg_style))
colormap.add_to(m)

m.to_streamlit(height=700)

st.markdown(""" Da moderne Windkraftanlagen fast alle nur drei Rotorblätter haben, 
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
- <https://www.stadtwerke-muenster.de/blog/energie/warum-sich-ein-windrad-nicht-immer-dreht/>
- <https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/leistungsbegrenzung/>
""")

#-------#-------#-------#-------#-------#-------#-------#

st.markdown("""_______________________________________ """)

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
m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5)

# Get a list of the unique month and year values in the 'month_year' column
month_year_values = df['month_year'].unique()

@st.cache
def get_selected_month_year_data(selected_month_year):
    # Get the selected month and year from the list of unique values
    selected_month_year_value = month_year_values[int(selected_month_year)]

    # Filter the data to only include rows with the selected month and year
    filtered_df = df[df['month_year'] == selected_month_year_value]
    
    return selected_month_year_value, filtered_df


# Use the st.slider function to create a slider for selecting the month and year
selected_month_year = st.slider("Wähle Jahr/Monat (beginnend im Jänner 2012):", 
0, len(month_year_values) - 1, 0, 1, key='windstaerke-slider-key')

# Get the selected month and year data
selected_month_year_value, filtered_df = get_selected_month_year_data(selected_month_year)
st.write(f"Derzeitiges Jahr/Monat: {selected_month_year_value}")

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
    radius=20,
    gradient= {
        0.0: '#ffffe5',
        0.10: '#fff7bc',
        0.20: '#ffffcc',
        0.30: '#ffeda0',
        0.40: '#fed976',
        0.50: '#feb24c',
        0.60: '#fd8d3c',
        0.70: '#fc4e2a',
        0.80: '#e31a1c',
        0.90: '#bd0026',
        1.0: '#800026'
    },
).add_to(folium.FeatureGroup(name="Windgeschwindigkeit Monatsmittel")).add_to(m)

colors = ['#ffffe5', '#fff7bc', '#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026']
vmin = 1.0
vmax = 26.0

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
- 0 Bft: 0 bis 1 kn | 0 bis 0.2 m/s | 0 bis 1 km/h | Windstille, Flaute
- 1 Bft: 1 bis 4 kn | 0.3 bis 1.5 m/s | 1 bis 5 km/h | leiser Zug
- 2 Bft: 4 bis 6 kn | 1.6 bis 3.3 m/s | 6 bis 11 km/h | leichte Brise
- 3 Bft: 7 bis 10 kn | 3.4 bis 5.4 m/s | 12 bis 19 km/h | schwache Brise
- 4 Bft: 11 bis 15 kn | 5.5 bis 7.9 m/s | 20 bis 28 km/h | mäßige Brise
- 5 Bft: 16 bis 21 kn | 8.0 bis 10.7 m/s | 29 bis 38 km/h | frische Brise, frischer Wind
- 6 Bft: 22 bis 27 kn | 10.8 b is 13.8 m/s | 39 bis 49 km/h | starker Wind
- 7 Bft: 28 bis 33 kn | 13.9 bis 17.1 m/s | 50 bis 61 km/h | steifer Wind
- 8 Bft: 34 bis 40 kn | 17.2 bis 20.7 m/s | 62 bis 74 km/h | stürmischer Wind
- 9 Bft: 41 bis 47 kn | 20.8 bis 24.4 m/s | 75 bis 88 km/h | Sturm
- 10 Bft: 48 bis 55 kn | 24.5 bis 28.4 m/s | 89 bis 102 km/h | schwerer Sturm
- 11 Bft: 56 bis 63 kn | 28.5 bis 32.6 m/s | 103 bis 117 km/h | Orkanartiger Sturm
- 12 Bft: >64 kn | >32.7 m/s | > 118 km/h | Orkan

Üblicherweise wird ab einer Windgeschwindigkeit von rund neun bis zwölf m/s die aus der Auftriebskraft resultierende Rotorleistung durch aerodynamische Maßnahmen begrenzt, 
um die vorgegebene Nennleistung nicht zu übersteigen, da es sonst zu Überlastungen und Materialschäden kommen könnte.

Bei Starkwind (12 m/s bis 25 m/s) ist die angebotene Windleistung zu groß und die Anlage muss 
in ihrer Leistungsabgabe begrenzt werden. Die Anlage wird dann „gepitcht“.
Der Pitchwinkel nimmt mit der Windgeschwindigkeit zu (von 0° bis circa 30 °) und die Auftriebskraft wird so beeinflusst, 
dass die Leistungsabgabe der Windenergieanlage konstant bei Nennleistung bleibt.

Quellen: 
- <https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/leistungsbegrenzung/>
- <https://de.wikipedia.org/wiki/Beaufortskala>

""")

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
m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5)

# Get a list of the unique month and year values in the 'month_year' column
month_year_values = df['month_year'].unique()

@st.cache
def get_selected_month_year_data(selected_month_year):
    # Get the selected month and year from the list of unique values
    selected_month_year_value = month_year_values[int(selected_month_year)]

    # Filter the data to only include rows with the selected month and year
    filtered_df = df[df['month_year'] == selected_month_year_value]
    
    return selected_month_year_value, filtered_df


# Use the st.slider function to create a slider for selecting the month and year
selected_month_year = st.slider("Wähle Jahr/Monat (beginnend im Jänner 2012):", 
0, len(month_year_values) - 1, 0, 1, key='windboen-slider-key')

# Get the selected month and year data
selected_month_year_value, filtered_df = get_selected_month_year_data(selected_month_year)
st.write(f"Derzeitiges Jahr/Monat: {selected_month_year_value}")

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
    radius=25,
    gradient= {
        0.0: '#f7fcfd',
        0.10: '#f7fcf5',
        0.20: '#e0f3db',
        0.30: '#e5f5e0',
        0.40: '#c7e9c0',
        0.50: '#a1d99b',
        0.60: '#74c476',
        0.70: '#41ab5d',
        0.80: '#238b45',
        0.90: '#006d2c',
        1.0: '#00441b'
    },
).add_to(folium.FeatureGroup(name="Anzahl Tage mit Windböen >= 80 km/h")).add_to(m)

colors = ['#f7fcfd', '#f7fcf5', '#e0f3db', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476', '#41ab5d', '#238b45', '#006d2c', '#00441b']
vmin = 1.0
vmax = 22.0

colormap = cm.LinearColormap(colors=colors, vmin=vmin, vmax=vmax, caption='Anzahl der Tage mit Windböen >= 80 km/h')
m.add_child(colormap)

svg_style = '<style>svg {background-color: white;}</style>'
m.get_root().header.add_child(folium.Element(svg_style))
colormap.add_to(m)

m.to_streamlit(height=700)

st.markdown(""" 
Bei Sturm (ab 25 m/s) ist der Wind so stark, dass die Windenergieanlage abgeschaltet werden muss, 
um eventuelle Schäden zu vermeiden. Der Pitchwinkel ist nahezu 90°; die Blätter sind in Fahnenstellung.

Quelle: <https://www.wind-energie.de/themen/anlagentechnik/funktionsweise/leistungsbegrenzung/>
""")