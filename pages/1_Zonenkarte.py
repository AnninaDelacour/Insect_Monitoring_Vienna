import streamlit as st
import leafmap.foliumap as leafmap
import folium

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
    Mithilfe des Karten-Layermenüs (Karte: rechts oben) können unterschiedliche Layer ein- und ausgeschaltet werden.
    Dadurch ist es möglich einen Überblick zu erhalten, wo sich in Tirol z.B. Schi- und Umweltschutzgebiete befinden.


    
    Die hier verwendeten Daten wurden von https://data-tiris.opendata.arcgis.com/ erhoben.
    

    """
)



#m = leafmap.Map(tiles="stamenwatercolor", center=[47.1133, 11.4147], zoom=8.5)
m = leafmap.Map(center=[47.1133, 11.4147], zoom=8.5, layer="Swiss Federal Geoportal Map")
m.add_basemap('Stamen.Toner')
#m.add_basemap('BasemapAT.basemap')
# Esri.DeLorme
# SwissFederalGeoportal.NationalMapColor



#csv


#geojson
schigebiet = '/Users/annina/Downloads/URP_Schigebietsgrenzen.geojson'
wald_wild_schutzzonen = '/Users/annina/Downloads/Wald_und_Wildschutzzonen.geojson'
natura_2000_ffh = '/Users/annina/Downloads/Natura_2000_FFH_Richtlinie.geojson'
naturdenkmaeler = '/Users/annina/Downloads/Naturdenkmaeler_Flaeche.geojson'
naturparke = '/Users/annina/Downloads/Naturparke.geojson'
schutzgebiete_umwelt = '/Users/annina/Downloads/Schutzgebiete_Umwelt(1).geojson'
natura_2000_vogelschutz = '/Users/annina/Downloads/Natura_2000_Vogelschutzrichtlinie.geojson'
ramsar = '/Users/annina/Downloads/Ramsar_Gebiete.geojson'


#m.add_geojson(schigebiet, layer_name='Schigebiete')
#m.add_geojson(wald_wild_schutzzonen, layer_name='Wald- und Wildschutzzonen')


folium.GeoJson(
    schigebiet,
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

folium.GeoJson(
    wald_wild_schutzzonen,
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

folium.GeoJson(
    natura_2000_ffh,
    name='Natura 2000 FFH Richtlinie',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Natura 2000 FFH Richtlinie',
        'fillColor': '#ff7d00',
        'fillOpacity': 0.5,
        'color': 'black',
        'weight': 1,
        #dashArray': '5, 5'
    }
).add_to(m)

folium.GeoJson(
    naturdenkmaeler,
    name='Naturdenkmäler',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Naturdenkmäler',
        'fillColor': '#00ffd0',
        'fillOpacity': 0.8,
        'color': 'black',
        'weight': 0.5,
        'dashArray': '1, 1'
    }
).add_to(m)

folium.GeoJson(
    schutzgebiete_umwelt,
    name='Schutzgebiete Umwelt',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Schutzgebiete Umwelt',
        'fillColor': '#821cff',
        'fillOpacity': 0.5,
        'color': 'black',
        'weight': .1,
        'dashArray': '2, 2'
    }
).add_to(m)

folium.GeoJson(
    natura_2000_vogelschutz,
    name='Natura 2000 Vogelschutzrichtlinie',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Natura 2000 Vogelschutzrichtlinie',
        'fillColor': '#ffce00',
        'fillOpacity': 0.4,
        'color': '#ffb700',
        'weight': 0.8,
        'dashArray': '1, 1'
    }
).add_to(m)

folium.GeoJson(
    ramsar,
    name='Ramsar (Feuchtgebiete)',
    show = False,
    style_function=lambda feature: {
        'aliases': 'Ramsar (Feuchtgebiete)',
        'fillColor': '#0d41e1',
        'fillOpacity': 0.7,
        'color': '#00aaff',
        'weight': 0.8,
        'dashArray': '1, 1'
    }
).add_to(m)

# Creating Legend for Map

legend_dict = {
    "Schigebeite": "10e0ff",
    "Wald- und Wildschutzzonen": "01d669",
    "Natura 2000 FFH Richtlinien": "ff7d00",
    "Naturdenkmäler": "00ffd0",
    "Schutzgebiete Umwelt": "ffce00",
    "Natura 2000 Vogelschutzrichtlinie": "ffb700",
    "Ramsar (Feuchtgebiete)": "00aaff",
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