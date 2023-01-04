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

st.title("Windkarte")

# get csv file
filepath = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/df_zamg_21_22.csv')

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