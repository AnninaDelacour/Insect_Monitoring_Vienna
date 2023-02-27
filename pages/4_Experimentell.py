import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


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

st.markdown("<h1 style='font-size: 60px; color: #FF8066;'>Experimentell</h1>", unsafe_allow_html=True)

# get csv file
# filepath = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/df_zamg_21_22.csv')

st.header("KrigR - Downscaling von Rasterdaten")

st.markdown("""
Im Zuge meiner Bachelorarbeit habe ich versucht, 
Winddaten von [ERA5-Land](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=overview) mithilfe des
[R Packages KrigR](https://github.com/ErikKusch/KrigR) herunterzuskalieren und diese Daten anschließend mit den Wetterstationsdaten zu vergleichen.\n
Da es nicht der Fokus meiner Arbeit ist, diese Daten aufzubereiten und zu bereinigen bzw. deren Signifikanz zu bewerten,
werde ich diese in einem Jupyter Notebook "roh" zur Verfügung stellen.<br>
Somit auch hier der Disclaimer, dass ich keine Fachperson für Windenergie o.ä. bin und lediglich veranschaulichen möchte,
dass man mit deutlich geringerem Aufwand als noch vor zehn Jahren bereits viele Daten heranziehen kann, um sich
ein erstes Bild zur Lage bezüglich Windenergiepotential machen kann.


[Link zum Notebook](https://github.com/AnninaDelacour/bachelor/blob/main/Experimentell.ipynb)
<br>
""", unsafe_allow_html=True)

st.markdown("")

col1, col2 = st.columns(2)

rasterlayer = 'https://bachelor.blob.core.windows.net/newcontainer/rasterlayer.png'
layerraster = 'https://bachelor.blob.core.windows.net/newcontainer/layer_raster.png'

with col1:
    st.image(rasterlayer)

with col2:
    st.image(layerraster)

