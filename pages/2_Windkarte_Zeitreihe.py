import streamlit as st
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import pandas as pd
import folium
from folium.plugins import HeatMap
import branca
import branca.colormap as cm

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    Web App URL: <https://geospatial.streamlitapp.com>
    GitHub repository: <https://github.com/giswqs/streamlit-geospatial>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Annina Ecker:
    [GitHub](https://github.com/) | [Mastodon](https://twitter.com/) | [LinkedIn](https://www.linkedin.com/in/)
    """
)

st.title("Windkarte")

# get csv files
data1 = pd.read_csv('/Users/annina/Downloads/monatlicher_datensatz_windricht_windgeschw_202111_202211.csv')
data2 = pd.read_csv('/Users/annina/Downloads/MON Stations-Metadaten.csv')

# rename id-column in data2 to 'station'
data2.rename(columns={"id":"station"}, inplace=True)

# merge the two files on column 'station'
output1 = pd.merge(data1, data2, on='station', how="outer")

output1.drop(['Startdatum', 'Enddatum', 'Sonnenschein', 'Bundesland', 'Globalstrahlung', 'Synop', 'Verknüpfungsnummer', 'Startdatum Teilzeitreihe', 
'Enddatum Teilzeitreihe', 'zusammengesetzt', 'substation', 'Synopstationsnummer'], axis=1, inplace=True)

# rename id-column in data2 to 'station', 'Länge' to 'Longitude, 'Breite' to 'Latitude', and 'Höhe' to 'Height'
output1.rename(columns={"Länge [°E]":"Longitude"}, inplace=True)
output1.rename(columns={"Breite [°N]":"Latitude"}, inplace=True)
output1.rename(columns={"Höhe [m]": "Height"}, inplace=True)

# drop all rows with NaN values
output2 = output1.dropna()

filepath = output2

# tiles ="stamentoner"
m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5)

m.add_heatmap(
      filepath,
      latitude="Latitude",
      longitude="Longitude",
      value="vv", # vv = Windgeschwindigkeit Monatsmittel
      name="Windgeschwindigkeit Monatsmittel",
      radius=20,
      gradient= {
             0.0: '#FFC75F',
             0.25: '#FF9671',
             0.50: '#FF6F91',
             0.75: '#D65DB1',
             1.0: '#845EC2'
         },
  )



colors = ['#FFC75F', '#FF9671', '#FF6F91', '#D65DB1', '#845EC2']
vmin = 0
vmax = 8.5

#m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax, labelsize=10, categorical=True, step=4, background_color='white')

colormap = cm.LinearColormap(colors=colors, vmin=vmin, vmax=vmax, caption='Windgeschwindigkeit (Monatsmittel)')
m.add_child(colormap)

svg_style = '<style>svg {background-color: white;}</style>'
m.get_root().header.add_child(folium.Element(svg_style))
colormap.add_to(m)


m.to_streamlit(height=800)