import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

st.title("Experimentell")

# get csv file
# filepath = pd.read_csv('https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/df_zamg_21_22.csv')

st.header("KrigR - Downscaling von Rasterdaten")

st.markdown("""
Im Zuge meiner Bachelorarbeit habe ich versucht, 
Windaten von [ERA5-Land](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=overview) mithilfe des
[R Packages KrigR](https://github.com/ErikKusch/KrigR) herunterzuskalieren und diese Daten anschließend mit den Wetterstationsdaten zu vergleichen.\n
Da es nicht der Fokus meiner Arbeit ist, diese Daten aufzubereiten und zu bereinigen bzw. deren Signifikanz zu bewerten,
werde ich diese in einem Jupyter Notebook "roh" zur Verfügung stellen.<br>
Somit auch hier der Disclaimer, dass ich keine Fachperson für Windenergie o.ä. bin und lediglich veranschaulichen möchte,
dass man mit deutlich geringerem Aufwand als noch vor zehn Jahren bereits viele Daten heranziehen kann, um sich
ein erstes Bild zur Lage bezüglich Windenergiepotential machen kann.

<br>

[Link zum Notebook]()
""", unsafe_allow_html=True)
