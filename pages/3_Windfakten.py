import streamlit as st 
from PIL import Image
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import pandas as pd
import folium
import psycopg2
import base64
from config import read_config

# Connect to the database
host = read_config('postgresql', 'host')
database = read_config('postgresql', 'database')
user = read_config('postgresql', 'user')
password = read_config('postgresql', 'password')

conn = psycopg2.connect(host=host, database=database, user=user, password=password)


#conn = psycopg2.connect(database='bachelor', user='postgres', password='', host='localhost')
cur = conn.cursor()

st.set_page_config(layout="wide")

st.markdown("""
<style>
p {
    font-size: 18px;
</style>
""", unsafe_allow_html=True)

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

st.title("Daten und Zahlen - Österreich und Tirol im Vergleich")

st.markdown("""
Die hier angezeigten Karten wurden vom Global Wind Atlas (<https://globalwindatlas.info/en/area/Austria>) entnommen.
Mit diesem ist es möglich, sich schnell und kostenlos einen groben Überblick zu verschaffen, wo potentiell geeignete
Zonen zur Energiegewinnung durch Windkraft in Österreich sind.

Weitere Fakten zu Windenergie in Österreich und Tirol sind weiter unten auf der Seite zu finden.
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Durchschnittliche Windgeschwindigkeiten")


# Retrieve BLOB data from the database.
sql1 = 'SELECT img FROM gwa_images WHERE id = 3'
cur.execute(sql1, ('data'))
data = cur.fetchone()[0]
austria_wind_speed = data.tobytes()

sql2 = 'SELECT img FROM gwa_images WHERE id = 7'
cur.execute(sql2, ('data'))
data = cur.fetchone()[0]
tirol_wind_speed = data.tobytes()

col1, col2 = st.columns(2)

with col1:
    st.header("Tirol")
    st.image(tirol_wind_speed)

with col2:
    st.header("Österreich")
    st.image(austria_wind_speed)

global_windatlas_url = "https://globalwindatlas.info/en/area/Austria"

    
st.markdown("""
Die durchschnittliche Windgeschwindigkeit ist ein Maß für die Ressource Wind.
Höhere Geschwindigkeiten sind normalerweise ein Indikator, dass es ausreichend Windressourcen gibt.
Ein genaueres Bild der Situation gibt jedoch die Windenergiedichte wieder über die verfügbaren Ressourcen.

Quelle: <https://globalwindatlas.info/en/about/method>
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Durchschnittliche Energiedichte")

# Retrieve BLOB data from the database.
sql3 = 'SELECT img FROM gwa_images WHERE id = 2'
cur.execute(sql3, ('data'))
data = cur.fetchone()[0]
austria_power_density = data.tobytes()

sql4 = 'SELECT img FROM gwa_images WHERE id = 6'
cur.execute(sql4, ('data'))
data = cur.fetchone()[0]
tirol_power_density = data.tobytes()

col3, col4 = st.columns(2)

with col3:
    st.header("Tirol")
    st.image(tirol_power_density)

with col4:
    st.header("Österreich")
    st.image(austria_power_density)

st.markdown("""
Die in den 10% der windreichsten Gebiete Tirols durchschnittliche Energiedichte beträgt 1549 W/m^2.
Das sind 10,1 m/s, ab einer Höhe von 200m über dem Boden.

Die mittlere Windleistungsdichte ist ein Maß für die Windressourcen.
Höhere mittlere Windleistungsdichten weisen auf bessere Windressourcen hin.

Quelle: <https://globalwindatlas.info/en/about/method>
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Roughness - Rauheit eines Geländes")

# Retrieve BLOB data from the database.
sql5 = 'SELECT img FROM gwa_images WHERE id = 4'
cur.execute(sql5, ('data'))
data = cur.fetchone()[0]
austria_roughness = data.tobytes()

sql6 = 'SELECT img FROM gwa_images WHERE id = 8'
cur.execute(sql6, ('data'))
data = cur.fetchone()[0]
tirol_roughness = data.tobytes()

col5, col6 = st.columns(2)

with col5:
    st.header("Tirol")
    st.image(tirol_roughness)

with col6:
    st.header("Österreich")
    st.image(austria_roughness)

st.markdown("""
Roughness - oder Rauheit ist das Maß der Rauhigkeitslänge von Oberflächen eines Geländes.
Überall auf der Erde hat die Rauheit einen großen Einfluss auf die Windressourcen. 
So bremsen beispielsweise Wälder und Städte den Wind im Vergleich zu kahlen Feldern und Seen.

Die Länge der Oberflächenrauheit ist eine Eigenschaft der Oberfläche, 
mit der sich die Veränderung der horizontalen Windgeschwindigkeit mittels der Höhe bestimmen lässt.
Die Windgeschwindigkeit in einer bestimmten Höhe nimmt mit zunehmender Oberflächenrauheit ab.
Heterogene Oberflächen sind sehr häufig anzutreffen, was das vertikale Windprofil verkompliziert.

Als Faustregel gilt, dass eine Veränderung der Oberflächenrauheit in 100 m Höhe über dem Gelände 
noch 10 km in Windrichtung einen Einfluss auf die Windgeschwindigkeit haben kann.


Quelle: <https://globalwindatlas.info/en/about/method>
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Orographie - Die physische Geographie")

# Retrieve BLOB data from the database.
sql7 = 'SELECT img FROM gwa_images WHERE id = 9'
cur.execute(sql7, ('data'))
data = cur.fetchone()[0]
austria_orography = data.tobytes()

sql8 = 'SELECT img FROM gwa_images WHERE id = 10'
cur.execute(sql8, ('data'))
data = cur.fetchone()[0]
tirol_orography = data.tobytes()

col7, col8 = st.columns(2)

with col7:
    st.header("Tirol")
    st.image(tirol_orography)

with col8:
    st.header("Österreich")
    st.image(austria_orography)

st.markdown("""
Das Gebeiet der Orographie beschäftigt sich mit der Frage, wie Berge, Hügel und Gebirgszüge entstehen,
welche Eigenschaften diese haben und wie sie sich entwickeln.
Dabei wird keine Rücksicht auf genetische oder chronoglische Aspekte genommen.

An den meisten Orten der Erde hat die Orographie einen großen Einfluss auf die Windressourcen.
So beeinflussen beispielsweise orografische Merkmale wie Hügel, Täler, Klippen, Steilhänge und Bergrücken den Wind.
In der Nähe des Gipfels, des Kammes von Hügeln und Bergrücken nimmt der Wind zu.
In der Nähe des Fußes von Hügeln und Kämmen sowie in Tälern wird er normalerweise langsamer.

Quellen:
- <https://www.meteorologiaenred.com/de/Orographie.html>
- <https://www.spektrum.de/lexikon/geographie/orographie/5731>
- <https://globalwindatlas.info/en/about/method>
""")

st.markdown("""
_________________________________________________________________
""")

st.header("Orographie - Die physische Geographie")

# Retrieve BLOB data from the database.
sql9 = 'SELECT img FROM gwa_images WHERE id = 1'
cur.execute(sql9, ('data'))
data = cur.fetchone()[0]
austria_iec3 = data.tobytes()

sql10 = 'SELECT img FROM gwa_images WHERE id = 5'
cur.execute(sql10, ('data'))
data = cur.fetchone()[0]
tirol_iec3 = data.tobytes()

col9, col10 = st.columns(2)

with col9:
    st.header("Tirol")
    st.image(tirol_iec3)

with col10:
    st.header("Österreich")
    st.image(austria_iec3)

st.markdown("""
Der Kapazitätsfaktor ist ein Maß für den jährlichen Energieertrag einer Windkraftanlage.
Höhere Kapazitätsfaktoren bedeuten einen höheren jährlichen Energieertrag.
Beachten werden sollte, dass die Kapazitätsfaktorkarten geschätzte Kapazitätsfaktoren zeigen 
und dass die Eignung des Standorts einer Windkraftanlage gesondert betrachtet werden muss.

Quelle: <https://globalwindatlas.info/en/about/method>
""")

cur.close()
conn.close()

st.markdown("""
_________________________________________________________________
""")

st.header("Bedeutung für Tirol")
st.markdown("""


<br>

Die Alpen sind nicht ein einheitliches Gebirge, sondern haben viele Einschnitte und Lücken, 
durch die die Luft strömen kann. Diese Lücken können breitere oder schmalere Kanäle bilden, 
die die Windgeschwindigkeit beeinflussen. Im Allgemeinen beschleunigt sich die Luft, 
die durch eine Verengung des Geländes strömt, was zu höheren Windgeschwindigkeiten führen kann. 
Die Alpen liegen fast senkrecht zu den durchschnittlichen Temperaturen, was dazu führt, 
dass sie Luftmassen mit unterschiedlichen Temperaturen trennen. Dieser Unterschied verursacht einen Druckunterschied, 
der wiederum die Luft beschleunigt. Aufgrund dieser Faktoren gibt es in den Lücken im Alpenkamm häufig starke Winde. 
In höheren Regionen über den Lücken sind die Windgeschwindigkeiten ähnlich wie in der freien Atmosphäre. 
In den kälteren Jahreszeiten können die Winde doppelt so stark sein wie im Sommer.

Die Windgeschwindigkeiten nehmen in der Regel mit der Höhe zu, 
dies trifft besonders in Flachlandgebieten oder Offshore-Gebieten (Küstengebiete) zu. Dies ist darauf zurückzuführen, 
dass die Luft in diesen Gebieten längere Aufwinde und Oberflächenreibung durchläuft, 
was zu einem steigenden Windprofil mit der Höhe führt. In Berggipfeln ist das nicht der Fall, 
da dort die Winde ungestört von Oberflächenreibung ankommen und keine lange Aufwindstrecke vorhanden ist, 
die das Windprofil beeinflussen könnte. Messungen an verschiedenen Berggipfeln in Tirol bestätigen dies.

Die Alpen beeinflussen die Windgeschwindigkeiten. 
Die Berge modifizieren die Strömung, so dass breite orographische Rinnen (Täler zwischen Bergen) 
das größte Windenergiepotential haben und nicht die höchsten Gipfel. 
Der höchste Bereich dieser Rinnen liegt in der Regel oberhalb 
von 1,5 km MSL (= Mean Sea Level; Höhe über dem  Meeresspiegel) und diese Rinnen haben oft 
eine doppelte Struktur in der Vertikalen, mit einem breiteren oberen Teil und einer schmalen Einbuchtung bis zum Talboden. 
Obwohl die Kosten für die Errichtung und Unterhalt eines Windparks in den Alpen höher sind als im Flachland, 
sind die Standorte mit dem höchsten Potenzial leichter zugänglich als isolierte Gipfel.

Die Bewertung des Windenergiepotenzials von Wetterstationen in Tirol *ergab, 
dass die besten Standorte jene Flachlandstandorte in Ostösterreich und sogar die Offshore-Standorte übertreffen würden!
Es gibt jedoch begrenzte Flächen, 
auf denen Anlagen errichtet werden können und Vereisung kann den Jahresertrag beeinträchtigen. 
Die höchsten Erträge werden auf breiten orographischen Rinnen auf Bergrücken und Gipfeln erzielt 
und nicht auf isolierten Gipfeln.

* Studie: [Meteorological wind energy potential in the Alps using ERA40 and wind measurement sites in the Tyrolean Alps](https://onlinelibrary.wiley.com/doi/10.1002/we.436)
""", unsafe_allow_html=True)

