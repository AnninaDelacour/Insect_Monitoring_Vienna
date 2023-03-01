import streamlit as st 
from PIL import Image
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
import pandas as pd
import folium
import base64
from config import read_config

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
    GitHub repository: [Annina Delacour](https://github.com/AnninaDelacour/bachelor)
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Annina Ecker: [Mastodon](https://mastodon.world/@aeae) | [LinkedIn](https://www.linkedin.com/in/annina-ecker/)
    """
)

st.markdown("""
<h1 style='font-size: 60px; color: #FF8066;'>Windenergiepotential: <br> Österreich und Tirol im Vergleich</h1>
""", unsafe_allow_html=True)

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
#sql1 = 'SELECT img FROM gwa_images WHERE id = 3'
#cur.execute(sql1, ('data'))
#data = cur.fetchone()[0]
#austria_wind_speed = data.tobytes()

#sql2 = 'SELECT img FROM gwa_images WHERE id = 7'
#cur.execute(sql2, ('data'))
#data = cur.fetchone()[0]
#tirol_wind_speed = data.tobytes()

col1, col2 = st.columns(2)

austria_wind_speed = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/at/gwa3_austria_mean-wind-speed-at-200m.jpg'
tirol_wind_speed = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/tirol/gwa3_tirol_mean-wind-speed.jpg'

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
Ein genaueres Bild der Situation gibt jedoch die Windenergiedichte wieder über die verfügbaren Ressourcen.<br><br>
Wie man im Vergleich zwischen Tirol und gesamt Österreich sehen kann, 
gibt es vor allem in den höher gelegenen Regionen der Alpen
potentiell viele Standorte, um Windräder zur Gewinnung erneuerbarer Energie aufzustellen. 
Auch in tiefer gelegenen Regionen Tirolswäre Potential vorhanden.

Quelle: <https://globalwindatlas.info/en/about/method>
""", unsafe_allow_html=True)

st.markdown("""
_________________________________________________________________
""")

st.header("Durchschnittliche Energiedichte")

austria_power_density = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/at/gwa3_austria_mean-wind-power-density-at-200m.jpg'
tirol_power_density = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/tirol/gwa3_tirol_mean-wind-power-density.jpg'

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
Höhere mittlere Windleistungsdichten weisen auf bessere Windressourcen hin.<br>

Die Energiedichte für ein windreiches Gebiet kann auf verschiedene Arten bestimmt werden.
Eine gängige Methode besteht darin, die Windgeschwindigkeitsdaten für ein bestimmtes Gebiet zu sammeln 
und dann die Leistungsdichte des Winds zu berechnen. Die Leistungsdichte ist definiert als die Energie, 
die pro Zeiteinheit und pro Fläche durch den Windstrom fließt. Diese wird in Watt pro Quadratmeter (W/m²) gemessen.<br>

Die Windgeschwindigkeitsdaten können mithilfe von Windmessmasten oder meteorologischen Satelliten gesammelt werden.
Sobald die Leistungsdichte des Winds für ein bestimmtes Gebiet bestimmt wurde, kann die Energiedichte berechnet werden, indem die Leistungsdichte mit dem Wirkungsgrad eines Windkraftwerks multipliziert wird. 
Der Wirkungsgrad gibt an, wie viel Prozent der Energie des Windstroms in elektrische Energie umgewandelt werden kann. 
Die Energiedichte wird normalerweise in Kilowattstunden pro Quadratmeter pro Jahr (kWh/m²/Jahr) gemessen.<br>

Es ist wichtig zu beachten, dass die Energiedichte für ein windreiches Gebiet nur ein Teil der Bewertung der Eignung für 
die Windenergieerzeugung ist. Andere Faktoren wie die Verfügbarkeit von Stromleitungen und die Genehmigungsprozesse für den 
Bau von Windkraftwerken können auch eine Rolle spielen.<br>

Quelle: [Global Windatlas](https://globalwindatlas.info/en/about/method)
""", unsafe_allow_html=True)

st.markdown("""
_________________________________________________________________
""")

st.header("Roughness - Rauheit eines Geländes")

austria_roughness = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/at/gwa3_austria_roughness.jpg'
tirol_roughness = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/tirol/gwa3_austria_tirol_roughness.jpg'

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

austria_orography = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/at/gwa3_austria_elevation.jpg'
tirol_orography = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/tirol/gwa3_tirol_elevation.jpg'

col7, col8 = st.columns(2)

with col7:
    st.header("Tirol")
    st.image(tirol_orography)

with col8:
    st.header("Österreich")
    st.image(austria_orography)

st.markdown("""
Das Gebiet der Orographie beschäftigt sich mit der Frage, wie Berge, Hügel und Gebirgszüge entstehen,
welche Eigenschaften diese haben und wie sie sich entwickeln.
Dabei wird keine Rücksicht auf genetische oder chronologische Aspekte genommen.

An den meisten Orten der Erde hat die Orographie einen großen Einfluss auf die Windressourcen.
So beeinflussen beispielsweise orografische Merkmale wie Hügel, Täler, Klippen, Steilhänge und Bergrücken den Wind.
In der Nähe des Gipfels, des Kammes von Hügeln und Bergrücken nimmt der Wind zu.
In der Nähe des Fußes von Hügeln und Kämmen sowie in Tälern wird er normalerweise langsamer.

In Gebieten mit hohen Bergen oder hügeligen Landschaften kann der orographische Effekt zu 
sehr unterschiedlichen Windgeschwindigkeiten führen, je nachdem, ob man sich auf der windabgewandten oder 
windzugewandten Seite der Erhebungen befindet. Diese Unterschiede können genutzt werden, um Windkraftanlagen 
strategisch zu platzieren, 
um den maximalen Nutzen aus den höheren Windgeschwindigkeiten zu ziehen.

Quellen:
- [MeteorologieenRot - Orographie](https://www.meteorologiaenred.com/de/Orographie.html)
- [Spektrum der Wissenschaft](https://www.spektrum.de/lexikon/geographie/orographie/5731)
- [Global Windatlas](https://globalwindatlas.info/en/about/method)
""", unsafe_allow_html=True)

st.markdown("""
_________________________________________________________________
""")

st.header("Der Kapzitätsfaktor IEC - Klasse 3")


austria_iec3 = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/at/gwa3_austria_capacity-factor-iec-class-3-1.jpg'
tirol_iec3 = 'https://raw.githubusercontent.com/AnninaDelacour/bachelor/main/gwa_img/tirol/gwa3_tirol_capacity-factor-iec-class-3.jpg'

col9, col10 = st.columns(2)

with col9:
    st.header("Tirol")
    st.image(tirol_iec3)

with col10:
    st.header("Österreich")
    st.image(austria_iec3)

st.markdown("""

Der Kapazitätsfaktor ist ein wichtiger Parameter zur Bewertung der Effizienz einer Windkraftanlage oder eines Windparks.
Der Kapazitätsfaktor gibt das Verhältnis zwischen der tatsächlichen produzierten Energie und der maximalen potenziellen 
Energie an, die die Windkraftanlage oder der Windpark produzieren könnte. <br>

Die IEC-Klasse 3 ist eine Norm, die von der International Electrotechnical Commission (IEC) für 
die Bewertung von Windbedingungen und Windenergieprojekten entwickelt wurde. Die IEC-Klasse 3 bezieht sich auf Gebiete, 
in denen die mittlere Windgeschwindigkeit in 50 Metern Höhe zwischen 6,0 und 6,9 Metern pro Sekunde liegt.<br>

Der Kapazitätsfaktor für eine Windkraftanlage oder einen Windpark der IEC-Klasse 3 hängt von mehreren Faktoren ab, 
wie z.B. der Art der Anlage, der Größe der Rotorblätter, der Höhe des Turms und der Standortbedingungen. 
In der Regel wird der Kapazitätsfaktor für eine Windkraftanlage der IEC-Klasse 3 auf etwa 25-35% geschätzt. 
Das bedeutet, dass eine Windkraftanlage in einem Gebiet der IEC-Klasse 3 etwa 25-35% der maximal möglichen 
Energie produzieren kann.<br>

Der Kapazitätsfaktor ist ein Maß für den jährlichen Energieertrag einer Windkraftanlage.
Höhere Kapazitätsfaktoren bedeuten einen höheren jährlichen Energieertrag.
Beachten werden sollte, dass die Kapazitätsfaktorkarten geschätzte Kapazitätsfaktoren zeigen 
und dass die Eignung des Standorts einer Windkraftanlage gesondert betrachtet werden muss.<br>

Quelle: [Global Windatlas](https://globalwindatlas.info/en/about/method)
""", unsafe_allow_html=True)


st.markdown("""
_________________________________________________________________
""")

kaunertal = 'https://bachelor.blob.core.windows.net/newcontainer/kaunertal.jpeg'


col11, col12 = st.columns(2)

st.write('<style> .text-justify {text-align: justify;} </style>', unsafe_allow_html=True)


with col11:
    st.header("Bedeutung für Tirol")
    st.markdown("""
    <br>
    <p class='text-justify'>Die Alpen sind nicht ein einheitliches Gebirge, sondern haben viele Einschnitte und Lücken, 
    durch die die Luft strömen kann. Diese Lücken können breitere oder schmalere Kanäle bilden, 
    die die Windgeschwindigkeit beeinflussen. Im Allgemeinen beschleunigt sich die Luft, 
    die durch eine Verengung des Geländes strömt, was zu höheren Windgeschwindigkeiten führen kann. 
    Die Alpen liegen fast senkrecht zu den durchschnittlichen Temperaturen, was dazu führt, 
    dass sie Luftmassen mit unterschiedlichen Temperaturen trennen. Dieser Unterschied verursacht einen Druckunterschied, 
    der wiederum die Luft beschleunigt. Aufgrund dieser Faktoren gibt es in den Lücken im Alpenkamm häufig starke Winde. 
    In höheren Regionen über den Lücken sind die Windgeschwindigkeiten ähnlich wie in der freien Atmosphäre. 
    In den kälteren Jahreszeiten können die Winde doppelt so stark sein wie im Sommer.</p>

    <p class='text-justify'>
    Die Windgeschwindigkeiten nehmen in der Regel mit der Höhe zu, 
    dies trifft besonders in Flachlandgebieten oder Offshore-Gebieten (Küstengebiete) zu. Dies ist darauf zurückzuführen, 
    dass die Luft in diesen Gebieten längere Aufwinde und Oberflächenreibung durchläuft, 
    was zu einem steigenden Windprofil mit der Höhe führt. In Berggipfeln ist das nicht der Fall, 
    da dort die Winde ungestört von Oberflächenreibung ankommen und keine lange Aufwindstrecke vorhanden ist, 
    die das Windprofil beeinflussen könnte. Messungen an verschiedenen Berggipfeln in Tirol bestätigen dies.</p>

    <p class='text-justify'>
    Die Alpen beeinflussen die Windgeschwindigkeiten. 
    Die Berge modifizieren die Strömung, so dass breite orographische Rinnen (Täler zwischen Bergen) 
    das größte Windenergiepotential haben und nicht die höchsten Gipfel. 
    Der höchste Bereich dieser Rinnen liegt in der Regel oberhalb 
    von 1,5 km MSL (= Mean Sea Level; Höhe über dem  Meeresspiegel) und diese Rinnen haben oft 
    eine doppelte Struktur in der Vertikalen, mit einem breiteren oberen Teil und einer schmalen Einbuchtung bis zum Talboden. 
    Obwohl die Kosten für die Errichtung und Unterhalt eines Windparks in den Alpen höher sind als im Flachland, 
    sind die Standorte mit dem höchsten Potenzial leichter zugänglich als isolierte Gipfel.</p>

    <p class='text-justify'>
    Die Bewertung des Windenergiepotenzials von Wetterstationen in Tirol *ergab, 
    dass die besten Standorte jene Flachlandstandorte in Ostösterreich und sogar die Offshore-Standorte übertreffen würden!
    Es gibt jedoch begrenzte Flächen, 
    auf denen Anlagen errichtet werden können und Vereisung kann den Jahresertrag beeinträchtigen. 
    Die höchsten Erträge werden auf breiten orographischen Rinnen auf Bergrücken und Gipfeln erzielt 
    und nicht auf isolierten Gipfeln.</p>

    * Studie: [Meteorological wind energy potential in the Alps using ERA40 and wind measurement sites in the Tyrolean Alps](https://onlinelibrary.wiley.com/doi/10.1002/we.436)
    """, unsafe_allow_html=True)

with col12:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.image(kaunertal, width=750)
    st.markdown("""
Image by [manu zoli](https://pixabay.com/users/manuzoli-7012210/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4385430)
""", unsafe_allow_html=True)