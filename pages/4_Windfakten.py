import streamlit as st 
from PIL import Image
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import pandas as pd
import folium

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

st.title("Daten und Zahlen - Österreich und Tirol im Vergleich")


austria_wind_speed_200m = Image.open('/Users/annina/Downloads/gwa3_austria_mean-wind-speed-at-200m.jpg')
tirol_wind_speed_200m = Image.open('/Users/annina/Downloads/gwa3_austria_tirol_mean-wind-speed-at-200m.jpg')

st.markdown("""
Die hier angezeigten Karten wurden vom Global Wind Atlas (<https://globalwindatlas.info/en/area/Austria>) entnommen.
Mit diesem ist es möglich, sich kostenlos und rasch einen Überblick zu verschaffen, wo es geeignete
Zonen in Österreich gibt, welche sich für die Energiegewinnung durch Windkraft eignen.

Weitere Fakten zu Windenergie in Österreich und Tirol sind weiter unten auf der Seite zu finden.
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Durchschnittliche Windgeschwindigkeiten")

col1, col2 = st.columns(2)

with col1:
    st.header("Tirol")
    st.image(tirol_wind_speed_200m)

with col2:
    st.header("Österreich")
    st.image(austria_wind_speed_200m)

global_windatlas_url = "https://globalwindatlas.info/en/area/Austria"

    
st.markdown("""
Die durchschnittliche Windgeschwindigkeit ist ein Maß für die Ressource Wind.
Höhere Geschwindigkeiten sind normalerweise ein Indikator, dass es ausreichend Windressourcen gibt.
Ein genaueres Bild der Situation gibt jedoch die Windenergiedichte wieder über die verfügbaren Ressourcen.
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Durchschnittliche Energiedichte")

austria_power_density_200m = Image.open('/Users/annina/Downloads/gwa3_austria_mean-wind-power-density-at-200m.jpg')
tirol_power_density_200m = Image.open('/Users/annina/Downloads/gwa3_austria_tirol_mean-wind-power-density-at-200m.jpg')

col3, col4 = st.columns(2)

with col3:
    st.header("Tirol")
    st.image(tirol_power_density_200m)

with col4:
    st.header("Österreich")
    st.image(austria_power_density_200m)

st.markdown("""
Geltend für Gebiete ab 200m über dem Boden
Die in den 10% der windreichsten Gebiete Tirols durchschnittliche Energiedichte beträgt 1334 W/m^2. 
""")